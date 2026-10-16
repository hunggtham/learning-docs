# 암호 알고리즘 및 암호화 기법 (Thuật toán mật mã học, Mã hóa đối xứng & Bất đối xứng)

## 학습 목표 (Mục tiêu)
- Phân biệt toàn diện hai trường phái mật mã học: **Mã hóa khóa đối xứng (대칭키 / 비밀키)** và **Mã hóa khóa bất đối xứng (비대칭키 / 공개키)** về tốc độ, cơ chế quản lý khóa và công thức tính số lượng khóa ($n(n-1)/2$ vs $2n$).
- Nắm vững các thuật toán mật mã khối kinh điển: **DES**, **3-DES**, **AES**, và hai chuẩn mật mã quốc gia Hàn Quốc: **SEED** (Feistel 128 bit) và **ARIA** (SPN 128 bit).
- Phân tích ưu nhược điểm của các chế độ vận hành mật mã khối: **ECB**, **CBC**, **CFB**, **OFB**, **CTR**.
- Làm chủ nguyên lý toán học nền tảng của mật mã bất đối xứng: Bài toán phân tích thừa số nguyên tố (**RSA**) và Bài toán logarit rời rạc trên đường cong elip (**ECC**).
- Thấu hiểu cơ chế hàm băm một chiều (**단방향 해시 함수: SHA-256, MD5**) và quy trình ký/xác minh **Chữ ký số (전자서명 - Digital Signature)** để bảo đảm tính toàn vẹn và chống chối bỏ.

## 핵심 키워드 (Từ khóa song ngữ)
- 대칭키 암호화 (Symmetric Encryption — Dùng chung 1 khóa, tốc độ nhanh, mã hóa dữ liệu lớn)
- 비대칭키 암호화 (Asymmetric Encryption — Cặp khóa Public/Private, giải bài toán phân phối khóa)
- 키 개수 계산 (Key Count Formula — Đối xứng $\frac{n(n-1)}{2}$ vs Bất đối xứng $2n$)
- 블록 암호 (Block Cipher — DES, AES, SEED, ARIA, IDEA, Skipjack)
- 스트림 암호 (Stream Cipher — RC4, LFSR, mã hóa từng bit/byte liên tục)
- SEED (KISA 개발 블록 암호 — 128비트 블록, 128비트 키, Feistel 구조)
- ARIA (국가보안기술연구소 개발 — 128비트 블록, 128/192/256비트 키, SPN 구조)
- RSA (소인수분해 난해성 — Phân tích thừa số nguyên tố lớn, dùng cho mã hóa và chữ ký số)
- ECC (타원곡선 이산대수 — Khóa ngắn, tốc độ nhanh, tối ưu cho thiết bị di động/IoT)
- 전자서명 (Digital Signature — Ký bằng Private Key người gửi, xác minh bằng Public Key người gửi)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Từ các yêu cầu bảo vệ dữ liệu nhạy cảm theo Đạo luật PIPA tại [05-khung-bao-mat-phan-mem-va-phap-luat.md](05-khung-bao-mat-phan-mem-va-phap-luat.md) và vá các lỗ hổng rò rỉ bộ nhớ tại [06-lo-hong-phan-mem-va-secure-coding.md](06-lo-hong-phan-mem-va-secure-coding.md), mã hóa là công cụ kỹ thuật bắt buộc để bảo vệ tính bí mật và toàn vẹn của thông tin.
- **Đang giải quyết gì (Current Problem):** Bài học này trang bị toàn bộ lý thuyết mật mã: phân loại thuật toán đối xứng/bất đối xứng, các chuẩn mật mã Hàn Quốc và quốc tế, cơ chế băm một chiều và chữ ký số chống chối bỏ.
- **Dùng đi đâu (Forward Handoff):** Các thuật toán mã hóa và chữ ký số này là nền móng để xây dựng hệ thống chứng thực máy chủ, cơ chế đăng nhập một lần (SSO) và phân quyền truy cập tại [08-xac-thuc-va-kiem-soat-truy-cap.md](08-xac-thuc-va-kiem-soat-truy-cap.md).

