# 7. OTC và chứng khoán phái sinh cấu trúc

**Phái sinh OTC (over-the-counter derivatives / 장외파생상품)** cho phép thiết kế payoff theo nhu cầu mà exchange product chuẩn hóa không đáp ứng. Đổi lại, người mua không chỉ mua một “lãi suất cao”: họ đang nhận một gói exposure gồm underlying, option sold/bought, credit của issuer, thanh khoản và điều kiện chấm dứt. Phần này là điểm kết của Sách 3 vì nó buộc người học đọc toàn bộ graph payoff thay vì nhìn coupon.

## 1. OTC bắt đầu từ nhu cầu, không phải từ tên sản phẩm

Exchange derivative có contract size, maturity, tick, clearing và margin chuẩn. OTC derivative bắt đầu từ vị thế và kỳ vọng của khách hàng; dealer định giá, hedge và báo giá riêng. Các bên cần thống nhất underlying, notional, maturity, settlement, collateral, events of default và close-out. Vì vậy rủi ro **counterparty** và **model** lớn hơn: giá không chỉ phụ thuộc thị trường mà còn phụ thuộc assumption volatility, correlation, recovery và liquidity.

Market participants gồm hedger, speculator, arbitrageur, dealer/issuer và end-user. Dealer có thể delta-hedge bằng futures hoặc option, nhưng hedge động không loại bỏ gap risk, transaction cost hay jump risk. Khi một cấu trúc được bán rộng rãi, các dealer có thể cùng mua/bán cùng một underlying, tạo feedback lên thị trường.

## 2. Đọc chứng khoán phái sinh cấu trúc

**Chứng khoán liên kết cổ phiếu/chỉ số (equity-linked security, ELS / 주가연계증권)** liên kết payoff với stock/index; **ELB** (source xếp vào nhóm equity-linked với điều kiện `원금보장`) nhấn mạnh cấu trúc bảo vệ vốn theo điều kiện; **ELF** đóng gói exposure qua fund; **DLS/DLB** (source xếp vào nhóm derivative-linked ngoài equity) dùng underlying ngoài cổ phiếu như rates, FX, commodity hoặc credit. Tên gọi chỉ là nhóm sản phẩm; phải đọc term sheet để biết issuer, maturity, observation dates, coupon, barrier, principal protection và settlement.

Raw source tách tên theo hai lớp, không nên trộn chúng:

| Lớp phân loại | Câu hỏi | Ví dụ cần đọc |
|---|---|---|
| underlying + principal condition | payoff gắn với cổ phiếu/chỉ số hay rate, FX, commodity, credit; có điều kiện bảo toàn vốn hay không? | ELS/ELB cho equity-linked; DLS/DLB cho derivative-linked ngoài equity |
| wrapper phân phối | payoff đó được phát hành dưới dạng security, fund, trust hay deposit? | ELS trực tiếp khác ELF/ELT ở lớp pháp lý, phí, tài sản và cách nhà đầu tư nhận exposure |

### Product-by-product matrix: không đọc acronym thay cho term sheet

Bảng dưới đây là **source-state taxonomy + risk-reading contract**, không phải định nghĩa pháp lý hiện hành. “`원금보장`” trong raw chỉ là nhãn cấu trúc của giáo trình; nó **không** đồng nghĩa government guarantee, deposit insurance hay không có issuer risk.

