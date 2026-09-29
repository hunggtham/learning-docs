# Động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)

> **Mạch đọc:** Đặt **động (dynamic / 동적) Programming trong Reinforcement học tập (learning / 학습)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **chính sách (policy / 정책) Evaluation** sang **chính sách (policy / 정책) Improvement**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**động (dynamic / 동적) Programming (DP / 동적 계획법)** giải MDP khi chuyển tiếp (transition / 전이) mô hình (model / 모델) và reward mô hình (model / 모델) đã biết. Ý tưởng là exploit Bellman recursion để chia long-horizon quyết định (decision / 결정) bài toán (problem / 문제) thành các subproblems liên kết qua giá trị (value / 값) functions.

DP không phải “huấn luyện (training / 학습) từ dữ liệu (data / 데이터)” theo nghĩa hiện đại (modern / 현대적) ML. Nó là chính xác (exact / 정확한)/planning-style computation trên known mô hình (model / 모델), nhưng concepts của nó là foundation cho RL.

## Chính sách (policy / 정책) Evaluation

Với chính sách (policy / 정책) cố định `π`, lặp Bellman expectation backup:

\[
V_{k+1}(s)=\sum_a\pi(a|s)\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Under tiêu chuẩn (standard / 표준) finite discounted MDP các giả định (assumptions / 가정들), chuỗi (sequence / 시퀀스) converge tới `V^π`.

## Chính sách (policy / 정책) Improvement

Sau khi có giá trị (value / 값) estimate, chọn hành động (action / 동작) greedy:

\[
\pi'(s)=\arg\max_a\sum_{s'}P(s'|s,a)[R+\gamma V^\pi(s')]
\]

Chính sách (policy / 정책) improvement theorem cho biết chính sách (policy / 정책) mới không tệ hơn chính sách (policy / 정책) cũ.

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

## Giá trị (value / 값) Iteration

Kết hợp evaluation và improvement trực tiếp:

\[
V_{k+1}(s)=\max_a\sum_{s'}P(s'|s,a)[R+\gamma V_k(s')]
\]

Sau convergence, extract greedy chính sách (policy / 정책).

## Synchronous vs Asynchronous Updates

Synchronous dùng old véc-tơ (vector / 벡터) `V_k` để cập nhật (update / 업데이트) all states.

Asynchronous/in-place cập nhật trạng thái (state / 상태) từng phần và dùng latest values ngay. Có thể converge nhanh hơn nếu scheduling tốt.

## Generalized chính sách (policy / 정책) Iteration

Một mô hình tư duy (mental model / 사고 모델) rộng:

```text
policy evaluation pushes value toward truth under current policy
policy improvement pushes policy toward greedy wrt current value
```

Hai processes tương tác cho tới consistency.

Nhiều RL algorithms hiện đại có thể nhìn như approximate Generalized chính sách (policy / 정책) Iteration.

## Computational chi phí (cost / 비용)

Tabular DP cần sweep qua trạng thái (state / 상태)/hành động (action / 동작)/chuyển tiếp (transition / 전이) spaces. Nếu trạng thái (state / 상태) không gian (space / 공간) khổng lồ, chi phí (cost / 비용) không khả thi.

Đây là **curse of dimensionality**: số states tăng combinatorially theo dimensions.

RL/hàm (function / 함수) approximation xuất hiện một phần vì không thể enumerate toàn trạng thái (state / 상태) không gian (space / 공간).

## Known mô hình (model / 모델) giả định (assumption / 가정)

DP cần `P` và `R`. Trong real world chúng thường unknown hoặc too complex.

Model-based RL có thể học approximate mô hình (model / 모델) rồi dùng planning/DP-like methods.

## Example: Gridworld

Grid cells là states; actions up/down/left/right; chuyển tiếp (transition / 전이) deterministic hoặc stochastic; reward -1 mỗi step.

Giá trị (value / 값) iteration propagate distance-to-goal thông tin (information / 정보) backward từ terminal cells. giá trị (value / 값) surfaces dần encode “trạng thái (state / 상태) này gần đường tốt tới goal đến đâu”.

## Bellman Operator

Define optimal Bellman operator `T`:

\[
(TV)(s)=\max_a\mathbb E[R+\gamma V(S')]
\]

Trong discounted finite MDP, `T` là contraction dưới sup norm với factor `γ`, giải thích convergence của giá trị (value / 값) iteration.

## DP và Shortest đường dẫn (path / 경로)

Deterministic shortest-path algorithms có related recursive cấu trúc (structure / 구조). Bellman-Ford cũng repeatedly relax edges. RL generalizes intuition sang stochastic dynamics + rewards.

## DP và Planning

Classical planning tìm kiếm (search / 검색) enumerates trajectories; DP reuses trạng thái (state / 상태) values across many possible trajectories. Khi nhiều paths merge vào same trạng thái (state / 상태), giá trị (value / 값) reuse rất powerful.

## Limitations

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

- cần known model;
- state enumeration;
- exact expectation có thể expensive;
- model errors propagate;
- partial observability cần richer belief-state formulation.

## Mô hình tư duy (mental model / 사고 모델)

> **động (dynamic / 동적) Programming là Bellman recursion khi ta có map đầy đủ của môi trường (environment / 환경); Reinforcement học tập (learning / 학습) học khi map không đầy đủ và chỉ thấy samples.**

## Dùng chung (common / 공통) Misconceptions

### “DP là một RL thuật toán (algorithm / 알고리즘) online”

DP thường giả định known mô hình (model / 모델) và full sweeps, nên gần planning hơn học tập (learning / 학습) from unknown môi trường (environment / 환경).

### “giá trị (value / 값) iteration luôn nhanh”

Convergence mathematical không có nghĩa practical chi phí (cost / 비용) thấp trên huge trạng thái (state / 상태) spaces.

### “chính sách (policy / 정책) iteration luôn cần chính xác (exact / 정확한) evaluation”

Approximate/partial evaluation vẫn có thể tạo useful variants.

## Liên kết kiến thức (knowledge connection / 지식 연결)

DP nối Bellman equations với sample-based methods. Monte Carlo sẽ bỏ known chuyển tiếp (transition / 전이) mô hình (model / 모델) và dùng complete sampled returns.

Xem tiếp: [Monte Carlo Methods](./04_monte_carlo_methods.md).
