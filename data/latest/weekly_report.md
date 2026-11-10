# Reporte semanal de vulnerabilidades — 2026-11-04 a 2026-11-10

## Resumen

- KEV agregadas: **6** (catálogo total: 1773; ransomware conocido: 0)
- CVE nuevos publicados: **3059** (rechazados: 262; registros actualizados: 6827)
- Por severidad CVSS: {'HIGH': 1138, 'MEDIUM': 1321, 'CRITICAL': 276, 'LOW': 161, 'SIN_CVSS': 163}  — con CVSS: 94.7%
- SSVC (CISA ADP) explotación PoC/activa: 279; automatizable + impacto total: 95
- EPSS ≥ 10%: 2

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-04 | CVE-2024-27834 | Apple Multiple Products | Apple Multiple Products Improper Authentication Vulnerability | 2026-11-18 | Unknown |
| 2026-11-06 | CVE-2026-19868 | SonicWall SonicOS SSLVPN | SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability | 2026-11-20 | Unknown |
| 2026-11-09 | CVE-2026-102895 | GPUStack GPUStack | GPUStack Improper Authentication Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-123158 | OpenBSD OpenSSH | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-116779 | SignalWire FreeSwitch | SignalWire FreeSwitch Code Injection Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-123218 | IBM Aspera Faspex | IBM Aspera Faspex Incorrect Authorization Vulnerability | 2026-11-12 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109469 | 10 | Microsoft | Entra Device Registration | CWE-639 |  |
| CVE-2026-110468 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-110469 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-115252 | 10 | Unknown | Confection WordPress Cable | CWE-94 | none |
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-120017 | 10 | SAP_SE | SAP NetWeaver AS ABAP and ABAP Platform  | CWE-347 |  |
| CVE-2026-121489 | 10 | Apache Software Foundation | Apache Juneau | CWE-22 |  |
| CVE-2026-121932 | 10 | Linksys | E5350 | CWE-77,CWE-78 | poc |
| CVE-2026-121933 | 10 | Linksys | E5350 | CWE-287,CWE-306 | poc |
| CVE-2026-122013 | 10 | Comfast | CF-WR632AX | CWE-22 | poc |
| CVE-2026-122051 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-123551 | 10 | OpenIdentityPlatform | OpenAM | CWE-201 |  |
| CVE-2026-123966 | 10 | Tenda | AC19 | CWE-119,CWE-122 | poc |
| CVE-2026-124580 | 10 | Chengdu Feiyuxing Technology | VW2100 | CWE-77,CWE-78 |  |
| CVE-2026-124600 | 10 | GeoVision Inc. | GV-Face | CWE-319 |  |
| CVE-2026-125086 | 10 | D-Link | M60 | CWE-259,CWE-798 |  |
| CVE-2026-71495 | 10 | open-wanderer | wanderer | CWE-918 | poc |
| CVE-2026-73098 | 10 | Apache Software Foundation | Apache Juneau | CWE-470 | none |
| CVE-2026-73099 | 10 | Apache Software Foundation | Apache Juneau | CWE-352 | none |
| CVE-2026-73100 | 10 | Apache Software Foundation | Apache Juneau | CWE-532 |  |
| CVE-2026-73101 | 10 | Apache Software Foundation | Apache Juneau | CWE-209 |  |
| CVE-2026-73116 | 10 | Apache Software Foundation | Apache Juneau | CWE-522 |  |
| CVE-2026-73117 | 10 | Apache Software Foundation | Apache Juneau | CWE-113 |  |
| CVE-2026-76964 | 10 | SAP_SE | SAP NetWeaver AS ABAP (Internet Communic | CWE-1287 |  |
| CVE-2026-89103 | 10 | SAP_SE | SAP Gateway | CWE-863 |  |
| CVE-2026-89126 | 10 | SAP_SE | SAP Web Dispatcher | CWE-122 |  |
| CVE-2026-96677 | 10 | Apache Software Foundation | Apache Juneau | CWE-79 |  |
| CVE-2026-107331 | 9.9 | IBM | DataStage on Cloud Pak for Data | CWE-36 |  |
| CVE-2026-109795 | 9.9 | SAP_SE | S4CRM | CWE-94 |  |
| CVE-2026-109803 | 9.9 | SAP_SE | SAP NetWeaver Knowledge Management (XML  | CWE-94 |  |
| CVE-2026-111489 | 9.9 | TPC Software | Matchpoint | CWE-798 | none |
| CVE-2026-111490 | 9.9 | TPC Software | Matchpoint | CWE-639 | none |
| CVE-2026-123800 | 9.9 | supertokens | supertokens-core | CWE-639,CWE-863 |  |
| CVE-2026-13312 | 9.9 | Axis Communications AB | AXIS Camera Station Pro | CWE-1287 |  |
| CVE-2026-16884 | 9.9 | IBM | API Connect | CWE-611 |  |
| CVE-2026-16920 | 9.9 | IBM | API Connect | CWE-441 |  |
| CVE-2026-17049 | 9.9 | IBM | API Connect | CWE-639 |  |
| CVE-2026-17117 | 9.9 | IBM | API Connect | CWE-915 | none |
| CVE-2026-17132 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17134 | 9.9 | IBM | API Connect | CWE-89 |  |

## Top proveedores (CVE nuevos)

- IBM: 322
- Unknown: 164
- Apache Software Foundation: 157
- n/a: 130
- FFmpeg: 121
- Mozilla: 103
- JetBrains: 89
- Red Hat: 75
- openemr: 60
- SAP_SE: 42

## Top CWE

- CWE-79: 280
- CWE-862: 203
- CWE-639: 154
- CWE-918: 134
- CWE-22: 110
- CWE-89: 96
- CWE-863: 92
- CWE-787: 86
- CWE-200: 78
- CWE-416: 65

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.09"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3321,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2688
  }
}
```