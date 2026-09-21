# Dynamic Programming trong Reinforcement Learning

**Quy hoạch động (Dynamic Programming — DP / 동적 계획법)** có thể giải MDP khi transition model và reward model đã biết. Ý tưởng cốt lõi là tận dụng Bellman recursion để chia bài toán quyết định dài hạn thành các subproblem liên kết thông qua value function.

DP không phải “training từ data” theo nghĩa Machine Learning hiện đại. Nó gần với planning hoặc exact computation trên một model đã biết, nhưng các concept của DP là nền tảng trực tiếp cho nhiều thuật toán RL.

## Policy Evaluation

Với policy cố định `π`, ta lặp Bellman expectation backup:

\[
V_{k+1}(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Dưới các giả định chuẩn của finite discounted MDP, chuỗi estimate này hội tụ về `V^π`.

Policy evaluation trả lời câu hỏi:

> Nếu agent tiếp tục làm theo policy hiện tại, mỗi state có expected return bao nhiêu?

## Policy Improvement

Sau khi có value estimate, ta có thể cải thiện policy bằng cách chọn action greedy:

\[
\pi'(s)=\arg\max_a\sum_{s'}P(s'|s,a)[R+\gamma V^\pi(s')]
\]

**Policy improvement theorem** cho biết policy mới tạo theo cách này không tệ hơn policy cũ trong điều kiện chuẩn.

## Policy Iteration

Policy iteration xen kẽ evaluation và improvement:

```text
khởi tạo π
lặp:
    evaluate V^π
    improve π theo hướng greedy
cho tới khi policy ổn định
```

Không phải lúc nào policy evaluation cũng cần hội tụ hoàn toàn trước bước improvement. **Modified Policy Iteration** dùng partial evaluation để giảm computation mỗi vòng.

## Value Iteration

Value iteration kết hợp evaluation và improvement trực tiếp trong một Bellman optimality update:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Sau khi value hội tụ đủ, policy có thể được trích xuất bằng cách chọn action greedy theo final value.

## Synchronous và Asynchronous Update

**Synchronous update** dùng vector value cũ `V_k` để cập nhật toàn bộ state thành `V_{k+1}`.

**Asynchronous** hoặc **in-place update** cập nhật từng state và có thể dùng ngay value mới nhất cho các state tiếp theo.

Asynchronous scheduling đôi khi hội tụ thực tế nhanh hơn vì thông tin mới được propagate ngay thay vì đợi hết một full sweep.

## Generalized Policy Iteration

Một mental model rộng hơn:

```text
policy evaluation
→ đẩy value về gần giá trị thật dưới policy hiện tại

policy improvement
→ đẩy policy về phía greedy đối với value hiện tại
```

Hai quá trình tương tác cho đến khi policy và value trở nên nhất quán.

Nhiều RL algorithm hiện đại có thể được nhìn như các phiên bản xấp xỉ của **Generalized Policy Iteration (GPI)**.

## Chi phí tính toán

Tabular DP cần sweep qua state, action và transition space. Nếu state space rất lớn, chi phí nhanh chóng trở nên không khả thi.

Đây là một biểu hiện của **curse of dimensionality**: số state có thể tăng theo cấp số nhân hoặc tổ hợp khi số dimension tăng.

Function approximation và sample-based RL xuất hiện một phần vì ta không thể enumerate toàn bộ state space trong các bài toán thực tế lớn.

## Giả định Known Model

DP cần biết `P` và `R`. Trong real-world problem, hai thành phần này thường chưa biết hoặc quá phức tạp để mô hình chính xác.

Model-based RL có thể học một approximate environment model, sau đó áp dụng planning hoặc DP-like computation trên model đã học.

## Ví dụ: Gridworld

Trong Gridworld:

```text
state  = ô hiện tại
Action = up / down / left / right
Reward = ví dụ -1 mỗi bước
goal   = terminal state
```

Value iteration propagate thông tin về “đường tới goal tốt đến đâu” ngược từ terminal state về các cell khác.

Sau nhiều sweep, value surface biểu diễn consequence dài hạn của việc bắt đầu ở từng vị trí.

## Bellman Operator

Định nghĩa optimal Bellman operator `T`:

\[
(TV)(s)=\max_a\mathbb E[R+\gamma V(S')]
\]

Trong discounted finite MDP, `T` là contraction dưới sup norm với factor `γ`. Property này là nền toán học giải thích vì sao value iteration hội tụ.

## DP và Shortest Path

Nhiều shortest-path algorithm cũng có cấu trúc đệ quy tương tự. Ví dụ Bellman-Ford repeatedly relax edge để propagate shortest-distance information.

RL mở rộng trực giác này sang environment có stochastic dynamics và reward tổng quát hơn distance.

## DP và Planning

Classical search thường reasoning theo trajectory. DP lưu value theo state và tái sử dụng value đó trên nhiều trajectory khác nhau.

Khi nhiều path cùng hội tụ vào một state, việc reuse state value giúp tránh lặp lại computation lớn.

## Hạn chế

Dynamic Programming có các giới hạn chính:

- cần environment model đã biết;
- thường cần enumerate state;
- expectation trên next state có thể đắt;
- lỗi trong model có thể propagate vào value;
- partial observability cần belief-state hoặc formulation phức tạp hơn.

## Mô hình tư duy

> **Dynamic Programming áp dụng Bellman recursion khi ta có bản đồ đầy đủ của environment; Reinforcement Learning học khi bản đồ chưa đầy đủ và ta chủ yếu thấy sample interaction.**

## Những nhầm lẫn thường gặp

### “DP là một online RL algorithm”

Không theo nghĩa phổ biến. DP thường giả định known model và full sweep nên gần planning hơn learning trực tiếp từ unknown environment.

### “Value iteration hội tụ nên luôn chạy nhanh”

Không. Mathematical convergence không đồng nghĩa practical cost thấp khi state space rất lớn.

### “Policy iteration luôn cần exact evaluation”

Không. Approximate hoặc partial evaluation vẫn tạo ra nhiều biến thể hữu ích.

## Liên kết kiến thức

DP nối Bellman equation với các sample-based method. Monte Carlo ở chapter tiếp theo bỏ giả định known transition model và học từ complete sampled return.

Xem tiếp: [Monte Carlo Methods](./04_monte_carlo_methods.md).