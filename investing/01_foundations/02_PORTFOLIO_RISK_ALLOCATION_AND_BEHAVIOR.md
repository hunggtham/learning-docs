# Portfolio, risk allocation và hành vi nhà đầu tư

Portfolio management không phải bài toán tìm thật nhiều mã “tốt”, mà là bài toán thiết kế một hệ thống tài sản có thể phục vụ mục tiêu tài chính trong điều kiện tương lai không chắc chắn. Một portfolio tốt phải đồng thời xử lý return, risk, liquidity, horizon, liabilities, taxes, behavior và khả năng chịu drawdown. Nếu chỉ tối ưu expected return mà bỏ qua những yếu tố còn lại, portfolio có thể đúng trên spreadsheet nhưng thất bại ngoài đời.

## 1. Portfolio không phải danh sách ticker

Một portfolio là tập hợp **risk exposures** chứ không phải danh sách tên sản phẩm. Bạn có thể sở hữu mười ticker nhưng nếu tám ticker đều là technology growth, danh mục vẫn concentrated. Ngược lại, bốn assets có economic drivers khác nhau đôi khi đa dạng hóa tốt hơn nhiều.

Khi nhìn portfolio, hãy chuyển từ câu hỏi “tôi có bao nhiêu mã?” sang “tôi đang chịu những factor nào?”. Equity chịu earnings risk và valuation risk. Long bonds chịu duration và inflation risk. Corporate bonds thêm credit risk. Gold nhạy với real yields, USD và safe-haven demand. Foreign assets thêm currency risk. REIT có property cycle, refinancing và cap-rate risk. Một ETF rộng vẫn có thể tập trung vào vài mega-cap nếu index methodology dùng market-cap weighting.

## 2. Ba lớp của risk: market, funding và behavioral risk

**Market risk** là rủi ro asset price biến động bất lợi. **Funding/liquidity risk** là rủi ro bạn buộc phải bán khi giá xấu vì cần cash, margin call hoặc nghĩa vụ đến hạn. **Behavioral risk** là rủi ro chính bạn phá kế hoạch vì fear, greed, FOMO hoặc loss aversion.

Nhiều người chỉ nhìn market risk. Nhưng trong thực tế, việc phải bán stock lúc -30% để trả một khoản cần thiết thường nguy hiểm hơn bản thân drawdown -30%. Vì vậy emergency liquidity và liability matching là một phần của portfolio design, không phải phần phụ.

## 3. Risk tolerance, risk capacity và risk requirement

**Risk tolerance** là mức volatility và drawdown về tâm lý bạn chịu được. **Risk capacity** là mức loss tài chính bạn thực sự có thể chịu mà không phá mục tiêu. **Risk requirement** là mức return cần thiết để đạt mục tiêu.

Ba biến có thể xung đột. Một người thích risk nhưng cần tiền mua nhà trong một năm có capacity thấp cho equities. Một người còn 30 năm tới retirement có capacity cao hơn, nhưng nếu panic sell ở -15% thì allocation quá aggressive vẫn không thực tế.

Portfolio tốt phải nằm trong vùng giao nhau của ba biến này. Nếu return requirement quá cao so capacity, giải pháp không phải luôn tăng risk; đôi khi phải tăng savings rate, kéo dài horizon hoặc giảm mục tiêu.

## 4. Horizon không phải một con số duy nhất

Một household thường có nhiều horizons cùng lúc: emergency fund vài tháng, tiền đặt cọc nhà 2–3 năm, retirement 20–30 năm, và một phần capital có thể đầu tư vĩnh viễn.

Do đó một portfolio duy nhất với một risk profile duy nhất thường không phản ánh đúng thực tế. Có thể chia theo **goal buckets** hoặc **liability buckets**. Tiền có deadline gần cần ưu tiên principal stability và liquidity; tiền có horizon dài mới có capacity cao hơn cho equity volatility.

## 5. Liability matching và liquidity reserve

Liability matching nghĩa là tài sản phải tương thích với thời điểm, currency và certainty của future obligations. Nếu một khoản chắc chắn phải trả bằng KRW trong 12 tháng, sử dụng volatile USD equity để “kiếm thêm chút return” tạo mismatch không cần thiết.

