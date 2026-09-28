# 06 — Price hành động (action / 동작), trend, phạm vi (range / 범위) và volatility regimes

> **Mạch đọc:** Đặt **06 — Price hành động (action / 동작), trend, phạm vi (range / 범위) và volatility regimes** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Price hành động (action / 동작) là description trước khi là prediction** sang **2. Trend là khái niệm phụ thuộc horizon**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Sau năm chương nền, bây giờ mới hợp lý để quay lại chart. Nhưng chart không nên được xem như nơi chứa các “mẫu hình bí mật”. Nó là một cách nén dữ liệu giao dịch theo thời gian. Nhiệm vụ của price hành động (action / 동작) là mô tả trạng thái của thị trường bằng quy tắc (rule / 규칙) đủ rõ để có thể kiểm tra lại.

Mô hình tư duy (mental model / 사고 모델):

```text
Price path
→ local structure
→ volatility/liquidity regime
→ hypothesis about participant behavior
→ explicit invalidation
→ executable rule
→ statistical validation
```

## 1. Price hành động (action / 동작) là description trước khi là prediction

Một chart cho biết giá đã di chuyển như thế nào. Từ đó ta có thể mô tả:

- xu hướng (trend);
- dao động trong biên (range);
- breakout;
- pullback;
- compression;
- volatility expansion;
- gap/jump;
- phản ứng quanh vùng giá.

Nhưng description không tự động biến thành edge. Một mẫu (pattern / 패턴) chỉ có giá trị khi quy tắc nhận diện và kết quả (outcome / 결과) sau đó có thể được định nghĩa đủ rõ để kiểm tra.

Ví dụ, “higher high và higher low” là description. Nó chỉ trở thành chiến lược (strategy / 전략) hypothesis khi thêm:

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

Không có mâu thuẫn. Mỗi horizon đang nhìn một thành phần khác của price đường dẫn (path / 경로).

Vì vậy câu “thị trường (market / 시장) đang trend” chưa đủ. Phải ghi rõ:

```text
Instrument
Timeframe / sampling interval
Lookback
Trend definition
```

Nếu đổi timeframe sau khi thấy kết quả, rất dễ rơi vào hindsight.

## 3. Trend có thể được định nghĩa bằng nhiều quy tắc (rule / 규칙)

Ví dụ:

```text
Price > moving average
Moving-average slope > 0
Higher-high / higher-low sequence
Positive time-series momentum
Breakout above N-period high
```

Các quy tắc (rule / 규칙) trên không hoàn toàn giống nhau. Chúng có thể nhận diện trend ở thời điểm khác nhau.

Do đó không nên tranh luận “định nghĩa trend nào đúng tuyệt đối”. Hãy hỏi:

> Định nghĩa nào phù hợp với hypothesis và dữ liệu, và nó có ổn định ngoài mẫu không?

## 4. phạm vi (range / 범위) là gì?

Phạm vi (range / 범위) không đơn giản là “giá đi ngang”. Một operational definition có thể dựa trên:

- directional return nhỏ so với realized volatility;
- repeated mean crossings;
- low trend strength;
- bounded high/low zone;
- failed breakouts;
- compressed phân phối (distribution / 분포) của returns.

Phạm vi (range / 범위) chiến lược (strategy / 전략) thường đặt cược rằng price displacement hiện tại chưa tạo một persistent repricing tiến trình (process / 프로세스).

Nhưng phạm vi (range / 범위) có thể kết thúc đột ngột khi new thông tin (information / 정보) xuất hiện.

## 5. Trend và mean reversion có thể cùng tồn tại

Một dùng chung (common / 공통) mistake là coi trend-following và mean-reversion là hai worldview loại trừ nhau.

Trên thực tế:

```text
Long horizon: trend
Short horizon: pullback / mean reversion
```

hoặc ngược lại.

Thị trường (market / 시장) có thể trend trong nhiều tuần nhưng vẫn có intraday oscillation quanh cục bộ (local / 로컬) mean. chiến lược (strategy / 전략) phải xác định horizon của edge.

## 6. Breakout là chuyển tiếp (transition / 전이) hypothesis

