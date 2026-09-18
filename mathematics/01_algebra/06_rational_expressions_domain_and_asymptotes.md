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

Nhưng điều này không biến hàm ban đầu thành đúng hoàn toàn với `x=1`. Biểu thức gốc vẫn không xác định tại đó. Graph của `f` giống đường thẳng `y=x+1` nhưng có một lỗ tại `(1,2)`.

Đây là ví dụ điển hình cho việc **biểu thức đại số tương đương trên một miền** chứ không nhất thiết tương đương trên mọi giá trị. Khi biến đổi, ta phải mang theo domain như một phần của object toán học.

Trong lập trình, cùng mental model xuất hiện khi một function có precondition. Một biểu thức có thể syntactically hợp lệ nhưng input cụ thể làm operation trở nên undefined, chẳng hạn chia cho 0 hoặc truy cập phần tử ngoài range.

## Phương trình hữu tỉ

Xét

```math
\frac{1}{x-1}=\frac{2}{x+2}.
```

Trước hết domain yêu cầu

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

`x=4` không vi phạm domain nên là nghiệm hợp lệ.

Việc “nhân chéo” thực chất chỉ là nhân hai vế với một quantity chung. Phép biến đổi chỉ bảo toàn nghiệm khi quantity đó khác 0 trên các giá trị đang xét. Vì vậy domain phải được xác định trước, không phải kiểm tra tùy hứng sau cùng.

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

Đây không phải mẹo “so bậc” vô lý. Quy tắc so bậc chỉ là shortcut của việc factor ra power lớn nhất của `x` rồi quan sát các lower-order terms trở nên không đáng kể ở scale lớn.

Nếu bậc tử nhỏ hơn bậc mẫu, limit thường là 0. Nếu bằng nhau, limit là tỉ số hệ số leading. Nếu tử lớn hơn đúng một bậc, polynomial division thường dẫn đến tiệm cận xiên (Oblique Asymptote / 사선점근선).

## Partial fractions: biến một rational function phức tạp thành các khối đơn giản

Một rational function như

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

So hệ số hoặc thay các giá trị thuận tiện giúp tìm `A,B`. Ý tưởng này quan trọng trong integration, differential equations, Laplace transforms và signal analysis: ta phân rã một object phức tạp thành các mode đơn giản hơn mà ta đã biết cách xử lý.

## Rational function trong mô hình thực tế

Các tỉ lệ thường xuất hiện khi một effect tăng lúc đầu nhưng bị giới hạn bởi capacity. Ví dụ một throughput model đơn giản có thể có dạng

```math
T(n)=\frac{an}{b+n}.
```

Khi `n` nhỏ, throughput gần tăng tuyến tính. Khi `n` rất lớn,

```math
T(n)\to a.
```

Nghĩa là hệ thống tiến tới một ceiling. Rational functions vì thế thường xuất hiện trong kinetics, saturation models, control systems và approximation.

## Knowledge Connection

Rational expressions nối đại số với calculus qua limits và asymptotes. Chúng nối với numerical computing qua domain checks và singularities. Trong matrix computation, phép nghịch đảo cũng tạo singularity khi determinant bằng 0. Trong probability, ratio xuất hiện trong odds và likelihood ratios. Cùng một mental model lặp lại: **phép chia luôn yêu cầu denominator mang đủ thông tin để operation tồn tại**.

## Mental Model

> Một rational expression không chỉ là “phân số của hai đa thức”. Nó là một phép chia có cấu trúc, và vì thế domain, singularity và hành vi ở scale lớn là một phần của bản chất. Mỗi lần rút gọn hay nhân chéo, hãy hỏi operation đó hợp lệ trên những input nào.

## Common Misconceptions

Rút gọn `(x-1)` không tự động thêm lại `x=1` vào domain. Zero của denominator không phải lúc nào cũng là vertical asymptote; factor có thể cancel và tạo hole. Tiệm cận ngang không có nghĩa graph không bao giờ cắt đường tiệm cận. “So bậc” chỉ là hệ quả của limit, không phải quy tắc độc lập cần học thuộc.
