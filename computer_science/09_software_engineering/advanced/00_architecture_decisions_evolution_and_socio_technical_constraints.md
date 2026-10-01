# Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. kiến trúc (architecture / 아키텍처) là tập các ràng buộc (constraints / 제약조건들) trên thay đổi và thất bại (failure / 실패)** xác định điều kiện hoặc ranh giới mà các cơ chế sau phải tôn trọng; sau đó sang **2. Bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ thành phần (component / 컴포넌트)** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Advanced software kiến trúc (architecture / 아키텍처) không phải thuộc nhiều mẫu (pattern / 패턴) hơn. Nó là khả năng chọn ranh giới (boundary / 경계) và sự đánh đổi (trade-off / 트레이드오프) phù hợp với **tải công việc (workload / 워크로드), bất biến (invariant / 불변식), tỷ lệ (rate / 비율) of thay đổi (change / 변경), miền lỗi (failure domain / 장애 도메인), quyền sở hữu (ownership / 소유권), dữ liệu (data / 데이터) consistency, triển khai (deployment / 배포) topology và organizational communication**.

Hệ thống (system / 시스템) thiết kế (design / 설계) cũng không phải ghép các hộp “bộ cân bằng tải (load balancer / 로드 밸런서) + bộ nhớ đệm (cache / 캐시) + hàng đợi (queue / 큐) + cơ sở dữ liệu (database / 데이터베이스)”. Một thiết kế tốt bắt đầu từ thuộc tính (property / 속성) hệ thống phải giữ, pressure mà nó phải chịu, thất bại (failure / 실패) nào được phép, rồi mới chọn topology và technology.

## 1. kiến trúc (architecture / 아키텍처) là tập các ràng buộc (constraints / 제약조건들) trên thay đổi và thất bại (failure / 실패)

Một kiến trúc (architecture / 아키텍처) tốt làm một số thay đổi dễ và một số thay đổi khó có chủ đích. ranh giới mô-đun (module boundary / 모듈 경계) tốt cho phép hiện thực (implementation / 구현) bên trong đổi mà bên tiêu thụ (consumer / 소비자) không cần biết chi tiết. thất bại (failure / 실패) ranh giới (boundary / 경계) tốt ngăn một thành phần (component / 컴포넌트) bị lỗi kéo cả hệ thống (system / 시스템) sập.

Do đó đánh giá kiến trúc (architecture / 아키텍처) phải hỏi hai loại scenario:

```text
change scenario:
- thêm field/protocol mới
- thay storage engine
- chia team/ownership
- deploy version mới

failure scenario:
- downstream chậm
- region mất
- credential compromise
- DB lag/lock
- cache outage
```

Diagram tĩnh không đủ để trả lời hành vi (behavior / 동작) dưới thay đổi (change / 변경)/thất bại (failure / 실패).

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **2. Bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ thành phần (component / 컴포넌트)** tiếp nhận điểm tựa từ **1. kiến trúc (architecture / 아키텍처) là tập các ràng buộc (constraints / 제약조건들) trên thay đổi và thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. chất lượng (quality / 품질) attributes tạo sự đánh đổi (trade-off / 트레이드오프) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ thành phần (component / 컴포넌트)

Ví dụ một payment hệ thống (system / 시스템) có thể có bất biến (invariant / 불변식):

```text
một payment intent không bị charge hai lần
successful charge phải có audit trail
caller timeout không được làm mất khả năng xác định outcome
```

Từ đây mới suy ra idempotency key, máy trạng thái (state machine / 상태 머신), durable log/outbox, thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론) và reconciliation.

