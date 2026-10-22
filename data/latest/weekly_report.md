# Reporte semanal de vulnerabilidades — 2026-10-16 a 2026-10-22

## Resumen

- KEV agregadas: **8** (catálogo total: 1754; ransomware conocido: 0)
- CVE nuevos publicados: **4251** (rechazados: 121; registros actualizados: 7451)
- Por severidad CVSS: {'MEDIUM': 1729, 'HIGH': 1374, 'SIN_CVSS': 651, 'CRITICAL': 304, 'LOW': 193}  — con CVSS: 84.7%
- SSVC (CISA ADP) explotación PoC/activa: 394; automatizable + impacto total: 107
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-16 | CVE-2026-102764 | BeyondTrust Remote Support | BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability | 2026-10-19 | Unknown |
| 2026-10-16 | CVE-2025-61624 | Fortinet Multiple Products | Fortinet Multiple Products Path Traversal Vulnerability | 2026-10-19 | Unknown |
| 2026-10-20 | CVE-2026-106931 | EG Secure Solutions SiteGuard Server Edition | EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96656 | Plex Media Server | Plex Media Server External Control of File Name or Path Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96655 | Plex Media Server | Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-03 | Unknown |
| 2026-10-20 | CVE-2026-96654 | Plex Media Server | Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96652 | Plex Media Server | Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-03 | Unknown |
| 2026-10-20 | CVE-2026-110936 | Siemens Software Center | Siemens Software Center Uncontrolled Search Path Element Vulnerability | 2026-11-03 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-101809 | 10 | Oracle Corporation | Workflow |  |  |
| CVE-2026-102785 | 10 | yootheme.com | YOOtheme Pro extension for Joomla | CWE-434 | none |
| CVE-2026-105944 | 10 | Apache Software Foundation | Apache Pulsar Manager | CWE-306 |  |
| CVE-2026-110264 | 10 | GitLab | GitLab | CWE-190 | none |
| CVE-2026-111057 | 10 | mljar | mercury | CWE-185,CWE-284 |  |
| CVE-2026-111813 | 10 | Apache Software Foundation | Apache Traffic Server | CWE-88 |  |
| CVE-2026-111832 | 10 | WP Mailster | WP Mailster | CWE-434 | none |
| CVE-2026-113744 | 10 | Tenda | AC19 | CWE-119,CWE-121 |  |
| CVE-2026-114382 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114383 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114575 | 10 | TOTOLINK | A950RG | CWE-74,CWE-77 |  |
| CVE-2026-78162 | 10 | Apache Software Foundation | Apache Camel | CWE-502 | poc |
| CVE-2026-81212 | 10 | IBM | DataStage on Cloud Pak for Data | CWE-285 |  |
| CVE-2026-87337 | 10 | Oracle Corporation | Oracle Access Manager |  |  |
| CVE-2026-91216 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91221 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91231 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91299 | 10 | Oracle Corporation | JD Edwards EnterpriseOne Orchestrator |  |  |
| CVE-2026-94169 | 10 | Theme-one | The Grid | CWE-94 | none |
| CVE-2026-95182 | 10 | n/a | n/a | CWE-426 | poc |
| CVE-2026-101446 | 9.9 | Oracle Corporation | Siebel CRM Cloud Applications |  |  |
| CVE-2026-101501 | 9.9 | Oracle Corporation | Oracle Trusted Answer Search |  |  |
| CVE-2026-101503 | 9.9 | Oracle Corporation | Oracle Trusted Answer Search |  |  |
| CVE-2026-101528 | 9.9 | Oracle Corporation | Oracle Enterprise Manager for Oracle Dat |  |  |
| CVE-2026-101529 | 9.9 | Oracle Corporation | Oracle Enterprise Manager for Oracle Dat |  |  |
| CVE-2026-105312 | 9.9 | Red Hat | StreamsHub Console for Apache Kafka® | CWE-269 | none |
| CVE-2026-110887 | 9.9 | HivePress | HivePress | CWE-94 | none |
| CVE-2026-111406 | 9.9 | PT Norther Lights Production | MapSVG | CWE-434 | none |
| CVE-2026-111834 | 9.9 | Kitae Park | Mang Board WP | CWE-434 | none |
| CVE-2026-113672 | 9.9 | argoproj | argo-cd | CWE-22 |  |
| CVE-2026-113708 | 9.9 | argoproj | argo-cd | CWE-88 | none |
| CVE-2026-113709 | 9.9 | argoproj | argo-cd | CWE-829 | none |
| CVE-2026-71195 | 9.9 | OpenStack | Manila | CWE-863 |  |
| CVE-2026-76299 | 9.9 | Splunk | Splunk Enterprise | CWE-284 | none |
| CVE-2026-76302 | 9.9 | Splunk | Splunk Enterprise | CWE-707 | none |
| CVE-2026-76531 | 9.9 | Splunk | Splunk SOAR | CWE-552 | none |
| CVE-2026-85746 | 9.9 | MariaDB | server | CWE-787 | none |
| CVE-2026-85748 | 9.9 | MariaDB | server | CWE-416 | none |
| CVE-2026-91222 | 9.9 | Oracle Corporation | Oracle Business Process Management Suite |  |  |
| CVE-2026-91224 | 9.9 | Oracle Corporation | Oracle SOA Suite |  |  |

## Top proveedores (CVE nuevos)

- Oracle Corporation: 1077
- Linux: 437
- Google: 358
- Apache Software Foundation: 165
- Unknown: 131
- Drupal: 72
- n/a: 58
- IBM: 58
- Apple: 46
- Red Hat: 43

## Top CWE

- CWE-862: 222
- CWE-79: 213
- CWE-119: 177
- CWE-416: 149
- CWE-284: 145
- CWE-639: 126
- CWE-89: 114
- CWE-22: 106
- CWE-306: 97
- CWE-200: 94

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.21"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4372,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4184
  }
}
```