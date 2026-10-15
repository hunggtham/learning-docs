# 104-1 ~ 108: 소프트웨어 매뉴얼 (Software Manuals)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, mục đích và cấu trúc của tài liệu hướng dẫn phần mềm (소프트웨어 매뉴얼 - Software Manuals).
- Phân biệt sâu sắc hai loại tài liệu người dùng cốt lõi: Tài liệu hướng dẫn cài đặt (설치 매뉴얼 - Installation Manual) và Tài liệu hướng dẫn sử dụng (사용자 매뉴얼 - User Manual).
- Ghi nhớ các nguyên tắc biên soạn bắt buộc: Viết từ góc nhìn của người dùng cuối (사용자 기준), tuần tự từng bước, bắt buộc có quy trình gỡ cài đặt (Uninstall), xử lý tình huống bất thường (예외 상황) và sử dụng ảnh chụp minh họa trực quan.

## 핵심 키워드 (Từ khóa)
- 소프트웨어 매뉴얼 (Software Manuals)
- 설치 매뉴얼 (Installation Manual / Hướng dẫn cài đặt)
- 사용자 매뉴얼 (User Manual / Hướng dẫn sử dụng)
- 사용자 중심 작성 (User-centric Writing)
- 삭제 / 언인스톨 (Uninstall / gỡ cài đặt sạch)
- 예외 상황 및 오류 메시지 (Exception Handling & Error Messages)
- 서문 (Preface / 문서 이력, 환경 체크)
- 컴포넌트 단위 구성 (Component-based Structure)

## 선행·연결 개념 (Kiến thức liên kết)
- [98-bai-hoc.md](98-bai-hoc.md): Công cụ xây dựng và công cụ hợp tác nhóm.
- [100-bai-hoc.md](100-bai-hoc.md): Các mô hình công cụ quản lý phiên bản (SCM).
- [41-bai-hoc.md](41-bai-hoc.md): Quy trình đóng gói và xuất bản phẩm phần mềm.

## 읽는 방법 (Cách đọc)
- Phân biệt hai loại tài liệu hướng dẫn chuẩn thi:
  - **설치 매뉴얼 (Hướng dẫn cài đặt):** Dành cho lúc bắt đầu đưa phần mềm vào máy tính. Phải hướng dẫn theo trình tự bấm nút từ đầu đến cuối; đặc biệt **bắt buộc phải có phần hướng dẫn gỡ cài đặt (삭제 / Uninstall)** và cách xử lý khi gặp lỗi cài đặt (thiếu RAM, sai OS).
  - **사용자 매뉴얼 (Hướng dẫn sử dụng):** Dành cho lúc vận hành nghiệp vụ hàng ngày. Được chia nhỏ theo từng chức năng/linh kiện (**컴포넌트 단위**), phải có nhiều hình ảnh chụp màn hình UI thực tế để người dùng dễ làm theo.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết: 설치 매뉴얼 vs 사용자 매뉴얼:**

| Tiêu chuẩn so sánh | 설치 매뉴얼 (Installation Manual) | 사용자 매뉴얼 (User Manual) |
| :--- | :--- | :--- |
| **Mục đích tài liệu** | Hướng dẫn người dùng đưa phần mềm vào môi trường máy tính hoạt động ổn định | Hướng dẫn cách thao tác, khai thác các chức năng nghiệp vụ của phần mềm |
| **Góc nhìn biên soạn** | **Góc nhìn của người dùng (사용자 기준)**; không dùng từ ngữ kỹ thuật hàn lâm | Hướng dẫn theo luồng công việc nghiệp vụ thực tế của người dùng |
| **Trình tự trình bày** | Trình bày **theo đúng thứ tự thời gian** các bước cài đặt từ chuẩn bị đến hoàn tất | Tổ chức theo **từng khối thành phần chức năng (컴포넌트 단위)** |
| **Nội dung bắt buộc** | Kiểm tra môi trường hệ thống (OS, CPU, RAM); Trình tự thao tác cài đặt từng bước; Xử lý ngoại lệ khi lỗi cài đặt; **Quy trình gỡ cài đặt (삭제 / Uninstall)** | Giới thiệu giao diện tổng quan; Các bước nhập liệu và bấm nút; Câu hỏi thường gặp (FAQ); Quản lý phiên bản khi phần mềm nâng cấp |
| **Yêu cầu trực quan** | Minh họa từng hộp thoại Next/Finish | **Bắt buộc có ảnh chụp màn hình (UI Screenshots)** kèm mũi tên hướng dẫn |

- **Các nội dung cấu thành phần Mở đầu (서문 - Preface):**
  - **문서 이력 (Lịch sử tài liệu):** Ghi rõ mã phiên bản (v1.0, v1.1), ngày ban hành và nội dung thay đổi.
  - **설치 환경 체크 (Kiểm tra môi trường):** Liệt kê cấu hình phần cứng tối thiểu, hệ điều hành được hỗ trợ, và yêu cầu tắt các phần mềm diệt virus hoặc ứng dụng xung đột trước khi cài.
  - **주석 및 주의사항 (Chú thích & Cảnh báo):** Lưu ý về quyền quản trị viên (Run as Administrator) và điều kiện mạng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình gỡ cài đặt sạch sẽ (Clean Uninstall):**
  - Đề thi thường nhấn mạnh tính năng Uninstall: Một tài liệu cài đặt đạt chuẩn không được phép chỉ hướng dẫn cài vào mà bắt buộc phải hướng dẫn chi tiết cách xóa phần mềm, làm sạch các khóa Registry, và xóa các thư mục tạm để trả lại không gian đĩa nguyên vẹn cho hệ điều hành.

### 복습 체크리스트
- [ ] Phân biệt được mục đích của 설치 매뉴얼 (cài đặt) và 사용자 매뉴얼 (sử dụng).
- [ ] Nhớ nguyên tắc: Phải viết theo góc nhìn người dùng (사용자 기준), không viết cho lập trình viên.
- [ ] Nhớ 설치 매뉴얼 BẮT BUỘC phải có hướng dẫn 삭제 (Uninstall) và xử lý ngoại lệ lỗi.
- [ ] Nhớ 사용자 매뉴얼 được tổ chức theo 컴포넌트 단위 (Component) và dùng ảnh chụp màn hình UI.
