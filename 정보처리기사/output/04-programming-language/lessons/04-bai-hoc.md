# 233. C/C++의 데이터 타입 크기 (Data Type Sizes in C/C++)

## 학습 목표 (Mục tiêu)
- Nắm vững kích thước bộ nhớ (Dung lượng tính theo Byte) và dải giá trị biểu diễn của các kiểu dữ liệu cơ bản trong ngôn ngữ lập trình C/C++.
- Ghi nhớ chính xác số byte chiếm dụng của từng kiểu: `char` (1 Byte), `short` (2 Bytes), `int` (4 Bytes), `long` (4 Bytes trên 32-bit/LLP64), `long long` (8 Bytes), `float` (4 Bytes), và `double` (8 Bytes).
- Hiểu cách sử dụng toán tử `sizeof` trong C để xác định kích thước bộ nhớ thực tế của biến hoặc kiểu dữ liệu trên môi trường biên dịch.

## 핵심 키워드 (Từ khóa)
- C/C++ 데이터 타입 크기 (Data Type Sizes)
- sizeof 연산자 (sizeof Operator)
- 문자형 (char / 1바이트 / ASCII 코드)
- 정수형 (short 2B, int 4B, long 4B, long long 8B)
- 실수형 (float 4B, double 8B)
- 부호 있는/없는 정수 (signed vs unsigned)

## 선행·연결 개념 (Kiến thức liên kết)
- [03-bai-hoc.md](03-bai-hoc.md): Kiểu dữ liệu, biến và toán tử.
- [05-bai-hoc.md](05-bai-hoc.md): Kích thước các kiểu dữ liệu trong Java (So sánh đối ứng).
- [정보처리기사/output/02-software-development/lessons/83-bai-hoc.md](../../02-software-development/lessons/83-bai-hoc.md): Kiến trúc bộ nhớ bán dẫn RAM.

## 읽는 방법 (Cách đọc)
- Ghi nhớ theo nấc lũy thừa của 2:
  - 1 Byte: `char` (Dùng lưu trữ 1 ký tự chuẩn mã ASCII).
  - 2 Bytes: `short` (Số nguyên ngắn).
  - 4 Bytes: `int`, `long` (Số nguyên chuẩn), `float` (Số thực chính xác đơn 32 bits).
  - 8 Bytes: `long long` (Số nguyên dài 64 bits), `double` (Số thực chính xác kép 64 bits).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng kích thước và dải giá trị các kiểu dữ liệu trong C/C++:**

| Kiểu dữ liệu | Kích thước (Bytes) | Số bits | Dải giá trị biểu diễn (Signed) | Mô tả ứng dụng chuẩn |
| :--- | :--- | :--- | :--- | :--- |
| **`char`** | **1 Byte** | 8 bits | -128 đến 127 (hoặc 0 đến 255 nếu `unsigned`) | Ký tự đơn trong bảng mã ASCII |
| **`short`** | **2 Bytes** | 16 bits | -32,768 đến 32,767 | Số nguyên ngắn, tiết kiệm bộ nhớ |
| **`int`** | **4 Bytes** | 32 bits | Khoảng -2.14 tỷ đến +2.14 tỷ | Kiểu số nguyên mặc định thông dụng nhất |
| **`long`** | **4 Bytes** | 32 bits | Tương tự `int` trên môi trường 32-bit tiêu chuẩn | Số nguyên dài chuẩn C truyền thống |
| **`long long`** | **8 Bytes** | 64 bits | Khoảng $-9 \times 10^{18}$ đến $+9 \times 10^{18}$ | Số nguyên siêu lớn cho các bài toán tính toán lớn |
| **`float`** | **4 Bytes** | 32 bits | Khoảng $\pm 3.4 \times 10^{-38}$ đến $\pm 3.4 \times 10^{38}$ | Số thực độ chính xác đơn (7 chữ số có nghĩa) |
| **`double`** | **8 Bytes** | 64 bits | Khoảng $\pm 1.7 \times 10^{-308}$ đến $\pm 1.7 \times 10^{308}$ | Số thực độ chính xác kép (15 chữ số có nghĩa) |

- **Từ khóa `unsigned` trong C:**
  - Khi thêm tiền tố `unsigned` trước kiểu số nguyên (ví dụ: `unsigned int`), bit dấu cao nhất (Most Significant Bit - MSB) được chuyển thành bit biểu diễn độ lớn.
  - Kết quả: Dải giá trị chuyển thành toàn số dương, gấp đôi cận trên:
    - `unsigned char`: 0 đến 255.
    - `unsigned short`: 0 đến 65,535.
    - `unsigned int`: 0 đến khoảng 4.29 tỷ ($2^{32} - 1$).

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Toán tử `sizeof`:**
  - `sizeof` là một toán tử thời gian biên dịch (Compile-time Operator), không phải hàm số.
  - Cú pháp: `sizeof(int)` hoặc `sizeof(biến)`.
  - Kết quả trả về là số lượng byte mà đối tượng chiếm dụng trong bộ nhớ RAM.
  - Ví dụ: `int arr[5]; sizeof(arr);` sẽ trả về giá trị là $5 \times 4 = 20$ bytes.

### 복습 체크리스트
- [ ] Nhớ chính xác kích thước: char (1B), short (2B), int (4B), long long (8B), float (4B), double (8B).
- [ ] Nhớ `unsigned` chỉ dùng cho số dương, giúp gấp đôi giá trị cực đại của kiểu nguyên.
- [ ] Biết cách tính kích thước mảng bằng toán tử `sizeof(arr)`.
