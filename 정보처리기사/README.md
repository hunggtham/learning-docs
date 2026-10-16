# Giám sát Toàn diện & Lộ trình Chinh phục Kỹ sư Xử lý Thông tin (정보처리기사 Master Hub)

Chào mừng bạn đến với **Cổng thông tin và Giáo trình chuẩn hóa Kỹ sư Xử lý Thông tin** (`정보처리기사`). Đây là chứng chỉ kỹ thuật quốc gia (국가기술자격) uy tín nhất do Cơ quan Phát triển Nguồn nhân lực Hàn Quốc (HRD Korea - 한국산업인력공단) quản lý theo khung tiêu chuẩn năng lực nghề nghiệp quốc gia (NCS - National Competency Standards).

Chứng chỉ là điều kiện tiên quyết và căn cứ pháp lý quan trọng để:
- Tích lũy tối đa điểm cộng trong xét tuyển công chức kỹ thuật và doanh nghiệp công (공기업/공무원 가산점).
- Đạt điều kiện kỹ sư phần mềm chuyên nghiệp khi xin và chuyển đổi visa lao động kỹ thuật cao tại Hàn Quốc (E-7-1, F-2-7 điểm số, và thường trú nhân F-5).

---

## 1. Cấu trúc Khảo thí & Tiêu chuẩn Đỗ (HRD Korea Standard)

Kỳ thi bao gồm 2 giai đoạn độc lập: **Thi Lý thuyết (필기)** trên máy tính (CBT) và **Thi Thực hành tự luận (실기)**.

| Hạng mục khảo thí | Thi Lý thuyết (필기 - CBT) | Thi Thực hành (실기 - Tự luận) |
| :--- | :--- | :--- |
| **Hình thức** | Trắc nghiệm 4 lựa chọn trên máy tính (CBT) | Tự luận viết tay / gõ máy (Short answer, Code, SQL) |
| **Quy mô môn học** | 5 môn trọng tâm (20 câu / môn = 100 câu) | 1 môn tổng hợp nghiệp vụ thực tế (20 câu) |
| **Thời gian làm bài** | 150 phút (2 giờ 30 phút) | 150 phút (2 giờ 30 phút) |
| **Thang điểm** | 100 điểm (20 điểm / môn) | 100 điểm |
| **Tiêu chuẩn đỗ** | Điểm trung bình $\ge 60/100$, không môn nào $< 40$ (과락) | Tổng điểm bài thi $\ge 60/100$ |

> [!WARNING] Cạm bẫy trượt điểm liệt (과락 - 40점 미만):
> Dù điểm tổng 4 môn khác đạt tối đa, chỉ cần 1 môn dưới 40 điểm (dưới 8 câu đúng trên 20 câu), thí sinh sẽ bị **trượt ngay lập tức**. Hai môn có tỷ lệ trượt điểm liệt cao nhất lịch sử là **Môn 4 (프로그래밍 언어 활용)** do bẫy con trỏ/đệ quy và **Môn 5 (정보시스템 구축관리)** do dung lượng thuật ngữ bảo mật và công thức ước lượng chi phí quá rộng.

---

## 2. Bản đồ 5 Môn học Trọng tâm (Core Subjects)

Toàn bộ 84 bài giảng chi tiết đã được biên soạn công phu, chuẩn hóa thuật ngữ ba thứ tiếng **Hàn – Anh – Việt** và vượt qua 100% kiểm định chất lượng:

```text
정보처리기사/output/
├── 01-software-design/               (12 bài học: Phân tích yêu cầu, UML, Pattern, Giao diện)
├── 02-software-development/          (19 bài học: Cấu trúc dữ liệu, Thuật toán, Kiểm thử, Refactoring)
├── 03-database-construction/         (13 bài học: Mô hình hóa, SQL, Chuẩn hóa 1NF-BCNF, Transaction)
├── 04-programming-language/          (22 bài học: C, Java OOP, Python, Bộ nhớ, Concurrency)
└── 05-information-system-management/ (18 bài học: Bảo mật mạng, Đám mây, Quản lý dự án, Khôi phục thảm họa)
```

### Chi tiết các môn học:

