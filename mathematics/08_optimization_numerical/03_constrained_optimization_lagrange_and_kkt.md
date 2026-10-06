# Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**. Route đi từ feasible set và objective → equality constraints/tangent geometry → Lagrange multipliers → KKT, constraint qualification và duality → sensitivity/active-set decisions.

Unconstrained tối ưu hóa (optimization / 최적화) hỏi:

```math
\min_x f(x).
```

Nhưng phần lớn bài toán thực tế chỉ cho phép một subset của không gian (space / 공간):

```text
budget ≤ limit
probabilities sum to 1
resources ≥ 0
risk ≤ threshold
latency ≤ SLA
```

Constrained tối ưu hóa (optimization / 최적화) vì vậy không hỏi “điểm thấp nhất của toàn landscape ở đâu?”, mà hỏi:

> Trong **feasible set** được phép, điểm (point / 지점) nào tốt nhất?

Mental luồng (flow / 흐름):

```text
objective
→ feasible set
→ feasible directions
→ active constraints
→ multipliers
→ KKT
→ duality / sensitivity
```

## 1. Feasible set quan trọng ngang mục tiêu (objective / 목표)

Bài toán (problem / 문제):

```math
\min_x f(x)
```

subject to:

```math
g_i(x)\le0,
\qquad
h_j(x)=0.
```

Feasible set:

```math
\mathcal F
=
\{x:g_i(x)\le0,\;h_j(x)=0\}.
```

Tối ưu hóa (optimization / 최적화) chỉ được di chuyển bên trong `\mathcal F`.

Một điểm (point / 지점) có độ dốc (gradient / 기울기) khác zero vẫn có thể là constrained optimum nếu mọi downhill direction đều vi phạm các ràng buộc (constraints / 제약조건들).

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **1. Feasible set quan trọng ngang mục tiêu (objective / 목표)** đặt câu hỏi cần giải quyết; **2. Equality ràng buộc (constraint / 제약조건) và tangent hình học (geometry / 기하학)** biến câu hỏi đó thành những điều kiện không được phá vỡ khi đi vào thực hành. Từ đây, **3. Lagrangian** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Equality ràng buộc (constraint / 제약조건) và tangent hình học (geometry / 기하학)

Xét:

```math
\min f(x)
```

subject to:

```math
g(x)=c.
```

Feasible movement cục bộ (local / 로컬) nằm trong tangent không gian (space / 공간) của mức (level / 수준) set.

Độ dốc (gradient / 기울기) ràng buộc (constraint / 제약조건):

```math
\nabla g
```

vuông góc tangent directions.

Tại regular constrained optimum, directional derivative của `f` theo mọi feasible tangent direction phải zero. Do đó:

```math
\nabla f
```

không có tangent thành phần (component / 컴포넌트) và phải nằm trong normal span:

```math
\nabla f=\lambda\nabla g.
```

Đây là geometric origin của Lagrange multiplier.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **3. Lagrangian** nối từ **2. Equality ràng buộc (constraint / 제약조건) và tangent hình học (geometry / 기하학)** sang **4. Worked example: fixed perimeter rectangle**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Lagrangian

Với equality:

```math
h(x)=0,
```

define:

```math
\mathcal L(x,\nu)=f(x)+\nu h(x).
```

First-order candidate conditions:

```math
\nabla_x\mathcal L=0,
```

```math
h(x)=0.
```

Multiplier `\nu` là coefficient needed để combine ràng buộc (constraint / 제약조건) normal với mục tiêu (objective / 목표) độ dốc (gradient / 기울기).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **3. Lagrangian** nêu quy tắc; **4. Worked example: fixed perimeter rectangle** thử quy tắc trong tình huống, rồi **5. Multiplier như sensitivity / shadow price** mở rộng hệ quả.

## 4. Worked example: fixed perimeter rectangle

Maximize:

```math
A(x,y)=xy
```

subject to:

