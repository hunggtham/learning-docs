# Môn 3 — 데이터베이스 구축: Deep Dive 2026

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. 데이터베이스 기본 개념** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. 논리 데이터베이스 설계 — Logical cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này dùng README làm bản đồ owner của database construction depth, rồi nối concept, design, SQL, storage và security.

> Môn 3 không nên học bằng cách thuộc lệnh SQL rời rạc. Cần hiểu toàn bộ chuỗi: **mô hình dữ liệu (data model / 데이터 모델) → key/phụ thuộc (dependency / 의존성) → normalization → vật lý (physical / 물리적) lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) → SQL → giao dịch (transaction / 트랜잭션)/tính đồng thời (concurrency / 동시성)/khôi phục (recovery / 복구) → di chuyển (migration / 마이그레이션)**.

## 1. 데이터베이스 기본 개념

Cơ sở dữ liệu (database / 데이터베이스) là tập dữ liệu có cấu trúc được quản lý để nhiều ứng dụng/người dùng (user / 사용자) có thể truy cập nhất quán. DBMS cung cấp definition, lưu trữ (storage / 저장소), truy vấn (query / 쿼리), giao dịch (transaction / 트랜잭션), tính đồng thời (concurrency / 동시성), khôi phục (recovery / 복구), bảo mật (security / 보안) và integrity.

### 1.1 Three-Schema kiến trúc (architecture / 아키텍처)

Bên ngoài (external / 외부) lược đồ (schema / 스키마) — 외부 스키마 — view của từng người dùng (user / 사용자)/ứng dụng (application / 애플리케이션). Conceptual lược đồ (schema / 스키마) — 개념 스키마 — mô hình lô-gic (logic / 논리) tổng thể của toàn cơ sở dữ liệu (database / 데이터베이스). nội bộ (internal / 내부) lược đồ (schema / 스키마) — 내부 스키마 — cách dữ liệu (data / 데이터) được lưu vật lý.

Dữ liệu (data / 데이터) independence được chia thành logical dữ liệu (data / 데이터) independence và vật lý (physical / 물리적) dữ liệu (data / 데이터) independence. vật lý (physical / 물리적) independence nghĩa thay đổi lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) mà ứng dụng (application / 애플리케이션) lô-gic (logic / 논리) không phải đổi. Logical independence khó hơn: thay đổi conceptual lược đồ (schema / 스키마) nhưng bên ngoài (external / 외부) view/ứng dụng (application / 애플리케이션) ít bị ảnh hưởng.

### 1.2 mô hình dữ liệu (data model / 데이터 모델)

Mô hình dữ liệu (data model / 데이터 모델) gồm cấu trúc (structure / 구조), thao tác (operation / 연산) và ràng buộc (constraint / 제약조건). Các mô hình lịch sử như hierarchical, mạng (network / 네트워크), relational có cách biểu diễn quan hệ (relation / 관계) khác nhau. Relational mô hình (model / 모델) biểu diễn dữ liệu (data / 데이터) bằng quan hệ (relation / 관계)/bảng (table / 테이블) và dựa mạnh vào relational algebra/set lý thuyết (theory / 이론).

> **Chuyển mạch:** Trong **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **1. 데이터베이스 기본 개념** nêu điều cần giải thích; **2. 논리 데이터베이스 설계 — Logical cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Relational Algebra** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. 논리 데이터베이스 설계 — Logical cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)

### 2.1 thực thể (entity / 엔터티), Attribute, Relationship

Thực thể (entity / 엔터티) là đối tượng cần quản lý. Attribute là đặc tính. Relationship mô tả liên hệ giữa thực thể (entity / 엔터티). Cardinality thường gặp: 1:1, 1:N, M:N. Participation có thể mandatory/optional tùy mô hình (model / 모델).

M:N trong relational hiện thực (implementation / 구현) thường cần associative/junction bảng (table / 테이블) để tách thành hai quan hệ 1:N.

### 2.2 Keys

Super Key — 슈퍼키 — tập attribute xác định duy nhất tuple, có thể thừa. Candidate Key — 후보키 — super key tối thiểu. Primary Key — 기본키 — candidate key được chọn chính. Alternate Key — 대체키 — candidate key còn lại. Foreign Key — 외래키 — attribute tham chiếu key của quan hệ (relation / 관계) khác. Composite Key — 복합키 — key gồm nhiều attribute.

