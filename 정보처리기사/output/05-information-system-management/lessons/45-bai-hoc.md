# Python의 기본 문법 (Cú pháp Cơ bản Ngôn ngữ Python)

## 학습 목표 (Mục tiêu)
- Nắm vững các đặc trưng kiến trúc của Python: Định kiểu động (Dynamic Typing), cú pháp không dùng chấm phẩy `;`, phân khối lệnh bằng thụt lề (Indentation).
- Thành thạo kỹ thuật gán đồng thời (Multiple Assignment) và hoán đổi giá trị biến không cần biến trung gian (`x, y = y, x`).
- Phân biệt 4 kiểu cấu trúc dữ liệu tập hợp chuẩn trong Python: List, Tuple, Set, Dictionary về tính khả biến (Mutability) và thứ tự.
- Làm chủ kỹ thuật cắt lát dữ liệu (Slicing: `start:end:step`) thường xuyên xuất hiện trong phần đọc hiểu mã nguồn đề thi.

## 핵심 키워드 (Từ khóa)
- **동적 타이핑 (Dynamic Typing)**: Không cần khai báo kiểu dữ liệu, tự động suy luận kiểu lúc runtime.
- **들여쓰기 (Indentation)**: Dùng khoảng trắng (chuẩn 4 spaces) và dấu hai chấm `:` thay cho cặp ngoặc `{}`.
- **다중 할당 (Multiple Assignment)**: `a, b = 10, 20`, hoán đổi giá trị tức thì `a, b = b, a`.
- **4대 컬렉션 (Collections)**: List (`[]` - mutable), Tuple (`()` - immutable), Set (`{}` - unique), Dictionary (`{k: v}`).
- **슬라이싱 (Slicing)**: Cú pháp trích xuất mảng con `arr[start:end:step]`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [40-bai-hoc.md](40-bai-hoc.md) (Câu lệnh rẽ nhánh và vòng lặp).
- Liên kết với [41-bai-hoc.md](41-bai-hoc.md) (Mảng và danh sách).
- Liên kết với [04-programming-language/72-bai-hoc.md](../../04-programming-language/lessons/72-bai-hoc.md) (Đặc tính các ngôn ngữ thông dịch).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý các bẫy cú pháp Python:
  - Cắt lát `a[1:4]`: Lấy từ chỉ số 1 đến chỉ số $4 - 1 = 3$ (chỉ số kết thúc luôn là Exclusive).
  - Bước nhảy âm `a[::-1]`: Đảo ngược toàn bộ chuỗi hoặc danh sách.
  - Cố gắng thay đổi phần tử của Tuple: `t = (1, 2); t[0] = 5;` $\rightarrow$ **TypeError** (Tuple là bất biến - Immutable).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Các đặc tính cú pháp cơ bản của Python
- **Không khai báo kiểu dữ liệu**: Biến được tạo ra tự động ngay khi gán giá trị lần đầu tiên (`x = 10` biến `x` có kiểu int, sau đó `x = "Hello"` biến `x` chuyển thành kiểu str).
- **Phân tách câu lệnh và khối mã**:
  - Không cần sử dụng dấu chấm phẩy `;` ở cuối câu (mỗi dòng lệnh tương ứng một phát biểu).
  - Sử dụng dấu hai chấm `:` ở cuối dòng lệnh điều khiển (`if`, `for`, `while`, `def`) và **thụt lề thống nhất (Indentation)** để xác định khối mã thay vì dùng `{}`.
- **Gán giá trị đồng thời (Unpacking)**:
  ```python
  x, y, z = 10, 20, 30       # Gán đồng thời 3 giá trị cho 3 biến
  x, y = y, x                # Hoán đổi giá trị của x và y tức thì mà không cần biến tạm temp
  ```

#### 2. Bảng so sánh 4 kiểu tập hợp dữ liệu tiêu chuẩn
| Cấu trúc (Type) | Ký hiệu khai báo | Có thứ tự (Ordered) | Trùng lặp phần tử | Tính khả biến (Mutable) | Ví dụ minh họa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List (Danh sách)** | Cặp ngoặc vuông `[]` | **Có** | **Cho phép** | **Có (Sửa được)** | `a = [1, 2, 2, 3]` |
| **Tuple (Bộ giá trị)** | Cặp ngoặc tròn `()` | **Có** | **Cho phép** | **Không (Bất biến)** | `b = (1, 2, 3)` |
| **Set (Tập hợp)** | Cặp ngoặc nhọn `{}` | **Không** | **Loại trừ trùng lặp** | **Có (Thêm/xóa)** | `c = {1, 2, 2} -> {1, 2}` |
| **Dictionary (Từ điển)** | Cặp ngoặc nhọn `{k: v}` | Có (từ Python 3.7) | Key không được trùng | **Có (Sửa value)** | `d = {"a": 1, "b": 2}` |

#### 3. Kỹ thuật cắt lát (Slicing) danh sách và chuỗi
- Cú pháp: `tên_biến[start : end : step]`
  - `start`: Chỉ số bắt đầu (mặc định là 0, bao gồm phần tử này).
  - `end`: Chỉ số kết thúc (mặc định là độ dài mảng, **không bao gồm** phần tử này).
  - `step`: Bước nhảy (mặc định là 1; nếu âm sẽ duyệt ngược từ phải sang trái).
- *Ví dụ minh họa thường gặp*:
  ```python
  s = "PYTHON"
  print(s[1:4])   # "YTH" (Lấy chỉ số 1, 2, 3)
  print(s[:3])    # "PYT" (Lấy từ đầu đến chỉ số 2)
  print(s[2:])    # "THON" (Lấy từ chỉ số 2 đến hết)
  print(s[::-1])  # "NOHTYP" (Đảo ngược chuỗi)
  ```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán lần vết đề thi Kỹ sư xử lý thông tin với List & Loop
```python
a = [10, 20, 30, 40, 50]
total = 0
for i in range(1, 4): # range(1, 4) sinh ra các giá trị i: 1, 2, 3
    total += a[i]     # total = a[1] + a[2] + a[3] = 20 + 30 + 40 = 90
print(total)          # Kết quả in ra màn hình: 90
```

#### 2. Kỹ thuật List Comprehension trong Python
- Cú pháp tạo danh sách ngắn gọn một dòng:
  ```python
  # Tạo danh sách bình phương các số chẵn từ 1 đến 5
  evens_squared = [x**2 for x in range(1, 6) if x % 2 == 0]
  # Kết quả: [4, 16] (với x = 2 và x = 4)
  ```

---

### 복습 체크리스트
- [ ] Quy tắc thụt lề (Indentation) trong Python thay thế cho thành phần cú pháp nào trong ngôn ngữ C/Java?
- [ ] Làm thế nào để hoán đổi giá trị của hai biến `a` và `b` trong Python chỉ bằng một dòng lệnh?
- [ ] Điểm khác biệt quan trọng nhất giữa List và Tuple trong Python là gì?
- [ ] Đoạn mã `nums = [10, 20, 30, 40, 50]; print(nums[1:4])` sẽ in ra danh sách con gồm những phần tử nào?
