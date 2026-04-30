# CLAUDE.md — TechDocs Development Guide

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**TechDocs** is a technical documentation management system for industrial SMEs requiring legally validated documentation (CE marking, ISO compliance, Machinery Directive). Built with Hugo + Markdown + Git, it generates both web portals and signed PDFs from the same content source.

**Key stakeholders:** Joan Linux (LinuxBCN.com), Carlos Campo (estategiadelcontenido.com)

## Architecture

### Core Stack
- **Content**: Markdown with YAML front matter
- **Engine**: Hugo static site generator (>= 0.120.0)
- **CMS**: Decap CMS (web-based editing, no Git CLI needed)
- **i18n**: Hugo native multilingual + Weblate (self-hosted)
- **PDF**: Pandoc + weasyprint
- **Search**: Pagefind (static search)
- **Deploy**: GitHub Pages via GitHub Actions

### Content Structure
- `content/manuals/` — Technical manuals organized by product model
- `content/warnings/` — Reusable safety warning modules
- `content/legal/` — CE declarations, certificates, compliance docs

### Key Features
- **Product variants**: Front matter `applies_to`/`not_applies_to` arrays filter content per model
- **Legal approval tracking**: `approved_by`, `approved_date`, `legal_review`, `revision` in front matter
- **Multi-language**: Full i18n support (ca, es, en) via Hugo's language system
- **Shortcodes**: `warning`, `note`, `step`, `applies-to`, `legal-approval`, `revision-history`

## Common Commands

### Development
```bash
# Start dev server with drafts
hugo server -D

# Start dev server for specific language
hugo server -D --language ca

# Build production site (all languages)
hugo --minify

# Build single language
hugo --minify --language ca
```

### PDF Generation
```bash
chmod +x scripts/generate-pdf.sh
./scripts/generate-pdf.sh content/manuals/model-X100/01-seguretat.ca.md
```

### Content Management
- New manual: `hugo new content/manuals/model-NEW/_index.ca.md`
- Edit via Decap CMS at `/admin/` (when deployed)
- All content supports YAML front matter with approval metadata

## Code Conventions

### Front Matter Standard
Every content file MUST have:
```yaml
title: "..."
date: YYYY-MM-DD
type: manual  # or warning, legal
applies_to: ["model1", "model2"]  # empty array = all models
revision: "X.Y"
approved_by: "Name"
approved_date: "YYYY-MM-DD"
legal_review: true/false
draft: true/false
weight: N  # for ordering within a manual
```

### Shortcodes
- Always use inline styles for visual consistency (no external CSS dependencies in shortcodes)
- Use i18n keys via `{{ i18n "key" }}` for all user-facing text
- Keep HTML semantic and accessible

### CSS
- Design tokens in `:root` custom properties
- Color palette: navy (#1B2A4A), blue (#2563EB), green (#16A34A), amber (#D97706), red (#DC2626)
- Print styles included for A4 output
- Mobile-first responsive breakpoints at 48rem

### Naming
- Content files: `{weight}-{name}.{lang}.md` (e.g., `01-seguretat.ca.md`)
- Shortcodes: kebab-case HTML files in `layouts/shortcodes/`
- Partials: kebab-case in `layouts/partials/`
- CSS: BEM-like naming with `.techdoc-` prefix

## Testing & Validation

### Hugo Build Check
```bash
hugo --minify --baseURL /  # Should complete without errors
```

### PDF Generation Test
```bash
./scripts/generate-pdf.sh content/manuals/model-X100/01-seguretat.ca.md test.pdf
```

### Content Validation
- All front matter fields present and correctly typed
- i18n keys exist in all language files (i18n/ca.yaml, i18n/es.yaml, i18n/en.yaml)
- Shortcodes render without errors

## Deployment

### GitHub Pages
Automated via `.github/workflows/hugo.yml`:
- Trigger: push to `main`
- Builds with latest Hugo
- Deploys to GitHub Pages environment
- Requires Pages enabled in repo settings

### Manual Deploy
```bash
hugo --minify --baseURL https://your-domain.com/
# Upload public/ directory to hosting
```

## Compliance Requirements

For CE marking compliance, the system must demonstrate:
1. **Version traceability**: Git history + front matter revision tracking
2. **Approval records**: `approved_by`, `approved_date`, `legal_review` on every document
3. **Multi-language**: Manuals in the language of the country of use
4. **10-year retention**: Git + backups provide this natively
5. **Change history**: Git log + revision-history shortcode

## Future Development (Roadmap)

### v1.0 (MVP) — Current
- Hugo base structure ✓
- Theme with print styles ✓
- Essential shortcodes ✓
- PDF via Pandoc ✓
- Multi-language (3 langs) ✓
- Decap CMS ✓
- GitHub Actions deploy ✓

### v1.5 (Legal value-add)
- Approval history registry
- Digitally signed PDFs (GPG/qualified certificate)
- Auto-incrementing revision numbers via CI/CD
- Structured XML export (DITA Light compatible)
- Translation status dashboard

### v2.0 (Platform)
- Client portal with authentication
- Advanced search by model/category/language
- Weblate integration for collaborative translations
- Email/Telegram notifications on document changes
- PDF/A export for legal archiving