Cash và short-duration high-quality instruments có expected return thấp hơn equity nhưng mang **option value**: chúng giúp bạn không phải forced seller khi market stress. Đây là lý do liquidity reserve có thể làm expected portfolio return thấp hơn một chút nhưng tăng xác suất đạt mục tiêu thực tế.

## 6. Expected return không thể tách khỏi distribution

Hai portfolios có cùng average return nhưng outcome khác rất nhiều nếu volatility, skewness và tail risk khác nhau. Một portfolio tăng đều 8% và một portfolio lúc +40%, lúc -30% có cùng average trong một số mẫu nhưng compounding khác mạnh.

Geometric return bị volatility drag. Nếu một asset tăng 50% rồi giảm 50%, arithmetic average bằng 0% nhưng capital từ 100 thành 75. Đây là lý do phải nhìn **compound growth rate**, drawdown và path, không chỉ average return.

## 7. Volatility là thước đo chưa hoàn hảo nhưng hữu ích

**Volatility** đo mức dispersion của returns. Nó không đồng nghĩa hoàn toàn với risk vì investor có thể không quan tâm temporary volatility nếu horizon dài và fundamental intact. Tuy nhiên volatility vẫn hữu ích vì nó ảnh hưởng sizing, rebalancing, leverage và xác suất drawdown.

Đặc biệt với leverage hoặc margin, volatility có thể biến thành permanent loss thông qua forced liquidation. Vì vậy một asset “cuối cùng hồi lại” vẫn có thể phá account nếu path quá xấu.

## 8. Drawdown và recovery math

Drawdown đo mức giảm từ peak xuống trough. Recovery không đối xứng với loss:

`Loss 10% → cần +11.1% để hồi`

`Loss 25% → cần +33.3%`

`Loss 50% → cần +100%`

`Loss 80% → cần +400%`

Điều này không có nghĩa phải tránh mọi drawdown. Nó có nghĩa position sizing phải ngăn một sai lầm đơn lẻ phá khả năng compounding dài hạn.

## 9. Diversification hoạt động nhờ covariance chứ không chỉ số lượng assets

Portfolio variance phụ thuộc volatility của từng asset, weight và **covariance** giữa chúng. Với hai assets, trực giác cơ bản là:

`σ²p = w1²σ1² + w2²σ2² + 2w1w2σ1σ2ρ12`

Trong đó `ρ12` là correlation. Nếu correlation thấp hoặc âm, total risk có thể thấp hơn weighted-average individual risk.

Nhưng correlation không cố định. Stocks và government bonds có thể diversify tốt trong disinflationary recession nhưng cùng giảm trong inflationary tightening. Vì vậy diversification phải dựa trên **economic drivers**, không chỉ historical matrix.

## 10. Correlation breakdown trong stress

Khi crisis xảy ra, nhiều participants cần cash cùng lúc. Assets tưởng khác nhau có thể cùng bị bán để đáp ứng margin calls hoặc redemption. Vì vậy correlation có thể tăng đúng lúc bạn cần diversification nhất.

Stress testing nên dùng cả scenarios “correlations converge toward one” hoặc “stocks and bonds both fall” thay vì chỉ dùng historical averages. Robust portfolio không giả định mọi relationship ổn định.

## 11. Capital allocation và risk contribution là hai chuyện khác nhau

Một portfolio 60% stocks và 40% bonds không có nghĩa 60% risk đến từ stocks. Nếu equity volatility cao hơn bond nhiều lần, equities có thể đóng góp phần lớn total risk.

**Risk contribution** trả lời câu hỏi một position đóng góp bao nhiêu vào portfolio volatility hoặc tail loss. Đây là nền tảng của risk budgeting.

Một thematic ETF weight 10% nhưng volatility 50% có thể ảnh hưởng portfolio nhiều hơn một bond allocation 30%. Vì vậy xem weight mà không xem risk là thiếu.

## 12. Marginal risk contribution

**Marginal contribution to risk** hỏi: nếu tăng position này thêm một chút, total portfolio risk tăng bao nhiêu? Một asset volatility cao nhưng correlation thấp có thể thêm ít portfolio risk hơn asset volatility thấp nhưng correlation gần 1 với holdings hiện tại.

