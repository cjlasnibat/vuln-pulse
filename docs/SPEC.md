# Agente de Inteligencia de Vulnerabilidades — Especificación v0.1

Fecha: 2026-10-04 · Semana analizada: 27-sep → 04-oct-2026 (UTC-3)

Archivos de este paquete:

| Archivo | Rol en el agente |
|---|---|
| `SPEC.md` | Este documento: hallazgos de la semana, catálogo de fuentes, modelo de datos, métricas por rol |
| `sources.json` | Catálogo de fuentes legible por máquina (configuración del agente) |
| `collector.py` | Herramienta de recolección (sin dependencias externas, Python 3.9+) |
| `out/weekly_report.json` | Salida de ejemplo — contrato de datos que consumirá el agente |
| `out/weekly_report.md` | Misma salida en formato legible |

---

## 1. Reporte de la semana (27-sep → 04-oct-2026)

### 1.1 Lo esencial

- **7 vulnerabilidades agregadas a CISA KEV**, en 5 fabricantes. **4 de 7 afectan equipos de perímetro** (Citrix NetScaler ×2, Cisco SD-WAN Manager, FortiMail): el patrón dominante sigue siendo la explotación de dispositivos de borde.
- **Todas con plazo de remediación de 3 días** para agencias federales EE.UU. (lo normal es 21): CISA las trató como urgencias.
- **2.625 CVE nuevos publicados** (12 rechazados) y 3.130 registros actualizados.
- Severidad CVSS: **299 críticos (11,4 %)**, 1.081 altos, 1.075 medios, 119 bajos, 51 sin puntaje (98,1 % con CVSS).
- **CISA SSVC**: 393 CVE nuevos con explotación *PoC* o *activa*; 140 son *automatizables con impacto técnico total* — los más propensos a explotación masiva.
- Debilidades más frecuentes: CWE-79 XSS (342), CWE-862 falta de autorización (140), CWE-89 SQLi (119), CWE-22 path traversal (108), CWE-416 use-after-free (96).
- Las CNA con más volumen fueron VulnCheck, VulDB, Patchstack, GitHub y Apache. El volumen viene sobre todo de plugins WordPress y de routers/IoT de bajo costo. Por eso conviene filtrar por inventario propio antes de alertar.

### 1.2 KEV agregadas

| Fecha | CVE | Producto | Tipo | Plazo CISA | Nota |
|---|---|---|---|---|---|
| 27-sep | CVE-2026-88771 | Citrix NetScaler ADC/Gateway | Validación de entrada (RCE) | 30-sep | Zero-day; Unit 42 y Help Net reportan explotación desde inicios de septiembre, posible actor estatal |
| 27-sep | CVE-2026-88772 | Citrix NetScaler ADC/Gateway | Desbordamiento de memoria | 30-sep | Ídem; hay reportes de reinicios tras aplicar el parche |
| 29-sep | CVE-2026-86950 | Apple iOS/iPadOS/macOS (CoreGraphics) | Escritura fuera de límites | 02-oct | Ataques dirigidos ("extremely sophisticated"); ya hay PoC público |
| 30-sep | CVE-2026-76504 | Cisco Catalyst SD-WAN Manager | Bypass de autenticación en API (CISA: "Hex Encoding", CWE-177) | 03-oct | Sin workaround |
| 01-oct | CVE-2026-104286 | Fortinet FortiMail | Path traversal + NULL byte (escritura arbitraria) | 04-oct | CVSS 9.8, sin autenticación; inicialmente sin parche |
| 02-oct | CVE-2026-102489 | Zammad | Session fixation → RCE | 05-oct | Encadenable con la siguiente hasta root |
| 02-oct | CVE-2026-102490 | Zammad | Gestión de privilegios | 05-oct | |

