# RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Mutual exclusion và thời gian tồn tại (lifetime / 수명) an toàn (safety / 안전) là hai bài toán khác nhau** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. RCU là publication + grace period + deferred reclamation** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối RCU, seqlock và memory reclamation, để phân biệt đọc không khóa với bảo đảm tuổi thọ dữ liệu và thứ tự quan sát.

Đọc trước [Kernel execution contexts, synchronization và syscall path](./00_kernel_execution_contexts_and_syscall_path.md) để có mô hình tư duy (mental model / 사고 모델) về tiến trình (process / 프로세스) ngữ cảnh (context / 맥락), interrupt ngữ cảnh (context / 맥락), blocking, spinlock và đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명). Chapter này đi sâu vào một lớp bài toán riêng: **làm thế nào cho rất nhiều reader truy cập trạng thái dùng chung (shared state / 공유 상태) với chi phí thấp mà writer vẫn có thể thay đổi hoặc thu hồi đối tượng (object / 객체) an toàn**.

Nếu chỉ nghĩ synchronization là “khóa trước khi đọc/ghi”, ta sẽ bỏ lỡ vấn đề khó hơn: một pointer có thể đã được reader lấy ra đúng lúc writer xóa đối tượng (object / 객체) khỏi cấu trúc (structure / 구조). Xóa khỏi chỉ mục (index / 인덱스) không đồng nghĩa đối tượng (object / 객체) có thể được `free` ngay. Vì vậy bất biến (invariant / 불변식) trung tâm của chapter là:

> Một đối tượng (object / 객체) chỉ được reclaim khi không còn thực thi (execution / 실행) ngữ cảnh (context / 맥락) hợp lệ nào có thể dereference phiên bản cũ của nó.

Mô hình tư duy (mental model / 사고 모델) xuyên suốt:

```text
publish
→ reader obtains reference
→ writer replaces/removes logical state
→ old readers may still exist
→ grace/reclamation protocol proves safety
→ physical memory can be reused
```

## 1. Mutual exclusion và thời gian tồn tại (lifetime / 수명) an toàn (safety / 안전) là hai bài toán khác nhau

Mutex hoặc spinlock có thể bảo đảm hai writer không sửa cùng trạng thái (state / 상태) đồng thời. Nhưng khóa (lock / 잠금) không tự động giải thời gian tồn tại (lifetime / 수명) nếu tham chiếu (reference / 참조) sống lâu hơn trọng yếu (critical / 중요) section hoặc reader đường dẫn (path / 경로) cố ý không giữ writer khóa (lock / 잠금).

Ví dụ một lookup trả về pointer `p`. Sau khi lookup hoàn tất, writer xóa `p` khỏi cây (tree / 트리) và `free(p)`. Nếu reader vẫn dùng `p`, tính đúng đắn (correctness / 정확성) đã hỏng dù thao tác remove được bảo vệ bằng khóa (lock / 잠금) hoàn hảo.

Do đó cần phân biệt:

```text
state synchronization
≠
object lifetime management
```

Nhiều kernel cấu trúc (structure / 구조), thời gian chạy (runtime / 런타임) bảng (table / 테이블), routing bảng (table / 테이블) và read-mostly registry tối ưu reader bằng cách tách hai vấn đề này.

> **Chuyển mạch:** Mutual exclusion bảo vệ truy cập, còn lifetime safety bảo vệ việc reclaim; RCU công bố rồi chờ grace period lô-gic, không thể thay bằng timeout tùy ý.

## 2. RCU là publication + grace period + deferred reclamation

Read-Copy-Update (RCU) là family technique trong đó reader thường không serialize với nhau. Writer chuẩn bị trạng thái (state / 상태) mới, publish nó, rồi hoãn reclaim trạng thái (state / 상태) cũ.

Một cập nhật (update / 업데이트) điển hình có dạng:

```text
old = current
new = copy_or_new_version(old)
mutate(new)
publish(new)
wait_until_preexisting_readers_are_gone()
reclaim(old)
```

