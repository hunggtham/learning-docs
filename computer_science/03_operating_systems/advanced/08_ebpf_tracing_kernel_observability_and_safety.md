# eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao tracing kernel khó** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Hook là nơi ngữ nghĩa (semantics / 의미론) được neo** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Khi ứng dụng (application / 애플리케이션) chậm, bằng chứng (evidence / 증거) ở người dùng (user / 사용자) không gian (space / 공간) thường chỉ cho thấy symptom: yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng, luồng thực thi (thread / 스레드) bị khối (block / 블록), syscall lâu hoặc packet biến mất. Muốn biết kernel thực sự làm gì, ta cần quan sát scheduler, syscall, mạng (network / 네트워크) đường dẫn (path / 경로), page fault, khối (block / 블록) I/O và nhiều chuyển tiếp trạng thái (state transition / 상태 전이) khác. Vấn đề là instrumentation trong kernel có thể làm crash máy hoặc thay đổi timing đủ lớn để phá chính hiện tượng đang đo.

**eBPF (extended Berkeley Packet Filter)** là một cơ chế cho phép chạy chương trình nhỏ trong các hook được kiểm soát, với xác minh (verification / 확인) và thời gian chạy (runtime / 런타임) các ràng buộc (constraints / 제약조건들) để biến kernel khả năng quan sát (observability / 관측 가능성) từ “patch kernel rồi reboot” thành một cơ chế động hơn.

Mô hình tư duy (mental model / 사고 모델):

```text
kernel event / hook
→ verified BPF program
→ bounded state access
→ map / ring buffer / counter
→ user-space collector
→ correlation với application evidence
```

Điểm cốt lõi không phải học công cụ (tool / 도구) command. Cần hiểu vì sao kernel cho phép mã (code / 코드) động chạy mà vẫn cố giữ an toàn (safety / 안전) bất biến (invariant / 불변식).

## 1. Vì sao tracing kernel khó

Kernel sở hữu address không gian (space / 공간) đặc quyền, scheduler, bộ nhớ (memory / 메모리) manager, thiết bị (device / 장치) và mạng (network / 네트워크) ngăn xếp (stack / 스택). Một null pointer, unbounded vòng lặp (loop / 루프) hoặc race trong instrumentation có thể ảnh hưởng toàn máy.

Traditional logging cũng có vấn đề. Nếu thêm log vào đường xử lý nóng (hot path / 핫 패스), formatting, allocation, khóa (lock / 잠금) và I/O có thể tạo overhead lớn. Khi sự kiện (event / 이벤트) tỷ lệ (rate / 비율) cao, log chuỗi xử lý (pipeline / 파이프라인) có thể trở thành bottleneck mới.

Khả năng quan sát (observability / 관측 가능성) vì vậy phải giữ hai bất biến (invariant / 불변식):

```text
instrumentation không được phá safety của kernel
instrumentation overhead phải đủ nhỏ để evidence còn đại diện workload thật
```

> **Chuyển mạch:** Kernel tracing khó vì timing và context; eBPF hook neo semantics vào điểm sự kiện, còn verifier là safety gate trước khi chương trình chạy trong kernel.

## 2. Hook là nơi ngữ nghĩa (semantics / 의미론) được neo

Một BPF program không chạy tùy ý mọi lúc. Nó được attach vào một hook: tracepoint, kprobe/kretprobe, perf sự kiện (event / 이벤트), socket/mạng (network / 네트워크) hook hoặc các attachment điểm (point / 지점) khác tùy subsystem.

Hook quyết định ngữ cảnh (context / 맥락) nào đang chạy, dữ liệu nào hợp lệ, helper nào được phép và độ trễ (latency / 지연 시간) ngân sách (budget / 예산) nào có thể chấp nhận. Instrumentation ở syscall entry trả lời câu hỏi khác instrumentation ở scheduler switch hoặc packet receive đường dẫn (path / 경로).