Nếu bắt đầu bằng “dùng Kafka hay RabbitMQ?”, ta đang chọn hiện thực (implementation / 구현) trước khi biết thuộc tính (property / 속성) cần giữ.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **3. chất lượng (quality / 품질) attributes tạo sự đánh đổi (trade-off / 트레이드오프) thật** tiếp nhận điểm tựa từ **2. Bắt đầu từ bất biến (invariant / 불변식), không bắt đầu từ thành phần (component / 컴포넌트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. tải công việc (workload / 워크로드) mô hình (model / 모델) là đầu vào (input / 입력) kiến trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. chất lượng (quality / 품질) attributes tạo sự đánh đổi (trade-off / 트레이드오프) thật

Độ trễ (latency / 지연 시간), availability, consistency, bảo mật (security / 보안), operability, modifiability và chi phí (cost / 비용) thường xung đột.

Tách dịch vụ (service / 서비스) có thể quy mô (scale / 규모)/deploy độc lập nhưng thêm:

```text
network partial failure
serialization/schema evolution
cross-service tracing
retry/idempotency
cross-service data consistency
more operational surfaces
```

“Microservices scalable hơn” là statement quá thô. Cần hỏi quy mô (scale / 규모) **tài nguyên (resource / 자원) nào**, thất bại (failure / 실패) ranh giới (boundary / 경계) nào và coordination chi phí (cost / 비용) nào.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **4. tải công việc (workload / 워크로드) mô hình (model / 모델) là đầu vào (input / 입력) kiến trúc** tiếp nhận điểm tựa từ **3. chất lượng (quality / 품질) attributes tạo sự đánh đổi (trade-off / 트레이드오프) thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Bottleneck tài nguyên (resource / 자원) quyết định topology hữu ích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. tải công việc (workload / 워크로드) mô hình (model / 모델) là đầu vào (input / 입력) kiến trúc

Thiết kế cho 100 RPS đều khác 100k RPS bursty; 99% read khác write-heavy; đối tượng (object / 객체) 1 KB khác 100 MB; toàn cục (global / 전역) users khác single region.

Tải công việc (workload / 워크로드) mô hình (model / 모델) nên gồm:

```text
arrival distribution, không chỉ average
read/write ratio
request/service-time distribution
object/data size
hot-key/skew
consistency/durability requirement
retention/growth
failure/recovery target
```

Hệ thống (system / 시스템) thiết kế (design / 설계) không có meaning nếu các giả định (assumptions / 가정들) tải công việc (workload / 워크로드) không được nói rõ.

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **4. tải công việc (workload / 워크로드) mô hình (model / 모델) là đầu vào (input / 입력) kiến trúc** nêu điều cần giải thích; **5. Bottleneck tài nguyên (resource / 자원) quyết định topology hữu ích** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. trạng thái (state / 상태) placement là quyết định (decision / 결정) trung tâm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Bottleneck tài nguyên (resource / 자원) quyết định topology hữu ích

Scale-out ứng dụng (application / 애플리케이션) nodes không tăng sức chứa (capacity / 용량) nếu bottleneck là dùng chung (shared / 공유) cơ sở dữ liệu (database / 데이터베이스) khóa (lock / 잠금), lưu trữ (storage / 저장소) IOPS hoặc third-party quota.

Mỗi quy mô (scale / 규모) quyết định (decision / 결정) nên hỏi:

```text
resource nào đang giới hạn throughput?
request giữ resource đó bao lâu?
resource có partition được không?
partition key có tạo hot spot không?
queue nằm đâu trước resource?
```

Điều này nối trực tiếp hệ thống (system / 시스템) thiết kế (design / 설계) với [capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **5. Bottleneck tài nguyên (resource / 자원) quyết định topology hữu ích** nêu điều cần giải thích; **6. trạng thái (state / 상태) placement là quyết định (decision / 결정) trung tâm** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) và giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải khớp bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. trạng thái (state / 상태) placement là quyết định (decision / 결정) trung tâm

Stateless compute dễ replicate nhưng ứng dụng (application / 애플리케이션) thực tế luôn có trạng thái (state / 상태) ở đâu đó: cơ sở dữ liệu (database / 데이터베이스), bộ nhớ đệm (cache / 캐시), đối tượng (object / 객체) store, hàng đợi (queue / 큐), session, cục bộ (local / 로컬) filesystem hoặc bên ngoài (external / 외부) dịch vụ (service / 서비스).

Trạng thái (state / 상태) placement quyết định:

```text
failure/recovery behavior
consistency boundary
deployment coupling
migration difficulty
latency/locality
backup/retention
```

“Stateless dịch vụ (service / 서비스)” chỉ có nghĩa trạng thái (state / 상태) được đẩy sang ranh giới (boundary / 경계) khác, không phải trạng thái (state / 상태) biến mất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **6. trạng thái (state / 상태) placement là quyết định (decision / 결정) trung tâm** đã nêu tiêu chí phân biệt, còn **7. dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) và giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải khớp bất biến (invariant / 불변식)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Synchronous lời gọi (call / 호출) tạo temporal coupling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) và giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải khớp bất biến (invariant / 불변식)

