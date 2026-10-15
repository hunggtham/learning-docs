# 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

## 학습 목표 (Mục tiêu)
- Nắm vững và phân biệt bản chất giữa hai trường phái mã hóa: **Mã hóa khóa đối xứng (Khóa bí mật - `개인키 / 비밀키 / 대칭키`)** và **Mã hóa khóa bất đối xứng (Khóa công khai - `공개키 / 비대칭키`)**.
- Phân biệt chi tiết 3 mô hình kiểm soát truy cập dữ liệu cốt lõi: **Kiểm soát truy cập tùy ý (DAC - `임의 접근통제`)**, **Kiểm soát truy cập bắt buộc (MAC - `강제 접근통제`)**, và **Kiểm soát truy cập dựa trên vai trò (RBAC - `역할기반 접근통제`)**.
- Hiểu sâu các mô hình bảo mật kinh điển của MAC: **Bell-LaPadula (Bảo vệ tính bí mật - `기밀성`)**, **Biba (Bảo vệ tính toàn vẹn - `무결성`)**, **Clark-Wilson**, và **Chinese Wall (Tránh xung đột lợi ích)**.

## 핵심 키워드 (Từ khóa)
- 개인키 / 대칭키 암호 (Khóa đối xứng: DES, AES, SEED, ARIA)
- 공개키 / 비대칭키 암호 (Khóa bất đối xứng: RSA, ECC)
- 접근통제 (Kiểm soát truy cập / Access Control)
- DAC (임의 접근통제 / Discretionary Access Control: 소유자 기준)
- MAC (강제 접근통제 / Mandatory Access Control: 보안 등급 기준)
- RBAC (역할기반 접근통제 / Role-Based Access Control: 역할 기준)
- 벨-라파듈라 모델 (Bell-LaPadula / BLP: 기밀성, No Read Up, No Write Down)
- 비바 모델 (Biba: 무결성, No Read Down, No Write Up)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ các bài trước ([26-bai-hoc.md](26-bai-hoc.md), [28-bai-hoc.md](28-bai-hoc.md), [38-bai-hoc.md](38-bai-hoc.md)):** Lệnh DCL `GRANT / REVOKE` trong SQL chính là phương tiện hiện thực hóa mô hình kiểm soát truy cập tùy ý DAC trên thực tế.
- **Tiếp nối sang bài sau ([40-bai-hoc.md](40-bai-hoc.md)):** Để bảo vệ cấu trúc quan hệ ở cấp độ sâu nhất, các quyền truy cập được áp đặt chi tiết lên từng Tuple (hàng) và Attribute (cột).

## 읽는 방법 (Cách đọc)
- Học thuộc bảng so sánh Mã hóa đối xứng vs Bất đối xứng:
  - Đối xứng (Symmetric): **Dùng 1 khóa chung $\rightarrow$ Tốc độ CỰC NHANH**, nhưng khó quản lý phân phối khóa.
  - Bất đối xứng (Asymmetric): **Dùng 2 khóa (Công khai + Bí mật) $\rightarrow$ Dễ quản lý khóa**, nhưng tốc độ chậm.
- Nhớ câu thần chú 3 mô hình Access Control:
  - **DAC:** Do **Chủ sở hữu (소유자)** quyết định.
  - **MAC:** Do **Cấp độ bảo mật hệ thống (보안 등급)** áp đặt.
  - **RBAC:** Do **Chức vụ / Vai trò (역할)** trong công ty quyết định.
- Nhớ 2 mô hình quân sự: **Bell-LaPadula = Tính bí mật (기밀성)**; **Biba = Tính toàn vẹn (무결성)**.

---

## 19. 암호화 기법과 접근 통제 (Kỹ thuật Mã hóa và Kiểm soát Truy cập)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng so sánh 2 trường phái Mã hóa dữ liệu:**
  | Tiêu chí so sánh | 개인키 / 대칭키 암호 (Khóa đối xứng) | 공개키 / 비대칭키 암호 (Khóa bất đối xứng) |
  |---|---|---|
  | **Số lượng khóa** | Dùng **DUY NHẤT 1 khóa** chung cho cả mã hóa và giải mã | Dùng **CẶP 2 KHÓA khác nhau** (Khóa công khai để mã hóa, Khóa bí mật để giải mã) |
  | **Tốc độ xử lý** | **Cực kỳ nhanh** (Thuật toán đơn giản) | **Chậm** (Phải tính toán các phép toán số học phức tạp) |
  | **Quản lý khóa** | **Rất khó khăn** khi số người dùng tăng (Cần $N(N-1)/2$ khóa) | **Dễ dàng** và an toàn (Mỗi người chỉ cần giữ 1 cặp khóa, tổng $2N$ khóa) |
  | **Thuật toán tiêu biểu** | - Khối (Block): `DES`, `AES`, `SEED` (Hàn Quốc), `ARIA` (Hàn Quốc) ; - Luồng (Stream): `RC4`. | `RSA` (dựa trên bài toán phân tích thừa số nguyên tố lớn), `ECC` (đường cong Elliptic). |

