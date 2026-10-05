# vuln-pulse

Pipeline de inteligencia de vulnerabilidades con fuentes abiertas: CISA KEV, CVE List V5 con la clasificación SSVC de CISA, y FIRST EPSS.

Todos los días a las 07:20 (hora de Chile, horario de verano), GitHub Actions hace lo siguiente:

1. Genera el reporte de los últimos 7 días en `data/latest/weekly_report.json` y `.md`.
2. Guarda una foto diaria pequeña en `data/history/AAAA-MM-DD.json`, para calcular tendencias de más de 30 días.
3. Construye el tablero de 30 días y lo publica en GitHub Pages.

n8n Cloud consume estos archivos para alertar y redactar resúmenes.

```
GitHub Actions (diario) ──► data/latest/*.json ──► n8n: resumen semanal por rol (LLM)
        │                   data/history/*.json
        └──► GitHub Pages: tablero
n8n (cada 2 h) ──► KEV desde cisagov/kev-data ──► alerta si afecta tus tecnologías
```

## Estructura

| Ruta | Contenido |
|---|---|
| `src/collector.py` | Recolector: KEV, CVE List V5 + SSVC y EPSS → reporte JSON/MD |
| `src/build_dashboard_data.py` | Datos de 30 días + plantilla → `site/index.html` |
| `src/dashboard_template.html` | Plantilla del tablero (perfiles: oficial, gerente TI, CISO) |
| `src/snapshot.py` | Foto diaria para el historial |
| `config/sources.json` | Catálogo de fuentes |
| `docs/SPEC.md` | Especificación: métricas por rol, prioridades y guardrails |
| `n8n/01_kev_alerta.json` | Workflow de n8n: alerta de KEV nuevas |
| `data/` | Lo escribe el workflow; no editar a mano |

No requiere dependencias: solo usa la librería estándar de Python 3.9 o superior.

## Puesta en marcha (cuenta gratuita de GitHub)

1. **Crea el repositorio** en GitHub, por ejemplo `vuln-pulse`.
   - **Público**: GitHub Pages en el plan gratuito requiere que el repo sea público. Todo lo que publica son datos abiertos.
   - **Privado**: si lo prefieres, el tablero no se puede publicar con Pages, pero el resto funciona. Actions tiene 2.000 minutos al mes gratis y cada corrida usa unos 3.
2. **Sube el código:**
   ```bash
   git remote add origin https://github.com/<tu-usuario>/vuln-pulse.git
   git push -u origin main
   ```
3. **Activa Pages:** *Settings → Pages → Build and deployment → Source: **GitHub Actions***.
4. **Opcional:** por defecto el tablero parte con una lista de ejemplo (top de fabricantes por KEV, ver `EXAMPLE_WATCHLIST` en `src/build_dashboard_data.py`). Para cambiarla, en *Settings → Secrets and variables → Actions → Variables* crea `WATCHLIST_DEFAULT` con tus tecnologías, por ejemplo `Microsoft, Cisco, Fortinet`. Si el repo es público, esa lista queda visible en el tablero, así que no pongas tu inventario real. Cada persona puede escribir la suya en el tablero y queda guardada solo en su navegador.
5. **Primera corrida:** en *Actions → Pulso diario de vulnerabilidades → Run workflow*. Tarda 3–4 minutos. El tablero queda en `https://<tu-usuario>.github.io/vuln-pulse/`.

## URLs para n8n

```
https://raw.githubusercontent.com/<tu-usuario>/vuln-pulse/main/data/latest/weekly_report.json
https://raw.githubusercontent.com/<tu-usuario>/vuln-pulse/main/data/history/AAAA-MM-DD.json
```

Si el repo es privado, n8n necesita un token de GitHub de solo lectura (fine-grained, permiso *Contents: Read*) en el encabezado `Authorization: Bearer …`.

## Ejecutar en local

```bash
python3 src/collector.py --days 7 --out data/latest
python3 src/build_dashboard_data.py --days 30 --template src/dashboard_template.html \
        --out site/index.html --data-out site/dashboard_data.json
```

## Notas

- **KEV** se descarga desde el repositorio oficial de CISA `cisagov/kev-data`, que CISA ofrece para consumo programático. Si falla, usa cisa.gov como respaldo.
- **EPSS** se descarga de `api.first.org`. Si no responde, el reporte lo indica en `sources_status` y el tablero muestra la fuente en rojo.
- **La clasificación SSVC** la asigna CISA con 1–3 días de retraso. Los últimos días siempre se ven incompletos.
- **GitHub pausa los workflows programados** en repositorios sin actividad por 60 días. Los commits diarios de datos mantienen el repo activo.
