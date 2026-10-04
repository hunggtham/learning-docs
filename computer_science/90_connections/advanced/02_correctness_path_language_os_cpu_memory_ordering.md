# Đường đi của tính đúng đắn: CPU bộ nhớ đệm (cache / 캐시) → bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) → ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) → tính đồng thời (concurrency / 동시성) bug

> **Mạch đọc:** [README](./README.md) là owner của tuyến correctness nâng cao. File tách ba lớp thường bị trộn lẫn—coherence của cache, ordering của hardware/ISA và happens-before của ngôn ngữ—rồi nối chúng với publication, atomicity, false sharing và bằng chứng vận hành.


Lỗi đồng thời thường bị rút gọn thành câu “CPU reorder instruction”. Cách giải thích đó quá thấp tầng để sửa mã (code / 코드) và cũng quá đơn giản để giải thích hành vi (behavior / 동작) thật. Tính đúng đắn của chương trình concurrent là một hợp đồng xuyên nhiều lớp trừu tượng (abstraction / 추상화): mã nguồn (source code / 소스 코드) → mô hình bộ nhớ của ngôn ngữ (language memory model) → trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) → thành phần nguyên thủy (primitive / 기본 요소) đồng bộ của OS → ISA và bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) → bộ nhớ đệm (cache / 캐시)/coherence → phần cứng thật.

Điểm quan trọng không phải nhớ từng fence instruction. Ta cần biết **bất biến (invariant / 불변식) nào mỗi tầng phải giữ**, tầng nào được phép reorder, và bằng chứng (evidence / 증거) nào chứng minh đặc tả hợp đồng (contract / 계약) đã bị vi phạm.

## 1. Bài toán ban đầu: nhiều thực thi (execution / 실행) ngữ cảnh (context / 맥락) cùng nhìn một trạng thái (state / 상태)

Khi hai threads truy cập cùng trạng thái (state / 상태), ta muốn một số thuộc tính (property / 속성) như:

```text
không có hai owner cùng giữ lock
reader chỉ thấy object sau khi object đã được khởi tạo hợp lệ
counter không mất update
state machine không đi qua trạng thái bất hợp lệ
```

Các thuộc tính (property / 속성) này là bất biến (invariant / 불변식) của chương trình. “luồng thực thi (thread / 스레드) A chạy trước luồng thực thi (thread / 스레드) B trong lần kiểm thử (test / 테스트) của tôi” không phải bất biến (invariant / 불변식), vì scheduler có thể interleave khác và hardware có thể làm visibility khác intuition source-order.

Do đó tính đồng thời (concurrency / 동시성) tính đúng đắn (correctness / 정확성) phải được chứng minh bằng **thứ tự (ordering / 순서) edge** và **quyền sở hữu (ownership / 소유권) quy tắc (rule / 규칙)**, không bằng timing.

## 2. bộ nhớ đệm (cache / 캐시) coherence không tạo ra language-level tính đúng đắn (correctness / 정확성)

Nhất quán bộ nhớ đệm (cache / 캐시) chủ yếu giải quyết một location: các cốt lõi (core / 핵심) phải hội tụ về một thứ tự hợp lệ của writes trên cùng bộ nhớ đệm (cache / 캐시) line. MESI/MOESI và interconnect giao thức (protocol / 프로토콜) quản lý quyền sở hữu (ownership / 소유권), vô hiệu hóa (invalidation / 무효화) và transfer của bộ nhớ đệm (cache / 캐시) lines.

Nhưng chương trình thường phụ thuộc nhiều locations:

```text
payload = 42
ready = true
```

Reader muốn suy luận rằng nếu thấy `ready == true` thì cũng phải thấy `payload == 42`. Coherence riêng lẻ của `ready` và `payload` không tạo ra quan hệ đó. Đây là lý do phải tách:

```text
coherence     -> một location được quan sát nhất quán ra sao
memory order  -> nhiều memory operations được phép xuất hiện theo thứ tự nào
synchronization -> software tạo ordering guarantee bằng cách nào
```

## 3. Vì sao hardware muốn reorder?

