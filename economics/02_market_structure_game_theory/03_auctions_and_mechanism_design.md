# Auctions & cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) — thông tin (information / 정보), incentives và quy tắc (rule / 규칙) thiết kế (design / 설계)

> **Mạch đọc:** Đặt **Auctions & cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) — thông tin (information / 정보), incentives và quy tắc (rule / 규칙) thiết kế (design / 설계)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Ba lớp phải tách trước khi phân tích** sang **2. Private giá trị (value / 값) và dùng chung (common / 공통) giá trị (value / 값)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Auction không chỉ là cách “bán cho người trả giá cao nhất”. Mỗi auction format xác định ai thắng, ai trả bao nhiêu, bidder nên reveal thông tin (information / 정보) thế nào và seller thu revenue ra sao. cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) đi xa hơn: thay vì nhận rules như cố định, designer chọn rules để đạt một mục tiêu (objective / 목표) dưới incentive và thông tin (information / 정보) các ràng buộc (constraints / 제약조건들).

## 1. Ba lớp phải tách trước khi phân tích

Một auction cần xác định ít nhất:

```text
Value structure
Information structure
Allocation/payment rule
```

Nếu bidder giá trị (value / 값) là private, chiến lược (strategy / 전략) khác common-value môi trường (environment / 환경). Nếu rủi ro (risk / 위험) aversion hoặc ngân sách (budget / 예산) ràng buộc (constraint / 제약조건) thay đổi, bidding hành vi (behavior / 동작) cũng đổi.

## 2. Private giá trị (value / 값) và dùng chung (common / 공통) giá trị (value / 값)

Trong independent private values, mỗi bidder biết own valuation và valuation đó không phụ thuộc trực tiếp thông tin (information / 정보) của others.

Trong dùng chung (common / 공통) giá trị (value / 값), item có một underlying giá trị (value / 값) chung nhưng bidders có signals khác nhau. Oil trường dữ liệu (field / 필드), mineral rights hoặc acquisition mục tiêu (target / 대상) có thể gần common-value setting.

Nhiều real auctions là affiliated/interdependent values: vừa có private thành phần (component / 컴포넌트) vừa có dùng chung (common / 공통) thành phần (component / 컴포넌트).

## 3. English auction

English auction tăng price dần cho đến khi chỉ còn một bidder.

Trong simple private-value setting, chiến lược (strategy / 전략) trực giác là ở lại cho đến khi price chạm own valuation. Winner trả gần second-highest valuation.

Open bidding cho bidders quan sát thông tin (information / 정보) từ rivals, nên trong common-value settings nó có thể giúp giảm winner’s curse qua thông tin (information / 정보) aggregation.

## 4. Dutch auction

Dutch auction bắt đầu từ price cao rồi hạ đến khi một bidder chấp nhận.

Bidder phải trade off price thấp hơn với rủi ro (risk / 위험) người khác accept trước. Trong independent private values và risk-neutral benchmark, Dutch auction có strategic equivalence với first-price sealed-bid auction.

## 5. First-price sealed-bid

Bidder gửi một bid kín; highest bid thắng và trả own bid.

Nếu bidder giá trị (value / 값) `v`, bid bằng đúng `v` làm zero surplus khi thắng, nên bidder thường shade bid dưới giá trị (value / 값).

Optimal shading phụ thuộc number of bidders và phân phối (distribution / 분포) of rivals’ values. Competition mạnh hơn thường làm shading nhỏ hơn.

## 6. Second-price sealed-bid và truthful bidding

Trong Vickrey auction, highest bid thắng nhưng trả second-highest bid.

Với private values, no ngân sách (budget / 예산) issue và tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들), bidding own true valuation là weakly dominant.

Reason: own bid chủ yếu quyết định thắng hay không; payment khi thắng do rival bid quyết định. Overbid có thể khiến bidder thắng khi price vượt giá trị (value / 값); underbid có thể khiến bidder thua dù price vẫn thấp hơn giá trị (value / 값).

Kết luận truthful bidding không được generalize sang dùng chung (common / 공통) values, collusion, ngân sách (budget / 예산) các ràng buộc (constraints / 제약조건들) hoặc complex multi-item settings.

## 7. Revenue equivalence theorem

