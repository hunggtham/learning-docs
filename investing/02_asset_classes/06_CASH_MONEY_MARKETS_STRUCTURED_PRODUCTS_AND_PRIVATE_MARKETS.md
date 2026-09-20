# 06 — Cash, Money Markets, Structured Products và Private Markets

> Cash-like instruments và private assets thường nhìn “êm” hơn public equities vì maturity ngắn hoặc mark-to-market ít thường xuyên. Nhưng sự ổn định bề mặt có thể che credit, liquidity, counterparty, leverage, valuation và embedded-option risk. Chapter này tập trung vào **economic substance**: ai nợ ai, cash flow đến từ đâu, collateral là gì, optionality nằm ở đâu và liquidity thực tế thế nào.

# Phần I — Cash và Money Markets

## 1. Cash không phải “không đầu tư”

Cash cung cấp nominal stability, liquidity và optionality. Với near-term liability, cash có thể là asset phù hợp nhất dù expected real return thấp.

Holding cash vì plan khác hoàn toàn holding cash vì panic. Strategic cash phải có role rõ: emergency reserve, liability bucket, collateral buffer hay dry powder.

## 2. Cash luôn có Currency Risk tương đối

KRW cash ổn định theo KRW nhưng chịu inflation. USD cash của Korean investor chịu USD/KRW translation risk. VND cash chịu local inflation và policy/currency risk.

“Cash” vì vậy luôn phải đi cùng câu hỏi: **cash bằng currency nào và phục vụ liability nào?**

## 3. Bank Deposit là Liability của Bank

Deposit là claim với bank, không phải tiền mặt nằm riêng chờ bạn. Deposit insurance có thể giảm loss risk trong limits/jurisdiction nhất định, nhưng rules phải được kiểm tra hiện hành.

Bank deposit, broker cash balance, money-market fund share và Treasury bill có legal claim khác nhau dù app đều hiển thị “cash-like”.

## 4. Demand Deposit và Time Deposit

Demand deposit đổi yield lấy liquidity. Time deposit đổi liquidity lấy yield cao hơn và có early-withdrawal conditions.

Comparison phải gồm insurance coverage, early-break penalty, tax, liquidity và reinvestment risk.

## 5. Money Market Fund

Money Market Fund (*MMF*) đầu tư short-duration instruments. Government MMF, Treasury MMF và prime/credit MMF có underlying risk khác nhau.

MMF không tự động giống insured deposit. Investor phải đọc NAV mechanism, liquidity gates/rules, weighted-average maturity, issuer concentration và sponsor structure.

## 6. Treasury Bills

T-bills là short-term sovereign obligations. Low duration không đồng nghĩa zero risk: selling before maturity vẫn có small price risk; foreign investor còn có FX risk.

T-bills đặc biệt hữu ích cho liability matching vì maturity rõ và credit/liquidity thường cao trong major sovereign markets.

## 7. Money-Market Quote Conventions

Discount yield, money-market yield và bond-equivalent yield có thể dùng denominator/day-count khác nhau.

Hai instruments cùng quote “5%” không nhất thiết economically identical. Khi compare, convert về consistent annualized basis nếu cần.

## 8. Day-Count Convention

Money-market contracts có thể dùng Actual/360, Actual/365 hoặc conventions khác. Điều này ảnh hưởng accrued interest và quoted yield.

Đây là chi tiết nhỏ nhưng quan trọng khi instruments có thin spread differences.

## 9. Reinvestment Risk

Rolling one-month bills liên tục tạo uncertainty về future short rates. Nếu goal chắc chắn sau 12 tháng, 12-month maturity có thể match liability tốt hơn chuỗi 1-month roll.

Short duration giảm price risk nhưng tăng reinvestment frequency.

## 10. Commercial Paper

Commercial Paper (*CP*) là short-term unsecured corporate funding. Spread trên government bills bù credit và liquidity risk.

Short maturity không remove default risk. Issuer phụ thuộc rollover market có thể gặp crisis nếu investors refuse refinancing.

## 11. Certificate of Deposit

Tradable CD là bank liability có secondary-market value. Credit, deposit-insurance treatment và liquidity phụ thuộc instrument/jurisdiction.

