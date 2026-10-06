# Đánh giá chất lượng — Sách 3

## Kết luận hiện tại

Bản route trước đã đạt mức **foundation pass**: architecture theo dependency đúng, raw OCR đã được tái tạo, 19 semantic rows có target lesson, link nội bộ sạch và không duplicate cả thư viện `investing/`. Tuy nhiên chưa nên gọi là learning edition hoàn chỉnh theo chuẩn “dễ hiểu hơn nhưng không biết ít hơn”. Với 381 trang nguồn và khoảng 7.600 từ lesson, bản cũ còn nén quá mạnh các cơ chế mà câu hỏi nguồn yêu cầu tính hoặc phân biệt.

## Gap audit trước khi update

| Khu vực | Vấn đề | Mức độ | Cách sửa |
|---|---|---:|---|
| Statistics | Có công thức nền nhưng thiếu geometric/harmonic mean, cách đọc sai số và assumptions của hồi quy | P1 | Bổ sung ví dụ và boundary |
| Portfolio | Chưa dẫn đủ từ correlation cases → minimum variance → efficient frontier → CAL | P0 | Thêm đạo hàm/trực giác và bài số |
| CAPM/EMH | Có CML/SML nhưng nén price adjustment, equilibrium và test matrix | P0 | Thêm cơ chế định giá và kiểm định |
| Performance/valuation | FCFF/FCFE, WACC, terminal value, EVA và multiple procedure còn quá ngắn | P0 | Thêm mô hình nhất quán và counter-example |
| Derivatives foundation | Thiếu zero-sum, long/short, ITM/ATM/OTM, daily settlement, financial-institution use | P0 | Mở rộng lesson 05 |
| Rates/FX/credit/commodity | Chưa có case hedge theo dấu exposure và cash/synthetic/CDS đủ chi tiết | P0 | Thêm payoff/sign table và roll/basis |
| OTC/structured | Có taxonomy nhưng thiếu coupon drivers, investor suitability, KIKO/no-knock-in, fees/tax | P0 | Thêm term-sheet walkthrough |
| QA | Coverage status “FULL” cần kiểm tra lại sau khi mở rộng | P1 | Chạy link/whitespace/keyword/source-question audit lại |

## Nguyên tắc update

Update này giữ canonical ownership hiện tại. Phần nào đã có owner sâu hơn trong `investing/` chỉ nhận learning bridge; phần nào Sách 3 dạy riêng (CAPM, Markowitz, derivative payoff, Korean structured products) được mở rộng tại route này. Claims về thuế, margin, luật và product rules vẫn là source-state và phải xác minh theo snapshot chính thức trước giao dịch.

## Verdict sau đợt đào sâu 2026-10-04

Bảy lesson đã được cập nhật theo gap audit: portfolio có các trường hợp tương quan và MVP; CAPM/EMH có cơ chế price adjustment và ma trận kiểm định; valuation có FCFF/FCFE, WACC, terminal value và quy trình multiples; phái sinh có zero-sum, ITM/ATM/OTM, mark-to-market và margin call; các lesson 06–07 có sign hedge, cap/floor, CDS basis, roll yield, coupon drivers, worst-of, funded/unfunded swap và phí/điều kiện sản phẩm.

Verdict hiện tại: **deepening pass cho learning route, chưa phải bản xuất bản cuối**. Nội dung đã đủ để thay thế bản tóm tắt mỏng và cho phép người học dựng lại cơ chế, nhưng các claim về thuế, margin, 숙려기간, contract specification và suitability vẫn phải được snapshot-check nếu dùng cho giao dịch thực tế. Raw OCR vẫn là provenance; những bảng/hình bị lỗi OCR chưa được coi là dữ kiện mới.

## Worked-example audit sau đợt cập nhật tiếp theo

Đợt này bổ sung các phép kiểm tra có số cho covariance/correlation, MVP, abnormal return, DCF terminal value, futures basis, option P&L, rate/FX hedge, CDS loss-given-default, commodity roll yield và autocall stepdown. Trong quá trình kiểm tra đã sửa một lỗi nội dung ở lesson 02: với \(\sigma_A=12\%\), \(\sigma_B=7\%\), \(\rho=0,5\), trọng số MVP của A là khoảng 0,064 (không phải 0,64); độ lệch chuẩn 6,97% mới là kết quả đúng.

