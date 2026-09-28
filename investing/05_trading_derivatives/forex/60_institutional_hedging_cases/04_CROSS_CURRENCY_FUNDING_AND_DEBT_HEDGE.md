# Case 04 — Cross-Currency Funding: Debt, FX Swap và Basis Risk

Một company hoặc financial institution có thể huy động vốn ở currency A nhưng thực sự cần economic funding ở currency B. Khi đó FX derivatives không chỉ hedge price risk; chúng **biến đổi currency của liabilities và funding cash flows**.

Mental model:

```text
Debt raised in Currency A
+ FX / Cross-Currency Hedge
→ Synthetic Funding in Currency B
```

Điểm quan trọng là so **all-in synthetic funding cost** với direct funding, đồng thời tính collateral, rollover, basis, counterparty và liquidity risk.

## 1. Business problem

Giả sử Korean company cần equivalent:

```text
USD 100m funding
for 3 years
```

Nhưng company có thể phát hành KRW bonds với investor demand tốt hơn.

Two alternatives:

```text
A. Borrow USD directly
B. Borrow KRW, then swap KRW funding into USD
```

Choice không nên dựa chỉ vào headline coupon.

## 2. Direct USD borrowing

Suppose:

```text
USD debt principal = 100m
USD interest = SOFR + credit spread
```

Company has direct USD liability.

If business cash flows are in USD, this may naturally match funding need.

## 3. KRW borrowing route

Company issues KRW debt:

```text
KRW principal equivalent to USD 100m
KRW coupon/floating cost
```

But project needs USD cash.

At inception, company can swap KRW into USD.

## 4. Cross-currency swap concept

A cross-currency swap may exchange:

```text
Principal at start
Periodic interest cash flows
Principal back at maturity
```

in two currencies.

Simplified:

```text
Company pays USD leg
Company receives KRW leg
```

so KRW debt service is economically offset while company bears synthetic USD funding.

Exact convention depends on contract.

## 5. Why not just spot-convert KRW into USD?

If company sells KRW for USD at inception but keeps unhedged KRW debt:

```text
Assets/use of funds = USD
Liability = KRW
```

Future principal repayment creates FX mismatch.

Cross-currency hedge transforms future cash flows too.

## 6. Synthetic funding cost

All-in synthetic USD funding roughly reflects:

```text
KRW borrowing cost
+ cross-currency swap/basis economics
+ transaction/credit/collateral cost
```

Not simply KRW coupon translated at spot.

## 7. Covered interest parity intuition

In frictionless world, FX forward/swaps align currency funding returns.

If synthetic USD were persistently much cheaper than direct USD with no constraints:

```text
arbitrage demand should compress gap
```

Real markets have balance-sheet, collateral, regulatory and credit frictions.

## 8. Cross-currency basis

Basis represents deviation/adjustment needed beyond simple interest differential in swap pricing.

It can reflect:

```text
relative demand for currency funding
dealer balance-sheet cost
collateral terms
credit/regulatory constraints
market segmentation
```

Basis is economics, not automatically arbitrage profit.

## 9. Funding currency vs reporting currency

Company may report in KRW but project cash flow in USD.

Best liability currency depends on economic matching, not reporting currency alone.

Questions:

```text
Where does revenue arrive?
Where are costs paid?
What currency services debt?
What happens under stress?
```

## 10. Natural hedge through revenue

If project generates stable USD revenue:

```text
USD debt
→ paid from USD revenue
```

can reduce transaction FX risk.

But if revenue is only partially USD or cyclical, mismatch remains.

## 11. Example capital structure

Suppose:

```text
KRW bond proceeds = 136bn KRW
Spot USD/KRW = 1,360
USD received through swap ≈ 100m USD
Tenor = 3 years
```

Cross-currency swap maps KRW debt cash flows into agreed USD cash flows.

## 12. Do not use spot movement to judge swap alone

If USD/KRW rises sharply, mark-to-market of swap can move significantly.

But company also has debt/assets whose economic values move.

Evaluate combined funding package.

## 13. Mark-to-market vs cash-flow objective

Treasury may intend to hold swap to maturity.

Still, mark-to-market matters for:

```text
collateral
credit limits
accounting/reporting
termination cost
```

