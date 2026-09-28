# Tối ưu hóa (optimization / 최적화) cho Artificial Intelligence

> **Mạch đọc:** Đặt **tối ưu hóa (optimization / 최적화) cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **mục tiêu (objective / 목표) hàm (function / 함수)** sang **mất mát (loss / 손실), mục tiêu (objective / 목표) và chỉ số (metric / 지표) khác nhau**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tối ưu hóa (optimization / 최적화) là quá trình tìm giá trị của variables để một mục tiêu (objective / 목표) trở nên tốt hơn. Trong Machine học tập (learning / 학습), kiến trúc (architecture / 아키텍처) xác định lớp (class / 클래스) of functions mô hình (model / 모델) có thể biểu diễn, dữ liệu (data / 데이터) cung cấp examples, hàm mất mát (loss function / 손실 함수) định nghĩa hành vi (behavior / 동작) nào được coi là tốt, còn optimizer tìm parameters phù hợp mục tiêu (objective / 목표) đó.

Một misconception phổ biến là “huấn luyện (training / 학습) = độ dốc (gradient / 기울기) descent”. Chính xác hơn, huấn luyện (training / 학습) là học tập (learning / 학습) tiến trình (process / 프로세스) rộng hơn; tối ưu hóa (optimization / 최적화) là cơ chế (mechanism / 메커니즘) tìm parameters; gradient-based methods chỉ là một family algorithms. Hơn nữa, optimize rất tốt một mục tiêu (objective / 목표) sai vẫn có thể tạo hệ thống (system / 시스템) tệ. Vì vậy tối ưu hóa (optimization / 최적화) phải luôn được học cùng **mục tiêu (objective / 목표) thiết kế (design / 설계), các ràng buộc (constraints / 제약조건들) và evaluation**.

Xem trước: [Calculus for AI](./04_calculus_for_ai.md).

## Mục tiêu (objective / 목표) hàm (function / 함수)

General tối ưu hóa (optimization / 최적화) bài toán (problem / 문제):

\[
\theta^*=\arg\min_\theta J(\theta)
\]

Trong supervised học tập (learning / 학습):

\[
J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)+\lambda\Omega(\theta)
\]

Term đầu đo fit với dữ liệu (data / 데이터). `Ω(θ)` regularize parameters hoặc hành vi (behavior / 동작). `λ` kiểm soát sự đánh đổi (trade-off / 트레이드오프).

Nếu maximize reward `R`, ta có thể equivalently minimize `-R`. `argmin` và `argmax` nói về location của optimum, không phải giá trị (value / 값) minimum/maximum.

## Mất mát (loss / 손실), mục tiêu (objective / 목표) và chỉ số (metric / 지표) khác nhau

**hàm mất mát (loss function / 손실 함수)** thường là differentiable quantity optimizer minimize trên examples.

**mục tiêu (objective / 목표)** có thể gồm mất mát (loss / 손실) + regularization + các ràng buộc (constraints / 제약조건들)/penalties.

**Evaluation chỉ số (metric / 지표)** là quantity ta thực sự report hoặc care about, ví dụ accuracy, F1, revenue, an toàn (safety / 안전) violation tỷ lệ (rate / 비율).

Chỉ số (metric / 지표) không nhất thiết differentiable. Ta có thể optimize cross-entropy nhưng evaluate accuracy.

Đây là idea của **surrogate mất mát (loss / 손실)**: optimize quantity tractable có relationship với mục tiêu (target / 대상) chỉ số (metric / 지표).

Nếu surrogate và real mục tiêu (objective / 목표) misaligned, huấn luyện (training / 학습) mất mát (loss / 손실) giảm nhưng sản phẩm (product / 제품) kết quả (outcome / 결과) có thể không tốt hơn.

## Ràng buộc (constraint / 제약조건) tối ưu hóa (optimization / 최적화)

Không phải mục tiêu (objective / 목표) chỉ là minimize một scalar unconstrained.

Ví dụ:

\[
\min_\theta L(\theta)
\]

subject to:

\[
C(\theta)\le c
\]

