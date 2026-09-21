# Temporal Difference Learning

**Temporal Difference (TD / 시간차 학습)** learning kết hợp hai ý tưởng: học từ sampled experience như Monte Carlo, nhưng update bằng **bootstrapping** như Dynamic Programming.

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

Monte Carlo phải chờ episode kết thúc mới có full return. TD có thể update ngay sau mỗi transition. Điều này quan trọng cho continuing tasks và long episodes.

## Sampling + Bootstrapping

TD không cần known transition model; nó lấy sample `S_{t+1},R_{t+1}` từ environment. Nhưng target dùng current estimate `V(S_{t+1})`, vì vậy bootstrap.

```text
DP: expectation + bootstrap
MC: sample + no bootstrap
TD: sample + bootstrap
```

## Bias–Variance

TD target phụ thuộc estimate chưa hoàn hảo nên có bias. Nhưng vì chỉ dùng một-step randomness, variance thường thấp hơn full-return Monte Carlo.

Đây là classic bias–variance trade-off.

## TD Prediction

Với fixed policy, TD(0) update online từng step. Under suitable conditions tabular TD converges tới true `V^π`.

## n-Step TD

Thay one-step target bằng:

\[
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n V(S_{t+n})
\]

`n=1` gần TD(0); `n` lớn tiến gần Monte Carlo.

## Eligibility Traces và TD(λ)

TD(λ) kết hợp returns ở nhiều horizons. Eligibility trace ghi “recently active” states/features để TD error hiện tại credit backward nhiều bước.

Trace đơn giản:

\[
e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf 1[S_t=s]
\]

Update:

\[
V(s)\leftarrow V(s)+\alpha\delta_t e_t(s)
\]

`λ` điều khiển mức dài của credit assignment.

## SARSA

On-policy TD control:

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)]
\]

Tên SARSA đến từ tuple:

```text
S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}
```

Vì target dùng actual next action theo current behavior policy, SARSA là on-policy.

## Q-Learning Preview

Q-learning thay next actual action bằng greedy max:

\[
R+\gamma\max_{a'}Q(s',a')
\]

nên off-policy. Chapter kế tiếp đi sâu.

## Why TD Can Learn Before Outcome

Nếu state B đã có value estimate tốt, transition A→B cho phép A update ngay mà không cần chờ reward cuối. Knowledge propagate through bootstrapping.

Đây là reason TD sample-efficient trong many sequential tasks.

## But Bootstrapping Can Propagate Error

Nếu `V(B)` sai, A inherit part of error. Repeated updates và sufficient experience mới correct dần.

Function approximation + off-policy + bootstrapping là combination nổi tiếng dễ instability, thường gọi “deadly triad”.

## The Deadly Triad

Ba factors:

```text
function approximation
+ bootstrapping
+ off-policy learning
```

có thể làm divergence trong một số settings.

Deep RL algorithms dùng target networks, replay design, clipping và other stabilizers để manage.

## Continuing Tasks

TD đặc biệt phù hợp tasks không có natural terminal episode vì update local theo transition.

## Example

Nếu:

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
V(A)\leftarrow2+0.26=2.26
\]

Agent không cần chờ episode kết thúc.

## TD Error như Surprise

`δ` đo difference giữa predicted current value và reward + predicted next value. Nó có thể hiểu như temporal prediction error: outcome tốt/xấu hơn expected bao nhiêu.

## Mental Model

> **TD học tương lai bằng cách dùng một bước thực tế cộng với estimate của phần tương lai còn lại.**

## Common Misconceptions

### “Bootstrapping luôn xấu vì dùng prediction để train prediction”

Không. Nó tăng efficiency nhưng cần stability conditions.

### “TD(0) luôn tốt hơn MC”

Không. Bias–variance và task structure quyết định.

### “SARSA và Q-learning giống nhau”

SARSA learns value of behavior/current policy; Q-learning targets greedy optimal policy off-policy.

## Knowledge Connection

TD là bridge từ value prediction sang model-free control. Q-learning sẽ dùng TD error để học optimal action values.

Xem tiếp: [Q-Learning](./06_q_learning.md).