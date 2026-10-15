# 프로그래밍 언어 기초 (Mở rộng) (Programming Language Basics - Extended)

## 학습 목표 (Mục tiêu)
- Nắm vững các kiểu dữ liệu chuỗi tuần tự (Sequence Types) trong ngôn ngữ Python: Danh sách (List), Bộ dữ liệu bất biến (Tuple), và Dãy số nguyên sinh tự động (`range`).
- Nắm vững cú pháp khai báo kiểu dữ liệu cấu trúc (구조체 - Struct) trong ngôn ngữ C.
- Phân biệt kích thước bộ nhớ của các kiểu dữ liệu cơ sở trong Java (đặc biệt là kiểu `char` chiếm 2 bytes chuẩn Unicode).
- Hiểu quy tắc đặt tên theo Ký pháp Hungary (헝가리안 표기법 - Hungarian Notation) và ôn tập cơ chế của Garbage Collector.

## 핵심 키워드 (Từ khóa)
- 파이썬 시퀀스 자료형 (Python Sequence Types)
- 리스트 vs 튜플 (List mutable vs Tuple immutable)
- 레인지 (range sequence)
- C언어 구조체 (C Struct / `struct` 키워드)
- 자바 데이터 타입 (Java Data Types / `char` 2바이트 유니코드)
- 헝가리안 표기법 (Hungarian Notation / 접두사 표기법)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Quy tắc đặt tên biến và Garbage Collector.
- [03-bai-hoc.md](03-bai-hoc.md): Kiểu dữ liệu, biến số và toán tử.
- [05-bai-hoc.md](05-bai-hoc.md): Kích thước chi tiết các kiểu dữ liệu trong Java.

## 읽는 방법 (Cách đọc)
- Phân biệt các đặc trưng cốt lõi:
  - **Python Sequence Types:**
    - `List`: Viết trong ngoặc vuông `[1, 2, 3]`; có thể sửa, thêm, xóa phần tử (**Mutable**).
    - `Tuple`: Viết trong ngoặc đơn `(1, 2, 3)`; **tuyệt đối không thể thay đổi giá trị sau khi tạo (Immutable)**.
    - `range`: Hàm sinh dãy số nguyên tự động (ví dụ: `range(1, 5)` sinh ra các số 1, 2, 3, 4).
  - **C Struct (구조체):** Gom các biến khác kiểu dữ liệu thành một kiểu mới do người dùng tự định nghĩa bằng từ khóa `struct`.
  - **Ký pháp Hungary (Hungarian Notation):** Thêm tiền tố viết tắt kiểu dữ liệu vào ngay trước tên biến (ví dụ: `strName` cho chuỗi String, `nAge` cho số nguyên Number/Int, `bFlag` cho kiểu Boolean).

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng so sánh 3 kiểu dữ liệu chuỗi tuần tự (Sequence) trong Python:**

| Kiểu dữ liệu | Ký hiệu cú pháp | Khả năng biến đổi (Mutability) | Thao tác và đặc trưng |
| :--- | :--- | :--- | :--- |
| **리스트 (List)** | Dấu ngoặc vuông `[ ]` | **Có thể thay đổi (Mutable)** | Thêm phần tử (`append`), xóa (`pop`), sửa giá trị `a[0] = 99` |
| **튜플 (Tuple)** | Dấu ngoặc tròn `( )` | **Bất biến (Immutable)** | Sau khi gán, không thể sửa hay xóa bất kỳ phần tử nào; bảo vệ dữ liệu cố định |
| **레인지 (range)** | Hàm gọi `range(start, stop, step)` | **Bất biến (Immutable)** | Sinh chuỗi số nguyên lặp liên tiếp; thường dùng trong vòng lặp `for i in range(...)` |

- **Bảng tổng hợp kiểu dữ liệu cơ sở trong Java:**

| Nhóm kiểu | Kiểu dữ liệu Java | Kích thước bộ nhớ | Đặc trưng lưu ý trong kỳ thi |
| :--- | :--- | :--- | :--- |
| **문자 (Ký tự)** | `char` | **2 Bytes (16 bits)** | **Khác với C (1 Byte)**; Java dùng bảng mã **Unicode (UTF-16)** |
| **정수 (Số nguyên)** | `byte` | **1 Byte (8 bits)** | Dải giá trị từ -128 đến 127 |
|  | `short` | **2 Bytes (16 bits)** | Dải giá trị từ -32,768 đến 32,767 |
|  | `int` | **4 Bytes (32 bits)** | Kiểu số nguyên mặc định trong Java |
|  | `long` | **8 Bytes (64 bits)** | Cần hậu tố `L` khi khai báo giá trị lớn |
| **실수 (Số thực)** | `float` | **4 Bytes (32 bits)** | Số thực dấu phẩy động độ chính xác đơn; cần hậu tố `f` |
|  | `double` | **8 Bytes (64 bits)** | Số thực độ chính xác kép mặc định trong Java |
| **논리 (Boolean)** | `boolean` | **1 Byte (8 bits)** | Chỉ lưu hai giá trị `true` hoặc `false` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Cú pháp định nghĩa Struct trong C:**
  ```c
  struct sawon {
      char name[20];
      int pay;
  };
  struct sawon s1;
  s1.pay = 5000;
  ```
  - Mọi câu lệnh khai báo cấu trúc và khai báo biến trong C/Java đều phải kết thúc bằng dấu chấm phẩy `;`.
  - Truy cập trường dữ liệu của Struct thông qua toán tử chấm (`.`) đối với biến thông thường, hoặc toán tử mũi tên (`->`) đối với con trỏ Struct.

### 복습 체크리스트
- [ ] Phân biệt được List (ngoặc vuông, mutable) và Tuple (ngoặc tròn, immutable) trong Python.
- [ ] Nhớ trong Java kiểu `char` chiếm 2 Bytes (khác C chỉ 1 Byte) do hỗ trợ Unicode.
- [ ] Nhớ cú pháp định nghĩa `struct` trong C kết thúc bằng dấu chấm phẩy `;`.
- [ ] Nhận diện được Ký pháp Hungary: Gắn tiền tố kiểu dữ liệu vào tên biến (`strName`, `nAge`).
