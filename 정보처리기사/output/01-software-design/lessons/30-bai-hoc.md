# 3. 모듈 (Module)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của Độ kết hợp (`결합도 - Coupling`) như thước đo mức độ phụ thuộc lẫn nhau giữa các mô-đun phần mềm.
- Thuộc nằm lòng thứ tự 6 cấp độ của 결합도 từ yếu nhất (tốt nhất) đến mạnh nhất (tồi tệ nhất): Dữ liệu < Stamp < Điều khiển < Bên ngoài < Dùng chung < Nội dung.
- Phân biệt bản chất kỹ thuật của từng loại kết hợp qua các kịch bản truyền tham số, dùng biến toàn cục và can thiệp bộ nhớ trong đề thi.

## 핵심 키워드 (Từ khóa)
- 결합도 (Độ kết hợp / Coupling / 모듈 간의 상호 의존성)
- 자료 결합도 (Data Coupling / 파라미터 전달 / Tốt nhất)
- 스탬프 결합도 (Stamp Coupling / 자료구조 전달)
- 제어 결합도 (Control Coupling / 제어 플래그 전달)
- 외부 결합도 (External Coupling / 외부 데이터 공유)
- 공통 결합도 (Common Coupling / 전역 변수 공유)
- 내용 결합도 (Content Coupling / 내부 자료 직접 참조 / Tồi tệ nhất)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([7. 설계 도구 및 모듈화 심화](29-bai-hoc.md)):** Sau khi xem xét nguyên lý mô-đun hóa, bài này cung cấp công cụ định lượng đầu tiên để đánh giá chất lượng thiết kế mô-đun: Độ kết hợp (Coupling).
- **Tiếp nối sang bài sau ([2. 모듈 (Module) & 독립성 (Independence)](31-bai-hoc.md)):** Khảo sát thước đo đối trọng thứ hai của thiết kế mô-đun: Độ gắn kết nội bộ (`응집도 - Cohesion`).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc làu câu thần chú 6 chữ cái: **자 - 스 - 제 - 외 - 공 - 내** (Data < Stamp < Control < External < Common < Content) - đây là câu hỏi kinh điển có mặt trong 100% đề thi.
- Đọc TẦNG B để phân tích ví dụ mã nguồn minh họa sự khác nhau giữa Data Coupling (tốt) và Stamp/Control Coupling (nguy cơ tiềm ẩn).

---

## 3. 모듈 (Module)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Độ kết hợp - 결합도 / Coupling):**
  - Là thước đo mức độ phụ thuộc lẫn nhau (`상호 의존 정도`) giữa hai hay nhiều mô-đun trong hệ thống phần mềm.
  - **Nguyên tắc vàng thiết kế:** **결합도는 낮을수록 좋다 (Độ kết hợp CÀNG THẤP CÀNG TỐT)**. 결합도 càng thấp thì mô-đun càng độc lập, khi sửa một mô-đun sẽ không làm hỏng các mô-đun khác, hệ thống dễ kiểm thử và dễ bảo trì.
- **Thứ tự 6 cấp độ 결합도 (Từ Yếu nhất/Tốt nhất $\rightarrow$ Mạnh nhất/Xấu nhất):**
  $$\text{자료 (Data)} < \text{스탬프 (Stamp)} < \text{제어 (Control)} < \text{외부 (External)} < \text{공통 (Common)} < \text{내용 (Content)}$$
  - 💡 **Thần chú ghi nhớ:** **자 - 스 - 제 - 외 - 공 - 내** (Dữ liệu -> Stamp -> Điều khiển -> Ngoài -> Chung -> Nội dung).
