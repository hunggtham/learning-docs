# Năng lượng, an ninh điện và chuyển đổi carbon tại Hàn Quốc (Energy Security & Transition / 에너지안보·전력시장·탄소전환)

Hàn Quốc là một nền kinh tế industrial, energy-intensive nhưng có ít domestic fossil resources và power grid gần như không kết nối với neighboring countries. Vì vậy energy đồng thời là **import dependency, industrial-cost issue, national-security variable và decarbonization challenge**.

Một semiconductor fab, steel mill hay AI data center không chỉ hỏi “điện bao nhiêu won/kWh?”. Nó còn hỏi grid connection có đủ không, outage risk thế nào, renewable procurement có khả thi không và policy/tariff có ổn định qua project life hay không.

## Energy balance bắt đầu từ imports

Oil, LNG và coal phần lớn phải nhập khẩu. Local KRW cost phụ thuộc both world commodity price và FX:

\[
KRW\ Import\ Cost \approx USD\ Commodity\ Price \times KRW/USD
\]

Nếu oil price không đổi nhưng KRW mất giá 10%, local-currency import cost vẫn tăng gần tương ứng trước hedging/tax adjustments.

Energy shock có thể truyền:

```text
Oil/LNG price ↑ or KRW weakens
          ↓
Import bill ↑
          ↓
Trade/GDI pressure
          ↓
Power/fuel/transport cost ↑
          ↓
Company margins + household real income ↓
          ↓
Inflation / policy response
```

Do đó energy và macro/FX không thể đọc tách nhau.

## Energy security không đồng nghĩa self-sufficiency 100%

Một resource-poor economy khó tự sản xuất toàn bộ oil/gas/minerals.

**Energy Security / 에너지안보** tốt hơn nên hiểu là ability duy trì supply với acceptable cost trong shocks.

Tools gồm:

- diversified suppliers;
- long-term contracts;
- strategic reserves;
- nuclear/renewable domestic generation;
- grid resilience;
- demand response;
- storage;
- efficient consumption.

Absolute self-sufficiency có thể quá đắt; resilience is portfolio design.

## Electricity khác oil: balance phải xảy ra gần real time

Oil can be stored relatively easily. Electricity storage at national scale is harder/costlier.

Power system must continuously balance:

\[
Generation = Demand + Losses
\]

If supply insufficient, frequency/voltage stability deteriorates and outages can occur.

Therefore system needs **reserve margin / 예비율** and dispatchable/flexible resources.

## Reliability has economic value beyond tariff

For ordinary household, short outage is inconvenience.

For semiconductor fab, outage/voltage disturbance can ruin wafer batches and disrupt clean processes. Loss can exceed electricity bill by orders of magnitude.

Thus industrial power competitiveness is:

```text
Price + Reliability + Connection speed + Power quality
```

not price alone.

## Korean power-market architecture

KEPCO / 한국전력공사 remains central in transmission/distribution and retail structure, while generation includes public subsidiaries and independent producers.

Wholesale power is settled through market mechanisms, while retail tariff is administratively structured rather than purely real-time market price.

This creates possible gap between **wholesale generation cost** and **retail tariff**.

If fuel costs spike faster than tariff adjustments, economic cost does not disappear; it accumulates in utility financials or future tariff burden.

Xem [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md).

## SMP: marginal cost concept

Korean wholesale market uses **System Marginal Price (SMP / 계통한계가격)** concepts.

Simplified merit-order logic:

```text
Low marginal-cost plants dispatched first
        ↓
Higher-cost plants added as demand rises
        ↓
Marginal accepted plant helps set settlement price
```

Exact settlement has market-specific rules, but mental model useful: gas/fuel price can influence wholesale power price even if nuclear/renewables have lower fuel cost.

Therefore generation mix and marginal plant matter.

## Retail tariff is policy as well as price

Electricity tariff influences households, inflation and industrial competitiveness.

If tariff fully follows volatile fuel cost immediately, households/firms face high volatility. If tariff adjustment is delayed, KEPCO/sector balance sheet absorbs loss temporarily.

So policy chooses **who bears cost and when**, not whether physical fuel cost exists.

This is classic public-enterprise trade-off.

## Nuclear economics: high upfront capital, low fuel sensitivity

Nuclear plants require enormous construction capital and long lead times, but fuel cost share is relatively low and output is stable.

Full lifecycle economics include:

```text
Construction
Financing during construction
Operations / maintenance
Fuel
Safety upgrades
Decommissioning
Waste management
```

Comparing only fuel cost understates capital/long-duration risk.

Korea has deep nuclear engineering/manufacturing capability, making nuclear not only domestic energy source but industrial/export ecosystem.

## Construction delay risk in nuclear

Because projects take years, financing cost compounds.

If initial capital `I` accrues financing cost `r` for years before operation, delay raises effective project cost materially.

This is **interest during construction**.

Therefore schedule execution is a major economic variable, not merely project-management detail.

## LNG: flexibility in exchange for import-price exposure

Gas plants can ramp more flexibly than nuclear/coal and help balance variable renewables.

But Korea imports LNG, exposing system to:

