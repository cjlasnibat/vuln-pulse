# Reporte semanal de vulnerabilidades — 2026-11-05 a 2026-11-11

## Resumen

- KEV agregadas: **11** (catálogo total: 1779; ransomware conocido: 0)
- CVE nuevos publicados: **4562** (rechazados: 259; registros actualizados: 9867)
- Por severidad CVSS: {'MEDIUM': 1744, 'HIGH': 2001, 'SIN_CVSS': 329, 'CRITICAL': 316, 'LOW': 172}  — con CVSS: 92.8%
- SSVC (CISA ADP) explotación PoC/activa: 235; automatizable + impacto total: 121
- EPSS ≥ 10%: 1

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
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-120017 | 10 | SAP_SE | SAP NetWeaver AS ABAP and ABAP Platform  | CWE-347 | none |
| CVE-2026-121351 | 10 | Adobe | Adobe Connect | CWE-22 | none |
| CVE-2026-121352 | 10 | Adobe | Adobe Connect | CWE-863 | none |
| CVE-2026-121353 | 10 | Adobe | Adobe Connect | CWE-93 | none |
| CVE-2026-121356 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-121489 | 10 | Apache Software Foundation | Apache Juneau | CWE-22 | none |
| CVE-2026-121889 | 10 | Adobe | Adobe Connect | CWE-918 | none |
| CVE-2026-123551 | 10 | OpenIdentityPlatform | OpenAM | CWE-201 |  |
| CVE-2026-123966 | 10 | Tenda | AC19 | CWE-119,CWE-122 | poc |
| CVE-2026-124580 | 10 | Chengdu Feiyuxing Technology | VW2100 | CWE-77,CWE-78 |  |
| CVE-2026-124600 | 10 | GeoVision Inc. | GV-Face | CWE-319 |  |
| CVE-2026-125086 | 10 | D-Link | M60 | CWE-259,CWE-798 |  |
| CVE-2026-71495 | 10 | open-wanderer | wanderer | CWE-918 | poc |
| CVE-2026-73098 | 10 | Apache Software Foundation | Apache Juneau | CWE-470 | none |
| CVE-2026-73099 | 10 | Apache Software Foundation | Apache Juneau | CWE-352 | none |
| CVE-2026-73100 | 10 | Apache Software Foundation | Apache Juneau | CWE-532 | none |
| CVE-2026-73101 | 10 | Apache Software Foundation | Apache Juneau | CWE-209 | none |
| CVE-2026-73116 | 10 | Apache Software Foundation | Apache Juneau | CWE-522 | none |
| CVE-2026-73117 | 10 | Apache Software Foundation | Apache Juneau | CWE-113 | none |
| CVE-2026-76964 | 10 | SAP_SE | SAP NetWeaver AS ABAP (Internet Communic | CWE-1287 | none |
| CVE-2026-78287 | 10 | Staggs | STAGGS | CWE-94 |  |
| CVE-2026-89103 | 10 | SAP_SE | SAP Gateway | CWE-863 | none |
| CVE-2026-89126 | 10 | SAP_SE | SAP Web Dispatcher | CWE-122 | none |
| CVE-2026-96677 | 10 | Apache Software Foundation | Apache Juneau | CWE-79 | none |
| CVE-2026-107331 | 9.9 | IBM | DataStage on Cloud Pak for Data | CWE-36 |  |
| CVE-2026-109467 | 9.9 | Microsoft | Azure DevOps | CWE-287 | none |
| CVE-2026-109795 | 9.9 | SAP_SE | S4CRM | CWE-94 | none |
| CVE-2026-109803 | 9.9 | SAP_SE | SAP NetWeaver Knowledge Management (XML  | CWE-94 | none |
| CVE-2026-110697 | 9.9 | Red Hat | Red Hat OpenShift Update Service | CWE-89 |  |
| CVE-2026-111489 | 9.9 | TPC Software | Matchpoint | CWE-798 | none |
| CVE-2026-111490 | 9.9 | TPC Software | Matchpoint | CWE-639 | none |
| CVE-2026-113579 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-113580 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-114371 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-119017 | 9.9 | Adobe | Adobe Experience Manager 6.5 | CWE-863 | none |

## Top proveedores (CVE nuevos)

- Microsoft: 1095
- IBM: 295
- Unknown: 197
- Google: 167
- Apache Software Foundation: 164
- n/a: 129
- FFmpeg: 121
- Adobe: 112
- Mozilla: 108
- JetBrains: 89

## Top CWE

- CWE-79: 357
- CWE-122: 335
- CWE-416: 269
- CWE-862: 254
- CWE-125: 166
- CWE-639: 155
- CWE-918: 141
- CWE-863: 129
- CWE-22: 119
- CWE-89: 114

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
    "fetched": 4821,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2272
  }
}
```