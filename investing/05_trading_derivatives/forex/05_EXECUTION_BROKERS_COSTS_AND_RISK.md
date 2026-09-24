# 05 — Execution, broker, chi phí và operational risk trong Forex

Một trading idea không đi thẳng từ chart vào P/L. Giữa hai điểm đó có một execution pipeline:

```text
Decision
→ Order
→ Broker / Dealer / Venue
→ Price discovery / routing
→ Fill or rejection
→ Position
→ Financing / margin
→ Exit
→ Settlement / cash adjustment
→ Account statement
```

Mỗi bước có thể tạo cost hoặc failure mode. Vì vậy một strategy chỉ có ý nghĩa nếu **edge sau execution** vẫn dương.

## 1. Signal khác order, order khác fill

Giả sử model nói:

```text
Buy EUR/USD at 1.1200
```

Đây chưa phải realized trade.

Thực tế có thể là:

```text
Signal at 1.1200
→ order transmitted
→ quote changes
→ fill at 1.1202
```

Khoảng cách giữa theoretical price và actual fill là một phần **implementation shortfall**.

Backtest lấy candle close `1.1200` làm fill chính xác mà không modeling latency/spread/slippage có thể overstate edge.

## 2. Market order

**Lệnh thị trường (market order)** ưu tiên execution hơn price certainty.

Mental model:

```text
Execute now
at best available executable price(s)
```

Market order không có nghĩa “fill đúng price đang thấy trên chart”. Price có thể thay đổi trong milliseconds, size available ở top quote có thể không đủ, và order có thể sweep nhiều price levels tùy market structure.

## 3. Limit order

**Lệnh giới hạn (limit order)** đặt giới hạn price chấp nhận.

Ví dụ buy limit:

```text
buy at price <= limit
```

Ưu điểm là control price tốt hơn. Đổi lại có **non-execution risk**: market chạm gần level rồi đi luôn, hoặc chỉ fill một phần.

Limit order không miễn adverse selection. Nếu price chạm limit đúng lúc new information làm fair value xấu đi, trader có thể được fill vì market đang chạy xuyên qua mình.

## 4. Stop order

**Stop order** thường trở thành executable order sau khi trigger condition xảy ra theo contract/platform rule.

Stop-loss giúp automate risk response nhưng:

```text
stop trigger price
≠ guaranteed fill price
```

Trong fast market hoặc gap, actual fill có thể xấu hơn đáng kể.

Do đó planned risk dùng stop distance là **estimate conditional on execution quality**, không phải absolute cap.

## 5. Stop-limit order

Stop-limit kết hợp trigger với limit price.

Nó có thể tránh fill quá xa nhưng đổi lại risk lớn hơn: market có thể gap qua limit và position **không thoát**.

Đây là trade-off:

```text
price protection
versus
execution certainty
```

Không có order type nào loại bỏ cả hai risk.

## 6. Bid/ask side của stop quan trọng

Chart có thể hiển thị bid, ask, mid hoặc broker-defined candle. Stop trigger lại có thể dựa trên một side cụ thể theo rule của platform.

Ví dụ long position thường được đóng bằng sell, nên executable exit liên quan bid. Khi spread widen, bid có thể chạm stop dù mid-price chart trông chưa tới level bạn kỳ vọng.

Vì vậy khi review trade cần biết:

- chart price basis;
- stop trigger basis;
- actual bid/ask at execution.

## 7. Slippage

**Trượt giá (slippage)** là chênh lệch giữa expected/decision price và actual execution price.

Slippage có thể positive hoặc negative, nhưng trong stress thường negative slippage đáng lo hơn vì liquidity biến mất khi nhiều participant cùng muốn thoát.

Sources:

- latency;
- fast-moving price;
- low depth;
- large order size;
- news event;
- weekend gap;
- venue fragmentation;
- broker routing/execution behavior.

## 8. Spread không cố định

Spread thường hẹp khi:

```text
liquidity high
+ volatility moderate
+ market makers confident in hedging
```

và rộng khi:

```text
uncertainty rises
+ liquidity falls
+ adverse-selection risk rises
```

