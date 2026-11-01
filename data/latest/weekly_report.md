# Reporte semanal de vulnerabilidades — 2026-10-26 a 2026-11-01

## Resumen

- KEV agregadas: **10** (catálogo total: 1766; ransomware conocido: 0)
- CVE nuevos publicados: **3386** (rechazados: 217; registros actualizados: 7460)
- Por severidad CVSS: {'MEDIUM': 1212, 'SIN_CVSS': 807, 'CRITICAL': 273, 'HIGH': 969, 'LOW': 125}  — con CVSS: 76.2%
- SSVC (CISA ADP) explotación PoC/activa: 145; automatizable + impacto total: 86
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
| 2026-10-30 | CVE-2026-118527 | Ivanti Connect Secure | Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability | 2026-11-13 | Unknown |
| 2026-10-30 | CVE-2026-111357 | Ivanti Connect Secure | Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability | 2026-11-02 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-105781 | 10 | Adobe | Adobe Campaign Classic | CWE-89 |  |
| CVE-2026-112816 | 10 | Canonical | LXD | CWE-295 | none |
| CVE-2026-115905 | 10 | zip-rs | zip2 | CWE-20,CWE-436 |  |
| CVE-2026-116508 | 10 | TOTOLINK | A950RG | CWE-119,CWE-121 | poc |
| CVE-2026-120189 | 10 | D-Link | DIR-505 | CWE-119,CWE-121 |  |
| CVE-2026-120195 | 10 | WAVLINK | WL-WN579A3-A | CWE-77,CWE-78 |  |
| CVE-2026-120198 | 10 | WAVLINK | WL-WN530BE1-A | CWE-74,CWE-77 |  |
| CVE-2026-120338 | 10 | PrefectHQ | prefab-ui | CWE-269,CWE-693 |  |
| CVE-2026-61564 | 10 | WWBN | AVideo-Encoder | CWE-94 |  |
| CVE-2026-61567 | 10 | WWBN | AVideo-Encoder | CWE-78 |  |
| CVE-2026-61738 | 10 | socfortress | CoPilot | CWE-22,CWE-434 |  |
| CVE-2026-61826 | 10 | morpheus65535 | bazarr | CWE-352,CWE-862 |  |
| CVE-2026-61991 | 10 | Ajax Load More | AjaxLoadMore Cache | CWE-94 | none |
| CVE-2026-65145 | 10 | NVIDIA | NeMo Agent Toolkit | CWE-306 |  |
| CVE-2026-84295 | 10 | Progress Software | WS_FTP Server | CWE-287,CWE-522 | none |
| CVE-2026-102649 | 9.9 | padok-team | burrito | CWE-306,CWE-863 | poc |
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
| CVE-2026-120306 | 9.9 | beam-cloud | Beta9 worker | CWE-269,CWE-653 |  |
| CVE-2026-120307 | 9.9 | beam-cloud | Beta9 worker | CWE-22,CWE-23 |  |
| CVE-2026-120308 | 9.9 | beam-cloud | Beta9 gateway | CWE-22,CWE-668 |  |
| CVE-2026-44179 | 9.9 | xwikisas | xwiki-pro-macros | CWE-95 |  |
| CVE-2026-61728 | 9.9 | socfortress | CoPilot | CWE-79,CWE-922 |  |
| CVE-2026-62853 | 9.9 | mqttsnet | thinglinks | CWE-78,CWE-94 |  |
| CVE-2026-90868 | 9.9 | Progress Software | WS_FTP Server | CWE-78,CWE-88 | none |
| CVE-2025-31704 | 9.8 | Dahua | Intelligent Connection Center | CWE-78 | none |
| CVE-2026-103039 | 9.8 | Gravity Forms | Gravity Forms | CWE-502 | none |
| CVE-2026-103406 | 9.8 | Juniper Networks | Session Smart Conductor | CWE-78 |  |
| CVE-2026-103409 | 9.8 | Juniper Networks | Session Smart Router | CWE-306 |  |
| CVE-2026-103688 | 9.8 | Unknown | Checkout Files Upload for WooCommerce | CWE-434 | none |
| CVE-2026-103780 | 9.8 | Dell | PowerProtect Data Domain | CWE-121 | none |
| CVE-2026-104339 | 9.8 | IBM | Langflow OSS | CWE-94 | none |

## Top proveedores (CVE nuevos)

- Apple: 328
- Mozilla: 176
- Linux: 129
- n/a: 112
- Unknown: 109
- Drupal: 106
- Google: 75
- Dell: 65
- n/d: 62
- Red Hat: 43

## Top CWE

- CWE-79: 358
- CWE-862: 229
- CWE-89: 92
- CWE-863: 88
- CWE-22: 87
- CWE-502: 83
- CWE-78: 82
- CWE-639: 78
- CWE-787: 76
- CWE-125: 73

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
    "fetched": 3603,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3370
  }
}
```