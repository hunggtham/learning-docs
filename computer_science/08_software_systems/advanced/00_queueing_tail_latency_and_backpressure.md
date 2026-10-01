# Queueing, tail độ trễ (latency / 지연 시간) và backpressure

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: thông lượng (throughput / 처리량) ổn định không có nghĩa độ trễ (latency / 지연 시간) ổn định** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Queueing delay và dịch vụ (service / 서비스) thời gian (time / 시간) phải đo riêng** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một hệ thống (system / 시스템) có thể còn CPU trung bình nhưng vẫn hết thời gian chờ (timeout / 타임아웃) vì requests đến bursty, dịch vụ (service / 서비스) thời gian (time / 시간) biến động và queues tích tụ. Advanced hiệu năng (performance / 성능) lập luận (reasoning / 추론) vì vậy không dừng ở average độ trễ (latency / 지연 시간) hay utilization; nó theo dõi **arrival tỷ lệ (rate / 비율), dịch vụ (service / 서비스) sức chứa (capacity / 용량), tính đồng thời (concurrency / 동시성), hàng đợi (queue / 큐) debt, percentile độ trễ (latency / 지연 시간) và phản hồi (feedback / 피드백) loops**.

Mô hình tư duy (mental model / 사고 모델) cốt lõi là: **hàng đợi (queue / 큐) là nơi demand gặp một tài nguyên (resource / 자원) hữu hạn**. Khi demand vượt sức chứa (capacity / 용량) đủ lâu, hệ thống phải backpressure, reject, degrade hoặc tích debt. Nếu nó chỉ tiếp tục accept rồi thử lại (retry / 재시도) khi hết thời gian chờ (timeout / 타임아웃), slowdown có thể tự khuếch đại thành cascading thất bại (failure / 실패).

## 1. Bài toán ban đầu: thông lượng (throughput / 처리량) ổn định không có nghĩa độ trễ (latency / 지연 시간) ổn định

Giả sử arrival tỷ lệ (rate / 비율) là `λ` và dịch vụ (service / 서비스) sức chứa (capacity / 용량) trung bình là `μ`. Nếu `λ < μ`, hàng đợi (queue / 큐) có thể drain về lâu dài. Nhưng khi `λ` tiến gần `μ`, một burst hoặc vài slow requests dễ làm hàng đợi (queue / 큐) tăng mạnh vì hệ thống (system / 시스템) không còn headroom để trả debt.

Utilization 90% không đơn giản nghĩa “còn 10%”. Variability làm tail độ trễ (latency / 지연 시간) tăng trước khi đạt 100%.

Vì vậy sức chứa (capacity / 용량) kỹ thuật (engineering / 엔지니어링) cần tìm **utilization knee**: vùng mà tăng tải (load / 로드) nhỏ bắt đầu làm waiting thời gian (time / 시간) tăng phi tuyến.

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **2. Queueing delay và dịch vụ (service / 서비스) thời gian (time / 시간) phải đo riêng** tiếp nhận điểm tựa từ **1. Bài toán ban đầu: thông lượng (throughput / 처리량) ổn định không có nghĩa độ trễ (latency / 지연 시간) ổn định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Little's Law nối tính đồng thời (concurrency / 동시성) với độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Queueing delay và dịch vụ (service / 서비스) thời gian (time / 시간) phải đo riêng

End-to-end độ trễ (latency / 지연 시간) có thể tách mô hình tư duy (mental model / 사고 모델):

```text
W = W_queue + W_service + W_downstream/network
```

Một DB truy vấn (query / 쿼리) chạy 20 ms không chứng minh yêu cầu (request / 요청) chỉ tốn 20 ms ở DB đường dẫn (path / 경로) nếu trước đó chờ 300 ms để acquire liên kết (connection / 연결).

Khi sự cố (incident / 인시던트), câu hỏi đầu tiên nên là:

> công việc (work / 작업) đang chờ **trước tài nguyên (resource / 자원) nào**?

Nếu không tách hàng đợi (queue / 큐) wait, nhóm (team / 팀) thường tối ưu mã (code / 코드) đang chạy thay vì tài nguyên (resource / 자원) đang saturated.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **3. Little's Law nối tính đồng thời (concurrency / 동시성) với độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **2. Queueing delay và dịch vụ (service / 서비스) thời gian (time / 시간) phải đo riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Variability tạo hàng đợi (queue / 큐) ngay cả khi average sức chứa (capacity / 용량) đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Little's Law nối tính đồng thời (concurrency / 동시성) với độ trễ (latency / 지연 시간)

