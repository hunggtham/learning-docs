# 8. 서브쿼리와 뷰 (Truy vấn con và View)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và cơ chế hoạt động của Truy vấn con (`서브쿼리 / Subquery`): Câu lệnh `SELECT` lồng bên trong một câu lệnh SQL chính nhằm cung cấp dữ liệu trung gian cho câu lệnh cha.
- Phân biệt chi tiết hai loại truy vấn con cốt lõi trong đề thi: **Truy vấn con đơn dòng (Single-Row Subquery - `단일 행 서브쿼리`)** và **Truy vấn con đa dòng (Multi-Row Subquery - `다중 행 서브쿼리`)**.
- Sử dụng thành thạo các toán tử so sánh đa dòng: `IN`, `ANY` / `SOME`, `ALL`, và toán tử kiểm tra sự tồn tại `EXISTS`.
- Phân biệt các loại truy vấn con theo vị trí xuất hiện: **Scalar Subquery** (trong SELECT), **Inline View (`인라인 뷰`)** (trong FROM), và Nested Subquery (trong WHERE/HAVING).

## 핵심 키워드 (Từ khóa)
- 서브쿼리 (Truy vấn con / Subquery)
- 단일 행 서브쿼리 (Truy vấn con đơn dòng: `=`, `>`, `<`)
- 다중 행 서브쿼리 (Truy vấn con đa dòng: `IN`, `ANY`, `ALL`, `EXISTS`)
- 인라인 뷰 (Khung nhìn nội tuyến / Inline View: Subquery ở mệnh đề FROM)
- 스칼라 서브쿼리 (Scalar Subquery: Subquery ở mệnh đề SELECT)
- 뷰 (Khung nhìn / View)
- 메인 쿼리 (Truy vấn chính / Main Query)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([29-bai-hoc.md](29-bai-hoc.md), [30-bai-hoc.md](30-bai-hoc.md), [31-bai-hoc.md](31-bai-hoc.md)):** Sau khi nắm vững câu lệnh SELECT và cấu trúc Khung nhìn ảo (View), truy vấn con là kỹ thuật mở rộng để thực hiện các bài toán lọc phức tạp nhiều cấp mà không cần tạo bảng trung gian.
- **Tiếp nối sang bài sau ([33-bai-hoc.md](33-bai-hoc.md)):** Để tối ưu hóa hiệu năng khi chạy các câu truy vấn con lồng nhau trên các bảng dữ liệu lớn, việc đánh chỉ mục (`인덱스`) trên các cột liên kết là điều kiện bắt buộc.

## 읽는 방법 (Cách đọc)
- Học thuộc các toán tử so sánh đi kèm loại Subquery ở TẦNG A:
  - Trả về 1 dòng $\rightarrow$ Dùng toán tử so sánh thông thường (`=`, `>`, `<`, `<>`).
  - Trả về nhiều dòng $\rightarrow$ Bắt buộc dùng `IN`, `ANY`, `ALL`, `EXISTS`. Cấm tuyệt đối dùng dấu bằng `=` đơn lẻ!
- Nhớ tên gọi theo vị trí:
  - Nằm ở **SELECT** $\rightarrow$ **스칼라 서브쿼리 (Scalar Subquery)**.
  - Nằm ở **FROM** $\rightarrow$ **인라인 뷰 (Inline View)**.

---

## 8. 서브쿼리와 뷰 (Truy vấn con và View)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại Truy vấn con theo số lượng dòng kết quả:**
  | Loại Subquery | Thuật ngữ Hàn - Anh | Số dòng kết quả | Toán tử đi kèm bắt buộc |
  |---|---|:---:|---|
  | **Đơn dòng** | `단일 행 서브쿼리` (Single-Row Subquery) | **Duy nhất 1 dòng** (1 giá trị) | Các toán tử so sánh đơn lẻ: `=`, `>`, `>=`, `<`, `<=`, `<>` |
  | **Đa dòng** | `다중 행 서브쿼리` (Multi-Row Subquery) | **Nhiều dòng** (1 cột, nhiều dòng) | Bắt buộc dùng toán tử tập hợp: `IN`, `ANY` / `SOME`, `ALL`, `EXISTS` |
  | **Đa cột** | `다중 컬럼 서브쿼리` (Multi-Column Subquery) | Nhiều cột cùng lúc | So sánh cặp thuộc tính: `WHERE (cột1, cột2) IN (SELECT ...)` |

