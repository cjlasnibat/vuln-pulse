# Reporte semanal de vulnerabilidades — 2026-10-20 a 2026-10-26

## Resumen

- KEV agregadas: **8** (catálogo total: 1756; ransomware conocido: 0)
- CVE nuevos publicados: **3842** (rechazados: 33; registros actualizados: 4006)
- Por severidad CVSS: {'SIN_CVSS': 312, 'HIGH': 1382, 'MEDIUM': 1584, 'CRITICAL': 334, 'LOW': 230}  — con CVSS: 91.9%
- SSVC (CISA ADP) explotación PoC/activa: 155; automatizable + impacto total: 96
- EPSS ≥ 10%: 3

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-20 | CVE-2026-106931 | EG Secure Solutions SiteGuard Server Edition | EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96656 | Plex Media Server | Plex Media Server External Control of File Name or Path Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96655 | Plex Media Server | Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-03 | Unknown |
| 2026-10-20 | CVE-2026-96654 | Plex Media Server | Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability | 2026-10-23 | Unknown |
| 2026-10-20 | CVE-2026-96652 | Plex Media Server | Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-03 | Unknown |
| 2026-10-20 | CVE-2026-110936 | Siemens Software Center | Siemens Software Center Uncontrolled Search Path Element Vulnerability | 2026-11-03 | Unknown |
| 2026-10-23 | CVE-2026-114625 | Arista VeloCloud Orchestrator | Arista VeloCloud Orchestrator SQL Injection Vulnerability | 2026-10-26 | Unknown |
| 2026-10-23 | CVE-2026-110447 | Collabora Collabora Online – Built-in CODE Server | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | 2026-10-26 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-101809 | 10 | Oracle Corporation | Workflow | CWE-284 | none |
| CVE-2026-102785 | 10 | yootheme.com | YOOtheme Pro extension for Joomla | CWE-434 | none |
| CVE-2026-105944 | 10 | Apache Software Foundation | Apache Pulsar Manager | CWE-306 | none |
| CVE-2026-110063 | 10 | Microsoft | VM Inspector for Azure Virtual Machines | CWE-59 | none |
| CVE-2026-110264 | 10 | GitLab | GitLab | CWE-190 | none |
| CVE-2026-111813 | 10 | Apache Software Foundation | Apache Traffic Server | CWE-88 | none |
| CVE-2026-111832 | 10 | WP Mailster | WP Mailster | CWE-434 | none |
| CVE-2026-113744 | 10 | Tenda | AC19 | CWE-119,CWE-121 |  |
| CVE-2026-114382 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114383 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114575 | 10 | TOTOLINK | A950RG | CWE-74,CWE-77 |  |
| CVE-2026-115905 | 10 | zip-rs | zip2 | CWE-20,CWE-436 |  |
| CVE-2026-79844 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-288 | none |
| CVE-2026-79846 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) |  | none |
| CVE-2026-79847 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-119 | none |
| CVE-2026-79848 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-89 | none |
| CVE-2026-79849 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-89 | none |
| CVE-2026-79850 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-288 | none |
| CVE-2026-79851 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-119 | none |
| CVE-2026-81212 | 10 | IBM | DataStage on Cloud Pak for Data | CWE-285 |  |
| CVE-2026-83938 | 10 | Microsoft | Azure Kubernetes Configuration Service | CWE-306 | none |
| CVE-2026-87337 | 10 | Oracle Corporation | Oracle Access Manager |  |  |
| CVE-2026-91216 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91221 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91231 | 10 | Oracle Corporation | Oracle SOA Suite |  |  |
| CVE-2026-91299 | 10 | Oracle Corporation | JD Edwards EnterpriseOne Orchestrator | CWE-284 | none |
| CVE-2026-97785 | 10 | Microsoft | Microsoft Entra application proxy | CWE-287 | none |
| CVE-2026-101446 | 9.9 | Oracle Corporation | Siebel CRM Cloud Applications |  |  |
| CVE-2026-101501 | 9.9 | Oracle Corporation | Oracle Trusted Answer Search |  |  |
| CVE-2026-101503 | 9.9 | Oracle Corporation | Oracle Trusted Answer Search |  |  |
| CVE-2026-101528 | 9.9 | Oracle Corporation | Oracle Enterprise Manager for Oracle Dat |  |  |
| CVE-2026-101529 | 9.9 | Oracle Corporation | Oracle Enterprise Manager for Oracle Dat |  |  |
| CVE-2026-105312 | 9.9 | Red Hat | StreamsHub Console for Apache Kafka® | CWE-269 | none |
| CVE-2026-111834 | 9.9 | Kitae Park | Mang Board WP | CWE-434 | none |
| CVE-2026-113672 | 9.9 | argoproj | argo-cd | CWE-22 |  |
| CVE-2026-113708 | 9.9 | argoproj | argo-cd | CWE-88 | none |
| CVE-2026-113709 | 9.9 | argoproj | argo-cd | CWE-829 | none |
| CVE-2026-114612 | 9.9 | BerriAI | litellm | CWE-269,CWE-345 |  |
| CVE-2026-115188 | 9.9 |  |  | CWE-434,CWE-94 | none |
| CVE-2026-115889 | 9.9 | bytecodealliance | wasmtime | CWE-197,CWE-843 |  |

## Top proveedores (CVE nuevos)

- Oracle Corporation: 1078
- Google: 357
- Linux: 231
- Unknown: 128
- Apache Software Foundation: 101
- n/a: 75
- Drupal: 72
- Hewlett Packard Enterprise (HPE): 71
- Eclipse Foundation: 41
- Cisco: 34

## Top CWE

- CWE-284: 354
- CWE-79: 197
- CWE-119: 193
- CWE-862: 166
- CWE-416: 146
- CWE-22: 110
- CWE-89: 92
- CWE-306: 91
- CWE-400: 90
- CWE-863: 88

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.23"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3875,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3666
  }
}
```