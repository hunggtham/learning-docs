# 9. 인덱스와 트랜잭션 (Index và Giao dịch)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và cấu trúc của Chỉ mục (`인덱스 / Index`): Cấu trúc dữ liệu dạng cặp `<Giá trị khóa, Con trỏ>` (`<키 값, 포인터>`) giúp tăng tốc độ truy xuất bản ghi trên thiết bị lưu trữ vật lý.
- Phân biệt chi tiết các loại chỉ mục phổ biến trong hệ quản trị CSDL: **Chỉ mục cây B+Tree (`트리 기반 인덱스`)**, **Chỉ mục Bitmap (`비트맵 인덱스`)**, và **Chỉ mục dựa trên hàm (`함수 기반 인덱스`)**.
- So sánh sự khác nhau cốt lõi giữa **Chỉ mục gom cụm (Clustered Index - `클러스터드 인덱스`)** và **Chỉ mục không gom cụm (Non-Clustered Index - `넌클러스터드 인덱스`)**.
- Nhận thức rõ sự đánh đổi (Trade-off): Chỉ mục tăng tốc độ đọc (`SELECT`) nhưng làm chậm thao tác ghi (`INSERT, UPDATE, DELETE`).

## 핵심 키워드 (Từ khóa)
- 인덱스 (Chỉ mục / Index: `<키 값, 포인터>`)
- 클러스터드 인덱스 (Chỉ mục gom cụm / Clustered Index)
- 넌클러스터드 인덱스 (Chỉ mục không gom cụm / Non-Clustered Index)
- B+ 트리 인덱스 (Chỉ mục B+ Tree)
- 비트맵 인덱스 (Chỉ mục Bitmap: 0 và 1)
- 함수 기반 인덱스 (Chỉ mục dựa trên hàm / Function-Based Index)
- 카디널리티 (Lượng số / Độ phân biệt / Cardinality)
- 트랜잭션 (Giao dịch / ACID)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([03-bai-hoc.md](03-bai-hoc.md), [21-bai-hoc.md](21-bai-hoc.md), [22-bai-hoc.md](22-bai-hoc.md)):** Thiết kế chỉ mục là công việc trọng tâm của bước Thiết kế vật lý nhằm hỗ trợ Bộ tối ưu hóa truy vấn (Optimizer) tìm đường dẫn truy xuất nhanh nhất.
- **Tiếp nối sang bài sau ([25-bai-hoc.md](25-bai-hoc.md)):** Khi nhiều giao dịch cùng thao tác trên các bản ghi có chỉ mục, hệ thống phải thực hiện kiểm soát đồng thời và quản trị khóa chỉ mục (Index Locking).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng so sánh **Clustered vs Non-Clustered Index** ở TẦNG A:
  - Clustered: Dữ liệu trên đĩa được sắp xếp **trùng thứ tự Index**, mỗi bảng chỉ có **DUY NHẤT 1** cái.
  - Non-Clustered: Dữ liệu thực tế không đổi thứ tự, mỗi bảng có thể tạo **NHIỀU** cái.
- Nhớ quy tắc chọn cột làm Bitmap Index: Cột có **độ phân biệt thấp (Low Cardinality)** như Giới tính (Nam/Nữ).

---

## 9. 인덱스와 트랜잭션 (Index và Giao dịch)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bản chất kỹ thuật của Chỉ mục (인덱스의 개념):**
  - Là cấu trúc dữ liệu lưu trữ các cặp **`<Giá trị khóa, Con trỏ / Địa chỉ bản ghi>` (`<키 값, 포인터>`)** nhằm giúp DBMS định vị nhanh vị trí dữ liệu trên ổ đĩa mà không cần quét toàn bộ bảng (`Table Full Scan`).
  - Được tạo, sửa đổi và xóa bỏ thông qua ngôn ngữ định nghĩa dữ liệu **DDL** (`CREATE INDEX`, `DROP INDEX`).
  - **Lưu ý hiệu năng:** Nếu một bảng có tần suất **thêm, xóa, sửa (`INSERT, DELETE, UPDATE`) diễn ra liên tục** thì **cần hạn chế số lượng chỉ mục ở mức tối thiểu**, vì mỗi lần ghi dữ liệu DBMS đều phải tự động tính toán sắp xếp lại chỉ mục.
