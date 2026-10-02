# Actor-Critic

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Actor-critic**. Route đi từ actor policy → critic value estimate → advantage/TD error → coupled updates → stability and on/off-policy variants, để critic giảm phương sai cho actor mà vẫn tạo bias cần kiểm soát.

**Actor-Critic (액터-크리틱)** kết hợp hai components:

- **Actor**: chính sách (policy / 정책) `π_θ(a|s)` quyết định hành động (action / 동작);
- **Critic**: giá trị (value / 값) estimator `V_w(s)` hoặc `Q_w(s,a)` đánh giá hành động (action / 동작)/trạng thái (state / 상태).

Actor học từ phản hồi (feedback / 피드백) của critic; critic học dự đoán long-term return.

```text
state
→ Actor chooses action
→ environment gives reward/next state
→ Critic computes TD/advantage signal
→ update Critic
→ update Actor
```

## Vì sao cần Critic?

REINFORCE dùng full Monte Carlo return nên variance cao. Critic bootstrap giá trị (value / 값) estimate để tạo lower-variance học tập (learning / 학습) tín hiệu (signal / 신호).

Một one-step TD lỗi (error / 오류):

\[
\delta_t=R_{t+1}+\gamma V_w(S_{t+1})-V_w(S_t)
\]

có thể dùng như approximate advantage cho actor:

\[
\theta\leftarrow\theta+\alpha\delta_t\nabla_\theta\log\pi_\theta(A_t|S_t)
\]

> **Chuyển mạch:** Trong **Actor-Critic**, **Actor mục tiêu (objective / 목표)** tiếp nhận điểm tựa từ **Vì sao cần Critic?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Critic mục tiêu (objective / 목표)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Actor mục tiêu (objective / 목표)

Actor muốn tăng expected return. Critic cung cấp estimate hành động (action / 동작) tốt hơn baseline bao nhiêu.

Nếu `δ_t>0`, hành động (action / 동작) tốt hơn expected → tăng xác suất (probability / 확률).

