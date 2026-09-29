# Deep học tập (learning / 학습) huấn luyện (training / 학습) Dynamics: hiểu quá trình mô hình (model / 모델) thực sự học

> **Mạch đọc:** Đặt **Deep học tập (learning / 학습) huấn luyện (training / 학습) Dynamics: hiểu quá trình mô hình (model / 모델) thực sự học** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **huấn luyện (training / 학습) vòng lặp (loop / 루프)** sang **mất mát (loss / 손실) curve nói gì và không nói gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Huấn luyện (training / 학습) neural mạng (network / 네트워크) không chỉ là lặp `forward → backward → optimizer.step()`. Một mô hình (model / 모델) có thể giảm mất mát (loss / 손실) nhưng học biểu diễn (representation / 표현) kém, diverge sau vài nghìn steps, overfit, collapse, hoặc đạt cùng final mất mát (loss / 손실) bằng trajectories rất khác nhau. **huấn luyện (training / 학습) dynamics (학습 동역학 / động lực học huấn luyện)** nghiên cứu hành vi (behavior / 동작) của tối ưu hóa (optimization / 최적화) tiến trình (process / 프로세스) theo thời gian (time / 시간).

Hiểu dynamics giúp gỡ lỗi (debug / 디버그) hệ thống (system / 시스템) thay vì chỉ thử hyperparameters ngẫu nhiên.

## Huấn luyện (training / 학습) vòng lặp (loop / 루프)

Một vòng lặp (loop / 루프) cơ bản:

```text
for batch in data:
    prediction = model(batch.x)
    loss = objective(prediction, batch.y)
    gradients = backward(loss)
    optimizer.update(parameters, gradients)
```

Môi trường vận hành (production / 운영 환경) huấn luyện (training / 학습) thêm:

```text
mixed precision
loss scaling
gradient accumulation
clipping
learning-rate schedule
logging
checkpointing
validation
distributed synchronization
```

Mỗi thành phần (component / 컴포넌트) có thể thay dynamics.

## Mất mát (loss / 손실) curve nói gì và không nói gì?

Huấn luyện (training / 학습) mất mát (loss / 손실) giảm nghĩa optimizer đang improve mục tiêu (objective / 목표) trên observed batches. Nó không đảm bảo:

- kiểm tra hợp lệ (validation / 검증) improve;
- calibration improve;
- robustness improve;
- biểu diễn (representation / 표현) semantically useful;
- triển khai (deployment / 배포) chỉ số (metric / 지표) improve.

Kiểm tra hợp lệ (validation / 검증) curve và downstream slices vẫn cần.

Mất mát (loss / 손실) curve shape hữu ích:

- flat từ đầu → LR quá nhỏ, bad init, frozen params, dữ liệu (data / 데이터)/label bug;
- explode → LR too high, numerical issue, bad normalization;
- oscillate mạnh → high LR/noisy batch;
- huấn luyện (training / 학습) ↓ kiểm tra hợp lệ (validation / 검증) ↑ → overfitting/shift;
- sudden spikes → bad batch, overflow, unstable optimizer trạng thái (state / 상태).

## Học tập (learning / 학습) tỷ lệ (rate / 비율) Warmup

Early parameters random; LayerNorm/residual/optimizer moments chưa stable. Large LR ngay từ step 1 có thể destabilize.

Warmup increase LR gradually:

\[
\eta_t=\eta_{max}\frac{t}{T_{warmup}}
\]

sau đó decay.

Transformer huấn luyện (training / 학습) đặc biệt sensitive với warmup/batch/initialization tương tác (interaction / 상호작용).

## Update-to-Weight Ratio

Không chỉ độ dốc (gradient / 기울기) norm; cập nhật (update / 업데이트) magnitude so parameter magnitude hữu ích:

\[
ratio=\frac{\|\Delta\theta\|}{\|\theta\|}
\]

Ratio quá lớn có thể destroy learned cấu trúc (structure / 구조); quá nhỏ mô hình (model / 모델) gần như không move.

Fine-tuning pretrained mô hình (model / 모델) thường cần cập nhật (update / 업데이트) nhỏ hơn pretraining from scratch.

