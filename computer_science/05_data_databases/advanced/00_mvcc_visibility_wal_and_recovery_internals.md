# MVCC, visibility, WAL và khôi phục (recovery / 복구) internals

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bài toán ban đầu: tính đồng thời (concurrency / 동시성) không được phá một lịch sử hợp lệ** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. MVCC biến một logical row thành phiên bản (version / 버전) lịch sử (history / 이력)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Ở mức foundation, ACID và MVCC thường được mô tả như cơ chế giúp nhiều transactions chạy đồng thời mà ít khối (block / 블록) nhau. Ở mức advanced, cần tách ba câu hỏi nhưng vẫn nối chúng thành một vòng đời (lifecycle / 생명주기):

```text
Visibility : transaction nào được nhìn thấy version nào?
Durability : history nào sống sót crash?
Reclamation: khi nào history cũ có thể bị quên?
```

Mô hình tư duy (mental model / 사고 모델) của chương này là: **MVCC, WAL, buffer pool, checkpoint, vacuum/purge và replication đều quản lý các biểu diễn (representation / 표현) khác nhau của cùng logical giao dịch (transaction / 트랜잭션) lịch sử (history / 이력). tính đúng đắn (correctness / 정확성) phụ thuộc vào việc các biểu diễn (representation / 표현) đó không vượt quá authority mà giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) cho phép.**

## 1. Bài toán ban đầu: tính đồng thời (concurrency / 동시성) không được phá một lịch sử hợp lệ

Nếu reader luôn khối (block / 블록) writer và writer luôn khối (block / 블록) reader, tính đúng đắn (correctness / 정확성) dễ hơn nhưng tính đồng thời (concurrency / 동시성) thấp. MVCC cho phép nhiều logical versions cùng tồn tại để reader có snapshot ổn định trong khi writer tiếp tục tạo trạng thái (state / 상태) mới.

Bất biến (invariant / 불변식) cơ bản:

> Một giao dịch (transaction / 트랜잭션) chỉ được quan sát versions phù hợp với isolation/snapshot đặc tả hợp đồng (contract / 계약), và crash khôi phục (recovery / 복구) không được biến vật lý (physical / 물리적) bytes chưa có lần ghi nhận (commit / 커밋) authority thành committed lịch sử (history / 이력).

Hai nửa của câu này nối visibility với durability.

> **Chuyển mạch:** Concurrency cần giữ lịch sử hợp lệ; MVCC lưu nhiều row version, còn snapshot định nghĩa visibility/order của transaction chứ không phải bản copy toàn database.

## 2. MVCC biến một logical row thành phiên bản (version / 버전) lịch sử (history / 이력)

Hiện thực (implementation / 구현) khác nhau giữa engines: tuple versions, undo chuỗi (chain / 사슬), phiên bản (version / 버전) store, giao dịch (transaction / 트랜잭션) siêu dữ liệu (metadata / 메타데이터) hoặc combination. Nhưng lớp trừu tượng (abstraction / 추상화) hữu ích là:

```text
logical row
→ version v1 created by T1
→ version v2 created by T2
→ version v3 deleted/updated by T3
```

Reader không lấy “phiên bản (version / 버전) mới nhất theo wall clock”. Nó chạy một **visibility hàm (function / 함수)(snapshot, version, transaction state)**.

Đây là reason hai transactions cùng truy vấn (query / 쿼리) một key tại gần cùng thời điểm có thể hợp lệ khi nhìn thấy hai answers khác nhau.

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **2. MVCC biến một logical row thành phiên bản (version / 버전) lịch sử (history / 이력)** nêu điều cần giải thích; **3. Snapshot là một đặc tả hợp đồng (contract / 계약) về giao dịch (transaction / 트랜잭션) thứ tự (order / 순서), không phải bản sao (copy / 복사) toàn cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Visibility không tự bảo đảm serializability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Snapshot là một đặc tả hợp đồng (contract / 계약) về giao dịch (transaction / 트랜잭션) thứ tự (order / 순서), không phải bản sao (copy / 복사) toàn cơ sở dữ liệu (database / 데이터베이스)