## 읽는 방법 (Cách đọc & Dấu hiệu nhận diện đề thi)
- **Công thức số lượng khóa (Bài toán tính toán cực kỳ hay gặp):**
  - Mạng có $n$ người dùng dùng **Khóa đối xứng (대칭키)** $\rightarrow$ Công thức: $\frac{n(n-1)}{2}$. Ví dụ: 10 người cần $\frac{10 \times 9}{2} = 45$ khóa.
  - Mạng có $n$ người dùng dùng **Khóa bất đối xứng (비대칭키)** $\rightarrow$ Mỗi người 1 cặp (Public + Private) $\rightarrow$ Tổng số khóa: $2n$. Ví dụ: 10 người cần $20$ khóa.
- **Chuẩn mật mã Hàn Quốc (Đặc thù thi Kỹ sư CNTT Hàn Quốc):**
  - **SEED:** Phát triển năm 1999 bởi KISA, cấu trúc **Feistel**, kích thước khối **128 bit**, độ dài khóa **128 bit**.
  - **ARIA:** Phát triển năm 2004 bởi Viện Nghiên cứu An ninh Quốc gia Hàn Quốc, cấu trúc **SPN**, khối **128 bit**, độ dài khóa **128/192/256 bit**.
- **Cơ sở toán học của Mật mã bất đối xứng:**
  - Nhắc đến **"큰 수의 소인수분해" (Phân tích thừa số nguyên tố lớn)** $\rightarrow$ Chọn ngay **RSA**.
  - Nhắc đến **"타원곡선 군에서의 이산대수 문제" (Logarit rời rạc đường cong elip)** $\rightarrow$ Chọn ngay **ECC** (đặc điểm: khóa ngắn, an toàn cao, hợp di động).
  - Nhắc đến **"이산대수 문제에 기반한 키 교환" (Trao đổi khóa trên kênh không an toàn)** $\rightarrow$ Chọn **Diffie-Hellman**.
- **Chế độ vận hành khối (Block Modes):**
  - Nhắc đến chế độ yếu nhất, bản rõ giống nhau sinh ra bản mã giống nhau $\rightarrow$ **ECB**.
  - Nhắc đến chế độ phổ biến dùng vector khởi tạo IV và phép XOR xâu chuỗi $\rightarrow$ **CBC**.
- **Chữ ký số (Digital Signature):**
  - **Ký (Tạo chữ ký):** Dùng **개인키 (Private Key) của người gửi**.
  - **Xác minh (Kiểm tra chữ ký):** Dùng **공개키 (Public Key) của người gửi**.

---

## 암호 알고리즘 및 암호화 기법

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng đối chiếu hai hệ thống mật mã học kinh điển

| Tiêu chí so sánh | Mật mã khóa đối xứng (대칭키 암호) | Mật mã khóa bất đối xứng (비대칭키 암호) |
| :--- | :--- | :--- |
| **Tên gọi khác** | **비밀키 암호 (Khóa bí mật)**, 단일키 (Khóa đơn). | **공개키 암호 (Khóa công khai)**. |
| **Số lượng khóa** | Dùng **cùng 1 khóa duy nhất** cho cả mã hóa và giải mã. | Dùng **1 cặp khóa**: Khóa công khai (Public Key) và Khóa riêng tư (Private Key). |
| **Tốc độ mã hóa** | **Rất nhanh**; tối ưu cho việc mã hóa các tệp tin hoặc luồng dữ liệu dung lượng lớn (Bulk Data). | **Rất chậm** (chậm hơn từ 100 đến 1,000 lần so với đối xứng); dùng cho lượng dữ liệu nhỏ. |
| **Quản lý & Phân phối khóa** | **Khó khăn**; phải tìm kênh an toàn tuyệt đối để trao đổi khóa bí mật ban đầu giữa 2 bên. | **Dễ dàng**; khóa công khai có thể chia sẻ rộng rãi qua mạng mà không sợ lộ dữ liệu. |
| **Công thức tính số khóa** | $$\text{Số khóa} = \frac{n(n - 1)}{2}$$ | $$\text{Số khóa} = 2n$$ |
| **Thuật toán tiêu biểu** | **DES, 3-DES, AES, SEED, ARIA, RC4**. | **RSA, ECC, Diffie-Hellman, DSA, ElGamal**. |
| **Ứng dụng chính** | Mã hóa dữ liệu lưu trữ CSDL, mã hóa kênh truyền VPN, mã hóa ổ đĩa. | Trao đổi khóa phiên (Key Exchange), Chữ ký số (Digital Signature), Chứng chỉ số PKI. |

