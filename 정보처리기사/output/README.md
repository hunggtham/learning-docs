# 정보처리기사 — Bộ tài liệu học

> **Nếu mục tiêu hiện tại là thi lại phần 필기, hãy bắt đầu từ [정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng](00-2026-written-exam-master-guide.md), không bắt đầu bằng cách đọc tuần tự hàng trăm lesson nhỏ.**

Tài liệu được chia thành 5 môn theo cấu trúc 필기 hiện hành. Các file cũ vẫn được giữ để tra cứu sâu theo chủ đề; master guide đóng vai trò **coverage map** để biết phần nào bắt buộc phải học, phần nào đang yếu và phần nào dễ bị nhầm trong đề.

## 2026 필기 — luồng học ưu tiên

1. [**Master Guide 2026 — học sâu + phủ toàn bộ 5 môn**](00-2026-written-exam-master-guide.md)
2. [**Deep-Dive Track 2026 — 5 môn + workbook + scenario + recall + remediation + 2 full mock**](2026-depth/README.md)
3. Học 5 deep-dive để hiểu concept theo mechanism, không chỉ thuộc definition.
4. Dùng `Cross-Subject Connection Map` để nối requirement → design → code → DB → OS/network → operation/security.
5. Với code, SQL, scheduling, page replacement, subnetting, transaction, PERT/CPM và security scenario: làm trực tiếp trong `Procedural Workbook`, không chỉ đọc lý thuyết.
6. Dùng `High-Risk Confusion Atlas` để phân biệt các cặp concept gần nhau và `Advanced Scenario Labs` để luyện root cause/layer/scope.
7. Dùng `Korean Term Bridge` nếu đã hiểu concept nhưng chưa nhận ra wording tiếng Hàn trong câu hỏi.
8. Dùng `Edge-Case Coverage Supplement` để bù các chi tiết nhỏ có độ salience thấp và `Active Recall Bank 250` để kiểm breadth mà không dựa vào multiple-choice recognition.
9. Dùng `Coverage Audit & Closed-Book Recall` để kiểm đủ `Explain + Distinguish + Solve` cho 21 chapter.
10. Làm Full Mock #1 100 câu; sau đó dùng `Error Remediation Map` cho mọi lỗi trước khi làm đề mới.
11. Chỉ sau khi lỗi cũ đạt `Explain → Distinguish → Reproduce → Transfer` mới làm `Full Mock #2 — Hard Mode 100`.
12. Mở `01-tai-lieu-hoc-day-du.md` hoặc lesson tương ứng của từng môn chỉ khi cần đào sâu một vùng cụ thể.

Theo Q-Net, 필기 gồm 5 môn, mỗi môn 20 câu trắc nghiệm 4 lựa chọn và 30 phút. Điều kiện đỗ là **mỗi môn từ 40 điểm trở lên và trung bình toàn bộ từ 60 điểm trở lên**. Năm 2026 có bộ 출제기준 riêng áp dụng `2026.1.1 ~ 2026.12.31`; vì vậy khi dùng tài liệu cũ phải kiểm tra lại phạm vi thay vì giả định mọi outline cũ đều là source of truth.

## Các môn

- [Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)](01-software-design/README.md)
- [Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)](02-software-development/README.md)
- [Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)](03-database-construction/README.md)
- [Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)](04-programming-language/README.md)
- [Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)](05-information-system-management/README.md)

## Deep-Dive 2026 đã bổ sung