- **Đặc trưng chi tiết của 6 cấp độ:**
  1. **자료 결합도 (Data Coupling - Kết hợp dữ liệu - TỐT NHẤT):**
     - Mô-đun A gọi mô-đun B và **chỉ truyền các giá trị dữ liệu thô đơn thuần (`단순한 데이터 값`)** qua tham số (Parameter) của phương thức (ví dụ: truyền `int a, int b`).
  2. **스탬프 결합도 (Stamp Coupling - Kết hợp cấu trúc):**
     - Mô-đun A truyền **cả một cấu trúc dữ liệu phức tạp (`배열, 레코드, 구조체, 객체`)** cho mô-đun B, dù mô-đun B thực tế chỉ sử dụng một vài trường nhỏ bên trong cấu trúc đó.
  3. **제어 결합도 (Control Coupling - Kết hợp điều khiển):**
     - Mô-đun A truyền một **tín hiệu cờ điều khiển (`제어 플래그 - Flag, Switch, Opcode`)** sang mô-đun B nhằm can thiệp và chỉ đạo trực tiếp luồng xử lý bên trong của mô-đun B.
  4. **외부 결합도 (External Coupling - Kết hợp bên ngoài):**
     - Các mô-đun cùng tham chiếu hoặc chia sẻ các biến dữ liệu, giao thức hoặc định dạng được định nghĩa ở bên ngoài hệ sinh thái phần mềm (ví dụ: giao tiếp qua thiết bị phần cứng, định dạng file bên ngoài).
  5. **공통 결합도 (Common Coupling - Kết hợp dùng chung):**
     - Nhiều mô-đun cùng truy cập và chia sẻ **vùng dữ liệu toàn cục (`전역 변수 - Global Variable / Shared Memory`)**. Khi một mô-đun thay đổi giá trị biến toàn cục, tất cả các mô-đun khác đều bị ảnh hưởng.
  6. **내용 결합도 (Content Coupling - Kết hợp nội dung - TỒI TỆ NHẤT):**
     - Một mô-đun **trực tiếp tham chiếu hoặc can thiệp sửa đổi dữ liệu nội bộ hay mã lệnh bên trong của một mô-đun khác** mà không thông qua bất kỳ hàm hay giao diện công khai nào.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Cấp độ kết hợp nào là tốt nhất mang lại tính độc lập cao nhất?"* -> **자료 결합도 (Data Coupling)**.
  - **Bẫy 2:** *"Cấp độ kết hợp nào là tồi tệ nhất làm mất tính độc lập của mô-đun?"* -> **내용 결합도 (Content Coupling)**.
  - **Bẫy 3:** *"Khi một mô-đun truyền một cờ Flag (True/False) để quyết định nhánh if-else bên trong mô-đun khác thì đó là kết hợp gì?"* -> **제어 결합도 (Control Coupling)**.
  - **Bẫy 4:** *"Nhiều mô-đun cùng đọc/ghi một biến toàn cục (Global Variable) thì đó là kết hợp gì?"* -> **공통 결합도 (Common Coupling)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Coupling càng thấp càng tốt: Data truyền giá trị thô tốt nhất, Stamp truyền cả struct, Control truyền Flag, Common dùng biến chung, Content thò tay vào ruột tồi tệ nhất".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa qua mã nguồn Java:**
  - **Data Coupling (Tốt):** `calcTax(double income)` -> Chỉ truyền 1 số thực đơn thuần.
  - **Stamp Coupling (Chưa tối ưu):** `calcTax(Employee emp)` -> Hàm tính thuế chỉ cần trường lương nhưng ta lại ném cả đối tượng `emp` (chứa tên, địa chỉ, số CMND, gia cảnh) vào hàm, tạo sự phụ thuộc cấu trúc không cần thiết.
  - **Control Coupling (Xấu):** `processOrder(Order o, int mode)` -> Nếu `mode == 1` thì thanh toán thẻ, `mode == 2` thì gửi hàng. Hàm bị chia nhánh theo chỉ đạo của bên ngoài, giảm tính đóng gói.

### 복습 체크리스트
- [ ] Khẳng định được nguyên tắc vàng: 결합도는 낮을수록 좋다.
- [ ] Đọc đúng thứ tự 6 cấp độ từ thấp đến cao: 자료 < 스탬프 < 제어 < 외부 < 공통 < 내용.
- [ ] Nhận diện được ví dụ của Data Coupling (truyền giá trị đơn thuần).
- [ ] Nhận diện được ví dụ của Control Coupling (truyền cờ điều khiển Flag).
- [ ] Nhận diện được ví dụ của Common Coupling (dùng chung biến toàn cục 전역 변수).
- [ ] Nhớ 내용 결합도 (Content Coupling) là tồi tệ nhất.
