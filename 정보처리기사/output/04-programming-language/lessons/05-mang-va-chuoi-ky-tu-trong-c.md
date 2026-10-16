# 배열 및 문자열 (Mảng & Chuỗi ký tự trong C)

## 학습 목표 (Mục tiêu)
- Nắm vững nguyên lý cấp phát bộ nhớ liên tục của mảng 1 chiều và mảng 2 chiều trong ngôn ngữ C; áp dụng chính xác công thức tính địa chỉ ô nhớ theo thứ tự ưu tiên hàng (행 우선 순서 - Row-Major Order).
- Thấu hiểu bản chất chuỗi ký tự trong C là mảng `char` kết thúc bằng ký tự rỗng `\0` (Null Character, mã ASCII 0); phân biệt rõ giữa số ký tự thực tế và kích thước bộ nhớ cần cấp phát.
- Sử dụng thành thạo và lần vết chính xác kết quả của các hàm xử lý chuỗi kinh điển trong thư viện `<string.h>`: `strlen`, `strcpy`, `strcat`, `strcmp`.

## 핵심 키워드 (Từ khóa)
- 배열 (Array) — Cấu trúc dữ liệu thuần nhất (Homogeneous) lưu trữ liên tục trên bộ nhớ RAM.
- 2차원 배열 주소 계산 (2D Array Memory Calculation) — Thứ tự ưu tiên hàng: $\text{Base} + (i \times C + j) \times \text{Size}$.
- 널 문자 (Null Terminator `\0`) — Ký tự báo hiệu kết thúc chuỗi trong C (ASCII code 0).
- 문자열 함수 (String Functions in `<string.h>`) — `strlen`, `strcpy`, `strcat`, `strcmp`.
- 버퍼 오버플로우 위험 (Buffer Overflow Risk) — Ghi vượt quá độ dài mảng chuỗi làm hỏng bộ nhớ lân cận.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa các kiểu dữ liệu nguyên thủy từ `01-bien-dinh-danh-va-kieu-du-lieu-c-java.md` và các vòng lặp `for` từ `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md` để duyệt các phần tử trong mảng.
- **Đang giải quyết gì (Current Problem):** Giải quyết các câu hỏi tính toán địa chỉ bộ nhớ và lần vết chuỗi ký tự trong đề thi: Khi khai báo một mảng 2 chiều hoặc thực hiện nối chuỗi, các byte bộ nhớ được sắp đặt ra sao và ký tự `\0` đóng vai trò ranh giới như thế nào.
- **Dùng đi đâu (Forward Handoff):** Tên mảng trong C thực chất là một hằng con trỏ trỏ tới địa chỉ phần tử đầu tiên; kiến thức này sẽ trực tiếp chuyển giao sang bài học chuyên sâu về con trỏ `06-con-tro-va-cau-truc-struct-trong-c.md`.

## 읽는 방법 (Cách đọc)
- **Công thức tính địa chỉ mảng 2 chiều:** Đề thi hay hỏi địa chỉ ô nhớ của `arr[i][j]` khi mảng có kích thước $R \times C$. Nhớ ngay công thức: Lấy chỉ số hàng $i$ nhân với tổng số cột $C$, cộng với chỉ số cột $j$, rồi tất cả nhân với kích thước kiểu dữ liệu ($\text{Size}$).
- **Ký tự Null `\0`:** Khi đếm độ dài bằng `strlen()`, máy tính **không đếm ký tự `\0`**. Nhưng khi khai báo mảng để lưu chuỗi "HELLO" (5 chữ cái), mảng bắt buộc phải có kích thước tối thiểu là **6** (5 chữ cái + 1 byte cho `\0`).
- **`strcmp(s1, s2)`:** Nếu 2 chuỗi giống hệt nhau thì trả về **`0`**. Nếu $s1$ đứng trước $s2$ trong từ điển thì trả về số âm ($< 0$); ngược lại trả về số dương ($> 0$).

---

