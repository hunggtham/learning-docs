# Valuation: DCF, multiples và scenario analysis

> Valuation không phải tìm một “giá đúng” duy nhất. Nó là quá trình chuyển assumptions về cash flow, growth, risk và capital allocation thành range of values, rồi so với expectations embedded trong market price. Precision đến từ hiểu drivers, không từ thêm nhiều decimal places.

## 1. Giá và value khác nhau

Market price là price giao dịch hiện tại. Intrinsic value là estimate của present value cash flows thuộc capital providers/shareholders dưới assumptions.

Price can deviate because expectations, liquidity, flows and risk premia. But intrinsic value itself uncertain because future cash flows unknown.

Therefore use ranges/scenarios, not exact target.

## 2. Expected return perspective

Valuation should also ask prospective return from current price.

A rough equity framework:

`Expected return ≈ earnings/FCF growth + shareholder yield + valuation change`

Company can compound earnings 12% but investor earn less if multiple compresses.

## 3. Present value

Future cash flow discounted:

`PV = CF_t / (1 + r)^t`

Higher discount rate lowers value, especially distant cash flows. This creates “equity duration”: high-growth company whose value lies far future is more rate-sensitive.

## 4. Nominal vs real valuation

Nominal cash flows should be discounted by nominal rate; real cash flows by real rate. Mixing produces inconsistency.

Inflation affects revenue, margin, working capital, capex and discount rates differently. Simply add inflation to growth without cost/reinvestment changes can overvalue.

## 5. Enterprise Value và Equity Value

Enterprise Value represents operating asset value available to debt+equity capital providers. Equity value is residual for common shareholders.

Simplified:

`EV = Market Cap + Debt + Preferred + Minority Interest - Cash/non-operating assets adjustments`

Exact bridge depends company.

## 6. Net debt nuance

Not all cash is excess. Operating cash may be required; restricted cash unavailable. Pension deficits, leases or off-balance obligations may act debt-like.

Non-core investments can be added separately if not reflected operating cash flow.

## 7. FCFF

Free Cash Flow to Firm (*FCFF*) available to all capital providers:

`FCFF = EBIT(1-T) + D&A - Capex - ΔNWC`

Discount FCFF using WACC to get enterprise value.

Forecast should connect revenue/margins/reinvestment to business drivers rather than arbitrary growth rates.

## 8. FCFE

Free Cash Flow to Equity (*FCFE*) is residual after debt-related flows:

`FCFE ≈ Net Income + D&A - Capex - ΔNWC + Net Borrowing`

Discount FCFE at cost of equity to get equity value.

FCFE can be unstable when leverage changes, so FCFF often easier for non-financial firms.

## 9. Why banks need different framework

For banks, debt/deposits are operating raw material, so industrial FCFF concept is awkward. Dividend Discount Model or excess-return/residual-income often more natural.

Valuation connects ROE, book value growth, payout and cost of equity.

## 10. Forecast revenue from drivers

Instead of “revenue +10%”, use:

`Units/customers × price/ARPU × mix`

SaaS: starting ARR + new ARR - churn + expansion. Semis: bit shipments × ASP. Retail: stores × sales/store plus same-store sales.

Driver model makes bull/bear cases causal.

## 11. Margin forecast

Gross margin depends price, mix, input cost, utilization. Operating margin adds scale/R&D/SG&A.

Do not extend peak margin forever without competitive response. Compare history, peers and capacity cycle.

## 12. Reinvestment requirement

Growth requires capital. Sustainable growth links reinvestment and return:

`Growth ≈ Reinvestment Rate × Return on Incremental Capital`

If company grows 20% but incremental ROIC only 5%, it must consume enormous capital. Growth itself isn't value creation unless return exceeds capital cost.

## 13. Working capital in DCF

Growth can absorb cash through receivables/inventory. Model DSO/DIO/DPO or working-capital-to-sales, not ignore it.

Businesses with negative working capital can finance growth via customer/supplier terms; slowing growth can reduce that benefit.

## 14. Capex and depreciation

Separate maintenance and growth conceptually. In steady state, capex cannot remain permanently below economic depreciation if assets wear out.

High-growth infrastructure/semis may require capex far above D&A for years.

## 15. Explicit forecast period

Forecast period should cover transition until business approaches stable economics, not arbitrary 5 years.

High-growth company may require 10–15 years transition assumptions; mature utility shorter.

Longer forecast doesn't mean better if assumptions weak.

## 16. Terminal value

