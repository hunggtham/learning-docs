# 06 — Price action, trend, range và volatility regimes

Sau năm chương nền, bây giờ mới hợp lý để quay lại chart. Nhưng chart không nên được xem như nơi chứa các “mẫu hình bí mật”. Nó là một cách nén dữ liệu giao dịch theo thời gian. Nhiệm vụ của price action là mô tả trạng thái của thị trường bằng rule đủ rõ để có thể kiểm tra lại.

Mental model:

```text
Price path
→ local structure
→ volatility/liquidity regime
→ hypothesis about participant behavior
→ explicit invalidation
→ executable rule
→ statistical validation
```

## 1. Price action là description trước khi là prediction

Một chart cho biết giá đã di chuyển như thế nào. Từ đó ta có thể mô tả:

- xu hướng (trend);
- dao động trong biên (range);
- breakout;
- pullback;
- compression;
- volatility expansion;
- gap/jump;
- phản ứng quanh vùng giá.

Nhưng description không tự động biến thành edge. Một pattern chỉ có giá trị khi quy tắc nhận diện và outcome sau đó có thể được định nghĩa đủ rõ để kiểm tra.

Ví dụ, “higher high và higher low” là description. Nó chỉ trở thành strategy hypothesis khi thêm:

```text
Definition of swing
Entry rule
Invalidation rule
Holding horizon
Cost model
Exit rule
```

## 2. Trend là khái niệm phụ thuộc horizon

EUR/USD có thể:

```text
Daily chart: uptrend
4H chart: range
15m chart: downtrend
```

Không có mâu thuẫn. Mỗi horizon đang nhìn một thành phần khác của price path.

Vì vậy câu “market đang trend” chưa đủ. Phải ghi rõ:

```text
Instrument
Timeframe / sampling interval
Lookback
Trend definition
```

Nếu đổi timeframe sau khi thấy kết quả, rất dễ rơi vào hindsight.

## 3. Trend có thể được định nghĩa bằng nhiều rule

Ví dụ:

```text
Price > moving average
Moving-average slope > 0
Higher-high / higher-low sequence
Positive time-series momentum
Breakout above N-period high
```

Các rule trên không hoàn toàn giống nhau. Chúng có thể nhận diện trend ở thời điểm khác nhau.

Do đó không nên tranh luận “định nghĩa trend nào đúng tuyệt đối”. Hãy hỏi:

> Định nghĩa nào phù hợp với hypothesis và dữ liệu, và nó có ổn định ngoài mẫu không?

## 4. Range là gì?

Range không đơn giản là “giá đi ngang”. Một operational definition có thể dựa trên:

- directional return nhỏ so với realized volatility;
- repeated mean crossings;
- low trend strength;
- bounded high/low zone;
- failed breakouts;
- compressed distribution của returns.

Range strategy thường đặt cược rằng price displacement hiện tại chưa tạo một persistent repricing process.

Nhưng range có thể kết thúc đột ngột khi new information xuất hiện.

## 5. Trend và mean reversion có thể cùng tồn tại

Một common mistake là coi trend-following và mean-reversion là hai worldview loại trừ nhau.

Trên thực tế:

```text
Long horizon: trend
Short horizon: pullback / mean reversion
```

hoặc ngược lại.

Market có thể trend trong nhiều tuần nhưng vẫn có intraday oscillation quanh local mean. Strategy phải xác định horizon của edge.

## 6. Breakout là transition hypothesis

Breakout strategy không nên được hiểu là:

> Giá vượt resistance nên chắc chắn tiếp tục.

Nó là hypothesis rằng:

```text
Price leaves prior equilibrium/range
→ new information or order imbalance persists
→ continuation probability/payoff exceeds false-break cost
```

Cần định nghĩa:

- breakout level;
- trigger side (bid/ask/mid);
- minimum penetration;
- close-confirmation hay intrabar;
- entry delay;
- false-break definition;
- stop/invalidation;
- time stop.

## 7. False breakout không phải exception hiếm

Nếu một level rõ ràng được nhiều participant theo dõi, quanh level đó có thể tập trung:

- stop orders;
- breakout entries;
- take-profit orders;
- liquidity provision;
- hedging flow.

Price có thể vượt level, kích hoạt flow rồi quay lại. Đây là market mechanism bình thường, không cần giả định manipulation.

Một strategy breakout phải sống sót sau distribution của false breakouts.

## 8. Pullback

Pullback strategy giả định trend hoặc repricing process còn tồn tại nhưng price tạm thời retrace.

Các câu hỏi cần formalize:

```text
How is trend defined?
How deep can pullback be?
What makes pullback invalid?
What event/news can change regime?
What is expected continuation horizon?
```

Nếu không formalize, mọi reversal nhỏ đều có thể được gọi là “healthy pullback” sau khi biết kết quả.

## 9. Support và resistance nên xem là vùng xác suất

Một mức price cũ có thể quan trọng vì:

- previous inventory;
- trapped positioning;
- benchmark/fixing interest;
- option-related hedging;
- psychologically salient round number;
- prior high/low;
- institutional execution interest.

Nhưng không có lý do để giả định một đường pixel-level sẽ luôn được bảo vệ.

Operationally, nên nghĩ:

```text
zone + tolerance + reaction rule
```

thay vì một con số tuyệt đối.

## 10. Swing high / swing low

Swing là cách nén local turning points. Nhưng swing phụ thuộc definition.

Ví dụ fractal rule:

```text
Swing High at t
if High_t > highs of k bars before and after
```

Rule này có look-ahead nếu dùng future bars. Trong live system, swing chỉ được xác nhận sau `k` bars.

Đây là ví dụ điển hình của **look-ahead bias** khi biến visual pattern thành backtest.

## 11. Market structure labels phải có deterministic rule

Các nhãn như:

- BOS (break of structure);
- CHoCH (change of character);
- liquidity sweep;
- order block;
- fair value gap;

có thể dùng như descriptive vocabulary. Nhưng để research cần chuyển thành code/rule rõ ràng.

Ví dụ “liquidity sweep” có thể định nghĩa:

```text
Price trades beyond prior N-bar extreme
then closes back inside range within M bars
with move size > threshold
```

Khi đó mới có thể đo frequency, expectancy và regime dependence.

## 12. Volatility là state variable trung tâm

Volatility không chỉ là “market chạy mạnh”. Nó ảnh hưởng:

- stop distance;
- expected move;
- transaction cost;
- leverage;
- margin stress;
- breakout probability;
- mean-reversion behavior;
- option pricing.

Cùng một signal có thể cần size khác hoàn toàn ở low-vol và high-vol regime.

## 13. Realized volatility

Một cách cơ bản:

```text
r_t = ln(P_t / P_{t-1})
```

Sau đó estimate độ lệch chuẩn của returns trên window.

Annualization gần đúng:

```text
σ_annual ≈ σ_period × √N
```

Nhưng FX returns có volatility clustering và fat tails, nên square-root scaling chỉ là approximation.

## 14. ATR

**Average True Range (ATR)** đo average trading range theo price units.

True Range thường xét max của:

```text
High - Low
|High - Previous Close|
|Low - Previous Close|
```

ATR hữu ích để normalize stop/position sizing theo current movement scale.

Nhưng ATR không nói hướng. Nó chỉ mô tả magnitude của movement.

## 15. Volatility clustering

Market thường có:

```text
high-vol periods followed by high-vol periods
low-vol periods followed by low-vol periods
```

Điều này làm volatility regime có persistence.

Một strategy dùng constant stop hoặc constant leverage bất chấp regime có thể bị overleveraged khi volatility chuyển cao.

## 16. Compression và expansion

Một common market process:

```text
volatility contracts
→ participants accumulate positions / information uncertainty resolves
→ catalyst or flow arrives
→ volatility expands
```

Nhưng compression không đảm bảo breakout direction hoặc profitability. Strategy phải estimate conditional distribution.

## 17. Range-normalized movement

Thay vì nói:

```text
EUR/USD moved 70 pips
```

hãy so với recent volatility:

```text
Move / ATR
Move / realized sigma
```

70 pips có thể là rất lớn trong low-vol regime nhưng bình thường trong crisis regime.

## 18. Multi-timeframe analysis — dùng hierarchy, không narrative

Một cách có kỷ luật:

```text
Higher timeframe: regime/context
Trading timeframe: signal
Lower timeframe: execution only if pre-specified
```

Không nên mở thêm timeframe chỉ để tìm confirmation sau khi setup không rõ.

Rule phải được xác định trước, ví dụ:

```text
Daily trend > 0
4H pullback condition true
1H execution trigger
```

## 19. Candlestick patterns

Doji, engulfing, pin bar, inside bar... chỉ là cách phân loại OHLC sequence.

Chúng không có edge chỉ vì có tên.

Muốn kiểm tra pin bar cần formalize:

```text
body / total range
upper wick ratio
lower wick ratio
location in prior distribution
volatility regime
future horizon
```

Sau đó mới đo outcome.

