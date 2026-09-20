# Case Study 01 — Từ CPI Surprise tới Portfolio Decision

> Đây là case study xuyên domain. Mục tiêu không phải học khẩu quyết `CPI tăng → cổ phiếu giảm`, mà hiểu một inflation surprise truyền qua rates, FX, credit, earnings, valuation, portfolio và execution như thế nào. Toàn bộ case dùng ví dụ giả định để giữ tính evergreen.

## 1. Bối cảnh giả định

Giả sử market bước vào ngày công bố CPI với expectation inflation đang giảm dần. Consensus headline CPI là 2,8% YoY, core CPI 2,9%. Market đang price một xác suất khá cao central bank sẽ bắt đầu easing trong vài meeting tới.

Actual data:

```text
Headline CPI: 3.2%
Core CPI: 3.3%
Shelter: sticky
Core services ex-housing: firm
Goods inflation: flat
```

Điểm đầu tiên cần nhìn không phải “3,2% cao”, mà là **surprise so với pricing**. Nếu market kỳ vọng 3,1%, surprise nhỏ. Nếu kỳ vọng 2,8%, cùng một actual tạo reaction lớn hơn.

## 2. Bước 1 — Decompose Inflation

Inflation không phải một số duy nhất. Hãy tách:

```text
Goods
Shelter
Services
Energy
Food
Wages / Unit Labor Cost
```

Goods inflation có thể biến động do supply chains. Shelter thường lag rental market. Services inflation thường gắn wage và domestic demand nhiều hơn.

Nếu surprise chủ yếu do energy spike tạm thời, central bank reaction có thể khác surprise đến từ sticky core services. Vì vậy composition quan trọng hơn headline alone.

Đọc thêm: [Macro Data Playbook](../04_economics/03_MACRO_DATA_PLAYBOOK.md).

## 3. Bước 2 — Update Reaction Function

Central bank không phản ứng với CPI một cách cơ học. Market hỏi:

```text
Inflation persistence?
Labor market still tight?
Growth resilient?
Financial conditions easy or tight?
Inflation expectations anchored?
```

Nếu core services vẫn mạnh và employment chưa hạ nhiệt, market có thể đẩy expected policy path cao hơn. Nếu growth đã suy yếu mạnh, same CPI surprise có thể không làm repricing lớn như vậy.

Do đó:

```text
CPI Surprise
→ Persistence Assessment
→ Reaction Function
→ Expected Policy Path
```

## 4. Bước 3 — Front-End Yields

2Y yield thường nhạy với expected policy path. Nếu market delay rate cuts, 2Y yield có thể tăng nhanh.

Đây là layer quan trọng vì nó cho biết market hiểu CPI shock chủ yếu như policy shock hay không.

Nếu CPI beat nhưng 2Y yield không phản ứng, có thể surprise đã priced hoặc composition được xem temporary.

## 5. Bước 4 — Long-End Yields

10Y/30Y phản ứng phức tạp hơn. Long-end yield có thể tăng vì:

```text
Higher expected short rates
Higher inflation uncertainty
Higher term premium
```

Nhưng nếu market nghĩ tighter policy sẽ crush future growth, long end có thể tăng ít hơn front end, tạo flattening.

Nếu fiscal supply/term premium cùng xấu đi, long end có thể tăng mạnh hơn, tạo bear steepening.

Đọc thêm: [Bonds, Rates and Credit](../02_asset_classes/02_BONDS_RATES_AND_CREDIT.md).

## 6. Bước 5 — Real Yields và Equity Duration

Equity valuation có thể nghĩ như present value của future cash flows. Long-duration equities phụ thuộc distant earnings nhiều hơn.

Nếu real yields tăng, discount rate tăng. Những companies có cash flow xa trong tương lai thường nhạy hơn.

Một simplified relation:

```text
Higher Real Yield
→ Higher Discount Rate
→ Lower PV of Distant Cash Flows
→ Pressure on High-Duration Equity Multiples
```

Điều này không có nghĩa tech luôn giảm khi yields tăng. Nếu earnings expectations tăng nhanh hơn discount rate, stock vẫn có thể tăng. Luôn tách **earnings effect** và **multiple effect**.

## 7. Bước 6 — USD

Nếu expected US rates repriced higher relative other economies, USD thường có support.

Nhưng FX không chỉ là interest differential. Risk-off flow, terms of trade, intervention và local policy đều matter.

Với Korea:

```text
Higher US Yields
→ Stronger USD
→ USD/KRW Up
→ Imported Inflation / Financial-Condition Pressure
```

Korean exporters có thể nhận translation benefit, nhưng foreign investor flow và valuation pressure có thể offset.

Với Vietnam, stronger USD có thể thu hẹp easing room nếu VND pressure tăng.

Đọc thêm: [Cross-Market Global Shocks](../06_markets_korea_vietnam/03_CROSS_MARKET_GLOBAL_SHOCKS.md).

## 8. Bước 7 — Credit Conditions

Nếu inflation surprise kéo rate expectations cao hơn, refinancing cost tăng. Impact lớn hơn với:

```text
Floating-rate borrowers
Near-term maturity wall
Low interest coverage
Leveraged property
Weak small businesses
```

Credit spread có thể widen nếu market chuyển từ “higher for longer nhưng growth okay” sang “higher for longer sẽ gây default”.

Nếu Treasury yields tăng nhưng credit spreads không widen, shock có thể chủ yếu là rate-duration shock. Nếu cả yields lẫn spreads tăng, financial conditions tighten rộng hơn.

## 9. Bước 8 — Sector Mapping

### Banks

Higher rates có thể hỗ trợ NIM lúc đầu nhưng funding cost và credit losses tăng về sau. Vì vậy bank sensitivity có time lag.

### REIT / Property

Higher discount/cap rates làm valuation pressure. Refinancing cost tăng. Nếu rents strong, NOI có thể offset một phần.

### Semiconductors / Growth

Multiple sensitivity phụ thuộc duration. Nhưng nếu AI capex/earnings revisions vẫn cực mạnh, earnings channel có thể dominate.

### Utilities / Defensives

Có stable cash flow nhưng often duration-like due high dividends/regulated returns. Rising long yields can pressure multiples.

### Commodity Producers

Nếu inflation surprise do demand strength, commodity companies có thể benefit. Nếu due supply shock, downstream users suffer more.

## 10. Bước 9 — Company Earnings

Một macro shock chỉ có giá trị đầu tư khi translate được tới company model.

Ví dụ exporter Korea:

```text
KRW weak
→ USD revenue translation benefit
BUT
Imported input cost up
+ Funding cost up
+ Global demand may slow
```

Do đó build currency map:

```text
Revenue currency
Cost currency
Debt currency
Hedge policy
```

Không dùng slogan `KRW weak = exporter good`.

## 11. Bước 10 — Valuation Attribution

Giả sử stock giảm 8% sau CPI. Hãy hỏi:

```text
Bao nhiêu do EPS estimate giảm?
Bao nhiêu do P/E multiple compress?
Bao nhiêu do FX/flow/liquidity?
```

Nếu EPS unchanged nhưng multiple từ 30x xuống 27x, move chủ yếu là discount-rate repricing.

Nếu EPS consensus cũng giảm, macro shock đang đi vào earnings channel.

Đọc thêm: [Valuation](../03_company_analysis/03_VALUATION_DCF_AND_MULTIPLES.md).

## 12. Bước 11 — Portfolio-Level Exposure

Một portfolio có thể chứa:

```text
US growth ETF
Long-duration Treasury ETF
Korea semiconductor ETF
REIT
Gold
```

Nhìn ticker thì đa dạng, nhưng inflation shock có thể làm four positions đầu cùng chịu rising real-yield pressure.

Hãy map factors:

```text
Duration
USD
Growth
Credit
Inflation
Commodity
Liquidity
```

Đọc thêm: [Multi-Asset Allocation](../02_asset_classes/05_MULTI_ASSET_HEDGING_CURRENCY_AND_REGIME_ALLOCATION.md).

## 13. Bước 12 — Hedge Design

Nếu concern là temporary rate shock, có thể hedge duration bằng futures hoặc reduce long-duration exposure.

Nếu concern là equity beta, index futures more direct.

Nếu concern là tail event, put/put spread có convex protection nhưng premium cost.

Hedge phải match risk:

```text
Rate Risk → DV01 / Rate Futures / Swaps
Equity Beta → Index Futures
Tail Risk → Options
FX Risk → FX Forward / Hedge Ratio
```

Sai hedge instrument tạo basis risk.

## 14. Bước 13 — Position Sizing

Không nên size chỉ dựa “CPI sẽ xấu”. Hãy define scenario loss.

Ví dụ:

```text
Base: 2Y +15bp, 10Y +10bp, USD +1%, equities -2%
Bear: 2Y +40bp, 10Y +35bp, USD +3%, credit spreads +30bp
Tail: inflation expectations unanchor, long-end +70bp, equities -8%, liquidity worse
```

Portfolio stress theo các states này rồi mới quyết định size.

## 15. Bước 14 — Execution

Macro event có spread/slippage lớn. Nếu trading quanh CPI:

- market order có gap/slippage;
- stop có thể fill xa trigger;
- limit order có thể không fill hoặc adverse-selected;
- option IV thường elevated trước event.

Execution plan phải được quyết định **trước** release.

Đọc thêm: [Execution & Microstructure](../05_trading_derivatives/03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md).

## 16. Long Option không chỉ cần direction đúng

Nếu investor mua put trước CPI, P/L phụ thuộc:

```text
Spot Move
Implied Volatility Change
Theta
Skew
Execution Cost
```

Market giảm ít hơn implied move có thể làm put không lời nhiều như kỳ vọng. Sau event, IV crush có thể offset directional gain.

Đọc thêm: [Options & Volatility](../05_trading_derivatives/05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md).

## 17. Korea-specific Translation

Một inflation shock US có thể đi:

```text
US CPI beat
→ US yields ↑
→ USD ↑
→ USD/KRW ↑
→ Foreign flow pressure
→ Long-duration KOSDAQ pressure
```

Nhưng semiconductors có thể resist nếu global earnings revisions vẫn improve. Banks có mixed NIM/credit effect. Airlines/importers có FX/fuel vulnerability.

Đọc thêm: [Korea Market Playbook](../06_markets_korea_vietnam/01_KOREA_MARKET_PLAYBOOK.md).

## 18. Vietnam-specific Translation

Potential chain:

```text
US yields / USD ↑
→ VND pressure ↑
→ SBV easing room ↓
→ Domestic liquidity expectation weaker
→ Property / brokers / leveraged sectors sensitive
```

Nhưng domestic credit policy, deposit rates, public investment và local earnings can dominate over time.

Đọc thêm: [Vietnam Market Playbook](../06_markets_korea_vietnam/02_VIETNAM_MARKET_PLAYBOOK.md).

## 19. What Was Priced?

Một CPI beat chỉ tạo edge nếu market reaction khác expectation embedded trước event.

Pre-event checklist:

```text
Consensus
Whisper estimate
Fed-path pricing
2Y yield level
Equity valuation
Positioning
Option implied move
USD positioning
```

Nếu market already priced hot CPI, actual beat có thể gây little reaction hoặc reversal.

## 20. Cross-Asset Confirmation

Sau release, check:

```text
2Y Yield
10Y Yield
Real Yield
Breakeven Inflation
USD
Credit Spreads
Gold
Oil
Equity Breadth
Growth vs Value
```

Nếu 2Y up nhưng real yields flat và USD weak, narrative “hawkish repricing” có thể không fully fit.

## 21. Post-Event Attribution

Một review tốt không ghi “tôi đoán đúng CPI”. Hãy tách:

```text
Macro thesis correct?
Rate reaction correct?
FX reaction correct?
Sector mapping correct?
Position sizing correct?
Execution cost acceptable?
Hedge worked as intended?
```

Decision quality có thể tốt dù P/L âm nếu one low-probability path xảy ra.

## 22. Invalidation

Ví dụ thesis ban đầu:

> Sticky inflation sẽ delay easing và gây duration-pressure.

Invalidation có thể là:

```text
Labor market collapses rapidly
Core inflation composition weakens
Central bank signals tolerance for temporary inflation
Financial stress forces policy pivot
```

Thesis phải update khi mechanism thay đổi, không khi price chỉ đi ngược vài sessions.

## 23. Reusable Template

Khi data inflation mới xuất hiện:

```text
1. Actual vs Consensus
2. Composition
3. Persistence
4. Reaction Function
5. Front-End Yields
6. Long-End / Term Premium
7. Real Yields / Breakevens
8. USD / Local FX
9. Credit
10. Sector Earnings
11. Valuation
12. Positioning
13. Portfolio Exposure
14. Hedge
15. Execution
16. Attribution
```

## Kết luận

Một CPI print không phải trading signal tự động. Nó là **information shock** làm market update probability distribution của growth, inflation và policy. Investor tốt không dừng ở `CPI ↑ → stocks ↓`; họ theo dõi từng transmission channel, kiểm tra what was priced, map tới cash flows và chỉ sau đó mới quyết định exposure, hedge và size.