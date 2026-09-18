# Mô hình tuyến tính và bậc hai

Hai families function xuất hiện rất sớm vì chúng capture hai patterns cơ bản: constant rate of change và rate of change thay đổi tuyến tính.

## Linear function

Dạng quen thuộc:

```math
y=mx+b
```

`m` là slope (기울기), `b` là y-intercept.

Slope giữa hai points:

```math
m=\frac{\Delta y}{\Delta x}
=\frac{y_2-y_1}{x_2-x_1}
```

Nó đo output thay đổi bao nhiêu trên một unit input. Unit của slope là unit-y chia unit-x.

Nếu `y` là cost KRW và `x` là GB storage, slope có unit KRW/GB. Đây là rate, không chỉ geometric angle.

## Affine vs linear theo linear algebra

Trong school algebra, `mx+b` thường gọi linear. Trong linear algebra nghiêm ngặt, transformation tuyến tính phải bảo toàn origin nên form một chiều là `y=mx`. `mx+b` với `b≠0` gọi affine transformation.

Sự khác biệt terminology này quan trọng khi đọc university textbook hoặc graphics documentation.

## Interpolation và extrapolation

Dùng line fit giữa observed points để estimate bên trong range là interpolation. Dự đoán ngoài range là extrapolation và rủi ro hơn vì assumption constant slope có thể không còn đúng.

Một salary trend 3 năm không đảm bảo tiếp tục linear 30 năm.

## Quadratic function

Dạng

```math
y=ax^2+bx+c,\qquad a\ne0
```

Graph là parabola. Derivative sau này cho

```math
y'=2ax+b
```

nên slope thay đổi tuyến tính theo `x`. Đây là lý do quadratic xuất hiện khi rate itself thay đổi constant.

Trong physics, constant acceleration `a` dẫn tới position

```math
x(t)=x_0+v_0t+\frac12at^2
```

vì velocity thay đổi linear theo time và position tích lũy velocity.

## Vertex form

Completing square biến

```math
y=ax^2+bx+c
```

thành

```math
y=a(x-h)^2+k
```

với vertex `(h,k)`.

Trong optimization một biến, nếu `a>0`, vertex là global minimum; nếu `a<0`, global maximum.

## Model fitting

Hai points xác định unique line nếu x-values khác nhau. Ba generic points xác định quadratic. Nhưng fitting data thực không chỉ là “đi qua mọi point”; với noisy data, exact interpolation có thể overfit. Least squares chọn parameters minimize tổng squared residuals.

## Residual

Nếu observed value là `y_i` và model prediction `\hat y_i`, residual:

```math
r_i=y_i-\hat y_i
```

Residual structure cho biết model bỏ sót pattern nào. Nếu residuals có curve rõ, linear model có thể quá đơn giản.

## Mental Model

> Linear model nói “mỗi bước input thêm cùng amount output”. Quadratic model nói “rate of change không còn constant, nhưng bản thân rate thay đổi đều”. Chọn model là chọn assumption về structure của change.

## Common Misconceptions

Linear correlation không chứng minh causal relationship. Một graph nhìn gần straight trong narrow range không có nghĩa underlying process thật sự linear. Quadratic formula giải roots, nhưng vertex form tốt hơn để hiểu extrema và geometry.

## Worked Example: tách fixed cost và variable cost

Giả sử một cloud service có fixed monthly cost 30,000 KRW và thêm 2,000 KRW cho mỗi 100 GB. Nếu đặt `x` là số block 100 GB, cost model:

```math
C(x)=2000x+30000
```

Slope 2,000 KRW/block nói marginal cost theo model; intercept 30,000 KRW là cost khi usage variable bằng zero. Nếu ta chỉ có hai observations và fit line, cần cẩn thận: intercept toán học có thể không có business meaning nếu `x=0` nằm ngoài range hoặc pricing có tiers.

## Worked Example: projectile model

Bỏ air resistance, vertical position:

```math
h(t)=h_0+v_0t-\frac12gt^2
```

đây là quadratic vì acceleration gravity constant `-g`. Vertex cho maximum height. Time của vertex:

```math
t_*=-\frac{b}{2a}=\frac{v_0}{g}
```

nếu viết coefficients theo standard quadratic. Đây là một ví dụ cho thấy vertex formula không phải trick đồ thị; nó encode thời điểm velocity vertical bằng zero.
