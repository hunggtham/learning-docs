# 05 — Thực thi (execution / 실행), broker, chi phí và operational rủi ro (risk / 위험) trong Forex

Một trading idea không đi thẳng từ chart vào P/L. Giữa hai điểm đó có một thực thi (execution / 실행) chuỗi xử lý (pipeline / 파이프라인):

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

Mỗi bước có thể tạo chi phí (cost / 비용) hoặc dạng thất bại (failure mode / 실패 모드). Vì vậy một chiến lược (strategy / 전략) chỉ có ý nghĩa nếu **edge sau thực thi (execution / 실행)** vẫn dương.

## 1. Tín hiệu (signal / 신호) khác thứ tự (order / 순서), thứ tự (order / 순서) khác fill

Giả sử mô hình (model / 모델) nói:

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

Khoảng cách giữa theoretical price và actual fill là một phần **hiện thực (implementation / 구현) shortfall**.

Backtest lấy candle close `1.1200` làm fill chính xác mà không modeling độ trễ (latency / 지연 시간)/spread/slippage có thể overstate edge.

## 2. Thị trường (market / 시장) thứ tự (order / 순서)

**Lệnh thị trường (market order)** ưu tiên thực thi (execution / 실행) hơn price certainty.

Mô hình tư duy (mental model / 사고 모델):

```text
Execute now
at best available executable price(s)
```

Thị trường (market / 시장) thứ tự (order / 순서) không có nghĩa “fill đúng price đang thấy trên chart”. Price có thể thay đổi trong milliseconds, kích thước (size / 크기) available ở top quote có thể không đủ, và thứ tự (order / 순서) có thể sweep nhiều price levels tùy thị trường (market / 시장) cấu trúc (structure / 구조).

## 3. Limit thứ tự (order / 순서)

**Lệnh giới hạn (limit order)** đặt giới hạn price chấp nhận.

Ví dụ buy limit:

```text
buy at price <= limit
```

Ưu điểm là điều khiển (control / 제어) price tốt hơn. Đổi lại có **non-execution rủi ro (risk / 위험)**: thị trường (market / 시장) chạm gần mức (level / 수준) rồi đi luôn, hoặc chỉ fill một phần.

Limit thứ tự (order / 순서) không miễn adverse selection. Nếu price chạm limit đúng lúc new thông tin (information / 정보) làm fair giá trị (value / 값) xấu đi, trader có thể được fill vì thị trường (market / 시장) đang chạy xuyên qua mình.

## 4. Stop thứ tự (order / 순서)

**Stop thứ tự (order / 순서)** thường trở thành executable thứ tự (order / 순서) sau khi trigger điều kiện (condition / 조건) xảy ra theo đặc tả hợp đồng (contract / 계약)/nền tảng (platform / 플랫폼) quy tắc (rule / 규칙).

Stop-loss giúp automate rủi ro (risk / 위험) phản hồi (response / 응답) nhưng:

```text
stop trigger price
≠ guaranteed fill price
```

Trong fast thị trường (market / 시장) hoặc gap, actual fill có thể xấu hơn đáng kể.

Do đó planned rủi ro (risk / 위험) dùng stop distance là **estimate conditional on thực thi (execution / 실행) chất lượng (quality / 품질)**, không phải absolute cap.

## 5. Stop-limit thứ tự (order / 순서)

Stop-limit kết hợp trigger với limit price.

Nó có thể tránh fill quá xa nhưng đổi lại rủi ro (risk / 위험) lớn hơn: thị trường (market / 시장) có thể gap qua limit và position **không thoát**.

Đây là sự đánh đổi (trade-off / 트레이드오프):

```text
price protection
versus
execution certainty
```

Không có thứ tự (order / 순서) kiểu (type / 타입) nào loại bỏ cả hai rủi ro (risk / 위험).

## 6. Bid/ask side của stop quan trọng

Chart có thể hiển thị bid, ask, mid hoặc broker-defined candle. Stop trigger lại có thể dựa trên một side cụ thể theo quy tắc (rule / 규칙) của nền tảng (platform / 플랫폼).

Ví dụ long position thường được đóng bằng sell, nên executable exit liên quan bid. Khi spread widen, bid có thể chạm stop dù mid-price chart trông chưa tới mức (level / 수준) bạn kỳ vọng.

