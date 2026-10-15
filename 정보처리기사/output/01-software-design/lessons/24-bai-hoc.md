# 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của Kiến trúc phần mềm (`소프트웨어 아키텍처`) như một bản thiết kế khung xương định hình toàn bộ cấu trúc hệ thống.
- Thuộc nằm lòng 6 đặc tính chất lượng phần mềm theo tiêu chuẩn quốc tế `ISO/IEC 9126`: Tính chức năng, Độ tin cậy, Tính khả dụng, Tính hiệu quả, Khả năng bảo trì, và Khả năng khả chuyển.
- Nhận diện các mẫu kiến trúc kinh điển (`아키텍처 패턴`): Mẫu phân tầng (Layered), Mẫu Khách - Chủ (Client-Server), Mẫu Ống dẫn - Bộ lọc (Pipe-Filter), Mẫu MVC, và Mẫu Môi giới (Broker).

## 핵심 키워드 (Từ khóa)
- 소프트웨어 아키텍처 (Kiến trúc phần mềm / Software Architecture)
- ISO/IEC 9126 (Tiêu chuẩn chất lượng phần mềm)
- 기능성·신뢰성·사용성·효율성·유지보수성·이식성 (6 đặc tính ISO 9126)
- 아키텍처 패턴 (Mẫu kiến trúc / Architectural Patterns)
- 레이어드 패턴 (Layered Pattern / 계층 구조)
- 파이프-필터 패턴 (Pipe-Filter Pattern / UNIX Shell)
- MVC 패턴 (Model-View-Controller)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([8. UI 및 UX, HCI](23-bai-hoc.md)):** Sau khi xem xét giao diện và trải nghiệm tương tác bên ngoài, bài này đi sâu vào khung xương kỹ thuật vững chắc bên dưới của hệ thống.
- **Tiếp nối sang bài sau ([1. 소프트웨어 아키텍처](25-bai-hoc.md)):** So sánh chi tiết giữa Thiết kế mức cao (상위 설계) và Thiết kế mức thấp (하위 설계), cùng mô hình 4+1 View.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc 6 đặc tính chất lượng của ISO/IEC 9126 bằng thần chú **기-신-사-효-유-이** và đặc trưng nhận diện của từng mẫu kiến trúc.
- Đọc TẦNG B để hiểu cơ chế truyền dữ liệu liên tục không phụ thuộc trạng thái của mẫu Pipe-Filter trong hệ điều hành và xử lý dữ liệu lớn.

---

## 5. 소프트웨어 아키텍처 및 설계 (Kiến trúc và Thiết kế Phần mềm)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Kiến trúc phần mềm):** Là khung cấu trúc cơ bản (`기본 구조`) của toàn bộ hệ thống phần mềm, xác định các thành phần phần mềm (Components), mối quan hệ tương tác giữa chúng và các nguyên tắc chỉ đạo việc thiết kế, tiến hóa hệ thống theo thời gian.
- **ISO/IEC 9126 (6 đặc tính chất lượng phần mềm quốc tế):**
  1. `기능성 (Functionality - Tính chức năng)`: Phần mềm cung cấp đúng và đủ các chức năng theo yêu cầu (Bao gồm: Tính phù hợp - 적절성, Độ chính xác - 정밀성, Khả năng tương tác - 상호운용성, Bảo mật - 보안성, Tuân thủ tiêu chuẩn - 준수성).
  2. `신뢰성 (Reliability - Độ tin cậy)`: Khả năng duy trì mức hiệu năng quy định trong các điều kiện xác định (Bao gồm: Độ chín muồi - 성숙성, Khả năng chịu lỗi - 결함 허용성, Khả năng phục hồi sự cố - 회복성).
  3. `사용성 (Usability - Tính khả dụng)`: Người dùng dễ hiểu, dễ học và thao tác thuận tiện (Bao gồm: Dễ hiểu - 이해성, Dễ học - 학습성, Dễ vận hành - 운용성, Thân thiện - 친근성).
  4. `효율성 (Efficiency - Tính hiệu quả)`: Mức hiệu năng tối ưu tương ứng với lượng tài nguyên tiêu tốn (Bao gồm: Thời gian đáp ứng nhanh - 시간 반응성, Sử dụng tiết kiệm tài nguyên - 자원 활용성).
  5. `유지보수성 (Maintainability - Khả năng bảo trì)`: Khả năng dễ dàng sửa đổi khi có lỗi hoặc nâng cấp (Bao gồm: Dễ phân tích lỗi - 분석성, Dễ sửa đổi - 변경성, Độ ổn định - 안정성, Dễ kiểm thử - 시험성).
  6. `이식성 (Portability - Khả năng khả chuyển)`: Khả năng chuyển đổi phần mềm sang môi trường phần cứng/hệ điều hành khác (Bao gồm: Dễ thích ứng - 적응성, Dễ cài đặt - 설치성, Khả năng cùng tồn tại - 공존성, Dễ thay thế - 대체성).
  - 💡 **Thần chú nhớ 6 đặc tính:** **기-신-사-효-유-이** (Kỹ Năng Sống Tối Ưu, Hữu Ích).