Từ “bản sao (copy / 복사)” không bắt buộc toàn bộ cấu trúc (structure / 구조) phải được clone. Nhiều hiện thực (implementation / 구현) chỉ allocate nút (node / 노드) mới, relink một số pointer rồi retire nút (node / 노드) cũ. Bản chất là **reader có thể tiếp tục nhìn một phiên bản (version / 버전) hợp lệ trong lúc writer tạo phiên bản (version / 버전) kế tiếp**.

> **Chuyển mạch:** Ở chặng này của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **3. Grace period là điều kiện lô-gic (logic / 논리), không phải hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **2. RCU là publication + grace period + deferred reclamation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Publication đúng còn phụ thuộc bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Grace period là điều kiện lô-gic (logic / 논리), không phải hết thời gian chờ (timeout / 타임아웃)

Grace period không có nghĩa “đợi 10 ms cho chắc”. Nó chứng minh rằng mọi reader có khả năng giữ tham chiếu (reference / 참조) từ trước publication đã đi qua một trạng thái mà giao thức (protocol / 프로토콜) coi là quiescent.

Tùy hiện thực (implementation / 구현), quiescent trạng thái (state / 상태) có thể liên quan đến ngữ cảnh (context / 맥락) switch, rời read-side trọng yếu (critical / 중요) section, người dùng (user / 사용자)/kernel chuyển tiếp (transition / 전이) hoặc một epoch progression. Điều quan trọng là proof về thời gian tồn tại (lifetime / 수명), không phải số milliseconds.

Nếu một CPU hoặc tác vụ (task / 작업) giữ read-side section quá lâu, writer có thể publish trạng thái (state / 상태) mới thành công nhưng bộ nhớ (memory / 메모리) cũ chưa được thu hồi. Khi đó độ trễ (latency / 지연 시간) reader vẫn tốt nhưng reclamation backlog tăng. Pressure chuyển từ tranh chấp khóa (lock contention / 잠금 경합) sang bộ nhớ (memory / 메모리) retention.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **4. Publication đúng còn phụ thuộc bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** tiếp nhận điểm tựa từ **3. Grace period là điều kiện lô-gic (logic / 논리), không phải hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Writer không được nhầm logical removal với vật lý (physical / 물리적) reclamation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Publication đúng còn phụ thuộc bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)

Writer không được publish pointer tới đối tượng (object / 객체) mới trước khi fields của đối tượng (object / 객체) được khởi tạo theo visibility đặc tả hợp đồng (contract / 계약). Nếu trình biên dịch (compiler / 컴파일러) hoặc CPU reordering làm reader thấy pointer mới nhưng trạng thái (state / 상태) bên trong chưa visible đúng, RCU vẫn sai.

Tính đúng đắn (correctness / 정확성) đường dẫn (path / 경로) là:

```text
initialize object
→ release/publication ordering
→ pointer becomes reachable
→ acquire/dependency semantics on reader side
→ object state becomes valid to observe
```

