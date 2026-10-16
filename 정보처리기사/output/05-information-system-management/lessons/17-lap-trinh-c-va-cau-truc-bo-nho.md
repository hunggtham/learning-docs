# Chuyên đề 17: Lập trình C, Con trỏ và Cấu trúc Bộ nhớ (C 언어, 포인터 및 메모리 구조)

## 학습 목표 (Mục tiêu học tập)
- Phân loại toàn diện các thế hệ và mô hình ngôn ngữ lập trình (절차적, 객체지향, 스크립트, 선언형) và đặc trưng cốt lõi của từng ngôn ngữ đại diện.
- Làm chủ cơ chế rẽ nhánh và điều khiển luồng thực thi với câu lệnh `break` và `continue`, tránh bẫy lặp vô tận và lần vết mã nguồn (trace code) chính xác.
- Hiểu thấu đáo bản chất cấu trúc lưu trữ của mảng (Array) 1 chiều, 2 chiều theo thứ tự hàng (Row-Major) và quy tắc tự động điền số 0 trong C.
- Nắm vững cơ chế biểu diễn chuỗi ký tự kết thúc bằng byte rỗng `\0` (Null-terminated string), phân biệt chính xác `sizeof` và `strlen`, cùng các hàm thư viện chuẩn `<string.h>`.
- Giải mã tường tận khái niệm con trỏ (Pointer), toán tử địa chỉ `&` và toán tử giải tham chiếu `*`, cùng mối liên hệ tương đương cú pháp kinh điển giữa mảng và con trỏ (`arr[i] == *(arr + i)`).
- Kết nối kiến thức bộ nhớ cấp thấp của C với các lỗ hổng an toàn phần mềm nghiêm trọng trong Môn 5 như tràn bộ đệm (Buffer Overflow), giải tham chiếu con trỏ rỗng (Null Pointer Dereference) và con trỏ lơ lửng (Dangling Pointer).

## 핵심 키워드 (Từ khóa cốt lõi)
- **언어 분류 (Language Classification)**: 절차적 (C, FORTRAN, COBOL), 객체지향 (Simula, Smalltalk, C++, Java), 스크립트 (Python, JS).
- **분기 제어 (Branch Control)**: `break` (thoát vòng lặp/switch ngay lập tức), `continue` (bỏ qua phần còn lại, nhảy tới bước lặp kế tiếp).
- **배열 (Array)**: 0-based Indexing, vùng nhớ liên tục, tự động điền 0 (`int a[5] = {1, 2}`).
- **널 문자 (Null Terminator `\0`)**: Ký tự kết thúc chuỗi (ASCII 0), chuỗi luôn tốn thêm 1 byte trong bộ nhớ.
- **포인터 (Pointer)**: `&` (Address-of - lấy địa chỉ), `*` (Dereference - giải tham chiếu lấy giá trị tại ô nhớ).
- **배열과 포인터 동치 (Array-Pointer Equivalence)**: `arr == &arr[0]`, `*(arr + i) == arr[i]`.
- **메모리 보안 취약점 (Memory Security Flaws)**: Buffer Overflow (tràn mảng), Dangling Pointer (con trỏ trỏ ô nhớ đã giải phóng).

## 선행·연결 개념 (Kiến thức liên kết)
- **Đi từ đâu (선행 개념)**: Tiếp thu từ [06-lo-hong-phan-mem-va-secure-coding.md](06-lo-hong-phan-mem-va-secure-coding.md) (Quy tắc lập trình an toàn và cơ chế bảo vệ bộ nhớ phần mềm) và [13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md](13-he-dieu-hanh-tien-trinh-va-dieu-phoi.md) (Không gian địa chỉ ảo và bộ nhớ tiến trình).
- **Đang giải quyết điều gì (핵심 해결)**: Cung cấp nền tảng lập trình cấu trúc cấp thấp bằng ngôn ngữ C, giúp kỹ sư hiểu thấu đáo kiến trúc bộ nhớ vật lý, cơ chế đánh địa chỉ và thao tác dữ liệu qua con trỏ.
- **Dùng để đi đâu (연결 개념)**: Làm cơ sở đọc hiểu mã nguồn kiểm tra an ninh trong kỳ thi Kỹ sư xử lý thông tin, chuẩn bị trực tiếp cho [18-lap-trinh-python-va-tu-dong-hoa.md](18-lap-trinh-python-va-tu-dong-hoa.md) (Lập trình kịch bản tự động hóa và quản trị hệ thống hiện đại).

