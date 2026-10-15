# 핵심 257: 분기/제어 (break, continue)

## 학습 목표 (Mục tiêu)
- Phân biệt chính xác hành vi luồng thực thi giữa hai câu lệnh điều khiển vòng lặp: `break` và `continue` trong C, Java và Python.
- Nắm vững quy tắc nhảy của `continue` trong vòng lặp `for` (nhảy tới bước tăng giảm) và vòng lặp `while` (nhảy tới biểu thức điều kiện).
- Giải quyết thành thạo các câu hỏi đọc hiểu mã nguồn có vòng lặp lồng nhau (Nested loops) và cấu trúc rẽ nhánh `switch-case`.

## 핵심 키워드 (Từ khóa)
- **break**: Thoát ngay lập tức khỏi vòng lặp hoặc cấu trúc `switch` bao bọc gần nhất.
- **continue**: Bỏ qua các lệnh còn lại của lần lặp hiện tại, chuyển ngay sang lần lặp kế tiếp (chỉ dùng trong vòng lặp).
- **중첩 제어문 (Nested Control Structures)**: Phạm vi tác động của `break` khi có nhiều vòng lặp lồng nhau.
- **증감식 점프 (Jump to Update)**: Hành vi đặc trưng của `continue` trong vòng lặp `for`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [04-programming-language/81-bai-hoc.md](../../04-programming-language/lessons/81-bai-hoc.md) (Cấu trúc rẽ nhánh switch-case và fall-through).
- Liên kết với [04-programming-language/82-bai-hoc.md](../../04-programming-language/lessons/82-bai-hoc.md) (Các cấu trúc vòng lặp for, while, do-while).
- Liên kết với [41-bai-hoc.md](41-bai-hoc.md) (Duyệt mảng bằng vòng lặp và câu lệnh rẽ nhánh).

## 읽는 방법 (Cách đọc)
- Khi gặp bài tập lần vết biến (Trace code) có `continue`:
  - Trong `for(khởi tạo; điều kiện; tăng_giảm)`: Khi gặp `continue`, lập tức bỏ qua toàn bộ mã bên dưới và nhảy ngay về phần **tăng_giảm** rồi mới kiểm tra **điều kiện**.
  - Trong `while(điều kiện)`: Khi gặp `continue`, nhảy ngay về phần kiểm tra **điều kiện**. Cần chú ý cẩn thận biến đếm: nếu biến đếm nằm sau lệnh `continue`, vòng lặp sẽ bị **lặp vô tận**!
  - `break` chỉ thoát khỏi **1 tầng vòng lặp duy nhất** chứa nó.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bảng so sánh bản chất kỹ thuật break vs continue
| Tiêu chí so sánh | Câu lệnh break | Câu lệnh continue |
| :--- | :--- | :--- |
| **Phạm vi sử dụng** | Trong các vòng lặp (`for`, `while`, `do-while`) và câu lệnh `switch` | **Chỉ được dùng trong các cấu trúc lặp** (`for`, `while`, `do-while`) |
| **Hành vi luồng lệnh** | **Chấm dứt hoàn toàn** vòng lặp hiện tại và nhảy ra lệnh kế tiếp phía sau khối lặp | **Bỏ qua phần còn lại** của vòng lặp hiện tại, chuyển sang lần lặp kế tiếp |
| **Điểm đến tiếp theo** | Lệnh đầu tiên nằm ngoài khối lặp / khối `switch` | - Vòng lặp `for`: Nhảy tới bước tăng/giảm (`i++`) / - Vòng lặp `while`: Nhảy tới phần kiểm tra điều kiện |
| **Vòng lặp lồng nhau** | Chỉ phá vỡ **vòng lặp trong cùng** chứa câu lệnh `break` đó | Chỉ áp dụng cho **vòng lặp trong cùng** chứa câu lệnh `continue` đó |

#### 2. Ví dụ phân biệt luồng thực thi trong ngôn ngữ C
```c
#include <stdio.h>
int main() {
    int sum = 0;
    for(int i = 1; i <= 5; i++) {
        if(i == 3) continue; // Khi i=3, bỏ qua sum += i, nhảy thẳng lên i++ (lúc này i=4)
        if(i == 5) break;    // Khi i=5, thoát ngay lập tức khỏi vòng for
        sum += i;            // Được thực thi khi i=1, 2, 4
    }
    printf("%d", sum);       // Kết quả in ra: 1 + 2 + 4 = 7
    return 0;
}
```

#### 3. Bẫy lặp vô tận (Infinite Loop Trap) với câu lệnh continue trong while
- Quan sát đoạn mã nguồn sau trong đề thi:
  ```c
  int i = 0, sum = 0;
  while(i < 5) {
      if(i == 2) continue; // NGUY HIỂM: Nhảy về while(i < 5), biến i vẫn giữ giá trị 2!
      sum += i;
      i++;                 // Lệnh tăng bị bỏ qua, dẫn đến lặp vô tận (Hang/Time out)
  }
  ```
- *Quy tắc an toàn*: Trong vòng lặp `while`, việc thay đổi biến đếm phải được thực hiện trước câu lệnh rẽ nhánh chứa `continue`.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Sơ đồ luồng xử lý của break và continue trong vòng lặp for
```
       ┌────────────────► [Khởi tạo biến: int i = 0]
       │                            │
       │                            ▼
       │                    [Kiểm tra điều kiện: i < 5 ?] ──(False)──► [Thoát vòng for] ◄─┐
       │                            │                                                     │
       │                         (True)                                                   │
       │                            ▼                                                     │
       │                 ┌───► [Lệnh bên trong]                                           │
       │                 │          │                                                     │
       │                 │          ▼                                                     │
       │  [continue] ────┼─── [if(điều kiện)?] ──(Gặp break)──────────────────────────────┘
       │                 │          │
       │                 │     (Không gặp)
       │                 │          ▼
       │                 │    [sum += i]
       │                 │          │
       │                 └──────────┘
       │                            │
       └─────── [Bước tăng giảm: i++] ◄┘
```

#### 2. Kỹ thuật Labeled break / continue trong Java
- Trong ngôn ngữ Java, khi muốn thoát hoặc nhảy qua một vòng lặp bên ngoài (Outer Loop) từ một vòng lặp bên trong (Inner Loop), ta có thể sử dụng nhãn (Label):
  ```java
  outerLoop:
  for(int i = 0; i < 3; i++) {
      for(int j = 0; j < 3; j++) {
          if(i == 1 && j == 1) {
              break outerLoop; // Thoát hoàn toàn khỏi cả 2 tầng vòng lặp!
          }
      }
  }
  ```

---

### 복습 체크리스트
- [ ] Sự khác biệt cốt lõi giữa câu lệnh `break` và `continue` là gì?
- [ ] Trong vòng lặp `for`, sau khi thực hiện `continue` thì chương trình sẽ nhảy tới vị trí nào?
- [ ] Tại sao sử dụng `continue` trong vòng lặp `while` lại có nguy cơ gây ra lỗi lặp vô tận?
- [ ] Trong vòng lặp lồng nhau gồm 2 cấp, lệnh `break` ở cấp trong cùng sẽ giải phóng những vòng lặp nào?
