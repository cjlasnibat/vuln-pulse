# Reporte semanal de vulnerabilidades — 2026-10-28 a 2026-11-03

## Resumen

- KEV agregadas: **6** (catálogo total: 1766; ransomware conocido: 0)
- CVE nuevos publicados: **2801** (rechazados: 189; registros actualizados: 7330)
- Por severidad CVSS: {'HIGH': 938, 'MEDIUM': 1085, 'LOW': 107, 'SIN_CVSS': 448, 'CRITICAL': 223}  — con CVSS: 84.0%
- SSVC (CISA ADP) explotación PoC/activa: 216; automatizable + impacto total: 100
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-28 | CVE-2026-41709 | Broadcom VMware ESX | Broadcom VMWare ESX Insufficient Logging Vulnerability | 2026-11-11 | Unknown |
| 2026-10-28 | CVE-2026-46300 | Linux Kernel | Linux Kernel Missing Initialization of a Variable Vulnerability | 2026-10-31 | Unknown |
| 2026-10-29 | CVE-2026-97229 | GitLab Community Edition and Enterprise Edition | GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability | 2026-11-01 | Unknown |
| 2026-10-29 | CVE-2026-76418 | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability | 2026-11-01 | Unknown |
| 2026-10-30 | CVE-2026-118527 | Ivanti Connect Secure | Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability | 2026-11-13 | Unknown |
| 2026-10-30 | CVE-2026-111357 | Ivanti Connect Secure | Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability | 2026-11-02 | Unknown |

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
| CVE-2026-61564 | 10 | WWBN | AVideo-Encoder | CWE-94 | poc |
| CVE-2026-61567 | 10 | WWBN | AVideo-Encoder | CWE-78 | poc |
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
| CVE-2026-44179 | 9.9 | xwikisas | xwiki-pro-macros | CWE-95 | poc |
| CVE-2026-61728 | 9.9 | socfortress | CoPilot | CWE-79,CWE-922 |  |
| CVE-2026-62853 | 9.9 | mqttsnet | thinglinks | CWE-78,CWE-94 |  |
| CVE-2026-90868 | 9.9 | Progress Software | WS_FTP Server | CWE-78,CWE-88 | none |
| CVE-2025-31704 | 9.8 | Dahua | Intelligent Connection Center | CWE-78 | none |
| CVE-2026-102435 | 9.8 | themefic | Ultra Addons for Contact Form 7 | CWE-502 |  |
| CVE-2026-103039 | 9.8 | Gravity Forms | Gravity Forms | CWE-502 | none |
| CVE-2026-103406 | 9.8 | Juniper Networks | Session Smart Conductor | CWE-78 |  |
| CVE-2026-103409 | 9.8 | Juniper Networks | Session Smart Router | CWE-306 |  |
| CVE-2026-103688 | 9.8 | Unknown | Checkout Files Upload for WooCommerce | CWE-434 | none |
| CVE-2026-103780 | 9.8 | Dell | PowerProtect Data Domain | CWE-121 | none |
| CVE-2026-104339 | 9.8 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-106803 | 9.8 | n/a | n/a | CWE-121 | poc |

## Top proveedores (CVE nuevos)

- Linux: 171
- Google: 162
- Unknown: 108
- Drupal: 106
- n/a: 85
- Dell: 73
- n/d: 56
- MediaTek, Inc.: 56
- Apache Software Foundation: 50
- Red Hat: 47

## Top CWE

- CWE-79: 315
- CWE-862: 222
- CWE-22: 92
- CWE-863: 86
- CWE-639: 84
- CWE-78: 83
- CWE-502: 80
- CWE-89: 78
- CWE-787: 75
- CWE-94: 60

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.30"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2990,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2556
  }
}
```