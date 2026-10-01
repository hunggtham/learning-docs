# Monte Carlo Methods trong Reinforcement học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao Monte Carlo quan trọng?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **First-Visit và Every-Visit** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Monte Carlo (MC / 몬테카를로)** methods học giá trị (value / 값) từ **complete sampled returns** thay vì cần known chuyển tiếp (transition / 전이) mô hình (model / 모델). tác nhân (agent / 에이전트) trải nghiệm episode, quan sát reward chuỗi (sequence / 시퀀스), rồi dùng return thực tế như mục tiêu (target / 대상).

Nếu episode từ thời gian (time / 시간) `t` có return:

\[
G_t = R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{T-t-1}R_T
\]

thì có thể estimate:

\[
V(s) \approx \văn bản (text / 텍스트){average of observed } G_t \văn bản (text / 텍스트){ after visiting } s
\]

## Vì sao Monte Carlo quan trọng?

Động (dynamic / 동적) Programming cần mô hình (model / 모델) `P(s'|s,a)`. Monte Carlo không cần chuyển tiếp (transition / 전이) probabilities; chỉ cần sampled trajectories.

Điều này là bước chuyển quan trọng từ planning with mô hình (model / 모델) sang học tập (learning / 학습) from experience.

> **Chuyển mạch:** Trong **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **First-Visit và Every-Visit** tiếp nhận điểm tựa từ **Vì sao Monte Carlo quan trọng?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Incremental Average** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## First-Visit và Every-Visit

**First-visit MC** cập nhật (update / 업데이트) trạng thái (state / 상태) từ lần xuất hiện đầu tiên trong episode.

**Every-visit MC** cập nhật (update / 업데이트) từ mọi lần trạng thái (state / 상태) xuất hiện.

Cả hai có thể converge under appropriate conditions; finite-sample hành vi (behavior / 동작) khác nhau.

> **Chuyển mạch:** Ở chặng này của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Incremental Average** tiếp nhận điểm tựa từ **First-Visit và Every-Visit** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monte Carlo Prediction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Incremental Average

Không cần lưu toàn returns. Running mean:

\[
V_{n+1}=V_n+\frac{1}{n+1}(G_n-V_n)
\]

Generalized constant step kích thước (size / 크기):

\[
V\leftarrow V+\alpha(G-V)
\]

Constant `α` phù hợp non-stationary settings vì recent samples có weight lâu dài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Monte Carlo Prediction** tiếp nhận điểm tựa từ **Incremental Average** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **No Bootstrapping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monte Carlo Prediction

Với chính sách (policy / 정책) cố định, generate episodes theo chính sách (policy / 정책) rồi estimate trạng thái (state / 상태)/hành động (action / 동작) values từ observed returns.

MC mục tiêu (target / 대상) là unbiased estimate của return under chính sách (policy / 정책), nhưng variance có thể cao vì chứa randomness từ toàn bộ future trajectory.

> **Chuyển mạch:** Trong **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **No Bootstrapping** tiếp nhận điểm tựa từ **Monte Carlo Prediction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monte Carlo điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## No Bootstrapping

MC mục tiêu (target / 대상):

\[
G_t
\]

không dùng hiện tại (current / 현재) giá trị (value / 값) estimate.

Contrast với TD:

\[
R_{t+1}+\gamma V(S_{t+1})
\]

MC tránh bootstrap độ lệch (bias / 편향) nhưng chờ episode kết thúc và có higher variance.

> **Chuyển mạch:** Ở chặng này của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Monte Carlo điều khiển (control / 제어)** tiếp nhận điểm tựa từ **No Bootstrapping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **On-Policy MC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monte Carlo điều khiển (control / 제어)

Nếu học `Q(s,a)`, chính sách (policy / 정책) có thể improve greedily/epsilon-greedily.

Bài toán (problem / 문제): nếu chính sách (policy / 정책) trở nên deterministic quá sớm, nhiều actions không được thử. Need **exploring starts** hoặc soft policies như epsilon-greedy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **On-Policy MC** tiếp nhận điểm tựa từ **Monte Carlo điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Off-Policy MC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## On-Policy MC

Hành vi (behavior / 동작) chính sách (policy / 정책) và mục tiêu (target / 대상) chính sách (policy / 정책) giống nhau. tác nhân (agent / 에이전트) generate dữ liệu (data / 데이터) theo epsilon-greedy chính sách (policy / 정책) và improve chính chính sách (policy / 정책) đó.

