# 제어문: 조건문과 반복문 (Cấu trúc điều khiển: Rẽ nhánh & Vòng lặp)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và bản chất vận hành của các cấu trúc điều khiển rẽ nhánh (`if`, `if - else`, `switch - case`) và cấu trúc lặp (`for`, `while`, `do - while`) trong các ngôn ngữ C, Java, Python.
- Thấu hiểu hiện tượng trôi nhánh (Fall-Through) khi thiếu lệnh `break` trong cấu trúc `switch - case` và tính chất bắt buộc chạy ít nhất một lần của vòng lặp `do - while`.
- Phân biệt rõ sự khác nhau giữa từ khóa `break` (ngắt toàn bộ vòng lặp) và `continue` (bỏ qua bước hiện tại nhảy sang lần lặp kế tiếp).
- Thành thạo kỹ năng lần vết thuật toán (Algorithm Tracing) cho vòng lặp lồng nhau (Nested Loops), tính tổng có điều kiện và xử lý mảng hai chiều.

## 핵심 키워드 (Từ khóa)
- 제어문 (Control Flow Statements) — Cấu trúc điều khiển luồng thực thi chương trình.
- 다중 if문 vs switch문 (Multiple if vs switch-case) — Đa nhánh tuần tự vs Nhánh hằng số trực tiếp.
- Fall-Through 현상 (Hiện tượng trôi nhánh) — Thiếu `break` khiến luồng tiếp tục chảy xuống các `case` bên dưới.
- 선행 판단 vs 후행 판단 (Pre-test vs Post-test Loop) — `while`/`for` (kiểm tra trước) vs `do - while` (kiểm tra sau).
- 최소 1회 실행 (Guaranteed Single Execution) — `do - while` luôn chạy thân vòng lặp ít nhất 1 lần.
- break vs continue — Thoát khỏi vòng lặp hoàn toàn vs Nhảy sang bước lặp tiếp theo.
- 중첩 반복문 (Nested Loops) — Vòng lặp lồng nhau duyệt chỉ số hàng cột.

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ đâu (Origin):** Kế thừa các biểu thức logic, quan hệ và thứ tự ưu tiên đã học ở bài `02-toan-tu-va-thu-tu-uu-tien-operators.md` để làm điều kiện rẽ nhánh/dừng lặp.
- **Đang giải quyết gì (Current Problem):** Giải quyết dạng câu hỏi chiếm tỷ trọng điểm số lớn nhất trong đề thi kỹ sư: Cho một đoạn mã nguồn C/Java có cấu trúc điều khiển lồng nhau phức tạp, yêu cầu lần vết từng bước biến số để xác định kết quả in ra màn hình.
- **Dùng đi đâu (Forward Handoff):** Các cấu trúc lặp `for` và `while` sẽ là công cụ bắt buộc để duyệt qua các phần tử của mảng và thao tác con trỏ ô nhớ trong bài `05-mang-va-chuoi-ky-tu-trong-c.md` và `06-con-tro-va-cau-truc-struct-trong-c.md`.

## 읽는 방법 (Cách đọc)
- **switch - case:** Nhìn ngay vào từng nhánh xem có lệnh `break` hay không. Nếu không có `break`, lệnh ở nhánh tiếp theo sẽ bị thực thi bất chấp điều kiện nhãn `case` đó có khớp hay không (hiện tượng Fall-through).
- **do - while:** Bắt buộc nhẩm trong đầu rằng khối lệnh bên trong `{ }` chắc chắn chạy qua một lần đầu tiên, rồi mới nhìn xuống điều kiện `while(điều kiện);` ở cuối.
- **continue:** Khi gặp `continue`, lập tức gạch bỏ các dòng lệnh phía dưới nó trong thân lặp và quay lên đầu vòng lặp.
- **Vòng lặp lồng nhau:** Với mỗi giá trị của biến lặp ngoài $i$, biến lặp trong $j$ sẽ chạy hết từ đầu đến cuối một chu kỳ đầy đủ.

---

## 제어문: 조건문과 반복문

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

- **핵심 원리 (Nguyên tắc cốt lõi):**
  - [한국어]: `switch문의 case 레이블에는 반드시 정수형 상수나 문자 상수가 와야 하며, break문이 없으면 다음 case문이 조건과 상관없이 연속 실행되는 Fall-Through 현상이 발생한다. do - while문은 조건식을 나중에 평가하므로 본문이 최소 1회 실행된다. break는 루프를 완전히 탈출하고 continue는 다음 반복 회차로 건너뛴다.`
  - [Tiếng Việt]: Nhãn case trong switch bắt buộc phải là hằng số nguyên hoặc ký tự; nếu thiếu break thì các case kế tiếp sẽ bị thực thi liên tục bất kể điều kiện (Fall-through). Vòng lặp do-while đánh giá điều kiện sau nên thân lặp được đảm bảo chạy ít nhất một lần. Lệnh break thoát hẳn vòng lặp còn continue nhảy sang bước lặp kế tiếp.