**Acción recomendada**: comprobar si hay NetScaler, SD-WAN Manager, FortiMail o Zammad expuestos. Si los hay, parchear y además **asumir compromiso**: buscar webshells y cuentas nuevas, y rotar sesiones y credenciales. En equipos Apple gestionados, forzar la actualización por MDM.

### 1.3 Limitaciones de esta corrida

- **KEV**: se obtuvo del repositorio oficial de CISA `cisagov/kev-data` (catalogVersion `2026.10.02`, 1.733 entradas). Las 7 entradas coinciden con las alertas públicas de CISA.
- **EPSS no se calculó** en esta corrida, porque el entorno de prueba bloquea `api.first.org` (también `nvd.nist.gov`). El JSON de salida registra el estado de cada fuente en `sources_status`.

### 1.4 Por qué KEV se consume desde GitHub

CISA publica el catálogo en dos canales oficiales: `cisa.gov` (fuente canónica) y `github.com/cisagov/kev-data`. Según el README del repositorio:

- El propósito del repo es **facilitar el consumo programático**, porque el código "has an easier time consuming data sources from GitHub than … from US government websites".
- Ambas fuentes se sincronizan con minutos de diferencia.
- La licencia es la misma (CC0).
- El historial de commits sirve como registro de cambios del catálogo.

Por eso `collector.py` usa el repo como fuente primaria y `cisa.gov` como respaldo. Para auditoría, la referencia sigue siendo `cisa.gov`.

---

## 2. Catálogo de fuentes

Criterio de prioridad: **gratis + estructurado (JSON/CSV/API) + licencia que permita reutilizar** > cobertura > latencia. El detalle de endpoints y campos está en `sources.json`.

### Tier 1 — núcleo del pipeline

| Fuente | Qué responde | Formato | Acceso |
|---|---|---|---|
| **CISA KEV** | ¿Se está explotando? (confirmado) | JSON / CSV / schema. Primaria: repo oficial `cisagov/kev-data`; respaldo: cisa.gov (ver §1.4) | Libre |
| **CVE List V5** (CVE Program) | ¿Qué CVE nuevos o cambiados hay? Registro canónico | JSON 5.x en GitHub (`deltaLog.json` cubre 30 días, zips diarios) + CVE Services API | Libre |
| **CISA Vulnrichment (ADP)** | SSVC: explotación (none/poc/active), automatizable, impacto técnico; CVSS/CWE cuando la CNA no los entrega | Dentro del registro CVE + repo `cisagov/vulnrichment` | Libre |
| **NVD API 2.0** | CVSS de NIST, **CPE match** (para cruzar con el inventario), historial de cambios | JSON REST | API key gratuita |
| **FIRST EPSS** | Probabilidad de explotación en 30 días | JSON REST + CSV diario | Libre |
| **ENISA EUVD** | Visión UE: listas de explotadas y críticas, EPSS integrado | JSON REST | Libre |

### Tier 2 — enriquecimiento

| Fuente | Qué aporta |
|---|---|
| OSV.dev | Dependencias open source (npm, PyPI, Maven, Go…), consultas en lote; útil contra SBOM |
| GitHub Advisory Database | Advisories revisados por ecosistema (formato OSV) |
| CSAF 2.0 / VEX de fabricantes (Microsoft, Red Hat, Siemens, Cisco, CISA ICS) | Versión corregida y estado de afectación por producto (VEX). Es la base para remediar automáticamente |
| MSRC Security Update Guide API | Patch Tuesday, marca *Exploitation Detected / More Likely* |
| Exploit-DB (CSV), Metasploit (JSON), nuclei-templates | Señales de **weaponización**: exploit público, módulo listo para usar, escaneo masivo posible |
| VulnCheck KEV (community, token gratis) | KEV más amplio y a menudo anterior a CISA |
| MITRE CWE / CAPEC / ATT&CK (STIX) | Taxonomía para agrupar y explicar tendencias |
| **Shadowserver** (registro gratuito como dueño de la red) | Exposición real de **tus** IPs y dominios. La fuente externa de más valor para la organización |

