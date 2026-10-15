# 21. 외계인 코드 (Alien Code)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và đặc điểm nhận diện của mã nguồn người ngoài hành tinh (외계인 코드 - Alien Code) trong kỹ nghệ phần mềm.
- Phân biệt rõ sự khác nhau giữa các thuật ngữ mã nguồn có vấn đề: Alien Code (외계인 코드), Spaghetti Code (스파게티 코드), và Legacy Code (레거시 코드).
- Hiểu được nguyên nhân hình thành và giải pháp quản lý rủi ro khi hệ thống phần mềm đối mặt với Alien Code trong giai đoạn bảo trì.

## 핵심 키워드 (Từ khóa)
- 외계인 코드 (Alien Code / Tác giả biến mất, không có tài liệu)
- 스파게티 코드 (Spaghetti Code / Cấu trúc rối như mì, lạm dụng goto)
- 레거시 코드 (Legacy Code / Mã cũ vẫn chạy tạo ra giá trị)
- 유지보수성 (Maintainability / Khả năng bảo trì)
- 기술 부채 (Technical Debt / Nợ kỹ thuật)
- 리버스 엔지니어링 (Reverse Engineering / Kỹ nghệ đảo ngược)

## 선행·연결 개념 (Kiến thức liên kết)
- [74-bai-hoc.md](74-bai-hoc.md): Các nguyên tắc viết mã nguồn sạch (Clean Code).
- [76-bai-hoc.md](76-bai-hoc.md): Các công cụ phân tích tĩnh kiểm tra chất lượng mã nguồn.
- [정보처리기사/output/01-software-design/lessons/02-bai-hoc.md](../../01-software-design/lessons/02-bai-hoc.md): Vòng đời phát triển phần mềm và giai đoạn bảo trì.

## 읽는 방법 (Cách đọc)
- Phân biệt rành mạch 3 loại mã nguồn "đau đầu" trong đề thi:
  - **외계인 코드 (Alien Code):** Mã nguồn được viết từ rất lâu, **tác giả gốc đã nghỉ việc hoặc không thể liên lạc, tài liệu thiết kế hoàn toàn không tồn tại**, khiến người tiếp quản đọc vào như "tiếng người ngoài hành tinh".
  - **스파게티 코드 (Spaghetti Code):** Mã nguồn có cấu trúc luồng điều khiển cực kỳ rối rắm, lạm dụng lệnh nhảy tùy tiện (`goto`) hoặc phụ thuộc chéo vòng vèo như sợi mì spaghetti.
  - **레거시 코드 (Legacy Code):** Hệ thống mã cũ đang vận hành thực tế nhưng thường thiếu kiểm thử tự động, khó nâng cấp công nghệ mới.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh các khái niệm mã nguồn đặc thù:**

| Thuật ngữ | Tên tiếng Hàn & Anh | Bản chất vấn đề | Hệ quả trong bảo trì |
| :--- | :--- | :--- | :--- |
| **외계인 코드** | **Alien Code** | Mã nguồn quá cũ kỹ, **không có tài liệu tham khảo (참고 문서 없음)** và **không còn người phát triển gốc (개발자 부재)** | Rất khó khăn và nguy hiểm khi bảo trì; sửa một dòng có thể làm sập toàn bộ hệ thống mà không rõ nguyên nhân |
| **스파게티 코드** | **Spaghetti Code** | Cấu trúc luồng thực thi phức tạp, nhảy loạn xạ, không tuân thủ lập trình có cấu trúc (Structured Programming) | Cực kỳ khó gỡ lỗi (Debug), khó lần theo luồng dữ liệu |
| **레거시 코드** | **Legacy Code** | Hệ thống phần mềm kế thừa từ công nghệ cũ nhưng vẫn đang tạo ra doanh thu cho doanh nghiệp | Chi phí bảo trì ngày càng tăng vọt, khó tích hợp với công nghệ hiện đại |

- **Giải pháp xử lý đối với Alien Code:**
  - **기록화 (Tài liệu hóa):** Thực hiện kỹ nghệ đảo ngược (Reverse Engineering) từ mã nguồn và cơ sở dữ liệu để vẽ lại tài liệu đặc tả thiết kế.
  - **테스트 케이스 확보 (Viết test case bao bọc):** Viết kiểm thử hồi quy (Regression Test / Characterization Test) trước khi can thiệp vào mã.
  - **점진적 리팩토링 (Refactoring từng bước):** Áp dụng mô hình Strangler Fig để thay thế từng module nhỏ thay vì viết lại từ đầu toàn bộ hệ thống cùng lúc.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Nguồn gốc nợ kỹ thuật (Technical Debt) dẫn đến Alien Code:**
  - Khi đội ngũ phát triển chịu áp lực bàn giao gấp (Deadline), bỏ qua việc viết tài liệu và chú thích (Comments), đồng thời lập trình viên rời bỏ dự án mà không bàn giao (Handover), mã nguồn bình thường sẽ dần thoái hóa thành Alien Code theo thời gian.

### 복습 체크리스트
- [ ] Nhớ 2 đặc trưng quan trọng nhất của Alien Code: Không có tài liệu (문서 없음) và không có nhà phát triển ban đầu (개발자 없음).
- [ ] Phân biệt được Alien Code (mất dấu vết tác giả/tài liệu) với Spaghetti Code (luồng code rối rắm).
- [ ] Hiểu vai trò của kiểm thử hồi quy trước khi can thiệp vào hệ thống mã cũ.
