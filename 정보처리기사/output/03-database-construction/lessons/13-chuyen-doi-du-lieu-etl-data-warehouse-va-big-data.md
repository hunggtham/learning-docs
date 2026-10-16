# 데이터 전환(ETL), 데이터 웨어하우스와 빅데이터 (Chuyển Đổi Dữ Liệu ETL, Data Warehouse và Big Data)

## 학습 목표
- Nắm vững 3 cấu trúc tệp truyền thống: Tệp tuần tự (`순차 파일 / SAM`), Tệp tuần tự có chỉ mục (`색인 순차 파일 / ISAM` gồm 3 vùng Prime, Index, Overflow), và Tệp trực tiếp (`직접 파일 / DAM`). Phân biệt ACL (gắn vào tệp) và Capability List (gắn vào người dùng).
- Phân tích sâu quy trình chuyển đổi ETL: Trích xuất (`추출 / Extraction`), Biến đổi (`변환 / Transformation` - làm sạch dữ liệu), và Nạp (`적재 / Loading`); cùng vòng đời 5 trạng thái quản lý lỗi dữ liệu.
- Thuộc lòng 4 đặc tính Data Warehouse của Inmon: Định hướng chủ đề (`주제 지향성`), Tính tích hợp (`통합성`), Chuỗi thời gian (`시계열성`), và Phi bốc hơi (`비휘발성`); phân biệt 5 thao tác OLAP (Roll-up, Drill-down, Slicing, Dicing, Pivoting).
- Nắm vững đặc trưng 3V/5V của Big Data và phân biệt 4 dòng cơ sở dữ liệu NoSQL: Key-Value, Document, Column-family, Graph.
- So sánh SQL Mapper (MyBatis) và ORM (JPA); thuộc lòng trật tự ưu tiên toán tử trong SQL (`( )` > Toán học > Quan hệ > `NOT` > `AND` > `OR`).

## 핵심 키워드
- 데이터 전환 (Chuyển đổi dữ liệu / ETL / 추출 Extraction, 변환 Transformation, 적재 Loading)
- 데이터 웨어하우스 (Kho dữ liệu / Data Warehouse / 주제 지향성, 통합성, 시계열성, 비휘발성)
- OLAP (롤업 Roll-up, 드릴다운 Drill-down, 슬라이싱 Slicing, 다이싱 Dicing, 피보팅 Pivoting)
- ISAM (Prime Area, Index Area, Overflow Area)
- NoSQL (Key-Value, Document, Column-family, Graph)
- SQL Mapper & ORM (MyBatis, JPA)
- 연산자 우선순위 (Operator Precedence / NOT > AND > OR)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md), chúng ta đã nắm vững các kỹ thuật phân vùng bảng lớn cùng các mô hình kiểm soát truy cập và thuật toán mã hóa dữ liệu.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc trích xuất và chuẩn hóa dữ liệu từ các hệ thống vận hành giao dịch (OLTP) phân mảnh để nạp vào hệ thống phân tích báo cáo (OLAP), đồng thời tổng kết hệ sinh thái Big Data, NoSQL và cầu nối lập trình ứng dụng (MyBatis, ORM).
- **Dùng đi đâu (Forward Handoff):** Bài học này khép lại toàn bộ 13 bài học master của Môn 3: Xây dựng Cơ sở dữ liệu. Toàn bộ logic thao tác dữ liệu và thứ tự ưu tiên toán tử này sẽ làm nền tảng trực tiếp để bước sang Môn 4: Lập trình ứng dụng (C, Java, Python).

## 읽는 방법
- Đọc TẦNG A để nắm chắc thứ tự ưu tiên toán tử (`NOT` > `AND` > `OR`), 4 đặc tính kinh điển của Data Warehouse, 3 vùng của ISAM, và bảng phân biệt 5 thao tác OLAP.
- Đọc TẦNG B để nắm chi tiết quy trình làm sạch dữ liệu trong ETL, phân loại 4 kiến trúc NoSQL và so sánh sự khác nhau giữa SQL Mapper và ORM.

---

## 데이터 전환(ETL), 데이터 웨어하우스와 빅데이터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại cấu trúc tệp truyền thống
| Cấu trúc tệp | Tên tiếng Hàn & Anh | Cơ chế lưu trữ & truy cập | Đặc trưng kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Tệp tuần tự** | `순차 파일` (SAM) | Ghi nối tiếp theo trật tự logic trên băng từ hoặc đĩa | Tối ưu xử lý hàng loạt, không thể tìm kiếm ngẫu nhiên |
| **Tệp tuần tự có chỉ mục** | `색인 순차 파일` (ISAM) | Lưu tuần tự kèm bảng chỉ mục hỗ trợ cả tuần tự và ngẫu nhiên | **Gồm 3 vùng: Prime, Index, Overflow** |
| **Tệp trực tiếp** | `직접 파일` (DAM) | Dùng hàm băm (Hash) tính toán địa chỉ vật lý từ Khóa | Tốc độ truy xuất nhanh nhất, cần cơ chế giải quyết xung đột |

