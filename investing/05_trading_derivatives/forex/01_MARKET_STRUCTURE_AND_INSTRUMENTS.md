# 01 — Cấu trúc thị trường Forex và các công cụ giao dịch

Forex thường được giới thiệu bằng một màn hình chart và nút Buy/Sell. Cách bắt đầu đó làm người học dễ hình thành mental model sai: tưởng rằng tồn tại một “sàn Forex toàn cầu” có một order book duy nhất, một mức giá duy nhất và tất cả trader đều giao dịch cùng một sản phẩm.

Thực tế, **foreign exchange market — thị trường ngoại hối (외환시장)** là một mạng lưới nhiều thị trường và nhiều loại hợp đồng liên kết với nhau. Spot FX, forward, FX swap, currency swap, futures, options và retail leveraged products có thể cùng tham chiếu một cặp tiền nhưng khác nhau về quyền pháp lý, settlement, counterparty, margin, financing và cách hình thành giá.

Mental model đầu tiên nên là:

```text
Currency exposure
→ instrument used to express/hedge that exposure
→ trading venue / dealer network
→ execution
→ settlement / collateral
→ resulting P/L and risk
```

## 1. Forex không phải là “mua một đồng tiền vì chart đẹp”

Một tỷ giá luôn là **giá tương đối**.

Nếu:

```text
EUR/USD = 1.1200
```

nghĩa là thị trường đang định giá xấp xỉ:

```text
1 EUR = 1.12 USD
```

Nếu EUR/USD tăng từ `1.1200` lên `1.1300`, có thể nói EUR đã tăng giá **so với USD**, hoặc USD đã giảm giá **so với EUR**. Không thể từ riêng chuyển động đó kết luận EUR “mạnh lên với mọi đồng tiền”. EUR có thể tăng so với USD nhưng đồng thời giảm so với CHF hoặc GBP.

Vì vậy Forex luôn là bài toán tương đối:

```text
Economy A / Currency A
versus
Economy B / Currency B
```

Đây là lý do phân tích FX cần so sánh chênh lệch lãi suất, kỳ vọng chính sách, tăng trưởng, lạm phát, dòng vốn và risk premium giữa hai phía thay vì chỉ phân tích một quốc gia.

## 2. Quy mô thị trường lớn không có nghĩa mọi phần của thị trường đều giống nhau

Theo 2025 Triennial Central Bank Survey của Bank for International Settlements (BIS), turnover FX toàn cầu trong tháng 4/2025 vào khoảng **9,6 nghìn tỷ USD mỗi ngày**. USD nằm ở một phía của phần lớn giao dịch, và FX swap tiếp tục chiếm phần rất lớn của turnover.

Điều quan trọng của con số này không phải để ghi nhớ `9.6 trillion`. Ý nghĩa sâu hơn là phần lớn hoạt động FX toàn cầu đến từ ngân hàng, tổ chức tài chính, doanh nghiệp, hedging, funding và institutional flow — không phải chỉ từ retail directional trading.

Một thị trường có turnover rất lớn vẫn có thể có những thời điểm hoặc instrument mà liquidity mỏng. Liquidity phải được xem theo:

```text
currency pair
× instrument
× tenor
× trading session
× market regime
× trade size
```

Không nên suy luận kiểu “Forex lớn nên lúc nào cũng thanh khoản tốt”.

## 3. OTC: Forex phần lớn không có một centralized exchange duy nhất

**Over-the-counter (OTC)** nghĩa là giao dịch được thỏa thuận trong mạng lưới dealer/client hoặc electronic venue thay vì tất cả lệnh phải đi qua một centralized exchange duy nhất.

Điều này tạo ra một cấu trúc phân mảnh:

```text
Interdealer venues
        ↕
Major banks / dealers
        ↕
Institutional clients
        ↕
Prime brokers / prime-of-prime
        ↕
Brokers / retail platforms
```