### Tier 3 — contexto (estructura limitada)

ransomware.live (API JSON de víctimas y grupos por país/sector), CSIRT de Gobierno / ANCI Chile (alertas y contexto regulatorio local), JVN (Japón), PSIRT de fabricantes vía RSS y prensa especializada para narrativa.

> Regla para el agente: **las decisiones solo se toman con fuentes Tier 1–2**; las de Tier 3 sirven para explicar, no para priorizar.

---

## 3. Modelo de datos y priorización

### 3.1 Entidad normalizada `vuln`

```json
{
  "cve_id": "CVE-2026-104286",
  "aliases": ["EUVD-…", "GHSA-…"],
  "vendor": "Fortinet", "product": "FortiMail",
  "cpe": ["cpe:2.3:a:fortinet:fortimail:*"],
  "published": "2026-10-01", "cwe": ["CWE-22"],
  "cvss": {"version": "3.1", "score": 9.8, "vector": "…"},
  "ssvc": {"exploitation": "active", "automatable": "yes", "technical_impact": "total"},
  "epss": {"score": 0.0, "percentile": 0.0, "date": "…"},
  "kev": {"in_kev": true, "date_added": "2026-10-01", "due": "2026-10-04", "ransomware": "Unknown"},
  "exploit_public": true, "metasploit": false, "nuclei": true,
  "fix": {"available": false, "csaf_url": "…"},
  "internal": {"assets_affected": 3, "internet_facing": 1, "crown_jewel": false, "owner": "Infra"}
}
```

El bloque `internal` lo llena el agente cruzando CPE, vendor y producto contra el inventario (CMDB, EDR, escáner). Sin ese cruce, las métricas de exposición propia no se pueden calcular.

### 3.2 Prioridad sugerida (alineada a SSVC / CISA)

| Prioridad | Regla | SLA sugerido |
|---|---|---|
| **P0 – Act** | KEV **o** SSVC `active`, y activo propio expuesto a Internet | 72 h (o el plazo KEV si es menor) |
| **P1 – Attend** | KEV/`active` en activo interno, **o** EPSS ≥ 0,10 (o percentil ≥ 95) con CVSS ≥ 7, **o** `automatable=yes` + `total` en activo expuesto | 7 días |
| **P2 – Track*** | CVSS ≥ 9 sin señal de explotación, o exploit público / nuclei | 30 días |
| **P3 – Track** | Resto | Ciclo normal de parches |

---

## 4. Métricas por rol

Leyenda de fuente: **E** = solo datos externos (calculable hoy con este paquete) · **E+I** = requiere cruzar con inventario o escáner propio.

### 4.1 Oficial de seguridad — uso diario y operativo

Objetivo: **qué hacer hoy**.

| # | Métrica | Definición / fórmula | Fuente | Frecuencia | Umbral o alerta |
|---|---|---|---|---|---|
| O1 | **Nuevas KEV que me afectan** | KEV agregadas en las últimas 24 h ∩ inventario | E+I | Diaria (y cada 4 h si es posible) | ≥1 → alerta inmediata |
| O2 | Nuevas KEV (global) | Conteo y lista de KEV agregadas en 24 h / 7 d | E | Diaria | Informativa; resaltar fabricantes presentes en el inventario |
| O3 | **Cola P0/P1 abierta** | N.º de pares activo-vulnerabilidad en P0 y P1 sin remediar | E+I | Diaria | P0 > 0 → escalar |
| O4 | KEV vencidas internas | Hallazgos KEV con fecha actual > `dueDate` (o SLA interno) | E+I | Diaria | > 0 |
| O5 | Saltos de EPSS | CVE presentes en el inventario cuyo EPSS subió ≥ 0,1 o cruzó el percentil 95 desde ayer | E+I | Diaria | Reclasificar a P1 |
| O6 | Cambio de estado SSVC | CVE presentes en el inventario que pasan `none → poc → active` | E+I | Diaria | `active` → P0/P1 |
| O7 | Nuevo exploit público / módulo / plantilla nuclei | CVE presentes en el inventario con exploit nuevo publicado | E+I | Diaria | Reclasificar |
| O8 | Exposición externa (Shadowserver/ASM) | Servicios vulnerables o comprometidos reportados para tus IPs | E+I | Diaria | ≥1 → incidente |
| O9 | Perímetro en la mira | % de KEV de la semana sobre equipos de borde (VPN, ADC, firewall, gateway de correo) | E | Semanal | Esta semana: **4/7 (57 %)** |
| O10 | Cobertura de detección | % de CVE P0 con regla de detección o caza activa (EDR/SIEM/IDS) | I | Diaria | < 100 % |

