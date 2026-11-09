# Reporte semanal de vulnerabilidades — 2026-11-03 a 2026-11-09

## Resumen

- KEV agregadas: **6** (catálogo total: 1772; ransomware conocido: 0)
- CVE nuevos publicados: **3236** (rechazados: 267; registros actualizados: 7198)
- Por severidad CVSS: {'MEDIUM': 1413, 'CRITICAL': 300, 'SIN_CVSS': 194, 'HIGH': 1161, 'LOW': 168}  — con CVSS: 94.0%
- SSVC (CISA ADP) explotación PoC/activa: 330; automatizable + impacto total: 94
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-03 | CVE-2026-119977 | WordPress WordPress Core | WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability | 2026-11-06 | Unknown |
| 2026-11-04 | CVE-2024-27834 | Apple Multiple Products | Apple Multiple Products Improper Authentication Vulnerability | 2026-11-18 | Unknown |
| 2026-11-06 | CVE-2026-19868 | SonicWall SonicOS SSLVPN | SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability | 2026-11-20 | Unknown |
| 2026-11-09 | CVE-2026-102895 | GPUStack GPUStack | GPUStack Improper Authentication Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-123158 | OpenBSD OpenSSH | OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability | 2026-11-12 | Unknown |
| 2026-11-09 | CVE-2026-116779 | SignalWire FreeSwitch | SignalWire FreeSwitch Code Injection Vulnerability | 2026-11-12 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109469 | 10 | Microsoft | Entra Device Registration | CWE-639 |  |
| CVE-2026-110468 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-110469 | 10 | Fundacja Widzialni | WidzialniCMS | CWE-434 | none |
| CVE-2026-115252 | 10 | Unknown | Confection WordPress Cable | CWE-94 | none |
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-121489 | 10 | Apache Software Foundation | Apache Juneau | CWE-22 |  |
| CVE-2026-121606 | 10 | Qihoo 360 | D621-2 | CWE-345,CWE-347 | poc |
| CVE-2026-121607 | 10 | Qihoo 360 | D603-2 | CWE-77,CWE-78 | poc |
| CVE-2026-121609 | 10 | Qihoo 360 | Whole Home Router M5 | CWE-259,CWE-798 | poc |
| CVE-2026-121615 | 10 | Linksys | E5600 | CWE-287 | poc |
| CVE-2026-121932 | 10 | Linksys | E5350 | CWE-77,CWE-78 | poc |
| CVE-2026-121933 | 10 | Linksys | E5350 | CWE-287,CWE-306 | poc |
| CVE-2026-122013 | 10 | Comfast | CF-WR632AX | CWE-22 | poc |
| CVE-2026-122051 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-123551 | 10 | OpenIdentityPlatform | OpenAM | CWE-201 |  |
| CVE-2026-123966 | 10 | Tenda | AC19 | CWE-119,CWE-122 |  |
| CVE-2026-124580 | 10 | Chengdu Feiyuxing Technology | VW2100 | CWE-77,CWE-78 |  |
| CVE-2026-71495 | 10 | open-wanderer | wanderer | CWE-918 | poc |
| CVE-2026-73098 | 10 | Apache Software Foundation | Apache Juneau | CWE-470 | none |
| CVE-2026-73099 | 10 | Apache Software Foundation | Apache Juneau | CWE-352 | none |
| CVE-2026-73100 | 10 | Apache Software Foundation | Apache Juneau | CWE-532 |  |
| CVE-2026-73101 | 10 | Apache Software Foundation | Apache Juneau | CWE-209 |  |
| CVE-2026-73116 | 10 | Apache Software Foundation | Apache Juneau | CWE-522 |  |
| CVE-2026-73117 | 10 | Apache Software Foundation | Apache Juneau | CWE-113 |  |
| CVE-2026-96677 | 10 | Apache Software Foundation | Apache Juneau | CWE-79 |  |
| CVE-2026-107331 | 9.9 | IBM | DataStage on Cloud Pak for Data | CWE-36 |  |
| CVE-2026-111489 | 9.9 | TPC Software | Matchpoint |  |  |
| CVE-2026-111490 | 9.9 | TPC Software | Matchpoint | CWE-639 |  |
| CVE-2026-123800 | 9.9 | supertokens | supertokens-core | CWE-639,CWE-863 |  |
| CVE-2026-16884 | 9.9 | IBM | API Connect | CWE-611 |  |
| CVE-2026-16920 | 9.9 | IBM | API Connect | CWE-441 |  |
| CVE-2026-17049 | 9.9 | IBM | API Connect | CWE-639 |  |
| CVE-2026-17117 | 9.9 | IBM | API Connect | CWE-915 | none |
| CVE-2026-17132 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17134 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17146 | 9.9 | IBM | API Connect | CWE-79 |  |
| CVE-2026-17147 | 9.9 | IBM | API Connect | CWE-22 | none |
| CVE-2026-17150 | 9.9 | IBM | API Connect | CWE-184 | none |
| CVE-2026-17158 | 9.9 | IBM | API Connect | CWE-287 |  |
| CVE-2026-17239 | 9.9 | IBM | API Connect | CWE-22 | none |

## Top proveedores (CVE nuevos)

- IBM: 322
- Google: 215
- Unknown: 168
- Apache Software Foundation: 122
- FFmpeg: 121
- JetBrains: 89
- Red Hat: 68
- openemr: 60
- Hewlett Packard Enterprise (HPE): 58
- FreeRDP: 42

## Top CWE

- CWE-79: 304
- CWE-862: 237
- CWE-639: 152
- CWE-918: 134
- CWE-863: 132
- CWE-22: 120
- CWE-200: 102
- CWE-89: 100
- CWE-787: 74
- CWE-770: 71

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
    "fetched": 3503,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2897
  }
}
```