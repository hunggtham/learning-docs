# Ứng dụng của đạo hàm: shape, approximation, sensitivity và tối ưu hóa (optimization / 최적화)

> **Mạch đọc:** Đọc **Ứng dụng của đạo hàm: shape, approximation, sensitivity và tối ưu hóa (optimization / 최적화)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Sign của derivative cho biết direction của movement** sang **trọng yếu (critical / 중요) điểm (point / 지점) chỉ là candidate**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Biết tính đạo hàm chỉ là bước đầu. Sức mạnh thật sự đến khi ta dùng derivative để **đọc hành vi (behavior / 동작) của một hàm (function / 함수)**, xây approximation, kiểm tra sensitivity và tìm optimum dưới các ràng buộc (constraints / 제약조건들).

Một hàm (function / 함수) có thể complicated globally nhưng derivative cho cục bộ (local / 로컬) thông tin (information / 정보) tại từng điểm (point / 지점). Nếu ghép những cục bộ (local / 로컬) clues lại, ta hiểu shape của toàn bộ đồ thị (graph / 그래프).

## Sign của derivative cho biết direction của movement

Nếu

```math
f'(x)>0
```

trên một interval, `f` tăng ở đó. Nếu

```math
f'(x)<0,
```

`f` giảm.

Lý do intuitive: derivative là cục bộ (local / 로컬) slope. Positive slope nghĩa step nhỏ theo `x` tạo positive first-order thay đổi (change / 변경).

Nhưng statement formal cần các giả định (assumptions / 가정들) phù hợp như differentiability trên interval. Ta không nên biến sign quy tắc (rule / 규칙) thành shortcut tách rời theorem.

## Trọng yếu (critical / 중요) điểm (point / 지점) chỉ là candidate

Trọng yếu (critical / 중요) điểm (point / 지점) thường là nơi

```math
f'(x)=0
```

hoặc derivative không tồn tại nhưng hàm (function / 함수) vẫn defined.

Đây là nơi first-order hành vi (behavior / 동작) đặc biệt, nhưng không tự động là max/min.

Ví dụ

```math
f(x)=x^3
```

có

```math
f'(0)=0,
```

nhưng 0 không là cục bộ (local / 로컬) max hay min. hàm (function / 함수) vẫn tăng xuyên qua điểm (point / 지점) đó.

## First derivative kiểm thử (test / 테스트): nhìn sign thay đổi (change / 변경) thay vì chỉ nhìn zero

Nếu derivative đổi từ positive sang negative, hàm (function / 함수) chuyển từ tăng sang giảm, nên có cục bộ (local / 로컬) maximum.

Nếu đổi từ negative sang positive, có cục bộ (local / 로컬) minimum.

Nếu không đổi sign, trọng yếu (critical / 중요) điểm (point / 지점) có thể là flat inflection hoặc higher-order hành vi (behavior / 동작).

Đây là lập luận (reasoning / 추론) robust hơn việc chỉ solve `f'=0`.

## Second derivative: slope itself đang thay đổi ra sao?

Second derivative

```math
f''(x)
```

là derivative của slope.

Nếu `f''>0`, slope đang tăng: đồ thị (graph / 그래프) concave up. Nếu `f''<0`, slope đang giảm: đồ thị (graph / 그래프) concave down.

Tại trọng yếu (critical / 중요) điểm (point / 지점) `x_0` với

```math
f'(x_0)=0,
```

nếu

```math
f''(x_0)>0,
```

Cục bộ (local / 로컬) quadratic mô hình (model / 모델) có curvature upward, nên thường là cục bộ (local / 로컬) minimum. Nếu `f''<0`, cục bộ (local / 로컬) maximum.

Nếu `f''=0`, kiểm thử (test / 테스트) inconclusive. `x^4` tại 0 vẫn là minimum dù second derivative zero.

## Taylor viewpoint: vì sao second derivative kiểm thử (test / 테스트) hoạt động?

Near `x_0`:

```math
f(x_0+h)
\approx
f(x_0)+f'(x_0)h+
\frac12f''(x_0)h^2.
```

Tại trọng yếu (critical / 중요) điểm (point / 지점), first-order term vanish:

```math
f(x_0+h)-f(x_0)
\approx
\frac12f''(x_0)h^2.
```

Vì `h^2\ge0`, sign của `f''` quyết định cục bộ (local / 로컬) curvature first nonzero thứ tự (order / 순서). Đây là reason behind kiểm thử (test / 테스트), không phải quy tắc (rule / 규칙) arbitrary.

## Inflection điểm (point / 지점) không phải chỉ là nơi `f''=0`

Inflection điểm (point / 지점) cần **thay đổi (change / 변경) of concavity**.

`f''(x_0)=0` chỉ là candidate. Ví dụ

```math
f(x)=x^4
```

có `f''(0)=0` nhưng concavity vẫn upward hai phía, nên không có inflection.

Trong khi

```math
f(x)=x^3
```

