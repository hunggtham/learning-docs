# 정보처리기사 — Bộ tài liệu học

> **Nếu mục tiêu hiện tại là thi lại phần 필기, hãy bắt đầu từ [정보처리기사 필기 2026 — Master Guide học sâu và phủ rộng](00-2026-written-exam-master-guide.md), không bắt đầu bằng cách đọc tuần tự hàng trăm lesson nhỏ.**

Tài liệu được chia thành 5 môn theo cấu trúc 필기 hiện hành. Các tệp (file / 파일) cũ vẫn được giữ để tra cứu sâu theo chủ đề; master guide đóng vai trò **coverage map** để biết phần nào bắt buộc phải học, phần nào đang yếu và phần nào dễ bị nhầm trong đề.

## 2026 필기 — luồng học ưu tiên

1. [**Master Guide 2026 — học sâu + phủ toàn bộ 5 môn**](00-2026-written-exam-master-guide.md)
2. [**Deep-Dive Track 2026 — 5 môn + workbook + scenario + recall + remediation + 2 full mock**](2026-depth/README.md)
3. Học 5 deep-dive để hiểu concept theo cơ chế (mechanism / 메커니즘), không chỉ thuộc definition.
4. Dùng `Cross-Subject Connection Map` để nối yêu cầu (requirement / 요구사항) → thiết kế (design / 설계) → mã (code / 코드) → DB → OS/mạng (network / 네트워크) → thao tác (operation / 연산)/bảo mật (security / 보안).
5. Với mã (code / 코드), SQL, scheduling, page replacement, subnetting, giao dịch (transaction / 트랜잭션), PERT/CPM và bảo mật (security / 보안) scenario: làm trực tiếp trong `Procedural Workbook`, không chỉ đọc lý thuyết.
6. Dùng `High-Risk Confusion Atlas` để phân biệt các cặp concept gần nhau và `Advanced Scenario Labs` để luyện nguyên nhân gốc (root cause / 근본 원인)/tầng (layer / 계층)/phạm vi (scope / 범위).
7. Dùng `Korean Term Bridge` nếu đã hiểu concept nhưng chưa nhận ra wording tiếng Hàn trong câu hỏi.
8. Dùng `Edge-Case Coverage Supplement` để bù các chi tiết nhỏ có độ salience thấp và `Active Recall Bank 250` để kiểm breadth mà không dựa vào multiple-choice recognition.
9. Dùng `Coverage Audit & Closed-Book Recall` để kiểm đủ `Explain + Distinguish + Solve` cho 21 chapter.
10. Làm Full Mock #1 100 câu; sau đó dùng `Error Remediation Map` cho mọi lỗi trước khi làm đề mới.
11. Chỉ sau khi lỗi cũ đạt `Explain → Distinguish → Reproduce → Transfer` mới làm `Full Mock #2 — Hard Mode 100`.
12. Mở `01-tai-lieu-hoc-day-du.md` hoặc lesson tương ứng của từng môn chỉ khi cần đào sâu một vùng cụ thể.

Theo Q-Net, 필기 gồm 5 môn, mỗi môn 20 câu trắc nghiệm 4 lựa chọn và 30 phút. Điều kiện đỗ là **mỗi môn từ 40 điểm trở lên và trung bình toàn bộ từ 60 điểm trở lên**. Năm 2026 có bộ 출제기준 riêng áp dụng `2026.1.1 ~ 2026.12.31`; vì vậy khi dùng tài liệu cũ phải kiểm tra lại phạm vi thay vì giả định mọi outline cũ đều là nguồn chuẩn (source of truth / 정본).

## Phạm vi học

- đầu ra (output / 출력) này tập trung vào **정보처리기사 필기** và giữ ranh giới 5 môn theo cấu trúc đề thi.
- Nội dung **실기 (정보처리 실무)** chưa được xem là phạm vi hoàn tất của bộ đầu ra (output / 출력) này; không dùng bộ 필기 này thay cho lộ trình 실기 riêng.
- Bản nguồn (source / 소스) hiện đối chiếu theo 출제기준 Q-Net giai đoạn **2023.1.1–2025.12.31**; đây không phải cam kết cho kỳ thi 2026. Trước khi thi, hãy kiểm tra bản mới nhất trên [Q-Net](https://www.q-net.or.kr/cst006.do?artlSeq=5210765&brdId=Q006&code=1202&gId=&gSite=Q&id=cst00602).

- [Coverage matrix / ma trận độ phủ](COVERAGE_MATRIX.md) ghi số lesson, nguồn (source / 소스) chuẩn gốc (canonical / 정본) và trạng thái rà soát của từng môn.

- [Research register / sổ nguồn nghiên cứu](RESEARCH_REGISTER.md) ghi nguồn Q-Net và tài liệu kỹ thuật dùng để fact-check.

## Các môn

- [Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)](01-software-design/README.md)
- [Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)](02-software-development/README.md)
- [Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)](03-database-construction/README.md)
- [Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)](04-programming-language/README.md)
- [Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)](05-information-system-management/README.md)

## Deep-Dive 2026 đã bổ sung

