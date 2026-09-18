# Hàm số: quy tắc biến input thành output

Hàm số (Function / 함수) là một trong những ideas trung tâm của toán học hiện đại. Nó cho phép ta tách câu hỏi “đối tượng nào đang được xử lý?” khỏi “quy tắc biến đổi là gì?”. Trong programming, một pure function gần với cùng mental model: mỗi input hợp lệ xác định một output.

## Domain, codomain và range

Ký hiệu

```math
f:A\to B
```

nói `f` nhận input từ domain `A` và output nằm trong codomain `B`.

Range/image là subset của `B` gồm những outputs thực sự đạt được.

Ví dụ

```math
f:\mathbb R\to\mathbb R,\qquad f(x)=x^2
```

có domain `R`, codomain `R`, nhưng range `[0,∞)`.

Nếu ta đổi codomain thành `[0,∞)`, cùng formula nhưng structural properties như surjectivity thay đổi.

## Function không nhất thiết có closed-form formula

Một lookup table, hash mapping, simulation, database query hay neural network đều có thể là function nếu mỗi input xác định đúng một output trong model deterministic. Formula chỉ là một representation.

## Graph

Graph của function một biến real là tập points

```math
\{(x,f(x))\mid x\in\text{domain}\}
```

Vertical line test đến từ definition: nếu một vertical line cắt graph hơn một point, cùng input `x` có nhiều outputs nên relation đó không phải function `y=f(x)`.

## Composition

Nếu

```math
g:A\to B,\qquad f:B\to C
```

thì composition

```math
(f\circ g)(x)=f(g(x))
```

là function từ `A` đến `C`.

Composition là nền của pipelines. Trong neural networks, mỗi layer là một transformation và whole network là composition của layers. Chain rule trong calculus chính là rule tính derivative của composition.

## Inverse function

Nếu `f` bijective, tồn tại inverse

```math
f^{-1}:B\to A
```

sao cho

```math
f^{-1}(f(x))=x
```

Inverse không phải reciprocal. `f^{-1}(x)` khác `1/f(x)`.

Ví dụ `f(x)=2x+3` có inverse:

```math
y=2x+3
```

swap roles rồi solve:

```math
x=2y+3\Rightarrow y=\frac{x-3}{2}
```

nên

```math
f^{-1}(x)=\frac{x-3}{2}
```

## One-to-one và monotonicity

Một function strictly increasing hoặc strictly decreasing trên interval là injective ở đó, nên có inverse trên range. `x^2` không injective trên toàn `R` vì `f(2)=f(-2)`. Nếu restrict domain `x≥0`, nó trở thành injective và inverse là `√x`.

Domain restriction đôi khi không phải technicality mà là bước tạo invertibility.

## Piecewise functions

Function có thể dùng different rules ở different regions:

```math
f(x)=
\begin{cases}
-x,&x<0\\
x,&x\ge0
\end{cases}
```

đây là `|x|`.

Piecewise models xuất hiện trong tax brackets, pricing tiers, ReLU activation và business rules.

## Parameters và families of functions

Trong

```math
f(x)=ax+b
```

`x` là variable input; `a,b` là parameters xác định một member trong family linear functions. Machine learning thường là quá trình chọn parameter values để function fit data tốt.

## Transformation of graphs

Nếu `y=f(x)`, thì

```math
f(x)+c
```

shift graph vertical `c`; `f(x-c)` shift right `c`; `af(x)` vertical scaling; `f(ax)` horizontal scaling inverse theo `a`.

Hiểu transformations giúp đọc model mà không cần plot từng function từ đầu.

## Mental Model

> Function là một machine có contract: input space, output space và rule mapping. Formula, graph, table và code chỉ là các representations khác nhau của cùng mapping.

## Common Misconceptions

Một function có thể nhiều input khác nhau cùng output; chỉ cấm một input có nhiều output. `f^{-1}` không phải reciprocal. Domain và codomain là một phần của function, không phải ghi chú phụ.
