# 배열 심화 (Arrays - Advanced)

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc, cú pháp khởi tạo và cơ chế lưu trữ bộ nhớ của mảng 2 chiều (2차원 배열) trong ngôn ngữ C và Java.
- Hiểu rõ nguyên lý lưu trữ ưu tiên theo hàng (행 우선 순서 - Row-Major Order) của mảng 2 chiều trong bộ nhớ vật lý tuyến tính và công thức tính toán địa chỉ phần tử `a[i][j]`.
- Nắm vững kỹ thuật duyệt mảng đa chiều bằng các vòng lặp lồng nhau (이중 for문 / Nested Loops) và biểu thức con trỏ tương đương: `a[i][j] == *(*(a + i) + j)`.

## 핵심 키워드 (Từ khóa)
- 2차원 배열 (2-Dimensional Array / 행렬 Matrix)
- 행 우선 순서 (Row-Major Order)
- 2차원 배열 주소 계산 (Address Calculation: $\text{Base} + (i \times C + j) \times \text{Size}$)
- 이중 루프 (Nested for Loops / 행 $i$, 열 $j$)
- 2차원 배열과 포인터 (`*(*(a + i) + j)`)
- 배열 포인터 vs 포인터 배열 (Array Pointer vs Pointer Array)

## 선행·연결 개념 (Kiến thức liên kết)
- [19-bai-hoc.md](19-bai-hoc.md): Cấu trúc, mảng và con trỏ cơ bản.
- [21-bai-hoc.md](21-bai-hoc.md): Con trỏ mảng nâng cao và chuỗi ký tự.
- [18-bai-hoc.md](18-bai-hoc.md): Câu lệnh điều khiển lặp lồng nhau.

## 읽는 방법 (Cách đọc)
- Hình dung mảng 2 chiều `int a[R][C]` như một ma trận gồm $R$ hàng và $C$ cột:
  - Khi lưu trữ trong bộ nhớ RAM (vốn là một đường thẳng tuyến tính), máy tính trải phẳng mảng theo nguyên tắc **행 우선 (Row-Major)**: Lưu toàn bộ Hàng 0 trước, rồi đến toàn bộ Hàng 1, rồi đến Hàng 2...
  - Chỉ số hàng $i$ chạy từ $0$ đến $R-1$; chỉ số cột $j$ chạy từ $0$ đến $C-1$.
  - Biểu thức tương đương giữa mảng 2 chiều và con trỏ:
    $$a[i][j] \iff *(*(a + i) + j)$$

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Công thức tính địa chỉ ô nhớ phần tử `a[i][j]` (Row-Major Order):**
  $$\mathbf{\text{Địa chỉ}(a[i][j]) = \text{Base Address} + [i \times C + j] \times S}$$
  *(Trong đó: $i$ là chỉ số hàng, $j$ là chỉ số cột, $C$ là tổng số cột của ma trận, $S = \text{sizeof(kiểu dữ liệu)}$).*

- **Bảng tương đương cú pháp giữa Mảng 2 chiều và Con trỏ:**

| Thao tác | Cú pháp chỉ số mảng (Array Notation) | Cú pháp con trỏ tương đương (Pointer Notation) |
| :--- | :--- | :--- |
| **Địa chỉ của Hàng thứ $i$** | `&a[i]` hoặc `a[i]` | `a + i` |
| **Địa chỉ của phần tử $a[i][j]$** | `&a[i][j]` | `*(a + i) + j` |
| **Giá trị của phần tử $a[i][j]$** | `a[i][j]` | `*(*(a + i) + j)` |

- **Bài toán thi mẫu lần vết vòng lặp lồng nhau duyệt mảng 2 chiều:**
  - *Đoạn mã C:*
    ```c
    int a[2][3] = { {1, 2, 3}, {4, 5, 6} };
    int sum = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            if (a[i][j] % 2 != 0) {
                sum += a[i][j];
            }
        }
    }
    printf("%d", sum);
    ```
  - *Quá trình lần vết:*
    - Duyệt qua tất cả các phần tử của mảng $a$: $1, 2, 3, 4, 5, 6$.
    - Điều kiện `a[i][j] % 2 != 0` lọc ra các số lẻ: $1, 3, 5$.
    - Biến `sum` tính tổng các số lẻ: $\text{sum} = 1 + 3 + 5 = 9$.
    - Kết quả in ra màn hình: `9`.

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Phân biệt Mảng con trỏ (Pointer Array) và Con trỏ mảng (Array Pointer):**
  - **포인터 배열 (Mảng con trỏ):** `int *arr[3];`
    - Do dấu ngoặc vuông `[]` có độ ưu tiên cao hơn dấu sao `*`, đây là một **Mảng gồm 3 phần tử**, mỗi phần tử là một con trỏ kiểu `int*`.
  - **배열 포인터 (Con trỏ mảng):** `int (*arr)[3];`
    - Do có dấu ngoặc tròn `()`, đây là **Một biến con trỏ duy nhất** chuyên trỏ tới một mảng 1 chiều có 3 phần tử số nguyên. Thường dùng làm tham số hàm khi truyền mảng 2 chiều.

### 복습 체크리스트
- [ ] Nhớ mảng trong C/Java được lưu trữ theo quy tắc 행 우선 순서 (Row-Major Order).
- [ ] Tính được địa chỉ phần tử: $\text{Base} + (i \times C + j) \times \text{Size}$.
- [ ] Nhớ biểu thức con trỏ tương đương: `a[i][j] == *(*(a + i) + j)`.
- [ ] Phân biệt được `int *arr[3]` (mảng các con trỏ) và `int (*arr)[3]` (con trỏ trỏ tới mảng).