CPU hiện đại che độ trễ (latency / 지연 시간) bằng out-of-order thực thi (execution / 실행), store buffer, invalidate hàng đợi (queue / 큐), speculative thực thi (execution / 실행) và nhiều outstanding bộ nhớ (memory / 메모리) operations. Một store có thể được đặt vào store buffer để cốt lõi (core / 핵심) tiếp tục chạy trước khi ghi (write / 쓰기) đã globally visible. Một tải (load / 로드) độc lập có thể hoàn thành trong khi store cũ hơn còn chờ quyền sở hữu (ownership / 소유권) của bộ nhớ đệm (cache / 캐시) line.

Hiệu năng (performance / 성능) pressure vì thế đẩy hardware tới hành vi (behavior / 동작) yếu hơn intuition “mỗi instruction hoàn tất tuần tự”. Nếu bắt mọi cốt lõi (core / 핵심) chờ mọi ghi (write / 쓰기) visible toàn hệ thống trước khi đi tiếp, thông lượng (throughput / 처리량) và khả năng che bộ nhớ (memory / 메모리) độ trễ (latency / 지연 시간) sẽ giảm mạnh.

Bất biến (invariant / 불변식) của hardware không phải “mọi cốt lõi (core / 핵심) thấy mọi ghi (write / 쓰기) ngay lập tức”. bất biến (invariant / 불변식) là **mọi hành vi (behavior / 동작) phải nằm trong bộ nhớ (memory / 메모리) mô hình (model / 모델) của ISA**, và các thành phần nguyên thủy (primitive / 기본 요소) thứ tự (ordering / 순서) phải có ngữ nghĩa (semantics / 의미론) mà trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) có thể dựa vào.

Đọc sâu hơn tại [Memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md).

> **Nối mạch:** Cache coherence chỉ đảm bảo từng line; quan hệ giữa nhiều biến còn phụ thuộc compiler reordering và memory model của ngôn ngữ, nên correctness phải đi qua cả hai tầng.

## 4. trình biên dịch (compiler / 컴파일러) cũng reorder, nhưng theo đặc tả hợp đồng (contract / 계약) khác

Trình biên dịch (compiler / 컴파일러) không chỉ chuyển dòng mã nguồn (source line / 소스 코드 줄) thành lệnh máy (machine instruction / 기계 명령어) một-một. Nó có thể hoist tải (load / 로드), eliminate redundant read, giữ giá trị (value / 값) trong register, vectorize hoặc reorder operations nếu transformation giữ hành vi (behavior / 동작) mà ngôn ngữ (language / 언어) specification cho phép.

Điểm này rất quan trọng: một chương trình có dữ liệu (data / 데이터) race có thể không chỉ “thỉnh thoảng đọc giá trị cũ”. Với những ngôn ngữ cho optimizer giả định absence của một số race/undefined hành vi (behavior / 동작), trình biên dịch (compiler / 컴파일러) có thể tạo mã máy (machine code / 기계어) khác hẳn intuition source-order.

Vì vậy debugging race bằng cách nhìn assembly rồi nói “CPU chưa reorder ở đây” là chưa đủ. đặc tả hợp đồng (contract / 계약) đầu tiên cần kiểm tra là ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델).

## 5. Happens-before là lớp trừu tượng (abstraction / 추상화) chính để lập luận (reasoning / 추론)

Quan hệ xảy-ra-trước (happens-before) không có nghĩa “wall-clock xảy ra sớm hơn”. Nó là quan hệ lô-gic (logic / 논리) được tạo bởi program thứ tự (order / 순서), synchronization edges và tính bắc cầu.

Ví dụ trong Java, monitor khóa (lock / 잠금)/unlock, `volatile`, luồng thực thi (thread / 스레드) start/phép nối (join / 조인) và các synchronization actions khác tạo những edge cụ thể. Trong C++/Rust atomics, acquire/bản phát hành (release / 릴리스) hoặc thứ tự (ordering / 순서) mạnh hơn tạo đặc tả hợp đồng (contract / 계약) tương ứng.

