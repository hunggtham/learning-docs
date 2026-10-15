# 5. 보안 및 암호화 (Security & Encryption)

## 학습 목표 (Mục tiêu)
- Nắm vững 3 mục tiêu cốt lõi của an toàn thông tin (`보안의 3대 요소`): Tính bí mật (`기밀성`), Tính toàn vẹn (`무결성`), và Tính sẵn sàng (`가용성`).
- Phân biệt tuyệt đối giữa Mật mã khóa đối xứng (`대칭키 암호화` - DES, AES, SEED) và Mật mã khóa bất đối xứng (`비대칭키 / 공개키 암호화` - RSA, ECC).
- Nắm vững 3 mô hình kiểm soát truy cập tiêu chuẩn: Kiểm soát tùy quyền (`DAC`), Kiểm soát bắt buộc (`MAC`), và Kiểm soát theo vai trò (`RBAC`).

## 핵심 키워드 (Từ khóa)
- 보안 3대 요소 (CIA Triad: 기밀성, 무결성, 가용성)
- 대칭키 암호화 (Symmetric Key / 비밀키 / DES, AES, SEED, ARIA / 고속)
- 비대칭키 암호화 (Asymmetric Key / 공개키 / RSA, ECC / 키 관리 용이)
- 일방향 해시 함수 (One-Way Hash Function: SHA-256, MD5)
- 접근 통제 모델 (Mô hình kiểm soát truy cập: DAC, MAC, RBAC)
- 벨-라파둘라 (Bell-LaPadula / 기밀성), 비바 (Biba / 무결성)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. 병행 제어 (Concurrency Control)](47-bai-hoc.md)):** Sau khi bảo vệ tính nhất quán dữ liệu trước các xung đột đồng thời, bài này thiết lập hàng rào phòng thủ bảo mật trước các nguy cơ tấn công đánh cắp và sửa đổi dữ liệu trái phép.
- **Tiếp nối sang bài sau ([6. 분산 데이터베이스 (Distributed Database)](49-bai-hoc.md)):** Khảo sát cấu trúc cơ sở dữ liệu phân tán và 4 tính trong suốt đặc thù.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nhớ bảng so sánh đối xứng (nhanh, 1 khóa, DES/AES) vs bất đối xứng (chậm, 2 khóa công khai/bí mật, RSA/ECC) và 3 mô hình kiểm soát truy cập (DAC chủ sở hữu, MAC cấp bậc quân đội, RBAC vai trò chức vụ).
- Đọc TẦNG B để hiểu cơ chế chữ ký số: Dùng Khóa bí mật của người gửi để ký, và dùng Khóa công khai của người gửi để xác minh chữ ký.

---

## 5. 보안 및 암호화 (Security & Encryption)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 3 mục tiêu an toàn thông tin kinh điển (보안의 3대 요소 - CIA Triad):**
  - `기밀성 (Confidentiality - Tính bí mật)`: Đảm bảo thông tin chỉ được phép truy cập và đọc bởi những đối tượng người dùng hợp pháp được cấp quyền; ngăn chặn rò rỉ dữ liệu trái phép.
  - `무결성 (Integrity - Tính toàn vẹn)`: Đảm bảo thông tin không bị sửa đổi, xóa bỏ hoặc làm sai lệch một cách tùy tiện, duy trì độ chính xác tuyệt đối từ nguồn.
  - `가용성 (Availability - Tính sẵn sàng)`: Đảm bảo hệ thống và dữ liệu luôn ở trạng thái sẵn sàng phục vụ khi người dùng hợp pháp có nhu cầu truy cập.