#### 2. Sơ đồ luồng và Bảng quy trình 3 bước ETL (데이터 전환)
```
[ 소스 레거시 시스템 ] ──(추출: Extraction)──> [ 스테이징 영역 ] ──(변환: Transformation)──> [ 적재: Loading ] ──> [ 데이터 웨어하우스 ]
(RDBMS, CSV, Log)                            (Data Cleansing, 표준화)                      (신규 대상 DB)
```

| Bước | Tên tiếng Hàn & Anh | Hoạt động kỹ thuật chính |
| :---: | :--- | :--- |
| **E** | **추출 (Extraction)** | Trích xuất dữ liệu từ các hệ thống nguồn không đồng nhất (RDBMS, Log, File) |
| **T** | **변환 (Transformation)** | **Làm sạch dữ liệu (Data Cleansing)**: xử lý NULL, định dạng chuẩn hóa, khử trùng lặp |
| **L** | **적재 (Loading)** | Nạp hàng loạt dữ liệu đã làm sạch vào kho Data Warehouse hoặc Data Mart |

#### 3. 4 đặc tính kinh điển của Data Warehouse (Inmon)
| Đặc tính | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật |
| :--- | :--- | :--- |
| **Định hướng chủ đề** | **주제 지향성 (Subject-Oriented)** | Tổ chức dữ liệu xoay quanh các chủ thể kinh doanh cốt lõi (Khách hàng, Sản phẩm) |
| **Tính tích hợp** | **통합성 (Integrated)** | Chuẩn hóa toàn bộ tên trường, mã danh mục, đơn vị đo lường từ các nguồn rời rạc |
| **Chuỗi thời gian** | **시계열성 (Time-Variant)** | Lưu trữ dữ liệu lịch sử theo từng mốc thời gian trong nhiều năm để phân tích xu hướng |
| **Phi bốc hơi** | **비휘발성 (Non-Volatile)** | Dữ liệu chỉ nạp vào để tra cứu phân tích (**Read-only**), không sửa xóa tùy tiện |

#### 4. 5 thao tác phân tích đa chiều OLAP
| Thao tác | Tên tiếng Hàn | Hành vi phân tích | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| **Roll-up** | `롤업` | Đi từ chi tiết lên mức tổng hợp cao hơn | Ngày $\rightarrow$ Tháng $\rightarrow$ Năm |
| **Drill-down** | `드릴다운` | Đi từ mức tổng hợp sâu xuống chi tiết cụ thể | Năm $\rightarrow$ Quý $\rightarrow$ Cửa hàng |
| **Slicing** | `슬라이싱` | Cắt một lát 2 chiều từ khối đa chiều | Lọc riêng dữ liệu của 'Năm 2026' |
| **Dicing** | `다이싱` | Cắt một khối lập phương nhỏ từ nhiều chiều | Lọc tổ hợp: 'Năm 2026 + Hà Nội + Laptop' |
| **Pivoting** | `피보팅` | Đảo trục hàng và cột trong báo cáo | Chuyển Thời gian sang hàng, Khu vực sang cột |

#### 5. Bảng ưu tiên toán tử SQL (Operator Precedence)
| Thứ tự | Loại toán tử | Các toán tử cụ thể |
| :---: | :--- | :--- |
| **1** | Dấu ngoặc đơn | `( )` |
| **2** | Toán tử số học | Nhân, Chia (`*`, `/`) $\rightarrow$ Cộng, Trừ (`+`, `-`) |
| **3** | Nối chuỗi | `\|\|` |
| **4** | Toán tử so sánh / quan hệ | `=`, `<>`, `<`, `>`, `LIKE`, `IN`, `BETWEEN`, `IS NULL` |
| **5** | **Toán tử logic NOT** | `NOT` (Ưu tiên cao nhất trong toán tử logic) |
| **6** | **Toán tử logic AND** | `AND` (Luôn được tính trước OR) |
| **7** | **Toán tử logic OR** | `OR` (Được tính cuối cùng) |

#### 6. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Độ ưu tiên NOT > AND > OR:**
  - Biểu thức `WHERE A OR B AND C` được động cơ CSDL xử lý là `A OR (B AND C)`, không tính từ trái qua phải.
- **Bẫy 2: Đặc tính Data Warehouse:**
  - Khẳng định: "Data Warehouse thường xuyên cập nhật và xóa dòng để phản ánh dữ liệu mới nhất" $\rightarrow$ **SAI**. Data Warehouse mang tính chất **비휘발성 (Non-Volatile)**, chỉ đọc và nạp thêm.