Vì vậy RCU không “đứng trên” bộ nhớ (memory / 메모리) mô hình (model / 모델). Nó dựa vào ngôn ngữ (language / 언어)/trình biên dịch (compiler / 컴파일러) thành phần nguyên thủy (primitive / 기본 요소) và ISA thứ tự (ordering / 순서). Đọc thêm [memory consistency, cache coherence và ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [correctness path xuyên tầng](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

> **Chuyển mạch:** Trong **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **4. Publication đúng còn phụ thuộc bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)** đã nêu tiêu chí phân biệt, còn **5. Writer không được nhầm logical removal với vật lý (physical / 물리적) reclamation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. RCU callback biến reclaim thành asynchronous debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Writer không được nhầm logical removal với vật lý (physical / 물리적) reclamation

Khi writer unlink nút (node / 노드) khỏi danh sách (list / 목록)/cây (tree / 트리)/bảng băm (hash table / 해시 테이블), nút (node / 노드) đã biến mất khỏi **future lookup** nhưng vẫn có thể được **past reader** giữ tham chiếu (reference / 참조).

Ta có ba thời điểm khác nhau:

```text
T1: object reachable
T2: object no longer reachable by new readers
T3: object safe to reclaim
```

`T2` và `T3` không giống nhau. Phần lớn bug use-after-free trong lock-free/read-mostly thiết kế (design / 설계) xuất hiện khi hiện thực (implementation / 구현) coi hai mốc này là một.

> **Chuyển mạch:** Ở chặng này của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **5. Writer không được nhầm logical removal với vật lý (physical / 물리적) reclamation** đã nêu tiêu chí phân biệt, còn **6. RCU callback biến reclaim thành asynchronous debt** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. Seqlock tối ưu một loại snapshot khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. RCU callback biến reclaim thành asynchronous debt

Thay vì writer chờ đồng bộ grace period, hệ thống có thể enqueue callback để reclaim sau. Điều này giảm độ trễ (latency / 지연 시간) của cập nhật (update / 업데이트) foreground nhưng tạo một hàng đợi (queue / 큐) hậu cảnh.

Khi cập nhật (update / 업데이트) tỷ lệ (rate / 비율) tăng hoặc readers giữ trọng yếu (critical / 중요) section lâu, callback hàng đợi (queue / 큐) có thể phình ra:

```text
update rate ↑
→ retired objects ↑
→ pending callbacks ↑
→ unreclaimed memory ↑
→ memory pressure / cache pressure ↑
```

Đây là phase thay đổi (change / 변경) quan trọng. Một thiết kế (design / 설계) rất tốt ở read-heavy steady trạng thái (state / 상태) có thể trở nên nguy hiểm trong cập nhật (update / 업데이트) storm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **7. Seqlock tối ưu một loại snapshot khác** tiếp nhận điểm tựa từ **6. RCU callback biến reclaim thành asynchronous debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Seqlock không phù hợp với pointer có thời gian tồn tại (lifetime / 수명) phức tạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Seqlock tối ưu một loại snapshot khác

Chuỗi (sequence / 시퀀스) khóa (lock / 잠금) (seqlock) phù hợp khi trạng thái (state / 상태) nhỏ, writer cập nhật tương đối nhanh và reader có thể thử lại (retry / 재시도).

Writer tăng chuỗi (sequence / 시퀀스) counter sang trạng thái “đang ghi”, cập nhật fields rồi publish chuỗi (sequence / 시퀀스) mới. Reader làm:

```text
v1 = sequence
read snapshot fields
v2 = sequence
accept only if v1 == v2 and version means no writer overlap
otherwise retry
```

Bất biến (invariant / 불변식) của seqlock không phải thời gian tồn tại (lifetime / 수명) của đối tượng (object / 객체) cũ mà là:

> Reader chỉ chấp nhận snapshot nếu không có writer làm thay đổi trạng thái (state / 상태) trong khoảng đọc.

Seqlock tránh reader khóa (lock / 잠금) nhưng không bảo đảm reader hoàn tất nhanh khi writer liên tục. Write-heavy pressure có thể biến optimistic read thành thử lại (retry / 재시도) storm.

> **Chuyển mạch:** Trong **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **8. Seqlock không phù hợp với pointer có thời gian tồn tại (lifetime / 수명) phức tạp** tiếp nhận điểm tựa từ **7. Seqlock tối ưu một loại snapshot khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Epoch-based reclamation và hazard pointer giải cùng family bài toán (problem / 문제) bằng proof khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Seqlock không phù hợp với pointer có thời gian tồn tại (lifetime / 수명) phức tạp

Nếu snapshot chứa pointer tới đối tượng (object / 객체) mà writer có thể free, việc chuỗi (sequence / 시퀀스) kiểm tra hợp lệ (validation / 검증) sau cùng có thể quá muộn: reader có thể đã dereference bộ nhớ (memory / 메모리) invalid trong lúc bản sao (copy / 복사).

Vì vậy seqlock thường an toàn nhất với dữ liệu (data / 데이터) có thể bản sao (copy / 복사) trực tiếp và thời gian tồn tại (lifetime / 수명) ổn định trong giao thức (protocol / 프로토콜). Khi trạng thái (state / 상태) chứa đối tượng (object / 객체) đồ thị (graph / 그래프) phức tạp, cần kết hợp thời gian tồn tại (lifetime / 수명) cơ chế (mechanism / 메커니즘) khác.

Điều này cho thấy “lock-free reader” không phải một category đồng nhất. Cần hỏi chính xác bất biến (invariant / 불변식) nào đang được bảo vệ.

> **Chuyển mạch:** Ở chặng này của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **9. Epoch-based reclamation và hazard pointer giải cùng family bài toán (problem / 문제) bằng proof khác** tiếp nhận điểm tựa từ **8. Seqlock không phù hợp với pointer có thời gian tồn tại (lifetime / 수명) phức tạp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. ABA cho thấy CAS success chưa chắc trạng thái (state / 상태) “vẫn như cũ”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Epoch-based reclamation và hazard pointer giải cùng family bài toán (problem / 문제) bằng proof khác

RCU không phải kỹ thuật duy nhất. **Epoch-based reclamation** cho reader tham gia epoch; đối tượng (object / 객체) retired ở epoch cũ chỉ được reclaim sau khi tất cả participant có thể giữ tham chiếu (reference / 참조) cũ đã tiến qua epoch an toàn.

**Hazard pointer** đi theo hướng khác: reader công bố pointer mà nó đang dùng; reclaimer không được free đối tượng (object / 객체) còn xuất hiện trong hazard set.

Mô hình tư duy (mental model / 사고 모델):

```text
RCU / epoch:
prove old readers are gone

hazard pointer:
prove this object is not currently protected by any reader
```

Mỗi cách có chi phí siêu dữ liệu (metadata / 메타데이터), scanning, bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và stall hành vi (behavior / 동작) khác nhau. Không có lựa chọn universal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **10. ABA cho thấy CAS success chưa chắc trạng thái (state / 상태) “vẫn như cũ”** tiếp nhận điểm tựa từ **9. Epoch-based reclamation và hazard pointer giải cùng family bài toán (problem / 문제) bằng proof khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Preemption và scheduler có thể trở thành một phần của reclamation proof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. ABA cho thấy CAS success chưa chắc trạng thái (state / 상태) “vẫn như cũ”

Trong lock-free thuật toán (algorithm / 알고리즘), luồng thực thi (thread / 스레드) có thể đọc pointer/giá trị (value / 값) `A`, bị pause, trong lúc luồng thực thi (thread / 스레드) khác đổi `A → B → A`. Khi luồng thực thi (thread / 스레드) đầu dùng compare-and-swap, giá trị bề ngoài vẫn là `A` nên CAS có thể thành công dù đối tượng (object / 객체) định danh (identity / 식별자)/thời gian tồn tại (lifetime / 수명) đã thay đổi.

Đó là ABA bài toán (problem / 문제). Tag/phiên bản (version / 버전) counter, hazard pointer, epoch reclamation hoặc đối tượng (object / 객체) định danh (identity / 식별자) discipline có thể cần thiết tùy cấu trúc (structure / 구조).

Điểm cần nhớ: atomicity của một instruction không chứng minh ngữ nghĩa (semantic / 의미적) continuity của đối tượng (object / 객체).

> **Chuyển mạch:** Trong **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **11. Preemption và scheduler có thể trở thành một phần của reclamation proof** tiếp nhận điểm tựa từ **10. ABA cho thấy CAS success chưa chắc trạng thái (state / 상태) “vẫn như cũ”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. NUMA và bộ nhớ đệm (cache / 캐시) coherence vẫn quyết định chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Preemption và scheduler có thể trở thành một phần của reclamation proof

Nếu grace-period detection dựa vào quiescent states, một tác vụ (task / 작업) bị preempt hoặc CPU không report progress có thể trì hoãn reclamation. Do đó scheduler hành vi (behavior / 동작) và RCU progress không hoàn toàn độc lập.

Trong môi trường vận hành (production / 운영 환경), symptom có thể là bộ nhớ (memory / 메모리) tăng dù allocation tỷ lệ (rate / 비율) nghiệp vụ (business / 비즈니스) không tăng tương ứng. Nguyên nhân thực sự có thể là reader stall hoặc callback backlog, không phải “bộ nhớ (memory / 메모리) leak” theo nghĩa đối tượng (object / 객체) bị mất tham chiếu (reference / 참조) vĩnh viễn.

> **Chuyển mạch:** Ở chặng này của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **12. NUMA và bộ nhớ đệm (cache / 캐시) coherence vẫn quyết định chi phí (cost / 비용)** tiếp nhận điểm tựa từ **11. Preemption và scheduler có thể trở thành một phần của reclamation proof** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. thất bại (failure / 실패) modes đặc trưng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. NUMA và bộ nhớ đệm (cache / 캐시) coherence vẫn quyết định chi phí (cost / 비용)

Reader đường dẫn (path / 경로) nhẹ không có nghĩa miễn phí. dùng chung (shared / 공유) chuỗi (sequence / 시퀀스) counters, toàn cục (global / 전역) epoch trạng thái (state / 상태) hoặc callback siêu dữ liệu (metadata / 메타데이터) vẫn có cache-line traffic. Với nhiều sockets/NUMA nodes, location của dùng chung (shared / 공유) siêu dữ liệu (metadata / 메타데이터) và frequency cập nhật có thể trở thành bottleneck.

Một thiết kế (design / 설계) quy mô (scale / 규모) tốt thường cố gắng:

```text
reader-local fast path
+ batched/global coordination hiếm hơn
+ amortized reclamation work
```

Nếu mọi read đều cập nhật (update / 업데이트) một toàn cục (global / 전역) bộ nhớ đệm (cache / 캐시) line, ta đã vô tình tái tạo contention ở dạng khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **13. thất bại (failure / 실패) modes đặc trưng** tiếp nhận điểm tựa từ **12. NUMA và bộ nhớ đệm (cache / 캐시) coherence vẫn quyết định chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. bằng chứng vận hành (production evidence / 운영 증거) cần phân biệt contention với reclamation debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. thất bại (failure / 실패) modes đặc trưng

Use-after-free xuất hiện khi reclaim quá sớm. bộ nhớ (memory / 메모리) retention xuất hiện khi grace period không hoàn tất hoặc reader quên exit giao thức (protocol / 프로토콜). thử lại (retry / 재시도) starvation xuất hiện với seqlock khi writer quá thường xuyên. ABA xuất hiện khi định danh (identity / 식별자) bị tái sử dụng mà phiên bản (version / 버전)/protection không đủ. Publication bug xuất hiện khi bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) không đúng.

