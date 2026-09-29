# Explainability và Interpretability

> **Mạch đọc:** Đặt **Explainability và Interpretability** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao cần?** sang **toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


AI mô hình (model / 모델) có thể đạt hiệu năng (performance / 성능) cao nhưng vẫn khó hiểu vì sao nó đưa ra prediction. **Explainability (설명 가능성)** và **interpretability (해석 가능성)** nghiên cứu cách con người hiểu mô hình (model / 모델) hành vi (behavior / 동작), nội bộ (internal / 내부) mechanisms hoặc reason behind outputs.

Hai thuật ngữ thường dùng gần nhau nhưng có thể phân biệt thực dụng:

```text
Interpretability → model/mechanism intrinsically understandable đến mức nào
Explainability   → technique tạo explanation cho một decision/model
```

## Vì sao cần?

Use cases:

- gỡ lỗi (debug / 디버그) mô hình (model / 모델);
- detect spurious features;
- satisfy lĩnh vực (domain / 도메인)/người dùng (user / 사용자) requirements;
- hỗ trợ (support / 지원) human rà soát (review / 검토);
- investigate fairness;
- validate an toàn (safety / 안전) các giả định (assumptions / 가정들);
- scientific understanding.

Nhưng explanation không tự động chứng minh mô hình (model / 모델) correct.

## Toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation

**toàn cục (global / 전역)**: mô hình (model / 모델) generally hoạt động ra sao?

Examples: tính năng (feature / 기능) importance, cây (tree / 트리) cấu trúc (structure / 구조), learned concepts.

**cục bộ (local / 로컬)**: vì sao trường hợp (case / 사례) cụ thể có đầu ra (output / 출력) này?

Examples: contribution of features for one loan quyết định (decision / 결정).

## Intrinsically Interpretable các mô hình (models / 모델들)

Mô hình tuyến tính (linear model / 선형 모델):

\[
\hat y = w^Tx+b
\]

Coefficients dễ inspect nhưng interpretation phụ thuộc tính năng (feature / 기능) scaling, correlation và functional các giả định (assumptions / 가정들).

Cây quyết định (decision tree / 의사결정 트리) có đường dẫn (path / 경로) readable, nhưng deep cây (tree / 트리) vẫn phức tạp.

Interpretability không đồng nghĩa nhân quả (causal / 인과적) explanation.

## Tính năng (feature / 기능) Importance

Cây (tree / 트리) gain/split counts hoặc permutation importance estimate tính năng (feature / 기능) influence.

Permutation importance đo hiệu năng (performance / 성능) drop khi shuffle tính năng (feature / 기능). Nhưng correlated features có thể share/redundantly encode tín hiệu (signal / 신호), làm interpretation tricky.

## Partial Dependence

PDP estimate average prediction as one tính năng (feature / 기능) varies while marginalizing others.

Nếu tính năng (feature / 기능) combinations generated unrealistic do correlation, plot có thể misleading.

## SHAP Intuition

SHAP dựa Shapley values từ cooperative game lý thuyết (theory / 이론): distribute prediction difference among features based on marginal contributions across coalitions.

Strong theoretical properties nhưng computational approximations/feature-dependence các giả định (assumptions / 가정들) matter.

SHAP giá trị (value / 값) không chứng minh nhân quả (causal / 인과적) tác động (effect / 효과).

## LIME

LIME fit cục bộ (local / 로컬) surrogate mô hình (model / 모델) quanh one example. Explanation chất lượng (quality / 품질) depends perturbation phân phối (distribution / 분포) và cục bộ (local / 로컬) fidelity.

Stable explanation cần kiểm thử (test / 테스트) sensitivity.

## Counterfactual Explanation

Question:

> “đầu vào (input / 입력) cần thay đổi thế nào để prediction đổi?”

Ví dụ loan denial → income/debt thay đổi (change / 변경) needed.

Counterfactual phải respect feasible/actionable các ràng buộc (constraints / 제약조건들); không đề xuất immutable characteristics.

Counterfactual quan hệ (relation / 관계) vẫn không tự động nhân quả (causal / 인과적) nếu mô hình (model / 모델) itself spurious.

## Saliency Maps

Vision/NLP gradient-based saliency highlight đầu vào (input / 입력) regions/tokens affecting đầu ra (output / 출력).

Challenges:

- noisy;
- unstable;
- method-dependent;
- visually plausible nhưng not faithful.

Need sanity checks, not trust visualization alone.

## Attention as Explanation?

Attention weights cho biết mô hình (model / 모델) routing/weighting within kiến trúc (architecture / 아키텍처), nhưng attention weight không necessarily equal nhân quả (causal / 인과적) importance of đơn vị từ (token / 토큰) to final đầu ra (output / 출력).

“Attention is explanation” quá simplistic.

## Concept-Based Explanation

Instead of raw pixels/features, ask mô hình (model / 모델) sensitivity to human concepts: “striped”, “wheel”, “tumor ranh giới (boundary / 경계)”.

Requires reliable concept biểu diễn (representation / 표현)/labels.

## Mechanistic Interpretability

For neural networks/LLMs, mechanistic interpretability cố identify circuits/features/nội bộ (internal / 내부) computations responsible hành vi (behavior / 동작).

Topics include:

- neuron/tính năng (feature / 기능) activation;
- probing;
- activation patching;
- nhân quả (causal / 인과적) interventions;
- sparse tính năng (feature / 기능) dictionaries.

Goal deeper than post-hoc explanation, nhưng quy mô (scale / 규모) and superposition make challenge lớn.

## Probing

Train simple probe on hidden biểu diễn (representation / 표현) to see thông tin (information / 정보) decodable.

Important distinction:

> thông tin (information / 정보) being decodable does not prove mô hình (model / 모델) uses it causally.

Nhân quả (causal / 인과적) intervention needed for stronger claim.

## Activation Patching

Run clean/corrupted inputs, replace nội bộ (internal / 내부) activation from clean run into corrupted run, observe đầu ra (output / 출력) khôi phục (recovery / 복구).

This tests nhân quả (causal / 인과적) role of nội bộ (internal / 내부) components more directly than correlation-only probe.

## Superposition

Mạng (network / 네트워크) may represent many features in overlapping directions rather than one neuron-one-concept. This makes neuron-level interpretation incomplete.

## LLM Explanations vs nội bộ (internal / 내부) lập luận (reasoning / 추론)

A generated natural-language rationale is đầu ra (output / 출력) văn bản (text / 텍스트), not guaranteed faithful transcript of nội bộ (internal / 내부) computation.

Do not equate “chain-of-thought sounding explanation” with verified nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘).

## Explanation Fidelity

An explanation should match actual mô hình (model / 모델) hành vi (behavior / 동작). Evaluate by perturbing allegedly important features or measuring surrogate fidelity.

Human plausibility alone can be deceptive.

## Stability

Similar inputs should often produce similar explanations if mô hình (model / 모델) hành vi (behavior / 동작) similar. Highly unstable explanations reduce trust.

## Explainability vs Privacy

Detailed explanation can reveal sensitive features or mô hình (model / 모델) thông tin (information / 정보). Need balance transparency with bảo mật (security / 보안)/privacy.

## Explainability vs Fairness

Explanation can reveal protected attribute influence or proxies, but absence in explanation does not prove fairness.

## Regulatory/Operational Use

Some domains require reason codes or contestability. Choose mô hình (model / 모델)/explanation kiến trúc (architecture / 아키텍처) that can meet these requirements rather than bolting explanation on later.

## Human Factors

Explanations can cause automation độ lệch (bias / 편향) if presented with false authority. giao diện (interface / 인터페이스) should communicate limitations and bất định (uncertainty / 불확실성).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Explanation is another model/measurement of behavior.
It must itself be validated for fidelity and usefulness.
```

## Dùng chung (common / 공통) Misconceptions

### “SHAP cho biết nguyên nhân”

SHAP explains mô hình (model / 모델) prediction contributions under các giả định (assumptions / 가정들), not real-world causality.

### “mô hình (model / 모델) đưa rationale nghĩa đó là lập luận (reasoning / 추론) thật”

Generated rationale may be post-hoc/unfaithful.

### “Interpretable mô hình (model / 모델) luôn less accurate”

Không universal; many tabular tasks simple các mô hình (models / 모델들) competitive and preferable.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Models](../04_machine_learning/05_linear_regression.md), [Neural Representations](../05_neural_networks/08_representation_learning.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Ethics/Governance](../19_ai_safety_security_alignment/README.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 evaluation foundations](./00_evaluation_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
