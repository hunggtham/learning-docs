# Reinforcement Learning Foundations

**Reinforcement Learning (RL / 강화학습 / học tăng cường)** nghiên cứu cách một agent học cách hành động qua interaction với environment để tối đa hóa reward tích lũy theo thời gian. Khác supervised learning, agent thường không nhận “đáp án đúng” cho từng action; nó nhận consequences và reward, đôi khi delayed nhiều bước.

```text
state s_t
→ agent chooses action a_t
→ environment transitions to s_{t+1}
→ reward r_{t+1}
→ repeat
```

## Vì sao RL khác supervised learning?

Supervised learning có dataset tương đối cố định `(x,y)`. RL có ba complication:

1. data distribution phụ thuộc policy hiện tại;
2. reward có thể delayed;
3. agent phải cân bằng exploration và exploitation.

Nếu agent chọn action khác, nó sẽ thấy data khác.

## Reward và Return

Reward `r_t` là feedback tại một thời điểm. Objective thường là expected discounted return:

\[
G_t = r_{t+1}+\gamma r_{t+2}+\gamma^2 r_{t+3}+\cdots
\]

với discount factor:

\[
0\le \gamma <1
\]

`γ` điều khiển trade-off giữa reward gần và xa, đồng thời giúp infinite-horizon sum hội tụ trong nhiều setting.

## Policy

Policy mô tả cách agent chọn action:

\[
\pi(a\mid s)
\]

Deterministic policy có thể viết `a=π(s)`; stochastic policy trả distribution.

## Value

State-value:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s]
\]

Action-value:

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]
\]

Value không phải immediate reward; nó ước lượng long-term consequence.

## Model-Free vs Model-Based

**Model-based RL** sử dụng/học transition/reward model để plan.

**Model-free RL** học policy/value trực tiếp từ experience mà không cần explicit environment model.

Hai approach có thể kết hợp.

## Exploration vs Exploitation

Agent phải chọn giữa:

- exploitation: dùng action currently estimated best;
- exploration: thử action để thu information.

Nếu chỉ exploit sớm, agent có thể kẹt với policy suboptimal.

Epsilon-greedy:

```text
with probability ε: random action
otherwise: argmax Q(s,a)
```

là strategy đơn giản, không phải universally best.

## On-Policy vs Off-Policy

On-policy học về policy đang generate data. Off-policy có thể học target policy khác behavior policy.

Q-learning là classic off-policy method. SARSA là on-policy.

## Credit Assignment

Nếu reward cuối episode tốt, action nào trước đó deserve credit? Đây là temporal credit-assignment problem.

Bellman methods, TD learning và policy gradients đưa ra các cách khác nhau để propagate signal backward qua time.

## Reward Specification

Reward là mathematical proxy cho goal. Nếu proxy sai, agent có thể optimize theo cách không mong muốn — **reward hacking/specification gaming**.

Ví dụ robot được reward “di chuyển nhanh” nhưng không penalize va chạm có thể học behavior dangerous.

## Sparse Reward

Nếu chỉ có reward ở cuối long task, learning signal rất yếu. Reward shaping thêm intermediate signal nhưng có thể distort objective nếu design kém.

## Episodes và Continuing Tasks

Episodic task có terminal state, như game. Continuing task chạy indefinite, như process control.

## Partial Observability

Nếu observation không đủ xác định true state, problem trở thành POMDP-like. Agent có thể cần memory/belief state.

## Offline RL

Offline/batch RL học từ fixed logged dataset mà không tương tác thêm environment. Khó vì policy mới có thể chọn actions ngoài data support, khiến value extrapolation unreliable.

## RL và LLM Alignment

RL xuất hiện trong alignment như RLHF, nhưng LLM post-training có đặc thù: action có thể là whole sequence/token decisions, reward đến từ preference model/human signal, và reference-policy constraints quan trọng.

Không nên equate toàn bộ RL với RLHF.

## Mental Model

> **Supervised learning hỏi “output nào đúng cho input này?”, RL hỏi “chuỗi action nào tạo long-term consequence tốt?”**

## Common Misconceptions

### “Reward = mục tiêu thật”

Reward chỉ là encoded objective. Nếu encoding thiếu, optimizer có thể exploit gap.

### “RL luôn cần robot/game”

RL áp dụng mọi sequential decision problem có feedback.

### “More exploration luôn tốt”

Exploration có cost/risk; real systems cần safe exploration.

## Knowledge Connection

RL nối [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md), [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), Probability và Optimization.

Xem tiếp: [Markov Decision Processes](./01_markov_decision_processes.md).