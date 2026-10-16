# Môn 2 · Bài 09 — Tích hợp hệ thống EAI/ESB và giao thức truyền thông

> **Mạch đọc:** [README](../README.md) là bản đồ chủ đề của **Môn 2 — 소프트웨어 개발 (Software Development)**. Tiếp nối [Bài 08: Hiện thực đơn vị module và IPC](08-hien-thuc-module-va-ipc.md) ở cấp độ tiến trình đơn lẻ, bài học này nâng tầm bài toán tích hợp lên quy mô doanh nghiệp và hệ thống phân tán đa nền tảng: **Tích hợp ứng dụng doanh nghiệp (EAI / ESB)**. Bài học phân tích 4 mô hình kiến trúc tích hợp EAI kinh điển, sự chuyển dịch sang trục dịch vụ doanh nghiệp ESB, cùng hai định dạng dữ liệu cốt lõi (JSON, XML) và công nghệ truyền thông bất đồng bộ AJAX/REST.

> **Phạm vi nguồn:** Hợp nhất và chuẩn hóa nội dung từ các bài học cũ `77-bai-hoc.md` và `79-bai-hoc.md` (tương ứng với các mục 23, 27 và phần EAI trong tài liệu chuẩn gốc). Toàn bộ công thức tính số kết nối và so sánh cấu trúc định dạng được đối chiếu chính xác theo chuẩn khảo thí HRDK.

> **Mạch kiến thức:** Một doanh nghiệp lớn thường vận hành hàng chục hệ thống phần mềm dị thể (ERP, CRM, Kế toán, Ngân hàng) viết bằng nhiều ngôn ngữ khác nhau trên các hệ điều hành khác nhau. Bài học này giải quyết ba vấn đề kỹ thuật: (1) Bốn mô hình kiến trúc EAI (Point-to-Point, Hub & Spoke, Message Bus, Hybrid) giải quyết bài toán kết nối mạng ra sao và điểm lỗi đơn (SPOF) nằm ở đâu? (2) ESB nâng cấp kiến trúc tích hợp lên nền tảng hướng dịch vụ (SOA) như thế nào? (3) Tại sao định dạng JSON và kỹ thuật truyền thông bất đồng bộ AJAX lại thay thế dần XML để trở thành chuẩn mực trao đổi dữ liệu web hiện đại?

---

## 1. 기업 애플리케이션 통합 (EAI — Enterprise Application Integration)

**EAI는 기업 내의 서로 다른 플랫폼 및 애플리케이션들을 통합하여 상호 간의 데이터 연계와 비즈니스 프로세스를 자동화하는 솔루션이다.**

Trong quá trình phát triển của doanh nghiệp, các phần mềm thường được mua sắm hoặc xây dựng riêng lẻ theo từng giai đoạn, tạo thành các "hòn đảo thông tin" (Information Silos). EAI đóng vai trò như chiếc cầu nối phần mềm trung gian (Middleware) giúp các hệ thống dị thể có thể trao đổi thông tin liền mạch.

### Bảng so sánh 4 mô hình kiến trúc EAI kinh điển

| Mô hình EAI | Cơ chế kết nối | Ưu điểm cốt lõi | Nhược điểm (Bẫy đề thi cốt lõi) |
| :--- | :--- | :--- | :--- |
| **Point-to-Point** | Kết nối trực tiếp 1:1 giữa từng cặp ứng dụng | Rất đơn giản khi hệ thống chỉ có 2 hoặc 3 ứng dụng | Khi số hệ thống $N$ tăng, số kết nối bùng nổ theo cấp số nhân: $\mathbf{\frac{N(N-1)}{2}}$; cực kỳ khó mở rộng và bảo trì |
| **Hub & Spoke** | Mọi hệ thống đều nối tập trung về một máy chủ trung gian là **Hub trung tâm (중앙 집중형)** | Dễ dàng quản lý dữ liệu, kiểm soát bảo mật và mở rộng chi nhánh mới | **Điểm lỗi đơn (SPOF — Single Point of Failure)**; nếu máy chủ Hub bị nghẽn mạng hoặc sập nguồn thì toàn bộ hệ thống tê liệt |
| **Message Bus (ESB)** | Các ứng dụng liên lạc thông qua một đường **trục thông điệp chung (미들웨어 버스)** dùng bộ đệm thông điệp | Khả năng mở rộng vượt trội, chịu tải dữ liệu lớn, truyền thông bất đồng bộ tin cậy | Chi phí mua sắm middleware và thiết kế cấu trúc ban đầu phức tạp |
| **Hybrid** | Kết hợp mô hình: Nội bộ từng cụm dùng **Hub & Spoke**, giữa các cụm lớn liên kết bằng **Message Bus** | Tận dụng sự linh hoạt của Hub trong nội bộ và khả năng mở rộng của Bus giữa các phân vùng lớn | Đòi hỏi đội ngũ kỹ thuật trình độ cao để quản trị hai kiến trúc song song |

