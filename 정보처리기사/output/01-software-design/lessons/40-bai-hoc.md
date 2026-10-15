# 14. 미들웨어 (Middleware)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, vị trí kiến trúc và vai trò của Phần mềm trung gian (`미들웨어 - Middleware`) trong môi trường điện toán phân tán không đồng nhất.
- Thuộc nằm lòng 6 chủng loại Middleware tiêu biểu: `DB Middleware`, `RPC`, `MOM`, `TP-Monitor`, `ORB`, và `WAS`.
- Nhận diện chính xác cơ chế hoạt động bất đồng bộ của MOM và cơ chế giám sát giao dịch ACID phân tán của TP-Monitor.

## 핵심 키워드 (Từ khóa)
- 미들웨어 (Phần mềm trung gian / Middleware / OS와 응용 프로그램 사이)
- 위치 투명성 (Tính trong suốt vị trí / Location Transparency)
- DB 미들웨어 (ODBC / JDBC)
- RPC (Remote Procedure Call / 원격 프로시저 호출)
- MOM (Message-Oriented Middleware / 비동기 메시지 / Message Queue)
- TP-Monitor (Transaction Processing Monitor / 트랜잭션 감시)
- ORB (Object Request Broker / CORBA 표준)
- WAS (Web Application Server / 동적 콘텐츠)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([13. 시스템 연계 및 인터페이스](39-bai-hoc.md)):** Sau khi xem xét các mô hình tích hợp EAI/ESB, bài này đi sâu vào hạ tầng phần mềm trung gian cụ thể làm xương sống cho việc truyền tin.
- **Tiếp nối sang bài sau ([4. 관계형 데이터베이스 구조](41-bai-hoc.md)):** Khởi đầu Cụm kiến thức thiết kế cơ sở dữ liệu quan hệ (Cấu trúc bảng, Khóa, Ràng buộc toàn vẹn).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ 6 loại Middleware và các từ khóa nhận diện: RPC là gọi hàm từ xa; MOM là thông điệp bất đồng bộ; TP-Monitor là giám sát giao dịch tải lớn; WAS là ứng dụng web động.
- Đọc TẦNG B để phân biệt cơ chế truyền đồng bộ (Synchronous của RPC) và cơ chế truyền bất đồng bộ (Asynchronous qua Queue của MOM).

---

## 14. 미들웨어 (Middleware)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Middleware):**
  - Là phần mềm nằm ở giữa **Hệ điều hành (`OS`)** và **Ứng dụng nghiệp vụ (`응용 프로그램`)**, cung cấp các dịch vụ chuẩn hóa nhằm kết nối và trao đổi dữ liệu giữa các phần cứng, hệ điều hành và mạng máy tính khác nhau trong môi trường điện toán phân tán.
  - **Đặc trưng kỹ thuật quan trọng nhất:** Cung cấp **Tính trong suốt về vị trí (`위치 투명성 - Location Transparency`)**, giúp ứng dụng gọi dịch vụ mà không cần biết máy chủ dịch vụ đang nằm ở địa chỉ IP hay máy trạm nào.
