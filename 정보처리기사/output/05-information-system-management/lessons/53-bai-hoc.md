# Python 제어문: while문 (Vòng lặp while trong Python)

## 학습 목표 (Mục tiêu)
- Nắm vững cú pháp và luồng điều khiển của vòng lặp `while` trong Python.
- Hiểu rõ cơ chế kiểm tra điều kiện lặp trước (Pre-test Loop) và điều kiện dừng nhằm tránh lỗi lặp vô tận (Infinite Loop).
- Làm chủ kỹ thuật vòng lặp vô tận có kiểm soát (`while True:`) kết hợp với câu lệnh rẽ nhánh `break` và `continue`.
- Phân tích cơ chế hoạt động của khối `while - else` độc đáo trong Python.

## 핵심 키워드 (Từ khóa)
- **`while 조건:`**: Lặp lại khối lệnh chừng nào biểu thức điều kiện còn giữ giá trị `True`.
- **사전 검사 반복 (Pre-test Loop)**: Kiểm tra điều kiện trước khi thực hiện thân vòng lặp (có thể chạy 0 lần).
- **무한 루프 (Infinite Loop)**: Vòng lặp không có điểm dừng (`while True:`), cần kiểm soát bằng `break`.
- **`while - else`**: Nhánh `else` được kích hoạt khi điều kiện vòng lặp trở thành `False` một cách tự nhiên.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [40-bai-hoc.md](40-bai-hoc.md) (Câu lệnh break và continue trong vòng lặp).
- Liên kết với [50-bai-hoc.md](50-bai-hoc.md) (Vòng lặp for và cấu trúc điều khiển if trong Python).
- Liên kết với [04-programming-language/82-bai-hoc.md](../../04-programming-language/lessons/82-bai-hoc.md) (So sánh while và do-while trong C/Java).

## 읽는 방법 (Cách đọc)
- Phân biệt với C/Java: Python **không có** cấu trúc `do-while`. Mọi vòng lặp `while` trong Python đều là kiểm tra điều kiện trước.
- Khi lần vết bài tập `while` trong đề thi:
  - Luôn kiểm tra dòng lệnh thay đổi biến điều kiện (như `i += 1`).
  - Nếu không có dòng cập nhật biến, vòng lặp sẽ bị treo vĩnh viễn (Time Limit Exceeded).
  - Nếu có lệnh `break` được kích hoạt, khối `else` của `while` sẽ **bị bỏ qua**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Cú pháp và nguyên lý hoạt động
- **Cú pháp cơ bản**:
  ```python
  while điều_kiện:
      khối_lệnh_lặp
  ```
- **Quy trình hoạt động**:
  1. Đánh giá `điều_kiện`: Nếu là `True`, chuyển sang bước 2. Nếu là `False`, kết thúc vòng lặp.
  2. Thực thi toàn bộ các câu lệnh trong `khối_lệnh_lặp`.
  3. Quay trở lại bước 1 để đánh giá lại điều kiện.

#### 2. So sánh vòng lặp `for` vs `while` trong Python
| Tiêu chí | Vòng lặp `for` | Vòng lặp `while` |
| :--- | :--- | :--- |
| **Bản chất sử dụng** | Khi đã **biết trước số lần lặp** hoặc duyệt qua một tập hợp hữu hạn (List, Range) | Khi **chưa biết trước số lần lặp**, chỉ lặp chừng nào một điều kiện logic còn thỏa mãn |
| **Biến đếm** | Tự động tăng và nhận phần tử kế tiếp qua mỗi vòng | Lập trình viên phải tự khởi tạo và tự cập nhật biến đếm thủ công |
| **Nguy cơ lỗi** | Hiếm khi bị lặp vô tận | Dễ bị lặp vô tận nếu quên cập nhật biến điều kiện |

#### 3. Kỹ thuật `while True` với `break`
```python
total = 0
i = 1
while True:
    total += i
    i += 1
    if i > 5:
        break # Điều kiện thoát khỏi vòng lặp vô tận
print(total) # 1 + 2 + 3 + 4 + 5 = 15
```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Cơ chế hoạt động của cấu trúc `while - else`
```python
count = 0
while count < 3:
    print(f"Lần {count}")
    count += 1
else:
    # Chạy sau khi điều kiện count < 3 trở thành False (count = 3)
    print("Vòng lặp hoàn thành bình thường!")

# Kết quả in ra:
# Lần 0
# Lần 1
# Lần 2
# Vòng lặp hoàn thành bình thường!
```
- *Lưu ý quan trọng*: Nếu bên trong vòng lặp xuất hiện lệnh `break` và lệnh đó được thực thi, khối `else` sẽ bị hủy bỏ ngay lập tức và không được chạy.

#### 2. Bài toán lần vết đề thi Kỹ sư xử lý thông tin
```python
n = 12
res = 0
while n > 0:
    res = res * 10 + n % 10 # Lấy chữ số cuối cùng ghép vào kết quả đảo ngược
    n //= 10                # Phép chia lấy phần nguyên trong Python

print(res) # Kết quả in ra số đảo ngược: 21
```

---

### 복습 체크리스트
- [ ] Vòng lặp `while` trong Python thuộc loại kiểm tra điều kiện trước hay kiểm tra điều kiện sau?
- [ ] Python có hỗ trợ câu lệnh lặp `do-while` như trong C và Java hay không?
- [ ] Trong trường hợp nào thì khối lệnh nằm trong mệnh đề `else` của vòng lặp `while - else` sẽ bị bỏ qua không chạy?
- [ ] Phép toán `//` trong đoạn mã `n //= 10` của Python thực hiện phép tính gì?
