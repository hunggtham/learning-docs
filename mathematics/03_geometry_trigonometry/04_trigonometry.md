# Lượng giác: từ tam giác đến rotation, phase và wave

Lượng giác (Trigonometry / 삼각함수) thường được giới thiệu bằng tam giác vuông, nhưng đó chỉ là cửa vào. Bản chất sâu hơn của lượng giác là **mô tả orientation và rotation bằng numbers**. Khi một point quay quanh circle, hai coordinates của nó thay đổi theo sine và cosine. Từ geometry này phát sinh triangle ratios, periodic functions, rotation matrices, wave models, Fourier analysis và nhiều công cụ trong graphics, robotics, signal processing và physics.

> Sine và cosine không phải hai công thức ngẫu nhiên gắn với tam giác. Chúng là hai coordinates của chuyển động quay.

## Vì sao ratio trong tam giác chỉ phụ thuộc angle?

Xét hai right triangles có cùng acute angle `θ`. Hai tam giác đó similar, nên corresponding side lengths chỉ khác nhau bởi một common scale factor.

Nếu một triangle được scale factor `k`, opposite, adjacent và hypotenuse đều nhân `k`. Vì thế ratios như

```math
\frac{opposite}{hypotenuse}
```

không đổi.

Đó là lý do ta có thể define

```math
\sin\theta=\frac{opposite}{hypotenuse},
```

```math
\cos\theta=\frac{adjacent}{hypotenuse},
```

```math
\tan\theta=\frac{opposite}{adjacent}.
```

Tangent cũng là ratio

```math
\tan\theta=\frac{\sin\theta}{\cos\theta}
```

khi `cosθ≠0`.

Điểm cần nhớ không phải mnemonic SOH-CAH-TOA tự thân, mà là **similarity makes these ratios invariant under scale**.

## Right-triangle definition chưa đủ

Triangle definition works naturally cho acute angles từ `0` đến `π/2`. Nhưng trong real systems ta cần angles lớn hơn `90°`, negative rotations, nhiều vòng quay và continuous phase.

Một robot arm có thể quay `-30°`; một signal có phase `5π`; một point có thể rotate nhiều vòng. Unit circle mở rộng trigonometry sang toàn bộ real line.

## Unit circle: definition cốt lõi

Xét circle radius 1 centered at origin. Bắt đầu từ point `(1,0)` và rotate counterclockwise angle `θ`.

Point mới có coordinates

```math
(\cos\theta,\sin\theta).
```

Đây là definition powerful hơn triangle ratio:

- `cosθ` là horizontal coordinate;
- `sinθ` là vertical coordinate.

Với this viewpoint, dấu của sine/cosine tự nhiên thay đổi theo quadrant.

Trong quadrant II, x-coordinate âm nên cosine âm, trong khi y-coordinate dương nên sine dương. Không cần memorize bảng dấu nếu hình dung point trên circle.

## Pythagorean identity xuất hiện từ circle geometry

Mọi point `(x,y)` trên unit circle thỏa

```math
x^2+y^2=1.
```

Substitute

```math
x=\cos\theta,\qquad y=\sin\theta
```

cho

```math
\cos^2\theta+\sin^2\theta=1.
```

Đây không phải identity để học thuộc riêng. Nó là Pythagorean theorem applied tới radius-1 triangle được tạo bởi point trên unit circle.

Từ đó,

```math
1+\tan^2\theta=\sec^2\theta
```

cũng follow bằng cách chia cho `cos²θ` khi `cosθ≠0`.

## Radian: measure angle bằng geometry tự nhiên

Degree chia full circle thành 360 parts do historical convention. Radian (Radian / 라디안) được định nghĩa trực tiếp từ arc length:

```math
\theta=\frac{s}{r},
```

trong đó `s` là arc length và `r` là radius.

Nếu arc length bằng radius, angle là `1` radian.

Full circle có arc length `2πr`, nên full rotation là

```math
\theta=\frac{2\pi r}{r}=2\pi.
```

Do đó

```math
360^\circ=2\pi\text{ rad}.
```

và

```math
180^\circ=\pi\text{ rad}.
```

Radian là dimensionless ratio và phù hợp trực tiếp với calculus.

## Vì sao calculus muốn radians?

Xét small angle `h` measured in radians. Trên unit circle, arc length bằng `h`. Khi `h→0`, geometry cho

```math
\frac{\sin h}{h}\to1.
```

Limit này dẫn tới derivative

```math
\frac{d}{dx}\sin x=\cos x.
```

