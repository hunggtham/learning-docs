# 42. 애플리케이션 테스트 원리 및 관련 용어 (Test Principles & Terms)

## 학습 목표 (Mục tiêu)
- Nắm vững 7 nguyên lý kiểm thử phần mềm nền tảng theo chuẩn quốc tế ISTQB (소프트웨어 테스트 7대 원리).
- Hiểu sâu bản chất các nguyên lý kinh điển thường xuyên xuất hiện trong đề thi: Hiện tượng co cụm lỗi (결함 집중 / 파레토 법칙), Nghịch lý thuốc trừ sâu (살충제 패러독스) và Ngụy biện về sự vắng mặt của lỗi (오류-부재의 궤변).
- Phân biệt bản chất triết học giữa Kiểm tra xác minh kỹ thuật (검증 - Verification: Làm đúng sản phẩm) và Kiểm tra xác nhận người dùng (확인 - Validation: Làm đúng sản phẩm cần thiết).

## 핵심 키워드 (Từ khóa)
- 테스트 7대 원리 (7 Testing Principles)
- 결함 집중 (Defect Clustering / 파레토 법칙 80:20)
- 살충제 패러독스 (Pesticide Paradox / 테스트 케이스 개선)
- 오류-부재의 궤변 (Absence-of-Errors Fallacy)
- 검증 (Verification / 개발자 관점 / "Are we building the product right?")
- 확인 (Validation / 사용자 관점 / "Are we building the right product?")

## 선행·연결 개념 (Kiến thức liên kết)
- [52-bai-hoc.md](52-bai-hoc.md): Kiểm thử hộp trắng vs Kiểm thử hộp đen.
- [56-bai-hoc.md](56-bai-hoc.md): Bản mô tả ca kiểm thử (Test Case).
- [62-bai-hoc.md](62-bai-hoc.md): Chi tiết đối chiếu Kiểm tra xác minh (Verification) vs Xác nhận (Validation).

## 읽는 방법 (Cách đọc)
- Nhớ 3 nguyên lý vàng hay thi nhất:
  - **결함 집중 (Defect Clustering):** 80% lỗi tập trung ở 20% mô-đun phức tạp nhất (Nguyên lý Pareto).
  - **살충제 패러독스 (Pesticide Paradox):** Xịt mãi 1 loại thuốc trừ sâu thì sâu bị nhờn thuốc $\rightarrow$ Chạy mãi 1 bộ Test Case cũ sẽ không tìm thêm được lỗi mới, phải định kỳ viết mới Test Case.
  - **오류-부재의 궤변 (Absence of Errors Fallacy):** Phần mềm không có một con bug nào (0 lỗi) nhưng người dùng không dùng được vì sai nhu cầu thì vẫn là sản phẩm vứt đi.
- Nhớ cặp đôi Verification vs Validation:
  - **Verification (검증):** Góc nhìn **Lập trình viên**, đối chiếu với **Đặc tả kỹ thuật (Spec)**.
  - **Validation (확인):** Góc nhìn **Người dùng cuối**, đối chiếu với **Yêu cầu thực tế (Requirement)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **7 nguyên lý kiểm thử phần mềm chuẩn quốc tế ISTQB:**
  1. **결함 존재 증명 (Testing shows presence of defects):** Kiểm thử chỉ có thể chứng minh là trong phần mềm có lỗi, **không thể chứng minh là phần mềm hoàn toàn sạch bóng lỗi 100%**.
  2. **완벽한 테스팅 불가능 (Exhaustive testing is impossible):** Không thể kiểm thử toàn bộ mọi tổ hợp dữ liệu và mọi đường dẫn thực thi (trừ các trường hợp vô cùng đơn giản).
  3. **조기 테스팅 (Early Testing):** Kiểm thử phải bắt đầu càng sớm càng tốt ngay từ giai đoạn phân tích yêu cầu để giảm chi phí sửa chữa lỗi.
  4. **결함 집중 (Defect Clustering - 파레토 법칙):** Phần lớn các lỗi được tìm thấy thường tập trung trong một số lượng nhỏ các mô-đun phức tạp (Quy luật Pareto: **Khoảng 80% lỗi nằm ở 20% mô-đun**).
  5. **살충제 패러독스 (Pesticide Paradox):** Nếu lặp đi lặp lại mãi cùng một bộ Test Case giống nhau thì sau một thời gian sẽ không thể tìm thấy bất kỳ lỗi mới nào nữa $\rightarrow$ **Bắt buộc phải định kỳ rà soát và bổ sung các ca kiểm thử mới**.
  6. **정황 의존성 (Testing is context dependent):** Kiểm thử phụ thuộc vào ngữ cảnh cụ thể (Phần mềm ngân hàng tài chính yêu cầu kiểm thử an toàn bảo mật gắt gao hơn nhiều so với ứng dụng mạng xã hội).
  7. **오류-부재의 궤변 (Absence-of-Errors Fallacy):** Việc tìm ra và sửa sạch sẽ toàn bộ lỗi được phát hiện không đồng nghĩa với việc hệ thống thành công, nếu phần mềm không đáp ứng đúng mục đích sử dụng thực tế của khách hàng.

- **Bảng phân biệt 검증 (Verification) vs 확인 (Validation):**

| Tiêu chí so sánh | 검증 (Verification - Xác minh kỹ thuật) | 확인 (Validation - Xác nhận người dùng) |
| :--- | :--- | :--- |
| **Góc nhìn đánh giá** | Góc nhìn của **Nhà phát triển (Developer)** | Góc nhìn của **Người sử dụng (User / Customer)** |
| **Câu hỏi triết lý** | *"Are we building the product right?"* (Chúng ta có đang xây dựng sản phẩm đúng quy chuẩn kỹ thuật không?) | *"Are we building the right product?"* (Chúng ta có đang xây dựng đúng sản phẩm mà khách hàng thực sự cần không?) |
| **Đối tượng đối chiếu** | Tài liệu thiết kế chi tiết, kiến trúc, bản đặc tả kỹ thuật | Nhu cầu kinh doanh thực tế, trải nghiệm người dùng cuối |
| **Hình thức kiểm tra** | Review tài liệu, Inspection, Kiểm thử đơn vị (Unit Test), Kiểm thử tích hợp | Kiểm thử hệ thống, Kiểm thử chấp nhận (Alpha / Beta Test) |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Chi phí khắc phục lỗi theo thời gian (Cost of Change):**
  - Chi phí sửa một lỗi phát hiện ở giai đoạn Yêu cầu (Requirements) là rẻ nhất (hệ số $1\times$).
  - Nếu lỗi đó lọt qua giai đoạn Thiết kế, Lập trình và chỉ bị phát hiện khi đã phát hành cho khách hàng (Maintenance), chi phí sửa chữa có thể đội lên gấp **$60 \sim 100$ lần** (bao gồm chi phí bồi thường, thu hồi sản phẩm, mất uy tín thương hiệu).
  - Đây chính là luận cứ khoa học giải thích cho nguyên lý **조기 테스팅 (Early Testing)**.

### 복습 체크리스트
- [ ] Kể tên đầy đủ 7 nguyên lý kiểm thử phần mềm theo chuẩn ISTQB.
- [ ] Giải thích nguyên lý 살충제 패러독스 (Pesticide Paradox) và giải pháp định kỳ cải tiến Test Case.
- [ ] Giải thích nguyên lý 오류-부재의 궤변 (Absence of Errors Fallacy).
- [ ] Phân biệt rõ Verification (Đúng quy chuẩn kỹ thuật) và Validation (Đúng nhu cầu người dùng).
