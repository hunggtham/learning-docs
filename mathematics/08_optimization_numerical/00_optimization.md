# Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**. Route đi từ decision variables/objective → constraints và feasible set → geometry, convexity và duality → algorithms, sensitivity và numerical limits → portfolio/engineering examples, để mô hình hóa đi trước thuật toán.

Tối ưu hóa (optimization / 최적화) không bắt đầu bằng độ dốc (gradient / 기울기) descent hay Lagrange multiplier. Nó bắt đầu bằng một modeling question:

> Ta được phép thay đổi điều gì, đang cố làm tốt điều gì, và các ràng buộc (constraints / 제약조건들) nào định nghĩa một solution hợp lệ?

Một optimizer cực mạnh vẫn có thể cho kết quả vô dụng nếu mục tiêu (objective / 목표) đo sai goal hoặc feasible set bỏ sót ràng buộc (constraint / 제약조건) quan trọng. Vì vậy tối ưu hóa (optimization / 최적화) là sự kết hợp của **modeling + mathematical cấu trúc (structure / 구조) + computation**.

## Cấu trúc tối thiểu của một tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)

General form:

```math
\min_x f(x)
```

subject to

```math
g_i(x)\le0,
```

```math
h_j(x)=0.
```

`x` là quyết định (decision / 결정) variable. `f` là mục tiêu (objective / 목표). các ràng buộc (constraints / 제약조건들) xác định feasible set.

Một điểm (point / 지점) có mục tiêu (objective / 목표) rất tốt nhưng violate ràng buộc (constraint / 제약조건) không phải solution.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Cấu trúc tối thiểu của một tối ưu hóa (optimization / 최적화) bài toán (problem / 문제)** nêu quy tắc; **Worked modeling example — portfolio allocation đơn giản** thử quy tắc trong tình huống, rồi **Cục bộ (local / 로컬) optimum và toàn cục (global / 전역) optimum** mở rộng hệ quả.

## Worked modeling example — portfolio allocation đơn giản

Giả sử weights `w_i` của assets phải sum to one:

```math
\sum_iw_i=1.
```

Nếu long-only:

```math
w_i\ge0.
```

Expected return:

```math
\mu^Tw.
```

Variance rủi ro (risk / 위험):

```math
w^T\Sigma w.
```

Một mean-variance formulation có thể là

```math
\min_w
\frac12w^T\Sigma w-\lambda\mu^Tw
```

subject to ngân sách (budget / 예산)/position các ràng buộc (constraints / 제약조건들).

Parameter `\lambda` encodes sự đánh đổi (trade-off / 트레이드오프) preference. Mathematics không tự quyết định investor nên chấp nhận rủi ro (risk / 위험) bao nhiêu; mục tiêu (objective / 목표) embeds that choice.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Worked modeling example — portfolio allocation đơn giản** nêu quy tắc; **Cục bộ (local / 로컬) optimum và toàn cục (global / 전역) optimum** thử quy tắc trong tình huống, rồi **Convexity: cấu trúc (structure / 구조) biến cục bộ (local / 로컬) thành toàn cục (global / 전역)** mở rộng hệ quả.

## Cục bộ (local / 로컬) optimum và toàn cục (global / 전역) optimum

`x^*` là cục bộ (local / 로컬) minimum nếu nó tốt hơn points đủ gần.

Nó là toàn cục (global / 전역) minimum nếu

```math
f(x^*)\le f(x)
```

cho mọi feasible `x`.

Nonconvex problems có thể có nhiều cục bộ (local / 로컬) minima và saddle points. First-order methods often reason locally; toàn cục (global / 전역) guarantees cần extra cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Convexity: cấu trúc (structure / 구조) biến cục bộ (local / 로컬) thành toàn cục (global / 전역)** nối từ **Cục bộ (local / 로컬) optimum và toàn cục (global / 전역) optimum** sang **First-order convexity điều kiện (condition / 조건)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Convexity: cấu trúc (structure / 구조) biến cục bộ (local / 로컬) thành toàn cục (global / 전역)

