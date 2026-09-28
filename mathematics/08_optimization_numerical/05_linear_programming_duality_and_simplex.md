# Tuyến tính (linear / 선형) programming, duality và simplex: hình học (geometry / 기하학), certificates và tài nguyên (resource / 자원) prices

> **Mạch đọc:** Đọc **tuyến tính (linear / 선형) programming, duality và simplex: hình học (geometry / 기하학), certificates và tài nguyên (resource / 자원) prices** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Modeling trước tối ưu hóa (optimization / 최적화)** sang **2. hình học (geometry / 기하학) của feasible region**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Quy hoạch tuyến tính (linear programming, LP / 선형계획법)** giải bài toán tối ưu khi mục tiêu (objective / 목표) và các ràng buộc (constraints / 제약조건들) đều tuyến tính.

Dạng điển hình:

```math
\max_x c^Tx
```

subject to

```math
Ax\le b,
\qquad x\ge0.
```

Nhìn bề ngoài đây chỉ là “tuyến tính (linear / 선형) equations + inequalities”. Nhưng cấu trúc (structure / 구조) tuyến tính tạo ra một hình học (geometry / 기하학) cực mạnh:

```text
linear constraints
→ convex polyhedron
→ extreme points
→ dual certificates
→ sensitivity / shadow prices
```

Đây là lý do LP vừa có lý thuyết (theory / 이론) đẹp vừa có solvers công nghiệp rất mạnh.

## 1. Modeling trước tối ưu hóa (optimization / 최적화)

Một LP không bắt đầu từ simplex; nó bắt đầu từ **quyết định (decision / 결정) variables**.

Ví dụ môi trường vận hành (production / 운영 환경) planning:

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

Điểm quan trọng: LP chỉ đúng nếu linearity các giả định (assumptions / 가정들) hợp lý.

Nếu đơn vị (unit / 단위) chi phí (cost / 비용) thay đổi theo volume, sức chứa (capacity / 용량) có startup threshold hoặc quyết định (decision / 결정) phải integer, pure LP chỉ là approximation/relaxation.

## 2. hình học (geometry / 기하학) của feasible region

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

## 3. Vì sao optimum thường nằm ở extreme điểm (point / 지점)?

Mục tiêu (objective / 목표) tuyến tính:

```math
c^Tx
```

có mức (level / 수준) sets là parallel hyperplanes.

Ta có thể tưởng tượng dịch hyperplane theo direction `c` cho tới khi nó rời feasible polyhedron.

Nếu finite optimum tồn tại, ít nhất một optimum nằm ở một **extreme điểm (point / 지점)**.

Proof intuition: nếu optimum nằm strictly bên trong line segment giữa hai feasible points khác nhau, linearity làm mục tiêu (objective / 목표) tại midpoint bằng weighted average objectives. Khi đó ít nhất một endpoint không tệ hơn.

Điều này không nói optimum luôn unique. Một whole edge/face có thể optimal.

## 4. Feasible, infeasible và unbounded là ba trạng thái khác nhau

Một LP có thể:

```text
feasible + finite optimum
infeasible
unbounded
```

**Infeasible** nghĩa các ràng buộc (constraints / 제약조건들) mâu thuẫn: không có điểm (point / 지점) nào satisfy tất cả.

**Unbounded** nghĩa có feasible direction làm mục tiêu (objective / 목표) tăng vô hạn.

Hai thất bại (failure / 실패) modes này khác nhau và solvers thường trả status riêng.

Trong môi trường vận hành (production / 운영 환경) modeling, phân biệt rất quan trọng:

```text
infeasible → business constraints conflict
unbounded → model thiếu limiting constraint hoặc objective có structural issue
```

## 5. Slack variables và unused tài nguyên (resource / 자원)

Ràng buộc (constraint / 제약조건):

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

Nếu `s=0`, ràng buộc (constraint / 제약조건) **binding/active**.
Nếu `s>0`, tài nguyên (resource / 자원) còn dư.

