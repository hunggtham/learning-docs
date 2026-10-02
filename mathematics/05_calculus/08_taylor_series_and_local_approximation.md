# Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bắt đầu từ linearization** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Vì sao quadratic term có hệ số 1/2?** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Taylor với xấp xỉ cục bộ và sai số, để chuyển đạo hàm thành một công cụ dự báo trong lân cận điểm.

Derivative bậc một cho slope. Derivative bậc hai cho curvature. Higher derivatives mô tả các lớp cục bộ (local / 로컬) hành vi (behavior / 동작) ngày càng tinh hơn.

Taylor approximation gom toàn bộ thông tin (information / 정보) này thành một polynomial quanh một expansion điểm (point / 지점) `a`.

Mental luồng (flow / 흐름):

```text
function
→ local value
→ local slope
→ local curvature
→ higher-order shape
→ polynomial approximation
→ remainder/error
```

Taylor không phải chỉ là một công thức series. Nó là khung phần mềm (framework / 프레임워크) trả lời:

> Nếu chỉ biết cục bộ (local / 로컬) derivatives tại một điểm (point / 지점), ta có thể reconstruct hoặc approximate hàm (function / 함수) quanh đó đến mức nào?

## 1. Bắt đầu từ linearization

Với differentiable hàm (function / 함수):

```math
f(a+h)
\approx
f(a)+f'(a)h.
```

Đây là first-order Taylor approximation.

Nó nói rằng sufficiently close to `a`, nonlinear hàm (function / 함수) nhìn gần như affine.

Lỗi (error / 오류) first-order thường nhỏ hơn thứ tự (order / 순서) `h` dưới suitable smoothness; nếu có second derivative bounded, lỗi (error / 오류) thường quy mô (scale / 규모) như `O(h^2)`.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **2. Vì sao quadratic term có hệ số 1/2?** tiếp nhận điểm tựa từ **1. Bắt đầu từ linearization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. General Taylor polynomial** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Vì sao quadratic term có hệ số 1/2?

Muốn polynomial

```math
P_2(x)=c_0+c_1(x-a)+c_2(x-a)^2
```

match hàm (function / 함수) giá trị (value / 값), slope và curvature tại `a`.

Conditions:

```math
P_2(a)=f(a)
```

cho

```math
c_0=f(a).
```

Derivative:

```math
P_2'(x)=c_1+2c_2(x-a)
```

nên

```math
c_1=f'(a).
```

Second derivative:

```math
P_2''(x)=2c_2
```

nên

```math
c_2=\frac{f''(a)}{2!}.
```

Factorial không xuất hiện bí ẩn; nó bù cho việc differentiate power nhiều lần.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **3. General Taylor polynomial** tiếp nhận điểm tựa từ **2. Vì sao quadratic term có hệ số 1/2?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Taylor series khác Taylor polynomial** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. General Taylor polynomial

Taylor polynomial bậc `n` quanh `a`:

```math
P_n(x)
=
\sum_{k=0}^{n}
\frac{f^{(k)}(a)}{k!}
(x-a)^k.
```

Nó là unique polynomial degree ≤ `n` có cùng derivatives tới thứ tự (order / 순서) `n` với `f` tại `a`.

Đây là characterization quan trọng hơn việc chỉ nhớ formula.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **4. Taylor series khác Taylor polynomial** tiếp nhận điểm tựa từ **3. General Taylor polynomial** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Smooth nhưng không analytic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Taylor series khác Taylor polynomial

Taylor polynomial luôn finite:

```math
P_n(x).
```

Taylor series là infinite formal expansion:

```math
\sum_{k=0}^{\infty}
\frac{f^{(k)}(a)}{k!}(x-a)^k.
```

Để viết

```math
f(x)=\text{Taylor series}
```

cần chứng minh remainder → 0 trong region đang xét.

