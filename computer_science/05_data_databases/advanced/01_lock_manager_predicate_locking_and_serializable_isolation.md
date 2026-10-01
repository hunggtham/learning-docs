# Khóa (lock / 잠금) manager, predicate locking và serializable isolation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Khóa (lock / 잠금) manager là một subsystem riêng** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Dùng chung (shared / 공유) và exclusive chỉ là khởi đầu** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

MVCC giúp nhiều giao dịch (transaction / 트랜잭션) đọc/ghi đồng thời, nhưng isolation mạnh vẫn cần cơ chế phát hiện hoặc ngăn các thực thi (execution / 실행) tương đương sai. Advanced cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성) không chỉ là “row khóa (lock / 잠금)”. Ta cần hiểu **khóa (lock / 잠금) manager, khóa (lock / 잠금) tính tương thích (compatibility / 호환성), deadlock, predicate/phạm vi (range / 범위) protection và serializability**.

## Khóa (lock / 잠금) manager là một subsystem riêng

Cơ sở dữ liệu (database / 데이터베이스) duy trì siêu dữ liệu (metadata / 메타데이터) về tài nguyên (resource / 자원) nào đang bị khóa (lock / 잠금), giao dịch (transaction / 트랜잭션) nào sở hữu khóa (lock / 잠금) và giao dịch (transaction / 트랜잭션) nào đang chờ.

Tài nguyên (resource / 자원) có thể là row, key, page, bảng (table / 테이블), chỉ mục (index / 인덱스) phạm vi (range / 범위) hoặc logical predicate tùy engine.

Khóa (lock / 잠금) manager phải trả lời nhanh:

```text
request lock -> compatible?
             -> grant ngay
             -> hoặc enqueue waiter
```

Nó cũng phải bản phát hành (release / 릴리스) khóa (lock / 잠금) khi lần ghi nhận (commit / 커밋)/quay lui (rollback / 롤백) và xử lý deadlock.

> **Chuyển mạch:** Trong **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Dùng chung (shared / 공유) và exclusive chỉ là khởi đầu** tiếp nhận điểm tựa từ **Khóa (lock / 잠금) manager là một subsystem riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Two-phase locking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) và exclusive chỉ là khởi đầu

Dùng chung (shared / 공유) khóa (lock / 잠금) cho nhiều readers cùng tồn tại. Exclusive khóa (lock / 잠금) xung đột với reader/writer khác.

Môi trường vận hành (production / 운영 환경) DB còn có intent locks ở hierarchy bảng (table / 테이블)/page/row để tránh phải scan hàng triệu child locks khi muốn khóa (lock / 잠금) cấp cao hơn.

Ví dụ `IX` trên bảng (table / 테이블) nói rằng giao dịch (transaction / 트랜잭션) có hoặc sẽ có exclusive khóa (lock / 잠금) ở một số descendants; nó giúp tính tương thích (compatibility / 호환성) check cấp bảng (table / 테이블) có meaning.

> **Chuyển mạch:** Ở chặng này của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Two-phase locking** tiếp nhận điểm tựa từ **Dùng chung (shared / 공유) và exclusive chỉ là khởi đầu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deadlock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Two-phase locking

**2PL** về conceptual có growing phase acquire locks và shrinking phase bản phát hành (release / 릴리스) locks. Strict 2PL thường giữ ghi (write / 쓰기) locks tới lần ghi nhận (commit / 커밋)/abort, giúp tránh dirty ghi (write / 쓰기)/read và làm khôi phục (recovery / 복구) lập luận (reasoning / 추론) dễ hơn.

Serializable schedule có thể đạt bằng locking thích hợp, nhưng tính đồng thời (concurrency / 동시성) giảm khi khóa (lock / 잠금) phạm vi (scope / 범위) lớn hoặc giao dịch (transaction / 트랜잭션) dài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Deadlock** tiếp nhận điểm tựa từ **Two-phase locking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Row khóa (lock / 잠금) chưa đủ chống phantom** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deadlock

Giao dịch (transaction / 트랜잭션) A giữ X và chờ Y; B giữ Y và chờ X. Nếu chỉ chờ, cả hai đứng mãi.

DB có thể dùng **wait-for đồ thị (graph / 그래프)** và cycle detection, hoặc hết thời gian chờ (timeout / 타임아웃)/deadlock prevention schemes. Khi phát hiện cycle, engine chọn victim quay lui (rollback / 롤백).

