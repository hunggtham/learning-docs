# Nghiên cứu hệ thống, backtest, rủi ro và triển khai thực tế

> Một ý tưởng trading chỉ trở thành chiến lược khi nó được chuyển thành rule rõ ràng, kiểm thử bằng dữ liệu đúng thời điểm, chịu được chi phí giao dịch và vẫn hoạt động ngoài mẫu. Chương này trình bày quy trình từ **giả thuyết → dữ liệu → backtest → validation → forward test → production monitoring**.

# Phần I — Bắt đầu từ giả thuyết

## 1. Idea không phải strategy

“Giá thường bật sau khi sweep liquidity” chỉ là một quan sát.

Muốn thành strategy cần xác định:

```text
Universe
Timeframe
Signal
Entry
Exit
Stop
Position Size
Cost Model
Invalidation
```

Nếu rule không đủ rõ để hai người code ra kết quả gần giống nhau, hệ thống còn quá mơ hồ.

## 2. Causal hypothesis

Một strategy tốt nên có lý do tại sao edge có thể tồn tại.

Nguồn edge có thể đến từ:

- risk premium;
- behavioral bias;
- institutional constraint;
- liquidity need;
- slow information diffusion;
- market structure.

Không phải mọi edge cần mô hình kinh tế hoàn hảo, nhưng một câu chuyện nhân quả giúp giảm data mining.

## 3. Falsifiable

Giả thuyết phải có khả năng bị bác bỏ.

Ví dụ:

```text
Nếu signal chỉ hoạt động trước cost,
hoặc mất hoàn toàn ở out-of-sample,
thì hypothesis cần xem lại.
```

# Phần II — Dữ liệu

## 4. Point-in-time data

Dữ liệu dùng trong backtest phải là dữ liệu **có thể biết tại thời điểm quyết định**.

Cần phân biệt:

```text
Observation Time
Publication Time
Revision Time
Decision Time
Execution Time
```

Dùng dữ liệu đã revise sau này cho quyết định quá khứ tạo look-ahead bias.

## 5. Timestamp audit

Mỗi nguồn cần biết:

- timezone;
- delay;
- bar close time;
- exchange timestamp;
- publication timestamp.

Sai timestamp vài phút có thể biến một strategy event-driven từ lỗ thành lời giả tạo.

## 6. Data quality

Cần kiểm tra:

- missing values;
- duplicate;
- bad ticks;
- corporate actions;
- futures roll;
- delisted securities;
- timezone changes.

Backtest tốt bắt đầu từ dữ liệu sạch, không từ indicator phức tạp.

# Phần III — Các bias phổ biến

## 7. Look-ahead bias

Dùng thông tin tương lai trong quá khứ.

Ví dụ dùng close của ngày để quyết định một entry được giả định xảy ra trước close.

## 8. Survivorship bias

Chỉ dùng những cổ phiếu còn tồn tại hôm nay làm universe lịch sử sẽ bỏ các công ty phá sản hoặc bị hủy niêm yết.

Kết quả thường đẹp giả tạo.

## 9. Selection bias

Chọn market hoặc period vì biết trước nó phù hợp strategy cũng tạo bias.

## 10. Data snooping

Thử quá nhiều biến, rule và timeframe rồi chỉ giữ cái tốt nhất làm tăng xác suất tìm được pattern ngẫu nhiên.

## 11. Multiple-testing problem

Nếu thử hàng nghìn strategy, một số sẽ có Sharpe cao chỉ do may mắn.

Do đó cần xem số lượng thử nghiệm và mức độ độc lập giữa các thử nghiệm.

# Phần IV — Chia dữ liệu

## 12. Train, validation và test

Một cấu trúc phổ biến:

```text
Train
→ xây / fit strategy

Validation
→ chọn phiên bản

Test
→ đánh giá cuối ngoài mẫu
```

Không nên liên tục nhìn test set rồi sửa strategy vì khi đó test set đã trở thành train set.

## 13. Out-of-sample

Out-of-sample (OOS) là phần dữ liệu không dùng để xây rule.

Hiệu quả OOS thường đáng tin hơn in-sample, dù vẫn có thể may mắn.

## 14. Walk-forward

Walk-forward lặp quy trình:

```text
Train quá khứ
→ Test đoạn tiếp theo
→ Trượt cửa sổ
→ Lặp lại
```

Nó mô phỏng tốt hơn cách strategy sẽ được cập nhật theo thời gian.

## 15. Purging và embargo

Khi labels hoặc trade overlap theo thời gian, train/test có thể rò rỉ thông tin qua các sample gần nhau.

**Purging** loại sample có overlap; **embargo** tạo khoảng cách giữa các tập.

