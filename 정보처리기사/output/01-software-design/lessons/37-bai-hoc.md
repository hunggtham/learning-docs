# 11. 디자인 패턴 (Design Pattern)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế hoạt động và ngữ cảnh áp dụng của các Mẫu hành vi (`행위 패턴 - Behavioral Patterns`) tiêu biểu nhất trong 23 mẫu GoF.
- Hiểu sâu nguyên lý của mẫu Quan sát (`Observer Pattern` - mô hình 1-N Publish/Subscribe), mẫu Chiến lược (`Strategy Pattern`), và mẫu Khuôn mẫu thuật toán (`Template Method Pattern`).
- Phân biệt cơ chế hỗ trợ hoàn tác Undo/Redo giữa mẫu Lệnh (`Command`) và mẫu Lưu trạng thái (`Memento`).

## 핵심 키워드 (Từ khóa)
- 행위 패턴 (Mẫu hành vi / Behavioral Patterns)
- Observer (옵서버 / 1:N 알림 / Publish-Subscribe)
- Strategy (전략 / 알고리즘 교체)
- Template Method (템플릿 메소드 / 골격 정의)
- State (상태 / 상태에 따른 행위 변화)
- Command / Memento (커맨드 / 메멘토 / Undo 지원)
- Iterator / Mediator (반복자 / 중재자)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. 디자인 패턴 (Design Patterns - GoF)](36-bai-hoc.md)):** Sau khi xem xét nhóm Tạo dựng và Cấu trúc, bài này hoàn tất trọn bộ 23 mẫu GoF với nhóm Hành vi chuyên điều phối thuật toán và tương tác đối tượng.
- **Tiếp nối sang bài sau ([2. 인터페이스 검토 및 연계 기술](38-bai-hoc.md)):** Chuyển từ thiết kế nội bộ phần mềm sang kỹ thuật liên kết và kiểm tra giao diện giữa các hệ thống doanh nghiệp (EAI, FTR).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ các từ khóa thi trắc nghiệm: "Thông báo 1-N" gắn với Observer; "Hoán đổi thuật toán linh hoạt" gắn với Strategy; "Khung sườn thuật toán ở lớp cha" gắn với Template Method; "Lưu trạng thái để Undo" gắn với Memento.
- Đọc TẦNG B để hiểu rõ sự kết hợp giữa Strategy Pattern và nguyên tắc Open-Closed Principle (OCP) trong kiến trúc mở rộng.

---

