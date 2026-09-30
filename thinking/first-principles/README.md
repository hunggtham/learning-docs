# First Principles — Tách assumptions ra khỏi constraints thật

Tư duy từ nguyên lý nền tảng (first-principles thinking / 제일 원리 사고) là cách phân rã vấn đề về các facts, constraints và relationships cơ bản nhất mà ta có lý do tốt để tin, rồi xây lời giải trở lại từ đó.

Nó không có nghĩa “bỏ qua toàn bộ kiến thức cũ”. Nếu một established result đã được chứng minh hoặc kiểm nghiệm tốt, dùng nó thường hiệu quả hơn reinventing everything.

## 1. Analogy vs first principles

**Reasoning by analogy:** “người khác làm X, nên ta cũng làm X”.

**First principles:** “X tồn tại để giải quyết constraint nào? Constraint đó có tồn tại trong case của ta không? Có cách khác thỏa constraint tốt hơn không?”.

Analogy nhanh và hữu ích khi contexts giống nhau. First principles đáng dùng khi convention có thể lỗi thời, cost lớn hoặc problem mới.

## 2. Decomposition

Một workflow:

```text
Desired outcome
→ constraints
→ variables we control
→ facts / laws / invariants
→ assumptions
→ remove assumptions one by one
→ rebuild candidate solutions
```

Điểm quan trọng là phân biệt **constraint thật** với **policy/convention**. “API chỉ cho phép X” có thể là constraint hiện tại; “team luôn làm X” chỉ là convention.

## 3. Assumption ledger

Với vấn đề khó, lập bảng:

```text
Assumption
Why do we believe it?
Evidence
What breaks if false?
How can we test it cheaply?
```

Nhiều breakthrough thực tế đến từ việc tìm assumption yếu nhưng đang khóa toàn solution space.

## 4. Reconstruction

Sau decomposition, phải build trở lại. Đây là phần thường bị bỏ quên. Một solution tốt cần thỏa physical, economic, legal, human và operational constraints cùng lúc.

First principles không miễn trừ system effects; solution local có thể tạo second-order cost. Vì vậy nối sang [Systems Thinking](../systems-thinking/README.md).

## 5. Khi không nên dùng quá mức

- task chuẩn hóa có established best practice tốt;
- safety-critical domain nơi reinventing bỏ qua accumulated knowledge;
- problem nhỏ mà analysis cost lớn hơn benefit;
- khi ta thiếu domain knowledge đến mức không biết “principle” nào thật sự fundamental.

## Examples

**Software:** thay vì hỏi “framework nào phổ biến?”, hỏi request cần đi qua state, data, rendering, security và latency constraints nào.

**Career:** thay vì “ngành nào hot?”, hỏi mục tiêu income, learning, geography, language, risk capacity và transferable skills.

**Investment:** thay vì “stock này đang trend”, hỏi asset tạo cash flow/value bằng mechanism nào, assumptions nào drive valuation và downside nào phá thesis.

## Connections

- [Mathematical Thinking](../../mathematics/00_foundations/00_mathematical_thinking.md): formal decomposition và assumptions.
- [Critical Thinking](../critical-thinking/README.md): evidence cho assumptions.
- [Systems Thinking](../systems-thinking/README.md): reconstruction trong system có interactions.
- [Opportunity Cost](../opportunity-cost/README.md): constraints tạo trade-offs.
- [Computer Science](../../computer_science/README.md): abstractions, invariants và system design.