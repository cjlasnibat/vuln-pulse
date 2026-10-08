# Reporte semanal de vulnerabilidades — 2026-10-02 a 2026-10-08

## Resumen

- KEV agregadas: **3** (catálogo total: 1734; ransomware conocido: 0)
- CVE nuevos publicados: **2623** (rechazados: 10; registros actualizados: 2518)
- Por severidad CVSS: {'HIGH': 957, 'MEDIUM': 1116, 'LOW': 91, 'SIN_CVSS': 204, 'CRITICAL': 255}  — con CVSS: 92.2%
- SSVC (CISA ADP) explotación PoC/activa: 319; automatizable + impacto total: 130
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-10-02 | CVE-2026-102490 | Zammad GmbH Zammad | Zammad GmbH Zammad Improper Privilege Management Vulnerability | 2026-10-05 | Unknown |
| 2026-10-02 | CVE-2026-102489 | Zammad GmbH Zammad | Zammad GmbH Zammad Session Fixation Vulnerability | 2026-10-05 | Unknown |
| 2026-10-04 | CVE-2026-88779 | Citrix NetScaler | Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability | 2026-10-07 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2025-70518 | 10 | n/a | n/a | CWE-77 | poc |
| CVE-2026-100103 | 10 | Perfoce | P4 (Helix Core) | CWE-1392 | none |
| CVE-2026-102255 | 10 | SonicWall | SMA1000 | CWE-441,CWE-918 | none |
| CVE-2026-103956 | 10 | AWS | loom | CWE-1188,CWE-306 | none |
| CVE-2026-104610 | 10 | Tenda | HG7 | CWE-119,CWE-121 | poc |
| CVE-2026-105134 | 10 | Ahsay | AhsayCBS | CWE-77,CWE-78 | none |
| CVE-2026-105135 | 10 | InternLM | MindSearch | CWE-74,CWE-94 | poc |
| CVE-2026-105284 | 10 | Totolink | A3002MU | CWE-266,CWE-285 | poc |
| CVE-2026-105285 | 10 | Totolink | A3002MU | CWE-119,CWE-121 | poc |
| CVE-2026-105484 | 10 | TOTOLINK | X6000R | CWE-77,CWE-78 | none |
| CVE-2026-105857 | 10 | payloadcms | payload | CWE-1321,CWE-94 | none |
| CVE-2026-106102 | 10 | quasarframework | quasar | CWE-116,CWE-79 | none |
| CVE-2026-12260 | 10 | NetBoard CRM | NetBoard CRM Demo Platform | CWE-89 |  |
| CVE-2026-32579 | 10 | kognetiks | Kognetiks Chatbot for WordPress | CWE-434 | none |
| CVE-2026-39770 | 10 | AmentoTech | Doctreat | CWE-434 | none |
| CVE-2026-39773 | 10 | AmentoTech | Doctreat Core | CWE-266 | none |
| CVE-2026-63688 | 10 | Dell | Dell Container Storage Modules (CSM) | CWE-306 | none |
| CVE-2026-63692 | 10 | Dell | Container Storage Modules | CWE-306 |  |
| CVE-2026-76482 | 10 | Cisco | Cisco License On-Prem | CWE-347 | none |
| CVE-2026-105636 | 9.9 | makeplane | plane | CWE-918 | poc |
| CVE-2026-105691 | 9.9 | penpot | penpot | CWE-78 | poc |
| CVE-2026-105697 | 9.9 | langflow-ai | langflow | CWE-78 | none |
| CVE-2026-105740 | 9.9 | langflow-ai | langflow | CWE-78 | poc |
| CVE-2026-32568 | 9.9 | JMAPlugins | WooCommerce Designer Pro | CWE-94 | none |
| CVE-2026-39755 | 9.9 | revmakx | WP Duplicate | CWE-434 | none |
| CVE-2026-39757 | 9.9 | AmentoTech | Taskbot | CWE-434 | none |
| CVE-2026-39759 | 9.9 | AmentoTech | Workreap Core | CWE-434 | none |
| CVE-2026-67269 | 9.9 | Dell | Container Storage Modules (CSM) | CWE-269 |  |
| CVE-2026-79798 | 9.9 | Hewlett Packard Enterprise (HPE) | ClearPass Policy Manager (CPPM) | CWE-89 | none |
| CVE-2026-90970 | 9.9 | GitLab | GitLab AI Gateway | CWE-1336 | none |
| CVE-2026-93698 | 9.9 | Webpros | cPanel | CWE-78 | none |
| CVE-2025-70521 | 9.8 | n/a | n/a | CWE-77 | none |
| CVE-2025-71383 | 9.8 | n/a | n/a | CWE-20 | poc |
| CVE-2026-103646 | 9.8 | Unknown | Ultimate Multisite | CWE-287 | none |
| CVE-2026-103692 | 9.8 | Unknown | Frontend Dashboard | CWE-269 | none |
| CVE-2026-103877 | 9.8 | Apache Software Foundation | Apache Directory LDAP API | CWE-502 | none |
| CVE-2026-104334 | 9.8 | IBM | Langflow OSS | CWE-94 | none |
| CVE-2026-104711 | 9.8 | Apache Software Foundation | Apache Struts | CWE-917 | none |
| CVE-2026-104846 | 9.8 | lxsmnsyc | seroval | CWE-843 | none |
| CVE-2026-105105 | 9.8 | NASA-AMMOS | AIT-Core | CWE-306 | none |

## Top proveedores (CVE nuevos)

- Google: 291
- Linux: 210
- Unknown: 106
- Apache Software Foundation: 96
- n/a: 76
- Red Hat: 67
- IBM: 64
- Brocade: 61
- backstage: 41
- Hewlett Packard Enterprise (HPE): 38

## Top CWE

- CWE-79: 263
- CWE-862: 179
- CWE-89: 121
- CWE-863: 111
- CWE-22: 85
- CWE-639: 79
- CWE-200: 77
- CWE-918: 71
- CWE-94: 68
- CWE-74: 64

## Estado de fuentes

```json
{
  "kev": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/cisagov/kev-data/main/known_exploited_vulnerabilities.json",
    "catalogVersion": "2026.10.04"
  },
  "cvelist": {
    "ok": true,
    "source": "https://raw.githubusercontent.com/CVEProject/cvelistV5/main/cves/deltaLog.json",
    "fetched": 2633,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2440
  }
}
```