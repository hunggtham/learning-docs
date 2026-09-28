# Thuật toán phép nối (join / 조인), thực thi véc-tơ (vector / 벡터) hóa và vật chất hóa muộn

> **Mạch đọc:** Đặt **Thuật toán phép nối (join / 조인), thực thi véc-tơ (vector / 벡터) hóa và vật chất hóa muộn** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. phép nối (join / 조인) thực chất là bài toán tìm quan hệ giữa hai tập bản ghi** sang **Nested-loop phép nối (join / 조인)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một hệ quản trị cơ sở dữ liệu không dừng ở việc chọn một kế hoạch truy vấn. Sau khi bộ tối ưu (optimizer) quyết định thứ tự bảng, chỉ mục (index / 인덱스) và phép toán, **bộ máy thực thi truy vấn (query execution engine / 질의 실행 엔진)** phải biến kế hoạch đó thành công việc CPU, truy cập bộ nhớ và I/O cụ thể. Hai kế hoạch có cùng độ phức tạp Big-O vẫn có thể khác nhau hàng chục lần vì locality, số lần gọi hàm, branch prediction, kích thước dữ liệu trung gian và cách dữ liệu đi qua bộ nhớ đệm (cache / 캐시) CPU.

Chapter này nối trực tiếp với [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md): optimizer trả lời “nên làm gì”, còn thực thi (execution / 실행) engine trả lời “thực hiện nó trên phần cứng như thế nào”.

## 1. phép nối (join / 조인) thực chất là bài toán tìm quan hệ giữa hai tập bản ghi

Với truy vấn:

```sql
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

hệ thống cần ghép mỗi `orders.customer_id` với bản ghi `customers.id` tương ứng. Cách ngây thơ là so từng thứ tự (order / 순서) với mọi customer, tạo chi phí gần `O(N×M)`. Các thuật toán phép nối (join / 조인) tồn tại để khai thác cấu trúc của dữ liệu: thứ tự, chỉ mục (index / 인덱스), hàm băm hoặc khả năng giữ dữ liệu trong bộ nhớ.

### Nested-loop phép nối (join / 조인)

**Vòng lặp lồng nhau (nested-loop join)** lấy từng hàng phía ngoài rồi tìm hàng phù hợp phía trong. Nếu phía trong có chỉ mục (index / 인덱스) tốt, đây có thể là lựa chọn rất mạnh:

```text
for each outer row:
    probe inner index
