---
title: "Operation"
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

## Control Panel

The control panel of the X100 model is located at the front of the machine and consists of the following elements:

| Element | Function |
|---|---|
| Main switch | General on/off |
| Mode selector | Manual / Automatic / Service |
| LCD screen | Parameter and warning display |
| Emergency button | Immediate stop (red) |
| LED indicator | Operating status |

{{< warning type="general" >}}
**Do not modify factory parameters** without prior authorization. Modifying critical parameters may invalidate CE certification and the manufacturer's warranty.
{{< /warning >}}

## Machine Startup

{{< step number="1" >}}
Verify that all guards are in place and that no person is in the danger zone.
{{< /step >}}

{{< step number="2" >}}
Turn the main switch to the **ON** position. The LCD screen will light up and display the startup screen for 5 seconds.
{{< /step >}}

{{< step number="3" >}}
Check that there are no active warnings on the screen. If there are, consult the troubleshooting chapter before continuing.
{{< /step >}}

{{< step number="4" >}}
Select the operating mode using the selector. For normal operation, use **Automatic** mode.
{{< /step >}}

{{< note >}}
The system performs an automatic self-check each time it is powered on. This process takes approximately 10 seconds. Do not start any cycle until the self-check has completed successfully.
{{< /note >}}

## Operating Modes

### Manual Mode

In manual mode, the operator controls each step of the process individually. This mode is used for:

- Initial setup and calibration
- Quality tests after maintenance
- Error diagnostics

### Automatic Mode

In automatic mode, the machine executes the complete cycle without operator intervention. This is the standard production mode.

### Service Mode

Restricted mode for authorized technicians. Requires access code.

{{< warning type="electric" >}}
**Service Mode** allows access to internal components without guards. Only qualified personnel with specific training may use it.
{{< /warning >}}

## Operating Parameters

### Standard Values

| Parameter | Value | Acceptable Range |
|---|---|---|
| Cycle speed | 12 cycles/min | 8-15 cycles/min |
| Operating temperature | 45°C | 40-55°C |
| Hydraulic pressure | 120 bar | 110-130 bar |
| Power consumption | 7.5 kW | 6.5-8.5 kW |

{{< note >}}
Parameters may vary depending on environmental conditions and processed material. Consult the compensation tables in Annex C for values adjusted for temperature and humidity.
{{< /note >}}

## Shutdown Procedure

### Normal Shutdown

1. Complete the current cycle or press **PAUSE**
2. Move the mode selector to **OFF**
3. Turn the main switch to **OFF**
4. Wait for all LED indicators to turn off

### Emergency Shutdown

Press the **red emergency button** on the control panel. The machine will stop immediately and the hydraulic system will lock.

{{< warning type="crush" >}}
**After an emergency shutdown:** Do not restart the machine until the cause of the emergency has been identified and resolved. Record the incident in the maintenance log.
{{< /warning >}}

{{< legal-approval >}}
