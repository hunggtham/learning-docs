# Deep Reinforcement học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Deep Reinforcement học tập (learning / 학습)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao Deep RL khó hơn supervised deep học tập (learning / 학습)?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **DQN: Deep Q-Network** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Deep Reinforcement học tập (learning / 학습)** kết hợp Reinforcement học tập (learning / 학습) với neural networks để xử lý trạng thái (state / 상태)/hành động (action / 동작) spaces quá lớn cho tabular methods. Neural mạng (network / 네트워크) đóng vai trò hàm (function / 함수) approximator cho giá trị (value / 값), Q-function, chính sách (policy / 정책) hoặc môi trường (environment / 환경) mô hình (model / 모델).

```text
pixels / sensors / embeddings
        ↓
 neural representation
        ↓
Q-value / policy / value / model
        ↓
RL objective
```

## Vì sao Deep RL khó hơn supervised deep học tập (learning / 학습)?

Supervised học tập (learning / 학습) thường train trên dataset tương đối stationary. Trong RL:

- chính sách (policy / 정책) thay đổi → dữ liệu (data / 데이터) phân phối (distribution / 분포) thay đổi;
- targets có thể bootstrap từ mạng (network / 네트워크) itself;
- rewards delayed/sparse;
- exploration determines future dữ liệu (data / 데이터);
- samples temporally correlated;
- mục tiêu (objective / 목표) non-stationary.

Vì vậy neural mạng (network / 네트워크) sức chứa (capacity / 용량) không tự giải quyết RL; nó còn tạo stability problems mới.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **DQN: Deep Q-Network** tiếp nhận điểm tựa từ **Vì sao Deep RL khó hơn supervised deep học tập (learning / 학습)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Replay Matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DQN: Deep Q-Network

DQN approximates:

\[
Q(s,a;\theta)
\]

với neural mạng (network / 네트워크). đầu vào (input / 입력) có thể là ảnh (image / 이미지), đầu ra (output / 출력) là Q-value cho each discrete hành động (action / 동작).

Key kỹ thuật (engineering / 엔지니어링) ideas:

1. **experience replay**;
2. **mục tiêu (target / 대상) mạng (network / 네트워크)**;
3. reward/độ dốc (gradient / 기울기) stabilization.

Mất mát (loss / 손실):