Trong stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

`L` là average number of items trong hệ thống (system / 시스템), `λ` thông lượng (throughput / 처리량) và `W` average thời gian (time / 시간).

Nếu thông lượng (throughput / 처리량) 1000 req/s và average end-to-end thời gian (time / 시간) 0.2 s, trung bình có khoảng 200 requests in-flight.

Little's Law không mô tả tail phân phối (distribution / 분포) và không cứu hệ thống (system / 시스템) unstable, nhưng là sanity check mạnh: nếu tính đồng thời (concurrency / 동시성) observed lệch rất xa estimate, có thể có hidden hàng đợi (queue / 큐), thử lại (retry / 재시도), zombie công việc (work / 작업) hoặc đo lường (measurement / 측정) ranh giới (boundary / 경계) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **4. Variability tạo hàng đợi (queue / 큐) ngay cả khi average sức chứa (capacity / 용량) đủ** tiếp nhận điểm tựa từ **3. Little's Law nối tính đồng thời (concurrency / 동시성) với độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Fan-out khuếch đại tail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Variability tạo hàng đợi (queue / 큐) ngay cả khi average sức chứa (capacity / 용량) đủ

Hai các hệ thống (systems / 시스템들) cùng average dịch vụ (service / 서비스) thời gian (time / 시간) có tail khác nếu variance khác. Một vài slow operations giữ workers/connections lâu hơn, làm requests phía sau chờ.

Sources của variability có thể là:

```text
cache hit vs miss
GC/runtime pause
lock contention
storage GC/checkpoint
network retransmission
replica lag
query plan/data skew
cold start/JIT warm-up
```

Tail độ trễ (latency / 지연 시간) là thuộc tính (property / 속성) của whole chuỗi xử lý (pipeline / 파이프라인), không chỉ slowest đường đi mã (code path / 코드 경로).

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **5. Fan-out khuếch đại tail** tiếp nhận điểm tựa từ **4. Variability tạo hàng đợi (queue / 큐) ngay cả khi average sức chứa (capacity / 용량) đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. thử lại (retry / 재시도) không phải backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Fan-out khuếch đại tail

Nếu một yêu cầu (request / 요청) gọi 20 shards song song và cần đủ tất cả, đường găng (critical path / 임계 경로) gần với slowest required branch. Xác suất gặp ít nhất một tail sự kiện (event / 이벤트) tăng khi fan-out tăng.

Hedged yêu cầu (request / 요청) có thể giảm tail bằng duplicate attempt sau threshold, nhưng tạo tải (load / 로드). Nếu hệ thống (system / 시스템) gần saturation, hedging thiếu ngân sách (budget / 예산) có thể làm tail xấu hơn.

Tối ưu hóa (optimization / 최적화) tail phải tính **extra công việc (work / 작업) generated per người dùng (user / 사용자) yêu cầu (request / 요청)**, không chỉ độ trễ (latency / 지연 시간) của winner.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **6. thử lại (retry / 재시도) không phải backpressure** tiếp nhận điểm tựa từ **5. Fan-out khuếch đại tail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. hết thời gian chờ (timeout / 타임아웃) là deadline quyết định (decision / 결정), không phải cancellation proof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. thử lại (retry / 재시도) không phải backpressure

**Backpressure** nói với producer: downstream không thể nhận công việc (work / 작업) với tốc độ hiện tại.

**thử lại (retry / 재시도)** nói: thử lại một attempt đã thất bại (fail / 실패)/không chắc kết quả (outcome / 결과).

Nếu phụ thuộc (dependency / 의존성) slow vì overload, thử lại (retry / 재시도) thường tạo demand mới đúng lúc `μ` đang giảm.

```text
slowdown
→ timeout
→ retry
→ arrival rate thực tế tăng
→ queue sâu hơn
→ contention/GC/storage pressure tăng
→ service time tăng
→ nhiều timeout hơn
```

Đây là positive vòng phản hồi (feedback loop / 피드백 루프) của **thử lại (retry / 재시도) storm**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **7. hết thời gian chờ (timeout / 타임아웃) là deadline quyết định (decision / 결정), không phải cancellation proof** tiếp nhận điểm tựa từ **6. thử lại (retry / 재시도) không phải backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Deadline cần giảm dần qua lời gọi (call / 호출) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. hết thời gian chờ (timeout / 타임아웃) là deadline quyết định (decision / 결정), không phải cancellation proof

Máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) chỉ nghĩa máy khách (client / 클라이언트) ngừng chờ sau ranh giới (boundary / 경계) nào đó. máy chủ (server / 서버)/downstream có thể vẫn xử lý công việc (work / 작업) cũ.

Nếu thử lại (retry / 재시도) ngay:

```text
attempt 1 vẫn chạy
+
attempt 2 mới bắt đầu
```

Tính đồng thời (concurrency / 동시성) thật tăng dù người dùng (user / 사용자) chỉ có một logical yêu cầu (request / 요청). Với side tác động (effect / 효과), còn có duplicate-effect rủi ro (risk / 위험) nếu thao tác (operation / 연산) thiếu idempotency.

Hết thời gian chờ (timeout / 타임아웃) thiết kế (design / 설계) phải đi cùng deadline propagation, cancellation ngữ nghĩa (semantics / 의미론) và idempotency đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **8. Deadline cần giảm dần qua lời gọi (call / 호출) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **7. hết thời gian chờ (timeout / 타임아웃) là deadline quyết định (decision / 결정), không phải cancellation proof** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Bounded hàng đợi (queue / 큐) biến hidden độ trễ (latency / 지연 시간) thành tường minh (explicit / 명시적) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Deadline cần giảm dần qua lời gọi (call / 호출) đồ thị (graph / 그래프)

Nếu upstream còn 100 ms nhưng downstream hết thời gian chờ (timeout / 타임아웃) 2 s, downstream có thể tiêu tài nguyên (resource / 자원) sau khi kết quả (result / 결과) không còn giá trị.

Một yêu cầu (request / 요청) ngân sách (budget / 예산) hợp lý cần account:

```text
queue wait
network uncertainty
service time
retry budget nếu có
serialization/response path
```

Deadline nên propagate để downstream biết remaining ngân sách (budget / 예산). Không nên reset full hết thời gian chờ (timeout / 타임아웃) ở mỗi hop, vì chuỗi (chain / 사슬) 5 services có thể tạo total wait lớn hơn người dùng (user / 사용자) SLO nhiều lần.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **9. Bounded hàng đợi (queue / 큐) biến hidden độ trễ (latency / 지연 시간) thành tường minh (explicit / 명시적) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **8. Deadline cần giảm dần qua lời gọi (call / 호출) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Backpressure phải reach producer có quyền giảm demand** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Bounded hàng đợi (queue / 큐) biến hidden độ trễ (latency / 지연 시간) thành tường minh (explicit / 명시적) chính sách (policy / 정책)

Unbounded hàng đợi (queue / 큐) tránh reject ngay nhưng đổi dạng thất bại (failure mode / 실패 모드) thành:

```text
memory growth
latency không giới hạn
stale work xử lý sau deadline
OOM / GC pressure
recovery chậm vì backlog
```

Bounded hàng đợi (queue / 큐) buộc hệ thống (system / 시스템) quyết định khi full: reject, khối (block / 블록) producer, shed low-priority công việc (work / 작업) hoặc degrade.

Đây không chỉ là hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화); nó làm thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) tường minh (explicit / 명시적).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **10. Backpressure phải reach producer có quyền giảm demand** tiếp nhận điểm tựa từ **9. Bounded hàng đợi (queue / 큐) biến hidden độ trễ (latency / 지연 시간) thành tường minh (explicit / 명시적) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + tính đồng thời (concurrency / 동시성) limiter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Backpressure phải reach producer có quyền giảm demand

Một nội bộ (internal / 내부) hàng đợi (queue / 큐) báo “full” nhưng upstream tiếp tục enqueue ở hàng đợi (queue / 큐) khác thì pressure chỉ bị dời chỗ.

Backpressure effective khi tín hiệu (signal / 신호) đi tới ranh giới (boundary / 경계) có thể:

```text
stop reading socket
reduce concurrency
pause producer
reduce fetch/poll rate
reject admission
slow tenant/client
```

Nếu mỗi tầng (layer / 계층) có unbounded buffer, hệ thống (system / 시스템) trông stable tới khi toàn bộ buffers cùng đầy.

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **10. Backpressure phải reach producer có quyền giảm demand** đã nêu tiêu chí phân biệt, còn **11. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + tính đồng thời (concurrency / 동시성) limiter** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trong safe operating region** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + tính đồng thời (concurrency / 동시성) limiter

