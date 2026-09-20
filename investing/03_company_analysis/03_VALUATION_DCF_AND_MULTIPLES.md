# Valuation: DCF, multiples và scenario analysis

> Valuation không phải tìm một “giá đúng” duy nhất. Nó là quá trình chuyển assumptions về cash flow, growth, risk và capital allocation thành range of values, rồi so với expectations embedded trong market price. Precision đến từ hiểu drivers, không từ thêm nhiều decimal places.

## 1. Giá và value khác nhau

Market price là price giao dịch hiện tại. Intrinsic value là estimate của present value cash flows thuộc capital providers/shareholders dưới assumptions.

Price có thể deviate vì expectations, liquidity, flows và risk premia. Intrinsic value cũng uncertain vì future cash flows unknown.

Vì vậy valuation nên tạo range/scenarios thay vì một target price exact giả tạo.

## 2. Valuation là bài toán expectation

Investor return không phụ thuộc company “tốt” tuyệt đối mà phụ thuộc outcome relative to what price already assumes.

Một business tuyệt vời có thể tạo poor return nếu market already prices decades of flawless growth. Ngược lại, business trung bình có thể tạo strong return nếu expectations extremely depressed và fundamentals chỉ cần “less bad”.

## 3. Expected-return perspective

Một rough equity framework:

`Expected return ≈ fundamental per-share growth + shareholder yield + valuation change`

Company compound EPS/FCF 12% nhưng investor có thể earn less nếu multiple compresses. Expected return framework giúp nối intrinsic value với holding-period outcome.

## 4. Present value

`PV = CF_t / (1 + r)^t`

Higher discount rate lowers value, especially distant cash flows. Điều này tạo intuition về equity duration: growth company với value nằm xa tương lai nhạy với rate changes hơn mature cash generator.

## 5. Nominal vs real consistency

Nominal cash flows phải discount bằng nominal rate; real cash flows bằng real rate. Mixing làm model internally inconsistent.

Inflation tác động revenue, margin, working capital, capex và discount rate khác nhau. Không nên chỉ add inflation vào top-line growth rồi giữ mọi cost assumption unchanged.

## 6. Enterprise Value và Equity Value

Enterprise Value đại diện operating asset value cho debt + equity capital providers.

`EV ≈ Equity Value + Debt + Preferred + Minority Interest - Cash/non-operating assets`

Bridge exact phụ thuộc leases, pensions, associates, excess cash và other claims.

## 7. Net debt nuance

Không phải mọi cash đều excess. Operating cash, restricted cash hoặc trapped cash có thể không available.

Pension deficits, leases, environmental obligations hoặc supplier financing đôi khi có debt-like economics. Valuation bridge cần economic substance, không chỉ balance-sheet labels.

## 8. FCFF

`FCFF = EBIT(1-T) + D&A - Capex - ΔNWC`

Discount FCFF bằng WACC để ra enterprise value.

Forecast phải nối revenue/margins/reinvestment với business drivers, không phải chỉ CAGR arbitrary.

## 9. FCFE

`FCFE ≈ Net Income + D&A - Capex - ΔNWC + Net Borrowing`

Discount FCFE bằng cost of equity. FCFE useful khi capital structure relatively stable; leverage changes lớn làm cash flow volatile và FCFF thường cleaner.

## 10. Mid-year convention

Cash flows thực tế đến xuyên năm chứ không phải toàn bộ cuối năm. *Mid-year convention* discount cash flows trung bình khoảng giữa kỳ, làm valuation hơi cao hơn end-year convention khi everything else equal.

Điều quan trọng không phải memorize adjustment mà hiểu timing assumption ảnh hưởng PV.

## 11. Forecast revenue từ drivers

Thay vì “revenue +10%”, build causal model:

`Units/customers × price/ARPU × mix`

SaaS: beginning ARR + new ARR - churn + expansion. Semis: bit shipment × ASP. Retail: stores × sales/store + same-store sales. Bank: earning assets × spread + fees.

Driver model làm bull/bear causal và monitorable.

## 12. Margin forecast

Gross margin phụ thuộc price, mix, input, utilization và scale. Operating margin thêm R&D/SG&A/overheads.

Peak margins hiếm khi persist forever nếu excess returns attract competition. Model fade hoặc explain moat strong enough to resist it.

## 13. Reinvestment requirement

Growth cần capital:

`Growth ≈ Reinvestment Rate × Return on Incremental Capital`