Snapshot thường encode đủ thông tin (information / 정보) để phân biệt giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) trước ranh giới (boundary / 경계), giao dịch (transaction / 트랜잭션) đang active và giao dịch (transaction / 트랜잭션) bắt đầu sau ranh giới (boundary / 경계).

Lập luận (reasoning / 추론) generic:

```text
version do transaction nào tạo?
creator đã commit theo snapshot chưa?
version đã bị transaction nào supersede/delete?
transaction đó có visible đối với snapshot không?
```

Một snapshot không nhất thiết materialize mọi row. Nó là siêu dữ liệu (metadata / 메타데이터)/quy tắc (rule / 규칙) để evaluate visibility khi row được đọc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **3. Snapshot là một đặc tả hợp đồng (contract / 계약) về giao dịch (transaction / 트랜잭션) thứ tự (order / 순서), không phải bản sao (copy / 복사) toàn cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **4. Visibility không tự bảo đảm serializability** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. cập nhật (update / 업데이트) không nhất thiết overwrite trạng thái (state / 상태) cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Visibility không tự bảo đảm serializability

MVCC giảm read-write blocking nhưng isolation mức (level / 수준) vẫn quyết định anomalies nào được phép. Snapshot isolation có thể ngăn nhiều dirty/non-repeatable phenomena nhưng không tự động loại mọi ghi (write / 쓰기) skew hoặc predicate anomaly.

Do đó “DB dùng MVCC” không trả lời giao dịch (transaction / 트랜잭션) tính đúng đắn (correctness / 정확성). Cần hỏi:

```text
application invariant là gì?
isolation level nào đang active?
write-write conflict được detect thế nào?
predicate/range dependency có được bảo vệ không?
```

Đọc [lock manager, predicate locking và serializable isolation](./01_lock_manager_predicate_locking_and_serializable_isolation.md).

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **5. cập nhật (update / 업데이트) không nhất thiết overwrite trạng thái (state / 상태) cũ** tiếp nhận điểm tựa từ **4. Visibility không tự bảo đảm serializability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) là authority của phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. cập nhật (update / 업데이트) không nhất thiết overwrite trạng thái (state / 상태) cũ

Một cập nhật (update / 업데이트) thường tạo phiên bản (version / 버전) mới hoặc ghi new trạng thái (state / 상태) kèm undo thông tin (information / 정보). Old phiên bản (version / 버전) phải tiếp tục tồn tại nếu snapshot cũ vẫn có quyền đọc nó.

Điều này đổi chi phí (cost / 비용) mô hình (model / 모델):

```text
reader ít block writer hơn
↔
engine phải giữ version metadata, old tuples/undo và reclamation work
```

Long-running giao dịch (transaction / 트랜잭션) vì vậy không chỉ “giữ liên kết (connection / 연결) lâu”; nó có thể giữ giao dịch (transaction / 트랜잭션) horizon cũ và ngăn cleanup của lượng lịch sử (history / 이력) lớn.

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **6. giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) là authority của phiên bản (version / 버전)** tiếp nhận điểm tựa từ **5. cập nhật (update / 업데이트) không nhất thiết overwrite trạng thái (state / 상태) cũ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. WAL giải durability bằng write-ahead quy tắc (rule / 규칙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) là authority của phiên bản (version / 버전)

Bytes của phiên bản (version / 버전) có thể đã nằm trong buffer pool hoặc thậm chí dữ liệu (data / 데이터) page đã được ghi (write / 쓰기) xuống lưu trữ (storage / 저장소) trước lần ghi nhận (commit / 커밋). vật lý (physical / 물리적) existence không đồng nghĩa logical visibility.

Engine phải giữ enough siêu dữ liệu (metadata / 메타데이터) để phân biệt:

```text
uncommitted
committed
aborted
in-progress / unknown until recovery resolves
```

Bất biến (invariant / 불변식) là **khôi phục (recovery / 복구) và visibility lô-gic (logic / 논리) phải cùng hiểu giao dịch (transaction / 트랜잭션) authority**. Nếu crash xảy ra giữa vật lý (physical / 물리적) ghi (write / 쓰기) và lần ghi nhận (commit / 커밋) bản ghi (record / 레코드), page bytes không được tự nhiên biến thành committed row.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **7. WAL giải durability bằng write-ahead quy tắc (rule / 규칙)** tiếp nhận điểm tựa từ **6. giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) là authority của phiên bản (version / 버전)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. lần ghi nhận (commit / 커밋) acknowledgement có một ranh giới (boundary / 경계) cụ thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. WAL giải durability bằng write-ahead quy tắc (rule / 규칙)

**Write-Ahead Logging (WAL / 선행 기록 로그)** yêu cầu log thông tin (information / 정보) đủ để khôi phục (recovery / 복구) một page thay đổi (change / 변경) phải đạt durability cần thiết **trước** khi dependent dữ liệu (data / 데이터) page được phép persistent theo giao thức (protocol / 프로토콜).

Simplified:

```text
modify page in buffer pool
→ append WAL record
→ WAL reaches required durable position
→ dirty data page may be flushed later
```

Dữ liệu (data / 데이터) pages không cần flush mỗi lần ghi nhận (commit / 커밋). Sequential-ish log flush thường rẻ hơn random page flush và cho phép group lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **7. WAL giải durability bằng write-ahead quy tắc (rule / 규칙)** đã nêu tiêu chí phân biệt, còn **8. lần ghi nhận (commit / 커밋) acknowledgement có một ranh giới (boundary / 경계) cụ thể** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. Steal/no-steal và force/no-force quyết định khôi phục (recovery / 복구) burden** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. lần ghi nhận (commit / 커밋) acknowledgement có một ranh giới (boundary / 경계) cụ thể

Một giao dịch (transaction / 트랜잭션) có thể đi qua:

```text
business logic finished
→ commit record generated
→ WAL buffered
→ WAL flush requested
→ durable boundary reached
→ transaction marked/announced committed
→ client acknowledgement
```

Chính xác (exact / 정확한) chuỗi (sequence / 시퀀스) khác engine, nhưng bất biến (invariant / 불변식) tổng quát là:

> `COMMIT OK` không được mạnh hơn durability chính sách (policy / 정책) mà engine đã thực sự đạt.

Nếu chính sách (policy / 정책) là asynchronous/local-only, guarantee yếu hơn synchronous replicated durability. Từ “lần ghi nhận (commit / 커밋)” phải luôn đi cùng thất bại (failure / 실패) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **8. lần ghi nhận (commit / 커밋) acknowledgement có một ranh giới (boundary / 경계) cụ thể** đã nêu tiêu chí phân biệt, còn **9. Steal/no-steal và force/no-force quyết định khôi phục (recovery / 복구) burden** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. LSN nối logical log thứ tự (order / 순서) với vật lý (physical / 물리적) page trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Steal/no-steal và force/no-force quyết định khôi phục (recovery / 복구) burden

Nếu dirty page của uncommitted giao dịch (transaction / 트랜잭션) được phép ghi ra disk, chính sách (policy / 정책) là **steal** và khôi phục (recovery / 복구) cần cách undo/ignore effects chưa lần ghi nhận (commit / 커밋).

Nếu committed pages không bắt buộc flush ngay khi lần ghi nhận (commit / 커밋), chính sách (policy / 정책) là **no-force** và khôi phục (recovery / 복구) cần redo committed changes chưa tới dữ liệu (data / 데이터) tệp (file / 파일).

