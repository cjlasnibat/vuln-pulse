# Reporte semanal de vulnerabilidades — 2026-10-22 a 2026-10-28

## Resumen

- KEV agregadas: **6** (catálogo total: 1760; ransomware conocido: 0)
- CVE nuevos publicados: **2865** (rechazados: 208; registros actualizados: 3649)
- Por severidad CVSS: {'MEDIUM': 896, 'LOW': 120, 'HIGH': 758, 'CRITICAL': 224, 'SIN_CVSS': 867}  — con CVSS: 69.7%
- SSVC (CISA ADP) explotación PoC/activa: 50; automatizable + impacto total: 52
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-23 | CVE-2026-114625 | Arista VeloCloud Orchestrator | Arista VeloCloud Orchestrator SQL Injection Vulnerability | 2026-10-26 | Unknown |
| 2026-10-23 | CVE-2026-110447 | Collabora Collabora Online – Built-in CODE Server | Collabora Online – Built-in CODE Server OS Command Injection Vulnerability | 2026-10-26 | Unknown |
| 2026-10-26 | CVE-2026-109618 | PHP Group PHP | PHP Memory Corruption Vulnerability | 2026-10-29 | Unknown |
| 2026-10-26 | CVE-2026-109619 | PHP Group PHP | PHP Stale Internal Request-State Vulnerability | 2026-10-29 | Unknown |
| 2026-10-27 | CVE-2026-48356 | Adobe Commerce and Magento | Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability | 2026-11-10 | Unknown |
| 2026-10-27 | CVE-2026-111497 | Google Brotli | Google Brotli Unchecked Return Value Vulnerability | 2026-11-10 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-102785 | 10 | yootheme.com | YOOtheme Pro extension for Joomla | CWE-434 | none |
| CVE-2026-105781 | 10 | Adobe | Adobe Campaign Classic | CWE-89 |  |
| CVE-2026-110063 | 10 | Microsoft | VM Inspector for Azure Virtual Machines | CWE-59 | none |
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
| CVE-2026-104351 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-104353 | 9.9 | Adobe | Adobe Campaign Classic | CWE-78 |  |
| CVE-2026-105489 | 9.9 | Adobe | Adobe Campaign Classic | CWE-89 | none |
| CVE-2026-105780 | 9.9 | Adobe | Adobe Campaign Classic | CWE-863 |  |
| CVE-2026-110720 | 9.9 | HashiCorp | Tooling | CWE-863 | none |
| CVE-2026-114612 | 9.9 | BerriAI | litellm | CWE-269,CWE-345 |  |
| CVE-2026-115188 | 9.9 |  |  | CWE-434,CWE-94 | none |
| CVE-2026-115889 | 9.9 | bytecodealliance | wasmtime | CWE-197,CWE-843 | none |
| CVE-2026-115893 | 9.9 | bytecodealliance | wasmtime | CWE-691 |  |
| CVE-2026-115931 | 9.9 | GitroomHQ | postiz-app | CWE-470,CWE-73 |  |
| CVE-2026-115933 | 9.9 | GitroomHQ | postiz-app | CWE-290,CWE-345 |  |
| CVE-2026-44179 | 9.9 | xwikisas | xwiki-pro-macros | CWE-95 |  |
| CVE-2026-53942 | 9.9 | conda | infrastructure | CWE-94 | none |
| CVE-2026-103406 | 9.8 | Juniper Networks | Session Smart Conductor | CWE-78 |  |
| CVE-2026-103409 | 9.8 | Juniper Networks | Session Smart Router | CWE-306 |  |
| CVE-2026-103780 | 9.8 | Dell | PowerProtect Data Domain | CWE-121 |  |
| CVE-2026-106013 | 9.8 | artbees | Jupiter X Core | CWE-287 |  |
| CVE-2026-107092 | 9.8 | n/a | n/a |  | poc |
| CVE-2026-10757 | 9.8 | Esri | ArcGIS Server | CWE-89 | none |
| CVE-2026-109218 | 9.8 | kleor | Contact Manager | CWE-434 |  |
| CVE-2026-110879 | 9.8 | FasterXML | jackson-databind | CWE-502 |  |
| CVE-2026-110956 | 9.8 | Unknown | asVereinbase | CWE-287 | none |
| CVE-2026-112241 | 9.8 | Brainstorm Force | SureCart | CWE-290 | none |
| CVE-2026-112832 | 9.8 | CozyThemes | Rootblox | CWE-98 | none |

## Top proveedores (CVE nuevos)

- Linux: 346
- Apple: 325
- Mozilla: 176
- Unknown: 119
- Hewlett Packard Enterprise (HPE): 71
- n/a: 67
- Google: 55
- Dell: 48
- Tanium: 31
- SemanticMediaWiki: 22

## Top CWE

- CWE-79: 223
- CWE-862: 125
- CWE-89: 84
- CWE-22: 82
- CWE-78: 60
- CWE-787: 56
- CWE-770: 56
- CWE-863: 53
- CWE-125: 51
- CWE-639: 51

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.27"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3073,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2621
  }
}
```