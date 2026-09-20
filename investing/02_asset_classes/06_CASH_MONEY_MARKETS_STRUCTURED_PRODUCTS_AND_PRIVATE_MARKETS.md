# 06 — Cash, Money Markets, Structured Products và Private Markets

Khi nói asset classes, người mới thường nghĩ tới stocks, bonds, gold và crypto. Nhưng portfolio thực tế còn chứa cash-like instruments, money-market claims, repo, structured notes và private assets. Những sản phẩm này thường trông “ổn định” hơn vì maturity ngắn hoặc price ít cập nhật, nhưng stability bề mặt không có nghĩa không có credit, liquidity, counterparty hay embedded-option risk.

Chapter này tập trung vào **economic substance**: ai nợ ai, cash flow đến từ đâu, collateral là gì, liquidity thực sự ra sao và yield cao đang bù cho risk nào.

# Phần I — Cash và Money Markets

## 1. Cash không phải “không đầu tư”

Cash cung cấp liquidity, optionality và principal stability tương đối. Với liability ngắn hạn, cash có thể là asset hợp lý nhất dù expected real return thấp.

Holding cash vì goal/liability khác holding cash do panic sau crash. Purpose matters.

## 2. Currency cash cũng có risk

Cash bằng KRW ổn định nominal theo KRW nhưng chịu inflation. USD cash của Korean investor thêm USD/KRW risk khi đo wealth bằng KRW.

“Cash” luôn phải nói rõ currency và institution.

## 3. Bank deposit là liability của bank

Deposit là claim đối với bank. Deposit insurance có thể giảm credit risk trong giới hạn luật/jurisdiction, nhưng không nên assume mọi balance đều insured.

Broker custody account và bank deposit có legal structure khác nhau.

## 4. Demand deposit vs time deposit

Demand deposits có liquidity cao. Time deposits đổi liquidity lấy yield và có early-withdrawal conditions.

Rate comparison phải account penalty, insurance coverage, tax và reinvestment opportunity.

## 5. Money Market Fund

MMF invests short-duration instruments. Types can differ: government-only, Treasury, prime/credit or jurisdiction-specific structures.

MMF is fund share, not automatically insured deposit. Underlying credit, liquidity rules, NAV mechanics and sponsor structure matter.

## 6. Treasury Bills

T-bills are short-term sovereign obligations. They often trade at discount to face value or quote yields under market conventions.

Short maturity means low duration, not zero price risk. Selling before maturity can still create small gain/loss.

## 7. Discount yield vs investment yield intuition

Money-market instruments may use quote conventions different from bond yield. Discount yield can divide discount by face value rather than purchase price and use 360-day basis.

Do not compare quoted yields across products without understanding convention.

## 8. Reinvestment risk

T-bill held to maturity returns principal, but future rate may be much lower. For a one-year cash need, rolling one-month bills exposes repeated reinvestment uncertainty.

Match maturity with liability when possible.

## 9. Commercial Paper

CP is short-term unsecured corporate debt. Yield spread over government bills compensates credit/liquidity risk.

Short maturity does not remove default risk; company can fail before maturity.

## 10. Certificate of Deposit

Tradable CDs are bank liabilities with market value. Their risk depends bank credit, deposit-insurance treatment, maturity and liquidity.

A high yield may simply reflect higher issuer/funding risk.

## 11. Bankers' acceptances and other short claims

Some money markets include trade-finance or bank-guaranteed instruments. Names vary across jurisdictions.

Always identify ultimate obligor/guarantor and secondary-market depth.

## 12. Repo

A **repurchase agreement** economically resembles collateralized short-term lending: one party sells security and agrees to repurchase later.

Collateral reduces but does not eliminate counterparty risk.

## 13. Repo rate

Repo rate is funding rate against specific collateral. It can diverge across collateral types and market stress.

Repo is central to dealer financing and monetary plumbing.

## 14. Haircut

Haircut means lender provides less cash than collateral market value. A 5% haircut on 100 collateral supports 95 cash.

