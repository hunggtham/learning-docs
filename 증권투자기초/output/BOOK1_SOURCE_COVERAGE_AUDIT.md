# Book 1 — Publication Audit

Authority: `증권투자기초/raw_md/sach1.md`. Khi OCR/text không đủ để xác nhận bảng,
hình, công thức hoặc answer key, ảnh tương ứng trong `증권투자기초/raw/sach1/`
được dùng làm nguồn đối chiếu. Raw source không bị sửa.

## Verdict

**PUBLICATION PASS**

Pass này áp dụng cho source-specific learning route của Sách 1 hiện nằm trên
`main`. Publication audit gốc được thực hiện trên branch
`fix/securities-book1-publication-pass-v2`; việc tích hợp Sách 2/3 sau đó không
thay đổi semantic coverage của Sách 1. Pass xác nhận source fidelity, navigation,
terminology và publication structure theo contract hiện tại; nó không biến các
snapshot pháp lý/thị trường trong textbook thành quy định hiện hành 2026.

## 1. Semantic inventory

Coverage matrix canonical: [SOURCE_COVERAGE.md](./SOURCE_COVERAGE.md).

| Status | Count |
|---|---:|
| FULL | 339 |
| PARTIAL | 0 |
| MISSING | 0 |
| SOURCE_AMBIGUITY | 0 |

Inventory đã được rebuild từ source, không kế thừa trạng thái `FULL` của matrix
55-row cũ. Một row hiện tương ứng một semantic unit độc lập hoặc một source
question.

Các vùng từng bị gộp quá rộng đã được split:

- IPO/listing/capital increase: 25 units;
- order/trading/settlement/venues: 36 units;
- derivatives: 15 units;
- securities tax: 14 units;
- M&A: 14 units;
- fund structure/pricing/redemption: 27 units;
- fund classification: 33 units;
- fund taxation: 3 units;
- source review questions: 91 units.

Các type được audit gồm definition, distinction, classification, process,
institution, legal/market rule, condition, exception, formula, variable, table,
figure, worked example, metric, tax rule và review question.

## 2. Source-question test

**PASS.**

Chapter 1 review questions và Chapter 2 review questions được map thành 91
`REVIEW_QUESTION` units trong coverage matrix. Mỗi row ghi destination lesson và
trạng thái `FULL`.

Các điểm OCR/answer-key dễ sai đã được image-verified:

- Ch1 Q50: `raw/sach1/221.jpg` và answer `231.jpg` xác nhận biến dùng
  `발행가액` và phục hồi denominator của first-issue formula.
- Ch1 Q60–61: `224.jpg` và answer `232.jpg` xác nhận distinction về disclosure
  và proxy.
- Ch2 Q29–30: `351.jpg`–`352.jpg` xác nhận Q29 = ① và Sharpe Q30 = 0.50.

Kết quả: người học không cần quay lại raw source chỉ để học thêm một concept
knowledge-bearing bị thiếu trước khi giải các câu source.

## 3. Table / figure / formula audit

**PASS.**

Các object quan trọng được reconstruct theo cơ chế, không chỉ nhắc tên:

- Hình phân loại financial market và bảng nhóm tổ chức tài chính;
- loss-to-principal/product classification;
- issuance/secondary-market flow;
- authorization/registration và business-unit tables;
- IPO/new-share vs old-share flow, paid/bonus increase và ex-right/issue-price
  formulas với variable/condition;
- trading priority, order type, IOC/FOK, clearing-settlement-depository,
  circuit breaker/Sidecar và venue comparison;
- KOSDAQ/KONEX/K-OTC/NXT rule/condition tables ở trạng thái textbook;
- futures/options/ELW payoff, margin, conversion/parity/gearing relations;
- securities-tax event/base/timing/exception matrix;
- M&A taxonomy, tender offer, large-holding report, treasury stock và proxy;
- NAV/base-price/unit math, fee/TER, subscription/redemption/deferral timing;
- fund classification/structure tables, REIT/special-assets flows;
- risk metrics, beta/benchmark excess và Sharpe worked example.

Mỗi formula/table quan trọng có input hoặc variable, cách đọc, điều kiện áp dụng
và boundary/exception tương ứng trong lesson hoặc coverage artifact.

## 4. Reconstruction test

**PASS.**

Từ learning edition có thể tái dựng các chuỗi chính của source mà không cần học
lại từ raw:

```text
financial system
→ security/right
→ issuance
→ listing
→ order/matching
→ clearing/settlement
→ disclosure/venue
→ derivative/tax/M&A
```

và:

```text
collective investment definition
→ legal form / participants
→ NAV / fees
→ subscription / redemption
→ fund classification
→ suitability / selection / risk
→ taxation
```

