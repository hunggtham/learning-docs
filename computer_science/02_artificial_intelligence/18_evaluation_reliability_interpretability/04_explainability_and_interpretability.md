# Explainability và Interpretability

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Explainability và Interpretability**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao cần?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation** tiếp nhận điểm tựa từ **Vì sao cần?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Intrinsically Interpretable các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation

**toàn cục (global / 전역)**: mô hình (model / 모델) generally hoạt động ra sao?

Examples: tính năng (feature / 기능) importance, cây (tree / 트리) cấu trúc (structure / 구조), learned concepts.

**cục bộ (local / 로컬)**: vì sao trường hợp (case / 사례) cụ thể có đầu ra (output / 출력) này?

Examples: contribution of features for one loan quyết định (decision / 결정).

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Intrinsically Interpretable các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Toàn cục (global / 전역) vs cục bộ (local / 로컬) Explanation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính năng (feature / 기능) Importance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intrinsically Interpretable các mô hình (models / 모델들)

Mô hình tuyến tính (linear model / 선형 모델):

\[
\hat y = w^Tx+b
\]

Coefficients dễ inspect nhưng interpretation phụ thuộc tính năng (feature / 기능) scaling, correlation và functional các giả định (assumptions / 가정들).

Cây quyết định (decision tree / 의사결정 트리) có đường dẫn (path / 경로) readable, nhưng deep cây (tree / 트리) vẫn phức tạp.

Interpretability không đồng nghĩa nhân quả (causal / 인과적) explanation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **Tính năng (feature / 기능) Importance** tiếp nhận điểm tựa từ **Intrinsically Interpretable các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial Dependence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính năng (feature / 기능) Importance

Cây (tree / 트리) gain/split counts hoặc permutation importance estimate tính năng (feature / 기능) influence.

Permutation importance đo hiệu năng (performance / 성능) drop khi shuffle tính năng (feature / 기능). Nhưng correlated features có thể share/redundantly encode tín hiệu (signal / 신호), làm interpretation tricky.

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Partial Dependence** tiếp nhận điểm tựa từ **Tính năng (feature / 기능) Importance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SHAP Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial Dependence

PDP estimate average prediction as one tính năng (feature / 기능) varies while marginalizing others.

Nếu tính năng (feature / 기능) combinations generated unrealistic do correlation, plot có thể misleading.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **SHAP Intuition** tiếp nhận điểm tựa từ **Partial Dependence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LIME** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SHAP Intuition

SHAP dựa Shapley values từ cooperative game lý thuyết (theory / 이론): distribute prediction difference among features based on marginal contributions across coalitions.

Strong theoretical properties nhưng computational approximations/feature-dependence các giả định (assumptions / 가정들) matter.

SHAP giá trị (value / 값) không chứng minh nhân quả (causal / 인과적) tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **LIME** tiếp nhận điểm tựa từ **SHAP Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Counterfactual Explanation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LIME

LIME fit cục bộ (local / 로컬) surrogate mô hình (model / 모델) quanh one example. Explanation chất lượng (quality / 품질) depends perturbation phân phối (distribution / 분포) và cục bộ (local / 로컬) fidelity.

Stable explanation cần kiểm thử (test / 테스트) sensitivity.

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Counterfactual Explanation** tiếp nhận điểm tựa từ **LIME** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Saliency Maps** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Counterfactual Explanation

Question:

> “đầu vào (input / 입력) cần thay đổi thế nào để prediction đổi?”

Ví dụ loan denial → income/debt thay đổi (change / 변경) needed.

Counterfactual phải respect feasible/actionable các ràng buộc (constraints / 제약조건들); không đề xuất immutable characteristics.

Counterfactual quan hệ (relation / 관계) vẫn không tự động nhân quả (causal / 인과적) nếu mô hình (model / 모델) itself spurious.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Saliency Maps** tiếp nhận điểm tựa từ **Counterfactual Explanation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention as Explanation?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Saliency Maps

Vision/NLP gradient-based saliency highlight đầu vào (input / 입력) regions/tokens affecting đầu ra (output / 출력).

Challenges:

- noisy;
- unstable;
- method-dependent;
- visually plausible nhưng not faithful.

Need sanity checks, not trust visualization alone.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **Attention as Explanation?** tiếp nhận điểm tựa từ **Saliency Maps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Concept-Based Explanation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention as Explanation?

Attention weights cho biết mô hình (model / 모델) routing/weighting within kiến trúc (architecture / 아키텍처), nhưng attention weight không necessarily equal nhân quả (causal / 인과적) importance of đơn vị từ (token / 토큰) to final đầu ra (output / 출력).

“Attention is explanation” quá simplistic.

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Concept-Based Explanation** tiếp nhận điểm tựa từ **Attention as Explanation?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mechanistic Interpretability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Concept-Based Explanation

Instead of raw pixels/features, ask mô hình (model / 모델) sensitivity to human concepts: “striped”, “wheel”, “tumor ranh giới (boundary / 경계)”.

