# Kernel packet đường dẫn (path / 경로), qdisc, NIC offload và khả năng quan sát (observability / 관측 가능성)

Một yêu cầu (request / 요청) HTTP có thể chậm dù ứng dụng (application / 애플리케이션) không dùng nhiều CPU, cơ sở dữ liệu (database / 데이터베이스) ổn và mạng (network / 네트워크) giao diện (interface / 인터페이스) vẫn báo băng thông còn dư. Lý do là “mạng (network / 네트워크)” không phải một hop duy nhất. Packet đi qua nhiều hàng đợi (queue / 큐) và lớp trừu tượng (abstraction / 추상화): socket buffer, vận chuyển (transport / 전송) trạng thái (state / 상태), IP routing, firewall/chính sách (policy / 정책), traffic điều khiển (control / 제어), driver ring, NIC hàng đợi (queue / 큐), vật lý (physical / 물리적) link; chiều nhận đi theo chuỗi ngược lại với interrupt/NAPI, receive hàng đợi (queue / 큐) và socket wakeup.

Chapter này đặt kernel packet đường dẫn (path / 경로) trong ranh giới (boundary / 경계) Networks & Phân tán (distributed / 분산) Các hệ thống (systems / 시스템들) nhưng cross-link chặt với Operating Các hệ thống (systems / 시스템들). Mục tiêu không phải học tên từng Linux hàm (function / 함수). Mục tiêu là biết **packet đang chờ ở đâu, hàng đợi (queue / 큐) nào sở hữu nó, backpressure được truyền hay bị che ở đâu và offload nào làm bằng chứng (evidence / 증거) nhìn khác với wire reality**.

Mô hình tư duy (mental model / 사고 모델):

```text
application write
→ socket send buffer
→ TCP/UDP/IP state
→ routing / policy
→ qdisc / traffic control
→ driver TX ring
→ NIC hardware queue
→ wire

wire
→ NIC RX ring
→ interrupt / polling
→ kernel network stack
→ socket receive buffer
→ application read
```

Bất biến (invariant / 불변식) cơ bản là bytes/packets phải được xử lý theo ngữ nghĩa (semantics / 의미론) của giao thức (protocol / 프로토콜) và chính sách (policy / 정책), trong khi mỗi tầng giữ hàng đợi (queue / 큐) hữu hạn và có thể drop, delay, coalesce hoặc batch công việc (work / 작업).

## 1. Socket API che rất nhiều hàng đợi (queue / 큐)

Khi ứng dụng (application / 애플리케이션) gọi `send` hoặc `write`, việc lời gọi (call / 호출) trả về không đồng nghĩa peer đã nhận bytes. Thông thường dữ liệu mới được bản sao (copy / 복사) hoặc tham chiếu (reference / 참조) vào kernel-owned buffer và được vận chuyển (transport / 전송)/mạng (network / 네트워크) ngăn xếp (stack / 스택) xử lý tiếp.

Vì vậy cần phân biệt:

```text
application accepted bytes
≠ kernel transmitted packet
≠ NIC put frame on wire
≠ peer received bytes
≠ peer application consumed bytes
```

Một syscall nhanh chỉ chứng minh enqueue ở ranh giới (boundary / 경계) gần ứng dụng (application / 애플리케이션) diễn ra nhanh. Nó không chứng minh downstream không đang backlog.

## 2. Send buffer và receive buffer là flow-control ranh giới (boundary / 경계)

Socket send buffer hấp thụ burst giữa tốc độ producer của ứng dụng (application / 애플리케이션) và tốc độ mạng (network / 네트워크)/peer có thể nhận. Nếu downstream chậm, buffer đầy và ứng dụng (application / 애플리케이션) cuối cùng phải khối (block / 블록), nhận `EAGAIN` trong non-blocking chế độ (mode / 모드) hoặc thấy async ghi (write / 쓰기) không progress.

Receive buffer làm điều tương tự ở chiều vào. Nếu ứng dụng (application / 애플리케이션) đọc chậm, buffer tăng. Với TCP, advertised receive cửa sổ (window / 윈도우) có thể giảm để truyền backpressure tới sender. Với UDP, không có reliable stream luồng (flow / 흐름) điều khiển (control / 제어); receive hàng đợi (queue / 큐) đầy có thể dẫn tới drop.

