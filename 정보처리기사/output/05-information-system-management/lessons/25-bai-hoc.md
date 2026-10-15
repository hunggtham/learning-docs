# 데이터베이스 신기술 (DB New Technologies)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, kiến trúc hạt nhân và cơ chế vận hành của hệ sinh thái Dữ liệu lớn (**Big Data**): Khung phần mềm phân tán **Hadoop (HDFS)** và mô hình tính toán song song **MapReduce**.
- Thuộc lòng 5 thao tác phân tích dữ liệu đa chiều kinh điển trong hệ thống **OLAP (On-Line Analytical Processing)**: Roll-up, Drill-down, Slicing, Dicing, và Pivoting.
- Phân biệt sự khác nhau giữa Khai phá dữ liệu (**Data Mining**) nhằm trích xuất mẫu quy luật tiềm ẩn và Cơ sở dữ liệu phi quan hệ (**NoSQL**) phục vụ mở rộng quy mô lưu trữ phân tán.

## 핵심 키워드 (Từ khóa)
- 빅데이터 기술 (Big Data Technologies)
- 하둡 (Hadoop - 오픈소스 자바 분산 프레임워크)
- HDFS (Hadoop Distributed File System - 블록 복제 분산 저장)
- 맵리듀스 (MapReduce - Map 분류 + Reduce 집계)
- 데이터 마이닝 (Data Mining - 숨겨진 패턴 및 규칙 발견)
- OLAP 5대 연산 (Roll-up, Drill-down, Slicing, Dicing, Pivoting)
- NoSQL (Not Only SQL - Key-Value, Document, Column, Graph)

## 선행·연결 개념 (Kiến thức liên kết)
- [24-bai-hoc.md](24-bai-hoc.md): Kỹ thuật lõi CSDL (Phục hồi REDO/UNDO và Kiểm soát đồng thời).
- [26-bai-hoc.md](26-bai-hoc.md): An toàn thông tin tổng quan và các tiêu chuẩn bảo mật.
- [28-bai-hoc.md](28-bai-hoc.md): Công nghệ bảo mật mới (Secure OS, Blockchain BaaS, TrustZone).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh 5 thao tác OLAP trong đề thi:
  - **Roll-up (롤업):** Đi từ **Chi tiết lên Khái quát** (ví dụ: Xem doanh thu từ Ngày $\rightarrow$ gom lên Tháng $\rightarrow$ Năm).
  - **Drill-down (드릴다운):** Đi từ **Khái quát xuống Chi tiết** (ví dụ: Xem từ Năm $\rightarrow$ bấm đào sâu xuống từng Quý $\rightarrow$ từng Ngày).
  - **Slicing (슬라이싱):** Cắt một lát mỏng theo **1 chiều duy nhất** (ví dụ: Xem lát cắt Doanh thu của riêng Năm 2026).
  - **Dicing (다이싱):** Cắt một **khối hộp nhỏ con** bằng cách chọn khoảng giá trị trên **nhiều chiều đồng thời**.
  - **Pivoting (피보팅):** **Xoay trục dữ liệu** (đổi Hàng thành Cột và Cột thành Hàng) để đổi góc nhìn báo cáo.
- Về Hadoop: Nhớ **HDFS** là lưu trữ phân tán có nhân bản dữ liệu, **MapReduce** là xử lý tính toán song song.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Hệ sinh thái xử lý dữ liệu lớn Hadoop (Apache Hadoop Ecosystem):**
  - **Hadoop:** Khung phần mềm mã nguồn mở viết bằng Java cho phép lưu trữ và xử lý phân tán các tập dữ liệu khổng lồ (Petabytes) trên các cụm máy tính thông thường (Commodity Hardware).
  - **2 thành phần hạt nhân:**
    1. **HDFS (Hadoop Distributed File System):** Chia nhỏ tệp tin lớn thành các khối Block (mặc định 128MB) và tự động nhân bản (Replication, thường là 3 bản sao) phân tán đều trên các máy tính DataNode trong cụm để chống mất mát dữ liệu khi có máy chủ bị hỏng phần cứng.
    2. **MapReduce (맵리듀스):** Mô hình lập trình tính toán song song gồm 2 giai đoạn:
       - **Map (맵):** Đọc dữ liệu thô, phân tích cú pháp, lọc và ánh xạ dữ liệu thành tập hợp các cặp khóa-giá trị trung gian `<Key, Value>`.
       - **Reduce (리듀스):** Gom nhóm (Shuffle & Sort) tất cả các giá trị có cùng một Khóa và thực hiện phép tính toán tổng hợp (Sum, Average, Count) để cho ra kết quả cuối cùng.

