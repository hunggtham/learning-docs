# Lab 03 — Portfolio FX Risk

Lab này chuyển tư duy từ từng ticket sang **currency-factor exposure**. Nhiều pair khác nhau có thể thực chất là cùng một directional bet được lặp lại.

## Bối cảnh

Giả sử portfolio có:

```text
Long EUR/USD   50,000 EUR
Long GBP/USD   40,000 GBP
Short USD/JPY  60,000 USD
Long AUD/JPY   50,000 AUD
Long XAU/USD   position with 70,000 USD-equivalent notional
```

Account currency là USD.

## Bước 1 — Currency decomposition

Viết mỗi position thành hai legs:

```text
EUR/USD long = +EUR -USD
GBP/USD long = +GBP -USD
USD/JPY short = -USD +JPY
AUD/JPY long = +AUD -JPY
```

Với gold, ghi rõ đây không phải currency pair nhưng vẫn có USD-price exposure.

Sau đó quy đổi approximate exposures về một reporting currency để có thể aggregate.

## Bước 2 — Gross và net

Tính:

```text
Gross notional
Net USD exposure
Net JPY exposure
Other currency exposures
Gross leverage
```

Giải thích tại sao net exposure nhỏ không có nghĩa gross liquidity/margin risk nhỏ.

## Bước 3 — Correlation is conditional

Lấy một correlation window bình thường và một stress window nếu có dữ liệu. So sánh:

```text
EUR/USD vs GBP/USD
EUR/USD vs XAU/USD
USD/JPY vs AUD/JPY
```

Không kết luận diversification chỉ từ full-sample correlation.

## Bước 4 — Stress scenarios

Tạo ít nhất bốn stress:

```text
A. Broad USD +5%
B. JPY +8% funding unwind
C. Global risk-off: USD +3%, JPY +5%, gold initially -4%, spreads widen
D. Policy-divergence reversal: EUR and GBP +4% vs USD while JPY weakens 3%
```

Với mỗi stress, ước lượng:

```text
Position-level P/L
Portfolio P/L
Margin impact
Largest factor contributor
Expected spread/slippage deterioration
```

## Bước 5 — Portfolio heat

Giả sử mỗi trade riêng lẻ có planned stop loss bằng `0.5%` equity. Tính nominal sum của planned risks, sau đó tạo common-shock scenario làm nhiều stops bị hit cùng lúc với slippage gấp đôi bình thường.

So sánh:

```text
Naive sum of standalone risk
vs
Correlated stressed loss
```

## Bước 6 — Hedge quality

Thử hedge một phần USD exposure bằng một instrument khác. Không chỉ hỏi hedge ratio theo notional. Hãy ghi:

```text
Target factor to hedge
Instrument chosen
Basis risk
Liquidity
Carry / financing cost
Maturity mismatch if any
Residual exposure
```

Một hedge làm giảm beta nhưng tạo carry hoặc basis risk vẫn cần được attribution riêng.

## Bước 7 — Risk limits

Thiết kế limits theo nhiều lớp:

```text
Max risk per trade
Max currency-factor exposure
Max gross leverage
Max portfolio heat
Max correlated cluster risk
Max event exposure
Max margin usage
Minimum free-margin buffer
```

Không dùng một limit duy nhất như “mỗi trade 1%”.

## Đầu ra bắt buộc

Tạo `fx_portfolio_risk_dashboard.md` với:

```text
Pair / instrument
Direction
Notional
Currency legs
Factor bucket
Standalone planned loss
Stress loss
Margin usage
Liquidity flag
Correlation cluster
Hedge status
```

Thêm một bảng stress tổng hợp và một phần giải thích limit nào sẽ kích hoạt trước trong từng scenario.

## Tự chấm

Bài đạt khi bạn có thể nhìn ba trade khác nhau và nhận ra chúng có thể là **một macro bet được nhân ba**.

Đọc lại:

- [11 — Portfolio FX risk, correlation and factor exposure](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [03 — Leverage, margin and position sizing](../03_LEVERAGE_MARGIN_POSITION_SIZING.md)
