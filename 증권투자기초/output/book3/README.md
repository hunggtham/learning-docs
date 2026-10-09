# Sách 3 — Lý thuyết danh mục và phái sinh (증권투자기초 제3권)

Đây là learning route tiếng Việt được tái cấu trúc từ Sách 3 của `증권투자기초`. Sách có hai khối lớn: **포트폴리오 이론** (portfolio theory) ở Chương 1 và **금융파생상품** (financial derivatives) ở Chương 2. Mạch học đi từ đo lường bất định → danh mục → định giá cân bằng → đánh giá kết quả → hợp đồng phái sinh và cấu trúc payoff.

Raw OCR chỉ là provenance, không phải bản học: [sach3.md](../../sach3/raw_md/sach3.md). Bản đồ semantic và quyết định owner nằm ở [SOURCE_COVERAGE_BOOK3.md](../../sach3/SOURCE_COVERAGE_BOOK3.md). Publication QA được tách thành [source-question map](../../sach3/SOURCE_QUESTION_MAP_BOOK3.md), [OCR/source ambiguities](../../sach3/SOURCE_AMBIGUITIES_BOOK3.md), [formula/table/figure audit](../../sach3/FORMULA_TABLE_FIGURE_AUDIT_BOOK3.md) và [terminology audit](../../sach3/TERMINOLOGY_AUDIT_BOOK3.md).

## Lộ trình

1. [Thống kê cho đầu tư](./01_PORTFOLIO_STATISTICS.md) — biến ngẫu nhiên, kỳ vọng, phương sai, hiệp phương sai, tương quan, hồi quy.
2. [Danh mục và phân tán rủi ro](./02_PORTFOLIO_THEORY.md) — Markowitz, utility, efficient frontier, systematic/unsystematic risk.
3. [CAPM và thị trường hiệu quả](./03_CAPM_AND_EFFICIENT_MARKETS.md) — CML, beta, SML, EMH và anomaly.
4. [Đo lường thành quả và định giá doanh nghiệp](./04_PERFORMANCE_AND_VALUATION.md) — money/time-weighted return, Sharpe, Treynor, Jensen, DCF, EVA, multiples.
5. [Nền tảng phái sinh và sản phẩm theo chỉ số](./05_DERIVATIVES_FOUNDATIONS_AND_INDEX_PRODUCTS.md) — futures, options, margin, basis, hedge, index futures/options.
6. [Phái sinh lãi suất, tiền tệ, tín dụng và hàng hóa](./06_RATES_CURRENCY_CREDIT_COMMODITY_DERIVATIVES.md) — swaps, forwards, CDS, commodity term structure và hedge.
7. [OTC và chứng khoán phái sinh cấu trúc](./07_OTC_DERIVATIVES_AND_STRUCTURED_SECURITIES.md) — OTC, market participants, ELS/ELB/ELF/DLS/DLB, payoff, tax và risk.
8. [Integrated case lab](./08_INTEGRATED_CASE_LAB.md) — nối CAPM, DCF, portfolio hedge và structured payoff trong một quyết định có stress case.

## Cách dùng

Đọc từng file theo thứ tự. Các công thức được viết lại theo ký hiệu chuẩn để tránh lỗi OCR; ví dụ số và tên hợp đồng giữ mục đích minh họa của nguồn. Khi một khái niệm đã có owner sâu hơn trong `investing/`, file này giải thích phần cần cho Sách 3 rồi liên kết tới owner thay vì chép lại toàn bộ chương.

Mỗi lesson có ít nhất một **worked check**: người học phải thay số, đọc dấu của exposure và kiểm tra boundary (chi phí, basis, terminal assumption, margin hoặc counterparty), không chỉ ghi nhớ định nghĩa. Các ví dụ là mô hình học tập; không dùng như dự báo hay khuyến nghị giao dịch.

## Bản đồ raw → learning docs

| Trang raw | Lesson | Năng lực sau khi học |
|---|---|---|
| pp. 12–41 | 01 | tính kỳ vọng, variance, covariance, correlation và regression boundary |
| pp. 42–79 | 02 | tính portfolio risk, MVP, utility, frontier và constraint |
| pp. 80–134 | 03 | nối beta/CML/SML với EMH, event study và bias dữ liệu |
| pp. 135–200 | 04 | đo performance, dựng DCF/EV bridge, EVA và multiples |
| pp. 202–288 | 05 | đọc futures/options payoff, Greeks, margin, liquidity và synthetic flow |
| pp. 289–332 | 06 | hedge rate/FX/credit/commodity bằng sign, duration, basis và roll |
| pp. 333–381 | 07 | đọc OTC/ELS/ELB/DLS và các nhánh barrier, wrapper, issuer risk |
| toàn Chương 1–2 | 08 | tái dựng một quyết định từ valuation đến hedge và structured payoff |

Raw Markdown là provenance và có thể chứa OCR noise; khi công thức hoặc hình nguồn không chắc chắn, hãy dùng coverage artifact để biết phần nào đã được reconstruct và phần nào cần mở PDF gốc.

Điểm chốt của toàn route là: danh mục làm giảm phần rủi ro riêng lẻ nhưng không xóa được rủi ro hệ thống; phái sinh thay đổi exposure và hình dạng payoff chứ không làm mất giá trị danh nghĩa hay rủi ro thanh khoản; mọi kết quả cần được đọc cùng chi phí, ký quỹ, basis, counterparty và điều kiện thị trường.