Smoothness `C^\infty` alone chưa đủ.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **5. Smooth nhưng không analytic** tiếp nhận điểm tựa từ **4. Taylor series khác Taylor polynomial** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Lagrange remainder cho lỗi (error / 오류) estimate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Smooth nhưng không analytic

Một classic example:

```math
f(x)=
\begin{cases}
e^{-1/x^2},&x\ne0\\
0,&x=0.
\end{cases}
```

Hàm (function / 함수) này infinitely differentiable tại 0 và mọi derivatives tại 0 đều bằng 0.

Taylor series quanh 0 vì vậy là zero series:

```math
0+0x+0x^2+\cdots
```

nhưng hàm (function / 함수) không zero khi `x\ne0`.

Do đó:

```text
infinitely differentiable ≠ analytic
```

Analytic nghĩa hàm (function / 함수) locally equals its convergent power series.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **6. Lagrange remainder cho lỗi (error / 오류) estimate** tiếp nhận điểm tựa từ **5. Smooth nhưng không analytic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. e^x là ideal Taylor hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Lagrange remainder cho lỗi (error / 오류) estimate

Dưới suitable conditions:

```math
R_n(x)
=
f(x)-P_n(x)
=
\frac{f^{(n+1)}(\xi)}{(n+1)!}
(x-a)^{n+1}
```

cho một `\xi` giữa `a` và `x`.

Nếu

```math
|f^{(n+1)}(t)|\le M
```

trên interval, thì

```math
|R_n(x)|
\le
\frac{M}{(n+1)!}|x-a|^{n+1}.
```

Đây là cầu nối (bridge / 브리지) từ symbolic approximation sang certified lỗi (error / 오류).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **7. e^x là ideal Taylor hàm (function / 함수)** tiếp nhận điểm tựa từ **6. Lagrange remainder cho lỗi (error / 오류) estimate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. sin và cos: derivative cycle tạo coefficient mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. e^x là ideal Taylor hàm (function / 함수)

Vì mọi derivatives của `e^x` đều là `e^x`, tại 0:

```math
f^{(k)}(0)=1.
```

Do đó:

```math
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.
```

Factorial denominator làm terms shrink rất nhanh cho fixed `x`, nên radius of convergence là infinite.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **8. sin và cos: derivative cycle tạo coefficient mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **7. e^x là ideal Taylor hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. ln(1+x) và finite radius** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. sin và cos: derivative cycle tạo coefficient mẫu (pattern / 패턴)

Derivatives cycle:

```text
sin → cos → -sin → -cos → sin
```

Tại 0 cho:

```math
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
```

```math
\cos x
=
1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots.
```

Small-angle approximations:

```math
\sin x\approx x
```

```math
\cos x\approx1-\frac{x^2}{2}.
```

Angles phải tính bằng radians để derivatives có form chuẩn này.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **9. ln(1+x) và finite radius** tiếp nhận điểm tựa từ **8. sin và cos: derivative cycle tạo coefficient mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. cục bộ (local / 로컬) approximation chất lượng (quality / 품질) phụ thuộc distance tới center** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. ln(1+x) và finite radius

Around 0:

```math
\ln(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
```

valid trong convergence region phù hợp.

Singularity tại `x=-1` giới hạn radius quanh 0.

Deep liên kết (connection / 연결):

> Radius of convergence thường bị giới hạn bởi nearest singularity trong complex plane.

Ngay cả khi đang học real calculus, complex phân tích (analysis / 분석) giải thích sâu hơn tại sao power series dừng ở đâu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **10. cục bộ (local / 로컬) approximation chất lượng (quality / 품질) phụ thuộc distance tới center** tiếp nhận điểm tựa từ **9. ln(1+x) và finite radius** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Taylor theorem giải thích derivative meaning sâu hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. cục bộ (local / 로컬) approximation chất lượng (quality / 품질) phụ thuộc distance tới center

Taylor polynomial quanh `a` thường tốt nhất gần `a`.

