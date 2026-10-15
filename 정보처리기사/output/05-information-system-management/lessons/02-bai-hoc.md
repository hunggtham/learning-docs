# 소프트웨어 개발 방법론 테일러링 및 프레임워크 (Tailoring & Framework)

## 학습 목표 (Mục tiêu)
- Nắm vững định nghĩa, sự cần thiết và quy trình thực hiện "Cắt may phương pháp luận" (방법론 테일러링 - Methodology Tailoring) nhằm tùy biến quy trình phát triển cho phù hợp với từng dự án phần mềm.
- Phân biệt chính xác giữa **Tiêu chí nội bộ (내부적 기준)** và **Tiêu chí bên ngoài (외부적 기준)** khi tiến hành Tailoring trong doanh nghiệp.
- Nhận diện các bộ khung phát triển ứng dụng máy chủ tiêu biểu: Spring Framework (Java), Microsoft .NET, và Khung chính phủ điện tử Hàn Quốc (**전자정부 프레임워크 - eGovFrame**).

## 핵심 키워드 (Từ khóa)
- 방법론 테일러링 (Methodology Tailoring)
- 내부적 기준 (Internal: 목표 환경, 요구사항, 프로젝트 규모, 보유 기술)
- 외부적 기준 (External: 법적 제약사항, 표준 품질 기준)
- 소프트웨어 개발 프레임워크 (Framework)
- 스프링 프레임워크 (Spring Framework - Java)
- 닷넷 프레임워크 (.NET Framework - Microsoft)
- 전자정부 표준 프레임워크 (eGovFrame - 공공부문 표준)

## 선행·연결 개념 (Kiến thức liên kết)
- [01-bai-hoc.md](01-bai-hoc.md): Đại cương về các phương pháp luận phát triển phần mềm (Cấu trúc, CBD, Agile).
- [03-bai-hoc.md](03-bai-hoc.md): Đặc tính của Framework (IoC) và các công nghệ mới SDE, SDN.
- [06-bai-hoc.md](06-bai-hoc.md): Quản trị dự án phần mềm và quản lý rủi ro.

## 읽는 방법 (Cách đọc)
- Điểm mấu chốt khi giải câu hỏi phân loại Tailoring trong đề thi kỹ sư CNTT:
  - **Tiêu chí nội bộ (내부적 기준):** Những yếu tố nằm trong tầm kiểm soát của nội bộ dự án và công ty:
    - Mục tiêu môi trường hệ thống (Target Environment).
    - Đặc thù yêu cầu của khách hàng (Requirements).
    - Quy mô dự án (Project Scale: thời gian, ngân sách, số lượng nhân sự).
    - Trình độ công nghệ và kỹ năng của nhân sự hiện có (Tech Stack, Skill).
  - **Tiêu chí bên ngoài (외부적 기준):** Những yếu tố khách quan từ bên ngoài ép buộc dự án phải tuân thủ:
    - **Ràng buộc về mặt pháp luật và chính sách nhà nước (법적 제약사항 / Legal Compliance)**.
    - **Tiêu chuẩn chất lượng chuẩn hóa của ngành (표준 품질 기준 / ISO, CMMI)**.

---

### TẦNG A – GHI CHÚ NÉN (ÔN / ĐI THI)
- **1. Bảng phân loại các tiêu chí cắt may phương pháp luận (Methodology Tailoring):**

| Nhóm tiêu chí | Tên tiếng Hàn & Anh | Yếu tố khảo sát chi tiết |
| :--- | :--- | :--- |
| **Tiêu chí nội bộ** (Internal) | **내부적 기준** | **목표 환경 (Môi trường mục tiêu):** Hệ điều hành, cơ sở dữ liệu, nền tảng phần cứng; **요구사항 (Yêu cầu):** Mức độ phức tạp nghiệp vụ, tần suất thay đổi; **프로젝트 규모 (Quy mô dự án):** Tổng chi phí ngân sách, thời hạn bàn giao, số lượng nhân sự; **보유 기술 (Công nghệ sẵn có):** Độ thành thạo của lập trình viên về công cụ và quy trình. |
| **Tiêu chí bên ngoài** (External) | **외부적 기준** | **법적 제약사항 (Ràng buộc pháp lý):** Luật bảo vệ thông tin cá nhân, luật sở hữu trí tuệ, quy định về chữ ký số, quy chuẩn bảo mật bắt buộc; **표준 품질 기준 (Tiêu chuẩn chất lượng):** Yêu cầu đạt các chứng chỉ quốc tế như ISO/IEC 12207, ISO 9001, CMMI Level 3 trở lên. |

- **2. Bảng tổng hợp các Framework phát triển phần mềm phổ biến:**

| Tên Framework | Nền tảng cốt lõi | Đặc điểm kiến trúc & Lĩnh vực áp dụng |
| :--- | :--- | :--- |
| **스프링 (Spring)** | **Java / JVM** | Mã nguồn mở toàn cầu, kiến trúc phân tầng linh hoạt; hạt nhân là cơ chế Đảo ngược điều khiển (**IoC**) và Tiêm phụ thuộc (**DI**), hỗ trợ lập trình hướng khía cạnh (**AOP**). |
| **닷넷 (.NET)** | **Microsoft / C#, VB** | Môi trường phát triển tích hợp đa ngôn ngữ của Microsoft chạy trên nền tảng máy ảo Common Language Runtime (CLR); hỗ trợ giao tiếp Windows API và đám mây Azure mạnh mẽ. |
| **전자정부 프레임워크** (eGovFrame) | **Java (Spring 기반)** | Bộ khung chuẩn do Chính phủ Hàn Quốc (Bộ Nội vụ và Hành chính an toàn) xây dựng dựa trên Spring Framework nhằm chuẩn hóa hạ tầng CNTT công, tránh phụ thuộc vào các tập đoàn giải pháp tư nhân độc quyền. |

### TẦNG B – GHI CHÚ BỔ SUNG (HIỂU SÂU)
- **Quy trình 3 bước thực hiện Tailoring chuẩn:**
  1. *Khảo sát đặc trưng dự án:* Đánh giá rủi ro, phân loại quy mô (Nhỏ, Vừa, Lớn), xác định công nghệ.
  2. *Lựa chọn phương pháp luận nền tảng:* Chọn Agile cho dự án startup yêu cầu thay đổi liên tục, hoặc Waterfall/Cấu trúc cho dự án tài chính ngân hàng yêu cầu tài liệu nghiệm thu nghiêm ngặt.
  3. *Tùy biến tài liệu và quy trình (Tailoring):* Lược bỏ các tài liệu rườm rà không cần thiết, bổ sung các biểu mẫu kiểm thử bảo mật đặc thù, phê duyệt bản hướng dẫn quy trình của dự án.

### 복습 체크리스트
- [ ] Phân biệt được tiêu chí nội bộ (Môi trường, Yêu cầu, Quy mô, Kỹ năng) và tiêu chí bên ngoài (Pháp luật, Tiêu chuẩn chất lượng).
- [ ] Nhớ eGovFrame là khung chính phủ điện tử của Hàn Quốc được xây dựng dựa trên nền Spring của Java.
- [ ] Nắm được mục đích của Tailoring: Điều chỉnh phương pháp luận chuẩn cho vừa vặn với thực tế dự án.
- [ ] Khẳng định .NET do Microsoft phát triển trên máy ảo CLR.
