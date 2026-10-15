# 104. 데이터 모델에 표시할 요소 (Elements of Data Model)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và ý nghĩa của mô hình dữ liệu (데이터 모델).
- Thuộc lòng 3 thành phần bắt buộc phải có trong một mô hình dữ liệu: Cấu trúc (`구조 / Structure`), Thao tác (`연산 / Operation`), và Ràng buộc (`제약 조건 / Constraint`).
- Phân biệt bản chất tĩnh của Cấu trúc với bản chất động của Thao tác và các quy tắc toàn vẹn của Ràng buộc trong đề thi.

## 핵심 키워드 (Từ khóa)
- 데이터 모델 (Mô hình dữ liệu / Data Model)
- 구조 (Cấu trúc / Structure)
- 정적 성질 (Tính chất tĩnh / Static Properties)
- 연산 (Thao tác / Phép toán / Operation)
- 동적 성질 (Tính chất động / Dynamic Properties)
- 제약 조건 (Điều kiện ràng buộc / Constraints)
- 무결성 규정 (Quy tắc toàn vẹn / Integrity Rules)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([02-bai-hoc.md](02-bai-hoc.md), [05-bai-hoc.md](05-bai-hoc.md)):** Ở bước thiết kế logic, ta đã biết mô hình hóa dữ liệu là nhiệm vụ trọng tâm. Bài học này đi sâu vào giải phẫu 3 thành phần cốt lõi cấu thành nên bất kỳ một mô hình dữ liệu nào.
- **Tiếp nối sang các bài sau ([07-bai-hoc.md](07-bai-hoc.md), [08-bai-hoc.md](08-bai-hoc.md)):** Sau khi nắm 3 thành phần tổng quát, ta sẽ áp dụng chúng vào mô hình dữ liệu phổ biến nhất trong kỳ thi: **Mô hình dữ liệu quan hệ (관계형 데이터 모델)** với bảng, khóa và các phép đại số quan hệ.

## 읽는 방법 (Cách đọc)
- Học thuộc công thức: **Cấu trúc (Structure) = Tĩnh; Thao tác (Operation) = Động; Ràng buộc (Constraint) = Quy tắc**.
- Đề thi thường cho định nghĩa của một thành phần và yêu cầu chọn tên tiếng Hàn (`구조`, `연산`, hay `제약 조건`).

---

## 104. 데이터 모델에 표시할 요소 (Elements of Data Model)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa):** Mô hình dữ liệu là công cụ trừu tượng hóa nhằm mô tả cấu trúc dữ liệu, mối quan hệ giữa các dữ liệu, ngữ nghĩa của dữ liệu và các ràng buộc nhất quán trong cơ sở dữ liệu. Mọi mô hình dữ liệu đều phải thể hiện đủ 3 yếu tố: **구조**, **연산**, **제약 조건**.
- **3 yếu tố cốt lõi của Mô hình dữ liệu (데이터 모델의 3요소):**
  1. **구조 (Structure - Cấu trúc):**
     - Biểu diễn mối quan hệ giữa các kiểu thực thể (Entity Types).
     - Thể hiện **cấu trúc dữ liệu và tính chất tĩnh (정적 성질)** của hệ thống.
     - *Ví dụ:* Các cột trong bảng, kiểu dữ liệu của thuộc tính, mối quan hệ 1:N giữa 2 bảng.
  2. **연산 (Operation - Thao tác / Phép toán):**
     - Đặc tả các thao tác xử lý dữ liệu thực tế lưu trữ trong CSDL.
     - Là công cụ cơ bản để thao tác CSDL, thể hiện **tính chất động (동적 성질)** của hệ thống.
     - *Ví dụ:* Các phép toán thêm (`INSERT`), sửa (`UPDATE`), xóa (`DELETE`), tìm kiếm/chọn lọc (`SELECT`).
  3. **제약 조건 (Constraint - Ràng buộc):**
     - Các quy tắc logic mà dữ liệu thực tế lưu trong CSDL bắt buộc phải tuân theo.
     - Đảm bảo tính toàn vẹn dữ liệu (Data Integrity).
     - *Ví dụ:* Khóa chính không được `NULL` (Toàn vẹn thực thể), Khóa ngoại phải tham chiếu hợp lệ (Toàn vẹn tham chiếu), Tuổi phải `> 0` (Ràng buộc miền giá trị).
- **시험 포인트 (Điểm thi trọng tâm):**
  - **Cách đề thi hỏi:** Đề thi trắc nghiệm thường hỏi: *"Đặc tính nào thể hiện tính chất tĩnh của dữ liệu?"* → Chọn ngay **구조 (Structure)**; *"Đặc tính nào thể hiện thao tác xử lý thực tế (tính chất động)?"* → Chọn ngay **연산 (Operation)**.
  - **Mẹo nhớ:** **Cấu - Toán - Buộc** (Cấu trúc tĩnh, Toán tử động, Ràng buộc quy tắc).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - Đề thi có thể đưa ra các từ gây nhiễu như `스키마 (Schema)`, `도메인 (Domain)`, `인덱스 (Index)` để hỏi đâu KHÔNG PHẢI là 1 trong 3 yếu tố của mô hình dữ liệu. Hãy nhớ chỉ có đúng 3 thành phần: **구조, 연산, 제약 조건**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Cấu trúc định hình (tĩnh), Thao tác xử lý (động), Ràng buộc bảo vệ tính đúng đắn".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế vận hành của 3 yếu tố trong RDBMS thực tế:**
  - Khi bạn tạo một bảng bằng lệnh `CREATE TABLE SinhVien (MaSV INT PRIMARY KEY, Tuoi INT CHECK (Tuoi >= 18))`:
    - `SinhVien (MaSV INT, Tuoi INT)` chính là **Cấu trúc (구조)**.
    - `PRIMARY KEY` và `CHECK (Tuoi >= 18)` chính là **Ràng buộc (제약 조건)**.
    - Khi bạn viết `SELECT * FROM SinhVien WHERE Tuoi > 20`, đó chính là **Thao tác (연산)**.
- **Tại sao cần cả 3 yếu tố?**
  - Nếu chỉ có Cấu trúc mà không có Thao tác, CSDL chỉ là một khung xương chết không thể dùng.
  - Nếu có Thao tác mà không có Ràng buộc, bất kỳ ai cũng có thể chèn dữ liệu rác, số âm, trùng khóa làm CSDL bị sụp đổ tính nhất quán.
- **Liên hệ mạch kiến thức:**
  - Bài này đặt nền móng lý thuyết. Bài 07 và Bài 08 kế tiếp sẽ đi vào cụ thể: Mô hình quan hệ áp dụng 3 yếu tố này như thế nào (Cấu trúc = Bảng/Relation; Thao tác = Đại số quan hệ; Ràng buộc = Toàn vẹn thực thể/tham chiếu).

### 복습 체크리스트
- [ ] Kể tên chuẩn 3 yếu tố của mô hình dữ liệu: 구조, 연산, 제약 조건.
- [ ] Phân biệt được tính chất tĩnh (정적 성질 - 구조) và tính chất động (동적 성질 - 연산).
- [ ] Nêu được vai trò của 제약 조건 là đảm bảo tính toàn vẹn dữ liệu.