Ràng buộc (constraint / 제약조건) có thể là độ trễ (latency / 지연 시간), bộ nhớ (memory / 메모리), fairness bound, năng lượng (energy / 에너지) ngân sách (budget / 예산) hoặc rủi ro (risk / 위험) limit.

Môi trường vận hành (production / 운영 환경) AI thường là multi-objective/ràng buộc (constraint / 제약조건) bài toán (problem / 문제):

```text
quality ↑
latency ↓
cost ↓
privacy risk ↓
safety violations ↓
```

Không có một mô hình (model / 모델) “best” độc lập ngữ cảnh (context / 맥락); có Pareto trade-offs.

## Convexity

Hàm (function / 함수) `f` convex nếu line segment giữa hai points trên đồ thị (graph / 그래프) nằm trên/above đồ thị (graph / 그래프) theo convexity inequality:

\[
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y)
\]

với `0≤λ≤1`.

Convex tối ưu hóa (optimization / 최적화) hấp dẫn vì cục bộ (local / 로컬) minimum cũng là toàn cục (global / 전역) minimum dưới suitable conditions.

Tuyến tính (linear / 선형) regression với squared mất mát (loss / 손실) là convex theo parameters. Logistic regression với tiêu chuẩn (standard / 표준) convex mất mát (loss / 손실) cũng convex.

Deep neural networks generally non-convex vì composition và parameter interactions tạo complex landscape.

## Cục bộ (local / 로컬) minima, saddle points và flat regions

Trong non-convex landscape, độ dốc (gradient / 기울기) bằng zero có thể là:

- cục bộ (local / 로컬) minimum;
- cục bộ (local / 로컬) maximum;
- saddle điểm (point / 지점);
- flat plateau.

High-dimensional neural networks có rất nhiều saddle/flat directions. tối ưu hóa (optimization / 최적화) hành vi (behavior / 동작) không nên được tưởng tượng chỉ như “quả bóng lăn xuống một cái bát”.

Landscape phụ thuộc parameterization và symmetries. Hai parameter sets khác nhau có thể represent same hàm (function / 함수).

## Độ dốc (gradient / 기울기) descent

Full-batch độ dốc (gradient / 기울기) descent:

\[
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t)
\]

`η` là học tập (learning / 학습) tỷ lệ (rate / 비율).

Nếu `η` quá nhỏ, progress chậm. Nếu quá lớn, updates có thể overshoot hoặc diverge.

Một quadratic 1D:

\[
J(w)=\frac{1}{2}aw^2
\]

có độ dốc (gradient / 기울기):

\[
J'(w)=aw
\]

Cập nhật (update / 업데이트):

\[
w_{t+1}=(1-\eta a)w_t
\]

Từ đây thấy học tập (learning / 학습) tỷ lệ (rate / 비율) stability phụ thuộc curvature `a`. Một học tập (learning / 학습) tỷ lệ (rate / 비율) phù hợp direction flat có thể quá lớn ở direction steep.

## Stochastic độ dốc (gradient / 기울기) Descent

Dataset lớn khiến compute full độ dốc (gradient / 기울기) expensive. SGD dùng one mẫu (sample / 표본) hoặc mini-batch:

\[
g_t=\frac{1}{B}\sum_{i\in\mathcal{B}_t}\nabla L_i(\theta_t)
\]

\[
\theta_{t+1}=\theta_t-\eta g_t
\]

`g_t` là noisy estimate của full độ dốc (gradient / 기울기).

Noise không chỉ là drawback. Nó giảm compute/cập nhật (update / 업데이트), có thể giúp exploration landscape và tạo implicit regularization effects.

Hiện đại (modern / 현대적) “SGD” trong practice thường nghĩa mini-batch SGD, không phải exactly one mẫu (sample / 표본).

## Batch kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)

Larger batch:

- độ dốc (gradient / 기울기) estimate ít noisy hơn;
- hardware utilization có thể tốt hơn;
- bộ nhớ (memory / 메모리) demand cao hơn;
- ít parameter updates trên mỗi epoch;
- generalization/huấn luyện (training / 학습) dynamics có thể đổi.

Small batch:

- noisy gradients hơn;
- nhiều updates hơn;
- bộ nhớ (memory / 메모리) nhẹ hơn;
- hardware thông lượng (throughput / 처리량) có thể kém nếu quá nhỏ.