- **Bẫy 3: 3 vùng của tệp ISAM:**
  - Khi vùng Prime Area bị đầy, bản ghi chèn thêm sẽ được đưa vào **오버플로 구역 (Overflow Area)**.
- **Bẫy 4: Thao tác OLAP:**
  - Đi từ chi tiết lên tổng quan là **Roll-up (롤업)**; từ tổng quan xuống chi tiết là **Drill-down (드릴다운)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cấu trúc 3 vùng của tệp ISAM
- `Prime Area (기본 구역)`: Vùng lưu trữ các bản ghi dữ liệu thực tế được sắp xếp theo thứ tự của khóa.
- `Index Area (색인 구역)`: Hệ thống chỉ mục phân cấp nhiều tầng gồm: Track Index $\rightarrow$ Cylinder Index $\rightarrow$ Master Index.
- `Overflow Area (오버플로 구역)`: Vùng đệm chứa các bản ghi bị tràn khi vùng Prime Area của track tương ứng không còn chỗ trống.

#### 2. Kiểm soát truy cập tệp: ACL vs Capability List
- **접근 제어 리스트 (Access Control List / ACL):** Tiếp cận theo hướng đối tượng (tệp). Mỗi tệp lưu trữ một danh sách các người dùng kèm theo quyền tương ứng (Read, Write, Execute).
- **권한 리스트 (Capability List):** Tiếp cận theo hướng chủ thể (người dùng). Mỗi người dùng sở hữu một "thẻ thông hành" liệt kê các tệp mà mình được phép truy cập.

#### 3. Vòng đời quản lý lỗi dữ liệu chuyển đổi (오류 데이터 정제 주기)
$$\text{Open (Phát hiện lỗi)} \longrightarrow \text{Assigned (Giao việc)} \longrightarrow \text{Fixed (Đã sửa)} \longrightarrow \text{Closed (Đóng lỗi)}$$
- `Deferred (Tạm hoãn)`: Trạng thái dành cho các lỗi có độ ưu tiên thấp hoặc chưa đủ tài nguyên để sửa trong phiên làm việc hiện tại, chuyển sang đợt bảo trì kế tiếp.

#### 4. Phân loại 4 dòng cơ sở dữ liệu NoSQL
- `Key-Value Store`: Lưu cặp khóa - giá trị đơn giản, tốc độ đọc ghi cực cao (Ví dụ: **Redis**, Memcached).
- `Document Store`: Lưu tài liệu bán cấu trúc dưới dạng JSON, BSON (Ví dụ: **MongoDB**, CouchDB).
- `Column-family Store`: Lưu trữ theo họ cột mở rộng linh hoạt cho dữ liệu lớn phân tán (Ví dụ: **HBase**, **Cassandra**).
- `Graph Store`: Lưu nút (Node) và cạnh (Edge) tối ưu truy vấn mạng xã hội, đồ thị tri thức (Ví dụ: **Neo4j**).

#### 5. Đối chiếu SQL Mapper vs ORM
- **SQL 매퍼 (SQL Mapper - MyBatis):** Hướng câu lệnh SQL; lập trình viên tự viết câu lệnh SQL trong file XML; dễ dàng tinh chỉnh tối ưu câu lệnh phức tạp nhưng gắn chặt với hệ CSDL cụ thể.
- **ORM (Object-Relational Mapping - JPA/Hibernate):** Hướng đối tượng; ánh xạ tự động Class thành Table; tự sinh câu lệnh SQL độc lập với hệ quản trị CSDL; tăng tốc độ phát triển nhưng khó tối ưu câu lệnh báo cáo phức tạp.

---

### 복습 체크리스트
- [ ] Phân biệt 3 cấu trúc tệp truyền thống: SAM (tuần tự), ISAM (3 vùng: Prime, Index, Overflow), DAM (hàm băm).
- [ ] Phân biệt ACL (gắn vào tệp) và Capability List (gắn vào người dùng).
- [ ] Trình bày 3 bước của quy trình ETL: 추출 (Extraction), 변환 (Transformation), 적재 (Loading).
- [ ] Nằm lòng 4 đặc tính Data Warehouse của Inmon: `주제 지향성`, `통합성`, `시계열성`, `비휘발성`.
- [ ] Phân biệt 5 thao tác OLAP: Roll-up, Drill-down, Slicing, Dicing, Pivoting.
- [ ] Nhớ thứ tự ưu tiên toán tử: `( )` > Toán học > Quan hệ > NOT > AND > OR.
- [ ] Phân biệt 4 dòng NoSQL (Key-Value, Document, Column-family, Graph) và MyBatis vs ORM.
