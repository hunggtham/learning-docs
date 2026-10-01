# Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chính sách (policy / 정책) Evaluation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chính sách (policy / 정책) Improvement** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**động (dynamic / 동적) Programming (DP / 동적 계획법)** giải MDP khi chuyển tiếp (transition / 전이) mô hình (model / 모델) và reward mô hình (model / 모델) đã biết. Ý tưởng là exploit Bellman recursion để chia long-horizon quyết định (decision / 결정) bài toán (problem / 문제) thành các subproblems liên kết qua giá trị (value / 값) functions.

DP không phải “huấn luyện (training / 학습) từ dữ liệu (data / 데이터)” theo nghĩa hiện đại (modern / 현대적) ML. Nó là chính xác (exact / 정확한)/planning-style computation trên known mô hình (model / 모델), nhưng concepts của nó là foundation cho RL.

## Chính sách (policy / 정책) Evaluation

Với chính sách (policy / 정책) cố định `π`, lặp Bellman expectation backup:

\[
V_{k+1}(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Under tiêu chuẩn (standard / 표준) finite discounted MDP các giả định (assumptions / 가정들), chuỗi (sequence / 시퀀스) converge tới `V^π`.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Chính sách (policy / 정책) Improvement** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính sách (policy / 정책) Iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) Improvement

Sau khi có giá trị (value / 값) estimate, chọn hành động (action / 동작) greedy:

\[
\pi'(s)=\arg\max_a\sum_{s'}P(s'|s,a)[R+\gamma V^\pi(s')]
\]

Chính sách (policy / 정책) improvement theorem cho biết chính sách (policy / 정책) mới không tệ hơn chính sách (policy / 정책) cũ.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Chính sách (policy / 정책) Iteration** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) Improvement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giá trị (value / 값) Iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) Iteration

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
initialize π
repeat:
    evaluate V^π
    improve π greedily
until stable
```

Evaluation không nhất thiết phải converge hoàn toàn mỗi iteration; modified chính sách (policy / 정책) iteration có thể xen kẽ partial updates.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Giá trị (value / 값) Iteration** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) Iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synchronous vs Asynchronous Updates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giá trị (value / 값) Iteration

Kết hợp evaluation và improvement trực tiếp:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Sau convergence, extract greedy chính sách (policy / 정책).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Synchronous vs Asynchronous Updates** tiếp nhận điểm tựa từ **Giá trị (value / 값) Iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Generalized chính sách (policy / 정책) Iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synchronous vs Asynchronous Updates

Synchronous dùng old véc-tơ (vector / 벡터) `V_k` để cập nhật (update / 업데이트) all states.

Asynchronous/in-place cập nhật trạng thái (state / 상태) từng phần và dùng latest values ngay. Có thể converge nhanh hơn nếu scheduling tốt.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Generalized chính sách (policy / 정책) Iteration** tiếp nhận điểm tựa từ **Synchronous vs Asynchronous Updates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Computational chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generalized chính sách (policy / 정책) Iteration

Một mô hình tư duy (mental model / 사고 모델) rộng:

```text
policy evaluation pushes value toward truth under current policy
policy improvement pushes policy toward greedy wrt current value
```

Hai processes tương tác cho tới consistency.

Nhiều RL algorithms hiện đại có thể nhìn như approximate Generalized chính sách (policy / 정책) Iteration.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Computational chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Generalized chính sách (policy / 정책) Iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Known mô hình (model / 모델) giả định (assumption / 가정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Computational chi phí (cost / 비용)

Tabular DP cần sweep qua trạng thái (state / 상태)/hành động (action / 동작)/chuyển tiếp (transition / 전이) spaces. Nếu trạng thái (state / 상태) không gian (space / 공간) khổng lồ, chi phí (cost / 비용) không khả thi.

Đây là **curse of dimensionality**: số states tăng combinatorially theo dimensions.

RL/hàm (function / 함수) approximation xuất hiện một phần vì không thể enumerate toàn trạng thái (state / 상태) không gian (space / 공간).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Known mô hình (model / 모델) giả định (assumption / 가정)** tiếp nhận điểm tựa từ **Computational chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: Gridworld** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Known mô hình (model / 모델) giả định (assumption / 가정)

DP cần `P` và `R`. Trong real world chúng thường unknown hoặc too complex.

Model-based RL có thể học approximate mô hình (model / 모델) rồi dùng planning/DP-like methods.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Known mô hình (model / 모델) giả định (assumption / 가정)** cho ta quy tắc; **Example: Gridworld** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Bellman Operator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: Gridworld

Grid cells là states; actions up/down/left/right; chuyển tiếp (transition / 전이) deterministic hoặc stochastic; reward -1 mỗi step.

Giá trị (value / 값) iteration propagate distance-to-goal thông tin (information / 정보) backward từ terminal cells. giá trị (value / 값) surfaces dần encode “trạng thái (state / 상태) này gần đường tốt tới goal đến đâu”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Example: Gridworld** cho ta quy tắc; **Bellman Operator** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **DP và Shortest đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bellman Operator

Define optimal Bellman operator `T`:

\[
(TV)(s)=\max_a\mathbb E[R+\gamma V(S')]
\]

Trong discounted finite MDP, `T` là contraction dưới sup norm với factor `γ`, giải thích convergence của giá trị (value / 값) iteration.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Bellman Operator** xác định đầu vào; **DP và Shortest đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **DP và Planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP và Shortest đường dẫn (path / 경로)

Deterministic shortest-path algorithms có related recursive cấu trúc (structure / 구조). Bellman-Ford cũng repeatedly relax edges. RL generalizes intuition sang stochastic dynamics + rewards.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **DP và Shortest đường dẫn (path / 경로)** xác định đầu vào; **DP và Planning** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Limitations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## DP và Planning

Classical planning tìm kiếm (search / 검색) enumerates trajectories; DP reuses trạng thái (state / 상태) values across many possible trajectories. Khi nhiều paths merge vào same trạng thái (state / 상태), giá trị (value / 값) reuse rất powerful.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **DP và Planning** đã nêu tiêu chí phân biệt, còn **Limitations** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Limitations

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- cần known model;
- state enumeration;
- exact expectation có thể expensive;
- model errors propagate;
- partial observability cần richer belief-state formulation.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Limitations** đã nêu tiêu chí phân biệt, còn **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **động (dynamic / 동적) Programming là Bellman recursion khi ta có map đầy đủ của môi trường (environment / 환경); Reinforcement học tập (learning / 학습) học khi map không đầy đủ và chỉ thấy samples.**

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “DP là một RL thuật toán (algorithm / 알고리즘) online”

DP thường giả định known mô hình (model / 모델) và full sweeps, nên gần planning hơn học tập (learning / 학습) from unknown môi trường (environment / 환경).

### “giá trị (value / 값) iteration luôn nhanh”

Convergence mathematical không có nghĩa practical chi phí (cost / 비용) thấp trên huge trạng thái (state / 상태) spaces.

### “chính sách (policy / 정책) iteration luôn cần chính xác (exact / 정확한) evaluation”

Approximate/partial evaluation vẫn có thể tạo useful variants.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

DP nối Bellman equations với sample-based methods. Monte Carlo sẽ bỏ known chuyển tiếp (transition / 전이) mô hình (model / 모델) và dùng complete sampled returns.

Xem tiếp: [Monte Carlo Methods](./04_monte_carlo_methods.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
