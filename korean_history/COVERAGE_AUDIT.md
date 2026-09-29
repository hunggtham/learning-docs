# Korean History — Coverage Audit

**Audit date:** 2026-09-29  
**Canonical root:** `korean_history/`  
**Entrypoint:** [`README.md`](./README.md)

## 1. Canonical ownership

`korean_history/` owns the historical development of the Korean peninsula and the Republic of Korea as a causal, chronological and comparative knowledge system.

It should explain not only what happened, but how political authority, land, taxation, labor, military organization, technology, trade, demography, institutions, ideas and geography interacted across periods.

Adjacent owners:

- contemporary Korean society/culture → [`../korean_culture/`](../korean_culture/README.md);
- Korean law/civic institutions and current procedures → [`../korea_law_civic_life/`](../korea_law_civic_life/README.md);
- Korean economy/business mechanisms and company cases → [`../korea_business_economy_knowledge_library/`](../korea_business_economy_knowledge_library/README.md);
- world chronology/comparative context → [`../world_history/`](../world_history/README.md);
- KIIP exam recall → [`../korean_culture/kiip/`](../korean_culture/kiip/README.md).

## 2. Coverage currently strong

The library has a continuous chronological spine from prehistory and early states through the Three Kingdoms, Goryeo, Joseon, the modern transition, colonial period, liberation/division, war, industrialization, democratization and contemporary Korea.

It also contains transversal companion layers for:

- social history;
- economic history;
- knowledge/information history;
- public memory;
- Korea–Vietnam parallel chronology/context;
- historical places and field observation;
- economy/society/everyday life by period;
- geography/routes/historical space;
- chronology and glossary;
- naming/translation conventions.

This is a strong architecture because chronology remains canonical while thematic companions prevent history from becoming a list of events.

## 3. Historical reasoning contract

A substantial chapter should answer, where relevant:

```text
starting conditions
→ institutions/power structure
→ resource and fiscal base
→ production/trade/technology
→ social groups and incentives
→ external/regional context
→ shock/conflict/change mechanism
→ new equilibrium/order
→ persistence/path dependence
→ material traces and present-day legacy
```

Chronology is necessary but not sufficient.

## 4. Evidence and interpretation boundary

Historical writing should distinguish:

1. relatively well-established chronology/facts;
2. interpretation supported by historical scholarship;
3. contested interpretation;
4. collective/public memory;
5. national narrative;
6. later political use of the past.

Do not collapse these categories into one voice.

When an issue is contested, preserve the strongest factual baseline first, then identify major interpretations and what evidence each relies on. Avoid presenting one later national narrative as though it were the only historical description.

## 5. Korea–Vietnam comparison boundary

The parallel timeline is useful for temporal orientation, but comparison should remain analytic rather than superficial.

A valid comparison asks:

```text
same period?
→ similar or different state capacity?
→ land/tax/labor regime?
→ trade and regional system?
→ technology/military environment?
→ demographic/geographic constraints?
→ similar outcome for same mechanism, or not?
```

Do not infer equivalence merely because two dynasties, wars or reforms occurred in the same century.

## 6. Historical-place boundary

Places and monuments are evidence, not decoration. When linking a site to a period, distinguish:

- original historical function;
- later rebuilding/restoration;
- archaeological/material evidence;
- memorial interpretation;
- present-day tourism/heritage framing.

A current monument may represent several historical layers rather than a preserved snapshot of one era.

## 7. Gaps / next depth

### P1 — Explicit source/provenance map by period

The README already defines a strong baseline source set. The next step is to make period-level provenance easier to audit:

```text
chapter/period
→ primary or near-primary evidence where relevant
→ institutional reference source
→ modern scholarship/interpretive source
→ contested questions
```

This does not require citation overload; the goal is traceability for claims most likely to be disputed or revised.

### P1 — State capacity / fiscal-military comparison route

Create a cross-period route following:

```text
land/household registration
→ taxation
→ military mobilization
→ bureaucracy/record keeping
→ transport/logistics
→ state capacity
→ crisis response
```

This would connect many existing chapters without duplicating chronology.

### P1 — Household/everyday-life continuity route

Strengthen continuity across periods for:

- household structure;
- gender/family roles;
- landholding/tenancy;
- labor obligations;
- food/energy/material life;
- literacy/education;
- urban/rural differences.

The goal is to make institutional change visible in ordinary life.

### P2 — Historical data uncertainty

Add clearer handling of uncertain population, production, fiscal or casualty estimates:

```text
estimate
→ source base
→ measurement problem
→ plausible range
→ what conclusion survives the uncertainty
```

### P2 — Public-memory and heritage update protocol

For museums, memorial sites, heritage designations and interpretation panels, distinguish durable historical claims from current institutional framing. Current exhibition text should not silently become canonical historical truth.

### P2 — Modern-period current-boundary rule

The closer a chapter approaches the present, the more carefully it should separate completed historical analysis from ongoing political/current-affairs evaluation. Current political actors, parties and unresolved events should be described factually and sourced rather than ranked or judged.

## 8. Naming and language governance

The existing Vietnamese–Korean–English naming convention is a strong asset. Preserve:

```text
Vietnamese readable name
+ Korean original
+ English/Romanization when useful
```

Do not force Sino-Vietnamese forms where they make a modern person/place harder to recognize. File paths should remain stable and practical for links/Git.

## 9. Review protocol

For substantial changes:

```text
chronological placement
→ causal mechanism
→ institutional/economic/social context
→ regional context
→ evidence/provenance
→ contested interpretation check
→ Korea–Vietnam comparison check if present
→ naming convention
→ internal links
```

For modern political history, add a neutrality/source pass before merge.

## 10. Current assessment

**Chronological coverage: strong.**  
**Economic/social contextualization: strong.**  
**Places/material-history integration: strong.**  
**Korea–Vietnam contextual comparison: strong architecture.**  
**Evidence-vs-interpretation distinction: explicitly present and should be maintained.**  
**Period-level provenance visibility: can be stronger.**  
**Cross-period state-capacity and household routes: high-value next work.**

The next depth pass should connect existing chapters through mechanisms and evidence rather than add another parallel chronology.