# Tối ưu hóa: mục tiêu, ràng buộc và trade-off

Tối ưu hóa (Optimization / 최적화) hỏi: trong tất cả lựa chọn hợp lệ, lựa chọn nào minimize hoặc maximize một objective? Cấu trúc này xuất hiện trong scheduling, portfolio allocation, model training, routing, resource allocation và engineering design.

## Objective và feasible set

Một optimization problem có objective function `f(x)` và constraints xác định feasible set.

```math
\min_x f(x)
```

subject to

```math
g_i(x)\le0,\qquad h_j(x)=0
```

Điểm `x` chỉ có thể là solution nếu feasible. Một point có objective cực tốt nhưng phá constraint không phải lời giải hợp lệ.

## Local vs global optimum

Local minimum tốt hơn nearby points; global minimum tốt hơn mọi feasible points.

Non-convex landscapes có thể có nhiều local minima, maxima và saddle points. Gradient zero chỉ cho stationary candidate.

## Convexity

Function `f` convex nếu với `0≤t≤1`:

```math
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
```

Geometrically, line segment giữa hai graph points nằm trên hoặc above graph.

Convex optimization đặc biệt vì mọi local minimum là global minimum. Đây là lý do convexity là structural gold: nó biến local information thành global guarantee.

## Constraint geometry

Linear constraints tạo half-spaces; intersection là convex polyhedron. Linear programming:

```math
\min c^Tx\quad\text{subject to }Ax\le b
```

có linear objective trên feasible polytope. Optimum, nếu finite và attained, thường có thể tìm ở extreme point/face structure.

## Lagrange multipliers

Muốn optimize `f(x,y)` subject to equality constraint `g(x,y)=c`. Tại smooth constrained optimum, không thể move tangent constraint để improve first order. Vì gradient `∇g` normal constraint, `∇f` phải parallel `∇g`:

```math
\nabla f=\lambda\nabla g
```

Đây là Lagrange multiplier condition.

`λ` còn có sensitivity interpretation: approximate change optimal objective khi constraint bound thay đổi một chút dưới conditions phù hợp.

## KKT idea

Karush–Kuhn–Tucker conditions mở rộng Lagrange multipliers cho inequality constraints với complementary slackness. Chúng là central language của constrained nonlinear optimization.

Không phải KKT luôn sufficient; convexity và constraint qualifications quyết định guarantees.

## Discrete optimization

Khi variables chỉ nhận integer/binary values, calculus có thể không áp trực tiếp. Knapsack, scheduling, routing và assignment là combinatorial optimization.

Search space thường tăng exponential/factorial, nên methods gồm dynamic programming, branch-and-bound, relaxations, heuristics và approximation algorithms.

## Multi-objective trade-offs

Thực tế thường có nhiều goals: cost thấp, latency thấp, reliability cao. Không phải lúc nào có một solution tốt hơn mọi mặt.

Pareto optimum là solution không thể improve một objective mà không worsen ít nhất một objective khác. Chọn điểm cụ thể cần preference/weights/business constraints ngoài mathematics thuần.

## Mental Model

> Optimization không bắt đầu bằng derivative; nó bắt đầu bằng việc xác định decision variables, objective và feasible set. Derivative chỉ là một công cụ để đọc local improvement khi structure cho phép.

## Common Misconceptions

Stationary point không chắc optimum. Local optimum không chắc global trừ khi có structure như convexity. Một objective function luôn encode priorities; nếu objective không phản ánh business goal đúng, optimizer sẽ “tối ưu sai thứ” rất hiệu quả.
