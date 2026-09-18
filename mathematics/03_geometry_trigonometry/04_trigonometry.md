# Lượng giác: góc, tỷ số và dao động

Lượng giác (Trigonometry / 삼각함수) bắt đầu từ triangles nhưng phát triển thành ngôn ngữ của rotation, periodic motion, waves và frequency.

## Sine, cosine, tangent trong right triangle

Với angle `θ`:

```math
\sin\theta=\frac{opposite}{hypotenuse}
```

```math
\cos\theta=\frac{adjacent}{hypotenuse}
```

```math
\tan\theta=\frac{opposite}{adjacent}
=\frac{\sin\theta}{\cos\theta}
```

Các ratios chỉ phụ thuộc angle vì mọi right triangles có cùng acute angle là similar.

## Unit circle định nghĩa đầy đủ hơn

Right-triangle definition chỉ tiện cho acute angles. Unit circle radius 1 mở rộng tới mọi angle.

Point sau rotation `θ` có coordinates:

```math
(\cos\theta,\sin\theta)
```

Vì radius 1:

```math
\cos^2\theta+\sin^2\theta=1
```

đây là Pythagorean theorem trên unit circle.

## Radian

Radian (라디안) định nghĩa angle:

```math
\theta=\frac{s}{r}
```

với `s` arc length.

Full circle có circumference `2πr`, nên full angle:

```math
\theta=\frac{2\pi r}{r}=2\pi.
```

Radian dimensionless ratio và làm derivative formulas tự nhiên:

```math
\frac{d}{dx}\sin x=\cos x
```

chỉ đúng ở form sạch này khi `x` measured radians.

## Periodicity

Sine/cosine repeat mỗi `2π`:

```math
\sin(x+2\pi)=\sin x
```

```math
\cos(x+2\pi)=\cos x
```

Periodic functions phù hợp model cycles: rotating machinery, seasons, AC signals, sound waves.

## Amplitude, frequency, phase

General sinusoid:

```math
y=A\sin(\omega t+\phi)
```

`A` amplitude, `ω` angular frequency, `φ` phase.

Period:

```math
T=\frac{2\pi}{|\omega|}
```

Frequency cycles/time:

```math
f=\frac1T=\frac{|\omega|}{2\pi}.
```

Phase shift mô tả alignment trong cycle.

## Dot product và cosine

Vectors `u,v`:

```math
u\cdot v=\|u\|\|v\|\cos\theta.
```

Do đó cosine đo directional alignment. Cosine similarity trong information retrieval/embeddings dựa trên same geometry.

## Rotation matrix

2D rotation:

```math
\begin{bmatrix}
x'\\y'
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}
\begin{bmatrix}
x\\y
\end{bmatrix}
```

Matrix entries không arbitrary: chúng là coordinates của rotated basis vectors.

## Triangulation

Biết baseline và angles có thể suy distance tới inaccessible point. GPS, surveying và computer vision dùng richer geometry nhưng same principle: infer position từ angular/distance constraints.

## Mental Model

> Sine/cosine là coordinates của rotation trên unit circle. Triangle ratios, waves, rotation matrices và frequency signals là các views khác nhau của cùng circular geometry.

## Common Misconceptions

Trigonometry không chỉ cho triangles. Calculator degree/radian mode sai tạo kết quả sai dù formula đúng. `sin^{-1}` thường nghĩa arcsin chứ không phải reciprocal `1/sin`.
