# Cổ phiếu, ETF và quỹ đầu tư

> Chapter này giải thích equity và fund products từ bản chất economic claim tới cách chọn wrapper. Mục tiêu là tránh hai nhầm lẫn phổ biến: coi mọi cổ phiếu chỉ là ticker để trade và coi mọi ETF là một “asset an toàn”. Stock là residual ownership; ETF/fund là vehicle chứa một exposure cụ thể.

## 1. Common stock là residual claim

Common shareholder sở hữu phần residual value của company sau operating obligations, taxes và creditors. Nếu business phát triển, equity holder có upside lớn; nếu company insolvency, common equity thường chịu loss cuối cùng sau creditors.

Ownership không có nghĩa shareholder trực tiếp lấy company cash. Cash chỉ đến shareholder qua dividends, buybacks, liquidation hoặc sale of shares to another investor. Economic value đến từ future cash-generation capacity của business và capital allocation.

## 2. Market capitalization và enterprise value

Market capitalization:

`Market Cap = Share Price × Shares Outstanding`

Share price riêng lẻ không nói company “đắt” hay “lớn”. Stock giá 500.000 KRW/share có thể có market cap nhỏ hơn stock 5.000 KRW nếu share count khác.

Enterprise Value (*EV*) gần đúng:

`EV = Equity Value + Debt - Cash + other claims/adjustments`

EV hữu ích khi so operating businesses với capital structures khác nhau.

## 3. Shares outstanding, float và free float

Shares outstanding là shares economically outstanding. Free float là phần có thể freely trade, excluding strategic/controlling holdings theo methodology.

Low free float can amplify volatility and index behavior. Market-cap weighted index often uses free-float-adjusted market cap rather than total shares.

For investor, low float means liquidity and ownership-concentration risk.

## 4. Stock return đến từ đâu?

Long-run shareholder return can be decomposed conceptually:

`Return ≈ earnings/cash-flow growth + shareholder distributions + valuation change`

If EPS grows 10% but P/E compresses 30x to 20x, stock can decline. Conversely weak current earnings can coexist with rally if market anticipates recovery.

This is why “company tốt” does not equal “stock will rise”. Starting expectations and valuation matter.

## 5. Dividends

Dividend transfers cash from company to shareholder. Ex-dividend price generally adjusts because company has less cash after distribution.

Dividend yield is not free return. Very high yield may reflect falling price or unsustainable payout. Analyze payout relative FCF, leverage and reinvestment opportunities.

Dividend growth can indicate durable cash generation, but forced high payout can underinvest business.

## 6. Buybacks

Buyback reduces share count only if shares are repurchased and not reissued/offset by employee dilution. Economic benefit depends purchase price.

Repurchasing undervalued shares can increase per-share value. Buying expensive shares using debt can destroy value.

Always compare buyback cash spent with net change in diluted shares.

## 7. Dilution

New issuance, stock-based compensation, convertibles and warrants can increase diluted share count. Business may grow total earnings while per-share economics lag.

For early growth companies, dilution can be a legitimate financing cost; investor should model fully diluted shares instead of ignoring it.

## 8. Stock split và reverse split

Stock split changes units, not enterprise value. A 2-for-1 split doubles shares and halves theoretical price. Reverse split does opposite.

Do not interpret lower post-split price as cheaper valuation.

## 9. Rights offering

Rights offering lets existing shareholders buy newly issued shares, often at discount. If shareholder does not participate/sell rights, economic ownership can dilute.

Evaluate why capital is raised: high-ROIC expansion, balance-sheet repair or repeated funding of weak economics?

## 10. Preferred shares

Preferred shares often have priority on dividends/liquidation vs common but limited voting/upside characteristics. Terms vary dramatically.

Some Korean preferred shares can trade at discount to common due liquidity/voting differences. Discount is not automatically arbitrage because rights differ.

## 11. Index là rule set

Index is not “market itself”; it is rules selecting and weighting securities. Common weighting: market-cap/free-float cap, equal weight, price weight or factor rules.