Dưới các giả định (assumptions / 가정들) mạnh — risk-neutral bidders, independent private values, symmetric distributions, same allocation quy tắc (rule / 규칙) và lowest kiểu (type / 타입) expected surplus giống nhau — nhiều tiêu chuẩn (standard / 표준) auction formats tạo cùng expected seller revenue.

Theorem quan trọng vì nó cho biết **format alone** không tạo revenue magic trong benchmark.

Nếu revenue khác ngoài đời, cần tìm giả định (assumption / 가정) bị phá: rủi ro (risk / 위험) aversion, entry, reserve price, affiliation, asymmetric bidders hoặc ngân sách (budget / 예산) các ràng buộc (constraints / 제약조건들).

## 8. rủi ro (risk / 위험) aversion

Trong first-price auction, risk-averse bidder thường bid more aggressively vì giá trị (value / 값) của tăng xác suất (probability / 확률) thắng lớn hơn chi phí (cost / 비용) của giảm surplus khi thắng.

Second-price truthful thuộc tính (property / 속성) trong private-value benchmark ít phụ thuộc rủi ro (risk / 위험) attitude hơn vì payment không do own bid quyết định tại margin tương tự.

Do đó rủi ro (risk / 위험) aversion có thể phá revenue equivalence.

## 9. Reserve price

Seller có thể đặt minimum acceptable price. Reserve cao tăng revenue conditional on sale nhưng tăng xác suất (probability / 확률) no sale.

Optimal reserve trong Bayesian mô hình (model / 모델) phụ thuộc giá trị (value / 값) phân phối (distribution / 분포) và seller outside option.

Reserve price là example classic của cơ chế (mechanism / 메커니즘) thiết kế (design / 설계): quy tắc (rule / 규칙) intentionally excludes some trades để improve seller mục tiêu (objective / 목표), nên revenue maximization không đồng nghĩa total-surplus maximization.

## 10. Winner’s curse

Trong common-value auction, winner thường là bidder có tín hiệu (signal / 신호) optimistic nhất. Conditional on winning, own tín hiệu (signal / 신호) có upward selection độ lệch (bias / 편향).

Nếu bidder không correct for this selection, expected profit có thể âm: winner’s curse.

Rational bidder shades bid để account for thông tin (information / 정보) contained in sự kiện (event / 이벤트) “I won”. More bidders can intensify winner’s curse even while increasing competition.

## 11. Affiliation và thông tin (information / 정보) bản phát hành (release / 릴리스)

Nếu signals positively related, observing others’ thông tin (information / 정보) can improve estimate of dùng chung (common / 공통) giá trị (value / 값). Open ascending auction may produce different kết quả (outcome / 결과) from sealed-bid format because bidding tiến trình (process / 프로세스) reveals thông tin (information / 정보).

Seller thông tin (information / 정보) disclosure can raise or lower revenue depending on môi trường (environment / 환경); there is no universal “more transparency always raises revenue” kết quả (result / 결과).

## 12. Entry chi phí (cost / 비용) và number of bidders

Auction revenue depends heavily on participation. A highly sophisticated cơ chế (mechanism / 메커니즘) with few bidders can perform worse than a simple cơ chế (mechanism / 메커니즘) that attracts broad entry.

Bid preparation, qualification, deposits and bất định (uncertainty / 불확실성) create entry costs.

Designer should therefore optimize not only bidding chiến lược (strategy / 전략) after entry but also ex-ante participation incentive.

## 13. Multi-unit auctions

When multiple identical units are sold, allocation and pricing rules become more complex. Uniform-price auction can create demand reduction: bidder may shade demand for additional units to avoid pushing clearing price up.

Pay-as-bid auction changes bidding incentives but does not automatically reduce procurement chi phí (cost / 비용) because rational bidders incorporate expected clearing conditions into bids.

## 14. Procurement auctions

In procurement, buyer wants low chi phí (cost / 비용) rather than high selling price. Lowest qualified bid may win, but chất lượng (quality / 품질) and completion rủi ro (risk / 위험) matter.

If đặc tả hợp đồng (contract / 계약) awards only on lowest price, suppliers may underbid then renegotiate, cut chất lượng (quality / 품질) or take excessive rủi ro (risk / 위험).

