# 데이터 전환(ETL), 데이터 웨어하우스와 빅데이터 (Chuyển Đổi Dữ Liệu ETL, Data Warehouse và Big Data)

## 학습 목표 (Mục tiêu)
- Nắm vững quy trình chuyển đổi dữ liệu ETL: Trích xuất (`추출 / Extraction`), Biến đổi (`변환 / Transformation` - làm sạch dữ liệu, chuẩn hóa), và Nạp (`적재 / Loading`) qua vùng đệm Staging Area.
- Phân biệt sâu sắc giữa Kho dữ liệu doanh nghiệp (Data Warehouse / `데이터 웨어하우스`) và Chợ dữ liệu bộ phận (Data Mart / `데이터 마트`), cùng hai triết lý thiết kế Inmon (Top-down) vs Kimball (Bottom-up).
- Thuộc lòng 4 đặc tính Data Warehouse của Inmon: Định hướng chủ đề (`주제 지향성`), Tính tích hợp (`통합성`), Chuỗi thời gian (`시계열성`), và Phi bốc hơi (`비휘발성`).
- Làm chủ 5 thao tác phân tích đa chiều OLAP: Roll-up (`롤업`), Drill-down (`드릴다운`), Slicing (`슬라이싱`), Dicing (`다이싱`), và Pivoting (`피보팅`).
- Nắm vững đặc trưng 3V/5V của Big Data, phân biệt 4 dòng cơ sở dữ liệu NoSQL (Key-Value, Document, Column-family, Graph) và cấu trúc tệp truyền thống (SAM, ISAM, DAM).

## 핵심 키워드 (Từ khóa)
- 데이터 전환 (Chuyển đổi dữ liệu / ETL / 추출 Extraction, 변환 Transformation, 적재 Loading)
- 데이터 웨어하우스 (Kho dữ liệu / Data Warehouse / Inmon 4대 특성)
- 데이터 마트 (Chợ dữ liệu / Data Mart / 부서별 특화)
- OLAP (롤업 Roll-up, 드릴다운 Drill-down, 슬라이싱 Slicing, 다이싱 Dicing, 피보팅 Pivoting)
- ISAM (Prime Area, Index Area, Overflow Area)
- NoSQL (Key-Value, Document, Column-family, Graph)
- 빅데이터 (Big Data 3V: Volume, Velocity, Variety / 5V)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md](12-phan-vung-du-lieu-va-bao-mat-ma-hoa-csdl.md), chúng ta đã nắm vững các kỹ thuật phân vùng bảng lớn cùng các mô hình kiểm soát truy cập và thuật toán mã hóa dữ liệu.
- **Đang giải quyết gì (Current Problem):** Bài học này giải quyết việc trích xuất và làm sạch dữ liệu từ các hệ thống vận hành giao dịch (OLTP) phân tán để nạp vào hệ thống phân tích báo cáo (Data Warehouse, Data Mart, OLAP), đồng thời tổng kết hệ sinh thái Big Data, NoSQL và cấu trúc lưu trữ tệp.
- **Dùng đi đâu (Forward Handoff):** Bài học này khép lại toàn bộ 13 bài học master của Môn 3: Xây dựng Cơ sở dữ liệu. Toàn bộ logic thao tác dữ liệu, cấu trúc quan hệ và tư duy thiết kế hệ thống này sẽ làm nền tảng trực tiếp để bước sang Môn 4: Ứng dụng ngôn ngữ lập trình.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm chắc bảng so sánh Data Warehouse vs Data Mart, 4 đặc tính kinh điển của DW, 5 thao tác OLAP và bảng đối chiếu 3 bước ETL.
- Đọc TẦNG B để nắm chi tiết quy trình làm sạch dữ liệu trong ETL, triết lý Inmon vs Kimball, phân loại 4 kiến trúc NoSQL và 3 vùng của tệp ISAM.

---

## 데이터 전환(ETL), 데이터 웨어하우스와 빅데이터

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Sơ đồ luồng và Bảng quy trình 3 bước ETL (데이터 전환 프로세스)

