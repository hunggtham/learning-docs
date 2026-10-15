# 3. 취약한 API 사용 (Vulnerable API / API Dễ bị Tổn thương)

## 학습 목표 (Mục tiêu)
- Nắm vững danh sách các hàm và API có lỗ hổng bảo mật cố hữu (C/C++, Java) thường xuyên xuất hiện trong đề thi Kỹ sư xử lý thông tin.
- Hiểu rõ cơ chế thay thế an toàn: Thay `strcpy()` bằng `strncpy()`, `gets()` bằng `fgets()`, `sprintf()` bằng `snprintf()`.
- Phân tích cạm bẫy ký tự Null (`\0`) khi sử dụng hàm `strncpy()` và cách khắc phục triệt để.
- Phân biệt bộ sinh số ngẫu nhiên giả yếu (`rand()`) và bộ sinh số ngẫu nhiên an toàn trong mật mã học (CSPRNG: `SecureRandom`, `/dev/urandom`).

## 핵심 키워드 (Từ khóa)
- **취약한 API (Vulnerable API)**: Các hàm không kiểm tra giới hạn bộ đệm (`gets`, `strcpy`, `strcat`, `sprintf`).
- **안전한 대체 함수 (Safe Replacements)**: `fgets()`, `strncpy()`, `snprintf()`, `strlcpy()`.
- **널 종료 함정 (Null-Termination Trap)**: `strncpy()` không tự động thêm `\0` nếu chuỗi nguồn vượt quá giới hạn $N$.
- **CSPRNG (Cryptographically Secure PRNG)**: Thay thế `rand()` bằng `SecureRandom` để chống đoán trước khóa/token.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [76-bai-hoc.md](76-bai-hoc.md) (Lỗ hổng tràn bộ đệm bộ nhớ).
- Liên kết với [42-bai-hoc.md](42-bai-hoc.md) (Mảng chuỗi ký tự và ký tự Null trong C).
- Liên kết với [34-bai-hoc.md](34-bai-hoc.md) (Các thuật toán mật mã và hàm băm an toàn).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - Hàm bị cấm hoàn toàn trong chuẩn C11 do không có cách nào giới hạn kích thước $\rightarrow$ **`gets()`**.
  - Hàm thay thế cho `strcpy()` có giới hạn độ dài $\rightarrow$ **`strncpy()`**.
  - Hàm sinh số ngẫu nhiên an toàn trong Java dùng cho mã OTP/Token $\rightarrow$ **`SecureRandom`** (không dùng `Math.random()` hay `Random`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng đối chiếu các API Nguy hiểm và Hàm Thay thế An toàn
| Hàm nguy hiểm (Cấm dùng) | Bản chất nguy cơ an ninh | Hàm thay thế an toàn | Cú pháp và Nguyên lý an toàn |
| :--- | :--- | :--- | :--- |
| **`gets(buf)`** | Không có tham số giới hạn kích thước bộ đệm; người dùng nhập bao nhiêu cũng đọc hết $\rightarrow$ **Gây Buffer Overflow 100%** | **`fgets(buf, size, stdin)`** | Chỉ đọc tối đa `size - 1` ký tự và tự động chèn `\0` ở cuối |
| **`strcpy(dest, src)`** | Sao chép toàn bộ chuỗi `src` sang `dest` mà không kiểm tra độ dài `dest` có chứa vừa không | **`strncpy(dest, src, n)`** / `strcpy_s()` | Giới hạn chỉ sao chép tối đa `n` ký tự từ nguồn sang đích |
| **`strcat(dest, src)`** | Nối chuỗi `src` vào cuối `dest` mà không kiểm tra vùng nhớ còn lại của `dest` | **`strncat(dest, src, n)`** / `strcat_s()` | Giới hạn số ký tự nối thêm tối đa là `n` |
| **`sprintf(buf, ...)`** | Định dạng và ghi chuỗi vào `buf` không giới hạn độ dài | **`snprintf(buf, size, ...)`** | Giới hạn số ký tự ghi vào bộ đệm không vượt quá `size` |
| **`rand()` (C) / `Random` (Java)** | Sử dụng thuật toán đồng dư tuyến tính (LCG), chuỗi số sinh ra có tính tuần hoàn và dễ bị đảo ngược toán học | **`SecureRandom`** (Java) / `/dev/urandom` (Linux) | Sử dụng nguồn entropy phần cứng ngẫu nhiên thực sự, an toàn cho mật mã |

#### 2. Cạm bẫy Ký tự Null (`\0`) trong hàm `strncpy()`
- Rất nhiều lập trình viên nghĩ rằng chỉ cần đổi sang `strncpy()` là đã tuyệt đối an toàn. Đây là một sai lầm nghiêm trọng trong đề thi:
- **Cơ chế nguy hiểm**: Nếu độ dài chuỗi nguồn `src` lớn hơn hoặc bằng tham số `n`, hàm `strncpy(dest, src, n)` **sẽ KHÔNG tự động chèn ký tự Null `\0` vào cuối chuỗi `dest`**!
- Hậu quả: Khi gọi `printf("%s", dest)` hoặc `strlen(dest)`, chương trình sẽ đọc tràn sang các ô nhớ bên ngoài (Buffer Over-read).
- **Quy tắc lập trình an toàn bắt buộc**:
  ```c
  char dest[16];
  // Luôn dành 1 byte cho ký tự kết thúc và chủ động gán '\0' tại vị trí cuối cùng:
  strncpy(dest, user_input, sizeof(dest) - 1);
  dest[sizeof(dest) - 1] = '\0'; // Bắt buộc phải có dòng này!
  ```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sự khác biệt giữa Pseudo-Random (`rand()`) và Cryptographic Random (`SecureRandom`)
```
[Hàm rand() / Math.random()]
  Hạt giống (Seed: Thời gian máy tính) ──► Thuật toán LCG ──► Dãy số có quy luật
  └── Hacker tính toán ngược lại Seed chỉ sau vài giá trị mẫu ──► Đoán được Session ID / Token!

[Lớp SecureRandom (CSPRNG)]
  Nhiễu nhiệt CPU + Biến động bàn phím + Ngắt mạng ──► Bể Entropy ngẫu nhiên thực
  └── Bất khả thi để dự đoán giá trị tiếp theo theo mặt toán học ──► AN TOÀN TUYỆT ĐỐI.
```

---

### 복습 체크리스트
- [ ] Tại sao hàm `gets()` lại bị khai tử và cấm sử dụng hoàn toàn trong tiêu chuẩn C11?
- [ ] Hàm `strncpy(dest, src, n)` gặp phải cạm bẫy gì liên quan đến ký tự kết thúc chuỗi `\0`?
- [ ] Tại sao trong các ứng dụng bảo mật (sinh mã OTP, Token xác thực) ta không được sử dụng hàm `rand()` hay `Math.random()`?
- [ ] Hàm thay thế an toàn cho hàm định dạng chuỗi `sprintf()` trong ngôn ngữ C là hàm nào?
