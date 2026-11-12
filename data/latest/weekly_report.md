# Reporte semanal de vulnerabilidades — 2026-11-06 a 2026-11-12

## Resumen

- KEV agregadas: **11** (catálogo total: 1779; ransomware conocido: 0)
- CVE nuevos publicados: **4753** (rechazados: 45; registros actualizados: 8094)
- Por severidad CVSS: {'HIGH': 2157, 'CRITICAL': 337, 'MEDIUM': 1763, 'LOW': 185, 'SIN_CVSS': 311}  — con CVSS: 93.5%
- SSVC (CISA ADP) explotación PoC/activa: 186; automatizable + impacto total: 132
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-06 | CVE-2026-19868 | SonicWall SonicOS SSLVPN | SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability | 2026-11-20 | Unknown |
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

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109469 | 10 | Microsoft | Entra Device Registration | CWE-639 | none |
| CVE-2026-110468 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-110469 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-115252 | 10 | Unknown | Confection WordPress Cable | CWE-94 | none |
| CVE-2026-117551 | 10 | jdownloads.com | jDownloads extension for Joomla | CWE-434 |  |
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-120017 | 10 | SAP_SE | SAP NetWeaver AS ABAP and ABAP Platform  | CWE-347 | none |
| CVE-2026-121351 | 10 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121352 | 10 | Adobe | Adobe Connect | CWE-863 | none |
| CVE-2026-121353 | 10 | Adobe | Adobe Connect | CWE-93 | none |
| CVE-2026-121356 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-121889 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-123551 | 10 | OpenIdentityPlatform | OpenAM | CWE-201 |  |
| CVE-2026-123966 | 10 | Tenda | AC19 | CWE-119,CWE-122 | poc |
| CVE-2026-124580 | 10 | Chengdu Feiyuxing Technology | VW2100 | CWE-77,CWE-78 |  |
| CVE-2026-124600 | 10 | GeoVision Inc. | GV-Face | CWE-319 | none |
| CVE-2026-124815 | 10 | Unknown | Clockinator Lite | CWE-89 | none |
| CVE-2026-125086 | 10 | D-Link | M60 | CWE-259,CWE-798 |  |
| CVE-2026-71495 | 10 | open-wanderer | wanderer | CWE-918 | poc |
| CVE-2026-76964 | 10 | SAP_SE | SAP NetWeaver AS ABAP (Internet Communic | CWE-1287 | none |
| CVE-2026-78287 | 10 | Staggs | STAGGS | CWE-94 | none |
| CVE-2026-89103 | 10 | SAP_SE | SAP Gateway | CWE-863 | none |
| CVE-2026-89126 | 10 | SAP_SE | SAP Web Dispatcher | CWE-122 | none |
| CVE-2026-107331 | 9.9 | IBM | DataStage on Cloud Pak for Data | CWE-36 |  |
| CVE-2026-109467 | 9.9 | Microsoft | Azure DevOps | CWE-287 | none |
| CVE-2026-109795 | 9.9 | SAP_SE | S4CRM | CWE-94 | none |
| CVE-2026-109803 | 9.9 | SAP_SE | SAP NetWeaver Knowledge Management (XML  | CWE-94 | none |
| CVE-2026-110697 | 9.9 | Red Hat | Red Hat OpenShift Update Service | CWE-89 | none |
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

## Top proveedores (CVE nuevos)

- Microsoft: 1095
- IBM: 295
- Google: 248
- Unknown: 189
- n/a: 180
- FFmpeg: 121
- Adobe: 110
- Apache Software Foundation: 108
- Mozilla: 108
- Fortinet: 98

## Top CWE

- CWE-79: 358
- CWE-122: 341
- CWE-416: 314
- CWE-862: 252
- CWE-125: 166
- CWE-639: 151
- CWE-863: 145
- CWE-918: 140
- CWE-22: 127
- CWE-89: 108

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.10"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4798,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4599
  }
}
```