# BOOK MD → LEARNING DOCS PROMPT

Dùng prompt này cùng với [`prompt/COMMON_PROMPT.md`](./COMMON_PROMPT.md) khi chuyển một sách, PDF đã OCR, raw Markdown, transcript hoặc giáo trình thành learning docs trong repository.

`COMMON_PROMPT.md` quyết định chất lượng giải thích, continuity, terminology, canonical ownership và source fidelity ở mức chung. File này quyết định pipeline cụ thể để không biến một source-book conversion thành summary hoặc một tài liệu “cùng chủ đề nhưng thiếu kiến thức nguồn”.

## Mục tiêu

Đầu ra phải là một **self-contained learning edition**:

> Dễ hiểu hơn SOURCE nhưng không nghèo kiến thức hơn SOURCE.

Người học có thể đọc learning docs để hiểu toàn bộ knowledge-bearing content quan trọng của SOURCE mà không phải quay lại raw source chỉ để bù definition, distinction, classification, condition, exception, formula, table, figure, procedure, market/legal rule hoặc concept bị bỏ sót.

Ưu tiên:

```text
Semantic completeness > brevity
Understanding > transcription
Explanation > summarization
Source fidelity + pedagogy > stylistic rewrite
```

Không được coi “viết lại hay hơn”, “dài hơn” hoặc “có nhiều ví dụ hơn” là bằng chứng rằng conversion đã hoàn thành.

---

## 1. Input contract

Trước khi viết:

1. Đọc `prompt/COMMON_PROMPT.md`.
2. Đọc README của repository và README/domain owner liên quan.
3. Đọc canonical files và internal links có thể trùng phạm vi.
4. Xác định SOURCE chính xác: file nào, edition/version nào, phạm vi chapter/page nào.
5. Đọc đủ SOURCE trước khi chốt architecture của lesson.

Nếu SOURCE chưa tồn tại hoặc không đọc được đầy đủ, không tự suy diễn nội dung sách từ tên/chủ đề. Báo rõ missing source và chỉ làm phần có bằng chứng.

Raw Markdown là **content authority** cho những gì source thực sự chứa. Canonical docs hiện có là authority cho ownership/structure trong repository.

---

## 2. Không generate final lesson trực tiếp từ chunk

Có thể đọc SOURCE theo chunk để xử lý context lớn, nhưng không được dùng pipeline:

```text
chunk 1 → final lesson 1
chunk 2 → final lesson 2
chunk 3 → final lesson 3
```

vì cách này dễ mất:

- định nghĩa được hoàn thiện ở trang sau;
- condition/exception nằm xa rule;
- bảng bị chia qua page boundary;
- concept lặp lại với meaning khác;
- prerequisite xuất hiện sau phần phụ thuộc;
- relationship giữa nhiều chapter.

Pipeline bắt buộc:

```text
SOURCE
→ normalize
→ semantic inventory
→ dependency / concept map
→ coverage map
→ lesson architecture
→ authoring
→ coverage audit
→ reconstruction test
→ learner replacement test
```

---

## 3. Source normalization

Trước semantic inventory, phân biệt content thật với noise:

- page number;
- header/footer lặp;
- OCR artifact;
- broken line;
- duplicated paragraph;
- table bị vỡ;
- image caption;
- footnote;
- answer key;
- metadata xuất bản.

Không silently sửa phần có thể làm đổi meaning. Nếu OCR/source không đủ rõ để khẳng định, đánh dấu:

`SOURCE_AMBIGUITY`

và đối chiếu PDF/image gốc nếu có.

---

## 4. Semantic inventory bắt buộc

Trước khi viết lesson, lập inventory của mọi **knowledge-bearing semantic unit**.

Mỗi unit nên có ID ổn định, ví dụ:

`B2-C03-S02-U004`

Ít nhất ghi:

- Source ID;
- source location;
- source heading;
- semantic type;
- concept/topic;
- short meaning;
- dependency;
- condition/exception nếu có;
- time sensitivity;
- proposed target lesson/section;
- status.

Semantic type dùng khi phù hợp:

- `CONCEPT`
- `DEFINITION`
- `DISTINCTION`
- `CLASSIFICATION`
- `RELATIONSHIP`
- `MECHANISM`
- `PROCESS`
- `CAUSE_EFFECT`
- `CONDITION`
- `EXCEPTION`
- `REQUIREMENT`
- `THRESHOLD`
- `FORMULA`
- `VARIABLE`
- `TABLE`
- `FIGURE`
- `EXAMPLE`
- `CASE`
- `WARNING`
- `LEGAL_RULE`
- `MARKET_RULE`
- `TAX_RULE`
- `INSTITUTION`
- `TERMINOLOGY`
- `EXERCISE`

Heading hoặc page không phải semantic unit. Một paragraph có thể chứa nhiều unit.

---

## 5. Coverage map

Mỗi source unit phải có destination rõ ràng.

Coverage status tối thiểu:

- `FULL`
- `PARTIAL`
- `MISSING`
- `N/A_NON_LEARNING_CONTENT`
- `SOURCE_AMBIGUITY`

Không đánh `FULL` chỉ vì keyword xuất hiện.

`FULL` chỉ khi người học có thể hiểu unit đó từ learning docs với depth cần thiết: bản chất, relationship/mechanism, condition/boundary và distinction quan trọng.

Với source conversion đủ lớn, tạo hoặc update `SOURCE_COVERAGE.md` hoặc coverage artifact tương đương gần module đó.

Schema khuyến nghị:

| Source ID | Source location | Semantic unit | Type | Target lesson/section | Status | Notes/action |
|---|---|---|---|---|---|---|

Acceptance target:

```text
PARTIAL = 0
MISSING = 0
```

trừ ambiguity được document rõ.

---

## 6. Thiết kế lesson architecture

Không cần giữ page/chapter order 1:1 nếu order nguồn không tối ưu cho learning.

Được phép:

- split;
- merge;
- reorder;
- rename;
- tạo prerequisite bridge;
- chuyển phần trùng sang canonical owner;
- tạo cross-link.

Nhưng mọi semantic unit phải trace được tới destination.

Architecture ưu tiên:

1. prerequisite;
2. mental model;
3. core concepts;
4. mechanisms/relationships;
5. conditions/exceptions;
6. applied examples;
7. synthesis/review.

Nếu source topic đã có canonical owner trong repository, không duplicate hàng loạt. Giữ phần source-specific cần thiết, giải thích đủ để không làm đứt mạch, rồi cross-link tới canonical owner cho depth mở rộng.

---

## 7. Authoring contract cho mỗi concept

Mỗi concept quan trọng phải đạt tối thiểu ba layer:

### Layer 1 — What

- Nó là gì?
- Thuật ngữ gốc là gì?
- Nó khác concept gần nhất ở đâu?

### Layer 2 — Why / Mechanism

- Nó tồn tại để giải quyết vấn đề gì?
- Hệ thống vận hành ra sao?
- Participants/components liên hệ thế nào?
- Nguyên nhân → cơ chế → hệ quả là gì?

### Layer 3 — Application / Boundary

- Dùng/quan sát concept ở đâu?
- Điều kiện áp dụng là gì?
- Ngoại lệ/rủi ro/boundary là gì?
- Người học dễ nhầm với gì?

Với concept hệ thống hoặc khó, thêm:

### Layer 4 — System view

- Nó nằm ở đâu trong broader system?
- Input/output của nó là gì?
- Concept trước/sau phụ thuộc nó thế nào?

Không bắt buộc dùng các heading Layer trong output; đây là semantic contract.

---

## 8. Ngôn ngữ và thuật ngữ

Tuân theo convention của domain hiện tại.

Nếu source là tiếng Hàn và learning docs viết bằng tiếng Việt:

- giải thích chính bằng tiếng Việt;
- giữ thuật ngữ Hàn quan trọng ngay tại lần xuất hiện hữu ích;
- thêm English term khi nó là thuật ngữ quốc tế/tra cứu quan trọng;
- không dịch mất distinction pháp lý/thị trường của tiếng Hàn.

Pattern khi hữu ích:

`Thuật ngữ Việt (English / 한국어)`

Không cần gắn ba ngôn ngữ cho mọi noun thông thường.

---

## 9. Table, figure, formula không được drop

Nếu SOURCE dùng table/figure/formula để mang kiến thức, conversion phải bảo toàn semantic meaning.

Có thể reconstruct bằng:

- Markdown table;
- Mermaid;
- ASCII flow;
- formula block;
- prose có cấu trúc.

### Với table

Phải giữ các row/column/condition quyết định distinction. Có prose dẫn cách đọc và prose chốt insight.

### Với figure/diagram

Phải mô tả nodes, direction, relationship và conclusion. Không chỉ ghi “hình minh họa”.

### Với formula

Giữ:

- formula;
- variables;
- units nếu có;
- assumptions;
- intuition;
- interpretation;
- worked example nếu cần.

---

## 10. Source example và editorial example

Phân biệt:

- **Source example:** ví dụ/case thuộc knowledge structure của sách.
- **Editorial example:** ví dụ mới được thêm để dễ hiểu.

Không được để editorial example thay thế source rule hoặc khiến người đọc tưởng đó là dữ kiện trong source.

Ví dụ mới phải phục vụ một concept cụ thể, không scope-drift sang chủ đề khác.

---

## 11. Time-sensitive knowledge

Đặc biệt áp dụng với:

- law;
- tax;
- regulation;
- market rule;
- institution;
- trading hours;
- listing requirement;
- threshold;
- product rule;
- policy;
- current statistics.

Không âm thầm overwrite textbook/source state bằng trạng thái hiện tại.

Nếu cần current update, tách:

```text
Source / textbook state
→ source đang dạy gì

Current verified state
→ hiện tại khác gì

Why it matters
→ thay đổi này ảnh hưởng cách hiểu/áp dụng ra sao
```

