# Thuế doanh nghiệp, regulation và chính sách cạnh tranh tại Hàn Quốc (Tax & Regulation / 법인세·규제·공정거래)

Doanh nghiệp không vận hành chỉ bằng contract giữa private parties. Nhà nước xác định **tax base, disclosure duties, competition rules, labor floors, environmental constraints, licensing requirements và giới hạn đối với ownership/market conduct**.

Vì vậy regulation không phải appendix pháp lý nằm ngoài business model. Trong nhiều ngành — finance, telecom, energy, healthcare, platform, defense — regulation trực tiếp quyết định revenue, cost, entry barrier và capital requirement.

> Mental model: policy/regulation là một **economic variable** giống interest rate, FX hay raw-material price. Nó thay payoff của business decisions.

## Corporate income tax: taxable income không phải revenue

Corporate Income Tax (법인세) đánh trên **taxable income / 과세표준**, không phải đơn giản trên revenue hay accounting operating profit.

Accounting profit và taxable income có thể khác vì:

- depreciation rules;
- tax credits;
- loss carryforwards;
- non-deductible expenses;
- foreign income/tax;
- timing differences;
- tax incentives.

A simplified bridge:

```text
Accounting profit before tax
± permanent differences
± timing/tax adjustments
= taxable income
```

Therefore analyst should not multiply financial-statement profit by headline statutory rate and expect exact tax expense.

## 2026 corporate tax brackets

For fiscal years beginning on or after 1 January 2026, Korea’s National Tax Service lists the basic corporate income-tax rates for ordinary for-profit corporations as:

| Taxable income | Basic rate |
|---|---:|
| up to 200 million KRW | 10% |
| over 200 million to 20 billion KRW | 20% |
| over 20 billion to 300 billion KRW | 22% |
| over 300 billion KRW | 25% |

These are statutory brackets. Actual tax expense/cash tax can differ materially.

Current legal details should always be checked with NTS or professional tax advice before transaction decisions.

## Statutory rate, effective rate và cash tax khác nhau

Three concepts:

**Statutory tax rate** — rate under tax law.

**Effective Tax Rate (ETR)**:

\[
ETR \approx \frac{Income\ Tax\ Expense}{Pre-tax\ Accounting\ Income}
\]

**Cash tax** — actual tax cash paid in period.

One-time tax credit can lower ETR; deferred tax can move expense across periods; tax-loss carryforward can reduce current cash tax.

Therefore one low-tax year does not prove structural tax advantage.

## Deferred tax: timing creates accounting asset/liability

Accounting and tax rules may recognize revenue/expense at different times.

This creates **deferred tax asset/liability / 이연법인세자산·부채**.

Example: accounting depreciation and tax depreciation differ. Total lifetime tax may be similar, but timing differs.

Deferred tax asset is valuable only if company is likely to generate taxable income to use it. Large DTA in persistently loss-making firm deserves scrutiny.

## Tax losses: economic value depends on future profit

Past losses can sometimes reduce future taxable income under rules.

But tax-loss carryforward is not cash today. Its value depends on:

- future taxable profits;
- expiry/usage restrictions;
- ownership/restructuring rules;
- jurisdiction.

This is similar to financial option: useful only if future profit exists.

## Tax credit and investment incentive

Government may encourage R&D or strategic CAPEX through tax credits/deductions.

Economically, investment credit changes project NPV:

\[
NPV = PV(After-tax\ Cash\ Flows) - Effective\ Initial\ Cost
\]

Tax credit can lower effective cost and move marginal project from negative to positive NPV.

This is why semiconductor/battery investment policy affects real corporate capital allocation.

But subsidy/tax credit does not guarantee positive ROIC. Bad project can remain bad even after support.

## VAT: transaction tax is different from profit tax

Value Added Tax (VAT / 부가가치세) is consumption/transaction-layer tax.

Business generally collects output VAT and claims eligible input VAT under rules.

VAT collected on behalf of government should not be confused with economic revenue.

When comparing customer invoice amount with company sales, understand whether VAT is included/excluded.

## Tax incidence: legal payer and economic bearer can differ

Suppose tax is legally imposed on company. Economic burden can still be shared through:

- higher prices;
- lower wages;
- lower supplier prices;
- lower shareholder returns.