## 11. 디자인 패턴 (Design Pattern)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Các Mẫu hành vi (행위 패턴 - Behavioral Patterns) trọng tâm thi trắc nghiệm:**
  1. **Observer (옵서버 패턴 - Mẫu quan sát):**
     - Thiết lập mối quan hệ phụ thuộc **1-N (một - nhiều)** giữa các đối tượng. Khi một đối tượng (Subject) thay đổi trạng thái, **tất cả các đối tượng phụ thuộc đã đăng ký theo dõi (Observers) đều được tự động thông báo và cập nhật (`상태 변화 시 객체들에게 자동 통지`)**.
     - Ứng dụng: Xử lý sự kiện giao diện (Event Listener), Kiến trúc Publish-Subscribe, Bảng tin mạng xã hội.
  2. **Strategy (전략 패턴 - Mẫu chiến lược):**
     - Đóng gói từng thuật toán trong một họ thuật toán thành các lớp độc lập có chung một giao diện (Interface), giúp **thuật toán có thể hoán đổi linh hoạt (`알고리즘을 캡슐화하여 동적으로 교체`)** theo ngữ cảnh mà không ảnh hưởng đến client gọi nó.
     - Ứng dụng: Các thuật toán sắp xếp khác nhau, các cổng thanh toán (Thẻ tín dụng / Ví điện tử / Tiền mặt).
  3. **Template Method (템플릿 메소드 패턴 - Mẫu khuôn mẫu):**
     - Lớp cha định nghĩa **khung sườn cấu trúc của một thuật toán (`알고리즘의 골격 정의`)** trong một phương thức mẫu, nhưng trì hoãn việc cài đặt các bước chi tiết cho các lớp con thực hiện (`세부 구현은 서브클래스에 위임`).
  4. **State (상태 패턴 - Mẫu trạng thái):**
     - Cho phép một đối tượng **thay đổi hành vi khi trạng thái nội bộ của nó thay đổi (`상태에 따라 행동이 변화`)**. Nhìn từ bên ngoài, đối tượng giống như được đổi sang một lớp khác.
  5. **Command (커맨드 패턴 - Mẫu lệnh):**
     - Đóng gói một yêu cầu thao tác thành một **đối tượng độc lập (`요청을 객체로 캡슐화`)**, cho phép tham số hóa các yêu cầu từ phía client, ghi log các thao tác và hỗ trợ tính năng **Hoàn tác (Undo/Redo)**.
  6. **Memento (메멘토 패턴 - Mẫu lưu trữ trạng thái):**
     - Chụp và lưu lại **trạng thái nội bộ của một đối tượng (`객체의 내부 상태를 캡슐화하여 저장`)** mà không vi phạm nguyên tắc đóng gói, cho phép khôi phục lại trạng thái đó khi cần (Rollback / Ctrl+Z).
  7. **Iterator (반복자 패턴 - Mẫu bộ lặp):**
     - Cung cấp phương thức truy cập tuần tự từng phần tử trong một tập hợp dữ liệu phức tạp (List, Set, Tree) mà không làm lộ cấu trúc lưu trữ nội bộ bên trong của tập hợp.
  8. **Mediator (중재자 패턴 - Mẫu trung gian điều phối):**
     - Đóng vai trò là đối tượng trung tâm quản lý giao tiếp giữa các đối tượng phức tạp, biến mối quan hệ nhiều-nhiều (N-N) chằng chịt thành mối quan hệ một-nhiều (1-N) đơn giản, giảm độ kết hợp giữa các đối tượng.
  9. **Chain of Responsibility (책임 연쇄 패턴 - Mẫu chuỗi trách nhiệm):**
     - Chuyển tiếp yêu cầu xử lý qua một chuỗi các đối tượng handler cho đến khi có một đối tượng phù hợp đứng ra giải quyết yêu cầu đó.
  10. **Visitor (방문자 패턴 - Mẫu khách thăm):**
      - Tách rời thuật toán hoặc thao tác xử lý ra khỏi cấu trúc dữ liệu của các phần tử mà nó thao tác, cho phép thêm thao tác mới mà không sửa đổi các lớp phần tử cũ.
  11. **Interpreter (인터프리터 패턴 - Mẫu trình thông dịch):**
      - Định nghĩa ngữ pháp cho một ngôn ngữ và xây dựng bộ thông dịch để phân tích cú pháp các câu lệnh trong ngôn ngữ đó (ví dụ: bộ phân tích biểu thức chính quy Regex, bộ phân tích SQL).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Mô hình Publish-Subscribe trong đó một đối tượng đổi trạng thái làm các đối tượng khác tự động cập nhật là mẫu nào?"* -> **Observer (옵서버)**.
  - **Bẫy 2:** *"Hoán đổi thuật toán linh hoạt trong runtime là mẫu nào?"* -> **Strategy (전략)**.
  - **Bẫy 3:** *"Khung sườn thuật toán viết ở lớp cha, chi tiết giao lớp con là mẫu nào?"* -> **Template Method (템플릿 메소드)**.
  - **Bẫy 4:** *"Lưu lại trạng thái nội bộ của đối tượng để hỗ trợ tính năng Undo/Rollback là mẫu nào?"* -> **Memento (메멘토)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Observer 1-N tự động báo tin; Strategy tráo đổi thuật toán; Template Method cha giữ khung con làm ruột; Memento lưu ảnh chụp để Undo".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh State Pattern và Strategy Pattern:**
  - Về mặt cấu trúc lớp (Class Diagram), State và Strategy hoàn toàn giống hệt nhau (đều gồm Context chứa tham chiếu đến một Interface).
  - Khác biệt bản chất:
    - Trong **Strategy**: Client tự tay quyết định và đưa thuật toán cụ thể vào (ví dụ: người dùng chọn nút "Thanh toán bằng Paypal").
    - Trong **State**: Trạng thái tự động tự chuyển đổi sang trạng thái tiếp theo dựa trên các sự kiện nội bộ của Context (ví dụ: máy bán nước tự động từ trạng thái `Chờ bỏ tiền` tự nhảy sang `Đã nhận tiền` khi cảm biến nhận được xu).

### 복습 체크리스트
- [ ] Nhận diện được hành vi của Observer Pattern (1-N thông báo tự động).
- [ ] Nhận diện được hành vi của Strategy Pattern (đóng gói và hoán đổi thuật toán linh hoạt).
- [ ] Phân biệt được Template Method (khung sườn ở cha, chi tiết ở con).
- [ ] Nhớ vai trò của Memento và Command trong việc hỗ trợ Undo/Redo.
- [ ] Kể tên đủ 11 mẫu thuộc nhóm hành vi (행위 패턴).
