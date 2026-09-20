# Bán dẫn, điện tử và display Hàn Quốc (Semiconductors & Electronics / 반도체·전자·디스플레이)

Semiconductor là một trong những ngành quan trọng nhất để hiểu mô hình kinh tế Hàn Quốc hiện đại vì nó kết hợp gần như tất cả themes của library: **capital intensity, R&D, learning-by-doing, export dependence, chaebol scale, supplier ecosystem, cyclicality và geopolitics**.

Nhưng “semiconductor industry” không phải một business model. Memory, foundry, fabless, equipment, materials, packaging và electronics final products có economics rất khác nhau. Nếu chỉ nhìn headline “chip demand tăng”, rất dễ áp sai logic cho company cụ thể.

## Từ consumer electronics tới semiconductor capability

Korean electronics industry không bắt đầu ở technology frontier.

GoldStar của LG bắt đầu electronics từ cuối 1950s; Samsung Electronics được thành lập năm 1969. Early phase dựa nhiều vào imported components, licensing, assembly và learning từ foreign technology.

Progression có thể hình dung:

```text
Assembly
   ↓
Component localization
   ↓
Process engineering
   ↓
Own product design
   ↓
Core components / semiconductors
   ↓
Frontier R&D + standards + ecosystem
```

Đây là **learning-by-doing / 생산을 통한 학습**. Capability không chỉ đến từ patent; nó tích lũy từ production repetition, defect solving, supplier coordination và equipment know-how.

Semiconductor là bước nhảy khó hơn consumer assembly vì fab cần vốn cực lớn và technology node thay đổi liên tục.

## Semiconductor value chain: ai làm gì?

Một simplified chain:

```text
EDA / IP / Architecture
        ↓
Chip Design (Fabless / IDM)
        ↓
Wafer Fabrication (Foundry / IDM)
        ↓
Assembly / Packaging / Test
        ↓
System / Device
```

Song song là equipment/material ecosystem:

```text
Lithography / Etch / Deposition / Metrology
Wafers / Gases / Photoresist / Chemicals
Substrates / Packaging materials
```

**IDM (Integrated Device Manufacturer / 종합반도체기업)** làm nhiều stages.

**Fabless / 팹리스** focus design.

**Foundry / 파운드리** manufacture designs của customers.

**OSAT** focus assembly/test.

Company analysis phải xác định node trước khi chọn metrics.

## Memory semiconductor: standardized product và supply-demand cycle

**DRAM** và **NAND** là memory categories lớn. Memory thường standardized hơn custom logic, nên industry supply-demand balance có influence mạnh tới ASP.

Một simplified memory cycle:

```text
Demand strong / supply tight
        ↓
ASP + profit ↑
        ↓
Capex ↑
        ↓
Capacity catches up
        ↓
Inventory ↑ / ASP ↓
        ↓
Capex cuts
        ↓
Supply growth slows
        ↓
Recovery
```

Đây là classic capital-intensive commodity-like cycle.

Nhưng “commodity-like” không nghĩa products identical hoàn toàn. Process node, power efficiency, reliability và product mix vẫn tạo differentiation.

## HBM: memory economics trở nên differentiated hơn

**HBM (High Bandwidth Memory / 고대역폭메모리)** stacks multiple DRAM dies để cung cấp bandwidth rất cao cho AI accelerators.

HBM economics khác commodity DRAM vì cần:

- high-quality dies;
- stacking/TSV process;
- advanced packaging integration;
- thermal control;
- customer qualification;
- high yield across multiple stacked layers.

Nếu một stack có nhiều dies, defect ở một layer có thể làm whole stack unusable. Vì vậy yield challenge phức tạp hơn ordinary single-die shipment.

AI boom do đó không chỉ tăng bit demand; nó tăng value của **packaging + yield + qualification capability**.

## Yield: kỹ thuật biến thành gross margin như thế nào?

**Yield / 수율** là tỷ lệ usable dies/process output so với theoretical output.

