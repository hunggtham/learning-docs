# Thực thi lệnh, cấu trúc vi mô thị trường và danh mục giao dịch

> Tín hiệu tốt chưa đủ. Một chiến lược chỉ tạo lợi thế thật khi lệnh được thực thi với chi phí hợp lý, trạng thái tài khoản chính xác và rủi ro được quản lý ở cấp toàn danh mục. Chương này nối **sổ lệnh → spread → slippage → market impact → execution algorithm → portfolio risk → TCA → operational safety**.

# Phần I — Trading system có ba lớp

## 1. Signal, sizing và execution

Một hệ thống tối thiểu gồm:

```text
Signal Generation
→ Risk Sizing
→ Execution
```

Nếu expectancy trước chi phí là `+0,12R` nhưng tổng spread, commission và slippage là `0,10R`, phần lớn edge đã biến mất.

Vì vậy thực thi lệnh không phải hậu cần; nó là một phần của kinh tế chiến lược.

## 2. Giá quyết định và giá thực thi

**Giá quyết định (decision price)** là mức giá khi chiến lược quyết định giao dịch.

**Giá thực thi (execution price)** là giá fill thực tế.

Khoảng cách giữa hai mức có thể đến từ:

- spread;
- latency;
- market impact;
- delay;
- missed fill;
- market movement.

Đây là nền tảng của **implementation shortfall**.

# Phần II — Limit Order Book

## 3. Sổ lệnh

Limit Order Book chứa các lệnh mua/bán đang chờ ở nhiều mức giá.

```text
Best Bid = giá mua cao nhất
Best Ask = giá bán thấp nhất
Spread = Best Ask - Best Bid
```

**Depth** cho biết lượng lệnh có sẵn ở nhiều mức giá.

Spread hẹp nhưng depth rất mỏng vẫn có thể gây slippage lớn cho lệnh lớn.

## 4. Price-time priority

Nhiều venue ưu tiên:

```text
Giá tốt hơn trước
→ nếu cùng giá, lệnh vào trước được ưu tiên trước
```

Do đó backtest giả định “giá chạm limit = chắc chắn fill” thường quá lạc quan.

## 5. Queue position

Xác suất fill phụ thuộc:

- lượng lệnh đứng trước;
- cancellation;
- incoming market orders;
- venue rules;
- thời gian chờ.

Với strategy rất ngắn hạn, queue position có thể quan trọng ngang signal.

## 6. Maker và taker

**Maker** cung cấp thanh khoản bằng lệnh chờ. **Taker** lấy thanh khoản bằng lệnh chủ động.

Maker có thể tiết kiệm spread nhưng chịu:

- non-fill risk;
- adverse selection;
- opportunity cost.

Taker có khả năng fill nhanh hơn nhưng trả spread và có thể chịu impact.

# Phần III — Các loại lệnh

## 7. Market order

Market order ưu tiên được thực thi, không bảo đảm giá.

Trong thị trường mỏng hoặc khi có tin lớn, fill có thể xa mức nhìn thấy trước khi gửi lệnh.

## 8. Marketable limit

Marketable limit đi qua spread nhưng đặt giới hạn giá tệ nhất chấp nhận được.

Nó giảm nguy cơ fill cực xấu nhưng có thể chỉ fill một phần trong thị trường chạy nhanh.

## 9. Passive limit

Passive limit kiểm soát giá nhưng có thể không được fill.

Một vấn đề quan trọng là **adverse selection**: lệnh có thể được fill nhiều nhất đúng lúc giá sắp tiếp tục đi ngược vị thế.

## 10. Stop order

Stop chỉ kích hoạt lệnh khi đạt điều kiện; trigger price không phải giá fill bảo đảm.

Gap có thể biến kế hoạch `-1R` thành lỗ lớn hơn đáng kể.

## 11. Stop-limit

Stop-limit kiểm soát giá tối đa chấp nhận được nhưng có nguy cơ không thoát được.

Vì vậy nó không tự động “an toàn hơn” stop-market.

