# 03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Ticket không phải true exposure** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Chuẩn gốc (canonical / 정본) currency-leg biểu diễn (representation / 표현)** để xác định owner và đường quay lại nguồn chuẩn. Mạch này nối portfolio risk với attribution engine, để lợi nhuận và drawdown được quy về exposure, factor, position và quyết định.

Một chiến lược (strategy / 전략) có thể đúng ở từng trade nhưng portfolio vẫn nguy hiểm nếu nhiều position thực chất là cùng một factor bet. Mô-đun (module / 모듈) này xây tầng (layer / 계층) biến **tickets → currency legs → factor exposures → portfolio rủi ro (risk / 위험) → P/L attribution**.

Mục tiêu là để hệ thống trả lời được hai câu hỏi khác nhau:

```text
What risks are we carrying now?
Why did the portfolio make or lose money?
```

Nếu không answer được cả hai, rủi ro (risk / 위험) management và research vòng phản hồi (feedback loop / 피드백 루프) đều thiếu.

## 1. Ticket không phải true exposure

Ví dụ:

```text
Long EUR/USD
Long GBP/USD
Short USD/JPY
```

Ba tickets nhưng decomposition:

```text
+EUR -USD
+GBP -USD
-USD +JPY
```

USD short factor xuất hiện ba lần.

Rủi ro (risk / 위험) engine phải aggregate legs thay vì chỉ đếm positions.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, sau nội dung của **1. Ticket không phải true exposure**, **2. Chuẩn gốc (canonical / 정본) currency-leg biểu diễn (representation / 표현)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **3. Reporting currency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Chuẩn gốc (canonical / 정본) currency-leg biểu diễn (representation / 표현)

Mỗi FX position `A/B` có thể biểu diễn:

```text
Long A/B  → +A, -B
Short A/B → -A, +B
```

Quy mô (scale / 규모) legs theo notional và hiện tại (current / 현재) price để có comparable reporting currency exposure.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **3. Reporting currency** tiếp nhận điểm tựa từ **2. Chuẩn gốc (canonical / 정본) currency-leg biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Gross và net exposure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Reporting currency

Chọn một reporting currency, ví dụ USD hoặc KRW.

Mọi exposure/P&L phải có:

```text
native currency
reporting currency
conversion timestamp
conversion rate source
```

Không overwrite bản địa (native / 네이티브) amount sau conversion; giữ cả hai để kiểm tra (audit / 감사).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **4. Gross và net exposure** tiếp nhận điểm tựa từ **3. Reporting currency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Gross leverage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Gross và net exposure

Tính:

```text
Gross Exposure = Σ absolute economic exposures
Net Currency Exposure = sum of signed legs by currency
```

Net nhỏ không đồng nghĩa rủi ro (risk / 위험) nhỏ vì gross exposure vẫn tạo:

```text
liquidity risk
margin usage
basis risk
execution cost
```

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **5. Gross leverage** tiếp nhận điểm tựa từ **4. Gross và net exposure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Net leverage không đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Gross leverage

```text
Gross Leverage = Σ|notional_i| / Equity
```

Nhánh học (track / 트랙) phân phối (distribution / 분포) theo thời gian:

```text
median
95th percentile
maximum
```

Một end-of-day snapshot có thể bỏ lỡ intraday leverage spikes.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **6. Net leverage không đủ** tiếp nhận điểm tựa từ **5. Gross leverage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Factor buckets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Net leverage không đủ

Hai opposing positions có thể giảm net directional exposure nhưng vẫn có:

```text
cross risk
basis risk
financing
spread/slippage
```

Rủi ro (risk / 위험) dashboard nên show cả gross và net.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **7. Factor buckets** tiếp nhận điểm tựa từ **6. Net leverage không đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Factor loading is conditional** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Factor buckets

Ngoài currency legs, map positions vào factors tùy chiến lược (strategy / 전략):

```text
Broad USD
Rate differential
Carry
Risk sentiment
Commodity beta
China/global-growth beta
Funding currency
Volatility
```

