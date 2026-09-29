# Korea Law, Civic & Everyday Life — Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `korea_law_civic_life/`  
**Entrypoint:** [`README.md`](./README.md)  
**Source-policy owner:** [`00_reading_method_and_source_policy.md`](./00_reading_method_and_source_policy.md)

## 1. Canonical ownership

This domain owns practical understanding of Korean law, public administration and everyday civic procedures for a reader who needs to understand the system, identify the competent authority, locate official current rules and interpret common administrative documents.

It is not a substitute for individualized legal advice and it should not turn into political advocacy.

Adjacent owners:

- exam-oriented Korean society/KIIP material → [`../korean_culture/kiip/`](../korean_culture/kiip/README.md);
- Korean history → [`../korean_history/`](../korean_history/README.md);
- Korean society/culture → [`../korean_culture/`](../korean_culture/README.md);
- Korean economy/business institutions → [`../korea_business_economy_knowledge_library/`](../korea_business_economy_knowledge_library/README.md);
- general economics → [`../economics/`](../economics/README.md).

## 2. Coverage currently strong

The current route is coherent and practical:

```text
source-reading method
→ constitution/legal hierarchy/state structure
→ legislature/executive/judiciary/local government
→ administrative law and petitions/disputes
→ civil law/contracts/consumer rights
→ labor
→ housing
→ tax/social insurance/welfare/healthcare
→ banking/credit/financial consumer protection
→ immigration/visa/permanent residence/naturalization
→ official portals/self-research
→ Korean administrative documents
→ life scenarios/checklists
```

Particularly strong is the explicit source hierarchy:

```text
real problem
→ legal field
→ competent authority
→ current law/regulation
→ current procedural guidance
→ forms/documents
→ deadlines/submission channel
→ result/appeal or objection route
```

This is the right long-term model because law and procedures change more quickly than foundational explanations.

## 3. Source-of-truth contract

For claims that can affect rights, obligations, residence status, money, deadlines or legal procedure, future updates should distinguish at least four layers:

1. **law/regulation currently in force**;
2. **official implementation guidance from the competent authority**;
3. **official explanatory material/portal guidance**;
4. **non-official explanatory/community material**.

A lower layer can help interpretation or discovery but should not silently replace a higher-authority source.

For time-sensitive material, a chapter should record or make recoverable:

- source/authority;
- relevant rule or page;
- effective date or version where applicable;
- date checked;
- known conditions/exceptions;
- what the reader still needs to verify for an individual case.

## 4. Dynamic-data boundary

The following should be treated as dynamic data rather than timeless knowledge:

- contribution rates;
- minimum-wage figures;
- monetary thresholds and penalties;
- visa/residence eligibility criteria;
- forms and required-document lists;
- filing/reporting deadlines;
- online/offline submission routes;
- agency names or electronic systems;
- welfare/support thresholds;
- procedural details that agencies may revise.

The durable content should explain mechanism, authority and verification workflow. Numerical/procedural snapshots need explicit review dates.

## 5. Neutral civic/political boundary

Coverage of the President, National Assembly, Government, courts, local government, elections or civic rights should remain descriptive:

```text
institution
→ legal basis
→ composition/selection mechanism
→ powers and limits
→ relationship with other institutions
→ procedure
→ official source
```

Do not rank parties, candidates, ideologies or political choices. Contested interpretations should be attributed rather than adopted as the library's own conclusion.

## 6. Important boundaries to preserve

### Legal rule vs administrative practice

A ministry/agency FAQ can explain practice but should not be written as though it were itself the statute. When the distinction matters, state both the legal basis and the operational guidance.

### General rule vs individual case

A rule may depend on employment type, workplace size, visa category, date, contract, household status, income, location or other facts. The library should explain the decision tree without pretending the general chapter resolves every personal case.

### KIIP exam knowledge vs real-life legal research

KIIP may compress facts for exam recall. This domain should retain more context, source hierarchy, exceptions and research workflow. Do not copy exam simplifications into a practical legal chapter without qualification.

### Civic structure vs political evaluation

Institutional powers, terms, procedures and checks/balances can be explained directly. Political performance or desirability judgments are outside the canonical scope.

## 7. Gaps / next depth

### P1 — Freshness metadata at chapter level

Introduce a lightweight convention for time-sensitive chapters, for example:

```yaml
last_source_reviewed: YYYY-MM-DD
primary_authorities:
  - ...
time_sensitive: true
```

This should not become heavy bureaucracy for stable conceptual chapters, but it is valuable for labor, tax, insurance, immigration, housing and procedural material.

### P1 — Change-impact checklist

When a law or procedure changes, reviewers should identify affected downstream chapters rather than update one number in isolation:

```text
rule changed
→ eligibility/rights
→ authority/procedure
→ form/document
→ deadline
→ examples/checklists
→ glossary/internal links
```

### P1 — Rights / procedure / evidence model

Strengthen practical chapters around three distinct questions:

```text
What right/obligation exists?
→ What procedure enforces or exercises it?
→ What evidence/documents prove the relevant facts?
```

This is especially useful for labor, housing, consumer and administrative disputes.

### P1 — Administrative decision and challenge route

Create a clearer cross-chapter route for:

```text
application/request
→ administrative disposition/notice
→ reason and deadline
→ correction/reconsideration where available
→ administrative appeal/litigation path
→ evidence preservation
```

The route should remain general and link to official current procedure rather than promise a universal remedy.

### P2 — Foreign-resident life-event routes

Compose existing chapters into practical routes such as:

- starting/changing a job;
- moving house and protecting a deposit;
- changing visa/residence status;
- tax year/insurance transitions;
- consumer/financial dispute;
- receiving an administrative notice.

These should be decision maps, not new duplicate legal domains.

### P2 — Bilingual document interpretation patterns

Expand recurring Korean administrative/legal language by function:

- obligation/prohibition;
- eligibility;
- exception;
- deadline;
- evidence/document request;
- disposition/result;
- appeal/objection.

This is more reusable than memorizing isolated vocabulary.

### P2 — Provenance register for highly dynamic claims

For numerical thresholds, contribution rates, visa conditions and procedure pages, consider a compact source register so stale claims can be found and revalidated systematically.

## 8. Review protocol

For a substantial change:

```text
identify claim type
→ identify competent authority
→ locate current primary/official source
→ check effective date/version
→ separate rule from guidance
→ enumerate conditions/exceptions
→ update practical workflow/checklist
→ record review date
→ verify internal links
```

For civic/political chapters, add a neutrality pass before merge.

## 9. Current assessment

**Domain structure: strong.**  
**Official-source policy: strong.**  
**Practical life coverage: broad and coherent.**  
**Exam-vs-real-life boundary: clear.**  
**Time-sensitive data governance: conceptually strong, but metadata can be more systematic.**  
**Cross-chapter change propagation: needs a clearer protocol.**  
**Rights/procedure/evidence integration: can be strengthened.**

The next improvement should be freshness/change governance and cross-chapter life-event routes, not more isolated legal-topic files.