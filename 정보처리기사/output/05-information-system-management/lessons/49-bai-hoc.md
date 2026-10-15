# 슬라이스 (Slice)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp cắt lát toàn diện trong Python: `seq[start:end:step]` trên chuỗi ký tự (String) và danh sách (List).
- Hiểu rõ nguyên lý loại trừ điểm kết thúc (Exclusive: chỉ lấy đến vị trí $\text{end} - 1$).
- Làm chủ kỹ thuật chỉ số âm (Negative Indexing) và bước nhảy âm (`step < 0`) để đảo ngược danh sách hoặc duyệt ngược dữ liệu.

## 핵심 키워드 (Từ khóa)
- **슬라이싱 (Slicing)**: Kỹ thuật trích xuất tập con từ chuỗi hoặc danh sách tuần tự.
- **`start : end : step`**: Ba tham số xác định vị trí bắt đầu, vị trí kết thúc và bước nhảy.
- **끝 위치 제외 (Exclusive End)**: Điểm kết thúc luôn lấy đến `end - 1`.
- **음수 스텝 (Negative Step - `[::-1]`)**: Đảo ngược thứ tự các phần tử trong danh sách hoặc ký tự trong chuỗi.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [48-bai-hoc.md](48-bai-hoc.md) (Cấu trúc danh sách List trong Python).
- Liên kết với [45-bai-hoc.md](45-bai-hoc.md) (Cú pháp cơ bản của Python).
- Liên kết với [42-bai-hoc.md](42-bai-hoc.md) (Thao tác chuỗi trong ngôn ngữ C).

## 읽는 방법 (Cách đọc)
- Nhớ quy tắc "Đầu lấy, Cuối bỏ":
  - `a[1:4]` lấy các chỉ số: $1, 2, 3$.
  - Nếu `start` bị bỏ trống: Mặc định tính từ vị trí đầu tiên ($0$).
  - Nếu `end` bị bỏ trống: Mặc định tính đến hết phần tử cuối cùng của mảng.
  - Cứ thấy `[::-1]` là biết ngay mục đích đoạn mã nhằm **đảo ngược chuỗi/danh sách**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cú pháp và ý nghĩa các tham số Slicing
$$\text{kết\_quả} = \text{danh\_sách}[\text{start} : \text{end} : \text{step}]$$

| Thành phần | Khi bỏ trống mặc định | Quy tắc hành vi | Ví dụ với `a = ['a', 'b', 'c', 'd', 'e']` | Kết quả |
| :--- | :--- | :--- | :--- | :--- |
| **`start`** | `0` (nếu `step > 0`) | Chỉ số bắt đầu trích xuất (bao gồm phần tử này) | `a[1:]` | `['b', 'c', 'd', 'e']` |
| **`end`** | Độ dài danh sách | Điểm dừng trích xuất (**không bao gồm** phần tử này) | `a[:3]` | `['a', 'b', 'c']` |
| **`step`** | `1` | Số bước nhảy giữa các phần tử tiếp theo | `a[0:5:2]` | `['a', 'c', 'e']` |
| **`[::-1]`** | Toàn bộ danh sách | Duyệt lùi từ cuối về đầu mảng | `a[::-1]` | `['e', 'd', 'c', 'b', 'a']` |

#### 2. Kỹ thuật chỉ số âm (Negative Indexing)
- Trong Python, phần tử cuối cùng mang chỉ số `-1`, phần tử kế cuối mang chỉ số `-2`:
  ```python
  text = "HELLO"
  #  Chỉ số dương:   0    1    2    3    4
  #  Ký tự:         'H'  'E'  'L'  'L'  'O'
  #  Chỉ số âm:    -5   -4   -3   -2   -1

  print(text[-3:])  # Lấy 3 ký tự cuối cùng: "LLO"
  print(text[:-1])  # Lấy từ đầu đến sát ký tự cuối cùng: "HELL"
  ```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Bài toán lần vết đề thi Kỹ sư xử lý thông tin
```python
nums = [10, 20, 30, 40, 50, 60]
sub1 = nums[1:5:2] # Lấy từ chỉ số 1 đến 4 với bước nhảy 2:
                   # Chỉ số 1 (20), Chỉ số 3 (40) -> sub1 = [20, 40]

sub2 = nums[-2::-2] # Bắt đầu từ chỉ số -2 (50), lùi về trước mỗi lần 2 bước:
                    # Chỉ số -2 (50), Chỉ số -4 (30), Chỉ số -6 (10) -> sub2 = [50, 30, 10]

print(sub1[0] + sub2[1]) # 20 + 30 = 50
```

#### 2. Tính chất tạo bản sao (Shallow Copy) của Slice
- Thao tác `copy_list = original[:]` sẽ tạo ra một bản sao nông (Shallow Copy) độc lập của danh sách. Khi sửa đổi các phần tử của `copy_list`, danh sách `original` sẽ không bị ảnh hưởng.

---

### 복습 체크리스트
- [ ] Cho danh sách `a = [1, 2, 3, 4, 5]`, biểu thức `a[1:4]` trả về kết quả nào?
- [ ] Tham số `step` mang giá trị âm sẽ thay đổi chiều duyệt của danh sách như thế nào?
- [ ] Biểu thức `s[::-1]` trên chuỗi `s = "PYTHON"` cho ra kết quả gì?
- [ ] Trong chuỗi văn bản gồm $N$ ký tự, ký tự cuối cùng có thể được truy cập thông qua chỉ số âm nào?
