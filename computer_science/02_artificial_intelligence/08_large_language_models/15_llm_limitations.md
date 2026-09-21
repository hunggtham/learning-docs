# Limitations của Large Language Models

LLM rất mạnh vì học broad statistical regularities từ lượng data và compute lớn, nhưng architecture/objective của chúng tạo ra limitations mang tính cấu trúc. Hiểu limitations giúp chọn đúng architecture system thay vì cố “prompt harder” mọi vấn đề.

## Knowledge không có provenance native

Weights không lưu source citation theo dạng database. Model có thể generate fact nhưng không tự biết exact document nào support fact đó.

Nếu provenance là requirement, cần retrieval/source tracking.

## Knowledge có cutoff và staleness

Pretraining xảy ra tại một thời điểm. Facts sau cutoff hoặc state dynamic không nằm trong weights trừ khi continued training/update.

Current data nên đến từ tools/APIs/RAG.

## Hallucination

Autoregressive objective yêu cầu tiếp tục sequence, không guarantee truth. Model có thể tạo confident falsehood.

Xem: [Hallucination and Grounding](./13_hallucination_and_grounding.md).

## Context window hữu hạn

Model chỉ condition trên tokens trong current context window. Long conversations cần truncation, summarization hoặc memory retrieval.

Ngay cả khi token technically fits, **effective use** của information ở đầu/giữa context có thể không đồng đều.

## Reasoning không guaranteed

LLM có thể solve many reasoning tasks nhưng vẫn fail logically simple variants, especially adversarial or distribution-shifted prompts.

External verification nên dùng khi exactness important.

## Exact computation yếu hơn algorithmic tools

Large-number arithmetic, exhaustive search, database aggregation và formal proof thường phù hợp với specialized tools hơn token generation.

System tốt dispatch operation tới right computational substrate.

## Calibration hạn chế

Language confidence không phải probability of correctness. Phrases như “chắc chắn” có thể chỉ là learned style.

Risk-sensitive decisions cần calibrated scores hoặc external checks.

## Prompt sensitivity

Small wording differences có thể alter output. Post-training reduces but does not eliminate sensitivity.

Production prompts cần regression tests.

## Susceptibility to prompt injection

Model naturally follows patterns/instructions in context. Khi untrusted documents nằm cùng context với privileged instructions, attacker có thể attempt steer model.

Security requires privilege boundaries outside model.

## Non-determinism

Sampling làm outputs vary. Even deterministic decoding can change across model/provider versions, kernels or system updates.

If application requires strict repeatability, isolate deterministic components and record model/config/version.

## Bias từ data

Training corpus reflects social, linguistic và geographic imbalance. Model can underperform on low-resource languages/domains or reproduce stereotypes.

Evaluation must include target population, not only average benchmark.

## Long-tail failures

Model may perform 99% on common cases but fail rare edge cases unpredictably. For large-scale deployment, 1% can be many incidents.

Guardrails/fallback human review should target high-cost tail failures.

## Distribution shift

User behavior changes, new jargon appears, malicious strategies evolve. Static offline eval decays over time.

Monitoring and continual evaluation are necessary.

## Tool errors compound

Agentic LLM can call tools, but wrong tool argument may change external state. Model language capability does not guarantee transaction safety.

Use permissions, idempotency, validation, confirmation and audit logs.

## Memory is not human-like

Conversation memory usually comes from explicit context, retrieval or application database. LLM does not automatically maintain persistent episodic memory across sessions unless system provides it.

## Interpretability is incomplete

Attention weights or generated rationales do not provide full explanation of internal computation. Mechanistic interpretability can reveal circuits/patterns but does not yet make large model decisions fully transparent.

## Training-data uncertainty

For many models, exact corpus composition may be partially unknown. This complicates copyright, contamination and provenance analysis.

## Language understanding vs world interaction

Text-only model learns world patterns through text. Physical grounding, sensing and real-time action require multimodal/robotic/tool interfaces.

Language competence should not be confused with direct embodied experience.

## Optimization target mismatch

Pretraining optimizes token prediction; post-training optimizes preference/policy signals. User's true objective may differ.

This is Goodhart-like problem: proxy metric can be optimized while real goal suffers.

## Model vs System limitation

Nhiều “LLM limitations” có thể mitigated ở system level:

```text
stale knowledge → RAG/API
arithmetic      → calculator
factuality      → grounding/verifier
long workflow   → agent state + tools
format          → constrained decoding/schema
security        → permissions/sandbox
```

Nhưng mitigation adds complexity and new failure modes.

## When LLM is the wrong tool

Nếu problem có exact deterministic rules, low ambiguity và high verification requirement, normal software may be better.

Examples:

```text
interest calculation
permission check
schema validation
unique ID generation
cryptographic verification
```

LLM có thể explain/interface quanh rule engine nhưng không nên replace deterministic core.

## Mental Model

> LLM là **probabilistic language-and-representation engine**, không phải database, calculator, theorem prover, policy engine hay operating system. Production AI mạnh bằng cách kết hợp LLM với đúng components khác.

## Common Misconceptions

### “Model thế hệ sau sẽ làm mọi limitation biến mất”

Some limitations improve, but truth guarantees, provenance, authorization và deterministic execution remain system concerns.

### “Nếu prompt đủ tốt thì không cần architecture khác”

Prompt không thay external knowledge, tools hoặc validation.

### “LLM failure nghĩa AI không hữu ích”

Không. Giá trị đến từ matching capability với task và engineering around failure modes.

## Knowledge Connection

Limitations dẫn trực tiếp tới các layer tiếp theo: [Retrieval & RAG](../09_retrieval_and_rag/00_information_retrieval_foundations.md), Agents, Evaluation, Safety và AI Engineering.