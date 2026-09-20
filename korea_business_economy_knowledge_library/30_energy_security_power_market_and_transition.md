# Năng lượng, an ninh điện và chuyển đổi carbon tại Hàn Quốc (Energy Security & Transition / 에너지안보·전력시장·탄소전환)

Hàn Quốc là một nền kinh tế industrial, energy-intensive nhưng có ít domestic fossil resources và power system hầu như không kết nối với neighboring grids. Vì vậy energy không chỉ là utility bill; nó là **industrial constraint, national-security variable và climate-transition problem** cùng lúc.

## Import dependency: energy bắt đầu từ external balance

Oil, LNG và coal phần lớn phải nhập khẩu. Khi commodity price hoặc KRW/USD tăng, import bill tăng. Một shock Middle East vì vậy có thể truyền từ oil price → trade balance → inflation → company input cost → household fuel/electricity cost.

Một simplified cost:

\[
KRW\ Energy\ Cost \approx USD\ Price \times KRW/USD\ Exchange\ Rate
\]

Nếu oil price đứng yên nhưng won yếu 10%, local-currency cost vẫn tăng gần tương ứng trước hedging/tax effects.

Đây là reason energy và FX phải được phân tích cùng nhau. Xem [21_economy_to_company_transmission](./21_economy_to_company_transmission.md).

## Electricity khác commodity bình thường

Electricity khó store ở scale lớn so với oil; supply và demand phải balance liên tục. Power system cần capacity đủ cho peak demand và reserve margin để chịu plant outage hoặc weather shock.

Một semiconductor fab không chỉ quan tâm electricity price; nó cần **quality và reliability**. Short outage có thể làm hỏng wafer batches và gây loss lớn hơn tiền điện. Vì vậy grid infrastructure là competitive factor của industrial cluster.

## KEPCO và cấu trúc thị trường điện

Korea Electric Power Corporation (KEPCO / 한국전력공사) giữ vai trò trung tâm trong transmission/distribution và retail system, trong khi generation có multiple subsidiaries/producers. Structure có tính public-policy cao hơn electricity markets fully liberalized.

Tariff vì thế vừa là price vừa là policy instrument. Nếu fuel cost tăng nhanh nhưng retail tariff điều chỉnh chậm, economic loss không biến mất; nó dịch vào utility balance sheet hoặc future tariff burden.

> Mental model: price cap có thể trì hoãn người trả cost, nhưng không xóa physical cost của fuel và generation.

Xem [25_public_enterprises_and_state_owned_companies](./25_public_enterprises_and_state_owned_companies.md).

## Nuclear: high fixed cost, low fuel share và baseload capability

Nuclear power (원자력) yêu cầu capital cost lớn và construction lead time dài, nhưng khi plant vận hành, fuel cost share thấp hơn fossil generation và output ổn định.

Korea có strong nuclear engineering/manufacturing ecosystem. IEA 2025 ghi nhận 26 reactors với khoảng 26 GW capacity cung cấp khoảng một phần ba electricity, và nuclear vẫn là pillar trong long-term strategy.

Economics của nuclear phải tính full lifecycle: construction, financing, operation, fuel, decommissioning và waste management. Chỉ so fuel cost sẽ sai.

## LNG: flexibility đổi lấy fuel exposure

Gas-fired power có thể ramp linh hoạt hơn và phù hợp balancing system, nhưng Korea phải import LNG. LNG price phụ thuộc global market, long-term contracts, spot market, shipping và FX.

Trong transition có nhiều renewable variable, flexible gas hoặc storage có system value ngay cả khi energy cost per kWh không thấp nhất mọi thời điểm.

## Renewable energy và geography constraint

Solar/wind có zero fuel cost sau khi build nhưng output phụ thuộc weather. Korea có land density cao, mountainous terrain và grid constraints. Offshore wind có potential nhưng construction, permitting, cable và local acceptance phức tạp.

Renewable penetration tăng làm nhu cầu grid reinforcement, storage, demand response và flexible generation tăng. Vì vậy “build more solar” không đủ; system architecture phải thay đổi.

IEA 2025 nhận xét Korea vẫn có renewable share thấp trong nhóm IEA countries và cần simultaneous investment vào clean generation và grid.

## 11th Basic Electricity Plan và mix tương lai

11th Basic Electricity Supply and Demand Plan đặt roadmap tới 2038 với nuclear và renewables tăng vai trò, coal giảm mạnh và LNG vẫn đóng balancing role. Plan là policy target, không phải guaranteed realized mix; actual outcome phụ thuộc construction, permitting, demand và economics.