Không có batch kích thước (size / 크기) universally optimal. Nó tương tác học tập (learning / 학습) tỷ lệ (rate / 비율), optimizer, mô hình (model / 모델), hardware và dataset quy mô (scale / 규모).

## Momentum

Vanilla SGD dễ oscillate trong ravine có curvature khác nhau theo axes.

Momentum giữ velocity:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Mô hình tư duy (mental model / 사고 모델): gradients consistent qua nhiều steps accumulate, oscillation alternating directions partly cancel.

Momentum không phải vật lý (physical / 물리적) momentum chính xác (exact / 정확한), nhưng analogy hữu ích vừa phải.

## Nesterov momentum

Nesterov-style phương thức (method / 메서드) evaluates/look-ahead độ dốc (gradient / 기울기) relative to momentum-shifted điểm (point / 지점) trong một formulation phổ biến. Nó có theoretical advantages trong convex settings và variants practical.

Khung phần mềm (framework / 프레임워크) implementations có conventions khác nhau, nên khi reproduce kết quả (result / 결과) cần check chính xác (exact / 정확한) optimizer definition thay vì chỉ name.

## Adaptive học tập (learning / 학습) rates

### AdaGrad

AdaGrad accumulate squared gradients:

\[
s_t=s_{t-1}+g_t^2
\]

và quy mô (scale / 규모) cập nhật (update / 업데이트):

