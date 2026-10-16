# 데이터 파티셔닝과 데이터베이스 보안·암호화 (Phân Vùng Dữ Liệu và Bảo Mật, Mã Hóa CSDL)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất Phân vùng (`파티셔닝` / Partitioning) và phân biệt 5 phương pháp phân chia: Phân vùng phạm vi (`범위 분할` / Range), Phân vùng băm (`해시 분할` / Hash), Phân vùng danh sách (`목록 분할` / List), Phân vùng kết hợp (`조합 분할` / Composite), và Phân vùng xoay vòng (`라운드 로빈` / Round Robin - không cần Primary Key).
- Hiểu rõ cơ chế cắt tỉa phân vùng (Partition Pruning) giúp giảm thiểu thao tác I/O đĩa và kỹ thuật quản trị vòng đời dữ liệu bằng lệnh `DROP PARTITION`.
- Làm chủ 4 phương thức kiến trúc triển khai mã hóa CSDL: Phương thức API (`API 방식`), Phương thức cắm thêm Plug-in (`Plug-in 방식`), Phương thức mã hóa trong suốt TDE (`TDE 방식` - cấp độ Tablespace/Column), và Phương thức phần cứng chuyên dụng / Hỗn hợp (`Hybrid / Appliance 방식`).
- So sánh toàn diện 3 mô hình kiểm soát truy cập: DAC (theo quyết định chủ sở hữu), MAC (theo cấp bậc an ninh hệ thống), và RBAC (theo vai trò và chức danh trong tổ chức).
- Phân tích đối trọng hai mô hình bảo mật kinh điển: Bell-LaPadula (bảo vệ tính bí mật: No Read Up, No Write Down) và Biba (bảo vệ tính toàn vẹn: No Read Down, No Write Up).
- So sánh mã hóa đối xứng vs mã hóa bất đối xứng về số lượng khóa, tốc độ, độ phức tạp quản lý và nhận diện các thuật toán tiêu biểu (SEED, ARIA, AES vs RSA, ECC).

## 핵심 키워드 (Từ khóa)
- 파티셔닝 (Phân vùng dữ liệu / Partitioning / 범위 Range, 해시 Hash, 목록 List, 조합 Composite, 라운드 로빈 Round Robin)
- 파티션 프루닝 (Cắt tỉa phân vùng / Partition Pruning / I/O 절감)
- 데이터베이스 암호화 방식 (Kiến trúc mã hóa CSDL: API, Plug-in, TDE, Hybrid)
- 컬럼 암호화 vs 테이블스페이스 암호화 (Mã hóa mức Cột vs Mã hóa Tablespace)
- 접근 통제 (Kiểm soát truy cập / DAC 임의, MAC 강제, RBAC 역할기반)
- 벨-라파듈라 모델 (Bell-LaPadula / BLP / 기밀성 / No Read Up, No Write Down)
- 비바 모델 (Biba / 무결성 / No Read Down, No Write Up)
- 대칭키 vs 비대칭키 (Mã hóa đối xứng SEED, ARIA vs Bất đối xứng RSA, ECC)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md), chúng ta đã nắm vững kiến trúc phân tán trên mạng diện rộng với các tính chất trong suốt và giao thức cam kết 2 pha 2PC.
- **Đang giải quyết gì (Current Problem):** Khi dữ liệu tích lũy lên hàng chục triệu bản ghi trên một nút lưu trữ, hiệu năng đọc/ghi suy giảm nghiêm trọng và nguy cơ lộ lọt thông tin tăng cao. Bài học này giải quyết việc xé nhỏ bảng dữ liệu qua **Phân vùng (Partitioning)** và thiết lập lá chắn bảo vệ thông qua **Kiểm soát truy cập và 4 phương thức Mã hóa CSDL**.
- **Dùng đi đâu (Forward Handoff):** Các phân vùng dữ liệu và chuẩn mã hóa này sẽ là đầu vào để xây dựng các đường ống chuyển đổi ETL, kho dữ liệu lớn Data Warehouse / OLAP và hệ sinh thái Big Data ở bài học tiếp theo [13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md](13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md).

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc lòng các bẫy đề thi hay hỏi nhất: 4 phương thức mã hóa CSDL (API vs Plug-in vs TDE), Round Robin không cần Primary Key, câu thần chú Bell-LaPadula (Bí mật) vs Biba (Toàn vẹn), và nhận diện 2 thuật toán quốc gia Hàn Quốc (SEED và ARIA là mã hóa khối đối xứng).
- Đọc TẦNG B để hiểu sâu công thức tính số lượng khóa trong mã hóa đối xứng $\frac{N(N-1)}{2}$, cơ chế Partition Pruning của bộ tối ưu hóa truy vấn và mô hình Clark-Wilson.

