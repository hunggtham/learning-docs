# Giao dịch phân tán: 2PC, consensus, saga và transactional outbox

> **Mạch đọc:** Đặt **Giao dịch phân tán: 2PC, consensus, saga và transactional outbox** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) không tự mở rộng thành phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션)** sang **2. Two-Phase lần ghi nhận (commit / 커밋)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một giao dịch trên một cơ sở dữ liệu (database / 데이터베이스) nút (node / 노드) có thể dựa vào WAL, khóa (lock / 잠금)/MVCC và khôi phục (recovery / 복구) để tạo atomicity. Khi một nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) chạm nhiều cơ sở dữ liệu (database / 데이터베이스) hoặc dịch vụ (service / 서비스), vấn đề thay đổi: không còn một tiến trình (process / 프로세스) hay một log duy nhất có quyền quyết định toàn bộ trạng thái.

Ví dụ đặt hàng có thể cần tạo thứ tự (order / 순서), trừ inventory, ghi payment và phát sự kiện (event / 이벤트). Nếu bước thứ ba thất bại sau khi hai bước đầu đã lần ghi nhận (commit / 커밋), hệ thống phải trả lời một câu hỏi khó: **“atomic” có nghĩa gì khi các thành phần có thể crash hoặc mất liên lạc độc lập?**

## 1. cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) không tự mở rộng thành phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션)

Giả sử dịch vụ (service / 서비스) thực hiện:

```text
DB A: COMMIT order
DB B: COMMIT inventory
```

Nếu tiến trình (process / 프로세스) chết giữa hai lần ghi nhận (commit / 커밋), A và B khác trạng thái. Không có quay lui (rollback / 롤백) thần kỳ vì DB A đã durable và không biết DB B thất bại.

Vấn đề không phải cú pháp SQL; đó là bài toán phối hợp (coordination) dưới thất bại (failure / 실패).

## 2. Two-Phase lần ghi nhận (commit / 커밋)

**Cam kết hai pha (2PC — Two-Phase Commit)** dùng coordinator và nhiều participant.

Pha chuẩn bị:

```text
coordinator -> PREPARE?
participant -> YES / NO
```

Participant trả `YES` phải ghi đủ trạng thái durable để sau crash vẫn có thể lần ghi nhận (commit / 커밋) nếu coordinator yêu cầu.

Pha quyết định:

```text
all YES -> COMMIT
otherwise -> ABORT
```

2PC tạo atomic commitment nhưng có giá: participant đã prepared có thể phải giữ khóa (lock / 잠금)/tài nguyên (resource / 자원) trong khi chờ quyết định.

## 3. thất bại (failure / 실패) cửa sổ (window / 윈도우) và trạng thái in-doubt

Nếu coordinator chết sau khi participants đã prepare nhưng trước khi họ nhận quyết định, participant không thể tự ý lần ghi nhận (commit / 커밋) hoặc abort mà không có thêm giao thức (protocol / 프로토콜). Nó rơi vào **trạng thái chưa biết quyết định (in-doubt state)**.

Đây là lý do 2PC thường được gọi là blocking giao thức (protocol / 프로토콜) trong một số thất bại (failure / 실패) scenario. Availability giảm để giữ atomicity.

## 4. 2PC không phải consensus

2PC và consensus đều có coordinator/leader-looking hành vi (behavior / 동작) nhưng giải quyết vấn đề khác. 2PC hỏi liệu một giao dịch (transaction / 트랜잭션) có lần ghi nhận (commit / 커밋) trên nhiều participant hay không. Consensus giúp một nhóm nút (node / 노드) đồng thuận một chuỗi quyết định dù một số nút (node / 노드) thất bại (fail / 실패).

Một coordinator 2PC đơn lẻ có thể là điểm thất bại (failure / 실패). Hệ thống có thể dùng replicated log/consensus để làm quyết định (decision / 결정) bản ghi (record / 레코드) của coordinator bền vững hơn, nhưng việc kết hợp hai cơ chế không làm chi phí coordination biến mất.

## 5. Consensus không làm giao dịch (transaction / 트랜잭션) miễn phí

Nếu mỗi shard dùng Raft để replicate trạng thái (state / 상태), một cross-shard giao dịch (transaction / 트랜잭션) vẫn phải phối hợp giữa nhiều consensus group. Mỗi group có leader, quorum và log riêng. giao dịch (transaction / 트랜잭션) có thể cần:

```text
client
 -> transaction coordinator
 -> shard A leader -> quorum A
 -> shard B leader -> quorum B
```

Độ trễ (latency / 지연 시간) tăng vì nhiều mạng (network / 네트워크) round trip và durable log. “cơ sở dữ liệu (database / 데이터베이스) phân tán (distributed / 분산) có consensus” không đồng nghĩa cross-shard giao dịch (transaction / 트랜잭션) rẻ như cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션).

## 6. Saga đổi atomic quay lui (rollback / 롤백) thành compensation

