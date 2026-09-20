# Kinh tế vĩ mô và chu kỳ kinh doanh Hàn Quốc (Macroeconomy & Business Cycle / 거시경제와 경기순환)

Một công ty có thể được quản trị rất tốt nhưng vẫn chịu shock từ lãi suất, KRW, giá năng lượng, global trade hoặc semiconductor cycle. **Macroeconomics / 거시경제학** là cách nhìn nền kinh tế ở cấp hệ thống để hiểu những điều kiện chung đó.

Mục tiêu của chapter này không phải biến người đọc thành forecaster. Mục tiêu là biết **macro variable nào đang thay constraint của household, bank, industry và company**, rồi trace effect xuống revenue, cost, balance sheet và valuation.

## GDP đo flow của value added, không phải “tài sản của quốc gia”

**Gross Domestic Product (GDP / 국내총생산)** đo value added được tạo ra trong lãnh thổ trong một period.

Từ phía chi tiêu:

\[
Y = C + I + G + (X-M)
\]

Trong đó:

- `C`: private consumption;
- `I`: investment;
- `G`: government consumption/investment;
- `X`: exports;
- `M`: imports.

Đây là accounting identity, không phải causal formula. Tăng `X` không tự động làm GDP tăng cùng magnitude nếu export dùng nhiều imported inputs hoặc các thành phần khác thay đổi.

Với Korea, `I` và external demand đặc biệt quan trọng vì semiconductor, manufacturing equipment, autos, shipbuilding và construction có weight lớn.

## Value added: tránh double counting

Nếu steel company bán steel 100 cho auto maker, auto maker bán car 300, GDP không cộng 100 + 300 = 400 nếu steel đã embedded trong car.

GDP tính **value added** ở mỗi stage.

Mental model:

```text
Revenue
- Intermediate inputs
= Value added
```

Điều này quan trọng khi đọc exports. Gross exports có thể lớn nhưng domestic value captured phụ thuộc imported content.

Xem [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md).

## Nominal GDP, Real GDP và price effect

**Nominal GDP / 명목 GDP** dùng current prices. **Real GDP / 실질 GDP** cố loại price change để đo output volume.

Tương tự company revenue:

```text
Revenue growth
= Price effect + Volume effect + Mix effect
```

Nếu nominal sales tăng 10% nhưng selling price tăng 12%, physical volume có thể giảm.

Macro cũng vậy: nominal growth không đồng nghĩa real activity tăng tương ứng.

## GDP per capita không bằng household welfare

GDP per capita giúp so output theo population nhưng vẫn không capture đầy đủ:

- income distribution;
- unpaid household work;
- leisure;
- environmental cost;
- asset-price affordability;
- quality of public services.

Một economy có GDP per capita tăng nhưng young renters có thể cảm thấy living standard xấu đi nếu housing cost tăng nhanh hơn income.

Vì vậy GDP là production metric quan trọng, không phải universal welfare score.

## GDI và Terms of Trade: purchasing power của Korea có thể đổi ngay cả khi output không đổi

Korea import phần lớn oil, gas và raw materials. Nếu import prices tăng mạnh, cùng export volume mua được ít imports hơn.

**Terms of Trade (교역조건)** có thể hiểu đơn giản:

\[
Terms\ of\ Trade = \frac{Export\ Price\ Index}{Import\ Price\ Index}
\]

Nếu denominator tăng nhanh, terms of trade xấu đi.

**Gross Domestic Income (GDI / 국내총소득)** giúp nhìn purchasing-power effect mà real GDP có thể không phản ánh đầy đủ.

Ví dụ, factory vẫn sản xuất same volume nhưng energy import bill tăng mạnh. Real production không giảm nhiều, nhưng national real income có thể chịu pressure.

## Potential growth: vì sao Korea không thể lặp lại tốc độ 1970s

Quarterly growth và long-run capacity là hai khái niệm khác nhau.

**Potential Growth / 잠재성장률** hỏi economy có thể tăng bền vững bao nhiêu khi labor/capital được sử dụng ở mức bình thường mà không tạo inflation pressure quá mức.

Một decomposition hữu ích:

\[
Growth \approx Labor\ Growth + Capital\ Deepening + TFP\ Growth
\]

High-growth Korea từng có cả ba drivers mạnh:

1. labor chuyển từ agriculture sang industry;
2. investment/capital stock tăng nhanh;
3. technology catch-up nâng TFP.

Current Korea có working-age population giảm, capital stock đã lớn và technology gap với frontier nhỏ hơn. Vì vậy same mechanism không thể tạo same growth rate.

BOK research gần đây nhấn mạnh slower capital accumulation, demographic decline và weak productivity diffusion như các constraints lên potential growth.

