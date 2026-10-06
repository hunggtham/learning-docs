# Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Sustainability, accessibility và computing as social infrastructure**. Route đi từ energy/embodied cost → datacenter/e-waste → digital divide/accessibility → platform concentration/resilience → rebound effects, để hạ tầng được đánh giá theo tác động dài hạn.

Computer các hệ thống (systems / 시스템들) consume electricity, hardware, water/cooling sức chứa (capacity / 용량) và human attention. Khi software trở thành hạ tầng (infrastructure / 인프라) cho banking, health, education và công khai (public / 공개) services, độ tin cậy (reliability / 신뢰성)/khả năng tiếp cận (accessibility / 접근성)/environmental chi phí (cost / 비용) trở thành properties của society—not chỉ technical metrics.

## Năng lượng (energy / 에너지) không chỉ là hardware concern

Thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도), dữ liệu (data / 데이터) movement, polling frequency, mô hình (model / 모델) kích thước (size / 크기), bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) và mạng (network / 네트워크) traffic đều ảnh hưởng năng lượng (energy / 에너지).

Moving dữ liệu (data / 데이터) often costs significant năng lượng (energy / 에너지) relative to cục bộ (local / 로컬) arithmetic. Better locality/compression/batching có thể giảm both độ trễ (latency / 지연 시간) và năng lượng (energy / 에너지).

> **Nối mạch:** Energy use không chỉ nằm ở lúc chạy hardware; embodied cost của sản xuất cộng với datacenter efficiency và accessibility quyết định tổng tác động xã hội của hạ tầng tính toán.

## Embodied chi phí (cost / 비용)

Carbon/tài nguyên (resource / 자원) impact không chỉ operational electricity; manufacturing servers/devices, mining materials và disposal có embodied impact.

Extending hardware thời gian tồn tại (lifetime / 수명) qua efficient software có thể giảm replacement pressure, nhưng phải balance bảo mật (security / 보안)/hỗ trợ (support / 지원) các ràng buộc (constraints / 제약조건들).

> **Nối mạch:** **Datacenter efficiency** nối từ **Embodied chi phí (cost / 비용)** sang **E-waste**, vì cơ chế trước tạo đầu vào cho bước sau.

## Datacenter efficiency

Power Usage Effectiveness (PUE) roughly compares total facility năng lượng (energy / 에너지) với IT equipment năng lượng (energy / 에너지). Lower overhead cooling/power phân phối (distribution / 분포) cải thiện efficiency, nhưng PUE không đo full carbon intensity hoặc hardware embodied emissions.

Tải công việc (workload / 워크로드) scheduling theo renewable availability/location có thể giảm carbon nếu độ trễ (latency / 지연 시간)/dữ liệu (data / 데이터) rules cho phép.

> **Nối mạch:** **E-waste** nối từ **Datacenter efficiency** sang **Digital divide**, vì cơ chế trước tạo đầu vào cho bước sau.

## E-waste

Short hỗ trợ (support / 지원) cycles và hardware obsolescence tạo electronic waste. Software requiring ever newer hardware has environmental/xã hội (social / 사회적) chi phí (cost / 비용).

Repairability, modularity và long-term updates là sản phẩm (product / 제품)/hệ thống (system / 시스템) thiết kế (design / 설계) concerns.

> **Nối mạch:** **Digital divide** nối từ **E-waste** sang **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Digital divide

Assuming fast broadband, latest phone hoặc constant connectivity excludes users. Offline-first, low-bandwidth modes, smaller bundles và graceful degradation có xã hội (social / 사회적) khả năng tiếp cận (accessibility / 접근성) giá trị (value / 값).

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) đôi khi là equity tính năng (feature / 기능), không chỉ UX polish.

> **Nối mạch:** **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)** nối từ **Digital divide** sang **Nền tảng (platform / 플랫폼) concentration**, vì cơ chế trước tạo đầu vào cho bước sau.

## Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)

Nếu công khai (public / 공개) dịch vụ (service / 서비스) không keyboard/screen-reader usable, một population effectively experiences outage dù máy chủ (server / 서버) uptime 99.99%.

Availability phải được nghĩ end-to-end từ hạ tầng (infrastructure / 인프라) đến human truy cập (access / 접근).

> **Nối mạch:** **Nền tảng (platform / 플랫폼) concentration** nối từ **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)** sang **Resilience**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nền tảng (platform / 플랫폼) concentration

Cloud/app stores/tìm kiếm (search / 검색)/xã hội (social / 사회적) platforms tạo economies of quy mô (scale / 규모) nhưng cũng concentration of điều khiển (control / 제어). API chính sách (policy / 정책) or outage của một nền tảng (platform / 플랫폼) có thể affect many dependent businesses/users.

Kiến trúc (architecture / 아키텍처) phụ thuộc (dependency / 의존성) có societal/economic dimension: technical lock-in biến thành bargaining power.

> **Nối mạch:** **Resilience** nối từ **Nền tảng (platform / 플랫폼) concentration** sang **Rebound effects**, vì cơ chế trước tạo đầu vào cho bước sau.

## Resilience

Trọng yếu (critical / 중요) hạ tầng (infrastructure / 인프라) cần disaster khôi phục (recovery / 복구), offline/manual fallback và communication plans. “Cloud highly available” không thay nghiệp vụ (business / 비즈니스) continuity nếu định danh (identity / 식별자) provider/mạng (network / 네트워크)/payment upstream cùng thất bại (fail / 실패).

Resilience includes organization/humans, not only replication.

> **Nối mạch:** **Rebound effects** nối từ **Resilience** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Rebound effects

Efficiency improvement có thể giảm chi phí (cost / 비용) rồi tăng total usage, khiến total tài nguyên (resource / 자원) consumption không giảm tương ứng. Đây là rebound tác động (effect / 효과).

Vì vậy per-request efficiency chỉ số (metric / 지표) cần đi cùng total tải công việc (workload / 워크로드) growth.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Rebound effects** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Software vô hình nên impact môi trường nhỏ.”** Compute/lưu trữ (storage / 저장소)/mạng (network / 네트워크) hardware và năng lượng (energy / 에너지) là vật lý (physical / 물리적) hạ tầng (infrastructure / 인프라).

**“khả năng tiếp cận (accessibility / 접근성) chỉ là UI compliance.”** mạng (network / 네트워크)/thiết bị (device / 장치)/hiệu năng (performance / 성능) các ràng buộc (constraints / 제약조건들) cũng quyết định truy cập (access / 접근).

**“Efficiency luôn giảm total consumption.”** Lower chi phí (cost / 비용) có thể stimulate more usage.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Computing là vật lý (physical / 물리적) + xã hội (social / 사회적) hạ tầng (infrastructure / 인프라). Một tối ưu hóa (optimization / 최적화)/kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) phân bố chi phí (cost / 비용) qua năng lượng (energy / 에너지), devices, people và institutions—không chỉ CPU milliseconds.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc [hardware performance/power](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md), [accessibility](../11_hci_graphics/01_interface_design_accessibility_and_usability.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