Đây là lý do “asset này biến động mạnh nên luôn nguy hiểm” là cách nhìn chưa đủ. Risk phải được đánh giá trong context portfolio.

## 13. Concentration có nhiều dạng

Concentration không chỉ là một ticker quá lớn. Có ít nhất năm dạng thường gặp: company concentration, sector concentration, geography concentration, currency concentration và factor concentration.

Ví dụ nắm Samsung Electronics, SK hynix, semiconductor ETF và Nasdaq ETF có thể nhìn như bốn products nhưng cùng mang technology/AI/capex/growth/rate sensitivity. Cần nhìn through wrapper tới underlying exposures.

## 14. Factor exposure

Equity portfolio có thể nghiêng về **value, growth, quality, momentum, size, low volatility** hoặc sector beta. Bond portfolio có duration và credit factor. Commodity exposure có inflation và global-growth factor.

Factor awareness giúp phân biệt diversification thật và diversification bề mặt. Nếu mọi positions cùng hưởng lợi khi real yields giảm, portfolio có hidden long-duration bet.

## 15. Strategic Asset Allocation

**Strategic Asset Allocation (SAA)** là cấu trúc dài hạn dựa trên goals, liabilities, horizon và risk capacity. Nó không nên thay đổi mỗi tuần theo news.

SAA trả lời các câu hỏi lớn: bao nhiêu growth assets, defensive assets, liquidity, real assets và foreign currency exposure. Sau đó mới chọn cụ thể ETF, bonds hay stocks.

## 16. Tactical Asset Allocation

**Tactical Asset Allocation (TAA)** là điều chỉnh ngắn/trung hạn quanh strategic target dựa trên valuation, macro regime hoặc opportunities. Tactical overlay chỉ nên nhỏ nếu investor chưa có strong evidence về timing skill.

Sai lầm phổ biến là gọi mọi market timing theo cảm xúc là “tactical allocation”. Tactical process tốt phải có rule, range, catalyst và exit condition.

## 17. Rebalancing là risk-control rule

Rebalancing đưa weights về target khi market movement làm portfolio drift. Nếu equities từ target 60% lên 75%, bạn có thể bán bớt hoặc dùng new contributions để tăng defensive assets.

Rebalancing không phải prediction. Nó là cơ chế kiểm soát risk và buộc bạn bán tương đối bớt phần đã tăng nhiều để mua phần giảm weight.

## 18. Calendar vs threshold rebalancing

**Calendar rebalancing** thực hiện theo lịch, ví dụ mỗi quý hoặc năm. **Threshold rebalancing** chỉ thực hiện khi weight lệch quá một mức đã định. Threshold thường phản ánh risk tốt hơn vì không trade nếu allocation chưa lệch đáng kể.

Một approach kết hợp là review theo lịch nhưng chỉ rebalance khi vượt band. Như vậy giảm turnover và tax/transaction cost.

## 19. Rebalancing premium và giới hạn của nó

Rebalancing có thể tạo benefit khi assets mean-revert và correlation không quá cao. Tuy nhiên không tồn tại “rebalancing bonus” đảm bảo. Nếu một asset suy giảm structurally, blind rebalancing có thể liên tục mua thêm vào thesis đang chết.

Do đó rebalancing phải đi cùng thesis review. Target allocation không phải lý do bỏ qua thay đổi fundamental.

## 20. Sequence-of-returns risk

Trong accumulation phase, thứ tự returns thường ít quan trọng hơn vì investor còn đóng góp thêm tiền. Trong **decumulation phase**, thứ tự returns có thể quyết định survival của portfolio.

Nếu crash xảy ra ngay khi retirement bắt đầu và investor phải rút tiền, họ bán nhiều units ở low prices. Dù average return 20 năm giống nhau, ending wealth có thể thấp hơn nhiều so người gặp crash ở cuối period.

Sequence risk là lý do retirees thường cần liquidity bucket, bonds hoặc withdrawal flexibility.

## 21. Withdrawal rate và spending flexibility

Một fixed withdrawal rule đơn giản nhưng có thể quá cứng. Dynamic spending rules giảm withdrawal khi portfolio stress và tăng khi portfolio mạnh có thể cải thiện robustness.

