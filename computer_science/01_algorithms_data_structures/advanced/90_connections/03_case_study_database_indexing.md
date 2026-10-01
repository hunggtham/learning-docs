# Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ chỉ mục (index / 인덱스)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. băm (hash / 해시) chỉ mục (index / 인덱스) cho equality lookup** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**cơ sở dữ liệu (database / 데이터베이스) Indexing trường hợp (case / 사례) Study / 데이터베이스 인덱스 설계 사례**

Một hệ quản trị cơ sở dữ liệu không chọn cấu trúc dữ liệu bằng cách hỏi “B+cây (tree / 트리) có tốt hơn bảng băm (hash table / 해시 테이블) không?”. Nó bắt đầu từ **khối lượng công việc (workload)**: loại truy vấn nào xuất hiện nhiều, dữ liệu thay đổi ra sao, kích thước lớn đến mức nào, dữ liệu nằm trong RAM hay trên SSD, và yêu cầu độ trễ có nghiêm ngặt hay không.

Trường hợp (case / 사례) study này kết nối nhiều chương DSA để trả lời một câu hỏi thực tế:

> Nếu phải thiết kế đường truy cập cho bảng có hàng trăm triệu bản ghi, ta dùng băm (hash / 해시) chỉ mục (index / 인덱스), B+cây (tree / 트리), Bloom Filter và Buffer Pool như thế nào để mỗi cấu trúc làm đúng phần việc của nó?

## 1. Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ chỉ mục (index / 인덱스)

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

