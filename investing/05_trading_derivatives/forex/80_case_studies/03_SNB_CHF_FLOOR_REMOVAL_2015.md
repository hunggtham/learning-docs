# Case 03 — SNB CHF Floor Removal 2015: policy floor, gap risk và liquidity discontinuity

Ngày 15/01/2015, Swiss National Bank (SNB) chấm dứt minimum exchange rate `CHF 1.20 per euro` mà ngân hàng đã duy trì từ 2011. Sự kiện này là case kinh điển về **regime break, discontinuous price movement, stop-loss failure và broker/counterparty risk**.

Điều cần học không phải “central bank luôn có thể đổi ý”. Điểm sâu hơn là: khi một policy commitment tạo artificial boundary cho price trong thời gian dài, market structure và positioning có thể thích nghi quanh boundary đó. Nếu commitment biến mất đột ngột, historical volatility và normal execution assumptions có thể trở nên gần như vô nghĩa trong vài phút.

## 1. Vì sao SNB đặt floor?

Trong euro-area sovereign stress, Swiss franc chịu strong safe-haven demand.

CHF appreciation quá mạnh tạo lo ngại về:

```text
Deflation
Export competitiveness
Domestic economic activity
```

SNB thiết lập minimum exchange rate:

```text
EUR/CHF >= 1.20
```

và tuyên bố sẵn sàng mua foreign currency với quy mô lớn để enforce floor.

Mental model:

```text
Private demand for CHF
→ would push EUR/CHF lower
→ SNB creates CHF / buys foreign currency
→ absorbs pressure
→ keeps EUR/CHF near or above floor
```

## 2. Policy floor changes market distribution

Nếu market tin floor credible:

```text
EUR/CHF downside appears limited near 1.20
```

Điều này thay đổi behavior của traders và hedgers.

Strategies có thể bắt đầu dựa vào assumption:

```text
Below 1.20 is effectively unavailable
```

Nhưng policy constraint không phải physical law.

## 3. Hidden option created by central bank

Một credible floor có payoff giống một implicit put-like policy support.

Participants gần floor có thể nghĩ:

```text
Downside limited by SNB
Upside remains open
```

Điều này có thể encourage crowded positioning.

Risk problem xuất hiện nếu participants price policy commitment như certainty thay vì conditional regime.

## 4. Balance-sheet cost of maintaining floor

Để giữ floor khi CHF demand mạnh, SNB phải mua foreign assets.

Do đó central-bank balance sheet expands.

Policy trade-off:

```text
Continue buying foreign currency
→ larger balance sheet / exposure

or
stop defending floor
→ CHF appreciates sharply
```

Không có costless option.

## 5. Euro-area policy matters

CHF floor không thể phân tích chỉ từ Switzerland.

Nếu ECB policy becomes more expansionary:

```text
EUR weakens
→ pressure on EUR/CHF floor increases
→ SNB must absorb more demand for CHF
```

Again, FX is relative macro.

## 6. December 2014: negative rates as support tool

Trước khi bỏ floor, SNB announced negative interest rate on sight deposits to reduce attractiveness of CHF holdings and support minimum exchange rate.

Điều này cho thấy central bank có thể combine:

```text
FX intervention
+ interest-rate policy
```

Nhưng multiple tools không guarantee permanence of the regime.

## 7. January 15, 2015 policy break

SNB announced:

```text
Minimum exchange rate discontinued
Sight-deposit rate lowered to -0.75%
Three-month Libor target range lowered further
```

Đây là fundamental regime change, không phải normal data surprise.

Before announcement:

```text
Market distribution conditioned on floor
```

After announcement:

```text
That boundary no longer exists
```

## 8. Why price moved discontinuously

Khi floor bị xóa:

```text
Existing buy/sell orders were not sufficient
at nearby prices
```

Market had to search for a new clearing price.

Trong normal market:

```text
1.2000
→ 1.1999
→ 1.1998
```

