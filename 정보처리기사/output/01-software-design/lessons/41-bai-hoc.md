# 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

시스템, 연계, 인터페이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**에서 만든 기준을 이어받아 **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

Sau khi đã đặt nền bằng **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, ta chuyển sang **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**. Đây là mắt xích 41/55 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Ta bắt đầu phần nội dung bằng **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)**. Hãy xác định **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** đang giải quyết câu hỏi nào, thành phần nào cần chú ý và giới hạn nào phải giữ trước khi chuyển sang các chi tiết nguồn.

### 13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)

Phần nguồn của **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

1.  **DB Link:** DB 객체 이용 (Kết nối trực tiếp qua DB Link).
2.  **API/Open API:** 프로그램 인터페이스 (Mở cổng API để ứng dụng khác gọi).
3.  **EAI (연계 솔루션):** 중계 서버/클라이언트 사용 (Dùng máy chủ trung gian Enterprise Application Integration).
4.  **Socket:** 포트 할당하여 연결 (Mở port mạng Socket để truyền dữ liệu).
5.  **Web Service:** WSDL, UDDI, SOAP 프로토콜 사용 (Dịch vụ web dùng giao thức chuẩn XML/SOAP).

Phần **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** không có nhiều dữ liệu rời để tách nhỏ, vì vậy hãy giữ câu hỏi mục đích và tự chốt bằng một câu giải thích trước khi đi tiếp.

Ta vừa chốt **13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Đoạn **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)

Các ý ngay dưới **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

*   **통신 유형 (Loại Giao tiếp):**
    *   **단방향 (Unidirectional):** 응답 없음 (Chỉ gửi, không cần phản hồi).
    *   **동기 (Synchronous):** 응답 대기 (Gửi và đợi phản hồi).
    *   **비동기 (Asynchronous):** 다른 작업 수행 (Gửi xong làm việc khác, trả lời sau).
*   **처리 유형 (Loại Xử lý):**
    *   **실시간 (Real-time):** 즉시 처리 (Xử lý ngay lập tức).
    *   **지연 처리 (Deferred):** 비용 절감을 위해 모아서 처리 (Trì hoãn xử lý để tiết kiệm chi phí).
    *   **배치 (Batch):** 대용량 일괄 처리 (Gom dữ liệu lớn xử lý 1 lần).

Các bullet của **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)**, đừng bắt đầu lại từ số không. **13.3 명세화 (Specification)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Ở đoạn **13.3 명세화 (Specification)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 13.3 명세화 (Specification)

Bây giờ ta đi vào nội dung của **13.3 명세화 (Specification)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

*   **송수신 데이터 명세화:** 데이터 필드명, 타입, 사이즈, **암호화 여부** 정의 (Đặc tả dữ liệu: Tên trường, Kiểu, Kích thước, và có Cần Mã hóa không).
*   **오류 식별 및 처리 방안 명세화:** 오류 코드, 메시지, 해결 방법 정의 (Đặc tả lỗi: Mã lỗi, Thông báo, Cách xử lý để dễ vận hành).

---

Các bullet của **13.3 명세화 (Specification)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Như vậy, **13.3 명세화 (Specification)** đã hoàn thành vai trò của mình trong mục này: nó cho ta một khung giải thích để nối các chi tiết nguồn với câu hỏi thực tế. Giữ khung đó khi bước sang phần tiếp theo.

Ta có thể khép mục **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.