Cơ chế (mechanism / 메커니즘) may need scoring quy tắc (rule / 규칙) combining price, chất lượng (quality / 품질), past hiệu năng (performance / 성능) and technical yêu cầu (requirement / 요구사항). This reconnects auction thiết kế (design / 설계) with principal–tác nhân (agent / 에이전트) and incomplete-contract problems.

## 15. cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) reverses the direction of phân tích (analysis / 분석)

Game lý thuyết (theory / 이론) asks:

```text
Given rules, what equilibrium behavior follows?
```

Cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) asks:

```text
Given desired outcome and private information,
what rules make desired behavior incentive-compatible?
```

Designer cannot directly command private kiểu (type / 타입); rules must make truthful or desired hành động (action / 동작) individually rational.

## 16. Incentive tính tương thích (compatibility / 호환성)

A cơ chế (mechanism / 메커니즘) is incentive compatible when each participant prefers to follow intended reporting/hành động (action / 동작) quy tắc (rule / 규칙) rather than misreport, given others do the same.

For direct cơ chế (mechanism / 메커니즘) with kiểu (type / 타입) `θ_i`, truthful hiện thực (implementation / 구현) requires:

```text
U_i(θ_i, truthful report) ≥ U_i(θ_i, alternative report)
```

for every feasible misreport under relevant equilibrium concept.

## 17. Participation ràng buộc (constraint / 제약조건)

Even truthful cơ chế (mechanism / 메커니즘) fails if agents prefer not to participate.

Individual rationality requires expected utility from participation at least outside option.

Designer therefore faces both:

```text
Incentive compatibility
Participation / individual rationality
```

plus ngân sách (budget / 예산) and feasibility các ràng buộc (constraints / 제약조건들).

## 18. Revelation principle

Revelation principle says that if an kết quả (outcome / 결과) can be implemented by some cơ chế (mechanism / 메커니즘), then under tiêu chuẩn (standard / 표준) conditions there is a direct cơ chế (mechanism / 메커니즘) where agents truthfully report types and the same kết quả (outcome / 결과) is implemented.

This is a simplification theorem for phân tích (analysis / 분석), not a claim that real-world cơ chế (mechanism / 메커니즘) must literally ask everyone to trạng thái (state / 상태) “true kiểu (type / 타입)”.

It lets theorists study truthful direct mechanisms without searching every complicated game form.

## 19. VCG intuition

Vickrey–Clarke–Groves mechanisms choose allocation maximizing reported total giá trị (value / 값) and charge each tác nhân (agent / 에이전트) according to externality they impose on others.

This can make truthful reporting dominant under quasilinear utility and suitable các giả định (assumptions / 가정들).

But VCG may have weak ngân sách (budget / 예산) balance, high thông tin (information / 정보)/computation yêu cầu (requirement / 요구사항) and vulnerability to collusion or false-name bids in some settings.

## 20. Myerson intuition

Revenue-optimal auction with private independent values may allocate based on **virtual valuation**, not raw valuation alone.

This explains why optimal reserve price can exclude some positive-surplus trades: seller revenue mục tiêu (objective / 목표) differs from xã hội (social / 사회적) surplus.

The chính xác (exact / 정확한) derivation is advanced, but conceptual lesson is central: “efficient cơ chế (mechanism / 메커니즘)” and “revenue-maximizing cơ chế (mechanism / 메커니즘)” are different thiết kế (design / 설계) targets.

## 21. Matching markets without prices

Cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) also covers environments where money is restricted or inappropriate, such as school choice, medical residency matching or organ exchange.

Stable matching asks whether any unmatched pair would prefer each other to assigned partners.

Strategy-proofness, stability and efficiency can xung đột (conflict / 충돌). There may be no cơ chế (mechanism / 메커니즘) satisfying every desirable thuộc tính (property / 속성) simultaneously.

## 22. Auctions with complements and substitutes

When bidders giá trị (value / 값) bundles, item-by-item auctions can create exposure bài toán (problem / 문제): bidder wins one thành phần (component / 컴포넌트) but not complementary thành phần (component / 컴포넌트).

Combinatorial auctions let bidders bid on bundles, but winner determination becomes computationally hard and strategic độ phức tạp (complexity / 복잡도) rises.

Cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) therefore interacts with khoa học máy tính (computer science / 컴퓨터 과학) through tối ưu hóa (optimization / 최적화) and computational độ phức tạp (complexity / 복잡도).

