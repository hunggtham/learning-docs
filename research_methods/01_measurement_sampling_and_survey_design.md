# Measurement, Sampling & Survey Design — Đo đúng trước khi phân tích đúng

Research quality thường bị quyết định ở measurement và sampling trước khi analyst mở statistical software. Một measure có thể rất precise nhưng đo sai construct; một sample rất lớn nhưng không đại diện population; một survey có response rate cao nhưng wording tạo systematic bias.

## 1. Concept → construct → indicator

Chuỗi measurement:

```text
Concept
→ conceptual definition
→ operational definition
→ observable indicator(s)
```

Ví dụ “job satisfaction” không phải một trực tiếp observable fact. Nó có thể được operationalize bằng validated scale, interview coding hoặc behavioral proxy — mỗi cách capture một phần khác nhau.

## 2. Reliability

Reliability là consistency của measure.

Các forms gồm:

- test–retest reliability;
- inter-rater reliability;
- internal consistency;
- measurement stability across forms/occasions.

High reliability không đảm bảo validity.

## 3. Validity

Measurement validity hỏi measure có represent intended construct không.

Các dimensions:

- content validity;
- convergent/discriminant validity;
- criterion validity;
- construct validity.

No single coefficient can fully “prove validity”; it accumulates through theory + evidence.

## 4. Measurement invariance

A scale may behave differently across languages, cultures, genders, age groups or time.

If respondents interpret items differently, comparing raw means can be invalid.

Translation requires semantic/conceptual equivalence, not word-for-word mapping only.

## 5. Reflective vs formative measures

Reflective model treats latent construct as causing observed indicators.

Formative model treats indicators as composing construct.

Dropping one item has different meaning in the two models.

## 6. Single-item vs multi-item measures

Single-item questions are efficient for concrete variables. Complex constructs often benefit from multiple items to cover dimensions and reduce random error.

More items are not automatically better if redundant or poorly worded.

## 7. Scale construction

Good scale development involves theory, item generation, cognitive testing, pilot data and validation.

Do not create arbitrary score by averaging unrelated questions because Cronbach’s alpha looks acceptable.

## 8. Internal consistency

Cronbach’s alpha depends on item number/correlation and assumes conditions often ignored.

High alpha can reflect redundancy, not unidimensionality.

Factor structure and substantive content matter.

## 9. Inter-rater reliability

When humans code texts/behavior, agreement needs training and explicit codebook.

Raw percent agreement can be misleading with imbalanced categories; kappa/ICC may be more appropriate depending data.

Disagreement can reveal ambiguous construct boundaries, not merely coder failure.

## 10. Measurement error

Observed value:

```text
Observed = True construct component + error/bias
```

Random error reduces precision; systematic error biases inference.

Self-report, administrative and sensor data have different error structures.

## 11. Common-method bias

If predictor and outcome come from same survey at same moment, response style/social desirability can inflate association.

Design remedies include temporal separation, multiple sources and objective measures where appropriate.

## 12. Social desirability

Sensitive topics can produce under/over-reporting based on norms.

Anonymity, indirect questioning or list/randomized-response methods can reduce bias but increase complexity.

## 13. Recall bias

Retrospective questions degrade with time and salience.

Event-history calendars or records can help.

Recall error may differ systematically by outcome/group.

## 14. Question wording

Leading, double-barreled, vague or loaded items change responses.

Ask one concept at a time and specify timeframe/reference.

## 15. Response options

Categories should be mutually exclusive, collectively sensible and ordered consistently when ordinal.

Adding/removing midpoint or “don’t know” can alter distributions.

## 16. Likert scales

Likert-type items are ordinal responses to statements; summated scales combine multiple items.

Treating ordinal scores as interval may be practical under conditions but should be justified rather than assumed invisibly.

## 17. Order effects

Earlier questions prime later responses. Randomization or careful grouping can diagnose/order effects.

Survey flow should balance context coherence with contamination risk.

## 18. Cognitive interviewing

Before launch, ask participants to explain how they understand and answer items.

This reveals interpretation problems quantitative pilots may miss.

## 19. Pilot studies

Pilot tests instrument, recruitment, timing, data pipeline and analysis feasibility.

