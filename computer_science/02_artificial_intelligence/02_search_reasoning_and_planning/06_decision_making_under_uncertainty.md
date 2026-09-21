# Decision Making Under Uncertainty

Classical search và deterministic planning giả định action dẫn tới successor state khá rõ ràng. Real world hiếm khi như vậy. Sensor noisy, action có thể fail, user behavior stochastic, future demand unknown, và ta thường không quan sát đầy đủ hidden state.

**Decision Making Under Uncertainty (불확실성 하의 의사결정)** hỏi:

> Khi không biết chắc state hoặc outcome, action nào nên chọn nếu mỗi outcome có probability và consequence khác nhau?

Đây là nơi Probability, Utility, Planning và Reinforcement Learning bắt đầu gặp nhau.

Xem trước: [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Planning](./05_planning.md).

## Probability chưa đủ để ra quyết định

Suppose model predicts:

\[
P(fraud\mid x)=0.20
\]

Có block transaction không?

Probability một mình không trả lời. Cần cost/utility:

- false block làm mất customer trust;
- missed fraud mất money;
- manual review có cost và capacity.

Decision Theory tách hai components:

```text
belief about what may happen
        +
value/cost of consequences
        ↓
action choice
```

## Utility

Utility function:

\[
U(o)
\]

gán value cho outcome `o`.

Nếu action `a` có possible outcomes `o`:

\[
EU(a)=\sum_o P(o\mid a)U(o)
\]

Expected Utility principle chọn:

\[
a^*=\arg\max_a EU(a)
\]

Điều này không nói utility phải là money. Nó có thể encode safety, time, satisfaction hoặc combination.

## Cost-sensitive classification

Binary decision có cost matrix:

| Actual / Action | Predict Negative | Predict Positive |
|---|---:|---:|
| Negative | 0 | `C_FP` |
| Positive | `C_FN` | 0 |

Nếu calibrated probability positive là `p`, choose positive khi expected cost thấp hơn.

Expected cost predict positive:

\[
(1-p)C_{FP}
\]

Expected cost predict negative:

\[
pC_{FN}
\]

Choose positive if:

\[
(1-p)C_{FP}<pC_{FN}
\]

which implies threshold:

\[
p>\frac{C_{FP}}{C_{FP}+C_{FN}}
\]

Threshold 0.5 only natural when costs symmetric.

## Risk neutrality vs risk sensitivity

Expected value alone corresponds to risk-neutral treatment of numerical payoff under linear utility.

Humans/businesses may be risk-averse. Losing $100k with 1% probability can matter differently from expected $1k loss due to tail risk, regulation or survival constraints.

Concave utility models diminishing marginal value:

\[
U(\mathbb{E}[X])\ge\mathbb{E}[U(X)]
\]

for concave `U` via Jensen's inequality.

AI systems may need explicit risk measures rather than average reward only.

## Value of information

Information is useful if it can change decision enough to improve expected utility.

**Expected Value of Perfect Information (EVPI)** roughly compares:

\[
\mathbb{E}[\max_a U(a,\theta)]
-
\max_a \mathbb{E}[U(a,\theta)]
\]

It bounds how much one should pay for perfect information about uncertain variable `θ`.

Practical example: should medical AI request another test before recommending action? Test is valuable only if expected decision improvement exceeds test cost/delay.

## Sequential decisions

One-shot expected utility is insufficient when actions affect future states.

State `s_t`, action `a_t`, next state `s_{t+1}`.

Action changes both immediate reward and future opportunities.

This leads to **Markov Decision Process (MDP / 마르코프 결정 과정)**.

## Markov property

A process is Markov if current state contains enough information that future conditional distribution does not depend on full history:

\[
P(s_{t+1}\mid s_t,a_t,s_{t-1},...)=P(s_{t+1}\mid s_t,a_t)
\]

This is property of chosen state representation, not magical property of world.

If state omits relevant history, Markov assumption fails.

Example: if machine failure probability depends on accumulated usage but state stores only current temperature, state is insufficient.

## MDP components

An MDP typically:

\[
\mathcal{M}=(S,A,P,R,\gamma)
\]

where:

- `S`: states;
- `A`: actions;
- `P(s'|s,a)`: transition probabilities;
- `R(s,a,s')`: reward;
- `γ`: discount factor.

A **policy**:

\[
\pi(a\mid s)
\]

maps state to action distribution.

Goal: find policy maximizing expected return.

## Return

Discounted return:

\[
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\]

`0≤γ<1` often ensures finite sum and weights near rewards more.

Discounting can represent time preference, uncertainty about continuation or mathematical convenience. Interpretation depends domain.

For finite horizon, discount may be unnecessary.

## State value

Value of policy `π`:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid s_t=s]
\]

It answers:

> Nếu bắt đầu ở state này và tiếp tục theo policy π, expected long-term return là bao nhiêu?