Hai services có API riêng nhưng cùng sửa tables của nhau chưa có dữ liệu (data / 데이터) autonomy. Ngược lại, tách cơ sở dữ liệu (database / 데이터베이스) chỉ để đạt purity có thể tạo saga/eventual-consistency độ phức tạp (complexity / 복잡도) không cần thiết.

Nếu hai facts phải lần ghi nhận (commit / 커밋) atomically rất thường xuyên vì cùng nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식), việc tách chúng qua mạng (network / 네트워크) có thể đang cắt sai aggregate ranh giới (boundary / 경계).

Ranh giới (boundary / 경계) nên được chọn từ **quyền sở hữu (ownership / 소유권) + bất biến (invariant / 불변식) + thay đổi (change / 변경) tỷ lệ (rate / 비율)**, không từ sơ đồ tổ chức mong muốn đơn lẻ.

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **7. dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) và giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải khớp bất biến (invariant / 불변식)** đã nêu tiêu chí phân biệt, còn **8. Synchronous lời gọi (call / 호출) tạo temporal coupling** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Synchronous lời gọi (call / 호출) tạo temporal coupling

Dịch vụ (service / 서비스) A gọi B synchronously nghĩa A's độ trễ (latency / 지연 시간)/availability phụ thuộc B trong yêu cầu (request / 요청) cửa sổ (window / 윈도우).

Async hàng đợi (queue / 큐)/sự kiện (event / 이벤트) có thể giảm temporal coupling nhưng tạo ngữ nghĩa (semantic / 의미적) độ phức tạp (complexity / 복잡도) mới:

```text
delivery duplicate
ordering
backlog
consumer lag
schema evolution
reconciliation
```

Không có “async = resilient” tự động. Nó đổi thất bại (failure / 실패) shape từ yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) sang backlog/trạng thái (state / 상태) convergence.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **9. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** tiếp nhận điểm tựa từ **8. Synchronous lời gọi (call / 호출) tạo temporal coupling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. bộ nhớ đệm (cache / 캐시) là consistency quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt

Hàng đợi (queue / 큐) hấp thụ mismatch tạm thời giữa producer/bên tiêu thụ (consumer / 소비자), nhưng hàng đợi (queue / 큐) dài là outstanding công việc (work / 작업) phải trả sau.

Hệ thống (system / 시스템) thiết kế (design / 설계) cần định nghĩa:

```text
max backlog?
deadline/TTL của message?
poison message?
retry/DLQ semantics?
consumer recovery rate > arrival rate sau outage không?
```

Nếu khôi phục (recovery / 복구) thông lượng (throughput / 처리량) chỉ bằng arrival thông lượng (throughput / 처리량), backlog sau sự cố (incident / 인시던트) không bao giờ được trả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **10. bộ nhớ đệm (cache / 캐시) là consistency quyết định (decision / 결정)** tiếp nhận điểm tựa từ **9. hàng đợi (queue / 큐) là trạng thái (state / 상태) và debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. miền lỗi (failure domain / 장애 도메인) phải cụ thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. bộ nhớ đệm (cache / 캐시) là consistency quyết định (decision / 결정)

Bộ nhớ đệm (cache / 캐시) không chỉ “giảm DB tải (load / 로드)”. Nó tạo replica trạng thái (state / 상태) và freshness đặc tả hợp đồng (contract / 계약).

Khi thiết kế bộ nhớ đệm (cache / 캐시), hỏi nguồn chuẩn (source of truth / 정본), staleness tolerance, vô hiệu hóa (invalidation / 무효화) thứ tự (ordering / 순서), hot-key hành vi (behavior / 동작) và origin sức chứa (capacity / 용량) khi bộ nhớ đệm (cache / 캐시) thất bại (fail / 실패).

