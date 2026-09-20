# Nghiên cứu độ bền chiến lược và danh mục nhiều chiến lược

> Một chiến lược đẹp trong backtest chưa đủ. Câu hỏi quan trọng hơn là: **lợi thế có thật không, có sống được ngoài mẫu không, có còn tồn tại sau chi phí không và nhiều chiến lược trong cùng portfolio có thật sự đa dạng hay chỉ lặp cùng một factor?**

# Phần I — Từ ý tưởng tới chiến lược có thể kiểm chứng

## 1. Ý tưởng chưa phải chiến lược

Một nhận định như “giá thường hồi sau oversold” chỉ là ý tưởng.

Chiến lược phải chỉ rõ:

```text
Universe
Signal
Entry
Exit
Sizing
Cost
Risk Limit
Invalidation
```

## 2. Bắt đầu bằng hypothesis

Giả thuyết nên có lý do edge tồn tại, ví dụ:

- risk premium;
- behavioral bias;
- liquidity need;
- institutional constraint;
- delayed information;
- market structure.

Việc có một cơ chế hợp lý giúp giảm nguy cơ tìm pattern ngẫu nhiên sau khi nhìn dữ liệu.

## 3. Falsification

Một research process tốt phải cố bác bỏ hypothesis.

Ví dụ:

```text
Nếu edge biến mất khi tăng cost hợp lý,
hoặc không tồn tại ngoài mẫu,
thì hypothesis chưa đủ mạnh.
```

# Phần II — In-sample và out-of-sample

## 4. In-sample

In-sample là dữ liệu dùng để xây hoặc điều chỉnh strategy.

Performance tốt ở đây dễ bị overfit nhất.

## 5. Out-of-sample

Out-of-sample là dữ liệu chưa dùng để thiết kế rule.

Nếu edge giữ được ở OOS, bằng chứng mạnh hơn nhưng vẫn chưa đủ để đảm bảo tương lai.

## 6. Walk-forward

Walk-forward mô phỏng quá trình cập nhật strategy theo thời gian:

```text
Train quá khứ
→ Test đoạn sau
→ Trượt cửa sổ
→ Lặp lại
```

Nó giúp kiểm tra strategy khi market regime thay đổi.

# Phần III — Các bias làm kết quả đẹp giả tạo

## 7. Look-ahead bias

Dùng dữ liệu chưa tồn tại ở thời điểm quyết định.

## 8. Survivorship bias

Chỉ dùng asset còn tồn tại hôm nay và bỏ các asset đã delist/fail.

## 9. Data snooping

Thử rất nhiều rule rồi chỉ giữ rule đẹp nhất.

## 10. Multiple testing

Nếu thử hàng nghìn strategy, một số sẽ có Sharpe cao chỉ do may mắn.

Phải tính tới số lượng thử nghiệm và mức độ tương quan giữa chúng.

# Phần IV — Parameter stability

## 11. Đừng tìm một điểm tối ưu duy nhất

Nếu strategy chỉ lời ở parameter 47 nhưng lỗ ở 46 và 48, edge có thể là noise.

## 12. Parameter plateau

Vùng parameter rộng có kết quả tương đối ổn thường đáng tin hơn một đỉnh hẹp.

## 13. Structural parameter

Parameter nên có ý nghĩa kinh tế hoặc market-structure nếu có thể, thay vì chỉ được tối ưu để đẹp nhất.

# Phần V — Chi phí và capacity

## 14. Edge trước chi phí và sau chi phí

Strategy chỉ có giá trị nếu:

```text
Gross Edge
- Spread
- Commission
- Slippage
- Impact
- Financing
- Borrow / Roll Cost
> 0
```

## 15. Market impact

Khi capital tăng, chính order của strategy có thể làm giá di chuyển.

Backtest không tính impact thường scale quá lạc quan.

## 16. Capacity

Capacity là lượng vốn có thể triển khai trước khi execution cost làm edge biến mất.

Nó phụ thuộc:

- liquidity;
- turnover;
- holding period;
- participation rate;
- market depth.

# Phần VI — Regime dependence

## 17. Edge có thể phụ thuộc regime

Một strategy trend-following có thể rất tốt khi trend mạnh nhưng tệ trong choppy range.

Một carry strategy có thể tốt khi volatility thấp nhưng chịu tail loss khi funding stress.

## 18. Regime không phải lý do để giải thích mọi loss sau sự kiện

Regime definition phải được đặt trước hoặc có rule quan sát rõ ràng.

Nếu trader chỉ nói “regime changed” sau khi strategy thua, đó có thể là hindsight explanation.

## 19. Stress regimes