## 읽는 방법 (Cách đọc & Khung tư duy)
- **Tư duy kiến trúc ô nhớ**: Ngôn ngữ C thao tác trực tiếp trên byte vật lý. Hãy luôn vẽ một dãy các ô chữ nhật liên tiếp để hình dung vị trí bộ nhớ, địa chỉ hex và giá trị lưu trữ bên trong mỗi khi phân tích mảng hay con trỏ.
- **Quy tắc phân biệt `*`**:
  - Đứng cạnh kiểu dữ liệu (`int *p;`): Đây là **khai báo** biến con trỏ.
  - Đứng trước biến trong biểu thức (`*p = 50;`): Đây là **toán tử giải tham chiếu** (lấy giá trị tại ô nhớ đang trỏ tới).
- **Quy tắc nhảy của `continue`**:
  - Trong `for(khởi tạo; điều kiện; tăng_giảm)`: Gặp `continue` $\rightarrow$ Nhảy ngay về bước **tăng_giảm** rồi mới kiểm tra điều kiện lặp.
  - Trong `while(điều kiện)`: Gặp `continue` $\rightarrow$ Nhảy thẳng về kiểm tra **điều kiện**. Nếu biến đếm đặt sau `continue`, vòng lặp sẽ bị kẹt vĩnh viễn (Infinite Loop)!

---

### TẦNG A – ghi chú NÉN (ÔN / ĐI THI)

### 1. Phân loại ngôn ngữ lập trình (프로그래밍 언어의 분류)

| Mô hình ngôn ngữ | Đặc trưng cốt lõi | Ngôn ngữ tiêu biểu & Điểm thi cần nhớ |
| :--- | :--- | :--- |
| **절차적 언어 (Procedural)** | Thực thi tuần tự theo dòng lệnh, chia nhỏ hàm/thủ tục, tốc độ cực nhanh, quản lý tài nguyên thủ công | • **FORTRAN**: Khoa học kỹ thuật, tính toán số học đầu tiên. • **COBOL**: Nghiệp vụ tài chính, cấu trúc văn bản 4 DIVISION. • **ALGOL**: Tổ phụ thuật toán của C và Pascal. • **C**: Phát triển hệ điều hành UNIX (Dennis Ritchie). |
| **객체지향 언어 (OOP)** | Mô hình hóa dữ liệu và hành vi thành Đối tượng (Object/Class), kế thừa, đóng gói, đa hình | • **Simula**: Ngôn ngữ đầu tiên đưa ra khái niệm Class/Object. • **Smalltalk**: Ngôn ngữ OOP thuần túy đầu tiên có giao diện GUI. • **C++**: Mở rộng từ C thêm tính năng OOP. • **Java**: Chạy trên máy ảo JVM (Write Once, Run Anywhere). |
| **스크립트 언어 (Scripting)** | Không cần biên dịch trước (thông dịch trực tiếp), cú pháp ngắn gọn, phát triển nhanh | • **Client-side**: JavaScript (thực thi trên trình duyệt). • **Server-side**: Python, PHP, Ruby (xử lý trên máy chủ). |
| **선언형 / AI 언어 (Declarative / AI)** | Khai báo "cần cái gì" thay vì "làm như thế nào", dựa trên logic toán học hoặc biểu thức hàm | • **LISP**: Xử lý danh sách bằng ngoặc tròn, nền tảng AI sơ khai. • **PROLOG**: Lập trình logic dựa trên tập luật và suy diễn. |

---

### 2. Phân nhánh điều khiển: `break` và `continue`

| Tiêu chí | `break` (Ngắt luồng) | `continue` (Bỏ qua lần lặp) |
| :--- | :--- | :--- |
| **Hành vi thực thi** | Thoát vĩnh viễn khỏi cấu trúc lặp hoặc khối lệnh bao bọc | Bỏ qua các câu lệnh còn lại trong thân vòng lặp của lần hiện tại, tiến hành bước lặp kế tiếp |
| **Phạm vi hỗ trợ** | Vòng lặp (`for`, `while`, `do-while`) và rẽ nhánh `switch-case` | **Chỉ dùng trong vòng lặp**, không được phép dùng trong `switch-case` độc lập |
| **Trong vòng `for`** | Nhảy ra ngoài dấu ngoặc nhọn kết thúc vòng `for` | Nhảy tới biểu thức **tăng/giảm** (Update expression) |
| **Trong vòng `while`** | Nhảy ra ngoài dấu ngoặc nhọn kết thúc vòng `while` | Nhảy thẳng về biểu thức **kiểm tra điều kiện** (Condition) |
| **Vòng lặp lồng nhau** | Chỉ phá vỡ **1 tầng lặp gần nhất** chứa câu lệnh `break` | Chỉ bỏ qua lần lặp của **1 tầng lặp gần nhất** chứa lệnh `continue` |

