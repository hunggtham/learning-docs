# 5. 요구공학 (Requirements Engineering)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa và mục tiêu của Kỹ nghệ yêu cầu (`요구공학 - Requirements Engineering`) trong việc kiểm soát vòng đời yêu cầu phần mềm.
- Phân biệt rõ hai nhánh lớn: Phát triển yêu cầu (`요구사항 개발` - Elicitation, Analysis, Specification, Validation) và Quản lý yêu cầu (`요구사항 관리` - Traceability, Baseline, Change Control).
- Nhận diện vai trò của Ma trận truy vết (`RTM`), Hội đồng kiểm soát thay đổi (`CCB`) và quy trình phê duyệt thay đổi yêu cầu.

## 핵심 키워드 (Từ khóa)
- 요구공학 (Kỹ nghệ yêu cầu / Requirements Engineering)
- 요구사항 개발 (Phát triển yêu cầu: 도출, 분석, 명세, 확인)
- 요구사항 관리 (Quản lý yêu cầu / Requirements Management)
- 요구사항 추적성 (Tính truy xuất yêu cầu / Traceability / RTM)
- 형상 관리 (Quản lý cấu hình / Configuration Management / SCM)
- CCB (Change Control Board / 형상 통제 위원회)

## 선행·연결 개념 (Kiến thức liên kết)
- **Từ bài trước ([12. UI 및 아키텍처 설계 심화](21-bai-hoc.md)):** Sau khi xem xét các chỉ dẫn thiết kế UI và các bước chuyển tiếp sang kiến trúc CSDL, bài này củng cố nền tảng quản trị yêu cầu ở quy mô toàn hệ thống.
- **Tiếp nối sang bài sau ([8. UI 및 UX, HCI](23-bai-hoc.md)):** Mở rộng từ kỹ nghệ yêu cầu sang trải nghiệm người dùng toàn diện qua các khái niệm UX và HCI.

## 읽는 방법 (Cách đọc)
- Đọc TẦNG A để phân biệt rạch ròi giữa 2 nhánh: "Phát triển yêu cầu" (sản sinh ra tài liệu SRS) và "Quản lý yêu cầu" (theo dõi và kiểm soát thay đổi sau khi chốt Baseline).
- Đọc TẦNG B để nắm vững luồng xử lý yêu cầu thay đổi từ phía khách hàng thông qua hội đồng CCB.

---

## 5. 요구공학 (Requirements Engineering)

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **개념 (Định nghĩa Kỹ nghệ yêu cầu):** Là một phân ngành của kỹ nghệ phần mềm chuyên nghiên cứu các nguyên tắc, phương pháp và công cụ nhằm tìm hiểu, mô hình hóa, tài liệu hóa và quản lý toàn bộ các yêu cầu của người dùng trong suốt vòng đời dự án (`생명 주기 동안 지속적으로 반복`).
- **2 nhánh cấu trúc của Kỹ nghệ yêu cầu:**
  1. **요구사항 개발 (Phát triển yêu cầu - 4 bước):**
     - `도출 (Elicitation)`: Khám phá nhu cầu qua phỏng vấn, khảo sát, Brainstorming.
     - `분석 (Analysis)`: Phân loại chức năng/phi chức năng, lập mô hình DFD, UML.
     - `명세 (Specification)`: Soạn thảo tài liệu đặc tả yêu cầu phần mềm chuẩn (SRS).
     - `확인 (Validation)`: Thẩm định tài liệu bằng Inspection, Walkthrough và chốt **Đường cơ sở (베이스라인 - Baseline)**.
  2. **요구사항 관리 (Quản lý yêu cầu - Sau khi có Baseline):**
     - `요구사항 협상 (Negotiation)`: Đàm phán phạm vi và chi phí khi có xung đột lợi ích.
     - `요구사항 기준선 (Baseline Setting)`: Thiết lập mốc đóng băng phiên bản tài liệu.
     - `요구사항 변경 통제 (Change Control)`: Tiếp nhận và đánh giá tác động của yêu cầu thay đổi thông qua **Hội đồng kiểm soát thay đổi (CCB - Change Control Board)**.
     - `요구사항 추적 (Traceability)`: Duy trì khả năng truy vết hai chiều giữa yêu cầu và thiết kế, mã nguồn, ca kiểm thử (bằng ma trận RTM).
- **주의/함정 (Bẫy đề thi dễ nhầm):**
  - **Bẫy 1:** *"Hoạt động quản lý thay đổi (변경 통제) và theo dõi truy vết (추적) thuộc nhánh Phát triển yêu cầu?"* -> **Sai**. Thuộc nhánh **Quản lý yêu cầu (요구사항 관리)**.
  - **Bẫy 2:** *"Hội đồng phê duyệt yêu cầu thay đổi trong dự án phần mềm viết tắt là gì?"* -> **CCB (Change Control Board)**.
  - **Bẫy 3:** *"Kỹ nghệ yêu cầu chỉ diễn ra ở giai đoạn đầu rồi kết thúc hẳn?"* -> **Sai**. Kỹ nghệ yêu cầu lặp đi lặp lại và đồng hành trong suốt toàn bộ vòng đời phát triển (`생명 주기 전 과정`).
- **한 문장 설명 (Câu chốt ghi nhớ):** "Kỹ nghệ yêu cầu gồm 2 cánh tay: Phát triển tạo ra Baseline, Quản lý dùng CCB và RTM kiểm soát thay đổi".

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình kiểm soát thay đổi (Change Control Workflow) qua CCB:**
  1. Khách hàng hoặc lập trình viên gửi Phiếu yêu cầu thay đổi (CR - Change Request).
  2. Nhóm kỹ thuật phân tích tác động (Impact Analysis) đến kiến trúc, chi phí và tiến độ.
  3. Hội đồng CCB họp đánh giá: Chấp thuận (Approve), Từ chối (Reject), hoặc Hoãn lại (Defer).
  4. Nếu chấp thuận, tiến hành sửa tài liệu SRS, cập nhật Baseline mới và thông báo cho toàn bộ đội ngũ.

### 복습 체크리스트
- [ ] Định nghĩa được 요구공학 và khẳng định nó diễn ra liên tục trong suốt vòng đời.
- [ ] Phân biệt rõ ràng 2 nhánh: 요구사항 개발 (Phát triển) và 요구사항 관리 (Quản lý).
- [ ] Nắm được vai trò của CCB (Change Control Board) trong quy trình duyệt thay đổi.
- [ ] Giải thích được tầm quan trọng của ma trận truy vết RTM trong quản lý yêu cầu.
