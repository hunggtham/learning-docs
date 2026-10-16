# 연계 통합 기술과 데이터 교환 (Tích hợp hệ thống EAI/ESB và giao thức truyền thông)

## 학습 목표
- Nắm vững định nghĩa và so sánh 4 mô hình kiến trúc EAI: Point-to-Point, Hub & Spoke, Message Bus (ESB), và Hybrid; tính đúng số đường kết nối của Point-to-Point: $\frac{N(N-1)}{2}$.
- Phân tích điểm lỗi đơn (`단일 장애점 / SPOF`) của mô hình Hub & Spoke và so sánh sự chuyển dịch từ EAI sang Trục dịch vụ doanh nghiệp ESB theo kiến trúc hướng dịch vụ (SOA).
- So sánh đối đầu giữa hai định dạng trao đổi dữ liệu: JSON (gọn nhẹ, cặp Key-Value, parse nhanh) vs XML (thẻ lồng nhau, kiểm tra tính hợp lệ qua DTD/XSD).
- Nắm vững cơ chế truyền thông bất đồng bộ của AJAX: sử dụng đối tượng `XMLHttpRequest` để trao đổi dữ liệu ngầm và cập nhật giao diện cục bộ (`부분 화면 갱신`) mà không tải lại toàn trang.
- Định nghĩa kiến trúc RESTful API, 4 phương thức HTTP tiêu chuẩn (GET, POST, PUT, DELETE) và đặc tính phi trạng thái (`Stateless`).

## 핵심 키워드
- EAI (Enterprise Application Integration / 기업 애플리케이션 통합)
- EAI 구축 유형 (Point-to-Point N(N-1)/2, Hub & Spoke 단일 장애점 SPOF, Message Bus, Hybrid)
- ESB (Enterprise Service Bus / SOA 서비스 지향 아키텍처 / 느슨한 결합 Loose Coupling)
- 데이터 교환 포맷 (JSON 경량 Key-Value vs XML DTD/XSD 태그 기반)
- AJAX (Asynchronous JavaScript and XML / 비동기 통신 / 부분 화면 갱신 / XMLHttpRequest)
- RESTful API (자원 중심 Resource-oriented / URI / GET, POST, PUT, DELETE / Stateless)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [08-hien-thuc-module-va-ipc.md](08-hien-thuc-module-va-ipc.md), chúng ta đã khảo sát các cơ chế giao tiếp liên tiến trình IPC (Shared Memory, Socket, Pipe) trong phạm vi một máy chủ độc lập.
- **Đang giải quyết gì (Current Problem):** Bài học này nâng tầm bài toán tích hợp lên quy mô mạng doanh nghiệp kết nối các hệ thống phần mềm dị thể (ERP, CRM, Ngân hàng), giải quyết bài toán chống nghẽn đường truyền và chuẩn hóa định dạng dữ liệu web mở qua EAI/ESB, JSON và AJAX.
- **Dùng đi đâu (Forward Handoff):** Khi các hệ thống liên kết qua mạng, vấn đề an ninh thông tin và xác minh giao diện trở thành yếu tố sống còn, bàn giao trực tiếp sang [10-bao-mat-giao-dien-va-kiem-chung.md](10-bao-mat-giao-dien-va-kiem-chung.md).

## 읽는 방법
- Đọc TẦNG A để nắm chắc công thức tính số kết nối Point-to-Point $\frac{N(N-1)}{2}$, bẫy SPOF của Hub & Spoke, và từ khóa nhận diện AJAX (비동기 통신, 부분 갱신).
- Đọc TẦNG B để hiểu sâu sự khác nhau giữa adapter độc quyền của EAI với chuẩn mở Web Services của ESB.

---

## 연계 통합 기술과 데이터 교환

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 4 mô hình kiến trúc EAI kinh điển
| Mô hình EAI | Cơ chế kết nối | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi cốt lõi) |
| :--- | :--- | :--- | :--- |
| **Point-to-Point** | Kết nối trực tiếp 1:1 giữa từng cặp ứng dụng | Đơn giản khi chỉ có 2-3 hệ thống | Số kết nối bùng nổ theo công thức $\mathbf{\frac{N(N-1)}{2}}$; cực khó bảo trì khi $N$ lớn |
| **Hub & Spoke** | Nối tập trung về một máy chủ **Hub trung tâm (중앙 집중형)** | Dễ quản lý dữ liệu, kiểm soát bảo mật | **Điểm lỗi đơn (SPOF - Single Point of Failure)**; Hub sập thì tê liệt toàn bộ |
| **Message Bus (ESB)**| Kết nối qua **đường trục thông điệp chung (미들웨어 버스)** | Khả năng mở rộng cao, truyền thông bất đồng bộ | Thiết kế ban đầu phức tạp, chi phí middleware |
| **Hybrid** | Nội bộ dùng **Hub & Spoke**, giữa các cụm dùng **Message Bus** | Kết hợp ưu điểm kiểm soát nội bộ và mở rộng liên vùng | Quản trị song song hai mô hình phức tạp |