Company tăng 20% nhưng incremental ROIC 5% phải consume capital lớn. Growth chỉ tạo value nếu return trên new capital đủ vượt cost of capital.

## 14. ROIC fade

Mature businesses thường thấy excess ROIC fade vì competition. Terminal assumptions cần decide ROIC eventually converge toward cost of capital, remain above due moat hay collapse below.

DCF that keeps 30% ROIC forever without economic explanation thường overvalue.

## 15. Growth fade

High growth không thể persist indefinitely vì market size, competition và law of large numbers.

Forecast nên có transition period từ high growth tới mature growth. Abrupt drop từ 30% năm 5 xuống 3% terminal thường mathematically convenient nhưng economically crude.

## 16. Working capital

Growth có thể absorb cash qua receivables/inventory. Model DSO/DIO/DPO hoặc working-capital-to-sales.

Negative working-capital business có thể finance growth via customers/suppliers; slowing growth có thể reverse benefit.

## 17. Capex, depreciation và maintenance

Trong steady state, capex không thể thấp hơn economic depreciation mãi. Growth businesses often capex > D&A; asset-light firms có intangible investment qua R&D/S&M thay vì physical capex.

Valuation phải capture economic reinvestment kể cả khi accounting expensed.

## 18. R&D capitalization intuition

Software/pharma/semiconductor có thể expense R&D dù một phần tạo multi-year assets. Analyst có thể capitalize R&D để better match investment and returns, nhưng assumptions về useful life/amortization matter.

Mục tiêu là hiểu economics, không “improve” earnings artificially.

## 19. Stock-based compensation

SBC là economic cost qua dilution dù non-cash trong cash flow statement.

Nếu add SBC back to FCF, model phải reflect higher future diluted shares or equivalent repurchase cost. Không thể vừa treat SBC free vừa ignore dilution.

## 20. Diluted share count

Per-share valuation nên dùng fully diluted share count, including options/warrants/convertibles when economically relevant.

Treasury-stock method hoặc if-converted method có accounting detail; intuition đơn giản là potential claims trên equity phải được recognized.

## 21. Taxes và NOLs

Effective tax rate có thể khác statutory vì geographic mix, tax credits, NOLs và one-offs.

Net Operating Losses có thể shield future taxes nhưng finite and conditional. Forecast tax normalization khi benefits expire.

## 22. Explicit forecast period

Forecast period nên đủ dài để business transition toward stable economics. Mature utility có thể 5–7 năm; high-growth platform có thể cần longer.

Longer horizon chỉ meaningful nếu assumptions có causal foundation.

## 23. Terminal value

Gordon growth:

`TV = FCF_(n+1) / (WACC - g)`

Terminal value thường chiếm phần lớn DCF. Vì denominator small, WACC/g errors matter massively.

Terminal assumptions phải internally consistent với growth, reinvestment và ROIC.

## 24. Terminal growth consistency

Long-run `g` không nên exceed sustainable nominal economy growth indefinitely trừ special assumptions.

Nếu business terminal growth 3% và terminal ROIC 15%, reinvestment rate implied khoảng 20%. Model phải actually fund growth đó.

## 25. Exit multiple terminal value

Alternative là apply terminal EV/EBITDA/P-E. Nó không eliminate uncertainty; chỉ convert uncertainty thành future multiple assumption.

Cross-check Gordon và exit multiple để detect inconsistent terminal economics.

## 26. WACC

`WACC = w_e × Cost of Equity + w_d × After-tax Cost of Debt`

Weights nên reflect sustainable market-value capital structure. WACC phải consistent với currency, inflation và leverage assumptions.

## 27. Cost of equity

CAPM:

`Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium`

Beta/ERP estimates uncertain. CAPM useful framework nhưng không physical law.

Nếu thêm country/small-cap premiums, cần avoid double counting risks already embedded in cash flows or beta.

## 28. Risk-free rate theo currency

Discount rate nên match cash-flow currency. KRW nominal cash flows không thể casually discount bằng USD risk-free mà bỏ FX/inflation consistency.

For multinational, model segment cash flows hoặc use coherent home-currency translation framework.

## 29. Country risk

Country risk có thể đến political, legal, capital controls, sovereign spread, FX convertibility và governance.

Có thể reflect through cash-flow scenarios hoặc discount premium, nhưng đừng double count. Scenario modeling thường clearer khi risk is discrete/nonlinear.

## 30. Cost of debt

