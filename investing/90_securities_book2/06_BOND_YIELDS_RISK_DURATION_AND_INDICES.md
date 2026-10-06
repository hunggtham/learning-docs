# 6. Lợi suất, tín dụng, duration và thị trường trái phiếu

Bài 5 đã xác định các dòng tiền hợp đồng. Bài cuối giải quyết câu hỏi vận hành: thị trường quy đổi dòng tiền đó thành lợi suất thế nào, giá nhạy ra sao với lãi suất, và chỉ số/đường cong truyền thông tin gì? Đây là nơi phân biệt coupon, IRR, YTM, credit spread, duration và total return.

## 1. Discount rate, IRR và YTM

Discount rate (할인율) là suất dùng để quy đổi dòng tiền về hiện tại. IRR (Internal Rate of Return / 내부수익률) là nghiệm làm NPV bằng 0 cho một chuỗi dòng tiền. YTM (Yield to Maturity / 만기수익률) là IRR của trái phiếu nếu giữ đến đáo hạn và các coupon được tái đầu tư theo cùng lợi suất; đó là quy đổi mô hình, không phải realized return nếu bán sớm, tái đầu tư khác mức hoặc issuer vỡ nợ. Coupon rate chỉ là tỷ lệ trên mệnh giá, không đồng nghĩa YTM.

### Coupon rate, current yield và YTM

Ba tỷ lệ thường bị gọi chung là “lợi suất” nhưng trả lời ba câu hỏi khác nhau:

```text
Coupon rate = coupon năm / mệnh giá
Current yield = coupon năm / giá thị trường hiện tại
YTM = IRR của toàn bộ coupon và gốc đến đáo hạn
```

Với trái phiếu mệnh giá 1.000, coupon năm 60 và giá 964,33: coupon rate là 6%, current yield khoảng `60 / 964,33 = 6,22%`, còn YTM xấp xỉ 8% vì nhà đầu tư còn nhận phần chênh lệch từ 964,33 lên 1.000. Current yield bỏ qua lãi/lỗ vốn đến đáo hạn; YTM đưa khoản đó vào nghiệm quy đổi. Không dùng current yield để thay cho YTM khi so sánh trái phiếu khác giá hoặc khác thời hạn.


### Worked YTM: coupon không phải lợi suất

Dùng trái phiếu ở Bài 5: mệnh giá 1.000, coupon 60 mỗi năm, còn hai năm và giá 964,33. YTM là nghiệm của phương trình:

```
964,33 = 60/(1+y) + 1.060/(1+y)^2
```

Nghiệm xấp xỉ là `y = 8%`, trong khi coupon rate chỉ là `60/1.000 = 6%`. Chênh lệch xuất hiện vì người mua trả dưới mệnh giá và nhận lại 1.000 khi đáo hạn. Nếu bán trước hạn hoặc coupon được tái đầu tư ở mức khác 8%, realized return sẽ lệch khỏi YTM. Đây là lý do YTM là ngôn ngữ quy đổi để so sánh, không phải lời hứa về kết quả thực nhận.

## 2. Đường cong lợi suất

Yield curve (수익률곡선) xếp lợi suất theo kỳ hạn. Source trình bày bốn cách giải thích: Expectations Theory (기대이론) coi lợi suất dài hạn phản ánh lãi suất ngắn hạn kỳ vọng; Liquidity Premium Theory (유동성프리미엄이론) cộng phần bù cho việc nắm giữ kỳ hạn dài; Market Segmentation Theory (시장분할이론) cho rằng cung–cầu mỗi bucket kỳ hạn tương đối tách biệt; Preferred Habitat Theory cho phép nhà đầu tư có kỳ hạn ưa thích nhưng dịch chuyển khi phần bù đủ lớn. Bốn theory là các lăng kính bổ sung, không phải bốn dự báo đồng nhất.

Đường cong dốc lên có thể phản ánh tăng trưởng/lạm phát kỳ vọng hoặc term premium; đường cong đảo có thể phản ánh kỳ vọng hạ lãi suất. Không được đọc hình dạng mà bỏ qua regime, thanh khoản, cung trái phiếu và chính sách. Những kênh vĩ mô rộng hơn thuộc [Monetary System, Liquidity and Crisis Transmission](../04_economics/04_MONETARY_SYSTEM_LIQUIDITY_AND_CRISIS_TRANSMISSION.md).

### Đặt bốn lý thuyết cạnh nhau

