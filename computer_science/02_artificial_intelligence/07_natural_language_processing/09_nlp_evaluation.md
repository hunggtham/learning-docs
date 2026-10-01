# NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Classification / NER** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Macro vs Micro F1** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

NLP Evaluation (자연어 처리 평가) khó vì ngôn ngữ (language / 언어) cho phép nhiều outputs khác nhau cùng đúng. Classification có label rõ; translation/summarization/generation có vô số acceptable phrasings. Vì vậy evaluation cần chọn chỉ số (metric / 지표) phù hợp tác vụ (task / 작업), tách automatic score khỏi human utility và luôn inspect thất bại (failure / 실패) categories.

## Classification / NER

Classification dùng accuracy, precision, recall, F1, calibration như ML chung.

NER nên thực thể (entity / 엔터티)/span-level F1 thay đơn vị từ (token / 토큰) accuracy vì lớp (class / 클래스) `O` dominate.

Chính xác (exact / 정확한) thực thể (entity / 엔터티) match strict:

```text
Gold: [Seoul National University]
Pred: [National University]
```

count wrong dù overlap. Có thể thêm partial-match phân tích (analysis / 분석) nhưng report convention rõ.

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Macro vs Micro F1** tiếp nhận điểm tựa từ **Classification / NER** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BLEU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Macro vs Micro F1

Micro aggregate all examples/counts, dominated frequent classes.

Macro average F1 each lớp (class / 클래스) equally, exposes rare-class weakness.

Weighted macro uses hỗ trợ (support / 지원) weights.

NLP label distributions often imbalanced, nên report more than one view.

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **BLEU** tiếp nhận điểm tựa từ **Macro vs Micro F1** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ROUGE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BLEU

BLEU measures modified n-gram precision + brevity penalty relative references.

Useful historical MT corpus chỉ số (metric / 지표), cheap/reproducible.

Limitations:

- valid paraphrases penalized;
- ngữ nghĩa (semantics / 의미론)/factuality weak;
- tokenization/tham chiếu (reference / 참조) count affect score;
- sentence-level noisy.

BLEU should compare same setup, not become universal language-quality score.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **ROUGE** tiếp nhận điểm tựa từ **BLEU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **METEOR / chrF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ROUGE

ROUGE family emphasizes overlap/recall, dùng chung (common / 공통) summarization.

ROUGE-L uses longest dùng chung (common / 공통) subsequence. It rewards content overlap but cannot reliably detect factual inconsistency.

Extractive các hệ thống (systems / 시스템들) often score well because wording overlaps nguồn (source / 소스).

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **METEOR / chrF** tiếp nhận điểm tựa từ **ROUGE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BERTScore** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## METEOR / chrF

METEOR includes stemming/synonym/alignment heuristics.

chrF uses character n-gram F-score and works well morphologically rich languages because less dependent word tokenization.

No chỉ số (metric / 지표) removes need for task-specific lỗi (error / 오류) phân tích (analysis / 분석).

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **BERTScore** tiếp nhận điểm tựa từ **METEOR / chrF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Learned Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BERTScore

BERTScore matches candidate/tham chiếu (reference / 참조) tokens using contextual embedding similarity.

It captures paraphrases better than surface overlap.

But depends pretrained encoder and can reward semantically similar yet factually wrong outputs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Learned Metrics** tiếp nhận điểm tựa từ **BERTScore** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Perplexity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Learned Metrics

COMET-style MT metrics learn from human judgments/nguồn (source / 소스)/tham chiếu (reference / 참조) representations and often correlate better with human chất lượng (quality / 품질).

Risks:

- lĩnh vực (domain / 도메인)/mô hình (model / 모델) độ lệch (bias / 편향);
- chỉ số (metric / 지표) gaming;
- phiên bản (version / 버전) drift;
- hidden huấn luyện (training / 학습) overlap.

Chỉ số (metric / 지표) is another mô hình (model / 모델) requiring kiểm tra hợp lệ (validation / 검증).

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Perplexity** tiếp nhận điểm tựa từ **Learned Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính xác (exact / 정확한) Match** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perplexity

Language-model intrinsic chỉ số (metric / 지표):

\[
PPL=\exp(crossentropy)
\]

Useful compare same tokenization/kiểm thử (test / 테스트) corpus. It measures next-token predictive fit, not downstream instruction/helpfulness directly.

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Chính xác (exact / 정확한) Match** tiếp nhận điểm tựa từ **Perplexity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ nghĩa (semantic / 의미적) QA Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính xác (exact / 정확한) Match

QA/structured extraction often use chính xác (exact / 정확한) string match.

Good when chuẩn gốc (canonical / 정본) answer strict, bad when formatting/paraphrase acceptable.

Normalization can lowercase/remove punctuation/articles but chính sách (policy / 정책) must match tác vụ (task / 작업) and languages.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Ngữ nghĩa (semantic / 의미적) QA Metrics** tiếp nhận điểm tựa từ **Chính xác (exact / 정확한) Match** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Faithfulness vs chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ nghĩa (semantic / 의미적) QA Metrics

Đơn vị từ (token / 토큰) F1 for extractive QA compares overlap. Generative QA may use learned judge/entailment plus factual nguồn (source / 소스) checks.

A semantically similar answer can still contain one dangerous wrong number; aggregate embedding similarity may miss it.

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Faithfulness vs chất lượng (quality / 품질)** tiếp nhận điểm tựa từ **Ngữ nghĩa (semantic / 의미적) QA Metrics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Faithfulness vs chất lượng (quality / 품질)

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

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Human Evaluation** tiếp nhận điểm tựa từ **Faithfulness vs chất lượng (quality / 품질)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM-as-a-Judge Preview** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human Evaluation

