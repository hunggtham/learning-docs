# Derivatives — Futures, Options, Swaps, CFD và Hedging

> Derivative là contract whose value depends on an underlying hoặc một risk factor. Nó cho phép transfer risk, tạo exposure capital-efficient hoặc hedge existing positions. Nhưng leverage, margin, collateral, basis, optionality và counterparty mechanics khiến derivative risk khác cash assets. Chapter này xây nền **contract-level** trước khi sang options/volatility chuyên sâu.

## 1. Derivative không đồng nghĩa Ownership

Mua stock thường tạo residual ownership. Futures, forwards, options, swaps và CFD tạo contractual exposure.

Vì vậy investor phải hiểu legal rights, notional, settlement, margin, collateral, expiry, exercise, financing và counterparty. Price direction chỉ là một layer.

## 2. Derivative tồn tại để Transfer Risk

Farmer hedge crop price; airline hedge fuel; exporter hedge FX; pension fund hedge duration; market maker intermediate order flow.

Speculator nhận risk vì kỳ vọng compensation. Derivatives không tạo risk từ hư không nhưng leverage và interconnected collateral can amplify systemic consequences.

## 3. Underlying và Reference Rate

Underlying có thể là equity, index, bond, rate, FX, commodity, credit event hoặc volatility.

Một contract có thể reference price nhưng settle cash rather than deliver asset. Luôn phân biệt **reference exposure** và **legal deliverable**.

## 4. Notional vs Market Value

Notional measures economic scale; market value là current contract value.

Futures notional:

```text
Notional = Futures Price × Contract Multiplier
```

Margin 5% không nghĩa risk = 5%. Market risk gần notional sensitivity.

## 5. Gross Notional và Net Exposure

Portfolio có thể có gross notional rất lớn nhưng net directional exposure nhỏ nếu offsetting positions.

Gross vẫn matter cho liquidity, counterparty, margin và basis risk. Net-only view có thể hide operational leverage.

# Phần I — Forwards và Futures

## 6. Forward

Forward là customized OTC agreement exchange asset/currency at future date at price agreed now.

Customization useful nhưng creates bilateral counterparty/legal risk. Professional market thường dùng master agreements và collateralization.

## 7. Futures

Futures standardized bởi exchange và centrally cleared. Contract size, tick, expiry, trading hours và settlement rules predefined.

Standardization improves liquidity nhưng hedge may imperfect if timing/grade/location không match actual exposure.

## 8. Tick Size và Tick Value

Tick size là minimum quote increment; tick value = tick size × multiplier.

Trader phải convert points/ticks thành currency loss before choosing position size.

## 9. Initial Margin

Initial margin là collateral to open/maintain exposure, không phải purchase price.

Exchange/broker can raise margin when volatility rises. Therefore leverage available thường giảm đúng lúc market stressed.

## 10. Maintenance Margin

If account equity falls below maintenance threshold, participant may need add funds or face liquidation.

Path matters: position can ultimately recover but trader may be liquidated before recovery.

## 11. Variation Margin

Futures are marked to market. Gains/losses settled periodically, usually daily and sometimes intraday depending system.

This reduces accumulated counterparty exposure but creates liquidity need. A profitable long-term hedge can still require cash during adverse interim moves.

## 12. Margin Buffer

Professional risk management separates required margin from **liquidity buffer**.

Using nearly all available margin leaves no room for volatility-driven requirement increase. Safe leverage should survive stress, not normal-day requirement.

## 13. Futures Fair Value

For financial assets:

```text
Futures ≈ Spot + Financing Carry - Income / Benefits
```

Exact relation depends dividends, borrow, rates and time. Fair value changes when expected dividends/funding change.

## 14. Basis

Basis is futures relative to spot/reference price. Hedger may be correct on underlying but lose due basis change.

Basis risk appears in index composition, commodity grade/location, bond cheapest-to-deliver and cross-hedges.

## 15. Convergence

As expiry approaches, futures converges toward settlement reference under arbitrage and contract rules.

Understanding convergence prevents confusing normal carry/basis with mispricing.

## 16. Contango và Backwardation

Commodity term structure reflects storage, financing, inventory scarcity, seasonality and convenience yield.

Contango/backwardation are curve states, not automatically bearish/bullish signals.

## 17. Roll Yield

Continuous exposure requires selling expiring contract and buying next one.

Total return roughly includes:

```text
Spot / Reference Move
+ Roll Effect
+ Collateral Return
- Trading Costs
```

