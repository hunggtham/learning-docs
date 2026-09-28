# 01 — Cấu trúc thị trường Forex và các công cụ giao dịch

> **Mạch đọc:** Đặt **01 — Cấu trúc thị trường Forex và các công cụ giao dịch** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Forex không phải là “mua một đồng tiền vì chart đẹp”** sang **2. Quy mô thị trường lớn không có nghĩa mọi phần của thị trường đều giống nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Forex thường được giới thiệu bằng một màn hình chart và nút Buy/Sell. Cách bắt đầu đó làm người học dễ hình thành mô hình tư duy (mental model / 사고 모델) sai: tưởng rằng tồn tại một “sàn Forex toàn cầu” có một thứ tự (order / 순서) book duy nhất, một mức giá duy nhất và tất cả trader đều giao dịch cùng một sản phẩm.

Thực tế, **foreign exchange thị trường (market / 시장) — thị trường ngoại hối (외환시장)** là một mạng lưới nhiều thị trường và nhiều loại hợp đồng liên kết với nhau. Spot FX, forward, FX swap, currency swap, futures, options và retail leveraged products có thể cùng tham chiếu một cặp tiền nhưng khác nhau về quyền pháp lý, settlement, counterparty, margin, financing và cách hình thành giá.

Mô hình tư duy (mental model / 사고 모델) đầu tiên nên là:

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

Đây là lý do phân tích FX cần so sánh chênh lệch lãi suất, kỳ vọng chính sách, tăng trưởng, lạm phát, dòng vốn và rủi ro (risk / 위험) premium giữa hai phía thay vì chỉ phân tích một quốc gia.

## 2. Quy mô thị trường lớn không có nghĩa mọi phần của thị trường đều giống nhau

Theo 2025 Triennial Central Bank Survey của Bank for International Settlements (BIS), turnover FX toàn cầu trong tháng 4/2025 vào khoảng **9,6 nghìn tỷ USD mỗi ngày**. USD nằm ở một phía của phần lớn giao dịch, và FX swap tiếp tục chiếm phần rất lớn của turnover.

Điều quan trọng của con số này không phải để ghi nhớ `9.6 trillion`. Ý nghĩa sâu hơn là phần lớn hoạt động FX toàn cầu đến từ ngân hàng, tổ chức tài chính, doanh nghiệp, hedging, funding và institutional luồng (flow / 흐름) — không phải chỉ từ retail directional trading.

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

**Over-the-counter (OTC)** nghĩa là giao dịch được thỏa thuận trong mạng lưới dealer/máy khách (client / 클라이언트) hoặc electronic venue thay vì tất cả lệnh phải đi qua một centralized exchange duy nhất.

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

Hệ quả quan trọng là **không tồn tại một universal thứ tự (order / 순서) book chứa toàn bộ lệnh Forex trên thế giới**. Hai nguồn dữ liệu có thể hiển thị bid/ask hơi khác nhau vì chúng lấy liquidity từ các pool khác nhau, có độ trễ (latency / 지연 시간) khác nhau hoặc áp dụng markup khác nhau.

Do đó khi nhìn chart retail, cần hiểu chart đó là một **biểu diễn (representation / 표현) của feed cụ thể**, không phải bản ghi tuyệt đối của mọi giao dịch (transaction / 트랜잭션) toàn cầu.

## 4. Interdealer thị trường (market / 시장) và dealer-client thị trường (market / 시장)

### Interdealer

Các dealer lớn giao dịch với nhau để:

- quản lý inventory;
- hedge exposure từ khách hàng;
- tạo giá;
- transfer rủi ro (risk / 위험);
- điều chỉnh funding và liquidity.

### Dealer-client

Máy khách (client / 클라이언트) có thể là:

- asset manager;
- hedge fund;
- pension fund;
- insurer;
- corporation;
- sovereign institution;
- smaller financial institution;
- retail customer thông qua broker/dealer.

Một corporation có thể mua USD forward để khóa tỷ giá cho khoản phải trả trong tương lai. Một asset manager có thể hedge currency exposure của danh mục trái phiếu nước ngoài. Một macro fund có thể chủ động nhận directional exposure. Cả ba đều tạo FX giao dịch (transaction / 트랜잭션) nhưng **mục đích kinh tế khác nhau**.

Luồng (flow / 흐름) vì vậy không đồng nghĩa với “view”. Một lệnh mua USD lớn có thể là hedging bắt buộc chứ không phải trader tin USD sẽ tăng.

## 5. Spot FX là gì?

**Spot foreign exchange** là giao dịch trao đổi hai đồng tiền theo tỷ giá hiện tại với settlement theo convention của cặp tiền.

Ví dụ đơn giản, một tổ chức thỏa thuận:

```text
Buy EUR
Sell USD
at EUR/USD = X
```