Giả sử wafer cost gần như fixed. Nếu good dies tăng, unit cost giảm:

\[
Cost\ per\ Good\ Die \approx \frac{Wafer\ Cost + Process\ Cost}{Good\ Dies}
\]

Yield tăng từ 70% lên 90% không chỉ làm shipment tăng; nó spread same fab cost trên nhiều sellable chips.

Vì scale của leading fabs rất lớn, vài percentage points yield có thể có financial effect rất lớn.

Đây là ví dụ rõ nhất của connection giữa engineering và accounting.

## Capital intensity: fab là một fixed-cost machine khổng lồ

Fab cần clean room, lithography, etch/deposition equipment, utilities và engineering staff. Depreciation là cost lớn.

Một approximation:

\[
Unit\ Fixed\ Cost = \frac{Total\ Fixed\ Fab\ Cost}{Good\ Units\ Shipped}
\]

Khi utilization thấp, unit cost tăng. Khi utilization cao, operating leverage mạnh.

Do đó same ASP có thể tạo margin rất khác tùy utilization/yield.

## Capacity lag tạo cycle

Fab không thể tăng capacity trong vài tuần. New fab/build-out, tool installation, process qualification và yield ramp mất thời gian.

Đây là **supply lag**.

Khi demand strong, price tăng trước khi new capacity online. Firms thấy high profit và invest; tới lúc capacity online, demand có thể đã chậm.

Capital intensity + lag là structural source of cyclicality.

## Capex: lớn không đồng nghĩa bullish

Capex có hai meanings:

**Maintenance/technology migration:** cần để giữ competitiveness.

**Growth capex:** tăng future capacity.

Capex lớn có thể signal confidence, nhưng cũng có thể tạo future oversupply.

Value creation phụ thuộc:

\[
Return\ on\ New\ Capacity > Cost\ of\ Capital
\]

Không phải `Capex ↑ = Value ↑`.

## Depreciation timing và profit

New fab capex không hit P&L toàn bộ ngay. Khi asset được placed in service, depreciation bắt đầu qua useful life.

Do đó company có thể có cash outflow trước, rồi depreciation burden tăng khi fab ramp.

Nếu demand yếu đúng lúc new capacity starts depreciating, margin pressure double:

```text
ASP/utilization ↓
+
Depreciation ↑
```

Đây là reason cash flow và P&L timing khác nhau.

## Foundry economics: manufacturing service nhưng moat sâu

Foundry manufacture customer designs. Core variables gồm:

- process node competitiveness;
- yield;
- utilization;
- customer trust;
- design ecosystem;
- packaging;
- time-to-volume.

Customer không chỉ mua transistor density. Họ cần **PDK (Process Design Kit)**, IP libraries, EDA compatibility, reliable yield learning và packaging support.

Switching foundry có cost lớn vì design phải be adapted/qualified. Đây tạo switching cost.

Nhưng node “nhỏ hơn” không tự động better. Cost, power, performance và yield phải match product use case.

## Fabless economics: asset-light hơn nhưng dependency khác

Fabless avoids gigantic fab capex nhưng spends heavily on R&D/design.

Risks gồm:

- foundry capacity access;
- tape-out cost;
- design failure;
- customer concentration;
- fast product obsolescence.

A single design win có thể tạo high margin; missed architecture generation có thể destroy growth.

Do đó R&D execution và ecosystem partnership quan trọng hơn physical utilization.

## Advanced packaging: boundary giữa front-end và back-end mờ đi

Historically packaging/test bị nhìn như lower-value back-end. AI/HBM/chiplets làm packaging trở thành performance bottleneck.

When multiple dies must communicate at high bandwidth, interposer/substrate/thermal design affect system performance.

Điều này làm value shift trong supply chain. Analyst phải update mental model khi technology architecture đổi; historical “low-value node” có thể become strategic node.

## Equipment suppliers: picks-and-shovels nhưng không immune cycle