| Dimension | ELS | ELB | DLS | DLB |
|---|---|---|---|---|
| Underlying | cổ phiếu/chỉ số | cổ phiếu/chỉ số | ít nhất một underlying ngoài equity: rate, FX, commodity, credit, fund, volatility… | như DLS, ngoài equity |
| Wrapper | security/note do issuer phát hành | security/bond-like note theo taxonomy source | security/note | security/bond-like note theo taxonomy source |
| Issuer | chứng khoán/issuer được phép phát hành trong source-state | issuer của note | issuer của note | issuer của note |
| Principal condition | có thể mất principal theo payoff | source gắn nhãn `원금보장`, nhưng vẫn phụ thuộc điều khoản + solvency của issuer | có thể mất principal theo payoff | source gắn nhãn `원금보장`, nhưng không phải bảo lãnh nhà nước |
| Coupon driver | option premium, volatility, correlation, barrier/early-redemption terms, funding | cùng logic option/funding nhưng payoff principal khác | option premium của underlying ngoài equity + funding/model inputs | tương tự DLS với principal condition khác |
| Barrier/path dependence | có thể có worst-of, knock-in/out, autocall, stepdown, no-knock-in… | chỉ tồn tại nếu term sheet quy định; acronym ELB tự nó không nói barrier | có thể có barrier/path condition theo rate/FX/commodity/credit | tương tự, phải đọc term sheet |
| Maturity / early redemption | thường có maturity + observation/autocall dates nếu cấu trúc dùng autocall | theo term sheet | theo term sheet | theo term sheet |
| Liquidity | secondary exit có thể kém, buy-back spread phụ thuộc issuer/market | tương tự | tương tự | tương tự |
| Credit/counterparty | investor là creditor của issuer; hedge counterparty phía sau có thể tạo thêm risk cho issuer | issuer default vẫn là risk dù source gọi `원금보장` | issuer + model/underlying credit nếu payoff liên quan credit | issuer risk vẫn tồn tại |
| Fee/economics | issue spread, sales fee, hedge cost, funding và issuer margin nằm trong economics | tương tự | tương tự | tương tự |
| Tax | **TEXTBOOK/SOURCE STATE**; không suy từ equity tax sang note tax | source-state | source-state | source-state |
| Suitability | loss-tail/path dependence cần stress; source-state suitability rules | vẫn phải đọc disclosure + issuer risk | underlying/model phức tạp có thể làm suitability khó hơn | source-state |

Wrapper là lớp thứ hai. Raw p.352 xác nhận **security → fund → trust → deposit** là các cách đóng gói khác nhau; OCR đủ để đọc rõ ELF ở lớp fund nhưng làm hỏng một số acronym trust/deposit, nên learning edition không tự điền acronym chưa OCR-verified.

| Wrapper | Ai giữ/đóng gói exposure? | Điều thay đổi dù payoff kinh tế có thể giống |
|---|---|---|
| direct security | investor nắm note của issuer | issuer credit, buy-back liquidity, issue spread |
| fund / ELF | fund/manager nắm tài sản/structured exposure | NAV, management fee, redemption/liquidity, asset segregation |
| trust | trustee giữ theo trust contract | legal ownership, fee, withdrawal/valuation convention |
| deposit | bank deposit wrapper trong ví dụ source | deposit terms, bank credit và **quy chế bảo vệ tiền gửi hiện hành phải kiểm tra riêng** |

Trong source-state, “ELB/DLB bảo toàn vốn” chỉ mô tả cấu trúc theo điều kiện và issuer; không nên dịch thành tiền gửi chắc chắn hoặc bỏ qua lạm phát, phí và default của issuer. Cùng một underlying có thể được đóng gói thành security hay fund nhưng tax, liquidity, counterparty và quyền bán sớm có thể khác. Vì vậy acronym là điểm bắt đầu để tìm term sheet, không phải kết luận về rủi ro.

Một ELS thường kết hợp bond-like cash flow với short put hoặc barrier option. Coupon cao hơn tiền gửi là giá của việc nhà đầu tư bán một phần insurance cho issuer: nếu underlying rơi qua **knock-in barrier (Knock In / 낙인)**, principal có thể chịu loss theo underlying; nếu không chạm barrier và thỏa điều kiện, sản phẩm có thể **knock-out (Knock Out / 낙아웃)** sớm và trả coupon đã định. Knock-out không có nghĩa “luôn có lợi”: nó chấm dứt upside tiếp theo và tái đầu tư ở mức lãi mới.

