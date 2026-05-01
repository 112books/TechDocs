---
title: "Operació"
date: 2026-04-30
type: manual
applies_to: ["X100"]
revision: "1.0"
approved_by: "TechDocs"
approved_date: "2026-04-30"
legal_review: false
weight: 3
---

{{< applies-to models="X100" >}}

## Panell de control

El panell de control del model X100 es troba a la part frontal de la màquina i consta dels elements següents:

| Element | Funció |
|---|---|
| Interruptor principal | Engegada/aturada general |
| Selector de mode | Manual / Automàtic / Servei |
| Pantalla LCD | Visualització de paràmetres i avisos |
| Botó d'emergència | Aturada immediata (vermell) |
| Indicador LED | Estat de funcionament |

{{< warning type="general" >}}
**No modifiqueu els paràmetres de fàbrica** sense autorització prèvia. La modificació de paràmetres crítics pot invalidar la certificació CE i la garantia del fabricant.
{{< /warning >}}

## Encesa de la màquina

{{< step number="1" >}}
Verifiqueu que totes les proteccions estan al seu lloc i que no hi ha cap persona a la zona de perill.
{{< /step >}}

{{< step number="2" >}}
Gireu l'interruptor principal a la posició **ON**. La pantalla LCD s'il·luminarà i mostrarà la pantalla d'inici durant 5 segons.
{{< /step >}}

{{< step number="3" >}}
Comproveu que no hi ha cap avís actiu a la pantalla. Si n'hi ha, consulteu el capítol de resolució de problemes abans de continuar.
{{< /step >}}

{{< step number="4" >}}
Seleccioneu el mode de funcionament amb el selector. Per a operació normal, utilitzeu el mode **Automàtic**.
{{< /step >}}

{{< note >}}
El sistema realitza una autocomprovació automàtica cada vegada que s'encén. Aquest procés dura aproximadament 10 segons. No inicieu cap cicle fins que l'autocomprovació hagi finalitzat correctament.
{{< /note >}}

## Modes de funcionament

### Mode Manual

En mode manual, l'operador controla cada pas del procés individualment. Aquest mode s'utilitza per:

- Configuració i calibratge inicial
- Proves de qualitat després del manteniment
- Diagnòstic d'errors

### Mode Automàtic

En mode automàtic, la màquina executa el cicle complet sense intervenció de l'operador. És el mode estàndard de producció.

### Mode Servei

Mode restringit per a tècnics autoritzats. Requereix codi d'accés.

{{< warning type="electric" >}}
El **Mode Servei** permet accés a components interns sense proteccions. Només personal qualificat amb formació específica pot utilitzar-lo.
{{< /warning >}}

## Paràmetres operatius

### Valors estàndard

| Paràmetre | Valor | Rang acceptable |
|---|---|---|
| Velocitat de cicle | 12 cicles/min | 8-15 cicles/min |
| Temperatura operativa | 45°C | 40-55°C |
| Pressió hidràulica | 120 bar | 110-130 bar |
| Consum elèctric | 7.5 kW | 6.5-8.5 kW |

{{< note >}}
Els paràmetres poden variar segons les condicions ambientals i el material processat. Consulteu les taules de compensació a l'annex C per a valors ajustats per temperatura i humitat.
{{< /note >}}

## Procediment d'aturada

### Aturada normal

1. Completeu el cicle actual o premeu **PAUSE**
2. Desplaceu el selector de mode a **OFF**
3. Gireu l'interruptor principal a **OFF**
4. Espereu que tots els indicadors LED s'apaguin

### Aturada d'emergència

Premeu el **botó vermell d'emergència** del panell de control. La màquina s'aturarà immediatament i es bloquejarà el sistema hidràulic.

{{< warning type="crush" >}}
**Després d'una aturada d'emergència:** No reinicieu la màquina fins que s'hagi identificat i resolt la causa de l'emergència. Registreu l'incident al llibre de manteniment.
{{< /warning >}}

{{< legal-approval >}}
