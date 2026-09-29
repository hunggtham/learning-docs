# Advanced I/O: epoll, io_uring, zero-copy và DMA

> **Mạch đọc:** Đặt **Advanced I/O: epoll, iouring, zero-copy và DMA** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Bài toán ban đầu: nhiều logical operations hơn số thực thi (execution / 실행) threads** sang **2. Readiness và completion là hai đặc tả hợp đồng (contract / 계약) khác nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


I/O hiệu năng (performance / 성능) không chỉ phụ thuộc thiết bị (device / 장치) nhanh hay chậm. Nó phụ thuộc cách ứng dụng (application / 애플리케이션) biểu diễn tính đồng thời (concurrency / 동시성), số lần chuyển người dùng (user / 사용자)/kernel, số copies, hàng đợi (queue / 큐) độ sâu (depth / 깊이), quyền sở hữu (ownership / 소유권) của buffers và việc ứng dụng (application / 애플리케이션) biết một thao tác (operation / 연산) **sẵn sàng** hay **đã hoàn tất** bằng cách nào.

Mô hình tư duy (mental model / 사고 모델) trung tâm là: **async I/O đổi cách chờ và cách giữ operations in-flight; nó không tạo thêm bandwidth vật lý.** Khi tính đồng thời (concurrency / 동시성) tăng, tính đúng đắn (correctness / 정확성) phải giữ thời gian tồn tại (lifetime / 수명)/quyền sở hữu (ownership / 소유권) của fd và buffers, còn hiệu năng (performance / 성능) phải giữ hàng đợi (queue / 큐) debt trong giới hạn downstream xử lý được.

## 1. Bài toán ban đầu: nhiều logical operations hơn số thực thi (execution / 실행) threads

Một blocking `read()` đơn giản và dễ lập luận (reasoning / 추론): luồng thực thi (thread / 스레드) ngủ tới khi có dữ liệu (data / 데이터). Với số liên kết (connection / 연결) nhỏ, mô hình (model / 모델) này có thể hoàn toàn tốt. Khi có hàng chục nghìn sockets hoặc nhiều lưu trữ (storage / 저장소) operations chờ đồng thời, one-thread-per-operation tạo ngăn xếp (stack / 스택) bộ nhớ (memory / 메모리), scheduler overhead và ngữ cảnh (context / 맥락) switches không cần thiết.

Non-blocking/async I/O tách:

```text
logical operation đang tồn tại
≠
OS thread phải đứng yên chờ operation đó
```

Đây là bất biến (invariant / 불변식) tài nguyên, không phải lời hứa rằng mỗi thao tác (operation / 연산) sẽ nhanh hơn.

## 2. Readiness và completion là hai đặc tả hợp đồng (contract / 계약) khác nhau

**Readiness mô hình (model / 모델)** báo rằng một fd *có khả năng* thực hiện thao tác (operation / 연산) mà không khối (block / 블록) theo điều kiện hiện tại. `epoll`/`kqueue` thuộc family này.

**Completion mô hình (model / 모델)** báo rằng thao tác (operation / 연산) đã được submit và kernel/thời gian chạy (runtime / 런타임) trả completion khi nó kết thúc. `io_uring`, IOCP và nhiều async lưu trữ (storage / 저장소) APIs thuộc family này ở mức lớp trừu tượng (abstraction / 추상화) khác nhau.

```text
readiness:
ready event → application gọi read/write → operation có thể partial

completion:
submit operation → kernel/device xử lý → completion event/result
```

Nhầm hai mô hình (model / 모델) tạo bug: “socket writable” không nghĩa toàn buffer đã gửi; “completion nhận được” mới là ranh giới (boundary / 경계) cho thao tác (operation / 연산) cụ thể đã submit.

## 3. `select`/`poll` tới `epoll`/`kqueue`: giữ interest trạng thái (state / 상태) ở đâu?

`select`/`poll` thường yêu cầu ứng dụng (application / 애플리케이션) đưa tập descriptors vào kernel và scan kết quả lặp lại. `epoll`/`kqueue` giữ registration/interest trạng thái (state / 상태) phía kernel và trả các events liên quan, giảm overhead khi tập fd rất lớn nhưng chỉ ít fd active.

