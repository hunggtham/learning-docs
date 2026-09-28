# Biểu thức hữu tỉ, miền xác định và tiệm cận

Biểu thức hữu tỉ (Rational Expression / 유리식) là thương của hai đa thức. Dạng tổng quát là

```math
R(x)=\frac{P(x)}{Q(x)},\qquad Q(x)\neq 0.
```

Điểm quan trọng không nằm ở việc “phân số có chữ”, mà ở chỗ phép chia tạo ra **điều kiện tồn tại**. Ngay khi một đại lượng xuất hiện ở mẫu, ta phải hỏi: tại những giá trị nào mẫu bằng 0? Những giá trị đó không còn thuộc miền xác định của biểu thức ban đầu.

## Miền xác định không phải chi tiết phụ

Xét

```math
f(x)=\frac{x^2-1}{x-1}.
```

Ta phân tích tử:

```math
x^2-1=(x-1)(x+1).
```

Với `x\neq1`, có thể rút gọn:

```math
f(x)=x+1.
```

Nhưng điều này không biến hàm ban đầu thành đúng hoàn toàn với `x=1`. Biểu thức gốc vẫn không xác định tại đó. Đồ thị (graph / 그래프) của `f` giống đường thẳng `y=x+1` nhưng có một lỗ tại `(1,2)`.

Đây là ví dụ điển hình cho việc **biểu thức đại số tương đương trên một miền** chứ không nhất thiết tương đương trên mọi giá trị. Khi biến đổi, ta phải mang theo lĩnh vực (domain / 도메인) như một phần của đối tượng (object / 객체) toán học.

Trong lập trình, cùng mô hình tư duy (mental model / 사고 모델) xuất hiện khi một hàm (function / 함수) có precondition. Một biểu thức có thể syntactically hợp lệ nhưng đầu vào (input / 입력) cụ thể làm thao tác (operation / 연산) trở nên undefined, chẳng hạn chia cho 0 hoặc truy cập phần tử ngoài phạm vi (range / 범위).

## Phương trình hữu tỉ

Xét

```math
\frac{1}{x-1}=\frac{2}{x+2}.
```

Trước hết lĩnh vực (domain / 도메인) yêu cầu

```math
x\neq1,\qquad x\neq-2.
```

Nhân hai vế với `(x-1)(x+2)`:

```math
x+2=2(x-1).
```

Suy ra

```math
x+2=2x-2
```

và

```math
x=4.
```

`x=4` không vi phạm lĩnh vực (domain / 도메인) nên là nghiệm hợp lệ.

Việc “nhân chéo” thực chất chỉ là nhân hai vế với một quantity chung. Phép biến đổi chỉ bảo toàn nghiệm khi quantity đó khác 0 trên các giá trị đang xét. Vì vậy lĩnh vực (domain / 도메인) phải được xác định trước, không phải kiểm tra tùy hứng sau cùng.

## Tiệm cận đứng

Nếu mẫu tiến về 0 còn tử không tiến về 0 cùng tốc độ, giá trị hàm có thể tăng không bị chặn. Với

```math
f(x)=\frac{1}{x-2},
```

khi `x\to2^+`, mẫu là một số dương rất nhỏ nên

```math
f(x)\to+\infty.
```

Khi `x\to2^-`, mẫu là số âm rất nhỏ nên

```math
f(x)\to-\infty.
```

Ta gọi `x=2` là tiệm cận đứng (Vertical Asymptote / 수직점근선).

Không phải mọi zero của mẫu đều tạo tiệm cận. Nếu factor tương ứng bị cancel với tử, ta có thể chỉ nhận được removable discontinuity, tức một lỗ như ví dụ `(x^2-1)/(x-1)`.

## Tiệm cận ngang và hành vi ở vô cực

Xét

```math
f(x)=\frac{2x+1}{x+3}.
```

Chia cả tử và mẫu cho `x`:

```math
f(x)=\frac{2+1/x}{1+3/x}.
```

Khi `|x|\to\infty`, các terms `1/x` và `3/x` tiến về 0, nên

```math
f(x)\to2.
```

Do đó `y=2` là tiệm cận ngang (Horizontal Asymptote / 수평점근선).

Đây không phải mẹo “so bậc” vô lý. Quy tắc so bậc chỉ là shortcut của việc factor ra power lớn nhất của `x` rồi quan sát các lower-order terms trở nên không đáng kể ở quy mô (scale / 규모) lớn.