---

## 데이터 파티셔닝과 데이터베이스 보안·암호화

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng phân loại 5 phương pháp phân vùng (파티셔닝 방식)

| Phương pháp | Tên tiếng Hàn & Anh | Tiêu chí phân chia | Điểm lưu ý thi cử |
| :--- | :--- | :--- | :--- |
| **Phân vùng phạm vi** | **범위 분할 (Range)** | Giá trị dải số hoặc chuỗi thời gian liên tục | Thường dùng cho dữ liệu **Ngày tháng (ngày, tháng, năm)** |
| **Phân vùng băm** | **해시 분할 (Hash)** | Áp dụng hàm băm lên cột chỉ định | Phân bổ đều dữ liệu; tối ưu cho cột có phân bố đồng đều (như Mã khách hàng) |
| **Phân vùng danh sách** | **목록 분할 (List)** | Danh sách giá trị rời rạc định nghĩa trước | Phân chia theo mã danh mục cố định (như Khu vực, Quốc gia) |
| **Phân vùng kết hợp** | **조합 분할 (Composite)** | Phân vùng 2 tầng: Cấp 1 Range, Cấp 2 Hash/List | Dùng cho bảng siêu lớn (ví dụ: phân vùng Tháng sau đó băm theo ID) |
| **Phân vùng xoay vòng**| **라운드 로빈 (Round Robin)** | Phân phối luân phiên từng bản ghi theo lượt | **Hoàn toàn không cần Khóa chính (Primary Key)** |

#### 2. Bốn phương thức triển khai mã hóa CSDL (데이터베이스 암호화 4대 구축 방식)

| Phương thức triển khai | Vị trí thực thi mã hóa / giải mã | Ưu điểm kỹ thuật | Nhược điểm / Đánh đổi |
| :--- | :--- | :--- | :--- |
| **1. API 방식** (Kiểu API tầng ứng dụng) | Thực thi tại **Máy chủ Ứng dụng (App Server)** thông qua thư viện mã hóa API. | Dữ liệu truyền trên mạng mạng đã được mã hóa an toàn, giảm tải CPU cho DB Server. | **Bắt buộc phải sửa mã nguồn ứng dụng** để gọi hàm mã hóa/giải mã. |
| **2. Plug-in 방식** (Kiểu module cắm thêm) | Thực thi tại **Máy chủ CSDL (DB Server)** bằng module Plug-in cài đặt vào DBMS. | **Không cần sửa đổi mã nguồn ứng dụng**, cài đặt và quản trị tập trung tại CSDL. | Tiêu tốn tài nguyên CPU và bộ nhớ của DB Server khi có nhiều truy vấn mã hóa. |
| **3. TDE 방식** (Mã hóa trong suốt / Tablespace) | Tích hợp sẵn trong nhân DBMS, tự động mã hóa cấp **Tablespace** hoặc **Cột**. | **Hoàn toàn trong suốt với ứng dụng**, hiệu năng cực cao nhờ lệnh tăng tốc phần cứng (AES-NI). | Chỉ mã hóa khi ghi xuống đĩa; dữ liệu nạp vào RAM máy chủ CSDL ở dạng giải mã. |
| **4. Hybrid / Appliance** (Phương thức hỗn hợp) | Kết hợp API và Plug-in, hoặc sử dụng **thiết bị phần cứng chuyên dụng** riêng biệt. | Tối ưu hóa hiệu năng và bảo mật theo từng loại dữ liệu, quản lý khóa độc lập. | Chi phí đầu tư phần cứng cao, kiến trúc mạng phức tạp hơn. |

#### 3. Bảng phân biệt mô hình an ninh: Bell-LaPadula vs Biba

