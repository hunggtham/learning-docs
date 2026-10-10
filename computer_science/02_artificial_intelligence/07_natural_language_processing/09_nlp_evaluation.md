# NLP Evaluation: từ chính xác (exact / 정확한) labels tới open-ended ngôn ngữ (language / 언어) chất lượng (quality / 품질)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **NLP evaluation**. Route đi từ classification/NER exact labels → macro/micro F1 → ranking/generation metrics → human/LLM-assisted evaluation → robustness and task validity, để điểm số không bị tách khỏi mục tiêu sử dụng.

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

> **Mạch nối:** Với nhãn rõ như classification/NER, câu hỏi tiếp theo là dữ liệu lệch lớp làm thay đổi cách đọc F1 ra sao. Macro và micro trả lời hai góc nhìn đó; sau phần này, BLEU mở rộng vấn đề sang đầu ra có nhiều cách diễn đạt.

## Macro vs Micro F1

Micro aggregate all examples/counts, dominated frequent classes.

Macro average F1 each lớp (class / 클래스) equally, exposes rare-class weakness.

Weighted macro uses hỗ trợ (support / 지원) weights.

NLP label distributions often imbalanced, nên report more than one view.

> **Mạch nối:** Macro/micro F1 vẫn đánh giá dựa trên nhãn hoặc quyết định rời rạc. Khi đầu ra là câu dịch, BLEU chuyển sang đo mức trùng khớp n-gram với các bản tham chiếu, vì vậy cần đọc kèm giới hạn của nó.

## BLEU

BLEU measures modified n-gram precision + brevity penalty relative references.

Useful historical MT corpus chỉ số (metric / 지표), cheap/reproducible.

Limitations:

- valid paraphrases penalized;
- ngữ nghĩa (semantics / 의미론)/factuality weak;
- tokenization/tham chiếu (reference / 참조) count affect score;
- sentence-level noisy.

BLEU should compare same setup, not become universal language-quality score.

> **Mạch nối:** BLEU thiên về precision của n-gram, còn ROUGE nhấn mạnh lượng nội dung được thu hồi từ bản tham chiếu. Sự đổi trọng tâm này hữu ích cho tóm tắt, nhưng vẫn chưa giải quyết paraphrase hay factuality.

## ROUGE

ROUGE family emphasizes overlap/recall, dùng chung (common / 공통) summarization.

ROUGE-L uses longest dùng chung (common / 공통) subsequence. It rewards content overlap but cannot reliably detect factual inconsistency.

Extractive các hệ thống (systems / 시스템들) often score well because wording overlaps nguồn (source / 소스).

> **Mạch nối:** Khi overlap bề mặt của ROUGE chưa đủ, METEOR và chrF bổ sung alignment, stemming hoặc character n-gram để bớt phụ thuộc cách tách từ. Những cải tiến này vẫn là tín hiệu tự động, không thay thế phân tích lỗi theo tác vụ.

## METEOR / chrF

METEOR includes stemming/synonym/alignment heuristics.

chrF uses character n-gram F-score and works well morphologically rich languages because less dependent word tokenization.

No chỉ số (metric / 지표) removes need for task-specific lỗi (error / 오류) phân tích (analysis / 분석).

> **Mạch nối:** BERTScore đi thêm một bước: so khớp token bằng biểu diễn ngữ cảnh để nhận ra paraphrase mà n-gram bỏ sót. Đổi lại, điểm số vẫn có thể cao dù nội dung sai sự thật.

## BERTScore

BERTScore matches candidate/tham chiếu (reference / 참조) tokens using contextual embedding similarity.

It captures paraphrases better than surface overlap.

But depends pretrained encoder and can reward semantically similar yet factually wrong outputs.

> **Mạch nối:** Learned metrics dùng mô hình đã học từ đánh giá của con người để ước lượng chất lượng gần hơn với phán đoán thực tế. Vì chúng cũng có bias và drift, perplexity ở mục kế tiếp sẽ quay về tín hiệu nội tại, dễ tái lập hơn nhưng hẹp hơn.

## Learned Metrics

COMET-style MT metrics learn from human judgments/nguồn (source / 소스)/tham chiếu (reference / 참조) representations and often correlate better with human chất lượng (quality / 품질).

Risks:

- lĩnh vực (domain / 도메인)/mô hình (model / 모델) độ lệch (bias / 편향);
- chỉ số (metric / 지표) gaming;
- phiên bản (version / 버전) drift;
- hidden huấn luyện (training / 학습) overlap.

Chỉ số (metric / 지표) is another mô hình (model / 모델) requiring kiểm tra hợp lệ (validation / 검증).

