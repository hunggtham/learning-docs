# Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Atomicity** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Consistency trong ACID** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) giải quyết một vấn đề sâu: nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) thường gồm nhiều reads/writes, trong khi crash hoặc concurrent transactions có thể xảy ra giữa bất kỳ bước nào. Ta muốn một higher-level chuyển tiếp trạng thái (state transition / 상태 전이) với guarantees rõ ràng thay vì các writes độc lập.

## Atomicity

Atomicity nghĩa giao dịch (transaction / 트랜잭션) effects được coi như all-or-nothing theo đặc tả hợp đồng (contract / 계약). Transfer 100 từ A sang B không được debit A rồi crash trước credit B mà để trạng thái (state / 상태) nửa chừng.

Atomicity thường dựa log/khôi phục (recovery / 복구) hoặc sao chép khi ghi (copy-on-write / 쓰기 시 복사) techniques, không phải hardware thực hiện mọi writes cùng một nanosecond.

> **Chuyển mạch:** Atomicity gom thay đổi thành một đơn vị; consistency giữ invariant của dữ liệu, rồi isolation quyết định các transaction đồng thời nhìn và ảnh hưởng nhau ở mức nào.

## Consistency trong ACID

Consistency ở ACID thường nghĩa giao dịch (transaction / 트랜잭션) đưa cơ sở dữ liệu (database / 데이터베이스) từ trạng thái (state / 상태) thỏa các ràng buộc (constraints / 제약조건들)/invariants sang trạng thái (state / 상태) thỏa các ràng buộc (constraints / 제약조건들) nếu giao dịch (transaction / 트랜잭션) lô-gic (logic / 논리) đúng. Nó khác “consistency” trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들)/CAP, nơi term nói về views/thứ tự (ordering / 순서) giữa replicas.

DB không tự biết mọi nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식). Nếu bất biến (invariant / 불변식) không encoded hoặc giao dịch (transaction / 트랜잭션) mã (code / 코드) sai, ACID không cứu lô-gic (logic / 논리).

> **Chuyển mạch:** Ở chặng này của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Isolation** tiếp nhận điểm tựa từ **Consistency trong ACID** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Durability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Isolation

Isolation điều khiển concurrent transactions được phép quan sát nhau đến mức nào. Nếu serializable, kết quả (outcome / 결과) tương đương một serial thứ tự (ordering / 순서) nào đó. Weaker isolation tăng tính đồng thời (concurrency / 동시성) nhưng cho anomalies.

Dirty read: đọc uncommitted dữ liệu (data / 데이터). Non-repeatable read: cùng row đọc hai lần cho values khác do lần ghi nhận (commit / 커밋) khác. Phantom: predicate truy vấn (query / 쿼리) trả thêm/bớt rows. ghi (write / 쓰기) skew có thể xảy ra dưới snapshot isolation khi two transactions đọc dùng chung (common / 공통) snapshot rồi cập nhật (update / 업데이트) disjoint rows, phá cross-row bất biến (invariant / 불변식).

Isolation-level names trong SQL standards và DB products có hiện thực (implementation / 구현) differences; cần đọc engine docs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Durability** tiếp nhận điểm tựa từ **Isolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Locks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Durability

Lần ghi nhận (commit / 커밋) success hứa effects survive defined failures. WAL/redo logs, fsync/thiết bị (device / 장치) guarantees và replication chính sách (policy / 정책) quyết định durability strength. Async replication có thể lose acknowledged dữ liệu (data / 데이터) khi primary dies trước replica receive, tùy hệ thống (system / 시스템).

> **Chuyển mạch:** Trong **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Locks** tiếp nhận điểm tựa từ **Durability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MVCC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Locks

Two-phase locking family dùng dùng chung (shared / 공유)/exclusive locks để điều khiển (control / 제어) conflicts. khóa (lock / 잠금) granularity row/page/bảng (table / 테이블) ảnh hưởng overhead/contention. Predicate/phạm vi (range / 범위) locks cần để bảo vệ phantoms ở serializable schemes.