## Độ dốc (gradient / 기울기) Norm Tracking

Toàn cục (global / 전역)/per-layer độ dốc (gradient / 기울기) norm cho biết tín hiệu (signal / 신호) phân phối (distribution / 분포).

Nếu early layers norm ~0 còn late layers lớn → vanishing/blocked gradients.

Nếu một tầng (layer / 계층) huge norm → instability/nguồn (source / 소스) quy mô (scale / 규모) issue.

Độ dốc (gradient / 기울기) clipping logs nên nhánh học (track / 트랙) fraction of steps clipped; nếu 90% steps bị clip, threshold/LR/nguyên nhân gốc (root cause / 근본 원인) cần inspect.

## Activation Statistics

Theo dõi mean/std/max/zero fraction across layers.

Dying ReLU: zero fraction gần 100%.

Saturation sigmoid/tanh: activations near boundaries, gradients tiny.

Exploding activation: std tăng nhanh qua độ sâu (depth / 깊이).

Norm layers mask một phần symptom nhưng không eliminate all instability.

## Dữ liệu (data / 데이터) thứ tự (order / 순서) và Shuffling

SGD assumes batches representative enough. Nếu dữ liệu (data / 데이터) sorted by label/thời gian (time / 시간)/lĩnh vực (domain / 도메인), consecutive gradients biased và huấn luyện (training / 학습) oscillate/drift.

Shuffle improves IID approximation, nhưng thời gian (time / 시간)/online học tập (learning / 학습) đôi khi intentionally preserves thứ tự (order / 순서).

Large phân tán (distributed / 분산) huấn luyện (training / 학습) cần deterministic sharding để avoid duplicate/missing samples.

## Curriculum học tập (learning / 학습)

Huấn luyện (training / 학습) examples theo easier→harder thứ tự (order / 순서) có thể improve tối ưu hóa (optimization / 최적화) trong some tasks. Nhưng defining difficulty đúng không trivial.

LLM instruction tuning sometimes mixes dữ liệu (data / 데이터) sources/qualities with schedules. dữ liệu (data / 데이터) curriculum becomes tối ưu hóa (optimization / 최적화) parameter.

## Sampling phân phối (distribution / 분포)

Dataset composition quyết định độ dốc (gradient / 기울기) expectation.

Nếu nguồn (source / 소스) A 90% dữ liệu (data / 데이터), mục tiêu (objective / 목표) implicitly weights A mạnh. Reweight/resample sources changes what mô hình (model / 모델) learns even with same mất mát (loss / 손실) formula.

Large foundation-model huấn luyện (training / 학습) thường carefully thiết kế (design / 설계) dữ liệu (data / 데이터) mixture weights.

## Lớp (class / 클래스) Imbalance Dynamics

Rare lớp (class / 클래스) contributes few độ dốc (gradient / 기울기) updates. mô hình (model / 모델) may learn majority hành vi (behavior / 동작) early and never recover well.

Lớp (class / 클래스) weighting, balanced sampling, focal mất mát (loss / 손실) hoặc two-stage approaches thay đổi (change / 변경) độ dốc (gradient / 기울기) phân phối (distribution / 분포).

Monitor per-class metrics, not just mất mát (loss / 손실).

## Catastrophic Forgetting

Fine-tuning on narrow new dữ liệu (data / 데이터) can overwrite capabilities from pretraining.

Mitigations:

- lower học tập (learning / 학습) tỷ lệ (rate / 비율);
- mix old/general dữ liệu (data / 데이터);
- regularize toward cơ sở (base / 기반) weights;
- adapters/LoRA;
- freeze layers;
- rehearsal methods.

This is a training-dynamics issue across sequential distributions.

## Fine-Tuning vs tính năng (feature / 기능) Extraction

Frozen encoder + new head preserves pretrained biểu diễn (representation / 표현) but may underadapt.

Full fine-tuning gives flexibility but higher compute/forgetting/overfit rủi ro (risk / 위험).

Gradual unfreezing or layer-wise học tập (learning / 학습) rates create middle ground.

## Layer-Wise học tập (learning / 학습) Rates

Earlier pretrained layers may need smaller updates, tác vụ (task / 작업) head larger.

