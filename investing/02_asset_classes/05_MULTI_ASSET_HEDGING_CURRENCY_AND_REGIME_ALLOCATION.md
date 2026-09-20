# 05 — Multi-Asset, Hedging, Currency và Regime Allocation

Tài liệu này nối các asset classes riêng lẻ thành một portfolio thực tế. Mục tiêu là hiểu vì sao cùng một tài sản có thể hữu ích trong regime này nhưng gây hại trong regime khác, vì sao currency exposure có thể quyết định phần lớn kết quả của một nhà đầu tư quốc tế, và hedging nên được xem như công cụ quản trị rủi ro chứ không phải cách “xóa biến động miễn phí”.

## 1. Multi-Asset khác với việc mua nhiều sản phẩm

Một multi-asset portfolio không chỉ là danh sách stocks, bonds, gold và cash. Điều quan trọng hơn là mỗi tài sản đang mang những economic exposures nào: growth, inflation, rates, duration, credit, liquidity, FX, commodity beta hay volatility.

Một portfolio có mười sản phẩm nhưng tất cả cùng hưởng lợi khi real yields giảm vẫn có thể là một portfolio rất concentrated. Multi-asset chỉ thực sự có ý nghĩa khi các sleeves phản ứng khác nhau trước những shock quan trọng.

## 2. Growth–Inflation framework

Một mental model đơn giản nhưng hữu ích là hai trục growth và inflation. Nếu growth tăng và inflation ổn định, equities và credit thường có môi trường thuận lợi. Nếu growth giảm và inflation giảm, high-quality government bonds có thể tốt hơn. Nếu growth mạnh nhưng inflation tăng, commodities, value và cyclicals có thể outperform tương đối. Nếu growth giảm nhưng inflation cao, stagflation gây khó cho cả equities lẫn long-duration bonds.

Đây không phải luật cơ học. Starting valuation, positioning, policy response và nguyên nhân shock đều có thể làm asset reaction khác textbook.

## 3. Regime không phải một nhãn cố định

Regime là tập hợp trạng thái của growth, inflation, liquidity, policy và credit. Một economy có thể chuyển từ Goldilocks sang overheating, rồi tightening, rồi growth slowdown chỉ trong vài quý.

Do đó regime allocation tốt không phải đoán đúng một nhãn rồi all-in. Nó là quá trình cập nhật xác suất khi data và market pricing thay đổi.

## 4. Duration là một exposure xuyên asset classes

Duration không chỉ thuộc bond. Growth stocks cũng có thể được xem như **long-duration equities** vì phần lớn expected cash flow nằm xa trong tương lai. Khi real yields hoặc discount rates tăng, present value của những cash flows xa bị giảm mạnh hơn.

Một portfolio chứa long Treasuries và expensive growth stocks nhìn bề ngoài đa dạng nhưng có thể cùng chịu rising-real-yield shock. Đây là ví dụ kinh điển của hidden macro concentration.

## 5. Equity beta không chỉ là stock exposure

High-yield credit, leveraged loans, private credit và một số REIT có thể mang equity-like downside khi growth xấu và credit spreads widen. Trong crisis, correlation giữa risky credit và equities thường tăng.

Do đó nếu một allocation được coi là “defensive” chỉ vì nó là bond fund, investor có thể hiểu sai risk. Phải tách government duration risk khỏi corporate credit risk.

## 6. Credit–Equity linkage

Equity là residual claim; debt nằm cao hơn trong capital structure. Nhưng khi enterprise value giảm đủ sâu, cả equity và risky credit đều chịu pressure. Credit spreads có thể widen trước khi earnings collapse hoàn toàn vì bond market tập trung mạnh vào refinancing và default probability.

Một multi-asset framework tốt nên xem credit spreads như bridge giữa macro và equity risk.

## 7. Cash có vai trò vượt quá “đợi cơ hội”

Cash mang liquidity, optionality và gần như không có duration risk. Nó có thể làm portfolio underperform trong bull market nhưng giúp tránh forced selling và tạo capacity để rebalance trong stress.

Cash không phải free asset vì chịu inflation erosion và opportunity cost. Vai trò của nó phụ thuộc liabilities, horizon và current short-rate environment.

## 8. Currency exposure là một asset exposure riêng

