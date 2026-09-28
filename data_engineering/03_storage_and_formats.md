# 03 — lưu trữ (storage / 저장소), tệp (file / 파일) format và analytical bố cục (layout / 레이아웃)

> **Mạch đọc:** Đặt **03 — lưu trữ (storage / 저장소), tệp (file / 파일) format và analytical bố cục (layout / 레이아웃)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Logical lược đồ (schema / 스키마) chưa đủ** sang **2. Row-oriented và column-oriented**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


## 1. Logical lược đồ (schema / 스키마) chưa đủ

Hai dataset có cùng column và cùng row nhưng hiệu năng (performance / 성능) có thể khác nhau hàng chục lần chỉ vì cách dữ liệu được đặt trên lưu trữ (storage / 저장소). Analytical hệ thống (system / 시스템) đọc khối lượng lớn dữ liệu, nên vật lý (physical / 물리적) bố cục (layout / 레이아웃) quyết định lượng byte phải đọc, khả năng parallel scan và hiệu quả compression.

Vì vậy dữ liệu (data / 데이터) Engineer phải lập luận (reasoning / 추론) cả logical mô hình (model / 모델) lẫn vật lý (physical / 물리적) biểu diễn (representation / 표현).

## 2. Row-oriented và column-oriented

Row-oriented bố cục (layout / 레이아웃) đặt các trường dữ liệu (field / 필드) của một bản ghi (record / 레코드) gần nhau. Nó phù hợp khi tải công việc (workload / 워크로드) thường đọc hoặc ghi phần lớn trường dữ liệu (field / 필드) của một số ít bản ghi (record / 레코드), như OLTP.

Column-oriented bố cục (layout / 레이아웃) nhóm giá trị cùng column. Analytical truy vấn (query / 쿼리) như `SELECT region, SUM(amount)` có thể bỏ qua hàng chục column không dùng. Các giá trị cùng kiểu và thường tương tự nhau cũng nén tốt hơn.

Columnar không có nghĩa là từng column luôn là một tệp (file / 파일) riêng. Format như Parquet tổ chức dữ liệu thành row group rồi lưu column chunk bên trong. Cấu trúc này cân bằng giữa scan theo column, siêu dữ liệu (metadata / 메타데이터) statistics và khả năng chia công việc (work / 작업).

## 3. Parquet như một ví dụ về predicate pushdown

Một Parquet tệp (file / 파일) có siêu dữ liệu (metadata / 메타데이터) như min/max cho column trong từng row group. Nếu truy vấn (query / 쿼리) cần `event_date = '2026-09-22'` và siêu dữ liệu (metadata / 메타데이터) chứng minh row group chỉ chứa ngày trước đó, engine có thể bỏ qua khối (block / 블록) mà không decode toàn bộ dữ liệu (data / 데이터).

Đây là predicate pushdown/dữ liệu (data / 데이터) skipping. Lợi ích phụ thuộc phân phối (distribution / 분포) và statistics. Nếu column có min/max gần như bao trùm toàn lĩnh vực (domain / 도메인) trong mọi row group, khả năng skip thấp.

Vật lý (physical / 물리적) thứ tự (ordering / 순서) vì vậy có thể làm siêu dữ liệu (metadata / 메타데이터) trở nên hữu ích hơn, nhưng sorting cũng tốn compute và làm ingestion phức tạp hơn. Không có bố cục (layout / 레이아웃) miễn phí.

## 4. Compression là sự đánh đổi (trade-off / 트레이드오프) CPU và I/O

Compression giảm byte trên lưu trữ (storage / 저장소) và mạng (network / 네트워크) nhưng cần CPU để encode/decode. Analytical tải công việc (workload / 워크로드) thường hưởng lợi vì I/O đắt và columnar dữ liệu (data / 데이터) nén tốt. Tuy nhiên codec mạnh hơn không mặc định tốt hơn nếu tải công việc (workload / 워크로드) latency-sensitive hoặc CPU đã là bottleneck.

Phải đo end-to-end: compressed kích thước (size / 크기), scan bytes, decode CPU, truy vấn (query / 쿼리) độ trễ (latency / 지연 시간) và chi phí (cost / 비용). Chọn codec chỉ theo compression ratio là tối ưu sai mục tiêu.

## 5. Partitioning

Partitioning chia dataset theo key để truy vấn (query / 쿼리) có thể loại bỏ phần dữ liệu không liên quan. Time-series thường partition theo date vì truy vấn (query / 쿼리) hay giới hạn thời gian.

Partition quá thô khiến mỗi truy vấn (query / 쿼리) vẫn đọc nhiều dữ liệu. Partition quá mịn tạo rất nhiều directory/tệp (file / 파일) nhỏ, tăng siêu dữ liệu (metadata / 메타데이터) overhead và scheduling chi phí (cost / 비용). Partition theo key cardinality cực cao như `user_id` thường tạo explosion trừ khi nền tảng (platform / 플랫폼) có cơ chế khác phù hợp.

