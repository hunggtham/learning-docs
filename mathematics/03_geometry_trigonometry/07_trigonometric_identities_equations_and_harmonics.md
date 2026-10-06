# Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. đơn vị (unit / 단위) circle là nguồn của identities cơ bản** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. Angle addition là composition của rotations** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối trigonometric identities với equations và harmonics, để biến đổi góc được dùng cho nghiệm, tín hiệu và hình học.

Sine và cosine nên được hiểu trước hết như **coordinates của rotation**, không phải hai functions rời rạc cần nhớ bảng công thức. Khi một điểm (point / 지점) quay trên đơn vị (unit / 단위) circle, `cos` là projection lên trục x và `sin` là projection lên trục y.

Từ viewpoint đó, identities, periodic equations, phasor, harmonics và Fourier phân tích (analysis / 분석) đều là các cách khác nhau để mô tả cùng một cấu trúc (structure / 구조): **rotation lặp lại theo thời gian hoặc angle**.

## 1. đơn vị (unit / 단위) circle là nguồn của identities cơ bản

Điểm (point / 지점) ở angle `\theta` trên đơn vị (unit / 단위) circle:

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

Vì vậy các identities này không phải formulas độc lập; chúng cùng xuất phát từ hình học (geometry / 기하학) của đơn vị (unit / 단위) circle.

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **1. đơn vị (unit / 단위) circle là nguồn của identities cơ bản** đặt vấn đề; **2. Angle addition là composition của rotations** đối chiếu bằng chứng, rồi **3. Double-angle, half-angle và identities khác** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. Angle addition là composition của rotations

Rotation ma trận (matrix / 행렬):

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

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **3. Double-angle, half-angle và identities khác** nối từ **2. Angle addition là composition của rotations** sang **4. Product-to-sum: vì sao multiplication tạo frequencies mới?**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Từ đây suy ra half-angle identities. Lesson quan trọng là không cần nhớ mọi định danh (identity / 식별자) như một item riêng; chỉ cần biết một vài generators và derive khi cần.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **4. Product-to-sum: vì sao multiplication tạo frequencies mới?** nối từ **3. Double-angle, half-angle và identities khác** sang **5. định danh (identity / 식별자) khác equation**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Một sản phẩm (product / 제품) của hai oscillations tạo components ở **sum frequency** và **difference frequency**.

Đây không chỉ là algebra. Nó là nền của mixing, modulation, heterodyning trong communications và tín hiệu (signal / 신호) processing.

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **5. định danh (identity / 식별자) khác equation** nối từ **4. Product-to-sum: vì sao multiplication tạo frequencies mới?** sang **6. Giải phương trình lượng giác cần tính periodicity**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. định danh (identity / 식별자) khác equation

Định danh (identity / 식별자):

```math
\sin^2x+\cos^2x=1
```

đúng cho mọi `x` trong lĩnh vực (domain / 도메인).

Equation:

```math
\sin x=\frac12
```

chỉ đúng tại một tập values cụ thể.

Phân biệt này quan trọng vì chiến lược (strategy / 전략) khác nhau: với định danh (identity / 식별자) ta transform hai expressions để chứng minh equivalence; với equation ta tìm solution set.

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **6. Giải phương trình lượng giác cần tính periodicity** nối từ **5. định danh (identity / 식별자) khác equation** sang **7. Symmetry giúp tìm solution set**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Inverse trig hàm (function / 함수) như `arcsin` chỉ trả principal branch. Nó không tự trả mọi nghiệm của periodic equation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **7. Symmetry giúp tìm solution set** nối từ **6. Giải phương trình lượng giác cần tính periodicity** sang **8. Sinusoid tổng quát**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Symmetry giúp tìm solution set

Trên đơn vị (unit / 단위) circle:

```math
\sin(\pi-x)=\sin x,
```

```math
\cos(-x)=\cos x,
```

```math
\sin(-x)=-\sin x.
```