Nên test ít nhất:

- high volatility;
- low volatility;
- liquidity crisis;
- trend;
- range;
- policy shock;
- gap events.

# Phần VII — Distribution và tail risk

## 20. Average không đủ

Cần xem:

- skew;
- kurtosis;
- tail loss;
- drawdown;
- loss clustering.

## 21. Short-vol profile

Strategy có nhiều win nhỏ và vài loss rất lớn có thể có negative skew.

Win rate 90% không bảo đảm an toàn.

## 22. Convexity

Long convexity thường mất chi phí nhỏ thường xuyên để nhận payoff lớn trong tail.

Short convexity thường ngược lại.

Portfolio nên biết mình đang nghiêng về hướng nào.

# Phần VIII — Expectancy và uncertainty

## 23. Expectancy

```text
Expectancy
= P(win) × AvgWin
- P(loss) × AvgLoss
```

Estimate này có uncertainty.

## 24. Confidence interval

Một mean return dương nhưng confidence interval rất rộng có thể chưa đủ bằng chứng edge thật.

Sample size và dependence quyết định độ tin cậy.

## 25. Effective sample size

500 trade trong cùng một macro regime không tương đương 500 quan sát hoàn toàn độc lập.

Correlation giữa trade làm effective sample nhỏ hơn.

# Phần IX — Bootstrap và Monte Carlo

## 26. Bootstrap

Bootstrap resample historical observations để tạo nhiều possible paths.

Nó giúp thấy phân phối drawdown và return thay vì một equity curve duy nhất.

## 27. Monte Carlo

Monte Carlo có thể mô phỏng:

- thứ tự trade;
- distribution của win/loss;
- volatility;
- regime transition;
- parameter uncertainty.

## 28. Không biến simulation thành “độ chính xác giả”

Kết quả phụ thuộc assumption đầu vào. Nếu distribution giả định sai, simulation phức tạp vẫn sai.

# Phần X — Risk of ruin và sizing

## 29. Risk of ruin

Nguy cơ phá sản tăng khi:

- risk/trade lớn;
- leverage cao;
- edge nhỏ;
- losses tương quan;
- tail risk lớn.

## 30. Kelly criterion

Kelly giúp tối đa long-run log growth dưới assumption biết chính xác edge.

Trong thực tế edge estimate không chắc, nên thường dùng **fractional Kelly**.

## 31. Drawdown budget

Portfolio nên định trước mức drawdown nào dẫn tới:

- giảm size;
- dừng strategy;
- review model;
- kiểm tra operation.

Không nên quyết định trong lúc đang panic.

# Phần XI — Strategy degradation

## 32. Vì sao edge suy giảm?

Có thể do:

- nhiều người khai thác cùng anomaly;
- market structure thay đổi;
- cost tăng;
- regulation thay đổi;
- regime thay đổi;
- execution xuống cấp.

## 33. Phân biệt normal variance và degradation

Một chuỗi loss không tự động chứng minh edge mất.

Cần so với distribution expected trước đó.

## 34. Monitoring metrics

Theo dõi:

```text
Expectancy
Hit Rate
Payoff Ratio
Drawdown
Slippage
Turnover
Factor Exposure
Capacity
```

# Phần XII — Research log

## 35. Mỗi thay đổi phải có lý do

Ghi:

```text
Date
Version
Hypothesis
Rule Change
Why
Expected Effect
Validation Result
```

## 36. Không rewrite lịch sử

Nếu strategy được sửa sau loss, phải giữ version cũ để biết decision lúc đó dựa trên rule nào.

Điều này giúp chống hindsight bias.

# Phần XIII — Forward test và small live

## 37. Forward test

Forward test chạy trên dữ liệu mới theo thời gian thật giúp phát hiện:

- data delay;
- execution mismatch;
- bug;
- cost cao hơn giả định.

## 38. Small live

Dùng size nhỏ cho phép đo fill và operation thực tế trước khi scale.

## 39. Scale từng bước

Không nên nhảy từ backtest sang full capital.

Một lộ trình hợp lý:

```text
Backtest
→ OOS
→ Walk-Forward
→ Paper / Forward
→ Small Live
→ Gradual Scale
```

# Phần XIV — Portfolio of strategies

## 40. Nhiều strategy không tự động đa dạng

Một portfolio có:

- trend strategy;
- FX carry;
- short put;
- mean reversion;

nhưng có thể cùng phụ thuộc low volatility hoặc abundant liquidity.

## 41. Strategy correlation

Correlation nên được đo cả normal và stress periods.

Historical average thấp không bảo đảm correlation thấp khi crisis.