- **Môn 1:** requirements, UML, UI, kiến trúc (architecture / 아키텍처), cohesion/coupling, OOP/SOLID, GoF patterns, giao diện (interface / 인터페이스)/EAI.
- **Môn 2:** dữ liệu (data / 데이터) structures, đồ thị (graph / 그래프)/cây (tree / 트리), sorting/tìm kiếm (search / 검색)/băm (hash / 해시), packaging/SCM/DRM, testing/coverage, giao diện (interface / 인터페이스) hiện thực (implementation / 구현).
- **Môn 3:** keys/relational algebra, phụ thuộc (dependency / 의존성)/normalization, vật lý (physical / 물리적) DB/chỉ mục (index / 인덱스), SQL, ACID/isolation/locking/khôi phục (recovery / 복구), di chuyển (migration / 마이그레이션).
- **Môn 4:** máy chủ (server / 서버) hiện thực (implementation / 구현), C/Java/Python tracing, OS scheduling/bộ nhớ (memory / 메모리)/page replacement, OSI/TCP-IP/subnet/routing.
- **Môn 5:** methodology/estimation/PERT, hạ tầng (infrastructure / 인프라)/mạng (network / 네트워크)/HW/DB/cloud, RAID/DR/RTO/RPO, secure coding và hệ thống (system / 시스템) bảo mật (security / 보안).
- **Mixed Exam Drills:** 40 câu tự viết, chia đều 8 câu/môn.
- **Cross-Subject liên kết (connection / 연결) Map:** nối các khái niệm giữa 5 môn bằng end-to-end hệ thống (system / 시스템) scenarios.
- **Procedural Workbook:** 35 drill có dấu vết (trace / 추적)/lời giải cho các dạng phải tự tính hoặc tự dấu vết (trace / 추적).
- **Full Mock #1:** 100 câu tự viết, đúng 20 câu/môn, có rationale và lỗi (error / 오류) kiểm tra (audit / 감사).
- **Coverage kiểm tra (audit / 감사) & Closed-Book Recall:** kiểm tra (audit / 감사) 21 chapter theo `Explain + Distinguish + Solve`.
- **High-Risk Confusion Atlas:** hơn 50 cặp/nhóm dễ nhầm, giải ranh giới bằng cơ chế (mechanism / 메커니즘) và wording.
- **Advanced Scenario Labs:** 25 lab theo môn + 3 mega-lab liên môn.
- **Korean Term cầu nối (bridge / 브리지):** `Korean → English → nghĩa Việt → mechanism` + wording patterns trong đề.
- **lỗi (error / 오류) Remediation Map:** chuyển câu sai thành đường sửa cụ thể theo lỗi (error / 오류) taxonomy.
- **Edge-Case Coverage Supplement:** 120 điểm nhỏ dễ bị bỏ sót nhưng vẫn nằm trong phạm vi 21 chapter.
- **Full Mock #2 — Hard chế độ (mode / 모드):** 100 câu mới, dùng distractor gần nhau và scenario nhiều tầng (layer / 계층) hơn.
- **Active Recall Bank 250:** 50 câu/môn, không có lựa chọn, có answer cues và spaced-recall luồng (flow / 흐름).

## Coverage chính dùng để kiểm tra (audit / 감사)

Master guide tổ chức phạm vi thành 21 chương lớn:

- **Môn 1:** 요구사항 확인 → 화면 설계 → 애플리케이션 설계 → 인터페이스 설계.
- **Môn 2:** 데이터 입출력 구현 → 통합 구현 → 제품 소프트웨어 패키징 → 애플리케이션 테스트 관리 → 인터페이스 구현.
- **Môn 3:** 논리 데이터베이스 설계 → 물리 데이터베이스 설계 → SQL 활용 → SQL 응용 → 데이터 전환.
- **Môn 4:** 서버 프로그램 구현 → 프로그래밍 언어 활용 → 응용 SW 기초 기술 활용. Trong deep-dive, `응용 SW 기초 기술 활용` được tách rõ thành OS và mạng (network / 네트워크) để tránh học sót.
- **Môn 5:** 소프트웨어 개발 방법론 활용 → IT 프로젝트 정보시스템 구축관리 → 소프트웨어 개발 보안 구축 → 시스템 보안 구축. Trong deep-dive, `IT 프로젝트 정보시스템 구축관리` được tách tiếp thành mạng (network / 네트워크)/SW/HW/DB/hạ tầng (infrastructure / 인프라) management.

Các lesson hiện có có nhiều chủ đề lặp lại từ các nguồn khác nhau. Sự lặp lại này được giữ như material tham khảo, nhưng **không dùng số lượng lesson làm thước đo coverage**.

## Phạm vi nguồn đã rà soát

- `raw/`: PDF, DOCX và bản tóm tắt gốc.
- `raw/notion/`: nội dung Notion theo môn.
- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.
- Các tệp (file / 파일) `final/Subject_*.md` cũ có đoạn ghép nhầm môn. đầu ra (output / 출력) đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.

## Nguồn ngoài dùng để kiểm chứng 2026

Nguồn chuẩn (source of truth / 정본) cho cấu trúc thi, tiêu chuẩn đỗ và 출제기준 là **Q-Net / 한국산업인력공단**. Q-Net hiện tách riêng bộ 출제기준 áp dụng `2026.1.1 ~ 2026.12.31`. Các ví dụ, scenarios, drills, recall prompts và mock questions trong bộ 2026 được viết mới để luyện cơ chế, không sao chép nguyên văn ngân hàng câu hỏi 기출.
