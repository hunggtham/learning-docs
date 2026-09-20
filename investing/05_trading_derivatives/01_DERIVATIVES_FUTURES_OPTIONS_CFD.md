# Derivatives — Futures, Options, CFD và hedging

> Derivative là contract whose value depends on an underlying. Nó có thể dùng để hedge, tạo exposure hiệu quả hoặc speculate, nhưng leverage và nonlinear payoff khiến risk khác cash assets. Chapter này là nền tảng toàn diện trước khi sang file options/volatility chuyên sâu.

## 1. Derivative không đồng nghĩa ownership

Mua common stock thường cho ownership/residual claim. Mua futures, option, forward hay CFD thường tạo contractual exposure chứ không làm bạn trở thành owner của underlying theo cùng nghĩa.

Điều này thay đổi legal rights, margin, counterparty và settlement. Trước trade, luôn biết underlying, contract type, multiplier, tick size, expiry, settlement, margin, financing và worst-case payoff.

## 2. Forward và futures khác nhau

*Forward* là agreement mua/bán underlying tại future date với price agreed today, thường OTC và customizable. Counterparty risk được quản lý bằng legal agreements/collateral tùy participants.

*Futures* được standardized bởi exchange: contract size, expiry và settlement rules cố định. Clearing house đứng giữa counterparties và mark-to-market/margin làm credit exposure được reset thường xuyên hơn.

Standardization tăng liquidity nhưng tạo basis/roll requirements nếu exposure của bạn không khớp exact contract.

## 3. Notional value

Futures notional thường:

`Notional = Futures Price × Contract Multiplier`

Nếu index futures price 400 và multiplier 250, notional = 100.000 currency units dù initial margin nhỏ hơn nhiều.

Margin posted không phải economic size. Risk phải tính trên notional và price sensitivity.

## 4. Tick size và tick value

*Tick size* là minimum price increment. *Tick value* = tick size × multiplier. Nếu contract tick 0,25 và multiplier 50, one tick = 12,5.

Trader phải biết tick value trước order; nếu không, stop “10 points” không nói rõ actual money risk.

## 5. Initial margin và maintenance margin

Initial margin là collateral requirement để open position. Maintenance margin là threshold cần duy trì. Exchange/clearing/broker có thể adjust requirements khi volatility tăng.

Nếu equity giảm dưới threshold, trader có thể nhận margin call hoặc bị liquidate. Margin increase trong stress có thể force deleveraging ngay khi price unfavorable.

## 6. Variation margin và mark-to-market

Futures P/L được marked to market theo rules. Daily/real-time losses reduce account equity; gains add equity. Vì vậy path matters.

Position cuối tuần quay lại entry vẫn có thể bị closed trước đó nếu intraday/intermediate loss vượt collateral.

## 7. Futures fair value và basis

*Basis* thường = futures price - spot price. For financial assets, fair-value intuition includes financing cost and benefits like dividends:

`Futures ≈ Spot × financing effect - expected distributions`

Exact formula depends compounding, time and asset. If futures too expensive relative spot/carry, arbitrageurs may sell futures/buy underlying; opposite if too cheap, subject to transaction/funding constraints.

## 8. Convergence near expiry

As expiry approaches, futures and spot should converge under arbitrage and settlement design. Persistent large difference at expiry would create exploitable trade if frictionless.

Before expiry, basis can move because rates, dividends, borrow cost, scarcity and positioning change.

## 9. Cash settlement vs physical delivery

Index futures are commonly cash-settled. Commodity futures may allow/require physical delivery under contract rules. Retail trader should never assume “broker will automatically handle everything” without reading specification.

If holding physically deliverable contract near expiry, know first notice day, last trade day and broker liquidation policy.

## 10. Commodity futures curve

Commodities have term structure across expiries. *Contango* generally means longer contracts priced above nearer contracts; *backwardation* the reverse.

Curve reflects storage, financing, insurance, inventory scarcity and *convenience yield*—economic benefit of holding physical inventory.

Spot direction alone does not determine futures-investor return.

## 11. Roll yield

A fund maintaining constant futures exposure must roll before expiry. In persistent contango, selling cheaper near contract and buying more expensive far contract can create negative roll effect. In backwardation, roll can be positive, though realized outcome also depends price changes.

Commodity ETF can therefore materially diverge from spot index people see in news.

## 12. Calendar spreads

Calendar spread trades relative price between expiries rather than outright commodity direction. Example long near/short far or reverse.