\[
\theta\leftarrow\theta-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Parameters có historical large gradients nhận smaller effective học tập (learning / 학습) tỷ lệ (rate / 비율).

Useful cho sparse features nhưng accumulated denominator chỉ tăng, có thể làm học tập (learning / 학습) tỷ lệ (rate / 비율) decay quá mạnh.

### RMSProp

RMSProp dùng exponential moving average:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

tránh accumulation không giới hạn của AdaGrad.

### Adam

Adam combine first moment và second moment estimates:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Sau độ lệch (bias / 편향) correction:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\quad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

Cập nhật (update / 업데이트):

\[
\theta_{t+1}=
\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam phổ biến vì robust across many tasks, nhưng không automatically best mọi setting.

## AdamW và weight decay

L2 regularization và weight decay có equivalence trong simple SGD settings, nhưng với adaptive optimizer chúng không necessarily equivalent.

AdamW decouples weight decay khỏi gradient-based adaptive scaling:

\[
\theta\leftarrow (1-\eta\lambda)\theta-	ext{AdamUpdate}
\]

Đây là reason AdamW phổ biến trong Transformer huấn luyện (training / 학습).

## Learning-rate schedule

Học tập (learning / 학습) tỷ lệ (rate / 비율) hiếm khi giữ constant từ đầu tới cuối large huấn luyện (training / 학습).

Dùng chung (common / 공통) patterns:

- warmup;
- step decay;
- exponential decay;
- cosine decay;
- one-cycle-like schedules.

**Warmup** tăng học tập (learning / 학습) tỷ lệ (rate / 비율) từ nhỏ lên mục tiêu (target / 대상) trong early steps. Với Transformer, early tối ưu hóa (optimization / 최적화) có thể unstable khi moments/activations chưa settled.

Cosine schedule giảm smoothly:

\[
\eta_t=\eta_{min}+\frac{1}{2}(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

Schedule là part của tối ưu hóa (optimization / 최적화) thuật toán (algorithm / 알고리즘), không phải cosmetic cấu hình (config / 설정).

## Weight initialization và tối ưu hóa (optimization / 최적화)

Nếu weights quá lớn, activations/gradients có thể explode hoặc saturate. Quá nhỏ, signals có thể vanish.

Xavier/Glorot initialization cân variance theo fan-in/fan-out, useful với certain activations.

He/Kaiming initialization điều chỉnh cho ReLU-like activations.

Initialization không chỉ “random seed”; nó đặt starting hình học (geometry / 기하학) và tín hiệu (signal / 신호) quy mô (scale / 규모) cho tối ưu hóa (optimization / 최적화).

## Normalization và trainability

BatchNorm, LayerNorm và variants normalize activations theo different axes.

Ngoài regularization effects, normalization cải thiện tối ưu hóa (optimization / 최적화) conditioning và tín hiệu (signal / 신호) scales.

Transformer thường dùng LayerNorm/RMSNorm-like mechanisms vì chuỗi (sequence / 시퀀스)/batch ngữ nghĩa (semantics / 의미론) khác CNN.

Normalization placement (`pre-norm` vs `post-norm`) ảnh hưởng độ dốc (gradient / 기울기) luồng (flow / 흐름) và deep Transformer stability.

## Conditioning

Tối ưu hóa (optimization / 최적화) bài toán (problem / 문제) **ill-conditioned** khi curvature khác nhau rất mạnh theo directions.

Với quadratic Hessian eigenvalues từ `λ_min` tới `λ_max`, điều kiện (condition / 조건) number:

\[
\kappa=\frac{\lambda_{max}}{\lambda_{min}}
\]

large `κ` khiến độ dốc (gradient / 기울기) descent zig-zag và require conservative học tập (learning / 학습) tỷ lệ (rate / 비율).

Tính năng (feature / 기능) scaling, normalization, preconditioning và adaptive methods cố improve effective conditioning.

## Second-order methods

Newton cập nhật (update / 업데이트):

\[
\theta_{t+1}=\theta_t-H^{-1}\nabla J
\]

uses Hessian curvature.

Nếu mục tiêu (objective / 목표) locally quadratic, Newton can converge fast near optimum. Nhưng neural-network Hessian khổng lồ, lưu trữ (storage / 저장소)/inversion impossible trực tiếp.

Quasi-Newton methods như BFGS/L-BFGS approximate curvature và useful ở smaller problems, nhưng large-scale stochastic Deep học tập (learning / 학습) chủ yếu dùng first-order methods.

## Độ dốc (gradient / 기울기) clipping

Toàn cục (global / 전역) norm clipping:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

nếu độ dốc (gradient / 기울기) norm vượt threshold `c`.

Clipping giúp prevent catastrophic huge cập nhật (update / 업데이트), đặc biệt chuỗi (sequence / 시퀀스) các mô hình (models / 모델들). Nhưng nếu clipping xảy ra liên tục, có thể là symptom học tập (learning / 학습) tỷ lệ (rate / 비율), normalization hoặc numerical instability khác.

## Regularization và tối ưu hóa (optimization / 최적화) không hoàn toàn tách rời

L2 penalty thay mục tiêu (objective / 목표).

Dropout thay stochastic huấn luyện (training / 학습) dynamics.

Early stopping dừng tối ưu hóa (optimization / 최적화) trước khi fully fit huấn luyện (training / 학습) set.

Dữ liệu (data / 데이터) augmentation thay empirical phân phối (distribution / 분포) optimizer sees.

Do đó generalization hành vi (behavior / 동작) là tương tác (interaction / 상호작용) giữa mục tiêu (objective / 목표), dữ liệu (data / 데이터) và tối ưu hóa (optimization / 최적화) trajectory.

## Early stopping

Kiểm tra hợp lệ (validation / 검증) mất mát (loss / 손실) có thể bắt đầu tăng dù huấn luyện (training / 학습) mất mát (loss / 손실) tiếp tục giảm. Early stopping chọn checkpoint trước overfitting.

Đây là implicit regularization: ta giới hạn number of tối ưu hóa (optimization / 최적화) steps.

Nhưng noisy kiểm tra hợp lệ (validation / 검증) chỉ số (metric / 지표) có thể khiến stop quá sớm; practical các hệ thống (systems / 시스템들) dùng patience/smoothing/checkpoint chiến lược (strategy / 전략).

## Hyperparameters như outer tối ưu hóa (optimization / 최적화)

Parameters `θ` được optimizer học từ dữ liệu huấn luyện (training data / 학습 데이터). Hyperparameters `λ`, học tập (learning / 학습) tỷ lệ (rate / 비율), kiến trúc (architecture / 아키텍처) độ sâu (depth / 깊이), batch kích thước (size / 크기) thường được chọn bằng kiểm tra hợp lệ (validation / 검증) tiến trình (process / 프로세스).

Có thể nhìn:

```text
inner loop: train θ
outer loop: choose hyperparameters h
```

Grid tìm kiếm (search / 검색), random tìm kiếm (search / 검색), Bayesian tối ưu hóa (optimization / 최적화) và population-based methods là strategies cho outer bài toán (problem / 문제).

Nếu tune quá nhiều trên một kiểm tra hợp lệ (validation / 검증) set, kiểm tra hợp lệ (validation / 검증) overfitting cũng xảy ra.

## Multi-objective tối ưu hóa (optimization / 최적화)

Suppose hệ thống (system / 시스템) cần maximize chất lượng (quality / 품질) `Q` và minimize độ trễ (latency / 지연 시간) `C`:

\[
\max Q(\theta),\quad \min C(\theta)
\]

Một scalarized mục tiêu (objective / 목표):

\[
J=-Q+\lambda C
\]

encode sự đánh đổi (trade-off / 트레이드오프) qua `λ`, nhưng choice `λ` là giá trị (value / 값) judgment/nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항), không phải mathematics tự quyết định.

Pareto frontier chứa solutions không thể improve một mục tiêu (objective / 목표) mà không worsen mục tiêu (objective / 목표) khác.

AI triển khai (deployment / 배포) thường chọn điểm (point / 지점) trên frontier theo sản phẩm (product / 제품) các ràng buộc (constraints / 제약조건들).

## Constrained tối ưu hóa (optimization / 최적화) và Lagrangian

Bài toán (problem / 문제):

\[
\min_x f(x)\quad \văn bản (text / 텍스트){s.t.}\quad g(x)\le0
\]

Lagrangian:

\[
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x)
\]

với `λ≥0` trong inequality setting.

Lagrange multipliers có interpretation shadow price: chi phí (cost / 비용) marginal của ràng buộc (constraint / 제약조건).

Idea này xuất hiện trong fairness các ràng buộc (constraints / 제약조건들), tài nguyên (resource / 자원) allocation và Reinforcement học tập (learning / 학습) constrained objectives.

## Tối ưu hóa (optimization / 최적화) trong Reinforcement học tập (learning / 학습)

RL tối ưu expected cumulative reward:

\[
J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]
\]

Độ dốc (gradient / 기울기) khó hơn supervised học tập (learning / 학습) vì hành động (action / 동작) sampling influence future states và reward.

Chính sách (policy / 정책) độ dốc (gradient / 기울기) theorem cho độ dốc (gradient / 기울기) estimator dựa trên log-policy:

\[
\nabla_\theta J
=\mathbb{E}[R\nabla_\theta\log\pi_\theta(a\mid s)]
\]

Noise/variance rất lớn, dẫn tới baselines, actor-critic và advanced tối ưu hóa (optimization / 최적화) methods.

## Tối ưu hóa (optimization / 최적화) trong LLM pretraining

LLM pretraining mục tiêu (objective / 목표) thường next-token cross-entropy trên huge đơn vị từ (token / 토큰) corpus.

Quy mô (scale / 규모) tạo challenges:

- phân tán (distributed / 분산) độ dốc (gradient / 기울기) aggregation;
- bộ nhớ (memory / 메모리) bandwidth;
- mixed precision;
- optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리);
- learning-rate schedule;
- độ dốc (gradient / 기울기) clipping;
- checkpointing;
- dữ liệu (data / 데이터) thứ tự (ordering / 순서).

