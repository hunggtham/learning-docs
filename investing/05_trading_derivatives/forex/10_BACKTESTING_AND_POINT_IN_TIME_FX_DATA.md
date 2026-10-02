# 10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)

> **Mạch đọc:** [README](./README.md) là owner của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**; dùng README để nối chapter với technical/fundamental FX và execution. Từ **1. Câu hỏi đầu tiên: chiến lược (strategy / 전략) biết gì tại thời điểm t?** đi qua point-in-time data, signal timestamp, realistic execution, costs, financing và out-of-sample validation; kết quả chỉ đáng tin khi không có look-ahead.

Backtest không phải máy chứng minh chiến lược (strategy / 전략) có edge. Nó là **thí nghiệm lịch sử có giả định**. Nếu dữ liệu, timestamp, thực thi (execution / 실행) hoặc selection tiến trình (process / 프로세스) sai, kết quả có thể chính xác về mã (code / 코드) nhưng sai về kinh tế.

Mô hình tư duy (mental model / 사고 모델):

```text
Hypothesis
→ point-in-time data
→ signal known at t
→ realistic execution after t
→ costs / financing
→ portfolio accounting
→ out-of-sample validation
→ uncertainty estimate
```

## 1. Câu hỏi đầu tiên: chiến lược (strategy / 전략) biết gì tại thời điểm t?

Mọi tính năng (feature / 기능) phải trả lời:

```text
Was this exact value observable then?
```

Nếu câu trả lời là không, backtest có look-ahead.

Ví dụ:

- revised CPI final giá trị (value / 값) chưa tồn tại lúc bản phát hành (release / 릴리스) đầu tiên;
- swing high cần future bars để confirm;
- end-of-day high/low chưa biết giữa ngày;
- historical constituent danh sách (list / 목록) hôm nay không đại diện past universe.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **1. Câu hỏi đầu tiên: chiến lược (strategy / 전략) biết gì tại thời điểm t?** nêu điều cần giải thích; **2. Point-in-time dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Vintage dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Point-in-time dữ liệu (data / 데이터)

**Point-in-time** nghĩa là dataset tái tạo thông tin như nó được biết tại thời điểm lịch sử đó.

Đặc biệt quan trọng với:

- macro releases;
- central-bank expectations;
- analyst forecasts;
- chỉ mục (index / 인덱스)/universe membership;
- financing rates;
- đặc tả hợp đồng (contract / 계약) specifications.

Final cleaned cơ sở dữ liệu (database / 데이터베이스) thường tốt cho economic lịch sử (history / 이력) nhưng có thể không hợp live-strategy simulation.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **2. Point-in-time dữ liệu (data / 데이터)** nêu điều cần giải thích; **3. Vintage dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Timezone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Vintage dữ liệu (data / 데이터)

Macro dữ liệu (data / 데이터) thường có revisions.

Research sự kiện (event / 이벤트) chiến lược (strategy / 전략) cần lưu:

```text
release timestamp
first-release value
consensus known before release
later revisions separately
```

Không được dùng final revised number để tính surprise quá khứ nếu trader lúc đó chưa biết.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **3. Vintage dữ liệu (data / 데이터)** nêu điều cần giải thích; **4. Timezone** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. Bar timestamp convention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Timezone

FX là 24-hour thị trường (market / 시장) nên timezone bug cực nguy hiểm.

Chuỗi xử lý (pipeline / 파이프라인) nên dùng:

```text
UTC internally
+
source timezone metadata
+
explicit local-session conversion
```

Daylight-saving phải được xử lý bằng timezone cơ sở dữ liệu (database / 데이터베이스), không hard-code offset quanh năm.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **5. Bar timestamp convention** tiếp nhận điểm tựa từ **4. Timezone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Bid, ask hay mid?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Bar timestamp convention

Một bar timestamp có thể đại diện:

- bar open thời gian (time / 시간);
- bar close thời gian (time / 시간);
- exchange/vendor convention.

Nếu không hiểu convention, tín hiệu (signal / 신호) có thể bị shifted một bar.

Ví dụ daily FX bars giữa vendors có thể dùng different session cutoff, tạo OHLC khác nhau.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **6. Bid, ask hay mid?** tiếp nhận điểm tựa từ **5. Bar timestamp convention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. OHLC limitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Bid, ask hay mid?

Nếu chiến lược (strategy / 전략) giao dịch thực tế ở bid/ask nhưng backtest dùng mid-price:

