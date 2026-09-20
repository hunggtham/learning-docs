# LG Energy Solution — battery economics, utilization, contracts và CAPEX cycle

Case này dùng LG Energy Solution như một laboratory để hiểu một trong những ngành strategic manufacturing quan trọng của Hàn Quốc: **secondary battery (이차전지)**. Battery nhìn bề ngoài giống một growth industry đơn giản: EV tăng thì battery tăng. Nhưng economic reality phức tạp hơn nhiều vì demand growth, chemistry, customer contracts, raw-material pricing, factory utilization, subsidies, geographic localization và CAPEX đều tương tác.

Mục tiêu là học cách biến câu chuyện “EV growth” thành một causal model có thể nối tới revenue, margin, cash flow và return on invested capital.

Xem nền tảng tại [15_automotive_battery_mobility](../15_automotive_battery_mobility.md), [02_trade_export_and_global_value_chains](../02_trade_export_and_global_value_chains.md) và [21_economy_to_company_transmission](../21_economy_to_company_transmission.md).

## 1. Battery company bán cái gì?

Battery manufacturer không đơn giản bán “pin”. Economic unit có thể là cells, modules, packs hoặc energy-storage products tùy customer/application.

Một simplified revenue bridge:

\[
Revenue \approx Shipment\ (GWh) \times Revenue\ per\ Wh
\]

Nhưng `revenue per Wh` không chỉ là pure selling price. Nó có thể chịu ảnh hưởng chemistry, product format, raw-material pass-through, customer contract, region và mix.

Vì vậy khi revenue giảm, analyst phải tách:

```text
Shipment volume?
Price / raw-material pass-through?
Product mix?
FX?
Customer production schedule?
```

## 2. EV demand không truyền 1:1 vào battery shipment

Causal chain thực tế dài hơn:

```text
Consumer auto demand
→ OEM vehicle production
→ EV / hybrid mix
→ battery size per vehicle
→ OEM inventory
→ battery order / shipment
→ cell factory utilization
```

Nếu EV retail demand tăng 10% nhưng OEM đang destock inventory, battery shipment trong một quarter vẫn có thể yếu.

Ngược lại, battery shipment có thể tăng trước vehicle sales nếu OEM build inventory hoặc ramp new model.

> **Mental Model:** battery demand là derived demand. Muốn hiểu cell maker, phải đi ngược tới vehicle platform và customer production schedule.

## 3. GWh capacity không đồng nghĩa GWh economic output

Một factory được công bố có `X GWh capacity` không có nghĩa ngay lập tức tạo ra X GWh saleable cells.

Giữa nameplate capacity và economic output có:

```text
Equipment installation
→ qualification
→ ramp
→ yield stabilization
→ customer approval
→ utilization
→ saleable output
```

Do đó hai variables phải tách rõ:

**Utilization (가동률)** phản ánh mức sử dụng capacity.

**Yield (수율)** phản ánh tỷ lệ output đạt yêu cầu chất lượng.

Một plant chạy nhiều nhưng yield thấp có thể consume materials/labor mà không tạo proportional saleable output.

## 4. Fixed-cost intensity và operating leverage

Battery manufacturing cần factory, coating equipment, formation equipment, dry room, quality systems và depreciation lớn. Khi utilization thấp, fixed cost được spread trên ít output hơn.

Simplified unit cost:

\[
Unit\ Cost = Variable\ Cost + \frac{Fixed\ Manufacturing\ Cost}{Saleable\ Output}
\]

Nếu fixed cost = 1,000 và output = 100 units, fixed cost/unit = 10. Nếu output giảm còn 60, fixed cost/unit tăng lên khoảng 16.7 dù total fixed cost không đổi.

Đây là lý do utilization có thể làm margin biến động mạnh hơn shipment.

## 5. Raw-material pass-through: revenue có thể giảm mà economics không xấu tương ứng

Lithium, nickel, cobalt và other materials có thể ảnh hưởng cell price. Nhiều contracts có cơ chế price adjustment/pass-through ở mức độ khác nhau.

Nếu raw-material price giảm và selling price được reset thấp hơn, reported revenue có thể giảm dù physical shipment không giảm tương ứng.

