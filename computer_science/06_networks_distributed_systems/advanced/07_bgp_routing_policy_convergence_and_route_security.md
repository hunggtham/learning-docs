# BGP, routing chính sách (policy / 정책), convergence và tuyến (route / 경로) bảo mật (security / 보안)

> **Mạch đọc:** Đặt **BGP, routing chính sách (policy / 정책), convergence và tuyến (route / 경로) bảo mật (security / 보안)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Routing có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인)** sang **2. Prefix và AS là hai lớp trừu tượng (abstraction / 추상화) khác nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đọc trước phần foundation về IP/routing và BGP trong [`basic/06_networks_distributed_systems`](../../basic/06_networks_distributed_systems/), cùng [TCP/UDP và congestion](../../basic/06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md). Chapter này không học BGP như danh sách message kiểu (type / 타입); mục tiêu là lập luận (reasoning / 추론) môi trường vận hành (production / 운영 환경) khi **điều khiển (control / 제어) plane quyết định tuyến (route / 경로) nào tồn tại, mặt phẳng dữ liệu (data plane / 데이터 플레인) forward theo tuyến (route / 경로) đó, chính sách (policy / 정책) giữa các Autonomous các hệ thống (systems / 시스템들) (AS) thay đổi đường dẫn (path / 경로), và thất bại (failure / 실패) có thể lan ra Internet dù từng router riêng lẻ vẫn hoạt động**.

Mô hình tư duy (mental model / 사고 모델):

```text
prefix ownership / reachability
→ route advertisement
→ policy + path selection
→ RIB
→ best routes installed into FIB
→ packet forwarding
→ observation from endpoints
```

## 1. Routing có điều khiển (control / 제어) plane và mặt phẳng dữ liệu (data plane / 데이터 플레인)

**điều khiển (control / 제어) plane** học và chọn reachability. **mặt phẳng dữ liệu (data plane / 데이터 플레인)** dùng forwarding bảng (table / 테이블) để chuyển packet ở tốc độ cao.

BGP chủ yếu là control-plane giao thức (protocol / 프로토콜). Khi BGP session thay đổi, router không “forward packet bằng BGP message”; nó recompute routes rồi cập nhật FIB hoặc equivalent hardware/software forwarding trạng thái (state / 상태).

Vì vậy sự cố có thể tồn tại ở ba lớp khác nhau:

```text
route không được học
route được học nhưng policy chọn path khác
route được chọn nhưng FIB/data plane không forward như mong đợi
```

## 2. Prefix và AS là hai lớp trừu tượng (abstraction / 추상화) khác nhau

IP prefix mô tả vùng địa chỉ. Autonomous hệ thống (system / 시스템) là lĩnh vực (domain / 도메인) quản trị routing có chính sách (policy / 정책) riêng. Một AS có thể originate nhiều prefixes; một prefix có thể được quảng bá qua nhiều upstreams.

BGP path-vector mang thông tin reachability và AS đường dẫn (path / 경로). Nhưng mục tiêu không phải tìm “đường ngắn nhất toàn Internet” theo độ trễ (latency / 지연 시간). Mỗi mạng (network / 네트워크) áp chính sách (policy / 정책) kinh tế/kỹ thuật riêng.

Đây là bất biến (invariant / 불변식) xã hội-kỹ thuật quan trọng: **toàn cục (global / 전역) routing emergent từ chính sách (policy / 정책) cục bộ (local / 로컬)**, không từ một optimizer trung tâm.

## 3. eBGP và iBGP giải hai ranh giới (boundary / 경계) khác nhau

Bên ngoài (external / 외부) BGP trao routes giữa ASes. nội bộ (internal / 내부) BGP phân phối bên ngoài (external / 외부) reachability bên trong một AS lớn. IGP như OSPF/IS-IS thường giải reachability nội bộ tới next hop; BGP giữ chính sách (policy / 정책)/inter-domain đường dẫn (path / 경로).

Một tuyến (route / 경로) có thể hợp lệ ở BGP tầng (layer / 계층) nhưng next-hop nội bộ unreachable vì IGP/FIB issue. Vì vậy debugging phải tách BGP điều khiển (control / 제어) trạng thái (state / 상태) khỏi underlay reachability.

## 4. Best-path không đồng nghĩa shortest AS_PATH

AS_PATH là một tín hiệu (signal / 신호) quan trọng và giúp vòng lặp (loop / 루프) prevention, nhưng chính sách (policy / 정책) attributes có thể ưu tiên nghiệp vụ (business / 비즈니스) relationship hoặc traffic kỹ thuật (engineering / 엔지니어링) trước độ dài đường dẫn (path / 경로).

