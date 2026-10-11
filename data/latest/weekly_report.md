# Reporte semanal de vulnerabilidades — 2026-10-05 a 2026-10-11

## Resumen

- KEV agregadas: **5** (catálogo total: 1739; ransomware conocido: 0)
- CVE nuevos publicados: **3144** (rechazados: 31; registros actualizados: 3813)
- Por severidad CVSS: {'HIGH': 1134, 'MEDIUM': 1319, 'LOW': 122, 'CRITICAL': 360, 'SIN_CVSS': 209}  — con CVSS: 93.4%
- SSVC (CISA ADP) explotación PoC/activa: 286; automatizable + impacto total: 213
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
| CVE-2026-100103 | 10 | Perfoce | P4 (Helix Core) | CWE-1392 | none |
| CVE-2026-102255 | 10 | SonicWall | SMA1000 | CWE-441,CWE-918 | none |
| CVE-2026-105284 | 10 | Totolink | A3002MU | CWE-266,CWE-285 | poc |
| CVE-2026-105285 | 10 | Totolink | A3002MU | CWE-119,CWE-121 | poc |
| CVE-2026-105484 | 10 | TOTOLINK | X6000R | CWE-77,CWE-78 | none |
| CVE-2026-105857 | 10 | payloadcms | payload | CWE-1321,CWE-94 | none |
| CVE-2026-106102 | 10 | quasarframework | quasar | CWE-116,CWE-79 | none |
| CVE-2026-108576 | 10 | TOZED | X300 | CWE-77,CWE-78 |  |
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
| CVE-2026-105636 | 9.9 | makeplane | plane | CWE-918 | poc |
| CVE-2026-105691 | 9.9 | penpot | penpot | CWE-78 | poc |
| CVE-2026-105697 | 9.9 | langflow-ai | langflow | CWE-78 | none |
| CVE-2026-105740 | 9.9 | langflow-ai | langflow | CWE-78 | poc |
| CVE-2026-108263 | 9.9 | iflytek | astron-agent | CWE-1392,CWE-306 |  |
| CVE-2026-32568 | 9.9 | JMAPlugins | WooCommerce Designer Pro | CWE-94 | none |
| CVE-2026-39755 | 9.9 | revmakx | WP Duplicate | CWE-434 | none |
| CVE-2026-39757 | 9.9 | AmentoTech | Taskbot | CWE-434 | none |
| CVE-2026-39759 | 9.9 | AmentoTech | Workreap Core | CWE-434 | none |
| CVE-2026-62024 | 9.9 | CodeBard | CodeBard Help Desk | CWE-434 | none |
| CVE-2026-62129 | 9.9 | WPFunnels | Creator LMS | CWE-434 | none |
| CVE-2026-67269 | 9.9 | Dell | Container Storage Modules (CSM) | CWE-269 | none |
| CVE-2026-79798 | 9.9 | Hewlett Packard Enterprise (HPE) | ClearPass Policy Manager (CPPM) | CWE-89 | none |
| CVE-2026-94510 | 9.9 | Microsoft | Microsoft Bookings | CWE-639 | none |
| CVE-2025-70521 | 9.8 | n/a | n/a | CWE-77 | none |
| CVE-2025-71383 | 9.8 | n/a | n/a | CWE-20 | poc |
| CVE-2026-103646 | 9.8 | Unknown | Ultimate Multisite | CWE-287 | none |
| CVE-2026-103692 | 9.8 | Unknown | Frontend Dashboard | CWE-269 | none |
| CVE-2026-103889 | 9.8 | expivi | 3D Product configurator for WooCommerce | CWE-434 |  |
| CVE-2026-104028 | 9.8 | Unknown | Anton Extensions | CWE-434 | none |
| CVE-2026-104334 | 9.8 | IBM | Langflow OSS | CWE-94 | none |

## Top proveedores (CVE nuevos)

- Google: 282
- Linux: 220
- Unknown: 152
- IBM: 117
- jeecgboot: 100
- n/a: 80
- Red Hat: 73
- Brocade: 61
- Apache Software Foundation: 44
- Dell: 41

## Top CWE

- CWE-862: 340
- CWE-79: 319
- CWE-89: 144
- CWE-863: 128
- CWE-639: 105
- CWE-22: 97
- CWE-502: 97
- CWE-200: 78
- CWE-918: 75
- CWE-94: 65

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
    "fetched": 3175,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3034
  }
}
```