Dùng current marginal borrowing cost hơn historical coupon. Stressed company có market yield cao hơn book interest.

Tax shield có value chỉ khi taxable income and laws allow. Debt cost should reflect maturity/refinancing profile.

## 31. Capital structure và leverage feedback

WACC không constant nếu leverage thay. Distressed company có cost of debt/equity explode khi value falls.

For highly leveraged business, Adjusted Present Value (*APV*) hoặc scenario analysis đôi khi clearer than single WACC.

## 32. Sensitivity table

At minimum vary WACC và terminal growth. Better vary revenue CAGR, margins, ROIC/reinvestment.

Nếu valuation moves từ 50 đến 150 với tiny change, fragility itself là key insight.

## 33. Tornado analysis

*Tornado chart* rank valuation sensitivity theo assumptions: volume, price, margin, WACC, terminal growth, capex, working capital.

Điều này giúp biết research time nên tập trung driver nào thay vì refine variables low impact.

## 34. Scenario analysis

Base/bull/bear phải có causal stories. Semiconductor bear: ASP down, utilization low, inventory correction, capex sticky. Bull: HBM mix, supply discipline, pricing strong.

Không nên simply +/-20% target value.

## 35. Probability-weighted valuation

`Expected Value = Σ p_i × Value_i`

Probabilities là judgment. Purpose là force explicit distributions.

Low-probability tail loss có thể vẫn require position-size control dù expected value positive.

## 36. Monte Carlo valuation

Monte Carlo sample multiple uncertain drivers từ distributions/correlations để tạo valuation distribution.

Nó useful để visualize uncertainty nhưng dễ tạo false sophistication nếu distributions guessed poorly. Model quality vẫn phụ thuộc economics.

## 37. Reverse DCF

Reverse DCF starts current price rồi solve assumptions required to justify it: growth, margin, ROIC.

Question chuyển từ “value bao nhiêu?” thành “market đang price điều gì?”. Đây thường là framing rất powerful.

## 38. Reverse DCF và implied fade

Không chỉ solve revenue CAGR. Hãy solve combinations: terminal margin, reinvestment, ROIC fade và duration of excess returns.

Market price có thể imply moat lasts 15 years rather than 5; đây là expectation more meaningful than simple P/E.

## 39. P/E

P/E useful khi earnings meaningful/stable. Nó mixes operating, financing và tax.

Low P/E có thể signal cyclical peak/distress; high P/E có thể rational if high ROIC/growth persist.

## 40. PEG caution

`PEG = P/E / growth` oversimplifies persistence, margins, ROIC, risk và duration.

Use rough heuristic only.

## 41. EV/EBITDA

EV/EBITDA compares operating value before D&A/financing/tax. Useful across leverage structures but ignores capex/working capital.

Capital-intensive business deserving same EV/EBITDA as asset-light company is not automatic.

## 42. EV/EBIT

EV/EBIT includes depreciation, often more economic when D&A approximates asset consumption.

Acquisition amortization/accounting differences still matter.

## 43. EV/Sales

Useful when profits negative, but sales only valuable if future margins/retention plausible.

Compare gross margin, unit economics and required reinvestment.

## 44. P/B

P/B useful khi book equity links earning assets: banks/insurers/asset-heavy.

Core relation: sustainable ROE relative cost of equity. ROE > COE supports P/B >1 all else equal.

## 45. FCF yield

`FCF Yield = FCF / Equity Value` or enterprise version consistently.

Normalize working capital and growth capex. Temporary inventory liquidation can make FCF yield artificially high.

## 46. Shareholder yield

Dividend + net buyback yield captures distributions better than dividend alone.

Debt-funded distribution or buyback above intrinsic value can destroy value despite high shareholder yield.

## 47. Comparable-company analysis

Peers cần similar growth, margins, ROIC, risk, geography, accounting và business model.

Explain premium/discount, don't just average multiples.

## 48. Historical multiple

Historical range is context, not fair-value law. Rate regime, business maturity, accounting and index composition change.

A company deserves different multiple after moat erosion even if current P/E below 10-year average.

## 49. Sum-of-the-parts

SOTP values segments separately then adjusts corporate debt, tax leakage, holding-company costs and minorities.

Pure-play peer multiples may overstate segments if separation impossible or synergies/corporate costs material.

## 50. NAV valuation

Property/holding companies/investment firms can use Net Asset Value.

Adjust asset values, debt, tax, liquidity discount và realizability. Land book value may not equal realizable value if legal restrictions exist.

