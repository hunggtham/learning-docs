# C언어 포인터 및 구조체 (Con trỏ & Cấu trúc Struct trong C)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất biến con trỏ (포인터 변수), kích thước cố định theo kiến trúc hệ thống (4 Byte trên 32-bit, 8 Byte trên 64-bit), và hai toán tử cốt lõi: toán tử địa chỉ `&` và toán tử giải tham chiếu `*`.
- Thành thạo các phép toán số học trên con trỏ và phân biệt chính xác cặp khái niệm kinh điển trong đề thi: Mảng con trỏ (`int *p[3]`) vs Con trỏ mảng (`int (*p)[3]`).
- Hiểu rõ bản chất kiểu cấu trúc `struct` trong C là tập hợp các dữ liệu dị nhất (Heterogeneous); sử dụng chuẩn xác toán tử truy xuất thành viên dấu chấm `.` (cho biến cấu trúc) và dấu mũi tên `->` (cho con trỏ cấu trúc).

## 핵심 키워드 (Từ khóa)
- 포인터 변수 (Pointer Variable) — Biến lưu trữ địa chỉ ô nhớ trong không gian RAM.
- 간접 참조 연산자 (Dereference Operator `*`) — Truy xuất giá trị tại địa chỉ ô nhớ được trỏ tới.
- 주소 연산자 (Address-of Operator `&`) — Lấy địa chỉ ô nhớ vật lý của một biến số.
- 포인터 배열 vs 배열 포인터 — Mảng chứa các con trỏ (`*p[]`) vs Con trỏ trỏ tới cả mảng (`(*p)[]`).
- C언어 구조체 (struct in C) — Kiểu dữ liệu tự định nghĩa tập hợp các phần tử khác kiểu (이질적 집합).
- 멤버 접근 연산자 (Member Access Operators) — Dấu chấm `.` cho biến thường, dấu mũi tên `->` cho con trỏ cấu trúc.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `01-bien-dinh-danh-va-kieu-du-lieu-c-java.md` (kích thước kiểu dữ liệu trong bộ nhớ) và `05-mang-va-chuoi-ky-tu-trong-c.md` (tên mảng là một hằng con trỏ).
- **Đang giải quyết gì (Current Problem):** Giải quyết chủ đề khó nhất và hay bị mất điểm nhất trong đề thi kỹ sư phần mềm: Thao tác trực tiếp trên vùng nhớ cấp thấp, biến động địa chỉ con trỏ và truy xuất dữ liệu struct lồng nhau.
- **Dùng đi đâu (Forward Handoff):** Mô hình struct và con trỏ chính là tiền đề tiến hóa trực tiếp lên khái niệm Lớp (Class), Thuộc tính và Đối tượng tham chiếu trong Lập trình hướng đối tượng Java ở bài `08-lap-trinh-huong-doi-tuong-java-oop.md`.

## 읽는 방법 (Cách đọc)
- **Toán tử `*` và `&`:**
  - Khi khai báo: `int *p;` $\rightarrow$ dấu `*` mang ý nghĩa khai báo biến con trỏ.
  - Khi thực thi: `*p` $\rightarrow$ dấu `*` mang ý nghĩa "giải tham chiếu", lấy giá trị bên trong ô nhớ mà `p` đang nắm giữ địa chỉ.
  - `&x` mang ý nghĩa "lấy địa chỉ ô nhớ của `x`".
- **Cặp ngoặc tròn phân biệt:**
  - `int *p[3]` (không có ngoặc bao `*p`): Do `[]` ưu tiên cao hơn `*`, đây là **Mảng gồm 3 con trỏ**.
  - `int (*p)[3]` (có ngoặc tròn bao `*p`): Dấu `*` đi với `p` trước, đây là **Một con trỏ trỏ tới mảng 3 phần tử**.
- **Toán tử `->`:** Cứ thấy con trỏ struct thì dùng mũi tên: `ptr->age` tương đương `(*ptr).age`.

---

## C언어 포인터 및 구조체

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `포인터 변수는 주소를 저장하며, 포인터 연산(p+1) 시 가리키는 자료형의 크기(sizeof)만큼 주소가 증가한다. 구조체는 서로 다른 자료형을 묶은 사용자 정의 자료형으로 일반 변수는 점(.), 포인터는 화살표(->) 연산자로 멤버에 접근한다.`
  - [Tiếng Việt]: Biến con trỏ lưu trữ địa chỉ ô nhớ; khi thực hiện phép toán con trỏ (p+1), địa chỉ sẽ tăng lên một lượng đúng bằng kích thước (sizeof) của kiểu dữ liệu mà nó trỏ tới. Struct là kiểu dữ liệu gom nhóm các phần tử khác kiểu; biến thường truy xuất bằng dấu chấm (.), con trỏ struct truy xuất bằng dấu mũi tên (->).