High CD rate thường phản ánh bank funding need; yield cao cần được đọc cùng issuer credit.

## 12. Repo

Repurchase agreement (*repo*) economically giống collateralized short-term loan: borrower đưa securities làm collateral và nhận cash, rồi reverse transaction sau.

Repo là core funding channel cho dealers và là phần quan trọng của monetary plumbing.

## 13. Repo Rate và Collateral Value

Repo rate phụ thuộc funding conditions và collateral desirability. High-quality collateral có thể finance rẻ hơn.

Một security có thể trở thành “special” khi demand borrow cao, khiến repo economics khác general collateral.

## 14. Haircut

Haircut nghĩa lender cho cash thấp hơn collateral market value. Collateral 100 với haircut 5% hỗ trợ 95 cash.

Khi volatility tăng, haircuts có thể tăng, buộc leveraged holder post thêm collateral hoặc deleverage. Đây là một transmission channel của liquidity crisis.

## 15. Margin Spiral

Sequence thường là:

```text
Asset Price ↓
→ Collateral Value ↓
→ Haircut / Margin ↑
→ Forced Sales ↑
→ Asset Price ↓ further
```

Money-market plumbing vì vậy có thể biến market risk thành funding/liquidity crisis.

## 16. Secured không đồng nghĩa Risk-Free

Collateral có thể gap, legal enforcement chậm hoặc collateral itself correlated với borrower stress.

Repo risk gồm counterparty, collateral quality, haircut adequacy, operational settlement và legal enforceability.

## 17. Counterparty Concentration

Cash management thường focus yield nhưng bỏ qua institution concentration. Keeping all liquidity at one bank/broker creates operational/credit concentration.

Large balances nên được map theo legal entity và guarantee/segregation structure, không chỉ brand.

## 18. Money-Market Yield Curve

Overnight, 1m, 3m, 6m và 1y rates price policy expectations, liquidity và credit.

Steep/inverted short curve affects cash-ladder choices. Cash allocation vẫn có curve/reinvestment decision dù duration ngắn.

## 19. Cash Ladder

Cash ladder chia future needs theo maturity buckets: immediate, 3m, 6m, 12m hoặc longer.

Objective không phải maximize yield mà match liquidity timing với minimum unnecessary risk.

## 20. Liquidity Tiering

Một framework:

```text
Tier 1: Immediate bank/broker cash
Tier 2: T-bills / Government MMF
Tier 3: Short high-quality bonds
Tier 4: Risk assets / illiquid assets
```

Near-term liabilities không nên phụ thuộc Tier 4 liquidation trong stress.

## 21. Cash Drag và Optionality

Cash giảm expected return trong bull market nhưng có option value khi opportunities xuất hiện hoặc liabilities đến.

Cash weight nên được evaluate against risk of forced selling, not against equity return alone.

# Phần II — Structured Products

## 22. Structured Product là gì?

Structured product kết hợp debt-like claim với derivatives để tạo payoff linked equity, FX, rates, commodities hoặc baskets.

Headline coupon thường đến từ option premium, issuer spread, leverage hoặc giving up upside/liquidity. “Yield cao” luôn phải được decomposed.

## 23. Decomposition trước Marketing Name

Một product có thể approximate:

```text
Zero-Coupon Bond
+ Long / Short Options
+ Issuer Credit Exposure
+ Structuring Margin
```

Nếu không vẽ được payoff từ components, investor chưa hiểu product.

## 24. Principal Protection

“Principal protected” thường chỉ có nghĩa under specified conditions và if issuer solvent, thường at maturity.

Market value trước maturity vẫn có thể dưới par. Protection không loại issuer default risk.

## 25. Participation Rate

Một note có thể trả 80% upside của index nhưng protect downside tới một threshold. Participation rate là price của protection/cap structure.

Luôn so payoff với direct asset + Treasury + options DIY alternative.

## 26. Capital-at-Risk Note

High coupon có thể compensation cho short put-like downside. Nếu barrier breached, investor có thể nhận underlying hoặc loss proportional to decline.

Coupon nhỏ không bù được large tail loss nếu structure negatively convex.

## 27. Autocallable / ELS