Quy trình ETL chịu trách nhiệm thu thập dữ liệu từ các hệ thống vận hành giao dịch (OLTP), chuẩn hóa và nạp vào kho dữ liệu phục vụ phân tích:

```text
[ Nguồn OLTP phân tán ] ──> [ 1. 추출 (Extraction) ] ──> [ Staging Area ]
(Oracle, MySQL, File)              │
                                   ▼
                         [ 2. 변환 (Transformation) ] (Làm sạch, Khử trùng, Chuẩn hóa)
                                   │
                                   ▼
                         [ 3. 적재 (Loading) ] ──> [ Data Warehouse / Data Mart ]
```

| Bước trong ETL | Tên tiếng Hàn & Anh | Hoạt động kỹ thuật cốt lõi | Điểm bẫy thi cử |
| :---: | :--- | :--- | :--- |
| **E** | **추출 (Extraction)** | Trích xuất dữ liệu từ các nguồn không đồng nhất (RDBMS, Log, CSV, API). | Chỉ trích xuất phần dữ liệu thay đổi (CDC - Change Data Capture) để tối ưu tải. |
| **T** | **변환 (Transformation)** | **Làm sạch dữ liệu (Data Cleansing)**: Xử lý giá trị NULL, loại bỏ trùng lặp, chuyển đổi kiểu dữ liệu, chuẩn hóa đơn vị đo. | Là bước chiếm nhiều thời gian và công sức nhất trong toàn bộ quy trình ETL. |
| **L** | **적재 (Loading)** | Nạp dữ liệu hoàn chỉnh vào kho Data Warehouse hoặc Data Mart đích theo lô (Batch) hoặc thời gian thực. | Cần vô hiệu hóa tạm thời chỉ mục Index trong quá trình nạp lớn để tăng tốc độ. |

#### 2. Đối chiếu Data Warehouse (DW) vs Data Mart (DM)

| Tiêu chí so sánh | 데이터 웨어하우스 (Data Warehouse) | 데이터 마트 (Data Mart) |
| :--- | :--- | :--- |
| **Phạm vi dữ liệu** | **Toàn bộ doanh nghiệp / tổ chức (Enterprise-wide)** | **Chuyên biệt cho một phòng ban / bộ phận cụ thể** |
| **Chủ thể sử dụng** | Toàn bộ lãnh đạo, nhà phân tích dữ liệu toàn công ty | Nhân viên và quản lý nghiệp vụ (Marketing, Bán hàng, Tài chính) |
| **Quy mô dung lượng** | Rất lớn: Hàng trăm Terabyte đến nhiều Petabyte | Nhỏ hơn: Từ vài chục Gigabyte đến vài Terabyte |
| **Nguồn dữ liệu** | Thu thập từ tất cả các hệ thống nghiệp vụ nội bộ và bên ngoài | Trích xuất từ chính Data Warehouse hoặc nguồn chuyên biệt |
| **Triết lý xây dựng** | Mô hình **Inmon (Top-down)**: Xây dựng kho tập trung trước | Mô hình **Kimball (Bottom-up)**: Xây các Mart nghiệp vụ trước |

#### 3. Bốn đặc tính kinh điển của Data Warehouse (W.H. Inmon)

| Đặc tính | Tên tiếng Hàn & Anh | Định nghĩa kỹ thuật |
| :--- | :--- | :--- |
| **1. Định hướng chủ đề** | **주제 지향성 (Subject-Oriented)** | Dữ liệu được tổ chức xoay quanh các chủ đề kinh doanh cốt lõi (Khách hàng, Sản phẩm, Doanh thu) thay vì theo quy trình xử lý đơn thuần. |
| **2. Tính tích hợp** | **통합성 (Integrated)** | Dữ liệu từ nhiều nguồn không đồng nhất được đồng bộ hóa hoàn toàn về tên trường, mã danh mục, đơn vị đo lường và định dạng. |
| **3. Chuỗi thời gian** | **시계열성 (Time-Variant)** | Dữ liệu luôn gắn kèm nhãn thời gian và được lưu trữ lịch sử qua nhiều năm (5~10 năm) để phục vụ phân tích xu hướng và dự báo. |
| **4. Phi bốc hơi** | **비휘발성 (Non-Volatile)** | Dữ liệu sau khi nạp chỉ dùng cho mục đích tra cứu phân tích (**Read-only**), không cho phép thao tác sửa đổi hay xóa tùy tiện như hệ thống giao dịch. |

