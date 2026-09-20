# Thuế doanh nghiệp, regulation và chính sách cạnh tranh (Tax & Regulation / 법인세·규제·공정거래)

Một nền kinh tế doanh nghiệp không vận hành chỉ bằng contract giữa private parties. Nhà nước xác định legal form, tax base, disclosure duty, labor floor, competition rules và giới hạn đối với những cấu trúc có thể tạo concentration hoặc conflict of interest. File này xây mental model về “luật chơi” thay vì biến thành sổ tay pháp lý.

## Corporate tax: thuế đánh vào taxable income, không phải revenue

Thuế thu nhập doanh nghiệp (Corporate Income Tax / 법인세) tính trên **thu nhập chịu thuế (taxable income / 과세표준)** sau các điều chỉnh theo luật, không đơn giản lấy revenue nhân tax rate.

Theo National Tax Service, với năm tài chính bắt đầu từ 01/01/2026, biểu thuế cơ bản cho công ty vì lợi nhuận sử dụng các bậc 10%, 20%, 22% và 25% theo mức taxable income. Tuy nhiên effective tax rate trên financial statements có thể khác statutory rate do deferred tax, tax credits, overseas tax, permanent differences và loss carryforwards.

\[
Effective\ Tax\ Rate \approx \frac{Income\ Tax\ Expense}{Pre\ Tax\ Income}
\]

Khi effective tax rate thay đổi mạnh, không nên kết luận ngay “company được ưu đãi” hoặc “tax tăng”; cần đọc tax note.

## VAT và transaction layer

Thuế giá trị gia tăng (Value Added Tax / 부가가치세) là tax trên consumption/transaction chain và khác corporate income tax. Doanh nghiệp thường thu output VAT và khấu trừ input VAT theo rule. Về economics, VAT không nên được trộn với company revenue/profit một cách máy móc.

## Fair Trade Commission

Korea Fair Trade Commission (공정거래위원회) giám sát competition, large business groups, unfair transactions và nhiều vấn đề market conduct. Với conglomerate analysis, KFTC đặc biệt quan trọng vì regulator nhìn **business group control** thay vì chỉ từng corporation.

Các large business groups thuộc framework `공시대상기업집단` có disclosure và related obligations; nhóm lớn hơn thuộc `상호출자제한기업집단` chịu thêm restrictions. Threshold cụ thể cần kiểm tra từng năm.

## Antitrust reasoning

Competition policy không đồng nghĩa “công ty lớn là xấu”. Một company có market share cao vì technology tốt có thể tạo consumer value. Vấn đề competition xuất hiện khi market power được dùng để ngăn entry, ép trading partners hoặc duy trì structure làm giảm cạnh tranh.

Market power phụ thuộc **relevant market definition / 관련시장 획정**. Một company có 80% market của một niche nhỏ nhưng vẫn bị substitute từ product khác. Vì vậy market share chỉ có nghĩa sau khi xác định product/geographic market.

## Subcontracting và fair transaction

Trong supplier ecosystem, power imbalance có thể nằm ở payment terms, price reduction, technology information hoặc unilateral contract change. Regulatory rules về 하도급 cố giảm abuse nhưng economic dependency vẫn tồn tại. Khi phân tích supplier, legal protection không thay thế việc đo customer concentration.

## Disclosure và securities regulation

Listed companies phải tuân disclosure và capital-market rules. Một event có thể đồng thời chịu Commercial Act, Capital Markets Act, exchange rules và accounting standards. Vì vậy “company announced X” phải đọc disclosure category và legal consequence, không chỉ headline.

## Regulation như economic variable

Regulation có thể tạo cost nhưng cũng tạo moat. Banking license, telecom spectrum, drug approval hoặc environmental permit hạn chế entry. Company đã có license/scale có thể hưởng barrier, trong khi rule change có thể phá economics cũ.

## Regulation là một phần của business model

Trong sectors như telecom, finance, energy, healthcare và platforms, regulation quyết định price, entry barrier, data use và permissible conduct. Vì vậy regulatory analysis không phải appendix legal; nó là revenue/cost driver.

## Effective tax rate vs statutory rate