Requires reliable concept biểu diễn (representation / 표현)/labels.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Mechanistic Interpretability** tiếp nhận điểm tựa từ **Concept-Based Explanation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Probing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mechanistic Interpretability

For neural networks/LLMs, mechanistic interpretability cố identify circuits/features/nội bộ (internal / 내부) computations responsible hành vi (behavior / 동작).

Topics include:

- neuron/tính năng (feature / 기능) activation;
- probing;
- activation patching;
- nhân quả (causal / 인과적) interventions;
- sparse tính năng (feature / 기능) dictionaries.

Goal deeper than post-hoc explanation, nhưng quy mô (scale / 규모) and superposition make challenge lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **Probing** tiếp nhận điểm tựa từ **Mechanistic Interpretability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Activation Patching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Probing

Train simple probe on hidden biểu diễn (representation / 표현) to see thông tin (information / 정보) decodable.

Important distinction:

> thông tin (information / 정보) being decodable does not prove mô hình (model / 모델) uses it causally.

Nhân quả (causal / 인과적) intervention needed for stronger claim.

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Activation Patching** tiếp nhận điểm tựa từ **Probing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Superposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Activation Patching

Run clean/corrupted inputs, replace nội bộ (internal / 내부) activation from clean run into corrupted run, observe đầu ra (output / 출력) khôi phục (recovery / 복구).

This tests nhân quả (causal / 인과적) role of nội bộ (internal / 내부) components more directly than correlation-only probe.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Superposition** tiếp nhận điểm tựa từ **Activation Patching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM Explanations vs nội bộ (internal / 내부) lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Superposition

Mạng (network / 네트워크) may represent many features in overlapping directions rather than one neuron-one-concept. This makes neuron-level interpretation incomplete.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **LLM Explanations vs nội bộ (internal / 내부) lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Superposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explanation Fidelity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM Explanations vs nội bộ (internal / 내부) lập luận (reasoning / 추론)

A generated natural-language rationale is đầu ra (output / 출력) văn bản (text / 텍스트), not guaranteed faithful transcript of nội bộ (internal / 내부) computation.

Do not equate “chain-of-thought sounding explanation” with verified nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Explanation Fidelity** tiếp nhận điểm tựa từ **LLM Explanations vs nội bộ (internal / 내부) lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explanation Fidelity

An explanation should match actual mô hình (model / 모델) hành vi (behavior / 동작). Evaluate by perturbing allegedly important features or measuring surrogate fidelity.

Human plausibility alone can be deceptive.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Stability** tiếp nhận điểm tựa từ **Explanation Fidelity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explainability vs Privacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stability

Similar inputs should often produce similar explanations if mô hình (model / 모델) hành vi (behavior / 동작) similar. Highly unstable explanations reduce trust.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **Explainability vs Privacy** tiếp nhận điểm tựa từ **Stability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explainability vs Fairness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explainability vs Privacy

Detailed explanation can reveal sensitive features or mô hình (model / 모델) thông tin (information / 정보). Need balance transparency with bảo mật (security / 보안)/privacy.

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Explainability vs Fairness** tiếp nhận điểm tựa từ **Explainability vs Privacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Regulatory/Operational Use** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explainability vs Fairness

Explanation can reveal protected attribute influence or proxies, but absence in explanation does not prove fairness.

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Regulatory/Operational Use** tiếp nhận điểm tựa từ **Explainability vs Fairness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human Factors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regulatory/Operational Use

Some domains require reason codes or contestability. Choose mô hình (model / 모델)/explanation kiến trúc (architecture / 아키텍처) that can meet these requirements rather than bolting explanation on later.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, **Human Factors** tiếp nhận điểm tựa từ **Regulatory/Operational Use** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human Factors

Explanations can cause automation độ lệch (bias / 편향) if presented with false authority. giao diện (interface / 인터페이스) should communicate limitations and bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Trong **Explainability và Interpretability**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Human Factors** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Explanation is another model/measurement of behavior.
It must itself be validated for fidelity and usefulness.
```

> **Chuyển mạch:** Ở chặng này của **Explainability và Interpretability**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “SHAP cho biết nguyên nhân”

SHAP explains mô hình (model / 모델) prediction contributions under các giả định (assumptions / 가정들), not real-world causality.

### “mô hình (model / 모델) đưa rationale nghĩa đó là lập luận (reasoning / 추론) thật”

Generated rationale may be post-hoc/unfaithful.

### “Interpretable mô hình (model / 모델) luôn less accurate”

Không universal; many tabular tasks simple các mô hình (models / 모델들) competitive and preferable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Explainability và Interpretability**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Linear Models](../04_machine_learning/05_linear_regression.md), [Neural Representations](../05_neural_networks/08_representation_learning.md), [Evaluation Foundations](./00_evaluation_foundations.md), [Ethics/Governance](../19_ai_safety_security_alignment/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