#### 4. Năm thao tác phân tích đa chiều OLAP (OLAP 연산)

| Thao tác OLAP | Tên tiếng Hàn | Hành vi phân tích dữ liệu | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| **Roll-up** | `롤업` | **Thu nhỏ độ chi tiết**, tăng mức tổng hợp lên cấp cao hơn | Xem dữ liệu từ Ngày $\rightarrow$ Tháng $\rightarrow$ Quý $\rightarrow$ Năm |
| **Drill-down** | `드릴다운` | **Mở rộng độ chi tiết**, đi sâu xuống các mức cụ thể hơn | Xem doanh thu từ Năm $\rightarrow$ Quý $\rightarrow$ Từng cửa hàng |
| **Slicing** | `슬라이싱` | Cắt lấy một lát cắt 2 chiều bằng cách cố định 1 chiều | Cắt riêng lát dữ liệu doanh thu của duy nhất 'Năm 2026' |
| **Dicing** | `다이싱` | Cắt lấy một khối lập phương con bằng cách chọn khoảng trên nhiều chiều | Lọc tổ hợp: 'Năm 2026' + 'Khu vực Hà Nội' + 'Mặt hàng Laptop' |
| **Pivoting** | `피보팅` | **Xoay chuyển các trục không gian** trong bảng báo cáo | Đổi chiều Thời gian từ Cột sang Hàng, Khu vực từ Hàng sang Cột |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)

- **Bẫy 1: Đặc tính 비휘발성 (Non-Volatile) của Data Warehouse:**
  - Khẳng định: "Data Warehouse thường xuyên thực hiện các câu lệnh UPDATE và DELETE để phản ánh trạng thái tức thời của nghiệp vụ" $\rightarrow$ **SAI HOÀN TOÀN**. Data Warehouse là hệ thống **chỉ đọc (Read-only)** và ghi nhận bổ sung, không sửa xóa dữ liệu lịch sử.
- **Bẫy 2: Phân biệt Roll-up vs Drill-down trong OLAP:**
  - Đi từ chi tiết lên tổng quan (khái quát hóa) là **Roll-up (롤업)**.
  - Đi từ tổng quan xuống chi tiết (cụ thể hóa) là **Drill-down (드릴다운)**.
- **Bẫy 3: Phân biệt Slicing vs Dicing:**
  - Cắt một lát 2 chiều bằng 1 tiêu chí $\rightarrow$ **Slicing (슬라이싱)**.
  - Cắt một khối nhỏ đa chiều kết hợp nhiều tiêu chí $\rightarrow$ **Dicing (다이싱)**.
- **Bẫy 4: Vùng tràn của tệp ISAM:**
  - Khi vùng Prime Area bị đầy, bản ghi chèn thêm sẽ được lưu tạm vào **Overflow Area (오버플로 구역)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết các bước làm sạch dữ liệu trong ETL (Data Cleansing)
- **Xử lý dữ liệu khuyết thiếu (Missing Data):** Điền giá trị mặc định, nội suy trung bình hoặc loại bỏ nếu trường đó là bắt buộc (như Khóa chính).
- **Chuẩn hóa định dạng (Format Standardization):** Đưa toàn bộ các kiểu ngày tháng khác nhau (`DD/MM/YYYY`, `YYYY-MM-DD`, `MM-DD-YYYY`) về một chuẩn duy nhất `YYYY-MM-DD`.
- **Hợp nhất mã danh mục:** Gộp các mã khác nhau nhưng cùng một nghĩa (ví dụ: `1`, `M`, `Male`, `Nam` đều chuyển thành `M`).
- **Khử trùng lặp (Deduplication):** Nhận diện khách hàng bị trùng lặp hồ sơ do mở tài khoản ở nhiều chi nhánh khác nhau bằng thuật toán so khớp chuỗi.

