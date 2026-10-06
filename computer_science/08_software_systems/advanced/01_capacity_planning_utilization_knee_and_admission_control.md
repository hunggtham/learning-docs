# Sức chứa (capacity / 용량) planning, utilization knee và admission điều khiển (control / 제어)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Capacity planning, utilization knee và admission control**. Route đi từ safe operating envelope → utilization/queueing knee → demand forecast/headroom → admission limits/load shedding → capacity evidence, để giới hạn được đặt trước khi overload.

Sức chứa (capacity / 용량) planning không phải lấy peak traffic rồi cộng 20%. Một dịch vụ (service / 서비스) có thể vẫn còn thông lượng (throughput / 처리량) sức chứa (capacity / 용량) nhưng tail độ trễ (latency / 지연 시간) đã tăng mạnh vì queueing và contention. Ở mức advanced, cần giữ một bất biến (invariant / 불변식) vận hành: **accepted công việc (work / 작업) phải nằm trong vùng mà hệ thống (system / 시스템) còn đủ tài nguyên (resource / 자원) để hoàn thành trước deadline với xác suất/SLO đã công bố.**

Khi hệ thống (system / 시스템) tiếp tục accept công việc (work / 작업) sau vùng đó, hàng đợi (queue / 큐) debt, hết thời gian chờ (timeout / 타임아웃) và thử lại (retry / 재시도) có thể biến slowdown thành overload collapse.

## 1. sức chứa (capacity / 용량) là một safe operating envelope

Một dịch vụ (service / 서비스) có nhiều bottleneck resources: CPU, bộ nhớ (memory / 메모리)/GC, luồng thực thi (thread / 스레드) hoặc event-loop tính đồng thời (concurrency / 동시성), DB connections, sockets/tệp (file / 파일) descriptors, I/O bandwidth, mạng (network / 네트워크) bandwidth, downstream quota và locks/trạng thái dùng chung (shared state / 공유 상태).

Thông lượng (throughput / 처리량) tối đa bị giới hạn bởi tài nguyên (resource / 자원) đầu tiên saturate hoặc bởi tương tác (interaction / 상호작용) giữa nhiều resources. CPU 40% không chứng minh dịch vụ (service / 서비스) còn nhiều sức chứa (capacity / 용량) nếu DB pool đã 100% busy.

Sức chứa (capacity / 용량) vì vậy là một **vùng đa chiều**, không phải một số RPS duy nhất.

> **Nối mạch:** **2. Utilization knee quan trọng hơn maximum thông lượng (throughput / 처리량)** nối từ **1. sức chứa (capacity / 용량) là một safe operating envelope** sang **3. Little's Law nối thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và độ trễ (latency / 지연 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Utilization knee quan trọng hơn maximum thông lượng (throughput / 처리량)

Khi arrival tỷ lệ (rate / 비율) tiến gần dịch vụ (service / 서비스) sức chứa (capacity / 용량), variance nhỏ cũng tạo hàng đợi (queue / 큐). độ trễ (latency / 지연 시간) thường cong mạnh trước khi tài nguyên (resource / 자원) đạt 100%.

Điểm chuyển từ “dịch vụ (service / 서비스) thời gian (time / 시간) chi phối” sang “hàng đợi (queue / 큐) wait chi phối” thường được gọi không chính thức là **utilization knee**.

Latency-sensitive hệ thống (system / 시스템) nên operate trước vùng này và giữ headroom cho burst, deploy, instance thất bại (failure / 실패) hoặc downstream degradation.

> **Nối mạch:** **3. Little's Law nối thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và độ trễ (latency / 지연 시간)** nối từ **2. Utilization knee quan trọng hơn maximum thông lượng (throughput / 처리량)** sang **4. Service-time phân phối (distribution / 분포) quan trọng hơn average**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Little's Law nối thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và độ trễ (latency / 지연 시간)

Trong stable hệ thống (system / 시스템):

```text
L = λW
```

`L` là số yêu cầu (request / 요청) trung bình trong hệ thống (system / 시스템), `λ` thông lượng (throughput / 처리량)/arrival tỷ lệ (rate / 비율), `W` average thời gian (time / 시간) trong hệ thống (system / 시스템).

Nếu thông lượng (throughput / 처리량) 1,000 req/s và average end-to-end thời gian (time / 시간) 0.2 s, trung bình khoảng 200 requests đang in-flight.

Little's Law không mô tả tail phân phối (distribution / 분포), nhưng là sanity check mạnh để phát hiện pool/tính đồng thời (concurrency / 동시성) các giả định (assumptions / 가정들) phi thực tế.

> **Nối mạch:** **4. Service-time phân phối (distribution / 분포) quan trọng hơn average** nối từ **3. Little's Law nối thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và độ trễ (latency / 지연 시간)** sang **5. tính đồng thời (concurrency / 동시성) limit là một điều khiển (control / 제어) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Service-time phân phối (distribution / 분포) quan trọng hơn average

Nếu 99% requests mất 5 ms nhưng 1% mất 1 s, slow requests giữ worker/liên kết (connection / 연결) lâu và có thể gây head-of-line blocking.