Độ sâu của payoff nằm ở điều kiện chứ không nằm ở tên viết tắt. Với cấu trúc **worst-of (Worst Performer)**, kết quả lấy tài sản kém nhất trong rổ; correlation giữa các tài sản càng thấp thì xác suất có một tài sản rơi sâu càng cao, nên coupon thường được chào cao hơn để bù rủi ro đó. Volatility cao, barrier bất lợi hoặc autocall level cao cũng làm xác suất mất vốn/không được gọi sớm tăng. Ngược lại, coupon cao không phải bằng chứng sản phẩm “rẻ”; nó có thể chỉ là giá thị trường của short barrier option mà nhà đầu tư đang bán.

Trong **autocall stepdown (Autocall Stepdown)**, mức gọi sớm có thể giảm dần qua các ngày quan sát; điều này làm xác suất được gọi sớm thay đổi theo thời gian nhưng không xóa rủi ro đáo hạn. Cấu trúc **no-knock-in (No-Knock In)** loại bỏ một trigger mất vốn cụ thể, nhưng không đồng nghĩa principal được bảo vệ tuyệt đối: issuer default, giá đáo hạn, phí và các điều kiện khác vẫn còn. Luôn phân biệt “không có barrier này” với “không có rủi ro”.

OTC còn cho phép nhiều lớp phụ thuộc mà option chuẩn không có: **Asian/average option** dùng giá bình quân; **barrier option** kích hoạt hoặc vô hiệu khi underlying chạm ngưỡng; **lookback** chọn mức thuận lợi nhất trong lịch sử; **ladder** chốt nhiều bậc strike; **cliquet** điều chỉnh strike theo từng kỳ; **shout** cho phép người mua khóa một trạng thái; **digital** trả khoản cố định khi điều kiện đúng; **Bermudan** chỉ exercise ở các ngày định trước; **chooser** cho phép chọn call hoặc put; **rainbow** chọn tài sản có thành quả tốt nhất; **quanto** dùng underlying nước ngoài nhưng settlement bằng đồng tiền khác; **accrual** tích lũy payoff theo từng observation unit trong suốt thời gian; leverage structure nhân payoff. Mỗi biến thể thêm value cho khách hàng nhưng cũng thêm model risk, liquidity risk và điều kiện khó đọc hơn.

Khi tự đọc một term sheet, hãy chuyển từng điều khoản thành hàm payoff: trigger nào làm quyền được kích hoạt, quyền bị mất lúc nào, và khoản tiền phụ thuộc vào mức giá nào. Với barrier, phải phân biệt chạm trong ngày với chạm tại ngày quan sát; với digital, phải biết khoản trả cố định hay tỷ lệ theo underlying; với Bermudan/chooser, phải ghi rõ các ngày exercise. Những chi tiết này quyết định giá option và không thể khôi phục chỉ từ coupon quảng cáo.

Một số cấu trúc trong nguồn minh họa cách thay đổi đường đi của payoff:

- **Lizard** thêm một cơ hội autocall ở các kỳ đầu, nên có thể kết thúc sớm trước khi cơ chế barrier dài hạn phát huy tác dụng. Người mua đổi một phần upside dài hạn lấy xác suất nhận vốn/coupon sớm hơn.
- **Ejectable** giảm phụ thuộc vào việc tất cả underlying cùng vượt mức gọi: chỉ cần các tài sản lần lượt đáp ứng điều kiện theo lịch, sản phẩm có thể được “đẩy ra” sớm. Nó làm giảm một phần correlation risk nhưng không biến worst-of thành best-of.
- **Swing** gắn payoff với quyền chọn giữa các underlying hoặc trạng thái theo từng kỳ; giá trị phụ thuộc vào correlation, volatility và quyền được chuyển trạng thái, không chỉ vào return cuối kỳ.
- **Daily-rebalanced leverage** reset exposure mỗi ngày. Với return ngày \(+10\%,-9,09\%\), underlying gần như trở lại mức đầu, nhưng sản phẩm 2x có return \(+20\%,-18,18\%\) vẫn mất khoảng 1,8%. Đây là volatility drag, không phải lỗi bảng giá.

