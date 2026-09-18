# Fourier, tín hiệu và miền tần số

Một signal phức tạp theo thời gian có thể khó hiểu trong time domain. Fourier đưa ra một viewpoint khác: thay vì hỏi signal có value gì tại mỗi thời điểm, hãy hỏi nó chứa những oscillatory components nào.

## Sine/cosine như basis của oscillation

Một sinusoid

```math
A\cos(\omega t+\phi)
```

được xác định bởi amplitude, angular frequency và phase.

Các sine/cosine frequencies khác nhau trực giao trên suitable intervals. Vì vậy chúng có thể đóng vai trò basis giống coordinate axes trong vector space.

Thay vì biểu diễn vector bằng coefficients theo `e_1,e_2,...`, ta biểu diễn function bằng coefficients theo trigonometric basis.

## Fourier series

Với periodic function period `2\pi`, một representation điển hình là

```math
f(x)\sim \frac{a_0}{2}
+\sum_{n=1}^{\infty}
\left(a_n\cos nx+b_n\sin nx\right).
```

Coefficients là projections:

```math
a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx,
```

```math
b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
```

Đây chính là linear algebra trong function space: inner products lấy component theo basis functions.

## Complex exponential form

Euler formula:

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Cho phép viết Fourier series compact:

```math
f(t)=\sum_{k=-\infty}^{\infty}c_ke^{ik\omega_0t}.
```

Complex numbers encode sine/cosine và phase trong một object algebraically thuận tiện.

## Fourier transform

Nonperiodic signals cần continuous range frequencies. Fourier transform một convention phổ biến:

```math
F(\omega)=\int_{-\infty}^{\infty}f(t)e^{-i\omega t}\,dt.
```

Inverse transform reconstruct signal từ spectrum.

Interpretation: `F(\omega)` đo complex amplitude của frequency `\omega` trong signal.

## Time localization và frequency localization

Một pure sinusoid tồn tại mãi theo thời gian và có single exact frequency. Một short pulse localized rất tốt trong time nhưng cần many frequencies để construct.

Đây là time–frequency trade-off, liên hệ sâu với uncertainty principles của Fourier analysis. Muốn biết “frequency thay đổi theo thời gian” cần tools như short-time Fourier transform hoặc wavelets.

## Convolution theorem

Convolution trong time domain:

```math
(f*g)(t)=\int f(\tau)g(t-\tau)d\tau.
```

Fourier transform biến convolution thành multiplication:

```math
\mathcal F\{f*g\}=F(\omega)G(\omega).
```

Đây là một lý do frequency domain mạnh: filtering vốn là convolution có thể trở thành pointwise multiplication.

Trong CNN, “convolution” discrete được dùng để extract local patterns; mathematical relation với frequency response giúp giải thích filters low-pass/high-pass.

## Sampling và Nyquist

Digital system chỉ observe signal ở discrete times. Nếu sampling frequency quá thấp, high frequencies có thể masquerade thành lower frequencies — aliasing.

Với band-limited signal có maximum frequency `f_{max}`, ideal sampling theorem yêu cầu sampling rate lớn hơn `2f_{max}` để reconstruct under ideal assumptions.

Nyquist rate không phải magic guarantee cho arbitrary signals; band limitation và idealized reconstruction assumptions rất quan trọng.

## DFT và FFT

Discrete Fourier Transform của `N` samples:

```math
X_k=\sum_{n=0}^{N-1}x_ne^{-i2\pi kn/N}.
```

Naive computation cần `O(N^2)` operations. Fast Fourier Transform uses symmetries để giảm xuống roughly

```math
O(N\log N).
```

Đây là ví dụ đẹp nơi algebraic structure trực tiếp thay đổi computational complexity.

## Compression và filtering

Nếu signal/image energy tập trung ở một số coefficients, ta có thể approximate bằng cách giữ components quan trọng và bỏ nhỏ hơn. JPEG dùng cosine-like transform blocks; audio codecs dùng frequency-domain ideas phức tạp hơn kết hợp perceptual models.

Noise thường có spectral signature khác signal, nên filters có thể attenuate frequency bands không mong muốn.

## Knowledge Connection

Fourier là điểm gặp của trigonometry, complex numbers, inner products, infinite series, integrals và algorithms. Differential equations cũng đơn giản hóa vì differentiation trong time/space domain tương ứng multiplication bởi frequency factor trong transform domain.

## Mental Model

> Fourier transform giống đổi hệ tọa độ: time domain hỏi signal xảy ra khi nào; frequency domain hỏi signal được tạo từ những nhịp dao động nào. Không phải hai signals khác nhau, mà là hai representations của cùng một object.

## Common Misconceptions

Spectrum không tự động nói frequency xảy ra vào thời điểm nào. Sampling rate `2f_max` chỉ đủ dưới assumptions lý tưởng và thường cần margin/anti-aliasing filters. FFT không phải một transform khác DFT; nó là family algorithms tính DFT nhanh hơn. Fourier representation có thể gặp Gibbs phenomenon gần discontinuities.
