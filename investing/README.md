# Investing Knowledge Library

Bộ tài liệu này được tổ chức theo domain thay vì một master book khổng lồ. Mỗi folder có một mục tiêu học rõ ràng, tài liệu core và các chapter nâng cao để chuyển kiến thức sang phân tích thực tế. Ngoài sáu domain kiến thức chính, thư viện hiện có một lớp **research conventions** dùng chung và một **capstone domain** để nối theory → analysis → position → execution → review.

## 00 — Glossary, Formulas & Research Conventions

[00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md](./00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)

Đây là reference dùng xuyên toàn bộ library: terminology, nominal/real return, CAGR, volatility/correlation, portfolio variance, beta/alpha, Sharpe/Sortino/IR, drawdown, VaR/ES, PV/DCF, EV vs Equity Value, FCFF/FCFE, ROIC/reinvestment, duration/DV01, credit expected loss, FX-return decomposition, derivatives notional, option payoff, expectancy, benchmark convention, point-in-time data, source hierarchy, timestamp rules, scenario/thesis/invalidation và performance attribution.

Nếu gặp cùng một thuật ngữ ở nhiều chapter, file này là nơi kiểm tra convention chung trước khi đi vào phần chuyên sâu.

## Cấu trúc domain

### 01 — Foundations

[01_foundations/README.md](./01_foundations/README.md)

Học tiền, hệ thống tài chính, market mechanics, portfolio risk, allocation, behavioral finance, lifecycle investing, rebalancing, custody, investment operations và portfolio analytics. Phần nâng cao hiện bao gồm volatility/drawdown, covariance, beta/alpha, Sharpe/Sortino/Calmar, VaR/Expected Shortfall, stress testing, performance attribution, fee/tax drag, decision journal và behavioral review.

### 02 — Asset Classes

[02_asset_classes/README.md](./02_asset_classes/README.md)

Học stocks, ETF/funds, bonds/credit, real assets, commodities, alternatives, factor investing, smart beta, index methodology, FX exposure và multi-asset regimes. Phần nâng cao nối các tài sản thành portfolio qua duration, carry/roll-down, credit spreads, currency hedging, risk contribution, robust allocation, cash/MMF/T-bills, structured products, ETN, private equity, venture capital, private credit và infrastructure.

### 03 — Company Analysis

[03_company_analysis/README.md](./03_company_analysis/README.md)

Học financial statements, accounting, business quality, moat, value chain, industry structure, valuation, DCF, earnings quality, working capital, unit economics, three-statement modeling và forensic analysis. Phần sector-specific cover banks, semiconductors, SaaS, retail, REITs và nhiều ngành mở rộng; phần governance/capital allocation bổ sung incremental ROIC, capex quality, dividends, buybacks, dilution, M&A, goodwill, controlling shareholders và management incentives.

### 04 — Economics

[04_economics/README.md](./04_economics/README.md)

Học microeconomics, macroeconomics, global economy, capital flows, banking/sovereign crises, macro data, central banking, monetary plumbing, repo/collateral, dollar funding và financial-conditions transmission. Phần nâng cao bổ sung regime thinking, crisis history, fiscal–monetary interaction, government debt dynamics, Treasury supply, term premium, fiscal dominance, demographics, productivity, TFP, institutions và neutral-rate framework.

### 05 — Trading & Derivatives

[05_trading_derivatives/README.md](./05_trading_derivatives/README.md)

Học Forex, futures, options, swaps, CFD, leverage/margin/collateral, technical structure, position sizing, expectancy, backtest, execution, order-book microstructure và trading-portfolio risk. Phần research nâng cao cover out-of-sample, walk-forward, data biases, parameter stability, transaction cost, market impact, Monte Carlo, strategy degradation, portfolio of strategies, volatility surface, Greeks interaction, event volatility, dynamic hedging và operational safety.

### 06 — Korea & Vietnam Markets

[06_markets_korea_vietnam/README.md](./06_markets_korea_vietnam/README.md)

Áp dụng toàn bộ framework vào KRX/KOSPI/KOSDAQ và HOSE/HNX/UPCoM, với sector maps, KRW/VND, BOK/SBV, semiconductor, banks, property, FDI, foreign flows, cross-market shocks và workflow research thực tế. Phần cross-border bổ sung four-currency framework, hedging, local wrappers/domicile, market access, settlement, custody, foreign room, repatriation, tax/withholding và operational resilience. Sector deep dives cover các ngành lớn của cả Korea và Vietnam với KPI, cycle, margin driver và valuation logic riêng.

### 07 — Integrated Case Studies

[07_integrated_case_studies/README.md](./07_integrated_case_studies/README.md)

Đây là capstone. Thay vì học thêm một theory domain mới, các case study buộc người đọc nối nhiều domain trong cùng một reasoning chain:

