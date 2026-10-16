# 클라우드 컴퓨팅 및 IT 신기술 트렌드 (Điện toán đám mây & Xu hướng công nghệ mới: Cloud IaaS/PaaS/SaaS, Docker, IoT, AI)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, đặc tính và phân biệt 3 mô hình dịch vụ điện toán đám mây kinh điển (**클라우드 서비스 모델: IaaS, PaaS, SaaS**) cùng 3 mô hình triển khai (Public, Private, Hybrid Cloud).
- Phân biệt sự khác nhau bản chất giữa Ảo hóa máy ảo phần cứng (**Virtual Machine - Hypervisor**) và Ảo hóa cấp hệ điều hành bằng bộ chứa (**Containerization - Docker**).
- Thấu hiểu kiến trúc vi dịch vụ (**MSA - Microservices Architecture**) và hạ tầng trung tâm dữ liệu định nghĩa bằng phần mềm (**SDDC: SDN, SDS, SDC**).
- Nắm bắt các định nghĩa và ứng dụng thực tiễn của các công nghệ mới nổi thường xuyên xuất hiện trong đề thi: **Mashup**, **Digital Twin**, **Edge Computing**, **N-Screen**, **BaaS** (Blockchain as a Service), và các công cụ xử lý dữ liệu lớn (**Sqoop**, **TensorFlow**).

