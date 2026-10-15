# 구조체, 배열 및 포인터 (Structs, Arrays, and Pointers)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm, cú pháp và cơ chế cấp phát bộ nhớ của 3 cấu trúc dữ liệu cốt lõi trong ngôn ngữ C: Kiểu cấu trúc (구조체 - Struct), Mảng (배열 - Array), và Biến con trỏ (포인터 - Pointer).
- Hiểu rõ cơ chế kết thúc chuỗi ký tự bằng ký tự rỗng `\0` (Null Character) và cách tính toán dung lượng bộ nhớ thực tế của chuỗi trong mảng `char`.
- Nắm vững mối quan hệ tương đương tuyệt đối giữa con trỏ và mảng trong ngôn ngữ C: Tên mảng chính là địa chỉ của phần tử đầu tiên, và biểu thức `a[i]` hoàn toàn đồng nhất với `*(a + i)`.

## 핵심 키워드 (Từ khóa)
- 구조체 (Struct / `struct` 키워드 / 이종 자료형 모음)
- 배열 (Array / 동종 자료형 연속 할당)
- 널 문자 (Null Terminator `\0` / ASCII 0)
- 포인터 변수 (Pointer Variable / `*` 간접 참조)
- 주소 연산자 (Address Operator `&`)
- 배열과 포인터의 관계 (`a[i] == *(a + i)`)
- 포인터 연산 (Pointer Arithmetic / `ptr + 1`)

## 선행·연결 개념 (Kiến thức liên kết)
- [18-bai-hoc.md](18-bai-hoc.md): Các câu lệnh điều khiển lặp trong C.
- [20-bai-hoc.md](20-bai-hoc.md): Mảng 2 chiều nâng cao và phân bổ hàng/cột.
- [04-bai-hoc.md](04-bai-hoc.md): Kích thước các kiểu dữ liệu và toán tử `sizeof`.

## 읽는 방법 (Cách đọc)
- Phân biệt các ký hiệu cốt lõi:
  - `struct`: Gom các biến **khác kiểu** (ví dụ: `name` dạng chuỗi, `age` dạng int) thành một kiểu dữ liệu mới.
  - `array`: Gom các biến **cùng kiểu** nằm liên tiếp nhau trên bộ nhớ; chỉ số index luôn bắt đầu từ 0.
  - `&`: Toán tử **Lấy địa chỉ** ô nhớ (Address-of Operator). Ví dụ: `&x` là địa chỉ nơi biến `x` cư ngụ.
  - `*`:
    - Khi khai báo (`int *p;`): Đánh dấu `p` là một **Biến con trỏ** (chuyên chứa địa chỉ).
    - Khi tính toán (`*p`): Toán tử **Giải tham chiếu (Dereferencing)**, nghĩa là đi đến địa chỉ mà `p` đang trỏ tới để móc lấy giá trị thực tế bên trong.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh Cấu trúc (Struct), Mảng (Array), và Con trỏ (Pointer):**

| Cấu trúc dữ liệu | Bản chất kiểu dữ liệu | Cách thức lưu trữ bộ nhớ | Cú pháp khai báo và truy xuất |
| :--- | :--- | :--- | :--- |
| **구조체 (Struct)** | Tập hợp các biến có **kiểu dữ liệu khác nhau (이종)** | Cấp phát liên tục; kích thước bằng tổng kích thước các trường (có thể thêm padding) | `struct Sawon { char name[10]; int pay; };` Truy xuất bằng dấu chấm `s1.pay` |
| **배열 (Array)** | Tập hợp các biến có **cùng kiểu dữ liệu (동종)** | Cấp phát **liên tiếp nhau** trên RAM; chỉ số từ $0$ đến $n-1$ | `int a[5];` Truy xuất bằng chỉ số `a[0]` hoặc con trỏ `*(a + 0)` |
| **포인터 (Pointer)** | Biến chuyên dùng để **lưu trữ địa chỉ ô nhớ** | Chiếm 4 Bytes (hệ 32-bit) hoặc 8 Bytes (hệ 64-bit) | `int *p = &a;` Lấy giá trị ô nhớ bằng `*p` |

- **Công thức tương đương kinh điển giữa Mảng và Con trỏ trong C:**
  $$\mathbf{a[i] \iff *(a + i)}$$
  $$\mathbf{\&a[i] \iff a + i}$$
  - Tên mảng `a` không có chỉ số chính là một hằng con trỏ trỏ tới phần tử đầu tiên: `a == &a[0]`.
  - Phép toán `a + i` không phải là cộng thêm $i$ byte, mà là nhảy thêm $i$ phần tử: $\text{Địa chỉ} = a + i \times \text{sizeof(kiểu dữ liệu)}$.

- **Chuỗi ký tự và Ký tự rỗng `\0`:**
  - Khai báo `char str[] = "LOVE";`
  - Thực tế trong bộ nhớ gồm 5 phần tử: `'L'`, `'O'`, `'V'`, `'E'`, và **`'\0'`**.
  - Hàm `sizeof(str)` trả về **5 bytes**; nhưng hàm tính độ dài chuỗi `strlen(str)` chỉ đếm các ký tự hiển thị nên trả về **4**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phép toán số học trên con trỏ (Pointer Arithmetic):**
  - Nếu `int *p = 1000;` (với `sizeof(int) = 4` bytes):
    - Phép tính `p + 1` sẽ có giá trị là $1000 + 1 \times 4 = 1004$.
    - Phép tính `p + 3` sẽ có giá trị là $1000 + 3 \times 4 = 1012$.
  - Nếu là kiểu `char *p = 1000;` (`sizeof(char) = 1` byte):
    - Phép tính `p + 1` sẽ có giá trị là $1000 + 1 \times 1 = 1001$.

### 복습 체크리스트
- [ ] Nhớ mảng chứa các phần tử cùng kiểu, struct chứa các phần tử khác kiểu.
- [ ] Nhớ chuỗi ký tự trong C luôn tự động gắn thêm ký tự `\0` (Null) ở cuối.
- [ ] Nhớ tên mảng `a` chính là địa chỉ phần tử đầu tiên `&a[0]`.
- [ ] Chuyển đổi thành thạo giữa `a[i]` và `*(a + i)`.
- [ ] Hiểu phép cộng con trỏ `p + 1` nhảy theo kích thước của kiểu dữ liệu mà nó trỏ tới.