## 51. Replacement cost

Commodity/capital-intensive industries sometimes anchor value to replacement cost. If industry trades well above replacement cost, new capacity may enter unless barriers strong.

Useful cycle tool, not universal valuation.

## 52. Liquidation value

Distressed business valuation should haircut receivables, inventory, PPE and deduct wind-down costs/claims.

Book equity can be meaningless if assets hard to monetize.

## 53. Banks: excess return model

For bank, industrial FCFF awkward. Residual-income intuition:

`Value ≈ Book Value + PV[(ROE - Cost of Equity) × Beginning Book Equity]`

Sustainable ROE above COE creates value; growth destroys value if ROE below COE.

## 54. Insurers

Insurance valuation may use P/B, ROE, embedded value or appraisal value depending life/non-life structure.

Reserve adequacy, underwriting profitability, investment duration và capital regulation matter more than simple P/E.

## 55. REITs

Use FFO/AFFO, NAV, cap rates, debt maturity, occupancy và lease growth.

P/E less informative due real-estate depreciation.

## 56. SaaS/growth

Near-term P/E may not meaningful. Focus ARR, retention, gross margin, CAC payback, SBC/dilution and path to FCF.

High growth without strong incremental unit economics should not automatically command premium.

## 57. Commodity producers

Value reserves/resources, cost curve, commodity assumptions, capex, royalties/tax, hedge book và balance sheet.

Do not extrapolate spot far above incentive price forever.

## 58. Early-stage/biotech probability valuation

For binary milestones, use probability-adjusted cash flows/scenarios rather than one deterministic DCF.

Clinical success probabilities, time-to-market, dilution, funding runway and competitive pipeline matter.

## 59. Per-share value

Enterprise can grow while shareholder stagnates if dilution high. Always model diluted shares and potential future issuance.

Per-share compounding is the objective, not revenue empire size.

## 60. Balance-sheet optionality

Net cash provides resilience and ability buy assets/shares during downturn. Heavy debt amplifies equity sensitivity and can force value-destructive refinancing.

Same enterprise value can create very different equity risk.

## 61. Reflexivity

For capital-dependent businesses, market valuation can influence fundamentals. High stock price lowers financing cost; collapsing price may force dilutive issuance.

Banks/property/early growth are especially reflexive.

## 62. Margin of safety

Margin of safety là buffer for assumption/model error, not arbitrary 20% discount.

Need wider buffer when leverage, cyclicality, governance uncertainty or terminal sensitivity high.

## 63. Expected-return range

Project holding-period outcomes:

`Future earnings/FCF × exit valuation + distributions - dilution/other claims`

Then compute CAGR/IRR from today's price across scenarios.

This often helps decision more than a one-year target price.

## 64. Path dependency

Two stocks with same year-5 value can produce different investor experience if one requires repeated dilution, capital calls or survives deep drawdown.

Path matters when leverage, liquidity or investor constraints can force action before terminal value realized.

## 65. Catalyst vs value

Intrinsic value gap can close slowly. Catalyst affects duration/opportunity cost but is not always necessary for long-term compounder.

Event-driven thesis requires much more precise path/timing analysis.

## 66. Value trap diagnostic

Cheap multiple may reflect structural decline, capital misallocation, leverage, governance, technological disruption or peak cyclical earnings.

Ask what must improve for multiple to normalize and whether evidence supports it.

## 67. What is priced in?

Current price implies some combination of growth, margin, ROIC duration, risk and failure probability.

Thesis should be phrased relative expectations: “market prices X, evidence supports Y”, not only absolute forecast.

## 68. Research uncertainty hierarchy

Separate assumptions into high-confidence, medium-confidence và speculative. Revenue volume may be easier than terminal multiple; unit cost may be easier than ten-year market share.

Allocate research effort to high-impact, high-uncertainty assumptions.

## 69. Valuation checklist

Before value: normalize accounting; identify drivers; choose cash flow; model reinvestment; choose consistent discount rate; account taxes/SBC/dilution; build terminal economics; bridge EV-to-equity; scenarios/sensitivity; comparable cross-check; reverse DCF; expected-return range.

Then write what would falsify valuation thesis.

## 70. Mental model cuối cùng

`Operating drivers → normalized cash flow → reinvestment/ROIC → growth fade → risk/discount rate → terminal economics → diluted per-share value → market-implied expectations → expected return`

Valuation là framework ra quyết định dưới uncertainty, không phải target-price manufacture.