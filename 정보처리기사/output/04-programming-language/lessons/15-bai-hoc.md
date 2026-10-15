# 074. 데이터 입출력 (Data Input/Output)

## 학습 목표 (Mục tiêu)
- Nắm vững bức tranh tổng quan về cơ chế nhập xuất dữ liệu (데이터 입·출력) trên cả 3 ngôn ngữ lập trình chủ đạo trong kỳ thi: C, Java, và Python.
- So sánh sự khác nhau về cú pháp hàm nhập: `scanf()` trong C, `Scanner` trong Java, và hàm `input()` trong Python.
- Hiểu rõ cơ chế điều khiển ký tự kết thúc dòng của hàm in: `\n` trong C/Java, `println()` trong Java, và tham số `end=''` trong Python.

## 핵심 키워드 (Từ khóa)
- 데이터 입출력 (Data Input & Output)
- 표준 입출력 스트림 (Standard I/O Streams / stdin, stdout)
- C언어 입출력 (scanf, printf)
- JAVA 입출력 (Scanner, System.out.println)
- Python 입출력 (input, print / sep, end 매개변수)
- 자동 개행 제어 (Newline Control)

## 선행·연결 개념 (Kiến thức liên kết)
- [14-bai-hoc.md](14-bai-hoc.md): Nhập xuất nâng cao và chuỗi định dạng trong C.
- [16-bai-hoc.md](16-bai-hoc.md): Các hàm xuất nhập ký tự và chuỗi trong C.
- [03-bai-hoc.md](03-bai-hoc.md): Kiểu dữ liệu, biến và toán tử.

## 읽는 방법 (Cách đọc)
- Phân biệt đặc trưng nhập xuất theo 3 ngôn ngữ:
  - **C:** Dùng chuỗi định dạng chặt chẽ (`%d`, `%f`). Hàm `scanf` đòi hỏi địa chỉ `&`.
  - **Java:** Hướng đối tượng hoàn toàn. Nhập dữ liệu qua lớp `Scanner sc = new Scanner(System.in);` (`nextInt()`, `nextLine()`). Xuất dữ liệu qua `System.out.println()`.
  - **Python:** Tối giản và linh hoạt nhất. Nhập dữ liệu bằng `input()` (mặc định luôn trả về kiểu chuỗi `str`). Xuất bằng `print()` (mặc định tự động xuống dòng; muốn không xuống dòng thì đặt tham số `end=''`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng đối chiếu hàm nhập xuất trên 3 ngôn ngữ:**

| Ngôn ngữ | Hàm nhập chuẩn (Standard Input) | Hàm xuất chuẩn (Standard Output) | Đặc trưng điều khiển xuống dòng |
| :--- | :--- | :--- | :--- |
| **C** | `scanf("%d", &a);` | `printf("%d\n", a);` | Bắt buộc phải có `\n` trong chuỗi định dạng để xuống dòng |
| **Java** | `Scanner sc = new Scanner(System.in); int a = sc.nextInt();` | `System.out.println(a);` | `println()` **tự động xuống dòng** sau khi in; `print()` không xuống dòng |
| **Python** | `a = int(input())` | `print(a)` | `print()` **mặc định tự động xuống dòng**; dùng `print(a, end='')` để giữ nguyên dòng |

- **Hai tham số tùy biến mạnh mẽ của hàm `print()` trong Python:**
  - **Tham số `sep` (Separator):** Chỉ định ký tự phân cách giữa các phần tử khi in nhiều giá trị:
    - *Ví dụ:* `print("2026", "10", "15", sep="-")` $\rightarrow$ In ra: `2026-10-15`.
  - **Tham số `end` (End character):** Chỉ định ký tự kết thúc sau cùng của lệnh in (mặc định là `\n`):
    - *Ví dụ:* `print("Hello", end=" ")` tiếp tục với `print("World")` $\rightarrow$ In ra: `Hello World` trên cùng 1 dòng.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bẫy kiểu dữ liệu của hàm `input()` trong Python:**
  - Trong Python, hàm `input()` luôn trả về kiểu chuỗi ký tự (`str`).
  - Nếu người dùng nhập số `10` và `20`:
    ```python
    a = input()  # Nhập 10
    b = input()  # Nhập 20
    print(a + b) # In ra: 1020 (Ghép chuỗi, không phải phép cộng số học)
    ```
  - Muốn thực hiện phép cộng toán học, bắt buộc phải ép kiểu bằng hàm `int()`: `print(int(a) + int(b))` $\rightarrow$ In ra `30`.

### 복습 체크리스트
- [ ] Nhớ hàm `input()` trong Python luôn trả về chuỗi ký tự (cần ép kiểu `int(input())`).
- [ ] Nhớ trong Python: dùng `end=''` để ngăn tự động xuống dòng, dùng `sep` để đổi ký tự phân cách.
- [ ] Nhớ đối tượng `Scanner` trong Java cần tạo mới qua `new Scanner(System.in)`.
- [ ] Nhớ hàm `scanf` trong C cần `&` trước biến để lấy địa chỉ ô nhớ.
