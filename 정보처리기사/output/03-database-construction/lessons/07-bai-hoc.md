# 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)

## 학습 목표 (Mục tiêu)
- Nắm vững lịch sử và các quy chuẩn ký hiệu nâng cao của mô hình E-R (Peter Chen) và mô hình quan hệ (E.F. Codd).
- Nhớ chính xác các ký hiệu E-R chuyên biệt trong đề thi: Thực thể yếu (`이중 사각형`), Quan hệ xác định (`이중 마름모`), Thuộc tính đa trị (`이중 타원`), Thuộc tính khóa chính (`밑줄 타원`).
- Thuộc lòng 4 đặc trưng bất biến của một Relation (Bảng quan hệ) và giải thích được tại sao chúng là nền tảng của lý thuyết CSDL quan hệ.

## 핵심 키워드 (Từ khóa)
- 피터 첸 E-R 모델 (Peter Chen E-R Model)
- 개체 타입 (Kiểu thực thể / Entity Type)
- 관계 타입 (Kiểu quan hệ / Relationship Type)
- 약한 개체 (Thực thể yếu / Weak Entity)
- 식별 관계 (Mối quan hệ xác định / Identifying Relationship)
- 다중값 속성 (Thuộc tính đa trị / Multi-valued Attribute)
- 관계형 데이터 모델 (Mô hình dữ liệu quan hệ / Relational Data Model)
- 튜플의 유일성 / 무순서성 (Tính duy nhất & Không thứ tự của Tuple)
- 원자값 (Giá trị nguyên tử / Atomic Value)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([06-bai-hoc.md](06-bai-hoc.md)):** Sau khi hiểu 3 yếu tố chung (`구조 - 연산 - 제약 조건`), bài này đào sâu vào 2 mô hình kinh điển nhất: Mô hình E-R ở tầng khái niệm và Mô hình quan hệ ở tầng logic.
- **Tiếp nối sang bài sau ([08-bai-hoc.md](08-bai-hoc.md)):** Bài tiếp theo sẽ bóc tách chi tiết giải phẫu học của một bảng quan hệ: Tuple, Attribute, Degree (차수), Cardinality (카디널리티), Domain (도메인).

## 읽는 방법 (Cách đọc)
- Ở TẦNG A, chú ý phần ký hiệu kép (Double): **Hình kép luôn dành cho cái "yếu" hoặc "đa trị"** (Hình chữ nhật kép = Thực thể yếu; Hình thoi kép = Quan hệ thực thể yếu; Hình elip kép = Thuộc tính đa trị).
- Nhớ 4 đặc trưng của Relation: **Duy nhất - Vô thứ tự hàng - Vô thứ tự cột - Nguyên tử**.

---

## 168-172. 관계형 데이터 모델 및 E-R 모델 심화 (Relational & E-R Model Deep Dive)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Mô hình E-R (Entity-Relationship Model - Peter Chen, 1976):**
  - Là công cụ mô hình hóa khái niệm trực quan phổ biến nhất.
  - **Bảng ký hiệu E-R nâng cao trong đề thi:**
    | Ký hiệu hình học | Thuật ngữ Hàn | Ý nghĩa kỹ thuật |
    |---|---|---|
    | **사각형 (Hình chữ nhật)** | 개체 (Entity) | Thực thể độc lập (Strong Entity). |
    | **이중 사각형 (Hình chữ nhật kép)** | 약한 개체 (Weak Entity) | Thực thể yếu (tồn tại phụ thuộc vào thực thể khác, ví dụ: Thân nhân nhân viên). |
    | **마름모 (Hình thoi)** | 관계 (Relationship) | Mối quan hệ giữa các thực thể (1:1, 1:N, N:M). |
    | **이중 마름모 (Hình thoi kép)** | 식별 관계 (Identifying Rel) | Quan hệ liên kết thực thể yếu với thực thể chủ. |
    | **타원 (Hình bầu dục)** | 속성 (Attribute) | Thuộc tính mô tả thực thể. |
    | **밑줄 타원 (Bầu dục gạch chân)** | 기본키 속성 (Primary Key) | Thuộc tính được chọn làm Khóa chính. |
    | **이중 타원 (Bầu dục kép)** | 다중값 속성 (Multivalued) | Thuộc tính có thể chứa nhiều giá trị (vd: Số điện thoại, Kỹ năng). |
    | **점선 타원 (Bầu dục nét đứt)** | 유도 속성 (Derived Attribute) | Thuộc tính suy diễn (tính toán từ thuộc tính khác, vd: Tuổi suy ra từ Ngày sinh). |
