# 235. JAVA의 데이터 타입 크기 (Data Type Sizes in JAVA)

## 학습 목표 (Mục tiêu)
- Nắm vững kích thước bộ nhớ cố định độc lập với nền tảng phần cứng của 8 kiểu dữ liệu nguyên thủy (Primitive Data Types) trong ngôn ngữ lập trình Java.
- Phân tích sâu sắc hai điểm khác biệt mang tính cốt lõi giữa Java và ngôn ngữ C: kiểu `char` chiếm **2 Bytes** do hỗ trợ bảng mã quốc tế Unicode, và kiểu `long` luôn cố định **8 Bytes**.
- Phân biệt cấu trúc lưu trữ giữa Kiểu dữ liệu nguyên thủy (Primitive Type - lưu trên Stack) và Kiểu dữ liệu tham chiếu (Reference Type - đối tượng lưu trên Heap).

## 핵심 키워드 (Từ khóa)
- 자바 데이터 타입 크기 (Java Primitive Data Types)
- char (2바이트 / 유니코드 Unicode UTF-16)
- byte (1바이트 / -128 ~ 127)
- boolean (1바이트 / true, false)
- long (8바이트 / 64비트 정수)
- 기본형 vs 참조형 (Primitive Type vs Reference Type)
- 플랫폼 독립성 (Platform Independence)

## 선행·연결 개념 (Kiến thức liên kết)
- [04-bai-hoc.md](04-bai-hoc.md): Kích thước các kiểu dữ liệu trong ngôn ngữ C/C++.
- [06-bai-hoc.md](06-bai-hoc.md): Biến môi trường và các lệnh kịch bản Shell trong hệ điều hành.
- [정보처리기사/output/02-software-development/lessons/74-bai-hoc.md](../../02-software-development/lessons/74-bai-hoc.md): Nguyên tắc viết mã nguồn sạch (Clean Code).

## 읽는 방법 (Cách đọc)
- Khắc sâu 2 bẫy thi thường xuyên xuất hiện khi so sánh Java và C:
  - **Bẫy 1 - Kiểu `char`:** Trong C chỉ chiếm **1 Byte** (bảng mã ASCII), nhưng trong Java bắt buộc chiếm **2 Bytes** để biểu diễn được tất cả các ký tự chữ cái trên toàn cầu bằng chuẩn **Unicode (UTF-16)**.
  - **Bẫy 2 - Kiểu `boolean`:** Trong C không có kiểu boolean nguyên thủy riêng (dùng số nguyên 0 và 1), trong Java có kiểu riêng `boolean` chiếm 1 Byte và chỉ nhận đúng hai giá trị từ khóa `true` hoặc `false`.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng 8 kiểu dữ liệu nguyên thủy (Primitive Types) trong Java:**

| Kiểu dữ liệu | Kích thước | Số bits | Dải giá trị biểu diễn | So sánh đối ứng với C/C++ |
| :--- | :--- | :--- | :--- | :--- |
| **`boolean`** | **1 Byte** | 8 bits | Chỉ nhận `true` hoặc `false` | C truyền thống không có, C dùng số nguyên |
| **`byte`** | **1 Byte** | 8 bits | -128 đến 127 | Tương đương `signed char` trong C |
| **`char`** | **2 Bytes** | **16 bits** | 0 đến 65,535 (Ký tự Unicode) | **C chỉ có 1 Byte (ASCII)**; Java là 2 Bytes |
| **`short`** | **2 Bytes** | 16 bits | -32,768 đến 32,767 | Giống `short` trong C |
| **`int`** | **4 Bytes** | 32 bits | Khoảng -2.14 tỷ đến +2.14 tỷ | Giống `int` trong C |
| **`long`** | **8 Bytes** | 64 bits | Khoảng $-9 \times 10^{18}$ đến $+9 \times 10^{18}$ | **Trong C long thường là 4 Bytes**; Java cố định 8 Bytes |
| **`float`** | **4 Bytes** | 32 bits | Số thực độ chính xác đơn (7 chữ số thập phân) | Cần hậu tố `F` hoặc `f` (ví dụ: `3.14f`) |
| **`double`** | **8 Bytes** | 64 bits | Số thực độ chính xác kép (15 chữ số thập phân) | Kiểu số thực mặc định trong Java |

- **So sánh Kiểu nguyên thủy (Primitive) vs Kiểu tham chiếu (Reference):**

| Tiêu chuẩn | 기본형 (Primitive Type) | 참조형 (Reference Type) |
| :--- | :--- | :--- |
| **Đối tượng** | 8 kiểu cơ sở: byte, short, int, long, float, double, char, boolean | Lớp (Class), Giao diện (Interface), Mảng (Array), Chuỗi (`String`) |
| **Nơi lưu trữ giá trị** | Lưu trực tiếp giá trị thực tế trên vùng nhớ **Stack** | Biến lưu địa chỉ con trỏ trên Stack; đối tượng thực thể nằm trên **Heap** |
| **Giá trị khởi tạo mặc định** | Số $= 0$, boolean $= \text{false}$, char $= \text{'\u0000'}$ | Luôn là **`null`** khi chưa khởi tạo bằng toán tử `new` |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tính độc lập phần cứng của Java Data Types:**
  - Trong ngôn ngữ C, kích thước của kiểu `int` hoặc con trỏ có thể thay đổi tùy thuộc vào kiến trúc máy tính (16-bit, 32-bit, hay 64-bit).
  - Ngược lại, trong Java, nhờ có máy ảo JVM, kích thước của toàn bộ 8 kiểu dữ liệu nguyên thủy hoàn toàn cố định trên mọi hệ điều hành (Write Once, Run Anywhere).

### 복습 체크리스트
- [ ] Nhớ kỹ: Kiểu `char` trong Java chiếm 2 Bytes do dùng chuẩn Unicode (khác C chỉ 1 Byte).
- [ ] Nhớ kiểu `long` trong Java luôn cố định 8 Bytes (64 bits).
- [ ] Nhớ kiểu `byte` là 1 Byte (dải giá trị từ -128 đến 127).
- [ ] Phân biệt được Primitive type (lưu giá trị trên Stack) và Reference type (lưu đối tượng trên Heap, biến trỏ từ Stack).