Nếu bậc tử nhỏ hơn bậc mẫu, limit thường là 0. Nếu bằng nhau, limit là tỉ số hệ số leading. Nếu tử lớn hơn đúng một bậc, polynomial division thường dẫn đến tiệm cận xiên (Oblique Asymptote / 사선점근선).

## Partial fractions: biến một rational hàm (function / 함수) phức tạp thành các khối đơn giản

Một rational hàm (function / 함수) như

```math
\frac{3x+5}{(x-1)(x+2)}
```

có thể viết dưới dạng

```math
\frac{A}{x-1}+\frac{B}{x+2}.
```

Quy đồng:

```math
3x+5=A(x+2)+B(x-1).
```

So hệ số hoặc thay các giá trị thuận tiện giúp tìm `A,B`. Ý tưởng này quan trọng trong tích hợp (integration / 통합), differential equations, Laplace transforms và tín hiệu (signal / 신호) phân tích (analysis / 분석): ta phân rã một đối tượng (object / 객체) phức tạp thành các chế độ (mode / 모드) đơn giản hơn mà ta đã biết cách xử lý.

## Rational hàm (function / 함수) trong mô hình thực tế

Các tỉ lệ thường xuất hiện khi một tác động (effect / 효과) tăng lúc đầu nhưng bị giới hạn bởi sức chứa (capacity / 용량). Ví dụ một thông lượng (throughput / 처리량) mô hình (model / 모델) đơn giản có thể có dạng

```math
T(n)=\frac{an}{b+n}.
```

Khi `n` nhỏ, thông lượng (throughput / 처리량) gần tăng tuyến tính. Khi `n` rất lớn,

```math
T(n)\to a.
```

Nghĩa là hệ thống tiến tới một ceiling. Rational functions vì thế thường xuất hiện trong kinetics, saturation các mô hình (models / 모델들), điều khiển (control / 제어) các hệ thống (systems / 시스템들) và approximation.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Rational expressions nối đại số với calculus qua limits và asymptotes. Chúng nối với numerical computing qua lĩnh vực (domain / 도메인) checks và singularities. Trong ma trận (matrix / 행렬) computation, phép nghịch đảo cũng tạo singularity khi determinant bằng 0. Trong xác suất (probability / 확률), ratio xuất hiện trong odds và likelihood ratios. Cùng một mô hình tư duy (mental model / 사고 모델) lặp lại: **phép chia luôn yêu cầu denominator mang đủ thông tin để thao tác (operation / 연산) tồn tại**.

## Mô hình tư duy (mental model / 사고 모델)

> Một rational expression không chỉ là “phân số của hai đa thức”. Nó là một phép chia có cấu trúc, và vì thế lĩnh vực (domain / 도메인), singularity và hành vi ở quy mô (scale / 규모) lớn là một phần của bản chất. Mỗi lần rút gọn hay nhân chéo, hãy hỏi thao tác (operation / 연산) đó hợp lệ trên những đầu vào (input / 입력) nào.

## Dùng chung (common / 공통) Misconceptions

Rút gọn `(x-1)` không tự động thêm lại `x=1` vào lĩnh vực (domain / 도메인). Zero của denominator không phải lúc nào cũng là vertical asymptote; factor có thể cancel và tạo hole. Tiệm cận ngang không có nghĩa đồ thị (graph / 그래프) không bao giờ cắt đường tiệm cận. “So bậc” chỉ là hệ quả của limit, không phải quy tắc độc lập cần học thuộc.

## Liên kết kiến thức

Prerequisite gần nhất là [Phương trình và bất phương trình](./01_equations_and_inequalities.md), [Đa thức và phân tích nhân tử](./04_polynomials_and_factorization.md) và [Hàm số](../02_functions/00_function_concept.md). Khi chuyển sang hành vi (behavior / 동작) ở singularity và vô cực, đọc [Giới hạn và tính liên tục](../05_calculus/00_limits_and_continuity.md).

Partial fractions và pole-like hành vi (behavior / 동작) được dùng tiếp trong [Phương trình vi phân](../05_calculus/05_differential_equations.md), [Laplace/Z-transform và Dynamic Systems](../09_connections/06_laplace_z_transform_and_dynamic_systems.md), còn vấn đề singularity/conditioning nối trực tiếp với [Toán số](../08_optimization_numerical/02_numerical_methods_and_error.md).
