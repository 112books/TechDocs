---
title: "Dashboard — Estado Documental"
type: dashboard
draft: false
---

# Dashboard — Estado Documental

Vista general del sistema de documentación TechDocs.

## Indicadores clave

- **Total documentos:** {{ len .Site.RegularPages }}
- **Manuales:** {{ len (where .Site.RegularPages "Type" "manual") }}
- **Avisos:** {{ len (where .Site.RegularPages "Type" "warning") }}
- **Legal:** {{ len (where .Site.RegularPages "Type" "legal") }}
- **Revisión legal:** {{ len (where .Site.RegularPages "Params.legal_review" true) }}
- **Pendientes:** {{ len (where .Site.RegularPages "Params.legal_review" false) }}

## Documentos por modelo

| Modelo | Documentos | Estado |
|---|---|---|
| X100 | 6 | ✅ Completo (CA/ES/EN) |
| X200 | 1 | 🔄 En desarrollo |
| SECO SV 1003/1005 D | 17 | ✅ Completo (CA/ES/EN) |

## Traducciones

| Idioma | Páginas | % Completo |
|---|---|---|
| Catalán | {{ len (where .Site.RegularPages "Site.Language.Lang" "ca") }} | 100% |
| Castellano | {{ len (where .Site.RegularPages "Site.Language.Lang" "es") }} | 95% |
| Inglés | {{ len (where .Site.RegularPages "Site.Language.Lang" "en") }} | 95% |

---

*Dashboard generado el {{ now | time.Format "2006-01-02" }}*