Khái niệm này nối trực tiếp sang complementary slackness và KKT.

## 6. Basic solution: algebra phía sau vertex

Trong tiêu chuẩn (standard / 표준) form:

```math
Ax=b,
\qquad x\ge0,
```

với `m` independent equations, một **basic solution** chọn roughly `m` basic variables rồi set remaining nonbasic variables bằng zero.

Khi basic solution thỏa nonnegativity, ta có **basic feasible solution**.

Geometrically, basic feasible solutions tương ứng các vertices dưới nondegeneracy các giả định (assumptions / 가정들).

Simplex vì vậy có hai viewpoints cùng lúc:

```text
algebra → basis of columns
geometry → vertex of polyhedron
```

## 7. Simplex phương thức (method / 메서드): cục bộ (local / 로컬) moves nhưng toàn cục (global / 전역) guarantee trong LP

Simplex bắt đầu từ basic feasible solution và thay basis để đi tới adjacent vertex có mục tiêu (objective / 목표) tốt hơn.

Mental luồng (flow / 흐름):

```text
current basis
→ identify improving nonbasic direction
→ ratio test để giữ feasibility
→ pivot
→ new basis
```

Điểm đặc biệt là dù move cục bộ (local / 로컬), convex/tuyến tính (linear / 선형) cấu trúc (structure / 구조) cho phép kết luận toàn cục (global / 전역) optimality khi không còn improving reduced-cost direction.

Đây là contrast với nonconvex tối ưu hóa (optimization / 최적화), nơi cục bộ (local / 로컬) stationarity không đủ.

## 8. Pivot không chỉ là row thao tác (operation / 연산)

Pivot trong simplex thay đổi biểu diễn (representation / 표현) của solution theo một basis mới.

Tuyến tính (linear / 선형) algebra phía dưới gồm repeatedly solving các hệ thống (systems / 시스템들) liên quan basis ma trận (matrix / 행렬) `B`:

```math
Bx_B=b.
```

Môi trường vận hành (production / 운영 환경) solvers không rebuild mọi thứ từ đầu; chúng dùng sparse factorization/cập nhật (update / 업데이트) để tận dụng cấu trúc (structure / 구조).

Vì vậy numerical tuyến tính (linear / 선형) algebra là engine bên dưới simplex.

## 9. Degeneracy và cycling

Một vertex có thể tương ứng nhiều different bases. Khi một basic variable bằng zero, solution **degenerate / 퇴화**.

Simplex pivot có thể đổi basis mà mục tiêu (objective / 목표) không cải thiện.

Trong pathological cases, naive pivot rules có thể cycle. Rules như Bland's quy tắc (rule / 규칙) tránh cycling theoretically.

Lesson: “đi qua vertices” là mô hình tư duy (mental model / 사고 모델) tốt, nhưng hiện thực (implementation / 구현) cần handle algebraic degeneracy.

## 10. Dual bài toán (problem / 문제): các ràng buộc (constraints / 제약조건들) trở thành prices

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

`y_i` có thể interpret như **shadow price (giá bóng / 잠재가격)** của tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) `i`.

Dual không chỉ là “bài toán phụ”. Nó cung cấp một cách định giá resources đủ cao để chứng minh rằng không feasible môi trường vận hành (production / 운영 환경) plan nào tạo profit vượt upper bound `b^Ty`.

## 11. Weak duality: certificate bằng một inequality chuỗi (chain / 사슬)

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

## 12. Strong duality: optimal giá trị (value / 값) có hai cách nhìn

Dưới tiêu chuẩn (standard / 표준) LP conditions, nếu finite optimum tồn tại thì:

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

Tối ưu hóa (optimization / 최적화) và proof of optimality gặp nhau.

Nếu tìm primal feasible `x` và dual feasible `y` có same mục tiêu (objective / 목표), ta có certificate rằng cả hai optimal mà không cần enumerate alternatives.

## 13. Complementary slackness

Một primal tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건) có slack:

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