## 배열 및 문자열

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `2차원 배열은 행 우선(Row-Major) 방식으로 메모리에 연속 저장되며, C언어의 문자열은 끝에 반드시 널 문자('\0', ASCII 0)가 포함되어야 한다. strlen()은 널 문자를 제외한 순수 길이를 반환하고, strcmp()는 두 문자열이 같을 때 0을 반환한다.`
  - [Tiếng Việt]: Mảng 2 chiều được lưu liên tục trong RAM theo thứ tự ưu tiên hàng (Row-Major); chuỗi ký tự C bắt buộc phải kết thúc bằng ký tự null `\0` (ASCII 0). Hàm strlen trả về độ dài không tính null; hàm strcmp trả về 0 khi hai chuỗi bằng nhau.

- **1. Bảng công thức tính địa chỉ ô nhớ mảng 2 chiều (2차원 배열 주소 계산):**

| Khái niệm | Ký hiệu quy ước | Ý nghĩa trong công thức |
| :--- | :---: | :--- |
| **Địa chỉ cơ sở** | $\text{Base}$ | Địa chỉ ô nhớ của phần tử đầu tiên $\&arr[0][0]$. |
| **Số cột của mảng** | $C$ (Columns) | Tổng số cột khai báo của mảng `arr[R][C]`. |
| **Vị trí phần tử cần tìm** | $i, j$ | Hàng $i$ và cột $j$ của phần tử `arr[i][j]`. |
| **Kích thước kiểu dữ liệu** | $\text{Size}$ | `sizeof(int) = 4`, `sizeof(char) = 1`, `sizeof(double) = 8`. |
| **CÔNG THỨC CHUẨN THI** | — | **$\text{Address} = \text{Base} + (i \times C + j) \times \text{Size}$** |

- **2. Bảng các hàm thao tác chuỗi chuẩn trong `<string.h>` (문자열 표준 함수):**

| Tên hàm C | Cú pháp điển hình | Bản chất chức năng | Giá trị trả về |
| :--- | :--- | :--- | :--- |
| **`strlen`** | `strlen(str)` | Đếm số ký tự thực tế từ đầu cho đến trước ký tự `\0`. | Trả về số nguyên `size_t` (độ dài chuỗi). |
| **`strcpy`** | `strcpy(dest, src)` | Sao chép toàn bộ chuỗi nguồn `src` (kèm cả `\0`) sang `dest`. | Trả về con trỏ trỏ tới chuỗi đích `dest`. |
| **`strcat`** | `strcat(dest, src)` | Nối chuỗi `src` vào ngay phía sau chuỗi `dest` (ghi đè lên `\0` cũ).| Trả về con trỏ trỏ tới chuỗi đích `dest`. |
| **`strcmp`** | `strcmp(s1, s2)` | So sánh thứ tự mã ASCII từng ký tự tương ứng của 2 chuỗi. | Bằng nhau: **`0`**; $s1 < s2$: **Số âm**; $s1 > s2$: **Số dương**. |
| **`strncpy`** | `strncpy(dest, src, n)`| Sao chép tối đa $n$ ký tự để chống tràn bộ nhớ. | Trả về con trỏ `dest`. |

- **3. Phân biệt mảng ký tự chuỗi và hằng chuỗi:**

| Cách khai báo chuỗi | Vùng nhớ lưu trữ | Khả năng sửa đổi từng ký tự |
| :--- | :--- | :--- |
| `char str[] = "HELLO";` | Nằm trên **Stack** của hàm hiện tại. | **Cho phép sửa đổi:** `str[0] = 'h';` hoàn toàn hợp lệ. |
| `char *ptr = "HELLO";` | Nằm trên vùng **Read-Only Data (ROData)**. | **Cấm sửa đổi:** `ptr[0] = 'h';` sẽ gây lỗi sập chương trình! |

