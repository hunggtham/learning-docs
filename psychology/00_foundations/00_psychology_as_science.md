# Tâm lý học như một khoa học

Tâm lý học nghiên cứu hành vi và quá trình tâm trí, nhưng phần lớn đối tượng quan tâm — trí nhớ, chú ý, động lực, cảm xúc, niềm tin, self-control — không thể quan sát trực tiếp như một vật thể. Vì vậy, câu hỏi trung tâm của psychology science không chỉ là “con người làm gì?”, mà là **làm sao suy luận đáng tin từ observation sang construct và mechanism**.

> **Trạng thái bằng chứng:** psychology là một empirical science sử dụng experiment, observation, measurement, statistics và cumulative evidence. Specific theories bên trong psychology có evidence status khác nhau; không nên đánh đồng “được nghiên cứu khoa học” với “đã chứng minh đúng”.

Xem [[../EVIDENCE_STATUS_GUIDE]].

## 1. Từ common sense sang scientific question

Một đồng nghiệp ít nói trong meeting có thể bị giải thích là introvert, không đồng ý, mệt, không hiểu ngôn ngữ, hoặc đang lo hierarchy. Nhiều story cùng plausible.

Science bắt đầu khi ta hỏi:

- prediction nào khác nhau giữa stories?
- variable nào đo được?
- alternative explanation nào phải control?
- evidence nào sẽ làm model yếu đi?

Common sense thường giải thích tốt **sau** khi outcome xảy ra. Science đòi prediction hoặc inference rule đủ rõ **trước** khi biết answer.

## 2. Construct và observable indicator

**Cấu trúc tâm lý (construct)** là concept lý thuyết như anxiety, intelligence, trust hoặc motivation.

Construct không phải direct object. Ta infer từ indicators:

```text
Reaction time
Self-report
Behavior
Physiology
Observer rating
Choice pattern
```

Một indicator không phải chính construct. Đây là lý do [[03_measurement_statistics]] và [[05_psychometrics_and_test_interpretation]] nằm ở core của library.

## 3. Operationalization

**Thao tác hóa (operationalization)** biến concept thành procedure measurable.

Attention có thể đo bằng reaction time, eye movement, accuracy under distraction hoặc neural signal. Các operationalizations có thể capture different aspects.

Nếu conclusion chỉ xuất hiện với một operationalization, cần hỏi effect thuộc construct hay task artifact.

## 4. Description, prediction, explanation và intervention

Bốn loại question khác nhau:

### Description

Điều gì đang xảy ra?

### Prediction

Khi X thay đổi, Y có tend thay đổi không?

### Explanation

Mechanism nào tạo relation?

### Intervention

Nếu ta chủ động thay X, Y có đổi không?

Correlation có thể support prediction mà chưa support intervention. Đây là lỗi phổ biến khi chuyển observational finding thành self-help recommendation.

## 5. Correlation không phải causation

Nếu poor sleep correlate with low mood:

```text
sleep → mood
mood → sleep
stress → both
measurement artifact
selection effect
```

đều có thể plausible.

Causal inference cần design và assumptions. Xem [[08_causal_inference_and_psychological_evidence]].

## 6. Multiple levels of analysis

Một phenomenon có thể được giải thích đồng thời ở nhiều levels:

```text
Biological
Cognitive
Learning
Developmental
Social
Cultural
Organizational
```

Interview anxiety có thể liên quan autonomic arousal, catastrophic prediction, prior learning, status threat và labor-market pressure.

Tìm neural correlate không làm social explanation disappear; social context cũng không phủ nhận biology.

## 7. Reductionism và explanatory level

Reductionism useful khi cần mechanism nhỏ hơn. Nhưng “amygdala activated” không giải thích toàn bộ fear. Neural event itself needs context, computation and behavior interpretation.

Ngược lại, vague explanation như “do society” cũng insufficient nếu không specify pathway.

Strong psychology connects levels instead of declaring one level “realer” than others.

## 8. Experimental method

Random assignment helps distribute confounders probabilistically between conditions. Manipulation supports causal inference stronger than simple observation.

But experiment can still fail because:

- manipulation does not target intended construct;
- demand characteristics;
- attrition;
- low power;
- poor measurement;
- unrealistic task;
- analysis flexibility.

Experiment is not automatic truth machine.

## 9. Observational research

Many important questions cannot be randomized: poverty, trauma, migration, personality development, long-term disease.

Observational research can be powerful with longitudinal designs, natural experiments, quasi-experiments, matching, instrumental variables or causal models — but assumptions must be explicit.

## 10. Internal và external validity

**Internal validity** asks whether inference inside study is credible. **External validity** asks whether finding generalizes to other people, settings, tasks and times.

Perfect lab control may reduce ecological realism; real-world study may increase confounding. Good science uses triangulation rather than treating one design as universal best.

## 11. Triangulation

Confidence increases when different methods with different weaknesses converge:

```text
Experiment
+ longitudinal data
+ field observation
+ psychophysiology
+ qualitative/contextual evidence
```

If all methods share same measurement bias, apparent convergence may still mislead.

## 12. Replication

One study is evidence, not verdict.

Replication asks whether pattern reappears under similar or theoretically related conditions. Failure to replicate can reveal original false positive, overestimated effect, context dependency, measurement issue or insufficient precision.