Hàm (function / 함수) `f` convex nếu

```math
f(tx+(1-t)y)
\le
_tf(x)+(1-t)f(y),
\qquad 0\le t\le1.
```

Correct notation:

```math
f(tx+(1-t)y)
\le
 t f(x)+(1-t)f(y).
```

Geometrically, chord giữa hai đồ thị (graph / 그래프) points nằm above đồ thị (graph / 그래프).

Nếu feasible set convex và mục tiêu (objective / 목표) convex, every cục bộ (local / 로컬) minimum is toàn cục (global / 전역). Đây là lý do convexity cực kỳ valuable: cục bộ (local / 로컬) conditions trở thành toàn cục (global / 전역) certificates.

Strict convexity còn giúp uniqueness under suitable conditions.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **First-order convexity điều kiện (condition / 조건)** nối từ **Convexity: cấu trúc (structure / 구조) biến cục bộ (local / 로컬) thành toàn cục (global / 전역)** sang **Second-order viewpoint**, vì cơ chế trước tạo đầu vào cho bước sau.

## First-order convexity điều kiện (condition / 조건)

Nếu `f` differentiable và convex:

```math
f(y)
\ge
f(x)+\nabla f(x)^T(y-x).
```

Tangent hyperplane nằm dưới đồ thị (graph / 그래프) everywhere.

Nếu

```math
\nabla f(x^*)=0,
```

then

```math
f(y)\ge f(x^*)
```

cho mọi `y`; stationary điểm (point / 지점) là toàn cục (global / 전역) minimum.

Đây là proof idea behind “độ dốc (gradient / 기울기) zero is enough” trong convex unconstrained tối ưu hóa (optimization / 최적화).

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Second-order viewpoint** nối từ **First-order convexity điều kiện (condition / 조건)** sang **Độ dốc (gradient / 기울기) descent được derive từ cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Second-order viewpoint

Nếu twice differentiable, convexity liên hệ Hessian:

```math
H_f(x)\succeq0
```

trên convex lĩnh vực (domain / 도메인).

Positive-semidefinite Hessian nghĩa curvature không downward theo bất kỳ direction nào.

Conditioning của Hessian quyết định tối ưu hóa (optimization / 최적화) hình học (geometry / 기하학). Nếu eigenvalues chênh lớn, mức (level / 수준) sets elongated và vanilla độ dốc (gradient / 기울기) descent có thể zig-zag/chậm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Độ dốc (gradient / 기울기) descent được derive từ cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** nối từ **Second-order viewpoint** sang **Worked quadratic example — học tập (learning / 학습) tỷ lệ (rate / 비율) và curvature**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ dốc (gradient / 기울기) descent được derive từ cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)

Taylor first-order:

```math
f(x+\Delta)
\approx
f(x)+\nabla f(x)^T\Delta.
```

Muốn giảm `f` với fixed small step norm, chọn direction opposite độ dốc (gradient / 기울기):

```math
\Delta=-\eta\nabla f(x).
```

Cập nhật (update / 업데이트):

```math
x_{k+1}=x_k-\eta\nabla f(x_k).
```

Học tập (learning / 학습) tỷ lệ (rate / 비율) `\eta` không phải cosmetic hyperparameter. Quá lớn có thể overshoot/diverge; quá nhỏ convergence rất chậm.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Độ dốc (gradient / 기울기) descent được derive từ cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** nêu quy tắc; **Worked quadratic example — học tập (learning / 학습) tỷ lệ (rate / 비율) và curvature** thử quy tắc trong tình huống, rồi **Các ràng buộc (constraints / 제약조건들) thay đổi hình học (geometry / 기하학) của allowable movement** mở rộng hệ quả.

