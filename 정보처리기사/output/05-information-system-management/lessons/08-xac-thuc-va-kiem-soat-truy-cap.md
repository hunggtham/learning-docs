# 사용자 인증 및 접근 통제 보안 (Xác thực người dùng & Kiểm soát truy cập hệ thống: AAA, MFA, DAC/MAC/RBAC)

## 학습 목표 (Mục tiêu)
- Nắm vững kiến trúc khung bảo mật máy chủ theo mô hình **AAA**: Xác thực (**Authentication**), Phân quyền (**Authorization**), và Ghi nhật ký kiểm toán (**Accounting**).
- Phân biệt toàn diện 4 nhóm nhân tố xác thực người dùng (Tri thức, Sở hữu, Sinh trắc, Hành vi/Vị trí) và nguyên tắc triển khai Xác thực đa nhân tố (**MFA - Multi-Factor Authentication**).
- Hiểu rõ cơ chế đăng nhập một lần (**SSO - Single Sign-On**) và giao thức xác thực vé **Kerberos** với KDC, AS, TGS.
- Phân biệt bản chất và trường hợp áp dụng của 3 mô hình kiểm soát truy cập kinh điển: **DAC** (Tùy ý, ma trận ACL), **MAC** (Bắt buộc, nhãn bảo mật), và **RBAC** (Dựa trên vai trò công việc).
- Làm chủ quy tắc luồng thông tin trong Mô hình bảo vệ tính bí mật **Bell-LaPadula (NRU, NWD)** và Mô hình bảo vệ tính toàn vẹn **Biba (NRD, NWU)**.

