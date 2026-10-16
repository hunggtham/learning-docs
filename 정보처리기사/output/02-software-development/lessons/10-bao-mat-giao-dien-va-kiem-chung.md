# 10. Bảo mật giao diện và công cụ kiểm chứng (인터페이스 보안 및 검증 도구)

## 1. Tổng quan và Phân vùng bảo mật giao diện

Trong kiến trúc phần mềm hiện đại, các module và hệ thống con không hoạt động độc lập mà liên tục trao đổi dữ liệu qua các điểm giao tiếp (Interface / API). Việc bảo vệ dữ liệu truyền thông và đảm bảo các giao diện hoạt động chính xác theo đặc tả kỹ thuật là yêu cầu sống còn.

Bảo mật giao diện được phân chia theo các tầng mô hình mạng OSI:
- **Tầng mạng (Network Layer - L3):** Bảo vệ toàn bộ gói tin IP ở mức hệ điều hành thông qua **IPSec**, tạo kênh truyền bảo mật cho mọi ứng dụng chạy phía trên mà không đòi hỏi sửa đổi mã nguồn ứng dụng.
- **Tầng giao vận / phiên (Transport / Session Layer - L4/L5):** Bảo vệ luồng dữ liệu TCP bằng **SSL/TLS**, phổ biến nhất trong các giao dịch web an toàn (HTTPS).
- **Tầng ứng dụng (Application Layer - L7):** Bảo vệ chi tiết từng bức điện hoặc thông điệp HTTP riêng lẻ thông qua **S-HTTP**.

Song song với việc mã hóa luồng truyền, hệ thống đòi hỏi các cơ chế kiểm tra tính toàn vẹn tệp tin máy chủ (như **Tripwire**) để phát hiện xâm nhập/cài cắm cửa sau (Backdoor), và các bộ khung kiểm thử tự động (**xUnit, STAF, FitNesse, NTAF, watir**) để kiểm chứng tính sẵn sàng và chính xác của giao diện trước và sau khi triển khai.

> [!NOTE]
> **Ranh giới môn học (Subject Boundary):** Bài học này tập trung vào các giao thức bảo mật và công cụ kiểm chứng dưới góc độ kết nối giao diện phần mềm trong Môn 2 (소프트웨어 개발). Các thuật toán mật mã học chi tiết (RSA, AES, SHA...), hạ tầng khóa công khai PKI và các hình thức tấn công mạng chuyên sâu được trình bày toàn diện trong Môn 5 (정보시스템 구축관리).

---

## 2. Giao thức bảo mật giao diện mạng (네트워크 영역 보안 프로토콜)

Kỳ thi kỹ sư xử lý thông tin đặc biệt nhấn mạnh sự phân loại tầng hoạt động và cơ chế bảo vệ của 3 giao thức: **IPSec**, **SSL/TLS**, và **S-HTTP**.

### 2.1. So sánh 3 giao thức bảo mật đường truyền

| Giao thức | Tầng OSI đối ứng | Cơ chế hoạt động cốt lõi | Phạm vi ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| **IPSec (IP Security)** | **Tầng mạng (L3 - Network)** | Mã hóa và xác thực trực tiếp tại mức gói tin IP bằng giao thức **AH** và **ESP** | Mạng riêng ảo **VPN**, kết nối an toàn giữa các văn phòng/chi nhánh |
| **SSL / TLS** | **Tầng giao vận (L4/L5 - Transport)** | Dùng mã hóa bất đối xứng để bắt tay trao đổi khóa, sau đó dùng mã hóa đối xứng truyền dữ liệu tốc độ cao | Web an toàn (**HTTPS / Port 443**), truyền file/mail an toàn (FTPS, SMTPS) |
| **S-HTTP** | **Tầng ứng dụng (L7 - Application)** | Chỉ mã hóa nội dung của thông điệp HTTP cụ thể giữa Client và Server, không mã hóa toàn bộ kênh truyền | Kiểm soát bảo mật chi tiết từng thông điệp riêng lẻ (ít dùng hơn SSL/TLS) |

### 2.2. Chi tiết bộ giao thức IPSec (IP Security Architecture)

IPSec hoạt động ở Tầng 3 (Network Layer) và được cấu thành từ 3 giao thức thành phần:
1. **AH (Authentication Header):**
   - Đảm bảo **tính toàn vẹn dữ liệu (Data Integrity)** và **xác thực nguồn gốc (Authentication)**.
   - Hỗ trợ chống phát lại gói tin (**Anti-replay**).
   - **Bẫy đề thi:** AH **KHÔNG** cung cấp tính năng bảo mật bí mật (Confidentiality / Encryption) — AH không mã hóa nội dung dữ liệu (Payload).
2. **ESP (Encapsulating Security Payload):**
   - Cung cấp đồng thời cả **mã hóa bảo mật bí mật (Confidentiality)**, **xác thực nguồn gốc** và **tính toàn vẹn dữ liệu**.
3. **IKE (Internet Key Exchange):**
   - Giao thức tự động thiết lập liên kết bảo mật (SA - Security Association) và thương lượng, trao đổi khóa mật mã giữa hai thiết bị truyền thông.

