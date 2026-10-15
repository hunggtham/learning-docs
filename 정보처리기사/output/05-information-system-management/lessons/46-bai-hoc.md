# Python 데이터 입·출력 함수 (Python Input/Output Functions)

## 학습 목표 (Mục tiêu)
- Nắm vững cơ chế hoạt động của hàm nhập chuẩn `input()` trong Python và bản chất luôn trả về kiểu chuỗi ký tự (`str`).
- Làm chủ cú pháp và các tham số tùy chọn của hàm xuất chuẩn `print()`: Tham số phân tách `sep` và tham số kết thúc `end`.
- Phân tích chính xác định dạng hiển thị kết quả đầu ra trong các bài tập đọc hiểu mã nguồn đề thi Kỹ sư xử lý thông tin.

## 핵심 키워드 (Từ khóa)
- **표준 입력 `input()`**: Đọc dữ liệu từ bàn phím, kết quả trả về luôn là kiểu chuỗi văn bản (`str`).
- **표준 출력 `print()`**: Hàm xuất dữ liệu ra màn hình console.
- **`sep` (Separator)**: Ký tự phân cách giữa các đối số truyền vào `print()` (mặc định là một dấu cách `' '`).
- **`end` (End character)**: Ký tự được in ra ở vị trí cuối cùng sau khi xuất hết các đối số (mặc định là ký tự xuống dòng `\n`).

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [45-bai-hoc.md](45-bai-hoc.md) (Cú pháp cơ bản của Python).
- Liên kết với [47-bai-hoc.md](47-bai-hoc.md) (Ép kiểu dữ liệu sau khi nhập bằng input).
- Liên kết với [04-programming-language/78-bai-hoc.md](../../04-programming-language/lessons/78-bai-hoc.md) (Hàm xuất dữ liệu chuẩn trong C và Java).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý quan sát kỹ tham số `end` trong vòng lặp:
  - Nếu `end=' '` hoặc `end=','`: Các lần in tiếp theo sẽ nằm trên **cùng một dòng** chứ không xuống hàng!
  - Mặc định của `print(a, b)` sẽ chèn một khoảng trắng ở giữa do `sep=' '`. Nếu đặt `sep='-'` thì `82` và `24` sẽ in thành `82-24`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Hàm nhập chuẩn `input()`
- **Đặc điểm cốt lõi**: Tạm dừng chương trình để nhận chuỗi ký tự người dùng nhập từ bàn phím cho đến khi nhấn phím Enter.
- **Giá trị trả về**: Luôn luôn là **kiểu chuỗi (`str`)**, ngay cả khi người dùng nhập toàn chữ số (ví dụ: nhập `100` thì biến nhận được chuỗi `"100"`).
- **Cú pháp**: `biến = input("Chuỗi nhắc thông báo")`
- *Hệ quả thi cử*: Nếu viết `a = input(); b = input(); print(a + b)` và nhập lần lượt 10 và 20, kết quả in ra sẽ là phép nối chuỗi `"1020"`, không phải phép cộng số học 30!

#### 2. Hàm xuất chuẩn `print()` và các tham số điều khiển
| Thành phần | Giá trị mặc định | Chức năng kỹ thuật | Ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| **Đối số giá trị** | Không có | Danh sách các biến, biểu thức hoặc chuỗi cần in ra | `print("A", 100, 3.14)` |
| **`sep` (Separator)** | `' '` (Một dấu cách) | Chuỗi ký tự chèn vào giữa các giá trị khi in | `print(1, 2, 3, sep=':')` $\rightarrow$ In ra `1:2:3` |
| **`end` (End char)** | `'\n'` (Ký tự xuống dòng) | Chuỗi ký tự in ở cuối cùng sau khi in xong | `print("Hi", end="")` $\rightarrow$ Không xuống dòng |

#### 3. Ví dụ mã nguồn thi Kỹ sư xử lý thông tin
```python
# Ví dụ kết hợp cả sep và end
print(82, 24, sep='-', end=',')
print(100)
# Dòng 1 in: 82-24, (không xuống dòng vì end=',')
# Dòng 2 in tiếp ngay sau: 100 (xuống dòng)
# Kết quả hiển thị hoàn chỉnh trên màn hình:
# 82-24,100
```

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. So sánh cơ chế in ấn giữa C, Java và Python
- **Trong C**: `printf("%d-%d\n", 82, 24);` (Cần định dạng đặc tả format `%d`, phải viết tường minh `\n`).
- **Trong Java**: `System.out.println(82 + "-" + 24);` (Tự động xuống dòng, phải dùng phép nối chuỗi `+`).
- **Trong Python**: `print(82, 24, sep='-')` (Tự động chuyển đổi kiểu dữ liệu của các đối số, tự động thêm dấu cách và xuống dòng).

#### 2. Kỹ thuật in chuỗi định dạng hiện đại (F-String) trong Python
- Từ Python 3.6 trở đi, F-String là phương pháp định dạng chuỗi được ưa chuộng nhất nhờ tốc độ nhanh và tính trực quan:
  ```python
  name = "Alice"
  score = 95.5
  print(f"Học viên {name} đạt {score:.1f} điểm.")
  # In ra: Học viên Alice đạt 95.5 điểm.
  ```

---

### 복습 체크리스트
- [ ] Hàm `input()` trong Python trả về kiểu dữ liệu gì theo mặc định?
- [ ] Giá trị mặc định của tham số `sep` và `end` trong hàm `print()` lần lượt là gì?
- [ ] Đoạn mã `print(1, 2, sep='*', end='#'); print(3)` sẽ cho kết quả đầu ra chính xác như thế nào?
- [ ] Tại sao phép tính `input() + input()` với đầu vào là 5 và 5 lại cho ra kết quả `55`?
