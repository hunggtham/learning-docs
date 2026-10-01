# Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Năng lượng (energy / 에너지) không chỉ là hardware concern** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Embodied chi phí (cost / 비용)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Computer các hệ thống (systems / 시스템들) consume electricity, hardware, water/cooling sức chứa (capacity / 용량) và human attention. Khi software trở thành hạ tầng (infrastructure / 인프라) cho banking, health, education và công khai (public / 공개) services, độ tin cậy (reliability / 신뢰성)/khả năng tiếp cận (accessibility / 접근성)/environmental chi phí (cost / 비용) trở thành properties của society—not chỉ technical metrics.

## Năng lượng (energy / 에너지) không chỉ là hardware concern

Thuật toán (algorithm / 알고리즘) độ phức tạp (complexity / 복잡도), dữ liệu (data / 데이터) movement, polling frequency, mô hình (model / 모델) kích thước (size / 크기), bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) và mạng (network / 네트워크) traffic đều ảnh hưởng năng lượng (energy / 에너지).

Moving dữ liệu (data / 데이터) often costs significant năng lượng (energy / 에너지) relative to cục bộ (local / 로컬) arithmetic. Better locality/compression/batching có thể giảm both độ trễ (latency / 지연 시간) và năng lượng (energy / 에너지).

> **Chuyển mạch:** Trong **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Embodied chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Năng lượng (energy / 에너지) không chỉ là hardware concern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Datacenter efficiency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embodied chi phí (cost / 비용)

Carbon/tài nguyên (resource / 자원) impact không chỉ operational electricity; manufacturing servers/devices, mining materials và disposal có embodied impact.

Extending hardware thời gian tồn tại (lifetime / 수명) qua efficient software có thể giảm replacement pressure, nhưng phải balance bảo mật (security / 보안)/hỗ trợ (support / 지원) các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Ở chặng này của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Datacenter efficiency** tiếp nhận điểm tựa từ **Embodied chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **E-waste** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Datacenter efficiency

Power Usage Effectiveness (PUE) roughly compares total facility năng lượng (energy / 에너지) với IT equipment năng lượng (energy / 에너지). Lower overhead cooling/power phân phối (distribution / 분포) cải thiện efficiency, nhưng PUE không đo full carbon intensity hoặc hardware embodied emissions.

Tải công việc (workload / 워크로드) scheduling theo renewable availability/location có thể giảm carbon nếu độ trễ (latency / 지연 시간)/dữ liệu (data / 데이터) rules cho phép.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **E-waste** tiếp nhận điểm tựa từ **Datacenter efficiency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Digital divide** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## E-waste

Short hỗ trợ (support / 지원) cycles và hardware obsolescence tạo electronic waste. Software requiring ever newer hardware has environmental/xã hội (social / 사회적) chi phí (cost / 비용).

Repairability, modularity và long-term updates là sản phẩm (product / 제품)/hệ thống (system / 시스템) thiết kế (design / 설계) concerns.

> **Chuyển mạch:** Trong **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Digital divide** tiếp nhận điểm tựa từ **E-waste** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Digital divide

Assuming fast broadband, latest phone hoặc constant connectivity excludes users. Offline-first, low-bandwidth modes, smaller bundles và graceful degradation có xã hội (social / 사회적) khả năng tiếp cận (accessibility / 접근성) giá trị (value / 값).

Hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) đôi khi là equity tính năng (feature / 기능), không chỉ UX polish.

> **Chuyển mạch:** Ở chặng này của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)** tiếp nhận điểm tựa từ **Digital divide** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nền tảng (platform / 플랫폼) concentration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)

Nếu công khai (public / 공개) dịch vụ (service / 서비스) không keyboard/screen-reader usable, một population effectively experiences outage dù máy chủ (server / 서버) uptime 99.99%.

Availability phải được nghĩ end-to-end từ hạ tầng (infrastructure / 인프라) đến human truy cập (access / 접근).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Nền tảng (platform / 플랫폼) concentration** tiếp nhận điểm tựa từ **Khả năng tiếp cận (accessibility / 접근성) như hạ tầng (infrastructure / 인프라) độ tin cậy (reliability / 신뢰성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resilience** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nền tảng (platform / 플랫폼) concentration

Cloud/app stores/tìm kiếm (search / 검색)/xã hội (social / 사회적) platforms tạo economies of quy mô (scale / 규모) nhưng cũng concentration of điều khiển (control / 제어). API chính sách (policy / 정책) or outage của một nền tảng (platform / 플랫폼) có thể affect many dependent businesses/users.

Kiến trúc (architecture / 아키텍처) phụ thuộc (dependency / 의존성) có societal/economic dimension: technical lock-in biến thành bargaining power.

> **Chuyển mạch:** Trong **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Resilience** tiếp nhận điểm tựa từ **Nền tảng (platform / 플랫폼) concentration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rebound effects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resilience

Trọng yếu (critical / 중요) hạ tầng (infrastructure / 인프라) cần disaster khôi phục (recovery / 복구), offline/manual fallback và communication plans. “Cloud highly available” không thay nghiệp vụ (business / 비즈니스) continuity nếu định danh (identity / 식별자) provider/mạng (network / 네트워크)/payment upstream cùng thất bại (fail / 실패).

Resilience includes organization/humans, not only replication.

> **Chuyển mạch:** Ở chặng này của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Rebound effects** tiếp nhận điểm tựa từ **Resilience** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rebound effects

Efficiency improvement có thể giảm chi phí (cost / 비용) rồi tăng total usage, khiến total tài nguyên (resource / 자원) consumption không giảm tương ứng. Đây là rebound tác động (effect / 효과).

Vì vậy per-request efficiency chỉ số (metric / 지표) cần đi cùng total tải công việc (workload / 워크로드) growth.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Rebound effects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Software vô hình nên impact môi trường nhỏ.”** Compute/lưu trữ (storage / 저장소)/mạng (network / 네트워크) hardware và năng lượng (energy / 에너지) là vật lý (physical / 물리적) hạ tầng (infrastructure / 인프라).

**“khả năng tiếp cận (accessibility / 접근성) chỉ là UI compliance.”** mạng (network / 네트워크)/thiết bị (device / 장치)/hiệu năng (performance / 성능) các ràng buộc (constraints / 제약조건들) cũng quyết định truy cập (access / 접근).

**“Efficiency luôn giảm total consumption.”** Lower chi phí (cost / 비용) có thể stimulate more usage.

> **Chuyển mạch:** Trong **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Computing là vật lý (physical / 물리적) + xã hội (social / 사회적) hạ tầng (infrastructure / 인프라). Một tối ưu hóa (optimization / 최적화)/kiến trúc (architecture / 아키텍처) quyết định (decision / 결정) phân bố chi phí (cost / 비용) qua năng lượng (energy / 에너지), devices, people và institutions—không chỉ CPU milliseconds.

> **Chuyển mạch:** Ở chặng này của **Sustainability, khả năng tiếp cận (accessibility / 접근성) và computing as xã hội (social / 사회적) hạ tầng (infrastructure / 인프라)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [hardware performance/power](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md), [accessibility](../11_hci_graphics/01_interface_design_accessibility_and_usability.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