Drivers include inventory, seasonality, storage constraints and temporary supply disruptions. Spread risk can still be large; it is not “market-neutral” in economic sense.

## 13. Options: quyền và nghĩa vụ

Call buyer has right, not obligation, to buy at strike. Put buyer has right to sell. Buyer pays premium; seller receives premium and takes obligation if exercised/assigned according to contract rules.

Long option loss is generally capped at premium for standalone purchased option. Short option loss can be much larger, especially naked short call.

## 14. Strike, expiry và moneyness

Option can be in-the-money (*ITM*), at-the-money (*ATM*) or out-of-the-money (*OTM*). Moneyness describes relationship between spot and strike, not whether trade profitable relative premium paid.

A call may be ITM at expiry yet buyer still lose if intrinsic value < premium originally paid.

## 15. Intrinsic và extrinsic value

Option price = intrinsic value + time/extrinsic value.

Call intrinsic = `max(S - K, 0)`; put intrinsic = `max(K - S, 0)`.

Extrinsic value reflects time, expected volatility, rates, dividends/borrow and supply-demand. It decays toward zero at expiry, though path is nonlinear.

## 16. American vs European exercise

American-style options can generally be exercised before expiry; European-style only at expiry. “European” does not mean traded only in Europe.

Early exercise economics depend dividends, rates and remaining time value. Selling an option often makes more economic sense than early exercise when extrinsic value remains, but exact situation varies.

## 17. Assignment risk

Short options can be assigned according to clearing rules. Assignment can create unexpected long/short underlying positions, funding needs or dividend obligations.

Around ex-dividend dates and deep ITM options, early assignment risk may rise. Trader must know broker exercise/assignment handling.

## 18. Put-call parity intuition

For European options under simplifying assumptions, call, put, underlying and financing are linked by arbitrage. A common relation:

`Call - Put ≈ Spot - PV(Strike)`

Adjust dividends/carry as needed. Put-call parity explains synthetic positions and why options prices cannot move independently without arbitrage bounds.

## 19. Greeks là ngôn ngữ risk

Delta measures first-order sensitivity to underlying. Gamma measures how delta changes. Theta measures sensitivity to time passage, all else equal. Vega measures sensitivity to implied volatility. Rho relates rates.

A portfolio delta-neutral can still carry huge short-gamma/short-vega risk. Greeks describe local sensitivities, not guaranteed P/L under large jumps.

## 20. Implied volatility

Implied volatility (*IV*) is volatility input that reconciles model price with market option price. It is not a prediction guaranteed to equal future realized volatility.

Higher IV generally raises option time value because distribution of possible outcomes widens. Option buyers pay for convexity/uncertainty; sellers receive premium for absorbing it.

## 21. Implied move

ATM straddle price can give rough market-implied move intuition around an event/horizon. If market prices very large move and actual move small, long-vol position can lose despite correct direction.

Direction alone is insufficient in options; magnitude and volatility repricing matter.

## 22. Event volatility và IV crush

Before earnings/FOMC or binary event, near-dated IV may rise. After uncertainty resolves, IV can drop sharply.

Long call can lose while stock rises if realized move is smaller than priced and IV crush/time decay outweigh delta gain. This is why buying options “because event coming” is not automatically favorable.

## 23. Long call và long put

Long call gives bullish convex exposure with premium-defined downside. Long put gives bearish convexity or insurance.

The key question is not just direction but breakeven relative to premium and time. Expensive option can be poor trade even with right directional thesis.

## 24. Vertical spreads

Bull call spread buys lower-strike call and sells higher strike. It reduces net premium but caps upside. Bear put spread is analogous bearish structure.

Spreads convert open-ended convexity into bounded payoff. Understand max gain/loss and assignment risk rather than memorize names.

## 25. Straddle và strangle

Long straddle buys call+put near same strike to express large-move/long-vol view. Strangle uses different strikes, usually cheaper but requires larger move.

Short versions earn premium when realized movement smaller than priced but carry convex tail risk. High historical win rate can coexist with poor risk-adjusted expectancy if rare losses dominate.

## 26. Covered call và protective put

Covered call = long underlying + short call. It collects premium but caps upside; it is not free income. Economically you sell part of upside convexity.

Protective put = long underlying + long put. It buys downside insurance, reducing expected return by premium cost if protection not used.

## 27. Collar

Collar combines protective put and short call. Premium from call can finance put partly/fully, creating downside floor and upside cap.