Methodology determines exposure. Two indices both called “technology” can differ materially by eligibility, rebalancing and concentration.

## 12. Rebalancing và reconstitution

Index periodically rebalances weights and may add/remove constituents. Funds tracking index must trade accordingly, creating technical flows.

Inclusion can move price before/around effective date, but it does not change company intrinsic value directly.

## 13. ETF là wrapper

Exchange-Traded Fund (*ETF*) issues shares that trade on exchange while fund owns/replicates underlying exposure. Underlying can be stocks, bonds, commodities, futures, options or systematic strategy.

Question “ETF có an toàn không?” is incomplete. Broad government-bond ETF and 3x leveraged semiconductor ETF are both ETFs but risk radically different.

## 14. NAV

Net Asset Value:

`NAV per share = (Fund assets - liabilities) / shares outstanding`

ETF market price can differ from NAV due intraday moves, stale underlying prices, liquidity or stress.

Premium = market price > NAV; discount = market price < NAV. Neither alone indicates bargain/mispricing without understanding price freshness.

## 15. Creation-redemption và Authorized Participants

Authorized Participants (*APs*) can create/redeem ETF units using basket or cash according methodology. If ETF trades rich vs basket, arbitrage can create shares/sell ETF; if cheap, reverse.

This mechanism usually anchors liquid ETF price, but during stressed/closed underlying markets deviations can widen.

## 16. Primary vs secondary ETF liquidity

Visible ETF volume is secondary-market liquidity. But ETF can also source liquidity from underlying basket through creation/redemption.

Low ETF volume does not automatically mean impossible to trade if underlying highly liquid, but spreads may still be wider. Large order should consider both ETF book and underlying liquidity.

## 17. Expense ratio

Expense ratio is annual recurring fund cost. Small difference compounds over years, especially broad passive products with similar exposures.

But cheapest fund is not always best if tracking, spread, tax, lending policy or AUM differ.

## 18. Tracking difference và tracking error

*Tracking difference* = actual fund return minus benchmark return over period. It includes fee, tax drag, replication, cash and securities-lending effects.

*Tracking error* measures variability of that difference. A fund consistently -0.15% behind benchmark can have low tracking error; fund alternating +1/-1 may have high tracking error.

## 19. Physical replication

Physical ETF holds all or sample of index securities. Full replication suits liquid indices; sampling may reduce cost for broad/illiquid indices.

Sampling introduces tracking risk because fund does not hold exact basket.

## 20. Synthetic replication

Synthetic ETF may use swap/derivative to receive benchmark return. This can improve access/tracking but adds counterparty/collateral structure.

Synthetic does not automatically mean bad; evaluate swap counterparty, collateral, reset and regulation.

## 21. Securities lending

Physical funds may lend securities to short sellers and earn lending revenue, potentially offsetting fees. But it introduces counterparty/collateral operational risk.

Read how lending revenue is shared between fund and manager.

## 22. Currency exposure

Trading currency does not define economic currency. Korean-listed US ETF bought in KRW can still be economically exposed to USD.

Approx home-currency return:

`(1 + underlying return) × (1 + FX return) - 1`

If S&P rises 8% in USD but USD weakens 7% vs KRW, KRW return can be much lower.

## 23. Currency-hedged ETF

Hedged fund uses forwards/futures/swaps to reduce FX exposure. Hedge cost/benefit reflects rate differentials and implementation.

Hedging reduces currency volatility but does not make underlying asset safer. Equity drawdown remains.

## 24. Leveraged ETF

Leveraged ETF typically targets multiple of DAILY return. Daily reset produces path dependency.

Example underlying +10% then -9.09% returns to original. 2x fund approximately +20% then -18.18%: 1.2 × 0.8182 ≈ 0.982, a loss despite flat underlying.

Volatility drag grows with leverage and oscillation.

## 25. Inverse ETF

Inverse fund targets negative daily return. It can be tactical hedge but long holding can deviate greatly from simple inverse cumulative performance.

Use only if daily reset behavior understood.

## 26. Active ETF

