# Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus

> **Mạch đọc:** [README](../README.md) là owner của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**; đặt chapter sau sequences/functions và trước complex analysis. Từ **Completeness của real numbers** nối qua sequences/convergence, epsilon–delta limits, continuity, compactness, series và theorem conditions, rồi dùng proof để phân biệt trực giác đúng với kết luận cần giả định.

Calculus thường bắt đầu bằng trực giác: một quantity “tiến gần” một giá trị (value / 값), một curve “trơn”, hoặc một infinite sum “có vẻ ổn định”. **Real phân tích (analysis / 분석)** hỏi câu khó hơn: chính xác điều đó có nghĩa gì, và ta chứng minh nó như thế nào mà không dựa vào hình vẽ hay cảm giác?

Mục tiêu của real phân tích (analysis / 분석) không phải làm calculus khó hơn. Nó làm rõ những các giả định (assumptions / 가정들) ẩn phía sau derivative, integral, infinite series, approximation và numerical computation. Khi hiểu phân tích (analysis / 분석), ta biết khi nào một phép đổi limit với integral là hợp lệ, khi nào một chuỗi (sequence / 시퀀스) thật sự hội tụ, và tại sao một theorem cần các conditions cụ thể.

## Completeness của real numbers

Điểm khác biệt quan trọng giữa rational numbers `Q` và real numbers `R` là **completeness (완비성)**.

Ví dụ chuỗi (sequence / 시퀀스) các rational approximations của `sqrt(2)` có thể tiến gần một limit không thuộc `Q`. Trong `R`, limit đó tồn tại.

Một formulation quan trọng là least upper bound thuộc tính (property / 속성): mọi nonempty subset của `R` bị chặn trên đều có supremum trong `R`.

Nếu

```math
S=\{x\in\mathbb R:x^2<2\},
```

thì `S` bị chặn trên và supremum của nó là `sqrt(2)`.

Completeness là nền móng của rất nhiều convergence theorems.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Completeness của real numbers** xác định đầu vào; **Chuỗi (sequence / 시퀀스) và convergence** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bounded và monotone chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) và convergence

Một chuỗi (sequence / 시퀀스) `(a_n)` hội tụ về `L` nếu

```math
\forall \varepsilon>0,\ \exists N\in\mathbb N
```

sao cho

```math
n\ge N\Rightarrow |a_n-L|<\varepsilon.
```

Ý tưởng là ta có thể yêu cầu sai số nhỏ tùy ý; từ một chỉ mục (index / 인덱스) đủ lớn trở đi chuỗi (sequence / 시퀀스) luôn nằm trong tolerance đó.

Ví dụ

```math
a_n=\frac1n.
```

Muốn `|1/n|<ε`, chỉ cần chọn `N>1/ε`.

Định nghĩa epsilon này biến câu “1/n tiến về 0” thành một claim có thể chứng minh.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Chuỗi (sequence / 시퀀스) và convergence** xác định đầu vào; **Bounded và monotone chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Cauchy chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bounded và monotone chuỗi (sequence / 시퀀스)

Nếu chuỗi (sequence / 시퀀스) tăng dần và bị chặn trên, nó hội tụ. Tương tự, chuỗi (sequence / 시퀀스) giảm dần và bị chặn dưới cũng hội tụ.

Đây là **monotone convergence theorem** cho sequences và là một biểu hiện trực tiếp của completeness.

Ví dụ iterative algorithms đôi khi tạo chuỗi (sequence / 시퀀스) mục tiêu (objective / 목표) values giảm dần và bị chặn dưới bởi 0. Điều đó cho biết values hội tụ, dù chưa đủ để kết luận parameters hội tụ tới toàn cục (global / 전역) optimum.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Bounded và monotone chuỗi (sequence / 시퀀스)** xác định đầu vào; **Cauchy chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Subsequences và Bolzano–Weierstrass** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cauchy chuỗi (sequence / 시퀀스)

Một chuỗi (sequence / 시퀀스) là Cauchy nếu các terms cuối cùng gần nhau:

```math
\forall\varepsilon>0,\exists N:\ m,n\ge N\Rightarrow |a_m-a_n|<\varepsilon.
```

Điểm hay là định nghĩa không cần biết trước limit là gì.

