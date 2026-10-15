# 254 - 257. 반복문과 제어 키워드 (Loops & Control Keywords)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp, nguyên lý hoạt động và trường hợp ứng dụng tối ưu của 3 cấu trúc lặp cơ bản: Vòng lặp `for`, Vòng lặp `while`, và Vòng lặp `do-while`.
- Phân biệt sự khác nhau mang tính bản chất giữa kiểm tra điều kiện trước (**선행 판단** trong `for`, `while`) và kiểm tra điều kiện sau (**후행 판단** trong `do-while` – **luôn thực thi tối thiểu 1 lần**).
- Thấu hiểu hành vi điều khiển luồng của hai từ khóa hạt nhân: **`break` (thoát hẳn vòng lặp)** và **`continue` (bỏ qua lần lặp hiện tại để nhảy sang lần lặp kế tiếp)**.

## 핵심 키워드 (Từ khóa)
- 반복문 (Loop Statements: for, while, do-while)
- 선행 판단 루프 (Pre-test Loop: for, while)
- 후행 판단 루프 (Post-test Loop: do-while - 최소 1회 실행)
- `break` 키워드 (Immediate Loop Termination)
- `continue` 키워드 (Skip to Next Iteration)
- 무한 루프 (Infinite Loop Prevention)
- 중첩 반복문 (Nested Loops)

## 선행·연결 개념 (Kiến thức liên kết)
- [81-bai-hoc.md](81-bai-hoc.md): Câu lệnh rẽ nhánh đa lựa chọn `switch-case` và từ khóa `break`.
- [83-bai-hoc.md](83-bai-hoc.md): Phân loại ngôn ngữ lập trình hướng thủ tục, OOP và khai báo.
- [18-bai-hoc.md](18-bai-hoc.md): Căn bản về vòng lặp và mảng trong ngôn ngữ C.

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh đặc điểm thi cử:
  - Khi hỏi: "Vòng lặp nào **chắc chắn được thực thi ít nhất một lần** ngay cả khi điều kiện ban đầu là Sai?" $\rightarrow$ Chọn ngay **`do-while`** (do kiểm tra điều kiện ở đuôi).
  - Phân biệt `break` vs `continue`:
    - Gặp `break` $\rightarrow$ Vứt bỏ vòng lặp, nhảy hẳn ra ngoài dấu ngoặc nhọn `}` của vòng lặp.
    - Gặp `continue` $\rightarrow$ Không chạy các lệnh bên dưới nó trong thân vòng lặp nữa, mà quay lên đầu bước tăng giảm để **chạy lần lặp tiếp theo**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng đối chiếu 3 cấu trúc vòng lặp kinh điển:**

| Cấu trúc lặp | Cú pháp chuẩn trong C/Java | Thời điểm kiểm tra điều kiện | Số lần thực thi tối thiểu | Trường hợp sử dụng tối ưu |
| :--- | :--- | :---: | :---: | :--- |
| **`for`** | `for (init; cond; step) { ... }` | **Trước khi vào lặp** (Pre-test) | 0 lần | Khi đã biết trước số lần lặp cụ thể hoặc duyệt mảng có độ dài cố định. |
| **`while`** | `while (condition) { ... }` | **Trước khi vào lặp** (Pre-test) | 0 lần | Khi số lần lặp chưa biết trước, lặp phụ thuộc vào một sự kiện/trạng thái biến động. |
| **`do-while`** | `do { ... } while (condition);` | **Sau khi thân lặp chạy xong** (Post-test) | **1 lần** | Nhập dữ liệu và kiểm tra tính hợp lệ (Menu chương trình, nhập lại nếu sai). |

- **2. Bảng phân biệt sâu sắc: `break` vs `continue`:**

| Từ khóa | Hành vi điều khiển luồng | Điểm nhảy kế tiếp |
| :--- | :--- | :--- |
| **`break`** | Dừng và **thoát vĩnh viễn** khỏi vòng lặp chứa nó ngay lập tức. | Câu lệnh đầu tiên nằm ngay sau khối ngoặc nhọn `{ }` đóng vòng lặp. |
| **`continue`** | Chấm dứt vòng lặp con hiện tại, **bỏ qua các lệnh còn lại phía dưới**. | Trong `for`: Nhảy tới biểu thức tăng giảm (`step`); trong `while` / `do-while`: Nhảy tới bước kiểm tra điều kiện (`cond`). |

- **3. Đoạn mã minh họa bẫy tính toán trace trong đề thi:**

```c
#include <stdio.h>

int main() {
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue; // Bỏ qua tất cả các số chẵn
        }
        if (i > 7) {
            break;    // Dừng vòng lặp khi i vượt quá 7
        }
        sum += i;     // Chỉ cộng các số lẻ: 1 + 3 + 5 + 7
    }
    printf("sum = %d\n", sum); // In ra: sum = 16
    return 0;
}
```

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Vòng lặp vô hạn (Infinite Loop) và cách kiểm soát:**
  - Cú pháp tạo vòng lặp vô hạn kinh điển: `for (;;) { ... }` hoặc `while (1) { ... }`.
  - Trong các hệ thống điều khiển nhúng hoặc hệ thống dịch vụ lắng nghe socket mạng, vòng lặp vô hạn được cố tình sử dụng kết hợp với cơ chế `break` có điều kiện hoặc tín hiệu ngắt (Signal Interrupt) để duy trì hoạt động thường trực của tiến trình.

### 복습 체크리스트
- [ ] Ghi nhớ `do-while` là vòng lặp duy nhất luôn thực thi tối thiểu 1 lần.
- [ ] Nhớ cuối câu lệnh `do { ... } while (cond);` bắt buộc phải có dấu chấm phẩy `;`.
- [ ] Phân biệt được: `break` thoát hẳn vòng lặp, `continue` chỉ bỏ qua lượt hiện tại.
- [ ] Nắm được trong `for`, sau lệnh `continue` chương trình nhảy đến bước cập nhật tăng giảm biến đếm.