Gordon growth:

`TV = FCF_(n+1) / (WACC - g)`

Terminal value often dominates DCF. Therefore terminal assumptions must be economically consistent: growth cannot exceed economy forever while maintaining unrealistic high ROIC without competition.

## 17. Terminal growth rate

Long-term nominal growth should reflect mature economy/inflation and company competitive position.

Very high terminal `g` near WACC mathematically explodes value. Treat as warning.

## 18. Exit multiple terminal value

Alternative is apply terminal EV/EBITDA or other multiple. This embeds market-comparable assumption at future date.

It does not avoid terminal uncertainty; it simply hides it in multiple. Cross-check Gordon vs exit multiple.

## 19. WACC

Weighted Average Cost of Capital:

`WACC = w_e × Cost of Equity + w_d × After-tax Cost of Debt`

Weights ideally reflect sustainable market-value capital structure.

WACC should match currency and nominal/real framework.

## 20. Cost of equity

CAPM common:

`Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium`

But beta is historical/model-dependent; ERP estimated. CAPM is tool, not truth.

Small/country/company risks may require judgment, but avoid piling arbitrary premiums to force result.

## 21. Risk-free rate

Risk-free rate should match cash-flow currency. KRW cash flows should not casually discount using US Treasury simply because available.

Currency risk and sovereign conditions belong consistently in cash flows/discount rate.

## 22. Cost of debt

Use current marginal borrowing cost, not only historical coupon. For stressed company, market yield can be much higher than book interest rate.

Tax shield only valuable if taxable income exists and rules permit.

## 23. Beta caution

Beta measures covariance with market, not total business risk. Low historical beta can result stale/illiquid prices.

DCF sensitivity should focus key drivers, not false confidence from single beta estimate.

## 24. Sensitivity table

At minimum vary WACC and terminal growth. Better also key operating assumptions: revenue CAGR, margin, reinvestment.

If valuation changes from 50 to 150 with tiny assumption shift, thesis is highly fragile. That is useful information.

## 25. Scenario analysis

Base/bull/bear should have causal stories.

Semiconductor bear: ASP down, utilization low, inventory correction, capex sticky. Bull: supply constrained, HBM mix high, pricing strong.

Do not simply multiply value ±20%.

## 26. Probability weighting

Expected value:

`EV_expected = Σ Probability_i × Value_i`

Probabilities are judgment. Purpose is force explicit downside/upside, not create scientific certainty.

Tail case may deserve separate risk control even low probability.

## 27. Reverse DCF

Reverse DCF starts current price and solves assumptions necessary to justify it: growth, margin, ROIC.

This is often more robust than forecasting distant future because question becomes “what must be true?”

If current price requires 25% revenue CAGR for decade + record margins, margin of safety low.

## 28. P/E

Price/Earnings works when earnings meaningful/stable. It mixes operating and financing/tax effects.

P/E high can be justified by high growth/ROIC/lower risk; low P/E can signal cyclical peak or distress.

Use forward vs trailing carefully; forward estimates can be wrong.

## 29. PEG ratio caution

PEG = P/E / growth. It assumes simplistic linear relationship and ignores duration, margins, ROIC, risk and growth persistence.

Use as rough heuristic only.

## 30. EV/EBITDA

EV/EBITDA compares operating value before D&A/financing/tax. Useful for companies with different debt.

But EBITDA ignores capex and working capital. Capital-intensive company deserves different multiple from asset-light even same EBITDA growth.

## 31. EV/EBIT

EV/EBIT includes depreciation, often better when D&A approximates economic asset consumption.

Still depends accounting depreciation and acquisition amortization.

## 32. EV/Sales

Useful when profits negative, but sales only valuable if future margins plausible.

A 2x sales low-margin retailer and 10x sales high-retention software cannot compare directly.

## 33. P/B

P/B meaningful when book equity relates earning assets—banks, insurers, some asset-heavy.

Core relationship: sustainable ROE vs cost of equity. ROE > COE supports P/B >1; ROE below COE often P/B <1, all else equal.

## 34. FCF yield

`FCF Yield = FCF / Equity Value` (or enterprise variant consistently).

Directly connects cash generation to price, but current FCF may be distorted by working capital or growth capex.

Normalize.

## 35. Dividend yield

Dividend yield ignores retained cash and capital allocation. High yield can signal distress/unsustainable payout.

Total shareholder yield can include net buyback + dividends, but debt-funded distribution may weaken balance sheet.