- **Các mẫu kiến trúc phần mềm tiêu biểu (아키텍처 패턴):**
  - **레이어드 패턴 (Layered Pattern - Mẫu phân tầng):**
    - Hệ thống được chia thành các tầng độc lập xếp chồng lên nhau (ví dụ: UI Layer -> Business Logic Layer -> Data Access Layer).
    - Tầng trên chỉ sử dụng dịch vụ của tầng ngay dưới nó. Ưu điểm: Độc lập cao, dễ bảo trì và nâng cấp từng tầng.
  - **클라이언트-서버 패턴 (Client-Server Pattern):**
    - Một máy chủ (Server) phục vụ nhiều máy khách (Client) gửi yêu cầu dịch vụ qua mạng.
  - **파이프-필터 패턴 (Pipe-Filter Pattern):**
    - Luồng dữ liệu chảy qua chuỗi các bộ lọc (`Filter`) được kết nối với nhau bằng các ống dẫn (`Pipe`). Mỗi Filter biến đổi dữ liệu nhận được và đẩy sang Filter kế tiếp (ví dụ tiêu biểu: lệnh đường ống `|` trong UNIX Shell, hệ thống chuyển đổi video/audio).
  - **MVC 패턴 (Model-View-Controller Pattern):**
    - Tách biệt hệ thống thành 3 phân hệ: Model (Quản lý dữ liệu và logic nghiệp vụ), View (Hiển thị giao diện cho người dùng), và Controller (Tiếp nhận tương tác của người dùng để cập nhật Model và View).
  - **브로커 패턴 (Broker Pattern):**
    - Áp dụng trong hệ thống phân tán không đồng nhất, thành phần Broker đóng vai trò trung gian tiếp nhận yêu cầu từ client và định tuyến đến server phù hợp nhất rồi trả kết quả về (chuẩn CORBA).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Đặc tính nào trong ISO 9126 đo lường khả năng phục hồi (회복성) khi hệ thống gặp sự cố?"* -> **신뢰성 (Độ tin cậy)**, KHÔNG PHẢI 유지보수성 (Bảo trì).
  - **Bẫy 2:** *"Đặc tính nào đo lường khả năng cài đặt (설치성) trên các hệ điều hành khác nhau?"* -> **이식성 (Khả năng khả chuyển)**.
  - **Bẫy 3:** *"Mẫu kiến trúc nào xử lý luồng dữ liệu tuần tự qua các bộ lọc như lệnh pipeline trong UNIX Shell?"* -> **파이프-필터 패턴 (Pipe-Filter Pattern)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "ISO 9126 gồm 6 trụ cột 기신사효유이; Layered phân tầng cách ly, Pipe-Filter lọc luồng dữ liệu, MVC chia tách giao diện nghiệp vụ".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tập con thuộc tính quan trọng của ISO/IEC 9126 thường bị hỏi xoắn:**
  - `결함 허용성 (Fault Tolerance)`: Khi một phân hệ bị lỗi (ví dụ 1 ổ cứng bị cháy), hệ thống vẫn không bị sập mà duy trì chức năng cơ bản -> Thuộc **신뢰성 (Reliability)**.
  - `시험성 (Testability)`: Mức độ dễ dàng để lập trình viên viết unit test kiểm tra từng mô-đun -> Thuộc **유지보수성 (Maintainability)**.
  - `상호운용성 (Interoperability)`: Khả năng hệ thống giao tiếp trơn tru với các phần mềm bên ngoài khác -> Thuộc **기능성 (Functionality)**.

### 복습 체크리스트
- [ ] Nhớ tên và giải thích 6 đặc tính của ISO/IEC 9126: 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성.
- [ ] Phân biệt được 회복성 (Độ tin cậy) và 유지보수성 (Khả năng bảo trì).
- [ ] Nhận diện được đặc trưng của Layered Pattern, Client-Server, Pipe-Filter và MVC.
- [ ] Nắm được nguyên lý hoạt động của Broker Pattern trong hệ thống phân tán.