Nếu `δ_t<0`, hành động (action / 동작) tệ hơn expected → giảm xác suất (probability / 확률).

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Critic mục tiêu (objective / 목표)** tiếp nhận điểm tựa từ **Actor mục tiêu (objective / 목표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **On-Policy Actor-Critic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Critic mục tiêu (objective / 목표)

Critic minimize giá trị (value / 값) prediction lỗi (error / 오류), ví dụ:

\[
L_V=(R+\gamma V_w(s')-V_w(s))^2
\]

Actor và critic học tập (learning / 학습) targets thay đổi cùng nhau, tạo coupled tối ưu hóa (optimization / 최적화) dynamics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **On-Policy Actor-Critic** tiếp nhận điểm tựa từ **Critic mục tiêu (objective / 목표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Off-Policy Actor-Critic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## On-Policy Actor-Critic

A2C/A3C family sử dụng on-policy trajectories. Advantage estimate từ critic giảm variance so với pure Monte Carlo.

> **Chuyển mạch:** Trong **Actor-Critic**, **Off-Policy Actor-Critic** tiếp nhận điểm tựa từ **On-Policy Actor-Critic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DDPG Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Off-Policy Actor-Critic

Algorithms như DDPG, TD3, SAC learn from replay buffers.

Actor có thể optimize:

\[
\max_\theta Q_w(s,\pi_\theta(s))
\]

trong continuous hành động (action / 동작) problems.

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **DDPG Intuition** tiếp nhận điểm tựa từ **Off-Policy Actor-Critic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Soft Actor-Critic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DDPG Intuition

**Deep Deterministic chính sách (policy / 정책) độ dốc (gradient / 기울기) (DDPG)** dùng deterministic actor cho continuous hành động (action / 동작), critic Q-function, replay buffer và mục tiêu (target / 대상) networks.

Nhưng DDPG sensitive/stability issues; TD3 cải thiện bằng clipped double critics, delayed chính sách (policy / 정책) updates và mục tiêu (target / 대상) smoothing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **Soft Actor-Critic** tiếp nhận điểm tựa từ **DDPG Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (shared / 공유) vs Separate Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Soft Actor-Critic

**SAC** maximize return + entropy:

\[
J(\pi)=\mathbb E\left[\sum_t \gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

Entropy encourage exploration và robustness. SAC là strong off-policy phương thức (method / 메서드) cho continuous điều khiển (control / 제어).

> **Chuyển mạch:** Trong **Actor-Critic**, **Dùng chung (shared / 공유) vs Separate Networks** tiếp nhận điểm tựa từ **Soft Actor-Critic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Critic độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) vs Separate Networks

Actor/critic có thể share biểu diễn (representation / 표현) trunk rồi tách heads, hoặc independent networks.

Dùng chung (shared / 공유) mạng (network / 네트워크) tiết kiệm compute và biểu diễn (representation / 표현), nhưng gradients từ chính sách (policy / 정책)/giá trị (value / 값) objectives có thể interfere.

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Critic độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Dùng chung (shared / 공유) vs Separate Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Advantage Estimation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Critic độ lệch (bias / 편향)

Nếu critic systematically wrong, actor optimize against wrong landscape. This is analogous reward-model exploitation: actor can exploit critic lỗi (error / 오류).

Double critics và conservative updates help.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **Advantage Estimation** tiếp nhận điểm tựa từ **Critic độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Two Timescales** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Advantage Estimation

Critic enables:

\[
A(s,a)=Q(s,a)-V(s)
\]

or GAE estimates. Advantage removes trạng thái (state / 상태) difficulty baseline: hành động (action / 동작) judged relative to what is normally achievable from trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Actor-Critic**, **Two Timescales** tiếp nhận điểm tựa từ **Advantage Estimation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu (target / 대상) Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Two Timescales

Actor và critic học tập (learning / 학습) rates ảnh hưởng stability. Critic cần nhánh học (track / 트랙) chính sách (policy / 정책) enough; actor không nên outrun critic too much.

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Mục tiêu (target / 대상) Networks** tiếp nhận điểm tựa từ **Two Timescales** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Replay Buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu (target / 대상) Networks

Off-policy critics often use slow mục tiêu (target / 대상) networks to stabilize bootstrap mục tiêu (target / 대상), giống DQN.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **Replay Buffer** tiếp nhận điểm tựa từ **Mục tiêu (target / 대상) Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuous hành động (action / 동작) Boundaries** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Replay Buffer

Off-policy actor-critic reuse transitions. Need handle phân phối (distribution / 분포) mismatch, stale dữ liệu (data / 데이터) and exploration coverage.

> **Chuyển mạch:** Trong **Actor-Critic**, **Continuous hành động (action / 동작) Boundaries** tiếp nhận điểm tựa từ **Replay Buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuous hành động (action / 동작) Boundaries

Actor đầu ra (output / 출력) thường squashed with `tanh` then scaled to hành động (action / 동작) bounds. xác suất (probability / 확률) correction needed for stochastic chính sách (policy / 정책) log-probs after transformation in SAC-like methods.

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Partial khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Continuous hành động (action / 동작) Boundaries** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Agent Actor-Critic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial khả năng quan sát (observability / 관측 가능성)

Actor/critic có thể use recurrent trạng thái (state / 상태)/transformer bộ nhớ (memory / 메모리) when observation not Markov.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **Multi-Agent Actor-Critic** tiếp nhận điểm tựa từ **Partial khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: Robot điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Agent Actor-Critic

Centralized critic can observe joint thông tin (information / 정보) during huấn luyện (training / 학습) while decentralized actors act from cục bộ (local / 로컬) observations at thực thi (execution / 실행). Đây là dùng chung (common / 공통) multi-agent RL paradigm.

> **Chuyển mạch:** Trong **Actor-Critic**, **Multi-Agent Actor-Critic** cho ta quy tắc; **Example: Robot điều khiển (control / 제어)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Actor-Critic và LLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: Robot điều khiển (control / 제어)

Trạng thái (state / 상태) includes joint positions/velocities; actor outputs motor torques; critic estimates future return. Continuous high-dimensional actions make Q-table impossible, actor provides direct điều khiển (control / 제어) ánh xạ (mapping / 매핑).

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Example: Robot điều khiển (control / 제어)** cho ta quy tắc; **Actor-Critic và LLM** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) Modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Actor-Critic và LLM

RLHF with PPO conceptually has chính sách (policy / 정책) actor and learned reward/giá trị (value / 값) components. But LLM hành động (action / 동작) không gian (space / 공간) and chuỗi (sequence / 시퀀스) generation make hiện thực (implementation / 구현) specialized.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, **Thất bại (failure / 실패) Modes** tiếp nhận điểm tựa từ **Actor-Critic và LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) Modes

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- critic divergence;
- actor exploits critic errors;
- insufficient exploration;
- giá trị (value / 값) overestimation;
- unstable entropy coefficient;
- replay phân phối (distribution / 분포) mismatch;
- reward quy mô (scale / 규모) problems.

> **Chuyển mạch:** Trong **Actor-Critic**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Thất bại (failure / 실패) Modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Actor nói “tôi sẽ làm gì”; Critic nói “lựa chọn đó tốt hơn kỳ vọng bao nhiêu”.**

> **Chuyển mạch:** Ở chặng này của **Actor-Critic**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Critic là một human reviewer”

Không. Critic trong RL là learned giá trị (value / 값)/Q estimator, dù bên ngoài (external / 외부) evaluators có thể provide reward.

### “Actor-Critic luôn on-policy”

Có cả on-policy và off-policy families.

### “Critic chính xác tuyệt đối”

Critic cũng là learned approximator và có độ lệch (bias / 편향)/lỗi (error / 오류).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Actor-Critic**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Actor-Critic kết hợp value-based và policy-based RL, là cầu nối (bridge / 브리지) trực tiếp sang Deep Reinforcement học tập (learning / 학습).

Xem tiếp: [Deep Reinforcement Learning](./09_deep_reinforcement_learning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
