# 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

## 학습 목표 (Mục tiêu)

이 단원을 읽은 뒤 **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**의 정의와 핵심 차이를 한국어 용어와 베트남어 의미로 설명할 수 있어야 한다.

Mục đích của bài này là hiểu **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** như một khái niệm có thể giải thích và áp dụng: nêu được nó dùng để làm gì, nhận diện điều kiện hoặc giới hạn quan trọng, rồi đối chiếu với **14. 미들웨어 (Middleware)** khi chuyển sang phần tiếp theo.

## 핵심 키워드 (Từ khóa)

시스템, 연계, 미들웨어

## 선행·연결 개념 (Kiến thức liên kết)

이 단원은 **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**에서 만든 기준을 이어받아 **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**을(를) 확장한다. 먼저 앞 단원의 기준이 여기서 어떤 질문으로 바뀌는지 확인하면, 세부 규칙을 따로 외우지 않고 관계로 읽을 수 있다.

## 읽는 방법 (Cách đọc)

1. 제목에서 **무엇을(대상)**, **왜 쓰는지(목적)**를 먼저 찾는다.
2. 본문에서 순서·조건·장단점을 표시하고, 앞 단원과 다음 단원 사이의 연결 문장을 확인한다.
3. 예시를 읽은 뒤 책을 덮고 핵심을 한국어 한 문장과 베트남어 한 문장으로 다시 말한다.

> **Quy ước:** `한국어 (English) (Tiếng Việt)`. Đọc phần tiếng Việt liền sau ý tiếng Hàn để vừa hiểu nghĩa vừa giữ được từ khóa làm đề.

---

## 17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)

Từ **13. 시스템 연계 및 인터페이스 (System Interface & Integration)**, ta đã có điểm tựa để bước vào **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)**. Câu hỏi dẫn đường ở đây là: phần mới này đang làm rõ, mở rộng hay đối chiếu điều gì? Trả lời được câu hỏi đó sẽ giúp ta hiểu mục đích của mục 42/55 trước khi đi vào chi tiết.

Để đọc **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** như một bài học cho người mới, hãy giữ câu hỏi: **khái niệm này đang giải quyết vấn đề nào, hoạt động theo điều kiện nào và tạo ra hệ quả gì?** Phần nguồn bên dưới cung cấp các dấu hiệu và quy tắc để trả lời câu hỏi này. Các bullet đang nén nhiều ý; hãy nối chúng thành chuỗi đối tượng → điều kiện → hệ quả để thấy quan hệ giữa chúng.  Hãy chốt phần này bằng chuỗi **đối tượng → điều kiện → hệ quả** trước khi chuyển tiếp.

Để không đọc **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** như một mẩu ghi chú rời, trước hết hãy đặt nó vào mục đích của toàn mục. Các ý tiếp theo sẽ lần lượt cho thấy khái niệm được nhận diện và sử dụng theo tiêu chí nào.

### 요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)

Các ý ngay dưới **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- **요구사항 검토 (Requirements Review):** 동료검토, 워크스루, 인스펙션. (Review thủ công bởi người).
- **프로토타이핑 (Prototyping):** 견본품을 만들어 최종 결과물을 예측. (Làm bản nháp/prototype để dự đoán kết quả).
- **테스트 설계 (Test Design):** 요구사항이 현실적으로 테스트 가능한지 검토 (Test Case 생성). (Tạo Test Case để xem yêu cầu có khả thi không).
- **CASE 도구 활용 (CASE Tools):** 일관성 분석(Consistency Analysis)을 통해 요구사항 변경사항 추적 및 분석. (Dùng tool để phân tích tính nhất quán).

Các bullet của **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Ta vừa chốt **요구사항 검증 방법 추가 (Các phương pháp kiểm chứng yêu cầu bổ sung)** bằng các điều kiện và điểm phân biệt của nó. Từ tiêu chí đó, ta chuyển sang **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** để xem câu hỏi được tiếp tục, mở rộng hay đối chiếu ra sao.
Ở đoạn **시스템 연계 기술 (Các công nghệ liên kết hệ thống)**, ta tập trung vào vai trò và giới hạn riêng của nó trong câu hỏi chung; các ý bên dưới sẽ giải thích vì sao nó cần xuất hiện ở bước này.

### 시스템 연계 기술 (Các công nghệ liên kết hệ thống)

Bây giờ ta đi vào nội dung của **시스템 연계 기술 (Các công nghệ liên kết hệ thống)**. Mỗi bullet hoặc bảng bên dưới nên được đọc như bằng chứng cho phạm vi và cách dùng vừa định vị, không phải như danh sách tách rời.

- **DB Link:** DB에서 제공하는 DB Link 객체를 이용. (Dùng trực tiếp link kết nối của DB).
- **API / Open API:** 송신 시스템의 DB에서 데이터를 읽어와 제공하는 프로그램. (Giao diện lập trình ứng dụng mở).
- **연계 솔루션:** EAI 서버와 송·수신 시스템에 설치되는 클라이언트(Client)를 이용. (Giải pháp dùng EAI Server).
- **Socket:** 통신을 위한 소켓을 생성하여 포트를 할당하고 클라이언트와 연결. (Tạo socket và cấp phát port để giao tiếp mạng).
- **Web Service:** WSDL, UDDI, SOAP 프로토콜을 이용. (Dịch vụ web dùng chuẩn SOAP/WSDL).