High-performance engines thường thích steal + no-force vì sử dụng buffer/lưu trữ (storage / 저장소) hiệu quả, đổi lại khôi phục (recovery / 복구) siêu dữ liệu (metadata / 메타데이터)/logging phức tạp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **10. LSN nối logical log thứ tự (order / 순서) với vật lý (physical / 물리적) page trạng thái (state / 상태)** tiếp nhận điểm tựa từ **9. Steal/no-steal và force/no-force quyết định khôi phục (recovery / 복구) burden** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. khôi phục (recovery / 복구) là một máy trạng thái (state machine / 상태 머신), không phải “tải (load / 로드) backup”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. LSN nối logical log thứ tự (order / 순서) với vật lý (physical / 물리적) page trạng thái (state / 상태)

**Log chuỗi (sequence / 시퀀스) Number (LSN)** tạo logical thứ tự (order / 순서) cho WAL records. dữ liệu (data / 데이터) page có thể lưu `pageLSN` cho biết nó đã phản ánh log tới position nào.

Bất biến (invariant / 불변식):

```text
durable WAL position phải đủ để giải thích durable page state
```

Khôi phục (recovery / 복구) có thể so pageLSN với log bản ghi (record / 레코드) LSN để tránh redo cập nhật (update / 업데이트) đã reflected.

Đây là liên kết (connection / 연결) trực tiếp sang filesystem/thiết bị (device / 장치) thứ tự (ordering / 순서): nếu lưu trữ (storage / 저장소) làm page durable nhưng log mà page phụ thuộc chưa thật sự persistent theo đặc tả hợp đồng (contract / 계약), WAL bất biến (invariant / 불변식) bị phá.

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **11. khôi phục (recovery / 복구) là một máy trạng thái (state machine / 상태 머신), không phải “tải (load / 로드) backup”** tiếp nhận điểm tựa từ **10. LSN nối logical log thứ tự (order / 순서) với vật lý (physical / 물리적) page trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Crash scenarios làm bất biến (invariant / 불변식) rõ hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. khôi phục (recovery / 복구) là một máy trạng thái (state machine / 상태 머신), không phải “tải (load / 로드) backup”

Nhiều WAL-based các hệ thống (systems / 시스템들) có conceptual phases tương tự:

```text
xác định transaction/page/log state cần quan tâm
→ redo effects cần tái tạo committed/known history
→ undo/ignore effects không được authority tùy architecture
→ rebuild runtime transaction metadata
```

Không phải mọi engine dùng ARIES hay cùng chính xác (exact / 정확한) thuật toán (algorithm / 알고리즘). mô hình tư duy (mental model / 사고 모델) quan trọng là khôi phục (recovery / 복구) **reconstructs a valid logical lịch sử (history / 이력) from durable bằng chứng (evidence / 증거)**, không đơn giản đọc dữ liệu (data / 데이터) tệp (file / 파일) như final truth.

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **12. Crash scenarios làm bất biến (invariant / 불변식) rõ hơn** tiếp nhận điểm tựa từ **11. khôi phục (recovery / 복구) là một máy trạng thái (state machine / 상태 머신), không phải “tải (load / 로드) backup”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Checkpoint giới hạn khôi phục (recovery / 복구) debt chứ không định nghĩa lần ghi nhận (commit / 커밋) truth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Crash scenarios làm bất biến (invariant / 불변식) rõ hơn

### WAL durable, dữ liệu (data / 데이터) page chưa flush

Đây là no-force trường hợp (case / 사례) bình thường. khôi phục (recovery / 복구) redo từ WAL.

### Dữ liệu (data / 데이터) page có bytes của uncommitted giao dịch (transaction / 트랜잭션)

Nếu engine cho steal, khôi phục (recovery / 복구)/visibility siêu dữ liệu (metadata / 메타데이터) phải bảo đảm bytes đó không trở thành committed lịch sử (history / 이력).

### Crash sau lần ghi nhận (commit / 커밋) log durable nhưng trước máy khách (client / 클라이언트) nhận phản hồi (response / 응답)