Used in concentrated-stock/risk-management contexts, but tax/liquidity/assignment rules matter.

## 28. Synthetic positions

Put-call parity allows constructing exposures synthetically. Long call + short put at same strike/expiry resembles leveraged forward exposure under assumptions.

Understanding synthetics helps identify when apparently different structures share same economic risk.

## 29. Short option tail risk

Short premium often appears smooth because many expiries end with small gains. But loss distribution can be negatively skewed.

Naked short call has theoretically unbounded loss. Short put can suffer large loss as underlying approaches zero. Margin can expand at same time volatility rises, worsening forced-liquidation risk.

Never size short-option risk by premium received alone.

## 30. CFD mechanics

Contract for Difference (*CFD*) is bilateral contract with broker based on price change. Client usually does not own underlying.

Economics include spread/commission, overnight financing, dividend adjustments, margin, stop-out and broker execution policy. Legal jurisdiction and client-money treatment are part of product risk.

## 31. Overnight financing

Leveraged CFD holds notional financed partly by broker structure; overnight swap/financing accumulates. A trade directionally right over months can still underperform due financing.

Therefore compare total holding cost with cash asset/futures alternative before using CFD for long horizon.

## 32. Broker and counterparty risk

For OTC CFD/Forex, broker is not just interface. Check legal entity, regulator, segregation/client money terms, negative-balance protection if applicable, execution model and withdrawal process.

High leverage offered is not evidence of better broker. Often it increases liquidation probability.

## 33. Hedging beta bằng index futures

If equity portfolio beta exposure is `Portfolio Value × Beta`, approximate futures hedge contracts:

`Contracts ≈ Exposure to hedge / Futures notional per contract`

This is approximation. Portfolio beta changes; futures basis and sector composition create basis risk.

## 34. FX hedging

Foreign asset return in home currency combines local-asset return and FX. Forward/futures or hedged fund can reduce currency exposure.

Hedge has carry based on rate differential plus transaction/basis cost. It changes risk profile rather than “remove risk for free”.

## 35. Duration hedging

Bond portfolio can use rate futures/swaps to alter duration/DV01. Hedge size should match sensitivity, not nominal value.

A $1m short-duration portfolio and $1m long-duration portfolio have very different rate risk despite same market value.

## 36. Commodity hedging

Producer can short futures to lock selling price; consumer can long to lock purchase price. But hedge instrument may differ grade/location/timing from physical exposure, creating basis risk.

Airline hedging fuel with crude futures is not perfect because jet fuel crack spreads can move.

## 37. Hedge ratio và basis risk

Perfect hedge requires matching underlying, quantity and timing, often impossible. *Basis risk* is risk hedge and exposure do not move one-for-one.

Hedge ratio can be notional-based, beta-based or statistical depending objective. More mathematically optimized hedge is not automatically operationally better if correlation unstable.

## 38. Position sizing bằng scenario loss, không bằng margin

A common beginner error is “broker requires only $500 margin so position is $500 risk”. Wrong. Economic risk comes from notional and price move.

Size derivative by loss under invalidation/stress scenario. Example: if one futures contract loses $1,000 on plausible adverse move and risk budget is $200, one full contract is already too large regardless margin.

## 39. Contract-spec checklist

Before trading any derivative verify: underlying, contract multiplier, tick size/value, trading hours, expiry, last trade/notice dates, settlement type, margin, price limits/circuit breakers, corporate-action handling, option style, assignment, financing and tax/account implications.

If one item unknown, pause rather than guess.

## 40. Common mistakes

Frequent mistakes include sizing by margin, forgetting multiplier, holding commodity future into delivery window, ignoring roll yield, treating CFD as stock ownership, buying options solely for direction, selling options based on win rate, ignoring assignment, assuming hedge perfect and using leverage to recover losses.

Most derivative blowups are not from obscure mathematics; they come from notional, path, liquidity and operational misunderstanding.

## 41. Derivatives trong portfolio

Derivatives have three legitimate broad roles: hedge existing risk, obtain efficient/temporary exposure, or speculate within defined risk budget.

For long-term investor, derivative should solve a portfolio problem. For trader, it should express a tested edge with explicit scenario loss. In both cases leverage is a tool, not source of expected return.

## 42. Mental model cuối cùng

Analyze every derivative through:

`Underlying → Contract payoff → Notional/leverage → Margin path → Liquidity/expiry → Counterparty/settlement → Portfolio interaction`

If you cannot explain all seven, do not trade it yet.