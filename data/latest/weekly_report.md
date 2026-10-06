# Reporte semanal de vulnerabilidades — 2026-09-30 a 2026-10-06

## Resumen

- KEV agregadas: **5** (catálogo total: 1734; ransomware conocido: 0)
- CVE nuevos publicados: **2504** (rechazados: 8; registros actualizados: 2875)
- Por severidad CVSS: {'HIGH': 962, 'CRITICAL': 245, 'MEDIUM': 980, 'SIN_CVSS': 234, 'LOW': 83}  — con CVSS: 90.7%
- SSVC (CISA ADP) explotación PoC/activa: 324; automatizable + impacto total: 127
- EPSS ≥ 10%: 0

## KEV agregadas en la semana

| Fecha | CVE | Proveedor / Producto | Vulnerabilidad | Vence (FCEB) | Ransomware |
|---|---|---|---|---|---|
| 2026-09-30 | CVE-2026-76504 | Cisco Catalyst SD-WAN Manager | Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability | 2026-10-03 | Unknown |
| 2026-10-01 | CVE-2026-104286 | Fortinet FortiMail | Fortinet FortiMail Path Traversal Vulnerability | 2026-10-04 | Unknown |
| 2026-10-02 | CVE-2026-102490 | Zammad GmbH Zammad | Zammad GmbH Zammad Improper Privilege Management Vulnerability | 2026-10-05 | Unknown |
| 2026-10-02 | CVE-2026-102489 | Zammad GmbH Zammad | Zammad GmbH Zammad Session Fixation Vulnerability | 2026-10-05 | Unknown |
| 2026-10-04 | CVE-2026-88779 | Citrix NetScaler | Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability | 2026-10-07 | Unknown |

## CVE críticos (CVSS ≥ 9.0) publicados

| CVE | Score | Proveedor | Producto | CWE | SSVC expl. |
|---|---|---|---|---|---|
| CVE-2026-100103 | 10 | Perfoce | P4 (Helix Core) | CWE-1392 | none |
| CVE-2026-101148 | 10 | Unknown | BackupSheep WordPress Backup Plugin | CWE-73 | none |
| CVE-2026-102427 | 10 | ordasoft.com | OrdaSoft Joomla CCK | CWE-434 | none |
| CVE-2026-103956 | 10 | AWS | loom | CWE-1188,CWE-306 | none |
| CVE-2026-104610 | 10 | Tenda | HG7 | CWE-119,CWE-121 | poc |
| CVE-2026-105134 | 10 | Ahsay | AhsayCBS | CWE-77,CWE-78 | none |
| CVE-2026-105135 | 10 | InternLM | MindSearch | CWE-74,CWE-94 |  |
| CVE-2026-105284 | 10 | Totolink | A3002MU | CWE-266,CWE-285 | poc |
| CVE-2026-105285 | 10 | Totolink | A3002MU | CWE-119,CWE-121 | poc |
| CVE-2026-105484 | 10 | TOTOLINK | X6000R | CWE-77,CWE-78 | none |
| CVE-2026-105857 | 10 | payloadcms | payload | CWE-1321,CWE-94 |  |
| CVE-2026-32579 | 10 | kognetiks | Kognetiks Chatbot for WordPress | CWE-434 | none |
| CVE-2026-39770 | 10 | AmentoTech | Doctreat | CWE-434 | none |
| CVE-2026-39773 | 10 | AmentoTech | Doctreat Core | CWE-266 | none |
| CVE-2026-55107 | 10 | elct9620 | kobako | CWE-470,CWE-94 | poc |
| CVE-2026-55393 | 10 | Teledyne FLIR | Aware2 | CWE-22 | none |
| CVE-2026-63688 | 10 | Dell | Dell Container Storage Modules (CSM) | CWE-306 |  |
| CVE-2026-63692 | 10 | Dell | Container Storage Modules | CWE-306 |  |
| CVE-2026-76570 | 10 | joomcode.com | JCTables extension for Joomla | CWE-89 | none |
| CVE-2026-96349 | 10 | SiteSkite | SiteSkite | CWE-94 | none |
| CVE-2026-105636 | 9.9 | makeplane | plane | CWE-918 |  |
| CVE-2026-105691 | 9.9 | penpot | penpot | CWE-78 | poc |
| CVE-2026-105697 | 9.9 | langflow-ai | langflow | CWE-78 | none |
| CVE-2026-105740 | 9.9 | langflow-ai | langflow | CWE-78 |  |
| CVE-2026-32568 | 9.9 | JMAPlugins | WooCommerce Designer Pro | CWE-94 | none |
| CVE-2026-39755 | 9.9 | revmakx | WP Duplicate | CWE-434 | none |
| CVE-2026-39757 | 9.9 | AmentoTech | Taskbot | CWE-434 | none |
| CVE-2026-39759 | 9.9 | AmentoTech | Workreap Core | CWE-434 | none |
| CVE-2026-67269 | 9.9 | Dell | Container Storage Modules (CSM) | CWE-269 |  |
| CVE-2026-79901 | 9.9 | Fortra | BoKS Manager boks-server | CWE-338 | none |
| CVE-2026-90970 | 9.9 | GitLab | GitLab AI Gateway | CWE-1336 | none |
| CVE-2026-93698 | 9.9 | Webpros | cPanel | CWE-78 | none |
| CVE-2026-96658 | 9.9 | Red Hat | Red Hat Satellite 6.16 for RHEL 8 | CWE-94 | none |
| CVE-2026-100512 | 9.8 | Hook & Filter | Nested Pages | CWE-502 | none |
| CVE-2026-102115 | 9.8 | Kiteworks | Core | CWE-640 | none |
| CVE-2026-103110 | 9.8 | Pexip | Infinity | CWE-787 | none |
| CVE-2026-103752 | 9.8 | Paul Ryan | Authorizer | CWE-266 | none |
| CVE-2026-104056 | 9.8 | Authlib | Authlib | CWE-345,CWE-346 | poc |
| CVE-2026-104286 | 9.8 | Fortinet | FortiMail | CWE-22 | active |
| CVE-2026-104711 | 9.8 | Apache Software Foundation | Apache Struts | CWE-917 | none |

## Top proveedores (CVE nuevos)

- Linux: 208
- Apache Software Foundation: 120
- NVIDIA: 114
- Unknown: 101
- n/a: 94
- Kiteworks: 61
- TryGhost: 54
- Red Hat: 53
- JetBrains: 40
- Google: 38

## Top CWE

- CWE-79: 363
- CWE-862: 168
- CWE-89: 151
- CWE-639: 90
- CWE-22: 88
- CWE-74: 77
- CWE-918: 77
- CWE-94: 64
- CWE-787: 61
- CWE-770: 57

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
    "fetched": 2512,
    "errors": 0
  },
  "epss": {
    "ok": true,
    "scored": 2399
  }
}
```