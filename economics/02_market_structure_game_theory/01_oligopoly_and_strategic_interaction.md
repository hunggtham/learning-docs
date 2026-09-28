# Oligopoly & Strategic Tương tác (interaction / 상호작용) — Best phản hồi (response / 응답), Nash equilibrium và strategic commitment

Oligopoly bắt đầu khi một firm không thể tối ưu chỉ bằng cách nhìn thị trường (market / 시장) price hoặc thị trường (market / 시장) demand tĩnh. Payoff của firm phụ thuộc hành động (action / 동작) của rivals, và mỗi rival cũng lập luận (reasoning / 추론) như vậy. Đây là lĩnh vực (domain / 도메인) của game lý thuyết (theory / 이론): xác định players, actions, thông tin (information / 정보), timing và payoff trước khi tìm equilibrium.

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

## 2. Best phản hồi (response / 응답)

Best phản hồi (response / 응답) của player `i` là hành động (action / 동작) tối đa hóa payoff khi giữ hành động (action / 동작) của players khác cố định.

```text
BR_i(a_-i) = argmax U_i(a_i, a_-i)
```

Nash equilibrium là profile nơi mỗi hành động (action / 동작) là best phản hồi (response / 응답) với actions của phần còn lại.

```text
∀i: a_i* ∈ BR_i(a_-i*)
```

Nash equilibrium không có nghĩa socially optimal, fair hay stable dưới mọi học tập (learning / 학습) tiến trình (process / 프로세스). Nó chỉ nói không player nào muốn unilateral deviation tại profile đó.

## 3. Prisoner’s dilemma và tension giữa individual incentive với collective kết quả (outcome / 결과)

Trong Prisoner’s Dilemma, mỗi player có dominant chiến lược (strategy / 전략) defect, nhưng kết quả cả hai defect làm cả hai tệ hơn cooperation.

Mô hình (model / 모델) này minh họa một principle: equilibrium có thể inefficient dù mọi player rational theo payoff riêng.

Nhưng không nên gọi mọi xung đột (conflict / 충돌) là Prisoner’s Dilemma. Payoff thứ tự (ordering / 순서) phải thực sự có cấu trúc tương ứng.

## 4. Cournot competition: firms chọn quantity

Trong Cournot mô hình (model / 모델), firms chọn quantity đồng thời. Thị trường (market / 시장) price phụ thuộc total quantity.

Với inverse demand:

```text
P = a − b(q1 + q2)
```

và marginal chi phí (cost / 비용) `c`, profit firm 1:

```text
π1 = [a − b(q1 + q2) − c]q1
```

FOC cho best phản hồi (response / 응답):

```text
q1 = (a − c − bq2) / 2b
```

Symmetric equilibrium:

```text
q1 = q2 = (a − c) / 3b
```

Total đầu ra (output / 출력) nằm giữa monopoly và perfect competition trong simple tuyến tính (linear / 선형) trường hợp (case / 사례). Khi số firms tăng, kết quả (outcome / 결과) thường tiến gần competitive benchmark nếu các giả định (assumptions / 가정들) giữ.

## 5. Strategic substitutes trong Cournot

Cournot best responses dốc xuống: rival produce nhiều hơn làm residual demand của firm nhỏ đi, nên best-response quantity giảm.

Actions như vậy được gọi là strategic substitutes.

Concept này quan trọng hơn việc nhớ công thức: nó giúp dự đoán phản hồi (response / 응답) sign khi chi phí (cost / 비용), sức chứa (capacity / 용량) hoặc entry thay đổi.

## 6. Bertrand competition: firms chọn price

Trong homogeneous-product Bertrand với constant marginal chi phí (cost / 비용), no sức chứa (capacity / 용량) ràng buộc (constraint / 제약조건) và simultaneous pricing, undercutting lô-gic (logic / 논리) đẩy price về marginal chi phí (cost / 비용) ngay cả với hai firms.

Đây là Bertrand paradox: rất ít firms nhưng kết quả (outcome / 결과) giống perfect competition.

Paradox biến mất khi thêm realistic frictions như sản phẩm (product / 제품) differentiation, sức chứa (capacity / 용량) ràng buộc (constraint / 제약조건), tìm kiếm (search / 검색) chi phí (cost / 비용) hoặc repeated tương tác (interaction / 상호작용).

## 7. Differentiated Bertrand

