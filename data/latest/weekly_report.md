# Reporte semanal de vulnerabilidades — 2026-10-06 a 2026-10-12

## Resumen

- KEV agregadas: **5** (catálogo total: 1739; ransomware conocido: 0)
- CVE nuevos publicados: **3241** (rechazados: 37; registros actualizados: 3742)
- Por severidad CVSS: {'CRITICAL': 365, 'HIGH': 1177, 'LOW': 132, 'MEDIUM': 1351, 'SIN_CVSS': 216}  — con CVSS: 93.3%
- SSVC (CISA ADP) explotación PoC/activa: 163; automatizable + impacto total: 204
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
| CVE-2026-105857 | 10 | payloadcms | payload | CWE-1321,CWE-94 | none |
| CVE-2026-106102 | 10 | quasarframework | quasar | CWE-116,CWE-79 | none |
| CVE-2026-108576 | 10 | TOZED | X300 | CWE-77,CWE-78 |  |
| CVE-2026-108804 | 10 | TRENDnet | TEW-751DR | CWE-77,CWE-78 |  |
| CVE-2026-108892 | 10 | Linksys | E1700 | CWE-119,CWE-121 |  |
| CVE-2026-108907 | 10 | Netcore | NR268 | CWE-287 |  |
| CVE-2026-108917 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 |  |
| CVE-2026-108918 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 |  |
| CVE-2026-12260 | 10 | NetBoard CRM | NetBoard CRM Demo Platform | CWE-89 | none |
| CVE-2026-32579 | 10 | kognetiks | Kognetiks Chatbot for WordPress | CWE-434 | none |
| CVE-2026-39770 | 10 | AmentoTech | Doctreat | CWE-434 | none |
| CVE-2026-39773 | 10 | AmentoTech | Doctreat Core | CWE-266 | none |
| CVE-2026-42696 | 10 | Royal Plugins | SiteVault – Backup, Restore, Migration & | CWE-94 | none |
| CVE-2026-63688 | 10 | Dell | Dell Container Storage Modules (CSM) | CWE-306 | none |
| CVE-2026-63692 | 10 | Dell | Container Storage Modules | CWE-306 | none |
| CVE-2026-76482 | 10 | Cisco | Cisco License On-Prem | CWE-347 | none |
| CVE-2026-94503 | 10 | PX-lab | Zombify | CWE-434 | none |
| CVE-2026-96207 | 10 | Microsoft | Microsoft Partner Center | CWE-295 | none |
| CVE-2026-108263 | 9.9 | iflytek | astron-agent | CWE-1392,CWE-306 |  |
| CVE-2026-32568 | 9.9 | JMAPlugins | WooCommerce Designer Pro | CWE-94 | none |
| CVE-2026-39755 | 9.9 | revmakx | WP Duplicate | CWE-434 | none |
| CVE-2026-39757 | 9.9 | AmentoTech | Taskbot | CWE-434 | none |
| CVE-2026-39759 | 9.9 | AmentoTech | Workreap Core | CWE-434 | none |
| CVE-2026-62024 | 9.9 | CodeBard | CodeBard Help Desk | CWE-434 | none |
| CVE-2026-62129 | 9.9 | WPFunnels | Creator LMS | CWE-434 | none |
| CVE-2026-67269 | 9.9 | Dell | Container Storage Modules (CSM) | CWE-269 | none |
| CVE-2026-77366 | 9.9 | The-40-Thieves | obsidian-tc | CWE-639,CWE-863 |  |
| CVE-2026-79798 | 9.9 | Hewlett Packard Enterprise (HPE) | ClearPass Policy Manager (CPPM) | CWE-89 | none |
| CVE-2026-85947 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-85948 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-85955 | 9.9 | Progress Software Corporation | MarkLogic Server | CWE-269 |  |
| CVE-2026-94510 | 9.9 | Microsoft | Microsoft Bookings | CWE-639 | none |
| CVE-2026-96012 | 9.9 | IBM | Db2 Mirror for i | CWE-264 |  |
| CVE-2025-70521 | 9.8 | n/a | n/a | CWE-77 | none |
| CVE-2025-71383 | 9.8 | n/a | n/a | CWE-20 | poc |
| CVE-2026-103646 | 9.8 | Unknown | Ultimate Multisite | CWE-287 | none |
| CVE-2026-103692 | 9.8 | Unknown | Frontend Dashboard | CWE-269 | none |
| CVE-2026-103889 | 9.8 | expivi | 3D Product configurator for WooCommerce | CWE-434 | none |

## Top proveedores (CVE nuevos)

- Google: 255
- Linux: 221
- Unknown: 153
- IBM: 129
- jeecgboot: 100
- n/a: 65
- Brocade: 61
- Red Hat: 56
- ImageMagick: 47
- Apache Software Foundation: 41

## Top CWE

- CWE-862: 344
- CWE-79: 318
- CWE-89: 138
- CWE-863: 131
- CWE-639: 104
- CWE-22: 100
- CWE-502: 91
- CWE-200: 81
- CWE-918: 66
- CWE-94: 62

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
    "fetched": 3278,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2894
  }
}
```