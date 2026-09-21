# Giao dịch phân tán: 2PC, consensus, saga và transactional outbox

Một giao dịch trên một database node có thể dựa vào WAL, lock/MVCC và recovery để tạo atomicity. Khi một business operation chạm nhiều database hoặc service, vấn đề thay đổi: không còn một process hay một log duy nhất có quyền quyết định toàn bộ trạng thái.

Ví dụ đặt hàng có thể cần tạo order, trừ inventory, ghi payment và phát event. Nếu bước thứ ba thất bại sau khi hai bước đầu đã commit, hệ thống phải trả lời một câu hỏi khó: **“atomic” có nghĩa gì khi các thành phần có thể crash hoặc mất liên lạc độc lập?**

## 1. Local transaction không tự mở rộng thành distributed transaction

Giả sử service thực hiện:

```text
DB A: COMMIT order
DB B: COMMIT inventory
```

Nếu process chết giữa hai commit, A và B khác trạng thái. Không có rollback thần kỳ vì DB A đã durable và không biết DB B thất bại.

Vấn đề không phải cú pháp SQL; đó là bài toán phối hợp (coordination) dưới failure.

## 2. Two-Phase Commit

**Cam kết hai pha (2PC — Two-Phase Commit)** dùng coordinator và nhiều participant.

Pha chuẩn bị:

```text
coordinator -> PREPARE?
participant -> YES / NO
```

Participant trả `YES` phải ghi đủ trạng thái durable để sau crash vẫn có thể commit nếu coordinator yêu cầu.

Pha quyết định:

```text
all YES -> COMMIT
otherwise -> ABORT
```

2PC tạo atomic commitment nhưng có giá: participant đã prepared có thể phải giữ lock/resource trong khi chờ quyết định.

## 3. Failure window và trạng thái in-doubt

Nếu coordinator chết sau khi participants đã prepare nhưng trước khi họ nhận quyết định, participant không thể tự ý commit hoặc abort mà không có thêm protocol. Nó rơi vào **trạng thái chưa biết quyết định (in-doubt state)**.

Đây là lý do 2PC thường được gọi là blocking protocol trong một số failure scenario. Availability giảm để giữ atomicity.

## 4. 2PC không phải consensus

2PC và consensus đều có coordinator/leader-looking behavior nhưng giải quyết vấn đề khác. 2PC hỏi liệu một transaction có commit trên nhiều participant hay không. Consensus giúp một nhóm node đồng thuận một chuỗi quyết định dù một số node fail.

Một coordinator 2PC đơn lẻ có thể là điểm failure. Hệ thống có thể dùng replicated log/consensus để làm decision record của coordinator bền vững hơn, nhưng việc kết hợp hai cơ chế không làm chi phí coordination biến mất.

## 5. Consensus không làm transaction miễn phí

Nếu mỗi shard dùng Raft để replicate state, một cross-shard transaction vẫn phải phối hợp giữa nhiều consensus group. Mỗi group có leader, quorum và log riêng. Transaction có thể cần:

```text
client
 -> transaction coordinator
 -> shard A leader -> quorum A
 -> shard B leader -> quorum B
```

Latency tăng vì nhiều network round trip và durable log. “Database distributed có consensus” không đồng nghĩa cross-shard transaction rẻ như local transaction.

## 6. Saga đổi atomic rollback thành compensation

Trong microservices, nhiều workflow kéo dài quá lâu để giữ distributed lock. **Saga** chia workflow thành các local transaction và định nghĩa hành động bù (compensating action).

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

Compensation không phải rollback vật lý. Email đã gửi không thể “unsend”; giá thị trường có thể đổi; refund là business event mới. Vì vậy saga cần semantics nghiệp vụ rõ ràng.

## 7. Orchestration và choreography

Saga **điều phối tập trung (orchestration)** có một orchestrator quyết định bước tiếp theo. Ưu điểm là workflow dễ nhìn; nhược điểm là coordinator trở thành thành phần quan trọng.

Saga **phối hợp qua sự kiện (choreography)** để mỗi service phản ứng với event. Coupling trực tiếp giảm nhưng flow tổng thể có thể khó quan sát, và event cycle hoặc dependency ẩn dễ xuất hiện.

Không có mô hình luôn tốt hơn; cần cân bằng visibility, ownership và complexity.

## 8. Dual-write problem

Một lỗi kinh điển:

```text
1. UPDATE database
2. publish message to broker
```

Nếu DB commit nhưng process chết trước publish, state đã đổi nhưng event biến mất. Nếu publish trước rồi DB rollback, consumer thấy event về trạng thái chưa tồn tại.

Đây là **bài toán ghi kép (dual-write problem)**: hai hệ thống độc lập không thể được làm atomic chỉ bằng thứ tự hai lời gọi.

