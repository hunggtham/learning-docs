# 6. 애자일 방법론 (Agile Methodology)

## 학습 목표 (Mục tiêu)
- Nắm vững triết lý, bối cảnh ra đời và bản chất linh hoạt thích ứng của Phương pháp luận Agile (`애자일 방법론`).
- Phân tích sâu sắc sự đối lập toàn diện giữa mô hình Thác nước truyền thống (`폭포수 모형` - Kế hoạch, Tài liệu) và mô hình Agile (`애자일` - Thích ứng, Khách hàng, Phần mềm chạy được).
- Thuộc nằm lòng 4 giá trị cốt lõi của Tuyên ngôn Agile và các phương pháp luận tiêu biểu thuộc họ Agile (Scrum, XP, Kanban, Lean).

## 핵심 키워드 (Từ khóa)
- 애자일 방법론 (Phương pháp luận Agile / Agile Methodology)
- 폭포수 vs 애자일 (Waterfall vs Agile / Kế hoạch vs Thích ứng)
- 애자일 선언 4대 가치 (4 giá trị cốt lõi tuyên ngôn Agile)
- 소통·협업·피드백 (Giao tiếp, Hợp tác, Phản hồi)
- 반복 및 점증 (Vòng lặp và Tăng trưởng / Iterative & Incremental)
- 스크럼 / XP / 칸반 (Scrum / XP / Kanban)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([14. 파일 편성 방식 (File Organization)](57-bai-hoc.md)):** Sau khi hoàn tất các bài học về cấu trúc dữ liệu và tập tin, bài này quay trở lại làm chủ các quy trình phát triển phần mềm hiện đại.
- **Tiếp nối sang bài sau ([7. 스크럼(Scrum) 및 XP(eXtreme Programming)](59-bai-hoc.md)):** Khảo sát chi tiết hai phương pháp luận Agile phổ biến nhất trong thực tế: Scrum và XP.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững 4 mệnh đề so sánh cốt lõi của Tuyên ngôn Agile và bảng đối chiếu Waterfall vs Agile.
- Đọc TẦNG B để hiểu tại sao Agile phù hợp với các dự án có yêu cầu biến động liên tục trong kỷ nguyên số.

---

## 6. 애자일 방법론 (Agile Methodology)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Agile):**
  - Là triết lý và phương pháp luận phát triển phần mềm mang tính **Linh hoạt (`민첩함`), Lặp đi lặp lại (`반복적 - Iterative`) và Tăng trưởng dần (`점증적 - Incremental`)**, tập trung vào việc chuyển giao sớm phần mềm có thể chạy được để liên tục tiếp nhận phản hồi từ khách hàng.
- **So sánh đối chiếu Waterfall (Thác nước) vs Agile:**
  - **폭포수 모형 (Waterfall):**
    - Trọng tâm: Kế hoạch và quy trình tài liệu (`계획 및 문서 중심`).
    - Cách triển khai: Đi theo đường thẳng tuần tự, chia giai đoạn dứt điểm.
    - Quản lý thay đổi: Hạn chế thay đổi, việc sửa đổi yêu cầu ở giai đoạn muộn rất tốn kém.
    - Phù hợp: Dự án có yêu cầu rõ ràng, cố định ngay từ đầu (quân sự, lõi ngân hàng).
  - **애자일 모형 (Agile):**
    - Trọng tâm: Con người, sự tương tác và sản phẩm chạy được (`사람과 상호작용, 작동하는 소프트웨어 중심`).
    - Cách triển khai: Chia nhỏ thành các chu kỳ ngắn (1-4 tuần), liên tục nhận phản hồi và cải tiến.
    - Quản lý thay đổi: Đón nhận và thích ứng nhanh với các thay đổi yêu cầu phát sinh.
    - Phù hợp: Dự án ứng dụng web, di động, khởi nghiệp sáng tạo có thị hiếu biến động nhanh.
- **애자일 선언 4대 핵심 가치 (4 giá trị cốt lõi của Tuyên ngôn Agile):**
  1. **개인과 상호작용** > 프로세스와 도구 (Cá nhân và sự tương tác quan trọng hơn quy trình và công cụ).
  2. **작동하는 소프트웨어** > 포괄적인 문서 (Phần mềm hoạt động tốt quan trọng hơn tài liệu đồ sộ).
  3. **고객과의 협력** > 계약 협상 (Hợp tác với khách hàng quan trọng hơn đàm phán hợp đồng).
  4. **변화에 대응하기** > 계획을 따르기 (Thích ứng linh hoạt với thay đổi quan trọng hơn bám sát kế hoạch).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Agile là một phương pháp luận cụ thể duy nhất?"* -> **Sai**. Agile là một **triết lý / chiếc ô bao trùm** gồm nhiều phương pháp luận cụ thể (Scrum, XP, FDD, Kanban, Lean).
  - **Bẫy 2:** *"Agile hoàn toàn không cần tài liệu?"* -> **Sai**. Agile vẫn có tài liệu nhưng ưu tiên phần mềm chạy được hơn.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Agile linh hoạt lấy phần mềm hoạt động và sự hài lòng của khách hàng làm thước đo tiến độ".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **12 nguyên tắc chỉ đạo của Tuyên ngôn Agile (Agile Principles):**
  - Chuyển giao phần mềm giá trị sớm và liên tục để làm thỏa mãn khách hàng.
  - Sẵn sàng đón nhận thay đổi yêu cầu kể cả ở giai đoạn muộn của quá trình phát triển.
  - Chuyển giao phần mềm hoạt động thường xuyên (từ vài tuần đến vài tháng, chu kỳ càng ngắn càng tốt).
  - Khách hàng và kỹ sư phát triển phải làm việc cùng nhau hàng ngày trong suốt dự án.
  - Xây dựng dự án xung quanh các cá nhân có động lực; tạo môi trường và sự hỗ trợ cần thiết, tin tưởng họ hoàn thành công việc.
  - Phương pháp truyền đạt thông tin hiệu quả nhất trong nhóm phát triển là **Trò chuyện trực tiếp mặt đối mặt (대면 대화)**.

### 복습 체크리스트
- [ ] Phân biệt được sự khác nhau giữa Waterfall (kế hoạch, tài liệu) và Agile (thích ứng, phần mềm).
- [ ] Thuộc lòng 4 giá trị cốt lõi của Tuyên ngôn Agile.
- [ ] Kể tên ít nhất 3 phương pháp luận thuộc dòng họ Agile.
- [ ] Nhớ phương thức truyền đạt thông tin hiệu quả nhất trong Agile là đối thoại trực tiếp (대면 대화).
