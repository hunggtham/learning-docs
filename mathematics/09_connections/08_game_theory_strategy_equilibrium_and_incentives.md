# Game theory: strategy, equilibrium và incentives trong các hệ nhiều tác nhân

> **Mạch đọc:** Chapter này nối [Probability & decision/risk](./07_probability_calibration_decision_and_risk.md), [Optimization](../08_optimization_numerical/00_optimization.md) và [Linear programming & duality](../08_optimization_numerical/05_linear_programming_duality_and_simplex.md) với economics, software systems và social interaction. Optimization thường hỏi “một decision maker nên làm gì?”. Game theory hỏi câu khó hơn: **ta nên làm gì khi outcome còn phụ thuộc vào decisions của những người/agents khác đang tối ưu mục tiêu của chính họ?**

Trong một ordinary optimization problem, environment thường được coi là fixed:

```math
\max_x U(x).
```

Trong strategic setting, utility của player `i` phụ thuộc cả strategy của player khác:

```math
u_i(s_1,s_2,\ldots,s_n).
```

Nếu ta đổi strategy, đối thủ cũng có thể đổi. Vì vậy “best action” không còn là property của action alone; nó phụ thuộc beliefs, rules và responses của others.

Đây là core idea của **game theory (lý thuyết trò chơi / 게임이론)**.

---

## 1. Một game cần những thành phần nào?

Một strategic-form game thường cần:

1. **players (플레이어)**;
2. strategy set `S_i` cho mỗi player;
3. payoff/utility function `u_i`;
4. information structure;
5. timing/rules nếu game có nhiều stages.

Một model game không phải description đầy đủ của con người. Nó deliberately giữ lại incentives và strategic dependencies relevant cho question.

Mental rule:

> Trước khi “solve game”, phải biết game model đang assume điều gì về options, information và preferences.

---

## 2. Strategy khác action

Một **action (행동)** là move tại một decision point.

Một **strategy (전략)** là complete contingent plan: player sẽ làm gì trong mọi situation mà họ có thể gặp.

Trong one-shot matrix game, action và strategy có thể trông giống nhau.

Trong sequential game, distinction quan trọng. Strategy phải specify cả actions ở branches có thể không xảy ra.

Điều này cần thiết để define equilibrium và credible responses.

---

## 3. Payoff matrix

Two-player finite game có thể represent bằng matrix.

Ví dụ:

```text
               Player B
             L           R
Player A U   (3,2)       (0,0)
         D   (1,1)       (2,3)
```

Pair `(a,b)` là payoff của A và B.

Matrix không nói payoff phải là money. Nó có thể represent utility ranking, profit, cost converted sign, latency preference hoặc abstract objective.

Utility scale phải được interpreted carefully; cardinal vs ordinal assumptions matter trong richer models.

---

## 4. Best response

Cho strategies của others cố định, **best response (최적반응)** của player `i` maximize payoff:

```math
s_i^*\in
\arg\max_{s_i\in S_i}
u_i(s_i,s_{-i}).
```

Ký hiệu `s_{-i}` nghĩa strategies của tất cả players trừ `i`.

Game theory chuyển optimization thành system of mutually dependent optimization problems:

```text
A best-responds to B
B best-responds to A
```

Equilibrium xuất hiện khi responses consistent với nhau.

---

## 5. Dominant strategy

Strategy `s_i` là **dominant (우월전략)** nếu nó tốt nhất bất kể others làm gì.

Nếu strict dominant strategy tồn tại, decision đơn giản hơn vì player không cần forecast opponent.

Nhưng dominant strategies hiếm hơn Nash equilibria.

Không nên học game theory bằng rule “tìm dominant strategy rồi xong”; nhiều important games không có one.

---

## 6. Prisoner's Dilemma: individual rationality có thể tạo collective loss

Canonical payoff ordering:

```text
                 B Cooperate   B Defect
A Cooperate          (3,3)        (0,5)
A Defect             (5,0)        (1,1)
```

Defect là dominant cho mỗi player:

```text
if other cooperates → defect gives 5 > 3
if other defects    → defect gives 1 > 0
```

Do đó outcome:

```text
(Defect, Defect)
```

