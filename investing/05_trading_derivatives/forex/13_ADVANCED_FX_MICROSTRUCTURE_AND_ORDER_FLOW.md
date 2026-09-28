# 13 — Advanced FX microstructure và thứ tự (order / 순서) luồng (flow / 흐름)

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

## 2. FX thứ tự (order / 순서) luồng (flow / 흐름) khó quan sát toàn bộ

OTC FX phân mảnh. Không có một toàn cục (global / 전역) tape chứa tất cả transactions.

Dữ liệu có thể đến từ:

- specific dealer;
- ECN/venue;
- futures exchange;
- broker clients;
- aggregated institutional nguồn (source / 소스).

Mỗi nguồn (source / 소스) chỉ quan sát một phần thị trường (market / 시장).

## 3. Dealer inventory

Dealer nhận máy khách (client / 클라이언트) luồng (flow / 흐름) có thể tạm thời tích lũy inventory.

Nếu inventory quá lệch, dealer có thể:

- adjust quote;
- hedge externally;
- internalize với opposite máy khách (client / 클라이언트) luồng (flow / 흐름).

Price thay đổi (change / 변경) ngắn hạn có thể phản ánh inventory management chứ không chỉ công khai (public / 공개) news.

## 4. Adverse selection

Liquidity provider sợ giao dịch với counterparty có thông tin (information / 정보) advantage.

Khi perceived adverse-selection rủi ro (risk / 위험) tăng:

```text
spread widens
quoted size shrinks
last-look rejection may rise depending on protocol
```

News windows là ví dụ rõ.

## 5. Spread decomposition

Conceptually spread bù cho:

- inventory rủi ro (risk / 위험);
- adverse selection;
- operating/technology chi phí (cost / 비용);
- capital/funding;
- expected profit.

Relative importance thay đổi theo venue/regime.

## 6. Price discovery

Price discovery là tiến trình (process / 프로세스) thị trường (market / 시장) incorporates thông tin (information / 정보) vào quotes/trades.

Trong FX, discovery có thể diễn ra across:

- interdealer spot venues;
- dealer-client platforms;
- futures;
- options;
- rates markets.

Một venue có thể lead ở một horizon nhưng không mọi lúc.

## 7. Fragmentation

Cùng currency pair có nhiều liquidity pools.

Arbitrage/thị trường (market / 시장) making giữ prices gần nhau nhưng độ trễ (latency / 지연 시간) và venue rules tạo temporary differences.

Do đó “thị trường (market / 시장) price” thường là constructed tham chiếu (reference / 참조) từ multiple quotes.

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

## 9. Thị trường (market / 시장) resilience

Sau large thứ tự (order / 순서), liquidity có quay lại nhanh không?

Resilience là dimension khác của liquidity bên cạnh spread/độ sâu (depth / 깊이).

## 10. Impact

Large aggressive thứ tự (order / 순서) có thể move price.

Temporary impact có thể mean-revert; permanent thành phần (component / 컴포넌트) có thể reflect thông tin (information / 정보).

Tách hai phần là thực thi (execution / 실행)/research bài toán (problem / 문제) khó.

## 11. Square-root-like impact intuition

Nhiều markets cho thấy impact tăng sublinearly với kích thước (size / 크기) trong empirical research, nhưng không nên hard-code universal law cho mọi FX venue/regime.

Need instrument/venue-specific calibration.

## 12. Internalization

Dealer có thể match opposite máy khách (client / 클라이언트) flows internally thay vì hedge mọi trade ra street.

Điều này giảm bên ngoài (external / 외부) footprint nhưng tạo inventory/xung đột (conflict / 충돌) considerations.

Internalization ratio có thể ảnh hưởng thực thi (execution / 실행) hành vi (behavior / 동작) nhưng dữ liệu (data / 데이터) không phải luôn công khai (public / 공개).

## 13. Last look

Một số FX electronic protocols cho liquidity provider short acceptance cửa sổ (window / 윈도우) sau yêu cầu (request / 요청)/trade attempt.