- **2. Mô hình quan hệ (Relational Model - E.F. Codd, 1970):**
  - Biểu diễn dữ liệu logic dưới dạng **bảng 2 chiều (2차원 테이블 / Relation)** gồm các hàng và các cột.
- **3. Bốn đặc trưng cốt lõi của Relation (릴레이션의 특징 - 172):**
  1. `튜플의 유일성` (Tính duy nhất của Tuple): Không thể tồn tại 2 hàng giống hệt nhau trong một bảng (phải phân biệt bằng khóa chính).
  2. `튜플의 무순서성` (Không có thứ tự giữa các hàng): Thứ tự xuất hiện của các hàng trong bảng không có ý nghĩa ngữ nghĩa (hoán đổi vị trí các hàng thì bảng vẫn không đổi).
  3. `속성의 무순서성` (Không có thứ tự giữa các cột): Thứ tự các cột không quan trọng, các cột được định danh bằng Tên thuộc tính (`속성명`).
  4. `속성의 원자성` (Tính nguyên tử của giá trị): Mọi giá trị tại giao điểm giữa hàng và cột đều phải là **giá trị nguyên tử (`원자값 / Atomic value`)**, không thể phân rã thành tập hợp con (đáp ứng dạng chuẩn 1NF).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề hỏi: *"Thứ tự các hàng trong bảng quan hệ có ý nghĩa gì không?"* → Chọn đáp án: **Hoàn toàn không có thứ tự (`무순서성`)**.
  - Đề hỏi: *"Thuộc tính đa trị trong E-R ký hiệu bằng gì?"* → Chọn **이중 타원 (Hình bầu dục kép)**.
  - Đề hỏi: *"Thực thể yếu (Weak Entity) ký hiệu bằng gì?"* → Chọn **이중 사각형 (Hình chữ nhật kép)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "E-R hình kép là yếu & đa trị; Bảng quan hệ thì hàng cột vô thứ tự, dữ liệu nguyên tử".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bản chất của Thực thể yếu (Weak Entity) và Khóa từng phần (Partial Key):**
  - Thực thể yếu không thể tự định danh nếu thiếu thực thể cha. Ví dụ: Bảng `THAN_NHAN` (Người phụ thuộc) của nhân viên. Một nhân viên có thể có con tên "An", nhân viên khác cũng có con tên "An". Do đó tên con không thể làm khóa chính một mình; nó cần kết hợp với `MaNV` của thực thể cha để xác định duy nhất.
  - Khóa từng phần (Discriminator) của thực thể yếu trên sơ đồ E-R được ký hiệu bằng **gạch chân nét đứt (점선 밑줄)**.
- **Tại sao Relation bắt buộc phải có giá trị nguyên tử (Atomic)?**
  - Nếu một cột `SoDienThoai` chứa chuỗi `"090123; 098456"`, câu lệnh SQL tìm kiếm `WHERE SoDienThoai = '090123'` sẽ bị lỗi hoặc phải dùng toán tử `LIKE` tốn kém. Tách thành các giá trị nguyên tử giúp phép toán đại số quan hệ và lập chỉ mục (index) vận hành hiệu quả nhất.

### 복습 체크리스트
- [ ] Nhận diện đúng ký hiệu E-R: Hình thoi kép (식별 관계), Bầu dục kép (다중값 속성), Hình chữ nhật kép (약한 개체).
- [ ] Thuộc lòng 4 đặc trưng của Relation: 유일성, 튜플 무순서, 속성 무순서, 원자값.
- [ ] Phân biệt được sự khác nhau giữa E-R model (khái niệm) và Relational model (logic).
