# Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa

Sine và cosine nên được hiểu trước hết như **coordinates của rotation**, không phải hai functions rời rạc cần nhớ bảng công thức. Khi một point quay trên unit circle, `cos` là projection lên trục x và `sin` là projection lên trục y.

Từ viewpoint đó, identities, periodic equations, phasor, harmonics và Fourier analysis đều là các cách khác nhau để mô tả cùng một structure: **rotation lặp lại theo thời gian hoặc angle**.

## 1. Unit circle là nguồn của identities cơ bản

Point ở angle `\theta` trên unit circle:

```math
(\cos\theta,\sin\theta).
```

Vì radius bằng 1:

```math
\cos^2\theta+\sin^2\theta=1.
```

Đây chính là Pythagorean theorem.

Chia cho `\cos^2\theta` khi `\cos\theta\ne0`:

```math
1+\tan^2\theta=\sec^2\theta.
```

Chia cho `\sin^2\theta` khi `\sin\theta\ne0`:

```math
\csc^2\theta=1+\cot^2\theta.
```

Vì vậy các identities này không phải formulas độc lập; chúng cùng xuất phát từ geometry của unit circle.

## 2. Angle addition là composition của rotations

Rotation matrix:

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Quay `\beta` rồi quay `\alpha` tương đương quay `\alpha+\beta`:

```math
R(\alpha)R(\beta)=R(\alpha+\beta).
```

So các entries ta được:

```math
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-
\sin\alpha\sin\beta,
```

```math
\sin(\alpha+\beta)
=
\sin\alpha\cos\beta+
\cos\alpha\sin\beta.
```

Đây là proof idea quan trọng: addition formula encode group law của rotations.

## 3. Double-angle, half-angle và identities khác

Đặt `\beta=\alpha`:

```math
\sin 2\alpha=2\sin\alpha\cos\alpha,
```

```math
\cos 2\alpha
=
\cos^2\alpha-\sin^2\alpha.
```

Kết hợp với

```math
\sin^2\alpha+\cos^2\alpha=1
```

cho:

```math
\cos 2\alpha=1-2\sin^2\alpha
```

và

```math
\cos 2\alpha=2\cos^2\alpha-1.
```

Từ đây suy ra half-angle identities. Lesson quan trọng là không cần nhớ mọi identity như một item riêng; chỉ cần biết một vài generators và derive khi cần.

## 4. Product-to-sum: vì sao multiplication tạo frequencies mới?

Từ angle addition/subtraction:

```math
\cos A\cos B
=
\frac12[\cos(A-B)+\cos(A+B)].
```

Tương tự:

```math
\sin A\sin B
=
\frac12[\cos(A-B)-\cos(A+B)].
```

Một product của hai oscillations tạo components ở **sum frequency** và **difference frequency**.

Đây không chỉ là algebra. Nó là nền của mixing, modulation, heterodyning trong communications và signal processing.

## 5. Identity khác equation

Identity:

```math
\sin^2x+\cos^2x=1
```

đúng cho mọi `x` trong domain.

Equation:

```math
\sin x=\frac12
```

chỉ đúng tại một tập values cụ thể.

Phân biệt này quan trọng vì strategy khác nhau: với identity ta transform hai expressions để chứng minh equivalence; với equation ta tìm solution set.

## 6. Giải phương trình lượng giác cần tính periodicity

Xét:

```math
\sin x=\frac12.
```

Trong một cycle:

```math
x=\frac\pi6,
\qquad
x=\frac{5\pi}{6}.
```

Full solution:

```math
x=\frac\pi6+2k\pi
```

hoặc

```math
x=\frac{5\pi}{6}+2k\pi,
\qquad k\in\mathbb Z.
```

Inverse trig function như `arcsin` chỉ trả principal branch. Nó không tự trả mọi nghiệm của periodic equation.

## 7. Symmetry giúp tìm solution set

Trên unit circle:

```math
\sin(\pi-x)=\sin x,
```

```math
\cos(-x)=\cos x,
```

```math
\sin(-x)=-\sin x.
```

Các symmetry này giải thích vì sao một value thường xuất hiện tại nhiều angles. Việc hiểu graph/unit circle tốt hơn memorizing case tables.

## 8. Sinusoid tổng quát

Một sinusoid:

```math
y=A\sin(\omega t+\phi)+C.
```

Các parameters có meaning:

```text
|A| → amplitude
\omega → angular frequency
\phi → phase
C → offset
```

Period:

```math
T=\frac{2\pi}{|\omega|}.
```

Ordinary frequency `f`:

```math
\omega=2\pi f.
```

Units matter: nếu `t` là seconds thì `\omega` có unit rad/s và `f` có Hz.

## 9. Phase không phải time delay, nhưng có relation

Với

```math
A\sin(\omega t+\phi)
```

viết:

```math
A\sin\bigl(\omega(t+\phi/\omega)\bigr).
```

Do đó phase shift `\phi` tương ứng time shift `\phi/\omega` cho fixed frequency.

Cùng một phase angle ở hai frequencies khác nhau không tạo cùng time delay. Đây là detail quan trọng trong signal/system analysis.

## 10. Simple harmonic motion từ differential equation

Ideal oscillator:

```math
x''(t)+\omega^2x(t)=0.
```

Sine/cosine là natural solutions vì:

```math
\frac{d^2}{dt^2}\cos(\omega t)
=-\omega^2\cos(\omega t).
```

General solution:

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Equivalent amplitude-phase form:

```math
x(t)=R\cos(\omega t-\delta).
```

Hai representations cùng mô tả một oscillator; lựa chọn representation phụ thuộc task.

## 11. State-space interpretation

Đặt state:

```math
\begin{bmatrix}x\\v\end{bmatrix}.
```

Với harmonic oscillator, state trajectory là ellipse/circle sau normalization. Oscillation trong time-domain có thể được hiểu như rotation trong phase space.

Đây là bridge giữa trigonometry, differential equations, matrices và control.

## 12. Damped và forced oscillation

Ideal SHM chỉ là model cơ bản. Real systems thường có damping và forcing:

```math
x''+2\zeta\omega_nx'+\omega_n^2x=F(t).
```

Khi forcing frequency gần natural frequency, resonance có thể làm amplitude lớn.

Trigonometric input/output analysis vì vậy là một phần cốt lõi của control systems và electrical engineering.

## 13. Complex exponential thống nhất sine và cosine

Euler formula:

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Do đó:

```math
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}2,
```

```math
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
```

Complex exponential biến differentiation thành multiplication:

```math
\frac{d}{dt}e^{i\omega t}=i\omega e^{i\omega t}.
```

Đây là lý do phasor/Fourier/Laplace methods cực kỳ hiệu quả: oscillation trở thành algebra trên complex amplitudes.

## 14. Orthogonality của harmonics

Trên interval phù hợp, sine/cosine ở different integer frequencies trực giao:

```math
\int_0^{2\pi}\cos(nx)\cos(mx)\,dx=0,
\qquad n\ne m.
```

Tương tự cho sine và mixed terms.

Điều này cho phép tách signal thành frequency components giống như vector được tách theo orthogonal basis.

Fourier analysis thực chất là linear algebra trong function space.

## 15. Harmonics và Fourier viewpoint

Một periodic signal có thể được represent conceptually như:

```math
f(t)
=
a_0+
\sum_{n=1}^{\infty}
[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)].
```

`\omega_0` là fundamental frequency; multiples `n\omega_0` là harmonics.

Complex signal không “chứa sine waves vật lý nhỏ” theo literal sense; Fourier representation là một basis decomposition giúp analysis.

## 16. Aliasing và sampling connection

Continuous sinusoid khi sampled không luôn có unique discrete-frequency representation. Frequencies khác nhau có thể tạo cùng sampled values nếu sampling rate không đủ.

Nyquist criterion trong ideal band-limited setting yêu cầu sampling frequency lớn hơn hai lần highest frequency để avoid ambiguity.

Đây là nơi trig, information, numerical sampling và signal processing gặp nhau.

## Worked example: beat frequency

Hai tones gần nhau:

```math
\cos(\omega_1t)+\cos(\omega_2t)
```

sum-to-product cho:

```math
2\cos\left(\frac{\omega_1-\omega_2}{2}t\right)
\cos\left(\frac{\omega_1+\omega_2}{2}t\right).
```

Ta thấy fast carrier được modulate bởi slow envelope. Beat phenomenon không cần thêm physics phức tạp để hiểu first-order; nó nằm ngay trong trig identity.

## Knowledge Connection

```text
unit circle
→ rotation matrix
→ identities
→ complex exponential
→ harmonic oscillator
→ Fourier basis
→ signal processing / control
```

Trong AI, positional encodings và spectral methods cũng dùng sinusoidal/frequency representations. Trong Physics, wave equations và quantum states thường decomposition theo modes. Trong Finance, periodic/seasonal components có thể được modeled bằng Fourier features, nhưng phải cẩn thận không nhầm periodic fit với causal mechanism.

## Mental Model

> Sine và cosine là coordinates của rotation. Identities là algebra của rotations; harmonics là repeated rotations ở different frequencies; Fourier analysis là decomposition theo orthogonal rotating modes.

## Common Misconceptions

Degrees và radians không interchangeable trong calculus. `arcsin(sin x)` không luôn bằng `x` vì inverse chỉ dùng principal branch. Identity không phải equation. Phase shift không đổi frequency. Một Fourier decomposition không tự chứng minh signal thật sự được tạo bởi independent sinusoidal causes.