```text
[ Bell-LaPadula (BLP) 모델 ]                     [ Biba (비바) 모델 ]
  • 핵심 목표: 기밀성 (Confidentiality)             • 핵심 목표: 무결성 (Integrity)
  • No Read Up   (NRU: 상위 등급 읽기 금지)        • No Read Down (NRD: 하위 등급 읽기 금지)
  • No Write Down (NWD: 하위 등급 쓰기 금지)       • No Write Up   (NWU: 상위 등급 쓰기 금지)
```

| Tiêu chí | Bell-LaPadula (BLP) | Biba Model |
| :--- | :--- | :--- |
| **Mục tiêu tối thượng** | **Tính bí mật (`기밀성` / Confidentiality)** | **Tính toàn vẹn (`무결성` / Integrity)** |
| **Quy tắc Đọc (Read)** | **No Read Up (NRU)**: Cấm đọc tài liệu cấp cao hơn | **No Read Down (NRD)**: Cấm đọc dữ liệu cấp thấp hơn |
| **Quy tắc Ghi (Write)** | **No Write Down (NWD)**: Cấm ghi xuống tài liệu cấp thấp hơn | **No Write Up (NWU)**: Cấm ghi lên dữ liệu cấp cao hơn |

#### 4. So sánh mã hóa: Đối xứng vs Bất đối xứng

| Tiêu chí | Mã hóa đối xứng (`대칭키 암호` / 비밀키) | Mã hóa bất đối xứng (`비대칭키 암호` / 공개키) |
| :--- | :--- | :--- |
| **Khóa giải mã** | **Khóa mã hóa = Khóa giải mã** (Dùng chung 1 khóa bí mật) | **Khóa mã hóa $\neq$ Khóa giải mã** (Cặp Public Key & Private Key) |
| **Tốc độ xử lý** | **Rất nhanh**, tối ưu cho dữ liệu dung lượng lớn | **Chậm**, tốn nhiều chi phí xử lý toán học |
| **Số lượng khóa** | $N$ người cần: $\mathbf{\frac{N(N-1)}{2}}$ khóa | $N$ người cần: $\mathbf{2N}$ khóa |
| **Mẹo ghi nhớ** | **대-개-빠-관** (Đại diện đối xứng = Cá nhân = Nhanh = Khó quản lý) | Khóa công khai = Dễ quản lý khóa, phân phối an toàn |
| **Thuật toán tiêu biểu**| DES, 3DES, AES, **SEED (Hàn Quốc)**, **ARIA (Hàn Quốc)** | RSA, DSA, ECC, Diffie-Hellman |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)

- **Bẫy 1: Phương thức mã hóa cần sửa code ứng dụng:**
  - *Câu hỏi:* "Phương thức triển khai mã hóa CSDL nào đòi hỏi phải chỉnh sửa mã nguồn của chương trình ứng dụng?"
  - *Đáp án đúng:* **API 방식**. Các phương thức Plug-in và TDE hoàn toàn không cần sửa mã nguồn ứng dụng.
- **Bẫy 2: Phân vùng không cần Khóa chính:**
  - Phương pháp phân vùng duy nhất **không cần Primary Key** là **라운드 로빈 분할 (Round Robin)**.
- **Bẫy 3: Phân biệt Bell-LaPadula và Biba:**
  - Nhắc tới bảo vệ **기밀성 (Tính bí mật)** $\rightarrow$ **Bell-LaPadula** (No Read Up, No Write Down).
  - Nhắc tới bảo vệ **무결성 (Tính toàn vẹn)** $\rightarrow$ **Biba** (No Read Down, No Write Up).
- **Bẫy 4: Thuật toán mã hóa quốc gia Hàn Quốc:**
  - Cả hai thuật toán **SEED** và **ARIA** đều thuộc nhóm **대칭키 블록 암호 (Mã hóa khối đối xứng)**, độ dài khối chuẩn 128-bit.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế Cắt tỉa phân vùng (Partition Pruning) và Quản trị vòng đời