Factor ánh xạ (mapping / 매핑) có thể model-based hoặc heuristic, nhưng phải versioned.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **8. Factor loading is conditional** tiếp nhận điểm tựa từ **7. Factor buckets** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Currency exposure bảng (table / 테이블)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Factor loading is conditional

EUR/USD sensitivity to yields không cố định.

Do đó factor beta nên có:

```text
estimation window
regime label
confidence / error
```

Không trình bày estimated beta như vật lý (physical / 물리적) constant.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **9. Currency exposure bảng (table / 테이블)** tiếp nhận điểm tựa từ **8. Factor loading is conditional** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Pair correlation vs currency-factor overlap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Currency exposure bảng (table / 테이블)

Đầu ra (output / 출력) ví dụ:

```text
Currency | Long Equivalent | Short Equivalent | Net | Stress Loss
EUR
USD
JPY
GBP
AUD
KRW
```

Rows phải derive từ positions, không manual spreadsheet nếu hệ thống (system / 시스템) có thể calculate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **10. Pair correlation vs currency-factor overlap** tiếp nhận điểm tựa từ **9. Currency exposure bảng (table / 테이블)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Covariance ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Pair correlation vs currency-factor overlap

Correlation giữa EUR/USD và GBP/USD có thể thay đổi.

Nhưng cả hai structurally contain USD leg.

Factor decomposition cung cấp thông tin (information / 정보) mà mẫu (sample / 표본) correlation có thể bỏ lỡ.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **11. Covariance ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **10. Pair correlation vs currency-factor overlap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Stress correlation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Covariance ma trận (matrix / 행렬)

Với return véc-tơ (vector / 벡터) `r` và weights `w`:

```text
Portfolio Variance = w' Σ w
```

Useful nhưng phụ thuộc mẫu (sample / 표본).

Store covariance mô hình (model / 모델) phiên bản (version / 버전) và estimation period.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **12. Stress correlation** tiếp nhận điểm tựa từ **11. Covariance ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Volatility targeting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Stress correlation

Normal correlation thường underestimate crisis clustering.

Compute separately nếu dữ liệu (data / 데이터) đủ:

```text
normal regime correlation
high-volatility correlation
downside correlation
funding-stress correlation
```

Do not assume one covariance ma trận (matrix / 행렬) describes all states.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **13. Volatility targeting** tiếp nhận điểm tựa từ **12. Stress correlation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Rủi ro (risk / 위험) contribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Volatility targeting

Mục tiêu (target / 대상) rủi ro (risk / 위험) example:

```text
Position Risk Budget
= Target Volatility / Estimated Instrument Volatility
```

Nhưng cap kích thước (size / 크기) bằng liquidity/margin các ràng buộc (constraints / 제약조건들).

Vol targeting without leverage cap can increase exposure dramatically in calm regime just before volatility jumps.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **14. Rủi ro (risk / 위험) contribution** tiếp nhận điểm tựa từ **13. Volatility targeting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Planned mất mát (loss / 손실) vs statistical rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Rủi ro (risk / 위험) contribution

Approximate marginal/thành phần (component / 컴포넌트) rủi ro (risk / 위험) giúp biết position nào đóng góp portfolio volatility.

Mục tiêu:

```text
Portfolio weight
≠ Portfolio risk contribution
```

A small position can dominate rủi ro (risk / 위험) if volatility/correlation high.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **15. Planned mất mát (loss / 손실) vs statistical rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **14. Rủi ro (risk / 위험) contribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Portfolio heat** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Planned mất mát (loss / 손실) vs statistical rủi ro (risk / 위험)

Trade stop-based rủi ro (risk / 위험):

```text
planned loss if stop executes normally
```

Statistical rủi ro (risk / 위험):

```text
distribution-based loss estimate
```

Stress rủi ro (risk / 위험):

```text
loss under specified extreme scenario
```

Store all three; none replaces the others.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **16. Portfolio heat** tiếp nhận điểm tựa từ **15. Planned mất mát (loss / 손실) vs statistical rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Scenario engine** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Portfolio heat

Define one practical chỉ số (metric / 지표):

```text
Portfolio Heat = Σ planned stop losses
```

Then enhance with cluster stress:

```text
Correlated Heat = stressed loss if common factor moves and slippage widens
```