Sơ đồ chỉ là simplification. Một tổ chức có thể kết nối nhiều venue và nhiều liquidity provider cùng lúc.

Hệ quả quan trọng là **không tồn tại một universal order book chứa toàn bộ lệnh Forex trên thế giới**. Hai nguồn dữ liệu có thể hiển thị bid/ask hơi khác nhau vì chúng lấy liquidity từ các pool khác nhau, có latency khác nhau hoặc áp dụng markup khác nhau.

Do đó khi nhìn chart retail, cần hiểu chart đó là một **representation của feed cụ thể**, không phải bản ghi tuyệt đối của mọi transaction toàn cầu.

## 4. Interdealer market và dealer-client market

### Interdealer

Các dealer lớn giao dịch với nhau để:

- quản lý inventory;
- hedge exposure từ khách hàng;
- tạo giá;
- transfer risk;
- điều chỉnh funding và liquidity.

### Dealer-client

Client có thể là:

- asset manager;
- hedge fund;
- pension fund;
- insurer;
- corporation;
- sovereign institution;
- smaller financial institution;
- retail customer thông qua broker/dealer.

Một corporation có thể mua USD forward để khóa tỷ giá cho khoản phải trả trong tương lai. Một asset manager có thể hedge currency exposure của danh mục trái phiếu nước ngoài. Một macro fund có thể chủ động nhận directional exposure. Cả ba đều tạo FX transaction nhưng **mục đích kinh tế khác nhau**.

Flow vì vậy không đồng nghĩa với “view”. Một lệnh mua USD lớn có thể là hedging bắt buộc chứ không phải trader tin USD sẽ tăng.

## 5. Spot FX là gì?

**Spot foreign exchange** là giao dịch trao đổi hai đồng tiền theo tỷ giá hiện tại với settlement theo convention của cặp tiền.

Ví dụ đơn giản, một tổ chức thỏa thuận:

```text
Buy EUR
Sell USD
at EUR/USD = X
```

Sau transaction, hai phía có nghĩa vụ trao đổi principal theo settlement convention tương ứng.

Trong institutional spot, settlement thực sự của hai đồng tiền là phần cốt lõi của transaction. Nhưng trong nhiều retail leveraged FX products, trader không nhận hàng triệu EUR vào bank account. Broker platform thường tạo một leveraged cash-settled hoặc rolling exposure theo contractual terms riêng.

Vì vậy phải phân biệt:

```text
institutional deliverable spot FX
≠
retail leveraged rolling FX product
```

Tên hiển thị trên platform có thể giống nhau nhưng legal/economic mechanics không hoàn toàn giống nhau.

## 6. Forward: khóa tỷ giá cho tương lai

**FX forward — hợp đồng kỳ hạn ngoại hối** là thỏa thuận hôm nay về việc trao đổi tiền tại một ngày tương lai với tỷ giá forward đã xác định.

Forward rate không đơn giản là “dự báo của thị trường về spot tương lai”. Trong điều kiện arbitrage lý tưởng, forward price liên hệ chặt với:

```text
spot rate
+ interest-rate differential
+ funding / basis effects
```

Trực giác first principles:

Nếu giữ USD và EUR tạo ra mức return khác nhau, mức chênh lệch đó phải được phản ánh vào forward pricing; nếu không, một arbitrageur có thể vay một currency, đổi sang currency kia, đầu tư và khóa tỷ giá quay lại để tạo lợi nhuận gần như không rủi ro.

Thực tế còn có transaction cost, balance-sheet constraint, cross-currency basis và credit/collateral terms, nên textbook covered interest parity không phải lúc nào cũng khớp hoàn hảo.

## 7. FX swap: trao đổi spot và đảo ngược ở tương lai

**FX swap** thường kết hợp hai legs:

```text
Near leg: exchange currencies now/near date
Far leg: reverse the exchange later
```

Ví dụ một ngân hàng cần USD trong ba tháng nhưng đang có EUR. Thay vì tạo directional bet, ngân hàng có thể dùng FX swap để chuyển funding currency tạm thời.

