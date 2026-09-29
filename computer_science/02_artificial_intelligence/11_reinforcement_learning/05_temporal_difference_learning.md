# Temporal Difference học tập (learning / 학습)

> **Mạch đọc:** Đặt **Temporal Difference học tập (learning / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao TD cần tồn tại?** sang **Sampling + Bootstrapping**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Temporal Difference (TD / 시간차 학습)** học tập (learning / 학습) kết hợp hai ý tưởng: học từ sampled experience như Monte Carlo, nhưng cập nhật (update / 업데이트) bằng **bootstrapping** như động (dynamic / 동적) Programming.

One-step TD mục tiêu (target / 대상):

\[
R_{t+1}+\gamma V(S_{t+1})
\]

TD lỗi (error / 오류):

\[
\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)
\]

Cập nhật (update / 업데이트):

\[
V(S_t)\leftarrow V(S_t)+\alpha\delta_t
\]

## Vì sao TD cần tồn tại?

Monte Carlo phải chờ episode kết thúc mới có full return. TD có thể cập nhật (update / 업데이트) ngay sau mỗi chuyển tiếp (transition / 전이). Điều này quan trọng cho continuing tasks và long episodes.

## Sampling + Bootstrapping

TD không cần known chuyển tiếp (transition / 전이) mô hình (model / 모델); nó lấy mẫu (sample / 표본) `S_{t+1},R_{t+1}` từ môi trường (environment / 환경). Nhưng mục tiêu (target / 대상) dùng hiện tại (current / 현재) estimate `V(S_{t+1})`, vì vậy bootstrap.

```text
DP: expectation + bootstrap
MC: sample + no bootstrap
TD: sample + bootstrap
```

## Độ lệch (bias / 편향)–Variance

TD mục tiêu (target / 대상) phụ thuộc estimate chưa hoàn hảo nên có độ lệch (bias / 편향). Nhưng vì chỉ dùng một-step randomness, variance thường thấp hơn full-return Monte Carlo.

Đây là classic độ lệch (bias / 편향)–variance sự đánh đổi (trade-off / 트레이드오프).

## TD Prediction

Với fixed chính sách (policy / 정책), TD(0) cập nhật (update / 업데이트) online từng step. Under suitable conditions tabular TD converges tới true `V^π`.

## n-Step TD

Thay one-step mục tiêu (target / 대상) bằng:

\[
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n V(S_{t+n})
\]

`n=1` gần TD(0); `n` lớn tiến gần Monte Carlo.

## Eligibility Traces và TD(λ)

TD(λ) kết hợp returns ở nhiều horizons. Eligibility dấu vết (trace / 추적) ghi “recently active” states/features để TD lỗi (error / 오류) hiện tại credit backward nhiều bước.

Dấu vết (trace / 추적) đơn giản:

\[
e_t(s)=\gamma\lambda e_{t-1}(s)+\mathbf 1[S_t=s]
\]

Cập nhật (update / 업데이트):

\[
V(s)\leftarrow V(s)+\alpha\delta_t e_t(s)
\]

`λ` điều khiển mức dài của credit assignment.

## SARSA

On-policy TD điều khiển (control / 제어):

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)]
\]

Tên SARSA đến từ tuple:

```text
S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}
```

Vì mục tiêu (target / 대상) dùng actual next hành động (action / 동작) theo hiện tại (current / 현재) hành vi (behavior / 동작) chính sách (policy / 정책), SARSA là on-policy.

## Q-Learning Preview

Q-learning thay next actual hành động (action / 동작) bằng greedy max:

\[
R+\gamma\max_{a'}Q(s',a')
\]

nên off-policy. Chapter kế tiếp đi sâu.

## Why TD Can Learn Before kết quả (outcome / 결과)

Nếu trạng thái (state / 상태) B đã có giá trị (value / 값) estimate tốt, chuyển tiếp (transition / 전이) A→B cho phép A cập nhật (update / 업데이트) ngay mà không cần chờ reward cuối. kiến thức (knowledge / 지식) propagate through bootstrapping.

Đây là reason TD sample-efficient trong many sequential tasks.

## But Bootstrapping Can Propagate lỗi (error / 오류)

Nếu `V(B)` sai, A inherit part of lỗi (error / 오류). Repeated updates và sufficient experience mới correct dần.

Hàm (function / 함수) approximation + off-policy + bootstrapping là combination nổi tiếng dễ instability, thường gọi “deadly triad”.

## The Deadly Triad

Ba factors:

```text
function approximation
+ bootstrapping
+ off-policy learning
```

có thể làm divergence trong một số settings.

Deep RL algorithms dùng mục tiêu (target / 대상) networks, replay thiết kế (design / 설계), clipping và other stabilizers để manage.

## Continuing Tasks

TD đặc biệt phù hợp tasks không có natural terminal episode vì cập nhật (update / 업데이트) cục bộ (local / 로컬) theo chuyển tiếp (transition / 전이).

## Example

Nếu:

```text
V(A)=2
reward A→B = 1
V(B)=4
γ=0.9
```

TD mục tiêu (target / 대상):

\[
1+0.9\times4=4.6
\]

TD lỗi (error / 오류):

\[
4.6-2=2.6
\]

Với `α=0.1`:

\[
V(A)\leftarrow2+0.26=2.26
\]

Tác nhân (agent / 에이전트) không cần chờ episode kết thúc.

## TD lỗi (error / 오류) như Surprise

`δ` đo difference giữa predicted hiện tại (current / 현재) giá trị (value / 값) và reward + predicted next giá trị (value / 값). Nó có thể hiểu như temporal prediction lỗi (error / 오류): kết quả (outcome / 결과) tốt/xấu hơn expected bao nhiêu.

## Mô hình tư duy (mental model / 사고 모델)

> **TD học tương lai bằng cách dùng một bước thực tế cộng với estimate của phần tương lai còn lại.**

## Dùng chung (common / 공통) Misconceptions

### “Bootstrapping luôn xấu vì dùng prediction để train prediction”

Không. Nó tăng efficiency nhưng cần stability conditions.

### “TD(0) luôn tốt hơn MC”

Không. độ lệch (bias / 편향)–variance và tác vụ (task / 작업) cấu trúc (structure / 구조) quyết định.

### “SARSA và Q-learning giống nhau”

SARSA learns giá trị (value / 값) of hành vi (behavior / 동작)/hiện tại (current / 현재) chính sách (policy / 정책); Q-learning targets greedy optimal chính sách (policy / 정책) off-policy.

## Liên kết kiến thức (knowledge connection / 지식 연결)

TD là cầu nối (bridge / 브리지) từ giá trị (value / 값) prediction sang model-free điều khiển (control / 제어). Q-learning sẽ dùng TD lỗi (error / 오류) để học optimal hành động (action / 동작) values.

Xem tiếp: [Q-Learning](./06_q_learning.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 reinforcement learning foundations](./00_reinforcement_learning_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
