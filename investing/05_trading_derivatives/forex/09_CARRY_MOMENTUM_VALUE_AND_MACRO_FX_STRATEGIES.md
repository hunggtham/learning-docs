# 09 — Carry, momentum, value và macro FX strategies

Sau khi hiểu mechanics, regime, indicator và event analysis, có thể bắt đầu nghiên cứu **strategy families**. Mục tiêu của chương này không phải đưa ra tín hiệu giao dịch mà giải thích các nguồn return hypothesis thường gặp trong FX và cách phân biệt chúng.

Mental model:

```text
Economic / behavioral hypothesis
→ measurable signal
→ portfolio construction
→ execution and financing
→ realized return
→ attribution
```

Một strategy family chỉ đáng tin khi return không phụ thuộc vào một chart example đẹp hoặc một parameter cụ thể.

## 1. Strategy family khác setup đơn lẻ

Một setup như “RSI < 30 rồi buy” là rule rất cụ thể.

Một strategy family như **trend/momentum** rộng hơn: nó giả định price changes có persistence ở một horizon nào đó.

Family-level thinking giúp hỏi:

- mechanism là gì;
- horizon nào phù hợp;
- regimes nào thuận lợi/bất lợi;
- implementation nào robust.

## 2. Carry

Carry strategy trong FX khai thác chênh lệch yield/financing giữa currencies.

Simplified intuition:

```text
Long relatively high-yield currency
Short relatively low-yield currency
```

Return gần:

```text
Total Return
≈ Spot Return
+ Carry
- Transaction Cost
```

Carry chỉ profitable nếu adverse spot move không xóa financing advantage.

## 3. Carry không phải free interest

High yield có thể phản ánh:

- inflation risk;
- devaluation risk;
- sovereign/political risk;
- liquidity risk;
- crash risk.

Do đó carry portfolios có thể kiếm nhỏ đều rồi mất mạnh trong risk-off unwind.

Risk metric cần chú ý skew/tail, không chỉ Sharpe.

## 4. Forward discount/premium và carry signal

Institutional research thường dùng forward points hoặc interest differential thay vì retail swap quote thô.

Retail broker financing có markup riêng, nên:

```text
academic carry signal
≠ exact retail realized carry
```

Backtest implementation phải dùng instrument-specific financing.

## 5. Momentum / trend following

Momentum hypothesis:

```text
Currencies that appreciated over lookback
may continue outperforming over holding horizon
```

Possible mechanisms:

- gradual policy repricing;
- capital-flow persistence;
- underreaction;
- institutional execution over time.

Implementation có thể dùng:

- time-series momentum;
- cross-sectional momentum;
- breakout;
- moving-average trend.

## 6. Time-series vs cross-sectional momentum

### Time-series

So một currency pair với chính history của nó:

```text
Past return > 0 → long
Past return < 0 → short
```

### Cross-sectional

Rank nhiều currencies theo past performance:

```text
Long strongest group
Short weakest group
```

Hai cách có exposure và portfolio dynamics khác nhau.

## 7. Trend strategy thường có profile khác carry

Trend following thường có:

- nhiều small losses/whipsaws;
- một số large winners trong persistent moves.

Carry thường có thể có:

- frequent positive carry;
- occasional sharp reversals.

Kết hợp strategy families cần nhìn correlation trong stress, không chỉ full-sample correlation.

## 8. Value trong FX

FX value cố ước lượng currency “cheap/expensive” so với fundamental anchor.

Một anchor phổ biến trong academic discussion là purchasing power parity (PPP), nhưng FX value có thể dùng nhiều models khác.

Value thường có horizon dài hơn intraday technical setup.

## 9. Purchasing Power Parity

PPP intuition:

```text
Long-run exchange rate
should relate to relative price levels
```

Nếu prices ở A tăng nhanh hơn B trong thời gian dài, currency A có thể cần adjust để restore relative purchasing power.

Nhưng PPP deviations có thể tồn tại nhiều năm vì:

- non-tradables;
- productivity differences;
- capital flows;
- risk premium;
- policy/regime differences;
- measurement issues.

Do đó PPP không phải short-term timing model.

## 10. Real exchange rate

A simplified real exchange-rate concept combines nominal FX với relative price levels.

Value strategy có thể rank currencies theo deviation của real exchange rate khỏi long-run reference.

Nhưng “mean” có thể shift structurally. Stationarity phải được tested, không assumed.

## 11. BEER / FEER-like thinking