Các hiện thực (implementation / 구현) thường có concept như cục bộ (local / 로컬) preference, origin/đường dẫn (path / 경로) attributes, MED và tie-breakers. Chi tiết thứ tự (order / 순서) khác ecosystem/vendor/phiên bản (version / 버전); mô hình tư duy (mental model / 사고 모델) bền là:

```text
import policy
→ preference class
→ path characteristics
→ tie-break
→ best route
```

Không nên nhìn AS_PATH ngắn hơn rồi kết luận tuyến (route / 경로) đó chắc chắn được chọn.

## 5. Import/export chính sách (policy / 정책) quyết định Internet mà neighbor nhìn thấy

Router không nhất thiết quảng bá mọi tuyến (route / 경로) nó biết cho mọi neighbor. Export chính sách (policy / 정책) phản ánh relationship như customer/provider/peer và bảo mật (security / 보안) controls.

Một cấu hình export sai có thể biến AS thành transit ngoài ý muốn hoặc leak routes học từ một provider sang provider khác. Vì vậy tuyến (route / 경로) leak thường là chính sách (policy / 정책) thất bại (failure / 실패), không phải packet corruption.

## 6. RIB và FIB phải được phân biệt

Routing thông tin (information / 정보) cơ sở (base / 기반) (RIB) giữ candidate/best routing trạng thái (state / 상태) ở điều khiển (control / 제어) plane. Forwarding thông tin (information / 정보) cơ sở (base / 기반) (FIB) là trạng thái (state / 상태) tối ưu cho packet lookup.

Nếu điều khiển (control / 제어) plane hội tụ nhưng FIB programming thất bại/chậm, operator có thể thấy BGP tuyến (route / 경로) “đúng” mà traffic vẫn drop/blackhole.

Bằng chứng vận hành (production evidence / 운영 증거) cần kiểm tra cả hai khi nền tảng (platform / 플랫폼) hỗ trợ.

## 7. Withdrawal và convergence tạo một khoảng thời gian bất định

Khi link/nút (node / 노드)/đường dẫn (path / 경로) hỏng, tuyến (route / 경로) withdrawal lan qua neighbors. Mỗi AS recompute theo chính sách (policy / 정책) rồi quảng bá trạng thái (state / 상태) mới. Trong khoảng convergence, các vantage points khác nhau có thể thấy paths khác nhau.

Do đó Internet routing không có instant atomic cập nhật (update / 업데이트). Một thất bại (failure / 실패) có thể biểu hiện transient mất mát (loss / 손실), đường dẫn (path / 경로) stretch hoặc asymmetric reachability trước khi ổn định.

Liveness của routing là eventual convergence; an toàn (safety / 안전) cần tránh vòng lặp (loop / 루프)/invalid reachability trong quá trình chuyển trạng thái.

## 8. đường dẫn (path / 경로) exploration làm convergence tốn thời gian hơn một lần recompute

Sau khi đường dẫn (path / 경로) tốt nhất biến mất, routers có thể thử các alternatives rồi lần lượt nhận withdrawals mới. điều khiển (control / 제어) plane có thể “khám phá” nhiều đường dẫn (path / 경로) trước khi ổn định.

Tuyến (route / 경로) flap damping và chính sách (policy / 정책) suppression từng được dùng để giảm churn nhưng có thể kéo dài outage nếu suppress reachability hợp lệ. Đây là ví dụ điển hình của điều khiển (control / 제어) chống instability nhưng có availability sự đánh đổi (trade-off / 트레이드오프).

## 9. tuyến (route / 경로) aggregation giảm trạng thái (state / 상태) nhưng mở rộng thất bại (failure / 실패) blast radius

Aggregating nhiều specific prefixes thành supernet giảm routing-table kích thước (size / 크기). Nhưng nếu aggregate vẫn được advertise khi một subprefix phía sau không reachable, traffic có thể đi vào AS rồi blackhole.

Do đó aggregate thường cần discard/null tuyến (route / 경로) hoặc reachability điều kiện (condition / 조건) thích hợp để tránh vòng lặp (loop / 루프). Aggregation là compression của routing trạng thái (state / 상태), và như mọi compression, nó làm mất chi tiết.

## 10. More-specific tuyến (route / 경로) thường thắng data-plane lookup

Longest-prefix match nghĩa tuyến (route / 경로) `/24` thường được ưu tiên hơn covering `/16` ở forwarding lookup. Vì vậy accidental hoặc malicious more-specific announcement có thể hút traffic khỏi origin rộng hơn nếu được Internet chấp nhận.

