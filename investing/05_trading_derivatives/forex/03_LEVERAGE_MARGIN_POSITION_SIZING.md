# 03 — Leverage, margin và position sizing

Forex retail hấp dẫn một phần vì broker có thể cho phép kiểm soát **giá trị danh nghĩa (notional)** lớn hơn nhiều so với cash trong account. Chính cơ chế này cũng là nguồn của phần lớn hiểu nhầm nguy hiểm nhất.

Ba khái niệm phải tách hoàn toàn:

```text
Notional Exposure
≠ Margin Requirement
≠ Amount at Risk
```

**Đòn bẩy (leverage, 레버리지)** nói về quan hệ giữa exposure và capital/equity. **Ký quỹ (margin, 증거금)** là collateral broker yêu cầu để duy trì position. **Amount at risk** là mức loss có thể xảy ra theo price path, stop, gap, slippage và các điều khoản liquidation. Ba con số này liên hệ với nhau nhưng không thay thế nhau.

## 1. Leverage không tạo ra edge

Giả sử account có 10.000 USD và mở 100.000 USD notional exposure.

Effective leverage xấp xỉ:

```text
Effective Leverage
= Gross Notional / Account Equity
= 100,000 / 10,000
= 10x
```

Nếu underlying exposure giảm 1% và bỏ qua cost:

```text
Loss ≈ 1% × 100,000
= 1,000 USD
```

So với equity 10.000 USD:

```text
Account loss ≈ 10%
```

Leverage không làm xác suất dự đoán đúng tăng. Nó chỉ làm cùng price move tạo biến động account lớn hơn.

## 2. Broker leverage limit và effective leverage khác nhau

Broker có thể quảng cáo maximum leverage, ví dụ `1:30`, `1:50`, `1:100` hoặc mức khác tùy jurisdiction/product/client classification.

Nhưng nếu broker cho phép `1:100`, trader không bắt buộc dùng 100x.

Ví dụ account 10.000 USD, broker cho maximum 100x nhưng trader chỉ mở 20.000 USD notional:

```text
Effective leverage = 20,000 / 10,000 = 2x
```

Do đó câu hỏi đúng không phải:

> Broker cho tôi leverage bao nhiêu?

mà là:

> Tổng notional exposure hiện tại bằng bao nhiêu lần equity và account sẽ mất bao nhiêu nếu market di chuyển bất lợi theo các stress scenario?

## 3. Margin requirement

Một cách xấp xỉ đơn giản:

```text
Required Margin
≈ Notional / Maximum Leverage Allowed
```

Nếu notional là 100.000 USD và margin regime tương đương leverage 20x:

```text
Required Margin
≈ 100,000 / 20
= 5,000 USD
```

Cũng có thể biểu diễn bằng margin rate:

```text
Margin Rate = 1 / Leverage
```

20x tương đương khoảng 5% margin requirement.

Nhưng broker thực tế có thể tính margin theo contract specification, pair, account currency, tiered notional, volatility regime hoặc regulatory rule. Công thức trên là mental model, không thay thế rule của broker.

## 4. Margin không phải maximum loss

Đây là distinction quan trọng nhất.

Nếu broker yêu cầu 2.000 USD margin cho position 100.000 USD, không có nghĩa loss bị giới hạn ở 2.000 USD.

P/L vẫn được tạo từ **100.000 USD exposure**.

Trong market move lớn hoặc gap:

```text
Loss can consume margin
→ consume remaining equity
→ potentially exceed planned loss
```

Treatment của negative balance phụ thuộc jurisdiction, client type và contractual terms. Không được giả định protection tồn tại nếu chưa kiểm tra.

CFTC cũng nhấn mạnh leverage trong retail OTC forex có thể khuếch đại loss mạnh và customer cần hiểu margin obligation trước khi giao dịch.

## 5. Balance, equity, used margin và free margin

### Balance

Balance thường phản ánh account value sau các transaction đã realized, chưa bao gồm floating P/L của open positions theo cách hiển thị phổ biến.

### Equity

```text
Equity
= Balance + Floating P/L
```

Nếu balance 10.000 USD và open positions đang lỗ 1.500 USD:

```text
Equity ≈ 8,500 USD
```

### Used margin

Phần margin đang được giữ cho open positions.

### Free margin

Một cách hiển thị phổ biến:

```text
Free Margin
= Equity - Used Margin
```

Free margin giảm khi:

- mở thêm position;
- floating losses tăng;
- margin requirement tăng.

## 6. Margin level

Nhiều retail platforms dùng:

```text
Margin Level
= Equity / Used Margin × 100%
```

