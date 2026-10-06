# Toán số: approximation, conditioning và stability trên máy tính hữu hạn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**. Route đi từ exact mathematics và computed number → absolute/relative error → conditioning, stability và floating-point → approximation/convergence → kiểm chứng numerical result, để công thức đúng được nối với độ tin cậy tính toán.

Toán số (Numerical Analysis / 수치해석) nghiên cứu cách biến một bài toán (problem / 문제) toán học thành computation đáng tin cậy trên máy tính thực. Điểm xuất phát là một sự thật dễ bỏ qua: computer không thao tác với số thực vô hạn chính xác, không thực hiện vô hạn bước, và thường chỉ thấy dữ liệu đã có đo lường (measurement / 측정) noise.

Vì vậy một công thức đúng về mặt toán học chưa bảo đảm kết quả tính được đáng tin. Numerical phân tích (analysis / 분석) tách ít nhất ba câu hỏi:

1. **bài toán (problem / 문제) có nhạy không?** — conditioning.
2. **Ta đang approximate ideal mathematics bằng scheme nào?** — discretization/truncation.
3. **thuật toán (algorithm / 알고리즘) trên finite precision có khuếch đại lỗi (error / 오류) không?** — stability.

> Một numerical kết quả (result / 결과) chỉ đáng tin khi ta hiểu cả mathematical bài toán (problem / 문제), approximation scheme và machine arithmetic.

## Chính xác (exact / 정확한) mathematics và computed number là hai tầng khác nhau

Giả sử ta muốn solve

```math
Ax=b.
```

Trong chính xác (exact / 정확한) arithmetic, nếu `A` invertible thì solution unique:

```math
x=A^{-1}b.
```

Nhưng trong thực tế có ba vấn đề riêng:

- entries của `A,b` có thể đã là measurements có noise;
- machine lưu numbers bằng floating điểm (point / 지점) nên arithmetic bị rounding;
- computing tường minh (explicit / 명시적) inverse có thể không phải thuật toán (algorithm / 알고리즘) tốt để solve hệ thống (system / 시스템).

Do đó statement “equation có unique solution” không trả lời được “computed solution có accurate không?”.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Lỗi (error / 오류): absolute và relative** nối từ **Chính xác (exact / 정확한) mathematics và computed number là hai tầng khác nhau** sang **Sai số đo lường (measurement error / 측정 오차), mô hình (model / 모델) lỗi (error / 오류) và numerical lỗi (error / 오류) không giống nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Lỗi (error / 오류): absolute và relative

Nếu true giá trị (value / 값) là `x` và approximation là `\hat x`, absolute lỗi (error / 오류) là

```math
|\hat x-x|.
```

Relative lỗi (error / 오류) là

```math
\frac{|\hat x-x|}{|x|},
```

khi `x≠0`.

Absolute lỗi (error / 오류) phù hợp khi quy mô (scale / 규모) tự thân có ý nghĩa. Relative lỗi (error / 오류) quan trọng khi so accuracy giữa quantities khác magnitude.

Ví dụ approximation `1000001` cho true giá trị (value / 값) `1000000` có absolute lỗi (error / 오류) `1`, nhưng relative lỗi (error / 오류) chỉ

```math
10^{-6}.
```

Ngược lại approximation `0.0011` cho `0.0010` có absolute lỗi (error / 오류) rất nhỏ `0.0001`, nhưng relative lỗi (error / 오류) 10%.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Lỗi (error / 오류): absolute và relative** đặt vấn đề; **Sai số đo lường (measurement error / 측정 오차), mô hình (model / 모델) lỗi (error / 오류) và numerical lỗi (error / 오류) không giống nhau** đối chiếu bằng chứng, rồi **Floating điểm (point / 지점): tại sao 0.1+0.2 không chính xác (exact / 정확한)?** mở rộng hệ quả hoặc giới hạn liên quan.

## Sai số đo lường (measurement error / 측정 오차), mô hình (model / 모델) lỗi (error / 오류) và numerical lỗi (error / 오류) không giống nhau

Một kỹ thuật (engineering / 엔지니어링) computation có thể sai do:

**sai số đo lường (measurement error / 측정 오차):** đầu vào (input / 입력) dữ liệu (data / 데이터) không chính xác (exact / 정확한).

**mô hình (model / 모델) lỗi (error / 오류):** mathematical mô hình (model / 모델) bỏ qua physics/nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작) quan trọng.

**Discretization lỗi (error / 오류):** continuous/infinite đối tượng (object / 객체) được replace bằng finite approximation.

**Rounding lỗi (error / 오류):** finite-precision arithmetic.

**Algorithmic instability:** small computational perturbations bị amplify.

Không nên gộp tất cả thành “máy tính sai số”. Nếu mô hình (model / 모델) giả định (assumption / 가정) sai, tăng floating-point precision không cứu được kết quả (result / 결과).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Sai số đo lường (measurement error / 측정 오차), mô hình (model / 모델) lỗi (error / 오류) và numerical lỗi (error / 오류) không giống nhau** đặt vấn đề; **Floating điểm (point / 지점): tại sao 0.1+0.2 không chính xác (exact / 정확한)?** đối chiếu bằng chứng, rồi **Machine epsilon và spacing** mở rộng hệ quả hoặc giới hạn liên quan.

## Floating điểm (point / 지점): tại sao `0.1+0.2` không chính xác (exact / 정확한)?

Nhị phân (binary / 이진) floating điểm (point / 지점) biểu diễn finite set numbers gần dạng

```math
(-1)^s\times m\times2^e,
```

với finite significand `m` và exponent `e`.

Giống như `1/3=0.3333...` không có finite decimal biểu diễn (representation / 표현), `0.1` không có finite nhị phân (binary / 이진) biểu diễn (representation / 표현). Computer lưu nearby representable number.

Do đó

```text
0.1 + 0.2
```

có thể không equal exactly `0.3` theo bit mẫu (pattern / 패턴).

Điểm đúng không phải “floating điểm (point / 지점) tệ”, mà là **finite biểu diễn (representation / 표현) không thể represent mọi real number**.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Machine epsilon và spacing** nối từ **Floating điểm (point / 지점): tại sao 0.1+0.2 không chính xác (exact / 정확한)?** sang **Associativity có thể mất**, vì cơ chế trước tạo đầu vào cho bước sau.

## Machine epsilon và spacing

Machine epsilon roughly mô tả khoảng cách relative giữa `1` và next representable number lớn hơn `1` cho một floating format.

Floating điểm (point / 지점) có approximately constant **relative** precision trong normal phạm vi (range / 범위), không constant absolute spacing. Numbers magnitude lớn có spacing lớn hơn.

Vì vậy adding tiny number vào huge number có thể không thay biểu diễn (representation / 표현):

```text
large + tiny == large
```

nếu `tiny` nhỏ hơn resolution tại quy mô (scale / 규모) đó.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Associativity có thể mất** nối từ **Machine epsilon và spacing** sang **Catastrophic cancellation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Associativity có thể mất

Trong chính xác (exact / 정확한) real arithmetic,

```math
(a+b)+c=a+(b+c).
```

Trong floating điểm (point / 지점), intermediate rounding làm định danh (identity / 식별자) có thể thất bại (fail / 실패) numerically.

Ví dụ nếu `a` rất lớn, `b=-a`, `c` nhỏ:

```text
(a + b) + c
```

có thể giữ `c`, trong khi

```text
a + (b + c)
```

có thể round `b+c` về gần `b`, rồi cancel thành 0.

Parallel reductions vì vậy có thể cho last-bit differences tùy thứ tự (order / 순서) summation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Catastrophic cancellation** nối từ **Associativity có thể mất** sang **Conditioning: bài toán (problem / 문제) bản thân nhạy tới mức nào?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Catastrophic cancellation

Nếu subtract hai gần-equal floating numbers, leading digits cancel và relative lỗi (error / 오류) có thể tăng mạnh.

