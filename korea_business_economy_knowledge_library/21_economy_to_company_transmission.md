# Từ kinh tế vĩ mô đến công ty: cơ chế truyền dẫn (Macro-to-Company Transmission / 거시경제의 기업 전이)

Một trong những kỹ năng quan trọng nhất khi đọc kinh tế là không dừng ở headline. “Lãi suất tăng”, “won yếu”, “semiconductor export tăng” chỉ có giá trị khi ta biết biến đó truyền vào income statement, balance sheet hoặc cash flow của company nào.

## Framework truyền dẫn

```mermaid
graph LR
    M[Macro shock] --> I[Industry economics]
    I --> C[Company revenue/cost]
    C --> F[Cash flow & balance sheet]
    F --> V[Valuation / hiring / capex]
```

Mỗi arrow cần mechanism. Nếu không mô tả được mechanism, kết luận có thể chỉ là story.

## Ví dụ 1: KRW yếu

Shock: KRW depreciates against USD.

Exporter có USD revenue → KRW reported revenue có thể tăng. Nhưng imported input cost cũng tăng. Company hedges FX làm timing khác. Nếu competitor currency cũng yếu, pricing advantage giảm.

Kết luận đúng không phải “KRW yếu tốt cho Samsung/Hyundai”, mà là tính **net exposure** theo revenue, costs, debt và hedging.

## Ví dụ 2: Bank of Korea tăng rate

Base rate ↑ → bank funding/yields ↑ → corporate borrowing cost ↑. Consumer mortgage/card cost cũng tăng → discretionary demand có thể giảm.

Construction/PF bị double hit từ financing cost và housing demand. Bank có thể hưởng asset yield cao hơn nhưng credit loss và funding cost cũng thay đổi.

Growth stock valuation chịu higher discount rate ngay cả trước khi reported earnings đổi.

## Ví dụ 3: AI capex toàn cầu tăng

Hyperscalers tăng AI server capex → accelerator/HBM demand tăng → memory supplier ASP/mix tốt hơn → fab utilization/capex tăng → equipment/material supplier orders tăng.

Nhưng lag không giống nhau. HBM maker có revenue impact trước; fab equipment vendor có order theo investment schedule; utility/infrastructure có another lag.

## Ví dụ 4: Oil price tăng

Airline/freight/chemical feedstock cost ↑; inflation pressure ↑; household real income có thể giảm. Shipbuilding có thể hưởng LNG/energy vessel demand ở horizon dài hơn. Refining company effect phụ thuộc crack spread chứ không chỉ crude price.

Cùng một shock tạo winners và losers theo position trong value chain.

## Ví dụ 5: China demand slowdown

Korean exporters có direct China revenue giảm; commodity/material price có thể giảm; tourism/retail duty-free có thể yếu. Nhưng cheaper input có thể giúp downstream manufacturer. Phải phân tích exposure matrix.

## Ví dụ 6: Domestic wage tăng

Labor-intensive service SME chịu cost pressure; high-margin tech có thể absorb tốt hơn. Wage growth đồng thời hỗ trợ consumption, nên retail demand có thể tăng. Macro variable vừa là cost vừa là income cho household sector.

## Stock vs flow

Rất nhiều lỗi reasoning đến từ trộn stock và flow. Debt là stock tại một thời điểm; interest expense là flow. Backlog là stock of future work; new orders là flow additions. Inventory là stock; COGS là flow.

Một shock có thể thay flow trước rồi dần tích lũy thành stock. Ví dụ weak sales làm inventory stock tăng qua nhiều quý.

## First-order và second-order effects

First-order effect là direct: oil price ↑ → fuel cost ↑. Second-order: airline tăng ticket price → demand giảm; inflation ↑ → rate expectations ↑; household spending pattern đổi.

Professional analysis cần ít nhất nghĩ đến second-order, nhưng tránh chain quá dài không kiểm chứng.

## Scenario thinking

Không cần predict macro chính xác. Tạo scenario:

| Variable | Bear | Base | Bull |
|---|---:|---:|---:|
| Demand growth | -10% | 0% | +10% |
| FX KRW/USD | stronger KRW | current | weaker KRW |
| Input cost | +15% | flat | -10% |
| Rate | +100bp | flat | -100bp |

Sau đó map vào company. Mục tiêu không phải đoán đúng từng number mà biết **company nhạy với cái gì**.