```text
entry too good
exit too good
spread cost missing
```

Tối thiểu phải apply spread mô hình (model / 모델). Với short-horizon chiến lược (strategy / 전략), historical bid/ask dữ liệu (data / 데이터) càng quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **6. Bid, ask hay mid?** đã nêu tiêu chí phân biệt, còn **7. OHLC limitation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Tick dữ liệu (data / 데이터) không tự động hoàn hảo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. OHLC limitation

Một bar chỉ cho:

```text
Open
High
Low
Close
```

Nó không cho intrabar chuỗi (sequence / 시퀀스).

Nếu cùng một bar vừa chạm stop vừa chạm mục tiêu (target / 대상), không biết cái nào xảy ra trước nếu không có finer dữ liệu (data / 데이터).

Conservative quy tắc (rule / 규칙) hoặc lower-resolution dữ liệu (data / 데이터) cần được dùng.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **7. OHLC limitation** đã nêu tiêu chí phân biệt, còn **8. Tick dữ liệu (data / 데이터) không tự động hoàn hảo** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. Broker-specific dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Tick dữ liệu (data / 데이터) không tự động hoàn hảo

Tick datasets có thể có:

- bad ticks;
- duplicated timestamps;
- stale quotes;
- different liquidity sources;
- missing periods;
- clock issues.

Higher resolution tăng data-quality burden.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **8. Tick dữ liệu (data / 데이터) không tự động hoàn hảo** nêu điều cần giải thích; **9. Broker-specific dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Universe selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Broker-specific dữ liệu (data / 데이터)

Retail chiến lược (strategy / 전략) deployed tại broker A nhưng backtest trên feed B có basis mismatch:

- spread khác;
- Sunday candles khác;
- rollover khác;
- high/low khác;
- stop trigger khác.

Không cần feed giống tuyệt đối, nhưng sensitivity cần được hiểu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **9. Broker-specific dữ liệu (data / 데이터)** nêu điều cần giải thích; **10. Universe selection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Structural breaks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Universe selection

Nếu chỉ backtest các major pairs hiện nay, có thể bỏ qua currencies/instruments từng tồn tại hoặc thay đổi regime.

Với FX majors, survivorship độ lệch (bias / 편향) ít trực diện hơn equities nhưng vẫn có:

- currency regime changes;
- pegs/breaks;
- capital controls;
- redenomination;
- liquidity changes.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **11. Structural breaks** tiếp nhận điểm tựa từ **10. Universe selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Tín hiệu (signal / 신호) timestamp và fill timestamp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Structural breaks

Examples conceptual:

```text
fixed/managed regime → float
capital controls change
negative-rate era begins/ends
market microstructure changes
```

Full-history average có thể trộn incompatible states.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **12. Tín hiệu (signal / 신호) timestamp và fill timestamp** tiếp nhận điểm tựa từ **11. Structural breaks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Tín hiệu (signal / 신호) timestamp và fill timestamp

Nếu tín hiệu (signal / 신호) dùng closing price tại `t`:

```text
Signal becomes known after/at close
```

Fill không nên magically xảy ra trước tín hiệu (signal / 신호).

Reasonable thực thi (execution / 실행):

```text
next executable quote
or
explicit closing-auction/market-on-close mechanism if product supports it
```

Retail OTC FX thường không có centralized closing auction như equities.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **13. Độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **12. Tín hiệu (signal / 신호) timestamp và fill timestamp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Spread mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Độ trễ (latency / 지연 시간)

Intraday các hệ thống (systems / 시스템들) cần mô hình (model / 모델):

```text
data arrival
→ calculation
→ order transmission
→ broker/venue processing
→ fill
```

Milliseconds có thể irrelevant với daily chiến lược (strategy / 전략) nhưng decisive với news scalping.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **14. Spread mô hình (model / 모델)** tiếp nhận điểm tựa từ **13. Độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Slippage mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Spread mô hình (model / 모델)

Levels:

```text
Level 1: fixed conservative spread
Level 2: pair + session spread
Level 3: historical bid/ask spread
Level 4: regime/event-aware executable quotes
```

Mô hình (model / 모델) độ phức tạp (complexity / 복잡도) phải tương xứng dữ liệu (data / 데이터) chất lượng (quality / 품질).

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **15. Slippage mô hình (model / 모델)** tiếp nhận điểm tựa từ **14. Spread mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Financing / rollover** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Slippage mô hình (model / 모델)

