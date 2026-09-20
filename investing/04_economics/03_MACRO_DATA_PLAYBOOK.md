# Macro Data Playbook — từ số liệu tới asset reaction

> Macro data chỉ hữu ích khi nó làm thay đổi xác suất về growth, inflation, policy, liquidity hoặc credit. Mục tiêu của chapter này là biến lịch kinh tế từ danh sách headline thành một quy trình: trước release biết market đang kỳ vọng gì, sau release hiểu surprise nằm ở đâu, rồi theo dõi bond/FX/credit để xem market thực sự diễn giải data như thế nào.

## 1. Đừng đọc data bằng headline

Market không phản ứng đơn giản với “CPI cao”, “NFP tốt” hay “GDP mạnh”. Price phản ứng với chênh lệch giữa actual và expectation, revisions, composition, positioning và implication cho future policy.

Framework cơ bản:

`Baseline → Consensus → Market pricing → Actual → Surprise → Composition → Reaction function → Yields/FX/Credit → Equities/Commodities`

Nếu bỏ qua consensus, bạn có thể thấy data mạnh nhưng market rally vì data “ít mạnh hơn priced”. Nếu bỏ qua positioning, bạn có thể thấy bullish data nhưng asset sell off vì investors đã quá long trước release.

## 2. Baseline, consensus và market pricing là ba thứ khác nhau

Baseline là view của chính bạn trước event. Consensus là survey forecast của economists/analysts. Market pricing là expectation embedded trong prices, ví dụ policy futures, yield curve, options implied move hoặc positioning proxies.

Consensus có thể nói central bank sẽ cut 25 bps, nhưng market pricing có thể imply meaningful chance của 50 bps. Khi decision là 25 bps, headline “đúng consensus” vẫn có thể hawkish relative to market pricing.

Do đó trước major event, luôn ghi cả consensus và observable market pricing nếu available.

## 3. Surprise không chỉ là Actual - Forecast

Simple surprise = actual - forecast, nhưng economic interpretation phụ thuộc sign và variable. Higher CPI thường hawkish; higher unemployment thường dovish, nhưng regime matters.

Revisions cũng quan trọng. Payroll headline +200k nhưng prior months revised -120k tạo different message so clean +200k. Retail sales beat với prior month sharply revised lower cũng có weaker underlying path.

Một release phải được đọc như time series, không phải isolated number.

## 4. CPI: headline, core và composition

Consumer Price Index (*CPI*) đo price changes của consumption basket theo methodology. Headline gồm food/energy; core thường exclude them vì volatility cao. Nhưng “core” không đồng nghĩa underlying inflation hoàn hảo.

Investor nên tách goods, shelter/housing-related components và services. Goods inflation chịu supply chains, commodity/input prices và inventory cycles. Shelter có measurement lag. Services inflation thường liên quan wages, demand và labor intensity hơn.

YoY rate dễ bị *base effects*. Vì vậy cần nhìn MoM và annualized short-run trends:

`3-month annualized ≈ (1 + cumulative 3m change)^4 - 1`

`6-month annualized ≈ (1 + cumulative 6m change)^2 - 1`

Short-run annualization noisy nhưng hữu ích để phát hiện momentum turning trước YoY.

## 5. Shelter lag và “supercore” caveat

Official rent/shelter measures thường adjust chậm hơn new-market rents. Khi market rents đã cool, shelter CPI có thể còn sticky. Ngược lại new rents turn up có thể chưa xuất hiện ngay trong official data.

Analysts đôi khi nhìn services ex housing hay “supercore” để đánh giá underlying pressure. Không có một measure thần kỳ. Central bank reaction function có thể thay đổi trọng tâm tùy period, nên investor phải biết policymakers đang nhấn metric nào và vì sao.

## 6. PCE inflation

Personal Consumption Expenditures price index (*PCE*) có weights/methodology khác CPI và thường là important reference cho Fed-style analysis. Core PCE loại food/energy nhưng vẫn cần đọc composition.

PCE release đôi khi chứa information partly inferable từ prior CPI/PPI data, nên market surprise có thể nhỏ hơn headline change. Một event calendar không nên assume mọi release có equal information content.

## 7. PPI, import prices và inflation pipeline

