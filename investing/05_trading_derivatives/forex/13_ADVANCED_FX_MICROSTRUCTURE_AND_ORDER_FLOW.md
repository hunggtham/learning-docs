# 13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Thứ tự (order / 순서) luồng (flow / 흐름) khác volume** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **2. FX thứ tự (order / 순서) luồng (flow / 흐름) khó quan sát toàn bộ** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Mạch này nối FX microstructure với order flow, liquidity và price impact, để đọc tỷ giá qua cơ chế khớp lệnh và độ sâu thị trường.

Ở cấp nâng cao, FX không chỉ là chuỗi price bars mà là một mạng lưới dealer, venue, máy khách (client / 클라이언트) luồng (flow / 흐름), inventory, hedging và độ trễ (latency / 지연 시간). **Microstructure** nghiên cứu cách những cơ chế này tạo ra executable prices, spreads, liquidity và short-horizon price discovery.

Mô hình tư duy (mental model / 사고 모델):

```text
Information / client demand
→ orders and dealer inventory
→ quote adjustment
→ execution across fragmented venues
→ hedging / internalization
→ observed price path
```

## 1. Thứ tự (order / 순서) luồng (flow / 흐름) khác volume

**Thứ tự (order / 순서) luồng (flow / 흐름)** thường nhấn mạnh hướng và chuỗi (sequence / 시퀀스) của trading demand, ví dụ signed buys/sells.

Raw volume chỉ nói activity magnitude.

Hai periods có cùng volume nhưng net aggressive buying khác nhau có thể tạo price impact khác.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **1. Thứ tự (order / 순서) luồng (flow / 흐름) khác volume** đặt đầu vào cho **2. FX thứ tự (order / 순서) luồng (flow / 흐름) khó quan sát toàn bộ**, rồi **3. Dealer inventory** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. FX thứ tự (order / 순서) luồng (flow / 흐름) khó quan sát toàn bộ

OTC FX phân mảnh. Không có một toàn cục (global / 전역) tape chứa tất cả transactions.

Dữ liệu có thể đến từ:

- specific dealer;
- ECN/venue;
- futures exchange;
- broker clients;
- aggregated institutional nguồn (source / 소스).

Mỗi nguồn (source / 소스) chỉ quan sát một phần thị trường (market / 시장).

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **2. FX thứ tự (order / 순서) luồng (flow / 흐름) khó quan sát toàn bộ** đặt đầu vào cho **3. Dealer inventory**, rồi **4. Adverse selection** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Dealer inventory

Dealer nhận máy khách (client / 클라이언트) luồng (flow / 흐름) có thể tạm thời tích lũy inventory.

Nếu inventory quá lệch, dealer có thể:

- adjust quote;
- hedge externally;
- internalize với opposite máy khách (client / 클라이언트) luồng (flow / 흐름).

Price thay đổi (change / 변경) ngắn hạn có thể phản ánh inventory management chứ không chỉ công khai (public / 공개) news.

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **4. Adverse selection** nối từ **3. Dealer inventory** sang **5. Spread decomposition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Adverse selection

Liquidity provider sợ giao dịch với counterparty có thông tin (information / 정보) advantage.

Khi perceived adverse-selection rủi ro (risk / 위험) tăng:

```text
spread widens
quoted size shrinks
last-look rejection may rise depending on protocol
```

News windows là ví dụ rõ.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **5. Spread decomposition** nối từ **4. Adverse selection** sang **6. Price discovery**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Spread decomposition

Conceptually spread bù cho:

- inventory rủi ro (risk / 위험);
- adverse selection;
- operating/technology chi phí (cost / 비용);
- capital/funding;
- expected profit.

Relative importance thay đổi theo venue/regime.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **6. Price discovery** nối từ **5. Spread decomposition** sang **7. Fragmentation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Price discovery

Price discovery là tiến trình (process / 프로세스) thị trường (market / 시장) incorporates thông tin (information / 정보) vào quotes/trades.

Trong FX, discovery có thể diễn ra across:

- interdealer spot venues;
- dealer-client platforms;
- futures;
- options;
- rates markets.

Một venue có thể lead ở một horizon nhưng không mọi lúc.

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **7. Fragmentation** nối từ **6. Price discovery** sang **8. Top-of-book vs độ sâu (depth / 깊이)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Fragmentation

Cùng currency pair có nhiều liquidity pools.

