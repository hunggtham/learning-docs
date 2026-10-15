# 입력 값의 형변환 (Type Casting)

## 학습 목표 (Mục tiêu)
- Nắm vững sự cần thiết của việc ép kiểu dữ liệu (Type Casting) khi nhận dữ liệu từ hàm `input()`.
- Làm chủ cú pháp ép kiểu đơn lẻ với `int()` và `float()` để thực hiện các phép tính số học chính xác.
- Hiểu rõ cơ chế kết hợp giữa hàm bóc tách chuỗi `split()` và hàm bậc cao `map()` để nhập nhiều biến số trên cùng một dòng.

## 핵심 키워드 (Từ khóa)
- **형변환 (Type Casting)**: Chuyển đổi giữa các kiểu dữ liệu (`str` sang `int`, `float`).
- **`split()`**: Phân tách chuỗi văn bản thành danh sách các chuỗi con dựa trên ký tự phân cách (mặc định là khoảng trắng).
- **`map()` (Ánh xạ hàm)**: Áp dụng một hàm biến đổi lên toàn bộ các phần tử của một tập hợp.
- **Mẹo nhớ M.I.S**: **M**ap - **I**nt - **S**plit (`map(int, input().split())`).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [46-bai-hoc.md](46-bai-hoc.md) (Hàm nhập xuất chuẩn input và print).
- Liên kết với [48-bai-hoc.md](48-bai-hoc.md) (Cấu trúc danh sách List trong Python).
- Liên kết với [04-programming-language/07-bai-hoc.md](../../04-programming-language/lessons/07-bai-hoc.md) (Ép kiểu ngầm định và tường minh trong C/Java).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh tình huống đề bài:
  - Nhập 1 số nguyên trên 1 dòng: `n = int(input())`.
  - Nhập 2 số thực cách nhau bởi dấu cách: `x, y = map(float, input().split())`.
  - Nhập danh sách gồm nhiều số trên 1 dòng: `arr = list(map(int, input().split()))`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các hàm ép kiểu dữ liệu cơ bản
| Hàm ép kiểu | Kiểu đích | Dữ liệu đầu vào ví dụ | Kết quả sau ép kiểu | Hành vi khi lỗi |
| :--- | :--- | :--- | :--- | :--- |
| **`int(x)`** | Số nguyên (`int`) | Chuỗi `"123"` hoặc số thực `3.8` | Số nguyên `123`, số nguyên `3` (cắt bỏ phần thập phân) | `ValueError` nếu chuỗi chứa chữ cái hoặc ký tự không hợp lệ |
| **`float(x)`** | Số thực (`float`) | Chuỗi `"3.14"` hoặc số nguyên `5` | Số thực `3.14`, số thực `5.0` | `ValueError` nếu chuỗi không đúng định dạng số |
| **`str(x)`** | Chuỗi ký tự (`str`) | Số `100` hoặc biểu thức logic `True` | Chuỗi `"100"`, chuỗi `"True"` | Luôn chuyển đổi an toàn mọi đối tượng |

#### 2. Kỹ thuật nhập nhiều giá trị với `map()` và `split()`
- **Cú pháp chuẩn**:
  ```python
  a, b = map(int, input().split())
  ```
- **Quy trình thực thi 4 bước bên dưới tầng thông dịch**:
  1. Người dùng nhập từ bàn phím chuỗi: `"10 20"` $\rightarrow$ `input()` nhận vào chuỗi `"10 20"`.
  2. Hàm `split()` tự động phân tách theo khoảng trắng $\rightarrow$ Sinh ra danh sách chuỗi con: `['10', '20']`.
  3. Hàm `map(int, ...)` duyệt qua từng phần tử và gọi hàm `int()` $\rightarrow$ Tạo ra chuỗi các số nguyên: `10, 20`.
  4. Cơ chế Unpacking phân rã các giá trị gán tương ứng vào hai biến: `a = 10` và `b = 20`.

#### 3. Ví dụ bài toán thi thực tế
```python
# Đề bài: Nhập vào 2 số nguyên a và b trên một dòng, in ra tổng của chúng
a, b = map(int, input().split())
print(a + b) # Nếu nhập "15 25", in ra màn hình: 40
```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Nhập một mảng gồm $N$ số nguyên trên một dòng
- Trong các đề thi lập trình giải thuật, đầu vào thường cho một dãy số cách nhau bởi dấu cách:
  ```python
  # Nhập cả dòng và chuyển thẳng thành List số nguyên:
  numbers = list(map(int, input().split()))
  print(sum(numbers)) # Tính tổng toàn bộ các phần tử trong danh sách
  ```

#### 2. Tùy biến dấu phân cách với tham số trong `split()`
- Theo mặc định, `split()` coi mọi khoảng trắng liên tiếp (dấu cách, dấu tab, dấu xuống dòng) là một phân tách.
- Nếu dữ liệu được phân cách bằng dấu phẩy `,` hoặc dấu hai chấm `:`:
  ```python
  # Dữ liệu vào: "2026,10,15"
  year, month, day = map(int, input().split(','))
  print(f"Năm {year} Tháng {month} Ngày {day}")
  ```

---

### 복습 체크리스트
- [ ] Tại sao không thể thực hiện phép cộng số học ngay với kết quả trả về của hàm `input()`?
- [ ] Cú pháp `map(int, input().split())` bao gồm những bước xử lý nào từ trong ra ngoài?
- [ ] Hàm `int(3.9)` trong Python sẽ cho kết quả là `3` hay `4`?
- [ ] Để lưu toàn bộ dãy số nhập vào từ một dòng thành một cấu trúc List trong Python, ta dùng cú pháp nào?