Đây là lý do cần mô tả thất bại (failure / 실패) theo bất biến (invariant / 불변식) thay vì chỉ nhớ API.

> **Chuyển mạch:** Trong **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **13. thất bại (failure / 실패) modes đặc trưng** nêu điều cần giải thích; **14. bằng chứng vận hành (production evidence / 운영 증거) cần phân biệt contention với reclamation debt** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Worked example: read-mostly routing bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bằng chứng vận hành (production evidence / 운영 증거) cần phân biệt contention với reclamation debt

Khi thông lượng (throughput / 처리량) giảm hoặc bộ nhớ (memory / 메모리) tăng, các tín hiệu hữu ích gồm reader critical-section duration, grace-period độ trễ (latency / 지연 시간), số callback/retires pending, bộ nhớ (memory / 메모리) chưa reclaim, writer cập nhật (update / 업데이트) tỷ lệ (rate / 비율), seqlock thử lại (retry / 재시도) count, CPU spinning, cache-to-cache transfer, scheduler stall và NUMA locality.

Một chuỗi nhân quả (causal chain / 인과 사슬) thường có dạng:

```text
reader stall
→ grace period kéo dài
→ retired objects tích tụ
→ memory pressure tăng
→ reclaim/page fault/cache miss tăng
→ latency application tăng
```

