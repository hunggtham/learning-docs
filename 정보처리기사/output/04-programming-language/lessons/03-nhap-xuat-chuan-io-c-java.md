# 표준 입출력 함수 및 포맷팅 (Nhập xuất chuẩn & Định dạng C/Java)

## 학습 목표 (Mục tiêu)
- Nắm vững các hàm nhập xuất chuẩn trong ngôn ngữ C (`printf`, `scanf`, `getchar`, `gets`, `putchar`, `puts`) và Java (`System.out.print`, `println`, `printf`).
- Hiểu và tính toán chính xác kết quả của chuỗi định dạng (Format String Specifiers) phức hợp trong C: căn lề, độ rộng trường, số chữ số thập phân (`%8.2f`, `%-5d`, `%04d`), các hệ cơ số bát phân `%o`, thập lục phân `%x`.
- Nhận biết các lỗi biên dịch và lỗi thực thi kinh điển: quên toán tử địa chỉ `&` trong `scanf`, hiện tượng trôi lệnh do bộ đệm nhập (Input Buffer Overflow / Trailing Newline).

## 핵심 키워드 (Từ khóa)
- 표준 입출력 (Standard Input/Output) — Luồng dữ liệu vào ra tiêu chuẩn qua `stdin` và `stdout`.
- 서식 지정자 (Format Specifiers) — Ký tự đặc tả kiểu: `%d`, `%u`, `%f`, `%c`, `%s`, `%o`, `%x`, `%p`.
- 출력 포맷 제어 (Output Formatting Flags) — Căn phải, căn trái (`-`), đệm số 0 (`0`), độ chính xác (`.n`).
- 주소 연산자 (Address Operator `&`) — Truyền địa chỉ ô nhớ biến số cho hàm `scanf()`.
- 입력 버퍼 개행 문자 (Input Buffer Newline) — Ký tự `\n` còn sót lại làm trôi các hàm nhập ký tự tiếp theo.
- Java 표준 출력 (Java Standard Output) — `System.out.print`, `System.out.println`, `System.out.printf`.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa từ `01-bien-dinh-danh-va-kieu-du-lieu-c-java.md` (các kiểu dữ liệu nguyên thủy) và `02-toan-tu-va-thu-tu-uu-tien-operators.md` (toán tử địa chỉ `&`).
- **Đang giải quyết gì (Current Problem):** Giải quyết câu hỏi: Làm thế nào chương trình nhận dữ liệu từ người dùng và hiển thị kết quả ra màn hình với định dạng chính xác từng khoảng trắng và chữ số thập phân theo yêu cầu đề thi.
- **Dùng đi đâu (Forward Handoff):** Các kỹ thuật hiển thị và định dạng biến này sẽ phục vụ trực tiếp cho việc theo dõi, lần vết dữ liệu đầu ra của các thuật toán rẽ nhánh và vòng lặp trong bài `04-cau-truc-dieu-khien-re-nhanh-va-vong-lap.md`.

## 읽는 방법 (Cách đọc)
- **Định dạng `%w.pf`:**
  - `w` (Width - độ rộng tối thiểu của toàn bộ số in ra, tính cả dấu chấm và chữ số thập phân).
  - `p` (Precision - số chữ số sau dấu phẩy).
  - Mặc định căn lề bên phải (chèn khoảng trắng phía trước); nếu có dấu trừ `%-w.pf` thì căn lề bên trái.
- **`scanf` và dấu `&`:** Biến đơn (`int`, `float`, `char`) bắt buộc phải có `&` trước tên biến. Riêng chuỗi ký tự (mảng `char[]`) không cần `&` vì tên mảng bản thân nó đã là con trỏ địa chỉ.

---

## 표준 입출력 함수 및 포맷팅

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `printf 서식 지정자에서 %w.p는 전체 자릿수 w와 소수점 이하 p자리를 의미하며 기본 우측 정렬된다. 음수 부호(-)가 붙으면 좌측 정렬되고, scanf 함수에서 변수에 값을 입력받을 때는 반드시 주소 연산자(&)를 사용해야 한다.`
  - [Tiếng Việt]: Trong chuỗi định dạng printf, `%w.p` thể hiện tổng độ rộng $w$ và $p$ chữ số thập phân, mặc định căn phải. Dấu trừ (`-`) căn trái; khi dùng hàm scanf phải bắt buộc đặt toán tử địa chỉ `&` trước biến số đơn.