Trong regime break:

```text
large zones may have almost no executable liquidity
```

Price can jump through levels rather than trade smoothly through every point.

## 9. Stop-loss is an instruction, not a guaranteed price

Nếu trader long EUR/CHF near floor với stop below 1.20:

```text
Trigger condition occurs
→ stop becomes market order
→ no liquidity near expected stop
→ fill can occur far away
```

Planned loss and realized loss can diverge massively.

Lesson:

```text
Stop distance
is not maximum loss
when gap/liquidity discontinuity exists.
```

## 10. Leverage turns price gap into account insolvency

Suppose:

```text
Equity = 10,000
Notional exposure = 500,000
Effective leverage = 50x
```

A 1% adverse move implies roughly:

```text
5,000 loss
```

A much larger discontinuous move can exceed account equity before liquidation occurs.

Thus:

```text
Broker maximum leverage
+ assumed policy floor
= potentially catastrophic combination
```

## 11. Negative-balance risk

In extreme gaps, a leveraged account can move from positive equity to negative before positions are closed.

Whether client owes negative balance depends on:

```text
Jurisdiction
Product terms
Client classification
Broker policy / regulation
```

Never assume stop-out guarantees zero floor on equity.

## 12. Broker risk becomes client risk

A broker/dealer aggregates many client positions.

If many clients are positioned similarly:

```text
Market gaps
→ clients incur losses beyond deposits
→ broker has receivables from clients
→ broker may simultaneously owe liquidity providers
→ broker capital/liquidity stress rises
```

Thus market risk can become counterparty risk.

## 13. Hedging is not instantaneous

A dealer may intend to hedge client flow externally.

In discontinuous market:

```text
hedge venue liquidity disappears
→ hedge price gaps
→ execution mismatch grows
```

A “fully hedged” business model may still have basis, latency and gap exposure.

## 14. Why historical VaR fails near regime breaks

Suppose EUR/CHF spent years near floor with very low realized volatility.

Historical model learns:

```text
Daily move distribution is narrow
```

But observed distribution is conditional on policy regime.

Once regime changes:

```text
old sample no longer describes current process
```

This is **model regime risk**.

## 15. Volatility suppression can hide tail risk

Policy floor suppresses observed volatility on one side.

Therefore low realized volatility may reflect:

```text
Active policy intervention
```

not:

```text
Low latent economic pressure
```

This mirrors lesson from managed currencies in other crises.

## 16. Position sizing should include regime-gap scenario

Normal sizing:

```text
Allowed loss / stop distance
```

is incomplete for policy-bound instrument.

Need additional scenario:

```text
What if policy boundary disappears overnight?
```

Then size should consider:

```text
Gap to plausible stress price
Not only stop level
```

## 17. Policy credibility is not probability 100%

SNB had repeatedly emphasized commitment to floor before removing it.

Research lesson:

```text
Official commitment can be strong
without being literally permanent.
```

A trader should model:

```text
Probability policy continues
Probability policy changes
Loss conditional on policy change
```

Expected loss may still be large even if policy-change probability seems small.

## 18. Asymmetric risk

Near a defended floor, trade may look attractive:

```text
Small downside under regime
Potential upside if EUR rises
```

But true distribution includes:

```text
Rare regime-break state
with very large loss
```

This resembles short-volatility payoff:

```text
frequent small gains
+ rare catastrophic loss
```

## 19. Liquidity is state dependent

A pair may be highly liquid in normal times.

Liquidity during regime break depends on willingness of market makers to quote into uncertainty.

```text
Normal liquidity
≠ stress liquidity
```

Risk model must distinguish both.

## 20. Market order vs limit order trade-off

During gap:

### Market order

```text
Higher execution probability
Lower price certainty
```

### Limit order

```text
Price protection
but may not execute
```

No order type eliminates both price and execution risk.

## 21. Guaranteed stop is a separate product feature