Nếu chỉ nhìn vùng nhớ động (heap / 힙)/RSS cuối chuỗi (chain / 사슬), dễ chẩn đoán sai thành allocator leak.

> **Chuyển mạch:** Ở chặng này của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **14. bằng chứng vận hành (production evidence / 운영 증거) cần phân biệt contention với reclamation debt** cho ta quy tắc; **15. Worked example: read-mostly routing bảng (table / 테이블)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. Khi nào không nên dùng RCU hoặc seqlock?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Worked example: read-mostly routing bảng (table / 테이블)

Giả sử dataplane lookup routing entry cho mỗi packet, trong khi điều khiển (control / 제어) plane cập nhật (update / 업데이트) tuyến (route / 경로) ít hơn nhiều. Nếu reader phải lấy toàn cục (global / 전역) mutex cho mỗi lookup, thông lượng (throughput / 처리량) chịu khóa (lock / 잠금)/cache-line pressure.

Một versioned publication thiết kế (design / 설계) cho phép writer tạo entry mới và atomically thay pointer. Packet đang dùng old entry vẫn hoàn tất; entry cũ chỉ reclaim sau khi read-side users cũ đã rời trọng yếu (critical / 중요) section.

Khi tuyến (route / 경로) churn tăng đột biến, lợi ích reader vẫn còn nhưng retired-entry backlog có thể tăng. Đây là lúc bằng chứng vận hành (production evidence / 운영 증거) phải đo cả cập nhật (update / 업데이트) tỷ lệ (rate / 비율) và grace/reclaim progress.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **15. Worked example: read-mostly routing bảng (table / 테이블)** cho ta quy tắc; **16. Khi nào không nên dùng RCU hoặc seqlock?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **17. Kết nối sang các chapter khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Khi nào không nên dùng RCU hoặc seqlock?