---

### 3. Cấu trúc mảng (배열 - Array)

#### Khái niệm & Quy tắc bộ nhớ
- **Bản chất**: Tập hợp các phần tử có **cùng kiểu dữ liệu**, được cấp phát trên một **vùng nhớ vật lý liên tục** (Contiguous memory).
- **Chỉ số 0-based**: Đánh số từ $0$ đến $N - 1$.
- **Truy xuất ngẫu nhiên $O(1)$**: Địa chỉ phần tử thứ $i$ được tính bằng:
  $$\text{Address}(arr[i]) = \text{Base\_Address} + i \times \text{sizeof(Type)}$$

#### Quy tắc khởi tạo mảng 1 chiều & Mảng 2 chiều
- **Tự động điền 0 (Auto Zero-Fill)**: Khi khai báo kích thước lớn hơn số lượng phần tử khởi tạo, các phần tử còn lại tự động mang giá trị 0.
  - Ví dụ: `int a[5] = {1, 2};` $\rightarrow$ Các phần tử là `a[0]=1, a[1]=2, a[2]=0, a[3]=0, a[4]=0`. (Không phải giá trị rác!).
- **Mảng 2 chiều theo thứ tự hàng (Row-Major Order)**: Lưu hết các cột của hàng 0 rồi mới sang hàng 1.
- **Quy tắc bỏ trống kích thước (Omission Rule)**:
  - Cho phép bỏ trống kích thước hàng (dòng đầu tiên): `int a[][3] = {{1, 2}, {3, 4, 5}};` $\rightarrow$ Hợp lệ! Trình biên dịch tự tính là 2 hàng.
  - Cấm tuyệt đối bỏ trống kích thước cột: `int a[2][] = ...;` $\rightarrow$ **LỖI BIÊN DỊCH (Compilation Error)**.

---

### 4. Mảng ký tự và Chuỗi trong C (문자열)

#### Bản chất chuỗi kết thúc bằng Null (`\0`)
- Trong C không có kiểu dữ liệu nguyên thủy `string`. Chuỗi được biểu diễn bằng một mảng các ký tự kiểu `char` kết thúc bằng ký tự đặc biệt **Null Terminator (`\0`)** có mã ASCII bằng 0.
- **Quy tắc kích thước**: Kích thước bộ nhớ lưu chuỗi luôn bằng:
  $$\text{Memory Size} = \text{Độ dài chuỗi hiển thị} + 1 \text{ byte (chứa } \backslash 0 \text{)}$$
  - Ví dụ: Chuỗi `"KOREA"` có độ dài 5 ký tự nhưng chiếm **6 bytes** trong bộ nhớ.
  - Hằng ký tự đơn `'A'` (1 byte) hoàn toàn khác hằng chuỗi `"A"` (2 bytes: `'A'` và `'\0'`).

#### Phân biệt `sizeof` và `strlen`

| Tiêu chí | Toán tử `sizeof` | Hàm thư viện `strlen` (`<string.h>`) |
| :--- | :--- | :--- |
| **Bản chất** | Toán tử cấp ngôn ngữ, tính kích thước vùng nhớ được cấp phát | Hàm duyệt chuỗi đếm số ký tự thực tế cho đến khi gặp `\0` |
| **Thời điểm tính** | Tính toán tại thời điểm biên dịch (Compile-time) | Thực thi duyệt bộ nhớ tại thời điểm chạy (Runtime) |
| **Ký tự `\0`** | **Tính cả byte `\0`** (và toàn bộ kích thước mảng cấp phát) | **Không tính byte `\0`** |
| **Ví dụ: `char s[10] = "Hi";`** | `sizeof(s)` trả về **10** bytes | `strlen(s)` trả về **2** |

#### Bảng hàm thao tác chuỗi chuẩn `<string.h>`