Sau restart giao dịch (transaction / 트랜잭션) có thể đã committed dù máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃)/liên kết (connection / 연결) drop. ứng dụng (application / 애플리케이션) thử lại (retry / 재시도) side tác động (effect / 효과) cần idempotency vì máy khách (client / 클라이언트) không biết final kết quả (outcome / 결과).

### Crash quanh checkpoint

Checkpoint siêu dữ liệu (metadata / 메타데이터) có thể incomplete theo moment crash; khôi phục (recovery / 복구) giao thức (protocol / 프로토콜) phải có ranh giới (boundary / 경계) để xác định checkpoint nào usable và WAL phạm vi (range / 범위) nào cần scan.

Những trường hợp (case / 사례) này cho thấy cơ sở dữ liệu (database / 데이터베이스) thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) nối trực tiếp với ứng dụng (application / 애플리케이션) thử lại (retry / 재시도) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **12. Crash scenarios làm bất biến (invariant / 불변식) rõ hơn** đã nêu tiêu chí phân biệt, còn **13. Checkpoint giới hạn khôi phục (recovery / 복구) debt chứ không định nghĩa lần ghi nhận (commit / 커밋) truth** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Group lần ghi nhận (commit / 커밋) đổi timing, không đổi durability bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Checkpoint giới hạn khôi phục (recovery / 복구) debt chứ không định nghĩa lần ghi nhận (commit / 커밋) truth

Checkpoint ghi enough siêu dữ liệu (metadata / 메타데이터) và/hoặc thúc đẩy dirty pages để khôi phục (recovery / 복구) không phải replay vô hạn WAL lịch sử (history / 이력).

**Fuzzy checkpoint** cho phép tải công việc (workload / 워크로드) tiếp tục, nên checkpoint không nhất thiết là toàn cục (global / 전역) instant nơi mọi dirty page sạch.

Sự đánh đổi (trade-off / 트레이드오프):

```text
checkpoint quá aggressive
→ foreground I/O pressure / latency spikes

checkpoint quá thưa
→ WAL retention + recovery time ↑
```

Đây là balancing giữa steady-state thông lượng (throughput / 처리량) và RTO.

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **13. Checkpoint giới hạn khôi phục (recovery / 복구) debt chứ không định nghĩa lần ghi nhận (commit / 커밋) truth** đã nêu tiêu chí phân biệt, còn **14. Group lần ghi nhận (commit / 커밋) đổi timing, không đổi durability bất biến (invariant / 불변식)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. Torn page và page-image chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Group lần ghi nhận (commit / 커밋) đổi timing, không đổi durability bất biến (invariant / 불변식)

Nếu mỗi giao dịch (transaction / 트랜잭션) tự flush WAL, lưu trữ (storage / 저장소) flush độ trễ (latency / 지연 시간) giới hạn thông lượng (throughput / 처리량). Group lần ghi nhận (commit / 커밋) gom nhiều lần ghi nhận (commit / 커밋) records vào một persistence thao tác (operation / 연산).

```text
T1 ─┐
T2 ─┼→ durable WAL flush → acknowledge group
T3 ─┘
```

Một giao dịch (transaction / 트랜잭션) có thể chờ thêm để batch, nhưng acknowledgement vẫn chỉ được phát sau ranh giới (boundary / 경계) chính sách (policy / 정책) yêu cầu. tối ưu hóa (optimization / 최적화) được phép đổi batching/timing, không được âm thầm làm yếu Đặc tả API (API contract / API 계약).

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **15. Torn page và page-image chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **14. Group lần ghi nhận (commit / 커밋) đổi timing, không đổi durability bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Vacuum/purge là garbage collection của phiên bản (version / 버전) lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Torn page và page-image chiến lược (strategy / 전략)

Lưu trữ (storage / 저장소) atomic-write granularity có thể nhỏ hơn cơ sở dữ liệu (database / 데이터베이스) page. Power mất mát (loss / 손실) giữa page ghi (write / 쓰기) có thể tạo page một phần old, một phần new.

