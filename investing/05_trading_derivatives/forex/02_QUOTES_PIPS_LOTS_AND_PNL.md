# 02 — Quotes, pips, lots và cơ chế P/L trong Forex

Sau khi hiểu Forex không phải một centralized exchange duy nhất, bước tiếp theo là hiểu **một quote thực sự nói điều gì và biến động của quote biến thành tiền lời/lỗ như thế nào**.

Đây là phần nên có khả năng tự tính bằng tay. Calculator của broker tiện lợi, nhưng nếu không tự suy luận được P/L thì rất dễ nhầm giữa lot, notional, margin và risk.

Mental model của chương:

```text
Currency pair
→ base / quote relationship
→ trade size in base currency
→ price change
→ P/L in quote currency
→ conversion into account currency
```

## 1. Base currency và quote currency

Với:

```text
EUR/USD = 1.1200
```

EUR là **đồng tiền cơ sở (base currency, 기준통화)**.

USD là **đồng tiền định giá (quote currency / counter currency, 상대통화)**.

Quote nói rằng:

```text
1 EUR costs 1.1200 USD
```

Cách đọc tổng quát:

```text
A/B = X
```

nghĩa là:

```text
1 unit of A = X units of B
```

Nếu `A/B` tăng, A mạnh lên tương đối với B. Nếu `A/B` giảm, A yếu đi tương đối với B.

## 2. Long và short một currency pair nghĩa là gì?

### Long EUR/USD

Bạn nhận exposure:

```text
Long EUR
Short USD
```

Bạn có lợi nếu EUR tăng giá tương đối so với USD.

### Short EUR/USD

Bạn nhận exposure:

```text
Short EUR
Long USD
```

Bạn có lợi nếu EUR giảm giá tương đối so với USD.

Đây là lý do mọi FX position đều chứa **hai currency exposures**. Nói “tôi long EUR” khi thực tế long EUR/USD là chưa đầy đủ; bạn long EUR **against USD**.

## 3. Bid và ask

Một quote executable có hai phía, ví dụ:

```text
EUR/USD
Bid  1.11998
Ask  1.12003
```

Broker/dealer sẵn sàng:

```text
buy EUR from you at Bid
sell EUR to you at Ask
```

Vì thế:

```text
Buy / open long  → thường khớp gần Ask
Sell / open short → thường khớp gần Bid
```

Nếu ngay lập tức đóng position mà market không thay đổi, bạn thường chịu spread.

## 4. Spread

**Chênh lệch mua bán (bid-ask spread, 스프레드)**:

```text
Spread = Ask - Bid
```

Với quote trên:

```text
1.12003 - 1.11998 = 0.00005
```

Nếu pip size là `0.0001`, spread là:

```text
0.5 pip
```

Spread là một phần transaction cost. Effective cost còn có thể gồm:

```text
commission
+ slippage
+ financing / rollover
+ market impact
```

Vì vậy một strategy gross-profitable có thể net-unprofitable sau chi phí.

## 5. Pip là gì?

**Pip** là đơn vị thay đổi giá quy ước.

Đối với nhiều currency pair không có JPY ở quote side:

```text
1 pip = 0.0001
```

Ví dụ:

```text
EUR/USD
1.1200 → 1.1201
= +1 pip
```

Đối với nhiều JPY pair:

```text
1 pip = 0.01
```

Ví dụ:

```text
USD/JPY
150.20 → 150.21
= +1 pip
```

Platform hiện đại thường quote thêm một decimal nhỏ hơn pip, thường gọi là **pipette / fractional pip**.

Ví dụ:

```text
EUR/USD = 1.12003
```

decimal cuối cùng `0.00001` tương ứng 1/10 pip theo convention phổ biến của pair này.

Không nên hard-code convention mà không kiểm tra contract specification, đặc biệt với exotic pair hoặc product khác FX spot convention.

## 6. Lot là gì?

Trong retail FX, **lot** thường là cách biểu diễn trade size theo số units của base currency.

Convention rất phổ biến:

```text
1 standard lot = 100,000 base-currency units
0.1 lot         = 10,000 units
0.01 lot        = 1,000 units
```

Ví dụ:

```text
0.1 lot EUR/USD
= 10,000 EUR exposure on base side
```

Nhưng `lot` là **contract convention**, không phải định luật tự nhiên. Broker hoặc instrument khác có thể dùng contract size khác. Luôn đọc specification.

## 7. Notional là exposure, không phải số tiền ký quỹ

**Giá trị danh nghĩa (notional)** là quy mô kinh tế của position.

Nếu long:

```text
100,000 EUR at EUR/USD = 1.1200
```

base notional là:

```text
100,000 EUR
```

quy đổi theo USD tại thời điểm đó xấp xỉ:

```text
100,000 × 1.1200
= 112,000 USD
```

Nếu broker chỉ yêu cầu margin vài nghìn USD, exposure vẫn là khoảng 112.000 USD. Margin không biến position thành một investment nhỏ hơn; nó chỉ cho phép collateral nhỏ hơn notional.

## 8. Công thức P/L cơ bản khi quote currency là currency bạn muốn tính

Với pair:

```text
A/B
```

trade size `Q` units của base currency A.

Một long position có P/L theo quote currency B gần bằng:

```text
P/L_B = Q × (Exit Price - Entry Price)
```

Một short position:

```text
P/L_B = Q × (Entry Price - Exit Price)
```

Hoặc dùng signed position:

```text
P/L_B = Signed_Q × (Exit - Entry)
```

với `Signed_Q > 0` cho long và `< 0` cho short.

## 9. Ví dụ EUR/USD

Long 1 standard lot:

```text
Q = 100,000 EUR
Entry = 1.1200
Exit  = 1.1250
```

Price change:

```text
1.1250 - 1.1200 = 0.0050
```

Tương đương:

```text
50 pips
```

P/L:

```text
100,000 × 0.0050
= 500 USD
```

Đây là lý do với `100,000` units EUR/USD, khi pip size là `0.0001`:

```text
Pip Value
= 100,000 × 0.0001
= 10 USD/pip
```

50 pips × 10 USD = 500 USD.

## 10. Pip value được suy ra, không cần học thuộc

Với pair `A/B`:

```text
Pip Value in B
= Base Units × Pip Size
```

Ví dụ `10,000 EUR` trên EUR/USD:

```text
10,000 × 0.0001
= 1 USD/pip
```

Ví dụ `100,000 GBP` trên GBP/USD:

```text
100,000 × 0.0001
= 10 USD/pip
```

Điểm quan trọng là pip value phụ thuộc trade size và quote convention.

## 11. JPY pair: vì sao pip value khác?

Long `100,000 USD` trên USD/JPY.

Pip size thường là:

```text
0.01 JPY per USD
```

Pip value theo JPY:

```text
100,000 × 0.01
= 1,000 JPY/pip
```

Nếu account dùng USD, phải convert 1.000 JPY về USD theo tỷ giá hiện tại.

Giả sử USD/JPY khoảng `150`:

```text
1 USD ≈ 150 JPY
```

thì:

```text
1,000 JPY / 150
≈ 6.67 USD/pip
```

Pip value theo USD do đó thay đổi khi USD/JPY thay đổi. Đây là lý do không nên học thuộc “1 lot luôn = 10 USD/pip”. Điều đó chỉ đúng cho một số cấu trúc pair/account currency nhất định.

## 12. Khi account currency khác quote currency

Giả sử account bằng KRW nhưng trade EUR/USD.

P/L trước hết hình thành theo USD:

```text
EUR/USD trade
→ P/L in USD
```

sau đó platform phải quy đổi:

```text
USD P/L
→ KRW P/L
```

Do đó account-level outcome còn chịu conversion rate.

Mental model:

```text
Instrument P/L currency
→ account currency conversion
→ final account P/L
```

Nếu account currency khác cả base lẫn quote, đừng bỏ qua bước conversion.

## 13. Cross currency pair

Một **cross** là pair không dùng USD trực tiếp, ví dụ EUR/JPY hay EUR/GBP.

Cross rate có thể được suy ra từ các pair liên quan.

Nếu:

```text
EUR/USD = 1.1200
USD/JPY = 150.00
```

thì approximate no-arbitrage mid cross:

```text
EUR/JPY
≈ EUR/USD × USD/JPY
≈ 1.1200 × 150
≈ 168.00
```

Thực tế executable cross phải xử lý bid/ask đúng phía, transaction cost và venue differences. Nhưng phép nhân này cho thấy cross rate không phải một con số tách rời khỏi hệ thống FX.

## 14. Khi nào chia thay vì nhân?

Nếu hai pair có cùng quote currency:

```text
EUR/USD
GBP/USD
```

muốn suy ra EUR/GBP:

```text
EUR/GBP
≈ (EUR/USD) / (GBP/USD)
```

Ví dụ:

```text
EUR/USD = 1.1200
GBP/USD = 1.2800
```

thì:

```text
EUR/GBP ≈ 1.1200 / 1.2800
≈ 0.8750
```

Cách tốt nhất không phải học công thức nhân/chia, mà kiểm tra đơn vị như algebra:

```text
USD cancels out
```

## 15. Unit analysis giúp tránh nhầm công thức