- **2. Bảng so sánh kinh điển: Clustered Index vs Non-Clustered Index:**
  | Tiêu chí | 클러스터드 인덱스 (Clustered Index) | 넌클러스터드 인덱스 (Non-Clustered Index) |
  |---|---|---|
  | **Thứ tự vật lý của dữ liệu** | **Trùng khớp hoàn toàn** với thứ tự sắp xếp của khóa chỉ mục | **Độc lập**, không làm thay đổi thứ tự lưu trữ vật lý của các dòng dữ liệu |
  | **Số lượng tối đa trên 1 bảng** | **Chỉ có DUY NHẤT 1** (Thường tự động gán cho Khóa chính `Primary Key`) | **Có thể tạo NHIỀU** trên cùng một bảng |
  | **Cấu trúc nút lá (Leaf Node)** | Nút lá chính là **dòng dữ liệu thực tế** (Data Page) | Nút lá chỉ chứa **con trỏ (RID / Bookmark)** trỏ đến vị trí dòng dữ liệu thực |
  | **Hiệu năng truy vấn khoảng** | **Cực kỳ nhanh** khi tìm kiếm theo dải phạm vi (`BETWEEN`, `<`, `>`) | Chậm hơn khi tìm theo khoảng vì phải tra cứu con trỏ nhiều lần |
  | **Chi phí khi Thêm / Sửa / Xóa** | Chi phí cao vì phải dịch chuyển sắp xếp lại vị trí vật lý trên đĩa | Chi phí thấp hơn vì chỉ cần sửa cây chỉ mục, không chuyển dữ liệu gốc |

- **3. Phân loại các cấu trúc Chỉ mục phổ biến (인덱스 종류):**
  - **B+Tree 인덱스 (Chỉ mục cây B+):** Cấu trúc phân cấp gồm Root, Branch, Leaf. Các nút lá được liên kết kép hai chiều (Doubly Linked List). Phổ biến nhất trong hầu hết các DBMS thương mại.
  - **비트맵 인덱스 (Bitmap Index):** Mã hóa dữ liệu cột thành chuỗi bit nhị phân `0` và `1`. Rất thích hợp cho các cột có **độ phân biệt thấp (Low Cardinality)** như Giới tính (`M/F`), Trạng thái đơn hàng.
  - **함수 기반 인덱스 (Function-Based Index):** Lưu giá trị kết quả sau khi áp dụng hàm toán học hoặc biểu thức (ví dụ: `UPPER(TenNV)`), giúp tăng tốc các truy vấn chứa hàm ở mệnh đề `WHERE`.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Mỗi bảng trong cơ sở dữ liệu có thể có bao nhiêu Clustered Index?"* $\rightarrow$ Đáp án: **Chỉ duy nhất 1 (단 1개)**.
  - Đề hỏi: *"Cột nào thích hợp nhất để tạo Bitmap Index?"* $\rightarrow$ Đáp án: **Cột có giá trị phân biệt thấp (카디널리티가 낮은 컬럼, ví dụ: Giới tính, Tình trạng hôn nhân)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa trực quan sự khác nhau giữa Clustered và Non-Clustered:**
  - **Clustered Index giống như Từ điển tiếng Anh:** Các từ được sắp xếp vật lý theo thứ tự chữ cái A-Z. Muốn tìm từ "Database", bạn lật ngay đến vần D là thấy toàn bộ định nghĩa từ (không cần mục lục trung gian).
  - **Non-Clustered Index giống như Mục lục cuối sách giáo khoa:** Cuối sách có danh mục thuật ngữ "Database $\rightarrow$ xem trang 45, 120". Bạn phải mở mục lục tra số trang trước, rồi mới lật đến trang đó để đọc nội dung.

### 복습 체크리스트
- [ ] Định nghĩa được 인덱스 là cặp `<키 값, 포인터>`.
- [ ] Phân biệt được 클러스터드 인덱스 (chỉ có 1, dữ liệu xếp theo thứ tự) và 넌클러스터드 인덱스 (có nhiều).
- [ ] Hiểu vì sao bảng có nhiều thao tác INSERT/DELETE thì nên giảm bớt số lượng Index.
- [ ] Nắm được trường hợp tối ưu của 비트맵 인덱스 (độ phân biệt thấp).
