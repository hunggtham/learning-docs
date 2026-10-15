# 9. 암호화 기술 (Công nghệ Mã hóa)

## 학습 목표 (Mục tiêu)
- Phân biệt toàn diện hai hệ mật mã cốt lõi: Mã hóa khóa đối xứng (대칭키 / 개인키) và Mã hóa khóa bất đối xứng (비대칭키 / 공개키).
- Nắm vững phân loại mật mã khối (Block Cipher: DES, AES, SEED, ARIA) và mật mã dòng (Stream Cipher: RC4, LFSR).
- Hiểu rõ nguyên lý hoạt động của hàm băm một chiều (Hash Functions: SHA-256, MD5) và cơ chế chữ ký số (Digital Signature).

## 핵심 키워드 (Từ khóa)
- **대칭키 (Symmetric Key)**: Dùng chung 1 khóa, tốc độ nhanh, số lượng khóa $n(n-1)/2$.
- **비대칭키 (Asymmetric / Public Key)**: Cặp khóa Public/Private Key, an toàn phân phối khóa, số lượng khóa $2n$, thuật toán RSA, ECC.
- **블록 암호 (Block Cipher)**: DES (64 bit block, 56 bit key), AES (128 bit block), SEED, ARIA.
- **스트림 암호 (Stream Cipher)**: RC4, LFSR.
- **해시 함수 (Hash)**: MD5 (128 bit), SHA-1 (160 bit), SHA-256, tính chất một chiều và kháng va chạm.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [35-bai-hoc.md](35-bai-hoc.md) (암호화 기법 - Công thức tính số khóa và so sánh chi tiết DES vs AES).
- Liên kết với [29-bai-hoc.md](29-bai-hoc.md) (소프트웨어 보안 - Chống chối bỏ và tính toàn vẹn).
- Liên kết với [22-bai-hoc.md](22-bai-hoc.md) (네트워크 보안 기술 - Giao thức VPN IPSec và SSL/TLS).

## 읽는 방법 (Cách đọc)
- Phân biệt mục đích sử dụng cặp khóa trong mật mã bất đối xứng (Public Key Cryptography):
  - **Mục đích Bảo mật (Bảo mật nội dung)**: Mã hóa bằng **Public Key của người nhận**, Giải mã bằng **Private Key của người nhận**.
  - **Mục đích Chữ ký số (Xác thực / Chống chối bỏ)**: Ký bằng **Private Key của người gửi**, Kiểm tra chữ ký bằng **Public Key của người gửi**.
- Ghi nhớ các thuật toán chuẩn của Hàn Quốc: **SEED**, **ARIA** (luôn là mật mã khối đối xứng 128-bit).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh Mật mã Đối xứng và Mật mã Bất đối xứng
| Tiêu chí | Mã hóa khóa đối xứng (대칭키 / 개인키) | Mã hóa khóa bất đối xứng (비대칭키 / 공개키) |
| :--- | :--- | :--- |
| **Bản chất khóa** | Cùng **1 khóa bí mật duy nhất** dùng cho cả mã hóa và giải mã | Gồm **cặp 2 khóa khác nhau**: Khóa công khai (Public) và Khóa bí mật (Private) |
| **Tốc độ xử lý** | **Rất nhanh**, tối ưu cho dữ liệu dung lượng lớn | **Chậm** (phức tạp về mặt toán học và chi phí CPU) |
| **Số lượng khóa ($n$ người)** | $\frac{n(n-1)}{2}$ khóa bí mật | $2n$ khóa (mỗi người giữ 1 Public và 1 Private) |
| **Vấn đề phân phối khóa** | Khó khăn (phải tìm kênh an toàn để trao đổi khóa bí mật) | Dễ dàng (khóa Public Key có thể công bố rộng rãi) |
| **Phân loại & Thuật toán** | - **Khối (Block)**: DES, 3DES, AES, SEED, ARIA, IDEA / - **Dòng (Stream)**: RC4, LFSR | RSA (dựa trên phân tích thừa số nguyên tố), ECC (đường cong elip), Diffie-Hellman, ElGamal |

#### 2. Phân loại Mật mã Khối và Mật mã Dòng
- **Mật mã khối (Block Cipher)**: Chia bản rõ thành các khối bit có kích thước cố định và thực hiện các phép thay thế (Substitution), hoán vị (Permutation) phức tạp:
  - **DES (Data Encryption Standard)**: Chuẩn cũ của Mỹ, kích thước khối 64 bits, độ dài khóa thực tế 56 bits (8 bits chẵn lẻ), cấu trúc mạng Feistel 16 vòng. Hiện đã lỗi thời.
  - **AES (Advanced Encryption Standard)**: Chuẩn hiện hành thay thế DES (thuật toán Rijndael), kích thước khối cố định **128 bits**, hỗ trợ độ dài khóa linh hoạt **128, 192, 256 bits** với số vòng tương ứng là 10, 12, 14 vòng.
  - **SEED**: Chuẩn mật mã khối quốc gia của Hàn Quốc do KISA phát triển năm 1999, kích thước khối 128 bits, khóa 128 bits.
  - **ARIA**: Chuẩn mật mã khối quốc gia của Hàn Quốc do NSRI phát triển năm 2004, tối ưu hóa cho môi trường phần cứng nhẹ, kích thước khối 128 bits, hỗ trợ khóa 128/192/256 bits.