Vì vậy “có dấu vết (trace / 추적)” chưa đủ. Phải hỏi dấu vết (trace / 추적) được lấy ở **chuyển tiếp trạng thái (state transition / 상태 전이) nào**.

> **Chuyển mạch:** Ở chặng này của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **3. Verifier là an toàn (safety / 안전) gate** tiếp nhận điểm tựa từ **2. Hook là nơi ngữ nghĩa (semantics / 의미론) được neo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. JIT và thực thi (execution / 실행) chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Verifier là an toàn (safety / 안전) gate

Trước khi chương trình được tải (load / 로드), verifier phân tích điều khiển (control / 제어) luồng (flow / 흐름) và trạng thái (state / 상태) để từ chối những chương trình không chứng minh được an toàn (safety / 안전) theo quy tắc (rule / 규칙) của thời gian chạy (runtime / 런타임). Ý tưởng quan trọng là kernel không tin mã (code / 코드) chỉ vì người dùng có quyền tải (load / 로드) nó.

Verifier lập luận (reasoning / 추론) thường quan tâm tới pointer provenance, bounds, initialized trạng thái (state / 상태), helper đặc tả hợp đồng (contract / 계약) và khả năng termination. Với vòng lặp (loop / 루프), hệ thống cần một bound mà verifier có thể lập luận (reasoning / 추론) được; một vòng lặp không kiểm soát trong kernel hook có thể treo CPU.

Đây là một dạng **proof before thực thi (execution / 실행)**: không chứng minh mọi tính chất của chương trình, nhưng chứng minh đủ một tập bất biến (invariant / 불변식) để giảm lớp (class / 클래스) thất bại (failure / 실패) nguy hiểm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **4. JIT và thực thi (execution / 실행) chi phí (cost / 비용)** tiếp nhận điểm tựa từ **3. Verifier là an toàn (safety / 안전) gate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Maps: trạng thái (state / 상태) có kiểm soát giữa kernel và người dùng (user / 사용자) không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. JIT và thực thi (execution / 실행) chi phí (cost / 비용)

Sau xác minh (verification / 확인), hiện thực (implementation / 구현) có thể interpret hoặc JIT compile BPF bytecode xuống bản địa (native / 네이티브) instruction. JIT giảm overhead trên đường xử lý nóng (hot path / 핫 패스) nhưng không làm instrumentation miễn phí.

Mỗi sự kiện (event / 이벤트) vẫn có chi phí (cost / 비용): execute instructions, truy cập (access / 접근) map, bản sao (copy / 복사)/aggregate dữ liệu (data / 데이터), có thể wake bên tiêu thụ (consumer / 소비자). Nếu attach vào sự kiện (event / 이벤트) xảy ra hàng triệu lần mỗi giây, một program nhỏ vẫn tạo overhead đáng kể.

Do đó sampling và in-kernel aggregation thường tốt hơn emit mọi sự kiện (event / 이벤트). Nếu câu hỏi chỉ cần histogram độ trễ (latency / 지연 시간), việc cộng bucket tại kernel rồi đọc định kỳ thường rẻ hơn stream từng sự kiện (event / 이벤트) ra người dùng (user / 사용자) không gian (space / 공간).

> **Chuyển mạch:** Trong **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **5. Maps: trạng thái (state / 상태) có kiểm soát giữa kernel và người dùng (user / 사용자) không gian (space / 공간)** tiếp nhận điểm tựa từ **4. JIT và thực thi (execution / 실행) chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Ring buffer và sự kiện (event / 이벤트) vận chuyển (transport / 전송)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Maps: trạng thái (state / 상태) có kiểm soát giữa kernel và người dùng (user / 사용자) không gian (space / 공간)

BPF map là cơ chế lưu trạng thái (state / 상태) có cấu trúc. Nó có thể dùng cho counter, histogram, lookup bảng (table / 테이블), per-CPU trạng thái (state / 상태) hoặc correlation giữa entry/exit sự kiện (event / 이벤트).