Mô hình tư duy (mental model / 사고 모델):

```text
write data
   ↓ program order
release / unlock / volatile write
   ↓ synchronization edge
acquire / lock / volatile read
   ↓ program order
read data
```

Nếu chuỗi edge tồn tại, software có cơ sở để yêu cầu thời gian chạy (runtime / 런타임)/trình biên dịch (compiler / 컴파일러)/hardware giữ visibility cần thiết. Nếu không có edge, việc “thường xuyên thấy đúng” chỉ là accidental hành vi (behavior / 동작).

> **Nối mạch:** Happens-before biến giả định về visibility thành quan hệ có thể lập luận; **6. Publication bug** cho thấy invariant đó hỏng thế nào trong một object cụ thể.

## 6. Publication bug: đối tượng (object / 객체) đã có tham chiếu (reference / 참조) nhưng trạng thái (state / 상태) chưa hợp lệ

Giả sử một luồng thực thi (thread / 스레드) khởi tạo đối tượng (object / 객체) rồi publish tham chiếu (reference / 참조) cho luồng thực thi (thread / 스레드) khác mà không có synchronization đúng. bất biến (invariant / 불변식) mong muốn là:

> Nếu reader thấy tham chiếu (reference / 참조), reader phải thấy toàn bộ initialization được đặc tả hợp đồng (contract / 계약) bảo đảm.

Nếu publication không tạo happens-before, reader có thể quan sát trạng thái (state / 상태) không được bảo đảm. Đây là gốc của nhiều double-checked-locking bug lịch sử và các lỗi lazy initialization tự chế.

Fix đúng không phải thêm `sleep`. Fix là dùng safe-publication cơ chế (mechanism / 메커니즘) như khóa (lock / 잠금), `volatile`, atomic bản phát hành (release / 릴리스)/acquire, static initialization hoặc thành phần nguyên thủy (primitive / 기본 요소) thời gian chạy (runtime / 런타임) có đặc tả hợp đồng (contract / 계약) rõ.

## 7. Atomicity, visibility và thứ tự (ordering / 순서) là ba câu hỏi khác nhau

Một thao tác (operation / 연산) có thể atomic nhưng vẫn chưa cung cấp thứ tự (ordering / 순서) mà giao thức (protocol / 프로토콜) cần. Ngược lại, một fence có thể tạo thứ tự (ordering / 순서) nhưng không biến read-modify-write ghép thành atomic.

Ví dụ `count++` về lô-gic (logic / 논리) gồm read → add → ghi (write / 쓰기). `volatile` trong Java không tự biến toàn bộ chuỗi (sequence / 시퀀스) thành atomic increment. Atomic counter hoặc khóa (lock / 잠금) giải quyết bất biến (invariant / 불변식) “mỗi increment chỉ được áp dụng đúng một lần”.

Khi rà soát (review / 검토) concurrent mã (code / 코드), tách ba câu hỏi:

```text
Atomicity: operation có bị interleave thành lost update không?
Visibility: write có được reader hợp lệ quan sát không?
Ordering: reader được phép suy luận các operation khác trước/sau nó thế nào?
```

> **Nối mạch:** Tách atomicity, visibility và ordering giúp tránh sửa nhầm bằng scheduler; **8. OS scheduler** chỉ thay interleaving, không tự tạo memory guarantee.

## 8. OS scheduler quyết định interleaving, không quyết định bộ nhớ (memory / 메모리) ngữ nghĩa (semantics / 의미론)

Hệ điều hành có thể preempt luồng thực thi (thread / 스레드), migrate luồng thực thi (thread / 스레드) sang cốt lõi (core / 핵심) khác, thay đổi run-queue placement hoặc làm luồng thực thi (thread / 스레드) ngủ vì page fault/I/O. Điều này làm interleaving đa dạng hơn và khiến bug dễ hoặc khó xuất hiện hơn.

Nhưng scheduler không sửa một giao thức (protocol / 프로토콜) thiếu happens-before. `sleep(10)` chỉ thay xác suất interleaving; nó không tạo synchronization edge hợp lệ.

