# Markov Decision Processes

**Markov Decision Process (MDP / 마르코프 결정 과정)** là mathematical framework cho sequential decision making khi state hiện tại chứa đủ information relevant để predict future dynamics dưới action.

Một MDP thường được mô tả bởi tuple:

\[
(\mathcal S,\mathcal A,P,R,\gamma)
\]

trong đó:

- `S`: state space;
- `A`: action space;
- `P(s'|s,a)`: transition distribution;
- `R(s,a,s')`: reward;
- `γ`: discount factor.

## Markov Property

Markov assumption:

\[
P(S_{t+1}\mid S_t,A_t,S_{t-1},...) = P(S_{t+1}\mid S_t,A_t)
\]

Nghĩa là nếu state representation đầy đủ, quá khứ không cung cấp thêm information cần cho next transition.

Điều này là assumption về **representation**, không phải world “không có history”. Nếu state thiếu thông tin, Markov property fail.

Ví dụ game board hiện tại có thể đủ để quyết định legal moves. Nhưng user conversation chỉ giữ latest message thường không đủ state.

## Transition Model

`P(s'|s,a)` nói environment có thể chuyển sang đâu sau action.

Deterministic case:

\[
s'=T(s,a)
\]

Stochastic case cần distribution.

Ví dụ autonomous vehicle braking có outcome phụ thuộc road condition, sensor uncertainty và other actors.

## Reward Function

Reward có thể depend on state/action/next state. Objective không phải maximize immediate reward mà expected return.

Một choice reward khác có thể tạo policy hoàn toàn khác dù dynamics giống nhau.

## Policy

Policy:

\[
\pi(a|s)
\]

induces a Markov chain over states. Khi policy fixed, decision problem biến thành policy evaluation problem.

## Trajectory Probability

Một trajectory:

\[
\tau=(s_0,a_0,r_1,s_1,a_1,...)
\]

có probability phụ thuộc initial state, policy và transition dynamics:

\[
P(\tau)=P(s_0)\prod_t \pi(a_t|s_t)P(s_{t+1}|s_t,a_t)
\]

Expression này giải thích tại sao policy ảnh hưởng distribution data agent thu được.

## Finite Horizon và Infinite Horizon

Finite-horizon problem có số bước giới hạn `T`. Optimal policy có thể depend on time remaining.

Infinite-horizon discounted problem thường tìm stationary policy dưới assumptions thích hợp.

## Terminal State

Terminal/absorbing state có thể kết thúc episode. Sau terminal không có meaningful future actions/rewards.

## MDP và Planning

Nếu `P` và `R` biết rõ, ta có thể solve MDP bằng Dynamic Programming như value iteration/policy iteration.

Nếu unknown, RL học từ samples.

Do đó:

```text
Known model + optimize policy → planning/control
Unknown model + experience → reinforcement learning
```

Boundary này mềm vì model-based RL có thể học model rồi plan.

## POMDP

Khi agent không observe full state, ta có **Partially Observable MDP (POMDP)**. Agent nhận observation `o_t`, không trực tiếp state `s_t`.

Có thể maintain belief:

\[
b_t(s)=P(S_t=s\mid history)
\]

Belief state biến uncertainty về hidden state thành state representation mới.

## State Design

State quá nhỏ → non-Markov, agent khó learn.

State quá lớn → sample complexity và computation tăng.

Representation learning trong RL tìm state features giữ decision-relevant information.

## Action Granularity

Action space cũng là design choice. Low-level continuous actions cho control chính xác nhưng horizon dài. High-level actions reduce horizon nhưng cần abstraction/model.

Agent tools trong LLM systems cũng có analogy: `click(x,y)` low-level vs `create_ticket(...)` high-level.

## Discount Factor Interpretation

`γ` có thể hiểu như:

- preference for sooner reward;
- effective horizon;
- mathematical device for convergence;
- probability-like continuation interpretation trong một số settings.

Effective horizon roughly grows as `1/(1-γ)` khi γ gần 1, nhưng đây chỉ intuition.

## Reward Scale

Scale reward ảnh hưởng numerical optimization và hyperparameters dù optimal policy lý tưởng có thể invariant với positive scaling trong một số settings.

## Mental Model

> **MDP là state-machine có uncertainty + rewards + choices. RL học cách điều khiển state-machine đó khi dynamics hoặc optimal policy chưa biết.**

## Common Misconceptions

### “Markov nghĩa là random”

Không. Markov nói future conditionally independent of past given present state; transition có thể deterministic.

### “State = observation”

Chỉ đúng trong fully observable setting.

### “MDP chỉ là lý thuyết cho game”

Nó là foundation cho robotics, operations, recommendation, resource allocation và sequential control.

## Knowledge Connection

MDP nối Probability, Dynamic Programming, Control Theory và agent state representation.

Xem tiếp: [Value Functions and Bellman Equations](./02_value_functions_and_bellman_equations.md).