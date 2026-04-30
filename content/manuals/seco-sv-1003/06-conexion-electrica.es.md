---
title: "Conexión eléctrica"
date: 2026-04-30
type: manual
applies_to: ["SV 1003 D", "SV 1005 D"]
revision: "B0004_es"
approved_by: "Michael Dostalek"
approved_date: "2021-04-16"
legal_review: true
draft: false
weight: 6
---

{{< warning type="electric" >}}
**PELIGRO** — Cables con electricidad. Riesgo de descarga eléctrica. Los trabajos de instalación eléctrica deben ser realizados únicamente por personal cualificado.
{{< /warning >}}

{{< warning type="electric" >}}
**PELIGRO** — No existe protección de corriente. De acuerdo con la norma **EN 60204-1**, el cliente debe garantizar una protección de corriente en su instalación.
{{< /warning >}}

{{< note >}}
**Compatibilidad electromagnética** — Asegúrese de que el motor de la máquina no se vea afectado por perturbaciones eléctricas ni electromagnéticas de la red eléctrica. Asegúrese de que la clase CEM de la máquina cumple los requisitos de su sistema de red de suministro.
{{< /note >}}

## Máquina entregada sin caja de mando o variador de frecuencia (VSD)

Requisitos de instalación:

- El suministro eléctrico del motor debe cumplir los requisitos indicados en la **placa identificativa** del motor
- Instale un **dispositivo de protección de corriente residual** (tipo B recomendado) para proteger a las personas en caso de pérdida de aislamiento
- Instale un **interruptor de desconexión con llave** o interruptor de parada de emergencia en la línea de alimentación
- Instale una **protección frente a sobrecargas** en el motor según EN 60204-1
- Conecte el conductor de puesta a tierra

{{< warning type="general" >}}
**AVISO** — Conexión incorrecta. Existe riesgo de daños en el motor. El esquema eléctrico que se incluye a continuación es el esquema habitual. Dentro de la caja de bornes podrá consultar instrucciones y esquemas para la conexión del motor.
{{< /warning >}}

## Esquema eléctrico de motor monofásico

{{< figure src="/images/seco-sv-1003/06-esquema-monofasico.svg" alt="Esquema eléctrico monofásico" caption="Esquema de conexión — Motor monofásico" numbered="6.2" >}}

| Abreviatura | Significado |
|---|---|
| **Ha** | Fase principal |
| **Hi** | Fase auxiliar |
| **Tw** | Protector térmico |
| **C** | Condensador permanente |
| **bk** | Negro |
| **br** | Marrón |
| **bl** | Azul |

## Esquema eléctrico de motor trifásico

{{< warning type="general" >}}
**AVISO** — Rotación en sentido incorrecto. Riesgo de daños en la máquina. La máquina puede dañarse rápidamente si se usa con un sentido de rotación incorrecto. **Antes de poner en marcha la máquina, asegúrese de que el sentido de rotación sea correcto.**
{{< /warning >}}

### Verificación del sentido de rotación

1. Compruebe el sentido de rotación correcto mediante la **flecha** (pegada o de fundición)
2. Ponga en marcha el motor brevemente
3. Observe la rueda del ventilador del motor y determine el sentido de rotación antes de que se detenga

Si es necesario modificar la rotación del motor:

- **Intercambie dos cables de fase** del motor cualesquiera

{{< legal-approval >}}