Các distinction độc lập như IPO ≠ listing, paid-in ≠ bonus capital increase,
dealer ≠ broker, advisory ≠ discretionary management, securities ≠ derivatives,
fund open/closed ≠ public/private, backward/forward pricing và KRX/KOSDAQ/KONEX/
K-OTC/NXT không bị collapse thành một khái niệm chung.

## 5. Learner replacement test

**PASS.**

Learning route vẫn là tài liệu học đầy đủ, không bị rút thành summary. Mỗi lesson
giữ explanation theo cơ chế, Korean terminology, condition/boundary và
checkpoints; `90-review-and-source-trace.md` dùng cho review/provenance chứ không
thay lesson.

Một người học có thể dùng route 01→13 để hiểu source knowledge, rồi dùng 90 để
ôn/reconstruct mà không cần raw source như tài liệu giảng giải chính.

## 6. Terminology audit

**PASS.**

- `00-korean-reading-guide.md` được giữ làm reading guide chung.
- Mỗi lesson giữ `한국어 핵심어` hoặc terminology cần thiết theo ngữ cảnh.
- Terminology pháp lý/thị trường không bị dịch làm mất distinction.
- Pattern ưu tiên là Vietnamese (English / 한국어) khi ba ngôn ngữ thật sự giúp
  giữ nghĩa; không ép mọi noun thành ba ngôn ngữ.

## 7. Time-sensitive boundary

**PASS về publication boundary; không tuyên bố current-law verification cho các
rule không được kiểm tra chính thức.**

Các nhóm sau vẫn chỉ là **SOURCE / TEXTBOOK STATE** trừ khi lesson có block
`CURRENT VERIFIED STATE` với official source và snapshot date:

- tax rates/bases/exceptions;
- trading hours, price limits, circuit breaker, Sidecar, settlement timing;
- IPO/listing thresholds và ownership-dispersion requirements;
- public/private offering thresholds;
- authorization/registration capital or business-unit requirements;
- KRX/KOSDAQ/KONEX/K-OTC/NXT eligibility/session/product rules;
- fund cut-off/pricing/redemption timing, fee/product rules.

Task này không thêm current-state chỉ để “modernize” textbook. Không có số liệu
textbook nào bị âm thầm biến thành quy định 2026.

## 8. Structure / navigation / link audit

**PASS.**

- `06-stock-market-trading.md` đã sửa duplicate numbering: section sau 13 chạy
  liên tục thành 14–20.
- Whole-book heading-number scan không còn duplicate exact numbered heading.
- Navigation tuần tự tồn tại từ index → 01 → … → 13 → 90.
- Không có orphan lesson trong route canonical.
- Book 1 không dùng explicit `#anchor` links nội bộ, nên renumbering không để lại
  broken anchor.
- Relative links từ index/navigation trỏ tới file tồn tại.
- Canonical cross-links trong output README tới các owner trong `investing/`
  đã được kiểm tra tồn tại.

## 9. Canonical integration

**PASS.**

Ownership được tách rõ:

- raw/provenance owner: `증권투자기초/raw_md/sach1.md` và
  `증권투자기초/raw/sach1/`;
- source-specific learning route: `증권투자기초/output/book1/`;
- canonical concept owner: `investing/`.

`investing/README.md` đăng ký các source-book route của cả ba sách và giữ
`investing/` làm canonical concept owner. Book 1 tiếp tục ở
`증권투자기초/output/book1/`; Book 2/3 dùng
`book2/` và `book3/`. Không di
chuyển Book 1 chỉ để đồng nhất path khi ba lớp ownership vẫn phân biệt rõ.

## 10. Diff hygiene

**PASS.**

Branch được tạo trực tiếp từ current `main`. Changed-file set chỉ gồm Book 1
artifacts và `investing/README.md` là integration file bắt buộc.

Connector-based equivalent của `git diff --check` đã kiểm tra toàn bộ changed
text files: không có trailing whitespace và không có conflict marker. Môi trường
connector không cung cấp một local checkout để chạy literal CLI
`git diff --check`; vì toàn bộ Book 1 files là added files và README integration
đã được scan toàn file, kiểm tra này bao phủ lỗi whitespace/conflict mà lệnh đó
sẽ báo cho diff hiện tại.

## Definition of Done

- source → output audit: PASS
- output → source reverse audit: PASS
- source-question test: PASS
- reconstruction test: PASS
- learner replacement test: PASS
- terminology audit: PASS
- table/figure/formula audit: PASS
- internal-link audit: PASS
- duplicate-heading audit: PASS
- time-state boundary: PASS
- clean-branch/unrelated-diff audit: PASS

**Final verdict: PUBLICATION PASS.**