nhưng both prefer `(Cooperate, Cooperate)` over `(Defect, Defect)`.

Key lesson:

> Individually optimal incentives có thể không tạo socially optimal outcome.

Đây là reason mechanism/rule design quan trọng trong markets, distributed protocols và institutions.

---

## 7. Nash equilibrium

Strategy profile `s*` là **Nash equilibrium (내시 균형)** nếu không player nào có incentive unilateral deviation:

```math
u_i(s_i^*,s_{-i}^*)
\ge
u_i(s_i,s_{-i}^*)
```

cho mọi `i` và mọi alternative `s_i`.

Equivalent:

```text
each player's strategy is a best response to the others
```

Nash equilibrium là **self-consistency condition**, không phải statement rằng outcome fair, efficient hoặc morally good.

---

## 8. Nash equilibrium không phải global optimum

Trong Prisoner's Dilemma, Nash equilibrium có total payoff:

```math
1+1=2,
```

trong khi cooperative outcome total:

```math
3+3=6.
```

Equilibrium giải câu hỏi:

```text
“Có ai muốn tự đổi action khi others giữ nguyên không?”
```

Nó không trực tiếp giải:

```text
“Outcome này có maximize social welfare không?”
```

Đây là distinction giữa equilibrium và efficiency.

---

## 9. Pareto efficiency

Outcome A **Pareto dominates** B nếu ít nhất một player tốt hơn và không ai tệ hơn.

Outcome là **Pareto efficient (파레토 효율)** nếu không có outcome khác Pareto dominate nó.

Nash và Pareto là independent concepts:

```text
Nash → unilateral deviation stability
Pareto → collective improvement possibility
```

Policy/economic analysis thường cần nhìn cả hai.

---

## 10. Zero-sum games

Trong two-player zero-sum game:

```math
u_1(s_1,s_2)
=-u_2(s_1,s_2).
```

Một player's gain exactly equals other's loss.

Ta có thể write one payoff matrix `A`; row player maximize, column player minimize.

Core optimization:

```math
\max_i \min_j A_{ij}
```

vs

```math
\min_j \max_i A_{ij}.
```

Nếu pure strategies không meet, mixed strategies become necessary.

---

## 11. Mixed strategy

A **mixed strategy (혼합전략)** là probability distribution over pure strategies.

Ví dụ Rock–Paper–Scissors equilibrium:

```math
P(R)=P(P)=P(S)=\frac13.
```

Randomization không phải vì player “không biết chọn gì”. Nó có strategic role: make opponent indifferent và prevent exploitation.

Expected payoff becomes bilinear in strategy probabilities.

---

## 12. Indifference principle

Trong many 2×2 mixed equilibria, player chooses probabilities khiến opponent indifferent giữa pure strategies họ randomize over.

Nếu opponent strictly prefers one action, họ would not mix.

So solve condition:

```math
E[u(\text{opponent action 1})]
=
E[u(\text{opponent action 2})].
```

Important subtlety:

> Ta choose our mixing probability to make **the other player** indifferent, not ourselves directly.

---

## 13. Minimax theorem

For finite two-player zero-sum games:

```math
\max_p\min_q p^TAq
=
\min_q\max_p p^TAq.
```

Mixed strategies eliminate gap between maximin and minimax.

This is closely connected to linear-programming duality.

A player's optimal mixed-strategy problem can be written as LP; opponent's problem is dual.

Thus game theory and optimization share one structural theorem:

```text
strategic equilibrium
↔ convex optimization / duality
```

---

## 14. Coordination game

Not all games are conflict.

Example:

```text
                 B Left    B Right
A Left            (4,4)     (0,0)
A Right           (0,0)     (2,2)
```

Có two Nash equilibria.

Problem không phải incentive to defect, mà **equilibrium selection**.

History, convention, communication hoặc focal points có thể determine which equilibrium society/system settles on.

This models standards, keyboard layouts, protocols and conventions.

---

## 15. Anti-coordination và congestion

Sometimes players prefer different resources.

Example: two services choosing same overloaded server.

Payoff decreases when too many agents choose same resource.

This leads to **congestion games (혼잡 게임)**.