Tương tự, positive primal variable liên hệ với binding dual ràng buộc (constraint / 제약조건).

Đây là LP-specialized phiên bản (version / 버전) của KKT complementary slackness.

## 14. Worked example: môi trường vận hành (production / 운영 환경) và shadow prices

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

Mục tiêu (objective / 목표):

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

Cả hai các ràng buộc (constraints / 제약조건들) active.

Nếu tài nguyên (resource / 자원) của first ràng buộc (constraint / 제약조건) tăng nhẹ, optimal mục tiêu (objective / 목표) có thể tăng theo dual multiplier tương ứng cho tới khi active-set cấu trúc (structure / 구조) thay đổi.

Đây là sensitivity interpretation, không phải toàn cục (global / 전역) law cho mọi mức perturbation.

## 15. Sensitivity phân tích (analysis / 분석) và allowable phạm vi (range / 범위)

Shadow price thường chỉ valid trong một phạm vi (range / 범위) nơi optimal basis không đổi.

Nếu thay `b_i` quá mạnh, active các ràng buộc (constraints / 제약조건들) có thể đổi và marginal giá trị (value / 값) cũng đổi.

Vì vậy đầu ra (output / 출력) kiểu:

```text
shadow price = 5
```

không nên đọc là “mỗi tài nguyên (resource / 자원) đơn vị (unit / 단위) mãi mãi worth 5”. Nó là cục bộ (local / 로컬) sensitivity kết quả (result / 결과) theo hiện tại (current / 현재) LP regime.

## 16. Duality và KKT

LP là convex tối ưu hóa (optimization / 최적화) với tuyến tính (linear / 선형) các ràng buộc (constraints / 제약조건들).

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

Lý thuyết (theory / 이론) hiện đại cho polynomial-time guarantees cho LP.

Practical solver choice phụ thuộc:

```text
problem size
sparsity
warm starts
need for basis/sensitivity info
numerical conditioning
```

Không có quy tắc (rule / 규칙) “simplex luôn tốt hơn” hoặc “interior-point luôn mới hơn nên tốt hơn”.

## 18. Integer programming: discreteness phá convex simplicity

Nếu quyết định (decision / 결정) phải integer:

```math
x_i\in\mathbb Z
```

hoặc nhị phân (binary / 이진):

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

Branch-and-bound dùng bound này để prune tìm kiếm (search / 검색) cây (tree / 트리).

## 19. Integrality gap

Difference giữa integer optimum và LP relaxation optimum gọi broadly là **integrality gap**.

Nếu gap nhỏ, LP relaxation rất informative.
Nếu gap lớn, rounding naive có thể tệ.

Đây là reason relaxation chất lượng (quality / 품질) quan trọng trong combinatorial tối ưu hóa (optimization / 최적화).

## 20. Total unimodularity: khi LP tự cho integer solution

Một số structured matrices như mạng (network / 네트워크) incidence matrices có thuộc tính (property / 속성) **total unimodularity**.

Với integer right-hand side phù hợp, LP vertices tự integer.

Điều này giải thích vì sao một số đồ thị (graph / 그래프) problems có polynomial LP formulations dù nhìn giống discrete tối ưu hóa (optimization / 최적화).

Cấu trúc (structure / 구조) ma trận (matrix / 행렬) có thể biến “integer-looking bài toán (problem / 문제)” thành pure LP tractable bài toán (problem / 문제).

## 21. mạng (network / 네트워크) luồng (flow / 흐름) như structured LP

Max luồng (flow / 흐름) có variables trên edges:

```math
f_e
```

Các ràng buộc (constraints / 제약조건들) gồm sức chứa (capacity / 용량):

```math
0\le f_e\le c_e
```

và luồng (flow / 흐름) conservation tại intermediate nodes.

Mục tiêu (objective / 목표) maximize total source-to-sink luồng (flow / 흐름).

Đồ thị (graph / 그래프) cấu trúc (structure / 구조) cho specialized algorithms nhanh hơn generic LP.

