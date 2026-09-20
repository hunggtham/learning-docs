# Trái phiếu, lãi suất và Credit

> Trái phiếu không phải chỉ là “sản phẩm an toàn trả coupon”. Một bond là chuỗi **contractual cash flows** chịu đồng thời lãi suất (*interest-rate risk*), lạm phát (*inflation risk*), tín dụng (*credit risk*), thanh khoản (*liquidity risk*), optionality, reinvestment risk và đôi khi cả FX risk. Chapter này xây fixed-income thinking từ present value tới yield curve, carry/roll-down, spread, default/recovery, securitized credit và portfolio implementation.

## 1. Bond là một hợp đồng cho vay

Bond holder cho issuer vay capital và nhận cash flows theo hợp đồng. **Face value / par value** là principal tham chiếu, **coupon** là interest payment, còn **maturity** là thời điểm principal được hoàn trả nếu issuer không default.

Một bond 5 năm face value 1.000, coupon 4% có thể trả 40 mỗi năm và 1.000 ở maturity. Nhưng market price hôm nay không nhất thiết bằng 1.000 vì investor discount toàn bộ future cash flows bằng yield phù hợp với maturity, credit, liquidity và optionality.

Bond holder đứng cao hơn common equity trong capital structure, nhưng upside thường bị giới hạn vào contractual payments. Vì vậy bond analysis tập trung nhiều vào **khả năng tránh mất vốn** hơn equity analysis.

## 2. Bond price là present value của future cash flows

Khung định giá cơ bản:

```text
Bond Price = Σ Coupon_t / (1 + y)^t + Face Value / (1 + y)^T
```

Khi required yield tăng, present value của fixed cash flows giảm nên price giảm. Đây là lý do government bond vẫn có thể drawdown mạnh dù issuer không hề default.

Phải phân biệt **credit safety** và **price stability**. Treasury dài hạn có credit quality cao nhưng duration rất lớn, nên vẫn có thể biến động mạnh khi yields thay đổi.

## 3. Coupon, Current Yield và Yield to Maturity

**Coupon rate** dựa trên par value. **Current yield** gần đúng bằng annual coupon chia current market price. **Yield to Maturity (YTM)** là internal rate khiến present value của các contractual cash flows bằng market price dưới một số assumptions.

YTM không phải realized return được đảm bảo. Nếu investor bán trước maturity, issuer default, cash flows được reinvest ở rate khác hoặc bond bị call, realized return sẽ khác.

Khi so bonds, không chỉ hỏi “coupon bao nhiêu?”, mà phải hỏi “yield nào phản ánh price hiện tại và các quyền embedded trong contract?”.

## 4. Yield to Call và Yield to Worst

Callable bond cho issuer quyền redeem bond sớm. Nếu rates giảm, issuer có incentive refinance coupon cao bằng debt mới rẻ hơn. Investor khi đó mất một phần upside kỳ vọng.

Vì vậy callable bond cần xem **Yield to Call (YTC)** và **Yield to Worst (YTW)**. YTW là yield thấp nhất trong các redemption scenarios hợp lệ, hữu ích để tránh bị headline YTM đánh lừa.

Nguyên tắc quan trọng: yield cao bất thường thường là compensation cho một risk hoặc một option mà investor đang bán.

## 5. Clean Price, Dirty Price và Accrued Interest

Bond thường quote theo **clean price**, chưa bao gồm accrued interest từ coupon period hiện tại. Amount thanh toán thực tế thường là **dirty price = clean price + accrued interest**.

Điều này quan trọng khi so price chart với transaction cash. Bond có thể “tăng giá” về dirty price đơn giản vì coupon accrual tích lũy, rồi giảm vào ex-coupon date mà không có thay đổi economic value tương đương.

## 6. Macaulay Duration và Modified Duration

**Macaulay duration** là weighted-average timing của cash flows. **Modified duration** chuyển nó thành sensitivity gần đúng của price với yield:

```text
%ΔPrice ≈ -Modified Duration × ΔYield
```

Bond duration 7 có thể giảm khoảng 7% nếu yield tăng 100 bps, trước convexity. Duration cao thường đi cùng maturity dài, coupon thấp và yield thấp.

Duration vì vậy là đơn vị tốt hơn maturity khi quản lý rate risk.

## 7. DV01 / PV01

**DV01** hoặc **PV01** đo dollar/currency change trong value nếu yield move 1 basis point.

