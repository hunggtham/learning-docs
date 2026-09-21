# NLP Evaluation: từ exact labels tới open-ended language quality

NLP Evaluation (자연어 처리 평가) khó vì language cho phép nhiều outputs khác nhau cùng đúng. Classification có label rõ; translation/summarization/generation có vô số acceptable phrasings. Vì vậy evaluation cần chọn metric phù hợp task, tách automatic score khỏi human utility và luôn inspect failure categories.

## Classification / NER

Classification dùng accuracy, precision, recall, F1, calibration như ML chung.

NER nên entity/span-level F1 thay token accuracy vì class `O` dominate.

Exact entity match strict:

```text
Gold: [Seoul National University]
Pred: [National University]
```

count wrong dù overlap. Có thể thêm partial-match analysis nhưng report convention rõ.

## Macro vs Micro F1

Micro aggregate all examples/counts, dominated frequent classes.

Macro average F1 each class equally, exposes rare-class weakness.

Weighted macro uses support weights.

NLP label distributions often imbalanced, nên report more than one view.

## BLEU

BLEU measures modified n-gram precision + brevity penalty relative references.

Useful historical MT corpus metric, cheap/reproducible.

Limitations:

- valid paraphrases penalized;
- semantics/factuality weak;
- tokenization/reference count affect score;
- sentence-level noisy.

BLEU should compare same setup, not become universal language-quality score.

## ROUGE

ROUGE family emphasizes overlap/recall, common summarization.

ROUGE-L uses longest common subsequence. It rewards content overlap but cannot reliably detect factual inconsistency.

Extractive systems often score well because wording overlaps source.

## METEOR / chrF

METEOR includes stemming/synonym/alignment heuristics.

chrF uses character n-gram F-score and works well morphologically rich languages because less dependent word tokenization.

No metric removes need for task-specific error analysis.

## BERTScore

BERTScore matches candidate/reference tokens using contextual embedding similarity.

It captures paraphrases better than surface overlap.

But depends pretrained encoder and can reward semantically similar yet factually wrong outputs.

## Learned Metrics

COMET-style MT metrics learn from human judgments/source/reference representations and often correlate better with human quality.

Risks:

- domain/model bias;
- metric gaming;
- version drift;
- hidden training overlap.

Metric is another model requiring validation.

## Perplexity

Language-model intrinsic metric:

\[
PPL=\exp(crossentropy)
\]

Useful compare same tokenization/test corpus. It measures next-token predictive fit, not downstream instruction/helpfulness directly.

## Exact Match

QA/structured extraction often use exact string match.

Good when canonical answer strict, bad when formatting/paraphrase acceptable.

Normalization can lowercase/remove punctuation/articles but policy must match task and languages.

## Semantic QA Metrics

Token F1 for extractive QA compares overlap. Generative QA may use learned judge/entailment plus factual source checks.

A semantically similar answer can still contain one dangerous wrong number; aggregate embedding similarity may miss it.

## Faithfulness vs Quality

Summaries can be fluent/relevant but unfaithful.

Separate axes:

```text
coverage/relevance
fluency/coherence
faithfulness/grounding
factual correctness
style/format
```

One overall score hides trade-offs.

## Human Evaluation

Human judges can assess nuanced meaning, but evaluation has variance/bias.

Need:

- clear rubric;
- blind/randomized comparison;
- multiple raters for subjective task;
- inter-rater agreement;
- representative samples;
- adjudication for edge cases.

Pairwise preference often easier/more reliable than absolute 1–5 score.

## LLM-as-a-Judge Preview

LLM can evaluate outputs cheaply at scale, especially pairwise/rubric tasks.

But judge has biases:

- position bias;
- verbosity/style preference;
- self/model-family preference;
- prompt sensitivity;
- factual errors;
- vulnerability to answer text injection.

Use calibrated judge against human labels and structured evidence where possible.

## Data Contamination

If benchmark appears in pretraining/fine-tuning, score may reflect memorization.

Contamination hard prove for closed training data. New/private/time-split evaluation reduces risk.

LLM era makes benchmark lifecycle important.

## Challenge Sets

Average IID test may miss linguistic phenomena. Create targeted sets:

```text
negation
coreference
rare entities
numbers/dates
long context
multilingual code-switching
adversarial spelling
ambiguity
```

Each tests specific capability/failure mode.

## Robustness

Perturb input without changing meaning:

```text
punctuation change
synonym paraphrase
typo
format reorder
irrelevant sentence insertion
```

Prediction should remain stable if task invariant.

But perturbation must genuinely preserve semantics.

## Multilingual Evaluation

Do not translate English benchmark and assume equivalence. Translation may change difficulty, culture, tokenization and ambiguity.

Use native-language datasets/raters and report per-language metrics.

For Korean/Vietnamese, spacing/morphology/tokenization can affect exact/overlap metrics; character or semantic metrics may complement.

## Statistical Uncertainty

Report confidence intervals via bootstrap over examples/documents when possible.

If samples grouped by user/document, resample at independent unit.

Tiny score difference without uncertainty should not drive deployment decision.

## Online Evaluation

Offline NLP metric does not capture user interaction. A/B testing can measure:

- task completion;
- search success;
- correction/retry rate;
- retention;
- latency abandonment.

But online metric can incentivize bad behavior (clickbait, verbosity). Guardrails needed.

## Error Taxonomy

For generated output, manually categorize:

```text
wrong entity
wrong number/date
omission
unsupported addition
contradiction
instruction violation
format error
language/style issue
retrieval grounding failure
```

Error counts guide engineering much more actionable than one BLEU/ROUGE score.

## Reproducible Evaluation

Record:

```text
model/tokenizer version
prompt/template
decoding config
dataset commit/version
metric version
normalization
random seed
retrieval index/version if used
```

Generation settings can materially change score.

## Mental Model

> NLP evaluation is measurement design. First define what “good language behavior” means for the task; only then choose multiple measurements that approximate it.

## Common Misconceptions

### “Automatic metric cao = output tốt cho user”

Metric captures subset of desired properties.

### “Semantic embedding metric solves paraphrase problem completely”

It may miss factual/number/logical errors.

### “Human evaluation is ground truth without noise”

Humans disagree and have biases; rubric/design matter.

### “Benchmark score is model capability”

It is performance on a sampled benchmark under specific prompt/eval protocol.

## Knowledge Connection

NLP evaluation extends [Model Evaluation](../04_machine_learning/15_model_evaluation.md) and prepares dedicated LLM/RAG evaluation layers where open-ended generation, judges and grounding become central.