### 2.3. Hai chế độ hoạt động của IPSec: 전송 모드 vs 터널 모드

| Chế độ hoạt động | Phạm vi mã hóa (Encrypted Area) | Cấu trúc IP Header mới | Ngữ cảnh ứng dụng |
| :--- | :--- | :--- | :--- |
| **전송 모드 (Transport Mode)** | Chỉ mã hóa **Payload (Dữ liệu)**; giữ nguyên IP Header gốc | **Không tạo** IP Header mới | Giao tiếp trực tiếp giữa 2 máy chủ trạm (**Host-to-Host**) |
| **터널 모드 (Tunnel Mode)** | Mã hóa **toàn bộ gói tin IP gốc** (cả IP Header cũ và Payload) | **Tạo thêm** New IP Header ở bên ngoài | Kết nối giữa hai cổng mạng an toàn qua VPN (**Gateway-to-Gateway**) |

- Trong chế độ **전송 모드 (Transport Mode)**, địa chỉ IP nguồn và đích ban đầu hiển thị công khai trên gói tin, do đó chỉ phù hợp khi hai trạm đầu cuối trực tiếp cấu hình mã hóa cho nhau.
- Trong chế độ **터널 모드 (Tunnel Mode)**, gói tin gốc được bảo vệ hoàn toàn và gói trong một gói tin IP hoàn toàn mới, giúp che giấu cấu trúc mạng nội bộ khi truyền qua môi trường Internet công cộng giữa hai Gateway/Router VPN.

---

## 3. Công cụ kiểm tra toàn vẹn hệ thống: Tripwire (트립와이어)

Bên cạnh bảo mật đường truyền, việc bảo vệ tính toàn vẹn của các tệp cấu hình và mã nguồn dịch vụ giao diện trên máy chủ là yếu tố then chốt nhằm ngăn ngừa cửa sau (Backdoor).

### 3.1. Khái niệm và nguyên lý hoạt động

- **트립와이어 (Tripwire)** là công cụ kiểm tra tính toàn vẹn dữ liệu hệ thống (**무결성 검사 도구 - Data Integrity Checker**), hoạt động như một hệ thống phát hiện xâm nhập dựa trên máy chủ (**HIDS - Host-based Intrusion Detection System**).
- **Cơ chế bẫy dây (Tripwire Metaphor):** Tương tự như sợi dây bẫy báo động khi kẻ trộm đột nhập, Tripwire tính toán và lưu trữ chữ ký số / mã băm mật mã (**Hash / Checksum: MD5, SHA**) của tất cả các tệp nhị phân hệ thống (`/bin`, `/sbin`), tệp cấu hình (`/etc`) và thư viện dùng chung ngay sau khi cài đặt hệ thống sạch.

### 3.2. Quy trình vận hành 3 pha của Tripwire

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

1. **Tạo lập cơ sở dữ liệu mẫu (Baseline DB Creation):** Quét toàn bộ danh mục chỉ định và lưu mã băm an toàn vào cơ sở dữ liệu mã hóa đặt tại vùng lưu trữ chỉ đọc (Read-Only).
2. **Quét định kỳ (Periodic Scanning):** Chạy tiến trình ngầm định kỳ để đọc lại nội dung tệp và tính toán giá trị băm tức thời.
3. **Báo cáo sai lệch (Discrepancy Reporting):** Nếu phát hiện bất kỳ sự thay đổi nào về kích thước, ngày hiệu chỉnh, quyền hạn hoặc giá trị băm, hệ thống lập tức ghi nhật ký và kích hoạt cảnh báo cho quản trị viên.

> [!WARNING]
> **Điểm mấu chốt trong đề thi:** Tripwire là công cụ phát hiện xâm nhập bị động (**Detection**) bằng cách so sánh **mã băm (해시 값 비교)** nhằm tìm kiếm **cửa sau (백도어 탐지)** hoặc tệp cấu hình bị biến đổi trái phép. Tripwire **không** phải là tường lửa (Firewall) và **không** tự động ngăn chặn gói tin mạng.

---

## 4. Công cụ kiểm chứng triển khai giao diện (인터페이스 구현 검증 도구)

Sau khi xây dựng các giao diện (API, RPC, Web Service), đội ngũ phát triển phải sử dụng các bộ khung kiểm thử tự động để xác minh tính tương thích, độ ổn định và tính sẵn sàng của hệ thống.

### 4.1. Bảng đối chiếu 5 công cụ kiểm chứng trọng tâm