Hai thuộc tính (property / 속성) cốt lõi của candidate key: uniqueness và minimality.

### 2.3 Integrity các ràng buộc (constraints / 제약조건들)

Thực thể (entity / 엔터티) Integrity: primary key không NULL. Referential Integrity: foreign key phải tham chiếu mục tiêu (target / 대상) hợp lệ hoặc NULL nếu lược đồ (schema / 스키마) cho phép. lĩnh vực (domain / 도메인) Integrity: giá trị (value / 값) nằm trong lĩnh vực (domain / 도메인)/kiểu (type / 타입)/phạm vi (range / 범위) hợp lệ.

Khi delete parent row, hành vi (behavior / 동작) có thể RESTRICT/NO hành động (action / 동작), CASCADE, SET NULL hoặc SET DEFAULT tùy DBMS/lược đồ (schema / 스키마).

> **Chuyển mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **2. 논리 데이터베이스 설계 — Logical cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** nêu điều cần giải thích; **3. Relational Algebra** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Functional phụ thuộc (dependency / 의존성) và Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Relational Algebra

Relational algebra là nền tảng thao tác quan hệ (relation / 관계). Các thao tác (operation / 연산) cơ bản:

Selection `σ` chọn row theo predicate. Projection `π` chọn column. Union hợp quan hệ (relation / 관계) compatible. Difference lấy tuple ở A không có trong B. Cartesian sản phẩm (product / 제품) ghép mọi tuple A với mọi tuple B. phép nối (join / 조인) kết hợp tuple liên quan theo điều kiện (condition / 조건). Division thường dùng cho truy vấn (query / 쿼리) dạng “đối tượng thỏa **tất cả** điều kiện trong một tập”.

Bẫy: Selection liên quan **row**, Projection liên quan **column**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **4. Functional phụ thuộc (dependency / 의존성) và Normalization** tiếp nhận điểm tựa từ **3. Relational Algebra** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. 물리 데이터베이스 설계 — vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Functional phụ thuộc (dependency / 의존성) và Normalization

### 4.1 Functional phụ thuộc (dependency / 의존성)

`X → Y` nghĩa nếu hai tuple có cùng X thì phải có cùng Y. X functionally determines Y.

Full Functional phụ thuộc (dependency / 의존성) nghĩa Y phụ thuộc toàn bộ composite key, không phụ thuộc chỉ một phần. Partial phụ thuộc (dependency / 의존성) là phụ thuộc vào một phần composite key. Transitive phụ thuộc (dependency / 의존성) xảy ra khi key → A và A → B, khiến B phụ thuộc gián tiếp key qua non-key attribute.

### 4.2 Anomaly

Unnormalized/redundant thiết kế (design / 설계) có thể gây:

- Insert Anomaly: không thể insert một fact nếu thiếu fact khác không liên quan.
- cập nhật (update / 업데이트) Anomaly: cùng fact lặp nhiều row, cập nhật (update / 업데이트) không đồng bộ.
- Delete Anomaly: xóa một row vô tình mất fact khác.

Normalization giảm anomaly bằng decomposition có lý do.

### 4.3 1NF

1NF yêu cầu attribute giá trị (value / 값) mang tính atomic theo relational thiết kế (design / 설계) đang xét; không có repeating group/danh sách (list / 목록) đa trị trong một cell theo cách thiết kế chuẩn.

### 4.4 2NF

2NF = 1NF + không có partial phụ thuộc (dependency / 의존성) của non-prime attribute lên một phần candidate key.

2NF đặc biệt đáng chú ý khi key là composite. Nếu primary/candidate key chỉ một attribute thì partial phụ thuộc (dependency / 의존성) theo key đó không xảy ra.

### 4.5 3NF

3NF loại transitive phụ thuộc (dependency / 의존성) không phù hợp giữa key và non-key attribute. Một formulation chính xác hơn với FD `X → A`: quan hệ (relation / 관계) ở 3NF nếu X là superkey hoặc A là prime attribute, sau khi đã ở mức normalization phù hợp.

### 4.6 BCNF

BCNF mạnh hơn 3NF: với mọi non-trivial FD `X → Y`, X phải là superkey.

