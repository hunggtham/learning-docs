# 5. Trái phiếu và sản phẩm thu nhập cố định

Trái phiếu (bond / 채권) là bước chuyển từ quyền sở hữu residual sang quyền đòi hỏi theo hợp đồng. Bài 4 đã nói về cổ phiếu và chỉ số; bài này xây bản đồ payoff của fixed-income securities, để bài 6 có thể giải thích giá–lợi suất, tín dụng và duration mà không lẫn coupon với realized return.

## 1. Cấu trúc trái phiếu

Một trái phiếu thường có mệnh giá (face value), ngày đáo hạn (maturity date), lãi coupon (coupon) và coupon rate. Coupon = face value × coupon rate theo kỳ trả. Zero-coupon/discount bond không trả coupon định kỳ; nhà đầu tư mua dưới mệnh giá và nhận mệnh giá khi đáo hạn. Coupon bond trả dòng tiền định kỳ và mệnh giá ở cuối kỳ. Perpetuity bond không có ngày đáo hạn hữu hạn trong mô hình.

Giá trái phiếu là giá trị hiện tại của coupon và gốc:

```text
P = Σ [C / (1 + y)^t] + [F / (1 + y)^n]
```

`C` là coupon mỗi kỳ, `F` là face value, `y` là lợi suất chiết khấu và `n` là số kỳ. Khi `y` tăng, giá giảm; khi coupon rate bằng lợi suất thị trường, giá gần mệnh giá. Quan hệ ngược này là cơ chế, không phải quy tắc ghi nhớ rời.

## 2. Trái phiếu có quyền chọn hoặc cấu trúc lai

Convertible bond (전환사채) cho người sở hữu quyền chuyển thành cổ phiếu theo điều khoản; giá chịu ảnh hưởng của cả trái phiếu và quyền chọn cổ phiếu. Bond with warrant (신주인수권부사채) gắn quyền mua riêng hoặc đi kèm; exchangeable bond (교환사채) cho phép đổi sang chứng khoán của tổ chức khác. Callable bond cho tổ chức phát hành quyền mua lại trước hạn; puttable bond cho nhà đầu tư quyền bán lại. Quyền chọn thay đổi thời hạn dòng tiền và làm duration không còn đơn giản.

## 3. Sản phẩm dựa trên tài sản hoặc chỉ số

ABS (Asset-Backed Securities / 자산유동화증권) và MBS (Mortgage-Backed Securities / 주택저당증권) gom dòng tiền từ tài sản cơ sở rồi phát hành chứng khoán. Pay-through và pass-through khác nhau ở cách dòng tiền đi qua cấu trúc. CMO (Collateralized Mortgage Obligation) chia dòng tiền thế chấp thành tranche, tạo prepayment và extension risk khác nhau. Floating-rate bond (변동금리채) điều chỉnh coupon theo lãi suất tham chiếu; reverse floater (역변동금리채) có coupon biến động ngược. Indexed bond (지수연동채권) gắn coupon hoặc gốc với chỉ số; international bond (국제채) và eurobond (유로채) liên quan nơi phát hành, tiền tệ và nhà đầu tư, không mặc nhiên loại bỏ rủi ro tỷ giá.

Preferred stock (우선주) có quyền ưu tiên cổ tức hoặc tài sản so với common stock nhưng thường hạn chế quyền biểu quyết. Catastrophe bond chuyển một phần rủi ro thảm họa sang nhà đầu tư; nếu trigger xảy ra, principal có thể dùng để bù tổn thất. Structured note (구조화채권) kết hợp trái phiếu với phái sinh, nên phải đọc payoff, collateral, issuer risk, liquidity và điều kiện trigger thay vì chỉ nhìn coupon quảng cáo.

Source minh họa floating-rate bond bằng coupon dạng `benchmark + spread` (ví dụ LIBOR + biên) và có thể đặt floor rate. Reverse floater đi theo dạng `constant − benchmark`, thường cần cap để giới hạn coupon. Cấu trúc này khiến coupon đổi theo benchmark và basis risk; LIBOR ở đây chỉ là ví dụ textbook trong raw, không phải khuyến nghị dùng benchmark hiện hành. Indexed bond có thể gắn coupon hoặc principal với chỉ số/real rate, nên phải kiểm tra index lag, cách điều chỉnh và liệu khoản bảo vệ có thực sự khớp với lạm phát của nhà đầu tư.

