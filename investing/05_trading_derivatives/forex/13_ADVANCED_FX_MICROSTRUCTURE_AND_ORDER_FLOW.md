# 13 — Advanced FX microstructure và order flow

Ở cấp nâng cao, FX không chỉ là chuỗi price bars mà là một mạng lưới dealer, venue, client flow, inventory, hedging và latency. **Microstructure** nghiên cứu cách những cơ chế này tạo ra executable prices, spreads, liquidity và short-horizon price discovery.

Mental model:

```text
Information / client demand
→ orders and dealer inventory
→ quote adjustment
→ execution across fragmented venues
→ hedging / internalization
→ observed price path
```

## 1. Order flow khác volume

**Order flow** thường nhấn mạnh hướng và sequence của trading demand, ví dụ signed buys/sells.

Raw volume chỉ nói activity magnitude.

Hai periods có cùng volume nhưng net aggressive buying khác nhau có thể tạo price impact khác.

## 2. FX order flow khó quan sát toàn bộ

OTC FX phân mảnh. Không có một global tape chứa tất cả transactions.

Dữ liệu có thể đến từ:

- specific dealer;
- ECN/venue;
- futures exchange;
- broker clients;
- aggregated institutional source.

Mỗi source chỉ quan sát một phần market.

## 3. Dealer inventory

Dealer nhận client flow có thể tạm thời tích lũy inventory.

Nếu inventory quá lệch, dealer có thể:

- adjust quote;
- hedge externally;
- internalize với opposite client flow.

Price change ngắn hạn có thể phản ánh inventory management chứ không chỉ public news.

## 4. Adverse selection

Liquidity provider sợ giao dịch với counterparty có information advantage.

Khi perceived adverse-selection risk tăng:

```text
spread widens
quoted size shrinks
last-look rejection may rise depending on protocol
```

News windows là ví dụ rõ.

## 5. Spread decomposition

Conceptually spread bù cho:

- inventory risk;
- adverse selection;
- operating/technology cost;
- capital/funding;
- expected profit.

Relative importance thay đổi theo venue/regime.

## 6. Price discovery

Price discovery là process market incorporates information vào quotes/trades.

Trong FX, discovery có thể diễn ra across:

- interdealer spot venues;
- dealer-client platforms;
- futures;
- options;
- rates markets.

Một venue có thể lead ở một horizon nhưng không mọi lúc.

## 7. Fragmentation

Cùng currency pair có nhiều liquidity pools.

Arbitrage/market making giữ prices gần nhau nhưng latency và venue rules tạo temporary differences.

Do đó “market price” thường là constructed reference từ multiple quotes.

## 8. Top-of-book vs depth

Best bid/ask chỉ là level đầu.

Institutional execution quan tâm:

```text
available size at best
next levels
depth shape
resiliency after trade
```

Tight spread nhưng shallow book vẫn có poor liquidity cho large orders.

## 9. Market resilience

Sau large order, liquidity có quay lại nhanh không?

Resilience là dimension khác của liquidity bên cạnh spread/depth.

## 10. Impact

Large aggressive order có thể move price.

Temporary impact có thể mean-revert; permanent component có thể reflect information.

Tách hai phần là execution/research problem khó.

## 11. Square-root-like impact intuition

Nhiều markets cho thấy impact tăng sublinearly với size trong empirical research, nhưng không nên hard-code universal law cho mọi FX venue/regime.

Need instrument/venue-specific calibration.

## 12. Internalization

Dealer có thể match opposite client flows internally thay vì hedge mọi trade ra street.

Điều này giảm external footprint nhưng tạo inventory/conflict considerations.

Internalization ratio có thể ảnh hưởng execution behavior nhưng data không phải luôn public.

## 13. Last look

Một số FX electronic protocols cho liquidity provider short acceptance window sau request/trade attempt.

Purpose có thể liên quan stale-price/latency risk; client perspective quan tâm rejection/asymmetric execution.

Khi đánh giá, cần empirical stats và protocol disclosure, không chỉ label.

## 14. Request-for-stream / request-for-quote

Institutional clients có thể nhận streaming prices hoặc request quote từ dealers.

Execution choice depends on:

- size;
- information leakage;
- urgency;
- relationship;
- expected impact.

## 15. Information leakage

Large order bị lộ có thể làm market move trước completion.

Execution algorithms cố balance:

```text
urgency
vs
market impact / information leakage
```

## 16. TWAP/VWAP/POV concepts

### TWAP
Spread order across time.

### VWAP
Target volume-weighted benchmark where meaningful volume data exists.

### POV
Trade as fraction of observed market volume.

Trong OTC FX, benchmark/data source phải được định nghĩa cẩn thận.

## 17. Implementation shortfall algorithm

Optimize trade-off:

```text
waiting risk
vs
immediate market impact
```

High urgency → execute faster, accept impact.
Low urgency → wait, accept price risk.

## 18. Fixing benchmark execution

WM/R-like fixing windows và institutional benchmarks có thể concentrate orders.

Participants hedging benchmark risk can create predictable activity, nhưng exploitability after cost/crowding không được assumed.

## 19. Stop clusters

Stops có thể cluster quanh:

- previous highs/lows;
- round numbers;
- technical levels.

Khi price reaches cluster:

```text
triggered market orders
→ temporary order imbalance
→ faster move
```

Đây là mechanism có thể giải thích acceleration mà không cần conspiracy narrative.

## 20. Liquidity sweep terminology

“Liquidity sweep” có thể map vào process:

```text
price reaches area with clustered conditional orders
→ aggressive flow increases
→ available liquidity consumed
→ price moves through level
→ continuation or reversal depends on subsequent flow
```

Term hữu ích nếu rule/data rõ; không nên biến thành deterministic setup.

## 21. Order-book imbalance

Trong centralized/visible venue:

```text
Imbalance = (Bid Depth - Ask Depth) / (Bid Depth + Ask Depth)
```

có thể be short-horizon feature.

Nhưng FX venue book chỉ là one pool, không global market.

## 22. Futures as proxy

Currency futures cung cấp centralized order-book/volume data và có thể dùng nghiên cứu price discovery/order flow.

Nhưng mapping sang OTC spot cần account:

- basis;
- trading hours;
- contract roll;
- participant mix.

## 23. COT data

Commitments of Traders cung cấp positioning categories cho futures, thường weekly và lagged.

Useful for broad positioning context, không phù hợp microsecond order flow.

## 24. Dealer-client flow datasets

Nếu có institutional dataset, flow có thể predictive ở horizons khác nhau.

Nhưng sample representativeness là central question:

```text
Which clients?
Which regions?
Which dealer?
How much market share?
```

## 25. Toxic flow

Dealer gọi flow “toxic” khi counterparty trades systematically before adverse price moves hoặc exploits stale quotes/latency.

Term phụ thuộc perspective và execution model, không đồng nghĩa misconduct.

## 26. Latency arbitrage

Nếu one venue updates faster than another, fast participant có thể trade stale quote.

Market makers respond bằng:

- faster infrastructure;
- wider spread;
- last look;
- quote throttling.

## 27. Co-location và speed

Ở ultra-short horizon, physical/network latency matters.

Retail internet trader không nên assume edge based on stale retail chart can compete with institutional low-latency systems.

## 28. Session handoff

Liquidity providers/participants change across Asia–Europe–US.

Spread/depth and price discovery behavior vary by local business hours and overlap.

## 29. Rollover window

Retail platforms may show poor liquidity/spread around daily rollover. Exact timing/product behavior broker-specific.

Short-term strategy should exclude/stress this window rather than assume daytime spread.

## 30. News microstructure

Near high-impact release:

```text
quotes pulled/widened
→ depth declines
→ algorithms process headline
→ price gaps across levels
→ liquidity gradually rebuilds
```

Historical candle cannot fully reconstruct executable path.

## 31. Flash events

Feedback loops among stops, leverage, thin liquidity and algorithms can create extreme short-lived moves.

Risk controls need:

- max slippage assumptions;
- price sanity checks;
- kill switch;
- leverage headroom.

## 32. Quote stuffing / manipulation claims

Specific manipulative practices require evidence and regulatory definitions. Do not label unusual quote behavior as manipulation from chart alone.

Use venue/regulator evidence where available.

## 33. Spread distribution

Rather than average spread only, store distribution:

```text
median
90th/95th/99th percentile
by session
event windows
stress periods
```

Tail spread drives stop/execution risk.

## 34. Slippage distribution

Average slippage can hide asymmetric tail.

Record positive and negative separately, especially stop orders.

## 35. Markout

Execution quality can use post-trade markout:

```text
price after 1s / 10s / 1m relative to fill
```

For liquidity provider, adverse markout suggests informed/toxic flow; for taker, it can measure execution timing.

## 36. TCA

Transaction Cost Analysis decomposes execution vs benchmark.

Metrics:

- arrival price;
- implementation shortfall;
- spread capture/cost;
- delay;
- market impact;
- post-trade markout.

## 37. Retail TCA

Retail trader can still log:

```text
decision price
quoted spread
fill price
latency estimate
slippage
exit fill
```

Across many trades this reveals broker/session/event execution quality.

## 38. Microstructure alpha decays fast

Short-horizon order-flow signals often have short half-life.

If infrastructure latency exceeds signal half-life, research alpha không executable.

## 39. Data synchronization

Combining spot, futures, rates, options requires clock synchronization.

Milliseconds/seconds mismatch can reverse lead-lag inference.

## 40. Causality caution

If futures move 50 ms before spot in sample, that does not automatically prove futures “cause” spot fundamentally. Could reflect common information processed at different speeds.

## 41. From microstructure to strategy

A microstructure strategy specification must include:

```text
venue/source
feature timestamp
latency
order type
fill model
size/depth
fees
rejections
market impact
```

Otherwise paper alpha can be impossible live.

## 42. Checklist

Bạn cần tự giải thích được:

1. Order flow vs volume.
2. Why no global FX order book exists.
3. Dealer inventory/adverse selection.
4. Depth/resilience vs spread.
5. Internalization/last look.
6. Stop clustering mechanics.
7. Limits of futures/order-book proxies.
8. TCA and markout.
9. Why microstructure alpha is execution-dependent.
10. Why unusual price behavior is not proof of manipulation.

## Đọc tiếp

→ [14 — FX options, volatility and hedging](./14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

## Internal links

- [01 — Market structure and instruments](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