Tra cứu chính xác cần **equality lookup**. Truy vấn theo thời gian cần **ordered phạm vi (range / 범위) scan**. Top-N cần thứ tự. Thống kê có thể cần scan, aggregation hoặc chỉ mục (index / 인덱스) khác. Đây là lý do hệ thống thật thường duy trì nhiều cấu trúc phụ trợ trên cùng dữ liệu.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **2. băm (hash / 해시) chỉ mục (index / 인덱스) cho equality lookup** tiếp nhận điểm tựa từ **1. Bắt đầu từ tải công việc (workload / 워크로드), không bắt đầu từ chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. B+cây (tree / 트리) cho phạm vi (range / 범위) truy vấn (query / 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. băm (hash / 해시) chỉ mục (index / 인덱스) cho equality lookup

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

Về mặt DSA, bảng băm (hash table / 해시 테이블) cho tra cứu kỳ vọng gần `O(1)` nếu:

```text
hàm băm phân phối đủ tốt
hệ số tải được kiểm soát
va chạm không bị đối kháng
rehash không tạo spike quá lớn
```

Nhưng băm (hash / 해시) chỉ mục (index / 인덱스) làm mất thứ tự khóa. Nó không trả lời tự nhiên:

```sql
WHERE transaction_id BETWEEN A AND B
ORDER BY transaction_id
```

Đây là giới hạn do bất biến của cấu trúc, không phải do hiện thực (implementation / 구현) chưa đủ tốt.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **3. B+cây (tree / 트리) cho phạm vi (range / 범위) truy vấn (query / 쿼리)** tiếp nhận điểm tựa từ **2. băm (hash / 해시) chỉ mục (index / 인덱스) cho equality lookup** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Tại sao thứ tự cột của composite chỉ mục (index / 인덱스) quan trọng?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. B+cây (tree / 트리) cho phạm vi (range / 범위) truy vấn (query / 쿼리)

Một B+cây (tree / 트리) duy trì khóa theo thứ tự và có hệ số phân nhánh lớn. Điểm mạnh không chỉ là `O(log n)`.

Trong bộ nhớ ngoài, chi phí chủ yếu có thể là số lần đọc trang. Nếu mỗi nút chứa hàng trăm khóa, cây chứa hàng trăm triệu bản ghi (record / 레코드) vẫn chỉ cao vài tầng.

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

có thể dùng composite B+cây (tree / 트리):

```text
(user_id, created_at)
```

Thứ tự từ điển tạo ra một vùng liên tục cho cùng `user_id`, sau đó sắp theo `created_at` bên trong vùng đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **4. Tại sao thứ tự cột của composite chỉ mục (index / 인덱스) quan trọng?** tiếp nhận điểm tựa từ **3. B+cây (tree / 트리) cho phạm vi (range / 범위) truy vấn (query / 쿼리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Top-N và B+cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Tại sao thứ tự cột của composite chỉ mục (index / 인덱스) quan trọng?

Chỉ mục (index / 인덱스):

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

Nếu đã biết `user_id`, các giá trị `created_at` liên quan nằm trong một khoảng liên tục. Nhưng nếu chỉ biết `created_at` mà không biết `user_id`, các bản ghi (record / 레코드) cùng thời gian có thể nằm rải rác giữa nhiều nhóm người dùng (user / 사용자).

Đây chính là **thứ tự từ điển (lexicographic order)** của tuple, không phải một quy tắc bí ẩn riêng của cơ sở dữ liệu (database / 데이터베이스).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **5. Top-N và B+cây (tree / 트리)** tiếp nhận điểm tựa từ **4. Tại sao thứ tự cột của composite chỉ mục (index / 인덱스) quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Chi phí cập nhật của chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Top-N và B+cây (tree / 트리)

Truy vấn:

```sql
SELECT *
FROM transaction
WHERE user_id = ?
ORDER BY created_at DESC
LIMIT 20;
```

với chỉ mục (index / 인덱스) phù hợp có thể:

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

Ta đã thay bài toán `sort + top-k` bằng **khai thác thứ tự đã được materialize trong chỉ mục (index / 인덱스)**.

Bài học chung:

> Nếu một thao tác đắt được lặp lại nhiều lần, có thể đáng để duy trì trước một bất biến giúp thao tác đó rẻ đi.

Đây chính là bản chất của chỉ mục (index / 인덱스).

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **6. Chi phí cập nhật của chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **5. Top-N và B+cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Covering chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Chi phí cập nhật của chỉ mục (index / 인덱스)

Chỉ mục (index / 인덱스) không miễn phí. Mỗi insert/cập nhật (update / 업데이트)/delete phải duy trì thêm cấu trúc.

Ví dụ insert vào B+cây (tree / 트리) có thể cần:

```text
tìm leaf phù hợp
chèn record/key
split page nếu đầy
cập nhật parent
có thể lan split lên trên
```

Băm (hash / 해시) chỉ mục (index / 인덱스) có thể cần resize/rehash. Secondary chỉ mục (index / 인덱스) có thể phải ghi thêm nhiều trang.

Vì vậy hệ thống nhiều chỉ mục (index / 인덱스) thường có:

```text
đọc nhanh hơn
nhưng ghi chậm hơn
nhiều bộ nhớ/SSD hơn
nhiều write amplification hơn
```

Đây là sự đánh đổi giữa chi phí truy vấn và chi phí duy trì bất biến.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **7. Covering chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **6. Chi phí cập nhật của chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Clustered và secondary chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Covering chỉ mục (index / 인덱스)

Nếu truy vấn chỉ cần:

```sql
SELECT created_at, amount
FROM transaction
WHERE user_id = ?
ORDER BY created_at DESC
LIMIT 20;
```

một chỉ mục (index / 인덱스) có thể chứa thêm `amount` để truy vấn không cần quay về bảng chính.

Về mặt DSA, ta đang tăng siêu dữ liệu (metadata / 메타데이터) trên cấu trúc tìm kiếm để giảm một bước truy cập khác.

Đây cùng nguyên lý với **cây tăng cường (augmented tree)**:

```text
thêm metadata
→ cập nhật đắt hơn / tốn bộ nhớ hơn
→ truy vấn cụ thể nhanh hơn
```

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **8. Clustered và secondary chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **7. Covering chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Buffer Pool: bộ nhớ đệm (cache / 캐시) của cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Clustered và secondary chỉ mục (index / 인덱스)

Nếu dữ liệu vật lý gần thứ tự chỉ mục (index / 인덱스), phạm vi (range / 범위) scan có locality tốt. Nếu secondary chỉ mục (index / 인덱스) chỉ chứa pointer tới tuple nằm rải rác, một scan theo chỉ mục (index / 인덱스) có thể dẫn tới nhiều random reads.

Cùng `O(k)` bản ghi (record / 레코드) đầu ra (output / 출력) nhưng chi phí vật lý khác nhau lớn vì locality.

Đây là lý do mô hình DSA phải được nối với **bộ nhớ (memory / 메모리) hierarchy / lưu trữ (storage / 저장소) hierarchy**.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **8. Clustered và secondary chỉ mục (index / 인덱스)** nêu điều cần giải thích; **9. Buffer Pool: bộ nhớ đệm (cache / 캐시) của cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Bloom Filter trong LSM cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Buffer Pool: bộ nhớ đệm (cache / 캐시) của cơ sở dữ liệu (database / 데이터베이스)

Cơ sở dữ liệu (database / 데이터베이스) thường không đọc trực tiếp từ SSD cho mỗi truy vấn (query / 쿼리). Nó giữ page trong **buffer pool**.

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

Nhưng cơ sở dữ liệu (database / 데이터베이스) thực có thể dùng Clock, LRU-K hoặc biến thể khác vì scan lớn có thể làm ô nhiễm LRU đơn giản.

Đây là ví dụ composition giữa bảng băm (hash table / 해시 테이블) và cấu trúc thứ tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **9. Buffer Pool: bộ nhớ đệm (cache / 캐시) của cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **10. Bloom Filter trong LSM cây (tree / 트리)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. B+cây (tree / 트리) và LSM cây (tree / 트리) tối ưu hai tải công việc (workload / 워크로드) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Bloom Filter trong LSM cây (tree / 트리)

LSM cây (tree / 트리) thường có nhiều SSTable bất biến. Nếu phải kiểm tra mọi tệp (file / 파일) để biết khóa có tồn tại hay không, tra cứu sẽ tốn nhiều I/O.

Bloom Filter cho mỗi SSTable trả lời:

```text
chắc chắn không có
hoặc
có thể có
```

Nếu Bloom nói “không có”, có thể bỏ qua tệp (file / 파일). Nếu “có thể có”, mới đọc chỉ mục (index / 인덱스)/dữ liệu (data / 데이터) thật.

Dương tính giả chỉ làm thêm I/O; không làm sai kết quả cuối cùng.

Đây là cách một cấu trúc xác suất được đặt trước một cấu trúc chính xác để giảm chi phí trung bình.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **11. B+cây (tree / 트리) và LSM cây (tree / 트리) tối ưu hai tải công việc (workload / 워크로드) khác nhau** tiếp nhận điểm tựa từ **10. Bloom Filter trong LSM cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. băm (hash / 해시) phép nối (join / 조인) và Sort-Merge phép nối (join / 조인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. B+cây (tree / 트리) và LSM cây (tree / 트리) tối ưu hai tải công việc (workload / 워크로드) khác nhau

B+cây (tree / 트리) cập nhật trực tiếp cấu trúc có thứ tự theo page. LSM cây (tree / 트리) gom ghi trong bộ nhớ (memory / 메모리) rồi flush tuần tự thành các run đã sắp xếp, sau đó compaction nền.

Có thể nhìn như:

```text
B+Tree:
  trả chi phí cập nhật tại thời điểm ghi

LSM:
  gom/batch ghi trước
  trả chi phí merge/compaction về sau
```

Đây là sự khác nhau về cách phân phối chi phí theo thời gian, gần với tư duy khấu hao.

LSM phù hợp tải công việc (workload / 워크로드) ghi lớn; B+cây (tree / 트리) thường mạnh khi cần phạm vi (range / 범위) truy vấn (query / 쿼리) và đọc ổn định với ít read amplification hơn.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **12. băm (hash / 해시) phép nối (join / 조인) và Sort-Merge phép nối (join / 조인)** tiếp nhận điểm tựa từ **11. B+cây (tree / 트리) và LSM cây (tree / 트리) tối ưu hai tải công việc (workload / 워크로드) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. băm (hash / 해시) phép nối (join / 조인) và Sort-Merge phép nối (join / 조인)

Chỉ mục (index / 인덱스) không phải nơi duy nhất DSA xuất hiện trong cơ sở dữ liệu (database / 데이터베이스).

Với equality phép nối (join / 조인):

```sql
A JOIN B ON A.user_id = B.user_id
```

Băm (hash / 해시) phép nối (join / 조인) có thể:

```text
build Hash Table trên phía nhỏ
scan phía lớn
probe từng khóa
```

Nếu hai phía đã có thứ tự theo phép nối (join / 조인) key, Sort-Merge phép nối (join / 조인) có thể quét tuyến tính bằng hai con trỏ.

Việc chọn phép nối (join / 조인) thuật toán (algorithm / 알고리즘) là bài toán chọn cấu trúc/thuật toán theo kích thước, thứ tự và bộ nhớ hiện có.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **13. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm** tiếp nhận điểm tựa từ **12. băm (hash / 해시) phép nối (join / 조인) và Sort-Merge phép nối (join / 조인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. trường hợp (case / 사례): thiết kế chỉ mục (index / 인덱스) cho tải công việc (workload / 워크로드) ban đầu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm

Một truy vấn (query / 쿼리) nhiều bảng có nhiều phép nối (join / 조인) thứ tự (order / 순서) khác nhau. Với `n` bảng, số kế hoạch có thể tăng rất nhanh.

Optimizer có thể dùng:

```text
Dynamic Programming
memoization
branch-and-bound style pruning
cost model
statistics
```

Tức là ngay cả việc **chọn thuật toán** cũng trở thành một bài toán DSA.

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **13. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm** cho ta quy tắc; **14. trường hợp (case / 사례): thiết kế chỉ mục (index / 인덱스) cho tải công việc (workload / 워크로드) ban đầu** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **15. Khi nào một chỉ mục (index / 인덱스) không còn đáng giá?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. trường hợp (case / 사례): thiết kế chỉ mục (index / 인덱스) cho tải công việc (workload / 워크로드) ban đầu

Quay lại tải công việc (workload / 워크로드):

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

Nếu hệ thống đọc rất nhiều theo `transaction_id`, hash-based đường dẫn (path / 경로) có thể hữu ích. Nhưng nếu engine đã có B+cây (tree / 트리) primary chỉ mục (index / 인덱스) đủ nhanh và cần đơn giản hóa hệ thống, thêm băm (hash / 해시) chỉ mục (index / 인덱스) riêng chưa chắc đáng giá.

Đây là bài học quan trọng: **DSA cho tập ứng viên, tải công việc (workload / 워크로드) và chi phí (cost / 비용) mô hình (model / 모델) quyết định lựa chọn cuối cùng**.

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **14. trường hợp (case / 사례): thiết kế chỉ mục (index / 인덱스) cho tải công việc (workload / 워크로드) ban đầu** cho ta quy tắc; **15. Khi nào một chỉ mục (index / 인덱스) không còn đáng giá?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **16. bất biến (invariant / 불변식) và crash consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Khi nào một chỉ mục (index / 인덱스) không còn đáng giá?

Một chỉ mục (index / 인덱스) có thể phản tác dụng nếu:

```text
cột có độ chọn lọc quá thấp
query hiếm khi dùng
bảng nhỏ đến mức scan rẻ hơn
write amplification quá lớn
index không vừa bộ nhớ và tạo thêm random I/O
statistics sai làm optimizer chọn plan tệ
```

Không nên đánh giá chỉ mục (index / 인덱스) chỉ từ Big-O của lookup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **16. bất biến (invariant / 불변식) và crash consistency** tiếp nhận điểm tựa từ **15. Khi nào một chỉ mục (index / 인덱스) không còn đáng giá?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Cách kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. bất biến (invariant / 불변식) và crash consistency

Trong bộ nhớ, một cấu trúc chỉ cần giữ bất biến lô-gic (logic / 논리). Trong cơ sở dữ liệu (database / 데이터베이스) bền vững, phải giữ thêm:

```text
trạng thái trên đĩa có thể phục hồi sau crash
page split không để index ở trạng thái nửa cập nhật
WAL/redo/undo đủ để khôi phục
```

Một B+cây (tree / 트리) đúng về mặt thuật toán nhưng không có giao thức (protocol / 프로토콜) ghi bền vững vẫn chưa đủ cho hệ quản trị dữ liệu thật.

Đây là ranh giới giữa DSA thuần và các hệ thống (systems / 시스템들) kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Trong **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **17. Cách kiểm thử** tiếp nhận điểm tựa từ **16. bất biến (invariant / 불변식) và crash consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Chuỗi suy luận hoàn chỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Cách kiểm thử

Không chỉ kiểm tra truy vấn (query / 쿼리) trả đúng. Cần kiểm tra:

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

> **Chuyển mạch:** Ở chặng này của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **17. Cách kiểm thử** xác định đầu vào; **18. Chuỗi suy luận hoàn chỉnh** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Chuỗi suy luận hoàn chỉnh

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Đó là cách kiến thức bảng băm (hash table / 해시 테이블), B+cây (tree / 트리), Bloom Filter, LRU, sorting, two pointers và chi phí (cost / 비용) mô hình (model / 모델) kết nối thành một thiết kế cơ sở dữ liệu (database / 데이터베이스) thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Trường hợp (case / 사례) Study: Thiết kế chỉ mục cơ sở dữ liệu từ góc nhìn DSA**, **Mô hình tư duy** gom các mảnh từ **18. Chuỗi suy luận hoàn chỉnh** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> **chỉ mục (index / 인덱스) là một cấu trúc dữ liệu được duy trì trước để mua lại tốc độ truy vấn trong tương lai.** Cái giá phải trả là bộ nhớ, I/O, ghi (write / 쓰기) amplification và độ phức tạp (complexity / 복잡도) khi cập nhật. Không có chỉ mục (index / 인덱스) tốt tuyệt đối; chỉ có chỉ mục (index / 인덱스) phù hợp với tập thao tác và tầng lưu trữ cụ thể.

Xem thêm: [Hash Tables](../01_linear_structures/04_hash_tables.md), [B/B+Tree & External Memory](../02_trees/05_b_trees_and_external_memory.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [DSA in Systems](./01_dsa_in_databases_networks_and_systems.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
