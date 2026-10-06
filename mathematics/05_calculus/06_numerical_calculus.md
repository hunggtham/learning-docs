# Numerical calculus: finite differences, quadrature và automatic differentiation

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Numerical calculus: finite differences, quadrature và automatic differentiation**. Route đi từ finite precision/samples → numerical derivatives and Taylor errors → quadrature → automatic differentiation → conditioning, stability và error budgets.

Calculus định nghĩa derivative/integral bằng limits ideal. Máy tính không thực hiện một tiến trình (process / 프로세스) vô hạn; nó làm việc với finite precision, finite samples và finite thời gian (time / 시간). Numerical calculus nghiên cứu cách thay những ideal operations đó bằng approximations có lỗi (error / 오류) được hiểu và kiểm soát.

Chapter này tập trung riêng vào ba vấn đề:

```text
numerical differentiation
numerical integration
automatic differentiation
```

Các topics rộng hơn như conditioning, floating-point stability, gốc (root / 루트) finding và numerical tuyến tính (linear / 선형) algebra được xử lý sâu ở chapter `08_optimization_numerical/02_numerical_methods_and_error.md`.

## 1. Numerical derivative là inverse bài toán (problem / 문제) nhạy cảm

Derivative hỏi cục bộ (local / 로컬) tỷ lệ (rate / 비율). Với sampled/noisy dữ liệu (data / 데이터), ta phải estimate slope từ nearby values.

Forward difference:

```math
f'(x)
\approx
\frac{f(x+h)-f(x)}{h}.
```

Nếu `h` large, approximation không cục bộ (local / 로컬) enough. Nếu `h` too small, subtraction giữa nearly equal floating-point numbers có thể mất significant digits.

Do đó numerical differentiation có một paradox:

> smaller step reduces truncation lỗi (error / 오류) only until rounding/noise amplification starts to dominate.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **2. Derive forward difference từ Taylor expansion** nối từ **1. Numerical derivative là inverse bài toán (problem / 문제) nhạy cảm** sang **3. Backward difference**, vì cơ chế trước tạo đầu vào cho bước sau.

## 2. Derive forward difference từ Taylor expansion

Taylor:

```math
f(x+h)
=
f(x)+hf'(x)+\frac{h^2}{2}f''(x)+O(h^3).
```

Rearrange:

```math
\frac{f(x+h)-f(x)}{h}
=
f'(x)+\frac h2f''(x)+O(h^2).
```

Nên

```math
f'(x)
=
\frac{f(x+h)-f(x)}{h}+O(h).
```

Forward difference có first-order truncation lỗi (error / 오류).

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **3. Backward difference** nối từ **2. Derive forward difference từ Taylor expansion** sang **4. Central difference: symmetry cancels lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Backward difference

Tương tự:

```math
f'(x)
\approx
\frac{f(x)-f(x-h)}{h}.
```

Nó cũng first-order.

Forward/backward formulas hữu ích gần boundaries khi samples chỉ available một phía.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **4. Central difference: symmetry cancels lỗi (error / 오류)** nối từ **3. Backward difference** sang **5. Second derivative formula**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Central difference: symmetry cancels lỗi (error / 오류)

Taylor:

```math
f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\frac{h^3}{6}f'''(x)+\cdots
```

```math
f(x-h)=f(x)-hf'(x)+\frac{h^2}{2}f''(x)-\frac{h^3}{6}f'''(x)+\cdots
```

Subtract:

```math
f(x+h)-f(x-h)
=2hf'(x)+\frac{h^3}{3}f'''(x)+\cdots
```

Do đó

```math
f'(x)
\approx
\frac{f(x+h)-f(x-h)}{2h}
```

với lỗi (error / 오류)

```math
O(h^2).
```

Symmetry làm even-order terms cancel.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **5. Second derivative formula** nối từ **4. Central difference: symmetry cancels lỗi (error / 오류)** sang **6. Step-size sự đánh đổi (trade-off / 트레이드오프)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Second derivative formula

Cộng Taylor expansions:

```math
f(x+h)-2f(x)+f(x-h)
=h^2f''(x)+O(h^4).
```

Nên

```math
f''(x)
\approx
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}
```

với truncation lỗi (error / 오류) `O(h^2)`.

Formula này là building khối (block / 블록) của finite-difference PDE solvers.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **6. Step-size sự đánh đổi (trade-off / 트레이드오프)** nối từ **5. Second derivative formula** sang **7. Noise amplification trong measured dữ liệu (data / 데이터)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Step-size sự đánh đổi (trade-off / 트레이드오프)