Ứng dụng (application / 애플리케이션) phải coi deadlock lỗi (error / 오류) là expected tính đồng thời (concurrency / 동시성) kết quả (outcome / 결과) có thể thử lại (retry / 재시도), không phải “DB bị lỗi”.

> **Chuyển mạch:** Trong **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Row khóa (lock / 잠금) chưa đủ chống phantom** tiếp nhận điểm tựa từ **Deadlock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Predicate khóa (lock / 잠금) và index-range khóa (lock / 잠금)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Row khóa (lock / 잠금) chưa đủ chống phantom

Giả sử giao dịch (transaction / 트랜잭션) đọc:

```sql
SELECT * FROM orders WHERE amount > 1000;
```

Nó khóa (lock / 잠금) tất cả rows hiện có thỏa điều kiện. giao dịch (transaction / 트랜잭션) khác insert một row mới `amount=5000`. Khi truy vấn (query / 쿼리) chạy lại, row “phantom” xuất hiện dù không row cũ nào bị sửa.

Để serializable theo locking, cơ sở dữ liệu (database / 데이터베이스) cần bảo vệ **predicate/key phạm vi (range / 범위)**, không chỉ rows đã materialize.

> **Chuyển mạch:** Ở chặng này của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Predicate khóa (lock / 잠금) và index-range khóa (lock / 잠금)** tiếp nhận điểm tựa từ **Row khóa (lock / 잠금) chưa đủ chống phantom** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MVCC + Serializable không có một hiện thực (implementation / 구현) duy nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predicate khóa (lock / 잠금) và index-range khóa (lock / 잠금)

Predicate khóa (lock / 잠금) lý tưởng bảo vệ tập “mọi row thỏa `amount > 1000`”. Implement trực tiếp predicate tổng quát rất đắt.

Nhiều engine dùng index-range/gap/next-key locking khi truy vấn (query / 쿼리) có chỉ mục (index / 인덱스) phù hợp. khóa (lock / 잠금) một interval trong B+cây (tree / 트리) keyspace ngăn insert vào phạm vi (range / 범위) có thể thay kết quả (result / 결과).

Do đó chỉ mục (index / 인덱스) thiết kế (design / 설계) có thể ảnh hưởng không chỉ hiệu năng (performance / 성능) mà cả granularity tính đồng thời (concurrency / 동시성) điều khiển (control / 제어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **MVCC + Serializable không có một hiện thực (implementation / 구현) duy nhất** tiếp nhận điểm tựa từ **Predicate khóa (lock / 잠금) và index-range khóa (lock / 잠금)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ghi (write / 쓰기) skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MVCC + Serializable không có một hiện thực (implementation / 구현) duy nhất

Một số engine dùng locking serializable; một số dùng Serializable Snapshot Isolation (SSI) phát hiện dangerous phụ thuộc (dependency / 의존성) patterns trên snapshot thực thi (execution / 실행); có hệ dùng optimistic kiểm tra hợp lệ (validation / 검증).

“Isolation mức (level / 수준) = Serializable” là ngữ nghĩa (semantic / 의미적) goal. cơ chế (mechanism / 메커니즘) bên dưới có thể rất khác và dạng thất bại (failure mode / 실패 모드)/thử lại (retry / 재시도) hành vi (behavior / 동작) cũng khác.

> **Chuyển mạch:** Trong **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Ghi (write / 쓰기) skew** tiếp nhận điểm tựa từ **MVCC + Serializable không có một hiện thực (implementation / 구현) duy nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Long giao dịch (transaction / 트랜잭션) là tính đồng thời (concurrency / 동시성) hazard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ghi (write / 쓰기) skew

Hai doctors cùng kiểm tra “ít nhất một doctor đang on-call”. Mỗi giao dịch (transaction / 트랜잭션) thấy hai người on-call và tắt chính mình. Hai writes ở rows khác nhau nên không write-write xung đột (conflict / 충돌), nhưng bất biến (invariant / 불변식) cuối cùng bị phá.

Snapshot isolation có thể cho phép ghi (write / 쓰기) skew. Serializable cần nhận ra phụ thuộc (dependency / 의존성) logical giữa reads và writes hoặc dùng predicate protection.

Đây là lý do chỉ nhìn row ghi (write / 쓰기) xung đột (conflict / 충돌) không đủ lập luận (reasoning / 추론) nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식).

