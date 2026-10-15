# 19. 클린 코드 작성 원칙 (Clean Code Principles)

## 학습 목표 (Mục tiêu)
- Nắm vững 5 nguyên tắc cốt lõi khi viết mã nguồn sạch (클린 코드 작성 원칙 - Clean Code Principles): Tính dễ đọc (가독성), Tính đơn giản (단순성), Giảm thiểu phụ thuộc (의존성 최소화/배제), Không lặp lại (중복 최소화), và Tính trừu tượng hóa hợp lý (추상화).
- Hiểu rõ lợi ích của Clean Code trong việc giảm thiểu nợ kỹ thuật (Technical Debt) và chi phí bảo trì phần mềm dài hạn.
- Phân biệt các thói quen viết mã xấu (Bad Smell / Code Smells) và cách tái cấu trúc (Refactoring) theo chuẩn Clean Code.

## 핵심 키워드 (Từ khóa)
- 클린 코드 (Clean Code)
- 가독성 (Readability / Ai cũng hiểu ngay ý định của mã)
- 단순성 (Simplicity / K.I.S.S - Keep It Simple, Stupid)
- 의존성 배제 (Loose Coupling / Minimized Dependencies)
- 중복 최소화 (Duplication Minimization / DRY - Don't Repeat Yourself)
- 추상화 (Abstraction / Thể hiện đúng bản chất lớp trên)

## 선행·연결 개념 (Kiến thức liên kết)
- [73-bai-hoc.md](73-bai-hoc.md): Độ phức tạp thời gian trong trường hợp xấu nhất.
- [75-bai-hoc.md](75-bai-hoc.md): Mã nguồn người ngoài hành tinh (Alien Code) và nợ kỹ thuật.
- [33-bai-hoc.md](33-bai-hoc.md): Các nguyên lý thiết kế mô-đun phần mềm (Abstraction, Information Hiding).

## 읽는 방법 (Cách đọc)
- Ghi nhớ 5 nguyên tắc Clean Code chuẩn thi Information Processing Engineer:
  1. **가독성 (Dễ đọc):** Đặt tên biến, hàm có ý nghĩa rõ ràng (ví dụ: `userList` thay vì `arr1`), định dạng thụt đầu dòng nhất quán.
  2. **단순성 (Đơn giản):** Mỗi hàm chỉ làm duy nhất một việc (Single Responsibility), code ngắn gọn, không viết logic lòng vòng.
  3. **의존성 배제 (Loại trừ phụ thuộc):** Giảm thiểu liên kết cứng giữa các lớp/mô-đun; thay đổi ở lớp này không làm đổ vỡ lớp khác.
  4. **중복 최소화 (Tránh trùng lặp):** Gom logic lặp lại thành hàm hoặc lớp dùng chung (DRY).
  5. **추상화 (Trừu tượng hóa):** Giấu chi tiết triển khai phức tạp đằng sau interface rõ ràng, chỉ hiển thị những gì cần thiết.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **Bảng tổng hợp 5 nguyên tắc viết Clean Code:**

| Nguyên tắc | Tên tiếng Hàn & Anh | Mục tiêu định hướng | Biểu hiện vi phạm (Code Smell) |
| :--- | :--- | :--- | :--- |
| **1. 가독성** | **Readability (Tính dễ đọc)** | Bất kỳ lập trình viên nào đọc vào cũng hiểu ngay mục đích và luồng xử lý của đoạn mã | Đặt tên biến vô nghĩa (`a`, `temp2`, `xyz`), thiếu định dạng thụt lề |
| **2. 단순성** | **Simplicity (Tính đơn giản)** | Mã nguồn được thiết kế tối giản, giải quyết vấn đề trực tiếp mà không phức tạp hóa | Hàm quá dài hàng trăm dòng, lồng ghép quá nhiều vòng lặp và câu lệnh `if-else` |
| **3. 의존성 배제** | **Dependency Minimization (Giảm phụ thuộc)** | Giảm thiểu sự gắn kết giữa các thành phần phần mềm; tăng tính độc lập | Thay đổi một hàm nhỏ ở module A buộc phải sửa đổi hàng loạt module B, C, D |
| **4. 중복 최소화** | **Duplication Minimization (Không trùng lặp)** | Một logic xử lý nghiệp vụ chỉ nên xuất hiện tại một nơi duy nhất trong toàn hệ thống (DRY) | Copy-paste cùng một đoạn code xử lý chuỗi hoặc tính toán thuế ra 5 tệp khác nhau |
| **5. 추상화** | **Abstraction (Tính trừu tượng)** | Tách biệt giữa "Hệ thống làm gì" (Interface) và "Hệ thống làm điều đó như thế nào" (Implementation) | Lộ chi tiết kết nối cơ sở dữ liệu cấp thấp ngay tại tầng giao diện người dùng |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Mối quan hệ giữa Clean Code và Refactoring:**
  - **리팩토링 (Refactoring):** Quá trình tái cấu trúc lại mã nguồn nội bộ nhằm cải thiện tính dễ đọc và bảo trì (hướng tới Clean Code) mà **tuyệt đối không làm thay đổi hành vi hoặc chức năng bên ngoài** của phần mềm.
  - Viết Unit Test tự động trước khi Refactoring là yêu cầu bắt buộc để đảm bảo việc dọn dẹp mã không tạo ra lỗi mới.

### 복습 체크리스트
- [ ] Kể tên đủ 5 nguyên tắc Clean Code: 가독성, 단순성, 의존성 배제, 중복 최소화, 추상화.
- [ ] Nhớ định nghĩa của 리팩토링 (Refactoring): Sửa cấu trúc bên trong, giữ nguyên chức năng bên ngoài.
- [ ] Hiểu nguyên tắc K.I.S.S và D.R.Y đối ứng với 단순성 và 중복 최소화.