Pilot effect estimates are usually too noisy to serve as final evidence.

## 20. Target population

Define who inference concerns.

Population can be narrower than accessible respondents. Avoid vague phrases like “people” when sample is “Korean office workers in Seoul tech firms”.

## 21. Sampling frame

Sampling frame is operational list/process from which sample is drawn.

Coverage error occurs when frame excludes portions of target population.

## 22. Probability sampling

Units have known/nonzero selection probabilities.

Common designs:

- simple random;
- stratified;
- cluster;
- multistage.

Weights may be required for unequal probabilities.

## 23. Stratified sampling

Divide population into strata and sample within each.

Useful to guarantee representation of small important groups and improve precision.

Analysis should account sampling weights/design.

## 24. Cluster sampling

Sample groups like schools/areas then units within them.

Cost-efficient but intra-cluster similarity reduces effective sample size.

## 25. Convenience sampling

Easy-access samples can be useful for exploratory work but limit population inference.

Large convenience sample is not transformed into probability sample by N alone.

## 26. Snowball/respondent-driven sampling

Useful for hidden populations through network recruitment.

Network structure and differential recruitment probabilities complicate representativeness.

## 27. Nonresponse

Response rate alone does not determine bias.

Bias occurs when response propensity relates to survey variables after weighting/adjustment.

A lower response rate can be less biased than a higher but selective one.

## 28. Post-stratification and weighting

Weights adjust sample to known population margins or selection probabilities.

They can reduce bias but increase variance and cannot fix unmeasured differences automatically.

## 29. Sample size

Sample size should follow estimand, expected variance, minimum meaningful effect, design effect and subgroup requirements.

“30 is enough” or “1000 is always representative” are not general rules.

## 30. Power

Power is probability of detecting a specified effect under assumptions.

Planning needs meaningful effect size, not only historical average.

For descriptive estimation, precision/margin-of-error may be more relevant than hypothesis-test power.

## 31. Census data are not error-free

Administrative/census sources can have undercoverage, coding changes, incentives and missingness.

No sampling error does not mean no measurement error.

## 32. Administrative data

Advantages: scale, longitudinal coverage, less recall.

Risks: variables created for operational—not research—purposes; policy-driven coding and missing populations.

## 33. Digital trace data

Clicks, GPS, logs and platform data measure behavior at high frequency but only for platform users under platform-generated environment.

Platform changes can change data-generating process.

## 34. Missing data

Missingness may be item nonresponse, attrition or unavailable records.

Deletion is unbiased only under restrictive mechanisms; imputation requires assumptions and should preserve uncertainty.

## 35. Mode effects

Phone, face-to-face, paper and online surveys can produce different answers due privacy, interviewer presence and interface.

Mode changes across waves threaten comparability.

## 36. Translation and multilingual research

Back-translation helps but does not guarantee conceptual equivalence.

Use bilingual expert review + cognitive interviews in target language/culture.

## 37. Pretesting data pipeline

Research errors also occur in IDs, merges, timestamps, coding and units.

Validation rules, range checks, duplicate detection and provenance should be designed before full collection.

## 38. Data dictionary

Every variable should document:

```text
name
definition
unit
coding
missing values
source
timing
transformations
```

This is part of scientific reproducibility.

## 39. Failure modes

Sai lầm thứ nhất là equate reliability with validity.

Sai lầm thứ hai là use a popular scale without checking population/language validity.

Sai lầm thứ ba là call large convenience sample representative.

Sai lầm thứ tư là treat response rate as sole nonresponse-bias measure.

Sai lầm thứ năm là change survey mode/items across waves without comparability analysis.

## 40. Measurement/sampling checklist

1. target population là ai?
2. frame cover ai và bỏ ai?
3. sampling mechanism nào?
4. construct definition là gì?
5. indicators capture dimensions nào?
6. reliability + validity evidence nào?
7. wording/mode/social-desirability threats nào?
8. missing/nonresponse mechanism nào?
9. weights/design effects cần xử lý không?
10. instrument/data pipeline đã pilot chưa?

Quantitative measurement chỉ là một route. Nhiều câu hỏi về meaning, process và institutions cần qualitative methods để tạo evidence sâu thay vì ép thành scale quá sớm.
