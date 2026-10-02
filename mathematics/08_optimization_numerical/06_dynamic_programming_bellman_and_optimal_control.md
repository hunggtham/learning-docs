# Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**. Route đi từ state/action/transition → principle of optimality → value function và Bellman equation → policy, backward induction và approximation → control/inventory/portfolio applications, để quyết định hiện tại nối với giá trị tương lai.

Nhiều tối ưu hóa (optimization / 최적화) problems không phải chọn một véc-tơ (vector / 벡터) duy nhất rồi kết thúc. Ta phải ra quyết định theo một chuỗi bước, trong đó hành động (action / 동작) hiện tại thay đổi trạng thái (state / 상태) tương lai và vì thế ảnh hưởng các lựa chọn sau. tuyến (route / 경로) planning, inventory, scheduling, reinforcement học tập (learning / 학습), điều khiển (control / 제어), portfolio rebalancing và chuỗi (sequence / 시퀀스) alignment đều có cấu trúc (structure / 구조) này.

**động (dynamic / 동적) programming — DP (동적 계획법)** là khung phần mềm (framework / 프레임워크) khai thác cấu trúc (structure / 구조) của bài toán nhiều giai đoạn bằng cách chia giá trị (value / 값) của toàn bài toán thành các subproblems liên quan.

Điểm cốt lõi không phải “dùng array để memoize”. Memoization chỉ là một hiện thực (implementation / 구현) technique. Bản chất toán học là **principle of optimality** và recursive giá trị (value / 값) decomposition.

## Trạng thái (state / 상태), hành động (action / 동작) và chuyển tiếp (transition / 전이)

Một sequential quyết định (decision / 결정) bài toán (problem / 문제) thường có trạng thái (state / 상태) `s_t`, hành động (action / 동작) `a_t`, chuyển tiếp (transition / 전이)

```math
s_{t+1}=F(s_t,a_t)
```

hoặc stochastic chuyển tiếp (transition / 전이)

```math
P(s_{t+1}\mid s_t,a_t),
```

và immediate chi phí (cost / 비용)

```math
c(s_t,a_t).
```

Mục tiêu có thể là minimize total chi phí (cost / 비용)

```math
\sum_{t=0}^{T-1} c(s_t,a_t)+g(s_T).
```