- [CPI Shock → Portfolio](./07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md): inflation composition → reaction function → yields/real yields → USD/KRW/VND → earnings/multiple → hedge/execution → attribution.
- [Credit & Liquidity Crisis](./07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md): duration mismatch → deposit/funding stress → collateral/haircut → forced selling → spreads/credit contraction → policy response → portfolio liquidity.
- [Korea Semiconductor Cycle](./07_integrated_case_studies/03_SEMICONDUCTOR_CYCLE_KOREA_CASE.md): AI capex → inventory/ASP/utilization → HBM/product mix → capex/suppliers → revisions → normalized valuation → position sizing.
- [Vietnam Property–Bank Credit Cycle](./07_integrated_case_studies/04_VIETNAM_PROPERTY_BANK_CREDIT_CASE.md): legal progress → presales/cash → refinancing → banks/NPL/provisions → domestic liquidity/SBV → valuation → stressed exit liquidity.

## Lộ trình học khuyến nghị

Nếu bắt đầu gần như từ số 0, đọc `00` trước như reference, sau đó đi theo:

```text
00 → 01 → 02 → 03 → 04 → 05 → 06 → 07
```

Không cần học thuộc `00`; hãy quay lại khi gặp thuật ngữ/công thức hoặc khi cần kiểm tra research convention.

Nếu mục tiêu chính là đầu tư dài hạn:

```text
00 → 01 → 02 → 03 → 04 → 06 → 07
```

Trading/derivatives có thể học sau, nhưng các phần hedge/execution trong case studies sẽ dễ hiểu hơn nếu đã đọc domain 05.

Nếu mục tiêu là macro/Forex:

```text
00 → 01 → 02 → 04 → 05 → 06 → 07
```

Vẫn nên quay lại Company Analysis để hiểu earnings channel và tại sao cùng một macro shock tạo outcome khác nhau giữa sectors/companies.

## Cách học để không biến thành đọc thụ động

Sau Foundations, tự viết Investment Policy Statement, stress-test portfolio theo ít nhất ba scenario và làm một monthly attribution review.

Sau Asset Classes, phân tích một ETF, một bond ETF, một cash-like product và một structured/private-market product theo legal claim, return driver, liquidity, optionality và embedded risk.

Sau Company Analysis, model một company với base/bull/bear case, chọn KPI đúng theo ngành, reconcile profit với cash flow và đánh giá lịch sử capital allocation của management.

Sau Economics, theo dõi một CPI/FOMC/BOK event từ consensus tới market reaction, xác định reaction function, curve/FX/credit transmission và phân biệt cyclical shock với structural regime change.

Sau Trading, backtest một setup duy nhất, làm out-of-sample/forward test, tính expectancy/drawdown, kiểm tra realistic execution và stress derivative positions theo P/L + margin/collateral path.

Sau Korea/Vietnam, tạo research notebook cho một stock Hàn và một stock Việt Nam, ghi rõ sector map, currency, market-access, balance-sheet risk, valuation, catalyst và thesis invalidation.

Cuối cùng, dùng domain 07 như bài kiểm tra tích hợp: trước khi đọc phần giải thích tiếp theo, tự viết causal chain và data cần kiểm tra cho từng case.

## Research note chuẩn sau khi hoàn thành library

Một note hoàn chỉnh nên trả lời tối thiểu:

```text
1. Legal/economic claim là gì?
2. Return driver chính là gì?
3. Facts, estimates và assumptions nào đang được dùng?
4. Market đang price expectation nào?
5. Driver tree và leading indicators là gì?
6. Base / Bull / Bear khác nhau ở mechanism nào?
7. Balance sheet và liquidity chịu được bear case không?
8. Valuation / expected return có đủ bù risk không?
9. Position duplicate factor nào trong portfolio?
10. Hedge / execution / total cost ra sao?
11. Catalyst và invalidation là gì?
12. Review cadence và attribution plan là gì?
```

## Mental model toàn thư viện

```text
Legal Claim
→ Financial System
→ Asset Class / Wrapper
→ Portfolio Construction
→ Company / Sector Economics
→ Macro Regime
→ Market Expectations
→ Valuation / Expected Return
→ Risk / Liquidity / Position Size
→ Execution / Hedge
→ Performance Attribution
→ Review & Thesis Update
```

Mục tiêu cuối cùng không phải dự báo mọi biến động giá. Mục tiêu là xây một hệ thống tư duy đủ rõ để biết mình đang sở hữu gì, return đến từ đâu, risk nằm ở đâu, market đang kỳ vọng điều gì, điều kiện nào làm thesis sai và evidence nào cần được cập nhật.

## Quy tắc cập nhật

Các nguyên lý nền tảng, accounting, valuation, portfolio theory và market microstructure có thể dùng lâu dài. Các phần về policy rates, tax, settlement, foreign-access rules, index classification, product specification và regulation phải được kiểm tra lại theo nguồn chính thức trước khi ra quyết định thật.

Snapshot macro trong các master note phải ghi rõ thời điểm. Fact động không có timestamp không nên được coi là knowledge vĩnh viễn.

Khi nội dung trùng giữa master note và chapter chuyên sâu, master note giữ vai trò overview/bridge; chapter chuyên sâu là source of truth cho mechanics. Khi cập nhật, ưu tiên link sang source-of-truth thay vì copy thêm một phiên bản mới.