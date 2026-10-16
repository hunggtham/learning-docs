# 인터페이스 설계, 미들웨어 및 연계 기술 (Thiết kế Giao diện, Middleware và Kỹ thuật Liên kết Hệ thống)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình và các nguyên tắc kỹ thuật trong thẩm định giao diện hệ thống (`정형 기술 검토 - FTR`).
- Làm chủ kỹ thuật tích hợp ứng dụng doanh nghiệp `EAI (Enterprise Application Integration)`: phân tích ưu nhược điểm của 4 topo kết nối (`Point-to-Point, Hub & Spoke, Message Bus, Hybrid`) và nguy cơ điểm lỗi đơn (`SPOF`).
- Phân biệt rõ sự khác nhau về kiến trúc và phạm vi giữa `EAI` và Trục dịch vụ doanh nghiệp `ESB (Enterprise Service Bus)`.
- Nắm vững các công nghệ truyền thông và định dạng dữ liệu web hiện đại: `JSON, XML, AJAX, REST API` cùng bộ ba Web Services truyền thống (`SOAP, WSDL, UDDI`).
- Phân loại chuẩn xác 6 loại phần mềm trung gian (`미들웨어 - Middleware`): `RPC, MOM, TP-Monitor, ORB, WAS`, và `DB 미들웨어 (ODBC/JDBC)`.