| Lý thuyết | Động lực chính | Dự đoán/insight | Giới hạn |
|---|---|---|---|
| Expectations | kỳ vọng lãi suất ngắn hạn tương lai | kỳ hạn dài phản ánh chuỗi short rate kỳ vọng | bỏ qua term/liquidity premium nếu dùng đơn độc |
| Liquidity premium | phần bù cho duration và thanh khoản | kỳ hạn dài thường cần lợi suất thêm | không nói premium cố định |
| Market segmentation | cung–cầu tách theo bucket kỳ hạn | mỗi đoạn có giá riêng theo nhà đầu tư và phát hành | khó giải thích thay thế giữa kỳ hạn |
| Preferred habitat | nhà đầu tư có kỳ hạn ưa thích nhưng có thể dịch chuyển | premium đủ lớn kéo vốn sang habitat khác | sở thích và premium khó quan sát trực tiếp |

Khi đọc một curve, hãy viết hai giả thuyết cạnh nhau: “thị trường đang dự báo short rate nào?” và “term/liquidity premium đang đóng góp bao nhiêu?”. Cách tách này ngăn việc gọi mọi đường cong dốc lên là tăng trưởng hoặc mọi đường cong đảo là suy thoái.

### Spot rate và forward rate

Source còn nối các điểm trên yield curve bằng forward rate. Nếu `s₁` là spot rate một năm và `s₂` là spot rate hai năm, forward một năm bắt đầu từ năm thứ hai thỏa:

```text
(1 + s₂)^2 = (1 + s₁) × (1 + f₁,₂)
f₁,₂ = (1 + s₂)^2 / (1 + s₁) − 1
```

Ví dụ `s₁ = 8%`, `s₂ = 10%` cho `f₁,₂ ≈ 12,04%`. Đây là mức được ngụ ý bởi các spot rate trong mô hình, không phải cam kết lãi suất tương lai; term premium, thanh khoản và sai số đo lường vẫn có thể làm cách diễn giải kinh tế khác đi.

## 3. Tín dụng và xếp hạng

Rủi ro tín dụng (credit risk / 신용위험) là rủi ro tổn thất do chất lượng tín dụng của issuer hoặc đối tác suy giảm; rủi ro vỡ nợ (default risk / 부도위험) là trường hợp hẹp hơn khi issuer không trả đủ hoặc đúng hạn. Xếp hạng tín dụng (credit rating / 신용등급) của Moody’s, S&P, Fitch và các tổ chức khác là đánh giá tương đối về credit risk; rating không phải bảo hiểm và có thể chậm hơn thông tin thị trường. Bảng source đặt vùng `BBB-/Baa3` quanh ranh giới investment grade và `BB/Ba` vào vùng speculative/high-yield; tên bậc và quy tắc phân loại phải đọc theo đúng agency, ngày phát hành và jurisdiction. Spread so với trái phiếu tham chiếu bù cho default, liquidity, tax và các rủi ro khác. High-yield/junk bond có spread và xác suất tổn thất cao hơn trong textbook, nhưng lợi suất cao không tự bù đủ nếu recovery thấp hoặc thanh khoản biến mất.

## 4. Duration và convexity

Macaulay duration (맥컬레이 듀레이션) là thời gian bình quân gia quyền theo giá trị hiện tại của các dòng tiền. Modified duration (수정듀레이션) xấp xỉ độ nhạy phần trăm của giá với thay đổi lợi suất:

```text
ΔP / P ≈ −Modified Duration × Δy
```

Duration dài hơn thường nghĩa là giá nhạy hơn với lãi suất; coupon thấp và maturity dài thường làm duration tăng. Convexity (볼록성) bổ sung độ cong của quan hệ giá–lợi suất, giúp approximation tốt hơn khi cú sốc lớn:

```text
ΔP/P ≈ −D_mod·Δy + 1/2·Convexity·(Δy)^2
```

Duration không dự báo default, spread widening hay prepayment. Với callable/MBS, dòng tiền thay đổi theo lãi suất nên duration có thể biến thiên (negative convexity). Đây là boundary cần giữ khi chuyển từ trái phiếu chính phủ sang sản phẩm cấu trúc.

### Worked Macaulay và modified duration

Với trái phiếu mệnh giá 1.000, coupon năm 60, còn hai năm và YTM 8%, giá là khoảng 964,33. Giá trị hiện tại của coupon năm 1 là `60/1,08 = 55,56`; giá trị hiện tại của coupon + gốc năm 2 là `1.060/(1,08)^2 = 908,78`. Macaulay duration là trung bình trọng số theo các giá trị hiện tại:

```text
D_Mac = [1 × 55,56 + 2 × 908,78] / 964,33 ≈ 1,94 năm
D_mod = D_Mac / (1 + YTM) = 1,94 / 1,08 ≈ 1,80
```

Nếu YTM tăng 50 điểm cơ bản, approximation bậc một cho biết giá giảm khoảng `1,80 × 0,005 = 0,90%`, tương đương khoảng 8,68 trên giá 964,33. Đây là độ nhạy cục bộ: khi cú sốc lớn hơn, convexity và việc yield curve dịch chuyển không song song làm kết quả khác đi. Một zero-coupon hai năm ở cùng YTM có duration gần 2 năm (modified khoảng `2/1,08 = 1,85`), nên nhạy hơn trái phiếu coupon này; coupon trả sớm kéo trọng tâm dòng tiền về phía trước.

Không được gọi Macaulay duration là “thời gian đáo hạn còn lại”. Nó là thời gian bình quân của giá trị hiện tại các dòng tiền, và thay đổi khi giá, coupon, YTM hoặc lịch dòng tiền thay đổi. Với callable, MBS hoặc trái phiếu có spread tín dụng, phải ghi rõ đang đo duration theo rate nào và dòng tiền giả định nào.

## 5. Benchmark và bond index

Một chỉ số trái phiếu (bond index / 채권지수) phải xác định universe, maturity, rating, currency, trọng số và cách xử lý phát hành mới, đáo hạn, coupon và default. Price index chỉ theo giá; coupon index theo coupon; yield index theo lợi suất; chỉ số tổng lợi suất (total-return index / 총수익지수) tái đầu tư coupon và phản ánh cả giá lẫn income. Benchmark portfolio source nêu dùng để so sánh, không phải danh mục “tối ưu” cho mọi nhà đầu tư.

Source nhắc các bond index Hàn Quốc, gồm KSDA-BLP Korean Bond Index và các phân nhóm market/bond subindex. Tên mã, thành phần và phương pháp hiện tại cần xác minh lại trước khi sử dụng; route chỉ giữ nguyên tắc construction vì OCR không đủ cho mọi chi tiết.

### Worked bond index và tracking error

Giả sử một trái phiếu có giá đầu kỳ 100, giá cuối kỳ 101 và trả coupon 3 trong kỳ. Nếu chỉ đo price return, chỉ số cơ sở 100 tăng lên 101, tức `+1%`. Coupon return trong ví dụ là `3/100 = 3%`; nếu nhận đủ coupon và chưa xét tái đầu tư, total return là `(101 + 3)/100 − 1 = 4%`, nên total-return index cơ sở 100 sẽ ở khoảng 104. Hai con số khác nhau không phải mâu thuẫn: price index trả lời “giá thay đổi thế nào?”, còn total-return index trả lời “nhà đầu tư nhận được bao nhiêu từ giá và income?”.

Trong chỉ số thật, cần ghi rõ clean/dirty price, accrued interest, ngày nhận coupon, giả định tái đầu tư và xử lý trái phiếu đáo hạn hoặc vỡ nợ. Nếu một quỹ nhận coupon nhưng benchmark chỉ là price index, active return sẽ bị thổi phồng giả tạo. Ngược lại, dùng benchmark total return cho danh mục không được phép tái đầu tư coupon sẽ làm so sánh lệch theo hướng ngược lại.

Raw cũng phân biệt broad market index, bond subindex và customized index. Customized index có thể khóa universe, rating, maturity hoặc duration theo mục tiêu danh mục; đổi quy tắc này đồng nghĩa đổi exposure, không chỉ đổi tên benchmark. Sau khi chọn benchmark, tracking error đo độ lệch biến động của lợi suất danh mục so với benchmark:

```text
Tracking error = độ lệch chuẩn(R_danh mục − R_benchmark)
```

Tracking error thấp không chứng minh danh mục tốt; nó chỉ nói danh mục bám benchmark sát. Cần đọc cùng active return, chi phí, duration, rating và currency để biết phần lệch là chủ ý hay sai lệch không được kiểm soát.

### Thị trường sơ cấp, thứ cấp và đấu giá

