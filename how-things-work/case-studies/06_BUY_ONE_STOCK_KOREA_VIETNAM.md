# Case 06 — Mua một cổ phiếu ở Hàn Quốc và Việt Nam: từ nút `Buy` tới ownership settlement

Case này nối [stock-market](../stock-market/README.md), [banking-system](../banking-system/README.md), [Internet](../internet/README.md) và [cloud-computing](../cloud-computing/README.md). Mục tiêu không phải chọn cổ phiếu nào tốt; mục tiêu là hiểu vì sao app báo `Filled` nhưng giao dịch vẫn còn lifecycle phía sau.

## 1. Bắt đầu từ hành động rất đơn giản

Bạn mở broker app và mua một cổ phiếu niêm yết.

```text
Investor
  ↓
Broker app
  ↓
Broker OMS/RMS
  ↓
Exchange order book
  ↓
Match
  ↓
Trade confirmation
  ↓
Clearing
  ↓
Cash + securities settlement
  ↓
Depository / broker account records updated
```

Hai nước khác institutions, nhưng architecture cơ bản rất giống.

## 2. App không gửi thẳng order vào matching engine

Broker cần kiểm tra:

- account status;
- buying power/cash/margin;
- quantity/price validity;
- market/session rules;
- risk/compliance controls.

```text
Tap BUY
  ↓
client request
  ↓
broker gateway
  ↓
risk validation
  ↓
order management system
  ↓
exchange gateway
```

Nếu broker/cloud/network lỗi trước exchange acknowledgement, user có thể không biết order đã tới exchange chưa. Vì vậy trading systems cần idempotency/order IDs/reconciliation.

## 3. Order book

Exchange matching engine giữ buy/sell orders theo rule, thường price-time priority ở many continuous-auction contexts.

```text
BUY  price  quantity
SELL price  quantity
        ↓
compatible prices meet
        ↓
trade generated
```

`Order accepted` ≠ `Filled`. `Filled` nghĩa execution đã xảy ra, chưa phải settlement.

## 4. Korea flow

Simplified:

```text
Investor
 ↓
Korean securities company
 ↓
KRX market
 ↓ trade
clearing obligations
 ↓
Korea Securities Depository / settlement infrastructure
 ↓
book-entry securities + cash settlement
```

Korean domestic stock market uses T+2 settlement: trade date is `T`, legal cash/securities settlement occurs two business days later under the standard cycle.

Example:

```text
Monday: trade executed (T)
Tuesday: T+1
Wednesday: T+2 settlement
```

Holidays shift actual calendar date.

## 5. Vietnam flow

Simplified:

```text
Investor
 ↓
Vietnam securities company
 ↓
HOSE / HNX trading venue depending instrument
 ↓ trade
VSDC clearing
 ↓
settlement bank + VSDC book-entry
 ↓
securities/cash settlement
```

VSDC states listed stocks, fund certificates and covered warrants settle on T+2 under multilateral clearing.

Again:

```text
Trade filled on T
      ↓
obligations calculated
      ↓
T+2 cash + securities settlement
```

## 6. Why clearing exists

If thousands/millions of trades occurred, settling each gross bilateral payment separately is inefficient.

Clearing can net obligations:

```text
Broker A buys 100 from B
Broker A sells 70 to C

Gross flows: 100 + 70
Net position for A: +30 shares (simplified)
```

Actual rules are more detailed, but netting reduces settlement flows and liquidity needs.

## 7. Depository ownership is book-entry, not paper certificate movement

Modern listed shares are generally immobilized/dematerialized in depository systems.

```text
Central depository records
      ↓
member / broker / custodian accounts
      ↓
beneficial-owner records at account layer
```

When you “receive shares”, no truck moves certificates. Book-entry positions change.

## 8. Cash leg and securities leg must meet

Settlement risk exists if one side delivers but the other does not. Systems therefore coordinate **delivery versus payment (DvP / 동시결제)** or equivalent mechanisms.

Mental model:

```text
cash finality
     ↕ coordinated
securities finality
```

The exact institutional implementation differs by market, but concept is universal.

## 9. What if broker app says `Filled`?

State machine:

```text
NEW
 ↓
ACCEPTED
 ↓
PARTIALLY_FILLED / FILLED
 ↓
CLEARED
 ↓
SETTLED
```

UI often highlights `FILLED` because trading intent is accomplished. Market infrastructure still works toward `SETTLED`.

## 10. Korea ↔ Vietnam comparison

| Layer | Korea | Vietnam |
|---|---|---|
| Trading venue | KRX markets | HOSE/HNX depending security/market |
| Broker role | order/risk/client account | order/risk/client account |
| Depository | Korea Securities Depository | VSDC |
| Standard stock settlement | T+2 | T+2 |
| Currency | KRW | VND |
| User-visible experience | broker app hides most post-trade infrastructure | broker app similarly abstracts clearing/settlement |

The important insight is not that both are identical. It is that both implement the same fundamental problem: **turn a matched promise into final exchange of cash and securities**.

## 11. Cross-border investor adds more layers

A Korean resident buying Vietnamese securities or vice versa may add:

```text
FX conversion
custodian
foreign investor account rules
capital controls/reporting where applicable
tax
repatriation
```

Those belong in [`../../investing/06_markets_korea_vietnam/`](../../investing/06_markets_korea_vietnam/README.md), not this mechanism case.

## 12. Failure scenarios

### Broker app down
Exchange can still be healthy; specific broker clients cannot send/manage orders.

### Exchange halt
Broker works, but matching stops for affected market/security.

### Clearing issue
Trades exist but obligations cannot progress normally.

### Settlement bank/liquidity problem
A member may have difficulty delivering cash.

### Depository/accounting problem
Securities ownership update/reconciliation may delay.

This separation explains why “stock market outage” is too vague. Ask which layer failed.

## 13. What is final?

For the investor, strongest mental checkpoint is:

```text
trade execution
        ↓
clearing obligation
        ↓
settled cash/securities
        ↓
post-settlement account record
```

A price on screen is information. A fill is execution. Settlement is final transfer layer.

## Nguồn chính thức tham chiếu

- Korea Financial Services Commission — T+2 settlement terminology: https://www.fsc.go.kr/in090301/view?dicId=1831
- Korea Exchange Global — settlement information: https://global.krx.co.kr/
- Vietnam Securities Depository and Clearing Corporation — clearing and settlement: https://vsdc.vn/en/sd/XAz40d2Q-9j569TvBgLQaQ