Một simple approach:

```text
slippage = fixed fraction of spread/ATR
```

better approach có thể điều kiện (condition / 조건) on:

- volatility;
- sự kiện (event / 이벤트) windows;
- thứ tự (order / 순서) kích thước (size / 크기);
- liquidity/session.

Nhưng slippage mô hình (model / 모델) cũng có thể overfit.

Sensitivity kiểm thử (test / 테스트) quan trọng hơn false precision.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **16. Financing / rollover** tiếp nhận điểm tựa từ **15. Slippage mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Forward-based research** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Financing / rollover

Swing/carry strategies phải include financing lịch sử (history / 이력).

Không được apply hiện tại (current / 현재) broker swap tỷ lệ (rate / 비율) cho 10 năm lịch sử.

Nếu historical retail financing không có, cần dùng transparent proxy + conservative markup và document limitation.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **17. Forward-based research** tiếp nhận điểm tựa từ **16. Financing / rollover** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Position sizing trong backtest** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Forward-based research

Academic FX carry research thường dùng spot + forward rates. Nếu hiện thực (implementation / 구현) thực tế dùng CFDs/rolling spot, cầu nối (bridge / 브리지) từ forward return sang retail realized P/L phải được giải thích.

Instrument mismatch là mô hình (model / 모델) rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **18. Position sizing trong backtest** tiếp nhận điểm tựa từ **17. Forward-based research** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Margin accounting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Position sizing trong backtest

Fixed lot làm account rủi ro (risk / 위험) thay đổi theo volatility/equity.

Nếu live plan dùng volatility scaling hoặc percent rủi ro (risk / 위험), backtest phải implement cùng quy tắc (rule / 규칙).

Không nên backtest tín hiệu (signal / 신호) fixed-notional rồi report kết quả (result / 결과) như fixed-risk chiến lược (strategy / 전략).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **19. Margin accounting** tiếp nhận điểm tựa từ **18. Position sizing trong backtest** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Stop-loss simulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Margin accounting

Leveraged backtest phải nhánh học (track / 트랙):

```text
cash/balance
equity
notional
used margin
financing
realized/unrealized P/L
```

Nếu chiến lược (strategy / 전략) có thể vi phạm margin yêu cầu (requirement / 요구사항) historically, không thể giả định position vẫn tồn tại đến final exit.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **20. Stop-loss simulation** tiếp nhận điểm tựa từ **19. Margin accounting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Limit-order fill độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Stop-loss simulation

Stop backtest cần xác định:

- trigger price side;
- gap hành vi (behavior / 동작);
- spread widening;
- intrabar đường dẫn (path / 경로) giả định (assumption / 가정).

Một chính xác (exact / 정확한) stop fill mọi lần là optimistic.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **20. Stop-loss simulation** đã nêu tiêu chí phân biệt, còn **21. Limit-order fill độ lệch (bias / 편향)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **22. Look-ahead độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Limit-order fill độ lệch (bias / 편향)

Price touching limit không guarantee fill. Hàng đợi (queue / 큐) position và liquidity matter.

Backtest kiểu:

```text
Low <= buy limit → filled
```

có thể overestimate fills, đặc biệt short-horizon.

Conservative các giả định (assumptions / 가정들) hoặc actual order-book/quote dữ liệu (data / 데이터) cần thiết nếu edge phụ thuộc passive fills.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **21. Limit-order fill độ lệch (bias / 편향)** đã nêu tiêu chí phân biệt, còn **22. Look-ahead độ lệch (bias / 편향)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **23. Dữ liệu (data / 데이터) snooping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Look-ahead độ lệch (bias / 편향)

Dùng chung (common / 공통) forms:

- using future-confirmed pivots;
- future volatility estimate;
- revised macro dữ liệu (data / 데이터);
- tối ưu hóa (optimization / 최적화) over full mẫu (sample / 표본) rồi report same mẫu (sample / 표본);
- normalizing bằng full-sample mean/std.

Preprocessing cũng phải fit only on huấn luyện (training / 학습) lịch sử (history / 이력).

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **22. Look-ahead độ lệch (bias / 편향)** nêu điều cần giải thích; **23. Dữ liệu (data / 데이터) snooping** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. In-sample, kiểm tra hợp lệ (validation / 검증), kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Dữ liệu (data / 데이터) snooping

