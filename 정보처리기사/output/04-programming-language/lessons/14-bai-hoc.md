# 입출력 심화 (Input/Output - Advanced)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và nguyên lý hoạt động của hàm nhập chuẩn `scanf` trong ngôn ngữ C; hiểu lý do bắt buộc phải sử dụng toán tử địa chỉ `&` trước tên biến thông thường.
- Ghi nhớ đầy đủ các chuỗi định dạng nâng cao trong C: `%u` (số nguyên không dấu), `%o` (bát phân - hệ 8), `%x` (thập lục phân - hệ 16), `%e` (số thực dạng số mũ), và `%p` (địa chỉ con trỏ).
- Nắm vững các ký tự điều khiển (Escape Characters / Control Characters): `\n`, `\t`, `\b`, `\r`, và ký tự kết thúc chuỗi `\0` (Null Character).
- Hiểu các chỉ định chiều rộng và căn lề trong chuỗi định dạng xuất của C và Java (ví dụ: `%-8.2f`).

## 핵심 키워드 (Từ khóa)
- scanf() (표준 입력 함수 / 키보드 입력)
- 주소 연산자 (Address Operator `&`)
- 진법별 서식 문자열 (`%u` unsigned, `%o` octal, `%x` hex)
- 지수형 및 포인터 서식 (`%e` exponent, `%p` pointer)
- 제어문자 (Escape Characters / `\n`, `\t`, `\r`, `\0`)
- 널 문자 (Null Character `\0` / ASCII 0 / 문자열 끝)
- 정렬 및 자릿수 포맷 (`%-8.2f` / 좌측 정렬, 폭, 정밀도)

## 선행·연결 개념 (Kiến thức liên kết)
- [13-bai-hoc.md](13-bai-hoc.md): Nhập xuất cơ bản và chuỗi định dạng `%d, %f, %c, %s`.
- [15-bai-hoc.md](15-bai-hoc.md): Tổng quan nhập xuất đa ngôn ngữ C, Java, Python.
- [19-bai-hoc.md](19-bai-hoc.md): Con trỏ, mảng và chuỗi ký tự kết thúc bằng `\0`.

## 읽는 방법 (Cách đọc)
- Phân biệt các quy tắc nhập xuất nâng cao:
  - **Quy tắc toán tử địa chỉ `&` trong `scanf`:** `scanf("%d", &a);` $\rightarrow$ Vì `scanf` cần ghi đè dữ liệu nhận từ bàn phím trực tiếp vào ô nhớ RAM của biến `a`, nó bắt buộc phải biết địa chỉ ô nhớ `&a`. Ngoại lệ duy nhất là Mảng chuỗi ký tự (`char str[20]; scanf("%s", str);`) không cần `&` vì bản thân tên mảng `str` đã đại diện cho địa chỉ ô nhớ đầu tiên.
  - **Quy tắc giải mã format `%-8.2f`:**
    - Dấu trừ `-`: Căn lề về bên trái (**좌측 정렬**). Nếu không có dấu trừ là căn phải mặc định.
    - Con số `8`: Tổng độ rộng của toàn bộ trường xuất ra là 8 ký tự (bao gồm cả dấu chấm).
    - `.2`: Lấy đúng 2 chữ số sau dấu phẩy thập phân.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các chuỗi định dạng số học nâng cao (서식 문자열):**

| Ký tự định dạng | Tên gốc tiếng Anh | Ý nghĩa biểu diễn chuẩn đề thi | Ví dụ in giá trị 10 |
| :--- | :--- | :--- | :--- |
| **`%u`** | **Unsigned Decimal** | Số nguyên hệ thập phân **không có dấu** (Chỉ biểu diễn số dương) | `printf("%u", 10);` $\rightarrow$ `10` |
| **`%o`** | **Octal (Bát phân)** | Số nguyên biểu diễn dưới dạng **hệ cơ số 8** | `printf("%o", 10);` $\rightarrow$ `12` ($1 \times 8 + 2$) |
| **`%x` / `%X`** | **Hexadecimal (Thập lục phân)** | Số nguyên biểu diễn dưới dạng **hệ cơ số 16** (a-f hoặc A-F) | `printf("%x", 10);` $\rightarrow$ `a` |
| **`%e` / `%E`** | **Exponential** | Số thực biểu diễn theo dạng **khoa học / số mũ ($m \times 10^n$)** | `printf("%e", 123.4);` $\rightarrow$ `1.234000e+02` |
| **`%p`** | **Pointer Address** | In giá trị **địa chỉ ô nhớ con trỏ** dưới dạng hệ 16 | `printf("%p", &a);` $\rightarrow$ `0x7ffee4b2` |

- **Bảng các ký tự điều khiển (Escape Sequence):**

| Ký tự | Tên tiếng Anh | Ý nghĩa hành vi khi in |
| :--- | :--- | :--- |
| **`\n`** | **New Line** | Di chuyển con trỏ xuống đầu dòng mới tiếp theo |
| **`\t`** | **Horizontal Tab** | Nhảy con trỏ sang điểm dừng Tab kế tiếp (thường là 4 hoặc 8 dấu cách) |
| **`\b`** | **Backspace** | Lùi con trỏ về phía trước 1 ký tự |
| **`\r`** | **Carriage Return** | Đưa con trỏ quay về vị trí đầu tiên của dòng hiện tại |
| **`\0`** | **Null Character** | Ký tự kết thúc chuỗi (ASCII code 0); đánh dấu điểm dừng của chuỗi trong C |
| **`\\`, `\"`, `\'`** | **Escape Quote / Slash** | In ra ký tự gạch chéo ngược, dấu nháy kép, hoặc nháy đơn |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật căn lề và định dạng số thập phân trong Java/C:**
  - Lệnh gọi: `System.out.printf("%-8.2f", 200.2);`
  - Giá trị: `200.2` được làm tròn 2 số thập phân thành `200.20` (độ dài 6 ký tự).
  - Độ rộng chỉ định là `8` và có dấu `-` (căn trái) $\rightarrow$ Hệ thống tự động bù thêm 2 dấu khoảng trắng vào phía sau.
  - Kết quả in ra màn hình: `'200.20  '`.

### 복습 체크리스트
- [ ] Nhớ hàm `scanf` bắt buộc phải có `&` trước tên biến (trừ tên mảng chuỗi).
- [ ] Nhớ các ký tự định dạng: `%o` (hệ 8), `%x` (hệ 16), `%u` (không dấu), `%p` (địa chỉ con trỏ).
- [ ] Nhớ ký tự `\0` (Null) đánh dấu kết thúc chuỗi trong C.
- [ ] Giải mã được định dạng `%-8.2f`: Căn lề trái, rộng 8 ký tự, 2 chữ số thập phân.