Producer Price Index (*PPI*) đo price pressures ở production stages. Import/export prices cho cross-border price dynamics. Những indicators này có thể giúp infer pipeline pressure nhưng pass-through tới consumer prices không one-to-one.

Company margins matter: higher input costs có thể được absorbed, passed to consumers hoặc offset by productivity. Vì vậy PPI up không mechanical imply CPI up cùng magnitude.

## 8. Inflation expectations

Survey expectations và market breakevens cung cấp different views. Short-term expectations có thể nhạy gasoline/food prices; long-term expectations quan trọng với wage/price setting và central-bank credibility.

Breakeven inflation = nominal yield - inflation-linked real yield là useful market measure nhưng chứa inflation risk premium và liquidity effects. Đừng gọi nó “market forecast” theo nghĩa pure expectation.

## 9. Payrolls: establishment và household perspectives

US-style payroll report có establishment survey và household survey với methodologies khác. Headline nonfarm payrolls đến từ establishment side; unemployment rate thường từ household survey.

Divergence có thể kéo dài. Investor không nên cherry-pick survey phù hợp thesis mà cần hiểu sample, revisions và trend.

## 10. Unemployment rate, participation và underemployment

Unemployment rate có thể tăng vì layoffs hoặc vì labor-force participation tăng nhanh hơn employment. Hai cases có different interpretation.

Participation rate cho biết share population tham gia labor force. Broader underemployment measures có thể capture part-time-for-economic-reasons và marginal attachment. Labor market health là multi-dimensional, không phải một unemployment number.

## 11. Wages, productivity và unit labor costs

Average hourly earnings cho wage trend nhưng mix effects có thể distort. Employment Cost Index hoặc other compensation measures có different strengths.

Wages tăng không automatically inflationary nếu productivity tăng tương ứng. *Unit Labor Cost* gần với compensation growth trừ productivity growth. Nếu wages +5% nhưng productivity +3%, unit labor pressure khác wages +5% với zero productivity.

Đây là cầu nối giữa labor data và sustainable services inflation.

## 12. Jobless claims

Initial claims là high-frequency indicator của new unemployment-insurance filings; continuing claims cho persistence. Weekly data noisy và seasonal adjustment quan trọng, nên nhìn moving trend hơn một print.

Claims thường turn nhanh hơn unemployment rate nhưng không capture toàn labor market. Chúng hữu ích cho inflection monitoring.

## 13. JOLTS: openings, hires và quits

Job Openings and Labor Turnover Survey (*JOLTS*) cung cấp vacancies, hires, quits và layoffs. Openings-to-unemployed ratio cho labor demand relative to supply; quits có thể proxy worker confidence/wage bargaining.

Openings data noisy và revisions lớn, nên direction qua nhiều months quan trọng hơn one print.

## 14. PMI/ISM: diffusion indices

Purchasing Managers' Index (*PMI*) là diffusion index. Level >50 thường expansion relative to prior period; <50 contraction, nhưng tốc độ và components matter.

New orders thường forward-looking hơn headline. Production/output cho current activity. Employment cho labor demand. Prices paid cho cost pressure. Supplier deliveries phải đọc cẩn thận: slower deliveries có thể signal strong demand hoặc supply disruption.

Manufacturing PMI đặc biệt relevant cho export/manufacturing economies như Korea; services measures quan trọng hơn với consumption-heavy economies.

## 15. New orders vs inventories

New orders rising while inventories low có thể signal future production recovery. Inventories high while new orders fall có thể signal destocking pressure.

Đối với semiconductor, manufacturing và shipping cycles, orders/inventory relationship thường informative hơn headline PMI alone.

## 16. Retail sales và consumption

Retail sales là high-frequency nominal spending measure. Inflation có thể làm nominal sales tăng dù real volume flat/down. Composition cũng quan trọng: autos/gasoline volatile; some control-group concepts better map into GDP consumption estimates.

Consumption sustainability nên đọc cùng real disposable income, savings rate, household balance sheets, credit-card growth và delinquencies.

## 17. Personal income, savings và credit

Household spending có thể tăng nhờ wage income, fiscal transfers, asset wealth hoặc borrowing. Spending funded by real-income growth bền hơn spending dựa vào rapidly rising debt, all else equal.