Higher volatility/credit concern raises haircut, forcing borrower to post more collateral or deleverage.

## 15. General collateral vs special collateral

Some securities are in high borrowing demand and trade “special” in repo, making funding economics different from generic collateral.

This shows collateral has convenience/liquidity value beyond coupon.

## 16. Secured does not mean risk-free

Collateral price can gap, legal enforcement can be delayed and counterparty default can occur. Margining/haircuts reduce expected loss but do not eliminate operational/legal risk.

## 17. Money-market yield curve

Short rates reflect central-bank policy expectations, liquidity and credit. Overnight, 1m, 3m and 1y instruments may price different future paths.

Cash allocation can therefore have duration/reinvestment choices even at short maturities.

## 18. Cash ladder

A cash ladder matches maturity buckets to future needs, for example 3m/6m/12m.

It reduces both unnecessary duration and reinvestment concentration.

## 19. Cash buffer and liquidity tiering

Portfolio can separate immediate cash, near-term T-bills/MMF and longer-term defensive assets.

This prevents every “safe” asset being treated as equally liquid.

## 20. Cash drag

Cash lowers volatility but can reduce long-run return. Opportunity cost is larger when risk assets offer high expected return and cash rates are low.

Cash weight should have explicit role.

# Phần II — Structured Products

## 21. Structured product là gì?

Structured product combines debt/deposit-like claim with derivatives to manufacture payoff linked to equity, index, FX, rates or commodities.

Marketing coupon is not free yield. It usually compensates investor for selling optionality, accepting issuer credit or giving up liquidity/upside.

## 22. Decompose before evaluating

Ask whether product can be approximated as:

`Zero-coupon bond + option positions`

Decomposition reveals where coupon comes from.

## 23. Principal protection

“Principal protected” may mean only if held to maturity and issuer remains solvent. Before maturity, mark-to-market can be below par.

Read conditions, not product name.

## 24. Capital-at-risk notes

Some notes pay high coupons while exposing investor to large downside if reference asset breaches barrier.

High coupon often means investor is effectively short put-like risk.

## 25. Autocallable / ELS

Autocallable observes underlying periodically. If conditions met, it redeems early with coupon. If not, exposure continues and barrier conditions can create nonlinear downside.

Path matters, not just final price.

## 26. Barrier risk

Knock-in/knock-out barriers can make payoff change discontinuously. Near barrier, hedging demand and gamma exposure may become large.

Retail investor should understand exact trigger convention: intraday, closing, observation dates or maturity only.

## 27. Worst-of structures

Basket note may depend on worst-performing underlying rather than average. Diversifying across multiple names can paradoxically increase probability one performs badly enough to trigger loss.

Correlation assumptions matter.

## 28. Callable notes

Issuer call feature means investor may not control maturity. Product can be redeemed when it is favorable for issuer.

Yield comparison should consider call probability, not headline maturity yield only.

## 29. Range accrual

Coupon may accrue only when reference rate/index stays within range. Higher coupon compensates path dependence and conditional payment.

Need scenario simulation, not simple yield-to-maturity thinking.

## 30. Reverse convertible

Reverse convertible often pays high coupon while investor accepts downside equity exposure below threshold.

Economically similar to bond plus short put in simplified form.

## 31. ETN

ETN is unsecured issuer debt linked to index/strategy. Investor faces both reference-index risk and issuer credit risk.

ETF and ETN are not interchangeable wrappers.

## 32. Embedded leverage

Some structured products have payoff multiplier, leveraged downside or capped upside. Leverage can be hidden because investor only sees coupon/participation rate.

Draw payoff diagram before investing.

## 33. Mark-to-market opacity

Structured notes may have dealer model pricing and wide secondary-market spreads. Exit before maturity can be expensive.

Quoted indicative value is not guaranteed executable price.

## 34. Issuer margin and distribution cost

Complex products can embed structuring/distribution margin not obvious as annual expense ratio.

Compare to DIY components where possible.

## 35. Counterparty risk

