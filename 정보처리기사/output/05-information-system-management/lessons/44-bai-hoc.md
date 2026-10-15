# 포인터와 배열 (Pointer and Array)

## 학습 목표 (Mục tiêu)
- Nắm vững mối quan hệ tương đương giữa tên mảng và con trỏ trong ngôn ngữ C: Tên mảng chính là địa chỉ của phần tử đầu tiên (`arr == &arr[0]`).
- Hiểu rõ nguyên lý số học con trỏ (Pointer Arithmetic): Khi con trỏ cộng/trừ một số nguyên, địa chỉ bộ nhớ tăng/giảm theo kích thước kiểu dữ liệu (`sizeof`).
- Thành thạo quy tắc tương đương cú pháp giữa chỉ số mảng và giải tham chiếu con trỏ: `arr[i] == *(arr + i)`.
- Phân biệt chính xác giữa Mảng con trỏ (`int *p[3]`) và Con trỏ trỏ mảng (`int (*p)[3]`).

## 핵심 키워드 (Từ khóa)
- **배열명 = 시작 주소 (Array Name as Base Address)**: `arr == &arr[0]`.
- **포인터 연산 (Pointer Arithmetic)**: `p + 1` tăng địa chỉ thêm `sizeof(T)` bytes.
- **문법적 동치 (Equivalence)**: `*(arr + i) == arr[i]`.
- **포인터 배열 vs 배열 포인터**: `int *p[3]` (mảng 3 con trỏ) vs `int (*p)[3]` (con trỏ trỏ mảng 3 phần tử).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [41-bai-hoc.md](41-bai-hoc.md) (Khái niệm mảng 1 chiều và 2 chiều).
- Liên kết với [43-bai-hoc.md](43-bai-hoc.md) (Toán tử con trỏ `&` và `*`).
- Liên kết với [04-programming-language/73-bai-hoc.md](../../04-programming-language/lessons/73-bai-hoc.md) (Bộ nhớ Heap và con trỏ).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý chuyển đổi qua lại:
  - Biểu thức `*(p + 2)` hoàn toàn tương đương với `p[2]`.
  - Biểu thức `*p + 2` mang nghĩa lấy giá trị tại `*p` rồi cộng thêm số 2 (khác với `*(p + 2)`).
  - Tên mảng là một **hằng con trỏ (Constant Pointer)**: Không được phép thực hiện phép gán thay đổi địa chỉ của tên mảng (ví dụ: `arr++` hay `arr = p` là **LỖI BIÊN DỊCH**), nhưng với biến con trỏ thì được (`p++` là hợp lệ).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mối quan hệ giữa Tên mảng và Con trỏ
- Trong C, tên mảng hoạt động như một hằng con trỏ trỏ tới phần tử thứ 0 của mảng:
  $$\text{arr} \equiv \&\text{arr}[0]$$
- Do đó, ta có thể gán tên mảng trực tiếp cho một biến con trỏ mà không cần dùng toán tử `&`:
  ```c
  int a[5] = {10, 20, 30, 40, 50};
  int *p = a; // Hoàn toàn tương đương với: int *p = &a[0];
  ```

#### 2. Nguyên lý Số học Con trỏ (Pointer Arithmetic)
- Khi thực hiện phép cộng hoặc trừ một số nguyên $i$ với con trỏ:
  $$\text{Địa chỉ mới} = \text{Địa chỉ hiện tại} \pm (i \times \text{sizeof}(\text{kiểu dữ liệu}))$$
- *Bảng minh họa bước nhảy địa chỉ trên RAM*:
  | Khai báo con trỏ | Giá trị `p` ban đầu | Biểu thức `p + 1` | Bước nhảy byte thực tế |
  | :--- | :--- | :--- | :--- |
  | `char *p;` | `1000` | `1001` | $+1$ byte (`sizeof(char)`) |
  | `int *p;` | `1000` | `1004` | $+4$ bytes (`sizeof(int)`) |
  | `double *p;` | `1000` | `1008` | $+8$ bytes (`sizeof(double)`) |

#### 3. Bảng công thức tương đương cú pháp
| Thao tác | Cú pháp chỉ số mảng | Cú pháp số học con trỏ |
| :--- | :--- | :--- |
| **Giá trị phần tử thứ 0** | `arr[0]` | `*arr` hoặc `*(arr + 0)` |
| **Giá trị phần tử thứ $i$** | `arr[i]` | `*(arr + i)` hoặc `*(p + i)` hoặc `p[i]` |
| **Địa chỉ phần tử thứ $i$** | `&arr[i]` | `arr + i` hoặc `p + i` |
| **Giá trị phần tử tiếp theo** | `arr[i+1]` | `*(p + i + 1)` |

#### 4. Phân biệt Mảng con trỏ vs Con trỏ trỏ mảng
- **Mảng con trỏ (Array of Pointers)**:
  - Cú pháp: `int *arr[3];`
  - Ý nghĩa: `[]` có độ ưu tiên cao hơn `*`. Đây là một **mảng gồm 3 phần tử**, mỗi phần tử là một biến con trỏ kiểu `int*`.
- **Con trỏ trỏ mảng (Pointer to an Array)**:
  - Cú pháp: `int (*arr)[3];`
  - Ý nghĩa: Dấu ngoặc đơn `()` ép độ ưu tiên cho `*`. Đây là một **biến con trỏ duy nhất** trỏ tới một mảng gồm 3 số nguyên `int` (thường dùng để trỏ hàng trong mảng 2 chiều).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán lần vết đề thi Kỹ sư xử lý thông tin
```c
#include <stdio.h>
int main() {
    int a[5] = {10, 11, 12, 13, 14};
    int *p = a;

    printf("%d\n", *(p + 1));  // In ra: 11 (giá trị phần tử a[1])
    printf("%d\n", *p + 1);    // In ra: 11 (*p là 10, cộng thêm 1)

    p = p + 2;                 // Con trỏ p dịch sang phần tử a[2]
    printf("%d\n", *p);        // In ra: 12
    printf("%d\n", p[1]);      // In ra: 13 (tương đương *(p + 1) -> a[3])
    return 0;
}
```

#### 2. Cơ chế duyệt mảng 2 chiều bằng con trỏ
- Với mảng `int a[2][3] = {{1, 2, 3}, {4, 5, 6}};`:
  - `a` là địa chỉ hàng 0: `a == &a[0]`.
  - `*a` là địa chỉ phần tử đầu tiên của hàng 0: `*a == &a[0][0]`.
  - `*(*(a + i) + j)` chính là giá trị của phần tử `a[i][j]`.

---

### 복습 체크리스트
- [ ] Tại sao câu lệnh `arr++` (với `int arr[5];`) lại gây ra lỗi biên dịch trong khi `p++` (với `int *p = arr;`) thì hợp lệ?
- [ ] Nếu con trỏ kiểu `int *` đang có giá trị địa chỉ `2000`, sau lệnh `p = p + 3;` thì địa chỉ mới của nó là bao nhiêu?
- [ ] Phân biệt sự khác biệt hoàn toàn về ý nghĩa giữa biểu thức `*(p + 1)` và `*p + 1`?
- [ ] Cú pháp `int *p[4]` và `int (*p)[4]` khác nhau về bản chất như thế nào?
