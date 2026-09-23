# 정보처리기사 — Bộ tài liệu học

Tài liệu được chia thành 5 môn. Mỗi folder có một bài học đầy đủ và mục lục học tập; nguồn gốc được bảo toàn trong `raw` và `raw_md`.

## Phạm vi học

- Output này tập trung vào **정보처리기사 필기** và giữ ranh giới 5 môn theo cấu trúc đề thi.
- Nội dung **실기 (정보처리 실무)** chưa được xem là phạm vi hoàn tất của bộ output này; không dùng bộ 필기 này thay cho lộ trình 실기 riêng.
- Bản source hiện đối chiếu theo 출제기준 Q-Net giai đoạn **2023.1.1–2025.12.31**; đây không phải cam kết cho kỳ thi 2026. Trước khi thi, hãy kiểm tra bản mới nhất trên [Q-Net](https://www.q-net.or.kr/cst006.do?artlSeq=5210765&brdId=Q006&code=1202&gId=&gSite=Q&id=cst00602).

- [Coverage matrix / ma trận độ phủ](COVERAGE_MATRIX.md) ghi số lesson, source canonical và trạng thái rà soát của từng môn.

- [Research register / sổ nguồn nghiên cứu](RESEARCH_REGISTER.md) ghi nguồn Q-Net và tài liệu kỹ thuật dùng để fact-check.

- [Exam pattern register / pattern đề thi](EXAM_PATTERN_REGISTER.md) ghi dạng câu hỏi đã nghiên cứu và link tới bộ luyện tập biến thể nguyên bản.

## Các môn

- [Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)](01-software-design/README.md)
- [Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)](02-software-development/README.md)
- [Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)](03-database-construction/README.md)
- [Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)](04-programming-language/README.md)
- [Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)](05-information-system-management/README.md)

## Phạm vi nguồn đã rà soát

- `raw/`: PDF, DOCX và bản tóm tắt gốc.
- `raw/notion/`: nội dung Notion theo môn.
- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.
- Các file `final/Subject_*.md` cũ có đoạn ghép nhầm môn. Output đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.