Savings rate thấp không automatically bearish; context matters. But persistent consumption above income financed by credit can increase future sensitivity to rates/job losses.

## 18. Housing data

Housing là rate-sensitive sector. Useful indicators gồm building permits, housing starts, new/existing home sales, inventories, house prices, mortgage rates và affordability.

Permits often lead construction; starts are physical activity; completions influence supply. Existing-home turnover affects brokers/furnishings differently from new construction.

Housing also transmits monetary policy through mortgages, collateral and household wealth.

## 19. GDP: đừng chỉ nhìn headline annualized growth

GDP identity:

`GDP = C + I + G + (X - M)`

Headline growth cần phân rã consumption, fixed investment, inventories, government và net exports. Inventory build can boost GDP even if final demand weaker. Imports subtract mechanically in identity but strong imports may reflect strong domestic demand, nên không đơn giản “imports xấu”.

Real Final Sales hoặc domestic final demand measures giúp tách inventory/noisy trade effects.

## 20. GDP, GDI và revisions

Gross Domestic Income (*GDI*) theoretically measures same economy from income side nhưng diverges due measurement. Looking at average/trend can add signal.

GDP undergoes multiple revisions. Market may react more to current high-frequency indicators than stale GDP if quarter already passed. Data hierarchy depends timing.

## 21. Central-bank meeting: đọc nhiều layer

Một policy event gồm decision, statement, economic projections, rate-path/dot-like guidance if applicable, vote split và press conference. One-line “hike/cut/hold” is insufficient.

Decision can be hawkish cut or dovish hike depending guidance. Central bank may cut because inflation normalized (supportive) or because crisis risk surged (negative macro signal).

Read reaction function: policymakers đang overweight inflation, labor, growth, FX hay financial stability? What data would make them change path?

## 22. Policy path vs current policy rate

Assets discount future rates, not just today's policy rate. A hold with expectation of three future hikes can tighten financial conditions more than one hike accompanied by clear end-of-cycle guidance.

Front-end futures/OIS and 2Y yields often reveal path repricing. Investor should compare post-event path with pre-event pricing.

## 23. Nominal yields, real yields và breakevens

Nominal yields can move because expected policy, expected inflation, real growth or term premium changes. Inflation-linked bonds help separate real yield/breakeven components, though not perfectly.

Equity valuation tends to be more sensitive when real yields move. Commodity/gold reaction may differ when nominal yield rise is mostly inflation compensation vs mostly real yield.

## 24. 2Y, 10Y và yield curve

2Y yield is highly sensitive to expected near-term policy. 10Y embeds longer growth/inflation and term premium. Curve spreads such as 2s10s help track cycle expectations but must be combined with absolute yield moves.

CPI hot causing 2Y +15 bps and 10Y +5 bps is different from fiscal supply shock causing 10Y +20 bps and 2Y little changed. Both raise yields, but source/risk transmission differ.

## 25. Term premium

Long yield is not simply average expected policy rates. *Term premium* compensates investors for uncertainty of holding duration. Fiscal issuance, inflation uncertainty, central-bank balance sheet and demand from pensions/foreign reserves can influence it.

A long-end selloff driven by term premium can pressure equities/mortgages even without hawkish central-bank repricing.

## 26. Credit spreads

Investment-grade and high-yield spreads reveal compensation for credit/liquidity risk. Spread widening alongside falling government yields can signal growth/credit deterioration.

High-yield spreads, default expectations and refinancing calendars are useful because monetary tightening often hits weak balance sheets with lag.

## 27. Bank lending standards

Bank surveys on lending standards/demand help bridge policy rate and real economy. If banks tighten underwriting and loan demand falls, credit impulse can weaken even before defaults rise.

This is why “central bank stopped hiking” does not immediately mean financial conditions easy; existing tightening continues through refinancing and bank behavior.

## 28. Financial conditions

Financial conditions combine rates, credit spreads, equity prices, FX and sometimes lending measures. Two economies with same policy rate can face different effective conditions depending market moves.

Investor should think transmission, not just policy setting:

`Policy → market rates → credit → FX/equities/property → spending/investment → inflation/growth`

## 29. FX is always relative

Currency pair compares two economies. Strong Korea data may not strengthen KRW if US surprise is even more hawkish for Fed path. Framework:

`Relative rates + relative growth + external balance + carry + positioning/risk flows`

Current account, commodity imports/exports, foreign liabilities and reserve adequacy become more important during stress.

## 30. Carry và funding currencies

Higher-yield currency can attract carry when volatility low, but carry positions may unwind violently during risk-off. Funding currency strength during deleveraging can surprise those who only track rate differentials.

Thus FX analysis needs volatility and positioning alongside macro differentials.

## 31. Oil: supply shock khác demand shock

Oil rising because global demand strong can coincide with cyclicals rally and higher yields. Oil rising because geopolitical supply disruption can raise inflation while lowering expected real growth, creating stagflationary pressure.

Always ask: demand, supply, inventory or risk premium? Same price move, different macro message.

## 32. Metals và industrial commodities

Copper/industrial metals often reflect manufacturing, China demand, inventories and supply constraints. But financial/speculative positioning can move prices too.

Commodity prices are both economic signals and direct input costs; transmission differs by country depending importer/exporter status.

## 33. Gold

Gold has no contractual yield. Important drivers include real yields, USD, central-bank/reserve demand, geopolitical risk and confidence in monetary/fiscal regimes.

“Inflation up = gold up” is not a reliable rule. If inflation surprise causes real yields/USD to rise sharply, gold can fall despite higher CPI.

## 34. Data revisions, seasonality và measurement error

Economic data are estimates, not ground truth measured without error. Seasonal adjustment, benchmark revisions and survey response rates affect interpretation.

A robust investor does not overfit thesis to one month. Look for confirmation across independent series and acknowledge confidence level.

## 35. Base effects

YoY data compares current level with same month last year. If last year's comparison base was unusually high/low, YoY can move sharply without a similar change in current momentum.

Whenever YoY changes dramatically, inspect MoM and recent annualized rates before declaring regime shift.

## 36. Positioning và reflexivity

Price reaction depends on who is already positioned. Bearish news can produce rally if market was even more bearish. A crowded long can sell off on merely “good but not great” data.

Options dealer hedging, CTA/systematic positioning and leveraged carry can amplify moves. You do not need perfect positioning data; simply distinguish fundamental surprise from positioning response.

## 37. Regime matrix

A useful 2×2 starts with growth surprise and inflation surprise. Growth up/inflation down resembles Goldilocks; growth up/inflation up can push yields higher; growth down/inflation down favors easing/long duration; growth down/inflation up is stagflationary.

But credit/liquidity can override the simple matrix. A benign inflation print during banking panic does not erase financial-stability stress.

## 38. Market-reaction map sau release

Immediately after major release, look first at the market closest to the economic variable. For US policy expectations, front-end yields are often informative. Then check long yields, FX, credit and equities.

Example:

`Hot CPI → 2Y ↑ sharply → USD ↑ → real yields ↑ → long-duration equities ↓`

If actual reaction differs, do not force textbook. Investigate composition, pricing, positioning or concurrent news.

## 39. Pre-event template

Before event record: current macro regime, consensus, prior value/revisions, market-implied policy path, key composition expected, major positioning risk and what outcome would invalidate your current view.

Write scenarios rather than single forecast: hot/base/cool CPI; strong/base/weak payrolls; hawkish/base/dovish central-bank communication.

## 40. Post-event template

After release record actual, revision and which subcomponents caused surprise. At 5–15 minutes record 2Y/10Y, FX and relevant commodity. At close record equities by sector and credit. A few days later assess whether move held.

This separates knee-jerk liquidity from durable repricing.

## 41. Weekly macro dashboard

A practical weekly dashboard can include growth momentum, inflation momentum, labor, policy pricing, nominal/real yields, curve, credit spreads, DXY/major FX, oil/gold, financial conditions and positioning notes.

Do not maximize indicators. Use a stable set and ask which changed enough to alter probability distribution.

## 42. Từ data tới investment thesis

Macro data should not directly output “buy/sell ticker”. Final chain is:

`Data → expectations → policy/financial conditions → sector/company cash flows → discount rate → valuation → position size`

The more layers between data and asset, the less deterministic the relationship. This is why disciplined macro analysis uses probabilities and scenarios rather than slogans.