Who ultimately bears burden depends on elasticity and market power.

This is **tax incidence / 조세귀착**.

Therefore policy analysis should ask not only “who remits tax?” but “who can pass cost onward?”

## International tax and transfer pricing

Multinational groups transact across affiliates for components, services, royalties, financing and IP.

**Transfer pricing / 이전가격** determines intra-group price and allocation of taxable profit.

Tax authorities apply arm’s-length principles and related rules to prevent artificial profit shifting.

For analyst, local subsidiary margin can reflect global functional allocation, not only local operational quality.

See [23_foreign_invested_companies_and_korea_entry](./23_foreign_invested_companies_and_korea_entry.md).

## Regulation as business architecture

Some industries cannot operate freely without licenses/permissions.

Examples:

- bank license;
- insurance rules;
- telecom spectrum;
- pharmaceutical approval;
- medical-device approval;
- environmental permits;
- defense export approval;
- electricity-market rules.

This creates two opposite effects.

### Regulation as cost

Compliance requires lawyers, systems, reporting, capital and audits.

### Regulation as moat

Once incumbent has license, compliance infrastructure and track record, new entrant must bear same fixed cost.

Thus regulation can simultaneously protect customers **and** raise entry barrier.

## Fixed compliance cost and firm size

Suppose regulation requires 5 billion KRW annual compliance system.

For company with 5 trillion revenue, cost is 0.1%.

For startup with 50 billion revenue, cost is 10%.

Same rule can therefore favor scale.

This is why “more regulation = less market power” is not always true.

Policy design must consider fixed-cost effects.

## KFTC and competition policy

Korea Fair Trade Commission (공정거래위원회) covers competition, large business groups, unfair transactions, consumer issues and related areas.

For chaebol analysis, KFTC is important because regulator often looks beyond one corporation to **economic control group / 기업집단**.

Large-group designation frameworks impose different disclosure/restriction obligations depending on statutory criteria. Thresholds and designations can change, so use current KFTC data for live analysis.

## Competition policy: company size itself is not violation

Large market share can arise from innovation, efficiency or network effects.

Competition problem appears when market power is used in ways that reduce contestability or harm trading partners/consumers under law.

Key concepts include:

- cartel/collusion;
- abuse of dominance/market power;
- exclusionary conduct;
- unfair trade practices;
- anti-competitive merger;
- unfair subcontracting.

Do not replace legal/economic analysis with “big = bad”.

## Relevant market definition

Market share has meaning only after defining **relevant market / 관련시장**.

Need ask:

- Which products are substitutes?
- Geographic scope?
- Can customers switch after price increase?
- Are platforms multi-sided?
- Are switching costs high?

A company can have 80% share of narrow category but face strong substitute from adjacent technology.

Market definition often determines competition conclusion.

## Concentration metrics: useful but incomplete

Industry concentration can be approximated by top-firm shares or HHI-type measures.

But static share does not capture:

- entry barriers;
- innovation rate;
- switching costs;
- potential competition;
- buyer power.

High concentration in semiconductor equipment with huge R&D barriers differs economically from temporary concentration in fashion trend.

## Merger control: shareholder synergy vs social competition

Company may propose M&A because synergy lowers cost or expands market.

Regulator asks different question: does transaction materially reduce competition?

These objectives can diverge.

A merger can create shareholder value while harming competition, or improve efficiency without meaningful harm.

Merger analysis therefore needs:

- market definition;
- concentration;
- entry barriers;
- efficiencies;
- buyer power;
- innovation effect.

## Chaebol regulation: group-level risks

Large business groups can create economic benefits through scale, internal capital and R&D.

But group structure can also create:

- cross-shareholding/control leverage;
- related-party favoritism;
- unfair internal support;
- supplier dependency;
- concentration of economic power.

Korea therefore has group-specific disclosure and competition framework beyond normal company law.

See [04_chaebol_and_large_business_groups](./04_chaebol_and_large_business_groups.md).

## Subcontracting regulation: buyer power in supply chains

A large buyer can influence supplier through:

- payment terms;
- price reduction;
- design/technology information;
- unilateral specification changes;
- delayed acceptance;
- volume concentration.

Fair-subcontracting rules attempt to limit abuse, but legal protection does not eliminate economic dependency.