- **2. Bảng ý nghĩa các toán tử đa dòng trong đề thi (다중 행 연산자):**
  - **`IN`**: Giá trị ở truy vấn chính bằng với **bất kỳ giá trị nào** trong tập kết quả của Subquery.
  - **`> ANY` (hoặc `> SOME`)**: Lớn hơn **giá trị nhỏ nhất** trong tập kết quả của Subquery (chỉ cần lớn hơn ít nhất 1 giá trị).
  - **`< ANY` (hoặc `< SOME`)**: Nhỏ hơn **giá trị lớn nhất** trong tập kết quả của Subquery.
  - **`> ALL`**: Lớn hơn **tất cả mọi giá trị** trong tập kết quả của Subquery (tức là lớn hơn giá trị lớn nhất / MAX).
  - **`< ALL`**: Nhỏ hơn **tất cả mọi giá trị** trong tập kết quả của Subquery (tức là nhỏ hơn giá trị nhỏ nhất / MIN).
  - **`EXISTS`**: Kiểm tra xem Subquery có trả về ít nhất một dòng dữ liệu nào hay không; trả về giá trị logic `TRUE` nếu có ít nhất 1 dòng, `FALSE` nếu rỗng.
- **3. Phân loại theo vị trí xuất hiện trong câu lệnh SQL:**
  - **스칼라 서브쿼리 (Scalar Subquery):** Nằm ở mệnh đề **SELECT**, bắt buộc phải trả về chính xác 1 dòng và 1 cột (1 giá trị vô hướng).
  - **인라인 뷰 (Inline View):** Nằm ở mệnh đề **FROM**, đóng vai trò như một bảng ảo động tạm thời phục vụ riêng cho câu truy vấn đó, không được lưu trong từ điển dữ liệu.
  - **중첩 서브쿼리 (Nested Subquery):** Nằm ở mệnh đề **WHERE** hoặc **HAVING**, đóng vai trò làm điều kiện lọc dòng hoặc lọc nhóm.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề đưa câu truy vấn con trả về nhiều dòng nhưng lại dùng dấu bằng: `WHERE Luong = (SELECT Luong FROM ...);` $\rightarrow$ **LỖI THỰC THI (Single-row subquery returns more than one row)**. Phải thay bằng toán tử `IN` hoặc `= ANY`.
  - Đề hỏi: *"Subquery nằm ở mệnh đề FROM được gọi là gì?"* $\rightarrow$ Đáp án: **인라인 뷰 (Inline View)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa phân biệt giữa `> ANY` và `> ALL`:**
  - Giả sử câu truy vấn con trả về tập hợp điểm: `{70, 80, 90}`.
  - Điều kiện `WHERE Diem > ANY (SELECT ...)`:
    - Nghĩa là: `Diem > 70` (chỉ cần lớn hơn giá trị nhỏ nhất là 70).
    - Sinh viên có điểm 75 sẽ được chọn.
  - Điều kiện `WHERE Diem > ALL (SELECT ...)`:
    - Nghĩa là: `Diem > 90` (phải lớn hơn cả 70, 80 và 90).
    - Chỉ sinh viên có điểm từ 91 trở lên mới được chọn.
- **So sánh View và Inline View:**
  - `View (Khung nhìn)`: Định nghĩa vĩnh viễn trong CSDL bằng `CREATE VIEW`, nhiều người dùng và nhiều câu lệnh khác nhau có thể tái sử dụng.
  - `Inline View`: Định nghĩa tạm thời trong mệnh đề `FROM`, giải phóng bộ nhớ ngay sau khi câu lệnh hoàn thành.

### 복습 체크리스트
- [ ] Phân biệt được 단일 행 서브쿼리 và 다중 행 서브쿼리.
- [ ] Giải thích được sự khác nhau giữa `> ANY` (lớn hơn Min) và `> ALL` (lớn hơn Max).
- [ ] Nêu chức năng của toán tử EXISTS (kiểm tra có dữ liệu trả về hay không).
- [ ] Nhớ tên gọi: Subquery ở SELECT là 스칼라 서브쿼리; ở FROM là 인라인 뷰.