Purpose có thể liên quan stale-price/độ trễ (latency / 지연 시간) rủi ro (risk / 위험); máy khách (client / 클라이언트) perspective quan tâm rejection/asymmetric thực thi (execution / 실행).

Khi đánh giá, cần empirical stats và giao thức (protocol / 프로토콜) disclosure, không chỉ label.

## 14. Request-for-stream / request-for-quote

Institutional clients có thể nhận streaming prices hoặc yêu cầu (request / 요청) quote từ dealers.

Thực thi (execution / 실행) choice depends on:

- kích thước (size / 크기);
- thông tin (information / 정보) leakage;
- urgency;
- relationship;
- expected impact.

## 15. Thông tin (information / 정보) leakage

Large thứ tự (order / 순서) bị lộ có thể làm thị trường (market / 시장) move trước completion.

Thực thi (execution / 실행) algorithms cố balance:

```text
urgency
vs
market impact / information leakage
```

## 16. TWAP/VWAP/POV concepts

### TWAP
Spread thứ tự (order / 순서) across thời gian (time / 시간).

### VWAP
Mục tiêu (target / 대상) volume-weighted benchmark where meaningful volume dữ liệu (data / 데이터) exists.

### POV
Trade as fraction of observed thị trường (market / 시장) volume.

Trong OTC FX, benchmark/dữ liệu (data / 데이터) nguồn (source / 소스) phải được định nghĩa cẩn thận.

## 17. Hiện thực (implementation / 구현) shortfall thuật toán (algorithm / 알고리즘)

Optimize sự đánh đổi (trade-off / 트레이드오프):

```text
waiting risk
vs
immediate market impact
```

High urgency → execute faster, accept impact.
Low urgency → wait, accept price rủi ro (risk / 위험).

## 18. Fixing benchmark thực thi (execution / 실행)

WM/R-like fixing windows và institutional benchmarks có thể concentrate orders.

Participants hedging benchmark rủi ro (risk / 위험) can create predictable activity, nhưng exploitability after chi phí (cost / 비용)/crowding không được assumed.

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

## 21. Order-book imbalance

Trong centralized/visible venue:

```text
Imbalance = (Bid Depth - Ask Depth) / (Bid Depth + Ask Depth)
```

có thể be short-horizon tính năng (feature / 기능).

Nhưng FX venue book chỉ là one pool, không toàn cục (global / 전역) thị trường (market / 시장).

## 22. Futures as proxy

Currency futures cung cấp centralized order-book/volume dữ liệu (data / 데이터) và có thể dùng nghiên cứu price discovery/thứ tự (order / 순서) luồng (flow / 흐름).

Nhưng ánh xạ (mapping / 매핑) sang OTC spot cần account:

- basis;
- trading hours;
- đặc tả hợp đồng (contract / 계약) roll;
- participant mix.

## 23. COT dữ liệu (data / 데이터)

Commitments of Traders cung cấp positioning categories cho futures, thường weekly và lagged.

Useful for broad positioning ngữ cảnh (context / 맥락), không phù hợp microsecond thứ tự (order / 순서) luồng (flow / 흐름).

## 24. Dealer-client luồng (flow / 흐름) datasets

Nếu có institutional dataset, luồng (flow / 흐름) có thể predictive ở horizons khác nhau.

Nhưng mẫu (sample / 표본) representativeness là central question:

```text
Which clients?
Which regions?
Which dealer?
How much market share?
```

## 25. Toxic luồng (flow / 흐름)

Dealer gọi luồng (flow / 흐름) “toxic” khi counterparty trades systematically before adverse price moves hoặc exploits stale quotes/độ trễ (latency / 지연 시간).

Term phụ thuộc perspective và mô hình thực thi (execution model / 실행 모델), không đồng nghĩa misconduct.

## 26. Độ trễ (latency / 지연 시간) arbitrage

Nếu one venue updates faster than another, fast participant có thể trade stale quote.

