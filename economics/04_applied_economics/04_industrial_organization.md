# Industrial Organization — Demand estimation, markups, entry, mergers và platform markets

Industrial Organization (IO) áp dụng microeconomics, game theory và econometrics vào industries cụ thể. Mục tiêu không chỉ là gọi market “competitive” hay “concentrated”, mà là đo demand substitution, costs, markups, entry barriers, strategic responses và counterfactual policy outcomes.

Theory cung cấp structure; data quyết định parameter; policy cần counterfactual.

## 1. Market definition là empirical substitution question

Relevant market phải phản ánh products/regions thật sự constrain pricing.

Cross-price elasticity giúp đo substitution:

```text
ε_ij = %ΔQ_i / %ΔP_j
```

Nếu product j tăng giá làm demand i tăng mạnh, chúng là close substitutes.

## 2. Concentration is not conduct

HHI/concentration mô tả structure nhưng không tự chứng minh market power hoặc anticompetitive conduct.

High concentration có thể đến từ economies of scale/productivity; low concentration vẫn có local/platform power.

## 3. Demand estimation

Firm-level pricing/merger analysis cần own- and cross-price elasticities.

Simple demand regression bị endogeneity vì price phản ứng demand shocks. Instruments có thể dùng cost shifters hoặc rival characteristics dưới assumptions.

## 4. Discrete choice

Consumers often choose one product among alternatives plus outside option.

Logit models map utility to choice probabilities; richer random-coefficient models allow heterogeneous substitution.

IIA restriction của simple logit can be unrealistic.

## 5. Diversion ratio

Diversion ratio hỏi khi product A mất một customer, bao nhiêu fraction chuyển sang B.

It is central for merger unilateral-effects analysis because close substitutes create stronger post-merger pricing incentive.

## 6. Marginal cost and markup

Under differentiated Bertrand, estimated demand + first-order pricing conditions can back out marginal costs and markups.

Observed accounting margin is not the same as economic markup.

## 7. Lerner index

```text
L = (P − MC) / P
```

In simple monopoly it relates to inverse elasticity, but empirical use requires credible MC/demand estimates.

## 8. Pass-through

How taxes/input costs move into prices reveals market structure and demand curvature.

Pass-through can exceed or fall below 100%; one-for-one is not universal.

## 9. Entry models

Entry occurs when expected profit covers fixed cost.

Observed number of firms reflects market size, fixed costs and strategic interaction.

Entry thresholds across markets can identify competitive effects but market heterogeneity matters.

## 10. Sunk costs

Advertising, R&D, network building and regulation can be sunk, changing contestability and exit decisions.

High fixed cost alone does not equal barrier if recoverable.

## 11. Product differentiation

Horizontal differentiation reflects taste; vertical differentiation reflects quality ranking.

Differentiation softens price competition but can increase variety and consumer surplus.

## 12. Quality choice

Firms may compete on quality, service, privacy or delivery rather than only price.

Merger effects can therefore include nonprice dimensions.

## 13. Price discrimination

IO estimates whether segments differ in elasticity and whether discrimination expands output or mainly transfers surplus.

Digital personalization raises measurement and privacy questions.

## 14. Switching costs

Contracts, data portability, learning and ecosystem lock-in make customers less elastic after adoption.

Switching cost can support investment but also entrench incumbent.

## 15. Network effects

Platform value can rise with users or complementors. Network effects can create tipping and high entry barriers.

Need distinguish direct network benefit from platform market power.

## 16. Two-sided platforms

Platform chooses prices/rules jointly across sides, e.g. users and advertisers, riders and drivers.

Price on one side may be zero/subsidized because it attracts participation valuable to other side.

Single-sided markup logic can mislead.

## 17. Most-favored-nation and parity clauses

Contract terms restricting lower prices elsewhere can reduce free-riding on platform services or soften inter-platform competition.

Effect is context-specific.

## 18. Vertical relationships

Manufacturer-retailer relationships create double marginalization, resale pricing, exclusive dealing and foreclosure questions.

Vertical integration can eliminate double markups but may disadvantage rivals.

## 19. Double marginalization

If upstream and downstream each add monopoly markup, final price can exceed integrated monopoly price.

Vertical integration may lower prices even while increasing control.

## 20. Exclusive dealing

Exclusivity can protect relationship-specific investment or foreclose rivals from key distribution/input.

Assess duration, coverage, alternatives and scale needed for entry.

## 21. Tying and bundling

Bundling can price discriminate, reduce transaction costs or leverage power across products.

Competitive effect depends on demand correlation and foreclosure mechanism.

## 22. Merger analysis

A horizontal merger may increase unilateral pricing incentive by internalizing diversion between merging products.

