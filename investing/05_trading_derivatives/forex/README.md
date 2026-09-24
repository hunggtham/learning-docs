# Forex — Foreign Exchange Learning Path

Forex (foreign exchange, **thị trường ngoại hối**, tiếng Hàn: **외환**) là một nhánh con của `05_trading_derivatives/`. Phần này không được tổ chức như một bộ mẹo giao dịch hay danh sách indicator. Mục tiêu là xây một mental model hoàn chỉnh từ **thị trường ngoại hối thực sự vận hành như thế nào → một cặp tiền biểu diễn điều gì → P/L hình thành ra sao → leverage/margin biến đổi rủi ro thế nào → vì sao tỷ giá di chuyển → lệnh được thực thi qua ai → làm thế nào nghiên cứu một chiến lược mà không tự lừa mình**.

Forex cần được học như giao điểm của nhiều lớp kiến thức:

```text
Macroeconomics
+ Interest Rates
+ Cross-border Capital Flows
+ Market Microstructure
+ Derivatives
+ Leverage / Margin
+ Risk Management
+ Execution
+ Statistical Research
```

Nếu chỉ biết đọc chart nhưng không hiểu các lớp này, người học có thể mô tả chuyển động giá nhưng khó giải thích vì sao exposure thực sự tồn tại, vì sao cùng một setup cho kết quả khác nhau giữa các regime, hoặc vì sao một chiến lược có vẻ tốt trên chart nhưng thất bại sau spread, financing và slippage.

## Vị trí trong Investing library

```text
investing/
└── 05_trading_derivatives/
    ├── 00_MASTER_TRADING_FOREX_RISK.md
    ├── ...
    └── forex/
        ├── README.md
        ├── 01_MARKET_STRUCTURE_AND_INSTRUMENTS.md
        ├── 02_QUOTES_PIPS_LOTS_AND_PNL.md
        ├── 03_LEVERAGE_MARGIN_POSITION_SIZING.md
        ├── 04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md
        └── 05_EXECUTION_BROKERS_COSTS_AND_RISK.md
```

File `00_MASTER_TRADING_FOREX_RISK.md` ở thư mục cha vẫn là bản đồ tổng quan của Trading & Derivatives. Folder này đi sâu riêng vào Forex để tránh làm file master phình to và tránh trộn mechanics của FX với options, futures hay systematic trading.

## Thứ tự học

### 01 — Market structure and instruments

[01_MARKET_STRUCTURE_AND_INSTRUMENTS.md](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)

Bắt đầu từ câu hỏi tưởng đơn giản nhưng rất quan trọng: **“Forex market” thực sự là thị trường nào?** Chương này phân biệt spot FX, retail rolling spot/OTC product, forward, FX swap, currency swap, futures và options; giải thích OTC, interdealer market, dealer-client market, liquidity provider, prime brokerage, settlement, CLS và vì sao giá Forex không đến từ một order book toàn cầu duy nhất.

### 02 — Quotes, pips, lots and P/L

[02_QUOTES_PIPS_LOTS_AND_PNL.md](./02_QUOTES_PIPS_LOTS_AND_PNL.md)

Học cách đọc một currency pair từ first principles: base currency, quote currency, direct/indirect quote, bid/ask, spread, pip, pipette, contract size, lot, notional, cross rate và conversion giữa account currency với quote currency. Trọng tâm là tự tính được P/L thay vì phụ thuộc calculator của broker.

### 03 — Leverage, margin and position sizing

[03_LEVERAGE_MARGIN_POSITION_SIZING.md](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)

Đi sâu vào leverage (đòn bẩy, **레버리지**), margin (ký quỹ, **증거금**), equity, used/free margin, margin level, liquidation/stop-out, gap risk và position sizing. Chương này tách rõ ba khái niệm thường bị trộn lẫn: **notional exposure, margin requirement và amount at risk**.

### 04 — Macro drivers, rates, carry and sessions

[04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)

Một currency pair là giá tương đối giữa hai đồng tiền, vì vậy phải phân tích **hai nền kinh tế và hai đường lãi suất**. Chương này nối central-bank reaction function, inflation, growth, real yield, yield differential, carry, balance of payments, capital flows, risk sentiment, safe-haven behavior, commodity linkage và trading sessions vào cùng một causal chain.

