# Reporte semanal de vulnerabilidades — 2026-10-31 a 2026-11-06

## Resumen

- KEV agregadas: **2** (catálogo total: 1768; ransomware conocido: 0)
- CVE nuevos publicados: **2607** (rechazados: 251; registros actualizados: 9296)
- Por severidad CVSS: {'HIGH': 961, 'LOW': 137, 'MEDIUM': 1037, 'CRITICAL': 236, 'SIN_CVSS': 236}  — con CVSS: 90.9%
- SSVC (CISA ADP) explotación PoC/activa: 204; automatizable + impacto total: 72
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-03 | CVE-2026-119977 | WordPress WordPress Core | WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability | 2026-11-06 | Unknown |
| 2026-11-04 | CVE-2024-27834 | Apple Multiple Products | Apple Multiple Products Improper Authentication Vulnerability | 2026-11-18 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-120189 | 10 | D-Link | DIR-505 | CWE-119,CWE-121 | poc |
| CVE-2026-120195 | 10 | WAVLINK | WL-WN579A3-A | CWE-77,CWE-78 | poc |
| CVE-2026-120198 | 10 | WAVLINK | WL-WN530BE1-A | CWE-74,CWE-77 | poc |
| CVE-2026-120276 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 | poc |
| CVE-2026-120277 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 |  |
| CVE-2026-120279 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 | poc |
| CVE-2026-120280 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 | poc |
| CVE-2026-120281 | 10 | WAVLINK | WN536AX6-A | CWE-119,CWE-121 |  |
| CVE-2026-120283 | 10 | Linksys | E8450 | CWE-119,CWE-121 | none |
| CVE-2026-120338 | 10 | PrefectHQ | prefab-ui | CWE-269,CWE-693 | none |
| CVE-2026-120344 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 | poc |
| CVE-2026-120345 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 | poc |
| CVE-2026-121489 | 10 | Apache Software Foundation | Apache Juneau | CWE-22 |  |
| CVE-2026-121606 | 10 | Qihoo 360 | D621-2 | CWE-345,CWE-347 |  |
| CVE-2026-121607 | 10 | Qihoo 360 | D603-2 | CWE-77,CWE-78 |  |
| CVE-2026-121609 | 10 | Qihoo 360 | Whole Home Router M5 | CWE-259,CWE-798 |  |
| CVE-2026-121615 | 10 | Linksys | E5600 | CWE-287 |  |
| CVE-2026-121932 | 10 | Linksys | E5350 | CWE-77,CWE-78 |  |
| CVE-2026-121933 | 10 | Linksys | E5350 | CWE-287,CWE-306 |  |
| CVE-2026-122013 | 10 | Comfast | CF-WR632AX | CWE-22 |  |
| CVE-2026-122051 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-73098 | 10 | Apache Software Foundation | Apache Juneau | CWE-470 | none |
| CVE-2026-73099 | 10 | Apache Software Foundation | Apache Juneau | CWE-352 | none |
| CVE-2026-73100 | 10 | Apache Software Foundation | Apache Juneau | CWE-532 |  |
| CVE-2026-73101 | 10 | Apache Software Foundation | Apache Juneau | CWE-209 |  |
| CVE-2026-73116 | 10 | Apache Software Foundation | Apache Juneau | CWE-522 |  |
| CVE-2026-73117 | 10 | Apache Software Foundation | Apache Juneau | CWE-113 |  |
| CVE-2026-96677 | 10 | Apache Software Foundation | Apache Juneau | CWE-79 |  |
| CVE-2026-111489 | 9.9 | TPC Software | Matchpoint |  |  |
| CVE-2026-111490 | 9.9 | TPC Software | Matchpoint | CWE-639 |  |
| CVE-2026-120306 | 9.9 | beam-cloud | Beta9 worker | CWE-269,CWE-653 | none |
| CVE-2026-120307 | 9.9 | beam-cloud | Beta9 worker | CWE-22,CWE-23 | none |
| CVE-2026-120308 | 9.9 | beam-cloud | Beta9 gateway | CWE-22,CWE-668 | none |
| CVE-2026-28336 | 9.9 | SolarWinds | Dameware | CWE-20 | none |
| CVE-2026-71550 | 9.9 | SuiteCRM | SuiteCRM | CWE-98 |  |
| CVE-2026-97693 | 9.9 | xerrors | Yuxi | CWE-284,CWE-522 |  |
| CVE-2026-100109 | 9.8 | Unknown | Security For WooCommerce | CWE-862 | none |
| CVE-2026-102435 | 9.8 | themefic | Ultra Addons for Contact Form 7 | CWE-502 | none |
| CVE-2026-102895 | 9.8 | gpustack | gpustack | CWE-287,CWE-290 | none |

## Top proveedores (CVE nuevos)

- Google: 354
- Apache Software Foundation: 119
- Unknown: 117
- JetBrains: 89
- Hewlett Packard Enterprise (HPE): 56
- MediaTek, Inc.: 56
- Red Hat: 47
- n/d: 44
- Linux: 44
- FreeRDP: 42

## Top CWE

- CWE-79: 209
- CWE-862: 179
- CWE-863: 111
- CWE-787: 93
- CWE-639: 90
- CWE-22: 90
- CWE-416: 87
- CWE-200: 84
- CWE-89: 79
- CWE-125: 67

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.04"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2858,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2366
  }
}
```