DB pool 50 connections không chỉ reuse connections; nó cap tối đa 50 active operations qua ranh giới (boundary / 경계) đó. Requests còn lại chờ acquire.

Tăng pool kích thước (size / 크기) có thể giảm ứng dụng (application / 애플리케이션) wait nhưng chuyển tính đồng thời (concurrency / 동시성) xuống DB. Khi DB đã saturated, pool lớn hơn làm khóa (lock / 잠금)/I/O/bộ nhớ đệm (cache / 캐시) contention tăng và dịch vụ (service / 서비스) thời gian (time / 시간) xấu hơn.

Pool sizing phải dựa tài nguyên (resource / 자원) bottleneck thật, không dựa “nhiều liên kết (connection / 연결) hơn = nhanh hơn”.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **11. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + tính đồng thời (concurrency / 동시성) limiter** đã nêu tiêu chí phân biệt, còn **12. Admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trong safe operating region** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. tải (load / 로드) shedding bảo vệ bất biến (invariant / 불변식) quan trọng hơn success-rate tức thời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trong safe operating region

Khi overload, hệ thống (system / 시스템) cần ngăn accepted công việc (work / 작업) vượt khả năng hoàn tất hữu ích trước deadline.

Admission có thể dựa:

```text
max concurrency
queue occupancy
estimated cost
tenant quota
priority class
current saturation signal
```

Reject sớm một phần requests có thể làm success count thực tế cao hơn việc accept 100% rồi để 100% hết thời gian chờ (timeout / 타임아웃).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **13. tải (load / 로드) shedding bảo vệ bất biến (invariant / 불변식) quan trọng hơn success-rate tức thời** tiếp nhận điểm tựa từ **12. Admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trong safe operating region** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Priority chỉ có nghĩa khi tài nguyên (resource / 자원) được phân lập hoặc schedule công bằng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. tải (load / 로드) shedding bảo vệ bất biến (invariant / 불변식) quan trọng hơn success-rate tức thời

Hệ thống (system / 시스템) có thể skip optional enrichment, serve stale bộ nhớ đệm (cache / 캐시), reject expensive reports hoặc degrade non-critical tính năng (feature / 기능) để giữ cốt lõi (core / 핵심) giao dịch (transaction / 트랜잭션) đường dẫn (path / 경로) khỏe.

Nhưng degrade chính sách (policy / 정책) phải biết phụ thuộc (dependency / 의존성)/bất biến (invariant / 불변식). Không thể serve stale authorization quyết định (decision / 결정) nếu bảo mật (security / 보안) đặc tả hợp đồng (contract / 계약) yêu cầu fresh revoke trạng thái (state / 상태), chẳng hạn.

Độ tin cậy (reliability / 신뢰성) tối ưu hóa (optimization / 최적화) luôn bị ràng buộc (constraint / 제약조건) bởi tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) bất biến (invariant / 불변식).

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **13. tải (load / 로드) shedding bảo vệ bất biến (invariant / 불변식) quan trọng hơn success-rate tức thời** nêu điều cần giải thích; **14. Priority chỉ có nghĩa khi tài nguyên (resource / 자원) được phân lập hoặc schedule công bằng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Multi-tenant noisy neighbor là hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Priority chỉ có nghĩa khi tài nguyên (resource / 자원) được phân lập hoặc schedule công bằng

Gắn `priority=high` vào yêu cầu (request / 요청) không giúp nếu high/low cùng tranh một exhausted FIFO pool.

Priority cần enforcement tại tài nguyên (resource / 자원):

```text
reserved concurrency
weighted fair queue
separate pool
preemption khi safe
per-class admission
```

Nếu không, low-priority burst có thể giữ toàn bộ connections trước khi high-priority traffic tới.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **14. Priority chỉ có nghĩa khi tài nguyên (resource / 자원) được phân lập hoặc schedule công bằng** nêu điều cần giải thích; **15. Multi-tenant noisy neighbor là hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권) bài toán (problem / 문제)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. đơn vị từ (token / 토큰) bucket và tỷ lệ (rate / 비율) limit kiểm soát tỷ lệ (rate / 비율) nhưng chưa chắc kiểm soát tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Multi-tenant noisy neighbor là hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권) bài toán (problem / 문제)

