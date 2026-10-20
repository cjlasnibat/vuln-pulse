# Reporte semanal de vulnerabilidades — 2026-10-14 a 2026-10-20

## Resumen

- KEV agregadas: **7** (catálogo total: 1748; ransomware conocido: 0)
- CVE nuevos publicados: **3147** (rechazados: 121; registros actualizados: 10436)
- Por severidad CVSS: {'MEDIUM': 1242, 'HIGH': 1006, 'LOW': 90, 'SIN_CVSS': 585, 'CRITICAL': 224}  — con CVSS: 81.4%
- SSVC (CISA ADP) explotación PoC/activa: 517; automatizable + impacto total: 114
- EPSS ≥ 10%: 2

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
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
| CVE-2026-107594 | 10 | Unknown | File Upload to Order | CWE-73 | none |
| CVE-2026-110536 | 10 | D-Link | DIR-868L | CWE-77,CWE-78 | poc |
| CVE-2026-110957 | 10 | Wavlink | WL-WN530BE2-A | CWE-77,CWE-78 | poc |
| CVE-2026-110958 | 10 | Wavlink | WN530HG4B | CWE-119,CWE-122 | poc |
| CVE-2026-111057 | 10 | mljar | mercury | CWE-185,CWE-284 |  |
| CVE-2026-55572 | 10 | e107inc | e107 | CWE-89 |  |
| CVE-2026-78162 | 10 | Apache Software Foundation | Apache Camel | CWE-502 | poc |
| CVE-2026-94169 | 10 | Theme-one | The Grid | CWE-94 | none |
| CVE-2026-95182 | 10 | n/a | n/a | CWE-426 | poc |
| CVE-2026-105037 | 9.9 | EnergizeLab | station-middleware | CWE-73 | none |
| CVE-2026-105312 | 9.9 | Red Hat | StreamsHub Console for Apache Kafka® | CWE-269 |  |
| CVE-2026-108390 | 9.9 | hestiacp | hestiacp | CWE-427,CWE-88 | poc |
| CVE-2026-110887 | 9.9 | HivePress | HivePress | CWE-94 | none |
| CVE-2026-111406 | 9.9 | PT Norther Lights Production | MapSVG | CWE-434 | none |
| CVE-2026-57155 | 9.9 | opnsense | core | CWE-22,CWE-73 | poc |
| CVE-2026-77524 | 9.9 | kedacore | keda | CWE-269,CWE-918 | poc |
| CVE-2026-85746 | 9.9 | MariaDB | server | CWE-787 | none |
| CVE-2026-85748 | 9.9 | MariaDB | server | CWE-416 | none |
| CVE-2026-92262 | 9.9 | MariaDB | server | CWE-706 |  |
| CVE-2026-101306 | 9.8 | FreeBSD | FreeBSD | CWE-273,CWE-281 | none |
| CVE-2026-103768 | 9.8 | elextensions | ELEX WordPress HelpDesk & Customer Ticke | CWE-434 | none |
| CVE-2026-104586 | 9.8 | n/a | n/a | CWE-94 | poc |
| CVE-2026-104730 | 9.8 | sunshinephotocart | Sunshine Photo Cart – Client Photo Galle | CWE-502 | none |
| CVE-2026-104736 | 9.8 | thimpress | LearnPress – WordPress LMS Plugin for Cr | CWE-502 | none |
| CVE-2026-104748 | 9.8 | wpazleen | SimpleForm – Form Maker to Chat Apps wit | CWE-269 | none |
| CVE-2026-104798 | 9.8 | joedolson | My Calendar – Accessible Event Manager | CWE-269 | none |
| CVE-2026-104800 | 9.8 | streetforce1 | AGE-GATE | CWE-434 | none |
| CVE-2026-105038 | 9.8 | EnergizeLab | FastAPI AI inference server | CWE-306 | none |
| CVE-2026-107083 | 9.8 | n/a | n/a | CWE-89 | poc |
| CVE-2026-107424 | 9.8 | M A Vinoth Kumar | Frontend Dashboard | CWE-266 | none |
| CVE-2026-108065 | 9.8 | Channel Software | WebAlliance eCommerce | CWE-89 | none |
| CVE-2026-108291 | 9.8 | itthinx | Affiliates | CWE-502 | none |
| CVE-2026-108587 | 9.8 | 10web | 10Web Booster – Website speed optimizati | CWE-434 | none |
| CVE-2026-108983 | 9.8 | GeoVision Inc. | GV-ASManager | CWE-78 | none |
| CVE-2026-109145 | 9.8 | Unknown | User Rights Access Manager | CWE-269 | none |
| CVE-2026-109219 | 9.8 | kitae-park | Mang Board | CWE-434 | none |
| CVE-2026-109515 | 9.8 | properfraction | MailOptin – Popup, Optin Forms & Email N | CWE-269 | none |
| CVE-2026-109686 | 9.8 | Link Whisper INC | Link Whisper Free | CWE-502 | none |
| CVE-2026-109694 | 9.8 | WP ManageNinja LLC | Fluent CRM | CWE-266 | none |
| CVE-2026-109892 | 9.8 | Shabti Kaplan | Frontend Admin by DynamiApps | CWE-266 | none |

## Top proveedores (CVE nuevos)

- Linux: 483
- Juniper Networks: 153
- Unknown: 121
- Apache Software Foundation: 92
- Red Hat: 66
- n/a: 53
- Eclipse Foundation: 49
- Gitea: 48
- IBM: 47
- Apple: 46

## Top CWE

- CWE-79: 224
- CWE-862: 200
- CWE-639: 142
- CWE-125: 124
- CWE-89: 105
- CWE-863: 82
- CWE-78: 80
- CWE-22: 78
- CWE-200: 76
- CWE-787: 75

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
    "fetched": 3268,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3054
  }
}
```