## 20. Chart pattern và multiple testing

Nếu thử:

```text
20 candlestick patterns
× 10 pairs
× 8 timeframes
× 5 stop rules
× 5 exits
```

đã có hàng chục nghìn combinations. Một số sẽ đẹp chỉ do chance.

Vì vậy visual pattern research phải nối với multiple-testing control và out-of-sample validation ở chapter 10.

## 21. Price action quanh news

Cùng một breakout có meaning khác nếu xảy ra:

- vài phút trước CPI;
- ngay sau central-bank surprise;
- trong low-liquidity rollover;
- trong normal London session.

Price structure không nên tách khỏi event/liquidity context.

## 22. Regime là latent state, không phải nhãn tuyệt đối

Các regime thường dùng:

```text
Trend / Range
High Vol / Low Vol
Risk-on / Risk-off
Policy divergence / convergence
Event-driven / normal
Liquidity-stress / normal
```

Không regime label nào quan sát trực tiếp hoàn hảo. Ta infer từ data.

Vì vậy regime classifier cũng có uncertainty và lag.

## 23. Regime transition là nơi strategy dễ gãy

Trend-following thường khó ở transition sang choppy range. Mean-reversion thường nguy hiểm khi range chuyển sang persistent trend.

Risk process nên theo dõi:

```text
signal degradation
volatility shift
correlation shift
spread shift
drawdown speed
```

Không chỉ cumulative P/L.

## 24. Hindsight charting

Sau khi market move mạnh, rất dễ vẽ:

- support đúng chỗ;
- trendline đẹp;
- order block hợp lý;
- “liquidity sweep” trước move.

Để tránh hindsight, research phải lưu **state tại thời điểm quyết định**.

Một rule chỉ hợp lệ nếu trader/model có thể biết nó bằng dữ liệu có sẵn lúc đó.

## 25. Trendline

Trendline là geometric summary của selected pivots. Vấn đề là pivot selection có thể subjective.

Nếu muốn backtest:

```text
How are pivots chosen?
How many points define line?
What tolerance counts as touch?
How is line updated over time?
```

Nếu không trả lời được, chart reading vẫn hữu ích cho discretionary review nhưng chưa thành reproducible strategy.

## 26. Fibonacci levels

Fibonacci retracement thường được dùng như reference levels. Tuy nhiên con số 38.2%, 50%, 61.8% tự nó không tạo causal mechanism.

Nếu nghiên cứu, cần hỏi:

```text
Does conditional outcome differ from nearby arbitrary levels?
Across which pairs/timeframes/regimes?
After costs?
```

Nếu không, level có thể chỉ là coordination convention hoặc hindsight artifact.

## 27. Round numbers

Round numbers như `1.1000` có thể thu hút attention vì human/institutional quoting conventions và order clustering.

Nhưng “round number” nên được test bằng distance normalization và control levels, không mặc định là support/resistance mạnh.

## 28. Price action và order flow

OHLC là compressed result của order flow. Hai bars giống nhau có thể được tạo bởi different intrabar paths.

Ví dụ cùng candle:

```text
Open 100
High 105
Low 95
Close 101
```

không cho biết chắc price đi `100→105→95→101` hay `100→95→105→101`.

Nếu strategy phụ thuộc sequence intrabar, bar data không đủ.

## 29. A robust price-action hypothesis

Ví dụ:

```text
Hypothesis:
After multi-day compression, a break accompanied by volatility expansion may continue because new information/order imbalance creates persistent repricing.

Definition:
Compression = N-day realized vol percentile < X.
Break = close beyond prior M-day high/low by threshold Y.

Entry:
Next bar open / executable rule.

Invalidation:
Return inside prior range by Z.

Risk:
Volatility-scaled position size.

Validation:
Walk-forward across pairs and regimes with realistic cost.
```

Đây là cách biến “breakout” từ từ khóa chart thành research object.

## 30. Checklist trước khi học indicators

Bạn cần phân biệt được:

1. Description và prediction.
2. Trend ở các horizon khác nhau.
3. Breakout hypothesis và false breakout.
4. Range/mean reversion và regime transition.
5. Volatility level và direction.
6. Look-ahead bias khi xác nhận swing/pattern.
7. Subjective chart annotation và deterministic rule.
8. Vì sao OHLC không chứa đầy đủ intrabar path.
9. Vì sao multiple testing làm pattern đẹp dễ xuất hiện ngẫu nhiên.

## Đọc tiếp

→ [07 — Technical indicators as data transformations](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)

## Internal links

- [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)
- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
