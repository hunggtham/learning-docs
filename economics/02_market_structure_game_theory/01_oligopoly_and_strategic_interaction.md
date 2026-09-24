# Oligopoly & Strategic Interaction — Best response, Nash equilibrium và strategic commitment

Oligopoly bắt đầu khi một firm không thể tối ưu chỉ bằng cách nhìn market price hoặc market demand tĩnh. Payoff của firm phụ thuộc action của rivals, và mỗi rival cũng reasoning như vậy. Đây là domain của game theory: xác định players, actions, information, timing và payoff trước khi tìm equilibrium.

## 1. Game phải được mô tả trước khi giải

Một strategic game tối thiểu cần:

```text
Players
Actions / strategies
Payoffs
Information
Timing
```

Nếu thay đổi một yếu tố, equilibrium có thể đổi hoàn toàn. Vì vậy “duopoly” không tự nói price hoặc quantity sẽ bằng bao nhiêu.

## 2. Best response

Best response của player `i` là action tối đa hóa payoff khi giữ action của players khác cố định.

```text
BR_i(a_-i) = argmax U_i(a_i, a_-i)
```

Nash equilibrium là profile nơi mỗi action là best response với actions của phần còn lại.

```text
∀i: a_i* ∈ BR_i(a_-i*)
```

Nash equilibrium không có nghĩa socially optimal, fair hay stable dưới mọi learning process. Nó chỉ nói không player nào muốn unilateral deviation tại profile đó.

## 3. Prisoner’s dilemma và tension giữa individual incentive với collective outcome

Trong Prisoner’s Dilemma, mỗi player có dominant strategy defect, nhưng kết quả cả hai defect làm cả hai tệ hơn cooperation.

Model này minh họa một principle: equilibrium có thể inefficient dù mọi player rational theo payoff riêng.

Nhưng không nên gọi mọi conflict là Prisoner’s Dilemma. Payoff ordering phải thực sự có cấu trúc tương ứng.

## 4. Cournot competition: firms chọn quantity

Trong Cournot model, firms chọn quantity đồng thời. Market price phụ thuộc total quantity.

Với inverse demand:

```text
P = a − b(q1 + q2)
```

và marginal cost `c`, profit firm 1:

```text
π1 = [a − b(q1 + q2) − c]q1
```

FOC cho best response:

```text
q1 = (a − c − bq2) / 2b
```

Symmetric equilibrium:

```text
q1 = q2 = (a − c) / 3b
```

Total output nằm giữa monopoly và perfect competition trong simple linear case. Khi số firms tăng, outcome thường tiến gần competitive benchmark nếu assumptions giữ.

## 5. Strategic substitutes trong Cournot

Cournot best responses dốc xuống: rival produce nhiều hơn làm residual demand của firm nhỏ đi, nên best-response quantity giảm.

Actions như vậy được gọi là strategic substitutes.

Concept này quan trọng hơn việc nhớ công thức: nó giúp dự đoán response sign khi cost, capacity hoặc entry thay đổi.

## 6. Bertrand competition: firms chọn price

Trong homogeneous-product Bertrand với constant marginal cost, no capacity constraint và simultaneous pricing, undercutting logic đẩy price về marginal cost ngay cả với hai firms.

Đây là Bertrand paradox: rất ít firms nhưng outcome giống perfect competition.

Paradox biến mất khi thêm realistic frictions như product differentiation, capacity constraint, search cost hoặc repeated interaction.

## 7. Differentiated Bertrand

Nếu products differentiated, mỗi firm có downward-sloping residual demand và có thể sustain markup.

Best-response prices thường dốc lên: rival tăng price làm own product attractive hơn, nên firm có incentive tăng price. Đây là strategic complements.

Differentiation làm substitution matrix trở thành key empirical object: demand của product A chuyển sang B, C hay out-of-market option bao nhiêu khi A tăng price?

## 8. Cournot hay Bertrand không phải câu hỏi về “firm thực tế chọn gì” theo nghĩa literal

Firms ngoài đời thường chọn price, quantity, capacity, quality và promotion cùng lúc. Cournot/Bertrand là abstractions để capture strategic margin chính.

Chọn model cần dựa vào institution:

- quantity/capacity commitment mạnh trước khi price clear → Cournot-like;
- price dễ thay đổi, capacity flexible → Bertrand-like;
- capacity set trước rồi price cạnh tranh → two-stage game.

## 9. Sequential game và backward induction

Khi actions xảy ra theo sequence, normal-form Nash equilibrium không đủ mô tả credibility.

Backward induction giải từ node cuối về đầu. Subgame-perfect equilibrium (SPE) yêu cầu strategy tạo Nash equilibrium trong mọi subgame.

Điều này loại non-credible threats.

## 10. Entry deterrence và credible threat

Incumbent có thể đe dọa price war nếu entrant vào. Nhưng nếu sau entry, price war làm incumbent thiệt hơn accommodation, threat đó không credible.