Per-CPU map giảm contention vì mỗi CPU cập nhật trạng thái (state / 상태) riêng rồi aggregate sau. Đây là sự đánh đổi (trade-off / 트레이드오프) quen thuộc:

```text
ít synchronization ở write path
↔ cần merge state khi đọc
```

Map cũng tạo thời gian tồn tại (lifetime / 수명) và memory-pressure concern. Cardinality không giới hạn theo PID, liên kết (connection / 연결) hoặc key tùy ý có thể biến khả năng quan sát (observability / 관측 가능성) thành bộ nhớ (memory / 메모리) leak lô-gic (logic / 논리). Instrumentation phải có eviction/bound hoặc aggregation phù hợp.

> **Chuyển mạch:** Ở chặng này của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **6. Ring buffer và sự kiện (event / 이벤트) vận chuyển (transport / 전송)** tiếp nhận điểm tựa từ **5. Maps: trạng thái (state / 상태) có kiểm soát giữa kernel và người dùng (user / 사용자) không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. kprobe, tracepoint và stability đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Ring buffer và sự kiện (event / 이벤트) vận chuyển (transport / 전송)

Khi cần sự kiện (event / 이벤트) chi tiết, kernel phải chuyển dữ liệu (data / 데이터) sang người dùng (user / 사용자) không gian (space / 공간). Ring-buffer-like cơ chế (mechanism / 메커니즘) tránh allocation cho từng sự kiện (event / 이벤트) và cho phép producer/bên tiêu thụ (consumer / 소비자) giao tiếp hiệu quả hơn.

Nhưng buffer hữu hạn. Nếu producer nhanh hơn bên tiêu thụ (consumer / 소비자):

```text
arrival rate > drain rate
→ backlog
→ buffer full
→ event drop hoặc backpressure tùy mechanism
```

Dropped telemetry là một phần của ngữ nghĩa (semantics / 의미론). Nếu không đo drop count, ta có thể nhìn dấu vết (trace / 추적) “sạch” chỉ vì hệ thống mất bằng chứng (evidence / 증거) đúng lúc overload.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **7. kprobe, tracepoint và stability đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **6. Ring buffer và sự kiện (event / 이벤트) vận chuyển (transport / 전송)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. CO-RE và kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. kprobe, tracepoint và stability đặc tả hợp đồng (contract / 계약)

Động (dynamic / 동적) probe vào hàm (function / 함수) nội bộ linh hoạt nhưng phụ thuộc hiện thực (implementation / 구현) detail. Kernel phiên bản (version / 버전) đổi symbol, signature hoặc inlining có thể làm probe không còn mang ngữ nghĩa (semantics / 의미론) cũ.

Stable tracepoint thường có đặc tả hợp đồng (contract / 계약) rõ hơn nhưng ít vị trí hơn. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa coverage và tính tương thích (compatibility / 호환성).

Khi xây môi trường vận hành (production / 운영 환경) khả năng quan sát (observability / 관측 가능성) lâu dài, nên ưu tiên ngữ nghĩa (semantic / 의미적) attachment điểm (point / 지점) ổn định nếu có; probe hiện thực (implementation / 구현) detail phù hợp hơn cho investigation có kiểm soát.

> **Chuyển mạch:** Trong **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **7. kprobe, tracepoint và stability đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **8. CO-RE và kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. Scheduler tracing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. CO-RE và kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터)

Một challenge thực tế là kernel cấu trúc dữ liệu (data structure / 자료구조) thay đổi theo phiên bản (version / 버전)/cấu hình (configuration / 구성). Cơ chế kiểu BTF/CO-RE cho phép program dựa vào kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터) và relocation thay vì hard-code offset của trường dữ liệu (field / 필드).

Mô hình tư duy (mental model / 사고 모델) không phải “portable nhị phân (binary / 이진) tuyệt đối”, mà là:

```text
program expresses field/type intent
→ target kernel exposes type metadata
→ loader relocates access
→ verifier kiểm tra target-specific result
```