Điều quan trọng với business analyst là direction: power demand từ semiconductors, AI data centers và electrification có thể tăng, nên grid/capacity investment trở thành constraint thật.

## Carbon pricing và K-ETS

Korea Emissions Trading Scheme (K-ETS / 배출권거래제) đặt carbon cost lên covered emitters. Nếu company phát thải vượt allowance, carbon có economic price.

Carbon cost có thể đi vào marginal cost:

\[
Carbon\ Cost = Emissions\ (tCO_2e) \times Allowance\ Price
\]

Steel, petrochemical, cement và power generation đặc biệt nhạy. Nếu competitor ở jurisdiction có carbon cost khác, trade policy như CBAM có thể thay relative competitiveness.

## Hydrogen và ammonia: carrier problem

Hydrogen được coi là option cho hard-to-abate sectors và power balancing, nhưng hydrogen không phải primary energy source tự nhiên dễ khai thác; nó là **energy carrier** cần energy để sản xuất.

Economics phụ thuộc production route, electricity/gas cost, carbon intensity, storage và transport. “Hydrogen economy” chỉ hợp lý khi full chain tạo emission/cost benefit so với alternative.

## Battery ESS và grid stability

Energy Storage System (ESS / 에너지저장장치) có thể charge khi supply dư và discharge khi demand cao. Nhưng value không chỉ energy arbitrage; storage còn cung cấp frequency control, reserve và congestion relief nếu market design cho phép monetize.

Korea có domestic battery manufacturing strength, nên ESS là intersection giữa industrial policy và power-system need.

## Energy intensive industries

Semiconductors cần electricity và water reliability. Steel/petrochemicals cần heat/feedstock. Data centers cần continuous power. Battery materials cần process energy.

Vì vậy industrial location decisions ngày càng hỏi: grid connection khi nào? power price ổn định không? renewable procurement có đủ để đáp ứng customer ESG requirement không?

Energy transition vì thế trở thành **site-selection variable**.

## Mental Model

> Korea phải tối ưu bốn mục tiêu cùng lúc: **security, affordability, reliability và decarbonization**. Không technology nào tối ưu cả bốn trong mọi thời điểm; energy policy là bài toán portfolio và system integration.

## Common misconceptions

Renewable có zero fuel cost không có nghĩa system cost bằng zero.

Nuclear low-carbon không có nghĩa construction/financing risk nhỏ.

Electricity tariff thấp không chứng minh generation cost thấp.

Energy independence tuyệt đối không cần thiết; diversification và resilience quan trọng hơn tự cung cấp 100%.

## Connections

Đọc cùng [14_semiconductors_electronics_display](./14_semiconductors_electronics_display.md), [16_shipbuilding_steel_chemicals_heavy_industry](./16_shipbuilding_steel_chemicals_heavy_industry.md), [24_regional_clusters_and_industrial_geography](./24_regional_clusters_and_industrial_geography.md) và [25_public_enterprises_and_state_owned_companies](./25_public_enterprises_and_state_owned_companies.md).

### Nguồn nền

- International Energy Agency, *Korea 2025*: https://www.iea.org/reports/korea-2025
- IEA, 11th Basic Electricity Supply and Demand Plan: https://www.iea.org/policies/28827-11th-basic-electricity-supply-and-demand-plan

## SMP, wholesale cost và retail tariff

Korean power market uses wholesale settlement mechanisms including System Marginal Price concepts, while retail tariff to end users is administratively structured. Wholesale cost and retail price can therefore diverge for periods.

This distinction helps explain why KEPCO earnings can deteriorate when fuel prices spike even if customer tariff does not change immediately.

## Industrial electricity và competitiveness

Power-intensive firms care about both average tariff and volatility/reliability. If electricity cost is 5% of total cost, 20% tariff increase can reduce operating margin materially when pricing power weak.

Data centers, fabs, electric furnaces and electrochemical plants have different load profiles, so same tariff schedule has different impact.

## RE100 và corporate procurement

Global customers/investors increasingly ask suppliers to use renewable electricity. Korean exporters may need PPAs, green premiums or certificates to satisfy procurement targets.

Thus renewable availability affects export competitiveness even before carbon tax directly applies.

## Grid bottleneck

Generation project can be economically attractive but useless if transmission connection delayed. Grid queue becomes real option constraint.

For industrial cluster, announced plant capacity without secured power/water should not be treated as fully executable capacity.

## Nuclear export as industry

Korea's nuclear capability is also export business: engineering, components, construction and lifecycle services. This links energy policy with defense-like government diplomacy and heavy-industry supply chains.