## 핵심 키워드 (Từ khóa)
- FTR (Formal Technical Review / 정형 기술 검토 / 제품 검토, 2시간 제한)
- EAI 4대 토폴로지 (Point-to-Point, Hub & Spoke - SPOF, Message Bus, Hybrid)
- ESB (Enterprise Service Bus / SOA 기반 / 느슨한 결합 / 서비스 중심)
- JSON vs XML (Key-Value 경량 포맷 vs 트리 구조 태그 기반)
- AJAX (Asynchronous JavaScript and XML / 비동기 통신 / 부분 새로고침)
- 웹 서비스 3대 표준 (SOAP - 통신 프로토콜, WSDL - 기술 언어, UDDI - 등록 저장소)
- 미들웨어 (Middleware / OS와 응용 프로그램 사이 / 위치 투명성 제공)
- RPC vs MOM (원격 프로시저 호출 - 동기 vs 메시지 지향 미들웨어 - 비동기 큐)
- TP-Monitor vs WAS (트랜잭션 감시자 vs 웹 애플리케이션 서버)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Tiếp nối từ các bài thiết kế module [08-thiet-ke-module-coupling-cohesion.md](08-thiet-ke-module-coupling-cohesion.md) và mẫu thiết kế [09-design-patterns-gof.md](09-design-patterns-gof.md), một hệ thống thông tin thực tế không bao giờ đứng độc lập một mình mà luôn phải trao đổi dữ liệu với các hệ thống ngân hàng, cổng thanh toán, cơ quan thuế và các đối tác bên ngoài.
- **Đang giải quyết gì (Current Problem):** Bài học này thuộc trọng tâm của **Chương 4: 인터페이스 설계 (Thiết kế giao diện liên kết)** trong chuẩn đề thi 정보처리기사, giải quyết bài toán làm thế nào để kết nối các hệ thống không đồng nhất (khác hệ điều hành, khác ngôn ngữ lập trình, khác cơ sở dữ liệu) một cách bảo mật, tin cậy và không bị nghẽn cổ chai.
- **Dùng đi đâu (Forward Handoff):** Hoàn tất toàn bộ 4 chương cốt lõi của Môn 1 (소프트웨어 설계). Đối với các bài toán liên kết hệ thống đòi hỏi lưu trữ dữ liệu bền vững và bảo đảm tính toàn vẹn giao dịch phức tạp, kiến thức sẽ mở rộng sang chuyên đề củng cố [11-co-so-du-lieu-va-quan-ly-giao-dich.md](11-co-so-du-lieu-va-quan-ly-giao-dich.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng bảng ma trận 4 topo EAI và nhận diện nguy cơ SPOF của Hub & Spoke; phân biệt bộ ba SOAP - WSDL - UDDI; và đặc trưng kỹ thuật của 6 loại Middleware (RPC gọi hàm từ xa, MOM hàng đợi bất đồng bộ, TP-Monitor quản lý giao dịch lớn, WAS máy chủ chạy ứng dụng web).
- Đọc TẦNG B để phân biệt kiến trúc Loosely-coupled của ESB so với EAI truyền thống, và cơ chế hoạt động bất đồng bộ của AJAX không tải lại trang.

---

## 인터페이스 설계, 미들웨어 및 연계 기술

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Thẩm định Giao diện: Kỹ thuật FTR (Formal Technical Review)
- **Định nghĩa:** Là quy trình đánh giá kỹ thuật chính thức nhằm phát hiện lỗi giao diện và sai lệch yêu cầu ngay từ giai đoạn thiết kế.
- **Các nguyên tắc vàng của FTR trong đề thi:**
  1. `제품 검토에 집중 (Tập trung đánh giá sản phẩm)`: Chỉ đánh giá tài liệu đặc tả và thiết kế giao diện, tuyệt đối **không đánh giá hay chỉ trích tác giả (người tạo ra sản phẩm)**.
  2. `사전 검토 및 준비 (Chuẩn bị tài liệu trước)`: Tài liệu phải được gửi cho các thành viên nghiên cứu trước cuộc họp.
  3. `시간 제한 (Giới hạn thời gian)`: Cuộc họp thẩm tra duy trì tập trung cao độ, **thường giới hạn tối đa 2 giờ**.
  4. `해결책 논쟁 지양 (Hạn chế tranh cãi tìm giải pháp tại chỗ)`: Buổi họp tập trung vào việc **phát hiện và ghi nhận lỗi (Defect Identification)**, việc tìm giải pháp khắc phục sẽ do tác giả thực hiện sau buổi họp.
  5. `공식 기록 유지 (Duy trì biên bản chính thức)`: Ghi lại đầy đủ các lỗi phát hiện và ký biên bản nghiệm thu.

---

#### 2. Kỹ thuật Tích hợp Ứng dụng Doanh nghiệp: EAI vs ESB

##### A. 4 Mô hình Topo liên kết của EAI (Enterprise Application Integration)
EAI là giải pháp phần mềm kết nối và đồng bộ hóa các hệ thống nghiệp vụ không đồng nhất (Kế toán, Bán hàng, Kho bãi, ERP, CRM) trong một doanh nghiệp.

| Topo kết nối EAI | Ký hiệu & Cấu trúc liên kết | Bản chất kỹ thuật & Ưu nhược điểm đề thi |
|:---|:---:|:---|
| **Point-to-Point<br>(Điểm - Điểm)** | `A ── B`<br>`│ ╲ ╱ │`<br>`C ── D` | • Các ứng dụng **kết nối trực tiếp 1-1** với nhau.<br>• Đơn giản khi có ít hệ thống.<br>• Khi số hệ thống $N$ tăng, số liên kết tăng vọt theo công thức: $\frac{N(N-1)}{2}$. Cực kỳ khó quản lý, chi phí bảo trì khổng lồ. |
| **Hub & Spoke<br>(Trục bánh xe)** | `A ── Hub ── B`<br>`      │`<br>`      C` | • Tất cả ứng dụng kết nối tập trung qua một **bộ điều phối trung tâm (Hub)**.<br>• Giảm số lượng đường truyền xuống còn $N$. Dễ mở rộng.<br>• **BẪY TỬ HUYỆT:** **Nguy cơ điểm lỗi đơn (SPOF - Single Point of Failure)**. Nếu Hub bị tê liệt hoặc quá tải, toàn bộ liên lạc của doanh nghiệp ngừng trệ hoàn toàn. |
| **Message Bus<br>(Trục thông điệp)** | `A    B    C`<br>`│    │    │`<br>`════ Bus ════` | • Các ứng dụng kết nối vào một **trục bus phần mềm trung gian chung** thông qua các Adapter.<br>• Truyền thông điệp bất đồng bộ (Asynchronous). Khả năng mở rộng tuyệt vời, tính độc lập cao, giảm tải tắc nghẽn. |
| **Hybrid<br>(Mô hình lai)** | `Hub ══ Bus ══ Hub`<br>` │              │`<br>`A, B           C, D` | • **Kết hợp giữa Hub & Spoke và Message Bus**.<br>• Nội bộ từng phòng ban dùng Hub & Spoke; các Hub lớn toàn công ty kết nối với nhau qua Message Bus. Tối ưu hóa hiệu năng và quản trị phân cấp. |

##### B. Phân biệt EAI vs ESB (Enterprise Service Bus)
- **EAI (Enterprise Application Integration):**
  - Tiếp cận tập trung, thường phụ thuộc chặt chẽ vào giải pháp của một nhà cung cấp phần mềm duy nhất (Vendor-dependent).
  - Tích hợp theo hướng ứng dụng với ứng dụng (Application-to-Application).
- **ESB (Enterprise Service Bus):**
  - Dựa trên **Kiến trúc hướng dịch vụ (SOA - Service-Oriented Architecture)**.
  - Các hệ thống giao tiếp với nhau dưới dạng các **Dịch vụ độc lập (Services)** thông qua các chuẩn Web mở (XML, JSON, SOAP, REST).
  - Thúc đẩy tính chất **Liên kết lỏng lẻo (Loosely Coupled)** tối đa giữa các hệ thống; hỗ trợ định tuyến thông minh (Intelligent Routing) và chuyển đổi giao thức tự động (Protocol Transformation).

---

#### 3. Định dạng dữ liệu và Giao thức truyền thông hiện đại

##### A. So sánh định dạng dữ liệu: JSON vs XML

| Tiêu chí so sánh | JSON (JavaScript Object Notation) | XML (eXtensible Markup Language) |
|:---|:---|:---|
| **Cấu trúc dữ liệu** | Dạng cặp **Khóa - Giá trị (`Key : Value`)** và Mảng | Cấu trúc phân cấp hình cây dựa trên **các thẻ mở/đóng (`<tag>...</tag>`)** |
| **Kích thước & Băng thông** | **Rất nhẹ (Lightweight)**, ít tốn băng thông truyền tải | Nặng và cồng kềnh do phải lặp lại các thẻ đóng mở |
| **Tốc độ xử lý** | **Rất nhanh**, JavaScript đọc trực tiếp thành Object | Chậm hơn, phải sử dụng bộ phân tích cú pháp (DOM, SAX Parser) |
| **Khả năng kiểm tra** | Kiểm tra cơ bản qua JSON Schema | Rất chặt chẽ nhờ DTD, XML Schema (XSD), hỗ trợ Namespace |
| **Phạm vi sử dụng** | Web hiện đại, Mobile Apps, RESTful API | Doanh nghiệp lớn, ngân hàng, giao thức SOAP, hồ sơ phức tạp |

##### B. Kỹ thuật AJAX (Asynchronous JavaScript and XML)
- **Bản chất kỹ thuật:** Là kỹ thuật cho phép trang web trao đổi dữ liệu với máy chủ **bất đồng bộ (Asynchronous)** trong nền.
- **Đặc trưng cốt lõi đề thi:** Trình duyệt có thể gửi và nhận dữ liệu từ server mà **KHÔNG CẦN PHẢI TẢI LẠI TOÀN BỘ TRANG WEB (No Full Page Reload)**, chỉ cập nhật cục bộ một vùng nội dung cần thiết (ví dụ: Gõ tìm kiếm hiện gợi ý tức thì trên Google).
- Sử dụng đối tượng `XMLHttpRequest` hoặc hàm `fetch()` trong JavaScript.

##### C. Bộ ba Tiêu chuẩn Web Services truyền thống

| Tiêu chuẩn | Tên đầy đủ & Ý nghĩa kỹ thuật | Vai trò nhận diện đề thi |
|:---|:---|:---|
| **SOAP** | `Simple Object Access Protocol`<br>(Giao thức truy cập đối tượng đơn giản) | **Giao thức truyền thông điệp** dựa trên XML thông qua các giao thức mạng phổ thông như HTTP, HTTPS, SMTP. Đảm bảo an toàn và giao dịch tin cậy. |
| **WSDL** | `Web Services Description Language`<br>(Ngôn ngữ mô tả dịch vụ web) | **Tài liệu định dạng XML mô tả chi tiết giao diện dịch vụ**: Dịch vụ cung cấp những hàm gì, tham số đầu vào là gì, kiểu dữ liệu trả về và địa chỉ mạng (Endpoint URL) ở đâu. |
| **UDDI** | `Universal Description, Discovery, and Integration`<br>(Hệ thống đăng ký và khám phá toàn cầu) | **Danh bạ đăng ký dịch vụ (Registry)**, đóng vai trò như cuốn niên giám điện thoại trực tuyến, cho phép các doanh nghiệp đăng ký dịch vụ của mình và tìm kiếm dịch vụ của đối tác. |

---

#### 4. Phân loại 6 dạng Phần mềm trung gian (Middleware)
- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [Hàn/Anh]: `미들웨어(Middleware)는 운영체제(OS)와 응용 프로그램 사이에서 서로 다른 기종의 하드웨어나 소프트웨어를 연결하여, 분산 컴퓨팅 환경에서 투명한(Transparent) 통신을 지원하는 소프트웨어이다.`
  - [Tiếng Việt]: Middleware là lớp phần mềm trung gian nằm giữa Hệ điều hành và Ứng dụng người dùng, che giấu sự khác biệt về phần cứng, mạng và hệ điều hành, cung cấp tính trong suốt vị trí (`위치 투명성 - Location Transparency`) để các ứng dụng phân tán giao tiếp trơn tru với nhau.

- **Chi tiết 6 loại Middleware kinh điển:**
  1. `RPC (Remote Procedure Call — Gọi thủ tục từ xa)`: Cho phép một chương trình gọi thực thi một hàm/thủ tục nằm trên một máy tính từ xa trong mạng như thể đang gọi một hàm cục bộ trong cùng tiến trình (giao tiếp đồng bộ).
  2. `MOM (Message-Oriented Middleware — Middleware hướng thông điệp)`:
     - Cơ chế truyền thông điệp **bất đồng bộ (Asynchronous)** thông qua hàng đợi thông điệp (`메시지 큐 - Message Queue`).
     - Người gửi gửi thông điệp vào hàng đợi và tiếp tục công việc; người nhận lấy thông điệp ra xử lý khi sẵn sàng. Hai bên không cần online cùng lúc (ví dụ: RabbitMQ, Apache Kafka).
  3. `TP-Monitor (Transaction Processing Monitor — Bộ giám sát xử lý giao dịch)`:
     - Chuyên trách theo dõi, quản trị và phân bổ tài nguyên cho các giao dịch phân tán quy mô lớn (Online Transaction Processing - OLTP).
     - Đảm bảo trọn vẹn 4 đặc tính **ACID** của giao dịch trong các hệ thống ngân hàng, đặt vé máy bay hàng triệu giao dịch/giây.
  4. `ORB (Object Request Broker — Môi giới yêu cầu đối tượng)`:
     - Thành phần cốt lõi trong kiến trúc CORBA, cho phép các đối tượng phần mềm được viết bằng các ngôn ngữ lập trình khác nhau (C++, Java) chạy trên các hệ điều hành khác nhau có thể tự do gửi nhận thông điệp gọi phương thức của nhau.
  5. `WAS (Web Application Server — Máy chủ ứng dụng web)`:
     - Máy chủ trung gian chuyên quản lý và thực thi **logic nghiệp vụ (Business Logic)** của các ứng dụng web động.
     - Quản lý vòng đời tiến trình, quản lý bộ nhớ đệm (Cache), và tối ưu hóa kết nối cơ sở dữ liệu (`DB 커넥션 풀 - Connection Pooling`). Ví dụ: Apache Tomcat, Oracle WebLogic, Tmax JEUS, IBM WebSphere.
  6. `DB 미들웨어 (ODBC / JDBC)`:
     - Giao diện chuẩn hóa độc lập giúp ứng dụng kết nối và gửi câu lệnh SQL tới các hệ quản trị cơ sở dữ liệu khác nhau (Oracle, MySQL, SQL Server) mà không cần viết lại mã truy vấn.

---

#### 5. Bẫy đề thi trắc nghiệm thường gặp (주의/함정)
- **Bẫy 1 (Nguy cơ của Hub & Spoke):** Đề hỏi *"Nhược điểm lớn nhất của mô hình tích hợp EAI Hub & Spoke là gì?"* $\rightarrow$ Đáp án chắc chắn là **단일 장애점 (SPOF - Single Point of Failure)**.
- **Bẫy 2 (Bộ ba Web Services):**
  - Giao thức truyền tin $\rightarrow$ **SOAP**.
  - Ngôn ngữ mô tả dịch vụ $\rightarrow$ **WSDL**.
  - Danh bạ đăng ký và tìm kiếm $\rightarrow$ **UDDI**.
- **Bẫy 3 (RPC vs MOM):**
  - Gọi hàm từ xa đồng bộ, chờ kết quả $\rightarrow$ **RPC (Remote Procedure Call)**.
  - Giao tiếp thông điệp bất đồng bộ qua hàng đợi Message Queue $\rightarrow$ **MOM (Message-Oriented Middleware)**.
- **Bẫy 4 (AJAX):** AJAX **không phải là một ngôn ngữ lập trình hay một định dạng dữ liệu mới**; nó là một kỹ thuật kết hợp JavaScript và đối tượng `XMLHttpRequest` để trao đổi dữ liệu bất đồng bộ không cần reload trang.

- **한 문장 설명 (Câu chốt ghi nhớ):** "EAI Hub&Spoke sợ nhất SPOF, ESB hướng dịch vụ lỏng liên kết; Web Services có SOAP truyền tin, WSDL đặc tả, UDDI danh bạ; Middleware có RPC gọi hàm, MOM gửi hàng đợi, WAS trị nghiệp vụ web".

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế hoạt động bất đồng bộ của MOM (Message-Oriented Middleware)
- Trong các hệ thống thương mại điện tử lớn vào ngày hội mua sắm (Mega Sale), hàng triệu người dùng bấm nút "Đặt mua" trong cùng một giây. Nếu xử lý đồng bộ trực tiếp (RPC), máy chủ CSDL sẽ lập tức bị sập do quá tải kết nối.
- **Giải pháp MOM:**
  1. Ứng dụng Web nhận yêu cầu, đóng gói thành một thông điệp nhỏ và đẩy vào Hàng đợi thông điệp (`Message Queue`) của MOM trong vòng vài mili-giây, sau đó báo ngay cho người dùng "Đặt hàng thành công!".
  2. Hệ thống xử lý đơn hàng và trừ kho ở phía sau sẽ từ từ rút từng thông điệp trong hàng đợi ra xử lý với tốc độ ổn định mà nó chịu đựng được.
  3. Ngay cả khi hệ thống kho bị mất điện trong 30 phút, thông điệp vẫn nằm an toàn trong hàng đợi của MOM và được xử lý tuần tự khi hệ thống hoạt động trở lại mà không làm mất bất kỳ đơn hàng nào của khách.

#### 2. So sánh chuyên sâu: Web Server vs Web Application Server (WAS)
- **Web Server (Máy chủ Web thuần túy: Nginx, Apache HTTP Server):**
  - Chỉ chuyên phục vụ các **tài nguyên tĩnh (Static Contents)** như file HTML, CSS, JavaScript, hình ảnh, video.
  - Đóng vai trò làm tường lửa ngoài cùng, định tuyến tải (Reverse Proxy / Load Balancer) cho các máy chủ bên trong.
- **Web Application Server (WAS: Tomcat, WebLogic, JEUS):**
  - Chuyên xử lý các **nội dung động (Dynamic Contents)** đòi hỏi tính toán logic nghiệp vụ và truy vấn cơ sở dữ liệu.
  - Chứa máy ảo (JVM), thực thi các Servlet/JSP, quản lý phiên người dùng (Session), và quản lý vùng kết nối dữ liệu (Connection Pool) để tiết kiệm thời gian kết nối lại CSDL.

---

### 복습 체크리스트
- [ ] Nhớ 4 nguyên tắc của FTR: tập trung sản phẩm không chỉ trích người, gửi tài liệu trước, giới hạn 2 giờ, tránh tranh cãi giải pháp tại chỗ.
- [ ] Phân biệt được 4 topo EAI: Point-to-Point, Hub & Spoke, Message Bus, Hybrid.
- [ ] Nhớ nhược điểm chết người của Hub & Spoke là 단일 장애점 (SPOF - Single Point of Failure).
- [ ] Phân biệt được EAI (tập trung, gắn chặt) và ESB (kiến trúc SOA, dịch vụ liên kết lỏng lẻo).
- [ ] Nhớ ưu thế của JSON (nhẹ, dạng Key-Value) so với XML (nặng, thẻ cây phân cấp).
- [ ] Định nghĩa được bản chất của AJAX: giao tiếp bất đồng bộ, cập nhật dữ liệu mà không cần tải lại toàn bộ trang web.
- [ ] Phân biệt bộ ba Web Services: SOAP (giao thức truyền tin), WSDL (ngôn ngữ đặc tả dịch vụ), UDDI (danh bạ đăng ký dịch vụ).
- [ ] Kể tên và giải thích được chức năng của 6 loại Middleware: RPC, MOM, TP-Monitor, ORB, WAS, DB Middleware.