## 핵심 키워드 (Từ khóa song ngữ)
- AAA 프레임워크 (Authentication 인증, Authorization 인가, Accounting 계정 관리)
- 인증 4대 요소 (4 Factors — 지식 Something You Know, 소유 Something You Have, 생체 Something You Are, 위치/행위 Somewhere/Do)
- 다중 요소 인증 (MFA — Multi-Factor Authentication, kết hợp ít nhất 2 nhóm khác loại)
- 생체 인증 오차율 (Biometric Error Rates — FAR 타인수락률 vs FRR 본인거부률, CER/EER)
- SSO (Single Sign-On — Đăng nhập một lần dùng cho nhiều hệ thống)
- 커버로스 (Kerberos — Giao thức xác thực vé Ticket dựa trên KDC, AS, TGS)
- DAC (임의적 접근 통제 — Discretionary Access Control, 신분 Identity 기반, 소유자 Owner 권한 부여, ACL)
- MAC (강제적 접근 통제 — Mandatory Access Control, 보안 등급 Label 기반, 관리자 통제, Secure OS)
- RBAC (역할 기반 접근 통제 — Role-Based Access Control, 역할 Role 기반, 최소 권한 원칙)
- 벨-라파둘라 모델 (Bell-LaPadula / BLP — 기밀성 보장, No Read Up / No Write Down)
- 비바 무결성 모델 (Biba Integrity Model — 무결성 보장, No Read Down / No Write Up)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi nghiên cứu các thuật toán mã hóa khóa công khai và chữ ký số tại [07-thuat-toan-ma-hoa-va-mat-ma-hoc.md](07-thuat-toan-ma-hoa-va-mat-ma-hoc.md), hệ thống ứng dụng cần một cơ chế để nhận diện đúng người dùng (Authentication) và chỉ cấp quyền truy cập tài nguyên tương xứng (Authorization).
- **Đang giải quyết gì (Current Problem):** Bài học này cung cấp toàn bộ kiến trúc kiểm soát an ninh định danh: khung AAA, các phương thức sinh trắc học, cơ chế SSO/Kerberos, và 3 chính sách phân quyền truy cập cốt lõi cùng các mô hình toán học kiểm soát luồng thông tin (BLP, Biba).
- **Dùng đi đâu (Forward Handoff):** Khi kẻ tấn công tìm cách vượt qua hàng rào xác thực và phân quyền, chúng sẽ thực hiện các đòn tấn công mạng (DoS, DDoS, Spoofing, Malware) được phân tích chi tiết tại [09-tan-cong-mang-va-nguy-co-an-ninh.md](09-tan-cong-mang-va-nguy-co-an-ninh.md) và đòi hỏi các thiết bị bảo vệ mạng tại [10-giai-phap-va-thiet-bi-bao-mat-mang.md](10-giai-phap-va-thiet-bi-bao-mat-mang.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Khung AAA:**
  - Xác minh "Bạn là ai?" $\rightarrow$ **Authentication (인증)**.
  - Xác minh "Bạn được phép làm gì?" $\rightarrow$ **Authorization (인가 / 권한 부여)**.
  - Ghi nhận "Bạn đã làm gì và dùng bao nhiêu tài nguyên?" $\rightarrow$ **Accounting (계정 관리 / 감사)**.
- **Xác thực đa nhân tố (MFA):** Đề hỏi trường hợp nào là MFA hợp lệ $\rightarrow$ Phải chọn phương án kết hợp **2 nhóm khác loại** (ví dụ: Mật khẩu [Tri thức] + Thẻ OTP [Sở hữu]). Nếu kết hợp 2 yếu tố cùng một nhóm (Mật khẩu + Mã PIN) $\rightarrow$ Không phải là MFA.
- **3 Mô hình kiểm soát truy cập (Phải nhận diện từ khóa quyết định):**
  - Nhắc đến **"사용자의 신분(Identity)"**, **"데이터 소유자(Owner)가 권한 부여"**, **"접근 제어 목록 ACL"** $\rightarrow$ Chọn **DAC**.
  - Nhắc đến **"보안 등급(Security Label: Top Secret, Secret)"**, **"중앙 관리자"**, **"군사/정부 시스템"** $\rightarrow$ Chọn **MAC**.
  - Nhắc đến **"조직 내의 직책/직무(Role)"**, **"최소 권한의 원칙"** $\rightarrow$ Chọn **RBAC**.
- **Mô hình Bell-LaPadula vs Biba (Cực kỳ hay bị bẫy):**
  - **Bell-LaPadula (Bảo vệ Tính Bí mật - 기밀성):**
    - **NRU (No Read Up):** Không được đọc lên cấp cao hơn.
    - **NWD (No Write Down):** Không được ghi xuống cấp thấp hơn.
  - **Biba (Bảo vệ Tính Toàn vẹn - 무결성):** Đảo ngược hoàn toàn so với BLP:
    - **NRD (No Read Down):** Không được đọc từ cấp thấp hơn.
    - **NWU (No Write Up):** Không được ghi lên cấp cao hơn.

---

## 사용자 인증 및 접근 통제 보안

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khung bảo mật máy chủ AAA (AAA Framework)
Mô hình chuẩn mực để quản lý truy cập và bảo vệ tài nguyên máy chủ:
- **1. Authentication (인증 - Xác thực):** Quá trình xác minh danh tính khai báo của người dùng hoặc tiến trình (User ID và Mật khẩu, Khóa sinh trắc học).
- **2. Authorization (인가 / 권한 부여 - Cấp quyền):** Quá trình xác định quyền hạn cụ thể mà người dùng sau khi đã xác thực được phép thực hiện (đọc, sửa, xóa, thực thi) trên từng tài nguyên.
- **3. Accounting (계정 관리 / 감사 - Kiểm toán):** Quá trình theo dõi, thu thập dữ liệu và ghi nhật ký về các hoạt động, thời gian đăng nhập và lượng tài nguyên mạng/hệ thống mà người dùng đã tiêu thụ.
- **Giao thức triển khai phổ biến:** **RADIUS** (Remote Authentication Dial-In User Service) và **TACACS+** (Terminal Access Controller Access-Control System Plus).

#### 2. Các nhóm nhân tố xác thực người dùng và MFA

| Nhóm nhân tố | Tên tiếng Hàn & Anh | Yếu tố cụ thể đại diện trong đề thi |
| :--- | :--- | :--- |
| **Dựa trên tri thức** | **지식 기반 (Something You Know)** | Mật khẩu (Password), số nhận dạng cá nhân (PIN), câu hỏi bảo mật riêng tư. Dễ bị tấn công từ điển hoặc tấn công phỏng đoán. |
| **Dựa trên sở hữu** | **소유 기반 (Something You Have)** | Thẻ thông minh (Smart Card), thẻ nhớ USB Token, thiết bị tạo mã OTP (One-Time Password), tin nhắn xác thực SMS gửi tới điện thoại. |
| **Dựa trên sinh trắc** | **생체 기반 (Something You Are)** | Dấu vân tay, mống mắt (Iris), võng mạc (Retina), nhận diện khuôn mặt, tĩnh mạch mu bàn tay, giọng nói. Khó giả mạo nhất. |
| **Dựa trên vị trí/hành vi** | **위치/행위 기반 (Somewhere/Do)** | Tọa độ địa lý GPS, dải địa chỉ IP nội bộ, chữ ký tay động học, nhịp độ gõ bàn phím (Keystroke Dynamics). |

- **Xác thực đa nhân tố (Multi-Factor Authentication - MFA):**
  - **핵심 원리 (Nguyên tắc cốt lõi):**
    - [Tiếng Hàn]: `다중 요소 인증(MFA)은 서로 다른 두 가지 이상의 인증 요소를 결합하여 사용하는 방식이다.`
    - [Tiếng Việt]: MFA bắt buộc phải kết hợp ít nhất 2 nhân tố thuộc các nhóm phân loại khác nhau (ví dụ: Mật khẩu [Tri thức] $+$ OTP [Sở hữu]). Việc sử dụng Mật khẩu kết hợp với Mã PIN cá nhân chỉ là xác thực 2 bước (2-Step Verification) thuộc cùng nhóm Tri thức, hoàn toàn không đạt chuẩn MFA.
- **Các chỉ số sai số trong sinh trắc học:**
  - **FAR (False Acceptance Rate - 타인 수락률):** Tỷ lệ hệ thống nhận nhầm một người lạ/kẻ mạo danh thành người dùng hợp lệ (đe dọa an ninh).
  - **FRR (False Rejection Rate - 본인 거부률):** Tỷ lệ hệ thống từ chối nhầm chính người dùng hợp lệ (gây phiền toái cho người dùng).
  - **CER / EER (Crossover / Equal Error Rate):** Điểm cân bằng khi $\text{FAR} = \text{FRR}$. Chỉ số CER càng nhỏ thì độ chính xác và chất lượng của hệ thống nhận dạng sinh trắc học càng cao.

#### 3. Đăng nhập một lần (SSO) và Giao thức Kerberos
- **SSO (Single Sign-On):**
  - Cơ chế cho phép người dùng chỉ cần thực hiện xác thực đăng nhập thành công một lần duy nhất tại cổng trung tâm, sau đó có thể truy cập tự do vào tất cả các ứng dụng, máy chủ và dịch vụ phân tán khác nhau trong cùng phiên làm việc.
  - Giảm thiểu việc người dùng phải nhớ quá nhiều mật khẩu, tập trung hóa quản trị an ninh; tuy nhiên nếu tài khoản SSO bị lộ thì toàn bộ hệ thống liên kết sẽ bị tổn thương (Single Point of Failure).
- **Kerberos:**
  - Giao thức xác thực mạng hoạt động dựa trên mô hình Máy khách/Máy chủ (Client/Server) sử dụng công nghệ mã hóa đối xứng và **Cơ chế cấp Vé (Ticket)**.
  - Trung tâm phân phối khóa (**KDC - Key Distribution Center**) gồm hai thành phần hạt nhân:
    1. **AS (Authentication Server):** Xác thực định danh người dùng và cấp Vé cấp vé (TGT - Ticket Granting Ticket).
    2. **TGS (Ticket Granting Server):** Kiểm tra TGT và cấp Vé dịch vụ (Service Ticket) để người dùng truy cập máy chủ ứng dụng đích.

#### 4. Ba mô hình chính sách kiểm soát truy cập (Access Control Policies)

| Mô hình kiểm soát | Tên tiếng Hàn & Anh | Cơ chế cấp quyền cốt lõi | Môi trường áp dụng tiêu biểu |
| :--- | :--- | :--- | :--- |
| **Kiểm soát tùy ý** | **DAC (Discretionary Access Control)** | Dựa trên **Danh tính (Identity)** của chủ thể. **Chủ sở hữu dữ liệu (Data Owner)** có toàn quyền tự do quyết định chia sẻ, cấp hoặc thu hồi quyền truy cập cho người khác thông qua **Danh sách kiểm soát truy cập (ACL)** hoặc Ma trận kiểm soát truy cập. | Hệ điều hành thương mại thông thường (Windows, Linux tiêu chuẩn), hệ thống tệp chia sẻ nhóm. |
| **Kiểm soát bắt buộc** | **MAC (Mandatory Access Control)** | Dựa trên **Nhãn bảo mật (Security Labels)** được gắn cố định cho Chủ thể (Clearance) và Đối tượng (Classification: Tuyệt mật, Mật, Nội bộ). Quyền truy cập do **Người quản trị trung tâm** ấn định theo luật; chủ sở hữu không có quyền tự thay đổi. | Hệ thống quân sự, cơ quan tình báo, hệ điều hành bảo mật chuyên dụng (**Secure OS**). |
| **Kiểm soát theo vai trò** | **RBAC (Role-Based Access Control)** | Quyền hạn được gán cho **Vai trò/Chức danh (Role)** trong tổ chức, sau đó người dùng được chỉ định vào các vai trò tương ứng. Tuân thủ triệt để nguyên tắc **Quyền tối thiểu (Least Privilege)** và **Phân tách nhiệm vụ (Separation of Duties)**. | Doanh nghiệp lớn, ngân hàng, bệnh viện, hệ thống ERP có cấu trúc phòng ban rõ ràng. |

#### 5. Mô hình bảo mật kiểm soát luồng thông tin (Information Flow Models)

##### A. Mô hình Bell-LaPadula (BLP Model) — Trọng tâm bảo vệ Tính Bí mật (기밀성)
Được phát triển cho Bộ Quốc phòng Mỹ nhằm tuyệt đối ngăn chặn việc rò rỉ thông tin mật ra ngoài:
- **1. Thuộc tính an toàn đơn giản (Simple Security Property / No Read Up - NRU):**
  - `주체는 자신보다 높은 보안 등급의 객체를 읽을 수 없다.`
  - Chủ thể chỉ được đọc tài liệu ở cấp độ bảo mật bằng hoặc thấp hơn cấp độ của mình; tuyệt đối **không được đọc lên cấp cao hơn (No Read Up)**.
- **2. Thuộc tính $*$-Property (Constar Property / No Write Down - NWD):**
  - `주체는 자신보다 낮은 보안 등급의 객체에 기록(쓰기)할 수 없다.`
  - Chủ thể ở cấp độ bảo mật cao tuyệt đối **không được ghi dữ liệu xuống cấp độ bảo mật thấp hơn (No Write Down)** nhằm ngăn chặn việc vô tình hoặc cố ý làm lộ lọt thông tin tối mật sang vùng công cộng.

##### B. Mô hình Biba (Biba Integrity Model) — Trọng tâm bảo vệ Tính Toàn vẹn (무결성)
Được thiết kế nhằm ngăn chặn việc dữ liệu cấp thấp làm ô nhiễm hoặc sửa đổi sai lệch dữ liệu cấp cao (đảo ngược quy tắc của Bell-LaPadula):
- **1. Thuộc tính toàn vẹn đơn giản (Simple Integrity Property / No Read Down - NRD):**
  - Chủ thể tuyệt đối **không được đọc dữ liệu từ cấp độ toàn vẹn thấp hơn (No Read Down)** để tránh bị nhiễm dữ liệu sai lệch hoặc không tin cậy.
- **2. Thuộc tính $*$-Integrity Property (No Write Up - NWU):**
  - Chủ thể tuyệt đối **không được ghi dữ liệu lên cấp độ toàn vẹn cao hơn (No Write Up)** để ngăn chặn đối tượng cấp thấp làm biến dạng dữ liệu chuẩn mực của cấp cao.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Đối chiếu trực quan quy tắc giữa Bell-LaPadula và Biba

| Mô hình | Trọng tâm bảo vệ | Quy tắc Đọc (Read Rule) | Quy tắc Ghi (Write Rule) | Khẩu quyết ghi nhớ |
| :--- | :--- | :--- | :--- | :--- |
| **Bell-LaPadula (BLP)** | **Tính Bí mật (기밀성)** | **No Read Up (NRU)**: Cấm đọc trộm tài liệu mật cấp trên | **No Write Down (NWD)**: Cấm làm lộ thông tin mật xuống cấp dưới | **BLP:** Bảo vệ Bí mật $\rightarrow$ Cấm Đọc Lên, Cấm Ghi Xuống. |
| **Biba** | **Tính Toàn vẹn (무결성)** | **No Read Down (NRD)**: Cấm đọc dữ liệu rác không tin cậy cấp dưới | **No Write Up (NWU)**: Cấm sửa đổi phá hoại dữ liệu cấp trên | **Biba:** Bảo vệ Toàn vẹn $\rightarrow$ Cấm Đọc Xuống, Cấm Ghi Lên. |

#### Ma trận kiểm soát truy cập (Access Control Matrix) trong DAC
Trong mô hình DAC, quyền truy cập giữa tập hợp Chủ thể (Subjects) và tập hợp Đối tượng (Objects) được biểu diễn qua ma trận 2 chiều:
- **Cột dọc (Theo Đối tượng):** Được gọi là **Danh sách kiểm soát truy cập (ACL - Access Control List)**. Cho biết từng đối tượng tài nguyên (tệp, thư mục) cho phép những ai được làm gì.
- **Hàng ngang (Theo Chủ thể):** Được gọi là **Danh sách năng lực (Capability List)**. Cho biết một người dùng cụ thể đang nắm giữ những chiếc chìa khóa quyền hạn nào trên toàn bộ hệ thống.

---

### 복습 체크리스트
- [ ] Định nghĩa 3 thành phần của AAA: Authentication (Bạn là ai?), Authorization (Bạn được làm gì?), Accounting (Bạn đã làm gì?).
- [ ] Phân biệt 4 nhóm nhân tố xác thực: Tri thức (지식), Sở hữu (소유), Sinh trắc (생체), Vị trí/Hành vi (위치/행위).
- [ ] Nhớ nguyên tắc MFA: Bắt buộc kết hợp ít nhất 2 nhóm khác loại.
- [ ] Nắm vững chỉ số sinh trắc học: FAR (nhận nhầm kẻ gian), FRR (từ chối nhầm người nhà), CER/EER càng nhỏ càng tốt.
- [ ] Hiểu cơ chế vé Kerberos: Do KDC quản lý, gồm máy chủ xác thực AS (cấp TGT) và máy chủ cấp vé TGS (cấp vé dịch vụ).
- [ ] Phân biệt 3 mô hình phân quyền: DAC (dựa trên Identity, do Owner quyết, quản lý bằng ACL/Capability List), MAC (dựa trên Security Label, do Admin quyết), RBAC (dựa trên Role công việc).
- [ ] Thuộc lòng quy tắc Bell-LaPadula (Bí mật): No Read Up (NRU), No Write Down (NWD).
- [ ] Thuộc lòng quy tắc Biba (Toàn vẹn): No Read Down (NRD), No Write Up (NWU).
