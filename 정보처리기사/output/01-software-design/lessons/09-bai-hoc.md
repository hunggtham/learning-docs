# 1. 요구사항 개발 기법 (Requirements Elicitation Techniques)

## 학습 목표 (Mục tiêu)
- Nắm vững các phương pháp và kỹ thuật thu thập yêu cầu (`요구사항 도출 기법`) phổ biến trong kỹ nghệ phần mềm.
- Phân biệt rõ các kỹ thuật đặc thù: Phỏng vấn (`인터뷰`), Khảo sát (`설문`), Công não (`브레인스토밍`), Kỹ thuật Delphi (`델파이 기법`), và Tạo nguyên mẫu (`프로토타이핑`).
- Nhớ chính xác đặc trưng mang tính sống còn của kỹ thuật Delphi là **Tính ẩn danh (`익명성`)** và của Brainstorming là **Tuyệt đối cấm chỉ trích (`비판 금지`)**.

## 핵심 키워드 (Từ khóa)
- 요구사항 도출 (Thu thập yêu cầu / Requirements Elicitation)
- 브레인스토밍 (Công não / Brainstorming / 비판 금지)
- 델파이 기법 (Kỹ thuật Delphi / Delphi Method / 전문가 익명성)
- 인터뷰 (Phỏng vấn / Interview)
- 설문 조사 (Khảo sát / Questionnaire / Survey)
- 유스케이스 (Ca sử dụng / Use Case / 액터와 시스템의 상호작용)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([3. 요구사항 분석기법 및 자동화 도구](08-bai-hoc.md)):** Sau khi xem xét các công cụ mô hình hóa luồng dữ liệu (DFD, DD), bài này tập trung vào khâu đầu vào trực tiếp: làm thế nào để khai thác trọn vẹn mong muốn từ người dùng và chuyên gia.
- **Tiếp nối sang bài sau ([12. 요구사항](10-bai-hoc.md)):** Sau khi thu thập yêu cầu bằng các kỹ thuật này, bước tiếp theo là tiến hành quy trình phân tích 5 bước, xác minh và đo lường theo 7 tiêu chí chất lượng đặc tả yêu cầu.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 2 đặc trưng thi trắc nghiệm thường bẫy nhất: Brainstorming cấm phê bình; Delphi dùng chuyên gia giấu tên nhiều vòng để lấy đồng thuận.
- Đọc TẦNG B để hiểu rõ ưu nhược điểm và tình huống phù hợp của từng kỹ thuật khi áp dụng vào các dự án phần mềm thực tế.

---