Bất biến (invariant / 불변식) không phải “epoll luôn O(1) và nhanh”. chi phí (cost / 비용) vẫn phụ thuộc sự kiện (event / 이벤트) tỷ lệ (rate / 비율), wakeups, tranh chấp khóa (lock contention / 잠금 경합), bộ nhớ đệm (cache / 캐시) locality và ứng dụng (application / 애플리케이션) xử lý sự kiện (event / 이벤트) thế nào.

Một vòng lặp sự kiện (event loop / 이벤트 루프) vẫn phải xử lý partial read/ghi (write / 쓰기), `EAGAIN`-like conditions, closed peer và fd vòng đời (lifecycle / 생명주기) chính xác.

## 4. Level-triggered và edge-triggered thay đổi giao thức (protocol / 프로토콜) đọc sự kiện (event / 이벤트)

Với level-triggered ngữ nghĩa (semantics / 의미론), sự kiện (event / 이벤트) có thể tiếp tục được báo khi điều kiện (condition / 조건) còn đúng. Với edge-triggered ngữ nghĩa (semantics / 의미론), ứng dụng (application / 애플리케이션) thường phải **drain** tài nguyên (resource / 자원) tới trạng thái “không còn làm tiếp được” trước khi chờ edge mới.

Thất bại (failure / 실패) điển hình:

```text
edge arrives
→ application đọc chỉ một phần
→ data vẫn còn nhưng app không drain
→ không có state transition mới để tạo edge tiếp
→ connection trông như “treo”
```

Đây là giao thức (protocol / 프로토콜) bug ở ứng dụng (application / 애플리케이션), không phải kernel đánh mất packet.

## 5. Partial I/O là normal hành vi (behavior / 동작), không phải rare lỗi (error / 오류)

`read` có thể trả ít bytes hơn message lô-gic (logic / 논리); `write` có thể chỉ accept một phần buffer. TCP là byte stream nên ứng dụng (application / 애플리케이션) phải giữ framing/trạng thái (state / 상태) riêng.

Một robust vòng lặp sự kiện (event loop / 이벤트 루프) cần máy trạng thái (state machine / 상태 머신):

```text
bytes expected
bytes received/sent
buffer ownership
current protocol state
deadline/cancellation
```

Nếu mã (code / 코드) giả định “một ghi (write / 쓰기) gửi cả phản hồi (response / 응답)”, bug sẽ chỉ xuất hiện dưới pressure khi socket buffer đầy hơn—đúng lúc môi trường vận hành (production / 운영 환경) khác cục bộ (local / 로컬) kiểm thử (test / 테스트).

## 6. FD vòng đời (lifecycle / 생명주기) và stale sự kiện (event / 이벤트) race

Tệp (file / 파일) descriptor là một integer handle có thể được kernel tái sử dụng sau close. Nếu ứng dụng (application / 애플리케이션) giữ sự kiện (event / 이벤트) cũ rồi descriptor number được cấp lại cho liên kết (connection / 연결) khác, xử lý sự kiện (event / 이벤트) stale theo chỉ số fd đơn thuần có thể tác động nhầm đối tượng (object / 객체).

Thời gian chạy (runtime / 런타임) thường cần generation/đơn vị từ (token / 토큰) hoặc đối tượng (object / 객체) định danh (identity / 식별자)/vòng đời (lifecycle / 생명주기) quy tắc (rule / 규칙) rõ. bất biến (invariant / 불변식) là:

> Một completion/readiness sự kiện (event / 이벤트) chỉ được áp dụng cho logical tài nguyên (resource / 자원) đã tạo registration/thao tác (operation / 연산) đó, không phải bất kỳ tài nguyên (resource / 자원) mới nào tình cờ có cùng integer handle.

Đây là cùng family với ABA: định danh (identity / 식별자) và thời gian tồn tại (lifetime / 수명) không thể suy ra chỉ từ bit mẫu (pattern / 패턴) của handle.

## 7. `io_uring`: submission/completion rings đổi syscall đường dẫn (path / 경로), không đổi sức chứa (capacity / 용량)

