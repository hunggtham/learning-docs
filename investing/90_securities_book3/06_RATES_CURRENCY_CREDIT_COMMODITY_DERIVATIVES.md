# 6. Phái sinh lãi suất, tiền tệ, tín dụng và hàng hóa

Index products chỉ mới cho thấy một loại market exposure. Chương này dùng cùng một workflow cho bốn underlying khác: xác định dòng tiền nhạy với biến nào, chọn futures/forward/option/swap có payoff đối nghịch, rồi kiểm tra basis, collateral, rollover và counterparty. Đây là nơi các ví dụ hedge của Sách 3 trở thành cơ chế có thể áp dụng.

## 1. Lãi suất: fixed, floating và hướng hedge

Lãi suất bản thân không phải một tài sản giao dịch như cổ phiếu; nó được suy ra từ giá trái phiếu và yield của một maturity cụ thể. Vì yield thay đổi làm giá trái phiếu đổi ngược chiều, người sở hữu tài sản fixed-rate chịu lỗ khi rates tăng. Người vay floating-rate cũng chịu lỗ khi rates tăng vì interest expense tăng.

Các công cụ chính:

- **interest-rate futures/forwards (금리선물·금리선도)** khóa mức yield hoặc giá;
- payer swap trả fixed, nhận floating, có lợi khi rates tăng;
- receiver swap trả floating, nhận fixed, có lợi khi rates giảm;
- rate options giữ quyền hưởng lợi khi scenario xảy ra nhưng trả premium.

Nguồn phân biệt **strip hedge (스트립헤지)** — dùng nhiều maturity khớp từng cash flow tương lai — với **stack hedge (스택헤지)** — dùng nearby contract rồi roll sang kỳ sau. Strip giảm mismatch maturity nhưng thanh khoản có thể hạn chế; stack dễ giao dịch hơn nhưng rollover/basis risk lớn hơn. Vì vậy “hedge lãi suất” không nói đủ; phải ghi rõ tài sản, kỳ hạn và dấu exposure.

Ví dụ, một doanh nghiệp trả lãi theo SOFR/KORIBOR sáu tháng một lần sẽ bị lỗ khi reference rate tăng. **Payer swap (고정금리 지급·변동금리 수취)** đổi dòng floating thành fixed nên làm chi phí dự toán ổn định; **receiver swap (고정금리 수취·변동금리 지급)** lại phù hợp người đang nhận floating và muốn khóa mức nhận. **Cap (캡)** mua quyền chỉ trả khi rate vượt strike, **floor (플로어)** trả khi rate xuống dưới strike, còn **collar (칼라)** mua một quyền và bán quyền kia để giảm premium. Cap/floor giới hạn rủi ro nhưng không làm mất basis giữa reference rate trong hợp đồng và chi phí vay thực tế. Với trái phiếu, cần ghép duration và key-rate exposure chứ không chỉ ghép tổng notional.

**Swaption (swap option / Swaption)** thêm quyền lựa chọn vào swap: payer swaption cho quyền bước vào swap trả fixed/nhận floating, phù hợp doanh nghiệp sợ lãi suất tăng nhưng chưa chắc khoản vay sẽ phát sinh; receiver swaption cho quyền nhận fixed/trả floating, phù hợp người sợ lãi giảm trên tài sản floating. Người mua trả premium để giữ quyền không thực hiện nếu scenario không xảy ra. Vì vậy swaption bảo vệ flexibility tốt hơn forward/swap bắt buộc, nhưng chi phí upfront và implied volatility làm giá hedge tăng.

### Worked check: cap, floor và collar biến dòng tiền ra sao

Một doanh nghiệp có khoản vay floating và mua cap strike 5%. Nếu reference rate lên 7%, khoản vay chịu 7% nhưng cap trả phần chênh 2%, nên chi phí lãi ròng gần 5% trước premium và basis. Nếu rate chỉ 3%, cap không trả và doanh nghiệp vẫn hưởng lợi từ rate thấp. Ngược lại, người sở hữu tài sản floating mua floor strike 2%: nếu rate rơi xuống 1%, floor trả thêm 1% để dòng thu nhập gần 2%.