Commodity fund return can diverge materially from spot headline.

## 18. Calendar Spread

Long one expiry/short another expresses relative curve view.

Spread can be driven by inventory, storage constraints, seasonality and supply disruption even when outright price stable.

## 19. Open Interest

Open interest measures outstanding contracts; volume measures transactions during period.

Price/OI combinations offer positioning context but not deterministic forecasts.

## 20. Physical Delivery

Some futures permit delivery. Key dates include first notice day, last trading day and delivery period.

Retail trader should know broker auto-close policy. “Tôi sẽ đóng trước expiry” is not operational plan without dates.

## 21. Cash Settlement

Index/rate contracts often settle against specified index/fixing. Settlement methodology can create basis around expiry.

Know whether final price uses close, auction, average or other reference.

## 22. Cheapest-to-Deliver

Bond futures often allow delivery of multiple eligible bonds. Short chooses **cheapest-to-deliver (CTD)** after conversion factors.

This creates basis and delivery-option complexity. Hedging Treasury duration with futures requires understanding CTD/DV01, not only contract notional.

## 23. Futures Curve Positioning

Front-month exposure, deferred-month exposure and calendar spreads can behave differently under same macro thesis.

A commodity supply shock may steepen backwardation rather than move all contracts equally.

# Phần II — Options Core

## 24. Option là State-Contingent Contract

Call gives right to buy; put gives right to sell at strike under terms. Buyer pays premium; seller assumes obligation.

Payoff depends not only direction but timing, magnitude and volatility.

## 25. Intrinsic và Extrinsic Value

```text
Call Intrinsic = max(S-K,0)
Put Intrinsic  = max(K-S,0)
```

Extrinsic value reflects time, IV, rates, dividends/borrow and supply-demand.

## 26. ITM / ATM / OTM

Moneyness describes relation between spot/forward and strike, not profitability after premium.

An option can expire ITM but still generate negative return to buyer.

## 27. Exercise Style

American options may exercise early; European only at expiry. Other contracts may have custom Bermudan-style dates.

Early exercise depends dividends, rates and remaining time value.

## 28. Assignment

Short option can be assigned. Assignment can create unexpected stock/cash obligations.

Understand broker cutoffs, settlement and ex-dividend risk.

## 29. Put-Call Parity

Under simplifying assumptions:

```text
Call - Put ≈ Spot - PV(Strike)
```

Parity explains synthetic forwards and arbitrage relations.

## 30. Greeks as Local Sensitivities

Delta, Gamma, Theta, Vega and Rho summarize local risk. They are not full scenario analysis for jumps or large moves.

A delta-neutral book can still be massively short gamma/vega.

## 31. Implied Volatility

IV is model input consistent with market price, not guaranteed future realized volatility.

Option decision should compare **priced distribution** with your expected distribution, not direction alone.

## 32. Event Volatility

Earnings/CPI/FOMC can elevate short-dated IV. After event, IV often collapses.

Long call can lose despite stock rising if move smaller than market priced.

## 33. Option Structures

Vertical spreads, straddles, strangles, collars and covered calls reshape payoff.

Structure does not create edge by itself. It only chooses which states you buy/sell.

## 34. Short-Volatility Risk

Selling options often produces frequent small gains and rare large losses.

High win rate is not proof of positive expectancy. Margin requirement can expand during same crash that creates mark-to-market loss.

## 35. Defined Risk vs Realized Risk

A vertical spread may have contractual max loss, but execution/assignment/early-close path can still create temporary margin or liquidity issues.

Know broker treatment rather than relying on expiry payoff diagram only.

# Phần III — Swaps

## 36. Swap là Exchange of Cash-Flow Rules

Swap counterparties exchange cash flows according formula, usually on notional that may never be exchanged directly.

Main categories include interest-rate, FX/cross-currency, total-return and credit swaps.

## 37. Interest-Rate Swap

Plain-vanilla IRS commonly exchanges fixed rate for floating reference.

Pay-fixed/receive-floating generally reduces duration; receive-fixed/pay-floating increases duration, all else equal.

## 38. Swap Curve

Swap rates form term structure distinct from government bond curve.

Swap spread versus government yields reflects credit, collateral, supply-demand and balance-sheet technicals.

## 39. DV01 of Swaps

Swap risk should be measured by DV01/key-rate sensitivities, not notional.

Long-maturity swap can carry much more rate risk per unit notional than short swap.

## 40. Overnight Indexed Swap