đổi concavity quanh 0, nên 0 là inflection điểm (point / 지점).

## Tối ưu hóa (optimization / 최적화): phần khó thường là modeling, không phải differentiation

Một tối ưu hóa (optimization / 최적화) bài toán (problem / 문제) cần ít nhất:

- quyết định (decision / 결정) variables;
- mục tiêu (objective / 목표);
- feasible lĩnh vực (domain / 도메인)/các ràng buộc (constraints / 제약조건들).

Derivative chỉ giúp sau khi mô hình (model / 모델) được viết đúng.

### Worked example — fixed perimeter rectangle

Perimeter fixed `P`:

```math
2x+2y=P.
```

Ràng buộc (constraint / 제약조건) cho

```math
y=\frac P2-x.
```

Area:

```math
A(x)=x\left(\frac P2-x\right).
```

Derivative:

```math
A'(x)=\frac P2-2x.
```

Trọng yếu (critical / 중요) điểm (point / 지점):

```math
x=\frac P4.
```

Then

```math
y=\frac P4.
```

Second derivative

```math
A''(x)=-2<0
```

confirms cục bộ (local / 로컬) maximum, và feasible interval cho thấy đây cũng là toàn cục (global / 전역) maximum.

Học tập (learning / 학습) điểm (point / 지점): ràng buộc (constraint / 제약조건) reduced a two-variable bài toán (problem / 문제) thành one-variable mục tiêu (objective / 목표).

## Ranh giới (boundary / 경계) matters

Trong constrained lĩnh vực (domain / 도메인), optimum có thể nằm ở ranh giới (boundary / 경계) dù derivative không zero.

Ví dụ maximize

```math
f(x)=x
```

trên `[0,1]`. Không có interior trọng yếu (critical / 중요) điểm (point / 지점); toàn cục (global / 전역) maximum là `x=1`.

Do đó practical tối ưu hóa (optimization / 최적화) workflow là:

```text
identify domain
→ find interior critical candidates
→ include boundaries / nondifferentiable points
→ compare objective values or use structural theorem.
```

## Cục bộ (local / 로컬) vs toàn cục (global / 전역) optimum

Derivative tests thường cục bộ (local / 로컬). Một hàm (function / 함수) nonconvex có nhiều cục bộ (local / 로컬) minima.

Nếu hàm (function / 함수) convex trên convex lĩnh vực (domain / 도메인), cục bộ (local / 로컬) minimum trở thành toàn cục (global / 전역) minimum. Đây là reason convexity quan trọng trong tối ưu hóa (optimization / 최적화): nó nâng cục bộ (local / 로컬) lập luận (reasoning / 추론) thành toàn cục (global / 전역) guarantee.

## Sensitivity và lan truyền lỗi (error propagation / 오류 전파)

Cục bộ (local / 로컬) linearization:

```math
\Delta y\approx f'(x)\Delta x.
```

Nếu đầu vào (input / 입력) bất định (uncertainty / 불확실성) khoảng `\sigma_x`, first-order đầu ra (output / 출력) bất định (uncertainty / 불확실성) roughly scales với `|f'(x)|`.

Trong multi-input các hệ thống (systems / 시스템들), độ dốc (gradient / 기울기)/Jacobian thay derivative scalar.

Điều này nối calculus với numerical conditioning và experimental bất định (uncertainty / 불확실성).

## Marginal quantities

Nếu chi phí (cost / 비용) `C(q)` phụ thuộc môi trường vận hành (production / 운영 환경) quantity:

```math
C'(q)
```

là marginal chi phí (cost / 비용): cục bộ (local / 로컬) chi phí (cost / 비용) increase per additional đơn vị (unit / 단위) around hiện tại (current / 현재) `q`.

Nếu revenue `R(q)`:

```math
R'(q)
```

là marginal revenue.

Profit

```math
\Pi(q)=R(q)-C(q)
```

có derivative

```math
\Pi'(q)=R'(q)-C'(q).
```

Interior optimum candidate thỏa

```math
R'(q)=C'(q).
```

Meaning: tăng thêm một đơn vị (unit / 단위) không còn tạo marginal gain vượt marginal chi phí (cost / 비용).

Đây là economic interpretation của first-order điều kiện (condition / 조건).

## Elasticity: sensitivity không phụ thuộc units

Derivative absolute phụ thuộc đơn vị (unit / 단위) quy mô (scale / 규모). Elasticity dùng

```math
E(x)=\frac{x}{f(x)}f'(x).
```

để đo approximate percentage đầu ra (output / 출력) thay đổi (change / 변경) per 1% đầu vào (input / 입력) thay đổi (change / 변경).

Nếu demand `Q(p)` theo price `p`, price elasticity giúp compare sensitivity giữa products có quy mô (scale / 규모) khác nhau.

## Newton's phương thức (method / 메서드): dùng tangent để tìm gốc (root / 루트)

Muốn solve

```math
f(x)=0,
```

linearize quanh hiện tại (current / 현재) guess `x_n`:

```math
f(x)
\approx
f(x_n)+f'(x_n)(x-x_n).
```

Set approximation bằng zero:

```math
0=f(x_n)+f'(x_n)(x_{n+1}-x_n),
```

suy ra

```math
x_{n+1}
=
x_n-rac{f(x_n)}{f'(x_n)}.
```

Phương thức (method / 메서드) nhanh gần a simple gốc (root / 루트) nhưng không globally guaranteed. Small derivative, poor initial guess hoặc multiple roots có thể gây thất bại (failure / 실패).

## Worked Newton example

Tìm `\sqrt2` bằng gốc (root / 루트) của

```math
f(x)=x^2-2.
```

Then

```math
f'(x)=2x.
```

Newton cập nhật (update / 업데이트):

```math
x_{n+1}
=
\frac12\left(x_n+\frac2{x_n}\right).
```

Starting `x_0=1.5`:

```math
x_1\approx1.41667,
```

```math
x_2\approx1.41422.
```

Fast convergence comes from cục bộ (local / 로컬) quadratic lỗi (error / 오류) reduction under suitable conditions.

## Physics liên kết (connection / 연결) — equilibrium và stability

Potential năng lượng (energy / 에너지) `U(x)` tạo force

```math
F(x)=-U'(x).
```

Equilibrium thỏa `U'(x)=0`. Nếu `U''(x)>0`, potential cục bộ (local / 로컬) minimum, thường stable equilibrium. Nếu `U''<0`, cục bộ (local / 로컬) maximum, thường unstable.

Tối ưu hóa (optimization / 최적화) ngôn ngữ (language / 언어) và physics stability share same curvature cấu trúc (structure / 구조).

## AI liên kết (connection / 연결) — gradient-based học tập (learning / 학습)

Huấn luyện (training / 학습) minimizes mất mát (loss / 손실) `L(\theta)`. In one dimension, derivative gives cục bộ (local / 로컬) descent direction. In many dimensions, độ dốc (gradient / 기울기) generalizes it.

But a zero độ dốc (gradient / 기울기) does not guarantee good mô hình (model / 모델): it may be cục bộ (local / 로컬) minimum, saddle điểm (point / 지점), flat region hoặc numerical plateau.

Second-order curvature explains why same học tập (learning / 학습) tỷ lệ (rate / 비율) behaves differently across directions.

## Finance liên kết (connection / 연결) — cục bộ (local / 로컬) Greeks

Option Greeks là derivatives của price theo thị trường (market / 시장) variables. Delta là first derivative theo underlying; gamma là second derivative. They quantify cục bộ (local / 로컬) sensitivity, not chính xác (exact / 정확한) finite move hành vi (behavior / 동작) for arbitrary price jumps.

Again, derivative means cục bộ (local / 로컬) phản hồi (response / 응답), not toàn cục (global / 전역) prediction.

## Các giả định (assumptions / 가정들) và thất bại (failure / 실패) modes

Derivative-based tối ưu hóa (optimization / 최적화) assumes enough smoothness. Nonsmooth objectives require subgradients hoặc other methods.

Stationary điểm (point / 지점) classification can thất bại (fail / 실패) if only low-order derivatives vanish. các ràng buộc (constraints / 제약조건들) can invalidate unconstrained conclusions. Real-world objectives may be noisy, discrete hoặc nonstationary, so symbolic calculus may only approximate operational decision-making.

## Mô hình tư duy (mental model / 사고 모델)

> Derivative applications are about reading a cục bộ (local / 로컬) landscape. First derivative tells which way the terrain slopes; second derivative tells how the slope bends; các ràng buộc (constraints / 제약조건들) tell where movement is allowed. tối ưu hóa (optimization / 최적화) is not “set derivative to zero” but a structured tìm kiếm (search / 검색) over feasible candidates using cục bộ (local / 로컬) hình học (geometry / 기하학) plus toàn cục (global / 전역) các giả định (assumptions / 가정들).

## Dùng chung (common / 공통) Misconceptions

**“`f'=0` nghĩa optimum.”** Chỉ là candidate.

**“Second derivative zero nghĩa inflection.”** Không; concavity phải thực sự thay đổi (change / 변경).

**“Tìm interior trọng yếu (critical / 중요) points là đủ.”** ranh giới (boundary / 경계) và nondifferentiable points có thể chứa toàn cục (global / 전역) optimum.

**“Newton phương thức (method / 메서드) luôn nhanh.”** Nó nhanh khi cục bộ (local / 로컬) các giả định (assumptions / 가정들) tốt; otherwise có thể diverge hoặc converge tới gốc (root / 루트) không mong muốn.

**“Derivative sensitivity là nhân quả (causal / 인과적) tác động (effect / 효과).”** Nó là sensitivity trong mô hình (model / 모델); causality cần các giả định (assumptions / 가정들)/dữ liệu (data / 데이터) khác.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 limits and continuity](./00_limits_and_continuity.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
