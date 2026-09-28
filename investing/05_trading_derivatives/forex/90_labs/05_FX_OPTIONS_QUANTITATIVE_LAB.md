# Lab 05 — FX Options Quantitative Lab

> **Mạch đọc:** Đặt **Lab 05 — FX Options Quantitative Lab** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Quy ước và đầu ra** sang **2. trường hợp (case / 사례) A — Từ forward đến premium**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Lab này chuyển chapter `14` từ vocabulary sang một bài tính có thể kiểm tra. Mục tiêu không phải tìm một option “đang rẻ” hay hứa hẹn lợi nhuận. Mục tiêu là tách được:

```text
forward / discounting
→ option premium
→ Greeks
→ scenario P/L
→ delta-hedging path
→ implied-vs-realized attribution
```

Mọi số liệu trong trường hợp (case / 사례) dưới đây là **simulation**. Nếu thay bằng thị trường (market / 시장) dữ liệu (data / 데이터) thật, phải ghi timestamp, currency convention, volatility nguồn (source / 소스), bid/ask và quy ước delta. Không dùng kết quả của lab làm khuyến nghị giao dịch.

## 1. Quy ước và đầu ra

Chọn một reporting currency và giữ nhất quán đơn vị. Trong lab này:

```text
Spot S       = USD per EUR
Domestic ccy = USD
Foreign ccy  = EUR
Notional     = EUR 1,000,000
Maturity     = 3 months = 0.25 years
```

Theo quy ước `USD/EUR`, một EUR lời gọi (call / 호출) là quyền mua EUR và bán USD. Đây là lời gọi (call / 호출) trên `S`; một EUR put là quyền bán EUR. Nếu dữ liệu thị trường (market / 시장) dùng `EUR/USD`, phải đảo quote và payoff trước khi tính, không chỉ đổi nhãn.

Tạo các sản phẩm tạo ra (artifact / 산출물) sau:

```text
fx_option_quote_sheet.md
fx_option_greeks_scenarios.csv hoặc bảng tương đương
fx_delta_hedge_ledger.md
fx_option_attribution.md
```

Trong mỗi sản phẩm tạo ra (artifact / 산출물), ghi rõ:

```text
as_of_timestamp
spot / forward convention
discounting convention
volatility convention
delta convention
rounding rule
source hoặc simulation flag
```


> **Chuyển mạch:** Từ **1. Quy ước và đầu ra**, ta sang **2. trường hợp (case / 사례) A — Từ forward đến premium** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. trường hợp (case / 사례) A — Từ forward đến premium

Giả sử thị trường cung cấp:

```text
Spot S_0                 = 1.0850 USD/EUR
USD continuously comp.  = 5.00% annualized
EUR continuously comp.  = 3.00% annualized
Time to expiry T         = 0.25 years
Strike K                 = 1.0900 USD/EUR
Volatility σ             = 8.00% annualized
EUR notional             = 1,000,000 EUR
```

### Bước 1 — Forward kiểm tra trước

Dùng simplified Garman–Kohlhagen convention:

```text
F_0 = S_0 × exp((r_USD − r_EUR) × T)
```

Tính `F_0` và giải thích tại sao quote này có thể khác spot dù chưa có view directional. Tách rõ:

```text
forward carry / rate differential
vs
expected future spot
```

Forward price là no-arbitrage pricing đối tượng (object / 객체) dưới các giả định funding/collateral, không phải cam kết dự báo spot tại expiry.

### Bước 2 — Black–Scholes/Garman–Kohlhagen premium

Với European lời gọi (call / 호출)/put trên foreign currency, dùng:

```text
d1 = [ln(S_0 / K) + (r_USD − r_EUR + 0.5σ²)T] / (σ√T)
d2 = d1 − σ√T

Call_USD_per_EUR = S_0 exp(−r_EUR T) N(d1)
                  − K exp(−r_USD T) N(d2)

Put_USD_per_EUR  = K exp(−r_USD T) N(−d2)
                  − S_0 exp(−r_EUR T) N(−d1)
```

Tính premium trên mỗi EUR và tổng premium cho `1,000,000 EUR`. Kiểm tra put–lời gọi (call / 호출) parity:

```text
Call − Put = S_0 exp(−r_EUR T) − K exp(−r_USD T)
```

Nếu parity không khớp, tìm lỗi ở quote direction, discount factor, normal CDF hoặc scaling notional trước khi tiếp tục. Không sửa sai bằng cách làm tròn mạnh hơn.

### Bước 3 — Sanity checks