Term lỗi (error / 오류) chứa factor:

```math
|x-a|^{n+1}.
```

Đi xa center làm lỗi (error / 오류) grow nhanh nếu không tăng degree hoặc đổi center.

Numerical libraries thường dùng **phạm vi (range / 범위) reduction**:

```text
reduce input to small region
→ approximate accurately there
→ transform result back
```

thay vì dùng một Taylor polynomial quanh 0 cho mọi đầu vào (input / 입력).

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **11. Taylor theorem giải thích derivative meaning sâu hơn** tiếp nhận điểm tựa từ **10. cục bộ (local / 로컬) approximation chất lượng (quality / 품질) phụ thuộc distance tới center** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Why linearization works so often** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Taylor theorem giải thích derivative meaning sâu hơn

First-order:

```math
f(a+h)=f(a)+f'(a)h+O(h^2)
```

under enough smoothness.

Second-order:

```math
f(a+h)
=
f(a)+f'(a)h
+\frac12f''(a)h^2
+O(h^3).
```

Notation `O(h^k)` nói lỗi (error / 오류) quy mô (scale / 규모) no faster than constant times `|h|^k` near zero.

Taylor vì vậy là formal ngôn ngữ (language / 언어) của “cục bộ (local / 로컬) hành vi (behavior / 동작) by orders of smallness”.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **12. Why linearization works so often** tiếp nhận điểm tựa từ **11. Taylor theorem giải thích derivative meaning sâu hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Multivariable Taylor expansion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Why linearization works so often

Nếu `h` small:

```text
h       >> h² >> h³ >> ...
```

về magnitude.

Do đó first nonzero low-order terms dominate.

Đây là lý do:

- small perturbations thường gần tuyến tính (linear / 선형);
- lan truyền lỗi (error propagation / 오류 전파) dùng derivatives;
- cục bộ (local / 로컬) stability dùng Jacobian;
- small-angle physics dùng low-order expansions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **13. Multivariable Taylor expansion** tiếp nhận điểm tựa từ **12. Why linearization works so often** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. tối ưu hóa (optimization / 최적화): stationary điểm (point / 지점) + Hessian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Multivariable Taylor expansion

Cho scalar hàm (function / 함수) `f:\mathbb R^n\to\mathbb R`:

```math
f(x+\Delta)
\approx
f(x)
+
\nabla f(x)^T\Delta
+
\frac12\Delta^TH(x)\Delta.
```

Độ dốc (gradient / 기울기) là first-order sensitivity véc-tơ (vector / 벡터).

Hessian là second-order curvature ma trận (matrix / 행렬).

Quadratic form

```math
\Delta^TH\Delta
```

cho curvature theo direction `\Delta`.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **14. tối ưu hóa (optimization / 최적화): stationary điểm (point / 지점) + Hessian** tiếp nhận điểm tựa từ **13. Multivariable Taylor expansion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Newton's phương thức (method / 메서드) đến từ quadratic/cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. tối ưu hóa (optimization / 최적화): stationary điểm (point / 지점) + Hessian

Tại trọng yếu (critical / 중요) điểm (point / 지점):

```math
\nabla f(x_*)=0.
```

Taylor cục bộ (local / 로컬) mô hình (model / 모델):

```math
f(x_*+\Delta)
\approx
f(x_*)+
\frac12\Delta^TH\Delta.
```

Nếu Hessian positive definite → cục bộ (local / 로컬) bowl → strict cục bộ (local / 로컬) minimum.

Nếu negative definite → cục bộ (local / 로컬) maximum.

Nếu indefinite → saddle.

Second derivative kiểm thử (test / 테스트) là consequence của quadratic Taylor hình học (geometry / 기하학).

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **15. Newton's phương thức (method / 메서드) đến từ quadratic/cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** tiếp nhận điểm tựa từ **14. tối ưu hóa (optimization / 최적화): stationary điểm (point / 지점) + Hessian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. lan truyền lỗi (error propagation / 오류 전파) là first-order Taylor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Newton's phương thức (method / 메서드) đến từ quadratic/cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)

