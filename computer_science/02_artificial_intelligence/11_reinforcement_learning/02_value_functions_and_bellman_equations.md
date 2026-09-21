# Value Function và Bellman Equation

Trong Reinforcement Learning, immediate reward không đủ để đánh giá một state hoặc action vì quyết định hiện tại còn ảnh hưởng toàn bộ future trajectory. **Hàm giá trị (value function / 가치 함수)** nén expected long-term return thành một đại lượng có thể học và tối ưu.

State value:

\[
V^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]
\]

Action value:

\[
Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]
\]

## Phân rã Bellman

Return có cấu trúc đệ quy:

\[
G_t=R_{t+1}+\gamma G_{t+1}
\]

Do đó:

\[
V^\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma V^\pi(S_{t+1})\mid S_t=s]
\]

Đây là **Bellman expectation equation**.

Nếu transition và reward model đã biết:

\[
V^\pi(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R(s,a,s')+\gamma V^\pi(s')]
\]

Bellman equation không phải heuristic. Nó xuất phát trực tiếp từ định nghĩa đệ quy của discounted return.

## Bellman Equation cho Q-function

\[
Q^\pi(s,a)=\mathbb E[R_{t+1}+\gamma\mathbb E_{a'\sim\pi}[Q^\pi(S_{t+1},a')]]
\]

Nếu Q-function được ước lượng tốt, agent có thể so sánh trực tiếp các action tại cùng state.

## Optimal Value

Optimal state value:

\[
V^*(s)=\max_\pi V^\pi(s)
\]

Bellman optimality equation:

\[
V^*(s)=\max_a\mathbb E[R_{t+1}+\gamma V^*(S_{t+1})]
\]

và:

\[
Q^*(s,a)=\mathbb E[R_{t+1}+\gamma\max_{a'}Q^*(S_{t+1},a')]
\]

Operator `max` chuyển bài toán từ đánh giá một policy cố định sang **control problem**: chọn action tốt nhất.

## Bootstrapping

Nếu value estimate mới được tính một phần từ estimate cũ hoặc estimate của next state:

```text
ước lượng hiện tại ← reward + γ × ước lượng value ở state tiếp theo
```

ta gọi đó là **bootstrapping**.

Dynamic Programming và Temporal-Difference learning dùng bootstrapping. Monte Carlo thường dùng sampled return thực tế tới cuối episode thay vì dựa vào next-state estimate.

## Bellman Backup

Một update dạng:

\[
V(s)\leftarrow R+\gamma V(s')
\]

được gọi là **Bellman backup**. Trong bài toán stochastic, update thường diễn ra dần bằng learning rate thay vì ghi đè hoàn toàn.

## Bellman Error và TD Error

Nếu function approximator `V_θ` chưa nhất quán với target Bellman, one-step residual là:

\[
\delta = R+\gamma V_\theta(s')-V_\theta(s)
\]

Đây chính là **Temporal-Difference error (TD error)** trong one-step setting.

- `δ > 0`: outcome quan sát được tốt hơn current estimate;
- `δ < 0`: outcome tệ hơn current estimate.

TD error trở thành learning signal trực tiếp cho nhiều thuật toán RL.

## Value như bản tóm tắt của tương lai

Value function có thể được xem là một prediction model về future return. Thay vì simulate toàn bộ future mỗi lần ra quyết định, agent dùng value estimate để ước lượng consequence dài hạn.

Có thể liên hệ với heuristic trong search: cả hai đều nén thông tin tương lai thành một scalar estimate. Khác biệt là value được định nghĩa cụ thể bởi reward, policy và environment dynamics.

## Policy Evaluation và Policy Improvement

Policy iteration dựa trên hai bước:

1. **policy evaluation**: ước lượng `V^π` hoặc `Q^π`;
2. **policy improvement**: tạo policy tốt hơn dựa trên value hiện tại.

Lặp evaluation và improvement có thể hội tụ tới optimal policy trong finite MDP dưới các giả định chuẩn.

## Advantage Function

**Advantage** đo một action tốt hơn baseline state value bao nhiêu:

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s)
\]

Nếu `A > 0`, action tốt hơn mức trung bình của policy tại state đó; nếu `A < 0`, action tệ hơn baseline.

Advantage đặc biệt quan trọng trong policy gradient và actor–critic vì giúp giảm variance và tập trung update vào **chất lượng tương đối của action**.

## Vì sao ước lượng Value khó?

Value phụ thuộc đồng thời vào:

- policy;
- cách định nghĩa reward;
- transition dynamics;
- distribution của future state;
- approximation error.

Khi policy thay đổi, target value cũng thay đổi. RL vì vậy có target không hoàn toàn cố định như supervised learning thông thường.

## Function Approximation

Trong tabular setting, có thể lưu một value cho mỗi state. Nhưng với state space lớn hoặc liên tục, ta cần function approximator:

\[
V_\theta(s)
\]

Neural network giúp generalize giữa các state tương tự. Tuy nhiên tổ hợp **bootstrapping + off-policy learning + nonlinear function approximation** có thể gây instability, thường được gọi là một phần của “deadly triad” trong RL.

## Overestimation Bias

Trong Q-learning, operator `max` trên các estimate có noise có thể tạo **overestimation bias**:

\[
\mathbb E[\max_a \hat Q(a)] \ge \max_a \mathbb E[\hat Q(a)]
\]

Double Q-learning và các biến thể Double DQN tách action selection khỏi action evaluation để giảm bias này.

## Reward-to-Go và Credit Assignment

Value function truyền thông tin của delayed reward ngược về các state trước đó. Đây là cơ chế giúp giải temporal credit assignment mà không cần một label trực tiếp cho từng action.

## Mô hình tư duy

> **Bellman equation nói rằng giá trị của hiện tại = reward nhận ngay + discounted value của tương lai.**

Quan hệ đệ quy này là xương sống của phần lớn Reinforcement Learning cổ điển.

## Những nhầm lẫn thường gặp

### “Value là xác suất thắng”

Chỉ đúng trong một số reward setup đặc biệt. Nói chung value là expected return.

### “Bellman equation cho ra value ngay lập tức”

Không. Nó là một consistency relation. Ta vẫn phải solve hoặc estimate value bằng Dynamic Programming, sampling hoặc function approximation.

### “Q-value và reward giống nhau”

Không. Q chứa expected long-term return, không chỉ immediate reward.

## Liên kết kiến thức

Bellman equation nối recursive algorithm, Dynamic Programming và bootstrapping. Chapter tiếp theo dùng environment model đã biết để tính value và policy một cách hệ thống.

Xem tiếp: [Dynamic Programming](./03_dynamic_programming.md).