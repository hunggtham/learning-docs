# 11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ticket view dễ che giấu exposure** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Currency decomposition** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối FX portfolio risk với correlation và factor exposure, để phân biệt rủi ro đồng tiền, rủi ro nhân tố và rủi ro tập trung.

Một danh sách nhiều trade không tự động là một danh mục đa dạng hóa. Trong Forex, cùng một currency hoặc cùng một macro factor có thể xuất hiện lặp lại dưới nhiều ticker khác nhau. Vì vậy rủi ro (risk / 위험) phải được tổng hợp ở cấp **currency, factor, chiến lược (strategy / 전략) và liquidity**, không chỉ theo từng ticket.

Mô hình tư duy (mental model / 사고 모델):

```text
Positions
→ currency decomposition
→ factor exposure
→ covariance / stress dependence
→ portfolio loss distribution
→ risk budget and constraints
```

## 1. Ticket view dễ che giấu exposure

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

Ba trade khác nhau nhưng đều có thành phần:

```text
short USD
```

Nếu USD tăng mạnh, cả ba có thể lỗ cùng lúc.

Đếm `3 trades` không nói được diversification.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **2. Currency decomposition** nối từ **1. Ticket view dễ che giấu exposure** sang **3. Notional aggregation chưa đủ**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Currency decomposition

Mỗi pair có thể biểu diễn bằng véc-tơ (vector / 벡터) exposure.

Ví dụ long EUR/USD:

```text
+EUR
-USD
```

Long USD/JPY:

```text
+USD
-JPY
```

Portfolio nên aggregate net exposure theo từng currency sau khi quy đổi về dùng chung (common / 공통) rủi ro (risk / 위험) units.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **3. Notional aggregation chưa đủ** nối từ **2. Currency decomposition** sang **4. Gross và net exposure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Notional aggregation chưa đủ

Hai positions có cùng notional nhưng volatility khác nhau.

Ví dụ:

```text
100k EUR/USD
100k USD/TRY
```

không thể coi là same rủi ro (risk / 위험).

Risk-normalized exposure cần volatility, liquidity và tail hành vi (behavior / 동작).

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **4. Gross và net exposure** nối từ **3. Notional aggregation chưa đủ** sang **5. Correlation là time-varying**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Gross và net exposure

```text
Gross Exposure = Σ |notional_i|
Net Exposure = directional aggregate after offsets
```

Net nhỏ không có nghĩa gross rủi ro (risk / 위험) nhỏ.

Một long EUR/USD và short EUR/JPY có thể net EUR một phần nhưng tạo USD/JPY cross exposure và thực thi (execution / 실행) rủi ro (risk / 위험) ở hai legs.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **5. Correlation là time-varying** nối từ **4. Gross và net exposure** sang **6. Covariance ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Correlation là time-varying

Correlation ước lượng từ historical returns không phải constant.

Trong stress:

```text
correlations can converge
liquidity can deteriorate together
```

Do đó full-sample correlation thường đánh giá thấp crisis dependence.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **6. Covariance ma trận (matrix / 행렬)** nối từ **5. Correlation là time-varying** sang **7. Estimation lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Covariance ma trận (matrix / 행렬)

Với return véc-tơ (vector / 벡터) `r` và weights `w`:

```text
Portfolio Variance = w' Σ w
```

`Σ` là covariance ma trận (matrix / 행렬).