Sức chứa (capacity / 용량) mô hình (model / 모델) cần tải công việc (workload / 워크로드) mix, percentile dịch vụ (service / 서비스) thời gian (time / 시간) và phụ thuộc (dependency / 의존성) hành vi (behavior / 동작). Average dịch vụ (service / 서비스) thời gian (time / 시간) có thể che đúng lớp (class / 클래스) yêu cầu (request / 요청) đang giữ tài nguyên (resource / 자원) lâu nhất.

> **Nối mạch:** **4. Service-time phân phối (distribution / 분포) quan trọng hơn average** đặt tiêu chí; **5. tính đồng thời (concurrency / 동시성) limit là một điều khiển (control / 제어) ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **6. Admission điều khiển (control / 제어) quyết định công việc (work / 작업) có được vào expensive đường dẫn (path / 경로) hay không** mở rộng hệ quả.

## 5. tính đồng thời (concurrency / 동시성) limit là một điều khiển (control / 제어) ranh giới (boundary / 경계)

Tăng threads/connections vô hạn không tăng thông lượng (throughput / 처리량) vô hạn. Sau một mức, ngữ cảnh (context / 맥락) switch, trượt bộ nhớ đệm (cache miss / 캐시 미스), GC, tranh chấp khóa (lock contention / 잠금 경합) và downstream saturation làm **dịch vụ (service / 서비스) thời gian (time / 시간) tự tăng**.

Tính đồng thời (concurrency / 동시성) limiting đặt upper bound active công việc (work / 작업). Excess công việc (work / 작업) có thể hàng đợi (queue / 큐) có giới hạn hoặc bị reject sớm.

Mục tiêu không phải giữ mọi yêu cầu (request / 요청) “đã được nhận”, mà giữ active set trong vùng mà tài nguyên (resource / 자원) còn làm useful progress.

> **Nối mạch:** **5. tính đồng thời (concurrency / 동시성) limit là một điều khiển (control / 제어) ranh giới (boundary / 경계)** đặt tiêu chí; **6. Admission điều khiển (control / 제어) quyết định công việc (work / 작업) có được vào expensive đường dẫn (path / 경로) hay không** dùng nó để kiểm tra ranh giới, rồi **7. Bounded hàng đợi (queue / 큐) biến overload thành thất bại (failure / 실패) hữu hạn** mở rộng hệ quả.

## 6. Admission điều khiển (control / 제어) quyết định công việc (work / 작업) có được vào expensive đường dẫn (path / 경로) hay không

Admission điều khiển (control / 제어) có thể dựa trên semaphore, hàng đợi (queue / 큐) length, đơn vị từ (token / 토큰)/tỷ lệ (rate / 비율) ngân sách (budget / 예산), tenant quota hoặc estimated yêu cầu (request / 요청) chi phí (cost / 비용).

Một `429/503` nhanh đôi khi đúng hơn accept rồi hết thời gian chờ (timeout / 타임아웃) 30 giây. Reject sớm bảo vệ tài nguyên (resource / 자원) cho công việc (work / 작업) đã nhận và cho caller tín hiệu (signal / 신호) rõ để backoff hoặc degrade.

Bất biến (invariant / 불변식) là rejection phải xảy ra **trước** khi yêu cầu (request / 요청) tiêu quá nhiều tài nguyên (resource / 자원) khan hiếm.

> **Nối mạch:** **6. Admission điều khiển (control / 제어) quyết định công việc (work / 작업) có được vào expensive đường dẫn (path / 경로) hay không** đặt đầu vào cho **7. Bounded hàng đợi (queue / 큐) biến overload thành thất bại (failure / 실패) hữu hạn**, rồi **8. thử lại (retry / 재시도) amplification tạo positive vòng phản hồi (feedback loop / 피드백 루프)** mở rộng hệ quả.

## 7. Bounded hàng đợi (queue / 큐) biến overload thành thất bại (failure / 실패) hữu hạn

Unbounded hàng đợi (queue / 큐) không loại thất bại (failure / 실패); nó đổi thất bại (failure / 실패) thành độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리) debt.

Nếu worker dịch vụ (service / 서비스) thời gian (time / 시간) là 100 ms nhưng hàng đợi (queue / 큐) cho phép hàng chục nghìn requests, nhiều yêu cầu (request / 요청) đã chắc chắn vượt deadline ngay lúc enqueue.

Hàng đợi (queue / 큐) sức chứa (capacity / 용량) cần liên hệ với độ trễ (latency / 지연 시간) ngân sách (budget / 예산) và cancellation ngữ nghĩa (semantics / 의미론). công việc (work / 작업) đã hết deadline không nên tiếp tục giữ slot nếu có thể hủy an toàn.

> **Nối mạch:** **8. thử lại (retry / 재시도) amplification tạo positive vòng phản hồi (feedback loop / 피드백 루프)** nối từ **7. Bounded hàng đợi (queue / 큐) biến overload thành thất bại (failure / 실패) hữu hạn** sang **9. tính đồng thời (concurrency / 동시성) limit khác tỷ lệ (rate / 비율) limit**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. thử lại (retry / 재시도) amplification tạo positive vòng phản hồi (feedback loop / 피드백 루프)

Máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) nhưng máy chủ (server / 서버) vẫn xử lý. máy khách (client / 클라이언트) thử lại (retry / 재시도) tạo thêm attempt. tải (load / 로드) tăng làm hàng đợi (queue / 큐) dài, dịch vụ (service / 서비스) thời gian (time / 시간) xấu, thêm hết thời gian chờ (timeout / 타임아웃) và thêm thử lại (retry / 재시도).

```text
slowdown
→ timeout
→ retry
→ arrival rate tăng
→ queue + contention tăng
→ service time tăng
→ nhiều timeout hơn
```

Mitigation gồm bounded retries, exponential backoff, jitter, thử lại (retry / 재시도) ngân sách (budget / 예산), deadline propagation và idempotency. Nhưng nếu phụ thuộc (dependency / 의존성) hết sức chứa (capacity / 용량) kéo dài, thử lại (retry / 재시도) chính sách (policy / 정책) không tạo sức chứa (capacity / 용량); admission/backpressure vẫn cần.

> **Nối mạch:** **8. thử lại (retry / 재시도) amplification tạo positive vòng phản hồi (feedback loop / 피드백 루프)** đặt tiêu chí; **9. tính đồng thời (concurrency / 동시성) limit khác tỷ lệ (rate / 비율) limit** dùng nó để kiểm tra ranh giới, rồi **10. Adaptive tính đồng thời (concurrency / 동시성) là điều khiển (control / 제어) lý thuyết (theory / 이론) bài toán (problem / 문제)** mở rộng hệ quả.

## 9. tính đồng thời (concurrency / 동시성) limit khác tỷ lệ (rate / 비율) limit

Tỷ lệ (rate / 비율) limit kiểm soát arrivals per thời gian (time / 시간). tính đồng thời (concurrency / 동시성) limit kiểm soát active công việc (work / 작업).

Thao tác (operation / 연산) 5 ms và 5 s có thể cùng QPS nhưng tài nguyên (resource / 자원) footprint khác rất nhiều. Với dịch vụ (service / 서비스) thời gian (time / 시간) biến động, tính đồng thời (concurrency / 동시성) thường phản ánh pressure trực tiếp hơn tỷ lệ (rate / 비율).

Nhiều hệ thống (system / 시스템) cần cả hai: tỷ lệ (rate / 비율) để bảo vệ abuse/burst, tính đồng thời (concurrency / 동시성) để bảo vệ finite downstream sức chứa (capacity / 용량).

> **Nối mạch:** **9. tính đồng thời (concurrency / 동시성) limit khác tỷ lệ (rate / 비율) limit** đặt tiêu chí; **10. Adaptive tính đồng thời (concurrency / 동시성) là điều khiển (control / 제어) lý thuyết (theory / 이론) bài toán (problem / 문제)** dùng nó để kiểm tra ranh giới, rồi **11. Bulkhead tạo failure-domain ranh giới (boundary / 경계)** mở rộng hệ quả.

## 10. Adaptive tính đồng thời (concurrency / 동시성) là điều khiển (control / 제어) lý thuyết (theory / 이론) bài toán (problem / 문제)

Static limit có thể sai khi downstream sức chứa (capacity / 용량) thay đổi. Adaptive controller quan sát độ trễ (latency / 지연 시간)/lỗi (error / 오류)/hàng đợi (queue / 큐) rồi điều chỉnh tính đồng thời (concurrency / 동시성).

Phản ứng quá nhanh gây oscillation; quá chậm cho overload lan rộng. đo lường (measurement / 측정) delay và noisy tail metrics có thể làm controller chase noise.

Adaptive limit phải lập luận (reasoning / 추론) như phản hồi (feedback / 피드백) controller, không phải magic autoscaling switch.

> **Nối mạch:** **10. Adaptive tính đồng thời (concurrency / 동시성) là điều khiển (control / 제어) lý thuyết (theory / 이론) bài toán (problem / 문제)** đặt tiêu chí; **11. Bulkhead tạo failure-domain ranh giới (boundary / 경계)** dùng nó để kiểm tra ranh giới, rồi **12. Headroom cho thất bại (failure / 실패) và deploy** mở rộng hệ quả.

## 11. Bulkhead tạo failure-domain ranh giới (boundary / 경계)

Chia tài nguyên (resource / 자원) pools theo tải công việc (workload / 워크로드)/tenant có thể ngăn một lớp (class / 클래스) ăn hết sức chứa (capacity / 용량).

Ví dụ background export và user-facing yêu cầu (request / 요청) dùng pools riêng. Điều này có thể làm tổng utilization kém tối ưu ở một số thời điểm, nhưng tăng fault isolation.

Isolation chỉ thật khi tài nguyên (resource / 자원) được reserve/partition ở tầng (layer / 계층) bottleneck. Hai logical priority classes cùng dùng một exhausted DB pool không phải bulkhead thực sự.