Nếu products differentiated, mỗi firm có downward-sloping residual demand và có thể sustain markup.

Best-response prices thường dốc lên: rival tăng price làm own sản phẩm (product / 제품) attractive hơn, nên firm có incentive tăng price. Đây là strategic complements.

Differentiation làm substitution ma trận (matrix / 행렬) trở thành key empirical đối tượng (object / 객체): demand của sản phẩm (product / 제품) A chuyển sang B, C hay out-of-market option bao nhiêu khi A tăng price?

## 8. Cournot hay Bertrand không phải câu hỏi về “firm thực tế chọn gì” theo nghĩa literal

Firms ngoài đời thường chọn price, quantity, sức chứa (capacity / 용량), chất lượng (quality / 품질) và promotion cùng lúc. Cournot/Bertrand là abstractions để capture strategic margin chính.

Chọn mô hình (model / 모델) cần dựa vào institution:

- quantity/sức chứa (capacity / 용량) commitment mạnh trước khi price clear → Cournot-like;
- price dễ thay đổi, sức chứa (capacity / 용량) flexible → Bertrand-like;
- sức chứa (capacity / 용량) set trước rồi price cạnh tranh → two-stage game.

## 9. Sequential game và backward induction

Khi actions xảy ra theo chuỗi (sequence / 시퀀스), normal-form Nash equilibrium không đủ mô tả credibility.

Backward induction giải từ nút (node / 노드) cuối về đầu. Subgame-perfect equilibrium (SPE) yêu cầu chiến lược (strategy / 전략) tạo Nash equilibrium trong mọi subgame.

Điều này loại non-credible threats.

## 10. Entry deterrence và credible threat

Incumbent có thể đe dọa price war nếu entrant vào. Nhưng nếu sau entry, price war làm incumbent thiệt hơn accommodation, threat đó không credible.

Một threat chỉ influence entrant nếu hành động (action / 동작) sau deviation thật sự optimal hoặc được hỗ trợ (support / 지원) bởi commitment/institution.

## 11. Commitment thay đổi game

Firm có thể làm threat credible bằng irreversible investment như sức chứa (capacity / 용량), long-term đặc tả hợp đồng (contract / 계약), phân phối (distribution / 분포) exclusivity hoặc sản phẩm (product / 제품) kiến trúc (architecture / 아키텍처).

Commitment có strategic giá trị (value / 값) khi nó thay đổi future best responses của rivals.

Nhưng commitment cũng giảm flexibility. Nếu demand đổi, sunk sức chứa (capacity / 용량) có thể trở thành liability.

## 12. Stackelberg quantity leadership

Trong Stackelberg mô hình (model / 모델), leader chọn quantity trước và follower quan sát rồi best respond.

Leader internalize follower reaction nên thường produce nhiều hơn Cournot firm và có first-mover advantage trong simple setup.

Nhưng first-mover advantage không universal. Với price competition, thông tin (information / 정보) revelation hoặc bất định (uncertainty / 불확실성), moving first có thể bất lợi.

## 13. Dominant chiến lược (strategy / 전략), Nash và iterated elimination

Dominant chiến lược (strategy / 전략) tối ưu bất kể rivals làm gì. Nash chỉ cần optimal tại equilibrium actions của rivals.

Một game có thể không có dominant chiến lược (strategy / 전략) nhưng vẫn có Nash equilibrium. Một game cũng có multiple equilibria.

Iterated elimination of strictly dominated strategies có thể đơn giản hóa game, nhưng không phải lúc nào cũng chọn duy nhất một equilibrium.

## 14. Mixed strategies

Nếu không có pure-strategy equilibrium hoặc players muốn giữ unpredictability, mixed chiến lược (strategy / 전략) có thể xuất hiện.

Player randomize giữa actions sao cho rival indifferent giữa actions trong hỗ trợ (support / 지원).

Mixed chiến lược (strategy / 전략) không nhất thiết mô tả con người “tung đồng xu” literal; nó có thể là population frequency, strategic unpredictability hoặc reduced-form biểu diễn (representation / 표현).

## 15. Coordination game và multiple equilibria

Trong coordination game, nhiều equilibria có thể cùng tồn tại. Technology tiêu chuẩn (standard / 표준), nền tảng (platform / 플랫폼) adoption hoặc convention xã hội thường có mạng (network / 네트워크) complementarity làm lịch sử (history / 이력) và expectation quan trọng.

