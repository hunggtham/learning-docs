# Systematic Reviews & Evidence Synthesis — Từ literature search đến kết luận có trọng số

Literature review không nên là danh sách paper nối bằng prose. Evidence synthesis cần question, inclusion criteria, search strategy, quality assessment và logic kết hợp findings đủ rõ để người khác hiểu vì sao một study được đưa vào và một study khác bị loại.

## 1. Narrative review vs systematic review

Narrative review linh hoạt, hữu ích để map theory/history nhưng dễ bị selection bias.

Systematic review pre-specifies transparent search/screening/synthesis process.

Neither is automatically superior; purpose differs.

## 2. Review question

A review question should specify population/context, exposure/intervention, comparison, outcome and study types when relevant.

Frameworks như PICO/SPIDER help structure but should not force inappropriate biomedical format onto social questions.

## 3. Protocol

Before searching, define:

```text
question
sources/databases
search concepts
inclusion/exclusion
screening process
quality/risk-of-bias criteria
extraction fields
synthesis plan
```

Protocol reduces post-hoc selection.

## 4. Search strategy

Search needs synonyms, controlled vocabulary, Boolean logic, citation chaining and grey literature where appropriate.

One database rarely covers all fields.

## 5. Search sensitivity vs precision

Broad search captures more relevant studies but increases screening load.

Narrow search is efficient but risks missing evidence.

Balance should be documented.

## 6. Grey literature

Theses, reports, preprints, working papers and government documents can reduce publication bias but vary in review quality.

Exclusion should be reasoned, not automatic.

## 7. Citation chaining

Backward chaining checks references; forward chaining finds later work citing key studies.

Useful for terminology changes and interdisciplinary topics.

## 8. Screening

Title/abstract then full-text screening should follow criteria consistently.

Multiple reviewers can estimate disagreement and reduce arbitrary inclusion.

## 9. Inclusion/exclusion criteria

Criteria should reflect question and minimum evidence requirements, not desired results.

Examples: population, timeframe, design, outcome definition, language, publication type.

## 10. PRISMA-style flow

A flow diagram records identified, deduplicated, screened, excluded and included records.

Transparency about exclusion is part of reproducibility.

## 11. Data extraction

Extract more than effect size:

```text
sample/context
design
measurement
treatment/exposure
estimand
follow-up
assumptions
uncertainty
funding/conflicts
```

This enables heterogeneity analysis.

## 12. Risk of bias

Study quality should be threat-specific: randomization, attrition, confounding, measurement, selective reporting, etc.

Avoid one opaque total quality score that treats all flaws as interchangeable.

## 13. Evidence hierarchy limitations

RCTs are powerful for causal intervention questions, but observational/qualitative/historical designs may be necessary for long-term, rare, institutional or mechanism questions.

Design suitability matters more than universal hierarchy.

## 14. Effect size

Meta-analysis needs comparable effect metrics: mean difference, standardized mean difference, risk ratio, odds ratio, correlation or transformed coefficients.

Conversion assumptions should be documented.

## 15. Fixed-effect model

Fixed-effect meta-analysis assumes studies estimate one common true effect and differences are sampling error.

Appropriate only when substantive homogeneity is plausible.

## 16. Random-effects model

Random-effects allows true effects vary across studies/settings.

Pooled estimate is mean of effect distribution under model, not a universal effect applying everywhere.

## 17. Heterogeneity

Statistical heterogeneity measures like `I²` summarize inconsistency but do not explain it.

Substantive heterogeneity may come from population, treatment intensity, design, measurement or institutions.

## 18. Prediction intervals

Confidence interval estimates uncertainty around mean effect; prediction interval estimates range for effect in a new comparable study under model.

High heterogeneity makes prediction interval especially important.

## 19. Meta-regression

Meta-regression explores study-level moderators.

It is observational at study level and vulnerable to confounding/ecological bias, especially with few studies.