- **2. Bảng 3 mô hình Kiểm soát truy cập (접근통제 3대 기술):**
  | Mô hình | Thuật ngữ Hàn - Anh | Tiêu chí trao quyền | Đặc điểm thi trắc nghiệm |
  |---|---|---|---|
  | **DAC** | `임의 접근통제` (Discretionary) | **Chủ sở hữu dữ liệu (`데이터 소유자`)** | Chủ dữ liệu toàn quyền tự do cấp hoặc thu hồi quyền truy cập đối tượng của mình cho người khác thông qua lệnh SQL `GRANT` và `REVOKE`. |
  | **MAC** | `강제 접근통제` (Mandatory) | **Cấp bậc bảo mật (`보안 등급 / 레이블`)** | Hệ thống tự động cưỡng chế quyền dựa trên mức độ bảo mật của dữ liệu (Tuyệt mật, Bí mật, Thường) và thẩm quyền của người dùng. Người dùng không thể tự ý chuyển quyền. |
  | **RBAC** | `역할기반 접근통제` (Role-Based) | **Vai trò / Chức vụ (`역할 / Role`)** | Quyền hạn được gắn vào Vai trò (Giám đốc, Kế toán, Nhân viên). Người dùng nhận quyền tự động khi được bổ nhiệm vai trò; rất phù hợp cho doanh nghiệp. |

- **3. Các mô hình bảo mật của MAC trong đề thi:**
  - **벨-라파듈라 모델 (Bell-LaPadula / BLP):**
    - Tập trung tuyệt đối vào **Tính bí mật (`기밀성`)** trong môi trường quân sự.
    - Quy tắc: **No Read Up (Không được đọc tài liệu có cấp bậc cao hơn)**; **No Write Down (Không được ghi dữ liệu mật xuống cấp bậc thấp hơn)** nhằm chống rò rỉ tin mật.
  - **비바 모델 (Biba Model):**
    - Tập trung tuyệt đối vào **Tính toàn vẹn (`무결성`)**. Ngược lại với BLP.
    - Quy tắc: **No Read Down (Không đọc dữ liệu ở cấp thấp hơn)** để tránh bị nhiễm dữ liệu rác/sai lệch; **No Write Up (Không ghi đè lên tài liệu cấp cao hơn)**.
  - **클락-윌슨 모델 (Clark-Wilson Model):** Bảo vệ tính toàn vẹn trong thương mại, buộc mọi sửa đổi phải thông qua các tiến trình phần mềm được xác thực (Well-formed Transactions).
  - **차이니즈 월 모델 (Chinese Wall Model):** Ngăn ngừa **Xung đột lợi ích (`이해 충돌 방지`)** trong tài chính và tư vấn kinh doanh.
- **주의/함정 (Bẫy đề thi trắc nghiệm):**
  - Đề hỏi: *"Mô hình bảo mật Bell-LaPadula ưu tiên yếu tố nào?"* $\rightarrow$ Đáp án: **기밀성 (Tính bí mật / Confidentiality)**.
  - Đề hỏi: *"Mô hình kiểm soát truy cập nào gắn quyền hạn với chức vụ của người dùng trong tổ chức?"* $\rightarrow$ Đáp án: **RBAC (역할기반 접근통제)**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Minh họa quy tắc No Read Up / No Write Down của Bell-LaPadula:**
  - Cán bộ có quyền cấp "Bí mật" (Secret):
    - Được đọc tài liệu cấp "Bí mật" và "Thường".
    - **Không được đọc tài liệu cấp "Tuyệt mật" (Top Secret)** $\rightarrow$ **No Read Up**.
    - Khi viết báo cáo, **không được ghi thông tin vào tài liệu cấp "Thường" (Unclassified)** để tránh vô tình tiết lộ bí mật ra ngoài $\rightarrow$ **No Write Down**.

### 복습 체크리스트
- [ ] Phân biệt được ưu nhược điểm của 대칭키 (nhanh, khó quản lý khóa) và 비대칭키 (chậm, dễ quản lý khóa).
- [ ] Kể tên các thuật toán: DES, AES, SEED (đối xứng) vs RSA, ECC (bất đối xứng).
- [ ] Phân biệt rõ 3 mô hình: DAC (chủ sở hữu), MAC (cấp bậc bảo mật), RBAC (vai trò chức vụ).
- [ ] Nắm vững quy tắc No Read Up / No Write Down của mô hình Bell-LaPadula.