Khái niệm này đặc biệt quan trọng trong machine-learning trading.

# Phần V — Expectancy và distribution

## 16. Expectancy

```text
E
= P(win) × AvgWin
- P(loss) × AvgLoss
```

Expectancy dương mới là nền tảng; win rate cao không đủ.

## 17. R-multiple

Chuẩn hóa kết quả theo risk ban đầu giúp so nhiều trade khác nhau.

## 18. Distribution quan trọng hơn average

Hai strategy cùng average return nhưng có thể khác:

- skew;
- fat tails;
- drawdown;
- loss clustering;
- liquidity exposure.

## 19. Drawdown

Maximum drawdown chỉ là một quan sát lịch sử, không phải worst-case tương lai.

Cần xem cả:

- duration của drawdown;
- recovery time;
- underwater curve.

# Phần VI — Parameter robustness

## 20. Đừng chỉ tìm một “magic parameter”

Nếu strategy chỉ lời ở MA = 47 nhưng lỗ ở 45, 46, 48, 49 thì edge có thể rất mong manh.

## 21. Parameter surface

Nên xem cả vùng tham số.

Một plateau rộng thường đáng tin hơn một đỉnh đơn lẻ.

## 22. Stability across markets

Nếu cùng logic hoạt động ở nhiều market liên quan, bằng chứng tốt hơn strategy chỉ hoạt động ở một ticker rất cụ thể.

Nhưng không nên yêu cầu universal edge nếu hypothesis vốn chỉ phù hợp một market structure.

## 23. Stability across regimes

Kiểm tra:

- trend;
- range;
- high vol;
- low vol;
- crisis;
- easing/tightening.

Strategy có thể hợp lệ nhưng chỉ trong một regime; điều quan trọng là biết điều đó.

# Phần VII — Placebo và falsification tests

## 24. Placebo test

Thay signal thật bằng signal ngẫu nhiên hoặc dịch thời gian để xem performance có còn tương tự không.

Nếu có, “edge” có thể chỉ đến từ market drift hoặc bias.

## 25. Randomized entry

Giữ exit/risk rule nhưng randomize entry giúp kiểm tra entry signal thật sự đóng góp bao nhiêu.

## 26. Reverse signal

Đảo signal đôi khi giúp hiểu edge đến từ direction thật hay chỉ từ risk-management overlay.

# Phần VIII — Cost model

## 27. Spread

Spread là cost trực tiếp giữa bid và ask.

Backtest dùng mid/close mà bỏ spread thường quá lạc quan.

## 28. Slippage

Slippage phụ thuộc:

- volatility;
- order type;
- size;
- liquidity;
- latency;
- event risk.

Không nên dùng một số slippage cố định cho mọi trạng thái nếu strategy lớn hoặc event-driven.

## 29. Market impact

Order lớn có thể tự đẩy giá đi ngược trader.

Capacity của strategy giảm khi size tăng.

## 30. Financing

CFD, margin, short borrow hoặc leveraged products có financing cost.

Strategy giữ lâu phải tính đầy đủ.

## 31. Borrow cost và short availability

Short strategy phải tính:

- borrow fee;
- locate availability;
- recall risk;
- hard-to-borrow behavior.

## 32. Futures roll

Futures strategy cần model:

- roll date;
- spread;
- liquidity migration;
- basis;
- commission.

# Phần IX — Monte Carlo và bootstrap

## 33. Bootstrap

Bootstrap lấy lại sample từ historical trades/returns để tạo nhiều đường P/L khả dĩ.

Nó giúp nhìn uncertainty của drawdown và return.

## 34. Monte Carlo

Monte Carlo có thể randomize:

- thứ tự trade;
- win/loss magnitude;
- volatility regime;
- parameter uncertainty.

Kết quả là distribution, không phải một equity curve duy nhất.

## 35. Sample size

100 trade không luôn tương đương 100 quan sát độc lập.

Nếu tất cả trade xảy ra trong cùng một regime, effective sample size nhỏ hơn nhiều.

## 36. Serial correlation

Returns có thể phụ thuộc theo chuỗi. Khi đó standard error đơn giản dựa independence có thể quá lạc quan.

# Phần X — Metrics

## 37. Sharpe

```text
Sharpe
= Excess Return / Volatility
```

Hữu ích nhưng không mô tả tail risk hoặc liquidity.

## 38. Sortino

Sortino dùng downside deviation thay total volatility.

## 39. Calmar

```text
Calmar
≈ CAGR / Maximum Drawdown
```

Hữu ích với trend-following và strategy có path dài.

## 40. Profit factor

```text
Profit Factor
= Gross Profit / Gross Loss
```