Current state phải có snapshot/date và ưu tiên official source.

---

## 12. Exercises và source-question test

Tất cả review question/exercise có knowledge value phải được inventory/mapping.

Không nhất thiết copy nguyên wording câu hỏi.

Nhưng với mỗi question phải kiểm tra:

> Nếu chỉ đọc learning docs, người học có đủ knowledge + reasoning để tự giải câu hỏi nguồn không?

Nếu không, relevant semantic unit vẫn là `PARTIAL` hoặc `MISSING`.

Cuối lesson/chapter có thể thêm knowledge checks theo các dạng:

- explain why;
- compare/distinguish;
- trace a process;
- apply a rule;
- identify an exception;
- interpret a table/formula;
- reconstruct a system flow.

Không chỉ dùng câu hỏi recall từ vựng.

---

## 13. Chống scope drift

Một book conversion không phải lý do để viết encyclopedia toàn domain.

Enrichment chỉ giữ khi:

1. giúp hiểu một source unit;
2. giải prerequisite thật sự cần thiết;
3. cập nhật current state cần thiết;
4. hoặc cross-link tới canonical owner phù hợp.

Nếu một chủ đề hay nhưng không cần cho source, không mở rộng chỉ vì agent biết nó.

---

## 14. Audit sau khi viết

Chạy cả hai chiều.

### SOURCE → output

Mỗi knowledge-bearing unit phải là:

- `FULL`, hoặc
- documented `SOURCE_AMBIGUITY`.

Không để `PARTIAL/MISSING` rồi vẫn tuyên bố complete.

### Output → SOURCE

Rà:

- scope drift;
- duplicate canonical content;
- editorial claims không có căn cứ;
- terminology inconsistency;
- invented relationship;
- current state thiếu verification;
- prose dài nhưng không tăng understanding.

---

## 15. Reconstruction test

Giả sử raw SOURCE biến mất.

Từ learning docs, thử dựng lại:

- chapter knowledge graph;
- major concepts;
- classifications;
- distinctions;
- procedures;
- system flows;
- formulas;
- conditions;
- exceptions;
- important tables/figures;
- institutional/legal/market relationships;
- knowledge required by source questions.

Nếu không reconstruct được một phần quan trọng, conversion chưa hoàn tất.

---

## 16. Learner replacement test

Đặt câu hỏi:

> Người học còn phải mở SOURCE vì learning docs thiếu một concept, condition, exception, distinction, table, formula hoặc rule quan trọng không?

Nếu có → chưa complete.

Việc quay lại source chỉ để xem wording/layout nguyên bản không tính là failure.

---

## 17. Repository integration

Trước khi tạo file mới:

- kiểm tra canonical owner;
- kiểm tra README;
- kiểm tra naming convention;
- kiểm tra links;
- kiểm tra lesson hiện có;
- tránh file cô lập.

Sau khi viết:

- update README/learning route khi cần;
- thêm internal links hai chiều khi có giá trị;
- chạy link/structure checks hiện có trong repo;
- giữ source/raw riêng với learning edition;
- không sửa raw source chỉ để làm output đẹp hơn, trừ khi nhiệm vụ là sửa OCR và thay đổi đó được trace rõ.

Thay đổi lớn nên thực hiện trên feature branch theo `COMMON_PROMPT.md`.

---

## 18. Output artifacts tối thiểu

Với một conversion lớn, đầu ra nên gồm:

1. learning lesson files;
2. coverage artifact (`SOURCE_COVERAGE.md` hoặc equivalent);
3. source ambiguity artifact nếu thực sự có ambiguity đáng theo dõi;
4. README/learning-route update nếu architecture thay đổi.

Không tạo artifact rỗng chỉ để đủ checklist.

---

## 19. Final report của agent

Khi hoàn thành một vòng conversion, báo cáo ngắn:

1. SOURCE đã đọc;
2. lesson/files đã tạo/sửa;
3. architecture đã chọn và lý do chính;
4. coverage: FULL/PARTIAL/MISSING/AMBIGUITY;
5. source questions đã được cover chưa;
6. current/time-sensitive enrichment nào đã thêm;
7. reconstruction test;
8. learner replacement test;
9. gaps còn lại nếu có.

Không nói “complete” nếu coverage artifact không chứng minh điều đó.

---

# Definition of done

Một source-book conversion chỉ hoàn tất khi:

- semantic inventory đã bao phủ source;
- mỗi knowledge-bearing unit có destination;
- `PARTIAL = 0` và `MISSING = 0` hoặc gap được nói rõ là chưa hoàn thành;
- table/figure/formula có semantic value không bị drop;
- conditions/exceptions/distinctions được bảo toàn;
- terminology nhất quán;
- time-sensitive content phân biệt source state và verified current state;
- source-question test pass;
- reconstruction test pass;
- learner replacement test pass;
- output tích hợp đúng canonical structure của repository.

Nguyên tắc cuối cùng:

> **Learning docs phải dễ hiểu hơn SOURCE nhưng không được biết ít hơn SOURCE.**
