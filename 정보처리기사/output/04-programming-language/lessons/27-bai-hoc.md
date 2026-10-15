# 236. Python의 시퀀스 자료형 (Sequence Data Types in Python)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và đặc điểm vận hành của các kiểu dữ liệu chuỗi tuần tự (시퀀스 자료형 - Sequence Data Types) trong Python: List, Tuple, và `range`.
- Phân biệt sâu sắc tính có thể biến đổi (가변성 - Mutability) của List và tính bất biến tuyệt đối (불변성 - Immutability) của Tuple.
- Nắm vững kỹ thuật đánh chỉ số âm (음수 인덱싱 - Negative Indexing: `a[-1]`) và các phương thức thao tác danh sách thông dụng: `append()`, `insert()`, `pop()`, `remove()`.

## 핵심 키워드 (Từ khóa)
- 시퀀스 자료형 (Sequence Data Types)
- 리스트 (List / 가변 시퀀스 / `[]`)
- 튜플 (Tuple / 불변 시퀀스 / `()`)
- 레인지 (range / 메모리 효율적 연속 수열)
- 음수 인덱싱 (Negative Indexing / `[-1]`은 마지막 요소)
- 리스트 조작 메서드 (append, pop, insert, sort)
- 패킹 및 언패킹 (Packing & Unpacking)

## 선행·연결 개념 (Kiến thức liên kết)
- [26-bai-hoc.md](26-bai-hoc.md): Cú pháp cơ bản và thụt lề trong Python.
- [28-bai-hoc.md](28-bai-hoc.md): Tổng hợp toàn diện ngữ pháp và các hàm Python.
- [25-bai-hoc.md](25-bai-hoc.md): Cấu trúc dữ liệu nền tảng trong Python.

## 읽는 방법 (Cách đọc)
- Phân biệt cơ chế đánh chỉ số trong Python:
  - **Chỉ số dương (Từ trái sang phải):** Bắt đầu từ `0` $\rightarrow$ Phần tử đầu tiên là `a[0]`.
  - **Chỉ số âm (Từ phải sang trái):** Bắt đầu từ `-1` $\rightarrow$ Phần tử cuối cùng là `a[-1]`, phần tử áp chót là `a[-2]`.
- Phân biệt List và Tuple:
  - List: Dùng khi dữ liệu biến động liên tục trong chương trình (như giỏ hàng, danh sách điểm thi).
  - Tuple: Dùng cho dữ liệu hằng số cố định cần bảo vệ an toàn, không muốn bất kỳ hàm nào vô tình sửa đổi (như tọa độ địa lý GPS, mã màu RGB `(255, 0, 0)`).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh chi tiết: List vs Tuple vs Range:**

| Kiểu dữ liệu tuần tự | Cú pháp khởi tạo | Tính bất biến (Immutability) | Phương thức hỗ trợ | Trường hợp sử dụng tối ưu |
| :--- | :--- | :--- | :--- | :--- |
| **`list`** | `[1, 2, 3]` hoặc `list()` | **Có thể sửa đổi (Mutable)**; cho phép thêm, xóa, gán lại phần tử | `append()`, `insert()`, `pop()`, `remove()`, `sort()` | Cần cấu trúc dữ liệu động, thay đổi linh hoạt |
| **`tuple`** | `(1, 2, 3)` hoặc `tuple()` | **Bất biến (Immutable)**; gán lại phần tử sẽ báo lỗi `TypeError` | `count()`, `index()` (Chỉ các phương thức đọc) | Dữ liệu cấu hình, khóa từ điển, dữ liệu chỉ đọc |
| **`range`** | `range(1, 10)` | **Bất biến (Immutable)**; sinh số theo nhu cầu, tiết kiệm RAM | Duyệt vòng lặp `for`, kiểm tra tồn tại `in` | Tạo dãy số nguyên lặp liên tiếp |

- **Bảng các phương thức thao tác danh sách List quan trọng:**

| Tên phương thức | Cú pháp gọi | Hành vi kỹ thuật | Ví dụ với `a = [10, 20, 30]` |
| :--- | :--- | :--- | :--- |
| **`append(x)`** | `a.append(40)` | Thêm phần tử $x$ vào **vị trí cuối cùng** của danh sách | `a` trở thành `[10, 20, 30, 40]` |
| **`insert(i, x)`** | `a.insert(1, 99)` | Chèn phần tử $x$ vào **vị trí chỉ số $i$**, dời các phần tử sau lùi lại | `a` trở thành `[10, 99, 20, 30]` |
| **`pop()`** | `val = a.pop()` | Lấy ra và **xóa phần tử cuối cùng** của danh sách | Trả về `30`, `a` còn `[10, 20]` |
| **`remove(x)`** | `a.remove(20)` | Tìm và **xóa phần tử đầu tiên có giá trị bằng $x$** | `a` trở thành `[10, 30]` |
| **`sort()`** | `a.sort()` | Sắp xếp lại danh sách theo thứ tự tăng dần trực tiếp | `[30, 10, 20].sort()` $\rightarrow$ `[10, 20, 30]` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Điểm lưu ý đặc biệt về Tuple có 1 phần tử:**
  - Nếu viết `t = (5)`, Python sẽ hiểu đây là một số nguyên `int` nằm trong dấu ngoặc đơn toán học, **không phải Tuple**.
  - Muốn tạo Tuple có duy nhất 1 phần tử, **bắt buộc phải có dấu phẩy**: `t = (5,)` $\rightarrow$ Kiểu dữ liệu lúc này mới là `tuple`. Đây là bẫy trắc nghiệm nhận diện kiểu dữ liệu cực kỳ tinh tế.

### 복습 체크리스트
- [ ] Nhớ chỉ số âm `a[-1]` luôn trỏ tới phần tử cuối cùng của chuỗi/mảng.
- [ ] Nhớ Tuple là bất biến (Immutable), cố tình sửa `t[0] = 99` sẽ bị lỗi `TypeError`.
- [ ] Nhớ Tuple 1 phần tử bắt buộc phải có dấu phẩy: `(5,)`.
- [ ] Phân biệt được `append()` (thêm vào cuối) và `insert()` (chèn vào chỉ số cụ thể).