Arbitrage/thị trường (market / 시장) making giữ prices gần nhau nhưng độ trễ (latency / 지연 시간) và venue rules tạo temporary differences.

Do đó “thị trường (market / 시장) price” thường là constructed tham chiếu (reference / 참조) từ multiple quotes.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **8. Top-of-book vs độ sâu (depth / 깊이)** nối từ **7. Fragmentation** sang **9. Thị trường (market / 시장) resilience**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Top-of-book vs độ sâu (depth / 깊이)

Best bid/ask chỉ là mức (level / 수준) đầu.

Institutional thực thi (execution / 실행) quan tâm:

```text
available size at best
next levels
depth shape
resiliency after trade
```

Tight spread nhưng shallow book vẫn có poor liquidity cho large orders.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **9. Thị trường (market / 시장) resilience** nối từ **8. Top-of-book vs độ sâu (depth / 깊이)** sang **10. Impact**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Thị trường (market / 시장) resilience

Sau large thứ tự (order / 순서), liquidity có quay lại nhanh không?

Resilience là dimension khác của liquidity bên cạnh spread/độ sâu (depth / 깊이).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **10. Impact** nối từ **9. Thị trường (market / 시장) resilience** sang **11. Square-root-like impact intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Impact

Large aggressive thứ tự (order / 순서) có thể move price.

Temporary impact có thể mean-revert; permanent thành phần (component / 컴포넌트) có thể reflect thông tin (information / 정보).

Tách hai phần là thực thi (execution / 실행)/research bài toán (problem / 문제) khó.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **11. Square-root-like impact intuition** nối từ **10. Impact** sang **12. Internalization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Square-root-like impact intuition

Nhiều markets cho thấy impact tăng sublinearly với kích thước (size / 크기) trong empirical research, nhưng không nên hard-code universal law cho mọi FX venue/regime.

Need instrument/venue-specific calibration.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **12. Internalization** nối từ **11. Square-root-like impact intuition** sang **13. Last look**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Internalization

Dealer có thể match opposite máy khách (client / 클라이언트) flows internally thay vì hedge mọi trade ra street.

Điều này giảm bên ngoài (external / 외부) footprint nhưng tạo inventory/xung đột (conflict / 충돌) considerations.

Internalization ratio có thể ảnh hưởng thực thi (execution / 실행) hành vi (behavior / 동작) nhưng dữ liệu (data / 데이터) không phải luôn công khai (public / 공개).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **13. Last look** nối từ **12. Internalization** sang **14. Request-for-stream / request-for-quote**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Last look

Một số FX electronic protocols cho liquidity provider short acceptance cửa sổ (window / 윈도우) sau yêu cầu (request / 요청)/trade attempt.

Purpose có thể liên quan stale-price/độ trễ (latency / 지연 시간) rủi ro (risk / 위험); máy khách (client / 클라이언트) perspective quan tâm rejection/asymmetric thực thi (execution / 실행).

Khi đánh giá, cần empirical stats và giao thức (protocol / 프로토콜) disclosure, không chỉ label.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **14. Request-for-stream / request-for-quote** nối từ **13. Last look** sang **15. Thông tin (information / 정보) leakage**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Request-for-stream / request-for-quote

Institutional clients có thể nhận streaming prices hoặc yêu cầu (request / 요청) quote từ dealers.

Thực thi (execution / 실행) choice depends on:

- kích thước (size / 크기);
- thông tin (information / 정보) leakage;
- urgency;
- relationship;
- expected impact.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **15. Thông tin (information / 정보) leakage** nối từ **14. Request-for-stream / request-for-quote** sang **16. TWAP/VWAP/POV concepts**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Thông tin (information / 정보) leakage

Large thứ tự (order / 순서) bị lộ có thể làm thị trường (market / 시장) move trước completion.

Thực thi (execution / 실행) algorithms cố balance:

```text
urgency
vs
market impact / information leakage
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **16. TWAP/VWAP/POV concepts** nối từ **15. Thông tin (information / 정보) leakage** sang **17. Hiện thực (implementation / 구현) shortfall thuật toán (algorithm / 알고리즘)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. TWAP/VWAP/POV concepts

### TWAP
Spread thứ tự (order / 순서) across thời gian (time / 시간).

### VWAP
Mục tiêu (target / 대상) volume-weighted benchmark where meaningful volume dữ liệu (data / 데이터) exists.

### POV
Trade as fraction of observed thị trường (market / 시장) volume.

Trong OTC FX, benchmark/dữ liệu (data / 데이터) nguồn (source / 소스) phải được định nghĩa cẩn thận.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **17. Hiện thực (implementation / 구현) shortfall thuật toán (algorithm / 알고리즘)** nối từ **16. TWAP/VWAP/POV concepts** sang **18. Fixing benchmark thực thi (execution / 실행)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Hiện thực (implementation / 구현) shortfall thuật toán (algorithm / 알고리즘)

Optimize sự đánh đổi (trade-off / 트레이드오프):

```text
waiting risk
vs
immediate market impact
```

High urgency → execute faster, accept impact.
Low urgency → wait, accept price rủi ro (risk / 위험).

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **18. Fixing benchmark thực thi (execution / 실행)** nối từ **17. Hiện thực (implementation / 구현) shortfall thuật toán (algorithm / 알고리즘)** sang **19. Stop clusters**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Fixing benchmark thực thi (execution / 실행)

WM/R-like fixing windows và institutional benchmarks có thể concentrate orders.

Participants hedging benchmark rủi ro (risk / 위험) can create predictable activity, nhưng exploitability after chi phí (cost / 비용)/crowding không được assumed.

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **19. Stop clusters** nối từ **18. Fixing benchmark thực thi (execution / 실행)** sang **20. Liquidity sweep terminology**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Stop clusters

Stops có thể cluster quanh:

- previous highs/lows;
- round numbers;
- technical levels.

Khi price reaches cluster:

```text
triggered market orders
→ temporary order imbalance
→ faster move
```

Đây là cơ chế (mechanism / 메커니즘) có thể giải thích acceleration mà không cần conspiracy narrative.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **20. Liquidity sweep terminology** nối từ **19. Stop clusters** sang **21. Order-book imbalance**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Liquidity sweep terminology

“Liquidity sweep” có thể map vào tiến trình (process / 프로세스):

```text
price reaches area with clustered conditional orders
→ aggressive flow increases
→ available liquidity consumed
→ price moves through level
→ continuation or reversal depends on subsequent flow
```

Term hữu ích nếu quy tắc (rule / 규칙)/dữ liệu (data / 데이터) rõ; không nên biến thành deterministic setup.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **21. Order-book imbalance** nối từ **20. Liquidity sweep terminology** sang **22. Futures as proxy**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Order-book imbalance

Trong centralized/visible venue:

```text
Imbalance = (Bid Depth - Ask Depth) / (Bid Depth + Ask Depth)
```

có thể be short-horizon tính năng (feature / 기능).

Nhưng FX venue book chỉ là one pool, không toàn cục (global / 전역) thị trường (market / 시장).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **22. Futures as proxy** nối từ **21. Order-book imbalance** sang **23. COT dữ liệu (data / 데이터)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Futures as proxy

Currency futures cung cấp centralized order-book/volume dữ liệu (data / 데이터) và có thể dùng nghiên cứu price discovery/thứ tự (order / 순서) luồng (flow / 흐름).

Nhưng ánh xạ (mapping / 매핑) sang OTC spot cần account:

- basis;
- trading hours;
- đặc tả hợp đồng (contract / 계약) roll;
- participant mix.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **22. Futures as proxy** đặt vấn đề; **23. COT dữ liệu (data / 데이터)** đối chiếu bằng chứng, rồi **24. Dealer-client luồng (flow / 흐름) datasets** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. COT dữ liệu (data / 데이터)

Commitments of Traders cung cấp positioning categories cho futures, thường weekly và lagged.

Useful for broad positioning ngữ cảnh (context / 맥락), không phù hợp microsecond thứ tự (order / 순서) luồng (flow / 흐름).

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **23. COT dữ liệu (data / 데이터)** đặt vấn đề; **24. Dealer-client luồng (flow / 흐름) datasets** đối chiếu bằng chứng, rồi **25. Toxic luồng (flow / 흐름)** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. Dealer-client luồng (flow / 흐름) datasets

Nếu có institutional dataset, luồng (flow / 흐름) có thể predictive ở horizons khác nhau.

Nhưng mẫu (sample / 표본) representativeness là central question:

```text
Which clients?
Which regions?
Which dealer?
How much market share?
```

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **24. Dealer-client luồng (flow / 흐름) datasets** đặt đầu vào cho **25. Toxic luồng (flow / 흐름)**, rồi **26. Độ trễ (latency / 지연 시간) arbitrage** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. Toxic luồng (flow / 흐름)

Dealer gọi luồng (flow / 흐름) “toxic” khi counterparty trades systematically before adverse price moves hoặc exploits stale quotes/độ trễ (latency / 지연 시간).

Term phụ thuộc perspective và mô hình thực thi (execution model / 실행 모델), không đồng nghĩa misconduct.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **25. Toxic luồng (flow / 흐름)** đặt đầu vào cho **26. Độ trễ (latency / 지연 시간) arbitrage**, rồi **27. Co-location và speed** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. Độ trễ (latency / 지연 시간) arbitrage

Nếu one venue updates faster than another, fast participant có thể trade stale quote.

Thị trường (market / 시장) makers respond bằng:

- faster hạ tầng (infrastructure / 인프라);
- wider spread;
- last look;
- quote throttling.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **27. Co-location và speed** nối từ **26. Độ trễ (latency / 지연 시간) arbitrage** sang **28. Session handoff**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Co-location và speed

Ở ultra-short horizon, vật lý (physical / 물리적)/mạng (network / 네트워크) độ trễ (latency / 지연 시간) matters.

Retail internet trader không nên assume edge based on stale retail chart can compete with institutional low-latency các hệ thống (systems / 시스템들).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **28. Session handoff** nối từ **27. Co-location và speed** sang **29. Rollover cửa sổ (window / 윈도우)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Session handoff

Liquidity providers/participants thay đổi (change / 변경) across Asia–Europe–US.

Spread/độ sâu (depth / 깊이) and price discovery hành vi (behavior / 동작) vary by cục bộ (local / 로컬) nghiệp vụ (business / 비즈니스) hours and overlap.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **29. Rollover cửa sổ (window / 윈도우)** nối từ **28. Session handoff** sang **30. News microstructure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Rollover cửa sổ (window / 윈도우)

Retail platforms may show poor liquidity/spread around daily rollover. Chính xác (exact / 정확한) timing/sản phẩm (product / 제품) hành vi (behavior / 동작) broker-specific.

Short-term chiến lược (strategy / 전략) should exclude/stress this cửa sổ (window / 윈도우) rather than assume daytime spread.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **30. News microstructure** nối từ **29. Rollover cửa sổ (window / 윈도우)** sang **31. Flash events**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. News microstructure

Near high-impact bản phát hành (release / 릴리스):

```text
quotes pulled/widened
→ depth declines
→ algorithms process headline
→ price gaps across levels
→ liquidity gradually rebuilds
```

Historical candle cannot fully reconstruct executable đường dẫn (path / 경로).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **31. Flash events** nối từ **30. News microstructure** sang **32. Quote stuffing / manipulation claims**, vì cơ chế trước tạo đầu vào cho bước sau.

## 31. Flash events

Phản hồi (feedback / 피드백) loops among stops, leverage, thin liquidity and algorithms can create extreme short-lived moves.

Rủi ro (risk / 위험) controls need:

- max slippage các giả định (assumptions / 가정들);
- price sanity checks;
- kill switch;
- leverage headroom.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **32. Quote stuffing / manipulation claims** nối từ **31. Flash events** sang **33. Spread phân phối (distribution / 분포)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 32. Quote stuffing / manipulation claims

Specific manipulative practices require bằng chứng (evidence / 증거) and regulatory definitions. Do not label unusual quote hành vi (behavior / 동작) as manipulation from chart alone.

Use venue/regulator bằng chứng (evidence / 증거) where available.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **33. Spread phân phối (distribution / 분포)** nối từ **32. Quote stuffing / manipulation claims** sang **34. Slippage phân phối (distribution / 분포)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 33. Spread phân phối (distribution / 분포)

Rather than average spread only, store phân phối (distribution / 분포):

```text
median
90th/95th/99th percentile
by session
event windows
stress periods
```

Tail spread drives stop/thực thi (execution / 실행) rủi ro (risk / 위험).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **34. Slippage phân phối (distribution / 분포)** nối từ **33. Spread phân phối (distribution / 분포)** sang **35. Markout**, vì cơ chế trước tạo đầu vào cho bước sau.

## 34. Slippage phân phối (distribution / 분포)

Average slippage can hide asymmetric tail.

Bản ghi (record / 레코드) positive and negative separately, especially stop orders.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **35. Markout** nối từ **34. Slippage phân phối (distribution / 분포)** sang **36. TCA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 35. Markout

Thực thi (execution / 실행) chất lượng (quality / 품질) can use post-trade markout:

```text
price after 1s / 10s / 1m relative to fill
```

For liquidity provider, adverse markout suggests informed/toxic luồng (flow / 흐름); for taker, it can measure thực thi (execution / 실행) timing.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **36. TCA** nối từ **35. Markout** sang **37. Retail TCA**, vì cơ chế trước tạo đầu vào cho bước sau.

## 36. TCA

Giao dịch (transaction / 트랜잭션) Chi phí (cost / 비용) Phân tích (analysis / 분석) decomposes thực thi (execution / 실행) vs benchmark.

Metrics:

- arrival price;
- hiện thực (implementation / 구현) shortfall;
- spread capture/chi phí (cost / 비용);
- delay;
- thị trường (market / 시장) impact;
- post-trade markout.

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **37. Retail TCA** nối từ **36. TCA** sang **38. Microstructure alpha decays fast**, vì cơ chế trước tạo đầu vào cho bước sau.

## 37. Retail TCA

Retail trader can still log:

```text
decision price
quoted spread
fill price
latency estimate
slippage
exit fill
```

Across many trades this reveals broker/session/sự kiện (event / 이벤트) thực thi (execution / 실행) chất lượng (quality / 품질).

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **38. Microstructure alpha decays fast** nối từ **37. Retail TCA** sang **39. Dữ liệu (data / 데이터) synchronization**, vì cơ chế trước tạo đầu vào cho bước sau.

## 38. Microstructure alpha decays fast

Short-horizon order-flow signals often have short half-life.

If hạ tầng (infrastructure / 인프라) độ trễ (latency / 지연 시간) exceeds tín hiệu (signal / 신호) half-life, research alpha không executable.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **38. Microstructure alpha decays fast** đặt vấn đề; **39. Dữ liệu (data / 데이터) synchronization** đối chiếu bằng chứng, rồi **40. Causality caution** mở rộng hệ quả hoặc giới hạn liên quan.

## 39. Dữ liệu (data / 데이터) synchronization

Combining spot, futures, rates, options requires clock synchronization.

Milliseconds/seconds mismatch can reverse lead-lag suy luận (inference / 추론).

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **39. Dữ liệu (data / 데이터) synchronization** đặt vấn đề; **40. Causality caution** đối chiếu bằng chứng, rồi **41. From microstructure to chiến lược (strategy / 전략)** mở rộng hệ quả hoặc giới hạn liên quan.

## 40. Causality caution

If futures move 50 ms before spot in mẫu (sample / 표본), that does not automatically prove futures “cause” spot fundamentally. Could reflect dùng chung (common / 공통) thông tin (information / 정보) processed at different speeds.

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **41. From microstructure to chiến lược (strategy / 전략)** nối từ **40. Causality caution** sang **42. Checklist**, vì cơ chế trước tạo đầu vào cho bước sau.

## 41. From microstructure to chiến lược (strategy / 전략)

A microstructure chiến lược (strategy / 전략) specification must include:

```text
venue/source
feature timestamp
latency
order type
fill model
size/depth
fees
rejections
market impact
```

Otherwise paper alpha can be impossible live.

> **Nối mạch:** Ở chặng này của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **42. Checklist** nối từ **41. From microstructure to chiến lược (strategy / 전략)** sang **Đọc tiếp**, vì cơ chế trước tạo đầu vào cho bước sau.

## 42. Checklist

Bạn cần tự giải thích được:

1. Thứ tự (order / 순서) luồng (flow / 흐름) vs volume.
2. Why no toàn cục (global / 전역) FX thứ tự (order / 순서) book exists.
3. Dealer inventory/adverse selection.
4. Độ sâu (depth / 깊이)/resilience vs spread.
5. Internalization/last look.
6. Stop clustering mechanics.
7. Limits of futures/order-book proxies.
8. TCA and markout.
9. Why microstructure alpha is execution-dependent.
10. Why unusual price hành vi (behavior / 동작) is not proof of manipulation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **Đọc tiếp** nối từ **42. Checklist** sang **Nội bộ (internal / 내부) links**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đọc tiếp

→ [14 — FX options, volatility and hedging](./14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

> **Nối mạch:** Trong **13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)**, **Nội bộ (internal / 내부) links** nối từ **Đọc tiếp** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Nội bộ (internal / 내부) links

- [01 — Market structure and instruments](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)

> **Bàn giao:** Sau **Nội bộ (internal / 내부) links**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