## 36. Comparable-company analysis

Peers should have comparable growth, margin, ROIC, risk, geography and accounting.

Do not compare Korean memory cyclical to US fabless growth company just because both “semiconductor”.

Explain why premium/discount exists.

## 37. Historical multiple

Historical range provides context but macro/regime may change. P/E 30 during zero rates may not be fair when real yields high.

Business itself can mature, changing warranted multiple.

## 38. Sum-of-the-parts (SOTP)

Conglomerate with distinct businesses may need value segments separately then subtract corporate debt/overheads.

SOTP useful for holding companies but beware assuming each part deserves pure-play multiple without conglomerate costs/taxes.

## 39. Asset/NAV valuation

Property, holding companies, investment firms can use Net Asset Value.

Adjust assets to realistic market value, taxes, debt and liquidity. Book land value may differ market/legal realizability.

## 40. Replacement cost

Commodity/capital-intensive industries sometimes compare EV to replacement cost of capacity. High prices encourage new supply; value cannot stay far above replacement cost forever absent barriers.

Replacement cost is cycle tool, not universal valuation.

## 41. Liquidation value

For distressed/asset-rich business estimate cash recoverable if operations wound down after liabilities, transaction costs and haircuts.

Book value can overstate liquidation if inventory/receivables/PPE difficult to monetize.

## 42. Cyclical valuation

At peak, earnings high make P/E low; at trough, P/E high/negative. Normalize mid-cycle price, volume, margins and utilization.

Use EV/normalized EBITDA, P/B/replacement or through-cycle DCF.

## 43. Banks

Bank valuation: P/B, ROE, cost of equity, growth, asset quality, capital and payout.

High ROE from leverage/underprovision is lower quality.

Residual income/excess return model values future ROE above COE on book capital.

## 44. REITs

Use FFO/AFFO, NAV, cap rates, debt, occupancy and lease growth.

P/E less useful due real-estate depreciation accounting.

## 45. SaaS/growth

Near-term P/E may meaningless. Focus ARR, retention, gross margin, CAC efficiency, SBC/dilution and path to FCF.

High growth without incremental economics should not automatically command premium.

## 46. Commodity producers

Value reserves/resources, cost curve, commodity assumptions, capex, royalties/tax and balance sheet.

Avoid valuing at current spot forever if price far above marginal incentive cost.

## 47. Per-share value

Enterprise can grow while shareholder value stagnates if dilution high. Always model diluted shares.

Acquisition funded by stock may raise total EPS depending accretion math but reduce intrinsic per-share if overpaid.

## 48. Balance-sheet optionality

Net cash gives resilience and capacity buybacks/M&A in downturn. Heavy debt amplifies equity sensitivity.

Same EV can produce radically different equity risk due leverage.

## 49. Reflexivity between price and fundamentals

For companies needing capital, high share price can lower financing cost and fund growth; collapsing price can force dilution/debt stress.

Valuation can influence fundamentals, especially banks/property/early growth.

## 50. Margin of safety

Margin of safety is buffer for assumption error, not arbitrary 20% discount.

Need larger buffer when leverage, cyclicality, governance uncertainty or terminal value sensitivity high.

High-quality predictable firm may justify narrower range but never zero uncertainty.

## 51. Expected-return range

Instead of target only, project 3–5 year scenarios including earnings/FCF, distributions and exit multiple.

Estimate IRR/CAGR from today's price. A stock can be “undervalued” but expected return mediocre if catalyst/time horizon distant.

## 52. Catalyst vs value

Intrinsic value doesn't require immediate catalyst for long-term investor, but catalyst affects duration and opportunity cost.

For event-driven thesis, timing matters more. Distinguish valuation gap from event path.

## 53. What is priced in?

Ask: current multiple implies what revenue growth, terminal margin, ROIC and failure probability?

Thesis is not “I forecast growth 20%”; it is “market appears to price 12%, and evidence supports higher sustainable growth”.

## 54. Valuation checklist

Before value: normalize accounting; identify business drivers; choose cash flow; choose consistent discount rate; model reinvestment; terminal assumptions; diluted shares; balance-sheet claims; scenarios; sensitivity; compare multiples; reverse DCF.

Then write what would make valuation wrong.

## 55. Mental model cuối cùng

`Operating drivers → normalized cash flow → reinvestment/ROIC → risk/discount rate → terminal economics → per-share value → market-implied expectations → expected return`

Valuation is a decision framework under uncertainty, not target-price manufacture.