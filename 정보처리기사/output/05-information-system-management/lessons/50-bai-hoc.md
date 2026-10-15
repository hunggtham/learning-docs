# Python 제어문: if문, for문 (Cấu trúc Điều khiển: if, for trong Python)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp câu lệnh điều kiện rẽ nhánh trong Python: `if`, `elif`, `else` và sự khác biệt với `else if` trong C/Java.
- Hiểu rõ nguyên lý hoạt động của hàm sinh dãy số `range(start, stop, step)` và quy tắc loại trừ giá trị cận trên `stop`.
- Thành thạo hai cách duyệt vòng lặp `for`: Duyệt theo chỉ số biến đếm với `range` và duyệt trực tiếp trên các phần tử của tập hợp dữ liệu (List, String).

## 핵심 키워드 (Từ khóa)
- **`if - elif - else`**: Cấu trúc rẽ nhánh điều kiện trong Python (chú ý từ khóa `elif`).
- **`range(start, stop, step)`**: Hàm sinh dãy số tuần tự, dừng lại tại $\text{stop} - 1$.
- **컬렉션 순회 (Collection Traversal)**: Duyệt trực tiếp `for x in list:` không cần biến đếm chỉ số.
- **`for - else`**: Khối lệnh `else` chỉ thực thi khi vòng lặp `for` chạy xong trọn vẹn mà không gặp lệnh `break`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [40-bai-hoc.md](40-bai-hoc.md) (Câu lệnh break và continue).
- Liên kết với [48-bai-hoc.md](48-bai-hoc.md) (Duyệt các phần tử của List và Dictionary).
- Liên kết với [53-bai-hoc.md](53-bai-hoc.md) (Vòng lặp while trong Python).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh tham số của hàm `range()`:
  - `range(5)` $\rightarrow$ Sinh ra 5 số: $0, 1, 2, 3, 4$ (bắt đầu từ 0).
  - `range(1, 6)` $\rightarrow$ Sinh ra các số: $1, 2, 3, 4, 5$ (dừng trước 6).
  - `range(1, 10, 2)` $\rightarrow$ Sinh ra các số lẻ: $1, 3, 5, 7, 9$.
  - `range(5, 0, -1)` $\rightarrow$ Đếm lùi: $5, 4, 3, 2, 1$ (dừng trước 0).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Câu lệnh điều kiện `if - elif - else`
- **Cú pháp chuẩn**:
  ```python
  if score >= 90:
      grade = 'A'
  elif score >= 80:     # Chú ý: viết là elif, không phải else if như trong C/Java
      grade = 'B'
  else:
      grade = 'C'
  ```
- **Toán tử ba ngôi (Ternary Operator) một dòng trong Python**:
  ```python
  status = "Đỗ" if score >= 60 else "Trượt"
  ```

#### 2. Vòng lặp `for` và hàm sinh số `range()`
| Dạng cú pháp | Dãy số sinh ra | Ý nghĩa hoạt động |
| :--- | :--- | :--- |
| **`range(stop)`** | $0, 1, \dots, \text{stop} - 1$ | Bắt đầu mặc định từ 0, bước tăng 1 |
| **`range(start, stop)`** | $\text{start}, \dots, \text{stop} - 1$ | Bắt đầu từ `start`, dừng trước `stop` |
| **`range(start, stop, step)`** | $\text{start}, \text{start}+\text{step}, \dots$ | Bước nhảy tùy biến theo `step` |

#### 3. Hai dạng duyệt vòng lặp `for` thông dụng
- **Dạng 1: Lặp theo số lần với `range()`**:
  ```python
  total = 0
  for i in range(1, 6): # i chạy từ 1 đến 5
      total += i
  print(total) # 1 + 2 + 3 + 4 + 5 = 15
  ```
- **Dạng 2: Duyệt trực tiếp trên danh sách**:
  ```python
  fruits = ["Cam", "Táo", "Xoài"]
  for item in fruits:
      print(item, end=' ') # In ra: Cam Táo Xoài
  ```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cấu trúc độc đáo: `for - else` trong Python
```python
# Tìm kiếm số nguyên tố
n = 7
for i in range(2, n):
    if n % i == 0:
        print("Không phải số nguyên tố")
        break
else:
    # Khối else này CHỈ CHẠY khi vòng lặp kết thúc tự nhiên mà không bị break!
    print(f"{n} là số nguyên tố")
```

#### 2. Hàm `enumerate()` lấy đồng thời Chỉ số và Giá trị
- Khi cần biết cả vị trí thứ tự index lẫn giá trị của phần tử:
  ```python
  colors = ["Red", "Green", "Blue"]
  for idx, color in enumerate(colors):
      print(f"Vị trí {idx}: {color}")
  # Vị trí 0: Red
  # Vị trí 1: Green
  # Vị trí 2: Blue
  ```

---

### 복습 체크리스트
- [ ] Từ khóa nào được dùng trong Python để biểu diễn nhánh điều kiện bổ sung thay cho `else if`?
- [ ] Vòng lặp `for i in range(2, 8, 2):` sẽ gán những giá trị nào cho biến `i`?
- [ ] Trong cấu trúc `for - else`, khi nào thì khối lệnh nằm trong `else` sẽ được kích hoạt thực thi?
- [ ] Hàm `enumerate()` mang lại lợi ích gì so với việc duyệt danh sách thông thường?
