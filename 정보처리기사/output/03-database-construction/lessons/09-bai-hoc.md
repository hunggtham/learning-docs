# 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 khái niệm cấu thành mô hình thực thể - mối quan hệ: Thực thể (`개체 / Entity`), Thuộc tính (`속성 / Attribute`), và Mối quan hệ (`관계 / Relationship`).
- Thuộc lòng bảng quy ước ký hiệu hình học Peter Chen trong sơ đồ E-R.
- Phân biệt rõ các loại quan hệ (1:1, 1:N, N:M) và cách biểu diễn trên liên kết giữa các thực thể.

## 핵심 키워드 (Từ khóa)
- E-R 다이어그램 (Sơ đồ thực thể - mối quan hệ / E-R Diagram)
- 개체 (Thực thể / Entity)
- 속성 (Thuộc tính / Attribute)
- 관계 (Mối quan hệ / Relationship)
- 사각형·마름모·타원 (Hình chữ nhật - Hình thoi - Hình bầu dục)
- 매핑 카디널리티 (Tỷ lệ ánh xạ / Mapping Cardinality: 1:1, 1:N, N:M)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([07-bai-hoc.md](07-bai-hoc.md), [08-bai-hoc.md](08-bai-hoc.md)):** Sau khi đã hiểu cấu trúc bảng logic (Relation), ta cần nắm chắc nguồn gốc sinh ra bảng: chính là sơ đồ E-R ở tầng khái niệm.
- **Tiếp nối sang bài sau ([10-bai-hoc.md](10-bai-hoc.md)):** Bài tiếp theo sẽ đi sâu vào phân loại các loại thuộc tính phức tạp hơn (thuộc tính phức hợp, thuộc tính suy diễn) và các bẫy đề thi về ký hiệu E-R.

## 읽는 방법 (Cách đọc)
- Học thuộc bảng ký hiệu Peter Chen ở TẦNG A: **Chữ nhật là Thực thể, Thoi là Quan hệ, Bầu dục là Thuộc tính**.
- Chú ý cách xác định tỷ lệ quan hệ 1:1, 1:N, N:M vì đây là tiền đề để chuyển đổi sang bảng có khóa ngoại.

---

## 13. 데이터 모델과 E-R 다이어그램 (Mô hình dữ liệu & Biểu đồ E-R)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Ba thành phần nền tảng của mô hình E-R (개념적 모델의 3요소):**
  - **개체 (Entity - Thực thể):** Là đối tượng trong thế giới thực có sự tồn tại độc lập và có thể phân biệt được với các đối tượng khác (ví dụ: `Học sinh`, `Giáo viên`, `Phòng học`).
  - **관계 (Relationship - Mối quan hệ):** Là sự liên kết ngữ nghĩa giữa hai hay nhiều thực thể (ví dụ: Học sinh `Đăng ký` Môn học, Giáo viên `Chủ nhiệm` Lớp).
  - **속성 (Attribute - Thuộc tính):** Là các đặc tính mô tả bản chất của thực thể hoặc của mối quan hệ (ví dụ: Học sinh có `Mã SV`, `Họ tên`, `Ngày sinh`).
- **2. Bảng ký hiệu E-R chuẩn Peter Chen (E-R 다이어그램 기호):**
  | Ký hiệu hình học | Thuật ngữ Hàn | Ý nghĩa kỹ thuật | Ví dụ thực tế |
  |---|---|---|---|
  | **사각형 (Hình chữ nhật)** | 개체 (Entity) | Thực thể độc lập | `고객` (Khách hàng), `상품` (Sản phẩm) |
  | **마름모 (Hình thoi)** | 관계 (Relationship) | Mối liên kết giữa các thực thể | `구매` (Mua hàng), `수강` (Đăng ký học) |
  | **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính mô tả | `고객ID`, `Tên`, `Giá tiền` |
  | **밑줄 타원 (Bầu dục gạch chân)** | 기본키 (Primary Key) | Thuộc tính khóa chính | `고객번호 (Gạch chân)` |
  | **이중 타원 (Bầu dục kép)** | 다중값 속성 (Multivalued) | Thuộc tính chứa nhiều giá trị | `전화번호` (Số ĐT nhà + Di động) |
  | **선 (Đường thẳng)** | 링크 (Link) | Nối thực thể với quan hệ hoặc thuộc tính | Đường liên kết |
- **3. Tỷ lệ ánh xạ (Mapping Cardinality):**
  - **1:1 (Một - Một):** Mỗi thực thể A chỉ liên kết với tối đa 1 thực thể B và ngược lại (ví dụ: Mỗi người chỉ có 1 CCCD).
  - **1:N (Một - Nhiều):** Một thực thể A liên kết với nhiều thực thể B, nhưng mỗi B chỉ thuộc về 1 A (ví dụ: Một Khoa có nhiều Sinh viên, mỗi SV chỉ thuộc 1 Khoa).
  - **N:M (Nhiều - Nhiều):** Một A liên kết nhiều B và một B liên kết nhiều A (ví dụ: Một SV học nhiều Môn, một Môn có nhiều SV).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Quan hệ N:M trên sơ đồ E-R **không thể chuyển trực tiếp thành 2 bảng quan hệ** mà bắt buộc phải tạo thêm 1 bảng trung gian (Junction Table) ở tầng logic.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Chữ nhật = Thực thể, Thoi = Quan hệ, Bầu dục = Thuộc tính".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Thuộc tính của chính mối quan hệ (Relationship Attribute):**
  - Trong mối quan hệ `구매 (Mua hàng)` giữa `고객 (Khách hàng)` và `상품 (Sản phẩm)`: Thuộc tính `Ngày mua (구매일자)` hoặc `Số lượng (구매수량)` không thuộc về riêng Khách hàng cũng không thuộc về riêng Sản phẩm. Nó là **thuộc tính gắn trực tiếp vào hình thoi `구매`**.
  - Khi chuyển sang mô hình quan hệ, thuộc tính của mối quan hệ N:M sẽ trở thành các cột trong bảng trung gian.
- **Quy tắc chuyển đổi tỷ lệ quan hệ sang RDBMS:**
  - Quan hệ 1:1: Có thể gộp chung thành 1 bảng hoặc đưa khóa chính bên này sang làm khóa ngoại bên kia.
  - Quan hệ 1:N: Bắt buộc lấy khóa chính của bên 1 đặt làm Khóa ngoại (Foreign Key) ở bên N.
  - Quan hệ N:M: Bắt buộc tạo bảng thứ ba có khóa chính là khóa kết hợp của 2 khóa chính ban đầu.

### 복습 체크리스트
- [ ] Vẽ đúng các ký hiệu Peter Chen: 사각형 (Entity), 마름모 (Relationship), 타원 (Attribute).
- [ ] Phân biệt được tỷ lệ ánh xạ 1:1, 1:N và N:M.
- [ ] Nhớ quy tắc: Thuộc tính của mối quan hệ N:M sẽ đi vào bảng trung gian.
