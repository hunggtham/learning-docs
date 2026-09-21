# Markov Decision Process

**Quá trình quyết định Markov (Markov Decision Process — MDP / 마르코프 결정 과정)** là framework toán học cho bài toán ra quyết định tuần tự, trong đó state hiện tại được giả định chứa đủ thông tin liên quan để dự đoán dynamics tương lai khi biết action được chọn.

Một MDP thường được mô tả bằng tuple:

\[
(\mathcal S,\mathcal A,P,R,\gamma)
\]

trong đó:

- `S`: không gian trạng thái (state space);
- `A`: không gian hành động (action space);
- `P(s'|s,a)`: phân phối chuyển trạng thái (transition distribution);
- `R(s,a,s')`: reward;
- `γ`: discount factor.

## Markov Property

Giả định Markov viết:

\[
P(S_{t+1}\mid S_t,A_t,S_{t-1},...) = P(S_{t+1}\mid S_t,A_t)
\]

Nghĩa là nếu state representation đủ đầy đủ, quá khứ không cung cấp thêm thông tin cần thiết để dự đoán next transition ngoài thông tin đã có trong state hiện tại.

Đây là giả định về **cách biểu diễn state**, không phải tuyên bố rằng thế giới “không có history”. Nếu state bỏ mất thông tin quan trọng, Markov property sẽ không còn đúng.

Ví dụ trạng thái bàn cờ hiện tại có thể đủ để xác định legal move. Ngược lại, trong một hội thoại dài, chỉ giữ message mới nhất thường không đủ để đại diện cho toàn bộ state liên quan.

## Transition Model

`P(s'|s,a)` mô tả environment có thể chuyển sang state nào sau action.

Trường hợp xác định:

\[
s'=T(s,a)
\]

Trường hợp ngẫu nhiên cần một distribution trên các next state có thể xảy ra.

Ví dụ hệ thống autonomous driving khi phanh có outcome phụ thuộc road condition, sensor uncertainty và hành vi của các actor khác.

## Reward Function

Reward có thể phụ thuộc state, action và next state. Objective của agent không phải tối đa hóa immediate reward từng bước, mà tối đa hóa expected return dài hạn.

Chỉ cần thay cách định nghĩa reward, optimal policy có thể thay đổi hoàn toàn dù transition dynamics của environment giữ nguyên.

## Policy

Policy được viết:

\[
\pi(a|s)
\]

Khi policy cố định, nó cùng transition model tạo ra một Markov chain trên state. Khi đó bài toán từ “chọn action nào?” chuyển thành “policy hiện tại có value bao nhiêu?”.

## Xác suất của Trajectory

Một trajectory có thể viết:

\[
\tau=(s_0,a_0,r_1,s_1,a_1,...)
\]

Xác suất xuất hiện trajectory đó phụ thuộc initial state, policy và transition dynamics:

\[
P(\tau)=P(s_0)\prod_t \pi(a_t|s_t)P(s_{t+1}|s_t,a_t)
\]

Biểu thức này cho thấy policy không chỉ quyết định action; nó còn quyết định distribution của dữ liệu mà agent sẽ quan sát trong tương lai.

## Finite Horizon và Infinite Horizon

**Finite-horizon problem** có số bước giới hạn `T`. Optimal policy khi đó có thể phụ thuộc thời gian còn lại.

Trong **infinite-horizon discounted problem**, dưới các điều kiện thích hợp ta thường tìm stationary policy, tức policy không cần phụ thuộc trực tiếp vào chỉ số thời gian.

## Terminal State

**Terminal state** hoặc **absorbing state** kết thúc episode. Sau terminal state, không còn action hoặc future reward có ý nghĩa đối với episode đó.

Cách định nghĩa terminal condition ảnh hưởng trực tiếp return và learning target.

## MDP và Planning

Nếu `P` và `R` đã biết, ta có thể giải MDP bằng Dynamic Programming, ví dụ value iteration hoặc policy iteration.

Nếu transition hoặc reward model chưa biết, Reinforcement Learning học từ sample interaction.

Có thể nhìn ranh giới như sau:

```text
Known model + tối ưu policy → planning / control
Unknown model + experience → reinforcement learning
```

Ranh giới này không tuyệt đối vì model-based RL có thể học model rồi dùng planning trên model đã học.

## POMDP

Khi agent không quan sát được full state, ta có **Partially Observable Markov Decision Process (POMDP)**. Agent nhận observation `o_t` thay vì trực tiếp thấy `s_t`.

Một cách xử lý là duy trì **belief state**:

\[
b_t(s)=P(S_t=s\mid history)
\]

Belief state biểu diễn distribution tin tưởng của agent về hidden state thật dựa trên observation history.

## Thiết kế State

State quá nhỏ làm mất thông tin và khiến bài toán không còn gần Markov.

State quá lớn làm sample complexity và computation tăng.

Representation learning trong RL cố tìm representation giữ lại information quan trọng cho decision nhưng loại bớt chi tiết không cần thiết.

## Độ hạt của Action

Action space cũng là một design choice.

Low-level continuous action cho khả năng control chi tiết nhưng làm horizon dài và planning khó hơn. High-level action rút ngắn horizon nhưng cần abstraction đủ tốt.

Có thể liên hệ với LLM agent:

```text
click(x,y)          → action rất low-level
create_ticket(...)  → action high-level có semantics rõ
```

## Diễn giải Discount Factor

`γ` có thể được hiểu theo nhiều góc:

- mức ưu tiên reward gần hơn reward xa;
- effective horizon;
- công cụ toán học giúp tổng return hội tụ;
- xác suất tiếp tục process trong một số formulation.

Khi `γ` gần 1, effective horizon tăng mạnh; trực giác thường dùng là khoảng `1/(1-γ)`, nhưng đây không phải một identity chính xác cho mọi bài toán.

## Reward Scale

Scale của reward ảnh hưởng numerical optimization, learning rate và các hyperparameter dù trong một số formulation, nhân toàn bộ reward với hằng số dương không đổi optimal policy lý tưởng.

Vì vậy khi implementation, reward scale vẫn là vấn đề kỹ thuật cần quan tâm.

## Mô hình tư duy

> **MDP là một state machine có uncertainty, reward và lựa chọn action. RL học cách điều khiển state machine đó khi dynamics hoặc optimal policy chưa biết.**

## Những nhầm lẫn thường gặp

### “Markov nghĩa là ngẫu nhiên”

Không. Markov chỉ nói future độc lập có điều kiện với quá khứ khi đã biết present state. Transition hoàn toàn có thể deterministic.

### “State luôn bằng observation”

Chỉ đúng trong fully observable setting. Với POMDP, observation chỉ là tín hiệu gián tiếp về hidden state.

### “MDP chỉ dành cho game”

Không. Nó là nền tảng cho robotics, operations research, recommendation, resource allocation và sequential control.

## Liên kết kiến thức

MDP nối Probability, Dynamic Programming, Control Theory và cách thiết kế state cho agent.

Xem tiếp: [Value Function và Bellman Equation](./02_value_functions_and_bellman_equations.md).