Thị trường (market / 시장) makers respond bằng:

- faster hạ tầng (infrastructure / 인프라);
- wider spread;
- last look;
- quote throttling.

## 27. Co-location và speed

Ở ultra-short horizon, vật lý (physical / 물리적)/mạng (network / 네트워크) độ trễ (latency / 지연 시간) matters.

Retail internet trader không nên assume edge based on stale retail chart can compete with institutional low-latency các hệ thống (systems / 시스템들).

## 28. Session handoff

Liquidity providers/participants thay đổi (change / 변경) across Asia–Europe–US.

Spread/độ sâu (depth / 깊이) and price discovery hành vi (behavior / 동작) vary by cục bộ (local / 로컬) nghiệp vụ (business / 비즈니스) hours and overlap.

## 29. Rollover cửa sổ (window / 윈도우)

Retail platforms may show poor liquidity/spread around daily rollover. Chính xác (exact / 정확한) timing/sản phẩm (product / 제품) hành vi (behavior / 동작) broker-specific.

Short-term chiến lược (strategy / 전략) should exclude/stress this cửa sổ (window / 윈도우) rather than assume daytime spread.

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

## 31. Flash events

Phản hồi (feedback / 피드백) loops among stops, leverage, thin liquidity and algorithms can create extreme short-lived moves.

Rủi ro (risk / 위험) controls need:

- max slippage các giả định (assumptions / 가정들);
- price sanity checks;
- kill switch;
- leverage headroom.

## 32. Quote stuffing / manipulation claims

Specific manipulative practices require bằng chứng (evidence / 증거) and regulatory definitions. Do not label unusual quote hành vi (behavior / 동작) as manipulation from chart alone.

Use venue/regulator bằng chứng (evidence / 증거) where available.

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

## 34. Slippage phân phối (distribution / 분포)

Average slippage can hide asymmetric tail.

Bản ghi (record / 레코드) positive and negative separately, especially stop orders.

## 35. Markout

Thực thi (execution / 실행) chất lượng (quality / 품질) can use post-trade markout:

```text
price after 1s / 10s / 1m relative to fill
```

For liquidity provider, adverse markout suggests informed/toxic luồng (flow / 흐름); for taker, it can measure thực thi (execution / 실행) timing.

## 36. TCA

Giao dịch (transaction / 트랜잭션) Chi phí (cost / 비용) Phân tích (analysis / 분석) decomposes thực thi (execution / 실행) vs benchmark.

Metrics:

- arrival price;
- hiện thực (implementation / 구현) shortfall;
- spread capture/chi phí (cost / 비용);
- delay;
- thị trường (market / 시장) impact;
- post-trade markout.

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

## 38. Microstructure alpha decays fast

Short-horizon order-flow signals often have short half-life.

If hạ tầng (infrastructure / 인프라) độ trễ (latency / 지연 시간) exceeds tín hiệu (signal / 신호) half-life, research alpha không executable.

## 39. Dữ liệu (data / 데이터) synchronization

Combining spot, futures, rates, options requires clock synchronization.

Milliseconds/seconds mismatch can reverse lead-lag suy luận (inference / 추론).

## 40. Causality caution

If futures move 50 ms before spot in mẫu (sample / 표본), that does not automatically prove futures “cause” spot fundamentally. Could reflect dùng chung (common / 공통) thông tin (information / 정보) processed at different speeds.

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

## Đọc tiếp

→ [14 — FX options, volatility and hedging](./14_FX_OPTIONS_VOLATILITY_AND_HEDGING.md)

## Nội bộ (internal / 내부) links

- [01 — Market structure and instruments](./01_MARKET_STRUCTURE_AND_INSTRUMENTS.md)
- [05 — Execution, brokers, costs and risk](./05_EXECUTION_BROKERS_COSTS_AND_RISK.md)
- [Execution, Microstructure and Trading Portfolio](../03_EXECUTION_MICROSTRUCTURE_AND_TRADING_PORTFOLIO.md)