## 12. Time-in-force

Một số loại phổ biến:

- DAY;
- GTC;
- IOC;
- FOK.

Time-in-force là một phần của logic execution, không chỉ là tùy chọn giao diện.

## 13. Partial fill

Lệnh chỉ fill một phần làm actual exposure khác intended exposure.

Execution engine phải theo dõi:

```text
Requested Quantity
Filled Quantity
Remaining Quantity
Actual Position
```

trước khi gửi lệnh thay thế.

## 14. Multi-leg execution

Option spread hoặc hedge nhiều chân có thể được giao dịch như package hoặc từng leg.

Thực thi từng chân tạo **legging risk**: chân đầu đã fill nhưng chân sau chạy khỏi giá dự kiến.

# Phần IV — Spread và thanh khoản

## 15. Vì sao spread tồn tại?

Spread bù cho liquidity provider các rủi ro như:

- adverse selection;
- inventory risk;
- volatility;
- capital usage;
- venue fee.

Khi uncertainty tăng, spread thường rộng hơn.

## 16. Quoted spread và effective spread

**Quoted spread** là bid–ask đang hiển thị.

**Effective spread** đo chi phí thực tế so với midpoint hoặc benchmark.

Price improvement có thể làm effective spread thấp hơn quote; fast market có thể làm nó cao hơn.

## 17. Realized spread

Realized spread đo phần spread còn thực sự giữ được sau một khoảng thời gian.

Nó giúp phân biệt:

```text
Spread Earned
và
Loss from Adverse Selection
```

## 18. Liquidity là khái niệm nhiều chiều

Cần nhìn cùng:

- spread;
- depth;
- resilience;
- turnover;
- impact;
- time-to-exit.

Volume cao không bảo đảm một order lớn có thể thoát với chi phí thấp.

## 19. Hidden và iceberg liquidity

Một số lệnh chỉ hiển thị một phần quantity. Vì vậy visible book có thể thấp hơn liquidity thật.

Ngược lại, displayed liquidity cũng có thể biến mất nhanh; snapshot không phải bảo đảm.

## 20. Dark pool và off-exchange venue

Dark venue giảm khả năng order lớn tự tiết lộ ý định trước giao dịch nhưng làm phân tích price discovery phức tạp hơn.

## 21. Venue fragmentation

Một security có thể giao dịch ở nhiều venue. Routing tốt phải cân nhắc:

```text
Price
Fee / Rebate
Queue
Latency
Fill Probability
```

Giá hiển thị tốt nhất chưa chắc tạo execution thực tế tốt nhất.

# Phần V — Price discovery và auction

## 22. Price discovery

Price discovery là quá trình thông tin mới được phản ánh vào giá.

Tùy thị trường, thông tin có thể xuất hiện trước ở:

- futures;
- ETF;
- options;
- FX;
- cash market.

Không nên dùng reference price đã stale như fair value hiện tại.

## 23. Opening auction

Phiên mở cửa gom thông tin qua đêm và lệnh chờ.

Backtest “mua tại open” cần mô hình hóa gap và cơ chế auction thực tế.

## 24. Closing auction

Closing auction thường có volume lớn vì:

- index funds;
- benchmark tracking;
- rebalance;
- institutional flows.

Official close không có nghĩa mọi trader đều có thể fill đúng giá đó.

## 25. Intraday seasonality

Volume và volatility có pattern theo thời gian trong ngày.

Equity thường có volume cao hơn đầu/cuối phiên; FX chịu ảnh hưởng Asia/London/New York session.

Cost model nên phản ánh time-of-day.

# Phần VI — Slippage và market impact

## 26. Slippage

Slippage là chênh lệch giữa giá kỳ vọng và giá thực thi.

Nó phụ thuộc:

- volatility;
- urgency;
- size/depth;
- latency;
- order type;
- event risk.

Không nên dùng một con số slippage cố định cho mọi regime.

## 27. Implementation shortfall

Implementation shortfall đo khoảng cách giữa danh mục giả định tại decision price và kết quả thật sau execution.

