---
block_id: "WARN-ELEC-001"
block_type: "warning"
block_category: "electrical"
title: "Perill de descàrrega elèctrica"
version: "1.0"
status: "approved"
created: "2026-04-30"
modified: "2026-04-30"
applies_to: ["SV 1003 D", "SV 1005 D"]
not_applies_to: []
language: "ca"
translation_of: ""
translation_status: "complete"
tags: ["electric", "high-voltage", "lockout-tagout", "personal-safety"]
severity: "critical"
author: "Joan Linux"
approved_by: "Michael Dostalek"
approved_date: "2021-04-16"
legal_review: true
related_blocks: ["PROC-INSTALL-001", "WARN-ELEC-002"]
references: ["EN 60204-1", "Directiva 2006/42/CE"]
---

{{< warning type="electric" >}}
**PERILL** — Cables amb electricitat. Risc de descàrrega elèctrica.

Els treballs d'instal·lació elèctrica han de ser realitzats únicament per personal qualificat.

D'acord amb la norma EN 60204-1, el client ha de garantir una protecció de corrent a la seva instal·lació.
{{< /warning >}}

### Procediment de bloqueig (LOTO)

Abans de qualsevol intervenció:

{{< step number="1" >}}
Desconnecteu l'alimentació de la màquina.
{{< /step >}}

{{< step number="2" >}}
Bloquegeu el dispositiu de tall amb cadenat personal.
{{< /step >}}

{{< step number="3" >}}
Verifiqueu l'absència de tensió amb equip adequat.
{{< /step >}}

{{< step number="4" >}}
Espereu un mínim de 5 minuts per a la dissipació de tensions residuals.
{{< /step >}}