| Tên hàm | Cú pháp | Công dụng & Nguy cơ bảo mật |
| :--- | :--- | :--- |
| `strlen(s)` | `size_t strlen(const char *s)` | Đếm độ dài chuỗi ký tự (không tính `\0`) |
| `strcpy(dest, src)` | `char *strcpy(char *dest, const char *src)` | Sao chép chuỗi `src` vào `dest`. **Cực kỳ nguy hiểm** (gây Buffer Overflow do không kiểm tra kích thước `dest`) |
| `strcat(dest, src)` | `char *strcat(char *dest, const char *src)` | Nối chuỗi `src` vào đuôi chuỗi `dest`. **Dễ gây tràn bộ đệm** |
| `strcmp(s1, s2)` | `int strcmp(const char *s1, const char *s2)` | So sánh thứ tự từ điển: trả về $0$ nếu bằng nhau, âm nếu $s1 < s2$, dương nếu $s1 > s2$ |
| `strncpy` / `strncat` | Thêm tham số kích thước `n` | **Hàm an toàn** trong Secure Coding, chặn đứng nguy cơ tràn bộ đệm |

---

### 5. Con trỏ (포인터 - Pointer) và Số học con trỏ

#### Khái niệm & Kích thước con trỏ
- **Biến con trỏ (Pointer Variable)**: Là biến dùng để chứa **địa chỉ ô nhớ** của một biến khác trong RAM.
- **Toán tử địa chỉ `&`**: Lấy địa chỉ ô nhớ của một biến (Address-of operator).
- **Toán tử giải tham chiếu `*`**: Truy xuất giá trị nằm tại địa chỉ ô nhớ mà con trỏ đang trỏ tới (Dereference operator).
- **Kích thước biến con trỏ**: Kích thước biến con trỏ chỉ phụ thuộc vào kiến trúc CPU, hoàn toàn không phụ thuộc vào kiểu dữ liệu nó trỏ tới:
  - Hệ điều hành **32-bit**: Kích thước con trỏ luôn là **4 bytes** (dải địa chỉ $2^{32}$).
  - Hệ điều hành **64-bit**: Kích thước con trỏ luôn là **8 bytes** (dải địa chỉ $2^{64}$).

#### Mối quan hệ tương đương giữa Mảng và Con trỏ
- **Tên mảng là một hằng con trỏ**: Tên của một mảng chính là địa chỉ của phần tử đầu tiên:
  $$arr \equiv \&arr[0]$$
- **Số học con trỏ (Pointer Arithmetic)**: Phép cộng `p + 1` không phải là tăng 1 byte địa chỉ, mà là tăng thêm `sizeof(*p)` bytes (kích thước một phần tử của kiểu dữ liệu con trỏ trỏ tới).
- **Quy tắc tương đương cú pháp**:
  $$arr[i] \equiv *(arr + i)$$
  $$\&arr[i] \equiv (arr + i)$$

---

### TẦNG B – ghi chú BỔ SUNG (HIỂU SÂU)

### 1. Phân tích luồng thực thi Trace Code với `break` và `continue`

Hãy phân tích bài toán thực tế thường gặp trong các đề thi Kỹ sư xử lý thông tin:

```c
#include <stdio.h>

int main() {
    int sum = 0;
    for (int i = 1; i <= 5; i++) {
        if (i % 2 == 0) {
            continue; // Bỏ qua số chẵn
        }
        if (i > 3) {
            break;    // Dừng khi i lớn hơn 3
        }
        sum += i;
    }
    printf("sum = %d\n", sum);
    return 0;
}
```

**Bảng lần vết biến (Variable Trace Table):**

| Bước lặp (`i`) | `i % 2 == 0` | `i > 3` | Hành động thực thi | Giá trị `sum` sau bước |
| :---: | :---: | :---: | :--- | :---: |
| $i = 1$ | Sai (1 lẻ) | Sai | Thực hiện `sum += 1` | **1** |
| $i = 2$ | Đúng (2 chẵn) | Không xét | Gặp `continue` $\rightarrow$ Nhảy thẳng về bước $i++$ | 1 (giữ nguyên) |
| $i = 3$ | Sai (3 lẻ) | Sai | Thực hiện `sum += 3` | **4** |
| $i = 4$ | Đúng (4 chẵn) | Không xét | Gặp `continue` $\rightarrow$ Nhảy thẳng về bước $i++$ | 4 (giữ nguyên) |
| $i = 5$ | Sai (5 lẻ) | Đúng ($5 > 3$) | Gặp `break` $\rightarrow$ Thoát ngay khỏi vòng `for` | 4 (kết thúc) |

