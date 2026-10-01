# Chính sách (policy / 정책) độ dốc (gradient / 기울기)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao optimize chính sách (policy / 정책) trực tiếp?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Log-Derivative Trick** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Value-based methods như Q-learning học hành động (action / 동작) values rồi suy ra chính sách (policy / 정책). **chính sách (policy / 정책) độ dốc (gradient / 기울기)** optimize chính sách (policy / 정책) parameters trực tiếp.

Một stochastic chính sách (policy / 정책):

\[
\pi_\theta(a|s)
\]

Mục tiêu (objective / 목표):

\[
J(\theta)=\mathbb E_{\tau\sim\pi_\theta}[G(\tau)]
\]

Ta muốn độ dốc (gradient / 기울기):

\[
\nabla_\theta J(\theta)
\]

để tăng expected return.

## Vì sao optimize chính sách (policy / 정책) trực tiếp?

Trong continuous hành động (action / 동작) spaces, việc tính `argmax_a Q(s,a)` có thể khó. chính sách (policy / 정책) mạng (network / 네트워크) có thể đầu ra (output / 출력) hành động (action / 동작) phân phối (distribution / 분포) trực tiếp.

Ngoài ra stochastic chính sách (policy / 정책) hữu ích khi optimal hành vi (behavior / 동작) inherently mixed hoặc exploration cần built-in randomness.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Log-Derivative Trick** tiếp nhận điểm tựa từ **Vì sao optimize chính sách (policy / 정책) trực tiếp?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **REINFORCE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log-Derivative Trick

Một key định danh (identity / 식별자):

\[
\nabla_\theta \pi_\theta(a|s)=\pi_\theta(a|s)\nabla_\theta\log\pi_\theta(a|s)
\]

Policy-gradient theorem dẫn tới estimator dạng:

\[
\nabla_\theta J(\theta)\propto \mathbb E[ G_t\nabla_\theta\log\pi_\theta(A_t|S_t)]
\]

Intuition:

- hành động (action / 동작) dẫn tới return cao → tăng log-probability;
- hành động (action / 동작) dẫn tới return thấp → giảm relative preference.

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **REINFORCE** tiếp nhận điểm tựa từ **Log-Derivative Trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Baseline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## REINFORCE

Classic Monte Carlo policy-gradient thuật toán (algorithm / 알고리즘) dùng complete return:

\[
\theta\leftarrow\theta+\alpha G_t\nabla_\theta\log\pi_\theta(A_t|S_t)
\]

Simple nhưng variance cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Baseline** tiếp nhận điểm tựa từ **REINFORCE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Baseline Reduces Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Baseline

Subtract baseline `b(s)` mà không introduce độ lệch (bias / 편향) under tiêu chuẩn (standard / 표준) conditions:

\[
(G_t-b(S_t))\nabla\log\pi(A_t|S_t)
\]

Natural baseline là giá trị (value / 값) hàm (function / 함수) `V(s)`.

Khi baseline là `V`, term gần advantage:

\[
A(s,a)=Q(s,a)-V(s)
\]

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Why Baseline Reduces Variance** tiếp nhận điểm tựa từ **Baseline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책) Parameterization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Baseline Reduces Variance

Nếu episode overall high reward, không phải mọi hành động (action / 동작) đều equally good. Baseline giúp measure hành động (action / 동작) hiệu năng (performance / 성능) relative to expected trạng thái (state / 상태) giá trị (value / 값).

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Chính sách (policy / 정책) Parameterization** tiếp nhận điểm tựa từ **Why Baseline Reduces Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Entropy Regularization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) Parameterization

Discrete actions:

```text
network logits → softmax → action distribution
```

Continuous actions:

```text
network outputs μ(s), σ(s)
→ sample Gaussian action
```

Phân phối (distribution / 분포) choice là inductive độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Entropy Regularization** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) Parameterization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **On-Policy Nature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Entropy Regularization

Để chính sách (policy / 정책) không collapse quá sớm:

\[
J'=J+\beta H(\pi(\cdot|s))
\]

Entropy bonus encourage exploration.

Nhưng quá nhiều entropy làm chính sách (policy / 정책) remain random.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **On-Policy Nature** tiếp nhận điểm tựa từ **Entropy Regularization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Importance Ratios** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## On-Policy Nature

Vanilla chính sách (policy / 정책) độ dốc (gradient / 기울기) thường on-policy: dữ liệu (data / 데이터) generated bởi old chính sách (policy / 정책) nhanh stale khi chính sách (policy / 정책) parameters thay đổi (change / 변경).

Điều này giảm mẫu (sample / 표본) efficiency so với replay-heavy off-policy methods.

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Importance Ratios** tiếp nhận điểm tựa từ **On-Policy Nature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **PPO Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Importance Ratios

Khi cập nhật (update / 업데이트) từ dữ liệu (data / 데이터) generated by old chính sách (policy / 정책), ratio:

\[
r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
\]

xuất hiện trong algorithms như PPO. Ratio đo chính sách (policy / 정책) mới thay đổi xác suất (probability / 확률) của sampled hành động (action / 동작) bao nhiêu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **PPO Intuition** tiếp nhận điểm tựa từ **Importance Ratios** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trust Region Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## PPO Intuition