Nếu thử hàng nghìn variations, best kết quả (result / 결과) likely upward-biased.

Research log nên ghi:

```text
all hypotheses tested
all parameter variants
all rejected models
```

Không chỉ final winner.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **23. Dữ liệu (data / 데이터) snooping** nêu điều cần giải thích; **24. In-sample, kiểm tra hợp lệ (validation / 검증), kiểm thử (test / 테스트)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Walk-forward** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. In-sample, kiểm tra hợp lệ (validation / 검증), kiểm thử (test / 테스트)

Chronological split phù hợp thời gian (time / 시간) series hơn random shuffle.

Ví dụ conceptual:

```text
Train → choose broad model
Validation → tune limited parameters
Test → final untouched evaluation
```

Sau khi xem kiểm thử (test / 테스트) kết quả (result / 결과) và thay mô hình (model / 모델), kiểm thử (test / 테스트) không còn untouched nữa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **25. Walk-forward** tiếp nhận điểm tựa từ **24. In-sample, kiểm tra hợp lệ (validation / 검증), kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Purging và embargo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Walk-forward

Walk-forward mô phỏng repeated research/triển khai (deployment / 배포):

```text
train window
→ test next period
→ roll forward
→ retrain if allowed
→ repeat
```

Nó giúp đánh giá parameter stability và regime adaptation.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **26. Purging và embargo** tiếp nhận điểm tựa từ **25. Walk-forward** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Cross-validation không được random máy móc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Purging và embargo

Khi labels overlap in thời gian (time / 시간), train/kiểm thử (test / 테스트) samples có thể leak thông tin (information / 정보).

Purging/embargo tách observations quanh ranh giới (boundary / 경계) để giảm overlap leakage.

Đặc biệt relevant với ML/horizon returns.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **27. Cross-validation không được random máy móc** tiếp nhận điểm tựa từ **26. Purging và embargo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Parameter surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Cross-validation không được random máy móc

Random k-fold phá chronology và có thể train on future relative to kiểm thử (test / 테스트).

Time-series CV phải preserve thứ tự (ordering / 순서) và overlap cấu trúc (structure / 구조).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **28. Parameter surface** tiếp nhận điểm tựa từ **27. Cross-validation không được random máy móc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Multiple testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Parameter surface

Đừng chỉ report best parameter.

Plot/evaluate neighborhood:

```text
lookback 20, 30, 40, 50, 60
threshold range
holding-period range
```