Checksum detect corruption nhưng khôi phục (recovery / 복구) cần cơ chế (mechanism / 메커니즘) bổ sung: WAL redo, full-page ảnh (image / 이미지), double-write, COW page hoặc chiến lược (strategy / 전략) khác tùy engine.

Bất biến (invariant / 불변식) là **khôi phục (recovery / 복구) không được tin một partial vật lý (physical / 물리적) ghi (write / 쓰기) như logical page hoàn chỉnh**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **16. Vacuum/purge là garbage collection của phiên bản (version / 버전) lịch sử (history / 이력)** tiếp nhận điểm tựa từ **15. Torn page và page-image chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Replica làm vòng đời (lifecycle / 생명주기) kéo dài sang phân tán (distributed / 분산) trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Vacuum/purge là garbage collection của phiên bản (version / 버전) lịch sử (history / 이력)

Old phiên bản (version / 버전) không thể xóa chỉ vì có phiên bản (version / 버전) mới. Engine cần biết không còn snapshot hợp lệ nào có thể nhìn thấy old trạng thái (state / 상태).

Reclamation horizon có thể bị kéo lùi bởi:

```text
long-running transaction
idle transaction holding snapshot
replica/read-only consumer cần old log/history
backup/export snapshot
```

Hậu quả: bảng (table / 테이블)/chỉ mục (index / 인덱스) bloat, undo/version-store growth, more I/O/bộ nhớ đệm (cache / 캐시) pressure và đôi khi transaction-ID/phiên bản (version / 버전) siêu dữ liệu (metadata / 메타데이터) pressure tùy engine.

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **16. Vacuum/purge là garbage collection của phiên bản (version / 버전) lịch sử (history / 이력)** xác định đầu vào; **17. Replica làm vòng đời (lifecycle / 생명주기) kéo dài sang phân tán (distributed / 분산) trạng thái (state / 상태)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **18. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) theo subsystem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Replica làm vòng đời (lifecycle / 생명주기) kéo dài sang phân tán (distributed / 분산) trạng thái (state / 상태)

Một replica có thể nhận WAL/log nhưng chưa apply; đã persist nhưng chưa visible; hoặc lag phía sau leader.

Do đó cần tách positions:

```text
leader generated
→ sent
→ replica received
→ replica persisted
→ replica replayed/applied
→ read visibility reached
```

Read from replica có consistency đặc tả hợp đồng (contract / 계약) phụ thuộc position đó. Failover lại phụ thuộc replica nào có authority/lịch sử (history / 이력) đủ để trở thành leader.

Đọc [multi-region replication và failover](../../06_networks_distributed_systems/advanced/05_multi_region_replication_and_geo_distributed_tradeoffs.md).

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **17. Replica làm vòng đời (lifecycle / 생명주기) kéo dài sang phân tán (distributed / 분산) trạng thái (state / 상태)** xác định đầu vào; **18. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) theo subsystem** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. bằng chứng vận hành (production evidence / 운영 증거): quan sát lịch sử (history / 이력) ở nhiều representations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) theo subsystem

High ghi (write / 쓰기) tỷ lệ (rate / 비율) tăng WAL bytes, dirty pages, checkpoint debt và vacuum công việc (work / 작업). Long snapshots tăng retained lịch sử (history / 이력). Random read miss tăng buffer-pool I/O. Replica lag kéo dài retention hoặc làm failover/read freshness xấu.

Các subsystem tạo phản hồi (feedback / 피드백):

```text
write load ↑
→ dirty/WAL ↑
→ checkpoint/storage pressure ↑
→ commit/read latency ↑
→ transaction lifetime ↑
→ MVCC horizon older
→ cleanup debt ↑
```

