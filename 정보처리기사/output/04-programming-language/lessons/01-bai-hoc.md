# 프로그래밍 언어 기초 (Programming Language Basics)

## 학습 목표 (Mục tiêu)
- Nắm vững các nguyên tắc cơ bản trong nhập môn ngôn ngữ lập trình: quy tắc đặt tên biến (변수명 작성 규칙) và cơ chế quản lý bộ nhớ tự động của Trình thu gom rác (가비지 콜렉터 - Garbage Collector).
- Nhớ các điều kiện hợp lệ và không hợp lệ khi đặt tên biến trong các ngôn ngữ lập trình phổ biến (C, Java, Python).
- Hiểu rõ cơ chế giải phóng bộ nhớ heap của Garbage Collector (GC), chu kỳ hoạt động và lợi ích trong việc ngăn ngừa rò rỉ bộ nhớ (Memory Leak).

## 핵심 키워드 (Từ khóa)
- 프로그래밍 언어 기초 (Programming Language Basics)
- 변수명 작성 규칙 (Variable Naming Rules)
- 예약어 사용 금지 (Keywords / Reserved Words Prohibited)
- 대소문자 구분 (Case Sensitivity)
- 가비지 콜렉터 (Garbage Collector / GC)
- 메모리 자동 해제 (Automatic Memory Deallocation)
- 메모리 누수 방지 (Memory Leak Prevention)

## 선행·연결 개념 (Kiến thức liên kết)
- [02-bai-hoc.md](02-bai-hoc.md): Kiểu chuỗi dữ liệu trong Python và ký pháp Hungary.
- [03-bai-hoc.md](03-bai-hoc.md): Các kiểu dữ liệu cơ bản, biến số và toán tử.
- [정보처리기사/output/02-software-development/lessons/74-bai-hoc.md](../../02-software-development/lessons/74-bai-hoc.md): Nguyên tắc viết mã nguồn sạch (Clean Code).

## 읽는 방법 (Cách đọc)
- Phân biệt hai mảng kiến thức trọng tâm:
  - **변수명 규칙 (Quy tắc đặt tên biến):**
    - Chỉ được dùng chữ cái (`A-Z`, `a-z`), chữ số (`0-9`), và dấu gạch dưới (`_`).
    - **Ký tự đầu tiên KHÔNG ĐƯỢC là chữ số** (ví dụ: `1a` là sai, `a1` là đúng).
    - Phân biệt chữ hoa chữ thường (`Name` khác `name`).
    - Không được trùng với **từ khóa định sẵn (예약어 - Reserved Words)** như `int`, `for`, `if`, `while`.
  - **가비지 콜렉터 (Garbage Collector - GC):**
    - Trình tự động quét vùng nhớ Heap trong thời gian chạy. Khi một đối tượng không còn bất kỳ biến nào tham chiếu tới (Unreachable Object), GC sẽ thu hồi lại vùng nhớ đó để cấp phát cho các tiến trình khác.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp quy tắc đặt tên biến chuẩn đề thi:**

| Tiêu chí quy tắc | Quy định chuẩn | Ví dụ hợp lệ | Ví dụ không hợp lệ (Bẫy thi) |
| :--- | :--- | :--- | :--- |
| **Ký tự cho phép** | Chữ cái tiếng Anh, chữ số, dấu gạch dưới (`_`) | `user_name`, `age1` | `user-name` (chứa dấu trừ), `user@` (chứa `@`) |
| **Ký tự đầu tiên** | **Bắt buộc là chữ cái hoặc dấu gạch dưới (`_`)** | `_count`, `sum` | `1sum` (bắt đầu bằng chữ số) |
| **Khoảng trắng** | Tuyệt đối **không được chứa khoảng trắng** | `first_name` | `first name` (có dấu cách ở giữa) |
| **Phân biệt chữ hoa/thường** | Phân biệt tuyệt đối (Case-sensitive) | `Data` và `data` là 2 biến khác nhau | Cho rằng `Score` và `score` là một |
| **Từ khóa dự phòng (예약어)** | **Không được sử dụng từ khóa của ngôn ngữ** | `my_int`, `for_loop` | `int`, `for`, `while`, `class`, `return` |

- **Bảng tóm tắt cơ chế Garbage Collector (GC):**

| Tiêu chuẩn | Nội dung kỹ thuật cốt lõi |
| :--- | :--- |
| **Khái niệm** | Tiến trình nền tự động quét và **thu hồi không gian bộ nhớ (Heap Memory)** của các đối tượng không còn được sử dụng |
| **Mục đích** | Ngăn ngừa lỗi **rò rỉ bộ nhớ (Memory Leak)** và giảm bớt gánh nặng quản lý con trỏ thủ công cho lập trình viên |
| **Ngôn ngữ tiêu biểu** | **Java (JVM GC)**, C# (.NET CLR GC), Python; trong khi C/C++ yêu cầu giải phóng thủ công bằng `free()` / `delete` |
| **Nhược điểm** | Tạm dừng tiến trình ứng dụng trong thời gian ngắn (Stop-The-World) để dọn rác; khó dự đoán thời điểm kích hoạt chính xác |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chu kỳ sống của đối tượng trong Java Virtual Machine (JVM):**
  - Không gian Heap chia làm 2 vùng chính: Young Generation (chứa đối tượng mới tạo qua lệnh `new`) và Old Generation (chứa đối tượng sống sót qua nhiều đợt dọn rác).
  - Minor GC dọn dẹp vùng Eden/Survivor; Major GC (Full GC) dọn dẹp vùng Old Generation.

### 복습 체크리스트
- [ ] Nhớ tên biến KHÔNG ĐƯỢC bắt đầu bằng số (ví dụ: `1a` là sai).
- [ ] Nhớ tên biến KHÔNG ĐƯỢC trùng với từ khóa dự phòng (예약어) như `int`, `while`.
- [ ] Nhớ tên biến KHÔNG ĐƯỢC chứa khoảng trắng hay ký tự đặc biệt trừ dấu gạch dưới `_`.
- [ ] Nêu được định nghĩa và vai trò của Garbage Collector trong Java/Python.
