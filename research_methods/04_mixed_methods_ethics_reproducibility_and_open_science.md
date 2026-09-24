# Mixed Methods, Ethics, Reproducibility & Open Science — Tích hợp evidence mà không đánh đổi integrity

Research design không kết thúc khi data đã được phân tích. Một study cần tích hợp các nguồn evidence đúng logic, bảo vệ participants, phân biệt exploratory với confirmatory analysis, và để người khác có thể audit/reproduce những gì đã làm.

## 1. Mixed methods không phải “có cả survey và interview”

Mixed-method research cần integration logic:

```text
Why is one method insufficient?
What does method A answer?
What does method B answer?
Where are results integrated?
```

Nếu hai methods chạy song song nhưng không inform each other, đó chỉ là multi-method collection.

## 2. Convergent design

Quantitative và qualitative data được thu tương đối song song rồi compare/integrate.

Useful khi cần kiểm tra convergence, complementarity hoặc contradiction.

Disagreement không nên bị ép thành một kết luận giả tạo; nó có thể reveal measurement/context differences.

## 3. Explanatory sequential design

Quantitative phase trước, qualitative phase sau để giải thích patterns/outliers/mechanisms.

Ví dụ survey tìm thấy subgroup effect; interviews investigate why.

Participant selection cho phase 2 nên follow analytic purpose.

## 4. Exploratory sequential design

Qualitative phase khám phá concepts/contexts trước, sau đó phát triển scale/survey hoặc quantitative test.

Useful khi construct chưa được định nghĩa tốt.

## 5. Embedded design

Một method đóng vai trò phụ bên trong primary design, ví dụ interviews embedded trong RCT để study implementation/mechanism.

Need distinguish primary estimand from supportive process evidence.

## 6. Integration points

Integration can occur at:

```text
design
sampling
instrument development
analysis
interpretation
```

A strong mixed-method study states exact integration point.

## 7. Joint displays

Tables/matrices can align quantitative result, qualitative theme and integrated interpretation for same subgroup/process.

Joint display prevents methods from living in separate chapters without synthesis.

## 8. Complementarity vs triangulation

Triangulation checks same phenomenon via different methods.

Complementarity uses different methods to answer different dimensions.

Do not demand numeric and interview findings “match” if they measure different constructs.

## 9. Research ethics starts at question/design

Ethics is not paperwork after protocol is complete.

Ask whether study is necessary, risk proportionate, recruitment fair, data minimally invasive and participants can meaningfully consent.

## 10. Informed consent

Consent requires information, comprehension and voluntariness.

A signed form does not guarantee understanding or absence of pressure.

Consent can be ongoing, especially ethnography/longitudinal research.

## 11. Vulnerable participants

Children, dependent employees, patients, migrants or politically exposed groups may face power asymmetry.

Recruitment and withdrawal must avoid coercion or consequences.

## 12. Privacy vs confidentiality

Privacy concerns access to person/context; confidentiality concerns handling information after collection.

Anonymization is difficult when rich qualitative or linked administrative data contain indirect identifiers.

## 13. Data minimization

Collect only fields needed for question.

“Maybe useful later” is not enough justification for highly sensitive data.

## 14. De-identification

Removing names does not guarantee anonymity. Location, age, job title, rare events or timestamps can re-identify.

Risk grows when datasets can be linked externally.

## 15. Sensitive topics

Research on health, immigration, workplace conflict, violence or illegal activity requires special storage/access/reporting plans.

Publication excerpts should not accidentally identify participants.

## 16. Secondary data ethics

Existing data may be legally accessible but ethically sensitive.

Original consent/context and reasonable expectations matter.

## 17. Internet research ethics

Public posts vary in expected privacy. Quoting searchable text can identify users even without username.

Paraphrase or permission may be needed depending risk/context.

## 18. Risk-benefit assessment

Research benefit is often societal/knowledge benefit; participant bears immediate risk.

Design should minimize harm independently of hoped-for importance.

## 19. Researcher conflicts of interest

Funding, employment, consulting or ideological commitments can influence question, analysis and reporting.

Disclosure does not eliminate bias but enables assessment.

## 20. Preregistration

Preregistration records hypotheses, outcomes and analysis plans before observing relevant results.

It reduces undisclosed flexibility but does not make weak design strong.

Exploratory work remains legitimate if labeled.

## 21. Pre-analysis plans

Detailed plans may specify samples, exclusions, transformations, models, outcomes and multiple-testing adjustments.

Deviations are acceptable when explained transparently.

## 22. Registered reports

Study question/method undergo peer review before results are known; publication commitment depends less on significance.

This directly reduces publication bias for confirmatory work.

## 23. Reproducibility

Computational reproducibility asks whether same data/code/environment regenerate figures/tables/results.

It requires versioned inputs, code, dependencies and deterministic processing where possible.

## 24. Replicability

Replication repeats study with new data/sample to assess whether finding recurs.