Một Korean investor mua S&P 500 unhedged ETF chịu ít nhất hai return drivers: S&P 500 bằng USD và USD/KRW. Gần đúng:

`KRW return ≈ USD asset return + USD/KRW return + interaction term`

Nếu stock tăng 10% bằng USD nhưng USD giảm 8% so với KRW, home-currency return có thể chỉ còn rất nhỏ. Ngược lại, USD mạnh có thể cushion equity loss cho Korean investor.

## 9. Currency có thể diversify hoặc làm tăng risk

Foreign currency exposure đôi khi hedge local risk. Ví dụ USD có thể mạnh trong global risk-off, giúp cushion KRW portfolio. Nhưng nếu future liability là KRW, quá nhiều USD exposure lại tạo mismatch khi KRW mạnh trở lại.

Currency nên được nhìn theo household balance sheet, không chỉ từng brokerage account.

## 10. Trading currency, underlying currency và liability currency

Một ETF niêm yết bằng KRW không có nghĩa economic exposure bằng KRW. Bạn cần phân biệt **trading currency**, **underlying asset currency** và **liability currency**.

Ví dụ Korean-listed ETF mua US stocks unhedged: trading currency là KRW nhưng economic currency exposure chủ yếu vẫn là USD. Đây là lỗi hiểu phổ biến của retail investors.

## 11. Hedged và unhedged

Currency-hedged product dùng forwards, futures hoặc swaps để giảm FX exposure. Hedging có cost phụ thuộc interest-rate differential, transaction cost, basis và roll.

Unhedged không luôn “rủi ro hơn”; với horizon dài, foreign currency có thể diversify. Nhưng với goal ngắn hạn bằng home currency, hedging có thể hợp lý hơn.

## 12. Forward points và hedge cost

FX hedge cost không đơn giản là một fee cố định. Nó chịu tác động của interest-rate differential giữa hai currencies. Khi US rates cao hơn Korea rates, hedging USD back to KRW thường có economic cost khác so khi differential đảo chiều.

Vì vậy cùng một hedged ETF có thể có relative attractiveness rất khác ở các rate regimes khác nhau.

## 13. Hedge ratio

Hedging không nhất thiết là 0% hoặc 100%. Investor có thể hedge một phần để cân bằng FX risk và diversification benefit.

**Hedge ratio** nên gắn với horizon và liability certainty. Near-term liabilities thường justify hedge cao hơn speculative long-term foreign allocation.

## 14. Equity hedging bằng futures

Index futures có thể hedge portfolio beta nhanh và capital-efficient. Hedge ratio gần đúng có thể dựa trên portfolio beta và notional futures.

Nhưng hedge không hoàn hảo vì basis risk, sector mismatch và beta instability. Nếu portfolio small-cap growth nhưng hedge bằng broad large-cap index, residual risk vẫn lớn.

## 15. Hedging bằng options

Long put tạo convex downside protection với max loss bằng premium. Protective put giữ upside nhưng có recurring insurance cost.

Collar giảm premium bằng cách bán call, đổi lại giới hạn upside. Put spread giảm cost nhưng protection dừng sau một mức downside. Không có cấu trúc hedge miễn phí.

## 16. Tail hedge

Tail hedge được thiết kế để payoff mạnh trong extreme events. Problem là tail insurance thường bleed trong normal periods.

Một tail hedge tốt nên được đánh giá theo portfolio function: nó có giúp tránh forced selling, margin calls hoặc behavioral panic không? Nếu chỉ nhìn hedge P/L riêng lẻ, bạn có thể đánh giá sai vai trò của nó.

## 17. Inflation hedge phải xác định loại inflation

Commodity spike do supply shock khác demand-driven inflation. Gold phản ứng với real yields và USD. TIPS bảo vệ principal theo inflation index nhưng vẫn có duration. Real estate có rent pass-through nhưng chịu financing cost.

Do đó câu hỏi “asset nào hedge inflation tốt nhất?” thiếu context. Cần hỏi inflation đến từ đâu và horizon là bao lâu.

## 18. Deflation hedge

Trong deflationary recession với sovereign credibility ổn, cash và high-quality government bonds thường hữu ích vì nominal cash flows có giá trị tương đối hơn và policy easing kéo yields xuống.