Naive heat ignores dùng chung (shared / 공유) USD/carry factor.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **17. Scenario engine** tiếp nhận điểm tựa từ **16. Portfolio heat** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Deterministic shock examples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Scenario engine

Scenario đối tượng (object / 객체):

```text
scenario_id
currency shocks
rate shocks
volatility shock
spread multiplier
slippage multiplier
margin-policy shock
notes
```

Apply same scenarios across historical experiments for comparability.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **17. Scenario engine** cho ta quy tắc; **18. Deterministic shock examples** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **19. Combined scenario** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Deterministic shock examples

```text
USD +5% broad
JPY +8% funding unwind
Oil +20%
US 2Y +100 bp
Risk-off + spread 3x
KRW -10% vs USD
```

Scenarios are not forecasts. They kiểm thử (test / 테스트) survivability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **18. Deterministic shock examples** cho ta quy tắc; **19. Combined scenario** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **20. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Combined scenario

Crisis rarely moves one variable.

Example:

```text
USD +4%
JPY +6%
Gold -5% initially
FX spreads 4x
Margin requirement +50%
```

Combined scenario often reveals hidden fragility.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **20. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** tiếp nhận điểm tựa từ **19. Combined scenario** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. VaR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)

Instead of choosing shock first, solve:

```text
What combination causes:
-10% equity
margin level < threshold
or forced liquidation?
```

