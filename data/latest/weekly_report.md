# Reporte semanal de vulnerabilidades — 2026-11-17 a 2026-11-23

## Resumen

- KEV agregadas: **9** (catálogo total: 1790; ransomware conocido: 0)
- CVE nuevos publicados: **4610** (rechazados: 27; registros actualizados: 7016)
- Por severidad CVSS: {'CRITICAL': 373, 'HIGH': 1596, 'SIN_CVSS': 485, 'MEDIUM': 1931, 'LOW': 225}  — con CVSS: 89.5%
- SSVC (CISA ADP) explotación PoC/activa: 443; automatizable + impacto total: 176
- EPSS ≥ 10%: 12

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-17 | CVE-2026-115731 | Perforce Puppet Enterprise | Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability | 2026-12-01 | Unknown |
| 2026-11-18 | CVE-2024-10441 | Synology DiskStation Manager (DSM) | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | 2026-11-21 | Unknown |
| 2026-11-18 | CVE-2026-40217 | BerriAI LiteLLM | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | 2026-12-02 | Unknown |
| 2026-11-18 | CVE-2026-90817 | Vanderbilt University Research Electronic Data Capture (REDCap) | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | 2026-11-21 | Unknown |
| 2026-11-18 | CVE-2026-90436 | Apache Axis | Apache Axis Unsafe Reflection Vulnerability | 2026-11-21 | Unknown |
| 2026-11-20 | CVE-2026-129448 | Apache Roller | Apache Roller Deserialization of Untrusted Data Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-123890 | Broadcom VMware vCenter | VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2025-42884 | SAP NetWeaver | SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability | 2026-11-23 | Unknown |
| 2026-11-20 | CVE-2026-76466 | Cisco Expressway Series | Cisco Expressway Series Use of Hard-coded Credentials Vulnerability | 2026-11-23 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-100397 | 10 | rucio | rucio | CWE-287 | poc |
| CVE-2026-114202 | 10 | ASUS | Control Center Express | CWE-321 | none |
| CVE-2026-114784 | 10 | Oracle Corporation | Oracle Business Intelligence Enterprise  | CWE-306 | none |
| CVE-2026-114824 | 10 | Oracle Corporation | Oracle Platform Security for Java | CWE-502 | none |
| CVE-2026-114835 | 10 | Oracle Corporation | Oracle Access Manager | CWE-306 | none |
| CVE-2026-120387 | 10 | Circutor | PowerStudio SCADA Wave | CWE-347 | poc |
| CVE-2026-130778 | 10 | lxc | incus | CWE-287 | none |
| CVE-2026-133323 | 10 | Mitel | MiCollab | CWE-78 | none |
| CVE-2026-133493 | 10 | D-Link | DIR-600L | CWE-77,CWE-78 | poc |
| CVE-2026-133993 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 |  |
| CVE-2026-134882 | 10 | TOTOLINK | A7100RU | CWE-77,CWE-78 |  |
| CVE-2026-14914 | 10 | Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. | Tegsoft Contact Center | CWE-434 | none |
| CVE-2026-62841 | 10 | Microsoft | Azure Event Grid System | CWE-287 |  |
| CVE-2026-71499 | 10 | hefy2027 | cf-manager | CWE-918,CWE-94 | none |
| CVE-2026-75521 | 10 | mirendev | runtime | CWE-295 | none |
| CVE-2026-77312 | 10 | flytohub | flyto-core | CWE-22 |  |
| CVE-2026-91500 | 10 | Oracle Corporation | Oracle Access Manager | CWE-284 | none |
| CVE-2026-91510 | 10 | Oracle Corporation | Oracle Access Manager | CWE-306 | none |
| CVE-2026-91569 | 10 | Oracle Corporation | Oracle WebLogic Server | CWE-306 | none |
| CVE-2026-95787 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-269 | none |
| CVE-2026-103782 | 9.9 | Dell | Enterprise Sonic Distributio | CWE-88 | none |
| CVE-2026-114819 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114822 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114848 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114978 | 9.9 | Oracle Corporation | Oracle Hyperion Financial Management | CWE-284 | none |
| CVE-2026-114980 | 9.9 | Oracle Corporation | Oracle AutoVue | CWE-284 | none |
| CVE-2026-127057 | 9.9 | Danfoss | AK-SC 355 | CWE-1392 | none |
| CVE-2026-129048 | 9.9 | Jacob N. Breetvelt | WP Photo Album Plus | CWE-94 | none |
| CVE-2026-129316 | 9.9 | Dokploy | dokploy | CWE-862 | poc |
| CVE-2026-129986 | 9.9 | Dokploy | dokploy | CWE-77,CWE-78 |  |
| CVE-2026-129987 | 9.9 | Dokploy | dokploy | CWE-77 | none |
| CVE-2026-129989 | 9.9 | Dokploy | dokploy | CWE-78 | poc |
| CVE-2026-129991 | 9.9 | Dokploy | dokploy | CWE-78 | none |
| CVE-2026-131253 | 9.9 | Splunk | Splunk SOAR | CWE-94 | none |
| CVE-2026-132231 | 9.9 | JetBrains | TeamCity | CWE-1289 | none |
| CVE-2026-132232 | 9.9 | JetBrains | TeamCity | CWE-88 | none |
| CVE-2026-132233 | 9.9 | JetBrains | TeamCity | CWE-23 | none |
| CVE-2026-132234 | 9.9 | JetBrains | TeamCity | CWE-88 | none |
| CVE-2026-132802 | 9.9 | Ubiquiti Inc | UniFi Access Application | CWE-59 | none |
| CVE-2026-132803 | 9.9 | Ubiquiti Inc | UniFi Access Application | CWE-89 | none |

## Top proveedores (CVE nuevos)

- Oracle Corporation: 578
- Linux: 493
- Google: 256
- JetBrains: 233
- Splunk: 146
- gpac: 77
- Unknown: 73
- frappe: 67
- Dell: 51
- Red Hat: 44

## Top CWE

- CWE-79: 458
- CWE-284: 356
- CWE-862: 348
- CWE-863: 183
- CWE-200: 175
- CWE-22: 144
- CWE-639: 138
- CWE-306: 132
- CWE-416: 118
- CWE-125: 104

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.20"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4637,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 4303
  }
}
```