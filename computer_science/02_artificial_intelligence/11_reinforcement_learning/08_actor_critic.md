# Actor-Critic

> **Mạch đọc:** Đặt **Actor-Critic** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao cần Critic?** sang **Actor mục tiêu (objective / 목표)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Actor mục tiêu (objective / 목표)

Actor muốn tăng expected return. Critic cung cấp estimate hành động (action / 동작) tốt hơn baseline bao nhiêu.

Nếu `δ_t>0`, hành động (action / 동작) tốt hơn expected → tăng xác suất (probability / 확률).

Nếu `δ_t<0`, hành động (action / 동작) tệ hơn expected → giảm xác suất (probability / 확률).

## Critic mục tiêu (objective / 목표)

Critic minimize giá trị (value / 값) prediction lỗi (error / 오류), ví dụ:

\[
L_V=(R+\gamma V_w(s')-V_w(s))^2
\]

Actor và critic học tập (learning / 학습) targets thay đổi cùng nhau, tạo coupled tối ưu hóa (optimization / 최적화) dynamics.

## On-Policy Actor-Critic

A2C/A3C family sử dụng on-policy trajectories. Advantage estimate từ critic giảm variance so với pure Monte Carlo.

## Off-Policy Actor-Critic

Algorithms như DDPG, TD3, SAC learn from replay buffers.

Actor có thể optimize:

\[
\max_\theta Q_w(s,\pi_\theta(s))
\]

trong continuous hành động (action / 동작) problems.

## DDPG Intuition

**Deep Deterministic chính sách (policy / 정책) độ dốc (gradient / 기울기) (DDPG)** dùng deterministic actor cho continuous hành động (action / 동작), critic Q-function, replay buffer và mục tiêu (target / 대상) networks.

Nhưng DDPG sensitive/stability issues; TD3 cải thiện bằng clipped double critics, delayed chính sách (policy / 정책) updates và mục tiêu (target / 대상) smoothing.

## Soft Actor-Critic

**SAC** maximize return + entropy:

\[
J(\pi)=\mathbb E\left[\sum_t \gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

Entropy encourage exploration và robustness. SAC là strong off-policy phương thức (method / 메서드) cho continuous điều khiển (control / 제어).

## Dùng chung (shared / 공유) vs Separate Networks

Actor/critic có thể share biểu diễn (representation / 표현) trunk rồi tách heads, hoặc independent networks.

Dùng chung (shared / 공유) mạng (network / 네트워크) tiết kiệm compute và biểu diễn (representation / 표현), nhưng gradients từ chính sách (policy / 정책)/giá trị (value / 값) objectives có thể interfere.

## Critic độ lệch (bias / 편향)

Nếu critic systematically wrong, actor optimize against wrong landscape. This is analogous reward-model exploitation: actor can exploit critic lỗi (error / 오류).

Double critics và conservative updates help.

## Advantage Estimation

Critic enables:

\[
A(s,a)=Q(s,a)-V(s)
\]

or GAE estimates. Advantage removes trạng thái (state / 상태) difficulty baseline: hành động (action / 동작) judged relative to what is normally achievable from trạng thái (state / 상태).

## Two Timescales

Actor và critic học tập (learning / 학습) rates ảnh hưởng stability. Critic cần nhánh học (track / 트랙) chính sách (policy / 정책) enough; actor không nên outrun critic too much.

## Mục tiêu (target / 대상) Networks

Off-policy critics often use slow mục tiêu (target / 대상) networks to stabilize bootstrap mục tiêu (target / 대상), giống DQN.

## Replay Buffer

Off-policy actor-critic reuse transitions. Need handle phân phối (distribution / 분포) mismatch, stale dữ liệu (data / 데이터) and exploration coverage.

## Continuous hành động (action / 동작) Boundaries

Actor đầu ra (output / 출력) thường squashed with `tanh` then scaled to hành động (action / 동작) bounds. xác suất (probability / 확률) correction needed for stochastic chính sách (policy / 정책) log-probs after transformation in SAC-like methods.

## Partial khả năng quan sát (observability / 관측 가능성)

Actor/critic có thể use recurrent trạng thái (state / 상태)/transformer bộ nhớ (memory / 메모리) when observation not Markov.

## Multi-Agent Actor-Critic

Centralized critic can observe joint thông tin (information / 정보) during huấn luyện (training / 학습) while decentralized actors act from cục bộ (local / 로컬) observations at thực thi (execution / 실행). Đây là dùng chung (common / 공통) multi-agent RL paradigm.

## Example: Robot điều khiển (control / 제어)

Trạng thái (state / 상태) includes joint positions/velocities; actor outputs motor torques; critic estimates future return. Continuous high-dimensional actions make Q-table impossible, actor provides direct điều khiển (control / 제어) ánh xạ (mapping / 매핑).

## Actor-Critic và LLM

RLHF with PPO conceptually has chính sách (policy / 정책) actor and learned reward/giá trị (value / 값) components. But LLM hành động (action / 동작) không gian (space / 공간) and chuỗi (sequence / 시퀀스) generation make hiện thực (implementation / 구현) specialized.

## Thất bại (failure / 실패) Modes

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- critic divergence;
- actor exploits critic errors;
- insufficient exploration;
- giá trị (value / 값) overestimation;
- unstable entropy coefficient;
- replay phân phối (distribution / 분포) mismatch;
- reward quy mô (scale / 규모) problems.

## Mô hình tư duy (mental model / 사고 모델)

> **Actor nói “tôi sẽ làm gì”; Critic nói “lựa chọn đó tốt hơn kỳ vọng bao nhiêu”.**

## Dùng chung (common / 공통) Misconceptions

### “Critic là một human reviewer”

Không. Critic trong RL là learned giá trị (value / 값)/Q estimator, dù bên ngoài (external / 외부) evaluators có thể provide reward.

### “Actor-Critic luôn on-policy”

Có cả on-policy và off-policy families.

### “Critic chính xác tuyệt đối”

Critic cũng là learned approximator và có độ lệch (bias / 편향)/lỗi (error / 오류).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Actor-Critic kết hợp value-based và policy-based RL, là cầu nối (bridge / 브리지) trực tiếp sang Deep Reinforcement học tập (learning / 학습).

Xem tiếp: [Deep Reinforcement Learning](./09_deep_reinforcement_learning.md).