Vì vậy khi rà soát (review / 검토) trade cần biết:

- chart price basis;
- stop trigger basis;
- actual bid/ask at thực thi (execution / 실행).

## 7. Slippage

**Trượt giá (slippage)** là chênh lệch giữa expected/quyết định (decision / 결정) price và actual thực thi (execution / 실행) price.

Slippage có thể positive hoặc negative, nhưng trong stress thường negative slippage đáng lo hơn vì liquidity biến mất khi nhiều participant cùng muốn thoát.

Sources:

- độ trễ (latency / 지연 시간);
- fast-moving price;
- low độ sâu (depth / 깊이);
- large thứ tự (order / 순서) kích thước (size / 크기);
- news sự kiện (event / 이벤트);
- weekend gap;
- venue fragmentation;
- broker routing/thực thi (execution / 실행) hành vi (behavior / 동작).

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

Chiến lược (strategy / 전략) dùng fixed spread `0.5 pip` cho mọi giờ, mọi năm và mọi sự kiện (event / 이벤트) thường đang under-modeling chi phí (cost / 비용).

Research tốt cần spread phân phối (distribution / 분포) theo thời gian (time / 시간)/regime nếu dữ liệu (data / 데이터) cho phép.

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

Effective round-trip chi phí (cost / 비용) gần hơn với:

```text
Entry spread/impact
+ exit spread/impact
+ commissions
+ slippage
+ financing while held
```

## 10. Rollover / financing

Leveraged FX position giữ qua rollover có thể nhận hoặc trả financing theo terms của sản phẩm (product / 제품).

Chi phí (cost / 비용) phụ thuộc:

- currency interest-rate relationship;
- tham chiếu (reference / 참조) tỷ lệ (rate / 비율);
- broker markup;
- long/short side;
- day-count convention;
- holiday/value-date adjustment;
- instrument cấu trúc (structure / 구조).

Không nên hard-code “positive swap” từ một website vào backtest dài hạn mà không phiên bản (version / 버전) dữ liệu (data / 데이터) theo thời gian.

## 11. Giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) phải quy mô (scale / 규모) với turnover

Một chiến lược (strategy / 전략) có edge nhỏ mỗi trade nhưng giao dịch cực nhiều có thể mất toàn bộ edge vào chi phí (cost / 비용).

Conceptual:

```text
Net Expectancy
= Gross Expectancy
- Expected Trading Cost per Trade
```

Nếu gross expectancy chỉ `0.15R` nhưng average all-in chi phí (cost / 비용) tương đương `0.12R`, edge còn rất mỏng và dễ biến mất khi spread/slippage tăng.

High-frequency turnover làm chi phí (cost / 비용) modeling quan trọng hơn tín hiệu (signal / 신호) storytelling.

## 12. Liquidity và độ sâu (depth / 깊이)

Một tight displayed spread không bảo đảm bạn có thể execute arbitrary kích thước (size / 크기) ở cùng price.

**Thị trường (market / 시장) độ sâu (depth / 깊이)** mô tả available liquidity theo các price levels.

Small retail thứ tự (order / 순서) có thể gần như không tạo thị trường (market / 시장) impact trong liquid major pair, nhưng institutional-size thứ tự (order / 순서) hoặc trade ở illiquid pair có thể phải chia nhỏ.

Kích thước (size / 크기) là một dimension của liquidity:

```text
A price is not meaningful without executable size
```

## 13. Thị trường (market / 시장) impact

**Thị trường (market / 시장) impact** là việc chính thứ tự (order / 순서) của bạn làm price xấu đi.

Với small trader, direct impact có thể negligible ở major FX. Nhưng concept vẫn cần hiểu cho systematic/institutional thực thi (execution / 실행) và khi trade thin products.

Thị trường (market / 시장) impact thường nonlinear với kích thước (size / 크기) và thị trường (market / 시장) điều kiện (condition / 조건).

## 14. OTC retail: broker/dealer là một phần của sản phẩm (product / 제품)

CFTC nhấn mạnh rằng retail OTC forex customer có thể đang giao dịch trực tiếp với dealer thay vì vào một open centralized exchange.

Điều đó có nghĩa due diligence không chỉ hỏi:

> EUR/USD sẽ đi đâu?

mà còn:

> Tôi có contractual claim với legal thực thể (entity / 엔터티) nào, quote/fill được hình thành thế nào và nếu có dispute/insolvency thì khung phần mềm (framework / 프레임워크) nào áp dụng?

## 15. Marketing labels không đủ để hiểu mô hình thực thi (execution model / 실행 모델)

Các label như:

- ECN;
- STP;
- A-book;
- B-book;
- thị trường (market / 시장) maker;
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

### Principal/dealer mô hình (model / 모델)

Firm có thể đứng đối diện máy khách (client / 클라이언트) giao dịch (transaction / 트랜잭션) về mặt contractual/economic cấu trúc (structure / 구조), sau đó internalize hoặc hedge exposure theo rủi ro (risk / 위험) chính sách (policy / 정책).

### Agency mô hình (model / 모델)

Firm tuyến (route / 경로)/arrange thứ tự (order / 순서) thực thi (execution / 실행) tới bên ngoài (external / 외부) venue/provider và kiếm commission/markup.

Thực tế có hybrid các mô hình (models / 모델들). Cùng firm có thể dùng treatment khác theo sản phẩm (product / 제품)/máy khách (client / 클라이언트)/luồng (flow / 흐름).

Vì vậy cần đọc disclosure cụ thể thay vì suy từ quảng cáo.

## 17. Internalization

Dealer có thể offset máy khách (client / 클라이언트) flows internally:

```text
Client A buys EUR/USD
Client B sells EUR/USD
→ dealer nets some exposure internally
```

Internalization không tự động là misconduct. Nó là một market-making/risk-management cơ chế (mechanism / 메커니즘) phổ biến.

Rủi ro (risk / 위험) issue nằm ở thực thi (execution / 실행) fairness, disclosure, conflicts, solvency và regulation — không phải ở từ “internalize” tự nó.

## 18. Xung đột (conflict / 충돌) of interest

Nếu dealer là counterparty, incentive cấu trúc (structure / 구조) cần được hiểu.

Potential conflicts có thể liên quan:

- spread/markup;
- thực thi (execution / 실행) price;
- máy khách (client / 클라이언트) turnover;
- affiliate compensation;
- rủi ro (risk / 위험) internalization.

Regulated khung phần mềm (framework / 프레임워크), best-execution/thực thi (execution / 실행) obligations tùy jurisdiction và transparent disclosure giúp quản lý conflicts nhưng không biến chúng thành zero.

## 19. Legal thực thể (entity / 엔터티) quan trọng hơn brand name

Một toàn cục (global / 전역) brand có thể có nhiều subsidiaries ở nhiều jurisdictions.

Account của bạn ký với **một legal thực thể (entity / 엔터티) cụ thể**.

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

Không nên chỉ tìm kiếm (search / 검색) logo/brand rồi giả định mọi subsidiary có cùng protections.

## 20. Regulatory registration check

Với US retail forex, CFTC khuyến nghị kiểm tra registration và disciplinary lịch sử (history / 이력) qua CFTC/NFA resources trước khi gửi tiền.

Tư duy tổng quát cho mọi jurisdiction:

```text
Find official regulator register
→ search exact legal entity
→ verify domain/contact details
→ verify permitted activities
→ inspect warnings/disciplinary history
```

Không dùng screenshot license do salesperson gửi làm proof duy nhất.

## 21. Offshore broker rủi ro (risk / 위험)

“Offshore” không tự động đồng nghĩa fraud, nhưng trader phải hiểu mình có thể thiếu một số protections hoặc gặp enforcement/dispute khó hơn tùy jurisdiction.

Red flags cần research kỹ:

- guaranteed high returns;
- pressure to deposit quickly;
- bonus terms khóa withdrawal;
- crypto-only payment without clear reason;
- fake regulator links;
- yêu cầu nộp thêm “tax/fee” để rút tiền;
- social-media account acting as broker hỗ trợ (support / 지원);
- không xác minh được legal thực thể (entity / 엔터티).

CFTC đã cảnh báo nhiều fraud complaints liên quan unregistered offshore dealers và social-media solicitation.

## 22. Máy khách (client / 클라이언트) money và insolvency

Câu hỏi “broker regulated không?” vẫn chưa đủ.

Cần hiểu:

