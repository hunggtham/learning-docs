# Mô hình tuyến tính và bậc hai: từ constant rate đến curvature

Linear và quadratic functions là hai families đầu tiên nên học thật sâu vì chúng tạo mental model cho phần lớn calculus sau này.

Linear model trả lời:

> Nếu input tăng một lượng cố định, output có thay đổi gần như cùng một lượng cố định không?

Quadratic model trả lời:

> Nếu bản thân rate of change đang thay đổi gần tuyến tính, shape của output sẽ ra sao?

Đây không chỉ là hai graph cần nhớ. Chúng là hai mức structure khác nhau của change.

## 1. Linear model bắt đầu từ constant rate of change

Một affine function một biến có dạng

```math
y=mx+b.
```

Trong school algebra thường gọi đây là linear function. Trong linear algebra nghiêm ngặt, `mx+b` với `b\ne0` là affine; linear map phải giữ origin và có dạng `y=mx`.

`m` là slope (기울기 / slope):

```math
m=\frac{\Delta y}{\Delta x}.
```

Điểm quan trọng không phải công thức mà là meaning:

```text
m = output change per input unit
```

Nếu `y` là KRW và `x` là GB:

```text
m unit = KRW/GB
```

Slope vì vậy là rate, không chỉ là “độ nghiêng của line”.

## 2. Vì sao constant slope tạo đường thẳng?

Nếu mọi increment `\Delta x` tạo cùng output increment

```math
\Delta y=m\Delta x,
```

thì bắt đầu từ reference point `(x_0,y_0)`:

```math
y-y_0=m(x-x_0).
```

Đó là point-slope equation.

Chọn `x_0=0`, đặt `b=y_0`:

```math
y=mx+b.
```

Vì vậy line equation không phải arbitrary syntax. Nó là consequence của assumption **constant rate of change**.

## 3. Intercept là baseline, nhưng chỉ khi baseline có meaning

Trong

```math
y=mx+b,
```

`b` là predicted output tại `x=0`.

Nhưng mathematical intercept không tự động có real-world meaning.

Ví dụ fit salary theo years of experience trên range 3–15 years. Intercept tại 0 years có thể là extrapolation ngoài data và không nên diễn giải mạnh.

Do đó khi đọc parameter:

```text
coefficient meaning = formula + domain + model assumptions
```

## 4. Worked example: fixed cost + variable cost

Cloud service:

```text
fixed fee = 30,000 KRW/month
variable fee = 20 KRW/GB
```

Model:

```math
C(x)=20x+30000.
```

Slope:

```text
20 KRW/GB
```

là marginal rate trong model.

Intercept:

```text
30,000 KRW
```

là baseline tại zero usage nếu pricing rule thực sự áp dụng ở zero.

Nếu pricing có tiers, function trở thành piecewise linear chứ không còn một line duy nhất.

## 5. Proportionality là special case của linear/affine behavior

Direct proportionality:

```math
y=kx
```

đi qua origin.

Nếu `x=0` thì `y=0`. Đây là stronger assumption so với affine model `mx+b`.

Ví dụ cost proportional với quantity chỉ hợp lý nếu không có fixed fee.

Rất nhiều lỗi modeling đến từ việc dùng proportionality khi thực tế có baseline.

## 6. Interpolation và extrapolation khác nhau về assumption risk

Interpolation dự đoán trong observed range.

Extrapolation dự đoán ngoài range.

Nếu data từ `x=10` đến `x=20`, prediction tại `x=15` dựa vào assumption local. Prediction tại `x=1000` yêu cầu assumption constant slope tồn tại xa ngoài evidence.

Một line có thể fit tốt trong narrow region của một nonlinear process.

Đây là bridge sang Taylor approximation: nonlinear functions thường gần linear locally dù global behavior khác hẳn.

## 7. Residual cho biết model bỏ sót structure nào

Observed value `y_i`, prediction `\hat y_i`:

```math
r_i=y_i-\hat y_i.
```

Nếu residuals random quanh zero, line có thể capture mean structure khá tốt.

Nếu residuals tạo curve:

```text
positive → negative → positive
```

đó là dấu hiệu linear model đang bỏ sót curvature.

Residual không chỉ là “error cần nhỏ”; pattern của residual là diagnostic signal.

## 8. Quadratic model xuất hiện khi first-order rate không constant

Quadratic function:

```math
y=ax^2+bx+c,
\qquad a\ne0.
```

Derivative:

```math
y'=2ax+b.
```

Slope thay đổi tuyến tính theo `x`.

Second derivative:

```math
y''=2a
```

constant.

Vì vậy một mental model rất mạnh là:

```text
linear function       → constant first derivative
quadratic function    → constant second derivative
```

Đây là lý do quadratic xuất hiện trong constant acceleration, local curvature và second-order optimization.

## 9. Physics derivation: constant acceleration tạo quadratic position

Nếu acceleration constant `a`:

```math
v(t)=v_0+at.
```

Position accumulation:

```math
x(t)=x_0+\int_0^t v(s)\,ds
```

nên

```math
x(t)=x_0+v_0t+\frac12at^2.
```

Quadratic không xuất hiện vì “projectile formula phải nhớ”. Nó xuất hiện vì tích phân của linear velocity là quadratic position.

## 10. Ba representations của quadratic trả lời ba câu hỏi khác nhau

Expanded form:

```math
f(x)=ax^2+bx+c
```

làm coefficients rõ.

Factored form:

```math
f(x)=a(x-r_1)(x-r_2)
```

làm roots rõ.

Vertex form:

```math
f(x)=a(x-h)^2+k
```

làm extremum và symmetry rõ.