> **Nối mạch:** **11. Bulkhead tạo failure-domain ranh giới (boundary / 경계)** đặt tiêu chí; **12. Headroom cho thất bại (failure / 실패) và deploy** dùng nó để kiểm tra ranh giới, rồi **13. Autoscaling không thay admission điều khiển (control / 제어)** mở rộng hệ quả.

## 12. Headroom cho thất bại (failure / 실패) và deploy

Cluster 10 nodes muốn chịu mất 2 nodes thì 8 nodes còn lại phải tiếp tục nằm trước utilization knee. Rolling triển khai (deployment / 배포), autoscaling warm-up, zone thất bại (failure / 실패) và bộ nhớ đệm (cache / 캐시) cold-start đều tiêu headroom.

Sức chứa (capacity / 용량) planning vì thế là độ tin cậy (reliability / 신뢰성) yêu cầu (requirement / 요구사항), không chỉ chi phí (cost / 비용) tối ưu hóa (optimization / 최적화).

> **Nối mạch:** **13. Autoscaling không thay admission điều khiển (control / 제어)** nối từ **12. Headroom cho thất bại (failure / 실패) và deploy** sang **14. Graceful degradation phải giữ correctness-critical bất biến (invariant / 불변식)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Autoscaling không thay admission điều khiển (control / 제어)

Autoscaler phản ứng sau chỉ số (metric / 지표) thay đổi (change / 변경) và instance cần startup/warmup. Burst có thể phá hệ thống (system / 시스템) trước khi scale-out hoàn tất.

Admission điều khiển (control / 제어)/tải (load / 로드) shedding bảo vệ trong transient cửa sổ (window / 윈도우) đó. Scale-out cũng không giúp nếu bottleneck là DB, dùng chung (shared / 공유) khóa (lock / 잠금) hoặc downstream quota.

> **Nối mạch:** **14. Graceful degradation phải giữ correctness-critical bất biến (invariant / 불변식)** nối từ **13. Autoscaling không thay admission điều khiển (control / 제어)** sang **15. bằng chứng vận hành (production evidence / 운영 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Graceful degradation phải giữ correctness-critical bất biến (invariant / 불변식)

Khi overload, hệ thống (system / 시스템) có thể bỏ optional enrichment, phục vụ stale bộ nhớ đệm (cache / 캐시), giảm chất lượng recommendation hoặc reject low-priority công việc (work / 작업).

Nhưng không được “degrade” bằng cách bỏ authorization, durability hoặc nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증) chỉ để giữ success tỷ lệ (rate / 비율). Degradation chính sách (policy / 정책) cần phân biệt optional chất lượng (quality / 품질) với tính đúng đắn (correctness / 정확성)/bảo mật (security / 보안) bất biến (invariant / 불변식).

> **Nối mạch:** **14. Graceful degradation phải giữ correctness-critical bất biến (invariant / 불변식)** đặt vấn đề; **15. bằng chứng vận hành (production evidence / 운영 증거)** kiểm tra bằng chứng, rồi **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** mở rộng hệ quả.

## 15. bằng chứng vận hành (production evidence / 운영 증거)

Sức chứa (capacity / 용량) diagnosis cần kết hợp arrival tỷ lệ (rate / 비율) và completion tỷ lệ (rate / 비율), active tính đồng thời (concurrency / 동시성), hàng đợi (queue / 큐) độ sâu (depth / 깊이) + hàng đợi (queue / 큐) wait, service-time phân phối (distribution / 분포), thử lại (retry / 재시도)/attempt tỷ lệ (rate / 비율), tài nguyên (resource / 자원) saturation tại bottleneck, rejection/load-shed count và remaining deadline/cancellation tỷ lệ (rate / 비율).

Nếu thông lượng (throughput / 처리량) đứng yên nhưng tính đồng thời (concurrency / 동시성)/hàng đợi (queue / 큐) tăng, hệ thống (system / 시스템) đang tích debt. Nếu CPU thấp mà pool wait cao, bottleneck nằm downstream/tài nguyên (resource / 자원) khác.

Kiểm thử tải (load test / 부하 테스트) cần tải công việc (workload / 워크로드) mix và dạng thất bại (failure mode / 실패 모드) gần môi trường vận hành (production / 운영 환경); benchmark single endpoint happy đường dẫn (path / 경로) không đủ để tìm safe envelope.

> **Nối mạch:** **15. bằng chứng vận hành (production evidence / 운영 증거)** đặt vấn đề; **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** kiểm tra bằng chứng, rồi **17. Whole-system profiling bắt đầu từ thời gian (time / 시간) decomposition** mở rộng hệ quả.

## 16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?

Nếu ứng dụng (application / 애플리케이션) hàng đợi (queue / 큐) tăng vì CPU run hàng đợi (queue / 큐) dài, scheduler là lower tầng (layer / 계층). Nếu DB pool full vì khóa (lock / 잠금) waits, cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) quyết định sức chứa (capacity / 용량). Nếu ghi (write / 쓰기) độ trễ (latency / 지연 시간) tăng vì lưu trữ (storage / 저장소) flush, durability đường dẫn (path / 경로) quyết định dịch vụ (service / 서비스) thời gian (time / 시간). Nếu TLS/KMS phụ thuộc (dependency / 의존성) chậm, bảo mật (security / 보안) điều khiển (control / 제어) plane cũng có thể trở thành sức chứa (capacity / 용량) bottleneck.

