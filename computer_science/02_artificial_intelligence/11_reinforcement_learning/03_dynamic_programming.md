# Dynamic Programming trong Reinforcement Learning

**Dynamic Programming (DP / 동적 계획법)** giải MDP khi transition model và reward model đã biết. Ý tưởng là exploit Bellman recursion để chia long-horizon decision problem thành các subproblems liên kết qua value functions.

DP không phải “training từ data” theo nghĩa modern ML. Nó là exact/planning-style computation trên known model, nhưng concepts của nó là foundation cho RL.

## Policy Evaluation

Với policy cố định `π`, lặp Bellman expectation backup:

\[
V_{k+1}(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Under standard finite discounted MDP assumptions, sequence converge tới `V^π`.

## Policy Improvement

Sau khi có value estimate, chọn action greedy:

\[
\pi'(s)=\arg\max_a\sum_{s'}P(s'|s,a)[R+\gamma V^\pi(s')]
\]

Policy improvement theorem cho biết policy mới không tệ hơn policy cũ.

## Policy Iteration

```text
initialize π
repeat:
    evaluate V^π
    improve π greedily
until stable
```

Evaluation không nhất thiết phải converge hoàn toàn mỗi iteration; modified policy iteration có thể xen kẽ partial updates.

## Value Iteration

Kết hợp evaluation và improvement trực tiếp:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Sau convergence, extract greedy policy.

## Synchronous vs Asynchronous Updates

Synchronous dùng old vector `V_k` để update all states.

Asynchronous/in-place cập nhật state từng phần và dùng latest values ngay. Có thể converge nhanh hơn nếu scheduling tốt.

## Generalized Policy Iteration

Một mental model rộng:

```text
policy evaluation pushes value toward truth under current policy
policy improvement pushes policy toward greedy wrt current value
```

Hai processes tương tác cho tới consistency.

Nhiều RL algorithms hiện đại có thể nhìn như approximate Generalized Policy Iteration.

## Computational Cost

Tabular DP cần sweep qua state/action/transition spaces. Nếu state space khổng lồ, cost không khả thi.

Đây là **curse of dimensionality**: số states tăng combinatorially theo dimensions.

RL/function approximation xuất hiện một phần vì không thể enumerate toàn state space.

## Known Model Assumption

DP cần `P` và `R`. Trong real world chúng thường unknown hoặc too complex.

Model-based RL có thể học approximate model rồi dùng planning/DP-like methods.

## Example: Gridworld

Grid cells là states; actions up/down/left/right; transition deterministic hoặc stochastic; reward -1 mỗi step.

Value iteration propagate distance-to-goal information backward từ terminal cells. Value surfaces dần encode “state này gần đường tốt tới goal đến đâu”.

## Bellman Operator

Define optimal Bellman operator `T`:

\[
(TV)(s)=\max_a\mathbb E[R+\gamma V(S')]
\]

Trong discounted finite MDP, `T` là contraction dưới sup norm với factor `γ`, giải thích convergence của value iteration.

## DP và Shortest Path

Deterministic shortest-path algorithms có related recursive structure. Bellman-Ford cũng repeatedly relax edges. RL generalizes intuition sang stochastic dynamics + rewards.

## DP và Planning

Classical planning search enumerates trajectories; DP reuses state values across many possible trajectories. Khi nhiều paths merge vào same state, value reuse rất powerful.

## Limitations

- cần known model;
- state enumeration;
- exact expectation có thể expensive;
- model errors propagate;
- partial observability cần richer belief-state formulation.

## Mental Model

> **Dynamic Programming là Bellman recursion khi ta có map đầy đủ của environment; Reinforcement Learning học khi map không đầy đủ và chỉ thấy samples.**

## Common Misconceptions

### “DP là một RL algorithm online”

DP thường giả định known model và full sweeps, nên gần planning hơn learning from unknown environment.

### “Value iteration luôn nhanh”

Convergence mathematical không có nghĩa practical cost thấp trên huge state spaces.

### “Policy iteration luôn cần exact evaluation”

Approximate/partial evaluation vẫn có thể tạo useful variants.

## Knowledge Connection

DP nối Bellman equations với sample-based methods. Monte Carlo sẽ bỏ known transition model và dùng complete sampled returns.

Xem tiếp: [Monte Carlo Methods](./04_monte_carlo_methods.md).