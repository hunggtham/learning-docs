# 제어문 (Control Statements)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và nguyên lý điều khiển luồng thực thi rẽ nhánh trong ngôn ngữ lập trình C và Java: Câu lệnh `if` đơn giản, cấu trúc `if-else`, và chuỗi rẽ nhánh nhiều tầng `if - else if - else`.
- Hiểu sâu cấu trúc câu lệnh lựa chọn đa nhánh `switch-case`: vai trò của từ khóa `break`, khối mặc định `default`, và hiện tượng thực thi trôi tuột (Fall-through) khi thiếu `break`.
- Nắm vững các kiểu dữ liệu hợp lệ được phép sử dụng trong biểu thức điều kiện của câu lệnh `switch` trên từng ngôn ngữ (số nguyên, ký tự trong C; chuỗi String trong Java 7+).

## 핵심 키워드 (Từ khóa)
- 제어문 (Control Statements / 선택문)
- if-else문 (선택 분기문)
- switch-case문 (다중 선택문)
- break문 (분기 탈출 / Fall-through 방지)
- default절 (기본 실행문)
- 복문 블록 (Block `{ }` / 중괄호 필수)
- C언어 조건식 참/거짓 (0은 거짓, 0 이외는 참)

## 선행·연결 개념 (Kiến thức liên kết)
- [16-bai-hoc.md](16-bai-hoc.md): Các hàm nhập xuất và định dạng độ rộng.
- [18-bai-hoc.md](18-bai-hoc.md): Câu lệnh điều khiển lặp (`for`, `while`, `do-while`).
- [11-bai-hoc.md](11-bai-hoc.md): Toán tử điều kiện ba ngôi thay thế `if-else`.

## 읽는 방법 (Cách đọc)
- Phân biệt hai loại câu lệnh rẽ nhánh:
  - **`if-else`:** Rẽ nhánh dựa trên **biểu thức điều kiện logic** (So sánh lớn bé, kết hợp `&&`, `||`). Nếu có từ 2 câu lệnh trở lên bên trong nhánh, bắt buộc phải bọc trong khối ngoặc nhọn `{ }`.
  - **`switch-case`:** Rẽ nhánh dựa trên **giá trị hằng số chính xác** (Constant Value). Nếu không có lệnh `break;` ở cuối mỗi nhánh `case`, chương trình sẽ **chạy tuột xuống (Fall-through)** thực thi luôn các lệnh của các `case` bên dưới bất kể điều kiện có khớp hay không.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh câu lệnh `if-else` vs câu lệnh `switch-case`:**

| Tiêu chuẩn so sánh | Cấu trúc `if - else if - else` | Cấu trúc `switch - case` |
| :--- | :--- | :--- |
| **Bản chất điều kiện** | Kiểm tra biểu thức logic bất kỳ (Dải giá trị, điều kiện phức) | So sánh **khớp giá trị hằng số cụ thể** (Discrete Values) |
| **Kiểu dữ liệu hỗ trợ** | Mọi kiểu dữ liệu (Số nguyên, số thực, con trỏ, đối tượng) | **Số nguyên (`int`, `char`, `short`, `byte`)**; Java 7+ cho phép thêm chuỗi `String`. **C cấm dùng số thực `float/double`** |
| **Cơ chế thoát nhánh** | Tự động thoát ra sau khi thực hiện xong một nhánh `else if` | **Bắt buộc phải có `break;`**; nếu thiếu `break` sẽ chạy tràn xuống các `case` tiếp theo |
| **Nhánh dự phòng** | Mệnh đề `else` cuối cùng | Mệnh đề `default:` thực thi khi không khớp bất kỳ `case` nào |

- **Bẫy kinh điển: Hiện tượng Fall-through trong `switch-case`:**
  - *Đoạn mã C:*
    ```c
    int n = 2;
    switch(n) {
        case 1: printf("One ");
        case 2: printf("Two ");
        case 3: printf("Three "); break;
        default: printf("Other");
    }
    ```
  - *Quá trình lần vết:*
    1. Giá trị $n = 2$ nhảy trúng vào `case 2:`, in ra `Two `.
    2. Do tại `case 2` **hoàn toàn không có câu lệnh `break;`**, chương trình tiếp tục chạy tràn xuống thực thi lệnh của `case 3:`, in tiếp `Three `.
    3. Tại `case 3` gặp lệnh `break;`, chương trình thoát khỏi khối `switch`.
    4. Màn hình in ra: `Two Three ` (Không in `Other`).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy tắc dấu ngoặc nhọn `{ }` trong câu lệnh `if`:**
  - Nếu sau `if` không có dấu ngoặc nhọn `{ }`, câu lệnh `if` chỉ kiểm soát duy nhất **một dòng lệnh đơn** nằm ngay phía sau nó.
  - *Ví dụ:*
    ```c
    int a = 5;
    if (a > 10)
        printf("A "); // Không chạy
        printf("B "); // Vẫn chạy vì nằm ngoài phạm vi if!
    ```
  - Kết quả: In ra `B ` vì dòng thứ hai là một câu lệnh độc lập. Đây là bẫy nhận diện luồng cực kỳ nguy hiểm.

### 복습 체크리스트
- [ ] Nhớ trong C: Biểu thức switch KHÔNG ĐƯỢC dùng số thực `float` hay `double`.
- [ ] Nhớ hiện tượng Fall-through khi thiếu `break` trong cấu trúc switch-case.
- [ ] Nhớ khối `default` trong switch là tùy chọn (optional), chạy khi không khớp case nào.
- [ ] Nhớ nếu không có ngoặc nhọn `{ }`, `if` chỉ điều khiển duy nhất một câu lệnh liền sau.
