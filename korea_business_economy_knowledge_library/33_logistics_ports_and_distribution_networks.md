# Logistics, cảng biển và mạng phân phối Hàn Quốc (Logistics, Ports & Distribution / 물류·항만·유통망)

Một nền kinh tế export-oriented không thể tồn tại chỉ với factories. Value phải di chuyển: raw materials vào Korea, intermediate goods giữa plants, finished products ra ports, parcels tới household. Logistics (물류) là connective tissue giữa manufacturing và market.

## Logistics không chỉ là transportation

Logistics gồm inventory, warehousing, transport, order processing, customs và information flow. Mục tiêu không phải “ship rẻ nhất” mà tối ưu total landed cost và service level.

Một simplified total cost:

\[
Total\ Logistics\ Cost = Transport + Warehousing + Inventory\ Carrying + Stockout + Handling
\]

Nếu dùng sea freight rẻ hơn nhưng lead time tăng 20 ngày, inventory carrying cost có thể lớn hơn shipping saving.

## Korea geography: peninsula nhưng trade bằng sea/air

Political division làm overland connection với Eurasia limited, nên ports và airports có vai trò rất lớn. Busan là global container hub; Incheon hỗ trợ capital-region logistics và air/sea connection; Ulsan/Gwangyang/Pohang gắn bulk industrial cargo.

Port specialization phản ánh industrial geography. Steel, petrochemicals, automobiles và containers có handling requirement khác nhau.

## Busan: transshipment economics

Transshipment port không chỉ phục vụ domestic cargo mà chuyển containers giữa shipping routes. Network effect xuất hiện: càng nhiều routes gọi cảng, càng hấp dẫn carriers/cargo; càng nhiều cargo, càng justify frequency.

Nhưng hub position phụ thuộc port efficiency, automation, labor, hinterland connection và competition với China/Japan/other Asian ports.

## Containerization thay đổi trade economics

Standard container giảm handling cost và damage, cho phép intermodal transport ship–rail–truck. Đây là technology có enormous economic impact vì nó giảm transaction/friction cost, giống API standard trong software.

> Mental model: container là “standardized interface” của physical supply chain.

## Inventory: cash bị khóa trong hàng hóa

Inventory không chỉ là operational object mà là working capital. Days Inventory Outstanding (DIO):

\[
DIO = \frac{Average\ Inventory}{COGS}\times365
\]

Nếu shipping disruption làm company giữ thêm 30 ngày inventory, cash conversion cycle dài hơn. Resilience có financial cost.

Xem [11_banks_finance_and_corporate_funding](./11_banks_finance_and_corporate_funding.md).

## Just-in-time và resilience

Just-in-time giảm inventory nhưng tăng sensitivity với disruption. Sau pandemic, chip shortage và geopolitical risk, nhiều firms chuyển sang “just-in-case” cho critical components.

Optimal buffer phụ thuộc shortage cost. A cheap screw nếu thiếu có thể stop entire assembly line; economic value của buffer không tỷ lệ với purchase price.

## Cold chain và specialized logistics

Biopharma, food và chemicals cần temperature/control compliance. Cold chain failure có thể destroy product value even if transport arrives on time.

High-regulation logistics tạo entry barrier qua certifications, equipment, tracking và quality system.

## E-commerce last mile

Coupang và Korean e-commerce ecosystem cho thấy warehouse density, routing software và delivery network có thể trở thành moat. Last-mile cost cao vì parcel phải đi từ shared network tới individual door.

Route density giảm unit cost: nếu driver giao nhiều packages trong cùng apartment complex, cost/order thấp hơn sparse rural route. Đây là **density economics**.

## Logistics automation và IT

Warehouse Management System (WMS), Transportation Management System (TMS), barcode/RFID, routing algorithms và robotics biến logistics thành data problem.

Shortest-path, vehicle-routing và inventory optimization liên hệ trực tiếp graph theory và operations research. Software quality có impact physical cost: bad demand forecast tạo excess inventory hoặc stockout.

## Shipping rates và exporter margin

Exporter quote terms theo Incoterms quyết định ai chịu freight/risk ở từng stage. Nếu ocean freight tăng, impact margin phụ thuộc contract terms và pricing power.

Không nên thấy shipping index tăng rồi kết luận mọi exporter margin giảm như nhau.

## Air cargo và semiconductors