## Transmission có lag và feedback

Macro shock hiếm khi vào income statement ngay lập tức. Rate tăng có thể mất vài tháng đến khi loan reset; FX hedge delay currency impact; commodity contract có formula lag. Vì vậy cần xác định **timing**.

Company cũng phản ứng lại macro: cut capex, raise prices, reduce hiring. Khi nhiều firms cùng làm vậy, micro response aggregate thành macro slowdown. Đây là feedback loop company → economy.

## Sensitivity matrix

Một cách thực dụng là tạo matrix:

| Shock | Revenue | Cost | Balance sheet | Valuation |
|---|---|---|---|---|
| KRW depreciation | exporter + / importer - | imported input - | FX debt - | foreign flow mixed |
| Rate increase | demand - | interest - | refinancing - | discount rate - |
| Oil increase | sector dependent | energy/logistics - | working capital - | inflation risk - |
| China slowdown | export exposure - | some commodity + | inventory risk | risk premium - |

Dấu không phải universal; purpose là force analyst trace channels.

## Second-order effect quan trọng hơn headline

Ví dụ oil price tăng trực tiếp làm airline cost tăng. Nhưng với petrochemical, feedstock cost tăng có thể pass-through tùy product spread. Với shipbuilding, high LNG price có thể thúc đẩy demand cho certain vessel types. Same shock, opposite second-order effects.

## Policy reaction

Macro shock thường kích thích response từ Bank of Korea, fiscal policy hoặc regulation. Analyst không nên freeze policy. Inflation cao có thể dẫn rate hike; recession có thể dẫn support package; housing stress có thể dẫn PF stabilization measures.

## Scenario tree

Thay vì one forecast, tạo base/upside/downside với key variables và probabilities riêng. Không cần precision giả. Mục tiêu là biết variable nào làm outcome đổi sign.

## Mental Model

> Tin kinh tế chỉ trở thành insight khi bạn có thể viết một chuỗi nhân quả ngắn: **shock → price/volume/cost → margin/cash flow → balance sheet → decision/valuation**.

## Common misconceptions

Correlation giữa macro variable và stock price trong quá khứ không chứng minh causal relationship ổn định. Regime, hedging và business mix thay đổi.

Một macro forecast chính xác cũng chưa đủ để kiếm lợi nhuận nếu expectation đó đã được priced in.

## Final connection

Dùng [20_how_to_analyze_a_korean_company](./20_how_to_analyze_a_korean_company.md) để biến transmission framework thành company-specific model. Quay lại [01_macro_economy_and_business_cycle](./01_macro_economy_and_business_cycle.md) và [02_trade_export_and_global_value_chains](./02_trade_export_and_global_value_chains.md) nếu cần nền macro/trade sâu hơn.

## Scenario matrix thay vì single forecast

Thay vì đoán một GDP/FX number, xây 3–4 scenarios với variables có causality rõ. Ví dụ semiconductor company:

| Scenario | Memory price | KRW/USD | AI demand | Expected direction |
|---|---:|---:|---|---|
| Bull cycle | tăng mạnh | KRW yếu vừa | mạnh | revenue/margin tốt |
| Mixed | tăng | KRW mạnh | mạnh | operational tốt, translation thấp hơn |
| Downcycle | giảm | KRW yếu | yếu | FX cushion nhưng ASP pressure |
| Supply shock | tăng | volatile | demand vừa | margin phụ thuộc input/capacity |

Table không phải forecast probability; nó giúp test thesis robustness.

## Elasticity thinking

Sensitivity không luôn linear. Nếu steel spread giảm 5%, profit có thể giảm >5% vì fixed cost. Nếu occupancy của platform/plant vượt breakeven, incremental margin có thể rất cao.

Do đó cần tìm nonlinear threshold.

## Feedback loop

Company response có thể quay lại macro. Semiconductor boom → capex/hiring → income/import equipment → current account/investment change. Housing downturn → construction cuts → employment/supplier income decline → demand giảm thêm.

Economy là feedback system, không phải one-way arrows.

## Time horizon

FX shock tác động translation ngay, contract pricing vài quý sau, capacity relocation vài năm sau. Một variable có sign khác theo horizon.

Analyst nên ghi rõ `0–3 months`, `1 year`, `3–5 years` thay vì nói “impact positive/negative” chung chung.