Điều này giải thích vì sao turnover FX swap rất lớn: FX market không chỉ tồn tại để đầu cơ tỷ giá, mà còn là hạ tầng funding và hedging của hệ thống tài chính toàn cầu.

Đừng nhầm FX swap với **currency swap** dài hạn.

## 8. Currency swap

**Cross-currency swap / currency swap** thường là hợp đồng dài hạn hơn, có thể trao đổi principal và các dòng interest payment bằng hai currency khác nhau.

Một doanh nghiệp có thể phát hành debt ở currency A nhưng muốn economic exposure giống như debt bằng currency B. Cross-currency swap có thể chuyển đổi profile đó.

Cần đọc một currency swap qua:

```text
notional principals
interest legs
fixed / floating structure
maturity
reset convention
collateral
counterparty risk
basis
```

Đây là instrument tài trợ/phòng vệ phức tạp hơn retail spot trading rất nhiều.

## 9. FX futures

**Currency futures** là hợp đồng chuẩn hóa giao dịch trên exchange.

Khác biệt mental model quan trọng:

```text
OTC spot/forward
→ bilateral / dealer network

Futures
→ standardized contract
→ exchange
→ central clearing
→ daily margining
```

Ví dụ futures có:

- contract multiplier;
- tick size;
- expiry;
- initial/maintenance margin;
- mark-to-market;
- exchange trading hours.

Futures mang lại centralized order book và transparency cao hơn về traded volume/order book trong venue đó, nhưng không có nghĩa futures order book đại diện toàn bộ global FX market.

## 10. FX options

**FX option** cho holder quyền, nhưng không phải nghĩa vụ, mua hoặc bán currency theo strike và điều khoản xác định.

P/L không còn tuyến tính đơn giản như spot:

```text
Spot / Forward:
P/L chủ yếu thay đổi gần tuyến tính theo tỷ giá

Option:
P/L phụ thuộc price
+ implied volatility
+ time
+ rates
+ convexity
```

Vì vậy một trader đúng hướng về EUR/USD nhưng vẫn có thể mất tiền với option nếu trả implied volatility quá cao hoặc timing sai.

Phần option chuyên sâu nằm ở `../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md`; Forex learning path chỉ dùng option khi cần nối FX với volatility/hedging.

## 11. CFD và các retail derivative tương tự

**Contract for Difference (CFD)** là hợp đồng với provider để thanh toán chênh lệch giá của underlying reference. CFD không làm trader sở hữu underlying asset.

Tùy jurisdiction và broker, một symbol như `EURUSD` hay `XAUUSD` trên platform có thể là CFD hoặc một retail OTC leveraged product với terms riêng.

Không được suy luận từ ticker rằng instrument giống institutional spot.

Trước khi giao dịch, phải đọc contract specification:

```text
legal entity
contract size
minimum size
margin rule
financing / rollover
spread / commission
price source
execution policy
stop-out rule
negative-balance treatment if any
corporate / market-event handling
withdrawal and dispute process
```

## 12. Liquidity provider là ai?

**Liquidity provider (LP)** cung cấp executable prices cho client/venue/broker tùy mô hình.

LP có thể là bank, non-bank market maker hoặc institution khác. Một broker có thể aggregate quotes từ nhiều LP rồi xây best bid/offer riêng cho client.

Điều này tạo ra distinction:

```text
raw market spread
+ broker markup
+ commission
+ slippage / market impact
= effective execution cost
```

“Zero commission” không đồng nghĩa “zero cost”. Cost có thể nằm trong spread hoặc financing.

## 13. Bid, ask và spread tồn tại vì sao?

Market maker sẵn sàng:

```text
buy at Bid
sell at Ask
```

và:

```text
Ask > Bid
```

Spread bù đắp một phần cho:

- inventory risk;
- adverse selection;
- market volatility;
- funding/capital cost;
- operational cost;
- profit margin.