Những tên gọi này không thay thế term sheet. Chúng chỉ cho biết nhà thiết kế đã đổi trigger, quyền lựa chọn hoặc tần suất reset; muốn biết ai chịu rủi ro, phải viết lại payoff ở từng nhánh.

Payoff phải viết theo kịch bản, nhưng không được ghép nhánh của hai sản phẩm khác nhau. **Ví dụ 주가연계예금 ở raw p.360** có KOSPI200, maturity 1 năm và knock-out tại mức tăng 20%: nếu barrier +20% bị chạm trong kỳ, source khóa lãi suất ở 3,70%/năm; nếu không chạm và giá đáo hạn nằm trong vùng 100–120% của mức đầu, participation có thể nâng mức lãi tối đa thêm khoảng 0,70 điểm phần trăm; nếu index giảm, raw vẫn mô tả mức 3,70%/năm. Đây là **deposit example/source-state**, không phải ELS loss branch và không phải mức lãi/guarantee hiện hành. Vì vậy barrier ở sản phẩm này giới hạn upside chứ không kích hoạt principal loss.

### Worked check: đọc một autocall stepdown bằng ba đường giá

Giả sử cấu trúc ba năm, coupon niêm yết 8%/năm, quan sát mỗi sáu tháng, mức autocall lần lượt 95%–95%–90%–90%–85%–85% và knock-in barrier 55% của **worst-of**. Nếu cả hai underlying đều trên 95% ở kỳ đầu, sản phẩm có thể trả principal + khoảng 4% cho sáu tháng rồi kết thúc; đó không phải 8% tiền mặt cho nửa năm. Nếu không được gọi sớm nhưng đến đáo hạn worst-of vẫn trên 55% và điều kiện coupon thỏa, tổng coupon có thể là 24% trước thuế cho ba năm. Nếu một underlying kết thúc ở 45% và barrier đã bị chạm, principal có thể chỉ còn khoảng 45% theo điều khoản loss, dù coupon quảng cáo vẫn là 8%/năm. Ba đường giá có cùng coupon nhưng phân phối payoff hoàn toàn khác.

Khi stress case, hãy ghi riêng: xác suất chạm barrier, xác suất autocall, loss-given-barrier, issuer default và giá bán sớm. Không được lấy coupon nhân số năm để gọi đó là expected return; cần xác suất của từng nhánh và chi phí thanh khoản.

## 3. Các bẫy mà coupon che khuất

1. **Principal protection có điều kiện.** “Bảo vệ vốn” thường chỉ đúng nếu issuer không default và barrier/điều kiện không bị kích hoạt; nó không bảo vệ purchasing power hay opportunity cost.
2. **Lợi suất annualized không phải tiền nhận chắc chắn.** Sản phẩm bị knock-out sau sáu tháng với coupon 8%/năm chỉ tạo khoảng 4% trước thuế cho nửa năm; tái đầu tư có thể khác.
3. **Correlation và volatility là input định giá.** Nhà đầu tư nghĩ hai index tương quan cao, issuer dùng correlation thấp, giá option và coupon thay đổi. Đây là disagreement về model, không phải “lãi miễn phí”.
4. **Liquidity và exit price.** Sản phẩm OTC/structured thường khó bán đúng giá lý thuyết trước maturity; issuer spread, hedge cost và market stress làm giá thứ cấp khác payoff cuối kỳ.
5. **Issuer credit.** Dù underlying không giảm, default của issuer vẫn có thể làm người mua không nhận được tiền.

Đọc cả lớp hedge phía sau sản phẩm. **Funded swap (Funded Swap)** chuyển cả dòng vốn cho bên hedge nên quy mô credit exposure lớn hơn; **unfunded swap (Unfunded Swap)** thường chỉ thanh toán phần lãi/lỗ theo hợp đồng. Hai cấu trúc có thể tạo cùng payoff đối với khách hàng nhưng không tạo cùng rủi ro khi dealer hoặc hedge counterparty vỡ nợ. Ngoài ra, phí bán, spread phát hành, chi phí hedge và giá mua lại sớm có thể khiến lợi suất nhìn trên term sheet không bằng lợi suất nhà đầu tư thực nhận.