Discriminative LR:

```text
embedding / early layers → small LR
middle layers            → medium LR
new task head            → larger LR
```

Not universal but useful concept: parameters have different adaptation needs.

## Mất mát (loss / 손실) quy mô (scale / 규모) across Objectives

Multi-task mất mát (loss / 손실):

\[
L=\sum_k\lambda_kL_k
\]

Raw mất mát (loss / 손실) magnitudes/độ dốc (gradient / 기울기) norms differ. `λ_k` determines huấn luyện (training / 학습) influence, not just displayed number.

One tác vụ (task / 작업) may dominate dùng chung (shared / 공유) biểu diễn (representation / 표현) if gradients much larger.

Methods can dynamically balance tasks by bất định (uncertainty / 불확실성), độ dốc (gradient / 기울기) norms or xung đột (conflict / 충돌) handling.

## Độ dốc (gradient / 기울기) xung đột (conflict / 충돌) in Multi-Task học tập (learning / 학습)

Two tác vụ (task / 작업) gradients may điểm (point / 지점) opposing directions:

\[
g_1^Tg_2<0
\]

Dùng chung (shared / 공유) cập nhật (update / 업데이트) helps one tác vụ (task / 작업), hurts other. This is biểu diễn (representation / 표현)/mục tiêu (objective / 목표) sự đánh đổi (trade-off / 트레이드오프), not optimizer bug.

Understanding độ dốc (gradient / 기울기) hình học (geometry / 기하학) helps thiết kế (design / 설계) tác vụ (task / 작업) weights or separate adapters.

## Sharp mất mát (loss / 손실) Spikes

Large-model huấn luyện (training / 학습) sometimes sees transient spikes due to rare batches, optimizer trạng thái (state / 상태), precision or dữ liệu (data / 데이터) anomalies.

Operational phản hồi (response / 응답):

- log offending batch/nguồn (source / 소스);
- inspect độ dốc (gradient / 기울기)/activation norms;
- checkpoint frequently;
- skip/recover if non-finite;
- consider clipping/lower LR/dữ liệu (data / 데이터) cleaning.

Blind restart without diagnosis wastes compute.

## Checkpointing

Checkpoint should include more than mô hình (model / 모델) weights if resume chính xác (exact / 정확한) huấn luyện (training / 학습):

```text
model parameters
optimizer states
scheduler state
random generator states
data-loader position / sampler state
scaler state for mixed precision
training step / config
```

Tải (load / 로드) only weights with fresh optimizer is **fine-tuning/restart-like**, not chính xác (exact / 정확한) resume.

## Exponential Moving Average of Weights

Maintain:

\[
\theta_{EMA}\leftarrow\beta\theta_{EMA}+(1-\beta)\theta
\]

EMA weights smooth trajectory and often improve evaluation in vision/generative huấn luyện (training / 학습).

Stochastic Weight Averaging similarly average checkpoints/weights in later huấn luyện (training / 학습) to seek wider solution region.

## Kiểm tra hợp lệ (validation / 검증) Frequency

Validate too often → overhead; too rarely → miss overfitting/divergence and waste compute.

Frequency should tie to dataset kích thước (size / 크기), huấn luyện (training / 학습) chi phí (cost / 비용) và expected thay đổi (change / 변경) tỷ lệ (rate / 비율).

For massive pretraining, proxy metrics and periodic full eval suites coexist.

## Reproducibility

Chính xác (exact / 정확한) reproducibility difficult due to:

- random seeds;
- dữ liệu (data / 데이터) thứ tự (order / 순서);
- GPU nondeterministic kernels;
- phân tán (distributed / 분산) reduction thứ tự (order / 순서);
- thư viện (library / 라이브러리)/trình biên dịch (compiler / 컴파일러) versions;
- low-precision rounding.

Scientific/môi trường vận hành (production / 운영 환경) reproducibility often targets metric-level consistency rather than bitwise equality.

Log all configs and mã (code / 코드)/dữ liệu (data / 데이터) versions.

## Phân tán (distributed / 분산) huấn luyện (training / 학습) Dynamics

Dữ liệu (data / 데이터) parallelism averages gradients across workers. Effective toàn cục (global / 전역) batch:

\[
B_{toàn cục (global / 전역)}=B_{thiết bị (device / 장치)}\times N_{devices}\times accumulation
\]

Changing thiết bị (device / 장치) count can thay đổi (change / 변경) batch/LR dynamics if not adjusted.

Communication precision/thứ tự (order / 순서) may affect numerical kết quả (result / 결과).

Large-scale tối ưu hóa (optimization / 최적화) is thuật toán (algorithm / 알고리즘) + hệ thống phân tán (distributed system / 분산 시스템) jointly.

## Scaling Laws Preview

As mô hình (model / 모델)/dữ liệu (data / 데이터)/compute quy mô (scale / 규모), mất mát (loss / 손실) often follows approximate power-law relationships over regimes. This informs tài nguyên (resource / 자원) allocation but does not guarantee downstream năng lực (capability / 역량)/an toàn (safety / 안전).

Scaling laws will be detailed in LLM chapter.

## A systematic debugging thứ tự (order / 순서)

Khi huấn luyện (training / 학습) thất bại (fail / 실패), đừng ngay lập tức đổi optimizer. Check từ simple to complex:

1. dữ liệu (data / 데이터)/labels correct?
2. Can tiny subset overfit? Nếu không, hiện thực (implementation / 구현)/mô hình (model / 모델) bug likely.
3. Forward outputs finite and reasonable?
4. mất mát (loss / 손실) hiện thực (implementation / 구현) correct?
5. Gradients nonzero/finite?
6. LR/cập nhật (update / 업데이트) magnitude reasonable?
7. Activation/độ dốc (gradient / 기울기) stats stable?
8. kiểm tra hợp lệ (validation / 검증) split correct/no leakage?
9. sức chứa (capacity / 용량)/regularization adequate?
10. phân tán (distributed / 분산)/mixed-precision issues?

**Overfit a tiny batch** là diagnostic cực mạnh: mô hình (model / 모델) đủ expressive nên phải memorize vài examples. Nếu không, chuỗi xử lý (pipeline / 파이프라인)/huấn luyện (training / 학습) bug.

## Mô hình tư duy (mental model / 사고 모델)

> huấn luyện (training / 학습) là một dynamical hệ thống (system / 시스템) trong parameter không gian (space / 공간), được điều khiển bởi dữ liệu (data / 데이터) chuỗi (sequence / 시퀀스), mục tiêu (objective / 목표), optimizer, schedule, numerical precision và kiến trúc (architecture / 아키텍처).

Không chỉ final hyperparameters mà cả trajectory quan trọng.

## Dùng chung (common / 공통) Misconceptions

### “mất mát (loss / 손실) đang giảm nên huấn luyện (training / 학습) bình thường”

Có thể kiểm tra hợp lệ (validation / 검증) degrade, mô hình (model / 모델) exploit shortcut hoặc dữ liệu (data / 데이터) leakage.

### “Same seed nghĩa chính xác (exact / 정확한) same run”

Phân tán (distributed / 분산) GPU operations có thể nondeterministic.

### “Checkpoint chỉ cần weights”

Chính xác (exact / 정확한) resume cần optimizer/scheduler/RNG/dữ liệu (data / 데이터) position.

### “huấn luyện (training / 학습) instability luôn do học tập (learning / 학습) tỷ lệ (rate / 비율)”

LR dùng chung (common / 공통) cause nhưng dữ liệu (data / 데이터) anomalies, precision, normalization, initialization, độ dốc (gradient / 기울기) explosion cũng có thể.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chapter này tổng hợp [Forward](./03_forward_propagation.md), [Backpropagation](./04_backpropagation.md), [Optimizers](./05_gradient_descent_and_optimizers.md), [Initialization/Normalization](./06_initialization_and_normalization.md), [Regularization](./07_regularization.md) và [Model Evaluation](../04_machine_learning/15_model_evaluation.md).

Nó là cầu sang `06_deep_learning_architectures/`, nơi kiến trúc (architecture / 아키텍처) cụ thể thay computation đồ thị (graph / 그래프) và huấn luyện (training / 학습) dynamics.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from linear models to neural networks](./00_from_linear_models_to_neural_networks.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
