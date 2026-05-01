---
title: "Connexió elèctrica"
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
**PERILL** — Cables amb electricitat. Risc de descàrrega elèctrica. Els treballs d'instal·lació elèctrica han de ser realitzats únicament per personal qualificat.
{{< /warning >}}

{{< warning type="electric" >}}
**PERILL** — No existeix protecció de corrent. D'acord amb la norma **EN 60204-1**, el client ha de garantir una protecció de corrent a la seva instal·lació.
{{< /warning >}}

{{< note >}}
**Compatibilitat electromagnètica** — Assegureu-vos que el motor de la màquina no es vegi afectat per perturbacions elèctriques ni electromagnètiques de la xarxa elèctrica. Assegureu-vos que la classe CEM de la màquina compleix els requisits del vostre sistema de xarxa de subministrament.
{{< /note >}}

## Màquina lliurada sense caixa de comandament o variador de freqüència (VSD)

Requisits d'instal·lació:

- El subministrament elèctric del motor ha de complir els requisits indicats a la **placa identificativa** del motor
- Instal·leu un **dispositiu de protecció de corrent residual** (tipus B recomanat) per protegir les persones en cas de pèrdua d'aïllament
- Instal·leu un **interruptor de desconnexió amb clau** o interruptor de parada d'emergència a la línia d'alimentació
- Instal·leu una **protecció davant sobrecàrregues** al motor segons EN 60204-1
- Connecteu el conductor de posada a terra

{{< warning type="general" >}}
**AVÍS** — Connexió incorrecta. Existeix risc de danys al motor. L'esquema elèctric que s'inclou a continuació és l'esquema habitual. Dins de la caixa de borns podreu consultar instruccions i esquemes per a la connexió del motor.
{{< /warning >}}

## Esquema elèctric de motor monofàsic

{{< figure src="/images/seco-sv-1003/06-esquema-monofasico.svg" alt="Esquema elèctric monofàsic" caption="Esquema de connexió — Motor monofàsic" numbered="6.2" >}}

| Abreviatura | Significat |
|---|---|
| **Ha** | Fase principal |
| **Hi** | Fase auxiliar |
| **Tw** | Protector tèrmic |
| **C** | Condensador permanent |
| **bk** | Negre |
| **br** | Marró |
| **bl** | Blau |

## Esquema elèctric de motor trifàsic

{{< warning type="general" >}}
**AVÍS** — Rotació en sentit incorrecte. Risc de danys a la màquina. La màquina pot danyar-se ràpidament si s'usa amb un sentit de rotació incorrecte. **Abans de posar en marxa la màquina, assegureu-vos que el sentit de rotació sigui correcte.**
{{< /warning >}}

### Verificació del sentit de rotació

1. Comproveu el sentit de rotació correcte mitjançant la **fletxa** (enganxada o de fosa)
2. Poseu en marxa el motor breument
3. Observeu la roda del ventilador del motor i determineu el sentit de rotació abans que la roda s'aturi

Si cal modificar la rotació del motor:

- **Intercanvieu dos cables de fase** del motor qualsvol

## Esquema elèctric trifàsic

{{< figure src="/images/seco-06-schematic-3phase.svg" caption="Connexió elèctrica trifàsica (L1-L2-L3-N-PE)" >}}

{{< legal-approval >}}
