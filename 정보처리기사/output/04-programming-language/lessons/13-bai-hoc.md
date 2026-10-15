# 입출력 (Input/Output)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và nguyên lý hoạt động của các hàm xuất dữ liệu tiêu chuẩn (표준 출력 함수) trong ngôn ngữ C (`printf`) và ngôn ngữ Java (`print`, `println`, `printf`).
- Ghi nhớ chính xác ý nghĩa của các chuỗi định dạng cơ bản (서식 문자열 - Format Specifiers): `%d` (Số nguyên hệ thập phân), `%f` (Số thực), `%c` (Ký tự đơn), và `%s` (Chuỗi ký tự).
- Phân biệt sự khác biệt về hành vi xuống dòng tự động giữa phương thức `print()` và `println()` trong Java.

## 핵심 키워드 (Từ khóa)
- 표준 출력 (Standard Output)
- printf() (Formatted Print / C언어 및 JAVA)
- 서식 문자열 (Format Specifiers / `%d`, `%f`, `%c`, `%s`)
- JAVA 출력 함수 (print, println, printf)
- 개행 문자 (Newline / `\n` / 자동 개행)
- 포맷 매칭 (Argument-Specifier Matching)

## 선행·연결 개념 (Kiến thức liên kết)
- [12-bai-hoc.md](12-bai-hoc.md): Thứ tự ưu tiên của các toán tử.
- [14-bai-hoc.md](14-bai-hoc.md): Nhập xuất nâng cao và hàm `scanf`.
- [15-bai-hoc.md](15-bai-hoc.md): Tổng hợp dữ liệu nhập xuất đa ngôn ngữ.

## 읽는 방법 (Cách đọc)
- Phân biệt các ký tự định dạng cốt lõi:
  - `%d`: Chữ cái đầu của **Decimal** $\rightarrow$ Dùng cho số nguyên hệ thập phân (`int`, `short`).
  - `%f`: Chữ cái đầu của **Float** $\rightarrow$ Dùng cho số thực có phần thập phân (`float`, `double`).
  - `%c`: Chữ cái đầu của **Character** $\rightarrow$ Dùng cho một ký tự đơn nằm trong nháy đơn `'A'`.
  - `%s`: Chữ cái đầu của **String** $\rightarrow$ Dùng cho một chuỗi ký tự nằm trong nháy kép `"Hello"`.
- Trong Java:
  - `System.out.print()`: In xong con trỏ đứng yên tại chỗ, **không xuống dòng**.
  - `System.out.println()`: In xong **tự động nhảy xuống đầu dòng tiếp theo** (tương đương in thêm `\n`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng các chuỗi định dạng xuất tiêu chuẩn (서식 문자열):**

| Chuỗi định dạng | Tên tiếng Anh đầy đủ | Kiểu dữ liệu tương thích | Ví dụ lệnh gọi và kết quả |
| :--- | :--- | :--- | :--- |
| **`%d`** | **Decimal (Thập phân)** | Số nguyên có dấu (`int`, `short`) | `printf("%d", 25);` $\rightarrow$ In ra `25` |
| **`%f`** | **Floating-point (Số thực)** | Số thực dấu phẩy động (`float`, `double`) | `printf("%.2f", 3.14159);` $\rightarrow$ In ra `3.14` |
| **`%c`** | **Character (Ký tự)** | Một ký tự đơn kiểu `char` | `printf("%c", 'K');` $\rightarrow$ In ra `K` |
| **`%s`** | **String (Chuỗi)** | Mảng ký tự, con trỏ chuỗi (`char*`) | `printf("%s", "PASS");` $\rightarrow$ In ra `PASS` |

- **Bảng so sánh 3 phương thức xuất dữ liệu trong Java:**

| Phương thức Java | Cơ chế xuống dòng | Khả năng định dạng chuỗi | Ví dụ cú pháp chuẩn |
| :--- | :--- | :--- | :--- |
| **`System.out.print()`** | **Không xuống dòng**; lần in tiếp theo dính liền ngay sau | Ghép chuỗi bằng toán tử cộng `+` | `System.out.print("A"); System.out.print("B");` $\rightarrow$ In ra `AB` |
| **`System.out.println()`** | **Tự động xuống dòng (Auto Newline)** sau khi in xong | Ghép chuỗi bằng toán tử cộng `+` | `System.out.println("Line1");` $\rightarrow$ In xong ngắt dòng |
| **`System.out.printf()`** | **Không tự động xuống dòng**; phải chèn thêm `\n` | Hỗ trợ chuỗi định dạng `%d, %f, %s` giống hệt C | `System.out.printf("%s: %d\n", "Score", 100);` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ghép chuỗi trong Java với toán tử `+`:**
  - Trong Java, khi toán tử cộng `+` gặp một toán hạng là chuỗi ký tự (`String`), toán hạng còn lại sẽ tự động được chuyển đổi thành chuỗi (String Concatenation).
  - *Ví dụ:* `System.out.println("Sum: " + 10 + 20);` sẽ in ra `Sum: 1020` (do ghép chuỗi tuần tự từ trái qua phải). Muốn in ra 30, phải bọc ngoặc: `System.out.println("Sum: " + (10 + 20));`.

### 복습 체크리스트
- [ ] Nhớ các ký tự định dạng: `%d` (nguyên), `%f` (thực), `%c` (ký tự), `%s` (chuỗi).
- [ ] Phân biệt được `print()` (không ngắt dòng) và `println()` (tự động ngắt dòng) trong Java.
- [ ] Nhớ hàm `printf` trong cả C và Java không tự động xuống dòng nếu không có `\n`.
- [ ] Giải thích được kết quả in của biểu thức `"A" + 1 + 2` trong Java.
