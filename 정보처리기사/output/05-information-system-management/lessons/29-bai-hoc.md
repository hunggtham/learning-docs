# 소프트웨어 보안 (Software Security)

## 학습 목표 (Mục tiêu)
- Nắm vững các tiêu chuẩn và nguyên lý an toàn thông tin mở rộng ngoài CIA Triad: Xác thực (인증) và Chống chối bỏ (부인 방지 - Non-Repudiation).
- Phân biệt các phương pháp luận phát triển phần mềm bảo mật (Secure SDLC): CLASP, Microsoft SDL, Seven Touchpoints.
- Hiểu rõ cơ chế rà soát và khắc phục các lỗ hổng mã nguồn phổ biến theo hướng dẫn chuẩn quốc tế.

## 핵심 키워드 (Từ khóa)
- **보안 속성 (Security Attributes)**: 기밀성 (Confidentiality), 무결성 (Integrity), 가용성 (Availability), 인증 (Authentication), 부인 방지 (Non-Repudiation).
- **Secure SDLC**: CLASP (tập trung pha đầu dự án), SDL (Microsoft Security Development Lifecycle), Seven Touchpoints (7 thực hành bảo mật của Gary McGraw).
- **취약점 대응 (Vulnerability Defense)**: 입력값 검증 (Input validation), 파라미터화 쿼리 (Parameterized Queries), 시큐어 코딩 (Secure Coding).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (정보 보안 일반 및 시스템 보안 - Nền tảng CIA Triad).
- Liên kết với [32-bai-hoc.md](32-bai-hoc.md) (보안 취약점 및 보안 기능 - Chi tiết kỹ thuật các lỗ hổng).
- Liên kết với [01-software-design/03-bai-hoc.md](../../01-software-design/lessons/03-bai-hoc.md) (SDLC models).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh đặc trưng phương pháp luận:
  - Xuất hiện từ khóa "초기 단계 중심" (trọng tâm pha đầu) -> chọn ngay **CLASP**.
  - Xuất hiện từ khóa "MS사 개발" (Microsoft phát triển) -> chọn ngay **SDL**.
  - Xuất hiện từ khóa "모범사례 7가지 접점" -> chọn ngay **Seven Touchpoints**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các thuộc tính an toàn thông tin cốt lõi
| Thuộc tính (KR / EN) | Định nghĩa và Bản chất kỹ thuật | Kỹ thuật bảo đảm tiêu biểu |
| :--- | :--- | :--- |
| **기밀성 (Confidentiality)** | Chỉ người dùng hợp lệ có thẩm quyền mới được xem nội dung dữ liệu | Mã hóa đối xứng / bất đối xứng, kiểm soát quyền truy cập |
| **무결성 (Integrity)** | Dữ liệu không bị thay đổi, giả mạo hoặc phá hủy trái phép trong lưu trữ và truyền dẫn | Hàm băm mật mã (SHA-256), chữ ký số (Digital Signature) |
| **가용성 (Availability)** | Hệ thống và dữ liệu luôn có thể sử dụng được bất cứ lúc nào người dùng hợp lệ yêu cầu | Máy chủ dự phòng, sao lưu định kỳ, giải pháp cân bằng tải |
| **인증 (Authentication)** | Xác minh danh tính thực sự của người dùng, máy trạm hoặc tiến trình | Tên đăng nhập / Mật khẩu, OTP, Chứng thư số PKI, Sinh trắc |
| **부인 방지 (Non-Repudiation)** | Người gửi hoặc người nhận không thể phủ nhận hành vi đã gửi hoặc nhận thông điệp | Chữ ký điện tử kèm nhãn thời gian tin cậy (Timestamp Authority - TSA) |