Supplier still needs customer diversification and working-capital strength.

See [06_sme_mid_sized_and_subcontracting_ecosystem](./06_sme_mid_sized_and_subcontracting_ecosystem.md).

## Platform competition: zero-price service breaks simple antitrust intuition

Many digital platforms charge user zero or low price while monetizing advertising, sellers or financial services.

Traditional “price increased?” test is insufficient.

Need inspect:

- network effects;
- data advantage;
- multi-homing;
- self-preferencing;
- tying/bundling;
- seller dependency;
- interoperability;
- switching costs.

Platform is multi-sided market, so intervention on one side can change another side.

## Financial regulation: capital requirement changes business model

Bank cannot maximize leverage like ordinary industrial firm because regulation requires capital/liquidity buffers.

Higher capital requirement can reduce ROE but increase resilience.

Thus regulation changes both return and risk.

Comparing bank ROE to software ROE without regulatory context is meaningless.

## Healthcare regulation: permission is part of product

Drug or medical device cannot monetize solely because technology works; it must pass regulatory approval and often reimbursement processes.

Regulatory capability becomes intangible asset.

This is why bio company value chain is:

```text
Science → Clinical evidence → Approval → Reimbursement → Commercial adoption
```

Regulation is embedded in product-market fit.

## Environmental regulation and transition cost

Steel, chemicals, energy and transport face emission rules, permits and carbon constraints.

Policy can create cost today but also market for cleaner technology.

Incumbent with old asset base may face stranded-asset risk; new technology firm may gain demand.

Regulation therefore reallocates value across sectors.

## Policy uncertainty and real options

If company plans irreversible 10-trillion-KRW plant but subsidy/tariff rule may change soon, waiting can have value.

This is real-option logic.

Uncertainty can cause:

- delayed CAPEX;
- higher hurdle rate;
- more cash retention;
- phased investment;
- geographic diversification.

Therefore policy announcement affects investment before rule becomes effective.

## Compliance as software/infrastructure problem

Modern regulation increasingly requires systems: transaction monitoring, audit logs, privacy controls, accounting data, cybersecurity and reporting.

Compliance cost is therefore not only legal staff; it becomes enterprise-IT architecture.

For Korean SI/SM companies, regulation itself generates demand for system projects.

This connects law directly to [34_digital_fintech_cloud_and_it_services](./34_digital_fintech_cloud_and_it_services.md).

## How to analyze regulatory exposure of a Korean company

Create a regulation map:

| Layer | Questions |
|---|---|
| Tax | statutory/effective/cash tax? credits? |
| Market entry | license/permit/certification required? |
| Pricing | free price or regulated tariff/reimbursement? |
| Competition | dominant position, merger, group restrictions? |
| Labor | overtime/employment obligations? |
| Environment | emissions/permit/carbon exposure? |
| Data/security | privacy, financial/security standards? |
| Trade | tariff, origin, export controls? |

Then identify which rule directly changes cash flow.

## Mental Model

> Tax and regulation define the **feasible strategy space** of a company. A business model is not just product + customer; it is product + customer + law + tax + licenses + competition structure. If profit depends on a rule, that rule belongs inside valuation and risk model.

## Common misconceptions

Statutory tax rate ≠ effective tax rate ≠ cash tax.

Regulation is not always negative for incumbent; it can create moat.

Large company is not automatically anti-competitive.

High market share alone does not prove dominance abuse.

Government support does not erase project economics.

A policy announcement is not realized cash flow until eligibility, amount and timing are clear.

## Connections

Read [04_chaebol_and_large_business_groups](./04_chaebol_and_large_business_groups.md) for group regulation, [08_corporate_governance_ownership_and_control](./08_corporate_governance_ownership_and_control.md) for internal power, [23_foreign_invested_companies_and_korea_entry](./23_foreign_invested_companies_and_korea_entry.md) for cross-border tax and [26_economic_institutions_and_policy_making](./26_economic_institutions_and_policy_making.md) for policy formation.

### Nguồn hiện hành

- National Tax Service, corporate-tax rates: https://nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7746&mi=2372
- Korea Fair Trade Commission, large business group policy: https://www.ftc.go.kr/www/contents.do?key=696