Autocallable có observation dates; nếu condition đạt, note redeems early. Nếu not called, investor tiếp tục carry risk.

Expected maturity có thể ngắn trong benign market nhưng kéo dài đúng lúc underlying weak, tạo unfavorable path dependence.

## 28. Knock-In / Knock-Out Barriers

Barrier convention có thể continuous, closing-only hoặc observation-date only.

Near barrier, option Greeks và hedging demand có thể change sharply. Retail investor cần hiểu trigger mechanics chính xác.

## 29. Worst-of Basket

Worst-of payoff phụ thuộc asset tệ nhất trong basket. Thêm nhiều underlyings đôi khi tăng chance một asset breach barrier.

Correlation là core input: lower correlation có thể làm worst-of structure riskier dù “basket diversified” nghe hấp dẫn.

## 30. Correlation Risk trong Structured Notes

Issuer prices basket options using implied correlations. Investor effectively takes view không chỉ từng underlying mà cả dependence structure.

Trong crisis, correlations thường rise, thay payoff probability và hedge behavior.

## 31. Callable Notes

Issuer call feature gives issuer timing option. Product có thể terminate khi continuation favorable cho investor, leaving reinvestment risk.

Yield-to-maturity headline không meaningful nếu call probability high.

## 32. Range Accrual

Coupon accrues only while reference stays in range. Product therefore short volatility around boundaries.

Need scenario/path simulation, not simple annual coupon comparison.

## 33. Reverse Convertible

Reverse convertible ≈ issuer debt + investor short put in simplified economics.

High coupon is payment for absorbing equity downside and issuer credit risk.

## 34. ETN

Exchange-Traded Note (*ETN*) là unsecured debt linked to index/strategy. Investor bears reference-index risk + issuer credit risk.

Unlike ETF, ETN normally does not own underlying basket in same legal way.

## 35. Embedded Leverage

Payoff multiplier, barrier or participation can create hidden leverage even if investor pays cash upfront.

Stress payoff, not purchase price. A 100-unit note can have downside equivalent to much larger notional around barrier.

## 36. Mark-to-Market Opacity

Dealer model values can differ from executable secondary bid. Wide spread và low secondary liquidity can make early exit costly.

Do not assume indicative value is realizable.

## 37. Structuring Margin

Complex products may embed issuer/distributor margin invisible as annual expense ratio.

Compare fair value of bond + options against issue price where disclosure allows. Complexity often increases hidden friction.

## 38. Counterparty / Issuer Risk

Perfect underlying performance does not guarantee payment if issuer defaults.

Legal seniority and bail-in/restructuring treatment matter. Structured product analysis must start with legal claim before payoff chart.

## 39. Greeks của Structured Product

Autocallables/worst-of notes can be short gamma, short vega and exposed to correlation skew. Risk becomes nonlinear near barriers/observation dates.

Retail investor không cần calculate every Greek but should understand that coupon comes from selling convexity.

## 40. Structured-Product Due Diligence

Write payoff under at least: +20%, flat, -10%, -30%, barrier breach, high volatility, issuer stress và early exit.

If one scenario outcome surprises you, product chưa được hiểu đủ để size.

# Phần III — Private Equity và Venture Capital

## 41. Private Equity Return Decomposition

PE return có thể decompose:

```text
Revenue Growth
+ Margin Improvement
+ Debt Paydown
+ Multiple Change
- Fees / Carry
```

Multiple expansion is market-dependent; operational improvement/deleveraging controllable hơn.

## 42. Leveraged Buyout

LBO uses debt at portfolio-company level. Leverage magnifies equity IRR if EV grows and debt falls, but also magnifies downside/refinancing risk.

Entry valuation matters enormously because high purchase multiple leaves less room for return without aggressive assumptions.

## 43. Commitment vs Paid-In Capital

LP commitment is future funding obligation. **Unfunded commitment** behaves like contingent liability.

Portfolio liquidity stress must reserve capacity for calls during public-market downturns.

## 44. J-Curve

Early years may show negative net return due fees/investment ramp; realizations arrive later.

J-curve is cash-flow timing pattern, not proof fund will recover.

## 45. Vintage Year

Funds investing in different vintages face different entry multiples, financing rates and exit environments.