- **1. Bảng đối chiếu hai toán tử con trỏ cốt lõi:**

| Toán tử | Tên gọi chuẩn | Cú pháp mẫu | Bản chất hành động trên bộ nhớ |
| :---: | :--- | :--- | :--- |
| **`&`** | **Toán tử địa chỉ** (Address-of) | `p = &a;` | Lấy địa chỉ ô nhớ nơi biến `a` đang cư trú và nạp vào con trỏ `p`. |
| **`*`** | **Toán tử giải tham chiếu** (Dereference) | `val = *p;` | Tìm đến ô nhớ do `p` chỉ tới và trích xuất giá trị chứa bên trong. |

- **2. Bảng phân biệt: Mảng con trỏ vs Con trỏ mảng:**

| Cú pháp khai báo | Tên gọi chuẩn Hàn/Anh | Bản chất cấu trúc bộ nhớ | Minh họa trực quan |
| :--- | :--- | :--- | :--- |
| **`int *p[3];`** | **포인터 배열** (Array of Pointers) | Một **Mảng gồm 3 phần tử**, trong đó mỗi phần tử là một con trỏ trỏ tới số nguyên. | Có 3 biến con trỏ độc lập: `p[0]`, `p[1]`, `p[2]`. |
| **`int (*p)[3];`** | **배열 포인터** (Pointer to an Array) | **Duy nhất 1 con trỏ**, được dùng để trỏ tới một mảng nguyên có đúng 3 phần tử. | `p` lưu địa chỉ của một hàng gồm 3 số nguyên. |

- **3. Đối chiếu Mảng (Array) vs Cấu trúc (Struct in C):**

| Tiêu chuẩn so sánh | Mảng (배열 - Array) | Cấu trúc (구조체 - Struct) |
| :--- | :--- | :--- |
| **Bản chất phần tử** | **Thuần nhất (Homogeneous):** Tất cả phần tử bắt buộc phải có cùng 1 kiểu dữ liệu. | **Dị nhất (Heterogeneous):** Cho phép gom nhóm nhiều kiểu dữ liệu khác nhau. |
| **Cách truy xuất phần tử**| Dùng chỉ số nguyên trong cặp ngoặc vuông: `arr[0]`, `arr[i]`. | Dùng tên định danh thành viên: `s.name`, `s.age` hoặc `ptr->name`. |
| **Từ khóa định nghĩa** | Khai báo trực tiếp: `int arr[10];` | Dùng từ khóa: `struct Student { ... };` |

- **주의/함정 (Bẫy đề thi):**
  - **Kích thước con trỏ:** Bất kể con trỏ trỏ tới kiểu 1 byte (`char*`) hay kiểu 8 byte (`double*`), bản thân biến con trỏ luôn có kích thước cố định là **4 Byte (hệ 32-bit)** hoặc **8 Byte (hệ 64-bit)** vì nó chỉ lưu một địa chỉ ô nhớ.
  - **Phép toán `p + 1`:** Nếu `p` là `int*` có địa chỉ là `1000`, thì `p + 1` sẽ có giá trị là `1004` (vì `int` chiếm 4 byte), không bao giờ là `1001`!
  - **Quên dấu ngoặc trong `(*p).age`:** Toán tử dấu chấm `.` có độ ưu tiên cao hơn dấu `*`, nên viết `*p.age` là sai cú pháp (trình biên dịch sẽ hiểu là `*(p.age)`). Do đó bắt buộc viết `(*p).age` hoặc dùng cú pháp ngắn gọn `p->age`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Con trỏ p cộng 1 tăng theo sizeof; biến struct chấm (.), con trỏ trỏ struct thì bắn mũi tên (->)."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ ô nhớ ASCII minh họa con trỏ `*ptr` và toán tử địa chỉ `&val`:

Khi khai báo biến số nguyên `int val = 42;` và con trỏ `int *ptr = &val;`, Hệ điều hành cấp phát các ô nhớ trong RAM như sau:

```text
+---------------+-------------------+------------------------+
| Tên biến      | Địa chỉ ô nhớ RAM | Giá trị lưu trong ô nhớ|
+---------------+-------------------+------------------------+
| val           | 0x1000 (4 Byte)   | 42                     |
+---------------+-------------------+------------------------+
        ^
        | trỏ tới (&val = 0x1000)
+---------------+-------------------+------------------------+
| ptr           | 0x2000 (4/8 Byte) | 0x1000                 |
+---------------+-------------------+------------------------+
```

Bảng giải nghĩa hành vi các toán tử trên ô nhớ:
- `val`: Giá trị nội dung của biến `val` $\rightarrow$ `42`.
- `&val`: Toán tử địa chỉ lấy nơi cư trú của `val` $\rightarrow$ `0x1000`.
- `ptr`: Giá trị chứa trong biến con trỏ `ptr` $\rightarrow$ `0x1000` (địa chỉ của `val`).
- `&ptr`: Địa chỉ ô nhớ của chính biến `ptr` trên Stack $\rightarrow$ `0x2000`.
- `*ptr`: Toán tử giải tham chiếu, tìm đến địa chỉ `0x1000` và đọc giá trị $\rightarrow$ `42`.

#### 2. Sơ đồ ô nhớ ASCII cho con trỏ cấp hai (Double Pointer `**pptr`):

Con trỏ cấp hai là biến con trỏ lưu trữ địa chỉ của một biến con trỏ khác:

```text
+---------------+-------------------+------------------------+
| Tên biến      | Địa chỉ ô nhớ RAM | Giá trị lưu trong ô nhớ|
+---------------+-------------------+------------------------+
| val           | 0x1000            | 100                    |
+---------------+-------------------+------------------------+
        ^
        | Giải tham chiếu cấp 1 (*ptr = val)
+---------------+-------------------+------------------------+
| ptr           | 0x2000            | 0x1000 (&val)          |
+---------------+-------------------+------------------------+
        ^
        | Giải tham chiếu cấp 2 (**pptr = *ptr = val)
+---------------+-------------------+------------------------+
| pptr          | 0x3000            | 0x2000 (&ptr)          |
+---------------+-------------------+------------------------+
```

Đoạn mã kiểm chứng và lần vết:
```c
#include <stdio.h>

int main() {
    int val = 100;
    int *ptr = &val;    // ptr lưu 0x1000
    int **pptr = &ptr;  // pptr lưu 0x2000

    printf("val = %d\n", val);         // 100
    printf("*ptr = %d\n", *ptr);       // 100 (đọc ô 0x1000)
    printf("**pptr = %d\n", **pptr);   // 100 (đọc ô 0x2000 -> đọc tiếp ô 0x1000)

    // Thao tác sửa dữ liệu qua con trỏ cấp 2
    **pptr = 200;
    printf("val sau khi **pptr = 200: %d\n", val); // In ra: 200
    return 0;
}
```

#### 3. Sơ đồ ô nhớ Mảng hai chiều và quan hệ đại số con trỏ trong C:

Khai báo: `int arr[2][3] = {{10, 20, 30}, {40, 50, 60}};`
Trong bộ nhớ vật lý, mảng hai chiều không lưu dạng ma trận lưới mà được trải phẳng liên tục theo thứ tự ưu tiên hàng (Row-Major Order):

```text
Địa chỉ RAM:  0x1000    0x1004    0x1008    0x100C    0x1010    0x1014
Phần tử:     arr[0][0] arr[0][1] arr[0][2] arr[1][0] arr[1][1] arr[1][2]
Giá trị:     [  10   ] [  20   ] [  30   ] [  40   ] [  50   ] [  60   ]
Phân hàng:   |-------- Hàng 0 (arr[0]) --------|-------- Hàng 1 (arr[1]) --------|
```

Quy tắc chuyển đổi đại số con trỏ chuẩn thi cử:
- `arr`: Địa chỉ bắt đầu của toàn mảng và cũng là địa chỉ hàng 0 (`0x1000`).
- `arr + 1`: Nhảy qua toàn bộ 1 hàng (gồm 3 số `int` = $3 \times 4 = 12$ Byte) $\rightarrow$ Địa chỉ hàng 1 là `0x100C`.
- `*(arr + i)`: Tương đương `arr[i]`, là địa chỉ của phần tử đầu tiên thuộc hàng $i$.
- `*(arr + i) + j`: Tương đương `&arr[i][j]`, là địa chỉ của phần tử tại hàng $i$, cột $j$.
- `*(*(arr + i) + j)`: Tương đương `arr[i][j]`, giải tham chiếu hai lần để lấy giá trị số nguyên tại hàng $i$, cột $j$.