Điểm quan trọng là buffer không tạo sức chứa (capacity / 용량) mới. Nó chỉ đổi **khi nào** pressure lộ ra.

## 3. TCP trạng thái (state / 상태) quyết định packet nào được phép gửi

TCP sender không chỉ nhìn socket buffer. Nó còn bị giới hạn bởi congestion cửa sổ (window / 윈도우), receive cửa sổ (window / 윈도우), pacing, retransmission trạng thái (state / 상태) và bytes đang in flight.

Có thể hình dung send permission gần đúng như:

```text
sendable ≈ min(congestion window, receive window) - in-flight data
```

Nếu congestion điều khiển (control / 제어) giảm cửa sổ (window / 윈도우) sau mất mát (loss / 손실)/ECN tín hiệu (signal / 신호), ứng dụng (application / 애플리케이션) có thể vẫn tiếp tục enqueue cho tới khi send buffer đầy. Đây tạo delay giữa mạng (network / 네트워크) congestion và application-visible backpressure.

Do đó thông lượng (throughput / 처리량) thấp với send buffer lớn chưa chắc là NIC bottleneck; có thể vận chuyển (transport / 전송) cố ý giới hạn flight kích thước (size / 크기).

## 4. Routing quyết định (decision / 결정) và chính sách (policy / 정책) không dừng ở bảng tuyến (route / 경로)

Sau khi packet có network-layer destination, kernel phải chọn tuyến (route / 경로), đầu ra (output / 출력) giao diện (interface / 인터페이스) và next hop theo routing/chính sách (policy / 정책) trạng thái (state / 상태). Không gian tên (namespace / 네임스페이스), VRF, chính sách (policy / 정책) routing, firewall/NAT hoặc tunnel có thể làm đường dẫn (path / 경로) khác trực giác “destination IP → giao diện (interface / 인터페이스)”.

BGP ở điều khiển (control / 제어) plane có thể quyết định tuyến (route / 경로) được học như thế nào, nhưng cục bộ (local / 로컬) kernel forwarding dùng trạng thái (state / 상태) đã được cài xuống routing/FIB. Vì vậy BGP session healthy không chứng minh host forwarding đúng; ngược lại packet đường dẫn (path / 경로) cục bộ (local / 로컬) có thể hỏng dù điều khiển (control / 제어) plane vẫn ổn.

Xem [BGP, routing policy và convergence](./07_bgp_routing_policy_convergence_and_route_security.md) để phân biệt advertisement/RIB/FIB với observed packet đường dẫn (path / 경로).

## 5. qdisc là queueing chính sách (policy / 정책) trước thiết bị (device / 장치)

**Queueing discipline (qdisc)** quyết định cách packet được xếp hàng, phân loại, pacing hoặc drop trước khi đi xuống thiết bị (device / 장치). Nó có thể rất đơn giản hoặc thực hiện scheduling/fairness/shaping phức tạp.

Mô hình tư duy (mental model / 사고 모델) không nên là “qdisc = một hàng đợi (queue / 큐)”. Qdisc là **chính sách (policy / 정책) trên backlog**. Nó trả lời packet nào được gửi tiếp, packet nào chờ, khi nào drop và luồng (flow / 흐름) nào được ưu tiên.

Nếu offered tải (load / 로드) vượt dịch vụ (service / 서비스) tỷ lệ (rate / 비율), backlog phải tăng hoặc packet phải bị drop. Không có queueing thuật toán (algorithm / 알고리즘) nào xóa định luật đó. Thuật toán (algorithm / 알고리즘) chỉ thay phân phối delay/drop giữa flows.

## 6. Bufferbloat là độ trễ (latency / 지연 시간) ẩn trong hàng đợi (queue / 큐)

Một buffer quá lớn có thể làm thông lượng (throughput / 처리량) trông tốt nhưng độ trễ (latency / 지연 시간) tăng mạnh. Khi bottleneck link phục vụ chậm hơn arrival tỷ lệ (rate / 비율), hàng đợi (queue / 큐) dài giữ packet thay vì drop sớm. Interactive traffic phải chờ sau bulk traffic.