Statutory corporate tax rate không bằng cash tax. Effective tax rate bị ảnh hưởng tax credits, loss carryforwards, foreign income, deferred tax và one-offs. Analyst nên reconcile income-tax expense với cash tax paid nhiều năm.

## Competition policy và chaebol

Korea competition policy phát triển một phần để xử lý concentration và unfair transactions trong large business groups. KFTC designation/disclosure rules tạo data về affiliates và control. Đây là nguồn quan trọng cho group analysis.

## Platform regulation

Digital platform tạo new competition problems: self-preferencing, tying, data advantage và dependency của sellers. Traditional market-share analysis đôi khi khó vì zero-price services. Regulator phải xác định relevant market và network effects.

## Compliance cost như fixed cost

Regulation có thể tăng fixed compliance cost. Điều này đôi khi vô tình lợi large incumbents vì họ spread cost trên scale lớn, tạo barrier cho SMEs. Vì vậy “stricter regulation = more competition” không luôn đúng.

## Policy uncertainty

Khi rule chưa final, market giá vào scenario. Company có thể delay capex hoặc giữ cash. Regulatory uncertainty vì vậy có real-option effect: chờ đợi có value khi irreversible investment lớn.

## Mental Model

> Regulation là một phần của business model. Nếu profit tồn tại vì license, tax credit, subsidy, tariff hoặc legal restriction, những policy variables phải nằm trong risk model giống raw-material price hay FX.

## Common misconceptions

Statutory tax rate khác effective tax rate và khác cash tax paid trong kỳ.

“Bị regulation” không tự động là negative. Regulation có thể giảm competition nhưng cũng làm compliance cost cao; net effect phải phân tích company-specific.

## Nguồn chính

National Tax Service: `법인세 세율 (2026년 이후)`; KFTC: `대기업집단 정책` và Fair Trade Act framework.

## Connections

Xem [04_chaebol_and_large_business_groups](./04_chaebol_and_large_business_groups.md), [06_sme_mid_sized_and_subcontracting_ecosystem](./06_sme_mid_sized_and_subcontracting_ecosystem.md), [08_corporate_governance_ownership_and_control](./08_corporate_governance_ownership_and_control.md) và [09_disclosure_accounting_dart_kind](./09_disclosure_accounting_dart_kind.md).
### Nguồn kiểm tra hiện hành

- National Tax Service, corporate tax rates from 2026: https://nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7746&mi=2372
- Korea Fair Trade Commission, Large Business Group Policy: https://www.ftc.go.kr/www/contents.do?key=696


## Tax incidence: người nộp thuế pháp lý và người chịu cost kinh tế có thể khác

Nếu government tăng tax lên firm, firm có thể pass một phần qua higher prices, lower wages hoặc lower shareholder return. Ai cuối cùng chịu burden phụ thuộc elasticity.

Đây là **tax incidence / 조세귀착**. Vì vậy policy analysis không dừng ở “tax đánh vào corporation”.

## Deferred tax và accounting profit

Tax expense trên income statement có thể khác cash tax vì timing differences. Deferred tax asset/liability phát sinh khi accounting recognition và tax recognition lệch thời điểm.

Một low effective tax rate một năm có thể do one-off credit, geographic mix hoặc deferred items, không chứng minh structural tax advantage.

## Merger control

Large M&A có thể cần competition review nếu transaction ảnh hưởng market concentration. Synergy cho shareholders không tự động đồng nghĩa social benefit; regulator xem price, entry barrier, innovation và consumer choice.

## Regulation as moat

Compliance cost có thể bất lợi cho small entrant nhưng advantage cho incumbent đã có legal/compliance infrastructure. Banking, healthcare, telecom và defense đều có effect này.

Regulation vì thế vừa giảm risk/externality vừa có thể tăng entry barrier. Good analysis phải thấy cả hai.

## Platform competition khác industrial cartel

Digital platform có zero/low-price user side, nên consumer-price test truyền thống không đủ. Competition authority còn phải nhìn data, self-preferencing, switching cost, seller dependency và network effects.

Market definition trong platform economy vì vậy khó hơn “ai bán cùng sản phẩm”.