$\rightarrow$ Kết quả in ra màn hình: `sum = 4`.

> [!WARNING] Cảnh báo bẫy lặp vô tận trong vòng lặp `while`
> Nếu chuyển đoạn mã trên sang vòng lặp `while` và đặt câu lệnh tăng biến đếm `i++` ở cuối thân vòng lặp:
> ```c
> int i = 1, sum = 0;
> while (i <= 5) {
>     if (i % 2 == 0) continue; // Khi i = 2, continue nhảy về kiểm tra (i <= 5), i không bao giờ tăng!
>     sum += i;
>     i++;
> }
> ```
> Chương trình sẽ rơi vào **vòng lặp vô tận (Infinite Loop)** ngay tại $i = 2$, làm cạn kiệt tài nguyên CPU của hệ thống.

---

### 2. Cấu trúc bộ nhớ của Chuỗi và Con trỏ: `char[]` vs `char *`

Hiểu thấu bản chất phân bố vùng nhớ giữa mảng ký tự và con trỏ hằng chuỗi là chìa khóa để phân tích an ninh phần mềm:

```c
char arr[] = "hello"; // Cách 1: Mảng ký tự trên Stack
char *ptr  = "hello"; // Cách 2: Con trỏ trỏ tới chuỗi trong phân vùng Text/Literal
```

```
[Phân vùng Bộ nhớ Tiến trình]
─────────────────────────────────────────────────────────────────────────────
1. Read-Only Data Segment (Phân vùng Text/Chỉ đọc):
   Địa chỉ: 0x00400000 ──> [ 'h' | 'e' | 'l' | 'l' | 'o' | '\0' ]
                              ▲
                              │ Trỏ tới địa chỉ chỉ đọc
2. Stack Segment:             │
   Địa chỉ: 0x7FFF0008 ───────┴──> ptr (Chứa địa chỉ 0x00400000)
   Địa chỉ: 0x7FFF0000 ──> arr   [ 'h' | 'e' | 'l' | 'l' | 'o' | '\0' ] (Cấp phát trên Stack)
─────────────────────────────────────────────────────────────────────────────
```

- **Hành vi sửa đổi dữ liệu**:
  - `arr[0] = 'H';` $\rightarrow$ **Hợp lệ!** Dữ liệu chuỗi nằm trong Stack Frame của hàm, cho phép ghi sửa tùy ý (`"Hello"`).
  - `ptr[0] = 'H';` $\rightarrow$ **LỖI PHẦN CỨNG (Segmentation Fault - SIGSEGV)!** Bộ nhớ Literal thuộc vùng Read-Only, hệ điều hành sẽ chặn thao tác ghi và hủy tiến trình lập tức để bảo vệ hệ thống.

---

### 3. Phân biệt Mảng con trỏ (`*p[]`) và Con trỏ mảng (`(*p)[]`)

Đây là câu hỏi phân loại ứng viên thường xuyên xuất hiện trong phần thi đọc hiểu mã nguồn C:

| Cú pháp | Tên gọi chuẩn | Bản chất cấu trúc | Ví dụ ứng dụng thực tế |
| :--- | :--- | :--- | :--- |
| `int *p[3];` | **Mảng con trỏ** (포인터 배열 - Array of Pointers) | Một mảng gồm 3 phần tử, mỗi phần tử là một biến con trỏ kiểu `int *` | Quản lý danh sách các chuỗi ký tự có độ dài biến thiên (Ragged Array) |
| `int (*p)[3];` | **Con trỏ trỏ mảng** (배열 포인터 - Pointer to an Array) | Một biến con trỏ duy nhất, trỏ tới một mảng 1 chiều chứa 3 số nguyên | Dùng làm tham số con trỏ duyệt mảng 2 chiều có số cột cố định bằng 3 |

**Quy tắc ưu tiên toán tử**: Dấu ngoặc vuông `[]` có độ ưu tiên cao hơn dấu sao `*`.
- Trong `int *p[3]`, `p` kết hợp với `[3]` trước tạo thành mảng 3 phần tử, sau đó mới kết hợp với `*` tạo thành mảng các con trỏ.
- Trong `int (*p)[3]`, dấu ngoặc đơn `()` ép `*` kết hợp với `p` trước, biến `p` thành một biến con trỏ trỏ tới mảng 3 phần tử.

