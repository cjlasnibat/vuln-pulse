# Reporte semanal de vulnerabilidades — 2026-09-28 a 2026-10-04

## Resumen

- KEV agregadas: **6** (catálogo total: 1734; ransomware conocido: 0)
- CVE nuevos publicados: **2510** (rechazados: 12; registros actualizados: 3214)
- Por severidad CVSS: {'MEDIUM': 1014, 'CRITICAL': 290, 'LOW': 105, 'HIGH': 1050, 'SIN_CVSS': 51}  — con CVSS: 98.0%
- SSVC (CISA ADP) explotación PoC/activa: 352; automatizable + impacto total: 134
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-09-29 | CVE-2026-86950 | Apple Multiple Products | Apple Multiple Products Out-of-Bounds Write Vulnerability | 2026-10-02 | Unknown |
| 2026-09-30 | CVE-2026-76504 | Cisco Catalyst SD-WAN Manager | Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability | 2026-10-03 | Unknown |
| 2026-10-01 | CVE-2026-104286 | Fortinet FortiMail | Fortinet FortiMail Path Traversal Vulnerability | 2026-10-04 | Unknown |
| 2026-10-02 | CVE-2026-102490 | Zammad GmbH Zammad | Zammad GmbH Zammad Improper Privilege Management Vulnerability | 2026-10-05 | Unknown |
| 2026-10-02 | CVE-2026-102489 | Zammad GmbH Zammad | Zammad GmbH Zammad Session Fixation Vulnerability | 2026-10-05 | Unknown |
| 2026-10-04 | CVE-2026-88779 | Citrix NetScaler | Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability | 2026-10-07 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-101000 | 10 | Netcore | NBR100V2 | CWE-862,CWE-863 | poc |
| CVE-2026-101001 | 10 | Netcore | NBR200V2 | CWE-77,CWE-78 | poc |
| CVE-2026-101039 | 10 | FAST | FAC1900R | CWE-119,CWE-121 | poc |
| CVE-2026-101072 | 10 | Netcore | NR289-GE | CWE-77,CWE-78 | poc |
| CVE-2026-101075 | 10 | Netcore | NR289-GE | CWE-77,CWE-78 | poc |
| CVE-2026-101076 | 10 | Netcore | NR289-GE | CWE-77,CWE-78 | poc |
| CVE-2026-101077 | 10 | Netcore | NR289-GE | CWE-287,CWE-306 | poc |
| CVE-2026-101148 | 10 | Unknown | BackupSheep WordPress Backup Plugin | CWE-73 | none |
| CVE-2026-102240 | 10 | Netcore | NAP930 | CWE-77,CWE-78 | poc |
| CVE-2026-102427 | 10 | ordasoft.com | OrdaSoft Joomla CCK | CWE-434 | none |
| CVE-2026-103956 | 10 | AWS | loom | CWE-1188,CWE-306 | none |
| CVE-2026-104610 | 10 | Tenda | HG7 | CWE-119,CWE-121 | poc |
| CVE-2026-105134 | 10 | Ahsay | AhsayCBS | CWE-77,CWE-78 |  |
| CVE-2026-105135 | 10 | InternLM | MindSearch | CWE-74,CWE-94 |  |
| CVE-2026-55107 | 10 | elct9620 | kobako | CWE-470,CWE-94 | poc |
| CVE-2026-55393 | 10 | Teledyne FLIR | Aware2 | CWE-22 | none |
| CVE-2026-71379 | 10 | Toptech Systems | TMS7 | CWE-552 | none |
| CVE-2026-76570 | 10 | joomcode.com | JCTables extension for Joomla | CWE-89 | none |
| CVE-2026-96349 | 10 | SiteSkite | SiteSkite | CWE-94 | none |
| CVE-2026-96587 | 10 | Viidure | Dashcam Android Application | CWE-798 | none |
| CVE-2026-79901 | 9.9 | Fortra | BoKS Manager boks-server | CWE-338 | none |
| CVE-2026-82377 | 9.9 | Apache Software Foundation | Apache Roller | CWE-862 | none |
| CVE-2026-84154 | 9.9 | Dassault Systèmes | GEOVIA Geospatial Data Manager | CWE-94 | none |
| CVE-2026-85526 | 9.9 | Canonical | LXD | CWE-22 | poc |
| CVE-2026-87799 | 9.9 | Canonical | LXD | CWE-59 | none |
| CVE-2026-90970 | 9.9 | GitLab | GitLab AI Gateway | CWE-1336 | none |
| CVE-2026-93698 | 9.9 | Webpros | cPanel | CWE-78 | none |
| CVE-2026-96658 | 9.9 | Red Hat | Red Hat Satellite 6.16 for RHEL 8 | CWE-94 | none |
| CVE-2024-31026 | 9.8 | n/a | n/a | CWE-94 | poc |
| CVE-2026-100512 | 9.8 | Hook & Filter | Nested Pages | CWE-502 | none |
| CVE-2026-100788 | 9.8 | Mozilla | Thunderbird | CWE-824 | none |
| CVE-2026-100810 | 9.8 | Mozilla | Thunderbird | CWE-200 | none |
| CVE-2026-102115 | 9.8 | Kiteworks | Core | CWE-640 | none |
| CVE-2026-103044 | 9.8 | The Wikimedia Foundation | Mediawiki - EasyTimeline extension | CWE-22,CWE-91 | none |
| CVE-2026-103110 | 9.8 | Pexip | Infinity | CWE-787 | none |
| CVE-2026-103752 | 9.8 | Paul Ryan | Authorizer | CWE-266 | none |
| CVE-2026-104286 | 9.8 | Fortinet | FortiMail | CWE-22 | active |
| CVE-2026-104846 | 9.8 | lxsmnsyc | seroval | CWE-843 |  |
| CVE-2026-105105 | 9.8 | NASA-AMMOS | AIT-Core | CWE-306 | none |
| CVE-2026-12627 | 9.8 | Fortra | Fortra's Core Privileged Access Manager  | CWE-121 | none |

## Top proveedores (CVE nuevos)

- Apache Software Foundation: 155
- Google: 155
- NVIDIA: 116
- Unknown: 100
- n/a: 91
- Mozilla: 78
- Kiteworks: 61
- Red Hat: 46
- JetBrains: 38
- YesWiki: 37

## Top CWE

- CWE-79: 331
- CWE-862: 132
- CWE-89: 112
- CWE-22: 104
- CWE-416: 95
- CWE-863: 78
- CWE-770: 69
- CWE-918: 65
- CWE-78: 65
- CWE-787: 65

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.04"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2522,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2479
  }
}
```