# Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Gradient descent và optimizers trong deep learning**. Route đi từ gradient update → batch/stochastic/mini-batch → momentum/adaptive methods → schedules/stability → convergence diagnostics, để optimizer được đánh giá bằng dynamics chứ không chỉ tên.

Sau khi backpropagation tính độ dốc (gradient / 기울기), optimizer quyết định **parameters sẽ thay đổi như thế nào**. Đây là distinction quan trọng: độ dốc (gradient / 기울기) chỉ là cục bộ (local / 로컬) thông tin (information / 정보) về slope; optimizer là chính sách (policy / 정책) sử dụng thông tin (information / 정보) đó qua thời gian (time / 시간).

Deep học tập (learning / 학습) tối ưu hóa (optimization / 최적화) khó vì mục tiêu (objective / 목표) non-convex, quy mô (scale / 규모) parameters lớn, gradients noisy do mini-batches và curvature khác nhau theo directions. Vì vậy simple độ dốc (gradient / 기울기) Descent là nền để hiểu, nhưng practical huấn luyện (training / 학습) thường dùng SGD with momentum, Adam/AdamW và learning-rate schedules.

## Độ dốc (gradient / 기울기) Descent

Cập nhật (update / 업데이트) cơ bản:

\[
\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)
\]

`η` là học tập (learning / 학습) tỷ lệ (rate / 비율).

Độ dốc (gradient / 기울기) chỉ direction steepest increase under Euclidean norm locally; negative độ dốc (gradient / 기울기) giảm mất mát (loss / 손실) nhanh nhất cho infinitesimal step. Với finite step, học tập (learning / 학습) tỷ lệ (rate / 비율) quyết định cập nhật (update / 업데이트) có còn useful hay overshoot.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Full Batch, Stochastic và Mini-Batch** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Descent** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Học tập (learning / 학습) tỷ lệ (rate / 비율) là hyperparameter trọng yếu (critical / 중요)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Full Batch, Stochastic và Mini-Batch

Full-batch độ dốc (gradient / 기울기) dùng toàn dataset:

\[
g=\frac1N\sum_i\nabla L_i
\]

accurate nhưng expensive.

Stochastic độ dốc (gradient / 기울기) Descent theo nghĩa strict dùng một mẫu (sample / 표본). Practical “SGD” thường dùng mini-batch:

\[
g_B=\frac1{|B|}\sum_{i\in B}\nabla L_i
\]

Mini-batch độ dốc (gradient / 기울기) là noisy estimator của full độ dốc (gradient / 기울기). Noise không chỉ nuisance; nó có thể giúp exploration và implicit regularization.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Học tập (learning / 학습) tỷ lệ (rate / 비율) là hyperparameter trọng yếu (critical / 중요)** tiếp nhận điểm tựa từ **Full Batch, Stochastic và Mini-Batch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Momentum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Học tập (learning / 학습) tỷ lệ (rate / 비율) là hyperparameter trọng yếu (critical / 중요)

Quá nhỏ:

- huấn luyện (training / 학습) chậm;
- có thể stuck lâu ở flat regions.

Quá lớn:

- oscillation;
- divergence;
- NaN/Inf.

Học tập (learning / 학습) tỷ lệ (rate / 비율) thường quan trọng hơn nhiều optimizer-detail khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Momentum** tiếp nhận điểm tựa từ **Học tập (learning / 학습) tỷ lệ (rate / 비율) là hyperparameter trọng yếu (critical / 중요)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nesterov Momentum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Momentum

Momentum tích lũy direction qua steps:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Nó smooth noisy độ dốc (gradient / 기울기) và tăng tốc qua directions độ dốc (gradient / 기울기) consistently aligned, đồng thời giảm zig-zag trong ravine.

Có analogy vật lý (physical / 물리적) momentum nhưng đây là mathematical trạng thái (state / 상태), không phải vật lý thật.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Nesterov Momentum** tiếp nhận điểm tựa từ **Momentum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AdaGrad** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nesterov Momentum

Nesterov-style methods evaluate/look ahead theo momentum direction rồi correct. Ý tưởng là anticipate future position để cập nhật (update / 업데이트) responsive hơn.

Hiện thực (implementation / 구현) conventions khác nhau giữa frameworks; cần đọc chính xác (exact / 정확한) formula nếu reproducibility quan trọng.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **AdaGrad** tiếp nhận điểm tựa từ **Nesterov Momentum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RMSProp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AdaGrad

AdaGrad quy mô (scale / 규모) học tập (learning / 학습) tỷ lệ (rate / 비율) per parameter bằng accumulated squared gradients:

\[
s_t=s_{t-1}+g_t^2
\]

