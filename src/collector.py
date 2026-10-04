#!/usr/bin/env python3
"""
collector.py — Recolector semanal de vulnerabilidades (herramienta para agente IA).

Fuentes (todas gratuitas y estructuradas):
  - CISA KEV (JSON, repo oficial cisagov/kev-data; respaldo cisa.gov) -> explotación confirmada
  - CVE List V5 / deltaLog.json (GitHub)    -> CVE nuevos/actualizados + CVSS, CWE,
                                               y enriquecimiento CISA ADP (SSVC, CVSS, CWE)
  - FIRST EPSS API                          -> probabilidad de explotación 30 días
Opcional: NVD API 2.0 (requiere API key para buen rendimiento).

Uso:
  python3 collector.py --start 2026-09-27 --end 2026-10-04 --out out/
  python3 collector.py --days 7 --kev-file kev.json --no-epss

Salida:
  out/weekly_report.json  (contrato estable para el agente; ver schema en spec)
  out/weekly_report.md    (resumen legible)

Diseño: cada fuente falla de forma aislada; el reporte registra en `sources_status`
qué se pudo obtener, para que el agente sepa qué métricas son confiables.
"""
from __future__ import annotations
import argparse, json, os, sys, time, datetime as dt
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import urllib.request, urllib.error

# KEV: se consume desde el repositorio oficial de CISA en GitHub (cisagov/kev-data).
# CISA declara que el propósito del repo es facilitar el consumo programático y que se
# sincroniza "within minutes" con la fuente canónica en cisa.gov. cisa.gov queda como respaldo.
KEV_URLS = [
    "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json",
]
CVE_DELTALOG_URL = "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json"
EPSS_URL = "https://api.first.org/data/v1/epss?cve={}"
UA = {"User-Agent": "vuln-weekly-collector/1.0"}


def http_json(url: str, timeout: int = 60, retries: int = 2):
    last = None
    for i in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except Exception as e:  # noqa
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


# ---------------------------------------------------------------- KEV
def load_kev(kev_file: str | None):
    if kev_file:
        return json.load(open(kev_file)), f"file:{kev_file}"
    errors = []
    for url in KEV_URLS:
        try:
            return http_json(url), url
        except Exception as e:  # noqa
            errors.append(f"{url}: {str(e)[:80]}")
    raise RuntimeError(" | ".join(errors))


def kev_in_window(kev: dict, start: dt.date, end: dt.date):
    out = []
    for v in kev.get("vulnerabilities", []):
        d = dt.date.fromisoformat(v["dateAdded"])
        if start <= d <= end:
            out.append(v)
    return sorted(out, key=lambda v: v["dateAdded"])


# ---------------------------------------------------------------- CVE List V5
def cves_in_window(start_utc: dt.datetime, end_utc: dt.datetime):
    log = http_json(CVE_DELTALOG_URL, timeout=180)
    new, upd = {}, {}
    for e in log:
        t = dt.datetime.fromisoformat(e["fetchTime"].replace("Z", "+00:00"))
        if start_utc <= t <= end_utc:
            for n in e.get("new", []):
                new[n["cveId"]] = n
            for u in e.get("updated", []):
                upd[u["cveId"]] = u
    for k in new:
        upd.pop(k, None)
    return new, upd


def _cvss_from_metrics(metrics):
    best = None
    for m in metrics or []:
        for key in ("cvssV4_0", "cvssV3_1", "cvssV3_0", "cvssV2_0"):
            if key in m:
                s = m[key].get("baseScore")
                sev = m[key].get("baseSeverity")
                if s is not None and (best is None or key > best["version"]):
                    best = {"version": key, "score": s, "severity": sev,
                            "vector": m[key].get("vectorString")}
    return best


def parse_cve_record(rec: dict) -> dict:
    meta = rec.get("cveMetadata", {})
    cna = rec.get("containers", {}).get("cna", {})
    adps = rec.get("containers", {}).get("adp", []) or []
    desc = next((d["value"] for d in cna.get("descriptions", []) if d.get("lang", "").startswith("en")), "")
    aff = cna.get("affected", []) or []
    vendor = aff[0].get("vendor") if aff else None
    product = aff[0].get("product") if aff else None
    cwes = set()
    for pt in cna.get("problemTypes", []) or []:
        for d in pt.get("descriptions", []):
            if d.get("cweId"):
                cwes.add(d["cweId"])
    cvss = _cvss_from_metrics(cna.get("metrics"))
    ssvc = None
    for a in adps:
        if not cvss:
            cvss = _cvss_from_metrics(a.get("metrics"))
        for pt in a.get("problemTypes", []) or []:
            for d in pt.get("descriptions", []):
                if d.get("cweId"):
                    cwes.add(d["cweId"])
        for m in a.get("metrics", []) or []:
            other = m.get("other", {})
            if other.get("type") == "ssvc":
                opts = {}
                for o in other.get("content", {}).get("options", []):
                    opts.update(o)
                ssvc = {"exploitation": opts.get("Exploitation"),
                        "automatable": opts.get("Automatable"),
                        "technical_impact": opts.get("Technical Impact")}
    return {
        "cve_id": meta.get("cveId"),
        "state": meta.get("state"),
        "assigner": meta.get("assignerShortName"),
        "date_published": meta.get("datePublished"),
        "vendor": vendor, "product": product,
        "cvss": cvss, "cwe": sorted(cwes), "ssvc": ssvc,
        "description": desc[:400],
    }