- **2. So sánh Mật mã đối xứng vs Mật mã bất đối xứng:**
  - **대칭키 암호화 (Mật mã khóa đối xứng / Khóa bí mật - Secret Key):**
    - **Cơ chế:** Dùng **DUY NHẤT 1 KHÓA** cho cả quá trình mã hóa dữ liệu lẫn giải mã dữ liệu (`암호화키 = 복호화키`).
    - *Ưu điểm:* Thuật toán tính toán đơn giản, **tốc độ mã hóa cực nhanh (`속도가 빠름`)**, rất thích hợp để mã hóa các tệp dữ liệu dung lượng lớn.
    - *Nhược điểm:* Khó khăn lớn trong việc phân phối và lưu trữ khóa an toàn giữa các bên; khi số người $N$ tăng, số khóa cần quản lý tăng vọt theo công thức $\frac{N(N-1)}{2}$.
    - *Các thuật toán tiêu biểu:*
      - `Khối (Block)`: **DES** (64-bit block, 56-bit key - chuẩn cũ IBM), **AES** (128/192/256-bit - chuẩn mới NIST), **SEED** (chuẩn Hàn Quốc KISA 128-bit), **ARIA** (chuẩn Hàn Quốc NSRI).
      - `Dòng (Stream)`: **RC4**.
  - **비대칭키 / 공개키 암호화 (Mật mã khóa bất đối xứng / Khóa công khai - Public Key):**
    - **Cơ chế:** Sử dụng **MỘT CẶP KHÓA (2 khóa khác nhau)**: **Khóa công khai (`공개키 - Public Key`)** dùng để mã hóa (công bố cho mọi người), và **Khóa bí mật (`비밀키 / 개인키 - Private Key`)** dùng để giải mã (chỉ người nhận giữ bí mật).
    - *Ưu điểm:* Quản lý và phân phối khóa cực kỳ dễ dàng (mỗi người chỉ cần 1 cặp khóa, tổng cộng chỉ cần $2N$ khóa); là nền tảng của **Chữ ký số (`전자서명`)** và xác thực không thể chối bỏ (Non-repudiation).
    - *Nhược điểm:* Cấu trúc toán học phức tạp nên **tốc độ mã hóa rất chậm (`속도가 느림`)**.
    - *Các thuật toán tiêu biểu:* **RSA** (dựa trên độ khó của bài toán phân tích thừa số nguyên tố lớn), **ECC** (đường cong Elliptic - khóa ngắn nhưng độ bảo mật tương đương RSA), **ElGamal**, **Diffie-Hellman** (giao thức trao đổi khóa).
- **3. Mô hình kiểm soát truy cập (접근 통제 모델 - Access Control Models):**
  - `DAC (Discretionary Access Control - Kiểm soát truy cập tùy quyền)`: Quyền truy cập tài nguyên do chính **Chủ sở hữu dữ liệu (`데이터 소유자`)** tự quyết định cấp hoặc thu hồi cho người dùng khác dựa trên Danh tính cá nhân (Identity / User ID).
  - `MAC (Mandatory Access Control - Kiểm soát truy cập bắt buộc)`: Phân quyền tự động dựa trên **Cấp độ bảo mật (`보안 등급`)** của tài nguyên (Tuyệt mật, Mật, Nội bộ) so với Thẩm quyền bảo mật của người dùng (áp dụng nghiêm ngặt trong quân đội, chính phủ).
  - `RBAC (Role-Based Access Control - Kiểm soát truy cập theo vai trò)`: Phân quyền dựa trên **Vai trò / Vị trí công việc (`역할 - Role`)** của người dùng trong tổ chức (ví dụ: vai trò Kế toán, Giám đốc, Bác sĩ). Dễ quản lý nhân sự khi có biến động luân chuyển vị trí.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Thuật toán SEED và ARIA thuộc loại mật mã nào?"* -> **대칭키 암호화 (Mật mã đối xứng)**, chuẩn quốc gia của Hàn Quốc.
  - **Bẫy 2:** *"RSA dựa trên bài toán toán học nào?"* -> **Độ khó của việc phân tích thừa số nguyên tố lớn (소인수 분해의 어려움)**.
  - **Bẫy 3:** *"Mô hình phân quyền dựa trên chức vụ và vai trò của người dùng trong công ty là gì?"* -> **RBAC (Role-Based Access Control)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Đối xứng 1 khóa nhanh (DES, AES, SEED), Bất đối xứng 2 khóa an toàn (RSA, ECC); DAC tùy chủ, MAC cấp bậc quân đội, RBAC theo vai trò chức danh".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cơ chế Chữ ký số (Digital Signature) vs Mã hóa dữ liệu:**
  - **Mã hóa bảo mật thông điệp:** Người gửi lấy **Khóa công khai của người nhận** để mã hóa $\rightarrow$ Chỉ người nhận có **Khóa bí mật của mình** mới giải mã được.
  - **Ký số xác thực danh tính:** Người gửi lấy **Khóa bí mật của chính mình** để ký lên bản băm (Hash) của tài liệu $\rightarrow$ Bất kỳ ai cũng có thể dùng **Khóa công khai của người gửi** để kiểm tra tính toàn vẹn và xác thực nguồn gốc.

### 복습 체크리스트
- [ ] Định nghĩa được 3 trụ cột an toàn thông tin: 기밀성, 무결성, 가용성.
- [ ] Phân biệt được ưu nhược điểm của 대칭키 (nhanh, 1 khóa) và 비대칭키 (chậm, 2 khóa).
- [ ] Kể tên đúng nhóm: DES, AES, SEED thuộc đối xứng; RSA, ECC thuộc bất đối xứng.
- [ ] Phân biệt rõ ràng 3 mô hình kiểm soát truy cập: DAC (chủ sở hữu), MAC (bắt buộc theo cấp bậc), RBAC (theo vai trò).