- **Môn 1:** requirements, UML, UI, architecture, cohesion/coupling, OOP/SOLID, GoF patterns, interface/EAI.
- **Môn 2:** data structures, graph/tree, sorting/search/hash, packaging/SCM/DRM, testing/coverage, interface implementation.
- **Môn 3:** keys/relational algebra, dependency/normalization, physical DB/index, SQL, ACID/isolation/locking/recovery, migration.
- **Môn 4:** server implementation, C/Java/Python tracing, OS scheduling/memory/page replacement, OSI/TCP-IP/subnet/routing.
- **Môn 5:** methodology/estimation/PERT, infrastructure/network/HW/DB/cloud, RAID/DR/RTO/RPO, secure coding và system security.
- **Mixed Exam Drills:** 40 câu tự viết, chia đều 8 câu/môn.
- **Cross-Subject Connection Map:** nối các khái niệm giữa 5 môn bằng end-to-end system scenarios.
- **Procedural Workbook:** 35 drill có trace/lời giải cho các dạng phải tự tính hoặc tự trace.
- **Full Mock #1:** 100 câu tự viết, đúng 20 câu/môn, có rationale và error audit.
- **Coverage Audit & Closed-Book Recall:** audit 21 chapter theo `Explain + Distinguish + Solve`.
- **High-Risk Confusion Atlas:** hơn 50 cặp/nhóm dễ nhầm, giải ranh giới bằng mechanism và wording.
- **Advanced Scenario Labs:** 25 lab theo môn + 3 mega-lab liên môn.
- **Korean Term Bridge:** `Korean → English → nghĩa Việt → mechanism` + wording patterns trong đề.
- **Error Remediation Map:** chuyển câu sai thành đường sửa cụ thể theo error taxonomy.
- **Edge-Case Coverage Supplement:** 120 điểm nhỏ dễ bị bỏ sót nhưng vẫn nằm trong phạm vi 21 chapter.
- **Full Mock #2 — Hard Mode:** 100 câu mới, dùng distractor gần nhau và scenario nhiều layer hơn.
- **Active Recall Bank 250:** 50 câu/môn, không có lựa chọn, có answer cues và spaced-recall flow.

## Coverage chính dùng để audit

Master guide tổ chức phạm vi thành 21 chương lớn:

- **Môn 1:** 요구사항 확인 → 화면 설계 → 애플리케이션 설계 → 인터페이스 설계.
- **Môn 2:** 데이터 입출력 구현 → 통합 구현 → 제품 소프트웨어 패키징 → 애플리케이션 테스트 관리 → 인터페이스 구현.
- **Môn 3:** 논리 데이터베이스 설계 → 물리 데이터베이스 설계 → SQL 활용 → SQL 응용 → 데이터 전환.
- **Môn 4:** 서버 프로그램 구현 → 프로그래밍 언어 활용 → 응용 SW 기초 기술 활용. Trong deep-dive, `응용 SW 기초 기술 활용` được tách rõ thành OS và network để tránh học sót.
- **Môn 5:** 소프트웨어 개발 방법론 활용 → IT 프로젝트 정보시스템 구축관리 → 소프트웨어 개발 보안 구축 → 시스템 보안 구축. Trong deep-dive, `IT 프로젝트 정보시스템 구축관리` được tách tiếp thành network/SW/HW/DB/infrastructure management.

Các lesson hiện có có nhiều chủ đề lặp lại từ các nguồn khác nhau. Sự lặp lại này được giữ như material tham khảo, nhưng **không dùng số lượng lesson làm thước đo coverage**.

## Phạm vi nguồn đã rà soát

- `raw/`: PDF, DOCX và bản tóm tắt gốc.
- `raw/notion/`: nội dung Notion theo môn.
- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.
- Các file `final/Subject_*.md` cũ có đoạn ghép nhầm môn. Output đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.

## Nguồn ngoài dùng để kiểm chứng 2026

Source of truth cho cấu trúc thi, tiêu chuẩn đỗ và 출제기준 là **Q-Net / 한국산업인력공단**. Q-Net hiện tách riêng bộ 출제기준 áp dụng `2026.1.1 ~ 2026.12.31`. Các ví dụ, scenarios, drills, recall prompts và mock questions trong bộ 2026 được viết mới để luyện cơ chế, không sao chép nguyên văn ngân hàng câu hỏi 기출.
