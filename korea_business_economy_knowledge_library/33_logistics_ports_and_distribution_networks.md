# Logistics, cảng biển và mạng phân phối Hàn Quốc (Logistics, Ports & Distribution / 물류·항만·유통망)

Một nền kinh tế export-oriented không thể tồn tại chỉ với factories. Raw materials phải vào Korea, components phải di chuyển giữa plants, finished goods phải ra ports/airports, và parcels phải tới household. **Logistics / 물류** là connective tissue nối manufacturing với market.

Điểm quan trọng nhất: logistics không tối ưu “shipping cost thấp nhất”. Nó tối ưu **total landed cost + time + reliability + working capital + service level**.

## Logistics là physical flow + information flow

A complete logistics system includes:

- transport;
- warehousing;
- inventory;
- customs;
- order processing;
- routing;
- tracking;
- returns.

Physical flow without information flow creates uncertainty; uncertainty forces higher safety stock.

A useful total-cost mental model:

\[
Total\ Logistics\ Cost = Transport + Warehousing + Inventory\ Carrying + Handling + Stockout + Delay\ Cost
\]

Sea freight may be cheaper than air, but if lead time adds 30 days of inventory or causes production delay, total cost can be higher.

## Korea geography: peninsula but trade is overwhelmingly sea/air dependent

Because overland connection through the peninsula is constrained, ports and airports are strategically important.

Different logistics nodes specialize:

- Busan: container hub/transshipment;
- Incheon: capital-region cargo + air/sea connectivity;
- Ulsan/Gwangyang/Pohang: industrial/bulk cargo;
- Incheon Airport: high-value time-sensitive air cargo.

Port geography reflects industrial geography.

Steel, petrochemicals, autos, containers and semiconductors require different infrastructure.

## Containerization: standardized interface of physical trade

Standard container transformed global logistics by reducing handling time, damage and intermodal friction.

Container acts like an **API standard for physical goods**: ship, truck, rail and crane can interact with same standardized unit.

This dramatically lowered transaction cost and enabled complex global value chains.

## Port economics: throughput, network and fixed infrastructure

Port/terminal has large fixed assets: berths, cranes, yards, IT systems and dredging/infrastructure.

Revenue often relates to throughput and services.

Scale matters because fixed assets spread across more containers/cargo.

But congestion can create diseconomies: waiting time rises, yard fills, truck turnaround slows.

Therefore port efficiency is not just maximum volume; it is high volume with reliable flow.

## Busan and transshipment network effects

A transshipment hub handles cargo that may not originate/end locally; containers transfer between services.

Network effect:

```text
More shipping routes
→ More connection options
→ More transshipment cargo
→ More reason for carriers to call
→ Higher route frequency
```

But hub status is contestable. Carriers compare cost, productivity, schedule reliability and regional alternatives.

Port automation, labor relations and hinterland connection therefore matter.

## Port operator vs shipping carrier: same containers, different economics

A port terminal earns handling/terminal fees and depends on throughput/utilization.

A container shipping carrier owns/charters vessels and faces freight-rate/bunker/vessel-supply cycles.

Same trade volume can produce very different earnings volatility.

Do not analyze “shipping/logistics” as one industry.

# Container shipping / 해운

## Freight rate is determined by demand against slow-moving vessel supply

Short-term vessel supply is relatively inelastic because building new ships takes years.

When trade demand suddenly rises or capacity is disrupted, freight rates can spike.

High rates then induce new ship orders. Years later many ships deliver, supply increases and rates can fall even if global trade still grows.

This creates long lag:

```text
Freight rate ↑
→ Carrier profit ↑
→ New ship orders ↑
→ 2–3+ year lag
→ Fleet supply ↑
→ Rate pressure
```

This connects shipping with shipbuilding cycle but with time shift.

## Operating leverage and charter exposure

Carrier economics depend whether vessel is owned or chartered.

Charter contracts lock cost for period; spot/contract freight revenue can move differently.

A carrier that locked expensive charters at cycle peak can suffer even after freight rates fall.

Thus fleet ownership/charter maturity structure matters.

## Bunker fuel

Fuel is major variable cost.

Profit depends on:

```text
Freight rate
- bunker fuel
- charter/depreciation
- port/canal cost
- operating overhead
```

Carrier may use bunker surcharge or hedging, but pass-through timing varies.

## Slow steaming: fuel vs capacity/time trade-off

Ships can reduce speed to save fuel.

But slower voyage means vessel is tied up longer, reducing effective fleet capacity.

