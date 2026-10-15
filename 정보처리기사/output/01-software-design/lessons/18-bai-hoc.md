# 7. UML 심화 (Advanced UML)

## 학습 목표 (Mục tiêu)
- Nắm vững lịch sử hình thành của UML do tổ chức OMG chuẩn hóa, hợp nhất từ 3 phương pháp luận hướng đối tượng kinh điển của Rumbaugh (OMT), Booch, và Jacobson (OOSE).
- Hiểu cấu trúc và cơ chế chuyển đổi trạng thái trong Biểu đồ trạng thái (`상태 다이어그램 - State Diagram`) và phân luồng song song trong Biểu đồ hoạt động (`활동 다이어그램 - Activity Diagram`).
- Nắm vững bộ ba Stereotype phân tích kiến trúc ECB kinh điển: Thực thể (`<<entity>>`), Biên giới giao diện (`<<boundary>>`), và Điều khiển logic (`<<control>>`).

## 핵심 키워드 (Từ khóa)
- OMG (Object Management Group / 표준화 기구)
- Rumbaugh (OMT), Booch, Jacobson (OOSE / Use Case 창시자)
- 상태 다이어그램 (State Diagram / 상태 전이, 이벤트)
- 활동 다이어그램 (Activity Diagram / 포크-조인 / Fork-Join)
- ECB 모델 (Entity-Control-Boundary: `<<entity>>`, `<<boundary>>`, `<<control>>`)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([5. UML 구성요소 상세](17-bai-hoc.md)):** Sau khi xem xét các thành phần cơ bản và cú pháp Class/Sequence, bài này nâng tầm kiến thức với nguồn gốc lịch sử và các biểu đồ phân tích chuyên sâu (State, Activity, ECB).
- **Tiếp nối sang bài sau ([4. 사용자 인터페이스](19-bai-hoc.md)):** Từ việc mô hình hóa phân tích chuyển sang thiết kế Giao diện người dùng (UI), các nguyên tắc tương tác người - máy.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ chuẩn xác 3 tác giả sáng lập UML và 3 vai trò kiến trúc ECB (Boundary - Giao diện, Control - Xử lý, Entity - Dữ liệu).
- Đọc TẦNG B để hiểu cơ chế Fork và Join điều khiển các luồng thực thi song song trong Activity Diagram.

---

## 7. UML 심화 (Advanced UML)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Nguồn gốc lịch sử chuẩn hóa UML (UML 표준화 역사):**
  - Được tổ chức **OMG (Object Management Group)** chính thức công nhận làm tiêu chuẩn quốc tế vào năm 1997.
  - Hợp nhất từ 3 phương pháp phân tích và thiết kế hướng đối tượng hàng đầu:
    1. **James Rumbaugh:** Đề xuất phương pháp **OMT (Object Modeling Technique)** - mô hình hóa theo 3 góc nhìn: Đối tượng (Object), Động (Dynamic - State chart), và Chức năng (Functional - DFD).
    2. **Grady Booch:** Đề xuất phương pháp **Booch Method** - tiếp cận theo mô hình phân tích vi mô và thiết kế vĩ mô.
    3. **Ivar Jacobson:** Đề xuất phương pháp **OOSE (Object-Oriented Software Engineering)** - người phát minh ra khái niệm **Use Case (유스케이스)** để nắm bắt yêu cầu người dùng.