Ví dụ portfolio DV01 = 2 triệu KRW nghĩa yield parallel shift +1 bp có thể làm value giảm khoảng 2 triệu KRW. Professional rates desks dùng DV01 vì nó cho phép cộng/trừ sensitivities giữa bonds, swaps và futures.

Notional không nói đủ. Hai bond có cùng 100 triệu notional nhưng DV01 rất khác nếu duration khác nhau.

## 8. Convexity

Price-yield relationship là curve chứ không tuyến tính. **Convexity** đo curvature.

Plain fixed-rate bond thường có positive convexity: khi yields giảm, price gain thường lớn hơn price loss khi yields tăng cùng magnitude so với linear duration approximation.

Optionality có thể đảo đặc tính này. Mortgage-backed securities có thể có negative convexity vì prepayment option của borrowers.

## 9. Effective Duration khi bond có option

Với callable bonds, MBS hoặc instruments có cash flows thay đổi khi rates đổi, traditional duration dựa contractual schedule có thể sai.

**Effective duration** dùng model để shock rates và re-estimate expected cash flows. Đây là cách phù hợp hơn khi borrower/issuer có quyền thay đổi timing của cash flows.

## 10. Key-Rate Duration

Yield curve hiếm khi dịch chuyển hoàn toàn parallel. **Key-rate duration** phân rã sensitivity theo 2Y, 5Y, 10Y, 30Y hoặc các maturities khác.

Hai portfolios có cùng total duration nhưng một portfolio concentrated ở 2–5Y và portfolio kia ở 20–30Y có curve risk rất khác.

Điều này quan trọng khi xây **barbell**, **bullet** hoặc liability-matching portfolio.

## 11. Yield Curve

Yield curve nối yields theo maturity. Front end nhạy policy-rate expectation; long end phản ánh expected future short rates, inflation, growth, fiscal supply và **term premium**.

Một decomposition hữu ích:

```text
Long Yield ≈ Expected Short-Rate Path + Term Premium
```

10Y yield có thể tăng dù market không price thêm hikes nếu term premium tăng do inflation uncertainty hoặc Treasury supply.

## 12. Bull/Bear Steepener và Flattener

Chỉ nói “curve steepening” là chưa đủ.

**Bull steepener**: yields giảm nhưng short end giảm nhanh hơn, thường gắn với easing/recession expectations.

**Bear steepener**: long yields tăng nhanh hơn, thường liên quan inflation, fiscal supply hoặc term-premium shock.

**Bull flattener** và **bear flattener** cũng có mechanics khác nhau. Luôn nhìn direction từng point trên curve.

## 13. Curve Inversion

Inversion thường xuất hiện khi current policy restrictive nhưng market kỳ vọng future rates thấp hơn.

Nó có historical information về recession risk nhưng không cho timing chính xác. Quan trọng hơn là hiểu **tại sao curve đang re-steepen** sau inversion: vì front-end easing hay vì long-end inflation/fiscal stress.

## 14. Nominal Yield, Real Yield và Breakeven

Nominal yield có thể phân tích gần đúng thành real yield + expected inflation + premia.

Breakeven inflation thường được suy ra từ nominal Treasury minus TIPS real yield. Nhưng breakeven không phải pure inflation forecast vì chịu liquidity và inflation-risk premium.

Real yield là một cross-asset variable quan trọng: rising real yields thường pressure long-duration bonds, long-duration equities và gold all else equal.

## 15. Carry trong Fixed Income

**Carry** là return investor nhận nếu market state không thay đổi đáng kể, thường gồm coupon/accrual và funding effects.

Một bond có yield cao hơn cash tạo positive carry, nhưng carry có thể bị xóa nhanh bởi rate/spread move bất lợi.

Không nên coi carry là “free yield”. Nó thường là compensation cho duration, credit, liquidity hoặc optionality risk.

## 16. Roll-Down

Nếu yield curve upward sloping và bond aging từ maturity dài xuống maturity ngắn hơn, nó có thể “roll down” tới point có yield thấp hơn, tạo price appreciation nếu curve shape không đổi.

Fixed-income expected return thường được phân tích:

```text
Expected Return ≈ Carry + Roll-Down + Rate Move + Spread Move + Optionality + FX - Costs
```

Carry/roll-down là lý do một bond có thể tạo return ngay cả khi central bank không cut.

## 17. Reinvestment Risk

Coupon/principal nhận trước maturity phải được reinvest. Nếu rates giảm mạnh, future reinvestment return thấp hơn.

