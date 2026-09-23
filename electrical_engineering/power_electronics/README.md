# Power Electronics — Điện tử công suất

Power electronics điều khiển dòng năng lượng bằng semiconductor switch, magnetics, capacitors và feedback. Khác với signal electronics, thermal, isolation, EMI và fault energy có thể quyết định an toàn của toàn hệ thống.

## Core route

```text
switching device → rectifier/inverter → buck/boost → PWM/control → magnetics → EMI/thermal/protection
```

## Core chapter

- [Switching converters and protection](00_switching_converters_protection.md) — buck model, ripple, losses, thermal path, protection và EMI/layout.
- [Inverter, battery and EMI](01_inverter_battery_emi.md) — half-bridge, dead time, SOC uncertainty, derating và common/differential-mode noise.

## Cần nắm

- conduction/switching loss, dead time, reverse recovery và safe operating area;
- inductor/capacitor ripple, continuous/discontinuous conduction và converter efficiency;
- gate drive, isolation, snubber, current limit và short-circuit protection;
- loop compensation, transient response, thermal path và derating;
- battery/charger interfaces, power integrity, EMI/EMC và compliance boundary.

## Bridge

Mạch và control là prerequisite; semiconductor device physics quay về [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md). Đi tiếp sang embedded khi converter cần digital control hoặc telemetry.
