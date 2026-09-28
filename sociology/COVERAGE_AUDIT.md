# Sociology — Coverage Audit

## Kết luận hiện tại

Sociology đã có core canonical route từ sociological reasoning và social structure đến culture/identity, groups/networks/organizations, stratification, social institutions và population/social change. Domain này được xem là **core complete ở foundation level**; advanced subfields chỉ nên mở khi tạo learning value riêng thay vì chia nhỏ lại nội dung đã có.

## Coverage matrix

| Module | Trạng thái | Coverage |
|---|---|---|
| 00 Sociological Imagination, Theory & Social Structure | Core complete | agency/structure, norms/roles/status, institutions, macro–meso–micro levels, major theoretical lenses, networks/fields, emergence, feedback |
| 01 Culture, Socialization, Identity & Deviance | Core complete | culture, socialization, identity, stigma/boundaries, norm enforcement, deviance, labeling/social control, diffusion và homophily |
| 02 Groups, Networks, Organizations & Bureaucracy | Core complete | group dynamics, network positions, strong/weak ties, brokerage/closure, collective action, organizations, bureaucracy, routines, legitimacy, professions, power |
| 03 Stratification, Class, Status & Social Mobility | Core complete | income/wealth/class/status/power, mobility, cumulative advantage, social reproduction, closure, spatial inequality, gender/race/ethnicity, poverty/social exclusion |
| 04 Social Institutions | Core complete | family, education, work, religion, media, civic life, law/health institutions, formal-vs-practice, institutional interdependence |
| 05 Population, Urbanization, Collective Behavior & Social Change | Core complete | demography, migration, urbanization, segregation/gentrification, collective behavior/movements, globalization, modernization/dependency, path dependence, environmental sociology |

## Domain boundaries

### Psychology

Psychology giữ individual cognition/emotion/personality/learning mechanisms. Sociology giữ relational positions, norms, networks, organizations, status và institutions. Không duplicate general psychology under a social label.

### Economics

Economics giữ market/incentive/allocation/welfare analysis và causal econometrics. Sociology giữ status, networks, norms, social closure, organizations, social reproduction và institutional meaning/power. Labor, inequality, organizations và education are bridge areas.

### Research Methods

Generic sampling, surveys, qualitative coding, mixed methods, systematic reviews, ethics và reproducibility belong to `research_methods/`. Sociology uses those tools but should not own duplicate methodology chapters.

### History / Geography / Korean Culture

History owns chronology and actors; Geography owns spatial/environmental systems; Korean Culture owns Korea-specific social/cultural detail. Sociology provides reusable mechanisms and comparative categories.

## Evidence discipline

Keep these distinctions explicit:

```text
Peer similarity ≠ peer influence
Persistence ≠ social reproduction mechanism
Group difference ≠ discrimination by itself
Formal policy ≠ implementation
Correlation between place and outcome ≠ neighborhood effect
Cultural label ≠ explanatory mechanism
```

A sociological explanation should specify social positions, relations, transmission/enforcement and plausible alternative mechanisms.

## Advanced expansion gate

Only add another Sociology module when at least one condition holds:

1. it introduces distinct mechanisms not teachable cleanly inside the core;
2. another domain depends directly on it;
3. the topic requires a separate long learning path rather than more examples;
4. it can include evidence boundaries/failure modes rather than a glossary.

Potential future modules: political sociology, sociology of science/knowledge, sociology of technology, medical sociology, environmental sociology, economic sociology, social network analysis advanced. These are **not current gaps** because their foundations already appear in core chapters or neighboring domains.

## Repo-wide next gate

Sociology should not immediately expand further. After integration, run a fresh repository-wide audit from `main` and prioritize whichever canonical domains still have structural/depth gaps. Earlier audit candidates such as Frontend structure must be re-verified because parallel work may already have fixed them.