Xem [Caching consistency](../../08_software_systems/advanced/02_caching_consistency_invalidation_stampede_and_hot_keys.md).

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **11. miền lỗi (failure domain / 장애 도메인) phải cụ thể** tiếp nhận điểm tựa từ **10. bộ nhớ đệm (cache / 캐시) là consistency quyết định (decision / 결정)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. thử lại (retry / 재시도) chính sách (policy / 정책) là kiến trúc (architecture / 아키텍처), không phải máy khách (client / 클라이언트) helper** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. miền lỗi (failure domain / 장애 도메인) phải cụ thể

“Highly available” không đủ. Cần nói survive cái gì:

```text
process crash?
node loss?
AZ/rack loss?
region loss?
control-plane outage?
operator error?
credential compromise?
```

Replication trong cùng rack không bảo vệ rack thất bại (failure / 실패). Multi-region replication không bảo vệ bad ghi (write / 쓰기) đã replicate. Backup không giúp yêu cầu (request / 요청) availability ngay lập tức.

Độ tin cậy (reliability / 신뢰성) thiết kế (design / 설계) phải map cơ chế (mechanism / 메커니즘) vào thất bại (failure / 실패) mô hình (model / 모델) cụ thể.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **12. thử lại (retry / 재시도) chính sách (policy / 정책) là kiến trúc (architecture / 아키텍처), không phải máy khách (client / 클라이언트) helper** tiếp nhận điểm tựa từ **11. miền lỗi (failure domain / 장애 도메인) phải cụ thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. ranh giới bảo mật (security boundary / 보안 경계) cũng là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. thử lại (retry / 재시도) chính sách (policy / 정책) là kiến trúc (architecture / 아키텍처), không phải máy khách (client / 클라이언트) helper

Thử lại (retry / 재시도) thay đổi tải (load / 로드) và side-effect ngữ nghĩa (semantics / 의미론) toàn lời gọi (call / 호출) đồ thị (graph / 그래프). Proxy, SDK và ứng dụng (application / 애플리케이션) cùng thử lại (retry / 재시도) có thể nhân attempts ngoài dự kiến.

Architectural rà soát (review / 검토) cần biết tầng nào được thử lại (retry / 재시도), ngân sách (budget / 예산) bao nhiêu, thao tác (operation / 연산) có idempotent không, deadline còn bao nhiêu và overload vòng phản hồi (feedback loop / 피드백 루프) được chặn ở đâu.

Xem [end-to-end request + overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **12. thử lại (retry / 재시도) chính sách (policy / 정책) là kiến trúc (architecture / 아키텍처), không phải máy khách (client / 클라이언트) helper** đã nêu tiêu chí phân biệt, còn **13. ranh giới bảo mật (security boundary / 보안 경계) cũng là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Reversibility quyết định mức đầu tư quyết định (decision / 결정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. ranh giới bảo mật (security boundary / 보안 경계) cũng là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)

Định danh (identity / 식별자) đổi khi yêu cầu (request / 요청) đi qua trình duyệt (browser / 브라우저) → edge → dịch vụ (service / 서비스) → cơ sở dữ liệu (database / 데이터베이스)/KMS. TLS termination, đơn vị từ (token / 토큰) exchange hoặc proxy header đều thay trust mô hình (model / 모델).

Kiến trúc (architecture / 아키텍처) rà soát (review / 검토) phải hỏi:

```text
principal ở mỗi hop là ai?
authorization nằm ở đâu?
secret/capability scope là gì?
compromise một service lan được tới đâu?
```

Bảo mật (security / 보안) không phải checklist thêm sau topology; trust đồ thị (graph / 그래프) là một phần topology.

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **13. ranh giới bảo mật (security boundary / 보안 경계) cũng là kiến trúc (architecture / 아키텍처) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **14. Reversibility quyết định mức đầu tư quyết định (decision / 결정)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) quan trọng hơn mục tiêu (target / 대상) diagram** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Reversibility quyết định mức đầu tư quyết định (decision / 결정)

Quyết định (decision / 결정) dễ đảo như cục bộ (local / 로컬) bộ nhớ đệm (cache / 캐시) thư viện (library / 라이브러리) nên thử nhanh. quyết định (decision / 결정) khó đảo như partition key, công khai (public / 공개) giao thức (protocol / 프로토콜), định danh (identity / 식별자) mô hình (model / 모델) hoặc dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권) cần nhiều bằng chứng (evidence / 증거) hơn.

