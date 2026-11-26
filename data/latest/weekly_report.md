# Reporte semanal de vulnerabilidades — 2026-11-20 a 2026-11-26

## Resumen

- KEV agregadas: **19** (catálogo total: 1805; ransomware conocido: 0)
- CVE nuevos publicados: **3654** (rechazados: 28; registros actualizados: 6653)
- Por severidad CVSS: {'MEDIUM': 1702, 'SIN_CVSS': 359, 'HIGH': 1191, 'LOW': 136, 'CRITICAL': 266}  — con CVSS: 90.2%
- SSVC (CISA ADP) explotación PoC/activa: 366; automatizable + impacto total: 75
- EPSS ≥ 10%: 3

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-20 | CVE-2026-129448 | Apache Roller | Apache Roller Deserialization of Untrusted Data Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-123890 | Broadcom VMware vCenter | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2025-42884 | SAP NetWeaver | SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-76466 | Cisco Expressway Series | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | 2026-11-23 | Unknown |
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
| CVE-2026-128797 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-668 |  |
| CVE-2026-128798 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 |  |
| CVE-2026-129514 | 10 | hexpm | hexpm | CWE-502 |  |
| CVE-2026-130169 | 10 | Significant-Gravitas | AutoGPT | CWE-287,CWE-330 | poc |
| CVE-2026-133493 | 10 | D-Link | DIR-600L | CWE-77,CWE-78 | poc |
| CVE-2026-133993 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | poc |
| CVE-2026-134882 | 10 | TOTOLINK | A7100RU | CWE-77,CWE-78 |  |
| CVE-2026-135792 | 10 | Panabit | Smart Application Gateway | CWE-77,CWE-78 |  |
| CVE-2026-135797 | 10 | Volans | NGFW Next-Generation Firewall | CWE-77,CWE-78 |  |
| CVE-2026-136136 | 10 | Netis | WF2409E | CWE-287 |  |
| CVE-2026-136547 | 10 | Tenda | RX3 | CWE-287 | poc |
| CVE-2026-136548 | 10 | Tenda | RX3 | CWE-119,CWE-121 |  |
| CVE-2026-136549 | 10 | Tenda | RX3 | CWE-74,CWE-77 |  |
| CVE-2026-136553 | 10 | Tenda | RX3 | CWE-287 |  |
| CVE-2026-136823 | 10 | D-Link | R32 | CWE-77,CWE-78 |  |
| CVE-2026-137043 | 10 | TOTOLINK | N350RT | CWE-285,CWE-639 |  |
| CVE-2026-14914 | 10 | Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. | Tegsoft Contact Center | CWE-434 | none |
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
| CVE-2026-127057 | 9.9 | Danfoss | AK-SC 355 | CWE-1392 | none |
| CVE-2026-132877 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-133648 | 9.9 | flowintel | flowintel | CWE-295 | none |
| CVE-2026-136835 | 9.9 | Jenkins Project | Jenkins Script Security Plugin | CWE-94 | none |
| CVE-2026-137498 | 9.9 | budibase | server | CWE-943 |  |
| CVE-2026-18530 | 9.9 | Lantronix | S2220 Series 2 | CWE-78 | none |

## Top proveedores (CVE nuevos)

- Linux: 246
- Mozilla: 120
- Adobe: 112
- Wikimedia Foundation: 75
- frappe: 70
- Apache Software Foundation: 65
- Dell: 62
- Unknown: 62
- Joomla! Project: 58
- Google: 54

## Top CWE

- CWE-79: 603
- CWE-862: 323
- CWE-863: 141
- CWE-89: 103
- CWE-22: 102
- CWE-639: 96
- CWE-125: 92
- CWE-416: 86
- CWE-78: 73
- CWE-770: 73

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
    "fetched": 3682,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3313
  }
}
```