### Công thức tính số lượng đường nối của Point-to-Point
$$\text{Số kết nối} = \frac{N(N - 1)}{2}$$
- *Ví dụ đề thi:* Doanh nghiệp có $N = 10$ hệ thống độc lập cần tích hợp theo mô hình Point-to-Point:
  $$\text{Số đường kết nối} = \frac{10 \times (10 - 1)}{2} = \mathbf{45} \text{ kết nối}$$

---

## 2. ESB (Enterprise Service Bus) — Trục dịch vụ doanh nghiệp

Sự phát triển của kiến trúc phần mềm đã đưa EAI tiến hóa lên mô hình **ESB (Enterprise Service Bus)**:

### So sánh đối đầu EAI vs ESB

| Tiêu chuẩn so sánh | EAI (Enterprise Application Integration) | ESB (Enterprise Service Bus) |
| :--- | :--- | :--- |
| **Triết lý kiến trúc** | Tập trung (Hub & Spoke) hoặc độc quyền | **Phân tán, hướng dịch vụ (SOA — Service-Oriented Architecture)** |
| **Mức độ liên kết** | Ghép nối tương đối chặt (Tight Coupling) | **Ghép nối lỏng lẻo (Loose Coupling)** |
| **Giao thức chuẩn** | Thường dùng Adapter riêng của từng nhà cung cấp | Sử dụng **chuẩn mở Web Services (SOAP, RESTful)** |
| **Định dạng dữ liệu** | Phụ thuộc vào công cụ chuyển đổi nội bộ | Chuẩn hóa thông qua **XML và JSON** |
| **Khả năng mở rộng** | Khó mở rộng xuyên qua ranh giới mạng Internet | Dễ dàng mở rộng qua mạng Internet và môi trường Cloud |

---

## 3. 데이터 교환 포맷: JSON vs XML — Định dạng trao đổi dữ liệu

Khi các hệ thống phần mềm giao tiếp qua mạng máy tính, dữ liệu bắt buộc phải được đóng gói thành các định dạng văn bản chuẩn mở để cả hai bên đều có thể phân tích cú pháp (Parsing):

### Bảng so sánh chi tiết JSON vs XML

| Tiêu chuẩn so sánh | JSON (JavaScript Object Notation) | XML (eXtensible Markup Language) |
| :--- | :--- | :--- |
| **Cấu trúc dữ liệu** | Cặp **속성-값 (Key-Value Pairs)** `{}` và Mảng `[]` | Cấu trúc cây thẻ lồng nhau mở-đóng (`<tag>...</tag>`) |
| **Dung lượng tệp** | **Rất nhẹ**, ít ký tự thừa, tiết kiệm băng thông | Cồng kềnh, nặng hơn do lặp lại các thẻ đóng mở |
| **Tốc độ xử lý (Parse)** | **Cực nhanh**; được hỗ trợ tự nhiên trong JavaScript (`JSON.parse()`) | Chậm hơn; cần bộ phân tích DOM / SAX Parser phức tạp |
| **Khả năng kiểm tra cấu trúc** | Hỗ trợ JSON Schema (ít phổ biến hơn) | Hỗ trợ kiểm tra ràng buộc kiểu dữ liệu cực mạnh qua **DTD** và **XML Schema (XSD)** |
| **Ứng dụng chủ đạo** | Các ứng dụng Web hiện đại, Mobile App, RESTful API | Hệ thống tài chính ngân hàng truyền thống, dịch vụ Web SOAP |

### Cú pháp mẫu trực quan:
- **JSON:**
  ```json
  { "id": 101, "name": "Antigravity", "role": "Engineer" }
  ```
- **XML:**
  ```xml
  <user>
      <id>101</id>
      <name>Antigravity</name>
      <role>Engineer</role>
  </user>
  ```

---

