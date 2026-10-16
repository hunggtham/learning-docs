# 데이터베이스 복구, 병행 제어 및 빅데이터 기술 (Phục hồi CSDL, Kiểm soát đồng thời & NoSQL, Big Data 5V, Hadoop/Spark)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế và trường hợp áp dụng của hai thao tác phục hồi dữ liệu hạt nhân: **REDO** (tái thực thi giao dịch đã commit) và **UNDO** (hủy bỏ giao dịch chưa commit).
- Phân biệt 4 kỹ thuật phục hồi cơ sở dữ liệu khi xảy ra sự cố: **Cập nhật trì hoãn (연기 갱신 - Deferred Update)**, **Cập nhật tức thì (즉각 갱신 - Immediate Update)**, **Điểm kiểm tra (검사점 - Checkpoint)**, và **Phân trang bóng (그림자 페이지 - Shadow Paging)**.
- Hiểu rõ 4 hiện tượng bất thường khi không kiểm soát đồng thời: Mất cập nhật (**Lost Update**), Đọc dữ liệu sai lệch (**Inconsistency**), Thu hồi dây chuyền (**Cascading Rollback**), và Đọc dữ liệu dở dang (**Dirty Read**).
- Thấu hiểu mối quan hệ đánh đổi của độ mịn khóa (**Locking Granularity**) và nguyên lý Giao thức khóa hai pha (**2PL - Two-Phase Locking**).
- Phân biệt 4 họ cơ sở dữ liệu phi quan hệ **NoSQL**: **Key-Value (Redis)**, **Document (MongoDB)**, **Column-family (Cassandra, HBase)**, và **Graph (Neo4j)**.
- Làm chủ 5 đặc trưng của Dữ liệu lớn (**Big Data 5V**: Volume, Velocity, Variety, Veracity, Value) và phân biệt kiến trúc phân tán **Hadoop HDFS / MapReduce** với nền tảng tính toán trong bộ nhớ **Apache Spark (In-Memory / RDD)**.
- Nắm vững 5 thao tác phân tích dữ liệu đa chiều **OLAP** (Roll-up, Drill-down, Slicing, Dicing, Pivoting).