Các bullet của **시스템 연계 기술 (Các công nghệ liên kết hệ thống)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Sau khi đọc **시스템 연계 기술 (Các công nghệ liên kết hệ thống)**, đừng bắt đầu lại từ số không. **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** dựa trên điểm vừa chốt để làm rõ trường hợp hoặc cơ chế tiếp theo; hãy đối chiếu hai phần trước khi ghi nhớ riêng từng ý.
Với **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)**, mục tiêu đọc là nhận ra đối tượng, điều kiện và phạm vi áp dụng trước khi đi tiếp; phần nguồn dưới đây cung cấp các chi tiết cho mục tiêu đó.

### 연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)

Phần nguồn của **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** sẽ lấp đầy khung giải thích vừa mở. Khi đọc, hãy chú ý dấu hiệu nhận biết, điều kiện áp dụng và hệ quả trước khi chuyển sang đoạn bàn giao.

- **송신 시스템 (Sender System):** 데이터를 전송 형식에 맞게 변환하여 송신. (Hệ thống gửi, chuyển đổi dữ liệu ra định dạng chuẩn).
- **수신 시스템 (Receiver System):** 수신한 데이터를 시스템에 맞게 변환하여 반영. (Hệ thống nhận, chuyển đổi dữ liệu chuẩn vào DB).
- **연계 서버 (Integration Server):** 송수신 현황을 모니터링. (Server trung gian giám sát quá trình truyền dữ liệu).

Các bullet của **연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

**연계 매커니즘 구성요소 (Thành phần cơ chế liên kết)** vừa cho ta cách đặt câu hỏi. Bây giờ **미들웨어(Middleware) 상세 (Chi tiết Middleware)** cung cấp bước tiếp theo trong việc trả lời, vì vậy mối nối giữa hai đoạn quan trọng hơn việc học chúng như hai danh sách rời.
Đoạn **미들웨어(Middleware) 상세 (Chi tiết Middleware)** trả lời một phần cụ thể của vấn đề đang học. Hãy dùng các ý sau để kiểm tra cách khái niệm này vận hành, thay vì chỉ ghi nhớ tên gọi.

### 미들웨어(Middleware) 상세 (Chi tiết Middleware)

Các ý ngay dưới **미들웨어(Middleware) 상세 (Chi tiết Middleware)** cung cấp dữ liệu và quy tắc để trả lời câu hỏi vừa đặt ra. Hãy đọc chúng theo quan hệ điều kiện–hệ quả, rồi dùng câu chốt sau đoạn để tự kiểm tra cách hiểu.

- 운영체제와 응용 프로그램 사이에서 다양한 서비스를 제공.
- **DB (DataBase):** 2-Tier 아키텍처에 주로 사용, 클라이언트와 원격 DB를 연결. (Kết nối Client-DB).
- **RPC (Remote Procedure Call):** 원격 프로시저를 로컬 프로시저처럼 호출. (Gọi hàm từ xa như gọi hàm cục bộ).
- **MOM (Message Oriented Middleware):** 비동기형 메시지 전달 (이기종 분산 데이터 시스템). (Truyền tin nhắn bất đồng bộ).
- **TP-Monitor (Transaction Processing Monitor):** 온라인 트랜잭션 처리 및 감시 (항공기/철도 예약). (Quản lý giao dịch online tốc độ cao).
- **ORB (Object Request Broker):** CORBA 표준 스펙을 구현한 객체 지향 미들웨어. (Middleware hướng đối tượng chuẩn CORBA).
- **WAS (Web Application Server):** 동적인 콘텐츠를 처리하는 미들웨어. (Xử lý web động).

---

# 3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)

Phần **3과목: 데이터베이스 (Phần 3: Cơ sở dữ liệu)** cần được đọc như một bước trong bài giảng: trước hết xác định mục đích, sau đó nối các ý bên dưới với điều kiện và hệ quả trước khi ghi nhớ từng dòng.
*(Lưu ý: Tùy theo chương trình, Database có thể thuộc Subject 1 hoặc 3. Dưới đây là kiến thức cốt lõi về DB)*

---

Các bullet của **미들웨어(Middleware) 상세 (Chi tiết Middleware)** đang nén nhiều ý thành các dấu hiệu nhận biết. Hãy gom chúng thành một câu hoàn chỉnh gồm đối tượng, điều kiện và hệ quả; đó là cách biến ghi chú nguồn thành hiểu biết có thể dùng lại.

Với **미들웨어(Middleware) 상세 (Chi tiết Middleware)**, ta đã đi từ tên gọi và dấu hiệu nhận biết đến cách đặt nó trong mạch kiến thức. Hãy tự nói lại điểm chính bằng một câu có đủ đối tượng, điều kiện và giới hạn trước khi chuyển mục.

Điểm chốt của **17. 시스템 연계 및 미들웨어 (Liên kết hệ thống & Middleware)** là biết nó đứng ở đâu và có giới hạn nào trong nguồn. Bước kế tiếp là **14. 미들웨어 (Middleware)**; hãy dùng phần vừa học như tiêu chí đối chiếu, không lặp lại toàn bộ định nghĩa khi chuyển mục.