#!/usr/bin/env python3
"""
snapshot.py — Guarda una foto diaria pequeña (~5 KB) en data/history/AAAA-MM-DD.json.

El deltaLog de CVE List V5 solo cubre 30 días; estas fotos permiten calcular tendencias
de meses (métricas C1, C7 del SPEC) sin volver a descargar todo.

Uso: python3 src/snapshot.py --report data/latest/weekly_report.json --date 2026-10-04 --out data/history
"""
import argparse, json, os


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--report", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--out", default="data/history")
    a = p.parse_args()

    r = json.load(open(a.report))
    s = r["summary"]
    snap = {
        "date": a.date,
        "window_7d": r["window"],
        "sources_status": r["sources_status"],
        "kev": {
            "catalog_version": r["sources_status"].get("kev", {}).get("catalogVersion"),
            "catalog_total": s.get("kev_catalog_total"),
            "added_7d": s.get("kev_added"),
            "added_7d_ids": [k["cveID"] for k in r.get("kev_new", [])],
            "ransomware_known_7d": s.get("kev_ransomware_known"),
            "vendors_7d": s.get("kev_vendors"),
        },
        "cve_7d": {
            "new": s.get("cve_new"), "rejected": s.get("cve_rejected"), "updated": s.get("cve_updated"),
            "by_severity": s.get("cve_by_severity"), "with_cvss_pct": s.get("cve_with_cvss_pct"),
            "ssvc_poc_or_active": s.get("ssvc_poc_or_active"),
            "ssvc_automatable_total_impact": s.get("ssvc_automatable_total_impact"),
            "epss_ge_10pct": s.get("epss_ge_10pct"),
            "top_vendors": s.get("top_vendors", [])[:10],
            "top_cwe": s.get("top_cwe", [])[:10],
        },
    }
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, f"{a.date}.json")
    json.dump(snap, open(path, "w"), ensure_ascii=False, indent=1)
    print("snapshot:", path)


if __name__ == "__main__":
    main()