## Worked quadratic example — học tập (learning / 학습) tỷ lệ (rate / 비율) và curvature

Cho

```math
f(x)=\frac12ax^2,
\qquad a>0.
```

Độ dốc (gradient / 기울기):

```math
f'(x)=ax.
```

Độ dốc (gradient / 기울기) descent:

```math
x_{k+1}
=(1-\eta a)x_k.
```

Converge khi

```math
|1-\eta a|<1,
```

suy ra

```math
0<\eta<\frac2a.
```

Curvature `a` giới hạn stable step kích thước (size / 크기). Trong many dimensions, largest Hessian eigenvalue đóng role tương tự.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Worked quadratic example — học tập (learning / 학습) tỷ lệ (rate / 비율) và curvature** nêu quy tắc; **Các ràng buộc (constraints / 제약조건들) thay đổi hình học (geometry / 기하학) của allowable movement** thử quy tắc trong tình huống, rồi **Lagrange multipliers: alignment của normals** mở rộng hệ quả.

## Các ràng buộc (constraints / 제약조건들) thay đổi hình học (geometry / 기하학) của allowable movement

Unconstrained optimum có thể move mọi direction. Constrained optimum chỉ được move trong feasible directions.

Với equality ràng buộc (constraint / 제약조건)

```math
g(x)=0,
```

feasible tangent directions `d` thỏa locally

```math
\nabla g(x)^Td=0.
```

Nếu mục tiêu (objective / 목표) độ dốc (gradient / 기울기) có thành phần (component / 컴포넌트) tangent, ta còn có thể improve. Tại smooth constrained optimum, độ dốc (gradient / 기울기) mục tiêu (objective / 목표) phải nằm trong span ràng buộc (constraint / 제약조건) normals.

Đó là intuition của Lagrange multipliers.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Lagrange multipliers: alignment của normals** nối từ **Các ràng buộc (constraints / 제약조건들) thay đổi hình học (geometry / 기하학) của allowable movement** sang **Inequality các ràng buộc (constraints / 제약조건들) và KKT**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lagrange multipliers: alignment của normals

Optimize `f(x)` subject to

```math
g(x)=c.
```

At regular constrained optimum:

```math
\nabla f(x^*)
=
\lambda\nabla g(x^*).
```

Multiplier `\lambda` còn có shadow-price interpretation: under suitable conditions, nó đo sensitivity của optimal mục tiêu (objective / 목표) với small relaxation/tightening ràng buộc (constraint / 제약조건).

Finance, economics và operations research dùng interpretation này để price scarce resources.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Inequality các ràng buộc (constraints / 제약조건들) và KKT** nối từ **Lagrange multipliers: alignment của normals** sang **Duality: tối ưu hóa (optimization / 최적화) nhìn từ prices/certificates**, vì cơ chế trước tạo đầu vào cho bước sau.

## Inequality các ràng buộc (constraints / 제약조건들) và KKT

For

```math
g_i(x)\le0,
```

KKT conditions include:

- primal feasibility;
- dual feasibility `\lambda_i\ge0`;
- stationarity;
- complementary slackness

```math
\lambda_i g_i(x)=0.
```

Complementary slackness means inactive ràng buộc (constraint / 제약조건) (`g_i<0`) has zero multiplier; positive multiplier can appear only when ràng buộc (constraint / 제약조건) binds.

KKT can be necessary under ràng buộc (constraint / 제약조건) qualifications; in convex problems with suitable conditions it often becomes sufficient.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Duality: tối ưu hóa (optimization / 최적화) nhìn từ prices/certificates** nối từ **Inequality các ràng buộc (constraints / 제약조건들) và KKT** sang **Tuyến tính (linear / 선형) programming: extreme-point hình học (geometry / 기하학)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Duality: tối ưu hóa (optimization / 최적화) nhìn từ prices/certificates