Investor cần phân biệt **essential liabilities** và discretionary spending. Essential expenses nên được tài trợ bằng assets có uncertainty thấp hơn.

## 22. Inflation risk

Cash giảm real purchasing power khi inflation kéo dài. Long nominal bonds cũng chịu inflation risk. Equities, real estate, TIPS, commodities và gold có inflation sensitivities khác nhau nhưng không asset nào hedge hoàn hảo mọi loại inflation.

Portfolio cần phân biệt demand inflation, supply shock và monetary debasement narratives vì mỗi loại có transmission khác.

## 23. Currency risk trong portfolio quốc tế

Foreign asset return bằng home currency có hai components chính: underlying asset return và FX move. Với Korean investor nắm US equities unhedged:

`KRW return ≈ USD asset return + USD/KRW change + interaction`

Currency có thể diversify nhưng cũng tạo mismatch với liabilities. Hedging decision nên gắn với purpose của capital.

## 24. Leverage và path dependency

Leverage tăng both expected return và expected loss theo exposure, nhưng risk tăng phi tuyến do margin calls, volatility và drawdown.

Một 2x portfolio không đơn giản là “cùng strategy nhưng nhanh hơn”. Nếu assets giảm đủ mạnh trước khi hồi, leverage có thể buộc de-risk ở đáy. Vì vậy leverage phải được stress test theo path, không chỉ terminal return.

## 25. Risk budget

Risk budget định nghĩa trước portfolio có thể chịu bao nhiêu risk ở total level và từng sleeve. Ví dụ core long-term assets có budget lớn hơn thematic hoặc trading sleeve.

Risk budget tốt không chỉ đặt maximum weight; nó còn đặt maximum contribution to loss, maximum leverage, maximum currency mismatch và liquidity requirements.

## 26. Core–Satellite framework

**Core** thường là diversified, low-cost, scalable exposures phục vụ compounding dài hạn. **Satellite** là single stocks, themes, tactical trades hoặc alternatives nơi investor có thesis cụ thể.

Core–Satellite giúp tách “wealth-building engine” khỏi “high-conviction ideas”. Nếu satellite sai, core plan vẫn sống.

## 27. Behavioral finance: FOMO và recency bias

**FOMO** khiến investor tăng allocation sau khi asset đã tăng mạnh. **Recency bias** khiến vài năm gần nhất bị coi như trạng thái bình thường của tương lai.

Cách chống hiệu quả không phải tự nhắc “bình tĩnh”, mà là dùng allocation bands và pre-commitment rules. Khi rules đã định trước, cảm xúc có ít quyền can thiệp hơn.

## 28. Loss aversion, anchoring và disposition effect

**Loss aversion** khiến loss 10% gây đau hơn gain 10% tạo vui. **Anchoring** khiến giá mua trở thành reference dù market không quan tâm. **Disposition effect** khiến investor bán winner sớm nhưng giữ loser vì không muốn “chốt lỗ”.

Cure là thesis-based review: nếu thesis/value thay đổi, decision phải dựa forward expected return, không dựa purchase price.

## 29. Confirmation bias và narrative bias

Sau khi mua, investor dễ tìm information xác nhận thesis và bỏ qua evidence ngược. Narrative hấp dẫn có thể làm valuation bị lãng quên.

Một discipline hữu ích là viết trước **disconfirming evidence**: những dữ kiện nào nếu xuất hiện sẽ khiến thesis yếu đi hoặc sai. Điều này biến research thành falsification thay vì defense.

## 30. Home bias và familiarity bias

Investor thường overweight quốc gia, employer hoặc ngành quen thuộc. Familiarity làm asset cảm giác an toàn hơn nhưng không giảm economic risk.

Nếu income, real estate và career đều phụ thuộc Korea, thêm quá nhiều Korea equities có thể làm household balance sheet concentration cao hơn tưởng tượng.

## 31. Investment Policy Statement

**Investment Policy Statement (IPS)** là constitution của portfolio. Nó nên mô tả goals, horizon, liquidity needs, target allocation, acceptable ranges, concentration limits, rebalancing rules, leverage policy, tax/account constraints và review cadence.