Kiểm tra bằng lập luận dấu và giới hạn:

```text
Call ≥ 0 và Put ≥ 0
Call không vượt quá discounted foreign notional
K tăng → call giảm, put tăng, all else equal
σ tăng → vanilla call và put thường tăng giá
```

Các nhận định “thường” ở trên không thay thế đạo hàm hoặc tính toán cụ thể. Ghi những trường hợp mà funding, quote convention hoặc premium adjustment có thể làm intuition đơn giản sai.


> **Chuyển mạch:** Từ **2. trường hợp (case / 사례) A — Từ forward đến premium**, ta sang **3. trường hợp (case / 사례) B — Greeks và rủi ro (risk / 위험) decomposition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. trường hợp (case / 사례) B — Greeks và rủi ro (risk / 위험) decomposition

Từ cùng một trạng thái (state / 상태) ở trường hợp (case / 사례) A, tính hoặc xấp xỉ:

```text
spot delta
gamma
vega cho 1 volatility point và cho 1.00 volatility unit
theta theo ngày calendar hoặc trading day — ghi rõ lựa chọn
rho_USD và rho_EUR nếu mô hình hỗ trợ
```

Có thể dùng công thức analytic của mô hình hoặc finite difference. Nếu dùng finite difference, ghi step kích thước (size / 크기) và kiểm tra độ ổn định bằng ít nhất hai step sizes.

Bảng kết quả phải có cả dấu và đơn vị:

| rủi ro (risk / 위험) | Định nghĩa | Đơn vị cần ghi | Câu hỏi kiểm tra |
|---|---|---|---|
| Delta | `∂V/∂S` | USD P/L cho 1 đơn vị spot hoặc EUR-equivalent | Position đang long hay short EUR theo quote? |
| Gamma | `∂²V/∂S²` | thay đổi delta khi spot đổi | Delta thay đổi nhanh ở vùng nào? |
| Vega | `∂V/∂σ` | USD cho `+1.00` vol và `+1 vol point` | Có đang nhầm 1% với 1.00 không? |
| Theta | thời gian (time / 시간) decay all else equal | USD/ngày theo convention | Có nhầm theta mô hình (model / 모델) với realized P/L không? |
| Rho | tỷ lệ (rate / 비율) sensitivity | USD cho một rate-point hoặc đơn vị (unit / 단위) | tỷ lệ (rate / 비율) nào là domestic, tỷ lệ (rate / 비율) nào là foreign? |

Đừng kết luận “delta-neutral = risk-neutral”. Một position có delta gần 0 vẫn giữ gamma, vega, theta, skew, jump và liquidity rủi ro (risk / 위험).


> **Chuyển mạch:** Từ **3. trường hợp (case / 사례) B — Greeks và rủi ro (risk / 위험) decomposition**, ta sang **4. trường hợp (case / 사례) C — Scenario grid, không chỉ nhìn expiry** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. trường hợp (case / 사례) C — Scenario grid, không chỉ nhìn expiry

Tạo grid với ít nhất:

```text
Spot: 1.0000, 1.0400, 1.0850, 1.1300, 1.1700
Vol:  6%, 8%, 10%, 14%
Time: 0.25 năm và 0.05 năm
```

Giữ các biến không nêu trong từng scenario cố định. Với mỗi ô, tính:

```text
option value
intrinsic value nếu đã gần expiry
time value
delta / vega nếu có thể
P/L so với initial premium
```

Sau đó mô tả ít nhất bốn đường dẫn (path / 경로):

```text
1. EUR tăng vừa phải, vol giảm
2. EUR tăng mạnh, vol tăng
3. EUR gần như đi ngang, vol crush
4. Spot gap qua strike khi thời gian còn rất ít
```

Mục tiêu là chứng minh bằng con số vì sao:

```text
đúng hướng spot ≠ chắc chắn lãi option
spot đi ngang ≠ chắc chắn lỗ nếu long gamma được realized đủ lớn
IV giảm sau event có thể xóa lợi ích của spot move
```

Đối với mỗi đường dẫn (path / 경로), ghi driver chính của P/L theo thứ tự gần đúng:

```text
delta contribution
gamma / convexity contribution
vega / IV repricing
theta / time decay
hedging and transaction cost
```

Không cộng các Greeks như thể chúng là chính xác (exact / 정확한) decomposition cho một move lớn. Với move lớn hoặc gap, dùng full revaluation rồi coi Greek approximation là diagnostic.


