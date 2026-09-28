# Research Methods — Coverage Audit

## Kết luận hiện tại

Research Methods đã có core canonical route đủ để phục vụ các domain khác mà không duplicate Econometrics. Five core modules hiện cover research design, measurement/sampling, qualitative methods, evidence synthesis, mixed methods/ethics/reproducibility.

Domain này được xem là **core complete ở foundation level**. Advanced methods chỉ nên mở khi một domain cụ thể cần, ví dụ advanced psychometrics, network analysis, text-as-data, spatial methods hoặc implementation science.

## Coverage matrix

| Module | Trạng thái | Coverage |
|---|---|---|
| 00 Research Questions, Theory & Design | Core complete | question types, concepts, theory, hypotheses, mechanisms, rival explanations, scope, case/longitudinal/comparative/experimental design, validity |
| 01 Measurement, Sampling & Survey Design | Core complete | reliability/validity, invariance, scales, survey wording/mode, sampling frames, probability/nonprobability sampling, weighting, nonresponse, data quality |
| 02 Qualitative Methods | Core complete | interviews, observation, ethnography, purposive sampling, coding, thematic/content/discourse analysis, process tracing, reflexivity, triangulation |
| 03 Systematic Reviews & Evidence Synthesis | Core complete | protocols, searches, screening, extraction, risk of bias, meta-analysis, heterogeneity, publication bias, qualitative synthesis, certainty |
| 04 Mixed Methods, Ethics, Reproducibility & Open Science | Core complete | convergent/sequential/embedded designs, ethics/privacy, preregistration, reproducibility, replication, data/code sharing, AI-assisted research boundaries |

## Domain boundary

### Econometrics

`economics/05_econometrics/` owns estimator-level detail and quantitative causal/statistical identification. Research Methods should cross-link rather than repeat OLS, IV, RDD, DiD, panel or time-series derivations.

### Philosophy

Philosophy owns epistemology and philosophy-of-science foundations. Research Methods operationalizes those ideas into study design, evidence and reporting.

### Psychology / Sociology / History / Business / Engineering

These domains should keep domain-specific measurement and cases, while generic sampling, survey, interview, systematic-review and reproducibility principles remain canonical here.

## Quality gates

Every research artifact should make explicit:

```text
question + claim type
scope / population / case boundary
construct + measurement
sampling / case-selection logic
evidence provenance
design / analysis method
validity threats / rival explanations
ethics / privacy
uncertainty / external validity
reproducibility / audit trail
```

## Anti-patterns

Do not treat:

```text
large sample = representative
reliability = validity
statistical significance = causal evidence
participant explanation = causal proof
many papers = strong evidence
reproducibility = correctness
ethics approval = complete ethical reasoning
```

## Advanced expansion gate

Only add a new methodology chapter when:

1. it is reused across multiple domains;
2. current chapters cannot explain it without becoming bloated;
3. it has distinct inferential assumptions/failure modes;
4. there is enough depth to teach mechanism, not glossary.

Potential advanced modules: psychometrics/latent variables, network methods, text-as-data/content computation, spatial research methods, implementation/process evaluation.

## Next repo-wide priority

After Research Methods, the next content gap identified by the repository audit is **Sociology**. Sociology should reuse this library for design/measurement and Psychology/Economics for individual/economic mechanisms rather than duplicate them.