```math
2x+2y=P.
```

Equivalent:

```math
h(x,y)=x+y-P/2=0.
```

Lagrangian:

```math
\mathcal L
=xy+\nu(P/2-x-y).
```

Stationarity:

```math
y-\nu=0,
```

```math
x-\nu=0.
```

Thus:

```math
x=y.
```

Ràng buộc (constraint / 제약조건) gives square.

Theorem/phương thức (method / 메서드) gives candidate; toàn cục (global / 전역) maximum conclusion còn dựa hình học (geometry / 기하학)/concavity/feasible lĩnh vực (domain / 도메인).

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **4. Worked example: fixed perimeter rectangle** nêu quy tắc; **5. Multiplier như sensitivity / shadow price** thử quy tắc trong tình huống, rồi **6. Inequality ràng buộc (constraint / 제약조건) khác equality ở chỗ có thể inactive** mở rộng hệ quả.

## 5. Multiplier như sensitivity / shadow price

Suppose ràng buộc (constraint / 제약조건):

```math
h(x)=b.
```

Optimal giá trị (value / 값):

```math
V(b).
```

Under suitable regularity/sign convention, multiplier relates to:

```math
\frac{dV}{db}.
```

Interpretation: nếu tài nguyên (resource / 자원) bound được nới nhẹ, optimal mục tiêu (objective / 목표) thay đổi khoảng bao nhiêu?

Operations research/economics gọi đây là shadow price.

Units phải được kiểm tra: multiplier có đơn vị (unit / 단위) “mục tiêu (objective / 목표) per constraint-unit”.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **6. Inequality ràng buộc (constraint / 제약조건) khác equality ở chỗ có thể inactive** nối từ **5. Multiplier như sensitivity / shadow price** sang **7. Lagrangian với inequalities**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Inequality ràng buộc (constraint / 제약조건) khác equality ở chỗ có thể inactive

Consider:

```math
g(x)\le0.
```

At optimum:

```text
g(x)<0 → constraint inactive/slack
g(x)=0 → constraint active
```

Nếu inactive, nó không chặn cục bộ (local / 로컬) movement; multiplier tương ứng nên zero trong KKT cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **7. Lagrangian với inequalities** nối từ **6. Inequality ràng buộc (constraint / 제약조건) khác equality ở chỗ có thể inactive** sang **8. KKT conditions**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Lagrangian với inequalities

For minimization:

```math
\mathcal L(x,\lambda,\nu)
=
f(x)
+
\sum_i\lambda_i g_i(x)
+
\sum_j\nu_jh_j(x),
```

với convention:

```math
g_i(x)\le0.
```

Then inequality multipliers require:

```math
\lambda_i\ge0.
```

Sign convention đổi nếu ràng buộc (constraint / 제약조건) được viết direction khác.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **8. KKT conditions** nối từ **7. Lagrangian với inequalities** sang **9. Complementary slackness là active-set lô-gic (logic / 논리)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. KKT conditions

Karush–Kuhn–Tucker conditions:

### Stationarity

Stationarity yêu cầu gradient của Lagrangian cân bằng theo các hướng khả thi tại nghiệm tối ưu. Nó là điều kiện ứng viên, không tự đảm bảo global optimum nếu bài toán không lồi.

```math
\nabla f(x^*)
+
\sum_i\lambda_i^*\nabla g_i(x^*)
+
\sum_j\nu_j^*\nabla h_j(x^*)
=0.
```

### Primal feasibility

Primal feasibility kiểm tra nghiệm có thỏa các ràng buộc gốc hay không. Một điểm làm objective tốt nhưng vi phạm constraint không phải nghiệm hợp lệ.

```math
g_i(x^*)\le0,
```

```math
h_j(x^*)=0.
```

### Dual feasibility

Dual feasibility giới hạn dấu của multiplier theo loại ràng buộc. Điều kiện này giữ ý nghĩa kinh tế của shadow price và loại nghiệm không phù hợp khỏi hệ KKT.

