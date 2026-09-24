# Auctions & Mechanism Design — Information, incentives và rule design

Auction không chỉ là cách “bán cho người trả giá cao nhất”. Mỗi auction format xác định ai thắng, ai trả bao nhiêu, bidder nên reveal information thế nào và seller thu revenue ra sao. Mechanism design đi xa hơn: thay vì nhận rules như cố định, designer chọn rules để đạt một objective dưới incentive và information constraints.

## 1. Ba lớp phải tách trước khi phân tích

Một auction cần xác định ít nhất:

```text
Value structure
Information structure
Allocation/payment rule
```

Nếu bidder value là private, strategy khác common-value environment. Nếu risk aversion hoặc budget constraint thay đổi, bidding behavior cũng đổi.

## 2. Private value và common value

Trong independent private values, mỗi bidder biết own valuation và valuation đó không phụ thuộc trực tiếp information của others.

Trong common value, item có một underlying value chung nhưng bidders có signals khác nhau. Oil field, mineral rights hoặc acquisition target có thể gần common-value setting.

Nhiều real auctions là affiliated/interdependent values: vừa có private component vừa có common component.

## 3. English auction

English auction tăng price dần cho đến khi chỉ còn một bidder.

Trong simple private-value setting, strategy trực giác là ở lại cho đến khi price chạm own valuation. Winner trả gần second-highest valuation.

Open bidding cho bidders quan sát information từ rivals, nên trong common-value settings nó có thể giúp giảm winner’s curse qua information aggregation.

## 4. Dutch auction

Dutch auction bắt đầu từ price cao rồi hạ đến khi một bidder chấp nhận.

Bidder phải trade off price thấp hơn với risk người khác accept trước. Trong independent private values và risk-neutral benchmark, Dutch auction có strategic equivalence với first-price sealed-bid auction.

## 5. First-price sealed-bid

Bidder gửi một bid kín; highest bid thắng và trả own bid.

Nếu bidder value `v`, bid bằng đúng `v` làm zero surplus khi thắng, nên bidder thường shade bid dưới value.

Optimal shading phụ thuộc number of bidders và distribution of rivals’ values. Competition mạnh hơn thường làm shading nhỏ hơn.

## 6. Second-price sealed-bid và truthful bidding

Trong Vickrey auction, highest bid thắng nhưng trả second-highest bid.

Với private values, no budget issue và standard assumptions, bidding own true valuation là weakly dominant.

Reason: own bid chủ yếu quyết định thắng hay không; payment khi thắng do rival bid quyết định. Overbid có thể khiến bidder thắng khi price vượt value; underbid có thể khiến bidder thua dù price vẫn thấp hơn value.

Kết luận truthful bidding không được generalize sang common values, collusion, budget constraints hoặc complex multi-item settings.

## 7. Revenue equivalence theorem

Dưới assumptions mạnh — risk-neutral bidders, independent private values, symmetric distributions, same allocation rule và lowest type expected surplus giống nhau — nhiều standard auction formats tạo cùng expected seller revenue.

Theorem quan trọng vì nó cho biết **format alone** không tạo revenue magic trong benchmark.

Nếu revenue khác ngoài đời, cần tìm assumption bị phá: risk aversion, entry, reserve price, affiliation, asymmetric bidders hoặc budget constraints.

## 8. Risk aversion

Trong first-price auction, risk-averse bidder thường bid more aggressively vì value của tăng probability thắng lớn hơn cost của giảm surplus khi thắng.

Second-price truthful property trong private-value benchmark ít phụ thuộc risk attitude hơn vì payment không do own bid quyết định tại margin tương tự.

Do đó risk aversion có thể phá revenue equivalence.

## 9. Reserve price

Seller có thể đặt minimum acceptable price. Reserve cao tăng revenue conditional on sale nhưng tăng probability no sale.

Optimal reserve trong Bayesian model phụ thuộc value distribution và seller outside option.

Reserve price là example classic của mechanism design: rule intentionally excludes some trades để improve seller objective, nên revenue maximization không đồng nghĩa total-surplus maximization.

## 10. Winner’s curse

Trong common-value auction, winner thường là bidder có signal optimistic nhất. Conditional on winning, own signal có upward selection bias.

Nếu bidder không correct for this selection, expected profit có thể âm: winner’s curse.

Rational bidder shades bid để account for information contained in event “I won”. More bidders can intensify winner’s curse even while increasing competition.

## 11. Affiliation và information release

Nếu signals positively related, observing others’ information can improve estimate of common value. Open ascending auction may produce different outcome from sealed-bid format because bidding process reveals information.

Seller information disclosure can raise or lower revenue depending on environment; there is no universal “more transparency always raises revenue” result.

## 12. Entry cost và number of bidders

Auction revenue depends heavily on participation. A highly sophisticated mechanism with few bidders can perform worse than a simple mechanism that attracts broad entry.

Bid preparation, qualification, deposits and uncertainty create entry costs.

Designer should therefore optimize not only bidding strategy after entry but also ex-ante participation incentive.

## 13. Multi-unit auctions

When multiple identical units are sold, allocation and pricing rules become more complex. Uniform-price auction can create demand reduction: bidder may shade demand for additional units to avoid pushing clearing price up.

Pay-as-bid auction changes bidding incentives but does not automatically reduce procurement cost because rational bidders incorporate expected clearing conditions into bids.

## 14. Procurement auctions

