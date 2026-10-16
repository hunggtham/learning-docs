# 연계 통합 구현과 EAI/ESB (Tích hợp hệ thống EAI/ESB)

## 학습 목표
- Nắm vững định nghĩa và vai trò của Tích hợp ứng dụng doanh nghiệp (`EAI / Enterprise Application Integration`), phân tích chi tiết 4 mô hình kiến trúc EAI kinh điển: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- Áp dụng thành thạo công thức tính số lượng đường kết nối trong mô hình Point-to-Point: $\frac{N(N-1)}{2}$.
- So sánh đối đầu giữa kiến trúc EAI truyền thống và Trục dịch vụ doanh nghiệp (`ESB / Enterprise Service Bus`) theo định hướng kiến trúc hướng dịch vụ (SOA).
- Phân tích ưu nhược điểm của hai định dạng trao đổi dữ liệu tiêu chuẩn: `JSON` (nhẹ, nhanh, cặp key-value) và `XML` (cấu trúc cây thẻ, hỗ trợ DTD/XSD).
- Nắm vững công nghệ truyền thông Web Services (SOAP, WSDL, UDDI) và cơ chế truyền thông bất đồng bộ qua mạng `AJAX` và `REST`.

## 핵심 키워드
- EAI (Enterprise Application Integration / 기업 애플리케이션 통합)
- EAI 4대 구축 유형 (Point-to-Point, Hub & Spoke 중앙 집중, Message Bus, Hybrid)
- SPOF (Single Point of Failure / 단일 장애점 / Hub & Spoke 단점)
- ESB (Enterprise Service Bus / SOA 서비스 지향 아키텍처 / 느슨한 결합 Loose Coupling)
- 데이터 교환 포맷 (JSON vs XML / WSDL, SOAP, REST)
- AJAX (Asynchronous JavaScript and XML / 비동기 통신)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [08-hien-thuc-module-va-ipc.md](08-hien-thuc-module-va-ipc.md), chúng ta đã khảo sát các cơ chế giao tiếp liên tiến trình IPC trên một máy chủ đơn lẻ.
- **Đang giải quyết gì (Current Problem):** Bài học này nâng tầm bài toán tích hợp lên quy mô doanh nghiệp và hệ thống phân tán đa nền tảng, giải quyết việc kết nối các hệ thống phần mềm dị thể qua EAI/ESB và chuẩn hóa định dạng dữ liệu truyền thông bằng JSON/XML.
- **Dùng đi đâu (Forward Handoff):** Khi các giao diện hệ thống được mở ra để tích hợp liên thông, nguy cơ bảo mật xuất hiện. Bài học tiếp theo [10-bao-mat-giao-dien-va-kiem-chung.md](10-bao-mat-giao-dien-va-kiem-chung.md) sẽ khảo sát các giao thức bảo mật IPSec, SSL/TLS và công cụ kiểm chứng.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng 4 mô hình EAI, bảng đối đầu EAI vs ESB, bảng so sánh JSON vs XML và các bẫy trắc nghiệm.
- Đọc TẦNG B để hiểu sâu công thức tính số kết nối Point-to-Point, các thành phần của Web Services (SOAP, WSDL, UDDI) và công nghệ AJAX/REST.

---

## 연계 통합 구현과 EAI/ESB

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng 4 mô hình kiến trúc EAI kinh điển

| Mô hình EAI | Cơ chế kết nối | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi cốt lõi) |
|:---|:---|:---|:---|
| **Point-to-Point** | Kết nối trực tiếp 1:1 giữa từng cặp ứng dụng | Rất đơn giản khi hệ thống chỉ có 2-3 ứng dụng | Khi $N$ tăng, số kết nối bùng nổ: $\mathbf{\frac{N(N-1)}{2}}$; cực kỳ khó bảo trì, chi phí thay đổi rất cao |
| **Hub & Spoke** | Mọi hệ thống đều nối tập trung về một **Hub trung tâm (중앙 집중형)** | Dễ quản lý dữ liệu, kiểm soát bảo mật và đồng bộ tập trung | **Điểm lỗi đơn (SPOF — Single Point of Failure)**; máy chủ Hub sập là tê liệt toàn bộ doanh nghiệp |
| **Message Bus** | Các ứng dụng liên lạc qua một **trục bus phần mềm trung gian chung (미들웨어 버스)** | Khả năng mở rộng vượt trội, truyền thông bất đồng bộ tin cậy qua Adapter | Chi phí mua middleware bản quyền và cấu hình thiết kế ban đầu phức tạp |
| **Hybrid** | Nội bộ cụm dùng **Hub & Spoke**, giữa các cụm lớn liên kết qua **Message Bus** | Tận dụng sự linh hoạt của Hub và khả năng mở rộng của Bus, giảm tải cho Hub | Đòi hỏi trình độ quản trị hai kiến trúc song song phức tạp |

