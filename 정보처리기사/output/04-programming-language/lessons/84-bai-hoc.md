# 281. 매시업과 SOA (SW Related Terms: Mashup & SOA)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, cơ chế kỹ thuật và ứng dụng thực tiễn của khái niệm **Mashup (매시업)** trong kỷ nguyên Web 2.0 và kinh tế Open API.
- Hiểu kiến trúc hướng dịch vụ (**SOA - Service Oriented Architecture / 서비스 지향 아키텍처**): Các nguyên tắc thiết kế dịch vụ độc lập, kết hợp lỏng lẻo (Loosely Coupled) và khả năng tái sử dụng liên hệ thống.
- Nhận diện 5 tầng kiến trúc chuẩn mực của SOA và vai trò huyết mạch của trục tích hợp dịch vụ doanh nghiệp (**ESB - Enterprise Service Bus**).

## 핵심 키워드 (Từ khóa)
- 매시업 (Mashup - Web Service Composition)
- 오픈 API (Open API Integration)
- SOA (Service Oriented Architecture)
- 느슨한 결합 (Loose Coupling) & 재사용성 (Reusability)
- ESB (Enterprise Service Bus - 서비스 연계 버스)
- SOAP & RESTful (Web Service Protocols)
- UDDI & WSDL (Service Registry & Description)

## 선행·연결 개념 (Kiến thức liên kết)
- [83-bai-hoc.md](83-bai-hoc.md): Các mô hình ngôn ngữ lập trình và tài liệu cấu trúc XML.
- [85-bai-hoc.md](85-bai-hoc.md): Công nghệ kết nối cơ sở dữ liệu JDBC vs ODBC.
- [69-bai-hoc.md](69-bai-hoc.md): Framework máy chủ và nguyên tắc kiến trúc mở rộng.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh trong đề thi:
  - Khi câu hỏi đề cập đến: "Kỹ thuật **kết hợp, pha trộn (Mix) nhiều dịch vụ web hoặc Open API có sẵn** từ các nguồn khác nhau để tạo ra một dịch vụ/ứng dụng mới hoàn toàn (ví dụ: Google Maps + Thông tin bất động sản)" $\rightarrow$ Chọn ngay **매시업 (Mashup)**.
  - Khi câu hỏi đề cập đến: "Kiến trúc hệ thống phần mềm được tổ chức thành các **khối dịch vụ (Service) độc lập, có thể tái sử dụng, giao tiếp qua giao thức chuẩn và kết hợp lỏng lẻo**" $\rightarrow$ Chọn ngay **SOA (서비스 지향 아키텍처)**.
  - Trục xương sống kết nối các dịch vụ trong SOA gọi là **ESB (Enterprise Service Bus)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Kỹ thuật Mashup (매시업):**
  - **Khái niệm:** Là ứng dụng web kết hợp dữ liệu hoặc chức năng từ hai hay nhiều nguồn khác nhau thông qua các giao diện lập trình ứng dụng mở (**Open API**) để tạo nên một sản phẩm mới có giá trị gia tăng cao hơn.
  - **Ví dụ kinh điển:**
    - Kết hợp *Google Maps API* + *Dữ liệu nhà trọ công cộng* $\rightarrow$ Dịch vụ tìm phòng trọ trên bản đồ tương tác.
    - Kết hợp *Twitter API* + *Bản đồ thời tiết* $\rightarrow$ Ứng dụng theo dõi tình trạng bão lũ theo thời gian thực.
  - **Lợi ích:** Rút ngắn tối đa thời gian phát triển sản phẩm, tận dụng thế mạnh của các nền tảng công nghệ lớn mà không phải tự xây dựng lại từ đầu.

- **2. Kiến trúc hướng dịch vụ (SOA - Service Oriented Architecture):**
  - **Định nghĩa:** Là mô hình kiến trúc phần mềm trong đó các chức năng nghiệp vụ được đóng gói thành các **Dịch vụ (Services)** tự quản, có ranh giới rõ ràng, có thể định vị và triệu gọi qua mạng bằng các giao thức chuẩn mở.
  - **3 vai trò cốt lõi trong tam giác SOA:**
    1. **Service Provider (Nhà cung cấp dịch vụ):** Xây dựng dịch vụ và xuất bản tài liệu mô tả (WSDL) lên danh bạ.
    2. **Service Broker / Registry (Cơ quan đăng kiểm):** Nơi lưu trữ danh mục dịch vụ để người dùng tra cứu (UDDI).
    3. **Service Requester / Consumer (Bên yêu cầu):** Tìm kiếm dịch vụ và gửi yêu cầu kết nối thực thi qua giao thức SOAP hoặc REST.

- **3. 5 tầng kiến trúc phân lớp của SOA:**

| Tầng kiến trúc | Tên tiếng Hàn & Anh | Chức năng nghiệp vụ chi tiết |
| :--- | :--- | :--- |
| **Tầng 1** | **표현 계층** (Presentation Layer) | Giao diện tương tác người dùng cuối (Web Portal, Ứng dụng di động, GUI). |
| **Tầng 2** | **업무 프로세스 계층** (Business Process) | Điều phối luồng quy trình nghiệp vụ tổng hợp (Choreography / Orchestration via BPEL). |
| **Tầng 3** | **서비스 중간 계층** (Service / ESB Layer) | Định tuyến thông điệp, chuyển đổi giao thức, trung chuyển dữ liệu giữa các dịch vụ thông qua **ESB**. |
| **Tầng 4** | **애플리케이션 계층** (Application Layer) | Các thành phần nghiệp vụ cụ thể của từng hệ thống con (Core Banking, CRM, ERP). |
| **Tầng 5** | **데이터 저장 계층** (Data Persistence) | Lưu trữ dữ liệu an toàn trên các hệ quản trị cơ sở dữ liệu (RDBMS, NoSQL, Data Warehouse). |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vai trò của Trục tích hợp ESB (Enterprise Service Bus):**
  - ESB đóng vai trò như một hạ tầng mạng lưới giao thông trung tâm, giải quyết bài toán "kết nối chằng chịt mạng nhện" (Point-to-Point) giữa $N$ ứng dụng khác nhau. Nhờ có ESB, các dịch vụ không cần biết địa chỉ vật lý hay định dạng giao thức của nhau; ESB sẽ tự động dịch chuyển đổi dữ liệu (XML sang JSON) và định tuyến thông điệp an toàn.

### 복습 체크리스트
- [ ] Nhớ Mashup là kỹ thuật trộn nhiều Open API để tạo ra một dịch vụ mới.
- [ ] Nắm vững định nghĩa SOA: Kiến trúc chia phần mềm thành các dịch vụ độc lập, loose coupling, tái sử dụng cao.
- [ ] Kể tên 3 thành phần tam giác SOA: Service Provider, Service Broker (UDDI), Service Requester.
- [ ] Nhớ tên trục xương sống kết nối và điều phối thông điệp trong SOA là **ESB (Enterprise Service Bus)**.
