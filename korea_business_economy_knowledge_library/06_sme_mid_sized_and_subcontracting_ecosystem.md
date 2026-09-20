# SME, doanh nghiệp trung견 và hệ sinh thái subcontracting (중소기업·중견기업·하도급 생태계)

Nếu chaebol là phần dễ thấy nhất của kinh tế Hàn Quốc, SME là phần lớn về số doanh nghiệp và việc làm. Theo thống kê cơ bản 2024 do Ministry of SMEs and Startups công bố năm 2026, SME chiếm khoảng 99,9% doanh nghiệp, 80,4% người làm việc và 43,7% doanh thu. Vì vậy muốn hiểu workplace, supply chain hoặc cơ hội việc làm tại Hàn Quốc phải hiểu SME ecosystem.

## SME không phải phiên bản nhỏ của large enterprise

Doanh nghiệp nhỏ và vừa (SME / 중소기업) thường có ít lớp quản trị hơn, access to capital hạn chế hơn và customer concentration cao hơn. Điều đó làm họ linh hoạt nhưng cũng dễ bị shock. Một supplier có 50% revenue từ một chaebol affiliate có thể có kỹ thuật tốt nhưng bargaining power yếu.

**Doanh nghiệp trung견 (Mid-sized Enterprise / 중견기업)** thường xuất hiện khi công ty đã vượt SME thresholds nhưng chưa đạt scale của large conglomerate. Nhiều công ty công nghệ công nghiệp B2B ít nổi tiếng với người tiêu dùng nằm ở đây.

## Tiered supplier network

Trong automotive hoặc electronics, supplier network có thể hình dung theo tầng:

```text
OEM / Final assembler
      ↓
Tier 1 — module/system suppliers
      ↓
Tier 2 — components/materials
      ↓
Tier 3 — process, tooling, raw inputs
```

Không phải ngành nào cũng dùng đúng nhãn Tier 1/2/3, nhưng mental model hữu ích. Khi demand của OEM thay đổi 5%, order ở upstream đôi khi biến động lớn hơn vì inventory adjustment; đây gần với **bullwhip effect / 채찍효과** trong supply-chain theory.

## Subcontracting và 하도급

**Subcontracting (하도급)** là việc contractor chính giao một phần công việc cho subcontractor. Nó giúp specialization nhưng tạo risk về payment terms, pricing pressure, technology appropriation và dependency. Vì thế Hàn Quốc có regulatory framework về fair subcontract transactions.

Trong IT/SI, mental model tương tự xuất hiện qua 원청–하청, prime contractor–subcontractor và multi-layer outsourcing. Những layer này ảnh hưởng scope, margin, communication path và career experience của developer.

## Productivity gap

Một vấn đề cấu trúc là productivity và wage gap giữa large enterprises và SME. Large firm thường có scale, automation, global demand và capital intensity cao hơn; SME service sectors có thể khó tăng productivity nhanh. Gap này ảnh hưởng labor mobility: nhiều người cạnh tranh để vào 대기업 hoặc public sector vì wage, benefits và perceived stability.

Nhưng không nên kết luận SME luôn kém. Một precision component company có thể có moat mạnh hơn một large subsidiary ở ngành commoditized. Company analysis phải quay lại unit economics, customer concentration, technology và balance sheet.

## Financing constraint

SME thường phụ thuộc bank loans hơn direct capital markets. Khi rate tăng, interest burden tác động nhanh. Collateral, guarantees và policy finance có vai trò lớn. Đây là lý do [11_banks_finance_and_corporate_funding](./11_banks_finance_and_corporate_funding.md) là dependency quan trọng.

## Human capital và key-person risk

Ở công ty nhỏ, một kỹ sư senior hoặc sales manager có thể giữ knowledge quan trọng. Nếu người đó rời đi, operational risk tăng mạnh. Large enterprise có process và redundancy tốt hơn nhưng có thể chậm hơn. Đây là trade-off giữa **organizational slack** và efficiency.