```math
\lambda_i^*\ge0.
```

### Complementary slackness

Complementary slackness nối constraint đang chặt với multiplier có thể khác không. Nó cho biết ràng buộc nào thực sự “đang trả giá” trong nghiệm tối ưu.

```math
\lambda_i^*g_i(x^*)=0.
```

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **9. Complementary slackness là active-set lô-gic (logic / 논리)** nối từ **8. KKT conditions** sang **10. Worked example: one-sided bound**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Complementary slackness là active-set lô-gic (logic / 논리)

For each inequality:

```text
constraint slack → multiplier = 0
multiplier > 0 → constraint must be active
```

This captures which walls actually hỗ trợ (support / 지원) the optimum.

It is one of the most useful conceptual parts of KKT.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **9. Complementary slackness là active-set lô-gic (logic / 논리)** nêu quy tắc; **10. Worked example: one-sided bound** thử quy tắc trong tình huống, rồi **11. ràng buộc (constraint / 제약조건) qualification: vì sao KKT không automatic?** mở rộng hệ quả.

## 10. Worked example: one-sided bound

Minimize:

```math
f(x)=(x-3)^2
```

subject to:

```math
x\le1.
```

Ghi (write / 쓰기):

```math
g(x)=x-1\le0.
```

Unconstrained minimum `x=3` infeasible. Feasible optimum is ranh giới (boundary / 경계) `x=1`.

Lagrangian:

```math
\mathcal L=(x-3)^2+\lambda(x-1).
```

Stationarity at `x=1`:

```math
2(1-3)+\lambda=0
```

so:

```math
\lambda=4>0.
```

Positive multiplier reflects active ràng buộc (constraint / 제약조건) blocking descent toward `x=3`.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **10. Worked example: one-sided bound** nêu quy tắc; **11. ràng buộc (constraint / 제약조건) qualification: vì sao KKT không automatic?** thử quy tắc trong tình huống, rồi **12. Convexity makes KKT much stronger** mở rộng hệ quả.

## 11. ràng buộc (constraint / 제약조건) qualification: vì sao KKT không automatic?

KKT necessity requires regularity các giả định (assumptions / 가정들).

If ràng buộc (constraint / 제약조건) gradients degenerate or feasible hình học (geometry / 기하학) pathological, multipliers may thất bại (fail / 실패) to exist even at optimum.

Examples of ràng buộc (constraint / 제약조건) qualifications include LICQ and Slater's điều kiện (condition / 조건) in convex settings.

Lesson:

> KKT is a theorem with các giả định (assumptions / 가정들), not a universal algebra recipe.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **12. Convexity makes KKT much stronger** nối từ **11. ràng buộc (constraint / 제약조건) qualification: vì sao KKT không automatic?** sang **13. Slater's điều kiện (condition / 조건) intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Convexity makes KKT much stronger

If:

```text
f convex
g_i convex
h_j affine
```

then feasible set convex.

Under suitable regularity, any KKT điểm (point / 지점) is toàn cục (global / 전역) optimum.

For nonconvex bài toán (problem / 문제), KKT điểm (point / 지점) may be only cục bộ (local / 로컬) candidate or saddle-like constrained stationary điểm (point / 지점).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **13. Slater's điều kiện (condition / 조건) intuition** nối từ **12. Convexity makes KKT much stronger** sang **14. Dual hàm (function / 함수)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Slater's điều kiện (condition / 조건) intuition

For convex inequality bài toán (problem / 문제), existence of a strictly feasible điểm (point / 지점):

```math
g_i(x)<0
```

for all inequalities often provides strong duality via Slater's điều kiện (condition / 조건).

Strict interior feasibility prevents certain ranh giới (boundary / 경계) pathologies.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **14. Dual hàm (function / 함수)** nối từ **13. Slater's điều kiện (condition / 조건) intuition** sang **15. Weak duality**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Dual hàm (function / 함수)