- **주의/함정 (Bẫy đề thi):**
  - **Quên cộng 1 cho ký tự `\0`:** Khai báo `char str[5] = "HELLO";` sẽ bị lỗi biên dịch hoặc tràn bộ đệm vì từ "HELLO" cần đúng 5 byte chữ cái cộng thêm 1 byte cho `\0` $\rightarrow$ mảng phải có kích thước tối thiểu là `6`.
  - **Nhầm lẫn chỉ số mảng:** Mảng `int arr[5]` chỉ có các phần tử từ `arr[0]` đến `arr[4]`. Truy cập `arr[5]` là lỗi tràn chỉ số (Off-by-one / Out of Bounds).
  - **Gán chuỗi bằng dấu bằng:** Trong C, cấm gán `str1 = str2;` sau khi đã khai báo (vì tên mảng là hằng con trỏ). Bắt buộc phải dùng hàm `strcpy(str1, str2);`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Hàng $i$ nhân cột $C$ cộng $j$, chuỗi C luôn chốt bằng ký tự null ('\0'); strlen đếm chữ trừ null, strcmp bằng nhau trả số không (0)."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán trắc nghiệm tính địa chỉ ô nhớ mảng 2 chiều chuẩn đề thi:
- **Đề bài:** Một mảng 2 chiều số nguyên `int A[4][5]` được cấp phát bộ nhớ bắt đầu từ địa chỉ cơ sở `1000`. Giả sử mỗi phần tử `int` chiếm `4 Byte`. Hỏi địa chỉ ô nhớ của phần tử `A[2][3]` là bao nhiêu?
- **Phân tích thay số:**
  - $\text{Base} = 1000$
  - Số cột $C = 5$
  - Chỉ số phần tử: $i = 2, j = 3$
  - Kích thước phần tử: $\text{Size} = 4$
  - Áp dụng công thức:
    $$\text{Address}(A[2][3]) = 1000 + (2 \times 5 + 3) \times 4 = 1000 + (10 + 3) \times 4 = 1000 + 13 \times 4 = 1000 + 52 = \mathbf{1052}$$
- **Đáp án:** Địa chỉ của `A[2][3]` là **`1052`**.

#### 2. Minh họa hoạt động của các hàm chuỗi trong C:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char s1[20] = "Info";
    char s2[] = "Processing";

    // 1. Kiểm tra độ dài strlen
    printf("Do dai s1: %zu\n", strlen(s1)); // In ra: 4 (không tính \0)

    // 2. Nối chuỗi strcat
    strcat(s1, " "); // s1 tro thanh "Info "
    strcat(s1, s2);  // s1 tro thanh "Info Processing"
    printf("Chuoi sau noi: %s\n", s1);

    // 3. So sánh chuỗi strcmp
    char a[] = "Apple";
    char b[] = "Banana";
    char c[] = "Apple";

    printf("strcmp(a, c): %d\n", strcmp(a, c)); // Giong nhau -> In ra: 0
    printf("strcmp(a, b): %d\n", strcmp(a, b)); // 'A' (65) < 'B' (66) -> In ra so am (vi du -1)

    return 0;
}
```

#### 3. Bảng lần vết thuật toán đảo ngược chuỗi (In-place String Reversal):
Đoạn mã C:
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "ABCD";
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - 1 - i];
        str[len - 1 - i] = temp;
    }
    printf("str = %s\n", str);
    return 0;
}
```

*Bảng lần vết biến:*
- `len = 4`, điều kiện lặp `i < 4 / 2` tức `i < 2` ($i$ chạy từ 0 đến 1):
  - Khi $i = 0$: Hoán đổi `str[0]` ('A') và `str[3]` ('D') $\rightarrow$ Chuỗi trở thành `"DBCD"`.
  - Khi $i = 1$: Hoán đổi `str[1]` ('B') và `str[2]` ('C') $\rightarrow$ Chuỗi trở thành `"DCBA"`.
- Kết thúc vòng lặp, kết quả in ra: **`str = DCBA`**.

---

### 복습 체크리스트
- [ ] Thuộc lòng công thức địa chỉ mảng 2 chiều: $\text{Base} + (i \times C + j) \times \text{Size}$.
- [ ] Ghi nhớ ký tự kết thúc chuỗi trong C là `\0` với mã ASCII bằng 0.
- [ ] Nhớ khai báo mảng chuỗi phải cộng thêm 1 phần tử cho `\0`.
- [ ] Nắm chắc `strlen()` chỉ đếm số ký tự thực tế, bỏ qua `\0`.
- [ ] Thuộc quy tắc `strcmp()`: Trả về `0` khi hai chuỗi giống hệt nhau.
- [ ] Phân biệt được sự an toàn của `strncpy()` so với `strcpy()`.