def fetch_records(entries: dict, workers: int = 24):
    def one(item):
        try:
            return parse_cve_record(http_json(item["githubLink"], timeout=30, retries=1))
        except Exception as e:  # noqa
            return {"cve_id": item["cveId"], "error": str(e)[:120]}
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(one, entries.values()))


# ---------------------------------------------------------------- EPSS
def epss_for(cve_ids: list[str]):
    res = {}
    for i in range(0, len(cve_ids), 100):
        chunk = ",".join(cve_ids[i:i + 100])
        data = http_json(EPSS_URL.format(chunk))
        for r in data.get("data", []):
            res[r["cve"]] = {"epss": float(r["epss"]), "percentile": float(r["percentile"])}
    return res


# ---------------------------------------------------------------- Report
def sev_bucket(c):
    if not c.get("cvss"):
        return "SIN_CVSS"
    s = c["cvss"]["score"]
    return "CRITICAL" if s >= 9 else "HIGH" if s >= 7 else "MEDIUM" if s >= 4 else "LOW"


def build(args):
    if args.days:
        end = dt.date.fromisoformat(args.end) if args.end else dt.date.today()
        start = end - dt.timedelta(days=args.days - 1)
    else:
        start, end = dt.date.fromisoformat(args.start), dt.date.fromisoformat(args.end)
    tz = dt.timezone(dt.timedelta(hours=args.utc_offset))
    start_utc = dt.datetime.combine(start, dt.time.min, tz).astimezone(dt.timezone.utc)
    end_utc = dt.datetime.combine(end, dt.time.max, tz).astimezone(dt.timezone.utc)

    status, report = {}, {"window": {"start": str(start), "end": str(end), "utc_offset": args.utc_offset},
                          "generated_at": dt.datetime.now(dt.timezone.utc).isoformat()}

    # KEV
    kev_new, kev_total = [], None
    try:
        kev, src = load_kev(args.kev_file)
        kev_total = kev.get("count") or len(kev.get("vulnerabilities", []))
        kev_new = kev_in_window(kev, start, end)
        status["kev"] = {"ok": True, "source": src, "catalogVersion": kev.get("catalogVersion")}
    except Exception as e:
        status["kev"] = {"ok": False, "error": str(e)[:200]}

    # CVE List
    records, upd_count = [], 0
    try:
        new, upd = cves_in_window(start_utc, end_utc)
        upd_count = len(upd)
        records = fetch_records(new) if not args.no_records else [{"cve_id": k} for k in new]
        status["cvelist"] = {"ok": True, "source": CVE_DELTALOG_URL,
                             "fetched": sum(1 for r in records if "error" not in r),
                             "errors": sum(1 for r in records if "error" in r)}
    except Exception as e:
        status["cvelist"] = {"ok": False, "error": str(e)[:200]}

    # EPSS
    epss = {}
    if not args.no_epss:
        try:
            ids = [r["cve_id"] for r in records] + [k["cveID"] for k in kev_new]
            epss = epss_for(sorted(set(ids)))
            status["epss"] = {"ok": True, "scored": len(epss)}
        except Exception as e:
            status["epss"] = {"ok": False, "error": str(e)[:200]}
    else:
        status["epss"] = {"ok": False, "error": "deshabilitado (--no-epss)"}

    for r in records:
        if r.get("cve_id") in epss:
            r["epss"] = epss[r["cve_id"]]
    for k in kev_new:
        if k["cveID"] in epss:
            k["epss"] = epss[k["cveID"]]

    ok = [r for r in records if "error" not in r and r.get("state") != "REJECTED"]
    rejected = [r for r in records if r.get("state") == "REJECTED"]
    sev = Counter(sev_bucket(r) for r in ok)
    vendors = Counter((r.get("vendor") or "n/d").strip() for r in ok)
    cwes = Counter(c for r in ok for c in r.get("cwe", []))
    cnas = Counter(r.get("assigner") for r in ok)
    ssvc_auto = [r for r in ok if (r.get("ssvc") or {}).get("automatable") == "yes"
                 and (r.get("ssvc") or {}).get("technical_impact") == "total"]
    ssvc_poc_active = [r for r in ok if (r.get("ssvc") or {}).get("exploitation") in ("poc", "active")]
    crit = sorted([r for r in ok if r.get("cvss") and r["cvss"]["score"] >= 9.0],
                  key=lambda r: (-r["cvss"]["score"], r["cve_id"]))
    high_epss = sorted([r for r in ok if r.get("epss", {}).get("epss", 0) >= 0.1],
                       key=lambda r: -r["epss"]["epss"])

    kev_vendors = Counter(k["vendorProject"] for k in kev_new)
    report.update({
        "sources_status": status,
        "summary": {
            "kev_added": len(kev_new),
            "kev_catalog_total": kev_total,
            "kev_ransomware_known": sum(1 for k in kev_new if k.get("knownRansomwareCampaignUse") == "Known"),
            "kev_vendors": dict(kev_vendors.most_common()),
            "cve_new": len(ok), "cve_rejected": len(rejected), "cve_updated": upd_count,
            "cve_by_severity": dict(sev),
            "cve_with_cvss_pct": round(100 * (1 - sev.get("SIN_CVSS", 0) / max(len(ok), 1)), 1),
            "ssvc_poc_or_active": len(ssvc_poc_active),
            "ssvc_automatable_total_impact": len(ssvc_auto),
            "epss_ge_10pct": len(high_epss),
            "top_vendors": vendors.most_common(15),
            "top_cwe": cwes.most_common(10),
            "top_cna": cnas.most_common(10),
        },
        "kev_new": kev_new,
        "critical_cves": crit[:args.top],
        "ssvc_poc_or_active": ssvc_poc_active[:args.top],
        "high_epss": high_epss[:args.top],
    })
    if args.include_all:
        report["all_new_cves"] = ok
    return report


