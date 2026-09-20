# Derivatives — Futures, Options, Swaps, CFD và hedging

> Derivative là contract whose value depends on an underlying. Nó có thể dùng để hedge, tạo exposure hiệu quả hoặc speculate, nhưng leverage, margin, collateral và nonlinear payoff khiến risk khác cash assets. Chapter này xây nền tảng rộng trước khi sang file options/volatility chuyên sâu.

## 1. Derivative không đồng nghĩa ownership

Mua common stock thường tạo ownership/residual claim. Futures, options, forwards, swaps hay CFD chủ yếu tạo contractual exposure.

Điều này thay đổi legal rights, margin, counterparty, settlement và cash-flow timing. Trước trade phải biết underlying, contract type, notional, multiplier, expiry, settlement, margin, financing, collateral và worst-case path.

## 2. Derivative tồn tại vì transfer risk

Derivative cho phép một participant chuyển risk cho participant khác. Farmer có thể hedge crop price; airline hedge fuel; importer hedge FX; fund hedge beta/duration.

Speculator nhận risk vì kỳ vọng được compensated. Market maker intermediate flow và hedge residual exposure. Derivative không tạo risk từ hư không; nó repackage và redistribute risk, dù leverage có thể amplify system exposure.

## 3. Forward

Forward là OTC agreement mua/bán underlying ở future date với price fixed today. Terms customizable nhưng counterparty risk lớn hơn standardized exchange futures.

Professional forwards thường operate under master agreements và collateral terms. Retail FX forward-like products có thể được embedded trong broker structure.

## 4. Futures

Futures standardized bởi exchange: contract size, tick, expiry và settlement rules cố định. Clearing house đứng giữa participants và mark-to-market P/L thường xuyên.

Standardization tăng liquidity nhưng tạo basis/roll requirement nếu exact underlying/timing của hedge khác contract.

## 5. Notional value

`Notional = Futures Price × Contract Multiplier`

Margin posted không phải position size. Contract margin 5% của notional vẫn expose trader gần 100% notional price movement.

Risk calculations phải bắt đầu từ notional/sensitivity, không từ margin deposit.

## 6. Tick size và tick value

Tick size là minimum quoted price change. Tick value = tick size × contract multiplier.

Nếu tick 0,25 và multiplier 50, one tick = 12,5 currency units.

Stop measured in points/ticks chỉ meaningful khi convert thành money risk.

## 7. Initial margin và maintenance margin

Initial margin là collateral needed open/maintain position. Maintenance margin là minimum threshold.

Exchange/clearing/broker có thể raise margin khi volatility tăng. Margin requirement itself therefore procyclical: risk capital demanded nhiều nhất lúc market stressed.

## 8. Variation margin và path dependence

Futures gains/losses marked to market. Intermediate losses reduce account equity even if contract later recovers.

Trader có thể bị liquidated before thesis ultimately proves right. Đây là path risk unique to leveraged marked-to-market instruments.

## 9. Margin waterfall

Risk process có nhiều layers: customer margin, broker capital, clearing member resources, clearing house default fund và other protections depending market.

Retail trader không cần memorize legal waterfall, nhưng nên hiểu broker failure/clearing stress là separate risk layer beyond market P/L.

## 10. Futures fair value và carry

Financial futures fair-value intuition:

`Futures ≈ Spot + financing/carry - distributions/benefits`

Exact formula depends compounding, dividends, borrow cost và time. Basis changes khi expected dividends, funding hoặc borrow availability change.

## 11. Basis

Basis = futures price relative spot/reference asset. Hedger can be right on underlying but hedge imperfect because basis moves.

Basis risk is central across commodity grade/location, bond cheapest-to-deliver, FX forward points và index composition differences.

## 12. Convergence near expiry

Near expiry, futures và settlement reference should converge under contract rules/arbitrage. Before expiry, basis can vary substantially.

Understanding convergence prevents mistaking normal carry for mispricing.

