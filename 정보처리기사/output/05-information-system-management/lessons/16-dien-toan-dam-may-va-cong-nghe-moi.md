# 클라우드 컴퓨팅 및 IT 신기술 트렌드 (Điện toán đám mây, Container, IoT, Blockchain, Edge Computing & Zero Trust)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, đặc tính và phân biệt 3 mô hình dịch vụ điện toán đám mây (**IaaS, PaaS, SaaS**) cùng 4 mô hình triển khai (**Public, Private, Hybrid, Community Cloud**).
- Phân biệt sự khác nhau bản chất giữa Ảo hóa máy ảo phần cứng (**Virtual Machine - Hypervisor**) và Ảo hóa cấp hệ điều hành bằng bộ chứa (**Containerization - Docker**).
- Làm chủ các giao thức truyền thông Internet vạn vật (IoT): **MQTT** (mô hình Publish/Subscribe qua Broker trên nền TCP) và **CoAP** (mô hình RESTful trên nền UDP cho mạng băng thông hẹp).
- Thấu hiểu bản chất của công nghệ chuỗi khối **Blockchain** (sổ cái phân tán DLT, hàm băm SHA-256) và phân biệt 3 cơ chế đồng thuận cốt lõi: **PoW** (Proof of Work), **PoS** (Proof of Stake), và **PBFT** (Byzantine Fault Tolerance).
- Làm chủ kiến trúc xử lý tại biên mạng **Edge Computing** và triết lý an ninh mạng hiện đại **Zero Trust Architecture (ZTA)** theo nguyên tắc *"Never Trust, Always Verify"*.
- Nắm bắt các định nghĩa và ứng dụng thực tiễn của các công nghệ mới: **Mashup**, **Digital Twin**, **N-Screen**, **BaaS**, và công cụ **Sqoop**.