#### 2. Các phương pháp luận Secure SDLC
- **Secure SDLC là gì?**: Việc bổ sung các hoạt động phân tích mối đe dọa, kiểm toán mã nguồn và kiểm thử thâm nhập vào tất cả các giai đoạn của quy trình phát triển phần mềm truyền thống (Yêu cầu -> Thiết kế -> Lập trình -> Kiểm thử -> Bảo trì).
- **3 phương pháp luận nổi tiếng thường gặp trong đề thi**:
  - **CLASP (Comprehensive, Lightweight Application Security Process)**:
    - Được thiết kế với trọng tâm tập trung vào **các giai đoạn ban đầu của dự án** (초기 단계 중심).
    - Cung cấp các hướng dẫn bảo mật thực hành gọn nhẹ, dễ áp dụng vào quy trình có sẵn mà không làm tăng gánh nặng quản lý.
  - **Microsoft SDL (Security Development Lifecycle)**:
    - Phương pháp luận do hãng Microsoft phát triển và chuẩn hóa nội bộ từ sau sáng kiến Trustworthy Computing.
    - Bắt buộc thực hiện mô hình hóa mối đe dọa (Threat Modeling) ở khâu thiết kế, rà soát mã nguồn tĩnh (Static Analysis) và kiểm thử động (Fuzz Testing) trước khi phát hành.
  - **Seven Touchpoints**:
    - Phương pháp luận của chuyên gia bảo mật Gary McGraw.
    - Xác định 7 điểm tiếp xúc thực hành bảo mật tốt nhất (Best Practices) độc lập với quy trình quản lý, bao gồm: Đánh giá mã nguồn bảo mật, Mô hình hóa rủi ro thiết kế, Kiểm thử bảo mật dựa trên rủi ro, Kiểm thử thâm nhập, v.v.

#### 3. Các quy tắc lập trình an toàn (Secure Coding)
- **Phòng thủ SQL Injection**: Tuyệt đối không nối chuỗi văn bản trực tiếp từ đầu vào người dùng vào câu lệnh SQL; luôn sử dụng tham số hóa (`PreparedStatement` trong Java, `@parameter` trong .NET).
- **Phòng thủ XSS**: Thực hiện mã hóa thực thể HTML (`<` thành `&lt;`, `>` thành `&gt;`) đối với toàn bộ dữ liệu người dùng nhập trước khi hiển thị lên giao diện trình duyệt.
- **Phòng ngừa rò rỉ thông tin qua thông báo lỗi**: Tùy chỉnh thông báo lỗi tổng quát hiển thị cho người dùng cuối (ví dụ: "Đã xảy ra sự cố kỹ thuật"), không in chi tiết dấu vết ngăn xếp (Stack Trace) hay thông tin tài khoản cơ sở dữ liệu.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Ánh xạ các hoạt động bảo mật vào từng pha SDLC
```
[Pha Yêu cầu] ──► Phân tích yêu cầu bảo mật, xác định quy định pháp lý (개인정보보호법)
       │
[Pha Thiết kế] ──► Mô hình hóa mối đe dọa (Threat Modeling - STRIDE), thiết kế kiến trúc bảo mật
       │
[Pha Cài đặt] ──► Lập trình an toàn (Secure Coding Standards), phân tích mã tĩnh (Static Analysis)
       │
[Pha Kiểm thử] ──► Kiểm thử thâm nhập (Penetration Test), kiểm thử Fuzzing, quét lỗ hổng động (DAST)
       │
[Pha Vận hành] ──► Quản lý bản vá (Patch Management), giám sát an ninh liên tục, ứng phó sự cố
```

#### 2. Mô hình hóa mối đe dọa STRIDE của Microsoft
- **S**poofing identity (Mạo danh người dùng) $\rightarrow$ Vi phạm **인증 (Authentication)**.
- **T**ampering with data (Làm sai lệch dữ liệu) $\rightarrow$ Vi phạm **무결성 (Integrity)**.
- **R**epudiation (Chối bỏ hành động) $\rightarrow$ Vi phạm **부인 방지 (Non-Repudiation)**.
- **I**nformation disclosure (Lộ lọt thông tin) $\rightarrow$ Vi phạm **기밀성 (Confidentiality)**.
- **D**enial of service (Từ chối dịch vụ) $\rightarrow$ Vi phạm **가용성 (Availability)**.
- **E**levation of privilege (Leo thang đặc quyền) $\rightarrow$ Vi phạm **권한 통제 (Authorization)**.

---

### 복습 체크리스트
- [ ] Phân biệt được điểm khác nhau căn bản giữa thuộc tính 무결성 (Integrity) và 부인 방지 (Non-Repudiation)?
- [ ] Ba phương pháp luận Secure SDLC (CLASP, SDL, Seven Touchpoints) có đặc trưng phân biệt nào?
- [ ] Để phòng ngừa SQL Injection, kỹ thuật lập trình nào là bắt buộc phải sử dụng?
- [ ] Mô hình đe dọa STRIDE liên kết 6 chữ cái với những thuộc tính an toàn thông tin nào?