High-value, low-weight products như chips phù hợp air cargo hơn bulk commodities. Time value cao hơn transport cost. Incheon airport vì vậy là logistics infrastructure quan trọng cho advanced manufacturing.

## 3PL và contract logistics

Third-party logistics (3PL / 제3자물류) cho phép firm outsource warehousing/transport. 3PL economics phụ thuộc network scale, utilization, customer concentration và labor/automation.

A logistics provider có low margin nhưng high asset turnover có thể vẫn tạo acceptable ROIC. Vì vậy margin alone không đủ.

## Mental Model

> Logistics tối ưu **time + reliability + working capital + transport cost**, không chỉ distance. Trong export economy, supply-chain design là một phần của competitive advantage.

## Common misconceptions

Inventory càng thấp không phải lúc nào càng tốt; stockout risk có thể lớn hơn carrying cost.

Port lớn không chỉ vì domestic economy lớn; transshipment/network position matter.

Fast delivery không miễn phí. Cost có thể nằm trong margin, membership fee, seller fee hoặc labor intensity.

## Connections

Đọc cùng [02_trade_export_and_global_value_chains](./02_trade_export_and_global_value_chains.md), [16_shipbuilding_steel_chemicals_heavy_industry](./16_shipbuilding_steel_chemicals_heavy_industry.md), [17_platform_telecom_content_retail_services](./17_platform_telecom_content_retail_services.md) và [24_regional_clusters_and_industrial_geography](./24_regional_clusters_and_industrial_geography.md).

## Shipping company economics khác port economics

Container shipping carrier sở hữu/charter vessels và chịu freight-rate cycle, bunker fuel và vessel supply. Port operator kiếm fee từ throughput/terminal services. Cùng container volume nhưng earnings volatility khác.

Shipping supply rất inelastic short-term vì build ship mất years. Khi demand jump, freight rate có thể spike; khi many new ships deliver, rates fall even if trade still grows.

## HMM và national shipping capability

Korean shipping history cho thấy container line có strategic value cho export economy nhưng business economics cực cyclical. Financial distress của carrier lớn có spillover tới exporters, ports và trade finance.

Điều này giải thích vì sao shipping đôi khi nhận policy attention cao hơn normal industry of similar GDP share.

## Bunker fuel và IMO regulation

Vessel economics chịu fuel price và environmental rules. Slow steaming giảm fuel consumption nhưng tăng transit time/capacity tied up.

Sulfur/carbon rules có thể làm modern efficient fleet more valuable, nhưng require capex/new fuels.

## Freight forwarder vs carrier

Freight forwarder không nhất thiết own ships/trucks; họ coordinate capacity, documentation và routing. Asset-light model có lower capex nhưng margin phụ thuộc procurement scale và customer relationships.

3PL có thể combine asset-heavy warehouses với asset-light coordination.

## Customs và bonded logistics

Goods crossing border cần classification, valuation, origin và documentation. Error có thể delay shipment or trigger duties/penalties.

Bonded warehouse cho phép goods stored before duties paid/clearance, useful for re-export/transshipment. Customs competence là operational capability, not admin afterthought.

## Incoterms: ai chịu cost và risk?

FOB, CIF, DDP và các Incoterms phân allocation của transport cost, insurance/risk và customs responsibility. Incoterm không xác định ownership/payment alone; nó xác định delivery obligations.

Khi compare exporter margins, shipping cost exposure phải đọc cùng Incoterm.

## Parcel density và Korean apartment geography

Korea high urban density/apartment concentration tạo favorable last-mile route economics. Driver có thể deliver many parcels per stop/building relative low-density suburbs.

Đây là geographic source của delivery speed, not software alone. Software routing + dense housing combine thành moat.

## Fulfillment center economics

Warehouse automation có high fixed capex. Return phụ thuộc throughput. Peak season cần excess capacity; off-season utilization thấp.

Robotics investment rational khi labor saving + throughput + error reduction exceed depreciation/maintenance.

## Reverse logistics

E-commerce returns tạo reverse flow: pickup, inspection, refurbish/disposal và refund. Fashion returns especially high có thể erase front-end gross margin.

A company reporting GMV growth nhưng return rate rising có lower economic quality.

## Supply-chain visibility

Digital tracking giúp firm know location/status inventory. Visibility không prevent disruption, nhưng reduce reaction time and safety stock uncertainty.

For software analogy, supply chain without visibility giống distributed system without observability: failure occurs, nhưng team không biết node nào broken.