Trong `R`, mọi Cauchy chuỗi (sequence / 시퀀스) đều hội tụ. Đây là một dạng khác của completeness.

Trong numerical computation, Cauchy-like stopping criteria rất tự nhiên: nếu successive iterates thay đổi ngày càng nhỏ, ta nghi ngờ thuật toán (algorithm / 알고리즘) đang ổn định. Tuy nhiên “successive difference nhỏ” trong finite computation không tự động chứng minh convergence về nghiệm đúng; conditioning và lỗi (error / 오류) phân tích (analysis / 분석) vẫn quan trọng.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Cauchy chuỗi (sequence / 시퀀스)** xác định đầu vào; **Subsequences và Bolzano–Weierstrass** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Limit superior và limit inferior** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Subsequences và Bolzano–Weierstrass

Một subsequence chọn một số terms theo thứ tự tăng của indices.

Bolzano–Weierstrass theorem nói rằng mọi bounded chuỗi (sequence / 시퀀스) trong `R^n` đều có một convergent subsequence.

Theorem này quan trọng trong tối ưu hóa (optimization / 최적화). Nếu iterates nằm trong một bounded region, ta có thể tìm convergent subsequences; từ đó phân tích cluster points và stationary conditions.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Subsequences và Bolzano–Weierstrass** đã nêu tiêu chí phân biệt, còn **Limit superior và limit inferior** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Continuity theo epsilon-delta** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Limit superior và limit inferior

Không phải chuỗi (sequence / 시퀀스) nào cũng hội tụ. Ví dụ

```math
a_n=(-1)^n
```

oscillates giữa `-1` và `1`.

Ta có thể mô tả long-term upper và lower hành vi (behavior / 동작) bằng

```math
\limsup a_n,
```

và

```math
\liminf a_n.
```

Nếu hai values bằng nhau và finite, chuỗi (sequence / 시퀀스) hội tụ về dùng chung (common / 공통) giá trị (value / 값) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Limit superior và limit inferior** đã nêu tiêu chí phân biệt, còn **Continuity theo epsilon-delta** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Sequential characterization của continuity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuity theo epsilon-delta

Hàm (function / 함수) `f` continuous tại `x_0` nếu

```math
\forall\varepsilon>0,\exists\delta>0:
|x-x_0|<\delta\Rightarrow |f(x)-f(x_0)|<\varepsilon.
```

`ε` là tolerance đầu ra (output / 출력); `δ` là tolerance đầu vào (input / 입력) đủ để đảm bảo đầu ra (output / 출력) nằm trong tolerance mong muốn.

Continuity có thể hiểu là small đầu vào (input / 입력) perturbations tạo small đầu ra (output / 출력) perturbations, nhưng epsilon-delta làm phát biểu này precise.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Sequential characterization của continuity** tiếp nhận điểm tựa từ **Continuity theo epsilon-delta** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Intermediate giá trị (value / 값) Theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sequential characterization của continuity

Một hàm (function / 함수) continuous tại `x` khi và chỉ khi mọi chuỗi (sequence / 시퀀스) `x_n→x` đều thỏa

```math
f(x_n)\to f(x).
```

Cách nhìn này đặc biệt hữu ích vì nhiều proofs về continuity có thể chuyển thành proofs về sequences.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Intermediate giá trị (value / 값) Theorem** tiếp nhận điểm tựa từ **Sequential characterization của continuity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Extreme giá trị (value / 값) Theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intermediate giá trị (value / 값) Theorem

Nếu `f` continuous trên `[a,b]` và một giá trị (value / 값) `y` nằm giữa `f(a)` và `f(b)`, thì tồn tại `c∈[a,b]` sao cho

```math
f(c)=y.
```

Root-finding methods như bisection dựa trên cấu trúc (structure / 구조) này. Nếu `f(a)` và `f(b)` trái dấu, continuity đảm bảo có ít nhất một gốc (root / 루트) giữa chúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Extreme giá trị (value / 값) Theorem** tiếp nhận điểm tựa từ **Intermediate giá trị (value / 값) Theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compactness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Extreme giá trị (value / 값) Theorem

Nếu `f` continuous trên compact interval `[a,b]`, thì `f` đạt maximum và minimum trên interval đó.

Không chỉ tồn tại supremum abstract; có điểm thực sự đạt nó.

