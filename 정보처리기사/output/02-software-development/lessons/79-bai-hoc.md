# 27. JSON 및 AJAX (JSON & AJAX)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm, cấu trúc cú pháp và ưu điểm của định dạng trao đổi dữ liệu JSON (JavaScript Object Notation).
- Hiểu rõ cơ chế hoạt động của công nghệ truyền thông bất đồng bộ AJAX (Asynchronous JavaScript and XML) giữa trình duyệt web (Client) và máy chủ (Server).
- Phân tích sự kết hợp giữa AJAX và JSON trong việc xây dựng các ứng dụng web tương tác mượt mà, không cần tải lại toàn bộ trang (Full Page Reload).

## 핵심 키워드 (Từ khóa)
- JSON (JavaScript Object Notation / 속성-값 쌍 / 개방형 표준 포맷)
- AJAX (Asynchronous JavaScript and XML / 비동기 통신 기술)
- 비동기 처리 (Asynchronous Processing / 페이지 깜빡임 없음)
- XMLHttpRequest (XHR 객체 / Fetch API)
- Key-Value Pair (속성-값 쌍 구조)
- 직렬화 및 역직렬화 (Serialization & Deserialization)

## 선행·연결 개념 (Kiến thức liên kết)
- [78-bai-hoc.md](78-bai-hoc.md): Công cụ kiểm tra tính toàn vẹn hệ thống Tripwire.
- [80-bai-hoc.md](80-bai-hoc.md): Danh sách tuyến tính liên tục và danh sách liên kết.
- [정보처리기사/output/01-software-design/lessons/09-bai-hoc.md](../../01-software-design/lessons/09-bai-hoc.md): Thiết kế giao diện người dùng (UI/UX) và tương tác hệ thống.

## 읽는 방법 (Cách đọc)
- Phân biệt vai trò của hai công nghệ:
  - **JSON:** Là **Định dạng dữ liệu** (Data Format). Dữ liệu được biểu diễn dưới dạng các cặp `tên: giá trị` (Key-Value) bọc trong dấu ngoặc nhọn `{}` và mảng bọc trong ngoặc vuông `[]`. Nhẹ hơn, dễ đọc hơn XML rất nhiều.
  - **AJAX:** Là **Kỹ thuật truyền thông** (Communication Technique). Trình duyệt gửi yêu cầu ngầm đến máy chủ bằng đối tượng `XMLHttpRequest` hoặc `fetch`, máy chủ trả về dữ liệu (thường là JSON), sau đó JavaScript chỉ cập nhật đúng phần giao diện cần thay đổi (ví dụ: nút Like, ô tìm kiếm gợi ý) mà không cần load lại cả trang.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết giữa JSON và XML:**

| Tiêu chí | JSON (JavaScript Object Notation) | XML (eXtensible Markup Language) |
| :--- | :--- | :--- |
| **Cấu trúc dữ liệu** | Cặp **속성-값 (Key-Value Pairs)** và mảng giá trị | Cấu trúc cây thẻ lồng nhau (Open-Close Tags: `<tag>...</tag>`) |
| **Dung lượng & Tốc độ** | Rất nhẹ, ít ký tự thừa; tốc độ truyền và phân tích cú pháp (Parsing) cực nhanh | Nặng hơn do các thẻ đóng mở lặp lại; tốc độ parse chậm hơn |
| **Tính tương thích** | Được hỗ trợ tự nhiên trong JavaScript (`JSON.parse()`, `JSON.stringify()`) và hầu hết ngôn ngữ hiện đại | Cần bộ phân tích DOM Parser phức tạp để bóc tách dữ liệu |
| **Khả năng đọc** | Con người dễ đọc, máy dễ bóc tách tự động | Dễ đọc nhưng cồng kềnh với dữ liệu lớn |

- **Đặc trưng cốt lõi của công nghệ AJAX:**
  - **비동기 통신 (Giao tiếp bất đồng bộ):** Người dùng vẫn có thể tiếp tục thao tác cuộn trang, bấm chuột trên giao diện trong khi dữ liệu từ máy chủ đang được tải ngầm.
  - **부분 화면 갱신 (Cập nhật giao diện cục bộ):** Chỉ vẽ lại phần DOM thay đổi, giảm thiểu băng thông mạng và mang lại trải nghiệm mượt mà như ứng dụng máy tính (Desktop App).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế xử lý trong AJAX:**
  - Trình duyệt khởi tạo đối tượng `XMLHttpRequest` hoặc dùng hàm `fetch()` trong JavaScript ES6.
  - Gửi yêu cầu HTTP (GET/POST/PUT/DELETE) tới RESTful API.
  - Khi máy chủ hoàn tất và trả về mã trạng thái `200 OK`, hàm gọi lại (Callback) hoặc Promise xử lý chuỗi JSON nhận được, phân tích thành Object trong bộ nhớ và cập nhật lên cây HTML DOM.

### 복습 체크리스트
- [ ] Nhớ định nghĩa của JSON: Định dạng dữ liệu chuẩn mở dạng 속성-값 쌍 (Key-Value Pairs).
- [ ] Nhớ định nghĩa của AJAX: Công nghệ giao tiếp bất đồng bộ (비동기 통신) không cần tải lại toàn bộ trang.
- [ ] Phân biệt được ưu điểm của JSON so với XML (nhẹ hơn, parse nhanh hơn).
