# 38. 릴리즈 노트 (Release Note)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục đích của ghi chú phát hành phần mềm (릴리즈 노트 - Release Note): tài liệu chính thức chia sẻ thông tin cập nhật, cải tiến và sửa lỗi giữa nhóm phát triển và người dùng cuối.
- Ghi nhớ các nguyên tắc soạn thảo văn bản kỹ thuật chuẩn: do chính đội ngũ phát triển lập trình biên soạn, sử dụng thì hiện tại (Present Tense), thông tin chính xác và hoàn chỉnh.
- Nắm rõ các hạng mục cấu thành bắt buộc trong một bản Release Note tiêu chuẩn: Tiêu đề đầu trang (Header), Tổng quan (Overview), Mục đích (Purpose), Tóm tắt sự cố (Issue Summary), Các bước tái hiện (Reproduction Steps), Nội dung cải tiến, Tác động người dùng và Điều khoản miễn trừ trách nhiệm (Disclaimer).

## 핵심 키워드 (Từ khóa)
- 릴리즈 노트 (Release Note / 배포 정보 공유 문서)
- 현재 시제 작성 (Written in Present Tense)
- 개발팀 직접 작성 (Authored Directly by Development Team)
- 머릿말 (Header)
- 개요 및 목적 (Overview & Purpose)
- 수정 및 개선 내용 (Bug Fixes & Improvements)
- 면책 조항 (Disclaimer)

## 선행·연결 개념 (Kiến thức liên kết)
- [81-bai-hoc.md](81-bai-hoc.md): Hệ thống quản lý cơ sở dữ liệu (DBMS).
- [83-bai-hoc.md](83-bai-hoc.md): Bộ nhớ RAM và kiến trúc máy tính.
- [41-bai-hoc.md](41-bai-hoc.md): Quy trình đóng gói phần mềm và tài liệu hướng dẫn sử dụng.

## 읽는 방법 (Cách đọc)
- Phân biệt đối tượng và phong cách viết của Release Note:
  - **Ai viết?** Do **개발팀 (Đội ngũ phát triển)** trực tiếp soạn thảo dựa trên các thay đổi mã thực tế trong kỳ phát hành.
  - **Viết thế nào?** Viết bằng **현재 시제 (Thì hiện tại)**, súc tích, mạch lạc, trung thực về các lỗi đã được sửa và các hạn chế còn tồn đọng.
  - **Gồm những gì?** Header (phiên bản, ngày tháng), Overview (tổng quan tính năng mới), Fixes (lỗi đã khắc phục), và Disclaimer (điều khoản miễn trừ trách nhiệm bảo vệ nhà cung cấp).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các hạng mục thành phần trong một bản Release Note tiêu chuẩn:**

| Hạng mục cấu thành | Tên tiếng Hàn & Anh | Nội dung mô tả chi tiết |
| :--- | :--- | :--- |
| **1. 머릿말** | **Header (Tiêu đề đầu trang)** | Tên phần mềm, mã phiên bản phát hành (Version/Release Number), ngày phát hành chính thức, tên công ty/tác giả |
| **2. 개요 및 목적** | **Overview & Purpose (Tổng quan & Mục đích)** | Tóm tắt bối cảnh bản phát hành (bản cập nhật định kỳ, vá lỗi khẩn cấp Hotfix, hoặc nâng cấp tính năng lớn) |
| **3. 문제 요약 및 재현** | **Issue Summary & Reproduction** | Mô tả ngắn gọn sự cố đã được báo cáo trong phiên bản trước và các bước tái hiện lỗi (Steps to reproduce) |
| **4. 수정 및 개선 내용** | **Fixes & Improvements (Nội dung sửa đổi)** | Danh sách chi tiết các tính năng mới được bổ sung, các lỗi logic đã khắc phục, tối ưu hóa giao diện hoặc hiệu năng |
| **5. 사용자 영향도** | **User Impact (Mức độ ảnh hưởng)** | Hướng dẫn người dùng các thay đổi về luồng thao tác hoặc cấu hình cần cập nhật sau khi nâng cấp phần bản mới |
| **6. SW 지원 영향도** | **Software Support Impact** | Khả năng tương thích ngược (Backward Compatibility), các thư viện bên thứ ba bị ngừng hỗ trợ hoặc yêu cầu nâng cấp |
| **7. 면책 조항** | **Disclaimer (Điều khoản miễn trừ)** | Tuyên bố pháp lý giới hạn trách nhiệm của nhà phát triển đối với các sự cố phát sinh ngoài phạm vi cam kết |

- **Các nguyên tắc biên soạn Release Note chuẩn:**
  - Viết hoàn toàn bằng thì hiện tại (Present Tense) để tạo cảm giác trực quan và xác thực.
  - Cung cấp đầy đủ thông tin kiểm thử liên quan nhằm giúp bộ phận vận hành (Ops) kiểm tra tính ổn định trước khi đưa lên môi trường Production.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chu trình phát hành từ Commit Log đến Release Note:**
  - Trong các dự án hiện đại, Release Note thường được tạo tự động một phần dựa trên các commit message tuân thủ quy chuẩn Conventional Commits (ví dụ: `fix:`, `feat:`, `perf:`) kết hợp với công cụ tự động hóa như Semantic Release.
  - Tuy nhiên, trước khi gửi cho khách hàng, nhóm phát triển phải biên tập lại bằng ngôn ngữ tự nhiên dễ hiểu với người dùng kinh doanh.

### 복습 체크리스트
- [ ] Nhớ người viết Release Note: Do 개발팀 (Đội ngũ phát triển) trực tiếp biên soạn.
- [ ] Nhớ phong cách viết: Dùng thì hiện tại (현재 시제).
- [ ] Kể tên các hạng mục chính: Header, 개요, 목적, 문제 요약, 재현 항목, 수정 내용, 사용자 영향도, 면책 조항.
