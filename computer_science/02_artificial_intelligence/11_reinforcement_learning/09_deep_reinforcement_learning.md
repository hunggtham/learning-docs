# Deep Reinforcement Learning

**Deep Reinforcement Learning (Deep RL / 심층 강화학습)** kết hợp Reinforcement Learning với neural networks để xử lý state/action spaces quá lớn cho tabular methods. Neural network đóng vai trò function approximator cho value, Q-function, policy hoặc environment model.

```text
pixels / sensors / embeddings
        ↓
 neural representation
        ↓
Q-value / policy / value / model
        ↓
RL objective
```

## Vì sao Deep RL khó hơn supervised deep learning?

Supervised learning thường train trên dataset tương đối stationary. Trong RL:

- policy thay đổi → data distribution thay đổi;
- targets có thể bootstrap từ network itself;
- rewards delayed/sparse;
- exploration determines future data;
- samples temporally correlated;
- objective non-stationary.

Vì vậy neural network capacity không tự giải quyết RL; nó còn tạo stability problems mới.

## DQN: Deep Q-Network

DQN approximates:

\[
Q(s,a;\theta)
\]

với neural network. Input có thể là image, output là Q-value cho each discrete action.

Key engineering ideas:

1. **experience replay**;
2. **target network**;
3. reward/gradient stabilization.

Loss:

\[
L(\theta)=\mathbb E[(r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta))^2]
\]

## Why Replay Matters

Sequential frames/states highly correlated. SGD assumes batches useful when samples not all nearly identical. Replay randomizes historical transitions and reuses expensive experience.

Prioritized replay samples high-TD-error transitions more often, but needs importance correction to reduce sampling bias.

## Target Networks

Moving target problem:

```text
network changes
→ target changes
→ network chases own changing prediction
```

Frozen/slow target network reduces feedback instability.

## Double DQN

Reduce max overestimation by selecting action with online network, evaluating it with target network:

\[
a^*=\arg\max_a Q(s',a;\theta)
\]

\[
y=r+\gamma Q(s',a^*;\theta^-)
\]

## Dueling Networks

Decompose:

\[
Q(s,a)=V(s)+A(s,a)
\]

with normalization to make decomposition identifiable. Useful when many actions have similar effect from a state.

## Policy-Based Deep RL

Policy network directly outputs action distribution. PPO, SAC and actor-critic methods scale naturally to continuous/high-dimensional action spaces.

## Representation Learning in RL

RL agent must learn not just control but useful state representations. Reward signal may be sparse, so representation learning can be data-inefficient.

Auxiliary/self-supervised objectives can help learn dynamics/relevant features.

## World Models

Model-based Deep RL learns environment dynamics:

\[
\hat s_{t+1}=f_\phi(s_t,a_t)
\]

or latent dynamics, then plans/improves policy using learned model.

Benefits: potential sample efficiency.

Risk: **model bias**. Planning can exploit model errors, especially far outside training distribution.

## Imagination and Latent Planning

Instead of simulating raw pixels, world-model agents can learn latent state `z_t` and predict latent transitions/rewards. Planning in latent space reduces cost if representation preserves control-relevant information.

## Exploration in High Dimensions

Random action exploration is inefficient when rewards sparse. Methods include:

- intrinsic motivation;
- curiosity/prediction error;
- count/pseudo-count bonuses;
- entropy maximization;
- uncertainty-driven exploration.

But intrinsic rewards can be gamed: agent may seek noisy unpredictable states forever.

## Sparse Reward and Hindsight

Hindsight Experience Replay relabels failed trajectories with goals they actually achieved, creating useful learning signal for goal-conditioned tasks.

## Distribution Shift

Policy improvement moves agent into new state distributions where function approximator may be poorly trained. This feedback loop is central RL risk.

## Sim-to-Real

Robotics often train in simulation then deploy physical system. Simulation mismatch causes transfer gap.

Techniques:

- domain randomization;
- system identification;
- fine-tuning with real data;
- safety constraints.

## Offline Deep RL

Learn from logged data only. Main challenge: policy may choose out-of-distribution actions whose Q-values are extrapolation errors.

Offline RL methods constrain policy near data support or learn conservative value estimates.

## Safe RL

Objective may include constraints:

\[
\max_\pi \mathbb E[G] \quad \text{s.t.}\quad \mathbb E[C_i]\le d_i
\]

where `C_i` are costs/risks. Real systems cannot freely explore catastrophic actions.

## Multi-Agent Deep RL

Multiple learning agents make environment non-stationary from each agent's perspective. Centralized training/decentralized execution is common strategy.

## Deep RL Evaluation

Single seed result unreliable. Need multiple random seeds and confidence intervals because training variance high.

Also report:

- sample efficiency;
- final return;
- stability;
- compute/environment steps;
- safety violations;
- generalization to changed environments.

## Reward Hacking

Strong optimizer finds loopholes. Example agent gets reward for touching checkpoints and learns loop around same reward trigger if environment allows. This demonstrates specification problem, not “malice”.

## Deep RL and Games

Games useful research environments because rules/rewards/simulation cheap, but success in games does not automatically transfer to open world where reward and state definitions are ambiguous.

## RLHF / LLM Post-Training

Deep RL techniques like PPO have been used for language-model alignment. Important differences:

- policy action is token sequence;
- pretrained policy already powerful;
- reward model learned from preferences;
- KL/reference constraints keep behavior near base/SFT model;
- online environment often human/preference proxy, not physics simulator.

Modern preference optimization may avoid full RL loop in some pipelines, but RL concepts remain useful for understanding policy optimization.

## The Deadly Triad Revisited

Deep RL frequently combines:

```text
function approximation
+ bootstrapping
+ off-policy data
```

Hence stabilizers are not incidental hacks; they address structural instability.

## Compute and Reproducibility

Deep RL experiments depend strongly on seeds, environment versions, wrappers, reward preprocessing and evaluation policy. Reproducibility requires versioning entire environment pipeline, not model code alone.

## Mental Model

> **Deep RL không chỉ là “neural network + reward”; nó là feedback system nơi model quyết định data nào nó sẽ thấy tiếp theo.**

Đây là khác biệt sâu với ordinary supervised learning.

## Common Misconceptions

### “Deep RL là con đường chung để tạo intelligence”

Nó mạnh cho sequential decision problems nhưng sample cost, reward specification và safety make it unsuitable for many tasks.

### “Simulation success nghĩa real-world success”

Sim-to-real gap có thể lớn.

### “Reward cao chứng minh behavior tốt”

Only if reward faithfully measures intended behavior and environment has no loopholes.

### “Bigger neural network fixes RL instability”

Optimization/data feedback instability vẫn tồn tại.

## Knowledge Connection

Deep RL nối [Neural Networks](../05_neural_networks/README.md), MDP/Bellman theory, Optimization, Agents và Safety. Đây là điểm kết thúc RL foundation; các later safety/alignment chapters sẽ quay lại reward specification, policy constraints và evaluation.