1. **[Môn 1: Thiết kế Phần mềm (소프트웨어 설계)](output/01-software-design/README.md)**
   - Khung phát triển Agile, XP, Scrum; Thu thập và phân tích yêu cầu phần mềm.
   - Mô hình hóa UML (Use Case, Sequence, Class, State, Activity Diagram).
   - Thiết kế kiến trúc (Architecture Pattern: MVC, Layered, Pipe-and-Filter, Microservices).
   - Design Patterns (GoF 23 mẫu: Creational, Structural, Behavioral).
   - *Tài liệu tổng hợp:* [Giáo trình đầy đủ Môn 1](output/01-software-design/01-tai-lieu-hoc-day-du.md)

2. **[Môn 2: Phát triển Phần mềm (소프트웨어 개발)](output/02-software-development/README.md)**
   - Cấu trúc dữ liệu nâng cao (Stack, Queue, Tree, Heap, Graph) và thuật toán (Sắp xếp, Tìm kiếm).
   - Chiến lược kiểm thử phần mềm: White-box (Statement, Branch, Condition coverage) và Black-box (Equivalence Partitioning, Boundary Value Analysis).
   - Mức độ kiểm thử (Unit, Integration, System, Acceptance Test).
   - Quản lý phiên bản mã nguồn (Git, Branching models) và Refactoring làm sạch code.
   - *Tài liệu tổng hợp:* [Giáo trình đầy đủ Môn 2](output/02-software-development/01-tai-lieu-hoc-day-du.md)

3. **[Môn 3: Xây dựng Cơ sở Dữ liệu (데이터베이스 구축)](output/03-database-construction/README.md)**
   - Mô hình dữ liệu quan hệ (Relational Model), Đại số quan hệ (Relational Algebra).
   - Toàn vẹn dữ liệu (Entity Integrity, Referential Integrity, Domain Integrity).
   - Chuẩn hóa cơ sở dữ liệu từ 1NF, 2NF, 3NF, BCNF đến 4NF, 5NF và bẫy phản chuẩn hóa (Denormalization).
   - Phân tích Transaction (ACID properties), Khóa và Điều khiển tương thời (Concurrency Control / Locking).
   - Tối ưu hóa truy vấn SQL, Khung nhìn (View), Chỉ mục (Index) và Clustered vs Non-Clustered.
   - *Tài liệu tổng hợp:* [Giáo trình đầy đủ Môn 3](output/03-database-construction/01-tai-lieu-hoc-day-du.md)

4. **[Môn 4: Ứng dụng Ngôn ngữ Lập trình (프로그래밍 언어 활용)](output/04-programming-language/README.md)**
   - Cốt lõi ngôn ngữ C: Cú pháp, con trỏ mảng (`*p`, `**p`), thao tác chuỗi, hàm đệ quy, cấp phát động.
   - Hướng đối tượng với Java: Kế thừa (Inheritance), Nạp chồng (Overloading), Ghi đè (Overriding), Tính đa hình (Polymorphism), Quản lý Ngoại lệ (Exception).
   - Cú pháp và cấu trúc dữ liệu Python: List slicing, Dictionary, Lambda, Map/Filter.
   - Quản lý bộ nhớ hệ thống: Phân vùng Code, Data, Heap, Stack, Thu gom rác (Garbage Collection).
   - Hệ điều hành & Tiến trình: Scheduling algorithms (FCFS, SJF, RR, SRT), Deadlock 4 điều kiện và Banker's Algorithm.
   - *Tài liệu tổng hợp:* [Giáo trình đầy đủ Môn 4](output/04-programming-language/01-tai-lieu-hoc-day-du.md)

5. **[Môn 5: Quản lý Xây dựng Hệ thống Thông tin (정보시스템 구축관리)](output/05-information-system-management/README.md)**
   - Phương pháp luận phát triển phần mềm và mô hình ước tính chi phí (COCOMO, Putnam, Function Point).
   - Mạng máy tính: Mô hình OSI 7 tầng, TCP/IP, Định tuyến IP, Subnetting CIDR.
   - Mật mã học: Khóa đối xứng (DES, AES, SEED, ARIA) vs Khóa bất đối xứng (RSA, ECC), Hàm băm (SHA, MD5).
   - An toàn thông tin: Tấn công mạng (DDoS, XSS, CSRF, SQL Injection), Tường lửa, IDS, IPS.
   - Công nghệ mới: Điện toán đám mây (IaaS, PaaS, SaaS), Docker, Kubernetes, Big Data, Blockchain.
   - *Tài liệu tổng hợp:* [Giáo trình đầy đủ Môn 5](output/05-information-system-management/01-tai-lieu-hoc-day-du.md)

