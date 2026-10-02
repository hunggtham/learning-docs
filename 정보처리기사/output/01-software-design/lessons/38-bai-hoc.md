# 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối interface review với contract, integration và compatibility, để các hệ thống liên kết qua điểm giao có thể kiểm chứng.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **13. 시스템 연계 및 인터페이스 (System Interface & Integration)** khi chuyển sang phần tiếp theo.

> **Chuyển mạch:** Trong **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, **핵심 키워드 (Từ khóa)** tiếp nhận điểm tựa từ **학습 목표 (Mục tiêu)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **선행·연결 개념 (Kiến thức liên kết)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 핵심 키워드 (Từ khóa)

인터페이스, 검토, 연계, 기술

> **Chuyển mạch:** Ở chặng này của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, sau nội dung của **핵심 키워드 (Từ khóa)**, **선행·연결 개념 (Kiến thức liên kết)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **읽는 방법 (Cách đọc)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **11. 디자인 패턴 (Design Pattern)**에서 만든 기준을 이어받아 **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, **읽는 방법 (Cách đọc)** tiếp nhận điểm tựa từ **선행·연결 개념 (Kiến thức liên kết)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Chuyển mạch:** Trong **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** tiếp nhận điểm tựa từ **읽는 방법 (Cách đọc)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)

Sau khi đã đặt nền bằng **11. 디자인 패턴 (Design Pattern)**, ta chuyển sang **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**. Đây là mắt xích 38/69 của lộ trình; mục đích là biến tiêu chí vừa có thành cách đọc và cách dùng kiến thức mới, thay vì học một định nghĩa đứng riêng.

Để đọc **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng. Trong khối này, **정형 기술 검토 (FTR - Formal Technical Review)**, **동료검토 (Peer Review)**, **워크 스루 (Walk Through)**, **인스펙션 (Inspection)** không phải các đáp án rời: chúng lần lượt cho thấy các lựa chọn khác nhau trước cùng một vấn đề, nên hãy so sánh tiêu chí áp dụng và hệ quả của chúng trước khi ghi nhớ tên. Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Phần “2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)” được nối với nội dung kế tiếp để người mới biết mục đích, tiêu chí đọc và kết luận cần rút ra trước khi xem các dòng nguồn.

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

Ta có thể khép mục **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)** bằng một câu hỏi bàn giao: điều gì trong phần này sẽ trở thành tiền đề cho **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**? Giữ câu hỏi đó khi đọc mục sau để mạch học tiếp tục liền thay vì tách thành các ghi chú độc lập.

> **Bàn giao:** Sau **2. 인터페이스 검토 및 연계 기술 (Interface Review & Tech)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