Nếu tải công việc (workload / 워크로드) write-heavy, bất biến (invariant / 불변식) cần atomic cập nhật (update / 업데이트) trên đối tượng (object / 객체) đồ thị (graph / 그래프) lớn, reader không thể thử lại (retry / 재시도), hoặc nhóm (team / 팀) không đủ tooling để chứng minh thời gian tồn tại (lifetime / 수명)/thứ tự (order / 순서) tính đúng đắn (correctness / 정확성), mutex/RW-lock đơn giản có thể tốt hơn.

Cấp cao (senior / 시니어) kỹ thuật (engineering / 엔지니어링) không phải chọn thành phần nguyên thủy (primitive / 기본 요소) “nhanh nhất”; là chọn proof dễ duy trì nhất trong tải công việc (workload / 워크로드) và thất bại (failure / 실패) mô hình (model / 모델) thực tế.

> **Chuyển mạch:** Trong **RCU, seqlock và safe bộ nhớ (memory / 메모리) reclamation**, **17. Kết nối sang các chapter khác** tiếp nhận điểm tựa từ **16. Khi nào không nên dùng RCU hoặc seqlock?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 17. Kết nối sang các chapter khác

RCU/seqlock nối trực tiếp với [kernel execution context](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md), [ownership và memory safety](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md) và [whole-system debugging](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Điểm cuối cùng cần giữ là: **reader speed chỉ an toàn khi publication, thứ tự (ordering / 순서) và reclamation cùng tạo thành một proof hoàn chỉnh về đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명).**

> **Bàn giao:** Giữ lại publication ordering, reader retry, grace/epoch progress và reclamation lifetime như một proof duy nhất. Sang [Kernel execution contexts](./00_kernel_execution_contexts_and_syscall_path.md) nếu cần nối preemption/RCU context, hoặc [Architecture memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) nếu cần kiểm tra ordering/coherence; quay về [README](./README.md) để xác nhận owner.
