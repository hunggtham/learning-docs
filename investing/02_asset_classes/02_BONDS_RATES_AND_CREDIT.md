# Trái phiếu, lãi suất và credit

> Trái phiếu thường bị mô tả như “sản phẩm an toàn trả lãi cố định”. Cách hiểu đó quá đơn giản. Bond là một tập hợp contractual cash flows chịu đồng thời rate risk, inflation risk, credit risk, liquidity risk, optionality và đôi khi FX risk. Chapter này xây bond analysis từ nguyên lý định giá đến cách đọc yield curve, credit spread và bond ETF.

## 1. Bond là hợp đồng cho vay

Bond holder cho issuer vay capital và nhận các cash flows theo hợp đồng. *Face value* hay *par value* là principal tham chiếu; *coupon* là khoản interest theo terms; *maturity* là ngày principal được hoàn trả nếu issuer không default.

Một bond 5 năm face value 1.000, coupon 4% trả annual có thể trả 40 mỗi năm rồi 1.000 ở maturity. Nhưng market price hôm nay không nhất thiết bằng 1.000. Giá phụ thuộc discount rate mà market yêu cầu cho toàn bộ future cash flows.

Bond holder khác equity holder ở claim. Equity nhận residual value sau creditors; bond holder có contractual priority cao hơn nhưng upside thường bị giới hạn vào coupon/principal, trừ instruments có embedded equity option như convertible bond.

## 2. Bond price là present value của cash flows

Logic định giá cơ bản:

`Bond Price = Σ Coupon_t / (1 + y)^t + Face Value / (1 + y)^T`

Trong đó `y` là discount rate/yield phù hợp với maturity, credit và liquidity của bond. Khi required yield tăng, present value của fixed future cash flows giảm; vì vậy price và yield thường di chuyển ngược chiều.

Điều này giải thích tại sao government bond không default vẫn có thể giảm mạnh. Investor không mất vì issuer không trả; investor mất mark-to-market vì market discount rate đã tăng.

## 3. Coupon, current yield và yield-to-maturity không giống nhau

Coupon rate là contractual interest dựa trên face value. *Current yield* gần đúng bằng annual coupon chia current market price. *Yield to Maturity* (*YTM*) là internal rate of return khiến present value của contractual cash flows bằng market price, với các assumptions nhất định như reinvestment và không default.

Ví dụ bond coupon 3% nhưng price giảm xuống dưới par có YTM cao hơn 3%. Ngược lại bond coupon 7% giao dịch premium có YTM thấp hơn coupon rate.

YTM không phải guaranteed realized return. Nếu bạn bán trước maturity, issuer default, cash flows được reinvest ở rate khác hoặc bond có call option, realized return có thể khác đáng kể.

## 4. Yield-to-call và optionality

Callable bond cho issuer quyền redeem bond sớm theo terms. Khi rates giảm mạnh, issuer có incentive refinance debt cũ coupon cao bằng debt mới rẻ hơn, nên investor có thể mất upside mong đợi.

Vì vậy callable bond cần nhìn *yield-to-call*, *yield-to-worst* và call schedule, không chỉ YTM. Putable bond ngược lại cho investor một số quyền bán lại. Convertible bond thêm option đổi debt thành equity, khiến valuation vừa có bond floor vừa có equity optionality.

Một principle quan trọng: khi một fixed-income product trả yield cao bất thường, hãy hỏi investor đang short option nào hoặc chịu risk nào mà headline yield không nói ra.

## 5. Duration: đo độ nhạy với lãi suất

*Macaulay duration* có thể hiểu như weighted-average timing của cash flows. *Modified duration* chuyển khái niệm đó thành sensitivity gần đúng của price đối với yield.

Nếu modified duration bằng 7, yield tăng 1 percentage point thì price có thể giảm gần 7%, trước khi xét convexity:

`%ΔPrice ≈ -Modified Duration × ΔYield`