`io_uring` dùng dùng chung (shared / 공유) ring structures để người dùng (user / 사용자) không gian (space / 공간) submit operations và kernel trả completion. Batching submission/completion có thể amortize syscall/chuyển tiếp (transition / 전이) chi phí (cost / 비용) và giữ nhiều operations in-flight.

Simplified:

```text
prepare SQ entries
→ publish to submission ring
→ kernel consumes
→ operation waits/runs through subsystem/device
→ CQ entry appears
→ application reaps completion
```

Tính đúng đắn (correctness / 정확성) cần quyền sở hữu (ownership / 소유권) rõ: entry nào thuộc thao tác (operation / 연산) nào, buffer còn sống tới khi nào, cancellation/hết thời gian chờ (timeout / 타임아웃) race với completion ra sao.

## 8. hàng đợi (queue / 큐) độ sâu (depth / 깊이): quá ít thì thiết bị (device / 장치) idle, quá nhiều thì tail độ trễ (latency / 지연 시간) phình

Lưu trữ (storage / 저장소)/NIC thường cần nhiều requests in-flight để đạt thông lượng (throughput / 처리량). Nhưng hàng đợi (queue / 큐) sâu tạo waiting thời gian (time / 시간) và giữ nhiều bộ nhớ (memory / 메모리)/trạng thái (state / 상태) hơn.

```text
queue depth thấp quá
→ pipeline/device không đủ work
→ utilization thấp

queue depth cao quá
→ waiting time + memory + tail latency tăng
→ cancellation làm nhiều zombie work
```

Điểm tối ưu phụ thuộc thiết bị (device / 장치), tải công việc (workload / 워크로드), yêu cầu (request / 요청) kích thước (size / 크기) và SLO. Async API không thay định luật queueing.

## 9. Cancellation là một chuyển tiếp trạng thái (state transition / 상태 전이), không phải xóa lịch sử thao tác (operation / 연산)

Khi cancel một async thao tác (operation / 연산), có race:

```text
operation chưa bắt đầu
operation đang chạy
operation vừa complete nhưng completion chưa được reap
cancel request đang đến
```

Ứng dụng (application / 애플리케이션) phải chấp nhận ngữ nghĩa (semantics / 의미론) mà API cung cấp: cancellation có thể thành công, thất bại (fail / 실패) vì thao tác (operation / 연산) đã hoàn thành, hoặc completion vẫn phải được consume để giải phóng tài nguyên (resource / 자원).

Bất biến (invariant / 불변식) quan trọng là buffer/tài nguyên (resource / 자원) chỉ được free/reuse sau ranh giới (boundary / 경계) mà API bảo đảm kernel/thiết bị (device / 장치) không còn truy cập nó.

## 10. Registered/pinned buffers đổi syscall/bản sao (copy / 복사) chi phí (cost / 비용) thành thời gian tồn tại (lifetime / 수명) chi phí (cost / 비용)

Một số async mechanisms cho phép register hoặc pin buffers để giảm repeated ánh xạ (mapping / 매핑)/setup. hiệu năng (performance / 성능) tốt hơn nhưng bộ nhớ (memory / 메모리) đó ít linh hoạt hơn với allocator/reclaim và quyền sở hữu (ownership / 소유권) giao thức (protocol / 프로토콜) phức tạp hơn.

Nếu buffer được tái sử dụng trước completion, DMA/kernel có thể ghi vào bộ nhớ (memory / 메모리) hiện đã thuộc logical yêu cầu (request / 요청) khác. Đây là tính đúng đắn (correctness / 정확성) bug do thời gian tồn tại (lifetime / 수명), không phải “dữ liệu (data / 데이터) corruption ngẫu nhiên”.

## 11. DMA: CPU không bản sao (copy / 복사) từng byte nhưng vẫn quản lý giao thức (protocol / 프로토콜)

**Direct bộ nhớ (memory / 메모리) truy cập (access / 접근) (DMA)** cho thiết bị (device / 장치) truyền dữ liệu (data / 데이터) tới/from RAM mà CPU không phải thực hiện từng tải (load / 로드)/store. CPU vẫn thiết lập descriptors, mappings, queues và xử lý completion.