Đây là **bufferbloat**: hệ thống dùng buffering để che overload, đổi packet mất mát (loss / 손실) thành queueing delay.

Bằng chứng (evidence / 증거) quan trọng không chỉ là giao diện (interface / 인터페이스) utilization mà là hàng đợi (queue / 큐) độ sâu (depth / 깊이)/sojourn thời gian (time / 시간), RTT inflation và drop/mark hành vi (behavior / 동작). Nếu RTT tăng cùng backlog trong khi link gần saturation, bottleneck có thể nằm ở hàng đợi (queue / 큐) trước link chứ không ở ứng dụng (application / 애플리케이션).

## 7. Driver ring và NIC hardware hàng đợi (queue / 큐)

Sau qdisc, driver thường đưa descriptors vào transmit ring. NIC đọc descriptors, DMA dữ liệu (data / 데이터) và gửi frame. Ở chiều nhận, NIC DMA packet vào receive buffers rồi kernel xử lý descriptors.

Ring là một hàng đợi (queue / 큐) khác. Nếu software producer nhanh hơn NIC, TX ring có thể đầy. Nếu NIC nhận nhanh hơn kernel drain, RX ring có thể overflow và packet bị drop trước khi giao thức (protocol / 프로토콜) ngăn xếp (stack / 스택) thấy nó.

Multi-queue NIC phân traffic qua nhiều hardware queues để quy mô (scale / 규모) trên nhiều CPU. RSS/băm (hash / 해시) chính sách (policy / 정책) và CPU affinity ảnh hưởng locality. Một hàng đợi (queue / 큐) có thể nóng trong khi aggregate giao diện (interface / 인터페이스) utilization chưa cao nếu luồng (flow / 흐름) phân phối (distribution / 분포) skew.

## 8. Interrupt, NAPI và polling sự đánh đổi (trade-off / 트레이드오프)

Nếu mỗi packet tạo một interrupt riêng ở packet tỷ lệ (rate / 비율) cao, CPU có thể bị interrupt storm. Kernel mạng (network / 네트워크) ngăn xếp (stack / 스택) thường dùng cơ chế kết hợp interrupt với polling/ngân sách (budget / 예산) để xử lý batch packet.

Batching tăng thông lượng (throughput / 처리량) vì amortize overhead nhưng có thể tăng độ trễ (latency / 지연 시간) cho packet chờ trong batch. Ngân sách (budget / 예산) quá nhỏ làm backlog không drain kịp; ngân sách (budget / 예산) quá lớn có thể để mạng (network / 네트워크) processing chiếm CPU lâu và làm ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) chậm được schedule.

Đây là cross-layer phản hồi (feedback / 피드백):

```text
packet rate tăng
→ softirq/poll work tăng
→ CPU time cho application giảm
→ application drain socket chậm
→ receive backlog tăng
→ latency/drop tăng
```

Mạng (network / 네트워크) bottleneck vì vậy có thể biểu hiện như CPU scheduling bài toán (problem / 문제).

## 9. Offload làm packet capture dễ bị hiểu sai

NIC/kernel có nhiều tối ưu hóa (optimization / 최적화) gom hoặc tách packet để giảm per-packet overhead. Ví dụ, transmit side có thể để kernel xử lý một buffer lớn rồi NIC chia thành nhiều frames; receive side có thể coalesce nhiều segments trước khi đưa lên ngăn xếp (stack / 스택).

Do đó packet capture ở host có thể thấy “packet” lớn hơn MTU hoặc segmentation khác wire. Đây không nhất thiết là lỗi giao thức (protocol / 프로토콜); có thể là vị trí capture nằm trước/after offload ranh giới (boundary / 경계).

Mô hình tư duy (mental model / 사고 모델) quan trọng:

```text
logical transport data
→ software segmentation/coalescing view
→ NIC offload transformation
→ wire frames
```

Khi gỡ lỗi (debug / 디버그) MTU, retransmission hoặc packet count, phải biết bằng chứng (evidence / 증거) được quan sát ở tầng (layer / 계층) nào.

## 10. Checksum offload và false alarm

Tương tự, packet capture trên sender có thể thấy checksum chưa hoàn chỉnh vì NIC sẽ tính checksum sau khi capture điểm (point / 지점) đã ghi packet. Nếu không hiểu offload ranh giới (boundary / 경계), engineer có thể kết luận sai rằng host đang phát packet corrupt.