Đây là một lớp trừu tượng (abstraction / 추상화) ranh giới (boundary / 경계) hay bị nhầm: **OS scheduling quyết định khi nào luồng thực thi (thread / 스레드) có cơ hội chạy; ngôn ngữ (language / 언어)/ISA bộ nhớ (memory / 메모리) mô hình (model / 모델) quyết định những quan sát bộ nhớ (memory / 메모리) nào được phép**.

## 9. False sharing: tính đúng đắn (correctness / 정확성) đúng nhưng hiệu năng (performance / 성능) vẫn hỏng

Hai threads có thể hoàn toàn đúng về synchronization nhưng ghi hai counters khác nhau nằm cùng bộ nhớ đệm (cache / 캐시) line. Coherence giao thức (protocol / 프로토콜) lúc đó vẫn phải chuyển quyền sở hữu (ownership / 소유권) của cả line qua lại giữa cores.

Bất biến (invariant / 불변식) lô-gic (logic / 논리) không bị phá, nhưng hiệu năng (performance / 성능) hành vi (behavior / 동작) thay đổi:

```text
threads ↑
→ invalidation/coherence traffic ↑
→ cache-line bouncing ↑
→ throughput không tăng hoặc giảm
```

Đây là ví dụ quan trọng cho triết lý của thư viện (library / 라이브러리): cùng một lower-layer cơ chế (mechanism / 메커니즘) có thể gây **tính đúng đắn (correctness / 정확성) bug** khi thứ tự (ordering / 순서) đặc tả hợp đồng (contract / 계약) sai và gây **hiệu năng (performance / 성능) bug** khi dữ liệu (data / 데이터) bố cục (layout / 레이아웃) sai.

## 10. Lock-free làm proof burden tăng chứ không biến mất

Compare-and-swap (CAS) cho phép xây lock-free cấu trúc dữ liệu (data structure / 자료구조), nhưng bất biến (invariant / 불변식) phải bao gồm nhiều lớp hơn: linearization điểm (point / 지점), bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), ABA, đối tượng (object / 객체) reclamation và progress guarantee.

Một CAS thành công chỉ chứng minh giá trị (value / 값) vẫn khớp điều kiện so sánh tại thời điểm thành phần nguyên thủy (primitive / 기본 요소) chạy. Nó không tự chứng minh nút (node / 노드) chưa bị free/reuse hoặc mọi trường dữ liệu (field / 필드) liên quan đã được publish đúng.

Vì vậy lock-free mã (code / 코드) cần lập luận (reasoning / 추론) formal hơn mã (code / 코드) dùng khóa (lock / 잠금), không phải ít lập luận (reasoning / 추론) hơn.

## 11. dạng thất bại (failure mode / 실패 모드) điển hình

Các thất bại (failure / 실패) thường xuất hiện dưới những dạng khác nhau nhưng cùng thiếu đặc tả hợp đồng (contract / 계약):

```text
lost update
stale read
unsafe publication
check-then-act race
ABA
use-after-free trong reclamation
livelock/starvation
false sharing và cache-line ping-pong
```

Một symptom có thể biến mất khi bật debugger hoặc thêm logging vì instrumentation đổi scheduling, mã (code / 코드) bố cục (layout / 레이아웃), fence hành vi (behavior / 동작) hoặc bộ nhớ đệm (cache / 캐시) pressure. Đây là reason race thường trở thành Heisenbug.

## 12. bằng chứng vận hành (production evidence / 운영 증거): đừng chỉ đọc nguồn (source / 소스)

Bằng chứng (evidence / 증거) nên đi theo tầng lớp trừu tượng (abstraction / 추상화) đang nghi ngờ.

