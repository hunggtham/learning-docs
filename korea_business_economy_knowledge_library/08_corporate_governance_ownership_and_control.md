# Corporate governance, ownership và control tại doanh nghiệp Hàn Quốc (Corporate Governance / 기업지배구조·소유·지배)

Corporate governance (Quản trị công ty / 기업지배구조) tồn tại vì **người cung cấp vốn, người có quyền kiểm soát và người điều hành không phải lúc nào cũng là cùng một người**. Khi quyền quyết định tách khỏi quyền hưởng lợi kinh tế, incentive có thể lệch nhau. Governance là tập hợp các cơ chế nhằm trả lời: ai có quyền quyết định, ai giám sát, ai hưởng upside, ai chịu downside và ai có thể challenge một quyết định gây xung đột lợi ích.

Trong Korea, governance phải được đọc ở cả **company level** và **business-group level**. Đây là điểm quan trọng nhất để tránh áp nguyên textbook US vào chaebol một cách máy móc.

## Hai loại agency problem cần phân biệt

Textbook corporate finance thường bắt đầu với **Type I agency problem**: dispersed shareholders (principal) thuê managers (agent), nhưng manager có thể ưu tiên compensation, empire building, perks hoặc job security hơn shareholder return.

Trong family-controlled business group, còn một dạng rất quan trọng: **Type II agency problem** giữa controlling shareholder (지배주주) và minority shareholders (소수주주).

Controlling shareholder có thể có incentive tối ưu lợi ích của family hoặc toàn group, trong khi minority investor chỉ sở hữu một specific legal entity.

Ví dụ, transaction có thể tốt cho Group A tổng thể nhưng làm Company B listed chịu cost disproportionate. Đây là reason analyst phải luôn tách **group interest** và **entity-level shareholder interest**.

## Ownership khác control

Ownership (소유) trả lời ai có economic claim; control (지배) trả lời ai thực sự có power over strategic decisions.

Hai thứ thường liên quan nhưng không identical.

Nếu Family owns 30% Company A, A owns 40% B, and B owns 50% C, indirect economic exposure của family tới C qua một path xấp xỉ:

\[
0.30 \times 0.40 \times 0.50 = 6\%
\]

Nhưng control influence có thể lớn hơn 6% nếu each intermediate stake đủ để control next entity và remaining shareholders are dispersed.

Đây là **control leverage / 지배력 레버리지**.

Control leverage không tự động xấu. Nó cho phép group coordinate capital với less direct ownership. Risk xuất hiện khi controller hưởng private benefit while downside shared with minority holders.

## Ownership graph: cách đọc group đúng hơn shareholder table

Top-shareholder table của one company không đủ cho chaebol analysis.

Need map:

```text
Controlling person / family
          ↓
       Company A
       ↙      ↘
  Company B   Company C
      ↓          ↓
  Subsidiary D  Affiliate E
```

Mỗi edge cần ghi:

- stake percentage;
- voting rights;
- whether entity consolidates another;
- related-party relationships;
- material guarantees/loans.

Graph reveals where control travels and where economic exposure differs.

This is why [05_group_structure_affiliates_holding_companies](./05_group_structure_affiliates_holding_companies.md) is a direct dependency.

## Board of Directors: governance không chỉ là số outside directors

Board of Directors (이사회) approves major strategic and financial decisions and oversees management according to law/articles.

**Outside directors / 사외이사** are designed to bring independent oversight, but independence has both **form** and **substance**.

A board may formally satisfy independence requirement yet remain weak if directors lack industry knowledge, information access or willingness to challenge management.

Useful questions include:

- Who nominated directors?
- What expertise do they have?
- How long have they served?
- Attendance rate?
- Committee membership?
- Any dissenting votes?
- Do they have ties to controlling shareholders or management?

Board quality cannot be inferred from title alone.

## Representative director, CEO và actual power

`대표이사` is statutory representative director. CEO in English title may or may not map perfectly to legal representative status.

