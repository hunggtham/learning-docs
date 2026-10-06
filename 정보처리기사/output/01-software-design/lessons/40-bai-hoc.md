# 14. 미들웨어 (Middleware)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **14. 미들웨어 (Middleware)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **학습 목표 (Mục tiêu)** đặt câu hỏi trung tâm và tiêu chí dùng để đọc các phần sau; sau đó sang **핵심 키워드 (Từ khóa)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối middleware với request pipeline, cross-cutting concern và order, để lớp trung gian không che mất lifecycle.

## 학습 목표 (Mục tiêu)

Sau khi đọc, hãy giải thích được định nghĩa và điểm khác nhau cốt lõi của **14. 미들웨어 (Middleware)**, đồng thời nối thuật ngữ 한국어 (tiếng Hàn) với nghĩa tiếng Việt.

Mục đích của bài này là hiểu **14. 미들웨어 (Middleware)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)** khi chuyển sang phần tiếp theo.

> **Nối mạch:** Trong **14. 미들웨어 (Middleware)**, **핵심 키워드 (Từ khóa)** nối từ **학습 목표 (Mục tiêu)** sang **선행·연결 개념 (Kiến thức liên kết)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 핵심 키워드 (Từ khóa)

미들웨어

> **Nối mạch:** Ở chặng này của **14. 미들웨어 (Middleware)**, **핵심 키워드 (Từ khóa)** dẫn sang **선행·연결 개념 (Kiến thức liên kết)**, nơi tài liệu chuẩn và vị trí sở hữu được chỉ rõ để biết chỗ đào sâu tiếp; **읽는 방법 (Cách đọc)** mở rộng hệ quả liên quan.

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**에서 만든 기준을 이어받아 **14. 미들웨어 (Middleware)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

> **Nối mạch:** Đặt trong câu hỏi lớn của **14. 미들웨어 (Middleware)**, **읽는 방법 (Cách đọc)** nối từ **선행·연결 개념 (Kiến thức liên kết)** sang **14. 미들웨어 (Middleware)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** ở mọi lần xuất hiện, giải thích bằng tiếng Việt trước và giữ `English / 한국어` ngay cạnh để đối chiếu đề.

---

> **Nối mạch:** Trong **14. 미들웨어 (Middleware)**, **14. 미들웨어 (Middleware)** nối từ **읽는 방법 (Cách đọc)** sang phần giải thích tiếp theo, vì phần trước cung cấp điểm tựa cho chủ đề này.

## 14. 미들웨어 (Middleware)

Ở bước 40/69, **14. 미들웨어 (Middleware)** xuất hiện như phần tiếp nối của **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**. Ta bắt đầu bằng việc xác định phạm vi và mục đích của nó, rồi mới đọc các quy tắc, điều kiện và ví dụ để thấy kiến thức hoạt động như thế nào.

Để đọc **14. 미들웨어 (Middleware)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Ví dụ là bước kiểm tra xem quy tắc vừa nêu tạo ra hệ quả gì trong một tình huống cụ thể.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

**개념 (Khái niệm):** 운영체제와 응용 프로그램 사이의 중재자 (Phần mềm trung gian đứng giữa OS và Ứng dụng).
💡 **Mẹo ghi nhớ 미들웨어:** DB, RPC, MOM, TP-Monitor, ORB, WAS

1.  **DB 미들웨어:** 2-Tier 원격 연결 (ODBC, IDAPI, Glue). (Kết nối CSDL 2 lớp).
2.  **RPC (Remote Procedure Call):** 원격을 로컬처럼 호출 (Entera, ONC/RPC). (Gọi hàm từ xa như gọi hàm cục bộ).
3.  **MOM (Message Oriented Middleware):** 비동기 메시지, 데이터 동기 (IBM MQ, JMS). (Truyền tin nhắn bất đồng bộ, đồng bộ dữ liệu hệ thống khác nền tảng).
4.  **TP-Monitor (Transaction Processing):** 항공/철도 예약, 빠른 응답/트랜잭션 감시 (tuxedo, tmax). (Giám sát giao dịch, đảm bảo tốc độ phản hồi nhanh cho đặt vé).
5.  **ORB (Object Request Broker):** 객체 지향, CORBA 표준 (Orbix). (Môi giới yêu cầu đối tượng, chuẩn CORBA).
6.  **WAS (Web Application Server):** 동적 콘텐츠, 웹 환경 핵심(Java/EJB) (WebLogic, WebSphere). (Xử lý nội dung web động, tác vụ doanh nghiệp quan trọng).
    *   *Example:* Apache là Web Server (tĩnh), còn WebLogic/Tomcat là WAS (động).

*   **솔루션 식별 & 명세서 작성:** 아키텍처 구성 정보, 구매 내역 확인 -> 제약사항 확인 (Xác định Middleware dựa trên kiến trúc và hóa đơn mua sắm -> Kiểm tra các hạn chế / constraints).

Như vậy, **14. 미들웨어 (Middleware)** không chỉ cung cấp các ý cần nhớ mà còn cho ta một cách định vị chúng trong mạch học. Khi chuyển sang **4. 관계형 데이터베이스 구조 (Cấu trúc CSDL Quan hệ)**, hãy mang theo tiêu chí vừa hình thành và kiểm tra xem phần mới đang dùng, mở rộng hay đối chiếu với nó như thế nào.

> **Bàn giao:** Sau **14. 미들웨어 (Middleware)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
