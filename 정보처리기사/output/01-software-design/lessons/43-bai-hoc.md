# 13. 시스템 연계 및 인터페이스 (System Interface & Integration)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

시스템, 연계, 인터페이스

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 13. 시스템 연계 및 인터페이스 (System Interface & Integration)
### 13.1 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
1.  **DB Link:** DB 객체 이용 (Kết nối trực tiếp qua DB Link).
2.  **API/Open API:** 프로그램 인터페이스 (Mở cổng API để ứng dụng khác gọi).
3.  **EAI (연계 솔루션):** 중계 서버/클라이언트 사용 (Dùng máy chủ trung gian Enterprise Application Integration).
4.  **Socket:** 포트 할당하여 연결 (Mở port mạng Socket để truyền dữ liệu).
5.  **Web Service:** WSDL, UDDI, SOAP 프로토콜 사용 (Dịch vụ web dùng giao thức chuẩn XML/SOAP).

### 13.2 인터페이스 통신 & 처리 유형 (Loại giao tiếp & xử lý)
*   **통신 유형 (Loại Giao tiếp):**
    *   **단방향 (Unidirectional):** 응답 없음 (Chỉ gửi, không cần phản hồi).
    *   **동기 (Synchronous):** 응답 대기 (Gửi và đợi phản hồi).
    *   **비동기 (Asynchronous):** 다른 작업 수행 (Gửi xong làm việc khác, trả lời sau).
*   **처리 유형 (Loại Xử lý):**
    *   **실시간 (Real-time):** 즉시 처리 (Xử lý ngay lập tức).
    *   **지연 처리 (Deferred):** 비용 절감을 위해 모아서 처리 (Trì hoãn xử lý để tiết kiệm chi phí).
    *   **배치 (Batch):** 대용량 일괄 처리 (Gom dữ liệu lớn xử lý 1 lần).

### 13.3 명세화 (Specification)
*   **송수신 데이터 명세화:** 데이터 필드명, 타입, 사이즈, **암호화 여부** 정의 (Đặc tả dữ liệu: Tên trường, Kiểu, Kích thước, và có Cần Mã hóa không).
*   **오류 식별 및 처리 방안 명세화:** 오류 코드, 메시지, 해결 방법 정의 (Đặc tả lỗi: Mã lỗi, Thông báo, Cách xử lý để dễ vận hành).

---
