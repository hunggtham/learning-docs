# Case Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA
**Database Indexing Case Study / 데이터베이스 인덱스 설계 사례**

Một hệ quản trị cơ sở dữ liệu không chọn cấu trúc dữ liệu bằng cách hỏi “B+Tree có tốt hơn Hash Table không?”. Nó bắt đầu từ **khối lượng công việc (workload)**: loại truy vấn nào xuất hiện nhiều, dữ liệu thay đổi ra sao, kích thước lớn đến mức nào, dữ liệu nằm trong RAM hay trên SSD, và yêu cầu độ trễ có nghiêm ngặt hay không.

Case study này kết nối nhiều chương DSA để trả lời một câu hỏi thực tế:

> Nếu phải thiết kế đường truy cập cho bảng có hàng trăm triệu bản ghi, ta dùng Hash Index, B+Tree, Bloom Filter và Buffer Pool như thế nào để mỗi cấu trúc làm đúng phần việc của nó?

## 1. Bắt đầu từ workload, không bắt đầu từ index

Giả sử có bảng giao dịch:

```text
Transaction(
    transaction_id,
    user_id,
    created_at,
    amount,
    status,
    merchant_id
)
```

Khối lượng công việc giả định:

```text
70%  tra cứu chính xác theo transaction_id
15%  lấy giao dịch của user trong một khoảng thời gian
10%  lấy N giao dịch mới nhất của user
 4%  thống kê theo merchant/status
 1%  insert/update khác
```

Ngay lập tức ta thấy không có một cấu trúc duy nhất tối ưu mọi truy vấn.

Tra cứu chính xác cần **equality lookup**. Truy vấn theo thời gian cần **ordered range scan**. Top-N cần thứ tự. Thống kê có thể cần scan, aggregation hoặc index khác. Đây là lý do hệ thống thật thường duy trì nhiều cấu trúc phụ trợ trên cùng dữ liệu.

## 2. Hash Index cho equality lookup

Nếu chỉ cần:

```sql
SELECT *
FROM transaction
WHERE transaction_id = ?;
```

thì bảng băm có mô hình rất phù hợp:

```text
transaction_id
      ↓ hash
bucket
      ↓
record pointer / tuple location
```

Về mặt DSA, Hash Table cho tra cứu kỳ vọng gần `O(1)` nếu:

```text
hàm băm phân phối đủ tốt
hệ số tải được kiểm soát
va chạm không bị đối kháng
rehash không tạo spike quá lớn
```

Nhưng Hash Index làm mất thứ tự khóa. Nó không trả lời tự nhiên:

```sql
WHERE transaction_id BETWEEN A AND B
ORDER BY transaction_id
```

Đây là giới hạn do bất biến của cấu trúc, không phải do implementation chưa đủ tốt.

## 3. B+Tree cho range query

Một B+Tree duy trì khóa theo thứ tự và có hệ số phân nhánh lớn. Điểm mạnh không chỉ là `O(log n)`.

Trong bộ nhớ ngoài, chi phí chủ yếu có thể là số lần đọc trang. Nếu mỗi nút chứa hàng trăm khóa, cây chứa hàng trăm triệu record vẫn chỉ cao vài tầng.

Mô hình truy vấn:

```text
root page
   ↓
internal page
   ↓
leaf page chứa lower bound
   ↓
quét tuần tự leaf pages
```

Truy vấn:

```sql
WHERE user_id = ?
  AND created_at BETWEEN ? AND ?
```

có thể dùng composite B+Tree:

```text
(user_id, created_at)
```

Thứ tự từ điển tạo ra một vùng liên tục cho cùng `user_id`, sau đó sắp theo `created_at` bên trong vùng đó.

## 4. Tại sao thứ tự cột của composite index quan trọng?

Index:

```text
(user_id, created_at)
```

được sắp như:

```text
(user 1, time 1)
(user 1, time 2)
(user 1, time 3)
(user 2, time 1)
...
```

Nếu đã biết `user_id`, các giá trị `created_at` liên quan nằm trong một khoảng liên tục. Nhưng nếu chỉ biết `created_at` mà không biết `user_id`, các record cùng thời gian có thể nằm rải rác giữa nhiều nhóm user.

Đây chính là **thứ tự từ điển (lexicographic order)** của tuple, không phải một quy tắc bí ẩn riêng của database.

## 5. Top-N và B+Tree

Truy vấn:

```sql
SELECT *
FROM transaction
WHERE user_id = ?
ORDER BY created_at DESC
LIMIT 20;
```

với index phù hợp có thể:

```text
seek tới vị trí cuối của user
đọc ngược 20 phần tử
```

thay vì:

```text
scan mọi giao dịch của user
sort toàn bộ
lấy 20 phần tử đầu
```

Ta đã thay bài toán `sort + top-k` bằng **khai thác thứ tự đã được materialize trong index**.

Bài học chung:

> Nếu một thao tác đắt được lặp lại nhiều lần, có thể đáng để duy trì trước một bất biến giúp thao tác đó rẻ đi.

Đây chính là bản chất của index.

## 6. Chi phí cập nhật của index

Index không miễn phí. Mỗi insert/update/delete phải duy trì thêm cấu trúc.

Ví dụ insert vào B+Tree có thể cần:

```text
tìm leaf phù hợp
chèn record/key
split page nếu đầy
cập nhật parent
có thể lan split lên trên
```

Hash Index có thể cần resize/rehash. Secondary index có thể phải ghi thêm nhiều trang.

Vì vậy hệ thống nhiều index thường có:

```text
đọc nhanh hơn
nhưng ghi chậm hơn
nhiều bộ nhớ/SSD hơn
nhiều write amplification hơn
```

Đây là sự đánh đổi giữa chi phí truy vấn và chi phí duy trì bất biến.

## 7. Covering Index

Nếu truy vấn chỉ cần:

```sql
SELECT created_at, amount
FROM transaction
WHERE user_id = ?
ORDER BY created_at DESC
LIMIT 20;
```

một index có thể chứa thêm `amount` để truy vấn không cần quay về bảng chính.

Về mặt DSA, ta đang tăng metadata trên cấu trúc tìm kiếm để giảm một bước truy cập khác.

Đây cùng nguyên lý với **cây tăng cường (augmented tree)**:

```text
thêm metadata
→ cập nhật đắt hơn / tốn bộ nhớ hơn
→ truy vấn cụ thể nhanh hơn
```

## 8. Clustered và secondary index

Nếu dữ liệu vật lý gần thứ tự index, range scan có locality tốt. Nếu secondary index chỉ chứa pointer tới tuple nằm rải rác, một scan theo index có thể dẫn tới nhiều random reads.

Cùng `O(k)` record output nhưng chi phí vật lý khác nhau lớn vì locality.

Đây là lý do mô hình DSA phải được nối với **memory hierarchy / storage hierarchy**.

## 9. Buffer Pool: cache của database

Database thường không đọc trực tiếp từ SSD cho mỗi query. Nó giữ page trong **buffer pool**.

Mô hình đơn giản:

```text
page_id -> frame trong RAM
```

Cần hai khả năng:

```text
tra cứu page nhanh
quyết định page nào bị đẩy ra khi đầy
```

Một thiết kế kiểu LRU có thể dùng:

```text
Hash Map      -> page_id → frame
Doubly List   -> thứ tự gần đây
```

Nhưng database thực có thể dùng Clock, LRU-K hoặc biến thể khác vì scan lớn có thể làm ô nhiễm LRU đơn giản.

Đây là ví dụ composition giữa Hash Table và cấu trúc thứ tự.

## 10. Bloom Filter trong LSM Tree

LSM Tree thường có nhiều SSTable bất biến. Nếu phải kiểm tra mọi file để biết khóa có tồn tại hay không, tra cứu sẽ tốn nhiều I/O.

Bloom Filter cho mỗi SSTable trả lời:

```text
chắc chắn không có
hoặc
có thể có
```

Nếu Bloom nói “không có”, có thể bỏ qua file. Nếu “có thể có”, mới đọc index/data thật.

Dương tính giả chỉ làm thêm I/O; không làm sai kết quả cuối cùng.

Đây là cách một cấu trúc xác suất được đặt trước một cấu trúc chính xác để giảm chi phí trung bình.

## 11. B+Tree và LSM Tree tối ưu hai workload khác nhau

B+Tree cập nhật trực tiếp cấu trúc có thứ tự theo page. LSM Tree gom ghi trong memory rồi flush tuần tự thành các run đã sắp xếp, sau đó compaction nền.

Có thể nhìn như:

```text
B+Tree:
  trả chi phí cập nhật tại thời điểm ghi

LSM:
  gom/batch ghi trước
  trả chi phí merge/compaction về sau
```

Đây là sự khác nhau về cách phân phối chi phí theo thời gian, gần với tư duy khấu hao.

LSM phù hợp workload ghi lớn; B+Tree thường mạnh khi cần range query và đọc ổn định với ít read amplification hơn.

## 12. Hash Join và Sort-Merge Join

