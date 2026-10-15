# 암호화 기법 (Encryption Techniques)

## 학습 목표 (Mục tiêu)
- Nắm vững các công thức toán học tính toán số lượng khóa mã hóa trong mạng truyền thông ($n(n-1)/2$ đối xứng vs $2n$ bất đối xứng).
- Phân tích chi tiết thông số kỹ thuật (kích thước khối, chiều dài khóa) của các thuật toán mật mã khối kinh điển (DES, 3DES, AES, SEED, ARIA).
- Hiểu rõ nguyên lý toán học nền tảng của mật mã bất đối xứng (bài toán phân tích thừa số nguyên tố RSA vs logarit rời rạc đường cong elip ECC).
- Nắm bắt các chế độ vận hành mật mã khối (Block Cipher Modes: ECB, CBC) và ứng dụng thực tiễn.

## 핵심 키워드 (Từ khóa)
- **키 개수 계산 (Key Count Calculation)**: Đổi xứng $= \frac{n(n-1)}{2}$, Bất đối xứng $= 2n$.
- **DES vs 3DES vs AES**: DES (64-bit block, 56-bit key), AES (128-bit block, 128/192/256-bit key).
- **국산 암호 알고리즘 (Korean Ciphers)**: SEED (128-bit block/key), ARIA (128-bit block, 128/192/256-bit key).
- **공개키 수학 원리 (Public Key Mathematics)**: RSA (소인수분해 - Phân tích số nguyên tố lớn), ECC (타원곡선 이산로그 - Logarit rời rạc đường cong elip).
- **블록 운영 모드 (Cipher Modes)**: ECB (Electronic Codebook - lộ quy luật mẫu ảnh), CBC (Cipher Block Chaining - sử dụng IV).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (암호화 기술 - Khái niệm tổng quan về mã hóa và băm dữ liệu).
- Liên kết với [36-bai-hoc.md](36-bai-hoc.md) (접근 통제 모델 - Quản lý quyền truy cập và chứng thực).
- Liên kết với [22-bai-hoc.md](22-bai-hoc.md) (네트워크 보안 기술 - VPN IPSec và các chế độ bảo mật đường truyền).

## 읽는 방법 (Cách đọc)
- Đi thi giải nhanh bài toán tính số khóa:
  - Cho mạng có $10$ người dùng ($n = 10$):
    - Mã hóa khóa đối xứng: $\frac{10 \times (10 - 1)}{2} = \frac{90}{2} = 45$ khóa.
    - Mã hóa khóa công khai: $2 \times 10 = 20$ khóa.
  - Phân biệt toán học nền tảng: Cứ thấy từ khóa "소인수분해" (thừa số nguyên tố) $\rightarrow$ chọn **RSA**; thấy "타원곡선" (đường cong elip) $\rightarrow$ chọn **ECC**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Công thức và bài toán tính số lượng khóa
| Hệ mật mã | Công thức tính số khóa ($n$ đối tượng) | Ví dụ với $n = 5$ người | Ví dụ với $n = 100$ người |
| :--- | :--- | :--- | :--- |
| **Mật mã đối xứng (대칭키 / 개인키)** | $\frac{n(n-1)}{2}$ | $\frac{5 \times 4}{2} = 10$ khóa | $\frac{100 \times 99}{2} = 4,950$ khóa |
| **Mật mã bất đối xứng (비대칭키 / 공개키)** | $2n$ | $2 \times 5 = 10$ khóa | $2 \times 100 = 200$ khóa |

*Nhận xét cốt lõi*: Khi số lượng người dùng trong mạng tăng lên quy mô lớn, số lượng khóa đối xứng tăng theo hàm bậc hai ($O(n^2)$), gây ra vấn đề bùng nổ khóa (Key Explosion). Mật mã bất đối xứng giải quyết triệt để vấn đề này vì số lượng khóa tăng tuyến tính ($O(n)$).