Quy tắc (rule / 규칙) chung: **bằng chứng (evidence / 증거) trước hardware transformation không thể được diễn giải như wire bằng chứng (evidence / 증거) nếu transformation chưa xảy ra**.

## 11. GRO/GSO và thông lượng (throughput / 처리량)–độ trễ (latency / 지연 시간) sự đánh đổi (trade-off / 트레이드오프)

Generic segmentation/coalescing giúp giảm số lần ngăn xếp (stack / 스택) xử lý packet. Khi packet tỷ lệ (rate / 비율) cao, giảm per-packet overhead có thể tiết kiệm CPU đáng kể.

Nhưng batching/coalescing thay timing. Công việc (work / 작업) được gom lại rồi xử lý theo cụm. Với tải công việc (workload / 워크로드) cực nhạy độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) tối ưu hóa (optimization / 최적화) có thể làm tail hành vi (behavior / 동작) khác. Không nên tắt offload theo thói quen; cần hypothesis và đo lường (measurement / 측정) theo tải công việc (workload / 워크로드).

## 12. Drops có nhiều đơn vị sở hữu (owner / 오너) khác nhau

“Packet drop” không đủ để chẩn đoán. Drop có thể xảy ra vì RX ring overflow, qdisc chính sách (policy / 정책), firewall, tuyến (route / 경로)/chính sách (policy / 정책), socket receive hàng đợi (queue / 큐), vận chuyển (transport / 전송) kiểm tra hợp lệ (validation / 검증) hoặc thiết bị (device / 장치)/link.

Một counter tổng không cho biết đơn vị sở hữu (owner / 오너). Debugging phải đi theo chuyển tiếp trạng thái (state transition / 상태 전이):

```text
packet có tới NIC không?
→ có vào RX ring không?
→ kernel có poll/process không?
→ routing/policy có accept không?
→ transport có accept không?
→ socket queue có chỗ không?
→ application có drain không?
```

Mỗi câu hỏi cần bằng chứng (evidence / 증거) ở đúng ranh giới (boundary / 경계).

## 13. ECMP/RSS skew và hot luồng (flow / 흐름)

Hash-based phân phối (distribution / 분포) giả định nhiều flows đủ đa dạng. Nếu tải công việc (workload / 워크로드) chỉ có vài elephant flows, một hardware hàng đợi (queue / 큐) hoặc một đường dẫn (path / 경로) có thể nóng. Aggregate bandwidth 40% không loại trừ hàng đợi (queue / 큐) riêng lẻ 100%.

Điều này tương tự shard skew trong cơ sở dữ liệu (database / 데이터베이스) hoặc partition skew trong stream processing. Average che phân phối (distribution / 분포). Cần nhìn per-queue/per-flow/per-CPU cohort.

## 14. Liên kết (connection / 연결) pooling thay đổi packet đường dẫn (path / 경로) pressure

Ứng dụng (application / 애플리케이션) dùng liên kết (connection / 연결) pool giữ TCP connections lâu hơn, giảm handshake nhưng làm traffic tập trung trên ít luồng (flow / 흐름). Tùy RSS/ECMP băm (hash / 해시), điều này có thể giảm phân phối (distribution / 분포) entropy và tạo hot hàng đợi (queue / 큐)/đường dẫn (path / 경로).

Ngược lại mở quá nhiều liên kết (connection / 연결) tăng handshake/trạng thái (state / 상태), cổng (port / 포트)/NAT pressure và scheduler overhead. Vì vậy pool sizing không chỉ là ứng dụng (application / 애플리케이션) concern; nó có thể đổi mạng (network / 네트워크) hàng đợi (queue / 큐) phân phối (distribution / 분포).

Cross-link với [load balancing, connection pools và locality](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md).

## 15. eBPF/tracing nằm ở bằng chứng (evidence / 증거) ranh giới (boundary / 경계)

Khi cần nối syscall, scheduler và packet trạng thái (state / 상태), động (dynamic / 동적) kernel tracing có thể cung cấp bằng chứng (evidence / 증거) ở các hook cụ thể. Nhưng tracing cũng có overhead và sampling độ lệch (bias / 편향).