Breakout chiến lược (strategy / 전략) không nên được hiểu là:

> Giá vượt resistance nên chắc chắn tiếp tục.

Nó là hypothesis rằng:

```text
Price leaves prior equilibrium/range
→ new information or order imbalance persists
→ continuation probability/payoff exceeds false-break cost
```

Cần định nghĩa:

- breakout mức (level / 수준);
- trigger side (bid/ask/mid);
- minimum penetration;
- close-confirmation hay intrabar;
- entry delay;
- false-break definition;
- stop/vô hiệu hóa (invalidation / 무효화);
- thời gian (time / 시간) stop.

## 7. False breakout không phải exception hiếm

Nếu một mức (level / 수준) rõ ràng được nhiều participant theo dõi, quanh mức (level / 수준) đó có thể tập trung:

- stop orders;
- breakout entries;
- take-profit orders;
- liquidity provision;
- hedging luồng (flow / 흐름).

Price có thể vượt mức (level / 수준), kích hoạt luồng (flow / 흐름) rồi quay lại. Đây là thị trường (market / 시장) cơ chế (mechanism / 메커니즘) bình thường, không cần giả định manipulation.

Một chiến lược (strategy / 전략) breakout phải sống sót sau phân phối (distribution / 분포) của false breakouts.

## 8. Pullback

Pullback chiến lược (strategy / 전략) giả định trend hoặc repricing tiến trình (process / 프로세스) còn tồn tại nhưng price tạm thời retrace.

Các câu hỏi cần formalize:

```text
How is trend defined?
How deep can pullback be?
What makes pullback invalid?
What event/news can change regime?
What is expected continuation horizon?
```

Nếu không formalize, mọi reversal nhỏ đều có thể được gọi là “healthy pullback” sau khi biết kết quả.

## 9. hỗ trợ (support / 지원) và resistance nên xem là vùng xác suất

Một mức price cũ có thể quan trọng vì:

- previous inventory;
- trapped positioning;
- benchmark/fixing interest;
- option-related hedging;
- psychologically salient round number;
- prior high/low;
- institutional thực thi (execution / 실행) interest.

Nhưng không có lý do để giả định một đường pixel-level sẽ luôn được bảo vệ.

Operationally, nên nghĩ:

```text
zone + tolerance + reaction rule
```

thay vì một con số tuyệt đối.

## 10. Swing high / swing low

Swing là cách nén cục bộ (local / 로컬) turning points. Nhưng swing phụ thuộc definition.

Ví dụ fractal quy tắc (rule / 규칙):

```text
Swing High at t
if High_t > highs of k bars before and after
```

Quy tắc (rule / 규칙) này có look-ahead nếu dùng future bars. Trong live hệ thống (system / 시스템), swing chỉ được xác nhận sau `k` bars.

Đây là ví dụ điển hình của **look-ahead độ lệch (bias / 편향)** khi biến visual mẫu (pattern / 패턴) thành backtest.

## 11. thị trường (market / 시장) cấu trúc (structure / 구조) labels phải có deterministic quy tắc (rule / 규칙)

Các nhãn như:

- BOS (break of structure);
- CHoCH (change of character);
- liquidity sweep;
- thứ tự (order / 순서) khối (block / 블록);
- fair giá trị (value / 값) gap;

có thể dùng như descriptive vocabulary. Nhưng để research cần chuyển thành mã (code / 코드)/quy tắc (rule / 규칙) rõ ràng.

Ví dụ “liquidity sweep” có thể định nghĩa:

```text
Price trades beyond prior N-bar extreme
then closes back inside range within M bars
with move size > threshold
```

Khi đó mới có thể đo frequency, expectancy và regime dependence.

## 12. Volatility là trạng thái (state / 상태) variable trung tâm

Volatility không chỉ là “thị trường (market / 시장) chạy mạnh”. Nó ảnh hưởng:

- stop distance;
- expected move;
- giao dịch (transaction / 트랜잭션) chi phí (cost / 비용);
- leverage;
- margin stress;
- breakout xác suất (probability / 확률);
- mean-reversion hành vi (behavior / 동작);
- option pricing.