Một quan hệ (relation / 관계) có thể đạt 3NF nhưng chưa BCNF khi determinant không phải superkey nhưng dependent là prime attribute.

### 4.7 4NF và 5NF

4NF xử lý non-trivial multivalued phụ thuộc (dependency / 의존성) khi determinant không phải superkey. 5NF xử lý phép nối (join / 조인) phụ thuộc (dependency / 의존성) phức tạp. Chúng ít xuất hiện hơn nhưng cần biết category để không nhầm với FD thông thường.

### 4.8 Lossless phép nối (join / 조인) và phụ thuộc (dependency / 의존성) Preservation

Decomposition tốt cần ưu tiên lossless phép nối (join / 조인) — phép nối (join / 조인) các quan hệ (relation / 관계) con phải tái tạo đúng quan hệ (relation / 관계) gốc, không sinh tuple giả. phụ thuộc (dependency / 의존성) preservation nghĩa các phụ thuộc (dependency / 의존성) quan trọng có thể enforce mà không phải phép nối (join / 조인) quan hệ (relation / 관계) phức tạp.

> **Chuyển mạch:** Trong **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **4. Functional phụ thuộc (dependency / 의존성) và Normalization** nêu điều cần giải thích; **5. 물리 데이터베이스 설계 — vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. SQL 기본 — DDL, DML, DCL, TCL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. 물리 데이터베이스 설계 — vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)

Logical thiết kế (design / 설계) nói **dữ liệu (data / 데이터) có ý nghĩa và quan hệ gì**; vật lý (physical / 물리적) thiết kế (design / 설계) nói **lưu và truy cập thế nào**.

### 5.1 chỉ mục (index / 인덱스)

Chỉ mục (index / 인덱스) tăng tốc lookup nhưng tốn lưu trữ (storage / 저장소) và tăng chi phí (cost / 비용) khi insert/cập nhật (update / 업데이트)/delete.

B-Tree giữ key/dữ liệu (data / 데이터) pointer theo cấu trúc balanced cây (tree / 트리). B+cây (tree / 트리) thường lưu bản ghi (record / 레코드)/dữ liệu (data / 데이터) pointer ở leaf, nội bộ (internal / 내부) nút (node / 노드) chủ yếu giữ tìm kiếm (search / 검색) key; leaf thường linked giúp phạm vi (range / 범위) scan hiệu quả.

Băm (hash / 해시) chỉ mục (index / 인덱스) rất tốt cho equality lookup nhưng không tự nhiên cho phạm vi (range / 범위) truy vấn (query / 쿼리) vì băm (hash / 해시) phá thứ tự (ordering / 순서).

### 5.2 Clustered vs Non-clustered

Khái niệm cụ thể phụ thuộc DBMS, nhưng ý chung: clustered organization/chỉ mục (index / 인덱스) ảnh hưởng cách row được sắp/bố trí gần theo key; non-clustered chỉ mục (index / 인덱스) là cấu trúc (structure / 구조) riêng trỏ tới row. Một bảng (table / 테이블) thường không thể có nhiều vật lý (physical / 물리적) clustering thứ tự (order / 순서) độc lập.

### 5.3 Partitioning

Horizontal Partitioning chia row. Vertical Partitioning chia column. phạm vi (range / 범위), băm (hash / 해시), danh sách (list / 목록) và Composite Partitioning là các chiến lược phổ biến.

Partitioning có thể tăng manageability/hiệu năng (performance / 성능) nhưng không thay normalization; đây là vật lý (physical / 물리적)/logical scaling quyết định (decision / 결정) khác loại.

### 5.4 Denormalization

Denormalization cố ý thêm redundancy để tối ưu read/hiệu năng (performance / 성능) sau khi hiểu rõ consistency chi phí (cost / 비용). Nó không phải “thiết kế sai” nếu được kiểm soát, nhưng làm tăng burden đồng bộ dữ liệu.

> **Chuyển mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **5. 물리 데이터베이스 설계 — vật lý (physical / 물리적) cơ sở dữ liệu (database / 데이터베이스) thiết kế (design / 설계)** nêu điều cần giải thích; **6. SQL 기본 — DDL, DML, DCL, TCL** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. SQL truy vấn (query / 쿼리) lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. SQL 기본 — DDL, DML, DCL, TCL

### 6.1 DDL