Bond maturity dài, coupon thấp và yield thấp thường có duration cao hơn. Đây là lý do long-duration government bonds có thể biến động mạnh dù credit quality cao.

## 6. DV01/PV01: một basis point đáng giá bao nhiêu?

*DV01* hay *PV01* đo thay đổi value xấp xỉ khi yield move 1 basis point, tức 0,01 percentage point. Nó hữu ích hơn duration khi quản lý portfolio bằng currency amount thay vì percentage.

Nếu portfolio có DV01 lớn, một movement nhỏ của yields cũng tạo P/L đáng kể. Professional rate-risk management thường nói bằng duration và DV01 thay vì chỉ bằng notional amount.

## 7. Convexity: tại sao duration chỉ là xấp xỉ tuyến tính

Price-yield relationship là curve chứ không phải straight line. *Convexity* đo curvature này. Với plain bond có positive convexity, price tăng do yield giảm thường lớn hơn price giảm do yield tăng cùng magnitude, so với approximation tuyến tính.

Khi rate move lớn, duration-only estimate kém chính xác. Optionality còn có thể làm convexity thay đổi: mortgage-backed securities có thể có negative convexity trong một số regimes vì prepayment behavior.

## 8. Key-rate duration và curve risk

Một bond portfolio không chỉ chịu parallel shift của toàn curve. 2Y yield có thể tăng trong khi 10Y gần như không đổi; long end có thể sell off trong khi front end ổn định.

*Key-rate duration* phân rã sensitivity theo maturity points. Điều này quan trọng với barbell, bullet hoặc liability-matching portfolios. Hai portfolios có cùng aggregate duration vẫn có curve exposure rất khác nhau.

## 9. Yield curve là gì?

Yield curve nối yields theo maturity. Front end thường nhạy với current/expected central-bank policy. Long end phản ánh expected future short rates, inflation risk, growth outlook, supply-demand và *term premium*.

Một decomposition hữu ích là:

`Long-term yield ≈ expected path of short rates + term premium`

Term premium là compensation mà investor yêu cầu để khóa vốn dài hạn trước uncertainty về inflation, rates và supply. Vì vậy 10Y yield có thể tăng dù market không kỳ vọng central bank hike thêm nếu term premium tăng.

## 10. Steepening và flattening phải đọc cùng direction của yields

Curve steepening chỉ nói gap long-short tăng; cần biết vì sao. *Bull steepener* thường xảy ra khi short yields giảm nhanh hơn long yields, có thể liên quan expectation easing/recession. *Bear steepener* xảy ra khi long yields tăng nhanh hơn, có thể do inflation, fiscal supply hoặc term premium.

Flattening cũng có bull/bear versions. Vì vậy không nên học thuộc “steepening tốt, inversion xấu”. Phải đọc front end, long end và macro shock cùng nhau.

## 11. Inversion và recession signal

Curve inversion xảy ra khi short yield cao hơn long yield ở một số maturities. Nó thường phản ánh restrictive current policy cùng expectation rằng rates sẽ thấp hơn trong tương lai.

Historically, inversion có thông tin về cycle nhưng không cho exact timing. Market có thể invert lâu trước slowdown; curve có thể re-steepen vì recessionary cuts hoặc vì long-end inflation/fiscal risk. Hai dạng re-steepening này có asset implications rất khác nhau.

## 12. Nominal yield, real yield và breakeven inflation

Nominal government yield có thể nghĩ gần đúng là real yield cộng expected inflation và premia. Inflation-linked securities như US TIPS cho market một reference cho real yield.

Breakeven inflation thường lấy nominal Treasury yield trừ TIPS real yield cùng maturity. Nhưng breakeven không phải pure expectation: inflation risk premium và liquidity differences cũng ảnh hưởng.

Real yield đặc biệt quan trọng với long-duration equities và gold. Real yield tăng làm discount rate cao hơn và opportunity cost của non-yielding gold lớn hơn, all else equal.

## 13. Treasury, agency, corporate và các lớp fixed income

