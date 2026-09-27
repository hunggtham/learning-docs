# 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

## 핵심 키워드 (Từ khóa)

시스템, 연계, 미들웨어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 앞 단원의 정의를 바탕으로 절차와 비교 기준을 확장한다. 먼저 용어의 주체·대상·목적을 확인한 뒤 세부 규칙을 읽으면 암기 부담이 줄어든다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 비슷한 용어는 한 줄로 비교한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

### 요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)
- **요구사항 검토 (Requirements Review):** 동료검토, 워크스루, 인스펙션. (Review thủ công bởi người).
- **프로토타이핑 (Prototyping):** 견본품을 만들어 최종 결과물을 예측. (Làm bản nháp/prototype để dự đoán kết quả).
- **테스트 설계 (Test Design):** 요구사항이 현실적으로 테스트 가능한지 검토 (Test Case 생성). (Tạo Test Case để xem yêu cầu có khả thi không).
- **CASE 도구 활용 (CASE Tools):** 일관성 분석(Consistency Analysis)을 통해 요구사항 변경사항 추적 및 분석. (Dùng tool để phân tích tính nhất quán).

### 시스템 연계 기술 (Các công nghệ liên kết hệ thống)
- **DB Link:** DB에서 제공하는 DB Link 객체를 이용. (Dùng trực tiếp link kết nối của DB).
- **API / Open API:** 송신 시스템의 DB에서 데이터를 읽어와 제공하는 프로그램. (Giao diện lập trình ứng dụng mở).
- **연계 솔루션:** EAI 서버와 송·수신 시스템에 설치되는 클라이언트(Client)를 이용. (Giải pháp dùng EAI Server).
- **Socket:** 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트와 연결. (Tạo socket và cấp phát port để giao tiếp mạng).
- **Web Service:** WSDL, UDDI, SOAP 프로토콜을 이용. (Dịch vụ web dùng chuẩn SOAP/WSDL).

### 연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)
- **송신 시스템 (Sender System):** 데이터를 전송 형식에 맞게 변환하여 송신. (Hệ thống gửi, chuyển đổi dữ liệu ra định dạng chuẩn).
- **수신 시스템 (Receiver System):** 수신한 데이터를 시스템에 맞게 변환하여 반영. (Hệ thống nhận, chuyển đổi dữ liệu chuẩn vào DB).
- **연계 서버 (Integration Server):** 송수신 현황을 모니터링. (Server trung gian giám sát quá trình truyền dữ liệu).

### 미들웨어(Middleware) 상세 (Chi tiết Middleware)
- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공.
- **DB (DataBase):** 2-Tier 아키텍처에 주로 사용, 클라이언트와 원격 DB를 연결. (Kết nối Client-DB).
- **RPC (Remote Procedure Call):** 원격 프로시저를 로컬 프로시저처럼 호출. (Gọi hàm từ xa như gọi hàm cục bộ).
- **MOM (Message Oriented Middleware):** 비동기형 메시지 전달 (이기종 분산 데이터 시스템). (Truyền tin nhắn bất đồng bộ).
- **TP-Monitor (Transaction Processing Monitor):** 온라인 트랜잭션 처리 및 감시 (항공기/철도 예약). (Quản lý giao dịch online tốc độ cao).
- **ORB (Object Request Broker):** CORBA 표준 스펙을 구현한 객체 지향 미들웨어. (Middleware hướng đối tượng chuẩn CORBA).
- **WAS (Web Application Server):** 동적인 콘텐츠를 처리하는 미들웨어. (Xử lý web động).

---

# 3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)
*(Lưu ý: Tùy theo chương trình, Database có thể thuộc Subject 1 hoặc 3. Dưới đây là kiến thức cốt lõi về DB)*

---
