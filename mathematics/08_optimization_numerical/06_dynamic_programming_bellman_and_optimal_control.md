# Dynamic programming, Bellman equation và tối ưu quyết định theo nhiều bước

Nhiều optimization problems không phải chọn một vector duy nhất rồi kết thúc. Ta phải ra quyết định theo một chuỗi bước, trong đó action hiện tại thay đổi state tương lai và vì thế ảnh hưởng các lựa chọn sau. Route planning, inventory, scheduling, reinforcement learning, control, portfolio rebalancing và sequence alignment đều có structure này.

**Dynamic programming — DP (동적 계획법)** là framework khai thác structure của bài toán nhiều giai đoạn bằng cách chia value của toàn bài toán thành các subproblems liên quan.

Điểm cốt lõi không phải “dùng array để memoize”. Memoization chỉ là một implementation technique. Bản chất toán học là **principle of optimality** và recursive value decomposition.

## State, action và transition

Một sequential decision problem thường có state `s_t`, action `a_t`, transition

```math
s_{t+1}=F(s_t,a_t)
```

hoặc stochastic transition

```math
P(s_{t+1}\mid s_t,a_t),
```

và immediate cost

```math
c(s_t,a_t).
```

Mục tiêu có thể là minimize total cost

```math
\sum_{t=0}^{T-1} c(s_t,a_t)+g(s_T).
```

Nếu future consequence của past được summarize đầy đủ trong current state, ta có thể solve recursively theo state thay vì enumerate toàn bộ history.

## Principle of optimality

Bellman's principle nói rằng nếu một policy là optimal từ initial state, thì phần còn lại của policy sau khi đi tới một intermediate state cũng phải optimal cho subproblem bắt đầu tại state đó.

Nếu suffix không optimal, ta có thể thay suffix bằng một solution tốt hơn và làm toàn solution tốt hơn, contradict optimality.

Đây là lý do optimal problems có thể tách thành optimal subproblems.

## Bellman equation cho finite horizon

Định nghĩa value function

```math
V_t(s)=\text{minimum future cost từ time }t\text{ khi current state là }s.
```

Boundary condition:

```math
V_T(s)=g(s).
```

Recursion:

```math
V_t(s)=\min_a\left[c(s,a)+V_{t+1}(F(s,a))\right].
```

Ta solve backward từ terminal time.

Công thức này biến exponential enumeration của action sequences thành reuse các subproblem values nếu số states manageable.

## Ví dụ shortest path

Cho directed graph với edge cost `w(u,v)`. Value từ node `u` tới target có thể viết

```math
V(u)=\min_{v:(u,v)\in E}\left[w(u,v)+V(v)\right].
```

Đây là Bellman structure. Algorithms như Bellman–Ford thực hiện relaxation dựa trên cùng idea.

Dijkstra cũng liên quan shortest-path optimal substructure nhưng khai thác nonnegative weights để chọn greedy order hiệu quả hơn.

## Memoization và tabulation

Top-down dynamic programming dùng recursive definition và cache results. Khi subproblem được gọi lại, ta reuse cached value.

Bottom-up tabulation tính subproblems theo thứ tự đảm bảo dependencies đã có sẵn.

Hai cách có cùng recurrence nhưng performance constants và memory pattern khác nhau.

Quan trọng nhất là xác định **state minimal nhưng sufficient**. State quá nhỏ mất information và recurrence sai; state quá lớn làm complexity bùng nổ.

## Ví dụ knapsack

Với items có weight `w_i`, value `v_i`, capacity `C`, define

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

Brute force xem `2^n` subsets. DP có khoảng `nC` states khi capacity integer, nên pseudo-polynomial complexity.

Điều này minh họa rằng DP efficiency đến từ number of distinct states chứ không phải number of possible histories.

## Overlapping subproblems

Dynamic programming hữu ích khi nhiều decision paths dẫn về cùng subproblem state.

Nếu subproblems hoàn toàn độc lập và không lặp, divide-and-conquer có thể phù hợp hơn.

Nếu current best local action luôn dẫn tới global optimum nhờ special exchange property, greedy algorithm có thể đơn giản hơn DP.

Chọn đúng paradigm cần nhìn structure chứ không dựa vào tên bài toán.

## Stochastic dynamic programming

Nếu next state random, Bellman recursion dùng expectation:

```math
V_t(s)=\min_a\left[c(s,a)+E[V_{t+1}(S_{t+1})\mid s,a]\right].
```

Nếu transition probabilities known,

```math
V_t(s)=\min_a\left[c(s,a)+\sum_{s'}P(s'\mid s,a)V_{t+1}(s')\right].
```

Đây là bridge trực tiếp từ optimization sang Markov decision processes.

## Infinite horizon và discounting

Với infinite horizon ta thường dùng discount factor `0≤γ<1`:

```math
E\left[\sum_{t=0}^{\infty}\gamma^t r_t\right].
```

Value function của policy `π` thỏa

```math
V^\pi(s)=E_\pi\left[r(s,a)+\gamma V^\pi(S')\mid s\right].
```

Optimal value thỏa Bellman optimality equation:

```math
V^*(s)=\max_a E\left[r(s,a)+\gamma V^*(S')\mid s,a\right].
```

Discounting vừa encode preference cho reward sớm hơn vừa giúp infinite sum finite dưới bounded rewards.

## Markov Decision Process

Một **MDP** gồm state space, action space, transition model, reward function và discount factor.

Markov assumption nói distribution của next state phụ thuộc current state/action, không cần toàn history nếu state được define đúng.

Policy

```math
\pi(a\mid s)
```