In procurement, buyer wants low cost rather than high selling price. Lowest qualified bid may win, but quality and completion risk matter.

If contract awards only on lowest price, suppliers may underbid then renegotiate, cut quality or take excessive risk.

Mechanism may need scoring rule combining price, quality, past performance and technical requirement. This reconnects auction design with principal–agent and incomplete-contract problems.

## 15. Mechanism design reverses the direction of analysis

Game theory asks:

```text
Given rules, what equilibrium behavior follows?
```

Mechanism design asks:

```text
Given desired outcome and private information,
what rules make desired behavior incentive-compatible?
```

Designer cannot directly command private type; rules must make truthful or desired action individually rational.

## 16. Incentive compatibility

A mechanism is incentive compatible when each participant prefers to follow intended reporting/action rule rather than misreport, given others do the same.

For direct mechanism with type `θ_i`, truthful implementation requires:

```text
U_i(θ_i, truthful report) ≥ U_i(θ_i, alternative report)
```

for every feasible misreport under relevant equilibrium concept.

## 17. Participation constraint

Even truthful mechanism fails if agents prefer not to participate.

Individual rationality requires expected utility from participation at least outside option.

Designer therefore faces both:

```text
Incentive compatibility
Participation / individual rationality
```

plus budget and feasibility constraints.

## 18. Revelation principle

Revelation principle says that if an outcome can be implemented by some mechanism, then under standard conditions there is a direct mechanism where agents truthfully report types and the same outcome is implemented.

This is a simplification theorem for analysis, not a claim that real-world mechanism must literally ask everyone to state “true type”.

It lets theorists study truthful direct mechanisms without searching every complicated game form.

## 19. VCG intuition

Vickrey–Clarke–Groves mechanisms choose allocation maximizing reported total value and charge each agent according to externality they impose on others.

This can make truthful reporting dominant under quasilinear utility and suitable assumptions.

But VCG may have weak budget balance, high information/computation requirement and vulnerability to collusion or false-name bids in some settings.

## 20. Myerson intuition

Revenue-optimal auction with private independent values may allocate based on **virtual valuation**, not raw valuation alone.

This explains why optimal reserve price can exclude some positive-surplus trades: seller revenue objective differs from social surplus.

The exact derivation is advanced, but conceptual lesson is central: “efficient mechanism” and “revenue-maximizing mechanism” are different design targets.

## 21. Matching markets without prices

Mechanism design also covers environments where money is restricted or inappropriate, such as school choice, medical residency matching or organ exchange.

Stable matching asks whether any unmatched pair would prefer each other to assigned partners.

Strategy-proofness, stability and efficiency can conflict. There may be no mechanism satisfying every desirable property simultaneously.

## 22. Auctions with complements and substitutes

When bidders value bundles, item-by-item auctions can create exposure problem: bidder wins one component but not complementary component.

Combinatorial auctions let bidders bid on bundles, but winner determination becomes computationally hard and strategic complexity rises.

Mechanism design therefore interacts with computer science through optimization and computational complexity.

## 23. Collusion and shill bidding

Bidders can collude to suppress bids or rotate winners. Seller can use fake bids to manipulate price in some formats.

Mechanism robust in non-cooperative benchmark may fail under coalition behavior.

Auction design therefore needs monitoring, identity rules, audit trails and anti-collusion policy in addition to equilibrium theory.

## 24. Algorithmic auctions and online platforms

Digital advertising auctions run at massive scale, with automated bidding and real-time signals. Mechanism design must coexist with latency, budget pacing, learning algorithms and strategic platform objective.

Repeated interaction may make “single-auction truthfulness” insufficient if bidders learn or game long-run platform rules.

## 25. Empirical evaluation

A mechanism claim should be checked against data such as bid distributions, entry, winning margins, reserve-price changes and bidder identities.

Structural estimation can recover value distributions under model assumptions; field experiments or policy changes can test reserve and format effects.

Observed bids are not automatically valuations. Mapping bid to value depends on strategic model.

## 26. Failure modes

Sai lầm thứ nhất là nói second-price auction luôn truthful mà không nêu private-value assumptions.

Sai lầm thứ hai là bỏ winner’s curse trong common-value setting.

Sai lầm thứ ba là optimize auction conditional on entrants nhưng bỏ participation cost.

Sai lầm thứ tư là đồng nhất seller revenue với social welfare.

Sai lầm thứ năm là coi incentive-compatible mechanism tự động budget-balanced, simple và collusion-proof.

## 27. Mental model

Khi phân tích auction/mechanism, hãy hỏi:

1. Value là private, common hay interdependent?
2. Bidder biết gì về mình và others?
3. Allocation rule và payment rule là gì?
4. Strategy truthful, shaded hay mixed? Vì sao?
5. Winner event reveal information gì?
6. Entry cost và reserve ảnh hưởng participation thế nào?
7. Objective là efficiency, revenue, fairness hay stability?
8. Incentive-compatibility và participation constraints có giữ không?
9. Mechanism có robust với budget limit, collusion và repeated interaction không?
10. Data quan sát là bid hay true value, và model nào nối hai thứ đó?

Market Structure & Game Theory kết thúc ở đây với một spine hoàn chỉnh: benchmark competition → market power → strategic interaction → repeated dynamics → mechanism design. Applied Industrial Organization và Econometrics sẽ dùng spine này để phân tích market thực tế bằng evidence thay vì chỉ mô hình lý thuyết.