If payoff is contract with issuer, even perfect underlying performance does not guarantee payment after issuer default.

Legal seniority matters.

## 36. Suitability framework

Structured product makes sense only if investor understands payoff, can hold through liquidity constraints and specifically wants that payoff distribution.

High headline coupon alone is not reason.

# Phần III — Private Equity và Venture Capital

## 37. Private Equity

PE funds buy private companies or take public companies private, often using leverage and operational change.

Return sources may include revenue/margin growth, deleveraging and exit multiple. Multiple expansion is less controllable than operational improvement.

## 38. Leveraged Buyout

LBO uses debt at portfolio company level. Equity return can be amplified if enterprise value grows and debt is repaid.

But leverage increases downside and refinancing risk.

## 39. Management fees and carried interest

Private funds often charge management fee plus carried interest on profits subject to terms such as hurdle/preferred return and catch-up.

Fee structure strongly affects LP net return.

## 40. Commitment vs invested capital

LP commits capital but fund calls it over time. Uncalled capital is **unfunded commitment**, an economic liability.

Liquidity planning must reserve for calls.

## 41. J-curve

Early fund years may show negative return because fees/costs arrive before exits. Later value creation and realizations can turn curve positive.

Comparing young funds with mature funds requires vintage awareness.

## 42. Vintage year

Funds deploying capital during expensive boom face different entry valuations than recession vintages.

Diversifying commitments over vintages can reduce timing concentration.

## 43. IRR

Private funds commonly report **Internal Rate of Return (IRR)**, which is sensitive to cash-flow timing.

Fast early distributions can boost IRR even if total multiple moderate.

## 44. MOIC/TVPI

**MOIC** or **TVPI** measures total value relative invested capital. It complements IRR by showing multiple of money.

A high IRR with low MOIC over short period and lower IRR with high MOIC over long period describe different outcomes.

## 45. DPI and RVPI

**DPI** = distributions / paid-in capital; it measures realized cash returned. **RVPI** = residual value / paid-in capital; it is unrealized NAV.

`TVPI = DPI + RVPI`

High TVPI driven mostly RVPI is less realized than high DPI.

## 46. Valuation marks

Private company NAV relies models, comparables and financing rounds. Marks can lag public-market repricing.

Reported smoothness should not be confused with low economic volatility.

## 47. Subscription credit lines

Funds may use short-term credit facilities before calling LP capital. This can delay capital calls and mechanically improve reported IRR timing.

Analyze cash economics and not IRR alone.

## 48. Venture Capital

VC return distribution is power-law-like: few winners drive fund return. Failure is common.

Access, ownership dilution, follow-on funding and exit markets are key.

## 49. Follow-on reserves

VC funds reserve capital to support winners. Failure to follow pro rata can dilute ownership in strongest companies.

Portfolio construction includes initial bets and follow-on strategy.

# Phần IV — Private Credit

## 50. Private credit economics

Private credit lends outside public bond markets. Yield may reflect illiquidity, borrower complexity, covenant package and higher risk.

Direct lending can offer floating-rate income but rising rates may stress borrower coverage.

## 51. Seniority

First-lien senior debt has priority over second-lien, mezzanine and equity. Recovery expectations differ substantially.

Headline yield must be viewed together with capital structure position.

## 52. Covenants

Maintenance covenants can detect deterioration early and give lender negotiation leverage. Covenant-lite loans reduce these protections.

Terms matter as much as coupon.

## 53. Interest coverage

Coverage ratios compare earnings/cash flow with interest. Floating-rate debt can deteriorate rapidly when benchmark rates rise.

Stress coverage using lower EBITDA and higher rates simultaneously.

## 54. PIK interest

**Payment-in-Kind (PIK)** interest capitalizes rather than paying cash. Reported yield increases but cash realization is delayed and debt burden compounds.

High PIK dependence can indicate borrower stress.

## 55. Recovery and collateral

Collateral appraisal may prove optimistic in default. Recovery depends asset liquidity, legal priority and restructuring process.

Do not treat collateral book value as guaranteed recovery.

