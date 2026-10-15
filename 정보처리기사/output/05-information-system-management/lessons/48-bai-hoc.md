# Python 자료구조 (Data Structures): 리스트와 딕셔너리

## 학습 목표 (Mục tiêu)
- Nắm vững cấu trúc, tính chất khả biến (Mutable) và phương thức thao tác trên cấu trúc dữ liệu danh sách `List` trong Python.
- Hiểu rõ bản chất ánh xạ cặp Khóa - Giá trị (Key-Value pairs) của cấu trúc `Dictionary` và yêu cầu tính bất biến của Khóa.
- Sử dụng thành thạo các hàm và phương thức tích hợp sẵn phổ biến (`append`, `pop`, `insert`, `keys`, `values`, `items`) trong các bài toán thi thực hành.

## 핵심 키워드 (Từ khóa)
- **리스트 (List - `[]`)**: Cấu trúc dữ liệu có thứ tự, kích thước co giãn động, cho phép chứa phần tử hỗn hợp nhiều kiểu.
- **딕셔너리 (Dictionary - `{}`)**: Bảng băm lưu trữ theo cặp Key-Value, tra cứu siêu tốc độ phức tạp trung bình $O(1)$.
- **List Methods**: `append()`, `insert()`, `pop()`, `remove()`, `sort()`.
- **Dict Methods**: `keys()`, `values()`, `items()`, `get()`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [45-bai-hoc.md](45-bai-hoc.md) (Tổng quan 4 cấu trúc tập hợp trong Python).
- Liên kết với [49-bai-hoc.md](49-bai-hoc.md) (Kỹ thuật cắt lát danh sách).
- Liên kết với [04-programming-language/41-bai-hoc.md](../../04-programming-language/lessons/41-bai-hoc.md) (So sánh cấu trúc mảng tĩnh trong C).

## 읽는 방법 (Cách đọc)
- Phân biệt nhanh hai cấu trúc:
  - Cần danh sách có thứ tự, đánh số bằng chỉ số nguyên ($0, 1, 2\dots$) $\rightarrow$ Dùng **List (`[]`)**.
  - Cần tra cứu dữ liệu theo tên gọi hoặc khóa tùy ý (như tra cứu mã nhân viên $\rightarrow$ tên) $\rightarrow$ Dùng **Dictionary (`{}`)**.
  - Chú ý: Khóa (Key) trong Dictionary bắt buộc phải là kiểu **bất biến (Immutable)** như `int`, `str`, `tuple`. Không thể dùng `list` làm Key!

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cấu trúc Danh sách (List)
- **Cú pháp khởi tạo**: `arr = [10, "Python", 3.14, True]` (hỗ trợ nhiều kiểu dữ liệu trong cùng một danh sách).
- **Các phương thức chỉnh sửa danh sách thông dụng**:
  | Phương thức | Tác vụ thực hiện | Ví dụ với `a = [10, 20]` | Kết quả |
  | :--- | :--- | :--- | :--- |
  | **`append(x)`** | Thêm phần tử `x` vào cuối danh sách | `a.append(30)` | `[10, 20, 30]` |
  | **`insert(idx, x)`** | Chèn phần tử `x` vào đúng vị trí chỉ số `idx` | `a.insert(1, 15)` | `[10, 15, 20]` |
  | **`pop()`** | Xóa và trả về phần tử nằm ở cuối cùng | `val = a.pop()` | `val = 20`, `a = [10]` |
  | **`remove(x)`** | Tìm và xóa phần tử đầu tiên có giá trị bằng `x` | `a.remove(10)` | `[20]` |
  | **`sort()`** | Sắp xếp các phần tử tăng dần tại chỗ | `[3, 1, 2].sort()` | `[1, 2, 3]` |

#### 2. Cấu trúc Từ điển (Dictionary)
- **Cú pháp khởi tạo**: `student = {"id": 101, "name": "Kim", "score": 90}`
- **Truy xuất và bổ sung dữ liệu**:
  - Đọc giá trị: `student["name"]` $\rightarrow$ Trả về `"Kim"`. (Nếu khóa không tồn tại sẽ báo lỗi `KeyError`).
  - Đọc an toàn: `student.get("age", 0)` $\rightarrow$ Trả về giá trị mặc định `0` nếu không tìm thấy khóa `"age"`.
  - Thêm mới hoặc cập nhật: `student["grade"] = "A"` (nếu có rồi sẽ ghi đè, chưa có sẽ thêm mới).
  - Xóa phần tử: `del student["score"]`
- **Các hàm duyệt Dictionary**:
  - `student.keys()`: Trả về danh sách tất cả các Khóa.
  - `student.values()`: Trả về danh sách tất cả các Giá trị.
  - `student.items()`: Trả về danh sách các bộ `(Key, Value)`.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Duyệt Dictionary bằng vòng lặp for
```python
scores = {"Toán": 90, "Văn": 85, "Anh": 95}

# Duyệt lấy cả Khóa và Giá trị đồng thời:
for subject, point in scores.items():
    print(f"Môn {subject}: {point} điểm")
```

#### 2. Lần vết đoạn mã đề thi Kỹ sư xử lý thông tin
```python
data = [10, 20, 30]
data.append(40)      # data = [10, 20, 30, 40]
data.insert(1, 15)   # data = [10, 15, 20, 30, 40]
x = data.pop()       # x = 40, data = [10, 15, 20, 30]
print(x + data[1])   # 40 + 15 = 55
```

---

### 복습 체크리스트
- [ ] Điểm khác nhau giữa phương thức `append()` và `insert()` trong List là gì?
- [ ] Tại sao không thể sử dụng một `List` để làm Khóa (Key) trong Dictionary của Python?
- [ ] Cú pháp `student.get("phone", "Chưa có")` khác gì so với `student["phone"]` khi không có khóa `"phone"`?
- [ ] Phương thức `items()` của Dictionary trả về cấu trúc dữ liệu như thế nào?
