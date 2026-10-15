# 106 암호 알고리즘 (Cryptography Algorithms / Thuật toán Mã hóa)

## 학습 목표 (Mục tiêu)
- Nắm vững các khái niệm nền tảng của mật mã học: Bản rõ (평문 - Plaintext), Bản mã (암호문 - Ciphertext), Khóa (Key), Quá trình mã hóa và giải mã.
- Phân biệt nguyên lý hoạt động của hai kỹ thuật biến đổi cổ điển: Mật mã thay thế (치환 암호 - Substitution) và Mật mã hoán vị (전치 암호 - Transposition).
- Hiểu rõ hai nguyên lý an toàn mật mã của Claude Shannon: Tính hỗn loạn (혼돈 - Confusion) và Tính khuếch tán (확산 - Diffusion).
- Phân tích cấu trúc thiết kế của Mạng Feistel (Feistel Network) và Mạng SPN (Substitution-Permutation Network).

## 핵심 키워드 (Từ khóa)
- **평문 (Plaintext) & 암호문 (Ciphertext)**: Thông tin gốc ban đầu vs Dữ liệu đã mã hóa bảo vệ.
- **치환 암호 (Substitution Cipher)**: Đổi ký tự này lấy ký tự khác (Caesar, Vigenère).
- **전치 암호 (Transposition Cipher)**: Giữ nguyên ký tự, thay đổi vị trí sắp xếp.
- **혼돈 (Confusion)**: Làm phức tạp hóa mối quan hệ giữa Bản mã và Khóa (S-Box).
- **확산 (Diffusion)**: 1 bit thay đổi làm lan tỏa thay đổi ít nhất 50% bản mã (P-Box / Avalanche Effect).
- **Feistel vs SPN**: Feistel (DES, SEED - mạch giải mã đảo ngược thứ tự khóa) vs SPN (AES, ARIA - xử lý song song).

## 선행·연결 개념 (Kiến thức liên결)
- Liên kết với [36-bai-hoc.md](36-bai-hoc.md) (Khái niệm cơ bản về mật mã học).
- Liên kết với [82-bai-hoc.md](82-bai-hoc.md) (Mật mã đối xứng vs bất đối xứng và các hình thức tấn công dịch vụ).
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (Công nghệ mã hóa và hàm băm).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh định nghĩa thi trắc nghiệm:
  - "Thay thế chữ cái bằng chữ cái khác theo quy tắc" $\rightarrow$ **치환 암호 (Substitution)**.
  - "Đảo lộn vị trí các chữ cái trong văn bản" $\rightarrow$ **전치 암호 (Transposition)**.
  - "Nguyên lý làm cho kẻ tấn công không thể suy đoán được khóa bí mật từ bản mã" $\rightarrow$ **혼돈 (Confusion)**.
  - "Nguyên lý làm cho một sự thay đổi nhỏ ở bản rõ lan truyền ra khắp bản mã" $\rightarrow$ **확산 (Diffusion)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các khái niệm Cơ sở trong Mật mã học
- **Bản rõ (평문 - Plaintext)**: Thông điệp nguyên bản dễ hiểu có thể đọc trực tiếp.
- **Bản mã (암호문 - Ciphertext)**: Dữ liệu đã trải qua biến đổi toán học không thể đọc hiểu nếu không có khóa giải mã.
- **Mã hóa (Encryption)**: Quá trình biến đổi từ Bản rõ sang Bản mã nhờ thuật toán và Khóa mã hóa.
- **Giải mã (Decryption)**: Quá trình khôi phục lại Bản rõ gốc từ Bản mã nhờ Khóa giải mã.

