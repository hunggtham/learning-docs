# 14. 미들웨어 (Middleware)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **14. 미들웨어 (Middleware)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

미들웨어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 14. 미들웨어 (Middleware)
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