Trong microservices, nhiều workflow kéo dài quá lâu để giữ phân tán (distributed / 분산) khóa (lock / 잠금). **Saga** chia workflow thành các cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션) và định nghĩa hành động bù (compensating action).

```text
reserve inventory
charge payment
create shipment
```

Nếu shipment thất bại:

```text
refund payment
release inventory
```

Compensation không phải quay lui (rollback / 롤백) vật lý. Email đã gửi không thể “unsend”; giá thị trường có thể đổi; refund là nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트) mới. Vì vậy saga cần ngữ nghĩa (semantics / 의미론) nghiệp vụ rõ ràng.

## 7. Orchestration và choreography

Saga **điều phối tập trung (orchestration)** có một orchestrator quyết định bước tiếp theo. Ưu điểm là workflow dễ nhìn; nhược điểm là coordinator trở thành thành phần quan trọng.

Saga **phối hợp qua sự kiện (choreography)** để mỗi dịch vụ (service / 서비스) phản ứng với sự kiện (event / 이벤트). Coupling trực tiếp giảm nhưng luồng (flow / 흐름) tổng thể có thể khó quan sát, và sự kiện (event / 이벤트) cycle hoặc phụ thuộc (dependency / 의존성) ẩn dễ xuất hiện.

Không có mô hình luôn tốt hơn; cần cân bằng visibility, quyền sở hữu (ownership / 소유권) và độ phức tạp (complexity / 복잡도).

## 8. Dual-write bài toán (problem / 문제)

Một lỗi kinh điển:

```text
1. UPDATE database
2. publish message to broker
```

Nếu DB lần ghi nhận (commit / 커밋) nhưng tiến trình (process / 프로세스) chết trước publish, trạng thái (state / 상태) đã đổi nhưng sự kiện (event / 이벤트) biến mất. Nếu publish trước rồi DB quay lui (rollback / 롤백), bên tiêu thụ (consumer / 소비자) thấy sự kiện (event / 이벤트) về trạng thái chưa tồn tại.

Đây là **bài toán ghi kép (dual-write problem)**: hai hệ thống độc lập không thể được làm atomic chỉ bằng thứ tự hai lời gọi.

## 9. Transactional Outbox

**Mẫu hộp thư giao dịch (transactional outbox pattern)** ghi nghiệp vụ (business / 비즈니스) trạng thái (state / 상태) và sự kiện (event / 이벤트) cần phát vào cùng cục bộ (local / 로컬) giao dịch (transaction / 트랜잭션):

```sql
BEGIN;
UPDATE orders ...;
INSERT INTO outbox(event_id, payload, status) ...;
COMMIT;
```

Một relay riêng đọc outbox và publish sang broker. Nếu relay crash sau publish nhưng trước khi đánh dấu sent, sự kiện (event / 이벤트) có thể được publish lại. Vì vậy bên tiêu thụ (consumer / 소비자) cần idempotency hoặc deduplication.

Outbox đổi bài toán “không được mất sự kiện (event / 이벤트)” thành bài toán dễ quản lý hơn: **at-least-once delivery + duplicate handling**.

## 10. Inbox và idempotency

Bên tiêu thụ (consumer / 소비자) có thể lưu `event_id` đã xử lý trong một bảng inbox cùng giao dịch (transaction / 트랜잭션) với nghiệp vụ (business / 비즈니스) cập nhật (update / 업데이트):

```text
if event_id already processed:
    skip
else:
    apply business change
    record event_id
```

Đây là cách biến delivery lặp thành tác động (effect / 효과) gần exactly-once ở ranh giới (boundary / 경계) nghiệp vụ. Exactly-once thường không phải thuộc tính của mạng (network / 네트워크) packet; nó là kết quả của giao thức (protocol / 프로토콜), durable trạng thái (state / 상태) và idempotent ngữ nghĩa (semantics / 의미론).

## 11. Isolation xuyên dịch vụ (service / 서비스) khó hơn atomicity

Ngay cả khi workflow cuối cùng thành công, các dịch vụ (service / 서비스) khác có thể quan sát trạng thái trung gian. Saga thường chấp nhận **nhất quán cuối cùng (eventual consistency)**.

Ví dụ inventory đã reserve nhưng payment chưa hoàn tất. Reporting dịch vụ (service / 서비스) có thể thấy thứ tự (order / 순서) ở trạng thái `PENDING_PAYMENT`. Thay vì cố giấu mọi trạng thái trung gian, lĩnh vực (domain / 도메인) mô hình (model / 모델) nên biểu diễn chúng rõ ràng.

## 12. hết thời gian chờ (timeout / 타임아웃) không cho biết thao tác (operation / 연산) thất bại

Nếu máy khách (client / 클라이언트) gửi `charge` và hết thời gian chờ (timeout / 타임아웃), có ba khả năng:

```text
request chưa tới server
server xử lý nhưng response mất
server đang xử lý
```