Nếu `x` measured in degrees, conversion factor `π/180` sẽ xuất hiện:

```math
\frac{d}{dx}\sin(x^\circ)=\frac{\pi}{180}\cos(x^\circ).
```

Vì vậy radian không chỉ là một unit khác; nó là angle measure làm local geometry của circle có scale tự nhiên.

## Periodicity đến từ quay trọn vòng

Sau full rotation `2π`, point trở lại position cũ. Vì thế

```math
\sin(\theta+2\pi)=\sin\theta,
```

```math
\cos(\theta+2\pi)=\cos\theta.
```

Sine và cosine là periodic functions với period `2π`.

Tangent có period `π` vì direction slope lặp sau half-turn:

```math
\tan(\theta+\pi)=\tan\theta.
```

Period không phải arbitrary property của graph; nó đến từ rotational symmetry.

## Reference angles và symmetry

Unit circle cho phép derive values ngoài first quadrant bằng symmetry.

Ví dụ

```math
\sin(\pi-\theta)=\sin\theta,
```

vì points đối xứng qua y-axis giữ same y-coordinate.

Trong khi

```math
\cos(\pi-\theta)=-\cos\theta,
```

vì x-coordinate đổi sign.

Trigonometric identities thường trở nên dễ hiểu hơn khi nghĩ bằng transformations của circle thay vì symbolic manipulation thuần túy.

## Tangent như slope của direction

Với point on unit circle,

```math
\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{y}{x}.
```

Đây chính là slope của ray từ origin đến point khi `x≠0`.

Do đó tangent naturally link angle với slope.

Một line có direction angle `θ` relative x-axis có slope

```math
m=\tan\theta.
```

Khi line vertical, `cosθ=0` và tangent undefined — đúng với fact vertical line có undefined/infinite slope trong standard Cartesian representation.

## Inverse trigonometric functions

Nếu sine/cosine map nhiều angles tới same value do periodicity, chúng không invertible trên toàn `R`.

Để define inverse, ta restrict domain.

Arcsine

```math
\arcsin x
```

trả principal angle trong

```math
[-\pi/2,\pi/2]
```

whose sine equals `x`.

Arccos returns principal angle in `[0,π]`.

Arctangent typically returns angle in `(-π/2,π/2)`.

Notation `sin^{-1}x` thường nghĩa arcsin, **không phải** reciprocal `1/sin x`. Reciprocal của sine là cosecant `csc x`.

## From circle motion to sinusoidal motion

Imagine point rotating uniformly around circle radius `A` với angular position

```math
\theta(t)=\omega t+\phi.
```

Vertical coordinate là

```math
y(t)=A\sin(\omega t+\phi).
```

Horizontal coordinate là

```math
x(t)=A\cos(\omega t+\phi).
```

Một sinusoid vì thế là **projection của uniform circular motion lên một axis**.

Đây là mental model mạnh cho waves và oscillations.

## Amplitude, angular frequency, phase

General sinusoid:

```math
y(t)=A\sin(\omega t+\phi).
```

`A` là amplitude: maximum magnitude relative equilibrium.

`ω` là angular frequency measured radians/time.

`φ` là phase offset: vị trí trong cycle tại `t=0`.

Full cycle xảy ra khi argument tăng `2π`:

```math
\omega T=2\pi,
```

nên period

```math
T=\frac{2\pi}{|\omega|}.
```

Frequency cycles/time là

```math
f=\frac1T=\frac{|\omega|}{2\pi}.
```

Do đó

```math
\omega=2\pi f.
```

`f` đếm cycles; `ω` đo radians accumulated per unit time.

## Phase không chỉ là “dịch graph”

Hai signals

```math
y_1=A\sin(\omega t)
```

và

```math
y_2=A\sin(\omega t+\phi)
```

có same frequency/amplitude nhưng khác alignment trong cycle.

Trong AC circuits, phase difference giữa voltage/current ảnh hưởng real power. Trong wave interference, relative phase quyết định constructive hay destructive combination.

Phase vì thế represent timing/orientation trong periodic state, không chỉ cosmetic horizontal shift.

## Addition formulas từ rotation composition

Rotation by `α` rồi `β` tương đương rotation by `α+β`.

Rotation matrix là

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Composition nói

```math
R(\alpha)R(\beta)=R(\alpha+\beta).
```

Multiply matrices và compare entries cho:

```math
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-\sin\alpha\sin\beta,
```

```math
\sin(\alpha+\beta)
=
\sin\alpha\cos\beta+\cos\alpha\sin\beta.
```