Sau giao dịch (transaction / 트랜잭션), hai phía có nghĩa vụ trao đổi principal theo settlement convention tương ứng.

Trong institutional spot, settlement thực sự của hai đồng tiền là phần cốt lõi của giao dịch (transaction / 트랜잭션). Nhưng trong nhiều retail leveraged FX products, trader không nhận hàng triệu EUR vào bank account. Broker nền tảng (platform / 플랫폼) thường tạo một leveraged cash-settled hoặc rolling exposure theo contractual terms riêng.

Vì vậy phải phân biệt:

```text
institutional deliverable spot FX
≠
retail leveraged rolling FX product
```

Tên hiển thị trên nền tảng (platform / 플랫폼) có thể giống nhau nhưng legal/economic mechanics không hoàn toàn giống nhau.

## 6. Forward: khóa tỷ giá cho tương lai

**FX forward — hợp đồng kỳ hạn ngoại hối** là thỏa thuận hôm nay về việc trao đổi tiền tại một ngày tương lai với tỷ giá forward đã xác định.

Forward tỷ lệ (rate / 비율) không đơn giản là “dự báo của thị trường về spot tương lai”. Trong điều kiện arbitrage lý tưởng, forward price liên hệ chặt với:

```text
spot rate
+ interest-rate differential
+ funding / basis effects
```

Trực giác nguyên lý nền tảng (first principles / 제일 원리):

Nếu giữ USD và EUR tạo ra mức return khác nhau, mức chênh lệch đó phải được phản ánh vào forward pricing; nếu không, một arbitrageur có thể vay một currency, đổi sang currency kia, đầu tư và khóa tỷ giá quay lại để tạo lợi nhuận gần như không rủi ro.

Thực tế còn có giao dịch (transaction / 트랜잭션) chi phí (cost / 비용), balance-sheet ràng buộc (constraint / 제약조건), cross-currency basis và credit/collateral terms, nên textbook covered interest parity không phải lúc nào cũng khớp hoàn hảo.

## 7. FX swap: trao đổi spot và đảo ngược ở tương lai

**FX swap** thường kết hợp hai legs:

```text
Near leg: exchange currencies now/near date
Far leg: reverse the exchange later
```

Ví dụ một ngân hàng cần USD trong ba tháng nhưng đang có EUR. Thay vì tạo directional bet, ngân hàng có thể dùng FX swap để chuyển funding currency tạm thời.

Điều này giải thích vì sao turnover FX swap rất lớn: FX thị trường (market / 시장) không chỉ tồn tại để đầu cơ tỷ giá, mà còn là hạ tầng funding và hedging của hệ thống tài chính toàn cầu.

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

Khác biệt mô hình tư duy (mental model / 사고 모델) quan trọng:

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

- đặc tả hợp đồng (contract / 계약) multiplier;
- tick kích thước (size / 크기);
- expiry;
- initial/maintenance margin;
- mark-to-market;
- exchange trading hours.

Futures mang lại centralized thứ tự (order / 순서) book và transparency cao hơn về traded volume/thứ tự (order / 순서) book trong venue đó, nhưng không có nghĩa futures thứ tự (order / 순서) book đại diện toàn bộ toàn cục (global / 전역) FX thị trường (market / 시장).

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

Phần option chuyên sâu nằm ở `../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md`; Forex lộ trình học (learning path / 학습 경로) chỉ dùng option khi cần nối FX với volatility/hedging.

## 11. CFD và các retail derivative tương tự

**đặc tả hợp đồng (contract / 계약) for Difference (CFD)** là hợp đồng với provider để thanh toán chênh lệch giá của underlying tham chiếu (reference / 참조). CFD không làm trader sở hữu underlying asset.

Tùy jurisdiction và broker, một symbol như `EURUSD` hay `XAUUSD` trên nền tảng (platform / 플랫폼) có thể là CFD hoặc một retail OTC leveraged sản phẩm (product / 제품) với terms riêng.

Không được suy luận từ ticker rằng instrument giống institutional spot.

Trước khi giao dịch, phải đọc đặc tả hợp đồng (contract / 계약) specification:

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

**Liquidity provider (LP)** cung cấp executable prices cho máy khách (client / 클라이언트)/venue/broker tùy mô hình.

LP có thể là bank, non-bank thị trường (market / 시장) maker hoặc institution khác. Một broker có thể aggregate quotes từ nhiều LP rồi xây best bid/offer riêng cho máy khách (client / 클라이언트).

Điều này tạo ra distinction:

```text
raw market spread
+ broker markup
+ commission
+ slippage / market impact
= effective execution cost
```

“Zero commission” không đồng nghĩa “zero chi phí (cost / 비용)”. chi phí (cost / 비용) có thể nằm trong spread hoặc financing.

