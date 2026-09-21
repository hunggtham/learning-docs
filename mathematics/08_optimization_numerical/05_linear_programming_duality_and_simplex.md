# Linear programming, duality và simplex: geometry, certificates và resource prices

**Quy hoạch tuyến tính (linear programming, LP / 선형계획법)** giải bài toán tối ưu khi objective và constraints đều tuyến tính.

Dạng điển hình:

```math
\max_x c^Tx
```

subject to

```math
Ax\le b,
\qquad x\ge0.
```

Nhìn bề ngoài đây chỉ là “linear equations + inequalities”. Nhưng structure tuyến tính tạo ra một geometry cực mạnh:

```text
linear constraints
→ convex polyhedron
→ extreme points
→ dual certificates
→ sensitivity / shadow prices
```

Đây là lý do LP vừa có theory đẹp vừa có solvers công nghiệp rất mạnh.

## 1. Modeling trước optimization

Một LP không bắt đầu từ simplex; nó bắt đầu từ **decision variables**.

Ví dụ production planning:

```text
x1 = units product A
x2 = units product B
```

Profit:

```math
\max 30x_1+20x_2.
```

Nếu machine hours:

```math
2x_1+x_2\le100
```

và material:

```math
x_1+2x_2\le80,
```

cùng nonnegativity:

```math
x_1,x_2\ge0.
```

Điểm quan trọng: LP chỉ đúng nếu linearity assumptions hợp lý.

Nếu unit cost thay đổi theo volume, capacity có startup threshold hoặc decision phải integer, pure LP chỉ là approximation/relaxation.

## 2. Geometry của feasible region

Mỗi inequality tuyến tính:

```math
a_i^Tx\le b_i
```

xác định một **half-space / 반공간**.

Intersection của các half-spaces tạo feasible set:

```math
\mathcal F=\{x:Ax\le b\}.
```

Vì half-spaces convex, feasible region cũng convex.

Điều này rất quan trọng: nếu `x` và `y` feasible thì mọi convex combination

```math
\theta x+(1-\theta)y,
\qquad 0\le\theta\le1
```

cũng feasible.

Không có “hole” hoặc disconnected feasible islands như trong nhiều nonconvex problems.

## 3. Vì sao optimum thường nằm ở extreme point?

Objective tuyến tính:

```math
c^Tx
```

có level sets là parallel hyperplanes.

Ta có thể tưởng tượng dịch hyperplane theo direction `c` cho tới khi nó rời feasible polyhedron.

Nếu finite optimum tồn tại, ít nhất một optimum nằm ở một **extreme point (đỉnh cực biên / 극점)**.

Proof intuition: nếu optimum nằm strictly bên trong line segment giữa hai feasible points khác nhau, linearity làm objective tại midpoint bằng weighted average objectives. Khi đó ít nhất một endpoint không tệ hơn.

Điều này không nói optimum luôn unique. Một whole edge/face có thể optimal.

## 4. Feasible, infeasible và unbounded là ba trạng thái khác nhau

Một LP có thể:

```text
feasible + finite optimum
infeasible
unbounded
```

**Infeasible** nghĩa constraints mâu thuẫn: không có point nào satisfy tất cả.

**Unbounded** nghĩa có feasible direction làm objective tăng vô hạn.

Hai failure modes này khác nhau và solvers thường trả status riêng.

Trong production modeling, phân biệt rất quan trọng:

```text
infeasible → business constraints conflict
unbounded → model thiếu limiting constraint hoặc objective có structural issue
```

## 5. Slack variables và unused resource

Constraint:

```math
x_1+x_2\le4
```

có thể đổi thành:

```math
x_1+x_2+s=4,
\qquad s\ge0.
```

`s` là **slack variable (biến dư / 여유변수)**.

Interpretation:

```text
s = unused resource
```

Nếu `s=0`, constraint **binding/active**.
Nếu `s>0`, resource còn dư.

Khái niệm này nối trực tiếp sang complementary slackness và KKT.

## 6. Basic solution: algebra phía sau vertex

Trong standard form:

```math
Ax=b,
\qquad x\ge0,
```

với `m` independent equations, một **basic solution** chọn roughly `m` basic variables rồi set remaining nonbasic variables bằng zero.

Khi basic solution thỏa nonnegativity, ta có **basic feasible solution**.

Geometrically, basic feasible solutions tương ứng các vertices dưới nondegeneracy assumptions.

Simplex vì vậy có hai viewpoints cùng lúc:

```text
algebra → basis of columns
geometry → vertex of polyhedron
```

## 7. Simplex method: local moves nhưng global guarantee trong LP

Simplex bắt đầu từ basic feasible solution và thay basis để đi tới adjacent vertex có objective tốt hơn.

Mental flow:

```text
current basis
→ identify improving nonbasic direction
→ ratio test để giữ feasibility
→ pivot
→ new basis
```

