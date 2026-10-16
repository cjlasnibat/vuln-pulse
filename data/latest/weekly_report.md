# Reporte semanal de vulnerabilidades — 2026-10-10 a 2026-10-16

## Resumen

- KEV agregadas: **7** (catálogo total: 1746; ransomware conocido: 0)
- CVE nuevos publicados: **5217** (rechazados: 27; registros actualizados: 4856)
- Por severidad CVSS: {'SIN_CVSS': 146, 'CRITICAL': 445, 'HIGH': 2476, 'MEDIUM': 2017, 'LOW': 133}  — con CVSS: 97.2%
- SSVC (CISA ADP) explotación PoC/activa: 630; automatizable + impacto total: 251
- EPSS ≥ 10%: 2

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-13 | CVE-2026-104935 | Ivanti Connect Secure | Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | 2026-10-16 | Unknown |
| 2026-10-13 | CVE-2026-96951 | Microsoft Windows | Microsoft Windows Command Injection Vulnerability | 2026-10-16 | Unknown |
| 2026-10-14 | CVE-2026-105134 | Ahsay AhsayCBS | Ahsay AhsayCBS Command Injection Vulnerability | 2026-10-17 | Unknown |
| 2026-10-14 | CVE-2026-76519 | Cisco Secure Email Gateway | Cisco Secure Email Gateway Relative Path Traversal Vulnerability | 2026-10-17 | Unknown |
| 2026-10-14 | CVE-2026-105133 | Ahsay AhsayCBS | Ahsay AhsayCBS Improper Authentication Vulnerability | 2026-10-17 | Unknown |
| 2026-10-14 | CVE-2026-0322 | Palo Alto Networks PAN-OS | Palo Alto Networks PAN-OS Code Injection Vulnerability | 2026-10-17 | Unknown |
| 2026-10-15 | CVE-2026-21589 | Atlassian Multiple Products | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | 2026-10-18 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2024-34323 | 10 | n/a | n/a | CWE-639 | none |
| CVE-2026-103849 | 10 | Adobe | Adobe Commerce | CWE-1336 | none |
| CVE-2026-105899 | 10 | Adobe | ColdFusion 2025 | CWE-434 | none |
| CVE-2026-106622 | 10 | Adobe | ColdFusion 2025 | CWE-918 | none |
| CVE-2026-106624 | 10 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-107594 | 10 | Unknown | File Upload to Order | CWE-73 | none |
| CVE-2026-108576 | 10 | TOZED | X300 | CWE-77,CWE-78 | none |
| CVE-2026-108804 | 10 | TRENDnet | TEW-751DR | CWE-77,CWE-78 | poc |
| CVE-2026-108892 | 10 | Linksys | E1700 | CWE-119,CWE-121 | poc |
| CVE-2026-108907 | 10 | Netcore | NR268 | CWE-287 | poc |
| CVE-2026-108917 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-108918 | 10 | Edimax | BR-6208AC | CWE-74,CWE-77 | poc |
| CVE-2026-109109 | 10 | Wavlink | WL-WN530BE1-A | CWE-119,CWE-121 | none |
| CVE-2026-109110 | 10 | Wavlink | WL-WN592AX6 | CWE-77,CWE-78 | poc |
| CVE-2026-110130 | 10 | Finsys | dockhand | CWE-288 | poc |
| CVE-2026-110536 | 10 | D-Link | DIR-868L | CWE-77,CWE-78 | poc |
| CVE-2026-110957 | 10 | Wavlink | WL-WN530BE2-A | CWE-77,CWE-78 |  |
| CVE-2026-110958 | 10 | Wavlink | WN530HG4B | CWE-119,CWE-122 | poc |
| CVE-2026-42696 | 10 | Royal Plugins | SiteVault – Backup, Restore, Migration & | CWE-94 | none |
| CVE-2026-48382 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-48383 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-55572 | 10 | e107inc | e107 | CWE-89 |  |
| CVE-2026-55675 | 10 | saltyorg | docs | CWE-1357,CWE-829 | poc |
| CVE-2026-65162 | 10 | NVIDIA | AIStore framework | CWE-250 | none |
| CVE-2026-89111 | 10 | SAP_SE | SAP Cloud | CWE-918 | none |
| CVE-2026-89309 | 10 | JTL SW GmbH | JTL-WMS | CWE-306 |  |
| CVE-2026-90532 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-94169 | 10 | Theme-one | The Grid | CWE-94 | none |
| CVE-2026-94603 | 10 | podman-container-tools | podman | CWE-693 | none |
| CVE-2026-97229 | 10 | GitLab | GitLab | CWE-190 | none |
| CVE-2026-103848 | 9.9 | Adobe | Adobe Experience Manager 6.5 LTS | CWE-78 | none |
| CVE-2026-105037 | 9.9 | EnergizeLab | station-middleware | CWE-73 |  |
| CVE-2026-105895 | 9.9 | Adobe | Adobe Experience Manager 6.5 | CWE-20 | none |
| CVE-2026-105903 | 9.9 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-106042 | 9.9 | Ivanti | Xtraction | CWE-73 | none |
| CVE-2026-106612 | 9.9 | Adobe | ColdFusion 2025 | CWE-863 | none |
| CVE-2026-108390 | 9.9 | hestiacp | hestiacp | CWE-427,CWE-88 | poc |
| CVE-2026-109412 | 9.9 | Ivanti | Neurons Patch for Intune | CWE-749 | none |
| CVE-2026-57155 | 9.9 | opnsense | core | CWE-22,CWE-73 | poc |
| CVE-2026-62024 | 9.9 | CodeBard | CodeBard Help Desk | CWE-434 | none |

## Top proveedores (CVE nuevos)

- Microsoft: 1439
- Adobe: 177
- Unknown: 159
- Juniper Networks: 153
- jeecgboot: 100
- frappe: 91
- Mozilla: 83
- IBM: 79
- n/a: 65
- Red Hat: 60

## Top CWE

- CWE-79: 431
- CWE-862: 414
- CWE-416: 407
- CWE-122: 373
- CWE-125: 325
- CWE-89: 177
- CWE-639: 159
- CWE-863: 156
- CWE-22: 131
- CWE-787: 114

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.15"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 5244,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 5173
  }
}
```