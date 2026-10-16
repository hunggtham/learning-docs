# 데이터 파티셔닝과 데이터베이스 보안·암호화 (Phân Vùng Dữ Liệu và Bảo Mật, Mã Hóa CSDL)

## 학습 목표
- Nắm vững bản chất Phân vùng (`파티셔닝 / Partitioning`) và phân biệt 5 phương pháp phân chia: Phân vùng phạm vi (`범위 분할 / Range`), Phân vùng băm (`해시 분할 / Hash`), Phân vùng danh sách (`목록 분할 / List`), Phân vùng kết hợp (`조합 분할 / Composite`), và Phân vùng xoay vòng (`라운드 로빈 / Round Robin` - không cần Primary Key).
- Hiểu rõ cơ chế cắt tỉa phân vùng (Partition Pruning) giúp giảm thiểu thao tác I/O đĩa và kỹ thuật quản trị vòng đời dữ liệu bằng lệnh `DROP PARTITION`.
- So sánh toàn diện 3 mô hình kiểm soát truy cập: DAC (theo quyết định chủ sở hữu), MAC (theo cấp bậc an ninh hệ thống), và RBAC (theo vai trò và chức danh trong tổ chức).
- Phân tích đối trọng hai mô hình bảo mật kinh điển: Bell-LaPadula (bảo vệ tính bí mật: No Read Up, No Write Down) và Biba (bảo vệ tính toàn vẹn: No Read Down, No Write Up).
- So sánh mã hóa đối xứng vs mã hóa bất đối xứng về số lượng khóa, tốc độ, độ phức tạp quản lý và nhận diện các thuật toán tiêu biểu (SEED, ARIA, AES vs RSA, ECC).

## 핵심 키워드
- 파티셔닝 (Phân vùng dữ liệu / Partitioning / 범위 Range, 해시 Hash, 목록 List, 조합 Composite, 라운드 로빈 Round Robin)
- 파티션 프루닝 (Cắt tỉa phân vùng / Partition Pruning / I/O 절감)
- 접근 통제 (Kiểm soát truy cập / DAC 임의, MAC 강제, RBAC 역할기반)
- 벨-라파듈라 모델 (Bell-LaPadula / BLP / 기밀성 / No Read Up, No Write Down)
- 비바 모델 (Biba / 무결성 / No Read Down, No Write Up)
- 암호화 (Mã hóa CSDL / 대칭키 SEED, ARIA, AES / 비대칭키 RSA, ECC)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md](11-co-so-du-lieu-phan-tan-va-tinh-trong-suot.md), chúng ta đã nắm vững kiến trúc phân tán trên mạng diện rộng với 4 tính chất trong suốt và giao thức cam kết 2 pha 2PC.
- **Đang giải quyết gì (Current Problem):** Khi dữ liệu tích lũy lên hàng chục triệu bản ghi trên một nút lưu trữ, hiệu năng đọc/ghi suy giảm nghiêm trọng và nguy cơ lộ lọt thông tin tăng cao. Bài học này giải quyết việc xé nhỏ bảng dữ liệu qua **Phân vùng (Partitioning)** và thiết lập lá chắn bảo vệ thông qua **Kiểm soát truy cập và Mã hóa CSDL**.
- **Dùng đi đâu (Forward Handoff):** Các phân vùng dữ liệu và chuẩn mã hóa này sẽ là đầu vào để xây dựng các đường ống chuyển đổi ETL, kho dữ liệu lớn Data Warehouse / OLAP và hệ sinh thái Big Data ở bài học tiếp theo [13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md](13-chuyen-doi-du-lieu-etl-data-warehouse-va-big-data.md).

## 읽는 방법
- Đọc TẦNG A để thuộc lòng các bẫy đề thi hay hỏi nhất: Round Robin không cần Primary Key, câu thần chú Bell-LaPadula (Bí mật) vs Biba (Toàn vẹn), và nhận diện 2 thuật toán quốc gia Hàn Quốc (SEED và ARIA là mã hóa khối đối xứng).
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
| **Phân vùng kết hợp** | **조합 분할 (Composite)** | Phân vùng 2 tầng: 1 cấp Range, 2 cấp Hash | Dùng cho bảng siêu lớn (ví dụ: phân vùng Tháng sau đó băm theo ID) |
| **Phân vùng xoay vòng**| **라운드 로빈 (Round Robin)** | Phân phối luân phiên từng bản ghi theo lượt | **Hoàn toàn không cần Khóa chính (Primary Key)** |

#### 2. Đối chiếu 3 mô hình kiểm soát truy cập (접근 통제)
| Mô hình | Tên tiếng Hàn & Anh | Cơ sở cấp quyền | Đặc trưng kỹ thuật then chốt |
| :--- | :--- | :--- | :--- |
| **DAC** | **임의 접근통제 (Discretionary)** | **Chủ sở hữu dữ liệu (Data Owner)** | Chủ sở hữu tự do cấp/hủy quyền cho người khác qua lệnh `GRANT`/`REVOKE` |
| **MAC** | **강제 접근통제 (Mandatory)** | **Cấp bậc an ninh của hệ thống** | So sánh nhãn bảo mật (Security Clearance vs Classification); người dùng không tự ý đổi quyền |
| **RBAC** | **역할기반 접근통제 (Role-Based)** | **Vai trò / Chức danh công việc** | Gán quyền vào Vai trò (Role), sau đó xếp người dùng vào Vai trò tương ứng |