CREATE, ALTER, DROP thường thuộc dữ liệu (data / 데이터) Definition ngôn ngữ (language / 언어). ràng buộc (constraint / 제약조건) như PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL giúp enforce integrity.

### 6.2 DML

SELECT, INSERT, cập nhật (update / 업데이트), DELETE thao tác dữ liệu (data / 데이터). Một số classification gọi SELECT riêng là DQL, nhưng trong nhiều giáo trình vẫn nhóm trong DML/truy vấn (query / 쿼리) ngôn ngữ (language / 언어); đọc đúng taxonomy của đề.

### 6.3 DCL/TCL

GRANT, REVOKE liên quan privilege và thường xếp DCL. lần ghi nhận (commit / 커밋), quay lui (rollback / 롤백), SAVEPOINT liên quan giao dịch (transaction / 트랜잭션) điều khiển (control / 제어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **7. SQL truy vấn (query / 쿼리) lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **6. SQL 기본 — DDL, DML, DCL, TCL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. View, chỉ mục (index / 인덱스), Procedure, Trigger** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. SQL truy vấn (query / 쿼리) lập luận (reasoning / 추론)

### 7.1 WHERE vs HAVING

WHERE lọc row trước grouping. HAVING lọc group sau GROUP BY/aggregation.

Ví dụ: muốn department có AVG(salary) > 5000 thì điều kiện (condition / 조건) aggregate đặt ở HAVING.

### 7.2 phép nối (join / 조인)

INNER phép nối (join / 조인) chỉ giữ match. LEFT OUTER phép nối (join / 조인) giữ mọi row bên trái và NULL phía phải nếu không match. RIGHT OUTER phép nối (join / 조인) tương tự phía phải. FULL OUTER phép nối (join / 조인) giữ mọi row hai bên nếu DBMS hỗ trợ.

CROSS phép nối (join / 조인) tạo Cartesian sản phẩm (product / 제품). SELF phép nối (join / 조인) là bảng (table / 테이블) phép nối (join / 조인) với chính nó qua alias.

### 7.3 NULL

NULL không bằng 0 và không bằng empty string. So sánh với NULL dùng `IS NULL` / `IS NOT NULL`, không dùng `= NULL`.

Trong SQL three-valued lô-gic (logic / 논리), expression với NULL có thể cho UNKNOWN; điều này ảnh hưởng WHERE filtering.

### 7.4 Aggregate

COUNT(*) đếm row. COUNT(column) bỏ NULL ở column đó. SUM/AVG thường bỏ NULL đầu vào (input / 입력). GROUP BY nhóm row theo key.

### 7.5 Subquery

Scalar subquery trả một giá trị (value / 값). Single-row/multi-row subquery cần operator phù hợp. `IN`, `EXISTS`, `ANY/SOME`, `ALL` có ngữ nghĩa (semantics / 의미론) khác nhau.

EXISTS kiểm tra sự tồn tại row từ subquery, thường không quan tâm giá trị (value / 값) cụ thể trong SELECT danh sách (list / 목록).

### 7.6 Set Operations

UNION loại duplicate. UNION ALL giữ duplicate. INTERSECT lấy phần giao. EXCEPT/MINUS lấy difference tùy DBMS.

> **Chuyển mạch:** Trong **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **8. View, chỉ mục (index / 인덱스), Procedure, Trigger** tiếp nhận điểm tựa từ **7. SQL truy vấn (query / 쿼리) lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. giao dịch (transaction / 트랜잭션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. View, chỉ mục (index / 인덱스), Procedure, Trigger

View là virtual quan hệ (relation / 관계) dựa truy vấn (query / 쿼리); có thể dùng lớp trừu tượng (abstraction / 추상화)/bảo mật (security / 보안) nhưng updateability phụ thuộc definition/DBMS.

Stored Procedure đóng gói procedural lô-gic (logic / 논리) chạy trong DB máy chủ (server / 서버). Trigger tự động chạy khi sự kiện (event / 이벤트) được định nghĩa xảy ra. Trigger tiện cho kiểm tra (audit / 감사)/integrity nhưng quá nhiều hidden hành vi (behavior / 동작) có thể khó maintain.

Chỉ mục (index / 인덱스) là truy cập (access / 접근) cấu trúc (structure / 구조), không phải bản sao (copy / 복사) logical bảng (table / 테이블) đầy đủ theo nghĩa view/materialization.

> **Chuyển mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **9. giao dịch (transaction / 트랜잭션)** tiếp nhận điểm tựa từ **8. View, chỉ mục (index / 인덱스), Procedure, Trigger** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Locking và Serializability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. giao dịch (transaction / 트랜잭션)

### 9.1 ACID

Atomicity: all-or-nothing. Consistency: giao dịch (transaction / 트랜잭션) đưa DB từ trạng thái (state / 상태) hợp lệ sang trạng thái (state / 상태) hợp lệ theo ràng buộc (constraint / 제약조건). Isolation: concurrent giao dịch (transaction / 트랜잭션) không gây interference vượt mức isolation cho phép. Durability: committed dữ liệu (data / 데이터) survive thất bại (failure / 실패) phù hợp guarantee của hệ thống (system / 시스템).

### 9.2 tính đồng thời (concurrency / 동시성) anomalies

Dirty Read: đọc dữ liệu (data / 데이터) chưa lần ghi nhận (commit / 커밋) từ giao dịch (transaction / 트랜잭션) khác. Non-repeatable Read: cùng row đọc hai lần thấy giá trị (value / 값) khác do giao dịch (transaction / 트랜잭션) khác lần ghi nhận (commit / 커밋) cập nhật (update / 업데이트). Phantom Read: cùng predicate truy vấn (query / 쿼리) hai lần thấy tập row thay đổi do insert/delete phù hợp predicate.

Lost cập nhật (update / 업데이트): hai giao dịch (transaction / 트랜잭션) cập nhật (update / 업데이트) cùng dữ liệu (data / 데이터) và một cập nhật (update / 업데이트) bị overwrite theo race mẫu (pattern / 패턴).

### 9.3 Isolation Levels

Theo mô hình SQL kinh điển:

- Read Uncommitted cho phép nhiều anomaly nhất.
- Read Committed ngăn dirty read.
- Repeatable Read ngăn dirty read và non-repeatable read; phantom hành vi (behavior / 동작) phụ thuộc hiện thực (implementation / 구현)/tiêu chuẩn (standard / 표준) interpretation.
- Serializable mạnh nhất về ngữ nghĩa (semantics / 의미론) tuần tự.

Đừng biến bảng này thành tuyệt đối cho mọi DBMS; engine có MVCC/locking hiện thực (implementation / 구현) khác nhau. Trong đề lý thuyết, bám ngữ nghĩa (semantics / 의미론) chuẩn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **10. Locking và Serializability** tiếp nhận điểm tựa từ **9. giao dịch (transaction / 트랜잭션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Locking và Serializability

Dùng chung (shared / 공유) khóa (lock / 잠금) cho read, Exclusive khóa (lock / 잠금) cho ghi (write / 쓰기) trong mô hình khóa (lock / 잠금) cơ bản. Nhiều dùng chung (shared / 공유) khóa (lock / 잠금) có thể cùng tồn tại; exclusive khóa (lock / 잠금) xung đột với khóa (lock / 잠금) khác tùy ma trận (matrix / 행렬).

Two-Phase Locking — 2PL — có growing phase chỉ acquire khóa (lock / 잠금) và shrinking phase bản phát hành (release / 릴리스) khóa (lock / 잠금), giúp xung đột (conflict / 충돌) serializability trong mô hình kinh điển.

Strict 2PL thường giữ exclusive khóa (lock / 잠금) tới lần ghi nhận (commit / 커밋)/abort để tránh cascading quay lui (rollback / 롤백) và tăng recoverability.

### 10.1 Deadlock

Deadlock có thể xảy ra khi giao dịch (transaction / 트랜잭션) chờ vòng tròn tài nguyên (resource / 자원)/khóa (lock / 잠금). Điều kiện Coffman quen thuộc: mutual exclusion, hold and wait, no preemption, circular wait.

Giải pháp có thể prevention, avoidance, detection + khôi phục (recovery / 복구), hết thời gian chờ (timeout / 타임아웃). Wait-for đồ thị (graph / 그래프) dùng để detect cycle trong khóa (lock / 잠금) wait quan hệ (relation / 관계).

> **Chuyển mạch:** Trong **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **11. khôi phục (recovery / 복구)** tiếp nhận điểm tựa từ **10. Locking và Serializability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. 데이터 전환 — dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) / Conversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. khôi phục (recovery / 복구)

### 11.1 Log và WAL

Write-Ahead Logging — WAL — yêu cầu log bản ghi (record / 레코드) cần thiết được ghi persistent trước khi dữ liệu (data / 데이터) page tương ứng được ghi theo giao thức (protocol / 프로토콜). Log cho phép REDO/UNDO sau thất bại (failure / 실패).

### 11.2 Checkpoint

Checkpoint giảm lượng log phải scan/reprocess khi khôi phục (recovery / 복구) bằng cách ghi mốc trạng thái cần thiết. Nó không có nghĩa xóa mọi log trước checkpoint trong mọi hệ thống (system / 시스템).

### 11.3 Undo / Redo

UNDO đảo thay đổi của giao dịch (transaction / 트랜잭션) chưa lần ghi nhận (commit / 커밋). REDO áp lại thay đổi committed chưa phản ánh đầy đủ trên disk. Cần hiểu quan hệ (relation / 관계) với buffer chính sách (policy / 정책) như steal/no-steal và force/no-force ở mức khái niệm.

> **Chuyển mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **11. khôi phục (recovery / 복구)** nêu điều cần giải thích; **12. 데이터 전환 — dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) / Conversion** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Cặp dễ nhầm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. 데이터 전환 — dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) / Conversion

