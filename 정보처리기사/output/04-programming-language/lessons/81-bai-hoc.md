# 253. switch문 (switch Statement)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp chuẩn và nguyên lý điều khiển rẽ nhánh đa lựa chọn của câu lệnh `switch-case` trong C, Java, và C++.
- Hiểu rõ vai trò của từ khóa `break`: Thoát ngay lập tức khỏi khối `switch` và nhận diện hiện tượng trôi nhánh (**Fall-Through**) khi thiếu sót `break`.
- Phân biệt các kiểu dữ liệu hợp lệ được phép sử dụng trong biểu thức điều khiển `switch(expr)` trên từng ngôn ngữ (Số nguyên, Ký tự, và Chuỗi trong Java $\ge 7$).

## 핵심 키워드 (Từ khóa)
- switch-case 제어문 (Multi-way Branching)
- `case` 레이블 (Constant Case Label)
- `break` 키워드 (Fall-through Prevention)
- `default` 레이블 (Fallback Exception Branch)
- Fall-through 현상 (Trôi nhánh thực thi)
- 정수형·문자형 수식 (Integer & Character Expressions)

## 선행·연결 개념 (Kiến thức liên kết)
- [80-bai-hoc.md](80-bai-hoc.md): Câu lệnh điều khiển rẽ nhánh đơn `if`.
- [82-bai-hoc.md](82-bai-hoc.md): Các vòng lặp (`for`, `while`, `do-while`) và từ khóa `break`/`continue`.
- [50-bai-hoc.md](50-bai-hoc.md): So sánh câu lệnh rẽ nhánh đa tầng `if - else if` vs `switch-case`.

## 읽는 방법 (Cách đọc)
- Trong các bài toán đọc mã `switch-case` của đề thi kỹ sư CNTT:
  - Bẫy kinh điển lớn nhất luôn là **THIẾU LỆNH `break;`**:
    - Khi một nhánh `case` khớp với giá trị biểu thức, chương trình sẽ chạy các lệnh trong nhánh đó.
    - **Nếu KHÔNG có `break;`**, chương trình sẽ **chạy tuôn trào (Fall-through) xuống tất cả các câu lệnh của các `case` bên dưới** (kể cả `default`) mà không hề kiểm tra lại điều kiện so sánh, cho tới khi nào gặp một lệnh `break;` hoặc chạm đến đáy dấu ngoặc nhọn `}` đóng khối `switch`.
  - Giá trị sau từ khóa `case` **bắt buộc phải là hằng số hoặc biểu thức hằng (Constant Expression)**; tuyệt đối không được dùng biến số hoặc biểu thức điều kiện so sánh (như `case x > 5:` là sai cú pháp).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng quy định kiểu dữ liệu trong biểu thức `switch`:**

| Ngôn ngữ | Các kiểu dữ liệu được phép trong `switch(expr)` | Ghi chú thi cử |
| :--- | :--- | :--- |
| **C / C++** | Số nguyên (`int`, `short`, `long`, `char`, `enum`) | **Cấm dùng số thực (`float`, `double`)** và cấm chuỗi ký tự (`string`). |
| **Java** | `byte`, `short`, `char`, `int`, `enum`, và **`String` (từ Java 7 trở lên)** | Cấm dùng số thực (`float`, `double`), cấm `boolean` và `long`. |

- **2. Bẫy trôi nhánh (Fall-through) trong mã nguồn thực tế:**

```c
#include <stdio.h>

int main() {
    int score = 2;
    int result = 10;

    switch (score) {
        case 1:
            result += 1;
            break;
        case 2:
            result += 2; // Khớp tại đây: result = 10 + 2 = 12
            // KHÔNG CÓ BREAK -> Rơi tự do xuống case 3!
        case 3:
            result += 3; // Tiếp tục chạy: result = 12 + 3 = 15
            // VẪN KHÔNG CÓ BREAK -> Rơi tiếp xuống default!
        default:
            result += 5; // Tiếp tục chạy: result = 15 + 5 = 20
            break;
    }

    printf("result = %d\n", result); // In ra màn hình: result = 20
    return 0;
}
```

- **3. Vai trò của nhánh `default`:**
  - Nhánh `default` là tùy chọn (Optional), được kích hoạt khi giá trị của biểu thức không trùng khớp với bất kỳ nhãn `case` nào phía trên.
  - Vị trí của `default` thông thường đặt ở cuối cùng, nhưng nếu đặt ở giữa mà không có `break`, luồng thực thi vẫn rơi tiếp xuống các `case` phía dưới.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tối ưu hóa bảng nhảy (Jump Table) của `switch-case` so với `if-else if`:**
  - Chuỗi `if - else if` có độ phức tạp thời gian là $O(N)$ vì phải thẩm định tuần tự từng điều kiện từ trên xuống dưới.
  - Câu lệnh `switch-case` được trình biên dịch tối ưu hóa thành một bảng con trỏ hàm/bảng nhảy (Jump Table / Branch Table) với độ phức tạp $O(1)$, cho phép nhảy thẳng đến khối mã tương ứng trong một chu kỳ tính toán địa chỉ duy nhất.

### 복습 체크리스트
- [ ] Nhớ hiện tượng Fall-through: Thiếu `break` sẽ khiến code chạy tuột xuống các `case` bên dưới.
- [ ] Khẳng định sau `case` bắt buộc phải là hằng số hoặc biểu thức hằng, không được dùng biến hay phép so sánh.
- [ ] Ghi nhớ trong C câu lệnh `switch` không hỗ trợ số thực (`float/double`) và chuỗi (`string`).
- [ ] Hiểu rõ `default` chỉ chạy khi không có nhãn `case` nào khớp (hoặc bị rơi từ case trên xuống).