Điểm đặc biệt là dù move local, convex/linear structure cho phép kết luận global optimality khi không còn improving reduced-cost direction.

Đây là contrast với nonconvex optimization, nơi local stationarity không đủ.

## 8. Pivot không chỉ là row operation

Pivot trong simplex thay đổi representation của solution theo một basis mới.

Linear algebra phía dưới gồm repeatedly solving systems liên quan basis matrix `B`:

```math
Bx_B=b.
```

Production solvers không rebuild mọi thứ từ đầu; chúng dùng sparse factorization/update để tận dụng structure.

Vì vậy numerical linear algebra là engine bên dưới simplex.

## 9. Degeneracy và cycling

Một vertex có thể tương ứng nhiều different bases. Khi một basic variable bằng zero, solution **degenerate / 퇴화**.

Simplex pivot có thể đổi basis mà objective không cải thiện.

Trong pathological cases, naive pivot rules có thể cycle. Rules như Bland's rule tránh cycling theoretically.

Lesson: “đi qua vertices” là mental model tốt, nhưng implementation cần handle algebraic degeneracy.

## 10. Dual problem: constraints trở thành prices

Với primal:

```math
\max c^Tx
```

subject to

```math
Ax\le b,
\qquad x\ge0,
```

một dual form là:

```math
\min b^Ty
```

subject to

```math
A^Ty\ge c,
\qquad y\ge0.
```

`y_i` có thể interpret như **shadow price (giá bóng / 잠재가격)** của resource constraint `i`.

Dual không chỉ là “bài toán phụ”. Nó cung cấp một cách định giá resources đủ cao để chứng minh rằng không feasible production plan nào tạo profit vượt upper bound `b^Ty`.

## 11. Weak duality: certificate bằng một inequality chain

Cho primal feasible `x` và dual feasible `y`.

Từ:

```math
Ax\le b,
\qquad y\ge0
```

suy ra:

```math
y^TAx\le y^Tb.
```

Từ:

```math
A^Ty\ge c,
\qquad x\ge0
```

suy ra:

```math
x^TA^Ty\ge c^Tx.
```

Vì:

```math
x^TA^Ty=y^TAx,
```

nên:

```math
c^Tx\le b^Ty.
```

Đây là **weak duality / 약한 쌍대성**.

Mọi dual feasible solution là upper bound cho primal maximization.

## 12. Strong duality: optimal value có hai cách nhìn

Dưới standard LP conditions, nếu finite optimum tồn tại thì:

```math
c^Tx^*=b^Ty^*.
```

Đây là **strong duality / 강한 쌍대성**.

Ý nghĩa sâu:

```text
best achievable decision value
=
best valid resource-price certificate
```

Optimization và proof of optimality gặp nhau.

Nếu tìm primal feasible `x` và dual feasible `y` có same objective, ta có certificate rằng cả hai optimal mà không cần enumerate alternatives.

## 13. Complementary slackness

Một primal resource constraint có slack:

```math
s_i=b_i-(Ax)_i.
```

Complementary slackness:

```math
y_i s_i=0.
```

Nghĩa là:

```text
resource dư → shadow price zero
shadow price positive → resource fully used
```

Tương tự, positive primal variable liên hệ với binding dual constraint.

Đây là LP-specialized version của KKT complementary slackness.

## 14. Worked example: production và shadow prices

Giả sử:

```math
\max 3x+2y
```

subject to:

```math
x+y\le4
```

```math
x\le2
```

```math
x,y\ge0.
```

Vertices:

```text
(0,0)
(2,0)
(0,4)
(2,2)
```

Objective:

```text
0
6
8
10
```

nên optimum tại:

```math
(x,y)=(2,2).
```

Cả hai constraints active.

Nếu resource của first constraint tăng nhẹ, optimal objective có thể tăng theo dual multiplier tương ứng cho tới khi active-set structure thay đổi.

Đây là sensitivity interpretation, không phải global law cho mọi mức perturbation.

## 15. Sensitivity analysis và allowable range

Shadow price thường chỉ valid trong một range nơi optimal basis không đổi.

Nếu thay `b_i` quá mạnh, active constraints có thể đổi và marginal value cũng đổi.

Vì vậy output kiểu:

```text
shadow price = 5
```

không nên đọc là “mỗi resource unit mãi mãi worth 5”. Nó là local sensitivity result theo current LP regime.

## 16. Duality và KKT

LP là convex optimization với linear constraints.

KKT conditions trở thành:

```text
primal feasibility
dual feasibility
stationarity
complementary slackness
```

Trong LP, these conditions align rất cleanly với primal/dual optimality.

Hiểu LP trước giúp KKT bớt abstract; hiểu KKT sau giúp thấy LP chỉ là một member đặc biệt của broader convex duality.

