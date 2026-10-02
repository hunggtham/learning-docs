# Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Latency, throughput, capacity và scalability**. Route đi từ latency/throughput → utilization/saturation/queueing → Little’s Law/bottleneck → vertical-horizontal scaling → cache, batching, pools và load balancing, để capacity được đo theo workload thực.

Kỹ thuật hiệu năng (performance engineering) không đơn giản là “làm mã chạy nhanh”. Một hệ thống là dòng công việc đi qua CPU, bộ nhớ đệm (cache / 캐시), bộ nhớ (memory / 메모리), scheduler, thời gian chạy (runtime / 런타임), mạng (network / 네트워크), cơ sở dữ liệu (database / 데이터베이스) và lưu trữ (storage / 저장소); mỗi tầng có dịch vụ (service / 서비스) thời gian (time / 시간), hàng đợi (queue / 큐) và giới hạn riêng. Tối ưu đúng bắt đầu bằng một câu hỏi có thể kiểm chứng: **công việc (work / 작업) đang chờ ở đâu, tài nguyên (resource / 자원) nào đang giới hạn progress, và bất biến (invariant / 불변식) nào về độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) phải được giữ khi tải (load / 로드) tăng?**

Hiệu năng (performance / 성능) tốt không phải maximum benchmark number. Với môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템), mục tiêu thường là giữ độ trễ (latency / 지연 시간) phân phối (distribution / 분포), thông lượng (throughput / 처리량), chi phí (cost / 비용) và độ tin cậy (reliability / 신뢰성) trong một **safe operating envelope** dưới tải công việc (workload / 워크로드) thực tế.

## 1. độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) là hai trục khác nhau

**độ trễ (latency / 지연 시간)** là thời gian một thao tác (operation / 연산) hoàn thành. **thông lượng (throughput / 처리량)** là số thao tác (operation / 연산) hoàn thành trên một đơn vị thời gian.

Hai chỉ số (metric / 지표) liên quan nhưng không đồng nhất. Batching có thể tăng thông lượng (throughput / 처리량) vì amortize fixed chi phí (cost / 비용) nhưng làm yêu cầu (request / 요청) đầu batch phải chờ. Tăng tính đồng thời (concurrency / 동시성) có thể tăng thông lượng (throughput / 처리량) đến một điểm, rồi contention và queueing làm độ trễ (latency / 지연 시간) tăng mạnh mà thông lượng (throughput / 처리량) hầu như không tăng nữa.

Một thiết kế (design / 설계) cần nói rõ mục tiêu (objective / 목표) nào quan trọng hơn theo tải công việc (workload / 워크로드): interactive API ưu tiên tail độ trễ (latency / 지연 시간); offline batch có thể chấp nhận độ trễ (latency / 지연 시간) lớn để đổi lấy thông lượng (throughput / 처리량)/chi phí (cost / 비용) tốt hơn.

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **2. dịch vụ (service / 서비스) thời gian (time / 시간) và waiting thời gian (time / 시간) phải được tách ra** tiếp nhận điểm tựa từ **1. độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량) là hai trục khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Utilization gần sức chứa (capacity / 용량) làm hàng đợi (queue / 큐) nhạy với variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. dịch vụ (service / 서비스) thời gian (time / 시간) và waiting thời gian (time / 시간) phải được tách ra

End-to-end độ trễ (latency / 지연 시간) có thể được xem gần đúng như:

```text
latency = useful/service time + waiting/queueing time + coordination overhead
```

Nếu truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) execute 20 ms nhưng yêu cầu (request / 요청) chờ liên kết (connection / 연결) pool 300 ms, tối ưu truy vấn (query / 쿼리) chỉ chạm một phần nhỏ độ trễ (latency / 지연 시간). Nếu CPU handler chỉ dùng 5 ms nhưng luồng thực thi (thread / 스레드) chờ run hàng đợi (queue / 큐) 100 ms, ứng dụng (application / 애플리케이션) profiler chỉ đo on-CPU mã (code / 코드) sẽ bỏ mất bottleneck.

