# Reporte semanal de vulnerabilidades — 2026-10-15 a 2026-10-21

## Resumen

- KEV agregadas: **9** (catálogo total: 1754; ransomware conocido: 0)
- CVE nuevos publicados: **4301** (rechazados: 130; registros actualizados: 8167)
- Por severidad CVSS: {'SIN_CVSS': 620, 'LOW': 179, 'MEDIUM': 1741, 'CRITICAL': 310, 'HIGH': 1451}  — con CVSS: 85.6%
- SSVC (CISA ADP) explotación PoC/activa: 456; automatizable + impacto total: 119
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-15 | CVE-2026-21589 | Atlassian Multiple Products | Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability | 2026-10-18 | Unknown |
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
| CVE-2026-110957 | 10 | Wavlink | WL-WN530BE2-A | CWE-77,CWE-78 | poc |
| CVE-2026-110958 | 10 | Wavlink | WN530HG4B | CWE-119,CWE-122 | poc |
| CVE-2026-111057 | 10 | mljar | mercury | CWE-185,CWE-284 |  |
| CVE-2026-111832 | 10 | WP Mailster | WP Mailster | CWE-434 |  |
| CVE-2026-113744 | 10 | Tenda | AC19 | CWE-119,CWE-121 |  |
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
| CVE-2026-105037 | 9.9 | EnergizeLab | station-middleware | CWE-73 | none |
| CVE-2026-105312 | 9.9 | Red Hat | StreamsHub Console for Apache Kafka® | CWE-269 | none |
| CVE-2026-110887 | 9.9 | HivePress | HivePress | CWE-94 | none |
| CVE-2026-111406 | 9.9 | PT Norther Lights Production | MapSVG | CWE-434 | none |
| CVE-2026-111834 | 9.9 | Kitae Park | Mang Board WP | CWE-434 |  |
| CVE-2026-113672 | 9.9 | argoproj | argo-cd | CWE-22 |  |
| CVE-2026-113708 | 9.9 | argoproj | argo-cd | CWE-88 | none |
| CVE-2026-113709 | 9.9 | argoproj | argo-cd | CWE-829 |  |
| CVE-2026-57155 | 9.9 | opnsense | core | CWE-22,CWE-73 | poc |
| CVE-2026-71195 | 9.9 | OpenStack | Manila | CWE-863 |  |
| CVE-2026-85746 | 9.9 | MariaDB | server | CWE-787 | none |
| CVE-2026-85748 | 9.9 | MariaDB | server | CWE-416 | none |
| CVE-2026-91222 | 9.9 | Oracle Corporation | Oracle Business Process Management Suite |  |  |
| CVE-2026-91224 | 9.9 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91232 | 9.9 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91250 | 9.9 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91251 | 9.9 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91354 | 9.9 | Oracle Corporation | Oracle Outside In Technology |  |  |
| CVE-2026-91637 | 9.9 | Oracle Corporation | Oracle Essbase |  |  |
| CVE-2026-91638 | 9.9 | Oracle Corporation | Oracle Essbase |  |  |

## Top proveedores (CVE nuevos)

- Oracle Corporation: 1076
- Linux: 439
- Google: 366
- Apache Software Foundation: 137
- Unknown: 127
- n/a: 65
- IBM: 58
- Eclipse Foundation: 57
- Apple: 46
- Red Hat: 41

## Top CWE

- CWE-79: 216
- CWE-862: 207
- CWE-119: 179
- CWE-416: 153
- CWE-639: 143
- CWE-125: 139
- CWE-22: 100
- CWE-89: 93
- CWE-306: 93
- CWE-200: 86

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.20"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4431,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2243
  }
}
```