## 17. Interior-point methods: không cần đi theo edges

Simplex đi vertex-to-vertex. **Interior-point methods / 내부점법** đi xuyên interior của feasible region bằng barrier ideas.

Theory hiện đại cho polynomial-time guarantees cho LP.

Practical solver choice phụ thuộc:

```text
problem size
sparsity
warm starts
need for basis/sensitivity info
numerical conditioning
```

Không có rule “simplex luôn tốt hơn” hoặc “interior-point luôn mới hơn nên tốt hơn”.

## 18. Integer programming: discreteness phá convex simplicity

Nếu decision phải integer:

```math
x_i\in\mathbb Z
```

hoặc binary:

```math
x_i\in\{0,1\},
```

ta có ILP/MILP.

Feasible solutions giờ là discrete points, không phải toàn polyhedron.

LP relaxation bỏ integrality:

```text
integer feasible set
⊂ LP relaxation polyhedron
```

Đối với maximization, LP optimum cho upper bound.

Branch-and-bound dùng bound này để prune search tree.

## 19. Integrality gap

Difference giữa integer optimum và LP relaxation optimum gọi broadly là **integrality gap**.

Nếu gap nhỏ, LP relaxation rất informative.
Nếu gap lớn, rounding naive có thể tệ.

Đây là reason relaxation quality quan trọng trong combinatorial optimization.

## 20. Total unimodularity: khi LP tự cho integer solution

Một số structured matrices như network incidence matrices có property **total unimodularity**.

Với integer right-hand side phù hợp, LP vertices tự integer.

Điều này giải thích vì sao một số graph problems có polynomial LP formulations dù nhìn giống discrete optimization.

Structure matrix có thể biến “integer-looking problem” thành pure LP tractable problem.

## 21. Network flow như structured LP

Max flow có variables trên edges:

```math
f_e
```

constraints gồm capacity:

```math
0\le f_e\le c_e
```

và flow conservation tại intermediate nodes.

Objective maximize total source-to-sink flow.

Graph structure cho specialized algorithms nhanh hơn generic LP.

Max-flow/min-cut theorem cũng là một duality statement: max primal flow value bằng min cut capacity.

## 22. LP trong Finance

Simplified portfolio allocation có thể là LP nếu objective/risk constraints được linearized.

Ví dụ:

```text
maximize expected return
subject to budget
sector exposure limits
transaction bounds
```

Nhưng classical variance risk:

```math
w^T\Sigma w
```

là quadratic, nên problem trở thành quadratic programming.

Model class phải follow actual structure, không ép mọi optimization thành LP.

## 23. LP trong Software/Operations

LP/MILP xuất hiện trong:

```text
cloud resource allocation
workforce scheduling
transportation
supply chain
ad placement
capacity planning
network routing
```

Một system design lesson quan trọng:

> Solver chỉ optimize model đã viết; model sai thì optimum có thể rất chính xác nhưng operationally vô nghĩa.

## 24. Numerical considerations

LP theory dùng exact real arithmetic, nhưng solver dùng floating point.

Problems có coefficients khác scale quá lớn có thể gây numerical difficulty.

Scaling, presolve và tolerances ảnh hưởng practical result.

Constraint:

```math
10^{-9}x+10^9y\le1
```

có severe scale imbalance.

Optimization status như “feasible within tolerance” không phải exact symbolic proof trong floating-point implementation.

## 25. Common failure modes

### Objective misspecification

Nếu objective không capture real cost/value, solver sẽ optimize wrong proxy.

### Missing constraints

Unbounded solution thường reveal missing physical/business limit.

### Arbitrary rounding

Rounding fractional LP solution có thể violate constraints.

### Shadow price overinterpretation

Dual sensitivity thường local theo current basis/regime.

### Ignoring uncertainty

Deterministic LP với uncertain demand có thể produce brittle plan. Robust/stochastic optimization thêm uncertainty explicitly.

## Knowledge Connection

LP nằm tại giao điểm:

```text
linear algebra → Ax
geometry → convex polyhedra
graph theory → network flow
KKT → complementary slackness
economics → shadow prices
combinatorics → integer programming
numerical analysis → sparse factorization / conditioning
```

## Mental Model

> LP là geometry của decisions dưới linear constraints. Simplex nhìn feasible polyhedron qua các bases/vertices. Duality biến constraints thành prices và tạo certificate của optimality. Khi thêm integrality, geometry continuous không còn đủ và search/combinatorics quay trở lại.

## Common Misconceptions

“Programming” trong linear programming nghĩa planning, không phải coding. LP optimum không nhất thiết unique. Vertex theorem không có nghĩa phải brute-force mọi corners. Simplex worst-case exponential không đồng nghĩa unusable trong practice. LP relaxation không phải integer solution. Dual variable là sensitivity quantity dưới assumptions, không phải universal economic truth.