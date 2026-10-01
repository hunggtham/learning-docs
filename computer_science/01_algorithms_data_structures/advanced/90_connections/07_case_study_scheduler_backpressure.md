# Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. FIFO là baseline** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Priority hàng đợi (queue / 큐)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Scheduling & Backpressure trường hợp (case / 사례) Study / 스케줄링과 백프레셔 사례**

Scheduler xuất hiện ở CPU, job hàng đợi (queue / 큐), luồng thực thi (thread / 스레드) pool, message processing, mạng (network / 네트워크) packet scheduling và background worker. Bài toán tưởng như chỉ là “chọn công việc tiếp theo”, nhưng thực tế phải cân bằng nhiều mục tiêu: độ trễ, thông lượng (throughput / 처리량), fairness, deadline, priority, bộ nhớ (memory / 메모리) và khả năng hấp thụ burst.

Trường hợp (case / 사례) study này nối hàng đợi (queue / 큐), Deque, Priority hàng đợi (queue / 큐), vùng nhớ động (heap / 힙), bảng băm (hash table / 해시 테이블), Fair Scheduling và Backpressure thành một mô hình hệ thống thống nhất.

## 1. FIFO là baseline

Hàng đợi (queue / 큐) FIFO xử lý theo thứ tự đến:

```text
job1 -> job2 -> job3 -> ...
```

Ưu điểm:

```text
đơn giản
fair theo thời gian đến
chi phí thấp
```

Nhưng FIFO không biết job nào quan trọng hơn hoặc job nào có deadline gần hơn.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **2. Priority hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **1. FIFO là baseline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Mutable Priority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Priority hàng đợi (queue / 큐)

Nếu mỗi job có priority, min/max vùng nhớ động (heap / 힙) là lựa chọn tự nhiên:

```text
(priority, arrivalOrder, jobId)
```

Tie-break bằng `arrivalOrder` giúp giữ fairness giữa các job cùng priority.

Nếu không có tie-break ổn định, scheduler có thể cho hành vi khó dự đoán dù priority chính vẫn đúng.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **3. Mutable Priority** tiếp nhận điểm tựa từ **2. Priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Starvation và Aging** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Mutable Priority

Priority có thể thay đổi theo thời gian: job chờ lâu được tăng độ ưu tiên để tránh starvation.

Vùng nhớ vùng nhớ động (heap / 힙) chuẩn không tự sắp xếp lại khi trường dữ liệu (field / 필드) của đối tượng (object / 객체) thay đổi. Có ba hướng:

```text
indexed heap + decrease/increase-key
chèn entry mới và bỏ entry cũ khi pop
rebuild heap theo chu kỳ
```

Lazy stale-entry thường đơn giản và robust nếu bộ nhớ (memory / 메모리) overhead chấp nhận được.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **4. Starvation và Aging** tiếp nhận điểm tựa từ **3. Mutable Priority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Deadline Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Starvation và Aging

Nếu luôn chọn priority cao nhất, job priority thấp có thể chờ vô hạn.

**Aging** tăng effective priority theo thời gian:

\[
effectivePriority = basePriority + f(waitTime)
\]

Scheduler không còn tối ưu một scalar cố định; priority trở thành hàm của trạng thái (state / 상태) động.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **5. Deadline Scheduling** tiếp nhận điểm tựa từ **4. Starvation và Aging** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Shortest Job First** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Deadline Scheduling

Nếu job có deadline, một chiến lược (strategy / 전략) cổ điển là **Earliest Deadline First (EDF)**: luôn chọn job có deadline sớm nhất.

Priority hàng đợi (queue / 큐) có key là deadline.

Nhưng EDF chỉ có guarantee mạnh dưới những giả định cụ thể về mô hình tác vụ (task / 작업) và utilization. Không nên áp dụng theorem real-time vào tải công việc (workload / 워크로드) tùy ý mà không kiểm tra giả định.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **6. Shortest Job First** tiếp nhận điểm tựa từ **5. Deadline Scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Multi-Level hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Shortest Job First

Nếu biết dịch vụ (service / 서비스) thời gian (time / 시간), xử lý job ngắn trước có thể giảm average waiting thời gian (time / 시간) trong một số mô hình.

Nhưng long job có thể starvation nếu short job đến liên tục.

Một mục tiêu tối ưu average độ trễ (latency / 지연 시간) có thể xung đột fairness.