Cần đọc cùng trade count và cost.

## 41. Hit rate

Hit rate là win rate. Không nên dùng riêng lẻ.

# Phần XI — Position sizing

## 42. Fixed risk

Một cách đơn giản là risk một tỷ lệ capital cố định theo invalidation.

## 43. Volatility scaling

Giảm size khi volatility tăng giúp giữ risk gần ổn định hơn.

## 44. Kelly

Kelly tối đa hóa long-run logarithmic growth dưới giả định biết chính xác edge.

Trong thực tế thường dùng fractional Kelly vì estimate rất không chắc chắn.

## 45. Portfolio heat

Tổng risk của nhiều position có thể lớn hơn tổng risk riêng lẻ nếu chúng tương quan.

# Phần XII — Capacity

## 46. Strategy capacity

Capacity là quy mô vốn có thể chạy trước khi impact và liquidity làm edge giảm đáng kể.

Một strategy micro-cap có Sharpe cao với 10.000 USD có thể không scale lên 10 triệu USD.

## 47. Turnover

Turnover cao làm strategy nhạy với transaction cost và execution quality.

# Phần XIII — Forward test

## 48. Paper/forward test

Forward test kiểm tra strategy trên dữ liệu mới theo thời gian thật.

Nó giúp phát hiện:

- data mismatch;
- latency;
- execution assumption sai;
- operational bug.

## 49. Small live

Sau forward test, chạy size rất nhỏ có thể cung cấp dữ liệu thực tế về fill và slippage trước khi scale.

# Phần XIV — Production system

## 50. Research code và production code khác nhau

Notebook backtest có thể chấp nhận thao tác thủ công. Production cần:

- deterministic logic;
- logging;
- retries;
- monitoring;
- failure handling.

## 51. Reconciliation

Hệ thống phải đối chiếu:

```text
Expected Position
vs
Broker Position
```

Nếu khác nhau, cần dừng hoặc xử lý rõ ràng.

## 52. Idempotent order

Một order command chạy lại không nên vô tình tạo position gấp đôi.

Đây là yêu cầu phần mềm quan trọng trong automation.

## 53. Kill switch

Kill switch cho phép dừng hệ thống khi:

- data lỗi;
- broker API lỗi;
- position mismatch;
- loss vượt threshold;
- market bất thường.

## 54. Circuit breaker nội bộ

Có thể thiết kế giới hạn:

- daily loss;
- max gross exposure;
- max leverage;
- max order size;
- max slippage.

# Phần XV — Drift và degradation

## 55. Strategy degradation

Edge có thể giảm vì:

- market adapts;
- competition;
- cost tăng;
- regime thay;
- implementation drift.

## 56. Feature drift

Distribution của input có thể thay đổi so training period.

## 57. Performance drift

Theo dõi:

- hit rate;
- expectancy;
- slippage;
- turnover;
- factor exposure;
- drawdown.

## 58. Không dừng strategy chỉ vì vài loss

Cần phân biệt normal variance với evidence edge đã hỏng.

Dùng threshold được định nghĩa trước thay vì phản ứng cảm xúc.

# Phần XVI — Research log

## 59. Versioning

Mỗi thay đổi strategy nên ghi:

```text
Version
Date
Hypothesis
Rule Change
Reason
Expected Effect
Validation Result
```

## 60. Không sửa lịch sử

Không nên thay code rồi chạy lại và quên strategy cũ từng là gì.

Versioning giúp tránh hindsight bias.

# Phần XVII — Quy trình hoàn chỉnh

## 61. Research pipeline

```text
1. Causal Hypothesis
2. Data Audit
3. Formal Rules
4. In-Sample Test
5. Robustness / Parameter Surface
6. Out-of-Sample
7. Walk-Forward
8. Cost / Impact Model
9. Bootstrap / Monte Carlo
10. Forward Test
11. Small Live
12. Production Monitoring
```

## 62. Câu hỏi trước khi scale

```text
Edge có lý do tồn tại không?
OOS còn dương không?
Cost model thực tế không?
Sample đủ không?
Drawdown có chịu được không?
Capacity bao nhiêu?
Operational failure có thể gây gì?
```

## Kết luận

Backtest không phải bằng chứng strategy chắc chắn kiếm tiền. Nó là một **thí nghiệm lịch sử có rất nhiều cách sai**.

Một process tốt phải cố phá strategy trước khi bỏ vốn thật:

```text
Tìm bias
→ tăng cost
→ đổi regime
→ đổi parameter
→ test OOS
→ stress execution
```

Nếu edge vẫn tồn tại sau các bước đó, bằng chứng mới mạnh hơn.
