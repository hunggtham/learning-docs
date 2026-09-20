# 02 — Asset Classes

Domain này giải thích từng nhóm tài sản theo bản chất kinh tế, nguồn lợi nhuận, rủi ro và cách chúng phản ứng trong các economic regime khác nhau. Mục tiêu không phải thuộc tên sản phẩm, mà hiểu mình đang mua quyền sở hữu, khoản nợ, real asset, cash-like claim, private asset hay derivative-like exposure nào, đồng thời biết implementation layer có thể làm realized return khác theoretical exposure ra sao.

## Thứ tự đọc

[01_STOCKS_ETF_AND_FUNDS.md](./01_STOCKS_ETF_AND_FUNDS.md) giải thích equity từ residual claim, diluted shares, dividends/buybacks/dilution và corporate actions tới voting/stewardship, index concentration, ETF NAV/iNAV/creation-redemption, liquidity under stress, tracking, physical/synthetic replication, FX hedging, leveraged/inverse reset, Active Share, direct indexing và total cost of ownership.

[02_BONDS_RATES_AND_CREDIT.md](./02_BONDS_RATES_AND_CREDIT.md) xây fixed-income thinking từ coupon/YTM/YTW, clean-vs-dirty price, duration/DV01/convexity/key-rate duration và yield curve tới carry/roll-down, Z-spread/OAS, credit spread/default/recovery, liquidity runway, rating migration, leveraged loans/covenants, callable/convertible bonds, TIPS, MBS/ABS/tranches, sovereign debt, bond ETFs, ladder/barbell/bullet, liability matching, rate/credit hedging và fixed-income return attribution.

[03_REAL_ASSETS_AND_ALTERNATIVES.md](./03_REAL_ASSETS_AND_ALTERNATIVES.md) đi sâu direct-property underwriting, NOI/FFO/AFFO, LTV/DSCR, cap rates, lease inflation pass-through, gold, commodity curves/convenience yield/cost curves, energy/metals/agriculture, infrastructure/concessions, crypto/stablecoin/protocol economics và private markets với LBO, IRR/MOIC/TVPI/DPI/RVPI, capital calls, subscription lines, vintage/secondary/denominator-effect risk.

[04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md](./04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md) nâng lên tầng systematic portfolio construction: market-cap/equal weight, value, quality, profitability, momentum, low volatility, size, dividend và smart beta; sau đó đi sâu factor definition/ranking, sector neutralization, attribution, value spread, factor crash, turnover/capacity, carry/trend ngoài equity, tracking-error budget, methodology risk, Active Share và risk-controlled multi-factor implementation.

[05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md](./05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md) nối asset classes thành portfolio hoàn chỉnh: growth/inflation regimes, duration/credit/liquidity factors, four-currency framework, strategic/dynamic FX hedge, futures/options/tail hedging, hedge budget/effectiveness, risk parity, marginal risk contribution, diversification ratio, trend/carry, volatility targeting, robust optimization, valuation overlay, liability-driven allocation, household balance sheet, stress/reverse-stress testing, return/risk attribution và portfolio governance.

[06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md](./06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md) đi sâu bank cash/MMF/T-bills/CP/CD/repo, quote/day-count conventions, haircuts/margin spirals và cash ladders; sau đó giải cấu trúc structured notes/ELS/autocallables/worst-of/ETN thành bond + option/correlation/issuer risk, rồi đi tới PE/VC/private credit/private real estate/infrastructure với IRR/MOIC/TVPI/DPI/RVPI/PME, leverage, EBITDA add-backs, PIK, LTV/DSCR, secondaries, capital calls, denominator effect và public-vs-private benchmarking.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng nhìn một product và xác định `economic claim → return source → duration/credit/FX/factor exposure → liquidity → leverage/optionality → wrapper → total cost → portfolio role`. Với fixed income, bạn phải tách carry/roll-down/rate/spread/default; với factors phải phân biệt label và implementation; với multi-asset phải nhìn risk contribution/currency/liability chứ không chỉ capital weight; với complex/private products phải nhìn xuyên headline yield hoặc smoothed NAV tới legal claim, leverage, cash-flow timing và stressed liquidity.

## Case studies để áp dụng

Đọc [CPI Shock → Portfolio](../07_integrated_case_studies/01_INFLATION_SHOCK_FROM_CPI_TO_PORTFOLIO.md) để thấy duration, real yield, FX, equity beta và hedging tương tác trong cùng một shock. Đọc [Credit & Liquidity Crisis](../07_integrated_case_studies/02_CREDIT_LIQUIDITY_CRISIS_TRANSMISSION.md) để luyện fixed-income spread, collateral, repo, private-market smoothing và liquidity hierarchy trong stress.

Sau đó chuyển sang [03_company_analysis](../03_company_analysis/README.md) nếu muốn chọn cổ phiếu, hoặc [04_economics](../04_economics/README.md) nếu muốn đi sâu macro trước.