Nếu doanh nghiệp muốn giới hạn cả hai phía trong vùng 2–5%, có thể mua cap và bán floor/call đối ứng để giảm premium, tạo **collar**. Đổi lại, khi rate giảm dưới 2%, quyền đã bán khiến doanh nghiệp không hưởng toàn bộ lợi ích. Collar là cách đổi convexity lấy chi phí thấp hơn; không phải bảo hiểm miễn phí.

Với một trái phiếu, xấp xỉ nhạy cảm giá là \(\Delta P/P\approx-D_{mod}\Delta y\). Ở đây \(D_{mod}\) đo theo năm, \(\Delta y\) là thay đổi yield ở dạng thập phân và \(\Delta P/P\) là tỷ lệ đổi giá; đây là xấp xỉ tuyến tính cho biến động yield nhỏ và bỏ qua convexity. Khi yield move lớn hoặc cash flow có option, sai số tuyến tính có thể đáng kể. Giả sử danh mục trái phiếu 10 tỷ có modified duration 5; yield tăng 0,5 điểm phần trăm thì giá giảm gần \(5\times0,005=2,5\%\), tức khoảng 250 triệu trước convexity. **BPV/DV01** là thay đổi giá tiền khi yield đổi 1 basis point; danh mục này có DV01 xấp xỉ \(10\text{ tỷ}\times5\times0,0001=5\) triệu đồng/bp. Nếu một hợp đồng futures giả định có DV01 1,6 triệu đồng/bp, hedge lý thuyết cần short khoảng 3,1 hợp đồng. Làm tròn hợp đồng, khác key-rate và convexity tạo residual risk; không được hedge duration bằng cách chỉ chia notional. **Duration (듀레이션)** có trong raw source; nhãn **BPV/DV01** và phép minh họa chi tiết ở đây là enrichment để biến cơ chế hedge duration thành công thức thực hành, không phải thuật ngữ nguyên văn của source Book 3.

**Hợp đồng lãi suất kỳ hạn (forward rate agreement/interest-rate forward; source dùng 금리선도계약, thường gọi FRA)** là cách khóa một lãi suất cho một khoảng thời gian tương lai: nó loại bỏ rủi ro lãi tăng nhưng cũng từ bỏ lợi ích nếu lãi giảm. **IFR (내재선도금리)** là một mốc no-arbitrage suy ra từ các lãi suất zero/spot: gọi là mốc kiểm tra giá, không phải forecast kinh tế. Nếu forward thị trường khác mốc này, cần xem xét credit spread, collateral, compounding và liquidity trước khi suy ra arbitrage.

### Worked check: suy ra IFR từ hai lãi suất hiện tại

Giả sử lãi suất đơn giản một năm là 4%, còn lãi suất 9 tháng là 3%. Lãi suất 3 tháng bắt đầu từ tháng thứ 9, ký hiệu \(f_{9m,3m}\), phải thỏa:

\[
1+0,04=(1+0,03\times0,75)(1+f_{9m,3m}\times0,25).
\]

Trong phương trình trên, các rate là annualized simple rates; 0,75 và 0,25 là year fractions, còn \(f_{9m,3m}\) là forward rate cho ba tháng bắt đầu sau chín tháng. Equality là no-arbitrage giữa hai chiến lược gửi tiền cùng horizon; đổi compounding/day-count thì phương trình phải đổi.

Suy ra \(f_{9m,3m}\approx6,85\%\) annualized theo quy ước đơn giản. Đây là rate làm cho gửi một năm ngay hôm nay tương đương gửi 9 tháng rồi tái đầu tư 3 tháng; nó không nói nền kinh tế chắc chắn sẽ có lãi suất 6,85% sau 9 tháng. Nếu dùng compounding khác, day-count khác hoặc có credit spread, con số phải được điều chỉnh.

**Source wording note:** raw p.293 mở rộng IFR thành “Internal Forward Rate”, trong khi câu hỏi tổng hợp p.373 dùng “Implied Forward Rate”; cơ chế và ký hiệu đều chỉ forward rate suy ra từ term structure. Vì source tự không nhất quán ở phần English expansion, learning edition giữ acronym **IFR** + Korean **내재선도금리**, và audit đánh exact English expansion là `SOURCE_AMBIGUITY` thay vì tự chọn một wording rồi gọi là source fidelity.

