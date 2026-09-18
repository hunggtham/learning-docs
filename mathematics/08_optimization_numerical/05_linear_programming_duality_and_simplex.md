# Linear programming, duality và simplex

Nhiều optimization problems trong logistics, scheduling, production và resource allocation có một structure đặc biệt: objective và constraints đều tuyến tính. **Quy hoạch tuyến tính (Linear Programming, LP / 선형계획법)** tận dụng structure này để giải problems rất lớn một cách có hệ thống.

Một LP tiêu chuẩn có dạng

```math
\max_x c^Tx
```

subject to

```math
Ax\le b,
\qquad
x\ge0.
```

`x` là decision vector, `c` chứa value/cost coefficients, `A` mô tả resource usage và `b` là available limits.

## Geometry của feasible region

Mỗi linear inequality xác định một half-space. Intersection của các half-spaces tạo **feasible region / 실행가능영역**, một convex polyhedron.

Ví dụ:

```math
\max 3x+2y
```

subject to

```math
x+y\le4,
\qquad
x\le2,
\qquad
x,y\ge0.
```

Objective `3x+2y` có level sets là parallel lines. Ta “đẩy” line theo direction tăng objective cho đến khi nó chạm feasible region lần cuối. Vì region convex polygon và objective linear, optimum — nếu finite và tồn tại — có thể đạt tại một **extreme point / 꼭짓점**.

Đây là geometric reason simplex method có thể di chuyển qua vertices thay vì search mọi interior point.

## Slack variables và standard form

Inequality

```math
x+y\le4
```

có thể viết thành equality bằng **slack variable / 여유변수** `s≥0`:

```math
x+y+s=4.
```

Slack đo unused resource. Nếu `s=0`, constraint active/binding; nếu `s>0`, còn resource dư.

KKT conditions ở optimization tổng quát cũng có notion active constraints. LP là một setting nơi geometry và algebra của constraints nhìn rất rõ.

## Simplex method: đi từ vertex sang vertex

**Simplex method / 심플렉스법** bắt đầu từ một basic feasible solution, tương ứng một vertex, rồi chọn adjacent vertex cải thiện objective. Quá trình lặp đến khi không còn improving direction theo simplex criterion.

Worst-case complexity của simplex có thể exponential với special constructions, nhưng trong thực tế nó rất hiệu quả trên nhiều classes of LPs. Interior-point methods cung cấp polynomial-time algorithms theo theory và thường cạnh tranh tốt trên large problems.

Điểm cần giữ: linear programming không đồng nghĩa “thử tất cả corners”. Algorithms khai thác matrix structure, sparsity và factorization để xử lý dimensions cực lớn.

## Dual problem: mỗi constraint có một price

Mỗi primal LP có một **dual / 쌍대문제**. Với primal

```math
\max c^Tx
\quad\text{s.t.}\quad
Ax\le b,
\ x\ge0,
```

dual điển hình là

```math
\min b^Ty
\quad\text{s.t.}\quad
A^Ty\ge c,
\ y\ge0.
```

Dual variables `y` có thể được hiểu như **shadow prices / 잠재가격** cho constraints/resources.

Nếu một unit resource thứ `i` tăng thêm một chút, optimal value có thể tăng gần `y_i` trong regime nơi active set không đổi. Đây là sensitivity interpretation của dual variables.

## Weak duality

Lấy any primal feasible `x` và dual feasible `y`. Vì

```math
Ax\le b,
\qquad
y\ge0,
```

nên

```math
y^TAx\le y^Tb.
```

Vì

```math
A^Ty\ge c,
\qquad x\ge0,
```

nên

```math
x^TA^Ty\ge x^Tc=c^Tx.
```

Nhưng `x^TA^Ty=y^TAx`, do đó

```math
c^Tx\le b^Ty.
```

Đây là **weak duality / 약한 쌍대성**: mọi dual feasible objective là upper bound cho primal maximization objective.

