# 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, vai trò của `EAI` (Enterprise Application Integration) và `ESB` (Enterprise Service Bus) trong tích hợp hệ thống doanh nghiệp.
- Thuộc nằm lòng đặc trưng, ưu nhược điểm của 4 mô hình kiến trúc EAI kinh điển: `Point-to-Point`, `Hub & Spoke`, `Message Bus`, và `Hybrid`.
- Phân biệt sự khác nhau bản chất giữa EAI (kết nối chặt chẽ, tập trung) và ESB (kết nối lỏng lẻo, hướng dịch vụ SOA).

## 핵심 키워드 (Từ khóa)
- EAI (Enterprise Application Integration / 기업 응용 프로그램 통합)
- Point-to-Point (Điểm - Điểm / trực tiếp 1-1)
- Hub & Spoke (Trung tâm điều phối / 단일 장애점 SPOF)
- Message Bus (Trục truyền thông điệp / 미들웨어 버스)
- Hybrid (Mô hình lai / Hub-and-Spoke + Message Bus)
- ESB (Enterprise Service Bus / SOA / 느슨한 결합 / Loosely Coupled)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 인터페이스 검토 및 연계 기술](38-bai-hoc.md)):** Sau khi xem xét các kỹ thuật liên kết tổng quát (DB Link, API), bài này phân tích sâu vào 4 hình thái kiến trúc của EAI và sự tiến hóa sang ESB.
- **Tiếp nối sang bài sau ([14. 미들웨어](40-bai-hoc.md)):** Khảo sát chi tiết tầng phần mềm trung gian (Middleware: MOM, RPC, TP-Monitor, WAS) cung cấp hạ tầng chạy bên dưới của EAI/ESB.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ 4 mô hình EAI và bẫy nhược điểm kinh điển: Hub & Spoke dễ bị nghẽn cổ chai và điểm lỗi duy nhất (SPOF); Point-to-Point bùng nổ số đường kết nối $N(N-1)/2$.
- Đọc TẦNG B để phân biệt kiến trúc kết nối chặt chẽ của EAI với kiến trúc kết nối lỏng lẻo theo chuẩn Web Service của ESB.

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. EAI (Enterprise Application Integration - Tích hợp ứng dụng doanh nghiệp):**
  - **Khái niệm:** Là giải pháp kiến trúc phần mềm trung gian giúp kết nối, tích hợp và đồng bộ hóa dữ liệu giữa các ứng dụng nghiệp vụ không đồng nhất (Heterogeneous Applications: ERP, CRM, SCM, Legacy Systems) trong một doanh nghiệp mà không cần sửa đổi mã nguồn gốc của từng ứng dụng.
- **4 mô hình kiến trúc EAI kinh điển (EAI 4대 구축 유형):**
  1. **Point-to-Point (Mô hình Điểm - Điểm):**
     - Các ứng dụng kết nối trực tiếp 1-1 với nhau bằng các kết nối tùy biến.
     - *Ưu điểm:* Dễ cài đặt khi số lượng ứng dụng ít (2-3 hệ thống).
     - *Nhược điểm:* Khi số ứng dụng $N$ tăng lên, số đường kết nối tăng theo công thức $\frac{N(N-1)}{2}$, tạo ra mạng lưới chằng chịt rất khó bảo trì và sửa đổi.
  2. **Hub & Spoke (Mô hình Trục bánh xe và Nan hoa / Trung tâm):**
     - Sử dụng một máy chủ trung tâm (`Hub`) làm đầu mối chuyển tiếp; tất cả các hệ thống con (`Spoke`) chỉ kết nối duy nhất vào Hub.
     - *Ưu điểm:* Giảm số đường kết nối từ $\frac{N(N-1)}{2}$ xuống còn $N$ đường, dễ mở rộng và quản trị tập trung.
     - *Nhược điểm:* **Gặp nguy cơ điểm nghẽn cổ chai (Bottleneck) và Điểm lỗi duy nhất (SPOF - Single Point of Failure)**; nếu máy chủ Hub bị sập, toàn bộ việc liên lạc giữa các hệ thống bị tê liệt.
  3. **Message Bus (Mô hình Trục thông điệp):**
     - Tất cả các ứng dụng trao đổi dữ liệu với nhau thông qua một trục đường truyền thông điệp chung (`Bus`) sử dụng phần mềm trung gian hướng thông điệp (MOM).
     - *Ưu điểm:* Khả năng mở rộng rất cao, xử lý phân tán tốt, không bị điểm lỗi tập trung tại một máy chủ duy nhất.
  4. **Hybrid (Mô hình Lai ghép):**
     - **Kết hợp linh hoạt giữa Hub & Spoke và Message Bus**.
     - Áp dụng Hub & Spoke cho các phân hệ nội bộ từng chi nhánh/phòng ban để dễ quản lý cục bộ; sau đó dùng Message Bus để liên kết các Hub đó lại với nhau.