Addition formulas vì vậy encode composition law của rotations.

Đây là explanation structural tốt hơn memorizing sign patterns.

## Rotation matrix: vì sao entries là sine và cosine?

Standard basis vectors là

```math
e_1=(1,0),\qquad e_2=(0,1).
```

Rotate `e_1` by `θ`:

```math
R(\theta)e_1=(\cos\theta,\sin\theta).
```

Rotate `e_2` by `θ`:

```math
R(\theta)e_2=(-\sin\theta,\cos\theta).
```

Matrix columns chính là images của basis vectors, nên

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Matrix không phải formula được “phát minh” riêng; nó là coordinate representation của rotation transformation.

## Rotation bảo toàn length và angle

Rotation matrix thỏa

```math
R(\theta)^TR(\theta)=I.
```

Do đó

```math
\|Rv\|^2
=v^TR^TRv
=v^Tv
=\|v\|^2.
```

Rotation giữ Euclidean length. Nó cũng giữ dot products, nên giữ angles.

Đây là bridge giữa trigonometry và orthogonal matrices trong linear algebra.

## Dot product và cosine similarity

Với nonzero vectors `u,v`:

```math
u\cdot v=\|u\|\|v\|\cos\theta.
```

Solve for cosine:

```math
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}.
```

Cosine đo alignment direction:

- `1`: same direction;
- `0`: orthogonal;
- `-1`: opposite direction.

Cosine similarity trong information retrieval/embeddings dùng same geometry, dù high-dimensional vectors không thể visualise trực tiếp như arrows 2D.

## Law of cosines: Pythagoras với non-right angle

Cho triangle sides `a,b,c`, angle `C` between sides `a,b`:

```math
c^2=a^2+b^2-2ab\cos C.
```

Nếu `C=π/2`, `cos C=0`, ta recover Pythagorean theorem:

```math
c^2=a^2+b^2.
```

Law of cosines có thể derive từ vector subtraction:

```math
\|u-v\|^2
=\|u\|^2+\|v\|^2-2u\cdot v.
```

Substitute

```math
u\cdot v=\|u\|\|v\|\cos C.
```

Điều này cho thấy triangle geometry và vector algebra là cùng structure được viết bằng hai languages.

## Law of sines

Cho triangle sides `a,b,c` đối diện angles `A,B,C`:

```math
\frac{a}{\sin A}
=
\frac{b}{\sin B}
=
\frac{c}{\sin C}
=2R,
```

trong đó `R` là circumradius.

Law of sines useful khi biết angle-side pairs. Nó cũng nối triangle với circle vì constant `2R` đến từ circumcircle geometry.

## Triangulation và localization

Nếu biết baseline và angles tới target, ta có thể infer position/distance qua trigonometric constraints.

Surveying dùng triangulation từ lâu. Computer vision recover geometry từ camera rays. Robotics dùng bearings/ranges. GPS chính xác hơn là trilateration/pseudorange geometry chứ không đơn giản “triangulation”, nhưng cùng idea broader: position được infer từ geometric constraints.

Modeling language quan trọng: angle measurements → trigonometric constraints → solve unknown geometry.

## Small-angle approximation

Khi `θ` nhỏ và measured in radians:

```math
\sin\theta\approx\theta,
```

```math
\tan\theta\approx\theta,
```

```math
\cos\theta\approx1-\frac{\theta^2}{2}.
```

Các approximations đến từ Taylor series.

Ví dụ với `θ=0.01` rad,

```math
\sin(0.01)\approx0.00999983,
```

rất gần `0.01`.

Small-angle approximations simplify pendulum equations, optics và control models, nhưng chỉ hợp lệ khi angle đủ nhỏ. Dùng degree value trực tiếp sẽ sai vì approximation assume radians.

## Harmonic oscillator và trigonometry

Simple harmonic equation

```math
x''+\omega^2x=0
```

có solutions

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Tại sao sine/cosine xuất hiện? Vì differentiation hai lần cho lại negative original function:

```math
\frac{d^2}{dt^2}\sin(\omega t)
=-\omega^2\sin(\omega t).
```

Rotation geometry và differential equations gặp nhau tại cùng periodic structure.

## Euler's formula: rotation bằng complex exponential

Một connection sâu là

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Complex multiplication by `e^{iθ}` rotate point trên complex plane angle `θ` mà giữ magnitude.

Điều này làm sine/cosine, exponentials và rotations trở thành facets của cùng object.

Từ Euler's formula:

```math
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},
```

```math
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
```

Đây là nền cho Fourier analysis và signal processing.