Human judges can assess nuanced meaning, but evaluation has variance/độ lệch (bias / 편향).

Need:

- clear rubric;
- blind/randomized comparison;
- multiple raters for subjective tác vụ (task / 작업);
- inter-rater agreement;
- representative samples;
- adjudication for edge cases.

Pairwise preference often easier/more reliable than absolute 1–5 score.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **LLM-as-a-Judge Preview** tiếp nhận điểm tựa từ **Human Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Contamination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM-as-a-Judge Preview

LLM can evaluate outputs cheaply at quy mô (scale / 규모), especially pairwise/rubric tasks.

But judge has biases:

- position độ lệch (bias / 편향);
- verbosity/style preference;
- self/model-family preference;
- prompt sensitivity;
- factual errors;
- vulnerability to answer văn bản (text / 텍스트) injection.

Use calibrated judge against human labels and structured bằng chứng (evidence / 증거) where possible.

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **LLM-as-a-Judge Preview** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Contamination** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Challenge Sets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Contamination

If benchmark appears in pretraining/fine-tuning, score may reflect memorization.

Contamination hard prove for closed dữ liệu huấn luyện (training data / 학습 데이터). New/private/time-split evaluation reduces rủi ro (risk / 위험).

LLM era makes benchmark vòng đời (lifecycle / 생명주기) important.

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Dữ liệu (data / 데이터) Contamination** nêu điều cần giải thích; **Challenge Sets** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Robustness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Challenge Sets

Average IID kiểm thử (test / 테스트) may miss linguistic phenomena. Create targeted sets:

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

Each tests specific năng lực (capability / 역량)/dạng thất bại (failure mode / 실패 모드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Robustness** tiếp nhận điểm tựa từ **Challenge Sets** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multilingual Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Robustness

Perturb đầu vào (input / 입력) without changing meaning:

```text
punctuation change
synonym paraphrase
typo
format reorder
irrelevant sentence insertion
```

Prediction should remain stable if tác vụ (task / 작업) bất biến (invariant / 불변식).

But perturbation must genuinely preserve ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Multilingual Evaluation** tiếp nhận điểm tựa từ **Robustness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Statistical bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multilingual Evaluation

Do not translate English benchmark and assume equivalence. Translation may thay đổi (change / 변경) difficulty, culture, tokenization and ambiguity.

Use native-language datasets/raters and report per-language metrics.

For Korean/Vietnamese, spacing/morphology/tokenization can affect chính xác (exact / 정확한)/overlap metrics; character or ngữ nghĩa (semantic / 의미적) metrics may complement.

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Statistical bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Multilingual Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Online Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Statistical bất định (uncertainty / 불확실성)

Report confidence intervals via bootstrap over examples/documents when possible.

If samples grouped by người dùng (user / 사용자)/document, resample at independent đơn vị (unit / 단위).

Tiny score difference without bất định (uncertainty / 불확실성) should not drive triển khai (deployment / 배포) quyết định (decision / 결정).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Online Evaluation** tiếp nhận điểm tựa từ **Statistical bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) Taxonomy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Online Evaluation

Offline NLP chỉ số (metric / 지표) does not capture người dùng (user / 사용자) tương tác (interaction / 상호작용). A/B testing can measure:

- tác vụ (task / 작업) completion;
- tìm kiếm (search / 검색) success;
- correction/thử lại (retry / 재시도) tỷ lệ (rate / 비율);
- retention;
- độ trễ (latency / 지연 시간) abandonment.

But online chỉ số (metric / 지표) can incentivize bad hành vi (behavior / 동작) (clickbait, verbosity). Guardrails needed.

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Lỗi (error / 오류) Taxonomy** tiếp nhận điểm tựa từ **Online Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reproducible Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) Taxonomy

For generated đầu ra (output / 출력), manually categorize:

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

Lỗi (error / 오류) counts guide kỹ thuật (engineering / 엔지니어링) much more actionable than one BLEU/ROUGE score.

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Reproducible Evaluation** tiếp nhận điểm tựa từ **Lỗi (error / 오류) Taxonomy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reproducible Evaluation

Bản ghi (record / 레코드):

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

Generation settings can materially thay đổi (change / 변경) score.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Reproducible Evaluation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> NLP evaluation is đo lường (measurement / 측정) thiết kế (design / 설계). First define what “good ngôn ngữ (language / 언어) hành vi (behavior / 동작)” means for the tác vụ (task / 작업); only then choose multiple measurements that approximate it.

> **Chuyển mạch:** Trong **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Automatic chỉ số (metric / 지표) cao = đầu ra (output / 출력) tốt cho người dùng (user / 사용자)”

Chỉ số (metric / 지표) captures subset of desired properties.

### “ngữ nghĩa (semantic / 의미적) embedding chỉ số (metric / 지표) solves paraphrase bài toán (problem / 문제) completely”

It may miss factual/number/logical errors.

### “Human evaluation is ground truth without noise”

Humans disagree and have biases; rubric/thiết kế (design / 설계) matter.

### “Benchmark score is mô hình (model / 모델) năng lực (capability / 역량)”

It is hiệu năng (performance / 성능) on a sampled benchmark under specific prompt/eval giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Ở chặng này của **NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

NLP evaluation extends [Model Evaluation](../04_machine_learning/15_model_evaluation.md) and prepares dedicated LLM/RAG evaluation layers where open-ended generation, judges and grounding become central.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
