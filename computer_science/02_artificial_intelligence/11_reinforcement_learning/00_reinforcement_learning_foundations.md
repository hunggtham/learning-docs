# Reinforcement học tập (learning / 학습) Foundations

> **Mạch đọc:** Đặt **Reinforcement học tập (learning / 학습) Foundations** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao RL khác supervised học tập (learning / 학습)?** sang **Reward và Return**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Reinforcement học tập (learning / 학습)** nghiên cứu cách một tác nhân (agent / 에이전트) học cách hành động qua tương tác (interaction / 상호작용) với môi trường (environment / 환경) để tối đa hóa reward tích lũy theo thời gian. Khác supervised học tập (learning / 학습), tác nhân (agent / 에이전트) thường không nhận “đáp án đúng” cho từng hành động (action / 동작); nó nhận consequences và reward, đôi khi delayed nhiều bước.

```text
state s_t
→ agent chooses action a_t
→ environment transitions to s_{t+1}
→ reward r_{t+1}
→ repeat
```

## Vì sao RL khác supervised học tập (learning / 학습)?

Supervised học tập (learning / 학습) có dataset tương đối cố định `(x,y)`. RL có ba complication:

1. dữ liệu (data / 데이터) phân phối (distribution / 분포) phụ thuộc chính sách (policy / 정책) hiện tại;
2. reward có thể delayed;
3. tác nhân (agent / 에이전트) phải cân bằng exploration và exploitation.

Nếu tác nhân (agent / 에이전트) chọn hành động (action / 동작) khác, nó sẽ thấy dữ liệu (data / 데이터) khác.

## Reward và Return

Reward `r_t` là phản hồi (feedback / 피드백) tại một thời điểm. mục tiêu (objective / 목표) thường là expected discounted return:

\[
G_t = r_{t+1}+\gamma r_{t+2}+\gamma^2 r_{t+3}+\cdots
\]

với discount factor:

\[
0\le \gamma <1
\]

`γ` điều khiển sự đánh đổi (trade-off / 트레이드오프) giữa reward gần và xa, đồng thời giúp infinite-horizon sum hội tụ trong nhiều setting.

## Chính sách (policy / 정책)

Chính sách (policy / 정책) mô tả cách tác nhân (agent / 에이전트) chọn hành động (action / 동작):

\[
\pi(a\mid s)
\]

Deterministic chính sách (policy / 정책) có thể viết `a=π(s)`; stochastic chính sách (policy / 정책) trả phân phối (distribution / 분포).

## Giá trị (value / 값)

State-value:

\[
V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s]
\]

Action-value:

\[
Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]
\]

Giá trị (value / 값) không phải immediate reward; nó ước lượng long-term consequence.

## Model-Free vs Model-Based

**Model-based RL** sử dụng/học chuyển tiếp (transition / 전이)/reward mô hình (model / 모델) để plan.

**Model-free RL** học chính sách (policy / 정책)/giá trị (value / 값) trực tiếp từ experience mà không cần tường minh (explicit / 명시적) môi trường (environment / 환경) mô hình (model / 모델).

Hai approach có thể kết hợp.

## Exploration vs Exploitation

Tác nhân (agent / 에이전트) phải chọn giữa:

- exploitation: dùng hành động (action / 동작) currently estimated best;
- exploration: thử hành động (action / 동작) để thu thông tin (information / 정보).

Nếu chỉ exploit sớm, tác nhân (agent / 에이전트) có thể kẹt với chính sách (policy / 정책) suboptimal.

Epsilon-greedy:

```text
with probability ε: random action
otherwise: argmax Q(s,a)
```

là chiến lược (strategy / 전략) đơn giản, không phải universally best.

## On-Policy vs Off-Policy

On-policy học về chính sách (policy / 정책) đang generate dữ liệu (data / 데이터). Off-policy có thể học mục tiêu (target / 대상) chính sách (policy / 정책) khác hành vi (behavior / 동작) chính sách (policy / 정책).

Q-learning là classic off-policy phương thức (method / 메서드). SARSA là on-policy.

## Credit Assignment

Nếu reward cuối episode tốt, hành động (action / 동작) nào trước đó deserve credit? Đây là temporal credit-assignment bài toán (problem / 문제).

Bellman methods, TD học tập (learning / 학습) và chính sách (policy / 정책) gradients đưa ra các cách khác nhau để propagate tín hiệu (signal / 신호) backward qua thời gian (time / 시간).

## Reward Specification

Reward là mathematical proxy cho goal. Nếu proxy sai, tác nhân (agent / 에이전트) có thể optimize theo cách không mong muốn — **reward hacking/specification gaming**.

Ví dụ robot được reward “di chuyển nhanh” nhưng không penalize va chạm có thể học hành vi (behavior / 동작) dangerous.

## Sparse Reward

Nếu chỉ có reward ở cuối long tác vụ (task / 작업), học tập (learning / 학습) tín hiệu (signal / 신호) rất yếu. Reward shaping thêm intermediate tín hiệu (signal / 신호) nhưng có thể distort mục tiêu (objective / 목표) nếu thiết kế (design / 설계) kém.

## Episodes và Continuing Tasks

Episodic tác vụ (task / 작업) có terminal trạng thái (state / 상태), như game. Continuing tác vụ (task / 작업) chạy indefinite, như tiến trình (process / 프로세스) điều khiển (control / 제어).

## Partial khả năng quan sát (observability / 관측 가능성)

Nếu observation không đủ xác định true trạng thái (state / 상태), bài toán (problem / 문제) trở thành POMDP-like. tác nhân (agent / 에이전트) có thể cần bộ nhớ (memory / 메모리)/belief trạng thái (state / 상태).

## Offline RL

Offline/batch RL học từ fixed logged dataset mà không tương tác thêm môi trường (environment / 환경). Khó vì chính sách (policy / 정책) mới có thể chọn actions ngoài dữ liệu (data / 데이터) hỗ trợ (support / 지원), khiến giá trị (value / 값) extrapolation unreliable.

## RL và LLM Alignment

RL xuất hiện trong alignment như RLHF, nhưng LLM post-training có đặc thù: hành động (action / 동작) có thể là whole chuỗi (sequence / 시퀀스)/đơn vị từ (token / 토큰) decisions, reward đến từ preference mô hình (model / 모델)/human tín hiệu (signal / 신호), và reference-policy các ràng buộc (constraints / 제약조건들) quan trọng.

Không nên equate toàn bộ RL với RLHF.

## Mô hình tư duy (mental model / 사고 모델)

> **Supervised học tập (learning / 학습) hỏi “đầu ra (output / 출력) nào đúng cho đầu vào (input / 입력) này?”, RL hỏi “chuỗi hành động (action / 동작) nào tạo long-term consequence tốt?”**

## Dùng chung (common / 공통) Misconceptions

### “Reward = mục tiêu thật”

Reward chỉ là encoded mục tiêu (objective / 목표). Nếu encoding thiếu, optimizer có thể exploit gap.

### “RL luôn cần robot/game”

RL áp dụng mọi sequential quyết định (decision / 결정) bài toán (problem / 문제) có phản hồi (feedback / 피드백).

### “More exploration luôn tốt”

Exploration có chi phí (cost / 비용)/rủi ro (risk / 위험); real các hệ thống (systems / 시스템들) cần safe exploration.

## Liên kết kiến thức (knowledge connection / 지식 연결)

RL nối [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md), [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), xác suất (probability / 확률) và tối ưu hóa (optimization / 최적화).

Xem tiếp: [Markov Decision Processes](./01_markov_decision_processes.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 markov decision processes](./01_markov_decision_processes.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