Viết quote như fraction của units:

```text
EUR/USD = USD per EUR
USD/JPY = JPY per USD
```

Nhân:

```text
(USD / EUR) × (JPY / USD)
= JPY / EUR
```

USD bị triệt tiêu, còn lại JPY per EUR → chính là EUR/JPY quote.

Cách unit analysis này đáng tin hơn học thuộc mnemonic.

## 16. Direct quote và indirect quote

Khái niệm direct/indirect phụ thuộc home currency của người quan sát.

Nếu home currency là KRW:

```text
USD/KRW
= KRW per USD
```

là cách trực tiếp biểu diễn một USD trị giá bao nhiêu KRW.

Trong tài liệu quốc tế, các pair conventions đã được market standard hóa theo ticker, nên khi trading tốt hơn hết đọc base/quote rõ ràng thay vì phụ thuộc vào từ “direct” có thể gây nhầm theo viewpoint.

## 17. Percentage return và pip move không phải cùng một thứ

EUR/USD tăng:

```text
1.1000 → 1.1100
```

là `100 pips`, nhưng percentage move gần:

```text
(1.1100 / 1.1000) - 1
≈ 0.91%
```

USD/JPY đi `100 pips` nghĩa là thay đổi `1.00` JPY, nhưng percentage move còn tùy starting level.

Do đó so volatility giữa pair chỉ bằng số pip có thể gây sai. Percentage return hoặc normalized volatility thường phù hợp hơn cho cross-asset/risk analysis.

## 18. Price return của pair và return của currency không hoàn toàn đối xứng

Nếu EUR/USD tăng 10%, USD/EUR không giảm đúng 10%.

Nếu:

```text
EUR/USD = 1.00 → 1.10
```

EUR/USD tăng 10%.

Inverse:

```text
USD/EUR = 1.00 → 1/1.10 ≈ 0.9091
```

USD/EUR giảm khoảng 9.09%.

Return đơn giản không đối xứng qua inversion. Log return có tính chất thuận tiện hơn:

```text
ln(A/B return) = -ln(B/A return)
```

Điều này quan trọng ở phần quantitative research sau này.

## 19. Gross P/L khác net P/L

Ví dụ strategy tạo gross profit:

```text
+500 USD
```

nhưng chịu:

```text
spread cost      -80
commission       -20
slippage         -35
overnight carry  -25
```

Net:

```text
500 - 80 - 20 - 35 - 25
= 340 USD
```

Một backtest bỏ cost đang mô hình hóa một thị trường không tồn tại.

## 20. Rollover / financing làm P/L thay đổi theo thời gian giữ lệnh

Leveraged FX position giữ qua rollover có thể phát sinh financing debit hoặc credit tùy product, currency-rate relationship và broker terms.

Không nên suy luận đơn giản:

```text
high-yield currency long
→ always receive positive swap
```

vì retail financing còn phụ thuộc:

- broker markup;
- benchmark/reference rate;
- day-count convention;
- holiday/weekend adjustment;
- product structure;
- long/short asymmetry.

Luôn đọc swap/financing specification thực tế.

## 21. XAU/USD không phải currency pair theo nghĩa giống EUR/USD

Retail platform thường đặt `XAU/USD` cạnh Forex pairs. XAU là code cho gold, nên:

```text
XAU/USD
= USD price per unit of gold defined by contract
```

Contract size có thể khác giữa broker/product. Không được áp dụng máy móc:

```text
1 standard FX lot = 100,000 base units
```

cho XAU/USD.

Cần kiểm tra contract size, tick size, margin, financing và price source riêng.

## 22. Từ lot đến risk: còn thiếu stop distance

Giả sử hai trader cùng trade `0.1 lot EUR/USD`.

Trader A stop 10 pips.

Trader B stop 100 pips.

Pip value giả sử 1 USD/pip:

```text
A initial price risk ≈ 10 USD
B initial price risk ≈ 100 USD
```

Cùng lot nhưng risk khác 10 lần.

Vì vậy:

```text
Lot Size ≠ Risk
```

Risk phải kết hợp:

```text
position size
× distance to invalidation
× pip value
+ gap/slippage risk
```

Đây là cầu nối sang chương leverage và position sizing.

## 23. Công thức sizing từ allowed loss

Nếu risk budget là `R_account` và stop distance `D_pips`:

```text
Required Pip Value
≈ R_account / D_pips
```

Sau đó suy ra base units:

```text
Base Units
≈ Required Pip Value / Pip Size
```

nếu P/L quote currency trùng account currency.

Ví dụ muốn risk khoảng 100 USD với stop 25 pips trên EUR/USD:

```text
Required Pip Value
= 100 / 25
= 4 USD/pip
```

Vì:

```text
1 EUR unit × 0.0001
= 0.0001 USD/pip
```

nên approximate size:

```text
4 / 0.0001
= 40,000 EUR
≈ 0.4 standard lot
```

Đây mới là logic đúng chiều:

```text
Allowed Loss
→ Stop / Invalidation Distance
→ Position Size
```

không phải:

```text
Broker offers 1:100 leverage
→ maximize lot size
```

## 24. Slippage phá vỡ assumption “stop = exact loss”

Nếu stop ở 25 pips, expected loss theo sizing có thể là 100 USD. Nhưng stop order không bảo đảm fill đúng trigger price trong mọi market condition.

News gap hoặc liquidity vacuum có thể tạo:

```text
planned stop = 25 pips
actual fill = 40 pips away
```

Actual loss khi đó lớn hơn modeled loss.

Vì vậy risk sizing phải có safety margin cho instrument/event regime phù hợp, và không được coi stop-loss là hard guarantee.

## 25. Portfolio exposure có thể ẩn sau nhiều pair

Giả sử:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

cả ba đều chứa directional component có thể tương đồng: **short USD** theo các đối trọng khác nhau.

Risk không nên tính đơn giản:

```text
3 trades × 1% risk = 3 independent risks
```

vì positions có thể cùng chịu USD factor shock.

Cần phân rã exposure theo currencies/factors.

## 26. Một cách ghi position rõ ràng hơn

Thay vì chỉ journal:

```text
Long EURUSD 0.5 lot
```

nên có:

```text
Pair: EUR/USD
Direction: Long
Base units: 50,000 EUR
Entry: 1.1200
Stop: 1.1150
Distance: 50 pips
Pip value: ~5 USD/pip if account USD
Planned price loss: ~250 USD before slippage/cost
Macro exposure: long EUR / short USD
Account currency: USD
```

Journal như vậy nối trade notation với actual economic exposure.

## 27. Những nhầm lẫn cần loại bỏ

### “1 lot = 100.000 USD”

Không chính xác. Standard lot phổ biến là `100,000 units of base currency`. Với EUR/USD đó là 100.000 EUR; với GBP/USD là 100.000 GBP.

### “1 pip luôn = 10 USD”

Sai. Phụ thuộc pair, trade size và account currency.

### “Notional = tiền tôi bỏ vào”

Sai khi leveraged. Margin/collateral có thể nhỏ hơn notional rất nhiều.

### “Stop 1% giá = risk 1% tài khoản”

Không đúng nếu chưa sizing position dựa trên account risk.

### “100 pips trên mọi pair có cùng economic risk”

Sai. Pip size, pip value, volatility và percentage move khác nhau.

## 28. Bài tự kiểm tra

### Case A

EUR/USD = `1.1000`, bạn long `20,000 EUR`, exit `1.1050`.

```text
Move = 50 pips
Pip value = 20,000 × 0.0001 = 2 USD
P/L ≈ 100 USD
```

### Case B

USD/JPY = `150.00`, trade size `100,000 USD`, move 30 pips.

```text
Pip value = 100,000 × 0.01 = 1,000 JPY
P/L = 30,000 JPY
```

Sau đó mới convert JPY sang account currency.

### Case C

Account USD, risk budget 200 USD, stop 40 pips trên EUR/USD.

```text
Required pip value = 200 / 40 = 5 USD/pip
Base units ≈ 5 / 0.0001 = 50,000 EUR
```

Approximate size = 0.5 standard lot theo convention 100.000 units.

## 29. Checklist trước khi sang leverage/margin

Bạn nên tự tính được:

- base và quote currency;
- bid/ask và spread;
- pip size;
- base units từ lot;
- notional;
- P/L theo quote currency;
- conversion sang account currency;
- cross rate bằng unit analysis;
- pip value;
- position size từ allowed loss và stop distance.

Nếu calculator là cách duy nhất bạn biết để có đáp án, nên luyện lại mechanics.

## Nối sang chương tiếp theo

Pip và lot cho biết **position thay đổi P/L bao nhiêu khi price move**. Nhưng chúng chưa trả lời vì sao account có thể kiểm soát notional lớn hơn vốn, khi nào margin call/stop-out xảy ra và mức leverage nào đang ẩn trong danh mục.

→ [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)

## Liên kết liên quan

- [01 — Market structure and instruments](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [Trading & Forex master map](../00_MASTER_TRADING_FOREX_RISK.md)
- [Glossary, formulas and research conventions](../../00_GLOSSARY_FORMULAS_AND_RESEARCH_CONVENTIONS.md)
