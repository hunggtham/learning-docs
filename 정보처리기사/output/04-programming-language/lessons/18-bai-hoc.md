# 제어문 심화 (Control Statements - Advanced)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp, nguyên lý vận hành và chu trình lặp của 3 cấu trúc vòng lặp cốt lõi: Vòng lặp `for`, Vòng lặp `while` (kiểm tra điều kiện trước), và Vòng lặp `do-while` (kiểm tra điều kiện sau).
- Phân biệt sự khác nhau căn bản giữa `while` (có thể không chạy lần nào nếu điều kiện sai từ đầu) và `do-while` (bắt buộc thực thi phần thân ít nhất 1 lần).
- Nắm vững vai trò và hành vi của hai từ khóa điều khiển vòng lặp: `break` (thoát văng ra khỏi vòng lặp ngay lập tức) và `continue` (bỏ qua các lệnh còn lại bên dưới, nhảy sang bước lặp tiếp theo).

## 핵심 키워드 (Từ khóa)
- 반복문 (Loop Statements / for, while, do-while)
- for문 (초기식, 조건식, 증감식 구조)
- while문 (선 조건 검사 / 0회 실행 가능)
- do-while문 (후 조건 검사 / 최소 1회 무조건 실행 / 세미콜론 필수)
- break문 (반복문 즉각 탈출)
- continue문 (다음 반복으로 건너뛰기)
- 무한 루프 (Infinite Loop / `for(;;)` / `while(1)`)

## 선행·연결 개념 (Kiến thức liên kết)
- [17-bai-hoc.md](17-bai-hoc.md): Câu lệnh rẽ nhánh `if-else` và `switch-case`.
- [19-bai-hoc.md](19-bai-hoc.md): Cấu trúc, mảng và con trỏ trong ngôn ngữ C.
- [20-bai-hoc.md](20-bai-hoc.md): Mảng 2 chiều và vòng lặp lồng nhau (Nested Loops).

## 읽는 방법 (Cách đọc)
- Phân biệt 3 loại vòng lặp:
  - **`for`:** Dùng khi **biết trước số lần lặp** cụ thể: `for (khởi_tạo; điều_kiện; tăng_giảm)`.
  - **`while`:** Dùng khi lặp dựa trên **trạng thái điều kiện** chưa biết trước số lần: Kiểm tra điều kiện TRƯỚC, đúng mới chạy thân vòng lặp. Nếu sai ngay từ đầu $\rightarrow$ Không chạy lần nào (0 lần).
  - **`do-while`:** Chạy thân vòng lặp TRƯỚC một lần rồi mới kiểm tra điều kiện ở cuối $\rightarrow$ **Luôn luôn chạy ít nhất 1 lần**. Chú ý cú pháp kết thúc bằng dấu chấm phẩy: `do { ... } while (điều_kiện);`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 cấu trúc vòng lặp kinh điển:**

| Cấu trúc lặp | Vị trí kiểm tra điều kiện | Số lần thực thi tối thiểu | Cú pháp kết thúc | Ngữ cảnh ứng dụng tối ưu |
| :--- | :--- | :--- | :--- | :--- |
| **`for`** | Đầu vòng lặp (Trước khi chạy thân) | **0 lần** (Nếu điều kiện ban đầu sai) | Không có dấu chấm phẩy sau dấu ngoặc tròn `)` | Duyệt mảng tuần tự từ $0$ đến $n-1$, lặp với biến đếm |
| **`while`** | Đầu vòng lặp (**선 조건 검사**) | **0 lần** (Nếu điều kiện ban đầu sai) | Không có dấu chấm phẩy sau `while(조건)` | Đọc dữ liệu từ luồng/tệp cho đến khi gặp kết thúc tệp (EOF) |
| **`do - while`** | Cuối vòng lặp (**후 조건 검사**) | **Ít nhất 1 lần (최소 1회 실행)** | **BẮT BUỘC có dấu chấm phẩy `;`** sau `while(조건);` | Hiển thị menu cho người dùng chọn ít nhất một lần |

- **Bảng phân biệt giữa `break` và `continue` trong vòng lặp:**

| Từ khóa | Hành vi điều khiển luồng | Vị trí nhảy đến tiếp theo | Ví dụ với vòng lặp `for (i=1; i<=5; i++)` |
| :--- | :--- | :--- | :--- |
| **`break;`** | **Chấm dứt hoàn toàn (Thoát)** vòng lặp chứa nó ngay lập tức | Nhảy ra câu lệnh đầu tiên nằm **bên ngoài** khối vòng lặp | Nếu gặp `if (i == 3) break;` $\rightarrow$ Vòng lặp dừng lại, các lượt $i=3, 4, 5$ không chạy |
| **`continue;`** | **Bỏ qua phần còn lại** của bước lặp hiện tại | Nhảy đến phần **tăng giảm của `for`** hoặc điều kiện của `while` để chạy lượt tiếp | Nếu gặp `if (i == 3) continue;` $\rightarrow$ Chỉ bỏ qua lượt $i=3$, các lượt $i=4, 5$ vẫn chạy bình thường |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Bài toán thi mẫu lần vết kết hợp `continue` và `break`:**
  - *Đoạn mã C:*
    ```c
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) continue; // Bỏ qua số chẵn
        if (i > 7) break;         // Dừng khi vượt quá 7
        sum += i;
    }
    printf("%d", sum);
    ```
  - *Lần vết từng bước:*
    - $i = 1$: Thỏa mãn cả 2 if $\rightarrow$ `sum += 1` $\rightarrow$ `sum = 1`.
    - $i = 2$: Chẵn $\rightarrow$ `continue` $\rightarrow$ Bỏ qua.
    - $i = 3$: Số lẻ $\le 7$ $\rightarrow$ `sum += 3` $\rightarrow$ `sum = 4`.
    - $i = 4$: Chẵn $\rightarrow$ `continue` $\rightarrow$ Bỏ qua.
    - $i = 5$: Số lẻ $\le 7$ $\rightarrow$ `sum += 5` $\rightarrow$ `sum = 9`.
    - $i = 6$: Chẵn $\rightarrow$ `continue` $\rightarrow$ Bỏ qua.
    - $i = 7$: Số lẻ $\le 7$ $\rightarrow$ `sum += 7` $\rightarrow$ `sum = 16`.
    - $i = 8$: Chẵn $\rightarrow$ `continue`.
    - $i = 9$: $i > 7$ là True $\rightarrow$ Gặp `break;` $\rightarrow$ Thoát vòng lặp!
  - Kết quả in ra: `16`.

### 복습 체크리스트
- [ ] Nhớ `do-while` chạy ít nhất 1 lần và bắt buộc có dấu chấm phẩy ở cuối `while(cond);`.
- [ ] Phân biệt được `break` (thoát hẳn vòng lặp) và `continue` (bỏ qua lượt này, chạy lượt kế tiếp).
- [ ] Nhớ cấu trúc vòng lặp vô tận: `for(;;)` và `while(1)`.
- [ ] Lần vết chính xác các bài toán kết hợp lặp và điều kiện rẽ nhánh.
