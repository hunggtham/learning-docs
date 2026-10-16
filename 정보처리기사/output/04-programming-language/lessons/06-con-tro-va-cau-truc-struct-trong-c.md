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

#### 1. Lần vết chi tiết con trỏ và phép toán số học con trỏ trong C:
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

#### 2. Minh họa Cấu trúc Struct và truy xuất con trỏ (`.` vs `->`):
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

#### 3. Bảng lần vết bài toán con trỏ cấp hai (Double Pointer `**pp`):
```c
#include <stdio.h>

int main() {
    int a = 100;
    int *p = &a;    // p lưu địa chỉ của a
    int **pp = &p;  // pp lưu địa chỉ của p

    printf("a = %d\n", a);      // 100
    printf("*p = %d\n", *p);    // Giải tham chiếu cấp 1 -> 100
    printf("**pp = %d\n", **pp);// Giải tham chiếu cấp 2 -> 100

    **pp = 200; // Sửa giá trị của a thông qua con trỏ kép
    printf("a sau khi sua = %d\n", a); // In ra: 200
    return 0;
}
```

*Sơ đồ ánh xạ bộ nhớ:*
$$\text{pp (Địa chỉ 0x3000)} \xrightarrow{\text{trỏ tới}} \text{p (Địa chỉ 0x2000)} \xrightarrow{\text{trỏ tới}} \text{a (Địa chỉ 0x1000, Giá trị: 200)}$$

---

### 복습 체크리스트
- [ ] Ghi nhớ kích thước con trỏ: Luôn cố định 4 Byte (32-bit) hoặc 8 Byte (64-bit).
- [ ] Nắm chắc ý nghĩa toán tử: `&` lấy địa chỉ ô nhớ, `*` lấy giá trị tại địa chỉ ô nhớ.
- [ ] Hiểu phép toán con trỏ: `p + k` tăng địa chỉ thêm $k \times \text{sizeof}(*p)$.
- [ ] Phân biệt được: `int *p[3]` là mảng các con trỏ, còn `int (*p)[3]` là con trỏ trỏ tới mảng.
- [ ] Nắm vững đặc trưng struct: Gom nhóm các phần tử có kiểu dữ liệu khác nhau (dị nhất).
- [ ] Thuộc quy tắc toán tử: Biến struct dùng dấu chấm `.`, con trỏ struct dùng mũi tên `->`.
