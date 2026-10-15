# Python 기본 문법 (Python Basic Syntax)

## 학습 목표 (Mục tiêu)
- Nắm vững các đặc trưng cú pháp nền tảng của ngôn ngữ lập trình Python: Không cần khai báo kiểu dữ liệu biến (Dynamic Typing), không bắt buộc dấu chấm phẩy `;` ở cuối dòng lệnh.
- Hiểu sâu nguyên tắc phân chia khối mã nguồn bằng dấu hai chấm `:` kết hợp thụt lề bắt buộc (들여쓰기 - Indentation) thay thế hoàn toàn cho cặp ngoặc nhọn `{ }` trong C/Java.
- Nắm vững cú pháp các câu lệnh điều khiển luồng trong Python: Câu lệnh rẽ nhánh `if - elif - else` (lưu ý dùng `elif` thay vì `else if`) và hàm định nghĩa `def`.

## 핵심 키워드 (Từ khóa)
- 파이썬 기본 문법 (Python Basic Syntax)
- 들여쓰기 (Indentation / 4 Spaces / 블록 구분)
- 콜론 (Colon `:` / 블록 시작 기호)
- 동적 타이핑 (Dynamic Typing / 타입 선언 생략)
- elif문 (Else If 대체 키워드)
- def 키워드 (함수 정의)
- IndentationError (들여쓰기 오류)

## 선행·연결 개념 (Kiến thức liên kết)
- [25-bai-hoc.md](25-bai-hoc.md): Các cấu trúc dữ liệu cơ bản trong Python.
- [27-bai-hoc.md](27-bai-hoc.md): Kiểu chuỗi tuần tự và đặc tính bất biến của Tuple.
- [28-bai-hoc.md](28-bai-hoc.md): Tổng hợp ngữ pháp và bài tập phân tích mã nguồn Python.

## 읽는 방법 (Cách đọc)
- Nhớ 3 điểm khác biệt lớn nhất giữa Python và C/Java:
  1. **Không dùng ngoặc nhọn `{ }` để tạo khối lệnh:** Python dùng dấu hai chấm `:` ở cuối dòng tiêu đề (như sau `if`, `for`, `while`, `def`, `class`), các dòng lệnh con bên trong **bắt buộc phải thụt lề cùng cấp độ** (thường là 4 dấu cách Space). Thụt lề sai sẽ bị lỗi cú pháp `IndentationError`.
  2. **Dùng từ khóa `elif` thay vì `else if`:** Cú pháp rẽ nhánh nhiều tầng là `if điều_kiện_1: ... elif điều_kiện_2: ... else: ...`.
  3. **Không cần khai báo kiểu dữ liệu:** Chỉ cần viết `x = 10` (tự hiểu là `int`) hoặc `x = "Hello"` (tự hiểu là `str`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu cú pháp cơ bản: C/Java vs Python:**

| Thành phần cú pháp | Ngôn ngữ C / Java | Ngôn ngữ Python | Điểm lưu ý thi cử |
| :--- | :--- | :--- | :--- |
| **Phân cách khối lệnh** | Cặp ngoặc nhọn `{ ... }` | **Dấu hai chấm `:` và thụt lề (Indentation)** | Sai thụt lề sẽ báo lỗi `IndentationError` ngay khi chạy |
| **Kết thúc câu lệnh** | Bắt buộc có dấu chấm phẩy `;` | **Xuống dòng là kết thúc**; không cần dấu `;` | Đặt dấu `;` trong Python không lỗi nhưng không bắt buộc |
| **Khai báo biến** | `int a = 10; String s = "Hi";` | `a = 10; s = "Hi"` | Kiểu dữ liệu được gán tự động tại thời điểm chạy (Dynamic Typing) |
| **Rẽ nhánh nhiều nhánh** | `if (...) { } else if (...) { }` | `if ... : ... elif ... : ... else :` | **Từ khóa là `elif`**, không phải `else if` |
| **Định nghĩa hàm** | `int add(int a, int b) { return a+b; }` | `def add(a, b): return a + b` | Dùng từ khóa **`def`**, không cần khai báo kiểu trả về |

- **Cấu trúc vòng lặp `for` với `range()` trong Python:**
  - Cú pháp: `for biến in range(bắt_đầu, kết_thúc, bước_nhảy):`
  - *Quy tắc:* Luôn chạy từ `bắt_đầu` đến **`kết_thúc - 1`**.
  - Ví dụ:
    ```python
    sum = 0
    for i in range(1, 6): # i lần lượt nhận 1, 2, 3, 4, 5
        sum += i
    print(sum) # In ra: 15
    ```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Hàm vô danh Lambda trong Python:**
  - Cú pháp viết hàm ngắn gọn 1 dòng: `lambda tham_số: biểu_thức`.
  - Ví dụ: `square = lambda x: x * x; print(square(5))` $\rightarrow$ In ra: `25`.
  - Thường kết hợp với hàm `map()` hoặc `filter()` để xử lý mảng dữ liệu.

### 복습 체크리스트
- [ ] Nhớ Python dùng dấu hai chấm `:` và thụt lề để phân tách khối lệnh (thay thế `{ }`).
- [ ] Nhớ từ khóa rẽ nhánh nhiều tầng trong Python là `elif` (không dùng `else if`).
- [ ] Nhớ từ khóa định nghĩa hàm trong Python là `def`.
- [ ] Tính đúng: `range(1, 5)` sinh ra dãy số 1, 2, 3, 4 (không có số 5).