Khi uncertainty tăng mạnh, market maker có thể widen spread vì rủi ro bị giao dịch bởi counterparty có information advantage tăng hoặc vì hedge trở nên đắt hơn.

Đây là lý do spread thường xấu đi quanh news event, market stress hoặc thời điểm liquidity thấp.

## 14. Price discovery không nằm ở một điểm duy nhất

Price discovery trong FX diễn ra qua tương tác giữa:

- interdealer venues;
- dealer-to-client platforms;
- electronic communication networks;
- futures markets;
- voice trading ở một số segment;
- internalization của dealer;
- algorithmic market making.

Arbitrage và competition giữ các price pool tương đối gần nhau, nhưng không loại bỏ hoàn toàn micro-difference.

Nếu broker A hiển thị EUR/USD `1.12001/1.12005` và broker B hiển thị `1.12002/1.12007`, điều đó không tự động có nghĩa một bên “sai giá”. Cần xét timestamp, liquidity source, markup và executable size.

## 15. Trading session: thị trường gần như 24 giờ nhưng liquidity không đồng nhất

FX vận hành xuyên các trung tâm tài chính lớn. Retail trader thường dùng các nhãn:

```text
Asia session
London / European session
New York session
```

Các session overlap làm participant set và liquidity thay đổi.

Điều quan trọng không phải nhớ một khung giờ cố định từ infographic, vì daylight-saving time có thể làm local clock thay đổi. Hãy hiểu cơ chế:

```text
major financial centres open
→ more active participants
→ more quoting and hedging
→ liquidity / volatility profile changes
```

Một strategy backtest theo giờ phải xử lý timezone và daylight-saving đúng, nếu không statistical result có thể lệch.

## 16. Settlement risk: trade đúng chưa có nghĩa tiền đã settle

Trong deliverable FX, hai currencies phải được trao đổi. Nếu một bên gửi currency của mình nhưng counterparty phá sản trước khi gửi currency còn lại, phát sinh **principal risk / settlement risk**.

Đây từng được gọi phổ biến là Herstatt risk sau một sự kiện lịch sử nổi tiếng trong banking.

Hệ thống payment-versus-payment như CLS được thiết kế để giảm principal settlement risk cho các currency đủ điều kiện bằng cách liên kết hai payment legs thay vì để một bên thanh toán trước mà không chắc nhận leg còn lại.

Retail platform user thường không trực tiếp vận hành settlement infrastructure này, nhưng hiểu settlement giúp thấy FX là financial plumbing thật sự, không chỉ là chart.

## 17. Counterparty risk thay đổi theo instrument

### OTC bilateral

Bạn phụ thuộc vào counterparty và contractual/legal framework.

### Centrally cleared futures

Central counterparty và margin system thay đổi cách counterparty risk được quản lý, nhưng không làm risk biến mất. Vẫn tồn tại liquidity, gap, margin, operational và clearing-member risk.

### Retail broker/dealer

Ngoài market risk còn phải xét:

```text
broker legal entity
regulatory status
segregation / custody terms
execution model
withdrawal process
platform reliability
cyber / operational risk
```

CFTC đặc biệt cảnh báo rằng retail OTC customer cần hiểu mình có thể đang giao dịch trực tiếp với dealer thay vì trên open centralized exchange.

## 18. Tại sao giá giữa spot, forward và futures liên hệ với nhau?

Nếu các instrument cùng biểu diễn exposure đến một currency pair nhưng pricing lệch quá xa sau khi tính:

- funding;
- interest differential;
- maturity;
- transaction cost;
- collateral;
- balance-sheet cost;

arbitrageur có động lực mua instrument rẻ và bán instrument đắt.

Arbitrage không làm mọi giá giống hệt nhau. Nó tạo **no-arbitrage relationships** có điều chỉnh theo carrying/funding mechanics.

Đây là nền tảng để hiểu later topics như:

- forward points;
- covered interest parity;
- cross-currency basis;
- futures basis;
- carry trade.