## 13. Bid, ask và spread tồn tại vì sao?

Thị trường (market / 시장) maker sẵn sàng:

```text
buy at Bid
sell at Ask
```

và:

```text
Ask > Bid
```

Spread bù đắp một phần cho:

- inventory rủi ro (risk / 위험);
- adverse selection;
- thị trường (market / 시장) volatility;
- funding/capital chi phí (cost / 비용);
- operational chi phí (cost / 비용);
- profit margin.

Khi bất định (uncertainty / 불확실성) tăng mạnh, thị trường (market / 시장) maker có thể widen spread vì rủi ro bị giao dịch bởi counterparty có thông tin (information / 정보) advantage tăng hoặc vì hedge trở nên đắt hơn.

Đây là lý do spread thường xấu đi quanh news sự kiện (event / 이벤트), thị trường (market / 시장) stress hoặc thời điểm liquidity thấp.

## 14. Price discovery không nằm ở một điểm duy nhất

Price discovery trong FX diễn ra qua tương tác giữa:

- interdealer venues;
- dealer-to-client platforms;
- electronic communication networks;
- futures markets;
- voice trading ở một số segment;
- internalization của dealer;
- algorithmic thị trường (market / 시장) making.

Arbitrage và competition giữ các price pool tương đối gần nhau, nhưng không loại bỏ hoàn toàn micro-difference.

Nếu broker A hiển thị EUR/USD `1.12001/1.12005` và broker B hiển thị `1.12002/1.12007`, điều đó không tự động có nghĩa một bên “sai giá”. Cần xét timestamp, liquidity nguồn (source / 소스), markup và executable kích thước (size / 크기).

## 15. Trading session: thị trường gần như 24 giờ nhưng liquidity không đồng nhất

FX vận hành xuyên các trung tâm tài chính lớn. Retail trader thường dùng các nhãn:

```text
Asia session
London / European session
New York session
```

Các session overlap làm participant set và liquidity thay đổi.

Điều quan trọng không phải nhớ một khung giờ cố định từ infographic, vì daylight-saving thời gian (time / 시간) có thể làm cục bộ (local / 로컬) clock thay đổi. Hãy hiểu cơ chế:

```text
major financial centres open
→ more active participants
→ more quoting and hedging
→ liquidity / volatility profile changes
```

Một chiến lược (strategy / 전략) backtest theo giờ phải xử lý timezone và daylight-saving đúng, nếu không statistical kết quả (result / 결과) có thể lệch.

## 16. Settlement rủi ro (risk / 위험): trade đúng chưa có nghĩa tiền đã settle

Trong deliverable FX, hai currencies phải được trao đổi. Nếu một bên gửi currency của mình nhưng counterparty phá sản trước khi gửi currency còn lại, phát sinh **principal rủi ro (risk / 위험) / settlement rủi ro (risk / 위험)**.

Đây từng được gọi phổ biến là Herstatt rủi ro (risk / 위험) sau một sự kiện lịch sử nổi tiếng trong banking.

Hệ thống payment-versus-payment như CLS được thiết kế để giảm principal settlement rủi ro (risk / 위험) cho các currency đủ điều kiện bằng cách liên kết hai payment legs thay vì để một bên thanh toán trước mà không chắc nhận leg còn lại.

Retail nền tảng (platform / 플랫폼) người dùng (user / 사용자) thường không trực tiếp vận hành settlement hạ tầng (infrastructure / 인프라) này, nhưng hiểu settlement giúp thấy FX là financial plumbing thật sự, không chỉ là chart.

## 17. Counterparty rủi ro (risk / 위험) thay đổi theo instrument

### OTC bilateral

Bạn phụ thuộc vào counterparty và contractual/legal khung phần mềm (framework / 프레임워크).

### Centrally cleared futures

Central counterparty và margin hệ thống (system / 시스템) thay đổi cách counterparty rủi ro (risk / 위험) được quản lý, nhưng không làm rủi ro (risk / 위험) biến mất. Vẫn tồn tại liquidity, gap, margin, operational và clearing-member rủi ro (risk / 위험).

### Retail broker/dealer

Ngoài thị trường (market / 시장) rủi ro (risk / 위험) còn phải xét:

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
- giao dịch (transaction / 트랜잭션) chi phí (cost / 비용);
- collateral;
- balance-sheet chi phí (cost / 비용);

arbitrageur có động lực mua instrument rẻ và bán instrument đắt.

Arbitrage không làm mọi giá giống hệt nhau. Nó tạo **no-arbitrage relationships** có điều chỉnh theo carrying/funding mechanics.

Đây là nền tảng để hiểu later topics như:

- forward points;
- covered interest parity;
- cross-currency basis;
- futures basis;
- carry trade.