Tính tương thích (compatibility / 호환성) vẫn phải được kiểm thử (test / 테스트); siêu dữ liệu (metadata / 메타데이터) không xóa mọi ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경).

> **Chuyển mạch:** Ở chặng này của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **8. CO-RE và kiểu (type / 타입) siêu dữ liệu (metadata / 메타데이터)** nêu điều cần giải thích; **9. Scheduler tracing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. mạng (network / 네트워크) tracing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Scheduler tracing

Một yêu cầu (request / 요청) “đang chạy chậm” có thể thực ra không chạy. Scheduler bằng chứng (evidence / 증거) giúp phân biệt:

```text
on-CPU execution time
run-queue waiting time
sleep/block time
preemption/migration
```

Nếu wall-clock độ trễ (latency / 지연 시간) cao nhưng on-CPU thấp và run-queue delay cao, bottleneck nằm ở scheduling/sức chứa (capacity / 용량) hơn là đường đi mã (code path / 코드 경로). Nếu luồng thực thi (thread / 스레드) ngủ trên futex, cần quay lên synchronization đơn vị sở hữu (owner / 오너). Nếu blocked ở I/O, cần nối tới thiết bị (device / 장치)/filesystem bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **10. mạng (network / 네트워크) tracing** tiếp nhận điểm tựa từ **9. Scheduler tracing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Off-CPU profiling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. mạng (network / 네트워크) tracing

Packet đường dẫn (path / 경로) đi qua NIC, driver/NAPI-like receive processing, kernel networking, firewall/routing, socket hàng đợi (queue / 큐) rồi mới tới ứng dụng (application / 애플리케이션). Một hết thời gian chờ (timeout / 타임아웃) ở ứng dụng (application / 애플리케이션) không nói packet mất ở đâu.

Kernel khả năng quan sát (observability / 관측 가능성) có thể kiểm tra drop reason, hàng đợi (queue / 큐) occupancy, retransmission-related trạng thái (state / 상태), socket backlog hoặc độ trễ (latency / 지연 시간) giữa mạng (network / 네트워크) hook. Nhưng cần tránh biến mỗi packet thành một sự kiện (event / 이벤트) user-space ở traffic cao.

Đây là nơi eBPF kết nối trực tiếp với [BGP/routing policy](../../06_networks_distributed_systems/advanced/07_bgp_routing_policy_convergence_and_route_security.md) và vận chuyển (transport / 전송) bằng chứng (evidence / 증거): BGP giải thích tuyến (route / 경로) điều khiển (control / 제어) plane; kernel tracing giải thích packet thực tế đi qua host như thế nào.

### Packet vòng đời (lifecycle / 생명주기) và các hàng đợi (queue / 큐) ranh giới (boundary / 경계)

Một mô hình host-level đơn giản cho chiều vào là:

```text
NIC DMA / RX ring
→ driver + NAPI poll / softirq
→ packet representation (thường là skb, tùy hook)
→ XDP/tc/ingress processing
→ routing + firewall/netfilter
→ transport state (TCP/UDP)
→ socket receive queue
→ task wakeup
→ application read()
```

Chiều ra có các ranh giới (boundary / 경계) tương ứng:

```text
application write()
→ socket send buffer
→ TCP segmentation / UDP packetization
→ qdisc / egress policy
→ driver TX ring
→ NIC DMA / wire
```

Mỗi mũi tên có thể tạo hàng đợi (queue / 큐), drop hoặc delay. `read()` thành công chỉ chứng minh ứng dụng (application / 애플리케이션) đã lấy bytes khỏi socket hàng đợi (queue / 큐); nó không chứng minh packet vừa đến, cũng không cho biết bytes đã đi qua wire ở chiều ra. Tương tự, packet rời một hook ingress không chứng minh nó sẽ được deliver tới tiến trình (process / 프로세스).