> **Chuyển mạch:** Trong **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Off-Policy MC** tiếp nhận điểm tựa từ **On-Policy MC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Importance Sampling Intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Off-Policy MC

Muốn evaluate/learn mục tiêu (target / 대상) chính sách (policy / 정책) `π` từ dữ liệu (data / 데이터) generated by hành vi (behavior / 동작) chính sách (policy / 정책) `b`.

Use **importance sampling** ratio:

\[
\rho_{t:T-1}=\prod_{k=t}^{T-1}\frac{\pi(A_k|S_k)}{b(A_k|S_k)}
\]

Nếu policies khác nhiều, ratio variance rất lớn.

> **Chuyển mạch:** Ở chặng này của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Importance Sampling Intuition** tiếp nhận điểm tựa từ **Off-Policy MC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Episodic yêu cầu (requirement / 요구사항)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Importance Sampling Intuition

Trajectory dùng chung (common / 공통) dưới mục tiêu (target / 대상) chính sách (policy / 정책) nhưng rare dưới hành vi (behavior / 동작) chính sách (policy / 정책) cần upweight, và ngược lại.

Nhưng sản phẩm (product / 제품) of many ratios có thể explode/collapse, khiến long-horizon off-policy MC difficult.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Episodic yêu cầu (requirement / 요구사항)** tiếp nhận điểm tựa từ **Importance Sampling Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ lệch (bias / 편향)–Variance sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Episodic yêu cầu (requirement / 요구사항)

Classical MC naturally chờ terminal episode. Continuing tasks cần artificial truncation hoặc other formulations.

TD methods có lợi vì cập nhật (update / 업데이트) online before episode ends.

> **Chuyển mạch:** Trong **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Độ lệch (bias / 편향)–Variance sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Episodic yêu cầu (requirement / 요구사항)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ lệch (bias / 편향)–Variance sự đánh đổi (trade-off / 트레이드오프)

MC:

```text
little bootstrap bias
high variance
late updates
```

TD:

```text
bootstrap bias
lower variance
online updates
```

N-step returns và TD(λ) tạo continuum giữa hai extremes.

> **Chuyển mạch:** Ở chặng này của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Độ lệch (bias / 편향)–Variance sự đánh đổi (trade-off / 트레이드오프)** cho ta quy tắc; **Example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Monte Carlo và Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example

Episode rewards:

```text
state A → 0
state B → 0
terminal → +1
```

MC cập nhật (update / 업데이트) A và B bằng return chứa final +1. Reward tín hiệu (signal / 신호) propagate toàn episode ngay sau completion, nhưng estimate noisy nếu outcomes stochastic.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Example** cho ta quy tắc; **Monte Carlo và Evaluation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monte Carlo và Evaluation

Ngoài RL học tập (learning / 학습), Monte Carlo sampling là general computational công cụ (tool / 도구) để estimate expectation:

\[
\mathbb E[f(X)]\approx \frac1N\sum_{i=1}^N f(x_i)
\]

RL use is special trường hợp (case / 사례) where samples are trajectories.

> **Chuyển mạch:** Trong **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Monte Carlo và Evaluation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Monte Carlo nói: đừng đoán giá trị (value / 값) từ giá trị (value / 값) estimate khác; hãy chơi hết episode và dùng kết quả (outcome / 결과) thực tế.**

> **Chuyển mạch:** Ở chặng này của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Monte Carlo luôn random hành động (action / 동작)”

Không. “Monte Carlo” ở đây nói dùng sampled returns; chính sách (policy / 정책) có thể structured.

### “MC không có độ lệch (bias / 편향)”

Return mẫu (sample / 표본) có thể unbiased under các giả định (assumptions / 가정들), nhưng finite dữ liệu (data / 데이터), truncation và hàm (function / 함수) approximation vẫn tạo issues.

### “MC tốt hơn TD vì dùng real kết quả (outcome / 결과)”

High variance và delayed cập nhật (update / 업데이트) có thể làm học tập (learning / 학습) kém sample-efficient.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Monte Carlo Methods trong Reinforcement học tập (learning / 학습)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Monte Carlo nối statistical estimation với sequential experience. Temporal Difference sẽ kết hợp sampling của MC với bootstrapping của DP.

Xem tiếp: [Temporal Difference Learning](./05_temporal_difference_learning.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
