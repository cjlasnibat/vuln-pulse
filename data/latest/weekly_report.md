# Reporte semanal de vulnerabilidades — 2026-10-29 a 2026-11-04

## Resumen

- KEV agregadas: **5** (catálogo total: 1767; ransomware conocido: 0)
- CVE nuevos publicados: **2870** (rechazados: 31; registros actualizados: 8404)
- Por severidad CVSS: {'HIGH': 996, 'MEDIUM': 1072, 'SIN_CVSS': 410, 'CRITICAL': 270, 'LOW': 122}  — con CVSS: 85.7%
- SSVC (CISA ADP) explotación PoC/activa: 204; automatizable + impacto total: 107
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-29 | CVE-2026-97229 | GitLab Community Edition and Enterprise Edition | GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability | 2026-11-01 | Unknown |
| 2026-10-29 | CVE-2026-76418 | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability | 2026-11-01 | Unknown |
| 2026-10-30 | CVE-2026-118527 | Ivanti Connect Secure | Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability | 2026-11-13 | Unknown |
| 2026-10-30 | CVE-2026-111357 | Ivanti Connect Secure | Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability | 2026-11-02 | Unknown |
| 2026-11-03 | CVE-2026-119977 | WordPress WordPress Core | WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability | 2026-11-06 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-112816 | 10 | Canonical | LXD | CWE-295 | none |
| CVE-2026-120189 | 10 | D-Link | DIR-505 | CWE-119,CWE-121 |  |
| CVE-2026-120195 | 10 | WAVLINK | WL-WN579A3-A | CWE-77,CWE-78 |  |
| CVE-2026-120198 | 10 | WAVLINK | WL-WN530BE1-A | CWE-74,CWE-77 | poc |
| CVE-2026-120276 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 |  |
| CVE-2026-120277 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 |  |
| CVE-2026-120279 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 | poc |
| CVE-2026-120280 | 10 | WAVLINK | WN536AX6-A | CWE-77,CWE-78 |  |
| CVE-2026-120281 | 10 | WAVLINK | WN536AX6-A | CWE-119,CWE-121 |  |
| CVE-2026-120283 | 10 | Linksys | E8450 | CWE-119,CWE-121 | none |
| CVE-2026-120338 | 10 | PrefectHQ | prefab-ui | CWE-269,CWE-693 | none |
| CVE-2026-120344 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 | poc |
| CVE-2026-120345 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 |  |
| CVE-2026-121606 | 10 | Qihoo 360 | D621-2 | CWE-345,CWE-347 |  |
| CVE-2026-121607 | 10 | Qihoo 360 | D603-2 | CWE-77,CWE-78 |  |
| CVE-2026-121609 | 10 | Qihoo 360 | Whole Home Router M5 | CWE-259,CWE-798 |  |
| CVE-2026-121615 | 10 | Linksys | E5600 | CWE-287 |  |
| CVE-2026-61738 | 10 | socfortress | CoPilot | CWE-22,CWE-434 |  |
| CVE-2026-61826 | 10 | morpheus65535 | bazarr | CWE-352,CWE-862 |  |
| CVE-2026-61991 | 10 | Ajax Load More | AjaxLoadMore Cache | CWE-94 | none |
| CVE-2026-84295 | 10 | Progress Software | WS_FTP Server | CWE-287,CWE-522 | none |
| CVE-2026-107327 | 9.9 | IBM | Langflow OSS | CWE-862 | none |
| CVE-2026-107328 | 9.9 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-107329 | 9.9 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-113617 | 9.9 | Unknown | Automated Import Products to Cart | CWE-22 | none |
| CVE-2026-120306 | 9.9 | beam-cloud | Beta9 worker | CWE-269,CWE-653 | none |
| CVE-2026-120307 | 9.9 | beam-cloud | Beta9 worker | CWE-22,CWE-23 | none |
| CVE-2026-120308 | 9.9 | beam-cloud | Beta9 gateway | CWE-22,CWE-668 | none |
| CVE-2026-28336 | 9.9 | SolarWinds | Dameware | CWE-20 | none |
| CVE-2026-61728 | 9.9 | socfortress | CoPilot | CWE-79,CWE-922 |  |
| CVE-2026-62853 | 9.9 | mqttsnet | thinglinks | CWE-78,CWE-94 |  |
| CVE-2026-90868 | 9.9 | Progress Software | WS_FTP Server | CWE-78,CWE-88 | none |
| CVE-2025-31704 | 9.8 | Dahua | Intelligent Connection Center | CWE-78 | none |
| CVE-2025-49602 | 9.8 | n/a | n/a | CWE-613 | none |
| CVE-2026-102435 | 9.8 | themefic | Ultra Addons for Contact Form 7 | CWE-502 | none |
| CVE-2026-103039 | 9.8 | Gravity Forms | Gravity Forms | CWE-502 | none |
| CVE-2026-104339 | 9.8 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-106803 | 9.8 | n/a | n/a | CWE-121 | poc |
| CVE-2026-107048 | 9.8 | n/a | n/a | CWE-926 | poc |
| CVE-2026-107050 | 9.8 | n/a | n/a | CWE-94 | poc |

## Top proveedores (CVE nuevos)

- Google: 375
- Drupal: 106
- Unknown: 98
- n/a: 90
- n/d: 62
- Apache Software Foundation: 61
- MediaTek, Inc.: 56
- Hewlett Packard Enterprise (HPE): 55
- Linux: 52
- Red Hat: 46

## Top CWE

- CWE-79: 289
- CWE-862: 210
- CWE-863: 133
- CWE-22: 98
- CWE-416: 96
- CWE-639: 92
- CWE-787: 92
- CWE-200: 76
- CWE-502: 76
- CWE-78: 70

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.03"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2901,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2760
  }
}
```