A chairman, vice chairman, CEO and representative director can hold different formal/informal influence.

Therefore governance analysis should combine:

1. statutory roles;
2. board seats;
3. ownership/control;
4. actual strategic influence.

Formal org chart is not always full power map.

## Audit Committee and internal control

Financial reporting has severe information asymmetry, so audit committee, external auditor and internal-control system are core governance mechanisms.

Audit opinion does not guarantee company is economically strong, but weak internal controls or serious audit issues can reveal reporting/governance risk.

Governance therefore connects directly to [09_disclosure_accounting_dart_kind](./09_disclosure_accounting_dart_kind.md).

## Related-party transactions: không phải cứ nội bộ là xấu

Business group naturally has internal transactions: IT affiliate, logistics affiliate, property lease, loans, guarantees, procurement and services.

Related-party transaction can be efficient if it reduces transaction cost or uses specialized group capability.

Problem arises when terms differ materially from arm’s-length economics and transfer value toward controller or favored entity.

Key questions:

- Is transaction necessary?
- Could market alternative be cheaper/better?
- Is pricing arm’s length?
- Was approval independent?
- Is disclosure sufficient?
- Who gains and who bears risk?

## Tunneling: mechanism, not label

**Tunneling / 터널링** means transferring value away from an entity toward controlling interests through mechanisms such as unfavorable asset sale, preferential contract, opportunity diversion or financing.

Do not diagnose tunneling simply because two affiliates transact.

Need evidence of value transfer.

A rigorous analysis compares transaction terms with market alternatives and traces beneficiary.

## Business opportunity diversion

A subtle governance risk occurs when valuable opportunity could belong to Company A but is routed to private/affiliate Company B under same controller.

Even without cash leaving A directly, shareholder value may be diverted.

This is why corporate opportunity rules and related-party disclosure matter in family groups.

## Capital allocation: governance becomes visible in numbers

Governance is not only scandals and board composition. The most persistent governance outcome is **capital allocation / 자본배분**.

Operating cash can go to:

```text
Maintenance CAPEX
Growth CAPEX
R&D
M&A
Debt repayment
Dividend
Buyback / cancellation
Cash accumulation
Affiliate investment
```

Management creates value if retained capital earns returns above opportunity cost.

A core metric:

\[
ROIC = \frac{NOPAT}{Invested\ Capital}
\]

If company continually reinvests at ROIC below cost of capital, accounting assets grow while economic value can shrink.

Board quality eventually shows up in these choices.

## Cash-rich company can still have governance problem

Large cash balance is not automatically shareholder-friendly.

Need ask:

- Why is cash held?
- Is it operating buffer or idle capital?
- Is cash trapped in subsidiaries?
- Is management planning low-return acquisition?
- Is shareholder return policy rational?

Governance analysis therefore connects cash balance to future allocation, not just liquidity safety.

## Dividend and buyback: return capital, but mechanism matters

Dividend is direct cash transfer to shareholders. Buyback reduces public float or creates treasury shares.

Economic effect depends on whether shares are cancelled, held, reused for compensation or used in corporate transactions.

If company buys stock below intrinsic value and cancels it, remaining shareholders can benefit. If buyback simply accumulates treasury shares indefinitely, effect differs.

Do not label every buyback “shareholder return” without reading purpose and treatment.

## Treasury shares (자기주식)

Treasury shares are company’s repurchased shares. Governance implications can involve voting/control, restructuring and future disposition depending on legal treatment.

Analyst should check:

- amount repurchased;
- cancellation plan;
- disposal recipients;
- compensation use;
- M&A/restructuring use;
- disclosure changes.

This is especially relevant in Korea because treasury-share policy has been an area of capital-market reform attention.

## Succession: governance, tax and capital markets collide

Family succession can trigger:

- inheritance/gift tax planning;
- stake transfer;
- mergers;
- spin-offs;
- holding-company reorganization;
- affiliate stake sales;
- dividend policy changes.

