# 정보처리기사 — Coverage Audit

> **Mạch đọc:** [README](./README.md) là entrypoint cấp domain; learning output chuẩn hóa nằm trong [`output/`](./output/README.md). Audit này dùng để kiểm tra độ phủ kỳ thi và ranh giới giữa certification material với canonical Computer Science/Backend/SQL content.

Cập nhật: **2026-09-29**. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## Phạm vi và nguồn chuẩn

Domain hiện tập trung vào **정보처리기사 필기**. Learning spine 2026 được tổ chức quanh 5 môn, master guide, deep-dive track, procedural workbook, confusion atlas, scenario labs, active recall và full mocks.

```text
필기
├── 1. 소프트웨어 설계
├── 2. 소프트웨어 개발
├── 3. 데이터베이스 구축
├── 4. 프로그래밍 언어 활용
└── 5. 정보시스템 구축 관리
```

Nguồn chuẩn cho cấu trúc thi, tiêu chuẩn đỗ và 출제기준 là **Q-Net / 한국산업인력공단**. Nội dung exam-specific có thời hạn; khi năm/phạm vi thi thay đổi phải kiểm tra lại nguồn chính thức trước khi sửa material.

`raw/` và `raw_md/` là material nguồn/chuyển đổi. `output/` mới là learning output chuẩn hóa. [`output/COVERAGE_MATRIX.md`](./output/COVERAGE_MATRIX.md) giữ ma trận độ phủ chi tiết và [`output/RESEARCH_REGISTER.md`](./output/RESEARCH_REGISTER.md) giữ provenance nguồn khi file này tồn tại trong learning output.

## Trạng thái coverage

| Vùng | Coverage hiện có | Trạng thái |
|---|---|---|
| 2026 written-exam map | master guide + 21 chapter coverage | Strong |
| 5 môn 필기 | deep-dive theo subject | Strong |
| Procedural reasoning | SQL, code trace, scheduling, page replacement, subnetting, transaction, PERT/CPM | Strong |
| Confusion handling | high-risk concept pairs / distractor boundaries | Strong |
| Scenario transfer | subject labs + cross-subject mega-labs | Strong |
| Korean terminology bridge | Korean → English → Vietnamese → mechanism | Strong |
| Recall / remediation | active recall + error remediation | Strong |
| Full-exam practice | 2 mock sets 100 questions | Strong |
| 실기 | chưa phải completed scope | Gap / out of current scope |

## Bất biến cần giữ

Mục tiêu không phải tăng số lesson mà phải giữ đủ ba năng lực:

```text
Explain → Distinguish → Solve
```

Một concept chỉ được coi là covered khi người học có thể giải thích cơ chế, phân biệt với concept gần và xử lý scenario/procedure tương ứng. Các file trùng nguồn hoặc OCR không làm coverage tăng nếu không bổ sung năng lực này.

Certification material cũng không thay canonical knowledge library. Khi cần hiểu sâu transaction, OS, network, software architecture, security hoặc algorithms ngoài phạm vi thi, phải handoff về `computer_science/`, `10_backend/`, `sql/` hoặc domain owner tương ứng.

## Gaps còn lại

1. **실기:** chưa được xem là completed scope; nếu mở rộng phải có learning spine và audit riêng thay vì pha vào 필기.
2. **Annual exam drift:** mỗi năm phải đối chiếu 출제기준 mới, ghi ngày kiểm tra và xác định chapter nào thay đổi.
3. **Weak-area evidence:** coverage rộng không đủ; các vùng có error rate cao cần remediation dựa trên mock/recall evidence.
4. **Source provenance:** generated/OCR/merged material chỉ được promoted khi mapping về subject/chapter và source rõ.
5. **Cross-domain transfer:** sau khi thi, nên handoff các concept quan trọng sang canonical Computer Science/Backend/SQL routes để kiến thức không dừng ở exam recognition.

## Review protocol

Mỗi lần cập nhật lớn:

1. kiểm tra Q-Net/출제기준 và ghi ngày;
2. cập nhật `COVERAGE_MATRIX.md` nếu subject/chapter coverage thay đổi;
3. không dùng số file hoặc số câu làm completion criterion;
4. với câu sai, phân loại lỗi thành knowledge gap, distinction gap, procedural gap hoặc Korean-wording gap;
5. kiểm tra internal links giữa master guide, deep-dive, workbook, recall và remediation;
6. giữ ranh giới `필기` / `실기` rõ ràng.

> **Bàn giao:** Nếu đang chuẩn bị thi, bắt đầu tại [root README](./README.md) rồi đi vào [output learning map](./output/README.md). Audit này chỉ quyết định coverage/gap; nó không thay thế tài liệu học.