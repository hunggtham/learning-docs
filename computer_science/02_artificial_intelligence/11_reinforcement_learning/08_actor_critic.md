# Actor–Critic

**Actor–Critic (액터-크리틱)** kết hợp hai thành phần:

- **Actor**: policy `π_θ(a|s)` quyết định action;
- **Critic**: value estimator `V_w(s)` hoặc `Q_w(s,a)` đánh giá state hoặc action.

Actor học từ feedback của critic; critic học dự đoán long-term return.

```text
state
→ Actor chọn action
→ environment trả reward và next state
→ Critic tính TD / advantage signal
→ update Critic
→ update Actor
```

## Vì sao cần Critic?

REINFORCE dùng full Monte Carlo return nên gradient variance cao. Critic dùng value estimate để tạo learning signal có variance thấp hơn thông qua bootstrapping.

Một one-step TD error:

\[
\delta_t=R_{t+1}+\gamma V_w(S_{t+1})-V_w(S_t)
\]

có thể được dùng như approximate advantage cho actor:

\[
\theta\leftarrow\theta+\alpha\delta_t\nabla_\theta\log\pi_\theta(A_t|S_t)
\]

## Objective của Actor

Actor muốn tăng expected return. Critic giúp ước lượng action hiện tại tốt hơn baseline bao nhiêu.

- nếu `δ_t>0`, outcome tốt hơn kỳ vọng → tăng probability của action;
- nếu `δ_t<0`, outcome tệ hơn kỳ vọng → giảm probability tương đối.

Actor vì vậy không cần đợi complete return mới biết hướng update.

## Objective của Critic

Critic cố giảm value-prediction error, ví dụ:

\[
L_V=(R+\gamma V_w(s')-V_w(s))^2
\]

Actor và critic được học đồng thời nên target của mỗi bên cũng thay đổi theo thời gian. Đây là một coupled optimization problem, không phải hai supervised model độc lập.

## On-Policy Actor–Critic

Các algorithm thuộc family A2C/A3C sử dụng on-policy trajectory. Critic cung cấp advantage estimate để giảm variance so với pure Monte Carlo policy gradient.

On-policy method thường đơn giản hơn về distribution correction nhưng phải thu dữ liệu mới thường xuyên khi policy thay đổi.

## Off-Policy Actor–Critic

Các algorithm như DDPG, TD3 và SAC có thể học từ replay buffer.

Trong continuous action problem, actor có thể được optimize theo:

\[
\max_\theta Q_w(s,\pi_\theta(s))
\]

thay vì cần tính `argmax_a Q(s,a)` bằng exhaustive search.

## Trực giác DDPG

**Deep Deterministic Policy Gradient (DDPG)** dùng:

```text
deterministic actor
Q critic
replay buffer
target network
```

để xử lý continuous action.

DDPG có thể nhạy với hyperparameter và overestimation. TD3 cải thiện bằng double critic, delayed policy update và target policy smoothing.

## Soft Actor–Critic

**Soft Actor–Critic (SAC)** tối ưu return đồng thời khuyến khích entropy:

\[
J(\pi)=\mathbb E\left[\sum_t \gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

Entropy làm policy tiếp tục exploration và tránh collapse quá sớm.

SAC là một off-policy method mạnh cho nhiều continuous-control problem.

## Shared và Separate Network

Actor và critic có thể:

- dùng hai network độc lập;
- share một representation trunk rồi tách thành các head riêng.

Shared representation tiết kiệm compute và có thể tận dụng common feature, nhưng gradient của policy objective và value objective cũng có thể interfere.

## Critic Bias

Critic là learned approximator nên có thể sai có hệ thống.

Nếu critic overestimate một vùng action space, actor có thể học cách exploit lỗi đó thay vì thật sự tăng return trong environment.

Vấn đề này tương tự optimizer khai thác reward-model error.

Double critic, target network và conservative update là các cách giảm rủi ro.

## Advantage Estimation

Critic cho phép estimate:

\[
A(s,a)=Q(s,a)-V(s)
\]

hoặc GAE.

Advantage loại bỏ baseline về độ khó của state: action được đánh giá dựa trên việc nó tốt hơn hoặc tệ hơn mức thường đạt được từ state đó bao nhiêu.

## Hai Timescale học

Learning rate của actor và critic ảnh hưởng stability.

Critic phải theo kịp policy đủ tốt để cung cấp signal hữu ích, trong khi actor không nên thay đổi nhanh đến mức critic liên tục học một target đã lỗi thời.

Đây là lý do actor–critic thường nhạy với relative update rate.

## Target Network

Off-policy critic thường dùng target network cập nhật chậm để ổn định bootstrap target, tương tự DQN.

Nếu target thay đổi quá mạnh mỗi gradient step, value learning dễ dao động.

## Replay Buffer

Off-policy actor–critic tái sử dụng transition cũ từ replay buffer.

Điều này tăng sample efficiency nhưng tạo các vấn đề:

```text
distribution mismatch
stale experience
exploration coverage
sampling bias
```

Replay strategy trở thành một thành phần quan trọng của algorithm.

## Continuous Action Boundary

Actor output thường được đưa qua `tanh` rồi scale về action bound thực tế.

Với stochastic policy như SAC, khi biến đổi random variable bằng `tanh`, log-probability cần correction tương ứng với Jacobian của phép biến đổi.

Đây là ví dụ cho thấy implementation detail có liên hệ trực tiếp với probability theory.

## Partial Observability

Nếu observation không có Markov property, actor và critic có thể dùng recurrent network, Transformer memory hoặc belief representation để giữ information từ history.

## Multi-Agent Actor–Critic

Trong multi-agent RL, một pattern phổ biến là:

```text
training: centralized critic thấy nhiều thông tin chung
execution: mỗi actor chỉ dùng local observation
```

Cách này gọi là **centralized training with decentralized execution** trong nhiều formulation.

## Ví dụ: Robot Control

State có thể gồm joint position và velocity. Actor output motor torque; critic estimate future return của control action.

Continuous high-dimensional action làm Q-table không khả thi, trong khi actor cung cấp direct mapping từ state sang control.

## Actor–Critic và LLM

PPO-style RLHF về mặt khái niệm cũng có policy model và value/reward component.

Tuy nhiên LLM có action space là token sequence và reward thường xuất hiện ở sequence level, nên implementation khác đáng kể so với continuous-control RL.

## Failure Mode

Actor–critic có thể gặp:

- critic divergence;
- actor exploit critic error;
- exploration không đủ;
- value overestimation;
- entropy coefficient không ổn định;
- replay distribution mismatch;
- reward scale không phù hợp.

Những failure này cần được tách khi debug thay vì chỉ nói “RL không hội tụ”.

## Mô hình tư duy

> **Actor nói “tôi sẽ làm gì”; Critic nói “lựa chọn đó tốt hơn hoặc tệ hơn kỳ vọng bao nhiêu”.**

## Những nhầm lẫn thường gặp

### “Critic là một human reviewer”

Không. Trong RL, critic thường là learned value hoặc Q estimator. Human hoặc external evaluator có thể tạo reward, nhưng đó là vai trò khác.

### “Actor–Critic luôn on-policy”

Không. Có cả on-policy và off-policy family.

### “Critic luôn đúng”

Không. Critic là function approximator và có bias, variance, distribution shift như các learned model khác.

## Liên kết kiến thức

Actor–Critic kết hợp value-based RL với policy-based RL và là cầu trực tiếp sang Deep Reinforcement Learning.

Xem tiếp: [Deep Reinforcement Learning](./09_deep_reinforcement_learning.md).