## 13. Cash vs physical settlement

Index contracts thường cash-settled. Commodity contracts may allow/require physical delivery.

Know first notice day, last trading day, delivery rules và broker forced-liquidation policy. Holding deliverable futures too near expiry without understanding can create operational disaster.

## 14. Commodity term structure

Commodity futures curve reflects storage, financing, inventories, seasonality và convenience yield.

Contango/backwardation are not simple bullish/bearish labels. Curve shape changes with scarcity and logistics.

## 15. Roll yield

Continuous exposure requires rolling expiries. In contango, buying more-expensive next contract can drag return. In backwardation, roll may help.

Total futures return includes spot/reference move, roll, collateral return and sometimes active contract-selection effects.

## 16. Calendar spreads

Calendar spread long one expiry/short another expresses curve view rather than pure directional view.

It is sensitive to inventory, storage, seasonality and temporary bottlenecks. Spread can gap sharply even when outright commodity price moves little.

## 17. Open interest

Open interest is outstanding contracts; volume is traded contracts during period. Rising price + rising OI can indicate new positions entering, but interpretation is not deterministic.

OI is positioning context, not a direct forecast.

## 18. Options: quyền và nghĩa vụ

Call buyer has right to buy at strike; put buyer right to sell. Buyer pays premium; seller accepts obligation under contract rules.

Standalone long option usually limits loss to premium. Short options can create much larger losses and margin expansion.

## 19. Strike, expiry và moneyness

ITM/ATM/OTM describe spot vs strike relationship, not trade profitability after premium.

A call can finish ITM but still produce loss if intrinsic value below premium paid.

## 20. Intrinsic và extrinsic value

Call intrinsic = `max(S-K,0)`; put intrinsic = `max(K-S,0)`.

Extrinsic value reflects time, implied volatility, rates, dividends/borrow and supply-demand. It decays to zero by expiry, but nonlinear.

## 21. American vs European exercise

American-style generally can exercise before expiry; European only at expiry. Early exercise decision depends remaining time value, dividends, rates và borrow.

Short sellers must understand assignment risk, particularly around ex-dividend dates.

## 22. Put-call parity

Under simplifying assumptions:

`Call - Put ≈ Spot - PV(Strike)`

Adjust for dividends/carry. Parity connects options, underlying và financing and explains synthetic positions.

## 23. Greeks

Delta, Gamma, Theta, Vega và Rho describe local sensitivities.

Portfolio delta-neutral can still be massively short gamma/vega. Greeks are not full scenario P/L under jumps; they are local approximations.

## 24. Implied volatility

IV is model input making model price equal market price. It embeds risk premium and supply-demand; not objective forecast.

Options trader must compare priced distribution with expected realized distribution, not only predict direction.

## 25. Event volatility và IV crush

Near earnings/CPI/FOMC, near-term IV can rise. After event, uncertainty disappears and IV often drops.

Long option may lose despite correct direction if move smaller than priced and vol/time decay dominates.

## 26. Vertical spreads

Vertical spreads buy one strike and sell another same expiry. They trade premium reduction for capped payoff.

Defined-risk structure can simplify sizing but still has assignment/liquidity risk before expiry.

## 27. Straddles và strangles

Long straddle/strangle express long-vol/large-move view. Short versions earn premium when realized movement smaller than priced but carry convex tail risk.

Win rate alone is misleading; payoff distribution matters.

## 28. Covered call

Covered call = long underlying + short call. It collects premium but sells upside convexity.

Income label can hide opportunity cost during strong rallies.

## 29. Protective put và collar

Protective put buys downside insurance. Collar finances part of protection by selling upside call.

Insurance has cost; hedge design always trades protection, participation and carry.

## 30. Short option tail risk

Naked short options can show many small wins then rare huge losses. Margin often rises when volatility spikes, exactly when mark-to-market losses appear.

Never size by premium received.

## 31. Swaps overview