Một tenant có thể hợp lệ nhưng tạo tải công việc (workload / 워크로드) lớn. Nếu mọi tenant share hàng đợi (queue / 큐)/pool/bộ nhớ đệm (cache / 캐시) mà không quota/fairness, một tenant làm p99 của tất cả tăng.

Useful bất biến (invariant / 불변식):

> Demand của tenant A không được tiêu toàn bộ sức chứa (capacity / 용량) cần thiết để giữ SLO tối thiểu của tenant B, theo isolation chính sách (policy / 정책) đã công bố.

Cơ chế (mechanism / 메커니즘) có thể là weighted fair scheduling, tính đồng thời (concurrency / 동시성) quota, đơn vị từ (token / 토큰) bucket, per-tenant queues hoặc partitioned tài nguyên (resource / 자원). chính xác (exact / 정확한) choice phụ thuộc tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **15. Multi-tenant noisy neighbor là hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권) bài toán (problem / 문제)** đã nêu tiêu chí phân biệt, còn **16. đơn vị từ (token / 토큰) bucket và tỷ lệ (rate / 비율) limit kiểm soát tỷ lệ (rate / 비율) nhưng chưa chắc kiểm soát tính đồng thời (concurrency / 동시성)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **17. Backoff + jitter giảm synchronization nhưng không tạo sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. đơn vị từ (token / 토큰) bucket và tỷ lệ (rate / 비율) limit kiểm soát tỷ lệ (rate / 비율) nhưng chưa chắc kiểm soát tính đồng thời (concurrency / 동시성)

Một yêu cầu (request / 요청) có thể nhanh hoặc rất chậm. Cùng 100 req/s nhưng dịch vụ (service / 서비스) thời gian (time / 시간) 10 ms tạo tính đồng thời (concurrency / 동시성) khác 2 s.

Tỷ lệ (rate / 비율) limit bảo vệ arrival tỷ lệ (rate / 비율); tính đồng thời (concurrency / 동시성) limiter bảo vệ number of active costly operations. các hệ thống (systems / 시스템들) thường cần cả hai nếu yêu cầu (request / 요청) chi phí (cost / 비용)/độ trễ (latency / 지연 시간) biến động.

Weighted admission hữu ích khi endpoint/mô hình (model / 모델)/truy vấn (query / 쿼리) có chi phí (cost / 비용) rất khác nhau.

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **16. đơn vị từ (token / 토큰) bucket và tỷ lệ (rate / 비율) limit kiểm soát tỷ lệ (rate / 비율) nhưng chưa chắc kiểm soát tính đồng thời (concurrency / 동시성)** đã nêu tiêu chí phân biệt, còn **17. Backoff + jitter giảm synchronization nhưng không tạo sức chứa (capacity / 용량)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **18. Circuit breaker là máy trạng thái (state machine / 상태 머신), không phải magic shield** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Backoff + jitter giảm synchronization nhưng không tạo sức chứa (capacity / 용량)

Exponential backoff giảm thử lại (retry / 재시도) frequency; jitter tránh clients wake cùng lúc. thử lại (retry / 재시도) ngân sách (budget / 예산) giới hạn tổng extra attempts.

Nhưng nếu phụ thuộc (dependency / 의존성) mất sức chứa (capacity / 용량) lâu dài, backoff chỉ giảm damage. hệ thống (system / 시스템) vẫn cần tải (load / 로드) shedding, failover sức chứa (capacity / 용량), repair hoặc demand reduction.

Thử lại (retry / 재시도) chính sách (policy / 정책) nên phân loại:

```text
transient/retryable
permanent/non-retryable
unknown-outcome requiring idempotency
```

Blind thử lại (retry / 재시도) mọi 5xx/hết thời gian chờ (timeout / 타임아웃) là tải (load / 로드) generator.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **18. Circuit breaker là máy trạng thái (state machine / 상태 머신), không phải magic shield** tiếp nhận điểm tựa từ **17. Backoff + jitter giảm synchronization nhưng không tạo sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. hàng đợi (queue / 큐) placement quyết định nơi chính sách (policy / 정책) và bằng chứng (evidence / 증거) tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Circuit breaker là máy trạng thái (state machine / 상태 머신), không phải magic shield

Circuit breaker quan sát failures và tạm ngừng calls để giảm pressure. Nhưng threshold/cửa sổ (window / 윈도우)/half-open probes tạo own hành vi (behavior / 동작).