#### 2. Các thuật toán mật mã khối đối xứng (Block Ciphers)
Mật mã khối chia dữ liệu thành các khối có kích thước cố định để biến đổi.

| Thuật toán | Kích thước khối (Block) | Độ dài khóa (Key Length) | Kiến trúc cấu trúc | Đặc điểm nhận diện đề thi |
| :--- | :---: | :---: | :---: | :--- |
| **DES** | **64 bit** | **56 bit** (8 bit parity) | Feistel (16 vòng) | Chuẩn cũ của Mỹ (1975); hiện đã bị bẻ khóa hoàn toàn do không gian khóa quá ngắn. |
| **3-DES** | **64 bit** | **112 bit** hoặc **168 bit** | Feistel (Áp dụng DES 3 lần) | Chạy tuần tự: Mã hóa $\rightarrow$ Giải mã $\rightarrow$ Mã hóa (EDE Mode) với 2 hoặc 3 khóa khác nhau. |
| **AES** | **128 bit** | **128 / 192 / 256 bit** | SPN (Substitution-Permutation) | Chuẩn quốc tế hiện đại của Viện NIST Mỹ thay thế DES; bảo mật cao, tốc độ xử lý phần cứng vượt trội. |
| **SEED** | **128 bit** | **128 bit** | Feistel (16 vòng) | Thuật toán chuẩn quốc gia của **Hàn Quốc (KISA 개발)** ban hành năm 1999 nhằm bảo đảm tự chủ an ninh mạng. |
| **ARIA** | **128 bit** | **128 / 192 / 256 bit** | SPN | Thuật toán của **Hàn Quốc (국가보안기술연구소)** phát triển năm 2004, tối ưu hóa cho thẻ thông minh và chip nhúng. |
| **IDEA** | **64 bit** | **128 bit** | Kết hợp phép toán số học | Do Thụy Sĩ phát triển, dùng trong phần mềm mã hóa email PGP phiên bản đầu. |
| **Skipjack** | **64 bit** | **80 bit** | Feistel biến thể | Do Cơ quan An ninh Quốc gia Mỹ (NSA) phát triển cài trong vi mạch Clipper Chip. |

#### 3. Các chế độ vận hành mật mã khối (Block Cipher Modes)
- **1. ECB (Electronic Codebook - Sổ tay điện tử):**
  - Mỗi khối bản rõ được mã hóa độc lập bằng cùng một khóa.
  - **Điểm yếu chí mạng:** Các khối bản rõ giống nhau luôn sinh ra các khối bản mã giống hệt nhau $\rightarrow$ Lộ mẫu cấu trúc dữ liệu. Tuyệt đối không dùng cho dữ liệu lớn.
- **2. CBC (Cipher Block Chaining - Xâu chuỗi khối mã):**
  - Mỗi khối bản rõ trước khi mã hóa được XOR với khối bản mã liền trước; khối đầu tiên được XOR với Vector khởi tạo ngẫu nhiên (**IV - Initialization Vector**).
  - Khắc phục triệt để nhược điểm của ECB; là chế độ chuẩn được sử dụng rộng rãi nhất.
- **3. CFB (Cipher Feedback) & OFB (Output Feedback):** Biến đổi thuật toán mật mã khối thành mật mã dòng để truyền dữ liệu theo luồng bit.
- **4. CTR (Counter - Chế độ bộ đếm):** Mã hóa một giá trị bộ đếm tăng dần rồi XOR với bản rõ; cho phép xử lý song song trên nhiều lõi CPU, tốc độ cực nhanh.

#### 4. Các thuật toán mật mã khóa bất đối xứng (Public Key Ciphers)
- **RSA (Rivest, Shamir, Adleman):**
  - **Cơ sở toán học:** Dựa trên độ khó của việc **phân tích thừa số nguyên tố của tích hai số nguyên tố cực lớn (큰 수의 소인수분해 문제)**.
  - Được sử dụng phổ biến nhất trên thế giới cho cả mục đích mã hóa khóa và tạo chữ ký số.