Countervailing effects include marginal-cost efficiencies, repositioning, entry and buyer power.

## 23. Merger simulation

Estimated demand + conduct assumptions + efficiencies can simulate post-merger prices.

Simulation is conditional counterfactual, not fact; results depend on demand form, conduct and cost assumptions.

## 24. Event studies around mergers

Stock-market reactions can reflect expected profit change but do not directly measure consumer welfare; event contamination and anticipation matter.

Product-level post-merger price studies can complement structural simulation.

## 25. Cartels

Cartels restrict competition through price/quantity/customer allocation. Empirical detection may use bids, communication, structural breaks or screens.

Parallel pricing alone is insufficient proof.

## 26. Procurement

Procurement IO studies bidding, entry and scoring rules. Lowest bid may not minimize lifecycle cost if quality/renegotiation risk matters.

Auction models identify costs under assumptions about bidder values and competition.

## 27. Dynamic competition

R&D, capacity, installed base and learning make current choices alter future states.

Static markup may understate or overstate long-run welfare effect if innovation response large.

## 28. Innovation and competition

Competition can increase innovation by escape-from-competition incentives or reduce it by shrinking rents/resources.

Relationship may be heterogeneous/non-monotonic.

## 29. Patents

Patents trade temporary exclusion against innovation incentive and disclosure.

Patent count/quality is an imperfect innovation measure.

## 30. Regulation

Price caps, licensing, standards and access rules alter entry and investment incentives.

Regulatory capture and information asymmetry can create government failure.

## 31. Natural monopoly and utilities

Network industries with large fixed costs may require price regulation or access rules.

Marginal-cost pricing can fail to cover fixed cost; average-cost regulation can weaken cost-reduction incentives.

## 32. Telecom and interoperability

Interconnection terms determine whether entrants can reach incumbent networks. Standards can expand network value while affecting platform control.

## 33. Digital markets and zero price

Consumer price of zero does not imply zero market power. Attention, data, advertising load, quality and privacy can be relevant prices/costs.

Market definition needs nonprice substitution.

## 34. Algorithmic pricing

Pricing algorithms can react rapidly and may facilitate parallel conduct without explicit agreement, but common algorithms/common shocks can also create similar prices.

Empirical attribution requires more than observed synchronization.

## 35. Self-preferencing

Integrated platform may rank own products/services preferentially. This can improve integration/quality or exclude rivals.

Need measure traffic diversion, quality and entry effects.

## 36. Essential facilities and access

Control over infrastructure/data/distribution can create bottleneck. Mandatory access may promote entry but reduce investment incentive.

Policy must assess feasible duplication and pricing/access terms.

## 37. Structural vs reduced-form IO

Reduced-form designs estimate causal effects of mergers, entry or regulation around shocks.

Structural models estimate primitives to simulate counterfactuals not directly observed.

Structural approach gains extrapolation at cost of stronger assumptions.

## 38. Common empirical designs

- demand IV using cost shifters;
- merger DiD/event studies;
- entry thresholds across local markets;
- procurement auction estimation;
- regulatory discontinuities;
- platform policy experiments;
- natural experiments in capacity/input costs.

## 39. Welfare accounting

IO welfare may include:

```text
consumer surplus
producer surplus
quality/variety
innovation
entry/fixed costs
externalities
privacy/data costs
```

One short-run price effect is not always whole welfare story.

## 40. Failure modes

Sai lầm thứ nhất là equate concentration with market power.

Sai lầm thứ hai là estimate demand without handling price endogeneity.

Sai lầm thứ ba là infer markup from accounting profit alone.

Sai lầm thứ tư là evaluate merger only by HHI or only by one post-merger price coefficient.

Sai lầm thứ năm là use single-sided price logic for multi-sided platforms.

## 41. Applied analysis template

Khi phân tích industry, hãy hỏi:

1. relevant substitution set là gì?
2. demand elasticity/diversion được estimate thế nào?
3. price endogeneity được xử lý ra sao?
4. fixed/sunk costs và entry barriers là gì?
5. conduct model: Bertrand, Cournot, auction hay bargaining?
6. nonprice quality/innovation dimensions nào matter?
7. vertical/platform relationships tạo efficiencies hay foreclosure bằng mechanism nào?
8. counterfactual policy/merger cần assumptions gì?
9. evidence reduced-form có khớp structural model không?
10. welfare horizon short-run vs dynamic khác nhau thế nào?

Industrial Organization khép Applied Economics core bằng cách đưa theory + econometrics vào market thực. Bước tiếp theo của toàn Economics library là Economic History & Institutions, nơi models được đặt vào sequence dài hạn của technology, state capacity, finance và institutional change.
