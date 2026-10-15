# 1. 암호화 기본 개념 (Khái niệm Cơ bản về Mã hóa)

## 학습 목표 (Mục tiêu)
- Nắm vững các khái niệm cơ bản của hệ thống mật mã: Bản rõ (평문 - Plaintext), Bản mã (암호문 - Ciphertext), Quá trình mã hóa và giải mã.
- Phân biệt nguyên lý hoạt động của hai kỹ thuật mật mã cổ điển: Mật mã thay thế (치환 암호 - Substitution Cipher) và Mật mã hoán vị (전치 암호 - Transposition Cipher).
- Hiểu rõ hai cấu trúc thiết kế mật mã khối hiện đại: Mạng Feistel (Feistel Network) và Mạng SPN (Substitution-Permutation Network).

## 핵심 키워드 (Từ khóa)
- **기본 용어 (Terminology)**: 평문 (Plaintext), 암호문 (Ciphertext), 암호화 (Encryption), 복호화 (Decryption), 키 (Key).
- **고전 암호 (Classical Ciphers)**: 치환 암호 (Substitution - thay đổi ký tự), 전치 암호 (Transposition - thay đổi vị trí).
- **현대 블록 구조 (Modern Structures)**: Feistel 구조 (DES, SEED - chia nửa L/R, dùng chung mạch giải mã), SPN 구조 (AES, ARIA - S-Box và P-Box song song).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (암호화 기술 - Phân loại mật mã đối xứng và bất đối xứng).
- Liên kết với [35-bai-hoc.md](35-bai-hoc.md) (암호화 기법 - Chi tiết các thuật toán DES, AES, SEED, ARIA).
- Liên kết với [26-bai-hoc.md](26-bai-hoc.md) (정보 보안 일반 - Thuộc tính 기밀성).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý phân biệt:
  - Thay thế chữ này bằng chữ khác ($A \rightarrow D$) $\rightarrow$ **치환 (Substitution)**.
  - Giữ nguyên chữ nhưng đảo lộn vị trí ($ABC \rightarrow CAB$) $\rightarrow$ **전치 (Transposition)**.
  - Phân loại cấu trúc: DES/SEED thuộc mạng **Feistel**; AES/ARIA thuộc mạng **SPN**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các thuật ngữ nền tảng trong Mật mã học
- **평문 (Plaintext - $P$)**: Thông tin ban đầu ở dạng văn bản thông thường chưa được bảo vệ mà bất kỳ ai cũng có thể đọc và hiểu được.
- **암호문 (Ciphertext - $C$)**: Dữ liệu đã được biến đổi qua thuật toán mã hóa, trở nên vô nghĩa đối với người không có khóa giải mã.
- **암호화 (Encryption - $E$)**: Quá trình biến đổi bản rõ thành bản mã: $C = E_K(P)$.
- **복호화 (Decryption - $D$)**: Quá trình khôi phục bản rõ gốc từ bản mã nhờ khóa bí mật: $P = D_K(C)$.
- **Khóa (Key - $K$)**: Tham số bí mật quyết định kết quả của phép mã hóa và giải mã.

#### 2. Kỹ thuật Mật mã cổ điển: Chi환 vs 전치
| Tiêu chí | 치환 암호 (Substitution Cipher) | 전치 암호 (Transposition Cipher) |
| :--- | :--- | :--- |
| **Nguyên lý** | Thay thế từng ký tự trong bản rõ bằng một ký tự, chữ số hoặc ký hiệu khác | Giữ nguyên các ký tự gốc nhưng **thay đổi vị trí/thứ tự** sắp xếp của chúng |
| **Bản chất** | Tần suất xuất hiện của từng ký tự bị xáo trộn và biến đổi | Tần suất xuất hiện của các chữ cái trong bản mã hoàn toàn giống hệt bản rõ |
| **Ví dụ kinh điển** | - Mật mã Caesar (dịch chuyển 3 ký tự: $A \rightarrow D$) / - Mật mã Vigenère (đa bảng thay thế) | - Mật mã hàng rào (Rail Fence Cipher) / - Mật mã hoán vị cột (Columnar Transposition) |

