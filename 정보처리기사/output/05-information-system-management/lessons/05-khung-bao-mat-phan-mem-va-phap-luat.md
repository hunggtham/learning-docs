# 소프트웨어 개발 보안 체계 및 관련 법규 (Khung bảo mật phát triển phần mềm Secure SDLC, CLASP & Hệ thống pháp luật PIPA)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 thuộc tính an toàn thông tin nền tảng (CIA Triad: 기밀성, 무결성, 가용성) và 2 thuộc tính mở rộng: Xác thực (인증 - Authentication) và Chống chối bỏ (부인 방지 - Non-Repudiation).
- Phân biệt các phương pháp luận phát triển phần mềm bảo mật (Secure SDLC): **MS-SDL**, **Seven Touchpoints**, và **CLASP**.
- Hiểu rõ tiêu chuẩn quốc tế về đánh giá an toàn thông tin **Common Criteria (CC / ISO/IEC 15408)** cùng các khái niệm PP, ST, EAL.
- Nắm vững các đạo luật bảo mật CNTT cốt lõi của Hàn Quốc: **Đạo luật bảo vệ thông tin cá nhân (개인정보 보호법)**, Luật mạng thông tin truyền thông (정보통신망법) và Tiêu chuẩn chứng nhận **ISMS-P**.
- Nhận diện các lỗi chức năng bảo mật phổ biến: Mật khẩu mã hóa cứng (Hardcoded Keys), lưu truyền bản rõ và rò rỉ thông tin qua thông báo lỗi hệ thống.