Nó có thể gồm:

```text
Commission
+ Spread
+ Delay Cost
+ Market Impact
+ Opportunity Cost
```

## 28. Opportunity cost

Một passive order không fill có commission bằng 0 nhưng vẫn có cost nếu bỏ lỡ move có lợi.

Chi phí “không giao dịch được” cũng là execution cost.

## 29. Market impact

Order của chính bạn có thể làm giá di chuyển.

Impact thường tăng khi:

- order lớn so với volume;
- depth thấp;
- urgency cao;
- volatility cao.

Capacity của strategy bị giới hạn bởi impact, không chỉ account balance.

## 30. Temporary và permanent impact

Temporary impact có thể hồi lại sau khi order hoàn tất.

Permanent impact phản ánh thông tin hoặc signaling đã được market hấp thụ.

Execution tốt cố giảm phần impact không cần thiết.

## 31. Participation rate

```text
Participation Rate
= Own Volume / Market Volume
```

Participation cao giúp hoàn tất nhanh nhưng thường làm impact và signaling risk lớn hơn.

## 32. Capacity

Capacity trả lời:

```text
Có thể chạy bao nhiêu vốn trước khi cost ăn hết edge?
```

Cần xem turnover, ADV, holding period, participation và stressed exit.

# Phần VII — Execution algorithms

## 33. TWAP

TWAP chia lệnh tương đối đều theo thời gian.

Đơn giản nhưng không thích nghi tốt với liquidity thay đổi.

## 34. VWAP

VWAP phân bổ execution theo profile volume dự kiến hoặc thực tế.

Đánh bại VWAP không đồng nghĩa investment decision ban đầu tốt; nó chỉ đo execution relative to benchmark.

## 35. POV

Percentage-of-Volume giữ tỷ lệ tham gia gần cố định so với market volume.

Nó thích nghi với activity nhưng có thể giao dịch nhiều hơn đúng lúc volume/volatility tăng mạnh.

## 36. Implementation-shortfall algorithm

Loại algorithm này cân bằng:

```text
Market Impact của giao dịch nhanh
vs
Price Risk của việc chờ
```

Urgency cao → front-load nhiều hơn.

## 37. Arrival price

Arrival price là giá lúc bắt đầu execution và phù hợp khi alpha có decay nhanh.

Benchmark phải được chọn trước khi nhìn kết quả.

## 38. Smart Order Routing

SOR chọn venue dựa trên price, fee, queue, latency và fill probability.

Mục tiêu là realized execution tốt hơn, không chỉ displayed price tốt hơn.

# Phần VIII — Adverse selection

## 39. Adverse selection

Một passive order có thể chỉ được fill khi bên kia có thông tin tốt hơn hoặc khi market đang chuẩn bị di chuyển ngược bạn.

Do đó “ăn spread” chưa chắc có lời.

## 40. Toxic flow

Liquidity provider dùng thuật ngữ toxic flow để chỉ dòng lệnh có xu hướng đến trước adverse price move.

Đây là vấn đề timing/information, không nên diễn giải thành âm mưu.

## 41. Liquidity sweep

Stop và breakout orders thường tập trung quanh high/low rõ ràng.

Khi vùng đó bị xuyên:

```text
Triggered Orders ↑
→ Market-Order Burst
→ Nếu có opposing liquidity hấp thụ
→ Có thể reversal
```

Cơ chế này có thể giải thích nhiều hành vi thường được gọi là “stop hunt” mà không cần giả định thao túng.

# Phần IX — News, gap và market controls

## 42. News execution

CPI, NFP, FOMC, earnings hoặc geopolitics có thể làm:

- spread tăng;
- depth giảm;
- slippage tăng;
- stop gap;
- option IV thay đổi mạnh.

Strategy không thiết kế cho event nên có rule giảm size hoặc tránh event.

## 43. Gap risk

Giá có thể nhảy qua stop level.

Risk model phải tính discontinuous move thay vì giả định giá luôn đi qua mọi mức liên tục.

