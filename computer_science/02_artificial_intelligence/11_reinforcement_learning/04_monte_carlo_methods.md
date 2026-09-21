# Monte Carlo Methods trong Reinforcement Learning

**Phương pháp Monte Carlo (MC / 몬테카를로)** học value từ **complete sampled return** thay vì cần biết transition model của environment. Agent trải nghiệm một episode, quan sát toàn bộ reward sequence rồi dùng return thực tế làm target học.

Nếu episode từ time `t` có return:

\[
G_t = R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{T-t-1}R_T
\]

thì có thể ước lượng:

\[
V(s) \approx \text{trung bình các } G_t \text{ quan sát được sau khi đi qua } s
\]

## Vì sao Monte Carlo quan trọng?

Dynamic Programming cần biết model `P(s'|s,a)`. Monte Carlo không cần transition probability; nó chỉ cần sample trajectory từ environment.

Đây là bước chuyển quan trọng từ **planning với model đã biết** sang **learning from experience**.

## First-Visit và Every-Visit

**First-visit MC** chỉ dùng lần xuất hiện đầu tiên của một state trong mỗi episode để update.

**Every-visit MC** dùng mọi lần state xuất hiện trong episode.

Dưới các điều kiện thích hợp, cả hai có thể hội tụ về cùng expectation, nhưng finite-sample behavior và variance có thể khác nhau.

## Incremental Average

Không cần lưu toàn bộ return cũ. Có thể cập nhật running mean:

\[
V_{n+1}=V_n+\frac{1}{n+1}(G_n-V_n)
\]

Dạng tổng quát với constant step size:

\[
V\leftarrow V+\alpha(G-V)
\]

Constant `α` hữu ích trong non-stationary setting vì sample mới tiếp tục có trọng số đáng kể thay vì bị chìm dần khi số sample tăng.

## Monte Carlo Prediction

Với một policy cố định, ta generate episode theo policy đó rồi estimate state value hoặc action value từ observed return.

MC target là sample của return thật dưới policy. Nó tránh bootstrapping nhưng variance có thể cao vì chứa randomness tích lũy từ toàn bộ future trajectory.

## Không dùng Bootstrapping

MC target là:

\[
G_t
\]

và không phụ thuộc current value estimate.

Ngược lại, TD dùng target kiểu:

\[
R_{t+1}+\gamma V(S_{t+1})
\]

Do đó MC giảm bootstrap bias nhưng phải đợi outcome xa hơn và thường có variance cao hơn.

## Monte Carlo Control

Nếu học `Q(s,a)`, policy có thể được cải thiện theo hướng greedy hoặc epsilon-greedy đối với Q estimate.

Vấn đề là nếu policy trở nên deterministic quá sớm, nhiều action không còn được thử và Q của chúng không được estimate tốt.

Cần exploration, ví dụ **exploring starts** hoặc soft policy như epsilon-greedy.

## On-Policy Monte Carlo

Trong on-policy MC, behavior policy tạo dữ liệu cũng chính là policy đang được đánh giá và cải thiện.

Ví dụ agent chạy epsilon-greedy, dùng episode do policy đó tạo ra để update Q, rồi tiếp tục cải thiện cùng policy.

## Off-Policy Monte Carlo

Trong off-policy setting, ta muốn học target policy `π` từ dữ liệu do behavior policy `b` tạo ra.

Một công cụ quan trọng là **importance sampling** với tỷ lệ:

\[
\rho_{t:T-1}=\prod_{k=t}^{T-1}\frac{\pi(A_k|S_k)}{b(A_k|S_k)}
\]

Nếu `π` và `b` khác nhau nhiều, product của các ratio có thể tạo variance rất lớn.

## Trực giác của Importance Sampling

Trajectory phổ biến dưới target policy nhưng hiếm dưới behavior policy cần được tăng trọng số; trajectory phổ biến dưới behavior nhưng target policy gần như không chọn cần được giảm trọng số.

Tuy nhiên khi horizon dài, tích của nhiều ratio có thể explode hoặc collapse. Đây là một lý do off-policy Monte Carlo có thể khó dùng thực tế.

## Yêu cầu Episode

Classical Monte Carlo tự nhiên phù hợp với episodic task vì cần chờ terminal outcome để biết complete return.

Với continuing task, cần truncation hoặc formulation khác.

Temporal-Difference method có lợi thế vì có thể update online trước khi episode kết thúc.

## Bias–Variance Trade-off

Có thể so sánh trực giác:

```text
Monte Carlo
→ ít bootstrap bias hơn
→ variance cao
→ update muộn

Temporal Difference
→ có bootstrap bias
→ variance thường thấp hơn
→ update online
```

N-step return và TD(λ) tạo một continuum giữa hai cực này.

## Ví dụ

Giả sử episode:

```text
state A → reward 0
state B → reward 0
terminal → reward +1
```

Sau khi episode kết thúc, MC có thể update cả A và B bằng return chứa reward cuối `+1`.

Reward signal vì vậy được propagate qua toàn episode ngay sau completion, nhưng estimate sẽ noisy nếu terminal outcome mang nhiều randomness.

## Monte Carlo như công cụ ước lượng tổng quát

Ngoài RL, Monte Carlo là phương pháp tính toán tổng quát để estimate expectation bằng sample:

\[
\mathbb E[f(X)]\approx \frac1N\sum_{i=1}^N f(x_i)
\]

Trong RL, sample không chỉ là điểm dữ liệu độc lập mà thường là trajectory có cấu trúc theo thời gian.

## Mô hình tư duy

> **Monte Carlo nói: thay vì ước lượng future value từ một value estimate khác, hãy quan sát outcome của trajectory rồi dùng sampled return thật làm target.**

## Những nhầm lẫn thường gặp

### “Monte Carlo nghĩa là action luôn random”

Không. “Monte Carlo” ở đây nói tới việc dùng sample để estimate expectation; policy có thể có cấu trúc rõ và không cần chọn action hoàn toàn ngẫu nhiên.

### “MC hoàn toàn không có bias”

Không nên hiểu tuyệt đối. Complete return có thể là unbiased sample dưới các giả định phù hợp, nhưng truncation, finite data và function approximation vẫn có thể tạo bias hoặc estimation error.

### “MC luôn tốt hơn TD vì dùng outcome thật”

Không. Variance cao và delayed update có thể làm sample efficiency kém hơn đáng kể.

## Liên kết kiến thức

Monte Carlo nối statistical estimation với sequential experience. Temporal-Difference Learning ở chapter tiếp theo kết hợp sampling của Monte Carlo với bootstrapping của Dynamic Programming.

Xem tiếp: [Temporal-Difference Learning](./05_temporal_difference_learning.md).