- máy khách (client / 클라이언트) funds được giữ thế nào;
- segregation rules nào áp dụng;
- money có được treated as margin/collateral không;
- protection scheme nào có/không;
- insolvency claim đứng ở đâu;
- negative balance rules nào áp dụng.

Các câu trả lời thay đổi theo jurisdiction/sản phẩm (product / 제품)/máy khách (client / 클라이언트) kiểu (type / 타입). Không được suy diễn universal protection.

## 23. Withdrawal là operational rủi ro (risk / 위험) tín hiệu (signal / 신호)

Trước khi tăng capital lớn, tiến trình (process / 프로세스) thiết kế (design / 설계) có thể bao gồm kiểm thử (test / 테스트):

```text
small deposit
→ trading / statement verification
→ small withdrawal
→ reconcile time/fees
```

Mục tiêu không phải “kiểm thử (test / 테스트) profitability” mà kiểm thử (test / 테스트) operational chuỗi xử lý (pipeline / 파이프라인) và documentation.

Nếu firm yêu cầu nộp thêm tiền không được quy định rõ chỉ để bản phát hành (release / 릴리스) withdrawal, cần dừng và verify qua official channels.

## 24. Nền tảng (platform / 플랫폼) rủi ro (risk / 위험)

Thị trường (market / 시장) view đúng nhưng nền tảng (platform / 플랫폼) thất bại (failure / 실패) vẫn có thể gây mất mát (loss / 손실).

Thất bại (failure / 실패) modes:

- liên kết (connection / 연결) mất mát (loss / 손실);
- app/máy chủ (server / 서버) outage;
- stale quote;
- thứ tự (order / 순서) duplicated;
- thứ tự (order / 순서) status uncertain;
- stop not synchronized as expected;
- API bug;
- cục bộ (local / 로컬) thiết bị (device / 장치)/mạng (network / 네트워크) issue.

Trading plan cần emergency contact/procedure phù hợp với broker, không nên phụ thuộc một UI duy nhất nếu kích thước (size / 크기) material.

## 25. API/algorithmic thực thi (execution / 실행) rủi ro (risk / 위험)

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

Thuật toán (algorithm / 알고리즘) without rủi ro (risk / 위험) controls không phải automation hoàn chỉnh.

## 26. Order-state machine

Một hệ thống (system / 시스템) không nên chỉ biết `BUY_SENT`.

Cần mô hình (model / 모델) states như:

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

Nếu mạng (network / 네트워크) hết thời gian chờ (timeout / 타임아웃) sau khi gửi thứ tự (order / 순서), hệ thống (system / 시스템) không được tự động assume thứ tự (order / 순서) failed rồi gửi duplicate. Phải truy vấn (query / 쿼리)/reconcile broker trạng thái (state / 상태).

## 27. Partial fills

Institutional/venue thực thi (execution / 실행) có thể fill position theo nhiều parts.

Average fill price:

```text
VWAP Fill
= Σ(price_i × qty_i) / Σqty_i
```

Rủi ro (risk / 위험) hệ thống (system / 시스템) phải dùng actual filled quantity, không phải requested quantity.

## 28. Requotes và last look

Một số OTC thực thi (execution / 실행) protocols có thể cho liquidity provider kiểm tra/accept/reject quote trong rất ngắn cửa sổ (window / 윈도우) theo rules của venue/giao thức (protocol / 프로토콜).

Retail experience có thể biểu hiện như requote/rejection tùy mô hình (model / 모델).

Không nên đánh giá thực thi (execution / 실행) bằng một anecdote. Cần thống kê:

- fill tỷ lệ (rate / 비율);
- rejection tỷ lệ (rate / 비율);
- positive/negative slippage;
- độ trễ (latency / 지연 시간);
- phân phối (distribution / 분포) by session/sự kiện (event / 이벤트).

## 29. Thực thi (execution / 실행) chất lượng (quality / 품질) phải đo bằng dữ liệu (data / 데이터)

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

Nếu chiến lược (strategy / 전략) edge biến mất sau realistic chi phí (cost / 비용), đó không phải thực thi (execution / 실행) “xui”; chiến lược (strategy / 전략) chưa đủ robust.

## 30. Hiện thực (implementation / 구현) shortfall

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

Khoảng cách giữa paper và live kết quả (result / 결과) cần được attribution, không giải thích bằng cảm giác.