Sức chứa (capacity / 용량) mô hình (model / 모델) chỉ đúng khi biết tài nguyên (resource / 자원) thật sự đang giới hạn progress.

> **Nối mạch:** **17. Whole-system profiling bắt đầu từ thời gian (time / 시간) decomposition** nối từ **16. Lower lớp trừu tượng (abstraction / 추상화) nào quyết định hành vi (behavior / 동작)?** sang **18. On-CPU và off-CPU trả lời hai câu hỏi khác nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Whole-system profiling bắt đầu từ thời gian (time / 시간) decomposition

Một yêu cầu (request / 요청) mất 500 ms không đồng nghĩa CPU đã dùng 500 ms. Wall-clock thời gian (time / 시간) có thể gồm hàng đợi (queue / 큐) wait, scheduler delay, khóa (lock / 잠금) wait, page fault, mạng (network / 네트워크) wait, DB pool wait, lưu trữ (storage / 저장소) flush và chỉ một phần nhỏ on-CPU thực thi (execution / 실행).

**Lập hồ sơ toàn hệ thống (whole-system profiling / 전체 시스템 프로파일링)** cần tách ít nhất:

```text
queueing time
on-CPU time
off-CPU blocked/waiting time
runtime pause/GC
network/downstream wait
storage I/O wait
```

CPU flame đồ thị (graph / 그래프) rất hữu ích khi công việc (work / 작업) thật sự on-CPU. Nhưng nếu luồng thực thi (thread / 스레드) ngủ chờ mutex hoặc socket, flame đồ thị (graph / 그래프) on-CPU có thể nhìn “khỏe” trong khi người dùng (user / 사용자) độ trễ (latency / 지연 시간) rất xấu.

> **Nối mạch:** **18. On-CPU và off-CPU trả lời hai câu hỏi khác nhau** nối từ **17. Whole-system profiling bắt đầu từ thời gian (time / 시간) decomposition** sang **19. Scheduler bằng chứng (evidence / 증거) nối ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) với CPU reality**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. On-CPU và off-CPU trả lời hai câu hỏi khác nhau

**On-CPU profiling** hỏi CPU cycles đang được tiêu ở đường đi mã (code path / 코드 경로) nào. Nó giúp tìm serialization, hashing, regex, GC công việc (work / 작업), khóa (lock / 잠금) spinning, compression hoặc thuật toán (algorithm / 알고리즘) đường xử lý nóng (hot path / 핫 패스).

**Off-CPU profiling** hỏi thực thi (execution / 실행) ngữ cảnh (context / 맥락) đang bị khối (block / 블록) ở đâu: futex/mutex, điều kiện (condition / 조건) variable, socket, disk I/O, page fault hoặc scheduler wait.

Một tranh chấp khóa (lock contention / 잠금 경합) sự cố (incident / 인시던트) có thể có CPU tổng thể thấp vì đa số threads ngủ; tăng CPU cores không giải quyết. Ngược lại spin khóa (lock / 잠금) có thể làm CPU 100% nhưng useful thông lượng (throughput / 처리량) không tăng.

Bằng chứng (evidence / 증거) phải khớp thất bại (failure / 실패) cơ chế (mechanism / 메커니즘), không phải công cụ (tool / 도구) quen tay nhất.

> **Nối mạch:** **18. On-CPU và off-CPU trả lời hai câu hỏi khác nhau** đặt vấn đề; **19. Scheduler bằng chứng (evidence / 증거) nối ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) với CPU reality** kiểm tra bằng chứng, rồi **20. PMU counters cho biết CPU chờ cái gì, nhưng cần hypothesis trước** mở rộng hệ quả.

## 19. Scheduler bằng chứng (evidence / 증거) nối ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) với CPU reality

Ứng dụng (application / 애플리케이션) có thể báo 200 runnable workers, nhưng máy chỉ có 8 cores. Khi runnable set lớn hơn thực thi (execution / 실행) sức chứa (capacity / 용량), run hàng đợi (queue / 큐) và ngữ cảnh (context / 맥락) switching tăng. luồng thực thi (thread / 스레드) di chuyển (migration / 마이그레이션) còn làm bộ nhớ đệm (cache / 캐시) locality xấu hơn.

Useful bằng chứng (evidence / 증거) gồm run-queue length, runnable-vs-blocked threads, scheduler delay, ngữ cảnh (context / 맥락) switches và CPU migrations. Nếu p99 yêu cầu (request / 요청) tăng đúng lúc run hàng đợi (queue / 큐) tăng dù handler compute không đổi, sức chứa (capacity / 용량) ranh giới (boundary / 경계) nằm ở scheduling contention chứ không phải mạng (network / 네트워크).