Index không phải nơi duy nhất DSA xuất hiện trong database.

Với equality join:

```sql
A JOIN B ON A.user_id = B.user_id
```

Hash Join có thể:

```text
build Hash Table trên phía nhỏ
scan phía lớn
probe từng khóa
```

Nếu hai phía đã có thứ tự theo join key, Sort-Merge Join có thể quét tuyến tính bằng hai con trỏ.

Việc chọn join algorithm là bài toán chọn cấu trúc/thuật toán theo kích thước, thứ tự và bộ nhớ hiện có.

## 13. Query Optimizer là bài toán tìm kiếm

Một query nhiều bảng có nhiều join order khác nhau. Với `n` bảng, số kế hoạch có thể tăng rất nhanh.

Optimizer có thể dùng:

```text
Dynamic Programming
memoization
branch-and-bound style pruning
cost model
statistics
```

Tức là ngay cả việc **chọn thuật toán** cũng trở thành một bài toán DSA.

## 14. Case: thiết kế index cho workload ban đầu

Quay lại workload:

```text
70% exact lookup by transaction_id
15% user + time range
10% latest-N by user
 4% aggregation
 1% writes khác
```

Một thiết kế khả thi:

```text
Primary/unique index:
    transaction_id

Ordered secondary index:
    (user_id, created_at DESC)

Analytics path:
    index/columnar/aggregation riêng tùy workload
```

Nếu hệ thống đọc rất nhiều theo `transaction_id`, hash-based path có thể hữu ích. Nhưng nếu engine đã có B+Tree primary index đủ nhanh và cần đơn giản hóa hệ thống, thêm Hash Index riêng chưa chắc đáng giá.

Đây là bài học quan trọng: **DSA cho tập ứng viên, workload và cost model quyết định lựa chọn cuối cùng**.

## 15. Khi nào một index không còn đáng giá?

Một index có thể phản tác dụng nếu:

```text
cột có độ chọn lọc quá thấp
query hiếm khi dùng
bảng nhỏ đến mức scan rẻ hơn
write amplification quá lớn
index không vừa bộ nhớ và tạo thêm random I/O
statistics sai làm optimizer chọn plan tệ
```

Không nên đánh giá index chỉ từ Big-O của lookup.

## 16. Invariant và crash consistency

Trong bộ nhớ, một cấu trúc chỉ cần giữ bất biến logic. Trong database bền vững, phải giữ thêm:

```text
trạng thái trên đĩa có thể phục hồi sau crash
page split không để index ở trạng thái nửa cập nhật
WAL/redo/undo đủ để khôi phục
```

Một B+Tree đúng về mặt thuật toán nhưng không có protocol ghi bền vững vẫn chưa đủ cho hệ quản trị dữ liệu thật.

Đây là ranh giới giữa DSA thuần và systems engineering.

## 17. Cách kiểm thử

Không chỉ kiểm tra query trả đúng. Cần kiểm tra:

```text
insert/delete ngẫu nhiên và đối chiếu với mô hình đơn giản
range scan có đúng thứ tự và không mất/trùng record
split/merge page có giữ invariant
index và bảng chính có cùng tập khóa
crash/recovery ở các điểm giữa cập nhật
Bloom Filter không có false negative trong mô hình hỗ trợ
```

Benchmark nên thay đổi:

```text
read/write ratio
data size
cache hit ratio
selectivity
range length
page size
concurrency
```

## 18. Chuỗi suy luận hoàn chỉnh

```text
Yêu cầu nghiệp vụ
    ↓
Các thao tác nóng
    ↓
Bất biến cần materialize
    ↓
Cấu trúc dữ liệu
    ↓
Cách bố trí theo page/cache
    ↓
Chi phí cập nhật và persistence
    ↓
Benchmark workload thật
```

Đó là cách kiến thức Hash Table, B+Tree, Bloom Filter, LRU, sorting, two pointers và cost model kết nối thành một thiết kế database thực tế.

## Mô hình tư duy

> **Index là một cấu trúc dữ liệu được duy trì trước để mua lại tốc độ truy vấn trong tương lai.** Cái giá phải trả là bộ nhớ, I/O, write amplification và complexity khi cập nhật. Không có index tốt tuyệt đối; chỉ có index phù hợp với tập thao tác và tầng lưu trữ cụ thể.

Xem thêm: [Hash Tables](../01_linear_structures/04_hash_tables.md), [B/B+Tree & External Memory](../02_trees/05_b_trees_and_external_memory.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [DSA in Systems](./01_dsa_in_databases_networks_and_systems.md).