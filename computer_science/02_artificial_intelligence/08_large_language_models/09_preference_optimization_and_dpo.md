# Preference Optimization và Direct Preference Optimization (DPO)

Sau RLHF cổ điển, một câu hỏi tự nhiên xuất hiện: nếu ta đã có preference pairs `chosen > rejected`, có nhất thiết phải train reward model riêng rồi chạy reinforcement learning như PPO không? **Direct Preference Optimization (DPO)** là một family method cho phép update language model trực tiếp từ preference data bằng objective supervised-like, giảm độ phức tạp pipeline.

## Preference pair

Một sample thường có dạng:

```text
prompt x
chosen response y_w
rejected response y_l
```

Ta muốn policy gán relative preference lớn hơn cho `y_w` so với `y_l`, nhưng vẫn giữ policy không drift quá xa reference model.

## Intuition của DPO

DPO xuất phát từ relationship giữa optimal KL-regularized reward policy và implicit reward. Thay vì explicitly fit `r(x,y)` rồi optimize it, objective có thể viết trực tiếp bằng log-probability ratios giữa policy hiện tại và reference policy.

Một form phổ biến:

\[
\mathcal L_{DPO}
=-\log\sigma\left(
\beta
\left[
\log\frac{\pi_\theta(y_w\mid x)}{\pi_{ref}(y_w\mid x)}
-
\log\frac{\pi_\theta(y_l\mid x)}{\pi_{ref}(y_l\mid x)}
\right]
\right)
\]

Không cần học thuộc formula ngay. Ý chính là model được khuyến khích **increase chosen relative to rejected**, sau khi accounting cho behavior ban đầu của reference model.

## Tại sao cần reference model?

Nếu chỉ maximize chosen response probability, model có thể overfit preference set và drift khỏi language distribution tốt đã học.

Reference model tạo anchor. Preference update đo “thay đổi so với policy ban đầu”, không chỉ raw likelihood.

## Vai trò của beta

`β` điều khiển strength của preference optimization/regularization relationship.

Trực giác:

```text
β nhỏ/lớn tùy convention implementation
→ trade-off giữa staying near reference và fitting preference strongly
```

Khi dùng library cụ thể cần kiểm tra exact parameterization; không nên chuyển meaning của `β` giữa implementations một cách máy móc.

## DPO không phải magic replacement cho RLHF

DPO đơn giản hóa engineering vì bỏ explicit reward model + on-policy RL loop. Nhưng nó vẫn phụ thuộc mạnh vào preference data quality và coverage.

Nếu preference dataset được thu từ policy cũ và model mới drift sang distribution khác, offline labels có thể không cover failure modes mới.

RL methods có advantage khi muốn online exploration hoặc reward signal phức tạp.

## Chosen response không phải absolute truth

Preference pair chỉ nói `A` được chọn hơn `B` theo guideline/annotator. Nếu cả hai đều sai, DPO vẫn có thể reinforce answer “ít tệ hơn”.

Vì vậy preference optimization không thay factual verification.

## Length bias

Annotators hoặc reward signals thường có bias theo response length. Nếu chosen responses thường dài hơn, model có thể learn verbosity preference ngoài intended quality.

Dataset analysis nên kiểm tra:

- length distribution;
- style artifacts;
- topic imbalance;
- annotator disagreement;
- position/order effects.

## Pair difficulty

Nếu chosen và rejected quá khác quality, signal dễ nhưng ít fine-grained. Nếu quá giống, labels có thể noisy.

Một good preference dataset thường cần mixture difficulty để model học distinctions meaningful.

## DPO và SFT data

Thường pipeline:

```text
pretrained model
→ SFT
→ preference optimization
```

SFT tạo stable instruction-following baseline. DPO sau đó refine ranking giữa alternative behaviors.

DPO trực tiếp từ weak base model có thể khó vì chosen samples quá xa current policy distribution.

## Other preference objectives

DPO không phải only method. Có nhiều variants/alternatives nhằm xử lý noise, reference-free setup, reward margins hoặc online updates. Tên algorithms thay đổi nhanh; mental model bền vững hơn là:

```text
preference data
+ policy/reference likelihood
→ objective làm preferred output tương đối có xác suất cao hơn
```

## Preference optimization và safety

Preference pairs có thể encode safe behavior, nhưng safety policy thường multi-dimensional và adversarial. Một model optimized trên static pairs vẫn có thể fail prompt injection/jailbreak.

Safety cần evaluation và defense-in-depth ở system layer.

## Offline distribution problem

Preference dataset phản ánh prompts và candidates đã sampled. Nếu deployment traffic khác mạnh, model may be optimized cho wrong region of input space.

Đây là connection với statistical distribution shift.

## Mental Model

> DPO biến “human thích A hơn B” thành **relative likelihood update** trực tiếp trên policy, thay vì bắt buộc xây reward model rồi chạy RL optimizer.

## Common Misconceptions

### “DPO không phải reinforcement-learning-related nên không cần hiểu preference/reward”

DPO vẫn bắt nguồn từ KL-regularized preference optimization; hiểu reward/preference framing giúp hiểu objective.

### “DPO luôn tốt hơn PPO”

Không. Choice phụ thuộc data, online feedback needs, stability và engineering constraints.

### “DPO đảm bảo model aligned”

Nó optimize observed preferences. Alignment rộng hơn dataset và objective.

## Knowledge Connection

DPO nối [RLHF](./08_rlhf.md), [SFT](./07_supervised_fine_tuning.md), [Probability](../01_mathematical_foundations/02_probability_for_ai.md) và [Distribution Shift](../04_machine_learning/14_bias_variance_and_generalization.md).

Xem tiếp: [In-Context Learning](./10_in_context_learning.md).