```

Chi phí không chỉ phụ thuộc số hàng mà còn phụ thuộc số lần probe, chiều cao chỉ mục (index / 인덱스), bộ nhớ đệm (cache / 캐시) hit và việc truy cập có ngẫu nhiên hay không. Với outer nhỏ và inner có chỉ mục (index / 인덱스) chọn lọc, nested-loop thường hợp lý. Với hai bảng lớn và không có chỉ mục (index / 인덱스) phù hợp, nó có thể trở thành thảm họa.

### Băm (hash / 해시) phép nối (join / 조인)

**Ghép nối bằng băm (hash join)** thường xây bảng băm từ phía nhỏ hơn rồi dò phía còn lại:

```text
build: small relation -> hash table
probe: large relation -> hash lookup
```

Trong trường hợp lý tưởng, chi phí gần tuyến tính theo tổng số hàng. Nhưng “O(N+M)” không có nghĩa là miễn phí: bảng băm cần bộ nhớ, có thể gây trượt bộ nhớ đệm (cache miss / 캐시 미스), collision và phải spill ra lưu trữ (storage / 저장소) nếu vượt bộ nhớ (memory / 메모리) ngân sách (budget / 예산).

Khi dữ liệu không vừa RAM, hệ thống có thể partition hai phía theo băm (hash / 해시) rồi xử lý từng partition. Lúc đó hiệu năng phụ thuộc mạnh vào I/O và độ lệch khóa (data skew). Một khóa xuất hiện cực nhiều có thể tạo partition quá lớn dù tổng dữ liệu nhìn chung cân bằng.

### Sort-merge phép nối (join / 조인)

**Ghép nối sắp xếp–trộn (sort-merge join)** sắp hai đầu vào theo khóa rồi quét đồng thời. Nếu dữ liệu đã có thứ tự từ chỉ mục (index / 인덱스) hoặc từ operator trước đó, chi phí sort có thể biến mất. Thuật toán này cũng phù hợp với phạm vi (range / 범위) điều kiện (condition / 조건) hơn băm (hash / 해시) phép nối (join / 조인) trong một số trường hợp.

Điểm quan trọng là không có “phép nối (join / 조인) tốt nhất”. Optimizer phải ước lượng cardinality, phân phối (distribution / 분포), thứ tự (ordering / 순서) và bộ nhớ (memory / 메모리) ngân sách (budget / 예산) để chọn thuật toán phù hợp.

## 2. bản dựng (build / 빌드) side và probe side không phải chi tiết nhỏ

Trong băm (hash / 해시) phép nối (join / 조인), phía được dùng để xây bảng băm (hash table / 해시 테이블) gọi là **phía xây dựng (build side)**; phía còn lại là **phía dò tìm (probe side)**. Thường muốn bản dựng (build / 빌드) side nhỏ hơn để giảm bộ nhớ (memory / 메모리) footprint.

Nếu optimizer ước lượng sai rằng bảng A có 10 nghìn hàng trong khi thực tế có 100 triệu hàng, nó có thể chọn A làm bản dựng (build / 빌드) side. Kế hoạch về mặt lô-gic (logic / 논리) vẫn đúng nhưng thời gian chạy (runtime / 런타임) có thể spill hàng GB dữ liệu ra đĩa. Đây là ví dụ rõ về liên kết (connection / 연결) giữa statistics, cardinality estimation và thực thi (execution / 실행) hành vi (behavior / 동작).

## 3. Volcano mô hình (model / 모델): đơn giản nhưng có overhead

Nhiều thực thi (execution / 실행) engine truyền thống dùng **mô hình iterator (iterator/Volcano model)**. Mỗi operator cung cấp thao tác kiểu `next()`:

```text
Project.next()
  -> Filter.next()
       -> Scan.next()
```

Thiết kế này modular và dễ kết hợp operator. Tuy nhiên, xử lý từng tuple tạo nhiều lời gọi hàm, virtual dispatch, branch và ít cơ hội dùng SIMD. Khi truy vấn phân tích phải xử lý hàng trăm triệu giá trị, overhead trên mỗi tuple trở nên đáng kể.

## 4. Thực thi véc-tơ (vector / 벡터) hóa

**Thực thi véc-tơ (vector / 벡터) hóa (vectorized execution / 벡터화 실행)** xử lý một batch gồm nhiều giá trị thay vì một hàng mỗi lần:

```text
scan 1024 values
filter 1024 values
aggregate selected values
```

Batch đủ lớn giúp giảm overhead điều phối và tăng locality, nhưng không quá lớn đến mức phá bộ nhớ đệm (cache / 캐시). Các vòng lặp đơn giản trên mảng liên tục cũng giúp trình biên dịch (compiler / 컴파일러) tận dụng SIMD.

Ví dụ, thay vì gọi một hàm filter một triệu lần, engine có thể chạy một vòng lặp chặt trên một véc-tơ (vector / 벡터) giá trị. CPU hiện đại rất giỏi kiểu công việc này vì prefetcher, bộ nhớ đệm (cache / 캐시) line và SIMD đều thích dữ liệu liên tục.

> mô hình tư duy (mental model / 사고 모델): vectorization không làm thay đổi lô-gic (logic / 논리) SQL; nó thay đổi **đơn vị công việc (unit of work)** từ một tuple thành một batch phù hợp hơn với phần cứng.

## 5. Selection véc-tơ (vector / 벡터)

Sau filter, engine không nhất thiết sao chép các hàng đạt điều kiện sang buffer mới. Nó có thể giữ một **véc-tơ (vector / 벡터) lựa chọn (selection vector)** chứa chỉ số các phần tử còn sống:

```text
values:    [8, 3, 11, 2, 20]
condition: value > 10
selection: [2, 4]
```

Operator tiếp theo chỉ xử lý vị trí 2 và 4. Cách này giảm sao chép dữ liệu nhưng tạo thêm indirection. Nếu selectivity rất cao hoặc rất thấp, chiến lược tối ưu có thể khác nhau.

## 6. Vật chất hóa muộn

Trong hệ thống hướng cột, **vật chất hóa muộn (late materialization)** trì hoãn việc ghép các cột thành bản ghi đầy đủ. Nếu truy vấn chỉ cần lọc `age` rồi tính tổng `salary`, engine không cần dựng đối tượng (object / 객체) chứa mọi column của từng row ngay từ đầu.

```text
scan age
  ↓
