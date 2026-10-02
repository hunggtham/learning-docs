# Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Sine và cosine là modes của rotation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Orthogonality biến functions thành coordinates** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Fourier với signals và frequency, để chuyển tín hiệu từ miền thời gian sang thành phần dao động có thể phân tích.

Một tín hiệu (signal / 신호) theo thời gian (time / 시간) lĩnh vực (domain / 도메인) trả lời:

```text
value ở thời điểm t là gì?
```

Fourier viewpoint hỏi câu khác:

```text
signal này được tạo từ những oscillatory components nào?
```

Đó không phải hai signals khác nhau. Đó là hai coordinate các hệ thống (systems / 시스템들) cho cùng một đối tượng (object / 객체).

Mental luồng (flow / 흐름):

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

Chúng cũng là solutions/eigenmodes của nhiều tuyến tính (linear / 선형) differential equations.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **2. Orthogonality biến functions thành coordinates** tiếp nhận điểm tựa từ **1. Sine và cosine là modes của rotation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Fourier series là tuyến tính (linear / 선형) algebra trong hàm (function / 함수) không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Orthogonality biến functions thành coordinates

Trên suitable interval:

```math
\int \sin(nt)\sin(mt)dt=0
```

khi `n≠m`, và tương tự cho cosine modes.

Đây là function-space phiên bản (version / 버전) của orthogonal vectors.

Nếu vectors có basis:

```text
e1,e2,...
```

thì periodic functions có thể dùng basis:

```text
1, cos t, sin t, cos 2t, sin 2t, ...
```

Fourier coefficient là projection.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **3. Fourier series là tuyến tính (linear / 선형) algebra trong hàm (function / 함수) không gian (space / 공간)** tiếp nhận điểm tựa từ **2. Orthogonality biến functions thành coordinates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Complex exponential làm phase algebra đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Fourier series là tuyến tính (linear / 선형) algebra trong hàm (function / 함수) không gian (space / 공간)

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

Đây cùng hình học (geometry / 기하학) với:

```math
c_i=\langle x,e_i\rangle
```

trong orthonormal basis.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **4. Complex exponential làm phase algebra đơn giản** tiếp nhận điểm tựa từ **3. Fourier series là tuyến tính (linear / 선형) algebra trong hàm (function / 함수) không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Fourier transform mở periodic basis thành continuum frequencies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Complex numbers không thêm “imaginary physics”; chúng là biểu diễn (representation / 표현) tiện cho amplitude + phase.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **5. Fourier transform mở periodic basis thành continuum frequencies** tiếp nhận điểm tựa từ **4. Complex exponential làm phase algebra đơn giản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Parseval: năng lượng (energy / 에너지) được bảo toàn qua biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Magnitude spectrum nói strength; phase spectrum nói alignment/thời gian (time / 시간) cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **6. Parseval: năng lượng (energy / 에너지) được bảo toàn qua biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **5. Fourier transform mở periodic basis thành continuum frequencies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Differentiation trở thành multiplication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Parseval: năng lượng (energy / 에너지) được bảo toàn qua biểu diễn (representation / 표현)

Under suitable convention:

```math
\int|f(t)|^2dt
\propto
\int|F(\omega)|^2d\omega.
```

Đây là Parseval/Plancherel idea.

Mô hình tư duy (mental model / 사고 모델):

> đổi basis không tạo hoặc xóa L2 năng lượng (energy / 에너지); nó chỉ redistribute coordinates.

Đây là direct liên kết (connection / 연결) với orthonormal tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **7. Differentiation trở thành multiplication** tiếp nhận điểm tựa từ **6. Parseval: năng lượng (energy / 에너지) được bảo toàn qua biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Convolution theorem** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Differential operators trở thành algebraic multipliers trong frequency lĩnh vực (domain / 도메인).

Đây là lý do Fourier cực mạnh cho tuyến tính (linear / 선형) PDE/ODE.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **8. Convolution theorem** tiếp nhận điểm tựa từ **7. Differentiation trở thành multiplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Convolution theorem

