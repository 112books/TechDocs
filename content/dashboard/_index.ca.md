---
title: "Dashboard — Estat Documental"
type: dashboard
draft: false
---

# Dashboard — Estat Documental

Vista general del sistema de documentació TechDocs.

## Indicadors clau

- **Total documents:** {{ len .Site.RegularPages }}
- **Manuals:** {{ len (where .Site.RegularPages "Type" "manual") }}
- **Avissos:** {{ len (where .Site.RegularPages "Type" "warning") }}
- **Legal:** {{ len (where .Site.RegularPages "Type" "legal") }}
- **Revisió legal:** {{ len (where .Site.RegularPages "Params.legal_review" true) }}
- **Pendents:** {{ len (where .Site.RegularPages "Params.legal_review" false) }}

## Documents per model

| Model | Documents | Estat |
|---|---|---|
| X100 | 6 | ✅ Complet (CA/ES/EN) |
| X200 | 1 | 🔄 En desenvolupament |
| SECO SV 1003/1005 D | 17 | ✅ Complet (CA/ES/EN) |

## Traduccions

| Idioma | Pàgines | % Complet |
|---|---|---|
| Català | {{ len (where .Site.RegularPages "Site.Language.Lang" "ca") }} | 100% |
| Castellà | {{ len (where .Site.RegularPages "Site.Language.Lang" "es") }} | 95% |
| Anglès | {{ len (where .Site.RegularPages "Site.Language.Lang" "en") }} | 95% |

---

*Dashboard generat el {{ now | time.Format "2006-01-02" }}*