Nhưng nếu deflation đi cùng sovereign crisis hay currency crisis, government bonds local-currency có thể phản ứng khác. Macro mechanism luôn quan trọng hơn label.

## 19. Commodity exposure và roll yield

Commodity futures return khác spot return do curve structure. Contango có thể tạo negative roll yield; backwardation có thể hỗ trợ positive carry.

Vì vậy allocation vào commodity ETF cần hiểu contract methodology, roll schedule và collateral return. Spot chart không đủ để suy ra fund return.

## 20. Gold trong multi-asset portfolio

Gold không tạo cash flow nhưng có thể diversify monetary, geopolitical và real-yield risk. Gold thường được coi safe haven nhưng short-term reaction vẫn phụ thuộc USD, real yields và liquidity needs.

Trong crisis, gold đôi khi cũng bị bán tạm thời để tạo cash. Vì vậy vai trò của nó nên được đánh giá qua cycle dài hơn một vài ngày.

## 21. Real estate và REIT trong regime framework

REIT có thể hưởng lợi từ nominal rent growth nhưng chịu cap-rate và refinancing risk. Higher inflation không tự động bullish nếu rates tăng nhanh hơn NOI.

Property type cũng quan trọng: data centers, logistics, offices, residential và retail phản ứng khác growth và structural demand shifts.

## 22. 60/40 portfolio

60/40 kết hợp growth exposure từ equities với duration/defensive exposure từ bonds. Nó hoạt động tốt hơn khi stock-bond correlation thấp hoặc âm.

Trong inflationary tightening, stocks và bonds có thể cùng giảm. Bài học không phải “60/40 chết”, mà là correlation regime thay đổi và starting yields matter.

## 23. Risk Parity

Risk parity phân bổ theo risk contribution thay vì capital weight. Vì bond volatility thường thấp, traditional risk parity có thể dùng leverage để tăng bond exposure.

Điểm yếu là khi stock-bond correlation đảo dương hoặc rates shock mạnh, leverage trên bonds làm drawdown lớn hơn dự kiến. Risk parity không loại bỏ regime risk.

## 24. All-Weather và permanent-portfolio thinking

Các frameworks này cố sở hữu exposures có thể sống qua growth/inflation regimes khác nhau. Giá trị lớn nhất nằm ở philosophy: không cần biết chắc tương lai để xây portfolio robust.

Copy tỷ trọng cố định mà không hiểu underlying risk thì mất tinh thần của framework.

## 25. Volatility targeting

Volatility targeting giảm exposure khi realized volatility tăng và tăng exposure khi volatility giảm. Mục tiêu là giữ risk ổn định hơn.

Nhược điểm là volatility thường tăng sau price decline, khiến strategy de-risk sau khi market đã giảm. Trong calm regime kéo dài, nó cũng có thể tăng leverage ngay trước shock.

## 26. Trend-following như diversifier

Managed-futures hoặc trend strategies có thể kiếm tiền từ persistent moves ở equities, rates, FX và commodities. Chúng thường được nghiên cứu như crisis diversifier vì có thể short markets.

Nhưng trend following không phải hedge instant. Sudden reversals hoặc range-bound markets có thể gây whipsaw.

## 27. Carry như risk premium

Carry xuất hiện ở FX, bonds, commodities và volatility. Carry strategy thường kiếm small positive returns trong normal periods nhưng có thể chịu sharp unwind trong stress.

Portfolio cần nhận diện hidden short-volatility exposure nếu nhiều sleeves cùng dựa vào carry.

## 28. Correlation matrix không đủ

Average correlation bỏ qua state dependence. Portfolio cần xem rolling correlation, downside correlation và crisis episodes.

Một pair có average correlation 0.2 nhưng correlation 0.8 khi equity crash không mang diversification như con số trung bình gợi ý.

## 29. Stress testing multi-asset

Stress tests nên bao gồm ít nhất: inflation shock, recession, USD spike, rate shock, credit spread blowout, commodity supply shock và simultaneous stock-bond selloff.

Mục tiêu không phải dự báo probability chính xác mà xem portfolio có hidden concentration và liquidity problem không.

## 30. Rebalancing across regimes

Rebalancing trong multi-asset portfolio nên dựa target weights hoặc risk bands. Khi một sleeve tăng mạnh, bán bớt có thể giữ risk ổn định.