## Action value

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid s_t=s,a_t=a]
\]

It evaluates taking action `a` first, then following `π`.

Decision:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

if deterministic greedy policy desired.

## Bellman equation

Value decomposes recursively:

\[
V^\pi(s)=\sum_a\pi(a\mid s)
\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma V^\pi(s')]
\]

Bellman equation states:

```text
value now
= expected immediate reward
+ discounted expected value later
```

This recursion is one of most important structures in Reinforcement Learning.

## Bellman optimality

Optimal value:

\[
V^*(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma V^*(s')]
\]

Optimal Q:

\[
Q^*(s,a)=\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma\max_{a'}Q^*(s',a')]
\]

This is stochastic generalization of shortest-path dynamic programming.

## Value iteration

Initialize `V_0`. Repeatedly apply Bellman optimality backup:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R+\gamma V_k(s')]
\]

Under discounted finite MDP conditions, contraction property gives convergence to `V*`.

Then derive policy by greedy action selection.

## Policy iteration

Alternate:

1. **Policy evaluation** — compute `V^π`.
2. **Policy improvement** — choose action better according to current values.

Repeat until policy stable.

Policy iteration can converge in fewer outer iterations but evaluation step costly.

## Search vs MDP

Deterministic shortest path can be seen as special case where transition probability concentrated on one successor.

Search node cost-to-go resembles negative value.

A* heuristic approximates remaining cost; RL value function approximates expected future return.

Connection:

```text
heuristic h(s)       ↔ estimated cost-to-go
value V(s)           ↔ expected return-to-go
```

Signs/objectives differ, but structural role similar.

## Unknown transition model

Classical MDP planning assumes `P` and `R` known.

Reinforcement Learning begins when environment model unknown or too expensive, and agent learns value/policy from experience.

Thus:

```text
known model + optimize policy → planning in MDP
unknown model + experience    → RL
```

Model-based RL learns/estimates model; model-free RL learns value/policy without explicit transition model.

## Partial observability

If agent cannot observe state `s`, it receives observation `o`.

A **POMDP (부분 관찰 마르코프 결정 과정)** adds observation model.

Agent maintains belief:

\[
b(s)=P(s\mid history)
\]

Belief state is a probability distribution over possible states.

POMDP can be transformed conceptually into MDP over belief space, but belief space continuous/high-dimensional and difficult.

## Belief update

After action `a` and observation `o`, Bayesian filtering updates belief:

\[
b'(s')\propto P(o\mid s')\sum_s P(s'\mid s,a)b(s)
\]

Two steps:

```text
predict next state distribution
        ↓
condition on new observation
```

This is Bayes theorem operating sequentially.

## State estimation

Kalman Filter solves linear-Gaussian state estimation efficiently.

Hidden state dynamics:

\[
x_t=Ax_{t-1}+Bu_t+w_t
\]

Observation:

\[
z_t=Hx_t+v_t
\]

with Gaussian noises.

Extended/Unscented Kalman variants handle nonlinear approximations; particle filters use samples for more general distributions.

Robotics perception/control relies heavily on state estimation before planning.

## Decision under model uncertainty

Even if environment stochasticity known, model parameters themselves may be uncertain.

Bayesian decision making integrates over posterior:

\[
EU(a)=\int U(a,\theta)p(\theta\mid D)d\theta
\]

In practice exact integration often intractable, requiring approximation.

Ignoring epistemic uncertainty can make system overconfident out-of-distribution.

## Robust decision making

Instead of trust one estimated distribution, robust optimization considers set of possible models:

\[
\max_\pi \min_{P\in\mathcal{P}} J(\pi,P)
\]

This protects worst-case within uncertainty set but may be conservative.

Distributionally Robust Optimization similarly optimizes against distributions near empirical one according to chosen distance/divergence.

## Chance constraints

Constraint may need hold with high probability:

\[
P(g(x,\xi)\le0)\ge1-\alpha
\]

Example autonomous system: collision-risk constraint < threshold.

Chance constraints convert uncertainty into probabilistic safety requirements, but require trustworthy uncertainty model.

## CVaR and tail risk

Expected loss can hide catastrophic tail.

Value-at-Risk gives quantile; Conditional Value-at-Risk (CVaR) averages losses beyond tail threshold under definitions.

Risk-sensitive RL can optimize CVaR-like objectives when rare catastrophic outcomes matter more than mean performance.

## Exploration vs exploitation

When action outcomes uncertain because we have not tried them, action has two values:

1. immediate reward;
2. information gained for future decisions.

Multi-armed bandit captures this simplest setting.

Each arm has unknown reward distribution. Agent chooses whether exploit best-known arm or explore uncertain arm.

This is sequential Value of Information.

## Multi-Armed Bandit

Suppose arm `a` has unknown mean `μ_a`.

Regret after `T` steps:

\[
R_T=T\mu^*-\sum_{t=1}^{T}\mu_{a_t}
\]

Goal minimize regret rather than simply maximize immediate observed reward.

Algorithms include ε-greedy, UCB, Thompson Sampling.

Bandits are relevant for recommendation, ads and online experimentation.

## Upper Confidence Bound

UCB chooses:

\[
a_t=\arg\max_a\left[\hat\mu_a+c\sqrt{\frac{\ln t}{N_a}}\right]
\]

First term exploitation. Second optimism under uncertainty: less-tried arms get exploration bonus.

This idea also appeared in MCTS selection.

## Thompson Sampling

Maintain posterior over each arm parameter. Sample one parameter from posterior and act greedily under sampled world.

Uncertain arms get naturally explored because posterior wide.

It converts Bayesian uncertainty into stochastic action selection.

## Contextual bandits

Recommendation depends user/context `x`:

\[
P(r\mid x,a)
\]

Choose action based on context, observe reward only for chosen action.

This introduces **partial feedback**: we do not see what reward unchosen recommendations would have produced.

Counterfactual evaluation becomes important.

## Off-policy evaluation

If logs generated by behavior policy `μ`, want estimate target policy `π` without deploying.

Importance sampling idea weights observations:

\[
w=\frac{\pi(a\mid s)}{\mu(a\mid s)}
\]

Under assumptions, reweight behavior data to target distribution.

But high variance when target chooses actions behavior rarely chose.

This connects Statistics, Causal Inference and RL evaluation.

## Reward design

Reward is not reality. It is a proxy signal.

If optimize engagement clicks, agent may learn behavior increasing short-term clicks but harming long-term satisfaction.

Sequential optimization amplifies reward misspecification because policy actively changes future data/state.

This is direct bridge to AI Alignment.

## Delayed consequences

Action may have low immediate reward but high long-term value.

Example server autoscaling: spinning instance costs now but avoids outage later.

Myopic decision maximizing immediate reward fails.

Bellman recursion handles delayed consequences by future value.

## Credit assignment

If reward arrives after long action sequence, which earlier actions deserve credit?

This is core RL difficulty.

Temporal Difference learning propagates value backward over experience rather than wait only final outcome.

LLM agent evaluation also faces credit assignment: task success/failure after 20 tool calls does not directly identify which decision caused outcome.

## Planning under uncertainty for agents

Tool agent may face:

```text
API may fail
search results incomplete
user intent partially specified
external state changes
```

Reliable pattern:

```text
belief/state estimate
    ↓
choose low-risk informative action
    ↓
observe result
    ↓
update state
    ↓
continue/replan
```

Sometimes best next action is asking for missing information rather than committing to plan.

## Irreversible actions

Actions like payment, deletion, sending message or deploying code have high downside.

Decision system should distinguish reversible vs irreversible actions.

Possible policy:

```text
low-risk reversible → autonomous
high-risk irreversible → stronger validation / confirmation
```

This is utility/risk-aware planning, not just UX convention.

## Model uncertainty vs environment randomness

Recall:

- **aleatoric uncertainty**: inherent stochasticity;
- **epistemic uncertainty**: ignorance/model uncertainty.

Decision strategy differs. More data may reduce epistemic uncertainty but not irreducible noise.

Exploration targets epistemic uncertainty; robust policy protects against uncertain model; risk-sensitive utility handles consequence structure.

## Expected utility is not morality

Encoding utility requires deciding whose outcomes count and how trade-offs measured. Mathematics optimizes provided utility; it does not define ethical values.

For social/high-impact AI, utility model, fairness constraints and governance are normative design choices requiring human institutions.

## Mental Model

```text
Probability = what may happen?
Utility     = how much do outcomes matter?
Policy      = what action to take in each state/belief?
Value       = expected future utility from here
MDP         = sequential decisions with stochastic transitions
POMDP       = state partially hidden; reason with beliefs
Exploration = act partly to learn
Risk        = care about distribution/tails, not mean only
```

## Common Misconceptions

### “Highest probability outcome should determine action”

Decision depends consequences. Low-probability catastrophic event can dominate expected/risk-sensitive choice.

### “MDP state is just current observation”

State must be Markov-sufficient. Observation may be partial.

### “Expected reward maximum means safest policy”

Not necessarily. Mean objective can tolerate rare catastrophic loss unless risk encoded.

### “RL begins whenever there is an agent”

If transition/reward model known and policy solved by DP, it is planning in an MDP. RL specifically learns from interaction/data when relevant model/value/policy unknown.

## Knowledge Connection

Decision Making Under Uncertainty completes bridge from Classical Search/Planning to Reinforcement Learning. Search handles deterministic alternatives; MDP adds stochastic transitions and long-term value; POMDP adds hidden state; RL learns behavior when model/value unknown.

Sau phần Knowledge Representation và Machine Learning, library sẽ quay lại MDP/Bellman equations sâu hơn trong `11_reinforcement_learning/`.