## 19. Một ví dụ nối toàn bộ thị trường (market / 시장) cấu trúc (structure / 구조)

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

Một giao dịch (transaction / 트랜잭션) corporate hedge cuối cùng có thể tạo luồng (flow / 흐름) ở nhiều tầng (layer / 계층). Vì vậy thấy USD/KRW được mua không đủ để kết luận “mọi participant bullish USD”.

Thuật ngữ Hàn Quốc hữu ích:

- ngoại hối: **외환**;
- tỷ giá: **환율**;
- phòng vệ rủi ro tỷ giá: **환헤지 / 환위험 헤지**;
- hợp đồng kỳ hạn: **선도계약**;
- hợp đồng tương lai: **선물계약**.

## 20. Sai lầm mô hình tư duy (mental model / 사고 모델) phổ biến

### “Forex có một giá chính xác duy nhất”

Sai ở microstructure mức (level / 수준). Có tham chiếu (reference / 참조) thị trường (market / 시장) price, nhưng executable quote phụ thuộc venue, timestamp, kích thước (size / 크기) và counterparty.

### “Spot FX = retail EURUSD trên mọi broker”

Không nhất thiết. Phải đọc legal sản phẩm (product / 제품) terms.

### “Volume trên chart retail = toàn cục (global / 전역) Forex volume”

Thường không đúng. Tick volume hoặc broker-specific volume chỉ phản ánh dữ liệu (data / 데이터) nguồn (source / 소스) đó.

### “Mọi FX trade là speculation”

Sai. Hedging, funding, liquidity management và corporate payment tạo lượng luồng (flow / 흐름) rất lớn.

### “OTC nghĩa là không có regulation”

Sai. OTC mô tả thị trường (market / 시장) cấu trúc (structure / 구조), không tự động nói một giao dịch (transaction / 트랜잭션) có hoặc không được regulated. Regulatory treatment phụ thuộc jurisdiction, participant và sản phẩm (product / 제품).

### “Centralized exchange = không còn counterparty rủi ro (risk / 위험)”

Sai. Clearing tái cấu trúc và quản lý counterparty rủi ro (risk / 위험) bằng collateral/margin/default waterfall, không xóa mọi rủi ro (risk / 위험).

## 21. Checklist trước khi học sang pip/lot

Bạn nên tự giải thích được:

1. Vì sao EUR/USD là relative price thay vì giá tuyệt đối của EUR.
2. OTC khác centralized exchange như thế nào.
3. Spot, forward, FX swap và currency futures khác nhau ở đâu.
4. Vì sao FX swap có thể rất lớn dù người dùng cuối không đầu cơ tỷ giá.
5. Vì sao broker feed khác nhau một vài pipette không nhất thiết là lỗi.
6. Vì sao spread thay đổi theo liquidity và volatility.
7. Vì sao settlement/counterparty rủi ro (risk / 위험) tồn tại ngoài price rủi ro (risk / 위험).
8. Vì sao retail symbol cần đọc đặc tả hợp đồng (contract / 계약) specification trước khi coi nó là một instrument cụ thể.

Nếu các câu này chưa rõ, quay lại thị trường (market / 시장) cấu trúc (structure / 구조) trước khi học chiến lược (strategy / 전략).

## Nối sang chương tiếp theo

Thị trường (market / 시장) cấu trúc (structure / 구조) trả lời **“mình đang giao dịch cái gì và với ai?”**. Chương tiếp theo trả lời **“giá đó được đọc và biến thành P/L như thế nào?”**:

→ [02 — Quotes, pips, lots and P/L](./02_QUOTES_PIPS_LOTS_AND_PNL.md)

Để theo trade qua matching, SSI, netting, funding cut-off, PvP hoặc gross bilateral settlement, đọc [FX settlement, PvP, netting and liquidity](./90_connections/03_FX_SETTLEMENT_PVP_NETTING_AND_LIQUIDITY.md).

## Nguồn nền

- BIS — 2025 Triennial Central Bank Survey: https://www.bis.org/publications/triennial-central-bank-survey-foreign-exchange-and-over-the-counter-otc-derivatives-markets-2025
- BIS — toàn cục (global / 전역) FX trading turnover / 2025 survey bản phát hành (release / 릴리스): https://www.bis.org/media-releases/20250930-global-fx-trading-hits-96-trillion-day-april-2025-and-otc-interest-rate-derivatives-surge-79
- CFTC — Eight Things You Should Know Before Trading Forex: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- Trading & Derivatives master map: [../00_MASTER_TRADING_FOREX_RISK.md](../00_MASTER_TRADING_FOREX_RISK.md)

> **Bàn giao:** Sau **Nguồn nền**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [02 QUOTES PIPS LOTS AND PNL](./02_QUOTES_PIPS_LOTS_AND_PNL.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