| Tên công cụ | Nền tảng / Đặc tính | Cơ chế kỹ thuật trọng tâm | Từ khóa nhận diện đề thi |
| :--- | :--- | :--- | :--- |
| **xUnit** | Đa ngôn ngữ (Java, C++, C#...) | Khung kiểm thử đơn vị (**단위 테스트 프레임워크**) tự động hóa việc thực thi và lập báo cáo kết quả | **단위 테스트**, JUnit, CppUnit, NUnit |
| **STAF** | Đa nền tảng (C/S, Daemon) | Khung tự động hóa kiểm thử hướng dịch vụ trong **môi trường phân tán (분산 환경)**; hỗ trợ tái sử dụng thành phần | **서비스 호출**, **컴포넌트 재사용**, **분산 환경** |
| **FitNesse** | Nền tảng Web / Wiki | Khung kiểm thử chấp nhận trực quan; thiết kế và hiển thị kịch bản kiểm thử dưới dạng **bảng biểu trên Web** | **웹 기반**, **Wiki 기반**, 케이스 테이블 작성 |
| **NTAF** | Do NHN (Naver) phát triển | Giải pháp tích hợp: kết hợp giao diện Web/Wiki thân thiện của **FitNesse** với năng lực kiểm thử phân tán của **STAF** | **FitNesse + STAF 결합**, **NHN(네이버)** |
| **watir** | Dựa trên **Ruby** | Khung kiểm thử tự động hóa tương tác trình duyệt ứng dụng Web dựa trên ngôn ngữ lập trình Ruby | **Ruby 기반**, 웹 애플리케이션 테스트 |

### 4.2. Mẹo ghi nhớ nhận diện từ khóa thi (Mnemonic Matching)

- **xUnit:** Thấy tiền tố ngôn ngữ gắn với Unit (Java $\rightarrow$ JUnit, C++ $\rightarrow$ CppUnit, C# $\rightarrow$ NUnit) $\rightarrow$ Khung kiểm thử đơn vị tiêu chuẩn.
- **STAF:** Thấy chữ **분산 환경 (Môi trường phân tán)** và **컴포넌트 재사용 (Tái sử dụng component)** $\rightarrow$ Chọn STAF.
- **FitNesse:** Thấy chữ **웹 기반 (Dựa trên Web)** và **Wiki (위키)** $\rightarrow$ Chọn FitNesse.
- **NTAF:** Thấy chữ viết tắt của **Naver** hoặc công thức **FitNesse + STAF** $\rightarrow$ Chọn NTAF.
- **watir:** Thấy ngôn ngữ **Ruby** để kiểm thử Web $\rightarrow$ Chọn watir.

### 4.3. Giám sát giao diện qua APM (Application Performance Monitoring)

Trong môi trường vận hành thực tế, việc kiểm tra giao diện không chỉ dừng lại ở chức năng gửi/nhận thành công mà còn bao gồm kiểm tra hiệu năng và độ trễ giao diện.
- **APM (Application Performance Monitoring / Management):** Công cụ giám sát hiệu năng ứng dụng theo thời gian thực (như Scouter, Jennifer, Datadog), giúp phát hiện tắc nghẽn tài nguyên (Bottleneck), lỗi hết kết nối (Connection Pool Exhaustion) và độ trễ gọi API từ xa giữa các hệ thống con.

---

## 5. Câu hỏi ôn tập và bẫy đề thi thực tế

1. **IPSec Transport Mode vs Tunnel Mode:**
   - *Câu hỏi:* Khi thiết lập mạng riêng ảo VPN kết nối giữa 2 Gateway chi nhánh công ty, chế độ nào của IPSec được sử dụng và cấu trúc gói tin thay đổi như thế nào?
   - *Đáp án chuẩn thi:* Sử dụng **터널 모드 (Tunnel Mode)**. Toàn bộ gói tin IP ban đầu (gồm cả Header cũ và Payload) được mã hóa hoàn toàn, và một **New IP Header** mới được đóng gói bên ngoài.
2. **Thành phần AH trong IPSec:**
   - *Bẫy đề thi:* "Giao thức AH trong IPSec mã hóa dữ liệu người dùng để chống nghe trộm." $\rightarrow$ **SAI**. AH chỉ cung cấp tính xác thực (Authentication) và toàn vẹn (Integrity). Muốn mã hóa bảo mật bí mật (Confidentiality), phải dùng **ESP**.
3. **Phát hiện Backdoor bằng Tripwire:**
   - *Câu hỏi:* Công cụ nào dưới đây được sử dụng làm **무결성 검사 도구 (Công cụ kiểm tra tính toàn vẹn)** nhằm phát hiện việc cài cắm **백도어 (Backdoor)** hoặc sửa đổi trái phép các tệp cấu hình hệ điều hành dựa trên việc so sánh mã băm?
   - *Đáp án chuẩn thi:* **트립와이어 (Tripwire)**.
4. **Nhận diện công cụ NTAF:**
   - *Câu hỏi:* Khung kiểm thử tự động do tập đoàn NHN (Naver) phát triển dựa trên sự kết hợp giữa FitNesse và STAF có tên là gì?
   - *Đáp án chuẩn thi:* **NTAF (Naver Test Automation Framework)**.

---

## 6. Liên kết bài học tiếp theo

Sau khi hoàn thiện thiết kế module, giao thức truyền thông liên hệ thống và các công cụ bảo mật/kiểm chứng, quy trình phát triển phần mềm bước vào giai đoạn đóng gói bản phát hành thương mại và quản lý bản quyền số. Tiếp tục với **[11-dong-goi-phan-mem-va-drm.md](11-dong-goi-phan-mem-va-drm.md)** để nắm vững quy trình đóng gói phần mềm và kiến trúc bảo vệ bản quyền số DRM.
