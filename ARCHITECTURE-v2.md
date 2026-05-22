# TechDocs v2 — Arquitectura de Blocs Modulars

## Filosofia

**Cada unitat de coneixement és un bloc atòmic independent** que es pot:
- Identificar únicament (ID codificat)
- Traduir (referència al bloc original)
- Reaprofitar (composició en múltiples documents)
- Exportar (PDF, HTML, JSON, XML)
- Etiquetar (tags semàntics per cerca i filtratge)

## Esquema de Codificació

```
[TIPUS]-[CATEGORIA]-[SEQÜÈNCIA]
```

### Tipus de Bloc

| Codi | Tipus | Descripció |
|---|---|---|
| `WARN` | Advertència | Avisos de seguretat, perills, precaucions |
| `PROC` | Procediment | Passos seqüencials (instal·lació, manteniment, operació) |
| `SPEC` | Especificació | Dades tècniques, paràmetres, valors |
| `INFO` | Informació | Descripcions, explicacions, context |
| `LEGAL` | Legal | Declaracions CE, certificats, normes |
| `DEF` | Definició | Glossari, termes tècnics |
| `REF` | Referència | Taules, diagrames, esquemes |

### Categories

| Codi | Categoria |
|---|---|
| `ELEC` | Elèctric |
| `MECH` | Mecànic |
| `THERM` | Tèrmic |
| `CHEM` | Químic |
| `SAFETY` | Seguretat general |
| `INSTALL` | Instal·lació |
| `MAINT` | Manteniment |
| `OPER` | Operació |
| `PERF` | Rendiment / Especificacions |
| `TROUBLE` | Resolució de problemes |
| `GENERAL` | General / Multiús |

### Exemples d'IDs

```
WARN-ELEC-001     # Primera advertència elèctrica
WARN-CRUSH-001    # Primera advertència d'aixafament
PROC-INSTALL-001  # Primer procediment d'instal·lació
PROC-MAINT-001    # Primer procediment de manteniment
SPEC-PERF-001     # Primera especificació de rendiment
LEGAL-CE-001      # Primera declaració CE
```

## Frontmatter Estandarditzat

```yaml
---
# Identificació
block_id: "WARN-ELEC-001"
block_type: "warning"
block_category: "electrical"
title: "Perill de descàrrega elèctrica"

# Versió i estat
version: "1.0"
status: "approved"  # draft | review | approved | deprecated
created: "2026-04-30"
modified: "2026-04-30"

# Aplicabilitat
applies_to: ["SV 1003 D", "SV 1005 D", "X100"]
not_applies_to: []

# Traducció
language: "ca"
translation_of: ""  # block_id del bloc original (buit si és l'original)
translation_status: "complete"  # none | partial | complete | reviewed

# Etiquetes semàntiques
tags: ["electric", "high-voltage", "lockout-tagout", "personal-safety"]
severity: "critical"  # low | medium | high | critical

# Aprovació
author: "Joan Linux"
approved_by: "Michael Dostalek"
approved_date: "2021-04-16"
legal_review: true

# Ús intern
related_blocks: ["WARN-ELEC-002", "PROC-INSTALL-001"]
references: ["EN 60204-1", "Directiva 2006/42/CE"]
---
```

## Estructura de Carpetes