Với futures lãi suất, phải đọc cả cơ chế settlement. **Cash settlement** chỉ chuyển phần chênh lệch giá; **physical delivery** yêu cầu bên short chọn một trái phiếu đủ điều kiện để giao. Khi underlying là “trái phiếu chuẩn” giả định, rổ giao thực tế có thể có nhiều bond với coupon và maturity khác nhau; bên giao thường tìm **trái phiếu giao rẻ nhất (cheapest-to-deliver, CTD / 최저인도가채권)** và dùng conversion factor để quy đổi. Vì vậy giá futures, hedge duration và basis của trái phiếu thực không thể đọc như một hợp đồng duy nhất; CTD và option giao hàng tạo thêm rủi ro mô hình.

Hedge cũng có thể là **phòng hộ chéo (cross-hedge / 교차헤지)**: doanh nghiệp giữ corporate bond nhưng dùng government-bond futures. Hai yield không di chuyển giống nhau vì credit spread, nên DV01 khớp chưa đủ; residual risk là thay đổi spread và correlation. Tương tự, một bảo hiểm có nợ dài hạn nhưng chỉ nắm tài sản ngắn hạn có thể dùng receiver swap để kéo dài duration; swap thay đổi exposure nhưng không thay thế asset-liability matching.

### Worked check: hedge chỉ bù đúng exposure đã viết ra

Một khoản vay floating 1 tỷ đồng có lãi suất từ 5% tăng lên 7% trong một năm sẽ làm chi phí tăng khoảng 20 triệu đồng trước khi xét ngày reset. Nếu payer swap cố định ở 5,5%, phần tăng từ 5,5% đến 7% được bù gần đúng trên notional swap; nhưng nếu khoản vay reset theo một benchmark khác, kỳ hạn không khớp hoặc notional giảm giữa kỳ, doanh nghiệp vẫn còn basis/mismatch risk. Con số 20 triệu là exposure cần bảo vệ, không phải bằng chứng swap chắc chắn tạo lợi nhuận.

## 2. Tiền tệ: forward, futures, option và swap

Exporter sẽ nhận USD trong tương lai và sợ USD giảm so với KRW/VND; importer phải trả USD và sợ USD tăng. Forward/futures khóa tỷ giá nên giảm uncertainty nhưng bỏ mất upside. Option cho phép giữ upside: exporter mua put USD để đặt sàn, importer mua call USD để đặt trần. Currency swap trao đổi principal/interest theo hai đồng tiền và phù hợp exposure dài hơn, nhưng kéo theo counterparty và basis.

Quy tắc dấu đơn giản: vẽ cash flow nội tệ trước. Nếu doanh thu ngoại tệ giảm khi foreign currency giảm, vị thế kinh tế là long foreign currency và hedge bằng bán forward hoặc mua put. Nếu nghĩa vụ thanh toán ngoại tệ tăng khi foreign currency tăng, hedge bằng mua forward hoặc call. Không chọn công cụ chỉ từ tên “import/export”; hãy bắt đầu từ dấu delta của dòng tiền.

**Ngang giá lãi suất (interest-rate parity / 이자율 평형)** cho ta một mốc kiểm tra forward, không phải dự báo tỷ giá. Với quy ước spot \(S_0\) = nội tệ trên 1 USD, công thức đơn giản là \(F_0=S_0(1+r_dT)/(1+r_fT)\), trong đó \(r_d\) là lãi nội tệ, \(r_f\) là lãi ngoại tệ và \(T\) là year fraction. Công thức giả định cùng credit/collateral convention và khả năng vay–cho vay hai đồng tiền; capital control, basis, bid–ask và funding khác nhau có thể làm forward thực tế lệch. Với spot 1.000 nội tệ/USD, lãi suất nội tệ 4%, lãi suất USD 2% và kỳ hạn một năm, forward đơn giản là \(1.000\times1,04/1,02\approx1.019,6\). Nếu báo giá lệch đáng kể, phải kiểm tra bid–ask, credit line, capital control, ngày thanh toán và compounding trước khi gọi đó là arbitrage. Chênh lệch lãi suất làm thay đổi forward points; nó không đảm bảo USD sẽ thực tế tăng đúng 1,96%.

