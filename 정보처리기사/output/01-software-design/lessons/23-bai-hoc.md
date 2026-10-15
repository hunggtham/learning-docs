# 8. UI 및 UX, HCI (UI, UX, HCI)

## 학습 목표 (Mục tiêu)
- Phân biệt bản chất và ranh giới giữa 3 khái niệm tương tác người - máy nền tảng: `HCI` (Tương tác Người - Máy), `UX` (Trải nghiệm người dùng), và `UI` (Giao diện người dùng).
- Nắm vững mối quan hệ tương hỗ: HCI là nền tảng nghiên cứu học thuật -> UX là cảm xúc và trải nghiệm tổng thể -> UI là lớp vỏ tiếp xúc trực quan bên ngoài.
- Nhận diện các tiêu chí đánh giá trải nghiệm người dùng theo mô hình kim tự tháp tổ ong (User Experience Honeycomb).

## 핵심 키워드 (Từ khóa)
- HCI (Human-Computer Interaction / 인간-컴퓨터 상호작용)
- UX (User Experience / 사용자 경험)
- UI (User Interface / 사용자 인터페이스)
- 상호작용성 (Tính tương tác / Interactivity)
- 감성·인지·만족도 (Cảm xúc, nhận thức, mức độ hài lòng)
- 접근성 (Tính dễ tiếp cận / Accessibility)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([5. 요구공학](22-bai-hoc.md)):** Sau khi quản lý yêu cầu chức năng, bài này tập trung vào trải nghiệm phi chức năng tinh tế nhất của người dùng thông qua góc nhìn tương tác học.
- **Tiếp nối sang bài sau ([5. 소프트웨어 아키텍처 및 설계](24-bai-hoc.md)):** Chuyển từ tầng trải nghiệm người dùng sang kiến trúc tổng thể phần mềm và các tiêu chuẩn chất lượng quốc tế ISO/IEC 9126.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững câu định nghĩa phân biệt: UI là "cái nhìn thấy và chạm vào", UX là "cảm xúc và sự hài lòng đọng lại", HCI là "khoa học tối ưu hóa tương tác người - máy".
- Đọc TẦNG B để hiểu rõ tại sao một sản phẩm có UI đẹp long lanh nhưng luồng xử lý giật lag và phức tạp thì UX vẫn bị đánh giá là thảm họa.

---

## 8. UI 및 UX, HCI (UI, UX, HCI)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **So sánh 3 khái niệm tương tác then chốt:**
  - **1. HCI (Human-Computer Interaction - Tương tác Người - Máy):**
    - Là ngành khoa học nghiên cứu sự tương tác giữa con người (`인간`) và hệ thống máy tính (`컴퓨터`) nhằm thiết kế các hệ thống an toàn, hiệu quả và tối ưu hóa năng suất lao động cho con người.
    - Trọng tâm: Tối ưu hóa tính khả dụng (Usability), công thái học (Ergonomics) và sự thuận tiện trong thao tác.
  - **2. UX (User Experience - Trải nghiệm người dùng):**
    - Là **toàn bộ cảm xúc, thái độ, nhận thức và sự thỏa mãn tổng thể (`총체적인 감정과 반응`)** mà người dùng trải qua trước, trong và sau khi tương tác với sản phẩm hoặc dịch vụ.
    - Mang tính chủ quan, biến đổi theo ngữ cảnh sử dụng và kỳ vọng cá nhân.
  - **3. UI (User Interface - Giao diện người dùng):**
    - Là **bề mặt tiếp xúc trực quan, vật lý cụ thể (`시각적·물리적 접점`)** giúp người dùng truyền lệnh và nhận phản hồi từ hệ thống (màn hình hiển thị, icon, bảng màu, font chữ, nút bấm).
  - **Mối quan hệ thứ bậc:** $\text{HCI (Khoa học nền tảng)} \rightarrow \text{UX (Mục tiêu trải nghiệm cảm xúc)} \rightarrow \text{UI (Phương tiện hiện thực hóa trực quan)}$.
- **7 yếu tố cấu thành trải nghiệm người dùng (UX Honeycomb):**
  1. `유용성 (Useful)`: Sản phẩm có giải quyết được vấn đề thực tế không?
  2. `사용성 (Usable)`: Thao tác có dễ dàng, không gây ức chế không?
  3. `매력성 (Desirable)`: Thiết kế hình ảnh, thương hiệu có lôi cuốn không?
  4. `검색성 (Findable)`: Thông tin cần tìm có dễ định vị trên màn hình không?
  5. `접근성 (Accessible)`: Người khuyết tật, người cao tuổi có tiếp cận được không?
  6. `신뢰성 (Credible)`: Dữ liệu và dịch vụ có đáng tin cậy và an toàn không?
  7. `가치성 (Valuable)`: Sản phẩm có đem lại giá trị thặng dư cho người dùng và doanh nghiệp không?
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"UI và UX là hai thuật ngữ đồng nghĩa có thể dùng thay thế nhau?"* -> **Sai hoàn toàn**. UI là giao diện hữu hình, còn UX là cảm xúc trải nghiệm vô hình bao trùm.
  - **Bẫy 2:** *"Một phần mềm có giao diện UI bắt mắt chắc chắn sẽ có trải nghiệm người dùng UX tốt?"* -> **Sai**. Nếu UI đẹp nhưng tải trang chậm, chuyển khoản bị lỗi thì UX vẫn cực kỳ kém.
- **한 문장 설명 (Câu chốt ghi nhớ):** "HCI là khoa học tương tác, UI là mặt tiền giao diện, UX là cảm xúc đọng lại trong lòng người dùng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ phân biệt thực tế:**
  - Hãy tưởng tượng một chiếc ấm trà:
    - Vòi ấm, quai cầm, nắp ấm và hoa văn trang trí bên ngoài chính là **UI**.
    - Việc tính toán quai ấm cách nhiệt bao nhiêu độ, góc nghiêng vòi ấm bao nhiêu để nước không đổ vào tay người rót là nghiên cứu **HCI**.
    - Cảm giác khi cầm ấm lên thấy vừa tay, rót nước êm ái không văng tung tóe, thưởng thức trà thấy thư thái chính là **UX**. Nếu vòi ấm đặt ngược phía quai cầm làm nước sôi đổ vào tay người dùng, đó là UI kỳ quặc và UX tồi tệ.

### 복습 체크리스트
- [ ] Phân biệt rõ định nghĩa của 3 thuật ngữ: HCI, UX, và UI.
- [ ] Nhớ mối quan hệ thứ bậc giữa HCI (khoa học) -> UX (trải nghiệm) -> UI (giao diện cụ thể).
- [ ] Nhớ tính chất của UX là bao trùm cả cảm xúc, nhận thức trước và sau khi sử dụng.
- [ ] Nêu được ít nhất 4 yếu tố trong mô hình tổ ong UX (Useful, Usable, Desirable, Accessible).