- **ECC (Elliptic Curve Cryptography - Mật mã đường cong Elip):**
  - **Cơ sở toán học:** Dựa trên độ khó của **bài toán logarit rời rạc trên nhóm đường cong elip (타원곡선 군의 이산대수 문제)**.
  - **Ưu thế vượt trội:** Đạt độ an toàn tương đương RSA nhưng với chiều dài khóa ngắn hơn rất nhiều (khóa ECC 256 bit có độ an toàn tương đương khóa RSA 3072 bit). Chiếm ít bộ nhớ, tiêu hao ít năng lượng, cực kỳ phù hợp cho thiết bị di động, thẻ thông minh và IoT.
- **Diffie-Hellman:** Giao thức cho phép hai bên tự thiết lập một khóa bí mật chung qua kênh truyền thông công cộng không an toàn mà không cần gửi trực tiếp khóa qua mạng.

#### 5. Hàm băm một chiều và Chữ ký số
- **단방향 해시 함수 (One-Way Hash Function):**
  - Chuyển đổi thông điệp có độ dài bất kỳ thành một chuỗi đại diện (Hash Digest) có **chiều dài cố định**.
  - **Thuộc tính then chốt:** Tính một chiều (không thể khôi phục bản rõ từ giá trị băm) và Tính chống đụng độ (Collision Resistance - không thể tìm được hai thông điệp khác nhau có cùng giá trị băm).
  - **Thuật toán:** MD5 (128 bit - đã mất an toàn); họ **SHA-2** (SHA-256, SHA-512 - chuẩn an toàn công nghiệp hiện nay).
- **전자서명 (Digital Signature — Chữ ký số):**
  - **Quy trình ký:** Người gửi tính mã băm của văn bản $\rightarrow$ Dùng **Private Key của người gửi** để mã hóa mã băm này $\rightarrow$ Tạo thành Chữ ký số đính kèm văn bản.
  - **Quy trình xác minh:** Người nhận dùng **Public Key của người gửi** để giải mã chữ ký số $\rightarrow$ So sánh mã băm thu được với mã băm tự tính trên văn bản.
  - **Mục đích:** Bảo đảm tính toàn vẹn (Integrity), xác minh danh tính người ký (Authentication) và chống chối bỏ (Non-Repudiation).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### Cơ chế Mã hóa lai (Hybrid Cryptosystem) trong thực tế
Vì mật mã đối xứng nhanh nhưng khó phân phối khóa, còn mật mã bất đối xứng an toàn nhưng tốc độ rất chậm, các giao thức bảo mật thực tế (như HTTPS/TLS, SSH, PGP) luôn kết hợp cả hai thành **Hệ thống mã hóa lai**:
1. Bên gửi tạo ngẫu nhiên một khóa đối xứng tạm thời gọi là **Khóa phiên (Session Key)**.
2. Dữ liệu lớn được mã hóa nhanh chóng bằng khóa phiên này thông qua thuật toán đối xứng (như AES-256).
3. Khóa phiên nhỏ (256 bit) được mã hóa an toàn bằng **Public Key của bên nhận** thông qua thuật toán bất đối xứng (như RSA hoặc ECC) rồi gửi kèm dữ liệu.
4. Bên nhận dùng **Private Key của mình** để giải mã lấy khóa phiên, sau đó dùng khóa phiên để giải mã toàn bộ khối dữ liệu lớn.

---

### 복습 체크리스트
- [ ] Tính thành thạo số lượng khóa: Đối xứng $=\frac{n(n-1)}{2}$, Bất đối xứng $=2n$.
- [ ] Nhớ thông số các thuật toán khối: DES (khối 64 bit, khóa 56 bit); AES (khối 128 bit, khóa 128/192/256 bit).
- [ ] Phân biệt 2 chuẩn Hàn Quốc: SEED (Feistel, khối 128 bit, khóa 128 bit); ARIA (SPN, khối 128 bit, khóa 128/192/256 bit).
- [ ] Nhớ cơ sở toán học: RSA dựa trên phân tích thừa số nguyên tố (소인수분해); ECC dựa trên logarit rời rạc đường cong elip (타원곡선 이산대수).
- [ ] Nắm vững ưu điểm của ECC: Khóa ngắn hơn nhiều so với RSA ở cùng cấp độ bảo mật, tiết kiệm tài nguyên di động.
- [ ] Phân biệt chế độ khối: ECB là yếu nhất; CBC dùng IV và xâu chuỗi XOR.
- [ ] Khắc ghi quy tắc chữ ký số: Ký bằng Private Key của người gửi, Xác minh bằng Public Key của người gửi.
