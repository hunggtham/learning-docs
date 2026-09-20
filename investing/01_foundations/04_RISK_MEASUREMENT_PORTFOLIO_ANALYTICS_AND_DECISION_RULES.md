# 04 — Đo lường rủi ro, Portfolio Analytics và quy tắc ra quyết định

Tài liệu này bổ sung lớp định lượng còn thiếu giữa việc “biết diversification” và khả năng thực sự đánh giá một danh mục. Mục tiêu không phải biến đầu tư thành bài toán thuần toán học, mà giúp người đọc hiểu các con số như volatility, covariance, beta, Sharpe hay drawdown đang đo điều gì, chúng bỏ sót điều gì và nên được dùng thế nào trong quyết định thực tế.

## 1. Return không chỉ có một cách đo

Nếu một tài sản tăng từ 100 lên 110, simple return là 10%. Nếu sau đó giảm từ 110 về 99, kỳ thứ hai là -10%, nhưng tổng cộng bạn không quay về 100 mà còn 99. Đây là lý do arithmetic average có thể gây ảo giác. Hai kỳ +10% và -10% có arithmetic average bằng 0%, nhưng compound return lại âm.

Geometric return phản ánh tốt hơn tốc độ tăng trưởng vốn qua nhiều kỳ. Với chuỗi return `r1, r2, ..., rn`, growth factor là tích của `(1+r)`. Annualized geometric return vì vậy phù hợp hơn khi hỏi “vốn thực sự tăng với tốc độ bao nhiêu”.

Khi có cash flow vào ra, cần tách Time-Weighted Return khỏi Money-Weighted Return. TWR đánh giá performance của strategy ít bị méo bởi thời điểm nạp tiền; MWR phản ánh trải nghiệm tiền thật của chính nhà đầu tư.

## 2. Volatility là dispersion, không phải toàn bộ risk

Volatility thường là standard deviation của returns. Nó cho biết returns dao động quanh average mạnh đến mức nào. Một tài sản có volatility 20% thường biến động mạnh hơn tài sản 5%, nhưng volatility không cho biết nguyên nhân, thanh khoản hay khả năng permanent loss.

Một government bond ngắn hạn và một illiquid private asset có thể cùng hiện volatility thấp, nhưng risk thực tế rất khác. Private asset đôi khi trông “ổn định” chỉ vì không có market price cập nhật mỗi ngày. Vì vậy volatility là market-risk statistic, không phải định nghĩa hoàn chỉnh của risk.

## 3. Downside risk và drawdown

Drawdown đo mức giảm từ equity peak xuống trough. Nếu portfolio đạt 100 triệu, giảm xuống 70 triệu rồi phục hồi, maximum drawdown của giai đoạn đó là 30%.

Drawdown đặc biệt quan trọng vì recovery không đối xứng. Mất 20% cần tăng 25% để về hòa vốn. Mất 50% cần tăng 100%. Do đó một strategy có expected return cao nhưng thường xuyên drawdown 60% có thể không usable cho phần lớn nhà đầu tư.

Ulcer Index, downside deviation và Expected Shortfall là các cách cố tập trung nhiều hơn vào phần giảm thay vì coi upside volatility cũng xấu như downside volatility.

## 4. Correlation và covariance

Diversification hoạt động vì assets không di chuyển hoàn toàn giống nhau. Correlation gần +1 nghĩa hai tài sản thường đi cùng chiều mạnh; gần -1 nghĩa chúng có xu hướng đi ngược chiều; gần 0 nghĩa relationship tuyến tính yếu.

Nhưng correlation không bất biến. Trong crisis, nhiều risky assets có thể trở nên tương quan cao hơn vì cùng bị deleveraging. Một portfolio tưởng đa dạng trong thời bình có thể trở nên concentrated đúng lúc cần diversification nhất.

Covariance đưa cả mức biến động và quan hệ đồng biến vào cùng một đại lượng. Portfolio variance vì vậy phụ thuộc không chỉ variance từng asset mà cả covariance giữa chúng. Đây là nền toán học của diversification.

## 5. Portfolio volatility

Với hai assets A và B, portfolio variance có thể viết đơn giản là:

`σp² = wA²σA² + wB²σB² + 2wAwBσAσBρAB`

Điểm quan trọng nằm ở term cuối. Nếu correlation thấp, total portfolio risk có thể thấp hơn weighted average risk của từng asset. Vì vậy diversification không có nghĩa mua nhiều ticker; nó có nghĩa kết hợp return drivers khác nhau.

## 6. Beta và systematic risk

Beta đo độ nhạy của asset so với benchmark. Beta 1,2 nghĩa trong sample đo lường, asset có xu hướng biến động mạnh hơn benchmark khoảng 20% theo hướng market movement. Nhưng beta là thống kê lịch sử, không phải hằng số vật lý.

Một company thay đổi leverage, business mix hoặc sector regime có thể làm beta thay đổi. Beta cũng phụ thuộc benchmark và time window. Do đó không nên dùng beta như nhãn cố định kiểu “stock này risk = 1,3”.

## 7. Alpha và benchmark

Alpha chỉ có nghĩa khi benchmark phù hợp. Nếu một portfolio semiconductor tăng 25% khi broad market tăng 10%, việc nói alpha 15% là quá đơn giản nếu semiconductor sector tăng 30%. Benchmark đúng có thể là sector index chứ không phải broad index.

