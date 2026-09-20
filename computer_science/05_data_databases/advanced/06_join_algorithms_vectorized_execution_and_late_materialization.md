# Thuật toán join, thực thi vector hóa và vật chất hóa muộn

Một hệ quản trị cơ sở dữ liệu không dừng ở việc chọn một kế hoạch truy vấn. Sau khi bộ tối ưu (optimizer) quyết định thứ tự bảng, index và phép toán, **bộ máy thực thi truy vấn (query execution engine / 질의 실행 엔진)** phải biến kế hoạch đó thành công việc CPU, truy cập bộ nhớ và I/O cụ thể. Hai kế hoạch có cùng độ phức tạp Big-O vẫn có thể khác nhau hàng chục lần vì locality, số lần gọi hàm, branch prediction, kích thước dữ liệu trung gian và cách dữ liệu đi qua cache CPU.

Chapter này nối trực tiếp với [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md): optimizer trả lời “nên làm gì”, còn execution engine trả lời “thực hiện nó trên phần cứng như thế nào”.

## 1. Join thực chất là bài toán tìm quan hệ giữa hai tập bản ghi

Với truy vấn:

```sql
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

hệ thống cần ghép mỗi `orders.customer_id` với bản ghi `customers.id` tương ứng. Cách ngây thơ là so từng order với mọi customer, tạo chi phí gần `O(N×M)`. Các thuật toán join tồn tại để khai thác cấu trúc của dữ liệu: thứ tự, index, hàm băm hoặc khả năng giữ dữ liệu trong bộ nhớ.

### Nested-loop join

**Vòng lặp lồng nhau (nested-loop join)** lấy từng hàng phía ngoài rồi tìm hàng phù hợp phía trong. Nếu phía trong có index tốt, đây có thể là lựa chọn rất mạnh:

```text
for each outer row:
    probe inner index
```

Chi phí không chỉ phụ thuộc số hàng mà còn phụ thuộc số lần probe, chiều cao index, cache hit và việc truy cập có ngẫu nhiên hay không. Với outer nhỏ và inner có index chọn lọc, nested-loop thường hợp lý. Với hai bảng lớn và không có index phù hợp, nó có thể trở thành thảm họa.

### Hash join

**Ghép nối bằng băm (hash join)** thường xây bảng băm từ phía nhỏ hơn rồi dò phía còn lại:

```text
build: small relation -> hash table
probe: large relation -> hash lookup
```

Trong trường hợp lý tưởng, chi phí gần tuyến tính theo tổng số hàng. Nhưng “O(N+M)” không có nghĩa là miễn phí: bảng băm cần bộ nhớ, có thể gây cache miss, collision và phải spill ra storage nếu vượt memory budget.

Khi dữ liệu không vừa RAM, hệ thống có thể partition hai phía theo hash rồi xử lý từng partition. Lúc đó hiệu năng phụ thuộc mạnh vào I/O và độ lệch khóa (data skew). Một khóa xuất hiện cực nhiều có thể tạo partition quá lớn dù tổng dữ liệu nhìn chung cân bằng.

### Sort-merge join

**Ghép nối sắp xếp–trộn (sort-merge join)** sắp hai đầu vào theo khóa rồi quét đồng thời. Nếu dữ liệu đã có thứ tự từ index hoặc từ operator trước đó, chi phí sort có thể biến mất. Thuật toán này cũng phù hợp với range condition hơn hash join trong một số trường hợp.

Điểm quan trọng là không có “join tốt nhất”. Optimizer phải ước lượng cardinality, distribution, ordering và memory budget để chọn thuật toán phù hợp.

## 2. Build side và probe side không phải chi tiết nhỏ

Trong hash join, phía được dùng để xây hash table gọi là **phía xây dựng (build side)**; phía còn lại là **phía dò tìm (probe side)**. Thường muốn build side nhỏ hơn để giảm memory footprint.

Nếu optimizer ước lượng sai rằng bảng A có 10 nghìn hàng trong khi thực tế có 100 triệu hàng, nó có thể chọn A làm build side. Kế hoạch về mặt logic vẫn đúng nhưng runtime có thể spill hàng GB dữ liệu ra đĩa. Đây là ví dụ rõ về connection giữa statistics, cardinality estimation và execution behavior.

## 3. Volcano model: đơn giản nhưng có overhead

Nhiều execution engine truyền thống dùng **mô hình iterator (iterator/Volcano model)**. Mỗi operator cung cấp thao tác kiểu `next()`:

```text
Project.next()
  -> Filter.next()
       -> Scan.next()