### International bond, foreign bond (외국채) và eurobond

Raw tách `foreign bond` và `eurobond` theo nơi phát hành, thị trường và tiền tệ, không chỉ theo tên địa lý:

| Nhóm | Cách đọc | Rủi ro cần tách |
|---|---|---|
| Foreign bond | Người vay nước ngoài phát hành trong thị trường nội địa của một nước, thường bằng tiền tệ và theo quy tắc của thị trường đó | Quy định địa phương, issuer risk và FX của nhà đầu tư nước ngoài |
| Eurobond | Phát hành ngoài thị trường nội địa của đồng tiền định danh; “euro” không nhất thiết nghĩa là phát hành tại châu Âu | FX, jurisdiction, withholding tax, thanh khoản và quy tắc thanh toán |

Các tên `Yankee`, `Samurai` và `Bulldog` trong source là nhãn thị trường/đồng tiền của foreign bond (lần lượt gắn với Mỹ, Nhật và Anh trong ví dụ textbook). Không nên suy ra issuer an toàn hơn từ tên gọi; điều cần đọc vẫn là prospectus, governing law, currency của coupon/gốc và nơi nhà đầu tư nhận tiền.

Ví dụ, một trái phiếu trả lợi suất 4% bằng ngoại tệ nhưng đồng ngoại tệ mất 5% so với KRW sẽ cho lợi suất quy đổi gần `1,04 × 0,95 − 1 = −1,2%` trước phí và thuế. Coupon dương bằng ngoại tệ vì thế không bảo đảm lợi nhuận dương trong đồng tiền của người học. Nếu hedge FX, phải cộng thêm chi phí hedge, basis và kỳ hạn hợp đồng; nếu không hedge, attribution phải tách bond return khỏi currency return.

Raw còn phân nhóm structured note theo tài sản hoặc điều kiện kích hoạt: interest-rate-linked note (inverse FRN, dual-index FRN, CMS và range accrual), default/credit-spread/credit-linked note, equity hoặc equity-index-linked note, currency/dual-currency note và commodity-linked note. Hãy đọc taxonomy này theo biến làm payoff đổi: benchmark lãi suất, spread tín dụng, giá cổ phiếu, tỷ giá hay hàng hóa. Mỗi tên chỉ là nhãn của tài sản tham chiếu; trước khi định giá vẫn phải tìm barrier, cap/floor, trigger, issuer risk và cách xử lý khi dữ liệu tham chiếu không còn tồn tại.

### Structured note: đọc theo biến làm payoff đổi

| Nhóm trong raw | Driver của coupon/gốc | Cấu phần/rủi ro cần kiểm tra |
|---|---|---|
| Interest-rate-linked | Benchmark lãi suất; inverse FRN đi ngược benchmark, dual-index dùng hai benchmark, CMS dùng kỳ hạn swap, range accrual chỉ tích lũy khi lãi suất nằm trong vùng | Công thức `constant − rate`, cap/floor, ngày reset, basis giữa hai benchmark và số ngày đủ điều kiện |
| Default/credit-spread/credit-linked | Vỡ nợ hoặc credit spread của issuer/reference entity | Trigger là default hay spread barrier, principal chịu lỗ theo waterfall nào, recovery giả định và issuer risk |
| Equity/equity-index-linked | Giá cổ phiếu hoặc chỉ số cổ phiếu | Quyền chọn mua/bán được nhúng, barrier, participation rate, dividend treatment và dilution |
| Currency/dual-currency | Tỷ giá hoặc đồng tiền trả coupon/gốc | Ai chịu quyền đổi tiền, strike, cap/floor, currency mismatch và chi phí hedge |
| Commodity-linked | Giá hoặc chỉ số hàng hóa | Basis với hàng hóa vật chất, futures roll, margin và trigger thanh toán |

Tên gọi không cho biết principal có được bảo vệ hay không. Một note có thể trả coupon cao vì nhà đầu tư đang bán quyền chọn, nhận rủi ro credit hoặc chấp nhận thanh khoản thấp. Trước khi so sánh hai note, hãy viết payoff ở ba trạng thái: benchmark tăng, benchmark giảm và trigger xảy ra; nếu không mô tả được ba trạng thái đó thì chưa thể gọi sản phẩm “fixed income” theo nghĩa an toàn.

