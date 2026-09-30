# 03 — Leverage, margin và position sizing

Forex retail hấp dẫn một phần vì broker có thể cho phép kiểm soát **giá trị danh nghĩa (notional)** lớn hơn nhiều so với cash trong account. Chính cơ chế này cũng là nguồn của phần lớn hiểu nhầm nguy hiểm nhất.

Ba khái niệm phải tách hoàn toàn:

```text
Notional Exposure
≠ Margin Requirement
≠ Amount at Risk
```

**Đòn bẩy (leverage, 레버리지)** nói về quan hệ giữa exposure và capital/equity. **Ký quỹ (margin, 증거금)** là collateral broker yêu cầu để duy trì position. **Amount at rủi ro (risk / 위험)** là mức mất mát (loss / 손실) có thể xảy ra theo price đường dẫn (path / 경로), stop, gap, slippage và các điều khoản liquidation. Ba con số này liên hệ với nhau nhưng không thay thế nhau.

## 1. Leverage không tạo ra edge

Giả sử account có 10.000 USD và mở 100.000 USD notional exposure.

Effective leverage xấp xỉ:

```text
Effective Leverage
= Gross Notional / Account Equity
= 100,000 / 10,000
= 10x
```

Nếu underlying exposure giảm 1% và bỏ qua chi phí (cost / 비용):

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

Broker có thể quảng cáo maximum leverage, ví dụ `1:30`, `1:50`, `1:100` hoặc mức khác tùy jurisdiction/sản phẩm (product / 제품)/máy khách (client / 클라이언트) classification.

Nhưng nếu broker cho phép `1:100`, trader không bắt buộc dùng 100x.

Ví dụ account 10.000 USD, broker cho maximum 100x nhưng trader chỉ mở 20.000 USD notional:

```text
Effective leverage = 20,000 / 10,000 = 2x
```

Do đó câu hỏi đúng không phải:

> Broker cho tôi leverage bao nhiêu?

mà là:

> Tổng notional exposure hiện tại bằng bao nhiêu lần equity và account sẽ mất bao nhiêu nếu thị trường (market / 시장) di chuyển bất lợi theo các stress scenario?

## 3. Margin yêu cầu (requirement / 요구사항)

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

Cũng có thể biểu diễn bằng margin tỷ lệ (rate / 비율):

```text
Margin Rate = 1 / Leverage
```

20x tương đương khoảng 5% margin yêu cầu (requirement / 요구사항).

Nhưng broker thực tế có thể tính margin theo đặc tả hợp đồng (contract / 계약) specification, pair, account currency, tiered notional, volatility regime hoặc regulatory quy tắc (rule / 규칙). Công thức trên là mô hình tư duy (mental model / 사고 모델), không thay thế quy tắc (rule / 규칙) của broker.

## 4. Margin không phải maximum mất mát (loss / 손실)

Đây là distinction quan trọng nhất.

Nếu broker yêu cầu 2.000 USD margin cho position 100.000 USD, không có nghĩa mất mát (loss / 손실) bị giới hạn ở 2.000 USD.

P/L vẫn được tạo từ **100.000 USD exposure**.

Trong thị trường (market / 시장) move lớn hoặc gap:

```text
Loss can consume margin
→ consume remaining equity
→ potentially exceed planned loss
```

Treatment của negative balance phụ thuộc jurisdiction, máy khách (client / 클라이언트) kiểu (type / 타입) và contractual terms. Không được giả định protection tồn tại nếu chưa kiểm tra.

CFTC cũng nhấn mạnh leverage trong retail OTC forex có thể khuếch đại mất mát (loss / 손실) mạnh và customer cần hiểu margin obligation trước khi giao dịch.

## 5. Balance, equity, used margin và free margin

### Balance

Balance thường phản ánh account giá trị (value / 값) sau các giao dịch (transaction / 트랜잭션) đã realized, chưa bao gồm floating P/L của open positions theo cách hiển thị phổ biến.

### Equity
Phần “Equity” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


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
- margin yêu cầu (requirement / 요구사항) tăng.

## 6. Margin mức (level / 수준)

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

Broker có thể đặt threshold riêng cho margin lời gọi (call / 호출) hoặc automatic stop-out. Không có một universal stop-out percentage cho mọi broker.

## 7. Margin lời gọi (call / 호출) và stop-out không giống stop-loss

### Stop-loss

Thứ tự (order / 순서) do chiến lược (strategy / 전략)/trader đặt để cố thoát khi thị trường (market / 시장) tới một mức nhất định.

### Margin lời gọi (call / 호출) / stop-out

Risk-control cơ chế (mechanism / 메커니즘) của broker/account, xảy ra khi account không còn đủ collateral theo quy tắc (rule / 규칙).

