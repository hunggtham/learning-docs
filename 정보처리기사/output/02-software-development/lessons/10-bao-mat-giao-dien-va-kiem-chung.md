# 인터페이스 보안 및 검증 도구 (Bảo mật giao diện và công cụ kiểm chứng)

## 학습 목표
- Nắm vững phân vùng bảo mật giao diện theo các tầng mô hình OSI: Tầng mạng L3 (`IPSec`), Tầng giao vận L4/L5 (`SSL/TLS`), và Tầng ứng dụng L7 (`S-HTTP`).
- Phân tích chi tiết 3 thành phần của bộ giao thức IPSec: `AH` (Xác thực, toàn vẹn, chống phát lại, **KHÔNG mã hóa payload**), `ESP` (Mã hóa bảo mật + Xác thực + Toàn vẹn), và `IKE` (Thương lượng và trao đổi khóa).
- Phân biệt 2 chế độ hoạt động của IPSec: Chế độ truyền tải (`전송 모드 / Transport Mode` - Host to Host) và Chế độ đường hầm (`터널 모드 / Tunnel Mode` - Gateway to Gateway, tạo New IP Header).
- Nắm vững vai trò của công cụ kiểm tra tính toàn vẹn hệ thống tệp `Tripwire` (so sánh mã băm MD5/SHA phát hiện cài cắm cửa sau Backdoor).
- Nhận diện 5 bộ khung kiểm thử tự động giao diện phần mềm: `xUnit`, `STAF`, `FitNesse`, `NTAF`, và `watir`.

## 핵심 키워드
- 인터페이스 보안 (Bảo mật giao diện / Interface Security)
- IPSec (Tầng mạng L3 / AH 무결성·인증 vs ESP 암호화 vs IKE 키 교환)
- 전송 모드 vs 터널 모드 (Transport Mode vs Tunnel Mode / New IP Header)
- SSL/TLS (Tầng giao vận L4/L5 / HTTPS 443)
- S-HTTP (Tầng ứng dụng L7 / 메시지 단위 암호화)
- 트립와이어 (Tripwire / 무결성 검사 도구 / 해시값 비교)
- 인터페이스 검증 도구 (xUnit, STAF, FitNesse, NTAF, watir)

## 선행·연결 개념
- **Từ đâu (Origin / Prerequisite):** Ở bài học trước [09-tich-hop-he-thong-eai-esb.md](09-tich-hop-he-thong-eai-esb.md), chúng ta đã khảo sát các kiến trúc tích hợp liên hệ thống EAI và ESB.
- **Đang giải quyết gì (Current Problem):** Khi các giao diện hệ thống được mở ra để truyền nhận dữ liệu qua mạng, nguy cơ bị nghe lén, giả mạo và cài backdoor xuất hiện. Bài học này giải quyết bài toán mã hóa đường truyền bằng IPSec, SSL/TLS, giám sát toàn vẹn máy chủ bằng Tripwire và kiểm thử tự động API bằng các công cụ chuyên dụng.
- **Dùng đi đâu (Forward Handoff):** Sau khi bảo vệ và kiểm chứng xong các giao diện kết nối, bài học tiếp theo [11-dong-goi-phan-mem-va-drm.md](11-dong-goi-phan-mem-va-drm.md) sẽ đưa người học sang quy trình đóng gói phần mềm và quản trị bản quyền số DRM.

## 읽는 방법
- Đọc TẦNG A để thuộc lòng bảng so sánh 3 giao thức bảo mật đường truyền (IPSec, SSL/TLS, S-HTTP), bảng đối chiếu Transport vs Tunnel Mode của IPSec, và danh sách 5 công cụ kiểm chứng giao diện.
- Đọc TẦNG B để hiểu sâu cơ chế hoạt động của AH/ESP/IKE, nguyên lý so sánh mã băm của Tripwire và đặc tính của từng công cụ kiểm thử xUnit/STAF/FitNesse.

---

## 인터페이스 보안 및 검증 도구

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh 3 giao thức bảo mật đường truyền
| Giao thức | Tầng OSI đối ứng | Cơ chế hoạt động cốt lõi | Phạm vi ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **IPSec (IP Security)** | **Tầng mạng (L3 - Network)** | Mã hóa và xác thực trực tiếp tại mức gói tin IP bằng giao thức **AH** và **ESP** | Mạng riêng ảo **VPN**, kết nối an toàn giữa các văn phòng/chi nhánh |
| **SSL / TLS** | **Tầng giao vận (L4/L5 - Transport)** | Dùng mã hóa bất đối xứng để bắt tay trao đổi khóa, sau đó dùng mã hóa đối xứng truyền dữ liệu tốc độ cao | Web an toàn (**HTTPS / Port 443**), truyền file/mail an toàn (FTPS, SMTPS) |
| **S-HTTP** | **Tầng ứng dụng (L7 - Application)** | Chỉ mã hóa nội dung của thông điệp HTTP cụ thể giữa Client và Server, không mã hóa toàn bộ kênh truyền | Kiểm soát bảo mật chi tiết từng thông điệp riêng lẻ (ít dùng hơn SSL/TLS) |

