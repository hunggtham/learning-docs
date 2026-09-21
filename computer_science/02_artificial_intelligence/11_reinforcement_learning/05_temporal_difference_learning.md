# Temporal-Difference Learning

**Học sai phân theo thời gian (Temporal-Difference Learning — TD / 시간차 학습)** kết hợp hai ý tưởng: học trực tiếp từ sampled experience như Monte Carlo, nhưng update bằng **bootstrapping** giống Dynamic Programming.

One-step TD target:

\[
R_{t+1}+\gamma V(S_{t+1})
\]

TD error:

\[
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)
\]

Update:

\[
V(S_t)\leftarrow V(S_t)+\alpha\delta_t
\]

## Vì sao TD cần tồn tại?

Monte Carlo thường phải chờ episode kết thúc mới có full return. TD có thể update ngay sau mỗi transition.

Điều này đặc biệt quan trọng với continuing task, episode rất dài hoặc environment nơi agent cần cải thiện online trước khi biết final outcome.

## Sampling kết hợp Bootstrapping

TD không cần biết transition model. Nó lấy sample `S_{t+1},R_{t+1}` trực tiếp từ environment.

Nhưng target lại dùng current estimate `V(S_{t+1})`, nên có bootstrapping:

```text
Dynamic Programming → expectation + bootstrap
Monte Carlo         → sample + không bootstrap
Temporal Difference → sample + bootstrap
```

TD vì vậy nằm giữa DP và Monte Carlo về cơ chế học.

## Bias–Variance Trade-off

TD target phụ thuộc một estimate chưa hoàn hảo nên có bootstrap bias.

Tuy nhiên vì target chỉ chứa randomness của một số transition gần thay vì toàn bộ remaining trajectory, variance thường thấp hơn complete-return Monte Carlo.

Đây là một bias–variance trade-off kinh điển trong RL.

## TD Prediction

Với policy cố định, TD(0) update online sau từng transition. Trong tabular setting, dưới các điều kiện phù hợp, TD có thể hội tụ tới true `V^π`.

Điểm mạnh là agent không cần đợi terminal state và không cần environment model.

## n-Step TD

Thay vì bootstrapping chỉ sau một bước, ta có thể dùng `n` reward trước khi bootstrap:

\[
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n V(S_{t+n})
\]

- `n=1`: gần TD(0);
- `n` lớn: dần gần Monte Carlo;
- `n` trung gian: trade-off giữa bias, variance và tốc độ propagate reward.

## Eligibility Trace và TD(λ)

**TD(λ)** kết hợp return ở nhiều horizon. Eligibility trace ghi lại state hoặc feature nào vừa hoạt động gần đây để TD error hiện tại có thể truyền credit ngược nhiều bước.

Một trace đơn giản:

\[
e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf 1[S_t=s]
\]

Update:

\[
V(s)\leftarrow V(s)+\alpha\delta_t e_t(s)
\]

`λ` điều khiển độ dài hiệu quả của credit assignment.

- `λ` nhỏ → gần one-step TD;
- `λ` lớn → ảnh hưởng trải dài hơn về quá khứ.

## SARSA

**SARSA** là on-policy TD control:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)]
\]

Tên SARSA đến từ sequence:

```text
S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}
```

Target dùng actual next action `A_{t+1}` được behavior policy chọn, vì vậy SARSA học value của policy đang thực sự hành động.

## Q-Learning: Preview

Q-learning thay actual next action bằng greedy maximum:

\[
R+\gamma\max_{a'}Q(s',a')
\]

Do target hướng tới greedy policy bất kể behavior policy hiện tại đang explore như thế nào, Q-learning là off-policy.

Chapter tiếp theo đi sâu vào cơ chế này.

## Vì sao TD học được trước Final Outcome?

Giả sử state B đã có value estimate tương đối tốt. Khi agent quan sát transition A→B, nó có thể update A ngay bằng:

```text
reward nhận được
+
discounted estimate của B
```

Không cần chờ trajectory từ B tới terminal hoàn tất lại lần nữa.

Bootstrapping nhờ đó giúp knowledge propagate từng bước và thường tăng sample efficiency.

## Nhưng Bootstrapping cũng truyền Error

Nếu `V(B)` sai, update cho A sẽ thừa hưởng một phần error đó.

Repeated experience và learning dynamics có thể sửa estimate dần, nhưng khi kết hợp với function approximation và off-policy learning, instability có thể xuất hiện.

## The Deadly Triad

Ba yếu tố nổi tiếng:

```text
function approximation
+ bootstrapping
+ off-policy learning
```

có thể làm một số thuật toán diverge.

Deep RL dùng nhiều stabilizer như target network, replay buffer design, gradient clipping hoặc double estimator để giảm các instability này.

## Continuing Task

TD đặc biệt phù hợp với bài toán không có terminal episode tự nhiên vì update chỉ cần local transition.

Ví dụ process control hoặc recommendation stream có thể học liên tục mà không cần “episode kết thúc”.

## Ví dụ số

Giả sử:

```text
V(A)=2
reward A→B = 1
V(B)=4
γ=0.9
```

TD target:

\[
1+0.9\times4=4.6
\]

TD error:

\[
4.6-2=2.6
\]

Với `α=0.1`:

\[
V(A)\leftarrow2+0.1\times2.6=2.26
\]

Agent đã học ngay sau transition A→B mà không phải chờ episode hoàn tất.

## TD Error như tín hiệu Surprise

`δ` đo chênh lệch giữa prediction hiện tại và observation + prediction ở next state.

Có thể hiểu trực giác:

```text
δ > 0 → kết quả tốt hơn kỳ vọng
δ < 0 → kết quả tệ hơn kỳ vọng
```

TD error vì vậy là temporal prediction error dùng để điều chỉnh value.

## Mô hình tư duy

> **TD học tương lai bằng một bước experience thật cộng với estimate của phần tương lai còn lại.**

## Những nhầm lẫn thường gặp

### “Bootstrapping luôn xấu vì dùng prediction để train prediction”

Không. Bootstrapping là nguồn sample efficiency quan trọng; vấn đề là stability và điều kiện hội tụ.

### “TD(0) luôn tốt hơn Monte Carlo”

Không. Task structure, variance, bias và function approximation quyết định phương pháp nào phù hợp hơn.

### “SARSA và Q-learning giống nhau”

Không. SARSA học value theo behavior policy hiện tại; Q-learning target greedy policy theo cách off-policy.

## Liên kết kiến thức

TD là cầu nối từ value prediction sang model-free control. Q-learning ở chapter tiếp theo dùng TD update để học optimal action value.

Xem tiếp: [Q-Learning](./06_q_learning.md).