## 9. Transactional Outbox

**Mẫu hộp thư giao dịch (transactional outbox pattern)** ghi business state và event cần phát vào cùng local transaction:

```sql
BEGIN;
UPDATE orders ...;
INSERT INTO outbox(event_id, payload, status) ...;
COMMIT;
```

Một relay riêng đọc outbox và publish sang broker. Nếu relay crash sau publish nhưng trước khi đánh dấu sent, event có thể được publish lại. Vì vậy consumer cần idempotency hoặc deduplication.

Outbox đổi bài toán “không được mất event” thành bài toán dễ quản lý hơn: **at-least-once delivery + duplicate handling**.

## 10. Inbox và idempotency

Consumer có thể lưu `event_id` đã xử lý trong một bảng inbox cùng transaction với business update:

```text
if event_id already processed:
    skip
else:
    apply business change
    record event_id
```

Đây là cách biến delivery lặp thành effect gần exactly-once ở boundary nghiệp vụ. Exactly-once thường không phải thuộc tính của network packet; nó là kết quả của protocol, durable state và idempotent semantics.

## 11. Isolation xuyên service khó hơn atomicity

Ngay cả khi workflow cuối cùng thành công, các service khác có thể quan sát trạng thái trung gian. Saga thường chấp nhận **nhất quán cuối cùng (eventual consistency)**.

Ví dụ inventory đã reserve nhưng payment chưa hoàn tất. Reporting service có thể thấy order ở trạng thái `PENDING_PAYMENT`. Thay vì cố giấu mọi trạng thái trung gian, domain model nên biểu diễn chúng rõ ràng.

## 12. Timeout không cho biết operation thất bại

Nếu client gửi `charge` và timeout, có ba khả năng:

```text
request chưa tới server
server xử lý nhưng response mất
server đang xử lý
```

Retry mù có thể charge hai lần. Vì vậy payment API thường cần **khóa idempotency (idempotency key)**. Server lưu kết quả theo key và trả lại cùng outcome cho retry tương đương.

Timeout chỉ nói rằng caller không nhận kết quả đúng hạn; nó không chứng minh remote operation chưa xảy ra.

## 13. Exactly-once là property end-to-end

Broker có thể cung cấp transaction hoặc exactly-once trong phạm vi riêng, nhưng application còn DB, HTTP side effect và external provider. Nếu một effect nằm ngoài transaction boundary của broker, guarantee phải được xây lại ở tầng cao hơn.

Do đó cần hỏi chính xác:

> Exactly once đối với **cái gì**, trong **boundary nào**, và được chứng minh bằng durable state nào?

## 14. Khi nào dùng 2PC, saga hay outbox?

Nếu nhiều resource cùng hỗ trợ transaction protocol và cần atomicity mạnh, 2PC có thể phù hợp dù availability/latency có giá. Nếu workflow dài, có business compensation tự nhiên và service ownership độc lập, saga thường phù hợp hơn. Nếu cần đồng bộ database change với message publication, outbox là primitive thực dụng.

Các pattern này không loại trừ nhau. Một hệ thống lớn có thể dùng local ACID transaction + outbox trong mỗi service, saga giữa service, và consensus bên trong database cluster.

## 15. Failure matrix

Thiết kế distributed transaction nên viết rõ failure matrix thay vì chỉ happy path:

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

Mỗi hàng cần một recovery rule. Nếu không thể giải thích outcome sau từng failure, protocol chưa hoàn chỉnh.

## Common Misconceptions

**“Retry sẽ làm hệ thống reliable.”** Retry không có idempotency có thể nhân đôi side effect.

**“Saga giống rollback database.”** Không. Compensation là business action mới và có thể không đảo ngược hoàn hảo quá khứ.

**“Exactly-once delivery giải quyết mọi duplicate.”** Guarantee của transport không tự bao phủ database và external side effect.

**“2PC và Raft là cùng một thứ.”** Chúng giải quyết các bài toán coordination khác nhau dù có thể được kết hợp.

## Mental Model

> Distributed transaction là bài toán **duy trì một câu chuyện nghiệp vụ nhất quán khi không có một nơi duy nhất kiểm soát toàn bộ sự thật và failure có thể xảy ra giữa mọi bước**.

Thay vì hỏi “làm sao rollback mọi thứ?”, hãy hỏi: boundary atomic nào thực sự tồn tại, trạng thái trung gian nào được phép, operation nào idempotent, recovery dựa vào log nào và business compensation nghĩa là gì.

Xem thêm: [MVCC/WAL](./00_mvcc_visibility_wal_and_recovery_internals.md), [Distributed Systems](../../06_networks_distributed_systems/advanced/README.md) và [Idempotency](../../08_software_systems/advanced/05_idempotency_and_deduplication_at_scale.md).