## 31. News thực thi (execution / 실행)

Quanh CPI, employment report, central-bank quyết định (decision / 결정) hoặc surprise headline:

```text
liquidity providers widen / pull quotes
→ spread widens
→ price jumps
→ stop/market orders receive worse fills
```

Backtest dùng 1-minute OHLC thường không đủ để reconstruct intra-bar đường dẫn (path / 경로) và executable spread.

Sự kiện (event / 이벤트) chiến lược (strategy / 전략) cần higher-resolution bid/ask dữ liệu (data / 데이터) nếu muốn estimate thực thi (execution / 실행) đáng tin hơn.

## 32. Weekend rủi ro (risk / 위험)

FX retail thị trường (market / 시장) đóng theo broker schedule cuối tuần. Thông tin (information / 정보) vẫn tiếp tục xuất hiện khi thị trường (market / 시장) đóng.

Khi reopen:

```text
new fair value
can be far from Friday close
```

Stop nằm giữa hai mức giá có thể không được fill tại stop price.

Holding weekend là intentional rủi ro (risk / 위험) quyết định (decision / 결정), không phải “thị trường (market / 시장) ngủ nên rủi ro (risk / 위험) bằng zero”.

## 33. Correlated thực thi (execution / 실행) rủi ro (risk / 위험)

Trong crisis, nhiều positions có thể cần exit cùng lúc trong khi liquidity của chúng cùng xấu đi.

Rủi ro (risk / 위험) mô hình (model / 모델) độc lập:

```text
each trade loses 1R with normal slippage
```

có thể underestimate actual portfolio mất mát (loss / 손실):

```text
correlated price move
+ correlated spread widening
+ correlated slippage
```

Tail rủi ro (risk / 위험) có cả **price correlation** và **liquidity correlation**.

## 34. Stop hunting: tách myth khỏi mechanics

Trader thường giải thích stop bị hit bằng “broker/thị trường (market / 시장) săn stop”.

Có những thị trường (market / 시장) mechanisms thật:

- stop orders cluster quanh obvious levels;
- liquidity near levels có thể mỏng;
- breakout triggers thị trường (market / 시장) orders;
- dealers/participants infer order-flow concentrations;
- price can move rapidly through liquidity pockets.

Nhưng từ đó không thể kết luận mọi stop-out là manipulation.

Phân tích cần dữ liệu (data / 데이터): independent price feeds, chính xác (exact / 정확한) bid/ask timestamp, spread, venue/broker thực thi (execution / 실행) chính sách (policy / 정책) và broader thị trường (market / 시장) move.

## 35. Demo account không tái tạo hoàn hảo live thực thi (execution / 실행)

Demo hữu ích để học nền tảng (platform / 플랫폼)/thứ tự (order / 순서) mechanics, nhưng có thể khác live về:

- slippage;
- độ trễ (latency / 지연 시간);
- liquidity/partial fill;
- psychological hành vi (behavior / 동작);
- financing details.

Do đó:

```text
Backtest
→ demo / paper test
→ small live forward test
→ scale only after evidence
```

là học tập (learning / 학습) progression hợp lý hơn nhảy thẳng từ chart vào maximum kích thước (size / 크기).

## 36. Broker comparison khung phần mềm (framework / 프레임워크) — không xếp hạng theo quảng cáo

Khi nghiên cứu broker, tạo ma trận (matrix / 행렬):

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

## 37. Chi phí (cost / 비용) mô hình (model / 모델) tối thiểu cho backtest

Mức (level / 수준) 1 — conservative fixed mô hình (model / 모델):

```text
spread + commission + financing
```

Mức (level / 수준) 2 — session-aware:

```text
spread by pair and session
+ commission
+ financing
```

Mức (level / 수준) 3 — regime-aware:

```text
bid/ask historical data
+ event/time-of-day spread
+ slippage model
+ size/liquidity relation
+ financing history
```

Mô hình (model / 모델) phức tạp hơn chỉ hữu ích nếu dữ liệu (data / 데이터) chất lượng (quality / 품질) đủ tốt.

## 38. Không overfit mô hình thực thi (execution model / 실행 모델)

Nếu bạn estimate slippage bằng 20 parameters để làm backtest đẹp hơn, mô hình thực thi (execution model / 실행 모델) cũng có thể overfit.

