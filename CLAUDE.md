# CLAUDE.md — TechDocs Development Guide

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**TechDocs** is a technical documentation management system for industrial SMEs requiring legally validated documentation (CE marking, ISO compliance, Machinery Directive). Built with Hugo + Markdown + Git, it generates both web portals and signed PDFs from the same content source.

**Key stakeholders:** Joan Linux (LinuxBCN.com), Carlos Campo (estategiadelcontenido.com)

**Repository:** https://github.com/112books/TechDocs  
**Live demo:** https://112books.github.io/TechDocs/  
**Password:** LinuxBCN2026

---

## Architecture

### Core Stack

| Component | Technology | Version |
|---|---|---|
| Content | Markdown + YAML front matter | — |
| Engine | Hugo static site generator | >= 0.120.0 |
| CMS | Decap CMS (web-based) | v3 (CDN) |
| i18n | Hugo native multilingual | ca, es, en |
| PDF | Pandoc + weasyprint | — |
| Search | Pagefind (static) | — |
| Version control | Git | — |
| Deploy | GitHub Pages via GitHub Actions | — |

### Project Structure

```
TechDocs/
├── .github/workflows/hugo.yml    # CI/CD: build + deploy to Pages
├── admin/                        # Decap CMS (web editor)
│   ├── index.html                # CMS entry point
│   └── config.yml                # CMS collections & fields
├── archetypes/
│   └── manual.md                 # Default front matter for new content
├── config/
│   └── pandoc-metadata.yaml      # PDF generation metadata & LaTeX headers
├── content/
│   ├── manuals/                  # Technical manuals by product model
│   │   ├── model-X100/           # Example model
│   │   │   ├── _index.{lang}.md  # Manual index per language
│   │   │   └── {weight}-{name}.{lang}.md  # Chapters
│   │   └── model-X200/
│   └── warnings/                 # Reusable safety warnings
│   └── legal/                    # CE declarations, certificates
│       └── declarations/
├── i18n/
│   ├── ca.yaml                   # Catalan translations
│   ├── es.yaml                   # Spanish translations
│   └── en.yaml                   # English translations
├── layouts/
│   ├── _default/
│   │   ├── baseof.html           # Master layout (includes password gate)
│   │   ├── home.html             # Homepage template
│   │   ├── list.html             # Section listing template
│   │   └── single.html           # Single content page template
│   ├── partials/
│   │   ├── legal-approval-block.html  # Approval metadata display
│   │   └── model-selector.html        # Product model filter
│   └── shortcodes/
│       ├── warning.html          # Colored warning/callout boxes
│       ├── note.html             # Info note boxes
│       ├── step.html             # Numbered procedure steps
│       ├── applies-to.html       # Model applicability badges
│       ├── legal-approval.html   # Legal approval record block
│       └── revision-history.html # Document revision table
├── scripts/
│   └── generate-pdf.sh           # Pandoc PDF generation script
├── static/
│   ├── css/main.css              # Theme styles (includes print/A4)
│   ├── js/main.js                # Client-side JS (model filter, smooth scroll)
│   └── images/                   # Static images
└── hugo.toml                     # Hugo configuration
```

---

## Development Commands

```bash
# Dev server with drafts visible
hugo server -D

# Dev server for specific language
hugo server -D --language ca

# Production build (all languages, no drafts)
hugo --minify

# Single language build
hugo --minify --language ca

# Generate PDF from a content file
./scripts/generate-pdf.sh content/manuals/model-X100/01-seguretat.ca.md

# Check build without deploying
hugo --minify --baseURL / && echo "Build OK"
```

---

## Code Conventions

### Front Matter — REQUIRED Fields

Every content file MUST have these fields:

```yaml
---
title: "Display Title"
date: YYYY-MM-DD
type: manual              # manual | warning | legal
applies_to: ["model1"]    # array of model codes; empty = all models
not_applies_to: []        # array of excluded models
revision: "X.Y"           # semantic version string
approved_by: "Full Name"  # approver name
approved_date: "YYYY-MM-DD"
legal_review: false       # true = legally reviewed
draft: false              # true = only visible in dev mode
weight: 1                 # ordering within a section (lower = first)
---
```

### i18n Keys

All user-facing text MUST use `{{ i18n "key" }}`. Available keys in `i18n/*.yaml`:

- `site_title`, `site_tagline`
- `manuals`, `warnings`, `legal`
- `revision`, `approved_by`, `approved_date`, `legal_review`
- `applies_to`, `not_applies_to`
- `warning`, `note`, `step`
- `table_of_contents`, `previous`, `next`
- `language`, `back_to_home`
- `model_selector`, `all_models`
- `document_history`, `version`
- `generated_on`, `powered_by`