Thus operational decision affects both cost and supply.

Environmental regulation can make slow steaming economically attractive.

## Shipping as strategic infrastructure

A large national carrier can have strategic relevance because exporter access to container capacity matters during disruption.

This explains why shipping can receive policy attention beyond its direct GDP share.

But strategic value does not erase brutal freight-rate cyclicality.

# Freight forwarder and 3PL / 포워더·3PL

## Freight forwarder sells coordination rather than vessels

Forwarder books capacity, handles documents, customs and routing without necessarily owning ships/aircraft.

This can be asset-light, but margin depends on procurement scale, customer relation and rate volatility.

When carrier spot rates rise faster than forwarder can reprice customer contract, margin compresses.

## 3PL combines coordination and physical assets

**Third-party logistics / 제3자물류** may operate warehouses/trucks/fulfillment plus information systems.

Economics depend on:

- warehouse utilization;
- labor productivity;
- route density;
- contract duration;
- customer concentration.

Low margin can still produce good ROIC if asset turnover high.

# Inventory and working capital

## Inventory is cash in physical form

Inventory consumes capital.

**DIO (Days Inventory Outstanding)**:

\[
DIO = \frac{Average\ Inventory}{COGS}\times365
\]

If shipping disruption forces firm to hold 30 extra days of components, cash conversion cycle increases.

This is the financial cost of resilience.

Xem [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md).

## Safety stock is insurance

Inventory buffer seems inefficient until stockout would stop whole factory.

Optimal inventory compares:

```text
Carrying cost of extra stock
vs
Expected stockout/disruption loss
```

A $2 component can justify large safety stock if its absence stops a $100m line.

Inventory importance is not proportional to unit purchase price.

## Just-in-time vs just-in-case

**JIT** minimizes inventory under predictable supply.

**Just-in-case** adds buffer for critical nodes.

Post-pandemic supply-chain design often uses segmentation:

- commodity/easy substitute → lean inventory;
- critical/long lead → larger buffer or dual source.

One inventory philosophy for all items is suboptimal.

# Customs and trade operations

## Customs is operational capability

Cross-border shipment requires:

- HS classification;
- customs valuation;
- origin documentation;
- permits;
- duties/taxes;
- security rules.

Error can delay cargo or trigger penalties.

For FTA, correct rules-of-origin documentation determines tariff benefit.

Therefore customs competence can create real cost advantage.

## Bonded logistics

Bonded warehouse allows goods stored/processed under customs control before duties are finalized/paid depending structure.

Useful for transshipment, re-export and inventory hubs.

This reduces cash/tax friction in global networks.

## Incoterms: allocation of delivery cost/risk

FOB, CIF, DDP and other **Incoterms** specify delivery responsibilities/risk/cost allocation.

They do not alone determine ownership/payment terms.

Exporter freight exposure must be read with Incoterm.

Two companies selling same FOB/CIF revenue may carry different logistics risk.

# Air cargo / 항공화물

## High-value, low-weight products justify air freight

Semiconductors, electronics, pharmaceuticals and urgent parts can have high time value.

Air freight is expensive per kg but minimizes lead time/inventory and disruption cost.

Incheon Airport therefore functions as infrastructure for advanced manufacturing, not just passenger travel.

## Yield and capacity

Air cargo rates depend on dedicated freighter capacity plus belly cargo on passenger flights.

Passenger travel disruption can reduce belly capacity, making cargo rates spike.

Thus passenger aviation and cargo markets interact.

# Cold chain / 콜드체인

Biopharma, vaccines, food and some chemicals require controlled temperature/humidity.

A shipment arriving on time but outside temperature range may be worthless.

Cold-chain economics include:

- specialized containers;
- sensors;
- qualification;
- monitoring;
- backup procedures.

Compliance capability creates entry barrier.

Xem [`31_biohealth_pharma_medical_devices_and_kbeauty.md`](./31_biohealth_pharma_medical_devices_and_kbeauty.md).

# E-commerce fulfillment and last mile

## Front-end digital, back-end physical

E-commerce may look like software but fulfillment requires warehouses, labor, vehicles and inventory coordination.

Business can be asset-heavy even if order interface is digital.

## Density economics

Last-mile cost/order falls when route density rises:

\[
Delivery\ Cost\ per\ Order \downarrow \quad as \quad Stops/Route\ Density \uparrow
\]

Korea’s dense urban/apartment geography can make delivery economics attractive because driver can deliver many parcels per building/area.

This is geographic advantage combined with routing software.