Nếu chỉ một điểm (point / 지점) profitable, edge fragile.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **29. Multiple testing** tiếp nhận điểm tựa từ **28. Parameter surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Cỡ mẫu (sample size / 표본 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Multiple testing

Nếu kiểm thử (test / 테스트) nhiều hypotheses, threshold “significant” thông thường có thể tạo false discoveries.

Cần hiểu:

- family-wise lỗi (error / 오류);
- false discovery;
- selection độ lệch (bias / 편향);
- data-mined Sharpe.

Không nhất thiết phải dùng một kiểm thử (test / 테스트) duy nhất, nhưng phải account tìm kiếm (search / 검색) tiến trình (process / 프로세스).

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **30. Cỡ mẫu (sample size / 표본 크기)** tiếp nhận điểm tựa từ **29. Multiple testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Bootstrap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Cỡ mẫu (sample size / 표본 크기)

100 trades không luôn là 100 independent observations.

Nếu trades cluster cùng regime/day/currency factor, **effective cỡ mẫu (sample size / 표본 크기)** thấp hơn.

Autocorrelation và overlap làm confidence interval rộng hơn tưởng tượng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **31. Bootstrap** tiếp nhận điểm tựa từ **30. Cỡ mẫu (sample size / 표본 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Bootstrap

Bootstrap có thể estimate bất định (uncertainty / 불확실성) bằng resampling, nhưng thời gian (time / 시간) series cần khối (block / 블록)/bootstrap methods nếu observations dependent.

Naive iid shuffle có thể phá dependence cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **32. Monte Carlo** tiếp nhận điểm tựa từ **31. Bootstrap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Monte Carlo

Monte Carlo có thể stress:

- trade chuỗi (sequence / 시퀀스);
- slippage variation;
- parameter bất định (uncertainty / 불확실성);
- regime frequencies.

Nó không cứu dataset biased hoặc mô hình (model / 모델) misspecified.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **33. Metrics** tiếp nhận điểm tựa từ **32. Monte Carlo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Drawdown bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Metrics

Không chỉ Sharpe.

Theo dõi:

```text
CAGR / total return
volatility
max drawdown
Calmar
Sharpe / Sortino
profit factor
expectancy
skew / tail loss
turnover
exposure
average holding period
cost share
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **34. Drawdown bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **33. Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Chi phí (cost / 비용) sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Drawdown bất định (uncertainty / 불확실성)

Observed max drawdown chỉ là một đường dẫn (path / 경로). Future đường dẫn (path / 경로) có thể worse.

Monte Carlo/bootstrap giúp estimate drawdown phân phối (distribution / 분포) nhưng vẫn phụ thuộc các giả định (assumptions / 가정들).

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **35. Chi phí (cost / 비용) sensitivity** tiếp nhận điểm tựa từ **34. Drawdown bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Parameter sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Chi phí (cost / 비용) sensitivity

Report ít nhất:

```text
Base cost
1.5× cost
2× cost
stress-event cost
```

Chiến lược (strategy / 전략) chết ngay khi spread tăng nhẹ là fragile.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **36. Parameter sensitivity** tiếp nhận điểm tựa từ **35. Chi phí (cost / 비용) sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Regime attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Parameter sensitivity

Tương tự:

```text
Base parameters
nearby values
slower/faster variants
```

Robustness quan trọng hơn tối ưu hóa (optimization / 최적화) peak.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **37. Regime attribution** tiếp nhận điểm tựa từ **36. Parameter sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Pair contribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Regime attribution

Break hiệu năng (performance / 성능) by:

- volatility regime;
- trend/phạm vi (range / 범위);
- chính sách (policy / 정책) divergence;
- crisis/normal;
- session;
- pair;
- decade/subperiod.

Một aggregate Sharpe có thể che chiến lược (strategy / 전략) kiếm toàn bộ profit trong một giai đoạn ngắn.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **38. Pair contribution** tiếp nhận điểm tựa từ **37. Regime attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Carry vs spot attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Pair contribution

Nếu multi-pair chiến lược (strategy / 전략), report contribution per pair và per underlying currency factor.

Có thể “diversified 10 pairs” nhưng 80% P/L đến từ USD trend trong một era.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **39. Carry vs spot attribution** tiếp nhận điểm tựa từ **38. Pair contribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Backtest-to-live gap** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Carry vs spot attribution

Tách:

```text
Spot P/L
Carry
Costs
```

để biết tín hiệu (signal / 신호) thực sự kiếm tiền từ đâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **40. Backtest-to-live gap** tiếp nhận điểm tựa từ **39. Carry vs spot attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Paper trading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Backtest-to-live gap

Paper/live differences:

- độ trễ (latency / 지연 시간);
- spread;
- rejected orders;
- nền tảng (platform / 플랫폼) outages;
- financing;
- emotional/manual overrides;
- dữ liệu (data / 데이터) revisions;
- broker đặc tả hợp đồng (contract / 계약) changes.

Forward kiểm thử (test / 테스트) là phase bắt buộc trước scaling material capital.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **41. Paper trading** tiếp nhận điểm tựa từ **40. Backtest-to-live gap** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Small-live forward kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Paper trading

Paper trading kiểm thử (test / 테스트):

- tín hiệu (signal / 신호) generation;
- operational chuỗi xử lý (pipeline / 파이프라인);
- position accounting.

Nhưng không reproduce fully:

- real slippage;
- liquidity;
- psychological pressure.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **42. Small-live forward kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **41. Paper trading** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Research reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Small-live forward kiểm thử (test / 테스트)

Mục tiêu:

```text
validate execution assumptions
validate statements/financing
measure live slippage
find operational bugs
```

Không phải maximize profit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **43. Research reproducibility** tiếp nhận điểm tựa từ **42. Small-live forward kiểm thử (test / 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Dữ liệu (data / 데이터) lineage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Research reproducibility

Mỗi experiment nên lưu:

```text
code version
config
input dataset version
run timestamp
universe
parameters
metrics
plots/results
```

Nếu không reproduce được backtest cũ, research tiến trình (process / 프로세스) chưa đủ đáng tin.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **43. Research reproducibility** nêu điều cần giải thích; **44. Dữ liệu (data / 데이터) lineage** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **45. Missing dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Dữ liệu (data / 데이터) lineage

Biết mỗi trường dữ liệu (field / 필드) đến từ đâu:

```text
Vendor/source
Timezone
Revision policy
Cleaning steps
Missing-value handling
```

Không có dữ liệu (data / 데이터) lineage thì bug khó kiểm tra (audit / 감사).

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **44. Dữ liệu (data / 데이터) lineage** nêu điều cần giải thích; **45. Missing dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **46. Outliers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Missing dữ liệu (data / 데이터)

Không forward-fill mọi thứ máy móc.

Forward-fill chính sách (policy / 정책) tỷ lệ (rate / 비율) có thể hợp giữa meetings; forward-fill price qua thị trường (market / 시장) outage có thể tạo fake tradability.

Handling phải theo ngữ nghĩa (semantic / 의미적) của trường dữ liệu (field / 필드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **45. Missing dữ liệu (data / 데이터)** nêu điều cần giải thích; **46. Outliers** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **47. Delisting/regime transitions equivalent trong FX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Outliers

Bad tick và true thị trường (market / 시장) jump có thể giống nhau.

Nếu filter mọi extreme return, có thể xóa chính tail rủi ro (risk / 위험) chiến lược (strategy / 전략) phải chịu.

Outlier cleaning cần cross-source/ngữ cảnh (context / 맥락) kiểm tra hợp lệ (validation / 검증) nếu possible.

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **47. Delisting/regime transitions equivalent trong FX** tiếp nhận điểm tựa từ **46. Outliers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. A minimal backtest kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Delisting/regime transitions equivalent trong FX

Currency conversion, peg break hoặc capital điều khiển (control / 제어) sự kiện (event / 이벤트) cần tường minh (explicit / 명시적) handling.

Không silently stitch incompatible price series.

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **48. A minimal backtest kiểm tra (audit / 감사)** tiếp nhận điểm tựa từ **47. Delisting/regime transitions equivalent trong FX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Khi nào backtest không đủ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. A minimal backtest kiểm tra (audit / 감사)

Trước khi tin kết quả (result / 결과), hỏi:

```text
1. Was every input known at decision time?
2. Is execution after signal formation?
3. Are bid/ask and costs modeled?
4. Is financing modeled?
5. Are timestamps/timezones correct?
6. Is margin/leverage realistic?
7. Was model selected using future/test data?
8. How many variants were tried?
9. Is result stable across parameters/regimes?
10. Can the run be reproduced?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **49. Khi nào backtest không đủ?** tiếp nhận điểm tựa từ **48. A minimal backtest kiểm tra (audit / 감사)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Handoff sang portfolio rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Khi nào backtest không đủ?

Nếu edge phụ thuộc:

- thị trường (market / 시장) độ sâu (depth / 깊이);
- hàng đợi (queue / 큐) priority;
- ultra-fast sự kiện (event / 이벤트) thực thi (execution / 실행);
- discretionary interpretation;

OHLC backtest có thể fundamentally inadequate.

Cần richer dữ liệu (data / 데이터) hoặc chấp nhận rằng chiến lược (strategy / 전략) không thể được validated theo cùng tiêu chuẩn (standard / 표준).

> **Chuyển mạch:** Trong **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **50. Handoff sang portfolio rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **49. Khi nào backtest không đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội bộ (internal / 내부) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Handoff sang portfolio rủi ro (risk / 위험)

Backtest một chiến lược (strategy / 전략) đơn lẻ chưa trả lời:

- nhiều strategies tương tác ra sao;
- currency factors overlap thế nào;
- correlation thay đổi trong stress;
- rủi ro (risk / 위험) ngân sách (budget / 예산) phân bổ thế nào.

→ [11 — Portfolio FX risk, correlation and factor exposure](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Chuyển mạch:** Ở chặng này của **10 — Backtesting và point-in-time FX dữ liệu (data / 데이터)**, **Nội bộ (internal / 내부) links** tiếp nhận điểm tựa từ **50. Handoff sang portfolio rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nội bộ (internal / 내부) links

- [Systematic Risk, Backtest and Execution](../02_SYSTEMATIC_RISK_BACKTEST_EXECUTION.md)
- [Strategy Research, Robustness and Portfolio of Strategies](../04_STRATEGY_RESEARCH_ROBUSTNESS_AND_PORTFOLIO_OF_STRATEGIES.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [09 — FX strategy families](./09_CARRY_MOMENTUM_VALUE_AND_MACRO_FX_STRATEGIES.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