Primal bài toán (problem / 문제) chooses decisions. Dual bài toán (problem / 문제) often assigns multipliers/prices to các ràng buộc (constraints / 제약조건들).

Weak duality gives bound: dual mục tiêu (objective / 목표) cannot beat primal optimum in wrong direction. Strong duality under suitable convex conditions means bounds meet exactly.

Dual variables help sensitivity phân tích (analysis / 분석) and prove optimality, not only compute answers.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Tuyến tính (linear / 선형) programming: extreme-point hình học (geometry / 기하학)** nối từ **Duality: tối ưu hóa (optimization / 최적화) nhìn từ prices/certificates** sang **Discrete tối ưu hóa (optimization / 최적화): calculus không còn đủ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tuyến tính (linear / 선형) programming: extreme-point hình học (geometry / 기하학)

Tuyến tính (linear / 선형) program:

```math
\min c^Tx
```

subject to tuyến tính (linear / 선형) các ràng buộc (constraints / 제약조건들).

Feasible region là polyhedron. tuyến tính (linear / 선형) mục tiêu (objective / 목표) contours là parallel hyperplanes. If finite optimum exists, an optimum can be found at an extreme điểm (point / 지점)/face.

Simplex exploits this hình học (geometry / 기하학) by moving across vertices; interior-point methods travel through interior using different computational chiến lược (strategy / 전략).

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Discrete tối ưu hóa (optimization / 최적화): calculus không còn đủ** nối từ **Tuyến tính (linear / 선형) programming: extreme-point hình học (geometry / 기하학)** sang **Động (dynamic / 동적) programming và Bellman principle**, vì cơ chế trước tạo đầu vào cho bước sau.

## Discrete tối ưu hóa (optimization / 최적화): calculus không còn đủ

Nếu variables integer/nhị phân (binary / 이진), feasible set is disconnected.

Examples:

- scheduling;
- routing;
- knapsack;
- assignment;
- facility location.

Derivative may describe continuous relaxation but cannot directly choose discrete combinatorial trạng thái (state / 상태).

Methods include động (dynamic / 동적) programming, branch-and-bound, cutting planes, relaxations, heuristics và approximation algorithms.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Động (dynamic / 동적) programming và Bellman principle** nối từ **Discrete tối ưu hóa (optimization / 최적화): calculus không còn đủ** sang **Multi-objective tối ưu hóa (optimization / 최적화) và Pareto frontier**, vì cơ chế trước tạo đầu vào cho bước sau.

## Động (dynamic / 동적) programming và Bellman principle

Sequential tối ưu hóa (optimization / 최적화) has trạng thái (state / 상태) `s`, hành động (action / 동작) `a`, chuyển tiếp (transition / 전이) and future giá trị (value / 값).

Bellman idea:

```math
V(s)
=
\min_a
\{c(s,a)+V(s')\}
```

in deterministic simplified form.

Optimal solution has optimal substructure: once first quyết định (decision / 결정) chosen, remaining chính sách (policy / 정책) must itself be optimal for resulting trạng thái (state / 상태).

This connects tối ưu hóa (optimization / 최적화) with điều khiển (control / 제어), reinforcement học tập (learning / 학습) and shortest-path algorithms.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Multi-objective tối ưu hóa (optimization / 최적화) và Pareto frontier** nối từ **Động (dynamic / 동적) programming và Bellman principle** sang **Robust tối ưu hóa (optimization / 최적화): optimize when parameters are uncertain**, vì cơ chế trước tạo đầu vào cho bước sau.

## Multi-objective tối ưu hóa (optimization / 최적화) và Pareto frontier

Real các hệ thống (systems / 시스템들) rarely optimize only one chỉ số (metric / 지표). chi phí (cost / 비용), độ trễ (latency / 지연 시간), độ tin cậy (reliability / 신뢰성), fairness, return and rủi ro (risk / 위험) may xung đột (conflict / 충돌).

A solution is Pareto optimal if no mục tiêu (objective / 목표) can improve without worsening at least one other.