Điều này cho thấy vì sao compactness quan trọng trong tối ưu hóa (optimization / 최적화): continuity cộng compact feasible set thường cho existence của optimum.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Compactness** tiếp nhận điểm tựa từ **Extreme giá trị (value / 값) Theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pointwise và uniform convergence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compactness

Trong `R^n`, Heine–Borel theorem cho biết một set compact khi và chỉ khi nó closed và bounded.

Compactness có thể hình dung là “không chạy ra infinity và không bỏ mất ranh giới (boundary / 경계) limit points”.

Nhiều theorem mạnh trở nên đúng trên compact sets: continuous functions uniformly continuous, extrema tồn tại, mọi chuỗi (sequence / 시퀀스) có convergent subsequence nằm trong set.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Pointwise và uniform convergence** tiếp nhận điểm tựa từ **Compactness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao pointwise convergence có thể gây bất ngờ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pointwise và uniform convergence

Cho chuỗi (sequence / 시퀀스) functions `f_n(x)`.

Pointwise convergence nghĩa là với mỗi `x` cố định,

```math
f_n(x)\to f(x).
```

Nhưng tốc độ convergence có thể khác rất nhiều tùy `x`.

Uniform convergence yêu cầu một `N` chung hoạt động cho toàn lĩnh vực (domain / 도메인):

```math
\forall\varepsilon>0,\exists N:
n\ge N\Rightarrow |f_n(x)-f(x)|<\varepsilon
```

cho mọi `x` trong lĩnh vực (domain / 도메인).

Uniform convergence mạnh hơn và thường cho phép bảo toàn continuity khi lấy limit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Vì sao pointwise convergence có thể gây bất ngờ** tiếp nhận điểm tựa từ **Pointwise và uniform convergence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Differentiability mạnh hơn continuity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao pointwise convergence có thể gây bất ngờ

Xét

```math
f_n(x)=x^n
```

trên `[0,1]`.

Với `0≤x<1`, `x^n→0`; tại `x=1`, giá trị (value / 값) luôn bằng 1. Limit hàm (function / 함수) là

```math
f(x)=
\begin{cases}
0,&0\le x<1\\
1,&x=1.
\end{cases}
```

Mỗi `f_n` continuous nhưng limit hàm (function / 함수) không continuous. Convergence chỉ pointwise, không uniform.

Đây là ví dụ cho thấy không thể tùy tiện chuyển mọi thuộc tính (property / 속성) qua limit.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Differentiability mạnh hơn continuity** tiếp nhận điểm tựa từ **Vì sao pointwise convergence có thể gây bất ngờ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mean giá trị (value / 값) Theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Differentiability mạnh hơn continuity

Nếu `f` differentiable tại một điểm thì nó continuous tại đó. Converse không đúng.

`f(x)=|x|` continuous tại 0 nhưng không differentiable vì left derivative và right derivative khác nhau.

Trong nhiều chiều, differentiability còn mạnh hơn việc tất cả partial derivatives tồn tại. Ta cần một single tuyến tính (linear / 선형) map approximates hàm (function / 함수) theo mọi direction cùng lúc.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Mean giá trị (value / 값) Theorem** tiếp nhận điểm tựa từ **Differentiability mạnh hơn continuity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Riemann integral và partitions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mean giá trị (value / 값) Theorem

Nếu `f` continuous trên `[a,b]` và differentiable trên `(a,b)`, tồn tại `c` sao cho

```math
f'(c)=\frac{f(b)-f(a)}{b-a}.
```

Theorem nối cục bộ (local / 로컬) derivative với toàn cục (global / 전역) thay đổi (change / 변경). Nhiều lỗi (error / 오류) bounds và uniqueness arguments dựa trên nó.

Ví dụ nếu `|f'(x)|≤M`, thì

```math
|f(x)-f(y)|\le M|x-y|.
```

Đây là một Lipschitz-type bound.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Riemann integral và partitions** tiếp nhận điểm tựa từ **Mean giá trị (value / 값) Theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fundamental Theorem of Calculus dưới góc nhìn phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Riemann integral và partitions

Riemann tích hợp (integration / 통합) chia interval thành subintervals và xấp xỉ area bằng sums.

Nếu partition là

```math
a=x_0<x_1<\cdots<x_n=b,
```

Riemann sum có dạng

```math
\sum_{i=1}^{n} f(\xi_i)(x_i-x_{i-1}).
```

