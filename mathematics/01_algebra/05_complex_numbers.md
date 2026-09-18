# Số phức: từ nghiệm phương trình đến rotation

Số phức (Complex number / 복소수) thường bị giới thiệu như cách “cho phép căn bậc hai của số âm”, nhưng vai trò của nó sâu hơn nhiều. Complex numbers biến rotation và oscillation thành algebra của multiplication.

## Định nghĩa

Một complex number có dạng

```math
z=a+bi
```

với `a,b∈R` và

```math
i^2=-1
```

`a` là real part, `b` là imaginary coefficient.

Hai complex numbers bằng nhau khi real parts và imaginary parts tương ứng bằng nhau.

## Complex plane

Ta biểu diễn `z=a+bi` như point `(a,b)` trên mặt phẳng. Horizontal axis là real axis, vertical axis là imaginary axis.

Magnitude/modulus:

```math
|z|=\sqrt{a^2+b^2}
```

chính là Euclidean distance từ origin.

Angle `θ` so với positive real axis gọi là argument.

## Addition và multiplication

Addition:

```math
(a+bi)+(c+di)=(a+c)+(b+d)i
```

là vector addition trên plane.

Multiplication:

```math
(a+bi)(c+di)=(ac-bd)+(ad+bc)i
```

Điều thú vị là multiplication không chỉ thay magnitude mà còn cộng angles.

## Polar form

Nếu `r=|z|` và angle `θ`, thì

```math
z=r(\cos\theta+i\sin\theta)
```

Euler formula cho

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

nên

```math
z=re^{i\theta}
```

Nếu

```math
z_1=r_1e^{i\theta_1},\qquad z_2=r_2e^{i\theta_2}
```

thì

```math
z_1z_2=r_1r_2e^{i(\theta_1+\theta_2)}
```

Multiplication nhân magnitudes và cộng angles. Đây là lý do complex number là representation cực gọn cho rotation.

## Nhân với i là quay 90°

Lấy `z=a+bi`:

```math
iz=ai+b i^2=-b+ai
```

point `(a,b)` biến thành `(-b,a)`, chính là rotation 90° counterclockwise.

Vì vậy `i` không chỉ là “imaginary”; multiplication by `i` là một transformation hình học cụ thể.

## Conjugate

Complex conjugate:

```math
\bar z=a-bi
```

Reflection qua real axis. Product:

```math
z\bar z=a^2+b^2=|z|^2
```

Điều này giúp division:

```math
\frac{1}{a+bi}=\frac{a-bi}{a^2+b^2}
```

với `z≠0`.

## Roots of unity

Solutions của

```math
z^n=1
```

là

```math
z_k=e^{2\pi i k/n},\qquad k=0,1,\ldots,n-1
```

chúng nằm đều trên unit circle. Cấu trúc này là nền của discrete Fourier transform và FFT.

## Signals và phasors

Một sinusoid

```math
A\cos(\omega t+\phi)
```

có thể được xử lý thông qua real part của

```math
Ae^{i(\omega t+\phi)}
```

Differentiation chỉ nhân thêm `iω`, khiến calculus của oscillations đơn giản hơn. Electrical engineering dùng phasors vì lý do này.

## Mental Model

> Complex number là một point/vector 2D được trang bị phép multiplication đặc biệt: multiplication vừa scale vừa rotate. Vì vậy nó là ngôn ngữ tự nhiên của periodicity, waves và frequency-domain computation.

## Common Misconceptions

“Imaginary” không có nghĩa vô nghĩa hoặc giả. Complex numbers có geometric interpretation rõ ràng. `i` không nằm “lớn hơn” hay “nhỏ hơn” real numbers theo total order tương thích với arithmetic. Magnitude `|z|` là real non-negative, không phải lấy absolute value từng component rồi cộng.

## Worked Example: giải phương trình bậc hai có nghiệm phức

Xét

```math
x^2-2x+5=0
```

Discriminant:

```math
\Delta=(-2)^2-4(1)(5)=4-20=-16
```

Quadratic formula cho

```math
x=\frac{2\pm\sqrt{-16}}{2}=1\pm2i
```

Hai roots là conjugates. Điều này không phải coincidence: polynomial có real coefficients, nên nếu `a+bi` là root thì conjugate `a-bi` cũng là root. Khi substitute conjugate, các real coefficients không thay đổi và complex conjugation commute với addition/multiplication.

Nhìn trên complex plane, roots `(1,2)` và `(1,-2)` phản xạ qua real axis. Representation hình học khiến “conjugate pair” trở thành một symmetry statement.

## Knowledge Connection: rotation matrix và complex multiplication

Matrix rotation 2D:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
```

apply lên vector `(x,y)`. Nếu encode point thành `z=x+iy`, multiply bằng `e^{i\theta}` tạo đúng coordinates rotated tương tự. Complex multiplication và rotation matrix là hai representations của cùng transformation.

Trong code xử lý 2D rotations, matrix form generalizes dễ tới affine pipelines, còn complex form có thể compact hơn nếu chỉ cần planar rotations/scales.
