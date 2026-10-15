# 258 - 261. 배열과 문자열 (Arrays & Strings)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc biểu diễn chuỗi ký tự (문자열 - String) dưới dạng mảng 1 chiều kiểu `char` kết thúc bằng ký tự rỗng `\0` trong ngôn ngữ C.
- Phân biệt sâu sắc sự khác nhau giữa toán tử kích thước `sizeof` (đo dung lượng bộ nhớ thực tế, tính cả `\0`) và hàm `strlen` (đo độ dài ký tự hiển thị, không tính `\0`).
- Nắm vững cú pháp, nguyên lý hoạt động và giá trị trả về của 4 hàm xử lý chuỗi kinh điển trong thư viện `<string.h>`: `strlen`, `strcpy`, `strcat`, và `strcmp`.

## 핵심 키워드 (Từ khóa)
- 문자열 배열 (Character Array / C-String)
- 널 문자 (Null Character `\0` / ASCII 0 / 종결자)
- strlen() (문자열 길이 계산 / 널 문자 제외)
- strcpy() (문자열 복사 / String Copy)
- strcat() (문자열 연결 / String Concatenate)
- strcmp() (문자열 비교 / 0, 음수, 양수 반환)
- sizeof vs strlen (메모리 크기 vs 실제 문자수)

## 선행·연결 개념 (Kiến thức liên kết)
- [22-bai-hoc.md](22-bai-hoc.md): Mảng, câu lệnh điều kiện và vòng lặp.
- [24-bai-hoc.md](24-bai-hoc.md): Con trỏ và quản lý bộ nhớ động.
- [19-bai-hoc.md](19-bai-hoc.md): Cấu trúc, mảng và con trỏ cơ bản.

## 읽는 방법 (Cách đọc)
- Phân biệt 4 hàm trong thư viện `<string.h>`:
  - **`strlen(s)`:** Đếm số ký tự từ đầu đến trước ký tự `\0`.
  - **`strcpy(dest, src)`:** Sao chép toàn bộ chuỗi từ nguồn `src` đè vào chuỗi đích `dest` (bao gồm cả ký tự `\0`).
  - **`strcat(dest, src)`:** Nối chuỗi `src` vào ngay phía sau đuôi của chuỗi `dest` (ghi đè lên ký tự `\0` cũ của `dest`).
  - **`strcmp(s1, s2)`:** So sánh theo thứ tự từ điển mã ASCII từng ký tự:
    - Bằng nhau: Trả về **`0`**.
    - $s1 \lt s2$: Trả về **số âm (`< 0`)**.
    - $s1 > s2$: Trả về **số dương (`> 0`)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 4 hàm xử lý chuỗi cốt lõi trong thư viện `<string.h>`:**

| Tên hàm | Cú pháp chuẩn | Mô tả hành vi kỹ thuật | Ví dụ minh họa và kết quả |
| :--- | :--- | :--- | :--- |
| **`strlen`** | `size_t strlen(const char *s)` | Đếm số lượng ký tự của chuỗi; **tuyệt đối không tính ký tự `\0`** | `strlen("KOREA")` $\rightarrow$ `5` |
| **`strcpy`** | `char *strcpy(char *dest, const char *src)` | Chép toàn bộ chuỗi từ `src` sang `dest` | `strcpy(a, "HELLO");` $\rightarrow$ $a$ chứa `"HELLO"` |
| **`strcat`** | `char *strcat(char *dest, const char *src)` | Nối chuỗi `src` vào đuôi chuỗi `dest`; tự động gắn thêm `\0` mới | $a = \text{"AB"}$, `strcat(a, "CD")` $\rightarrow$ $a = \text{"ABCD"}$ |
| **`strcmp`** | `int strcmp(const char *s1, const char *s2)` | So sánh từng ký tự theo bảng mã ASCII; dừng ngay khi có cặp ký tự khác nhau | `strcmp("A", "B")` $\rightarrow$ Âm (`-1`); `strcmp("C", "A")` $\rightarrow$ Dương (`1`); `strcmp("A", "A")` $\rightarrow$ Bằng `0` |

- **Bảng so sánh trực diện: `sizeof` vs `strlen`:**

| Tiêu chuẩn so sánh | `sizeof(str)` | `strlen(str)` |
| :--- | :--- | :--- |
| **Bản chất kỹ thuật** | **Toán tử ngôn ngữ (Operator)** xác định tại thời điểm biên dịch (Compile-time) | **Hàm thư viện (Library Function)** thực thi duyệt chuỗi tại thời điểm chạy (Runtime) |
| **Xử lý ký tự `\0`** | **Có tính cả ký tự `\0`** và toàn bộ kích thước mảng cấp phát | **Bỏ qua ký tự `\0`**, chỉ đếm ký tự chữ cái thực tế |
| **Ví dụ: `char s[10] = "ABC";`** | `sizeof(s)` trả về **`10`** (Tổng dung lượng mảng) | `strlen(s)` trả về **`3`** (Độ dài chữ "ABC") |
| **Ví dụ: `char s[] = "ABC";`** | `sizeof(s)` trả về **`4`** (Gồm 'A','B','C','\0') | `strlen(s)` trả về **`3`** |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu lần vết hàm chuỗi kết hợp:**
  - *Đoạn mã C:*
    ```c
    char a[20] = "Data";
    char b[] = "Base";
    strcat(a, b);
    printf("%d %d", strlen(a), sizeof(a));
    ```
  - *Quá trình phân tích:*
    1. Chuỗi ban đầu của `a` là `"Data"` (độ dài 4, kích thước mảng 20).
    2. Hàm `strcat(a, b)` nối chuỗi `"Base"` vào đuôi mảng `a` $\rightarrow$ Mảng `a` trở thành `"DataBase\0"`.
    3. `strlen(a)` đếm độ dài chữ `"DataBase"` $\rightarrow$ Trả về **`8`**.
    4. `sizeof(a)` đo kích thước khai báo cố định của mảng `a[20]` $\rightarrow$ Trả về **`20`**.
    5. Kết quả in ra màn hình: `8 20`.

### 복습 체크리스트
- [ ] Nhớ `strlen` không đếm `\0`, nhưng `sizeof` chuỗi tính cả `\0`.
- [ ] Nhớ hàm `strcmp` trả về 0 khi hai chuỗi giống nhau 100%.
- [ ] Nhớ thứ tự tham số của `strcpy(đích, nguồn)` và `strcat(đích, nguồn)`.
- [ ] Cảnh giác: Mảng đích `dest` phải đủ lớn để chứa chuỗi nối, nếu không sẽ bị tràn bộ đệm (Buffer Overflow).
