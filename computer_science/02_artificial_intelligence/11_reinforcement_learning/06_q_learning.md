# Q-Learning

**Q-learning (Q 러닝)** là model-free, off-policy Temporal Difference control algorithm học approximation của optimal action-value function:

\[
Q^*(s,a)
\]

Core update:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\right]
\]

## Vì sao Q-learning mạnh?

Agent có thể behave exploratory nhưng target update toward greedy policy. Đây là off-policy distinction:

```text
behavior policy → generates data
optimal greedy target → drives learning
```

Với sufficient exploration và standard tabular assumptions, Q-learning converge tới `Q*`.

## Greedy Policy từ Q

Nếu Q đã tốt:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

Không cần explicit transition model để chọn action.

## Exploration

Nếu luôn greedy từ random initial Q, agent có thể không discover good actions. Epsilon-greedy:

```text
random action with ε
argmax Q otherwise
```

`ε` có thể decay theo time, nhưng decay quá nhanh dẫn tới insufficient exploration.

## Off-Policy Target

Q-learning target:

\[
y=R+\gamma\max_{a'}Q(s',a')
\]

không depend on action behavior policy thực sự chọn ở next step. Vì vậy agent có thể learn greedy target while behaving exploratory.

## SARSA Contrast

SARSA target:

\[
R+\gamma Q(s',a'_{behavior})
\]

Trong risky environment, SARSA có thể learn safer path under exploratory behavior vì nó accounts possibility of exploratory mistakes. Q-learning learns value of ideal greedy continuation.

## Tabular Limit

Table size:

\[
|S|\times|A|
\]

không feasible cho images/continuous states. Function approximation leads to Deep Q-Networks.

## Overestimation Bias

`max` over noisy estimates tends to select positive noise. Double Q-learning separates action selection and evaluation to reduce bias.

## Experience Replay

Deep Q-learning stores transitions:

```text
(s,a,r,s',done)
```

in replay buffer and samples mini-batches.

Benefits:

- breaks temporal correlation;
- reuses data;
- improves hardware batching.

But replay distribution may differ from current policy; this is compatible with off-policy learning but creates prioritization/staleness concerns.

## Target Network

If same network both defines target and is updated every gradient step, target moves rapidly.

DQN keeps slowly updated/frozen target network:

\[
y=r+\gamma\max_{a'}Q_{\theta^-}(s',a')
\]

then optimize online network `Q_θ` toward target.

Target network stabilizes bootstrapping.

## DQN Loss

\[
L(\theta)=\mathbb E[(y-Q_\theta(s,a))^2]
\]

or Huber loss often used for robustness.

## Terminal Transitions

If transition ends episode:

\[
y=r
\]

No bootstrap from terminal next state.

Incorrect handling `done` can bias learning.

## Reward Clipping

Some classic deep RL systems clip rewards for stability, but this changes objective by discarding magnitude information. Engineering trick must be understood as objective transformation.

## Continuous Actions

`max_a Q(s,a)` difficult when action continuous high-dimensional. Actor-critic methods learn explicit policy to produce action, avoiding exhaustive argmax.

## Q-learning và Planning Analogy

Q value acts like cached long-term action utility. Classical planning computes consequence from model; Q-learning learns it from experience.

## Example

Suppose:

```text
Q(s,a)=2
r=1
max Q(s',·)=5
γ=0.9
α=0.1
```

Target:

\[
1+0.9\times5=5.5
\]

Error:

\[
3.5
\]

Update:

\[
Q(s,a)=2+0.1\times3.5=2.35
\]

## Distribution Shift in Replay

Old buffer transitions may come from obsolete policies. Too-old data can slow adaptation; too-recent-only data reduces diversity. Replay design is a data-engineering problem inside RL.

## Offline Q-Learning Risk

If dataset lacks certain actions, max may exploit overestimated unseen actions. Conservative offline RL methods penalize out-of-distribution action values.

## Mental Model

> **Q-learning học “nếu ở state này và làm action này, long-term return tốt nhất có thể từ đó là bao nhiêu?”.**

## Common Misconceptions

### “Q-learning cần biết environment model”

Không; nó học from transitions.

### “Off-policy nghĩa là agent không cần exploration”

Vẫn cần data coverage cho relevant state-actions.

### “DQN chỉ là Q-table bằng neural network”

Function approximation thêm instability; replay/target networks là critical system changes.

## Knowledge Connection

Q-learning nối TD bootstrapping với Deep Learning. Policy-gradient methods tiếp cận control trực tiếp bằng optimizing policy distribution thay vì argmax trên Q.

Xem tiếp: [Policy Gradient](./07_policy_gradient.md).