#### 4. Đối chiếu cấu trúc ô nhớ: Mảng con trỏ vs Con trỏ mảng:

```text
[1] Mảng con trỏ: int *p[3]; (3 con trỏ riêng biệt)
    p[0] (0x2000) ----> [ Ô nhớ A: 10 ]
    p[1] (0x2004) ----> [ Ô nhớ B: 20 ]
    p[2] (0x2008) ----> [ Ô nhớ C: 30 ]
    * Kích thước mảng p: 3 con trỏ x 4 Byte = 12 Byte (trên hệ 32-bit).

[2] Con trỏ mảng: int (*p)[3]; (Duy nhất 1 biến con trỏ p)
    p (0x3000) ----> [ Mảng 3 int: {10, 20, 30} ] (0x1000 ~ 0x100B)
    * Phép toán p + 1: Tăng đúng 12 Byte (bước nhảy bằng cả kích thước mảng 3 int).
```

#### 5. Lần vết chi tiết con trỏ và phép toán số học con trỏ trong C:
```c
#include <stdio.h>

int main() {
    int arr[3] = {10, 20, 30};
    int *p = arr; // p trỏ tới phần tử đầu tiên arr[0]

    printf("Gia tri *p ban dau: %d\n", *p);       // In ra: 10
    printf("Gia tri *(p + 1): %d\n", *(p + 1));   // In ra: 20 (dịch 1 vị trí int = 4 byte)
    printf("Gia tri *(p + 2): %d\n", *(p + 2));   // In ra: 30

    // Phân biệt *p++ và (*p)++
    int val1 = *p++; // Lấy giá trị *p (10) gán cho val1, sau đó con trỏ p nhảy sang arr[1]
    printf("val1 = %d, gia tri tai vi tri moi *p = %d\n", val1, *p); // val1 = 10, *p = 20

    (*p)++; // Tăng giá trị của phần tử mà p đang trỏ tới (arr[1] tăng từ 20 lên 21)
    printf("arr[1] sau khi (*p)++: %d\n", arr[1]); // In ra: 21

    return 0;
}
```

#### 6. Minh họa Cấu trúc Struct và truy xuất con trỏ (`.` vs `->`):
```c
#include <stdio.h>
#include <string.h>

// Định nghĩa kiểu cấu trúc SinhVien
struct SinhVien {
    char name[20];
    int age;
    double score;
};

int main() {
    // Khởi tạo biến cấu trúc trực tiếp
    struct SinhVien sv1;
    strcpy(sv1.name, "Nguyen");
    sv1.age = 22;
    sv1.score = 8.5;

    // Truy xuất qua biến thường: DÙNG DẤU CHẤM (.)
    printf("SV1: %s, Tuoi: %d, Diem: %.1f\n", sv1.name, sv1.age, sv1.score);

    // Khai báo con trỏ cấu trúc trỏ tới sv1
    struct SinhVien *ptr = &sv1;

    // Truy xuất qua con trỏ: DÙNG MŨI TÊN (->)
    printf("Truy xuat qua con tro ptr->name: %s\n", ptr->name);
    printf("Tuong duong (*ptr).age: %d\n", (*ptr).age);

    // Thay đổi dữ liệu qua con trỏ
    ptr->score = 9.5;
    printf("Diem sv1 sau khi sua qua con tro: %.1f\n", sv1.score); // In ra: 9.5

    return 0;
}
```

---

### 복습 체크리스트
- [ ] Ghi nhớ kích thước con trỏ: Luôn cố định 4 Byte (32-bit) hoặc 8 Byte (64-bit).
- [ ] Nắm chắc ý nghĩa toán tử: `&` lấy địa chỉ ô nhớ, `*` lấy giá trị tại địa chỉ ô nhớ.
- [ ] Hiểu phép toán con trỏ: `p + k` tăng địa chỉ thêm $k \times \text{sizeof}(*p)$.
- [ ] Phân biệt được: `int *p[3]` là mảng các con trỏ, còn `int (*p)[3]` là con trỏ trỏ tới mảng.
- [ ] Nắm vững đặc trưng struct: Gom nhóm các phần tử có kiểu dữ liệu khác nhau (dị nhất).
- [ ] Thuộc quy tắc toán tử: Biến struct dùng dấu chấm `.`, con trỏ struct dùng mũi tên `->`.