Nếu để position đi đến stop-out, trader đã chuyển quyền kiểm soát exit từ chiến lược (strategy / 전략) sang margin hệ thống (system / 시스템).

Một rủi ro (risk / 위험) tiến trình (process / 프로세스) tốt thường không dựa vào:

```text
“I will be liquidated before things get too bad.”
```

Liquidation có thể xảy ra trong điều kiện spread rộng và liquidity xấu, chính là lúc thực thi (execution / 실행) chất lượng (quality / 품질) giảm.

## 8. Effective leverage tăng khi equity giảm

Giả sử gross notional giữ nguyên 100.000 USD.

Ban đầu:

```text
Equity = 20,000
Effective leverage = 5x
```

Sau mất mát (loss / 손실):

```text
Equity = 10,000
Effective leverage = 10x
```

Không cần mở thêm trade, portfolio đã **tự trở nên leveraged hơn** khi equity giảm.

Đây là vòng phản hồi (feedback loop / 피드백 루프) nguy hiểm:

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

Net USD exposure có thể nhỏ hơn gross exposure, nhưng portfolio vẫn có substantial EUR-vs-GBP relative exposure và thực thi (execution / 실행)/liquidity rủi ro (risk / 위험) ở cả hai legs.

Một approximate gross leverage chỉ số (metric / 지표):

```text
Gross Leverage
= Sum(|Position Notional|) / Equity
```

Netting chỉ theo USD có thể che giấu cross-currency rủi ro (risk / 위험).

## 10. Position sizing phải bắt đầu từ vô hiệu hóa (invalidation / 무효화)

Một trade setup cần trả lời:

1. Thesis là gì?
2. Điều kiện nào làm thesis sai hoặc setup invalid?
3. Từ entry đến vô hiệu hóa (invalidation / 무효화) bao xa?
4. Account chấp nhận mất bao nhiêu nếu scenario đó xảy ra?
5. Kích thước (size / 크기) nào biến distance đó thành allowed mất mát (loss / 손실)?

Luồng (flow / 흐름):

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

đối với cấu trúc (structure / 구조) đơn giản như EUR/USD account USD.

## 12. Ví dụ sizing

Account equity:

```text
20,000 USD
```

Giả sử research chính sách (policy / 정책) cho phép initial planned rủi ro (risk / 위험) `0.5%` equity cho một trade:

```text
Allowed Loss
= 20,000 × 0.005
= 100 USD
```

Setup EUR/USD có vô hiệu hóa (invalidation / 무효화) 40 pips.

Required pip giá trị (value / 값):

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

Đây chỉ là planned mất mát (loss / 손실) **trước** slippage, gap và some costs.

## 13. Fixed percentage rủi ro (risk / 위험) có lợi ích gì?

Nếu mỗi trade rủi ro (risk / 위험) một fraction của hiện tại (current / 현재) equity, kích thước (size / 크기) tự co lại sau drawdown và tăng dần khi equity tăng.

Ví dụ rủi ro (risk / 위험) 1%:

```text
Equity 10,000 → planned risk 100
Equity 8,000  → planned risk 80
```

Cơ chế này giảm tốc độ mất vốn tương đối so với fixed-dollar rủi ro (risk / 위험) khi account giảm mạnh.

Nhưng fixed percentage không tự tạo edge. Một chiến lược (strategy / 전략) có negative expectancy vẫn mất tiền, chỉ có thể mất chậm hơn.

## 14. Vì sao “rủi ro (risk / 위험) 2% mỗi trade” không phải quy tắc universal?

Các con số như 1% hoặc 2% thường được truyền như rule-of-thumb. Không có một tỷ lệ phù hợp cho mọi chiến lược (strategy / 전략).

Rủi ro (risk / 위험) fraction cần phụ thuộc:

- edge bất định (uncertainty / 불확실성);
- stop hành vi (behavior / 동작);
- return phân phối (distribution / 분포);
- gap/tail rủi ro (risk / 위험);
- number of simultaneous positions;
- correlation;
- chiến lược (strategy / 전략) frequency;
- maximum tolerable drawdown;
- operational các ràng buộc (constraints / 제약조건들).

Một chiến lược (strategy / 전략) có nhiều correlated trades không thể đánh giá rủi ro (risk / 위험) từng trade riêng lẻ.

## 15. Portfolio heat

**Portfolio heat** là tổng planned mất mát (loss / 손실)/exposure nếu nhiều positions cùng đi tới stop hoặc stress threshold.

Ví dụ có 5 trades, mỗi trade planned `1%` account rủi ro (risk / 위험). Không nên ngay lập tức kết luận portfolio rủi ro (risk / 위험) là “an toàn vì mỗi trade chỉ 1%”.

Nếu cả 5 đều là variants của short USD:

```text
USD shock
→ multiple stops hit together
→ slippage correlated
→ portfolio loss clusters
```

Cần stress cả **dùng chung (common / 공통) factor**.

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

Một rủi ro (risk / 위험) dashboard tốt nên aggregate theo currency:

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

Một fixed 20-pip stop có ý nghĩa rất khác khi pair daily phạm vi (range / 범위) là 40 pips so với 200 pips.

Nếu stop nằm bên trong normal noise, chiến lược (strategy / 전략) có thể bị exit liên tục dù thesis chưa invalidated.

Có thể dùng volatility measure như ATR hoặc realized volatility để **normalize ngữ cảnh (context / 맥락)**, nhưng indicator không quyết định stop thay cho thesis.

Mô hình tư duy (mental model / 사고 모델):

```text
Market structure / thesis invalidation
+ volatility context
→ stop distance
→ size adjusted to keep account risk controlled
```

Không nên giữ kích thước (size / 크기) cố định rồi nới stop trong high volatility; làm vậy rủi ro (risk / 위험) tăng hai lần.

## 18. Gap rủi ro (risk / 위험)

FX spot thường giao dịch gần liên tục trong tuần, nhưng gap vẫn có thể xảy ra:

- weekend reopen;
- unexpected geopolitical sự kiện (event / 이벤트);
- sudden chính sách (policy / 정책) announcement;
- liquidity vacuum;
- instrument-specific trading halt/price discontinuity.

Stop thứ tự (order / 순서) chỉ kích hoạt thực thi (execution / 실행); nó không guarantee chính xác (exact / 정확한) fill.

Planned mất mát (loss / 손실):

```text
100 USD
```

có thể thành:

```text
150 / 300 / more
```

nếu price jumps qua stop.

Rủi ro (risk / 위험) mô hình (model / 모델) phải có tail scenario thay vì giả định continuous price đường dẫn (path / 경로).

## 19. Spread widening cũng làm liquidation pressure tăng

Floating P/L thường được marked theo executable bid/ask side. Khi spread widen mạnh:

```text
mark-to-market loss increases
→ equity falls
→ free margin falls
→ margin level falls
```

Ngay cả khi mid-price không di chuyển nhiều, account có thể chịu stress từ spread.

Đây là lý do margin headroom cần lớn hơn minimum yêu cầu (requirement / 요구사항).

## 20. Rollover và financing ảnh hưởng equity

Position giữ lâu có financing debit/credit. Với leveraged position lớn, chi phí (cost / 비용) nhỏ theo notional có thể trở thành đáng kể so với equity.

Ví dụ financing chi phí (cost / 비용) annualized chỉ vài phần trăm của notional nhưng effective leverage cao:

```text
small % of large notional
→ material % of account equity
```

Do đó backtest swing/carry chiến lược (strategy / 전략) phải include financing.

## 21. Drawdown math

Nếu account mất:

```text
10% → cần +11.1% để hồi phục
20% → cần +25%
50% → cần +100%
```

Mất mát (loss / 손실) và khôi phục (recovery / 복구) không đối xứng.

Leverage cao làm account dễ rơi vào vùng mà mathematical khôi phục (recovery / 복구) trở nên khó.

Mục tiêu rủi ro (risk / 위험) management vì vậy không chỉ là tránh bankruptcy, mà là **preserve compounding sức chứa (capacity / 용량)**.

## 22. Rủi ro (risk / 위험) of ruin

**Rủi ro (risk / 위험) of ruin** là xác suất capital rơi xuống mức không thể tiếp tục chiến lược (strategy / 전략) theo cách dự kiến.

Nó tăng khi:

- rủi ro (risk / 위험) per trade tăng;
- edge nhỏ hoặc không chắc;
- payoff phân phối (distribution / 분포) có fat tails;
- trades correlated;
- leverage cao;
- thực thi (execution / 실행) mất mát (loss / 손실) lớn hơn mô hình (model / 모델);
- trader thay đổi quy tắc (rule / 규칙) sau drawdown.

Một chiến lược (strategy / 전략) có positive expectancy vẫn có thể ruin nếu sizing quá lớn.

## 23. Chuỗi (sequence / 시퀀스) rủi ro (risk / 위험)

Hai traders có cùng 60 wins và 40 losses nhưng thứ tự trade khác nhau có thể trải qua drawdown rất khác nếu sizing phụ thuộc hiện tại (current / 현재) equity hoặc leverage.

Đây là lý do Monte Carlo reshuffling hữu ích:

```text
same trade distribution
→ many possible sequences
→ distribution of drawdowns
```

Backtest equity curve duy nhất không cho thấy đầy đủ đường dẫn (path / 경로) rủi ro (risk / 위험).

