# Evaluation của Large Language Models

LLM evaluation khó hơn traditional software testing vì output space rộng, nhiều answers có thể acceptable và behavior phụ thuộc prompt/context. Một evaluation tốt phải trả lời **model/system tốt cho task nào, trên population nào, với metric nào và dưới constraints nào**.

## Perplexity không đủ

Pretraining thường monitor cross-entropy/perplexity. Perplexity thấp hơn nghĩa model predict held-out tokens tốt hơn:

\[
PPL=\exp\left(-\frac{1}{N}\sum_i \log P(x_i\mid x_{<i})\right)
\]

Nhưng perplexity không trực tiếp đo instruction following, factuality, coding correctness hay safety.

Model A có perplexity tốt hơn nhưng application performance có thể kém hơn model B do post-training khác.

## Capability benchmarks

Benchmarks đo slices như mathematics, coding, knowledge, reading comprehension hoặc multilingual tasks. Chúng hữu ích để compare controlled capabilities nhưng dễ bị overinterpreted.

Một benchmark score chỉ valid cho dataset, prompt protocol, evaluator và model version cụ thể.

## Contamination

Nếu benchmark examples hoặc near-duplicates xuất hiện trong training data, score có thể overestimate generalization.

Contamination khó phát hiện hoàn toàn với proprietary training corpora. Vì vậy fresh/private eval sets có giá trị lớn.

## Exact match vs semantic quality

Structured tasks như classification có thể dùng exact match. Open-ended answer cần semantic grading.

LLM-as-judge có thể score relevance/correctness nhưng evaluator model cũng có biases, position preference và style bias.

Human evaluation vẫn quan trọng cho ambiguous/high-value tasks.

## Pairwise evaluation

Thay vì chấm absolute score, evaluator chọn response A hay B tốt hơn. Pairwise comparison thường dễ và consistent hơn rubric 1–10.

Nhưng ordering bias và tie handling cần control.

## Task-specific evals

Production eval nên reflect actual user workload. Ví dụ support assistant cần đo:

```text
correct resolution
policy adherence
citation support
escalation accuracy
latency
cost
```

Generic benchmark không thay thế task eval.

## Golden set

Một curated **golden set** gồm representative cases, edge cases và known failures. Nó nên versioned và chạy regression khi đổi model, prompt, RAG hoặc tool code.

Không nên tune liên tục trên same golden set rồi vẫn gọi nó unbiased test.

## Error taxonomy

Aggregate score che failure modes. Nên categorize errors:

- factual error;
- instruction miss;
- reasoning error;
- retrieval miss;
- citation mismatch;
- formatting error;
- unsafe behavior;
- tool misuse.

Taxonomy giúp biết layer nào cần fix.

## Evaluation stack

Một AI application nên có nhiều tầng:

```text
unit tests for deterministic code
retrieval tests
model response evals
end-to-end workflow evals
online monitoring
human review
```

Không có một benchmark duy nhất cover tất cả.

## Offline và online evaluation

Offline eval reproducible và safe. Online eval phản ánh real traffic nhưng chịu confounding và risk.

A/B testing đo product outcome nhưng cần sample size, guardrails và careful interpretation.

## LLM-as-judge

Judge model có thể scale evaluation cho open-ended text. Rubric phải explicit và ideally judge should receive reference/evidence when relevant.

Risks:

```text
self-preference
verbosity bias
position bias
shared model blind spots
prompt sensitivity
```

Calibration với human labels giúp biết judge đáng tin ở đâu.

## Factuality eval

Nếu answer phải grounded, evaluator nên check claims against source. Có thể decompose response thành atomic claims rồi verify entailment.

Một overall “looks correct” score thường quá coarse.

## Tool-use eval

Agent/tool model cần evaluate:

```text
tool selection
argument correctness
schema validity
recovery from tool error
unnecessary tool calls
final answer based on result
```

Task success quan trọng hơn tool-call syntax đơn thuần.

## Safety evaluation

Safety eval cần benign + adversarial prompts, multilingual variants và transformations. Chỉ test obvious harmful phrase không đủ.

Đồng thời phải đo over-refusal trên benign tasks.

## Robustness

Paraphrase cùng request nhiều cách. Nếu score biến động lớn, model behavior brittle.

Perturbation tests gồm typo, long context, irrelevant distraction và conflicting evidence.

## Statistical uncertainty

Benchmark score là estimate từ finite samples. Difference nhỏ có thể không statistically meaningful.

Confidence interval hoặc bootstrap hữu ích khi compare models.

## Cost-quality frontier

Production model selection thường là multi-objective:

\[
quality, latency, cost, reliability
\]

Model tốt nhất về benchmark có thể không tốt nhất về business system.

Plot quality vs cost/latency giúp chọn Pareto frontier.

## Eval-driven development

Workflow tốt:

```text
collect failures
→ convert to regression evals
→ change prompt/model/system
→ rerun eval suite
→ deploy guarded
→ monitor new failures
```

Evaluation không phải final stage; nó là feedback loop của AI engineering.

## Mental Model

> Một model không có “chất lượng” tuyệt đối. Chất lượng luôn là **performance distribution trên một task/population under a protocol**.

## Common Misconceptions

### “Benchmark cao hơn = model tốt hơn mọi mặt”

Không. Benchmarks đo slices.

### “LLM judge thay thế human hoàn toàn”

Không. Judge cần calibration và audit.

### “Một test set dùng mãi vẫn unbiased”

Nếu team tune theo nó, nó trở thành development signal.

## Knowledge Connection

LLM evaluation nối [Machine Learning Evaluation](../04_machine_learning/15_model_evaluation.md), RAG evaluation, Agent evaluation và LLMOps monitoring.

Xem tiếp: [LLM Limitations](./15_llm_limitations.md).