> **Mạch nối:** Perplexity đo độ phù hợp dự đoán token tiếp theo, không đo trực tiếp ích lợi của đầu ra. Với QA hoặc trích xuất có đáp án chuẩn, exact match đặt ra một tiêu chí hẹp nhưng minh bạch hơn.

## Perplexity

Language-model intrinsic chỉ số (metric / 지표):

\[
PPL=\exp(crossentropy)
\]

Useful compare same tokenization/kiểm thử (test / 테스트) corpus. It measures next-token predictive fit, not downstream instruction/helpfulness directly.

> **Mạch nối:** Exact match phù hợp khi đáp án có dạng chuẩn và phải khớp nghiêm ngặt; nó trở nên quá cứng khi chấp nhận paraphrase. Vì thế QA ngữ nghĩa cần thêm các phép đo nhận ra tương đồng nghĩa và vẫn kiểm tra đúng factuality.

## Chính xác (exact / 정확한) Match

QA/structured extraction often use chính xác (exact / 정확한) string match.

Good when chuẩn gốc (canonical / 정본) answer strict, bad when formatting/paraphrase acceptable.

Normalization can lowercase/remove punctuation/articles but chính sách (policy / 정책) must match tác vụ (task / 작업) and languages.

> **Mạch nối:** Các metric ngữ nghĩa nới rộng phép đo vượt khỏi chuỗi ký tự, nhưng tương đồng ngữ nghĩa vẫn có thể bỏ sót một chi tiết sai. Đó là lý do đánh giá faithfulness cần tách riêng khả năng bám nguồn khỏi độ trôi chảy.

## Ngữ nghĩa (semantic / 의미적) QA Metrics

Đơn vị từ (token / 토큰) F1 for extractive QA compares overlap. Generative QA may use learned judge/entailment plus factual nguồn (source / 소스) checks.

A semantically similar answer can still contain one dangerous wrong number; aggregate embedding similarity may miss it.

> **Mạch nối:** Faithfulness và chất lượng bề mặt là hai trục khác nhau: câu có thể trôi chảy nhưng không trung thành với nguồn. Khi nhiều trục cùng quan trọng, human evaluation giúp xem xét những khác biệt mà metric tự động khó biểu diễn.

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

> **Mạch nối:** Đánh giá con người cung cấp phán đoán giàu ngữ cảnh, nhưng cũng chịu variance và bias. LLM-as-a-judge có thể mở rộng quy mô chấm, với điều kiện được hiệu chuẩn và đối chiếu bằng nhãn người.

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

> **Mạch nối:** LLM-as-a-judge giảm chi phí chấm các rubric hoặc so sánh cặp, nhưng bản thân nó là một bộ đánh giá có bias. Trước khi tin vào điểm số, cần xem benchmark có bị nhiễm dữ liệu huấn luyện hay không.

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

> **Mạch nối:** Contamination khiến điểm benchmark có thể phản ánh ghi nhớ thay vì năng lực khái quát. Challenge set bổ sung các trường hợp được thiết kế để buộc mô hình bộc lộ năng lực hoặc lỗi cụ thể.

## Dữ liệu (data / 데이터) Contamination

If benchmark appears in pretraining/fine-tuning, score may reflect memorization.

Contamination hard prove for closed dữ liệu huấn luyện (training data / 학습 데이터). New/private/time-split evaluation reduces rủi ro (risk / 위험).

LLM era makes benchmark vòng đời (lifecycle / 생명주기) important.

> **Mạch nối:** Challenge set biến những nghi ngờ chung về benchmark thành các phép thử hiện tượng cụ thể. Sau đó robustness kiểm tra liệu kết quả có giữ ổn định trước biến đổi đầu vào vẫn bảo toàn nghĩa hay không.

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

> **Mạch nối:** Robustness không chỉ là thêm nhiễu; phép biến đổi phải giữ nguyên yêu cầu của tác vụ. Khi đánh giá nhiều ngôn ngữ, cần kiểm tra riêng tác động của tokenization, văn hóa và dữ liệu bản địa thay vì suy ra từ một ngôn ngữ.

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

> **Mạch nối:** Multilingual evaluation đòi hỏi bộ dữ liệu và người chấm phù hợp từng ngôn ngữ, không chỉ bản dịch của benchmark tiếng Anh. Để biết chênh lệch điểm có đáng tin hay không, phần tiếp theo lượng hóa bất định của ước lượng.

## Multilingual Evaluation

Do not translate English benchmark and assume equivalence. Translation may thay đổi (change / 변경) difficulty, culture, tokenization and ambiguity.