Swap exchanges cash-flow streams according formula. Common examples: interest-rate swap, FX swap/cross-currency swap, total-return swap and credit-default swap.

Swaps are usually OTC/institutional and rely heavily on legal agreements, collateral and counterparty management.

## 32. Interest-rate swap

Plain-vanilla interest-rate swap commonly exchanges fixed rate vs floating reference on notional principal.

A borrower with floating debt can pay fixed/receive floating to reduce rate uncertainty. A bond investor can use swaps to alter duration without selling cash bonds.

## 33. Swap DV01 và duration

Rate swap risk should be measured by sensitivity such as DV01/PV01 rather than notional alone.

Large notional short-maturity swap can have less rate sensitivity than smaller long-duration swap.

## 34. Cross-currency swap

Cross-currency swaps exchange principal/cash flows in different currencies. They can hedge both FX and interest-rate mismatch.

Cross-currency basis can deviate from textbook covered-interest parity due balance-sheet/funding constraints.

## 35. Total Return Swap

Total Return Swap (*TRS*) transfers economic return of asset/index without direct ownership. Receiver gets price appreciation + income and pays financing/spread, depending contract.

TRS creates leverage/counterparty exposure and can hide economic ownership from simple cash-security view.

## 36. Credit Default Swap

Credit Default Swap (*CDS*) transfers credit risk. Protection buyer pays premium; protection seller compensates upon defined credit event subject to contract settlement.

CDS spread is market price of credit protection, not exact default probability. Recovery, liquidity and risk premium matter.

## 37. CDS basis

Cash bond spread and CDS spread can differ because funding, deliverability, liquidity, counterparty and technical flows.

Basis trade is not risk-free even if theoretical relation suggests convergence.

## 38. Variance/volatility swaps intuition

Institutional derivatives can exchange realized variance against fixed strike. They offer purer volatility exposure than options but have nonlinear tail behavior and OTC complexity.

Retail learner mainly needs understand volatility itself can be underlying risk factor.

## 39. CFD mechanics

CFD is bilateral contract with broker based on price change; client usually does not own underlying.

Economics include spread/commission, financing, dividend adjustments, margin, stop-out and broker execution policy.

## 40. Overnight financing

CFD/leveraged spot positions accrue financing. Directionally correct long-horizon trade can underperform badly after carry.

Always compare with cash asset/futures alternative.

## 41. Broker/counterparty risk

For OTC products, broker is legal counterparty/intermediary. Check entity, regulator, client-money segregation, negative-balance rules, execution policy and withdrawal process.

Marketing labels such as ECN/STP do not replace legal due diligence.

## 42. Central clearing vs bilateral exposure

Exchange futures/options generally clear centrally; many OTC derivatives may also be centrally cleared depending product/regulation, while others remain bilateral.

Clearing reduces bilateral counterparty complexity but concentrates risk into clearing system and margin mechanisms.

## 43. Collateral

Collateral protects against counterparty default but creates liquidity demand. Haircuts determine how much value counts.

In stress, collateral requirements/haircuts can rise, forcing cash raising and asset sales. Thus “hedged” derivative can still create liquidity risk.

## 44. Netting

Master agreements may allow offsetting positive/negative derivative values with same counterparty upon default.

Netting reduces gross credit exposure, but enforceability depends legal agreement/jurisdiction. Retail accounts may have simpler broker-level netting rules.

## 45. Counterparty wrong-way risk

Wrong-way risk occurs when counterparty becomes weaker exactly when exposure to it rises.

Example: buying protection from institution whose credit quality deteriorates in same systemic crisis you hedge against.

## 46. Hedging beta bằng index futures

Approx hedge contracts:

`Contracts ≈ Portfolio Value × Beta / Futures Notional`

But beta changes and sector composition creates basis risk. Hedge should be monitored, not set-and-forget.

## 47. FX hedging

FX forwards/futures reduce foreign-currency exposure but create carry/roll/basis costs.