- **Partition Pruning:** Khi câu truy vấn có điều kiện `WHERE NgayTao >= '2026-01-01'`, Optimizer sẽ tự động nhận diện và chỉ đọc đúng tệp dữ liệu của phân vùng Năm 2026, loại bỏ hoàn toàn các phân vùng của các năm trước ra khỏi phạm vi đọc đĩa.
- **Quản trị vòng đời (Data Lifecycle):** Xóa phân vùng cũ bằng `ALTER TABLE GIAO_DICH DROP PARTITION p_2021;` giải phóng không gian đĩa tức thì trong 1 giây mà không phát sinh lượng log khổng lồ như lệnh `DELETE`.

#### 2. Phân tích sâu 2 phạm vi mã hóa CSDL: Mã hóa Cột vs Mã hóa Tablespace

##### 2.1. Mã hóa mức Cột (Column-level Encryption)
- **Cơ chế:** Chỉ lựa chọn những cột chứa thông tin cực kỳ nhạy cảm để mã hóa (ví dụ: Số CCCD/CMND, Số thẻ tín dụng, Mật khẩu tài khoản).
- **Ưu điểm:** Dung lượng dữ liệu bị mã hóa ít, giảm thiểu tối đa chi phí tiêu tốn tài nguyên xử lý so với mã hóa toàn bộ cơ sở dữ liệu.
- **Hạn chế:** Các cột bị mã hóa sẽ khó khăn trong việc tạo chỉ mục Index và tìm kiếm theo khoảng (Range Search).

##### 2.2. Mã hóa Tablespace (Tablespace-level / TDE)
- **Cơ chế:** Toàn bộ tập tin vật lý chứa không gian bảng (Tablespace) được mã hóa tự động khi ghi xuống ổ cứng và tự động giải mã khi nạp vào bộ nhớ đệm RAM (Buffer Pool) của hệ quản trị CSDL.
- **Ưu điểm:** Hoàn toàn trong suốt với các ứng dụng, các câu lệnh truy vấn SQL không hề thay đổi, các chỉ mục Index xây dựng trên bảng vẫn hoạt động bình thường với hiệu năng tối ưu.
- **Bảo vệ:** Chống lại các nguy cơ đánh cắp ổ cứng vật lý, sao chép trái phép file sao lưu (`.bak`, `.dmp`) hoặc đọc lén file dữ liệu từ hệ điều hành.

#### 3. Ba mô hình kiểm soát truy cập (접근 통제 모델)
1. **DAC (임의 접근통제 / Discretionary Access Control):** Cấp quyền dựa trên quyết định cá nhân của **chủ sở hữu đối tượng dữ liệu (Data Owner)** qua lệnh `GRANT` và `REVOKE`.
2. **MAC (강제 접근통제 / Mandatory Access Control):** Cấp quyền tự động dựa trên việc so sánh **nhãn bảo mật (Security Clearance)** của người dùng và mức độ mật của dữ liệu do hệ thống quy định.
3. **RBAC (역할기반 접근통제 / Role-Based Access Control):** Cấp quyền cho các **Vai trò (Roles)** trong doanh nghiệp, sau đó phân bổ người dùng vào các vai trò tương ứng.

---

### 복습 체크리스트
- [ ] Phân biệt 5 phương pháp phân vùng: Range (khoảng liên tục), Hash (phân bổ đều), List (danh mục rời rạc), Composite (kết hợp 2 tầng), Round Robin (luân phiên, không cần PK).
- [ ] Giải thích nguyên lý hoạt động và lợi ích giảm thiểu I/O của Partition Pruning.
- [ ] Nắm vững 4 phương thức triển khai mã hóa CSDL: API (sửa code app), Plug-in (chạy trong DB, không sửa app), TDE (trong suốt mức tablespace/cột), Hybrid.
- [ ] Phân biệt Mã hóa mức Cột (tiết kiệm, mã hóa dữ liệu nhạy cảm) vs Mã hóa Tablespace (trong suốt, mã hóa toàn bộ file đĩa).
- [ ] Nằm lòng quy tắc Bell-LaPadula (No Read Up, No Write Down cho Bí mật) và Biba (No Read Down, No Write Up cho Toàn vẹn).
- [ ] Thuộc công thức tính số lượng khóa trong mã hóa đối xứng $\frac{N(N-1)}{2}$ và câu thần chú `대-개-빠-관`.
- [ ] Ghi nhớ SEED và ARIA là 2 thuật toán mã hóa khối đối xứng của Hàn Quốc.
