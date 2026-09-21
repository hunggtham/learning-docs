# Knowledge Connection — Fourier, Signals và Frequency: đổi representation để làm lộ structure

Một signal theo time domain trả lời:

```text
value ở thời điểm t là gì?
```

Fourier viewpoint hỏi câu khác:

```text
signal này được tạo từ những oscillatory components nào?
```

Đó không phải hai signals khác nhau. Đó là hai coordinate systems cho cùng một object.

Mental flow:

```text
periodic motion
→ sine/cosine basis
→ projection coefficients
→ Fourier series
→ Fourier transform
→ convolution/filtering
→ sampling/aliasing
→ DFT/FFT
```

## 1. Sine và cosine là modes của rotation

Một sinusoid:

```math
x(t)=A\cos(\omega t+\phi)
```

có:

```text
A       amplitude
ω       angular frequency
φ       phase
T=2π/ω  period
```

Sine/cosine xuất hiện tự nhiên vì uniform rotation projected lên coordinate axis tạo sinusoidal motion.

Chúng cũng là solutions/eigenmodes của nhiều linear differential equations.

## 2. Orthogonality biến functions thành coordinates

Trên suitable interval:

```math
\int \sin(nt)\sin(mt)dt=0
```

khi `n≠m`, và tương tự cho cosine modes.

Đây là function-space version của orthogonal vectors.

Nếu vectors có basis:

```text
e1,e2,...
```

thì periodic functions có thể dùng basis:

```text
1, cos t, sin t, cos 2t, sin 2t, ...
```

Fourier coefficient là projection.

## 3. Fourier series là linear algebra trong function space

Với period `2π`:

```math
f(t)\sim \frac{a_0}{2}
+\sum_{n=1}^{\infty}
(a_n\cos nt+b_n\sin nt).
```

Coefficients:

```math
a_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\cos(nt)dt
```

```math
b_n=\frac1\pi\int_{-\pi}^{\pi}f(t)\sin(nt)dt.
```

Đây cùng geometry với:

```math
c_i=\langle x,e_i\rangle
```

trong orthonormal basis.

## 4. Complex exponential làm phase algebra đơn giản

Euler:

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Một oscillation:

```math
Ae^{i(\omega t+\phi)}.
```

Phase shift trở thành multiplication bởi complex phase factor.

Fourier series complex form:

```math
f(t)=\sum_{k=-\infty}^{\infty}c_ke^{ik\omega_0t}.
```

Complex numbers không thêm “imaginary physics”; chúng là representation tiện cho amplitude + phase.

## 5. Fourier transform mở periodic basis thành continuum frequencies

Một convention:

```math
F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}dt.
```

Inverse:

```math
f(t)=\frac1{2\pi}\int_{-\infty}^{\infty}F(\omega)e^{i\omega t}d\omega.
```

Interpretation:

```text
F(ω) = complex coefficient của frequency ω
```

Magnitude spectrum nói strength; phase spectrum nói alignment/time structure.

## 6. Parseval: energy được bảo toàn qua representation

Under suitable convention:

```math
\int|f(t)|^2dt
\propto
\int|F(\omega)|^2d\omega.
```

Đây là Parseval/Plancherel idea.

Mental model:

> đổi basis không tạo hoặc xóa L2 energy; nó chỉ redistribute coordinates.

Đây là direct connection với orthonormal linear algebra.

## 7. Differentiation trở thành multiplication

Nếu:

```math
f(t)\leftrightarrow F(\omega),
```

thì roughly:

```math
f'(t)\leftrightarrow i\omega F(\omega).
```

Second derivative:

```math
f''(t)\leftrightarrow -\omega^2F(\omega).
```

Differential operators trở thành algebraic multipliers trong frequency domain.

Đây là lý do Fourier cực mạnh cho linear PDE/ODE.

## 8. Convolution theorem

Convolution:

```math
(f*g)(t)=\int f(\tau)g(t-\tau)d\tau.
```

Fourier transform:

```math
\mathcal F\{f*g\}=F(\omega)G(\omega).
```

Một operation “trộn” phức tạp trong time domain trở thành pointwise multiplication trong frequency domain.

Đây là theme lớn của transforms:

```text
chọn representation nơi operator trở nên đơn giản
```

## 9. Linear time-invariant systems

Một LTI system có impulse response `h(t)`.

Output:

```math
y=x*h.
```

Frequency domain:

```math
Y(\omega)=X(\omega)H(\omega).
```

`H(ω)` là frequency response.

Low-pass filter có `|H(ω)|` lớn ở low frequencies và nhỏ ở high frequencies.

Filtering trở thành shaping spectrum.

## 10. Frequency không tự nói “khi nào”

Pure Fourier transform có global support.

Nếu signal frequency content thay đổi theo time, ordinary spectrum không nói component xuất hiện lúc nào.

Need time-frequency methods:

```text
Short-Time Fourier Transform
wavelets
```

Trade-off:

```text
window ngắn → tốt về time, kém frequency resolution
window dài → tốt frequency, kém time localization
```

## 11. Time-frequency uncertainty

Signal localized rất hẹp trong time cần broad frequency content.

Pure sinusoid có exact frequency nhưng tồn tại infinitely long.

Đây là structural trade-off của Fourier representation, không chỉ limitation của instrument.

## 12. Sampling biến continuous signal thành discrete sequence

Sample:

```math
x[n]=x(nT_s).
```

Sampling frequency:

```math
f_s=1/T_s.
```

Sampling không chỉ “ghi ít points hơn”; nó periodize spectrum theo frequency.

Nếu spectral copies overlap, aliasing xảy ra.

## 13. Aliasing: different frequencies trở nên indistinguishable

Discrete-time sinusoid:

```math
\cos(2\pi(f+kf_s)n/f_s)
```

cho same samples với frequency shifted by integer multiples of `f_s`.

Vì vậy high frequency có thể masquerade thành low frequency.

Aliasing là information loss from sampling.

## 14. Nyquist theorem cần assumptions

Với ideal band-limited signal max frequency `f_max`, perfect reconstruction theoretically possible nếu:

```math
f_s>2f_{max}.
```

Nhưng real signals không perfectly band-limited và filters không ideal.

Practical systems use margin + anti-alias filtering.

“Sample at twice frequency” không phải universal magic rule.

## 15. DFT: Fourier coordinates cho finite discrete vector

Với `N` samples:

```math
X_k=\sum_{n=0}^{N-1}x_ne^{-i2\pi kn/N}.
```

DFT là linear transformation:

```math
X=Fx.
```

Fourier matrix entries là complex roots of unity.

DFT vì vậy cũng là matrix multiplication conceptually.

## 16. FFT không phải transform khác

Naive DFT:

```text
O(N²)
```

FFT exploits symmetry/factorization để tính same DFT in roughly:

```text
O(N log N)
```

Đây là classic example:

```text
same mathematics
+ better algorithmic structure
→ radically lower compute cost
```

## 17. Spectral leakage

Finite observation window effectively multiplies infinite signal by window function.

Time-domain multiplication corresponds to frequency-domain convolution.

If sinusoid does not align DFT bins, energy spreads across bins — spectral leakage.

Window functions reduce some leakage patterns but trade main-lobe width vs side-lobe suppression.

## 18. Frequency resolution

Observation duration `T` affects spacing of frequency bins roughly:

```math
\Delta f\approx1/T.
```

Longer observation distinguishes closer frequencies.

Higher sample rate increases captured frequency range but does not by itself give arbitrarily fine frequency resolution for fixed duration.

Range và resolution là different concepts.

## 19. Filtering và causality

Ideal brick-wall frequency filter has impulse response extending indefinitely in time.

Real-time causal implementations need approximations/delay.

Perfect frequency selectivity and perfect time localization cannot both be achieved freely.

Engineering filters live inside these trade-offs.

## 20. Gibbs phenomenon

Fourier series approximating discontinuity overshoots near jump.

Increasing number modes narrows oscillation region but maximum overshoot does not simply vanish pointwise at boundary in naive sense.

This is representation behavior near nonsmooth structure.

## 21. Compression

If signal energy concentrated in few transform coefficients, sparse-ish frequency representation enables compression.

Transform coding idea:

```text
signal
→ transform
→ coefficients
→ quantize/drop less important components
→ inverse transform
```

JPEG uses DCT-like block transforms; audio codecs combine transform ideas with perceptual models.

Compression quality depends on what information humans/tasks care about, not only coefficient magnitude.

## 22. Fourier trong PDE

Heat equation:

```math
u_t=\alpha u_{xx}.
```

Fourier transform in space turns:

```math
u_{xx}
```

into:

```math
-\omega^2\hat u.
```

Each frequency mode evolves independently roughly:

```math
\hat u_t=-\alpha\omega^2\hat u.
```

Higher frequencies decay faster, explaining diffusion as smoothing.

Transform reveals qualitative behavior almost immediately.

## 23. Fourier trong convolutional networks

Convolution filters have frequency responses.

Early vision filters can behave like edge/high-frequency detectors or smoothing/low-pass operations.

But modern CNN behavior is nonlinear and data-dependent, so frequency-domain intuition is one lens, not complete explanation.

## 24. Fourier features trong AI

Mapping inputs through sinusoidal features can help represent periodic/high-frequency variation.

Positional encodings use sinusoidal components in some architectures.

Connection:

```text
coordinates
→ phases at multiple frequencies
→ richer representation of position
```

Again, transform-style basis design affects learnability.

## 25. Fourier vs Laplace vs Z-transform

Rough mental map:

```text
Fourier → frequency decomposition, oscillatory basis
Laplace → exponential weighting + continuous-time dynamics/stability
Z-transform → discrete-time sequences/systems
```

They overlap but answer different questions and have different convergence domains.

## 26. Common failure modes

### Reading spectrum without phase

Magnitude alone may not reconstruct waveform.

### Assuming frequency means cause

Spectral peak shows component/periodicity, not causal explanation.

### Ignoring windowing

Finite record changes observed spectrum.

### Misusing Nyquist

Band-limit assumption matters.

### Thinking FFT changes mathematics

FFT only computes DFT efficiently.

## Knowledge Connection

```text
Trigonometry → sine/cosine
Complex numbers → phase/exponential
Inner product → coefficients
Linear algebra → basis change
Calculus → derivative multipliers
Convolution → filtering
Sampling → discrete math / aliasing
Algorithms → FFT complexity
PDE → mode decomposition
AI → convolution / Fourier features
```

## Mental Model

> Fourier analysis is a change of coordinates. Time/space domain shows where behavior happens; frequency domain shows which oscillatory modes compose it. The power comes from choosing coordinates where convolution, differentiation and many linear systems become simpler — but localization, sampling and finite windows introduce real trade-offs.