OIS references overnight rate compounded over period. OIS curve is important for policy expectations and collateralized discounting in many markets.

Central-bank meeting pricing is often inferred from short OIS/futures structures.

## 41. FX Swap

FX swap exchanges currencies spot and reverses at forward date. It is major short-term funding tool, not same as directional FX spot trade.

Funding stress can appear in swap points/basis.

## 42. Cross-Currency Swap

Cross-currency swap exchanges cash flows/principal in different currencies, allowing institutions hedge long-term FX + rate mismatch.

Cross-currency basis deviates from textbook parity when balance-sheet/funding constraints matter.

## 43. Total Return Swap

TRS transfers total economic return of asset/index without direct ownership.

Receiver gets price + income return and pays financing/spread. TRS creates leverage, counterparty exposure and sometimes opacity about economic ownership.

# Phần IV — Credit Derivatives

## 44. Credit Default Swap

CDS protection buyer pays periodic premium; seller compensates upon defined credit event.

CDS spread is market price of protection, not pure default probability. Recovery, liquidity and risk premium matter.

## 45. CDS Notional và Jump-to-Default

Credit book may look low-vol until default event causes sudden loss.

**Jump-to-default** risk should be stressed independently of daily spread volatility.

## 46. CDS Basis

Cash bond spread and CDS spread can diverge due funding, liquidity, deliverability and technical demand.

Basis trade has convergence/counterparty/funding risk; not arbitrage-free in real world.

## 47. Credit Index Derivatives

CDS indices allow hedge/bet on basket credit more liquidly than many single-name bonds.

They reduce idiosyncratic exposure but introduce index composition/basis vs actual portfolio.

# Phần V — Volatility and Other Institutional Derivatives

## 48. Variance Swap Intuition

Variance swaps exchange realized variance vs fixed variance strike.

They provide more direct volatility exposure than options but have nonlinear tail economics and OTC collateral complexity.

## 49. Volatility as an Underlying Risk Factor

Volatility can itself carry risk premium. Short-vol strategies earn premium in calm periods but are exposed to convex crisis loss.

Portfolio factor mapping should include vol exposure, not only delta/beta.

# Phần VI — CFD và Leveraged OTC Products

## 50. CFD Mechanics

CFD is bilateral contract with broker on price change. Client usually does not own underlying.

Costs include spread, commission, financing, dividend adjustments and potential conversion fees.

## 51. Overnight Financing

CFD held for long periods can accumulate significant financing. Directional thesis may be right but economics poor after carry.

Compare CFD with futures/cash asset before choosing implementation.

## 52. Broker Counterparty

Legal entity, regulator, client-money treatment, execution policy and withdrawal process matter.

“ECN/STP” marketing language does not replace legal/execution due diligence.

## 53. Stop-Out Mechanics

Broker can liquidate positions when margin level breaches rule. Liquidation may occur at unfavorable price and order sequence.

Know formula, threshold and whether protection against negative balance applies under your entity.

# Phần VII — Collateral và Counterparty Risk

## 54. Central Clearing

CCP interposes between buyers/sellers, reducing bilateral complexity through margining/netting.

But risk becomes concentrated in clearing ecosystem; participant still faces broker/clearing-member operational risk.

## 55. Bilateral OTC Exposure

Non-cleared OTC trades depend master agreement, collateral annex, netting and counterparty limits.

Legal documentation is part of economic risk.

## 56. Collateral

Collateral reduces unsecured exposure but creates liquidity requirement.

When volatility rises, variation margin/haircuts can increase, forcing cash raising and asset sales.

## 57. Initial vs Variation Margin

Initial margin protects against future liquidation gap after default; variation margin settles current mark-to-market.

Both consume liquidity but serve different purposes.

## 58. Netting

Close-out netting offsets positive and negative positions with same counterparty after default where legally enforceable.

Gross derivative notionals can be huge while net current exposure much smaller, but legal enforceability is crucial.

## 59. Wrong-Way Risk

Wrong-way risk occurs when counterparty quality worsens exactly when exposure to it increases.

Example: buying crisis protection from institution highly exposed to same crisis.

## 60. Collateral Currency Mismatch

Derivative P/L may be in one currency while eligible collateral/liquidity sits in another.

FX move can therefore create margin stress beyond market thesis.

# Phần VIII — Hedging

## 61. Hedge Objective trước Instrument

Define objective: reduce beta, duration, FX, commodity input, tail drawdown or liability mismatch.

