# Robustness và Distribution Shift

**Robustness (강건성 / tính bền vững)** hỏi system còn hoạt động tốt khi input, environment hoặc assumptions thay đổi trong phạm vi nào. Một model đạt benchmark cao trên clean data nhưng sụp khi có typo, sensor noise, unseen language hoặc distribution shift chưa phải robust system.

## Clean performance không đủ

Training/test thường giả định examples từ distribution tương tự. Production world tạo perturbations:

- device/sensor change;
- typo/spelling;
- background noise;
- lighting/weather;
- new user behavior;
- malicious inputs;
- missing fields;
- downstream API changes.

Robustness evaluation cố đo performance dưới những variations này.

## Distribution Shift

Nếu production distribution khác training:

\[
P_{prod}(X,Y) \neq P_{train}(X,Y)
\]

model generalization assumptions bị thử thách.

Shift types include covariate, label/prior và concept shift. Taxonomy useful nhưng diagnosis thực tế cần look at data + outcomes.

## Corruption Robustness

Computer Vision có thể test blur, noise, compression, brightness. NLP test typo, paraphrase, code-switching. Audio test background noise, microphone variation.

Goal không phải score trên mọi corruption imaginable mà map degradation curve theo severity.

## Perturbation Invariance

Nếu small meaning-preserving perturbation đổi output lớn, model unstable.

Examples:

```text
paraphrase same question
format whitespace change
image slight crop
reordering irrelevant metadata
```

Metamorphic tests define relationships expected giữa original và transformed inputs.

## Adversarial Examples

Adversarial input được optimize để gây error. Small perturbation có thể exploit local decision boundary.

Threat model phải specify attacker capability. Robustness against random noise khác robustness against adaptive attacker.

## Spurious Correlations

Model có thể dựa shortcut feature correlated trong training nhưng không causal/reliable.

Ví dụ image classifier học background thay vì object.

Stress test change background/context để reveal shortcut.

## OOD Generalization

OOD test should be intentionally separated by domain/time/source. Random split thường underestimate challenge.

Examples:

- train hospitals A/B, test hospital C;
- train past months, test future;
- train English, test code-switch;
- train known product categories, test new category.

## Robustness vs Invariance

Không phải mọi changes nên ignored. Nếu feature change thực sự alters target, forcing invariance harmful.

Domain knowledge quyết định which transformations preserve label.

## Data Augmentation

Augmentation injects expected variations during training:

```text
image crop/flip/color
text noise/paraphrase
audio noise/time shift
```

Augmentation defines inductive bias about invariance. Wrong augmentation can distort semantics.

## Regularization và Robustness

Regularization may improve average generalization but does not guarantee adversarial or OOD robustness.

Need direct stress testing.

## Robustness Curves

Instead of single score, measure metric vs perturbation severity:

```text
noise level 0 → accuracy 95%
noise level 1 → 93%
noise level 2 → 88%
noise level 3 → 60%
```

Curve shows degradation onset.

## LLM Robustness

Test:

- prompt paraphrases;
- irrelevant context;
- conflicting instructions;
- long context;
- multilingual inputs;
- format variation;
- retrieval noise;
- misleading premises.

LLM behavior can be highly sensitive to prompt wording/order.

## Context Robustness

Longer context can introduce distractors. A robust QA system should focus relevant evidence and ignore irrelevant chunks.

Need test retrieval with mix relevant/irrelevant/contradictory sources.

## Agent Robustness

Agent operates in changing environment:

- tool timeout;
- stale state;
- partial failure;
- unexpected schema;
- human interruption;
- duplicate retry.

Robust design requires recovery, replanning, idempotency and bounded loops.

## Robustness vs Reliability

Robustness concerns behavior under variation/perturbation. Reliability broader: availability, recovery, operational consistency and verified outcomes.

## Distributionally Robust Optimization

Some methods optimize worst-case or neighborhood distributions rather than empirical average. Conceptually:

\[
\min_\theta \max_{Q\in\mathcal U(P)} E_Q[L_\theta]
\]

Useful intuition but uncertainty set choice crucial.

## Domain Generalization

Train across multiple domains to learn features stable across environments. Success depends diversity and structure; no guarantee for arbitrary unseen domain.

## Causal Perspective

Causal features may transfer better across interventions than spurious correlations, but learning causal structure itself is hard. Causality is not automatic fix.

## Robustness Budget

Production system can layer defenses:

```text
input validation
OOD detection
model robustness
retrieval verification
fallback
human escalation
```

Do not demand model alone handle all uncertainty.

## Mental Model

```text
Robustness = how gracefully behavior degrades when reality differs from the clean assumptions used to build the model.
```

## Common Misconceptions

### “Data augmentation làm model robust”

Chỉ với variation augmentation actually represents; unknown/adaptive shifts remain.

### “OOD detector biết mọi unknown”

OOD is open-world problem; detectors have blind spots.

### “Robustness score là một con số universal”

Robustness depends threat/shift model and severity.

## Knowledge Connection

Xem [Drift](../16_mlops_and_llmops/07_drift_and_retraining.md), [Uncertainty](./02_uncertainty_and_calibration.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md) và [Safety/Security](../19_ai_safety_security_alignment/README.md).