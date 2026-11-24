# Reporte semanal de vulnerabilidades — 2026-11-18 a 2026-11-24

## Resumen

- KEV agregadas: **13** (catálogo total: 1795; ransomware conocido: 1)
- CVE nuevos publicados: **4166** (rechazados: 29; registros actualizados: 7569)
- Por severidad CVSS: {'HIGH': 1392, 'MEDIUM': 1756, 'CRITICAL': 366, 'LOW': 157, 'SIN_CVSS': 495}  — con CVSS: 88.1%
- SSVC (CISA ADP) explotación PoC/activa: 470; automatizable + impacto total: 136
- EPSS ≥ 10%: 12

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-18 | CVE-2024-10441 | Synology DiskStation Manager (DSM) | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | 2026-11-21 | Known |
| 2026-11-18 | CVE-2026-40217 | BerriAI LiteLLM | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | 2026-12-02 | Unknown |
| 2026-11-18 | CVE-2026-90817 | Vanderbilt University Research Electronic Data Capture (REDCap) | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | 2026-11-21 | Unknown |
| 2026-11-18 | CVE-2026-90436 | Apache Axis | Apache Axis Unsafe Reflection Vulnerability | 2026-11-21 | Unknown |
| 2026-11-20 | CVE-2026-129448 | Apache Roller | Apache Roller Deserialization of Untrusted Data Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-123890 | Broadcom VMware vCenter | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2025-42884 | SAP NetWeaver | SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-76466 | Cisco Expressway Series | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | 2026-11-23 | Unknown |
| 2026-11-23 | CVE-2026-133968 | Project MONAI MONAI Label | Project MONAI MONAI Label Path Traversal Vulnerability | 2026-11-26 | Unknown |
| 2026-11-23 | CVE-2026-134624 | N-able MailAssure | N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability | 2026-11-26 | Unknown |
| 2026-11-24 | CVE-2026-132224 | Optimizely Web Experimentation | Optimizely Web Experimentation External Control of Critical State Data Vulnerability | 2026-11-27 | Unknown |
| 2026-11-24 | CVE-2026-131914 | Idunno AntiCsrf | Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability | 2026-11-27 | Unknown |
| 2026-11-24 | CVE-2026-132165 | Drupal Core | Drupal Core Remote Code Execution Vulnerability | 2026-11-27 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-109484 | 10 | Microsoft | Azure App Service for Linux | CWE-75 | none |
| CVE-2026-128791 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 | none |
| CVE-2026-128797 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-668 |  |
| CVE-2026-128798 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 |  |
| CVE-2026-129514 | 10 | hexpm | hexpm | CWE-502 |  |
| CVE-2026-130169 | 10 | Significant-Gravitas | AutoGPT | CWE-287,CWE-330 | poc |
| CVE-2026-130778 | 10 | lxc | incus | CWE-287 | none |
| CVE-2026-133323 | 10 | Mitel | MiCollab | CWE-78 | none |
| CVE-2026-133493 | 10 | D-Link | DIR-600L | CWE-77,CWE-78 | poc |
| CVE-2026-133993 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 |  |
| CVE-2026-134882 | 10 | TOTOLINK | A7100RU | CWE-77,CWE-78 |  |
| CVE-2026-135792 | 10 | Panabit | Smart Application Gateway | CWE-77,CWE-78 |  |
| CVE-2026-135797 | 10 | Volans | NGFW Next-Generation Firewall | CWE-77,CWE-78 |  |
| CVE-2026-14914 | 10 | Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. | Tegsoft Contact Center | CWE-434 | none |
| CVE-2026-59415 | 10 | Spring | Spring AI |  |  |
| CVE-2026-62841 | 10 | Microsoft | Azure Event Grid System | CWE-287 | none |
| CVE-2026-71499 | 10 | hefy2027 | cf-manager | CWE-918,CWE-94 | none |
| CVE-2026-75521 | 10 | mirendev | runtime | CWE-295 | none |
| CVE-2026-77312 | 10 | flytohub | flyto-core | CWE-22 | poc |
| CVE-2026-86155 | 10 | Apache Software Foundation | Apache Jena Fuseki | CWE-918 |  |
| CVE-2026-95787 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-269 | none |
| CVE-2026-9790 | 10 | Acer | Connect M6E 5G Portable WiFi Router | CWE-306 | none |
| CVE-2026-103782 | 9.9 | Dell | Enterprise Sonic Distributio | CWE-88 | none |
| CVE-2026-123266 | 9.9 | Adobe | Adobe Experience Manager as a Cloud Serv | CWE-94 | none |
| CVE-2026-123342 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-123722 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-123723 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-123986 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-123987 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 |  |
| CVE-2026-125675 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-125676 | 9.9 | Adobe | Adobe Campaign Classic | CWE-94 | none |
| CVE-2026-127057 | 9.9 | Danfoss | AK-SC 355 | CWE-1392 | none |
| CVE-2026-129048 | 9.9 | Jacob N. Breetvelt | WP Photo Album Plus | CWE-94 | none |
| CVE-2026-129316 | 9.9 | Dokploy | dokploy | CWE-862 | poc |
| CVE-2026-129986 | 9.9 | Dokploy | dokploy | CWE-77,CWE-78 | poc |
| CVE-2026-129987 | 9.9 | Dokploy | dokploy | CWE-77 | none |
| CVE-2026-129989 | 9.9 | Dokploy | dokploy | CWE-78 | poc |
| CVE-2026-129991 | 9.9 | Dokploy | dokploy | CWE-78 | none |
| CVE-2026-131253 | 9.9 | Splunk | Splunk SOAR | CWE-94 | none |
| CVE-2026-132231 | 9.9 | JetBrains | TeamCity | CWE-1289 | none |

## Top proveedores (CVE nuevos)

- Linux: 493
- JetBrains: 233
- Splunk: 146
- Mozilla: 120
- Adobe: 112
- Unknown: 74
- frappe: 67
- gpac: 64
- Apache Software Foundation: 59
- Joomla! Project: 58

## Top CWE

- CWE-79: 570
- CWE-862: 324
- CWE-863: 158
- CWE-639: 140
- CWE-22: 134
- CWE-89: 106
- CWE-125: 103
- CWE-416: 97
- CWE-78: 84
- CWE-918: 83

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.24"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4195,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3562
  }
}
```