Logical tính đồng thời (concurrency / 동시성), OS runnable tính đồng thời (concurrency / 동시성) và vật lý (physical / 물리적) cores là ba tầng khác nhau.

> **Nối mạch:** **19. Scheduler bằng chứng (evidence / 증거) nối ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성) với CPU reality** đặt vấn đề; **20. PMU counters cho biết CPU chờ cái gì, nhưng cần hypothesis trước** kiểm tra bằng chứng, rồi **21. Roofline lập luận (reasoning / 추론) phân biệt compute-bound và bandwidth-bound** mở rộng hệ quả.

## 20. PMU counters cho biết CPU chờ cái gì, nhưng cần hypothesis trước

**Bộ đếm hiệu năng phần cứng (Performance Monitoring Unit counters, PMU / 성능 모니터링 카운터)** có thể cung cấp bằng chứng (evidence / 증거) về cycles, instructions, bộ nhớ đệm (cache / 캐시) misses, branch misses, stalled cycles, bộ nhớ (memory / 메모리) bandwidth hoặc cache-to-cache traffic tùy CPU/mô hình (model / 모델)/công cụ (tool / 도구).

Counter không tự giải thích nguyên nhân gốc (root cause / 근본 원인). LLC miss cao có thể hợp lý với streaming tải công việc (workload / 워크로드); branch miss thấp không chứng minh mã (code / 코드) tối ưu; sự kiện (event / 이벤트) names khác giữa architectures.

Cách dùng đúng là bắt đầu bằng hypothesis, ví dụ “thông lượng (throughput / 처리량) dừng tăng vì bộ nhớ (memory / 메모리) bandwidth”, rồi tìm bằng chứng (evidence / 증거) tương ứng.

> **Nối mạch:** **21. Roofline lập luận (reasoning / 추론) phân biệt compute-bound và bandwidth-bound** nối từ **20. PMU counters cho biết CPU chờ cái gì, nhưng cần hypothesis trước** sang **22. I/O hàng đợi (queue / 큐) độ sâu (depth / 깊이) cũng có utilization knee**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Roofline lập luận (reasoning / 추론) phân biệt compute-bound và bandwidth-bound

Một tải công việc (workload / 워크로드) thực hiện nhiều phép tính trên mỗi byte dữ liệu có **cường độ tính toán (operational intensity / 연산 집약도)** cao và có thể tiến gần compute limit. tải công việc (workload / 워크로드) đọc lượng lớn bộ nhớ (memory / 메모리) để làm ít arithmetic thường bị memory-bandwidth limit trước.

Mô hình tư duy (mental model / 사고 모델) roofline đơn giản:

```text
performance thực tế
≤ min(compute ceiling,
      memory bandwidth × operational intensity)
```

Nếu tải công việc (workload / 워크로드) bandwidth-bound, tăng cốt lõi (core / 핵심) count có thể làm các cores tranh cùng bộ nhớ (memory / 메모리) channels và không tăng thông lượng (throughput / 처리량). Tối ưu dữ liệu (data / 데이터) bố cục (layout / 레이아웃)/bộ nhớ đệm (cache / 캐시) reuse có thể giá trị hơn vectorizing thêm arithmetic.

> **Nối mạch:** **22. I/O hàng đợi (queue / 큐) độ sâu (depth / 깊이) cũng có utilization knee** nối từ **21. Roofline lập luận (reasoning / 추론) phân biệt compute-bound và bandwidth-bound** sang **23. chi phí (cost / 비용)/hiệu năng (performance / 성능) phải tính theo bottleneck đơn vị (unit / 단위)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. I/O hàng đợi (queue / 큐) độ sâu (depth / 깊이) cũng có utilization knee

Lưu trữ (storage / 저장소) thông lượng (throughput / 처리량) có thể tăng khi nhiều operations in-flight vì thiết bị (device / 장치) có parallelism. Nhưng hàng đợi (queue / 큐) độ sâu (depth / 깊이) quá cao làm requests chờ lâu trước thiết bị (device / 장치) và tail độ trễ (latency / 지연 시간) tăng.

Mạng (network / 네트워크) NIC, NVMe, remote lưu trữ (storage / 저장소) và cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool đều có biến thể của cùng mẫu (pattern / 패턴): cần đủ tính đồng thời (concurrency / 동시성) để giữ chuỗi xử lý (pipeline / 파이프라인) bận, nhưng không để hàng đợi (queue / 큐) debt vượt độ trễ (latency / 지연 시간) ngân sách (budget / 예산).

Với latency-sensitive foreground công việc (work / 작업), background compaction/checkpoint có thể cần throttle dù bandwidth chưa đạt peak benchmark đẹp nhất.

> **Nối mạch:** **23. chi phí (cost / 비용)/hiệu năng (performance / 성능) phải tính theo bottleneck đơn vị (unit / 단위)** nối từ **22. I/O hàng đợi (queue / 큐) độ sâu (depth / 깊이) cũng có utilization knee** sang **24. Heterogeneous hardware làm sức chứa (capacity / 용량) thành placement bài toán (problem / 문제)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. chi phí (cost / 비용)/hiệu năng (performance / 성능) phải tính theo bottleneck đơn vị (unit / 단위)

