# Reinforcement học tập (learning / 학습) Foundations

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Reinforcement learning foundations**. Route đi từ state/action/environment → reward and return → policy/value → exploration/exploitation → episodic interaction, để RL được đọc như học qua hậu quả của hành động.

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

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, **Reward và Return** tiếp nhận điểm tựa từ **Vì sao RL khác supervised học tập (learning / 학습)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) Foundations**, **Chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Reward và Return** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책)

Chính sách (policy / 정책) mô tả cách tác nhân (agent / 에이전트) chọn hành động (action / 동작):

\[
\pi(a\mid s)
\]

Deterministic chính sách (policy / 정책) có thể viết `a=π(s)`; stochastic chính sách (policy / 정책) trả phân phối (distribution / 분포).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) Foundations**, **Giá trị (value / 값)** tiếp nhận điểm tựa từ **Chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Model-Free vs Model-Based** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, **Model-Free vs Model-Based** tiếp nhận điểm tựa từ **Giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exploration vs Exploitation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Model-Free vs Model-Based

**Model-based RL** sử dụng/học chuyển tiếp (transition / 전이)/reward mô hình (model / 모델) để plan.

**Model-free RL** học chính sách (policy / 정책)/giá trị (value / 값) trực tiếp từ experience mà không cần tường minh (explicit / 명시적) môi trường (environment / 환경) mô hình (model / 모델).

Hai approach có thể kết hợp.

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) Foundations**, **Exploration vs Exploitation** tiếp nhận điểm tựa từ **Model-Free vs Model-Based** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **On-Policy vs Off-Policy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) Foundations**, **On-Policy vs Off-Policy** tiếp nhận điểm tựa từ **Exploration vs Exploitation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Credit Assignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## On-Policy vs Off-Policy

On-policy học về chính sách (policy / 정책) đang generate dữ liệu (data / 데이터). Off-policy có thể học mục tiêu (target / 대상) chính sách (policy / 정책) khác hành vi (behavior / 동작) chính sách (policy / 정책).

Q-learning là classic off-policy phương thức (method / 메서드). SARSA là on-policy.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, **Credit Assignment** tiếp nhận điểm tựa từ **On-Policy vs Off-Policy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward Specification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Credit Assignment

Nếu reward cuối episode tốt, hành động (action / 동작) nào trước đó deserve credit? Đây là temporal credit-assignment bài toán (problem / 문제).

Bellman methods, TD học tập (learning / 학습) và chính sách (policy / 정책) gradients đưa ra các cách khác nhau để propagate tín hiệu (signal / 신호) backward qua thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) Foundations**, **Reward Specification** tiếp nhận điểm tựa từ **Credit Assignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sparse Reward** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward Specification

Reward là mathematical proxy cho goal. Nếu proxy sai, tác nhân (agent / 에이전트) có thể optimize theo cách không mong muốn — **reward hacking/specification gaming**.

Ví dụ robot được reward “di chuyển nhanh” nhưng không penalize va chạm có thể học hành vi (behavior / 동작) dangerous.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) Foundations**, **Sparse Reward** tiếp nhận điểm tựa từ **Reward Specification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Episodes và Continuing Tasks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparse Reward

Nếu chỉ có reward ở cuối long tác vụ (task / 작업), học tập (learning / 학습) tín hiệu (signal / 신호) rất yếu. Reward shaping thêm intermediate tín hiệu (signal / 신호) nhưng có thể distort mục tiêu (objective / 목표) nếu thiết kế (design / 설계) kém.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, **Episodes và Continuing Tasks** tiếp nhận điểm tựa từ **Sparse Reward** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Episodes và Continuing Tasks

Episodic tác vụ (task / 작업) có terminal trạng thái (state / 상태), như game. Continuing tác vụ (task / 작업) chạy indefinite, như tiến trình (process / 프로세스) điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) Foundations**, **Partial khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Episodes và Continuing Tasks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Offline RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial khả năng quan sát (observability / 관측 가능성)

Nếu observation không đủ xác định true trạng thái (state / 상태), bài toán (problem / 문제) trở thành POMDP-like. tác nhân (agent / 에이전트) có thể cần bộ nhớ (memory / 메모리)/belief trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) Foundations**, **Offline RL** tiếp nhận điểm tựa từ **Partial khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RL và LLM Alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline RL

Offline/batch RL học từ fixed logged dataset mà không tương tác thêm môi trường (environment / 환경). Khó vì chính sách (policy / 정책) mới có thể chọn actions ngoài dữ liệu (data / 데이터) hỗ trợ (support / 지원), khiến giá trị (value / 값) extrapolation unreliable.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, **RL và LLM Alignment** tiếp nhận điểm tựa từ **Offline RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RL và LLM Alignment

RL xuất hiện trong alignment như RLHF, nhưng LLM post-training có đặc thù: hành động (action / 동작) có thể là whole chuỗi (sequence / 시퀀스)/đơn vị từ (token / 토큰) decisions, reward đến từ preference mô hình (model / 모델)/human tín hiệu (signal / 신호), và reference-policy các ràng buộc (constraints / 제약조건들) quan trọng.

Không nên equate toàn bộ RL với RLHF.

> **Chuyển mạch:** Ở chặng này của **Reinforcement học tập (learning / 학습) Foundations**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **RL và LLM Alignment** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Supervised học tập (learning / 학습) hỏi “đầu ra (output / 출력) nào đúng cho đầu vào (input / 입력) này?”, RL hỏi “chuỗi hành động (action / 동작) nào tạo long-term consequence tốt?”**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Reinforcement học tập (learning / 학습) Foundations**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Reward = mục tiêu thật”

Reward chỉ là encoded mục tiêu (objective / 목표). Nếu encoding thiếu, optimizer có thể exploit gap.

### “RL luôn cần robot/game”

RL áp dụng mọi sequential quyết định (decision / 결정) bài toán (problem / 문제) có phản hồi (feedback / 피드백).

### “More exploration luôn tốt”

Exploration có chi phí (cost / 비용)/rủi ro (risk / 위험); real các hệ thống (systems / 시스템들) cần safe exploration.

> **Chuyển mạch:** Trong **Reinforcement học tập (learning / 학습) Foundations**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

RL nối [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md), [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), xác suất (probability / 확률) và tối ưu hóa (optimization / 최적화).

Xem tiếp: [Markov Decision Processes](./01_markov_decision_processes.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