Reverse stress identifies thất bại (failure / 실패) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **21. VaR** tiếp nhận điểm tựa từ **20. Reverse kiểm thử sức chịu tải (stress test / 스트레스 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Expected Shortfall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. VaR

VaR can answer:

```text
Under model assumptions,
what loss threshold corresponds to confidence level X?
```

It cannot answer maximum possible mất mát (loss / 손실).

Store mô hình (model / 모델)/phương thức (method / 메서드):

```text
historical
parametric
Monte Carlo
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **22. Expected Shortfall** tiếp nhận điểm tựa từ **21. VaR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Tail events outside mẫu (sample / 표본)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Expected Shortfall

Expected Shortfall estimates average mất mát (loss / 손실) beyond VaR threshold.

Still depends on dữ liệu (data / 데이터)/mô hình (model / 모델) and may underestimate regime breaks absent from mẫu (sample / 표본).

Use alongside scenario tests.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **23. Tail events outside mẫu (sample / 표본)** tiếp nhận điểm tựa từ **22. Expected Shortfall** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Margin stress** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Tail events outside mẫu (sample / 표본)

CHF 2015-style discontinuity demonstrates:

```text
Historical distribution
may exclude relevant future regime break
```

Rủi ro (risk / 위험) engine needs tường minh (explicit / 명시적) jump scenarios not just empirical quantiles.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **24. Margin stress** tiếp nhận điểm tựa từ **23. Tail events outside mẫu (sample / 표본)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Động (dynamic / 동적) margin chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Margin stress

For each scenario compute:

```text
Equity
Used Margin
Free Margin
Margin Level
Gross Leverage
Positions liquidated under policy
```

Price rủi ro (risk / 위험) and margin rủi ro (risk / 위험) must be simulated together.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **25. Động (dynamic / 동적) margin chính sách (policy / 정책)** tiếp nhận điểm tựa từ **24. Margin stress** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Liquidity stress** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Động (dynamic / 동적) margin chính sách (policy / 정책)

Provider may raise margin during stress.

Scenario:

```text
Margin requirement × 2
without price move
```

can still force deleveraging.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **26. Liquidity stress** tiếp nhận điểm tựa từ **25. Động (dynamic / 동적) margin chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Concentration limits** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Liquidity stress

Add:

```text
spread multiplier
slippage multiplier
max executable size reduction
```

A position may be small in notional but hard to exit in stressed thị trường (market / 시장).

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **26. Liquidity stress** đã nêu tiêu chí phân biệt, còn **27. Concentration limits** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. Pre-trade rủi ro (risk / 위험) check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Concentration limits

Possible limits:

```text
max instrument notional
max currency net exposure
max factor exposure
max gross leverage
max planned portfolio heat
max stressed loss
max margin utilization
```

Limits should be chiến lược (strategy / 전략)/account specific, not universal percentages.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **27. Concentration limits** đã nêu tiêu chí phân biệt, còn **28. Pre-trade rủi ro (risk / 위험) check** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Post-fill check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Pre-trade rủi ro (risk / 위험) check

Before thứ tự (order / 순서):

```text
Current portfolio
+ proposed fill
→ projected exposures
→ projected margin
→ projected stress loss
```

Reject if limits breached.

Do not check only position after fill.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **29. Post-fill check** tiếp nhận điểm tựa từ **28. Pre-trade rủi ro (risk / 위험) check** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Hedge biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Post-fill check

Actual fill may differ from requested kích thước (size / 크기)/price.

Recompute rủi ro (risk / 위험) using filled quantity immediately.

Partial fill changes hedge ratio.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **30. Hedge biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **29. Post-fill check** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Hedge effectiveness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Hedge biểu diễn (representation / 표현)

A hedge must have mục tiêu (target / 대상):

```text
hedged factor
hedge instrument
hedge ratio
expected basis risk
carry cost
liquidity
```

Do not label position “hedged” as boolean only.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **31. Hedge effectiveness** tiếp nhận điểm tựa từ **30. Hedge biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. P/L attribution kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Hedge effectiveness

Measure:

```text
Reduction in targeted exposure
Reduction in stress loss
Cost introduced
Residual basis risk
```

A hedge can reduce variance while increasing negative carry.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **32. P/L attribution kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **31. Hedge effectiveness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Gross vs net alpha** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. P/L attribution kiến trúc (architecture / 아키텍처)

Portfolio P/L should decompose:

```text
price / spot move
carry / financing
spread
commission
slippage
currency conversion
hedge P/L
other fees
```

Then aggregate by:

```text
strategy
instrument
currency
factor
session
event/regime
```

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **33. Gross vs net alpha** tiếp nhận điểm tựa từ **32. P/L attribution kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Factor attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Gross vs net alpha

Define:

```text
Gross Signal P/L
- implementation costs
- financing
= Net Strategy P/L
```

Research should not lời gọi (call / 호출) gross paper return “alpha”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **34. Factor attribution** tiếp nhận điểm tựa từ **33. Gross vs net alpha** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Benchmark attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Factor attribution

If portfolio gains because broad USD moves, but chiến lược (strategy / 전략) thesis was pair-specific giá trị (value / 값):

```text
factor attribution reveals mismatch
```

This is crucial for học tập (learning / 학습) whether edge came from intended cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **35. Benchmark attribution** tiếp nhận điểm tựa từ **34. Factor attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. R-multiple attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Benchmark attribution

Possible benchmarks:

```text
zero exposure
simple carry basket
broad USD factor
risk-parity FX basket
```

Benchmark depends on chiến lược (strategy / 전략) mục tiêu (objective / 목표).

Do not choose benchmark after seeing hiệu năng (performance / 성능).

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **36. R-multiple attribution** tiếp nhận điểm tựa từ **35. Benchmark attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. MAE/MFE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. R-multiple attribution

At trade mức (level / 수준):

```text
Realized R = Net P/L / Planned Initial Risk
```

Also store:

```text
Gross R
Cost R
Slippage R
```

This normalizes trades of different sizes.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **37. MAE/MFE** tiếp nhận điểm tựa từ **36. R-multiple attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Drawdown attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. MAE/MFE

Store:

```text
Maximum Adverse Excursion
Maximum Favorable Excursion
```

relative to entry and planned R.

Useful for exit research but vulnerable to hindsight overfitting if repeatedly optimized.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **38. Drawdown attribution** tiếp nhận điểm tựa từ **37. MAE/MFE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Correlated losing clusters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Drawdown attribution

When portfolio hits drawdown, identify:

```text
which strategies
which currencies
which factors
which cost components
```

contributed.

Do not treat drawdown as one number only.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **39. Correlated losing clusters** tiếp nhận điểm tựa từ **38. Drawdown attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Risk-adjusted metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Correlated losing clusters

Detect periods where multiple strategies lose simultaneously.

This may reveal:

```text
shared hidden factor
regime dependence
liquidity shock
```

Portfolio of strategies is not diversified merely because chiến lược (strategy / 전략) names differ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **40. Risk-adjusted metrics** tiếp nhận điểm tựa từ **39. Correlated losing clusters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Turnover and sức chứa (capacity / 용량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Risk-adjusted metrics

Can report:

```text
Sharpe
Sortino
Calmar
Max Drawdown
Expected Shortfall
```

but always alongside leverage, liquidity and tail scenarios.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **41. Turnover and sức chứa (capacity / 용량)** tiếp nhận điểm tựa từ **40. Risk-adjusted metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Exposure by session** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Turnover and sức chứa (capacity / 용량)

Nhánh học (track / 트랙):

```text
turnover
average ticket size
size relative to liquidity proxy
```

A scalable chiến lược (strategy / 전략) should not assume unlimited thực thi (execution / 실행) at top-of-book.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **42. Exposure by session** tiếp nhận điểm tựa từ **41. Turnover and sức chứa (capacity / 용량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Sự kiện (event / 이벤트) rủi ro (risk / 위험) inventory** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Exposure by session

Rủi ro (risk / 위험) may cluster around:

```text
Asia
London
New York
rollover
macro-event windows
```

Report exposure before major scheduled events.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **43. Sự kiện (event / 이벤트) rủi ro (risk / 위험) inventory** tiếp nhận điểm tựa từ **42. Exposure by session** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Chiến lược (strategy / 전략) virtual books** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Sự kiện (event / 이벤트) rủi ro (risk / 위험) inventory

At any thời gian (time / 시간) hệ thống (system / 시스템) can danh sách (list / 목록):

```text
positions
next known central-bank event
next macro release
weekend holding
```

This supports event-specific limits.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **44. Chiến lược (strategy / 전략) virtual books** tiếp nhận điểm tựa từ **43. Sự kiện (event / 이벤트) rủi ro (risk / 위험) inventory** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Allocation of thực thi (execution / 실행) chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Chiến lược (strategy / 전략) virtual books

If broker nets positions but multiple strategies share pair, maintain nội bộ (internal / 내부) virtual books:

```text
strategy_A +50k EUR/USD
strategy_B -20k EUR/USD
broker net +30k
```

Attribution remains possible.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **45. Allocation of thực thi (execution / 실행) chi phí (cost / 비용)** tiếp nhận điểm tựa từ **44. Chiến lược (strategy / 전략) virtual books** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Allocation of financing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Allocation of thực thi (execution / 실행) chi phí (cost / 비용)

When orders are netted, need quy tắc (rule / 규칙) to allocate savings/costs among strategies.

Possible:

```text
pro rata by requested quantity
```

Document consistently.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **46. Allocation of financing** tiếp nhận điểm tựa từ **45. Allocation of thực thi (execution / 실행) chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Reconciliation bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Allocation of financing

Financing charged to net broker position may differ from sum of virtual chiến lược (strategy / 전략) positions.

Define attribution chính sách (policy / 정책); otherwise strategy-level P/L won't reconcile to account P/L.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **47. Reconciliation bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **46. Allocation of financing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Rủi ro (risk / 위험) snapshot lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Reconciliation bất biến (invariant / 불변식)

At end of period:

```text
Σ strategy attributed P/L
+ unallocated account adjustments
= account P/L
```

Difference must be zero within rounding tolerance.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **48. Rủi ro (risk / 위험) snapshot lược đồ (schema / 스키마)** tiếp nhận điểm tựa từ **47. Reconciliation bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Rủi ro (risk / 위험) snapshot lược đồ (schema / 스키마)

Example:

```text
snapshot_time
account_equity
gross_leverage
used_margin
free_margin
currency_exposures_json
factor_exposures_json
planned_heat
stress_loss_base
stress_loss_severe
```

Store snapshots for later rà soát (review / 검토).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)** tiếp nhận điểm tựa từ **48. Rủi ro (risk / 위험) snapshot lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)

```text
scenario_id
snapshot_time
projected_pnl
projected_equity
projected_margin_level
largest_loss_factor
liquidation_flag
```

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)** tiếp nhận điểm tựa từ **49. Scenario kết quả (result / 결과) lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Đơn vị (unit / 단위) tests — decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)

```text
trade_id
strategy_id
instrument
spot_pnl
carry_pnl
spread_cost
commission
slippage_cost
conversion_effect
net_pnl
factor_tags
```

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **51. Đơn vị (unit / 단위) tests — decomposition** tiếp nhận điểm tựa từ **50. Attribution bản ghi (record / 레코드) lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Đơn vị (unit / 단위) tests — aggregation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Đơn vị (unit / 단위) tests — decomposition

Example:

```text
Long 100k EUR/USD
```

must produce:

```text
+100k EUR economic leg
negative USD leg equal to quote value
```

within defined valuation convention.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **52. Đơn vị (unit / 단위) tests — aggregation** tiếp nhận điểm tựa từ **51. Đơn vị (unit / 단위) tests — decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Đơn vị (unit / 단위) tests — P/L reconciliation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Đơn vị (unit / 단위) tests — aggregation

Long EUR/USD + long GBP/USD should show larger negative USD aggregate than either trade alone.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **53. Đơn vị (unit / 단위) tests — P/L reconciliation** tiếp nhận điểm tựa từ **52. Đơn vị (unit / 단위) tests — aggregation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. Stress regression tests** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Đơn vị (unit / 단위) tests — P/L reconciliation

For known fills and costs:

```text
Gross P/L - costs = Net P/L
```

and sum of chiến lược (strategy / 전략) attribution equals account ledger.

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **54. Stress regression tests** tiếp nhận điểm tựa từ **53. Đơn vị (unit / 단위) tests — P/L reconciliation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Mô hình (model / 모델) thay đổi (change / 변경) quản trị (governance / 거버넌스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Stress regression tests

Keep fixed scenarios so mã (code / 코드) changes don't silently alter rủi ro (risk / 위험) calculation.

Example expected outputs can use tolerance ranges.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **55. Mô hình (model / 모델) thay đổi (change / 변경) quản trị (governance / 거버넌스)** tiếp nhận điểm tựa từ **54. Stress regression tests** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Completion criteria** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Mô hình (model / 모델) thay đổi (change / 변경) quản trị (governance / 거버넌스)

If rủi ro (risk / 위험) mô hình (model / 모델) changes:

```text
risk_model_version++
```

Do not overwrite historical rủi ro (risk / 위험) snapshots with new methodology without label.

> **Chuyển mạch:** Trong **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **56. Completion criteria** tiếp nhận điểm tựa từ **55. Mô hình (model / 모델) thay đổi (change / 변경) quản trị (governance / 거버넌스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deliverables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Completion criteria

Reviewer should be able to answer:

```text
Which currencies are we truly long/short?
Which common factors dominate risk?
What loss occurs under severe scenario?
Will margin force liquidation first?
Where did yesterday's P/L actually come from?
Did intended edge or unintended beta generate return?
```

> **Chuyển mạch:** Ở chặng này của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **Deliverables** tiếp nhận điểm tựa từ **56. Completion criteria** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deliverables

Create:

```text
currency_exposure_spec.md
factor_model_spec.md
risk_limits.md
stress_scenarios.md
portfolio_risk_report.md
pnl_attribution_spec.md
attribution_report.md
reconciliation_tests.md
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — Portfolio Rủi ro (risk / 위험) và Attribution Engine cho Systematic FX**, **Đọc tiếp** tiếp nhận điểm tựa từ **Deliverables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Đọc tiếp

→ [04 — Forward Test, Monitoring và Kill Switch](./04_FORWARD_TEST_MONITORING_AND_KILL_SWITCH.md)

Liên quan:

- [11 — Portfolio FX risk](../11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)
- [12 — Journal, review and attribution](../12_TRADING_JOURNAL_REVIEW_AND_PERFORMANCE_ATTRIBUTION.md)
- [03 — Leverage, margin and position sizing](../03_LEVERAGE_MARGIN_POSITION_SIZING.md)

> **Bàn giao:** Sau **Đọc tiếp**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
