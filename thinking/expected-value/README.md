# Expected Value — So sánh các tương lai bằng probability-weighted payoff

Giá trị kỳ vọng (expected value / 기대값, EV) là cách kết hợp outcome và probability. Formal definition nằm ở [Expectation & Variance](../../mathematics/06_probability_statistics/04_expectation_variance_and_limit_laws.md). Ở đây EV được dùng như decision tool.

## 1. Core idea

Với các states `i`:

```text
EV = Σ P(state_i) × payoff(state_i)
```

EV buộc ta nói rõ hai điều mà intuition thường trộn lẫn: **khả năng xảy ra** và **mức lợi/hại nếu xảy ra**.

## 2. Example

Một project nhỏ có:

- 40% chance tạo +₩5M value;
- 50% chance hòa vốn;
- 10% chance mất ₩1M.

EV khái niệm = `0.4×5 + 0.5×0 - 0.1×1 = +1.9M KRW`.

Nhưng EV dương chưa tự động có nghĩa “nên làm”. Ta còn phải kiểm tra capital constraint, time opportunity cost, downside, correlation và reversibility.

## 3. One-shot vs repeated decisions

EV đặc biệt hữu ích khi decision được lặp nhiều lần trong điều kiện tương đối ổn định. Với one-shot life decision, utility, ruin và irreversibility có thể quan trọng hơn average payoff.

Một bet có EV dương nhưng 5% chance bankruptcy có thể không phù hợp nếu bankruptcy làm ta không thể tiếp tục chơi.

## 4. Monetary payoff ≠ utility

₩1M tăng thêm không tạo cùng utility cho mọi người và mọi mức wealth. Decision đời thực có non-monetary outcomes: health, time, stress, flexibility, reputation.

Có thể dùng multi-criteria decision analysis thay vì ép mọi thứ thành tiền, nhưng vẫn nên giữ trade-offs explicit.

## 5. Value of information

Nếu một test/research nhỏ có thể làm probabilities thay đổi và giúp tránh decision lớn sai, information có value.

Câu hỏi:

```text
Will this information change my action?
How much downside can it prevent?
How much does obtaining it cost?
```

Nếu information không thể thay đổi decision, research thêm có thể chỉ là delay.

## 6. Common failure modes

- probability giả chính xác;
- chỉ tính upside states;
- bỏ opportunity cost;
- bỏ correlated outcomes;
- dùng EV để biện minh risk of ruin;
- double-count same benefit ở nhiều states.

## Connections

- [Probability](../probability/README.md): xây probabilities.
- [Risk](../risk/README.md): variance, tails, ruin.
- [Opportunity Cost](../opportunity-cost/README.md): payoff phải tính best alternative forgone.
- [Decision Making](../decision-making/README.md): EV là input, không phải toàn bộ decision.
- [Investing](../../investing/README.md): scenario returns and capital allocation.
- [Economics](../../economics/README.md): choices under scarcity/uncertainty.