Ví dụ:

```text
Equity = 8,000
Used Margin = 4,000
```

thì:

```text
Margin Level = 200%
```

Broker có thể đặt threshold riêng cho margin call hoặc automatic stop-out. Không có một universal stop-out percentage cho mọi broker.

## 7. Margin call và stop-out không giống stop-loss

### Stop-loss

Order do strategy/trader đặt để cố thoát khi market tới một mức nhất định.

### Margin call / stop-out

Risk-control mechanism của broker/account, xảy ra khi account không còn đủ collateral theo rule.

Nếu để position đi đến stop-out, trader đã chuyển quyền kiểm soát exit từ strategy sang margin system.

Một risk process tốt thường không dựa vào:

```text
“I will be liquidated before things get too bad.”
```

Liquidation có thể xảy ra trong điều kiện spread rộng và liquidity xấu, chính là lúc execution quality giảm.

## 8. Effective leverage tăng khi equity giảm

Giả sử gross notional giữ nguyên 100.000 USD.

Ban đầu:

```text
Equity = 20,000
Effective leverage = 5x
```

Sau loss:

```text
Equity = 10,000
Effective leverage = 10x
```

Không cần mở thêm trade, portfolio đã **tự trở nên leveraged hơn** khi equity giảm.

Đây là feedback loop nguy hiểm:

```text
Loss
→ lower equity
→ higher effective leverage
→ same market move creates larger % equity change
→ higher liquidation risk
```

## 9. Gross leverage và net exposure

Nếu có nhiều positions, cần nhìn cả gross lẫn net.

Ví dụ:

```text
Long 100k EUR/USD
Short 100k GBP/USD equivalent
```

Net USD exposure có thể nhỏ hơn gross exposure, nhưng portfolio vẫn có substantial EUR-vs-GBP relative exposure và execution/liquidity risk ở cả hai legs.

Một approximate gross leverage metric:

```text
Gross Leverage
= Sum(|Position Notional|) / Equity
```

Netting chỉ theo USD có thể che giấu cross-currency risk.

## 10. Position sizing phải bắt đầu từ invalidation

Một trade setup cần trả lời:

1. Thesis là gì?
2. Điều kiện nào làm thesis sai hoặc setup invalid?
3. Từ entry đến invalidation bao xa?
4. Account chấp nhận mất bao nhiêu nếu scenario đó xảy ra?
5. Size nào biến distance đó thành allowed loss?

Flow:

```text
Thesis
→ Invalidation
→ Stop Distance
→ Allowed Account Loss
→ Position Size
```

Không nên làm ngược:

```text
Choose huge lot
→ then invent a stop to fit it
```

## 11. Basic sizing formula

Nếu account currency trùng P/L currency:

```text
Position Size
≈ Allowed Loss / Loss Per Unit at Stop
```

Theo pip:

```text
Required Pip Value
≈ Allowed Loss / Stop Distance in Pips
```

Sau đó:

```text
Base Units
≈ Required Pip Value / Pip Size
```

đối với structure đơn giản như EUR/USD account USD.

## 12. Ví dụ sizing

Account equity:

```text
20,000 USD
```

Giả sử research policy cho phép initial planned risk `0.5%` equity cho một trade:

```text
Allowed Loss
= 20,000 × 0.005
= 100 USD
```

Setup EUR/USD có invalidation 40 pips.

Required pip value:

```text
100 / 40
= 2.50 USD/pip
```

Với EUR/USD:

```text
Base Units
≈ 2.50 / 0.0001
= 25,000 EUR
```

Approximate standard-lot notation:

```text
0.25 lot
```

Đây chỉ là planned loss **trước** slippage, gap và some costs.

## 13. Fixed percentage risk có lợi ích gì?

Nếu mỗi trade risk một fraction của current equity, size tự co lại sau drawdown và tăng dần khi equity tăng.

Ví dụ risk 1%:

```text
Equity 10,000 → planned risk 100
Equity 8,000  → planned risk 80
```

Cơ chế này giảm tốc độ mất vốn tương đối so với fixed-dollar risk khi account giảm mạnh.

Nhưng fixed percentage không tự tạo edge. Một strategy có negative expectancy vẫn mất tiền, chỉ có thể mất chậm hơn.

## 14. Vì sao “risk 2% mỗi trade” không phải quy tắc universal?

Các con số như 1% hoặc 2% thường được truyền như rule-of-thumb. Không có một tỷ lệ phù hợp cho mọi strategy.

Risk fraction cần phụ thuộc:

- edge uncertainty;
- stop behavior;
- return distribution;
- gap/tail risk;
- number of simultaneous positions;
- correlation;
- strategy frequency;
- maximum tolerable drawdown;
- operational constraints.

Một strategy có nhiều correlated trades không thể đánh giá risk từng trade riêng lẻ.

## 15. Portfolio heat

**Portfolio heat** là tổng planned loss/exposure nếu nhiều positions cùng đi tới stop hoặc stress threshold.

Ví dụ có 5 trades, mỗi trade planned `1%` account risk. Không nên ngay lập tức kết luận portfolio risk là “an toàn vì mỗi trade chỉ 1%”.

Nếu cả 5 đều là variants của short USD:

```text
USD shock
→ multiple stops hit together
→ slippage correlated
→ portfolio loss clusters
```

Cần stress cả **common factor**.

## 16. Currency-factor decomposition

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Long AUD/USD
```

Có thể mô tả sơ bộ:

```text
+EUR -USD
+GBP -USD
+AUD -USD
```

USD short exposure xuất hiện ba lần.

Một risk dashboard tốt nên aggregate theo currency:

```text
EUR exposure
GBP exposure
AUD exposure
USD exposure
JPY exposure
...
```

thay vì chỉ đếm tickets.

## 17. Stop distance nên liên hệ volatility

Một fixed 20-pip stop có ý nghĩa rất khác khi pair daily range là 40 pips so với 200 pips.

Nếu stop nằm bên trong normal noise, strategy có thể bị exit liên tục dù thesis chưa invalidated.

Có thể dùng volatility measure như ATR hoặc realized volatility để **normalize context**, nhưng indicator không quyết định stop thay cho thesis.

Mental model:

```text
Market structure / thesis invalidation
+ volatility context
→ stop distance
→ size adjusted to keep account risk controlled
```

Không nên giữ size cố định rồi nới stop trong high volatility; làm vậy risk tăng hai lần.

## 18. Gap risk

FX spot thường giao dịch gần liên tục trong tuần, nhưng gap vẫn có thể xảy ra:

- weekend reopen;
- unexpected geopolitical event;
- sudden policy announcement;
- liquidity vacuum;
- instrument-specific trading halt/price discontinuity.

Stop order chỉ kích hoạt execution; nó không guarantee exact fill.

Planned loss:

```text
100 USD
```

có thể thành:

```text
150 / 300 / more
```

nếu price jumps qua stop.

Risk model phải có tail scenario thay vì giả định continuous price path.

## 19. Spread widening cũng làm liquidation pressure tăng

Floating P/L thường được marked theo executable bid/ask side. Khi spread widen mạnh:

```text
mark-to-market loss increases
→ equity falls
→ free margin falls
→ margin level falls
```

Ngay cả khi mid-price không di chuyển nhiều, account có thể chịu stress từ spread.

Đây là lý do margin headroom cần lớn hơn minimum requirement.

## 20. Rollover và financing ảnh hưởng equity

Position giữ lâu có financing debit/credit. Với leveraged position lớn, cost nhỏ theo notional có thể trở thành đáng kể so với equity.

Ví dụ financing cost annualized chỉ vài phần trăm của notional nhưng effective leverage cao:

```text
small % of large notional
→ material % of account equity
```

Do đó backtest swing/carry strategy phải include financing.

## 21. Drawdown math

Nếu account mất:

```text
10% → cần +11.1% để hồi phục
20% → cần +25%
50% → cần +100%
```

Loss và recovery không đối xứng.

Leverage cao làm account dễ rơi vào vùng mà mathematical recovery trở nên khó.

Mục tiêu risk management vì vậy không chỉ là tránh bankruptcy, mà là **preserve compounding capacity**.

## 22. Risk of ruin

**Risk of ruin** là xác suất capital rơi xuống mức không thể tiếp tục strategy theo cách dự kiến.

Nó tăng khi:

- risk per trade tăng;
- edge nhỏ hoặc không chắc;
- payoff distribution có fat tails;
- trades correlated;
- leverage cao;
- execution loss lớn hơn model;
- trader thay đổi rule sau drawdown.

Một strategy có positive expectancy vẫn có thể ruin nếu sizing quá lớn.

## 23. Sequence risk

Hai traders có cùng 60 wins và 40 losses nhưng thứ tự trade khác nhau có thể trải qua drawdown rất khác nếu sizing phụ thuộc current equity hoặc leverage.

Đây là lý do Monte Carlo reshuffling hữu ích:

```text
same trade distribution
→ many possible sequences
→ distribution of drawdowns
```

Backtest equity curve duy nhất không cho thấy đầy đủ path risk.

## 24. Kelly criterion: tối ưu growth không đồng nghĩa dễ chịu hay robust

Kelly framework liên hệ optimal betting fraction với edge/payoff dưới assumptions cụ thể.

Vấn đề trong trading thực tế:

- true edge không biết chính xác;
- distribution thay đổi;
- tail risk bị estimate kém;
- transaction cost thay đổi;
- psychological tolerance thấp hơn mathematical tolerance.

Vì vậy nếu dùng Kelly trong research, thường cần hiểu fractional Kelly và estimation error. Không nên lấy một Kelly fraction từ backtest nhỏ rồi coi là “size tối ưu”.

## 25. Margin stress test

Một position plan nên kiểm tra ít nhất vài scenario:

```text
Normal adverse move
Large adverse move
Gap through stop
Spread doubles/triples
Multiple correlated positions move together
Broker raises margin requirement
Financing cost increases
```

Với mỗi scenario, tính:

```text
P/L
Equity
Used Margin
Free Margin
Margin Level
Remaining Gross Leverage
```

Risk plan chỉ nhìn stop-loss mà không nhìn margin dynamics là chưa đủ cho leveraged product.

## 26. Leverage và time horizon

Shorter timeframe không tự động cho phép leverage cao hơn an toàn.

Intraday strategy có thể tránh overnight gap nhưng lại chịu:

- nhiều transaction costs;
- execution noise;
- event spikes;
- operational risk;
- latency/slippage.

Longer horizon có fewer trades nhưng chịu overnight/weekend risk và financing lâu hơn.

Leverage phải phù hợp **distribution of adverse moves**, không chỉ holding period label.

## 27. Broker margin có thể thay đổi

Margin requirement không nhất thiết cố định mãi.

Trong stress hoặc quanh sự kiện, broker/venue/risk system có thể thay đổi margin according to terms/rules.

Nếu strategy chỉ tồn tại vì đang dùng gần maximum allowed leverage:

```text
margin increase
→ forced deleveraging
→ bad execution timing
```

Đó là structural fragility.

## 28. Một trade plan đầy đủ nên ghi gì?

Ví dụ:

```text
Account equity: 20,000 USD
Pair: EUR/USD
Thesis: ...
Entry: 1.1200
Invalidation: 1.1160
Stop distance: 40 pips
Allowed planned loss: 100 USD
Pip value target: 2.5 USD/pip
Base size: ~25,000 EUR
Notional in USD: ~28,000 USD at entry
Effective leverage from this position: ~1.4x
Existing correlated exposure: ...
Estimated transaction cost: ...
Gap/event risk: ...
Portfolio heat after entry: ...
```

Notice rằng `0.25 lot` chỉ là một dòng trong risk specification, không phải trung tâm của plan.

## 29. Sai lầm cần loại bỏ

### “Margin là tiền mất tối đa”

Sai. Margin là collateral requirement.

### “Broker cho leverage 1:100 nên dùng 100x mới hiệu quả vốn”

Sai. Maximum buying power không phải recommended exposure.

### “Có stop-loss nên không thể mất hơn planned risk”

Sai trong gap/slippage hoặc operational failure.

### “Mỗi trade risk 1% nên 10 trades = diversified”

Sai nếu trades cùng factor.

### “Lot nhỏ nghĩa là risk nhỏ”

Chưa đủ. Cần stop distance, pip value, volatility và account size.

### “Không bị margin call nghĩa là position an toàn”

Sai. Account có thể chịu drawdown rất lớn trước liquidation threshold.

## 30. Checklist trước khi học macro drivers

Bạn cần tự giải thích được:

1. Notional, margin và risk khác nhau thế nào.
2. Effective leverage khác broker maximum leverage ra sao.
3. Equity giảm làm leverage tự tăng như thế nào.
4. Margin level được hình thành từ equity/used margin ra sao.
5. Vì sao stop-out không phải risk plan.
6. Cách sizing từ allowed loss và invalidation distance.
7. Vì sao correlated positions làm portfolio heat lớn hơn tưởng tượng.
8. Vì sao gap/slippage khiến planned loss chỉ là estimate.
9. Vì sao margin headroom quan trọng ngay cả khi mỗi trade có stop.

## Nối sang chương tiếp theo

Sau khi biết position tạo risk ra sao, câu hỏi tiếp theo là: **điều gì làm relative value của hai currency thay đổi?**

→ [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

## Nguồn và liên kết

- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- CFTC — Foreign Currency (Forex) Fraud / risk information: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_forex.html
- [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)
