# Phương trình và bất phương trình

Phương trình (Equation / 방정식) là một constraint: nó yêu cầu hai expression có cùng value. Giải phương trình không phải “tìm số bí mật” theo nghĩa hẹp; đó là tìm toàn bộ values trong domain làm constraint đúng.

## Solution set

Với

```math
2x+3=11
```

solution set là `{4}`. Với

```math
x^2=1
```

solution set là `{-1,1}` trên real numbers. Với

```math
x^2=-1
```

solution set rỗng trên `R` nhưng có `{-i,i}` trên complex numbers.

Vì vậy một equation không có “nghiệm tuyệt đối” nếu domain chưa xác định.

## Linear equation

Phương trình tuyến tính một biến có dạng

```math
ax+b=c
```

với `a≠0`. Ta isolate `x`:

```math
ax=c-b
```

```math
x=\frac{c-b}{a}
```

Tên “linear” phản ánh việc variable chỉ xuất hiện power 1 và graph tương ứng là đường thẳng.

## Systems of equations

Một hệ phương trình (System of equations / 연립방정식) yêu cầu nhiều constraints đồng thời đúng.

```math
\begin{cases}
x+y=10\\
x-y=2
\end{cases}
```

Cộng hai equation:

```math
2x=12\Rightarrow x=6
```

rồi `y=4`.

Hình học, mỗi linear equation hai variables là một line. Solving system là tìm intersection. Hai line có thể cắt một điểm, song song không cắt, hoặc trùng nhau có vô hạn intersections. Điều này tương ứng unique, no, hoặc infinitely many solutions.

Trong linear algebra, ý tưởng này được mở rộng bằng matrices và vector spaces.

## Quadratic equation

Phương trình bậc hai

```math
ax^2+bx+c=0,\qquad a\ne0
```

có thể giải bằng factorization, completing the square hoặc quadratic formula.

Để derive formula, chia cho `a`:

```math
x^2+\frac{b}{a}x+\frac{c}{a}=0
```

chuyển constant:

```math
x^2+\frac{b}{a}x=-\frac{c}{a}
```

thêm bình phương nửa coefficient của `x` vào hai vế:

```math
x^2+\frac{b}{a}x+\frac{b^2}{4a^2}
=\frac{b^2-4ac}{4a^2}
```

vế trái là

```math
\left(x+\frac{b}{2a}\right)^2
```

nên

```math
x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}
```

và

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
```

Discriminant

```math
\Delta=b^2-4ac
```

cho biết số real roots: `Δ>0` hai roots phân biệt, `Δ=0` root kép, `Δ<0` không có real roots.

## Equations với absolute value

Vì `|x|` là distance từ `x` đến 0,

```math
|x|=a
```

với `a>0` có hai nghiệm `x=a` và `x=-a`. General hơn:

```math
|x-c|=r
```

nghĩa distance từ `x` đến `c` bằng `r`, nên

```math
x=c\pm r
```

Cách hiểu distance giúp tránh học case-splitting máy móc.

## Inequality

Bất phương trình (Inequality / 부등식) mô tả order thay vì equality. Khi cộng cùng quantity vào hai vế, direction giữ nguyên. Nhưng khi nhân với số âm, direction đảo:

```math
2<5
```

nhân `-1`:

```math
-2>-5
```

Tại sao? Number line bị reflection qua 0; thứ tự trái-phải đảo ngược.

## Interval notation

Solution của inequality thường là interval. Ví dụ

```math
2x-1<5
```

cho

```math
x<3
```

viết interval:

```math
(-\infty,3)
```

Parenthesis nghĩa endpoint không được lấy; bracket nghĩa được lấy.

## Constraint trong optimization và engineering

Inequality là ngôn ngữ tự nhiên của constraints:

```math
CPU\_usage\le 80\%
```

```math
cost\le budget
```

```math
x_i\ge0
```

Trong linear programming, ta tối ưu objective dưới một system inequalities. Geometrically, mỗi inequality xác định một half-space; intersection của chúng tạo feasible region.

## Extraneous solutions

Khi transformation không reversible, có thể sinh nghiệm ngoại lai. Ví dụ

```math
\sqrt{x}=x-2
```

bình phương hai vế cho equation mới, nhưng mọi nghiệm của equation mới phải substitute lại original vì squaring mất thông tin về sign.

Đây là principle tổng quát: nếu transformation chỉ one-way implication thay vì equivalence, final candidates cần validation.

## Mental Model

> Equation là tập constraints bằng nhau; inequality là constraints về order. “Giải” nghĩa là biến đổi representation của constraints nhưng bảo toàn hoặc kiểm soát solution set cho đến khi các values hợp lệ trở nên rõ ràng.

## Common Misconceptions

Không phải equation nào cũng có một nghiệm. “Chuyển vế” không phải phép toán riêng. Bình phương hai vế có thể sinh nghiệm ngoại lai. Nhân inequality với số âm phải đảo chiều vì ordering trên number line bị reflection.
