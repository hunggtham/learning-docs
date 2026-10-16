# 데이터베이스 복구, 병행 제어 및 빅데이터 기술 (Phục hồi cơ sở dữ liệu, Kiểm soát đồng thời & Công nghệ Big Data NoSQL)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế và trường hợp áp dụng của hai thao tác phục hồi dữ liệu hạt nhân: **REDO** (tái thực thi giao dịch đã commit) và **UNDO** (hủy bỏ giao dịch chưa commit).
- Phân biệt 4 kỹ thuật phục hồi cơ sở dữ liệu khi xảy ra sự cố: **Cập nhật trì hoãn (연기 갱신 - Deferred Update)**, **Cập nhật tức thì (즉각 갱신 - Immediate Update)**, **Điểm kiểm tra (검사점 - Checkpoint)**, và **Phân trang bóng (그림자 페이지 - Shadow Paging)**.
- Hiểu rõ 4 hiện tượng bất thường khi không kiểm soát đồng thời: Mất cập nhật (**갱신 분실 - Lost Update**), Đọc dữ liệu sai lệch (**모순성 - Inconsistent Analysis**), Thu hồi dây chuyền (**연쇄 복귀 - Cascading Rollback**), và Đọc dữ liệu dở dang (**Dirty Read**).
- Thấu hiểu mối quan hệ đánh đổi của độ mịn khóa (**Locking Granularity**) và nguyên lý Giao thức khóa hai pha (**2PL - Two-Phase Locking**).
- Nắm vững kiến trúc hệ sinh thái Big Data: **Hadoop HDFS** (hệ thống tệp phân tán nhân bản 3 khối) và mô hình tính toán song song **MapReduce**.
- Phân loại 4 nhóm cơ sở dữ liệu phi quan hệ **NoSQL** (Key-Value, Document, Column, Graph) và 5 thao tác phân tích dữ liệu đa chiều **OLAP** (Roll-up, Drill-down, Slicing, Dicing, Pivoting).