\[
L(\theta)=\mathbb E[(r+\gamma\max_{a'}Q(s',a';\theta^-)-Q(s,a;\theta))^2]
\]

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Why Replay Matters** tiếp nhận điểm tựa từ **DQN: Deep Q-Network** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu (target / 대상) Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Replay Matters

Sequential frames/states highly correlated. SGD assumes batches useful when samples not all nearly identical. Replay randomizes historical transitions and reuses expensive experience.

Prioritized replay samples high-TD-error transitions more often, but needs importance correction to reduce sampling độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Mục tiêu (target / 대상) Networks** tiếp nhận điểm tựa từ **Why Replay Matters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Double DQN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu (target / 대상) Networks

Moving mục tiêu (target / 대상) bài toán (problem / 문제):

```text
network changes
→ target changes
→ network chases own changing prediction
```

Frozen/slow mục tiêu (target / 대상) mạng (network / 네트워크) reduces phản hồi (feedback / 피드백) instability.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Double DQN** tiếp nhận điểm tựa từ **Mục tiêu (target / 대상) Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dueling Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Double DQN

Reduce max overestimation by selecting hành động (action / 동작) with online mạng (network / 네트워크), evaluating it with mục tiêu (target / 대상) mạng (network / 네트워크):

\[
a^*=\arg\max_a Q(s',a;\theta)
\]

\[
y=r+\gamma Q(s',a^*;\theta^-)
\]

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Dueling Networks** tiếp nhận điểm tựa từ **Double DQN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Policy-Based Deep RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dueling Networks

Decompose:

\[
Q(s,a)=V(s)+A(s,a)
\]

with normalization to make decomposition identifiable. Useful when many actions have similar tác động (effect / 효과) from a trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Policy-Based Deep RL** tiếp nhận điểm tựa từ **Dueling Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Biểu diễn (representation / 표현) học tập (learning / 학습) in RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Policy-Based Deep RL

Chính sách (policy / 정책) mạng (network / 네트워크) directly outputs hành động (action / 동작) phân phối (distribution / 분포). PPO, SAC and actor-critic methods quy mô (scale / 규모) naturally to continuous/high-dimensional hành động (action / 동작) spaces.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Biểu diễn (representation / 표현) học tập (learning / 학습) in RL** tiếp nhận điểm tựa từ **Policy-Based Deep RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **World các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Biểu diễn (representation / 표현) học tập (learning / 학습) in RL

RL tác nhân (agent / 에이전트) must learn not just điều khiển (control / 제어) but useful trạng thái (state / 상태) representations. Reward tín hiệu (signal / 신호) may be sparse, so biểu diễn (representation / 표현) học tập (learning / 학습) can be data-inefficient.

Auxiliary/self-supervised objectives can help learn dynamics/relevant features.

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **World các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Biểu diễn (representation / 표현) học tập (learning / 학습) in RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Imagination and Latent Planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## World các mô hình (models / 모델들)

Model-based Deep RL learns môi trường (environment / 환경) dynamics:

\[
\hat s_{t+1}=f_\phi(s_t,a_t)
\]

or latent dynamics, then plans/improves chính sách (policy / 정책) using learned mô hình (model / 모델).

Benefits: potential mẫu (sample / 표본) efficiency.

Rủi ro (risk / 위험): **mô hình (model / 모델) độ lệch (bias / 편향)**. Planning can exploit mô hình (model / 모델) errors, especially far outside huấn luyện (training / 학습) phân phối (distribution / 분포).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Imagination and Latent Planning** tiếp nhận điểm tựa từ **World các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exploration in High Dimensions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Imagination and Latent Planning

Instead of simulating raw pixels, world-model agents can learn latent trạng thái (state / 상태) `z_t` and predict latent transitions/rewards. Planning in latent không gian (space / 공간) reduces chi phí (cost / 비용) if biểu diễn (representation / 표현) preserves control-relevant thông tin (information / 정보).

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Exploration in High Dimensions** tiếp nhận điểm tựa từ **Imagination and Latent Planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sparse Reward and Hindsight** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exploration in High Dimensions

Random hành động (action / 동작) exploration is inefficient when rewards sparse. Methods include:

- intrinsic motivation;
- curiosity/prediction lỗi (error / 오류);
- count/pseudo-count bonuses;
- entropy maximization;
- uncertainty-driven exploration.

But intrinsic rewards can be gamed: tác nhân (agent / 에이전트) may seek noisy unpredictable states forever.

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Sparse Reward and Hindsight** tiếp nhận điểm tựa từ **Exploration in High Dimensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) Shift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparse Reward and Hindsight

Hindsight Experience Replay relabels failed trajectories with goals they actually achieved, creating useful học tập (learning / 학습) tín hiệu (signal / 신호) for goal-conditioned tasks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Phân phối (distribution / 분포) Shift** tiếp nhận điểm tựa từ **Sparse Reward and Hindsight** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sim-to-Real** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) Shift

Chính sách (policy / 정책) improvement moves tác nhân (agent / 에이전트) into new trạng thái (state / 상태) distributions where hàm (function / 함수) approximator may be poorly trained. This vòng phản hồi (feedback loop / 피드백 루프) is central RL rủi ro (risk / 위험).

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Sim-to-Real** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) Shift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Offline Deep RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sim-to-Real

Robotics often train in simulation then deploy vật lý (physical / 물리적) hệ thống (system / 시스템). Simulation mismatch causes transfer gap.

Techniques:

- lĩnh vực (domain / 도메인) randomization;
- hệ thống (system / 시스템) identification;
- fine-tuning with real dữ liệu (data / 데이터);
- an toàn (safety / 안전) các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Offline Deep RL** tiếp nhận điểm tựa từ **Sim-to-Real** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Safe RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline Deep RL

Learn from logged dữ liệu (data / 데이터) only. Main challenge: chính sách (policy / 정책) may choose out-of-distribution actions whose Q-values are extrapolation errors.

Offline RL methods constrain chính sách (policy / 정책) near dữ liệu (data / 데이터) hỗ trợ (support / 지원) or learn conservative giá trị (value / 값) estimates.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Safe RL** tiếp nhận điểm tựa từ **Offline Deep RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Agent Deep RL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Safe RL

Mục tiêu (objective / 목표) may include các ràng buộc (constraints / 제약조건들):

\[
\max_\pi \mathbb E[G] \quad \văn bản (text / 텍스트){s.t.}\quad \mathbb E[C_i]\le d_i
\]

where `C_i` are costs/risks. Real các hệ thống (systems / 시스템들) cannot freely explore catastrophic actions.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Multi-Agent Deep RL** tiếp nhận điểm tựa từ **Safe RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deep RL Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Agent Deep RL

Multiple học tập (learning / 학습) agents make môi trường (environment / 환경) non-stationary from each tác nhân (agent / 에이전트)'s perspective. Centralized huấn luyện (training / 학습)/decentralized thực thi (execution / 실행) is dùng chung (common / 공통) chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Deep RL Evaluation** tiếp nhận điểm tựa từ **Multi-Agent Deep RL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward Hacking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deep RL Evaluation

Single seed kết quả (result / 결과) unreliable. Need multiple random seeds and confidence intervals because huấn luyện (training / 학습) variance high.

Also report:

- mẫu (sample / 표본) efficiency;
- final return;
- stability;
- compute/môi trường (environment / 환경) steps;
- an toàn (safety / 안전) violations;
- generalization to changed environments.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Reward Hacking** tiếp nhận điểm tựa từ **Deep RL Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deep RL and Games** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward Hacking

Strong optimizer finds loopholes. Example tác nhân (agent / 에이전트) gets reward for touching checkpoints and learns vòng lặp (loop / 루프) around same reward trigger if môi trường (environment / 환경) allows. This demonstrates specification bài toán (problem / 문제), not “malice”.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Deep RL and Games** tiếp nhận điểm tựa từ **Reward Hacking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RLHF / LLM Post-Training** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deep RL and Games

Games useful research environments because rules/rewards/simulation cheap, but success in games does not automatically transfer to open world where reward and trạng thái (state / 상태) definitions are ambiguous.

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **RLHF / LLM Post-Training** tiếp nhận điểm tựa từ **Deep RL and Games** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **The Deadly Triad Revisited** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RLHF / LLM Post-Training

Deep RL techniques like PPO have been used for language-model alignment. Important differences:

- chính sách (policy / 정책) hành động (action / 동작) is đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스);
- pretrained chính sách (policy / 정책) already powerful;
- reward mô hình (model / 모델) learned from preferences;
- KL/tham chiếu (reference / 참조) các ràng buộc (constraints / 제약조건들) keep hành vi (behavior / 동작) near cơ sở (base / 기반)/SFT mô hình (model / 모델);
- online môi trường (environment / 환경) often human/preference proxy, not physics simulator.

Hiện đại (modern / 현대적) preference tối ưu hóa (optimization / 최적화) may avoid full RL vòng lặp (loop / 루프) in some pipelines, but RL concepts remain useful for understanding chính sách (policy / 정책) tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **The Deadly Triad Revisited** tiếp nhận điểm tựa từ **RLHF / LLM Post-Training** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compute and Reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## The Deadly Triad Revisited

Deep RL frequently combines:

```text
function approximation
+ bootstrapping
+ off-policy data
```

Hence stabilizers are not incidental hacks; they address structural instability.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, **Compute and Reproducibility** tiếp nhận điểm tựa từ **The Deadly Triad Revisited** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compute and Reproducibility

Deep RL experiments depend strongly on seeds, môi trường (environment / 환경) versions, wrappers, reward preprocessing and evaluation chính sách (policy / 정책). Reproducibility requires versioning entire môi trường (environment / 환경) chuỗi xử lý (pipeline / 파이프라인), not mô hình (model / 모델) mã (code / 코드) alone.

> **Chuyển mạch:** Ở chặng này của **Deep Reinforcement học tập (learning / 학습)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Compute and Reproducibility** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Deep RL không chỉ là “neural mạng (network / 네트워크) + reward”; nó là phản hồi (feedback / 피드백) hệ thống (system / 시스템) nơi mô hình (model / 모델) quyết định dữ liệu (data / 데이터) nào nó sẽ thấy tiếp theo.**

Đây là khác biệt sâu với ordinary supervised học tập (learning / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Deep Reinforcement học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Deep RL là con đường chung để tạo intelligence”

Nó mạnh cho sequential quyết định (decision / 결정) problems nhưng mẫu (sample / 표본) chi phí (cost / 비용), reward specification và an toàn (safety / 안전) make it unsuitable for many tasks.

### “Simulation success nghĩa real-world success”

Sim-to-real gap có thể lớn.

### “Reward cao chứng minh hành vi (behavior / 동작) tốt”

Only if reward faithfully measures intended hành vi (behavior / 동작) and môi trường (environment / 환경) has no loopholes.

### “Bigger neural mạng (network / 네트워크) fixes RL instability”

Tối ưu hóa (optimization / 최적화)/dữ liệu (data / 데이터) phản hồi (feedback / 피드백) instability vẫn tồn tại.

> **Chuyển mạch:** Trong **Deep Reinforcement học tập (learning / 학습)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Deep RL nối [Neural Networks](../05_neural_networks/README.md), MDP/Bellman lý thuyết (theory / 이론), tối ưu hóa (optimization / 최적화), Agents và an toàn (safety / 안전). Đây là điểm kết thúc RL foundation; các later an toàn (safety / 안전)/alignment chapters sẽ quay lại reward specification, chính sách (policy / 정책) các ràng buộc (constraints / 제약조건들) và evaluation.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