Government securities thường là benchmark cho risk-free-ish rates trong currency đó, nhưng sovereign risk phụ thuộc monetary/fiscal structure. Agency hoặc quasi-government debt có support characteristics khác.

Corporate debt thêm business/default risk. Secured debt có collateral claims; unsecured debt dựa nhiều hơn vào enterprise creditworthiness; senior debt đứng trên subordinated debt trong claim priority. Preferred securities và hybrids có thể nằm giữa debt và equity về economics.

Không nên so two bonds chỉ bằng headline yield nếu seniority, collateral, maturity và embedded options khác nhau.

## 14. Credit spread là compensation cho nhiều thứ

Credit spread là yield premium so benchmark government/risk-free curve. Nó compensation cho expected default loss, uncertainty, liquidity, risk aversion và technical supply-demand.

Expected loss có intuition:

`Expected Credit Loss ≈ Probability of Default × Loss Given Default`

Nhưng market spread thường lớn hơn simple expected loss vì investor đòi risk premium và liquidity compensation.

## 15. Rating không thay thế credit analysis

Credit ratings tóm tắt agency assessment nhưng có thể lag market. Spread thường reprices nhanh hơn rating changes. Investment-grade bond vẫn có thể drawdown do spread widening, duration hoặc downgrade risk.

Credit analysis cần xem leverage, interest coverage, FCF, cyclicality, asset coverage, maturity schedule và access to capital. Một issuer EBITDA cao nhưng gần-term maturity wall lớn vẫn có refinancing risk nếu capital market đóng cửa.

## 16. Maturity wall và refinancing risk

Debt không cần default hôm nay để equity/bond holder gặp vấn đề. Nếu lượng lớn debt đáo hạn trong 12–24 tháng và refinancing rate cao hơn nhiều, interest burden tương lai có thể tăng mạnh.

Investor nên map từng maturity bucket, fixed/floating mix và secured/unsecured structure. “Net debt/EBITDA chỉ 3x” không đủ nếu EBITDA đang ở cycle peak hoặc major debt maturity đến trước cash recovery.

## 17. Spread duration

Corporate bond chịu hai sensitivity lớn: rate duration và spread duration. Treasury yields có thể giảm 100 bps nhưng credit spread widen 200 bps, khiến corporate bond vẫn giảm.

Đây là lý do high-yield bonds thường behave partly like equities: trong recession, risk-free yields giảm nhưng spreads có thể explode. Portfolio diversification phải nhìn total economic exposure, không chỉ asset label “bond”.

## 18. Credit cycle

Trong expansion, earnings tốt, defaults thấp và lending standards dễ; spreads thường compress. Leverage có thể tích tụ vì financing rẻ.

Khi policy tightens, growth slows hoặc collateral values fall, weak borrowers gặp refinancing pressure. Lenders thắt standards, spreads widen, new issuance khó hơn và defaults tăng. Credit cycle vì thế khuếch đại business cycle.

Một useful sequence là:

`easy credit → leverage build-up → shock → spread widening → refinancing stress → defaults/deleveraging → credit repair`

## 19. Floating-rate debt và rate resets

Floating-rate instruments có lower duration to benchmark rates nhưng coupon resets làm borrower interest burden thay đổi nhanh. Investor giảm price sensitivity với rates nhưng có thể tăng indirect credit risk vì borrower phải trả interest cao hơn.

Do đó floating-rate loan không đơn giản là “an toàn khi rates tăng”. Nếu rate rise làm debtor cash flow stress, credit losses có thể bù hết benefit từ higher coupons.

## 20. Inflation-linked bonds

Inflation-linked bonds điều chỉnh principal/cash flows theo inflation index theo rules. Chúng hữu ích khi muốn real purchasing-power exposure, nhưng price vẫn chịu real-yield duration.

Một investor có thể lỗ trên inflation-linked bond trong năm inflation cao nếu real yields tăng đủ mạnh. “Inflation bond” không có nghĩa price luôn tăng khi CPI tăng.

## 21. Mortgage-backed securities và negative convexity