## 23. Collusion and shill bidding

Bidders can collude to suppress bids or rotate winners. Seller can use fake bids to manipulate price in some formats.

Cơ chế (mechanism / 메커니즘) robust in non-cooperative benchmark may thất bại (fail / 실패) under coalition hành vi (behavior / 동작).

Auction thiết kế (design / 설계) therefore needs monitoring, định danh (identity / 식별자) rules, kiểm tra (audit / 감사) trails and anti-collusion chính sách (policy / 정책) in addition to equilibrium lý thuyết (theory / 이론).

## 24. Algorithmic auctions and online platforms

Digital advertising auctions run at massive quy mô (scale / 규모), with automated bidding and real-time signals. cơ chế (mechanism / 메커니즘) thiết kế (design / 설계) must coexist with độ trễ (latency / 지연 시간), ngân sách (budget / 예산) pacing, học tập (learning / 학습) algorithms and strategic nền tảng (platform / 플랫폼) mục tiêu (objective / 목표).

Repeated tương tác (interaction / 상호작용) may make “single-auction truthfulness” insufficient if bidders learn or game long-run nền tảng (platform / 플랫폼) rules.

## 25. Empirical evaluation

A cơ chế (mechanism / 메커니즘) claim should be checked against dữ liệu (data / 데이터) such as bid distributions, entry, winning margins, reserve-price changes and bidder identities.

Structural estimation can recover giá trị (value / 값) distributions under mô hình (model / 모델) các giả định (assumptions / 가정들); trường dữ liệu (field / 필드) experiments or chính sách (policy / 정책) changes can kiểm thử (test / 테스트) reserve and format effects.

Observed bids are not automatically valuations. ánh xạ (mapping / 매핑) bid to giá trị (value / 값) depends on strategic mô hình (model / 모델).

## 26. thất bại (failure / 실패) modes

Sai lầm thứ nhất là nói second-price auction luôn truthful mà không nêu private-value các giả định (assumptions / 가정들).

Sai lầm thứ hai là bỏ winner’s curse trong common-value setting.

Sai lầm thứ ba là optimize auction conditional on entrants nhưng bỏ participation chi phí (cost / 비용).

Sai lầm thứ tư là đồng nhất seller revenue với xã hội (social / 사회적) welfare.

Sai lầm thứ năm là coi incentive-compatible cơ chế (mechanism / 메커니즘) tự động budget-balanced, simple và collusion-proof.

## 27. mô hình tư duy (mental model / 사고 모델)

Khi phân tích auction/cơ chế (mechanism / 메커니즘), hãy hỏi:

1. giá trị (value / 값) là private, dùng chung (common / 공통) hay interdependent?
2. Bidder biết gì về mình và others?
3. Allocation quy tắc (rule / 규칙) và payment quy tắc (rule / 규칙) là gì?
4. chiến lược (strategy / 전략) truthful, shaded hay mixed? Vì sao?
5. Winner sự kiện (event / 이벤트) reveal thông tin (information / 정보) gì?
6. Entry chi phí (cost / 비용) và reserve ảnh hưởng participation thế nào?
7. mục tiêu (objective / 목표) là efficiency, revenue, fairness hay stability?
8. Incentive-compatibility và participation các ràng buộc (constraints / 제약조건들) có giữ không?
9. cơ chế (mechanism / 메커니즘) có robust với ngân sách (budget / 예산) limit, collusion và repeated tương tác (interaction / 상호작용) không?
10. dữ liệu (data / 데이터) quan sát là bid hay true giá trị (value / 값), và mô hình (model / 모델) nào nối hai thứ đó?

Thị trường (market / 시장) cấu trúc (structure / 구조) & Game lý thuyết (theory / 이론) kết thúc ở đây với một spine hoàn chỉnh: benchmark competition → thị trường (market / 시장) power → strategic tương tác (interaction / 상호작용) → repeated dynamics → cơ chế (mechanism / 메커니즘) thiết kế (design / 설계). Applied Industrial Organization và Econometrics sẽ dùng spine này để phân tích thị trường (market / 시장) thực tế bằng bằng chứng (evidence / 증거) thay vì chỉ mô hình lý thuyết.

> **Bàn giao:** Sau **27. mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 competition monopoly and market power](./00_competition_monopoly_and_market_power.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