Một simplified lỗi (error / 오류) mô hình (model / 모델) cho forward difference:

```math
E(h)
\approx
C_1h+
C_2\frac{\varepsilon_{mach}}{h}.
```

Term đầu là truncation; term sau là rounding/cancellation amplification.

Minimize rough mô hình (model / 모델) cho optimal `h` quy mô (scale / 규모) around

```math
h\sim\sqrt{\varepsilon_{mach}}
```

times bài toán (problem / 문제) quy mô (scale / 규모), under simplified các giả định (assumptions / 가정들).

Central difference có different balance because truncation is `O(h^2)`.

Điểm chính: “use smallest possible h” là wrong quy tắc (rule / 규칙).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **6. Step-size sự đánh đổi (trade-off / 트레이드오프)** đặt vấn đề; **7. Noise amplification trong measured dữ liệu (data / 데이터)** đối chiếu bằng chứng, rồi **8. Higher-order finite differences** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Noise amplification trong measured dữ liệu (data / 데이터)

Nếu observed values:

```math
\tilde f(x)=f(x)+\epsilon(x),
```

finite difference divides noise difference by `h`:

```math
\frac{\epsilon(x+h)-\epsilon(x)}{h}.
```

As `h→0`, noise term can explode.

Derivative estimation từ experimental dữ liệu (data / 데이터) thường cần smoothing, regularization, cục bộ (local / 로컬) polynomial fit hoặc lĩnh vực (domain / 도메인) các mô hình (models / 모델들), không chỉ smaller spacing.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **7. Noise amplification trong measured dữ liệu (data / 데이터)** đặt vấn đề; **8. Higher-order finite differences** đối chiếu bằng chứng, rồi **9. Richardson extrapolation** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. Higher-order finite differences

Ta có thể combine more mẫu (sample / 표본) points để cancel more Taylor terms.

Higher thứ tự (order / 순서) formulas giảm truncation lỗi (error / 오류) với smooth functions, nhưng:

- need wider stencil;
- boundaries khó hơn;
- noise sensitivity có thể tăng;
- floating-point coefficients có trade-offs.

Thứ tự (order / 순서) cao không automatic nghĩa practical accuracy cao hơn.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **9. Richardson extrapolation** nối từ **8. Higher-order finite differences** sang **10. Numerical tích hợp (integration / 통합) khác numerical differentiation về stability**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Richardson extrapolation

Nếu approximation có expansion

```math
D(h)=D+C h^p+O(h^{p+1}),
```

và compute `D(h)` cùng `D(h/2)`, ta combine để cancel leading lỗi (error / 오류) term.

Ý tưởng này tạo Richardson extrapolation và là principle phía sau Romberg tích hợp (integration / 통합).

Nó dùng kiến thức (knowledge / 지식) về lỗi (error / 오류) cấu trúc (structure / 구조) để improve estimate thay vì chỉ shrink step blindly.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **10. Numerical tích hợp (integration / 통합) khác numerical differentiation về stability** nối từ **9. Richardson extrapolation** sang **11. Trapezoidal quy tắc (rule / 규칙) từ tuyến tính (linear / 선형) interpolation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Numerical tích hợp (integration / 통합) khác numerical differentiation về stability

Tích hợp (integration / 통합) averages/accumulates values, nên thường smoothing hơn differentiation.

Ta approximate

```math
\int_a^b f(x)\,dx
```

bằng weighted sum of samples:

```math
\sum_i w_i f(x_i).
```

Choice nodes/weights quyết định quadrature quy tắc (rule / 규칙).

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **11. Trapezoidal quy tắc (rule / 규칙) từ tuyến tính (linear / 선형) interpolation** nối từ **10. Numerical tích hợp (integration / 통합) khác numerical differentiation về stability** sang **12. Simpson's quy tắc (rule / 규칙) từ quadratic interpolation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Trapezoidal quy tắc (rule / 규칙) từ tuyến tính (linear / 선형) interpolation

Trên one interval `[a,b]`, approximate `f` bằng line nối endpoints.

Area trapezoid:

```math
\int_a^b f(x)dx
\approx
\frac{b-a}{2}[f(a)+f(b)].
```

Composite trapezoidal quy tắc (rule / 규칙) chia interval thành many subintervals.