\[
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Parameters hiếm cập nhật (update / 업데이트) có effective học tập (learning / 학습) tỷ lệ (rate / 비율) lớn hơn, useful cho sparse features. Nhưng accumulator chỉ tăng nên học tập (learning / 학습) tỷ lệ (rate / 비율) có thể decay quá mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **RMSProp** tiếp nhận điểm tựa từ **AdaGrad** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adam** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RMSProp

RMSProp dùng exponential moving average:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

rồi normalize độ dốc (gradient / 기울기).

Điều này tránh AdaGrad accumulator grow forever.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Adam** tiếp nhận điểm tựa từ **RMSProp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AdamW và Weight Decay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adam

Adam kết hợp first-moment và second-moment estimates:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Độ lệch (bias / 편향) correction:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

Cập nhật (update / 업데이트):

\[
\theta_{t+1}=\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam adapts per-parameter step quy mô (scale / 규모) và thường easy-to-use cho Transformers.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **AdamW và Weight Decay** tiếp nhận điểm tựa từ **Adam** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Learning-Rate Schedules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AdamW và Weight Decay

L2 regularization và weight decay tương đương trong vanilla SGD dưới certain formulation, nhưng không hoàn toàn equivalent với adaptive optimizers.

**AdamW** decouples weight decay from gradient-based adaptive cập nhật (update / 업데이트):

\[
\theta\leftarrow(1-\eta\lambda)\theta-\eta\cdot AdamUpdate
\]

Đây là reason AdamW trở thành default phổ biến cho Transformer huấn luyện (training / 학습)/fine-tuning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Learning-Rate Schedules** tiếp nhận điểm tựa từ **AdamW và Weight Decay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weight Decay và parameters không decay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Learning-Rate Schedules

Constant LR hiếm là best cho long huấn luyện (training / 학습).

### Warmup

Bắt đầu LR nhỏ rồi tăng dần. Early huấn luyện (training / 학습) parameters/optimizer moments chưa stable; warmup giảm rủi ro (risk / 위험) unstable updates, đặc biệt Transformers/large batch.

### Step / Exponential Decay

Giảm LR theo milestones hoặc exponential schedule.

### Cosine Decay

\[
\eta_t=\eta_{min}+\frac12(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

smoothly giảm tới low LR.

### One-Cycle

LR tăng rồi giảm theo cycle, often combined momentum schedule.

Schedule là part của tối ưu hóa (optimization / 최적화) thuật toán (algorithm / 알고리즘), không decorative cấu hình (config / 설정).

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Weight Decay và parameters không decay** tiếp nhận điểm tựa từ **Learning-Rate Schedules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) Clipping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight Decay và parameters không decay

Hiện đại (modern / 현대적) huấn luyện (training / 학습) thường không apply weight decay cho mọi parameter như độ lệch (bias / 편향) hoặc normalization quy mô (scale / 규모). chính xác (exact / 정확한) parameter groups matter.

Fine-tuning recipe reproduce không được nếu chỉ ghi “AdamW lr=1e-4” mà bỏ weight-decay groups, warmup, batch kích thước (size / 크기) và schedule.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Độ dốc (gradient / 기울기) Clipping** tiếp nhận điểm tựa từ **Weight Decay và parameters không decay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch kích thước (size / 크기) và học tập (learning / 학습) tỷ lệ (rate / 비율)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Clipping

Toàn cục (global / 전역) norm clipping:

\[
g\leftarrow g\cdot\min(1,c/\|g\|)
\]

phòng rare exploding cập nhật (update / 업데이트). RNN/Transformer huấn luyện (training / 학습) thường dùng.

Clipping không chữa nguyên nhân gốc (root cause / 근본 원인) nếu độ dốc (gradient / 기울기) luôn explode; nó là an toàn (safety / 안전) cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Batch kích thước (size / 크기) và học tập (learning / 학습) tỷ lệ (rate / 비율)** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Clipping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) Noise và Generalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch kích thước (size / 크기) và học tập (learning / 학습) tỷ lệ (rate / 비율)

Larger batch giảm độ dốc (gradient / 기울기) noise và tăng hardware utilization nhưng dùng bộ nhớ (memory / 메모리) nhiều. Effective tối ưu hóa (optimization / 최적화) hành vi (behavior / 동작) đổi theo batch kích thước (size / 크기).

Tuyến tính (linear / 선형) scaling quy tắc (rule / 규칙) (`lr ∝ batch`) là heuristic under regimes, không universal law.

**độ dốc (gradient / 기울기) accumulation** mô phỏng larger effective batch bằng nhiều micro-batches trước optimizer step.

Nếu mất mát (loss / 손실) averaging/scaling sai, accumulated độ dốc (gradient / 기울기) magnitude cũng sai.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Độ dốc (gradient / 기울기) Noise và Generalization** tiếp nhận điểm tựa từ **Batch kích thước (size / 크기) và học tập (learning / 학습) tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-Convex Landscape** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Noise và Generalization

Small batches tạo noise có thể độ lệch (bias / 편향) optimizer toward flatter/wider regions và đôi khi improve generalization. Nhưng lý thuyết (theory / 이론) complex; không nên biến thành quy tắc (rule / 규칙) “small batch luôn generalize tốt hơn”.

Hardware thông lượng (throughput / 처리량) và normalization also matter.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Non-Convex Landscape** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Noise và Generalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sharpness và Flatness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Non-Convex Landscape

Deep mạng (network / 네트워크) mục tiêu (objective / 목표) có saddle points, flat directions, symmetries và many equivalent minima.

Goal practical không phải tìm toàn cục (global / 전역) minimum mathematically; ta cần solution low mất mát (loss / 손실) + good generalization under ngân sách (budget / 예산).

Parameter symmetries làm nhiều minima functionally equivalent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Sharpness và Flatness** tiếp nhận điểm tựa từ **Non-Convex Landscape** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mixed Precision và mất mát (loss / 손실) Scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sharpness và Flatness

Intuition: solution robust với small parameter perturbations có thể generalize better. Nhưng raw sharpness phụ thuộc parameterization/quy mô (scale / 규모), nên interpretation cần cẩn thận.

Methods like SAM optimize neighborhood-aware mục tiêu (objective / 목표), nhưng no single flatness chỉ số (metric / 지표) explains generalization universally.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Mixed Precision và mất mát (loss / 손실) Scaling** tiếp nhận điểm tựa từ **Sharpness và Flatness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mixed Precision và mất mát (loss / 손실) Scaling

FP16 gradients nhỏ có thể underflow. **mất mát (loss / 손실) scaling** multiply mất mát (loss / 손실) trước backward:

\[
L'=sL
\]

compute gradients scaled, rồi divide before cập nhật (update / 업데이트). động (dynamic / 동적) mất mát (loss / 손실) scaling adjust `s` nếu overflow.

BF16 có exponent phạm vi (range / 범위) lớn hơn nên less underflow-sensitive, dù precision mantissa thấp.

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Mixed Precision và mất mát (loss / 손실) Scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Choosing Optimizer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)

Adam stores parameters + gradients + first moment + second moment, thường nhiều lần parameter bộ nhớ (memory / 메모리). Với huge LLM, optimizer trạng thái (state / 상태) cực lớn.

Phân tán (distributed / 분산) huấn luyện (training / 학습) dùng sharding (ZeRO/FSDP-style) để split states across devices.

Tối ưu hóa (optimization / 최적화) vì vậy nối trực tiếp với hạ tầng (infrastructure / 인프라).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Choosing Optimizer** tiếp nhận điểm tựa từ **Optimizer trạng thái (state / 상태) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Choosing Optimizer

Không có universal winner.

- SGD+momentum: strong in vision/classical deep nets, bộ nhớ (memory / 메모리) lower.
- AdamW: dùng chung (common / 공통) Transformer/default fine-tuning.
- Adafactor/8-bit optimizer: reduce trạng thái (state / 상태) bộ nhớ (memory / 메모리) in large các mô hình (models / 모델들).
- Specialized optimizers có trade-offs khác.

Recipe phải evaluate cùng kiến trúc (architecture / 아키텍처)/dữ liệu (data / 데이터)/schedule.

> **Chuyển mạch:** Trong **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Choosing Optimizer** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Backprop = measure slope now
Optimizer = remember history + scale/update policy
Scheduler = change step policy over training time
```

> **Chuyển mạch:** Ở chặng này của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Adam luôn hội tụ nhanh hơn nên tốt hơn SGD”

Convergence speed, final generalization và tác vụ (task / 작업) differ. Không universal.

### “học tập (learning / 학습) tỷ lệ (rate / 비율) càng nhỏ càng an toàn”

Quá nhỏ có thể huấn luyện (training / 학습) impractically slow hoặc converge poor under fixed ngân sách (budget / 예산).

### “Weight decay chỉ là L2 regularization đổi tên”

Với adaptive optimizer, decoupled weight decay khác naive L2 độ dốc (gradient / 기울기) penalty.

### “Optimizer tự xử lý exploding gradients”

Adaptive scaling không đảm bảo; clipping/kiến trúc (architecture / 아키텍처)/normalization vẫn cần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ dốc (gradient / 기울기) Descent và Optimizers trong Deep học tập (learning / 학습)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Optimization](../01_mathematical_foundations/06_optimization.md), [Backpropagation](./04_backpropagation.md), [Initialization and Normalization](./06_initialization_and_normalization.md) và [Training Dynamics](./09_deep_learning_training_dynamics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