## 핵심 키워드 (Từ khóa song ngữ)
- REDO / UNDO (재실행 REDO: Commit 완료 복구 vs 취소 UNDO: 미완료 롤백)
- 연기 갱신 기법 (Deferred Update — Log에만 기록, Commit 전 DB 미반영, REDO만 수행, UNDO 없음)
- 즉각 갱신 기법 (Immediate Update — Log와 DB 동시 반영, REDO와 UNDO 모두 수행)
- 그림자 페이지 (Shadow Paging — Current Page Table vs Shadow Page Table, Log 불필요)
- 병행 제어 이상 현상 (갱신 분실 Lost Update, 모순성 Inconsistency, 연쇄 복귀 Cascading, Dirty Read)
- NoSQL 4대 유형 (Key-Value Redis, Document MongoDB, Column Cassandra/HBase, Graph Neo4j)
- 빅데이터 5V (Volume 규모, Velocity 속도, Variety 다양성, Veracity 정확성/신뢰성, Value 가치)
- 하둡 / HDFS (Hadoop Distributed File System — 128MB 블록, 3중 복제 3-way Replication)
- 맵리듀스 vs 스파크 (MapReduce 디스크 기반 배치 vs Apache Spark 인메모리 RDD 고속 분산처리)
- OLAP 5대 연산 (Roll-up 드릴업 요약, Drill-down 상세분석, Slicing 단면, Dicing 소입방체, Pivoting 회전)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi nghiên cứu kiến trúc bộ nhớ và hệ thống đĩa lưu trữ tại [14-quan-ly-bo-nho-va-luu-tru-storage.md](14-quan-ly-bo-nho-va-luu-tru-storage.md), các hệ thống doanh nghiệp phải đảm bảo tính bền vững (Durability) và tính nhất quán (Consistency) cho dữ liệu nghiệp vụ quan trọng thông qua hệ quản trị CSDL.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn diện các giải pháp vận hành CSDL ở quy mô doanh nghiệp: phục hồi sau sự cố nguồn điện/phần cứng, điều phối đồng thời các giao dịch không bị xung đột, và mở rộng quy mô xử lý sang các cụm máy chủ Big Data, Hadoop HDFS, Spark và CSDL phi quan hệ NoSQL.
- **Dùng đi đâu (Forward Handoff):** Các cụm lưu trữ phân tán Hadoop và CSDL NoSQL này là các thành phần hạ tầng được đóng gói triển khai trên nền tảng Điện toán đám mây và Container tại [16-dien-toan-dam-may-va-cong-nghe-moi.md](16-dien-toan-dam-may-va-cong-nghe-moi.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Kỹ thuật phục hồi CSDL (Bẫy đề thi kinh điển):**
  - **Cập nhật trì hoãn (연기 갱신 - Deferred Update):** Đề hỏi kỹ thuật nào **CHỈ DÙNG REDO, KHÔNG BAO GIỜ CẦN UNDO** $\rightarrow$ Chọn ngay **연기 갱신 기법**.
  - **Cập nhật tức thời (즉각 갱신 - Immediate Update):** Cần cả **REDO (cho giao dịch đã Commit)** VÀ **UNDO (cho giao dịch chưa Commit)**.
  - **Phân trang bóng (그림자 페이지 - Shadow Paging):** Đề hỏi kỹ thuật phục hồi nào **KHÔNG CẦN DÙNG TỆP NHẬT KÝ (Log file)** $\rightarrow$ Chọn **그림자 페이지**.
- **Độ mịn khóa (Locking Granularity):**
  - Khóa quy mô lớn (Database, Table): Mức độ đồng thời thấp, chi phí quản lý Overhead ít, không sợ Deadlock.
  - Khóa quy mô nhỏ (Record, Field): Mức độ đồng thời cao, chi phí quản lý Overhead lớn, nguy cơ Deadlock cao.
- **4 họ NoSQL:**
  - Key-Value: Redis, Memcached (tốc độ RAM).
  - Document: MongoDB, CouchDB (JSON/BSON).
  - Column-family: Cassandra, HBase (phân tích bảng lớn).
  - Graph: Neo4j (đồ thị nút-cạnh).
- **Big Data 5V & Hệ sinh thái Hadoop/Spark:**
  - Thuộc lòng 5 chữ V: **Volume, Velocity, Variety, Veracity, Value**.
  - HDFS: Chia khối (Block 128MB), nhân bản mặc định 3 bản sao.
  - Xử lý phân tán trong bộ nhớ RAM tốc độ cao gấp nhiều lần MapReduce $\rightarrow$ Chọn ngay **Apache Spark (In-Memory / RDD)**.
- **Thao tác OLAP (Nhận diện bằng động từ hành động):**
  - Đi từ chi tiết lên khái quát hơn $\rightarrow$ **Roll-up (드릴업)**.
  - Đi từ khái quát xuống chi tiết sâu hơn $\rightarrow$ **Drill-down (드릴다운)**.
  - Cắt một lát cắt cố định trên một chiều $\rightarrow$ **Slicing (슬라이싱)**.
  - Cắt một khối hộp con nhỏ hơn trên nhiều chiều $\rightarrow$ **Dicing (다이싱)**.
  - Đổi trục hàng thành cột và ngược lại $\rightarrow$ **Pivoting (피버팅)**.

---

## 데이터베이스 복구, 병행 제어 및 빅데이터 기술

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các kỹ thuật phục hồi cơ sở dữ liệu (Database Recovery)
Mục tiêu đưa cơ sở dữ liệu về trạng thái nhất quán và chính xác gần nhất trước khi sự cố xảy ra:

| Kỹ thuật phục hồi | Tên tiếng Hàn & Anh | Cơ chế vận hành chi tiết | Thao tác phục hồi bắt buộc |
| :--- | :--- | :--- | :---: |
| **Cập nhật trì hoãn** | **연기 갱신 (Deferred Update)** | Trong quá trình giao dịch thực thi, mọi thao tác sửa đổi dữ liệu chỉ được ghi vào tệp nhật ký (Log), tuyệt đối chưa ghi vào CSDL vật lý trên đĩa. Chỉ khi giao dịch Commit thành công, các thay đổi mới chính thức được ghi xuống đĩa CSDL. | **Chỉ thực hiện REDO** (Tuyệt đối KHÔNG cần UNDO) |
| **Cập nhật tức thì** | **즉각 갱신 (Immediate Update)** | Trong quá trình giao dịch thực thi, mọi sửa đổi được ghi đồng thời vào cả tệp nhật ký (Log) và CSDL vật lý ngay lập tức. Nếu xảy ra sự cố trước khi Commit, CSDL đã chứa dữ liệu dở dang. | **Thực hiện cả REDO và UNDO** (REDO cho Commit, UNDO cho chưa Commit) |
| **Điểm kiểm tra** | **검사점 (Checkpoint)** | Định kỳ hệ thống cưỡng chế ghi toàn bộ bộ đệm nhật ký và dữ liệu xuống đĩa vật lý rồi đánh dấu mốc 검사점. Khi sự cố xảy ra, bộ phục hồi chỉ cần quét nhật ký từ điểm Checkpoint gần nhất trở lại, không phải duyệt lại toàn bộ Log từ đầu. | Tùy thuộc vào thời điểm giao dịch so với mốc Checkpoint |
| **Phân trang bóng** | **그림자 페이지 (Shadow Paging)** | Duy trì song song 2 bảng trang: Bảng trang hiện tại (Current Page Table) phục vụ ghi dữ liệu và Bảng trang bóng (Shadow Page Table) lưu giữ trạng thái CSDL ban đầu. Khi có sự cố, hệ thống chỉ việc trỏ lại bảng trang bóng; hoàn toàn không cần tệp Log. | Trỏ lại bảng trang bóng ban đầu |

#### 2. Kiểm soát đồng thời và Độ mịn khóa (Concurrency Control)
- **4 hiện tượng bất thường khi thực thi đồng thời không được kiểm soát:**
  1. **갱신 분실 (Lost Update - Mất cập nhật):** Hai giao dịch cùng cập nhật một trường dữ liệu; giao dịch chạy sau ghi đè lên kết quả của giao dịch chạy trước, làm mất mát hoàn toàn dữ liệu cập nhật của giao dịch đầu.
  2. **모순성 / 비일관성 (Inconsistency - Bất nhất quán):** Giao dịch thứ nhất đang tính toán tổng trên nhiều bản ghi thì giao dịch thứ hai xen vào sửa đổi một số bản ghi, dẫn đến kết quả tổng hợp bị sai lệch và không nhất quán.
  3. **연쇄 복귀 (Cascading Rollback - Thu hồi dây chuyền):** Giao dịch $T_1$ gặp sự cố phải hủy bỏ (`ROLLBACK`), kéo theo giao dịch $T_2$ (đã lỡ đọc dữ liệu dở dang của $T_1$) cũng phải `ROLLBACK`, gây phản ứng dây chuyền làm lãng phí tài nguyên hệ thống.
  4. **미완료 의존성 / Dirty Read (Đọc dữ liệu bẩn):** Giao dịch $T_2$ đọc một bản ghi do giao dịch $T_1$ sửa đổi nhưng chưa kịp `COMMIT`; ngay sau đó $T_1$ bị lỗi và `ROLLBACK` về giá trị cũ $\implies T_2$ đã dùng dữ liệu sai hoàn toàn.
- **Độ mịn khóa (로킹 단위 - Locking Granularity):**

| Cấp độ khóa | Mức độ đồng thời (Concurrency) | Chi phí quản lý khóa (Overhead) | Nguy cơ bế tắc (Deadlock) |
| :--- | :---: | :---: | :---: |
| **Khóa quy mô lớn** (Database, Table) | **Rất thấp** (Phải xếp hàng đợi cả bảng) | **Rất ít** (Chỉ quản lý vài chiếc khóa lớn) | **Cực thấp** |
| **Khóa quy mô nhỏ** (Record, Field) | **Rất cao** (Cập nhật các dòng khác nhau) | **Rất lớn** (Phải lưu vết hàng triệu chiếc khóa) | **Rất cao** |

#### 3. Cơ sở dữ liệu phi quan hệ NoSQL (Not Only SQL)
NoSQL được thiết kế để vượt qua giới hạn mở rộng (Scale-out) của CSDL quan hệ truyền thống đối với dữ liệu phi cấu trúc lớn:

| Họ NoSQL | Mô hình dữ liệu & Cơ chế lưu trữ | Cơ sở dữ liệu đại diện | Ưu điểm & Điểm thi trọng tâm |
| :--- | :--- | :--- | :--- |
| **Key-Value Store** | Lưu trữ từng cặp Khóa - Giá trị (`Key-Value`) đơn giản; tìm kiếm trực tiếp qua bảng băm trên RAM. | **Redis**, Memcached | Tốc độ đọc ghi cực nhanh (In-Memory); phù hợp cho lưu bộ nhớ đệm Cache, Session người dùng. |
| **Document Store** | Dữ liệu được lưu trữ dưới dạng tài liệu bán cấu trúc JSON, BSON, hoặc XML; không ràng buộc Schema. | **MongoDB**, CouchDB | Khả năng biểu diễn cấu trúc dữ liệu lồng nhau linh hoạt; dễ dàng mở rộng và truy vấn phức tạp. |
| **Column-family Store** | Lưu trữ dữ liệu theo nhóm cột (Column Families) thay vì theo hàng; hỗ trợ bảng hàng triệu cột thưa thớt. | **Apache Cassandra**, HBase | Tối ưu hóa tối đa cho các truy vấn phân tích tổng hợp trên tập dữ liệu lớn hàng Petabyte. |
| **Graph Database** | Lưu trữ dữ liệu dưới dạng Nút (Nodes - Thực thể), Cạnh (Edges - Quan hệ) và Thuộc tính (Properties). | **Neo4j**, OrientDB | Hiệu năng vượt trội trong việc duyệt đồ thị và mối quan hệ phức tạp (mạng xã hội, đồ thị tri thức). |

#### 4. Đặc trưng Big Data 5V và Hệ sinh thái Hadoop / Spark
- **Năm đặc trưng cốt lõi của Dữ liệu lớn (Big Data 5V):**
  1. **Volume (Dung lượng):** Quy mô kích thước dữ liệu khổng lồ từ Terabyte đến Petabyte và Exabyte.
  2. **Velocity (Tốc độ):** Tốc độ sinh ra và yêu cầu xử lý dữ liệu cực nhanh theo thời gian thực (Streaming).
  3. **Variety (Đa dạng):** Dữ liệu có nhiều hình thái: có cấu trúc (RDB), bán cấu trúc (JSON, XML), và phi cấu trúc (Hình ảnh, Video, Âm thanh, Log văn bản).
  4. **Veracity (Tính xác thực / Độ tin cậy):** Độ tin cậy và chất lượng của dữ liệu, loại bỏ nhiễu và dữ liệu giả mạo.
  5. **Value (Giá trị):** Giá trị kinh tế và tri thức chiến lược có thể khai phá được từ dữ liệu phục vụ kinh doanh.
- **Hệ sinh thái phân tán Hadoop:**
  - **HDFS (Hadoop Distributed File System):** Hệ thống tệp phân tán chia tệp thành các khối (**Blocks**, mặc định 128MB) và tự động nhân bản **3 bản sao (3-way Replication)** phân tán trên các cụm máy chủ giá rẻ để đảm bảo khả năng chịu lỗi.
  - **MapReduce:** Mô hình lập trình tính toán phân tán gồm pha **Map** (chia nhỏ dữ liệu thành cặp Key-Value) và pha **Reduce** (gom nhóm và tổng hợp kết quả theo Key); ghi trung gian xuống đĩa cứng.
- **Apache Spark (Nền tảng tính toán phân tán In-Memory):**
  - Khung xử lý phân tán thế hệ mới xử lý dữ liệu hoàn toàn **trong bộ nhớ RAM (In-Memory Computing)**, cho tốc độ xử lý nhanh hơn Hadoop MapReduce từ 10 đến 100 lần.
  - Cấu trúc dữ liệu hạt nhân là **RDD (Resilient Distributed Datasets - Tập dữ liệu phân tán có khả năng phục hồi)**, cho phép xử lý song song chịu lỗi cao mà không cần ghi đĩa liên tục.

#### 5. Năm phép toán phân tích trực tuyến đa chiều OLAP (OLAP Operations)

| Phép toán OLAP | Tên tiếng Hàn & Anh | Bản chất thao tác phân tích dữ liệu |
| :--- | :--- | :--- |
| **Roll-up** | **롤업 (드릴업 - Drill-up)** | Thu gom, tổng hợp dữ liệu từ mức độ chi tiết lên mức độ bao quát tổng quan hơn (Doanh thu từ cấp Thành phố $\rightarrow$ Tỉnh $\rightarrow$ Quốc gia). |
| **Drill-down** | **드릴다운 (Drill-down)** | Mở rộng, đào sâu dữ liệu từ mức độ tổng quan xuống mức độ chi tiết cụ thể hơn (Doanh thu từ cấp Năm $\rightarrow$ Quý $\rightarrow$ Tháng $\rightarrow$ Ngày). |
| **Slicing** | **슬라이싱 (Slicing)** | Cắt một lát cắt cố định của khối dữ liệu đa chiều bằng cách chọn một giá trị duy nhất trên một chiều (lọc riêng dữ liệu của Năm 2026). |
| **Dicing** | **다이싱 (Dicing)** | Cắt ra một khối lập phương con nhỏ hơn từ khối dữ liệu lớn bằng cách chọn một tập hợp các giá trị trên nhiều chiều đồng thời. |
| **Pivoting** | **피버팅 (Pivoting)** | Xoay trục tọa độ biểu diễn dữ liệu (hoán đổi hàng thành cột và cột thành hàng) để người quản trị có góc nhìn phân tích mới trực quan hơn. |

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Giao thức Khóa hai pha (2PL - Two-Phase Locking Protocol)
Để đảm bảo tính tuần tự hóa của các giao dịch đồng thời và ngăn chặn xung đột dữ liệu:
1. **Pha mở rộng (Growing Phase / 확장 단계):** Giao dịch chỉ được phép xin cấp phát thêm các khóa (Lock) mới; **tuyệt đối không được nhả bất kỳ khóa nào**.
2. **Pha thu hẹp (Shrinking Phase / 축소 단계):** Khi giao dịch nhả chiếc khóa đầu tiên, nó chính thức bước vào pha thu hẹp; trong pha này giao dịch **chỉ được phép giải phóng khóa, tuyệt đối không được xin thêm khóa mới**.
- *Lưu ý đề thi:* Giao thức 2PL bảo đảm tính tuần tự hóa (Serializability) nhưng **KHÔNG ngăn chặn được bế tắc Deadlock**!

---

### 복습 체크리스트
- [ ] Phân biệt rõ: Cập nhật trì hoãn (연기 갱신) chỉ dùng REDO; Cập nhật tức thì (즉각 갱신) dùng cả REDO và UNDO.
- [ ] Nhớ kỹ thuật Shadow Paging: Quản lý 2 bảng trang (Current vs Shadow), không cần dùng tệp Log.
- [ ] Nhận diện 4 lỗi đồng thời: Mất cập nhật (Lost Update), Đọc bất nhất quán (Inconsistency), Thu hồi dây chuyền (Cascading Rollback), Đọc dở dang (Dirty Read).
- [ ] Nắm vững quy luật độ mịn khóa: Khóa to thì đồng thời kém, chi phí ít; Khóa nhỏ thì đồng thời cao, chi phí lớn, dễ Deadlock.
- [ ] Phân loại chính xác 4 họ NoSQL: Key-Value (Redis), Document (MongoDB), Column-family (Cassandra/HBase), Graph (Neo4j).
- [ ] Thuộc lòng Big Data 5V: Volume (dung lượng), Velocity (tốc độ), Variety (đa dạng), Veracity (chính xác/tin cậy), Value (giá trị).
- [ ] Phân biệt Hadoop HDFS/MapReduce (ghi đĩa phân tán) vs Apache Spark (In-Memory RDD tốc độ cao).
- [ ] Phân biệt 5 phép toán OLAP: Roll-up (lên khái quát), Drill-down (xuống chi tiết), Slicing (cắt lát 1 chiều), Dicing (cắt khối nhiều chiều), Pivoting (xoay trục).