Verdict mới: **learning-depth pass** cho các khái niệm và cơ chế chính; tám lesson hiện có 17.921 từ. Vẫn **chưa phải publication pass** vì nguồn OCR còn bảng/hình không đọc chắc chắn và các claim hiện hành cần nguồn chính thức theo ngày hiệu lực. Tài liệu hiện đã có thể dùng để học, tính lại và stress-test các cơ chế, thay vì chỉ đọc tóm tắt.

Integrated case lab bổ sung reconstruction layer chứ không tạo thêm semantic source claim: nó dùng lại CAPM, DCF, futures và structured-product mechanics trong một quyết định duy nhất, có sensitivity và hedge residual risk. Vì vậy coverage nguồn vẫn giữ 19 semantic rows; case được xem là learning synthesis/assessment layer.

Đợt đào sâu kế tiếp bổ sung harmonic-mean example, expected-utility comparison, dynamic delta/gamma hedge và các boundary về việc hedge theo đường đi của giá. Đây là các phần nguồn thường bị rút thành định nghĩa; hiện đã có số liệu để người học kiểm tra lại bằng tay.

Audit tiếp tục xác nhận ba điểm còn thiếu đã được xử lý: (1) duration/BPV và hedge theo DV01 thay cho chia notional đơn giản; (2) interest-rate parity được trình bày như mốc kiểm tra forward, không phải dự báo tỷ giá; (3) Black–Scholes và implied volatility được đặt trong đúng boundary về volatility surface, early exercise, jump và transaction cost.

Batch hiện tại bổ sung thêm downside deviation, frontier có constraint/no-short, worked comparison của Sharpe–Treynor–Jensen, calendar spread futures và range-forward FX. Những phần này làm rõ câu hỏi mà mỗi công thức trả lời và tránh biến một cấu trúc hedge thành tuyên bố “an toàn” chung chung.

Đợt audit tiếp theo sửa một cách diễn đạt dễ gây hiểu sai: basis dương/âm không đồng nhất tuyệt đối với contango/backwardation; basis còn bao gồm carry, dividend, storage và convenience yield. Đồng thời bổ sung EV-to-equity bridge và ba bias chính trong kiểm định EMH: survivorship, look-ahead và multiple testing.

Structured-product audit tiếp tục bổ sung Lizard, Ejectable, Swing và daily-rebalanced leverage, cùng phần economics phía issuer (model inputs, funding spread, hedge slippage, giá phát hành và giá mua lại). Đây là phần cần thiết để người học không đánh đồng coupon với expected return hoặc gọi mọi cấu trúc barrier là cùng một sản phẩm.

Đợt trích xuất trực tiếp từ raw Markdown tiếp theo bổ sung cho derivatives lesson: delta-neutral/put–call parity, simulation và liquidity boundary của option; FRA/IFR, cross-hedge và asset-liability matching của rate products. Các điểm này được ghi vào coverage như source-derived additions, không phải kiến thức chèn ngoài phạm vi Sách 3.

Batch mới bổ sung thêm cash/physical settlement và CTD của interest-rate futures, cùng NDF và FX margin. Các khái niệm này được giữ ở mức cơ chế và source-state; không đưa thông số hợp đồng hiện hành vào learning prose.

Raw extraction mới nhất bổ sung TRS/CLN và phân biệt chúng với CDS; giải thích credit spread lớn như phí bảo hiểm có recovery/liquidity component; đồng thời đưa vào commodity lesson physical-delivery/negative-price boundary, commercial vs non-commercial flow và price–roll–collateral total-return decomposition.

Derivatives foundation tiếp tục nhận thêm covered call và short strangle từ raw: payoff được tính ở vùng giữa và hai tail, để người học thấy premium income hữu hạn không bù được lỗ mở rộng khi underlying vượt strike.

Structured-product extraction bổ sung taxonomy hai lớp: underlying/principal condition (ELS, ELB, DLS, DLB) và wrapper phân phối (security, fund, trust, deposit). Lesson giữ đây là source-state để người học không suy ra “bảo toàn vốn” hay tax/liquidity chỉ từ acronym.

Valuation extraction bổ sung worked EVA case: cùng một tăng trưởng doanh thu có thể tạo giá trị hoặc phá hủy giá trị tùy ROIC biên có vượt WACC hay không.

