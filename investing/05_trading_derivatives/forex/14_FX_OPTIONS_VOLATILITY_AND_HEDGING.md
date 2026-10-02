# 14 — FX options, volatility và hedging

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **14 — FX options, volatility và hedging**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Lời gọi (call / 호출) và put** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. FX option có hai currencies** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối FX options với volatility, Greeks và hedging, để định giá rủi ro phi tuyến thay vì chỉ nhìn hướng tỷ giá.

FX options thêm một chiều mới vào trading: payoff không còn chỉ phụ thuộc hướng spot mà còn phụ thuộc **implied volatility, thời gian (time / 시간), rates và convexity**. Vì vậy đúng hướng spot vẫn có thể lỗ nếu option premium, timing hoặc volatility view sai.

Mô hình tư duy (mental model / 사고 모델):

```text
Spot / forward state
+ strike
+ maturity
+ implied volatility
+ rates / carry
→ option value
→ Greeks
→ hedge behavior
→ P/L path
```

## 1. Lời gọi (call / 호출) và put

Một lời gọi (call / 호출) cho quyền mua underlying theo strike `K`.

Một put cho quyền bán.

Payoff tại expiry:

```text
Call = max(S_T - K, 0)
Put  = max(K - S_T, 0)
```

Nhưng trước expiry, option giá trị (value / 값) còn chứa thời gian (time / 시간) giá trị (value / 값).

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **2. FX option có hai currencies** tiếp nhận điểm tựa từ **1. Lời gọi (call / 호출) và put** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Spot, forward và option** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. FX option có hai currencies

Trong FX, underlying là tỷ giá giữa hai currencies. Rates của cả hai phía ảnh hưởng forward và option valuation.

Không nên bản sao (copy / 복사) intuition equity option mà bỏ qua domestic/foreign-rate cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **3. Spot, forward và option** tiếp nhận điểm tựa từ **2. FX option có hai currencies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Spot, forward và option

Option thường được định giá relative to forward dynamics.

Simplified:

```text
Spot
+ interest-rate differential
→ forward
+ volatility / strike / time
→ option value
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)** tiếp nhận điểm tựa từ **3. Spot, forward và option** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Implied volatility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)

Option premium gồm:

```text
intrinsic value
+ time value
```

Out-of-the-money option có intrinsic 0 nhưng vẫn có thời gian (time / 시간) giá trị (value / 값) nếu còn khả năng finish in-the-money.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **5. Implied volatility** tiếp nhận điểm tựa từ **4. Intrinsic và thời gian (time / 시간) giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Realized volatility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Implied volatility

**Implied volatility (IV)** là volatility parameter khiến pricing mô hình (model / 모델) match thị trường (market / 시장) option price.

Nó không phải trực tiếp “dự báo chính xác volatility tương lai”. Nó phản ánh:

- expected movement;
- rủi ro (risk / 위험) premium;
- supply/demand;
- hedging pressure;
- mô hình (model / 모델) convention.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **6. Realized volatility** tiếp nhận điểm tựa từ **5. Implied volatility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Realized volatility

Realized volatility đo movement đã xảy ra.

Volatility trading thường quan tâm relationship:

```text
Implied Vol
vs
Future Realized Vol
```

Nhưng option P/L còn phụ thuộc đường dẫn (path / 경로), skew, giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và hedging.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **7. Delta** tiếp nhận điểm tựa từ **6. Realized volatility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Gamma** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Delta

Delta xấp xỉ sensitivity option giá trị (value / 값) với small spot move.

```text
Delta ≈ ∂V/∂S
```

Lời gọi (call / 호출) delta thường positive, put delta negative theo convention phổ biến.

Delta thay đổi theo spot/thời gian (time / 시간)/volatility.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **8. Gamma** tiếp nhận điểm tựa từ **7. Delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Theta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Gamma

Gamma đo thay đổi (change / 변경) của delta theo spot:

```text
Gamma = ∂²V/∂S²
```

Long option thường long gamma: delta thay đổi theo hướng có lợi cho convexity, nhưng buyer trả theta/premium cho đặc tính đó.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **9. Theta** tiếp nhận điểm tựa từ **8. Gamma** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Vega** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Theta

Theta đo thời gian (time / 시간) decay, all else equal.

Long option thường chịu negative theta.

Nhưng realized P/L không chỉ là “mỗi ngày mất theta”; spot/vol/hedging moves có thể offset.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **10. Vega** tiếp nhận điểm tựa từ **9. Theta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Rho / tỷ lệ (rate / 비율) sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Vega

Vega đo sensitivity với implied volatility.

Long option thường positive vega.

Nếu IV giảm mạnh sau sự kiện (event / 이벤트), option buyer có thể lỗ dù spot direction đúng nhẹ.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **11. Rho / tỷ lệ (rate / 비율) sensitivity** tiếp nhận điểm tựa từ **10. Vega** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Delta-neutral không risk-neutral** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Rho / tỷ lệ (rate / 비율) sensitivity

FX options phụ thuộc tỷ lệ (rate / 비율) differential, nên sensitivity với rates relevant hơn simple equity-option intuition trong một số maturities.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **12. Delta-neutral không risk-neutral** tiếp nhận điểm tựa từ **11. Rho / tỷ lệ (rate / 비율) sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Gamma scalping intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Delta-neutral không risk-neutral

Một portfolio delta ≈ 0 vẫn có:

- gamma;
- vega;
- theta;
- skew;
- jump rủi ro (risk / 위험);
- liquidity rủi ro (risk / 위험).

Neutralizing first-order direction không xóa nonlinear rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **13. Gamma scalping intuition** tiếp nhận điểm tựa từ **12. Delta-neutral không risk-neutral** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Volatility surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Gamma scalping intuition

Long gamma trader có thể rebalance delta:

```text
price rises → sell some underlying
price falls → buy some underlying
```

Nếu realized movement đủ lớn relative to option premium/chi phí (cost / 비용), rehedging can monetize convexity.

Nhưng giao dịch (transaction / 트랜잭션) chi phí (cost / 비용) và discrete jumps matter.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **14. Volatility surface** tiếp nhận điểm tựa từ **13. Gamma scalping intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Smile / skew** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Volatility surface

IV không chỉ là một số. Nó thay đổi theo:

```text
maturity
strike / delta
```

Collection này là volatility surface.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **15. Smile / skew** tiếp nhận điểm tựa từ **14. Volatility surface** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Rủi ro (risk / 위험) reversal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Smile / skew

Different strikes can trade at different IV.

FX thị trường (market / 시장) thường quote skew via conventions như rủi ro (risk / 위험) reversals/butterflies.

Skew phản ánh asymmetric demand/rủi ro (risk / 위험) perceptions, không chỉ statistical phân phối (distribution / 분포).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **16. Rủi ro (risk / 위험) reversal** tiếp nhận điểm tựa từ **15. Smile / skew** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Butterfly** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Rủi ro (risk / 위험) reversal

Conceptually, rủi ro (risk / 위험) reversal compares IV of out-of-the-money lời gọi (call / 호출) vs put at matched delta convention.

It gives thông tin (information / 정보) about relative demand for upside vs downside protection.

Chính xác (exact / 정확한) quoting conventions depend on pair/thị trường (market / 시장).

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **17. Butterfly** tiếp nhận điểm tựa từ **16. Rủi ro (risk / 위험) reversal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Delta conventions in FX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Butterfly

Butterfly quote captures curvature/smile relative to ATM and wings.

It helps construct surface, not a directional spot tín hiệu (signal / 신호) by itself.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **18. Delta conventions in FX** tiếp nhận điểm tựa từ **17. Butterfly** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. ATM conventions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Delta conventions in FX

FX options have market-specific delta conventions, including spot/forward delta and premium-adjusted variants depending on pair/thị trường (market / 시장).

Never assume a quoted “25-delta option” has one universal formula without checking convention.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **19. ATM conventions** tiếp nhận điểm tựa từ **18. Delta conventions in FX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Straddle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. ATM conventions

ATM can mean different things:

- spot ATM;
- forward ATM;
- delta-neutral straddle conventions.

Thị trường (market / 시장) documentation matters.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **20. Straddle** tiếp nhận điểm tựa từ **19. ATM conventions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Strangle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Straddle

Long straddle:

```text
long call + long put
same strike/maturity
```

It is primarily a long-volatility/large-move cấu trúc (structure / 구조), not simply “bet price goes up or down”.

Break-even depends on premium and final move.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **21. Strangle** tiếp nhận điểm tựa từ **20. Straddle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Rủi ro (risk / 위험) reversal trade** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Strangle

Long OTM lời gọi (call / 호출) + OTM put.

Cheaper than comparable straddle but requires larger move to profit at expiry.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **22. Rủi ro (risk / 위험) reversal trade** tiếp nhận điểm tựa từ **21. Strangle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Butterfly structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Rủi ro (risk / 위험) reversal trade

Buy lời gọi (call / 호출)/sell put or opposite creates directional + skew exposure.

It is not pure direction because option vols and convexity differ.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **23. Butterfly structures** tiếp nhận điểm tựa từ **22. Rủi ro (risk / 위험) reversal trade** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Sự kiện (event / 이벤트) volatility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Butterfly structures

Can express view on phân phối (distribution / 분포) around central region vs tails.

Payoff shape must be understood exactly before using labels.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **24. Sự kiện (event / 이벤트) volatility** tiếp nhận điểm tựa từ **23. Butterfly structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Implied move** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Sự kiện (event / 이벤트) volatility

Before CPI/FOMC/election-like or major chính sách (policy / 정책) sự kiện (event / 이벤트), option IV may rise.

After sự kiện (event / 이벤트) bất định (uncertainty / 불확실성) resolves, IV can collapse.

This is **vol crush** intuition.

A trader long options needs spot movement/vol dynamics sufficient to offset premium decay.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **25. Implied move** tiếp nhận điểm tựa từ **24. Sự kiện (event / 이벤트) volatility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Volatility rủi ro (risk / 위험) premium** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Implied move

Traders sometimes translate short-dated option premium into approximate market-implied move.

This is heuristic/model-dependent, not hard hỗ trợ (support / 지원)/resistance.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **26. Volatility rủi ro (risk / 위험) premium** tiếp nhận điểm tựa từ **25. Implied move** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Jump rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Volatility rủi ro (risk / 위험) premium

Option sellers may earn premium because implied volatility can exceed subsequently realized volatility on average in some samples, but compensation comes with convex tail/jump rủi ro (risk / 위험).

“Short vol earns theta” is incomplete without crash exposure.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **27. Jump rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **26. Volatility rủi ro (risk / 위험) premium** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Gap and liquidity rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Jump rủi ro (risk / 위험)

Discrete chính sách (policy / 정책)/geopolitical events can move spot beyond continuous-model các giả định (assumptions / 가정들).

Delta hedging cannot eliminate jump rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **28. Gap and liquidity rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **27. Jump rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Vol-of-vol** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Gap and liquidity rủi ro (risk / 위험)

During stress:

- IV spikes;
- spreads widen;
- hedges slip;
- correlations thay đổi (change / 변경).

Option portfolio marks may move even if theoretical mô hình (model / 모델) inputs seem manageable.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **29. Vol-of-vol** tiếp nhận điểm tựa từ **28. Gap and liquidity rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Vanna / volga intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Vol-of-vol

Implied volatility itself moves. Vol-of-vol matters for longer-dated/exotic exposure and surface dynamics.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **30. Vanna / volga intuition** tiếp nhận điểm tựa từ **29. Vol-of-vol** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Barrier options** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Vanna / volga intuition

Higher-order Greeks describe interactions between spot and vol or curvature with vol.

They become important when portfolio is large/complex; beginner should first master delta/gamma/theta/vega.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **31. Barrier options** tiếp nhận điểm tựa từ **30. Vanna / volga intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Digital options** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Barrier options

Barrier option activates/deactivates when spot touches mức (level / 수준).

Near barrier, hedging hành vi (behavior / 동작) can become nonlinear and path-dependent.

Retail structured products can embed barrier-like risks without obvious “option” label.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **32. Digital options** tiếp nhận điểm tựa từ **31. Barrier options** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Exotic FX options** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Digital options

Pay fixed amount conditional on threshold sự kiện (event / 이벤트).

Payoff discontinuity creates concentrated rủi ro (risk / 위험) near strike/expiry.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **33. Exotic FX options** tiếp nhận điểm tựa từ **32. Digital options** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Hedging corporate FX exposure with options** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Exotic FX options

Examples include:

- barriers;
- digitals;
- Asians;
- lookbacks;
- accumulators/structured variants.

Độ phức tạp (complexity / 복잡도) adds mô hình (model / 모델), liquidity and legal-product rủi ro (risk / 위험).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **34. Hedging corporate FX exposure with options** tiếp nhận điểm tựa từ **33. Exotic FX options** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Forward vs option hedge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Hedging corporate FX exposure with options

Options can protect adverse move while preserving upside.

Example conceptual:

```text
Importer needs USD later
→ buy USD call / local-currency put
```

Premium is tường minh (explicit / 명시적) insurance chi phí (cost / 비용).

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **35. Forward vs option hedge** tiếp nhận điểm tựa từ **34. Hedging corporate FX exposure with options** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Collar** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Forward vs option hedge

Forward:

```text
lock rate
low/no upfront premium often
but give up favorable move
```

Option:

```text
pay premium
protect adverse tail
retain favorable move subject to structure
```

Choice depends on mục tiêu (objective / 목표)/chi phí (cost / 비용)/accounting/liquidity.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **36. Collar** tiếp nhận điểm tựa từ **35. Forward vs option hedge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Hedge ratio and delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Collar

Collar can reduce option premium by buying protection and selling upside beyond another mức (level / 수준).

But sold option creates obligation/cap on favorable kết quả (outcome / 결과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **37. Hedge ratio and delta** tiếp nhận điểm tựa từ **36. Collar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Hedge ratio and delta

Option hedge notional should consider delta, which changes over thời gian (time / 시간).

A static “same notional” hedge may not remain equivalent.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)** tiếp nhận điểm tựa từ **37. Hedge ratio and delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Surface marking rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Động (dynamic / 동적) hedging chi phí (cost / 비용)

Frequent delta rebalancing incurs:

- spread;
- slippage;
- thị trường (market / 시장) impact.

Theoretical continuous hedge is impossible in real thị trường (market / 시장).

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **39. Surface marking rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **38. Động (dynamic / 동적) hedging chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Options backtest difficulty** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Surface marking rủi ro (risk / 위험)

P/L attribution should separate:

```text
spot delta
volatility
skew/surface movement
time decay
rates
hedging cost
```

Without attribution, option hiệu năng (performance / 성능) is opaque.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **40. Options backtest difficulty** tiếp nhận điểm tựa từ **39. Surface marking rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Stale/missing quotes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Options backtest difficulty

Need historical:

- full option chuỗi (chain / 사슬)/surface;
- bid/ask;
- conventions;
- expiries;
- rates/forwards;
- realistic hedging.

Backtesting options from spot OHLC + hiện tại (current / 현재) IV giả định (assumption / 가정) is usually inadequate.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **41. Stale/missing quotes** tiếp nhận điểm tựa từ **40. Options backtest difficulty** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Greeks are cục bộ (local / 로컬) approximations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Stale/missing quotes

OTC option datasets may be indicative, sparse or interpolation-heavy.

Research must know whether quotes are executable, composite or model-derived.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **42. Greeks are cục bộ (local / 로컬) approximations** tiếp nhận điểm tựa từ **41. Stale/missing quotes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Greeks are cục bộ (local / 로컬) approximations

Delta/gamma Taylor approximation works for small moves.

Large jump changes Greeks themselves; full revaluation needed.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)** tiếp nhận điểm tựa từ **42. Greeks are cục bộ (local / 로컬) approximations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Tail hedge chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)

Option book should shock:

```text
spot ±X%
IV ±Y vols
skew shift
time passage
rate shift
liquidity spread widening
```

Not just delta move.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **44. Tail hedge chi phí (cost / 비용)** tiếp nhận điểm tựa từ **43. Kiểm thử sức chịu tải (stress test / 스트레스 테스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Selling options and margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Tail hedge chi phí (cost / 비용)

Buying protection repeatedly can drag return.

Evaluate:

```text
premium paid
crisis payoff
carry drag
roll timing
basis to risk being hedged
```

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **45. Selling options and margin** tiếp nhận điểm tựa từ **44. Tail hedge chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Selling options and margin

Short option has potentially large nonlinear mất mát (loss / 손실) and margin requirements can rise sharply as thị trường (market / 시장) moves/volatility rises.

Margin stress must be modeled before premium income.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **45. Selling options and margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Do not infer xác suất (probability / 확률) directly from delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)

If using retail OTC products, legal thực thể (entity / 엔터티), settlement and pricing transparency are part of rủi ro (risk / 위험) mô hình (model / 모델) just as with spot/CFD.

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **47. Do not infer xác suất (probability / 확률) directly from delta** tiếp nhận điểm tựa từ **46. Broker OTC option/sản phẩm (product / 제품) rủi ro (risk / 위험)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. Risk-neutral vs real-world xác suất (probability / 확률)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Do not infer xác suất (probability / 확률) directly from delta

Option delta is sometimes loosely interpreted as probability-like. Under specific các mô hình (models / 모델들)/conventions it relates to risk-neutral measures, but it is not a simple real-world xác suất (probability / 확률) of expiring ITM.

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **48. Risk-neutral vs real-world xác suất (probability / 확률)** tiếp nhận điểm tựa từ **47. Do not infer xác suất (probability / 확률) directly from delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Minimal option position sheet** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Risk-neutral vs real-world xác suất (probability / 확률)

Option prices encode risk-neutral valuation plus rủi ro (risk / 위험) premia, not pure vật lý (physical / 물리적) xác suất (probability / 확률) forecast.

This distinction matters when using options thị trường (market / 시장) as macro expectation indicator.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **49. Minimal option position sheet** tiếp nhận điểm tựa từ **48. Risk-neutral vs real-world xác suất (probability / 확률)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. Checklist** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Minimal option position sheet

```text
Pair
Structure
Notional
Expiry
Strike(s)
Premium
Delta
Gamma
Theta
Vega
IV / skew context
Spot/forward
Max loss / nonlinear tail
Liquidity
Hedge plan
Event exposure
```

> **Chuyển mạch:** Trong **14 — FX options, volatility và hedging**, **50. Checklist** tiếp nhận điểm tựa từ **49. Minimal option position sheet** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đọc tiếp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. Checklist

Bạn cần tự giải thích được:

1. Option P/L depends on more than spot direction.
2. IV vs realized volatility.
3. Delta/gamma/theta/vega.
4. Why delta-neutral is not risk-neutral.
5. Surface/skew/risk-reversal concepts.
6. Sự kiện (event / 이벤트) vol and vol crush.
7. Forward vs option hedge sự đánh đổi (trade-off / 트레이드오프).
8. Động (dynamic / 동적) hedging costs/jump rủi ro (risk / 위험).
9. Why option backtesting needs surface dữ liệu (data / 데이터).
10. Why short-vol premium income carries tail rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **14 — FX options, volatility và hedging**, **Đọc tiếp** tiếp nhận điểm tựa từ **50. Checklist** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nội bộ (internal / 내부) links** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đọc tiếp

→ [15 — Korea / Vietnam FX market context and regulations](./15_KOREA_VIETNAM_FX_MARKET_CONTEXT_AND_REGULATIONS.md)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **14 — FX options, volatility và hedging**, **Nội bộ (internal / 내부) links** tiếp nhận điểm tựa từ **Đọc tiếp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nội bộ (internal / 내부) links

- [Options, Volatility Surface, Greeks and Hedging](../05_OPTIONS_VOLATILITY_SURFACE_GREEKS_AND_HEDGING.md)
- [04 — Macro drivers](./04_MACRO_DRIVERS_RATES_CARRY_AND_SESSIONS.md)
- [11 — Portfolio FX risk](./11_PORTFOLIO_FX_RISK_CORRELATION_AND_FACTOR_EXPOSURE.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
