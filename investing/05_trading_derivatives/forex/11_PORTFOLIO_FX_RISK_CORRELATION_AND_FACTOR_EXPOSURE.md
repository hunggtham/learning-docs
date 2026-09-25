# 11 — Portfolio FX risk, correlation và factor exposure

Một danh sách nhiều trade không tự động là một danh mục đa dạng hóa. Trong Forex, cùng một currency hoặc cùng một macro factor có thể xuất hiện lặp lại dưới nhiều ticker khác nhau. Vì vậy risk phải được tổng hợp ở cấp **currency, factor, strategy và liquidity**, không chỉ theo từng ticket.

Mental model:

```text
Positions
→ currency decomposition
→ factor exposure
→ covariance / stress dependence
→ portfolio loss distribution
→ risk budget and constraints
```

## 1. Ticket view dễ che giấu exposure

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

Ba trade khác nhau nhưng đều có thành phần:

```text
short USD
```

Nếu USD tăng mạnh, cả ba có thể lỗ cùng lúc.

Đếm `3 trades` không nói được diversification.

## 2. Currency decomposition

Mỗi pair có thể biểu diễn bằng vector exposure.

Ví dụ long EUR/USD:

```text
+EUR
-USD
```

Long USD/JPY:

```text
+USD
-JPY
```

Portfolio nên aggregate net exposure theo từng currency sau khi quy đổi về common risk units.

## 3. Notional aggregation chưa đủ

Hai positions có cùng notional nhưng volatility khác nhau.

Ví dụ:

```text
100k EUR/USD
100k USD/TRY
```

không thể coi là same risk.

Risk-normalized exposure cần volatility, liquidity và tail behavior.

## 4. Gross và net exposure

```text
Gross Exposure = Σ |notional_i|
Net Exposure = directional aggregate after offsets
```

Net nhỏ không có nghĩa gross risk nhỏ.

Một long EUR/USD và short EUR/JPY có thể net EUR một phần nhưng tạo USD/JPY cross exposure và execution risk ở hai legs.

## 5. Correlation là time-varying

Correlation ước lượng từ historical returns không phải constant.

Trong stress:

```text
correlations can converge
liquidity can deteriorate together
```

Do đó full-sample correlation thường đánh giá thấp crisis dependence.

## 6. Covariance matrix

Với return vector `r` và weights `w`:

```text
Portfolio Variance = w' Σ w
```

`Σ` là covariance matrix.

Công thức hữu ích nhưng kết quả phụ thuộc estimate window, data frequency và regime.

## 7. Estimation error

Covariance matrix từ sample ngắn có thể unstable, đặc biệt với nhiều instruments.

Một optimizer có thể tạo extreme weights từ small estimation errors.

Practical controls:

- shrinkage;
- weight caps;
- simpler factor model;
- stress scenarios.

## 8. Factor model

FX returns có thể liên quan đến factors như:

- broad USD;
- carry;
- global risk sentiment;
- commodity exposure;
- rate differential;
- regional Asia risk;
- volatility/liquidity.

Thay vì chỉ pair correlation, có thể estimate sensitivity tới factors.

## 9. Dollar factor

Nhiều portfolios vô tình trở thành USD bet.

Nếu long EUR/USD, GBP/USD, AUD/USD và short USD/CHF, portfolio có broad anti-USD exposure.

Performance attribution phải tách broad USD move khỏi skill của từng signal.

## 10. Carry factor

High-yield currencies có thể cùng chịu carry unwind trong risk-off.

Correlation bình thường thấp nhưng tail losses có thể cluster.

## 11. Commodity factor

Currencies của commodity exporters có thể đồng biến với commodity/China/global-growth factors.

Nhưng relationship không cố định và khác theo economy structure.

## 12. Rate factor

Positions nhạy với front-end yield differential có thể cùng react khi global central-bank expectations shift.

Một portfolio nhiều pairs không diversified nếu tất cả đều là cùng một “rates divergence” trade.

## 13. Strategy correlation

Cần nhìn cả correlation giữa **strategies**:

- carry;
- trend;
- mean reversion;
- event;
- value.

Hai strategies trên khác pairs vẫn có thể cùng factor exposure.

## 14. Correlation of losses quan trọng hơn average correlation

Có thể estimate:

- downside correlation;
- tail dependence;
- conditional correlation during high-vol periods.

Risk management quan tâm nhất lúc nhiều positions cùng lỗ.

## 15. Portfolio heat

Một practical metric:

```text
Portfolio Heat
≈ sum of planned losses to stops
```

Nhưng nếu stops correlated/slippage correlated, actual tail loss có thể lớn hơn sum planned loss.

Do đó portfolio heat chỉ là first layer.

## 16. Scenario stress

Stress theo factor:

```text
USD +3%
JPY +5% safe-haven move
global risk-off
oil +20%
front-end US yields +100 bps
KRW liquidity stress
```

Sau đó map positions vào P/L.

Scenario không cần có probability chính xác để hữu ích.

## 17. Historical stress

Replay conceptual periods:

- global financial stress;
- pandemic shock;
- abrupt central-bank repricing;
- peg break;
- geopolitical energy shock.

Nhưng historical scenario không bao phủ mọi future shock.

## 18. VaR

VaR trả lời gần:

> Với model và confidence level, threshold loss là bao nhiêu?

Không phải maximum loss.

FX tails/gaps/liquidity breaks làm VaR dễ underestimate extreme risk nếu model quá Gaussian.