Analyst vì vậy phải tránh suy luận:

> Revenue down = demand down.

Cần decomposition:

\[
Revenue\ Growth \approx Volume\ Effect + Price/Mix\ Effect + FX\ Effect
\]

và price effect cần tách commodity pass-through khỏi pricing power.

## 6. Chemistry là economics, không chỉ science

Battery chemistry ảnh hưởng energy density, safety, raw-material exposure, cost, performance và target vehicle segment.

High-nickel chemistry có different cost/performance trade-off so với LFP. Nhưng analyst không nên biến chemistry thành slogan “công nghệ A tốt hơn B”. Một chemistry có thể thắng ở premium long-range segment trong khi chemistry khác phù hợp mass-market/storage.

Economic question là:

```text
Customer requirement
→ chemistry choice
→ material bill
→ manufacturing process
→ yield / cost
→ price / margin
```

Technology advantage chỉ tạo value khi chuyển được thành qualification, volume và acceptable return on capital.

## 7. Customer concentration và platform risk

Battery supplier thường phụ thuộc một số global OEM/platforms lớn. Long-term contract có thể tăng visibility nhưng không loại bỏ risk.

Analyst cần hỏi:

- contract là firm purchase hay framework?
- volume commitment có flexibility không?
- pricing formula thế nào?
- customer có quyền delay platform không?
- plant có dedicated cho customer không?
- nếu customer demand yếu, capacity có chuyển sang customer khác được không?

Một dedicated plant có strategic value khi customer mạnh, nhưng tạo stranded-capacity risk nếu platform thất bại.

## 8. Joint venture — chia CAPEX nhưng tăng governance complexity

Battery expansion ở overseas markets thường dùng **joint venture (JV / 합작법인)** với automaker hoặc partner.

JV có thể giúp:

```text
Share capital burden
+ secure anchor customer
+ align production location
+ share execution knowledge
```

Nhưng accounting boundary rất quan trọng. JV có thể consolidated, equity-accounted hoặc có guarantee/commitment khác nhau tùy structure.

Không được nhìn headline “plant investment X trillion won” rồi mặc định toàn bộ CAPEX/debt nằm trên listed parent.

Hãy quay lại [09_disclosure_accounting_dart_kind](../09_disclosure_accounting_dart_kind.md) để xác định reporting perimeter.

## 9. Localization: geopolitics trở thành factory economics

Battery industry chịu tác động mạnh từ industrial policy, local-content rules, tariff, subsidy và supply-chain security.

Một plant ở North America có thể được xây không chỉ vì transport cost mà vì customer localization và policy economics.

Causal model:

```text
Policy incentive / local-content rule
→ plant location
→ CAPEX
→ local supply chain
→ labor / energy cost
→ subsidy / tax benefit
→ customer qualification
→ project ROIC
```

Do đó subsidy không nên được coi là “free profit”. Nếu subsidy chỉ bù cho structurally higher production cost, underlying competitiveness vẫn phải được đánh giá riêng.

## 10. CAPEX cycle: growth có thể làm cash flow xấu trước khi tốt

Một battery maker có thể report revenue growth và accounting profit nhưng free cash flow âm do aggressive capacity expansion.

Simplified:

\[
FCF \approx CFO - CAPEX
\]

Nhưng với growth manufacturer, câu hỏi quan trọng hơn là:

\[
Future\ Incremental\ ROIC = \frac{Incremental\ Operating\ Profit\ After\ Tax}{Incremental\ Invested\ Capital}
\]

Nếu industry overbuild capacity, future utilization thấp và incremental ROIC có thể thấp dù total market vẫn tăng.

> Growth industry không bảo đảm growth investment tạo value.

## 11. Depreciation lag và margin illusion

Factory CAPEX hôm nay không đi hết vào income statement hôm nay. Nó được capitalized rồi depreciated qua thời gian.

Khi new plants start production:

```text
CAPEX already spent
→ asset enters service
→ depreciation rises
→ utilization may still be low
→ margin pressure appears
```

Vì vậy peak CAPEX có thể đi trước peak depreciation. Analyst cần model cả cash timing và accounting timing.