#### 2. So sánh thông số kỹ thuật các thuật toán mật mã khối
| Thuật toán | Xuất xứ | Kích thước khối (Block) | Chiều dài khóa (Key length) | Cấu trúc giải thuật | Ghi chú thi cử |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DES** | IBM / NIST (Mỹ) | 64 bits | 56 bits (8 bits parity) | Mạng Feistel (16 vòng) | Đã bị bẻ gãy, không an toàn |
| **3DES** | NIST (Mỹ) | 64 bits | 112 hoặc 168 bits | Chạy DES 3 lần (Encrypt-Decrypt-Encrypt) | Giải pháp chuyển tiếp tạm thời |
| **AES** | Rijndael / NIST | **128 bits** | **128, 192, 256 bits** | Mạng SPN (Substitution-Permutation) | **Tiêu chuẩn mã hóa hiện hành** |
| **SEED** | KISA (Hàn Quốc) | **128 bits** | **128 bits** | Mạng Feistel (16 vòng) | Chuẩn quốc gia Hàn Quốc (1999) |
| **ARIA** | NSRI (Hàn Quốc) | **128 bits** | **128, 192, 256 bits** | Mạng SPN | Nhẹ, tối ưu cho chip nhúng (2004) |

#### 3. Các chế độ vận hành mật mã khối (Block Cipher Modes of Operation)
- **ECB (Electronic Codebook)**:
  - Mỗi khối bản rõ 128-bit được mã hóa độc lập bằng cùng một khóa bí mật.
  - **Nhược điểm chí mạng**: Các khối bản rõ giống hệt nhau sẽ tạo ra các khối bản mã giống hệt nhau, làm lộ cấu trúc và hoa văn của dữ liệu gốc (ví dụ: hình ảnh bitmap vẫn nhìn rõ đường nét sau khi mã hóa). **Không khuyến nghị sử dụng**.
- **CBC (Cipher Block Chaining)**:
  - Khối bản rõ hiện tại được thực hiện phép XOR với khối bản mã trước đó trước khi đưa vào hàm mã hóa.
  - Khối đầu tiên sử dụng một vectơ khởi tạo ngẫu nhiên **IV (Initialization Vector)**.
  - Ngăn chặn hoàn toàn việc phát hiện mẫu lặp lại của bản rõ, đảm bảo tính ngẫu nhiên cao của bản mã.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ cơ chế hoạt động của chế độ mã hóa CBC
```
   [Bản rõ 1]               [Bản rõ 2]               [Bản rõ 3]
       │                        │                        │
       ▼                        ▼                        ▼
[IV] ─►⊕                       ┌─►⊕                     ┌─►⊕
       │                       │  │                     │  │
       ▼                       │  ▼                     │  ▼
 [Mã hóa AES]                  │ [Mã hóa AES]           │ [Mã hóa AES]
       │                       │  │                     │  │
       ├───────────────────────┘  ├─────────────────────┘  │
       ▼                          ▼                        ▼
  [Bản mã 1]                 [Bản mã 2]               [Bản mã 3]
```

#### 2. Cơ sở toán học của Mật mã Bất đối xứng
- **Thuật toán RSA (Rivest, Shamir, Adleman)**:
  - Dựa trên độ khó tính toán của **bài toán phân tích một số nguyên cực lớn thành tích các thừa số nguyên tố (소인수분해의 난해성)**: Cho $n = p \times q$ (với $p, q$ là các số nguyên tố rất lớn hàng nghìn bit), việc tính $n$ từ $p$ và $q$ thì cực nhanh, nhưng tìm ngược lại $p$ và $q$ từ $n$ thì cần hàng triệu năm tính toán trên siêu máy tính.
- **Thuật toán ECC (Elliptic Curve Cryptography)**:
  - Dựa trên độ khó của **bài toán logarit rời rạc trên đường cong elip (타원곡선 이산대수 문제)**.
  - **Ưu thế vượt trội**: Cung cấp mức độ an ninh tương đương RSA với kích thước khóa ngắn hơn rất nhiều (ví dụ: ECC 256-bit có độ an toàn tương đương RSA 3072-bit), giúp tiết kiệm băng thông và tối ưu hiệu năng cho thiết bị di động, IoT và thẻ thông minh.

---

### 복습 체크리스트
- [ ] Tính số khóa bí mật cần dùng trong một tổ chức có 20 nhân sự nếu sử dụng hệ mật mã đối xứng?
- [ ] Kích thước khối dữ liệu (Block size) của chuẩn mã hóa AES, SEED và ARIA là bao nhiêu bits?
- [ ] Tại sao chế độ vận hành ECB lại bị cấm sử dụng trong các hệ thống truyền dẫn dữ liệu bảo mật?
- [ ] Nền tảng toán học của thuật toán mã hóa RSA khác gì so với thuật toán ECC?