Active ETF does not mechanically follow static index. Manager may select holdings within mandate.

Due diligence becomes manager/process oriented: philosophy, portfolio construction, turnover, capacity, benchmark, fees and historical factor exposures.

## 27. Mutual fund

Mutual funds transact at end-of-day NAV rather than intraday exchange price in many structures. They can be passive or active.

ETF vs mutual fund is wrapper comparison; strategy exposure can be identical.

## 28. Index fund

Index fund aims replicate benchmark. “Passive” does not mean neutral: benchmark methodology makes active-like design choices about inclusion and weighting.

A cap-weighted index automatically concentrates in companies whose market caps become largest.

## 29. Active fund và alpha

Active performance should be judged against appropriate benchmark and factor exposures after fees.

If fund outperforms because it simply held more small-cap/value/momentum, return may be factor beta rather than manager-specific alpha.

Consistency, capacity and turnover matter.

## 30. Style drift

Fund marketed as dividend/value may gradually move toward growth/tech to chase performance. This changes portfolio role.

Monitor holdings and factor exposures, not name only.

## 31. Concentration risk in thematic ETFs

Thematic ETF can appear diversified by holding 30 names yet all depend same economic factor—AI capex, lithium price, biotech funding.

Ticker count is not diversification. Identify common revenue drivers and correlations under stress.

## 32. Broad-market ETF

Broad ETF reduces company-specific research burden and usually offers low-cost beta. It is often suitable core holding when investor believes market-wide earnings growth more predictable than single-name selection.

But broad index still carries country, sector, valuation and concentration risks.

## 33. Sector ETF

Sector ETF expresses industry view without picking exact winner. Useful when thesis is macro/industry but company uncertainty high.

Trade-off: you own weak firms alongside winners and index weights may concentrate in leaders after rally.

## 34. Bond ETF

Bond ETF should be analyzed by duration, credit, yield, maturity bucket, currency and underlying liquidity, not simply called “defensive”.

Long Treasury ETF can be more volatile than some equities when yields move sharply.

## 35. Commodity ETF/ETN

Commodity product may hold physical commodity, futures or note. Futures curve/roll yield and issuer risk can dominate result.

Read product structure before assuming it tracks spot.

## 36. Fund distributions

ETF/fund may distribute dividends/interest or reinvest. Distribution yield is not total return.

Large distribution reduces NAV mechanically. Compare total-return series, not price chart only.

## 37. Premium/discount around market-hour mismatch

Korean ETF tracking US assets trades while US cash market may be closed. Its price reflects futures/FX/current information while official NAV based stale close.

App may show apparent large premium/discount that is partly time-zone valuation difference.

## 38. AUM và closure risk

Very small fund can face closure/merger if economically unviable. Closure usually returns NAV value but can create tax/reinvestment inconvenience.

AUM alone is not quality; combine with spread, issuer stability and underlying liquidity.

## 39. Due-diligence checklist cho ETF

Before buying answer: benchmark/mandate; holdings; weighting; rebalancing; concentration; replication; currency hedge; leverage/reset; expense ratio; tracking difference; AUM; spread; underlying liquidity; distribution; securities lending; tax/account treatment and issuer/counterparty risks.

If cannot explain underlying exposure in one paragraph, do not buy because of theme name.

## 40. Single stock vs ETF

Single stock gives concentrated exposure and possible alpha if research edge exists. ETF lowers idiosyncratic risk and monitoring burden.

Core-satellite approach can use broad ETF core and smaller single-stock/thematic positions. But it is framework, not universal optimal allocation.

## 41. When single-stock diversification is fake

Holding Samsung Electronics, SK hynix and semiconductor ETF creates multiple tickers but one semiconductor factor. Similarly banks/property/securities in Vietnam may share domestic credit/liquidity factor.

Aggregate by economic drivers, not names.

## 42. Mental model cuối cùng

Analyze equity/fund product through:

`Underlying economic claim → index/manager rules → wrapper structure → fees/tracking → currency → liquidity → portfolio factor exposure`

Ticker is last layer, not first.