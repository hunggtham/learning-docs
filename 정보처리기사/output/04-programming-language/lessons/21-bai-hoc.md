# 배열과 포인터 심화 (Arrays & Pointers - Advanced)

## 학습 목표 (Mục tiêu)
- Nắm vững các phép toán số học nâng cao trên con trỏ (포인터 연산) và cơ chế dịch chuyển địa chỉ ô nhớ theo kích thước kiểu dữ liệu cơ sở.
- Phân biệt sự khác biệt giữa Con trỏ chuỗi ký tự (`char *p = "KOREA";`) và Mảng chuỗi ký tự (`char str[] = "KOREA";`).
- Phân biệt rõ ràng giữa Mảng con trỏ (포인터 배열 / `int *arr[3]`) và Con trỏ mảng (배열 포인터 / `int (*arr)[3]`).

## 핵심 키워드 (Từ khóa)
- 포인터 연산 (Pointer Arithmetic / `ptr + n`)
- 문자열 포인터 (String Pointer / 문자열 상수)
- 포인터 배열 (Array of Pointers / `int *arr[]`)
- 배열 포인터 (Pointer to an Array / `int (*arr)[]`)
- 간접 참조 (Dereferencing / `*(*(arr + i) + j)`)
- 불변 문자열 (Read-only String Literal)

## 선행·연결 개념 (Kiến thức liên kết)
- [20-bai-hoc.md](20-bai-hoc.md): Mảng 2 chiều và công thức tính địa chỉ ô nhớ.
- [22-bai-hoc.md](22-bai-hoc.md): Tổng hợp mảng, câu lệnh điều kiện và vòng lặp.
- [19-bai-hoc.md](19-bai-hoc.md): Con trỏ, mảng và ký tự kết thúc chuỗi `\0`.

## 읽는 방법 (Cách đọc)
- Phân biệt hai khai báo dễ gây nhầm lẫn nhất trong đề thi:
  - **`int *arr[3]` (Mảng các con trỏ):** Đọc từ dấu ngoặc vuông trước $\rightarrow$ Là một MẢNG gồm 3 phần tử, mỗi phần tử bên trong là một con trỏ kiểu `int*`. Thường dùng để quản lý một danh sách nhiều chuỗi ký tự có độ dài ngắn khác nhau.
  - **`int (*arr)[3]` (Con trỏ trỏ tới mảng):** Đọc dấu ngoặc tròn trước $\rightarrow$ Là duy nhất MỘT CON TRỎ trỏ tới một mảng gồm 3 số nguyên. Kích thước biến `arr` chỉ bằng kích thước 1 con trỏ (4 hoặc 8 bytes).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh: Mảng con trỏ vs Con trỏ mảng:**

| Cú pháp khai báo | Tên gọi chuẩn thi | Bản chất biến | Kích thước bộ nhớ (32-bit) | Ngữ cảnh ứng dụng |
| :--- | :--- | :--- | :--- | :--- |
| **`int *arr[3];`** | **포인터 배열 (Pointer Array)** | Là một **Mảng gồm 3 phần tử**, mỗi phần tử chứa 1 địa chỉ ô nhớ | $3 \times 4\text{ Bytes} = 12\text{ Bytes}$ | Quản lý danh sách các chuỗi hoặc mảng rời rạc |
| **`int (*arr)[3];`** | **배열 포인터 (Array Pointer)** | Là **Duy nhất 1 biến con trỏ**, trỏ tới mảng 1 chiều có 3 số nguyên | Đúng bằng $1$ con trỏ $= 4\text{ Bytes}$ | Truyền mảng 2 chiều làm tham số hàm |

- **So sánh Con trỏ chuỗi vs Mảng chuỗi trong C:**

| Tiêu chuẩn | `char str[] = "KOREA";` (Mảng chuỗi) | `char *p = "KOREA";` (Con trỏ chuỗi) |
| :--- | :--- | :--- |
| **Vị trí lưu trữ** | Toàn bộ các ký tự được chép vào vùng nhớ **Stack** | Chuỗi nằm ở vùng nhớ hằng số **Read-Only Data Segment**; con trỏ `p` lưu trên Stack |
| **Khả năng thay đổi** | **Có thể sửa đổi:** `str[0] = 'C';` hợp lệ | **Tuyệt đối không thể sửa:** `*p = 'C';` gây lỗi hệ thống (Segmentation Fault) |
| **Bản chất biến** | `str` là một **hằng con trỏ**, không thể gán địa chỉ mới | `p` là một **biến con trỏ**, có thể trỏ sang chuỗi khác `p = "SEOUL";` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu lần vết con trỏ chuỗi:**
  - *Đoạn mã C:*
    ```c
    char *p = "KOREA";
    printf("%s\n", p + 2);
    printf("%c\n", *(p + 1));
    ```
  - *Quá trình phân tích:*
    1. Chuỗi `"KOREA"` gồm các ký tự tại các chỉ số $0, 1, 2, 3, 4$: `'K'`, `'O'`, `'R'`, `'E'`, `'A'`.
    2. Phép toán `p + 2`: Con trỏ nhảy sang địa chỉ của ký tự thứ 3 (chỉ số 2) là `'R'`. Do dùng định dạng chuỗi `%s`, hàm in toàn bộ phần còn lại từ vị trí đó cho đến khi gặp `\0` $\rightarrow$ In ra: `REA`.
    3. Phép toán `*(p + 1)`: Lấy giá trị của ký tự tại chỉ số 1 (định dạng `%c`) $\rightarrow$ In ra: `O`.

### 복습 체크리스트
- [ ] Phân biệt được `int *arr[3]` (mảng gồm 3 con trỏ) và `int (*arr)[3]` (con trỏ trỏ tới mảng 3 số nguyên).
- [ ] Nhớ con trỏ chuỗi `char *p = "..."` trỏ vào vùng nhớ chỉ đọc (Read-only), không được sửa ký tự.
- [ ] Tính đúng: Với `p = "KOREA"`, lệnh `printf("%s", p + 2)` in ra `REA`.
