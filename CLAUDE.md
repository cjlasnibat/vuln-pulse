# vuln-pulse — contexto para Claude Code

Pipeline de inteligencia de vulnerabilidades con fuentes abiertas, pensado como base de un agente IA.
Lo usan tres perfiles: **oficial de seguridad** (operación diaria), **gerente TI** (carga y remediación) y **CISO** (riesgo y tendencia).
Idioma del proyecto: español de Chile (código y comentarios pueden ir en inglés o español; textos de usuario siempre en español).

## Arquitectura (en producción)

```
GitHub Actions (.github/workflows/daily.yml, 10:20 UTC)
  src/collector.py           → data/latest/weekly_report.{json,md}   (ventana 7 días)
  src/snapshot.py            → data/history/AAAA-MM-DD.json           (~2 KB/día, tendencias largas)
  src/build_dashboard_data.py + src/dashboard_template.html → site/index.html → GitHub Pages
                               https://cjlasnibat.github.io/vuln-pulse/
n8n Cloud (workflows exportados en n8n/)
  01_kev_alerta.json         cada 2 h: KEV nuevas ∩ watchlist → correo
  02_resumen_semanal.json    lunes 08:00: weekly_report + snapshot previo → Claude API → 3 correos por rol
```

## Fuentes (detalle en config/sources.json)

- **CISA KEV**: primaria `raw.githubusercontent.com/cisagov/kev-data` (canal oficial de CISA para consumo programático), respaldo cisa.gov.
- **CVE List V5**: `cves/deltaLog.json` en `CVEProject/cvelistV5`. Solo cubre 30 días; por eso existe `data/history/`.
- **CISA ADP / Vulnrichment**: SSVC (exploitation, automatable, technical impact) dentro de cada registro CVE.
- **FIRST EPSS**: `api.first.org`. Funciona desde GitHub Actions.

## Reglas del proyecto (no romper)

1. **Solo librería estándar de Python (3.9+).** Sin dependencias, para que corra igual en Actions, local o cualquier runner.
2. **Los números se calculan en código, nunca en el LLM.** El LLM (workflow 02) solo redacta a partir del JSON.
3. **Cada fuente falla de forma aislada** y queda registrada en `sources_status`; las métricas que dependen de una fuente caída se marcan, no se inventan.
4. **Prioridad por explotación antes que severidad**: KEV / SSVC active > EPSS > CVSS. Nunca degradar una KEV por CVSS o EPSS bajo.
5. **Zona horaria America/Santiago** para fechas de corte y agrupación diaria.
6. **El repo es público.** Nunca commitear: watchlist real, correos, llaves, inventario de activos, nombres de clientes. Esos datos viven en n8n o en almacenamiento privado. Antes de exportar un workflow de n8n a `n8n/`, reemplazar destinatarios y watchlist por valores de ejemplo (las credenciales no se exportan, pero el código de los nodos sí).
   - **La watchlist del repo es de ejemplo, no un inventario.** Es el top 20 de fabricantes por cantidad de KEV en el catálogo de CISA (corte 2026-10-04) más empates en el corte (Mozilla, Atlassian): Microsoft, Cisco, Apple, Adobe, Google, Oracle, Apache, Ivanti, Fortinet, Linux, Citrix, D-Link, VMware, SonicWall, Synacor, Android, Palo Alto Networks, Samsung, SAP, Zyxel, Mozilla, Atlassian.
   - Vive en tres lugares que deben mantenerse iguales: `WATCHLIST` en `n8n/01_kev_alerta.json` y `n8n/02_resumen_semanal.json`, y `EXAMPLE_WATCHLIST` en `src/build_dashboard_data.py` (es el default del tablero cuando `WATCHLIST_DEFAULT` no está definida).
   - Criterio de desempate en el corte: se incluye el fabricante si es de perímetro o de endpoint (Atlassian entró por decisión explícita). Para regenerarla, contar `vendorProject` en `known_exploited_vulnerabilities.json` de `cisagov/kev-data`.
   - La lista real se configura solo dentro de n8n o en la variable `WATCHLIST_DEFAULT` de Actions (que es pública en el tablero, así que tampoco debe ser el inventario real).
7. **No editar `data/` a mano**: lo escribe el workflow diario.

## Contrato de datos (lo consumen n8n y el tablero)

`data/latest/weekly_report.json` — claves usadas por los workflows de n8n; cambios = versión nueva + actualizar n8n:
- `window{start,end,utc_offset}`, `generated_at`, `sources_status{kev,cvelist,epss}{ok,…}`
- `summary{kev_added, kev_catalog_total, kev_ransomware_known, kev_vendors, cve_new, cve_rejected, cve_updated, cve_by_severity, cve_with_cvss_pct, ssvc_poc_or_active, ssvc_automatable_total_impact, epss_ge_10pct, top_vendors, top_cwe, top_cna}`
- `kev_new[]` (registros KEV + `epss`), `critical_cves[]`, `ssvc_poc_or_active[]`, `high_epss[]` (con `--top 500`)

`data/history/AAAA-MM-DD.json` — ver `src/snapshot.py` (`kev.*`, `cve_7d.*`). El workflow 02 lee el de hace 7 días.

## Comandos

```bash
# Reporte de 7 días (≈40 s)
python3 src/collector.py --days 7 --out out/ --top 500
# Tablero de 30 días (≈2–3 min, descarga ~14k registros CVE)
python3 src/build_dashboard_data.py --days 30 --template src/dashboard_template.html \
        --out out/site/index.html --data-out out/site/dashboard_data.json
# Foto diaria
python3 src/snapshot.py --report out/weekly_report.json --date $(TZ=America/Santiago date +%F) --out out/history
```
Usar `out/` para pruebas locales (está en .gitignore); no escribir en `data/`.

## Limitaciones conocidas

- SSVC llega con 1–3 días de retraso: los últimos días siempre se ven incompletos.
- EPSS es bajo para CVE recién publicados (KEV de la semana con EPSS < 3 %). No sirve para descartar urgencia.
- "Perímetro" es una heurística por palabras clave (`EDGE_HINTS` en build_dashboard_data.py y `EDGE` en n8n/01).
- El cron de Actions está en UTC: 07:20 en horario de verano chileno, 06:20 en invierno.
- `dashboard_data.json` pesa ~2,4 MB: no se commitea, solo va al artefacto de Pages.
- Métricas internas (SLA, MTTR, exposición KEV propia) están "pendientes": requieren inventario.

## Roadmap (orden sugerido)

1. **Tests**: pytest con fixtures pequeñas (KEV y registros CVE recortados) para `parse_cve_record`, `kev_in_window`, `sev_bucket`, snapshot. Job de CI que corra tests en cada push/PR.
2. **JSON Schema** de `weekly_report.json` y validación en CI, para no romper n8n sin aviso.
3. **Tendencias largas en el tablero** leyendo `data/history/` (KEV/semana, críticos/semana, 12+ semanas).
4. **Inventario** (privado): formato CSV mínimo `activo,fabricante,producto,version,expuesto_internet,criticidad,dueño`; cruce por fabricante/producto y luego por CPE (NVD API). Debe vivir fuera del repo público (repo privado, secreto de Actions o n8n).
5. **Cruce CPE con NVD** para reducir falsos positivos del match por texto.
6. **Fuentes Tier 2**: VulnCheck KEV, Exploit-DB/Metasploit/nuclei como señal de weaponización, CSAF/VEX de fabricantes.
7. Sincronizar los workflows de n8n con `n8n/` (exportación saneada).
