# Quyết định (decision / 결정) Making Under bất định (uncertainty / 불확실성)

> **Mạch đọc:** Đặt **quyết định (decision / 결정) Making Under bất định (uncertainty / 불확실성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **xác suất (probability / 확률) chưa đủ để ra quyết định** sang **Utility**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Classical tìm kiếm (search / 검색) và deterministic planning giả định hành động (action / 동작) dẫn tới successor trạng thái (state / 상태) khá rõ ràng. Real world hiếm khi như vậy. Sensor noisy, hành động (action / 동작) có thể thất bại (fail / 실패), người dùng (user / 사용자) hành vi (behavior / 동작) stochastic, future demand unknown, và ta thường không quan sát đầy đủ hidden trạng thái (state / 상태).

**quyết định (decision / 결정) Making Under bất định (uncertainty / 불확실성)** hỏi:

> Khi không biết chắc trạng thái (state / 상태) hoặc kết quả (outcome / 결과), hành động (action / 동작) nào nên chọn nếu mỗi kết quả (outcome / 결과) có xác suất (probability / 확률) và consequence khác nhau?

Đây là nơi xác suất (probability / 확률), Utility, Planning và Reinforcement học tập (learning / 학습) bắt đầu gặp nhau.

Xem trước: [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Planning](./05_planning.md).

## Xác suất (probability / 확률) chưa đủ để ra quyết định

Suppose mô hình (model / 모델) predicts:

\[
P(fraud\mid x)=0.20
\]

Có khối (block / 블록) giao dịch (transaction / 트랜잭션) không?

Xác suất (probability / 확률) một mình không trả lời. Cần chi phí (cost / 비용)/utility:

- false khối (block / 블록) làm mất customer trust;
- missed fraud mất money;
- manual rà soát (review / 검토) có chi phí (cost / 비용) và sức chứa (capacity / 용량).

Quyết định (decision / 결정) lý thuyết (theory / 이론) tách hai components:

```text
belief about what may happen
        +
value/cost of consequences
        ↓
action choice
```

## Utility

Utility hàm (function / 함수):

\[
U(o)
\]

gán giá trị (value / 값) cho kết quả (outcome / 결과) `o`.

Nếu hành động (action / 동작) `a` có possible outcomes `o`:

\[
EU(a)=\sum_o P(o\mid a)U(o)
\]

Expected Utility principle chọn:

\[
a^*=\arg\max_a EU(a)
\]

Điều này không nói utility phải là money. Nó có thể encode an toàn (safety / 안전), thời gian (time / 시간), satisfaction hoặc combination.

## Cost-sensitive classification

Nhị phân (binary / 이진) quyết định (decision / 결정) có chi phí (cost / 비용) ma trận (matrix / 행렬):

| Actual / hành động (action / 동작) | Predict Negative | Predict Positive |
|---|---:|---:|
| Negative | 0 | `C_FP` |
| Positive | `C_FN` | 0 |

Nếu calibrated xác suất (probability / 확률) positive là `p`, choose positive khi expected chi phí (cost / 비용) thấp hơn.

Expected chi phí (cost / 비용) predict positive:

\[
(1-p)C_{FP}
\]

Expected chi phí (cost / 비용) predict negative:

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

## Rủi ro (risk / 위험) neutrality vs rủi ro (risk / 위험) sensitivity

Expected giá trị (value / 값) alone corresponds to risk-neutral treatment of numerical payoff under tuyến tính (linear / 선형) utility.

Humans/businesses may be risk-averse. Losing $100k with 1% xác suất (probability / 확률) can matter differently from expected $1k mất mát (loss / 손실) due to tail rủi ro (risk / 위험), regulation or survival các ràng buộc (constraints / 제약조건들).

Concave utility các mô hình (models / 모델들) diminishing marginal giá trị (value / 값):

\[
U(\mathbb{E}[X])\ge\mathbb{E}[U(X)]
\]

for concave `U` via Jensen's inequality.

AI các hệ thống (systems / 시스템들) may need tường minh (explicit / 명시적) rủi ro (risk / 위험) measures rather than average reward only.

## Giá trị (value / 값) of thông tin (information / 정보)

Thông tin (information / 정보) is useful if it can thay đổi (change / 변경) quyết định (decision / 결정) enough to improve expected utility.

**Expected giá trị (value / 값) of Perfect thông tin (information / 정보) (EVPI)** roughly compares:

\[
\mathbb{E}[\max_a U(a,\theta)]
-
\max_a \mathbb{E}[U(a,\theta)]
\]

It bounds how much one should pay for perfect thông tin (information / 정보) about uncertain variable `θ`.

Practical example: should medical AI yêu cầu (request / 요청) another kiểm thử (test / 테스트) before recommending hành động (action / 동작)? kiểm thử (test / 테스트) is valuable only if expected quyết định (decision / 결정) improvement exceeds kiểm thử (test / 테스트) chi phí (cost / 비용)/delay.

## Sequential decisions

One-shot expected utility is insufficient when actions affect future states.

Trạng thái (state / 상태) `s_t`, hành động (action / 동작) `a_t`, next trạng thái (state / 상태) `s_{t+1}`.

Hành động (action / 동작) changes both immediate reward and future opportunities.

This leads to **Markov quyết định (decision / 결정) tiến trình (process / 프로세스)**.

## Markov thuộc tính (property / 속성)

A tiến trình (process / 프로세스) is Markov if trạng thái hiện tại (current state / 현재 상태) contains enough thông tin (information / 정보) that future conditional phân phối (distribution / 분포) does not depend on full lịch sử (history / 이력):

\[
P(s_{t+1}\mid s_t,a_t,s_{t-1},...)=P(s_{t+1}\mid s_t,a_t)
\]

This is thuộc tính (property / 속성) of chosen trạng thái (state / 상태) biểu diễn (representation / 표현), not magical thuộc tính (property / 속성) of world.

If trạng thái (state / 상태) omits relevant lịch sử (history / 이력), Markov giả định (assumption / 가정) fails.

Example: if machine thất bại (failure / 실패) xác suất (probability / 확률) depends on accumulated usage but trạng thái (state / 상태) stores only hiện tại (current / 현재) temperature, trạng thái (state / 상태) is insufficient.

## MDP components

An MDP typically:

\[
\mathcal{M}=(S,A,P,R,\gamma)
\]

where:

- `S`: states;
- `A`: actions;
- `P(s'|s,a)`: chuyển tiếp (transition / 전이) probabilities;
- `R(s,a,s')`: reward;
- `γ`: discount factor.

A **chính sách (policy / 정책)**:

\[
\pi(a\mid s)
\]

maps trạng thái (state / 상태) to hành động (action / 동작) phân phối (distribution / 분포).

Goal: find chính sách (policy / 정책) maximizing expected return.

## Return

Discounted return:

\[
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\]

`0≤γ<1` often ensures finite sum and weights near rewards more.

Discounting can represent thời gian (time / 시간) preference, bất định (uncertainty / 불확실성) about continuation or mathematical convenience. Interpretation depends lĩnh vực (domain / 도메인).

For finite horizon, discount may be unnecessary.

## Trạng thái (state / 상태) giá trị (value / 값)

Giá trị (value / 값) of chính sách (policy / 정책) `π`:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid s_t=s]
\]

