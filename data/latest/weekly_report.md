# Reporte semanal de vulnerabilidades — 2026-11-12 a 2026-11-18

## Resumen

- KEV agregadas: **3** (catálogo total: 1782; ransomware conocido: 0)
- CVE nuevos publicados: **3432** (rechazados: 21; registros actualizados: 3294)
- Por severidad CVSS: {'SIN_CVSS': 140, 'MEDIUM': 1446, 'HIGH': 1301, 'CRITICAL': 324, 'LOW': 221}  — con CVSS: 95.9%
- SSVC (CISA ADP) explotación PoC/activa: 384; automatizable + impacto total: 170
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-13 | CVE-2026-114713 | UnrealIRCd UnrealIRCd | UnrealIRCd Improper Neutralization of Delimiters Vulnerability | 2026-11-16 | Unknown |
| 2026-11-13 | CVE-2026-123039 | Check Point Multiple Products | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | 2026-11-16 | Unknown |
| 2026-11-17 | CVE-2026-115731 | Perforce Puppet Enterprise | Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability | 2026-12-01 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-100397 | 10 | rucio | rucio | CWE-287 | poc |
| CVE-2026-114202 | 10 | ASUS | Control Center Express | CWE-321 |  |
| CVE-2026-114784 | 10 | Oracle Corporation | Oracle Business Intelligence Enterprise  | CWE-306 | none |
| CVE-2026-114824 | 10 | Oracle Corporation | Oracle Platform Security for Java | CWE-502 | none |
| CVE-2026-114835 | 10 | Oracle Corporation | Oracle Access Manager | CWE-306 | none |
| CVE-2026-117551 | 10 | jdownloads.com | jDownloads extension for Joomla | CWE-434 | none |
| CVE-2026-120387 | 10 | Circutor | PowerStudio SCADA Wave | CWE-347 | poc |
| CVE-2026-124815 | 10 | Unknown | Clockinator Lite | CWE-89 | none |
| CVE-2026-124822 | 10 | Unknown | Easy DragDrop File Uploader | CWE-73 | none |
| CVE-2026-127275 | 10 | Linksys | EA8100 | CWE-287,CWE-306 | poc |
| CVE-2026-127277 | 10 | Linksys | EA8100 | CWE-665 | poc |
| CVE-2026-129351 | 10 | TRENDnet | TEW-657BRM | CWE-119,CWE-787 | poc |
| CVE-2026-129353 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | none |
| CVE-2026-129354 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | poc |
| CVE-2026-129444 | 10 | D-Link | DSL-6740C | CWE-259,CWE-798 | none |
| CVE-2026-53998 | 10 | Arize-ai | phoenix | CWE-134,CWE-200 | none |
| CVE-2026-91500 | 10 | Oracle Corporation | Oracle Access Manager | CWE-284 | none |
| CVE-2026-91510 | 10 | Oracle Corporation | Oracle Access Manager |  |  |
| CVE-2026-91569 | 10 | Oracle Corporation | Oracle WebLogic Server | CWE-306 | none |
| CVE-2026-93664 | 10 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-502 | none |
| CVE-2026-95787 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-269 | none |
| CVE-2026-114819 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114822 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114848 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114978 | 9.9 | Oracle Corporation | Oracle Hyperion Financial Management | CWE-284 | none |
| CVE-2026-114980 | 9.9 | Oracle Corporation | Oracle AutoVue | CWE-284 | none |
| CVE-2026-125851 | 9.9 | themagnifico52 | Hotel Booking Lite | CWE-434 | none |
| CVE-2026-12591 | 9.9 | Zohocorp | M365 Manager Plus | CWE-862 | none |
| CVE-2026-132231 | 9.9 | JetBrains | TeamCity | CWE-1289 | none |
| CVE-2026-132232 | 9.9 | JetBrains | TeamCity | CWE-88 | none |
| CVE-2026-132233 | 9.9 | JetBrains | TeamCity | CWE-23 | none |
| CVE-2026-132234 | 9.9 | JetBrains | TeamCity | CWE-88 | none |
| CVE-2026-19732 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 | none |
| CVE-2026-28273 | 9.9 | ZoneMinder | zoneminder | CWE-862 |  |
| CVE-2026-77033 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 | none |
| CVE-2011-10042 | 9.8 |  |  | CWE-93 | none |
| CVE-2015-10149 | 9.8 |  |  | CWE-1286 | none |
| CVE-2026-107904 | 9.8 | valorapps.com | Easy File Uploader extension for Joomla | CWE-434 | none |
| CVE-2026-110009 | 9.8 | unzerplugins | Unzer Payments | CWE-287 |  |
| CVE-2026-110486 | 9.8 | Eclipse Foundation | Eclipse Mosquitto | CWE-191,CWE-787 |  |

## Top proveedores (CVE nuevos)

- Oracle Corporation: 578
- Google: 203
- Unknown: 95
- openemr: 80
- nocodb: 70
- Dell: 66
- n/a: 65
- Red Hat: 37
- GitLab: 37
- Samsung Mobile: 36

## Top CWE

- CWE-79: 310
- CWE-862: 240
- CWE-863: 158
- CWE-306: 133
- CWE-22: 115
- CWE-639: 102
- CWE-200: 95
- CWE-416: 90
- CWE-89: 88
- CWE-284: 67

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.17"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3453,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2992
  }
}
```