Tối ưu hóa (optimization / 최적화) không chỉ là equation; nó là phân tán (distributed / 분산) các hệ thống (systems / 시스템들) bài toán (problem / 문제) ở large quy mô (scale / 규모).

## Tối ưu hóa (optimization / 최적화) trong alignment

Instruction tuning vẫn supervised tối ưu hóa (optimization / 최적화) trên curated responses.

Preference tối ưu hóa (optimization / 최적화) dùng human/mô hình (model / 모델) preference dữ liệu (data / 데이터). RLHF, PPO-style objectives, DPO-like methods encode different tối ưu hóa (optimization / 최적화) formulations.

Quan trọng: optimizer không biết “helpful” hay “safe” theo human sense. Nó chỉ thấy mathematical mục tiêu (objective / 목표) constructed from dữ liệu (data / 데이터)/rewards/preferences.

> An optimizer is powerful at finding what the mục tiêu (objective / 목표) rewards, not what the designer vaguely intended.

Liên kết (connection / 연결) này là cốt lõi (core / 핵심) của specification gaming và alignment.

## Reward hacking / specification gaming

Nếu mục tiêu (objective / 목표) proxy không exactly match desired kết quả (outcome / 결과), tác nhân (agent / 에이전트)/mô hình (model / 모델) có thể exploit loophole.