### 05 — Execution, brokers, costs and operational risk

[05_EXECUTION_BROKERS_COSTS_AND_RISK.md](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)

Giải thích điều gì xảy ra từ lúc nhấn Buy/Sell tới khi position được fill: market/limit/stop order, spread, slippage, requote, rollover/financing, liquidity, news gaps, dealer model, agency model, counterparty risk, legal entity và broker due diligence. Đây là phần phải hiểu trước khi đánh giá bất kỳ strategy nào.

## Sau 5 chương đầu, người học phải tự trả lời được

Không cần học thuộc định nghĩa. Bạn cần có thể tự suy luận các câu hỏi như:

- EUR/USD tăng nghĩa là đồng nào mạnh tương đối so với đồng nào?
- vì sao `1 lot` không đồng nghĩa với cùng một mức rủi ro trên mọi pair?
- tại sao leverage 1:100 không có nghĩa nên dùng toàn bộ buying power?
- margin 1.000 USD có phải maximum loss là 1.000 USD không?
- vì sao pip value có thể thay đổi khi account currency khác quote currency?
- tại sao EUR/USD, GBP/USD và XAU/USD có thể tạo cùng một USD factor exposure dù là ba position khác nhau?
- vì sao một central bank tăng lãi suất nhưng currency vẫn có thể giảm?
- vì sao spread/slippage thường xấu đi đúng lúc trader muốn thoát nhất?
- vì sao retail OTC FX và exchange-traded FX futures không có cùng market structure?

Nếu chưa giải thích được bằng causal chain, phần nền vẫn chưa đủ chắc.

## Hướng mở rộng tiếp theo

Sau nền mechanics, nhánh Forex nên được mở rộng theo thứ tự:

```text
06  Price action, trend, range and volatility regimes
07  Technical indicators as data transformations
08  Fundamental and event-driven FX analysis
09  Carry, momentum, value and macro FX strategies
10  Backtesting and point-in-time FX data
11  Portfolio FX risk, correlation and factor exposure
12  Trading journal, review and performance attribution
13  Advanced FX microstructure and order flow
14  FX options, volatility and hedging
15  Korea / Vietnam FX market context and regulations
```

Các phần strategy chỉ nên xuất hiện sau khi người đọc hiểu mechanics và risk. Một setup không thể được đánh giá chỉ bằng win rate; nó phải được đặt trong expectancy, transaction cost, sample size, regime dependence, drawdown và khả năng thực thi thật.

## Nguyên tắc an toàn nghiên cứu

Forex là thị trường có thể sử dụng đòn bẩy lớn. Tài liệu này phục vụ **học cơ chế, phân tích và quản trị rủi ro**, không đưa ra tín hiệu mua/bán cá nhân hay hứa hẹn lợi nhuận.

Đối với retail OTC forex, phải xem broker/dealer như một phần của risk model. CFTC đặc biệt lưu ý rằng OTC retail customer không nhất thiết đang giao dịch trên một centralized exchange, và leverage có thể khuếch đại thua lỗ mạnh. Cần kiểm tra legal entity, cơ quan quản lý, điều khoản account, cách xử lý client money/margin, withdrawal, execution và dispute process trước khi nạp vốn.

## Nguồn nền nên dùng xuyên suốt

- Bank for International Settlements (BIS), **2025 Triennial Central Bank Survey**: https://www.bis.org/publications/triennial-central-bank-survey-foreign-exchange-and-over-the-counter-otc-derivatives-markets-2025
- BIS, **OTC foreign exchange turnover in April 2025** và các commentary liên quan.
- CFTC, **Eight Things You Should Know Before Trading Forex**: https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/CustomerAdvisory_MustKnowForex.html
- Các central bank, statistical agencies và official exchange/clearing documentation cho dữ liệu lãi suất, inflation, market convention và instrument-specific mechanics.

Với số liệu thời điểm, luôn ghi rõ ngày/kỳ dữ liệu. Không biến một snapshot thị trường thành quy luật vĩnh viễn.