Locks có thể deadlock; DB detect wait-for cycles và abort một giao dịch (transaction / 트랜잭션). ứng dụng (application / 애플리케이션) phải sẵn sàng thử lại (retry / 재시도) giao dịch (transaction / 트랜잭션) bị deadlock victim.

> **Chuyển mạch:** Ở chặng này của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **MVCC** tiếp nhận điểm tựa từ **Locks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Optimistic tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MVCC

Multi-Version tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) giữ multiple row versions để readers và writers ít khối (block / 블록) nhau. giao dịch (transaction / 트랜잭션) đọc snapshot theo visibility rules; cập nhật (update / 업데이트) tạo new phiên bản (version / 버전).

MVCC không “loại locks hoàn toàn”. Writes/các ràng buộc (constraints / 제약조건들)/siêu dữ liệu (metadata / 메타데이터) vẫn cần coordination, và old versions cần vacuum/garbage collection.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Optimistic tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **MVCC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Serializability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimistic tính đồng thời (concurrency / 동시성)

Optimistic scheme cho công việc (work / 작업) tiến hành rồi validate phiên bản (version / 버전)/timestamp trước lần ghi nhận (commit / 커밋). Nếu xung đột (conflict / 충돌), thử lại (retry / 재시도). Hợp khi conflicts hiếm; khi hot contention cao, retries có thể waste công việc (work / 작업).

Ứng dụng (application / 애플리케이션) mẫu (pattern / 패턴) `UPDATE ... WHERE id=? AND version=?` là simple compare-and-swap at DB mức (level / 수준).

> **Chuyển mạch:** Trong **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Serializability** tiếp nhận điểm tựa từ **Optimistic tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Serializability

Serializability là tính đúng đắn (correctness / 정확성) criterion: concurrent thực thi (execution / 실행) equivalent về tác động (effect / 효과) với một serial schedule. xung đột (conflict / 충돌) serializability có thể analyze precedence đồ thị (graph / 그래프); cycle chỉ non-serializable schedule.

Serializable Snapshot Isolation dùng phụ thuộc (dependency / 의존성) tracking để abort dangerous structures thay vì khóa (lock / 잠금) mọi read theo classic 2PL.

> **Chuyển mạch:** Ở chặng này của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Serializability** đã nêu tiêu chí phân biệt, còn **Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)

Giao dịch (transaction / 트랜잭션) quá lớn giữ versions/locks lâu, tăng contention và khôi phục (recovery / 복구) chi phí (cost / 비용). Quá nhỏ làm nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) split. ranh giới (boundary / 경계) nên match atomic bất biến (invariant / 불변식), không phải mỗi repository phương thức (method / 메서드) mặc định.

Remote API lời gọi (call / 호출) bên trong DB giao dịch (transaction / 트랜잭션) nguy hiểm vì độ trễ (latency / 지연 시간)/thất bại (failure / 실패) kéo dài locks. Saga/outbox patterns giải cross-service workflows với weaker atomicity và compensations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> giao dịch (transaction / 트랜잭션) là **một chuyển tiếp trạng thái (state transition / 상태 전이) có đặc tả hợp đồng (contract / 계약) dưới tính đồng thời (concurrency / 동시성) và crash**. ACID không phải bốn checkbox độc lập; hiện thực (implementation / 구현) phối hợp isolation + logging + các ràng buộc (constraints / 제약조건들) để giữ invariants.

> **Chuyển mạch:** Trong **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“ACID consistency = CAP consistency.”** Hai khái niệm khác ngữ cảnh (context / 맥락).

**“MVCC nghĩa không có blocking.”** Writes, DDL, các ràng buộc (constraints / 제약조건들) và cleanup vẫn có conflicts.

**“READ COMMITTED đủ vì không dirty read.”** Cross-row invariants và lost-update/write-skew patterns vẫn cần rà soát (review / 검토).

> **Chuyển mạch:** Ở chặng này của **Transactions, ACID và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Concurrency/deadlock](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) là same family bài toán (problem / 문제) ở dùng chung (shared / 공유) bộ nhớ (memory / 메모리). [WAL/recovery](./04_storage_logs_recovery_and_durability.md) hiện thực atomicity/durability. Cross-node transactions gặp [distributed consistency/consensus](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