Hai instance cùng giá không có nghĩa cùng economics. tải công việc (workload / 워크로드) có thể bị giới hạn bởi CPU, bộ nhớ (memory / 메모리) sức chứa (capacity / 용량), bộ nhớ (memory / 메모리) bandwidth, mạng (network / 네트워크) egress, cục bộ (local / 로컬) NVMe, accelerator bộ nhớ (memory / 메모리) hoặc managed-service quota.

Một useful chi phí (cost / 비용) mô hình (model / 모델) có dạng:

```text
cost per completed useful request
cost per durable transaction
cost per GB processed
cost per model token under SLO
```

thay vì chỉ `$/instance-hour`.

Nếu instance đắt hơn 30% nhưng hoàn thành gấp đôi useful công việc (work / 작업) trước utilization knee, nó có thể rẻ hơn trên một đơn vị kết quả (outcome / 결과). Ngược lại scale-up CPU không giúp nếu bottleneck là dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스).

> **Nối mạch:** **24. Heterogeneous hardware làm sức chứa (capacity / 용량) thành placement bài toán (problem / 문제)** nối từ **23. chi phí (cost / 비용)/hiệu năng (performance / 성능) phải tính theo bottleneck đơn vị (unit / 단위)** sang **25. Worked example: CPU thấp nhưng p99 tăng mạnh**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Heterogeneous hardware làm sức chứa (capacity / 용량) thành placement bài toán (problem / 문제)

Hiện đại (modern / 현대적) fleet có thể có cores khác tốc độ, NUMA topology khác, cục bộ (local / 로컬) vs remote bộ nhớ (memory / 메모리), GPU/accelerator khác generation hoặc lưu trữ (storage / 저장소) lớp (class / 클래스) khác nhau. Một yêu cầu (request / 요청) “giống nhau” có dịch vụ (service / 서비스) thời gian (time / 시간) khác tùy placement.

Scheduler/bộ cân bằng tải (load balancer / 로드 밸런서) cần hiểu tài nguyên (resource / 자원) shape khi tải công việc (workload / 워크로드) nhạy topology. Memory-heavy worker chạy trên NUMA placement xấu có thể tăng độ trễ (latency / 지연 시간); AI mô hình (model / 모델) không fit accelerator bộ nhớ (memory / 메모리) có thể spill/offload và đổi bottleneck từ compute sang PCIe/mạng (network / 네트워크) transfer.

Sức chứa (capacity / 용량) mô hình (model / 모델) vì vậy phải ghi rõ **hardware lớp (class / 클래스)**, không gộp mọi replica thành một số instance count.

> **Nối mạch:** **24. Heterogeneous hardware làm sức chứa (capacity / 용량) thành placement bài toán (problem / 문제)** nêu quy tắc; **25. Worked example: CPU thấp nhưng p99 tăng mạnh** thử quy tắc trong tình huống, rồi **26. Worked example: thêm cores nhưng thông lượng (throughput / 처리량) không tăng** mở rộng hệ quả.

## 25. Worked example: CPU thấp nhưng p99 tăng mạnh

Giả sử dịch vụ (service / 서비스) có 100 yêu cầu (request / 요청)/s, CPU chỉ 35%, truy vấn (query / 쿼리) cơ sở dữ liệu (database / 데이터베이스) mất 20 ms nhưng end-to-end p99 là 900 ms. DB liên kết (connection / 연결) pool có 20 slots và pool-acquire p99 là 700 ms.

```text
request concurrency tăng
→ 20 DB slots giữ lâu
→ queue trước pool tăng
→ handler phần lớn off-CPU chờ connection
→ process CPU vẫn thấp
→ p99 tăng
```

Tăng ứng dụng (application / 애플리케이션) threads từ 100 lên 500 làm hàng đợi (queue / 큐) lớn hơn nhưng không tạo DB sức chứa (capacity / 용량). Tăng pool lên 100 có thể chuyển hàng đợi (queue / 큐) vào DB và làm khóa (lock / 잠금)/I/O contention xấu hơn.

Bằng chứng (evidence / 증거) cần đo giao dịch (transaction / 트랜잭션) thời gian tồn tại (lifetime / 수명), pool hold thời gian (time / 시간), acquire wait, DB active sessions và DB saturation.

> **Nối mạch:** **25. Worked example: CPU thấp nhưng p99 tăng mạnh** nêu quy tắc; **26. Worked example: thêm cores nhưng thông lượng (throughput / 처리량) không tăng** thử quy tắc trong tình huống, rồi **27. Benchmark phải tìm phase chuyển tiếp (transition / 전이), không chỉ một điểm đẹp** mở rộng hệ quả.

## 26. Worked example: thêm cores nhưng thông lượng (throughput / 처리량) không tăng

Một analytics tải công việc (workload / 워크로드) scan vùng bộ nhớ (memory / 메모리) lớn, arithmetic ít và LLC miss cao. Từ 8 lên 16 cores, CPU utilization vẫn cao nhưng thông lượng (throughput / 처리량) gần như đứng yên, bộ nhớ (memory / 메모리) bandwidth đã gần ceiling.