Nếu future consequence của past được summarize đầy đủ trong trạng thái hiện tại (current state / 현재 상태), ta có thể solve recursively theo trạng thái (state / 상태) thay vì enumerate toàn bộ lịch sử (history / 이력).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Principle of optimality** tiếp nhận điểm tựa từ **Trạng thái (state / 상태), hành động (action / 동작) và chuyển tiếp (transition / 전이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bellman equation cho finite horizon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Principle of optimality

Bellman's principle nói rằng nếu một chính sách (policy / 정책) là optimal từ initial trạng thái (state / 상태), thì phần còn lại của chính sách (policy / 정책) sau khi đi tới một intermediate trạng thái (state / 상태) cũng phải optimal cho subproblem bắt đầu tại trạng thái (state / 상태) đó.

Nếu suffix không optimal, ta có thể thay suffix bằng một solution tốt hơn và làm toàn solution tốt hơn, contradict optimality.

Đây là lý do optimal problems có thể tách thành optimal subproblems.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Bellman equation cho finite horizon** tiếp nhận điểm tựa từ **Principle of optimality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ shortest đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bellman equation cho finite horizon

Định nghĩa giá trị (value / 값) hàm (function / 함수)

```math
V_t(s)=\text{minimum future cost từ time }t\text{ khi current state là }s.
```

Ranh giới (boundary / 경계) điều kiện (condition / 조건):

```math
V_T(s)=g(s).
```

Recursion:

```math
V_t(s)=\min_a\left[c(s,a)+V_{t+1}(F(s,a))\right].
```

Ta solve backward từ terminal thời gian (time / 시간).

Công thức này biến exponential enumeration của hành động (action / 동작) sequences thành reuse các subproblem values nếu số states manageable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Bellman equation cho finite horizon** cho ta quy tắc; **Ví dụ shortest đường dẫn (path / 경로)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Memoization và tabulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ shortest đường dẫn (path / 경로)

Cho directed đồ thị (graph / 그래프) với edge chi phí (cost / 비용) `w(u,v)`. giá trị (value / 값) từ nút (node / 노드) `u` tới mục tiêu (target / 대상) có thể viết

```math
V(u)=\min_{v:(u,v)\in E}\left[w(u,v)+V(v)\right].
```

Đây là Bellman cấu trúc (structure / 구조). Algorithms như Bellman–Ford thực hiện relaxation dựa trên cùng idea.

Dijkstra cũng liên quan shortest-path optimal substructure nhưng khai thác nonnegative weights để chọn greedy thứ tự (order / 순서) hiệu quả hơn.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Ví dụ shortest đường dẫn (path / 경로)** cho ta quy tắc; **Memoization và tabulation** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ví dụ knapsack** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memoization và tabulation

Top-down động (dynamic / 동적) programming dùng recursive definition và bộ nhớ đệm (cache / 캐시) results. Khi subproblem được gọi lại, ta reuse cached giá trị (value / 값).

Bottom-up tabulation tính subproblems theo thứ tự đảm bảo dependencies đã có sẵn.

Hai cách có cùng recurrence nhưng hiệu năng (performance / 성능) constants và bộ nhớ (memory / 메모리) mẫu (pattern / 패턴) khác nhau.

Quan trọng nhất là xác định **trạng thái (state / 상태) minimal nhưng sufficient**. trạng thái (state / 상태) quá nhỏ mất thông tin (information / 정보) và recurrence sai; trạng thái (state / 상태) quá lớn làm độ phức tạp (complexity / 복잡도) bùng nổ.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Memoization và tabulation** cho ta quy tắc; **Ví dụ knapsack** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Overlapping subproblems** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ knapsack

Với items có weight `w_i`, giá trị (value / 값) `v_i`, sức chứa (capacity / 용량) `C`, define

```math
V(i,c)=\text{max value dùng items từ }i\text{ trở đi với remaining capacity }c.
```

Recurrence:

```math
V(i,c)=\max\left(
V(i+1,c),
\ v_i+V(i+1,c-w_i)
\right)
```

nếu `w_i≤c`.

Brute force xem `2^n` subsets. DP có khoảng `nC` states khi sức chứa (capacity / 용량) integer, nên pseudo-polynomial độ phức tạp (complexity / 복잡도).

Điều này minh họa rằng DP efficiency đến từ number of distinct states chứ không phải number of possible histories.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Ví dụ knapsack** cho ta quy tắc; **Overlapping subproblems** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Stochastic động (dynamic / 동적) programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Overlapping subproblems

Động (dynamic / 동적) programming hữu ích khi nhiều quyết định (decision / 결정) paths dẫn về cùng subproblem trạng thái (state / 상태).

Nếu subproblems hoàn toàn độc lập và không lặp, divide-and-conquer có thể phù hợp hơn.

Nếu hiện tại (current / 현재) best cục bộ (local / 로컬) hành động (action / 동작) luôn dẫn tới toàn cục (global / 전역) optimum nhờ special exchange thuộc tính (property / 속성), greedy thuật toán (algorithm / 알고리즘) có thể đơn giản hơn DP.

Chọn đúng paradigm cần nhìn cấu trúc (structure / 구조) chứ không dựa vào tên bài toán.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Stochastic động (dynamic / 동적) programming** tiếp nhận điểm tựa từ **Overlapping subproblems** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Infinite horizon và discounting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stochastic động (dynamic / 동적) programming

Nếu next trạng thái (state / 상태) random, Bellman recursion dùng expectation:

```math
V_t(s)=\min_a\left[c(s,a)+E[V_{t+1}(S_{t+1})\mid s,a]\right].
```

Nếu chuyển tiếp (transition / 전이) probabilities known,

```math
V_t(s)=\min_a\left[c(s,a)+\sum_{s'}P(s'\mid s,a)V_{t+1}(s')\right].
```

Đây là cầu nối (bridge / 브리지) trực tiếp từ tối ưu hóa (optimization / 최적화) sang Markov quyết định (decision / 결정) processes.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Infinite horizon và discounting** tiếp nhận điểm tựa từ **Stochastic động (dynamic / 동적) programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Markov quyết định (decision / 결정) tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Infinite horizon và discounting

Với infinite horizon ta thường dùng discount factor `0≤γ<1`:

```math
E\left[\sum_{t=0}^{\infty}\gamma^t r_t\right].
```

Giá trị (value / 값) hàm (function / 함수) của chính sách (policy / 정책) `π` thỏa

```math
V^\pi(s)=E_\pi\left[r(s,a)+\gamma V^\pi(S')\mid s\right].
```

Optimal giá trị (value / 값) thỏa Bellman optimality equation:

```math
V^*(s)=\max_a E\left[r(s,a)+\gamma V^*(S')\mid s,a\right].
```

Discounting vừa encode preference cho reward sớm hơn vừa giúp infinite sum finite dưới bounded rewards.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Infinite horizon và discounting** xác định đầu vào; **Markov quyết định (decision / 결정) tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Giá trị (value / 값) iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Markov quyết định (decision / 결정) tiến trình (process / 프로세스)

Một **MDP** gồm trạng thái (state / 상태) không gian (space / 공간), hành động (action / 동작) không gian (space / 공간), chuyển tiếp (transition / 전이) mô hình (model / 모델), reward hàm (function / 함수) và discount factor.

Markov giả định (assumption / 가정) nói phân phối (distribution / 분포) của next trạng thái (state / 상태) phụ thuộc trạng thái hiện tại (current state / 현재 상태)/hành động (action / 동작), không cần toàn lịch sử (history / 이력) nếu trạng thái (state / 상태) được define đúng.

Chính sách (policy / 정책)

```math
\pi(a\mid s)
```

mô tả cách chọn hành động (action / 동작) tại each trạng thái (state / 상태).

Reinforcement học tập (learning / 학습) khác classical DP chủ yếu ở việc chuyển tiếp (transition / 전이)/reward mô hình (model / 모델) có thể unknown và phải học từ tương tác (interaction / 상호작용).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Markov quyết định (decision / 결정) tiến trình (process / 프로세스)** xác định đầu vào; **Giá trị (value / 값) iteration** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chính sách (policy / 정책) iteration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giá trị (value / 값) iteration

Giá trị (value / 값) iteration lặp Bellman optimality cập nhật (update / 업데이트):

```math
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma V_k(s')\right].
```

Under finite discounted MDP conditions, Bellman operator là contraction với factor `γ`, nên iteration converge tới unique fixed điểm (point / 지점) `V*`.

Đây là liên kết (connection / 연결) sâu giữa fixed-point lý thuyết (theory / 이론) và sequential tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Chính sách (policy / 정책) iteration** tiếp nhận điểm tựa từ **Giá trị (value / 값) iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bellman equation như fixed điểm (point / 지점)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính sách (policy / 정책) iteration

Chính sách (policy / 정책) iteration alternating hai bước.

Chính sách (policy / 정책) evaluation tính `V^π` cho hiện tại (current / 현재) chính sách (policy / 정책).

Chính sách (policy / 정책) improvement chọn hành động (action / 동작) tốt hơn theo hiện tại (current / 현재) giá trị (value / 값):

```math
\pi_{new}(s)=\arg\max_a
E[r+\gamma V^\pi(S')\mid s,a].
```

Quá trình lặp tới khi chính sách (policy / 정책) không còn cải thiện.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Bellman equation như fixed điểm (point / 지점)** tiếp nhận điểm tựa từ **Chính sách (policy / 정책) iteration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deterministic optimal điều khiển (control / 제어)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bellman equation như fixed điểm (point / 지점)

Viết Bellman operator `T`:

```math
(TV)(s)=\max_a E[r+\gamma V(S')\mid s,a].
```

Optimal giá trị (value / 값) thỏa

```math
V^*=TV^*.
```

Nhìn theo fixed điểm (point / 지점) giúp kết nối động (dynamic / 동적) programming với phân tích (analysis / 분석) và numerical methods. giá trị (value / 값) iteration là repeated ứng dụng (application / 애플리케이션) của operator cho tới fixed điểm (point / 지점).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Deterministic optimal điều khiển (control / 제어)** tiếp nhận điểm tựa từ **Bellman equation như fixed điểm (point / 지점)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Curse of dimensionality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deterministic optimal điều khiển (control / 제어)

Trong điều khiển (control / 제어), trạng thái (state / 상태) dynamics có thể là

```math
x_{t+1}=f(x_t,u_t)
```

với điều khiển (control / 제어) `u_t` và chi phí (cost / 비용)

```math
\sum_t \ell(x_t,u_t).
```

Bellman equation vẫn giữ same cấu trúc (structure / 구조):

```math
V_t(x)=\min_u\left[\ell(x,u)+V_{t+1}(f(x,u))\right].
```

Nếu trạng thái (state / 상태) continuous và high-dimensional, chính xác (exact / 정확한) DP thường impossible do **curse of dimensionality**.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Curse of dimensionality** tiếp nhận điểm tựa từ **Deterministic optimal điều khiển (control / 제어)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relationship với greedy algorithms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Curse of dimensionality

Nếu mỗi trạng thái (state / 상태) dimension discretized thành `k` values và có `d` dimensions, tổng grid states là

```math
k^d.
```

Chỉ tăng dimension một chút có thể làm bộ nhớ (memory / 메모리) và computation explode exponentially.

Đây là lý do approximate động (dynamic / 동적) programming, hàm (function / 함수) approximation và reinforcement học tập (learning / 학습) quan trọng.

Neural networks trong RL có thể approximate giá trị (value / 값) hàm (function / 함수) thay vì lưu bảng (table / 테이블) cho từng trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Relationship với greedy algorithms** tiếp nhận điểm tựa từ **Curse of dimensionality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Relationship với backtracking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relationship với greedy algorithms

Greedy chọn hành động (action / 동작) tốt nhất ngay lúc này. DP chọn hành động (action / 동작) tốt nhất xét cả giá trị (value / 값) của future trạng thái (state / 상태).

Nếu mục tiêu (objective / 목표) là

```math
\text{immediate reward}+\text{future value},
```

bỏ future giá trị (value / 값) thường sai.

Greedy đúng khi bài toán (problem / 문제) có stronger cấu trúc (structure / 구조) chứng minh rằng cục bộ (local / 로컬) choice safe, như matroid cấu trúc (structure / 구조) hoặc exchange arguments trong một số problems.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Relationship với backtracking** tiếp nhận điểm tựa từ **Relationship với greedy algorithms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Relationship với backtracking

Backtracking enumerate possibilities nhưng prune khi partial solution impossible. động (dynamic / 동적) programming merge histories dẫn đến cùng trạng thái (state / 상태).

Một bài toán (problem / 문제) có thể dùng cả hai: tìm kiếm (search / 검색) over high-level choices, DP solve repeated subproblem bên trong.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Relationship với backtracking** xác định đầu vào; **Chuỗi (sequence / 시퀀스) alignment** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Tài nguyên (resource / 자원) allocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) alignment