- **Mật mã dòng (Stream Cipher)**: Tạo ra một dòng khóa ngẫu nhiên giả (Keystream) và thực hiện phép XOR từng bit hoặc byte liên tục với dòng dữ liệu bản rõ:
  - Phù hợp với luồng dữ liệu truyền âm thanh, video thời gian thực. Thuật toán tiêu biểu: **RC4**, **LFSR** (Linear Feedback Shift Register).

#### 3. Hàm băm mật mã (Hash Function) và Chữ ký số
- **Đặc trưng hàm băm một chiều**:
  - Biến đổi thông điệp có chiều dài tùy ý thành một giá trị băm (Hash Value / Digest) có **độ dài cố định**.
  - **Tính chất một chiều (One-wayness)**: Không thể tính ngược từ giá trị băm để tìm lại bản rõ gốc ban đầu.
  - **Kháng va chạm (Collision Resistance)**: Cực kỳ khó để tìm thấy hai thông điệp khác nhau ($M_1 \neq M_2$) mà lại cho ra cùng một giá trị băm ($H(M_1) = H(M_2)$).
- **Thuật toán hàm băm phổ biến**:
  - **MD5**: Sinh chuỗi băm 128 bits, hiện đã bị phá vỡ kháng va chạm, không an toàn.
  - **SHA-1**: Sinh chuỗi băm 160 bits, đã bị khuyến nghị ngưng sử dụng.
  - **SHA-2 (SHA-256 / SHA-512)**: Tiêu chuẩn an toàn hiện hành, sinh chuỗi băm 256 hoặc 512 bits.
- **Cơ chế Chữ ký số (Digital Signature)**:
  - Người gửi: Tạo bản băm của tài liệu $\rightarrow$ Mã hóa bản băm bằng **Private Key của người gửi** $\rightarrow$ Tạo thành Chữ ký số đính kèm tài liệu.
  - Người nhận: Dùng **Public Key của người gửi** để giải mã chữ ký số nhằm lấy bản băm gốc $\rightarrow$ So sánh với bản băm tự tính toán từ tài liệu nhận được.
  - Nếu khớp: Xác nhận đúng tác giả gửi và dữ liệu không bị sửa đổi trên đường truyền.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ quy trình tạo và xác minh Chữ ký số
```
[Bên gửi]
  Văn bản gốc ──(Hàm băm SHA-256)──► Giá trị băm (Digest)
                                            │
                                            ▼ (Mã hóa bằng Private Key của bên gửi)
                                      [CHỮ KÝ SỐ]
                                            │
  (Gửi qua mạng: Văn bản gốc + Chữ ký số) ────┼────────────────────────┐
                                                                       ▼
[Bên nhận]                                                     [Bên nhận nhận được]
  Văn bản gốc nhận được ──(Hàm băm SHA-256)──► Giá trị băm A            │
                                                                       ▼
  Chữ ký số nhận được ──(Giải mã bằng Public Key người gửi)──► Giá trị băm B
                                                                       │
                                              So sánh A == B ? ────────┘
                                                    │
                                     ┌──────────────┴──────────────┐
                                     ▼                             ▼
                            [Khớp: Hợp lệ]               [Lệch: Giả mạo / Bị sửa]
```

#### 2. Kỹ thuật mã hóa lai (Hybrid Cryptography)
- Trong thực tế (như HTTPS / SSL / TLS), người ta không dùng đơn lẻ một hệ mật mã:
  - Dùng **Mật mã bất đối xứng (RSA/ECC)** trong giai đoạn bắt tay để xác thực danh tính máy chủ và trao đổi an toàn một **Khóa phiên (Session Key)** ngẫu nhiên.
  - Dùng **Mật mã đối xứng (AES-256-GCM)** kết hợp cùng Khóa phiên đó để mã hóa toàn bộ dữ liệu truyền tải thực tế nhằm đạt tốc độ tối đa.

---

### 복습 체크리스트
- [ ] Công thức tính số lượng khóa bí mật cần thiết cho mạng gồm $n$ người dùng trong hệ mật đối xứng là gì?
- [ ] Sự khác biệt then chốt giữa thuật toán mã hóa khối (Block) và mã hóa dòng (Stream) là gì?
- [ ] Tại sao khi tạo Chữ ký số, người ta lại sử dụng Private Key của người gửi thay vì Public Key?
- [ ] Kể tên hai thuật toán mã hóa khối chuẩn của Hàn Quốc thường xuyên xuất hiện trong đề thi?