Investor cần phân biệt **price risk** và **reinvestment risk**. Long-duration zero-coupon bond có price risk cao nhưng reinvestment risk thấp; short bills có price risk thấp nhưng phải roll thường xuyên nên reinvestment risk cao.

## 18. Treasury, Agency và Corporate Credit

Government debt thường làm benchmark curve cho currency đó. Agency/quasi-government securities có support structure riêng. Corporate debt thêm operating/default risk.

Trong corporate capital structure, secured debt đứng trên unsecured; senior trên subordinated; hybrids/preferred nằm giữa debt và equity về economics.

Yield comparison chỉ meaningful sau khi normalize seniority, collateral, maturity và embedded options.

## 19. Credit Spread

Credit spread là premium trên benchmark government/risk-free curve. Nó bù cho expected default loss, uncertainty, liquidity, risk aversion và technical supply-demand.

Simple intuition:

```text
Expected Credit Loss ≈ Probability of Default × Loss Given Default
```

Market spread thường lớn hơn pure expected loss vì investor cần risk premium.

## 20. Spread Duration

Corporate bond chịu cả rate duration và spread duration.

Ví dụ Treasury yield -100 bps nhưng credit spread +200 bps vẫn có thể làm bond giảm. Đây là lý do high-yield bonds thường có downside giống equities trong recession.

Bond label không đảm bảo diversification; phải biết exposure là government duration hay risky credit.

## 21. Z-Spread và Option-Adjusted Spread

**Z-spread** là spread cố định thêm vào spot curve để discount contractual cash flows tới market price.

Với bond có embedded option, **Option-Adjusted Spread (OAS)** cố gắng loại giá trị option để so pure credit/liquidity spread tốt hơn.

OAS useful hơn raw yield spread cho callable bonds/MBS, nhưng phụ thuộc model assumptions về rates và prepayment.

## 22. Rating và Market-Implied Credit Risk

Rating agency opinion hữu ích nhưng có thể lag. Market spreads, CDS, equity volatility và funding access có thể phản ứng sớm hơn downgrade.

Credit analysis phải dựa leverage, interest coverage, FCF, cyclicality, asset coverage, maturity schedule và access to capital chứ không chỉ rating letter.

## 23. Gross Leverage, Net Leverage và Interest Coverage

**Gross leverage** nhìn debt/EBITDA; **net leverage** trừ cash. Nhưng cash có thể restricted hoặc cần cho operations.

Interest coverage nên stress cả numerator và denominator: EBITDA có thể giảm đúng lúc refinancing rate tăng.

Một issuer 3x leverage ở cyclical peak có thể rủi ro hơn issuer 4x leverage với recurring contracted cash flows.

## 24. Maturity Wall

Map debt maturities theo từng năm. Refinancing concentration thường quan trọng hơn total debt headline.

Nếu 60% debt đáo hạn trong 18 tháng khi market spreads rộng, company có thể phải refinance đắt, sell assets, issue equity hoặc restructure.

Bond investor nên hỏi: cash + FCF + committed facilities có đủ để bridge tới thời điểm capital markets bình thường hóa không?

## 25. Liquidity Runway

**Liquidity runway** gồm unrestricted cash, expected FCF, undrawn revolver và other committed sources so với debt maturities, capex và working-capital needs.

Một credit có accounting solvency tốt nhưng liquidity runway ngắn vẫn có default/refinancing risk lớn.

## 26. Default Probability và Recovery

Default không đồng nghĩa recovery = 0. Recovery phụ thuộc enterprise value, collateral, seniority, legal process và restructuring costs.

Senior secured bond có thể recover đáng kể trong default trong khi subordinated debt gần như mất toàn bộ.

Expected credit loss phải model cả **PD** và **LGD**, không chỉ probability of default.

## 27. Fallen Angels và Rising Stars

**Fallen angel** là issuer bị downgrade từ investment grade xuống high yield; technical forced selling có thể làm spread widen vượt fundamental deterioration.

**Rising star** là high-yield issuer cải thiện lên investment grade. Rating migration tạo technical flow ngoài operating performance.

Đây là ví dụ fixed-income market nơi mandate constraints tạo price pressure.

## 28. Credit Cycle

Một simplified sequence:

```text
Easy Credit
→ Leverage Build-Up
→ Shock / Policy Tightening
→ Spread Widening
→ Refinancing Stress
→ Defaults / Deleveraging
→ Balance-Sheet Repair
→ Spread Compression
```

