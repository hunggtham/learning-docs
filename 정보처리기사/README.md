# 정보처리기사 — Root Entrypoint

`정보처리기사/` là canonical root cho bộ tài liệu học chứng chỉ **정보처리기사**. Learning output hiện được tổ chức tại [output/README.md](./output/README.md); root README này tạo entrypoint nhất quán với các domain khác và giữ ranh giới rõ giữa source material với tài liệu học đã chuẩn hóa.

## Mạch đọc ưu tiên

Nếu mục tiêu là **필기**, bắt đầu tại [Bộ tài liệu học — output](./output/README.md). Từ đó đi theo Master Guide 2026, Deep-Dive Track, procedural workbook, confusion atlas, recall bank và full mock thay vì đọc tuần tự toàn bộ source cũ.

Năm môn chính được giữ theo cấu trúc đề:

```text
소프트웨어 설계
→ 소프트웨어 개발
→ 데이터베이스 구축
→ 프로그래밍 언어 활용
→ 정보시스템 구축 관리
```

Các topic nền như algorithms, operating systems, networking, databases, security và software engineering có canonical owner trong [Computer Science](../computer_science/README.md). Bộ 정보처리기사 dùng chúng theo **exam scope, Korean terminology và question pattern**, không thay thế library Computer Science.

## Coverage và ranh giới source/output

Trạng thái coverage của 5 môn, tiêu chí `Explain → Distinguish → Solve`, gap `실기` và protocol rà soát theo Q-Net nằm tại [COVERAGE_AUDIT.md](./COVERAGE_AUDIT.md). Ma trận chi tiết vẫn nằm ở [output/COVERAGE_MATRIX.md](./output/COVERAGE_MATRIX.md) và provenance nguồn ở [output/RESEARCH_REGISTER.md](./output/RESEARCH_REGISTER.md).

Các file nguồn/PDF/OCR/capture có thể được giữ để provenance và tra cứu, nhưng learning path chính phải đi qua `output/`. Không dùng số lượng lesson hoặc raw document làm bằng chứng rằng một môn đã đủ coverage; tiêu chí là người học có thể `Explain → Distinguish → Solve` và xử lý scenario/edge case trong phạm vi thi.

Các thông tin có thể thay đổi theo năm như 출제기준, cấu trúc thi, lịch thi hoặc quy định Q-Net phải được kiểm lại theo nguồn chính thức trước kỳ thi. Static docs nên ghi rõ baseline thay vì giả định một outline cũ luôn còn hiệu lực.

## Kết nối với các library khác

- [Computer Science](../computer_science/README.md) — cơ chế nền của OS, network, DB, algorithms, security và software systems.
- [Backend](../10_backend/README.md) — request lifecycle, auth, persistence và production application boundaries.
- [SQLD / SQL](../sql/README.md) — SQL/data modeling practice riêng.
- [DevOps / Platform Engineering](../devops_platform_engineering/README.md) — runtime, delivery, observability, incident và infrastructure reasoning.

> **Bàn giao:** Đi tiếp tới [output/README.md](./output/README.md). Nếu một exam concept vẫn chỉ được nhớ bằng definition, quay về canonical owner tương ứng để hiểu mechanism trước khi tiếp tục drill câu hỏi. Dùng [coverage audit](./COVERAGE_AUDIT.md) để quyết định gap nào cần ưu tiên.