## 4. 비동기 통신 기술: AJAX 및 RESTful API — Truyền thông web bất đồng bộ

### 4.1. AJAX (Asynchronous JavaScript and XML)
**AJAX는 웹 브라우저가 서버와 비동기적으로 데이터를 교환함으로써 전체 페이지를 다시 고치지 않고도 웹 페이지의 일부분만을 갱신할 수 있는 웹 개발 기술이다.**

- **Cơ chế vận hành:**
  - Trình duyệt khởi tạo đối tượng `XMLHttpRequest` hoặc hàm `fetch()` trong JavaScript để gửi yêu cầu HTTP ngầm đến máy chủ.
  - **Giao tiếp bất đồng bộ (비동기 통신):** Người dùng vẫn có thể tiếp tục thao tác cuộn trang hoặc bấm chuột bình thường mà không bị hiện tượng "đơ" màn hình trong khi máy chủ đang xử lý.
  - **Cập nhật giao diện cục bộ (부분 화면 갱신):** Khi máy chủ trả về kết quả (thường là dữ liệu JSON), JavaScript chỉ vẽ lại đúng phần tử HTML tương ứng trên cây DOM (ví dụ: cập nhật số lượt Like, hiển thị gợi ý tìm kiếm tức thời) mà **không làm chớp màn hình (không tải lại toàn bộ trang)**.

---

### 4.2. RESTful API (Representational State Transfer)
- Là phong cách kiến trúc phần mềm định hướng tài nguyên (Resource-oriented) trên nền tảng giao thức HTTP.
- Mỗi tài nguyên được định danh duy nhất bằng một địa chỉ **URI** (ví dụ: `/users/101`).
- Sử dụng đúng 4 phương thức HTTP tiêu chuẩn tương ứng với các thao tác CRUD:
  - **`GET`**: Đọc / Truy vấn tài nguyên.
  - **`POST`**: Tạo mới tài nguyên.
  - **`PUT`**: Cập nhật toàn bộ tài nguyên.
  - **`DELETE`**: Xóa tài nguyên.
- **Tính chất phi trạng thái (Stateless):** Mỗi yêu cầu gửi từ Client lên Server phải chứa đầy đủ mọi thông tin cần thiết để Server xử lý, Server không lưu trữ ngữ cảnh phiên làm việc của Client.

---

## 5. Nối mạch kiến thức sang bài tiếp theo

Khi các hệ thống ứng dụng doanh nghiệp được kết nối xuyên suốt qua mạng thông qua EAI/ESB và truyền tải dữ liệu bằng JSON/AJAX, một nguy cơ kỹ thuật sống còn lập tức xuất hiện: **Lỗ hổng an toàn thông tin trên đường truyền và sự sai lệch chức năng của các giao diện liên kết**.

Để đảm bảo dữ liệu không bị nghe lén, giả mạo và các giao diện hoạt động chính xác 100%, chúng ta sẽ chuyển sang **[Bài 10: Bảo mật giao diện và công cụ xác minh tích hợp](10-bao-mat-giao-dien-va-kiem-chung.md)** để khảo sát các giao thức bảo mật mạng (IPSec, SSL/TLS), công cụ kiểm tra tính toàn vẹn Tripwire và các framework tự động xác minh giao diện (xUnit, STAF, FitNesse).

---

## 6. 복습 체크리스트 (Checklist ôn tập)

- [ ] Kể tên đầy đủ 4 mô hình EAI: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- [ ] Tính đúng số kết nối của Point-to-Point theo công thức $N(N-1)/2$.
- [ ] Nhớ nhược điểm Single Point of Failure (SPOF) của mô hình Hub & Spoke.
- [ ] Phân biệt được sự chuyển dịch từ EAI (tập trung) sang ESB (phân tán, hướng dịch vụ SOA).
- [ ] So sánh được ưu điểm của JSON so với XML (nhẹ hơn, ít ký tự thừa, parse nhanh hơn).
- [ ] Định nghĩa AJAX là công nghệ truyền thông bất đồng bộ (비동기 통신) cho phép cập nhật cục bộ không tải lại toàn trang.
- [ ] Kể tên đối tượng nền tảng của AJAX: `XMLHttpRequest` (hoặc `fetch`).
- [ ] Nắm vững 4 phương thức HTTP trong RESTful API: GET (đọc), POST (tạo), PUT (sửa), DELETE (xóa).
