# Thinking Toolkit — Conceptual Dependencies

File này mô tả **dependency graph** giữa các thinking tools. Nó không ép thứ tự học tuyệt đối; mục tiêu là giúp reader biết khi nào một tool đang dựa trên concept nào khác.

## Core graph

```text
Problem Framing
├── Critical Thinking
│   ├── Logical Fallacies
│   └── Cognitive Bias
├── Model Selection
│   ├── First Principles
│   └── Systems Thinking
└── Causal Reasoning
    └── Statistics for Life

Probability
├── Forecasting
├── Expected Value
│   └── Value of Information
└── Risk

Opportunity Cost
└── Decision Making

Incentives
├── Game Theory
└── Systems Thinking

All paths
└── Decision Making
```

## Dependency by question type

### “Claim này có đáng tin không?”

```text
Problem Framing
→ Critical Thinking
→ Statistics for Life
→ Causal Reasoning
→ Cognitive Bias / Logical Fallacies
```

### “Điều gì có thể xảy ra tiếp theo?”

```text
Probability
→ Base rate
→ Forecasting
→ Model Selection
→ Risk
```

### “Tôi nên chọn phương án nào?”

```text
Problem Framing
→ Opportunity Cost
→ Probability
→ Expected Value
→ Risk
→ Value of Information
→ Decision Making
```

### “Người khác sẽ phản ứng thế nào?”

```text
Incentives
→ Game Theory
→ Systems Thinking
→ Decision Making
```

### “Vì sao hệ thống cho kết quả này?”

```text
Problem Framing
→ Causal Reasoning
→ Systems Thinking
→ Incentives
→ Model Selection
```

## Canonical ownership

`thinking/` chỉ sở hữu workflow tích hợp. Theory sâu tiếp tục thuộc:

- [Mathematics](../mathematics/README.md): probability, statistics, expectation, optimization, formal modeling.
- [Philosophy](../philosophy/README.md): logic, argument, epistemology, justification.
- [Psychology](../psychology/README.md): cognitive bias, decision science, human cognition.
- [Economics](../economics/README.md): opportunity cost, incentives, equilibrium, game theory.
- [Research Methods](../research_methods/README.md): measurement, study design, causal inference, evidence synthesis.

## Editorial rule

Khi thêm một thinking tool mới, phải trả lời được ba câu:

1. Tool giải quyết failure mode nào mà existing tools chưa bao phủ rõ?
2. Canonical theory nằm ở đâu để tránh duplicate?
3. Tool này handoff sang ít nhất hai domain thực tế nào?

Nếu không trả lời được, ưu tiên internal link thay vì tạo file mới.