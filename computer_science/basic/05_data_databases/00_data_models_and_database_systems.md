# Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình dữ liệu (data model / 데이터 모델) là cách nhìn dữ liệu** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **Lược đồ (schema / 스키마) và các ràng buộc (constraints / 제약조건들)** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Một program nhỏ có thể giữ trạng thái (state / 상태) trong bộ nhớ (memory / 메모리) hoặc tệp (file / 파일). Khi dữ liệu cần sống lâu hơn tiến trình (process / 프로세스), được truy cập đồng thời, truy vấn theo nhiều cách, khôi phục (recovery / 복구) sau crash và enforce các ràng buộc (constraints / 제약조건들), ta cần một dữ liệu (data / 데이터) management hệ thống (system / 시스템). cơ sở dữ liệu (database / 데이터베이스) Management hệ thống (system / 시스템) — DBMS (데이터베이스 관리 시스템) không chỉ “lưu rows”; nó quản lý biểu diễn (representation / 표현), truy vấn (query / 쿼리), tính đồng thời (concurrency / 동시성), durability và siêu dữ liệu (metadata / 메타데이터) dưới một đặc tả hợp đồng (contract / 계약) thống nhất.

## Mô hình dữ liệu (data model / 데이터 모델) là cách nhìn dữ liệu

Mô hình dữ liệu (data model / 데이터 모델) định nghĩa structures, relationships và operations mà người dùng (user / 사용자) nhìn thấy. Relational mô hình (model / 모델) biểu diễn dữ liệu (data / 데이터) bằng relations/tuples/attributes và operations theo relational algebra. Document mô hình (model / 모델) tổ chức documents nested. Key-value mô hình (model / 모델) expose key→giá trị (value / 값). đồ thị (graph / 그래프) cơ sở dữ liệu (database / 데이터베이스) nhấn mạnh vertices/edges/traversal.

Mô hình (model / 모델) không chỉ là lưu trữ (storage / 저장소) bố cục (layout / 레이아웃). Một relational bảng (table / 테이블) có thể physically stored row-wise, columnar, compressed hoặc phân tán (distributed / 분산) nhưng vẫn expose relational ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Mô hình dữ liệu (data model / 데이터 모델) là cách nhìn dữ liệu** nêu điều cần giải thích; **Lược đồ (schema / 스키마) và các ràng buộc (constraints / 제약조건들)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Logical vs vật lý (physical / 물리적) dữ liệu (data / 데이터) independence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lược đồ (schema / 스키마) và các ràng buộc (constraints / 제약조건들)

Lược đồ (schema / 스키마) mô tả cấu trúc (structure / 구조) và các ràng buộc (constraints / 제약조건들). kiểu (type / 타입), NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY và CHECK encode invariants gần dữ liệu (data / 데이터). Khi bất biến (invariant / 불변식) chỉ tồn tại trong ứng dụng (application / 애플리케이션) mã (code / 코드), nhiều writers/services dễ vi phạm.

Ràng buộc (constraint / 제약조건) có chi phí (cost / 비용) khi ghi (write / 쓰기) nhưng đổi lại integrity được centralized. Tuy nhiên nghiệp vụ (business / 비즈니스) rules phức tạp không phải lúc nào phù hợp DB ràng buộc (constraint / 제약조건); ranh giới (boundary / 경계) phải được chọn có chủ đích.

> **Chuyển mạch:** Ở chặng này của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Lược đồ (schema / 스키마) và các ràng buộc (constraints / 제약조건들)** nêu điều cần giải thích; **Logical vs vật lý (physical / 물리적) dữ liệu (data / 데이터) independence** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) và declarative thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logical vs vật lý (physical / 물리적) dữ liệu (data / 데이터) independence

Một mục tiêu lịch sử của DBMS là tách logical mô hình (model / 모델) khỏi vật lý (physical / 물리적) lưu trữ (storage / 저장소). ứng dụng (application / 애플리케이션) viết truy vấn (query / 쿼리) “tìm orders của customer X”; optimizer/lưu trữ (storage / 저장소) engine quyết định chỉ mục (index / 인덱스) scan, phép nối (join / 조인) thứ tự (order / 순서), pages.

Lớp trừu tượng (abstraction / 추상화) này cho phép thêm chỉ mục (index / 인덱스) mà không sửa truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론). Nhưng hiệu năng (performance / 성능) vẫn leak: truy vấn (query / 쿼리) shape, selectivity và giao dịch (transaction / 트랜잭션) patterns ảnh hưởng plan.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Logical vs vật lý (physical / 물리적) dữ liệu (data / 데이터) independence** nêu điều cần giải thích; **Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) và declarative thực thi (execution / 실행)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **OLTP và OLAP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) và declarative thực thi (execution / 실행)

SQL declarative: người dùng (user / 사용자) mô tả tập kết quả (result set / 결과 집합), optimizer chọn thực thi (execution / 실행) plan. Đây khác imperative vòng lặp (loop / 루프) qua records. Optimizer dùng statistics và chi phí (cost / 비용) mô hình (model / 모델) để estimate rows/I/O/CPU.

Same SQL có thể chọn plan khác khi dữ liệu (data / 데이터) phân phối (distribution / 분포), indexes hoặc parameters thay đổi. Vì vậy “SQL văn bản (text / 텍스트) giống nhau” không guarantee hiệu năng (performance / 성능) giống nhau.