Đây là bài học quan trọng: scheduler cần **mục tiêu (objective / 목표) rõ ràng**, không chỉ cấu trúc dữ liệu (data structure / 자료구조) nhanh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **7. Multi-Level hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **6. Shortest Job First** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Weighted Fairness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Multi-Level hàng đợi (queue / 큐)

Có thể chia job thành nhiều hàng đợi (queue / 큐):

```text
critical
interactive
batch
background
```

Scheduler chọn giữa các hàng đợi (queue / 큐) theo chính sách (policy / 정책) rồi FIFO/priority bên trong mỗi hàng đợi (queue / 큐).

Composition này thường dễ kiểm soát hơn một toàn cục (global / 전역) priority formula cực phức tạp.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **8. Weighted Fairness** tiếp nhận điểm tựa từ **7. Multi-Level hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. hàng đợi (queue / 큐) có giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Weighted Fairness

Giả sử ba tenant có trọng số:

```text
A: 5
B: 3
C: 2
```

Ta muốn chia sức chứa (capacity / 용량) tương đối 50% / 30% / 20% trong dài hạn.

Weighted Round Robin là một cách đơn giản. Các thuật toán công bằng hơn có thể mô hình hóa **virtual finish thời gian (time / 시간)** và dùng priority hàng đợi (queue / 큐).

Một scheduler tốt phải phân biệt:

```text
priority -> ai nên đi trước
fairness -> ai nhận bao nhiêu tài nguyên theo thời gian
```

Hai khái niệm không giống nhau.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **8. Weighted Fairness** đã nêu tiêu chí phân biệt, còn **9. hàng đợi (queue / 큐) có giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. hàng đợi (queue / 큐) có giới hạn

Hàng đợi (queue / 큐) vô hạn về lô-gic (logic / 논리) là nguy hiểm trong hệ thống thật.

Nếu producer tạo 100k job/s nhưng bên tiêu thụ (consumer / 소비자) chỉ xử lý 80k/s, hàng đợi (queue / 큐) tăng 20k/s. Sau đủ lâu, bộ nhớ (memory / 메모리) hoặc disk sẽ cạn.

Hàng đợi (queue / 큐) có giới hạn biến tài nguyên hữu hạn thành một bất biến (invariant / 불변식):

```text
0 <= size <= capacity
```

Khi đầy, hệ thống buộc phải có chính sách (policy / 정책).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **9. hàng đợi (queue / 큐) có giới hạn** đã nêu tiêu chí phân biệt, còn **10. Backpressure** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. Little’s Law** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Backpressure

Backpressure là cơ chế truyền tín hiệu “downstream đang quá tải” ngược lên upstream.

Các lựa chọn:

```text
block producer
reject request
return 429 / busy
slow down producer
drop low-priority work
spill to disk
scale consumer
```

Không có chính sách (policy / 정책) chung đúng cho mọi hệ thống. Log telemetry có thể drop một phần; payment yêu cầu (request / 요청) thường không thể âm thầm drop.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **11. Little’s Law** tiếp nhận điểm tựa từ **10. Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Little’s Law

Trong trạng thái ổn định:

\[
L = \lambda W
\]

với:

```text
L      = số item trung bình trong hệ thống
lambda = throughput trung bình
W      = thời gian trung bình một item ở trong hệ thống
```

Nếu arrival tỷ lệ (rate / 비율) tiến sát dịch vụ (service / 서비스) sức chứa (capacity / 용량), queueing độ trễ (latency / 지연 시간) có thể tăng mạnh.

Little’s Law không thiết kế scheduler thay ta, nhưng giúp liên hệ hàng đợi (queue / 큐) length, thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **12. Batching** tiếp nhận điểm tựa từ **11. Little’s Law** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. công việc (work / 작업) Stealing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Batching

Thay vì xử lý từng item:

```text
pop 1 -> xử lý -> pop 1
```

có thể lấy một batch:

```text
pop 100 -> xử lý chung
```

Batching giảm overhead khóa, syscall, mạng (network / 네트워크) round-trip hoặc vectorization chi phí (cost / 비용) trên mỗi item.

Nhưng batch quá lớn làm tăng waiting độ trễ (latency / 지연 시간) cho item đầu tiên.

