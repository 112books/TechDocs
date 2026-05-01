---
title: "Operación"
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

## Panel de control

El panel de control del modelo X100 se encuentra en la parte frontal de la máquina y consta de los elementos siguientes:

| Elemento | Función |
|---|---|
| Interruptor principal | Encendido/parada general |
| Selector de modo | Manual / Automático / Servicio |
| Pantalla LCD | Visualización de parámetros y avisos |
| Botón de emergencia | Parada inmediata (rojo) |
| Indicador LED | Estado de funcionamiento |

{{< warning type="general" >}}
**No modifique los parámetros de fábrica** sin autorización previa. La modificación de parámetros críticos puede invalidar la certificación CE y la garantía del fabricante.
{{< /warning >}}

## Encendido de la máquina

{{< step number="1" >}}
Verifique que todas las protecciones están en su lugar y que no hay ninguna persona en la zona de peligro.
{{< /step >}}

{{< step number="2" >}}
Gire el interruptor principal a la posición **ON**. La pantalla LCD se iluminará y mostrará la pantalla de inicio durante 5 segundos.
{{< /step >}}

{{< step number="3" >}}
Compruebe que no hay ningún aviso activo en la pantalla. Si los hay, consulte el capítulo de resolución de problemas antes de continuar.
{{< /step >}}

{{< step number="4" >}}
Seleccione el modo de funcionamiento con el selector. Para operación normal, utilice el modo **Automático**.
{{< /step >}}

{{< note >}}
El sistema realiza una autocomprobación automática cada vez que se enciende. Este proceso dura aproximadamente 10 segundos. No inicie ningún ciclo hasta que la autocomprobación haya finalizado correctamente.
{{< /note >}}

## Modos de funcionamiento

### Modo Manual

En modo manual, el operador controla cada paso del proceso individualmente. Este modo se utiliza para:

- Configuración y calibrado inicial
- Pruebas de calidad después del mantenimiento
- Diagnóstico de errores

### Modo Automático

En modo automático, la máquina ejecuta el ciclo completo sin intervención del operador. Es el modo estándar de producción.

### Modo Servicio

Modo restringido para técnicos autorizados. Requiere código de acceso.

{{< warning type="electric" >}}
El **Modo Servicio** permite acceso a componentes internos sin protecciones. Solo personal cualificado con formación específica puede utilizarlo.
{{< /warning >}}

## Parámetros operativos

### Valores estándar

| Parámetro | Valor | Rango aceptable |
|---|---|---|
| Velocidad de ciclo | 12 ciclos/min | 8-15 ciclos/min |
| Temperatura operativa | 45°C | 40-55°C |
| Presión hidráulica | 120 bar | 110-130 bar |
| Consumo eléctrico | 7.5 kW | 6.5-8.5 kW |

{{< note >}}
Los parámetros pueden variar según las condiciones ambientales y el material procesado. Consulte las tablas de compensación en el anexo C para valores ajustados por temperatura y humedad.
{{< /note >}}

## Procedimiento de parada

### Parada normal

1. Complete el ciclo actual o presione **PAUSE**
2. Desplace el selector de modo a **OFF**
3. Gire el interruptor principal a **OFF**
4. Espere que todos los indicadores LED se apaguen

### Parada de emergencia

Pulse el **botón rojo de emergencia** del panel de control. La máquina se parará inmediatamente y se bloqueará el sistema hidráulico.

{{< warning type="crush" >}}
**Después de una parada de emergencia:** No reinicie la máquina hasta que se haya identificado y resuelto la causa de la emergencia. Registre el incidente en el libro de mantenimiento.
{{< /warning >}}

{{< legal-approval >}}