A hedge cannot be evaluated without objective.

## 62. Equity Beta Hedge

```text
Contracts ≈ Portfolio Value × Beta / Futures Notional
```

Beta instability and composition mismatch create residual risk.

## 63. Duration Hedge

Match DV01/key-rate DV01 using futures/swaps rather than nominal.

Curve twists can leave residual risk even if total duration matched.

## 64. FX Hedge

Forward/futures hedge foreign asset currency. Return impact includes rate differential, basis and transaction cost.

Hedge ratio should connect to liability currency, not only FX forecast.

## 65. Commodity Hedge

Producer short futures; consumer long futures. Grade/location/timing mismatch creates basis risk.

Hedging crude for jet fuel leaves crack-spread risk.

## 66. Cross-Hedge

If direct instrument unavailable, correlated proxy can be used. Effectiveness depends relationship stability.

Crisis correlation breakdown can make cross-hedge fail exactly when needed.

## 67. Hedge Slippage

Hedge ratio is only theoretical until executed. Spread, impact, roll and rebalancing alter realized protection.

Hedge cost attribution should separate market and implementation.

## 68. Over-Hedging

Hedge larger than underlying exposure creates net speculative position.

As underlying size/beta changes, hedge should be recalibrated or deliberately left with known residual.

# Phần IX — Portfolio Risk và Lifecycle

## 69. Aggregate Sensitivities

Derivative book nên aggregate:

```text
Delta-equivalent notional
Gamma
Vega
DV01 / Key-rate DV01
FX notionals
Credit spread DV01
Jump-to-default
Margin requirement
```

Ticket count is meaningless if many contracts share same factor.

## 70. Gross vs Net Derivative Exposure

Low net delta with huge gross options positions can still have large gamma/vega/liquidity risk.

Report both net and gross dimensions.

## 71. Basis Book

Maintain map of direct exposure vs hedge instrument, expected relationship and failure scenario.

Basis is a position; it should have risk limit.

## 72. Expiry Calendar

Concentrated expiries create roll/settlement risk. Maintain calendar of last trade, notice, exercise and corporate-action dates.

Operational discipline prevents avoidable losses.

## 73. Corporate Actions

Equity derivative strikes/multipliers/deliverables may adjust after split, special dividend, merger or spin-off.

Read exchange notice; do not assume contract unchanged.

## 74. Roll Management

Rolling contracts means close old + open new. Track spread, liquidity, carry and tax/account effects.

Roll should be planned before liquidity migrates away from expiring contract.

## 75. P/L Attribution

Derivative P/L should separate:

```text
Underlying Move
Carry / Roll
Volatility
Rates
Basis
Financing
FX
Execution
```

Without attribution, strategy improvement becomes guesswork.

## 76. Scenario-Based Position Sizing

Never size by margin posted. Size by plausible adverse P/L and liquidity/margin consequences.

If one contract can lose 1,000 under normal stress while budget is 200, contract is too large regardless of 100 margin.

## 77. Margin Stress Test

Stress both price and requirement increase. Example price loss consumes 30% buffer while exchange doubles initial margin.

A strategy can survive P/L but fail funding.

## 78. Liquidity Stress

Quoted spread/depth can vanish around events or limit moves.

Stress wider spread, partial fills and inability to close all positions simultaneously.

## 79. Counterparty Stress

Ask what happens if broker/issuer becomes unavailable while market moves. Keep records, backup liquidity and avoid concentration where possible.

## 80. Tax / Regulatory / Account Layer

Eligibility, taxation, reporting and margin rules vary by jurisdiction/account and change over time.

Permanent notes explain concepts; real-money use requires current verification.

## 81. Contract-Spec Checklist

Before trade know: underlying, notional, multiplier, tick, hours, expiry, settlement, margin, price limits, exercise, assignment, corporate-action treatment, financing, tax, legal counterparty and worst-case path.

Unknown specification = no trade.

## 82. Mental Model cuối cùng

```text
Underlying Risk
→ Contract Payoff
→ Notional / Sensitivities
→ Carry / Basis / Roll
→ Margin / Collateral
→ Liquidity / Expiry
→ Counterparty / Settlement
→ Hedge / Portfolio Interaction
→ Stress / Attribution
```

Derivative sophistication không nằm ở dùng cấu trúc phức tạp. Nó nằm ở việc hiểu đầy đủ lifecycle của contract và biết risk nào đang được transfer, leverage hoặc giữ lại.