Ở phía issuer, coupon là kết quả của giá các option đã bán/mua, funding spread, chi phí hedge và biên lợi nhuận phân phối. Nếu issuer dùng volatility cao hơn hoặc correlation thấp hơn trong mô hình, coupon có thể cao hơn nhưng payoff cũng bất lợi hơn cho người mua. Đây là **model disagreement**, không phải arbitrage: người mua chịu rủi ro mô hình, còn issuer phải chịu model risk và hedge slippage khi thị trường nhảy gap. Vì vậy cần tách ba giá: giá lý thuyết, giá phát hành và giá mua lại; chúng có thể khác nhau ngay cả khi underlying chưa đổi.

Nguồn cũng mô tả cơ chế 숙려기간/đánh giá phù hợp cho một số cấu trúc có khả năng mất vốn. Những mốc và điều kiện này là **source-state**; phải kiểm tra quy định và chính sách phân phối hiện hành trước khi dùng làm hướng dẫn giao dịch. Ở cấp độ học tập, nguyên tắc không đổi: sản phẩm càng khó định giá hoặc có lỗ đuôi càng lớn thì càng cần đọc risk disclosure, stress scenario và khả năng chịu lỗ trước khi nhìn coupon.

Có thể đọc quy trình phân phối theo bốn lớp source-state:

| Lớp | Exposure người mua nhận | Điểm phải kiểm tra |
|---|---|---|
| listed futures/options | margin, daily settlement, exchange/clearing rule | education, account/margin requirement, contract specification |
| OTC derivative | payoff tùy biến và counterparty trực tiếp | professional eligibility, collateral, close-out, model valuation |
| structured security | credit của issuer + payoff option nhúng | suitability, disclosure, loss scenario, early redemption |
| fund/trust wrapper | exposure thông qua manager/trustee và tài sản wrapper | NAV, fee, liquidity, tax treatment và quyền rút/bán |

Đây là bản đồ học tập, không phải bảng luật hiện hành. Cùng một payoff kinh tế nhưng đổi wrapper có thể đổi counterparty, cách định giá cuối ngày, phí và thuế. Vì vậy câu “tôi đang mua index” chưa đủ: phải hỏi mình đang sở hữu index, option trên index, note do issuer phát hành hay unit của một fund/trust.

## 4. Thuế và current state

Nguồn dành riêng nhiều trang cho việc phân biệt lợi suất trước thuế, dividend/interest, warrant/derivative và trường hợp principal tưởng như được bảo vệ nhưng thực nhận sau thuế thấp hơn. Đây là **textbook/source state**, không phải tư vấn thuế hiện tại. Luật thuế, cách phân loại sản phẩm, withholding và treatment của từng thị trường thay đổi theo jurisdiction và ngày hiệu lực; trước giao dịch phải đối chiếu cơ quan thuế, sàn/issuer và term sheet snapshot-date. Không suy ra treatment của cổ phiếu từ treatment của ELS hay DLS.

## 5. Checklist đọc term sheet

Trước khi ký, hãy trả lời theo thứ tự:

- underlying là gì, quyền kinh tế nào đang được nhận/bán?
- payoff ở từng vùng giá, từng ngày quan sát và ngày đáo hạn ra sao?
- barrier là knock-in hay knock-out; chạm trong ngày hay chỉ tại ngày quan sát?
- maximum loss, maximum gain, early redemption và settlement currency là gì?
- issuer/counterparty, collateral và khả năng bán sớm thế nào?
- notional, fee, hedge cost, tax và risk disclosure đã tính chưa?

Người học phải giải được câu hỏi nguồn về ELS/ELB/DLS, option terminology, barrier, tax và payoff. Reconstruction test của phần sản phẩm cấu trúc kết thúc ở đây; toàn route còn có integrated case lab để người đọc dựng lại chuỗi **uncertainty → asset exposure → portfolio risk → CAPM return → valuation → derivative hedge/speculation → structured payoff**, đồng thời biết chỗ nào là textbook state cần kiểm tra current rule.