Use native-language datasets/raters and report per-language metrics.

For Korean/Vietnamese, spacing/morphology/tokenization can affect chính xác (exact / 정확한)/overlap metrics; character or ngữ nghĩa (semantic / 의미적) metrics may complement.

> **Mạch nối:** Khoảng tin cậy và đơn vị bootstrap cho biết một chênh lệch nhỏ có thể chỉ là nhiễu lấy mẫu. Nhưng score offline vẫn chưa nói hết trải nghiệm thực tế; online evaluation nối kết quả đo với hành vi người dùng.

## Statistical bất định (uncertainty / 불확실성)

Report confidence intervals via bootstrap over examples/documents when possible.

If samples grouped by người dùng (user / 사용자)/document, resample at independent đơn vị (unit / 단위).

Tiny score difference without bất định (uncertainty / 불확실성) should not drive triển khai (deployment / 배포) quyết định (decision / 결정).

> **Mạch nối:** Online evaluation quan sát hoàn thành tác vụ và tương tác thật, đồng thời phải đề phòng metric thúc đẩy hành vi xấu. Khi một chỉ số không giải thích được kết quả, error taxonomy giúp biến thất bại thành nhóm nguyên nhân có thể sửa.

## Online Evaluation

Offline NLP chỉ số (metric / 지표) does not capture người dùng (user / 사용자) tương tác (interaction / 상호작용). A/B testing can measure:

- tác vụ (task / 작업) completion;
- tìm kiếm (search / 검색) success;
- correction/thử lại (retry / 재시도) tỷ lệ (rate / 비율);
- retention;
- độ trễ (latency / 지연 시간) abandonment.

But online chỉ số (metric / 지표) can incentivize bad hành vi (behavior / 동작) (clickbait, verbosity). Guardrails needed.

> **Mạch nối:** Error taxonomy cho biết mô hình sai ở đâu thay vì chỉ cho biết điểm tổng là bao nhiêu. Muốn so sánh hoặc sửa chữa đáng tin, quy trình tái lập cũng phải ghi lại dữ liệu, mã, phiên bản và cấu hình.

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

> **Mạch nối:** Reproducible evaluation biến kết quả thành một phép đo có thể kiểm tra lại, đồng thời làm rõ tác động của prompt và generation settings. Từ các mảnh đó, mô hình tư duy ở phần sau gom lại nguyên tắc chọn metric.

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

> **Mạch nối:** Mô hình tư duy cốt lõi là: định nghĩa hành vi tốt trước, rồi dùng nhiều phép đo để xấp xỉ nó. Hai ngộ nhận ở phần tiếp theo cho thấy điều gì xảy ra khi đảo ngược thứ tự này.

## Mô hình tư duy (mental model / 사고 모델)

> NLP evaluation is đo lường (measurement / 측정) thiết kế (design / 설계). First define what “good ngôn ngữ (language / 언어) hành vi (behavior / 동작)” means for the tác vụ (task / 작업); only then choose multiple measurements that approximate it.

> **Mạch nối:** Khi đã xác định metric chỉ là phép đo gần đúng, ta có thể nhận diện hai ngộ nhận phổ biến thay vì đồng nhất điểm số với chất lượng. Phần liên kết cuối sẽ chỉ đường quay lại các tài liệu nền tảng.

## Dùng chung (common / 공통) Misconceptions

### “Automatic chỉ số (metric / 지표) cao = đầu ra (output / 출력) tốt cho người dùng (user / 사용자)”

Chỉ số (metric / 지표) captures subset of desired properties.

### “ngữ nghĩa (semantic / 의미적) embedding chỉ số (metric / 지표) solves paraphrase bài toán (problem / 문제) completely”

It may miss factual/number/logical errors.

### “Human evaluation is ground truth without noise”

Humans disagree and have biases; rubric/thiết kế (design / 설계) matter.

### “Benchmark score is mô hình (model / 모델) năng lực (capability / 역량)”

It is hiệu năng (performance / 성능) on a sampled benchmark under specific prompt/eval giao thức (protocol / 프로토콜).

> **Mạch nối:** Các ngộ nhận trên đều bắt nguồn từ việc tách điểm số khỏi mục tiêu và điều kiện đo. Phần liên kết dưới đây đặt NLP evaluation cạnh tài liệu model evaluation và các lớp đánh giá LLM/RAG để tiếp tục đào sâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

NLP evaluation extends [Model Evaluation](../04_machine_learning/15_model_evaluation.md) and prepares dedicated LLM/RAG evaluation layers where open-ended generation, judges and grounding become central.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