Đây không phải dấu hiệu economy “thất bại”; nó phản ánh stage of development. Câu hỏi mới là productivity và per-capita living standards tăng thế nào.

## Output gap: actual economy so với sustainable capacity

**Output Gap / GDP갭** là difference giữa actual output và estimated potential output.

```text
Positive output gap
→ demand > sustainable capacity
→ inflation/wage pressure dễ tăng

Negative output gap
→ slack / idle capacity
→ disinflationary pressure dễ tăng
```

Nhưng potential output không quan sát trực tiếp; nó là model estimate. Vì vậy output gap không phải thermometer chính xác và có thể được revise.

Central bank luôn nhìn nhiều indicators thay vì dựa một number.

## Business cycle: trend và cycle phải tách riêng

Economy dao động quanh long-term trend.

Một simplified cycle:

```text
Demand recovery
   ↓
Production / orders rise
   ↓
Inventory + capex + hiring rise
   ↓
Capacity pressure / inflation
   ↓
Financial tightening
   ↓
Demand slows
   ↓
Inventory correction / capex cuts
```

Cycle không chạy như đồng hồ và mỗi sector có timing khác nhau.

Korea đặc biệt có **semiconductor cycle**, housing/construction cycle, credit cycle và global trade cycle.

Vì vậy khi company earnings tăng phải hỏi: **structural growth hay cyclical recovery?**

## Semiconductor cycle: tại sao một industry có thể làm macro data rung mạnh

Memory semiconductor có high fixed cost và volatile price. Khi demand/supply balance thay đổi, price và profit có thể swing rất mạnh.

Boom truyền qua:

```text
Chip price/order ↑
→ semiconductor profit ↑
→ exports ↑
→ capex ↑
→ equipment/material orders ↑
→ tax/income/employment spillover
```

Downcycle đảo chain.

Do semiconductor có weight lớn trong exports/corporate profits, macro Korea có sensitivity lớn hơn many diversified economies.

Xem [`14_semiconductors_electronics_display.md`](./14_semiconductors_electronics_display.md).

## Inflation: price level chung, không phải một món hàng tăng giá

**Inflation / 인플레이션** là sustained increase trong general price level.

Headline CPI có food/energy; **core inflation / 근원물가** cố nhìn underlying trend bằng cách loại một số volatile components tùy methodology.

Inflation có thể đến từ:

- demand mạnh;
- wage pressure;
- import price/FX;
- energy/food shocks;
- supply constraints;
- expectations.

Một oil shock đối với Korea vừa là inflation shock vừa là income shock vì country import energy.

## Inflation expectations: belief có thể ảnh hưởng actual behavior

Nếu workers/firms tin inflation cao sẽ kéo dài, workers đòi wage cao hơn và firms set price cao hơn để protect margins.

Do đó central bank quan tâm expectations, không chỉ current CPI.

Inflation credibility quan trọng vì policy dễ hơn nếu public tin inflation sẽ quay về target.

## Bank of Korea policy rate: một price ảnh hưởng nhiều markets

BOK không “điều khiển GDP” trực tiếp. Policy rate truyền qua system:

```text
Base rate
   ↓
Money-market / bond yields
   ↓
Bank deposit & loan rates
   ↓
Household + corporate debt service
   ↓
Consumption / capex / housing
```

Song song, rate expectations ảnh hưởng FX và asset prices.

Transmission có **lag / 시차** vì loans reprice khác nhau và firms/households không đổi behavior ngay lập tức.

## Discount rate và company valuation

Một future cash flow có present value:

\[
PV = \frac{CF_t}{(1+r)^t}
\]

Nếu `r` tăng, distant cash flow bị discount mạnh hơn.

Do đó growth companies với cash flow xa trong future thường valuation-sensitive hơn firms tạo cash ngay hiện tại.

Nhưng “rate cut = stocks tăng” không phải luật. Nếu cut xảy ra vì recession sâu, earnings deterioration có thể lớn hơn discount-rate benefit.

## Yield curve: market kỳ vọng gì về time

Government bond yields ở các maturities tạo **yield curve / 수익률곡선**.

Curve phản ánh expected future policy rates, inflation, term premium và risk sentiment.

Corporate debt pricing lại thêm credit spread.

Vì vậy company refinancing cost có thể tăng dù BOK rate không đổi nếu investor risk premium tăng.

Xem [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md).

## KRW/USD: tỷ giá là relative price và balance-sheet variable

Nếu KRW weakens against USD, exporter nhận USD có thể quy đổi nhiều KRW hơn. Nhưng benefit chỉ đúng nếu costs/debt không tăng tương ứng.