IOMMU tạo address-translation/isolation ranh giới (boundary / 경계) cho DMA để thiết bị (device / 장치) không có quyền truy cập arbitrary vật lý (physical / 물리적) bộ nhớ (memory / 메모리). Vì vậy hiệu năng (performance / 성능) đường dẫn (path / 경로) đi cùng bảo mật (security / 보안)/isolation đường dẫn (path / 경로):

```text
user buffer
→ kernel mapping/pinning
→ DMA descriptor
→ IOMMU translation
→ device transfer
→ completion
```

Lower lớp trừu tượng (abstraction / 추상화) quyết định độ trễ (latency / 지연 시간) có thể là IOMMU/TLB, PCIe/interconnect hoặc thiết bị (device / 장치) hàng đợi (queue / 큐), không phải user-space hàm (function / 함수).

## 12. Zero-copy là giảm copies, không phải “dữ liệu (data / 데이터) không di chuyển”

“Zero-copy” thường nghĩa loại bỏ một hoặc nhiều copies giữa layers. `sendfile`, splice-like paths, bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑) hoặc NIC offloads có thể tránh user-buffer → kernel-buffer bản sao (copy / 복사) trong một số workloads.

Nhưng dữ liệu (data / 데이터) vẫn di chuyển qua bộ nhớ (memory / 메모리)/interconnect/NIC. bất biến (invariant / 불변식) mới xuất hiện: buffer/page phải sống đủ lâu và không bị mutate sai lúc thiết bị (device / 장치)/kernel còn tham chiếu (reference / 참조).

Zero-copy có lợi khi bản sao (copy / 복사) + bộ nhớ (memory / 메모리) bandwidth là bottleneck; với payload nhỏ, setup/thời gian tồn tại (lifetime / 수명) độ phức tạp (complexity / 복잡도) có thể lớn hơn lợi ích.

## 13. Interrupt, interrupt moderation và polling là sự đánh đổi (trade-off / 트레이드오프) độ trễ (latency / 지연 시간)–thông lượng (throughput / 처리량)–CPU

Interrupt phù hợp sự kiện (event / 이벤트) thưa: CPU làm việc khác rồi được đánh thức. Ở packet tỷ lệ (rate / 비율) cao, một interrupt mỗi sự kiện (event / 이벤트) có overhead lớn; hệ thống có thể coalesce/moderate interrupts hoặc chuyển sang polling/batched processing.

Busy-poll có thể giảm wakeup độ trễ (latency / 지연 시간) nhưng dùng CPU ngay cả khi ít công việc (work / 작업). Không có chế độ (mode / 모드) “luôn nhanh nhất”; tải công việc (workload / 워크로드) thay đổi thì operating điểm (point / 지점) tối ưu cũng thay đổi.

## 14. vòng lặp sự kiện (event loop / 이벤트 루프) vẫn có thể bị starvation

Non-blocking socket không giúp nếu callback chạy CPU-heavy 100 ms trên single event-loop luồng thực thi (thread / 스레드). Trong lúc đó hàng nghìn connections ready nhưng không được dịch vụ (service / 서비스).

Bằng chứng (evidence / 증거) phải tách:

```text
kernel/device wait
runtime ready-queue wait
on-CPU callback time
GC/runtime pause
network/storage service time
```

CPU toàn máy có thể chỉ 20% trên máy nhiều cốt lõi (core / 핵심) nhưng một event-loop cốt lõi (core / 핵심) đã saturated.

## 15. Backpressure phải bắt đầu trước khi buffers đầy

Event-driven máy chủ (server / 서버) có thể accept/read công việc (work / 작업) nhanh hơn downstream xử lý. Nếu mọi socket được drain vào unbounded user-space hàng đợi (queue / 큐), tiến trình (process / 프로세스) chỉ chuyển hàng đợi (queue / 큐) từ kernel sang vùng nhớ động (heap / 힙).

Nhân quả (causal / 인과적) vòng lặp (loop / 루프):

```text
arrival > service capacity
→ user queue grows
→ memory + latency grow
→ deadlines expire
→ clients retry
→ arrival grows further
→ OOM/cascading failure
```