Credit thường lead hoặc amplify business cycle vì funding conditions thay đổi trước reported earnings.

## 29. Loan Market và Floating-Rate Credit

Leveraged loans/private credit thường floating-rate nên benchmark-duration thấp hơn fixed bond. Nhưng borrower interest burden reprices nhanh.

Rate hike vì vậy chuyển risk từ investor duration sang borrower credit. “Floating rate” không đồng nghĩa defensive nếu company coverage collapse.

## 30. Covenants

Covenants có thể giới hạn leverage, require minimum coverage hoặc restrict asset transfers. **Maintenance covenants** test periodically; **incurrence covenants** trigger khi issuer muốn thực hiện action nhất định.

Covenant-lite structure cho borrower flexibility hơn nhưng giảm early-warning/protection cho lender.

## 31. Callable Bonds

Callable issuer thường exercise khi rates/spreads giảm. Investor bị **negative selection**: bond bị trả lại khi nó trở nên hấp dẫn nhất.

Callable credit vì vậy có upside cap và cần OAS/YTW analysis thay vì headline YTM.

## 32. Convertible Bonds

Convertible bond gồm debt floor + equity conversion option.

Khi stock thấp, behavior giống bond/credit; khi stock tăng mạnh, delta lên và behavior giống equity hơn. Investor phải hiểu conversion ratio, call/put features, dilution và credit floor.

## 33. Inflation-Linked Bonds

TIPS hoặc local equivalents bảo vệ principal/coupon theo inflation index rules nhưng vẫn chịu real-yield duration.

High CPI không guarantee positive total return nếu real yields tăng đủ mạnh.

Phải phân biệt **inflation carry**, breakeven move và real-rate move.

## 34. MBS và Prepayment Risk

Mortgage borrowers sở hữu implicit prepayment option. Khi rates giảm, refinancing tăng và investor nhận principal sớm; khi rates tăng, prepayment chậm và duration extends.

Đây là nguồn **negative convexity**.

MBS hedging flows có thể amplify Treasury rate moves vì investors điều chỉnh duration khi prepayment expectation thay đổi.

## 35. ABS và Securitized Credit

Asset-Backed Securities (*ABS*) package loans/receivables như auto loans, credit cards hoặc other cash-flow pools.

Analysis cần xem collateral quality, underwriting vintage, excess spread, subordination, waterfall và servicer quality.

Securitization không xóa credit risk; nó redistribute risk giữa tranches.

## 36. Tranche và Waterfall

Senior tranche nhận cash trước junior tranche. Junior/equity tranche absorb losses trước để protect senior.

Do đó same underlying pool có securities với risk profile rất khác nhau.

Credit enhancement, overcollateralization và reserve accounts cần được hiểu trước khi nhìn rating.

## 37. Sovereign Debt bằng Local Currency

Sovereign phát hành bằng currency mình control có nominal-default dynamics khác company. Government có taxation và monetary capacity nhưng investor vẫn chịu inflation, financial repression hoặc currency depreciation.

Fiscal credibility, institutional quality, debt maturity và local investor base matter.

## 38. Foreign-Currency Sovereign Debt

Nếu sovereign vay USD/EUR, họ không tự tạo foreign currency để repay. FX reserves, current account, export base, external debt và market access trở nên quan trọng.

Currency mismatch có thể biến depreciation thành debt crisis vì local-currency value của foreign debt tăng.

## 39. Bond ETFs khác Individual Bonds

Individual bond held to maturity “rolls down” tới maturity và, absent default, principal repayment. Perpetual bond ETF liên tục replace holdings để giữ duration/maturity bucket.

Vì vậy “giữ bond ETF tới đáo hạn” thường sai. Target-maturity ETFs là category khác và vẫn cần đọc methodology.

## 40. ETF Price Discovery trong Stress

Underlying corporate bonds có thể OTC và stale marks. ETF market price đôi khi move trước NAV estimates.

Discount to NAV trong stress không tự động nghĩa arbitrage/free bargain. Nó có thể phản ánh price discovery thực nhanh hơn accounting/dealer marks.

## 41. Bond Fund Distribution Yield vs Portfolio Yield

Distribution yield phản ánh cash distributions gần đây; portfolio yield/YTM phản ánh current holdings economics. Hai số có thể khác do old coupons, capital gains distributions hoặc changing rates.

Investor nên đọc yield methodology thay vì chọn fund theo highest displayed distribution yield.

