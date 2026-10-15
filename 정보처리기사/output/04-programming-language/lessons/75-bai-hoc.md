# 추가: 응용 SW 기초 기술 (4과목 핵심 요약 1)

## 학습 목표 (Mục tiêu)
- Tổng hợp toàn diện các khái niệm nền tảng thường xuyên xuất hiện trong đề thi môn 4: Chương trình xử lý hàng loạt (배치 프로그램), Hệ thống kiểu dữ liệu đối chiếu C vs Java, Cấu trúc dữ liệu Struct trong C, Kiểu dữ liệu tuần tự trong Python, và Trình thu gom rác bộ nhớ (Garbage Collector).
- Phân biệt sự khác nhau mang tính bản chất giữa kiểu `char` trong C (1 Byte ASCII) và `char` trong Java (2 Byte Unicode).
- Phân biệt tính biến đổi (Mutability) giữa mảng động `list` (thay đổi được) và bộ `tuple` (bất biến - Immutable) trong Python.
- Nắm vững các toán tử thao tác bit và thứ tự ưu tiên lượng giá biểu thức phức hợp.

## 핵심 키워드 (Từ khóa)
- 응용 SW 기초 기술 (Application Software Fundamentals)
- 배치 프로그램 5대 요소 (대용량, 자동화, 견고성, 안정성, 성능)
- C vs JAVA 자료형 크기 (C char 1B vs Java char 2B 유니코드)
- C 언어 구조체 (struct - 서로 다른 자료형의 묶음)
- Python 리스트 vs 튜플 (List Mutable vs Tuple Immutable)
- 가비지 컬렉터 (Garbage Collector - 메모리 누수 방지)
- 비트 연산자 (Bitwise: AND, OR, XOR `^`, Shift)

## 선행·연결 개념 (Kiến thức liên kết)
- [74-bai-hoc.md](74-bai-hoc.md): 4 điều kiện bế tắc Deadlock và giải thuật tương hỗ loại trừ.
- [76-bai-hoc.md](76-bai-hoc.md): Chuyên đề sâu về chương trình xử lý hàng loạt Batch.
- [77-bai-hoc.md](77-bai-hoc.md): Chuyên đề cú pháp và con trỏ cấu trúc struct trong C.

## 읽는 방법 (Cách đọc)
- Bài học này đóng vai trò như một bản đồ tóm tắt cô đọng các câu hỏi tính điểm nhanh của môn 4:
  - Khẩu quyết Batch: **대자견안성** (Đại dung lượng, Tự động hóa, Kiên cố, An định, Hiệu năng).
  - So sánh kiểu dữ liệu: Nhớ ngay **Java char = 2 Byte (Unicode)**, Java boolean = 1 Byte.
  - Python: Cặp ngoặc tròn `()` là **Tuple (bất biến)**, ngoặc vuông `[]` là **List (sửa được)**.
  - Toán tử bit XOR `^`: Hai bit **khác nhau thì bằng 1**, giống nhau thì bằng 0.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Đối chiếu kích thước kiểu dữ liệu C/C++ vs Java:**

| Kiểu dữ liệu | Ngôn ngữ C / C++ | Ngôn ngữ JAVA | Ghi chú thi cử then chốt |
| :--- | :--- | :--- | :--- |
| **Ký tự (Character)** | `char`: **1 Byte** (ASCII) | `char`: **2 Byte** (Unicode UTF-16) | Java thiết kế hỗ trợ đa ngôn ngữ quốc tế |
| **Số nguyên 1 Byte** | `char` (dùng làm số) | `byte`: **1 Byte** (-128 ~ 127) | Java có kiểu `byte` chuyên biệt |
| **Số nguyên chuẩn** | `int`: **4 Byte** | `int`: **4 Byte** | Cả hai đều biểu diễn bù 2 (Two's Complement) |
| **Số nguyên dài** | `long`: 4 hoặc 8 Byte | `long`: **8 Byte** | Java quy định cố định 64-bit |
| **Số thực độ chính xác kép** | `double`: **8 Byte** | `double`: **8 Byte** | Chuẩn IEEE 754 |
| **Kiểu logic chân trị** | `_Bool` (hoặc số nguyên 0/1) | `boolean`: **1 Byte** | Java chỉ nhận `true` / `false`, không dùng số `0/1` |

- **2. Tổng hợp các khái niệm cấu trúc dữ liệu và runtime:**
  - **C Struct (구조체):** Gom nhóm các biến có **kiểu dữ liệu khác nhau (Heterogeneous)** vào một kiểu tự định nghĩa mới. Khác với mảng (Array) chỉ gom các phần tử cùng kiểu.
  - **Python Sequence:**
    - `List` (dùng dấu `[]`): Có thể thay đổi giá trị phần tử (Mutable), thêm bớt tùy ý (`append`, `pop`).
    - `Tuple` (dùng dấu `()`): **Bất biến (Immutable)**; một khi đã tạo thì không thể sửa đổi, thêm hoặc xóa phần tử. Thích hợp lưu trữ dữ liệu hằng số bảo vệ (như tọa độ địa lý, cấu hình cố định).
  - **Garbage Collector (Trình gom rác):** Chạy ngầm trong nền tảng JVM để tự động phát hiện và thu hồi bộ nhớ Heap của các đối tượng không còn tham chiếu nào trỏ tới, ngăn ngừa triệt để lỗi rò rỉ bộ nhớ (Memory Leak).

- **3. Bảng quy tắc toán tử bit:**

| Toán tử bit | Tên gọi | Quy tắc lượng giá chân trị bit |
| :---: | :--- | :--- |
| `&` | Bitwise AND | Cả 2 bit đều bằng 1 thì kết quả là 1; ngược lại bằng 0. |
| `\|` | Bitwise OR | Chỉ cần ít nhất 1 bit bằng 1 thì kết quả là 1. |
| `^` | Bitwise XOR | **Hai bit khác nhau thì bằng 1** ($1 \oplus 0 = 1$); hai bit giống nhau thì bằng 0. |
| `~` | Bitwise NOT | Đảo ngược toàn bộ bit (0 thành 1, 1 thành 0). |
| `<<` | Left Shift | Dịch bit sang trái $k$ vị trí, tương đương phép nhân với $2^k$. |
| `>>` | Right Shift | Dịch bit sang phải $k$ vị trí, tương đương phép chia nguyên cho $2^k$. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ví dụ tính toán bit XOR (`^`) và dịch bit trong đề thi:**
  - Tính biểu thức: `7 ^ 4`
    - $7$ ở dạng nhị phân 4-bit: `0111`
    - $4$ ở dạng nhị phân 4-bit: `0100`
    - Thực hiện XOR từng vị trí: `0111 ^ 0100 = 0011` (Hệ thập phân là $3$).
  - Biểu thức gán phức hợp: `a += 1` tương đương hoàn toàn với `a = a + 1`.

### 복습 체크리스트
- [ ] Ghi nhớ sự khác biệt: C `char` chiếm 1 Byte, Java `char` chiếm 2 Byte Unicode.
- [ ] Nhớ trong Python: List `[]` là Mutable, còn Tuple `()` là Immutable.
- [ ] Thuộc quy tắc toán tử XOR: 2 bit khác nhau cho ra 1, giống nhau cho ra 0.
- [ ] Kể tên 5 yếu tố của Batch: Đại dung lượng, Tự động hóa, Kiên cố, Ổn định, Hiệu năng.