Integral tồn tại khi các sums hội tụ về cùng giá trị (value / 값) khi mesh của partition tiến về 0, bất kể mẫu (sample / 표본) points `ξ_i` được chọn hợp lệ như thế nào.

Continuous functions trên closed bounded interval là Riemann integrable.

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Fundamental Theorem of Calculus dưới góc nhìn phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **Riemann integral và partitions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Interchanging limits, derivatives và integrals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fundamental Theorem of Calculus dưới góc nhìn phân tích (analysis / 분석)

Nếu `f` continuous và

```math
F(x)=\int_a^x f(t)dt,
```

thì

```math
F'(x)=f(x).
```

Đây không chỉ là formula. Nó khẳng định hai processes tưởng khác nhau — cục bộ (local / 로컬) tỷ lệ (rate / 비율) và toàn cục (global / 전역) accumulation — là inverses theo một nghĩa precise dưới appropriate conditions.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Fundamental Theorem of Calculus dưới góc nhìn phân tích (analysis / 분석)** đã nêu tiêu chí phân biệt, còn **Interchanging limits, derivatives và integrals** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Normed spaces và convergence không chỉ trong R** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Interchanging limits, derivatives và integrals

Trong applied math ta thường muốn viết

```math
\lim_n\int f_n=\int\lim_n f_n
```

hoặc

```math
\frac{d}{dx}\int f(x,t)dt
=\int\frac{\partial f}{\partial x}(x,t)dt.
```

Các operations này không tự động hợp lệ. Cần conditions như uniform convergence hoặc, trong measure lý thuyết (theory / 이론), dominated convergence conditions.

Phân tích (analysis / 분석) dạy một principle quan trọng: trước khi đổi thứ tự two limiting operations, phải hỏi theorem nào cho phép.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Interchanging limits, derivatives và integrals** đã nêu tiêu chí phân biệt, còn **Normed spaces và convergence không chỉ trong R** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normed spaces và convergence không chỉ trong R

Trong véc-tơ (vector / 벡터) không gian (space / 공간) có norm `||·||`, ta định nghĩa

```math
x_n\to x
```

nếu

```math
\|x_n-x\|\to0.
```

Điều này mở đường tới functional phân tích (analysis / 분석), tối ưu hóa (optimization / 최적화) và numerical tuyến tính (linear / 선형) algebra. Một thuật toán (algorithm / 알고리즘) có thể hội tụ theo Euclidean norm, operator norm hoặc hàm (function / 함수) norm tùy bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Normed spaces và convergence không chỉ trong R** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Real phân tích (analysis / 분석) là “hệ kiểu (type system / 타입 시스템)” cho các thao tác vô hạn. Nó buộc ta xác định lĩnh vực (domain / 도메인), notion of distance, convergence chế độ (mode / 모드) và các giả định (assumptions / 가정들) trước khi chuyển limits, derivatives hay integrals qua nhau. Calculus cho ta powerful operations; phân tích (analysis / 분석) cho biết operations đó hợp lệ ở đâu.

> **Chuyển mạch:** Ở chặng này của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

“Hội tụ” không chỉ có một loại. chuỗi (sequence / 시퀀스) numbers, chuỗi (sequence / 시퀀스) functions và random variables có nhiều notions of convergence khác nhau. Pointwise convergence cũng không đủ để bảo toàn mọi thuộc tính (property / 속성).

Một misconception khác là nghĩ epsilon-delta chỉ là formalism không thực dụng. Thực ra robust numerical bounds, stability, conditioning và lỗi (error / 오류) guarantees đều dựa trên cùng tư duy: đầu vào (input / 입력) perturbation bao nhiêu thì đầu ra (output / 출력) thay đổi bao nhiêu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Real phân tích (analysis / 분석): giới hạn, hội tụ và nền tảng chặt chẽ của calculus**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Chapter này làm nền chặt chẽ cho [Limits and continuity](./00_limits_and_continuity.md), [Infinite series](./07_infinite_series_power_series_and_convergence.md), [Numerical methods and error](../08_optimization_numerical/02_numerical_methods_and_error.md), [Optimization](../08_optimization_numerical/00_optimization.md) và xác suất (probability / 확률) lý thuyết (theory / 이론) ở mức sâu hơn.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