Weighted-sum mục tiêu (objective / 목표)

```math
\min_x
\sum_kw_kf_k(x)
```

encodes preferences but can hide sự đánh đổi (trade-off / 트레이드오프) cấu trúc (structure / 구조). Choosing weights is a chính sách (policy / 정책)/nghiệp vụ (business / 비즈니스) quyết định (decision / 결정), not purely mathematical deduction.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Robust tối ưu hóa (optimization / 최적화): optimize when parameters are uncertain** nối từ **Multi-objective tối ưu hóa (optimization / 최적화) và Pareto frontier** sang **AI liên kết (connection / 연결) — huấn luyện (training / 학습) is tối ưu hóa (optimization / 최적화) under mô hình (model / 모델) các giả định (assumptions / 가정들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Robust tối ưu hóa (optimization / 최적화): optimize when parameters are uncertain

If mô hình (model / 모델) parameters uncertain, optimizing nominal estimate can produce fragile solution.

Robust tối ưu hóa (optimization / 최적화) asks for hiệu năng (performance / 성능) across an bất định (uncertainty / 불확실성) set. Stochastic tối ưu hóa (optimization / 최적화) optimizes expected/risk-sensitive mục tiêu (objective / 목표) over distributions.

This is important in portfolio allocation, supply chains, điều khiển (control / 제어) and ML phân phối (distribution / 분포) shift.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, sau nội dung của **Robust tối ưu hóa (optimization / 최적화): optimize when parameters are uncertain**, **AI liên kết (connection / 연결) — huấn luyện (training / 학습) is tối ưu hóa (optimization / 최적화) under mô hình (model / 모델) các giả định (assumptions / 가정들)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) minimization** mở rộng hệ quả hoặc giới hạn liên quan.

## AI liên kết (connection / 연결) — huấn luyện (training / 학습) is tối ưu hóa (optimization / 최적화) under mô hình (model / 모델) các giả định (assumptions / 가정들)

Neural-network huấn luyện (training / 학습) minimizes empirical mất mát (loss / 손실):

```math
\min_\theta
\frac1n\sum_{i=1}^n\ell(f_\theta(x_i),y_i).
```

But low huấn luyện (training / 학습) mất mát (loss / 손실) does not guarantee generalization. tối ưu hóa (optimization / 최적화) mục tiêu (objective / 목표) is proxy for desired real-world hiệu năng (performance / 성능).

Regularization, kiểm tra hợp lệ (validation / 검증) and dữ liệu (data / 데이터) phân phối (distribution / 분포) các giả định (assumptions / 가정들) sit outside pure tối ưu hóa (optimization / 최적화) hình học (geometry / 기하학).

SGD uses noisy độ dốc (gradient / 기울기) estimates to trade computation per step against variance.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) minimization** nối từ **AI liên kết (connection / 연결) — huấn luyện (training / 학습) is tối ưu hóa (optimization / 최적화) under mô hình (model / 모델) các giả định (assumptions / 가정들)** sang **Finance liên kết (connection / 연결) — return, rủi ro (risk / 위험), các ràng buộc (constraints / 제약조건들)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) minimization

Stable equilibria often minimize potential năng lượng (energy / 에너지). Variational principles formulate vật lý (physical / 물리적) laws as tối ưu hóa (optimization / 최적화) over functions/paths.

This connects calculus of variations, PDEs, mechanics and optimal điều khiển (control / 제어).

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Finance liên kết (connection / 연결) — return, rủi ro (risk / 위험), các ràng buộc (constraints / 제약조건들)** nối từ **Physics liên kết (connection / 연결) — năng lượng (energy / 에너지) minimization** sang **“Optimizer’s curse” và mục tiêu (objective / 목표) misspecification**, vì cơ chế trước tạo đầu vào cho bước sau.