##### Sơ đồ ASCII 4 mô hình kiến trúc EAI kinh điển:

```text
  [1. POINT-TO-POINT (ĐIỂM - ĐIỂM)]            [2. HUB & SPOKE (TRỤC BÁNH XE - TẬP TRUNG)]
       ┌─────┐       ┌─────┐                               ┌─────┐
       │ App1├───────┤ App2│                               │ App1│
       └──┬──┘╲     ╱└──┬──┘                               └──┬──┘
          │    ╲   ╱    │                                     │
          │     ╲ ╱     │                               ┌─────┴─────┐
          │      ╳      │                        ┌──────┤    HUB    ├──────┐
          │     ╱ ╲     │                        │      │ TRUNG TÂM │      │
       ┌──┴──┐ ╱   ╲ ┌──┴──┐                     ▼      └─────┬─────┘      ▼
       │ App3├───────┤ App4│                  ┌─────┐         │         ┌─────┐
       └─────┘       └─────┘                  │ App2│         ▼         │ App3│
     (Số kết nối = N*(N-1)/2)                 └─────┘      ┌─────┐      └─────┘
                                                           │ App4│
                                                           └─────┘
                                                    (Nguy cơ SPOF tại Hub)

  [3. MESSAGE BUS (TRỤC THÔNG ĐIỆP)]           [4. HYBRID (MÔ HÌNH LAI PHÂN CẤP)]
       ┌─────┐  ┌─────┐  ┌─────┐                   [Hub Phòng A]       [Hub Phòng B]
       │ App1│  │ App2│  │ App3│                    ┌───┴───┐           ┌───┴───┐
       └──┬──┘  └──┬──┘  └──┬──┘                    App1   App2        App3   App4
       ═══╪════════╪════════╪════                   │     │             │     │
          [ TRỤC THÔNG ĐIỆP BUS ]                   └───┬─┘             └───┬─┘
       ═══╪════════╪════════╪════                       │                   │
       ┌──┴──┐  ┌──┴──┐  ┌──┴──┐                  ══════╪═══════════════════╪══════
       │ App4│  │ App5│  │ App6│                     [ TRỤC CHÍNH MESSAGE BUS ]
       └─────┘  └─────┘  └─────┘                  ═════════════════════════════════
    (Giao tiếp bất đồng bộ qua Adapter)            (Nội bộ dùng Hub, liên phòng dùng Bus)
```

#### 2. Bảng so sánh đối đầu toàn diện EAI vs ESB

| Tiêu chuẩn so sánh | EAI (Enterprise Application Integration) | ESB (Enterprise Service Bus) |
|:---|:---|:---|
| **Triết lý kiến trúc** | Tập trung (Hub & Spoke) hoặc đóng gói theo sản phẩm của nhà cung cấp | **Phân tán, hướng dịch vụ (SOA — Service-Oriented Architecture)** |
| **Mức độ liên kết** | Ghép nối tương đối chặt (Tight Coupling), phụ thuộc API ứng dụng | **Ghép nối lỏng lẻo (Loose Coupling)**, chuẩn hóa giao diện dịch vụ |
| **Giao thức chuẩn** | Dùng Adapter độc quyền riêng của từng vendor (Vendor-dependent) | Sử dụng **chuẩn mở Web Services (SOAP, REST, HTTP, AMQP)** |
| **Định dạng dữ liệu** | Phụ thuộc vào công cụ chuyển đổi nội bộ của EAI | Chuẩn hóa toàn diện thông qua **XML và JSON** |
| **Cơ chế định tuyến** | Định tuyến cơ bản tĩnh theo cấu hình đường dẫn | **Định tuyến thông minh theo nội dung (Content-Based Routing)** |
| **Khả năng mở rộng** | Giới hạn bên trong tường lửa nội bộ mạng doanh nghiệp | Dễ dàng mở rộng xuyên biên giới qua Internet và đa nền tảng Cloud |

#### 3. Bảng so sánh chi tiết JSON vs XML

