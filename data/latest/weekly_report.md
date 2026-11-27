# Reporte semanal de vulnerabilidades — 2026-11-21 a 2026-11-27

## Resumen

- KEV agregadas: **15** (catálogo total: 1805; ransomware conocido: 0)
- CVE nuevos publicados: **3279** (rechazados: 30; registros actualizados: 6329)
- Por severidad CVSS: {'MEDIUM': 1592, 'HIGH': 1114, 'LOW': 141, 'CRITICAL': 249, 'SIN_CVSS': 183}  — con CVSS: 94.4%
- SSVC (CISA ADP) explotación PoC/activa: 308; automatizable + impacto total: 68
- EPSS ≥ 10%: 1

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-23 | CVE-2026-133968 | Project MONAI MONAI Label | Project MONAI MONAI Label Path Traversal Vulnerability | 2026-11-26 | Unknown |
| 2026-11-23 | CVE-2026-134624 | N-able MailAssure | N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-26 | Unknown |
| 2026-11-24 | CVE-2026-132224 | Optimizely Web Experimentation | Optimizely Web Experimentation External Control of Critical State Data Vulnerability | 2026-11-27 | Unknown |
| 2026-11-24 | CVE-2026-131914 | Idunno AntiCsrf | Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability | 2026-11-27 | Unknown |
| 2026-11-24 | CVE-2026-132165 | Drupal Core | Drupal Core Remote Code Execution Vulnerability | 2026-11-27 | Unknown |
| 2026-11-25 | CVE-2026-103406 | Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router | Hewlett Packard Enterprise (HPE) Juniper Session Smart Conductor and Session Smart Router OS Command Injection Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2026-133469 | Vates Xen Orchestra | Vates Xen Orchestra Improper Validation of Specified Type of Input Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2025-41450 | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Improper Authentication Vulnerability | 2026-12-09 | Unknown |
| 2026-11-25 | CVE-2023-25914 | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Path Traversal Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2023-25915 | Danfoss AK-SM 800A Series | Danfoss AK-SM 800A Series Improper Input Validation Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2026-133324 | Mitel MiCollab | Mitel MiCollab Not Failing Securely Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2026-133275 | Mitel MiCollab | Mitel MiCollab Unrestricted Upload of File with Dangerous Type Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2026-133311 | Mitel MiCollab | Mitel MiCollab Weak Authentication Vulnerability | 2026-12-09 | Unknown |
| 2026-11-25 | CVE-2026-133303 | Mitel MiCollab | Mitel MiCollab XML Injection Vulnerability | 2026-11-28 | Unknown |
| 2026-11-25 | CVE-2026-133323 | Mitel MiCollab | Mitel MiCollab OS Command Injection Vulnerability | 2026-11-28 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109484 | 10 | Microsoft | Azure App Service for Linux | CWE-75 | none |
| CVE-2026-126984 | 10 | Pulp | pulp_python | CWE-918 |  |
| CVE-2026-128791 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 | none |
| CVE-2026-128797 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-668 | none |
| CVE-2026-128798 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 | none |
| CVE-2026-129514 | 10 | hexpm | hexpm | CWE-502 |  |
| CVE-2026-130169 | 10 | Significant-Gravitas | AutoGPT | CWE-287,CWE-330 | poc |
| CVE-2026-133993 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | poc |
| CVE-2026-134882 | 10 | TOTOLINK | A7100RU | CWE-77,CWE-78 |  |
| CVE-2026-135792 | 10 | Panabit | Smart Application Gateway | CWE-77,CWE-78 |  |
| CVE-2026-135797 | 10 | Volans | NGFW Next-Generation Firewall | CWE-77,CWE-78 |  |
| CVE-2026-136136 | 10 | Netis | WF2409E | CWE-287 |  |
| CVE-2026-136547 | 10 | Tenda | RX3 | CWE-287 | poc |
| CVE-2026-136548 | 10 | Tenda | RX3 | CWE-119,CWE-121 | poc |
| CVE-2026-136549 | 10 | Tenda | RX3 | CWE-74,CWE-77 |  |
| CVE-2026-136553 | 10 | Tenda | RX3 | CWE-287 | poc |
| CVE-2026-136823 | 10 | D-Link | R32 | CWE-77,CWE-78 |  |
| CVE-2026-137043 | 10 | TOTOLINK | N350RT | CWE-285,CWE-639 | poc |
| CVE-2026-137721 | 10 | Mitel | OpenScape 4000 | CWE-78 | none |
| CVE-2026-137724 | 10 | Mitel | OpenScape 4000 | CWE-306 |  |
| CVE-2026-59415 | 10 | Spring | Spring AI | CWE-74 | none |
| CVE-2026-62841 | 10 | Microsoft | Azure Event Grid System | CWE-287 | none |
| CVE-2026-78114 | 10 | Apache Software Foundation | Apache JSPWiki | CWE-384 |  |
| CVE-2026-86155 | 10 | Apache Software Foundation | Apache Jena Fuseki | CWE-918 |  |
| CVE-2026-9790 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 | none |
| CVE-2026-103782 | 9.9 | Dell | Enterprise Sonic Distributio | CWE-88 | none |
| CVE-2026-123266 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-123342 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-123722 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-123723 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-123986 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-123987 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-125675 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-125676 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-132877 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-134963 | 9.9 | Webdeclic | WPMasterToolKit | CWE-94 | none |
| CVE-2026-136835 | 9.9 | Jenkins Project | Jenkins Script Security Plugin | CWE-94 | none |
| CVE-2026-137498 | 9.9 | budibase | server | CWE-943 |  |
| CVE-2026-18530 | 9.9 | Lantronix | S2220 Series 2 | CWE-78 | none |
| CVE-2026-50691 | 9.9 | Microsoft | Microsoft 365 Copilot | CWE-285 | none |

## Top proveedores (CVE nuevos)

- Dell: 123
- Mozilla: 120
- Adobe: 113
- Wikimedia Foundation: 75
- frappe: 70
- Apache Software Foundation: 66
- Unknown: 61
- Joomla! Project: 58
- Google: 54
- FFmpeg: 51

## Top CWE

- CWE-79: 585
- CWE-862: 254
- CWE-863: 148
- CWE-89: 102
- CWE-22: 99
- CWE-416: 95
- CWE-639: 89
- CWE-918: 77
- CWE-78: 73
- CWE-770: 69

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.25"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 3309,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3098
  }
}
```