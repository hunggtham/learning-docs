# Value Functions và Bellman Equations

Trong Reinforcement Learning, immediate reward không đủ để đánh giá một state/action vì action hiện tại ảnh hưởng cả future. **Value function (가치 함수 / hàm giá trị)** nén expected long-term return thành một quantity có thể học và optimize.

State value:

\[
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]
\]

Action value:

\[
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]
\]

## Bellman decomposition

Return có recursive structure:

\[
G_t=R_{t+1}+\gamma G_{t+1}
\]

Do đó:

\[
V^\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma V^\pi(S_{t+1})\mid S_t=s]
\]

Đây là Bellman expectation equation.

Nếu transition/reward known:

\[
V^\pi(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R(s,a,s')+\gamma V^\pi(s')]
\]

Bellman equation không phải một heuristic; nó đến trực tiếp từ recursive definition của discounted return.

## Q-function Bellman equation

\[
Q^\pi(s,a)=\mathbb E[R_{t+1}+\gamma\mathbb E_{a'\sim\pi}[Q^\pi(S_{t+1},a')]]
\]

Nếu biết Q tốt, policy có thể chọn action value cao.

## Optimal value

\[
V^*(s)=\max_\pi V^\pi(s)
\]

Optimal Bellman equation:

\[
V^*(s)=\max_a\mathbb E[R_{t+1}+\gamma V^*(S_{t+1})]
\]

và:

\[
Q^*(s,a)=\mathbb E[R_{t+1}+\gamma\max_{a'}Q^*(S_{t+1},a')]
\]

`max` biến policy evaluation thành control problem.

## Bootstrapping

Nếu estimate value dựa trên estimate khác:

```text
current estimate ← reward + γ × next value estimate
```

đó là **bootstrapping**.

Dynamic Programming và Temporal Difference dùng bootstrapping. Monte Carlo dùng actual sampled return tới cuối episode thay vì bootstrap.

## Bellman Backup

Một update dạng:

\[
V(s)\leftarrow R+\gamma V(s')
\]

được gọi là backup. Trong stochastic problems thường update gradual bằng learning rate.

## Bellman Error

Nếu function approximator `V_θ` không satisfy Bellman consistency, residual:

\[
\delta = R+\gamma V_\theta(s')-V_\theta(s)
\]

là TD error trong one-step setting.

Positive δ nghĩa outcome tốt hơn current estimate; negative δ nghĩa tệ hơn.

## Value như compressed future

Value function là một prediction model về future return. Thay vì simulate toàn future mỗi decision, agent consult value estimate.

Đây tương tự heuristic trong search: cả hai compress future consequence thành scalar estimate. Nhưng value được defined bởi reward/policy/environment dynamics.

## Policy Evaluation và Improvement

Policy iteration dựa hai ideas:

1. evaluate `V^π`;
2. improve policy greedily theo value/Q.

Repeated evaluation + improvement có thể converge tới optimal policy trong finite MDP under standard assumptions.

## Advantage

Advantage đo action tốt hơn baseline state value bao nhiêu:

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)
\]

Nó rất quan trọng trong policy-gradient/actor-critic vì giảm variance và tập trung vào relative quality của action.

## Why value estimation is hard

Value depends on:

- policy;
- reward definition;
- transition dynamics;
- future state distribution;
- approximation error.

Policy thay đổi thì target value cũng thay đổi.

## Function Approximation

Tabular value có one entry per state. Large/continuous state cần approximator:

\[
V_\theta(s)
\]

Neural network generalizes across states, nhưng bootstrapping + off-policy + nonlinear approximation có thể gây instability.

## Overestimation Bias

Trong Q-learning, max trên noisy estimates có thể overestimate:

\[
\mathbb E[\max_a \hat Q(a)] \ge \max_a \mathbb E[\hat Q(a)]
\]

Double Q-learning/DQN variants tách selection/evaluation để giảm bias.

## Reward-to-Go và Credit

Value functions propagate delayed reward backward qua states. Đây là cơ chế giải temporal credit assignment mà không cần mỗi action có direct label.

## Mental Model

> **Bellman equation nói: giá trị của hiện tại = reward ngay bây giờ + discounted value của tương lai.**

Recursive relation này là xương sống của large part of RL.

## Common Misconceptions

### “Value là probability thắng”

Chỉ trong reward setup đặc biệt. General value là expected return.

### “Bellman equation cho biết value ngay lập tức”

Nó là consistency relation. Ta vẫn cần solve/estimate qua DP, sampling hoặc function approximation.

### “Q và reward giống nhau”

Q chứa long-term expected return, không chỉ immediate reward.

## Knowledge Connection

Bellman equations nối recursive algorithms, Dynamic Programming và bootstrapping. Chapter tiếp theo dùng known model để compute values systematically.

Xem tiếp: [Dynamic Programming](./03_dynamic_programming.md).