Bounded queues, per-connection/per-tenant limits, luồng (flow / 흐름) điều khiển (control / 제어), semaphore/admission điều khiển (control / 제어) và stop-reading chiến lược (strategy / 전략) là các cách biểu diễn sức chứa (capacity / 용량). Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 16. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) đổi phase

Ở low tính đồng thời (concurrency / 동시성), syscall/bản sao (copy / 복사) overhead có thể negligible. Khi QPS tăng, chuyển tiếp (transition / 전이)/bản sao (copy / 복사)/bộ nhớ đệm (cache / 캐시) pollution trở nên đáng kể; batching và async giúp thông lượng (throughput / 처리량). Khi tính đồng thời (concurrency / 동시성) tiếp tục tăng, hàng đợi (queue / 큐) wait và bộ nhớ (memory / 메모리) pressure lại dominate.

Vì vậy “io_uring nhanh hơn epoll” không phải universal conclusion. Hai các mô hình (models / 모델들) phù hợp thao tác (operation / 연산) mix khác nhau; benchmark phải giữ yêu cầu (request / 요청) kích thước (size / 크기), tính đồng thời (concurrency / 동시성), hàng đợi (queue / 큐) độ sâu (depth / 깊이), CPU pinning, thiết bị (device / 장치)/mạng (network / 네트워크) conditions và SLO tương đồng.

## 17. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) hữu ích theo tầng:

```text
Application/runtime:
- event-loop lag / ready-queue wait
- active operations, queue depth, cancellation/timeout
- buffer pool / allocator pressure
- syscall rate và batch size

OS:
- runnable vs blocked/off-CPU time
- context switch / wakeup rate
- fd/socket state, send/receive queue
- I/O scheduler/block queue latency

Hardware/device:
- NIC/storage queue depth
- interrupt/poll rate
- throughput, packet/drop/retransmission hoặc device errors
- memory bandwidth / NUMA locality khi copy path nghi ngờ
```

Một flame đồ thị (graph / 그래프) on-CPU không giải thích thời gian đang nằm trong thiết bị (device / 장치) hàng đợi (queue / 큐); một lưu trữ (storage / 저장소) độ trễ (latency / 지연 시간) đồ thị (graph / 그래프) không giải thích event-loop starvation. Cần nhân quả (causal / 인과적) timeline xuyên layers.

## 18. thất bại (failure / 실패) lập luận (reasoning / 추론) theo lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층)

Nếu fd “ready nhưng không chạy tiếp”, kiểm tra edge-triggered drain/vòng đời (lifecycle / 생명주기) trước khi nghi kernel. Nếu dữ liệu (data / 데이터) bị ghi vào yêu cầu (request / 요청) sai, kiểm tra buffer/fd định danh (identity / 식별자) và late completion. Nếu thông lượng (throughput / 처리량) thấp nhưng thiết bị (device / 장치) idle, xem hàng đợi (queue / 큐) độ sâu (depth / 깊이)/submission batching. Nếu p99 tăng khi QPS cao, xem hàng đợi (queue / 큐)/backpressure trước khi chỉ tối ưu syscall.

## 19. Mô hình tư duy

> Advanced I/O là bài toán **quyền sở hữu (ownership / 소유권) + queues + completion ngữ nghĩa (semantics / 의미론)**. Readiness cho biết lúc nào nên thử; completion cho biết thao tác (operation / 연산) nào đã kết thúc; DMA/zero-copy giảm CPU/bản sao (copy / 복사) chi phí (cost / 비용) nhưng làm buffer thời gian tồn tại (lifetime / 수명) quan trọng hơn; async giữ chuỗi xử lý (pipeline / 파이프라인) đầy nhưng không tạo sức chứa (capacity / 용량). **Khi tính đồng thời (concurrency / 동시성) tăng, backpressure quyết định hệ thống còn ổn định hay chỉ tích lũy công việc (work / 작업) nhanh hơn.**

## Kết nối

Ôn [OS async I/O foundation](../../basic/03_operating_systems/07_boot_device_drivers_and_async_io.md), [runtime coroutine/event loop](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel execution contexts and syscall path](./00_kernel_execution_contexts_and_syscall_path.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
