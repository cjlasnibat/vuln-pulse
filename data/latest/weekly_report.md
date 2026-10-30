# Reporte semanal de vulnerabilidades — 2026-10-24 a 2026-10-30

## Resumen

- KEV agregadas: **8** (catálogo total: 1764; ransomware conocido: 0)
- CVE nuevos publicados: **3189** (rechazados: 215; registros actualizados: 6301)
- Por severidad CVSS: {'MEDIUM': 1156, 'HIGH': 831, 'SIN_CVSS': 847, 'CRITICAL': 230, 'LOW': 125}  — con CVSS: 73.4%
- SSVC (CISA ADP) explotación PoC/activa: 128; automatizable + impacto total: 59
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-26 | CVE-2026-109618 | PHP Group PHP | PHP Memory Corruption Vulnerability | 2026-10-29 | Unknown |
| 2026-10-26 | CVE-2026-109619 | PHP Group PHP | PHP Stale Internal Request-State Vulnerability | 2026-10-29 | Unknown |
| 2026-10-27 | CVE-2026-48356 | Adobe Commerce and Magento | Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability | 2026-11-10 | Unknown |
| 2026-10-27 | CVE-2026-111497 | Google Brotli | Google Brotli Unchecked Return Value Vulnerability | 2026-11-10 | Unknown |
| 2026-10-28 | CVE-2026-41709 | Broadcom VMware ESX | Broadcom VMWare ESX Insufficient Logging Vulnerability | 2026-11-11 | Unknown |
| 2026-10-28 | CVE-2026-46300 | Linux Kernel | Linux Kernel Missing Initialization of a Variable Vulnerability | 2026-10-31 | Unknown |
| 2026-10-29 | CVE-2026-97229 | GitLab Community Edition and Enterprise Edition | GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability | 2026-11-01 | Unknown |
| 2026-10-29 | CVE-2026-76418 | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability | 2026-11-01 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-105781 | 10 | Adobe | Adobe Campaign Classic | CWE-89 |  |
| CVE-2026-115905 | 10 | zip-rs | zip2 | CWE-20,CWE-436 |  |
| CVE-2026-116508 | 10 | TOTOLINK | A950RG | CWE-119,CWE-121 |  |
| CVE-2026-61564 | 10 | WWBN | AVideo-Encoder | CWE-94 |  |
| CVE-2026-61567 | 10 | WWBN | AVideo-Encoder | CWE-78 |  |
| CVE-2026-61738 | 10 | socfortress | CoPilot | CWE-22,CWE-434 |  |
| CVE-2026-61991 | 10 | Ajax Load More | AjaxLoadMore Cache | CWE-94 |  |
| CVE-2026-65145 | 10 | NVIDIA | NeMo Agent Toolkit | CWE-306 |  |
| CVE-2026-84295 | 10 | Progress Software | WS_FTP Server | CWE-287,CWE-522 | none |
| CVE-2026-102649 | 9.9 | padok-team | burrito | CWE-306,CWE-863 |  |
| CVE-2026-104351 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-104353 | 9.9 | Adobe | Adobe Campaign Classic | CWE-78 |  |
| CVE-2026-105489 | 9.9 | Adobe | Adobe Campaign Classic | CWE-89 | none |
| CVE-2026-105780 | 9.9 | Adobe | Adobe Campaign Classic | CWE-863 |  |
| CVE-2026-107327 | 9.9 | IBM | Langflow OSS | CWE-862 | none |
| CVE-2026-107328 | 9.9 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-107329 | 9.9 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-110720 | 9.9 | HashiCorp | Tooling | CWE-863 | none |
| CVE-2026-113617 | 9.9 | Unknown | Automated Import Products to Cart | CWE-22 | none |
| CVE-2026-115188 | 9.9 |  |  | CWE-434,CWE-94 | none |
| CVE-2026-115933 | 9.9 | GitroomHQ | postiz-app | CWE-290,CWE-345 |  |
| CVE-2026-44179 | 9.9 | xwikisas | xwiki-pro-macros | CWE-95 |  |
| CVE-2026-61728 | 9.9 | socfortress | CoPilot | CWE-79,CWE-922 |  |
| CVE-2026-90868 | 9.9 | Progress Software | WS_FTP Server | CWE-78,CWE-88 | none |
| CVE-2025-31704 | 9.8 | Dahua | Intelligent Connection Center | CWE-78 | none |
| CVE-2026-103039 | 9.8 | Gravity Forms | Gravity Forms | CWE-502 | none |
| CVE-2026-103406 | 9.8 | Juniper Networks | Session Smart Conductor | CWE-78 |  |
| CVE-2026-103409 | 9.8 | Juniper Networks | Session Smart Router | CWE-306 |  |
| CVE-2026-103688 | 9.8 | Unknown | Checkout Files Upload for WooCommerce | CWE-434 | none |
| CVE-2026-103780 | 9.8 | Dell | PowerProtect Data Domain | CWE-121 | none |
| CVE-2026-104339 | 9.8 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-106013 | 9.8 | artbees | Jupiter X Core | CWE-287 | none |
| CVE-2026-107058 | 9.8 | n/a | n/a | CWE-287 | poc |
| CVE-2026-107092 | 9.8 | n/a | n/a | CWE-22 | poc |
| CVE-2026-10757 | 9.8 | Esri | ArcGIS Server | CWE-89 | none |
| CVE-2026-109218 | 9.8 | kleor | Contact Manager | CWE-434 | none |
| CVE-2026-109516 | 9.8 | guruteam | Bot for Telegram on WooCommerce | CWE-287 | none |
| CVE-2026-110186 | 9.8 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-110799 | 9.8 | givanz | Vvveb | CWE-287 | poc |
| CVE-2026-110879 | 9.8 | FasterXML | jackson-databind | CWE-502 |  |

## Top proveedores (CVE nuevos)

- Apple: 328
- Mozilla: 176
- Linux: 129
- Unknown: 123
- n/a: 117
- Drupal: 104
- Google: 75
- Dell: 65
- n/d: 55
- Red Hat: 37

## Top CWE

- CWE-79: 313
- CWE-862: 207
- CWE-89: 95
- CWE-639: 80
- CWE-22: 79
- CWE-863: 77
- CWE-787: 75
- CWE-502: 74
- CWE-78: 73
- CWE-125: 68

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.29"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3404,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2944
  }
}
```