Credit/commodity extraction bổ sung bảng payoff CDS–TRS–CLN và worked roll-return từ raw (price return khác continuous-futures return). Coverage hiện ghi rõ đây là cơ chế source-derived, không phải quote thị trường hiện hành.

Structured-product extraction tiếp tục thêm suitability map theo wrapper: listed derivative, OTC derivative, structured security và fund/trust. Bảng này được gắn source-state để giữ chiều sâu khái niệm mà không khẳng định quy định hiện hành.

Commodity extraction bổ sung margin/notional worked example từ raw, có nhãn source-state, để người học thấy leverage và liquidity pressure trước khi đọc payoff cuối kỳ.

Option extraction bổ sung tick-cost example từ raw: option giá 0,20 với tick 0,01 có chi phí tương đối 5% mỗi tick; turnover cao có thể tiêu hết gross return. Đây là bridge giữa payoff lý thuyết và khả năng thực thi.

Raw option section cũng được chuyển thêm thành currency-delta boundary: option quốc tế có thể tạo FX exposure qua margin và settlement, nên delta hedge underlying chưa đủ để khóa P&L.

Commodity extraction bổ sung asset-allocation/global-hedge boundary: correlation lịch sử không cố định, còn index fund vẫn chịu roll rule và contango. Đây là cầu nối trực tiếp từ commodity lesson về lại portfolio theory.

Rate extraction bổ sung worked IFR calculation từ raw: người học suy ra forward rate từ hai spot rates, đồng thời phân biệt no-arbitrage benchmark với macro forecast.

Rate derivatives extraction tiếp tục thêm swaption: quyền chọn payer/receiver swap cho phép giữ flexibility trước khi khoản vay hoặc tài sản floating thực sự phát sinh.

Lesson rate/FX bổ sung worked cap–floor–collar case từ raw, làm rõ dòng tiền được giới hạn ở đâu và phần convexity bị bán để giảm premium.

Raw FX section tiếp tục được chuyển thành KIKO/zero-cost payoff walkthrough với ba nhánh range, downside protection và upper-barrier tail; nội dung được gắn textbook warning, không coi là mẫu hợp đồng hiện hành.

Valuation extraction bổ sung normalized-EPS/P-E và EV–EBITDA bridge case, giúp người học kiểm tra multiple ngầm định thay vì kết luận “rẻ” từ một denominator ở đỉnh chu kỳ.

Index-futures extraction bổ sung worked synthetic-flow case từ raw: stock/futures/option legs phải được quy đổi về delta/notional ròng trước khi suy ra market view hoặc gọi là program trading.

Portfolio extraction bổ sung worked systematic-risk floor, biến đường cong diversification trong raw thành phép tính variance theo số lượng tài sản.

Utility extraction bổ sung case A/B/C cùng expected return nhưng variance khác nhau, với expected utility cho risk-averse, risk-neutral và risk-seeking investor.

Statistics extraction tiếp tục chuyển thêm worked linear-transform check từ raw: biến đổi \(Y=aX+b\) làm mean dịch theo \(aE(X)+b\), độ lệch chuẩn nhân bởi \(|a|\) và covariance đổi theo slope. Ví dụ này nối trực tiếp phép tính thống kê với leverage, beta và exposure, để người học không chỉ nhớ công thức mà còn thấy notional thay đổi đồng thời cả expected return và risk.

CAPM extraction tiếp tục chuyển worked CML check từ raw: với rf = 5%, market expected return = 20%, market standard deviation = 3% và portfolio standard deviation = 4%, danh mục trên CML có expected return 25%; nếu correlation với market là 0,5 thì covariance là 6 theo đơn vị phần trăm bình phương. Phần này giữ ranh giới giữa vị trí trên CML và covariance, tránh dùng một đại lượng thay cho đại lượng kia.

EMH extraction tiếp tục chuyển worked expectation-surprise case từ raw: doanh thu tăng 30% vẫn có thể làm giá giảm nếu consensus đã là 50%. Bản học giữ phép tính surprise, timestamp, benchmark và event window để người học không nhầm headline tốt với abnormal return dương.

EMH extraction bổ sung worked winner/loser reversal từ raw: 47% cho nhóm losers và -8% cho nhóm winners trong giai đoạn nghiên cứu được trình bày như source-state observation, không annualize và không gọi là alpha hiện tại; lesson ghi rõ formation/holding window, delisting, chi phí và out-of-sample là điều kiện để kiểm định lại.