def to_md(rep: dict) -> str:
    s, w = rep["summary"], rep["window"]
    L = [f"# Reporte semanal de vulnerabilidades — {w['start']} a {w['end']}", "",
         "## Resumen", "",
         f"- KEV agregadas: **{s['kev_added']}** (catálogo total: {s['kev_catalog_total']}; ransomware conocido: {s['kev_ransomware_known']})",
         f"- CVE nuevos publicados: **{s['cve_new']}** (rechazados: {s['cve_rejected']}; registros actualizados: {s['cve_updated']})",
         f"- Por severidad CVSS: {s['cve_by_severity']}  — con CVSS: {s['cve_with_cvss_pct']}%",
         f"- SSVC (CISA ADP) explotación PoC/activa: {s['ssvc_poc_or_active']}; automatizable + impacto total: {s['ssvc_automatable_total_impact']}",
         f"- EPSS ≥ 10%: {s['epss_ge_10pct']}", "", "## KEV agregadas en la semana", "",
         "| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |",
         "|---|---|---|---|---|---|"]
    for k in rep["kev_new"]:
        L.append(f"| {k['dateAdded']} | {k['cveID']} | {k['vendorProject']} {k['product']} | {k['vulnerabilityName']} | {k['dueDate']} | {k.get('knownRansomwareCampaignUse','')} |")
    L += ["", "## CVE críticos (CVSS ≥ 9.0) publicados", "", "| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |", "|---|---|---|---|---|---|"]
    for r in rep["critical_cves"]:
        L.append(f"| {r['cve_id']} | {r['cvss']['score']} | {r.get('vendor') or ''} | {(r.get('product') or '')[:40]} | {','.join(r.get('cwe', [])[:2])} | {(r.get('ssvc') or {}).get('exploitation') or ''} |")
    L += ["", "## Top proveedores (CVE nuevos)", ""] + [f"- {v}: {n}" for v, n in rep["summary"]["top_vendors"][:10]]
    L += ["", "## Top CWE", ""] + [f"- {c}: {n}" for c, n in rep["summary"]["top_cwe"]]
    L += ["", "## Estado de fuentes", "", "```json", json.dumps(rep["sources_status"], indent=2, ensure_ascii=False), "```"]
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--start"); p.add_argument("--end")
    p.add_argument("--days", type=int)
    p.add_argument("--utc-offset", type=int, default=-3, help="zona horaria del reporte (Chile = -3/-4)")
    p.add_argument("--kev-file", help="usar KEV local en vez de descargar")
    p.add_argument("--no-epss", action="store_true")
    p.add_argument("--no-records", action="store_true", help="no descargar cada registro CVE")
    p.add_argument("--include-all", action="store_true", help="incluir todos los CVE nuevos en el JSON")
    p.add_argument("--top", type=int, default=40)
    p.add_argument("--out", default="out")
    a = p.parse_args()
    if not a.days and not (a.start and a.end):
        a.days = 7
    rep = build(a)
    os.makedirs(a.out, exist_ok=True)
    json.dump(rep, open(os.path.join(a.out, "weekly_report.json"), "w"), indent=2, ensure_ascii=False)
    open(os.path.join(a.out, "weekly_report.md"), "w").write(to_md(rep))
    print(json.dumps(rep["sources_status"], ensure_ascii=False))
    print(json.dumps({k: v for k, v in rep["summary"].items() if not k.startswith("top")}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