Semiconductor equipment revenue phụ thuộc fab capex schedule hơn direct chip ASP.

Order timing có thể lead actual chip capacity.

Equipment company economics thường có:

- high R&D;
- qualification barriers;
- installed-base service revenue;
- customer concentration;
- export-control exposure.

“Picks-and-shovels” không nghĩa non-cyclical. If fabs cut capex, new-tool orders can fall sharply.

## Materials/chemicals: recurring demand nhưng qualification moat

Gases, photoresists, wafers và specialty chemicals được consumed continuously.

Compared with equipment, revenue may be more recurring once fab runs. But qualification is strict because tiny impurity can damage yield.

Supplier moat có thể đến từ purity, consistency, logistics and customer qualification—not just patent.

Customer concentration remains risk because a few large fabs account for large demand.

## Inventory: supplier và customer inventory đều matter

Memory price recovery có thể đến từ final demand hoặc temporary restocking.

Analyst should separate:

```text
End demand
Customer inventory
Producer inventory
Channel inventory
```

If customers restock after very low inventory, orders may temporarily exceed end consumption.

Extrapolating restocking as structural demand leads to cycle mistakes.

## Bit growth, ASP và mix

Memory revenue can be decomposed conceptually:

\[
Revenue \approx Bits\ Shipped \times ASP\ per\ Bit
\]

But HBM/product mix complicates average ASP.

Revenue growth can come from:

- more bits;
- higher market price;
- richer HBM/premium mix;
- FX translation.

Margin effect differs by driver.

## Customer concentration: AI demand can create new dependency

High-end HBM customers are fewer than generic consumer-memory buyers.

Winning large hyperscaler/accelerator customers creates huge growth but may raise qualification/customer concentration.

Customer power can influence pricing, capex timing and technology roadmap.

Therefore structural demand growth does not remove bargaining risk.

## Supply-chain geopolitics: semiconductor is now strategic infrastructure

Advanced chips depend on global equipment, EDA, IP and materials. No single country owns every critical node.

Export controls and technology restrictions therefore can affect:

- equipment access;
- customer markets;
- fab location;
- China operations;
- R&D collaboration.

**Self-sufficiency 100%** is unrealistic and often inefficient. Resilience means reducing critical single-point dependency and maintaining alternatives.

Geopolitics is now a company cash-flow variable, not merely foreign-policy background.

## Location economics: why fabs cluster

Fabs need stable power, ultrapure water, suppliers, engineering talent and logistics.

Clusters reduce coordination time and improve labor/supplier density.

But concentration also creates common-mode risk: local grid/water/disaster issue can affect multiple facilities.

Industrial geography is therefore a trade-off between agglomeration efficiency and resilience.

Xem [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md) và [`30_energy_security_power_market_and_transition.md`](./30_energy_security_power_market_and_transition.md).

## Electronics final products: economics khác chip

Smartphone, TV và appliances have BOM, channel inventory, marketing, product-cycle and brand economics.

Premium brand creates pricing power; however replacement cycle can limit unit growth.

Hardware margin may be moderate while ecosystem services/accessories raise lifetime value.

Therefore Samsung Electronics cannot be analyzed as “a semiconductor company” only. Segment mix matters.

## Display: technology leadership can migrate

Korea historically led LCD, but commoditization and Chinese scale pressure changed economics. Korean firms shifted emphasis toward OLED and advanced display technologies.

Display has semiconductor-like characteristics:

- high capex;
- yield learning;
- customer qualification;
- technology generations;
- overcapacity risk.

A technology can be superior technically but fail economically if yield/cost/customer adoption are poor.

## OLED: differentiation vs capex risk

OLED can create higher barriers through materials/process know-how and premium-device demand.

But new-generation capacity still must reach utilization. If customer product cycle disappoints, expensive display lines can underutilize.

Technology leadership does not eliminate capacity economics.

## Supplier ecosystem: capability spreads beyond Samsung/SK/LG

Large Korean semiconductor/electronics champions rely on many equipment/material/component suppliers.

