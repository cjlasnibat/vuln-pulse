# Reporte semanal de vulnerabilidades — 2026-11-02 a 2026-11-08

## Resumen

- KEV agregadas: **3** (catálogo total: 1769; ransomware conocido: 0)
- CVE nuevos publicados: **3146** (rechazados: 268; registros actualizados: 7494)
- Por severidad CVSS: {'MEDIUM': 1258, 'CRITICAL': 297, 'LOW': 154, 'HIGH': 1188, 'SIN_CVSS': 249}  — con CVSS: 92.1%
- SSVC (CISA ADP) explotación PoC/activa: 228; automatizable + impacto total: 72
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-03 | CVE-2026-119977 | WordPress WordPress Core | WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability | 2026-11-06 | Unknown |
| 2026-11-04 | CVE-2024-27834 | Apple Multiple Products | Apple Multiple Products Improper Authentication Vulnerability | 2026-11-18 | Unknown |
| 2026-11-06 | CVE-2026-19868 | SonicWall SonicOS SSLVPN | SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability | 2026-11-20 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109469 | 10 | Microsoft | Entra Device Registration | CWE-639 |  |
| CVE-2026-118423 | 10 | Unknown | WP Libre Form | CWE-434 | none |
| CVE-2026-120344 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 | poc |
| CVE-2026-120345 | 10 | WAVLINK | WN551X3-A | CWE-77,CWE-78 | poc |
| CVE-2026-121489 | 10 | Apache Software Foundation | Apache Juneau | CWE-22 |  |
| CVE-2026-121606 | 10 | Qihoo 360 | D621-2 | CWE-345,CWE-347 |  |
| CVE-2026-121607 | 10 | Qihoo 360 | D603-2 | CWE-77,CWE-78 |  |
| CVE-2026-121609 | 10 | Qihoo 360 | Whole Home Router M5 | CWE-259,CWE-798 |  |
| CVE-2026-121615 | 10 | Linksys | E5600 | CWE-287 |  |
| CVE-2026-121932 | 10 | Linksys | E5350 | CWE-77,CWE-78 |  |
| CVE-2026-121933 | 10 | Linksys | E5350 | CWE-287,CWE-306 |  |
| CVE-2026-122013 | 10 | Comfast | CF-WR632AX | CWE-22 |  |
| CVE-2026-122051 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-123551 | 10 | OpenIdentityPlatform | OpenAM | CWE-201 |  |
| CVE-2026-123966 | 10 | Tenda | AC19 | CWE-119,CWE-122 |  |
| CVE-2026-71495 | 10 | open-wanderer | wanderer | CWE-918 |  |
| CVE-2026-73098 | 10 | Apache Software Foundation | Apache Juneau | CWE-470 | none |
| CVE-2026-73099 | 10 | Apache Software Foundation | Apache Juneau | CWE-352 | none |
| CVE-2026-73100 | 10 | Apache Software Foundation | Apache Juneau | CWE-532 |  |
| CVE-2026-73101 | 10 | Apache Software Foundation | Apache Juneau | CWE-209 |  |
| CVE-2026-73116 | 10 | Apache Software Foundation | Apache Juneau | CWE-522 |  |
| CVE-2026-73117 | 10 | Apache Software Foundation | Apache Juneau | CWE-113 |  |
| CVE-2026-96677 | 10 | Apache Software Foundation | Apache Juneau | CWE-79 |  |
| CVE-2026-111489 | 9.9 | TPC Software | Matchpoint |  |  |
| CVE-2026-111490 | 9.9 | TPC Software | Matchpoint | CWE-639 |  |
| CVE-2026-16884 | 9.9 | IBM | API Connect | CWE-611 |  |
| CVE-2026-16920 | 9.9 | IBM | API Connect | CWE-441 |  |
| CVE-2026-17049 | 9.9 | IBM | API Connect | CWE-639 |  |
| CVE-2026-17117 | 9.9 | IBM | API Connect | CWE-915 |  |
| CVE-2026-17132 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17134 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17146 | 9.9 | IBM | API Connect | CWE-79 |  |
| CVE-2026-17147 | 9.9 | IBM | API Connect | CWE-22 |  |
| CVE-2026-17150 | 9.9 | IBM | API Connect | CWE-184 |  |
| CVE-2026-17158 | 9.9 | IBM | API Connect | CWE-287 |  |
| CVE-2026-17239 | 9.9 | IBM | API Connect | CWE-22 |  |
| CVE-2026-17298 | 9.9 | IBM | API Connect | CWE-918 |  |
| CVE-2026-17336 | 9.9 | IBM | API Connect | CWE-89 |  |
| CVE-2026-17342 | 9.9 | IBM | API Connect | CWE-94 |  |
| CVE-2026-17354 | 9.9 | IBM | API Connect | CWE-22 |  |

## Top proveedores (CVE nuevos)

- Google: 354
- IBM: 243
- Unknown: 146
- Apache Software Foundation: 98
- JetBrains: 89
- Linux: 61
- openemr: 60
- Hewlett Packard Enterprise (HPE): 56
- Red Hat: 50
- FreeRDP: 42

## Top CWE

- CWE-79: 278
- CWE-862: 242
- CWE-639: 156
- CWE-918: 129
- CWE-863: 123
- CWE-22: 110
- CWE-89: 100
- CWE-200: 81
- CWE-416: 81
- CWE-787: 75

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.06"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3414,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3057
  }
}
```