Với smooth hàm (function / 함수) và uniform step `h`, toàn cục (global / 전역) lỗi (error / 오류) thường `O(h^2)`.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **12. Simpson's quy tắc (rule / 규칙) từ quadratic interpolation** nối từ **11. Trapezoidal quy tắc (rule / 규칙) từ tuyến tính (linear / 선형) interpolation** sang **13. Gaussian quadrature: choose nodes intelligently**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Simpson's quy tắc (rule / 규칙) từ quadratic interpolation

Trên interval với midpoint `m=(a+b)/2`, fit quadratic qua `a,m,b` rồi integrate chính xác (exact / 정확한) polynomial đó:

```math
\int_a^b f(x)dx
\approx
\frac{b-a}{6}
\left[
f(a)+4f(m)+f(b)
\right].
```

Composite Simpson thường có high accuracy for smooth functions, with toàn cục (global / 전역) lỗi (error / 오류) `O(h^4)` under tiêu chuẩn (standard / 표준) conditions.

Weights `1,4,1` không arbitrary; chúng đến từ integrating quadratic interpolation basis.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **13. Gaussian quadrature: choose nodes intelligently** nối từ **12. Simpson's quy tắc (rule / 규칙) từ quadratic interpolation** sang **14. Adaptive quadrature**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Gaussian quadrature: choose nodes intelligently

Newton–Cotes rules như trapezoidal/Simpson use equally spaced nodes.

Gaussian quadrature chooses nodes/weights để integrate polynomials tới high degree exactly với fixed number samples.

Nó cho thấy numerical tích hợp (integration / 통합) không chỉ là “mẫu (sample / 표본) dày hơn”; placement của samples có mathematical cấu trúc (structure / 구조).

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **14. Adaptive quadrature** nối từ **13. Gaussian quadrature: choose nodes intelligently** sang **15. Improper integrals cần transformation/truncation chiến lược (strategy / 전략)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Adaptive quadrature

Hàm (function / 함수) có thể smooth ở most interval nhưng thay đổi nhanh ở small region.

Uniform fine grid wastes công việc (work / 작업).

Adaptive methods estimate cục bộ (local / 로컬) lỗi (error / 오류) và subdivide nơi cần thiết:

```text
coarse estimate
vs
refined estimate
→ if mismatch large, split interval further
```

Đây là general numerical principle: allocate computation where lỗi (error / 오류) indicators say it matters.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **15. Improper integrals cần transformation/truncation chiến lược (strategy / 전략)** nối từ **14. Adaptive quadrature** sang **16. Highly oscillatory integrals**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Improper integrals cần transformation/truncation chiến lược (strategy / 전략)

For

```math
\int_0^\infty f(x)dx,
```

computer cannot integrate to literal infinity.

Strategies:

- truncate lĩnh vực (domain / 도메인) with tail lỗi (error / 오류) bound;
- thay đổi (change / 변경) variables map infinite interval to finite;
- use specialized quadrature.

Mathematical convergence không automatically cho numerical chiến lược (strategy / 전략) tốt.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **16. Highly oscillatory integrals** nối từ **15. Improper integrals cần transformation/truncation chiến lược (strategy / 전략)** sang **17. Monte Carlo tích hợp (integration / 통합)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Highly oscillatory integrals

Nếu integrand oscillates rapidly, naive uniform sampling có thể alias/cancel incorrectly.

Methods may need:

- sufficiently high resolution;
- analytic phase thông tin (information / 정보);
- Filon-type/specialized quadrature;
- transform methods.

Liên kết (connection / 연결) với sampling lý thuyết (theory / 이론)/Fourier rất trực tiếp.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **17. Monte Carlo tích hợp (integration / 통합)** nối từ **16. Highly oscillatory integrals** sang **18. Quasi-Monte Carlo**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Monte Carlo tích hợp (integration / 통합)

For high-dimensional integral,

```math
I=E[f(X)]
```

under suitable phân phối (distribution / 분포) biểu diễn (representation / 표현).

Estimate:

```math
\hat I
=\frac1N\sum_{i=1}^N f(X_i).
```

Tiêu chuẩn (standard / 표준) lỗi (error / 오류) typically scales

```math
O(N^{-1/2}),
```

slow compared with deterministic low-dimensional quadrature nhưng less sensitive to dimension in exponent.

Đây là lý do Monte Carlo mạnh trong finance, Bayesian computation và high-dimensional physics.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **18. Quasi-Monte Carlo** nối từ **17. Monte Carlo tích hợp (integration / 통합)** sang **19. Automatic differentiation khác finite differences hoàn toàn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Quasi-Monte Carlo