Convolution:

```math
(f*g)(t)=\int f(\tau)g(t-\tau)d\tau.
```

Fourier transform:

```math
\mathcal F\{f*g\}=F(\omega)G(\omega).
```

Một thao tác (operation / 연산) “trộn” phức tạp trong thời gian (time / 시간) lĩnh vực (domain / 도메인) trở thành pointwise multiplication trong frequency lĩnh vực (domain / 도메인).

Đây là theme lớn của transforms:

```text
chọn representation nơi operator trở nên đơn giản
```

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **9. tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **8. Convolution theorem** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Frequency không tự nói “khi nào”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들)

Một LTI hệ thống (system / 시스템) có impulse phản hồi (response / 응답) `h(t)`.

Đầu ra (output / 출력):

```math
y=x*h.
```

Frequency lĩnh vực (domain / 도메인):

```math
Y(\omega)=X(\omega)H(\omega).
```

`H(ω)` là frequency phản hồi (response / 응답).

Low-pass filter có `|H(ω)|` lớn ở low frequencies và nhỏ ở high frequencies.

Filtering trở thành shaping spectrum.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **10. Frequency không tự nói “khi nào”** tiếp nhận điểm tựa từ **9. tuyến tính (linear / 선형) time-invariant các hệ thống (systems / 시스템들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Time-frequency bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Frequency không tự nói “khi nào”

Pure Fourier transform có toàn cục (global / 전역) hỗ trợ (support / 지원).

Nếu tín hiệu (signal / 신호) frequency content thay đổi theo thời gian (time / 시간), ordinary spectrum không nói thành phần (component / 컴포넌트) xuất hiện lúc nào.

Need time-frequency methods:

```text
Short-Time Fourier Transform
wavelets
```

Sự đánh đổi (trade-off / 트레이드오프):

```text
window ngắn → tốt về time, kém frequency resolution
window dài → tốt frequency, kém time localization
```

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **11. Time-frequency bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **10. Frequency không tự nói “khi nào”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Sampling biến continuous tín hiệu (signal / 신호) thành discrete chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Time-frequency bất định (uncertainty / 불확실성)

Tín hiệu (signal / 신호) localized rất hẹp trong thời gian (time / 시간) cần broad frequency content.

Pure sinusoid có chính xác (exact / 정확한) frequency nhưng tồn tại infinitely long.

Đây là structural sự đánh đổi (trade-off / 트레이드오프) của Fourier biểu diễn (representation / 표현), không chỉ limitation của instrument.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **11. Time-frequency bất định (uncertainty / 불확실성)** xác định đầu vào; **12. Sampling biến continuous tín hiệu (signal / 신호) thành discrete chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Aliasing: different frequencies trở nên indistinguishable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Sampling biến continuous tín hiệu (signal / 신호) thành discrete chuỗi (sequence / 시퀀스)

Mẫu (sample / 표본):

```math
x[n]=x(nT_s).
```

Sampling frequency:

```math
f_s=1/T_s.
```

Sampling không chỉ “ghi ít points hơn”; nó periodize spectrum theo frequency.

Nếu spectral copies overlap, aliasing xảy ra.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **12. Sampling biến continuous tín hiệu (signal / 신호) thành discrete chuỗi (sequence / 시퀀스)** xác định đầu vào; **13. Aliasing: different frequencies trở nên indistinguishable** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. Nyquist theorem cần các giả định (assumptions / 가정들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Aliasing: different frequencies trở nên indistinguishable

Discrete-time sinusoid:

```math
\cos(2\pi(f+kf_s)n/f_s)
```

cho same samples với frequency shifted by integer multiples of `f_s`.

Vì vậy high frequency có thể masquerade thành low frequency.

Aliasing là thông tin (information / 정보) mất mát (loss / 손실) from sampling.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **14. Nyquist theorem cần các giả định (assumptions / 가정들)** tiếp nhận điểm tựa từ **13. Aliasing: different frequencies trở nên indistinguishable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. DFT: Fourier coordinates cho finite discrete véc-tơ (vector / 벡터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Nyquist theorem cần các giả định (assumptions / 가정들)

Với ideal band-limited tín hiệu (signal / 신호) max frequency `f_max`, perfect reconstruction theoretically possible nếu:

```math
f_s>2f_{max}.
```

Nhưng real signals không perfectly band-limited và filters không ideal.

Practical các hệ thống (systems / 시스템들) use margin + anti-alias filtering.

“mẫu (sample / 표본) at twice frequency” không phải universal magic quy tắc (rule / 규칙).

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **15. DFT: Fourier coordinates cho finite discrete véc-tơ (vector / 벡터)** tiếp nhận điểm tựa từ **14. Nyquist theorem cần các giả định (assumptions / 가정들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. FFT không phải transform khác** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. DFT: Fourier coordinates cho finite discrete véc-tơ (vector / 벡터)

Với `N` samples:

```math
X_k=\sum_{n=0}^{N-1}x_ne^{-i2\pi kn/N}.
```

DFT là tuyến tính (linear / 선형) transformation:

```math
X=Fx.
```

Fourier ma trận (matrix / 행렬) entries là complex roots of unity.

DFT vì vậy cũng là phép nhân ma trận (matrix multiplication / 행렬 곱셈) conceptually.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **16. FFT không phải transform khác** tiếp nhận điểm tựa từ **15. DFT: Fourier coordinates cho finite discrete véc-tơ (vector / 벡터)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Spectral leakage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **17. Spectral leakage** tiếp nhận điểm tựa từ **16. FFT không phải transform khác** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Frequency resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Spectral leakage

Finite observation cửa sổ (window / 윈도우) effectively multiplies infinite tín hiệu (signal / 신호) by hàm cửa sổ (window function / 윈도우 함수).

Time-domain multiplication corresponds to frequency-domain convolution.

If sinusoid does not align DFT bins, năng lượng (energy / 에너지) spreads across bins — spectral leakage.

Cửa sổ (window / 윈도우) functions reduce some leakage patterns but trade main-lobe width vs side-lobe suppression.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **18. Frequency resolution** tiếp nhận điểm tựa từ **17. Spectral leakage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Filtering và causality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Frequency resolution

Observation duration `T` affects spacing of frequency bins roughly:

```math
\Delta f\approx1/T.
```

Longer observation distinguishes closer frequencies.

Higher mẫu (sample / 표본) tỷ lệ (rate / 비율) increases captured frequency phạm vi (range / 범위) but does not by itself give arbitrarily fine frequency resolution for fixed duration.

Phạm vi (range / 범위) và resolution là different concepts.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **19. Filtering và causality** tiếp nhận điểm tựa từ **18. Frequency resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Gibbs phenomenon** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Filtering và causality

Ideal brick-wall frequency filter has impulse phản hồi (response / 응답) extending indefinitely in thời gian (time / 시간).

Real-time nhân quả (causal / 인과적) implementations need approximations/delay.

Perfect frequency selectivity and perfect thời gian (time / 시간) localization cannot both be achieved freely.

Kỹ thuật (engineering / 엔지니어링) filters live inside these trade-offs.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **20. Gibbs phenomenon** tiếp nhận điểm tựa từ **19. Filtering và causality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Gibbs phenomenon

Fourier series approximating discontinuity overshoots near jump.

Increasing number modes narrows oscillation region but maximum overshoot does not simply vanish pointwise at ranh giới (boundary / 경계) in naive sense.

This is biểu diễn (representation / 표현) hành vi (behavior / 동작) near nonsmooth cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **21. Compression** tiếp nhận điểm tựa từ **20. Gibbs phenomenon** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Fourier trong PDE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Compression

If tín hiệu (signal / 신호) năng lượng (energy / 에너지) concentrated in few transform coefficients, sparse-ish frequency biểu diễn (representation / 표현) enables compression.

Transform coding idea:

```text
signal
→ transform
→ coefficients
→ quantize/drop less important components
→ inverse transform
```

JPEG uses DCT-like khối (block / 블록) transforms; audio codecs combine transform ideas with perceptual các mô hình (models / 모델들).

Compression chất lượng (quality / 품질) depends on what thông tin (information / 정보) humans/tasks care about, not only coefficient magnitude.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **22. Fourier trong PDE** tiếp nhận điểm tựa từ **21. Compression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Fourier trong convolutional networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Fourier trong PDE

Heat equation:

```math
u_t=\alpha u_{xx}.
```

Fourier transform in không gian (space / 공간) turns:

```math
u_{xx}
```

into:

```math
-\omega^2\hat u.
```

Each frequency chế độ (mode / 모드) evolves independently roughly:

```math
\hat u_t=-\alpha\omega^2\hat u.
```

Higher frequencies decay faster, explaining diffusion as smoothing.

Transform reveals qualitative hành vi (behavior / 동작) almost immediately.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **23. Fourier trong convolutional networks** tiếp nhận điểm tựa từ **22. Fourier trong PDE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Fourier features trong AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Fourier trong convolutional networks

Convolution filters have frequency responses.

Early vision filters can behave like edge/high-frequency detectors or smoothing/low-pass operations.

But hiện đại (modern / 현대적) CNN hành vi (behavior / 동작) is nonlinear and data-dependent, so frequency-domain intuition is one lens, not complete explanation.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **24. Fourier features trong AI** tiếp nhận điểm tựa từ **23. Fourier trong convolutional networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Fourier vs Laplace vs Z-transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Fourier features trong AI

Ánh xạ (mapping / 매핑) inputs through sinusoidal features can help represent periodic/high-frequency variation.

Positional encodings use sinusoidal components in some architectures.

Liên kết (connection / 연결):

```text
coordinates
→ phases at multiple frequencies
→ richer representation of position
```

Again, transform-style basis thiết kế (design / 설계) affects learnability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **25. Fourier vs Laplace vs Z-transform** tiếp nhận điểm tựa từ **24. Fourier features trong AI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. dùng chung (common / 공통) thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Fourier vs Laplace vs Z-transform

Rough mental map:

```text
Fourier → frequency decomposition, oscillatory basis
Laplace → exponential weighting + continuous-time dynamics/stability
Z-transform → discrete-time sequences/systems
```

They overlap but answer different questions and have different convergence domains.

> **Chuyển mạch:** Trong **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **26. dùng chung (common / 공통) thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **25. Fourier vs Laplace vs Z-transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. dùng chung (common / 공통) thất bại (failure / 실패) modes

### Reading spectrum without phase

Magnitude alone may not reconstruct waveform.

### Assuming frequency means cause

Spectral peak shows thành phần (component / 컴포넌트)/periodicity, not nhân quả (causal / 인과적) explanation.

### Ignoring windowing

Finite bản ghi (record / 레코드) changes observed spectrum.

### Misusing Nyquist

Band-limit giả định (assumption / 가정) matters.

### Thinking FFT changes mathematics

FFT only computes DFT efficiently.

> **Chuyển mạch:** Ở chặng này của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** tiếp nhận điểm tựa từ **26. dùng chung (common / 공통) thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần kết nối đặt Fourier cạnh linear algebra, complex numbers, convolution, filtering và PDE. Hãy xem frequency domain như một phép đổi biểu diễn để tách pattern, không phải một thế giới công thức riêng.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Liên kết kiến thức (knowledge connection / 지식 연결) — Fourier, Signals và Frequency: đổi biểu diễn (representation / 표현) để làm lộ cấu trúc (structure / 구조)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Fourier analysis is a change of coordinates. Time/space domain shows where behavior happens; frequency domain shows which oscillatory modes compose it. The power comes from choosing coordinates where convolution, differentiation and many linear systems become simpler — but localization, sampling and finite windows introduce real trade-offs.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