## 44. Circuit breaker và halt

Trading halt chỉ tạm dừng giao dịch; nó không xóa risk.

Khi reopen, market vẫn có thể gap tiếp.

## 45. Daily price limit

Ở thị trường có biên độ ngày, position có thể bị kẹt nhiều phiên nếu không có opposite liquidity.

Sizing cần tính cả multi-session exit scenario.

## 46. Liquidation cascade

```text
Price ↓
→ Margin Breach
→ Forced Sell
→ Price ↓ thêm
```

Đây là feedback thường thấy ở leveraged futures, CFD và crypto.

# Phần X — Hệ thống và operational safety

## 47. Latency

Latency chỉ quan trọng so với horizon của strategy.

Swing strategy không cần cạnh tranh microseconds; HFT thì cần.

Không nên chọn strategy vượt khả năng infrastructure.

## 48. Đồng bộ thời gian

Market data, signal, order và fill timestamps phải dùng clock nhất quán.

Sai thời gian làm attribution và live-vs-backtest comparison mất tin cậy.

## 49. Data quality

Stale quote, bad tick hoặc feed mất dữ liệu có thể tạo signal giả.

Production system cần validation và fallback behavior.

## 50. API state

Order submit thành công không đồng nghĩa order đã fill.

Nếu network timeout, phải query broker state trước khi retry để tránh duplicate.

## 51. Idempotency

Workflow idempotent giúp một request chạy lại không tạo thêm position ngoài ý muốn.

## 52. Reconciliation

Phải thường xuyên so:

```text
Internal Position
vs
Broker Position
```

Broker/exchange state là nguồn xác nhận exposure thật.

## 53. Order reject

Reject có thể do:

- margin;
- price band;
- quantity;
- market closed;
- symbol state.

Hệ thống phải có hành vi rõ cho từng nhóm lỗi.

## 54. Kill switch

Điều kiện dừng có thể gồm:

- market data lỗi;
- duplicate order;
- broker outage;
- spread bất thường;
- daily loss limit;
- position mismatch.

Kill switch bảo vệ survival, không phải tính năng phụ.

# Phần XI — Danh mục giao dịch

## 55. Portfolio heat

Portfolio heat tổng hợp risk của các trade nhưng phải điều chỉnh overlap.

Năm trade mỗi trade 0,5% risk nhưng cùng short USD có thể cùng thua khi USD tăng mạnh.

## 56. Gross và net exposure

Long-short book có net beta thấp nhưng gross leverage cao.

Gross exposure ảnh hưởng:

- funding;
- turnover;
- margin;
- liquidity;
- gap risk.

Phải theo dõi cả gross và net.

## 57. Factor exposure

Map position theo:

```text
USD
Rates
Equity Beta
Growth
Commodity
Volatility
Country
Liquidity
```

Cách này phát hiện concentration tốt hơn chỉ nhìn ticker.

## 58. Delta-equivalent exposure

Option book không nên tổng hợp theo premium paid.

Cần xem:

- Delta;
- Gamma;
- Vega;
- Theta;
- state-dependent exposure.

## 59. DV01

Fixed-income book nên tổng hợp DV01 và key-rate DV01.

Hai position notional bằng nhau chưa chắc rate risk bằng nhau.

## 60. Volatility factor

Short option, carry và một số mean-reversion strategy có thể cùng là short-vol dù instrument khác nhau.

Volatility nên là một risk bucket riêng.

## 61. Liquidity factor

Small caps, high-yield credit và crowded futures có thể cùng mất liquidity khi funding stress.

Correlation thanh khoản thường tăng trong crisis.

## 62. Correlation instability

Historical correlation không cố định.

Trong deleveraging, nhiều asset trước đó ít tương quan có thể giảm cùng nhau.

Nên dùng scenario correlation ngoài sample covariance.

## 63. Volatility targeting

Vol targeting giảm size khi vol tăng và tăng size khi vol giảm để giữ expected risk ổn định hơn.

Nhược điểm là tính procyclical:

```text
Low Vol → Leverage ↑
Shock → Vol ↑
→ Forced Deleverage sau selloff
```

Cần cap/floor và stress overlay.

## 64. Risk parity giữa các trade

Equal risk contribution giúp một market không chi phối toàn book.

Nhưng equal volatility không đồng nghĩa equal tail risk; vẫn phải điều chỉnh gap, liquidity và convexity.

## 65. VaR và Expected Shortfall

VaR ước tính threshold loss theo model tại confidence level.

Expected Shortfall ước tính loss trung bình khi đã vượt threshold.

Cả hai đều phụ thuộc dữ liệu/model và không thay thế scenario stress.

## 66. Drawdown control

Rule giảm risk phải được định nghĩa trước, không phải sau khi trader hoảng loạn.

Mục tiêu là bảo vệ khi distribution hoặc operation có dấu hiệu khác model.

# Phần XII — Position management

## 67. Pyramiding

Thêm position vào trade đang thắng có thể hợp lý với trend strategy, nhưng total stop risk sau mỗi lần thêm phải nằm trong budget.

## 68. Averaging down

Chỉ hợp lý khi là rule định trước với total risk cap.

Thêm position chỉ để tránh thừa nhận trade sai là hành vi cảm xúc.

## 69. MAE và MFE

- MAE: mức bất lợi lớn nhất trong trade;
- MFE: mức có lợi lớn nhất.

Chúng hữu ích để nghiên cứu stop/exit nhưng phải validation OOS trước khi thay rule.

# Phần XIII — Transaction Cost Analysis

## 70. Execution attribution

Phân rã performance gap thành:

```text
Signal Timing
Position Size
Spread
Commission
Slippage
Missed Fill
Market Impact
Discretionary Override
```

Như vậy mới biết phải sửa signal hay execution.

## 71. TCA

Transaction Cost Analysis (TCA) phân nhóm fills theo:

- benchmark;
- venue;
- order type;
- size;
- time-of-day;
- volatility;
- liquidity.

Mục tiêu là tìm leakage có hệ thống.

## 72. Expected vs realized cost

Cost model nên tạo expected spread/slippage.

Live result phải thường xuyên so với distribution dự kiến. Nếu cost xấu dần, nguyên nhân có thể là crowding, capacity hoặc broker/market change.

## 73. Fill probability

Passive strategy cần theo dõi xác suất fill và chất lượng fill.

Fill rate cao không tốt nếu fills chủ yếu xảy ra trước adverse move.

## 74. Adverse-selection diagnostic

Có thể đo price move sau fill ở nhiều horizon.

Nếu passive fills thường bị giá tiếp tục đi ngược ngay sau đó, spread capture có thể chỉ là ảo giác.

# Phần XIV — Production review

## 75. Live vs backtest

So định kỳ:

```text
Signal Frequency
Fill Rate
Spread
Slippage
Holding Period
Turnover
PnL Distribution
Drawdown
Factor Exposure
```

Khác biệt lớn cần được giải thích.

## 76. Capacity review

Khi capital tăng, execution cost có thể tăng phi tuyến.

Scale từng bước và đo realized cost thay vì giả định backtest scale vô hạn.

## 77. Retirement rule

Một strategy nên có điều kiện giảm hoặc dừng khi:

- edge mất theo evidence;
- cost vượt threshold;
- market structure thay đổi;
- operational risk không còn chấp nhận được.

Không nên giữ strategy chỉ vì đã đầu tư nhiều công sức vào nó.

## Kết luận

Lợi nhuận thực tế là kết quả của cả **tín hiệu và cách tương tác với thị trường**.

Chuỗi cần theo dõi là:

```text
Signal
→ Intended Position
→ Order
→ Fill
→ Actual Exposure
→ Portfolio Risk
→ Realized P/L
→ Attribution
→ Improvement
```

Một strategy có backtest tốt nhưng execution kém, capacity nhỏ hoặc operational control yếu vẫn có thể thất bại khi chạy thật.
