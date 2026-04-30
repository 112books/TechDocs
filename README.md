# TechDocs — Sistema de documentació tècnica validada

> **Documentació tècnica validada legalment, lliure de llicències, mantenible pel vostre equip.**

Un sistema de gestió de documentació tècnica estructurada per a pymes industrials i empreses amb necessitat de documentació **validada legalment** (CE, ISO, directiva de maquinària, etc.).

Basat en **Hugo + Markdown + Git**, amb un frontend d'edició senzill i un pipeline de publicació que genera tant portals web com PDFs signats.

---

## Per a què serveix?

- Manuals d'operació, manteniment i seguretat
- Declaracions CE i certificats
- Documentació multiidioma (català, castellà, anglès...)
- Gestió de variants de producte
- Control de versions i historial d'aprovacions
- Publicació en múltiples formats: portal web + PDF signat

## Stack tecnològic

| Component | Tecnologia |
|---|---|
| Contingut | Markdown + front matter YAML |
| Motor | Hugo (generador d'estàtics) |
| Edició | Decap CMS (UI web, sense necessitat de Git) |
| Traduccions | Hugo i18n natiu + Weblate |
| PDF | Pandoc + weasyprint |
| Cerca | Pagefind (cerca estàtica) |
| Versionat | Git |
| Deploy | GitHub Pages |
| CI/CD | GitHub Actions |

## Inici ràpid

### Requisits

- [Hugo](https://gohugo.io/) >= 0.120.0
- Git
- (Opcional) Pandoc per a generació de PDF

### Desenvolupament local

```bash
# Clonar el repositori
git clone https://github.com/112books/TechDocs.git
cd TechDocs

# Executar el servidor de desenvolupament
hugo server -D

# Obrir http://localhost:1313
```

### Generar PDF d'un document

```bash
chmod +x scripts/generate-pdf.sh
./scripts/generate-pdf.sh content/manuals/model-X100/01-seguretat.ca.md
```

### Deploy automàtic

Cada push a `main` activa el workflow de GitHub Actions que construeix i desplega el lloc a GitHub Pages.

## Estructura del projecte

```
TechDocs/
├── content/              # Continguts en Markdown
│   ├── manuals/          # Manuals tècnics per model
│   ├── warnings/         # Avissos de seguretat reutilitzables
│   └── legal/            # Declaracions CE i certificats
├── layouts/              # Templates del tema
│   ├── _default/         # Layouts base
│   ├── shortcodes/       # Shortcodes personalitzats
│   └── partials/         # Parcial del tema
├── static/               # Assets (CSS, JS, imatges)
├── admin/                # Configuració de Decap CMS
├── scripts/              # Scripts d'automatització
├── i18n/                 # Fitxers de traducció
├── config/               # Configuració Hugo
└── .github/workflows/    # CI/CD
```

## Shortcodes disponibles

- `{{< warning type="electric" >}}` — Avís de seguretat amb tipus (electric, crush, chemical, thermal, general)
- `{{< note >}}` — Nota informativa
- `{{< step number="1" >}}` — Pas numerat per a procediments
- `{{< applies-to models="X100,X200" >}}` — Indicador de models aplicables
- `{{< legal-approval >}}` — Bloc d'aprovació legal amb metadades del document
- `{{< revision-history >}}` — Taula d'historial de revisions

## Multiidioma

El sistema suporta nativament múltiples idiomes via Hugo i18n:

```bash
# Construir tots els idiomes
hugo --minify

# Servir amb un idioma específic
hugo server --language ca
hugo server --language es
hugo server --language en
```

## Licència

Aquest projecte és propietat de **LinuxBCN / estategiadelcontenido.com**.

- El codi del tema i la configuració es distribueixen sota llicència MIT.
- Cada client és propietari del seu contingut i configuració específica.
- No hi ha llicències anuals: el client controla el seu sistema.

---

**Projecte TechDocs** by [LinuxBCN](https://linuxbcn.com) / [estategiadelcontenido.com](https://estategiadelcontenido.com)