Mortgage-backed securities (*MBS*) nhận cash flows từ pools of mortgages. Borrowers có prepayment option. Khi rates giảm, refinancing/prepayment có thể tăng, khiến investor nhận principal sớm đúng lúc muốn giữ high coupon. Khi rates tăng, prepayment chậm, duration kéo dài.

Đây là *negative convexity* intuition. Investor không chỉ chịu rate direction mà còn borrower optionality.

## 22. Sovereign debt: local currency và foreign currency

Sovereign phát hành debt bằng currency mà chính họ control có risk profile khác sovereign vay foreign currency. Local-currency sovereign có thể có lower nominal default risk nhưng investor vẫn chịu inflation/currency debasement risk.

Foreign-currency sovereign không thể tạo USD/EUR để repay, nên FX reserves, current account, external debt và access to international capital markets quan trọng hơn.

Foreign investor còn chịu translation risk. US Treasury tăng bằng USD nhưng KRW-based return có thể thấp hoặc âm nếu USD depreciates mạnh so KRW.

## 23. Bond ETF không giống individual bond

Individual bond held to maturity có remaining maturity giảm dần và, nếu không default, price converges toward principal repayment. A perpetual bond ETF thường bán bonds khi chúng ra khỏi target maturity range và mua bonds mới để duy trì duration profile.

Vì vậy “cứ giữ bond ETF tới đáo hạn” thường là sai conceptual model. Target-maturity bond ETF khác vì fund có planned terminal date nhưng vẫn phải đọc methodology, default handling và reinvestment policy.

## 24. Bond-fund liquidity

ETF share có thể liquid dù underlying bonds OTC và less liquid. Trong stress, ETF price có thể trade discount/premium so estimated NAV. Điều này không nhất thiết chứng minh ETF “broken”; đôi lúc ETF price đang price underlying market nhanh hơn stale dealer marks.

Investor cần nhìn spread, fund AUM, underlying quality, duration và creation/redemption mechanism, không chỉ expense ratio.

## 25. Bond ladder và liability matching

Nếu bạn biết sẽ cần cash ở các dates cụ thể, laddering có thể giảm reinvestment concentration. Một ladder gồm bonds maturities trải theo thời gian, tạo scheduled principal cash flows.

Liability matching tập trung vào việc asset cash flows/duration phù hợp obligations. Đây là tư duy khác “mua bond vì nghĩ rates sẽ giảm”. Một portfolio có thể dùng bond chủ yếu để bảo vệ khả năng chi trả tương lai hơn là để forecast market.

## 26. Khi nào long-duration bond diversifies equity?

Long government bonds thường diversifying tốt trong demand-driven recession/deflation khi growth và inflation expectations giảm, yields fall. Nhưng trong inflation shock, cả equities và long bonds có thể giảm cùng lúc vì discount rates và inflation uncertainty tăng.

Do đó stock-bond correlation là regime-dependent. Portfolio design phải stress both recession và inflation scenarios.

## 27. Checklist phân tích một bond hoặc bond ETF

Trước khi mua, cần trả lời: issuer là ai, seniority/collateral ra sao, maturity/call date thế nào, coupon fixed hay floating, YTM/yield-to-worst bao nhiêu, duration/DV01 thế nào, spread so benchmark là bao nhiêu, rating và market-implied risk có phù hợp không, maturity wall/refinancing risk ra sao, currency exposure gì, liquidity thế nào và worst plausible scenario là gì.

Với bond ETF, thêm weighted duration, average credit quality, holdings concentration, underlying liquidity, distribution yield vs SEC-like yield methodology nếu có, tracking, fees và FX hedge.

## 28. Mental model cuối cùng

Bond return không thể rút gọn thành “nhận coupon”. Hãy tách:

`Income + rate movement + curve movement + credit-spread movement + optionality + FX + default/recovery + fees`

Một fixed-income position chỉ được hiểu đúng khi investor biết mỗi component đóng góp gì vào expected return và downside.