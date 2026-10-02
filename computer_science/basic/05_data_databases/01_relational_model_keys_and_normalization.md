# Relational mô hình (model / 모델), keys và normalization

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Relational model, keys và normalization**. Route đi từ relation/tuple/attribute → keys và functional dependencies → normal forms → denormalization và NULL semantics, để schema giữ được dữ liệu đúng mà vẫn phục vụ truy cập.

Relational mô hình (model / 모델) do Edgar F. Codd đề xuất tách logical dữ liệu (data / 데이터) relationships khỏi pointer/điều hướng (navigation / 내비게이션) vật lý (physical / 물리적) lưu trữ (storage / 저장소). Ý tưởng cốt lõi: dữ liệu được mô tả bằng relations và queries dựa values/relations thay vì ứng dụng (application / 애플리케이션) phải biết bản ghi (record / 레코드) nằm ở khối (block / 블록) hay nối bằng pointer nào.

## Quan hệ (relation / 관계), tuple và attribute

Trong mô hình (model / 모델) lý tưởng, quan hệ (relation / 관계) là tập tuples cùng attributes. SQL bảng (table / 테이블) gần quan hệ (relation / 관계) nhưng có differences: SQL thường là bag/multiset trừ khi DISTINCT; NULL thêm three-valued lô-gic (logic / 논리); row thứ tự (ordering / 순서) không được guarantee nếu thiếu thứ tự (order / 순서) BY.

Attribute có lĩnh vực (domain / 도메인) — tập giá trị hợp lệ. lược đồ (schema / 스키마) đặt types và các ràng buộc (constraints / 제약조건들) để approximate lĩnh vực (domain / 도메인).

> **Chuyển mạch:** Trong **Relational mô hình (model / 모델), keys và normalization**, **Keys từ định danh (identity / 식별자) và functional phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **Quan hệ (relation / 관계), tuple và attribute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Foreign key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Keys từ định danh (identity / 식별자) và functional phụ thuộc (dependency / 의존성)

Superkey là tập attributes xác định duy nhất tuple. Candidate key là superkey tối thiểu. Primary key là candidate key được chọn làm identifier chính trong lược đồ (schema / 스키마); alternate keys vẫn có thể UNIQUE.

Surrogate key như generated ID không làm natural uniqueness biến mất. Nếu nghiệp vụ (business / 비즈니스) nói email+tenant phải unique, vẫn cần ràng buộc (constraint / 제약조건) phù hợp dù có numeric primary key.

Functional phụ thuộc (dependency / 의존성) `X → Y` nghĩa nếu hai tuples có cùng X thì phải cùng Y. Đây là foundation của normalization.

