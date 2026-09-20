# Actor-Critic

**Actor-Critic (액터-크리틱)** kết hợp hai components:

- **Actor**: policy `π_θ(a|s)` quyết định action;
- **Critic**: value estimator `V_w(s)` hoặc `Q_w(s,a)` đánh giá action/state.

Actor học từ feedback của critic; critic học dự đoán long-term return.

```text
state
→ Actor chooses action
→ environment gives reward/next state
→ Critic computes TD/advantage signal
→ update Critic
→ update Actor
```

## Vì sao cần Critic?

REINFORCE dùng full Monte Carlo return nên variance cao. Critic bootstrap value estimate để tạo lower-variance learning signal.

Một one-step TD error:

\[
\delta_t=R_{t+1}+\gamma V_w(S_{t+1})-V_w(S_t)
\]

có thể dùng như approximate advantage cho actor:

\[
\theta\leftarrow\theta+\alpha\delta_t\nabla_\theta\log\pi_\theta(A_t|S_t)
\]

## Actor Objective

Actor muốn tăng expected return. Critic cung cấp estimate action tốt hơn baseline bao nhiêu.

Nếu `δ_t>0`, action tốt hơn expected → tăng probability.

Nếu `δ_t<0`, action tệ hơn expected → giảm probability.

## Critic Objective

Critic minimize value prediction error, ví dụ:

\[
L_V=(R+\gamma V_w(s')-V_w(s))^2
\]

Actor và critic learning targets thay đổi cùng nhau, tạo coupled optimization dynamics.

## On-Policy Actor-Critic

A2C/A3C family sử dụng on-policy trajectories. Advantage estimate từ critic giảm variance so với pure Monte Carlo.

## Off-Policy Actor-Critic

Algorithms như DDPG, TD3, SAC learn from replay buffers.

Actor có thể optimize:

\[
\max_\theta Q_w(s,\pi_\theta(s))
\]

trong continuous action problems.

## DDPG Intuition

**Deep Deterministic Policy Gradient (DDPG)** dùng deterministic actor cho continuous action, critic Q-function, replay buffer và target networks.

Nhưng DDPG sensitive/stability issues; TD3 cải thiện bằng clipped double critics, delayed policy updates và target smoothing.

## Soft Actor-Critic

**SAC** maximize return + entropy:

\[
J(\pi)=\mathbb E\left[\sum_t \gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

Entropy encourage exploration và robustness. SAC là strong off-policy method cho continuous control.

## Shared vs Separate Networks

Actor/critic có thể share representation trunk rồi tách heads, hoặc independent networks.

Shared network tiết kiệm compute và representation, nhưng gradients từ policy/value objectives có thể interfere.

## Critic Bias

Nếu critic systematically wrong, actor optimize against wrong landscape. This is analogous reward-model exploitation: actor can exploit critic error.

Double critics và conservative updates help.

## Advantage Estimation

Critic enables:

\[
A(s,a)=Q(s,a)-V(s)
\]

or GAE estimates. Advantage removes state difficulty baseline: action judged relative to what is normally achievable from state.

## Two Timescales

Actor và critic learning rates ảnh hưởng stability. Critic cần track policy enough; actor không nên outrun critic too much.

## Target Networks

Off-policy critics often use slow target networks to stabilize bootstrap target, giống DQN.

## Replay Buffer

Off-policy actor-critic reuse transitions. Need handle distribution mismatch, stale data and exploration coverage.

## Continuous Action Boundaries

Actor output thường squashed with `tanh` then scaled to action bounds. Probability correction needed for stochastic policy log-probs after transformation in SAC-like methods.

## Partial Observability

Actor/critic có thể use recurrent state/transformer memory when observation not Markov.

## Multi-Agent Actor-Critic

Centralized critic can observe joint information during training while decentralized actors act from local observations at execution. Đây là common multi-agent RL paradigm.

## Example: Robot Control

State includes joint positions/velocities; actor outputs motor torques; critic estimates future return. Continuous high-dimensional actions make Q-table impossible, actor provides direct control mapping.

## Actor-Critic và LLM

RLHF with PPO conceptually has policy actor and learned reward/value components. But LLM action space and sequence generation make implementation specialized.

## Failure Modes

- critic divergence;
- actor exploits critic errors;
- insufficient exploration;
- value overestimation;
- unstable entropy coefficient;
- replay distribution mismatch;
- reward scale problems.

## Mental Model

> **Actor nói “tôi sẽ làm gì”; Critic nói “lựa chọn đó tốt hơn kỳ vọng bao nhiêu”.**

## Common Misconceptions

### “Critic là một human reviewer”

Không. Critic trong RL là learned value/Q estimator, dù external evaluators có thể provide reward.

### “Actor-Critic luôn on-policy”

Có cả on-policy và off-policy families.

### “Critic chính xác tuyệt đối”

Critic cũng là learned approximator và có bias/error.

## Knowledge Connection

Actor-Critic kết hợp value-based và policy-based RL, là bridge trực tiếp sang Deep Reinforcement Learning.

Xem tiếp: [Deep Reinforcement Learning](./09_deep_reinforcement_learning.md).