# 7. 공통 모듈 (Common Module)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và vai trò của Mô-đun dùng chung (`공통 모듈 - Common Module`) trong việc tối ưu hóa tái sử dụng mã nguồn và chuẩn hóa quy trình phát triển.
- Thuộc nằm lòng 5 nguyên tắc vàng khi viết tài liệu đặc tả mô-đun dùng chung (`공통 모듈 명세 기법 5대 원칙`): Tính chính xác (`정확성`), Tính rõ ràng (`명확성`), Tính đầy đủ (`완전성`), Tính nhất quán (`일관성`), và Tính truy xuất nguồn gốc (`추적성`).
- Nhận diện các vi phạm và bẫy đề thi về đặc tả mô-đun dùng chung trong kỹ nghệ phần mềm.

## 핵심 키워드 (Từ khóa)
- 공통 모듈 (Mô-đun dùng chung / Common Module / 재사용성)
- 공통 모듈 명세 기법 (5 nguyên tắc đặc tả mô-đun dùng chung)
- 정확성 (Tính chính xác / Correctness)
- 명확성 (Tính rõ ràng / Clarity)
- 완전성 (Tính đầy đủ / Completeness)
- 일관성 (Tính nhất quán / Consistency)
- 추적성 (Tính truy xuất / Traceability)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([2. 모듈 (Module) & 독립성 (Independence)](31-bai-hoc.md)):** Sau khi hiểu các cấp độ kết hợp và gắn kết, bài này cụ thể hóa việc áp dụng vào các mô-đun dùng chung xuyên suốt toàn hệ thống.
- **Tiếp nối sang bài sau ([9. 효과적인 모듈 설계 방안](33-bai-hoc.md)):** Mở rộng các chiến lược thiết kế mô-đun hiệu quả về mặt phân cấp điều khiển (Fan-in / Fan-out) và phạm vi tác động.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để thuộc nằm lòng 5 chữ cái thần chú: **정 - 명 - 완 - 일 - 추** (Chính xác, Minh bạch, Hoàn chỉnh, Nhất quán, Truy xuất) - đây là câu hỏi lựa chọn xuất hiện thường xuyên trong đề thi.
- Đọc TẦNG B để hiểu tại sao tính truy xuất (추적성) là điều kiện bắt buộc để bảo trì và nâng cấp các mô-đun dùng chung quy mô lớn.

---

## 7. 공통 모듈 (Common Module)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Mô-đun dùng chung):**
  - Là các mô-đun chức năng chuẩn hóa độc lập được thiết kế để **nhiều chương trình, phân hệ khác nhau trong toàn bộ hệ thống có thể cùng gọi và tái sử dụng (`여러 프로그램에서 공통으로 재사용`)**.
  - Ví dụ tiêu biểu: Mô-đun xác thực người dùng (Login / JWT Auth), Mô-đun mã hóa dữ liệu (SHA-256), Mô-đun xử lý ngày tháng, Mô-đun gửi thông báo Notification.
- **공통 모듈 명세 기법 5대 원칙 (5 nguyên tắc viết đặc tả mô-đun dùng chung):**
  1. **정확성 (Correctness - Tính chính xác):**
     - Mô tả chính xác các chức năng cần thiết mà hệ thống yêu cầu, không thừa không thiếu, để quá trình cài đặt mã nguồn diễn ra hoàn toàn chuẩn xác (`해당 기능이 필요하다는 것을 정확히 작성`).
  2. **명확성 (Clarity - Tính rõ ràng / Minh bạch):**
     - Nội dung đặc tả phải dễ hiểu, mạch lạc, **chỉ có duy nhất một cách hiểu, không bị mơ hồ hay đa nghĩa (`모호하지 않게 하나로만 해석`)**.
  3. **완전성 (Completeness - Tính đầy đủ / Hoàn chỉnh):**
     - Tài liệu phải bao quát trọn vẹn toàn bộ các luồng xử lý, bao gồm cả luồng nghiệp vụ thông thường lẫn các trường hợp ngoại lệ (Exception Handling) phát sinh, không bỏ sót bất kỳ chi tiết nào.
  4. **일관성 (Consistency - Tính nhất quán):**
     - Các quy ước đặt tên, kiểu dữ liệu, thông điệp phản hồi và định dạng giao tiếp phải đồng bộ xuyên suốt, **không xảy ra bất kỳ xung đột hay mâu thuẫn nào (`상호 충돌이 발생하지 않도록`)** với các mô-đun khác.
  5. **추적성 (Traceability - Tính truy xuất nguồn gốc):**
     - Mỗi mô-đun dùng chung phải liên kết trực tiếp với mã định danh yêu cầu ban đầu (Requirement ID) và các trường hợp kiểm thử (Test Cases), **cho phép dễ dàng truy vết nguồn gốc và lịch sử thay đổi (`요구사항과의 유기적 연결 관계 추적`)**.
  - 💡 **Thần chú ghi nhớ 5 nguyên tắc:** **정 - 명 - 완 - 일 - 추** (Chính - Minh - Hoàn - Nhất - Truy).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** Đề thi đưa các từ như `복잡성 (Tính phức tạp)`, `효율성 (Tính hiệu quả)` hoặc `다양성 (Tính đa dạng)` và hỏi có phải nguyên tắc đặc tả mô-đun dùng chung không -> **Không phải**. Bộ 5 nguyên tắc chuẩn chỉ gồm: **정확성, 명확성, 완전성, 일관성, 추적성**.
  - **Bẫy 2:** *"Đặc tả chỉ cần mô tả luồng chạy thành công bình thường, các trường hợp lỗi sẽ do dev tự xử lý?"* -> **Vi phạm Tính đầy đủ (완전성)**.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Mô-đun dùng chung là tái sử dụng nhiều nơi; đặc tả chuẩn phải đủ 5 tiêu chí Chính - Minh - Hoàn - Nhất - Truy (정명완일추)".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Tầm quan trọng của Mô-đun dùng chung trong kiến trúc Microservices:**
  - Trong các hệ thống lớn (như ứng dụng ngân hàng hay sàn thương mại điện tử), các chức năng chung như `Ghi nhận Log hệ thống` hay `Kiểm tra chữ ký số` nếu mỗi nhóm tự viết một kiểu sẽ gây ra tình trạng phân mảnh, sai lệch bảo mật và tốn gấp 10 lần chi phí bảo trì.
  - Việc đóng gói thành các thư viện dùng chung (Common Libraries / Shared Modules) tuân thủ 5 nguyên tắc đặc tả giúp đảm bảo khi sửa một lỗi bảo mật tại Common Module, toàn bộ hệ thống được vá lỗi đồng bộ ngay lập tức.

### 복습 체크리스트
- [ ] Nêu định nghĩa và ít nhất 3 ví dụ thực tế của 공통 모듈 (Common Module).
- [ ] Đọc thuộc lòng 5 nguyên tắc viết đặc tả mô-đun dùng chung bằng thần chú: 정 - 명 - 완 - 일 - 추.
- [ ] Giải thích ý nghĩa của 정확성 (Chính xác) và 명확성 (Rõ ràng, một cách hiểu).
- [ ] Nhớ 추적성 là khả năng liên kết truy vết với tài liệu yêu cầu ban đầu.
