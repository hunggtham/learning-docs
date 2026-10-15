# 336. 소프트웨어 개발 프레임워크 (Software Development Framework)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, 4 đặc tính kiến trúc cốt lõi của Khung phát triển phần mềm (모듈화, 재사용성, 확장성, 제어의 역흐름 - IoC) và vai trò giải phóng sự phụ thuộc vào nhà thầu.
- Nắm vững và phân biệt chính xác 4 nhóm kiến thức hay bị bẫy nhầm lẫn nhất trong đề thi kỹ sư CNTT:
  1. Phân loại chuẩn COCOMO (Organic, Semi-Detached, Embedded – tuyệt đối không có "Sequential").
  2. Giao thức định tuyến mạng (RIP 거리 벡터 vs OSPF 링크 상태 vs BGP 경로 벡터).
  3. Phân loại mật mã học (Khóa đối xứng AES/DES/SEED vs Khóa công khai RSA vs Hàm băm một chiều Hash MD5/SHA).
  4. Các mô hình bảo mật thông tin kinh điển (Bell-LaPadula bảo mật bí mật vs Biba bảo toàn vẹn vs Chinese Wall chống xung đột lợi ích).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 개발 프레임워크 (Software Development Framework)
- 제어의 역흐름 (Inversion of Control - IoC)
- COCOMO 3대 유형 (Organic, Semi-Detached, Embedded)
- 라우팅 프로토콜 (RIP 15홉 거리벡터, OSPF 링크상태, BGP 자율시스템간)
- 암호 알고리즘 분류 (대칭키 AES/DES vs 공개키 RSA vs 일방향 해시 SHA)
- 보안 모델 (Bell-LaPadula 기밀성, Biba 무결성, Chinese Wall 이해상충)

## 선행·연결 개념 (Kiến thức liên kết)
- [04-bai-hoc.md](04-bai-hoc.md): Tổng hợp tái sử dụng phần mềm và các mô hình ước tính chi phí.
- [06-bai-hoc.md](06-bai-hoc.md): Quản lý dự án phần mềm và công thức tính Man-Month.
- [07-bai-hoc.md](07-bai-hoc.md): Quản lý tiến độ dự án bằng sơ đồ mạng PERT/CPM và biểu đồ Gantt.

## 읽는 방법 (Cách đọc)
- Các điểm phân biệt "sống còn" để lấy trọn điểm trắc nghiệm:
  - **COCOMO:** Chỉ có 3 loại **Organic / Semi-Detached / Embedded**. Nếu đề bài đưa ra chữ *Sequential* hoặc *Iterative* $\rightarrow$ Đó là đáp án sai bẫy!
  - **Mật mã:** AES, DES, SEED, ARIA là **Đối xứng (Symmetric)**; RSA, ECC là **Bất đối xứng/Công khai (Public Key)**; SHA-256, MD5 là **Hàm băm (Hash)** – không có khái niệm giải mã ngược lại bằng khóa.
  - **Mô hình bảo mật:**
    - **Bell-LaPadula (BLP):** Bảo vệ tính **Bí mật (Confidentiality / 기밀성)** $\rightarrow$ Luật NRU/NWD (*No Read Up, No Write Down*).
    - **Biba:** Bảo vệ tính **Toàn vẹn (Integrity / 무결성)** $\rightarrow$ Luật NRD/NWU (*No Read Down, No Write Up* - ngược hoàn toàn với BLP).
    - **Chinese Wall:** Ngăn chặn **Xung đột lợi ích (Conflict of Interest / 이해상충 방지)** giữa các khách hàng cạnh tranh nhau trong cùng ngân hàng.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu các mô hình an ninh bảo mật kinh điển:**

| Mô hình bảo mật | Mục tiêu bảo vệ tối cao | Nguyên tắc kiểm soát truy cập bắt buộc | Ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **Bell-LaPadula** (BLP) | **Tính bí mật / Bảo mật** (Confidentiality / 기밀성) | **No Read Up (NRU):** Cấm đọc tài liệu cấp cao hơn; **No Write Down (NWD):** Cấm ghi đè thông tin nhạy cảm xuống cấp thấp hơn. | Hệ thống quốc phòng quân sự, an ninh quốc gia. |
| **Biba Model** | **Tính toàn vẹn** (Integrity / 무결성) | **No Read Down (NRD):** Cấm đọc dữ liệu từ nguồn bẩn cấp dưới; **No Write Up (NWU):** Cấm ghi dữ liệu chưa kiểm chứng lên cấp độ tin cậy cao hơn. | Hệ thống tài chính kế toán ngân hàng, cơ sở dữ liệu học bạ. |
| **Chinese Wall** (Brewer & Nash) | **Chống xung đột lợi ích** (Conflict of Interest / 이해상충) | Người dùng chỉ được phép truy cập vào một tập dữ liệu của công ty nếu chưa từng truy cập vào tập dữ liệu của công ty đối thủ cạnh tranh cùng ngành. | Công ty tư vấn tài chính, hãng luật phục vụ nhiều tập đoàn cạnh tranh. |