Ở thị trường sơ cấp, issuer phát hành trái phiếu và nhận vốn; ở thị trường thứ cấp, nhà đầu tư mua bán lại các trái phiếu đã phát hành. Giá và lợi suất sơ cấp tạo điểm khởi đầu cho khoản nợ, nhưng giá thứ cấp còn phản ánh lãi suất mới, credit spread, thanh khoản và cung–cầu sau phát hành. Vì vậy giá phát hành không phải “giá trị cố định” của trái phiếu; nó có thể lệch ngay sau khi thị trường cập nhật thông tin.

Source đặt cạnh nhau hai kiểu đấu giá textbook:

| Kiểu | Cách phân bổ khái quát | Rủi ro diễn giải |
|---|---|---|
| Conventional/American (discriminatory) | Bên trúng trả theo mức giá/lợi suất trong chính lệnh của mình | Cùng một phiên nhưng các bên có thể nhận mức khác nhau |
| Dutch/uniform-price | Các lệnh trúng cùng chịu một mức giá/lợi suất cắt duy nhất | Chiến lược đặt lệnh và mức cutoff quyết định kết quả chung |

Ví dụ, nếu các mức lợi suất dự thầu hợp lệ là 5,0%, 5,2% và 5,4%, cutoff ở 5,4% thì kiểu discriminatory áp mức riêng cho từng lệnh trúng; kiểu uniform-price áp cùng mức cutoff cho các lệnh trúng. Đây chỉ là sơ đồ cơ chế: quy tắc ưu tiên, khối lượng, lệnh cạnh tranh/không cạnh tranh và cách báo giá phụ thuộc từng jurisdiction và prospectus.

Khi nối đấu giá với yield curve, hãy hỏi ba điều: issuer huy động được vốn ở mức nào, nhà đầu tư nhận exposure kỳ hạn/rating nào, và trái phiếu giao dịch thứ cấp với spread bao nhiêu. Một phiên sơ cấp có lợi suất thấp không tự chứng minh issuer ít rủi ro; có thể thanh khoản dồi dào hoặc lệnh bị giới hạn. Ngược lại, thanh khoản thứ cấp kém có thể làm spread tăng dù default risk chưa đổi.

## 6. Repo (repurchase agreement / 환매조건부매매) và cơ chế thị trường

Repo là giao dịch bán và mua lại, về kinh tế gần khoản vay có tài sản thế chấp. Haircut, margin, collateral quality và haircut change quyết định đòn bẩy và liquidity. Khi giá tài sản giảm hoặc haircut tăng, bên vay có thể phải bổ sung tài sản hoặc bán cưỡng bức. Vì vậy repo nối đường cong lợi suất với funding và stress thị trường; không nên đọc bond market như một bảng giá tĩnh.

Ở phần thị trường trái phiếu, source đặt repo cạnh bond index và mô tả repo như một giao dịch có ngày mua lại, tài sản bảo đảm và lãi repo; `KSDA-BLP Korean Bond Index` được nêu như một chỉ số chuẩn hóa có mức cơ sở 100.00. Một bảng còn dùng hạng tín nhiệm `BBB-` để minh họa normal bond. Đây là trạng thái textbook của ví dụ, không phải xác nhận cấu phần hay mức hiện hành của thị trường Hàn Quốc.

### Worked repo haircut

Giả sử collateral trị giá 100 và haircut ban đầu là 5%, bên vay chỉ nhận 95 tiền mặt. Nếu giá collateral giảm còn 90 mà haircut vẫn là 5%, khoản vay tối đa còn `90 × 95% = 85,5`; bên vay thiếu 9,5 và phải nộp thêm tiền hoặc tài sản. Nếu haircut tăng lên 10% ngay cả khi giá vẫn là 100, khoản vay tối đa cũng giảm còn 90 và tạo margin call 5.

Ví dụ tách hai cú sốc thường bị gộp nhầm: giá tài sản giảm làm giá trị bảo đảm co lại, còn haircut tăng làm lender yêu cầu đệm an toàn lớn hơn. Cả hai đều có thể buộc deleveraging và bán cưỡng bức. Con số trên là mô hình minh họa, không phải ngưỡng margin hiện hành của một thị trường cụ thể.

## 7. Worked duration and spread scenario

Giả sử một trái phiếu có modified duration bằng 4. Khi lợi suất tăng 50 điểm cơ bản, xấp xỉ bậc một cho biết:

```text
ΔP/P ≈ −4 × 0,005 = −2%
```