## 19. Một ví dụ nối toàn bộ market structure

Giả sử một công ty Hàn Quốc sẽ phải trả `10 million USD` cho supplier sau ba tháng.

Nếu công ty không hedge:

```text
KRW weakens against USD
→ cần nhiều KRW hơn để mua 10m USD
→ cost bằng KRW tăng
```

Công ty có thể dùng FX forward để khóa gần trước tỷ giá tương lai.

Dealer cung cấp forward price dựa trên:

```text
spot USD/KRW
+ KRW/USD funding relationship
+ forward points / basis
+ balance-sheet and credit terms
+ dealer spread
```

Dealer sau đó có thể hedge exposure qua spot, forward, swap hoặc các dealer khác.

Một transaction corporate hedge cuối cùng có thể tạo flow ở nhiều layer. Vì vậy thấy USD/KRW được mua không đủ để kết luận “mọi participant bullish USD”.

Thuật ngữ Hàn Quốc hữu ích:

- ngoại hối: **외환**;
- tỷ giá: **환율**;
- phòng vệ rủi ro tỷ giá: **환헤지 / 환위험 헤지**;
- hợp đồng kỳ hạn: **선도계약**;
- hợp đồng tương lai: **선물계약**.

## 20. Sai lầm mental model phổ biến

### “Forex có một giá chính xác duy nhất”

Sai ở microstructure level. Có reference market price, nhưng executable quote phụ thuộc venue, timestamp, size và counterparty.

### “Spot FX = retail EURUSD trên mọi broker”

Không nhất thiết. Phải đọc legal product terms.

### “Volume trên chart retail = global Forex volume”

Thường không đúng. Tick volume hoặc broker-specific volume chỉ phản ánh data source đó.

### “Mọi FX trade là speculation”

Sai. Hedging, funding, liquidity management và corporate payment tạo lượng flow rất lớn.

### “OTC nghĩa là không có regulation”

Sai. OTC mô tả market structure, không tự động nói một transaction có hoặc không được regulated. Regulatory treatment phụ thuộc jurisdiction, participant và product.

### “Centralized exchange = không còn counterparty risk”

Sai. Clearing tái cấu trúc và quản lý counterparty risk bằng collateral/margin/default waterfall, không xóa mọi risk.

## 21. Checklist trước khi học sang pip/lot

Bạn nên tự giải thích được:

1. Vì sao EUR/USD là relative price thay vì giá tuyệt đối của EUR.
2. OTC khác centralized exchange như thế nào.
3. Spot, forward, FX swap và currency futures khác nhau ở đâu.
4. Vì sao FX swap có thể rất lớn dù người dùng cuối không đầu cơ tỷ giá.
5. Vì sao broker feed khác nhau một vài pipette không nhất thiết là lỗi.
6. Vì sao spread thay đổi theo liquidity và volatility.
7. Vì sao settlement/counterparty risk tồn tại ngoài price risk.
8. Vì sao retail symbol cần đọc contract specification trước khi coi nó là một instrument cụ thể.

Nếu các câu này chưa rõ, quay lại market structure trước khi học strategy.

## Nối sang chương tiếp theo

Market structure trả lời **“mình đang giao dịch cái gì và với ai?”**. Chương tiếp theo trả lời **“giá đó được đọc và biến thành P/L như thế nào?”**:

→ [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)

## Nguồn nền

- BIS — 2025 Triennial Central Bank Survey: https://www.bis.org/publications/triennial-central-bank-survey-foreign-exchange-and-over-the-counter-otc-derivatives-markets-2025
- BIS — Global FX trading turnover / 2025 survey release: https://www.bis.org/media-releases/20250930-global-fx-trading-hits-96-trillion-day-april-2025-and-otc-interest-rate-derivatives-surge-79
- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- Trading & Derivatives master map: [../00_MASTER_TRADING_FOREX_RISK.md](../00_MASTER_TRADING_FOREX_RISK.md)