Đây là cơ chế nền của nhiều tuyến (route / 경로) hijack scenario: không cần “hack router của nạn nhân”; chỉ cần invalid reachability được propagated và selected.

## 11. tuyến (route / 경로) leak và tuyến (route / 경로) hijack không hoàn toàn giống nhau

**tuyến (route / 경로) leak** thường là tuyến (route / 경로) hợp lệ về origin/reachability nhưng được export qua relationship không nên export, tạo đường dẫn (path / 경로) chính sách (policy / 정책) bất thường.

**tuyến (route / 경로) hijack** thường chỉ việc một AS originate/propagate prefix không được phép hoặc làm Internet chọn origin/đường dẫn (path / 경로) sai.

Từ endpoint, cả hai có thể trông như đường dẫn (path / 경로) đổi, độ trễ (latency / 지연 시간) tăng, traffic mất hoặc đi qua mạng (network / 네트워크) lạ. Phân loại cần control-plane bằng chứng (evidence / 증거).

## 12. RPKI origin kiểm tra hợp lệ (validation / 검증) bảo vệ một phần bất biến (invariant / 불변식)

Tài nguyên (resource / 자원) công khai (public / 공개) Key hạ tầng (infrastructure / 인프라) (RPKI) cho phép publish tuyến (route / 경로) Origin Authorization (ROA), nói AS nào được phép originate prefix với max length nhất định.

Router có thể classify tuyến (route / 경로) origin kiểm tra hợp lệ (validation / 검증) thành valid/invalid/not-found và áp chính sách (policy / 정책) tương ứng.

RPKI giúp chống nhiều origin hijack nhưng **không chứng minh toàn bộ AS đường dẫn (path / 경로) hợp lệ** và không tự ngăn mọi tuyến (route / 경로) leak. bảo mật (security / 보안) điều khiển (control / 제어) phải được hiểu đúng phạm vi (scope / 범위).

## 13. Prefix filtering và max-prefix là containment controls

Neighbor chính sách (policy / 정책) có thể chỉ chấp nhận prefixes/AS paths phù hợp expectation. Max-prefix limit giúp ngăn một peer/customer vô tình đẩy hàng trăm nghìn routes làm control-plane/tài nguyên (resource / 자원) pressure.

Nhưng fail-closed mạnh quá có thể cắt legitimate traffic khi mạng (network / 네트워크) tăng prefix count. Vì vậy threshold cần operational quản trị (governance / 거버넌스), không chỉ cấu hình một lần.

## 14. Communities là siêu dữ liệu (metadata / 메타데이터) chính sách (policy / 정책), không phải routing guarantee

BGP communities cho phép gắn siêu dữ liệu (metadata / 메타데이터) để upstream/downstream áp hành động (action / 동작) như preference, export phạm vi (scope / 범위) hoặc blackholing. ngữ nghĩa (semantics / 의미론) phụ thuộc agreement giữa networks.

Một community có ý nghĩa trong đặc tả hợp đồng (contract / 계약) cụ thể, không phải toàn cục (global / 전역) bất biến (invariant / 불변식). Khi gỡ lỗi (debug / 디버그) phải biết ai set nó, ở ranh giới (boundary / 경계) nào, và chính sách (policy / 정책) nào consume nó.

## 15. Anycast dựa vào routing để đưa cùng IP tới nhiều sites

Nhiều locations có thể advertise cùng prefix. Internet chính sách (policy / 정책) chọn đường dẫn (path / 경로) tới một site “gần” theo routing, không nhất thiết theo geographic distance.

Anycast cải thiện độ trễ (latency / 지연 시간)/resilience nhưng session/stateful hành vi (behavior / 동작) trở nên nhạy với tuyến (route / 경로) thay đổi (change / 변경). Khi đường dẫn (path / 경로) flips, yêu cầu (request / 요청) sau có thể tới site khác. ứng dụng (application / 애플리케이션) tầng (layer / 계층) cần thiết kế trạng thái (state / 상태), thử lại (retry / 재시도) và idempotency phù hợp.

## 16. Asymmetric routing là bình thường hơn nhiều người nghĩ

Forward đường dẫn (path / 경로) và return đường dẫn (path / 경로) có thể đi qua ASes khác nhau do chính sách (policy / 정책) độc lập. Firewall/stateful middlebox các giả định (assumptions / 가정들) có thể hỏng nếu topology yêu cầu symmetry.

Traceroute từ A tới B không mô tả reverse đường dẫn (path / 경로). Debugging one-way mất mát (loss / 손실) cần vantage điểm (point / 지점) hai phía hoặc telemetry trung gian.

## 17. ECMP phân phối traffic nhưng băm (hash / 해시) tạo hidden skew

