# 증권투자기초 — Sách 2 learning route

Đây là bản learning edition của Sách 2, được xây từ [source authority](../../증권투자기초/raw/sach2.md) và audit theo [coverage granular](../../증권투자기초/sach2/SOURCE_COVERAGE_BOOK2.md). Bộ QA đi kèm gồm [source-question map](../../증권투자기초/sach2/SOURCE_QUESTION_MAP_BOOK2.md), [formula/table/figure audit](../../증권투자기초/sach2/FORMULA_TABLE_FIGURE_AUDIT_BOOK2.md), [KR/EN terminology audit](../../증권투자기초/sach2/TERMINOLOGY_AUDIT_BOOK2.md) và [source ambiguities](../../증권투자기초/sach2/SOURCE_AMBIGUITIES_BOOK2.md).

Mục tiêu của route này là **thay source OCR để học**, không thay thế canonical owner chuyên sâu của toàn library. Mỗi chapter giữ knowledge của giáo trình theo bốn lớp: **What → Why/mechanism → Application/relationship → Boundary/exception**.

## Lộ trình 6 bài

1. [Nền tảng đầu tư, macro, industry và phân tích tài chính](./01_SECURITIES_MACRO_AND_FINANCIAL_ANALYSIS.md)
2. [Định giá cổ phiếu: dòng tiền, CAPM và multiples](./02_EQUITY_VALUATION_AND_MULTIPLES.md)
3. [Phân tích kỹ thuật: pattern, candlestick và indicators](./03_TECHNICAL_ANALYSIS.md)
4. [Chiến lược đầu tư, diversification và stock-price index](./04_INVESTMENT_STRATEGIES_AND_INDICES.md)
5. [Trái phiếu và fixed-income instruments](./05_BONDS_AND_FIXED_INCOME_INSTRUMENTS.md)
6. [YTM, term structure, credit, duration, market và bond index](./06_BOND_YIELDS_RISK_DURATION_AND_INDICES.md)

## Cách đọc terminology

Khi source hoặc authoritative Korean usage xác nhận một thuật ngữ quan trọng, lần xuất hiện hữu ích đầu tiên dùng dạng:

```text
Thuật ngữ Việt (English / 한국어)
```

Không gắn Hangul cho noun thông thường và không “khôi phục” Korean wording khi OCR/source không đủ evidence.

## Source questions

Các review question trong source được audit riêng trong [SOURCE_QUESTION_MAP_BOOK2.md](../../증권투자기초/sach2/SOURCE_QUESTION_MAP_BOOK2.md), theo chuỗi **source cluster → semantic units → lesson**. Câu hỏi không được dùng như một semantic row để che nhiều concept. Nếu wording, option hoặc số liệu OCR không đủ chắc, [SOURCE_AMBIGUITIES_BOOK2.md](../../증권투자기초/sach2/SOURCE_AMBIGUITIES_BOOK2.md) giữ `SOURCE_AMBIGUITY`; route cung cấp reasoning cho phần đã xác nhận nhưng không đoán đáp án.

## Formula / table / figure contract

Knowledge-bearing formula/table/figure được reconstruct khi evidence đủ, kèm:

- câu dẫn cách đọc;
- variable/assumption;
- explanation sau block;
- boundary/exception;
- worked example khi người mới cần để hiểu mechanism.

Figure technical-analysis không còn đủ ảnh hình học trong OCR được reconstruct bằng structure/prose; chi tiết không đọc chắc không được bịa.

## Canonical owners

Khi cần depth vượt source, đi sang owner tương ứng:

- [Foundations](../01_foundations/README.md)
- [Asset Classes](../02_asset_classes/README.md)
- [Company Analysis](../03_company_analysis/README.md)
- [Economics](../04_economics/README.md)
- [Trading & Derivatives](../05_trading_derivatives/README.md)
- [Korea/Vietnam Markets](../06_markets_korea_vietnam/README.md)
- [Integrated Cases](../07_integrated_case_studies/README.md)

Các owner trên mở rộng depth; chúng không được dùng để che unit source-specific bị thiếu khỏi route này.

## Provenance và publication boundary

- Provenance/coverage: [`../../증권투자기초/sach2/`](../../증권투자기초/sach2/README.md)
- Source authority: [`../../증권투자기초/raw/sach2.md`](../../증권투자기초/raw/sach2.md)
- Không có normalized `raw_md/sach2.md` canonical trong publication pass này.
- Institutional/current-state claims phải được kiểm tra ở owner/current sources; các tên/index/benchmark trong chapter được hiểu theo trạng thái textbook khi không ghi khác.