#### 3. Hai cấu trúc Mật mã khối hiện đại: Feistel vs SPN
- **Cấu trúc mạng Feistel (Feistel Network)**:
  - Khối dữ liệu đầu vào được chia thành 2 nửa bằng nhau: Nửa trái ($L$) và Nửa phải ($R$).
  - Tại mỗi vòng (Round), nửa phải $R$ được đưa qua hàm vòng $F$ với khóa con $K_i$, sau đó lấy kết quả XOR với nửa trái $L$, rồi hoán đổi hai nửa cho nhau.
  - **Ưu điểm lớn nhất**: Cấu trúc mã hóa và giải mã **hoàn toàn giống hệt nhau**, giải mã chỉ cần đưa các khóa con vào theo thứ tự đảo ngược ($K_n \rightarrow K_1$). Hàm $F$ không cần có hàm nghịch đảo.
  - **Thuật toán tiêu biểu**: **DES**, **3DES**, **SEED**, Blowfish.
- **Cấu trúc mạng SPN (Substitution-Permutation Network)**:
  - Khối dữ liệu được xử lý song song toàn bộ thông qua các tầng thay thế phi tuyến **S-Box (Substitution Box)** để tạo tính hỗn loạn (Confusion) xen kẽ các tầng hoán vị **P-Box (Permutation Box)** để tạo tính khuếch tán (Diffusion).
  - **Ưu điểm**: Xử lý song song hiệu năng cao, tốc độ nhanh hơn Feistel trên phần cứng 64-bit và 128-bit.
  - **Nhược điểm**: Mạch giải mã phải thiết kế các khối nghịch đảo riêng biệt (Inverse S-Box, Inverse P-Box).
  - **Thuật toán tiêu biểu**: **AES**, **ARIA**.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. So sánh sơ đồ kiến trúc Feistel và SPN
```
           [Feistel Network]                              [SPN Network]
        Khối bản rõ (Chia đôi)                       Khối bản rõ toàn phần
           ┌────────┬────────┐                                  │
           │ L(i-1) │ R(i-1) │                                  ▼
           └───┬────┴───┬────┘                         ┌────────────────┐
               │        │                              │  Cộng khóa con │
               │   ┌────┴────┐                         └───────┬────────┘
               │   │ Hàm F(K)│                                 ▼
               │   └────┬────┘                         ┌────────────────┐
               ▼        │                              │ Tầng S-Box (치환)│
              [⊕]◄──────┘                              └───────┬────────┘
               │                                               ▼
         ┌─────┴────────┐                              ┌────────────────┐
         ▼              ▼                              │ Tầng P-Box (전치)│
       R(i)            L(i)                            └───────┬────────┘
     (Đổi chỗ cho vòng kế tiếp)                                ▼
```

#### 2. Hai nguyên lý an toàn của Claude Shannon
- **Confusion (Hỗn loạn / 혼돈)**: Làm cho mối quan hệ giữa bản mã và khóa bí mật trở nên phức tạp nhất có thể, khiến kẻ thù không thể suy luận ra khóa dù có nhiều bản mã. (Được thực hiện chủ yếu bằng tầng S-Box).
- **Diffusion (Khuếch tán / 확산)**: Làm cho ảnh hưởng của một bit bản rõ hoặc một bit khóa lan tỏa ra toàn bộ các bit của bản mã. Khi thay đổi 1 bit bản rõ, ít nhất 50% các bit trong bản mã sẽ thay đổi (Hiệu ứng Tuyết lở - Avalanche Effect). (Được thực hiện chủ yếu bằng tầng P-Box).

---

### 복습 체크리스트
- [ ] Phân biệt được cơ chế biến đổi giữa 치환 암호 (Substitution) và 전치 암호 (Transposition)?
- [ ] Tại sao mạng Feistel lại có thể dùng chung một mạch phần cứng cho cả mã hóa và giải mã?
- [ ] Mật mã AES và ARIA được xây dựng dựa trên cấu trúc mạng nào (Feistel hay SPN)?
- [ ] Hai nguyên lý cốt lõi Confusion và Diffusion trong mật mã học có mục tiêu bảo vệ là gì?