---

### 4. Từ Cấp thấp đến An ninh Hệ thống: Các lỗ hổng bộ nhớ kinh điển

Hiểu sâu ngôn ngữ C chính là hiểu nguồn gốc gốc rễ của các cuộc tấn công mạng trong Môn 5:

```
[Bản chất lỗi bộ nhớ C] ──────> [Kỹ thuật khai thác tấn công] ──────> [Giải pháp Secure Coding]
1. Không kiểm tra biên mảng ──> Buffer Overflow (Ghi đè EIP/RIP) ──> Dùng strncpy, fgets, Stack Canary
2. Con trỏ rỗng (NULL)     ──> Denial of Service (Crash hệ thống) ──> Luôn kiểm tra if (p != NULL)
3. Giải phóng ô nhớ sai     ──> Use-After-Free / Dangling Pointer ──> Gán p = NULL sau khi free(p)
```

1. **Tràn bộ đệm (Buffer Overflow / 버퍼 오버플로우)**:
   - Vì C ưu tiên hiệu năng tối đa nên không có cơ chế tự động kiểm tra biên (Boundary Check) khi truy xuất chỉ số mảng. Khi một hàm như `strcpy(dest, src)` hoặc `gets(buffer)` ghi dữ liệu vượt quá kích thước được cấp phát trên Stack, dữ liệu dư thừa sẽ tràn qua biến lân cận và **ghi đè lên Địa chỉ trả về (Return Address / EIP)** của hàm, cho phép tin tặc chuyển hướng luồng thực thi sang shellcode độc hại.
2. **Giải tham chiếu con trỏ rỗng (Null Pointer Dereference)**:
   - Khi hàm cấp phát bộ nhớ `malloc()` thất bại (do cạn kiệt RAM), nó trả về địa chỉ `NULL` (0x0). Nếu chương trình không kiểm tra mà lập tức thực hiện `*p = 100`, CPU sẽ kích hoạt ngắt phần cứng hủy tiến trình, tạo điều kiện cho các cuộc tấn công từ chối dịch vụ (DoS).
3. **Con trỏ lơ lửng (Dangling Pointer) & Sử dụng sau khi giải phóng (Use-After-Free)**:
   - Khi bộ nhớ Heap được giải phóng bằng lệnh `free(p)`, ô nhớ đó được trả về cho hệ điều hành hoặc trình quản lý bộ nhớ tái cấp phát cho mục đích khác. Nếu lập trình viên không gán `p = NULL`, biến con trỏ `p` vẫn giữ địa chỉ cũ. Việc truy xuất hoặc ghi đè qua `p` sau đó sẽ làm hỏng dữ liệu của đối tượng khác hoặc dẫn đến chiếm đoạt quyền điều khiển tiến trình.

---

### 복습 체크리스트
- [ ] Tôi có thể phân biệt ngay lập tức hành vi của `break` (thoát lặp) và `continue` (nhảy tới bước lặp kế tiếp)?
- [ ] Tôi có hiểu rõ quy tắc nhảy của `continue` trong vòng `for` (nhảy tới tăng/giảm) so với vòng `while` (nhảy tới điều kiện lặp)?
- [ ] Tôi có nhớ mảng trong C luôn đánh chỉ số từ 0 và các phần tử chưa gán sẽ tự động nhận giá trị 0 khi khởi tạo một phần?
- [ ] Tôi có thể giải thích tại sao mảng 2 chiều được phép bỏ trống kích thước hàng nhưng bắt buộc phải có kích thước cột?
- [ ] Tôi có giải thích được sự khác nhau giữa `sizeof("Hi")` (3 bytes) và `strlen("Hi")` (2 bytes)?
- [ ] Tôi có phân biệt được cơ chế vùng nhớ giữa `char str[] = "abc";` (Stack, sửa được) và `char *p = "abc";` (Read-only, cấm sửa)?
- [ ] Tôi có thuộc lòng công thức tương đương cú pháp `arr[i] == *(arr + i)` và `arr == &arr[0]`?
- [ ] Tôi có phân biệt được cú pháp mảng con trỏ `int *p[3]` và con trỏ trỏ mảng `int (*p)[3]`?
- [ ] Tôi có liên kết được việc C không kiểm tra biên mảng với lỗ hổng tràn bộ đệm (Buffer Overflow) trong an toàn hệ thống?