#### 2. Kỹ thuật Mật mã cổ điển: Substitution vs Transposition
| Kỹ thuật | Bản chất toán học | Đặc trưng phân tích mật mã | Ví dụ kinh điển |
| :--- | :--- | :--- | :--- |
| **치환 암호 (Substitution)** | Thay thế một ký tự hoặc nhóm ký tự bằng một ký tự hoặc nhóm ký tự khác | Tần suất xuất hiện của các chữ cái bị biến đổi, nhưng có thể bị bẻ gãy bằng phân tích tần suất chữ cái (Frequency Analysis) | Mật mã Caesar (dịch 3 ký tự), Mật mã Vigenère (đa bảng) |
| **전치 암호 (Transposition)** | Giữ nguyên tập hợp các chữ cái ban đầu, chỉ **thay đổi trật tự/vị trí** của chúng | Tần suất xuất hiện của từng chữ cái trong bản mã giống hệt bản rõ ban đầu | Mật mã hoán vị cột (Columnar Transposition), Mật mã hàng rào |

#### 3. Hai Nguyên lý An toàn của Claude Shannon
- **혼돈 (Confusion - Tính hỗn loạn)**:
  - Mục tiêu: Che giấu tối đa mối quan hệ thống kê giữa **Khóa bí mật** và **Bản mã**.
  - Triển khai: Sử dụng các bảng thay thế phi tuyến tính **S-Box (Substitution Box)**. Khi kẻ thù có hàng triệu cặp bản rõ - bản mã, họ vẫn không thể tìm ra quy luật của khóa.
- **확산 (Diffusion - Tính khuếch tán)**:
  - Mục tiêu: Lan tỏa ảnh hưởng của từng bit trong bản rõ và khóa ra khắp toàn bộ bản mã.
  - Hiệu ứng tuyết lở (Avalanche Effect): Khi chỉ cần thay đổi **1 bit duy nhất** của bản rõ hoặc khóa, có ít nhất $50\%$ các bit trong bản mã sẽ bị đảo ngược ngẫu nhiên.
  - Triển khai: Sử dụng các tầng hoán vị vị trí **P-Box (Permutation Box)** kết hợp phép XOR.

#### 4. Hai Cấu trúc Mật mã khối Hiện đại: Feistel vs SPN
- **Cấu trúc Feistel**:
  - Khối bản rõ được chia thành 2 nửa: Trái ($L$) và Phải ($R$).
  - Trong mỗi vòng, nửa phải $R$ qua hàm vòng $F(R, K)$ rồi XOR với nửa trái $L$, sau đó đổi chỗ hai nửa:
    $$L_{i} = R_{i-1}, \quad R_{i} = L_{i-1} \oplus F(R_{i-1}, K_i)$$
  - *Đặc điểm*: Mã hóa và giải mã dùng chung một cấu trúc mạch (chỉ đảo ngược thứ tự khóa con $K_{16} \rightarrow K_1$).
  - *Thuật toán*: **DES**, **3DES**, **SEED**, Blowfish.
- **Cấu trúc SPN (Substitution-Permutation Network)**:
  - Khối dữ liệu được xử lý song song toàn phần qua các tầng thay thế S-Box và hoán vị P-Box luân phiên.
  - *Đặc điểm*: Tốc độ mã hóa nhanh, tối ưu trên kiến trúc vi xử lý hiện đại; mạch giải mã cần thiết kế nghịch đảo riêng.
  - *Thuật toán*: **AES**, **ARIA**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế Avalanche Effect (Khuếch tán)
```
Bản rõ 1: "Hello World 1" ──(AES-128)──► Bản mã: 7A 9F 3B 21 C8 ...
Bản rõ 2: "Hello World 2" ──(AES-128)──► Bản mã: 4E 12 D9 FA 80 ...
(Chỉ đổi đúng 1 bit ở ký tự cuối!)        (Toàn bộ 128 bit bản mã thay đổi hoàn toàn!)
```

---

### 복습 체크리스트
- [ ] Sự khác biệt then chốt giữa 치환 암호 (Substitution) và 전치 암호 (Transposition) là gì?
- [ ] Hai nguyên lý cốt lõi Confusion và Diffusion của Claude Shannon có vai trò bảo vệ an toàn như thế nào?
- [ ] Tại sao trong cấu trúc Feistel Network, việc giải mã không đòi hỏi hàm $F$ phải có hàm nghịch đảo?
- [ ] Liệt kê các thuật toán mật mã khối tiêu biểu thuộc cấu trúc Feistel và cấu trúc SPN?