Để solve scalar equation

```math
f(x)=0,
```

first-order Taylor quanh `x_n`:

```math
0
\approx
f(x_n)+f'(x_n)(x_{n+1}-x_n).
```

Solve:

```math
x_{n+1}
=
x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Newton phương thức (method / 메서드) không phải formula ngẫu nhiên; nó tìm zero của cục bộ (local / 로컬) tangent approximation.

Trong tối ưu hóa (optimization / 최적화), Newton step từ quadratic mô hình (model / 모델):

```math
\Delta=-H^{-1}\nabla f.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **16. lan truyền lỗi (error propagation / 오류 전파) là first-order Taylor** tiếp nhận điểm tựa từ **15. Newton's phương thức (method / 메서드) đến từ quadratic/cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Physics: small oscillation approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. lan truyền lỗi (error propagation / 오류 전파) là first-order Taylor

Nếu

```math
y=f(x)
```

và sai số đo lường (measurement error / 측정 오차) `\Delta x` small:

```math
\Delta y
\approx
f'(x)\Delta x.
```

Multivariable:

```math
\Delta y
\approx
\nabla f^T\Delta x.
```

Nếu đầu vào (input / 입력) bất định (uncertainty / 불확실성) covariance `\Sigma_x`, linearized đầu ra (output / 출력) variance:

```math
\operatorname{Var}(y)
\approx
\nabla f^T\Sigma_x\nabla f.
```

Taylor approximation là foundation của bất định (uncertainty / 불확실성) propagation.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **17. Physics: small oscillation approximation** tiếp nhận điểm tựa từ **16. lan truyền lỗi (error propagation / 오류 전파) là first-order Taylor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Relativity/kỹ thuật (engineering / 엔지니어링) style perturbation intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Physics: small oscillation approximation

Pendulum equation:

```math
\theta''+
\frac gL\sin\theta=0.
```

For small angle:

```math
\sin\theta\approx\theta.
```

Hệ thống (system / 시스템) becomes tuyến tính (linear / 선형):

```math
\theta''+
\frac gL\theta=0.
```

Nonlinear pendulum locally behaves like harmonic oscillator.

Giả định (assumption / 가정) is not “pendulum equation simplified magically”; it is a Taylor truncation valid for small `|\theta|`.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **18. Relativity/kỹ thuật (engineering / 엔지니어링) style perturbation intuition** tiếp nhận điểm tựa từ **17. Physics: small oscillation approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. AI: cục bộ (local / 로컬) mất mát (loss / 손실) hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Relativity/kỹ thuật (engineering / 엔지니어링) style perturbation intuition

Expressions như

```math
(1+x)^\alpha
```

for small `x`:

```math
(1+x)^\alpha
\approx
1+\alpha x
+
\frac{\alpha(\alpha-1)}2x^2+\cdots.
```

This converts nonlinear multiplicative expressions into manageable polynomial corrections.