Cùng một tín hiệu (signal / 신호) có thể cần kích thước (size / 크기) khác hoàn toàn ở low-vol và high-vol regime.

## 13. Realized volatility

Một cách cơ bản:

```text
r_t = ln(P_t / P_{t-1})
```

Sau đó estimate độ lệch chuẩn của returns trên cửa sổ (window / 윈도우).

Annualization gần đúng:

```text
σ_annual ≈ σ_period × √N
```

Nhưng FX returns có volatility clustering và fat tails, nên square-root scaling chỉ là approximation.

## 14. ATR

**Average True phạm vi (range / 범위) (ATR)** đo average trading phạm vi (range / 범위) theo price units.

True phạm vi (range / 범위) thường xét max của:

```text
High - Low
|High - Previous Close|
|Low - Previous Close|
```

ATR hữu ích để normalize stop/position sizing theo hiện tại (current / 현재) movement quy mô (scale / 규모).

Nhưng ATR không nói hướng. Nó chỉ mô tả magnitude của movement.

## 15. Volatility clustering

Thị trường (market / 시장) thường có:

```text
high-vol periods followed by high-vol periods
low-vol periods followed by low-vol periods
```

Điều này làm volatility regime có persistence.

Một chiến lược (strategy / 전략) dùng constant stop hoặc constant leverage bất chấp regime có thể bị overleveraged khi volatility chuyển cao.

## 16. Compression và expansion

Một dùng chung (common / 공통) thị trường (market / 시장) tiến trình (process / 프로세스):

```text
volatility contracts
→ participants accumulate positions / information uncertainty resolves
→ catalyst or flow arrives
→ volatility expands
```

Nhưng compression không đảm bảo breakout direction hoặc profitability. chiến lược (strategy / 전략) phải estimate conditional phân phối (distribution / 분포).

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

## 18. Multi-timeframe phân tích (analysis / 분석) — dùng hierarchy, không narrative

Một cách có kỷ luật:

```text
Higher timeframe: regime/context
Trading timeframe: signal
Lower timeframe: execution only if pre-specified
```

Không nên mở thêm timeframe chỉ để tìm confirmation sau khi setup không rõ.

Quy tắc (rule / 규칙) phải được xác định trước, ví dụ:

```text
Daily trend > 0
4H pullback condition true
1H execution trigger
```

## 19. Candlestick patterns

Doji, engulfing, pin bar, inside bar... chỉ là cách phân loại OHLC chuỗi (sequence / 시퀀스).

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

Sau đó mới đo kết quả (outcome / 결과).

## 20. Chart mẫu (pattern / 패턴) và multiple testing

Nếu thử:

```text
20 candlestick patterns
× 10 pairs
× 8 timeframes
× 5 stop rules
× 5 exits
```

đã có hàng chục nghìn combinations. Một số sẽ đẹp chỉ do chance.

Vì vậy visual mẫu (pattern / 패턴) research phải nối với multiple-testing điều khiển (control / 제어) và out-of-sample kiểm tra hợp lệ (validation / 검증) ở chapter 10.

## 21. Price hành động (action / 동작) quanh news

Cùng một breakout có meaning khác nếu xảy ra:

- vài phút trước CPI;
- ngay sau central-bank surprise;
- trong low-liquidity rollover;
- trong normal London session.

Price cấu trúc (structure / 구조) không nên tách khỏi sự kiện (event / 이벤트)/liquidity ngữ cảnh (context / 맥락).

## 22. Regime là latent trạng thái (state / 상태), không phải nhãn tuyệt đối

Các regime thường dùng:

```text
Trend / Range
High Vol / Low Vol
Risk-on / Risk-off
Policy divergence / convergence
Event-driven / normal
Liquidity-stress / normal
```

Không regime label nào quan sát trực tiếp hoàn hảo. Ta infer từ dữ liệu (data / 데이터).

Vì vậy regime classifier cũng có bất định (uncertainty / 불확실성) và lag.

## 23. Regime chuyển tiếp (transition / 전이) là nơi chiến lược (strategy / 전략) dễ gãy

Trend-following thường khó ở chuyển tiếp (transition / 전이) sang choppy phạm vi (range / 범위). Mean-reversion thường nguy hiểm khi phạm vi (range / 범위) chuyển sang persistent trend.

