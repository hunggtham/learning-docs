# Hợp hàm, hàm ngược và phép biến đổi hàm

Một hàm số (Function / 함수) mô tả một mapping từ input sang output. Khi các hệ thống thực tế gồm nhiều bước, ta hiếm khi chỉ có một mapping đơn lẻ. Ta có pipeline: input đi qua bước A, output của A trở thành input của B. Toán học của pipeline đó là hợp hàm (Function Composition / 함수의 합성).

## Composition là phép nối các transformations

Nếu

```math
g:X\to Y
```

và

```math
f:Y\to Z,
```

thì hợp hàm

```math
f\circ g:X\to Z
```

được định nghĩa bởi

```math
(f\circ g)(x)=f(g(x)).
```

Ví dụ

```math
g(x)=2x+1,
```

```math
f(u)=u^2.
```

Khi đó

```math
(f\circ g)(x)=(2x+1)^2.
```

Ta không nên coi `f(g(x))` là syntax trang trí. Nó diễn tả thứ tự xử lý. `g` chạy trước, `f` chạy sau.

Trong software, đây là function composition hoặc pipeline. Trong neural network, mỗi layer là một transformation và toàn network là composition của nhiều layers. Trong calculus, chain rule tồn tại chính vì change phải đi xuyên qua một composition.

## Composition thường không giao hoán

Thông thường

```math
f\circ g\neq g\circ f.
```

Với `f(x)=x^2` và `g(x)=x+1`:

```math
(f\circ g)(x)=(x+1)^2,
```

trong khi

```math
(g\circ f)(x)=x^2+1.
```

Kết quả khác nhau vì thứ tự transformation khác nhau. Cùng ý tưởng xuất hiện trong matrix multiplication, rotations 3D, database transformations và stateful workflows.

## Hàm ngược là undo một mapping

Hàm ngược (Inverse Function / 역함수) của `f` là function `f^{-1}` sao cho

```math
f^{-1}(f(x))=x
```

và, trên miền thích hợp,

```math
f(f^{-1}(y))=y.
```

Ví dụ

```math
f(x)=3x+5.
```

Đặt

```math
y=3x+5.
```

Giải `x` theo `y`:

```math
x=\frac{y-5}{3}.
```

Do đó

```math
f^{-1}(x)=\frac{x-5}{3}.
```

Hàm ngược không phải reciprocal. `f^{-1}(x)` không có nghĩa `1/f(x)`.

## Vì sao cần one-to-one?

Xét

```math
f(x)=x^2
```

trên toàn bộ real numbers. Cả `2` và `-2` đều map tới `4`. Nếu chỉ biết output là `4`, ta không thể biết input ban đầu là `2` hay `-2`. Mapping đã làm mất thông tin.

Để có inverse là một function, `f` phải injective, tức one-to-one trên domain đang xét. Ta có thể restrict domain của `x^2` thành `[0,\infty)`; khi đó inverse là

```math
f^{-1}(x)=\sqrt{x}.
```

Điều này liên hệ trực tiếp với data processing: operation mất thông tin thường không thể đảo ngược duy nhất. Hashing, rounding và compression mất dữ liệu là các ví dụ thực tế.

## Graph của inverse

Nếu `(a,b)` nằm trên graph của `y=f(x)`, thì `(b,a)` nằm trên graph của `y=f^{-1}(x)`. Vì vậy hai graphs đối xứng qua đường

```math
y=x.
```

Đây là hệ quả trực tiếp của việc hoán đổi role input và output.

## Biến đổi graph từ một function gốc

Nếu biết graph của `y=f(x)`, ta có thể hiểu nhiều graph mới mà không cần vẽ lại từ đầu.

Với

```math
y=f(x)+k,
```

toàn graph dịch lên `k` units. Với

```math
y=f(x-h),
```

graph dịch sang phải `h` units.

Điểm dễ nhầm là horizontal shift có dấu “ngược trực giác”. Muốn điểm cũ tại input `a` xuất hiện tại input mới `a+h`, ta cần argument bên trong thỏa

```math
x-h=a,
```

nên `x=a+h`.

Scaling cũng có hai loại. Với

```math
y=af(x),
```

output được scale theo vertical direction. Với

```math
y=f(bx),
```

input cần nhỏ đi `1/b` để argument bên trong đạt cùng value, nên graph bị horizontal compression khi `|b|>1`.

Nếu `a<0` hoặc `b<0`, ta có reflection qua trục `x` hoặc trục `y`.

## Symmetry của functions

Hàm chẵn (Even Function / 짝함수) thỏa

```math
f(-x)=f(x),
```

nên graph đối xứng qua trục `y`.

Hàm lẻ (Odd Function / 홀함수) thỏa

```math
f(-x)=-f(x),
```

nên graph đối xứng qua origin.

Symmetry giúp giảm computation. Trong integration, nếu integrand odd trên `[-a,a]`, integral bằng 0; nếu even, integral bằng hai lần integral trên `[0,a]`.

## Composition và dependency trong software

Một API pipeline có thể được model là

```text
raw input -> parser -> validator -> transformer -> serializer
```

Mỗi stage là một function-like transformation. Nếu một stage không injective, thông tin có thể mất và bước sau không thể reconstruct input. Nếu stage có side effects, model function thuần túy không còn đủ, nhưng composition vẫn là mental model hữu ích để phân tích data flow.

## Knowledge Connection

Composition tạo nền cho chain rule, matrix products, coordinate transformations và neural networks. Inverse nối với solving equations, inverse matrices và reversible computing. Function transformations nối algebra với signal processing: shift theo thời gian, scale amplitude và frequency đều có dạng biến đổi argument/output.

## Mental Model

> Hãy nghĩ function như một transformation box. Composition là nối nhiều boxes thành pipeline; inverse là một box có khả năng undo box trước; graph transformation là thay đổi coordinate frame hoặc scale của input/output mà không cần quên structure gốc.

## Common Misconceptions

`f^{-1}` không phải `1/f`. Không phải function nào cũng có inverse trên domain hiện tại. Composition không thường giao hoán. `f(x-h)` dịch phải chứ không phải trái vì transformation xảy ra bên trong input coordinate.

## Liên kết kiến thức

Chapter này giả định bạn đã nắm [Function Concept](./00_function_concept.md) và [Sets, Relations and Mappings](../00_foundations/02_sets_relations_and_mappings.md). Composition được dùng tiếp trong [Linear Transformations](../04_vectors_linear_algebra/02_linear_transformations.md) và [Derivatives](../05_calculus/01_derivatives.md), nơi chain rule chính là sensitivity của một composition.

Trong AI/Software, xem [Matrix Calculus, Jacobian, Hessian và Autodiff](../04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md) và [Math for AI, Data and Software](../09_connections/03_math_for_ai_data_and_software.md) để thấy computational graph, pipeline và information loss dưới cùng mental model.
