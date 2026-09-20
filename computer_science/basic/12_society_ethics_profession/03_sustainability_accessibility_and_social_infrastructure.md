# Sustainability, accessibility và computing as social infrastructure

Computer systems consume electricity, hardware, water/cooling capacity và human attention. Khi software trở thành infrastructure cho banking, health, education và public services, reliability/accessibility/environmental cost trở thành properties của society—not chỉ technical metrics.

## Energy không chỉ là hardware concern

Algorithm complexity, data movement, polling frequency, model size, cache behavior và network traffic đều ảnh hưởng energy.

Moving data often costs significant energy relative to local arithmetic. Better locality/compression/batching có thể giảm both latency và energy.

## Embodied cost

Carbon/resource impact không chỉ operational electricity; manufacturing servers/devices, mining materials và disposal có embodied impact.

Extending hardware lifetime qua efficient software có thể giảm replacement pressure, nhưng phải balance security/support constraints.

## Datacenter efficiency

Power Usage Effectiveness (PUE) roughly compares total facility energy với IT equipment energy. Lower overhead cooling/power distribution cải thiện efficiency, nhưng PUE không đo full carbon intensity hoặc hardware embodied emissions.

Workload scheduling theo renewable availability/location có thể giảm carbon nếu latency/data rules cho phép.

## E-waste

Short support cycles và hardware obsolescence tạo electronic waste. Software requiring ever newer hardware has environmental/social cost.

Repairability, modularity và long-term updates là product/system design concerns.

## Digital divide

Assuming fast broadband, latest phone hoặc constant connectivity excludes users. Offline-first, low-bandwidth modes, smaller bundles và graceful degradation có social accessibility value.

Performance optimization đôi khi là equity feature, không chỉ UX polish.

## Accessibility như infrastructure reliability

Nếu public service không keyboard/screen-reader usable, một population effectively experiences outage dù server uptime 99.99%.

Availability phải được nghĩ end-to-end từ infrastructure đến human access.

## Platform concentration

Cloud/app stores/search/social platforms tạo economies of scale nhưng cũng concentration of control. API policy or outage của một platform có thể affect many dependent businesses/users.

Architecture dependency có societal/economic dimension: technical lock-in biến thành bargaining power.

## Resilience

Critical infrastructure cần disaster recovery, offline/manual fallback và communication plans. “Cloud highly available” không thay business continuity nếu identity provider/network/payment upstream cùng fail.

Resilience includes organization/humans, not only replication.

## Rebound effects

Efficiency improvement có thể giảm cost rồi tăng total usage, khiến total resource consumption không giảm tương ứng. Đây là rebound effect.

Vì vậy per-request efficiency metric cần đi cùng total workload growth.

## Common Misconceptions

**“Software vô hình nên impact môi trường nhỏ.”** Compute/storage/network hardware và energy là physical infrastructure.

**“Accessibility chỉ là UI compliance.”** Network/device/performance constraints cũng quyết định access.

**“Efficiency luôn giảm total consumption.”** Lower cost có thể stimulate more usage.

## Mental Model

> Computing là physical + social infrastructure. Một optimization/architecture decision phân bố cost qua energy, devices, people và institutions—không chỉ CPU milliseconds.

## Kết nối

Đọc [hardware performance/power](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md), [accessibility](../11_hci_graphics/01_interface_design_accessibility_and_usability.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).