Max-flow/min-cut theorem cũng là một duality statement: max primal luồng (flow / 흐름) giá trị (value / 값) bằng min cut sức chứa (capacity / 용량).

## 22. LP trong Finance

Simplified portfolio allocation có thể là LP nếu mục tiêu (objective / 목표)/rủi ro (risk / 위험) các ràng buộc (constraints / 제약조건들) được linearized.

Ví dụ:

```text
maximize expected return
subject to budget
sector exposure limits
transaction bounds
```

Nhưng classical variance rủi ro (risk / 위험):

```math
w^T\Sigma w
```

là quadratic, nên bài toán (problem / 문제) trở thành quadratic programming.

Mô hình (model / 모델) lớp (class / 클래스) phải follow actual cấu trúc (structure / 구조), không ép mọi tối ưu hóa (optimization / 최적화) thành LP.

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

Một hệ thống (system / 시스템) thiết kế (design / 설계) lesson quan trọng:

> Solver chỉ optimize mô hình (model / 모델) đã viết; mô hình (model / 모델) sai thì optimum có thể rất chính xác nhưng operationally vô nghĩa.

## 24. Numerical considerations

LP lý thuyết (theory / 이론) dùng chính xác (exact / 정확한) real arithmetic, nhưng solver dùng floating điểm (point / 지점).

Problems có coefficients khác quy mô (scale / 규모) quá lớn có thể gây numerical difficulty.

Scaling, presolve và tolerances ảnh hưởng practical kết quả (result / 결과).

Ràng buộc (constraint / 제약조건):

```math
10^{-9}x+10^9y\le1
```

có severe quy mô (scale / 규모) imbalance.

Tối ưu hóa (optimization / 최적화) status như “feasible within tolerance” không phải chính xác (exact / 정확한) symbolic proof trong floating-point hiện thực (implementation / 구현).

## 25. dùng chung (common / 공통) thất bại (failure / 실패) modes

### Mục tiêu (objective / 목표) misspecification

Nếu mục tiêu (objective / 목표) không capture real chi phí (cost / 비용)/giá trị (value / 값), solver sẽ optimize wrong proxy.

### Missing các ràng buộc (constraints / 제약조건들)

Unbounded solution thường reveal missing vật lý (physical / 물리적)/nghiệp vụ (business / 비즈니스) limit.

### Arbitrary rounding

Rounding fractional LP solution có thể violate các ràng buộc (constraints / 제약조건들).

### Shadow price overinterpretation

Dual sensitivity thường cục bộ (local / 로컬) theo hiện tại (current / 현재) basis/regime.

### Ignoring bất định (uncertainty / 불확실성)

Deterministic LP với uncertain demand có thể produce brittle plan. Robust/stochastic tối ưu hóa (optimization / 최적화) thêm bất định (uncertainty / 불확실성) explicitly.

## Liên kết kiến thức (knowledge connection / 지식 연결)

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

## Mô hình tư duy (mental model / 사고 모델)

> LP là hình học (geometry / 기하학) của decisions dưới tuyến tính (linear / 선형) các ràng buộc (constraints / 제약조건들). Simplex nhìn feasible polyhedron qua các bases/vertices. Duality biến các ràng buộc (constraints / 제약조건들) thành prices và tạo certificate của optimality. Khi thêm integrality, hình học (geometry / 기하학) continuous không còn đủ và tìm kiếm (search / 검색)/combinatorics quay trở lại.

## Dùng chung (common / 공통) Misconceptions

“Programming” trong tuyến tính (linear / 선형) programming nghĩa planning, không phải coding. LP optimum không nhất thiết unique. Vertex theorem không có nghĩa phải brute-force mọi corners. Simplex worst-case exponential không đồng nghĩa unusable trong practice. LP relaxation không phải integer solution. Dual variable là sensitivity quantity dưới các giả định (assumptions / 가정들), không phải universal economic truth.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 optimization](./00_optimization.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
