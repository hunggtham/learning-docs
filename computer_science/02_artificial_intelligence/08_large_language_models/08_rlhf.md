# Reinforcement Learning from Human Feedback (RLHF)

**RLHF (Reinforcement Learning from Human Feedback / 인간 피드백 기반 강화학습)** là một family of post-training methods dùng human preference signal để làm model outputs phù hợp hơn với desired behavior. Mục tiêu không phải “human cho biết fact nào đúng rồi model học thuộc”. RLHF thường học **preference ordering giữa candidate responses** và dùng signal đó để update policy.

## Vì sao SFT chưa đủ?

SFT cần một target response cụ thể. Nhưng nhiều prompts có nhiều answers đều acceptable ở mức khác nhau. Ta thường quan tâm preference mềm:

```text
response A hữu ích hơn B
A chính xác hơn B
A ít harmful hơn B
A concise hơn B
```

Human ranking chứa information mà single-target imitation không thể biểu diễn đầy đủ.

## Pipeline cổ điển

Một RLHF pipeline phổ biến gồm ba giai đoạn:

```text
1. SFT policy
2. collect preference pairs → train reward model
3. optimize policy against reward model with RL
```

### Preference data

Với prompt `x`, model tạo candidates `y_a`, `y_b`. Human label chọn response preferred:

\[
y_w \succ y_l
\]

trong đó `w` là winner và `l` là loser.

### Reward model

Reward model `r_\phi(x,y)` học score sao cho preferred answer có reward cao hơn. Một objective điển hình:

\[
\mathcal L_{RM}=-\log\sigma(r_\phi(x,y_w)-r_\phi(x,y_l))
\]

Reward model không phải oracle truth. Nó approximates preference distribution trong annotation data.

## Policy optimization

Policy LLM sau đó được optimized để maximize learned reward, nhưng nếu chỉ maximize reward model trực tiếp, model có thể exploit its imperfections. Vì vậy objective thường thêm penalty giữ policy gần reference model:

\[
\max_\theta \; \mathbb E[r_\phi(x,y)] - \beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

KL term hạn chế policy drift quá xa khỏi model đã có language quality tốt.

## PPO intuition

**Proximal Policy Optimization (PPO)** từng là algorithm phổ biến cho RLHF. PPO giới hạn update quá lớn giữa policy mới và cũ để training ổn định hơn.

Trong LLM setting, “action” là generated token và trajectory là response sequence. Reward thường đến ở cuối sequence hoặc qua learned signal.

Điều này làm credit assignment khó: reward tổng cho cả response không nói rõ token nào đóng góp bao nhiêu.

## Reward hacking

Nếu reward model có blind spot, policy có thể tìm output score cao nhưng human không thực sự thích. Đây là **reward hacking / specification gaming**.

Ví dụ nếu reward model correlate verbosity với helpfulness, policy có thể tạo answer dài không cần thiết chỉ để tăng reward.

Đây là general lesson của optimization:

> Optimizer sẽ tối ưu **metric được cho**, không phải mục tiêu trong đầu designer.

## Preference không bằng truth

Human annotators có thể disagree, thiếu domain expertise hoặc bị ảnh hưởng wording. Reward model phản ánh annotation process.

Vì vậy RLHF có thể cải thiện helpfulness/style nhưng không guarantee factual correctness.

Grounding, retrieval và verification vẫn cần thiết.

## Annotation design

Preference guideline ảnh hưởng model behavior rất mạnh. Nếu labelers được yêu cầu ưu tiên concise answers, model sẽ học concise preference. Nếu safety policy mơ hồ, labels inconsistent.

Inter-annotator disagreement là signal quan trọng: problem có thể subjective hoặc guideline chưa đủ rõ.

## Helpful, Honest, Harmless là multi-objective

Một assistant thường phải balance nhiều objectives. Helpfulness và harmlessness đôi khi conflict; honesty có thể yêu cầu model thừa nhận uncertainty thay vì đưa answer decisive.

Không có một scalar reward hoàn hảo biểu diễn mọi value. Practical systems dùng mixtures, policies và separate evaluations.

## Online vs offline preference optimization

Classical RLHF có model generate new trajectories trong loop, nên distribution thay đổi khi policy update. Đây là online/on-policy flavor.

Các methods như DPO có thể optimize trực tiếp trên offline preference pairs mà không cần explicit reward-model + PPO loop.

Xem tiếp: [Preference Optimization and DPO](./09_preference_optimization_and_dpo.md).

## RLHF và safety

Safety preference data có thể dạy refusal, safe completion và policy adherence. Nhưng model vẫn có thể bị jailbreak vì training distribution không cover mọi adversarial prompt.

Runtime defenses, input/output filters, tool permission boundaries và red teaming là system-level layers bổ sung.

## KL penalty như stability constraint

Nếu reward optimization quá mạnh, model có thể mất fluency hoặc collapse vào weird high-reward outputs. KL penalty giữ distribution gần reference.

`β` lớn → policy conservative.

`β` nhỏ → policy có thể move aggressively theo reward.

Đây là một trust-region-like trade-off.

## Reward model overoptimization

Khi optimize policy ngày càng mạnh against fixed reward model, actual human preference có thể tăng lúc đầu rồi giảm khi policy exploit imperfections.

Do đó reward-model score không nên là only evaluation after training.

## Mental Model

```text
Human preferences
      ↓
learned preference signal
      ↓
optimize policy
      ↓
assistant behavior shifts
```

RLHF là **behavior alignment under imperfect preference measurement**, không phải “upload human values vào model”.

## Common Misconceptions

### “RLHF làm model biết facts đúng hơn”

Có thể gián tiếp cải thiện honesty, nhưng factual knowledge chủ yếu đến từ pretraining/retrieval; reward optimization không biến preference labels thành complete world model.

### “Reward model chính là human judgment”

Không. Nó là learned approximation có bias/error.

### “RLHF = PPO”

PPO là một optimization choice. RLHF rộng hơn và preference optimization có nhiều alternatives.

## Knowledge Connection

RLHF là ứng dụng của [Reinforcement Learning](../11_reinforcement_learning/00_reinforcement_learning_foundations.md) và [Optimization](../01_mathematical_foundations/06_optimization.md), nhưng practical LLM post-training có structure riêng vì action space là token sequences và reward learned from preferences.

Xem tiếp: [DPO](./09_preference_optimization_and_dpo.md).