Đây là sự đánh đổi (trade-off / 트레이드오프) thông lượng (throughput / 처리량)–độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **13. công việc (work / 작업) Stealing** tiếp nhận điểm tựa từ **12. Batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. toàn cục (global / 전역) hàng đợi (queue / 큐) vs cục bộ (local / 로컬) Queues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. công việc (work / 작업) Stealing

Trong luồng thực thi (thread / 스레드) pool, mỗi worker có deque riêng.

Worker thường:

```text
push/pop task của mình ở một đầu
```

Worker rảnh có thể **steal** từ đầu còn lại của worker khác.

Deque giúp giảm contention vì đơn vị sở hữu (owner / 오너) và thief thường thao tác ở hai đầu khác nhau.

Công việc (work / 작업) stealing đặc biệt phù hợp tác vụ (task / 작업) recursive/fork-join vì các tác vụ (task / 작업) mới sinh thường có locality với worker hiện tại.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **14. toàn cục (global / 전역) hàng đợi (queue / 큐) vs cục bộ (local / 로컬) Queues** tiếp nhận điểm tựa từ **13. công việc (work / 작업) Stealing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. SPSC, MPSC, MPMC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. toàn cục (global / 전역) hàng đợi (queue / 큐) vs cục bộ (local / 로컬) Queues

Toàn cục (global / 전역) hàng đợi (queue / 큐) đơn giản nhưng nhiều worker cùng tranh chấp một khóa (lock / 잠금)/bộ nhớ đệm (cache / 캐시) line.

Per-worker hàng đợi (queue / 큐) giảm contention nhưng tạo imbalance.

Công việc (work / 작업) stealing là một cách kết hợp:

```text
local fast path
+
steal khi thiếu việc
```

Đây là ví dụ hệ thống (system / 시스템) thiết kế (design / 설계) sinh ra từ việc ghép nhiều hàng đợi (queue / 큐) thay vì chỉ tối ưu một hàng đợi (queue / 큐) duy nhất.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **15. SPSC, MPSC, MPMC** tiếp nhận điểm tựa từ **14. toàn cục (global / 전역) hàng đợi (queue / 큐) vs cục bộ (local / 로컬) Queues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Ring Buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. SPSC, MPSC, MPMC

Hàng đợi (queue / 큐) đồng thời cần xác định mô hình producer/bên tiêu thụ (consumer / 소비자):

```text
SPSC -> single producer, single consumer
MPSC -> multiple producer, single consumer
MPMC -> multiple producer, multiple consumer
```

SPSC có thể đơn giản hơn rất nhiều vì quyền sở hữu (ownership / 소유권) của head/tail rõ ràng. MPMC cần giao thức (protocol / 프로토콜) atomic/memory-order phức tạp hơn.

Không nên dùng cấu trúc concurrent tổng quát nếu mô hình thực tế đơn giản hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **16. Ring Buffer** tiếp nhận điểm tựa từ **15. SPSC, MPSC, MPMC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. hàng đợi (queue / 큐) độ sâu (depth / 깊이) không chỉ là chỉ số (metric / 지표) vận hành** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Ring Buffer

Bounded hàng đợi (queue / 큐) thường dùng ring buffer:

```text
buffer[capacity]
head
tail
```

Nếu sức chứa (capacity / 용량) là lũy thừa hai, modulo có thể thay bằng bitmask trong một số hiện thực (implementation / 구현):

```text
index & (capacity - 1)
```

Nhưng tối ưu hóa (optimization / 최적화) này chỉ đúng nếu bất biến (invariant / 불변식) sức chứa (capacity / 용량) được giữ.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **17. hàng đợi (queue / 큐) độ sâu (depth / 깊이) không chỉ là chỉ số (metric / 지표) vận hành** tiếp nhận điểm tựa từ **16. Ring Buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. thử lại (retry / 재시도) Storm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. hàng đợi (queue / 큐) độ sâu (depth / 깊이) không chỉ là chỉ số (metric / 지표) vận hành

Hàng đợi (queue / 큐) độ sâu (depth / 깊이) phản ánh chênh lệch giữa arrival và dịch vụ (service / 서비스) tỷ lệ (rate / 비율).

Một spike ngắn có thể được hàng đợi (queue / 큐) hấp thụ. hàng đợi (queue / 큐) tăng liên tục cho thấy hệ thống không đạt trạng thái ổn định.

Các alert nên nhìn:

```text
queue length
age của item cũ nhất
arrival rate
service rate
rejection/drop rate
processing latency
```

