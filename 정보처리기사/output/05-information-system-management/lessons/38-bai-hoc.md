# 6. IT 신기술 및 소프트웨어 (Công nghệ IT mới & Phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm bắt các xu hướng công nghệ thông tin nổi bật: Docker, Mashup, Digital Twin, BaaS, N-Screen, Scrapy, TensorFlow.
- Hiểu rõ kiến trúc nền tảng tính toán phân tán xử lý dữ liệu lớn (Big Data): Hệ sinh thái Hadoop, HDFS và công cụ chuyển đổi dữ liệu Sqoop.
- Phân tích nguyên lý mô hình lập trình phân tán MapReduce trong việc chia nhỏ và tổng hợp khối dữ liệu khổng lồ.

## 핵심 키워드 (Từ khóa)
- **IT 신기술 (Emerging Tech)**: Docker (Containerization), Mashup (kết hợp API tạo dịch vụ mới), Digital Twin (bản sao số hóa thực tế), BaaS (Blockchain as a Service), N-Screen (đồng bộ đa màn hình).
- **데이터 도구 (Data Tools)**: TensorFlow (thư viện Machine Learning của Google), Scrapy (framework thu thập dữ liệu Python).
- **분산 컴퓨팅 (Distributed Computing)**: Hadoop (nền tảng xử lý phân tán), HDFS (hệ thống tệp phân tán), Sqoop (công cụ chuyển dữ liệu RDBMS $\leftrightarrow$ Hadoop), MapReduce (mô hình Map và Reduce).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [25-bai-hoc.md](25-bai-hoc.md) (DB 신기술 - Big Data, Hadoop HDFS, Data Mining).
- Liên kết với [18-bai-hoc.md](18-bai-hoc.md) (네트워크 및 인프라 신기술 - SDN, SDS, SDDC, NFV).
- Liên kết với [03-bai-hoc.md](03-bai-hoc.md) (프레임워크 특성 및 신기술).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh định nghĩa các thuật ngữ thi trắc nghiệm:
  - Ghép nhiều API công cộng để tạo dịch vụ mới (như ghép Bản đồ + Thông tin giá nhà) $\rightarrow$ **Mashup (매시업)**.
  - Tạo mô hình ảo mô phỏng y hệt máy móc thiết bị ngoài đời thực $\rightarrow$ **Digital Twin (디지털 트윈)**.
  - Chuyển dữ liệu giữa cơ sở dữ liệu quan hệ RDBMS và Hadoop $\rightarrow$ **Sqoop (스쿱)**.
  - Xem phim trên điện thoại rồi chuyển sang Smart TV xem tiếp đúng đoạn đó $\rightarrow$ **N-Screen (앤 스크린)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các thuật ngữ công nghệ mới tiêu biểu
| Thuật ngữ (KR / EN) | Định nghĩa và Bản chất kỹ thuật | Ứng dụng thực tiễn điển hình |
| :--- | :--- | :--- |
| **도커 (Docker)** | Nền tảng ảo hóa cấp hệ điều hành (Container) nhẹ, đóng gói ứng dụng cùng mọi thư viện phụ thuộc để chạy nhất quán trên mọi môi trường | Đóng gói microservices, triển khai CI/CD nhanh chóng |
| **매시업 (Mashup)** | Kỹ thuật lai ghép và kết hợp nội dung, dữ liệu từ hai hoặc nhiều giao diện lập trình ứng dụng (API) mở trên web để tạo ra một dịch vụ hoàn toàn mới | Ứng dụng bản đồ Google Maps tích hợp thông tin kẹt xe thời gian thực hoặc vị trí các quán ăn |
| **디지털 트윈 (Digital Twin)** | Bản sao ảo của một vật thể vật lý, máy móc hoặc quy trình trong thế giới thực, được cập nhật dữ liệu liên tục từ cảm biến IoT để mô phỏng và dự đoán | Giám sát tình trạng tua-bin gió, dự báo bảo trì máy bay, quản lý nhà máy thông minh |
| **앤 스크린 (N-Screen)** | Dịch vụ chia sẻ nội dung đa phương tiện liền mạch trên nhiều loại thiết bị phần cứng khác nhau (PC, TV, điện thoại thông minh, máy tính bảng) | Người dùng xem dở bộ phim trên điện thoại di động khi đi tàu, về nhà bật TV tiếp tục xem đúng vị trí đó |
| **BaaS (Blockchain as a Service)** | Mô hình điện toán đám mây cho phép người dùng xây dựng, lưu trữ và vận hành các ứng dụng chuỗi khối (DApp) mà không cần tự xây dựng cơ sở hạ tầng node | Triển khai nhanh hợp đồng thông minh (Smart Contract) trong truy xuất nguồn gốc nông sản |
| **스크래피 (Scrapy)** | Framework mã nguồn mở phát triển bằng Python phục vụ cho việc tự động thu thập và bóc tách dữ liệu có cấu trúc từ các trang web (Web Scraping) | Thu thập tự động bảng giá thương mại điện tử từ hàng nghìn website bán hàng |
| **텐서플로 (TensorFlow)** | Thư viện phần mềm mã nguồn mở do Google phát triển dành cho việc tính toán số học sử dụng đồ thị luồng dữ liệu (Dataflow graphs), tối ưu cho Machine Learning và Deep Learning | Huấn luyện mạng nơ-ron nhận diện giọng nói, thị giác máy tính, dịch tự động |