- **2. Đi sâu Biểu đồ trạng thái (State Diagram) & Biểu đồ hoạt động (Activity Diagram):**
  - **상태 다이어그램 (State Diagram / Biểu đồ trạng thái):**
    - Biểu diễn vòng đời và chuỗi biến đổi trạng thái của duy nhất một đối tượng cụ thể từ khi sinh ra đến khi bị hủy.
    - `시작 상태 (Trạng thái bắt đầu)`: Biểu diễn bằng **Dấu chấm tròn đen đặc (채워진 원)**.
    - `종료 상태 (Trạng thái kết thúc)`: Biểu diễn bằng **Dấu chấm tròn đen nằm bên trong một vòng tròn (이중 원)**.
    - `상태 전이 (Chuyển trạng thái - Transition)`: Mũi tên có hướng nối giữa các trạng thái kèm theo Sự kiện kích hoạt (Event) và Điều kiện canh gác (Guard Condition: `[condition]`).
  - **활동 다이어그램 (Activity Diagram / Biểu đồ hoạt động):**
    - Biểu diễn luồng công việc xử lý logic bên trong hệ thống (tương tự Flowchart nhưng hỗ trợ xử lý song song).
    - `포크 (Fork - Rẽ nhánh song song)`: Một luồng vào tách thành nhiều luồng chạy song song đồng thời. Biểu diễn bằng **Thanh ngang đen đặc (굵은 수평선)**.
    - `조인 (Join - Hợp nhất luồng)`: Chờ tất cả các luồng song song hoàn tất rồi mới tiếp tục một luồng duy nhất. Biểu diễn bằng **Thanh ngang đen đặc**.
- **3. Mô hình Stereotype kiến trúc ECB (Boundary - Control - Entity):**
  - `<<boundary>>`: Lớp biên giới, chịu trách nhiệm nhận tương tác từ người dùng bên ngoài và hiển thị giao diện (Màn hình form, Web page). Ký hiệu hình tròn có vạch đứng và thanh ngang.
  - `<<control>>`: Lớp điều khiển, chịu trách nhiệm xử lý logic nghiệp vụ, điều phối dữ liệu giữa Boundary và Entity. Ký hiệu hình tròn có mũi tên xoay tròn ở trên đầu.
  - `<<entity>>`: Lớp thực thể, chịu trách nhiệm lưu trữ thông tin trạng thái bền vững (Bảng dữ liệu trong DB, Hồ sơ tài khoản). Ký hiệu hình tròn có vạch chân ngang ở dưới đáy.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Ai là tác giả phát minh ra phương pháp OOSE và đưa khái niệm Use Case vào kỹ nghệ phần mềm?"* -> **Ivar Jacobson (야콥슨)**.
  - **Bẫy 2:** *"Thanh ngang đen đặc trong Activity Diagram dùng để làm gì?"* -> **Đồng bộ hóa các luồng xử lý song song (Fork và Join)**.
  - **Bẫy 3:** *"Lớp tiếp nhận trực tiếp sự kiện từ người dùng trong mô hình phân tích ECB là gì?"* -> **<<boundary>> (Biên giới)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "OMG chuẩn hóa OMT Rumbaugh, Booch và OOSE Jacobson; Fork-Join thanh ngang song song; ECB gồm Biên giới, Điều khiển và Thực thể".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tương quan giữa ECB và mô hình MVC (Model-View-Controller):**
  - Trong thiết kế hệ thống, mô hình phân tích ECB chính là tiền thân trực tiếp của kiến trúc MVC:
    - `<<boundary>>` tương ứng với **View (Giao diện hiển thị)**.
    - `<<control>>` tương ứng với **Controller (Bộ điều khiển nghiệp vụ)**.
    - `<<entity>>` tương ứng với **Model (Mô hình dữ liệu và cơ sở dữ liệu)**.
- **Cơ chế hoạt động của Guard Condition trong State Machine:**
  - Cú pháp chuyển trạng thái: `Tên_Sự_Kiện [Điều_Kiện_Canh_Gác] / Hành_Động`.
  - Ví dụ tại máy ATM: Từ trạng thái `Chờ rút tiền` sang `Nhả tiền` chỉ diễn ra khi có sự kiện `Yêu cầu rút [Số dư >= Số tiền rút] / Đếm tiền`. Nếu điều kiện canh gác sai, quá trình chuyển trạng thái bị chặn đứng.

### 복습 체크리스트
- [ ] Nhớ tên tổ chức OMG chuẩn hóa UML và 3 nhà khoa học: Rumbaugh (OMT), Booch, Jacobson (OOSE).
- [ ] Nhận diện được ký hiệu trạng thái bắt đầu (tròn đen) và kết thúc (vòng tròn đôi có chấm đen) của State Diagram.
- [ ] Giải thích được vai trò của Fork và Join trong xử lý song song ở Activity Diagram.
- [ ] Phân biệt được 3 thành phần của mô hình kiến trúc ECB: Boundary, Control, Entity.
