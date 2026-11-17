# Reporte semanal de vulnerabilidades — 2026-11-11 a 2026-11-17

## Resumen

- KEV agregadas: **2** (catálogo total: 1781; ransomware conocido: 0)
- CVE nuevos publicados: **2588** (rechazados: 15; registros actualizados: 2839)
- Por severidad CVSS: {'MEDIUM': 1089, 'HIGH': 1073, 'CRITICAL': 222, 'LOW': 167, 'SIN_CVSS': 37}  — con CVSS: 98.6%
- SSVC (CISA ADP) explotación PoC/activa: 256; automatizable + impacto total: 106
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-13 | CVE-2026-114713 | UnrealIRCd UnrealIRCd | UnrealIRCd Improper Neutralization of Delimiters Vulnerability | 2026-11-16 | Unknown |
| 2026-11-13 | CVE-2026-123039 | Check Point Multiple Products | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | 2026-11-16 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-117551 | 10 | jdownloads.com | jDownloads extension for Joomla | CWE-434 | none |
| CVE-2026-120387 | 10 | Circutor | PowerStudio SCADA Wave | CWE-347 | poc |
| CVE-2026-124815 | 10 | Unknown | Clockinator Lite | CWE-89 | none |
| CVE-2026-124822 | 10 | Unknown | Easy DragDrop File Uploader | CWE-73 | none |
| CVE-2026-127275 | 10 | Linksys | EA8100 | CWE-287,CWE-306 | poc |
| CVE-2026-127277 | 10 | Linksys | EA8100 | CWE-665 |  |
| CVE-2026-129351 | 10 | TRENDnet | TEW-657BRM | CWE-119,CWE-787 |  |
| CVE-2026-129353 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | none |
| CVE-2026-129354 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 |  |
| CVE-2026-129444 | 10 | D-Link | DSL-6740C | CWE-259,CWE-798 | none |
| CVE-2026-53998 | 10 | Arize-ai | phoenix | CWE-134,CWE-200 |  |
| CVE-2026-78287 | 10 | Staggs | STAGGS | CWE-94 | none |
| CVE-2026-93664 | 10 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-502 | none |
| CVE-2026-110697 | 9.9 | Project Quay | quay | CWE-89 | none |
| CVE-2026-125851 | 9.9 | themagnifico52 | Hotel Booking Lite | CWE-434 | none |
| CVE-2026-12591 | 9.9 | Zohocorp | M365 Manager Plus | CWE-862 | none |
| CVE-2026-19732 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 | none |
| CVE-2026-28273 | 9.9 | ZoneMinder | zoneminder | CWE-862 |  |
| CVE-2026-77033 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 | none |
| CVE-2011-10042 | 9.8 |  |  | CWE-93 | none |
| CVE-2015-10149 | 9.8 |  |  | CWE-1286 | none |
| CVE-2026-107904 | 9.8 | valorapps.com | Easy File Uploader extension for Joomla | CWE-434 | none |
| CVE-2026-110959 | 9.8 | Unknown | Descope | CWE-287 | none |
| CVE-2026-110960 | 9.8 | Unknown | Auth Armor | CWE-287 | none |
| CVE-2026-118063 | 9.8 | Unknown | Advance Guest Post | CWE-434 | none |
| CVE-2026-118064 | 9.8 | Unknown | Advance Guest Post | CWE-434 | none |
| CVE-2026-119077 | 9.8 | elextensions | ELEX WordPress HelpDesk & Customer Ticke | CWE-502 | none |
| CVE-2026-120522 | 9.8 | fluentwiz | Cloud Storage Manager for Fluent Forms – | CWE-22 | none |
| CVE-2026-121497 | 9.8 | Unknown | AskAny | CWE-434 | none |
| CVE-2026-122147 | 9.8 | ICRTouch | PocketTouch | CWE-798 | none |
| CVE-2026-122662 | 9.8 | Barn2 Plugins | Document Library Pro | CWE-502 | none |
| CVE-2026-123374 | 9.8 | Apache Software Foundation | Apache Roller | CWE-502 | none |
| CVE-2026-123695 | 9.8 | Unknown | Security For WooCommerce | CWE-269 | none |
| CVE-2026-123710 | 9.8 | Project Quay | quay | CWE-1287 | none |
| CVE-2026-124814 | 9.8 | Unknown | Ultimate Addons for Elementor Forms | CWE-434 | none |
| CVE-2026-124833 | 9.8 | Unknown | Ahime Image Printer | CWE-434 | none |
| CVE-2026-125055 | 9.8 | sameh101 | Chatterbug Forms – Fast, Flexible WordPr | CWE-434 | none |
| CVE-2026-125769 | 9.8 | Nasir Ahmed | Advanced Form Integration | CWE-266 | none |
| CVE-2026-125795 | 9.8 | Estatik | Estatik | CWE-98 | none |
| CVE-2026-125855 | 9.8 | Elextensions | ELEX WordPress HelpDesk & Customer Ticke | CWE-502 | none |

## Top proveedores (CVE nuevos)

- Unknown: 138
- Fortinet: 93
- Google: 83
- openemr: 80
- n/a: 62
- Dell: 58
- Apache Software Foundation: 52
- Red Hat: 43
- GitLab: 37
- Samsung Mobile: 36

## Top CWE

- CWE-79: 278
- CWE-862: 219
- CWE-863: 124
- CWE-22: 98
- CWE-639: 97
- CWE-89: 79
- CWE-200: 71
- CWE-787: 66
- CWE-416: 63
- CWE-78: 57

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.13"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2603,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2431
  }
}
```