Xem [eBPF, tracing, kernel observability và safety boundary](../../03_operating_systems/advanced/08_ebpf_tracing_kernel_observability_and_safety.md). Điểm quan trọng không phải dùng công cụ (tool / 도구) nào mà là attach bằng chứng (evidence / 증거) vào đúng chuyển tiếp trạng thái (state transition / 상태 전이): enqueue, retransmit, qdisc delay, driver completion, receive/drop hay socket wakeup.

## 16. Worked lập luận (reasoning / 추론): độ trễ (latency / 지연 시간) tăng nhưng không có packet mất mát (loss / 손실) rõ ràng

Giả sử dịch vụ (service / 서비스) A gọi dịch vụ (service / 서비스) B, p99 tăng từ 20 ms lên 400 ms khi backup traffic chạy. CPU ứng dụng (application / 애플리케이션) chỉ 50%, retransmission không tăng đáng kể.

Ta không nên dừng ở “mạng (network / 네트워크) congestion”. Hãy kiểm tra:

```text
RTT tăng?
qdisc backlog/sojourn tăng?
interface/link utilization tăng?
per-queue utilization có skew?
socket send wait tăng?
softirq CPU tăng?
application runnable delay tăng?
```

Nếu RTT và qdisc backlog cùng tăng, bufferbloat/shaping là hypothesis mạnh. Nếu qdisc ổn nhưng một TX hàng đợi (queue / 큐) đầy, hardware hàng đợi (queue / 큐) skew hoặc driver đường dẫn (path / 경로) đáng nghi. Nếu softirq CPU tăng mạnh và ứng dụng (application / 애플리케이션) runnable nhưng không được schedule, bottleneck đã đi từ mạng (network / 네트워크) packet tỷ lệ (rate / 비율) sang CPU scheduling.

## 17. Lower layers quyết định hành vi (behavior / 동작)

Packet đường dẫn (path / 경로) dựa trên DMA, bộ nhớ đệm (cache / 캐시) locality, interrupt delivery, NUMA placement và thiết bị (device / 장치) hàng đợi (queue / 큐). Driver descriptors nằm trong bộ nhớ (memory / 메모리); NIC DMA qua IOMMU/thiết bị (device / 장치) ánh xạ (mapping / 매핑); CPU xử lý giao thức (protocol / 프로토콜) trạng thái (state / 상태) và bản sao (copy / 복사)/tham chiếu (reference / 참조) buffer. Vì vậy mạng (network / 네트워크) hiệu năng (performance / 성능) không tách khỏi kiến trúc (architecture / 아키텍처) và OS.

Cross-layer đường dẫn (path / 경로) hữu ích:

```text
flow distribution
→ NIC queue
→ CPU affinity / NUMA
→ softirq work
→ socket wakeup
→ application scheduler latency
→ request tail latency
```

Đây là lý do môi trường vận hành (production / 운영 환경) diagnosis cần nối Mạng (network / 네트워크) với [scheduler internals](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [I/O/DMA](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md) và [NUMA/interconnect](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).

## 18. Mô hình tư duy (mental model / 사고 모델) cuối

Kernel mạng (network / 네트워크) đường dẫn (path / 경로) là chuỗi hàng đợi (queue / 큐) + trạng thái (state / 상태) machines. Thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간) và drop là hệ quả của nơi arrival tỷ lệ (rate / 비율) vượt dịch vụ (service / 서비스) tỷ lệ (rate / 비율), nơi chính sách (policy / 정책) chủ động trì hoãn/drop, và nơi backpressure được truyền về ứng dụng (application / 애플리케이션).

Khi gỡ lỗi (debug / 디버그), không hỏi chung “mạng (network / 네트워크) có chậm không?”. Hãy hỏi: **packet đã tới ranh giới (boundary / 경계) nào, đang chờ trong hàng đợi (queue / 큐) nào, ai sở hữu hàng đợi (queue / 큐) đó, hàng đợi (queue / 큐) được drain bởi CPU/thiết bị (device / 장치) nào, offload nào biến đổi bằng chứng (evidence / 증거), và pressure có được phản hồi về producer hay đang bị buffer che đi?**