Strategy dùng fixed spread `0.5 pip` cho mọi giờ, mọi năm và mọi event thường đang under-modeling cost.

Research tốt cần spread distribution theo time/regime nếu data cho phép.

## 9. Commission

Broker có thể charge:

```text
explicit commission
or
spread markup
or
both
```

Không nên so broker chỉ bằng advertised spread.

Effective round-trip cost gần hơn với:

```text
Entry spread/impact
+ exit spread/impact
+ commissions
+ slippage
+ financing while held
```

## 10. Rollover / financing

Leveraged FX position giữ qua rollover có thể nhận hoặc trả financing theo terms của product.

Cost phụ thuộc:

- currency interest-rate relationship;
- reference rate;
- broker markup;
- long/short side;
- day-count convention;
- holiday/value-date adjustment;
- instrument structure.

Không nên hard-code “positive swap” từ một website vào backtest dài hạn mà không version data theo thời gian.

## 11. Transaction cost phải scale với turnover

Một strategy có edge nhỏ mỗi trade nhưng giao dịch cực nhiều có thể mất toàn bộ edge vào cost.

Conceptual:

```text
Net Expectancy
= Gross Expectancy
- Expected Trading Cost per Trade
```

Nếu gross expectancy chỉ `0.15R` nhưng average all-in cost tương đương `0.12R`, edge còn rất mỏng và dễ biến mất khi spread/slippage tăng.

High-frequency turnover làm cost modeling quan trọng hơn signal storytelling.

## 12. Liquidity và depth

Một tight displayed spread không bảo đảm bạn có thể execute arbitrary size ở cùng price.

**Market depth** mô tả available liquidity theo các price levels.

Small retail order có thể gần như không tạo market impact trong liquid major pair, nhưng institutional-size order hoặc trade ở illiquid pair có thể phải chia nhỏ.

Size là một dimension của liquidity:

```text
A price is not meaningful without executable size
```

## 13. Market impact

**Market impact** là việc chính order của bạn làm price xấu đi.

Với small trader, direct impact có thể negligible ở major FX. Nhưng concept vẫn cần hiểu cho systematic/institutional execution và khi trade thin products.

Market impact thường nonlinear với size và market condition.

## 14. OTC retail: broker/dealer là một phần của product

CFTC nhấn mạnh rằng retail OTC forex customer có thể đang giao dịch trực tiếp với dealer thay vì vào một open centralized exchange.

Điều đó có nghĩa due diligence không chỉ hỏi:

> EUR/USD sẽ đi đâu?

mà còn:

> Tôi có contractual claim với legal entity nào, quote/fill được hình thành thế nào và nếu có dispute/insolvency thì framework nào áp dụng?

## 15. Marketing labels không đủ để hiểu execution model

Các label như:

- ECN;
- STP;
- A-book;
- B-book;
- market maker;
- agency;

thường được dùng trong marketing với meanings không hoàn toàn standardized cho retail audience.

Không nên kết luận broker “tốt/xấu” chỉ từ label.

Cần đọc:

```text
execution policy
client agreement
legal entity
regulator/register
conflict-of-interest disclosure
price source / order handling
margin and liquidation rules
```

## 16. Principal vs agency concept

### Principal/dealer model

Firm có thể đứng đối diện client transaction về mặt contractual/economic structure, sau đó internalize hoặc hedge exposure theo risk policy.

### Agency model

Firm route/arrange order execution tới external venue/provider và kiếm commission/markup.

Thực tế có hybrid models. Cùng firm có thể dùng treatment khác theo product/client/flow.

Vì vậy cần đọc disclosure cụ thể thay vì suy từ quảng cáo.

## 17. Internalization

Dealer có thể offset client flows internally:

```text
Client A buys EUR/USD
Client B sells EUR/USD
→ dealer nets some exposure internally
```

Internalization không tự động là misconduct. Nó là một market-making/risk-management mechanism phổ biến.

Risk issue nằm ở execution fairness, disclosure, conflicts, solvency và regulation — không phải ở từ “internalize” tự nó.

## 18. Conflict of interest

