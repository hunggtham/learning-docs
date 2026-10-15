# 251. 단순 if문 (Simple if Statement)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp cơ bản và nguyên lý điều khiển luồng thực thi của câu lệnh điều kiện rẽ nhánh đơn (단순 if문 - Simple if Statement) trong các ngôn ngữ lập trình C, Java, và Python.
- Thấu hiểu quy ước chân trị số học đặc thù trong ngôn ngữ C: **Giá trị `0` đại diện cho Sai (False), mọi giá trị khác 0 (kể cả số âm) đều được coi là Đúng (True)**.
- Nhận diện và phòng tránh các bẫy đề thi kinh điển: Thiếu cặp ngoặc nhọn `{ }` khi có nhiều câu lệnh và nhầm lẫn giữa toán tử so sánh `==` với toán tử gán `=`.

## 핵심 키워드 (Từ khóa)
- 단순 if문 (Simple if Statement)
- 조건식 평가 (Condition Evaluation: True / False)
- 중괄호 블록 (`{ }` Compound Statement Block)
- C언어 참/거짓 규정 (0은 거짓, 0 이외는 모두 참)
- 대입 연산자 (`=`) vs 관계 연산자 (`==`)
- 세미콜론 bẫy cú pháp (Dangling Semicolon Trap)

## 선행·연결 개념 (Kiến thức liên kết)
- [79-bai-hoc.md](79-bai-hoc.md): Xuất dữ liệu chuẩn và bẫy nối chuỗi trong Java.
- [81-bai-hoc.md](81-bai-hoc.md): Câu lệnh rẽ nhánh đa lựa chọn `switch-case`.
- [17-bai-hoc.md](17-bai-hoc.md): Nền tảng các câu lệnh điều khiển luồng trong lập trình C.

## 읽는 방법 (Cách đọc)
- Trong các câu hỏi đọc mã C:
  - Bẫy giá trị logic: Nếu điều kiện ghi `if (x)` mà $x = -5$, kết quả vẫn là **True** vì $-5 \neq 0$. Chỉ khi nào $x = 0$ thì điều kiện mới là False.
  - Bẫy gán biến: `if (a = 0)` $\rightarrow$ Gán $a = 0$, giá trị biểu thức là $0$ (False) $\rightarrow$ Không bao giờ chạy vào trong `if`. Nhưng `if (a = 3)` $\rightarrow$ Gán $a = 3$, giá trị biểu thức là $3 \neq 0$ (True) $\rightarrow$ Luôn luôn chạy vào `if`!
  - Bẫy không có ngoặc `{ }`:
    ```c
    if (x > 10)
        a = 1;
        b = 2; // Câu lệnh này KHÔNG thuộc if, luôn luôn được chạy!
    ```

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Cú pháp và quy tắc khối lệnh:**
  - Nếu sau `if` chỉ có duy nhất 1 câu lệnh, có thể lược bỏ cặp ngoặc nhọn `{ }`.
  - Nếu sau `if` có từ 2 câu lệnh trở lên, **bắt buộc phải đặt trong cặp ngoặc nhọn `{ }`** để tạo thành một khối lệnh hợp thành (Compound Statement).

- **2. Bảng đối chiếu quy ước chân trị True/False giữa các ngôn ngữ:**

| Ngôn ngữ | Quy tắc xác định Chân trị (Truthiness) |
| :--- | :--- |
| **C / C++** | Không có kiểu boolean nguyên thủy ban đầu. Số nguyên **`0` là False**; **tất cả các số khác 0 (dương hoặc âm như `1, -1, 100`) đều là True**. |
| **Java** | Kiểm tra kiểu tĩnh nghiêm ngặt. Biểu thức trong `if (...)` **bắt buộc phải trả về kiểu `boolean` (`true` hoặc `false`)**. Ghi số nguyên như `if (1)` sẽ bị lỗi biên dịch ngay lập tức. |
| **Python** | `False`, `None`, số `0`, chuỗi rỗng `""`, danh sách rỗng `[]`, bộ rỗng `()` đều là False; các giá trị còn lại là True. |

- **3. Phân tích các bẫy đề thi kinh điển:**

```c
#include <stdio.h>

int main() {
    int x = 5;
    int y = 0;

    // Bẫy 1: Dấu chấm phẩy ngay sau if (Empty statement)
    if (x < 0); // Dấu ; kết thúc câu lệnh if ngay tại đây!
    {
        y = 10; // Khối này trở thành khối độc lập, LUÔN LUÔN CHẠY!
    }
    printf("y = %d\n", y); // In ra: y = 10

    // Bẫy 2: Nhầm toán tử gán (=) thay vì so sánh (==)
    int a = 0;
    if (a = 5) { // Gán a = 5; giá trị biểu thức là 5 (Khác 0 -> True)
        printf("True! a = %d\n", a); // In ra: True! a = 5
    }

    // Bẫy 3: Giá trị âm trong C
    int b = -10;
    if (b) { // b = -10 khác 0 -> Được coi là True!
        printf("Negative is True\n"); // In ra dòng này!
    }

    return 0;
}
```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Kỹ thuật Yoda Conditions trong phòng chống lỗi gán nhầm:**
  - Để tránh viết nhầm `if (x = 5)` thay vì `if (x == 5)`, các chuyên gia phần mềm đề xuất viết hằng số lên trước biến: `if (5 == x)`. Nếu vô tình gõ thiếu một dấu `=` thành `if (5 = x)`, trình biên dịch sẽ báo lỗi cú pháp ngay (do không thể gán giá trị cho hằng số 5), giúp loại bỏ hoàn toàn lỗi ngầm logic.

### 복습 체크리스트
- [ ] Ghi nhớ trong C: Số 0 là False, mọi số khác 0 (kể cả số âm) đều là True.
- [ ] Nhớ trong Java câu điều kiện `if` chỉ chấp nhận kiểu `boolean`, không dùng số nguyên `0/1`.
- [ ] Cảnh giác dấu chấm phẩy đứng ngay sau `if (...) ;` làm vô hiệu hóa điều kiện.
- [ ] Phân biệt được phép so sánh `==` và phép gán `=` bên trong biểu thức `if`.