## Vì sao SME chiếm số lượng áp đảo nhưng không chiếm cùng tỷ trọng value added?

SME (Small and Medium-sized Enterprise / 중소기업) thường chiếm gần như toàn bộ số doanh nghiệp và phần lớn employment, nhưng productivity và wage trung bình có thể thấp hơn large enterprises. Đây không phải contradiction. Số lượng firms đo **count**, còn value added phụ thuộc scale, capital intensity, technology và bargaining power.

Một semiconductor fab có thể tạo value added rất lớn với số nhân viên tương đối nhỏ; hàng nghìn restaurants hoặc small suppliers lại tạo nhiều jobs nhưng margin thấp. Vì vậy khi nói “SME là xương sống”, phải hỏi đang nói về employment, firm count hay value creation.

## Supplier dependence và monopsony-like pressure

Trong tiered supply chain, supplier nhỏ đôi khi có một hoặc hai customers lớn. Khi customer concentration cao, buyer có bargaining power mạnh về price, payment terms và quality investment. Đây gần với **monopsony power / 수요독점력** ở phía mua.

Nhưng relationship không chỉ exploitative. Long-term OEM contract có thể cho supplier demand visibility, technical support và chance scale. Vấn đề là how value/risk are shared.

## 중견기업: bridge bị bỏ quên

Mid-sized enterprise (중견기업) quan trọng vì nó nằm giữa SME policy world và large-enterprise world. Một firm vượt SME thresholds có thể mất tax/support benefits trước khi có scale/finance advantages của chaebol. Đây thường được gọi là growth ladder problem.

Policy tốt cần tránh tạo incentive “không lớn nữa để giữ ưu đãi”. Firm nên muốn graduate khỏi SME status vì productivity và market expansion, không bị penalty quá mạnh khi lớn lên.

## Succession, owner dependence và professionalization

Nhiều SMEs là founder-led. Founder có customer relationship, technical know-how và credit guarantee personally. Khi succession xảy ra, company đối mặt key-person risk. Professional management, documented processes và governance vì vậy là phần của scale-up, không phải bureaucracy thừa.

## Digitalization và ERP

SME productivity thường bị giới hạn bởi fragmented processes, manual Excel, undocumented know-how và weak data systems. ERP/MES/CRM không tự động tăng productivity, nhưng giúp biến tacit knowledge thành repeatable process.

Trong manufacturing, MES data có thể giảm downtime và defect; trong services, CRM giúp retention. Đây là nơi IT investment có return thực nếu process được redesign, không chỉ “cài software”.

## Cách đọc SME supplier

Khi phân tích một SME supplier, hãy xem top-customer share, contract duration, switching cost, certification, machine utilization, receivable days, inventory và whether company owns unique process/IP. Revenue growth từ một customer duy nhất có thể nhìn đẹp nhưng tăng concentration risk.

## Mental Model

> SME ecosystem là “mạch máu mao quản” của nền kinh tế: mỗi công ty nhỏ có vẻ không quan trọng ở cấp macro, nhưng hàng triệu quan hệ supplier–customer–employment kết hợp lại quyết định khả năng nền kinh tế truyền công nghệ và thu nhập xuống rộng đến đâu.

## Common misconceptions

SME không đồng nghĩa low-tech. Nhiều supplier chuyên sâu có technology rất cao nhưng market niche nhỏ.

Làm supplier cho chaebol không tự động an toàn. Customer concentration tạo cả volume stability lẫn dependency risk.

## Connections

Xem [02_trade_export_and_global_value_chains](./02_trade_export_and_global_value_chains.md), [11_banks_finance_and_corporate_funding](./11_banks_finance_and_corporate_funding.md), [12_labor_titles_compensation_and_workplace](./12_labor_titles_compensation_and_workplace.md) và industry files `14–16`.