## Fourier viewpoint: periodic pattern như tổng của rotations

Fourier theory nói broad classes of signals có thể decompose thành sums của sine/cosine hoặc complex exponentials với different frequencies.

Một waveform phức tạp có thể được represent như combination:

```math
f(t)\approx
\sum_k
A_k\cos(\omega_k t+\phi_k).
```

Trigonometry vì thế không chỉ model one wave; nó cung cấp coordinate system cho whole signal space.

## Aliasing: sampling phải tôn trọng frequency

Nếu continuous sinusoid được sample quá chậm, different frequencies có thể produce same sample pattern. Đây là aliasing.

Nyquist principle yêu cầu sampling frequency lớn hơn twice highest frequency component trong ideal band-limited setting:

```math
f_s>2f_{max}.
```

Connection này cho thấy frequency/period không chỉ là textbook parameters; chúng quyết định digital representation có preserve signal information hay không.

## Angles trong 3D: cần vectors/matrices hơn là một `θ`

Trong 2D, one angle đủ describe orientation. Trong 3D, rotation phức tạp hơn vì rotations quanh different axes không commute.

Euler angles, rotation matrices và quaternions là các representations phổ biến. Trigonometric functions vẫn xuất hiện trong matrices/quaternions, nhưng single-angle intuition không còn đủ.

Graphics, robotics và AR/VR vì thế nối trigonometry với linear algebra và group structure của rotations.

## Degree/radian bug là model-unit bug

Nếu API `sin()` mong radians nhưng code truyền degrees, formula algebraically đúng nhưng unit semantics sai.

Ví dụ

```text
sin(90)
```

trong most programming libraries nghĩa `sin(90 radians)`, không phải `sin(90°)=1`.

Convert:

```math
\theta_{rad}=\theta_{deg}\frac{\pi}{180}.
```

Unit mismatch là một trong những bugs dễ xảy ra nhất khi trigonometry đi vào code.

## Knowledge Connection — trigonometry và embeddings

Cosine similarity không quan tâm vector magnitudes trực tiếp, chỉ normalized directional alignment:

```math
\operatorname{cosSim}(u,v)
=\frac{u\cdot v}{\|u\|\|v\|}.
```

Trong embedding space, “angle” không phải physical angle nhưng geometry vẫn hợp lệ trong high-dimensional inner-product space.

Điều này là ví dụ classic của concept sinh ra từ circle/triangle nhưng generalize thành tool trong AI.

## Knowledge Connection — phase và distributed/signal systems

Hai periodic processes có same frequency nhưng phase lệch có thể reinforce hoặc cancel khi combine. Trong AC power, communication và control, relative phase mang information về timing.

Trong software, ta không nên kéo analogy quá xa, nhưng periodic jobs với same cadence cũng có phase/offset concept: staggering phase có thể tránh synchronized load spikes. Mathematical phase language giúp reason về cyclic timing.

## Mental Model

> Hãy xem sine và cosine như **coordinates của rotation**. Tam giác chỉ là một local geometric view; unit circle mở rộng chúng cho mọi angle. Khi rotation diễn ra đều theo time, projection tạo sinusoidal wave. Khi nhiều rotations/frequencies cộng lại, ta tiến tới Fourier analysis. Trigonometry vì thế là bridge giữa geometry, linear algebra, differential equations và signal processing.

## Common Misconceptions

**“Trigonometry chỉ dùng cho triangles.”** Triangle ratios là entry point. Unit circle/rotation mới là framework general cho periodic motion và waves.

**“Degree và radian chỉ khác cách ghi.”** Chúng convert được, nhưng calculus formulas và small-angle approximations có clean form khi angle measured radians.

**“`sin^{-1}` là `1/sin`.”** Trong common notation, `sin^{-1}` nghĩa arcsin; reciprocal là `csc`.

**“Tangent luôn là một finite ratio.”** `tanθ` undefined khi `cosθ=0`, tương ứng vertical direction có undefined slope.

**“Amplitude lớn hơn nghĩa frequency cao hơn.”** Amplitude và frequency là independent parameters trong sinusoidal model.

**“Hai waves cùng frequency thì giống nhau.”** Phase và amplitude vẫn có thể khác, tạo rất different combined behavior.

**“Cosine similarity bằng 1 nghĩa vectors bằng nhau.”** Nó chỉ nói same direction; magnitudes có thể khác nếu vectors chưa normalized.

**“Rotation order trong 3D không quan trọng.”** 3D rotations generally do not commute. Rotate X then Y thường khác Y then X.