Các symmetry này giải thích vì sao một giá trị (value / 값) thường xuất hiện tại nhiều angles. Việc hiểu đồ thị (graph / 그래프)/đơn vị (unit / 단위) circle tốt hơn memorizing trường hợp (case / 사례) tables.

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **8. Sinusoid tổng quát** nối từ **7. Symmetry giúp tìm solution set** sang **9. Phase không phải thời gian (time / 시간) delay, nhưng có quan hệ (relation / 관계)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Units matter: nếu `t` là seconds thì `\omega` có đơn vị (unit / 단위) rad/s và `f` có Hz.

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **9. Phase không phải thời gian (time / 시간) delay, nhưng có quan hệ (relation / 관계)** nối từ **8. Sinusoid tổng quát** sang **10. Simple harmonic motion từ differential equation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Phase không phải thời gian (time / 시간) delay, nhưng có quan hệ (relation / 관계)

Với

```math
A\sin(\omega t+\phi)
```

viết:

```math
A\sin\bigl(\omega(t+\phi/\omega)\bigr).
```

Do đó phase shift `\phi` tương ứng thời gian (time / 시간) shift `\phi/\omega` cho fixed frequency.

Cùng một phase angle ở hai frequencies khác nhau không tạo cùng thời gian (time / 시간) delay. Đây là detail quan trọng trong tín hiệu (signal / 신호)/hệ thống (system / 시스템) phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **10. Simple harmonic motion từ differential equation** nối từ **9. Phase không phải thời gian (time / 시간) delay, nhưng có quan hệ (relation / 관계)** sang **11. State-space interpretation**, vì cơ chế trước tạo đầu vào cho bước sau.

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

Hai representations cùng mô tả một oscillator; lựa chọn biểu diễn (representation / 표현) phụ thuộc tác vụ (task / 작업).

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **11. State-space interpretation** nối từ **10. Simple harmonic motion từ differential equation** sang **12. Damped và forced oscillation**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. State-space interpretation

Đặt trạng thái (state / 상태):

```math
\begin{bmatrix}x\\v\end{bmatrix}.
```

Với harmonic oscillator, trạng thái (state / 상태) trajectory là ellipse/circle sau normalization. Oscillation trong time-domain có thể được hiểu như rotation trong phase không gian (space / 공간).

Đây là cầu nối (bridge / 브리지) giữa trigonometry, differential equations, matrices và điều khiển (control / 제어).

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **12. Damped và forced oscillation** nối từ **11. State-space interpretation** sang **13. Complex exponential thống nhất sine và cosine**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Damped và forced oscillation

Ideal SHM chỉ là mô hình (model / 모델) cơ bản. Real các hệ thống (systems / 시스템들) thường có damping và forcing:

```math
x''+2\zeta\omega_nx'+\omega_n^2x=F(t).
```

Khi forcing frequency gần natural frequency, resonance có thể làm amplitude lớn.

Trigonometric đầu vào (input / 입력)/đầu ra (output / 출력) phân tích (analysis / 분석) vì vậy là một phần cốt lõi của điều khiển (control / 제어) các hệ thống (systems / 시스템들) và electrical kỹ thuật (engineering / 엔지니어링).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **13. Complex exponential thống nhất sine và cosine** nối từ **12. Damped và forced oscillation** sang **14. Orthogonality của harmonics**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **14. Orthogonality của harmonics** nối từ **13. Complex exponential thống nhất sine và cosine** sang **15. Harmonics và Fourier viewpoint**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Orthogonality của harmonics

Trên interval phù hợp, sine/cosine ở different integer frequencies trực giao:

```math
\int_0^{2\pi}\cos(nx)\cos(mx)\,dx=0,
\qquad n\ne m.
```

Tương tự cho sine và mixed terms.

Điều này cho phép tách tín hiệu (signal / 신호) thành frequency components giống như véc-tơ (vector / 벡터) được tách theo orthogonal basis.

