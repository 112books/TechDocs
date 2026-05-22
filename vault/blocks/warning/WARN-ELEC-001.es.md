---
block_id: "WARN-ELEC-001"
block_type: "warning"
block_category: "electrical"
title: "Peligro de descarga eléctrica"
version: "1.0"
status: "approved"
created: "2026-04-30"
modified: "2026-04-30"
applies_to: ["SV 1003 D", "SV 1005 D"]
not_applies_to: []
language: "es"
translation_of: "WARN-ELEC-001"
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
**PELIGRO** — Cables con electricidad. Riesgo de descarga eléctrica.

Los trabajos de instalación eléctrica deben ser realizados únicamente por personal cualificado.

De acuerdo con la norma EN 60204-1, el cliente debe garantizar una protección de corriente en su instalación.
{{< /warning >}}

### Procedimiento de bloqueo (LOTO)

Antes de cualquier intervención:

{{< step number="1" >}}
Desconecte la alimentación de la máquina.
{{< /step >}}

{{< step number="2" >}}
Bloquee el dispositivo de corte con candado personal.
{{< /step >}}

{{< step number="3" >}}
Verifique la ausencia de tensión con equipo adecuado.
{{< /step >}}

{{< step number="4" >}}
Espere un mínimo de 5 minutos para la disipación de tensiones residuales.
{{< /step >}}
