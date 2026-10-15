# 075 - 077. 배열, 조건문, 반복문 (Arrays, Conditionals & Loops)

## 학습 목표 (Mục tiêu)
- Tổng hợp và liên kết toàn diện 3 trụ cột cơ bản của cấu trúc lập trình điều khiển: Mảng dữ liệu (배열), Câu lệnh điều kiện (조건문), và Câu lệnh lặp (반복문).
- Rèn luyện kỹ năng phân tích thuật toán giải các bài toán kinh điển: Tìm giá trị lớn nhất/nhỏ nhất trong mảng, Đếm số lượng phần tử thỏa mãn điều kiện, và Tính tổng dồn có điều kiện.
- Nắm vững các bước lập bảng vết (Trace Table) để theo dõi biến đếm, chỉ số mảng và điều kiện rẽ nhánh trong các câu hỏi code thi Kỹ sư xử lý thông tin.

## 핵심 키워드 (Từ khóa)
- 배열과 제어문 종합 (Arrays & Control Flow Synthesis)
- 최대값/최소값 탐색 (Max/Min Search Algorithm)
- 누적 합계 (Cumulative Sum / `sum += arr[i]`)
- 조건부 필터링 (Conditional Filtering / `if (arr[i] % 2 == 0)`)
- 루프 인덱스 제어 (Loop Index Control / `0`부터 `n-1`까지)
- 다중 반복문 추적 (Trace of Nested Loops)

## 선행·연결 개념 (Kiến thức liên kết)
- [21-bai-hoc.md](21-bai-hoc.md): Con trỏ và mảng nâng cao.
- [23-bai-hoc.md](23-bai-hoc.md): Xử lý chuỗi ký tự và các hàm thư viện `string.h`.
- [18-bai-hoc.md](18-bai-hoc.md): Chi tiết câu lệnh lặp `for`, `while`, `do-while`.

## 읽는 방법 (Cách đọc)
- Luôn tuân thủ quy trình 3 bước khi lần vết bài toán mảng kết hợp vòng lặp:
  1. **Bước 1 - Khởi tạo:** Ghi nhận kích thước mảng $n$, giá trị ban đầu của biến tích lũy `sum = 0` hoặc biến cực trị `max = arr[0]`.
  2. **Bước 2 - Lần vết từng vòng lặp:** Lập bảng các cột: Vòng lặp `i`, Giá trị `arr[i]`, Điều kiện `if`, Biến tích lũy thay đổi.
  3. **Bước 3 - Điều kiện dừng:** Kiểm tra chính xác chỉ số lặp cuối cùng (ví dụ: `i < 5` thì lượt lặp cuối cùng là `i = 4`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Mẫu thuật toán tìm Giá trị Lớn nhất (Max) và Nhỏ nhất (Min) trong mảng:**

| Bước thuật toán | Thao tác lập trình chuẩn | Ý nghĩa logic |
| :--- | :--- | :--- |
| **1. Khởi tạo cực trị** | `int max = arr[0]; int min = arr[0];` | Luôn gán giá trị của phần tử đầu tiên làm chuẩn đối sánh ban đầu |
| **2. Vòng lặp duyệt** | `for (int i = 1; i < n; i++)` | Bắt đầu duyệt từ phần tử thứ 2 (chỉ số 1) đến cuối mảng |
| **3. Cập nhật cực đại** | `if (arr[i] > max) max = arr[i];` | Nếu tìm thấy phần tử lớn hơn `max` hiện thời thì cập nhật `max` mới |
| **4. Cập nhật cực tiểu** | `if (arr[i] < min) min = arr[i];` | Nếu tìm thấy phần tử nhỏ hơn `min` hiện thời thì cập nhật `min` mới |

- **Bài toán thi mẫu: Tính tổng các phần tử có chỉ số lẻ và giá trị chẵn:**
  - *Đoạn mã C:*
    ```c
    int a[] = { 12, 15, 8, 20, 14, 7, 30 };
    int sum = 0;
    int len = sizeof(a) / sizeof(a[0]); // len = 7
    for (int i = 0; i < len; i++) {
        if (i % 2 != 0 && a[i] % 2 == 0) {
            sum += a[i];
        }
    }
    printf("%d", sum);
    ```
  - *Bảng lần vết chi tiết:*

| Chỉ số `i` | Giá trị `a[i]` | Điều kiện `i % 2 != 0` (Chỉ số lẻ) | Điều kiện `a[i] % 2 == 0` (Giá trị chẵn) | Kết quả điều kiện `&&` | Giá trị `sum` tích lũy |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 12 | Sai (0 là chẵn) | Đúng | Sai | 0 |
| **1** | **15** | Đúng | Sai (15 là lẻ) | Sai | 0 |
| 2 | 8 | Sai | Đúng | Sai | 0 |
| **3** | **20** | **Đúng** | **Đúng (20 là chẵn)** | **ĐÚNG** | $0 + 20 = \mathbf{20}$ |
| 4 | 14 | Sai | Đúng | Sai | 20 |
| **5** | **7** | Đúng | Sai (7 là lẻ) | Sai | 20 |
| 6 | 30 | Sai | Đúng | Sai | 20 |

  - *Kết quả cuối cùng:* In ra **`20`**.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Công thức xác định độ dài mảng trong C:**
  - Trong C không có thuộc tính `a.length` như Java. Độ dài mảng được tính bằng:
    $$\text{Độ dài} = \frac{\text{sizeof(mảng)}}{\text{sizeof(phần tử đầu)}} = \frac{\text{sizeof(a)}}{\text{sizeof(a[0])}}$$
  - Công thức này chỉ đúng khi mảng còn nằm trong cùng hàm khai báo. Khi mảng được truyền vào một hàm con dưới dạng tham số, nó bị suy biến thành con trỏ (Pointer Decay), khi đó `sizeof(a)` sẽ trả về kích thước con trỏ (4 hoặc 8 bytes) chứ không còn là dung lượng mảng.

### 복습 체크리스트
- [ ] Tính thành thạo số phần tử mảng bằng công thức `sizeof(a) / sizeof(a[0])`.
- [ ] Lập được bảng lần vết các bài toán mảng kết hợp vòng lặp và điều kiện logic.
- [ ] Nhớ chỉ số mảng luôn bắt đầu từ 0 và kết thúc tại $n - 1$.
- [ ] Nhớ gán giá trị khởi tạo `max = arr[0]` thay vì gán bằng 0 (tránh trường hợp mảng toàn số âm).
