# Reporte semanal de vulnerabilidades — 2026-10-21 a 2026-10-27

## Resumen

- KEV agregadas: **4** (catálogo total: 1758; ransomware conocido: 0)
- CVE nuevos publicados: **2773** (rechazados: 35; registros actualizados: 5293)
- Por severidad CVSS: {'LOW': 136, 'MEDIUM': 987, 'HIGH': 713, 'SIN_CVSS': 725, 'CRITICAL': 212}  — con CVSS: 73.9%
- SSVC (CISA ADP) explotación PoC/activa: 79; automatizable + impacto total: 62
- EPSS ≥ 10%: 3

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-23 | CVE-2026-114625 | Arista VeloCloud Orchestrator | Arista VeloCloud Orchestrator SQL Injection Vulnerability | 2026-10-26 | Unknown |
| 2026-10-23 | CVE-2026-110447 | Collabora Collabora Online – Built-in CODE Server | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | 2026-10-26 | Unknown |
| 2026-10-26 | CVE-2026-109618 | PHP Group PHP | PHP Memory Corruption Vulnerability | 2026-10-29 | Unknown |
| 2026-10-26 | CVE-2026-109619 | PHP Group PHP | PHP Stale Internal Request-State Vulnerability | 2026-10-29 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-102785 | 10 | yootheme.com | YOOtheme Pro extension for Joomla | CWE-434 | none |
| CVE-2026-105944 | 10 | Apache Software Foundation | Apache Pulsar Manager | CWE-306 | none |
| CVE-2026-110063 | 10 | Microsoft | VM Inspector for Azure Virtual Machines | CWE-59 | none |
| CVE-2026-110264 | 10 | GitLab | GitLab | CWE-190 | none |
| CVE-2026-111813 | 10 | Apache Software Foundation | Apache Traffic Server | CWE-88 | none |
| CVE-2026-111832 | 10 | WP Mailster | WP Mailster | CWE-434 | none |
| CVE-2026-114382 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114383 | 10 | TOTOLINK | EX200 | CWE-119,CWE-121 |  |
| CVE-2026-114575 | 10 | TOTOLINK | A950RG | CWE-74,CWE-77 |  |
| CVE-2026-115905 | 10 | zip-rs | zip2 | CWE-20,CWE-436 |  |
| CVE-2026-116508 | 10 | TOTOLINK | A950RG | CWE-119,CWE-121 |  |
| CVE-2026-65145 | 10 | NVIDIA | NeMo Agent Toolkit | CWE-306 |  |
| CVE-2026-79844 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-288 | none |
| CVE-2026-79846 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) |  | none |
| CVE-2026-79847 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-119 | none |
| CVE-2026-79848 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-89 | none |
| CVE-2026-79849 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-89 | none |
| CVE-2026-79850 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-288 | none |
| CVE-2026-79851 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-119 | none |
| CVE-2026-83938 | 10 | Microsoft | Azure Kubernetes Configuration Service | CWE-306 | none |
| CVE-2026-97785 | 10 | Microsoft | Microsoft Entra application proxy | CWE-287 | none |
| CVE-2026-102649 | 9.9 | padok-team | burrito | CWE-306,CWE-863 |  |
| CVE-2026-110720 | 9.9 | HashiCorp | Tooling | CWE-863 | none |
| CVE-2026-111834 | 9.9 | Kitae Park | Mang Board WP | CWE-434 | none |
| CVE-2026-114612 | 9.9 | BerriAI | litellm | CWE-269,CWE-345 |  |
| CVE-2026-115188 | 9.9 |  |  | CWE-434,CWE-94 | none |
| CVE-2026-115889 | 9.9 | bytecodealliance | wasmtime | CWE-197,CWE-843 | none |
| CVE-2026-115893 | 9.9 | bytecodealliance | wasmtime | CWE-691 |  |
| CVE-2026-115931 | 9.9 | GitroomHQ | postiz-app | CWE-470,CWE-73 |  |
| CVE-2026-115933 | 9.9 | GitroomHQ | postiz-app | CWE-290,CWE-345 |  |
| CVE-2026-53942 | 9.9 | conda | infrastructure | CWE-94 | none |
| CVE-2026-71195 | 9.9 | OpenStack | Manila | CWE-863 |  |
| CVE-2026-76299 | 9.9 | Splunk | Splunk Enterprise | CWE-284 | none |
| CVE-2026-76302 | 9.9 | Splunk | Splunk Enterprise | CWE-707 | none |
| CVE-2026-76531 | 9.9 | Splunk | Splunk SOAR | CWE-552 | none |
| CVE-2026-107092 | 9.8 | n/a | n/a |  | poc |
| CVE-2026-10757 | 9.8 | Esri | ArcGIS Server | CWE-89 | none |
| CVE-2026-110956 | 9.8 | Unknown | asVereinbase | CWE-287 | none |
| CVE-2026-111183 | 9.8 | GStreamer | GStreamer | CWE-122 | none |
| CVE-2026-112241 | 9.8 | Brainstorm Force | SureCart | CWE-290 | none |

## Top proveedores (CVE nuevos)

- Apple: 325
- Linux: 231
- Mozilla: 169
- Unknown: 130
- Apache Software Foundation: 83
- n/a: 80
- Drupal: 72
- Hewlett Packard Enterprise (HPE): 71
- Cisco: 34
- Splunk: 31

## Top CWE

- CWE-79: 215
- CWE-862: 141
- CWE-89: 88
- CWE-863: 80
- CWE-22: 78
- CWE-770: 60
- CWE-125: 59
- CWE-74: 58
- CWE-400: 57
- CWE-639: 56

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.26"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2808,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2474
  }
}
```