#### 2. Nền tảng Dữ liệu lớn Hadoop và MapReduce
- **Hệ sinh thái Apache Hadoop**:
  - Nền tảng phần mềm mã nguồn mở cho phép lưu trữ và xử lý phân tán các tập dữ liệu khổng lồ (Big Data) trên các cụm máy chủ thông thường (Commodity Hardware).
  - **HDFS (Hadoop Distributed File System)**: Hệ thống tệp phân tán chia nhỏ các tệp tin lớn thành các khối (Block kích thước mặc định 128MB) và nhân bản chúng (Replication Factor = 3) trên nhiều nút lưu trữ (DataNodes) để đảm bảo độ tin cậy cao.
  - **Sqoop (SQL-to-Hadoop)**: Công cụ dòng lệnh chuyên dụng được thiết kế để truyền tải dữ liệu hiệu quả hai chiều giữa cơ sở dữ liệu quan hệ truyền thống (RDBMS như Oracle, MySQL) và hệ sinh thái phân tán Hadoop (HDFS, Hive, HBase).
- **Mô hình lập trình MapReduce**:
  - **Map (Ánh xạ)**: Đọc dữ liệu đầu vào từ HDFS, phân tích và lọc để trích xuất ra tập hợp các cặp khóa-giá trị trung gian: `(Key, Value)`.
  - **Shuffle & Sort (Xáo trộn & Sắp xếp)**: Gom nhóm tất cả các giá trị có cùng một Khóa lại với nhau và gửi tới các tiến trình Reduce.
  - **Reduce (Thu gọn / Tổng hợp)**: Tiếp nhận dữ liệu đã gom nhóm theo từng khóa, thực hiện các phép tính toán tổng hợp (như cộng dồn, đếm từ, tính trung bình) và xuất kết quả cuối cùng ra hệ thống tệp HDFS.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ luồng xử lý của mô hình MapReduce (Đếm từ - WordCount)
```
[Tài liệu đầu vào] ──► "apple banana apple"
          │
          ▼
    [Giai đoạn MAP]
    - Nút 1: ("apple", 1), ("banana", 1)
    - Nút 2: ("apple", 1)
          │
          ▼
 [SHUFFLE & SORT (Gom nhóm theo Khóa)]
    - Khóa "apple"  ──► [1, 1]
    - Khóa "banana" ──► [1]
          │
          ▼
   [Giai đoạn REDUCE (Tính tổng)]
    - ("apple", 2)
    - ("banana", 1)
          │
          ▼
[Ghi kết quả ra HDFS]
```

#### 2. So sánh Containerization (Docker) vs Virtual Machine (VM)
- **Máy ảo (Virtual Machine - Hypervisor)**: Cần một hệ điều hành khách (Guest OS) hoàn chỉnh trên mỗi máy ảo $\rightarrow$ Nặng nề, tốn RAM, thời gian khởi động tính bằng phút.
- **Docker Container**: Chia sẻ chung nhân hệ điều hành của máy chủ chủ (Host OS Kernel), chỉ đóng gói mã nguồn và thư viện phụ thuộc $\rightarrow$ Siêu nhẹ, khởi động chỉ mất vài mili-giây, mật độ container trên một máy chủ cao hơn gấp nhiều lần.

---

### 복습 체크리스트
- [ ] Công nghệ Mashup kết hợp những yếu tố nào để tạo ra một dịch vụ web mới?
- [ ] Công cụ Sqoop trong hệ sinh thái Hadoop đảm nhận vai trò kết nối với loại cơ sở dữ liệu nào?
- [ ] Hai giai đoạn Map và Reduce trong mô hình xử lý phân tán MapReduce thực hiện những nhiệm vụ kỹ thuật gì?
- [ ] Sự khác biệt then chốt về mặt kiến trúc giữa Docker Container và máy ảo VM truyền thống là gì?
