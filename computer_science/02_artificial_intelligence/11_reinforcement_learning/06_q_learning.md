# Q-Learning

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Q-learning**. Route đi từ off-policy TD target → max over next actions → epsilon-greedy behavior → tabular convergence assumptions → function approximation limits, để Q-learning được nối với exploration và stability.

**Q-learning (Q 러닝)** là model-free, off-policy Temporal Difference điều khiển (control / 제어) thuật toán (algorithm / 알고리즘) học approximation của optimal action-value hàm (function / 함수):

\[
Q^*(s,a)
\]

Cốt lõi (core / 핵심) cập nhật (update / 업데이트):

\[
Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\left[R_{t+1}+\gamma\max_a Q(S_{t+1},a)-Q(S_t,A_t)\right]
\]

## Vì sao Q-learning mạnh?

Tác nhân (agent / 에이전트) có thể behave exploratory nhưng mục tiêu (target / 대상) cập nhật (update / 업데이트) toward greedy chính sách (policy / 정책). Đây là off-policy distinction:

```text
behavior policy → generates data
optimal greedy target → drives learning
```

Với sufficient exploration và tiêu chuẩn (standard / 표준) tabular các giả định (assumptions / 가정들), Q-learning converge tới `Q*`.

> **Chuyển mạch:** Trong **Q-Learning**, **Greedy chính sách (policy / 정책) từ Q** tiếp nhận điểm tựa từ **Vì sao Q-learning mạnh?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exploration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy chính sách (policy / 정책) từ Q

Nếu Q đã tốt:

\[
\pi(s)=\arg\max_a Q(s,a)
\]

Không cần tường minh (explicit / 명시적) chuyển tiếp (transition / 전이) mô hình (model / 모델) để chọn hành động (action / 동작).

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **Exploration** tiếp nhận điểm tựa từ **Greedy chính sách (policy / 정책) từ Q** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Off-Policy mục tiêu (target / 대상)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exploration

Nếu luôn greedy từ random initial Q, tác nhân (agent / 에이전트) có thể không discover good actions. Epsilon-greedy:

```text
random action with ε
argmax Q otherwise
```

`ε` có thể decay theo thời gian (time / 시간), nhưng decay quá nhanh dẫn tới insufficient exploration.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **Off-Policy mục tiêu (target / 대상)** tiếp nhận điểm tựa từ **Exploration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SARSA Contrast** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Off-Policy mục tiêu (target / 대상)

Q-learning mục tiêu (target / 대상):