Rủi ro (risk / 위험) tiến trình (process / 프로세스) nên theo dõi:

```text
signal degradation
volatility shift
correlation shift
spread shift
drawdown speed
```

Không chỉ cumulative P/L.

## 24. Hindsight charting

Sau khi thị trường (market / 시장) move mạnh, rất dễ vẽ:

- hỗ trợ (support / 지원) đúng chỗ;
- trendline đẹp;
- thứ tự (order / 순서) khối (block / 블록) hợp lý;
- “liquidity sweep” trước move.

Để tránh hindsight, research phải lưu **trạng thái (state / 상태) tại thời điểm quyết định**.

Một quy tắc (rule / 규칙) chỉ hợp lệ nếu trader/mô hình (model / 모델) có thể biết nó bằng dữ liệu có sẵn lúc đó.

## 25. Trendline

Trendline là geometric summary của selected pivots. Vấn đề là pivot selection có thể subjective.

Nếu muốn backtest:

```text
How are pivots chosen?
How many points define line?
What tolerance counts as touch?
How is line updated over time?
```

Nếu không trả lời được, chart reading vẫn hữu ích cho discretionary rà soát (review / 검토) nhưng chưa thành reproducible chiến lược (strategy / 전략).

## 26. Fibonacci levels

Fibonacci retracement thường được dùng như tham chiếu (reference / 참조) levels. Tuy nhiên con số 38.2%, 50%, 61.8% tự nó không tạo nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘).

Nếu nghiên cứu, cần hỏi:

```text
Does conditional outcome differ from nearby arbitrary levels?
Across which pairs/timeframes/regimes?
After costs?
```

Nếu không, mức (level / 수준) có thể chỉ là coordination convention hoặc hindsight sản phẩm tạo ra (artifact / 산출물).

## 27. Round numbers

Round numbers như `1.1000` có thể thu hút attention vì human/institutional quoting conventions và thứ tự (order / 순서) clustering.

Nhưng “round number” nên được kiểm thử (test / 테스트) bằng distance normalization và điều khiển (control / 제어) levels, không mặc định là hỗ trợ (support / 지원)/resistance mạnh.

## 28. Price hành động (action / 동작) và thứ tự (order / 순서) luồng (flow / 흐름)

OHLC là compressed kết quả (result / 결과) của thứ tự (order / 순서) luồng (flow / 흐름). Hai bars giống nhau có thể được tạo bởi different intrabar paths.

Ví dụ cùng candle:

```text
Open 100
High 105
Low 95
Close 101
```

không cho biết chắc price đi `100→105→95→101` hay `100→95→105→101`.

Nếu chiến lược (strategy / 전략) phụ thuộc chuỗi (sequence / 시퀀스) intrabar, bar dữ liệu (data / 데이터) không đủ.

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

Đây là cách biến “breakout” từ từ khóa chart thành research đối tượng (object / 객체).

## 30. Checklist trước khi học indicators

Bạn cần phân biệt được:

1. Description và prediction.
2. Trend ở các horizon khác nhau.
3. Breakout hypothesis và false breakout.
4. phạm vi (range / 범위)/mean reversion và regime chuyển tiếp (transition / 전이).
5. Volatility mức (level / 수준) và direction.
6. Look-ahead độ lệch (bias / 편향) khi xác nhận swing/mẫu (pattern / 패턴).
7. Subjective chart annotation và deterministic quy tắc (rule / 규칙).
8. Vì sao OHLC không chứa đầy đủ intrabar đường dẫn (path / 경로).
9. Vì sao multiple testing làm mẫu (pattern / 패턴) đẹp dễ xuất hiện ngẫu nhiên.

## Đọc tiếp

→ [07 — Technical indicators as data transformations](./07_TECHNICAL_INDICATORS_AS_DATA_TRANSFORMATIONS.md)

## Nội bộ (internal / 내부) links

- [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)
- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy research and robustness](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)

> **Bàn giao:** Sau **nội bộ (internal / 내부) links**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 MARKET STRUCTURE AND INSTRUMENTS](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