Dữ liệu (data / 데이터) conversion gồm phân tích (analysis / 분석) nguồn/đích, ánh xạ (mapping / 매핑), cleansing, transformation, extraction/tải (load / 로드), kiểm tra hợp lệ (validation / 검증) và reconciliation.

Một di chuyển (migration / 마이그레이션) thành công không chỉ là “bản sao (copy / 복사) đủ row”. Phải kiểm tra datatype, encoding, key quan hệ (relation / 관계), nullability, nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙), duplicate, referential integrity và aggregate/điều khiển (control / 제어) total.

ETL: Extract → Transform → tải (load / 로드). ELT: Extract → tải (load / 로드) → Transform, phổ biến khi mục tiêu (target / 대상) nền tảng (platform / 플랫폼) có compute mạnh. Trong kỳ thi truyền thống ETL thường gặp hơn, nhưng hiểu cả hai giúp không nhầm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **12. 데이터 전환 — dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) / Conversion** đã nêu tiêu chí phân biệt, còn **13. Cặp dễ nhầm** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Procedural drills** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| bên ngoài (external / 외부)/Conceptual/nội bộ (internal / 내부) lược đồ (schema / 스키마) | người dùng (user / 사용자) view / toàn cục (global / 전역) logical / vật lý (physical / 물리적) lưu trữ (storage / 저장소) |
| Super Key vs Candidate Key | unique có thể thừa / minimal unique |
| Selection vs Projection | row / column |
| Partial vs Transitive phụ thuộc (dependency / 의존성) | một phần composite key / qua non-key intermediate |
| 3NF vs BCNF | cho phép một số FD với prime attribute / determinant phải superkey |
| B+cây (tree / 트리) vs băm (hash / 해시) chỉ mục (index / 인덱스) | phạm vi (range / 범위)/thứ tự (order / 순서) tốt / equality tốt |
| WHERE vs HAVING | row trước grouping / group sau aggregation |
| COUNT(*) vs COUNT(col) | mọi row / bỏ NULL col |
| Dirty vs Non-repeatable vs Phantom | uncommitted giá trị (value / 값) / changed row / changed row set |
| dùng chung (shared / 공유) vs Exclusive khóa (lock / 잠금) | read sharing / ghi (write / 쓰기) exclusive |
| UNDO vs REDO | quay lui (rollback / 롤백) uncommitted / reapply committed |
| Normalization vs Partitioning | logical redundancy / vật lý (physical / 물리적) phân phối (distribution / 분포) |

