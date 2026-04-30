---
title: "Electrical Connection"
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
**DANGER** — Live cables. Risk of electric shock. Electrical installation work must only be carried out by qualified personnel.
{{< /warning >}}

{{< warning type="electric" >}}
**DANGER** — No current protection. In accordance with **EN 60204-1**, the customer must ensure current protection in their installation.
{{< /warning >}}

{{< note >}}
**Electromagnetic compatibility** — Ensure that the machine motor is not affected by electrical or electromagnetic disturbances from the power supply. Ensure that the EMC class of the machine meets the requirements of your supply network system.
{{< /note >}}

## Machine Delivered Without Control Box or Variable Speed Drive (VSD)

Installation requirements:

- The motor power supply must meet the requirements indicated on the motor **nameplate**
- Install a **residual current protection device** (type B recommended) to protect people in case of insulation loss
- Install a **key-operated disconnect switch** or emergency stop switch on the power supply line
- Install **overload protection** on the motor according to EN 60204-1
- Connect the grounding conductor

{{< warning type="general" >}}
**NOTICE** — Incorrect connection. Risk of damage to the motor. The electrical diagram included below is the standard diagram. Inside the terminal box you will find instructions and diagrams for motor connection.
{{< /warning >}}

## Single-Phase Motor Electrical Diagram

{{< figure src="/images/seco-sv-1003/06-esquema-monofasico.svg" alt="Single-phase electrical diagram" caption="Connection diagram — Single-phase motor" numbered="6.2" >}}

| Abbreviation | Meaning |
|---|---|
| **Ha** | Main phase |
| **Hi** | Auxiliary phase |
| **Tw** | Thermal protector |
| **C** | Permanent capacitor |
| **bk** | Black |
| **br** | Brown |
| **bl** | Blue |

## Three-Phase Motor Electrical Diagram

{{< warning type="general" >}}
**NOTICE** — Incorrect direction of rotation. Risk of damage to the machine. The machine can be damaged quickly if used with an incorrect direction of rotation. **Before starting the machine, make sure the direction of rotation is correct.**
{{< /warning >}}

### Direction of Rotation Verification

1. Check the correct direction of rotation using the **arrow** (sticker or cast)
2. Start the motor briefly
3. Observe the motor fan wheel and determine the direction of rotation before the wheel stops

If it is necessary to change the motor rotation:

- **Swap any two motor phase cables**

{{< legal-approval >}}
