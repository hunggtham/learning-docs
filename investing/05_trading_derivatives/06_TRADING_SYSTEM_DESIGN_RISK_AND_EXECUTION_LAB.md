# Phòng thí nghiệm nâng cao: thiết kế hệ thống giao dịch, rủi ro và thực thi

> File này nối phần phái sinh, backtest, độ bền chiến lược và vi cấu trúc thị trường thành một quy trình vận hành hoàn chỉnh. Mục tiêu là biến một ý tưởng thành **một hệ thống có quy tắc, có mô hình chi phí, có ngân sách rủi ro, có kiểm soát vận hành và có tiêu chí dừng**.

## 1. Tách ý tưởng, tín hiệu và chiến lược

Một quan sát như “giá thường hồi sau khi quét thanh khoản” chưa phải chiến lược.

Cần tách:

```text
Ý tưởng kinh tế / hành vi
→ tín hiệu quan sát được
→ quy tắc vào lệnh
→ quy tắc thoát
→ quy mô vị thế
→ chi phí
→ điều kiện vô hiệu hóa
```

Nếu hai người đọc cùng mô tả mà viết ra hai hệ thống rất khác nhau, đặc tả vẫn chưa đủ chặt.

## 2. Viết giả thuyết trước khi nhìn kết quả

Giả thuyết tốt nên nói rõ **vì sao** lợi thế có thể tồn tại.

Nguồn có thể là:

```text
Phần bù rủi ro
Thiên lệch hành vi
Ràng buộc tổ chức
Nhu cầu thanh khoản
Chậm phản ánh thông tin
Cấu trúc vi mô
```

Viết trước giúp giảm nguy cơ nhìn dữ liệu rồi kể câu chuyện hợp lý hóa sau.

## 3. Xác định đơn vị rủi ro trước đơn vị lợi nhuận

Trước khi hỏi hệ thống lời bao nhiêu, phải định nghĩa 1R là gì.

Ví dụ:

```text
1R = mức lỗ nếu stop hợp lệ bị chạm
```

Sau đó mọi giao dịch được chuẩn hóa theo R-multiple. Điều này cho phép so sánh nhiều thị trường và nhiều khoảng biến động khác nhau.

## 4. Expectancy phải tách win rate và payoff

```text
Expectancy
= P(win) × AvgWin
- P(loss) × AvgLoss
```

Một chiến lược thắng 70% vẫn có thể âm nếu khoản lỗ lớn. Một chiến lược thắng 35% vẫn có thể tốt nếu payoff cao.

Không tối ưu win rate tách khỏi phân phối P/L.

## 5. Backtest phải bắt đầu bằng audit thời gian

Với mọi biến dữ liệu, ghi:

```text
Observation time
Publication time
Revision time
Decision time
Execution time
```

Sai vài phút trong chiến lược quanh CPI/FOMC có thể biến kết quả thật thành một backtest giả tạo.

## 6. Dữ liệu point-in-time

Không được dùng dữ liệu đã sửa sau này để ra quyết định quá khứ.

Ví dụ EPS consensus hôm nay không thể dùng cho backtest ngày hai năm trước nếu consensus lịch sử đã thay đổi.

Đây là lý do dữ liệu “đẹp” nhưng không point-in-time rất nguy hiểm.

## 7. Phân tách tập dữ liệu đúng vai trò

Một cấu trúc:

```text
Train
→ xây quy tắc

Validation
→ chọn phiên bản

Test
→ đánh giá cuối cùng ngoài mẫu
```

Nếu nhìn test set rồi sửa chiến lược nhiều lần, test set đã trở thành train set.

## 8. Walk-forward mô phỏng tốt hơn thực tế cập nhật

Quy trình:

```text
Huấn luyện trên quá khứ
→ kiểm tra đoạn tiếp theo
→ trượt cửa sổ
→ lặp
```

Nó không loại overfit nhưng buộc hệ thống chứng minh khả năng thích nghi qua nhiều giai đoạn.

## 9. Purging và embargo khi dữ liệu chồng lấn

Nếu nhãn hoặc giao dịch kéo dài qua ranh giới train/test, thông tin có thể rò rỉ.

- **Purging:** loại quan sát chồng lấn;
- **Embargo:** tạo khoảng trống thời gian giữa hai tập.

Điều này đặc biệt quan trọng với machine learning và chiến lược có thời gian giữ vị thế dài.

## 10. Parameter surface quan trọng hơn điểm tối ưu

Nếu tham số 47 rất tốt nhưng 46 và 48 đều tệ, kết quả có thể là nhiễu.

Nên tìm **vùng ổn định** thay vì đỉnh tối ưu hẹp.

Một plateau rộng thường đáng tin hơn một magic number.

## 11. Placebo test để cố phá chiến lược

Có thể thử:

```text
Dịch tín hiệu vài kỳ
Đảo tín hiệu
Ngẫu nhiên hóa entry
Giữ exit nhưng thay entry
Giữ entry nhưng thay exit
```

Nếu chiến lược vẫn “tốt” khi tín hiệu chính bị phá, có thể lợi nhuận thật đến từ drift thị trường hoặc một yếu tố khác.

## 12. Chi phí phải phụ thuộc trạng thái

Spread và slippage không cố định.

Trong bình thường:

```text
spread nhỏ
+ depth cao
```

Trong sự kiện:

```text
spread rộng
+ depth giảm
+ gap
+ impact tăng
```

Cost model dùng một con số cố định thường đánh giá quá cao chiến lược event-driven hoặc turnover cao.

## 13. Capacity là giới hạn kinh tế

Một chiến lược lời với 10.000 USD chưa chắc scale tới 10 triệu USD.

Theo dõi:

```text
ADV
Participation rate
Turnover
Spread
Market impact
Time-to-exit
```

Khi vốn tăng, chính lệnh của chiến lược có thể ăn hết lợi thế.

## 14. Position sizing phải xuất phát từ khoảng lỗ

Một quy tắc đơn giản:

```text
Position Size
≈ Risk Budget / Distance to Invalidation
```

Nhưng với gap risk hoặc option short, stop không giới hạn được lỗ tối đa. Khi đó cần dùng stress loss thay vì khoảng stop.

## 15. Volatility scaling có lợi và có rủi ro

Giảm vị thế khi biến động tăng giúp giữ rủi ro gần ổn định.

Nhưng volatility thường tăng **sau khi giá đã giảm**. Nếu giảm size máy móc, hệ thống có thể bán thấp và mua lại cao.

Vì vậy cần giới hạn tốc độ điều chỉnh và hiểu mục tiêu của volatility targeting.

## 16. Kelly chỉ là giới hạn lý thuyết

Kelly criterion tối đa hóa tăng trưởng log dài hạn khi biết chính xác xác suất và payoff.

Trong thực tế edge không chắc chắn, nên full Kelly thường quá hung hăng. Fractional Kelly an toàn hơn vì phản ánh sai số ước lượng.

## 17. Risk of ruin quan trọng hơn lợi suất trung bình

Một hệ thống expectancy dương vẫn có thể phá sản nếu:

```text
Leverage cao
Risk/trade lớn
Losses tương quan
Tail risk lớn
```

Mục tiêu đầu tiên là sống đủ lâu để edge có cơ hội xuất hiện.

## 18. Portfolio heat

Nhiều vị thế riêng lẻ 1R không đồng nghĩa tổng rủi ro bằng tổng đơn giản.

Nếu năm vị thế đều long USD hoặc long tech beta, một cú sốc có thể làm tất cả cùng lỗ.

Phải tổng hợp theo factor:

```text
Equity beta
Rates
USD
Carry
Volatility
Commodity
Liquidity
```

## 19. Correlation phải kiểm tra trong stress

Correlation trung bình thấp không đủ.

Một số chiến lược:

```text
carry
short volatility
mean reversion
liquidity provision
```

có thể cùng chịu lỗ khi funding stress dù lịch sử bình thường trông đa dạng.

## 20. Tail profile phải được nhìn riêng

Phân phối lợi nhuận có thể có:

```text
negative skew
fat tails
clustered losses
```

Sharpe cao không nói hết.

Đặc biệt chiến lược bán quyền chọn thường có nhiều lời nhỏ và ít lỗ rất lớn.

## 21. Monte Carlo không tạo sự thật mới

Monte Carlo hữu ích để tạo nhiều đường P/L nhưng kết quả phụ thuộc giả định đầu vào.

Có thể mô phỏng:

```text
Thứ tự giao dịch
Độ lớn win/loss
Regime transition
Slippage stress
Parameter uncertainty
```

Nhưng nếu distribution đầu vào sai, mô phỏng đẹp vẫn sai.

## 22. Backtest và thực thi phải dùng cùng logic vị thế

Một lỗi phổ biến:

```text
Backtest giả định fill toàn bộ tại close
Live dùng limit order và partial fill
```

Khi đó hệ thống thật khác hệ thống được nghiên cứu.

Cần mô hình hóa order type, thời gian chờ và partial fill từ đầu nếu chúng ảnh hưởng lớn.

## 23. Decision price và execution price

Ghi hai mức:

```text
Giá khi chiến lược quyết định
Giá thực tế được khớp
```

Khoảng chênh là nền tảng của **thiếu hụt thực thi (implementation shortfall)**.

## 24. TCA phải phân rã nguyên nhân

Chi phí giao dịch nên tách:

```text
Spread
Delay
Market impact
Opportunity cost
Commission
```

Nếu slippage tăng, cần biết do thị trường xấu hơn hay thuật toán thực thi tệ hơn.

## 25. Maker không tự động tốt hơn taker