Nếu dealer là counterparty, incentive structure cần được hiểu.

Potential conflicts có thể liên quan:

- spread/markup;
- execution price;
- client turnover;
- affiliate compensation;
- risk internalization.

Regulated framework, best-execution/execution obligations tùy jurisdiction và transparent disclosure giúp quản lý conflicts nhưng không biến chúng thành zero.

## 19. Legal entity quan trọng hơn brand name

Một global brand có thể có nhiều subsidiaries ở nhiều jurisdictions.

Account của bạn ký với **một legal entity cụ thể**.

Cần xác minh:

```text
exact company name
registration/license number
jurisdiction
regulator
client classification
product permissions
complaint/dispute channel
insolvency/client-money terms
```

Không nên chỉ search logo/brand rồi giả định mọi subsidiary có cùng protections.

## 20. Regulatory registration check

Với US retail forex, CFTC khuyến nghị kiểm tra registration và disciplinary history qua CFTC/NFA resources trước khi gửi tiền.

Tư duy tổng quát cho mọi jurisdiction:

```text
Find official regulator register
→ search exact legal entity
→ verify domain/contact details
→ verify permitted activities
→ inspect warnings/disciplinary history
```

Không dùng screenshot license do salesperson gửi làm proof duy nhất.

## 21. Offshore broker risk

“Offshore” không tự động đồng nghĩa fraud, nhưng trader phải hiểu mình có thể thiếu một số protections hoặc gặp enforcement/dispute khó hơn tùy jurisdiction.

Red flags cần research kỹ:

- guaranteed high returns;
- pressure to deposit quickly;
- bonus terms khóa withdrawal;
- crypto-only payment without clear reason;
- fake regulator links;
- yêu cầu nộp thêm “tax/fee” để rút tiền;
- social-media account acting as broker support;
- không xác minh được legal entity.

CFTC đã cảnh báo nhiều fraud complaints liên quan unregistered offshore dealers và social-media solicitation.

## 22. Client money và insolvency

Câu hỏi “broker regulated không?” vẫn chưa đủ.

Cần hiểu:

- client funds được giữ thế nào;
- segregation rules nào áp dụng;
- money có được treated as margin/collateral không;
- protection scheme nào có/không;
- insolvency claim đứng ở đâu;
- negative balance rules nào áp dụng.

Các câu trả lời thay đổi theo jurisdiction/product/client type. Không được suy diễn universal protection.

## 23. Withdrawal là operational risk signal

Trước khi tăng capital lớn, process design có thể bao gồm test:

```text
small deposit
→ trading / statement verification
→ small withdrawal
→ reconcile time/fees
```

Mục tiêu không phải “test profitability” mà test operational pipeline và documentation.

Nếu firm yêu cầu nộp thêm tiền không được quy định rõ chỉ để release withdrawal, cần dừng và verify qua official channels.

## 24. Platform risk

Market view đúng nhưng platform failure vẫn có thể gây loss.

Failure modes:

- connection loss;
- app/server outage;
- stale quote;
- order duplicated;
- order status uncertain;
- stop not synchronized as expected;
- API bug;
- local device/network issue.

Trading plan cần emergency contact/procedure phù hợp với broker, không nên phụ thuộc một UI duy nhất nếu size material.

## 25. API/algorithmic execution risk

Bot có thể gửi lệnh nhanh hơn human nhưng cũng nhân lỗi nhanh hơn.

Controls cần có:

```text
max order size
max position
max daily loss
max number of orders
price sanity check
duplicate-order prevention
heartbeat
reconciliation
kill switch
```

Algorithm without risk controls không phải automation hoàn chỉnh.

## 26. Order-state machine

Một system không nên chỉ biết `BUY_SENT`.

Cần model states như:

```text
CREATED
SENT
ACKNOWLEDGED
PARTIALLY_FILLED
FILLED
CANCELED
REJECTED
UNKNOWN / RECONCILE
```

Nếu network timeout sau khi gửi order, system không được tự động assume order failed rồi gửi duplicate. Phải query/reconcile broker state.

## 27. Partial fills