Advanced diagnosis luôn hỏi: **thời gian được dùng để làm việc hay để chờ quyền dùng tài nguyên (resource / 자원)?**

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **3. Utilization gần sức chứa (capacity / 용량) làm hàng đợi (queue / 큐) nhạy với variance** tiếp nhận điểm tựa từ **2. dịch vụ (service / 서비스) thời gian (time / 시간) và waiting thời gian (time / 시간) phải được tách ra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Little's Law nối tính đồng thời (concurrency / 동시성), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Utilization gần sức chứa (capacity / 용량) làm hàng đợi (queue / 큐) nhạy với variance

Khi arrival tỷ lệ (rate / 비율) `λ` tiến gần dịch vụ (service / 서비스) tỷ lệ (rate / 비율) `μ`, một burst nhỏ hoặc vài yêu cầu (request / 요청) chậm có thể tạo hàng đợi (queue / 큐). Mô hình M/M/1 đơn giản với `ρ = λ/μ` chỉ là approximation, nhưng intuition quan trọng vẫn đúng: khi `ρ` tiến gần 1, waiting thời gian (time / 시간) tăng rất nhanh.

Môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드) thường tệ hơn mô hình (model / 모델) lý tưởng vì dịch vụ (service / 서비스) thời gian (time / 시간) không exponential đẹp, arrivals bursty, dependencies correlated và tài nguyên (resource / 자원) có nhiều classes. Vì vậy mục tiêu (target / 대상) 100% utilization cho user-facing tải công việc (workload / 워크로드) thường đồng nghĩa không còn headroom hấp thụ variance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **4. Little's Law nối tính đồng thời (concurrency / 동시성), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)** tiếp nhận điểm tựa từ **3. Utilization gần sức chứa (capacity / 용량) làm hàng đợi (queue / 큐) nhạy với variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Bottleneck là tài nguyên (resource / 자원) làm giới hạn thông lượng (throughput / 처리량) hoặc độ trễ (latency / 지연 시간) hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Little's Law nối tính đồng thời (concurrency / 동시성), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)

Trong stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

`L` là average công việc (work / 작업) in-flight, `λ` là thông lượng (throughput / 처리량)/arrival tỷ lệ (rate / 비율) ổn định, `W` là average thời gian (time / 시간) trong hệ thống (system / 시스템).

Nếu dịch vụ (service / 서비스) hoàn thành 1.000 req/s và average độ trễ (latency / 지연 시간) 0,2 s, khoảng 200 requests tồn tại trong hệ thống (system / 시스템) trung bình.

Little's Law không dự đoán p99, nhưng rất mạnh để sanity-check. Nếu nhóm (team / 팀) nói dịch vụ (service / 서비스) cần 10.000 req/s, mỗi yêu cầu (request / 요청) giữ DB liên kết (connection / 연결) trung bình 100 ms, thì tải công việc (workload / 워크로드) đó đã hàm ý khoảng 1.000 concurrent connection-hold thời gian (time / 시간) nếu không thay kiến trúc (architecture / 아키텍처)/parallelism. Một pool 50 connections không thể giữ cùng đặc tả hợp đồng (contract / 계약) chỉ bằng “tuning”.

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **4. Little's Law nối tính đồng thời (concurrency / 동시성), độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)** đã nêu tiêu chí phân biệt, còn **5. Bottleneck là tài nguyên (resource / 자원) làm giới hạn thông lượng (throughput / 처리량) hoặc độ trễ (latency / 지연 시간) hiện tại** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. CPU utilization không nói CPU đang làm gì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Bottleneck là tài nguyên (resource / 자원) làm giới hạn thông lượng (throughput / 처리량) hoặc độ trễ (latency / 지연 시간) hiện tại

