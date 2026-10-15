# 5. UML 구성요소 상세 (UML Components Detail)

## 학습 목표 (Mục tiêu)
- Thuộc nằm lòng 4 ký hiệu chỉ định quyền truy cập (`접근 제어자`) trong Class Diagram: `+` (Public), `-` (Private), `#` (Protected), và `~` (Package).
- Hiểu cấu trúc chi tiết của Use Case Diagram và phân biệt tuyệt đối giữa quan hệ bắt buộc `<<include>>` và quan hệ tùy chọn `<<extend>>`.
- Nắm vững các loại thông điệp trong Sequence Diagram: Thông điệp đồng bộ, Thông điệp bất đồng bộ, và Thông điệp phản hồi kết quả.

## 핵심 키워드 (Từ khóa)
- 접근 제어자 (Chỉ định quyền truy cập / Access Modifiers: `+`, `-`, `#`, `~`)
- Public, Private, Protected, Package
- 유스케이스 구성요소 (Thành phần Use Case: 시스템 범위, 액터, 유스케이스)
- `<<include>>` (Quan hệ bao hàm bắt buộc)
- `<<extend>>` (Quan hệ mở rộng tùy chọn)
- 동기 / 비동기 메시지 (Synchronous / Asynchronous Message)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([4. UML](16-bai-hoc.md)):** Sau khi nắm các đường nối quan hệ tổng quát, bài này đi sâu vào cú pháp thuộc tính bên trong của Class Diagram và cấu trúc các phần tử Use Case, Sequence.
- **Tiếp nối sang bài sau ([7. UML 심화](18-bai-hoc.md)):** Đi sâu vào nguồn gốc chuẩn hóa OMG (Booch, Rumbaugh, Jacobson) và các ứng dụng nâng cao của Stereotype.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 4 ký hiệu quyền truy cập (`+ - # ~`) và phân biệt `<<include>>` (bắt buộc) vs `<<extend>>` (tùy chọn) - đây là câu hỏi thi có tần suất lặp lại cao nhất trong Môn 1.
- Đọc TẦNG B để hiểu cách ánh xạ các ký hiệu này trực tiếp vào mã nguồn Java và C++.

---

## 5. UML 구성요소 상세 (UML Components Detail)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. 접근 제어자 (Access Modifiers - Ký hiệu quyền truy cập trong Class Diagram):**
  - `+`: **Public** - Cho phép truy cập tự do từ bất kỳ lớp nào ở ngoài hệ thống.
  - `-`: **Private** - Chỉ cho phép truy cập từ chính bên trong lớp định nghĩa nó.
  - `#`: **Protected** - Cho phép truy cập từ chính lớp đó và các lớp con kế thừa (`자식 클래스`) từ nó.
  - `~`: **Package (Default)** - Cho phép truy cập từ tất cả các lớp cùng nằm trong một gói (`동일 패키지 내`).
  - *Cú pháp biểu diễn thuộc tính:* `[접근제어자] 속성명 : 자료형 [= 기본값]` (Ví dụ: `- age : int = 0`).
  - *Cú pháp biểu diễn thao tác:* `[접근제어자] 오퍼레이션명(매개변수:자료형) : 반환자료형` (Ví dụ: `+ getName() : String`).