## 42. Factor decomposition

Map strategy về factor:

```text
Equity Beta
Rates
USD
Carry
Trend
Volatility
Liquidity
Commodity
Country
```

Hai strategy instrument khác nhau có thể là cùng một factor bet.

## 43. Equal capital vs equal risk

Chia capital bằng nhau không đồng nghĩa chia risk bằng nhau.

Một strategy volatility 5% và strategy volatility 30% không nên được xem như contribution ngang nhau chỉ vì capital weight giống nhau.

## 44. Volatility scaling

Có thể scale strategy để target risk gần nhau.

Nhưng phải bổ sung cap cho tail, leverage và liquidity.

## 45. Risk contribution

Mục tiêu là biết strategy nào đóng góp bao nhiêu vào portfolio volatility và stress loss.

## 46. Correlation breakdown

Trong funding crisis, nhiều strategy cùng deleverage có thể làm correlation tăng đột ngột.

Nên có stress matrix ngoài historical covariance.

# Phần XV — Convexity và tail trong portfolio

## 47. Short-vol concentration

Các strategy tưởng khác nhau như:

- selling options;
- carry;
- liquidity provision;
- some mean reversion;

có thể cùng chịu short-vol/tail exposure.

## 48. Tail hedge

Tail hedge có thể giảm loss cực đoan nhưng có carrying cost.

Phải đánh giá theo nhiều năm và toàn portfolio, không theo một tháng.

## 49. Hedge budget

Định trước ngân sách hedge giúp tránh mua protection quá đắt sau khi crisis đã bắt đầu.

# Phần XVI — Operational risk

## 50. Strategy đúng vẫn có thể mất tiền vì operation

Rủi ro gồm:

- stale data;
- duplicate order;
- wrong symbol;
- wrong multiplier;
- API disconnect;
- margin mismatch.

## 51. Kill switch

Mỗi strategy cần điều kiện dừng khi operational state không đáng tin.

## 52. Reconciliation

Actual positions phải được đối chiếu với broker/exchange state.

# Phần XVII — Post-trade attribution

## 53. Không chỉ hỏi “trade lời hay lỗ”

Phân rã:

```text
Signal Quality
Sizing
Execution
Cost
Market Regime
Factor Move
Discretionary Override
```

## 54. Decision quality và outcome

Một decision đúng process vẫn có thể lỗ do uncertainty.

Một decision tệ vẫn có thể lời do luck.

Review phải tách hai thứ.

# Phần XVIII — Monthly review

## 55. Review theo strategy

```text
Return
Drawdown
Expectancy
Hit Rate
Average Win/Loss
Slippage
Cost
Capacity
Factor Exposure
```

## 56. Review portfolio

```text
Gross / Net
Risk Contribution
Correlation
Tail Exposure
Liquidity
Margin
Stress Loss
```

## 57. Rule change discipline

Không thay rule chỉ vì tháng vừa rồi xấu.

Mọi thay đổi phải có hypothesis, test và version riêng.

# Phần XIX — Khi nào dừng strategy?

## 58. Evidence edge mất

Có thể cân nhắc dừng khi:

- OOS/live performance lệch lớn khỏi distribution;
- cost vượt edge;
- structural market change;
- capacity quá nhỏ;
- operational risk quá cao.

## 59. Sunk cost

Thời gian đã bỏ vào research không phải lý do giữ strategy không còn hiệu quả.

# Phần XX — Quy trình nghiên cứu chuẩn

## 60. Pipeline

```text
Hypothesis
→ Formal Rules
→ Data Audit
→ In-Sample
→ Robustness
→ Out-of-Sample
→ Walk-Forward
→ Cost / Capacity
→ Bootstrap / Monte Carlo
→ Forward Test
→ Small Live
→ Portfolio Integration
→ Monitoring
```

## 61. Checklist cuối

```text
Edge có cơ chế hợp lý không?
Có survives OOS không?
Parameter có stable không?
Cost realistic không?
Tail risk là gì?
Capacity bao nhiêu?
Correlation với strategy khác?
Operation fail thì sao?
Khi nào invalidate?
```

## Kết luận

Một strategy tốt không chỉ có backtest đẹp. Nó phải chứng minh được rằng:

```text
Edge có thể tồn tại
+ không phụ thuộc một parameter duy nhất
+ sống qua out-of-sample
+ còn dương sau cost
+ chịu được drawdown
+ không trùng risk với toàn portfolio
+ vận hành an toàn
```

Mục tiêu của research không phải chứng minh ý tưởng của mình đúng, mà **tìm đủ cách làm nó sai trước khi đưa vốn thật vào**.
