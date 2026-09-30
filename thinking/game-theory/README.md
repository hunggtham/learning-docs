# Game Theory — Khi outcome phụ thuộc vào lựa chọn của người khác

Lý thuyết trò chơi (game theory / 게임 이론) nghiên cứu strategic interaction: payoff của tôi phụ thuộc không chỉ vào action của tôi mà còn vào action của actor khác. Canonical economics nằm ở [Market Structure & Game Theory](../../economics/02_market_structure_game_theory/README.md). Trang này tập trung vào mental models dùng rộng hơn.

## 1. Khi nào problem là một “game”?

Dùng game-theoretic lens khi có:

- nhiều actors;
- mỗi actor có actions;
- payoff phụ thuộc vào combination of actions;
- actors có beliefs về nhau;
- rules/information structure ảnh hưởng strategy.

Nếu outcome chủ yếu do nature/randomness, probability model có thể phù hợp hơn game theory.

## 2. Dominant strategy

Một action là dominant nếu tốt hơn alternatives bất kể actor khác làm gì. Nhiều real-world games không có dominant strategy, nên đừng cố tìm “best move” độc lập khỏi context.

## 3. Nash equilibrium

Nash equilibrium là profile actions nơi không actor nào muốn đơn phương đổi strategy khi giữ strategies của others cố định.

Equilibrium **không đồng nghĩa optimal, fair hoặc desirable**. Prisoner’s Dilemma nổi tiếng vì equilibrium cá nhân có thể cho collective outcome kém hơn cooperation.

## 4. Zero-sum vs positive-sum

Không phải mọi negotiation là zero-sum. Nếu actors có preferences khác nhau về time, risk, features hoặc resources, trade có thể tạo surplus cho cả hai.

Bước đầu của negotiation tốt là tìm dimensions có thể đổi chác, không chỉ tranh một fixed pie.

## 5. Repeated games

Khi actors gặp lại nhau, reputation và future punishment/reward thay đổi incentives. Cooperation có thể ổn định hơn nếu future interaction quan trọng và defection quan sát được.

Điều này giúp giải thích supplier relationships, team norms, platform ecosystems và international agreements nhưng mỗi domain cần institutional evidence riêng.

## 6. Information asymmetry và signaling

Actor có private information có thể signal type qua costly actions. Nhưng không phải mọi signal đều credible. Cần hỏi signal có cost khác nhau giữa types hay không.

## 7. Commitment

Tự giới hạn future options đôi khi tăng bargaining power nếu commitment credible. Contract, escrow, public promise hoặc technical architecture có thể đóng vai trò commitment device.

## 8. Practical game map

```text
Players
Actions
Information
Payoffs
Sequence / timing
Repeated or one-shot?
Can players communicate?
Can commitments be enforced?
What equilibrium-like responses are plausible?
How would changing the rules change behavior?
```

## Applications

- **Business:** pricing, entry, platform strategy, auctions.
- **Negotiation:** outside options, credible commitments, repeated interaction.
- **Politics/public institutions:** coalition/rule analysis at institutional level, without inferring private motives without evidence.
- **Cybersecurity:** attacker–defender adaptation.
- **Distributed systems:** mechanism design, resource allocation and adversarial environments.

## Connections

- [Economics](../../economics/README.md): canonical formal game theory, auctions and mechanism design.
- [Incentives](../incentives/README.md): payoff structure.
- [Systems Thinking](../systems-thinking/README.md): feedback from adaptation.
- [Decision Making](../decision-making/README.md): strategic decisions.
- [Psychology](../../psychology/README.md): actual humans may deviate from idealized rational-player assumptions.
- [Computer Science](../../computer_science/README.md): algorithms, mechanism design and adversarial settings.