### 4.2 Gerente de TI — ejecución y capacidad de remediación

Objetivo: **¿estamos parchando a tiempo y con qué carga?**

| # | Métrica | Definición / fórmula | Fuente | Frecuencia | Meta referencial |
|---|---|---|---|---|---|
| G1 | **Cumplimiento de SLA por prioridad** | % de hallazgos cerrados dentro del SLA (P0/P1/P2) | E+I | Diaria (tablero) y semanal (reporte) | P0 ≥ 95 %, P1 ≥ 90 % |
| G2 | **MTTR** (tiempo medio de remediación) | Mediana y p90 de (fecha de cierre − fecha de detección), por prioridad y por equipo | E+I | Semanal | P0 ≤ 3 d, P1 ≤ 7 d |
| G3 | Backlog y tendencia | Hallazgos abiertos por prioridad, con su variación semanal (Δ) | E+I | Diaria | Δ ≤ 0 |
| G4 | Burn-down rate | Hallazgos cerrados ÷ hallazgos nuevos en la semana | E+I | Semanal | ≥ 1,0 |
| G5 | Antigüedad del backlog | Distribución en 0-7 / 8-30 / 31-90 / > 90 días | E+I | Semanal | Ninguna P0/P1 > 30 d |
| G6 | Cobertura de parches por plataforma | % de equipos al día por SO o fabricante (Windows, Apple, Linux, red) | I | Semanal | ≥ 95 % |
| G7 | Carga prevista de la semana | Nuevos CVE que afectan al inventario, por fabricante, con parche disponible (CSAF/VEX) | E+I | Semanal | Para planificar ventanas |
| G8 | Vulnerabilidades sin parche | CVE presentes en el inventario sin fix disponible, con su mitigación aplicada (sí/no) | E+I | Diaria | 100 % mitigadas |
| G9 | Concentración por fabricante | Top 10 fabricantes por CVE (global y en el inventario) | E | Semanal | Esta semana el top global es Apache, Google y NVIDIA |
| G10 | Activos sin dueño o fuera de inventario | % de activos descubiertos (escáner/ASM) sin dueño en la CMDB | I | Semanal | < 2 % |

### 4.3 CISO — riesgo, tendencia y rendición de cuentas

Objetivo: **¿el riesgo sube o baja, estamos invirtiendo bien y podemos demostrarlo?**

