# 16. 소프트웨어 테스트 단계 (Software Testing Phases)

## 학습 목표 (Mục tiêu)
- Nắm vững 4 tầng cấp độ kiểm thử phần mềm theo mô hình chữ V: Kiểm thử đơn vị (단위 테스트) $\rightarrow$ Kiểm thử tích hợp (통합 테스트) $\rightarrow$ Kiểm thử hệ thống (시스템 테스트) $\rightarrow$ Kiểm thử chấp nhận (인수 테스트).
- Phân biệt hai phương pháp kiểm thử tích hợp kinh điển: Tích hợp từ trên xuống (하향식 - Top-down dùng Test Stub) và Tích hợp từ dưới lên (상향식 - Bottom-up dùng Test Driver).
- Phân biệt chính xác hai hình thức kiểm thử chấp nhận người dùng cuối: Kiểm thử Alpha (알파 테스트 - có lập trình viên giám sát) và Kiểm thử Beta (베타 테스트 - môi trường thực tế không có lập trình viên).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 테스트 4단계 (4 Testing Levels)
- 단위 테스트 (Unit Test) & 통합 테스트 (Integration Test)
- 시스템 테스트 (System Test) & 인수 테스트 (Acceptance Test)
- 하향식 (Top-down) & 테스트 스텁 (Test Stub)
- 상향식 (Bottom-up) & 테스트 드라이버 (Test Driver)
- 알파 테스트 (Alpha Test) & 베타 테스트 (Beta Test / 필드 테스트)

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): Kiểm thử hộp trắng vs Kiểm thử hộp đen.
- [54-bai-hoc.md](54-bai-hoc.md): Test Oracle và các công cụ bổ trợ kiểm thử.
- [55-bai-hoc.md](55-bai-hoc.md): Chi tiết kỹ thuật kiểm thử tích hợp Top-down và Test Stub.
- [60-bai-hoc.md](60-bai-hoc.md): Mô hình V-Model đối chiếu giữa các pha phát triển và các cấp độ kiểm thử.

## 읽는 방법 (Cách đọc)
- Phân biệt cặp công cụ giả lập kiểm thử tích hợp:
  - Top-down (Từ trên xuống) $\rightarrow$ Thiếu mô-đun cấp dưới $\rightarrow$ Dùng **스텁 (Stub - Giả lập mô-đun con bị gọi)**.
  - Bottom-up (Từ dưới lên) $\rightarrow$ Thiếu mô-đun cấp trên $\rightarrow$ Dùng **드라이버 (Driver - Giả lập chương trình chính gọi xuống)**.
- Phân biệt Alpha vs Beta:
  - **알파 (Alpha):** Người dùng test tại phòng thí nghiệm của công ty phát triển, **có mặt lập trình viên (개발자 앞에서)**.
  - **베타 (Beta / Field Test):** Thả tự do cho người dùng test ngoài môi trường thực tế, **không có lập trình viên giám sát**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 4 cấp độ kiểm thử phần mềm:**

| Cấp độ kiểm thử | Tên tiếng Hàn & Anh | Đối tượng và Mục tiêu kiểm tra | Kỹ thuật / Công cụ sử dụng |
| :--- | :--- | :--- | :--- |
| **1. Kiểm thử đơn vị** | **단위 테스트 (Unit Test)** | Từng mô-đun, lớp (Class) hoặc hàm riêng lẻ ngay sau khi viết mã; phát hiện lỗi thuật toán, vòng lặp vô hạn | Chủ yếu là **화이트박스 (White-box)**; dùng xUnit (JUnit) |
| **2. Kiểm thử tích hợp** | **통합 테스트 (Integration Test)** | Kiểm tra sự tương tác và giao diện liên kết (Interface) giữa các mô-đun khi ghép nối lại với nhau | **하향식 (Top-down)** dùng **Stub**; **상향식 (Bottom-up)** dùng **Driver**; hoặc Big Bang |
| **3. Kiểm thử hệ thống** | **시스템 테스트 (System Test)** | Toàn bộ hệ thống phần mềm hoàn chỉnh chạy trên môi trường thực; kiểm tra cả chức năng và phi chức năng | Kiểm thử hiệu năng, tải quá mức (Stress), bảo mật an toàn, phục hồi sự cố |
| **4. Kiểm thử chấp nhận** | **인수 테스트 (Acceptance Test)** | Khách hàng hoặc người dùng cuối trực tiếp nghiệm thu xem phần mềm có thỏa mãn đúng hợp đồng không | Chia thành **알파 테스트 (Alpha Test)** và **베타 테스트 (Beta Test)** |

- **Bảng so sánh chi tiết Alpha Test vs Beta Test:**

| Tiêu chí | 알파 테스트 (Alpha Test) | 베타 테스트 (Beta Test / Field Test) |
| :--- | :--- | :--- |
| **Địa điểm thực hiện** | Môi trường kiểm soát nội bộ (Phòng Lab của nhà phát triển) | Môi trường vận hành thực tế phân tán của người dùng (Real-world) |
| **Sự hiện diện của Dev** | **Có lập trình viên quan sát trực tiếp** để ghi nhận lỗi tức thời | **Không có lập trình viên**, người dùng tự trải nghiệm và gửi báo cáo lỗi |
| **Đối tượng tham gia** | Nhóm người dùng nội bộ hoặc khách hàng được mời đến công ty | Số lượng lớn người dùng đại chúng (Public / Closed Beta) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Các hình thức khác của Kiểm thử chấp nhận:**
  - **계약 인수 테스트 (Contract Acceptance Testing):** Nghiệm thu dựa trên các điều khoản cam kết trong hợp đồng kinh tế.
  - **규정 인수 테스트 (Regulation Acceptance Testing):** Kiểm tra sự tuân thủ các quy định pháp luật của chính phủ (an toàn thông tin, bảo vệ dữ liệu cá nhân GDPR).
  - **운영 인수 테스트 (Operational Acceptance Testing - OAT):** Bộ phận vận hành IT kiểm tra việc sao lưu dự phòng (Backup/Restore), khôi phục thảm họa (DR) và bảo trì hệ thống.

### 복습 체크리스트
- [ ] Kể đúng thứ tự 4 cấp độ kiểm thử: 단위 $\rightarrow$ 통합 $\rightarrow$ 시스템 $\rightarrow$ 인수.
- [ ] Phân biệt Top-down dùng Test Stub và Bottom-up dùng Test Driver.
- [ ] Nhớ Alpha Test diễn ra trước mặt lập trình viên tại phòng Lab.
- [ ] Nhớ Beta Test (Field Test) diễn ra ngoài môi trường thực tế không có lập trình viên.