filter positions
  ↓
fetch salary only for selected positions
  ↓
aggregate
```

Điều này giảm bộ nhớ (memory / 메모리) bandwidth — một tài nguyên thường quan trọng hơn số phép toán số học trong analytical tải công việc (workload / 워크로드).

Ngược lại, vật chất hóa quá muộn có thể làm tăng random truy cập (access / 접근) khi cần lấy nhiều cột ở giai đoạn cuối. Vì vậy đây vẫn là một đánh đổi (trade-off), không phải quy tắc tuyệt đối.

## 7. chuỗi xử lý (pipeline / 파이프라인) và chuỗi xử lý (pipeline / 파이프라인) breaker

Các operator như filter và projection có thể truyền dữ liệu liên tục qua **đường ống (pipeline)**. Nhưng sort thường phải nhìn thấy toàn bộ đầu vào (input / 입력) trước khi trả kết quả; băm (hash / 해시) aggregate hoặc băm (hash / 해시) phép nối (join / 조인) cũng cần xây trạng thái (state / 상태) trước một số giai đoạn. Những operator như vậy tạo **điểm ngắt đường ống (pipeline breaker)**.

Chuỗi xử lý (pipeline / 파이프라인) breaker ảnh hưởng bộ nhớ (memory / 메모리), độ trễ (latency / 지연 시간) và khả năng song song. Một kế hoạch truy vấn (query plan / 쿼리 계획) không chỉ là cây operator; nó còn là đồ thị các giai đoạn có thể stream và các điểm buộc phải materialize trạng thái (state / 상태).

## 8. Spill khi bộ nhớ không đủ

Cơ sở dữ liệu (database / 데이터베이스) không thể giả định mọi bảng băm (hash table / 해시 테이블) hoặc sort buffer đều vừa RAM. Khi vượt bộ nhớ (memory / 메모리) quota, engine phải **tràn ra lưu trữ (spill to storage)**.

Một bên ngoài (external / 외부) sort thường tạo các run đã sắp xếp rồi merge. băm (hash / 해시) phép nối (join / 조인) có thể partition dữ liệu sao cho từng partition nhỏ hơn bộ nhớ (memory / 메모리) ngân sách (budget / 예산). Spill làm tăng độ trễ (latency / 지연 시간) mạnh vì đường đi chuyển từ bộ nhớ đệm (cache / 캐시)/RAM sang lưu trữ (storage / 저장소).

Do đó giới hạn bộ nhớ (memory limit / 메모리 제한) cho một truy vấn (query / 쿼리) là vấn đề quản trị tài nguyên, không chỉ là cấu hình hiệu năng. Cho một truy vấn (query / 쿼리) quá nhiều RAM có thể làm truy vấn (query / 쿼리) đó nhanh hơn nhưng khiến các truy vấn (query / 쿼리) khác hoặc OS rơi vào bộ nhớ (memory / 메모리) pressure.

## 9. dữ liệu (data / 데이터) skew phá giả định trung bình

Nếu `customer_id=1` chiếm 40% orders, băm (hash / 해시) partition theo `customer_id` không cân bằng. Một worker có thể nhận phần lớn dữ liệu trong khi các worker khác rảnh.

Đây là **độ lệch dữ liệu (data skew)**. phân tán (distributed / 분산) truy vấn (query / 쿼리) engine thường cần kỹ thuật như phát hiện heavy hitter, repartition đặc biệt hoặc broadcast phía nhỏ. Average cardinality không mô tả được tail hành vi (behavior / 동작) này.

## 10. Row engine và columnar engine

OLTP thường truy cập vài hàng nhưng nhiều cột và cần cập nhật nhanh; bố cục (layout / 레이아웃) theo hàng phù hợp vì một bản ghi (record / 레코드) nằm gần nhau. OLAP thường quét rất nhiều hàng nhưng chỉ vài cột; columnar bố cục (layout / 레이아웃) giảm lượng byte phải đọc và nén tốt hơn.

Thực thi (execution / 실행) engine thường phản ánh tải công việc (workload / 워크로드) này. Row-oriented engine có thể ưu tiên độ trễ (latency / 지연 시간) của điểm (point / 지점) lookup; analytical engine ưu tiên batch, SIMD, compression và parallel scan.

## 11. Parallel truy vấn (query / 쿼리) thực thi (execution / 실행)

Một scan lớn có thể chia thành nhiều morsel hoặc partition cho nhiều worker. Nhưng song song không miễn phí. Cần phân phối công việc, đồng bộ, merge kết quả và kiểm soát bộ nhớ (memory / 메모리).

Nếu truy vấn (query / 쿼리) chỉ mất 2 ms, tạo thêm nhiều tác vụ (task / 작업) có thể tốn hơn phần tính toán được tiết kiệm. Nếu truy vấn (query / 쿼리) quét 500 GB, parallelism lại là điều thiết yếu. Vì vậy degree of parallelism phải gắn với kích thước công việc và tài nguyên toàn hệ thống.

## 12. Quan sát thực thi (execution / 실행) engine trong thực tế

Khi `EXPLAIN` hoặc thực thi (execution / 실행) plan cho thấy một truy vấn (query / 쿼리) chậm, đừng chỉ nhìn “có dùng chỉ mục (index / 인덱스) hay không”. Cần hỏi:

- cardinality ước lượng khác thực tế bao nhiêu;
- phép nối (join / 조인) nào đang bản dựng (build / 빌드) và probe phía nào;
- operator có spill không;
- sort/băm (hash / 해시) dùng bao nhiêu bộ nhớ (memory / 메모리);
- số row bị loại ở từng stage;
- thời gian nằm ở CPU, I/O hay chờ khóa (lock / 잠금);
- parallel workers có cân bằng hay bị skew.

Những câu hỏi này nối optimizer với thời gian chạy (runtime / 런타임) bằng chứng (evidence / 증거).

## Dùng chung (common / 공통) Misconceptions

**“băm (hash / 해시) phép nối (join / 조인) luôn nhanh hơn nested-loop.”** Không đúng. Nested-loop với outer nhỏ và indexed inner có thể cực kỳ hiệu quả.

**“truy vấn (query / 쿼리) có Big-O tốt thì thực thi (execution / 실행) sẽ nhanh.”** Big-O bỏ qua bộ nhớ đệm (cache / 캐시) locality, branch, SIMD, allocation, bộ nhớ (memory / 메모리) bandwidth và spill.

**“Vectorization nghĩa là GPU.”** Không. Vectorized thực thi (execution / 실행) thường chạy trên CPU và xử lý dữ liệu theo batch; SIMD chỉ là một khả năng tối ưu thêm.

**“Thêm RAM luôn giải quyết truy vấn (query / 쿼리) chậm.”** RAM có thể giảm spill, nhưng cardinality sai, skew, tranh chấp khóa (lock contention / 잠금 경합) hoặc plan xấu vẫn tồn tại.

## Mô hình tư duy (mental model / 사고 모델)

> Optimizer tạo chiến lược; thực thi (execution / 실행) engine biến chiến lược đó thành luồng byte và phép toán trên phần cứng.

Muốn hiểu hiệu năng cơ sở dữ liệu (database / 데이터베이스) ở mức sâu, phải theo dõi cùng lúc ba lớp: **đại số quan hệ và plan**, **cấu trúc dữ liệu/thời gian chạy (runtime / 런타임) operator**, và **CPU–bộ nhớ (memory / 메모리)–lưu trữ (storage / 저장소) thực tế**.

Xem tiếp: [Distributed transactions](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Computer Architecture](../../02_computer_architecture/advanced/README.md).

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mvcc visibility wal and recovery internals](./00_mvcc_visibility_wal_and_recovery_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