## 핵심 키워드 (Từ khóa song ngữ)
- 클라우드 서비스 모델 (Cloud SPI — IaaS 인프라, PaaS 플랫폼, SaaS 소프트웨어 서비스)
- 클라우드 배포 모델 (Deployment — 퍼블릭 Public, 프라이빗 Private, 하이브리드 Hybrid, 커뮤니티 Community)
- 도커 컨테이너 (Docker Container — OS 레벨 가상화, namespaces/cgroups, Host Kernel 공유)
- 사물인터넷 IoT 프로토콜 (MQTT Pub/Sub Broker TCP vs CoAP RESTful UDP 경량 통신)
- 블록체인 합의 알고리즘 (Consensus — PoW 작업증명 연산경쟁, PoS 지분증명, PBFT 비잔틴 내결함성)
- 엣지 컴퓨팅 (Edge Computing — 데이터 발생 지점 근처 실시간 분산 처리, 초저지연)
- 제로 트러스트 (Zero Trust Architecture — Never Trust Always Verify, 마이크로 세그멘테이션)
- 디지털 트윈 (Digital Twin — 현실 물리 객체를 가상 공간에 동일하게 복제하여 시뮬레이션)
- 매시업 (Mashup — 여러 공개 오픈 API를 결합하여 새로운 웹 서비스 창출)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi nghiên cứu kiến trúc phân tán Big Data Hadoop và CSDL NoSQL tại [15-quan-tri-co-so-du-lieu-va-big-data.md](15-quan-tri-co-so-du-lieu-va-big-data.md), việc vận hành các cụm máy chủ và ứng dụng hiện đại ngày nay đều được chuyển đổi lên hạ tầng đám mây và công nghệ container.
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị toàn bộ bức tranh xu hướng công nghệ tương lai: từ kiến trúc dịch vụ và triển khai đám mây, giải pháp đóng gói Docker, giao thức mạng IoT (MQTT, CoAP), công nghệ chuỗi khối Blockchain, điện toán biên Edge Computing cho đến triết lý bảo mật Zero Trust.
- **Dùng đi đâu (Forward Handoff):** Để viết mã các kịch bản kiểm thử bảo mật, giải mã lỗ hổng bộ nhớ và tự động hóa hệ thống trên nền tảng đám mây, quản trị viên cần nắm vững cú pháp lập trình hệ thống C tại [17-lap-trinh-c-va-cau-truc-bo-nho.md](17-lap-trinh-c-va-cau-truc-bo-nho.md) và Python tại [18-lap-trinh-python-va-tu-dong-hoa.md](18-lap-trinh-python-va-tu-dong-hoa.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Mô hình dịch vụ Đám mây (IaaS / PaaS / SaaS):**
  - Cung cấp phần cứng thô (CPU, RAM, Ổ đĩa, Mạng), người dùng tự cài HĐH $\rightarrow$ Chọn **IaaS** (AWS EC2).
  - Cung cấp sẵn HĐH, Runtime, Database, người dùng chỉ tải mã nguồn lên chạy $\rightarrow$ Chọn **PaaS** (Google App Engine).
  - Cung cấp phần mềm ứng dụng hoàn chỉnh qua web $\rightarrow$ Chọn **SaaS** (Google Docs, Microsoft 365).
- **4 Mô hình triển khai Đám mây:**
  - Nhắc đến **"여러 조직이 공통의 목적/규제를 위해 공유하는 클라우드"** $\rightarrow$ Chọn ngay **커뮤니티 클라우드 (Community Cloud)**.
- **Docker Container vs Virtual Machine (VM):**
  - VM cần cài **Guest OS riêng biệt trên mỗi máy ảo** qua Hypervisor $\rightarrow$ Nặng nề, khởi động theo phút.
  - Docker Container **chia sẻ chung nhân Kernel của Host OS** $\rightarrow$ Siêu nhẹ, khởi động theo mili-giây.
- **Giao thức IoT:**
  - Nhắc đến mô hình **Publish/Subscribe qua máy chủ Broker chạy trên nền TCP** $\rightarrow$ Chọn **MQTT**.
  - Nhắc đến giao thức dạng **RESTful chạy trên nền UDP cho thiết bị nhỏ hẹp** $\rightarrow$ Chọn **CoAP**.
- **Cơ chế đồng thuận Blockchain:**
  - Cạnh tranh tính toán giải bài toán mật mã (Mining / Nonce) $\rightarrow$ **PoW (Proof of Work)**.
  - Phân bổ quyền tạo khối dựa trên lượng tiền mã hóa đặt cọc $\rightarrow$ **PoS (Proof of Stake)**.
  - Chịu lỗi Byzantine trong mạng liên minh không cần đào $\rightarrow$ **PBFT**.
- **Zero Trust:**
  - Khẩu quyết cốt lõi: **"Never Trust, Always Verify"** (Tuyệt đối không tin tưởng, luôn luôn xác thực mọi kết nối dù ở trong mạng nội bộ).

---

## 클라우드 컴퓨팅 및 IT 신기술 트렌드

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Điện toán đám mây: Mô hình dịch vụ và Mô hình triển khai
- **개념 (Khái niệm):** Mô hình điện toán cho phép người dùng truy cập theo nhu cầu (On-Demand) vào một nhóm tài nguyên máy tính dùng chung (mạng, máy chủ, lưu trữ, ứng dụng, dịch vụ) có thể cấp phát nhanh chóng qua Internet mà không cần tốn chi phí đầu tư hạ tầng phần cứng ban đầu.
- **3 mô hình dịch vụ đám mây kinh điển (SPI Model):**

| Mô hình dịch vụ | Tên tiếng Hàn & Anh | Phạm vi nhà cung cấp quản lý | Phạm vi người dùng quản lý | Ví dụ điển hình |
| :--- | :--- | :--- | :--- | :--- |
| **Hạ tầng như dịch vụ** | **IaaS (Infrastructure as a Service)** | Phần cứng máy chủ vật lý, ảo hóa (Hypervisor), hệ thống lưu trữ, dây cáp mạng và điện nguồn. | Tự cài đặt và quản trị **Hệ điều hành (OS), Runtime, Middleware, Dữ liệu và Ứng dụng**. | AWS EC2, Google Compute Engine (GCE), Microsoft Azure VM. |
| **Nền tảng như dịch vụ** | **PaaS (Platform as a Service)** | Quản lý toàn bộ phần cứng, mạng, **Hệ điều hành, Runtime, Web Server và Hệ quản trị CSDL**. | Người dùng chỉ tập trung phát triển và tải lên **Mã nguồn ứng dụng (Code) và Dữ liệu nghiệp vụ**. | Google App Engine, Heroku, AWS Elastic Beanstalk. |
| **Phần mềm như dịch vụ** | **SaaS (Software as a Service)** | Nhà cung cấp vận hành và bảo trì **toàn bộ 100% hệ thống** từ hạ tầng cho tới phần mềm ứng dụng cuối cùng. | Người dùng **chỉ việc sử dụng chức năng và cấu hình tài khoản** qua giao diện trình duyệt web. | Google Workspace, Microsoft 365, Salesforce CRM, Dropbox. |

- **4 mô hình triển khai đám mây (Deployment Models):**
  - **퍼블릭 클라우드 (Public Cloud - Đám mây công cộng):** Hạ tầng của nhà cung cấp lớn chia sẻ chung cho nhiều tổ chức, người dùng đa thuê bao (Multi-tenant) qua Internet.
  - **프라이빗 클라우드 (Private Cloud - Đám mây riêng tư):** Hạ tầng dành riêng cho một tổ chức hoặc cơ quan chính phủ độc quyền sử dụng, an toàn dữ liệu tuyệt đối.
  - **하이브리드 클라우드 (Hybrid Cloud - Đám mây lai):** Kết hợp linh hoạt giữa Public Cloud (cho các dịch vụ tải cao biến động) và Private Cloud (cho cơ sở dữ liệu tối mật).
  - **커뮤니티 클라우드 (Community Cloud - Đám mây cộng đồng):** Hạ tầng đám mây được chia sẻ và sử dụng chung bởi nhiều tổ chức có cùng mục đích hoạt động, chính sách an ninh hoặc sứ mệnh nghiệp vụ (ví dụ: liên minh các ngân hàng tài chính, nhóm trường đại học).

#### 2. Công nghệ ảo hóa Container (Docker) vs Máy ảo (Virtual Machine)

| Tiêu chí so sánh | Máy ảo truyền thống (Virtual Machine - Hypervisor) | Bộ chứa ứng dụng (Docker Container) |
| :--- | :--- | :--- |
| **Cơ chế trừu tượng** | Ảo hóa ở **cấp độ phần cứng (Hardware Virtualization)**; Hypervisor mô phỏng toàn bộ CPU, RAM, Disk. | Ảo hóa ở **cấp độ hệ điều hành (OS-Level Virtualization)**; sử dụng tính năng `namespaces` và `cgroups` của Linux. |
| **Hệ điều hành** | Mỗi máy ảo bắt buộc phải có một **Hệ điều hành khách (Guest OS)** hoàn chỉnh riêng biệt. | Các container **chia sẻ chung nhân hệ điều hành của máy chủ (Host OS Kernel)**; không có Guest OS. |
| **Dung lượng & Khởi động** | Dung lượng tệp ảnh lớn (hàng Gigabyte); thời gian khởi động lâu (tính bằng phút). | Tệp ảnh container siêu nhỏ (hàng Megabyte); **thời gian khởi động tức thì (tính bằng mili-giây)**. |
| **Hiệu năng & Tiêu hao** | Tiêu tốn nhiều tài nguyên CPU/RAM cho việc duy trì nhiều Guest OS; mật độ máy ảo thấp. | Tiêu hao tài nguyên gần như tương đương tiến trình gốc; mật độ container trên 1 máy chủ cao gấp hàng chục lần. |

#### 3. Giao thức truyền thông Internet vạn vật (IoT Protocols)
Các thiết bị cảm biến IoT có dung lượng pin hạn chế và đường truyền băng thông hẹp đòi hỏi các giao thức chuyên biệt:
- **MQTT (Message Queuing Telemetry Transport):**
  - Hoạt động theo mô hình **Xuất bản / Đăng ký (Publish / Subscribe)** thông qua một máy chủ trung tâm gọi là **Broker**.
  - Chạy trên nền tảng giao vận **TCP** đảm bảo độ tin cậy; tiêu đề gói tin siêu nhẹ (chỉ từ 2 Byte); hỗ trợ 3 cấp độ chất lượng dịch vụ QoS (0, 1, 2); rất thích hợp cho mạng cảm biến giám sát từ xa.
- **CoAP (Constrained Application Protocol):**
  - Hoạt động theo mô hình yêu cầu/phản hồi **RESTful** (sử dụng các phương thức GET, POST, PUT, DELETE giống HTTP).
  - Chạy trên nền tảng giao vận **UDP** để loại bỏ độ trễ bắt tay 3 bước của TCP; tiêu đề ngắn gọn chỉ 4 Byte; được thiết kế tối ưu cho các vi điều khiển nhúng trong mạng cảm biến không dây có độ trễ cao.

#### 4. Công nghệ chuỗi khối (Blockchain) và Cơ chế đồng thuận
- **Bản chất kỹ thuật:** Là công nghệ sổ cái phân tán (**Distributed Ledger Technology - DLT**), nơi các giao dịch được gom thành các khối (Block) kết nối với nhau thành chuỗi tuyến tính bất biến bằng hàm băm mật mã học (**SHA-256**). Mọi nút mạng đều lưu trữ một bản sao sổ cái, không thể giả mạo dữ liệu quá khứ.
- **3 cơ chế đồng thuận phân tán tiêu biểu (Consensus Mechanisms):**
  1. **PoW (Proof of Work - Bằng chứng công việc):** Các nút mạng (thợ đào) cạnh tranh nhau giải bài toán hàm băm phức tạp để tìm giá trị Nonce hợp lệ; nút nào tìm ra trước sẽ được quyền đóng khối mới và nhận phần thưởng; an toàn cực cao nhưng tiêu tốn năng lượng điện khổng lồ (Bitcoin).
  2. **PoS (Proof of Stake - Bằng chứng cổ phần):** Quyền xác thực và tạo khối mới được phân bổ tỷ lệ thuận theo số lượng tiền mã hóa (cổ phần / Stake) mà nút mạng đang khóa ký quỹ; loại bỏ hoàn toàn việc lãng phí điện năng đào coin, tốc độ giao dịch nhanh hơn.
  3. **PBFT (Practical Byzantine Fault Tolerance):** Thuật toán giải quyết bài toán các vị tướng Byzantine trong mạng phân tán; bảo đảm tính đồng thuận và chịu lỗi được khi có tối đa $f$ nút gian lận với tổng số nút $N \ge 3f + 1$; không cần cạnh tranh tính toán, độ trễ giao dịch cực thấp, phù hợp mạng Blockchain doanh nghiệp (Hyperledger).

#### 5. Điện toán biên (Edge Computing) và Kiến trúc Zero Trust (ZTA)
- **Edge Computing (엣지 컴퓨팅):**
  - **Bản chất:** Chuyển dịch năng lực tính toán, lưu trữ và phân tích dữ liệu từ các trung tâm dữ liệu đám mây về **ngay tại rìa mạng (gần các cảm biến, thiết bị thu thập dữ liệu)**.
  - **Lợi ích:** Mang lại độ trễ cực thấp (Ultra-Low Latency), giảm tải áp lực băng thông đường truyền về đám mây, bảo đảm dịch vụ vẫn hoạt động liên tục ngay cả khi mất kết nối Internet (xe tự hành, robot phẫu thuật y tế, tự động hóa nhà máy thông minh).
- **Zero Trust Architecture (ZTA - 제로 트러스트 아키텍처):**
  - **Triết lý cốt lõi:** *"Never Trust, Always Verify"* (Không bao giờ tin tưởng, luôn luôn xác thực).
  - Không mặc định tin cậy bất kỳ người dùng hay thiết bị nào, bất kể họ đang kết nối từ mạng Internet công cộng hay đang cắm dây mạng bên trong văn phòng nội bộ.
  - Mọi yêu cầu truy cập tài nguyên đều phải trải qua quy trình xác thực định danh nghiêm ngặt, phân quyền động dựa trên ngữ cảnh và mã hóa đầu cuối (End-to-End Encryption) kết hợp kỹ thuật vi phân vùng mạng (**Micro-segmentation**).

#### 6. Bảng thuật ngữ các xu hướng công nghệ mới trong đề thi

| Thuật ngữ (KR / EN) | Định nghĩa kỹ thuật & Bản chất cơ chế | Ứng dụng thực tiễn điển hình |
| :--- | :--- | :--- |
| **매시업 (Mashup)** | Kỹ thuật lai ghép và kết hợp nội dung từ **hai hoặc nhiều giao diện lập trình mở (Open API)** khác nhau trên web để tạo ra một dịch vụ hoàn toàn mới. | Ứng dụng tìm nhà trọ kết hợp API bản đồ Google Maps với API dữ liệu giá đất thời gian thực. |
| **디지털 트윈 (Digital Twin)** | **Bản sao ảo hóa số** của một đối tượng vật lý, máy móc, hoặc quy trình trong thế giới thực, được cập nhật dữ liệu liên tục từ cảm biến IoT để mô phỏng và dự đoán. | Giám sát tình trạng vận hành của động cơ máy bay, dự báo bảo trì tua-bin điện gió trong Smart Factory. |
| **앤 스크린 (N-Screen)** | Dịch vụ chia sẻ và đồng bộ nội dung đa phương tiện liền mạch trên **nhiều loại thiết bị màn hình khác nhau** (Smart TV, PC, Smartphone, Tablet). | Người dùng xem dở bộ phim trên điện thoại di động khi đi xe buýt, về nhà bật TV tiếp tục xem đúng đoạn đó. |
| **BaaS (Blockchain as a Service)** | Dịch vụ đám mây cho phép doanh nghiệp xây dựng, lưu trữ và vận hành các ứng dụng chuỗi khối (**DApp**) mà không cần tự đầu tư xây dựng hạ tầng nút mạng Node. | Triển khai nhanh chóng giải pháp Hợp đồng thông minh (Smart Contract) trong truy xuất nguồn gốc nông sản và chuỗi cung ứng. |
| **스쿱 (Sqoop)** | Công cụ dòng lệnh chuyên dụng được thiết kế để truyền tải dữ liệu hai chiều hiệu quả giữa **Cơ sở dữ liệu quan hệ truyền thống (RDBMS)** và **Hệ thống phân tán Hadoop HDFS**. | Xuất các bảng giao dịch từ Oracle/MySQL sang Hadoop HDFS để phục vụ phân tích dữ liệu lớn. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### So sánh trực quan giao thức IoT: MQTT vs CoAP

| Đặc tính so sánh | Giao thức MQTT | Giao thức CoAP |
| :--- | :--- | :--- |
| **Giao thức tầng giao vận** | **TCP** (Hướng kết nối, tin cậy) | **UDP** (Phi kết nối, tốc độ nhanh) |
| **Mô hình kiến trúc** | **Publish / Subscribe** qua Broker trung tâm | **Request / Response** (RESTful kiểu Client/Server) |
| **Kích thước tiêu đề** | Cố định chỉ **2 Byte** | Cố định chỉ **4 Byte** |
| **Đặc điểm liên lạc** | Nhiều-nhiều (Many-to-Many), phụ thuộc Broker | Một-một (1:1), giao tiếp trực tiếp ngang hàng |
| **Trường hợp tối ưu** | Thu thập dữ liệu cảm biến liên tục đẩy về máy chủ | Thiết bị ngủ sâu đánh thức, gửi truy vấn nhẹ nhanh |

---

### 복습 체크리스트
- [ ] Phân biệt 3 mô hình dịch vụ đám mây: IaaS (thuê phần cứng), PaaS (thuê nền tảng/runtime), SaaS (thuê ứng dụng hoàn chỉnh).
- [ ] Phân biệt 4 mô hình triển khai đám mây: Public, Private, Hybrid, Community Cloud (dùng chung cho các tổ chức có cùng mục đích).
- [ ] Nắm vững ưu thế của Docker Container so với VM: Chia sẻ chung Host OS Kernel, không cần Guest OS, siêu nhẹ, khởi động mili-giây.
- [ ] Phân biệt 2 giao thức IoT: MQTT (Pub/Sub qua Broker trên nền TCP) vs CoAP (RESTful trên nền UDP).
- [ ] Nắm vững cơ chế đồng thuận Blockchain: PoW (tính toán Nonce đào coin), PoS (cổ phần ký quỹ), PBFT (chịu lỗi Byzantine cho liên minh).
- [ ] Định nghĩa được Edge Computing: Xử lý dữ liệu ngay tại rìa mạng gần thiết bị để đạt độ trễ siêu thấp.
- [ ] Khắc ghi triết lý Zero Trust: "Never Trust, Always Verify", không mặc định tin cậy bất kỳ kết nối nào.
- [ ] Nhớ các khái niệm: Digital Twin (bản sao số hóa), Mashup (ghép nhiều Open API), Sqoop (RDBMS $\leftrightarrow$ Hadoop).