- global LNG prices;
- shipping;
- FX;
- contract structure.

LNG can have high **system value** as flexible capacity even if energy-only cost is not lowest.

This distinction matters in power economics: cheapest average kWh is not always most valuable plant for reliability.

## Coal: legacy asset and transition pressure

Coal historically provided large stable generation but has high carbon emissions and pollution externalities.

As Korea reduces coal, remaining plants face utilization decline and potential stranded-asset economics.

Transition must manage both emission goals and capacity adequacy.

## Renewable power: zero fuel cost does not equal zero system cost

Solar/wind require no fuel once built, but output is variable.

As share rises, system needs:

- transmission;
- storage;
- flexible generation;
- forecasting;
- demand response;
- curtailment management.

Thus renewable LCOE alone cannot describe full system economics.

Korea additionally faces high population density, limited land, mountainous geography and grid constraints.

## Offshore wind: resource potential nhưng execution heavy

Offshore wind offers larger-scale renewable potential but needs:

- seabed/site rights;
- permitting;
- turbines/foundations;
- subsea cable;
- port/vessels;
- grid connection;
- local acceptance.

It resembles infrastructure/shipbuilding project as much as simple power plant.

Korean heavy-industry capability may create supply-chain opportunity, but project economics still depend on financing and execution.

## Capacity adequacy: energy and capacity are different

A solar plant may generate many MWh annually but not necessarily during peak evening winter demand.

Power system must have enough **firm/available capacity** when needed.

Therefore planning asks both:

```text
How much energy over year?
How much dependable capacity at peak?
```

This is why storage, nuclear, gas and demand response can have value beyond annual generation share.

## Grid bottleneck: generation without transmission is stranded supply

A project can have permits/finance but fail to produce economic value if grid connection delayed.

Transmission construction often takes years and faces siting/community issues.

For industrial clusters, same problem appears on demand side: factory announced capacity is not fully executable unless sufficient power/water connection secured.

Grid queue becomes a real economic constraint.

## Semiconductor and AI load growth

Semiconductor fabs require high-quality continuous electricity. AI data centers add large, concentrated loads with high power density.

Therefore Korea’s digital/AI strategy connects directly to grid planning.

A region that lacks power infrastructure cannot simply attract unlimited data centers/fabs through tax incentives.

Xem [`14_semiconductors_electronics_display.md`](./14_semiconductors_electronics_display.md) và [`34_digital_fintech_cloud_and_it_services.md`](./34_digital_fintech_cloud_and_it_services.md).

## Industrial electricity and cost sensitivity

If electricity is 5% of total production cost, 20% tariff rise increases total cost roughly 1 percentage point before efficiency/pass-through effects.

For thin-margin commodity industries, that can materially affect EBIT.

Power intensity differs greatly:

- data center: continuous electrical load;
- electric furnace: highly power-intensive;
- semiconductor: power + reliability + water;
- chemical: energy/feedstock complexity.

Therefore same tariff change produces different company impact.

## Corporate renewable procurement and RE100

Global customers/investors may require suppliers to use renewable electricity.

Korean exporters can use mechanisms such as PPAs, green premiums/certificates depending rules.

Availability/cost of clean power therefore affects export competitiveness even before carbon tax directly applies.

This creates a link:

```text
Customer ESG requirement
→ renewable procurement need
→ energy sourcing cost/site choice
→ export contract competitiveness
```

## Carbon pricing: K-ETS turns emissions into financial cost

Korean Emissions Trading Scheme / 배출권거래제 places carbon cost on covered emitters.

Simplified:

\[
Carbon\ Cost = Net\ Emissions\ Subject\ to\ Purchase \times Allowance\ Price
\]

Steel, chemicals, cement and power are especially exposed.

Free allocation can reduce near-term burden but does not remove long-term decarbonization pressure.

Carbon pricing changes marginal economics of process choices.

## Carbon border measures: domestic emissions become export variable

If export destination charges embodied carbon or requires reporting, Korean industrial emissions affect market access/pricing abroad.

Therefore carbon transition is no longer only domestic environmental policy.

Exporter must manage product carbon intensity, traceability and customer requirements.

## Steel/chemicals: hard-to-abate sectors

Electrifying passenger vehicles is easier than fully decarbonizing blast furnaces or petrochemical feedstock.

Options include:

- hydrogen-based processes;
- electric furnaces;
- recycled inputs;
- CCUS;
- low-carbon feedstocks;
- clean electricity.

Many options require huge new capex and infrastructure.

Thus transition economics involves **technology uncertainty + carbon-policy uncertainty + customer willingness to pay**.

## Hydrogen: carrier, not free primary energy

Hydrogen must be produced using energy.

Economics depends:

```text
Production route
Electricity/gas cost
Carbon intensity
Storage
Transport
Conversion losses
End-use value
```

Hydrogen only makes sense where full-chain benefit beats alternatives.

“Hydrogen economy” should never be assessed from production cost alone.

## Ammonia as transport/storage vector

Ammonia can carry hydrogen more easily in some contexts but requires synthesis and potentially cracking back to hydrogen.

Every conversion loses energy and adds capex.

