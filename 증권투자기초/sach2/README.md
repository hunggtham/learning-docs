# Sách 2 — source/provenance

Thư mục này **không phải learning route**. Nó giữ provenance, source boundary và coverage cho Sách 2 của `증권투자기초`.

## Source authority

- Content authority: [`../raw/sach2.md`](../raw/sach2.md)
- Hiện **không có** canonical `raw_md/sach2.md`.
- Audit publication pass này **không tạo** một normalized raw giả chỉ để đồng nhất path với Sách 1.
- Repo cũng không có asset/image gốc riêng cho Sách 2 ngoài raw Markdown hiện tại. Những nơi OCR không đủ evidence được ghi chính xác trong [SOURCE_COVERAGE_BOOK2.md](./SOURCE_COVERAGE_BOOK2.md) bằng `SOURCE_AMBIGUITY`.

Nếu sau này có scan/image gốc hoặc normalized transcription được tạo từ evidence thật, file đó phải ghi transformation/provenance rõ và không được thay raw source chỉ vì dễ đọc hơn.

## Canonical conversion contract

Sách 2 đã được re-audit từ source theo các contract hiện có của repository, bao gồm:

- `prompt/COMMON_PROMPT.md`
- `prompt/BOOK_MD_TO_LEARNING_DOCS_PROMPT.md`
- `prompt/DOCS_AUDIT_PROMPT.md`
- `prompt/DOCS_REVIEW_PROMPT.md`

Claim cũ rằng `BOOK_MD_TO_LEARNING_DOCS_PROMPT.md` “không tồn tại trong checkout” đã lỗi thời và **không còn áp dụng**. Publication pass hiện tại dùng prompt đó như canonical source-to-learning contract.

## Learning route

Bản để học/đọc nằm tại:

- [`../../investing/90_securities_book2/README.md`](../../investing/90_securities_book2/README.md)

Coverage và các audit artifact nằm tại:

- [`SOURCE_COVERAGE_BOOK2.md`](./SOURCE_COVERAGE_BOOK2.md) — semantic inventory/source → output.
- [`SOURCE_QUESTION_MAP_BOOK2.md`](./SOURCE_QUESTION_MAP_BOOK2.md) — source review/exercise → required units → lesson.
- [`FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md`](./FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md) — formula/table/figure reconstruction contract.
- [`TERMINOLOGY_AUDIT_BOOK2.md`](./TERMINOLOGY_AUDIT_BOOK2.md) — KR/EN terminology bridge.
- [`SOURCE_AMBIGUITIES_BOOK2.md`](./SOURCE_AMBIGUITIES_BOOK2.md) — exact OCR/source evidence boundary.

Branch cũ `feat/securities-investment-book2-learning-edition` chỉ được dùng làm **prose reference**. Publication pass không merge branch đó; nội dung cần thiết được mang sang/regenerate trên clean branch từ current `main` rồi re-audit lại theo source.

## Architecture convention

Không tạo layout thứ tư cho bộ sách. Sách 2 dùng convention tách rõ hai vai trò:

```text
증권투자기초/
├── raw/sach2.md                 # source authority
└── sach2/                       # provenance + coverage
    ├── README.md
    ├── SOURCE_COVERAGE_BOOK2.md
    ├── SOURCE_QUESTION_MAP_BOOK2.md
    ├── FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md
    ├── TERMINOLOGY_AUDIT_BOOK2.md
    └── SOURCE_AMBIGUITIES_BOOK2.md

investing/
└── 90_securities_book2/         # publication/learning route
```

Convention này khớp hướng tách source/provenance khỏi canonical learning route đang dùng cho source-book integration trong `investing/`.

## Textbook-state boundary

Source là giáo trình; tên tổ chức, benchmark, market convention, luật, thuế, cấu phần index và institutional details có thể thay đổi theo thời gian. Learning route chỉ giữ chúng như **textbook-state/source examples** khi cần hiểu kiến thức.

Các owner chuyên sâu/current-facing nằm trong `investing/`, đặc biệt:

- [Foundations](../../investing/01_foundations/README.md)
- [Asset Classes](../../investing/02_asset_classes/README.md)
- [Company Analysis](../../investing/03_company_analysis/README.md)
- [Economics](../../investing/04_economics/README.md)
- [Trading & Derivatives](../../investing/05_trading_derivatives/README.md)
- [Korea/Vietnam Markets](../../investing/06_markets_korea_vietnam/README.md)

Cross-link sang owner **không thay thế** knowledge source-specific: semantic unit của source vẫn phải xuất hiện đủ trong learning route hoặc được ghi ambiguity.
