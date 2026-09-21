# Q-Learning

**Q-learning (Q 러닝)** là một thuật toán **Temporal-Difference control không cần model (model-free)** và **off-policy**, dùng để học xấp xỉ optimal action-value function:

\[
Q^*(s,a)
\]

Core update:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\right]
\]

## Vì sao Q-learning mạnh?

Agent có thể hành động theo một behavior policy có exploration, trong khi learning target vẫn hướng về greedy optimal policy.

```text
behavior policy → tạo dữ liệu

greedy target policy → định hướng learning
```

Đây chính là đặc trưng off-policy.

Trong tabular setting, với exploration đủ và các giả định hội tụ chuẩn, Q-learning có thể hội tụ về `Q*`.

## Greedy Policy từ Q

Nếu Q-function đã đủ chính xác:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

Agent có thể chọn action tốt nhất mà không cần biết transition model của environment.

## Exploration

Nếu luôn greedy ngay từ random initial Q, agent có thể không bao giờ khám phá action tốt nằm ngoài trajectory ban đầu.

Một cách đơn giản là epsilon-greedy:

```text
với xác suất ε → chọn action ngẫu nhiên
ngược lại       → chọn argmax Q(s,a)
```

`ε` có thể giảm dần theo thời gian, nhưng giảm quá nhanh khiến state-action coverage không đủ.

## Off-Policy Target

Q-learning target:

\[
y=R+\gamma\max_{a'}Q(s',a')
\]

không phụ thuộc action mà behavior policy thực sự chọn ở next step.

Do đó agent có thể tiếp tục explore trong environment nhưng value update vẫn giả định rằng từ next state trở đi sẽ chọn action greedy nhất.

## So sánh với SARSA

SARSA dùng target:

\[
R+\gamma Q(s',a'_{behavior})
\]

Nó tính đến action thực tế mà exploratory behavior policy sẽ chọn.

Trong environment có rủi ro, SARSA đôi khi học route thận trọng hơn vì value phản ánh possibility của exploratory mistake. Q-learning lại học value của một ideal greedy continuation.

## Giới hạn của Tabular Q-learning

Q-table cần kích thước:

\[
|S|\times|A|
\]

Điều này không khả thi với image state, continuous state hoặc state space khổng lồ.

Function approximation dẫn tới Deep Q-Network (DQN), nơi neural network nhận state và output Q-value cho action.

## Overestimation Bias

Operator `max` trên các Q estimate có noise có xu hướng chọn estimate bị noise đẩy lên cao.

Điều này tạo **overestimation bias**.

Double Q-learning tách action selection và action evaluation để giảm bias.

## Experience Replay

Deep Q-learning thường lưu transition:

```text
(s, a, r, s', done)
```

vào **replay buffer**, sau đó sample mini-batch để training.

Lợi ích:

- giảm temporal correlation giữa sample liên tiếp;
- tái sử dụng experience nhiều lần;
- tăng hiệu quả batching trên GPU;
- hỗ trợ off-policy learning.

Tuy nhiên replay buffer cũng tạo vấn đề về stale data, sampling distribution và ưu tiên sample.

## Target Network

Nếu cùng một neural network vừa tạo target vừa được update liên tục, target sẽ di chuyển quá nhanh và training dễ bất ổn.

DQN dùng một target network `Q_{θ^-}` được freeze hoặc cập nhật chậm:

\[
y=r+\gamma\max_{a'}Q_{\theta^-}(s',a')
\]

Online network `Q_θ` được optimize để tiến gần target này.

Target network làm bootstrapping ổn định hơn.

## DQN Loss

Một loss điển hình:

\[
L(\theta)=\mathbb E[(y-Q_\theta(s,a))^2]
\]

Trong thực tế Huber loss thường được dùng để giảm ảnh hưởng của TD error quá lớn.

## Terminal Transition

Nếu transition kết thúc episode:

\[
y=r
\]

Không bootstrap từ terminal next state.

Xử lý sai `done` hoặc terminal flag có thể làm value estimate bị bias.

## Reward Clipping

Một số deep RL system cổ điển clip reward để ổn định training.

Nhưng clipping thay đổi objective vì loại bỏ thông tin magnitude của reward.

Do đó đây không chỉ là một numerical trick; nó có thể thay behavior mà agent tối ưu.

## Continuous Action

Trong continuous high-dimensional action space, việc tính:

\[
\max_a Q(s,a)
\]

trở nên khó vì không thể enumerate toàn bộ action.

Actor–critic method giải quyết bằng cách học explicit policy network để trực tiếp tạo action thay vì exhaustive argmax.

## Liên hệ với Planning

Q-value có thể được xem như cached estimate của long-term utility cho từng state-action pair.

Classical planning tính consequence bằng environment model. Q-learning học consequence từ experience.

## Ví dụ số

Giả sử:

```text
Q(s,a)=2
r=1
max Q(s',·)=5
γ=0.9
α=0.1
```

Target:

\[
1+0.9\times5=5.5
\]

TD error:

\[
5.5-2=3.5
\]

Update:

\[
Q(s,a)=2+0.1\times3.5=2.35
\]

Q-value dịch dần về phía observed Bellman target thay vì bị ghi đè trong một lần.

## Distribution Shift trong Replay Buffer

Transition cũ có thể được tạo bởi policy đã rất khác policy hiện tại.

Nếu buffer chứa quá nhiều data cũ, adaptation có thể chậm. Nếu chỉ giữ sample rất mới, diversity giảm và temporal correlation tăng.

Replay buffer vì vậy cũng là một data-engineering problem bên trong RL.

## Rủi ro của Offline Q-Learning

Trong offline RL, dataset có thể không chứa một số action. Nhưng Q-function vẫn phải output value cho chúng.

Operator `max` có thể chọn một unseen action bị overestimate chỉ vì function approximator extrapolate sai.

Đây là lý do conservative offline RL cố penalize hoặc hạn chế value của out-of-distribution action.

## Mô hình tư duy

> **Q-learning học: “nếu đang ở state này và chọn action này, long-term return tốt nhất có thể đạt từ đây là bao nhiêu?”**

## Những nhầm lẫn thường gặp

### “Q-learning cần biết environment model”

Không. Nó học trực tiếp từ sampled transition.

### “Off-policy nghĩa là không cần exploration”

Không. Off-policy chỉ nói target policy khác behavior policy; learning vẫn cần đủ data coverage.

### “DQN chỉ là thay Q-table bằng neural network”

Không hoàn toàn. Function approximation tạo instability mới, nên replay buffer, target network và các stabilizer trở thành thành phần rất quan trọng.

## Liên kết kiến thức

Q-learning nối TD bootstrapping với Deep Learning. Policy-gradient method ở chapter tiếp theo tiếp cận control theo hướng khác: optimize trực tiếp policy distribution thay vì gián tiếp chọn argmax trên Q.

Xem tiếp: [Policy Gradient](./07_policy_gradient.md).