## 핵심 키워드 (Từ khóa song ngữ)
- 보안 3대 요소 (CIA Triad — 기밀성 Confidentiality, 무결성 Integrity, 가용성 Availability)
- 부인 방지 (Non-Repudiation — Chống chối bỏ bằng chữ ký số và nhật ký xác thực)
- Secure SDLC (소프트웨어 개발 보안 생명주기 — Tích hợp bảo mật xuyên suốt các pha phát triển)
- CLASP (Comprehensive, Lightweight Application Security Process — Tập trung bảo mật pha đầu)
- MS-SDL (Microsoft Security Development Lifecycle — Mô hình STRIDE, kiểm thử bảo mật)
- 공통평가기준 (CC - Common Criteria / ISO/IEC 15408 — PP, ST, EAL 1~7)
- 개인정보 보호법 (Personal Information Protection Act — PIPA, mã hóa mật khẩu và số định danh)
- ISMS-P (Information Security Management System - Personal — Chứng nhận quản trị an toàn thông tin)
- 하드코드된 자격증명 (Hardcoded Credentials — Nguy cơ lộ khóa bí mật trong mã nguồn)
- 오류 메시지 정보 노출 (Information Exposure through Error Messages — Rò rỉ cấu trúc DB qua Stack Trace)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Sau khi thiết lập quy trình quản lý chất lượng tại [04-tieu-chuan-chat-luong-va-cmmi.md](04-tieu-chuan-chat-luong-va-cmmi.md), phần mềm cần một khuôn khổ thể chế và quy trình để kiểm soát rủi ro an ninh mạng trước khi đi vào giai đoạn lập trình.
- **Đang giải quyết gì (Current Problem):** Bài học này xây dựng hệ thống quy chuẩn bảo mật toàn diện: từ các mục tiêu an ninh tối thượng, quy trình Secure SDLC chuẩn quốc tế, tiêu chuẩn đánh giá CC cho đến hành lang pháp lý bắt buộc (PIPA) để bảo vệ dữ liệu người dùng.
- **Dùng đi đâu (Forward Handoff):** Các nguyên tắc của Secure SDLC được hiện thực hóa trực tiếp qua các kỹ thuật lập trình phòng thủ và vá lỗ hổng mã nguồn trong [06-lo-hong-phan-mem-va-secure-coding.md](06-lo-hong-phan-mem-va-secure-coding.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Thuộc tính an toàn:**
  - Nhắc đến **"인가되지 않은 사용자의 접근/열람 통제" (Ngăn chặn đọc trái phép)** $\rightarrow$ **기밀성 (Confidentiality)**.
  - Nhắc đến **"데이터의 위·변조 방지" (Chống sửa đổi, giả mạo dữ liệu)** $\rightarrow$ **무결성 (Integrity)**.
  - Nhắc đến **"권한 있는 사용자가 필요할 때 언제든 접근 보장" (Bảo đảm luôn sẵn sàng truy cập)** $\rightarrow$ **가용성 (Availability)**.
  - Nhắc đến **"송·수신 사실을 증명하여 행위를 부인하지 못하게 함" (Bằng chứng chống chối bỏ)** $\rightarrow$ **부인 방지 (Non-Repudiation)**.
- **Phương pháp luận Secure SDLC:**
  - Nhắc đến **"초기 단계에서 보안을 강화하기 위한 경량 프로세스" (Quy trình nhẹ tập trung vào các pha ban đầu)** $\rightarrow$ Chọn ngay **CLASP**.
  - Nhắc đến mô hình bảo mật của Microsoft áp dụng mô hình đe dọa **STRIDE** $\rightarrow$ Chọn **MS-SDL**.
- **Pháp luật bảo mật (PIPA):**
  - Mật khẩu người dùng (비밀번호) $\rightarrow$ Bắt buộc dùng **단방향 암호화 (Mã hóa một chiều / Hash)**.
  - Số định danh cá nhân độc nhất (주민등록번호, 여권번호, 운전면허번호) $\rightarrow$ Bắt buộc dùng **안전한 양방향 암호화 (Mã hóa hai chiều an toàn)** khi lưu trữ hoặc truyền trên mạng.
- **Xử lý lỗi an toàn:** Tuyệt đối không để lộ **Stack Trace, câu truy vấn SQL hay đường dẫn thư mục nội bộ** ra màn hình người dùng; chỉ trả về thông báo lỗi chung chung (Generic Error Page).

---

## 소프트웨어 개발 보안 체계 및 관련 법규

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các thuộc tính an toàn thông tin cốt lõi (Security Attributes)

| Thuộc tính | Tên tiếng Hàn & Anh | Bản chất kỹ thuật & Điểm thi trọng tâm |
| :--- | :--- | :--- |
| **Tính bí mật** | **기밀성 (Confidentiality)** | Chỉ những đối tượng (User/System) được phân quyền hợp lệ mới được phép đọc hoặc truy cập thông tin. Biện pháp bảo vệ chính là **Mã hóa (Encryption)** và **Kiểm soát truy cập (Access Control)**. |
| **Tính toàn vẹn** | **무결성 (Integrity)** | Dữ liệu không bị xóa bỏ, giả mạo, chèn thêm hoặc sửa đổi trái phép trong quá trình lưu trữ và truyền tải. Biện pháp bảo vệ chính là **Hàm băm (Hash)** và **Chữ ký số (Digital Signature)**. |
| **Tính khả dụng** | **가용성 (Availability)** | Hệ thống và dữ liệu luôn sẵn sàng phục vụ khi người dùng hợp lệ có nhu cầu sử dụng. Bị đe dọa nghiêm trọng bởi các cuộc tấn công **Từ chối dịch vụ (DoS/DDoS)** và thảm họa hạ tầng. |
| **Xác thực** | **인증 (Authentication)** | Quá trình kiểm tra và xác minh tính chính danh của người dùng hoặc hệ thống (User ID, Mật khẩu, OTP, Sinh trắc học). |
| **Chống chối bỏ** | **부인 방지 (Non-Repudiation)** | Ngăn chặn việc người gửi phủ nhận đã gửi thông điệp hoặc người nhận phủ nhận đã nhận thông điệp; dựa trên bằng chứng kỹ thuật từ **Chữ ký số (전자서명)** và hệ thống chứng thực **PKI**. |

#### 2. Các phương pháp luận phát triển phần mềm bảo mật (Secure SDLC)
Secure SDLC là quy trình đưa các hoạt động kiểm tra an ninh, rà soát mã nguồn và kiểm thử lỗ hổng vào từng giai đoạn của vòng đời SDLC truyền thống:

- **1. CLASP (Comprehensive, Lightweight Application Security Process):**
  - Do OWASP tiếp quản, là quy trình có tính linh hoạt và nhẹ nhàng (Lightweight).
  - Có thể áp dụng linh hoạt cho mọi mô hình SDLC, đặc biệt tập trung vào **các hoạt động bảo mật ngay từ giai đoạn lập kế hoạch và phân tích ban đầu** của dự án.
- **2. MS-SDL (Microsoft Security Development Lifecycle):**
  - Phương pháp luận bảo mật chuẩn mực của Microsoft.
  - Tích hợp kỹ thuật mô hình hóa mối đe dọa (**STRIDE Threat Modeling**) ở pha thiết kế và bắt buộc kiểm tra mã tĩnh/động trước khi phát hành.
- **3. Seven Touchpoints (Gary McGraw):**
  - Đưa ra 7 điểm tiếp xúc bảo mật thực hành tốt nhất: Kiểm toán mã nguồn bảo mật (Code Review), Mô hình hóa rủi ro, Kiểm thử thâm nhập (Penetration Testing), Xây dựng kịch bản lạm dụng (Abuse Cases).

#### 3. Tiêu chuẩn đánh giá an toàn thông tin Common Criteria (CC / ISO/IEC 15408)
- **개념 (Khái niệm):** Tiêu chuẩn quốc tế thống nhất dùng để đánh giá và chứng nhận độ an toàn của các sản phẩm và hệ thống công nghệ thông tin.
- **Các thành phần cốt lõi:**
  - **보호프로필 (PP - Protection Profile):** Bộ yêu cầu an toàn độc lập với sản phẩm, do người tiêu dùng hoặc cơ quan quản lý ban hành nhằm chuẩn hóa yêu cầu cho một nhóm sản phẩm (ví dụ: PP cho Tường lửa).
  - **보안목표명세서 (ST - Security Target):** Bản mô tả cụ thể về mục tiêu và cơ chế bảo mật do nhà sản xuất viết riêng cho sản phẩm cụ thể cần chứng nhận.
  - **보증 등급 (EAL - Evaluation Assurance Level):** Thang đo mức độ tin cậy bảo đảm an toàn, chia thành 7 mức từ **EAL 1 (thấp nhất) đến EAL 7 (cao nhất)**.

#### 4. Hành lang pháp lý bảo mật CNTT tại Hàn Quốc (IT Security Regulations)

| Văn bản luật | Tên tiếng Hàn | Phạm vi điều chỉnh & Quy định bắt buộc trong đề thi |
| :--- | :--- | :--- |
| **Đạo luật bảo vệ thông tin cá nhân** | **개인정보 보호법 (PIPA)** | - Đạo luật cơ sở bao trùm toàn bộ mọi cá nhân, doanh nghiệp và cơ quan nhà nước xử lý thông tin cá nhân.<br>- **Mật khẩu (비밀번호):** Bắt buộc mã hóa **một chiều (단방향 - Hash)** kèm Salt.<br>- **Số định danh duy nhất (주민등록번호, 여권번호 등):** Bắt buộc mã hóa **hai chiều an toàn (안전한 양방향)** khi lưu trữ trong CSDL và khi truyền qua mạng công cộng. |
| **Luật mạng thông tin truyền thông** | **정보통신망법** | Điều chỉnh các nhà cung cấp dịch vụ Internet, sàn thương mại điện tử, viễn thông; quy định trách nhiệm bồi thường khi lộ lọt dữ liệu. |
| **Hệ thống chứng nhận ISMS-P** | **ISMS-P 인증 제도** | Hệ thống chứng nhận hợp nhất tiêu chuẩn Quản trị an ninh thông tin (ISMS) và Bảo vệ dữ liệu cá nhân (PIMS) của Hàn Quốc. |

#### 5. Phòng ngừa lỗi chức năng bảo mật và xử lý ngoại lệ
- **1. Tránh lưu trữ thông tin xác thực mã hóa cứng (Hardcoded Credentials):**
  - Tuyệt đối không nhúng chuỗi kết nối CSDL, API Key, hoặc mật khẩu tài khoản quản trị trực tiếp trong mã nguồn code hoặc tệp cấu hình không mã hóa. Phải sử dụng biến môi trường (Environment Variables) hoặc dịch vụ quản lý khóa chuyên dụng (AWS Secrets Manager, HashiCorp Vault).
- **2. Phòng ngừa lộ lọt thông tin qua thông báo lỗi (Information Leakage through Error Messages):**
  - **Nguy cơ:** Khi ứng dụng gặp lỗi ngoại lệ (Exception), nếu in nguyên văn dấu vết ngăn xếp (Stack Trace) hoặc câu truy vấn SQL ra trình duyệt, kẻ tấn công sẽ nắm được cấu trúc bảng CSDL, phiên bản máy chủ và đường dẫn tệp để thực hiện các cuộc tấn công tiếp theo.
  - **Biện pháp:** Bắt toàn bộ ngoại lệ bằng khối `try-catch`, ghi chi tiết lỗi vào tệp log an toàn nội bộ máy chủ, và chỉ hiển thị một trang thông báo lỗi chung thân thiện (Custom Generic Error Page) cho người dùng cuối.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Mô hình đe dọa STRIDE trong MS-SDL
Mô hình STRIDE phân loại các mối đe dọa an ninh phần mềm tương ứng với các mục tiêu bảo vệ:
- **S - Spoofing (Mạo danh):** Đe dọa đến Tính xác thực (Authentication).
- **T - Tampering (Can thiệp/Sửa đổi):** Đe dọa đến Tính toàn vẹn (Integrity).
- **R - Repudiation (Chối bỏ):** Đe dọa đến Tính chống chối bỏ (Non-Repudiation).
- **I - Information Disclosure (Tiết lộ thông tin):** Đe dọa đến Tính bí mật (Confidentiality).
- **D - Denial of Service (Từ chối dịch vụ):** Đe dọa đến Tính khả dụng (Availability).
- **E - Elevation of Privilege (Leo thang đặc quyền):** Đe dọa đến Phân quyền kiểm soát truy cập (Authorization).

---

### 복습 체크리스트
- [ ] Nắm vững 3 yếu tố CIA Triad: 기밀성 (Bí mật - chống đọc trộm), 무결성 (Toàn vẹn - chống sửa đổi), 가용성 (Khả dụng - luôn sẵn sàng phục vụ).
- [ ] Nhớ thuộc tính 부인 방지 (Non-Repudiation): Chống chối bỏ bằng chữ ký số.
- [ ] Phân biệt Secure SDLC: CLASP là quy trình nhẹ tập trung vào các pha ban đầu; MS-SDL áp dụng STRIDE.
- [ ] Nhớ các thành phần của Common Criteria: PP (Hồ sơ bảo vệ chuẩn), ST (Đặc tả mục tiêu cụ thể), EAL 1~7.
- [ ] Nắm vững luật PIPA: Mật khẩu bắt buộc mã hóa 1 chiều (Hash); Số định danh cư dân bắt buộc mã hóa 2 chiều an toàn.
- [ ] Hiểu nguyên tắc xử lý lỗi: Không bao giờ hiển thị Stack Trace ra ngoài, chỉ hiển thị thông báo lỗi chung (Generic Error Page).