```

Thiết kế này modular và dễ kết hợp operator. Tuy nhiên, xử lý từng tuple tạo nhiều lời gọi hàm, virtual dispatch, branch và ít cơ hội dùng SIMD. Khi truy vấn phân tích phải xử lý hàng trăm triệu giá trị, overhead trên mỗi tuple trở nên đáng kể.

## 4. Thực thi vector hóa

**Thực thi vector hóa (vectorized execution / 벡터화 실행)** xử lý một batch gồm nhiều giá trị thay vì một hàng mỗi lần:

```text
scan 1024 values
filter 1024 values
aggregate selected values
```

Batch đủ lớn giúp giảm overhead điều phối và tăng locality, nhưng không quá lớn đến mức phá cache. Các vòng lặp đơn giản trên mảng liên tục cũng giúp compiler tận dụng SIMD.

Ví dụ, thay vì gọi một hàm filter một triệu lần, engine có thể chạy một vòng lặp chặt trên một vector giá trị. CPU hiện đại rất giỏi kiểu công việc này vì prefetcher, cache line và SIMD đều thích dữ liệu liên tục.

> Mental model: vectorization không làm thay đổi logic SQL; nó thay đổi **đơn vị công việc (unit of work)** từ một tuple thành một batch phù hợp hơn với phần cứng.

## 5. Selection vector

Sau filter, engine không nhất thiết sao chép các hàng đạt điều kiện sang buffer mới. Nó có thể giữ một **vector lựa chọn (selection vector)** chứa chỉ số các phần tử còn sống:

```text
values:    [8, 3, 11, 2, 20]
condition: value > 10
selection: [2, 4]
```

Operator tiếp theo chỉ xử lý vị trí 2 và 4. Cách này giảm sao chép dữ liệu nhưng tạo thêm indirection. Nếu selectivity rất cao hoặc rất thấp, chiến lược tối ưu có thể khác nhau.

## 6. Vật chất hóa muộn

Trong hệ thống hướng cột, **vật chất hóa muộn (late materialization)** trì hoãn việc ghép các cột thành bản ghi đầy đủ. Nếu truy vấn chỉ cần lọc `age` rồi tính tổng `salary`, engine không cần dựng object chứa mọi column của từng row ngay từ đầu.

```text
scan age
  ↓
filter positions
  ↓
fetch salary only for selected positions
  ↓