Perturbation methods across physics/kỹ thuật (engineering / 엔지니어링) bản dựng (build / 빌드) on this lô-gic (logic / 논리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **19. AI: cục bộ (local / 로컬) mất mát (loss / 손실) hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **18. Relativity/kỹ thuật (engineering / 엔지니어링) style perturbation intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Finance: delta-gamma approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. AI: cục bộ (local / 로컬) mất mát (loss / 손실) hình học (geometry / 기하학)

Near parameter `\theta`:

```math
L(\theta+\Delta)
\approx
L(\theta)
+
\nabla L^T\Delta
+
\frac12\Delta^TH\Delta.
```

Độ dốc (gradient / 기울기) descent uses first-order cục bộ (local / 로컬) thông tin (information / 정보).

Newton/quasi-Newton/preconditioning use curvature thông tin (information / 정보) more directly.

Sharp/flat directions correspond roughly to large/small Hessian eigenvalues locally.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **20. Finance: delta-gamma approximation** tiếp nhận điểm tựa từ **19. AI: cục bộ (local / 로컬) mất mát (loss / 손실) hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Taylor vs polynomial interpolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Finance: delta-gamma approximation

For nonlinear portfolio giá trị (value / 값) `V(S)`:

```math
\Delta V
\approx
V'(S)\Delta S
+
\frac12V''(S)(\Delta S)^2.
```

Finance terminology:

```text
Delta  → first derivative sensitivity
Gamma  → second derivative curvature
```

Again, this is just second-order Taylor approximation.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **21. Taylor vs polynomial interpolation** tiếp nhận điểm tựa từ **20. Finance: delta-gamma approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Taylor vs Fourier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Taylor vs polynomial interpolation

Taylor polynomial chooses coefficients from derivatives at one điểm (point / 지점).

Interpolation polynomial chooses coefficients to match values at several points.

Both produce polynomials but encode different thông tin (information / 정보).

Taylor is cục bộ (local / 로컬) derivative matching; interpolation is multi-point giá trị (value / 값) matching.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **22. Taylor vs Fourier** tiếp nhận điểm tựa từ **21. Taylor vs polynomial interpolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Asymptotic expansion may be useful even if series diverges** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Taylor vs Fourier

Taylor basis:

```text
1, (x-a), (x-a)², ...
```

is cục bộ (local / 로컬) polynomial cấu trúc (structure / 구조).

Fourier basis:

```text
sin(kx), cos(kx)
```

captures toàn cục (global / 전역) frequency cấu trúc (structure / 구조).

A periodic hàm (function / 함수) may be represented much more naturally by Fourier series than Taylor series.

Biểu diễn (representation / 표현) should match cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **23. Asymptotic expansion may be useful even if series diverges** tiếp nhận điểm tựa từ **22. Taylor vs Fourier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Numerical danger: more terms can make kết quả (result / 결과) worse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Asymptotic expansion may be useful even if series diverges

Not every useful expansion is convergent.

An asymptotic series may satisfy:

```text
first few terms improve approximation as parameter → limit
```

while infinite series itself diverges.

This matters in advanced physics/numerical phân tích (analysis / 분석): usefulness of truncation does not always require convergence of infinite expansion.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **24. Numerical danger: more terms can make kết quả (result / 결과) worse** tiếp nhận điểm tựa từ **23. Asymptotic expansion may be useful even if series diverges** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. phạm vi (range / 범위) reduction example for e^x** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Numerical danger: more terms can make kết quả (result / 결과) worse

In chính xác (exact / 정확한) arithmetic, adding Taylor terms within convergence region tends toward hàm (function / 함수).

In floating điểm (point / 지점):

- large intermediate terms may cancel;
- factorial/powers may overflow/underflow;
- rounding accumulates;
- evaluation thứ tự (order / 순서) matters.

Horner form often evaluates polynomial more stably/efficiently:

```math
c_0+x(c_1+x(c_2+\cdots)).
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **24. Numerical danger: more terms can make kết quả (result / 결과) worse** cho ta quy tắc; **25. phạm vi (range / 범위) reduction example for e^x** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. Worked example: approximate e^0.1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. phạm vi (range / 범위) reduction example for e^x

Instead of approximate huge `x` directly, ghi (write / 쓰기):

```math
x=k\ln2+r
```

with small `r`.

Then:

```math
e^x=2^ke^r.
```

Approximate `e^r` where `r` small.

This illustrates kỹ thuật (engineering / 엔지니어링) principle:

```text
mathematical identity
+ local approximation
+ numerical representation
```

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **25. phạm vi (range / 범위) reduction example for e^x** cho ta quy tắc; **26. Worked example: approximate e^0.1** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. Worked example: when sin x ≈ x fails** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Worked example: approximate e^0.1

Third-order Maclaurin:

```math
P_3(x)
=1+x+\frac{x^2}{2}+\frac{x^3}{6}.
```

At `x=0.1`:

```math
P_3(0.1)
=1+0.1+0.005+0.0001667
\approx1.1051667.
```

True giá trị (value / 값) roughly `1.105170...`, so lỗi (error / 오류) is only a few millionths.

Reason approximation works well: `x` is small and factorial denominator suppresses higher terms.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **26. Worked example: approximate e^0.1** cho ta quy tắc; **27. Worked example: when sin x ≈ x fails** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **28. Proof idea behind Taylor theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Worked example: when sin x ≈ x fails

At `x=0.1 rad`:

```math
\sin(0.1)\approx0.09983
```

close to `0.1`.

At `x=2 rad`:

```math
\sin2\approx0.909
```

far from `2`.

Approximation is cục bộ (local / 로컬). Same formula used outside its validity region becomes a modeling lỗi (error / 오류).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **27. Worked example: when sin x ≈ x fails** cho ta quy tắc; **28. Proof idea behind Taylor theorem** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **29. Analyticity and complex singularities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Proof idea behind Taylor theorem

Full proof may use repeated Mean giá trị (value / 값) Theorem or integral remainder.

Cốt lõi (core / 핵심) idea:

1. bản dựng (build / 빌드) polynomial matching derivatives at `a`;
2. subtract it from `f`;
3. resulting lỗi (error / 오류) hàm (function / 함수) has many derivatives vanishing at `a`;
4. Mean Value-type arguments force lỗi (error / 오류) to contain high power `(x-a)^{n+1}`.

Factorial and higher derivative emerge naturally from repeated differentiation.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **29. Analyticity and complex singularities** tiếp nhận điểm tựa từ **28. Proof idea behind Taylor theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Analyticity and complex singularities

For many familiar analytic functions, Taylor radius around `a` equals distance to nearest singularity in complex plane.

Example:

```math
f(x)=\frac1{1+x^2}.
```

As real hàm (function / 함수) smooth everywhere, but complex singularities at

```math
z=\pm i.
```

Distance from 0 is 1, so Maclaurin radius is 1.

Complex phân tích (analysis / 분석) explains convergence limits that real đồ thị (graph / 그래프) alone does not reveal.

> **Chuyển mạch:** Ở chặng này của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, sau nội dung của **29. Analyticity and complex singularities**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Taylor series nối đạo hàm cục bộ với mô hình xấp xỉ và sai số toàn cục. Nó cho biết khi nào một biểu diễn đơn giản đủ tốt và khi nào remainder trở thành rủi ro.

```text
derivatives
→ local polynomial model
→ Taylor theorem
→ error/remainder
→ numerical approximation
→ Newton methods
→ Hessian optimization
→ uncertainty propagation
→ perturbation physics
→ delta-gamma finance
→ analytic functions / complex singularities
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Taylor expansion is a **cục bộ (local / 로컬) thông tin (information / 정보) compressor**. Derivatives at one điểm (point / 지점) become polynomial coefficients. First thứ tự (order / 순서) records slope, second thứ tự (order / 순서) curvature, higher orders finer shape. The approximation is useful only together with its **center, thứ tự (order / 순서) and lỗi (error / 오류) regime**.

> **Chuyển mạch:** Trong **Taylor series và cục bộ (local / 로컬) approximation: derivatives như cục bộ (local / 로컬) polynomial thông tin (information / 정보)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

`C^\infty` does not imply analytic. More Taylor terms are not automatically numerically better. A Taylor approximation valid near one center need not work far away. `sin x\approx x` assumes radians and small `x`. Taylor polynomial and Taylor series are different objects. A convergent Taylor series must still be shown to converge to the original function, not merely converge to something.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