\[
y=R+\gamma\max_{a'}Q(s',a')
\]

không depend on hành động (action / 동작) hành vi (behavior / 동작) chính sách (policy / 정책) thực sự chọn ở next step. Vì vậy tác nhân (agent / 에이전트) có thể learn greedy mục tiêu (target / 대상) while behaving exploratory.

> **Chuyển mạch:** Trong **Q-Learning**, **Off-Policy mục tiêu (target / 대상)** đã nêu tiêu chí phân biệt, còn **SARSA Contrast** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Tabular Limit** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SARSA Contrast

SARSA mục tiêu (target / 대상):

\[
R+\gamma Q(s',a'_{behavior})
\]

Trong risky môi trường (environment / 환경), SARSA có thể learn safer đường dẫn (path / 경로) under exploratory hành vi (behavior / 동작) vì nó accounts possibility of exploratory mistakes. Q-learning learns giá trị (value / 값) of ideal greedy continuation.

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **SARSA Contrast** đã nêu tiêu chí phân biệt, còn **Tabular Limit** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Overestimation độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tabular Limit

Bảng (table / 테이블) kích thước (size / 크기):

\[
|S|\times|A|
\]

không feasible cho images/continuous states. hàm (function / 함수) approximation leads to Deep Q-Networks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **Tabular Limit** đã nêu tiêu chí phân biệt, còn **Overestimation độ lệch (bias / 편향)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Experience Replay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Overestimation độ lệch (bias / 편향)

`max` over noisy estimates tends to select positive noise. Double Q-learning separates hành động (action / 동작) selection and evaluation to reduce độ lệch (bias / 편향).

> **Chuyển mạch:** Trong **Q-Learning**, **Experience Replay** tiếp nhận điểm tựa từ **Overestimation độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu (target / 대상) mạng (network / 네트워크)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Experience Replay

Deep Q-learning stores transitions:

```text
(s,a,r,s',done)
```

in replay buffer and samples mini-batches.

Benefits:

- breaks temporal correlation;
- reuses dữ liệu (data / 데이터);
- improves hardware batching.

But replay phân phối (distribution / 분포) may differ from hiện tại (current / 현재) chính sách (policy / 정책); this is compatible with off-policy học tập (learning / 학습) but creates prioritization/staleness concerns.

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **Mục tiêu (target / 대상) mạng (network / 네트워크)** tiếp nhận điểm tựa từ **Experience Replay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **DQN mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu (target / 대상) mạng (network / 네트워크)

If same mạng (network / 네트워크) both defines mục tiêu (target / 대상) and is updated every độ dốc (gradient / 기울기) step, mục tiêu (target / 대상) moves rapidly.

DQN keeps slowly updated/frozen mục tiêu (target / 대상) mạng (network / 네트워크):

\[
y=r+\gamma\max_{a'}Q_{\theta^-}(s',a')
\]

then optimize online mạng (network / 네트워크) `Q_θ` toward mục tiêu (target / 대상).

Mục tiêu (target / 대상) mạng (network / 네트워크) stabilizes bootstrapping.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **DQN mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Mục tiêu (target / 대상) mạng (network / 네트워크)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Terminal Transitions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DQN mất mát (loss / 손실)

\[
L(\theta)=\mathbb E[(y-Q_\theta(s,a))^2]
\]

or Huber mất mát (loss / 손실) often used for robustness.

> **Chuyển mạch:** Trong **Q-Learning**, **Terminal Transitions** tiếp nhận điểm tựa từ **DQN mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reward Clipping** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Terminal Transitions

If chuyển tiếp (transition / 전이) ends episode:

\[
y=r
\]

No bootstrap from terminal next trạng thái (state / 상태).

Incorrect handling `done` can độ lệch (bias / 편향) học tập (learning / 학습).

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **Reward Clipping** tiếp nhận điểm tựa từ **Terminal Transitions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuous Actions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reward Clipping

Some classic deep RL các hệ thống (systems / 시스템들) clip rewards for stability, but this changes mục tiêu (objective / 목표) by discarding magnitude thông tin (information / 정보). kỹ thuật (engineering / 엔지니어링) trick must be understood as mục tiêu (objective / 목표) transformation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **Continuous Actions** tiếp nhận điểm tựa từ **Reward Clipping** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Q-learning và Planning Analogy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuous Actions

`max_a Q(s,a)` difficult when hành động (action / 동작) continuous high-dimensional. Actor-critic methods learn tường minh (explicit / 명시적) chính sách (policy / 정책) to produce hành động (action / 동작), avoiding exhaustive argmax.

> **Chuyển mạch:** Trong **Q-Learning**, **Q-learning và Planning Analogy** tiếp nhận điểm tựa từ **Continuous Actions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Q-learning và Planning Analogy

Q giá trị (value / 값) acts like cached long-term hành động (action / 동작) utility. Classical planning computes consequence from mô hình (model / 모델); Q-learning learns it from experience.

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **Q-learning và Planning Analogy** cho ta quy tắc; **Example** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Phân phối (distribution / 분포) Shift in Replay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example

Suppose:

```text
Q(s,a)=2
r=1
max Q(s',·)=5
γ=0.9
α=0.1
```

Mục tiêu (target / 대상):

\[
1+0.9\times5=5.5
\]

Lỗi (error / 오류):

\[
3.5
\]

Cập nhật (update / 업데이트):

\[
Q(s,a)=2+0.1\times3.5=2.35
\]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **Example** cho ta quy tắc; **Phân phối (distribution / 분포) Shift in Replay** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Offline Q-Learning rủi ro (risk / 위험)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) Shift in Replay

Old buffer transitions may come from obsolete policies. Too-old dữ liệu (data / 데이터) can slow adaptation; too-recent-only dữ liệu (data / 데이터) reduces diversity. Replay thiết kế (design / 설계) is a data-engineering bài toán (problem / 문제) inside RL.

> **Chuyển mạch:** Trong **Q-Learning**, **Offline Q-Learning rủi ro (risk / 위험)** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) Shift in Replay** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Offline Q-Learning rủi ro (risk / 위험)

If dataset lacks certain actions, max may exploit overestimated unseen actions. Conservative offline RL methods penalize out-of-distribution hành động (action / 동작) values.

> **Chuyển mạch:** Ở chặng này của **Q-Learning**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Offline Q-Learning rủi ro (risk / 위험)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Q-learning học “nếu ở trạng thái (state / 상태) này và làm hành động (action / 동작) này, long-term return tốt nhất có thể từ đó là bao nhiêu?”.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Q-Learning**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Q-learning cần biết môi trường (environment / 환경) mô hình (model / 모델)”

Không; nó học from transitions.

### “Off-policy nghĩa là tác nhân (agent / 에이전트) không cần exploration”

Vẫn cần dữ liệu (data / 데이터) coverage cho relevant state-actions.

### “DQN chỉ là Q-table bằng neural mạng (network / 네트워크)”

Hàm (function / 함수) approximation thêm instability; replay/mục tiêu (target / 대상) networks là trọng yếu (critical / 중요) hệ thống (system / 시스템) changes.

> **Chuyển mạch:** Trong **Q-Learning**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Q-learning nối TD bootstrapping với Deep học tập (learning / 학습). Policy-gradient methods tiếp cận điều khiển (control / 제어) trực tiếp bằng optimizing chính sách (policy / 정책) phân phối (distribution / 분포) thay vì argmax trên Q.

Xem tiếp: [Policy Gradient](./07_policy_gradient.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