> **Chuyển mạch:** Ở chặng này của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Long giao dịch (transaction / 트랜잭션) là tính đồng thời (concurrency / 동시성) hazard** tiếp nhận điểm tựa từ **Ghi (write / 쓰기) skew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khóa (lock / 잠금) escalation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Long giao dịch (transaction / 트랜잭션) là tính đồng thời (concurrency / 동시성) hazard

Giao dịch (transaction / 트랜잭션) giữ locks lâu hoặc giữ snapshot quá cũ làm contention/phiên bản (version / 버전) retention tăng. Một API yêu cầu (request / 요청) mở giao dịch (transaction / 트랜잭션) rồi gọi bên ngoài (external / 외부) dịch vụ (service / 서비스) trong 5 giây có thể làm DB tính đồng thời (concurrency / 동시성) tệ mạnh.

Giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) nên ôm đúng atomic chuyển tiếp trạng thái (state transition / 상태 전이) cần thiết, không phải toàn workflow nghiệp vụ (business / 비즈니스) nếu không cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Khóa (lock / 잠금) escalation** tiếp nhận điểm tựa từ **Long giao dịch (transaction / 트랜잭션) là tính đồng thời (concurrency / 동시성) hazard** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khóa (lock / 잠금) escalation

Quá nhiều row locks tốn bộ nhớ (memory / 메모리)/management overhead. Engine có thể escalate thành page/bảng (table / 테이블) khóa (lock / 잠금). Điều này giảm khóa (lock / 잠금) siêu dữ liệu (metadata / 메타데이터) nhưng tăng contention bất ngờ.

Một truy vấn (query / 쿼리) cập nhật (update / 업데이트) nhiều rows có thể vì vậy ảnh hưởng concurrent requests rộng hơn nhà phát triển (developer / 개발자) nghĩ.

> **Chuyển mạch:** Trong **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Khóa (lock / 잠금) escalation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성)

Khi hệ thống chậm, cần phân biệt CPU/I/O bottleneck với khóa (lock / 잠금) wait.

Thông tin hữu ích: blocking session, khóa (lock / 잠금) chế độ (mode / 모드)/tài nguyên (resource / 자원), wait duration, giao dịch (transaction / 트랜잭션) age, deadlock đồ thị (graph / 그래프) và SQL/plan gây khóa (lock / 잠금) footprint.

“truy vấn (query / 쿼리) chạy lâu” đôi khi thực tế là truy vấn (query / 쿼리) chạy 10ms nhưng chờ khóa (lock / 잠금) 4s.

> **Chuyển mạch:** Ở chặng này của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khả năng quan sát (observability / 관측 가능성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Serializable isolation bảo vệ **lịch sử lô-gic (logic / 논리) của transactions**, không chỉ từng row. khóa (lock / 잠금) manager quản lý quyền truy cập; predicate/phạm vi (range / 범위) locking bảo vệ những rows chưa tồn tại; deadlock/thử lại (retry / 재시도) là một phần tự nhiên của tính đồng thời (concurrency / 동시성) điều khiển (control / 제어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“MVCC nghĩa không cần khóa (lock / 잠금).”** Writers, lược đồ (schema / 스키마) changes và serializable mechanisms vẫn có thể cần khóa (lock / 잠금)/latch.

**“Row khóa (lock / 잠금) ngăn phantom.”** Không nếu new row có thể xuất hiện trong predicate phạm vi (range / 범위).

**“Deadlock là bug của DB.”** Nó là possible kết quả (outcome / 결과) của concurrent khóa (lock / 잠금) acquisition; thiết kế (design / 설계) giao dịch (transaction / 트랜잭션) thứ tự (order / 순서) và thử lại (retry / 재시도) chiến lược (strategy / 전략) mới là phần ứng dụng (application / 애플리케이션) cần xử lý.

> **Chuyển mạch:** Trong **Khóa (lock / 잠금) manager, predicate locking và serializable isolation**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Tiếp theo đọc [B+Tree page layout và latch coupling](./02_bplus_tree_pages_splits_merges_and_latch_coupling.md). Với Oracle/SQL các hệ thống (systems / 시스템들), nên kết hợp thực thi (execution / 실행) plan, chỉ mục (index / 인덱스) phạm vi (range / 범위) và giao dịch (transaction / 트랜잭션) phạm vi (scope / 범위) để hiểu khóa (lock / 잠금) footprint thực tế.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
