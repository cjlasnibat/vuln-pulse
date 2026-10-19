# Reporte semanal de vulnerabilidades — 2026-10-13 a 2026-10-19

## Resumen

- KEV agregadas: **9** (catálogo total: 1748; ransomware conocido: 0)
- CVE nuevos publicados: **5028** (rechazados: 30; registros actualizados: 8864)
- Por severidad CVSS: {'MEDIUM': 1770, 'HIGH': 2234, 'SIN_CVSS': 578, 'CRITICAL': 356, 'LOW': 90}  — con CVSS: 88.5%
- SSVC (CISA ADP) explotación PoC/activa: 515; automatizable + impacto total: 196
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
| 2026-10-16 | CVE-2026-102764 | BeyondTrust Remote Support | BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability | 2026-10-19 | Unknown |
| 2026-10-16 | CVE-2025-61624 | Fortinet Multiple Products | Fortinet Multiple Products Path Traversal Vulnerability | 2026-10-19 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2024-34323 | 10 | n/a | n/a | CWE-639 | none |
| CVE-2026-103849 | 10 | Adobe | Adobe Commerce | CWE-1336 | poc |
| CVE-2026-105899 | 10 | Adobe | ColdFusion 2025 | CWE-434 | none |
| CVE-2026-106622 | 10 | Adobe | ColdFusion 2025 | CWE-918 | none |
| CVE-2026-106624 | 10 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-107594 | 10 | Unknown | File Upload to Order | CWE-73 | none |
| CVE-2026-109109 | 10 | Wavlink | WL-WN530BE1-A | CWE-119,CWE-121 | none |
| CVE-2026-109110 | 10 | Wavlink | WL-WN592AX6 | CWE-77,CWE-78 | poc |
| CVE-2026-110130 | 10 | Finsys | dockhand | CWE-288 | poc |
| CVE-2026-110536 | 10 | D-Link | DIR-868L | CWE-77,CWE-78 | poc |
| CVE-2026-110957 | 10 | Wavlink | WL-WN530BE2-A | CWE-77,CWE-78 |  |
| CVE-2026-110958 | 10 | Wavlink | WN530HG4B | CWE-119,CWE-122 | poc |
| CVE-2026-111057 | 10 | mljar | mercury | CWE-185,CWE-284 |  |
| CVE-2026-48382 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-48383 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-55572 | 10 | e107inc | e107 | CWE-89 |  |
| CVE-2026-55675 | 10 | saltyorg | docs | CWE-1357,CWE-829 | poc |
| CVE-2026-65162 | 10 | NVIDIA | AIStore framework | CWE-250 | none |
| CVE-2026-78162 | 10 | Apache Software Foundation | Apache Camel | CWE-502 |  |
| CVE-2026-89309 | 10 | JTL SW GmbH | JTL-WMS | CWE-306 | none |
| CVE-2026-90532 | 10 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-863 | none |
| CVE-2026-94169 | 10 | Theme-one | The Grid | CWE-94 | none |
| CVE-2026-94603 | 10 | podman-container-tools | podman | CWE-693 | none |
| CVE-2026-95182 | 10 | n/a | n/a | CWE-426 | poc |
| CVE-2026-103848 | 9.9 | Adobe | Adobe Experience Manager 6.5 LTS | CWE-78 | none |
| CVE-2026-105037 | 9.9 | EnergizeLab | station-middleware | CWE-73 | none |
| CVE-2026-105895 | 9.9 | Adobe | Adobe Experience Manager 6.5 | CWE-20 | none |
| CVE-2026-105903 | 9.9 | Adobe | ColdFusion 2025 | CWE-94 | none |
| CVE-2026-106042 | 9.9 | Ivanti | Xtraction | CWE-73 | none |
| CVE-2026-106612 | 9.9 | Adobe | ColdFusion 2025 | CWE-863 | none |
| CVE-2026-108390 | 9.9 | hestiacp | hestiacp | CWE-427,CWE-88 | poc |
| CVE-2026-109412 | 9.9 | Ivanti | Neurons Patch for Intune | CWE-749 | none |
| CVE-2026-110887 | 9.9 | HivePress | HivePress | CWE-94 | none |
| CVE-2026-111406 | 9.9 | PT Norther Lights Production | MapSVG | CWE-434 | none |
| CVE-2026-57155 | 9.9 | opnsense | core | CWE-22,CWE-73 | poc |
| CVE-2026-75732 | 9.9 | Adobe | Adobe Experience Manager 6.5 LTS | CWE-863 | none |
| CVE-2026-77459 | 9.9 | argoproj | argo-cd | CWE-863 | none |
| CVE-2026-77524 | 9.9 | kedacore | keda | CWE-269,CWE-918 |  |
| CVE-2026-85746 | 9.9 | MariaDB | server | CWE-787 | none |
| CVE-2026-85748 | 9.9 | MariaDB | server | CWE-416 | none |

## Top proveedores (CVE nuevos)

- Microsoft: 1441
- Linux: 483
- Adobe: 177
- Juniper Networks: 153
- Unknown: 121
- Mozilla: 83
- Apache Software Foundation: 79
- n/a: 66
- Red Hat: 64
- Google: 49

## Top CWE

- CWE-416: 402
- CWE-122: 373
- CWE-125: 337
- CWE-79: 296
- CWE-862: 246
- CWE-639: 168
- CWE-863: 138
- CWE-89: 133
- CWE-787: 116
- CWE-22: 110

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.16"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 5058,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4805
  }
}
```