> **Chuyển mạch:** Trong **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **13. Cặp dễ nhầm** đã nêu tiêu chí phân biệt, còn **14. Procedural drills** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. 과락 방지 checklist — Môn 3** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Procedural drills

### Drill 1 — Key

Quan hệ (relation / 관계) `ENROLL(StudentId, CourseId, StudentName, CourseName, Grade)` có key `(StudentId, CourseId)`. Xác định partial phụ thuộc (dependency / 의존성) và đề xuất decomposition tới 2NF.

### Drill 2 — 3NF

Nếu `EmployeeId → DeptId` và `DeptId → DeptName`, vì sao `DeptName` tạo transitive phụ thuộc (dependency / 의존성) trong quan hệ (relation / 관계) Employee?

### Drill 3 — Relational Algebra

Muốn lấy chỉ `name` của employee có salary > 5000, thao tác (operation / 연산) nào phải xảy ra về mặt lô-gic (logic / 논리): Selection và Projection theo thứ tự nào?

### Drill 4 — SQL

Viết truy vấn (query / 쿼리) tìm department có ít nhất 5 employee và average salary > 5000. Giải thích điều kiện (condition / 조건) nào nằm WHERE và điều kiện (condition / 조건) nào nằm HAVING nếu thêm `status='ACTIVE'`.