## 핵심 키워드 (Từ khóa song ngữ)
- 클라우드 컴퓨팅 (Cloud Computing — IaaS 인프라, PaaS 플랫폼, SaaS 소프트웨어 서비스)
- 배포 모델 (Deployment Models — 퍼블릭 클라우드 Public, 프라이빗 Private, 하이브리드 Hybrid)
- 도커 (Docker — OS 레벨 가상화, 컨테이너, 호스트 커널 공유, 경량성)
- 마이크로서비스 아키텍처 (MSA — 독립 배포 가능한 소규모 서비스, REST API 연동)
- SDDC (Software-Defined Data Center — SDN 네트워크, SDS 스토리지, SDC 서버 가상화)
- 엣지 컴퓨팅 (Edge Computing — 데이터 발생 지점 근처에서 실시간 처리, 초저지연)
- 매시업 (Mashup — 여러 공개 오픈 API를 결합하여 새로운 웹 서비스 창출)
- 디지털 트윈 (Digital Twin — 현실 객체의 물리적 특성을 가상 공간에 동일하게 복제)
- 앤 스크린 (N-Screen — 여러 기기에서 콘텐츠를 끊김 없이 연속 시청하는 서비스)
- BaaS (Blockchain as a Service — 블록체인 노드 인프라 구축 없이 DApp 배포 클라우드)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi nghiên cứu kiến trúc phân tán Big Data Hadoop và CSDL NoSQL tại [15-quan-tri-co-so-du-lieu-va-big-data.md](15-quan-tri-co-so-du-lieu-va-big-data.md), việc vận hành các cụm máy chủ và ứng dụng hiện đại ngày nay đều được chuyển đổi lên hạ tầng đám mây và công nghệ container.
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị toàn bộ bức tranh xu hướng công nghệ tương lai: từ kiến trúc dịch vụ đám mây, giải pháp đóng gói Docker/Kubernetes, cho đến các khái niệm công nghệ mũi nhọn như Edge Computing, Digital Twin, Mashup và Blockchain.
- **Dùng đi đâu (Forward Handoff):** Để viết mã các kịch bản kiểm thử bảo mật, giải mã lỗ hổng bộ nhớ và tự động hóa hệ thống trên nền tảng đám mây, quản trị viên cần nắm vững cú pháp lập trình hệ thống C tại [17-lap-trinh-c-va-cau-truc-bo-nho.md](17-lap-trinh-c-va-cau-truc-bo-nho.md) và Python tại [18-lap-trinh-python-va-tu-dong-hoa.md](18-lap-trinh-python-va-tu-dong-hoa.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Mô hình dịch vụ Đám mây (IaaS / PaaS / SaaS):**
  - Cung cấp phần cứng thô (CPU, RAM, Ổ đĩa, Mạng), người dùng tự cài HĐH và môi trường $\rightarrow$ Chọn **IaaS** (ví dụ: AWS EC2).
  - Cung cấp sẵn HĐH, Runtime, Database, người dùng chỉ việc tải mã nguồn code lên chạy $\rightarrow$ Chọn **PaaS** (ví dụ: Google App Engine, Heroku).
  - Cung cấp ứng dụng phần mềm hoàn chỉnh qua trình duyệt web, người dùng chỉ việc sử dụng $\rightarrow$ Chọn **SaaS** (ví dụ: Google Docs, Microsoft 365).
- **Docker Container vs Virtual Machine (VM):**
  - VM cần cài **Guest OS riêng biệt trên mỗi máy ảo** thông qua Hypervisor $\rightarrow$ Nặng nề, khởi động theo phút.
  - Docker Container **chia sẻ chung nhân Kernel của Host OS** $\rightarrow$ Siêu nhẹ, khởi động theo mili-giây.
- **Nhận diện các thuật ngữ công nghệ mới:**
  - Kết hợp nhiều API mở tạo dịch vụ mới (Bản đồ + Giá nhà) $\rightarrow$ **Mashup (매시업)**.
  - Bản sao số hóa ảo của máy móc/nhà máy ngoài đời thực để mô phỏng, dự báo $\rightarrow$ **Digital Twin (디지털 트윈)**.
  - Xử lý dữ liệu tại rìa mạng để đạt độ trễ siêu thấp (xe tự hành, camera AI) $\rightarrow$ **Edge Computing (엣지 컴퓨팅)**.
  - Xem dở phim trên điện thoại, bật TV lên xem tiếp liền mạch đúng đoạn đó $\rightarrow$ **N-Screen (앤 스크린)**.
  - Chuyển đổi dữ liệu hai chiều giữa CSDL quan hệ RDBMS và Hadoop HDFS $\rightarrow$ **Sqoop (스쿱)**.

---

## 클라우드 컴퓨팅 및 IT 신기술 트렌드

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Điện toán đám mây và Các mô hình dịch vụ (Cloud Computing)
- **개념 (Khái niệm):** Mô hình điện toán cho phép người dùng truy cập theo nhu cầu (On-Demand) vào một nhóm tài nguyên máy tính dùng chung (mạng, máy chủ, lưu trữ, ứng dụng, dịch vụ) có thể cấp phát nhanh chóng qua Internet mà không cần tốn chi phí đầu tư hạ tầng phần cứng ban đầu.
- **3 mô hình dịch vụ đám mây kinh điển (SPI Model):**

| Mô hình dịch vụ | Tên tiếng Hàn & Anh | Phạm vi nhà cung cấp quản lý | Phạm vi người dùng quản lý | Ví dụ điển hình |
| :--- | :--- | :--- | :--- | :--- |
| **Hạ tầng như dịch vụ** | **IaaS (Infrastructure as a Service)** | Phần cứng máy chủ vật lý, ảo hóa (Hypervisor), hệ thống lưu trữ, dây cáp mạng và điện nguồn. | Tự cài đặt và quản trị **Hệ điều hành (OS), Runtime, Middleware, Dữ liệu và Ứng dụng**. | AWS EC2, Google Compute Engine (GCE), Microsoft Azure VM. |
| **Nền tảng như dịch vụ** | **PaaS (Platform as a Service)** | Quản lý toàn bộ phần cứng, mạng, **Hệ điều hành, Runtime, Web Server và Hệ quản trị CSDL**. | Người dùng chỉ tập trung phát triển và tải lên **Mã nguồn ứng dụng (Code) và Dữ liệu nghiệp vụ**. | Google App Engine, Heroku, AWS Elastic Beanstalk. |
| **Phần mềm như dịch vụ** | **SaaS (Software as a Service)** | Nhà cung cấp vận hành và bảo trì **toàn bộ 100% hệ thống** từ hạ tầng cho tới phần mềm ứng dụng cuối cùng. | Người dùng **chỉ việc sử dụng chức năng và cấu hình tài khoản** qua giao diện trình duyệt web. | Google Workspace, Microsoft 365, Salesforce CRM, Dropbox. |

- **3 mô hình triển khai đám mây (Deployment Models):**
  - **퍼블릭 클라우드 (Public Cloud - Đám mây công cộng):** Hạ tầng của nhà cung cấp lớn (AWS, Azure) chia sẻ chung cho nhiều tổ chức, người dùng đa thuê bao (Multi-tenant).
  - **프라이빗 클라우드 (Private Cloud - Đám mây riêng tư):** Hạ tầng dành riêng cho một doanh nghiệp hoặc cơ quan chính phủ độc quyền sử dụng, độ an toàn và tuân thủ cao nhất.
  - **하이브리드 클라우드 (Hybrid Cloud - Đám mây lai):** Kết hợp linh hoạt giữa Public Cloud (cho các dịch vụ tải cao biến động) và Private Cloud (cho cơ sở dữ liệu tối mật).

#### 2. Công nghệ ảo hóa Container (Docker) vs Máy ảo (Virtual Machine)

| Tiêu chí so sánh | Máy ảo truyền thống (Virtual Machine - Hypervisor) | Bộ chứa ứng dụng (Docker Container) |
| :--- | :--- | :--- |
| **Cơ chế trừu tượng** | Ảo hóa ở **cấp độ phần cứng (Hardware Virtualization)**; Hypervisor mô phỏng toàn bộ CPU, RAM, Disk. | Ảo hóa ở **cấp độ hệ điều hành (OS-Level Virtualization)**; sử dụng tính năng `namespaces` và `cgroups` của Linux. |
| **Hệ điều hành** | Mỗi máy ảo bắt buộc phải có một **Hệ điều hành khách (Guest OS)** hoàn chỉnh riêng biệt. | Các container **chia sẻ chung nhân hệ điều hành của máy chủ (Host OS Kernel)**; không có Guest OS. |
| **Dung lượng & Khởi động** | Dung lượng tệp ảnh lớn (hàng Gigabyte); thời gian khởi động lâu (tính bằng phút). | Tệp ảnh container siêu nhỏ (hàng Megabyte); **thời gian khởi động tức thì (tính bằng mili-giây)**. |
| **Hiệu năng & Tiêu hao** | Tiêu tốn nhiều tài nguyên CPU/RAM cho việc duy trì nhiều Guest OS; mật độ máy ảo thấp. | Tiêu hao tài nguyên gần như tương đương tiến trình gốc; mật độ container trên 1 máy chủ cao gấp hàng chục lần. |

#### 3. Bảng thuật ngữ các xu hướng công nghệ mới trong đề thi

| Thuật ngữ (KR / EN) | Định nghĩa kỹ thuật & Bản chất cơ chế | Ứng dụng thực tiễn điển hình |
| :--- | :--- | :--- |
| **매시업 (Mashup)** | Kỹ thuật lai ghép và kết hợp nội dung từ **hai hoặc nhiều giao diện lập trình mở (Open API)** khác nhau trên web để tạo ra một dịch vụ hoàn toàn mới. | Ứng dụng tìm nhà trọ kết hợp API bản đồ Google Maps với API dữ liệu giá đất thời gian thực. |
| **디지털 트윈 (Digital Twin)** | **Bản sao ảo hóa số** của một đối tượng vật lý, máy móc, hoặc quy trình trong thế giới thực, được cập nhật dữ liệu liên tục từ cảm biến IoT để mô phỏng và dự đoán. | Giám sát tình trạng vận hành của động cơ máy bay, dự báo bảo trì tua-bin điện gió trong Smart Factory. |
| **엣지 컴퓨팅 (Edge Computing)** | Mô hình xử lý dữ liệu **ngay tại rìa mạng (gần các cảm biến, thiết bị đầu cuối)** thay vì truyền toàn bộ dữ liệu thô về đám mây trung tâm; giúp giảm thiểu độ trễ tối đa. | Hệ thống xe tự hành (Autonomous Vehicles), phẫu thuật y tế từ xa, camera AI nhận diện khuôn mặt thời gian thực. |
| **앤 스크린 (N-Screen)** | Dịch vụ chia sẻ và đồng bộ nội dung đa phương tiện liền mạch trên **nhiều loại thiết bị màn hình khác nhau** (Smart TV, PC, Smartphone, Tablet). | Người dùng xem dở bộ phim trên điện thoại di động khi đi xe buýt, về nhà bật TV tiếp tục xem đúng đoạn đó. |
| **BaaS (Blockchain as a Service)** | Dịch vụ đám mây cho phép doanh nghiệp xây dựng, lưu trữ và vận hành các ứng dụng chuỗi khối (**DApp**) mà không cần tự đầu tư xây dựng hạ tầng nút mạng Node. | Triển khai nhanh chóng giải pháp Hợp đồng thông minh (Smart Contract) trong truy xuất nguồn gốc nông sản và chuỗi cung ứng. |
| **스쿱 (Sqoop)** | Công cụ dòng lệnh chuyên dụng được thiết kế để truyền tải dữ liệu hai chiều hiệu quả giữa **Cơ sở dữ liệu quan hệ truyền thống (RDBMS)** và **Hệ thống phân tán Hadoop HDFS**. | Xuất các bảng giao dịch từ Oracle/MySQL sang Hadoop HDFS để phục vụ phân tích dữ liệu lớn. |
| **텐서플로 (TensorFlow)** | Thư viện phần mềm mã nguồn mở do Google phát triển dành cho việc tính toán số học sử dụng đồ thị luồng dữ liệu (Dataflow Graphs), tối ưu cho **Machine Learning và Deep Learning**. | Huấn luyện mạng nơ-ron nhân tạo cho các bài toán xử lý ngôn ngữ tự nhiên, thị giác máy tính và nhận diện giọng nói. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Kiến trúc Trung tâm dữ liệu định nghĩa bằng phần mềm (SDDC)
SDDC (Software-Defined Data Center) là kiến trúc mà toàn bộ hạ tầng phần cứng của trung tâm dữ liệu đều được ảo hóa và điều khiển tập trung thông qua phần mềm thông minh:
- **SDC (Software-Defined Compute):** Ảo hóa tài nguyên tính toán (CPU, RAM) thông qua các giải pháp như VMware ESXi, KVM, Docker.
- **SDN (Software-Defined Networking):** Ảo hóa tài nguyên mạng, tách rời Control Plane và Data Plane.
- **SDS (Software-Defined Storage):** Ảo hóa toàn bộ các hệ thống đĩa lưu trữ thành một nhóm dung lượng chung linh hoạt.

---

### 복습 체크리스트
- [ ] Phân biệt 3 mô hình đám mây: IaaS (thuê phần cứng thô), PaaS (thuê nền tảng/runtime), SaaS (thuê ứng dụng hoàn chỉnh).
- [ ] Nắm vững ưu thế của Docker Container so với VM: Chia sẻ chung Host OS Kernel, không cần Guest OS, siêu nhẹ, khởi động mili-giây.
- [ ] Định nghĩa được Mashup: Ghép nối từ 2 Open API trở lên để tạo dịch vụ mới.
- [ ] Định nghĩa được Digital Twin: Bản sao số hóa ảo mô phỏng thiết bị thực tế để dự báo bảo trì.
- [ ] Định nghĩa được Edge Computing: Xử lý dữ liệu ngay tại rìa mạng gần thiết bị để đạt độ trễ siêu thấp (Zero Latency).
- [ ] Nhớ công cụ Sqoop: Chuyển đổi dữ liệu hai chiều giữa RDBMS và Hadoop.