Succession is not merely family event. It can alter ownership graph and distribution of economic value among listed entities.

When restructuring is announced, analyst should draw **before/after ownership graph** and ask:

1. Does controller voting power change?
2. Does economic ownership change?
3. Which listed entity gives/receives assets?
4. What valuation/exchange ratio is used?
5. Are minority shareholders treated symmetrically?

## Spin-offs: 인적분할 và 물적분할

`인적분할` generally separates a company such that existing shareholders receive proportional ownership in separated entity according to structure.

`물적분할` generally creates a subsidiary retained under parent ownership.

The governance consequence can differ substantially if growth business is moved into subsidiary and later raises outside capital or lists separately.

Therefore spin-off analysis should not stop at “focus strategy”; ask **who owns the future growth asset after transaction?**

## Mergers and exchange ratios

A merger can have valid industrial logic but still redistribute value depending on valuation ratio.

Suppose A shareholders receive too few shares in combined entity relative to A’s fair value; synergy may exist yet minority holders of A still lose relative value.

Governance analysis therefore separates:

- strategic rationale;
- valuation/fairness;
- control consequence.

These are three different questions.

## Institutional investors and stewardship

Pension funds, asset managers and foreign institutions can influence governance through voting and engagement.

Institutional ownership increases potential monitoring, but passive holding does not automatically mean active governance.

Need observe actual voting, engagement policies and concentration of ownership.

## Activism: governance pressure as capital-market mechanism

Shareholder activists may demand dividends, buybacks, board changes, asset sales or governance reform.

Activism can improve capital discipline but not every activist proposal is automatically value-maximizing. Short horizon and long-term investment needs can conflict.

Evaluate proposal by economics, not by identity of proposer.

## Governance and “Korea discount”

Korean equity valuation discussions often mention governance, controlling-shareholder structure, capital allocation and shareholder return as contributors to valuation discounts.

But valuation discount is not one variable with one cause. Sector mix, cyclicality, geopolitical exposure, growth outlook and interest rates also matter.

Therefore governance is one component of required return and expected cash-flow distribution, not a magic explanation for every low P/E.

## Type I vs Type II agency: why country context matters

In a company with dispersed ownership, main concern may be manager empire building.

In controlled group, manager may be disciplined by controller, but minority shareholder faces different risk: controller may extract private benefit.

Governance solution must match agency structure.

This is why importing one-country governance template without ownership context is dangerous.

## Governance due diligence workflow

A practical workflow:

1. Identify exact legal entity and listing.
2. Map top shareholders and related parties.
3. Draw group ownership graph at least one–two levels.
4. Review board and committees.
5. Check treasury shares and preferred shares.
6. Read related-party transactions and guarantees.
7. Review major restructurings/M&A/spin-offs.
8. Study 5–10 years of capital allocation.
9. Compare ROIC with reinvestment rate.
10. Check whether controller incentives align with entity shareholders.

## Mental Model

> Governance is the **operating system of corporate power**. Financial statements show what happened; governance explains who had authority and incentive to make those decisions. In Korean groups, always ask both `who owns?` and `who controls through the network?`.

## Common misconceptions

Founder ownership below 50% does not mean founder has no control.

Outside directors do not guarantee substantive independence.

Related-party transaction is not automatically tunneling.

High dividend is not always “good governance” if company has high-return reinvestment opportunity.

Low dividend is not always bad if retained earnings compound at strong ROIC.

Group-level synergy does not automatically justify transferring value away from minority shareholders of a specific listed affiliate.

## Connections

Read [05_group_structure_affiliates_holding_companies](./05_group_structure_affiliates_holding_companies.md) first for ownership graphs, then [09_disclosure_accounting_dart_kind](./09_disclosure_accounting_dart_kind.md) to locate governance evidence in filings, and [20_how_to_analyze_a_korean_company](./20_how_to_analyze_a_korean_company.md) for end-to-end application.
