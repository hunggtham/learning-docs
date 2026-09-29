# 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

인터페이스, 검토, 연계, 기술

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **11. 디자인 패턴 (Design Pattern)**에서 만든 기준을 이어받아 **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

Ở bước 40/55, **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** xuất hiện như phần tiếp nối của **11. 디자인 패턴 (Design Pattern)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **정형 기술 검토 (FTR - Formal Technical Review)**, **동료검토 (Peer Review)**, **워크 스루 (Walk Through)**, **인스펙션 (Inspection)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

- **정형 기술 검토 (FTR - Formal Technical Review)**:
  - **동료검토 (Peer Review)**: Tác giả tự giải thích tài liệu, đồng nghiệp tìm lỗi.
  - **워크 스루 (Walk Through)**: Gửi tài liệu trước, họp review ngắn để tìm lỗi nhanh.
  - **인스펙션 (Inspection)**: Chuyên gia khác (không phải tác giả) kiểm tra chặt chẽ để tìm lỗi.
  - 💡 **Mẹo ghi nhớ**: 동료(Tự thuyết trình) / 워크스루(Họp ngắn) / 인스펙션(Chuyên gia chém).
- **연계 기술 (Connection Tech)**: 
  - DB Link, API, Socket (Cấp phát cổng), JDBC.
- **미들웨어 (Middleware)**: Phần mềm trung gian kết nối các hệ thống khác biệt.
  - **TP Monitor**: Giám sát Transaction (Giao dịch).
  - **MOM (Message-Oriented)**: Bất đồng bộ (비동기), dùng hàng đợi tin nhắn (메시지 큐).
  - **ORB (Object Request Broker)**: Hướng đối tượng, chuẩn CORBA.
  - **WAS (Web Application Server)**: Xử lý nội dung web động (동적인 콘텐츠).

---
# 소프트웨어 생명 주기 및 개발 방법론 (SDLC & Methodologies)

Như vậy, **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.