Economic cash-flow hedge can create interim liquidity needs.

## 14. Collateral mechanics

Under collateral agreement, adverse swap MTM can require cash/securities.

This creates:

```text
market move
→ collateral call
→ liquidity need
```

Even if final maturity cash flows remain economically matched.

## 15. Wrong-way liquidity risk

Stress can produce:

```text
business cash flow weakens
+ swap collateral call increases
+ funding markets tighten
```

Treasury must stress combined liquidity, not each item separately.

## 16. Counterparty credit risk

OTC cross-currency swap exposes company to bank/dealer counterparty.

Risk management includes:

```text
legal agreement
netting
collateral
counterparty limits
replacement cost
```

A 3-year hedge has longer counterparty horizon than 1-month forward.

## 17. Replacement risk

If counterparty defaults when swap is valuable to company:

```text
company must replace hedge at current market rate
```

Replacement cost can be material.

## 18. Maturity mismatch

Suppose debt is 5 years but hedge is 3 years.

At year 3:

```text
hedge expires
2 years debt remain
```

Company faces roll/refinancing risk for hedge.

## 19. Rollover basis risk

Future swap basis may be very different.

A strategy that looks cheap today because 3-year basis is favorable may become expensive when rolled.

## 20. Debt refinancing risk

Even with 5-year hedge matching 5-year debt, company may refinance debt early or repay early.

If hedge remains:

```text
orphan derivative exposure
```

must be closed/restructured.

## 21. Call/put features in debt

Callable debt or prepayment optionality creates uncertain liability horizon.

Fixed hedge maturity can become mismatched.

Instrument optionality and hedge optionality should be considered together.

## 22. Floating vs fixed legs

Cross-currency swap can exchange:

```text
fixed vs fixed
fixed vs floating
floating vs floating
```

Funding transformation includes both:

```text
currency risk
and
interest-rate risk
```

Do not discuss currency leg while ignoring rate reset structure.

## 23. Interest-rate swap combination

Treasury may use multiple derivatives:

```text
Cross-currency swap
+ interest-rate swap
```

or one structure that transforms both currency and rate basis.

Risk system should consolidate sensitivities.

## 24. DV01 and FX delta

Funding hedge can carry:

```text
FX delta
interest-rate DV01 by currency
basis sensitivity
```

A “currency hedge” can still have substantial rates/basis risk.

## 25. Basis sensitivity

If cross-currency basis widens, swap MTM changes even if spot FX stays unchanged.

This is why funding hedge cannot be monitored by spot chart alone.

## 26. NDF/funding limitation

NDF hedges exchange-rate settlement but does not necessarily provide physical currency funding.

If company needs actual USD cash:

```text
NDF P/L
≠ USD funding itself
```

This distinction is critical in restricted/onshore-offshore markets.

## 27. FX swap for short-term funding

For shorter horizon, institution can use FX swap:

```text
Near leg: obtain USD now
Far leg: return USD / receive KRW later
```

This transforms temporary liquidity.

## 28. FX swap rollover

Rolling overnight/1m/3m funding creates maturity mismatch if underlying asset is long-term.

```text
long asset
funded by short FX swaps
```

can be vulnerable to rollover freeze.

## 29. 2020 lesson

Global USD funding stress showed that:

```text
USD availability
and
cross-currency funding cost
```

can change rapidly under system stress.

A normal-times synthetic funding advantage may disappear when needed most.

## 30. Reserve/corporate distinction

Central-bank swap lines can improve system USD liquidity, but private company access is indirect through domestic financial system and program rules.

Do not assume central-bank facility guarantees company funding.

## 31. All-in funding comparison

Create matrix:

```text
Direct USD debt
KRW debt + CCS
KRW debt + rolling FX swaps
Other market route
```

Compare:

```text
coupon/reference rate
credit spread
basis
transaction cost
collateral liquidity
roll risk
counterparty risk
market-access risk
```

## 32. Cheap funding can be compensation for hidden risk

If rolling short-dated swaps looks cheaper than 5-year fixed CCS:

```text
lower current cost
may reflect taking future rollover/basis risk
```

Do not compare expected cost without risk horizon.

## 33. Term funding premium

Longer hedge tenor often embeds liquidity/credit/basis conditions for longer horizon.

Paying more can buy certainty.