---

## 3. Hệ sinh thái Chuyên sâu 2026 (2026 Depth Path)

Nhằm đáp ứng yêu cầu nâng cao độ khó trong các kỳ thi gần đây, thư mục [`output/2026-depth/`](output/2026-depth/README.md) cung cấp 12 cẩm nang phòng thi chuyên biệt:

- **Bản đồ Liên môn & Vở bài tập:**
  - [Bản đồ Kết nối Liên môn (Cross-Subject Connection Map)](output/2026-depth/07-cross-subject-connection-map.md): Cách một yêu cầu nghiệp vụ đi xuyên qua cả 5 môn học.
  - [Vở Bài tập Xử lý Thủ tục & Thuật toán (Procedural Workbook)](output/2026-depth/08-procedural-workbook.md): Luyện tập tính toán Subnetting, Function Point, Deadlock và Chuẩn hóa.
- **Tránh Bẫy & Phòng Thí nghiệm:**
  - [Cẩm nang Bẫy Nhầm lẫn Nguy cơ Cao (High-Risk Confusion Atlas)](output/2026-depth/11-high-risk-confusion-atlas.md): Phân biệt chính xác các cặp thuật ngữ dễ nhầm (Coupling vs Cohesion, Black-box vs White-box).
  - [Phòng Thí nghiệm Tình huống Nâng cao (Advanced Scenario Labs)](output/2026-depth/12-advanced-scenario-labs.md): Phân tích bài toán kiến trúc thực tế.
- **Thuật ngữ & Xử lý Ngoại lệ:**
  - [Cầu nối Thuật ngữ Hàn - Anh - Việt (Korean Term Bridge)](output/2026-depth/13-korean-term-bridge.md): Từ điển thuật ngữ kỹ thuật chuẩn phục vụ phòng thi CBT.
  - [Bản đồ Khắc phục Lỗi Kỹ thuật (Error Remediation Map)](output/2026-depth/14-error-remediation-map.md): Xử lý các lỗi biên dịch, runtime và ngoại lệ phổ biến.
  - [Bổ sung Bao phủ Trường hợp Biên (Edge-Case Coverage Supplement)](output/2026-depth/15-edge-case-coverage-supplement.md): Quét các câu hỏi hiếm gặp trong đề thi những năm gần đây.

---

## 4. Cẩm nang Chiến thuật Phòng thi Thực chiến

1. **Phân bổ thời gian lý thuyết (150 phút cho 100 câu):**
   - Vòng 1 (60 phút): Quét qua toàn bộ 100 câu, giải dứt điểm các câu lý thuyết định nghĩa ở Môn 1, 2, 3 và 5.
   - Vòng 2 (50 phút): Dành toàn bộ sự tập trung cho Môn 4 để tính nháp từng bước mã nguồn C/Java/Python và Môn 5 cho các bài toán mạng/chi phí.
   - Vòng 3 (30 phút): Rà soát lại các câu đánh dấu nghi ngờ, kiểm tra bẫy phủ định ("올바르지 않은 것은?").
   - 10 phút cuối: Kiểm tra màn hình nộp bài CBT, bảo đảm không bỏ sót câu hỏi nào.
2. **Kỹ thuật đọc từ khóa đề thi tiếng Hàn:**
   - Chú ý các từ khóa loại trừ: `아닌 것` (không phải), `틀린 것` (sai), `가장 거리가 먼 것` (xa rời thực tế nhất).
   - Nắm chắc các cặp đối nghịch: `결합도`(Coupling - càng thấp càng tốt) vs `응집도`(Cohesion - càng cao càng tốt).

---

## 5. Điều hướng Liên kết Hệ thống

- [Quay về Cổng Chứng chỉ Chuyên môn Quốc gia](../cert/README.md)
- [Cẩm nang Tổng quan Kỳ thi Lý thuyết 2026](output/00-2026-written-exam-master-guide.md)
- [Ma trận Độ phủ Đề thi (Coverage Matrix)](output/COVERAGE_MATRIX.md)
- [Sổ Đăng ký Nghiên cứu & Tham chiếu (Research Register)](output/RESEARCH_REGISTER.md)
