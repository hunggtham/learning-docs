# Lab 00 — Quotes, Margin và Position Sizing

Lab này kiểm tra xem bạn có thực sự hiểu economics của một FX position hay chỉ đang nhập số vào calculator của broker.

## Case A — EUR/USD, account USD

Giả sử:

```text
Account equity = 20,000 USD
EUR/USD bid/ask = 1.0848 / 1.0850
Planned long entry = market
Invalidation = 1.0800
Allowed planned loss = 0.50% equity
Commission = 7 USD per standard-lot round trip
Expected slippage on stop = 1.5 pip
```

Không bắt đầu bằng lot size. Hãy tính theo đúng flow:

```text
1. Planned entry price
2. Stop distance in pips
3. Allowed account loss
4. Pip value required
5. Base-currency units
6. Approximate lot size
7. Notional in USD
8. Effective leverage contributed by this position
9. Expected commission
10. Loss if stop fills with 1.5-pip adverse slippage
```

Sau đó trả lời: nếu broker cho leverage tối đa 1:100 thì thông tin đó có làm thay đổi position size vừa tính không? Giải thích tại sao.

## Case B — USD/JPY, account USD

```text
USD/JPY = 148.40 / 148.42
Position = long 100,000 USD
Exit = 149.02
```

Tính:

```text
Pip size
Move in pips
P/L in JPY
Approximate P/L in USD at exit
Pip value in JPY
Pip value in USD
```

Sau đó thay tỷ giá USD/JPY thành 120 và 170 nhưng giữ `100,000 USD` position. Quan sát vì sao pip value theo USD thay đổi dù contract size không đổi.

## Case C — EUR/GBP, account KRW

```text
EUR/GBP entry = 0.8650
Exit = 0.8720
Size = 50,000 EUR
GBP/USD = 1.2850
USD/KRW = 1,360
```

Tính P/L theo:

```text
GBP
→ USD
→ KRW
```

Sau đó giải thích tại sao account return còn phụ thuộc conversion path dù trade thesis ban đầu chỉ là EUR so với GBP.

## Case D — Margin stress

Giả sử:

```text
Account balance = 10,000 USD
Floating P/L initially = 0
Gross notional = 120,000 USD
Required margin = 4,000 USD
```

Tính equity, free margin và margin level ban đầu. Sau đó stress lần lượt:

```text
Scenario 1: floating loss -1,500
Scenario 2: floating loss -3,000
Scenario 3: spread widening creates additional -500 mark-to-market effect
Scenario 4: broker raises required margin from 4,000 to 6,000
```

Với từng scenario, tính lại:

```text
Equity
Used Margin
Free Margin
Margin Level
Effective Gross Leverage
```

Mục tiêu là thấy margin stress có thể tăng dù strategy chưa chạm stop.

## Case E — Portfolio heat

Bạn đang có:

```text
Long EUR/USD: planned loss 100 USD
Long GBP/USD: planned loss 100 USD
Short USD/JPY: planned loss 100 USD
```

Không được kết luận tổng risk chỉ là `300 USD` độc lập. Hãy viết currency decomposition:

```text
EUR exposure
GBP exposure
JPY exposure
USD exposure
```

Sau đó tạo stress `USD strengthens rapidly` và mô tả vì sao ba vị thế có thể cùng bị adverse move và cùng chịu spread/slippage cao hơn bình thường.

## Đầu ra bắt buộc

Tạo `fx_position_risk_sheet.md` gồm:

```text
Instrument
Legal/contract product
Account currency
Base units
Notional
Entry / Stop
Pip value
Planned loss
Expected execution cost
Gap/slippage stress loss
Required margin
Effective leverage
Currency-factor exposure
Portfolio heat contribution
```

## Tự chấm

Bài đạt khi bạn có thể đi từ **account-risk budget → invalidation → size → notional → margin → stress loss** mà không dùng “broker cho bao nhiêu lot” làm điểm xuất phát.

Đọc lại nếu cần:

- [02 — Quotes, pips, lots and P/L](../02_QUOTES_PIPS_LOTS_AND_PNL.md)
- [03 — Leverage, margin and position sizing](../03_LEVERAGE_MARGIN_POSITION_SIZING.md)