#### 3. Sơ đồ và Bảng so sánh mô hình an ninh: Bell-LaPadula vs Biba
```
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
| Tiêu chí | Mã hóa đối xứng (`대칭키 암호`) | Mã hóa bất đối xứng (`비대칭키 암호`) |
| :--- | :--- | :--- |
| **Khóa giải mã** | **Khóa mã hóa = Khóa giải mã** (Dùng chung 1 khóa bí mật) | **Khóa mã hóa $\neq$ Khóa giải mã** (Cặp Public Key & Private Key) |
| **Tốc độ xử lý** | **Rất nhanh**, tối ưu cho dữ liệu dung lượng lớn | **Chậm**, tốn nhiều chi phí xử lý toán học |
| **Số lượng khóa** | $N$ người cần: $\mathbf{\frac{N(N-1)}{2}}$ khóa | $N$ người cần: $\mathbf{2N}$ khóa |
| **Thuật toán tiêu biểu**| DES, 3DES, AES, **SEED (Hàn Quốc)**, **ARIA (Hàn Quốc)** | RSA, DSA, ECC, Diffie-Hellman |

#### 5. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Phân vùng không cần Khóa chính:** Phương pháp phân vùng duy nhất **không cần Primary Key** là **라운드 로빈 분할 (Round Robin)**.
- **Bẫy 2: Phân biệt Bell-LaPadula và Biba:**
  - Nhắc tới bảo vệ **기밀성 (Tính bí mật)** $\rightarrow$ **Bell-LaPadula** (No Read Up, No Write Down).
  - Nhắc tới bảo vệ **무결성 (Tính toàn vẹn)** $\rightarrow$ **Biba** (No Read Down, No Write Up).
- **Bẫy 3: Thuật toán mã hóa của Hàn Quốc:** Cả hai thuật toán **SEED** và **ARIA** đều thuộc nhóm **대칭키 블록 암호 (Mã hóa khối đối xứng)**.
- **Bẫy 4: Thao tác cấp quyền của DAC:** Hệ thống sử dụng lệnh `GRANT` và `REVOKE` do chủ sở hữu tự do quyết định quyền thuộc mô hình **DAC (임의 접근통제)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế Cắt tỉa phân vùng (Partition Pruning)
- **Bản chất:** Khi câu lệnh truy vấn có điều kiện `WHERE NgayTao >= '2026-01-01'`, Optimizer sẽ tự động nhận diện và chỉ đọc đúng tệp dữ liệu của phân vùng Năm 2026, loại bỏ hoàn toàn các phân vùng của các năm trước ra khỏi phạm vi đọc đĩa.
- **Lợi ích quản trị vòng đời (Data Lifecycle Management):** Khi cần dọn dẹp dữ liệu của 5 năm trước, DBA chỉ cần thực thi một câu lệnh duy nhất `ALTER TABLE GIAO_DICH DROP PARTITION p_2021;`. Thao tác này giải phóng đĩa tức thì trong 1 giây mà không phát sinh log khổng lồ như lệnh `DELETE`.

#### 2. Các mô hình bảo mật bổ trợ
- **클락-윌슨 모델 (Clark-Wilson Model):** Mô hình an ninh chuyên dụng cho doanh nghiệp thương mại nhằm duy trì tính toàn vẹn dữ liệu; quy định người dùng không được can thiệp trực tiếp vào dữ liệu mà bắt buộc phải thông qua các tiến trình biến đổi được chứng nhận (`Transformation Procedure`).
- **차이니즈 월 모델 (Chinese Wall / Brewer-Nash Model):** Mô hình tường lửa người Hoa áp dụng cho ngành tài chính - ngân hàng để ngăn chặn xung đột lợi ích (`이해 충돌`); người dùng khi đã truy cập dữ liệu của một doanh nghiệp sẽ bị cấm truy cập dữ liệu của doanh nghiệp đối thủ cạnh tranh.

#### 3. Phân loại thuật toán mã hóa đối xứng
- **Mã hóa khối (`블록 암호`):** Chia dữ liệu thành từng khối có độ dài cố định (như 64-bit, 128-bit) để mã hóa. Ví dụ: DES (64-bit), AES (128-bit), SEED (128-bit), ARIA (128-bit).
- **Mã hóa dòng (`스트림 암호`):** Mã hóa liên tục từng bit hoặc từng byte dữ liệu theo chuỗi khóa bit ngẫu nhiên. Ví dụ: RC4.

---

### 복습 체크리스트
- [ ] Phân biệt 5 phương pháp phân vùng: Range (khoảng liên tục), Hash (phân bổ đều), List (danh mục rời rạc), Composite (2 tầng), Round Robin (luân phiên, không cần PK).
- [ ] Giải thích nguyên lý hoạt động và lợi ích giảm thiểu I/O của Partition Pruning.
- [ ] Phân biệt 3 mô hình kiểm soát truy cập: DAC (chủ sở hữu), MAC (cấp bậc an ninh), RBAC (vai trò chức danh).
- [ ] Nằm lòng quy tắc Bell-LaPadula (No Read Up, No Write Down cho Bí mật) và Biba (No Read Down, No Write Up cho Toàn vẹn).
- [ ] Thuộc công thức tính số lượng khóa trong mã hóa đối xứng $\frac{N(N-1)}{2}$ và bất đối xứng $2N$.
- [ ] Ghi nhớ SEED và ARIA là 2 thuật toán mã hóa khối đối xứng của Hàn Quốc.