**NDF (Non-Deliverable Forward)** — source mô tả là `실물인수도` 없이 `매매차액`을 `현금결제`하는 선도거래 — là forward cash-settled: không giao đồng tiền hạn chế chuyển đổi mà thanh toán chênh lệch theo fixing. Nó hữu ích khi thị trường deliverable kém thanh khoản, nhưng vẫn là OTC nên có counterparty, fixing, collateral và basis risk. **FX margin (FX 마진)** có thể trông như “không phí” vì nhà cung cấp kiếm từ bid–ask và financing; đòn bẩy thấp margin làm lỗ trên notional rất lớn, còn counterparty và gap risk vẫn tồn tại. Đây là source-state về cơ chế, không phải thông số hay khuyến nghị giao dịch hiện hành.

Forward khóa tỷ giá nhưng tạo obligation và counterparty exposure; option trả premium để đổi lấy quyền bỏ giao dịch khi tỷ giá đi theo hướng có lợi. Vì vậy một “zero-cost collar” không miễn phí theo nghĩa rủi ro: premium mua put/call được bù bằng việc bán quyền ở strike khác, làm upside hoặc downside bị cắt. KIKO trong nguồn là cảnh báo cụ thể: doanh nghiệp tưởng đang giới hạn biên độ nhưng việc bán call knock-out/knock-in có thể làm lỗ tăng mạnh khi đồng nội tệ mất giá. Đây là textbook case, không phải khuyến nghị thiết kế sản phẩm hiện tại.

Ví dụ một exporter phải thu 1 triệu USD có thể bán forward ở 1.300 nội tệ/USD để khóa 1,3 tỷ nội tệ. Nếu spot đáo hạn chỉ còn 1.200, forward bù phần giảm so với việc bán USD ở spot; nếu spot tăng lên 1.400, doanh nghiệp vẫn chỉ nhận mức đã khóa. Mua put thay cho forward giữ upside nhưng phải trả premium. Câu hỏi đúng không phải “công cụ nào lời hơn”, mà là doanh nghiệp muốn chắc chắn ngân sách hay muốn giữ convexity.

**Range forward (범위 선물환)** ghép long put ở 1.110 với short call ở 1.130 cho exporter. Nếu tỷ giá đáo hạn nằm trong vùng, doanh nghiệp còn hưởng biến động spot; dưới 1.110, put đặt sàn; trên 1.130, short call cắt upside. Chọn strike sao cho premium hai quyền gần bù nhau tạo cảm giác “không tốn phí”, nhưng chi phí thật là mất một phần convexity và nhận nghĩa vụ khi tỷ giá vượt biên. Cấu trúc này chỉ là collar có tên khác; không được đọc nó như một forward miễn phí.

### KIKO/zero-cost FX option: đọc theo nhánh payoff

Một KIKO minh họa trong raw có thể bắt đầu bằng nhu cầu exporter muốn bảo vệ tỷ giá giảm. Doanh nghiệp mua put để đặt sàn nhưng bán call ở vùng cao nhằm bù premium; nếu chỉ nhìn vùng tỷ giá bình thường, giao dịch có vẻ gần như không tốn tiền. Khi tỷ giá vượt upper barrier, short call bị kích hoạt hoặc notional bị khuếch đại theo điều khoản; lúc đó doanh nghiệp không còn chỉ “bỏ upside” mà có thể phát sinh nghĩa vụ lớn hơn khoản phải thu.

Hãy vẽ ba nhánh trước khi ký: (1) tỷ giá nằm trong range—premium gần bù nhau; (2) tỷ giá giảm—put bảo vệ sàn; (3) tỷ giá tăng vượt barrier—short call và multiplier tạo loss tail. Nhánh (3) phải được tính trên notional option, không chỉ trên doanh thu USD thật. Đây là textbook warning từ KIKO 2008, không phải mẫu hợp đồng hay khuyến nghị hiện hành.

## 3. Phái sinh tín dụng (credit derivatives / 신용파생상품) và cash/synthetic securitization

**Credit default swap (CDS)** tách **rủi ro tín dụng (credit risk / 신용위험)** khỏi bond: protection buyer trả premium định kỳ; protection seller bồi thường khi credit event của reference entity xảy ra. Buyer hedge default risk nhưng chịu premium và counterparty risk; seller nhận carry nhưng gánh tail loss. CDS không biến nợ xấu thành an toàn.

