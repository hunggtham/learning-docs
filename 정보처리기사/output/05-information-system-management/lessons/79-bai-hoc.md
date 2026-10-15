# 널 포인터 역참조 (Null Pointer Dereference / Tham chiếu ngược Con trỏ Null)

## 학습 목표 (Mục tiêu)
- Nắm vững bản chất cơ chế phát sinh lỗi tham chiếu ngược con trỏ Null (Null Pointer Dereference).
- Phân tích hậu quả an ninh phần mềm khi xảy ra lỗi Null: Làm sập ứng dụng đột ngột (Crash / Segmentation Fault) và tạo điều kiện cho các đòn tấn công Từ chối dịch vụ (DoS).
- Làm chủ các biện pháp phòng vệ chuẩn trong lập trình an toàn: Kiểm tra Null tường minh, áp dụng mẫu thiết kế Null Object Pattern, sử dụng lớp bao bọc `Optional` và toán tử an toàn (Safe Call / Optional Chaining).

## 핵심 키워드 (Từ khóa)
- **널 포인터 역참조 (Null Pointer Dereference)**: Cố gắng đọc/ghi dữ liệu hoặc gọi phương thức thông qua con trỏ/tham chiếu rỗng (`NULL`).
- **서비스 거부 (DoS - Denial of Service)**: Hậu quả phổ biến khi ứng dụng bị sập do không bắt lỗi ngoại lệ `NullPointerException`.
- **널 검사 (Null Check)**: Kiểm tra điều kiện `if (ptr != NULL)` trước khi truy xuất.
- **`Optional<T>`**: Lớp bao bọc đối tượng trong Java/C++ nhằm xử lý an toàn giá trị có thể rỗng.
- **Null Object Pattern**: Mẫu thiết kế trả về đối tượng rỗng thay vì trả về `null`.

## 선행·연결 개념 (Kiến thức liên kết)
- Liên kết với [43-bai-hoc.md](43-bai-hoc.md) (Khái niệm con trỏ và toán tử giải tham chiếu `*`).
- Liên kết với [80-bai-hoc.md](80-bai-hoc.md) (Sử dụng API an toàn trong phát triển phần mềm).
- Liên kết với [04-programming-language/70-bai-hoc.md](../../04-programming-language/lessons/70-bai-hoc.md) (Lỗ hổng bảo mật phần mềm).

## 읽는 방법 (Cách đọc)
- Đi thi chú ý nhận diện nhanh:
  - "Con trỏ chưa được trỏ vào vùng nhớ hợp lệ nhưng chương trình vẫn cố đọc ghi hoặc gọi phương thức" $\rightarrow$ **널 포인터 역참조 (Null Pointer Dereference)**.
  - Hậu quả nghiêm trọng nhất về mặt an ninh thông tin: **Hệ thống bị dừng hoạt động bất thường (비정상 종료) $\rightarrow$ Tấn công từ chối dịch vụ (DoS)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)

#### 1. Bản chất Kỹ thuật của Lỗi Null Pointer Dereference
- **Cơ chế**: Trong kiến trúc bộ nhớ, con trỏ `NULL` (hoặc `0x0`) trỏ tới một vùng không gian địa chỉ được hệ điều hành bảo vệ đặc biệt (cấm truy cập).
- Khi lập trình viên cố tình giải tham chiếu con trỏ rỗng (`*ptr` trong C) hoặc gọi phương thức của một biến tham chiếu đang mang giá trị `null` (`user.getName()` trong Java):
  - Phần cứng CPU (MMU) phát hiện sự cố vi phạm phân trang bảo vệ và phát tín hiệu ngắt phần cứng (Hardware Exception).
  - Hệ điều hành gửi tín hiệu kết thúc tiến trình: Trong C/C++ sinh lỗi **Segmentation Fault (SIGSEGV)**; trong Java ném ra ngoại lệ **`java.lang.NullPointerException` (NPE)**.
- **Rủi ro An ninh Thông tin**: Nếu một hàm API của máy chủ web bị lỗi NPE khi nhận tham số rỗng mà không có khối xử lý ngoại lệ `try-catch`, kẻ tấn công có thể gửi liên tục các yêu cầu chứa giá trị rỗng để làm sập tiến trình máy chủ, gây ra tình trạng **Từ chối dịch vụ (Denial of Service - DoS)**.

#### 2. So sánh Đoạn mã Nguy hiểm vs Đoạn mã An toàn
| Ngôn ngữ | Đoạn mã Nguy hiểm (Chứa lỗ hổng) | Đoạn mã An toàn (Đã phòng thủ) |
| :--- | :--- | :--- |
| **C / C++** | ```c
char *str = get_data();
printf("%s", str); // Nếu str == NULL sẽ crash!
``` | ```c
char *str = get_data();
if (str != NULL) {
    printf("%s", str);
}
``` |
| **Java** | ```java
String name = user.getName();
if (name.equals("admin")) { ... } // NPE nếu name null!
``` | ```java
String name = user.getName();
// Đưa hằng số lên trước để tránh NPE:
if ("admin".equals(name)) { ... }
``` |

#### 3. Các Giải pháp Phòng ngừa Hiện đại
1. **Kiểm tra Null chủ động (Explicit Null Checking)**: Luôn kiểm tra con trỏ khác Null ở đầu hàm (Pre-condition check) trước khi xử lý logic nghiệp vụ.
2. **Sử dụng lớp `Optional<T>` (Java 8+)**:
   - Ép buộc lập trình viên phải tường minh xử lý trường hợp không có giá trị:
   ```java
   Optional<User> userOpt = findUser(id);
   String name = userOpt.map(User::getName).orElse("Khách");
   ```
3. **Toán tử an toàn (Safe Call / Optional Chaining)**: Trong Kotlin, Swift, TypeScript dùng toán tử `?.` (ví dụ: `user?.getName()`), nếu `user` là null thì biểu thức tự động trả về null mà không gây crash.
4. **Mẫu thiết kế Null Object Pattern**: Trả về một đối tượng đặc biệt có hành vi rỗng (ví dụ: danh sách rỗng `Collections.emptyList()`, đối tượng `GuestUser`) thay vì trả về giá trị nguyên thủy `null`.

---

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)

#### 1. Quy tắc lập trình an toàn KISA / OWASP cho chuỗi trong Java
- Khi so sánh chuỗi với một hằng số (Literal), luôn gọi phương thức `.equals()` từ phía hằng số thay vì từ biến:
  ```java
  // Cách sai (Dễ bị NPE nếu status là null):
  if (status.equals("ACTIVE")) { ... }

  // Cách đúng (Tuyệt đối an toàn, không bao giờ bị NPE):
  if ("ACTIVE".equals(status)) { ... }
  ```

---

### 복습 체크리스트
- [ ] Lỗi Null Pointer Dereference dẫn đến hậu quả trực tiếp nào đối với tiến trình đang thực thi?
- [ ] Tại sao lỗ hổng Null Pointer Dereference lại được xếp vào nhóm nguy cơ tấn công Từ chối dịch vụ (DoS)?
- [ ] Quy tắc đảo vị trí hằng số trong phép so sánh `equals()` của Java giúp tránh được lỗi gì?
- [ ] Mẫu thiết kế Null Object Pattern giúp loại bỏ việc kiểm tra null lặp đi lặp lại như thế nào?