Một threat chỉ influence entrant nếu action sau deviation thật sự optimal hoặc được support bởi commitment/institution.

## 11. Commitment thay đổi game

Firm có thể làm threat credible bằng irreversible investment như capacity, long-term contract, distribution exclusivity hoặc product architecture.

Commitment có strategic value khi nó thay đổi future best responses của rivals.

Nhưng commitment cũng giảm flexibility. Nếu demand đổi, sunk capacity có thể trở thành liability.

## 12. Stackelberg quantity leadership

Trong Stackelberg model, leader chọn quantity trước và follower quan sát rồi best respond.

Leader internalize follower reaction nên thường produce nhiều hơn Cournot firm và có first-mover advantage trong simple setup.

Nhưng first-mover advantage không universal. Với price competition, information revelation hoặc uncertainty, moving first có thể bất lợi.

## 13. Dominant strategy, Nash và iterated elimination

Dominant strategy tối ưu bất kể rivals làm gì. Nash chỉ cần optimal tại equilibrium actions của rivals.

Một game có thể không có dominant strategy nhưng vẫn có Nash equilibrium. Một game cũng có multiple equilibria.

Iterated elimination of strictly dominated strategies có thể đơn giản hóa game, nhưng không phải lúc nào cũng chọn duy nhất một equilibrium.

## 14. Mixed strategies

Nếu không có pure-strategy equilibrium hoặc players muốn giữ unpredictability, mixed strategy có thể xuất hiện.

Player randomize giữa actions sao cho rival indifferent giữa actions trong support.

Mixed strategy không nhất thiết mô tả con người “tung đồng xu” literal; nó có thể là population frequency, strategic unpredictability hoặc reduced-form representation.

## 15. Coordination game và multiple equilibria

Trong coordination game, nhiều equilibria có thể cùng tồn tại. Technology standard, platform adoption hoặc convention xã hội thường có network complementarity làm history và expectation quan trọng.

Nash equilibrium concept không tự chọn equilibrium nào xảy ra. Cần thêm focal point, learning, institutions, switching cost hoặc equilibrium-selection refinement.

## 16. Chicken và strategic brinkmanship

Chicken game có incentive tránh mutual escalation nhưng mỗi side muốn đối phương nhượng trước.

Commitment, reputation và signaling resolve game khác Prisoner’s Dilemma. Việc phân biệt payoff structure quyết định policy interpretation.

## 17. Information và Bayesian games

Nếu players không biết type của rival, strategy phụ thuộc belief.

Bayesian Nash equilibrium yêu cầu mỗi type best respond theo posterior belief về types khác.

Auction, entry, pricing với private cost và bargaining thường cần incomplete-information game thay vì complete-information Nash.

## 18. Strategic entry với private information

Incumbent có thể không biết entrant cost; entrant có thể không biết incumbent willingness to fight. Actions như aggressive price hoặc capacity expansion có thể vừa ảnh hưởng payoff trực tiếp vừa signal type.

Đây là bridge giữa game theory và information asymmetry.

## 19. Welfare trong oligopoly

Oligopoly có thể gây markup và output restriction, nhưng firms cũng compete qua quality, innovation và fixed investment.

Một merger giảm số firms có thể tăng pricing power nhưng cũng tạo cost synergy. Antitrust analysis vì vậy cần estimate cả unilateral effects và efficiencies, không dựa duy nhất vào concentration.

## 20. Empirical mapping

Theory tạo testable predictions như:

```text
Rival cost increases → own price/quantity response?
Entry → markup decreases?
Capacity expansion → rival investment changes?
Merger → diversion ratios and price pressure?
```

Data cần demand estimation, cost proxies, event variation hoặc structural model tùy claim.

## 21. Failure modes

Sai lầm thứ nhất là dùng “Nash equilibrium” như synonym của optimal outcome.

Sai lầm thứ hai là chọn Cournot/Bertrand chỉ vì market có vài firms mà không xét timing/capacity/product differentiation.

Sai lầm thứ ba là tin mọi threat vì nó được phát biểu.

Sai lầm thứ tư là nghĩ first mover luôn có advantage.

Sai lầm thứ năm là infer collusion chỉ từ parallel pricing; common cost shock hoặc strategic complement cũng có thể tạo đồng biến.

## 22. Mental model

Khi gặp strategic market, hãy hỏi:

1. Players là ai và action margin chính là gì?
2. Actions simultaneous hay sequential?
3. Player quan sát gì trước khi chọn?
4. Best response dốc lên hay xuống?
5. Equilibrium unique hay multiple?
6. Threat/commitment có credible không?
7. Entry hoặc cost shock làm best responses dịch thế nào?
8. Outcome khác competitive/monopoly benchmark ở quantity, price, quality và welfare ra sao?
9. Evidence nào phân biệt model này với alternative model?

Static games giải một interaction. Khi firms gặp nhau nhiều lần, future punishment và reputation có thể sustain behavior không tồn tại trong one-shot game. Đó là repeated-game layer.
