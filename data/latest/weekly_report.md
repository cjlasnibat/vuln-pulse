# Reporte semanal de vulnerabilidades — 2026-11-14 a 2026-11-20

## Resumen

- KEV agregadas: **5** (catálogo total: 1786; ransomware conocido: 0)
- CVE nuevos publicados: **4182** (rechazados: 17; registros actualizados: 6926)
- Por severidad CVSS: {'CRITICAL': 360, 'HIGH': 1316, 'SIN_CVSS': 530, 'MEDIUM': 1748, 'LOW': 228}  — con CVSS: 87.3%
- SSVC (CISA ADP) explotación PoC/activa: 334; automatizable + impacto total: 174
- EPSS ≥ 10%: 7

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-11-17 | CVE-2026-115731 | Perforce Puppet Enterprise | Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability | 2026-12-01 | Unknown |
| 2026-11-18 | CVE-2024-10441 | Synology DiskStation Manager (DSM) | Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability | 2026-11-21 | Unknown |
| 2026-11-18 | CVE-2026-40217 | BerriAI LiteLLM | BerriAI LiteLLM Unprotected Alternate Channel Vulnerability | 2026-12-02 | Unknown |
| 2026-11-18 | CVE-2026-90817 | Vanderbilt University Research Electronic Data Capture (REDCap) | Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability | 2026-11-21 | Unknown |
| 2026-11-18 | CVE-2026-90436 | Apache Axis | Apache Axis Unsafe Reflection Vulnerability | 2026-11-21 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-100397 | 10 | rucio | rucio | CWE-287 | poc |
| CVE-2026-114202 | 10 | ASUS | Control Center Express | CWE-321 | none |
| CVE-2026-114784 | 10 | Oracle Corporation | Oracle Business Intelligence Enterprise  | CWE-306 | none |
| CVE-2026-114824 | 10 | Oracle Corporation | Oracle Platform Security for Java | CWE-502 | none |
| CVE-2026-114835 | 10 | Oracle Corporation | Oracle Access Manager | CWE-306 | none |
| CVE-2026-120387 | 10 | Circutor | PowerStudio SCADA Wave | CWE-347 | poc |
| CVE-2026-129351 | 10 | TRENDnet | TEW-657BRM | CWE-119,CWE-787 | poc |
| CVE-2026-129353 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | none |
| CVE-2026-129354 | 10 | D-Link | DIR-600L | CWE-119,CWE-121 | poc |
| CVE-2026-129444 | 10 | D-Link | DSL-6740C | CWE-259,CWE-798 | none |
| CVE-2026-130778 | 10 | lxc | incus | CWE-287 |  |
| CVE-2026-133323 | 10 | Mitel | MiCollab | CWE-78 | none |
| CVE-2026-133493 | 10 | D-Link | DIR-600L | CWE-77,CWE-78 | poc |
| CVE-2026-14914 | 10 | Tegsoft Yönetim ve Bilişim Hizmetleri Tic. Ltd. Şti. | Tegsoft Contact Center | CWE-434 | none |
| CVE-2026-53998 | 10 | Arize-ai | phoenix | CWE-134,CWE-200 | none |
| CVE-2026-71499 | 10 | hefy2027 | cf-manager | CWE-918,CWE-94 | none |
| CVE-2026-75521 | 10 | mirendev | runtime | CWE-295 |  |
| CVE-2026-77312 | 10 | flytohub | flyto-core | CWE-22 |  |
| CVE-2026-91500 | 10 | Oracle Corporation | Oracle Access Manager | CWE-284 | none |
| CVE-2026-91510 | 10 | Oracle Corporation | Oracle Access Manager | CWE-306 | none |
| CVE-2026-91569 | 10 | Oracle Corporation | Oracle WebLogic Server | CWE-306 | none |
| CVE-2026-93664 | 10 | Dassault Systèmes | Station Launcher App in 3DEXPERIENCE pla | CWE-502 | none |
| CVE-2026-95787 | 10 | Hewlett Packard Enterprise (HPE) | ArubaOS (AOS) | CWE-269 | none |
| CVE-2026-114819 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114822 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114848 | 9.9 | Oracle Corporation | Oracle Database Server | CWE-284 | none |
| CVE-2026-114978 | 9.9 | Oracle Corporation | Oracle Hyperion Financial Management | CWE-284 | none |
| CVE-2026-114980 | 9.9 | Oracle Corporation | Oracle AutoVue | CWE-284 | none |
| CVE-2026-127057 | 9.9 | Danfoss | AK-SC 355 | CWE-1392 | none |
| CVE-2026-129048 | 9.9 | Jacob N. Breetvelt | WP Photo Album Plus | CWE-94 |  |
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

## Top proveedores (CVE nuevos)

- Oracle Corporation: 578
- Linux: 516
- JetBrains: 231
- Google: 203
- Splunk: 146
- Unknown: 61
- gpac: 48
- nocodb: 43
- Dell: 40
- flowintel: 37

## Top CWE

- CWE-79: 390
- CWE-862: 307
- CWE-284: 291
- CWE-200: 174
- CWE-863: 165
- CWE-22: 134
- CWE-639: 133
- CWE-306: 133
- CWE-416: 97
- CWE-125: 82

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.11.18"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 4199,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 3969
  }
}
```