This creates spillover: suppliers learn world-class quality and can export to external customers.

But captive dependence can also emerge. A supplier with one dominant customer may have technology but weak bargaining power.

Thus semiconductor success can either diffuse productivity or concentrate it depending on supplier scale-up.

Xem [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## R&D and talent: process knowledge is cumulative

Semiconductor frontier moves continuously, so R&D is not optional growth spending; much of it is **survival investment**.

Skill also contains tacit knowledge. Senior process engineer may know subtle interactions not captured fully in manuals.

This makes talent retention and cluster depth strategic assets.

Xem [`29_innovation_rnd_education_and_human_capital.md`](./29_innovation_rnd_education_and_human_capital.md).

## Company-analysis dashboard

For memory/IDM:

```text
ASP / bit growth
HBM/premium mix
Inventory days
Utilization
Yield commentary
Capex
Depreciation
R&D
Net cash/debt
```

For foundry:

```text
Node mix
Utilization
Yield/ramp
Customer concentration
Capex
Advanced packaging ecosystem
```

For equipment/material supplier:

```text
Customer concentration
Order backlog
Installed base
Service/consumable share
Qualification wins
Export-control exposure
```

No metric should be read alone.

## Cycle normalization

At peak memory price, trailing P/E can appear extremely low. At trough, P/E can appear very high or meaningless.

Therefore semiconductor valuation needs normalized cycle assumptions.

Ask:

```text
What is mid-cycle ASP?
What utilization is sustainable?
How much depreciation after new fabs?
What premium mix is structural?
```

This is more useful than mechanically comparing one-year P/E.

## Stress test

Useful shocks:

- memory ASP -20%;
- HBM qualification delay;
- utilization -10pt;
- new-fab depreciation starts before demand;
- export restriction;
- top customer loses share;
- KRW move;
- electricity cost increase.

Then trace operating margin, FCF and capex response.

## Mental Model

> Semiconductor là cuộc chơi của **technology + yield + capacity + product mix + cycle + ecosystem**. Korea’s advantage không nằm ở một factory; nó nằm ở cumulative manufacturing and engineering system built across decades.

Một map ngắn:

```text
R&D / Process
      ↓
Yield + Product capability
      ↓
Customer qualification
      ↓
Volume / ASP / Mix
      ↓
Cash flow
      ↓
Next-generation capex
      ↓
Learning loop repeats
```

## Common misconceptions

**“AI boom làm memory hết cycle.”** Sai. Structural demand tăng nhưng supply response/capex vẫn tạo cycle.

**“Capex lớn là bullish.”** Không nếu future return thấp hoặc overcapacity.

**“Advanced node nhỏ hơn luôn tốt hơn.”** Không; yield/cost/PPA/use case matter.

**“Semiconductor company nào cũng hưởng AI như nhau.”** Sai. Node/value-chain exposure khác nhau.

**“Self-sufficiency 100% là resilience tối ưu.”** Không nhất thiết. Diversification và trusted alternatives thường efficient hơn.

**“Revenue tăng nghĩa technology lead tăng.”** Không; ASP/FX/cycle có thể giải thích growth.

## Connections

Đọc cùng [`02_trade_export_and_global_value_chains.md`](./02_trade_export_and_global_value_chains.md), [`06_sme_mid_sized_and_subcontracting_ecosystem.md`](./06_sme_mid_sized_and_subcontracting_ecosystem.md), [`11_banks_finance_and_corporate_funding.md`](./11_banks_finance_and_corporate_funding.md), [`21_economy_to_company_transmission.md`](./21_economy_to_company_transmission.md), [`24_regional_clusters_and_industrial_geography.md`](./24_regional_clusters_and_industrial_geography.md), [`29_innovation_rnd_education_and_human_capital.md`](./29_innovation_rnd_education_and_human_capital.md) và [`30_energy_security_power_market_and_transition.md`](./30_energy_security_power_market_and_transition.md).