#### 2. Đối chiếu Transport Mode vs Tunnel Mode trong IPSec
| Chế độ hoạt động | Phạm vi mã hóa (Encrypted Area) | Cấu trúc IP Header mới | Ngữ cảnh ứng dụng |
| :--- | :--- | :--- | :--- |
| **전송 모드 (Transport Mode)** | Chỉ mã hóa **Payload (Dữ liệu)**; giữ nguyên IP Header gốc | **Không tạo** IP Header mới | Giao tiếp trực tiếp giữa 2 máy chủ trạm (**Host-to-Host**) |
| **터널 모드 (Tunnel Mode)** | Mã hóa **toàn bộ gói tin IP gốc** (cả IP Header cũ và Payload) | **Tạo thêm** New IP Header ở bên ngoài | Kết nối giữa hai cổng mạng an toàn qua VPN (**Gateway-to-Gateway**) |

#### 3. Bảng các công cụ kiểm chứng giao diện tự động chuẩn đề thi
| Tên công cụ | Đặc điểm kỹ thuật nhận diện đề thi |
| :--- | :--- |
| **xUnit** | Bộ khung kiểm thử đơn vị tự động theo ngôn ngữ: JUnit (Java), CppUnit (C++), NUnit (.NET), PyUnit (Python) |
| **STAF** | Khung kiểm thử tự động hóa phân tán đa nền tảng dựa trên kiến trúc dịch vụ (Service-driven) |
| **FitNesse** | Khung kiểm thử chấp nhận tự động dựa trên giao diện Wiki đồ họa bảng biểu |
| **NTAF** | Bộ khung kiểm thử tự động do Naver phối hợp cùng FitNesse và STAF phát triển |
| **watir** | Công cụ kiểm thử ứng dụng web tự động hóa viết trên nền tảng ngôn ngữ Ruby |

#### 4. Bẫy đề thi trắc nghiệm kinh điển (기출 함정 포인트)
- **Bẫy 1: Chức năng của AH trong IPSec:** AH cung cấp tính toàn vẹn (Integrity) và xác thực (Authentication), nhưng **TUYỆT ĐỐI KHÔNG CUNG CẤP TÍNH BẢO MẬT BÍ MẬT (Confidentiality / Encryption)** vì AH không mã hóa dữ liệu. Muốn mã hóa phải dùng **ESP**.
- **Bẫy 2: Cổng mặc định của HTTPS:** Giao thức web bảo mật SSL/TLS (HTTPS) sử dụng cổng mạng **443** (khác với HTTP thông thường dùng cổng 80).
- **Bẫy 3: Nhận diện công cụ Tripwire:** Khi đề hỏi "Công cụ nào giám sát các tệp tin hệ thống máy chủ, tính toán mã băm để phát hiện sự thay đổi bất thường hoặc cửa sau (Backdoor)?" $\rightarrow$ Chọn ngay **트립와이어 (Tripwire)**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Chi tiết 3 thành phần cấu tạo của IPSec
1. **AH (Authentication Header):**
   - Đảm bảo **tính toàn vẹn dữ liệu (Data Integrity)** và **xác thực nguồn gốc (Authentication)**.
   - Hỗ trợ chống phát lại gói tin (**Anti-replay**).
   - Không mã hóa phần thân gói tin.
2. **ESP (Encapsulating Security Payload):**
   - Cung cấp đồng thời cả **mã hóa bảo mật bí mật (Confidentiality)**, **xác thực nguồn gốc** và **tính toàn vẹn dữ liệu**.
3. **IKE (Internet Key Exchange):**
   - Giao thức tự động thiết lập liên kết bảo mật (SA - Security Association) và thương lượng, trao đổi khóa mật mã giữa hai thiết bị truyền thông.

#### 2. Nguyên lý hoạt động của Tripwire
```
[Hệ thống sạch ban đầu]
       │
       ▼
[Pha 1: Tạo Baseline DB] ──► Lưu giá trị băm (MD5/SHA), kích thước, inode, permission vào DB an toàn
       │
       ▼
[Pha 2: Quét định kỳ]    ──► Tính toán lại mã băm hiện tại của các file hệ thống
       │
       ▼
[Pha 3: So sánh & Cảnh báo]
       ├─ Không đổi ──► Hệ thống an toàn
       └─ Sai lệch 1 bit ──► Cảnh báo xâm nhập! Phát hiện Backdoor hoặc sửa đổi file trái phép
```
- Trong lần khởi tạo đầu tiên, Tripwire quét toàn bộ các tệp thực thi, tệp cấu hình quan trọng trong hệ thống và tính toán mã băm mật mã (MD5/SHA) của từng tệp, lưu thành một cơ sở dữ liệu đường cơ sở an toàn.
- Định kỳ, Tripwire quét lại hệ thống và đối chiếu mã băm hiện tại với cơ sở dữ liệu gốc:
  - Nếu mã băm bị thay đổi dù chỉ 1 bit, Tripwire lập tức phát cảnh báo quản trị viên về nguy cơ tệp tin đã bị tin tặc chỉnh sửa hoặc chèn mã độc.

---

### 복습 체크리스트
- [ ] Phân loại tầng OSI của 3 giao thức: IPSec (L3 Network), SSL/TLS (L4/L5 Transport), S-HTTP (L7 Application).
- [ ] Nhớ AH trong IPSec không mã hóa dữ liệu (chỉ xác thực và toàn vẹn); ESP mới có mã hóa.
- [ ] Phân biệt 전송 모드 (Transport Mode - Host to Host) và 터널 모드 (Tunnel Mode - Gateway to Gateway có New IP Header).
- [ ] Nhớ HTTPS dùng cổng mạng 443.
- [ ] Định nghĩa Tripwire là công cụ kiểm tra tính toàn vẹn tệp tin bằng mã băm.
- [ ] Nhận diện 5 công cụ kiểm chứng giao diện: xUnit, STAF, FitNesse, NTAF, watir.
