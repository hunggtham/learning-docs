# 핵심 258, 259, 260: 배열 (Array)

## 학습 목표 (Mục tiêu)
- Nắm vững khái niệm mảng (Array), tính chất vùng nhớ liên tục và quy tắc đánh chỉ số bắt đầu từ 0 (0-based indexing) trong ngôn ngữ C và Java.
- Hiểu rõ các quy tắc khởi tạo mảng 1 chiều và cơ chế tự động điền giá trị 0 cho các phần tử còn thiếu.
- Phân tích cấu trúc mảng 2 chiều, thứ tự lưu trữ theo hàng (Row-Major Order) và quy tắc bỏ trống chỉ số khi khởi tạo.

## 핵심 키워드 (Từ khóa)
- **배열 (Array)**: Cùng kiểu dữ liệu, lưu trữ trên vùng nhớ vật lý liên tục, truy xuất ngẫu nhiên $O(1)$.
- **0-based Indexing**: Chỉ số phần tử bắt đầu từ 0 đến $N - 1$.
- **자동 0 초기화 (Auto Zero Fill)**: Khi khai báo kích thước lớn hơn số lượng phần tử khởi tạo, phần tử thừa tự động mang giá trị 0.
- **2차원 배열 (2D Array)**: Cấu trúc Hàng (Row) và Cột (Col), lưu trữ theo Row-Major trong C.
- **크기 생략 규칙 (Omission Rule)**: Được phép bỏ trống kích thước hàng (dòng) đầu tiên nhưng bắt buộc phải khai báo kích thước cột.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [40-bai-hoc.md](40-bai-hoc.md) (Câu lệnh điều khiển lặp duyệt mảng).
- Liên kết với [42-bai-hoc.md](42-bai-hoc.md) (Mảng ký tự và chuỗi trong C).
- Liên kết với [44-bai-hoc.md](44-bai-hoc.md) (Mối liên hệ giữa Con trỏ và Mảng).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý các bẫy khai báo mảng trong C:
  - `int a[5] = {1, 2};` $\rightarrow$ `a[0]=1, a[1]=2, a[2]=0, a[3]=0, a[4]=0`. Không phải mang giá trị rác!
  - `int a[][3] = {{1, 2}, {3, 4, 5}};` $\rightarrow$ Hợp lệ! Số hàng tự tính là 2, các phần tử thiếu tự điền 0 (`a[0][2]=0`).
  - `int a[2][] = ...;` $\rightarrow$ **LỖI BIÊN DỊCH** (Cột bắt buộc phải có kích thước).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Mảng một chiều (1D Array)
- **Khái niệm**: Cấu trúc dữ liệu tuyến tính lưu trữ các phần tử có cùng kiểu dữ liệu tại các ô nhớ nằm liền kề nhau trong bộ nhớ máy tính.
- **Cú pháp khai báo và cấp phát**: `자료형 배열명[크기];` (Ví dụ: `int a[5];` chiếm $5 \times 4 = 20$ bytes bộ nhớ).
- **Quy tắc khởi tạo giá trị**:
  - `int a[5] = {10, 20, 30, 40, 50};` $\rightarrow$ Khởi tạo đủ 5 phần tử.
  - `int a[5] = {10, 20};` $\rightarrow$ Phần tử `a[0]=10, a[1]=20`, ba phần tử còn lại `a[2], a[3], a[4]` đều tự động mang giá trị **0**.
  - `int a[] = {1, 2, 3};` $\rightarrow$ Tự động xác định kích thước mảng là 3 phần tử.
  - `int a[5];` (khai báo cục bộ không gán giá trị) $\rightarrow$ Chứa **giá trị rác (Garbage Value)** không xác định.

#### 2. Mảng hai chiều (2D Array)
- **Khái niệm**: Mảng của các mảng, được tổ chức logic dưới dạng bảng gồm các Hàng (Row) và Cột (Column).
- **Cú pháp khai báo**: `자료형 배열명[행크기][열크기];`
  - Ví dụ: `int a[2][3];` $\rightarrow$ Mảng gồm 2 hàng và 3 cột, tổng cộng $2 \times 3 = 6$ phần tử.
- **Thứ tự lưu trữ trong bộ nhớ (Row-Major Order)**:
  - Trong ngôn ngữ C và Java, mảng 2 chiều được lưu trữ liên tục trên RAM theo từng hàng một (hết hàng 0 đến hàng 1):
  $$\text{Vị trí ô nhớ: } a[0][0] \rightarrow a[0][1] \rightarrow a[0][2] \rightarrow a[1][0] \rightarrow a[1][1] \rightarrow a[1][2]$$
- **Quy tắc bỏ trống chỉ số kích thước**:
  - Khi khởi tạo mảng 2 chiều đồng thời gán dữ liệu, **có thể bỏ trống kích thước hàng thứ nhất**, nhưng **bắt buộc phải chỉ định kích thước cột**:
  - Hợp lệ: `int a[][3] = {1, 2, 3, 4, 5, 6};` (Trình biên dịch tự tính ra 2 hàng).
  - Không hợp lệ: `int a[2][] = ...;` hoặc `int a[][] = ...;` (Gây lỗi biên dịch).

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Công thức tính địa chỉ ô nhớ của phần tử mảng 2 chiều
- Gọi:
  - $\text{BaseAddress}$: Địa chỉ ô nhớ bắt đầu của mảng (địa chỉ của `a[0][0]`).
  - $R$: Số hàng, $C$: Số cột của mảng (`int a[R][C]`).
  - $S$: Kích thước (số byte) của một phần tử dữ liệu (với kiểu `int` là 4 bytes).
- Địa chỉ ô nhớ của phần tử tại vị trí hàng $i$, cột $j$ ($a[i][j]$) theo thứ tự ưu tiên hàng (Row-Major) được tính bằng công thức:
  $$\text{Address}(a[i][j]) = \text{BaseAddress} + (i \times C + j) \times S$$
- *Ví dụ*: Mảng `int a[3][4]` bắt đầu tại địa chỉ $1000$. Địa chỉ của phần tử `a[2][1]` là:
  $$\text{Address}(a[2][1]) = 1000 + (2 \times 4 + 1) \times 4 = 1000 + 9 \times 4 = 1036$$

#### 2. Bài toán duyệt mảng 2 chiều tính tổng đường chéo
```c
#include <stdio.h>
int main() {
    int arr[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int diag_sum = 0;
    for(int i = 0; i < 3; i++) {
        diag_sum += arr[i][i]; // Cộng các phần tử trên đường chéo chính: 1 + 5 + 9
    }
    printf("Tổng đường chéo = %d\n", diag_sum); // In ra: 15
    return 0;
}
```

---

### 복습 체크리스트
- [ ] Khi khai báo mảng `int a[10] = {5, 10};` trong C, các phần tử từ `a[2]` đến `a[9]` mang giá trị gì?
- [ ] Tại sao khi khai báo và khởi tạo mảng 2 chiều trong C, ta không được phép bỏ trống kích thước cột?
- [ ] Trong kiến trúc máy tính, việc các phần tử của mảng được xếp trên các ô nhớ liên tục mang lại lợi ích gì cho bộ nhớ đệm (Cache Locality)?
- [ ] Với mảng `int a[3][5]`, hãy tính vị trí tuyến tính tương đối của phần tử `a[2][3]`?
