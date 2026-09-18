# Hàm mũ và logarithmic models

Hàm mũ (Exponential function / 지수함수) mô tả processes nơi change tỷ lệ với current amount hoặc nơi cùng multiplicative factor được lặp. Hàm logarithm (Logarithmic function / 로그함수) là inverse của exponential và đo multiplicative depth.

## Discrete exponential growth

Nếu mỗi period quantity nhân với `r`, recurrence là

```math
A_{n+1}=rA_n
```

Repeated substitution cho

```math
A_n=A_0r^n
```

Nếu `r>1`, growth; `0<r<1`, decay.

Half-life model có factor `1/2` sau mỗi half-life `H`:

```math
A(t)=A_0\left(\frac12\right)^{t/H}
```

## Continuous growth

Khi instantaneous rate proportional to amount:

```math
\frac{dA}{dt}=kA
```

solution:

```math
A(t)=A_0e^{kt}
```

Positive `k` growth, negative `k` decay. Exponential không được chọn vì “fit đẹp”; nó là function tự tái tạo dưới differentiation.

## Doubling time

Nếu

```math
A(t)=A_0e^{kt}
```

muốn `A(T)=2A_0`:

```math
e^{kT}=2
```

lấy ln:

```math
kT=\ln2
```

nên

```math
T=\frac{\ln2}{k}
```

Logarithm xuất hiện vì ta đang solve exponent.

## Compound interest

Với principal `P`, periodic rate `r`, `n` periods:

```math
A=P(1+r)^n
```

Nếu compounding `m` lần mỗi year với annual nominal rate `r`:

```math
A=P\left(1+\frac rm\right)^{mt}
```

Khi `m→∞`, limit dẫn tới

```math
A=Pe^{rt}
```

continuous compounding.

## Logistic growth

Pure exponential giả định resource vô hạn. Khi capacity giới hạn, logistic model:

```math
\frac{dP}{dt}=rP\left(1-\frac PK\right)
```

Khi `P` nhỏ so với carrying capacity `K`, factor gần 1 nên gần exponential. Khi `P` gần `K`, growth rate giảm. Đây là ví dụ cách thêm constraint vào first-principles model thay vì dùng exponential ngoài phạm vi hợp lý.

## Logarithmic perception và scales

Nếu quantities trải nhiều orders of magnitude, log compresses scale. Trên log axis, equal distances đại diện equal ratios. Vì vậy exponential curve trên semi-log plot có thể trở thành straight line:

```math
A=A_0e^{kt}
```

lấy log:

```math
\ln A=\ln A_0+kt.
```

Đây từng là technique quan trọng để detect exponential pattern, dù modern fitting nên account noise model thay vì chỉ transform blindly.

## Mental Model

> Exponential là model của “amount hiện tại quyết định amount change” hoặc repeated multiplication. Logarithm mở ngược quá trình đó để hỏi time/number of multiplicative steps.

## Common Misconceptions

Exponential growth không thể tiếp tục mãi trong bounded physical systems. “Tăng 5% mỗi năm” là multiplicative, không phải cộng cùng absolute amount mỗi năm. Log-transform có thể thay đổi error structure; fit line sau transform không luôn equivalent với fitting original data.