Cần map four exposures:

```text
Revenue currency
Cost currency
Asset currency
Debt currency
```

Shipbuilder có USD contract và nhiều KRW cost khác airline mua fuel USD. Semiconductor seller có USD revenue nhưng nhập equipment. Domestic retailer import goods có exposure ngược exporter.

Do đó “won yếu tốt cho Korea” là oversimplification.

## FX pass-through và imported inflation

KRW depreciation làm imported oil/material/product price tính bằng KRW cao hơn nếu supplier không giảm USD price.

Mức độ truyền vào CPI gọi là **exchange-rate pass-through**.

Firm có pricing power có thể pass cost sang consumer; firm cạnh tranh mạnh phải absorb margin.

Vì vậy FX shock có distribution effect giữa sectors.

## Current account và trade balance khác nhau

**Trade Balance / 무역수지** thường nói goods exports minus goods imports.

**Current Account / 경상수지** rộng hơn, gồm:

- goods;
- services;
- primary income;
- secondary income/transfers.

Korean firms sở hữu assets/operations abroad nên investment income ngày càng quan trọng.

Một economy có goods surplus lớn vẫn có service deficit; current account mới cho external income flow rộng hơn.

## Current account surplus không tự động “tốt”

Surplus có thể phản ánh strong exports/productivity, nhưng cũng có thể tăng khi domestic investment/consumption yếu làm imports giảm.

Do đó phải hỏi **why surplus exists**.

Macro variables không nên được đánh giá tốt/xấu chỉ bằng sign.

## Fiscal policy và automatic stabilizers

Government budget ảnh hưởng demand trực tiếp qua spending và transfers.

**Automatic Stabilizers / 자동안정화장치** hoạt động không cần new law mỗi recession: tax revenue giảm khi income/profit giảm, một số transfers/social spending tăng.

Discretionary fiscal stimulus có multiplier phụ thuộc:

- spare capacity;
- household saving;
- monetary stance;
- import leakage;
- policy design.

Open economy như Korea có thể thấy một phần stimulus chảy sang imports.

## Fiscal deficit và public debt: stock vs flow

**Fiscal deficit** là flow trong một period. **Public debt** là accumulated stock.

Một year deficit không giống debt crisis. Sustainability phụ thuộc growth, interest rate, maturity, tax base và future spending obligations.

Aging làm pension/health spending trở thành long-run fiscal variable, nên demographic analysis phải nối với public finance.

## Household credit cycle

Housing và household debt là macro amplifier.

Khi property values rise:

```text
Collateral value ↑
→ borrowing capacity ↑
→ spending/investment ↑
→ asset demand ↑
```

Downturn có thể đảo loop.

Macroprudential rules như LTV/DSR cố target leverage cụ thể hơn policy rate.

Xem [`27_demographics_households_and_consumption.md`](./27_demographics_households_and_consumption.md).

## Construction cycle và PF

Construction có long lead time và financing dependence cao. Rate increase hoặc presale weakness có thể làm project finance stress xuất hiện trước official construction GDP collapse.

PF distress truyền sang contractors, securities firms, lenders và suppliers.

Do đó Korean macro dashboard nên include housing transactions, unsold units, construction orders và PF indicators khi relevant.

Xem [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md).

## Labor market: employment quantity và job quality khác nhau

Unemployment rate thấp không tự động nghĩa labor market khỏe toàn diện.

Cần nhìn:

- participation rate;
- employment by age/gender;
- regular vs non-regular;
- wage growth;
- hours;
- vacancies;
- SME/large-firm gap.

Aging có thể làm unemployment rate thấp một phần vì labor-force composition thay đổi, không chỉ vì demand rất mạnh.

## Wage–productivity relationship

Nếu nominal wage tăng nhanh hơn productivity kéo dài, unit labor cost tăng và firm margin/price chịu pressure.

Một simplified measure:

\[
Unit\ Labor\ Cost \approx \frac{Wage\ per\ Worker}{Output\ per\ Worker}
\]

Nhưng aggregate relationship khác nhau theo sector. Semiconductor capital intensity cao, restaurant labor intensity cao.

Do đó wage pressure phải map theo business model.

## Leading, coincident và lagging indicators

Economic indicators phản ứng ở timing khác nhau.

**Leading indicators / 선행지표** có thể đổi trước realized activity: orders, surveys, semiconductor prices.

**Coincident indicators / 동행지표** đi cùng activity: industrial production/sales.

**Lagging indicators / 후행지표** phản ánh sau: some employment/credit losses.

Company earnings có thể lead official GDP, nên không mâu thuẫn nếu stock/industry cycle phục hồi trước macro headline.