Nash equilibrium concept không tự chọn equilibrium nào xảy ra. Cần thêm focal điểm (point / 지점), học tập (learning / 학습), institutions, switching chi phí (cost / 비용) hoặc equilibrium-selection refinement.

## 16. Chicken và strategic brinkmanship

Chicken game có incentive tránh mutual escalation nhưng mỗi side muốn đối phương nhượng trước.

Commitment, reputation và signaling resolve game khác Prisoner’s Dilemma. Việc phân biệt payoff cấu trúc (structure / 구조) quyết định chính sách (policy / 정책) interpretation.

## 17. Thông tin (information / 정보) và Bayesian games

Nếu players không biết kiểu (type / 타입) của rival, chiến lược (strategy / 전략) phụ thuộc belief.

Bayesian Nash equilibrium yêu cầu mỗi kiểu (type / 타입) best respond theo posterior belief về types khác.

Auction, entry, pricing với private chi phí (cost / 비용) và bargaining thường cần incomplete-information game thay vì complete-information Nash.

## 18. Strategic entry với private thông tin (information / 정보)

Incumbent có thể không biết entrant chi phí (cost / 비용); entrant có thể không biết incumbent willingness to fight. Actions như aggressive price hoặc sức chứa (capacity / 용량) expansion có thể vừa ảnh hưởng payoff trực tiếp vừa tín hiệu (signal / 신호) kiểu (type / 타입).

Đây là cầu nối (bridge / 브리지) giữa game lý thuyết (theory / 이론) và thông tin (information / 정보) asymmetry.

## 19. Welfare trong oligopoly

Oligopoly có thể gây markup và đầu ra (output / 출력) restriction, nhưng firms cũng compete qua chất lượng (quality / 품질), innovation và fixed investment.

Một merger giảm số firms có thể tăng pricing power nhưng cũng tạo chi phí (cost / 비용) synergy. Antitrust phân tích (analysis / 분석) vì vậy cần estimate cả unilateral effects và efficiencies, không dựa duy nhất vào concentration.

## 20. Empirical ánh xạ (mapping / 매핑)

Lý thuyết (theory / 이론) tạo testable predictions như:

```text
Rival cost increases → own price/quantity response?
Entry → markup decreases?
Capacity expansion → rival investment changes?
Merger → diversion ratios and price pressure?
```

Dữ liệu (data / 데이터) cần demand estimation, chi phí (cost / 비용) proxies, sự kiện (event / 이벤트) variation hoặc structural mô hình (model / 모델) tùy claim.

## 21. Thất bại (failure / 실패) modes

Sai lầm thứ nhất là dùng “Nash equilibrium” như synonym của optimal kết quả (outcome / 결과).

Sai lầm thứ hai là chọn Cournot/Bertrand chỉ vì thị trường (market / 시장) có vài firms mà không xét timing/sức chứa (capacity / 용량)/sản phẩm (product / 제품) differentiation.

Sai lầm thứ ba là tin mọi threat vì nó được phát biểu.

Sai lầm thứ tư là nghĩ first mover luôn có advantage.

Sai lầm thứ năm là infer collusion chỉ từ parallel pricing; dùng chung (common / 공통) chi phí (cost / 비용) shock hoặc strategic complement cũng có thể tạo đồng biến.

## 22. Mô hình tư duy (mental model / 사고 모델)

Khi gặp strategic thị trường (market / 시장), hãy hỏi:

1. Players là ai và hành động (action / 동작) margin chính là gì?
2. Actions simultaneous hay sequential?
3. Player quan sát gì trước khi chọn?
4. Best phản hồi (response / 응답) dốc lên hay xuống?
5. Equilibrium unique hay multiple?
6. Threat/commitment có credible không?
7. Entry hoặc chi phí (cost / 비용) shock làm best responses dịch thế nào?
8. Kết quả (outcome / 결과) khác competitive/monopoly benchmark ở quantity, price, chất lượng (quality / 품질) và welfare ra sao?
9. Bằng chứng (evidence / 증거) nào phân biệt mô hình (model / 모델) này với alternative mô hình (model / 모델)?

Static games giải một tương tác (interaction / 상호작용). Khi firms gặp nhau nhiều lần, future punishment và reputation có thể sustain hành vi (behavior / 동작) không tồn tại trong one-shot game. Đó là repeated-game tầng (layer / 계층).