Nếu mở quá nhạy, transient blip biến thành self-inflicted outage; nếu đóng quá lâu, phụ thuộc (dependency / 의존성) tiếp tục bị hammered. Half-open probes phải bounded để khôi phục (recovery / 복구) traffic không tạo thundering herd.

Breaker chỉ hữu ích khi caller có fallback/reject hành vi (behavior / 동작) phù hợp; nó không chữa phụ thuộc (dependency / 의존성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **18. Circuit breaker là máy trạng thái (state machine / 상태 머신), không phải magic shield** nêu điều cần giải thích; **19. hàng đợi (queue / 큐) placement quyết định nơi chính sách (policy / 정책) và bằng chứng (evidence / 증거) tồn tại** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Overload làm dịch vụ (service / 서비스) tỷ lệ (rate / 비율) giảm, không chỉ hàng đợi (queue / 큐) tăng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. hàng đợi (queue / 큐) placement quyết định nơi chính sách (policy / 정책) và bằng chứng (evidence / 증거) tồn tại

Có thể có hàng đợi (queue / 큐) ở:

```text
load balancer
kernel accept/socket buffers
runtime executor/event loop
application work queue
DB connection pool
database lock manager
storage device
```

Ba queues mỗi nơi “chỉ 100 ms” đã tạo 300+ ms trước dịch vụ (service / 서비스) công việc (work / 작업).

Hàng đợi (queue / 큐) nên nằm nơi hệ thống (system / 시스템) hiểu deadline, priority, quyền sở hữu (ownership / 소유권) và sức chứa (capacity / 용량) tốt nhất; hidden queues ở lower tầng (layer / 계층) cần khả năng quan sát (observability / 관측 가능성) vì chúng vẫn thuộc đường găng (critical path / 임계 경로).

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **19. hàng đợi (queue / 큐) placement quyết định nơi chính sách (policy / 정책) và bằng chứng (evidence / 증거) tồn tại** nêu điều cần giải thích; **20. Overload làm dịch vụ (service / 서비스) tỷ lệ (rate / 비율) giảm, không chỉ hàng đợi (queue / 큐) tăng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. khôi phục (recovery / 복구) cũng cần admission điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Overload làm dịch vụ (service / 서비스) tỷ lệ (rate / 비율) giảm, không chỉ hàng đợi (queue / 큐) tăng

Simple queueing mô hình (model / 모델) hay giả định `μ` cố định. môi trường vận hành (production / 운영 환경) overload thường làm `μ` giảm vì:

```text
context switches ↑
cache locality ↓
GC pressure ↑
lock contention ↑
storage queue/GC ↑
DB plan/cache churn ↑
retry bookkeeping ↑
```

Do đó vượt knee có thể tạo **overload collapse**: thêm demand làm thông lượng (throughput / 처리량) useful giảm.

Đây là lý do headroom quan trọng hơn chạy sát 100% utilization.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **21. khôi phục (recovery / 복구) cũng cần admission điều khiển (control / 제어)** tiếp nhận điểm tựa từ **20. Overload làm dịch vụ (service / 서비스) tỷ lệ (rate / 비율) giảm, không chỉ hàng đợi (queue / 큐) tăng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. bằng chứng vận hành (production evidence / 운영 증거) phải theo luồng (flow / 흐름) của công việc (work / 작업)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. khôi phục (recovery / 복구) cũng cần admission điều khiển (control / 제어)

Sau outage, backlog + retries + reconnects có thể tạo **khôi phục (recovery / 복구) storm**. Nếu phụ thuộc (dependency / 의존성) vừa hồi và toàn fleet gửi traffic cùng lúc, nó lại collapse.

Khôi phục (recovery / 복구) đường dẫn (path / 경로) nên ramp traffic, jitter reconnect, limit replay consumers và prioritize fresh/trọng yếu (critical / 중요) công việc (work / 작업) khi nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) cho phép.