## 12. Working capital

Battery manufacturing cần raw materials, work-in-process, finished goods và receivables. Growth có thể hút cash qua inventory/receivable.

Một stylized example:

```text
Revenue +25%
Operating profit +15%
Receivables +35%
Inventory +40%
```

Nếu CFO không theo profit, cần hỏi đó là normal ramp hay sign của weak sell-through/collection.

## 13. Warranty, quality và recall tail risk

Battery defect có thể tạo cost lớn vì cell là safety-critical component. Accounting provision chỉ là management estimate tại một thời điểm.

Analyst cần phân biệt:

```text
Known incident
→ estimated affected population
→ responsibility sharing with OEM
→ provision
→ actual cash settlement
```

Nếu technical root cause chưa chắc chắn, provision uncertainty cao.

Quality risk còn ảnh hưởng reputation, future customer qualification và insurance/legal costs — không chỉ one-time accounting charge.

## 14. Scenario model

### Base scenario

```text
EV demand grows moderately
→ shipment +15%
→ utilization improves
→ raw-material prices stable
→ yield normalizes
→ margin expands modestly
→ CAPEX remains elevated
```

### Downside scenario

```text
OEM delays EV platforms
→ shipment +0~5%
→ utilization falls
→ price competition increases
→ fixed cost per Wh rises
→ CAPEX already committed
→ FCF deteriorates
```

### Upside scenario

```text
Customer launches succeed
→ utilization rises faster
→ high-value mix improves
→ yield improves
→ fixed-cost absorption improves
→ operating leverage lifts margin
```

Scenario không cần dự đoán chính xác; mục tiêu là thấy **which variable dominates economics**.

## 15. Valuation: tránh dùng một multiple không có context

High-growth battery company có thể được valued bằng EV/EBITDA, P/E hoặc DCF tùy maturity, nhưng denominator cần normalized.

Nếu EBITDA cao trước khi depreciation phản ánh full new capacity, EV/EBITDA có thể trông rẻ giả tạo. Nếu current earnings depressed bởi ramp cost nhưng future utilization có path rõ, current P/E lại có thể vô nghĩa.

Reverse valuation hữu ích hơn:

> Current enterprise value đang imply utilization, margin và ROIC dài hạn ở mức nào?

Sau đó kiểm tra assumptions đó có phù hợp industry capacity và customer demand không.

## 16. Common misconceptions

### “EV sales tăng thì battery maker chắc chắn tăng lợi nhuận”

Sai vì price, mix, utilization, yield và contract economics có thể offset volume.

### “Capacity càng lớn càng có lợi thế”

Sai nếu capacity không được sử dụng hoặc project ROIC thấp.

### “Long-term contract loại bỏ cycle”

Sai vì volume timing, pricing formula và customer platform success vẫn thay đổi.

### “Subsidy là pure upside”

Sai nếu subsidy bù cho higher local cost hoặc cần CAPEX lớn để qualify.

## 17. Research workbook

Khi cập nhật filing mới, dựng table:

| Driver | Y-4 | Y-3 | Y-2 | Y-1 | Y0 |
|---|---:|---:|---:|---:|---:|
| Shipment / capacity proxy | | | | | |
| Revenue | | | | | |
| Operating margin | | | | | |
| CAPEX | | | | | |
| Depreciation | | | | | |
| CFO | | | | | |
| FCF | | | | | |
| Inventory | | | | | |
| Receivables | | | | | |
| Net debt / cash | | | | | |

Sau đó annotate new plants, JV, major platform launches, recalls và policy changes.

## Mental Model cuối

> Battery maker là một **capacity-allocation business dưới technology và policy constraints**. EV demand tạo opportunity, nhưng shareholder value chỉ xuất hiện khi company biến CAPEX thành qualified capacity, capacity thành high-yield output, output thành customer shipment và shipment thành cash với ROIC đủ cao.

Đọc tiếp [08_hanwha_aerospace_defense_backlog_case](./08_hanwha_aerospace_defense_backlog_case.md) để so sánh battery — nơi demand/capacity cycle quan trọng — với defense, nơi backlog, procurement và delivery schedule đóng vai trò trung tâm.