# 262 - 263. 포인터 (Pointers)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và nguyên lý hoạt động của biến con trỏ (포인터 변수 - Pointer Variable): biến chuyên biệt lưu trữ địa chỉ vùng nhớ vật lý (Memory Address) của biến khác trong bộ nhớ RAM.
- Phân biệt rõ ràng hai toán tử cốt lõi thao tác với con trỏ: Toán tử lấy địa chỉ `&` (Address-of Operator) và Toán tử giải tham chiếu gián tiếp `*` (Dereferencing Operator).
- Hiểu cấu trúc và cơ chế truy xuất của con trỏ cấp hai (이중 포인터 - Double Pointer / `**ptr`).
- Nắm vững quy trình cấp phát bộ nhớ động (동적 메모리 할당) bằng các hàm `malloc()`, `calloc()` và giải phóng bộ nhớ bằng `free()`.

## 핵심 키워드 (Từ khóa)
- 포인터 변수 (Pointer Variable / 주소 저장 변수)
- 간접 참조 연산자 (Dereference Operator `*`)
- 주소 연산자 (Address-of Operator `&`)
- 이중 포인터 (Double Pointer / `**ptr`)
- 동적 메모리 할당 (Dynamic Memory Allocation / Heap 영역)
- malloc() & free() (동적 할당 및 메모리 해제)
- 댕글링 포인터 (Dangling Pointer / 허공을 가리키는 포인터)

## 선행·연결 개념 (Kiến thức liên kết)
- [23-bai-hoc.md](23-bai-hoc.md): Xử lý mảng và chuỗi ký tự trong C.
- [25-bai-hoc.md](25-bai-hoc.md): Nhập môn cú pháp và cấu trúc dữ liệu Python.
- [19-bai-hoc.md](19-bai-hoc.md): Cấu trúc, mảng và quan hệ tương đương con trỏ.

## 읽는 방법 (Cách đọc)
- Phân biệt hai vai trò của dấu hoa thị `*`:
  - **Khi khai báo (`int *p;`):** Dấu `*` đi liền sau kiểu dữ liệu mang ý nghĩa: "Khai báo `p` là một biến con trỏ, nơi chứa địa chỉ của một biến số nguyên `int`".
  - **Khi tính toán câu lệnh (`*p = 20;` hoặc `x = *p;`):** Dấu `*` mang ý nghĩa hành động: "Hãy đi tới địa chỉ mà `p` đang nắm giữ, mở ô nhớ đó ra để đọc hoặc ghi đè giá trị mới vào".
- Con trỏ cấp hai `int **q;`:
  - `q` lưu địa chỉ của con trỏ cấp một `p`.
  - `*q` trỏ tới con trỏ `p` (giá trị là địa chỉ của `a`).
  - `**q` giải tham chiếu 2 lần để chạm tới giá trị thực sự của biến `a`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng phân tích mối quan hệ giữa biến, địa chỉ và con trỏ:**

| Thao tác | Biểu thức C | Ý nghĩa kỹ thuật cốt lõi | Giá trị ví dụ (Giả sử $a=10$ tại ô nhớ 0x100) |
| :--- | :--- | :--- | :--- |
| **Giá trị của biến** | `a` | Dữ liệu thực tế lưu bên trong biến `a` | `10` |
| **Địa chỉ của biến** | `&a` | Vị trí ô nhớ vật lý mà hệ điều hành cấp phát cho `a` | `0x100` |
| **Gán con trỏ** | `p = &a;` | Cho con trỏ `p` lưu giữ địa chỉ ô nhớ của `a` | `p` có giá trị là `0x100` |
| **Giải tham chiếu** | `*p` | Truy cập vào giá trị của ô nhớ mà `p` đang trỏ tới | `*p` trả về `10` |
| **Gán qua con trỏ** | `*p = 50;` | Ghi đè số 50 trực tiếp vào ô nhớ của biến `a` | Biến `a` đổi thành `50` |

- **Bảng các hàm cấp phát bộ nhớ động trong thư viện `<stdlib.h>`:**

| Tên hàm | Cú pháp chuẩn | Cơ chế cấp phát trên vùng nhớ Heap | Giải phóng bộ nhớ |
| :--- | :--- | :--- | :--- |
| **`malloc`** | `void *malloc(size_t size);` | Cấp phát một khối bộ nhớ có dung lượng `size` bytes; **không khởi tạo giá trị** (chứa rác) | Bắt buộc phải gọi hàm `free(ptr);` sau khi dùng xong để tránh rò rỉ bộ nhớ (Memory Leak) |
| **`calloc`** | `void *calloc(size_t n, size_t size);` | Cấp phát $n$ phần tử, mỗi phần tử `size` bytes; **tự động khởi tạo toàn bộ bit bằng 0** | Bắt buộc gọi `free(ptr);` |
| **`realloc`** | `void *realloc(void *ptr, size_t size);` | Thay đổi kích thước khối bộ nhớ đã cấp phát trước đó sang kích thước mới | Bắt buộc gọi `free(ptr);` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu lần vết con trỏ cấp hai:**
  - *Đoạn mã C:*
    ```c
    int a = 10;
    int *p = &a;
    int **q = &p;
    **q += 20;
    printf("%d %d %d", a, *p, **q);
    ```
  - *Quá trình phân tích:*
    1. Biến $a = 10$. Con trỏ $p$ trỏ tới $a$. Con trỏ kép $q$ trỏ tới $p$.
    2. Câu lệnh `**q += 20;` giải tham chiếu 2 lần qua $q \rightarrow p \rightarrow a$, thực hiện cộng dồn 20 vào chính ô nhớ của biến $a$ $\rightarrow$ $a = 10 + 20 = 30$.
    3. Do $p$ và $q$ cùng trỏ tới biến $a$, cả `a`, `*p`, và `**q` đều mang giá trị là 30.
    4. Kết quả in ra: `30 30 30`.

### 복습 체크리스트
- [ ] Nhớ toán tử `&` lấy địa chỉ ô nhớ, toán tử `*` lấy giá trị tại địa chỉ con trỏ trỏ tới.
- [ ] Phân biệt được `malloc` (không khởi tạo, chứa giá trị rác) và `calloc` (khởi tạo toàn bộ bit bằng 0).
- [ ] Nhớ mọi vùng nhớ cấp phát động bằng `malloc/calloc` đều bắt buộc phải giải phóng bằng `free()`.
- [ ] Hiểu cơ chế hoạt động của con trỏ cấp hai `**q` giải tham chiếu 2 lần.