### So sánh nhanh: cùng là “fixed income” nhưng payoff không giống nhau

Tên nhóm sản phẩm chỉ cho biết lớp tài sản; muốn đánh giá phải xác định ai sở hữu dòng tiền, biến cố nào làm dòng tiền lệch khỏi kế hoạch và rủi ro nào không thể quan sát từ coupon. Bảng dưới đây dùng cùng một bộ câu hỏi để tránh xếp các sản phẩm khác bản chất vào một rổ:

| Sản phẩm | Dòng tiền chính đến từ đâu? | Rủi ro đặc thù cần tách riêng | Câu hỏi kiểm tra trước khi định giá |
| --- | --- | --- | --- |
| Trái phiếu coupon thông thường | Coupon cố định + hoàn gốc | Lãi suất, tín dụng issuer, thanh khoản | YTM dựa trên giá nào và thứ tự ưu tiên khi vỡ nợ ra sao? |
| Zero-coupon | Khoản hoàn gốc duy nhất ở đáo hạn | Duration dài, nhạy với lãi suất, không có dòng tiền giữa kỳ | Khoảng thời gian khóa vốn và giá trị chiết khấu là bao nhiêu? |
| Convertible / warrant | Coupon hoặc gốc + quyền tham gia upside của tài sản cơ sở | Biến động cổ phiếu, dilution, điều khoản chuyển đổi | Quyền chuyển đổi thuộc ai, tỷ lệ chuyển đổi và ngày khóa quyền thế nào? |
| Callable / puttable | Dòng tiền trái phiếu + quyền mua lại/bán lại | Reinvestment risk hoặc extension risk | Ai có quyền kích hoạt, tại mức giá và thời điểm nào? |
| ABS / MBS / CMO | Dòng tiền từ pool tài sản và waterfall | Default pool, prepayment, tranche, pháp lý cấu trúc | Tiền trả theo pass-through hay waterfall; tranche chịu lỗ trước hay sau? |
| Floating-rate / reverse floater | Coupon gắn với benchmark, theo cùng chiều hoặc ngược chiều | Basis risk, reset, leverage coupon | Benchmark, spread, kỳ reset và floor/cap cụ thể là gì? |
| Structured note | Trái phiếu issuer + payoff phái sinh | Issuer risk, barrier/trigger, định giá khó và thanh khoản thấp | Nếu barrier/trigger xảy ra thì mất coupon, gốc hay cả hai? |

Điểm cần nhớ là **nguồn dòng tiền** và **quyền thay đổi dòng tiền** là hai trục khác nhau. Một MBS có thể có tài sản thế chấp nhưng vẫn chịu prepayment; một structured note có thể hứa coupon cao nhưng phần bù nằm ở rủi ro issuer hoặc quyền chọn bán cho nhà đầu tư. Vì thế không nên dùng một chỉ tiêu duy nhất (coupon, rating hay duration) để kết luận sản phẩm “an toàn”.

### Source product inventory: mỗi sản phẩm là một semantic unit

Raw source đặt các heading sản phẩm riêng; vì vậy coverage không dùng một hàng chung để che mất khác biệt payoff. Bảng này là minimum reconstruction của các distinction đọc chắc từ source:

| Sản phẩm | Thuật ngữ | Cơ chế chính | Boundary / điều kiện không được bỏ |
|---|---|---|---|
| Convertible bond | 전환사채 (CB) | trái phiếu + quyền chuyển thành cổ phiếu của issuer | conversion ratio/price, period và dilution quyết định payoff |
| Bond with warrant | 신주인수권부사채 (BW) | trái phiếu + quyền mua cổ phiếu | warrant có thể tách rời tùy điều khoản; không đồng nhất với CB |
| Exchangeable bond | 교환사채 (EB) | đổi sang chứng khoán đã chỉ định, thường không phải cổ phiếu mới của chính issuer | phải đọc exchange asset và exchange ratio |
| ABS | 자산유동화증권 | dòng tiền từ pool tài sản được securitize | credit enhancement, waterfall và servicing quan trọng hơn tên “asset-backed” |
| MBS | 주택저당증권 | ABS dựa trên khoản vay thế chấp | prepayment/extension risk làm timing dòng tiền thay đổi |
| CMO | CMO | chia dòng tiền mortgage thành các tranche | tranche khác nhau nhận principal/loss khác nhau |
| Floating-rate bond | 변동금리채 | coupon = benchmark +/− spread, reset định kỳ | benchmark, reset lag, floor/cap và basis risk phải ghi rõ |
| Reverse floater | 역변동금리채 | coupon biến động ngược benchmark, thường dạng constant − rate | có thể tạo leverage coupon; cần cap/floor để hiểu downside |
| Preferred stock | 우선주 | ưu tiên cổ tức/tài sản hơn common stock nhưng vẫn là equity-like claim | voting, cumulative/non-cumulative và conversion phụ thuộc điều khoản |
| Indexed bond | 지수연동채권 | coupon hoặc principal gắn với index | index lag, floor và cách điều chỉnh principal thay đổi realized payoff |
| International bond | 국제채 | phát hành xuyên biên giới/ngoài thị trường nội địa | currency, jurisdiction và settlement phải tách riêng |
| Foreign bond | 외국채 | issuer nước ngoài phát hành trong một thị trường nội địa | không đồng nghĩa eurobond |
| Eurobond | 유로채 | phát hành ngoài thị trường nội địa của đồng tiền định danh | “euro” không có nghĩa bắt buộc phát hành ở châu Âu |
| Catastrophe bond | catastrophe bond | principal/coupon phụ thuộc trigger thảm họa | trigger và loss waterfall là phần cốt lõi |
| Structured note | 구조화채권 | debt claim + derivative-linked payoff | barrier, participation, cap/floor, trigger, issuer/liquidity risk phải đọc trước coupon |

Raw còn có một heading riêng "Asset-Backed Bond" quanh vùng source pp. 247–248; OCR hiện không đủ sạch để chứng minh distinction của mục này so với ABS ở ngay trước đó. Coverage vì thế giữ unit đó ở SOURCE_AMBIGUITY thay vì tự phát minh định nghĩa.

## 4. Cách đọc một sản phẩm

Trước khi định giá, ghi bảy câu hỏi: ai là issuer; dòng tiền cố định hay biến đổi; gốc trả khi nào; quyền chọn thuộc ai; tài sản bảo đảm và thứ tự ưu tiên ra sao; điều gì làm dòng tiền đổi; và thị trường thứ cấp có thanh khoản không. Hai sản phẩm cùng coupon có thể có duration, default risk và liquidity risk khác hẳn. Đây là mối nối từ classification sang mechanism.

## 5. Boundary của textbook-state

Tên sản phẩm, điều khoản phát hành và luật thuế thay đổi theo jurisdiction và ngày phát hành. Source cung cấp taxonomy, không cung cấp bản cập nhật pháp lý hiện tại. Trước khi mua sản phẩm thật, cần đọc prospectus và nguồn chính thức; không suy ra suitability từ tên gọi “fixed income”.

## 6. Worked bond price

Giả sử trái phiếu mệnh giá 1.000, coupon năm 6% và còn hai năm. Nếu lợi suất thị trường là 8%, giá lý thuyết là:

```text
P = 60/1,08 + (60 + 1.000)/(1,08)^2 ≈ 964,33
```

Giá thấp hơn mệnh giá vì coupon 6% thấp hơn lợi suất yêu cầu 8%. Nếu lợi suất giảm xuống 4%, cùng dòng tiền sẽ có giá cao hơn mệnh giá. Ví dụ này cho thấy coupon rate cố định nhưng market yield thay đổi; không được gọi coupon 6% là “lợi suất chắc chắn” khi mua trên thị trường thứ cấp.

### Worked indexed bond: gốc và coupon cùng đổi theo chỉ số

Một bảng trong raw minh họa trái phiếu có mệnh giá gốc 10.000, coupon danh nghĩa 4% và principal được điều chỉnh theo chỉ số. Nếu chỉ số tăng lần lượt 2%, 3% và 1%, principal điều chỉnh là:

| Kỳ | Mức tăng chỉ số | Principal điều chỉnh | Coupon 4% trên principal |
|---:|---:|---:|---:|
| 0 | — | 10.000,0 | — |
| 1 | 2% | 10.200,0 | 408,0 |
| 2 | 3% | 10.506,0 | 420,2 |
| 3 | 1% | 10.611,1 | 424,4 |

Ở kỳ cuối, nhà đầu tư nhận coupon khoảng 424,4 và principal khoảng 10.611,1, tổng khoảng 11.035,5 trước thuế và phí. Cách tính cho thấy “coupon 4%” không còn là 400 cố định mỗi kỳ; nó được áp trên gốc đã index. Nếu prospectus chỉ index coupon mà không index principal, payoff sẽ khác hoàn toàn. Vì vậy phải kiểm tra chỉ số tham chiếu, lag, công thức làm tròn, floor/deflation protection và thời điểm điều chỉnh trước khi so sánh với trái phiếu thường.

Đây là ví dụ textbook được reconstruct từ bảng raw, không phải điều khoản của một sản phẩm hiện hành. Indexed bond có thể giảm rủi ro lạm phát danh nghĩa nhưng vẫn có issuer risk, basis risk và rủi ro chỉ số không phản ánh đúng chi phí của người nắm giữ.

## 7. Payoff map cho sản phẩm lai

Convertible bond có một phần trái phiếu và một quyền chọn chuyển đổi; khi giá cổ phiếu tăng, quyền chọn có thể làm giá sản phẩm tăng nhanh hơn trái phiếu thuần. Callable bond trao quyền cho issuer mua lại khi lãi suất giảm, nên nhà đầu tư bị giới hạn upside và chịu reinvestment risk. Puttable bond trao quyền ngược lại cho nhà đầu tư, thường có giá trị bảo vệ khi lãi suất tăng hoặc credit xấu đi. ABS/MBS thêm prepayment và waterfall risk: dòng tiền có thể đến sớm, đến muộn hoặc bị phân tầng khác dự kiến.

Khi đọc structured note, hãy tách payoff thành trái phiếu nền + quyền chọn + rủi ro issuer + điều kiện trigger. Coupon cao có thể là tiền bán quyền chọn hoặc bù cho thanh khoản thấp, không phải “free yield”. Đây là mental model giúp người học không nhầm tên sản phẩm với mức an toàn.

## 8. Thứ tự ưu tiên, recovery và expected loss

Khi issuer gặp stress, câu hỏi không còn chỉ là coupon bao nhiêu mà là ai chịu lỗ trước và tài sản nào còn lại để thu hồi. Senior secured, senior unsecured và subordinated có thể có thứ tự ưu tiên khác nhau; thứ tự cụ thể phụ thuộc prospectus và luật phá sản, nên không được coi bảng phân loại textbook là quy tắc pháp lý phổ quát.

Một mental model đơn giản là:

Expected loss ≈ xác suất vỡ nợ × tỷ lệ mất mát khi vỡ nợ × exposure

Nếu xác suất vỡ nợ một kỳ là 2%, tỷ lệ mất mát sau recovery là 60% và exposure là 100, expected loss giản lược là `0,02 × 0,60 × 100 = 1,2`. Đây không phải giá trái phiếu hay spread quan sát được: spread còn chứa premium thanh khoản, risk appetite, kỳ hạn, thuế và sai số mô hình. Nhưng phép nhân giúp người học hiểu vì sao cùng rating mà recovery hoặc collateral khác nhau vẫn tạo payoff khác nhau.

Khi đọc ABS/MBS hoặc structured note, hãy hỏi thêm waterfall phân phối tiền và tranche nào hấp thụ lỗ đầu tiên. Khi đọc trái phiếu doanh nghiệp thông thường, hãy tách issuer risk khỏi rate risk; coupon cao có thể bù cho expected loss và liquidity, nhưng không biến principal thành chắc chắn.

## Chốt và bàn giao

Invariant là “trái phiếu là gói dòng tiền có thời điểm, ưu tiên và quyền chọn”. Giá phụ thuộc discount rate và xác suất dòng tiền thực sự nhận được. Bài 6 dùng invariant này để giải YTM, đường cong lợi suất, spread, duration và chỉ số trái phiếu. Xem [Lợi suất và rủi ro trái phiếu](./06_BOND_YIELDS_RISK_DURATION_AND_INDICES.md).