aggregate
```

Điều này giảm memory bandwidth — một tài nguyên thường quan trọng hơn số phép toán số học trong analytical workload.

Ngược lại, vật chất hóa quá muộn có thể làm tăng random access khi cần lấy nhiều cột ở giai đoạn cuối. Vì vậy đây vẫn là một đánh đổi (trade-off), không phải quy tắc tuyệt đối.

## 7. Pipeline và pipeline breaker

Các operator như filter và projection có thể truyền dữ liệu liên tục qua **đường ống (pipeline)**. Nhưng sort thường phải nhìn thấy toàn bộ input trước khi trả kết quả; hash aggregate hoặc hash join cũng cần xây state trước một số giai đoạn. Những operator như vậy tạo **điểm ngắt đường ống (pipeline breaker)**.

Pipeline breaker ảnh hưởng memory, latency và khả năng song song. Một query plan không chỉ là cây operator; nó còn là đồ thị các giai đoạn có thể stream và các điểm buộc phải materialize state.

## 8. Spill khi bộ nhớ không đủ

Database không thể giả định mọi hash table hoặc sort buffer đều vừa RAM. Khi vượt memory quota, engine phải **tràn ra lưu trữ (spill to storage)**.

Một external sort thường tạo các run đã sắp xếp rồi merge. Hash join có thể partition dữ liệu sao cho từng partition nhỏ hơn memory budget. Spill làm tăng latency mạnh vì đường đi chuyển từ cache/RAM sang storage.

Do đó memory limit cho một query là vấn đề quản trị tài nguyên, không chỉ là cấu hình hiệu năng. Cho một query quá nhiều RAM có thể làm query đó nhanh hơn nhưng khiến các query khác hoặc OS rơi vào memory pressure.

## 9. Data skew phá giả định trung bình

Nếu `customer_id=1` chiếm 40% orders, hash partition theo `customer_id` không cân bằng. Một worker có thể nhận phần lớn dữ liệu trong khi các worker khác rảnh.

Đây là **độ lệch dữ liệu (data skew)**. Distributed query engine thường cần kỹ thuật như phát hiện heavy hitter, repartition đặc biệt hoặc broadcast phía nhỏ. Average cardinality không mô tả được tail behavior này.

## 10. Row engine và columnar engine

OLTP thường truy cập vài hàng nhưng nhiều cột và cần cập nhật nhanh; layout theo hàng phù hợp vì một record nằm gần nhau. OLAP thường quét rất nhiều hàng nhưng chỉ vài cột; columnar layout giảm lượng byte phải đọc và nén tốt hơn.

Execution engine thường phản ánh workload này. Row-oriented engine có thể ưu tiên latency của point lookup; analytical engine ưu tiên batch, SIMD, compression và parallel scan.

## 11. Parallel query execution

Một scan lớn có thể chia thành nhiều morsel hoặc partition cho nhiều worker. Nhưng song song không miễn phí. Cần phân phối công việc, đồng bộ, merge kết quả và kiểm soát memory.

Nếu query chỉ mất 2 ms, tạo thêm nhiều task có thể tốn hơn phần tính toán được tiết kiệm. Nếu query quét 500 GB, parallelism lại là điều thiết yếu. Vì vậy degree of parallelism phải gắn với kích thước công việc và tài nguyên toàn hệ thống.

## 12. Quan sát execution engine trong thực tế

Khi `EXPLAIN` hoặc execution plan cho thấy một query chậm, đừng chỉ nhìn “có dùng index hay không”. Cần hỏi:

- cardinality ước lượng khác thực tế bao nhiêu;
- join nào đang build và probe phía nào;
- operator có spill không;
- sort/hash dùng bao nhiêu memory;
- số row bị loại ở từng stage;
- thời gian nằm ở CPU, I/O hay chờ lock;
- parallel workers có cân bằng hay bị skew.

Những câu hỏi này nối optimizer với runtime evidence.

## Common Misconceptions

**“Hash join luôn nhanh hơn nested-loop.”** Không đúng. Nested-loop với outer nhỏ và indexed inner có thể cực kỳ hiệu quả.

**“Query có Big-O tốt thì execution sẽ nhanh.”** Big-O bỏ qua cache locality, branch, SIMD, allocation, memory bandwidth và spill.

**“Vectorization nghĩa là GPU.”** Không. Vectorized execution thường chạy trên CPU và xử lý dữ liệu theo batch; SIMD chỉ là một khả năng tối ưu thêm.

**“Thêm RAM luôn giải quyết query chậm.”** RAM có thể giảm spill, nhưng cardinality sai, skew, lock contention hoặc plan xấu vẫn tồn tại.

## Mental Model

> Optimizer tạo chiến lược; execution engine biến chiến lược đó thành luồng byte và phép toán trên phần cứng.

Muốn hiểu hiệu năng database ở mức sâu, phải theo dõi cùng lúc ba lớp: **đại số quan hệ và plan**, **cấu trúc dữ liệu/runtime operator**, và **CPU–memory–storage thực tế**.

Xem tiếp: [Distributed transactions](./07_distributed_transactions_2pc_consensus_sagas_and_outbox.md) và [Computer Architecture](../../02_computer_architecture/advanced/README.md).
