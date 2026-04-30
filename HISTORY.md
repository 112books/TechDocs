# HISTORY.md — TechDocs Production Log

Registro cronológico de todo lo que se ha hecho en el proyecto, paso a paso, con fecha y hora.

---

## 2026-04-30

### 18:23 — Creación del repositorio
- Repositorio creado en GitHub: `https://github.com/112books/TechDocs.git`
- Propietario: 112books (Joan Linux)
- Proyecto: TechDocs by LinuxBCN / estategiadelcontenido.com

### 18:25 — Estructura inicial del proyecto
- Hugo site configurado con `hugo.toml` (multiidioma: ca, es, en)
- Arquetipo de manual con front matter completo (applies_to, revision, approved_by, legal_review)
- Archivos i18n para los 3 idiomas (ca.yaml, es.yaml, en.yaml)
- Estructura de contenidos: manuals/, warnings/, legal/

### 18:30 — Tema visual TechDocs
- Layouts base: `baseof.html`, `home.html`, `list.html`, `single.html`
- CSS con diseño tokenizado (navy #1B2A4A, blue #2563EB, green #16A34A, amber #D97706, red #DC2626)
- Estilos de impresión A4 incluidos (`@page { size: A4; margin: 2cm }`)
- Diseño responsive con breakpoint en 48rem
- JS básico con filtro por modelo y smooth scroll para TOC

### 18:35 — Shortcodes técnicos
- `warning` — Cajas de advertencia con tipos (electric, crush, chemical, thermal, general)
- `note` — Cajas de nota informativa
- `step` — Pasos numerados con indicador visual
- `applies-to` — Badges de modelos aplicables
- `legal-approval` — Bloque de aprobación legal con metadatas
- `revision-history` — Tabla de historial de revisiones

### 18:40 — Contenido de demostración (Modelo X100)
- Índice del manual X100 en 3 idiomas (ca, es, en)
- Capítulo 01: Seguridad (ca) — con shortcodes de warning, note, tabla EPIs
- Capítulo 02: Instalación (ca) — con pasos numerados, tabla de dimensiones
- Capítulo 03: Operación (ca) — modos de funcionamiento, tabla de parámetros, procedimientos
- Avisos de seguridad reutilizables (electric-hazard, crush-risk)
- Declaración CE de ejemplo para X100

### 18:45 — Decap CMS
- `admin/config.yml` con 3 colecciones (manuals, warnings, legal)
- Configuración de `editorial_workflow` para aprobaciones
- Fields mapeados al front matter de cada tipo de contenido
- `admin/index.html` con Decap CMS v3 via CDN

### 18:50 — CI/CD con GitHub Actions
- Workflow `.github/workflows/hugo.yml` con build + deploy
- Hugo 0.124.0, `--minify`
- `actions/configure-pages` para obtener baseURL correcta
- `actions/upload-pages-artifact` + `actions/deploy-pages`
- `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` para compatibilidad futura

### 19:00 — Password gate para demo
- Gate inline en `baseof.html` (zero dependencias externas)
- Contraseña: `LinuxBCN2026`
- Autenticación basada en sessionStorage
- Diseño con backdrop-blur y gradiente navy

### 19:05 — Fix de baseURL
- **Problema detectado**: baseURL era `https://techdocs.linuxbcn.com/` pero se servía en `/TechDocs/`
- Solución: cambiado a `https://112books.github.io/TechDocs/`
- Los assets CSS/JS ahora cargan correctamente

### 19:10 — Activación de contenido
- **Problema detectado**: todos los contenidos tenían `draft: true` → no aparecían en producción
- Solución: eliminado `draft: true` de los 7 ficheros de contenido

### 19:15 — Fix de rutas en CI/CD
- **Problema detectado**: faltaba el step `actions/configure-pages` → `baseURL` caía a `/`
- Solución: añadido el step con `id: pages`

### 19:20 — CLAUDE.md completo
- Guía de desarrollo para Claude Code
- Estructura del proyecto, convenciones, comandos, checklist de testing
- Reglas de contenido, requisitos de compliance CE/ISO
- Roadmap con estados v1.0, v1.5, v2.0

### 19:25 — Manual SECO SV 1003/1005 D (primer caso real)
- Contenido extraído del manual original de Busch (ref. 0870140843, fecha 22/03/2023)
- **Nueva estructura**: `content/manuals/seco-sv-1003/`
- **Shortcode nuevo**: `figure` con caption, numeración, alineación
- **4 diagramas SVG creados**:
  - `02-descripcion-general.svg` — Vista general con componentes (IN, OUT, VA, FW)
  - `05-espacio-instalacion.svg` — Espacio mínimo de instalación (~2 cm lateral/superior)
  - **`06-esquema-monofasico.svg`** — Esquema eléctrico motor monofásico
  - `08-mantenimiento-paletas.svg` — Procedimiento de cambio de paletas y arandelas
- **Capítulos creados**:
  - 01: Seguridad (tipos de advertencia: PELIGRO, ADVERTENCIA, PRECAUCIÓN, AVISO, NOTA)
  - 02: Descripción del producto (principio de funcionamiento, uso apropiado, accesorios)
  - 05: Instalación (condiciones, conductos, conexiones G1/4 y G3/8)
  - 06: Conexión eléctrica (monofásico, trifásico, sentido de rotación)
  - 07: Puesta en marcha inicial (procedimiento paso a paso)
  - 08: Mantenimiento (plan, cambio de paletas, piezas de repuesto con referencias Busch)
  - 12: Resolución de problemas (tabla completa de problemas/causas/soluciones)
  - 13: Datos técnicos (especificaciones SV 1003 D y SV 1005 D)
- **Declaración CE**: `content/legal/declarations/ce-seco-sv1003.es.md` con directivas y normas armonizadas

---

*Última actualización: 2026-04-30 19:30 CET*