- **2. So sánh đối chiếu EAI vs ESB:**
  - **EAI:**
    - Mục tiêu: Tích hợp ứng dụng trong nội bộ một doanh nghiệp (`기업 내부 통합`).
    - Tính kết nối: **Kết nối chặt chẽ (Tightly coupled)**, phụ thuộc vào công nghệ và giải pháp độc quyền của một nhà cung cấp (Vendor).
    - Kiến trúc: Thường tập trung hóa (Centralized) theo mô hình Hub-and-Spoke.
  - **ESB (Enterprise Service Bus):**
    - Mục tiêu: Tích hợp các dịch vụ phân tán xuyên suốt doanh nghiệp và các đối tác bên ngoài theo Kiến trúc hướng dịch vụ (**SOA - Service-Oriented Architecture**).
    - Tính kết nối: **Kết nối lỏng lẻo (Loosely coupled)**.
    - Chuẩn công nghệ: Sử dụng các tiêu chuẩn mở quốc tế (Web Services, XML, JSON, WSDL, SOAP, REST).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Mô hình EAI nào có nguy cơ gặp sự cố Single Point of Failure (SPOF) tại máy chủ trung tâm?"* -> **Hub & Spoke**.
  - **Bẫy 2:** *"Mô hình Hybrid kết hợp những loại nào?"* -> **Hub & Spoke và Message Bus**, KHÔNG PHẢI Point-to-Point.
  - **Bẫy 3:** *"ESB có tính chất kết nối chặt chẽ (Tightly coupled) hay lỏng lẻo (Loosely coupled)?"* -> **Kết nối lỏng lẻo (느슨한 결합 / Loosely coupled)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "EAI có 4 mô hình: Point-to-Point chằng chịt, Hub-Spoke chết trung tâm, Message Bus trục thông điệp, Hybrid kết hợp cả hai; ESB liên kết lỏng lẻo theo chuẩn SOA".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính toán số đường kết nối trong mô hình Point-to-Point:**
  - Nếu một doanh nghiệp có $N = 10$ hệ thống ứng dụng riêng lẻ:
    - Nếu dùng Point-to-Point: Cần $\frac{10 \times 9}{2} = 45$ đường cáp và giao diện kết nối riêng biệt. Khi có thêm hệ thống thứ 11, phải viết thêm 10 interface mới.
    - Nếu dùng Hub & Spoke: Chỉ cần 10 đường kết nối vào Hub. Thêm hệ thống thứ 11 chỉ cần đấu đúng 1 đường vào Hub.

### 복습 체크리스트
- [ ] Phân biệt được đặc trưng của 4 mô hình kiến trúc EAI: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- [ ] Giải thích được tại sao Hub & Spoke có nguy cơ bị điểm lỗi duy nhất (SPOF).
- [ ] Nhớ Hybrid là sự kết hợp giữa Hub & Spoke và Message Bus.
- [ ] So sánh được EAI (chặt chẽ, tập trung) và ESB (lỏng lẻo, chuẩn mở SOA).