Diversifying commitments over time reduces dependence on one cycle peak.

## 46. IRR

IRR is highly timing-sensitive. Subscription lines or early small distributions can mechanically improve IRR.

Never evaluate private fund using IRR alone.

## 47. MOIC / TVPI

**MOIC/TVPI** measures total value relative paid-in capital. It answers “how many dollars of value exist per dollar invested?” rather than timing.

IRR + TVPI together are more informative than either alone.

## 48. DPI và RVPI

**DPI** = realized distributions / paid-in capital. **RVPI** = residual NAV / paid-in capital.

```text
TVPI = DPI + RVPI
```

High TVPI dominated by RVPI is mostly unrealized and depends mark quality/exits.

## 49. PME — Public Market Equivalent

**PME** compares private-fund cash flows with public benchmark using same timing.

It helps answer whether illiquidity/fees were compensated relative to investable public alternative.

## 50. Valuation Marks

Private NAV uses comparables, DCF, financing rounds and manager judgment. Marks can lag public repricing.

Smooth reported NAV does not mean low economic volatility; stale pricing can artificially improve Sharpe/correlation metrics.

## 51. Subscription Lines

Fund may borrow short-term before calling LP capital. This can improve reported IRR by delaying denominator timing.

Economic analysis should reconstruct underlying asset return and leverage, not accept headline IRR mechanically.

## 52. Fund-Level Leverage

Private fund may borrow at fund level in addition to portfolio-company leverage. Layered leverage increases liquidity/covenant risk.

Look through all leverage layers.

## 53. Venture Capital Power-Law Distribution

VC outcomes are highly skewed: a few winners may drive fund return.

Portfolio construction therefore needs enough shots, follow-on reserves and discipline around ownership/dilution.

## 54. Follow-On Reserves

Reserve capital lets fund defend ownership in winners. Too little reserve causes dilution; too much can trap capital in losers if governance weak.

Follow-on decision quality is part of manager alpha.

## 55. Exit Market Dependency

VC/PE value realization depends IPO/M&A/secondary markets. NAV can remain high while distributions stall when exit window closes.

DPI therefore becomes especially important in weak capital-market regimes.

# Phần IV — Private Credit

## 56. Private Credit Return Source

Yield comes from base rate + credit spread + illiquidity/complexity premium + fees, sometimes enhanced by fund leverage.

Higher yield should be mapped to borrower quality, covenant strength, seniority và liquidity.

## 57. First Lien, Second Lien và Mezzanine

Seniority drives recovery priority. First-lien secured generally safer than second-lien/mezzanine but collateral quality still matters.

Headline coupon without capital-structure position is meaningless.

## 58. Interest Coverage

Stress both earnings and rates:

```text
Coverage = EBITDA / Cash Interest
```

Floating-rate borrower can see interest expense surge exactly when economy slows.

## 59. PIK Interest

Payment-in-Kind interest capitalizes into principal instead of cash payment.

It raises stated yield but delays realization and increases leverage. Rising PIK share can signal borrower stress.

## 60. Covenants

Maintenance covenants provide early intervention rights. Covenant-lite structures reduce lender control.

Read baskets, add-backs, EBITDA definitions and leakage provisions, not only headline leverage covenant.

## 61. EBITDA Add-Back Risk

Private credit/LBO documents may allow “adjusted EBITDA” with synergies or cost savings not yet realized.

Leverage measured on aggressive adjusted EBITDA can materially understate real debt burden.

## 62. Recovery and Collateral

Recovery depends realizable collateral value, legal priority, restructuring time and expenses.

Book/appraisal value often overstates stressed liquidation value.

## 63. Redemption Mismatch

Open-ended fund offering frequent redemptions while holding illiquid private loans can face gates or suspension.

Liquidity promise of vehicle is separate from credit quality of assets.

# Phần V — Private Real Estate và Infrastructure

## 64. Private Real Estate Economics

Return comes from NOI growth, leverage, cap-rate move and development/value-add.

Appraisal-based NAV can lag transaction market. Debt maturity and refinancing rate often determine equity outcome more than reported annual volatility.

## 65. LTV và DSCR