Không có representation “tốt nhất” universal. Good algebra thường là chọn representation phù hợp question.

## 11. Completing the square là đổi representation, không phải trick

Từ

```math
ax^2+bx+c,
```

factor `a` khỏi quadratic terms:

```math
=a\left(x^2+\frac ba x\right)+c.
```

Thêm/bớt square:

```math
x^2+\frac ba x
=
\left(x+\frac{b}{2a}\right)^2
-
\frac{b^2}{4a^2}.
```

Do đó

```math
f(x)=
a\left(x+\frac{b}{2a}\right)^2
+
\left(c-\frac{b^2}{4a}\right).
```

Vertex:

```math
h=-\frac{b}{2a}.
```

Điểm này cũng là nơi derivative bằng zero:

```math
2ax+b=0.
```

Algebra và calculus đang nói cùng một structure bằng hai ngôn ngữ.

## 12. Discriminant encode root geometry

Quadratic equation:

```math
ax^2+bx+c=0.
```

Discriminant:

```math
\Delta=b^2-4ac.
```

Nếu `\Delta>0`: hai real roots.

Nếu `\Delta=0`: tangent touch, repeated root.

Nếu `\Delta<0`: no real roots, nhưng có complex conjugate roots.

Discriminant vì vậy không chỉ là symbol trong formula; nó tóm tắt intersection geometry của parabola với x-axis.

## 13. Quadratic as local approximation

Gần `x_0`, smooth function có Taylor approximation:

```math
f(x_0+h)
\approx
f(x_0)
+f'(x_0)h
+\frac12f''(x_0)h^2.
```

Linear term mô tả slope; quadratic term mô tả curvature.

Optimization methods như Newton's method và second-order models dùng đúng viewpoint này.

Một quadratic model không chỉ là school function family; nó là universal local model cấp hai cho smooth functions.

## 14. Multivariable quadratic form

Trong nhiều dimensions, quadratic structure viết:

```math
q(x)=x^TAx+b^Tx+c.
```

Matrix `A` encode curvature.

Nếu `A` positive definite, bowl shape có unique minimum.

Đây là bridge sang Hessian, least squares, optimization và Gaussian models.

## 15. Linear regression vs exact line through points

Hai points với different x xác định một exact line.

Nhưng noisy data nhiều points thường không nằm trên một line. Khi đó regression solve:

```math
\min_{m,b}
\sum_i
(y_i-(mx_i+b))^2.
```

Đây là projection problem, không phải interpolation.

Distinction:

```text
interpolation → pass through selected data exactly
regression → estimate underlying relationship under noise
```

## 16. Quadratic fitting và overfitting intuition

Thêm degree cho polynomial làm model flexible hơn. Training residual có thể giảm, nhưng generalization không chắc tốt hơn.

Với few noisy samples, quadratic có thể fit apparent curvature chỉ do noise.

Model choice cần:

```text
structure + data + validation
```

không chỉ “higher degree fits better”.

## 17. Worked example: braking distance

Nếu reaction distance scale roughly linear với speed `v`:

```math
d_r\propto v,
```

còn braking distance dưới simplified constant deceleration model scale như

```math
d_b\propto v^2,
```

thì total stopping distance có form gần

```math
d(v)=av+bv^2.
```

Doubling speed không chỉ double stopping distance vì quadratic term tăng factor 4.

Đây là example tốt cho việc hiểu model terms bằng scaling.

## 18. Finance connection: local linear vs convex exposure

Một portfolio value có thể local approximate theo price change:

```math
\Delta V\approx \Delta\,\Delta S
```

(first-order sensitivity).

Với nonlinear instruments, second-order term:

```math
\Delta V
\approx
\Delta\,\Delta S
+
\frac12\Gamma(\Delta S)^2
```

cho curvature exposure.

Không cần học option pricing ở chapter này; important connection là linear + quadratic terms tạo local sensitivity model.

## 19. AI connection: linear layer nhưng nonlinear model

Một layer thường viết:

```math
z=Wx+b.
```

đây là affine transformation.

Nếu chỉ compose affine layers mà không activation nonlinear, toàn network vẫn collapse thành một affine transformation.

Nonlinearity là thứ tạo richer function family.

Điều này cho thấy linear model là building block nhưng không đủ cho arbitrary nonlinear structure.

## 20. Assumptions checklist

Khi dùng linear model, hỏi:

```text
rate có thực sự gần constant không?
intercept có meaning không?
range nào model valid?
residual có pattern không?
extrapolation có hợp lý không?
```

Khi dùng quadratic model, hỏi thêm:

```text
curvature có gần constant không?
quadratic behavior là global hay chỉ local?
vertex/root có nằm trong domain meaningful không?
```

## Knowledge Connection

Linear/quadratic models nối:

```text
ratio/rate
→ functions
→ derivatives
→ Taylor approximation
→ least squares
→ optimization
→ physics motion
→ AI affine layers
→ Finance sensitivity
```

## Mental Model

> Linear model là **constant first-order change**. Quadratic model là **constant second-order change** hoặc **first-order rate thay đổi tuyến tính**. Đừng bắt đầu từ graph shape; bắt đầu từ structure của change mà model đang giả định.

## Common Misconceptions

`y=mx+b` không phải linear map theo definition linear algebra nếu `b\ne0`. High `R^2` không chứng minh relationship truly linear hoặc causal. Vertex formula không phải mẹo; nó là nơi first derivative bằng zero. Quadratic fit tốt trong sample không có nghĩa process thật sự quadratic ngoài range. Một graph nhìn thẳng trên narrow interval có thể chỉ là local linearization của nonlinear function.