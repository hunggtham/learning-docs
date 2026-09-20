# Instruction Tuning

Base LLM được pretrain để **tiếp tục text**, nhưng user muốn một assistant có thể hiểu request và tạo response phù hợp. **Instruction tuning (지시 튜닝 / tinh chỉnh theo chỉ dẫn)** là quá trình điều chỉnh model để map từ instruction + context sang desired response format và behavior.

Điểm quan trọng là instruction tuning không “dạy toàn bộ kiến thức mới”. Phần lớn broad knowledge và language capability đã được hình thành trong pretraining. Post-training thay đổi cách model **sử dụng** capability đó theo interaction pattern mong muốn.

## Từ continuation tới instruction following

Pretraining objective:

\[
P(x_t\mid x_{<t})
\]

không phân biệt semantic role như system, user hay assistant trừ khi những pattern đó xuất hiện trong data.

Instruction dataset đưa structure rõ hơn:

```text
Instruction: Explain recursion simply.
Response: ...
```

hoặc chat format:

```text
system → policy/context
user   → request
assistant → desired answer
```

Model học rằng một số token sequence đóng vai trò instruction và output nên theo constraints đó.

## Instruction data

Instruction data có thể đến từ human-written examples, synthetic generation, transformed datasets hoặc mixtures của nhiều tasks. Quality quan trọng hơn việc chỉ tăng số lượng.

Một example tốt không chỉ có “đáp án đúng”; nó thể hiện format, depth, tone, refusal boundary, tool-use schema hoặc reasoning style cần thiết.

Nếu dataset inconsistent, model học distribution inconsistent.

## Task diversity và generalization

Instruction tuning hữu ích vì model có thể generalize từ many task templates sang instruction mới. Nếu training chỉ có narrow templates, model có thể overfit phrasing.

Diversity giúp model học meta-pattern:

> text trước mô tả intent/constraints; text sau phải satisfy intent/constraints.

Đây là một dạng learned interface giữa human language và model capability.

## System/User/Assistant roles

Modern chat systems thường encode role tokens hoặc special formatting. Role hierarchy không phải property tự nhiên của language model; nó là behavior được tạo bởi training, serving protocol và runtime policy.

Vì vậy prompt injection là system-level problem: model đang đọc nhiều text streams nhưng application muốn một số streams có authority cao hơn streams khác.

## Instruction tuning và knowledge

Fine-tuning có thể inject some domain knowledge, nhưng đây không phải always best tool. Nếu knowledge thay đổi thường xuyên hoặc cần provenance, retrieval thường phù hợp hơn.

Use instruction tuning khi muốn thay đổi **behavior mapping**, ví dụ:

```text
input schema → structured JSON
support ticket → classification + explanation
question → answer theo policy/domain style
```

Use RAG khi muốn cung cấp facts/document context fresh và traceable.

## Catastrophic forgetting

Nếu fine-tune quá mạnh trên narrow data, model có thể mất capability hoặc style rộng trước đó. Mitigation gồm lower learning rate, data mixture, regularization và parameter-efficient tuning.

## Multi-task instruction tuning

Một model có thể train trên translation, summarization, QA, extraction, coding và dialogue cùng lúc. Shared representation cho phép transfer giữa tasks.

Nhưng task mixture cần weighting. Dataset lớn nhưng easy có thể dominate gradient và làm hard/rare task bị underrepresented.

## Synthetic instruction data

Stronger model có thể generate instruction-response pairs cho weaker/open model. Điều này scale nhanh nhưng có nguy cơ propagate errors, stylistic artifacts và blind spots của teacher.

Synthetic data cần filtering/evaluation thay vì assume teacher output là ground truth.

## Instruction tuning vs SFT

Hai thuật ngữ overlap nhiều. **Supervised Fine-Tuning (SFT)** mô tả learning procedure dùng labeled input-output pairs. **Instruction tuning** mô tả loại behavior/data: examples có instruction semantics.

Instruction tuning thường được thực hiện bằng SFT, nhưng SFT cũng có thể dùng cho task không phải natural-language instruction.

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).

## Instruction following không bằng alignment hoàn chỉnh

Model có thể follow instruction rất tốt nhưng vẫn:

- hallucinate;
- follow malicious instruction;
- violate safety policy;
- optimize wording thay vì intent;
- fail under conflicting instructions.

Preference training và runtime safety layers thường được thêm sau.

## Over-refusal và under-refusal

Post-training safety có trade-off. Nếu refusal examples quá rộng, model có thể từ chối benign requests. Nếu quá hẹp, harmful transformations có thể bypass.

Evaluation phải đo cả helpfulness lẫn appropriate refusal, không chỉ một phía.

## Formatting as behavior

Instruction tuning có thể dạy structured output như JSON/XML/tool call. Tuy nhiên generation vẫn probabilistic. Nếu output phải syntactically valid tuyệt đối, constrained decoding hoặc schema validation nên bổ sung.

Model behavior và deterministic validation là hai layers khác nhau.

## Mental Model

> Pretraining tạo **general capability**; instruction tuning tạo **interaction protocol** để capability đó phục vụ request theo cách hữu ích hơn.

## Common Misconceptions

### “Fine-tune là cách tốt nhất để cập nhật facts mới”

Không nhất thiết. Retrieval có freshness/provenance tốt hơn cho knowledge dynamic.

### “Instruction tuning làm model hiểu mọi instruction”

Nó cải thiện generalization nhưng vẫn phụ thuộc distribution, context complexity và conflicting constraints.

### “Role hierarchy là hard-coded truth trong Transformer”

Role semantics đến từ training format và runtime system, không phải attention tự nhiên biết system message có authority cao hơn.

## Knowledge Connection

Instruction tuning nối pretraining với assistant behavior. Sau SFT, preference optimization như RLHF/DPO tiếp tục điều chỉnh output theo human preferences và policy.

Xem tiếp: [Supervised Fine-Tuning](./07_supervised_fine_tuning.md).