# Phương trình và bất phương trình: constraint, equivalence và miền nghiệm

Phương trình (equation / 방정식) và bất phương trình (inequality / 부등식) đều là cách biểu diễn **ràng buộc** lên những giá trị có thể xảy ra. Khi viết

```math
2x+3=11
```

điều quan trọng không phải là ký hiệu `=` tự nó, mà là statement: ta chỉ chấp nhận những `x` làm hai biểu thức đại diện cho cùng một giá trị.

Với bất phương trình

```math
2x+3\le 11,
```

constraint yếu hơn: ta chấp nhận cả một vùng giá trị thay vì chỉ các điểm làm hai vế bằng nhau.

Vì vậy, tư duy đúng không phải là “chuyển vế cho nhanh”, mà là:

> Ta đang biến đổi representation của cùng một solution set. Mỗi bước cần biết nó có bảo toàn nghiệm hai chiều hay chỉ tạo ra candidate cần kiểm tra lại.

## 1. Solution set luôn phụ thuộc domain

Một phương trình không có solution set hoàn toàn tách khỏi domain.

Ví dụ

```math
x^2=2
```

không có nghiệm trong rational numbers `\mathbb Q`, nhưng có hai nghiệm trong real numbers `\mathbb R`:

```math
x=\pm\sqrt2.
```

Tương tự,

```math
x^2=-1
```

không có nghiệm thực nhưng có nghiệm phức:

```math
x=\pm i.
```

Điều này nối trực tiếp equations với number systems: mở rộng tập số thường xuất hiện vì một class equations trước đó chưa “đóng” dưới phép giải.

## 2. Equivalence transformations: vì sao các phép biến đổi hợp lệ?

Giả sử

```math
A(x)=B(x).
```

Nếu ta cộng cùng một expression `C(x)` vào hai vế, ta được

```math
A(x)+C(x)=B(x)+C(x).
```

Phép biến đổi này reversible: trừ lại `C(x)` sẽ quay về equation ban đầu. Vì thế hai equations có cùng solution set.

Tương tự, nhân hai vế với một nonzero constant `k` cũng reversible:

```math
A=B
\iff
kA=kB,\qquad k\ne0.
```

Đây là bản chất của những câu quen thuộc như “chuyển vế đổi dấu”: không có operation đặc biệt tên là chuyển vế; ta chỉ đang cộng hoặc trừ cùng quantity ở hai phía.

### Khi phép biến đổi không reversible

Nếu từ

```math
x=1
```

bình phương hai vế, ta được

```math
x^2=1,
```

nhưng equation mới có thêm nghiệm `x=-1`. Vì squaring là many-to-one trên real numbers: `1` và `-1` cùng map tới `1`.

Do đó

```math
A=B \Rightarrow A^2=B^2
```

nhưng chiều ngược lại không luôn đúng.

Đây là lý do equations có square root, absolute value, rational expressions hoặc trigonometric transformations thường cần **substitute back** vào original constraint.

## 3. Linear equations: solving là undo một affine transformation

Phương trình

```math
ax+b=c,\qquad a\ne0
```

có thể hiểu như một function

```math
f(x)=ax+b
```

và câu hỏi là tìm preimage của `c` dưới `f`.

Ta undo translation trước:

```math
ax=c-b,
```

rồi undo scaling:

```math
x=\frac{c-b}{a}.
```

Cách nhìn này nối equations với inverse functions. Solving linear equation là áp dụng inverse của affine map.

### Worked example

Giải

```math
3(2x-1)+4=19.
```

Khai triển không phải lúc nào cũng là bước đầu bắt buộc, nhưng ở đây giúp thấy structure:

```math
6x-3+4=19
```

```math
6x+1=19
```

```math
6x=18
```

```math
x=3.
```

Mỗi bước đều equivalence-preserving.

## 4. Hệ phương trình: intersection của constraints

System

```math
\begin{cases}
x+y=10\\
x-y=2
\end{cases}
```

không phải hai bài riêng. Solution phải thỏa **cả hai** constraints.

Cộng equations:

```math
2x=12
```

nên

```math
x=6,
```

rồi

```math
y=4.
```

Geometrically, mỗi equation trong hai variables là một line; solution là intersection. Hai lines có thể:

- cắt nhau tại một điểm → unique solution;
- song song → no solution;
- trùng nhau → infinitely many solutions.

Linear algebra tổng quát hóa cùng idea này thành

```math
Ax=b.
```

Rank, column space và null space sau này chỉ là ngôn ngữ có hệ thống hơn để mô tả consistency và degrees of freedom.

## 5. Quadratic equations: vì sao có nhiều representations?

Quadratic

```math
ax^2+bx+c=0,\qquad a\ne0
```

có thể được viết ở nhiều forms vì mỗi representation làm lộ một structure khác.

Expanded form:

```math
ax^2+bx+c
```

làm coefficients rõ.

Factored form:

```math
a(x-r_1)(x-r_2)
```

làm roots rõ.

Vertex form:

```math
a(x-h)^2+k
```

làm geometry rõ.

### Derive quadratic formula từ completing the square

Bắt đầu:

```math
ax^2+bx+c=0.
```

Chia cho `a`:

```math
x^2+\frac ba x+\frac ca=0.
```

Chuyển constant:

```math
x^2+\frac ba x=-\frac ca.
```

Thêm bình phương nửa coefficient của `x` vào hai phía:

```math
x^2+\frac ba x+\frac{b^2}{4a^2}
=
\frac{b^2-4ac}{4a^2}.
```

Vế trái trở thành perfect square:

```math
\left(x+\frac{b}{2a}\right)^2
=
\frac{b^2-4ac}{4a^2}.
```

