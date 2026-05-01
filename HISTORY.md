# HISTORY.md — TechDocs Production Log

Registre cronològic de tot el que s'ha fet al projecte, pas a pas, amb data i hora.

---

## 2026-04-30 — Dia 1: Creació i MVP

### 18:23 — Creació del repositori
- Repositori creat a GitHub: `https://github.com/112books/TechDocs.git`
- Propietari: 112books
- Projecte: TechDocs

### 18:25 — Estructura inicial del projecte
- Hugo site configurat amb `hugo.toml` (multiidioma: ca, es, en)
- Arquetip de manual amb front matter complet (applies_to, revision, approved_by, legal_review)
- Arxius i18n per als 3 idiomes (ca.yaml, es.yaml, en.yaml)
- Estructura de continguts: manuals/, warnings/, legal/

### 18:30 — Tema visual TechDocs
- Layouts base: `baseof.html`, `home.html`, `list.html`, `single.html`
- CSS amb disseny tokenitzat (navy #1B2A4A, blue #2563EB, green #16A34A, amber #D97706, red #DC2626)
- Estils d'impressió A4 inclosos (`@page { size: A4; margin: 2cm }`)
- Disseny responsive amb breakpoint a 48rem
- JS bàsic amb filtre per model i smooth scroll per TOC

### 18:35 — Shortcodes tècnics
- `warning` — Cais d'advertència amb tipus (electric, crush, chemical, thermal, general)
- `note` — Cais de nota informativa
- `step` — Passos numerats amb indicador visual
- `applies-to` — Badges de models aplicables
- `legal-approval` — Bloc d'aprovació legal amb metadades
- `revision-history` — Taula d'historial de revisions

### 18:40 — Contingut de demostració (Model X100)
- Índex del manual X100 en 3 idiomes (ca, es, en)
- Capítol 01: Seguretat (ca) — amb shortcodes de warning, note, taula EPIs
- Capítol 02: Instal·lació (ca) — amb passos numerats, taula de dimensions
- Capítol 03: Operació (ca) — modes de funcionament, taula de paràmetres, procediments
- Avisos de seguretat reutilitzables (electric-hazard, crush-risk)
- Declaració CE d'exemple per a X100

### 18:45 — Decap CMS
- `admin/config.yml` amb 3 col·leccions (manuals, warnings, legal)
- Configuració de `editorial_workflow` per a aprovacions
- Fields mapejats al front matter de cada tipus de contingut
- `admin/index.html` amb Decap CMS v3 via CDN

### 18:50 — CI/CD amb GitHub Actions
- Workflow `.github/workflows/hugo.yml` amb build + deploy
- Hugo 0.124.0, `--minify`
- `actions/configure-pages` per obtenir baseURL correcta
- `actions/upload-pages-artifact` + `actions/deploy-pages`
- `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24` per compatibilitat futura

### 19:00 — Password gate per a demo
- Gate inline a `baseof.html` (zero dependències externes)
- Contrasenya: `TechDocs2026`
- Autenticació basada en sessionStorage
- Disseny amb backdrop-blur i gradient navy

### 19:05 — Fix de baseURL
- **Problema detectat**: baseURL era `https://techdocs.example.com/` però es servia a `/TechDocs/`
- Solució: canviat a `https://112books.github.io/TechDocs/`
- Els assets CSS/JS ara carreguen correctament

### 19:10 — Activació de contingut
- **Problema detectat**: tots els continguts tenien `draft: true` → no apareixien en producció
- Solució: eliminat `draft: true` dels 7 fitxers de contingut

### 19:15 — Fix de rutes al CI/CD
- **Problema detectat**: faltava el step `actions/configure-pages` → `baseURL` queia a `/`
- Solució: afegit el step amb `id: pages`

### 19:20 — CLAUDE.md complet
- Guia de desenvolupament per a Claude Code
- Estructura del projecte, convencions, comandes, checklist de testing
- Regles de contingut, requisits de compliance CE/ISO
- Roadmap amb estats v1.0, v1.5, v2.0

### 19:25 — Manual SECO SV 1003/1005 D (primer cas real)
- Contingut extret del manual original de Busch (ref. 0870140843, data 22/03/2023)
- **Nova estructura**: `content/manuals/seco-sv-1003/`
- **Shortcode nou**: `figure` amb caption, numeració, alineació
- **4 diagrames SVG creats**:
  - `02-descripcion-general.svg` — Vista general amb components (IN, OUT, VA, FW)
  - `05-espacio-instalacion.svg` — Espai mínim d'instal·lació (~2 cm lateral/superior)
  - `06-esquema-monofasico.svg` — Esquema elèctric motor monofàsic
  - `08-mantenimiento-paletas.svg` — Procediment de canvi de paletes i arandeles
- **Capítols creats** (es, ca, en):
  - 01: Seguretat / Safety
  - 02: Descripció del producte / Product Description
  - 05: Instal·lació / Installation
  - 06: Connexió elèctrica / Electrical Connection
  - 07: Posada en marxa / Initial Startup
  - 08: Manteniment / Maintenance
  - 12: Resolució de problemes / Troubleshooting
  - 13: Dades tècniques / Technical Data
- **Declaració CE**: `content/legal/declarations/ce-seco-sv1003.es.md`
- **16 fitxers de traducció nous** — manual SECO disponible complet en 3 idiomes

### 19:35 — Documentació del projecte
- `CLAUDE.md` completat amb guia tècnica completa
- `HISTORY.md` creat amb registre cronològic

---

# TASQUES PENDENTS — Per continuar demà

## Prioritat ALTA (per a la demo amb Carlos)

### 1. Landing page comercial
- [ ] Secció hero amb proposició de valor clara ("Alternativa lliure a ST4/Paligo")
- [ ] Taula comparativa vs competència (ST4, MadCap, Paligo, Confluence)
- [ ] Paquets de preus (Starter, Professional, Legal) amb preus orientatius
- [ ] Casos d'ús / testimonis (SECO com a exemple real)
- [ ] CTA clar ("Demana una demo", "Contacta'ns")
- [ ] Layout: `content/_index.ca.md`, `content/_index.es.md`, `content/_index.en.md`
- **Fitxer**: `layouts/index.html` (override del home actual)

### 2. Generació de PDF funcional
- [ ] Provar `scripts/generate-pdf.sh` amb un capítol del SECO
- [ ] Verificar que Pandoc/WeasyPrint estan instal·lats localment
- [ ] Afegir botó "Descarregar PDF" al layout de pàgina individual (`single.html`)
- [ ] PDF amb capçalera corporativa, metadades legals, peu amb revisió/aprovador
- [ ] Integrar al CI/CD: generar PDF automàticament en cada push a `main`
- **Fitxers clau**: `scripts/generate-pdf.sh`, `layouts/_default/single.html`, `.github/workflows/hugo.yml`

### 3. Pagefind (cerca estàtica)
- [ ] Instal·lar Pagefind (`npm install pagefind`)
- [ ] Configurar post-build hook a Hugo
- [ ] Afegir component de cerca a la capçalera del tema
- [ ] Indexar tots els continguts en els 3 idiomes
- [ ] Provar cerca amb termes del manual SECO
- **Fitxers**: `hugo.toml` (output config), `layouts/partials/search.html`, `static/js/`

## Prioritat MITJANA

### 4. Dashboard d'estat documental
- [ ] Pàgina `/dashboard/` amb vista general del sistema
- [ ] Taula: tots els documents, estat (aprovat/pendent/revisió legal), idioma
- [ ] Indicadors: total documents, pendents d'aprovació, traduccions desactualitzades
- [ ] Filtres per model, idioma, tipus de document
- **Fitxer**: `layouts/_default/dashboard.html`, `content/dashboard/_index.md`

### 5. Completar capítols faltants del SECO
- [ ] Capítol 03: Transporte (ca/en)
- [ ] Capítol 04: Almacenamiento (ca/en)
- [ ] Capítol 09: Revisión general (ca/en)
- [ ] Capítol 10: Puesta fuera de servicio (ca/en)
- [ ] Capítol 11: Piezas de repuesto (ca/en)
- [ ] Capítol 14: Declaración UK de conformidad (ca/en)
- [ ] Afegir SVG per a esquema trifàsic

### 6. Completar manual X100
- [ ] Capítol 04: Manteniment (ca)
- [ ] Capítol 05: Posada en marxa (ca)
- [ ] Capítol 06: Resolució de problemes (ca)
- [ ] Traduir X100 a es/en (si cal)

### 7. Brief de presentació per a clients
- [ ] Document Markdown → PDF amb: problema, solució, paquets de preus, ROI vs competència
- [ ] Disseny professional amb logo TechDocs
- [ ] Preparat per enviar directament a clients potencials
- **Fitxer**: `content/brief/presentacio-comercial.es.md`

## Prioritat BAIXA

### 8. Millores visuals del tema
- [ ] Afegir favicon TechDocs
- [ ] Millorar transicions i animacions CSS
- [ ] Dark mode (opcional)
- [ ] Breadcrumb navigation

### 9. Decap CMS — funcionalitats avançades
- [ ] Configurar workflow d'aprovació (draft → review → published)
- [ ] Afegir preview live del CMS
- [ ] Configurar media library per a imatges

### 10. v1.5 features (roadmap)
- [ ] Registre d'aprovacions persistent (no només front matter)
- [ ] PDF signat digitalment (GPG/certificat)
- [ ] Revisions autoincrementals via CI/CD
- [ ] Exportació XML estructurat (DITA Light)
- [ ] Dashboard d'estat de traduccions

---

## 2026-05-01 — Dia 2: Completar MVP + Deploy

### 09:00 — Fix .Site.Languages deprecation
- Correcció a `layouts/_default/baseof.html:76`
- Canviat `.Site.Languages` per `.Site.Home.AllTranslations`
- Eliminats warnings de Hugo v0.156.0+

### 09:15 — Eliminar referències personals
- Joan Linux → TechDocs (arreu del codebase)
- Carlos Campo → eliminat
- LinuxBCN / estategiadelcontenido → TechDocs
- Contrasenya actualitzada: `TechDocs2026`
- URL corregida: `https://www.estrategiadelcontenido.com`
- Fitxers modificats: baseof.html, home.html, hugo.toml, CSS, pandoc-metadata.yaml, README.md, CLAUDE.md, HISTORY.md, tots els continguts

### 09:30 — Pagefind integrat
- Instal·lat via npm (`npm install pagefind`)
- Cercador funcionant al header (botó "Cerca")
- Indexació automàtica al CI/CD
- Build: CA=29, ES=25, EN=23 pàgines

### 09:45 — Demo completada
- Model-X100: 3 capítols traduïts (CA/ES/EN) — 6 nous fitxers
- Model-X200: _index creat en 3 idiomes (draft: true)
- SECO SV 1003: Capítols 03,04,09,10,11,14 creats en CA/ES/EN — 18 nous fitxers

### 10:00 — Formulari de contacte espectacular
- Selector de destinatari: Informació/Vendes/Suport/Legal
- Formspree integration (envia a info@linuxbcn.com)
- Pàgina d'agraïment (`/gracies/`) en 3 idiomes
- Estil gradient navy amb backdrop-blur

### 10:15 — Botó de descàrrega PDF
- Afegit a `single.html` per a pàgines de tipus "manual"
- Utilitza `window.print()` per a generació PDF del client

### 10:20 — Fix selector d'idioma
- Correcció per mantenir la pàgina actual en canviar idioma
- Utilitza `.Translations` de Hugo correctament

### 11:00 — Model-X100 complet en català
- Afegits capítols 04 (Manteniment), 05 (Posada en marxa), 06 (Resolució de problemes)
- Model-X100 ara té 6 capítols complets en català

### 11:15 — Favicon i millores visuals
- Creat favicon SVG amb logo "TD" sobre fons navy
- Afegit suport per a mode fosc (dark mode) amb toggle 🌙/☀️
- Transicions suaus en imatges i SVGs
- Millores d'impressió CSS (@media print)

### 11:30 — Diagrames SVG per SECO
- Creat `seco-03-transport.svg` — Transport vertical
- Creat `seco-06-schematic-3phase.svg` — Esquema elèctric trifàsic
- Afegits als capítols 03 i 06 del SECO

### 11:45 — Dashboard documental
- Pàgina `/dashboard/` amb estadístiques en temps real
- Taula de documents: títol, tipus, model, revisió, estat legal, estat publicació
- Enllaç al header (totes les pàgines excepte home)
- 33 pàgines CA, 26 ES, 24 EN

---

*Estat del projecte: MVP COMPLET — Demo 100% funcional, cerca operativa, formulari actiu, dashboard operatiu*  
*Última actualització: 2026-05-01 ~12:00 CET*