- **1. Bảng đối chiếu các cấu trúc rẽ nhánh điều kiện (조건문 비교):**

| Cấu trúc | Cú pháp cốt lõi | Kiểu dữ liệu điều kiện | Điểm bẫy đề thi HRDK |
| :--- | :--- | :--- | :--- |
| **Đơn if / if-else** | `if (조건식) { ... } else { ... }` | C: Số nguyên (`0` là False, khác 0 là True); Java: kiểu `boolean`. | Quên ngoặc nhọn `{ }` khi có từ 2 lệnh trở lên -> chỉ lệnh đầu tiên thuộc `if`. |
| **Đa nhánh else-if** | `if (...) ... else if (...) ... else ...` | Biểu thức quan hệ, logic bất kỳ. | Các nhánh mang tính **loại trừ lẫn nhau (Mutual Exclusion)**; chỉ 1 nhánh duy nhất được chạy. |
| **switch - case** | `switch (변수) { case C1: ... break; default: ... }` | **Số nguyên (`int`, `char`), cấm số thực (`float`, `double`)**. Java 7+ cho phép `String`. | **Thiếu break:** Chương trình chạy tràn xuống các case dưới (Fall-Through). |

- **2. Bảng đối chiếu các cấu trúc vòng lặp (반복문 비교):**

| Loại vòng lặp | Thời điểm kiểm tra điều kiện | Số lần lặp tối thiểu | Ngữ cảnh ứng dụng chuẩn thi |
| :--- | :---: | :---: | :--- |
| **`for`** | **Kiểm tra trước (선행 판단)** | 0 lần | Đã biết trước chính xác số lần lặp hoặc duyệt chỉ số mảng. |
| **`while`** | **Kiểm tra trước (선행 판단)** | 0 lần | Lặp theo điều kiện logic, số lần lặp chưa xác định trước. |
| **`do - while`** | **Kiểm tra sau (후행 판단)** | **Ít nhất 1 lần (최소 1회)** | Thân lặp cần chạy trước ít nhất 1 lần rồi mới kiểm tra điều kiện dừng. |

- **3. Phân biệt từ khóa điều khiển: `break` vs `continue`:**

| Tiêu chí so sánh | Từ khóa `break` | Từ khóa `continue` |
| :--- | :--- | :--- |
| **Bản chất hành vi** | **Chấm dứt hoàn toàn** vòng lặp hoặc khối `switch` gần nhất. | **Chỉ kết thúc lần lặp hiện tại**, bỏ qua các lệnh còn lại phía dưới. |
| **Điểm đến tiếp theo** | Nhảy ra lệnh đầu tiên ngay sau dấu ngoặc nhọn kết thúc `}`. | Nhảy lên bước tăng giảm (với `for`) hoặc kiểm tra điều kiện (với `while`). |
| **Phạm vi sử dụng** | Dùng được trong cả `switch` và các vòng lặp (`for`, `while`, `do-while`).| **Chỉ dùng duy nhất bên trong các vòng lặp**, không dùng trong `switch`. |

- **주의/함정 (Bẫy đề thi):**
  - **Dấu chấm phẩy vô tình sau vòng lặp:** `for (int i=0; i<10; i++);` -> Dấu `;` ở cuối tạo thành thân lặp rỗng; khối lệnh thụt lề bên dưới chỉ chạy đúng 1 lần sau khi vòng lặp đã kết thúc!
  - **Biểu thức gán trong `if`:** Trong C, `if (a = 0)` là phép gán biến `a` thành 0, giá trị biểu thức trả về `0` (False); ngược lại `if (a = 5)` trả về 5 (True). Phép so sánh bắt buộc phải dùng hai dấu bằng `if (a == 0)`.
  - **`switch` với số thực:** Đoạn mã `double x = 1.0; switch(x) { ... }` sẽ bị **lỗi biên dịch ngay lập tức**.
  - **Fall-Through có chủ đích:** Các case liên tiếp không có thân lệnh: `case 1: case 2: case 3: do_something(); break;` -> Dùng để gom nhóm các giá trị có cùng hành động xử lý.

- **한 문장 설명 (Câu chốt tự nhớ):**
  - *"Switch cấm số thực, thiếu break trôi dòng; do-while chạy một vòng rồi mới mong xét biến; continue bỏ lượt, break dừng luôn."*

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Lần vết hiện tượng Fall-Through trong `switch-case`:
```c
#include <stdio.h>

int main() {
    int score = 2;
    int bonus = 0;

    switch (score) {
        case 1:
            bonus += 10;
            break;
        case 2:
            bonus += 20; // Khớp điều kiện score == 2: bonus = 20
            // KHÔNG CÓ BREAK: Chảy thẳng xuống case 3 và default!
        case 3:
            bonus += 30; // bonus = 20 + 30 = 50
        default:
            bonus += 5;  // bonus = 50 + 5 = 55
    }

    printf("Bonus nhan duoc: %d\n", bonus); // Kết quả in ra: 55 (chứ không phải 20!)
    return 0;
}
```

