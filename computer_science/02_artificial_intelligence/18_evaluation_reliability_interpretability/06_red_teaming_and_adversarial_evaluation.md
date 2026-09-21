# Red Teaming và Adversarial Evaluation

**Red teaming (레드팀 평가)** là quá trình chủ động tìm cách làm AI system thất bại, vi phạm policy hoặc hành xử nguy hiểm trước khi attacker/user/environment vô tình tìm ra. Khác robustness testing thông thường, red teaming thường giả định input hoặc strategy có tính đối kháng và thích nghi với system.

## Threat Model trước Attack List

Không bắt đầu bằng danh sách prompt tricks. Xác định:

```text
asset cần bảo vệ là gì?
attacker có capability gì?
attacker biết gì về system?
entry points nào?
impact nào đáng lo?
```

Threat model cho RAG assistant khác autonomous payment agent.

## Attack Surfaces

AI application có nhiều surfaces:

- user prompt;
- uploaded files;
- retrieved documents;
- tools/APIs;
- memory;
- model endpoint;
- training data;
- logs/caches;
- orchestration state.

Chỉ red-team prompt layer là chưa đủ.

## Prompt Injection

Malicious instruction cố override intended behavior.

Direct injection đến từ user. Indirect injection có thể nằm trong webpage/document/tool result mà system retrieve.

Important principle:

> Untrusted content phải được coi là data, không phải authority.

System prompt không phải security boundary.

## Data Exfiltration Tests

Try to extract:

- secrets;
- hidden prompts;
- other tenant data;
- retrieved unauthorized documents;
- tool credentials.

Strong defense dựa auth/permissions/data isolation, không dựa model “biết không nên nói”.

## Tool Abuse

Agent có tools tạo side effect cần test:

- unauthorized action;
- parameter manipulation;
- duplicate action;
- confused-deputy attack;
- injected tool result;
- privilege escalation.

Authorization phải enforced outside model.

## Jailbreak Evaluation

Jailbreaks thử vượt safety behavior qua roleplay, encoding, instruction conflict hoặc multi-turn setup.

Red team nên measure failure categories/impact, không chỉ collect clever prompts.

## Adversarial Examples

Vision/classification có optimized perturbations. Threat model cần specify norm/physical realism/query access.

Robustness against white-box gradient attack khác black-box real-world attack.

## RAG Poisoning

Attacker chèn malicious document vào corpus hoặc manipulate ranking.

Tests:

```text
poisoned document ranks high?
model follows hidden instruction?
citation makes attack look legitimate?
metadata filters bypassed?
```

## Memory Poisoning

Agent persistent memory có thể store malicious false instruction/state, causing future sessions fail.

Need write validation, provenance, scope và deletion.

## Multi-Turn Attacks

Single-turn safety tests miss gradual context manipulation. Stateful agents need multi-turn adversarial scenarios.

## Resource Exhaustion

Security includes availability:

- huge prompts/files;
- recursive agent loops;
- expensive tool calls;
- adversarial inputs maximizing output length.

Enforce quotas, budgets, size limits, cancellation.

## Model Extraction / Abuse

Public endpoint có thể be queried for imitation or exploit. Rate limits, abuse detection và terms may reduce risk, though complete prevention difficult.

## Automated Red Teaming

Attacker models/generators can create variants at scale. Useful for breadth but can overfit to generator style.

Human red teams bring creativity/domain context. Best approach combines automation + human expertise.

## Adaptive Evaluation

Once system patched, attackers adapt. Red teaming is recurring lifecycle, not one pre-launch exercise.

## Scoring

Track more than attack success rate:

```text
severity
reproducibility
required attacker capability
time/cost to exploit
blast radius
detectability
```

A rare catastrophic exploit can matter more than common harmless policy deviation.

## Defense-in-Depth Validation

Test layers independently:

```text
model refuses?
permission layer blocks?
schema validator rejects?
rate limit triggers?
audit alert fires?
```

If model defense fails but authorization still prevents harm, blast radius bounded.

## Red Team to Regression

Confirmed vulnerability should become:

- regression test;
- monitoring signal;
- architecture fix where possible;
- incident/runbook knowledge.

Do not depend solely on prompt patch that attacker can rephrase around.

## Safe Evaluation Environment

High-impact tools/actions should be red-teamed in sandbox/simulation or with harmless test credentials.

Do not perform destructive real-world actions just to test agent.

## Mental Model

```text
Red teaming = adversarial search over the whole AI system, guided by a threat model and impact.
```

## Common Misconceptions

### “Prompt injection là model problem”

Nó là system security problem; model robustness helps but permission boundary is essential.

### “Pass jailbreak benchmark nghĩa secure”

Attackers adapt and other surfaces remain.

### “Red team xong trước launch là đủ”

Models, prompts, tools và attackers change continuously.

## Knowledge Connection

Xem [Robustness](./03_robustness_and_distribution_shift.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md) và [AI Safety/Security](../19_ai_safety_security_alignment/README.md).