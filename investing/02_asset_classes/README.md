# 02 — Asset Classes

Domain này giải thích từng nhóm tài sản theo bản chất kinh tế, nguồn lợi nhuận, rủi ro và cách chúng phản ứng trong các economic regime khác nhau. Mục tiêu không phải thuộc tên sản phẩm, mà biết mình đang mua quyền sở hữu, khoản nợ, real asset, cash-like claim, private asset hay derivative exposure nào.

## Thứ tự đọc

[01_STOCKS_ETF_AND_FUNDS.md](./01_STOCKS_ETF_AND_FUNDS.md) giải thích equity từ residual claim, diluted shares, dividends/buybacks/dilution và corporate actions tới voting/stewardship, index methodology/concentration, ETF NAV/iNAV/creation-redemption, liquidity under stress, tracking, physical/synthetic replication, securities lending, FX hedging, leveraged/inverse reset, Active Share, direct indexing và total cost of ownership.

[02_BONDS_RATES_AND_CREDIT.md](./02_BONDS_RATES_AND_CREDIT.md) xây nền fixed income từ coupon/yield/YTM/YTW tới duration, DV01, convexity, key-rate duration, yield curve, real yield, term premium, credit structure/spreads/default, callable/convertible bonds, inflation-linked bonds, MBS và bond-fund implementation.

[03_REAL_ASSETS_AND_ALTERNATIVES.md](./03_REAL_ASSETS_AND_ALTERNATIVES.md) đi sâu direct-property underwriting, NOI/FFO/AFFO, LTV/DSCR, cap rates, lease inflation pass-through, gold, commodity curves/convenience yield/cost curves, energy/metals/agriculture, infrastructure/concessions, crypto/stablecoin/protocol economics và private markets với LBO, IRR/MOIC/TVPI/DPI/RVPI, capital calls, subscription lines, vintage/secondary/denominator-effect risk.

[04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md](./04_FACTORS_INDEXING_AND_MULTI_ASSET_BEHAVIOR.md) nâng lên tầng systematic portfolio construction: market-cap/equal weight, value, quality, profitability, momentum, low volatility, size, dividend và smart beta; sau đó đi sâu factor definition, z-score/ranking, sector neutralization, factor attribution, value spread, factor crash, turnover/capacity, carry/trend ngoài equity, tracking-error budget, index-governance/methodology risk, active share và risk-controlled multi-factor implementation.

[05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md](./05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md) nối các asset classes thành portfolio thực tế: growth/inflation regimes, hidden duration, equity-credit linkage, cash optionality, FX decomposition, hedged/unhedged exposure và hedge ratio, futures/options hedging, inflation/deflation hedges, gold/commodities/REITs, 60/40, risk parity, trend/carry, volatility targeting, liquidity hierarchy, household balance sheet và regime-probability allocation.

[06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md](./06_CASH_MONEY_MARKETS_STRUCTURED_PRODUCTS_AND_PRIVATE_MARKETS.md) đào sâu cash/deposits/MMF/T-bills/CP/CD/repo/haircuts, structured notes/ELS/autocallables/barriers/worst-of/ETN và embedded options, sau đó đi sang PE/VC/private credit/private real estate/infrastructure, IRR/TVPI/DPI/RVPI, J-curve, capital calls, subscription lines, secondary markets, liquidity mismatch và private-market valuation smoothing.

## Sau domain này bạn cần làm được gì?

Bạn cần có khả năng nhìn một sản phẩm và xác định economic claim, return driver, liquidity, duration/credit/FX/factor risk; biết wrapper có làm thay đổi economic exposure hay chỉ cách triển khai; hiểu vì sao hai ETF cùng theme hoặc cùng factor label vẫn có thể khác nhau; phân rã return thành market beta, factor exposures và residual alpha; nhận ra hidden concentration giữa nhiều wrappers; phân biệt spot commodity với futures/producer equity; giải cấu trúc structured product thành bond + option risk và đọc private-fund performance mà không bị reported NAV/IRR đánh lừa.

Sau đó chuyển sang [03_company_analysis](../03_company_analysis/README.md) nếu muốn chọn cổ phiếu, hoặc [04_economics](../04_economics/README.md) nếu muốn đi sâu macro trước.