Nên ưu tiên conservative giả định (assumption / 가정) và sensitivity kiểm thử (test / 테스트):

```text
Base cost
1.5 × cost
2 × cost
stress-event cost
```

Chiến lược (strategy / 전략) robust nên không chết ngay khi chi phí (cost / 비용) giả định (assumption / 가정) xấu đi nhẹ.

## 39. Operational checklist trước mỗi chiến lược (strategy / 전략) live kiểm thử (test / 테스트)

Trước khi forward kiểm thử (test / 테스트) bằng real capital:

1. Xác minh chính xác (exact / 정확한) legal thực thể (entity / 엔터티)/regulator.
2. Đọc đặc tả hợp đồng (contract / 계약) specification.
3. Biết spread/commission/financing.
4. Biết margin và stop-out rules.
5. Kiểm thử (test / 테스트) thứ tự (order / 순서) types bằng kích thước (size / 크기) nhỏ.
6. Kiểm thử (test / 테스트) deposit/withdrawal tiến trình (process / 프로세스) hợp lý.
7. Biết emergency procedure nếu nền tảng (platform / 플랫폼) lỗi.
8. Journal quyết định (decision / 결정) price và fill price.
9. Đặt max mất mát (loss / 손실)/max exposure controls.
10. Reconcile statement với journal.

## 40. Một chiến lược (strategy / 전략) specification đầy đủ

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

Lúc đó chiến lược (strategy / 전략) mới gần một executable hệ thống (system / 시스템).

## 41. Sai lầm cần loại bỏ

### “Spread thấp nhất = broker tốt nhất”

Không đủ. Cần all-in chi phí (cost / 비용), thực thi (execution / 실행), legal/operational an toàn (safety / 안전).

### “Stop-loss guarantee chính xác (exact / 정확한) mất mát (loss / 손실)”

Sai nếu sản phẩm (product / 제품) không có tường minh (explicit / 명시적) guaranteed-stop tính năng (feature / 기능) theo terms cụ thể.

### “ECN/STP label chứng minh không xung đột (conflict / 충돌)”

Không đủ. Cần đọc legal/thực thi (execution / 실행) disclosures.

### “Demo profitable nghĩa live sẽ giống”

Sai vì thực thi (execution / 실행)/chi phí (cost / 비용)/hành vi (behavior / 동작) có thể đổi.

### “Price chart là executable price”

Không luôn đúng. Cần bid/ask and actual fill.

### “Broker regulated nên không cần đọc terms”

Sai. Regulation không thay thế hiểu sản phẩm (product / 제품), margin, client-money và dispute terms.

## 42. Từ mechanics sang chiến lược (strategy / 전략) research

Sau năm chương đầu, người học đã có nền:

```text
Market Structure
→ Quote / P&L
→ Leverage / Margin
→ Macro Drivers
→ Execution / Counterparty / Cost
```

Bây giờ mới hợp lý để học:

- trend/phạm vi (range / 범위)/volatility regimes;
- price hành động (action / 동작);
- indicators như transformations của dữ liệu (data / 데이터);
- fundamental/sự kiện (event / 이벤트) strategies;
- carry/momentum/giá trị (value / 값);
- backtest;
- portfolio construction.

Nếu đảo thứ tự và học entry setup trước, người học dễ tối ưu entry trong khi bỏ qua những biến quyết định survival.

## Đọc tiếp

Quay lại [Forex learning path](./README.md) để xem các chapter mở rộng dự kiến từ `06` trở đi.

Đối với methodology nghiên cứu chiến lược (strategy / 전략), đọc:

- [Systematic Risk, Backtest and Execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [Strategy Research, Robustness and Portfolio of Strategies](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)

## Nguồn nền
Phần “Nguồn nền” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- CFTC — Check registration/backgrounds: https://www.cftc.gov/check
- CFTC — Foreign Currency (Forex) Fraud: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_forex.html

Các regulatory details thay đổi theo jurisdiction và thời điểm. Khi tài liệu sau này đi vào Korea/Vietnam-specific FX, phải research lại từ regulator/official rules hiện hành thay vì bản sao (copy / 복사) quy tắc (rule / 규칙) của Mỹ sang thị trường khác.