Lagrangian dual hàm (function / 함수):

```math
q(\lambda,\nu)
=
\inf_x\mathcal L(x,\lambda,\nu).
```

For minimization, dual hàm (function / 함수) gives lower bounds on primal optimum for dual-feasible multipliers.

Thus dual bài toán (problem / 문제) searches best lower bound:

```math
\max_{\lambda\ge0,\nu}q(\lambda,\nu).
```

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **15. Weak duality** nối từ **14. Dual hàm (function / 함수)** sang **16. Strong duality**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Weak duality

For any primal feasible `x` and dual feasible `(\lambda,\nu)`:

```math
q(\lambda,\nu)\le f(x).
```

Therefore:

```text
dual optimum ≤ primal optimum
```

for minimization.

This bound holds very generally.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **16. Strong duality** nối từ **15. Weak duality** sang **17. Equality ràng buộc (constraint / 제약조건) example via hình học (geometry / 기하학)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Strong duality

Under suitable convexity/regularity:

```text
dual optimum = primal optimum
```

Dual variables then gain strong sensitivity/economic interpretation.

Duality gap zero becomes both theoretical guarantee and numerical stopping tín hiệu (signal / 신호) in algorithms.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **16. Strong duality** nêu quy tắc; **17. Equality ràng buộc (constraint / 제약조건) example via hình học (geometry / 기하학)** thử quy tắc trong tình huống, rồi **18. Projection as constrained tối ưu hóa (optimization / 최적화)** mở rộng hệ quả.

## 17. Equality ràng buộc (constraint / 제약조건) example via hình học (geometry / 기하학)

Minimize distance from origin:

```math
f(x,y)=x^2+y^2
```

subject to line:

```math
x+y=1.
```

Ràng buộc (constraint / 제약조건) độ dốc (gradient / 기울기):

```math
(1,1).
```

Mục tiêu (objective / 목표) độ dốc (gradient / 기울기):

```math
(2x,2y).
```

At optimum they align:

```math
(2x,2y)=\lambda(1,1),
```

so `x=y`; ràng buộc (constraint / 제약조건) gives:

```math
x=y=1/2.
```

This is orthogonal projection of origin onto the line.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **17. Equality ràng buộc (constraint / 제약조건) example via hình học (geometry / 기하학)** nêu quy tắc; **18. Projection as constrained tối ưu hóa (optimization / 최적화)** thử quy tắc trong tình huống, rồi **19. Projected độ dốc (gradient / 기울기) descent** mở rộng hệ quả.

## 18. Projection as constrained tối ưu hóa (optimization / 최적화)

Projection onto convex set `C`:

```math
\min_{x\in C}\frac12\|x-v\|^2.
```

For tuyến tính (linear / 선형) subspace, solution satisfies orthogonality.

For closed convex set, Euclidean projection is unique.

