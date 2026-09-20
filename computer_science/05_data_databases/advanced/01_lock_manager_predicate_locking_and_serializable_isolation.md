# Lock manager, predicate locking và serializable isolation

MVCC giúp nhiều transaction đọc/ghi đồng thời, nhưng isolation mạnh vẫn cần cơ chế phát hiện hoặc ngăn các execution tương đương sai. Advanced database concurrency không chỉ là “row lock”. Ta cần hiểu **lock manager, lock compatibility, deadlock, predicate/range protection và serializability**.

## Lock manager là một subsystem riêng

Database duy trì metadata về resource nào đang bị lock, transaction nào sở hữu lock và transaction nào đang chờ.

Resource có thể là row, key, page, table, index range hoặc logical predicate tùy engine.

Lock manager phải trả lời nhanh:

```text
request lock -> compatible?
             -> grant ngay
             -> hoặc enqueue waiter
```

Nó cũng phải release lock khi commit/rollback và xử lý deadlock.

## Shared và exclusive chỉ là khởi đầu

Shared lock cho nhiều readers cùng tồn tại. Exclusive lock xung đột với reader/writer khác.

Production DB còn có intent locks ở hierarchy table/page/row để tránh phải scan hàng triệu child locks khi muốn lock cấp cao hơn.

Ví dụ `IX` trên table nói rằng transaction có hoặc sẽ có exclusive lock ở một số descendants; nó giúp compatibility check cấp table có meaning.

## Two-phase locking

**2PL** về conceptual có growing phase acquire locks và shrinking phase release locks. Strict 2PL thường giữ write locks tới commit/abort, giúp tránh dirty write/read và làm recovery reasoning dễ hơn.

Serializable schedule có thể đạt bằng locking thích hợp, nhưng concurrency giảm khi lock scope lớn hoặc transaction dài.

## Deadlock

Transaction A giữ X và chờ Y; B giữ Y và chờ X. Nếu chỉ chờ, cả hai đứng mãi.

DB có thể dùng **wait-for graph** và cycle detection, hoặc timeout/deadlock prevention schemes. Khi phát hiện cycle, engine chọn victim rollback.

Application phải coi deadlock error là expected concurrency outcome có thể retry, không phải “DB bị lỗi”.

## Row lock chưa đủ chống phantom

Giả sử transaction đọc:

```sql
SELECT * FROM orders WHERE amount > 1000;
```

Nó lock tất cả rows hiện có thỏa điều kiện. Transaction khác insert một row mới `amount=5000`. Khi query chạy lại, row “phantom” xuất hiện dù không row cũ nào bị sửa.

Để serializable theo locking, database cần bảo vệ **predicate/key range**, không chỉ rows đã materialize.

## Predicate lock và index-range lock

Predicate lock lý tưởng bảo vệ tập “mọi row thỏa `amount > 1000`”. Implement trực tiếp predicate tổng quát rất đắt.

Nhiều engine dùng index-range/gap/next-key locking khi query có index phù hợp. Lock một interval trong B+Tree keyspace ngăn insert vào range có thể thay result.

Do đó index design có thể ảnh hưởng không chỉ performance mà cả granularity concurrency control.

## MVCC + Serializable không có một implementation duy nhất

Một số engine dùng locking serializable; một số dùng Serializable Snapshot Isolation (SSI) phát hiện dangerous dependency patterns trên snapshot execution; có hệ dùng optimistic validation.

“Isolation level = Serializable” là semantic goal. Mechanism bên dưới có thể rất khác và failure mode/retry behavior cũng khác.

## Write skew

Hai doctors cùng kiểm tra “ít nhất một doctor đang on-call”. Mỗi transaction thấy hai người on-call và tắt chính mình. Hai writes ở rows khác nhau nên không write-write conflict, nhưng invariant cuối cùng bị phá.

Snapshot isolation có thể cho phép write skew. Serializable cần nhận ra dependency logical giữa reads và writes hoặc dùng predicate protection.

Đây là lý do chỉ nhìn row write conflict không đủ reasoning business invariant.

## Long transaction là concurrency hazard

Transaction giữ locks lâu hoặc giữ snapshot quá cũ làm contention/version retention tăng. Một API request mở transaction rồi gọi external service trong 5 giây có thể làm DB concurrency tệ mạnh.

Transaction boundary nên ôm đúng atomic state transition cần thiết, không phải toàn workflow business nếu không cần.

## Lock escalation

Quá nhiều row locks tốn memory/management overhead. Engine có thể escalate thành page/table lock. Điều này giảm lock metadata nhưng tăng contention bất ngờ.

Một query update nhiều rows có thể vì vậy ảnh hưởng concurrent requests rộng hơn developer nghĩ.

## Observability

Khi hệ thống chậm, cần phân biệt CPU/I/O bottleneck với lock wait.

Thông tin hữu ích: blocking session, lock mode/resource, wait duration, transaction age, deadlock graph và SQL/plan gây lock footprint.

“Query chạy lâu” đôi khi thực tế là query chạy 10ms nhưng chờ lock 4s.

## Mental Model

> Serializable isolation bảo vệ **lịch sử logic của transactions**, không chỉ từng row. Lock manager quản lý quyền truy cập; predicate/range locking bảo vệ những rows chưa tồn tại; deadlock/retry là một phần tự nhiên của concurrency control.

## Common Misconceptions

**“MVCC nghĩa không cần lock.”** Writers, schema changes và serializable mechanisms vẫn có thể cần lock/latch.

**“Row lock ngăn phantom.”** Không nếu new row có thể xuất hiện trong predicate range.

**“Deadlock là bug của DB.”** Nó là possible outcome của concurrent lock acquisition; design transaction order và retry strategy mới là phần application cần xử lý.

## Kết nối

Tiếp theo đọc [B+Tree page layout và latch coupling](./02_btree_page_layout_splits_merges_and_latch_coupling.md). Với Oracle/SQL systems, nên kết hợp execution plan, index range và transaction scope để hiểu lock footprint thực tế.