- **2. Bảng phân loại thuật toán mật mã học:**

| Nhóm mật mã | Tên thuật toán đại diện | Đặc điểm vận hành & Trao đổi khóa |
| :--- | :--- | :--- |
| **Khóa đối xứng** (Symmetric / Bí mật) | **DES, 3-DES, AES, SEED, ARIA** | Dùng **chung một khóa bí mật** cho cả việc mã hóa và giải mã. Tốc độ rất nhanh, nhưng khó khăn trong việc phân phối và lưu trữ $N(N-1)/2$ khóa. |
| **Khóa bất đối xứng** (Asymmetric / Công khai) | **RSA, Diffie-Hellman, ECC, DSA** | Sử dụng một cặp khóa: **Khóa công khai (Public Key)** dùng để mã hóa và **Khóa bí mật (Private Key)** dùng để giải mã. Quản lý khóa dễ dàng, dùng làm chữ ký số. |
| **Hàm băm một chiều** (One-way Hash) | **SHA-256, SHA-512, MD5** | Biến đổi đầu vào có độ dài bất kỳ thành chuỗi nhị phân có độ dài cố định. **Không thể giải mã ngược lại**; dùng kiểm tra tính toàn vẹn dữ liệu. |

- **3. Bảng phân biệt giao thức định tuyến mạng (Routing Protocols):**

| Giao thức | Thuật toán định tuyến | Phạm vi áp dụng | Đặc tính kỹ thuật cốt lõi |
| :--- | :--- | :--- | :--- |
| **RIP** | **거리 벡터 (Distance Vector)** | IGP (Nội bộ mạng nhỏ) | Dùng thuật toán Bellman-Ford; thước đo là số bước nhảy (Hop Count); **giới hạn tối đa 15 Hop** (Hop 16 là vô cùng / không tới được). |
| **OSPF** | **링크 상태 (Link State)** | IGP (Nội bộ mạng lớn) | Dùng thuật toán Dijkstra tìm đường đi ngắn nhất (SPF); tính toán dựa trên băng thông đường truyền, cập nhật nhanh, không giới hạn Hop. |
| **BGP** | **경로 벡터 (Path Vector)** | EGP (Giữa các hệ tự trị AS) | Định tuyến đường trục Internet toàn cầu giữa các nhà mạng ISP; dựa trên chính sách định tuyến mạng và danh sách các số hiệu AS đi qua. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc phân biệt BLP vs Biba bằng trực giác:**
  - *Bell-LaPadula (Bí mật):* Bí mật của cấp trên thì cấp dưới **không được đọc (NRU)**, và người ở cấp cao thì **không được viết lộ tin xuống cấp thấp (NWD)**.
  - *Biba (Toàn vẹn):* Dữ liệu sạch của sếp thì **không được đọc rác từ cấp dưới vào làm bẩn (NRD)**, và người cấp thấp kém tin cậy thì **không được viết bừa vào tài liệu chuẩn mực của cấp cao (NWU)**.

### 복습 체크리스트
- [ ] Ghi nhớ 3 loại quy mô của COCOMO: Organic, Semi-Detached, Embedded (loại trừ Sequential).
- [ ] Phân biệt được: BLP bảo vệ tính bí mật (NRU/NWD), Biba bảo vệ tính toàn vẹn (NRD/NWU).
- [ ] Nhớ Chinese Wall ra đời để chống xung đột lợi ích (이해상충 방지).
- [ ] Phân biệt được: AES/DES là khóa đối xứng, RSA là khóa công khai, SHA là hàm băm một chiều.
- [ ] Nhớ RIP dùng Distance Vector (tối đa 15 hop), OSPF dùng Link State (Dijkstra), BGP dùng Path Vector liên AS.