- **2. Bảng 5 thao tác xử lý phân tích trực tuyến đa chiều (OLAP Operations):**

| Thao tác OLAP | Tên tiếng Hàn & Anh | Bản chất thao tác dữ liệu đa chiều | Ví dụ minh họa thực tiễn |
| :--- | :--- | :--- | :--- |
| **Roll-up** | **롤업** | Gom cụm, trừu tượng hóa dữ liệu từ cấp độ chi tiết thấp lên cấp độ tổng hợp vĩ mô cao hơn dọc theo cây phân cấp. | Từ báo cáo doanh số theo từng *Cửa hàng* gom lên thành doanh số theo từng *Tỉnh thành* và *Toàn quốc*. |
| **Drill-down** | **드릴다운** (Drill-through) | Mở rộng chi tiết, đào sâu cấu trúc dữ liệu từ cấp độ tóm tắt vĩ mô xuống các cấp độ vi mô cụ thể hơn. | Từ tổng doanh số *Năm* bấm mở rộng để xem chi tiết doanh số của từng *Quý*, từng *Tháng*, từng *Tuần*. |
| **Slicing** | **슬라이싱** | Cố định giá trị của đúng một chiều duy nhất để trích xuất ra một lát cắt bảng dữ liệu 2 chiều từ khối đa chiều. | Trích xuất toàn bộ dữ liệu bán hàng của riêng chiều *Khu vực = Miền Bắc* (bỏ qua các miền khác). |
| **Dicing** | **다이싱** | Chọn lọc một dải giá trị trên hai hoặc nhiều chiều khác nhau để cắt ra một khối hộp dữ liệu con (Sub-cube). | Trích xuất khối dữ liệu bán hàng của *Khu vực Miền Nam* VÀ *Thời gian trong Quý 3* VÀ *Mặt hàng Điện thoại*. |
| **Pivoting** | **피보팅** | Hoán đổi vị trí của các chiều phân tích trong không gian (Xoay trục ma trận hiển thị). | Chuyển chiều *Sản phẩm* từ Cột sang Hàng và chiều *Thời gian* từ Hàng sang Cột để tiện so sánh. |

- **3. Phân loại 4 họ cơ sở dữ liệu phi quan hệ (NoSQL):**
  - **Key-Value Store:** Dữ liệu lưu dưới dạng cặp khóa-giá trị đơn giản, tốc độ đọc ghi cực nhanh trên RAM. *Ví dụ:* Redis, Memcached, DynamoDB.
  - **Document Store:** Lưu dữ liệu dạng tài liệu bán cấu trúc (JSON, BSON, XML), linh hoạt schema. *Ví dụ:* MongoDB, CouchDB.
  - **Column-Family Store:** Lưu trữ dữ liệu phân tán theo từng cột thay vì từng dòng, tối ưu cho truy vấn phân tích bảng lớn. *Ví dụ:* Apache Cassandra, HBase.
  - **Graph Store:** Biểu diễn các nút (Node) và cạnh liên kết (Edge) để phân tích mạng xã hội, phòng chống gian lận. *Ví dụ:* Neo4j.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật Khai phá dữ liệu (Data Mining):**
  - Sử dụng các giải thuật học máy (Machine Learning) và thống kê để tự động tìm kiếm các mối liên hệ ngầm trong kho dữ liệu (Data Warehouse).
  - *Các kỹ thuật chính:* Phân lớp (Classification - Cây quyết định Decision Tree), Gom cụm (Clustering - K-Means), Phân tích luật kết hợp (Association Rules - Thuật toán Apriori: ví dụ phát hiện khách mua bia thường mua kèm tã lót).

### 복습 체크리스트
- [ ] Nhớ 2 thành phần lõi của Hadoop: HDFS (lưu trữ phân tán) và MapReduce (tính toán song song).
- [ ] Thuộc lòng 5 thao tác OLAP: Roll-up (tổng hợp lên), Drill-down (đào sâu xuống), Slicing (cắt 1 chiều), Dicing (cắt khối nhiều chiều), Pivoting (xoay trục).
- [ ] Phân biệt được: Data Mining là tìm quy luật ẩn, còn Data Warehouse là kho lưu trữ dữ liệu tích hợp.
- [ ] Kể tên 4 họ NoSQL: Key-Value (Redis), Document (MongoDB), Column (HBase), Graph (Neo4j).