Therefore carrier choice is systems-engineering problem.

## ESS: value is more than buy-low sell-high

Battery Energy Storage System can provide:

- energy arbitrage;
- frequency response;
- reserve;
- renewable smoothing;
- congestion relief.

Economic value depends market design: can storage be paid for these services?

Korea’s battery manufacturing capability creates industrial-policy link, but grid economics and battery manufacturing economics remain distinct.

## Demand response: sometimes cheapest capacity is “not consuming now”

Industrial/commercial users can shift flexible demand away from peak if compensated.

**Demand Response / 수요반응** reduces need for peaking capacity and grid stress.

For factories with inflexible continuous processes, ability is limited; data centers with backup/storage may have different flexibility.

## Energy efficiency: virtual supply

Saving 1 MWh can be economically similar to generating 1 MWh, if efficiency investment costs less.

Efficiency reduces import exposure and grid load simultaneously.

In mature industrial economy, process optimization/building efficiency can be lower-cost than adding generation for every demand increase.

## Energy transition creates capital-allocation problem

Utilities and industrial firms must decide between maintaining old assets and investing new technology before demand/policy fully certain.

This creates risk of:

- underinvestment → reliability shortages;
- overinvestment → stranded/low-utilization assets.

Portfolio approach is necessary.

## 11th Basic Electricity Plan: plan vs realized outcome

Korea’s 11th Basic Electricity Supply and Demand Plan points toward larger roles for nuclear and renewables, coal decline and continuing balancing role for LNG through planning horizon.

A plan is **policy trajectory**, not guaranteed physical outcome.

Realization depends on permits, construction, grid, demand and costs.

Analyst should treat plan as scenario baseline, then track actual project execution.

## Nuclear export as industrial business

Korean nuclear capability includes engineering, EPC, components, operations and lifecycle services.

Export projects combine industrial economics with government diplomacy, sovereign credit and long construction cycle.

Thus nuclear export resembles heavy infrastructure/defense business as much as commodity energy.

## How to analyze KEPCO/power-sector economics

Monitor:

```text
Fuel purchase cost
Wholesale power cost
Retail tariff adjustments
Generation mix
FX
Interest expense/debt
Grid capex
Demand growth
```

Profitability can improve because fuel cost falls even without tariff hike, or worsen because tariff lags input cost.

## How to analyze power-intensive manufacturer

Ask:

1. Electricity share of cost?
2. Tariff category?
3. Load profile?
4. Reliability sensitivity?
5. Renewable procurement obligation?
6. Power-price pass-through to customers?
7. Site has secured grid capacity?

A 10% tariff move can be trivial for software company but thesis-changing for electrochemical process.

## Stress tests

Useful scenarios:

- LNG +30% and KRW -10%;
- industrial tariff +15%;
- grid connection delayed 2 years;
- carbon allowance price doubles;
- new nuclear/wind project delay;
- AI/data-center load grows faster than grid.

Trace impact into company cash flow and public utility balance sheets.

## Mental Model

> Korea must optimize four objectives simultaneously: **security, affordability, reliability and decarbonization**. No single technology maximizes all four; energy strategy is a portfolio and system-integration problem.

A compact map:

```text
Imported fuels + Domestic generation
              ↓
Wholesale power / Grid
              ↓
Retail tariff + Reliability
              ↓
Households / Industry
              ↓
Inflation + Competitiveness + Investment
```

## Common misconceptions

**“Renewables have zero fuel cost, so system cost is near zero.”** Sai. Grid/storage/balancing/capex matter.

**“Nuclear has low fuel cost, so project risk is low.”** Sai. Construction/financing/schedule matter.

**“Low tariff means cheap generation.”** Not necessarily; cost may sit in utility balance sheet.

**“Energy independence means self-producing everything.”** Diversification/resilience matter more.

**“More generation automatically solves industrial power shortage.”** Not if transmission/grid connection constrained.

**“Hydrogen is an energy source.”** More accurately it is an energy carrier produced using other energy.

## Connections

Đọc cùng [`01_macro_economy_and_business_cycle.md`](./01_macro_economy_and_business_cycle.md), [`14_semiconductors_electronics_display.md`](./14_semiconductors_electronics_display.md), [`16_shipbuilding_steel_chemicals_heavy_industry.md`](./16_shipbuilding_steel_chemicals_heavy_industry.md), [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md), [`25_public_enterprises_and_state_owned_companies.md`](./25_public_enterprises_and_state_owned_companies.md), [`32_defense_aerospace_and_strategic_industries.md`](./32_defense_aerospace_and_strategic_industries.md) và [`34_digital_fintech_cloud_and_it_services.md`](./34_digital_fintech_cloud_and_it_services.md).

### Nguồn nền

- International Energy Agency, *Korea 2025*: https://www.iea.org/reports/korea-2025
- IEA, Korea 11th Basic Electricity Supply and Demand Plan: https://www.iea.org/policies/28827-11th-basic-electricity-supply-and-demand-plan
- Korean power/energy authorities and KEPCO disclosures for current tariff/market data.

Energy mix, tariff and plan numbers change over time; re-check official current data before investment/legal decisions.