CDS còn có **basis risk**: spread CDS, spread trái phiếu và loss thực tế không nhất thiết di chuyển đồng nhất; protection cũng chỉ trả theo reference entity và credit-event definition trong hợp đồng. Với cash securitization, người mua chịu waterfall, prepayment và credit enhancement của pool thật. Với synthetic structure, exposure được chuyển bằng swap nên không cần chuyển toàn bộ tài sản; notional có thể lớn hơn pool vật lý và nhiều bên cùng phụ thuộc một reference entity. Khi stress, collateral, close-out và wrong-way risk có thể làm seller không trả được đúng lúc.

Raw source còn phân biệt ba cách đóng gói credit exposure. **TRS (total return swap)** chuyển coupon và lãi/lỗ giá của reference bond cho counterparty, đổi lại holder nhận một dòng tiền thỏa thuận như government yield + spread; credit risk của bond được đổi thành counterparty risk. **CLN (credit-linked note)** làm điều ngược với protection buyer: người mua nhận thêm spread vì đang bán protection; nếu credit event xảy ra, principal có thể chịu loss lớn. **CDS** là quyền bảo hiểm riêng, TRS là trao đổi toàn bộ total return, còn CLN là security đã nhúng short-credit-option. Ba cái cùng liên quan credit nhưng không thể dùng tên thay cho payoff.

| Vị thế | Dòng tiền thường nhận/trả | Rủi ro chính |
|---|---|---|
| CDS protection buyer | trả spread; nhận bồi thường khi credit event | premium, basis, counterparty, definition của event |
| TRS receiver of financing leg | trả total return của bond; nhận funding rate + spread | mất upside/coupon của bond, counterparty và funding |
| CLN buyer | nhận coupon cao hơn vì bán protection nhúng trong note | principal loss, issuer default, thanh khoản thứ cấp |

Bảng này giải thích vì sao câu “đã hedge credit risk” chưa đủ: CDS có thể hedge default nhưng vẫn còn basis; TRS chuyển toàn bộ total return; CLN biến short-credit exposure thành security mà nhà đầu tư có thể đánh giá thấp vì coupon được trả đều.

CDS spread phải đọc như chi phí bảo hiểm hàng năm trên notional, không phải xác suất default thuần túy. Ví dụ textbook 3.000 bp/năm tương đương khoảng 30% notional mỗi năm trước recovery, accrual, restructuring và liquidity; mức spread cao có thể phản ánh recovery thấp, funding/counterparty risk hoặc premium thanh khoản chứ không chỉ một xác suất đơn giản. Historical examples trong raw là source-state để hiểu cơ chế, không phải quote hiện hành.

Với cách viết đơn giản, **loss given default (LGD)** là \(LGD=1-R\) với \(R\) là recovery rate, và khoản protection gộp xấp xỉ \(N\times LGD\) trên notional \(N\). Nếu CDS notional là 100 triệu và spread danh nghĩa 300 điểm cơ bản/năm, premium đơn giản hóa là khoảng 3 triệu/năm; nếu credit event dẫn tới recovery 40%, khoản bồi thường gộp theo loss-given-default khoảng 60 triệu trước settlement convention. Đây chỉ là minh họa cơ chế: premium thực tế phụ thuộc schedule, accrued premium, restructuring definition, collateral và recovery market. Công thức LGD trên chỉ mô tả loss leg; CDS fair spread còn phụ thuộc xác suất default theo thời gian, discounting và premium leg.

Sách 3 phân biệt **cash** và **synthetic securitization (현금형·합성형 증권화)**. Cash structure mua pool tài sản thật rồi phát hành claims; synthetic chuyển credit exposure bằng derivatives mà không nhất thiết mua tài sản cơ sở. Raw p.320 phân biệt pooled debt/loan/bond obligations, nhưng OCR làm hỏng ít nhất một acronym: token cho debt obligation hiện ra như “Coo”, còn **CLO** đọc rõ. Vì vậy learning edition dùng nhãn chuẩn **CDO/CLO** để nối cơ chế, nhưng audit không coi exact acronym “CDO” ở p.320 là OCR-verified; unit đó được đánh `SOURCE_AMBIGUITY` cho wording, trong khi distinction cash-vs-synthetic và pooled-loan CLO vẫn được xác nhận.