Traffic routing is classic case: each driver chooses route minimizing own travel time, but selfish equilibrium may create worse total travel time than centrally optimized routing.

---

## 16. Price of anarchy

**Price of Anarchy — PoA (무질서의 대가)** measures inefficiency of decentralized equilibrium relative to social optimum.

For cost minimization:

```math
PoA
=
\frac{\text{worst equilibrium social cost}}
{\text{optimal social cost}}.
```

This concept is important in algorithmic game theory and distributed systems.

It turns “selfish agents can be inefficient” into a quantitative question.

---

## 17. Repeated games change incentives

One-shot Prisoner's Dilemma favors defection.

If game repeats and future matters, current defection can be punished later.

Discounted total utility might be:

```math
U
=
\sum_{t=0}^{\infty}\delta^t u_t,
\qquad 0<\delta<1.
```

High `δ` means players value future strongly.

Cooperation can become sustainable because short-run gain from cheating is traded against long-run loss.

Repeated interaction changes game even if stage-game payoffs unchanged.

---

## 18. Trigger strategies và reputation

A trigger strategy might cooperate while opponent cooperates, then punish after deviation.

Such strategies create credible future consequences.

In markets/software ecosystems, reputation systems can similarly alter incentives by linking today's behavior to tomorrow's opportunities.

But punishment must be credible: if punishing is itself irrational when time comes, threat may not influence current behavior.

---

## 19. Sequential games và game trees

When timing matters, matrix form can hide information.

Extensive-form representation uses game tree:

```text
Player A moves
   ├─ action L → Player B moves
   └─ action R → Player B moves
```

Nodes encode decision points; edges actions; leaves payoffs.

Sequential rationality requires evaluating what players would do after every possible history.

---

## 20. Backward induction

For finite perfect-information game, analyze from terminal decisions backward.

Pattern:

```text
solve last mover's best choice
→ replace subtree by resulting payoff
→ move one step backward
→ repeat
```

This is dynamic programming on a game tree.

But backward induction depends on assumptions like rationality and known payoffs/information.

---

## 21. Subgame-perfect equilibrium

A Nash equilibrium may rely on non-credible threats off equilibrium path.

**Subgame-perfect equilibrium (부분게임 완전균형)** requires strategy profile be Nash equilibrium in every subgame.

It filters equilibria using sequential rationality.

This is why complete strategy—not just observed action—matters.

---

## 22. Imperfect information

Players may not observe previous actions or private types.

Then we need information sets and beliefs.

Examples:

- auction bidder knows own valuation but not others';
- cybersecurity attacker/defender has partial information;
- hiring market has private worker quality;
- distributed node may not know global state.

Strategic problem becomes joint reasoning about actions **and information**.

---

## 23. Bayesian games

If player has private type `\theta_i`, payoff:

```math
u_i(s,\theta_i,\theta_{-i}).
```

Players have beliefs over unknown types.

A strategy maps type to action:

```math
s_i:\Theta_i\to A_i.
```

Bayesian Nash equilibrium requires optimality in expectation given beliefs.

This connects game theory with Bayesian probability and decision theory.

---

## 24. Mechanism design: reverse game theory

Ordinary game theory:

```text
given rules
→ predict strategic behavior
```

**Mechanism design (cơ chế thiết kế / 메커니즘 디자인)** asks reverse question:

```text
desired outcome
→ what rules/incentives make strategic behavior produce it?
```

Examples:

- auction rules;
- matching systems;
- tax/subsidy structures;
- API pricing/rate limits;
- marketplace fees;
- protocol rewards/penalties.

This is engineering of incentives.

---

## 25. Incentive compatibility

A mechanism is **incentive compatible (유인 양립적)** if following desired/truthful strategy is optimal under specified conditions.

Instead of hoping users behave correctly, system designer aligns private incentives with system goal.

This is a crucial systems principle:

> Good rules make desired behavior locally rational.

---

## 26. Auctions: first-price vs second-price intuition

In first-price sealed-bid auction, winner pays own bid. Bidders generally have incentive to shade bid below true value depending beliefs/risk model.

In second-price auction, winner pays second-highest bid. Under classic independent private-value assumptions, truthful bidding is a dominant strategy.

The important lesson is not “second price always best”. It is:

> Payment rule changes strategic incentives even when allocation objective looks similar.

Mechanism details are part of the model, not administrative decoration.

---

## 27. Stable matching khác maximum matching

Maximum bipartite matching asks maximize number of matched pairs.

**Stable matching (안정 매칭)** adds preferences and asks avoid blocking pair: two agents who would both prefer each other over current assignments.

Thus:

```text
maximum matching → cardinality/feasibility objective
stable matching  → strategic/preference stability
```

Same graph may have different “best” matching depending problem definition.

---

## 28. Evolutionary game theory

Not all agents solve optimization explicitly.

Evolutionary game theory studies strategy frequencies changing under differential success.

Replicator equation:

```math
\dot x_i
=
x_i\left[(Ax)_i-x^TAx\right].
```

A strategy grows when its payoff exceeds population average.

This connects game theory directly to [Dynamical systems](../05_calculus/16_dynamical_systems_bifurcations_and_chaos.md).

Equilibrium becomes population-state stability question.

---

## 29. Security games

Defender has limited resources; attacker chooses target.

Defender strategy can intentionally randomize patrol/inspection allocation.

If schedule predictable, attacker exploits weak time/location.

Mixed strategies become operationally meaningful.

But real security modeling must include asymmetric information, bounded rationality and changing attacker objectives.

---

## 30. Game theory trong software/platform systems

Strategic behavior appears whenever users adapt to rules:

```text
ranking algorithm → creators optimize content
rate limit        → clients alter request patterns
pricing           → customers shift usage
fraud detection   → attackers adapt
matching system   → participants game reported preferences
performance metric→ teams optimize measured metric
```

This is Goodhart-like environment: once metric becomes target, agents react.

Software design with strategic users needs incentive-aware thinking, not only algorithm correctness.

---

## 31. Equilibrium can be fragile

A predicted equilibrium depends on assumptions:

- rationality;
- common knowledge;
- payoff specification;
- information;
- ability to randomize;
- repeated vs one-shot interaction;
- coordination conventions.

Small model changes can change equilibrium set.

Game theory is not a machine that predicts human behavior from a payoff table with certainty. It is a framework for conditional reasoning:

> **If** these rules, preferences and information assumptions hold, **then** these strategic pressures follow.

---

## 32. Common misconceptions

**“Game theory means zero-sum competition.”** Many games are non-zero-sum, coordination or mixed cooperation/conflict.

**“Nash equilibrium is best outcome.”** It means unilateral stability, not social optimality.

**“Rational players always choose deterministic actions.”** Mixed strategy can be rational and necessary.

**“Dominant strategy always exists.”** Many games have none.

**“Repeated game is same game repeated mechanically.”** Future consequences fundamentally change incentives.

**“Mechanism can force truth without assumptions.”** Incentive compatibility depends on model conditions.

**“Stable matching and maximum matching are same.”** They optimize different concepts.

---

## 33. Mental model

> Optimization asks for the best action when environment is fixed. Game theory makes environment endogenous: other agents observe, choose and adapt. Best response is conditional optimization; Nash equilibrium is mutual consistency of best responses; repeated games add future consequences; mechanism design chooses rules so private incentives produce desired outcomes. The central question is never only “what is optimal?”, but “optimal given that everyone else is also choosing strategically?”.

---

## 34. Mạch học tiếp

```text
Probability / expected value
→ Optimization
→ Best response
→ Nash equilibrium
→ Mixed strategies / minimax
→ Sequential & repeated games
→ Bayesian games
→ Mechanism design
```

Connections:

- [Linear programming and duality](../08_optimization_numerical/05_linear_programming_duality_and_simplex.md)
- [Network flows and matching](../07_discrete_cs/12_network_flows_matchings_and_min_cut.md)
- [Probability calibration, decision and risk](./07_probability_calibration_decision_and_risk.md)
- [Dynamical systems](../05_calculus/16_dynamical_systems_bifurcations_and_chaos.md)
- Economics library for market/institution applications.

## Further reading

- Jennifer Firkins Nordstrom — *Introduction to Game Theory: a Discovery Approach*, an open introductory text covering two-person zero-sum, repeated zero-sum and non-zero-sum games.
