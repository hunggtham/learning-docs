# 정보처리기사 — kiểm toán phạm vi học tập

> **Mạch đọc:** Đọc audit này sau [README](./README.md). `README.md` định vị domain; learning output chuẩn hóa nằm trong [`output/`](./output/README.md). Audit này trả lời: **phần thi viết (필기) đã phủ đủ để giải thích–phân biệt–giải bài hay chưa, đâu là dữ kiện phải kiểm lại theo năm, và khi nào cần bàn giao sang Computer Science/Backend/SQL để hiểu sâu hơn?**

**Ngày rà soát:** 2026-09-29. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## 1. Phạm vi và nguồn chuẩn

Domain hiện tập trung vào **kỳ thi viết (필기 / written exam)** của 정보처리기사. Learning spine 2026 được tổ chức quanh 5 môn, master guide, deep-dive track, procedural workbook, confusion atlas, scenario labs, active recall và full mock.

```text
필기
├── 1. 소프트웨어 설계
├── 2. 소프트웨어 개발
├── 3. 데이터베이스 구축
├── 4. 프로그래밍 언어 활용
└── 5. 정보시스템 구축 관리
```

Nguồn chuẩn cho phạm vi thi, tiêu chuẩn đỗ và **tiêu chuẩn ra đề (출제기준 / exam criteria)** là Q-Net / 한국산업인력공단. Nội dung exam-specific có thể thay đổi theo năm, vì vậy phải kiểm nguồn chính thức trước khi sửa các fact về cấu trúc kỳ thi hoặc phạm vi môn.

`raw/` và `raw_md/` là material nguồn/chuyển đổi. `output/` mới là learning output chuẩn hóa. [`output/COVERAGE_MATRIX.md`](./output/COVERAGE_MATRIX.md) theo dõi độ phủ chi tiết; [`output/RESEARCH_REGISTER.md`](./output/RESEARCH_REGISTER.md) giữ provenance cho các nguồn đã xác minh.

## 2. Coverage hiện đã mạnh

Phần 필기 hiện có coverage mạnh ở cả 5 môn, procedural reasoning như SQL/code trace/scheduling/page replacement/subnetting/transaction/PERT-CPM, confusion pairs, scenario transfer, Korean terminology bridge, active recall, remediation và full mock.

Tuy nhiên, completion không nên đo bằng số file hoặc số câu. Một concept chỉ thật sự “được phủ” khi người học làm được ba việc:

```text
Giải thích (Explain)
→ Phân biệt (Distinguish)
→ Giải bài / áp dụng (Solve)
```

Ví dụ, biết định nghĩa deadlock nhưng không phân biệt được deadlock với starvation hoặc không giải được wait-for/resource-allocation scenario thì coverage vẫn chưa hoàn chỉnh.

## 3. Ranh giới với canonical knowledge libraries

Tài liệu chứng chỉ tối ưu cho phạm vi thi, wording và distractor. Nó không thay thế knowledge library chuẩn gốc.

Khi câu hỏi cần hiểu sâu transaction, OS, network, software architecture, security hoặc algorithm ngoài mức exam, phải bàn giao sang [`computer_science/`](../computer_science/README.md), [`10_backend/`](../10_backend/README.md) hoặc [`sql/`](../sql/README.md). Cách này giúp người học vừa thi được vừa không mắc kẹt ở mức nhận diện đáp án.

## 4. Khoảng trống ưu tiên

### P1 — Phần thực hành (실기 / practical exam) là scope riêng

`실기` chưa được coi là completed scope. Nếu mở rộng, cần learning spine, source map, practice model và audit riêng; không trộn thêm vài file vào 필기 rồi gọi là đã phủ 실기.

### P1 — Trôi phạm vi theo năm

Mỗi năm cần kiểm tra `출제기준`, ngày hiệu lực và thay đổi subject/chapter. Nếu một fact đổi, phải xác định chapter, mock, recall bank và confusion note nào bị ảnh hưởng thay vì chỉ sửa một dòng trong master guide.

### P1 — Remediation dựa trên lỗi thật

Coverage rộng chưa nói được người học yếu ở đâu. Khi có mock/recall evidence, nên phân lỗi thành:

```text
knowledge gap
→ distinction gap
→ procedural gap
→ Korean wording gap
```

Bốn loại lỗi cần cách sửa khác nhau. Học lại cả chapter khi lỗi chỉ do wording Hàn thường kém hiệu quả.

### P1 — Provenance của material sinh tự động/OCR

Generated/OCR/merged material chỉ được promote khi mapping rõ về subject/chapter và source. Một file dài hơn không tự làm tài liệu đáng tin hơn.

### P2 — Handoff sau kỳ thi

Các concept có giá trị lâu dài nên link sang canonical owner để người học tiếp tục từ “nhớ để thi” sang “hiểu để dùng”. Đây là bước nối chứng chỉ với knowledge library chung của repository.

## 5. Quy trình review

Khi cập nhật lớn:

1. kiểm Q-Net/출제기준 và ghi ngày;
2. cập nhật `COVERAGE_MATRIX.md` nếu coverage thay đổi;
3. không dùng số file/số câu làm completion criterion;
4. với câu sai, phân loại lỗi theo knowledge/distinction/procedural/Korean-wording;
5. kiểm internal links giữa master guide, deep dive, workbook, recall và remediation;
6. giữ ranh giới 필기/실기 rõ ràng;
7. với nội dung cần hiểu sâu hơn mức thi, thêm handoff sang canonical owner.

## 6. Kết luận và bàn giao

Coverage 필기 hiện **mạnh**; gap lớn nhất là governance theo năm, remediation dựa trên evidence và việc tách riêng 실기 nếu mở rộng sau này.

Nếu đang ôn thi, bắt đầu tại [root README](./README.md) rồi vào [output learning map](./output/README.md). Khi một concept khó vì chưa hiểu cơ chế, dùng internal link sang Computer Science/Backend/SQL rồi quay lại practice thay vì cố học thuộc wording.