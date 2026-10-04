# Case — Đọc nghiên cứu, health claim và statistical evidence

Các claim về sức khỏe và nghiên cứu khoa học thường trộn nhiều tầng: measurement, statistics, causality, effect size, external validity và decision consequence. Một p-value hoặc một headline không thể thay cho toàn bộ chuỗi reasoning.

Trang này không cung cấp chẩn đoán hay điều trị. Khi quyết định sức khỏe cá nhân có stakes cao, phải handoff sang bằng chứng y khoa và chuyên môn phù hợp.

## Situation

Bạn đọc:

> “Study cho thấy intervention X giảm risk của outcome Y.”

## Step 1 — What exactly was studied?

```text
Population?
Exposure / intervention?
Comparator?
Outcome?
Time horizon?
Study design?
```

Nếu population nghiên cứu khác xa người đang áp dụng, external validity cần được xem riêng.

## Step 2 — Measurement

Hỏi:

- outcome là clinical outcome hay surrogate?
- self-report hay objective measure?
- measurement error có systematic không?
- attrition/missing data lớn không?

Measurement kém không thể được “sửa” chỉ bằng sample size lớn.

## Step 3 — Relative vs absolute effect

Ví dụ risk giảm từ 2% xuống 1%:

```text
relative risk reduction = 50%
absolute risk reduction = 1 percentage point
```

Cả hai đều đúng nhưng trả lời câu hỏi khác nhau. Decision consequence thường cần absolute magnitude.

## Step 4 — Uncertainty

Đừng chỉ hỏi estimate là bao nhiêu; hỏi range plausible rộng đến đâu.

```text
point estimate
confidence / credible interval
sample size
heterogeneity
```

Statistical significance không đồng nghĩa clinical importance.

## Step 5 — Causality

Nếu observational study, check confounding, reverse causality và selection. Nếu randomized trial, vẫn cần kiểm tra adherence, attrition, outcome choice và generalizability.

Handoff: [Causal Reasoning](../causal-reasoning/README.md).

## Step 6 — Single study vs evidence body

Một study là một observation trong evidence ecosystem.

```text
single study
→ replication
→ multiple studies
→ systematic synthesis
→ guideline / cumulative evidence when appropriate
```

Không phải meta-analysis nào cũng mạnh; quality phụ thuộc included studies, heterogeneity và methods.

## Step 7 — Decision threshold

Evidence không tự quyết định action. Cần kết hợp:

```text
baseline risk
expected benefit
possible harm
uncertainty
alternatives
preferences / constraints
```

Thinking toolkit dừng ở cấu trúc này; clinical recommendation thuộc domain y khoa.

## Step 8 — Red flags khi đọc online

- chỉ nói relative change;
- không nói population;
- causal headline từ observational data;
- “statistically significant” nhưng effect rất nhỏ;
- subgroup được nhấn mạnh sau nhiều comparisons;
- animal/lab result được viết như proven human outcome;
- một paper được trình bày như scientific consensus.

## Toolkit used

[Problem Framing](../problem-framing/README.md) → [Statistics for Life](../statistics-for-life/README.md) → [Causal Reasoning](../causal-reasoning/README.md) → [Critical Thinking](../critical-thinking/README.md) → [Risk](../risk/README.md) → [Value of Information](../value-of-information/README.md).

## Handoff

- Study design, sampling, evidence synthesis → [Research Methods](../../research_methods/README.md)
- Probability/statistics → [Mathematics](../../mathematics/README.md)
- Behavior/cognition → [Psychology](../../psychology/README.md)
- Biological mechanism → [Biology](../../biology/README.md)