Lấy square root:

```math
x+\frac{b}{2a}
=
\pm\frac{\sqrt{b^2-4ac}}{2a},
```

nên

```math
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
```

Quadratic formula không phải rule rơi từ trên xuống; nó là completing-the-square được đóng gói.

## 6. Discriminant là thông tin hình học

```math
\Delta=b^2-4ac
```

quyết định số real intersections giữa parabola và x-axis.

- `\Delta>0`: hai real roots;
- `\Delta=0`: tangent vào trục, một root kép;
- `\Delta<0`: không cắt x-axis trong real plane.

Trong complex numbers, vẫn có hai roots tính theo multiplicity.

Discriminant vì vậy nối algebra với geometry và complex number systems.

## 7. Absolute value: distance trước case splitting

Absolute value nên được hiểu trước hết là distance.

```math
|x-c|=r
```

nghĩa distance từ `x` tới `c` bằng `r`. Nếu `r>0`, có hai points:

```math
x=c-r
```

và

```math
x=c+r.
```

Còn

```math
|x-c|<r
```

nghĩa `x` nằm **bên trong** interval bán kính `r` quanh `c`:

```math
c-r<x<c+r.
```

Trong khi

```math
|x-c|>r
```

nghĩa nằm bên ngoài interval đó.

Cách hiểu distance làm absolute-value inequalities trở nên tự nhiên hơn việc học thuộc cases.

## 8. Rational equations và domain restrictions

Ví dụ

```math
\frac{1}{x-1}=2.
```

Trước khi solve phải ghi nhận

```math
x\ne1.
```

Nhân hai phía bởi `x-1` chỉ hợp lệ trên domain nơi denominator khác zero:

```math
1=2(x-1)
```

```math
x=\frac32.
```

Candidate này hợp lệ vì không vi phạm restriction.

Trong rational equations, domain restriction không phải ghi chú phụ; nó là part of the problem definition.

## 9. Inequalities: order structure khác equality ở đâu?

Nếu

```math
a<b,
```

thêm cùng `c` vào hai phía giữ order:

```math
a+c<b+c.
```

Nhân với positive `k` cũng giữ order. Nhưng nếu `k<0`, direction đảo:

```math
ka>kb.
```

Tại sao? Multiplication by a negative number phản chiếu number line qua 0. Reflection đổi left ↔ right, nên thứ tự đảo.

### Worked example

Giải

```math
-3x+5\le14.
```

Trừ 5:

```math
-3x\le9.
```

Chia cho `-3`, đảo inequality:

```math
x\ge-3.
```

Solution set:

```math
[-3,\infty).
```

## 10. Polynomial inequalities: sign chart đến từ factors

Giải

```math
(x-1)(x+2)>0.
```

Critical points là roots `-2` và `1`. Chúng chia number line thành ba intervals:

```text
(-∞,-2), (-2,1), (1,∞)
```

Product positive khi hai factors cùng sign. Do đó solution là

```math
(-\infty,-2)\cup(1,\infty).
```

Sign chart không phải trick riêng; nó là reasoning từ multiplicative signs và roots.

## 11. Constraints trong optimization, physics và software

Inequalities là language của feasible regions:

```math
x_i\ge0,
```

```math
cost(x)\le budget,
```

```math
latency\le200\text{ ms}.
```

Trong linear programming, mỗi linear inequality tạo một half-space. Intersection của các half-spaces là feasible set.

Trong physics, constraints có thể đến từ conservation laws hoặc physical bounds. Trong software, validation rules cũng là predicates xác định allowed state.

Điểm chung là: equations/inequalities không chỉ là bài solve `x`; chúng là ngôn ngữ mô tả **state nào được phép tồn tại**.

## 12. Proof idea: vì sao solution-preserving transformations quan trọng?

Khi solving, ta muốn xây chain

```math
E_0\iff E_1\iff E_2\iff\cdots\iff E_k.
```

Nếu mỗi arrow là equivalence, mọi stage có cùng solution set.

Nếu một bước chỉ có

```math
E_i\Rightarrow E_{i+1},
```

thì `E_{i+1}` có thể có extra solutions. Khi đó final answers chỉ là candidates và phải check lại original equation.

Đây là proof-theoretic viewpoint của algebraic manipulation: mỗi step cần biết logical strength của transformation.

## Applications và connections

**Computer Science:** constraint solvers, type constraints, SAT/SMT reasoning và validation systems đều mở rộng idea “tìm assignments làm predicates đúng”.

**Physics:** equations of motion và conservation equations xác định states/trajectories hợp lệ.

**AI:** optimization training là solve inequalities/equalities gián tiếp qua objectives và constraints.

**Finance:** budget, leverage, regulatory capital và no-arbitrage relationships đều được viết dưới dạng equations/inequalities.

## Mental Model

> Equation và inequality là descriptions của feasible states. Solving là thay representation của constraint bằng representations dễ đọc hơn trong khi theo dõi chính xác solution set. Algebra tốt không phải thao tác ký hiệu nhanh; nó là logic-preserving transformation.

## Common Misconceptions

**“Chuyển vế” là một phép toán đặc biệt.** Không; đó là shorthand cho cộng/trừ cùng quantity ở hai phía.

**Bình phương hai vế luôn equivalent.** Không; squaring có thể mất sign information và tạo extraneous solutions.

**Một equation có nghiệm mà không cần domain.** Không; solution set phụ thuộc number system và restrictions.

**`f'(x)=0` hay `\Delta=0` tự nó là một mẹo riêng.** Những conditions này đều encode geometry/structure cụ thể; hiểu structure giúp tránh học thuộc rời rạc.