## Inventory cycle: một small change trong final demand có thể tạo large production swing

Nếu retailers thấy demand giảm, họ vừa order ít hơn vừa destock. Supplier nhận demand shock lớn hơn consumer-sales change.

Đây là **inventory accelerator / 재고순환** và liên quan bullwhip effect.

Manufacturing Korea nhạy với inventory cycles vì intermediate-goods exports lớn.

## Structural vs cyclical: câu hỏi quan trọng nhất

Một variable tăng có thể đến từ cycle hoặc structural change.

Ví dụ HBM demand tăng có both:

- cyclical AI investment boom;
- structural shift sang higher-bandwidth memory.

Analyst cần tách hai layers vì valuation và capex decision khác nhau.

Cyclical earnings nên không được extrapolate vô hạn; structural capability cũng không nên bị đánh giá chỉ qua một downcycle.

## Current 2026 snapshot: forecast và policy stance phải ghi date

Bank of Korea Economic Outlook tháng 8/2026 dự báo real GDP growth **3,3% năm 2026** và **2,9% năm 2027**, cùng CPI **2,7% năm 2026**. Semiconductor/AI-related demand là một driver quan trọng. Đây là **forecast tại thời điểm tháng 8/2026**, không phải realized final data.

Đến Monetary Policy Report tháng 9/2026, BOK ghi nhận base rate đã được nâng lên **3,00%**, trong bối cảnh inflation pressure, robust growth và housing/household-loan concerns. Đây là **policy snapshot tháng 9/2026** và có thể thay đổi sau đó.

Hai snapshot minh họa lý do chapter tách current data khỏi structural mental models.

## Macro dashboard cho Korean company analysis

Không cần forecast tất cả. Một dashboard practical có thể gồm:

```text
Growth: real GDP / GDI
Prices: CPI / core CPI
Rates: BOK rate / government yields / credit spreads
FX: KRW/USD
External: exports / current account / semiconductor indicators
Household: housing / debt / confidence
Labor: employment / wage / participation
Industry: orders / inventory / utilization / backlog
```

Sau đó chỉ chọn variables relevant với company.

Airline cần oil/FX/demand. Bank cần rates/credit/housing. Semiconductor needs memory prices/global AI capex. Retail needs real income/household debt.

## Scenario analysis tốt hơn một forecast point

Thay vì nói “KRW sẽ là 1,xxx”, hãy xây scenarios:

```text
Scenario A: global AI capex mạnh + KRW stable
Scenario B: semiconductor downcycle + KRW weak
Scenario C: rates stay high + housing soft
```

Rồi trace company earnings/cash flow.

Scenario thinking tránh false precision và phù hợp với macro uncertainty.

## Mental Model

> Macro là hệ thống **thay đổi boundary conditions** của firms: demand, input prices, funding cost, FX, wages và asset values. Nó không quyết định outcome một mình; company business model quyết định shock được khuếch đại hay hấp thụ.

Một map nén:

```text
Global cycle + Domestic demand
          ↓
Inflation / Rates / FX
          ↓
Household + Corporate balance sheets
          ↓
Industry orders / Costs
          ↓
Company cash flow
```

## Common misconceptions

**“GDP tăng = mọi company tốt.”** Sai. Sector cycles khác nhau.

**“KRW yếu = mọi exporter được lợi.”** Sai. Cost/debt currency matters.

**“Rate cut = bullish.”** Không luôn; reason for cut quan trọng.

**“Current-account surplus luôn tốt.”** Không; weak imports/domestic demand cũng có thể tăng surplus.

**“Low unemployment = no labor problem.”** Sai. Participation, aging và job quality matter.

**“One forecast point là truth.”** Sai. Forecast là conditional estimate và phải ghi date.

## Connections

Đọc tiếp [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md), [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md), [`18_construction_real_estate_and_project_finance.md`](./18_construction_real_estate_and_project_finance.md), [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md), [`27_demographics_households_and_consumption.md`](./27_demographics_households_and_consumption.md) và [`28_productivity_services_and_economic_dualism.md`](./28_productivity_services_and_economic_dualism.md).

### Nguồn nền và current snapshots

- Bank of Korea, Economic Outlook (August 2026): https://www.bok.or.kr/eng/bbs/E0000634/view.do?menuNo=400423&nttId=11064205
- Bank of Korea, Monetary Policy Report (September 2026).
- Bank of Korea research on potential growth, productivity and financial stability.
- Statistics Korea for CPI, labor and household statistics.

Các forecast, rate và current-cycle statements luôn cần re-check khi dùng sau ngày tài liệu được cập nhật; các causal mechanisms trong chapter được viết để dùng lâu dài.