Partition key phải xuất phát từ truy cập (access / 접근) mẫu (pattern / 패턴), volume và vòng đời (lifecycle / 생명주기) thao tác (operation / 연산), không phải từ việc column đó "quan trọng".

## 6. Small-file bài toán (problem / 문제)

Một triệu tệp (file / 파일) 10 KB và mười tệp (file / 파일) 1 GB có tổng byte tương tự nhưng operational hành vi (behavior / 동작) hoàn toàn khác. Mỗi tệp (file / 파일) cần siêu dữ liệu (metadata / 메타데이터) lookup, open yêu cầu (request / 요청), tác vụ (task / 작업) scheduling và bookkeeping. Với đối tượng (object / 객체) lưu trữ (storage / 저장소), yêu cầu (request / 요청) overhead và listing cũng trở thành chi phí (cost / 비용).

Streaming/micro-batch ingestion dễ sinh tệp (file / 파일) nhỏ vì mỗi tác vụ (task / 작업) liên tục flush đầu ra (output / 출력). Compaction gom các tệp (file / 파일) nhỏ thành tệp (file / 파일) lớn hơn là maintenance thao tác (operation / 연산) quan trọng của analytical lưu trữ (storage / 저장소).

Nhưng compaction cần coordination: không được làm reader nhìn thấy half-written trạng thái (state / 상태), không được mất concurrent writes và cần garbage-collect tệp (file / 파일) cũ an toàn. Đây là một trong các lý do bảng (table / 테이블) format hiện đại tồn tại trên đối tượng (object / 객체) lưu trữ (storage / 저장소).

## 7. đối tượng (object / 객체) lưu trữ (storage / 저장소) không phải filesystem truyền thống

Đối tượng (object / 객체) lưu trữ (storage / 저장소) cung cấp không gian tên (namespace / 네임스페이스) key/đối tượng (object / 객체) và API thay vì POSIX filesystem ngữ nghĩa (semantics / 의미론) đầy đủ. Rename có thể không phải atomic siêu dữ liệu (metadata / 메타데이터) thao tác (operation / 연산) như cục bộ (local / 로컬) filesystem; trong một số hệ thống nó tương đương bản sao (copy / 복사) rồi delete.

Thuật toán (algorithm / 알고리즘) được thiết kế dựa trên atomic rename của HDFS/cục bộ (local / 로컬) filesystem có thể hoạt động kém hoặc không đúng khi chuyển thẳng sang đối tượng (object / 객체) lưu trữ (storage / 저장소). hiện đại (modern / 현대적) bảng (table / 테이블) formats giải quyết vấn đề này bằng siêu dữ liệu (metadata / 메타데이터)/manifest và lần ghi nhận (commit / 커밋) giao thức (protocol / 프로토콜) phù hợp hơn.

## 8. Warehouse, lake và lakehouse

Dữ liệu (data / 데이터) warehouse truyền thống cung cấp lưu trữ (storage / 저장소) + compute + danh mục (catalog / 카탈로그) + giao dịch (transaction / 트랜잭션)/truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론) trong một hệ thống được quản lý chặt. dữ liệu (data / 데이터) lake ưu tiên lưu dữ liệu linh hoạt trên lưu trữ (storage / 저장소) rẻ/open format nhưng nếu thiếu siêu dữ liệu (metadata / 메타데이터), chất lượng (quality / 품질) và quản trị (governance / 거버넌스) rất dễ thành dữ liệu (data / 데이터) swamp.

Lakehouse cố gắng đưa bảng (table / 테이블) ngữ nghĩa (semantics / 의미론) như snapshot, lược đồ (schema / 스키마) evolution, transaction-like lần ghi nhận (commit / 커밋) và thời gian (time / 시간) travel lên đối tượng (object / 객체) lưu trữ (storage / 저장소)/open tệp (file / 파일) formats. Điểm cốt lõi không phải marketing term mà là separation giữa dữ liệu (data / 데이터) files và siêu dữ liệu (metadata / 메타데이터) tầng (layer / 계층) mô tả snapshot hợp lệ.

## 9. lược đồ (schema / 스키마) evolution

Thêm column, đổi kiểu (type / 타입) hoặc rename trường dữ liệu (field / 필드) phải được xét ở cả writer, stored dữ liệu (data / 데이터) và reader. Một reader cũ có thể không hiểu lược đồ (schema / 스키마) mới. Một rename đôi khi bị engine nhìn như drop + add nếu định danh (identity / 식별자) chỉ dựa vào tên.