Thứ tự chi tiết phụ thuộc driver, offload, không gian tên (namespace / 네임스페이스), kernel cấu hình (configuration / 구성) và hook kiểu (type / 타입). Vì vậy phải ghi rõ ngữ nghĩa (semantics / 의미론) của attachment điểm (point / 지점) thay vì vẽ một chuỗi xử lý (pipeline / 파이프라인) duy nhất rồi coi đó là mọi máy.

### GRO, GSO và offload làm thay đổi đơn vị quan sát

NIC và kernel có thể gộp nhiều packet thành một biểu diễn (representation / 표현) lớn ở receive đường dẫn (path / 경로) (GRO), hoặc trì hoãn segmentation tới driver/NIC ở transmit đường dẫn (path / 경로). Firewall, qdisc, TCP counters và user-space capture vì vậy có thể đếm các đơn vị khác nhau.

Một sự kiện (event / 이벤트) “packet” trong dấu vết (trace / 추적) không nhất thiết tương ứng một Ethernet frame trên wire. Nếu không biết tầng (layer / 계층) đang đếm gì, ta dễ kết luận sai về packet tỷ lệ (rate / 비율), MTU, retransmission hoặc chi phí (cost / 비용) per packet. Khi cần đối chiếu, ghi rõ:

```text
wire frame count
→ kernel aggregate/segment count
→ transport segment/byte count
→ socket read/write bytes
→ application message count
```

Offload cũng có thể làm dấu vết ngăn xếp (stack trace / 스택 트레이스) hoặc timestamp nằm ở điểm khác với intuition. Đây là lý do packet capture, NIC counters, kernel hook và ứng dụng (application / 애플리케이션) dấu vết (trace / 추적) nên được dùng như các bằng chứng (evidence / 증거) nguồn (source / 소스) độc lập, không trộn chúng thành một chỉ số (metric / 지표) “packets” duy nhất.

### Drop, delay và retransmission là ba hypothesis khác nhau

Khi yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃), tối thiểu phải tách:

```text
drop: packet bị loại ở một boundary
delay: packet còn sống nhưng chờ queue/processing
retransmission: transport không nhận ACK/response đúng hạn và gửi lại
```

Một retransmission counter tăng không tự chứng minh host đã drop packet; mất mát (loss / 손실) có thể xảy ra trên link, remote host, middlebox hoặc do ACK bị mất. Ngược lại, socket backlog đầy có thể tạo cục bộ (local / 로컬) drop trước khi TCP có cơ hội phản ứng như operator mong đợi.

Bằng chứng (evidence / 증거) hữu ích nên ghép theo cùng luồng (flow / 흐름)/liên kết (connection / 연결) và thời gian (time / 시간) cửa sổ (window / 윈도우):

```text
RX/TX ring và softirq work
→ ingress/egress drop reason
→ qdisc/socket backlog và queue age
→ TCP state, retransmission, RTT/RTO
→ wakeup/read/write delay
→ application span/message deadline
```

Nếu hàng đợi (queue / 큐) age tăng trước khi drop, sức chứa (capacity / 용량)/servicing là hypothesis mạnh. Nếu kernel đường dẫn (path / 경로) pass nhưng retransmission chỉ xuất hiện ở một link/vantage điểm (point / 지점), cần quay lên mạng (network / 네트워크) đường dẫn (path / 경로)/điều khiển (control / 제어) plane. Nếu socket có bytes nhưng tác vụ (task / 작업) không wake/read kịp, bottleneck có thể nằm ở scheduler hoặc ứng dụng (application / 애플리케이션) backpressure thay vì packet forwarding.

### Tracing packet đường dẫn (path / 경로) mà không biến tracing thành bottleneck

Packet-level tracing toàn bộ traffic thường không bền vững. Một workflow an toàn hơn là:

```text
flow/CPU/drop counters
→ sample connection hoặc namespace/CPU bị nghi
→ correlate queue boundary bằng flow identity
→ chỉ emit stack/event chi tiết cho một fraction nhỏ
→ kiểm tra event loss và instrumentation overhead
```