> **Chuyển mạch:** Từ **4. trường hợp (case / 사례) C — Scenario grid, không chỉ nhìn expiry**, ta sang **5. trường hợp (case / 사례) D — sự kiện (event / 이벤트) straddle và implied move** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. trường hợp (case / 사례) D — sự kiện (event / 이벤트) straddle và implied move

Giả sử một ATM 1-week EUR/USD straddle có tổng premium `0.90%` của notional. Chọn và ghi rõ cách quy đổi premium thành implied move heuristic.

So sánh:

```text
break-even move ở expiry
market-implied move heuristic
realized move quan sát được sau event
```

Không gọi implied move là hỗ trợ (support / 지원)/resistance. Hãy trả lời:

```text
Premium đã bao gồm volatility risk premium và transaction cost chưa?
ATM là spot ATM hay forward/delta-neutral ATM?
Có event gap, weekend hoặc fixing risk bị bỏ qua không?
Nếu IV crush nhưng spot move lớn hơn implied move thì long straddle có chắc lãi không?
```

Nếu dùng dữ liệu lịch sử, snapshot IV phải là dữ liệu có sẵn trước sự kiện (event / 이벤트); không được lấy volatility surface sau sự kiện (event / 이벤트) rồi kể ngược.


> **Chuyển mạch:** Từ **5. trường hợp (case / 사례) D — sự kiện (event / 이벤트) straddle và implied move**, ta sang **6. trường hợp (case / 사례) E — rủi ro (risk / 위험) reversal và butterfly** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. trường hợp (case / 사례) E — rủi ro (risk / 위험) reversal và butterfly

Dùng bảng quote simulation:

```text
25Δ call IV = 9.20%
ATM IV      = 8.00%
25Δ put IV  = 8.60%
```

Tính theo convention đã chọn:

```text
25Δ risk reversal = IV_25Δ_call − IV_25Δ_put
25Δ butterfly     = 0.5 × (IV_25Δ_call + IV_25Δ_put) − IV_ATM
```

Sau đó ghi rõ giới hạn của phép tính:

```text
delta matching phụ thuộc spot/forward/premium-adjusted convention
call/put wing không nhất thiết cùng strike distance
quoted RR/BF convention thay đổi theo thị trường
IV quote không tự nói về executable bid/ask hoặc hedge cost
```

Vẽ hoặc lập bảng volatility smile đơn giản. Không dùng RR dương như một directional tín hiệu (signal / 신호) tự động; nó có thể phản ánh hedging demand, supply/demand imbalance hoặc rủi ro (risk / 위험) premium.

Nếu có dữ liệu strike/delta dày hơn, nội suy một điểm ở giữa hai quote bằng một quy tắc (rule / 규칙) đã khóa trước, chẳng hạn tuyến tính (linear / 선형) theo delta hoặc tuyến tính (linear / 선형) theo log-moneyness. So sánh kết quả của hai quy tắc (rule / 규칙) và kiểm tra:

```text
interpolated IV không nhảy bất thường giữa các quote
strike ordering và delta ordering vẫn nhất quán
surface không bị dùng như executable price nếu chưa có bid/ask
```

Mục tiêu là hiểu interpolation là một giả định của research chuỗi xử lý (pipeline / 파이프라인), không phải quan sát trực tiếp từ thị trường.


> **Chuyển mạch:** Từ **6. trường hợp (case / 사례) E — rủi ro (risk / 위험) reversal và butterfly**, ta sang **7. trường hợp (case / 사례) F — Delta hedge ledger** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. trường hợp (case / 사례) F — Delta hedge ledger

Chọn long lời gọi (call / 호출) ở trường hợp (case / 사례) A. Giả sử hedge tại các thời điểm:

```text
t0: spot 1.0850, option delta theo mô hình
t1: spot 1.0950, còn 0.20 năm, IV thay đổi theo scenario
t2: spot 1.0750, còn 0.10 năm, IV thay đổi theo scenario
t3: expiry
```

Lập ledger từng bước:

```text
timestamp
spot / forward
time remaining
IV snapshot
option value
model delta trước hedge
underlying hedge trade
hedge price
cash balance
spread / commission / slippage
option P/L
hedge P/L
financing / discount adjustment
combined P/L
```

Nếu mô phỏng delta hedge, nêu quy tắc (rule / 규칙) trước khi chạy:

```text
rehedge mỗi ngày
hoặc rehedge khi |delta| vượt threshold
hoặc rehedge theo event schedule
```

So sánh ít nhất hai quy tắc (rule / 규칙). Một ledger tốt phải cho thấy:

```text
long gamma không đảm bảo hedge P/L dương
discrete hedging bỏ lỡ path giữa hai lần rebalance
transaction cost ăn vào convexity capture
vega và skew có thể chi phối kết quả dù delta đã hedge
```

Tách **mô hình (model / 모델) hedge P/L** khỏi **executable hedge P/L**. Không dùng mid price cho một leg rồi dùng bid/ask cho leg kia mà không ghi rõ.


> **Chuyển mạch:** Từ **7. trường hợp (case / 사례) F — Delta hedge ledger**, ta sang **8. trường hợp (case / 사례) G — Implied-versus-realized attribution** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. trường hợp (case / 사례) G — Implied-versus-realized attribution

Tạo một bảng post-mortem cho option position:

```text
Initial premium / carry
Change in spot
Change in implied volatility
Change in skew / smile
Time decay
Delta hedge result
Funding / discounting
Spread, commission, slippage
Residual / model error
```

Dùng full revaluation làm P/L chính. Dùng Greeks để attribution gần đúng:

```text
ΔV ≈ Delta·ΔS
    + 0.5·Gamma·(ΔS)^2
    + Vega·Δσ
    + Theta·Δt
    + cross-terms / residual
```

Ghi rõ các cross-term bị bỏ qua, ví dụ `vanna`, `volga` hoặc tương tác (interaction / 상호작용) giữa spot và IV. Nếu residual lớn, đó là tín hiệu cần giảm step kích thước (size / 크기), dùng higher-order Greeks hoặc full repricing; không phải lý do để ép attribution khớp bằng tay.


> **Chuyển mạch:** Từ **8. trường hợp (case / 사례) G — Implied-versus-realized attribution**, ta sang **9. dữ liệu (data / 데이터) và hiện thực (implementation / 구현) checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. dữ liệu (data / 데이터) và hiện thực (implementation / 구현) checklist

Trước khi tin vào kết quả, kiểm tra:

```text
[ ] Quote direction đã nhất quán giữa spot, strike, payoff và delta
[ ] Domestic/foreign rate đã gắn đúng currency
[ ] Discounting/collateral convention đã ghi rõ
[ ] Volatility là implied hay realized, mid hay executable
[ ] ATM, 25Δ, RR và butterfly convention đã ghi rõ
[ ] Expiry timestamp, holiday và day-count đã khóa
[ ] Premium scale (per unit, notional, percentage) không bị trộn
[ ] Bid/ask và market-impact assumption có trong hedge ledger
[ ] Không dùng revised/post-event data cho pre-event decision
[ ] Mọi rounding chỉ làm ở bước trình bày cuối
```

Nếu mã (code / 코드) bằng spreadsheet hoặc Python, viết một kiểm thử (test / 테스트) nhỏ cho:

```text
put-call parity
zero-volatility limit gần payoff discounted
monotonicity theo strike và volatility
delta finite-difference vs analytic delta
P/L ledger reconciliation
```


> **Chuyển mạch:** Từ **9. dữ liệu (data / 데이터) và hiện thực (implementation / 구현) checklist**, ta sang **10. Đầu ra đạt yêu cầu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. Đầu ra đạt yêu cầu

Bài đạt khi người đọc có thể trả lời bằng sản phẩm tạo ra (artifact / 산출물), không phải bằng khẩu hiệu:

```text
Option value đang được drive bởi biến nào ở từng scenario?
Vì sao đúng hướng spot nhưng position vẫn lỗ?
Hedge ratio thay đổi thế nào khi spot/vol/time thay đổi?
Bao nhiêu P/L đến từ delta, gamma, vega, theta và cost?
Kết quả là model result, mid-market estimate hay executable result?
Điều gì sẽ làm giả thuyết “long vol có lợi” sai?
```

Không đạt nếu:

```text
chỉ chép công thức nhưng không ghi đơn vị
gọi IV là forecast chắc chắn của realized volatility
coi delta-neutral là không còn rủi ro
dùng RR/BF như tín hiệu direction không điều kiện
bỏ qua quote convention, cost hoặc hedge path
```

Đọc lại:

- [14 — FX options, volatility và hedging](../14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)
- [10 — Backtesting and point-in-time FX data](../10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [12 — Trading journal, review and performance attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [03 — Portfolio FX risk](./03_PORTFOLIO_FX_RISK_LAB.md)

> **Bàn giao:** Sau **10. Đầu ra đạt yêu cầu**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 QUOTES MARGIN AND POSITION SIZING LAB](./00_QUOTES_MARGIN_AND_POSITION_SIZING_LAB.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