Công thức hữu ích nhưng kết quả phụ thuộc estimate cửa sổ (window / 윈도우), dữ liệu (data / 데이터) frequency và regime.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **7. Estimation lỗi (error / 오류)** nối từ **6. Covariance ma trận (matrix / 행렬)** sang **8. Factor mô hình (model / 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Estimation lỗi (error / 오류)

Covariance ma trận (matrix / 행렬) từ mẫu (sample / 표본) ngắn có thể unstable, đặc biệt với nhiều instruments.

Một optimizer có thể tạo extreme weights từ small estimation errors.

Practical controls:

- shrinkage;
- weight caps;
- simpler factor mô hình (model / 모델);
- stress scenarios.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **8. Factor mô hình (model / 모델)** nối từ **7. Estimation lỗi (error / 오류)** sang **9. Dollar factor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Factor mô hình (model / 모델)

FX returns có thể liên quan đến factors như:

- broad USD;
- carry;
- toàn cục (global / 전역) rủi ro (risk / 위험) sentiment;
- commodity exposure;
- tỷ lệ (rate / 비율) differential;
- regional Asia rủi ro (risk / 위험);
- volatility/liquidity.

Thay vì chỉ pair correlation, có thể estimate sensitivity tới factors.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **9. Dollar factor** nối từ **8. Factor mô hình (model / 모델)** sang **10. Carry factor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Dollar factor

Nhiều portfolios vô tình trở thành USD bet.

Nếu long EUR/USD, GBP/USD, AUD/USD và short USD/CHF, portfolio có broad anti-USD exposure.

Hiệu năng (performance / 성능) attribution phải tách broad USD move khỏi skill của từng tín hiệu (signal / 신호).

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **10. Carry factor** nối từ **9. Dollar factor** sang **11. Commodity factor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Carry factor

High-yield currencies có thể cùng chịu carry unwind trong risk-off.

Correlation bình thường thấp nhưng tail losses có thể cluster.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **11. Commodity factor** nối từ **10. Carry factor** sang **12. Tỷ lệ (rate / 비율) factor**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Commodity factor

Currencies của commodity exporters có thể đồng biến với commodity/China/global-growth factors.

Nhưng relationship không cố định và khác theo economy cấu trúc (structure / 구조).

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **12. Tỷ lệ (rate / 비율) factor** nối từ **11. Commodity factor** sang **13. Chiến lược (strategy / 전략) correlation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Tỷ lệ (rate / 비율) factor

Positions nhạy với front-end yield differential có thể cùng react khi toàn cục (global / 전역) central-bank expectations shift.

Một portfolio nhiều pairs không diversified nếu tất cả đều là cùng một “rates divergence” trade.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **13. Chiến lược (strategy / 전략) correlation** nối từ **12. Tỷ lệ (rate / 비율) factor** sang **14. Correlation of losses quan trọng hơn average correlation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Chiến lược (strategy / 전략) correlation

Cần nhìn cả correlation giữa **strategies**:

- carry;
- trend;
- mean reversion;
- sự kiện (event / 이벤트);
- giá trị (value / 값).

Hai strategies trên khác pairs vẫn có thể cùng factor exposure.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **14. Correlation of losses quan trọng hơn average correlation** nối từ **13. Chiến lược (strategy / 전략) correlation** sang **15. Portfolio heat**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Correlation of losses quan trọng hơn average correlation

Có thể estimate:

- downside correlation;
- tail dependence;
- conditional correlation during high-vol periods.

Rủi ro (risk / 위험) management quan tâm nhất lúc nhiều positions cùng lỗ.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **15. Portfolio heat** nối từ **14. Correlation of losses quan trọng hơn average correlation** sang **16. Scenario stress**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Portfolio heat

Một practical chỉ số (metric / 지표):

```text
Portfolio Heat
≈ sum of planned losses to stops
```

Nhưng nếu stops correlated/slippage correlated, actual tail mất mát (loss / 손실) có thể lớn hơn sum planned mất mát (loss / 손실).

Do đó portfolio heat chỉ là first tầng (layer / 계층).

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **16. Scenario stress** nối từ **15. Portfolio heat** sang **17. Historical stress**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Scenario stress

Stress theo factor:

```text
USD +3%
JPY +5% safe-haven move
global risk-off
oil +20%
front-end US yields +100 bps
KRW liquidity stress
```

Sau đó map positions vào P/L.

Scenario không cần có xác suất (probability / 확률) chính xác để hữu ích.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **17. Historical stress** nối từ **16. Scenario stress** sang **18. VaR**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Historical stress

Replay conceptual periods:

- toàn cục (global / 전역) financial stress;
- pandemic shock;
- abrupt central-bank repricing;
- peg break;
- geopolitical năng lượng (energy / 에너지) shock.

Nhưng historical scenario không bao phủ mọi future shock.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **18. VaR** nối từ **17. Historical stress** sang **19. Expected Shortfall**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. VaR

VaR trả lời gần:

> Với mô hình (model / 모델) và confidence mức (level / 수준), threshold mất mát (loss / 손실) là bao nhiêu?

Không phải maximum mất mát (loss / 손실).

FX tails/gaps/liquidity breaks làm VaR dễ underestimate extreme rủi ro (risk / 위험) nếu mô hình (model / 모델) quá Gaussian.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **19. Expected Shortfall** nối từ **18. VaR** sang **20. Drawdown ràng buộc (constraint / 제약조건)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Expected Shortfall

Expected Shortfall nhìn average mất mát (loss / 손실) beyond VaR threshold.

Nó tập trung tail tốt hơn VaR nhưng vẫn mô hình (model / 모델)/dữ liệu (data / 데이터) dependent.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **20. Drawdown ràng buộc (constraint / 제약조건)** nối từ **19. Expected Shortfall** sang **21. Volatility targeting**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Drawdown ràng buộc (constraint / 제약조건)

Portfolio có thể đặt:

- soft drawdown rà soát (review / 검토);
- hard exposure reduction;
- kill switch.

Threshold phải được thiết kế trước, không tùy cảm xúc sau mất mát (loss / 손실).

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **21. Volatility targeting** nối từ **20. Drawdown ràng buộc (constraint / 제약조건)** sang **22. Leverage cap**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Volatility targeting

Một portfolio có thể quy mô (scale / 규모) exposure để giữ mục tiêu (target / 대상) volatility:

```text
Scale ≈ Target Vol / Estimated Vol
```

Nhưng volatility estimate giảm chậm/tăng chậm có lag. Shock có thể xảy ra trước khi mô hình (model / 모델) giảm kích thước (size / 크기).

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **22. Leverage cap** nối từ **21. Volatility targeting** sang **23. Rủi ro (risk / 위험) contribution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Leverage cap

Ngoài volatility mục tiêu (target / 대상), cần cap:

- gross leverage;
- currency concentration;
- chiến lược (strategy / 전략) concentration;
- illiquid exposure.

Không dựa duy nhất vào covariance optimizer.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **23. Rủi ro (risk / 위험) contribution** nối từ **22. Leverage cap** sang **24. Rủi ro (risk / 위험) parity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Rủi ro (risk / 위험) contribution

Marginal rủi ro (risk / 위험) contribution hỏi:

> Position này thêm bao nhiêu vào portfolio volatility/rủi ro (risk / 위험)?

Một small notional position có thể đóng góp lớn nếu volatility/correlation cao.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **24. Rủi ro (risk / 위험) parity** nối từ **23. Rủi ro (risk / 위험) contribution** sang **25. Concentration by currency**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Rủi ro (risk / 위험) parity

Rủi ro (risk / 위험) parity phân bổ để các components đóng góp rủi ro (risk / 위험) tương tự.

Đây là allocation quy tắc (rule / 규칙), không đảm bảo return tốt hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **25. Concentration by currency** nối từ **24. Rủi ro (risk / 위험) parity** sang **26. Concentration by macro thesis**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. Concentration by currency

Có thể đặt cap theo:

```text
USD
EUR
JPY
GBP
AUD
KRW
...
```

Tính cả direct và synthetic exposures.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **26. Concentration by macro thesis** nối từ **25. Concentration by currency** sang **27. Sự kiện (event / 이벤트) concentration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Concentration by macro thesis

Ví dụ nhiều trades đều dựa trên “Fed dovish”. Dù tickers khác, thesis concentration vẫn lớn.

Journal nên tag thesis/factor.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **27. Sự kiện (event / 이벤트) concentration** nối từ **26. Concentration by macro thesis** sang **28. Liquidity concentration**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Sự kiện (event / 이벤트) concentration

Nếu portfolio có nhiều USD pairs trước FOMC, sự kiện (event / 이벤트) exposure tập trung.

Rủi ro (risk / 위험) ngân sách (budget / 예산) nên xét scheduled sự kiện (event / 이벤트) cluster.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **28. Liquidity concentration** nối từ **27. Sự kiện (event / 이벤트) concentration** sang **29. Cross-margin và broker dependence**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Liquidity concentration

Nhiều positions có thể liquid trong normal thị trường (market / 시장) nhưng cùng illiquid trong stress.

Need stress:

```text
spread widening
slippage multiplier
partial/no fill
margin increase
```

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **29. Cross-margin và broker dependence** nối từ **28. Liquidity concentration** sang **30. Multiple brokers không tự động safer**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Cross-margin và broker dependence

Một broker outage hoặc stop-out quy tắc (rule / 규칙) có thể ảnh hưởng toàn portfolio cùng lúc.

Operational diversification khác thị trường (market / 시장) diversification.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **30. Multiple brokers không tự động safer** nối từ **29. Cross-margin và broker dependence** sang **31. Hedge ratio**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Multiple brokers không tự động safer

Có thể giảm single-platform phụ thuộc (dependency / 의존성) nhưng tăng:

- reconciliation độ phức tạp (complexity / 복잡도);
- fragmented margin;
- transfer delay;
- inconsistent thực thi (execution / 실행).

Phải có reason rõ.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **31. Hedge ratio** nối từ **30. Multiple brokers không tự động safer** sang **32. Basis rủi ro (risk / 위험)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Hedge ratio

Nếu hedge underlying foreign asset exposure:

```text
Hedge Ratio = FX hedge notional / underlying currency exposure
```

100% hedge không luôn optimal nếu underlying exposure thay đổi hoặc hedge chi phí (cost / 비용) cao.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **32. Basis rủi ro (risk / 위험)** nối từ **31. Hedge ratio** sang **33. Động (dynamic / 동적) hedging**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Basis rủi ro (risk / 위험)

Hedge instrument có thể không perfectly match:

- currency;
- maturity;
- settlement;
- underlying exposure timing.

Residual difference là basis rủi ro (risk / 위험).

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **33. Động (dynamic / 동적) hedging** nối từ **32. Basis rủi ro (risk / 위험)** sang **34. Currency overlay**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Động (dynamic / 동적) hedging

Hedge ratio có thể adjust theo:

- asset giá trị (value / 값);
- rủi ro (risk / 위험) tolerance;
- hedge chi phí (cost / 비용);
- volatility.

Nhưng frequent rehedging tạo turnover/chi phí (cost / 비용).

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **34. Currency overlay** nối từ **33. Động (dynamic / 동적) hedging** sang **35. Portfolio of strategies**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Currency overlay

Institutional portfolio có thể tách asset allocation khỏi currency overlay.

Ví dụ giữ foreign equities nhưng hedge một phần FX exposure bằng forwards.

Điều này cho thấy FX position có thể là risk-management tầng (layer / 계층), không phải standalone speculative trade.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **35. Portfolio of strategies** nối từ **34. Currency overlay** sang **36. Capital allocation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Portfolio of strategies

Một robust hệ thống (system / 시스템) có thể combine strategies có different return drivers.

Need assess:

```text
correlation
shared factor exposure
turnover
capacity
crisis behavior
```

Không chỉ individual Sharpe.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **36. Capital allocation** nối từ **35. Portfolio of strategies** sang **37. Rebalancing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. Capital allocation

Allocation có thể dựa trên:

- equal capital;
- equal rủi ro (risk / 위험);
- expected return/rủi ro (risk / 위험);
- drawdown ngân sách (budget / 예산);
- Bayesian/uncertainty-aware estimates.

More complex không luôn better vì expected return estimates rất noisy.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **37. Rebalancing** nối từ **36. Capital allocation** sang **38. Stress correlation ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Rebalancing

Rebalance quá thường → chi phí (cost / 비용) cao.

Quá ít → exposure drift.

Need define:

- calendar-based;
- threshold-based;
- event-triggered.

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **38. Stress correlation ma trận (matrix / 행렬)** nối từ **37. Rebalancing** sang **39. Rủi ro (risk / 위험) dashboard**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Stress correlation ma trận (matrix / 행렬)

Có thể xây covariance riêng cho high-vol observations để so normal vs stress.

Nếu diversification biến mất trong stress, normal ma trận (matrix / 행렬) không đủ.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **39. Rủi ro (risk / 위험) dashboard** nối từ **38. Stress correlation ma trận (matrix / 행렬)** sang **40. Pre-trade portfolio check**, vì cơ chế trước tạo đầu vào cho bước sau.

## 39. Rủi ro (risk / 위험) dashboard

Một dashboard tối thiểu:

```text
Equity
Gross leverage
Net currency exposures
Risk by currency
Risk by strategy
Portfolio heat
Realized volatility
Drawdown
Margin headroom
Upcoming event exposure
Liquidity flags
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **40. Pre-trade portfolio check** nối từ **39. Rủi ro (risk / 위험) dashboard** sang **41. Rủi ro (risk / 위험) ngân sách (budget / 예산) không phải profit mục tiêu (target / 대상)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 40. Pre-trade portfolio check

Trước trade mới:

```text
What factor does it add?
How much currency exposure?
How correlated with existing trades?
What happens if common thesis fails?
What is portfolio heat after entry?
What event/liquidity risk is added?
```

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **41. Rủi ro (risk / 위험) ngân sách (budget / 예산) không phải profit mục tiêu (target / 대상)** nối từ **40. Pre-trade portfolio check** sang **42. Checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. Rủi ro (risk / 위험) ngân sách (budget / 예산) không phải profit mục tiêu (target / 대상)

Rủi ro (risk / 위험) ngân sách (budget / 예산) giới hạn acceptable mất mát (loss / 손실)/exposure. Không nên ép chiến lược (strategy / 전략) tạo mục tiêu (target / 대상) return bằng tăng leverage.

> **Nối mạch:** Ở chặng này của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **42. Checklist** nối từ **41. Rủi ro (risk / 위험) ngân sách (budget / 예산) không phải profit mục tiêu (target / 대상)** sang **Đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Checklist

Bạn cần tự giải thích được:

1. Ticket diversification khác factor diversification.
2. Gross vs net exposure.
3. Currency decomposition.
4. Correlation regime dependence.
5. Portfolio heat limitations.
6. Why VaR is not max mất mát (loss / 손실).
7. Volatility targeting lag.
8. Basis rủi ro (risk / 위험) trong hedge.
9. Chiến lược (strategy / 전략) correlation vs pair correlation.
10. Operational concentration.

> **Nối mạch:** Đặt trong câu hỏi lớn của **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **Đọc tiếp** nối từ **42. Checklist** sang **Nội bộ (internal / 내부) links**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đọc tiếp

→ [12 — Trading journal, review and performance attribution](./12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)

> **Nối mạch:** Trong **11 — Portfolio FX rủi ro (risk / 위험), correlation và factor exposure**, **Nội bộ (internal / 내부) links** nối từ **Đọc tiếp** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [03 — Leverage, margin and position sizing](./03_LEVERAGE_MARGIN_POSITION_SIZING.md)
- [09 — FX strategy families](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)
- [10 — Backtesting and point-in-time data](./10_BACKTESTING_AND_POINT_IN_TIME_FX_DATA.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