Safe evolution cần tính tương thích (compatibility / 호환성) chính sách (policy / 정책) và triển khai (deployment / 배포) thứ tự (order / 순서). Ví dụ producer thêm trường dữ liệu (field / 필드) optional trước, bên tiêu thụ (consumer / 소비자) được nâng cấp để đọc trường dữ liệu (field / 필드) đó, sau đó mới bắt đầu dựa vào trường dữ liệu (field / 필드). Breaking thay đổi (change / 변경) cần phiên bản (version / 버전) hoặc di chuyển (migration / 마이그레이션) tường minh (explicit / 명시적).

## 10. chi phí (cost / 비용) lập luận (reasoning / 추론)

Trong cloud analytics, hiệu năng (performance / 성능) và chi phí (cost / 비용) thường cùng liên quan đến lượng dữ liệu (data / 데이터) scan, shuffle và thời gian compute. Partition pruning, column pruning và compact tệp (file / 파일) không chỉ là tối ưu hóa (optimization / 최적화) kỹ thuật mà trực tiếp thay đổi hóa đơn.

Tuy nhiên tối ưu lưu trữ (storage / 저장소) để giảm scan có thể tăng ingestion/maintenance chi phí (cost / 비용). Một hệ thống tốt tối ưu total chi phí (cost / 비용) of quyền sở hữu (ownership / 소유권), bao gồm compute, lưu trữ (storage / 저장소), mạng (network / 네트워크), operational độ phức tạp (complexity / 복잡도) và thời gian kỹ sư, thay vì chỉ tối thiểu một chỉ số (metric / 지표).

## 11. bố cục (layout / 레이아웃) invariants và read amplification

Vật lý (physical / 물리적) bố cục (layout / 레이아웃) nên được đánh giá bằng tỷ lệ giữa dữ liệu hữu ích và dữ liệu phải đọc:

```text
read amplification = bytes read / bytes returned or used
```

Partition pruning và column pruning giảm read amplification. Nhưng statistics không đáng tin nếu row group quá lớn, dữ liệu không được cluster hoặc predicate có selectivity thấp. tệp (file / 파일) nhỏ hơn không mặc định tốt hơn nếu số yêu cầu (request / 요청) và siêu dữ liệu (metadata / 메타데이터) overhead tăng mạnh.

## 12. tệp (file / 파일) lần ghi nhận (commit / 커밋) và visibility

Writer không nên ghi trực tiếp vào đường dẫn (path / 경로) mà reader coi là committed. Mẫu an toàn là ghi temporary files, validate lược đồ (schema / 스키마)/row count/checksum, rồi publish manifest hoặc siêu dữ liệu (metadata / 메타데이터) lần ghi nhận (commit / 커밋). Nếu đối tượng (object / 객체) lưu trữ (storage / 저장소) không có atomic rename, siêu dữ liệu (metadata / 메타데이터) pointer phải là nguồn chuẩn (source of truth / 정본) về visibility.

Khi thử lại (retry / 재시도), temporary files cũ phải có naming/phiên bản (version / 버전) và garbage-collection chính sách (policy / 정책). Nếu không, reader có thể double-count tệp (file / 파일) hoặc compaction gom cả đầu ra (output / 출력) chưa lần ghi nhận (commit / 커밋).

## 13. Compaction và delete ngữ nghĩa (semantics / 의미론)

Compaction rewrite dữ liệu (data / 데이터) files nhưng không được thay đổi logical kết quả (result / 결과). Cần kiểm tra số row, distinct key, min/max statistics, delete/tombstone và khả năng đọc snapshot cũ trong retention cửa sổ (window / 윈도우). tệp (file / 파일) cũ chỉ được xóa sau khi không còn reader cần.

Delete vật lý và delete lô-gic (logic / 논리) khác nhau. Tombstone bị compaction bỏ qua quá sớm có thể làm bản ghi (record / 레코드) đã xóa “sống lại” khi đọc snapshot cũ hoặc replay.

## 14. lược đồ (schema / 스키마) định danh (identity / 식별자) và kiểu (type / 타입) widening

Lược đồ (schema / 스키마) evolution nên phân biệt add trường dữ liệu (field / 필드), rename, drop và kiểu (type / 타입) widening. `INT → BIGINT` có thể an toàn hơn `STRING → TIMESTAMP`; rename cần trường dữ liệu (field / 필드) định danh (identity / 식별자) hoặc tường minh (explicit / 명시적) di chuyển (migration / 마이그레이션) để reader không coi là drop+add.

Tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) phải kiểm tra writer mới/reader cũ, writer cũ/reader mới và tệp (file / 파일) cũ/tệp (file / 파일) mới. Chỉ kiểm thử (test / 테스트) một hướng là không đủ cho rolling triển khai (deployment / 배포).

> **Bàn giao:** Sau **14. lược đồ (schema / 스키마) định danh (identity / 식별자) và kiểu (type / 타입) widening**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 foundations](./01_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