- **1. Bảng ký tự định dạng chuẩn (서식 문자열 일람):**

| Ký tự định dạng | Kiểu dữ liệu tương ứng | Cơ số / Cách biểu diễn | Ví dụ in ra với giá trị 255 |
| :---: | :--- | :--- | :--- |
| `%d` / `%i` | Số nguyên có dấu (`int`) | Hệ thập phân (Decimal) | `255` |
| `%u` | Số nguyên không dấu (`unsigned int`)| Hệ thập phân dương | `255` |
| `%o` | Số nguyên | **Hệ bát phân (Octal - cơ số 8)** | `377` ($3 \times 8^2 + 7 \times 8 + 7$) |
| `%x` / `%X` | Số nguyên | **Hệ thập lục phân (Hex - cơ số 16)**| `ff` (với `%x`) hoặc `FF` (với `%X`) |
| `%c` | Ký tự đơn (`char`) | Một ký tự mã ASCII | `'A'` |
| `%s` | Chuỗi ký tự (`char*`, `String`) | Chuỗi kết thúc bằng `\0` | `"Antigravity"` |
| `%f` | Số thực (`float`, `double`) | Dấu phẩy động thông thường | `255.000000` (mặc định 6 số lẻ) |
| `%e` / `%E` | Số thực | Dạng số mũ khoa học | `2.550000e+02` |
| `%p` | Con trỏ (`void*`) | Địa chỉ vùng nhớ hexa | `0x7ffee3b4` |

- **2. Bảng quy tắc cờ điều khiển độ rộng và căn lề (포맷 제어 플래그):**

| Chuỗi định dạng | Giá trị đầu vào | Kết quả in ra thực tế | Diễn giải quy tắc chuẩn thi |
| :--- | :---: | :--- | :--- |
| `%5d` | `123` | `  123` (2 khoảng trắng đầu) | Độ rộng tối thiểu 5 ký tự, **căn phải**, bù dấu cách phía trước. |
| `%-5d` | `123` | `123  ` (2 khoảng trắng cuối) | Có dấu `-`: **căn trái**, bù khoảng trắng ở phía sau. |
| `%05d` | `123` | `00123` | Có số `0`: Điền **số 0** vào các vị trí trống thay cho dấu cách. |
| `%8.2f` | `12.3456` | `   12.35` (3 khoảng trắng đầu)| Tổng độ rộng 8 ký tự, lấy 2 chữ số thập phân (làm tròn số). |
| `%-8.2f` | `12.3456` | `12.35   ` (3 khoảng trắng sau)| Căn trái, tổng độ rộng 8, lấy 2 số thập phân. |
| `%.3s` | `"KOREA"` | `KOR` | Lấy tối đa **3 ký tự đầu tiên** của chuỗi. |

- **3. Đối chiếu các hàm xuất trong Java (Java 표준 출력 함수):**

| Hàm Java | Hành vi xuống dòng | Hỗ trợ định dạng | Ngữ cảnh ứng dụng |
| :--- | :---: | :---: | :--- |
| `System.out.print()` | **Không xuống dòng** | Không | In liên tiếp trên cùng một dòng. |
| `System.out.println()`| **Tự động xuống dòng (`\n`)** | Không | In xong nội dung thì đẩy con trỏ sang dòng mới. |
| `System.out.printf()` | **Không xuống dòng** | **Có (dùng `%`)** | Dùng khi cần căn lề, làm tròn số như trong C. |

