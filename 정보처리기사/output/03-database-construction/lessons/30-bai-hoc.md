# 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp chi tiết và cơ chế thực thi của các câu lệnh DML nâng cao: `INSERT`, `UPDATE`, `DELETE`, và `SELECT`.
- Phân biệt chính xác các ký tự đại diện trong toán tử so khớp mẫu chuỗi `LIKE`: ký tự đại diện chuỗi bất kỳ (`%`), ký tự đại diện đúng một ký tự (`_`), và ký tự đại diện chữ số (`#`).
- Sử dụng thành thạo các toán tử điều kiện trong mệnh đề WHERE: `BETWEEN ... AND ...`, `IN (...)`, và phép kiểm tra giá trị rỗng `IS NULL` / `IS NOT NULL`.

## 핵심 키워드 (Từ khóa)
- DML (데이터 조작어 / Data Manipulation Language)
- UPDATE SET / DELETE FROM
- SELECT DISTINCT
- LIKE 연산자 (Toán tử LIKE: `%`, `_`, `#`)
- BETWEEN 연산자 (Khoảng giá trị: BETWEEN A AND B)
- IN 연산자 (Tập hợp giá trị)
- IS NULL / IS NOT NULL (Kiểm tra giá trị rỗng)
- 와일드카드 (Ký tự đại diện / Wildcard characters)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([28-bai-hoc.md](28-bai-hoc.md), [29-bai-hoc.md](29-bai-hoc.md)):** Sau khi hiểu thứ tự thực thi của câu lệnh SELECT, các toán tử điều kiện này là vũ khí chính để viết vị từ lọc dòng chính xác tại mệnh đề WHERE.
- **Tiếp nối sang các bài sau ([31-bai-hoc.md](31-bai-hoc.md), [32-bai-hoc.md](32-bai-hoc.md)):** Các câu lệnh SELECT phức hợp chứa điều kiện LIKE, BETWEEN thường được đóng gói thành các Khung nhìn ảo (`뷰 / View`) để bảo mật và tái sử dụng thường xuyên.

## 읽는 방법 (Cách đọc)
- Học thuộc 2 ký tự đại diện thường gặp nhất của `LIKE`:
  - **`%`**: Đại diện cho chuỗi ký tự bất kỳ với độ dài từ 0 ký tự trở lên.
  - **`_`**: Đại diện cho **đúng 1 ký tự duy nhất**.
- Khắc ghi quy tắc kiểm tra NULL: **Cấm dùng `= NULL`**, bắt buộc phải viết **`IS NULL`** hoặc **`IS NOT NULL`**.

---

## 150-155. 데이터 조작어 (DML) 확장 및 조건 연산자

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Cú pháp chi tiết các câu lệnh DML thực thi:**
  - **INSERT (Chèn bản ghi mới):**
    ```sql
    INSERT INTO SINH_VIEN (MaSV, HoTen, Tuoi) VALUES ('B2101', 'Kim', 21);
    ```
    - Nếu chèn giá trị cho toàn bộ các cột theo đúng thứ tự bảng định nghĩa thì có thể lược bỏ danh sách tên cột.
  - **UPDATE (Cập nhật dữ liệu):**
    ```sql
    UPDATE SINH_VIEN SET Tuoi = 22, Lop = 'IT01' WHERE MaSV = 'B2101';
    ```
    - Nếu không chỉ định mệnh đề `WHERE`, **toàn bộ các dòng** trong bảng đều sẽ bị cập nhật đồng loạt.
  - **DELETE (Xóa dữ liệu):**
    ```sql
    DELETE FROM SINH_VIEN WHERE Tuoi < 18;
    ```
    - Khác với DROP (xóa cả bảng), DELETE chỉ xóa các dòng bản ghi bên trong bảng và giữ nguyên cấu trúc bảng.
  - **SELECT (Truy vấn dữ liệu):**
    - Mệnh đề `DISTINCT`: Loại bỏ hoàn toàn các hàng trùng lặp trong tập kết quả trả về (`SELECT DISTINCT Khoa FROM SINH_VIEN;`).
- **2. Bảng tổng hợp các toán tử điều kiện và Ký tự đại diện (와일드카드):**
  | Toán tử / Ký tự | Ý nghĩa kỹ thuật | Ví dụ minh họa trong SQL | Kết quả khớp |
  |---|---|---|---|
  | **LIKE `'%đoạn%'`** | So khớp chuỗi bất kỳ (từ 0 ký tự trở lên) | `WHERE HoTen LIKE '김%'` | Khớp với mọi tên bắt đầu bằng chữ "김" ("김", "김철수", "김민수"). |
  | **LIKE `'_'`** | So khớp đúng **chính xác 1 ký tự** | `WHERE HoTen LIKE '김_'` | Khớp với tên có **đúng 2 ký tự** và bắt đầu bằng "김" ("김철", "김박"). Không khớp với tên có 3 chữ. |
  | **LIKE `'#'`** | So khớp **chính xác 1 chữ số** (0-9) | `WHERE MaPhong LIKE 'P#0'` | Khớp với "P10", "P20", không khớp với "PA0". |
  | **BETWEEN A AND B** | Nằm trong đoạn từ A đến B (bao gồm cả A và B) | `WHERE Diem BETWEEN 80 AND 90` | Tương đương: `Diem >= 80 AND Diem <= 90`. |
  | **IN (giá trị1, ...)** | Bằng bất kỳ giá trị nào trong tập hợp liệt kê | `WHERE Khoa IN ('CNTT', 'DienTu')` | Tương đương: `Khoa = 'CNTT' OR Khoa = 'DienTu'`. |
  | **IS NULL** | Kiểm tra thuộc tính mang giá trị rỗng | `WHERE Email IS NULL` | Lấy các dòng chưa có dữ liệu Email. **Tuyệt đối không viết `Email = NULL`**. |

- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Để tìm người có họ 'Kim' và tên gồm 3 chữ cái (ví dụ: Kim Chul Soo) thì dùng mẫu nào?"* $\rightarrow$ Đáp án: **`LIKE '김__'`** (chữ Kim kèm theo 2 dấu gạch dưới).
  - Đề hỏi: *"Giá trị NULL có thể so sánh bằng toán tử `=` hoặc `<>` được không?"* $\rightarrow$ **KHÔNG**, bắt buộc phải dùng **`IS NULL`** hoặc **`IS NOT NULL`**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa phân biệt giữa `%` và `_`:**
  - Giả sử bảng có các giá trị cột `MaSo`:
    1. `AB`
    2. `ABC`
    3. `ABCD`
  - Biểu thức `WHERE MaSo LIKE 'A%'`: Trả về cả 3 dòng (`AB`, `ABC`, `ABCD`).
  - Biểu thức `WHERE MaSo LIKE 'A_'`: Chỉ trả về duy nhất dòng `AB` (A + đúng 1 ký tự nữa).
  - Biểu thức `WHERE MaSo LIKE 'A__'` (2 dấu gạch dưới): Chỉ trả về dòng `ABC` (A + đúng 2 ký tự nữa).

### 복습 체크리스트
- [ ] Viết đúng cấu trúc lệnh UPDATE và DELETE có mệnh đề WHERE.
- [ ] Phân biệt được chức năng của `%` (chuỗi bất kỳ) và `_` (đúng 1 ký tự) trong LIKE.
- [ ] Chuyển đổi thành thạo giữa cú pháp BETWEEN A AND B và phép so sánh `>=, <=`.
- [ ] Nhớ kỹ quy tắc bắt buộc dùng IS NULL / IS NOT NULL thay vì dấu bằng `=`.
