# Reporte semanal de vulnerabilidades — 2026-10-08 a 2026-10-14

## Resumen

- KEV agregadas: **7** (catálogo total: 1741; ransomware conocido: 0)
- CVE nuevos publicados: **4781** (rechazados: 39; registros actualizados: 3915)
- Por severidad CVSS: {'HIGH': 2215, 'MEDIUM': 1803, 'CRITICAL': 423, 'SIN_CVSS': 210, 'LOW': 130}  — con CVSS: 95.6%
- SSVC (CISA ADP) explotación PoC/activa: 397; automatizable + impacto total: 227
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-08 | CVE-2015-5477 | ISC BIND |  ISC BIND Data Processing Errors Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2016-3081 | Apache Struts | Apache Struts Command Injection Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2023-22894 | Strapi Strapi | Strapi Cleartext Storage of Sensitive Information Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2021-3199 | ONLYOFFICE Docs | ONLYOFFICE Docs Server Path Traversal Vulnerability | 2026-10-11 | Unknown |
| 2026-10-08 | CVE-2015-3306 | ProFTPD ProFTPD | ProFTPD Improper Access Control Vulnerability | 2026-10-11 | Unknown |
| 2026-10-13 | CVE-2026-104935 | Ivanti Connect Secure | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | 2026-10-16 | Unknown |
| 2026-10-13 | CVE-2026-96951 | Microsoft Windows | Microsoft Windows Command Injection Vulnerability | 2026-10-16 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2024-34323 | 10 | n/a | n/a | CWE-639 | none |
| CVE-2026-103849 | 10 | Adobe | Adobe Commerce | CWE-1336 |  |
| CVE-2026-105899 | 10 | Adobe | ColdFusion 2025 | CWE-434 | none |
| CVE-2026-106622 | 10 | Adobe | ColdFusion 2025 | CWE-918 | none |
| CVE-2026-106624 | 10 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-107594 | 10 | Unknown | File Upload to Order | CWE-73 | none |
| CVE-2026-108576 | 10 | TOZED | X300 | CWE-77,CWE-78 | none |
| CVE-2026-108804 | 10 | TRENDnet | TEW-751DR | CWE-77,CWE-78 |  |
| CVE-2026-108892 | 10 | Linksys | E1700 | CWE-119,CWE-121 |  |
| CVE-2026-108907 | 10 | Netcore | NR268 | CWE-287 | poc |
| CVE-2026-108917 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-108918 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 |  |
| CVE-2026-109109 | 10 | Wavlink | WL-WN530BE1-A | CWE-119,CWE-121 | none |
| CVE-2026-109110 | 10 | Wavlink | WL-WN592AX6 | CWE-77,CWE-78 |  |
| CVE-2026-110130 | 10 | Finsys | dockhand | CWE-288 |  |
| CVE-2026-12260 | 10 | NetBoard CRM | NetBoard CRM Demo Platform | CWE-89 | none |
| CVE-2026-42696 | 10 | Royal Plugins | SiteVault – Backup, Restore, Migration & | CWE-94 | none |
| CVE-2026-48382 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 |  |
| CVE-2026-48383 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 |  |
| CVE-2026-55675 | 10 | saltyorg | docs | CWE-1357,CWE-829 | poc |
| CVE-2026-65162 | 10 | NVIDIA | AIStore framework | CWE-250 | none |
| CVE-2026-89111 | 10 | SAP_SE | SAP Cloud | CWE-918 |  |
| CVE-2026-89309 | 10 | JTL SW GmbH | JTL-WMS | CWE-306 |  |
| CVE-2026-90532 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-94503 | 10 | PX-lab | Zombify | CWE-434 | none |
| CVE-2026-94603 | 10 | podman-container-tools | podman | CWE-693 | none |
| CVE-2026-96207 | 10 | Microsoft | Microsoft Partner Center | CWE-295 | none |
| CVE-2026-97229 | 10 | GitLab | GitLab | CWE-190 | none |
| CVE-2026-103848 | 9.9 | Adobe | Adobe Experience Manager 6.5 LTS | CWE-78 | none |
| CVE-2026-105895 | 9.9 | Adobe | Adobe Experience Manager 6.5 | CWE-20 | none |
| CVE-2026-105903 | 9.9 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-106042 | 9.9 | Ivanti | Xtraction | CWE-73 | none |
| CVE-2026-106612 | 9.9 | Adobe | ColdFusion 2025 | CWE-863 | none |
| CVE-2026-108263 | 9.9 | iflytek | astron-agent | CWE-1392,CWE-306 | none |
| CVE-2026-109412 | 9.9 | Ivanti | Neurons Patch for Intune | CWE-749 |  |
| CVE-2026-62024 | 9.9 | CodeBard | CodeBard Help Desk | CWE-434 | none |
| CVE-2026-62129 | 9.9 | WPFunnels | Creator LMS | CWE-434 | none |
| CVE-2026-75732 | 9.9 | Adobe | Adobe Experience Manager 6.5 LTS | CWE-863 | none |
| CVE-2026-77366 | 9.9 | The-40-Thieves | obsidian-tc | CWE-639,CWE-863 | none |
| CVE-2026-77459 | 9.9 | argoproj | argo-cd | CWE-863 |  |

## Top proveedores (CVE nuevos)

- Microsoft: 1414
- Adobe: 177
- Unknown: 172
- IBM: 172
- jeecgboot: 100
- frappe: 89
- Mozilla: 83
- n/a: 66
- Linux: 57
- Red Hat: 46

## Top CWE

- CWE-416: 398
- CWE-79: 393
- CWE-862: 390
- CWE-122: 346
- CWE-125: 278
- CWE-89: 163
- CWE-863: 144
- CWE-639: 132
- CWE-22: 115
- CWE-502: 99

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.13"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4820,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4562
  }
}
```