### Drill 5 — NULL

Giải thích vì sao `WHERE bonus = NULL` không tìm được row như mong đợi và phải sửa thành gì.

### Drill 6 — Isolation

T1 đọc balance=100. T2 cập nhật (update / 업데이트) balance=120 và lần ghi nhận (commit / 커밋). T1 đọc lại cùng row thấy 120. Đây là anomaly nào?

### Drill 7 — Phantom

T1 truy vấn (query / 쿼리) `salary > 5000` thấy 10 row. T2 insert một employee salary 6000 và lần ghi nhận (commit / 커밋). T1 chạy lại thấy 11 row. Đây là gì?

### Drill 8 — Deadlock

T1 giữ khóa (lock / 잠금) A chờ B; T2 giữ B chờ A. Vẽ wait-for đồ thị (graph / 그래프) và xác định cycle.

### Drill 9 — chỉ mục (index / 인덱스)

Truy vấn (query / 쿼리) chủ yếu là `WHERE created_at BETWEEN ...` và thứ tự (order / 순서) BY created_at. Tại sao B+cây (tree / 트리) thường tự nhiên hơn băm (hash / 해시) chỉ mục (index / 인덱스)?

### Drill 10 — di chuyển (migration / 마이그레이션)

Nguồn (source / 소스) có 100.000 row, mục tiêu (target / 대상) cũng 100.000 row nhưng 2% foreign key invalid. Vì sao row count match chưa đủ để xác nhận di chuyển (migration / 마이그레이션)?

> **Chuyển mạch:** Ở chặng này của **Môn 3 — 데이터베이스 구축: Deep Dive 2026**, **15. 과락 방지 checklist — Môn 3** tiếp nhận điểm tựa từ **14. Procedural drills** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 15. 과락 방지 checklist — Môn 3

Phải tự làm được:

- phân biệt 3 lược đồ (schema / 스키마) và dữ liệu (data / 데이터) independence;
- tìm candidate/primary/foreign/composite key;
- giải Selection, Projection, phép nối (join / 조인), Division ở mức ý nghĩa;
- nhận diện functional, partial, transitive phụ thuộc (dependency / 의존성);
- normalize scenario tới ít nhất 3NF/BCNF ở mức bài cơ bản;
- phân biệt B/B+cây (tree / 트리), băm (hash / 해시), partitioning, denormalization;
- viết/đọc SELECT, phép nối (join / 조인), GROUP BY, HAVING, subquery, set thao tác (operation / 연산);
- giải NULL ngữ nghĩa (semantics / 의미론) và aggregate;
- phân loại DDL/DML/DCL/TCL;
- phân biệt view/chỉ mục (index / 인덱스)/procedure/trigger;
- giải ACID, anomaly và isolation;
- phân biệt dùng chung (shared / 공유)/exclusive khóa (lock / 잠금), 2PL, deadlock;
- hiểu WAL, checkpoint, UNDO/REDO;
- mô tả luồng (flow / 흐름) dữ liệu (data / 데이터) di chuyển (migration / 마이그레이션) và kiểm tra hợp lệ (validation / 검증).

Nếu normalization, SQL và giao dịch (transaction / 트랜잭션) chỉ “nhìn quen” nhưng không tự suy luận được, Môn 3 vẫn còn rủi ro cao.

> **Bàn giao:** Sau **15. 과락 방지 checklist — Môn 3**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