## 19. Expected Shortfall

Expected Shortfall nhìn average loss beyond VaR threshold.

Nó tập trung tail tốt hơn VaR nhưng vẫn model/data dependent.

## 20. Drawdown constraint

Portfolio có thể đặt:

- soft drawdown review;
- hard exposure reduction;
- kill switch.

Threshold phải được thiết kế trước, không tùy cảm xúc sau loss.

## 21. Volatility targeting

Một portfolio có thể scale exposure để giữ target volatility:

```text
Scale ≈ Target Vol / Estimated Vol
```

Nhưng volatility estimate giảm chậm/tăng chậm có lag. Shock có thể xảy ra trước khi model giảm size.

## 22. Leverage cap

Ngoài volatility target, cần cap:

- gross leverage;
- currency concentration;
- strategy concentration;
- illiquid exposure.

Không dựa duy nhất vào covariance optimizer.

## 23. Risk contribution

Marginal risk contribution hỏi:

> Position này thêm bao nhiêu vào portfolio volatility/risk?

Một small notional position có thể đóng góp lớn nếu volatility/correlation cao.

## 24. Risk parity

Risk parity phân bổ để các components đóng góp risk tương tự.

Đây là allocation rule, không đảm bảo return tốt hơn.

## 25. Concentration by currency

Có thể đặt cap theo:

```text
USD
EUR
JPY
GBP
AUD
KRW
...
```

Tính cả direct và synthetic exposures.

## 26. Concentration by macro thesis

Ví dụ nhiều trades đều dựa trên “Fed dovish”. Dù tickers khác, thesis concentration vẫn lớn.

Journal nên tag thesis/factor.

## 27. Event concentration

Nếu portfolio có nhiều USD pairs trước FOMC, event exposure tập trung.

Risk budget nên xét scheduled event cluster.

## 28. Liquidity concentration

Nhiều positions có thể liquid trong normal market nhưng cùng illiquid trong stress.

Need stress:

```text
spread widening
slippage multiplier
partial/no fill
margin increase
```

## 29. Cross-margin và broker dependence

Một broker outage hoặc stop-out rule có thể ảnh hưởng toàn portfolio cùng lúc.

Operational diversification khác market diversification.

## 30. Multiple brokers không tự động safer

Có thể giảm single-platform dependency nhưng tăng:

- reconciliation complexity;
- fragmented margin;
- transfer delay;
- inconsistent execution.

Phải có reason rõ.

## 31. Hedge ratio

Nếu hedge underlying foreign asset exposure:

```text
Hedge Ratio = FX hedge notional / underlying currency exposure
```

100% hedge không luôn optimal nếu underlying exposure thay đổi hoặc hedge cost cao.

## 32. Basis risk

Hedge instrument có thể không perfectly match:

- currency;
- maturity;
- settlement;
- underlying exposure timing.

Residual difference là basis risk.

## 33. Dynamic hedging

Hedge ratio có thể adjust theo:

- asset value;
- risk tolerance;
- hedge cost;
- volatility.

Nhưng frequent rehedging tạo turnover/cost.

## 34. Currency overlay

Institutional portfolio có thể tách asset allocation khỏi currency overlay.

Ví dụ giữ foreign equities nhưng hedge một phần FX exposure bằng forwards.

Điều này cho thấy FX position có thể là risk-management layer, không phải standalone speculative trade.

## 35. Portfolio of strategies

Một robust system có thể combine strategies có different return drivers.

Need assess:

```text
correlation
shared factor exposure
turnover
capacity
crisis behavior
```

Không chỉ individual Sharpe.

## 36. Capital allocation

Allocation có thể dựa trên:

- equal capital;
- equal risk;
- expected return/risk;
- drawdown budget;
- Bayesian/uncertainty-aware estimates.

More complex không luôn better vì expected return estimates rất noisy.

## 37. Rebalancing

Rebalance quá thường → cost cao.

Quá ít → exposure drift.

Need define:

- calendar-based;
- threshold-based;
- event-triggered.

## 38. Stress correlation matrix

Có thể xây covariance riêng cho high-vol observations để so normal vs stress.

Nếu diversification biến mất trong stress, normal matrix không đủ.

## 39. Risk dashboard

Một dashboard tối thiểu:

```text
Equity
Gross leverage
Net currency exposures
Risk by currency
Risk by strategy
Portfolio heat
Realized volatility
Drawdown
Margin headroom
Upcoming event exposure
Liquidity flags
```

## 40. Pre-trade portfolio check

Trước trade mới:

```text
What factor does it add?
How much currency exposure?
How correlated with existing trades?
What happens if common thesis fails?
What is portfolio heat after entry?
What event/liquidity risk is added?
```

## 41. Risk budget không phải profit target

Risk budget giới hạn acceptable loss/exposure. Không nên ép strategy tạo target return bằng tăng leverage.

## 42. Checklist

Bạn cần tự giải thích được:

1. Ticket diversification khác factor diversification.
2. Gross vs net exposure.
3. Currency decomposition.
4. Correlation regime dependence.
5. Portfolio heat limitations.
6. Why VaR is not max loss.
7. Volatility targeting lag.
8. Basis risk trong hedge.
9. Strategy correlation vs pair correlation.
10. Operational concentration.

## Đọc tiếp

→ [12 — Trading journal, review and performance attribution](./12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)

## Internal links

- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [09 — FX strategy families](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