## Finance liên kết (connection / 연결) — return, rủi ro (risk / 위험), các ràng buộc (constraints / 제약조건들)

Portfolio tối ưu hóa (optimization / 최적화) makes trade-offs tường minh (explicit / 명시적) but is highly sensitive to estimates of expected returns/covariance. Optimizer can amplify estimation noise by exploiting uncertain directions.

Thus robust các ràng buộc (constraints / 제약조건들), shrinkage and regularization are not afterthoughts; they respond to mô hình (model / 모델) bất định (uncertainty / 불확실성).

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **“Optimizer’s curse” và mục tiêu (objective / 목표) misspecification** nối từ **Finance liên kết (connection / 연결) — return, rủi ro (risk / 위험), các ràng buộc (constraints / 제약조건들)** sang **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes**, vì cơ chế trước tạo đầu vào cho bước sau.

## “Optimizer’s curse” và mục tiêu (objective / 목표) misspecification

If mục tiêu (objective / 목표) imperfectly represents desired kết quả (outcome / 결과), stronger optimizer may exploit loopholes more aggressively.

Examples include recommendation các hệ thống (systems / 시스템들) maximizing engagement proxies, schedules minimizing mean độ trễ (latency / 지연 시간) while hurting tail độ trễ (latency / 지연 시간), or portfolios chasing unstable estimated alpha.

Tối ưu hóa (optimization / 최적화) does exactly what mục tiêu (objective / 목표)/các ràng buộc (constraints / 제약조건들) say, not what author vaguely intended.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** nối từ **“Optimizer’s curse” và mục tiêu (objective / 목표) misspecification** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Độ dốc (gradient / 기울기) methods assume differentiability or usable generalized gradients. Convex guarantees require convexity. KKT requires ràng buộc (constraint / 제약조건) qualifications for necessity and stronger cấu trúc (structure / 구조) for sufficiency.

Numerical scaling matters: badly scaled variables/các ràng buộc (constraints / 제약조건들) harm solver hiệu năng (performance / 성능). mô hình (model / 모델) parameters may be uncertain. Discrete problems can be computationally hard despite simple-looking objectives.

> **Nối mạch:** Trong **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> tối ưu hóa (optimization / 최적화) is hình học (geometry / 기하학) of choice under các ràng buộc (constraints / 제약조건들). The mục tiêu (objective / 목표) defines what “better” means; feasible set defines where movement is allowed; derivatives describe cục bộ (local / 로컬) improvement; convexity tells when cục bộ (local / 로컬) thông tin (information / 정보) is globally trustworthy; dual variables price các ràng buộc (constraints / 제약조건들); động (dynamic / 동적) programming extends the same idea through thời gian (time / 시간). The optimizer is only as meaningful as the mô hình (model / 모델) it is asked to optimize.

> **Nối mạch:** Ở chặng này của **Tối ưu hóa: mục tiêu (objective / 목표), feasible set và hình học (geometry / 기하학) của sự đánh đổi (trade-off / 트레이드오프)**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“tối ưu hóa (optimization / 최적화) means take derivative and set zero.”** That handles only a narrow smooth unconstrained lớp (class / 클래스).

**“cục bộ (local / 로컬) minimum is good enough because optimizer found it.”** Depends on nonconvex landscape and bài toán (problem / 문제) goals.

**“Convex means hàm (function / 함수) looks like a bowl in 2D only.”** Convexity is a high-dimensional inequality/hình học (geometry / 기하학) thuộc tính (property / 속성).

**“KKT conditions always prove toàn cục (global / 전역) optimum.”** Not without conditions such as convexity and ràng buộc (constraint / 제약조건) qualifications.

**“Best mục tiêu (objective / 목표) giá trị (value / 값) means best real-world quyết định (decision / 결정).”** Only if mục tiêu (objective / 목표) and các ràng buộc (constraints / 제약조건들) correctly encode real goal and bất định (uncertainty / 불확실성).

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