## 24. Kelly criterion: tối ưu growth không đồng nghĩa dễ chịu hay robust

Kelly khung phần mềm (framework / 프레임워크) liên hệ optimal betting fraction với edge/payoff dưới các giả định (assumptions / 가정들) cụ thể.

Vấn đề trong trading thực tế:

- true edge không biết chính xác;
- phân phối (distribution / 분포) thay đổi;
- tail rủi ro (risk / 위험) bị estimate kém;
- giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) thay đổi;
- psychological tolerance thấp hơn mathematical tolerance.

Vì vậy nếu dùng Kelly trong research, thường cần hiểu fractional Kelly và estimation lỗi (error / 오류). Không nên lấy một Kelly fraction từ backtest nhỏ rồi coi là “kích thước (size / 크기) tối ưu”.

## 25. Margin kiểm thử sức chịu tải (stress test / 스트레스 테스트)

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

Rủi ro (risk / 위험) plan chỉ nhìn stop-loss mà không nhìn margin dynamics là chưa đủ cho leveraged sản phẩm (product / 제품).

## 26. Leverage và thời gian (time / 시간) horizon

Shorter timeframe không tự động cho phép leverage cao hơn an toàn.

Intraday chiến lược (strategy / 전략) có thể tránh overnight gap nhưng lại chịu:

- nhiều giao dịch (transaction / 트랜잭션) costs;
- thực thi (execution / 실행) noise;
- sự kiện (event / 이벤트) spikes;
- operational rủi ro (risk / 위험);
- độ trễ (latency / 지연 시간)/slippage.

Longer horizon có fewer trades nhưng chịu overnight/weekend rủi ro (risk / 위험) và financing lâu hơn.

Leverage phải phù hợp **phân phối (distribution / 분포) of adverse moves**, không chỉ holding period label.

## 27. Broker margin có thể thay đổi

Margin yêu cầu (requirement / 요구사항) không nhất thiết cố định mãi.

Trong stress hoặc quanh sự kiện, broker/venue/rủi ro (risk / 위험) hệ thống (system / 시스템) có thể thay đổi margin according to terms/rules.

Nếu chiến lược (strategy / 전략) chỉ tồn tại vì đang dùng gần maximum allowed leverage:

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

Notice rằng `0.25 lot` chỉ là một dòng trong rủi ro (risk / 위험) specification, không phải trung tâm của plan.

## 29. Sai lầm cần loại bỏ

### “Margin là tiền mất tối đa”

Sai. Margin là collateral yêu cầu (requirement / 요구사항).

### “Broker cho leverage 1:100 nên dùng 100x mới hiệu quả vốn”

Sai. Maximum buying power không phải recommended exposure.

### “Có stop-loss nên không thể mất hơn planned rủi ro (risk / 위험)”

Sai trong gap/slippage hoặc operational thất bại (failure / 실패).

### “Mỗi trade rủi ro (risk / 위험) 1% nên 10 trades = diversified”

Sai nếu trades cùng factor.

### “Lot nhỏ nghĩa là rủi ro (risk / 위험) nhỏ”

Chưa đủ. Cần stop distance, pip giá trị (value / 값), volatility và account kích thước (size / 크기).

### “Không bị margin lời gọi (call / 호출) nghĩa là position an toàn”

Sai. Account có thể chịu drawdown rất lớn trước liquidation threshold.

## 30. Checklist trước khi học macro drivers

Bạn cần tự giải thích được:

1. Notional, margin và rủi ro (risk / 위험) khác nhau thế nào.
2. Effective leverage khác broker maximum leverage ra sao.
3. Equity giảm làm leverage tự tăng như thế nào.
4. Margin mức (level / 수준) được hình thành từ equity/used margin ra sao.
5. Vì sao stop-out không phải rủi ro (risk / 위험) plan.
6. Cách sizing từ allowed mất mát (loss / 손실) và vô hiệu hóa (invalidation / 무효화) distance.
7. Vì sao correlated positions làm portfolio heat lớn hơn tưởng tượng.
8. Vì sao gap/slippage khiến planned mất mát (loss / 손실) chỉ là estimate.
9. Vì sao margin headroom quan trọng ngay cả khi mỗi trade có stop.

## Nối sang chương tiếp theo

Sau khi biết position tạo rủi ro (risk / 위험) ra sao, câu hỏi tiếp theo là: **điều gì làm relative giá trị (value / 값) của hai currency thay đổi?**

→ [04 — Macro drivers, rates, carry and sessions](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

## Nguồn và liên kết
Phần “Nguồn và liên kết” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- CFTC — Foreign Currency (Forex) Fraud / rủi ro (risk / 위험) thông tin (information / 정보): https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_forex.html
- [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)
- [Systematic risk, backtest and execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)
