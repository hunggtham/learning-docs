# 4. 사용자 인터페이스 (Giao diện người dùng - UI)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và đặc trưng kỹ thuật của Giao diện người dùng (`UI - User Interface`) trong thiết kế phần mềm hiện đại.
- Thuộc nằm lòng 4 nguyên tắc vàng trong thiết kế UI (`UI 4대 기본 원칙`): Tính trực quan (`직관성`), Tính hữu hiệu (`유효성`), Tính dễ học (`학습성`), và Tính linh hoạt (`유연성`).
- Phân biệt các mô hình giao diện người dùng kinh điển: Giao diện dòng lệnh (`CLI`), Giao diện đồ họa (`GUI`), và Giao diện tự nhiên (`NUI`).

## 핵심 키워드 (Từ khóa)
- 사용자 인터페이스 (Giao diện người dùng / User Interface - UI)
- UI 4대 기본 원칙 (4 nguyên tắc vàng của UI)
- 직관성 (Tính trực quan / Intuitiveness)
- 유효성 (Tính hữu hiệu / Effectiveness)
- 학습성 (Tính dễ học / Learnability)
- 유연성 (Tính linh hoạt / Flexibility)
- CLI / GUI / NUI (Command Line / Graphical / Natural User Interface)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([7. UML 심화](18-bai-hoc.md)):** Sau khi hoàn thành thiết kế mô hình phân tích cấu trúc và hành vi hệ thống, bài này bước sang giai đoạn thiết kế trải nghiệm người dùng qua giao diện UI.
- **Tiếp nối sang bài sau ([1. 사용자 인터페이스](20-bai-hoc.md)):** Mở rộng các cử chỉ tương tác di động (Mobile Gestures), giao diện hữu cơ (OUI) và 4 công cụ tạo mẫu giao diện (Wireframe, Mockup, Storyboard, Prototype).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 4 nguyên tắc UI bằng mẹo: **Trực Học Hằng Ngày** (Trực quan - Học hỏi - Hữu hiệu - Nhuần nhuyễn/Linh hoạt) - đề thi thường đưa ra một phát biểu rồi hỏi thuộc nguyên tắc nào.
- Đọc TẦNG B để hiểu sâu cách áp dụng các nguyên tắc này vào việc giảm thiểu thao tác sai của người dùng trong các hệ thống nghiệp vụ thực tế.

---

## 4. 사용자 인터페이스 (Giao diện người dùng - UI)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa UI):** Là phương tiện và môi trường tương tác giúp người dùng giao tiếp, điều khiển hệ thống và nhận kết quả phản hồi từ phần mềm hoặc thiết bị phần cứng.
- **Đặc trưng kỹ thuật của UI:**
  - Nâng cao tính tiện lợi (`편리성`) và khả năng dễ đọc (`가독성`) cho người sử dụng.
  - Rút ngắn thời gian thao tác và hạn chế sai sót khi vận hành công việc.
  - **Là thành phần có tần suất thay đổi nhiều nhất (`변경이 가장 많이 발생`)** trong suốt vòng đời của một dự án phần mềm do phản hồi liên tục của người dùng.
- **UI 4대 기본 원칙 (4 nguyên tắc vàng bắt buộc phải thuộc):**
  1. **직관성 (Intuitiveness - Tính trực quan):**
     - Bất kỳ ai nhìn vào màn hình cũng có thể **dễ dàng hiểu ngay lập tức** cách thức vận hành mà không cần phải đọc tài liệu hướng dẫn dày đặc.
  2. **유효성 (Effectiveness - Tính hữu hiệu):**
     - Đảm bảo người dùng có thể **đạt được mục tiêu công việc một cách chính xác và trọn vẹn** (`사용자의 목적을 정확하고 완벽하게 달성`).
  3. **학습성 (Learnability - Tính dễ học):**
     - Giúp người dùng **dễ dàng học hỏi và làm quen** với các chức năng trong thời gian ngắn nhất; sau một thời gian dài không dùng vẫn có thể thao tác lại dễ dàng.
  4. **유연성 (Flexibility - Tính linh hoạt):**
     - Đáp ứng tối đa các yêu cầu đa dạng và thói quen sử dụng khác nhau của người dùng; có cơ chế **ngăn chặn sai sót và cho phép người dùng hoàn tác (Undo/Redo)** khi có thao tác nhầm lẫn.
- **Các thế hệ giao diện người dùng:**
  - `CLI (Command Line Interface)`: Tương tác thuần túy qua dòng lệnh văn bản gõ từ bàn phím (DOS, Bash Shell).
  - `GUI (Graphical User Interface)`: Tương tác qua đồ họa trực quan (Cửa sổ, Icon, Menu, Con trỏ chuột - WIMP) xuất hiện trên Windows, macOS.
  - `NUI (Natural User Interface)`: Tương tác bằng các hành vi tự nhiên của con người như Giọng nói, Chạm đa điểm, Cử chỉ cơ thể (Siri, Kinect).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Nguyên tắc nào quy định hệ thống phải cho phép người dùng sửa đổi thao tác sai và hạn chế lỗi nhầm lẫn?"* -> **유연성 (Tính linh hoạt)**.
  - **Bẫy 2:** *"Nguyên tắc nào đảm bảo người dùng hoàn thành mục tiêu công việc một cách chính xác và đầy đủ?"* -> **유효성 (Tính hữu hiệu)**, KHÔNG PHẢI 직관성 (Trực quan).
  - **Bẫy 3:** *"Thành phần nào trong phần mềm thường xuyên bị yêu cầu thay đổi nhiều nhất?"* -> **사용자 인터페이스 (UI)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "UI là cầu nối người-máy thay đổi nhiều nhất; 4 nguyên tắc vàng: Trực quan dễ hiểu, Hữu hiệu đạt đích, Học hỏi mau nhớ, Linh hoạt sửa sai".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tình huống thực tế minh họa 4 nguyên tắc UI:**
  - **Trực quan (직관성):** Nút "Thùng rác" có hình cái sọt rác, ai nhìn vào cũng biết là để xóa file.
  - **Hữu hiệu (유효성):** Khi bấm "Chuyển khoản", hệ thống chuyển đúng số tiền đến đúng tài khoản người nhận, không làm mất mát thông tin.
  - **Dễ học (학습성):** Các phím tắt chuẩn như `Ctrl + C` (Copy), `Ctrl + V` (Paste) đồng bộ trên mọi ứng dụng, người mới dùng 1 lần là nhớ mãi.
  - **Linh hoạt (유연성):** Khi người dùng lỡ tay bấm "Xóa tài liệu quan trọng", hệ thống hiển thị hộp thoại xác nhận "Bạn có chắc chắn muốn xóa không?" và hỗ trợ phím `Ctrl + Z` để khôi phục lại ngay.

### 복습 체크리스트
- [ ] Định nghĩa được UI và nhớ đặc trưng là phần thay đổi nhiều nhất trong phần mềm.
- [ ] Đọc tên vanh vách 4 nguyên tắc cơ bản của UI: 직관성, 유효성, 학습성, 유연성.
- [ ] Phân biệt được định nghĩa cụ thể của từng nguyên tắc trong các câu hỏi tình huống đề thi.
- [ ] Phân biệt được sự phát triển từ CLI sang GUI và NUI.