Ở đây cốt lõi (core / 핵심) count không còn là sức chứa (capacity / 용량) dimension hữu ích. Lower lớp trừu tượng (abstraction / 추상화) quyết định hành vi (behavior / 동작) là bộ nhớ (memory / 메모리) subsystem. Tối ưu biểu diễn (representation / 표현), batching/bộ nhớ đệm (cache / 캐시) locality hoặc giảm bytes touched có thể tốt hơn mua thêm CPU.

> **Nối mạch:** **26. Worked example: thêm cores nhưng thông lượng (throughput / 처리량) không tăng** nêu quy tắc; **27. Benchmark phải tìm phase chuyển tiếp (transition / 전이), không chỉ một điểm đẹp** thử quy tắc trong tình huống, rồi **28. bằng chứng (evidence / 증거) chuỗi (chain / 사슬) cho hiệu năng (performance / 성능) sự cố (incident / 인시던트)** mở rộng hệ quả.

## 27. Benchmark phải tìm phase chuyển tiếp (transition / 전이), không chỉ một điểm đẹp

Sức chứa (capacity / 용량) kiểm thử (test / 테스트) tốt tăng tải (load / 로드) theo các bậc và quan sát khi hệ thống (system / 시스템) đổi phase:

```text
service-time dominated
→ queue begins growing
→ tail increases sharply
→ retries/errors appear
→ useful throughput plateaus
→ collapse/recovery behavior
```

Cần giữ tải công việc (workload / 워크로드) mix, payload kích thước (size / 크기), bộ nhớ đệm (cache / 캐시) trạng thái (state / 상태) và phụ thuộc (dependency / 의존성) điều kiện (condition / 조건) đủ gần môi trường vận hành (production / 운영 환경). Nếu benchmark chỉ chạy ngắn, autoscaling/warm-up/GC/compaction/checkpoint có thể chưa lộ.

Sau khi giảm tải (load / 로드), còn phải quan sát **khôi phục (recovery / 복구)**. hệ thống (system / 시스템) có hàng đợi (queue / 큐)/thử lại (retry / 재시도) debt lớn có thể tiếp tục xấu sau khi traffic trở lại bình thường.

> **Nối mạch:** **27. Benchmark phải tìm phase chuyển tiếp (transition / 전이), không chỉ một điểm đẹp** đặt vấn đề; **28. bằng chứng (evidence / 증거) chuỗi (chain / 사슬) cho hiệu năng (performance / 성능) sự cố (incident / 인시던트)** kiểm tra bằng chứng, rồi **29. Mô hình tư duy** mở rộng hệ quả.

## 28. bằng chứng (evidence / 증거) chuỗi (chain / 사슬) cho hiệu năng (performance / 성능) sự cố (incident / 인시던트)

Whole-system diagnosis có thể đi theo thứ tự:

```text
SLO symptom
→ trace critical path
→ queue/service-time split
→ on-CPU vs off-CPU
→ subsystem saturation
→ OS scheduler/I/O evidence
→ PMU/device evidence nếu cần
```

Không phải sự cố (incident / 인시던트) nào cũng cần xuống PMU. Mục tiêu là xuống đủ thấp để cơ chế (mechanism / 메커니즘) rõ rồi sửa ở tầng (layer / 계층) sở hữu bất biến (invariant / 불변식)/sức chứa (capacity / 용량) ranh giới (boundary / 경계).

> **Nối mạch:** **28. bằng chứng (evidence / 증거) chuỗi (chain / 사슬) cho hiệu năng (performance / 성능) sự cố (incident / 인시던트)** cung cấp dấu vết cho **29. Mô hình tư duy**, rồi **Kết nối** mở rộng hệ quả của mô hình.

## 29. Mô hình tư duy

> sức chứa (capacity / 용량) kỹ thuật (engineering / 엔지니어링) là giữ hệ thống (system / 시스템) **bên trái điểm overload** và biết tài nguyên (resource / 자원) nào thật sự giới hạn progress. Utilization cao làm hàng đợi (queue / 큐) nhạy với variance; tính đồng thời (concurrency / 동시성) limit giữ active công việc (work / 작업) hữu hạn; admission điều khiển (control / 제어) giới hạn debt. Whole-system profiling nối yêu cầu (request / 요청) thời gian (time / 시간) với on-CPU, off-CPU, scheduler, bộ nhớ (memory / 메모리) và I/O bằng chứng (evidence / 증거). chi phí (cost / 비용)/hiệu năng (performance / 성능) chỉ có ý nghĩa khi tính trên useful kết quả (outcome / 결과) dưới SLO, không phải peak benchmark hay giá instance riêng lẻ.

> **Nối mạch:** **Kết nối** tổng hợp từ **29. Mô hình tư duy**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc cùng [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md), [Load balancing và connection pools](./03_load_balancing_connection_pools_and_locality.md), [End-to-end request và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md), [Debugging xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md), [OS scheduler internals](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [Memory hierarchy/cache](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md) và [NUMA/interconnect](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