### Shortcodes

```
{{< warning type="electric" >}}content{{< /warning >}}
  Types: electric, crush, chemical, thermal, general

{{< note >}}content{{< /note >}}

{{< step number="1" >}}content{{< /step >}}

{{< applies-to models="X100,X200" >}}

{{< legal-approval >}}

{{< revision-history >}}  # Uses .Params.revision_history array
```

### CSS

- **Design tokens** in `:root` custom properties
- **Color palette:**
  - Navy `#1B2A4A` — headers, primary backgrounds
  - Blue `#2563EB` — links, accents, buttons
  - Green `#16A34A` — success, applies-to badges
  - Amber `#D97706` — warnings, medium alerts
  - Red `#DC2626` — danger, critical alerts
- **Typography:** System font stack (Apple, Segoe, Roboto, Helvetica, Arial)
- **Print styles:** `@page { size: A4; margin: 2cm }` included in `main.css`
- **Breakpoint:** 48rem for mobile-responsive
- **Naming:** BEM-like with `.techdoc-` prefix

### Content File Naming

```
{weight}-{slug}.{language_code}.md
```

Examples: `01-seguretat.ca.md`, `02-installacio.ca.md`, `03-operacio.ca.md`

---

## Password Gate

The site is protected by a client-side password gate (inline in `baseof.html`):

- **Password:** `LinuxBCN2026`
- **Mechanism:** Session-based (`sessionStorage`) — persists per browser session
- **Implementation:** All CSS/JS inline in `baseof.html` — zero external file dependencies
- **Limitation:** Not cryptographically secure. For production with sensitive content, use server-side auth (Cloudflare Pages Access, Netlify basic auth, or custom proxy).

---

## GitHub Actions CI/CD

Workflow: `.github/workflows/hugo.yml`

1. **Triggers:** push or PR to `main`
2. **Build:** Hugo `--minify` with `baseURL` from `actions/configure-pages`
3. **Deploy:** GitHub Pages (only on push to `main`)

**Critical:** The `actions/configure-pages` step MUST be present and have `id: pages`. Without it, `baseURL` falls back to `/` and all asset paths break.

```yaml
- name: Setup Pages
  id: pages
  uses: actions/configure-pages@v5
```

---

## Content Rules

1. **Never commit content with `draft: true` to `main`** — it won't appear in production builds
2. **Always add i18n keys** for new UI text — don't hardcode strings
3. **Every page needs approval metadata** — this is the core value proposition
4. **Use shortcodes for warnings/steps** — don't use raw HTML for these elements
5. **Model filtering** is handled via `applies_to`/`not_applies_to` front matter — the `model-selector` partial and JS handle frontend filtering

---

## Testing Checklist

Before pushing:

- [ ] `hugo --minify` builds without errors
- [ ] All content files have required front matter fields
- [ ] i18n keys exist in all 3 language files (ca, es, en)
- [ ] Shortcodes use inline styles (no external CSS refs)
- [ ] No `draft: true` on content meant for production
- [ ] Password gate inline JS is intact in `baseof.html`

---

## Compliance Requirements (CE / ISO 9001)

The system must demonstrate:

1. **Version traceability:** Git history + front matter `revision` field
2. **Approval records:** `approved_by`, `approved_date`, `legal_review` on every document
3. **Multi-language:** Manuals available in the language of the country of use
4. **10-year retention:** Git provides this natively; backups recommended
5. **Change history:** Git log + `revision-history` shortcode for visual display

---

## Roadmap

### v1.0 (MVP) — In Progress
- [x] Hugo base structure
- [x] Theme with print/A4 styles
- [x] Essential shortcodes
- [x] Multi-language (ca, es, en)
- [x] Decap CMS configured
- [x] GitHub Actions deploy
- [x] Password gate for demo
- [ ] Pagefind search integration
- [ ] Complete demo manual (all chapters)

### v1.5 (Legal value-add)
- [ ] Approval history registry (persistent)
- [ ] Digitally signed PDFs (GPG/qualified cert)
- [ ] Auto-incrementing revision via CI/CD
- [ ] Structured XML export (DITA Light)
- [ ] Translation status dashboard

### v2.0 (Platform)
- [ ] Client portal with authentication
- [ ] Advanced search by model/category/language
- [ ] Weblate integration
- [ ] Email/Telegram notifications on doc changes
- [ ] PDF/A export for legal archiving
