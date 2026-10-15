# 25. 트립와이어 (tripwire)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và nguyên lý hoạt động của công cụ bảo mật Tripwire (트립와이어): công cụ kiểm tra tính toàn vẹn của tệp tin và dữ liệu hệ thống (무결성 검사 도구).
- Hiểu rõ cơ chế phát hiện sự xâm nhập của tin tặc (Cracker/Attacker), cài cắm cửa sau (Backdoor), hoặc thay đổi trái phép các tệp cấu hình quan trọng trong hệ điều hành.
- Phân biệt vai trò của Tripwire như một hệ thống phát hiện xâm nhập dựa trên máy chủ (HIDS - Host-based Intrusion Detection System) sử dụng mã băm (Hash/Checksum).

## 핵심 키워드 (Từ khóa)
- 트립와이어 (Tripwire / 무결성 검사 도구)
- 데이터 무결성 (Data Integrity / Tính toàn vẹn dữ liệu)
- 백도어 탐지 (Backdoor Detection / Phát hiện cửa sau)
- 시스템 설정 파일 변조 감지 (System Configuration Tampering Detection)
- 해시 값 비교 (Hash / Checksum Comparison: MD5, SHA)
- HIDS (Host-based Intrusion Detection System)

## 선행·연결 개념 (Kiến thức liên kết)
- [77-bai-hoc.md](77-bai-hoc.md): Các kiểu kiến trúc tích hợp ứng dụng doanh nghiệp (EAI).
- [79-bai-hoc.md](79-bai-hoc.md): Định dạng dữ liệu JSON và cơ chế truyền bất đồng bộ AJAX.
- [정보처리기사/output/05-information-system-management/lessons/02-bai-hoc.md](../../05-information-system-management/lessons/02-bai-hoc.md): Các mối đe dọa an toàn thông tin và hệ thống phát hiện xâm nhập (IDS).

## 읽는 방법 (Cách đọc)
- Ghi nhớ hình ảnh ẩn dụ "Tripwire" (Sợi dây bẫy):
  - Kẻ trộm đột nhập vào nhà dù có xóa sạch dấu chân nhưng nếu vướng chân vào "sợi dây bẫy" thì chuông báo động sẽ reo.
  - Trong máy tính, Tripwire tạo một bản chụp (Snapshot) lưu trữ mã băm (Hash/Checksum) của toàn bộ các file hệ thống quan trọng (như `/etc/passwd`, `/etc/shadow`, file thực thi nhị phân).
  - Định kỳ, Tripwire quét lại và so sánh mã băm hiện tại với bản chụp gốc. Nếu mã băm thay đổi dù chỉ 1 bit, Tripwire phát cảnh báo: File đã bị sửa đổi hoặc có cửa sau (Backdoor)!

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp đặc tính cốt lõi của Tripwire:**

| Tiêu chí | Nội dung chi tiết chuẩn thi |
| :--- | :--- |
| **Phân loại công cụ** | **도구 유형:** Công cụ kiểm tra tính toàn vẹn dữ liệu hệ thống (**무결성 검사 도구 - Integrity Checker**) kiêm HIDS |
| **Mục tiêu phát hiện** | Phát hiện kẻ tấn công (Cracker) xâm nhập tạo cửa sau (**백도어 - Backdoor**), sửa đổi tệp cấu hình, thay thế tệp nhị phân hệ thống |
| **Cơ chế kỹ thuật** | Tạo cơ sở dữ liệu đối chuẩn chứa các giá trị băm mật mã (**MD5, SHA**) và thông số inode, quyền hạn (permission), kích thước tệp ban đầu; định kỳ so sánh đối chiếu |
| **Phạm vi bảo vệ** | Tệp nhị phân hệ thống (`/bin`, `/sbin`), tệp cấu hình dịch vụ (`/etc`), tệp nhật ký kiểm toán hệ thống |

- **Quy trình vận hành 3 pha của Tripwire:**
  1. **Tạo lập cơ sở dữ liệu mẫu (Baseline DB Creation):** Khi hệ thống vừa được cài đặt sạch, Tripwire quét toàn bộ thư mục chỉ định và lưu mã băm an toàn vào cơ sở dữ liệu mã hóa.
  2. **Quét định kỳ (Periodic Scanning):** Hệ thống định kỳ chạy tiến trình ngầm để tính toán lại giá trị băm của các tệp hiện thời.
  3. **Báo cáo sai lệch (Report Discrepancies):** Nếu phát hiện bất kỳ sự thay đổi kích thước, ngày sửa đổi, hoặc mã băm không khớp, gửi thông báo cảnh báo tức thì cho Quản trị viên hệ thống.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Giới hạn của công cụ kiểm tra toàn vẹn:**
  - Tripwire là công cụ phát hiện bị động (Detection) sau khi sự việc đã diễn ra, không có tính năng chủ động ngăn chặn xâm nhập (như IPS hay Firewall).
  - Bản thân cơ sở dữ liệu đối chuẩn của Tripwire và các khóa ký điện tử phải được bảo vệ nghiêm ngặt (lưu trên phương tiện chỉ đọc Read-Only) để tránh bị chính kẻ tấn công ghi đè.

### 복습 체크리스트
- [ ] Nhớ từ khóa định nghĩa của Tripwire: "무결성 검사 도구" (Công cụ kiểm tra tính toàn vẹn).
- [ ] Nhớ mục đích nhận diện: Phát hiện 백도어 (Backdoor) và sửa đổi file cấu hình hệ thống.
- [ ] Hiểu cơ chế so sánh giá trị băm (Hash/Checksum) giữa trạng thái sạch ban đầu và trạng thái hiện tại.
