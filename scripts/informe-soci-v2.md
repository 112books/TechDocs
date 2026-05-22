# TechDocs v2 — Informe d'Avanç per al Soci

**Data:** 22 de maig de 2026  
**Versió:** 2.0 (Arquitectura de Blocs)  
**Confidencialitat:** Document intern — No distribuir

---

## 1. Resum Executiu

TechDocs v2 ha migrat d'un model de **documents individuals** a un sistema de **blocs atòmics de coneixement**. Cada unitat de contingut (advertència, procediment, especificació, definició) és un fitxer independent amb identificació única, etiquetes semàntiques i metadades d'aprovació legal.

Aquest canvi permet:
- **Reaproveir** un bloc a múltiples manuals sense duplicació
- **Traduir** bloc per bloc, amb control de cobertura
- **Actualitzar** un avís → es reflecteix a tots els manuals automàticament
- **Exportar** a JSON, HTML, PDF des de la mateixa font
- **Gestionar** amb Obsidian (Markdown pur, sense vendor lock-in)

---

## 2. Arquitectura

### 2.1 Esquema de Codificació

Cada bloc té un ID únic format per: `[TIPUS]-[CATEGORIA]-[SEQÜÈNCIA]`

| Tipus | Codi | Exemple |
|---|---|---|
| Advertència | `WARN` | `WARN-ELEC-001` (perill elèctric) |
| Procediment | `PROC` | `PROC-INSTALL-001` (instal·lació) |
| Especificació | `SPEC` | `SPEC-PERF-SV1003` (dades tècniques) |
| Legal | `LEGAL` | `LEGAL-CE-SV1003` (declaració CE) |
| Referència | `REF` | `REF-TROUBLE-001` (taula de problemes) |

### 2.2 Estructura del Vault

```
vault/
├── blocks/              ← 19 blocs atòmics (font de veritat)
│   ├── warning/         ← 9 blocs (elèctric, aixafament, tèrmic...)
│   ├── procedure/       ← 2 blocs (instal·lació, manteniment)
│   ├── specification/   ← 6 blocs (rendiment, peces, intervals...)
│   ├── legal/           ← 1 bloc (declaració CE)
│   └── reference/       ← 1 bloc (taula de resolució de problemes)
├── compositions/        ← 4 capítols compostos de blocs
│   └── manuals/seco-sv1003/
│       ├── cap-seguretat.ca.md          (3 blocs)
│       ├── cap-manteniment.ca.md        (8 blocs)
│       ├── cap-dades-tecniques.ca.md    (1 bloc)
│       └── cap-resolucio-problemes.ca.md (3 blocs)
└── exports/             ← Exports generats
    └── json/seco-sv1003.ca.json         (API-ready)
```

### 2.3 Frontmatter per Bloc

Cada bloc porta metadades estructurades:

```yaml
block_id: "WARN-ELEC-001"
status: "approved"              # draft → review → approved
language: "ca"
translation_of: ""              # vincula a l'original
tags: ["electric", "high-voltage"]
severity: "critical"            # low | medium | high | critical
approved_by: "Michael Dostalek"
approved_date: "2021-04-16"
legal_review: true
applies_to: ["SV 1003 D", "SV 1005 D"]
```

---

## 3. Pipeline Automatitzat

El sistema inclou un pipeline Python que gestiona:

| Comanda | Funció |
|---|---|
| `--list-blocks` | Llista tots els blocs amb estat |
| `--list-compositions` | Llista capítols i els seus blocs |
| `--check-translations es` | Verifica cobertura de traducció |
| `--format json` | Exporta manual sencer a JSON |

### 3.1 Traducció

El pipeline detecta automàticament blocs sense traduir:

```
Translation coverage for 'es':
  Source blocks (ca): 19
  Translated: 1 (5%)
  Missing: 18 blocs
```

Cada traducció és un fitxer independent amb el mateix `block_id`:
```
WARN-ELEC-001.ca.md   ← original
WARN-ELEC-001.es.md   ← traducció (translation_of: WARN-ELEC-001)
```

---

## 4. Estat Actual

### 4.1 Blocs Creats

| Tipus | Quantitat | Estat |
|---|---|---|
| Advertències | 9 | Aprovats (M. Dostalek) |
| Procediments | 2 | Aprovats |
| Especificacions | 6 | Aprovats |
| Legal | 1 | Aprovat |
| Referència | 1 | Aprovat |
| **Total** | **19** | |

### 4.2 Capítols Composats

| Capítol | Blocs | Traduccions |
|---|---|---|
| Seguretat | 3 | ES: 1/3 (33%) |
| Manteniment | 8 | ES: 0/8 (0%) |
| Dades tècniques | 1 | ES: 0/1 (0%) |
| Resolució de problemes | 3 | ES: 0/3 (0%) |

### 4.3 Demo Web

- **URL:** https://112books.github.io/TechDocs/
- **Accés:** Password `TechDocs2026`
- **Contingut:** Manual SECO complet (14 capítols, 3 idiomes)
- **Generat:** Hugo + GitHub Actions (CI/CD automàtic)

---

## 5. Avantatges respecte al Model Anterior

| Aspecte | Abans (v1) | Ara (v2) |
|---|---|---|
| Unitat de contingut | Capítol sencer | Bloc atòmic |
| Duplicació | Sí (mateix avís a 3 manuals) | No (1 bloc → 3 manuals) |
| Traducció | Crear fitxers sencers | Traduir bloc per bloc |
| Actualització | Manual, capítol per capítol | Automàtica, un bloc → tots |
| Cerca per tags | No disponible | Tags semàntics per bloc |
| Export | Només web + PDF | Web + PDF + JSON + HTML |
| Edició | Hugo + CMS | Obsidian (Markdown pur) |

---

## 6. Pròxims Passos

1. **Migrar 10 capítols restants** del SECO a estructura de blocs
2. **Adaptar Hugo** per consumir blocs directament (shortcode `{{< block >}}`)
3. **Completar traduccions** ES/EN dels blocs migrats
4. **Pipeline PDF/HTML** amb Pandoc/WeasyPrint
5. **Configurar Obsidian** vault amb plugins (dataview, templates)
6. **Portal client** amb autenticació per marca blanca

---

## 7. Contacte

**Desenvolupat per:** Joan Linux — LinuxBCN  
**Repositori:** https://github.com/112books/TechDocs  
**Documentació tècnica:** `ARCHITECTURE-v2.md` al repositori
