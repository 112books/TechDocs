---
title: "Dashboard — Document Status"
type: dashboard
draft: false
---

# Dashboard — Document Status

Overview of the TechDocs documentation system.

## Key Indicators

- **Total documents:** {{ len .Site.RegularPages }}
- **Manuals:** {{ len (where .Site.RegularPages "Type" "manual") }}
- **Warnings:** {{ len (where .Site.RegularPages "Type" "warning") }}
- **Legal:** {{ len (where .Site.RegularPages "Type" "legal") }}
- **Legal review:** {{ len (where .Site.RegularPages "Params.legal_review" true) }}
- **Pending:** {{ len (where .Site.RegularPages "Params.legal_review" false) }}

## Documents by Model

| Model | Documents | Status |
|---|---|---|
| X100 | 6 | ✅ Complete (CA/ES/EN) |
| X200 | 1 | 🔄 In development |
| SECO SV 1003/1005 D | 17 | ✅ Complete (CA/ES/EN) |

## Translations

| Language | Pages | % Complete |
|---|---|---|
| Catalan | {{ len (where .Site.RegularPages "Site.Language.Lang" "ca") }} | 100% |
| Spanish | {{ len (where .Site.RegularPages "Site.Language.Lang" "es") }} | 95% |
| English | {{ len (where .Site.RegularPages "Site.Language.Lang" "en") }} | 95% |

---

*Dashboard generated on {{ now | time.Format "2006-01-02" }}*