Institutional/venue execution có thể fill position theo nhiều parts.

Average fill price:

```text
VWAP Fill
= Σ(price_i × qty_i) / Σqty_i
```

Risk system phải dùng actual filled quantity, không phải requested quantity.

## 28. Requotes và last look

Một số OTC execution protocols có thể cho liquidity provider kiểm tra/accept/reject quote trong rất ngắn window theo rules của venue/protocol.

Retail experience có thể biểu hiện như requote/rejection tùy model.

Không nên đánh giá execution bằng một anecdote. Cần thống kê:

- fill rate;
- rejection rate;
- positive/negative slippage;
- latency;
- distribution by session/event.

## 29. Execution quality phải đo bằng data

Journal nên lưu:

```text
signal timestamp
decision price
order-send timestamp
order type
requested size
fill timestamp
fill price
spread at decision/fill
slippage
commission
financing
exit details
```

Sau nhiều trades có thể tính:

```text
Average Slippage
Slippage Distribution
Cost per Trade
Cost per Unit Turnover
Fill Rate
Performance by Session
Performance around News
```

Nếu strategy edge biến mất sau realistic cost, đó không phải execution “xui”; strategy chưa đủ robust.

## 30. Implementation shortfall

Một decomposition đơn giản:

```text
Paper Strategy P/L
- delay cost
- spread
- commission
- slippage/impact
- financing
= Realized Strategy P/L
```

Khoảng cách giữa paper và live result cần được attribution, không giải thích bằng cảm giác.

## 31. News execution

Quanh CPI, employment report, central-bank decision hoặc surprise headline:

```text
liquidity providers widen / pull quotes
→ spread widens
→ price jumps
→ stop/market orders receive worse fills
```

Backtest dùng 1-minute OHLC thường không đủ để reconstruct intra-bar path và executable spread.

Event strategy cần higher-resolution bid/ask data nếu muốn estimate execution đáng tin hơn.

## 32. Weekend risk

FX retail market đóng theo broker schedule cuối tuần. Information vẫn tiếp tục xuất hiện khi market đóng.

Khi reopen:

```text
new fair value
can be far from Friday close
```

Stop nằm giữa hai mức giá có thể không được fill tại stop price.

Holding weekend là intentional risk decision, không phải “market ngủ nên risk bằng zero”.

## 33. Correlated execution risk

Trong crisis, nhiều positions có thể cần exit cùng lúc trong khi liquidity của chúng cùng xấu đi.

Risk model độc lập:

```text
each trade loses 1R with normal slippage
```

có thể underestimate actual portfolio loss:

```text
correlated price move
+ correlated spread widening
+ correlated slippage
```

Tail risk có cả **price correlation** và **liquidity correlation**.

## 34. Stop hunting: tách myth khỏi mechanics

Trader thường giải thích stop bị hit bằng “broker/market săn stop”.

Có những market mechanisms thật:

- stop orders cluster quanh obvious levels;
- liquidity near levels có thể mỏng;
- breakout triggers market orders;
- dealers/participants infer order-flow concentrations;
- price can move rapidly through liquidity pockets.

Nhưng từ đó không thể kết luận mọi stop-out là manipulation.

Phân tích cần data: independent price feeds, exact bid/ask timestamp, spread, venue/broker execution policy và broader market move.

## 35. Demo account không tái tạo hoàn hảo live execution

Demo hữu ích để học platform/order mechanics, nhưng có thể khác live về:

- slippage;
- latency;
- liquidity/partial fill;
- psychological behavior;
- financing details.

Do đó:

```text
Backtest
→ demo / paper test
→ small live forward test
→ scale only after evidence
```

là learning progression hợp lý hơn nhảy thẳng từ chart vào maximum size.

## 36. Broker comparison framework — không xếp hạng theo quảng cáo

Khi nghiên cứu broker, tạo matrix:

```text
Legal entity / jurisdiction
Regulatory register verification
Product actually offered
Client-money / insolvency terms
Margin / stop-out policy
Execution policy
Spread distribution
Commission
Financing
Order types
Historical uptime / incident handling
Deposit / withdrawal process
Statements / tax records
API / data quality if needed
Dispute process
```