Chỉ nhìn CPU usage có thể bỏ sót backlog.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **18. thử lại (retry / 재시도) Storm** tiếp nhận điểm tựa từ **17. hàng đợi (queue / 큐) độ sâu (depth / 깊이) không chỉ là chỉ số (metric / 지표) vận hành** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Delay hàng đợi (queue / 큐) và Timer vùng nhớ động (heap / 힙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. thử lại (retry / 재시도) Storm

Khi downstream lỗi, upstream có thể thử lại (retry / 재시도). Nếu mọi máy khách (client / 클라이언트) thử lại (retry / 재시도) ngay, arrival tỷ lệ (rate / 비율) tăng đúng lúc sức chứa (capacity / 용량) giảm.

Hàng đợi (queue / 큐)/backpressure cần phối hợp với:

```text
exponential backoff
jitter
retry budget
circuit breaker
```

DSA hàng đợi (queue / 큐) đúng nhưng chính sách (policy / 정책) thử lại (retry / 재시도) sai vẫn làm hệ thống sụp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **19. Delay hàng đợi (queue / 큐) và Timer vùng nhớ động (heap / 힙)** tiếp nhận điểm tựa từ **18. thử lại (retry / 재시도) Storm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Dedup và Idempotency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Delay hàng đợi (queue / 큐) và Timer vùng nhớ động (heap / 힙)

Nếu job chỉ được chạy sau `readyAt`, scheduler cần cấu trúc theo thời gian.

Min-heap theo timestamp:

```text
peek -> job sớm nhất
```

phù hợp khi số timer vừa phải.

Nếu có hàng triệu timer với độ phân giải giới hạn, **timer wheel** có thể hiệu quả hơn vùng nhớ động (heap / 힙) vì bucket hóa thời gian.

Lựa chọn phụ thuộc độ phân giải và quy mô (scale / 규모).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **20. Dedup và Idempotency** tiếp nhận điểm tựa từ **19. Delay hàng đợi (queue / 큐) và Timer vùng nhớ động (heap / 힙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Cancellation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Dedup và Idempotency

Job có thể được gửi lại sau thử lại (retry / 재시도). Nếu side tác động (effect / 효과) không idempotent, xử lý hai lần có thể gây lỗi.

Có thể dùng:

```text
job_id -> processed state
```

trong băm (hash / 해시) Map/cơ sở dữ liệu (database / 데이터베이스) với TTL.

Nhưng dedup trạng thái (state / 상태) cũng tăng theo số job và cần cleanup.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **21. Cancellation** tiếp nhận điểm tựa từ **20. Dedup và Idempotency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Admission điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Cancellation

Nếu job đang trong vùng nhớ động (heap / 힙)/hàng đợi (queue / 큐) bị cancel, xóa tùy ý có thể đắt.

Một chiến lược (strategy / 전략) đơn giản:

```text
cancelled[jobId] = true
```

khi pop thì bỏ qua job đã cancel.

Đây là lazy deletion, tương tự stale entries trong Dijkstra/Priority hàng đợi (queue / 큐).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **22. Admission điều khiển (control / 제어)** tiếp nhận điểm tựa từ **21. Cancellation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Cost-aware Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Admission điều khiển (control / 제어)

Tốt hơn việc nhận mọi job rồi để hàng đợi (queue / 큐) nổ là quyết định ngay từ đầu hệ thống có đủ sức chứa (capacity / 용량) hay không.

Admission điều khiển (control / 제어) có thể dựa trên:

```text
queue depth
concurrency limit
estimated cost
tenant quota
memory budget
```

Một yêu cầu (request / 요청) bị từ chối sớm đôi khi tốt hơn yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) sau 30 giây.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **23. Cost-aware Scheduling** tiếp nhận điểm tựa từ **22. Admission điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Priority Inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Cost-aware Scheduling

Không phải mọi job có chi phí (cost / 비용) giống nhau. Nếu một job cần 10 GB RAM còn job khác cần 100 MB, chỉ priority theo thời gian có thể làm tài nguyên (resource / 자원) fragmentation.

Scheduler có thể mô hình (model / 모델) nhiều tài nguyên:

```text
CPU
memory
GPU
network
```

Bài toán trở thành multidimensional packing/scheduling và có thể khó về mặt tổ hợp.

Đây là ranh giới nơi vùng nhớ động (heap / 힙) đơn giản không còn đủ.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **24. Priority Inversion** tiếp nhận điểm tựa từ **23. Cost-aware Scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Fairness theo tenant** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Priority Inversion

Một tác vụ (task / 작업) priority cao có thể phải chờ khóa (lock / 잠금) đang được tác vụ (task / 작업) priority thấp giữ, trong khi tác vụ (task / 작업) trung bình tiếp tục chạy. Đây là **priority inversion**.

Các cơ chế như priority inheritance xử lý ở tầng synchronization, cho thấy scheduler và khóa (lock / 잠금)/tài nguyên (resource / 자원) đồ thị (graph / 그래프) có liên hệ với nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **25. Fairness theo tenant** tiếp nhận điểm tựa từ **24. Priority Inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. thất bại (failure / 실패) khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Fairness theo tenant

Nếu một tenant gửi 90% traffic, toàn cục (global / 전역) FIFO có thể làm tenant khác chờ lâu.

Per-tenant hàng đợi (queue / 큐) + weighted scheduler cho phép isolation tốt hơn.

Băm (hash / 해시) Map có thể ánh xạ:

```text
tenant_id -> queue state
```

và vùng nhớ động (heap / 힙)/round-robin chọn tenant tiếp theo.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **26. thất bại (failure / 실패) khôi phục (recovery / 복구)** tiếp nhận điểm tựa từ **25. Fairness theo tenant** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. thất bại (failure / 실패) khôi phục (recovery / 복구)

Hàng đợi (queue / 큐) in-memory mất job khi tiến trình (process / 프로세스) crash nếu không có persistence.

Persistent hàng đợi (queue / 큐) phải thêm:

```text
log
ack state
replay
visibility timeout
```

Một cấu trúc FIFO đúng trong RAM chưa đủ cho delivery ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **27. Testing** tiếp nhận điểm tựa từ **26. thất bại (failure / 실패) khôi phục (recovery / 복구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Benchmark** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Testing

Kiểm tra không chỉ thứ tự đầu ra (output / 출력) mà còn bất biến (invariant / 불변식):

```text
không vượt capacity
không mất job
không chạy job đã cancel
priority/tie-break đúng
aging không làm starvation
retry không double-apply side effect theo contract
```

Property-based kiểm thử (test / 테스트) có thể sinh chuỗi enqueue/dequeue/cancel/reprioritize ngẫu nhiên và so với mô hình tham chiếu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **28. Benchmark** tiếp nhận điểm tựa từ **27. Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. chuỗi xử lý (pipeline / 파이프라인) khái niệm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Benchmark

Cần đo:

```text
throughput
p50/p95/p99 latency
queue age
contention theo số worker
allocation/GC
batch size
burst traffic
hot tenant
```

Average thông lượng (throughput / 처리량) tốt nhưng p99 rất xấu có thể không đáp ứng SLA.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **28. Benchmark** xác định đầu vào; **29. chuỗi xử lý (pipeline / 파이프라인) khái niệm** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. chuỗi xử lý (pipeline / 파이프라인) khái niệm

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Incoming Work
   ↓
Admission Control
   ↓
Per-tenant / global queues
   ↓
Priority / fairness scheduler
   ↓
Workers
   ↓
Ack / Retry / DLQ
```

Vòng phản hồi (feedback loop / 피드백 루프):

```text
queue depth + latency
   ↓
backpressure / autoscaling / rejection
```

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Scheduler, hàng đợi (queue / 큐) và Backpressure**, **Mô hình tư duy** gom các mảnh từ **29. chuỗi xử lý (pipeline / 파이프라인) khái niệm** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Scheduler là bài toán **chọn item tiếp theo dưới mục tiêu và ràng buộc tài nguyên**. hàng đợi (queue / 큐) lưu backlog, Priority hàng đợi (queue / 큐) mã hóa thứ tự ưu tiên, Deque hỗ trợ công việc (work / 작업) stealing, băm (hash / 해시) Map giữ trạng thái (state / 상태) theo job/tenant, còn backpressure bảo đảm backlog không biến thành sự cố tài nguyên. cấu trúc dữ liệu (data structure / 자료구조) chỉ là một nửa; chính sách (policy / 정책) và mục tiêu (objective / 목표) mới quyết định hệ thống có công bằng, ổn định và chịu tải tốt hay không.

Xem thêm: [Queue, Deque & Priority Queue](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Problem-Solving Workflow](./02_problem_solving_workflow.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
