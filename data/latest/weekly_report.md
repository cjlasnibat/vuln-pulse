# Reporte semanal de vulnerabilidades — 2026-10-07 a 2026-10-13

## Resumen

- KEV agregadas: **5** (catálogo total: 1739; ransomware conocido: 0)
- CVE nuevos publicados: **2959** (rechazados: 38; registros actualizados: 3982)
- Por severidad CVSS: {'HIGH': 1044, 'SIN_CVSS': 128, 'MEDIUM': 1355, 'LOW': 123, 'CRITICAL': 309}  — con CVSS: 95.7%
- SSVC (CISA ADP) explotación PoC/activa: 261; automatizable + impacto total: 171
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-08 | CVE-2015-5477 | ISC BIND |  ISC BIND Data Processing Errors Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2016-3081 | Apache Struts | Apache Struts Command Injection Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2023-22894 | Strapi Strapi | Strapi Cleartext Storage of Sensitive Information Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2021-3199 | ONLYOFFICE Docs | ONLYOFFICE Docs Server Path Traversal Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2015-3306 | ProFTPD ProFTPD | ProFTPD Improper Access Control Vulnerability | 2026-10-11 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2025-70518 | 10 | n/a | n/a | CWE-77 | poc |
| CVE-2026-102255 | 10 | SonicWall | SMA1000 | CWE-441,CWE-918 | none |
| CVE-2026-108576 | 10 | TOZED | X300 | CWE-77,CWE-78 |  |
| CVE-2026-108804 | 10 | TRENDnet | TEW-751DR | CWE-77,CWE-78 |  |
| CVE-2026-108892 | 10 | Linksys | E1700 | CWE-119,CWE-121 |  |
| CVE-2026-108907 | 10 | Netcore | NR268 | CWE-287 | poc |
| CVE-2026-108917 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-108918 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 |  |
| CVE-2026-109109 | 10 | Wavlink | WL-WN530BE1-A | CWE-119,CWE-121 |  |
| CVE-2026-109110 | 10 | Wavlink | WL-WN592AX6 | CWE-77,CWE-78 |  |
| CVE-2026-12260 | 10 | NetBoard CRM | NetBoard CRM Demo Platform | CWE-89 | none |
| CVE-2026-42696 | 10 | Royal Plugins | SiteVault – Backup, Restore, Migration & | CWE-94 | none |
| CVE-2026-55675 | 10 | saltyorg | docs | CWE-1357,CWE-829 | poc |
| CVE-2026-65162 | 10 | NVIDIA | AIStore framework | CWE-250 | none |
| CVE-2026-76482 | 10 | Cisco | Cisco License On-Prem | CWE-347 | none |
| CVE-2026-89111 | 10 | SAP_SE | SAP Cloud | CWE-918 |  |
| CVE-2026-94503 | 10 | PX-lab | Zombify | CWE-434 | none |
| CVE-2026-94603 | 10 | podman-container-tools | podman | CWE-693 |  |
| CVE-2026-96207 | 10 | Microsoft | Microsoft Partner Center | CWE-295 | none |
| CVE-2026-97229 | 10 | GitLab | GitLab | CWE-190 |  |
| CVE-2026-106042 | 9.9 | Ivanti | Xtraction | CWE-73 |  |
| CVE-2026-108263 | 9.9 | iflytek | astron-agent | CWE-1392,CWE-306 |  |
| CVE-2026-109412 | 9.9 | Ivanti | Neurons Patch for Intune | CWE-749 |  |
| CVE-2026-62024 | 9.9 | CodeBard | CodeBard Help Desk | CWE-434 | none |
| CVE-2026-62129 | 9.9 | WPFunnels | Creator LMS | CWE-434 | none |
| CVE-2026-77366 | 9.9 | The-40-Thieves | obsidian-tc | CWE-639,CWE-863 | none |
| CVE-2026-77459 | 9.9 | argoproj | argo-cd | CWE-863 |  |
| CVE-2026-85947 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-85948 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-85955 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-89107 | 9.9 | SAP_SE | SAP S/4HANA (Manage Substitution/Validat | CWE-94 | none |
| CVE-2026-89110 | 9.9 | SAP_SE | SAP NetWeaver Visual Composer | CWE-749 | none |
| CVE-2026-94510 | 9.9 | Microsoft | Microsoft Bookings | CWE-639 | none |
| CVE-2026-96012 | 9.9 | IBM | Db2 Mirror for i | CWE-264 | none |
| CVE-2026-96119 | 9.9 | IBM | i | CWE-94 | none |
| CVE-2025-70521 | 9.8 | n/a | n/a | CWE-77 | none |
| CVE-2026-103646 | 9.8 | Unknown | Ultimate Multisite | CWE-287 | none |
| CVE-2026-103692 | 9.8 | Unknown | Frontend Dashboard | CWE-269 | none |
| CVE-2026-103889 | 9.8 | expivi | 3D Product configurator for WooCommerce | CWE-434 | none |
| CVE-2026-104028 | 9.8 | Unknown | Anton Extensions | CWE-434 | none |

## Top proveedores (CVE nuevos)

- IBM: 159
- Unknown: 149
- jeecgboot: 100
- frappe: 89
- Mozilla: 81
- n/a: 80
- Brocade: 61
- Red Hat: 50
- ImageMagick: 48
- FreeRDP: 39

## Top CWE

- CWE-862: 345
- CWE-79: 322
- CWE-89: 151
- CWE-639: 115
- CWE-22: 102
- CWE-863: 91
- CWE-502: 89
- CWE-200: 74
- CWE-918: 64
- CWE-74: 63

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.08"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2997,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2572
  }
}
```