mô tả cách chọn action tại each state.

Reinforcement learning khác classical DP chủ yếu ở việc transition/reward model có thể unknown và phải học từ interaction.

## Value iteration

Value iteration lặp Bellman optimality update:

```math
V_{k+1}(s)=\max_a\sum_{s'}P(s'\mid s,a)
\left[r(s,a,s')+\gamma V_k(s')\right].
```

Under finite discounted MDP conditions, Bellman operator là contraction với factor `γ`, nên iteration converge tới unique fixed point `V*`.

Đây là connection sâu giữa fixed-point theory và sequential optimization.

## Policy iteration

Policy iteration alternating hai bước.

Policy evaluation tính `V^π` cho current policy.

Policy improvement chọn action tốt hơn theo current value:

```math
\pi_{new}(s)=\arg\max_a
E[r+\gamma V^\pi(S')\mid s,a].
```

Quá trình lặp tới khi policy không còn cải thiện.

## Bellman equation như fixed point

Viết Bellman operator `T`:

```math
(TV)(s)=\max_a E[r+\gamma V(S')\mid s,a].
```

Optimal value thỏa

```math
V^*=TV^*.
```

Nhìn theo fixed point giúp kết nối dynamic programming với analysis và numerical methods. Value iteration là repeated application của operator cho tới fixed point.

## Deterministic optimal control

Trong control, state dynamics có thể là

```math
x_{t+1}=f(x_t,u_t)
```

với control `u_t` và cost

```math
\sum_t \ell(x_t,u_t).
```

Bellman equation vẫn giữ same structure:

```math
V_t(x)=\min_u\left[\ell(x,u)+V_{t+1}(f(x,u))\right].
```

Nếu state continuous và high-dimensional, exact DP thường impossible do **curse of dimensionality**.

## Curse of dimensionality

Nếu mỗi state dimension discretized thành `k` values và có `d` dimensions, tổng grid states là

```math
k^d.
```

Chỉ tăng dimension một chút có thể làm memory và computation explode exponentially.

Đây là lý do approximate dynamic programming, function approximation và reinforcement learning quan trọng.

Neural networks trong RL có thể approximate value function thay vì lưu table cho từng state.

## Relationship với greedy algorithms

Greedy chọn action tốt nhất ngay lúc này. DP chọn action tốt nhất xét cả value của future state.

Nếu objective là

```math
\text{immediate reward}+\text{future value},
```

bỏ future value thường sai.

Greedy đúng khi problem có stronger structure chứng minh rằng local choice safe, như matroid structure hoặc exchange arguments trong một số problems.

## Relationship với backtracking

Backtracking enumerate possibilities nhưng prune khi partial solution impossible. Dynamic programming merge histories dẫn đến cùng state.

Một problem có thể dùng cả hai: search over high-level choices, DP solve repeated subproblem bên trong.

## Sequence alignment

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

State `(i,j)` summarize toàn relevant past. Đây là lý do exponentially many edit sequences collapse vào `O(mn)` states.

## Resource allocation

Giả sử có budget `B` phân cho projects. Nếu reward project `i` khi cấp `x` units là `r_i(x)`, define

```math
V(i,b)=\text{max reward từ projects }i..n\text{ với budget }b.
```

Then

```math
V(i,b)=\max_{0\le x\le b}
\left[r_i(x)+V(i+1,b-x)\right].
```

Đây là generic pattern: state giữ remaining resource, action chọn lượng resource cấp hiện tại.

## Optimal control và Pontryagin

Dynamic programming dùng value function trên state space. Một alternative framework trong continuous optimal control là Pontryagin maximum principle, dùng costate variables và Hamiltonian.

Hai approaches nhìn cùng problem từ góc khác nhau. Bellman/HJB equation thiên về global value function; Pontryagin conditions thiên về necessary conditions dọc optimal trajectory.

## Hamilton–Jacobi–Bellman equation

Trong continuous time, Bellman principle dẫn tới HJB PDE. Với dynamics

```math
\dot x=f(x,u)
```

và running cost `L(x,u)`, dạng schematic là

```math
0=\min_u\left[L(x,u)+\nabla V(x)^Tf(x,u)\right]
```

cộng time derivative nếu finite horizon.

HJB nối optimization, calculus of variations, control và PDE.

## Mental Model

Dynamic programming biến một “tree của histories” thành một “graph của states”. Nếu nhiều histories dẫn tới cùng state và future chỉ phụ thuộc state, ta không cần solve future lại nhiều lần. Bellman equation là statement rằng optimal total value bằng immediate value cộng optimal future value.

## Common Misconceptions

DP không đồng nghĩa với memoization. Memoization là kỹ thuật cache; dynamic programming là structural decomposition của optimization problem.

Một nhầm lẫn khác là nghĩ mọi recurrence đều là DP. Recurrence chỉ trở thành useful DP khi state/subproblem được define sao cho optimal substructure và reuse tồn tại.

Bellman equation cũng không đảm bảo computation rẻ. Với continuous hoặc high-dimensional states, exact DP có thể infeasible vì curse of dimensionality.

## Liên kết kiến thức

Chapter này dựa trên [Recurrence and induction](../07_discrete_cs/02_recurrence_and_induction_in_algorithms.md), [Optimization](./00_optimization.md), [Stochastic processes and Markov chains](../06_probability_statistics/11_stochastic_processes_markov_chains_and_time_series.md) và [PDE](../05_calculus/10_partial_differential_equations_and_fields_intro.md). Nó là nền toán học trực tiếp cho reinforcement learning, shortest path, scheduling và optimal control.