## 1. 요구사항 개발 기법 (Requirements Elicitation Techniques)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Các kỹ thuật thu thập yêu cầu (도출 기법) cốt lõi:**
  1. **인터뷰 (Interview - Phỏng vấn):**
     - Trao đổi trực tiếp (1-1 hoặc nhóm nhỏ) giữa chuyên viên phân tích và người dùng/khách hàng.
     - Hiệu quả cao trong việc làm rõ các yêu cầu phức tạp, sâu sắc; có thể dùng câu hỏi đóng hoặc câu hỏi mở. Nhược điểm: tốn nhiều thời gian và chi phí.
  2. **설문조사 (Questionnaire / Survey - Khảo sát bằng phiếu câu hỏi):**
     - Sử dụng bộ câu hỏi soạn sẵn gửi đến một lượng lớn người dùng ở các vị trí địa lý phân tán.
     - Thích hợp khi cần thu thập thông tin thống kê đại trà từ nhiều người trong thời gian ngắn. Nhược điểm: tỷ lệ phản hồi có thể thấp, khó đào sâu chi tiết nghiệp vụ mơ hồ.
  3. **브레인스토밍 (Brainstorming - Công não):**
     - Buổi thảo luận tập thể nhằm sản sinh ra càng nhiều ý tưởng mới càng tốt trong thời gian ngắn.
     - **Nguyên tắc vàng thi trắc nghiệm:** **Tuyệt đối không chỉ trích, phê phán (`비판 금지`)**; khuyến khích ý tưởng tự do bay bổng; ưu tiên số lượng ý tưởng hơn chất lượng ban đầu.
  4. **델파이 기법 (Delphi Technique - Kỹ thuật chuyên gia Delphi):**
     - Kỹ thuật trưng cầu ý kiến từ một hội đồng chuyên gia thông qua bảng câu hỏi lặp lại nhiều vòng (`반복적인 설문`).
     - **Đặc trưng sống còn:** **Hoàn toàn ẩn danh (`전문가의 익명성 보장`)**. Các chuyên gia không họp mặt trực tiếp, tránh được hiện tượng bị chi phối tâm lý bởi người có quyền lực hoặc tiếng nói lớn nhất trong phòng họp. Sau mỗi vòng, ý kiến được tổng hợp và gửi lại cho các chuyên gia điều chỉnh cho đến khi đạt được sự đồng thuận cao.
  5. **프로토타이핑 (Prototyping - Tạo mẫu thử nghiệm):**
     - Xây dựng một bản demo giao diện hoặc mô phỏng tương tác để người dùng trực tiếp thao tác thử và phản hồi yêu cầu.
  6. **유스케이스 (Use Case - Ca sử dụng):**
     - Mô tả chuỗi tương tác hoàn chỉnh giữa tác nhân bên ngoài (`액터 - Actor`) và hệ thống (`시스템 - System`) để đạt được một mục tiêu nghiệp vụ cụ thể.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Delphi Technique):** Đề hỏi *"Kỹ thuật nào thu thập ý kiến chuyên gia thông qua nhiều vòng khảo sát ẩn danh nhằm loại bỏ sự chi phối của người có uy thế?"* -> **Chắc chắn là 델파이 기법 (Delphi)**.
  - **Bẫy 2 (Brainstorming Rule):** Đề hỏi *"Trong buổi Brainstorming, các thành viên cần tranh luận và phản bác ngay các ý tưởng phi thực tế?"* -> **Sai hoàn toàn**. Nguyên tắc cốt lõi của Brainstorming là **비판 금지 (Nghiêm cấm phê bình/chỉ trích)** trong giai đoạn phát sinh ý tưởng.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Phỏng vấn đào sâu, Khảo sát diện rộng, Brainstorming cấm phê bình, Delphi chuyên gia ẩn danh nhiều vòng".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh Brainstorming và Delphi trong dự báo công nghệ phần mềm:**
  - Khi nhóm cần giải pháp sáng tạo cho một tính năng giao diện mới, việc ngồi cùng phòng và áp dụng Brainstorming sẽ kích thích tư duy tương tác liên tục giữa các thành viên.
  - Ngược lại, khi cần ước lượng ngân sách hoặc đánh giá tính khả thi của một kiến trúc vi dịch vụ (Microservices) cực kỳ rủi ro, áp dụng Delphi giúp tránh tình trạng "tư duy bầy đàn" (Groupthink) hay nhân viên cấp dưới phải đồng ý theo ý kiến của giám đốc công nghệ (CTO). Các chuyên gia đưa ra đánh giá độc lập, trung thực qua các phiếu điều tra ẩn danh.
- **Quy trình kết hợp các kỹ thuật trong dự án thực tế:**
  - Thông thường, các kỹ sư phần mềm bắt đầu bằng **Khảo sát (Survey)** để nắm bức tranh tổng thể, sau đó chọn lọc các nhân sự chủ chốt để **Phỏng vấn sâu (Interview)**, tổ chức **Brainstorming** để giải quyết các nút thắt kỹ thuật, và dựng **Prototype** để khách hàng ký duyệt yêu cầu.

### 복습 체크리스트
- [ ] Phân biệt được mục đích sử dụng của Phỏng vấn (đào sâu) và Khảo sát (diện rộng).
- [ ] Nhớ nguyên tắc cốt lõi của Brainstorming là 비판 금지 (Cấm phê bình).
- [ ] Nhớ đặc trưng cốt lõi của kỹ thuật Delphi: 전문가 익명성 (Chuyên gia ẩn danh) và lặp lại nhiều vòng.
- [ ] Định nghĩa được Use Case là tương tác giữa 액터 (Actor) và hệ thống để đạt mục tiêu người dùng.
