# Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa

Sine và cosine không phải hai functions độc lập ngẫu nhiên. Chúng là coordinates của một point quay trên unit circle. Khi hiểu chúng như geometry của rotation, nhiều identities trở thành consequences của matrix multiplication và angle addition thay vì một danh sách cần ghi nhớ.

## Pythagorean identity

Trên unit circle, point góc `θ` có coordinates

```math
(\cos\theta,\sin\theta).
```

Vì radius bằng 1:

```math
\cos^2\theta+\sin^2\theta=1.
```

Đây chỉ là Pythagorean theorem.

Chia cho `\cos^2\theta` khi `\cos\theta\neq0`:

```math
1+\tan^2\theta=\sec^2\theta.
```

Vì vậy identity tangent không phải formula riêng biệt; nó được derive từ unit-circle identity.

## Angle addition từ rotation

Rotation matrix:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Quay `\beta` rồi quay `\alpha` bằng quay `\alpha+\beta`:

```math
R(\alpha)R(\beta)=R(\alpha+\beta).
```

Nhân matrices rồi so entries cho:

```math
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-
\sin\alpha\sin\beta,
```

và

```math
\sin(\alpha+\beta)
=
\sin\alpha\cos\beta+
\cos\alpha\sin\beta.
```

Addition formulas vì vậy encode composition của rotations.

Đặt `\beta=-\alpha` hoặc chọn các angles thích hợp ta derive double-angle, subtraction và nhiều identities khác.

## Product-to-sum và sum-to-product

Từ angle addition/subtraction, có thể derive

```math
\cos A\cos B
=
\frac12[\cos(A-B)+\cos(A+B)].
```

Các identities này có ý nghĩa trong signal processing: product của sinusoids tạo frequency components ở sum và difference frequencies. Mixing/modulation trong communications sử dụng chính behavior này.

## Giải phương trình lượng giác

Xét

```math
\sin x=\frac12.
```

Trên một vòng unit circle, sine bằng `1/2` ở

```math
x=\frac\pi6,
\qquad
x=\frac{5\pi}{6}.
```

Nhưng sine periodic, nên full solution:

```math
x=\frac\pi6+2k\pi
```

hoặc

```math
x=\frac{5\pi}{6}+2k\pi,
\qquad k\in\mathbb Z.
```

Điểm quan trọng là inverse trig function thường chỉ trả một principal value. `arcsin(1/2)=\pi/6` không phải toàn bộ solution set của equation `sin x=1/2`.

## Amplitude, frequency, phase và offset

Một sinusoid tổng quát có dạng

```math
y=A\sin(\omega t+\phi)+C.
```

`A` là amplitude, `\omega` là angular frequency, `\phi` là phase và `C` là vertical offset.

Period là

```math
T=\frac{2\pi}{|\omega|}.
```

Nếu frequency thường `f` đo cycles per second, thì

```math
\omega=2\pi f.
```

Đây là lý do radians tự nhiên trong calculus và physics: một full cycle là `2\pi` radians, khiến derivative formulas không cần constant conversion phụ.

## Simple harmonic motion

Một hệ thỏa differential equation

```math
x''(t)+\omega^2x(t)=0
```

có solution dạng

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Đạo hàm hai lần của sine/cosine trả lại chính function với dấu âm, nên chúng là natural modes của oscillation.

Spring ideal, small-angle pendulum approximation, AC signals và nhiều wave systems đều dẫn tới sinusoidal behavior.

## Phasor và complex exponential

Euler formula

```math
e^{i\theta}=\cos\theta+i\sin\theta
```

cho phép encode amplitude và phase bằng complex numbers. Một oscillation có thể viết compact:

```math
Ae^{i(\omega t+\phi)}.
```

Real signal thường lấy real part. Representation này biến phase shifts thành multiplication, giúp circuit analysis, signal processing và Fourier theory đơn giản hơn đáng kể.

## Knowledge Connection

Trigonometric identities liên hệ trực tiếp với matrix rotations. Harmonic motion nối với differential equations. Complex exponential nối trig với complex numbers. Fourier analysis đi xa hơn: nhiều signals phức tạp có thể được phân rã thành tổng các sine/cosine ở nhiều frequencies.

## Mental Model

> `sin` và `cos` là shadow của chuyển động quay đều lên hai trục vuông góc. Identities phản ánh geometry của rotation; periodic equations phản ánh việc một góc có thể quay thêm nhiều vòng; harmonic motion phản ánh systems mà restoring force tạo ra rotation trong state space.

## Common Misconceptions

Degrees và radians không interchangeable trong calculus formulas. `arcsin(sin\theta)` không luôn bằng `\theta` vì inverse dùng principal branch. Identity khác equation: identity đúng cho mọi input hợp lệ. Phase shift không thay đổi frequency; nó chỉ thay vị trí của cycle theo thời gian.