Equal-Cost Multi-Path có thể băm (hash / 해시) luồng (flow / 흐름) theo 5-tuple hoặc fields khác. Tổng bandwidth còn dư nhưng một subset flows có thể dồn vào một member đường dẫn (path / 경로) nóng.

Một elephant luồng (flow / 흐름) không được chia nếu băm (hash / 해시) per-flow. Link utilization trung bình vì vậy có thể che micro-hotspot và packet mất mát (loss / 손실) trên một member.

## 18. BGP session health không chứng minh ứng dụng (application / 애플리케이션) reachability

TCP session BGP có thể `Established`, routes có thể present, nhưng packet vẫn thất bại (fail / 실패) do ACL, MTU, FIB, tunnel, congestion, next-hop reachability hoặc remote ứng dụng (application / 애플리케이션).

Ngược lại, ứng dụng (application / 애플리케이션) có thể vẫn hoạt động trong lúc control-plane session flap nhờ stale/graceful-restart forwarding trạng thái (state / 상태) tùy thiết kế (design / 설계).

Status ở một tầng (layer / 계층) không thay proof ở tầng (layer / 계층) khác.

## 19. bằng chứng vận hành (production evidence / 운영 증거) cần dựng lại tuyến (route / 경로) quyết định (decision / 결정) theo thời gian

Một sự cố (incident / 인시던트) routing tốt cần biết:

```text
prefix nào bị ảnh hưởng?
origin AS/path trước và sau là gì?
advertisement/withdrawal xuất hiện lúc nào?
neighbor nào học route nào?
import/export policy nào áp dụng?
RIB chọn gì?
FIB install gì?
packet loss/latency/path từ nhiều vantage points ra sao?
```

Looking glass, tuyến (route / 경로) collector, router telemetry, luồng (flow / 흐름) logs, packet counters và endpoint probes là các nguồn bằng chứng (evidence / 증거) khác nhau. Không nguồn nào một mình là “sự thật toàn Internet”.

## 20. Worked sự cố (incident / 인시던트): more-specific tuyến (route / 경로) xuất hiện

Giả sử dịch vụ (service / 서비스) prefix `203.0.112.0/20` bình thường originate từ AS A. Đột nhiên một AS B announce `203.0.113.0/24` và nhiều networks chấp nhận.

Endpoint trong `/24` đi theo B do longest-prefix match. BGP session của A vẫn healthy; phần còn lại `/20` vẫn normal. Nếu chỉ nhìn overall dịch vụ (service / 서비스) availability, sự cố (incident / 인시던트) có thể trông regional/random.

Diagnosis cần prefix-level reachability và route-origin lịch sử (history / 이력). Containment có thể liên quan tuyến (route / 경로) filtering/RPKI/coordination với upstream; ứng dụng (application / 애플리케이션) thử lại (retry / 재시도) không sửa authority của routing điều khiển (control / 제어) plane.

## 21. Convergence pressure có thể trở thành CPU/bộ nhớ (memory / 메모리) pressure

Mass tuyến (route / 경로) churn tạo cập nhật (update / 업데이트) storms, chính sách (policy / 정책) evaluation tải (load / 로드), RIB/FIB programming pressure và telemetry volume. điều khiển (control / 제어) plane có thể chậm hơn đúng lúc mạng (network / 네트워크) đang cần hội tụ nhanh.

Đây là vòng phản hồi (feedback loop / 피드백 루프):

```text
failure/churn
→ route updates ↑
→ control-plane load ↑
→ convergence slower
→ inconsistency window kéo dài
```

Sức chứa (capacity / 용량) planning cho router/control-plane trạng thái (state / 상태) vì vậy là độ tin cậy (reliability / 신뢰성) concern.

## 22. Kết nối sang các chapter khác

BGP/routing nối trực tiếp với [HTTP/2, HTTP/3 và QUIC](../../basic/06_networks_distributed_systems/08_http2_http3_quic_and_modern_transport.md), [multi-region replication](./05_multi_region_replication_and_geo_distributed_tradeoffs.md), [load balancing/locality](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md) và [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng: **routing sự cố (incident / 인시던트) phải được gỡ lỗi (debug / 디버그) như một phân tán (distributed / 분산) chính sách (policy / 정책) máy trạng thái (state machine / 상태 머신): advertisement → chính sách (policy / 정책) → selected tuyến (route / 경로) → forwarding trạng thái (state / 상태) → observed traffic, không phải chỉ như “mạng chậm”.**

> **Bàn giao:** Sau **22. Kết nối sang các chapter khác**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 distributed transactions exactly once and failure semantics](./00_distributed_transactions_exactly_once_and_failure_semantics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
