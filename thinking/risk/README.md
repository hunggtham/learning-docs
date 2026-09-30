# Risk — Không chỉ hỏi “xác suất bao nhiêu?” mà còn “sai thì mất gì?”

Rủi ro (risk / 위험) là sự kết hợp giữa uncertainty và consequences. Hai event có cùng probability nhưng không có cùng mức risk nếu một event chỉ gây bất tiện còn event kia gây ruin hoặc irreversible harm.

## 1. Probability × consequence chỉ là điểm bắt đầu

Expected loss hữu ích nhưng không đủ. Cần hỏi thêm:

- tail severity;
- correlation giữa failures;
- reversibility;
- time to recover;
- liquidity/capacity buffer;
- possibility of ruin;
- whether uncertainty itself is poorly known.

Một risk nhỏ lặp nhiều lần khác risk hiếm nhưng catastrophic.

## 2. Hazard, exposure, vulnerability

Một mental model hữu ích:

```text
hazard: thứ có thể gây hại
exposure: ta tiếp xúc với hazard đến mức nào
vulnerability: khi bị tác động, ta dễ tổn thương đến đâu
```

Ta có thể giảm risk bằng giảm bất kỳ thành phần nào, không chỉ cố dự báo hazard chính xác hơn.

## 3. Known risk vs deep uncertainty

Nếu distribution tương đối biết được, probability model hữu ích. Nếu system mới, regime thay đổi hoặc data quá ít, numeric precision có thể giả. Khi deep uncertainty cao, nên dùng scenario range, robustness và margin of safety.

## 4. Ruin constraint

Nếu một outcome có thể loại ta khỏi cuộc chơi, expected value dương chưa chắc đủ để chấp nhận. Ví dụ một strategy có EV tốt nhưng leverage khiến một tail event gây bankruptcy.

Nguyên tắc thực hành:

```text
Survive first → optimize second.
```

Đây không phải lời khuyên luôn tránh risk; nó nhắc rằng repeated decision chỉ tồn tại nếu ta còn capacity để tiếp tục.

## 5. Diversification và correlation

Diversification giảm idiosyncratic risk khi exposures không hoàn toàn correlated. Nếu nhiều positions cùng phụ thuộc một macro driver, số lượng assets tăng nhưng effective diversification có thể thấp.

## 6. Margin of safety

Margin of safety là buffer giữa estimate và failure boundary: extra cash runway, spare capacity, conservative load limit, lower leverage, backup path.

Nó đặc biệt hữu ích khi model error lớn hoặc consequence asymmetric.

## 7. Risk register mini-format

```text
Risk
Trigger / early signal
Likelihood range
Impact
Correlation / common cause
Mitigation
Contingency
Owner
Review condition
```

## Connections

- [Probability](../probability/README.md): model likelihood.
- [Expected Value](../expected-value/README.md): average weighted payoff.
- [Decision Making](../decision-making/README.md): trade risk against objective.
- [Investing](../../investing/README.md): drawdown, leverage, liquidity, portfolio risk.
- [PMP](../../pmp/README.md): project risk, contingency and governance.
- [Computer Science](../../computer_science/README.md): reliability/security risks and common-mode failure.
- [Systems Thinking](../systems-thinking/README.md): feedback, nonlinear failure và cascading effects.