Treasury choice is risk allocation, not only price optimization.

## 34. Liquidity stress scenario

Assume:

```text
USD/KRW +15%
Cross-currency basis moves adversely
USD funding spread +200 bp
Collateral call = 10m USD
New FX-swap tenor available only 1 month
```

Calculate whether company can meet:

```text
collateral
interest
principal/roll needs
```

## 35. Revenue shock scenario

USD project revenue falls 40% while USD debt service unchanged.

Natural hedge deteriorates.

Currency-matched debt does not remove business-volume risk.

## 36. Early termination scenario

Project is sold after 18 months.

Debt prepaid, but 3-year cross-currency swap remains.

Need compute termination value and liquidity impact.

## 37. Counterparty failure scenario

Bank counterparty defaults when hedge is positive MTM to company.

Company must replace at stressed market terms.

Stress:

```text
replacement spread
basis
legal closeout delay
```

## 38. Multi-counterparty strategy

Splitting hedge among banks can reduce concentration but increases:

```text
legal documentation
operational complexity
netting fragmentation
```

Diversification has cost.

## 39. Collateral currency

Collateral posted in different currency can itself create FX/funding need.

CSA terms are part of economics.

## 40. Hedge accounting boundary

Accounting designation can affect P&L presentation, but economic hedge should first be understood as cash-flow/balance-sheet transformation.

Professional implementation requires current accounting and legal review separately.

## 41. Regulatory/access boundary

Cross-border derivatives access depends on:

```text
entity type
jurisdiction
product
reporting
collateral/legal framework
```

Korea/Vietnam-specific rules should be verified from current official sources before real use.

## 42. Funding attribution

Treasury should decompose:

```text
Base borrowing cost
Credit spread
Cross-currency basis
Hedge execution cost
Collateral funding cost
Roll cost
Early termination cost
```

Without decomposition, “synthetic USD cost” is opaque.

## 43. Performance vs risk objective

A funding hedge can look expensive ex post if currency moved favorably.

But objective may be:

```text
ensure debt-service capacity
and remove FX mismatch
```

Evaluate against risk objective, not hindsight spot rate.

## 44. Balance-sheet exposure map

Create:

```text
Assets by currency
Revenue by currency
Operating costs by currency
Debt by currency
Derivative legs
Collateral currency
Liquidity reserves
Maturity buckets
```

This map should precede derivative choice.

## 45. Maturity ladder

Bucket:

```text
0–1m
1–3m
3–12m
1–3y
3y+
```

for debt, derivatives and expected cash flows.

Funding risk often hides in maturity mismatch rather than net currency exposure.

## 46. Sensitivity dashboard

Monitor:

```text
FX delta by currency
Rate DV01 by currency
Cross-currency basis sensitivity
Collateral requirement
Counterparty exposure
Refinancing amount by horizon
```

## 47. What not to learn

Wrong:

```text
Borrow wherever coupon is lowest.
```

Wrong:

```text
Cross-currency swap eliminates funding risk.
```

Wrong:

```text
NDF is equivalent to physical USD funding.
```

Better:

```text
Compare all-in synthetic funding cost together with
basis, collateral, rollover, counterparty and maturity risk.
```

## 48. Case outputs

Create:

```text
funding_currency_map.md
asset_liability_maturity_ladder.md
direct_vs_synthetic_funding_matrix.md
cross_currency_swap_cashflow_map.md
basis_collateral_stress_test.md
counterparty_limit_report.md
funding_cost_attribution.md
```

## 49. Review questions

Explain:

1. Why debt currency should be compared with cash-flow currency.
2. Why spot conversion alone does not hedge future liability cash flows.
3. Why cross-currency basis enters synthetic funding cost.
4. Why economically hedged swap can still create collateral liquidity stress.
5. Why short FX-swap funding against long assets creates rollover risk.
6. Why NDF hedge is not physical funding.
7. Why all-in funding cost must include hidden risk, not coupon only.

## Internal links

- [Funding, NDF, basis and forward curve](../90_connections/00_FX_FUNDING_NDF_BASIS_AND_FORWARD_CURVE.md)
- [2020 global USD funding stress](../80_case_studies/04_GLOBAL_USD_FUNDING_STRESS_2020.md)
- [Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
