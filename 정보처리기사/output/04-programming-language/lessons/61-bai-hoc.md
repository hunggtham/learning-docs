# 199. 검사 전략 (Testing Strategies / Chiến lược kiểm thử)

## 학습 목표 (Mục tiêu)
- Nắm vững các cấp độ trong chiến lược kiểm thử phần mềm (소프트웨어 검사 전략): Kiểm thử đơn vị (단위 검사), Kiểm thử tích hợp (통합 검사), Kiểm thử xác thực (검증/확인 검사), và Kiểm thử hệ thống (시스템 검사).
- Phân biệt chi tiết hai kỹ thuật kiểm thử tích hợp: **Tích hợp từ trên xuống (하향식 / Top-Down)** sử dụng **Stub (모듈 스터브)** và **Tích hợp từ dưới lên (상향식 / Bottom-Up)** sử dụng **Driver (테스트 드라이버)** và **Cluster**.
- Phân biệt rõ sự khác nhau giữa Kiểm thử Alpha (알파 검사) và Kiểm thử Beta (베타 검사) trong giai đoạn nghiệm thu xác thực.

## 핵심 키워드 (Từ khóa)
- 검사 전략 (Testing Strategies)
- 단위 검사 (Unit Testing - 모듈 중심)
- 하향식 통합 (Top-Down Integration - Stub 필요)
- 상향식 통합 (Bottom-Up Integration - Driver/Cluster 필요)
- 모듈 스터브 (Module Stub) vs 테스트 드라이버 (Test Driver)
- 알파 검사 (Alpha Test - 통제된 개발자 환경)
- 베타 검사 (Beta Test - 통제되지 않은 실제 환경)
- 시스템 검사 (System Testing - 회복, 안전, 강도, 성능)
- 암기 공식 (하스 상드)

## 선행·연결 개념 (Kiến thức liên kết)
- [60-bai-hoc.md](60-bai-hoc.md): Kiểm thử hộp đen (Black Box Test: Phân vùng tương đương, Giá trị biên).
- [59-bai-hoc.md](59-bai-hoc.md): Kiểm thử hộp trắng (White Box Test: Statement, Branch, Condition Coverage).
- [62-bai-hoc.md](62-bai-hoc.md): Các loại hình bảo trì phần mềm (수적완예).

## 읽는 방법 (Cách đọc)
- Khẩu quyết kiểm thử tích hợp bắt buộc phải thuộc:
  $$\mathbf{하스 \quad 상드}$$
  - **하**향식 (Top-Down) = **스**터브 (Stub - giả lập module con phía dưới).
  - **상**향식 (Bottom-Up) = **드**라이버 (Driver - giả lập module cha gọi từ trên xuống).
- Phân biệt Alpha Test vs Beta Test:
  - Alpha: Người dùng test tại **văn phòng / môi trường của lập trình viên** (có sự giám sát chặt chẽ).
  - Beta: Người dùng test tại **môi trường thực tế của chính họ** (không có mặt lập trình viên).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Các giai đoạn trong chiến lược kiểm thử theo mô hình chữ V:**

| Giai đoạn kiểm thử | Đối tượng & Phạm vi kiểm thử | Phương pháp kiểm thử chủ đạo |
| :--- | :--- | :--- |
| **단위 검사 (Unit Test)** | Từng module, hàm, phương thức độc lập | **화이트 박스 (White Box)** |
| **통합 검사 (Integration Test)** | Giao diện liên kết giữa các module sau khi ghép nối | Cả White Box và Black Box |
| **시스템 검사 (System Test)** | Toàn bộ hệ thống phần mềm chạy trên phần cứng thực | **블랙 박스 (Black Box)** |
| **인수/검증 검사 (Acceptance Test)** | Đối chiếu yêu cầu người dùng (Alpha / Beta) | **블랙 박스 (Black Box)** |

- **2. So sánh Kiểm thử tích hợp: Top-Down vs Bottom-Up:**

| Tiêu chí | 하향식 통합 (Top-Down) | 상향식 통합 (Bottom-Up) |
| :--- | :--- | :--- |
| **Hướng tích hợp** | Từ module cấp cao (gốc) xuống module con cấp dưới | Từ module con ở đáy lên dần module cấp cao |
| **Thành phần giả lập** | **Stub (모듈 스터브):** Đóng vai trò module con chưa phát triển xong | **Driver (테스트 드라이버):** Đóng vai trò module cha điều khiển để truyền tham số |
| **Gom nhóm module** | Tích hợp theo chiều sâu (Depth-First) hoặc chiều rộng (Breadth-First) | Gom các module cấp dưới thành **Cluster (클러스터)** |
| **Ưu điểm** | Sớm thấy được cấu trúc toàn cảnh của hệ thống | Thuận tiện kiểm tra chi tiết các thuật toán xử lý dữ liệu ở tầng thấp |

- **3. Phân biệt Alpha Test vs Beta Test:**
  - **Alpha Test (알파 검사):** Khách hàng/người dùng được mời đến **môi trường của nhà phát triển (개발자 환경)** để chạy thử nghiệm dưới sự theo dõi và ghi nhận lỗi trực tiếp của kỹ sư phần mềm.
  - **Beta Test (베타 검사):** Bản thử nghiệm được phát hành trực tiếp ra **môi trường vận hành thực tế của người dùng (실제 환경)**. Người dùng tự do trải nghiệm và gửi phản hồi lỗi mà không có sự giám sát của lập trình viên.

- **4. 4 phép kiểm tra cốt lõi trong Hệ thống (System Testing):**
  1. **회복 검사 (Recovery Testing):** Đánh giá khả năng tự phục hồi khi hệ thống gặp sự cố phần cứng hoặc sập nguồn.
  2. **안전 검사 (Security Testing):** Thẩm định cơ chế phòng thủ trước các hành vi tấn công, thâm nhập trái phép.
  3. **강도 검사 (Stress Testing):** Đưa tải hệ thống lên mức quá tải cực đoan vượt quá hạn mức thiết kế để tìm điểm gãy.
  4. **성능 검사 (Performance Testing):** Đo lường thời gian phản hồi (Response Time) và thông lượng xử lý (Throughput).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kiểm thử hồi quy (Regression Testing - 회귀 검사):**
  - Khi một module được sửa lỗi hoặc thêm tính năng mới, bắt buộc phải chạy lại tập hợp các test case đã từng pass trước đó để bảo đảm việc sửa đổi mã nguồn mới không làm hỏng các tính năng cũ đang chạy ổn định.

### 복습 체크리스트
- [ ] Thuộc làu khẩu quyết: **하스 상드** (Top-Down dùng Stub, Bottom-Up dùng Driver).
- [ ] Phân biệt được Stub (thay thế module con chưa code) và Driver (thay thế module cha gọi hàm).
- [ ] Nhớ Alpha Test diễn ra ở văn phòng developer, Beta Test diễn ra ở môi trường người dùng cuối.
- [ ] Nắm được 4 loại System Test: Recovery (hồi phục), Security (an toàn), Stress (chịu tải quá mức), Performance (hiệu năng).
