# Q-Learning

> **Mạch đọc:** Đặt **Q-Learning** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao Q-learning mạnh?** sang **Greedy chính sách (policy / 정책) từ Q**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Q-learning (Q 러닝)** là model-free, off-policy Temporal Difference điều khiển (control / 제어) thuật toán (algorithm / 알고리즘) học approximation của optimal action-value hàm (function / 함수):

\[
Q^*(s,a)
\]

Cốt lõi (core / 핵심) cập nhật (update / 업데이트):

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\right]
\]

## Vì sao Q-learning mạnh?

Tác nhân (agent / 에이전트) có thể behave exploratory nhưng mục tiêu (target / 대상) cập nhật (update / 업데이트) toward greedy chính sách (policy / 정책). Đây là off-policy distinction:

```text
behavior policy → generates data
optimal greedy target → drives learning
```

Với sufficient exploration và tiêu chuẩn (standard / 표준) tabular các giả định (assumptions / 가정들), Q-learning converge tới `Q*`.

## Greedy chính sách (policy / 정책) từ Q

Nếu Q đã tốt:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

Không cần tường minh (explicit / 명시적) chuyển tiếp (transition / 전이) mô hình (model / 모델) để chọn hành động (action / 동작).

## Exploration

Nếu luôn greedy từ random initial Q, tác nhân (agent / 에이전트) có thể không discover good actions. Epsilon-greedy:

```text
random action with ε
argmax Q otherwise
```

`ε` có thể decay theo thời gian (time / 시간), nhưng decay quá nhanh dẫn tới insufficient exploration.

## Off-Policy mục tiêu (target / 대상)

Q-learning mục tiêu (target / 대상):

\[
y=R+\gamma\max_{a'}Q(s',a')
\]

không depend on hành động (action / 동작) hành vi (behavior / 동작) chính sách (policy / 정책) thực sự chọn ở next step. Vì vậy tác nhân (agent / 에이전트) có thể learn greedy mục tiêu (target / 대상) while behaving exploratory.

## SARSA Contrast

SARSA mục tiêu (target / 대상):

\[
R+\gamma Q(s',a'_{behavior})
\]

Trong risky môi trường (environment / 환경), SARSA có thể learn safer đường dẫn (path / 경로) under exploratory hành vi (behavior / 동작) vì nó accounts possibility of exploratory mistakes. Q-learning learns giá trị (value / 값) of ideal greedy continuation.

## Tabular Limit

Bảng (table / 테이블) kích thước (size / 크기):

\[
|S|\times|A|
\]

không feasible cho images/continuous states. hàm (function / 함수) approximation leads to Deep Q-Networks.

## Overestimation độ lệch (bias / 편향)

`max` over noisy estimates tends to select positive noise. Double Q-learning separates hành động (action / 동작) selection and evaluation to reduce độ lệch (bias / 편향).

## Experience Replay

Deep Q-learning stores transitions:

```text
(s,a,r,s',done)
```

in replay buffer and samples mini-batches.

Benefits:

- breaks temporal correlation;
- reuses dữ liệu (data / 데이터);
- improves hardware batching.

But replay phân phối (distribution / 분포) may differ from hiện tại (current / 현재) chính sách (policy / 정책); this is compatible with off-policy học tập (learning / 학습) but creates prioritization/staleness concerns.

## Mục tiêu (target / 대상) mạng (network / 네트워크)

If same mạng (network / 네트워크) both defines mục tiêu (target / 대상) and is updated every độ dốc (gradient / 기울기) step, mục tiêu (target / 대상) moves rapidly.

DQN keeps slowly updated/frozen mục tiêu (target / 대상) mạng (network / 네트워크):

\[
y=r+\gamma\max_{a'}Q_{\theta^-}(s',a')
\]

then optimize online mạng (network / 네트워크) `Q_θ` toward mục tiêu (target / 대상).

Mục tiêu (target / 대상) mạng (network / 네트워크) stabilizes bootstrapping.

## DQN mất mát (loss / 손실)

\[
L(\theta)=\mathbb E[(y-Q_\theta(s,a))^2]
\]

or Huber mất mát (loss / 손실) often used for robustness.

## Terminal Transitions

If chuyển tiếp (transition / 전이) ends episode:

\[
y=r
\]

No bootstrap from terminal next trạng thái (state / 상태).

Incorrect handling `done` can độ lệch (bias / 편향) học tập (learning / 학습).

## Reward Clipping

Some classic deep RL các hệ thống (systems / 시스템들) clip rewards for stability, but this changes mục tiêu (objective / 목표) by discarding magnitude thông tin (information / 정보). kỹ thuật (engineering / 엔지니어링) trick must be understood as mục tiêu (objective / 목표) transformation.

## Continuous Actions

`max_a Q(s,a)` difficult when hành động (action / 동작) continuous high-dimensional. Actor-critic methods learn tường minh (explicit / 명시적) chính sách (policy / 정책) to produce hành động (action / 동작), avoiding exhaustive argmax.

## Q-learning và Planning Analogy

Q giá trị (value / 값) acts like cached long-term hành động (action / 동작) utility. Classical planning computes consequence from mô hình (model / 모델); Q-learning learns it from experience.

## Example

Suppose:

```text
Q(s,a)=2
r=1
max Q(s',·)=5
γ=0.9
α=0.1
```

Mục tiêu (target / 대상):

\[
1+0.9\times5=5.5
\]

Lỗi (error / 오류):

\[
3.5
\]

Cập nhật (update / 업데이트):

\[
Q(s,a)=2+0.1\times3.5=2.35
\]

## Phân phối (distribution / 분포) Shift in Replay

Old buffer transitions may come from obsolete policies. Too-old dữ liệu (data / 데이터) can slow adaptation; too-recent-only dữ liệu (data / 데이터) reduces diversity. Replay thiết kế (design / 설계) is a data-engineering bài toán (problem / 문제) inside RL.

## Offline Q-Learning rủi ro (risk / 위험)

If dataset lacks certain actions, max may exploit overestimated unseen actions. Conservative offline RL methods penalize out-of-distribution hành động (action / 동작) values.

## Mô hình tư duy (mental model / 사고 모델)

> **Q-learning học “nếu ở trạng thái (state / 상태) này và làm hành động (action / 동작) này, long-term return tốt nhất có thể từ đó là bao nhiêu?”.**

## Dùng chung (common / 공통) Misconceptions

### “Q-learning cần biết môi trường (environment / 환경) mô hình (model / 모델)”

Không; nó học from transitions.

### “Off-policy nghĩa là tác nhân (agent / 에이전트) không cần exploration”

Vẫn cần dữ liệu (data / 데이터) coverage cho relevant state-actions.

### “DQN chỉ là Q-table bằng neural mạng (network / 네트워크)”

Hàm (function / 함수) approximation thêm instability; replay/mục tiêu (target / 대상) networks là trọng yếu (critical / 중요) hệ thống (system / 시스템) changes.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Q-learning nối TD bootstrapping với Deep học tập (learning / 학습). Policy-gradient methods tiếp cận điều khiển (control / 제어) trực tiếp bằng optimizing chính sách (policy / 정책) phân phối (distribution / 분포) thay vì argmax trên Q.

Xem tiếp: [Policy Gradient](./07_policy_gradient.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 reinforcement learning foundations](./00_reinforcement_learning_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