```
TechDocs/
├── vault/                          # Obsidian vault (font de veritat)
│   ├── blocks/                     # Blocs atòmics
│   │   ├── warning/
│   │   │   ├── WARN-ELEC-001.ca.md
│   │   │   ├── WARN-ELEC-001.en.md
│   │   │   ├── WARN-CRUSH-001.ca.md
│   │   │   └── WARN-THERM-001.ca.md
│   │   ├── procedure/
│   │   │   ├── PROC-INSTALL-001.ca.md
│   │   │   ├── PROC-MAINT-001.ca.md
│   │   │   └── PROC-STARTUP-001.ca.md
│   │   ├── specification/
│   │   │   ├── SPEC-PERF-SV1003.ca.md
│   │   │   └── SPEC-PERF-SV1005.ca.md
│   │   ├── legal/
│   │   │   └── LEGAL-CE-SV1003.ca.md
│   │   ├── definition/
│   │   │   └── DEF-VACUUM-001.ca.md
│   │   └── reference/
│   │       └── REF-DIAG-001.svg
│   ├── compositions/               # Documents compostos de blocs
│   │   ├── manuals/
│   │   │   ├── seco-sv1003/
│   │   │   │   ├── _index.md       # Metadades del manual
│   │   │   │   ├── cap-seguretat.md
│   │   │   │   └── cap-instalacio.md
│   │   │   └── model-x100/
│   │   └── templates/
│   │       └── manual-template.md
│   └── exports/                    # Exports generats
│       ├── pdf/
│       ├── html/
│       └── json/
├── pipeline/                       # Scripts de processament
│   ├── build.py                    # Pipeline principal
│   ├── export-pdf.py               # Export PDF
│   ├── export-html.py              # Export HTML
│   ├── export-json.py              # Export JSON
│   └── translate.py                # Gestió de traduccions
├── hugo/                           # Site Hugo (consumidor de blocs)
│   ├── layouts/
│   ├── static/
│   └── hugo.toml
├── admin/                          # Decap CMS (opcional)
└── README.md
```

## Composició de Documents

Un capítol és una **composició de blocs**, no un fitxer independent:

```markdown
---
title: "Seguretat"
manual: "seco-sv1003"
chapter: 1
blocks:
  - WARN-ELEC-001
  - WARN-CRUSH-001
  - WARN-THERM-001
  - INFO-SAFETY-001
---

# Seguretat

{{< block id="WARN-ELEC-001" >}}
{{< block id="WARN-CRUSH-001" >}}
{{< block id="INFO-SAFETY-001" >}}
```

## Pipeline Multi-Format

```
[vault/blocks/] → [pipeline] → [exports/]
                     ↓
              build.py llegeix tots els blocs
              els composa segons composicions
              i genera:

              → PDF (Pandoc/WeasyPrint)
              → HTML (Hugo o template propi)
              → JSON (API-ready)
              → XML (DITA Light compatible)
```

## Traducció

Cada bloc té una còpia per idioma amb el **mateix block_id**:

```
WARN-ELEC-001.ca.md   ← original
WARN-ELEC-001.es.md   ← traducció (translation_of: WARN-ELEC-001)
WARN-ELEC-001.en.md   ← traducció
```

El pipeline pot detectar:
- Blocs sense traduir (manca fitxer `.es.md`)
- Traduccions desactualitzades (modified date diferent)
- Cobertura de traducció per manual

## Exemple Real: WARN-ELEC-001

```markdown
---
block_id: "WARN-ELEC-001"
block_type: "warning"
block_category: "electrical"
title: "Perill de descàrrega elèctrica"
version: "1.0"
status: "approved"
applies_to: ["SV 1003 D", "SV 1005 D"]
language: "ca"
tags: ["electric", "high-voltage", "lockout-tagout"]
severity: "critical"
approved_by: "Michael Dostalek"
approved_date: "2021-04-16"
legal_review: true
---

{{< warning type="electric" >}}
**PERILL** — Cables amb electricitat. Risc de descàrrega elèctrica.

Els treballs d'instal·lació elèctrica han de ser realitzats únicament per personal qualificat.

Abans de qualsevol intervenció:
1. Desconnecteu l'alimentació
2. Bloquegeu el dispositiu de tall (LOTO)
3. Verifiqueu l'absència de tensió
{{< /warning >}}
```

## Avantatges

| Abans (documents) | Ara (blocs) |
|---|---|
| Cada capítol és un fitxer independent | Cada advertència/procediment és un fitxer |
| Si canvies un avís, cal canviar-lo a tots els manuals | Canvies un bloc → s'actualitza a tots els manuals |
| No es pot saber quins blocs hi ha sense llegir tot | Cada bloc té ID, tipus, categoria, tags |
| Traduir = crear fitxers sencers nous | Traduir = crear fitxers per bloc |
| Exportar = processar documents sencers | Exportar = seleccionar blocs per tags/producte |
