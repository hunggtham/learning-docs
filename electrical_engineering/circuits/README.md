# Circuits — Mạch điện

Nhánh này xây ngôn ngữ nền của kỹ thuật điện: node, branch, loop, charge, voltage, current, power, impedance và energy. Mạch được học như một mô hình có boundary, source, load, state và measurement point.

## Core route

```text
KCL/KVL → Thévenin/Norton → RC/RL/RLC → phasor/impedance → frequency response → measurement
```

## Core chapter

- [Circuit analysis and measurement](00_circuit_analysis_and_measurement.md) — KCL/KVL, loading, transient, AC impedance, ADC divider và đo kiểm.
- [Network theorems and frequency response](01_network_theorems_frequency_response.md) — nodal/mesh, Thevenin/Norton, Bode, sensitivity và tolerance.

## Cần nắm

- sign convention, reference node, floating ground và common-mode;
- DC operating point, transient response, time constant và initial condition;
- AC steady state, complex impedance, resonance, power factor và three-phase intuition;
- loading, source impedance, tolerance, parasitic và error budget;
- multimeter, oscilloscope, probe loading, grounding và safe measurement.

## Bridge

Prerequisite chính là [Physics — mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md) và [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md); chapter này tập trung vào analysis/design/measurement. Đi tiếp sang [analog electronics](../analog_electronics/README.md) hoặc [signals and systems](../signals_and_systems/README.md).