CDO gom debt, CLO gom loan, còn cấu trúc synthetic có thể tạo notional lớn hơn tài sản vật lý và khuếch đại interconnectedness. Bài học 2008 trong nguồn là boundary: một hợp đồng bảo hiểm tín dụng có thể phân phối rủi ro, nhưng không làm tổng default risk biến mất.

## 4. Hàng hóa: contango, backwardation và roll yield

Commodity futures cho phép đầu tư vào gold, corn, copper, crude oil, natural gas mà không phải nhận và lưu kho hàng thật. Giá futures gồm spot/carry, **chi phí lưu kho (storage cost / 보관비용)**, financing và **convenience yield (편의수익)**; vì thế futures return không đồng nhất với spot return.

Vì commodity futures thường gắn với physical delivery, giá có thể trở nên âm khi bên long không còn kho chứa hoặc khả năng nhận hàng trước ngày giao. Giá âm trong textbook case không có nghĩa “tài sản luôn vô giá trị”; nó có thể phản ánh bên giữ hàng phải trả cả chi phí xử lý, vận chuyển và lưu trữ để người khác nhận hàng. Đây là khác biệt của commodity futures so với một chỉ số tài chính cash-settled, và là lý do phải biết first notice/last trade date trước khi roll.

Raw đưa công thức carry đơn giản cho commodity futures: \(F\approx S+S(r+s-c)T\), với \(S\) là spot, \(r\) funding rate, \(s\) storage-cost rate, \(c\) convenience yield và \(T\) là thời gian đến maturity. Các rate phải cùng kỳ/scale; convenience yield thường không quan sát trực tiếp nên đây là valuation relation, không phải forecast. Khi inventory constraint, seasonality, delivery option hoặc storage nonlinear, mô hình đơn giản có thể lệch đáng kể.

**Contango (콘탱고)** là futures xa kỳ hạn cao hơn gần kỳ hạn; khi nhà đầu tư long phải roll từ hợp đồng sắp đáo hạn sang hợp đồng đắt hơn, roll yield thường âm. **Backwardation (백워데이션)** ngược lại có thể tạo roll yield dương cho long. Đây là lý do giá dầu đi ngang nhưng ETF futures vẫn lỗ hoặc lời qua thời gian. Hợp đồng xa kỳ hạn còn có liquidity và basis khác nhau; không được suy ra kết quả dài hạn từ một chart spot.

**Giao dịch thương mại (commercial / 상업적 거래)** hedge dùng futures để ổn định biên lợi nhuận: hãng nhập corn có thể long corn futures để bù giá nguyên liệu tăng; producer có thể short để khóa giá bán. Nếu thời điểm, grade, location hoặc quantity không khớp, phần chênh còn lại là basis risk. Speculator nhận rủi ro ấy để cung cấp thanh khoản và kỳ vọng kiếm return.

Thị trường phân biệt **commercial (상업적 거래)** (có nhu cầu vật chất hoặc cash-flow thật cần hedge) với **non-commercial (비상업적 거래)** (chủ yếu tìm exposure/return). Với một position được roll, có thể viết schematic \(R_{total}\approx R_{price}+R_{roll}+R_{collateral}-fees\). Đây là decomposition kinh tế; cách index provider định nghĩa excess/total return có thể khác theo convention. tổng return nên tách thành price return, roll return và collateral/interest return; “excess return” thường chỉ phần price + roll, còn total return cộng thêm collateral. Vì vậy một commodity index có thể lỗ dù chart spot đi ngang, hoặc có lãi khi roll yield và collateral bù được spot yếu.

Raw có một phép tính cảnh báo về leverage: nếu một hợp đồng gold có notional minh họa khoảng 242 triệu đồng nhưng margin khoảng 8,8 triệu, biến động 3,7% trên notional tạo lãi/lỗ gần 9 triệu—xấp xỉ toàn bộ margin. Các con số này là **source-state minh họa**, không phải thông số hợp đồng hiện hành; điều cần học là phải đo rủi ro theo notional và price move, không theo số tiền ký quỹ. Nếu thêm FX conversion, spread và daily settlement, áp lực thanh khoản còn lớn hơn con số payoff cuối kỳ.

