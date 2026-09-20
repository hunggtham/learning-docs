# Synthetic Data

**Synthetic data (합성 데이터 / dữ liệu tổng hợp)** là data được tạo bởi simulator, rules hoặc generative model thay vì thu trực tiếp từ phenomenon thật. Nó hữu ích để tăng coverage, bảo vệ privacy, tạo rare scenarios hoặc bootstrap labels, nhưng không phải “data miễn phí” vì synthetic data luôn kế thừa assumptions của generator.

## Các nguồn synthetic data

```text
rule-based generation
simulation / digital twin
generative models
LLM-generated text
rendered images
procedural environments
counterfactual transformations
```

Mỗi source có fidelity và failure modes khác.

## Simulation

Robotics/autonomous driving có thể generate unlimited trajectories/images trong simulator.

Ưu điểm:

- labels exact từ simulator state;
- rare/dangerous cases cheap;
- full control conditions.

Nhược điểm: **sim-to-real gap**. Renderer/physics/sensor model không perfect.

## Domain Randomization

Randomize textures, lighting, camera, physics parameters để force model learn invariant structure rather than overfit one simulator look.

Goal không phải make simulation photorealistic nhất, mà cover real domain sufficiently.

## Generative Synthetic Data

Diffusion/LLM can produce new examples. Use cases:

- augment rare classes;
- generate instruction-response pairs;
- create paraphrases;
- simulate edge cases;
- anonymized-like samples.

But generated data reflects generator training distribution.

## Self-Instruct / Synthetic Instructions

LLM can generate tasks then answers, scaling instruction-tuning data.

Pipeline:

```text
seed tasks
→ generate candidate instructions
→ filter/deduplicate
→ generate responses
→ quality judge/human sample audit
```

Risk: errors compound and model family may teach its own blind spots.

## Teacher–Student Distillation

Strong model labels/generates training data for smaller model. Student approximates teacher behavior, not necessarily ground truth.

Quality ceiling tied to teacher + filtering.

## Rare Event Generation

Fraud/failure cases rare. Synthetic generation can balance training, but if synthetic rare cases unrealistic model learns artifacts separating “synthetic” from “real” rather than true phenomenon.

Need realism evaluation and mixed real data.

## Privacy Motivation

Synthetic records may reduce direct exposure of real individuals, but privacy is not automatic.

Generator can memorize and reproduce training records. Privacy needs attacks/tests or formal mechanisms like Differential Privacy.

## Differential Privacy Connection

DP training limits influence of any one training record. Synthetic data generated from DP-trained model can inherit formal privacy guarantees under assumptions, unlike ordinary synthetic data.

## Statistical Fidelity

For tabular synthetic data, compare:

- marginals;
- correlations;
- conditional distributions;
- rare category frequency;
- temporal patterns;
- downstream model utility.

Matching simple histograms does not guarantee joint fidelity.

## Utility Evaluation

Train on synthetic, test on **real holdout**. This TSTR (Train Synthetic Test Real) style evaluation measures whether synthetic captures task-relevant structure.

Also compare model trained real vs real+synthetic.

## Diversity

Generator mode collapse/low diversity produces many near-duplicates. Count alone overstates effective sample size.

Deduplication and diversity metrics needed.

## Synthetic-to-Real Ratio

Too much synthetic data can shift model toward generator artifacts. Optimal ratio task-dependent; monitor real validation performance.

## Distribution Steering

Synthetic generator can intentionally rebalance subgroup/category coverage. But forcing uniform distribution may no longer match deployment prior. Separate training balancing from probability calibration.

## Counterfactual Data Augmentation

Modify one attribute while preserving label semantics:

```text
he ↔ she
background color change
style transfer
```

Useful to break shortcuts, but generated counterfactual must remain plausible and not unintentionally alter target.

## Adversarial Synthetic Data

Generate hard negatives or red-team prompts near model decision boundary. This can strengthen robustness, but generator may overfocus known failure modes.

## Synthetic Evaluation Sets

Generated benchmarks scale scenario creation, but using LLM to both generate and judge can create circularity. Keep human/real anchors.

## Data Contamination

As web fills with AI-generated content, future foundation-model training may ingest synthetic data unknowingly. Repeated model-generated distributions can narrow diversity or amplify errors.

Provenance becomes increasingly important.

## Model Collapse Intuition

If generations replace real data over repeated generations without fresh real signal, distribution tails may erode. Exact behavior depends setup, but principle: synthetic feedback loop can lose information.

## Watermark / Metadata

Synthetic media can carry provenance metadata/watermarks. Metadata can be stripped; watermark robust detection is probabilistic, not perfect.

## Simulation Labels vs Real Labels

Simulator gives exact internal state, but mapping to real sensor semantics may differ. Perfect simulated ground truth does not mean perfect real-world relevance.

## Example: Document OCR

Synthetic text rendered with many fonts/backgrounds gives exact transcription/bounding boxes. Useful pretraining. But real scans add fold, glare, handwriting, compression; real fine-tuning still needed.

## Example: Code Data

LLM-generated code can create exercises/solutions/tests. But compiler/test execution should verify, because syntactically plausible code may be wrong/insecure.

## Mental Model

> **Synthetic data là output của một model về world. Training trên synthetic nghĩa là học từ assumptions của world-model đó; giá trị đến từ controllability, không phải vì synthetic inherently truthful.**

## Common Misconceptions

### “Synthetic data solves privacy”

Not automatically; memorization/re-identification possible.

### “More synthetic samples always increase diversity”

Generator may output near-duplicates/mode bias.

### “If synthetic looks realistic to human, it is statistically correct”

Visual plausibility does not guarantee task-relevant joint distribution.

## Knowledge Connection

Synthetic data connects Generative AI, Simulation, Privacy, RL environments and Data Governance.

Xem tiếp: [Data Governance](./08_data_governance.md).