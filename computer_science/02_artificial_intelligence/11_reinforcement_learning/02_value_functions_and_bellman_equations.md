# Giá trị (value / 값) Functions và Bellman Equations

> **Mạch đọc:** Đặt **giá trị (value / 값) Functions và Bellman Equations** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Bellman decomposition** sang **Q-function Bellman equation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Trong Reinforcement học tập (learning / 학습), immediate reward không đủ để đánh giá một trạng thái (state / 상태)/hành động (action / 동작) vì hành động (action / 동작) hiện tại ảnh hưởng cả future. **giá trị (value / 값) hàm (function / 함수)** nén expected long-term return thành một quantity có thể học và optimize.

Trạng thái (state / 상태) giá trị (value / 값):

\[
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]
\]

Hành động (action / 동작) giá trị (value / 값):

\[
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]
\]

## Bellman decomposition

Return có recursive cấu trúc (structure / 구조):

\[
G_t=R_{t+1}+\gamma G_{t+1}
\]

Do đó:

\[
V^\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma V^\pi(S_{t+1})\mid S_t=s]
\]

Đây là Bellman expectation equation.

Nếu chuyển tiếp (transition / 전이)/reward known:

\[
V^\pi(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R(s,a,s')+\gamma V^\pi(s')]
\]

Bellman equation không phải một heuristic; nó đến trực tiếp từ recursive definition của discounted return.

## Q-function Bellman equation

\[
Q^\pi(s,a)=\mathbb E[R_{t+1}+\gamma\mathbb E_{a'\sim\pi}[Q^\pi(S_{t+1},a')]]
\]

Nếu biết Q tốt, chính sách (policy / 정책) có thể chọn hành động (action / 동작) giá trị (value / 값) cao.

## Optimal giá trị (value / 값)

\[
V^*(s)=\max_\pi V^\pi(s)
\]

Optimal Bellman equation:

\[
V^*(s)=\max_a\mathbb E[R_{t+1}+\gamma V^*(S_{t+1})]
\]

và:

\[
Q^*(s,a)=\mathbb E[R_{t+1}+\gamma\max_{a'}Q^*(S_{t+1},a')]
\]

`max` biến chính sách (policy / 정책) evaluation thành điều khiển (control / 제어) bài toán (problem / 문제).

## Bootstrapping

Nếu estimate giá trị (value / 값) dựa trên estimate khác:

```text
current estimate ← reward + γ × next value estimate
```

đó là **bootstrapping**.

Động (dynamic / 동적) Programming và Temporal Difference dùng bootstrapping. Monte Carlo dùng actual sampled return tới cuối episode thay vì bootstrap.

## Bellman Backup

Một cập nhật (update / 업데이트) dạng:

\[
V(s)\leftarrow R+\gamma V(s')
\]

được gọi là backup. Trong stochastic problems thường cập nhật (update / 업데이트) gradual bằng học tập (learning / 학습) tỷ lệ (rate / 비율).

## Bellman lỗi (error / 오류)

Nếu hàm (function / 함수) approximator `V_θ` không satisfy Bellman consistency, residual:

\[
\delta = R+\gamma V_\theta(s')-V_\theta(s)
\]

là TD lỗi (error / 오류) trong one-step setting.

Positive δ nghĩa kết quả (outcome / 결과) tốt hơn hiện tại (current / 현재) estimate; negative δ nghĩa tệ hơn.

## Giá trị (value / 값) như compressed future

Giá trị (value / 값) hàm (function / 함수) là một prediction mô hình (model / 모델) về future return. Thay vì simulate toàn future mỗi quyết định (decision / 결정), tác nhân (agent / 에이전트) consult giá trị (value / 값) estimate.

Đây tương tự heuristic trong tìm kiếm (search / 검색): cả hai compress future consequence thành scalar estimate. Nhưng giá trị (value / 값) được defined bởi reward/chính sách (policy / 정책)/môi trường (environment / 환경) dynamics.

## Chính sách (policy / 정책) Evaluation và Improvement

Chính sách (policy / 정책) iteration dựa hai ideas:

1. evaluate `V^π`;
2. improve chính sách (policy / 정책) greedily theo giá trị (value / 값)/Q.

Repeated evaluation + improvement có thể converge tới optimal chính sách (policy / 정책) trong finite MDP under tiêu chuẩn (standard / 표준) các giả định (assumptions / 가정들).

## Advantage

Advantage đo hành động (action / 동작) tốt hơn baseline trạng thái (state / 상태) giá trị (value / 값) bao nhiêu:

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)
\]

Nó rất quan trọng trong policy-gradient/actor-critic vì giảm variance và tập trung vào relative chất lượng (quality / 품질) của hành động (action / 동작).

## Why giá trị (value / 값) estimation is hard

Giá trị (value / 값) depends on:

- chính sách (policy / 정책);
- reward definition;
- chuyển tiếp (transition / 전이) dynamics;
- future trạng thái (state / 상태) phân phối (distribution / 분포);
- approximation lỗi (error / 오류).

Chính sách (policy / 정책) thay đổi thì mục tiêu (target / 대상) giá trị (value / 값) cũng thay đổi.

## Hàm (function / 함수) Approximation

Tabular giá trị (value / 값) có one entry per trạng thái (state / 상태). Large/continuous trạng thái (state / 상태) cần approximator:

\[
V_\theta(s)
\]

Neural mạng (network / 네트워크) generalizes across states, nhưng bootstrapping + off-policy + nonlinear approximation có thể gây instability.

## Overestimation độ lệch (bias / 편향)

Trong Q-learning, max trên noisy estimates có thể overestimate:

\[
\mathbb E[\max_a \hat Q(a)] \ge \max_a \mathbb E[\hat Q(a)]
\]

Double Q-learning/DQN variants tách selection/evaluation để giảm độ lệch (bias / 편향).

## Reward-to-Go và Credit

Giá trị (value / 값) functions propagate delayed reward backward qua states. Đây là cơ chế giải temporal credit assignment mà không cần mỗi hành động (action / 동작) có direct label.

## Mô hình tư duy (mental model / 사고 모델)

> **Bellman equation nói: giá trị của hiện tại = reward ngay bây giờ + discounted giá trị (value / 값) của tương lai.**

Recursive quan hệ (relation / 관계) này là xương sống của large part of RL.

## Dùng chung (common / 공통) Misconceptions

### “giá trị (value / 값) là xác suất (probability / 확률) thắng”

Chỉ trong reward setup đặc biệt. General giá trị (value / 값) là expected return.

### “Bellman equation cho biết giá trị (value / 값) ngay lập tức”

Nó là consistency quan hệ (relation / 관계). Ta vẫn cần solve/estimate qua DP, sampling hoặc hàm (function / 함수) approximation.

### “Q và reward giống nhau”

Q chứa long-term expected return, không chỉ immediate reward.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Bellman equations nối recursive algorithms, động (dynamic / 동적) Programming và bootstrapping. Chapter tiếp theo dùng known mô hình (model / 모델) để compute values systematically.

Xem tiếp: [Dynamic Programming](./03_dynamic_programming.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 reinforcement learning foundations](./00_reinforcement_learning_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
