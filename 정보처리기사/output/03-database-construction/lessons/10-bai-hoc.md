# 105. E-R 다이어그램 (E-R Diagram)

## 학습 목표 (Mục tiêu)
- Nắm vững phân loại chi tiết các loại thuộc tính trong mô hình E-R: Thuộc tính đơn vs Phức hợp, Đơn trị vs Đa trị, Lưu trữ vs Suy diễn.
- Thuộc lòng ký hiệu hình học chuyên biệt cho từng loại thuộc tính trên sơ đồ E-R Peter Chen.
- Giải quyết chính xác các câu hỏi tình huống về lựa chọn thuộc tính và chuyển đổi sơ đồ E-R sang bảng trong đề thi.

## 핵심 키워드 (Từ khóa)
- 단순 속성 (Thuộc tính đơn / Simple Attribute)
- 복합 속성 (Thuộc tính phức hợp / Composite Attribute)
- 단일값 속성 (Thuộc tính đơn trị / Single-valued Attribute)
- 다중값 속성 (Thuộc tính đa trị / Multi-valued Attribute)
- 저장 속성 (Thuộc tính lưu trữ / Stored Attribute)
- 유도 속성 (Thuộc tính suy diễn / Derived Attribute)
- 이중 타원 (Hình bầu dục kép / Double Oval)
- 점선 타원 (Hình bầu dục nét đứt / Dashed Oval)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([09-bai-hoc.md](09-bai-hoc.md)):** Sau khi làm quen với 3 thành phần Thực thể - Quan hệ - Thuộc tính, bài học này đào sâu vào thế giới của các loại thuộc tính trong sơ đồ E-R.
- **Tiếp nối sang bài sau ([11-bai-hoc.md](11-bai-hoc.md)):** Sau khi nắm chắc toàn bộ ký hiệu và phân loại E-R, bài tiếp theo sẽ khảo sát mối quan hệ giữa các thực thể và các ràng buộc toàn vẹn khi chuyển đổi sang mô hình dữ liệu quan hệ.

## 읽는 방법 (Cách đọc)
- Học thuộc 2 ký hiệu đặc biệt nhất hay bị hỏi trong đề thi: **Thuộc tính đa trị = Bầu dục kép (이중 타원)**; **Thuộc tính suy diễn = Bầu dục nét đứt (점선 타원)**.
- Ghi nhớ ví dụ phân biệt giữa Lưu trữ (`Ngày sinh`) và Suy diễn (`Tuổi`).

---

## 105. E-R 다이어그램 (E-R Diagram)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Phân loại thuộc tính trong mô hình E-R (속성의 분류):**
  - **단순 속성 (Simple) vs 복합 속성 (Composite):**
    - `단순 속성 (Thuộc tính đơn)`: Không thể phân chia nhỏ hơn thành các phần mang ý nghĩa độc lập (ví dụ: `나이` - Tuổi, `성별` - Giới tính).
    - `복합 속성 (Thuộc tính phức hợp)`: Có thể phân rã thành nhiều thuộc tính thành phần nhỏ hơn (ví dụ: `주소` - Địa chỉ có thể tách thành Tỉnh, Thành phố, Quận; `성명` - Họ tên tách thành Họ và Tên).
  - **단일값 속성 (Single-valued) vs 다중값 속성 (Multi-valued):**
    - `단일값 속성 (Đơn trị)`: Mỗi thực thể chỉ có duy nhất một giá trị tại một thời điểm (ví dụ: `주민등록번호` - Số CCCD, `사번` - Mã nhân viên).
    - `다중값 속성 (Đa trị)`: Một thực thể có thể sở hữu một tập hợp nhiều giá trị (ví dụ: `전화번호` - một người có thể có 2-3 số ĐT; `취미` - Sở thích; `학력` - Bằng cấp).
      - **Ký hiệu E-R:** **이중 타원 (Hình bầu dục kép)**.
  - **저장 속성 (Stored) vs 유도 속성 (Derived):**
    - `저장 속성 (Lưu trữ)`: Giá trị gốc được lưu trữ trực tiếp trong CSDL (ví dụ: `생년월일` - Ngày tháng năm sinh).
    - `유도 속성 (Suy diễn)`: Giá trị không cần lưu cứng mà được tính toán tự động dựa trên các thuộc tính khác (ví dụ: `나이` - Tuổi được suy ra từ Ngày sinh; `총점` - Tổng điểm được tính từ điểm thành phần).
      - **Ký hiệu E-R:** **점선 타원 (Hình bầu dục nét đứt)**.
- **2. Tổng kết ký hiệu hình học E-R Peter Chen:**
  - `사각형 (Hình chữ nhật)`: Thực thể (`개체`)
  - `이중 사각형 (Hình chữ nhật kép)`: Thực thể yếu (`약한 개체`)
  - `마름모 (Hình thoi)`: Mối quan hệ (`관계`)
  - `이중 마름모 (Hình thoi kép)`: Mối quan hệ xác định thực thể yếu (`식별 관계`)
  - `타원 (Hình bầu dục)`: Thuộc tính (`속성`)
  - `밑줄 타원 (Bầu dục gạch chân)`: Khóa chính (`기본키 속성`)
  - `이중 타원 (Bầu dục kép)`: Thuộc tính đa trị (`다중값 속성`)
  - `점선 타원 (Bầu dục nét đứt)`: Thuộc tính suy diễn (`유도 속성`)
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề thi hay hỏi: *"Ký hiệu nào thể hiện thuộc tính suy diễn (Derived Attribute)?"* → Đáp án là **점선 타원 (Hình bầu dục nét đứt)**.
  - Đề hỏi: *"Địa chỉ (주소) thuộc loại thuộc tính nào?"* → Đáp án là **복합 속성 (Thuộc tính phức hợp)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Đa trị vẽ bầu dục kép, Suy diễn vẽ bầu dục nét đứt".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc chuyển đổi thuộc tính đa trị (Multi-valued Attribute) sang Bảng logic:**
  - Trong mô hình quan hệ (RDBMS), vi phạm giá trị nguyên tử (Atomic Value) là điều cấm kỵ (1NF). Do đó, một thuộc tính đa trị như `전화번호 (Số điện thoại)` khi chuyển sang tầng logic **không thể nằm trong cùng 1 cột của bảng chính**.
  - **Giải pháp chuyển đổi:** Bắt buộc phải tách thành một bảng riêng (ví dụ: bảng `NHAN_VIEN_SDT` gồm `MaNV` và `SoDienThoai`), trong đó cặp `(MaNV, SoDienThoai)` tạo thành khóa chính kết hợp.
- **Tại sao nên dùng Thuộc tính suy diễn (Derived Attribute)?**
  - Giúp tránh dư thừa dữ liệu (Data Redundancy) và tránh mâu thuẫn dữ liệu: Nếu lưu cả `Ngày sinh` lẫn `Tuổi`, hàng năm hệ thống sẽ phải chạy batch job cập nhật lại số tuổi của toàn bộ nhân viên; nếu quên cập nhật, tuổi sẽ bị sai lệch so với ngày sinh. Tính toán động giúp dữ liệu luôn chính xác 100%.

### 복습 체크리스트
- [ ] Phân biệt rõ 단순 속성 (đơn) và 복합 속성 (phức hợp).
- [ ] Phân biệt rõ 저장 속성 (lưu trữ) và 유도 속성 (suy diễn).
- [ ] Vẽ đúng ký hiệu 이중 타원 (đa trị) và 점선 타원 (suy diễn).
- [ ] Nêu được cách xử lý thuộc tính đa trị khi chuyển sang mô hình quan hệ (tách thành bảng riêng).
