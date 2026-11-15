# Reporte semanal de vulnerabilidades — 2026-11-09 a 2026-11-15

## Resumen

- KEV agregadas: **12** (catálogo total: 1781; ransomware conocido: 0)
- CVE nuevos publicados: **4527** (rechazados: 27; registros actualizados: 6163)
- Por severidad CVSS: {'MEDIUM': 1624, 'HIGH': 2203, 'CRITICAL': 321, 'SIN_CVSS': 192, 'LOW': 187}  — con CVSS: 95.8%
- SSVC (CISA ADP) explotación PoC/activa: 230; automatizable + impacto total: 134
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-09 | CVE-2026-102895 | GPUStack GPUStack | GPUStack Improper Authentication Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-123158 | OpenBSD OpenSSH | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-116779 | SignalWire FreeSwitch | SignalWire FreeSwitch Code Injection Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-123218 | IBM Aspera Faspex | IBM Aspera Faspex Incorrect Authorization Vulnerability | 2026-11-12 | Unknown |
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
| CVE-2026-110468 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-110469 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-115252 | 10 | Unknown | Confection WordPress Cable | CWE-94 | none |
| CVE-2026-117551 | 10 | jdownloads.com | jDownloads extension for Joomla | CWE-434 | none |
| CVE-2026-120017 | 10 | SAP_SE | SAP NetWeaver AS ABAP and ABAP Platform  | CWE-347 | none |
| CVE-2026-121351 | 10 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121352 | 10 | Adobe | Adobe Connect | CWE-863 | none |
| CVE-2026-121353 | 10 | Adobe | Adobe Connect | CWE-93 | none |
| CVE-2026-121356 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-121889 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-124580 | 10 | Chengdu Feiyuxing Technology | VW2100 | CWE-77,CWE-78 | poc |
| CVE-2026-124600 | 10 | GeoVision Inc. | GV-Face | CWE-319 | none |
| CVE-2026-124815 | 10 | Unknown | Clockinator Lite | CWE-89 | none |
| CVE-2026-124822 | 10 | Unknown | Easy DragDrop File Uploader | CWE-73 | none |
| CVE-2026-125086 | 10 | D-Link | M60 | CWE-259,CWE-798 | poc |
| CVE-2026-127275 | 10 | Linksys | EA8100 | CWE-287,CWE-306 | poc |
| CVE-2026-127277 | 10 | Linksys | EA8100 | CWE-665 |  |
| CVE-2026-129351 | 10 | TRENDnet | TEW-657BRM | CWE-119,CWE-787 |  |
| CVE-2026-129353 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 |  |
| CVE-2026-129354 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 |  |
| CVE-2026-129444 | 10 | D-Link | DSL-6740C | CWE-259,CWE-798 |  |
| CVE-2026-76964 | 10 | SAP_SE | SAP NetWeaver AS ABAP (Internet Communic | CWE-1287 | none |
| CVE-2026-78287 | 10 | Staggs | STAGGS | CWE-94 | none |
| CVE-2026-89103 | 10 | SAP_SE | SAP Gateway | CWE-863 | none |
| CVE-2026-89126 | 10 | SAP_SE | SAP Web Dispatcher | CWE-122 | none |
| CVE-2026-109467 | 9.9 | Microsoft | Azure DevOps | CWE-287 | none |
| CVE-2026-109795 | 9.9 | SAP_SE | S4CRM | CWE-94 | none |
| CVE-2026-109803 | 9.9 | SAP_SE | SAP NetWeaver Knowledge Management (XML  | CWE-94 | none |
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

## Top proveedores (CVE nuevos)

- Microsoft: 1094
- Google: 248
- n/a: 176
- Unknown: 161
- FFmpeg: 121
- Apache Software Foundation: 110
- Adobe: 110
- Mozilla: 108
- Fortinet: 98
- openemr: 80

## Top CWE

- CWE-122: 346
- CWE-416: 330
- CWE-79: 320
- CWE-862: 211
- CWE-125: 186
- CWE-863: 149
- CWE-787: 135
- CWE-22: 106
- CWE-89: 105
- CWE-639: 104

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
    "fetched": 4554,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4485
  }
}
```