## 핵심 키워드 (Từ khóa song ngữ)
- REDO / UNDO (재실행 REDO: Commit 완료 트랜잭션 복구 vs 취소 UNDO: 미완료 트랜잭션 롤백)
- 연기 갱신 기법 (Deferred Update — Log에만 기록, Commit 전 DB 반영 안 함, REDO만 수행, UNDO 없음)
- 즉각 갱신 기법 (Immediate Update — Log와 DB에 실시간 반영, REDO와 UNDO 모두 수행)
- 검사점 기법 (Checkpoint — 특정 시점 메모리 강제 디스크 저장, 장애 시 검사점 이후만 회복)
- 그림자 페이지 (Shadow Paging — Current Page Table vs Shadow Page Table 2개 관리, Log 불필요)
- 병행 제어 미수행 문제 (Concurrency Anomalies — 갱신 분실, 모순성/비일관성, 연쇄 복귀, Dirty Read)
- 로킹 단위 (Locking Granularity — 단위 크면: 관리 쉽고 병행성 낮음 vs 단위 작으면: 병행성 높고 오버헤드 큼)
- 하둡 / HDFS (Hadoop Distributed File System — 저가 서버 클러스터, 블록 3중 복제)
- 맵리듀스 (MapReduce — Map 분할 쌍생성 $\rightarrow$ Reduce 집계 요약 분산 컴퓨팅)
- OLAP 5대 연산 (Roll-up 드릴업 요약, Drill-down 상세분석, Slicing 단면, Dicing 소입방체, Pivoting 회전)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi nghiên cứu kiến trúc bộ nhớ và hệ thống đĩa lưu trữ tại [14-quan-ly-bo-nho-va-luu-tru-storage.md](14-quan-ly-bo-nho-va-luu-tru-storage.md), các hệ thống doanh nghiệp phải đảm bảo tính bền vững (Durability) và tính nhất quán (Consistency) cho dữ liệu nghiệp vụ quan trọng thông qua hệ quản trị CSDL.
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn diện các giải pháp vận hành CSDL ở quy mô doanh nghiệp: phục hồi sau sự cố nguồn điện/phần cứng, điều phối đồng thời các giao dịch không bị xung đột, và mở rộng quy mô xử lý sang các cụm máy chủ Big Data và CSDL phi quan hệ NoSQL.
- **Dùng đi đâu (Forward Handoff):** Các cụm lưu trữ phân tán Hadoop và CSDL NoSQL này là các thành phần hạ tầng được đóng gói triển khai trên nền tảng Điện toán đám mây và Container tại [16-dien-toan-dam-may-va-cong-nghe-moi.md](16-dien-toan-dam-may-va-cong-nghe-moi.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Kỹ thuật phục hồi CSDL (Bẫy đề thi kinh điển):**
  - **Cập nhật trì hoãn (연기 갱신 - Deferred Update):** Đề hỏi kỹ thuật nào **CHỈ DÙNG REDO, KHÔNG BAO GIỜ CẦN UNDO** $\rightarrow$ Chọn ngay **연기 갱신 기법**.
  - **Cập nhật tức thời (즉각 갱신 - Immediate Update):** Cần cả **REDO (cho giao dịch đã Commit)** VÀ **UNDO (cho giao dịch chưa Commit)**.
  - **Phân trang bóng (그림자 페이지 - Shadow Paging):** Đề hỏi kỹ thuật phục hồi nào **KHÔNG CẦN DÙNG TỆP NHẬT KÝ (Log file)** $\rightarrow$ Chọn **그림자 페이지**.
- **Độ mịn khóa (Locking Granularity):**
  - Khóa quy mô lớn (Toàn bộ CSDL, Bảng): Mức độ đồng thời (Concurrency) thấp, chi phí quản lý Overhead ít, không sợ Deadlock.
  - Khóa quy mô nhỏ (Bản ghi, Thuộc tính): Mức độ đồng thời cao, chi phí quản lý Overhead lớn, nguy cơ Deadlock cao.
- **Thao tác OLAP (Nhận diện bằng động từ hành động):**
  - Đi từ chi tiết lên khái quát hơn (Ngày $\rightarrow$ Tháng $\rightarrow$ Năm) $\rightarrow$ **Roll-up (드릴업)**.
  - Đi từ khái quát xuống chi tiết sâu hơn (Năm $\rightarrow$ Quý $\rightarrow$ Ngày) $\rightarrow$ **Drill-down (드릴다운)**.
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
| **Cập nhật trì hoãn** | **연기 갱신 (Deferred Update)** | Trong quá trình giao dịch thực thi, mọi thao tác sửa đổi dữ liệu **chỉ được ghi vào tệp nhật ký (Log)**, tuyệt đối chưa ghi vào CSDL vật lý trên đĩa. Chỉ khi giao dịch thực hiện lệnh `COMMIT` thành công, các thay đổi mới chính thức được ghi xuống đĩa CSDL. | **Chỉ thực hiện REDO**<br>*(Tuyệt đối KHÔNG cần UNDO)* |
| **Cập nhật tức thì** | **즉각 갱신 (Immediate Update)** | Trong quá trình giao dịch thực thi, mọi sửa đổi được **ghi đồng thời vào cả tệp nhật ký (Log) và CSDL vật lý** ngay lập tức. Nếu xảy ra sự cố trước khi Commit, CSDL đã chứa dữ liệu dở dang. | **Thực hiện cả REDO và UNDO**<br>*(REDO cho giao dịch đã Commit, UNDO cho giao dịch chưa Commit)* |
| **Điểm kiểm tra** | **검사점 (Checkpoint)** | Định kỳ hệ thống cưỡng chế ghi toàn bộ bộ đệm nhật ký và dữ liệu xuống đĩa vật lý rồi đánh dấu mốc 검사점. Khi sự cố xảy ra, bộ phục hồi chỉ cần quét nhật ký từ điểm Checkpoint gần nhất trở lại, **không phải duyệt lại toàn bộ Log từ đầu**, giúp tăng tốc độ phục hồi tối đa. | Tùy thuộc vào thời điểm giao dịch so với mốc Checkpoint |
| **Phân trang bóng** | **그림자 페이지 (Shadow Paging)** | Duy trì song song 2 bảng trang: **Bảng trang hiện tại (Current Page Table)** phục vụ các thao tác ghi dữ liệu của giao dịch, và **Bảng trang bóng (Shadow Page Table)** lưu trữ nguyên vẹn trạng thái CSDL ban đầu. Khi có sự cố, hệ thống chỉ việc trỏ lại bảng trang bóng; **hoàn toàn không cần tệp Log**. | Trỏ lại bảng trang bóng ban đầu |

#### 2. Kiểm soát đồng thời và Độ mịn khóa (Concurrency Control)
- **4 hiện tượng bất thường khi thực thi đồng thời không được kiểm soát:**
  1. **갱신 분실 (Lost Update - Mất cập nhật):** Hai giao dịch cùng cập nhật một trường dữ liệu; giao dịch chạy sau ghi đè lên kết quả của giao dịch chạy trước, làm mất mát hoàn toàn dữ liệu cập nhật của giao dịch đầu.
  2. **모순성 / 비일관성 (Inconsistency - Bất nhất quán):** Giao dịch thứ nhất đang tính toán tổng trên nhiều bản ghi thì giao dịch thứ hai xen vào sửa đổi một số bản ghi, dẫn đến kết quả tổng hợp bị sai lệch và không nhất quán.
  3. **연쇄 복귀 (Cascading Rollback - Thu hồi dây chuyền):** Giao dịch $T_1$ gặp sự cố phải hủy bỏ (`ROLLBACK`), kéo theo giao dịch $T_2$ (đã lỡ đọc dữ liệu dở dang của $T_1$) cũng phải `ROLLBACK`, gây phản ứng dây chuyền làm lãng phí tài nguyên hệ thống.
  4. **미완료 의존성 / Dirty Read (Đọc dữ liệu bẩn):** Giao dịch $T_2$ đọc một bản ghi do giao dịch $T_1$ sửa đổi nhưng chưa kịp `COMMIT`; ngay sau đó $T_1$ bị lỗi và `ROLLBACK` về giá trị cũ $\implies T_2$ đã dùng dữ liệu sai hoàn toàn.
- **Độ mịn khóa (로킹 단위 - Locking Granularity):**

| Cấp độ khóa | Mức độ đồng thời (Concurrency) | Chi phí quản lý khóa (Overhead) | Nguy cơ bế tắc (Deadlock) |
| :--- | :---: | :---: | :---: |
| **Khóa quy mô lớn**<br>(Database, Table) | **Rất thấp**<br>(Tiến trình khác phải xếp hàng đợi cả bảng) | **Rất ít**<br>(Chỉ cần quản lý vài chiếc khóa lớn) | **Cực thấp** |
| **Khóa quy mô nhỏ**<br>(Record, Field) | **Rất cao**<br>(Nhiều tiến trình cập nhật các dòng khác nhau) | **Rất lớn**<br>(Hệ thống phải lưu vết hàng triệu chiếc khóa) | **Rất cao** |

#### 3. Hệ sinh thái Dữ liệu lớn (Big Data) và Hadoop
- **HDFS (Hadoop Distributed File System):**
  - Hệ thống tệp phân tán của Hadoop cho phép lưu trữ các tệp dữ liệu khổng lồ (hàng Terabyte đến Petabyte) trên các cụm máy chủ phần cứng giá rẻ (Commodity Hardware).
  - Tệp tin được chia thành các khối (**Blocks**, mặc định 128MB); mỗi khối được **nhân bản mặc định 3 bản sao (3-way Replication)** và phân tán trên các máy chủ (DataNode) khác nhau trong cụm để bảo đảm khả năng chịu lỗi phần cứng.
- **MapReduce (Mô hình tính toán phân tán):**
  - **Pha Map (매핑):** Chia nhỏ dữ liệu đầu vào và chuyển đổi thành danh sách các cặp khóa-giá trị `(Key, Value)` độc lập trên từng máy con.
  - **Pha Shuffle & Sort (정렬/혼합):** Gom nhóm tất cả các giá trị có cùng một Khóa về chung một nút xử lý.
  - **Pha Reduce (리듀싱):** Tổng hợp và tính toán trên tập dữ liệu đã gom nhóm theo từng Khóa để sinh ra kết quả cuối cùng.

#### 4. Cơ sở dữ liệu NoSQL và Các phép toán OLAP
- **Bốn họ cơ sở dữ liệu NoSQL (Not Only SQL):**
  1. **Key-Value Store:** Lưu trữ cặp khóa-giá trị đơn giản, tốc độ đọc/ghi cực nhanh trên RAM (*Redis, Memcached*).
  2. **Document Store:** Lưu trữ dữ liệu dưới dạng tài liệu bán cấu trúc JSON/BSON (*MongoDB, CouchDB*).
  3. **Column-family Store:** Lưu trữ theo cột thay vì theo hàng, tối ưu cho việc truy vấn phân tích dữ liệu lớn (*HBase, Apache Cassandra*).
  4. **Graph Database:** Lưu trữ các thực thể dưới dạng Nút (Nodes) và Mối quan hệ cạnh (Edges), tối ưu cho mạng xã hội và phân tích đồ thị (*Neo4j*).
- **Năm phép toán phân tích trực tuyến đa chiều OLAP (OLAP Operations):**

| Phép toán OLAP | Tên tiếng Hàn & Anh | Bản chất thao tác phân tích dữ liệu |
| :--- | :--- | :--- |
| **Roll-up** | **롤업 (드릴업 - Drill-up)** | Thu gom, tổng hợp dữ liệu từ mức độ chi tiết lên mức độ bao quát tổng quan hơn (ví dụ: xem Doanh thu từ cấp Thành phố $\rightarrow$ Tỉnh $\rightarrow$ Quốc gia). |
| **Drill-down** | **드릴다운 (Drill-down)** | Mở rộng, đào sâu dữ liệu từ mức độ tổng quan xuống mức độ chi tiết cụ thể hơn (ví dụ: xem Doanh thu từ cấp Năm $\rightarrow$ Quý $\rightarrow$ Tháng $\rightarrow$ Ngày). |
| **Slicing** | **슬라이싱 (Slicing)** | Cắt một lát cắt cố định của khối dữ liệu đa chiều bằng cách chọn một giá trị duy nhất trên một chiều (ví dụ: lọc riêng dữ liệu của Năm 2026). |
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
- [ ] Hiểu kiến trúc Hadoop: HDFS chia khối nhân bản 3 bản sao; MapReduce gồm Map (chia cặp K-V) và Reduce (tổng hợp gom nhóm).
- [ ] Phân biệt 5 phép toán OLAP: Roll-up (lên khái quát), Drill-down (xuống chi tiết), Slicing (cắt lát 1 chiều), Dicing (cắt khối nhiều chiều), Pivoting (xoay trục).