## 42. Bond Ladder

Ladder chia maturities theo nhiều dates để tạo recurring principal cash flows và giảm concentration vào một reinvestment date.

Ladder đặc biệt hữu ích khi goals có cash requirements định kỳ và investor không muốn forecast rates.

## 43. Bullet và Barbell

**Bullet** concentrates maturities quanh một target date. **Barbell** kết hợp short và long maturities để đạt average duration tương tự nhưng khác convexity/curve sensitivity.

Không có structure luôn tốt hơn; choice phụ thuộc liabilities và curve view.

## 44. Immunization và Liability Matching

Portfolio immunization tìm cách match duration/PV của assets với liabilities để giảm sensitivity của funding ratio trước rate moves.

Liability-driven investor quan tâm khả năng chi trả tương lai hơn việc beat bond index từng quý.

Đây là cách fixed income khác hoàn toàn speculative rate trading.

## 45. Rate Hedging bằng Futures/Swaps

Bond portfolio có thể hedge duration bằng Treasury futures hoặc interest-rate swaps.

Hedge nên match DV01/key-rate exposures, không match notional đơn giản. Futures còn có cheapest-to-deliver và basis risk; swaps có counterparty/collateral considerations.

## 46. Credit Hedging

Credit risk có thể hedge bằng CDS/index products hoặc short credit ETFs tùy market. Nhưng hedge basis giữa cash bond và CDS có thể thay đổi.

Một hedge “theoretically correct” vẫn có residual liquidity/basis risk trong stress.

## 47. Relative Value trong Fixed Income

Relative-value analysis so bonds cùng issuer hoặc peers sau khi normalize maturity, seniority, option và liquidity.

Spread rẻ hơn peer không tự động mispricing; có thể phản ánh lower recovery, weaker covenant hoặc supply technicals.

## 48. Carry-to-Risk

Yield cao phải được đặt cạnh duration, spread duration, default loss và liquidity.

Một bond +150 bps carry nhưng 8-year spread duration có thể mất nhiều năm carry chỉ trong một spread shock nhỏ.

Hãy hỏi “tôi được trả bao nhiêu carry cho mỗi unit risk?” thay vì chỉ “yield cao hay thấp?”.

## 49. Scenario Analysis cho Bond Portfolio

Stress ít nhất các scenarios:

```text
1. Policy +100 bps, curve parallel.
2. Bull steepener recession.
3. Bear steepener fiscal/inflation shock.
4. Credit spread +200 bps.
5. Rate down 100 bps nhưng spread +300 bps.
6. FX -10% với foreign bond.
7. Liquidity discount / margin shock.
```

Scenario P/L giúp nhìn interaction giữa rate và credit thay vì một duration number.

## 50. Return Attribution

Fixed-income P/L nên tách:

```text
Coupon / Accrual
+ Carry
+ Roll-Down
+ Risk-Free Rate Move
+ Curve Shape Move
+ Credit Spread Move
+ Optionality
+ FX
+ Default / Recovery
- Fees / Execution
```

Nếu không attribution, investor dễ nhầm “bond selection skill” với tailwind từ falling rates.

## 51. Khi nào Long Government Bonds Diversify Equity?

Long sovereign bonds thường diversify tốt trong demand-led recession/disinflation khi yields fall.

Trong inflation/fiscal shock, bonds và equities có thể cùng giảm. Vì vậy stock-bond correlation phải được stress theo regime chứ không dùng one historical average.

## 52. Due-Diligence Checklist

Với individual bond: issuer, seniority, collateral, maturity/call, coupon type, YTM/YTW, duration/DV01, spread/OAS, rating, leverage, coverage, maturity wall, liquidity runway, covenant, FX, liquidity và recovery case.

Với bond ETF: thêm weighted duration, spread duration, credit-quality distribution, sector concentration, underlying liquidity, distribution-vs-portfolio yield, tracking, expense ratio, derivatives use và FX hedge.

## 53. Mental Model cuối cùng

Một fixed-income position nên được đọc theo chuỗi:

```text
Contractual Cash Flows
→ Discount Curve
→ Duration / Convexity
→ Carry / Roll-Down
→ Credit Spread
→ Default / Recovery
→ Optionality
→ Liquidity / Funding
→ FX
→ Portfolio Role
```

Bond investing không phải chỉ “nhận coupon”. Nó là quản lý timing của cash flows, probability of repayment và sensitivity của present value dưới nhiều states của rates, credit và liquidity.