Vì vậy nguyên nhân gốc (root cause / 근본 원인) có thể không nằm ở truy vấn (query / 쿼리) văn bản (text / 텍스트) đang chậm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **18. hiệu năng (performance / 성능) pressure thay đổi hành vi (behavior / 동작) theo subsystem** nêu điều cần giải thích; **19. bằng chứng vận hành (production evidence / 운영 증거): quan sát lịch sử (history / 이력) ở nhiều representations** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. bằng chứng vận hành (production evidence / 운영 증거): quan sát lịch sử (history / 이력) ở nhiều representations

Bằng chứng (evidence / 증거) generic nên gồm:

```text
Transaction/MVCC:
- active/long transaction age
- snapshot horizon / old-version retention
- abort/conflict rate
- table/index/undo/version-store bloat

WAL/recovery:
- WAL generation rate
- flush latency / group size
- checkpoint duration/frequency
- recovery/replay position

Buffer/storage:
- dirty-page count
- buffer hit/miss và eviction pressure
- foreground/background I/O latency

Replication:
- send/receive/persist/apply positions
- replication lag
- failover term/epoch/leader timeline
```

Chỉ số (metric / 지표) names khác DBMS; mô hình tư duy (mental model / 사고 모델) là đo **visibility horizon + durable-log frontier + dirty-page frontier + replica frontier**.

> **Chuyển mạch:** Trong **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **19. bằng chứng vận hành (production evidence / 운영 증거): quan sát lịch sử (history / 이력) ở nhiều representations** nêu điều cần giải thích; **20. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?

Nếu reader thấy stale trạng thái (state / 상태), kiểm tra snapshot/isolation/replica position trước khi nghi disk. Nếu committed dữ liệu (data / 데이터) mất sau crash, kiểm tra WAL acknowledgment và lưu trữ (storage / 저장소) durability đường dẫn (path / 경로). Nếu DB phình dù traffic nhỏ, kiểm tra old snapshot horizon. Nếu p99 lần ghi nhận (commit / 커밋) spike, kiểm tra WAL flush/checkpoint/lưu trữ (storage / 저장소) hàng đợi (queue / 큐) chứ không chỉ CPU.

> **Chuyển mạch:** Ở chặng này của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **21. Mô hình tư duy** gom các mảnh từ **20. lớp trừu tượng (abstraction / 추상화) nào thực sự quyết định hành vi (behavior / 동작)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Mô hình tư duy

> MVCC quyết định **ai nhìn thấy phiên bản (version / 버전) nào**; giao dịch (transaction / 트랜잭션) trạng thái (state / 상태) quyết định **phiên bản (version / 버전) nào có authority**; WAL/khôi phục (recovery / 복구) quyết định **lịch sử (history / 이력) nào sống sót crash**; checkpoint giới hạn **khôi phục (recovery / 복구) debt**; vacuum/purge quyết định **khi nào lịch sử (history / 이력) cũ có thể bị quên**; replication kéo cùng lịch sử (history / 이력) qua nhiều nodes. **tính đúng đắn (correctness / 정확성) đến từ việc mọi biểu diễn (representation / 표현) tôn trọng cùng giao dịch (transaction / 트랜잭션) authority, còn hiệu năng (performance / 성능) đến từ cách hệ thống (system / 시스템) trì hoãn, batch và reclaim công việc (work / 작업) mà không phá bất biến (invariant / 불변식).**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **MVCC, visibility, WAL và khôi phục (recovery / 복구) internals**, **Kết nối** gom các mảnh từ **21. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Ôn [Transactions/ACID](../../basic/05_data_databases/02_transactions_acid_and_concurrency_control.md), [storage/WAL foundation](../../basic/05_data_databases/04_storage_logs_recovery_and_durability.md), đọc [buffer pool](./04_buffer_pool_replacement_and_dirty_page_management.md), [filesystem crash consistency](../../03_operating_systems/advanced/04_filesystem_crash_consistency_journaling_and_cow.md), [distributed transactions](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [durability path xuyên tầng](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
