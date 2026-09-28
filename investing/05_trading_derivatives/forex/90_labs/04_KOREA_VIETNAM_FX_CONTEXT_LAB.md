# Lab 04 — Korea / Vietnam FX Context

Lab này luyện phân tích USD/KRW và USD/VND như hai hệ thống khác nhau về market structure, policy framework, capital flows và khả năng tiếp cận. Không được lấy rule của EUR/USD rồi áp thẳng sang KRW hoặc VND.

## Case A — USD/KRW shock map

Giả sử:

```text
US 2Y yield +75 bp
Oil +15%
Global semiconductor demand remains strong
Foreign investors reduce Korean equity exposure
BOK expected path changes only slightly
Broad DXY +4%
```

Viết causal map:

```text
US rates
→ relative yield / USD funding
→ broad USD
→ USD/KRW
→ imported-energy cost
→ Korea inflation / BOK constraint
→ foreign portfolio flows
→ exporter/importer earnings sensitivity
```

Sau đó tách ít nhất ba forces có thể đi ngược nhau. Ví dụ semiconductor export strength có thể hỗ trợ Korea external income trong khi oil và foreign outflow gây áp lực KRW.

## Case B — USD/VND pressure

Giả sử:

```text
USD broad +5%
Regional Asian currencies weaken
Vietnam export growth remains positive
Domestic credit growth accelerates
Import demand rises
```

Không kết luận ngay VND phải giảm đúng bằng broad USD move. Hãy phân tích:

```text
FX-management framework
Official/reference/interbank context
Trade flows
FDI / portfolio flows
Domestic liquidity
Interest-rate constraints
Reserve / policy considerations
Market-access constraints
```

Mục tiêu là hiểu VND không có cùng price-discovery structure với major freely floating FX pairs.

## Case C — Cross-border investor

Một investor sống tại Hàn Quốc có KRW liabilities nhưng nắm:

```text
US ETF in USD
Korean equities in KRW
Vietnam exposure through a fund/wrapper
Cash in KRW
```

Lập bảng:

```text
Asset
Trading currency
Underlying economic currency
Reporting currency
Liability currency
Hedged or unhedged
Wrapper / domicile
FX conversion path
Liquidity
Tax / operational item to verify
```

Sau đó stress:

```text
KRW +10% vs USD
KRW -10% vs USD
VND weakens while underlying Vietnamese assets rise 12%
```

Giải thích local-asset return và investor return có thể khác nhau như thế nào.

## Case D — Regulation/access checklist

Không ghi một rule pháp lý từ trí nhớ. Với Korea và Vietnam, tạo checklist research:

```text
Exact product
Retail vs institutional participant
Onshore vs offshore access
Legal entity / intermediary
Regulator / official authority
Current rule date
Capital / reporting restriction if relevant
Settlement / conversion mechanics
Official source URL
```

Nếu một rule có thể thay đổi, ghi `verify current rule before use` và ngày kiểm tra.

## Case E — Korea retail FX-margin distinction

Giải thích bằng lời của bạn sự khác nhau giữa:

```text
Ordinary currency exchange
Institutional spot/forward FX
Exchange-traded currency futures
Retail leveraged FX-margin product
```

Sau đó xác định loại intermediary/legal framework nào cần được kiểm tra trước khi giao dịch retail leveraged FX tại Korea.

Không biến phần này thành broker recommendation.

## Case F — Event transmission comparison

Chọn một broad USD shock và so:

```text
EUR/USD
USD/KRW
USD/VND
```

Với mỗi pair, ghi:

```text
Market structure
Policy framework
Liquidity
Capital-flow sensitivity
Main macro channels
Potential intervention/management channel
Data quality / accessibility
Execution implication
```

Mục tiêu là thấy cùng một USD shock có thể truyền khác nhau vì institutional structure khác nhau.

## Đầu ra bắt buộc

Tạo:

```text
krw_fx_map.md
vnd_fx_map.md
cross_border_currency_exposure.md
fx_regulatory_verification_checklist.md
```

Mỗi file phải có `as_of_date` nếu dùng regulation hoặc market-structure facts có thể thay đổi.

## Tự chấm

Bài chưa đạt nếu kết luận chỉ là `Fed hawkish → USD/KRW up` hoặc `USD mạnh → USD/VND up`. Bài đạt khi bạn chỉ ra được **policy constraint, flow, market structure, access rule và transmission channel** khác nhau giữa hai thị trường.

Đọc lại:

- [15 — Korea / Vietnam FX market context and regulations](../15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)
- [04 — Macro drivers, rates, carry and sessions](../04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
