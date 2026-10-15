# 핵심 262: 포인터와 포인터 변수 (Pointer)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm con trỏ (Pointer) và bản chất của việc lưu trữ địa chỉ ô nhớ trong kiến trúc máy tính.
- Phân biệt chính xác cú pháp và ý nghĩa của hai toán tử cốt lõi: Toán tử lấy địa chỉ `&` và toán tử giải tham chiếu `*`.
- Hiểu rõ cơ chế thao tác dữ liệu gián tiếp qua con trỏ và cách thay đổi giá trị của biến gốc thông qua con trỏ.
- Nắm bắt quy tắc kích thước biến con trỏ trên hệ điều hành 32-bit (4 bytes) và 64-bit (8 bytes).

## 핵심 키워드 (Từ khóa)
- **포인터 변수 (Pointer Variable)**: Biến chứa địa chỉ ô nhớ của biến khác.
- **주소 연산자 `&` (Address-of)**: Lấy địa chỉ ô nhớ vật lý của một biến.
- **역참조 연산자 `*` (Dereference)**: Truy xuất hoặc ghi đè giá trị tại ô nhớ mà con trỏ đang trỏ tới.
- **포인터 크기 (Pointer Size)**: Cố định theo kiến trúc CPU (32-bit là 4 bytes, 64-bit là 8 bytes).
- **Mẹo ghi nhớ**: `&` = **Address** (Địa chỉ), `*` = **Value** (Giá trị tại ô nhớ).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [42-bai-hoc.md](42-bai-hoc.md) (Mảng chuỗi và con trỏ chuỗi trong C).
- Liên kết với [44-bai-hoc.md](44-bai-hoc.md) (Mối liên hệ giữa Con trỏ và Mảng).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Lỗ hổng Dangling Pointer và Null Pointer Dereference).

## 읽는 방법 (Cách đọc)
- Phân biệt vai trò của dấu `*` theo ngữ cảnh:
  - Khi đứng cạnh kiểu dữ liệu (`int *p;`): Đóng vai trò là **khai báo** biến con trỏ.
  - Khi đứng trước tên con trỏ trong câu lệnh (`*p = 100;` hoặc `printf("%d", *p);`): Đóng vai trò là **toán tử giải tham chiếu** (lấy giá trị trong ô nhớ).
- `p` là **Địa chỉ**, `*p` là **Giá trị** chứa tại địa chỉ đó.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Khái niệm và Toán tử con trỏ
| Toán tử | Tên gọi kỹ thuật | Ý nghĩa hành động | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| **`&`** | **주소 연산자 / (Address-of Operator)** | Trả về địa chỉ ô nhớ mà biến đang chiếm giữ trên RAM | `int a = 10;` / `int *p = &a;` // Gán địa chỉ của `a` cho `p` |
| **`*`** | **역참조 연산자 / (Dereference Operator)** | Truy cập trực tiếp vào giá trị lưu tại địa chỉ mà con trỏ đang chỉ đến | `*p = 50;` // Đổi giá trị của biến `a` thành 50 thông qua `p` |

#### 2. Ví dụ luồng thực thi con trỏ trong đề thi
```c
#include <stdio.h>
int main() {
    int a = 50;
    int *p;         // Khai báo biến con trỏ p trỏ tới kiểu int
    p = &a;         // Con trỏ p lưu địa chỉ ô nhớ của biến a

    *p = 70;        // Gán 70 vào ô nhớ mà p đang trỏ tới (tức là biến a)
    printf("a = %d, *p = %d\n", a, *p); // In ra: a = 70, *p = 70
    return 0;
}
```

#### 3. Kích thước biến con trỏ trong bộ nhớ
- Kích thước của một biến con trỏ **không phụ thuộc vào kiểu dữ liệu mà nó trỏ tới**, mà chỉ phụ thuộc vào độ rộng bus địa chỉ của kiến trúc vi xử lý và hệ điều hành:
  - Trên hệ thống **32-bit (x86)**: Mọi biến con trỏ đều có kích thước là **4 bytes** (`sizeof(char*) == sizeof(int*) == sizeof(double*) == 4`).
  - Trên hệ thống **64-bit (x64)**: Mọi biến con trỏ đều có kích thước là **8 bytes** (`sizeof(char*) == sizeof(int*) == sizeof(double*) == 8`).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ minh họa bộ nhớ của biến và con trỏ
```
Địa chỉ ô nhớ:       0x1000                     0x2000
                ┌──────────────┐           ┌──────────────┐
Biến:           │   Giá trị:   │           │   Giá trị:   │
                │      70      │ ◄──────── │    0x1000    │
                └──────────────┘           └──────────────┘
Tên biến:            int a                     int *p
               (Địa chỉ &a = 0x1000)      (Địa chỉ &p = 0x2000)
```
- Khi thực thi lệnh `*p = 70;`: CPU nhìn vào giá trị bên trong biến `p` (là `0x1000`), sau đó nhảy tới ô nhớ `0x1000` và ghi đè giá trị `70` vào đó. Kết quả là biến `a` bị đổi giá trị gián tiếp.

#### 2. Con trỏ hai cấp (Double Pointer)
- Con trỏ trỏ tới một con trỏ khác:
  ```c
  int a = 100;
  int *p = &a;     // p trỏ tới a
  int **q = &p;    // q trỏ tới p (con trỏ cấp 2)

  // Các cách truy xuất:
  // a == *p == **q == 100
  // &a == p == *q
  ```

---

### 복습 체크리스트
- [ ] Toán tử `&` và toán tử `*` trong C thực hiện nhiệm vụ khác nhau như thế nào?
- [ ] Khi chạy lệnh `*p = 20;` với `p = &x;`, giá trị của biến `x` sẽ trở thành bao nhiêu?
- [ ] Tại sao trên hệ điều hành 64-bit, cả `char*` và `double*` đều chiếm 8 bytes dung lượng bộ nhớ?
- [ ] Con trỏ cấp 2 (`int **q`) lưu trữ giá trị gì trong ô nhớ của nó?