ADR hữu ích khi ghi:

```text
context + invariant
assumptions/workload
alternatives
chosen trade-off
failure consequences
revisit trigger
```

ADR là snapshot lập luận (reasoning / 추론), không phải bằng chứng quyết định (decision / 결정) sẽ đúng mãi.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **14. Reversibility quyết định mức đầu tư quyết định (decision / 결정)** xác định đầu vào; **15. di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) quan trọng hơn mục tiêu (target / 대상) diagram** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. tính tương thích (compatibility / 호환성) là phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) quan trọng hơn mục tiêu (target / 대상) diagram

Kiến trúc vận hành (production architecture / 운영 아키텍처) hiếm khi rewrite một lần. Safe evolution thường cần:

```text
old system
→ compatibility seam
→ dual-read/replication/backfill có kiểm soát
→ verify equivalence
→ shift traffic
→ retire old path
```

Dual-write nguy hiểm nếu thiếu idempotency/reconciliation. Backfill có thể phá môi trường vận hành (production / 운영 환경) sức chứa (capacity / 용량). di chuyển (migration / 마이그레이션) thiết kế (design / 설계) phải có khả năng quan sát (observability / 관측 가능성) và quay lui (rollback / 롤백)/roll-forward story.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **15. di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) quan trọng hơn mục tiêu (target / 대상) diagram** xác định đầu vào; **16. tính tương thích (compatibility / 호환성) là phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **17. Conway's Law là coupling giữa communication đồ thị (graph / 그래프) và software đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. tính tương thích (compatibility / 호환성) là phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian

Khi old/new binaries cùng chạy, API/lược đồ (schema / 스키마)/dữ liệu (data / 데이터) phải hợp lệ trong overlap cửa sổ (window / 윈도우).

Triển khai (deployment / 배포) topology vì thế biến tính tương thích (compatibility / 호환성) thành phân tán (distributed / 분산) ràng buộc (constraint / 제약조건). “mã (code / 코드) mới compile” không chứng minh mixed-version fleet hoạt động đúng.

Expand-contract và tolerant reader/writer strategies nên được lập luận (reasoning / 추론) từ coexistence cửa sổ (window / 윈도우) cụ thể.

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **17. Conway's Law là coupling giữa communication đồ thị (graph / 그래프) và software đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **16. tính tương thích (compatibility / 호환성) là phân tán (distributed / 분산) giao thức (protocol / 프로토콜) theo thời gian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. kiến trúc (architecture / 아키텍처) rà soát (review / 검토) nên dùng stress/thất bại (failure / 실패) scenarios** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Conway's Law là coupling giữa communication đồ thị (graph / 그래프) và software đồ thị (graph / 그래프)

Nếu hai teams phải thay cùng thành phần (component / 컴포넌트) liên tục nhưng quyền sở hữu (ownership / 소유권) tách rời, coordination chi phí (cost / 비용) trở thành kiến trúc (architecture / 아키텍처) reality. Nếu dịch vụ (service / 서비스) boundaries cắt qua năng lực (capability / 역량) sai, hệ thống (system / 시스템) có chatty mạng (network / 네트워크) calls và cross-team transactions.

Socio-technical thiết kế (design / 설계) nhìn mã (code / 코드) đồ thị (graph / 그래프), dữ liệu (data / 데이터) đồ thị (graph / 그래프) và communication đồ thị (graph / 그래프) cùng lúc.

Một monolith modular có thể ít coupling hơn một fleet microservices phải bản phát hành (release / 릴리스) đồng bộ.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **18. kiến trúc (architecture / 아키텍처) rà soát (review / 검토) nên dùng stress/thất bại (failure / 실패) scenarios** tiếp nhận điểm tựa từ **17. Conway's Law là coupling giữa communication đồ thị (graph / 그래프) và software đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. bằng chứng vận hành (production evidence / 운영 증거) phải kiểm chứng giả định (assumption / 가정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. kiến trúc (architecture / 아키텍처) rà soát (review / 검토) nên dùng stress/thất bại (failure / 실패) scenarios