If a broker explicitly offers guaranteed-stop protection under contractual terms, economics differ.

But ordinary stop order is not guaranteed stop.

Always distinguish:

```text
Stop order
Guaranteed stop product
```

## 22. Risk concentration across clients

A broker may appear diversified across thousands of clients.

But if clients all use same popular strategy near policy floor:

```text
Client count high
but factor concentration also high
```

This is same portfolio lesson at broker level.

## 23. Why backtest cannot reproduce this with ordinary candles

A daily candle only gives:

```text
Open
High
Low
Close
```

It does not tell:

```text
Executable bid/ask path
Depth
Rejected quotes
Latency
Actual fill availability
```

Therefore backtest around CHF 2015 needs high-resolution market/execution assumptions and still contains uncertainty.

## 24. Options lesson

FX options incorporate probability distribution and jump risk differently from spot.

Before regime break, option market may show:

```text
skew
implied volatility
barrier demand
```

that contains information about perceived tail risk.

But options are not perfect oracle; pricing also reflects supply/demand and policy credibility assumptions.

## 25. Central-bank balance sheet as regime variable

Research should monitor:

```text
FX reserves / foreign assets
Balance-sheet growth
Intervention pace
Domestic political debate
Inflation/deflation objective
External central-bank policy
```

Policy sustainability is dynamic.

## 26. What not to learn

Wrong lesson:

```text
"Never trust central banks."
```

Central-bank guidance often matters and many commitments persist.

Better lesson:

```text
Treat policy commitments as conditional regimes,
not physical guarantees.
```

Wrong lesson:

```text
"Use wider stop around central-bank events."
```

A wider stop still may be jumped.

Better lesson:

```text
Reduce exposure to survive discontinuity.
```

## 27. Stress-test template

For any policy-supported currency:

```text
Normal move: 1%
Large move: 5%
Regime break: 15–30%
Spread: 5x normal
No fill near stop
Margin requirement doubled
Counterparty unavailable for 30 minutes
```

Calculate:

```text
P/L
Equity
Margin level
Negative-balance risk
Counterparty dependency
```

## 28. Mechanism map

```text
Safe-haven demand for CHF
→ SNB establishes EUR/CHF floor
→ intervention suppresses downside volatility
→ market adapts around credible boundary
→ balance-sheet/intervention burden grows
+ euro-area policy pressure
→ SNB removes floor
→ liquidity discontinuity
→ CHF reprices sharply
→ stop slippage / leveraged losses
→ client losses transmit to brokers/counterparties
```

## 29. Practical checklist derived from the case

Before trading near policy boundary:

```text
What is exact policy commitment?
Is it legally/operationally guaranteed?
How is it enforced?
What would cause policy reversal?
How crowded is positioning?
What does option market imply?
What happens if no quotes exist near stop?
Can account survive 10x normal move?
Can broker survive client losses?
Is negative-balance protection contractual/regulatory?
```

## 30. Research exercise

Create a hypothetical EUR/CHF position before 15/01/2015:

```text
Equity = 50,000 CHF
Long EUR/CHF notional = 500,000 EUR
Entry = 1.2010
Stop = 1.1980
```

First calculate planned stop loss under normal execution.

Then ignore stop and stress fill at:

```text
1.15
1.10
1.05
```

Compare:

```text
Planned loss
Stress loss
Equity remaining
Effective leverage after first move
```

Mục tiêu là thấy why stop-based risk budget fails under discontinuity.

## Nguồn nền

- Swiss National Bank, press release, **15 January 2015 — SNB discontinues minimum exchange rate and lowers interest rate to -0.75%**.
- Swiss National Bank, monetary-policy chronology describing establishment and removal of the EUR/CHF minimum exchange rate.

Case này tập trung vào mechanics of regime break, không dùng hindsight để khẳng định việc bỏ floor có thể được dự đoán chắc chắn.