#### 2. Lần vết vòng lặp `do-while` với điều kiện ban đầu sai:
```c
#include <stdio.h>

int main() {
    int count = 10;

    // Vòng lặp while: Không bao giờ chạy vì 10 < 5 là False
    while (count < 5) {
        count++;
    }
    printf("Sau while: count = %d\n", count); // count vẫn là 10

    // Vòng lặp do-while: Luôn chạy thân lặp trước 1 lần
    do {
        count += 5; // count = 10 + 5 = 15
    } while (count < 5); // 15 < 5 là False -> Thoát lặp ngay

    printf("Sau do-while: count = %d\n", count); // Kết quả: count = 15!
    return 0;
}
```

#### 3. Bảng lần vết (Trace Table) bài toán lồng nhau kết hợp `continue` và `break`:
Đoạn mã C:
```c
#include <stdio.h>

int main() {
    int sum = 0;
    for (int i = 1; i <= 5; i++) {
        if (i == 2) {
            continue; // Bỏ qua lần lặp i = 2
        }
        if (i == 4) {
            break;    // Thoát khỏi vòng lặp khi i = 4
        }
        sum += i;
    }
    printf("sum = %d\n", sum);
    return 0;
}
```

*Bảng lần vết từng bước thực thi:*

| Bước lặp ($i$) | Điều kiện `i == 2` | Điều kiện `i == 4` | Hành động thực hiện | Giá trị tích lũy `sum` |
| :---: | :---: | :---: | :--- | :---: |
| $i = 1$ | Sai | Sai | Thực hiện `sum += 1` | **1** |
| $i = 2$ | **Đúng** | (Chưa xét) | Gặp `continue` -> Bỏ qua dòng cộng, tăng $i$ | 1 |
| $i = 3$ | Sai | Sai | Thực hiện `sum += 3` | **4** |
| $i = 4$ | Sai | **Đúng** | Gặp `break` -> **Thoát ngay lập tức khỏi vòng lặp** | **4** |
| **Kết quả in ra**| — | — | **`sum = 4`** | — |

#### 4. Lần vết vòng lặp `for` lồng nhau (Nested For Loops):
Đoạn mã tính tổng tam giác:
```c
#include <stdio.h>

int main() {
    int total = 0;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= i; j++) {
            total += (i * j);
        }
    }
    printf("total = %d\n", total);
    return 0;
}
```

*Bảng lần vết vòng lặp lồng:*

| Vòng ngoài ($i$) | Vòng trong ($j$) | Điều kiện $j \le i$ | Giá trị cộng thêm ($i \times j$) | Giá trị tích lũy `total` |
| :---: | :---: | :---: | :---: | :---: |
| $i = 1$ | $j = 1$ | Đúng ($1 \le 1$) | $1 \times 1 = 1$ | **1** |
| $i = 2$ | $j = 1$ | Đúng ($1 \le 2$) | $2 \times 1 = 2$ | **3** |
| $i = 2$ | $j = 2$ | Đúng ($2 \le 2$) | $2 \times 2 = 4$ | **7** |
| $i = 3$ | $j = 1$ | Đúng ($1 \le 3$) | $3 \times 1 = 3$ | **10** |
| $i = 3$ | $j = 2$ | Đúng ($2 \le 3$) | $3 \times 2 = 6$ | **16** |
| $i = 3$ | $j = 3$ | Đúng ($3 \le 3$) | $3 \times 3 = 9$ | **25** |
| **Kết quả in ra**| — | — | — | **`total = 25`** |

---

### 복습 체크리스트
- [ ] Nhớ trong C: số 0 là False, mọi số khác 0 đều là True trong biểu thức `if`.
- [ ] Phân biệt được phép gán `if (a = 5)` (luôn True) và phép so sánh `if (a == 5)`.
- [ ] Ghi nhớ `switch` cấm dùng số thực (`float`, `double`), các nhãn `case` phải là hằng số.
- [ ] Hiểu rõ hiện tượng Fall-Through: Nếu thiếu lệnh `break`, code tự động tràn sang các case phía dưới.
- [ ] Nhớ `do-while` có dấu chấm phẩy `;` ở cuối cú pháp và đảm bảo chạy thân lặp ít nhất 1 lần.
- [ ] Phân biệt thành thạo: `break` ngắt vòng lặp vĩnh viễn, `continue` chỉ bỏ qua lượt lặp hiện tại.
- [ ] Thành thạo lần vết vòng lặp lồng nhau với các biểu thức nhân và cộng tích lũy.