> **Chuyển mạch:** Ở chặng này của **Relational mô hình (model / 모델), keys và normalization**, **Foreign key** tiếp nhận điểm tựa từ **Keys từ định danh (identity / 식별자) và functional phụ thuộc (dependency / 의존성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tại sao normalization tồn tại?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Foreign key

Foreign key encode referential integrity: child giá trị (value / 값) phải tham chiếu (reference / 참조) existing parent candidate/primary key theo rules, hoặc NULL nếu allowed. Delete/cập nhật (update / 업데이트) chính sách (policy / 정책) có RESTRICT, CASCADE, SET NULL... tùy ngữ nghĩa (semantics / 의미론).

Cascade tiện nhưng có thể tạo large implicit effects; cần hiểu đồ thị (graph / 그래프) relationships và giao dịch (transaction / 트랜잭션) phạm vi (scope / 범위).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational mô hình (model / 모델), keys và normalization**, **Tại sao normalization tồn tại?** tiếp nhận điểm tựa từ **Foreign key** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1NF, 2NF, 3NF và BCNF bằng bản chất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao normalization tồn tại?

Giả sử một bảng (table / 테이블) lặp customer address trên mỗi thứ tự (order / 순서). cập nhật (update / 업데이트) address phải sửa nhiều rows; bỏ thứ tự (order / 순서) cuối có thể mất customer info; thêm customer chưa có thứ tự (order / 순서) khó biểu diễn. Đây là cập nhật (update / 업데이트)/delete/insert anomalies.

Normalization decomposition tách facts theo dependencies để mỗi fact có một home rõ, giảm redundancy gây inconsistency.

> **Chuyển mạch:** Trong **Relational mô hình (model / 모델), keys và normalization**, **1NF, 2NF, 3NF và BCNF bằng bản chất** tiếp nhận điểm tựa từ **Tại sao normalization tồn tại?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Denormalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1NF, 2NF, 3NF và BCNF bằng bản chất

1NF trong practical SQL teaching thường yêu cầu attributes atomic theo chosen relational biểu diễn (representation / 표현), không repeating groups. “Atomic” phụ thuộc lĩnh vực (domain / 도메인); JSON document có thể là một scalar giá trị (value / 값) trong DB nhưng relational decomposition khác.

2NF loại partial phụ thuộc (dependency / 의존성) của non-key attribute trên một phần composite candidate key. Nó chỉ relevant khi candidate key composite.

3NF loại certain transitive dependencies của non-key attributes qua non-key determinants, nhằm để non-key facts phụ thuộc key đúng place.

BCNF mạnh hơn: với mọi non-trivial FD `X→Y`, X phải là superkey. Một số schemas đạt 3NF nhưng không BCNF để preserve dependencies hoặc vì practical sự đánh đổi (trade-off / 트레이드오프).

Normalization không phải ritual đếm forms; nó là lập luận (reasoning / 추론) “fact này phụ thuộc identifier nào?”.

> **Chuyển mạch:** Ở chặng này của **Relational mô hình (model / 모델), keys và normalization**, **Denormalization** tiếp nhận điểm tựa từ **1NF, 2NF, 3NF và BCNF bằng bản chất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NULL và three-valued lô-gic (logic / 논리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Denormalization

Denormalization intentional duplicate/precompute để giảm joins hoặc hỗ trợ (support / 지원) analytics. Nó không “ngược quy tắc” nếu sự đánh đổi (trade-off / 트레이드오프) tường minh (explicit / 명시적) và consistency cơ chế (mechanism / 메커니즘) tồn tại.

Materialized view, bộ nhớ đệm (cache / 캐시), tìm kiếm (search / 검색) chỉ mục (index / 인덱스) đều là derived/duplicated trạng thái (state / 상태). Câu hỏi là nguồn chuẩn (source of truth / 정본) và refresh consistency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational mô hình (model / 모델), keys và normalization**, **NULL và three-valued lô-gic (logic / 논리)** tiếp nhận điểm tựa từ **Denormalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relational algebra intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NULL và three-valued lô-gic (logic / 논리)

SQL NULL thường biểu diễn unknown/missing/not applicable tùy thiết kế (design / 설계), nhưng ngữ nghĩa (semantics / 의미론) tạo UNKNOWN trong comparisons. `NULL = NULL` không TRUE; dùng `IS NULL`. `WHERE` giữ rows predicate TRUE, loại FALSE và UNKNOWN.

`NOT IN` với subquery chứa NULL có thể gây kết quả bất ngờ vì UNKNOWN propagation. Đây là chỗ logical mô hình (model / 모델) và SQL ngữ nghĩa (semantics / 의미론) cần phân biệt.

> **Chuyển mạch:** Trong **Relational mô hình (model / 모델), keys và normalization**, **Relational algebra intuition** tiếp nhận điểm tựa từ **NULL và three-valued lô-gic (logic / 논리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relational algebra intuition

Selection lọc rows; projection chọn attributes; phép nối (join / 조인) kết hợp tuples theo predicate; union/difference/set operations compose relations. SQL optimizer có thể reorder equivalent operations khi ngữ nghĩa (semantics / 의미론) cho phép, như push predicate trước phép nối (join / 조인) để giảm intermediate dữ liệu (data / 데이터).

> **Chuyển mạch:** Ở chặng này của **Relational mô hình (model / 모델), keys và normalization**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Relational algebra intuition** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Relational thiết kế (design / 설계) là **phân bố facts theo dependencies**. Key trả lời “fact thuộc thực thể (entity / 엔터티)/định danh (identity / 식별자) nào”; normalization giảm việc cùng một fact phải được cập nhật ở nhiều nơi.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational mô hình (model / 모델), keys và normalization**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Primary key phải là auto-increment integer.”** Đây chỉ là hiện thực (implementation / 구현)/thiết kế (design / 설계) choice; key concept rộng hơn.

**“3NF luôn là lược đồ (schema / 스키마) tối ưu.”** tải công việc (workload / 워크로드), các ràng buộc (constraints / 제약조건들) và read các mô hình (models / 모델들) có thể justify denormalization; integrity sự đánh đổi (trade-off / 트레이드오프) phải tường minh (explicit / 명시적).

**“NULL là empty string/zero.”** Không; NULL có special ngữ nghĩa (semantics / 의미론) và three-valued lô-gic (logic / 논리).

> **Chuyển mạch:** Trong **Relational mô hình (model / 모델), keys và normalization**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Logic/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) giúp hiểu các ràng buộc (constraints / 제약조건들). [Indexes](./03_indexes_and_query_execution.md) là vật lý (physical / 물리적) acceleration không thay logical normalization. [Transactions](./02_transactions_acid_and_concurrency_control.md) giữ multiple related writes atomic.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