> **Chuyển mạch:** Trong **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **OLTP và OLAP** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) ngôn ngữ (language / 언어) và declarative thực thi (execution / 실행)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Row store vs column store** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OLTP và OLAP

Online giao dịch (transaction / 트랜잭션) Processing thường nhiều short reads/writes, low độ trễ (latency / 지연 시간), tính đồng thời (concurrency / 동시성) cao, normalized relational thiết kế (design / 설계) phổ biến. Online Analytical Processing thường scan/aggregate volumes lớn; columnar lưu trữ (storage / 저장소), denormalization/star schemas và vectorized thực thi (execution / 실행) phù hợp hơn.

Một lược đồ (schema / 스키마) tối ưu giao dịch (transaction / 트랜잭션) không luôn tối ưu analytics. tải công việc (workload / 워크로드) shape quyết định vật lý (physical / 물리적) thiết kế (design / 설계).

> **Chuyển mạch:** Ở chặng này của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Row store vs column store** tiếp nhận điểm tựa từ **OLTP và OLAP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **In-memory, disk-backed và phân tán (distributed / 분산) databases** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Row store vs column store

Row store đặt fields cùng bản ghi (record / 레코드) gần nhau, tốt khi giao dịch (transaction / 트랜잭션) đọc/ghi (write / 쓰기) nhiều columns của một row. Column store đặt cùng column gần nhau, tốt khi analytic truy vấn (query / 쿼리) chỉ đọc vài columns qua nhiều rows và compression theo column hiệu quả.

Cùng logical bảng (table / 테이블), lưu trữ (storage / 저장소) orientation khác tạo locality khác — liên kết (connection / 연결) trực tiếp với [data layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **In-memory, disk-backed và phân tán (distributed / 분산) databases** tiếp nhận điểm tựa từ **Row store vs column store** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) và danh mục (catalog / 카탈로그)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## In-memory, disk-backed và phân tán (distributed / 분산) databases

“In-memory cơ sở dữ liệu (database / 데이터베이스)” không nghĩa durability không tồn tại; nó có thể dùng WAL/snapshots để recover. Disk-backed DB bộ nhớ đệm (cache / 캐시) hot pages trong bộ nhớ (memory / 메모리). phân tán (distributed / 분산) DB partition/replicate dữ liệu (data / 데이터) qua nodes và phải đối mặt mạng (network / 네트워크) thất bại (failure / 실패), consistency và consensus.

> **Chuyển mạch:** Trong **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **In-memory, disk-backed và phân tán (distributed / 분산) databases** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) và danh mục (catalog / 카탈로그)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) và danh mục (catalog / 카탈로그)

DBMS cần biết tables, columns, indexes, các ràng buộc (constraints / 제약조건들), privileges và statistics. hệ thống (system / 시스템) danh mục (catalog / 카탈로그) lưu siêu dữ liệu (metadata / 메타데이터) này. truy vấn (query / 쿼리) planner phụ thuộc statistics; stale/misleading stats có thể làm cardinality estimates sai và chọn plan tệ.

> **Chuyển mạch:** Ở chặng này của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, các dấu vết trong **Siêu dữ liệu (metadata / 메타데이터) và danh mục (catalog / 카탈로그)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> DBMS là **máy trạng thái (state machine / 상태 머신) bền vững với truy vấn (query / 쿼리) engine**: mô hình dữ liệu (data model / 데이터 모델) định nghĩa logical trạng thái (state / 상태); các ràng buộc (constraints / 제약조건들) bảo vệ invariants; giao dịch (transaction / 트랜잭션) điều khiển concurrent transitions; lưu trữ (storage / 저장소)/khôi phục (recovery / 복구) làm trạng thái (state / 상태) sống qua crash.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“cơ sở dữ liệu (database / 데이터베이스) chỉ là tệp (file / 파일) có API.”** DBMS thêm tính đồng thời (concurrency / 동시성) điều khiển (control / 제어), truy vấn (query / 쿼리) planning, transactions, các ràng buộc (constraints / 제약조건들), khôi phục (recovery / 복구) và bảo mật (security / 보안).

**“NoSQL nghĩa không có lược đồ (schema / 스키마).”** lược đồ (schema / 스키마) vẫn tồn tại trong dữ liệu (data / 데이터)/ứng dụng (application / 애플리케이션) expectations; có thể flexible/implicit thay vì centrally enforced.

**“Relational mô hình (model / 모델) = SQL hiện thực (implementation / 구현) cụ thể.”** SQL là ngôn ngữ (language / 언어) family và DBMS implementations có extensions; relational mô hình (model / 모델) là mathematical foundation rộng hơn.

> **Chuyển mạch:** Trong **Mô hình dữ liệu (data model / 데이터 모델) và cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들)**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Tiếp theo: [relational model/normalization](./01_relational_model_keys_and_normalization.md), [transactions](./02_transactions_acid_and_concurrency_control.md), [indexes/query execution](./03_indexes_and_query_execution.md), [WAL/recovery](./04_storage_logs_recovery_and_durability.md). Phần SQL thực hành trong repo có thể đọc song song với conceptual chapters này.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
