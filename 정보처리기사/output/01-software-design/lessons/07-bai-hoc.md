# 2. 요구사항 정의 (Requirements Definition)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa chuẩn của Yêu cầu phần mềm (`요구사항`) theo tiêu chuẩn kỹ nghệ phần mềm và vai trò làm nền tảng cho toàn bộ quá trình thiết kế, lập trình và kiểm thử.
- Thiết lập bảng so sánh đối chiếu toàn diện giữa Yêu cầu chức năng (`기능 요구사항`) và Yêu cầu phi chức năng (`비기능 요구사항`), phân loại chính xác các ví dụ thực tế.
- Khắc sâu chu trình 4 bước của kỹ nghệ yêu cầu: Thu thập (`도출`) -> Phân tích (`분석`) -> Đặc tả (`명세`) -> Xác minh (`확인/검증`).

## 핵심 키워드 (Từ khóa)
- 요구사항 정의 (Định nghĩa yêu cầu / Requirements Definition)
- 기능 요구사항 (Yêu cầu chức năng / Functional Requirements)
- 비기능 요구사항 (Yêu cầu phi chức năng / Non-functional Requirements)
- 요구공학 프로세스 (Quy trình kỹ nghệ yêu cầu / Requirements Engineering Process)
- 베이스라인 (Đường cơ sở / Baseline)
- 추적성 (Tính truy xuất nguồn gốc / Traceability)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([10. 요구사항 심화](06-bai-hoc.md)):** Sau khi tìm hiểu các kỹ thuật đặc tả hình thức và công cụ CASE, bài này chuẩn hóa định nghĩa yêu cầu và cách thiết lập tài liệu yêu cầu hoàn chỉnh.
- **Tiếp nối sang bài sau ([3. 요구사항 분석기법 및 자동화 도구](08-bai-hoc.md)):** Từ định nghĩa yêu cầu, bước tiếp theo là đi sâu vào các công cụ phân tích có cấu trúc như DFD, Từ điển dữ liệu và HIPO để chuẩn hóa luồng xử lý.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để nắm vững ma trận phân biệt Chức năng và Phi chức năng - câu hỏi phân loại này xuất hiện trong hầu hết các đề thi.
- Đọc TẦNG B để hiểu tầm quan trọng của việc đóng băng yêu cầu thành Baseline trước khi bước vào giai đoạn thiết kế kiến trúc.

---

## 2. 요구사항 정의 (Requirements Definition)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa yêu cầu phần mềm):** Là các điều kiện hoặc năng lực mà hệ thống phải đáp ứng để người dùng giải quyết được vấn đề thực tế, hoặc các điều kiện mà hệ thống phải thỏa mãn để tuân thủ hợp đồng, tiêu chuẩn và quy định kỹ thuật.
- **So sánh phân biệt đối chiếu chức năng vs phi chức năng:**
  - **기능 요구사항 (Yêu cầu chức năng - What to do):**
    - Trực tiếp mô tả các dịch vụ, chức năng mà hệ thống cung cấp (`시스템이 무엇을 하는지`).
    - Quy định dữ liệu đầu vào, các bước tính toán, xử lý và dữ liệu đầu ra hiển thị cho người dùng.
    - Ví dụ: Người dùng có thể tìm kiếm sản phẩm theo tên; Hệ thống tự động tính thuế VAT 10%; Gửi email xác nhận sau khi thanh toán thành công.
  - **비기능 요구사항 (Yêu cầu phi chức năng - How well to do):**
    - Quy định các ràng buộc về chất lượng, hiệu năng, bảo mật và môi trường vận hành (`품질, 성능, 보안, 제약조건`).
    - Các nhóm chỉ tiêu chính:
      - `성능 (Hiệu năng)`: Thời gian phản hồi trang dưới 2 giây; Khả năng xử lý 5.000 truy vấn đồng thời.
      - `보안 (Bảo mật)`: Dữ liệu cá nhân phải được mã hóa theo chuẩn AES-256; Đăng nhập sai 5 lần khóa tài khoản.
      - `신뢰성 / 가용성 (Độ tin cậy / Sẵn sàng)`: Hệ thống hoạt động 99.9% thời gian trong năm (MTBF cao, MTTR thấp).
      - `호환성 / 제약 (Tương thích / Ràng buộc)`: Chạy mượt mà trên trình duyệt Chrome, Safari và hệ điều hành iOS, Android.
- **Quy trình 4 bước phát triển yêu cầu (요구사항 개발 프로세스):**
  1. `도출 (Elicitation)`: Tìm hiểu nhu cầu khách hàng qua phỏng vấn, khảo sát, quan sát thực tế.
  2. `분석 (Analysis)`: Phân loại, làm rõ các điểm mơ hồ, phát hiện và hòa giải xung đột lợi ích giữa các bên liên quan.
  3. `명세 (Specification)`: Ghi lại thành văn bản chuẩn xác trong Tài liệu đặc tả yêu cầu phần mềm (SRS).
  4. `확인 및 검증 (Validation & Verification)`: Khách hàng và chuyên gia cùng rà soát, ký duyệt chốt Baseline.
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Tốc độ truyền dữ liệu của hệ thống đạt tối thiểu 100Mbps là yêu cầu chức năng?"* -> **Sai**. Đây là yêu cầu phi chức năng thuộc nhóm hiệu năng (성능 요구사항).
  - **Bẫy 2:** *"Xác minh (Verification) kiểm tra xem yêu cầu có đáp ứng đúng nhu cầu thực tế của người dùng hay không?"* -> **Sai**. Đó là Xác nhận (Validation). Verification chỉ kiểm tra xem sản phẩm có làm đúng theo đặc tả hay không.
- **한 문장 설명 (Câu chốt ghi nhớ):** "Chức năng là làm gì (What), Phi chức năng là tốt thế nào (Quality); quy trình Đồ - Phân - Minh - Xác tạo nên Baseline".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Ý nghĩa sống còn của Đường cơ sở (Baseline):**
  - Sau khi giai đoạn xác minh yêu cầu hoàn tất và được các bên ký duyệt, tài liệu SRS trở thành Đường cơ sở (Baseline). Mọi thay đổi phát sinh sau thời điểm này đều phải thông qua Hội đồng kiểm soát thay đổi (CCB - Change Control Board) và đánh giá lại chi phí, lịch trình. Nếu không có Baseline, dự án sẽ rơi vào tình trạng "Phình phạm vi" (Scope Creep) dẫn đến trễ hạn và phá sản.
- **Ví dụ phân biệt chi tiết trong đề thi:**
  - *"Hệ thống phải cung cấp chức năng rút tiền tại cây ATM"* -> **기능 요구사항**.
  - *"Thời gian đếm và nhả tiền tại cây ATM không được quá 15 giây"* -> **비기능 요구사항 (성능)**.
  - *"Giao diện ATM phải có hướng dẫn bằng âm thanh cho người khiếm thị"* -> **비기능 요구사항 (사용성 / Usability)**.

### 복습 체크리스트
- [ ] Nêu định nghĩa chuẩn của yêu cầu phần mềm và vai trò của nó.
- [ ] Phân loại chính xác 5 ví dụ thực tế thành yêu cầu chức năng hoặc phi chức năng.
- [ ] Nhớ tên và thứ tự của 4 bước trong quy trình phát triển yêu cầu.
- [ ] Giải thích được khái niệm 베이스라인 (Baseline) và tại sao phải chốt Baseline sau bước xác minh.