Nếu convexity dương, số lỗ thực tế thường nhỏ hơn một chút so với approximation tuyến tính khi cú sốc không quá lớn. Nhưng nếu spread tín dụng đồng thời tăng 100 điểm cơ bản, chỉ dùng duration của đường cong chính phủ sẽ đánh giá thiếu rủi ro. Nhà đầu tư cần tách rate duration, spread duration và khả năng dòng tiền thay đổi.

Có thể lượng hóa tách rủi ro bằng hai duration:

```
ΔP/P ≈ −D_rate·Δy_rate − D_spread·Δspread
```

Ví dụ, nếu `D_rate = 4`, `D_spread = 3`, lợi suất chính phủ tăng 50 điểm cơ bản và spread tăng 100 điểm cơ bản, tác động bậc một xấp xỉ là `−4 × 0,005 − 3 × 0,01 = −5%`. Con số này chưa tính convexity, default thực tế hay thay đổi dòng tiền; nó chỉ cho biết một danh mục có thể lỗ vì hai kênh cùng lúc. Nếu chỉ nhìn yield curve chính phủ, người học sẽ quy toàn bộ −5% cho lãi suất và bỏ sót credit exposure.


Với trái phiếu callable, lãi suất giảm có thể khiến issuer gọi lại trái phiếu; nhà đầu tư nhận tiền sớm đúng lúc cơ hội tái đầu tư có lợi suất thấp. Với MBS, lãi suất giảm có thể làm prepayment tăng và duration rút ngắn. Vì vậy duration là trạng thái của dòng tiền tại một kịch bản, không phải nhãn cố định trên sản phẩm.

## 8. Từ benchmark đến attribution

Total return của danh mục trái phiếu có thể phân rã thành carry/coupon, thay đổi giá do đường cong, thay đổi spread, FX nếu có và chi phí. So sánh với bond index cần hỏi phần chênh lệch đến từ duration khác, rating khác, sector khác hay timing giao dịch. Một danh mục vượt benchmark trong môi trường lợi suất giảm chưa chắc có kỹ năng; có thể chỉ đang mang duration dài hơn. Attribution làm rõ exposure nào đã tạo kết quả.

### Reconstruction: bond index, thị trường và auction không phải một unit

Source tách measurement khỏi market plumbing. Chỉ số trái phiếu (bond index / 채권지수) có thể là price index, coupon-income index, yield-related measure hoặc chỉ số tổng lợi suất (total-return index / 총수익지수); với mục tiêu đo performance, total return phải cộng income và thay đổi giá theo đúng convention. Tracking error chỉ có ý nghĩa khi portfolio và benchmark dùng cùng universe, pricing time, currency và reinvestment rule.

Primary market (발행시장) là nơi chứng khoán nợ được phát hành; secondary market (유통시장) là nơi nhà đầu tư giao dịch lại. Auction là cơ chế price discovery ở phát hành và raw phân biệt conventional/multiple-price với Dutch/single-price. Hai cơ chế có incentive bidding khác nhau; không được gom chúng vào một nhãn “auction”. Repo (repurchase agreement / 환매조건부매매) là giao dịch bán chứng khoán kèm cam kết mua lại, kinh tế gần một khoản funding có collateral; haircut tạo buffer nhưng không xóa market, liquidity hay counterparty risk.

## 9. Source-question test

Để giải câu hỏi cuối sách, người học cần: (1) phân biệt coupon với YTM; (2) suy ra giá giảm khi lợi suất tăng; (3) chọn duration/convexity phù hợp; (4) phân biệt price index với total-return index; (5) nhận diện spread và rating là thước đo rủi ro, không phải bảo đảm. Các câu hỏi có số liệu hình/OCR không rõ được đánh `SOURCE_AMBIGUITY` trong coverage thay vì bịa đáp án.

## Chốt toàn Sách 2

Sách 2 tạo một knowledge graph: chu kỳ và chỉ báo ảnh hưởng dòng tiền; dòng tiền và rủi ro quyết định định giá; giá và khối lượng tạo tín hiệu; chiến lược biến tín hiệu thành exposure; trái phiếu biến thời hạn, tín dụng và funding thành lợi suất. Ranh giới cuối cùng là mô hình textbook không thay thế dữ liệu đúng thời điểm, prospectus hay quy định hiện hành. Để đi từ route này sang quy trình đầu tư hoàn chỉnh, quay lại [Investing README](../README.md) và [Full Investment Process](../07_integrated_case_studies/05_FULL_INVESTMENT_PROCESS_FROM_THESIS_TO_REVIEW.md).