Ví dụ simple tác nhân (agent / 에이전트) rewarded “number of items picked” có thể repeatedly pick/drop same item nếu môi trường (environment / 환경) allows và reward definition không prevent.

Trong ML sản phẩm (product / 제품), optimizing click-through tỷ lệ (rate / 비율) alone có thể encourage sensational content dù long-term người dùng (user / 사용자) satisfaction giảm.

Tối ưu hóa (optimization / 최적화) amplifies chỉ số (metric / 지표) thiết kế (design / 설계) mistakes.

## No Free Lunch intuition

Không optimizer hoặc mô hình (model / 모델) universally best trên mọi possible bài toán (problem / 문제). hiệu năng (performance / 성능) dựa vào structural các giả định (assumptions / 가정들)/inductive biases về lớp (class / 클래스) of tasks.

Adam mạnh trong nhiều Deep học tập (learning / 학습) tasks, nhưng không có theorem “Adam always best”. Hyperparameter defaults cũng là lĩnh vực (domain / 도메인) priors, không universal constants.

## Mô hình tư duy (mental model / 사고 모델)

```text
Model architecture → những functions nào có thể represent
Loss/objective      → behavior nào được rewarded
Gradient            → local direction signal
Optimizer           → rule biến signal thành parameter updates
Schedule            → update scale thay đổi theo thời gian
Regularization      → preference ngoài pure training fit
Constraints         → boundaries system không được vượt
Evaluation          → objective có thực sự map tới desired outcome không
```

## Dùng chung (common / 공통) Misconceptions

### “mất mát (loss / 손실) càng thấp thì mô hình (model / 모델) càng tốt”

Chỉ trên mục tiêu (objective / 목표)/dataset đang optimize. Generalization, calibration, an toàn (safety / 안전) và sản phẩm (product / 제품) metrics có thể khác.

### “Adam luôn tốt hơn SGD vì hiện đại hơn”

Optimizer choice phụ thuộc tác vụ (task / 작업), tuning và goal. SGD với momentum vẫn mạnh trong nhiều vision settings; Adam/AdamW phổ biến cho Transformers.

### “toàn cục (global / 전역) minimum luôn cần thiết”

Trong Deep học tập (learning / 학습), solution có good generalization quan trọng hơn mathematical toàn cục (global / 전역) minimum của huấn luyện (training / 학습) mất mát (loss / 손실). Nhiều parameter solutions có near-zero mất mát (loss / 손실).

### “tối ưu hóa (optimization / 최적화) tự tìm đúng hành vi (behavior / 동작) nếu mô hình (model / 모델) đủ mạnh”

Không. Optimizer faithfully follows provided tín hiệu (signal / 신호); mis-specified objectives tạo misaligned hành vi (behavior / 동작).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tối ưu hóa (optimization / 최적화) nối [Calculus](./04_calculus_for_ai.md) với Machine học tập (learning / 학습) huấn luyện (training / 학습) và nối trực tiếp tới AI an toàn (safety / 안전) qua mục tiêu (objective / 목표) specification. Sau này SGD/AdamW sẽ quay lại trong Neural Networks; constrained and chính sách (policy / 정책) tối ưu hóa (optimization / 최적화) quay lại trong Reinforcement học tập (learning / 학습); preference objectives quay lại trong LLM Alignment.

Khi huấn luyện (training / 학습) fails, đừng chỉ đổi optimizer. Hãy kiểm tra mục tiêu (objective / 목표), dữ liệu (data / 데이터) quy mô (scale / 규모), normalization, độ dốc (gradient / 기울기) statistics, learning-rate schedule, batch kích thước (size / 크기), initialization và numerical precision như một coupled hệ thống (system / 시스템).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mathematics for ai](./00_mathematics_for_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