Edit distance giữa strings là classic DP.

Define `D(i,j)` là minimum edits để biến prefix đầu `i` chars của string A thành prefix đầu `j` chars của B.

Recurrence xét insert, delete và substitute:

```math
D(i,j)=\min\begin{cases}
D(i-1,j)+1\\
D(i,j-1)+1\\
D(i-1,j-1)+[A_i\ne B_j]
\end{cases}.
```

Trạng thái (state / 상태) `(i,j)` summarize toàn relevant past. Đây là lý do exponentially many edit sequences collapse vào `O(mn)` states.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Chuỗi (sequence / 시퀀스) alignment** nêu điều cần giải thích; **Tài nguyên (resource / 자원) allocation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Optimal điều khiển (control / 제어) và Pontryagin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tài nguyên (resource / 자원) allocation

Giả sử có ngân sách (budget / 예산) `B` phân cho projects. Nếu reward dự án (project / 프로젝트) `i` khi cấp `x` units là `r_i(x)`, define

```math
V(i,b)=\text{max reward từ projects }i..n\text{ với budget }b.
```

Then

```math
V(i,b)=\max_{0\le x\le b}
\left[r_i(x)+V(i+1,b-x)\right].
```

Đây là generic mẫu (pattern / 패턴): trạng thái (state / 상태) giữ remaining tài nguyên (resource / 자원), hành động (action / 동작) chọn lượng tài nguyên (resource / 자원) cấp hiện tại.

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Tài nguyên (resource / 자원) allocation** nêu điều cần giải thích; **Optimal điều khiển (control / 제어) và Pontryagin** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hamilton–Jacobi–Bellman equation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimal điều khiển (control / 제어) và Pontryagin

