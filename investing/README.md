# Investing Knowledge Library

Bộ tài liệu này được tổ chức theo domain thay vì một master book khổng lồ. Mỗi folder có một mục tiêu học rõ ràng, tài liệu core và các chapter nâng cao để chuyển kiến thức sang phân tích thực tế.

## Cấu trúc domain

### 01 — Foundations

[01_foundations/README.md](./01_foundations/README.md)

Học tiền, hệ thống tài chính, market mechanics, portfolio risk, allocation, behavioral finance, lifecycle investing, rebalancing, custody, investment operations và portfolio analytics. Phần nâng cao hiện bao gồm volatility/drawdown, covariance, beta/alpha, Sharpe/Sortino/Calmar, VaR/Expected Shortfall, stress testing, performance attribution, fee/tax drag, decision journal và behavioral review.

### 02 — Asset Classes

[02_asset_classes/README.md](./02_asset_classes/README.md)

Học stocks, ETF/funds, bonds/credit, real assets, commodities, alternatives, factor investing, smart beta, index methodology, FX exposure và multi-asset regimes. Phần nâng cao nối các tài sản thành portfolio qua duration, currency hedging, inflation/deflation hedges, risk parity, volatility targeting, cash/MMF/T-bills, structured products, ETN, private equity, venture capital, private credit và infrastructure.

### 03 — Company Analysis

[03_company_analysis/README.md](./03_company_analysis/README.md)

Học financial statements, accounting, business quality, moat, industry structure, valuation, DCF, earnings quality, working capital, unit economics, three-statement modeling và forensic analysis. Phần sector-specific cover banks, semiconductors, SaaS, retail và REITs; phần governance/capital allocation bổ sung incremental ROIC, capex quality, dividends, buybacks, dilution, M&A, goodwill, controlling shareholders và management incentives.

### 04 — Economics

[04_economics/README.md](./04_economics/README.md)

Học microeconomics, macroeconomics, global economy, capital flows, banking/sovereign crises, macro data, central banking, monetary plumbing, repo/collateral, dollar funding và financial-conditions transmission. Phần nâng cao bổ sung regime thinking, các crisis case lịch sử, fiscal–monetary interaction, government debt dynamics, Treasury supply, term premium, fiscal dominance, demographics, productivity, TFP, institutions và neutral-rate framework.

### 05 — Trading & Derivatives

[05_trading_derivatives/README.md](./05_trading_derivatives/README.md)

Học Forex, futures, options, CFD, leverage/margin, technical structure, position sizing, expectancy, backtest, execution, order-book microstructure và trading-portfolio risk. Phần research nâng cao cover in/out-of-sample, walk-forward, data biases, parameter stability, transaction cost, Monte Carlo, strategy degradation và portfolio of strategies. Options được mở rộng thêm với volatility surface, skew, term structure, Greeks interaction, event volatility, synthetic positions, dynamic hedging và tail-risk structures.

### 06 — Korea & Vietnam Markets

[06_markets_korea_vietnam/README.md](./06_markets_korea_vietnam/README.md)

Áp dụng toàn bộ framework vào KRX/KOSPI/KOSDAQ và HOSE/HNX/UPCoM, với sector maps, KRW/VND, BOK/SBV, semiconductor, banks, property, FDI, foreign flows, cross-market shocks và workflow research thực tế. Phần cross-border bổ sung currency decomposition, hedging, local wrappers, market access, settlement, foreign room, repatriation và operational/tax framework. Sector deep dives hiện cover các ngành lớn của cả Korea và Vietnam với KPI, cycle, margin driver và valuation logic riêng.

## Lộ trình học khuyến nghị

Nếu bắt đầu gần như từ số 0, đọc theo thứ tự `01 → 02 → 03 → 04 → 05 → 06`. Cách này đi từ hiểu tiền và sản phẩm, sang doanh nghiệp, rồi mở rộng ra nền kinh tế trước khi học trading và áp dụng theo thị trường.

Nếu mục tiêu chính là đầu tư dài hạn, ưu tiên `01 → 02 → 03 → 04 → 06`; trading/derivatives có thể học sau.

Nếu mục tiêu là macro/Forex, ưu tiên `01 → 02 → 04 → 05 → 06`, nhưng vẫn nên học company analysis để hiểu earnings channel và equity-market reaction.

## Cách học để không biến thành đọc thụ động

Sau Foundations, tự viết Investment Policy Statement, stress-test portfolio theo ít nhất ba scenario và làm một monthly attribution review. Sau Asset Classes, phân tích một ETF, một bond ETF, một cash-like product và một structured/private-market product theo legal claim, return driver, liquidity và embedded risk. Sau Company Analysis, model một company với base/bull/bear case, chọn KPI đúng theo ngành và đánh giá lịch sử capital allocation của management. Sau Economics, theo dõi một CPI/FOMC/BOK event từ consensus tới market reaction, xác định regime và giải thích đồng thời fiscal/monetary backdrop. Sau Trading, backtest một setup duy nhất, làm out-of-sample/forward test, tính expectancy/drawdown và stress option/derivative positions theo spot–volatility–time scenarios. Sau Korea/Vietnam, tạo research notebook cho một stock Hàn và một stock Việt Nam, ghi rõ sector map, currency, market-access, operational layer và thesis invalidation.

## Mental model toàn thư viện

```text
Financial System
→ Asset Class
→ Portfolio Construction
→ Company / Sector Economics
→ Macro Regime
→ Valuation / Expected Return
→ Position & Execution
→ Performance Attribution
→ Review & Thesis Update
```

Mục tiêu cuối cùng không phải dự báo mọi biến động giá. Mục tiêu là xây một hệ thống tư duy đủ rõ để biết mình đang sở hữu gì, return đến từ đâu, risk nằm ở đâu, điều kiện nào làm thesis sai và evidence nào cần được cập nhật.

## Quy tắc cập nhật

Các nguyên lý nền tảng, accounting, valuation, portfolio theory và market microstructure có thể dùng lâu dài. Các phần về policy rates, tax, settlement, foreign-access rules, index classification và regulation phải được kiểm tra lại theo nguồn chính thức trước khi ra quyết định thật.

Snapshot macro trong các master note được ghi rõ theo thời điểm để tránh biến dữ liệu hiện tại thành kiến thức vĩnh viễn.