Khi dùng per-CPU maps, phải merge theo luồng (flow / 흐름)/CPU mà không tạo cardinality vô hạn. Khi dùng ring buffer, ghi drop counter và bên tiêu thụ (consumer / 소비자) lag cạnh sự kiện (event / 이벤트) count. Khi dấu vết (trace / 추적) bộ chứa (container / 컨테이너), cần giữ mạng (network / 네트워크) không gian tên (namespace / 네임스페이스), cgroup, pod/tác vụ (task / 작업) định danh (identity / 식별자) và giao diện (interface / 인터페이스) chỉ mục (index / 인덱스); thiếu một chiều định danh (identity / 식별자) có thể ghép nhầm hai luồng (flow / 흐름) giống tuple ở các không gian tên (namespace / 네임스페이스) khác nhau.

> **Chuyển mạch:** Trong **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **11. Off-CPU profiling** tiếp nhận điểm tựa từ **10. mạng (network / 네트워크) tracing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Observer tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Off-CPU profiling

CPU profiler truyền thống tập trung nơi chương trình đang execute. Nhiều môi trường vận hành (production / 운영 환경) độ trễ (latency / 지연 시간) lại đến từ thời gian **không chạy**: khóa (lock / 잠금) wait, scheduler wait, I/O sleep, page fault hoặc throttling.

Off-CPU profiling ghi lại ngăn xếp (stack / 스택)/ngữ cảnh (context / 맥락) khi tác vụ (task / 작업) bị deschedule và khi nó trở lại, từ đó gán waiting thời gian (time / 시간) về lời gọi (call / 호출) đường dẫn (path / 경로) gây khối (block / 블록). Nó giúp biến “dịch vụ (service / 서비스) chậm nhưng CPU thấp” thành hypothesis cụ thể.

> **Chuyển mạch:** Ở chặng này của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **12. Observer tác động (effect / 효과)** tiếp nhận điểm tựa từ **11. Off-CPU profiling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Observer tác động (effect / 효과)

Instrumentation có thể thay đổi hệ thống đang đo. sự kiện (event / 이벤트) emission dày làm bộ nhớ đệm (cache / 캐시) pressure tăng; ngăn xếp (stack / 스택) walking tốn CPU; map contention tạo khóa (lock / 잠금)/cache-line bouncing; user-space bên tiêu thụ (consumer / 소비자) cạnh tranh CPU với tải công việc (workload / 워크로드).

Do đó bằng chứng (evidence / 증거) phải kèm overhead ngân sách (budget / 예산). Một dấu vết (trace / 추적) chỉ xuất hiện khi bật tracing nặng có thể là sản phẩm tạo ra (artifact / 산출물).

Một workflow tốt là:

```text
cheap always-on counters
→ detect anomaly
→ targeted sampling
→ narrow high-detail tracing
→ disable/reduce sau khi có evidence
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **12. Observer tác động (effect / 효과)** đã nêu tiêu chí phân biệt, còn **13. ranh giới bảo mật (security boundary / 보안 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. ranh giới bảo mật (security boundary / 보안 경계)

BPF program có visibility rất mạnh vào kernel/ứng dụng (application / 애플리케이션) hành vi (behavior / 동작). Quyền tải (load / 로드)/attach vì thế là bảo mật (security / 보안) năng lực (capability / 역량), không chỉ khả năng quan sát (observability / 관측 가능성) permission. Một triển khai (deployment / 배포) sai quyền có thể tạo dữ liệu (data / 데이터) exposure hoặc mở attack surface.

Verifier giảm memory-safety rủi ro (risk / 위험) nhưng không thay authorization. Program hợp lệ về bộ nhớ (memory / 메모리) vẫn có thể thu thập dữ liệu nhạy cảm nếu principal được cấp năng lực (capability / 역량) quá rộng.

> **Chuyển mạch:** Trong **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **13. ranh giới bảo mật (security boundary / 보안 경계)** đã nêu tiêu chí phân biệt, còn **14. thất bại (failure / 실패) modes** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. bằng chứng vận hành (production evidence / 운영 증거) và workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. thất bại (failure / 실패) modes

**Telemetry mất mát (loss / 손실):** ring buffer đầy hoặc collector chậm làm mất sự kiện (event / 이벤트) đúng lúc overload.

**Cardinality explosion:** map key theo yêu cầu (request / 요청)/liên kết (connection / 연결) không bounded làm bộ nhớ (memory / 메모리) tăng.

**phiên bản (version / 버전) drift:** probe dựa hiện thực (implementation / 구현) detail không còn đúng sau kernel cập nhật (update / 업데이트).

**Instrumentation-induced độ trễ (latency / 지연 시간):** tracing quá dày làm tải công việc (workload / 워크로드) chậm rồi kết luận sai nguyên nhân.

**ngữ nghĩa (semantic / 의미적) misattachment:** hook nằm trước/ sau chuyển tiếp trạng thái (state transition / 상태 전이) khác với giả định, khiến timestamp/counter bị diễn giải sai.

**Privilege overreach:** khả năng quan sát (observability / 관측 가능성) tác nhân (agent / 에이전트) có năng lực (capability / 역량) kernel lớn hơn nhu cầu thực.

> **Chuyển mạch:** Ở chặng này của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **14. thất bại (failure / 실패) modes** nêu điều cần giải thích; **15. bằng chứng vận hành (production evidence / 운영 증거) và workflow** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Kết nối các tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. bằng chứng vận hành (production evidence / 운영 증거) và workflow

Khi điều tra sự cố (incident / 인시던트), bắt đầu từ bất biến (invariant / 불변식) và câu hỏi cụ thể. Ví dụ:

```text
request latency tăng
→ CPU hay waiting?
→ nếu waiting: scheduler, lock hay I/O?
→ nếu I/O: filesystem/device hay network?
→ chọn hook gần state transition cần chứng minh
→ thu evidence tối thiểu
→ correlate bằng timestamp/identity
```

Không attach hàng chục probe chỉ vì có thể. bằng chứng (evidence / 증거) càng nhiều càng tăng overhead và ambiguity.

Các tín hiệu (signal / 신호) quan trọng gồm sự kiện (event / 이벤트)/drop count, map occupancy, per-CPU skew, run-queue delay, off-CPU duration, syscall độ trễ (latency / 지연 시간), page-fault độ trễ (latency / 지연 시간), mạng (network / 네트워크)/socket hàng đợi (queue / 큐) và correlation với ứng dụng (application / 애플리케이션) dấu vết (trace / 추적).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **eBPF, tracing, kernel khả năng quan sát (observability / 관측 가능성) và an toàn (safety / 안전) ranh giới (boundary / 경계)**, **15. bằng chứng vận hành (production evidence / 운영 증거) và workflow** nêu điều cần giải thích; **16. Kết nối các tầng (layer / 계층)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 16. Kết nối các tầng (layer / 계층)

Chapter này nối [kernel execution context](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [async I/O/DMA](./05_epoll_io_uring_zero_copy_and_dma.md) và [debugging across abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Lập luận (reasoning / 추론) đường dẫn (path / 경로) cuối cùng là:

```text
symptom ở application
→ hypothesis về kernel state transition
→ attachment point đúng semantics
→ verified low-overhead instrumentation
→ bounded evidence transport
→ correlation
→ lower-layer cause hoặc hypothesis bị bác bỏ
```

Giá trị của eBPF không nằm ở việc có thêm một công cụ (tool / 도구), mà ở khả năng đưa **state-transition bằng chứng (evidence / 증거)** từ kernel vào cùng lập luận (reasoning / 추론) chuỗi (chain / 사슬) với thời gian chạy (runtime / 런타임), cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) và dịch vụ (service / 서비스).

> **Bàn giao:** Sau **16. Kết nối các tầng (layer / 계층)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