Thay vì hỏi “có clean kiến trúc (architecture / 아키텍처) không?”, dùng scenarios:

```text
traffic 10x trong 5 phút
DB p99 tăng 20x
cache mất toàn cluster
region A mất
schema N+1 deploy khi N vẫn chạy
client retry sau timeout
credential service A bị compromise
storage flush latency spike
```

Scenario buộc thiết kế (design / 설계) reveal hidden các giả định (assumptions / 가정들), queues và thất bại (failure / 실패) propagation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **18. kiến trúc (architecture / 아키텍처) rà soát (review / 검토) nên dùng stress/thất bại (failure / 실패) scenarios** nêu điều cần giải thích; **19. bằng chứng vận hành (production evidence / 운영 증거) phải kiểm chứng giả định (assumption / 가정)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Lower lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. bằng chứng vận hành (production evidence / 운영 증거) phải kiểm chứng giả định (assumption / 가정)

Kiến trúc (architecture / 아키텍처) không chỉ tồn tại trong document. Các giả định (assumption / 가정) cần metrics/traces/logs hoặc tests:

```text
actual traffic/skew
queue wait và saturation
dependency critical path
failure injection result
replication/recovery lag
schema/version compatibility errors
security policy decisions
cost per workload unit
```

Nếu ADR nói “bộ nhớ đệm (cache / 캐시) outage không ảnh hưởng origin” nhưng chaos kiểm thử (test / 테스트) làm DB sập, kiến trúc (architecture / 아키텍처) bằng chứng (evidence / 증거) đã phủ định giả định (assumption / 가정).

> **Chuyển mạch:** Trong **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **19. bằng chứng vận hành (production evidence / 운영 증거) phải kiểm chứng giả định (assumption / 가정)** nêu điều cần giải thích; **20. Lower lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Lower lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Một kiến trúc (architecture / 아키텍처) diagram có thể nói “cơ sở dữ liệu (database / 데이터베이스) durable”, nhưng guarantee cuối phụ thuộc WAL/filesystem/lưu trữ (storage / 저장소). Diagram nói “dịch vụ (service / 서비스) isolated”, nhưng cgroup/DB pool/dùng chung (shared / 공유) KMS có thể là hidden dùng chung (shared / 공유) fate. Diagram nói “secure mTLS”, nhưng authorization chính sách (policy / 정책) có thể vẫn allow-all.

Advanced hệ thống (system / 시스템) thiết kế (design / 설계) luôn hỏi: lớp trừu tượng (abstraction / 추상화) nào bên dưới thực sự giữ thuộc tính (property / 속성) đang hứa?

> **Chuyển mạch:** Ở chặng này của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **21. Mô hình tư duy** gom các mảnh từ **20. Lower lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Mô hình tư duy

> kiến trúc (architecture / 아키텍처) là **thiết kế bất biến (invariant / 불변식), cost-of-change và thất bại (failure / 실패) boundaries dưới tải công việc (workload / 워크로드) + organizational các ràng buộc (constraints / 제약조건들)**. hệ thống (system / 시스템) thiết kế (design / 설계) bắt đầu từ properties và pressure, không từ technology boxes. mẫu (pattern / 패턴) là vocabulary; quyết định (decision / 결정) chất lượng (quality / 품질) đến từ tường minh (explicit / 명시적) các giả định (assumptions / 가정들), bottleneck mô hình (model / 모델), thất bại (failure / 실패) scenarios, di chuyển (migration / 마이그레이션) đường dẫn (path / 경로) và bằng chứng vận hành (production evidence / 운영 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc (architecture / 아키텍처) decisions, evolution và socio-technical các ràng buộc (constraints / 제약조건들)**, **Kết nối** gom các mảnh từ **21. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [System decomposition foundation](../../basic/08_software_systems/07_system_decomposition_services_and_boundaries.md), [Distributed consistency](../../06_networks_distributed_systems/advanced/06_time_clocks_ordering_and_causality.md), [Capacity engineering](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [Security containment](../../90_connections/advanced/00_debugging_across_abstraction_layers.md) và [Deployment safety](./05_deployment_safety_canary_blue_green_flags_and_rollback.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