It answers:

> Nếu bắt đầu ở trạng thái (state / 상태) này và tiếp tục theo chính sách (policy / 정책) π, expected long-term return là bao nhiêu?

## Hành động (action / 동작) giá trị (value / 값)

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid s_t=s,a_t=a]
\]

It evaluates taking hành động (action / 동작) `a` first, then following `π`.

Quyết định (decision / 결정):

\[
\pi(s)=\arg\max_a Q(s,a)
\]

if deterministic greedy chính sách (policy / 정책) desired.

## Bellman equation

Giá trị (value / 값) decomposes recursively:

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

This recursion is one of most important structures in Reinforcement học tập (learning / 학습).

## Bellman optimality

Optimal giá trị (value / 값):

\[
V^*(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma V^*(s')]
\]

Optimal Q:

\[
Q^*(s,a)=\sum_{s'}P(s'\mid s,a)
[R(s,a,s')+\gamma\max_{a'}Q^*(s',a')]
\]

This is stochastic generalization of shortest-path động (dynamic / 동적) programming.

## Giá trị (value / 값) iteration

Initialize `V_0`. Repeatedly apply Bellman optimality backup:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
[R+\gamma V_k(s')]
\]

Under discounted finite MDP conditions, contraction thuộc tính (property / 속성) gives convergence to `V*`.

Then derive chính sách (policy / 정책) by greedy hành động (action / 동작) selection.

## Chính sách (policy / 정책) iteration

Alternate:

1. **chính sách (policy / 정책) evaluation** — compute `V^π`.
2. **chính sách (policy / 정책) improvement** — choose hành động (action / 동작) better according to hiện tại (current / 현재) values.

Repeat until chính sách (policy / 정책) stable.

Chính sách (policy / 정책) iteration can converge in fewer outer iterations but evaluation step costly.

## Tìm kiếm (search / 검색) vs MDP

Deterministic shortest đường dẫn (path / 경로) can be seen as special trường hợp (case / 사례) where chuyển tiếp (transition / 전이) xác suất (probability / 확률) concentrated on one successor.

Tìm kiếm (search / 검색) nút (node / 노드) cost-to-go resembles negative giá trị (value / 값).

A* heuristic approximates remaining chi phí (cost / 비용); RL giá trị (value / 값) hàm (function / 함수) approximates expected future return.

Liên kết (connection / 연결):

```text
heuristic h(s)       ↔ estimated cost-to-go
value V(s)           ↔ expected return-to-go
```

Signs/objectives differ, but structural role similar.

## Unknown chuyển tiếp (transition / 전이) mô hình (model / 모델)

Classical MDP planning assumes `P` and `R` known.

Reinforcement học tập (learning / 학습) begins when môi trường (environment / 환경) mô hình (model / 모델) unknown or too expensive, and tác nhân (agent / 에이전트) learns giá trị (value / 값)/chính sách (policy / 정책) from experience.

Thus:

```text
known model + optimize policy → planning in MDP
unknown model + experience    → RL
```

Model-based RL learns/estimates mô hình (model / 모델); model-free RL learns giá trị (value / 값)/chính sách (policy / 정책) without tường minh (explicit / 명시적) chuyển tiếp (transition / 전이) mô hình (model / 모델).

## Partial khả năng quan sát (observability / 관측 가능성)

If tác nhân (agent / 에이전트) cannot observe trạng thái (state / 상태) `s`, it receives observation `o`.

A **POMDP (부분 관찰 마르코프 결정 과정)** adds observation mô hình (model / 모델).

Tác nhân (agent / 에이전트) maintains belief:

\[
b(s)=P(s\mid history)
\]

Belief trạng thái (state / 상태) is a xác suất (probability / 확률) phân phối (distribution / 분포) over possible states.

POMDP can be transformed conceptually into MDP over belief không gian (space / 공간), but belief không gian (space / 공간) continuous/high-dimensional and difficult.

## Belief cập nhật (update / 업데이트)

After hành động (action / 동작) `a` and observation `o`, Bayesian filtering updates belief:

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

## Trạng thái (state / 상태) estimation

Kalman Filter solves linear-Gaussian trạng thái (state / 상태) estimation efficiently.

Hidden trạng thái (state / 상태) dynamics:

\[
x_t=Ax_{t-1}+Bu_t+w_t
\]

Observation:

\[
z_t=Hx_t+v_t
\]

with Gaussian noises.

Extended/Unscented Kalman variants handle nonlinear approximations; particle filters use samples for more general distributions.

Robotics perception/điều khiển (control / 제어) relies heavily on trạng thái (state / 상태) estimation before planning.

## Quyết định (decision / 결정) under mô hình (model / 모델) bất định (uncertainty / 불확실성)

Even if môi trường (environment / 환경) stochasticity known, mô hình (model / 모델) parameters themselves may be uncertain.

Bayesian quyết định (decision / 결정) making integrates over posterior:

\[
EU(a)=\int U(a,\theta)p(\theta\mid D)d\theta
\]

In practice chính xác (exact / 정확한) tích hợp (integration / 통합) often intractable, requiring approximation.

Ignoring epistemic bất định (uncertainty / 불확실성) can make hệ thống (system / 시스템) overconfident out-of-distribution.

## Robust quyết định (decision / 결정) making

Instead of trust one estimated phân phối (distribution / 분포), robust tối ưu hóa (optimization / 최적화) considers set of possible các mô hình (models / 모델들):

\[
\max_\pi \min_{P\in\mathcal{P}} J(\pi,P)
\]

This protects worst-case within bất định (uncertainty / 불확실성) set but may be conservative.

Distributionally Robust tối ưu hóa (optimization / 최적화) similarly optimizes against distributions near empirical one according to chosen distance/divergence.

## Chance các ràng buộc (constraints / 제약조건들)

Ràng buộc (constraint / 제약조건) may need hold with high xác suất (probability / 확률):

\[
P(g(x,\xi)\le0)\ge1-\alpha
\]

Example autonomous hệ thống (system / 시스템): collision-risk ràng buộc (constraint / 제약조건) < threshold.

Chance các ràng buộc (constraints / 제약조건들) convert bất định (uncertainty / 불확실성) into probabilistic an toàn (safety / 안전) requirements, but require trustworthy bất định (uncertainty / 불확실성) mô hình (model / 모델).

## CVaR and tail rủi ro (risk / 위험)

Expected mất mát (loss / 손실) can hide catastrophic tail.

Value-at-Risk gives quantile; Conditional Value-at-Risk (CVaR) averages losses beyond tail threshold under definitions.

Risk-sensitive RL can optimize CVaR-like objectives when rare catastrophic outcomes matter more than mean hiệu năng (performance / 성능).

## Exploration vs exploitation

When hành động (action / 동작) outcomes uncertain because we have not tried them, hành động (action / 동작) has two values:

1. immediate reward;
2. thông tin (information / 정보) gained for future decisions.

Multi-armed bandit captures this simplest setting.

Each arm has unknown reward phân phối (distribution / 분포). tác nhân (agent / 에이전트) chooses whether exploit best-known arm or explore uncertain arm.

This is sequential giá trị (value / 값) of thông tin (information / 정보).

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

First term exploitation. Second optimism under bất định (uncertainty / 불확실성): less-tried arms get exploration bonus.

This idea also appeared in MCTS selection.

## Thompson Sampling

Maintain posterior over each arm parameter. mẫu (sample / 표본) one parameter from posterior and act greedily under sampled world.

Uncertain arms get naturally explored because posterior wide.

It converts Bayesian bất định (uncertainty / 불확실성) into stochastic hành động (action / 동작) selection.

## Contextual bandits

Recommendation depends người dùng (user / 사용자)/ngữ cảnh (context / 맥락) `x`:

\[
P(r\mid x,a)
\]

Choose hành động (action / 동작) based on ngữ cảnh (context / 맥락), observe reward only for chosen hành động (action / 동작).

This introduces **partial phản hồi (feedback / 피드백)**: we do not see what reward unchosen recommendations would have produced.

Counterfactual evaluation becomes important.

## Off-policy evaluation

If logs generated by hành vi (behavior / 동작) chính sách (policy / 정책) `μ`, want estimate mục tiêu (target / 대상) chính sách (policy / 정책) `π` without deploying.

Importance sampling idea weights observations:

\[
w=\frac{\pi(a\mid s)}{\mu(a\mid s)}
\]

Under các giả định (assumptions / 가정들), reweight hành vi (behavior / 동작) dữ liệu (data / 데이터) to mục tiêu (target / 대상) phân phối (distribution / 분포).

But high variance when mục tiêu (target / 대상) chooses actions hành vi (behavior / 동작) rarely chose.

This connects Statistics, nhân quả (causal / 인과적) suy luận (inference / 추론) and RL evaluation.

## Reward thiết kế (design / 설계)

Reward is not reality. It is a proxy tín hiệu (signal / 신호).

If optimize engagement clicks, tác nhân (agent / 에이전트) may learn hành vi (behavior / 동작) increasing short-term clicks but harming long-term satisfaction.

Sequential tối ưu hóa (optimization / 최적화) amplifies reward misspecification because chính sách (policy / 정책) actively changes future dữ liệu (data / 데이터)/trạng thái (state / 상태).

This is direct cầu nối (bridge / 브리지) to AI Alignment.

## Delayed consequences

Hành động (action / 동작) may have low immediate reward but high long-term giá trị (value / 값).

Example máy chủ (server / 서버) autoscaling: spinning instance costs now but avoids outage later.

Myopic quyết định (decision / 결정) maximizing immediate reward fails.

Bellman recursion handles delayed consequences by future giá trị (value / 값).

## Credit assignment

If reward arrives after long hành động (action / 동작) chuỗi (sequence / 시퀀스), which earlier actions deserve credit?

This is cốt lõi (core / 핵심) RL difficulty.

Temporal Difference học tập (learning / 학습) propagates giá trị (value / 값) backward over experience rather than wait only final kết quả (outcome / 결과).

LLM tác nhân (agent / 에이전트) evaluation also faces credit assignment: tác vụ (task / 작업) success/thất bại (failure / 실패) after 20 công cụ (tool / 도구) calls does not directly identify which quyết định (decision / 결정) caused kết quả (outcome / 결과).

## Planning under bất định (uncertainty / 불확실성) for agents

Công cụ (tool / 도구) tác nhân (agent / 에이전트) may face:

```text
API may fail
search results incomplete
user intent partially specified
external state changes
```

Reliable mẫu (pattern / 패턴):

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

Sometimes best next hành động (action / 동작) is asking for missing thông tin (information / 정보) rather than committing to plan.

## Irreversible actions

Actions like payment, deletion, sending message or deploying mã (code / 코드) have high downside.

Quyết định (decision / 결정) hệ thống (system / 시스템) should distinguish reversible vs irreversible actions.

Possible chính sách (policy / 정책):

```text
low-risk reversible → autonomous
high-risk irreversible → stronger validation / confirmation
```

This is utility/risk-aware planning, not just UX convention.

## Mô hình (model / 모델) bất định (uncertainty / 불확실성) vs môi trường (environment / 환경) randomness

Recall:

- **aleatoric bất định (uncertainty / 불확실성)**: inherent stochasticity;
- **epistemic bất định (uncertainty / 불확실성)**: ignorance/mô hình (model / 모델) bất định (uncertainty / 불확실성).

Quyết định (decision / 결정) chiến lược (strategy / 전략) differs. More dữ liệu (data / 데이터) may reduce epistemic bất định (uncertainty / 불확실성) but not irreducible noise.

Exploration targets epistemic bất định (uncertainty / 불확실성); robust chính sách (policy / 정책) protects against uncertain mô hình (model / 모델); risk-sensitive utility handles consequence cấu trúc (structure / 구조).

## Expected utility is not morality

Encoding utility requires deciding whose outcomes count and how trade-offs measured. Mathematics optimizes provided utility; it does not define ethical values.

For xã hội (social / 사회적)/high-impact AI, utility mô hình (model / 모델), fairness các ràng buộc (constraints / 제약조건들) and quản trị (governance / 거버넌스) are normative thiết kế (design / 설계) choices requiring human institutions.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

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

## Dùng chung (common / 공통) Misconceptions

### “Highest xác suất (probability / 확률) kết quả (outcome / 결과) should determine hành động (action / 동작)”

Quyết định (decision / 결정) depends consequences. Low-probability catastrophic sự kiện (event / 이벤트) can dominate expected/risk-sensitive choice.

### “MDP trạng thái (state / 상태) is just hiện tại (current / 현재) observation”

Trạng thái (state / 상태) must be Markov-sufficient. Observation may be partial.

### “Expected reward maximum means safest chính sách (policy / 정책)”

Not necessarily. Mean mục tiêu (objective / 목표) can tolerate rare catastrophic mất mát (loss / 손실) unless rủi ro (risk / 위험) encoded.

### “RL begins whenever there is an tác nhân (agent / 에이전트)”

If chuyển tiếp (transition / 전이)/reward mô hình (model / 모델) known and chính sách (policy / 정책) solved by DP, it is planning in an MDP. RL specifically learns from tương tác (interaction / 상호작용)/dữ liệu (data / 데이터) when relevant mô hình (model / 모델)/giá trị (value / 값)/chính sách (policy / 정책) unknown.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Quyết định (decision / 결정) Making Under bất định (uncertainty / 불확실성) completes cầu nối (bridge / 브리지) from Classical tìm kiếm (search / 검색)/Planning to Reinforcement học tập (learning / 학습). tìm kiếm (search / 검색) handles deterministic alternatives; MDP adds stochastic transitions and long-term giá trị (value / 값); POMDP adds hidden trạng thái (state / 상태); RL learns hành vi (behavior / 동작) when mô hình (model / 모델)/giá trị (value / 값) unknown.

Sau phần Knowledge Representation và Machine Learning, library sẽ quay lại MDP/Bellman equations sâu hơn trong `11_reinforcement_learning/`.