Động (dynamic / 동적) programming dùng giá trị (value / 값) hàm (function / 함수) trên trạng thái (state / 상태) không gian (space / 공간). Một alternative khung phần mềm (framework / 프레임워크) trong continuous optimal điều khiển (control / 제어) là Pontryagin maximum principle, dùng costate variables và Hamiltonian.

Hai approaches nhìn cùng bài toán (problem / 문제) từ góc khác nhau. Bellman/HJB equation thiên về toàn cục (global / 전역) giá trị (value / 값) hàm (function / 함수); Pontryagin conditions thiên về necessary conditions dọc optimal trajectory.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Hamilton–Jacobi–Bellman equation** tiếp nhận điểm tựa từ **Optimal điều khiển (control / 제어) và Pontryagin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hamilton–Jacobi–Bellman equation

Trong continuous thời gian (time / 시간), Bellman principle dẫn tới HJB PDE. Với dynamics

```math
\dot x=f(x,u)
```

và running chi phí (cost / 비용) `L(x,u)`, dạng schematic là

```math
0=\min_u\left[L(x,u)+\nabla V(x)^Tf(x,u)\right]
```

cộng thời gian (time / 시간) derivative nếu finite horizon.

HJB nối tối ưu hóa (optimization / 최적화), calculus of variations, điều khiển (control / 제어) và PDE.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Hamilton–Jacobi–Bellman equation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Động (dynamic / 동적) programming biến một “cây (tree / 트리) của histories” thành một “đồ thị (graph / 그래프) của states”. Nếu nhiều histories dẫn tới cùng trạng thái (state / 상태) và future chỉ phụ thuộc trạng thái (state / 상태), ta không cần solve future lại nhiều lần. Bellman equation là statement rằng optimal total giá trị (value / 값) bằng immediate giá trị (value / 값) cộng optimal future giá trị (value / 값).