## 56. Fund-level leverage

Private-credit fund can leverage its loan portfolio, magnifying both income and losses.

Distinguish borrower leverage from fund leverage.

## 57. Redemption mismatch

Open-ended vehicle offering frequent redemptions while owning illiquid loans can face gates or suspension.

Liquidity promise deserves separate due diligence from asset quality.

# Phần V — Private Real Estate và Infrastructure

## 58. Private real estate

Return comes from NOI growth, leverage, cap-rate change and development. Appraisal-based NAV can lag market.

Property type and geography matter.

## 59. Leverage

Real estate debt magnifies equity return but refinancing rates and LTV covenant matter.

Falling property values can breach covenants even if property still occupied.

## 60. Infrastructure

Infrastructure includes utilities, roads, airports, pipelines, renewable assets and digital infrastructure.

Long contracts can stabilize revenue but regulatory/counterparty/concession risk remains.

## 61. Inflation linkage

Some contracts have CPI-linked escalators. This creates inflation sensitivity but caps/floors and regulatory lag determine effectiveness.

## 62. Political/regulatory risk

Tariffs, concession rules and allowed returns can change. Infrastructure is physical but cash flows often policy-dependent.

# Phần VI — Illiquidity và Secondary Markets

## 63. Illiquidity premium

Expected extra return for locking capital is not guaranteed. If investors overpay private assets, future illiquidity premium can disappear.

Illiquidity is cost, not source of magic alpha.

## 64. Behavioral benefit of illiquidity

Not seeing daily prices can reduce panic selling, but this is behavioral smoothing—not risk reduction.

Economic value can still fall sharply.

## 65. Secondary private markets

LP interests or private shares can sometimes be sold in secondary markets, often at discount/premium to reported NAV.

Secondary price reveals liquidity conditions and confidence in marks.

## 66. Denominator effect

When public markets fall quickly but private NAV lags, private assets become larger share of total portfolio mechanically.

Institutional investors may need sell private interests or reduce new commitments to restore allocation.

## 67. Capital-call stress

Market crisis can combine public asset losses with private capital calls. Investor may need liquidity exactly when public assets are down.

This is why unfunded commitments belong in portfolio stress tests.

# Phần VII — Product Due Diligence

## 68. Legal claim

First question: am I depositor, fund shareholder, unsecured creditor, limited partner or derivative counterparty?

Legal claim defines recovery and rights.

## 69. Return source

Coupon/yield should map to economic source: short rates, credit spread, option premium, leverage, illiquidity or manager skill.

If source unclear, risk likely unclear.

## 70. Liquidity

Ask normal liquidity and stressed liquidity. Daily NAV does not guarantee daily executable exit for all products.

## 71. Valuation

Is price exchange-traded, dealer-quoted, model-based or appraisal-based? How often updated? Who controls assumptions?

Valuation governance matters.

## 72. Counterparty

Identify issuer, custodian, collateral agent, GP/manager and derivative counterparties.

Structure can have multiple failure points.

## 73. Leverage

Leverage may exist at investor, fund, portfolio-company or derivative layer simultaneously.

Look through all layers.

## 74. Fees

Include management, performance/carry, structuring, distribution, financing, FX, spread and exit fees.

Headline management fee can understate total cost.

## 75. Worst-case scenario

Do not ask only “expected return?”. Ask what happens under issuer default, barrier breach, redemption run, capital call during crash or refinancing failure.

Scenario clarity is prerequisite to sizing.

## 76. Final framework

Before allocating to any complex product, answer in writing:

`Underlying → Legal Claim → Cash-flow Source → Liquidity → Leverage → Counterparty → Valuation → Fees → Tax → Stress Scenario → Portfolio Role`

If one layer is missing, due diligence is incomplete.

## 77. Kết luận

Cash-like products, structured notes and private markets are not exotic side topics. They expose core concepts of finance very clearly: time value, credit, collateral, optionality, liquidity and legal priority.

The more complex the wrapper, the more important it is to strip the product back to those basic economic building blocks.