Lệnh chờ tiết kiệm spread nhưng chịu adverse selection và non-fill risk.

Lệnh chủ động trả spread nhưng giảm rủi ro bỏ lỡ.

Lựa chọn phụ thuộc decay của tín hiệu và thanh khoản.

## 26. Signal decay quyết định mức khẩn cấp

Nếu edge biến mất trong 30 giây, thực thi chậm để tiết kiệm 1 bp có thể vô nghĩa.

Nếu edge tồn tại nhiều ngày, có thể ưu tiên giảm impact.

Do đó execution phải gắn với **half-life của alpha**.

## 27. Derivatives phải quản trị notional và margin riêng

Margin không phải mức rủi ro kinh tế.

Một futures position có margin 5.000 USD nhưng notional 100.000 USD vẫn mang exposure 100.000 USD.

Theo dõi đồng thời:

```text
Notional
Delta / DV01
Margin
Liquidity buffer
```

## 28. Options cần scenario grid

Delta-neutral không có nghĩa risk-free.

Stress ít nhất:

```text
Spot ±5%, ±10%
IV ±5, ±10 vol
Thời gian trôi
Skew thay đổi
```

Gamma/Vega có thể làm P/L khác xa dự đoán tuyến tính.

## 29. Margin stress có thể giết vị thế đúng

Một thesis dài hạn đúng vẫn thất bại nếu tài khoản không chịu được variation margin trong ngắn hạn.

Cần hỏi:

```text
Nếu volatility gấp đôi?
Nếu margin requirement tăng 50%?
Nếu gap qua stop?
```

## 30. Forward test là giai đoạn kiểm tra hệ thống

Paper/forward test giúp phát hiện:

```text
Data delay
Mismatch timezone
Order reject
Partial fill
Broker API issue
Slippage thực
```

Đây là bước kiểm tra kỹ thuật, không chỉ kiểm tra edge.

## 31. Small live để đo ma sát thật

Sau forward test, dùng quy mô nhỏ để kiểm tra:

```text
fill quality
commission thực
borrow availability
roll
funding cost
```

Không nên nhảy từ backtest trực tiếp sang full size.

## 32. Production monitoring cần tách edge và vận hành

Theo dõi hai bảng:

**Chất lượng chiến lược:**

```text
Expectancy
Hit rate
Payoff ratio
Drawdown
Factor exposure
```

**Chất lượng thực thi:**

```text
Slippage
Reject rate
Latency
Fill rate
Position mismatch
```

Nếu P/L xấu, phải biết lớp nào đang hỏng.

## 33. Drift detection

Theo dõi phân phối của:

```text
Input features
Signal frequency
Holding time
Hit rate
Slippage
Market regime
```

Thay đổi nhỏ từng phần có thể cho thấy chiến lược đang rời khỏi môi trường được nghiên cứu.

## 34. Kill switch phải được thiết kế trước

Điều kiện dừng có thể gồm:

```text
Dữ liệu stale
Broker disconnect
Position mismatch
Daily loss vượt ngưỡng
Margin quá cao
Slippage bất thường
```

Không được chờ tới lúc có sự cố mới quyết định cách dừng.

## 35. Strategy retirement

Một chiến lược nên được dừng khi bằng chứng đủ mạnh rằng:

```text
Edge sau chi phí <= 0
Cấu trúc thị trường thay đổi
Capacity không còn đáng kể
Operational risk quá cao
Live performance lệch cấu trúc quá lớn
```

Không giữ chiến lược chỉ vì đã bỏ nhiều thời gian nghiên cứu.

## 36. Bài tập xây hệ thống từ đầu tới live

Chọn một ý tưởng và hoàn thành:

1. giả thuyết nhân quả;
2. rule chính xác;
3. data audit;
4. cost model;
5. train/validation/test;
6. walk-forward;
7. placebo tests;
8. Monte Carlo;
9. risk/trade và portfolio heat;
10. execution model;
11. forward test;
12. small live checklist;
13. kill switch;
14. retirement criteria.

Nếu thiếu một bước, hệ thống chưa sẵn sàng để tăng quy mô.

## 37. Liên kết đọc tiếp

- [Phái sinh: futures, options, swaps và CFD](./01_DERIVATIVES_FUTURES_OPTIONS_CFD.md)
- [Backtest và rủi ro hệ thống](./02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Thực thi và vi cấu trúc](./03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
- [Độ bền chiến lược](./04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
- [Options và bề mặt biến động](./05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md)

## Kết luận

Một chiến lược hoàn chỉnh không phải là tín hiệu vào lệnh. Nó là:

```text
Giả thuyết
→ dữ liệu
→ kiểm thử
→ rủi ro
→ thực thi
→ vận hành
→ giám sát
→ dừng khi edge biến mất
```

Chất lượng của hệ thống nằm ở **toàn bộ chuỗi**, không nằm ở một backtest đẹp.