## Fulfillment-center economics

Warehouse has fixed capex and labor/automation cost.

Return depends on throughput/utilization.

Peak season requires spare capacity; off-season lower utilization.

Automation is rational when labor saving + throughput + accuracy benefit exceed depreciation/maintenance.

## WMS/TMS and software

**WMS (Warehouse Management System)** controls inventory/location/picking.

**TMS (Transportation Management System)** helps planning/routes/carrier allocation.

Routing, forecasting and slotting connect logistics to operations research/graph algorithms.

Bad software forecast creates physical consequences: overstock, stockout or empty truck miles.

## Reverse logistics

Returns create reverse flow:

```text
Customer pickup
→ transport
→ inspection
→ restock/refurbish/disposal
→ refund
```

Fashion/e-commerce return rate can be high enough to erase front-end margin.

GMV growth with worsening returns may be low-quality growth.

# Supply-chain visibility and observability

Tracking does not prevent disruption but reduces uncertainty/reaction time.

Software analogy:

> Supply chain without visibility resembles distributed system without observability: failure occurs, but team cannot identify broken node quickly.

Visibility can reduce safety-stock uncertainty and improve customer communication.

## Control tower and event-driven logistics

Modern logistics systems combine shipment events, inventory, weather/port status and orders to re-route or reprioritize.

Economic benefit is not dashboard itself; it is avoided stockout/delay and lower buffer.

# Logistics and industrial clusters

Port/airport/warehouse proximity influences location economics.

Heavy bulk cargo benefits port adjacency. Semiconductor high-value cargo values airport and supplier speed. E-commerce fulfillment values household density/highway access.

Therefore “best logistics location” depends product physics.

Xem [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md).

# Resilience and multi-sourcing

Dual sourcing reduces single-point failure but can sacrifice volume discount/quality learning.

Resilience strategy should segment components by:

- criticality;
- substitutability;
- lead time;
- geopolitical exposure.

Not every screw requires second supplier; some critical chips do.

# Shipping-rate impact on exporter depends contract

Freight rate rise affects company differently depending:

- Incoterm;
- long-term carrier contract;
- product margin;
- pricing power;
- transport mode.

Therefore shipping index should not be mechanically plugged into every exporter margin.

# How to analyze a logistics company

## Container carrier

```text
Freight rates
Volume
Fleet capacity
Orderbook/new vessel deliveries
Bunker fuel
Owned vs chartered fleet
Contract vs spot revenue
Net debt
```

## Port/terminal

```text
Throughput
Transshipment share
Utilization
Fee structure
Capex
Productivity/turnaround time
```

## 3PL/fulfillment

```text
Customer concentration
Warehouse utilization
Route density
Labor cost
Automation capex
Contract margin
```

## E-commerce logistics

```text
Orders/day
Delivery cost/order
Fulfillment utilization
Return rate
Membership/subsidy
Geographic density
```

# Stress tests

- freight rate -40% after new vessels deliver;
- bunker fuel +30%;
- port congestion;
- critical route closure;
- lead time +20 days;
- fulfillment order density -15%;
- return rate +5pt.

Always connect operational shock to working capital and cash.

# Mental Model

> Logistics optimizes **time + reliability + inventory + transport + information**. Cheapest freight is not necessarily cheapest supply chain.

A compact loop:

```text
Demand forecast
   ↓
Inventory position
   ↓
Transport / Warehouse decision
   ↓
Lead time / Service level
   ↓
Cash conversion + Customer experience
```

# Common misconceptions

**“Inventory thấp luôn tốt.”** Sai. Stockout/disruption cost can exceed carrying cost.

**“Port lớn vì domestic economy lớn.”** Transshipment/network position matter.

**“Fast delivery is free digital feature.”** It requires density, labor, warehouse and transport capital.

**“Shipping rates rise → every exporter margin falls.”** Contract/Incoterm/pricing power differ.

**“Automation always lowers logistics cost.”** Only if throughput/utilization justifies fixed investment.

**“Visibility prevents supply shock.”** It improves response; does not eliminate physical constraints.

# Connections

Đọc cùng [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md), [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md), [`16_shipbuilding_steel_chemicals_heavy_industry.md`](./16_shipbuilding_steel_chemicals_heavy_industry.md), [`17_platform_telecom_content_retail_services.md`](./17_platform_telecom_content_retail_services.md), [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md) và [`31_biohealth_pharma_medical_devices_and_kbeauty.md`](./31_biohealth_pharma_medical_devices_and_kbeauty.md).