#### 2. Đối chiếu EAI vs ESB
| Tiêu chí | EAI (Enterprise Application Integration) | ESB (Enterprise Service Bus) |
| :--- | :--- | :--- |
| **Triết lý kiến trúc** | Tập trung (Hub & Spoke) hoặc adapter độc quyền | **Phân tán, hướng dịch vụ (SOA - Service-Oriented Architecture)** |
| **Mức độ liên kết** | Ghép nối tương đối chặt (Tight Coupling) | **Ghép nối lỏng lẻo (Loose Coupling)** |
| **Giao thức chuẩn** | Thường dùng Adapter riêng của nhà sản xuất | Sử dụng **chuẩn mở Web Services (SOAP, RESTful)** |
| **Định dạng dữ liệu** | Phụ thuộc vào công cụ chuyển đổi nội bộ | Chuẩn hóa thông qua **XML và JSON** |

#### 3. Bảng so sánh JSON vs XML
| Tiêu chuẩn so sánh | JSON (JavaScript Object Notation) | XML (eXtensible Markup Language) |
| :--- | :--- | :--- |
| **Cấu trúc dữ liệu** | Cặp **속성-값 (Key-Value)** `{}` và Mảng `[]` | Cấu trúc cây thẻ lồng nhau mở-đóng (`<tag>...</tag>`) |
| **Dung lượng tệp** | **Rất nhẹ**, ít ký tự thừa, tiết kiệm băng thông | Cồng kềnh, nặng hơn do lặp lại các thẻ đóng mở |
| **Tốc độ xử lý** | **Cực nhanh**; hỗ trợ tự nhiên trong JavaScript | Chậm hơn; cần bộ phân tích DOM/SAX Parser phức tạp |
| **Kiểm tra cấu trúc**| Hỗ trợ JSON Schema | Hỗ trợ kiểm tra ràng buộc chặt chẽ qua **DTD** và **XSD** |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Số kết nối Point-to-Point:** Doanh nghiệp có $N = 10$ hệ thống độc lập thì cần $\frac{10 \times 9}{2} = \mathbf{45}$ đường kết nối.
- **Bẫy 2: Nhược điểm của Hub & Spoke:** Luôn luôn gắn liền với khái niệm **단일 장애점 (Single Point of Failure / SPOF)**.
- **Bẫy 3: Đặc trưng nhận diện AJAX:** Cứ thấy câu hỏi *"công nghệ web trao đổi dữ liệu bất đồng bộ (`비동기`) và cập nhật cục bộ (`부분 화면 갱신`) mà không cần tải lại toàn trang"* $\rightarrow$ Chọn ngay **AJAX**.
- **Bẫy 4: 4 phương thức HTTP trong RESTful API:**
  - `GET`: Đọc / Truy vấn.
  - `POST`: Tạo mới tài nguyên.
  - `PUT`: Sửa / Cập nhật tài nguyên.
  - `DELETE`: Xóa tài nguyên.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế vận hành của AJAX
- Trình duyệt khởi tạo đối tượng `XMLHttpRequest` hoặc hàm `fetch()` trong JavaScript để gửi yêu cầu HTTP ngầm đến máy chủ.
- **Giao tiếp bất đồng bộ (비동기 통신):** Người dùng vẫn có thể thao tác cuộn trang hoặc bấm chuột bình thường mà không bị treo màn hình trong khi máy chủ đang xử lý.
- Khi máy chủ trả về kết quả (thường là dữ liệu JSON), JavaScript chỉ vẽ lại đúng phần tử HTML tương ứng trên cây DOM (ví dụ: cập nhật số lượt Like, hiển thị gợi ý tìm kiếm tức thời) mà **không làm tải lại toàn bộ trang**.

#### 2. Tính chất phi trạng thái (Stateless) của RESTful API
- Mỗi yêu cầu gửi từ Client lên Server phải chứa đầy đủ mọi thông tin cần thiết (Authentication Token, Headers, Payload) để Server xử lý.
- Server không lưu trữ bất kỳ trạng thái phiên làm việc nào của Client giữa các lần gọi; điều này giúp hệ thống máy chủ dễ dàng mở rộng theo chiều ngang (Scale-out) phía sau bộ cân bằng tải Load Balancer.

---

### 복습 체크리스트
- [ ] Kể tên đầy đủ 4 mô hình EAI: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- [ ] Tính đúng số kết nối của Point-to-Point theo công thức $\frac{N(N-1)}{2}$.
- [ ] Nhớ nhược điểm Single Point of Failure (SPOF) của mô hình Hub & Spoke.
- [ ] Phân biệt được sự chuyển dịch từ EAI (tập trung) sang ESB (phân tán, hướng dịch vụ SOA).
- [ ] So sánh được ưu điểm của JSON so với XML (nhẹ hơn, ít ký tự thừa, parse nhanh hơn).
- [ ] Định nghĩa AJAX là công nghệ truyền thông bất đồng bộ cho phép cập nhật cục bộ không tải lại toàn trang.
- [ ] Kể tên đối tượng nền tảng của AJAX: `XMLHttpRequest` (hoặc `fetch`).
- [ ] Nắm vững 4 phương thức HTTP trong RESTful API: GET (đọc), POST (tạo), PUT (sửa), DELETE (xóa).
