# Reporte semanal de vulnerabilidades — 2026-11-10 a 2026-11-16

## Resumen

- KEV agregadas: **8** (catálogo total: 1781; ransomware conocido: 0)
- CVE nuevos publicados: **4279** (rechazados: 16; registros actualizados: 5868)
- Por severidad CVSS: {'HIGH': 2135, 'MEDIUM': 1533, 'CRITICAL': 305, 'LOW': 182, 'SIN_CVSS': 124}  — con CVSS: 97.1%
- SSVC (CISA ADP) explotación PoC/activa: 238; automatizable + impacto total: 138
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-10 | CVE-2026-124194 | Microsoft Office | Microsoft Office Outlook Missing User Interaction for Potentially Unsafe Action Vulnerability | 2026-11-24 | Unknown |
| 2026-11-10 | CVE-2026-111793 | Openwave Messaging Limited Webtop Media Transcoder | Openwave Messaging Limited Webtop Media Transcoder Incorrect Resource Transfer Between Spheres Vulnerability | 2026-11-24 | Unknown |
| 2026-11-10 | CVE-2026-20320 | Cisco BroadWorks | Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability | 2026-11-24 | Unknown |
| 2026-11-10 | CVE-2026-111560 | Barracuda Networks Multiple Products | Barracuda Networks Multiple Products OS Command Injection Vulnerability | 2026-11-13 | Unknown |
| 2026-11-10 | CVE-2026-116606 | Barracuda Networks Barracuda Email Security Gateway (ESG) | Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-13 | Unknown |
| 2026-11-10 | CVE-2026-125350 | Google Chromium | Google Chromium Use-After-Free Vulnerability | 2026-11-24 | Unknown |
| 2026-11-13 | CVE-2026-114713 | UnrealIRCd UnrealIRCd | UnrealIRCd Improper Neutralization of Delimiters Vulnerability | 2026-11-16 | Unknown |
| 2026-11-13 | CVE-2026-123039 | Check Point Multiple Products | Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability | 2026-11-16 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-117551 | 10 | jdownloads.com | jDownloads extension for Joomla | CWE-434 | none |
| CVE-2026-121351 | 10 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121352 | 10 | Adobe | Adobe Connect | CWE-863 | none |
| CVE-2026-121353 | 10 | Adobe | Adobe Connect | CWE-93 | none |
| CVE-2026-121356 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-121889 | 10 | Adobe | Adobe Connect | CWE-918 | none |
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
| CVE-2026-109467 | 9.9 | Microsoft | Azure DevOps | CWE-287 | none |
| CVE-2026-110697 | 9.9 | Project Quay | quay | CWE-89 | none |
| CVE-2026-113579 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-113580 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-114371 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-119017 | 9.9 | Adobe | Adobe Experience Manager 6.5 | CWE-863 | none |
| CVE-2026-120002 | 9.9 | Microsoft | Microsoft SharePoint Server Subscription | CWE-863 | none |
| CVE-2026-121354 | 9.9 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121887 | 9.9 | Adobe | Adobe Connect | CWE-611 | none |
| CVE-2026-121892 | 9.9 | Adobe | Adobe Connect | CWE-94 | none |
| CVE-2026-121894 | 9.9 | Adobe | Adobe Connect | CWE-89 | none |
| CVE-2026-121896 | 9.9 | Adobe | Adobe Connect | CWE-89 | none |
| CVE-2026-121898 | 9.9 | Adobe | Adobe Connect | CWE-89 | none |
| CVE-2026-121906 | 9.9 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121908 | 9.9 | Adobe | Adobe Connect | CWE-89 | none |
| CVE-2026-125851 | 9.9 | themagnifico52 | Hotel Booking Lite | CWE-434 | none |
| CVE-2026-12591 | 9.9 | Zohocorp | M365 Manager Plus | CWE-862 | none |
| CVE-2026-13312 | 9.9 | Axis Communications AB | AXIS Camera Station Pro | CWE-1287 | none |
| CVE-2026-19732 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 |  |
| CVE-2026-77033 | 9.9 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-78 |  |
| CVE-2026-110959 | 9.8 | Unknown | Descope | CWE-287 | none |
| CVE-2026-110960 | 9.8 | Unknown | Auth Armor | CWE-287 | none |
| CVE-2026-111240 | 9.8 | Apache Software Foundation | Apache TomEE | CWE-287 | none |

## Top proveedores (CVE nuevos)

- Microsoft: 1103
- Google: 248
- n/a: 165
- Unknown: 142
- Adobe: 110
- Mozilla: 105
- Fortinet: 98
- Apache Software Foundation: 89
- openemr: 80
- Dell: 58

## Top CWE

- CWE-122: 332
- CWE-416: 325
- CWE-79: 310
- CWE-862: 225
- CWE-125: 173
- CWE-863: 148
- CWE-787: 122
- CWE-22: 102
- CWE-639: 100
- CWE-89: 100

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
    "fetched": 4295,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4038
  }
}
```