> **Chuyển mạch:** Trong **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

DP không đồng nghĩa với memoization. Memoization là kỹ thuật bộ nhớ đệm (cache / 캐시); động (dynamic / 동적) programming là structural decomposition của tối ưu hóa (optimization / 최적화) bài toán (problem / 문제).

Một nhầm lẫn khác là nghĩ mọi recurrence đều là DP. Recurrence chỉ trở thành useful DP khi trạng thái (state / 상태)/subproblem được define sao cho optimal substructure và reuse tồn tại.

Bellman equation cũng không đảm bảo computation rẻ. Với continuous hoặc high-dimensional states, chính xác (exact / 정확한) DP có thể infeasible vì curse of dimensionality.

> **Chuyển mạch:** Ở chặng này của **Động (dynamic / 동적) programming, Bellman equation và tối ưu quyết định theo nhiều bước**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Chapter này dựa trên [Recurrence and induction](../07_discrete_cs/02_recurrence_and_induction_in_algorithms.md), [Optimization](./00_optimization.md), [Stochastic processes and Markov chains](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md) và [PDE](../05_calculus/10_partial_differential_equations_and_fields_intro.md). Nó là nền toán học trực tiếp cho reinforcement học tập (learning / 학습), shortest đường dẫn (path / 경로), scheduling và optimal điều khiển (control / 제어).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
