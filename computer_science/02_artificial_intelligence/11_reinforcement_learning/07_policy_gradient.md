# Policy Gradient

Các value-based method như Q-learning học action value rồi suy ra policy. **Policy Gradient (정책 경사법)** đi theo hướng khác: tối ưu trực tiếp tham số của policy.

Một stochastic policy:

\[
\pi_\theta(a|s)
\]

Objective:

\[
J(\theta)=\mathbb E_{\tau\sim\pi_\theta}[G(\tau)]
\]

Ta muốn tính gradient:

\[
\nabla_\theta J(\theta)
\]

để điều chỉnh `θ` theo hướng tăng expected return.

## Vì sao tối ưu Policy trực tiếp?

Trong continuous action space, việc tính `argmax_a Q(s,a)` có thể khó hoặc không thực tế.

Policy network có thể output trực tiếp một action distribution hoặc parameter của distribution.

Ngoài ra stochastic policy hữu ích khi:

- exploration cần randomness ngay trong policy;
- optimal behavior không phải deterministic hoàn toàn;
- action space liên tục;
- ta muốn kiểm soát entropy hoặc độ đa dạng của hành vi.

## Log-Derivative Trick

Một identity quan trọng:

\[
\nabla_\theta \pi_\theta(a|s)=\pi_\theta(a|s)\nabla_\theta\log\pi_\theta(a|s)
\]

Policy-gradient theorem dẫn tới estimator dạng:

\[
\nabla_\theta J(\theta)\propto \mathbb E[ G_t\nabla_\theta\log\pi_\theta(A_t|S_t)]
\]

Trực giác:

- action dẫn tới return cao → tăng log-probability của action đó;
- action dẫn tới return thấp tương đối → giảm preference đối với action đó.

Điểm quan trọng là gradient không cần differentiate xuyên qua environment transition.

## REINFORCE

Thuật toán Monte Carlo policy gradient kinh điển **REINFORCE** dùng complete return:

\[
\theta\leftarrow\theta+\alpha G_t\nabla_\theta\log\pi_\theta(A_t|S_t)
\]

Cơ chế đơn giản nhưng gradient variance thường cao vì `G_t` phụ thuộc toàn future trajectory.

## Baseline

Ta có thể trừ một baseline `b(s)` mà không làm đổi expected gradient dưới các điều kiện chuẩn:

\[
(G_t-b(S_t))\nabla\log\pi(A_t|S_t)
\]

Baseline tự nhiên nhất là state value `V(s)`.

Khi dùng `V`, phần weight gần với advantage:

\[
A(s,a)=Q(s,a)-V(s)
\]

## Vì sao Baseline giảm Variance?

Nếu một episode có total reward cao, không có nghĩa mọi action trong episode đều tốt như nhau.

Baseline cho biết “ở state này bình thường expected return là bao nhiêu”, nhờ đó update dựa trên action tốt hoặc tệ **so với kỳ vọng tại chính state đó**.

## Policy Parameterization

Với discrete action:

```text
network logits
→ softmax
→ action distribution
```

Với continuous action, network có thể output parameter của Gaussian:

```text
μ(s), σ(s)
→ sample action
```

Choice của probability distribution tạo một inductive bias về loại action mà policy có thể biểu diễn.

## Entropy Regularization

Để policy không collapse thành deterministic behavior quá sớm, objective có thể thêm entropy bonus:

\[
J'=J+\beta H(\pi(\cdot|s))
\]

Entropy cao khuyến khích exploration và diversity.

Tuy nhiên nếu coefficient quá lớn, policy có thể tiếp tục random dù đã biết action tốt.

## Tính On-Policy

Vanilla policy gradient thường là on-policy. Dữ liệu được tạo bởi policy cũ nhanh chóng trở nên stale khi `θ` thay đổi.

Điều này thường làm sample efficiency thấp hơn các off-policy method có thể replay nhiều experience cũ.

## Importance Ratio

Khi update từ data được tạo bởi policy cũ, ta thường gặp tỷ lệ:

\[
r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
\]

Ratio này đo probability của sampled action đã thay đổi bao nhiêu dưới policy mới.

Nó là thành phần quan trọng trong các algorithm như PPO.

## Trực giác PPO

**Proximal Policy Optimization (PPO)** cố tránh policy update quá lớn bằng clipped surrogate objective:

\[
L^{clip}=\mathbb E[\min(r_tA_t,\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A_t)]
\]

Ý tưởng không phải “clip gradient” đơn giản, mà hạn chế lợi ích của việc đẩy ratio quá xa khỏi vùng gần policy cũ.

PPO phổ biến vì cân bằng relative simplicity với stability khá tốt trong nhiều setting, bao gồm một số RLHF pipeline.

## Trust-Region Intuition

Nếu policy thay đổi quá xa sau một update, data được thu dưới old policy không còn đại diện tốt cho new policy.

Trust-region hoặc proximal method buộc learning tiến từng bước đủ nhỏ để optimization ổn định hơn.

## Credit Assignment

Policy gradient vẫn gặp delayed reward. Một action đầu trajectory có thể chỉ nhận feedback qua reward xuất hiện rất xa về sau.

Advantage estimator và critic giúp truyền credit hiệu quả hơn thay vì dùng full return có variance lớn.

## Generalized Advantage Estimation

**Generalized Advantage Estimation (GAE)** kết hợp nhiều TD error theo horizon:

\[
\hat A_t^{GAE(\gamma,\lambda)}=\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}
\]

`λ` điều khiển một phần trade-off giữa bias và variance.

GAE đặc biệt phổ biến trong actor–critic và PPO implementation.

## Gradient Variance

Trajectory stochastic làm policy gradient noisy. Các kỹ thuật thường dùng để giảm variance gồm:

- batch lớn hơn;
- baseline;
- advantage normalization;
- GAE;
- reward normalization;
- entropy tuning.

Mục tiêu là cải thiện signal-to-noise của gradient mà không làm thay objective ngoài ý muốn.

## Reward Scale

Gradient magnitude phụ thuộc scale của reward và advantage.

Reward quá lớn có thể làm update bất ổn; reward quá nhỏ có thể làm learning chậm. Vì vậy reward normalization hoặc scale tuning là vấn đề implementation quan trọng.

## Policy Collapse

Nếu tối ưu quá mạnh theo một reward không hoàn hảo, policy có thể mất diversity hoặc exploit reward specification.

Trong alignment, KL constraint hoặc reference policy thường được dùng để hạn chế policy drift quá xa.

## Liên hệ với RLHF

Trong LLM, policy là distribution trên token. PPO-style RLHF có thể tối ưu sequence-level reward trong khi penalize divergence khỏi reference model:

\[
Reward'=Reward_{pref}-\beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Đây là một ứng dụng cụ thể của policy optimization, không phải định nghĩa đầy đủ của policy gradient.

## Mô hình tư duy

> **Policy gradient tăng xác suất những action tạo outcome tốt hơn baseline và giảm xác suất những action tương đối kém, bằng gradient trên log-probability của policy.**

## Những nhầm lẫn thường gặp

### “Policy gradient không cần value function”

REINFORCE cơ bản không bắt buộc critic, nhưng value baseline thường giảm variance rất mạnh.

### “PPO đảm bảo policy an toàn”

Không. PPO chỉ kiểm soát optimization step tương đối. Nó không đảm bảo reward đúng, dữ liệu an toàn hay behavior đáp ứng policy thực tế.

### “Direct policy optimization luôn tốt hơn Q-learning”

Không. Lựa chọn phụ thuộc action space, sample efficiency, stability và khả năng function approximation.

## Liên kết kiến thức

Policy gradient nối stochastic optimization, probability distribution và RL control. Actor–Critic ở chapter tiếp theo kết hợp policy gradient với learned value estimator để giảm variance và học hiệu quả hơn.

Xem tiếp: [Actor–Critic](./08_actor_critic.md).