**Loan-to-Value (LTV)** measures debt relative property value. **Debt-Service Coverage Ratio (DSCR)** measures property cash flow relative debt service.

Falling value raises LTV; rising rates reduce DSCR. Both can trigger covenant/refinancing stress.

## 66. Development Risk

Ground-up development includes construction-cost, delay, leasing and financing risk. Stabilized asset and development project should not share same required return.

## 67. Infrastructure

Roads, airports, pipelines, utilities và data infrastructure can have long-duration contracted cash flows.

But political/regulatory, concession-renewal, counterparty and capex risk remain. “Infrastructure” is not automatically bond-like.

## 68. Inflation Linkage

CPI-linked tariffs can hedge inflation only if pass-through timely and enforceable. Caps/floors/regulatory lag reduce hedge quality.

# Phần VI — Liquidity, Secondaries và Portfolio Effects

## 69. Illiquidity Premium

Illiquidity is a cost investor may or may not be compensated for. High entry valuation/fees can consume any premium.

Do not assume private = higher expected return by definition.

## 70. Behavioral Smoothing

Not seeing daily price may reduce panic but does not reduce economic risk.

Portfolio risk systems should adjust private volatility/correlation for stale marks rather than use reported NAV series naively.

## 71. Secondary Markets

LP interests/private shares can trade at discount/premium to NAV. Secondary price contains information about liquidity and mark credibility.

During stress, discount can widen even if manager NAV unchanged.

## 72. Denominator Effect

If public assets fall fast while private NAVs lag, private allocation percentage rises mechanically.

Institutional investor may be forced to slow commitments or sell secondaries to restore policy weights.

## 73. Capital-Call Stress

Worst combination is public drawdown + capital calls + weak distributions.

Stress unfunded commitments as liabilities, not optional future investments.

## 74. Liquidity Waterfall

Plan which assets fund cash needs first, second and last. Avoid selling deeply discounted illiquid assets when liquid reserves could have been held strategically.

## 75. Public vs Private Benchmarking

Compare private return after all fees, leverage and timing against appropriate public benchmark using PME or similar methodology.

“Private fund returned 15% IRR” says little without opportunity-cost benchmark.

# Phần VII — Due Diligence Framework

## 76. Legal Claim

Identify whether you are depositor, fund shareholder, unsecured creditor, limited partner or derivative counterparty.

Legal claim determines recovery rights before return analysis.

## 77. Return Source

Map yield to source:

```text
Short Rate
Credit Spread
Option Premium
Leverage
Illiquidity
Manager Skill
Asset Appreciation
```

If source cannot be identified, risk cannot be identified either.

## 78. Valuation Method

Exchange price, dealer quote, model mark và appraisal have different information quality.

Ask frequency, governance, independent verification and lag.

## 79. Leverage Map

Leverage may exist at investor, fund, SPV, portfolio company and derivative level simultaneously.

A “low-vol” private product can be highly leveraged underneath.

## 80. Fee Map

Include management fee, carry/performance fee, structuring margin, financing, FX, spread, custody, transaction and exit costs.

Net return after all friction is what matters.

## 81. Counterparty Map

Identify bank, issuer, GP, custodian, sub-custodian, collateral agent and derivative counterparties.

Multiple legal entities mean multiple failure points.

## 82. Stress Test

At minimum test issuer default, barrier breach, redemption gate, capital call during crash, refinancing failure, collateral haircut increase and FX shock.

Complex product should be sized by stressed loss/liquidity, not headline coupon.

## 83. Portfolio Role

Every allocation should answer one purpose: liquidity, income, diversification, inflation sensitivity, growth, liability matching or asymmetric speculation.

If role is simply “yield cao hơn”, analysis chưa đủ.

## 84. Final Framework

```text
Underlying Economics
→ Legal Claim
→ Cash-Flow Source
→ Optionality / Leverage
→ Counterparty / Collateral
→ Valuation Method
→ Liquidity
→ Fees / Tax
→ Stress Behavior
→ Portfolio Role
```

Cash-like và private products không cần bị tránh chỉ vì complex. Nhưng complexity phải được paid for bằng clear economic benefit, và investor phải biết chính xác risk nào đang được nhận để đổi lấy return.