Nó cho một certificate cực mạnh. Nếu tìm được primal feasible `x` và dual feasible `y` có equal objective values, cả hai đều optimal.

## Strong duality

Dưới standard LP feasibility conditions, nếu primal có finite optimum thì dual cũng có optimum và

```math
c^Tx^*=b^Ty^*.
```

Đây là **strong duality / 강한 쌍대성**.

Duality không chỉ là trick tạo bài toán khác. Nó nói optimization có hai viewpoints complementary: trực tiếp chọn decisions và gián tiếp định giá constraints sao cho không decision nào tạo value vượt chi phí implied bởi prices.

## Complementary slackness

Primal slack và dual variables liên hệ bằng **complementary slackness / 상보적 느슨성**. Trực giác: nếu một resource constraint không binding, shadow price của nó phải zero tại optimum; nếu shadow price positive, resource phải fully used.

Dạng component-wise thường là

```math
y_i(b_i-(Ax)_i)=0.
```

Và tương tự giữa primal variables và dual constraint slacks.

Condition này là special case của complementary slackness trong KKT theory.

## Integer programming: khi decision không thể fractional

Nhiều real problems yêu cầu `x_i` integer hoặc binary. Không thể mua `0.37` chiếc xe hoặc chọn `0.6` project. Khi thêm integrality constraints ta có **Integer Linear Programming (ILP / 정수선형계획)** hoặc Mixed-Integer Linear Programming.

Geometry thay đổi mạnh: feasible set không còn convex continuous polyhedron mà chỉ gồm discrete lattice points. LP relaxation bỏ integrality để lấy bound; branch-and-bound, cutting planes và heuristics dùng bound đó để search.

Đây là reason scheduling/routing có thể khó dù formulas nhìn “chỉ tuyến tính”. Discreteness làm computational complexity tăng mạnh.

## Network flow như LP đặc biệt

Max-flow/min-cost-flow problems có LP formulations với network incidence matrices. Structure đặc biệt cho phép algorithms nhanh hơn generic LP.

Ví dụ flow conservation tại node là linear equality: inflow minus outflow bằng supply/demand. Capacities là linear inequalities. Routing, transportation và matching nhiều khi có thể nhìn như optimization trên graph.

## LP trong công việc và đời sống

Production planning: chọn quantities để maximize profit dưới machine-hours và material constraints. Portfolio ở dạng đơn giản: allocate capital dưới budget/exposure constraints. Workforce scheduling: cover demand với minimum cost. Cloud capacity planning: allocate workloads dưới CPU/memory/network limits.

Tất cả đều cần cẩn thận với model assumptions. Nếu cost curve thực ra nonlinear, demand uncertain hoặc decisions indivisible, pure LP chỉ là approximation hoặc relaxation.

## Knowledge Connection

Linear programming nối geometry của convex sets, linear algebra của `Ax`, optimization duality và economics của shadow prices. KKT conditions generalize nhiều LP optimality ideas. Graph algorithms xuất hiện như structured LPs. Numerical linear algebra nằm dưới solvers thực tế.

Trong machine learning, linear programming xuất hiện trong certain robust optimization, sparse formulations và piecewise-linear models. Duality cũng là nền tảng để hiểu support vector machines và Lagrangian methods.

## Mental Model

> LP là bài toán “đẩy một hyperplane tuyến tính đến mép của một polyhedron”. Primal hỏi nên chọn decisions nào; dual hỏi mỗi constraint/resource phải có price bao nhiêu để chứng minh không solution nào tốt hơn. Equality giữa hai viewpoints là certificate của optimality.

## Common Misconceptions

Linear programming không phải lập trình máy tính theo nghĩa coding; “programming” ở đây có nghĩa planning/optimization.

Optimum tại vertex không có nghĩa unique. Cả một edge/face có thể optimal nếu objective song song với nó.

LP solution fractional không tự động dùng được cho integer decisions. Rounding arbitrary có thể violate constraints hoặc mất optimality rất lớn; integer optimization cần methods riêng.