Ví dụ quadratic formula

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
```

có thể unstable cho một gốc (root / 루트) khi `b` và square gốc (root / 루트) gần nhau, vì numerator subtract gần-equal quantities.

Algebraically equivalent reformulation có thể numerically tốt hơn.

Đây là lesson quan trọng: **symbolically equivalent formulas không nhất thiết computationally equivalent**.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Conditioning: bài toán (problem / 문제) bản thân nhạy tới mức nào?** nối từ **Catastrophic cancellation** sang **Điều kiện (condition / 조건) number của hệ tuyến tính (linear system / 선형 시스템)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Conditioning: bài toán (problem / 문제) bản thân nhạy tới mức nào?

Conditioning là thuộc tính (property / 속성) của bài toán (problem / 문제), không phải của thuật toán (algorithm / 알고리즘).

Suppose hàm (function / 함수)

```math
y=f(x).
```

Nếu small perturbation `δx` tạo large relative thay đổi (change / 변경) trong `y`, bài toán (problem / 문제) ill-conditioned quanh đó.

First-order sensitivity có thể nhìn qua derivative:

```math
\delta y\approx f'(x)\delta x.
```

Relative điều kiện (condition / 조건) number một biến thường liên quan

```math
\kappa(x)=\left|\frac{x f'(x)}{f(x)}\right|,
```

khi expression hợp lệ.

Large `κ` nghĩa đầu vào (input / 입력) relative lỗi (error / 오류) có thể bị amplify mạnh trong đầu ra (output / 출력).

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Điều kiện (condition / 조건) number của hệ tuyến tính (linear system / 선형 시스템)** nối từ **Conditioning: bài toán (problem / 문제) bản thân nhạy tới mức nào?** sang **Stability: thuật toán (algorithm / 알고리즘) có thêm amplification không?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điều kiện (condition / 조건) number của hệ tuyến tính (linear system / 선형 시스템)

Cho invertible ma trận (matrix / 행렬) `A`, điều kiện (condition / 조건) number theo chosen norm là

```math
\kappa(A)=\|A\|\,\|A^{-1}\|.
```

Nếu `κ(A)` lớn, hệ thống (system / 시스템) gần singular theo norm đó; small perturbations trong dữ liệu (data / 데이터) có thể gây large changes trong solution.

Geometrically, transformation `A` squash một số directions rất mạnh. Inverting phải expand lại những directions đó, đồng thời amplify noise.

Đây là reason near-collinear features làm least squares nhạy và multicollinearity gây unstable coefficients.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Stability: thuật toán (algorithm / 알고리즘) có thêm amplification không?** nối từ **Điều kiện (condition / 조건) number của hệ tuyến tính (linear system / 선형 시스템)** sang **Forward lỗi (error / 오류) và backward lỗi (error / 오류)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Stability: thuật toán (algorithm / 알고리즘) có thêm amplification không?

Conditioning hỏi “bài toán (problem / 문제) khó nhạy đến đâu”. Stability hỏi “thuật toán (algorithm / 알고리즘) có làm tình hình tệ hơn bản chất bài toán (problem / 문제) không?”.

Một thuật toán (algorithm / 알고리즘) backward stable trả computed answer đúng chính xác cho một nearby bài toán (problem / 문제):

```text
computed solution = exact solution of slightly perturbed input.
```

Nếu bài toán (problem / 문제) well-conditioned, nearby đầu vào (input / 입력) tạo nearby đầu ra (output / 출력), nên backward stability thường dẫn tới forward accuracy tốt.

Numerical tuyến tính (linear / 선형) algebra đánh giá algorithms theo lens này thay vì chỉ count arithmetic operations.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Forward lỗi (error / 오류) và backward lỗi (error / 오류)** nối từ **Stability: thuật toán (algorithm / 알고리즘) có thêm amplification không?** sang **Truncation lỗi (error / 오류): finite approximation của infinite tiến trình (process / 프로세스)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Forward lỗi (error / 오류) và backward lỗi (error / 오류)

Forward lỗi (error / 오류) đo distance từ computed kết quả (result / 결과) tới true kết quả (result / 결과).

Backward lỗi (error / 오류) hỏi: đầu vào (input / 입력) phải thay đổi ít nhất bao nhiêu để computed kết quả (result / 결과) trở thành chính xác (exact / 정확한) answer?

Một kết quả (result / 결과) có forward lỗi (error / 오류) lớn nhưng backward lỗi (error / 오류) nhỏ nếu bài toán (problem / 문제) ill-conditioned. Khi đó thuật toán (algorithm / 알고리즘) có thể hoạt động tốt, nhưng bài toán (problem / 문제) bản thân amplify bất định (uncertainty / 불확실성).

Distinction này giúp tránh blame thuật toán (algorithm / 알고리즘) cho sensitivity vốn nằm trong bài toán (problem / 문제).

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Forward lỗi (error / 오류) và backward lỗi (error / 오류)** đặt đầu vào cho **Truncation lỗi (error / 오류): finite approximation của infinite tiến trình (process / 프로세스)**, rồi **Tại sao “step càng nhỏ càng tốt” sai?** mở rộng hệ quả hoặc giới hạn liên quan.

## Truncation lỗi (error / 오류): finite approximation của infinite tiến trình (process / 프로세스)

Derivative được định nghĩa bằng limit:

```math
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
```

Computer phải chọn finite `h`, nên dùng approximation

```math
f'(x)\approx\frac{f(x+h)-f(x)}{h}.
```

Taylor expansion cho thấy forward difference có truncation lỗi (error / 오류) thứ tự (order / 순서) `O(h)` dưới smoothness các giả định (assumptions / 가정들).

Central difference

```math
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
```

thường có truncation lỗi (error / 오류) `O(h^2)`.

Higher thứ tự (order / 순서) không có nghĩa luôn better: smaller `h` giảm truncation lỗi (error / 오류) nhưng có thể tăng rounding/cancellation lỗi (error / 오류).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Truncation lỗi (error / 오류): finite approximation của infinite tiến trình (process / 프로세스)** đặt đầu vào cho **Tại sao “step càng nhỏ càng tốt” sai?**, rồi **Gốc (root / 루트) finding: bisection từ continuity** mở rộng hệ quả hoặc giới hạn liên quan.

## Tại sao “step càng nhỏ càng tốt” sai?

Derivative finite difference minh họa sự đánh đổi (trade-off / 트레이드오프).

Nếu `h` lớn, approximation lỗi (error / 오류) do Taylor truncation lớn.

Nếu `h` cực nhỏ, `f(x+h)` và `f(x)` gần nhau; subtraction có cancellation, sau đó division by tiny `h` amplify rounding.

Total lỗi (error / 오류) thường có U-shaped hành vi (behavior / 동작) theo `h`: giảm trước rồi tăng.

Optimal step kích thước (size / 크기) cân bằng truncation và floating-point errors.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Gốc (root / 루트) finding: bisection từ continuity** nối từ **Tại sao “step càng nhỏ càng tốt” sai?** sang **Newton phương thức (method / 메서드): cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gốc (root / 루트) finding: bisection từ continuity

Suppose continuous hàm (function / 함수) `f` thỏa

```math
f(a)f(b)<0.
```

Intermediate giá trị (value / 값) Theorem bảo đảm có ít nhất một gốc (root / 루트) trong `(a,b)`.

Bisection lấy midpoint

```math
m=\frac{a+b}{2}
```

và giữ half interval còn sign thay đổi (change / 변경).

Sau `k` iterations, interval width là

```math
\frac{b-a}{2^k}.
```

Muốn width ≤ `ε`, cần

```math
k\ge\log_2\frac{b-a}{\varepsilon}.
```

Bisection chậm hơn Newton nhưng robust vì giữ bracket và dựa trên theorem rõ ràng.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Newton phương thức (method / 메서드): cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** nối từ **Gốc (root / 루트) finding: bisection từ continuity** sang **Hybrid gốc (root / 루트) solvers**, vì cơ chế trước tạo đầu vào cho bước sau.

## Newton phương thức (method / 메서드): cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)

Newton iteration là

```math
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}.
```

Derivation đến từ tangent approximation quanh `x_n`:

```math
f(x)\approx f(x_n)+f'(x_n)(x-x_n).
```

Set approximation bằng zero và solve cho `x`:

```math
0\approx f(x_n)+f'(x_n)(x_{n+1}-x_n),
```

suy ra Newton cập nhật (update / 업데이트).

Near a simple gốc (root / 루트) và dưới smoothness/initialization conditions tốt, convergence có thể quadratic.

Nhưng Newton có thất bại (failure / 실패) modes: derivative gần zero, initial guess xấu, oscillation hoặc convergence tới gốc (root / 루트) không mong muốn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Hybrid gốc (root / 루트) solvers** nối từ **Newton phương thức (method / 메서드): cục bộ (local / 로컬) mô hình tuyến tính (linear model / 선형 모델)** sang **Interpolation và approximation không giống nhau**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hybrid gốc (root / 루트) solvers

Môi trường vận hành (production / 운영 환경) numerical libraries thường không chọn “bisection hoặc Newton” theo kiểu tuyệt đối. Hybrid methods combine robustness của bracketing với speed của interpolation/Newton-like steps.

Đây là recurring kỹ thuật (engineering / 엔지니어링) mẫu (pattern / 패턴): use fast phương thức (method / 메서드) khi conditions tốt, fallback sang safe phương thức (method / 메서드) khi bất biến (invariant / 불변식) bị đe dọa.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Interpolation và approximation không giống nhau** nối từ **Hybrid gốc (root / 루트) solvers** sang **Polynomial basis và conditioning**, vì cơ chế trước tạo đầu vào cho bước sau.

## Interpolation và approximation không giống nhau

Interpolation tìm hàm (function / 함수) đi qua dữ liệu (data / 데이터) points exactly.

Approximation/regression cho phép residual để đạt stability/generalization tốt hơn.

High-degree polynomial interpolation qua equally spaced points có thể oscillate mạnh gần endpoints — Runge phenomenon.

Piecewise polynomial splines dùng cục bộ (local / 로컬) low-degree pieces, thường smooth và stable hơn toàn cục (global / 전역) high-degree polynomial.

Điều này minh họa nguyên tắc: **degree cao hơn không tự động là mô hình (model / 모델) tốt hơn**.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Polynomial basis và conditioning** nối từ **Interpolation và approximation không giống nhau** sang **Numerical tích hợp (integration / 통합)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Polynomial basis và conditioning

Ngay cả khi polynomial mô hình (model / 모델) hợp lý, basis choice ảnh hưởng numerical conditioning.

Monomial basis

```math
1,x,x^2,\ldots,x^n
```

trên wide interval có thể tạo Vandermonde ma trận (matrix / 행렬) ill-conditioned.

Orthogonal polynomial bases như Chebyshev polynomials thường tốt hơn cho approximation.

Một lần nữa, mathematical không gian (space / 공간) giống nhau nhưng biểu diễn (representation / 표현)/basis khác có numerical hành vi (behavior / 동작) rất khác.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Numerical tích hợp (integration / 통합)** nối từ **Polynomial basis và conditioning** sang **Monte Carlo tích hợp (integration / 통합)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Numerical tích hợp (integration / 통합)

Definite integral

```math
\int_a^b f(x)\,dx
```

thường được approximate từ finite evaluations.

Trapezoidal quy tắc (rule / 규칙) approximate đồ thị (graph / 그래프) bằng line segments. Simpson's quy tắc (rule / 규칙) dùng cục bộ (local / 로컬) quadratic approximation. Gaussian quadrature chọn nodes/weights thông minh để integrate polynomial degree cao với ít evaluations hơn.

Adaptive quadrature refine interval nơi hàm (function / 함수) khó hơn thay vì dùng uniform tiny step mọi nơi.

Phương thức (method / 메서드) phù hợp phụ thuộc smoothness, singularities, oscillation và chi phí (cost / 비용) của evaluating `f`.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Monte Carlo tích hợp (integration / 통합)** nối từ **Numerical tích hợp (integration / 통합)** sang **Solve tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): đừng mặc định invert ma trận (matrix / 행렬)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Monte Carlo tích hợp (integration / 통합)

Trong high dimensions, deterministic grid-based tích hợp (integration / 통합) chịu curse of dimensionality. Monte Carlo estimate expectation bằng random samples:

```math
\int f(x)p(x)dx
=\mathbb E[f(X)]
\approx\frac1N\sum_{i=1}^N f(X_i).
```

Typical tiêu chuẩn (standard / 표준) lỗi (error / 오류) decrease khoảng

```math
O(N^{-1/2}).
```

Convergence tỷ lệ (rate / 비율) không nhanh theo `N`, nhưng không explode trực tiếp với dimension theo grid count, nên Monte Carlo rất quan trọng trong finance, Bayesian suy luận (inference / 추론) và physics simulations.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Solve tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): đừng mặc định invert ma trận (matrix / 행렬)** nối từ **Monte Carlo tích hợp (integration / 통합)** sang **Sparsity thay đổi computation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Solve tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): đừng mặc định invert ma trận (matrix / 행렬)

Mathematically,

```math
x=A^{-1}b.
```

Nhưng computationally, forming tường minh (explicit / 명시적) inverse thường tốn hơn và có thể less stable so với factorization + solve.

Dense hệ thống (system / 시스템) thường dùng LU decomposition. Symmetric positive definite hệ thống (system / 시스템) có thể dùng Cholesky. Least squares thường dùng QR; SVD robust hơn khi rank-deficient hoặc near-degenerate.

Thuật toán (algorithm / 알고리즘) choice nên exploit cấu trúc (structure / 구조).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Sparsity thay đổi computation** nối từ **Solve tuyến tính (linear / 선형) các hệ thống (systems / 시스템들): đừng mặc định invert ma trận (matrix / 행렬)** sang **Iterative tuyến tính (linear / 선형) solvers**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sparsity thay đổi computation

Large matrices trong PDE, graphs và recommendation các hệ thống (systems / 시스템들) thường sparse: phần lớn entries bằng zero.

Dense `n×n` lưu trữ (storage / 저장소) cần `O(n^2)` numbers, nhưng sparse biểu diễn (representation / 표현) chỉ lưu nonzeros.

Sparse direct/iterative solvers có thể giảm bộ nhớ (memory / 메모리) và computation cực lớn, nhưng fill-in, thứ tự (ordering / 순서) và conditioning trở thành issues quan trọng.

“ma trận (matrix / 행렬) kích thước (size / 크기)” một mình không đủ dự đoán difficulty.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Iterative tuyến tính (linear / 선형) solvers** nối từ **Sparsity thay đổi computation** sang **Numerical ODE và stability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Iterative tuyến tính (linear / 선형) solvers

Khi ma trận (matrix / 행렬) quá lớn để factorize dense, iterative methods xây chuỗi (sequence / 시퀀스) approximations.

Conjugate độ dốc (gradient / 기울기) hiệu quả cho symmetric positive definite các hệ thống (systems / 시스템들). GMRES xử lý broader nonsymmetric cases.

Convergence thường phụ thuộc spectrum/điều kiện (condition / 조건) number. Preconditioning transform hệ thống (system / 시스템) thành equivalent bài toán (problem / 문제) có conditioning tốt hơn.

Preconditioner tốt có thể quan trọng hơn micro-optimization mã (code / 코드).

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Numerical ODE và stability** nối từ **Iterative tuyến tính (linear / 선형) solvers** sang **Convergence, consistency và stability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Numerical ODE và stability

Euler phương thức (method / 메서드) cho

```math
x'(t)=f(t,x)
```

là

```math
x_{n+1}=x_n+h f(t_n,x_n).
```

Nó dùng tangent cục bộ (local / 로컬) để advance one step.

Higher-order Runge–Kutta methods combine multiple slope evaluations để giảm truncation lỗi (error / 오류).

Nhưng differential equations có thể **stiff**: tường minh (explicit / 명시적) phương thức (method / 메서드) cần tiny step vì stability, không chỉ accuracy. Implicit methods có thể cho phép larger stable steps dù mỗi step phải solve equation.

Numerical stability của thời gian (time / 시간) tích hợp (integration / 통합) là concept riêng, không thể đánh giá chỉ bằng cục bộ (local / 로컬) truncation thứ tự (order / 순서).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Convergence, consistency và stability** nối từ **Numerical ODE và stability** sang **Stopping criteria**, vì cơ chế trước tạo đầu vào cho bước sau.

## Convergence, consistency và stability

Trong discretized differential equations, ba ideas thường liên kết:

**Consistency:** discrete scheme approximate đúng continuous equation khi step → 0.

**Stability:** errors không grow uncontrolled dưới discretized dynamics.

**Convergence:** numerical solution tiến tới chính xác (exact / 정확한) solution khi refinement.

Một scheme có cục bộ (local / 로컬) approximation đẹp nhưng unstable vẫn có thể diverge globally.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Stopping criteria** nối từ **Convergence, consistency và stability** sang **Scaling và nondimensionalization**, vì cơ chế trước tạo đầu vào cho bước sau.

## Stopping criteria

Iterative thuật toán (algorithm / 알고리즘) không nên dừng chỉ vì “đã chạy 1000 iterations”. Better criteria dựa trên residual, cập nhật (update / 업데이트) kích thước (size / 크기) hoặc estimated lỗi (error / 오류).

Cho hệ tuyến tính (linear system / 선형 시스템),

```math
r=b-A\hat x
```

là residual. Small residual nói computed `\hat x` gần satisfy equation. Nhưng nếu bài toán (problem / 문제) ill-conditioned, small residual không guarantee small forward lỗi (error / 오류).

Stopping criterion phải match quantity ta thật sự quan tâm.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Scaling và nondimensionalization** nối từ **Stopping criteria** sang **Reproducibility trong parallel computing**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scaling và nondimensionalization

Nếu variables khác orders of magnitude rất lớn, numerical solver có thể khó optimize hoặc solve hệ thống (system / 시스템).

Rescaling variables về comparable ranges giúp conditioning và tối ưu hóa (optimization / 최적화) hình học (geometry / 기하학).

Trong vật lý (physical / 물리적) các mô hình (models / 모델들), nondimensionalization còn reveal controlling ratios và reduce parameter count.

Scaling không chỉ là cosmetic normalization; nó có thể thay numerical difficulty.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Reproducibility trong parallel computing** nối từ **Scaling và nondimensionalization** sang **Mixed precision**, vì cơ chế trước tạo đầu vào cho bước sau.

## Reproducibility trong parallel computing

Floating-point sum phụ thuộc thứ tự (order / 순서). Parallel threads/GPUs có thể reduce values theo different trees, tạo last-bit differences.

Deterministic bitwise reproducibility có thể cần fixed reduction thứ tự (order / 순서) và chi phí (cost / 비용) hiệu năng (performance / 성능).

Trong ML/scientific computing, cần phân biệt:

- bitwise identical kết quả (result / 결과);
- numerically close kết quả (result / 결과);
- statistically equivalent huấn luyện (training / 학습) kết quả (outcome / 결과).

Không phải mọi nondeterminism đều là bug, nhưng yêu cầu (requirement / 요구사항) phải được định nghĩa rõ.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Mixed precision** nối từ **Reproducibility trong parallel computing** sang **Interval arithmetic và rigorous bounds**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mixed precision

Hiện đại (modern / 현대적) accelerators thường dùng FP16/BF16 cho speed và bộ nhớ (memory / 메모리), trong khi giữ một số accumulations/parameters ở FP32.

Mixed-precision huấn luyện (training / 학습) thành công nhờ hiểu động (dynamic / 동적) phạm vi (range / 범위), scaling và lan truyền lỗi (error propagation / 오류 전파) — không phải vì lower precision “đủ đại khái”.

Mất mát (loss / 손실) scaling giúp tránh độ dốc (gradient / 기울기) underflow trong low precision.

Đây là numerical phân tích (analysis / 분석) xuất hiện trực tiếp trong deep học tập (learning / 학습) kỹ thuật (engineering / 엔지니어링).

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Interval arithmetic và rigorous bounds** nối từ **Mixed precision** sang **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Interval arithmetic và rigorous bounds

Tiêu chuẩn (standard / 표준) floating điểm (point / 지점) trả một approximation. Interval arithmetic represent giá trị (value / 값) bằng interval guaranteed chứa true kết quả (result / 결과) under controlled rounding.

Nó hữu ích khi cần verified computation, nhưng intervals có thể widen do phụ thuộc (dependency / 의존성) effects.

Không phải mọi ứng dụng (application / 애플리케이션) cần rigorous bounds, nhưng concept này cho thấy numerical đầu ra (output / 출력) có thể đi kèm certificate về bất định (uncertainty / 불확실성) thay vì chỉ một number.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, sau nội dung của **Interval arithmetic và rigorous bounds**, **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링)** mở rộng hệ quả hoặc giới hạn liên quan.

## Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)

Độ dốc (gradient / 기울기) descent dùng gradients được computed finite precision. học tập (learning / 학습) tỷ lệ (rate / 비율) quá lớn gây dynamical instability; gradients rất nhỏ có underflow; ill-conditioned Hessian tạo narrow valleys và slow convergence.

Preconditioning, normalization, adaptive optimizers và second-order methods đều có numerical-analysis flavor: reshape bài toán (problem / 문제) để thuật toán (algorithm / 알고리즘) thấy hình học (geometry / 기하학) dễ hơn.

> **Nối mạch:** Trong **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và tối ưu hóa (optimization / 최적화)** đặt vấn đề; **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링)** đối chiếu bằng chứng, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả hoặc giới hạn liên quan.

## Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링)

Summing billions of values có rounding accumulation. Naive mean/variance formulas có thể cancellation. Stable online algorithms như Welford's phương thức (method / 메서드) giảm lỗi (error / 오류) khi tính variance streaming.

Financial các hệ thống (systems / 시스템들) thường tránh nhị phân (binary / 이진) floating điểm (point / 지점) cho chính xác (exact / 정확한) decimal currency rules, dùng fixed-point/decimal representations phù hợp nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

Biểu diễn (representation / 표현) choice vì thế là mathematical quyết định (decision / 결정), không chỉ programming detail.

> **Nối mạch:** Ở chặng này của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, các dấu vết trong **Liên kết kiến thức (knowledge connection / 지식 연결) — numerical phân tích (analysis / 분석) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Numerical phân tích (analysis / 분석) là science của **độ tin cậy khi toán học đi qua máy tính hữu hạn**. Trước một number computed, hãy hỏi: đầu vào (input / 입력) có noise gì, bài toán (problem / 문제) nhạy tới đâu, approximation bỏ qua gì, arithmetic round thế nào, thuật toán (algorithm / 알고리즘) có amplify lỗi (error / 오류) không, và đầu ra (output / 출력) accuracy ta thật sự cần là gì. Một formula đúng chỉ là điểm bắt đầu.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Toán số: approximation, conditioning và stability trên máy tính hữu hạn**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

**“Dùng nhiều chữ số hơn thì answer tự động chính xác hơn.”** Precision cao giảm rounding nhưng không sửa mô hình (model / 모델) lỗi (error / 오류), đo lường (measurement / 측정) noise hay ill-conditioning.

**“Step kích thước (size / 크기) càng nhỏ càng tốt.”** Quá nhỏ có thể tăng cancellation/rounding và computation chi phí (cost / 비용); stiff các hệ thống (systems / 시스템들) còn có stability các ràng buộc (constraints / 제약조건들) riêng.

**“Hai formulas algebraically equivalent sẽ cho cùng computed kết quả (result / 결과).”** Finite precision làm thứ tự (order / 순서) và cancellation matter.

**“điều kiện (condition / 조건) number lớn nghĩa thuật toán (algorithm / 알고리즘) tệ.”** Conditioning là thuộc tính (property / 속성) của bài toán (problem / 문제). thuật toán (algorithm / 알고리즘) stability là question khác.

**“Residual nhỏ nghĩa solution lỗi (error / 오류) nhỏ.”** Chỉ chắc hơn khi bài toán (problem / 문제) well-conditioned hoặc có additional bounds.

**“Muốn solve `Ax=b` thì cứ tính `A^{-1}`.”** Trong numerical tuyến tính (linear / 선형) algebra, factorization/structured solvers thường nhanh và stable hơn tường minh (explicit / 명시적) inverse.

**“Floating điểm (point / 지점) bug vì `0.1+0.2≠0.3` chính xác (exact / 정확한).”** Đó là consequence bình thường của finite nhị phân (binary / 이진) biểu diễn (representation / 표현). Bug chỉ xuất hiện khi software giả định chính xác (exact / 정확한) ngữ nghĩa (semantics / 의미론) mà biểu diễn (representation / 표현) không bảo đảm.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