- **6 chủng loại Middleware tiêu biểu (Bắt buộc phải thuộc):**
  1. **DB 미들웨어 (Database Middleware):**
     - Cung cấp kết nối tiêu chuẩn hóa giữa ứng dụng phía Client và hệ quản trị cơ sở dữ liệu (DBMS).
     - Tiêu biểu: `ODBC (Open Database Connectivity - chuẩn Microsoft)`, `JDBC (Java Database Connectivity)`.
  2. **RPC (Remote Procedure Call - Gọi thủ tục từ xa):**
     - Cho phép ứng dụng client gọi thực thi một hàm/thủ tục (`프로시저`) nằm trên một máy chủ từ xa qua mạng giống hệt như đang gọi một hàm cục bộ trên chính máy mình.
  3. **MOM (Message-Oriented Middleware - Phần mềm trung gian hướng thông điệp):**
     - Cơ chế truyền thông điệp **Bất đồng bộ (`비동기식 메시지 전달`)** thông qua hàng đợi thông điệp (Message Queue).
     - *Ưu điểm:* Client gửi thông điệp vào Queue rồi tiếp tục làm việc khác ngay mà không cần chờ Server phản hồi; đảm bảo thông điệp không bị mất khi Server đích tạm thời quá tải hoặc mất mạng.
     - Tiêu biểu: RabbitMQ, Apache Kafka, IBM MQ.
  4. **TP-Monitor (Transaction Processing Monitor - Bộ giám sát xử lý giao dịch):**
     - Chuyên trách quản lý, phân phối tải và giám sát các giao dịch (`트랜잭션`) có khối lượng lớn trong môi trường phân tán (ngân hàng, hàng không), đảm bảo tính toàn vẹn dữ liệu chuẩn ACID và khả năng chịu lỗi cao.
     - Tiêu biểu: Tuxedo, TOP END.
  5. **ORB (Object Request Broker - Bộ môi giới yêu cầu đối tượng):**
     - Cho phép các đối tượng phần mềm viết bằng các ngôn ngữ khác nhau trên các nền tảng khác nhau có thể gửi thông điệp và gọi phương thức của nhau theo tiêu chuẩn **CORBA (Common Object Request Broker Architecture)**.
  6. **WAS (Web Application Server - Máy chủ ứng dụng web):**
     - Phần mềm trung gian chạy logic nghiệp vụ web động, kết nối giữa Web Server tĩnh và Cơ sở dữ liệu.
     - Tiêu biểu: Tomcat, WebLogic, JEUS, JBoss.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Middleware nào hỗ trợ truyền thông điệp bất đồng bộ (비동기식) qua Message Queue?"* -> **MOM (Message-Oriented Middleware)**.
  - **Bẫy 2:** *"Middleware nào quản lý và đảm bảo tính toàn vẹn giao dịch khối lượng lớn trong ngân hàng?"* -> **TP-Monitor**.
  - **Bẫy 3:** *"Tiêu chuẩn CORBA gắn liền với loại Middleware nào?"* -> **ORB (Object Request Broker)**.
  - **Bẫy 4:** *"Middleware nằm ở đâu trong kiến trúc máy tính?"* -> **Nằm giữa Hệ điều hành (OS) và Ứng dụng (응용 프로그램)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Middleware nằm giữa OS và App có tính trong suốt vị trí; DB nối CSDL, RPC gọi hàm từ xa, MOM hàng đợi bất đồng bộ, TP-Monitor canh giao dịch, ORB theo chuẩn CORBA, WAS web động".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **So sánh cơ chế hoạt động RPC vs MOM:**
  - **RPC (Gọi thủ tục đồng bộ):** Client gọi hàm `calculate()` trên server từ xa $\rightarrow$ Client bị đóng băng (Block/Wait) cho đến khi server tính xong và trả về kết quả. Nếu server chết hoặc rớt mạng giữa chừng, client bị lỗi timeout ngay lập tức.
  - **MOM (Hướng thông điệp bất đồng bộ):** Client ném gói tin `OrderCreated` vào Queue của RabbitMQ $\rightarrow$ Client tiếp tục phục vụ người dùng khác ngay lập tức (Non-blocking). Phía sau có 10 worker server cùng rút message từ Queue ra để xử lý dần dần. Kể cả khi toàn bộ worker chết hết, tin nhắn vẫn nằm an toàn trên đĩa của hàng đợi, không bao giờ bị mất đơn hàng.

### 복습 체크리스트
- [ ] Định nghĩa được vị trí và vai trò của Middleware cùng đặc tính 위치 투명성.
- [ ] Phân biệt được 6 loại Middleware: DB, RPC, MOM, TP-Monitor, ORB, WAS.
- [ ] Nhớ MOM hoạt động theo cơ chế bất đồng bộ (비동기식) dùng Message Queue.
- [ ] Nhớ TP-Monitor chuyên giám sát giao dịch lớn đảm bảo ACID.
- [ ] Nhớ ORB gắn liền với tiêu chuẩn đối tượng phân tán CORBA.