Một hệ thống (system / 시스템) có nhiều resources, nhưng tại một operating điểm (point / 지점) thường có một hoặc vài resources đang giới hạn progress: CPU thực thi (execution / 실행), bộ nhớ (memory / 메모리) bandwidth, run hàng đợi (queue / 큐), GC, khóa (lock / 잠금), liên kết (connection / 연결) pool, DB I/O, WAL flush, mạng (network / 네트워크) bandwidth hoặc downstream quota.

Tăng tốc phần không phải bottleneck chỉ cải thiện tổng thể rất ít. Đây là intuition của Amdahl: speedup toàn hệ thống bị giới hạn bởi phần thời gian không được cải thiện.

Quan trọng hơn, bottleneck **di chuyển**. Sau khi giảm CPU chi phí (cost / 비용), cơ sở dữ liệu (database / 데이터베이스) có thể trở thành giới hạn mới; sau khi thêm replica, mạng (network / 네트워크) hoặc lưu trữ (storage / 저장소) trở thành giới hạn tiếp theo. hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링) là vòng lặp đo → giả thuyết → thay đổi → đo lại, không phải một lần tối ưu.

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **5. Bottleneck là tài nguyên (resource / 자원) làm giới hạn thông lượng (throughput / 처리량) hoặc độ trễ (latency / 지연 시간) hiện tại** đã nêu tiêu chí phân biệt, còn **6. CPU utilization không nói CPU đang làm gì** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. bộ nhớ (memory / 메모리) hierarchy làm Big-O chưa đủ để dự đoán hiệu năng (performance / 성능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. CPU utilization không nói CPU đang làm gì

CPU 100% có thể là useful compute, spin khóa (lock / 잠금), GC, scheduler overhead hoặc thử lại (retry / 재시도) vòng lặp (loop / 루프). CPU 40% cũng không chứng minh dịch vụ (service / 서비스) có headroom nếu bottleneck là single-thread vòng lặp sự kiện (event loop / 이벤트 루프), DB pool, khóa (lock / 잠금) hay lưu trữ (storage / 저장소).

Ở tầng CPU, IPC, bộ nhớ đệm (cache / 캐시)/TLB miss, branch miss, stalled cycles và bộ nhớ (memory / 메모리) bandwidth có thể giải thích vì sao cùng 100% CPU nhưng thông lượng (throughput / 처리량) khác nhau. Ở tầng OS, run hàng đợi (queue / 큐)/ngữ cảnh (context / 맥락) switch/throttling cho biết runnable công việc (work / 작업) có đang phải chờ hay không.

Do đó utilization chỉ là symptom-level tín hiệu (signal / 신호). Cần attribution xuống cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **7. bộ nhớ (memory / 메모리) hierarchy làm Big-O chưa đủ để dự đoán hiệu năng (performance / 성능)** tiếp nhận điểm tựa từ **6. CPU utilization không nói CPU đang làm gì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. tính đồng thời (concurrency / 동시성) tạo parallelism nhưng cũng tạo contention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. bộ nhớ (memory / 메모리) hierarchy làm Big-O chưa đủ để dự đoán hiệu năng (performance / 성능)

Hai thuật toán cùng `O(n)` có thể khác rất xa nếu một bên sequentially scan contiguous array còn bên kia pointer-chase qua random vùng nhớ động (heap / 힙) nodes.

Bộ nhớ đệm (cache / 캐시) line, TLB, prefetcher, NUMA và bộ nhớ (memory / 메모리) bandwidth quyết định chi phí (cost / 비용) của dữ liệu (data / 데이터) movement. Khi working set không fit bộ nhớ đệm (cache / 캐시), arithmetic có thể rẻ hơn rất nhiều so với chờ bộ nhớ (memory / 메모리).

Đây là lý do dữ liệu (data / 데이터) bố cục (layout / 레이아웃), locality và allocation chiến lược (strategy / 전략) là hiệu năng (performance / 성능) concepts ngang hàng với algorithmic độ phức tạp (complexity / 복잡도) trong các hệ thống (systems / 시스템들) mã (code / 코드).

Đọc [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) và advanced kiến trúc (architecture / 아키텍처) để nối tới hardware bằng chứng (evidence / 증거).

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **8. tính đồng thời (concurrency / 동시성) tạo parallelism nhưng cũng tạo contention** tiếp nhận điểm tựa từ **7. bộ nhớ (memory / 메모리) hierarchy làm Big-O chưa đủ để dự đoán hiệu năng (performance / 성능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Tail độ trễ (latency / 지연 시간) quan trọng vì fan-out khuếch đại phần đuôi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. tính đồng thời (concurrency / 동시성) tạo parallelism nhưng cũng tạo contention

Tăng workers/threads chỉ giúp khi tải công việc (workload / 워크로드) có independent công việc (work / 작업) và tài nguyên (resource / 자원) phía dưới còn sức chứa (capacity / 용량). Khi nhiều workers cùng tranh khóa (lock / 잠금), bộ nhớ đệm (cache / 캐시) line, DB row, liên kết (connection / 연결) pool hoặc bộ nhớ (memory / 메모리) bandwidth, tính đồng thời (concurrency / 동시성) tăng có thể làm **dịch vụ (service / 서비스) thời gian (time / 시간) tự xấu đi**.

Một đường cong phổ biến:

```text
concurrency thấp  → resource chưa dùng hết → throughput tăng
concurrency vừa   → gần điểm hiệu quả nhất
concurrency cao   → queue + contention + cache/scheduler overhead tăng
                   → latency tăng mạnh, throughput phẳng hoặc giảm
```

Vì vậy tính đồng thời (concurrency / 동시성) limit là một hiệu năng (performance / 성능) điều khiển (control / 제어), không chỉ độ tin cậy (reliability / 신뢰성) điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **9. Tail độ trễ (latency / 지연 시간) quan trọng vì fan-out khuếch đại phần đuôi** tiếp nhận điểm tựa từ **8. tính đồng thời (concurrency / 동시성) tạo parallelism nhưng cũng tạo contention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Batching amortize fixed chi phí (cost / 비용) nhưng đổi queueing hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Tail độ trễ (latency / 지연 시간) quan trọng vì fan-out khuếch đại phần đuôi

Average che slow outliers. Nếu một yêu cầu (request / 요청) cần kết quả từ nhiều dependencies/shards, end-to-end độ trễ (latency / 지연 시간) bị chi phối bởi slow branch cần thiết nhất.

Fan-out càng lớn, xác suất gặp ít nhất một tail sự kiện (event / 이벤트) càng cao. Vì vậy p95/p99 của downstream không thể cộng/trừ đơn giản để suy ra p99 của hệ thống (system / 시스템).

Hiệu năng (performance / 성능) kiểm thử (test / 테스트) cần đo phân phối (distribution / 분포), không chỉ mean. Với SLO, cần biết p50 cho normal đường dẫn (path / 경로) nhưng cũng phải quan sát p95/p99 và hết thời gian chờ (timeout / 타임아웃) tỷ lệ (rate / 비율) dưới tải (load / 로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **10. Batching amortize fixed chi phí (cost / 비용) nhưng đổi queueing hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **9. Tail độ trễ (latency / 지연 시간) quan trọng vì fan-out khuếch đại phần đuôi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. bộ nhớ đệm (cache / 캐시) là sự đánh đổi (trade-off / 트레이드오프) giữa reuse và consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Batching amortize fixed chi phí (cost / 비용) nhưng đổi queueing hành vi (behavior / 동작)

Batching chia sẻ chi phí (cost / 비용) như syscall, mạng (network / 네트워크) round-trip, disk flush, giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋) hoặc GPU kernel launch.

Nhưng batch phải chờ hình thành; batch lớn giữ bộ nhớ (memory / 메모리) nhiều hơn, tăng head-of-line delay và tăng blast radius nếu thất bại (failure / 실패) xảy ra.

Group lần ghi nhận (commit / 커밋) trong cơ sở dữ liệu (database / 데이터베이스) là ví dụ rõ: nhiều giao dịch (transaction / 트랜잭션) dùng chung một WAL flush để tăng thông lượng (throughput / 처리량), nhưng batching chính sách (policy / 정책) vẫn phải giữ durability bất biến (invariant / 불변식) trước khi acknowledgement.

Tối ưu hóa (optimization / 최적화) tốt đổi timing/chi phí (cost / 비용), không âm thầm đổi tính đúng đắn (correctness / 정확성) đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **11. bộ nhớ đệm (cache / 캐시) là sự đánh đổi (trade-off / 트레이드오프) giữa reuse và consistency** tiếp nhận điểm tựa từ **10. Batching amortize fixed chi phí (cost / 비용) nhưng đổi queueing hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + admission-control ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. bộ nhớ đệm (cache / 캐시) là sự đánh đổi (trade-off / 트레이드오프) giữa reuse và consistency

Bộ nhớ đệm (cache / 캐시) có lợi khi reuse xác suất (probability / 확률) cao và bộ nhớ đệm (cache / 캐시) hit rẻ hơn nguồn (source / 소스) lookup đủ nhiều. Nhưng bộ nhớ đệm (cache / 캐시) tạo thêm trạng thái (state / 상태) cần eviction, vô hiệu hóa (invalidation / 무효화) và sức chứa (capacity / 용량) management.

Metrics cần tách hit ratio với **miss chi phí (cost / 비용)**. Hit ratio 99% vẫn có thể tệ nếu 1% miss cực đắt và nằm trong tail-critical đường dẫn (path / 경로).

Bộ nhớ đệm (cache / 캐시) stampede, hot key và stale dữ liệu (data / 데이터) là thất bại (failure / 실패) modes xuất hiện khi tải (load / 로드) tăng. Advanced bộ nhớ đệm (cache / 캐시) lập luận (reasoning / 추론) nằm ở [caching consistency, invalidation, stampede và hot keys](../../08_software_systems/advanced/02_caching_consistency_invalidation_stampede_and_hot_keys.md).

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **11. bộ nhớ đệm (cache / 캐시) là sự đánh đổi (trade-off / 트레이드오프) giữa reuse và consistency** đã nêu tiêu chí phân biệt, còn **12. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + admission-control ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Vertical scaling và horizontal scaling giải các ràng buộc (constraint / 제약조건) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + admission-control ranh giới (boundary / 경계)

Liên kết (connection / 연결) pool tái sử dụng setup chi phí (cost / 비용) và giới hạn tính đồng thời (concurrency / 동시성) xuống downstream.

Pool quá nhỏ làm yêu cầu (request / 요청) chờ; pool quá lớn có thể làm cơ sở dữ liệu (database / 데이터베이스) nhận quá nhiều simultaneous công việc (work / 작업), tăng khóa (lock / 잠금)/I/O/bộ nhớ đệm (cache / 캐시) pressure. Tăng pool kích thước (size / 크기) thường chỉ **di chuyển hàng đợi (queue / 큐)** từ ứng dụng (application / 애플리케이션) sang cơ sở dữ liệu (database / 데이터베이스) chứ không xóa hàng đợi (queue / 큐).

Khi gỡ lỗi (debug / 디버그), đo riêng:

```text
acquire wait
active connections
query service time
transaction lifetime
DB saturation/wait class
```

Đừng chỉ nhìn truy vấn (query / 쿼리) thực thi (execution / 실행) duration.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **12. liên kết (connection / 연결) pool là hàng đợi (queue / 큐) + admission-control ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **13. Vertical scaling và horizontal scaling giải các ràng buộc (constraint / 제약조건) khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Backpressure và admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trước utilization knee** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Vertical scaling và horizontal scaling giải các ràng buộc (constraint / 제약조건) khác nhau

Vertical scaling tăng tài nguyên (resource / 자원) của một nút (node / 노드) và thường giữ kiến trúc (architecture / 아키텍처) đơn giản hơn. Horizontal scaling thêm nodes nhưng chỉ giúp nếu công việc (work / 작업) có thể partition và dùng chung (shared / 공유) bottleneck không trở thành giới hạn.

Thêm ứng dụng (application / 애플리케이션) replicas không tăng DB ghi (write / 쓰기) sức chứa (capacity / 용량) nếu mọi replicas cùng tranh một cơ sở dữ liệu (database / 데이터베이스). Sharding có thể tăng sức chứa (capacity / 용량) nhưng thêm routing, rebalancing, cross-shard giao dịch (transaction / 트랜잭션) và hotspot rủi ro (risk / 위험).

“quy mô (scale / 규모) out” là thay kiến trúc (architecture / 아키텍처) của tài nguyên (resource / 자원) đồ thị (graph / 그래프), không phải phép nhân sức chứa (capacity / 용량) tự động.

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **14. Backpressure và admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trước utilization knee** tiếp nhận điểm tựa từ **13. Vertical scaling và horizontal scaling giải các ràng buộc (constraint / 제약조건) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. thử lại (retry / 재시도) có thể biến hiệu năng (performance / 성능) regression thành outage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Backpressure và admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trước utilization knee

Khi demand vượt sức chứa (capacity / 용량), hệ thống (system / 시스템) cần một nơi nói “đủ rồi”. Bounded queues, tính đồng thời (concurrency / 동시성) semaphore, đơn vị từ (token / 토큰)/tỷ lệ (rate / 비율) limits và tải (load / 로드) shedding tạo tường minh (explicit / 명시적) điều khiển (control / 제어).

Unbounded hàng đợi (queue / 큐) biến overload thành độ trễ (latency / 지연 시간) debt. yêu cầu (request / 요청) đã quá deadline nhưng vẫn chờ/được xử lý là wasted công việc (work / 작업).

Hiệu năng (performance / 성능) và độ tin cậy (reliability / 신뢰성) gặp nhau ở đây: bảo vệ độ trễ (latency / 지연 시간) của accepted công việc (work / 작업) đôi khi cần reject một phần arrivals sớm.

Đọc [capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **15. thử lại (retry / 재시도) có thể biến hiệu năng (performance / 성능) regression thành outage** tiếp nhận điểm tựa từ **14. Backpressure và admission điều khiển (control / 제어) giữ hệ thống (system / 시스템) trước utilization knee** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Warm trạng thái (state / 상태) và transient trạng thái (state / 상태) phải được tách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. thử lại (retry / 재시도) có thể biến hiệu năng (performance / 성능) regression thành outage

Một phụ thuộc (dependency / 의존성) chậm làm hết thời gian chờ (timeout / 타임아웃); caller thử lại (retry / 재시도); attempts tăng arrival tỷ lệ (rate / 비율); hàng đợi (queue / 큐) dài hơn; dịch vụ (service / 서비스) thời gian (time / 시간) xấu đi; hết thời gian chờ (timeout / 타임아웃) tiếp tục tăng.

```text
slowdown → timeout → retry → overload → longer queue → more timeout
```

Vì vậy thử lại (retry / 재시도) tỷ lệ (rate / 비율) là hiệu năng (performance / 성능) chỉ số (metric / 지표), không chỉ error-handling chỉ số (metric / 지표). Deadline propagation, cancellation, backoff+jitter và thử lại (retry / 재시도) ngân sách (budget / 예산) giúp giới hạn amplification nhưng không tạo sức chứa (capacity / 용량) nếu bottleneck vẫn saturated.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **16. Warm trạng thái (state / 상태) và transient trạng thái (state / 상태) phải được tách** tiếp nhận điểm tựa từ **15. thử lại (retry / 재시도) có thể biến hiệu năng (performance / 성능) regression thành outage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Coordinated omission và benchmark methodology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Warm trạng thái (state / 상태) và transient trạng thái (state / 상태) phải được tách

JIT compilation, bộ nhớ đệm (cache / 캐시) warming, liên kết (connection / 연결) establishment, DNS/TLS setup, page faults và mô hình (model / 모델)/dữ liệu (data / 데이터) loading làm cold hành vi (behavior / 동작) khác steady trạng thái (state / 상태).

Benchmark chỉ đo warm steady-state có thể bỏ startup/cold failover; benchmark chỉ đo cold có thể đánh giá thấp steady-state thông lượng (throughput / 처리량).

Triển khai (deployment / 배포), autoscaling và failover đều tạo transient trạng thái (state / 상태), nên sức chứa (capacity / 용량) plan phải giữ headroom cho warm-up phase.

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **17. Coordinated omission và benchmark methodology** tiếp nhận điểm tựa từ **16. Warm trạng thái (state / 상태) và transient trạng thái (state / 상태) phải được tách** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. bằng chứng vận hành (production evidence / 운영 증거) cần đi từ SLO xuống tài nguyên (resource / 자원)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Coordinated omission và benchmark methodology

Tải (load / 로드) generator cũng có thể nói dối. Nếu generator gửi yêu cầu (request / 요청) tiếp theo chỉ sau yêu cầu (request / 요청) trước hoàn thành, khi máy chủ (server / 서버) chậm nó vô tình giảm arrival tỷ lệ (rate / 비율) và bỏ sót queueing mà real clients vẫn tạo. Đây là một dạng **coordinated omission**.

Kiểm thử tải (load test / 부하 테스트) cần mô hình arrivals gần tải công việc (workload / 워크로드) thật, giữ yêu cầu (request / 요청) timestamps/deadlines, report độ trễ (latency / 지연 시간) phân phối (distribution / 분포) và không âm thầm hạ pressure khi máy chủ (server / 서버) chậm nếu môi trường vận hành (production / 운영 환경) hành vi (behavior / 동작) không như vậy.

Sai số đo lường (measurement error / 측정 오차) là một dạng thất bại (failure mode / 실패 모드) của hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **17. Coordinated omission và benchmark methodology** nêu điều cần giải thích; **18. bằng chứng vận hành (production evidence / 운영 증거) cần đi từ SLO xuống tài nguyên (resource / 자원)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) phải giữ bất biến (invariant / 불변식) tính đúng đắn (correctness / 정확성)/độ tin cậy (reliability / 신뢰성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. bằng chứng vận hành (production evidence / 운영 증거) cần đi từ SLO xuống tài nguyên (resource / 자원)

Một workflow thực tế:

```text
1. xác định user-visible SLI/SLO hoặc performance invariant
2. chọn slow percentile/failed window
3. lấy trace đại diện critical path
4. tách service time và queue wait ở từng boundary
5. correlate resource saturation đúng layer
6. profile on-CPU/off-CPU hoặc hardware/runtime mechanism khi cần
7. thay đổi một hypothesis rồi đo lại
```

Bằng chứng (evidence / 증거) có thể gồm dấu vết (trace / 추적), hàng đợi (queue / 큐) wait, CPU profile, run hàng đợi (queue / 큐), GC pause/allocation, bộ nhớ đệm (cache / 캐시)/TLB/PMU counters, DB waits, I/O độ trễ (latency / 지연 시간), retransmission và replica lag. Không cần luôn thu mọi chỉ số (metric / 지표); chọn chỉ số (metric / 지표) theo hypothesis.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **18. bằng chứng vận hành (production evidence / 운영 증거) cần đi từ SLO xuống tài nguyên (resource / 자원)** nêu điều cần giải thích; **19. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) phải giữ bất biến (invariant / 불변식) tính đúng đắn (correctness / 정확성)/độ tin cậy (reliability / 신뢰성)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) phải giữ bất biến (invariant / 불변식) tính đúng đắn (correctness / 정확성)/độ tin cậy (reliability / 신뢰성)

Một tối ưu hóa (optimization / 최적화) không hợp lệ nếu đạt benchmark bằng cách làm yếu đặc tả hợp đồng (contract / 계약) không được công bố: bỏ fsync, giảm isolation không được phép, bỏ auth, drop kiểm tra hợp lệ (validation / 검증), dùng stale bộ nhớ đệm (cache / 캐시) vượt yêu cầu (requirement / 요구사항) hoặc tăng thử lại (retry / 재시도) vô hạn để che lỗi (error / 오류).

Khi đánh đổi có chủ đích, API/SLO phải nói rõ ngữ nghĩa (semantics / 의미론) mới. hiệu năng (performance / 성능) là chất lượng (quality / 품질) attribute nằm dưới tính đúng đắn (correctness / 정확성) các ràng buộc (constraints / 제약조건들), không phải lý do để phá chúng.

> **Chuyển mạch:** Trong **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **20. Mô hình tư duy** gom các mảnh từ **19. hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) phải giữ bất biến (invariant / 불변식) tính đúng đắn (correctness / 정확성)/độ tin cậy (reliability / 신뢰성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu nhầm thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Mô hình tư duy

> Hiệu năng là **dòng công việc qua các dịch vụ (service / 서비스) centers hữu hạn**. dữ liệu (data / 데이터) locality quyết định chi phí (cost / 비용) bên trong CPU/bộ nhớ (memory / 메모리); scheduler/thời gian chạy (runtime / 런타임) quyết định khi công việc (work / 작업) được chạy; pools/queues quyết định khi công việc (work / 작업) được vào tài nguyên (resource / 자원); mạng (network / 네트워크)/cơ sở dữ liệu (database / 데이터베이스)/lưu trữ (storage / 저장소) quyết định downstream dịch vụ (service / 서비스) thời gian (time / 시간). Khi tải (load / 로드) tăng, waiting thời gian (time / 시간) và contention thường thay đổi hành vi (behavior / 동작) trước khi thông lượng (throughput / 처리량) đạt cực đại. Tối ưu đúng là tìm bottleneck bằng bằng chứng (evidence / 증거) và giữ hệ thống (system / 시스템) trong safe operating envelope.

> **Chuyển mạch:** Ở chặng này của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **20. Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những hiểu nhầm thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu nhầm thường gặp

**“CPU 100% nghĩa là tối ưu.”** Có thể CPU đang spin, GC hoặc scheduler overhead trong khi useful thông lượng (throughput / 처리량) kém.

**“Thêm threads luôn tăng thông lượng (throughput / 처리량).”** Chỉ tới khi independent công việc (work / 작업) và downstream sức chứa (capacity / 용량) còn đủ; sau đó contention/queueing có thể làm tệ hơn.

**“Average độ trễ (latency / 지연 시간) đủ để benchmark.”** Tail và tải công việc (workload / 워크로드) mix mới quyết định nhiều môi trường vận hành (production / 운영 환경) SLO.

**“quy mô (scale / 규모) horizontal giải mọi bottleneck.”** trạng thái dùng chung (shared state / 공유 상태), cơ sở dữ liệu (database / 데이터베이스), mạng (network / 네트워크) hoặc coordination có thể trở thành bottleneck mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng**, **Những hiểu nhầm thường gặp** đã nêu tiêu chí phân biệt, còn **Kết nối** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [Architecture memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS scheduler advanced](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [Runtime GC](../../04_programming_languages/advanced/06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [End-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