A reproducible analysis can still be scientifically wrong; reproducibility is necessary transparency, not validity proof.

## 25. Data provenance

Track raw source, collection date, transformations, merges and exclusions.

Never overwrite raw data with cleaned version.

## 26. Reproducible pipeline

A strong workflow:

```text
raw data (read-only)
→ scripted cleaning
→ analysis-ready data
→ analysis code
→ figures/tables/report
```

Manual spreadsheet edits should be avoided or logged.

## 27. Version control

Git or equivalent tracks code/protocol changes.

Data versions need separate handling when files large/sensitive.

Commit history should reflect meaningful analytical changes, not replace documentation.

## 28. Environment capture

Package/library versions can alter results.

Use lockfiles, environment files or containers where appropriate.

## 29. Random seeds

Simulation, bootstrapping and ML workflows should set/report seeds when deterministic reproduction matters.

Seed alone does not guarantee reproducibility across hardware/software implementations.

## 30. Reproducible figures/tables

Final numbers should be generated from code, not manually copied/edited.

This prevents report/code drift.

## 31. Data sharing

Open data improves audit/replication but may conflict with privacy, contracts or indigenous/community governance.

Options include synthetic data, secure enclaves, restricted access or sharing code/data dictionaries only.

## 32. Code sharing

Even when data cannot be shared, analysis code, schemas and simulated examples can expose logic.

Remove credentials/identifiers before publication.

## 33. FAIR principles

Data should be as Findable, Accessible, Interoperable and Reusable as ethically/legal feasible.

“Open” is not always appropriate; “as open as possible, as closed as necessary” is better.

## 34. Open materials

Survey instruments, interview guides, codebooks and protocols improve interpretability and replication.

Copyright/license restrictions may apply to proprietary scales.

## 35. Reporting guidelines

Different designs have reporting standards (experiments, observational studies, qualitative research, systematic reviews).

Guidelines improve completeness but do not substitute for methodological judgment.

## 36. Null and negative results

Report meaningful null/contradictory evidence rather than hiding it.

Selective reporting distorts literature and future meta-analysis.

## 37. HARKing

Hypothesizing After Results are Known is problematic when presented as pre-specified confirmation.

Post-hoc hypotheses are valuable for future testing if labeled exploratory.

## 38. P-hacking and analytical flexibility

Trying many exclusions/outcomes/models until significance appears inflates false positives.

Transparent multiverse/specification analysis and preregistration reduce hidden flexibility.

## 39. AI-assisted research

AI can help search, code, summarize or draft, but researcher remains responsible for source verification, privacy and analytical correctness.

Do not upload sensitive data to systems without approved data handling.

Generated citations/claims must be checked against original sources.

## 40. Automation risks

Automated cleaning/classification can silently propagate errors at scale.

Build validation checks, sample manual review and logs.

## 41. Research notebook

Maintain decisions, anomalies, failed analyses and rationale.

This is especially important when final report shows only polished path.

## 42. Team workflows

Define ownership of data, code, analysis decisions and review.

Code review and double-checking critical transformations reduce single-person errors.

## 43. Reproducibility audit

Before release, another person should be able to run pipeline from documented inputs and regenerate outputs.

Missing path, hidden manual step or local-only dependency is a reproducibility defect.

## 44. Interpretation discipline

Final conclusion should match strongest supported claim:

```text
descriptive association
interpretive theme
identified causal effect
mechanism evidence
prediction
```

Do not upgrade claim category during writing.

## 45. Uncertainty communication

Report sampling/statistical uncertainty plus design, measurement and external-validity uncertainty qualitatively where not quantifiable.

Precision is not certainty.

## 46. Ethical publication

Avoid sensationalizing vulnerable groups, overclaiming intervention benefits or exposing identifiable details.

Participants are not raw materials for a compelling story.

## 47. Failure modes

Sai lầm thứ nhất là call any two-method project “mixed methods”.

Sai lầm thứ hai là treat ethics approval as complete ethical reasoning.

Sai lầm thứ ba là equate reproducibility with correctness.

Sai lầm thứ tư là hide exploratory decisions behind confirmatory language.

Sai lầm thứ năm là open sensitive data without re-identification assessment.

## 48. Final research-quality checklist

1. question/design alignment rõ chưa?
2. measurement/sampling credible không?
3. quantitative/qualitative inference category đúng không?
4. mixed-method integration point ở đâu?
5. ethics/consent/privacy risks được xử lý chưa?
6. protocol/deviations documented chưa?
7. raw→clean→analysis pipeline reproducible không?
8. code/material/data sharing phù hợp chưa?
9. null/negative evidence có bị selective reporting không?
10. final claims có đúng phạm vi evidence không?

Research Methods kết thúc ở đây với một principle: rigor không đến từ một method label. Nó đến từ alignment giữa question, evidence, design, analysis, transparency và phạm vi claim.