Fourier phân tích (analysis / 분석) thực chất là tuyến tính (linear / 선형) algebra trong hàm (function / 함수) không gian (space / 공간).

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **15. Harmonics và Fourier viewpoint** nối từ **14. Orthogonality của harmonics** sang **16. Aliasing và sampling liên kết (connection / 연결)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Harmonics và Fourier viewpoint

Một periodic tín hiệu (signal / 신호) có thể được represent conceptually như:

```math
f(t)
=
a_0+
\sum_{n=1}^{\infty}
[a_n\cos(n\omega_0t)+b_n\sin(n\omega_0t)].
```

`\omega_0` là fundamental frequency; multiples `n\omega_0` là harmonics.

Complex tín hiệu (signal / 신호) không “chứa sine waves vật lý nhỏ” theo literal sense; Fourier biểu diễn (representation / 표현) là một basis decomposition giúp phân tích (analysis / 분석).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, sau nội dung của **15. Harmonics và Fourier viewpoint**, **16. Aliasing và sampling liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Worked example: beat frequency** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. Aliasing và sampling liên kết (connection / 연결)

Continuous sinusoid khi sampled không luôn có unique discrete-frequency biểu diễn (representation / 표현). Frequencies khác nhau có thể tạo cùng sampled values nếu sampling tỷ lệ (rate / 비율) không đủ.

Nyquist criterion trong ideal band-limited setting yêu cầu sampling frequency lớn hơn hai lần highest frequency để avoid ambiguity.

Đây là nơi trig, thông tin (information / 정보), numerical sampling và tín hiệu (signal / 신호) processing gặp nhau.

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **16. Aliasing và sampling liên kết (connection / 연결)** nêu quy tắc; **Worked example: beat frequency** thử quy tắc trong tình huống, rồi **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả.

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

Ta thấy fast carrier được modulate bởi slow envelope. Beat phenomenon không cần thêm physics phức tạp để hiểu first-order; nó nằm ngay trong trig định danh (identity / 식별자).

> **Nối mạch:** Ở chặng này của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **Worked example: beat frequency** nêu quy tắc; **Liên kết kiến thức (knowledge connection / 지식 연결)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phần này nối lượng giác với rotation, complex numbers, Fourier và dao động. Hãy giữ identity như biểu hiện của cấu trúc chu kỳ thay vì học thuộc từng công thức.

Phần kết nối đặt lượng giác cạnh rotation, complex numbers, Fourier và dao động. Mục tiêu là thấy identity và harmonic không phải công thức rời mà là cùng một cấu trúc chu kỳ.

```text
unit circle
→ rotation matrix
→ identities
→ complex exponential
→ harmonic oscillator
→ Fourier basis
→ signal processing / control
```

Trong AI, positional encodings và spectral methods cũng dùng sinusoidal/frequency representations. Trong Physics, wave equations và quantum states thường decomposition theo modes. Trong Finance, periodic/seasonal components có thể được modeled bằng Fourier features, nhưng phải cẩn thận không nhầm periodic fit với nhân quả (causal / 인과적) cơ chế (mechanism / 메커니즘).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Liên kết kiến thức (knowledge connection / 지식 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> Sine và cosine là coordinates của rotation. Identities là algebra của rotations; harmonics là repeated rotations ở different frequencies; Fourier phân tích (analysis / 분석) là decomposition theo orthogonal rotating modes.

> **Nối mạch:** Trong **Đồng nhất thức lượng giác, phương trình lượng giác và dao động điều hòa**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Dùng chung (common / 공통) Misconceptions

Degrees và radians không interchangeable trong calculus. `arcsin(sin x)` không luôn bằng `x` vì inverse chỉ dùng principal branch. định danh (identity / 식별자) không phải equation. Phase shift không đổi frequency. Một Fourier decomposition không tự chứng minh tín hiệu (signal / 신호) thật sự được tạo bởi independent sinusoidal causes.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