- **주의/함정 (Bẫy đề thi):**
  - **Quên dấu `&` trong `scanf`:** Lệnh `scanf("%d", a);` thay vì `scanf("%d", &a);` sẽ gây lỗi sập chương trình (Segmentation Fault / Access Violation) vì `scanf` coi giá trị của `a` là một địa chỉ ô nhớ để ghi đè.
  - **Khoảng trắng trong chuỗi `scanf("%s", str)`:** Hàm `scanf` với `%s` sẽ **ngừng đọc ngay khi gặp khoảng trắng** hoặc dấu tab/xuống dòng. Muốn đọc cả dòng có khoảng trắng trong C, phải dùng `gets()` (hoặc `fgets()`).
  - **Làm tròn số thập phân:** `%8.2f` với giá trị `3.146` sẽ làm tròn thành `3.15`.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Độ rộng $w$, thập phân $p$, âm căn trái dương căn phải; scanf nhớ dấu và (&), chuỗi đọc gặp cách là dừng."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Minh họa định dạng in trong C và bẫy làm tròn số:
```c
#include <stdio.h>

int main() {
    int num = 45;
    double pi = 3.141592;
    char str[] = "Information";

    // In số nguyên có căn lề và bù số 0
    printf("[%5d]\n", num);   // In ra: [   45] (căn phải)
    printf("[%-5d]\n", num);  // In ra: [45   ] (căn trái)
    printf("[%05d]\n", num);  // In ra: [00045] (bù số 0)

    // In số thực có làm tròn
    printf("[%8.2f]\n", pi);  // In ra: [    3.14] (tổng độ rộng 8, lấy 2 số lẻ)
    printf("[%8.4f]\n", pi);  // In ra: [  3.1416] (làm tròn số 5 lên)

    // Cắt chuỗi
    printf("[%.4s]\n", str);  // In ra: [Info] (chỉ lấy 4 ký tự đầu)

    // In hệ bát phân và thập lục phân
    printf("Octal: %o, Hex: %x, HEX: %X\n", num, num, num);
    // 45 = 5*8 + 5 -> %o ra 55
    // 45 = 2*16 + 13 (D) -> %x ra 2d, %X ra 2D

    return 0;
}
```

#### 2. Lần vết hiện tượng trôi lệnh trong `scanf` do bộ đệm bàn phím:
```c
#include <stdio.h>

int main() {
    int age;
    char grade;

    printf("Nhap tuoi: ");
    scanf("%d", &age); // Người dùng nhập: 25 rồi nhấn phím Enter ('\n')
    // Số 25 được đưa vào age, nhưng ký tự '\n' vẫn còn nằm lại trong Input Buffer (bộ đệm stdin)

    printf("Nhap xep loai (A/B/C): ");
    // scanf("%c", &grade); // LỖI BẪY: Lệnh này đọc ngay ký tự '\n' còn sót lại và kết thúc luôn!

    // GIẢI PHÁP ĐỀ THI: Thêm một dấu cách trước %c để yêu cầu bỏ qua mọi khoảng trắng và ký tự newline
    scanf(" %c", &grade); 

    printf("Tuoi: %d, Xep loai: %c\n", age, grade);
    return 0;
}
```

#### 3. Minh họa xuất chuẩn trong Java:
```java
public class JavaIODemo {
    public static void main(String[] args) {
        String name = "Kim";
        int score = 95;
        double gpa = 3.876;

        // print không xuống dòng
        System.out.print("Name: " + name);
        // println tự động thêm \n ở cuối
        System.out.println(" | Score: " + score);

        // printf định dạng theo chuẩn C
        System.out.printf("GPA lam tron: %.2f | Ma dinh danh: [%06d]\n", gpa, 123);
        // In ra: GPA lam tron: 3.88 | Ma dinh danh: [000123]
    }
}
```

---

### 복습 체크리스트
- [ ] Ghi nhớ ý nghĩa định dạng: `%d` (thập phân), `%o` (bát phân), `%x` (thập lục phân), `%f` (số thực).
- [ ] Hiểu rõ công thức `%w.pf`: $w$ là tổng độ rộng, $p$ là số chữ số thập phân.
- [ ] Nhớ dấu `-` là căn trái (`%-5d`), số `0` là điền số không vào khoảng trống (`%05d`).
- [ ] Nắm chắc quy tắc: `scanf` với biến đơn bắt buộc phải có toán tử địa chỉ `&`.
- [ ] Nhớ `%s` trong `scanf` tự động dừng khi gặp khoảng trắng đầu tiên.
- [ ] Phân biệt được trong Java: `print` không xuống dòng, `println` có xuống dòng, `printf` hỗ trợ định dạng `%`.