Performance attribution nên tách market exposure, sector exposure, factor exposure và security selection. Một investor tưởng mình chọn stock giỏi có thể thực ra chỉ đang overweight momentum hoặc high-beta growth đúng chu kỳ.

## 8. Tracking Error và Active Share

Tracking Error đo độ biến động của excess return so với benchmark. Portfolio càng khác benchmark theo thời gian, tracking error thường càng lớn.

Active Share đo khác biệt trong holdings weights. Hai portfolio có thể có Active Share cao nhưng tracking error thấp nếu exposures bù nhau. Ngược lại futures overlay có thể tạo tracking error đáng kể dù holdings underlying gần benchmark.

## 9. Sharpe, Sortino và Calmar

Sharpe Ratio lấy excess return chia volatility. Nó hữu ích để so efficiency của return trên mỗi đơn vị volatility, nhưng giả định ngầm rằng volatility hai chiều đều là điều cần penalize.

Sortino dùng downside deviation nên phù hợp hơn khi upside volatility không bị coi là xấu. Calmar so annualized return với maximum drawdown và đặc biệt hữu ích cho strategies có drawdown là vấn đề lớn.

Không metric nào đủ một mình. Strategy có Sharpe đẹp vẫn có thể ẩn tail risk; strategy selling options thường là ví dụ điển hình nếu chỉ nhìn return ổn định trước khi shock xuất hiện.

## 10. Value at Risk và Expected Shortfall

VaR cố trả lời câu hỏi: với confidence level nhất định, loss threshold nào thường không bị vượt trong một horizon. Ví dụ one-day 95% VaR 2% có nghĩa model ước lượng khoảng 95% ngày loss sẽ không vượt 2%.

Nhưng VaR không nói loss tệ đến mức nào trong 5% còn lại. Expected Shortfall cố giải quyết điểm đó bằng cách đo average loss khi đã vượt threshold.

Hai metric đều phụ thuộc model và dữ liệu lịch sử. Nếu distribution thay đổi hoặc có gap event chưa từng xuất hiện trong sample, con số có thể tạo cảm giác chính xác giả.

## 11. Efficient Frontier và giới hạn của optimization

Mean-variance optimization tìm combination có expected return cao nhất cho một mức variance hoặc variance thấp nhất cho một expected return. Về lý thuyết, nó tạo efficient frontier.

Vấn đề lớn là expected returns rất khó ước lượng. Chỉ cần thay nhẹ assumptions, optimizer có thể chuyển allocation cực mạnh. Vì vậy trong thực tế, robust portfolio construction thường dùng constraints, shrinkage, broad diversification và qualitative judgment thay vì tin tuyệt đối vào output tối ưu.

## 12. Risk contribution và concentration ẩn

Capital weight không bằng risk weight. Một asset có volatility cao có thể đóng góp phần lớn total risk dù chỉ chiếm tỷ trọng vốn vừa phải.

Risk contribution giúp trả lời “asset nào thực sự quyết định biến động portfolio”. Một portfolio 60% bonds và 40% equities có thể vẫn có phần lớn risk đến từ equities.

Điều tương tự xảy ra với thematic ETFs. Ba quỹ khác tên nhưng cùng top holdings có thể tạo concentration ẩn.

## 13. Stress Testing

Stress test đặt portfolio vào những kịch bản xấu nhưng plausible. Ví dụ equities giảm 25%, long yields tăng 150 bps, KRW yếu 10%, oil tăng 40%. Sau đó bạn xem portfolio chịu tác động thế nào.

Stress test tốt hơn việc chỉ hỏi “maximum historical loss là bao nhiêu”, vì tương lai không bắt buộc lặp lại đúng lịch sử. Nó buộc investor suy nghĩ theo transmission channels.

## 14. Scenario Matrix

Một framework hữu ích là phân economy thành bốn quadrant theo growth và inflation: growth lên/inflation xuống; growth lên/inflation lên; growth xuống/inflation xuống; growth xuống/inflation lên. Mỗi quadrant tạo pressure khác nhau lên equities, bonds, commodities và currencies.

Không nên biến matrix thành công thức cố định. Ví dụ bonds thường tốt khi growth và inflation cùng giảm, nhưng nếu sovereign-risk premium tăng mạnh, bond vẫn có thể giảm. Matrix chỉ là starting hypothesis.

## 15. Decision Rules thay vì prediction

Portfolio tốt không đòi hỏi dự báo chính xác mọi biến. Quan trọng hơn là có rules cho những tình huống khác nhau.

Ví dụ, nếu asset allocation lệch target quá một threshold, rebalance. Nếu single stock vượt concentration limit vì tăng giá mạnh, review và trim theo IPS. Nếu thesis thay đổi do balance sheet deterioration, không dùng giá mua làm anchor. Nếu volatility tăng nhưng fundamentals không đổi, không tự động bán chỉ vì cảm xúc.

Decision rules chuyển process từ “đoán đúng tương lai” sang “phản ứng có kỷ luật trước thông tin mới”.

## 16. Portfolio Review thực tế

Một review tốt nên trả lời bốn câu hỏi. Portfolio kiếm/lỗ từ exposure nào? Risk hiện tập trung ở đâu? Assumption nào đã thay đổi? Allocation có còn phù hợp với liabilities và horizon không?

Nếu không trả lời được bốn câu này, việc biết Sharpe hay beta chỉ là trang trí thống kê. Portfolio analytics có giá trị khi nó giúp thay đổi quyết định, không phải khi tạo thêm dashboard đẹp.