Không chọn chỉ vì leverage cao hoặc welcome bonus.

## 37. Cost model tối thiểu cho backtest

Level 1 — conservative fixed model:

```text
spread + commission + financing
```

Level 2 — session-aware:

```text
spread by pair and session
+ commission
+ financing
```

Level 3 — regime-aware:

```text
bid/ask historical data
+ event/time-of-day spread
+ slippage model
+ size/liquidity relation
+ financing history
```

Model phức tạp hơn chỉ hữu ích nếu data quality đủ tốt.

## 38. Không overfit execution model

Nếu bạn estimate slippage bằng 20 parameters để làm backtest đẹp hơn, execution model cũng có thể overfit.

Nên ưu tiên conservative assumption và sensitivity test:

```text
Base cost
1.5 × cost
2 × cost
stress-event cost
```

Strategy robust nên không chết ngay khi cost assumption xấu đi nhẹ.

## 39. Operational checklist trước mỗi strategy live test

Trước khi forward test bằng real capital:

1. Xác minh exact legal entity/regulator.
2. Đọc contract specification.
3. Biết spread/commission/financing.
4. Biết margin và stop-out rules.
5. Test order types bằng size nhỏ.
6. Test deposit/withdrawal process hợp lý.
7. Biết emergency procedure nếu platform lỗi.
8. Journal decision price và fill price.
9. Đặt max loss/max exposure controls.
10. Reconcile statement với journal.

## 40. Một strategy specification đầy đủ

Không nên chỉ viết:

```text
Buy when EMA20 crosses EMA50
```

Specification cần thêm:

```text
Instrument and legal product
Data source
Timezone/session
Signal timestamp
Order type
Entry execution assumption
Exit execution assumption
Spread/commission/slippage model
Financing
Sizing rule
Maximum gross/net leverage
Portfolio heat
Event handling
Weekend rule
Margin stress
Kill switch
Reconciliation process
```

Lúc đó strategy mới gần một executable system.

## 41. Sai lầm cần loại bỏ

### “Spread thấp nhất = broker tốt nhất”

Không đủ. Cần all-in cost, execution, legal/operational safety.

### “Stop-loss guarantee exact loss”

Sai nếu product không có explicit guaranteed-stop feature theo terms cụ thể.

### “ECN/STP label chứng minh không conflict”

Không đủ. Cần đọc legal/execution disclosures.

### “Demo profitable nghĩa live sẽ giống”

Sai vì execution/cost/behavior có thể đổi.

### “Price chart là executable price”

Không luôn đúng. Cần bid/ask and actual fill.

### “Broker regulated nên không cần đọc terms”

Sai. Regulation không thay thế hiểu product, margin, client-money và dispute terms.

## 42. Từ mechanics sang strategy research

Sau năm chương đầu, người học đã có nền:

```text
Market Structure
→ Quote / P&L
→ Leverage / Margin
→ Macro Drivers
→ Execution / Counterparty / Cost
```

Bây giờ mới hợp lý để học:

- trend/range/volatility regimes;
- price action;
- indicators như transformations của data;
- fundamental/event strategies;
- carry/momentum/value;
- backtest;
- portfolio construction.

Nếu đảo thứ tự và học entry setup trước, người học dễ tối ưu entry trong khi bỏ qua những biến quyết định survival.

## Đọc tiếp

Quay lại [Forex learning path](./README.md) để xem các chapter mở rộng dự kiến từ `06` trở đi.

Đối với methodology nghiên cứu strategy, đọc:

- [Systematic Risk, Backtest and Execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [Strategy Research, Robustness and Portfolio of Strategies](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)

## Nguồn nền

- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- CFTC — Check registration/backgrounds: https://www.cftc.gov/check
- CFTC — Foreign Currency (Forex) Fraud: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_forex.html

Các regulatory details thay đổi theo jurisdiction và thời điểm. Khi tài liệu sau này đi vào Korea/Vietnam-specific FX, phải research lại từ regulator/official rules hiện hành thay vì copy rule của Mỹ sang thị trường khác.