| Tiêu chuẩn | JSON (JavaScript Object Notation) | XML (eXtensible Markup Language) |
|:---|:---|:---|
| **Cấu trúc dữ liệu** | Cặp **속성-값 (Key-Value)** `{}` và Mảng `[]` | Cấu trúc cây thẻ lồng nhau mở-đóng (`<tag>...</tag>`) |
| **Dung lượng tệp** | **Rất nhẹ**, ít ký tự thừa, tiết kiệm băng thông mạng | Cồng kềnh, nặng hơn do lặp lại các thẻ mở và đóng |
| **Tốc độ Parse** | **Cực nhanh**; hỗ trợ tự nhiên trong JS (`JSON.parse`) | Chậm hơn; cần bộ phân tích DOM / SAX Parser phức tạp |
| **Kiểm tra schema** | Hỗ trợ JSON Schema (ít phổ biến) | Hỗ trợ kiểm tra ràng buộc kiểu dữ liệu cực mạnh qua **DTD** và **XSD** |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Công thức kết nối Point-to-Point:** Khi hệ thống có $N = 10$ ứng dụng $\rightarrow \frac{10 \times 9}{2} = \mathbf{45}$ đường kết nối. Nếu $N = 20 \rightarrow \frac{20 \times 19}{2} = \mathbf{190}$ kết nối.
- **Bẫy 2: Nhược điểm chí tử của Hub & Spoke:** Điểm yếu lớn nhất là xuất hiện **단일 장애점 (SPOF - Single Point of Failure)** tại máy chủ Hub trung tâm.
- **Bẫy 3: Triết lý của ESB:** ESB luôn gắn liền với **SOA (Service-Oriented Architecture)** và nguyên tắc **느슨한 결합 (Loose Coupling - Ghép nối lỏng lẻo)**.
- **Bẫy 4: Định tuyến thông minh:** Hệ thống nào có khả năng đọc nội dung gói tin XML/JSON để quyết định chuyển tiếp gói tin đến dịch vụ nào? $\rightarrow$ **ESB (Content-based Routing)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bộ 3 công nghệ Web Services chuẩn đề thi
- **SOAP (Simple Object Access Protocol):** Giao thức truyền thông điệp dựa trên XML qua giao thức HTTP/HTTPS.
- **WSDL (Web Services Description Language):** Ngôn ngữ dựa trên XML dùng để mô tả chi tiết các dịch vụ web: các hàm cung cấp, tham số đầu vào và kiểu dữ liệu trả về.
- **UDDI (Universal Description, Discovery, and Integration):** Sổ danh bạ trực tuyến toàn cầu dựa trên XML cho phép các doanh nghiệp đăng ký và tìm kiếm các dịch vụ web.

#### 2. Công nghệ AJAX và REST
- **AJAX (Asynchronous JavaScript and XML):** Kỹ thuật cho phép trang web trao đổi một lượng nhỏ dữ liệu với máy chủ ở chế độ bất đồng bộ (Background), giúp cập nhật một phần nội dung giao diện mà **không cần tải lại toàn bộ trang web (페이지 새로고침 없음)**.
- **REST (Representational State Transfer):** Kiến trúc dịch vụ web sử dụng trực tiếp các phương thức HTTP chuẩn (`GET`, `POST`, `PUT`, `DELETE`) để thao tác trên các tài nguyên được định danh bằng URL (URI).

#### 3. Minh họa định dạng dữ liệu JSON vs XML
- **JSON (gọn nhẹ, cặp Key-Value):**
  ```json
  { "id": 101, "name": "Antigravity", "role": "Engineer" }
  ```
- **XML (cấu trúc thẻ cây phân cấp, kèm DTD/XSD):**
  ```xml
  <user>
      <id>101</id>
      <name>Antigravity</name>
      <role>Engineer</role>
  </user>
  ```

---

### 복습 체크리스트
- [ ] Tính thành thạo số kết nối Point-to-Point: $\frac{N(N-1)}{2}$.
- [ ] Nêu nhược điểm SPOF (Single Point of Failure) của mô hình Hub & Spoke.
- [ ] Phân biệt EAI (ghép nối chặt) và ESB (ghép nối lỏng lẻo, SOA).
- [ ] So sánh ưu nhược điểm giữa JSON (nhẹ, nhanh) và XML (chuẩn hóa DTD/XSD).
- [ ] Kể tên bộ ba Web Services: SOAP (giao thức), WSDL (mô tả dịch vụ), UDDI (sổ danh bạ tìm kiếm).
- [ ] Nêu định nghĩa AJAX là truyền thông bất đồng bộ không cần tải lại toàn trang.