Thay pseudorandom samples bằng low-discrepancy sequences để fill không gian (space / 공간) more evenly.

Can improve convergence for sufficiently regular integrands, though guarantees/hành vi (behavior / 동작) depend dimension and variation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **19. Automatic differentiation khác finite differences hoàn toàn** nối từ **18. Quasi-Monte Carlo** sang **20. Forward-mode AD**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Automatic differentiation khác finite differences hoàn toàn

Automatic differentiation (AD / 자동미분) không approximate derivative bằng `h`.

Nó decompose computation thành thành phần nguyên thủy (primitive / 기본 요소) operations và apply chuỗi (chain / 사슬) quy tắc (rule / 규칙) exactly theo machine arithmetic.

Ví dụ:

```text
x → multiply → sin → add → loss
```

AD propagates derivative thông tin (information / 정보) through this computational đồ thị (graph / 그래프).

No truncation lỗi (error / 오류) from finite step exists, though floating-point rounding still exists.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **20. Forward-mode AD** nối từ **19. Automatic differentiation khác finite differences hoàn toàn** sang **21. Reverse-mode AD**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Forward-mode AD

Forward chế độ (mode / 모드) propagates pairs like

```text
(value, derivative wrt chosen input direction)
```

through computation.

Efficient khi number of đầu vào (input / 입력) directions nhỏ relative to outputs.

Mathematically it computes Jacobian-vector products (JVPs).

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **21. Reverse-mode AD** nối từ **20. Forward-mode AD** sang **22. Computational đồ thị (graph / 그래프) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Reverse-mode AD

Reverse chế độ (mode / 모드) runs forward to bản ghi (record / 레코드) intermediate values, then propagates adjoints backward.

Efficient khi đầu ra (output / 출력) scalar and inputs many — exactly neural-network mất mát (loss / 손실) setting.

It computes vector-Jacobian products (VJPs).

Backpropagation is reverse-mode AD specialized to layered/computational-graph các mô hình (models / 모델들).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **21. Reverse-mode AD** đặt đầu vào cho **22. Computational đồ thị (graph / 그래프) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)**, rồi **23. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프) của reverse chế độ (mode / 모드)** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. Computational đồ thị (graph / 그래프) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)

If

```math
z=f(y),\qquad y=g(x),
```

then

```math
\frac{dz}{dx}
=
\frac{dz}{dy}
\frac{dy}{dx}.
```

For many intermediate variables, reverse chế độ (mode / 모드) accumulates all downstream sensitivity contributions.

This is động (dynamic / 동적) programming on the đồ thị (graph / 그래프) of cục bộ (local / 로컬) derivatives.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **22. Computational đồ thị (graph / 그래프) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)** đặt đầu vào cho **23. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프) của reverse chế độ (mode / 모드)**, rồi **24. Nondifferentiability và subgradients** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프) của reverse chế độ (mode / 모드)

Reverse chế độ (mode / 모드) often needs intermediate activations from forward pass.

Large các mô hình (models / 모델들) therefore face bộ nhớ (memory / 메모리) chi phí (cost / 비용).

Checkpointing trades recomputation for bộ nhớ (memory / 메모리): save only selected states, recompute others during backward.

This links AD to time-memory trade-offs in CS.

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **24. Nondifferentiability và subgradients** nối từ **23. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프) của reverse chế độ (mode / 모드)** sang **25. độ dốc (gradient / 기울기) checking**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Nondifferentiability và subgradients

Thành phần nguyên thủy (primitive / 기본 요소) like ReLU:

```math
\max(0,x)
```

nondifferentiable at `x=0`.

Frameworks choose a convention/subgradient at such points.

AD differentiates **implemented computation**, not an abstract smooth ideal. Branches, clipping, discrete operations and stop-gradient ngữ nghĩa (semantics / 의미론) matter.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **25. độ dốc (gradient / 기울기) checking** nối từ **24. Nondifferentiability và subgradients** sang **26. Complex-step differentiation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 25. độ dốc (gradient / 기울기) checking

To gỡ lỗi (debug / 디버그) AD hiện thực (implementation / 구현), compare with central finite difference:

```math
g_i^{FD}
=
\frac{f(x+he_i)-f(x-he_i)}{2h}.
```

Use relative lỗi (error / 오류), not bitwise equality:

```math
\frac{\|g^{AD}-g^{FD}\|}
{\|g^{AD}\|+\|g^{FD}\|+\epsilon}.
```

If `h` too small/large, finite-difference tham chiếu (reference / 참조) itself is bad.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **26. Complex-step differentiation** nối từ **25. độ dốc (gradient / 기울기) checking** sang **27. Physics and kỹ thuật (engineering / 엔지니어링)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 26. Complex-step differentiation

For analytic real-valued computation that can accept complex perturbation without non-analytic operations, one can use

```math
f'(x)
\approx
\frac{\operatorname{Im}f(x+ih)}{h}.
```

This avoids subtractive cancellation and can achieve very high accuracy.

But it requires hiện thực (implementation / 구현) compatible with complex arithmetic and analyticity các giả định (assumptions / 가정들).

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **27. Physics and kỹ thuật (engineering / 엔지니어링)** nối từ **26. Complex-step differentiation** sang **28. Finance**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. Physics and kỹ thuật (engineering / 엔지니어링)

Finite differences approximate spatial/thời gian (time / 시간) derivatives in PDE discretization.

Quadrature computes công việc (work / 작업), năng lượng (energy / 에너지), mass and flux from sampled fields.

AD increasingly appears in differentiable simulation and inverse problems.

Each phương thức (method / 메서드) addresses a different computational biểu diễn (representation / 표현) of calculus.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **28. Finance** nối từ **27. Physics and kỹ thuật (engineering / 엔지니어링)** sang **29. AI**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. Finance

Numerical derivatives of option prices produce Greeks when analytic formulas unavailable, but bump kích thước (size / 크기)/noise matter.

Monte Carlo integrates expected discounted payoff:

```math
V=e^{-rT}E[\text{payoff}].
```

Pathwise derivatives, likelihood-ratio methods and AD can estimate sensitivities more efficiently than naive finite differences.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **29. AI** nối từ **28. Finance** sang **30. Chapter ranh giới (boundary / 경계): what belongs elsewhere?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. AI

Huấn luyện (training / 학습) neural networks relies on reverse-mode AD.

Độ dốc (gradient / 기울기) checking uses finite differences only as debugging tham chiếu (reference / 참조) on small các mô hình (models / 모델들).

Numerical tích hợp (integration / 통합) appears in continuous-time các mô hình (models / 모델들), diffusion/ODE các hệ thống (systems / 시스템들) and probabilistic suy luận (inference / 추론).

> **Nối mạch:** Ở chặng này của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **29. AI** đặt tiêu chí; **30. Chapter ranh giới (boundary / 경계): what belongs elsewhere?** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## 30. Chapter ranh giới (boundary / 경계): what belongs elsewhere?

This chapter does **not** repeat all numerical-analysis topics.

For:

- floating-point conditioning/stability;
- gốc (root / 루트) finding;
- interpolation broadly;
- numerical tuyến tính (linear / 선형) algebra;
- ODE solver stability;

see `08_optimization_numerical/02_numerical_methods_and_error.md` and related chapters.

The goal here is to keep numerical calculus conceptually focused rather than duplicate a second numerical-analysis survey.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Numerical calculus: finite differences, quadrature và automatic differentiation**, **30. Chapter ranh giới (boundary / 경계): what belongs elsewhere?** đặt tiêu chí; **Mô hình tư duy (mental model / 사고 모델)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## Mô hình tư duy (mental model / 사고 모델)

> Numerical differentiation probes cục bộ (local / 로컬) thay đổi (change / 변경) and is inherently sensitive to noise/cancellation. Numerical tích hợp (integration / 통합) accumulates and is often smoother. Automatic differentiation does neither approximation: it executes the chuỗi (chain / 사슬) quy tắc (rule / 규칙) through a computational đồ thị (graph / 그래프). Choosing among them depends on what biểu diễn (representation / 표현) of the hàm (function / 함수) you actually possess.

> **Nối mạch:** Trong **Numerical calculus: finite differences, quadrature và automatic differentiation**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**Smaller finite-difference step is always better.** No; truncation falls while rounding/noise amplification eventually rises.

**AD is numerical differentiation.** No; AD applies chính xác (exact / 정확한) chain-rule algebra to program primitives in floating-point arithmetic.

**Higher-order quadrature always wins.** Only when smoothness and sampling các giả định (assumptions / 가정들) justify it.

**A symbolic derivative guarantees stable numerical evaluation.** No; evaluation can still suffer overflow, cancellation or ill-conditioning.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
