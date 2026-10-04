#!/usr/bin/env python3
"""
build_dashboard_data.py — Genera dashboard_data.json para el tablero HTML y lo inyecta en la plantilla.

Fuentes: CVE List V5 (deltaLog, 30 días) + CISA KEV (repo oficial cisagov/kev-data; respaldo cisa.gov)
         + EPSS (opcional, si hay acceso a api.first.org).
Reutiliza las funciones de collector.py.

Uso:
  python3 src/build_dashboard_data.py --end 2026-10-04 --days 30 \
      --template src/dashboard_template.html --out site/index.html --data-out site/dashboard_data.json
"""
from __future__ import annotations
import argparse, json, os, datetime as dt
from collections import Counter, defaultdict
import collector as C

EDGE_HINTS = ["netscaler", "citrix adc", "gateway", "vpn", "fortigate", "fortios", "fortimail", "fortiweb",
              "pan-os", "globalprotect", "asa", "firepower", "sd-wan", "ivanti connect", "pulse", "sonicwall",
              "sma", "big-ip", "f5", "firewall", "router", "routeros", "edge", "secure access", "junos",
              "check point", "zyxel", "draytek", "esxi", "vcenter", "exchange", "sharepoint"]


def is_edge(v: dict) -> bool:
    s = f"{v.get('vendorProject','')} {v.get('product','')}".lower()
    return any(h in s for h in EDGE_HINTS)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--end", default=str(dt.date.today()))
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--week", type=int, default=7)
    p.add_argument("--utc-offset", type=int, default=-3)
    p.add_argument("--template", default="dashboard_template.html")
    p.add_argument("--out", default="dashboard.html")
    p.add_argument("--data-out", default="out/dashboard_data.json")
    p.add_argument("--default-watch", default=os.environ.get("WATCHLIST_DEFAULT", ""),
                   help="lista por defecto de 'Mis tecnologías' en el tablero (público si se publica)")
    a = p.parse_args()

    tz = dt.timezone(dt.timedelta(hours=a.utc_offset))
    end = dt.date.fromisoformat(a.end)
    start = end - dt.timedelta(days=a.days - 1)
    wstart = end - dt.timedelta(days=a.week - 1)
    s_utc = dt.datetime.combine(start, dt.time.min, tz).astimezone(dt.timezone.utc)
    e_utc = dt.datetime.combine(end, dt.time.max, tz).astimezone(dt.timezone.utc)
    status = {}

    # ---- CVE (30 días)
    new, upd = C.cves_in_window(s_utc, e_utc)
    recs = [r for r in C.fetch_records(new) if "error" not in r and r.get("state") != "REJECTED"]
    status["cvelist"] = {"ok": True, "records": len(recs)}

    def local_day(iso):
        if not iso:
            return None
        t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=dt.timezone.utc)
        return t.astimezone(tz).date()

    days = [start + dt.timedelta(days=i) for i in range(a.days)]
    daily = {d: Counter() for d in days}
    week_cves = []
    for r in recs:
        d = local_day(r.get("date_published"))
        if d is None or d < start or d > end:
            continue
        b = C.sev_bucket(r)
        daily[d][b] += 1
        daily[d]["total"] += 1
        ss = r.get("ssvc") or {}
        if ss.get("exploitation") in ("poc", "active"):
            daily[d]["ssvc_exp"] += 1
        week_cves.append({
            "id": r["cve_id"], "d": str(d), "v": (r.get("vendor") or "n/d").strip()[:60],
            "p": (r.get("product") or "")[:80], "s": r["cvss"]["score"] if r.get("cvss") else None,
            "sev": b, "cwe": (r.get("cwe") or [None])[0], "x": ss.get("exploitation"),
            "au": ss.get("automatable"), "ti": ss.get("technical_impact"), "cna": r.get("assigner"),
        })

    # ---- KEV
    kev, src = C.load_kev(None)
    status["kev"] = {"ok": True, "source": src, "catalogVersion": kev.get("catalogVersion"), "count": kev.get("count")}
    kv = kev["vulnerabilities"]
    kev_daily = Counter(v["dateAdded"] for v in kv)
    # semanas ISO últimas 52
    weeks = []
    wk_end = end
    for i in range(52):
        we = wk_end - dt.timedelta(days=7 * i)
        ws = we - dt.timedelta(days=6)
        sel = [v for v in kv if ws <= dt.date.fromisoformat(v["dateAdded"]) <= we]
        weeks.append({"start": str(ws), "end": str(we), "n": len(sel),
                      "edge": sum(1 for v in sel if is_edge(v)),
                      "ransom": sum(1 for v in sel if v.get("knownRansomwareCampaignUse") == "Known")})
    weeks.reverse()
    kev_week = [v for v in kv if start <= dt.date.fromisoformat(v["dateAdded"]) <= end]
    for v in kev_week:
        v["edge"] = is_edge(v)
    last365 = [v for v in kv if dt.date.fromisoformat(v["dateAdded"]) > end - dt.timedelta(days=365)]
    kev_vendors_365 = Counter(v["vendorProject"] for v in last365).most_common(12)
    deadline_days = [(dt.date.fromisoformat(v["dueDate"]) - dt.date.fromisoformat(v["dateAdded"])).days for v in last365]

    # ---- EPSS (opcional)
    epss = {}
    try:
        epss = C.epss_for([c["id"] for c in week_cves] + [v["cveID"] for v in kev_week])
        status["epss"] = {"ok": True, "scored": len(epss)}
    except Exception as e:
        status["epss"] = {"ok": False, "error": str(e)[:120]}
    for c in week_cves:
        if c["id"] in epss:
            c["e"] = epss[c["id"]]["epss"]
    for v in kev_week:
        if v["cveID"] in epss:
            v["epss"] = epss[v["cveID"]]["epss"]

    data = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"),
        "window": {"start": str(start), "end": str(end), "week_start": str(wstart)},
        "sources_status": status,
        "daily": [{"d": str(d), **{k: daily[d].get(k, 0) for k in ("total", "CRITICAL", "HIGH", "MEDIUM", "LOW", "SIN_CVSS", "ssvc_exp")},
                   "kev": kev_daily.get(str(d), 0)} for d in days],
        "kev_weeks": weeks,
        "kev_recent": kev_week,
        "kev_total": len(kv),
        "kev_vendors_365": kev_vendors_365,
        "kev_365": {"n": len(last365), "ransom": sum(1 for v in last365 if v.get("knownRansomwareCampaignUse") == "Known"),
                    "edge": sum(1 for v in last365 if is_edge(v)),
                    "deadline_hist": sorted(Counter(deadline_days).items())},
        "cves": week_cves,
        "cves_updated_30d": len(upd),
    }
    os.makedirs(os.path.dirname(a.data_out) or ".", exist_ok=True)
    json.dump(data, open(a.data_out, "w"), ensure_ascii=False, separators=(",", ":"))
    html = (open(a.template).read()
            .replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
            .replace('/*__WATCH__*/""', json.dumps(a.default_watch, ensure_ascii=False)))
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    open(a.out, "w").write(html)
    print(json.dumps(status), len(week_cves), "CVE detalle;", sum(x["total"] for x in data["daily"]), "CVE 30d")


if __name__ == "__main__":
    main()