IPS quan trọng nhất lúc market stress, vì khi đó decision quality thường giảm. Một rule được viết khi bình tĩnh tốt hơn một decision được nghĩ ra giữa panic.

## 32. Decision journal

Mỗi allocation change lớn nên ghi: thesis, expected return source, main risks, catalyst, invalidation, sizing logic và alternatives considered.

Sau vài tháng hoặc năm, journal giúp phân biệt skill và luck. Nếu result tốt nhưng reasoning sai, không nên học sai lesson. Nếu result xấu nhưng process đúng, có thể chỉ là adverse outcome trong distribution.

## 33. Performance attribution

Portfolio return nên được tách thành market beta, asset allocation, security selection, currency, income, fees, tax và behavior.

Nếu portfolio underperform vì intentionally giữ cash cho liability, đó khác underperform do chọn stock tệ. Attribution giúp review đúng layer thay vì phản ứng cảm xúc với total return.

## 34. Benchmark phải phù hợp mandate

Portfolio Korean small caps không nên được đánh giá chỉ bằng S&P 500. Global balanced portfolio không “thất bại” chỉ vì Nasdaq tăng mạnh một năm.

Benchmark phải phản ánh opportunity set và risk budget. Nếu benchmark sai, performance interpretation cũng sai.

## 35. Time-weighted và money-weighted return

**Time-Weighted Return (TWR)** loại bớt ảnh hưởng timing của external cash flows và hữu ích để đánh giá strategy/manager. **Money-Weighted Return (MWR/IRR)** phản ánh trải nghiệm thực của investor vì tính thời điểm deposit/withdrawal.

Một investor có thể dùng strategy tốt nhưng MWR thấp vì đổ nhiều tiền vào đúng peak. Vì vậy behavior và cash-flow timing có thể quan trọng ngang product selection.

## 36. Stress testing

Stress test không cần dự báo chính xác. Mục tiêu là hỏi “nếu điều xấu hợp lý xảy ra, portfolio còn hoạt động không?”. Scenarios có thể gồm equity -40%, yields +200 bps, KRW tăng/giảm mạnh, credit spreads widening, unemployment shock hoặc simultaneous stock-bond decline.

Nếu một scenario hợp lý buộc bán house savings hoặc tạo margin call, design cần sửa trước khi scenario xảy ra.

## 37. Scenario analysis và probability ranges

Không nên xây một forecast duy nhất. Base/bull/bear scenarios giúp nhìn distribution outcomes. Probabilities chỉ là judgment, nhưng việc buộc phải viết alternative paths làm giảm overconfidence.

Portfolio robust không đòi hỏi forecast đúng một kịch bản; nó cố sống được qua nhiều kịch bản khác nhau.

## 38. Portfolio review cadence

Daily review thường gây overtrading với long-term portfolio. Một cadence hợp lý hơn là monitoring events khi cần, monthly allocation/risk check, quarterly thesis review và annual IPS review.

Tần suất review phải phù hợp horizon. Càng dài hạn, càng phải tránh để noise ngắn hạn điều khiển allocation.

## 39. Khi nào nên thay strategic allocation?

Strategic allocation nên thay khi goals, liabilities, income stability, family situation, horizon, tax/account structure hoặc risk capacity thay đổi đáng kể. Nó không nên thay chỉ vì một headline hoặc một năm asset class underperform.

Market valuation có thể ảnh hưởng tactical ranges, nhưng core plan cần độ ổn định để compounding hoạt động.

## 40. Một framework kiểm tra position mới

Trước khi thêm một position, hãy trả lời bằng văn bản: exposure là gì, return driver ở đâu, correlation với portfolio hiện tại, worst plausible loss, liquidity, currency, role trong portfolio, sizing và invalidation condition.

Nếu không thể trả lời những câu này, position có thể chỉ là một trade cảm xúc đội lốt investment.

## 41. Kết luận

Portfolio management là engineering under uncertainty. Mục tiêu không phải tối đa hóa return của một năm mà tối đa hóa xác suất đạt goals sau khi tính market risk, liquidity, behavior, taxes và unexpected life events.

Một portfolio tốt là portfolio bạn hiểu, có thể giữ đúng process trong drawdown và không cần một forecast hoàn hảo để tồn tại.