## 20. Publication bias

Positive/significant findings may be overrepresented.

Funnel plots/tests can detect asymmetry but also respond to heterogeneity and design differences.

No single correction solves publication bias reliably.

## 21. P-hacking and selective outcomes

A published study may report one of many outcomes/specifications.

Compare protocols/registrations when available; outcome switching affects synthesis.

## 22. Small-study effects

Small studies may have larger effects due publication bias, different populations/interventions or higher variance.

Treat as diagnostic pattern requiring explanation.

## 23. Dependence among effects

One study may report many outcomes/timepoints, violating independence if all treated as separate studies.

Use pre-specified selection, multilevel meta-analysis or robust variance methods.

## 24. Clustered and repeated designs

Effect sizes must respect original design. Ignoring cluster randomization or repeated measures can understate variance.

## 25. Combining different designs

RCTs, observational and qualitative studies may answer different pieces of question.

Do not mechanically pool incomparable estimands. Use separate synthesis layers then integrate conclusions.

## 26. Qualitative evidence synthesis

Thematic synthesis, meta-ethnography and framework synthesis combine concepts/themes across qualitative studies.

Goal is interpretation/mechanism, not numeric averaging.

## 27. Scoping review

Scoping review maps breadth, concepts, evidence gaps and study types when question too broad/immature for effect synthesis.

It should still use transparent search/screening.

## 28. Umbrella review

Umbrella review synthesizes existing systematic reviews.

Risk: double-counting primary studies and propagating weak reviews.

## 29. Living review

For fast-moving topics, living systematic review updates searches/synthesis periodically.

Requires automation/workflow and clear versioning.

## 30. Evidence certainty

Certainty should consider bias, consistency, precision, directness and publication/reporting concerns.

“Many papers” is not equivalent to strong evidence.

## 31. Directness

A study can be internally valid but indirect for target question due different population, intervention, outcome or context.

Synthesis should separate validity from applicability.

## 32. Mechanism synthesis

When effects vary, ask which mechanisms/boundary conditions explain variation.

This connects systematic review to theory rather than ending at pooled number.

## 33. Contradictory studies

Do not vote-count “5 positive vs 3 negative”.

Compare estimands, power, designs, contexts and measurement. Apparent contradiction may be different questions.

## 34. Null results

Null/non-significant studies contribute information if precision adequate.

Do not treat non-significance as evidence of exact zero.

## 35. Citation quality

Review should cite primary evidence for empirical claims where possible, not only secondary summaries.

Check whether cited study actually supports exact claim/population/time.

## 36. Automation and AI assistance

Tools can deduplicate, screen candidates or extract fields, but researcher must validate inclusion and interpretation.

Automated summarization can hallucinate study details; retain source-level audit trail.

## 37. Reproducible review package

Store search strings, dates, databases, deduplication rules, screening decisions, extraction sheet and synthesis code.

Search date matters because literature changes.

## 38. Failure modes

Sai lầm thứ nhất là call prose bibliography a systematic review.

Sai lầm thứ hai là pool incomparable estimands because they share topic label.

Sai lầm thứ ba là use I² as explanation of heterogeneity.

Sai lầm thứ tư là vote-count significance.

Sai lầm thứ năm là equate publication count with evidence certainty.

## 39. Review checklist

1. review question rõ không?
2. protocol/search sources đủ không?
3. screening criteria pre-specified không?
4. study designs/estimands comparable không?
5. risk-of-bias assessed by threats nào?
6. heterogeneity substantive ở đâu?
7. publication/selective-reporting risk nào?
8. pooled effect có meaningful không?
9. prediction/directness/external validity ra sao?
10. all decisions/search/code reproducible không?

Evidence synthesis giúp biết “literature collectively nói gì”. Chapter cuối cần đảm bảo toàn research process — quantitative lẫn qualitative — có ethics, reproducibility, mixed-method integration và transparent reporting.