This links constrained tối ưu hóa (optimization / 최적화) directly with inner-product hình học (geometry / 기하학).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **19. Projected độ dốc (gradient / 기울기) descent** nối từ **18. Projection as constrained tối ưu hóa (optimization / 최적화)** sang **20. Penalty phương thức (method / 메서드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Projected độ dốc (gradient / 기울기) descent

For simple convex feasible set:

```math
x_{k+1}
=\Pi_C(x_k-\eta\nabla f(x_k)).
```

Thuật toán (algorithm / 알고리즘) alternates:

```text
gradient step toward lower objective
→ project back into feasible set
```

Useful when projection is cheap.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **20. Penalty phương thức (method / 메서드)** nối từ **19. Projected độ dốc (gradient / 기울기) descent** sang **21. Barrier phương thức (method / 메서드)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Penalty phương thức (method / 메서드)

Replace hard ràng buộc (constraint / 제약조건) with penalty:

```math
f(x)+\rho\,\phi(g(x)).
```

Large violation increases mục tiêu (objective / 목표).

But finite penalty does not always exactly enforce hard ràng buộc (constraint / 제약조건).

Very large `\rho` can cause poor conditioning.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **21. Barrier phương thức (method / 메서드)** nối từ **20. Penalty phương thức (method / 메서드)** sang **22. xác suất (probability / 확률) simplex**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Barrier phương thức (method / 메서드)

For inequality `g(x)<0`, logarithmic barrier:

```math
-\mu\log(-g(x))
```

blows up near ranh giới (boundary / 경계).

Interior-point methods solve chuỗi (sequence / 시퀀스) of barrier problems as `\mu→0`.

This is fundamentally different from projected methods: stay interior instead of stepping outside then projecting.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **22. xác suất (probability / 확률) simplex** nối từ **21. Barrier phương thức (method / 메서드)** sang **23. Regularization vs các ràng buộc (constraints / 제약조건들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. xác suất (probability / 확률) simplex

Xác suất (probability / 확률) véc-tơ (vector / 벡터):

```math
p_i\ge0,
\qquad
\sum_i p_i=1.
```

Feasible set is simplex.

Many ML problems optimize weights/probabilities on simplex.

Softmax:

```math
p_i=\frac{e^{z_i}}{\sum_je^{z_j}}
```

parameterizes strictly positive interior points automatically.

Encoding các ràng buộc (constraints / 제약조건들) via parameterization can simplify tối ưu hóa (optimization / 최적화) but may thay đổi (change / 변경) hình học (geometry / 기하학)/conditioning.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **23. Regularization vs các ràng buộc (constraints / 제약조건들)** nối từ **22. xác suất (probability / 확률) simplex** sang **24. L1 hình học (geometry / 기하학) và sparsity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Regularization vs các ràng buộc (constraints / 제약조건들)

Problems:

```math
\min f(x)+\lambda R(x)
```

and

```math
\min f(x)
\quad\text{s.t. }R(x)\le c
```

can correspond under suitable convexity and parameter quan hệ (relation / 관계), but not universally one-to-one for every `\lambda,c`.

Penalty and ràng buộc (constraint / 제약조건) are two views of sự đánh đổi (trade-off / 트레이드오프), not always identical implementations.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **24. L1 hình học (geometry / 기하학) và sparsity** nối từ **23. Regularization vs các ràng buộc (constraints / 제약조건들)** sang **25. Portfolio tối ưu hóa (optimization / 최적화) liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. L1 hình học (geometry / 기하학) và sparsity

Ràng buộc (constraint / 제약조건):

```math
\|x\|_1\le c
```

has diamond-like hình học (geometry / 기하학) with corners aligned to coordinate axes.

Quadratic mất mát (loss / 손실) contours touching these corners often produce zero coordinates.

This geometric intuition helps explain why L1 regularization promotes sparsity.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, sau nội dung của **24. L1 hình học (geometry / 기하학) và sparsity**, **25. Portfolio tối ưu hóa (optimization / 최적화) liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **26. tài nguyên (resource / 자원) allocation / shadow price** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. Portfolio tối ưu hóa (optimization / 최적화) liên kết (connection / 연결)

Classical setup:

```math
\min_w w^T\Sigma w
```

subject to:

```math
1^Tw=1
```

and possibly:

```math
\mu^Tw\ge r_0,
\qquad
w\ge0.
```

This combines quadratic mục tiêu (objective / 목표) with equality/inequality các ràng buộc (constraints / 제약조건들).

KKT/duality make the cấu trúc (structure / 구조) transparent.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **25. Portfolio tối ưu hóa (optimization / 최적화) liên kết (connection / 연결)** đặt vấn đề; **26. tài nguyên (resource / 자원) allocation / shadow price** đối chiếu bằng chứng, rồi **27. Second-order conditions** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. tài nguyên (resource / 자원) allocation / shadow price

Suppose mục tiêu (objective / 목표) is profit and ràng buộc (constraint / 제약조건) is CPU sức chứa (capacity / 용량).

Multiplier on sức chứa (capacity / 용량) ràng buộc (constraint / 제약조건) estimates marginal improvement if sức chứa (capacity / 용량) increases one đơn vị (unit / 단위).

A high shadow price says tài nguyên (resource / 자원) is binding/valuable; zero multiplier says extra tài nguyên (resource / 자원) is not locally useful under hiện tại (current / 현재) optimum/mô hình (model / 모델).

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **26. tài nguyên (resource / 자원) allocation / shadow price** đặt vấn đề; **27. Second-order conditions** đối chiếu bằng chứng, rồi **28. Active-set methods** mở rộng hệ quả hoặc giới hạn liên quan.

## 27. Second-order conditions

First-order KKT identifies stationary candidates.

Second-order constrained phân tích (analysis / 분석) examines Hessian of Lagrangian restricted to feasible tangent directions.

Positive curvature on feasible directions supports cục bộ (local / 로컬) minimum classification.

This is constrained analogue of Hessian tests.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **28. Active-set methods** nối từ **27. Second-order conditions** sang **29. Nonconvex caution**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Active-set methods

Algorithms may guess which inequalities are active, solve equality-constrained subproblem, then cập nhật (update / 업데이트) active set.

KKT complementary slackness provides theoretical lô-gic (logic / 논리) behind active-set computation.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **29. Nonconvex caution** nối từ **28. Active-set methods** sang **30. Units and scaling matter**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. Nonconvex caution

Neural/mạng (network / 네트워크)/điều khiển (control / 제어) problems often nonconvex.

KKT conditions can still generate candidates, but:

```text
KKT satisfied ≠ global optimum
```

Toàn cục (global / 전역) guarantees need additional cấu trúc (structure / 구조).

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **30. Units and scaling matter** nối từ **29. Nonconvex caution** sang **Liên kết kiến thức (knowledge connection / 지식 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 30. Units and scaling matter

If one ràng buộc (constraint / 제약조건) uses dollars ~`10^6` and another normalized xác suất (probability / 확률) ~`1`, poorly scaled bài toán (problem / 문제) can cause numerical difficulty.

Rescaling variables/các ràng buộc (constraints / 제약조건들) may improve conditioning without changing underlying feasible set meaning.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, sau nội dung của **30. Units and scaling matter**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đặt KKT cạnh convexity, duality, machine learning và resource allocation. Hãy dùng nó để biết khi nào điều kiện cần trở thành điều kiện đủ và khi nào phải kiểm tra thêm.

```text
gradient geometry
→ tangent/normal spaces
→ Lagrange multipliers
→ KKT active constraints
→ duality / shadow prices
→ convex optimization algorithms
```

Inner products explain projection. tuyến tính (linear / 선형) algebra supplies null/tangent spaces. Finance uses covariance quadratic objectives. AI uses simplex các ràng buộc (constraints / 제약조건들), regularization and projected/proximal methods.

> **Nối mạch:** Trong **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Constrained optimum is a điểm (point / 지점) where all useful downhill directions are blocked by feasible hình học (geometry / 기하학). Multipliers quantify which walls khối (block / 블록) movement and how valuable relaxing those walls would be.

> **Nối mạch:** Ở chặng này của **Tối ưu có ràng buộc, Lagrange multipliers và KKT: hình học (geometry / 기하학) của feasible directions**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

Lagrange/KKT do not automatically give toàn cục (global / 전역) optima. KKT needs ràng buộc (constraint / 제약조건) qualifications. Multiplier sign depends on ràng buộc (constraint / 제약조건) convention. Penalty is not identical to hard ràng buộc (constraint / 제약조건) in every setup. Shadow-price interpretation requires correct mô hình (model / 모델)/units and regularity. Strong duality is not universal outside suitable convex settings.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