#### 2. Phân loại 4 dòng cơ sở dữ liệu NoSQL
1. **Key-Value Store:** Lưu trữ cặp Khóa - Giá trị đơn giản, tốc độ đọc ghi cực cao trên bộ nhớ RAM (Ví dụ: **Redis**, Memcached).
2. **Document Store:** Lưu trữ dữ liệu bán cấu trúc dưới dạng văn bản JSON, BSON; mỗi tài liệu có thể có cấu trúc thuộc tính linh hoạt (Ví dụ: **MongoDB**, CouchDB).
3. **Column-family Store:** Lưu trữ dữ liệu theo các nhóm cột mở rộng linh hoạt, tối ưu hóa cho dữ liệu lớn phân tán hàng tỷ dòng (Ví dụ: **HBase**, **Cassandra**).
4. **Graph Store:** Lưu trữ các nút (Node), cạnh (Edge) và thuộc tính (Property), tối ưu cho truy vấn các mạng quan hệ phức tạp như mạng xã hội, phát hiện gian lận tài chính (Ví dụ: **Neo4j**).

#### 3. Cấu trúc 3 vùng của tệp tuần tự có chỉ mục (ISAM)
- `Prime Area (기본 구역)`: Vùng lưu trữ các bản ghi dữ liệu thực tế được sắp xếp theo thứ tự tuần tự của khóa.
- `Index Area (색인 구역)`: Hệ thống chỉ mục phân cấp nhiều tầng gồm: Track Index $\rightarrow$ Cylinder Index $\rightarrow$ Master Index.
- `Overflow Area (오버플로 구역)`: Vùng đệm chứa các bản ghi bị tràn khi vùng Prime Area của track tương ứng không còn chỗ trống.

#### 4. Đặc trưng 3V / 5V của Big Data
- **3V cơ bản:**
  - `Volume (Quy mô dữ liệu)`: Khối lượng dữ liệu khổng lồ từ Terabyte đến Exabyte.
  - `Velocity (Tốc độ)`: Tốc độ sinh ra và xử lý dữ liệu theo thời gian thực cực nhanh.
  - `Variety (Đa dạng)`: Đa dạng cấu trúc từ có cấu trúc (RDBMS), bán cấu trúc (JSON, XML) đến phi cấu trúc (Video, Âm thanh, Hình ảnh).
- **5V mở rộng:** Bổ sung thêm `Veracity (Tính xác thực / độ tin cậy)` và `Value (Giá trị nghiệp vụ mang lại)`.

---

### 복습 체크리스트
- [ ] Trình bày 3 bước của quy trình ETL: 추출 (Extraction), 변환 (Transformation - làm sạch dữ liệu), 적재 (Loading).
- [ ] Phân biệt được sự khác nhau giữa Data Warehouse (toàn doanh nghiệp) và Data Mart (chuyên biệt từng bộ phận).
- [ ] Nằm lòng 4 đặc tính Data Warehouse của Inmon: `주제 지향성` (Định hướng chủ đề), `통합성` (Tính tích hợp), `시계열성` (Chuỗi thời gian), `비휘발성` (Phi bốc hơi).
- [ ] Phân biệt thành thạo 5 thao tác OLAP: Roll-up (lên tổng quát), Drill-down (xuống chi tiết), Slicing (cắt lát), Dicing (cắt khối con), Pivoting (xoay trục).
- [ ] Nhớ cấu trúc 3 vùng của tệp ISAM: Prime Area, Index Area, Overflow Area.
- [ ] Phân biệt 4 dòng cơ sở dữ liệu NoSQL: Key-Value, Document, Column-family, Graph Store.
