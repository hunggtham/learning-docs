# Explainability và Interpretability

AI model có thể đạt performance cao nhưng vẫn khó hiểu vì sao nó đưa ra prediction. **Explainability (설명 가능성)** và **interpretability (해석 가능성)** nghiên cứu cách con người hiểu model behavior, internal mechanisms hoặc reason behind outputs.

Hai thuật ngữ thường dùng gần nhau nhưng có thể phân biệt thực dụng:

```text
Interpretability → model/mechanism intrinsically understandable đến mức nào
Explainability   → technique tạo explanation cho một decision/model
```

## Vì sao cần?

Use cases:

- debug model;
- detect spurious features;
- satisfy domain/user requirements;
- support human review;
- investigate fairness;
- validate safety assumptions;
- scientific understanding.

Nhưng explanation không tự động chứng minh model correct.

## Global vs Local Explanation

**Global**: model generally hoạt động ra sao?

Examples: feature importance, tree structure, learned concepts.

**Local**: vì sao case cụ thể có output này?

Examples: contribution of features for one loan decision.

## Intrinsically Interpretable Models

Linear model:

\[
\hat y = w^Tx+b
\]

Coefficients dễ inspect nhưng interpretation phụ thuộc feature scaling, correlation và functional assumptions.

Decision tree có path readable, nhưng deep tree vẫn phức tạp.

Interpretability không đồng nghĩa causal explanation.

## Feature Importance

Tree gain/split counts hoặc permutation importance estimate feature influence.

Permutation importance đo performance drop khi shuffle feature. Nhưng correlated features có thể share/redundantly encode signal, làm interpretation tricky.

## Partial Dependence

PDP estimate average prediction as one feature varies while marginalizing others.

Nếu feature combinations generated unrealistic do correlation, plot có thể misleading.

## SHAP Intuition

SHAP dựa Shapley values từ cooperative game theory: distribute prediction difference among features based on marginal contributions across coalitions.

Strong theoretical properties nhưng computational approximations/feature-dependence assumptions matter.

SHAP value không chứng minh causal effect.

## LIME

LIME fit local surrogate model quanh one example. Explanation quality depends perturbation distribution và local fidelity.

Stable explanation cần test sensitivity.

## Counterfactual Explanation

Question:

> “Input cần thay đổi thế nào để prediction đổi?”

Ví dụ loan denial → income/debt change needed.

Counterfactual phải respect feasible/actionable constraints; không đề xuất immutable characteristics.

Counterfactual relation vẫn không tự động causal nếu model itself spurious.

## Saliency Maps

Vision/NLP gradient-based saliency highlight input regions/tokens affecting output.

Challenges:

- noisy;
- unstable;
- method-dependent;
- visually plausible nhưng not faithful.

Need sanity checks, not trust visualization alone.

## Attention as Explanation?

Attention weights cho biết model routing/weighting within architecture, nhưng attention weight không necessarily equal causal importance of token to final output.

“Attention is explanation” quá simplistic.

## Concept-Based Explanation

Instead of raw pixels/features, ask model sensitivity to human concepts: “striped”, “wheel”, “tumor boundary”.

Requires reliable concept representation/labels.

## Mechanistic Interpretability

For neural networks/LLMs, mechanistic interpretability cố identify circuits/features/internal computations responsible behavior.

Topics include:

- neuron/feature activation;
- probing;
- activation patching;
- causal interventions;
- sparse feature dictionaries.

Goal deeper than post-hoc explanation, nhưng scale and superposition make challenge lớn.

## Probing

Train simple probe on hidden representation to see information decodable.

Important distinction:

> Information being decodable does not prove model uses it causally.

Causal intervention needed for stronger claim.

## Activation Patching

Run clean/corrupted inputs, replace internal activation from clean run into corrupted run, observe output recovery.

This tests causal role of internal components more directly than correlation-only probe.

## Superposition

Network may represent many features in overlapping directions rather than one neuron-one-concept. This makes neuron-level interpretation incomplete.

## LLM Explanations vs Internal Reasoning

A generated natural-language rationale is output text, not guaranteed faithful transcript of internal computation.

Do not equate “chain-of-thought sounding explanation” with verified causal mechanism.

## Explanation Fidelity

An explanation should match actual model behavior. Evaluate by perturbing allegedly important features or measuring surrogate fidelity.

Human plausibility alone can be deceptive.

## Stability

Similar inputs should often produce similar explanations if model behavior similar. Highly unstable explanations reduce trust.

## Explainability vs Privacy

Detailed explanation can reveal sensitive features or model information. Need balance transparency with security/privacy.

## Explainability vs Fairness

Explanation can reveal protected attribute influence or proxies, but absence in explanation does not prove fairness.

## Regulatory/Operational Use

Some domains require reason codes or contestability. Choose model/explanation architecture that can meet these requirements rather than bolting explanation on later.

## Human Factors

Explanations can cause automation bias if presented with false authority. Interface should communicate limitations and uncertainty.

## Mental Model

```text
Explanation is another model/measurement of behavior.
It must itself be validated for fidelity and usefulness.
```

## Common Misconceptions

### “SHAP cho biết nguyên nhân”

SHAP explains model prediction contributions under assumptions, not real-world causality.

### “Model đưa rationale nghĩa đó là reasoning thật”

Generated rationale may be post-hoc/unfaithful.

### “Interpretable model luôn less accurate”

Không universal; many tabular tasks simple models competitive and preferable.

## Knowledge Connection

Xem [Linear Models](../04_machine_learning/05_linear_and_logistic_regression.md), [Neural Representations](../05_neural_networks/08_representation_learning.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Ethics/Governance](../20_ethics_governance_and_society/README.md).