- **2. Thành phần và mối quan hệ trong Use Case Diagram:**
  - **Thành phần cơ bản:**
    - `시스템 범위 (System Boundary)`: Khung hình chữ nhật bao quanh các Use Case, phân tách bên trong hệ thống và tác nhân bên ngoài.
    - `액터 (Actor)`: Người que hoặc hình chữ nhật, nằm ngoài biên giới hệ thống.
    - `유스케이스 (Use Case)`: Hình elip nằm ngang, mô tả chức năng người dùng thực hiện.
  - **Mối quan hệ đặc thù trong Use Case:**
    - `포함 관계 (<<include>>)`: Mối quan hệ phụ thuộc **BẮT BUỘC**. Khi thực hiện Use Case A, **bắt buộc phải thực hiện** Use Case B. Mũi tên nét đứt hướng từ A sang B ($A \xrightarrow{<<include>>} B$). Ví dụ: Đặt hàng $\xrightarrow{<<include>>}$ Đăng nhập tài khoản.
    - `확장 관계 (<<extend>>)`: Mối quan hệ **TÙY CHỌN (Không bắt buộc)**. Khi thực hiện Use Case A, tùy theo điều kiện cụ thể mà có thể kích hoạt thêm Use Case B mở rộng. **Chú ý chiều mũi tên:** Mũi tên nét đứt hướng từ Use Case mở rộng B về Use Case gốc A ($B \xrightarrow{<<extend>>} A$). Ví dụ: Áp dụng mã giảm giá VIP $\xrightarrow{<<extend>>}$ Thanh toán đơn hàng.
- **3. Các loại thông điệp (Message) trong Sequence Diagram:**
  - `동기 메시지 (Synchronous Message)`: Người gửi thông điệp sẽ tạm dừng chờ cho đến khi nhận được kết quả trả về. Biểu diễn bằng **Đường nét liền có đầu mũi tên đặc (채워진 화살표)**.
  - `비동기 메시지 (Asynchronous Message)`: Người gửi gửi thông điệp đi và tiếp tục làm việc khác ngay mà không chờ phản hồi. Biểu diễn bằng **Đường nét liền có đầu mũi tên mở/gạch chéo (선 화살표)**.
  - `반환 메시지 (Return Message)`: Kết quả xử lý gửi ngược về cho đối tượng gọi hàm. Biểu diễn bằng **Đường nét đứt có đầu mũi tên mở (점선 화살표)**.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1 (Ký hiệu quyền truy cập):** Ký hiệu `#` tương ứng với quyền nào? -> **Protected**. Ký hiệu `~` tương ứng với quyền nào? -> **Package**.
  - **Bẫy 2 (Chiều mũi tên extend):** Trong quan hệ 확장 (`<<extend>>`), mũi tên chỉ từ đâu sang đâu? -> **Chỉ từ Use Case mở rộng về Use Case gốc**, KHÔNG PHẢI từ gốc sang mở rộng.
  - **Bẫy 3:** *"Thao tác nào là bắt buộc thực hiện trong quy trình Use Case?"* -> **포함 관계 (<<include>>)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Cộng Public, Trừ Private, Thăng Protected, Ngã Package; Include bắt buộc mũi tên đi, Extend tùy chọn mũi tên về".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ánh xạ ký hiệu truy cập vào mã nguồn:**
  ```java
  public class Account {
      + public String accountHolder;  // +
      - private double balance;       // -
      # protected String bankBranch;  // #
      ~ String internalCode;          // ~ (Package-private, không ghi từ khóa)
  }
  ```
- **Phân biệt bản chất Include vs Extend trong thiết kế nghiệp vụ:**
  - Nếu không có chức năng `Đăng nhập`, khách hàng không thể `Xem thông tin tài khoản` -> Đây là **Include** (phụ thuộc tồn tại, phải có).
  - Khách hàng đang thanh toán giỏ hàng, nếu tài khoản có điểm tích lũy thì có thể chọn `Đổi điểm lấy quà`, không có điểm thì bỏ qua và thanh toán bình thường -> Đây là **Extend** (hành vi bổ sung tùy biến theo điều kiện).

### 복습 체크리스트
- [ ] Nhớ chính xác ý nghĩa của 4 ký hiệu quyền truy cập: `+`, `-`, `#`, `~`.
- [ ] Phân biệt được tính bắt buộc của `<<include>>` và tính tùy chọn của `<<extend>>`.
- [ ] Vẽ đúng chiều mũi tên của `<<include>>` (gốc sang con) và `<<extend>>` (mở rộng về gốc).
- [ ] Nhận diện được 3 loại mũi tên thông điệp trong Sequence Diagram: Đồng bộ, Bất đồng bộ, và Trả về.
