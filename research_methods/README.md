# Research Methods Knowledge Library

`research_methods/` là domain canonical về cách biến một câu hỏi thành nghiên cứu có thể kiểm tra, đo lường, thu thập evidence, phân tích và báo cáo minh bạch. Nó nằm giữa Philosophy of Science, Statistics/Econometrics và các domain applied: không thay thế các tool thống kê chuyên sâu, mà xác định **question–design–measurement–evidence–claim alignment**.

## Thứ tự học canonical

1. [Research Questions, Theory & Design](./00_research_questions_theory_and_design.md) — question types, concepts, theory, hypotheses, mechanisms, rival explanations, scope, case/longitudinal/comparative/experimental logic và validity.
2. [Measurement, Sampling & Survey Design](./01_measurement_sampling_and_survey_design.md) — construct validity, reliability, scale design, measurement error, probability/nonprobability sampling, nonresponse, weighting, surveys và data-quality pipelines.
3. [Qualitative Methods](./02_qualitative_methods_interviews_ethnography_and_case_studies.md) — purposive sampling, interviews, observation, ethnography, coding, thematic/content/discourse analysis, process tracing, reflexivity và qualitative generalization.
4. [Systematic Reviews & Evidence Synthesis](./03_systematic_reviews_and_evidence_synthesis.md) — protocols, search/screening, risk of bias, meta-analysis, heterogeneity, publication bias, qualitative synthesis và evidence certainty.
5. [Mixed Methods, Ethics, Reproducibility & Open Science](./04_mixed_methods_ethics_reproducibility_and_open_science.md) — integration designs, consent/privacy, preregistration, reproducible pipelines, replication, data/code sharing, reporting và AI-assisted research boundaries.

## Learning spine

```text
Research problem
→ question type
→ theory / concepts / mechanism
→ design and case/sample selection
→ measurement / evidence collection
→ analysis method
→ validity / rival explanations
→ synthesis / interpretation
→ ethics / reproducibility
→ scoped claim
```

Method choice comes after question. A survey, RCT, interview, case study or meta-analysis is not inherently “stronger” independent of what is being asked.

## Boundary với Econometrics

[Econometrics](../economics/05_econometrics/README.md) owns quantitative estimators and statistical/causal identification in depth: OLS, experiments, IV, RDD, DiD, panel, time series, inference and robustness.

Research Methods owns broader design logic: construct/operationalization, sampling, survey design, qualitative inference, mixed methods, literature synthesis, ethics, research protocols and open-science workflow.

Cross-link instead of duplicating equations/estimator derivations.

## Boundary với Philosophy

[Philosophy](../philosophy/README.md) handles epistemology, philosophy of science, explanation, causation and normative questions at a foundational level. Research Methods turns those questions into operational research decisions.

## Boundary với domain applied

Psychology, Sociology, Economics, History, Education, Business or Engineering research should reuse this domain for common methodology and keep domain-specific measurement/design examples in their own libraries.

A domain chapter should not re-explain generic sampling, interview coding or systematic-review mechanics unless a special domain constraint changes them.

## Evidence categories

Every claim should be labeled internally by the evidence it actually supports:

```text
Descriptive
Predictive
Interpretive
Causal
Mechanistic
Synthesized / literature-level
```

Do not upgrade category during writing. A participant explanation is not automatically causal evidence; a predictive model is not automatically explanatory; a statistically significant association is not automatically causal.

## Quality contract

A complete study should make explicit:

```text
question
scope / population / setting
concepts and operational definitions
unit / level of analysis
sampling or case-selection logic
data/evidence provenance
analysis method
rival explanations / validity threats
ethics and privacy
uncertainty and limits
reproducibility materials
```

## Connections

- [Mathematics](../mathematics/README.md): probability/statistics foundation.
- [Economics / Econometrics](../economics/05_econometrics/README.md): causal/statistical estimators.
- [Philosophy](../philosophy/README.md): epistemology, causation and explanation.
- [Psychology](../psychology/README.md): psychometrics, experiments, behavioral measurement.
- [World History](../world_history/README.md): archival/historical evidence and source criticism.
- [Computer Science](../computer_science/README.md): data pipelines, computation, reproducibility and AI-assisted workflows.

## Mục tiêu cuối

Người học không chỉ biết tên methods. Họ phải có thể nhìn một research claim và hỏi đúng thứ tự: câu hỏi là gì, construct có đo đúng không, sample/case đến từ đâu, design phân biệt competing explanations thế nào, analysis phù hợp data-generating process không, ethics/reproducibility ra sao, và conclusion có đi xa hơn evidence cho phép hay không.
