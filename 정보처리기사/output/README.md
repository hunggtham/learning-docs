# 정보처리기사 — Bộ tài liệu học

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **정보처리기사 — Bộ tài liệu học**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Các môn** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Phạm vi nguồn đã rà soát** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này dùng README làm bản đồ owner của Information Processing Engineer, rồi nối các môn, phạm vi và bài học theo dependency.

Tài liệu được chia thành 5 môn. Mỗi folder có một bài học đầy đủ và mục lục học tập; nguồn gốc được bảo toàn trong `raw` và `raw_md`. Mọi lesson và full guide đều được dựng với mạch mở đầu → giải thích → bàn giao → kết thúc; kiểm tra lại bằng `scripts/audit_learning_output.py`.

## Các môn

Phần này là mục lục định hướng: chọn môn theo thứ tự học, rồi đi vào lesson để theo dõi mạch giải thích và phần bàn giao.

- [Môn 1 — 소프트웨어 설계 (Software Design) (Thiết kế phần mềm)](01-software-design/README.md)
- [Môn 2 — 소프트웨어 개발 (Software Development) (Phát triển phần mềm)](02-software-development/README.md)
- [Môn 3 — 데이터베이스 구축 (Database Construction) (Xây dựng cơ sở dữ liệu)](03-database-construction/README.md)
- [Môn 4 — 프로그래밍 언어 활용 (Programming Language Application) (Ứng dụng ngôn ngữ lập trình)](04-programming-language/README.md)
- [Môn 5 — 정보시스템 구축 관리 (Information System Construction Management) (Quản lý xây dựng hệ thống thông tin)](05-information-system-management/README.md)

> **Chuyển mạch:** Trong **정보처리기사 — Bộ tài liệu học**, **Các môn** nêu điều cần giải thích; **Phạm vi nguồn đã rà soát** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Phạm vi nguồn đã rà soát

Phần này nêu nguồn và giới hạn biên soạn, giúp người học biết nội dung nào là tài liệu học đã chuẩn hóa trước khi tra cứu nguồn thô.

- `raw/`: PDF, DOCX và bản tóm tắt gốc.
- `raw/notion/`: nội dung Notion theo môn.
- `raw_md/generated_markdown*`, `final`, `final_extended`, `merged_subjects`: các lần OCR/dịch/tổng hợp trước.
- Các file `final/Subject_*.md` cũ có đoạn ghép nhầm môn. Output đã lọc lại theo ranh giới môn trong `raw/notion/` (Môn 1: 0–72; Môn 2: 73–162; Môn 3: 163–231; Môn 4: 232–314; Môn 5: 315–376), đồng thời giữ các phần mở rộng cùng chủ đề.

> **Bàn giao:** Sau **Phạm vi nguồn đã rà soát**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