Thử lại (retry / 재시도) mù có thể charge hai lần. Vì vậy payment API thường cần **khóa idempotency (idempotency key)**. máy chủ (server / 서버) lưu kết quả theo key và trả lại cùng kết quả (outcome / 결과) cho thử lại (retry / 재시도) tương đương.

Hết thời gian chờ (timeout / 타임아웃) chỉ nói rằng caller không nhận kết quả đúng hạn; nó không chứng minh remote thao tác (operation / 연산) chưa xảy ra.

## 13. Exactly-once là thuộc tính (property / 속성) end-to-end

Broker có thể cung cấp giao dịch (transaction / 트랜잭션) hoặc exactly-once trong phạm vi riêng, nhưng ứng dụng (application / 애플리케이션) còn DB, HTTP side tác động (effect / 효과) và bên ngoài (external / 외부) provider. Nếu một tác động (effect / 효과) nằm ngoài giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) của broker, guarantee phải được xây lại ở tầng cao hơn.

Do đó cần hỏi chính xác:

> Exactly once đối với **cái gì**, trong **ranh giới (boundary / 경계) nào**, và được chứng minh bằng durable trạng thái (state / 상태) nào?

## 14. Khi nào dùng 2PC, saga hay outbox?

Nếu nhiều tài nguyên (resource / 자원) cùng hỗ trợ giao dịch (transaction / 트랜잭션) giao thức (protocol / 프로토콜) và cần atomicity mạnh, 2PC có thể phù hợp dù availability/độ trễ (latency / 지연 시간) có giá. Nếu workflow dài, có nghiệp vụ (business / 비즈니스) compensation tự nhiên và dịch vụ (service / 서비스) quyền sở hữu (ownership / 소유권) độc lập, saga thường phù hợp hơn. Nếu cần đồng bộ cơ sở dữ liệu (database / 데이터베이스) thay đổi (change / 변경) với message publication, outbox là thành phần nguyên thủy (primitive / 기본 요소) thực dụng.

Các mẫu (pattern / 패턴) này không loại trừ nhau. Một hệ thống lớn có thể dùng cục bộ (local / 로컬) ACID giao dịch (transaction / 트랜잭션) + outbox trong mỗi dịch vụ (service / 서비스), saga giữa dịch vụ (service / 서비스), và consensus bên trong cơ sở dữ liệu (database / 데이터베이스) cluster.

## 15. thất bại (failure / 실패) ma trận (matrix / 행렬)

Thiết kế phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) nên viết rõ thất bại (failure / 실패) ma trận (matrix / 행렬) thay vì chỉ happy đường dẫn (path / 경로):

```text
crash trước local commit
crash sau commit trước publish
message duplicate
message reorder
consumer crash trước commit
consumer commit nhưng ack mất
coordinator mất kết nối
participant unavailable
```

Mỗi hàng cần một khôi phục (recovery / 복구) quy tắc (rule / 규칙). Nếu không thể giải thích kết quả (outcome / 결과) sau từng thất bại (failure / 실패), giao thức (protocol / 프로토콜) chưa hoàn chỉnh.

## Dùng chung (common / 공통) Misconceptions

**“thử lại (retry / 재시도) sẽ làm hệ thống reliable.”** thử lại (retry / 재시도) không có idempotency có thể nhân đôi side tác động (effect / 효과).

**“Saga giống quay lui (rollback / 롤백) cơ sở dữ liệu (database / 데이터베이스).”** Không. Compensation là nghiệp vụ (business / 비즈니스) hành động (action / 동작) mới và có thể không đảo ngược hoàn hảo quá khứ.

**“Exactly-once delivery giải quyết mọi duplicate.”** Guarantee của vận chuyển (transport / 전송) không tự bao phủ cơ sở dữ liệu (database / 데이터베이스) và bên ngoài (external / 외부) side tác động (effect / 효과).

**“2PC và Raft là cùng một thứ.”** Chúng giải quyết các bài toán coordination khác nhau dù có thể được kết hợp.

## Mô hình tư duy (mental model / 사고 모델)

> phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션) là bài toán **duy trì một câu chuyện nghiệp vụ nhất quán khi không có một nơi duy nhất kiểm soát toàn bộ sự thật và thất bại (failure / 실패) có thể xảy ra giữa mọi bước**.

Thay vì hỏi “làm sao quay lui (rollback / 롤백) mọi thứ?”, hãy hỏi: ranh giới (boundary / 경계) atomic nào thực sự tồn tại, trạng thái trung gian nào được phép, thao tác (operation / 연산) nào idempotent, khôi phục (recovery / 복구) dựa vào log nào và nghiệp vụ (business / 비즈니스) compensation nghĩa là gì.

Xem thêm: [MVCC/WAL](./00_mvcc_visibility_wal_and_recovery_internals.md), [Distributed Systems](../../06_networks_distributed_systems/advanced/README.md) và [Idempotency](../../08_software_systems/advanced/05_idempotency_and_deduplication_at_scale.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