Xem [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 13. Open science

Preregistration, registered reports, open materials, data/code sharing when ethical, and transparent analysis help reduce hidden researcher flexibility.

These practices do not guarantee good science. A bad study can be preregistered. Their value is making inference process more auditable.

Xem [[06_open_science_and_evidence_evaluation]].

## 14. Statistical significance is not importance

A tiny effect can have low p-value in huge sample. A meaningful effect can be uncertain in small sample.

Read:

```text
effect size
+ uncertainty
+ measurement quality
+ design
+ generalizability
```

not p-value alone.

## 15. Null result is informative only under conditions

“Non-significant” does not automatically mean no effect. Study may be low power or measure poorly.

But repeatedly precise estimates near zero can meaningfully constrain theory.

Bayesian and equivalence approaches can formalize evidence about small/null effects under explicit assumptions.

## 16. Theory vs hypothesis

A **giả thuyết (hypothesis)** is specific testable proposal. A **lý thuyết (theory)** organizes multiple findings and generates predictions.

Popular discourse sometimes calls speculation “theory”; science uses theory as structured explanatory model.

See five-level taxonomy in [[../EVIDENCE_STATUS_GUIDE]].

## 17. Falsifiability is useful but not sufficient

A scientific claim should expose itself to possible failure. But falsifiability alone does not make theory good; vague auxiliary assumptions can rescue almost any model after failure.

Useful theory also needs precision, explanatory scope, predictive success and parsimony relative to alternatives.

## 18. Measurement is theory-laden

If we define depression by a questionnaire, instrument choices shape what data can say. If item asks sleep difficulty, sleep changes can move depression score even if other symptoms stable.

Measurement is not neutral pipeline after theory; it partly constructs empirical target.

## 19. Population matters

Psychology historically relied heavily on Western, educated samples. A result in university students cannot automatically become “human nature”.

Culture, language, socioeconomic context, age and migration can change both behavior and how questionnaire items function.

Xem [[../03_human_development_and_person/04_social_and_cultural_psychology]] và [[05_psychometrics_and_test_interpretation]].

## 20. WEIRD problem

WEIRD = Western, Educated, Industrialized, Rich, Democratic.

The point is not that Western samples are invalid; it is that **sampling frame limits inference**. Cross-cultural replication can test whether theory generalizes or needs boundary conditions.

## 21. Individual difference vs group average

An average effect does not tell every person's response.

If intervention improves score by 0.3 SD on average, some improve more, some less, some worsen. Personalized prediction requires reliable moderators and out-of-sample validation, not post-hoc storytelling.

## 22. Science of individual people

Group research is useful, but everyday application often asks “what works for this person?”. N-of-1 designs, EMA and repeated measures can help estimate within-person pattern.

But self-tracking also suffers confounding, expectation and regression to mean.

Xem [[07_ecological_momentary_assessment_and_real_world_measurement]].

## 23. Psychology and self-help

Self-help often starts from recommendation:

> wake at 5, think positive, use body language, build habit in 21 days.

Scientific psychology asks:

- construct?
- mechanism?
- comparator?
- effect size?
- boundary condition?
- harm/trade-off?
- replication?

A useful tip can work despite wrong theory; a statistically real average effect may be too small to matter individually.

## 24. Evidence hierarchy is not a ladder that solves everything

RCTs, meta-analyses and systematic reviews are powerful, but quality varies. Meta-analysis of biased studies can give precise biased answer.

Mechanism question may need experiment; prevalence question may need representative survey; lived-experience question may need qualitative method.

Best method depends question.

## 25. Historical theories

Freud, Adler and Jung belong to history of Psychology and psychotherapy. They introduced influential questions about unconscious process, meaning, goal, identity and development.

But historical influence is not scientific validation.

```text
Historical theory
→ can inspire hypothesis
→ hypothesis must be operationalized
→ data test claim
→ modern evidence status determined independently
```

Xem [[../90_connections/06_historical_theories_and_modern_evidence_matrix]].

## 26. Psychology and neuroscience

Psychological construct and neural implementation are different levels.

A construct can be scientifically useful without one-to-one brain region. Conversely, brain activity only gains psychological meaning through task/model interpretation.

## 27. Psychology and AI

AI creates a useful analogy: a model can predict accurately without causal understanding; feature importance does not equal causal variable; benchmark performance can fail out-of-distribution.

Psychology shares same problems: measurement, generalization, confounding and interpretability.

Xem [[../90_connections/01_psychology_biology_statistics_and_ai]].

## 28. Five evidence statuses

Every claim should be readable as one of:

1. bằng chứng tương đối vững;
2. lý thuyết hiện đại;
3. giả thuyết;
4. vấn đề còn tranh luận;
5. lý thuyết lịch sử.

This avoids language like “scientists proved” when evidence only supports a model under assumptions.

## 29. Mental model

```text
Phenomenon
   ↓
Construct
   ↓
Operationalization
   ↓
Measurement
   ↓
Data
   ↓
Statistical / causal inference
   ↓
Replication & synthesis
   ↓
Theory update
   ↓
Careful application
```

Every arrow can fail. Scientific maturity is not certainty; it is explicit error-correction.

## Kết nối kiến thức

Đọc tiếp [[02_research_methods]], [[03_measurement_statistics]], [[05_psychometrics_and_test_interpretation]], [[06_open_science_and_evidence_evaluation]], [[08_causal_inference_and_psychological_evidence]], [[09_replication_meta_analysis_and_bayesian_reasoning]] và [[../CONCEPTUAL_DEPENDENCIES]].