Nhưng trước khi rebalance cần hỏi thesis/regime có thay đổi structurally không. Mechanical rebalancing không thay thế fundamental review.

## 31. Liquidity hierarchy

Cash, T-bills, large government bonds, large-cap ETFs, small caps, high-yield bonds, private credit và real estate có liquidity rất khác nhau.

Portfolio phải có đủ liquid assets để đáp ứng liabilities và margin without fire sale. Illiquidity premium chỉ đáng nhận nếu investor thực sự có capacity khóa vốn.

## 32. Private-market smoothing

Private assets thường được mark theo appraisal hoặc less-frequent transactions. Reported volatility vì vậy có thể thấp hơn economic volatility.

Không nên kết luận private equity hay private real estate diversify mạnh chỉ vì NAV series mượt. Correlation có thể bị understated do stale pricing.

## 33. Risk budgeting giữa asset classes

Capital weights nên đi cùng risk budgets. Equity sleeve, credit sleeve, duration sleeve, inflation sleeve và alternatives sleeve cần biết mình đóng góp gì cho total risk.

Nếu một 10% allocation commodity futures tạo 25% portfolio volatility, capital weight đang đánh lừa investor.

## 34. Strategic vs Tactical Allocation

Strategic allocation dựa goals và horizon. Tactical allocation điều chỉnh quanh strategic ranges theo valuation, macro hoặc positioning.

Tactical decision phải có expected edge rõ. Nếu không, frequent regime timing dễ trở thành performance chasing và transaction cost drag.

## 35. Regime probability framework

Thay vì nói “đang stagflation” như chắc chắn, hãy gán probability tương đối cho các paths: growth reacceleration, soft landing, recession, inflation resurgence.

Portfolio có thể nghiêng nhẹ theo highest-probability case nhưng vẫn giữ exposures cho alternative scenarios. Đây là cách giảm dependence vào single forecast.

## 36. Valuation và expected return trong allocation

Macro regime không đủ. Asset bắt đầu từ valuation quá cao có thể return kém dù regime đúng. Ngược lại valuation depressed có thể cushion downside.

Allocation decision tốt kết hợp three layers: economic regime, valuation và portfolio role.

## 37. Product implementation risk

Sau khi chọn exposure, product implementation mới bắt đầu. ETF structure, expense ratio, tracking, spread, tax, leverage reset, derivatives collateral và counterparty risk đều có thể làm realized return khác theoretical exposure.

Không nên dừng analysis ở asset-class label.

## 38. Household balance sheet

Investment portfolio chỉ là một phần total wealth. Human capital, pension, real estate, debt và currency of future income đều là implicit exposures.

Một software engineer có career income nhạy với tech cycle có thể không muốn toàn bộ financial assets cũng concentrated tech. Household-level diversification rộng hơn brokerage-level diversification.

## 39. Multi-country liabilities

Nếu household có future expenses ở nhiều currencies, currency allocation nên phản ánh liabilities đó. KRW, VND và USD exposures không nên được xem độc lập nếu goals trải trên Korea và Vietnam.

Liability-matched assets có thể giảm risk mà không cần dự báo FX.

## 40. Portfolio Construction thực tế

Quy trình nên đi theo thứ tự: goals → liabilities → liquidity → strategic risk exposures → risk budgets → currency policy → product selection → rebalancing → review.

Nếu bắt đầu từ “ETF nào đang hot”, portfolio dễ trở thành collection của narratives.

## 41. Checklist trước khi thêm một asset

Trước khi thêm exposure mới, hãy trả lời: return driver là gì, nó hedge risk nào, nó duplicate risk nào, expected downside trong stress, liquidity, currency, cost, tax, rebalancing rule và điều gì khiến thesis không còn hợp lệ.

Nếu không thể giải thích vai trò trong một đoạn ngắn, position đó có thể không cần thiết.

## 42. Kết luận

Multi-asset investing là quản lý một tập hợp economic sensitivities. Diversification thực sự không đến từ số lượng tickers mà từ việc sở hữu các return drivers khác nhau, với liquidity và currency phù hợp liabilities.

Hedging, regime allocation và rebalancing chỉ là tools. Chúng hữu ích khi phục vụ một portfolio design rõ ràng, nhưng không thể thay thế việc hiểu underlying risk.