Ở ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) tầng (layer / 계층), dùng race detector khi ecosystem hỗ trợ, luồng thực thi (thread / 스레드) dump, khóa (lock / 잠금)/park statistics, contention profiler, GC/thời gian chạy (runtime / 런타임) logs và minimal kiểm thử sức chịu tải (stress test / 스트레스 테스트). Ở OS tầng (layer / 계층), quan sát run hàng đợi (queue / 큐), ngữ cảnh (context / 맥락) switch, CPU di chuyển (migration / 마이그레이션), scheduler độ trễ (latency / 지연 시간) và blocked/off-CPU thời gian (time / 시간). Ở hardware tầng (layer / 계층), hiệu năng (performance / 성능) counters có thể cho thấy LLC miss, cache-to-cache transfer, stalled cycles hoặc coherence pressure tùy CPU/tooling.

Bằng chứng (evidence / 증거) không thay proof. Race detector có thể không cover mọi interleaving; PMU counter không nói dòng mã nguồn (source line / 소스 코드 줄) nào vi phạm happens-before. Mục tiêu là kết hợp:

```text
invariant/proof
+
reproducible execution
+
runtime/OS/hardware evidence
```

## 13. nhân quả (causal / 인과적) walkthrough: CPU bộ nhớ đệm (cache / 캐시) → bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) → ngôn ngữ (language / 언어) mô hình (model / 모델) → bug

Một lập luận (reasoning / 추론) chuỗi (chain / 사슬) hoàn chỉnh có thể là:

```text
hai cores ghi/đọc shared state
↓
store buffer + cache coherence làm visibility không đồng thời
↓
ISA chỉ bảo đảm ordering theo memory model/fence semantics
↓
compiler map atomic/volatile/lock của language xuống ISA primitive
↓
program thiếu synchronization edge cần thiết
↓
reader không có happens-before guarantee
↓
unsafe publication hoặc stale observation xuất hiện
↓
logging/debugger thay timing nên bug khó tái hiện
```

Điểm sửa đúng nằm ở tầng **program giao thức (protocol / 프로토콜)/ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델)**, dù lower tầng (layer / 계층) giải thích vì sao bug có thể lộ ra.

## 14. Checklist lập luận (reasoning / 추론) trước khi sửa tính đồng thời (concurrency / 동시성) bug

Hãy viết bất biến (invariant / 불변식) bằng câu rõ ràng trước. Xác định dùng chung (shared / 공유) mutable trạng thái (state / 상태) và đơn vị sở hữu (owner / 오너). Xác định thao tác (operation / 연산) nào cần atomic. Vẽ happens-before edge giữa writer và reader. Chỉ sau đó mới hỏi thành phần nguyên thủy (primitive / 기본 요소) đó map xuống fence/atomic nào và có chi phí (cost / 비용) gì.

Nếu fix hiệu năng (performance / 성능), kiểm tra thêm contention topology: khóa (lock / 잠금) đơn vị sở hữu (owner / 오너), bộ nhớ đệm (cache / 캐시) line, NUMA nút (node / 노드), run hàng đợi (queue / 큐) và bộ nhớ (memory / 메모리) bandwidth. Nếu fix tính đúng đắn (correctness / 정확성), không đổi sang thứ tự (ordering / 순서) yếu hơn chỉ vì benchmark nhanh hơn khi chưa chứng minh giao thức (protocol / 프로토콜).

## Mô hình tư duy

> CPU bộ nhớ đệm (cache / 캐시) và coherence quyết định dữ liệu di chuyển vật lý thế nào; ISA bộ nhớ (memory / 메모리) mô hình (model / 모델) giới hạn các thứ tự (ordering / 순서) phần cứng được phép; trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) phải ánh xạ ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) xuống các thành phần nguyên thủy (primitive / 기본 요소) đó; chương trình chỉ đúng khi bất biến (invariant / 불변식) của nó được biểu diễn bằng synchronization edges hợp lệ. **Lower tầng (layer / 계층) giải thích hành vi (behavior / 동작), nhưng fix phải được đặt ở lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) sở hữu bất biến (invariant / 불변식).**

## Kết nối

Đọc cùng [Cache hierarchy foundation](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS concurrency foundation](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Programming Languages concurrency foundation](../../basic/04_programming_languages/08_concurrency_models_and_memory_safety.md), [Memory consistency advanced](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [Debugging xuyên abstraction layers](./00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 debugging across abstraction layers](./00_debugging_across_abstraction_layers.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