“dịch vụ (service / 서비스) healthy again” không đồng nghĩa “dịch vụ (service / 서비스) chịu được toàn backlog ngay lập tức”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **21. khôi phục (recovery / 복구) cũng cần admission điều khiển (control / 제어)** nêu điều cần giải thích; **22. bằng chứng vận hành (production evidence / 운영 증거) phải theo luồng (flow / 흐름) của công việc (work / 작업)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. hiệu năng (performance / 성능) experiments phải tìm knee và vòng phản hồi (feedback loop / 피드백 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. bằng chứng vận hành (production evidence / 운영 증거) phải theo luồng (flow / 흐름) của công việc (work / 작업)

Bằng chứng (evidence / 증거) hữu ích:

```text
Demand:
- original request rate
- attempt/retry/hedge rate
- per-tenant/per-class rate

Queues:
- queue depth
- queue wait distribution
- oldest item age
- reject/shed count

Capacity:
- active workers/connections
- saturation/utilization
- service time distribution
- downstream pool/storage/runtime state

Deadlines:
- timeout rate by hop
- cancellation success/late completion
- work completed after caller deadline
```

Một CPU đồ thị (graph / 그래프) không chỉ ra hidden DB pool hàng đợi (queue / 큐); p99 alone không chỉ ra attempt amplification.

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **22. bằng chứng vận hành (production evidence / 운영 증거) phải theo luồng (flow / 흐름) của công việc (work / 작업)** nêu điều cần giải thích; **23. hiệu năng (performance / 성능) experiments phải tìm knee và vòng phản hồi (feedback loop / 피드백 루프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. hiệu năng (performance / 성능) experiments phải tìm knee và vòng phản hồi (feedback loop / 피드백 루프)

Kiểm thử tải (load test / 부하 테스트) nên ramp demand và giữ đủ lâu để background debt xuất hiện. Ghi lại thông lượng (throughput / 처리량) useful, attempt tỷ lệ (rate / 비율), hàng đợi (queue / 큐) wait, saturation và p50/p95/p99.

Nếu QPS người dùng (user / 사용자) tăng 10% nhưng attempt tỷ lệ (rate / 비율) tăng 40% do thử lại (retry / 재시도), benchmark phải coi extra attempts là part of tải (load / 로드). Nếu thông lượng (throughput / 처리량) useful plateau rồi giảm, đã bước vào collapse region.

> **Chuyển mạch:** Ở chặng này của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **24. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** tiếp nhận điểm tựa từ **23. hiệu năng (performance / 성능) experiments phải tìm knee và vòng phản hồi (feedback loop / 피드백 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Nếu yêu cầu (request / 요청) chậm nhưng CPU thấp, tìm hàng đợi (queue / 큐) trước pool/I/O/mạng (network / 네트워크). Nếu hết thời gian chờ (timeout / 타임아웃) tăng cùng thử lại (retry / 재시도) tỷ lệ (rate / 비율), inspect amplification. Nếu one tenant làm tất cả chậm, inspect fairness/tài nguyên (resource / 자원) isolation. Nếu adding threads worsens thông lượng (throughput / 처리량), lower bottleneck/contended tài nguyên (resource / 자원) đang quyết định dịch vụ (service / 서비스) tỷ lệ (rate / 비율).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **25. Mô hình tư duy** gom các mảnh từ **24. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Mô hình tư duy

> hàng đợi (queue / 큐) là **debt của demand đối với sức chứa (capacity / 용량)**. Tail độ trễ (latency / 지연 시간) tăng khi variability và saturation làm debt khó trả. hết thời gian chờ (timeout / 타임아웃) có thể bỏ người chờ nhưng không xóa công việc (work / 작업); thử lại (retry / 재시도) có thể nhân demand; backpressure và admission điều khiển (control / 제어) giữ debt bounded; fairness quyết định ai được dùng sức chứa (capacity / 용량); tải (load / 로드) shedding giữ hệ thống (system / 시스템) trong safe region. **Khi sự cố (incident / 인시던트) độ trễ (latency / 지연 시간) xảy ra, hãy tìm hàng đợi (queue / 큐), quyền sở hữu (ownership / 소유권) và vòng phản hồi (feedback loop / 피드백 루프) trước khi chỉ tối ưu mã (code / 코드).**

> **Chuyển mạch:** Trong **Queueing, tail độ trễ (latency / 지연 시간) và backpressure**, **Kết nối** gom các mảnh từ **25. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [performance/capacity](../../basic/08_software_systems/02_performance_capacity_and_scalability.md), [state/queues/backpressure](../../basic/08_software_systems/03_state_queues_backpressure_and_boundaries.md) và [reliability](../../basic/07_security_reliability/05_fault_tolerance_observability_and_reliability.md). Đọc tiếp [capacity/admission control](./01_capacity_planning_utilization_knee_and_admission_control.md), [load balancing/pools](./03_load_balancing_connection_pools_and_locality.md), [async runtime](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md) và [end-to-end request/retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