**Proximal chính sách (policy / 정책) tối ưu hóa (optimization / 최적화) (PPO)** hạn chế cập nhật (update / 업데이트) quá lớn bằng clipped surrogate mục tiêu (objective / 목표):

\[
L^{clip}=\mathbb E[\min(r_tA_t,\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A_t)]
\]

Goal: improve chính sách (policy / 정책) nhưng tránh một độ dốc (gradient / 기울기) step làm phân phối (distribution / 분포) thay đổi catastrophic.

PPO được dùng rộng vì relative simplicity/stability, bao gồm một số RLHF pipelines.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Trust Region Intuition** tiếp nhận điểm tựa từ **PPO Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Credit Assignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trust Region Intuition

Chính sách (policy / 정책) cập nhật (update / 업데이트) quá lớn khiến dữ liệu (data / 데이터) collected under old chính sách (policy / 정책) không còn represent new chính sách (policy / 정책). Trust-region/proximal methods enforce cục bộ (local / 로컬) thay đổi (change / 변경).

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Credit Assignment** tiếp nhận điểm tựa từ **Trust Region Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Generalized Advantage Estimation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Credit Assignment

Chính sách (policy / 정책) gradients still face delayed rewards. Advantage estimators và critics propagate credit more efficiently.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Generalized Advantage Estimation** tiếp nhận điểm tựa từ **Credit Assignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ dốc (gradient / 기울기) Variance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generalized Advantage Estimation

GAE blends multi-step TD errors:

\[
\hat A_t^{GAE(\gamma,\lambda)}=\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}
\]

Sự đánh đổi (trade-off / 트레이드오프) độ lệch (bias / 편향) vs variance controlled partly by `λ`.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Độ dốc (gradient / 기울기) Variance** tiếp nhận điểm tựa từ **Generalized Advantage Estimation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ dốc (gradient / 기울기) Variance

Stochastic trajectories make gradients noisy. Techniques:

- larger batches;
- baselines;
- advantage normalization;
- GAE;
- reward normalization;
- entropy tuning.

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Reward quy mô (scale / 규모)** tiếp nhận điểm tựa từ **Độ dốc (gradient / 기울기) Variance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책) Collapse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward quy mô (scale / 규모)

Độ dốc (gradient / 기울기) magnitude depends reward/advantage quy mô (scale / 규모). Poor scaling destabilizes học tập (learning / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Chính sách (policy / 정책) Collapse** tiếp nhận điểm tựa từ **Reward quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RLHF liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) Collapse

Aggressive tối ưu hóa (optimization / 최적화) toward imperfect reward can collapse diversity or exploit reward mô hình (model / 모델). KL các ràng buộc (constraints / 제약조건들)/tham chiếu (reference / 참조) policies in alignment help limit drift.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, sau nội dung của **Chính sách (policy / 정책) Collapse**, **RLHF liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RLHF liên kết (connection / 연결)

LLM chính sách (policy / 정책) is đơn vị từ (token / 토큰) phân phối (distribution / 분포). PPO-like RLHF can optimize sequence-level reward while constraining divergence from tham chiếu (reference / 참조) mô hình (model / 모델):

\[
Reward'=Reward_{pref}-\beta D_{KL}(\pi_\theta\|\pi_{ref})
\]

Đây là special ứng dụng (application / 애플리케이션), không phải definition của chính sách (policy / 정책) độ dốc (gradient / 기울기).

> **Chuyển mạch:** Ở chặng này của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **RLHF liên kết (connection / 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **chính sách (policy / 정책) độ dốc (gradient / 기울기) tăng xác suất những hành động (action / 동작) đã dẫn tới kết quả (outcome / 결과) tốt và giảm xác suất những hành động (action / 동작) tương đối tệ, bằng độ dốc (gradient / 기울기) trên log-probability.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “chính sách (policy / 정책) độ dốc (gradient / 기울기) không cần giá trị (value / 값) hàm (function / 함수)”

Vanilla REINFORCE không bắt buộc, nhưng critics/baselines greatly improve variance.

### “PPO đảm bảo chính sách (policy / 정책) an toàn”

Clipping/KL chỉ giới hạn cập nhật (update / 업데이트) kích thước (size / 크기), không đảm bảo reward đúng hay hành vi (behavior / 동작) safe.

### “Direct chính sách (policy / 정책) tối ưu hóa (optimization / 최적화) luôn tốt hơn Q-learning”

Trade-offs depend hành động (action / 동작) không gian (space / 공간), mẫu (sample / 표본) efficiency và stability.

> **Chuyển mạch:** Trong **Chính sách (policy / 정책) độ dốc (gradient / 기울기)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chính sách (policy / 정책) độ dốc (gradient / 기울기) nối stochastic tối ưu hóa (optimization / 최적화), xác suất (probability / 확률) distributions và RL điều khiển (control / 제어). Actor-Critic kết hợp chính sách (policy / 정책) độ dốc (gradient / 기울기) với learned giá trị (value / 값) estimator.

Xem tiếp: [Actor-Critic](./08_actor_critic.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