Hedge ratio should reflect liability currency and desired volatility, not automatically 100%.

## 48. Duration hedging

Bond exposure can be hedged with rate futures/swaps by matching DV01/key-rate sensitivities rather than nominal values.

Curve twists mean one-duration number can be insufficient.

## 49. Commodity hedging

Producer can short futures; consumer long futures. Grade, location and timing mismatch create basis risk.

Airline hedging crude does not perfectly hedge jet fuel crack spread.

## 50. Equity-option hedge

Protective puts/put spreads can cap downside but cost premium. Index future short removes beta linearly but also removes upside.

Choice depends whether risk to hedge is linear beta, tail loss or event-specific.

## 51. Hedge ratio

Hedge ratio can be notional-based, beta-based, DV01-based, delta-based or statistical.

Mathematically optimized hedge may fail if correlation changes. Objective must be defined first: reduce variance, cap tail, match liability or protect a specific scenario?

## 52. Basis risk

Perfect hedge rarely exists because hedge instrument differs from exposure in grade, timing, index composition or liquidity.

Basis risk should be treated as residual position, not ignored.

## 53. Cross-hedging

When direct hedge absent, use correlated instrument. Example small exporter hedging via broader FX/index proxy.

Cross-hedge effectiveness depends stable relationship; stress can break correlation.

## 54. Derivative P/L attribution

Separate P/L into underlying move, carry/roll, volatility, financing, basis and execution.

Without attribution, trader may think directional thesis worked while return actually came from favorable carry, or vice versa.

## 55. Position sizing bằng scenario loss

Do not size by margin. Size based on loss under invalidation and stress scenario.

If one contract can lose $1,000 in plausible adverse move while risk budget is $200, one contract already too large regardless margin requirement.

## 56. Portfolio Greeks/notional aggregation

Across derivatives, aggregate Delta-equivalent, Gamma, Vega, DV01, FX notionals and credit exposure.

Ten small trades may create one huge common factor exposure.

## 57. Liquidity risk

Derivative liquidity can vanish around events/limit moves. Quoted spread/depth in normal markets may not represent exit cost in stress.

Options far OTM, deferred commodity expiries and small contracts can be especially fragile.

## 58. Expiry clustering

Portfolio with many contracts expiring same date has operational and market concentration. Roll periods can create large execution need.

Stagger expiries when appropriate and maintain calendar of notice/exercise dates.

## 59. Corporate actions

Equity options/futures can be adjusted for splits, mergers, special dividends or spin-offs. Contract deliverable may change.

Never assume old multiplier/strike remains economically identical after action; read exchange notice.

## 60. Tax/accounting/regulatory layer

Derivative tax, reporting and eligibility vary by jurisdiction/account. Economic exposure may be same but after-tax result different.

For real-money decisions, verify current broker/exchange/tax rules rather than rely static note.

## 61. Contract-spec checklist

Verify underlying, multiplier, tick, trading hours, expiry, notice dates, settlement, margin, price limits, exercise style, assignment, corporate-action adjustment, financing, tax và counterparty.

Unknown spec = no trade.

## 62. Common mistakes

Frequent errors: sizing by margin, forgetting multiplier, ignoring roll/carry, holding deliverable contract too long, treating CFD as ownership, buying option solely for direction, selling premium because win rate high, ignoring collateral calls, assuming hedge perfect, and stacking correlated derivatives.

## 63. Derivatives trong portfolio

Three broad roles: hedge existing risk, obtain efficient/temporary exposure, or speculate within defined risk budget.

Derivative should solve portfolio problem or express tested edge. Leverage is implementation tool, not alpha source.

## 64. Mental model cuối cùng

Analyze every derivative through:

`Underlying → Contract payoff → Notional/sensitivity → Margin/collateral path → Carry/roll/basis → Liquidity/expiry → Counterparty/settlement → Portfolio interaction`

Nếu không giải thích được tất cả layers này, chưa nên dùng contract đó.