### Commodity trong asset allocation và global hedge

Raw source không coi commodity chỉ là một trade riêng lẻ. Nhà đầu tư có thể thêm commodity exposure vào portfolio vì correlation lịch sử với cổ phiếu từng thấp, nhưng correlation thay đổi theo lạm phát, dollar, chiến tranh, lãi suất và chính cấu trúc futures curve. Do đó commodity có thể giảm portfolio risk trong một giai đoạn rồi cùng giảm với equities trong stress khác.

“Global hedge” cũng phải viết thành exposure cụ thể: long gold có thể hedge một số lo ngại lạm phát hoặc currency debasement; long energy có thể bù một phần chi phí đầu vào; long USD futures có thể bù doanh thu ngoại tệ. Nhưng mỗi vị thế còn có roll, margin, FX, liquidity và basis risk. Index fund commodity giúp phân tán theo nhiều hợp đồng nhưng không xóa contango; quy tắc roll của index phải được đọc như một phần payoff.

Đường cong futures có thể dốc vì lãi suất, storage cost, convenience yield và kỳ vọng cung cầu; không nên gọi mọi contango là “thị trường bearish”. Với ETF/ETN roll định kỳ, return gần đúng là spot return + collateral return + roll yield − phí, nhưng tỷ trọng và lịch roll phải đọc từ prospectus. Một hedge hàng hóa cũng có thể thất bại khi grade/location khác (cross-hedge), hoặc khi doanh nghiệp cần giao hàng trước ngày hợp đồng thanh khoản nhất.

Ví dụ, long một hợp đồng gần đáo hạn ở 100 rồi phải roll sang hợp đồng cùng quy mô ở 105 tạo roll loss 5 đơn vị ngay cả khi spot vẫn quanh 100. Nếu đường cong chuyển sang backwardation và hợp đồng mới chỉ 96, roll yield có thể dương cho long. Đây là return của việc thay hợp đồng, không phải dự báo rằng giá hàng hóa giao ngay chắc chắn tăng hay giảm.

Worked example từ raw: mua March ở 81, bán trước đáo hạn ở 82, rồi mua June ở 83 và bán June ở 84. Lãi giao dịch từng hợp đồng là \((82-81)+(84-83)=2\). Nhưng nếu chỉ nhìn giá gần tháng từ 81 lên 84, có vẻ return là 3; phần chênh 1 bị mất khi roll từ 82 sang 83. Total return còn phải cộng collateral interest và trừ fee/margin cost. Đây là lý do chart continuous futures cần đọc cùng quy tắc roll, không thể coi nó là spot price kéo dài.

## 5. Bảng quyết định exposure

| Exposure kinh tế | Rủi ro chính | Công cụ thường dùng | Chi phí/giới hạn |
|---|---|---|---|
| khoản vay floating | rate tăng | payer swap, long rate option | premium, basis, collateral |
| tài sản fixed-rate | rate tăng làm giá giảm | rate futures short, payer hedge | mismatch duration, roll |
| phải thu USD | USD giảm | sell forward, USD put | mất upside, counterparty |
| phải trả USD | USD tăng | buy forward, USD call | premium hoặc khóa giá |
| trái phiếu reference | default/spread widening | buy CDS protection | premium, counterparty, basis |
| mua nguyên liệu | spot tăng | long futures/call | basis, roll, margin |

Source-question test yêu cầu chọn đúng chiều hedge, phân biệt strip/stack, giải thích CDS protection, cash/synthetic và tác động contango/backwardation. Bàn giao sang OTC: cùng payoff ấy có thể được đóng gói tùy biến trong một security, nhưng khi mất chuẩn hóa, ta phải đọc thêm issuer, liquidity, knock-in/out, tax và disclosure.

Một bài tự kiểm tra đầy đủ phải trả lời được: (i) ai đang long duration, long USD hay short commodity; (ii) cash flow nào được bảo vệ và cash flow nào vẫn mở; (iii) phần lỗ đến từ basis, roll, margin hay counterparty; và (iv) hedge có làm thay đổi lợi nhuận kỳ vọng hay chỉ làm giảm phương sai. Nếu không trả lời được bốn câu này, việc gọi một vị thế là “hedge” vẫn còn quá sớm.