| # | Métrica | Definición / fórmula | Fuente | Frecuencia | Uso |
|---|---|---|---|---|---|
| C1 | **Exposición KEV** | N.º de activos (y % de los críticos) con al menos una KEV abierta; tendencia de 12 semanas | E+I | Semanal / mensual | KRI principal |
| C2 | **Ventana de exposición KEV** | Mediana de días entre `dateAdded` de KEV y el cierre interno | E+I | Mensual | Comparable con los plazos que fija CISA para KEV (directiva vigente: BOD 26-04) |
| C3 | Riesgo ponderado | Σ por activo de (criticidad × factor de explotación), con factor = 1,0 si KEV/active; EPSS en otro caso | E+I | Mensual | Mostrar tendencia, no valor absoluto |
| C4 | % de remediación priorizada por riesgo | Del esfuerzo de parcheo, % dedicado a P0/P1 frente al total | E+I | Mensual | Muestra si el equipo trabaja en lo que importa |
| C5 | Excepciones de riesgo | N.º y antigüedad de excepciones o aceptaciones de riesgo vigentes; % vencidas | I | Mensual | Gobierno |
| C6 | Riesgo de terceros | N.º de proveedores críticos con productos en KEV en el período | E+I | Mensual | Gestión de proveedores |
| C7 | Panorama externo | KEV/mes, % en equipos de borde, % con ransomware conocido, volumen de CVE y % críticos | E | Mensual / trimestral | Contexto para directorio. Esta semana: 7 KEV, 2.625 CVE, 11,4 % críticos |
| C8 | Cumplimiento regulatorio | Avance frente a obligaciones (p. ej. Ley 21.663 / ANCI para operadores de importancia vital; CIS Control 7; ISO 27001 A.8.8) | I | Trimestral | Auditoría |
| C9 | Cobertura de visibilidad | % de activos con escaneo autenticado o agente; % con SBOM | I | Trimestral | Mide qué tan confiables son las demás métricas |
| C10 | Eventos explotados | N.º de incidentes cuyo vector fue una vulnerabilidad conocida, y cuántos días llevaba abierta | I | Trimestral | Lección aprendida y caso de inversión |

### 4.4 Principios de diseño de las métricas

1. **Explotación por sobre severidad**: KEV, SSVC y EPSS ordenan; el CVSS solo desempata. Con 299 críticos en una semana, priorizar por CVSS es inmanejable.
2. **Siempre cruzar con el inventario**: el volumen global (2.625 CVE por semana) es ruido mientras no se filtre por lo que la organización tiene.
3. **Medianas y p90** en vez de promedios para los tiempos.
4. **Tendencia > foto**: el CISO ve 12 semanas, el gerente la semana y el oficial el día.
5. **Cada métrica declara su fuente y su frescura**: si `sources_status.epss.ok = false`, las métricas O5 y C3 se marcan como no confiables.

---

## 5. Diseño del agente (borrador)

```
[Cron 07:00 y 13:00 CLT]
   └─ collector.py --days 1   (diario)   / --days 7 (lunes)
        ├─ KEV, CVE List V5 (+ADP/SSVC), EPSS, EUVD
        └─ weekly_report.json  ── sources_status
   └─ enrich: NVD CPE, CSAF/VEX, exploit-db/metasploit/nuclei
   └─ match: inventario (CMDB/EDR/escáner/SBOM) → bloque `internal`
   └─ score: reglas §3.2 → P0..P3
   └─ outputs por rol:
        Oficial  → alerta inmediata P0 + digest diario (O1–O10)
        Gerente  → tablero SLA/MTTR/backlog (G1–G10), lunes
        CISO     → resumen mensual con tendencias (C1–C10) y narrativa
```

Guardrails para el LLM:

- Los números **solo** salen del JSON; el modelo redacta, no calcula.
- Cada afirmación lleva el CVE y la fuente.
- Si una fuente falla, el reporte lo dice explícitamente.
- Deduplicar por `cve_id` y alias (EUVD, GHSA).
- Nunca degradar una KEV por tener CVSS bajo.

Próximos pasos sugeridos:

1. Conectar el inventario (es lo que habilita O1, G1 y C1).
2. Habilitar egress a `raw.githubusercontent.com`, `cisa.gov` (respaldo), `nvd.nist.gov`, `api.first.org` y `euvd.enisa.europa.eu`.
3. Registrar la red en Shadowserver.
4. Agregar módulos de NVD/CSAF/exploit-db a `collector.py`.
5. Persistir los snapshots diarios para calcular tendencias.