Behavioral/equilibrium exchange-rate frameworks có thể relate FX valuation tới:

- terms of trade;
- productivity;
- net foreign assets;
- real interest differentials;
- fiscal/external balance.

Model choice tạo model risk lớn. Không nên có một “fair value” với false precision.

## 12. Macro directional strategy

Macro FX strategy xây thesis từ:

```text
policy divergence
relative growth/inflation
capital flows
external balance
risk regime
```

Điểm khó là timing. Fundamental mispricing có thể kéo dài.

Vì vậy macro trader thường cần catalyst hoặc price confirmation.

## 13. Event-driven strategy

Event strategy tập trung quanh scheduled/unscheduled releases.

Có thể nghiên cứu:

- surprise-following;
- initial overreaction mean reversion;
- post-announcement drift;
- volatility expansion;
- option event premium.

Mỗi hypothesis cần timestamp resolution phù hợp.

## 14. Mean reversion

Mean-reversion strategy giả định displacement hiện tại tạm thời và price sẽ quay về reference.

Possible mechanisms:

- liquidity shock;
- temporary inventory imbalance;
- short-term overreaction;
- fixing/rebalancing flow.

Rủi ro chính: temporary move thực ra là beginning của new trend/regime.

## 15. Relative-value / cross strategy

Thay vì directional USD exposure, có thể trade relative view:

```text
Long currency A
Short currency B
```

chọn B để isolate factor tốt hơn.

Ví dụ nếu thesis là Europe outperform Japan, EUR/JPY có thể express thesis trực tiếp hơn EUR/USD nếu USD factor không liên quan — nhưng instrument/liquidity/risk vẫn phải đánh giá.

## 16. Dollar-neutral không đồng nghĩa risk-neutral

Một basket có net USD exposure gần zero vẫn có:

- EUR/JPY/AUD factor risk;
- carry risk;
- global risk sentiment;
- liquidity risk.

Neutrality luôn phải nói neutral đối với factor nào.

## 17. Statistical relative value

Pairs/spread models có thể tìm mean-reverting relationship giữa FX rates hoặc related markets.

Nhưng correlation cao không đủ. Cần kiểm tra:

- economic linkage;
- stationarity/cointegration if relevant;
- structural breaks;
- execution cost.

## 18. Volatility strategy

FX options cho phép strategy trên volatility thay vì chỉ direction:

- long/short volatility;
- relative vol;
- skew/risk reversal;
- event volatility;
- carry from option premium.

Đây là separate risk dimension và được học sâu ở chapter 14.

## 19. Hedging strategy khác alpha strategy

Một corporate/portfolio FX hedge có mục tiêu giảm variance hoặc protect liabilities, không phải maximize standalone P/L.

Đánh giá hedge bằng:

```text
risk reduction
cash-flow stability
cost
basis
liquidity
```

Không nên gọi hedge “thất bại” chỉ vì position hedge mất tiền khi underlying exposure tăng giá.

## 20. Signal combination

Có thể combine:

```text
Carry
Momentum
Value
Macro regime
```

Nhưng combination cần tránh double counting.

Ví dụ high-yield currency có thể đồng thời đang trong uptrend; carry và momentum signals correlated trong một regime.

## 21. Composite score

Một cách:

```text
Score = w1*Carry_z + w2*Momentum_z + w3*Value_z
```

Nhưng weights tạo estimation risk.

Nên test:

- equal weights;
- broad stable ranges;
- walk-forward weights;
- sensitivity to normalization.

## 22. Ranking vs absolute signal

Cross-sectional strategies thường rank currencies:

```text
Top quantile → long
Bottom quantile → short
```

Điều này tạo relative portfolio nhưng có turnover và concentration implications.

## 23. Volatility scaling

Để risk across pairs comparable, position size có thể scale inversely với volatility:

```text
Weight_i ∝ Signal_i / Volatility_i
```

Nhưng volatility estimate lags shocks. Stress cap vẫn cần.

## 24. Risk parity không tạo alpha

Equalizing risk contribution chỉ là portfolio construction. Nó không làm signals có positive expectancy.

Alpha hypothesis và risk allocation phải tách riêng.

## 25. Currency basket exposure

Nếu trade nhiều pairs, nên convert sang underlying currency exposures.

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

có concentrated short-USD factor.

Portfolio optimizer phải nhìn factor/currency matrix, không chỉ ticket weights.

## 26. Carry + momentum

Một practical research question:

> Carry signal có tốt hơn khi aligned với momentum không?

Test conditional groups:

```text
High carry + positive momentum
High carry + negative momentum
Low carry + positive momentum
Low carry + negative momentum
```

Sau đó so distribution net of cost.

Không assume combination better trước test.

## 27. Value + momentum

Value có thể bắt falling knife; momentum có thể buy expensive currency.

Combination đôi khi dùng momentum làm timing filter cho long-horizon value.

Nhưng filter có thể làm giảm sample size và tăng data-mining risk.

## 28. Regime-conditioned strategy

Một strategy có thể chỉ active khi:

```text
volatility below threshold
policy divergence high
liquidity normal
```

Conditioning phải có economic reason và được xác định trước, nếu không rất dễ overfit.

## 29. Strategy turnover

Turnover quyết định sensitivity với cost.

```text
Annual turnover
× average all-in cost
```

có thể ăn phần lớn gross alpha.

Signal frequency cao chưa chắc tốt nếu edge per trade nhỏ.

## 30. Capacity

Retail major-FX strategy thường có capacity lớn so với account nhỏ, nhưng không nên bỏ concept.

Capacity giảm khi:

- pair illiquid;
- horizon ngắn;
- order size lớn;
- event execution;
- exotic/offshore instruments.

## 31. Crowding

Một strategy widely known như carry/momentum có thể bị crowded.

Crowding có thể:

- compress expected return;
- increase unwind correlation;
- worsen crash risk.

Không dễ đo trực tiếp, nên positioning/liquidity proxies chỉ là partial information.

## 32. Structural break

FX regimes thay đổi vì:

- monetary framework;
- capital controls;
- market structure;
- intervention;
- crisis;
- regulation.

Một strategy profitable 1990–2010 không tự động representative 2020s.

Validation phải span multiple regimes và emphasize recent relevance without discarding history arbitrarily.

## 33. Strategy decay

Sau deployment, edge có thể giảm vì:

- market adaptation;
- cost changes;
- data relationship breaks;
- crowding;
- implementation drift.

Monitoring cần compare live distribution với research assumptions.

## 34. Attribution by return source

Một FX strategy P/L nên tách nếu có thể:

```text
Spot move
Carry/financing
Transaction cost
Slippage
Hedge effect
Currency conversion
```

Nếu không, trader có thể tưởng signal kiếm tiền trong khi actual return chủ yếu đến từ carry hoặc broad USD beta.

## 35. Benchmark

Strategy cần benchmark phù hợp:

- cash/risk-free;
- passive currency exposure;
- simple carry/momentum rule;
- equal-risk baseline.

Một complex model chỉ có value nếu vượt simple baseline sau cost và complexity penalty.

## 36. Strategy specification template

```text
Universe:
Eligible currency pairs/instruments.

Hypothesis:
Economic/behavioral mechanism.

Signal:
Exact formula and timestamp.

Rebalance:
Frequency and calendar rule.

Sizing:
Volatility/risk constraints.

Execution:
Order/fill assumption.

Financing:
Instrument-specific carry.

Costs:
Spread, commission, slippage.

Risk:
Gross/net leverage, currency caps, drawdown controls.

Validation:
Out-of-sample / walk-forward.

Kill criteria:
Conditions for research review or shutdown.
```

## 37. Không đánh giá bằng win rate

Carry/trend/value có payoff distributions khác nhau.

Cần nhìn:

- expectancy;
- volatility;
- drawdown;
- skew;
- tail loss;
- turnover;
- cost;
- correlation;
- sample size.

Win rate alone gần như không đủ.

## 38. Không chọn strategy vì backtest đẹp nhất

Nếu thử 100 strategy families/settings rồi chọn top Sharpe, estimate bị selection bias.

Chapter 10 sẽ đi sâu cách backtest point-in-time, multiple testing và robustness.

## 39. Checklist

Bạn cần phân biệt được:

1. Carry return và spot return.
2. Time-series và cross-sectional momentum.
3. Value horizon và timing problem.
4. Macro strategy với event strategy.
5. Mean reversion risk khi regime shifts.
6. Alpha signal và portfolio construction.
7. Currency-factor aggregation.
8. Turnover/cost/capacity.
9. Strategy family và parameterized implementation.
10. Vì sao attribution quan trọng.

## Đọc tiếp

→ [10 — Backtesting and point-in-time FX data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)

## Internal links

- [08 — Fundamental and event-driven FX analysis](./08_FUNDAMENTAL_AND_EVENT_DRIVEN_FX_ANALYSIS.md)
- [07 — Technical indicators](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
