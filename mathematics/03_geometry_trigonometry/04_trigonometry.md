# Lượng giác: từ tam giác đến rotation, phase và wave

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lượng giác: từ tam giác đến rotation, phase và wave**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao ratio trong tam giác chỉ phụ thuộc angle?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Right-triangle definition chưa đủ** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối trigonometry với angle, unit circle và periodicity, để hàm lượng giác gắn với hình học và dao động.

Lượng giác (Trigonometry / 삼각함수) thường được giới thiệu bằng tam giác vuông, nhưng đó chỉ là cửa vào. Bản chất sâu hơn của lượng giác là **mô tả orientation và rotation bằng numbers**. Khi một điểm (point / 지점) quay quanh circle, hai coordinates của nó thay đổi theo sine và cosine. Từ hình học (geometry / 기하학) này phát sinh triangle ratios, periodic functions, rotation matrices, wave các mô hình (models / 모델들), Fourier phân tích (analysis / 분석) và nhiều công cụ trong graphics, robotics, tín hiệu (signal / 신호) processing và physics.

> Sine và cosine không phải hai công thức ngẫu nhiên gắn với tam giác. Chúng là hai coordinates của chuyển động quay.

## Vì sao ratio trong tam giác chỉ phụ thuộc angle?

Xét hai right triangles có cùng acute angle `θ`. Hai tam giác đó similar, nên corresponding side lengths chỉ khác nhau bởi một dùng chung (common / 공통) quy mô (scale / 규모) factor.

Nếu một triangle được quy mô (scale / 규모) factor `k`, opposite, adjacent và hypotenuse đều nhân `k`. Vì thế ratios như

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

Điểm cần nhớ không phải mnemonic SOH-CAH-TOA tự thân, mà là **similarity makes these ratios bất biến (invariant / 불변식) under quy mô (scale / 규모)**.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Right-triangle definition chưa đủ** tiếp nhận điểm tựa từ **Vì sao ratio trong tam giác chỉ phụ thuộc angle?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị (unit / 단위) circle: definition cốt lõi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Right-triangle definition chưa đủ

Triangle definition works naturally cho acute angles từ `0` đến `π/2`. Nhưng trong real các hệ thống (systems / 시스템들) ta cần angles lớn hơn `90°`, negative rotations, nhiều vòng quay và continuous phase.

Một robot arm có thể quay `-30°`; một tín hiệu (signal / 신호) có phase `5π`; một điểm (point / 지점) có thể rotate nhiều vòng. đơn vị (unit / 단위) circle mở rộng trigonometry sang toàn bộ real line.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Đơn vị (unit / 단위) circle: definition cốt lõi** tiếp nhận điểm tựa từ **Right-triangle definition chưa đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pythagorean định danh (identity / 식별자) xuất hiện từ circle hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị (unit / 단위) circle: definition cốt lõi

Xét circle radius 1 centered at origin. Bắt đầu từ điểm (point / 지점) `(1,0)` và rotate counterclockwise angle `θ`.

Điểm (point / 지점) mới có coordinates

```math
(\cos\theta,\sin\theta).
```

Đây là definition powerful hơn triangle ratio:

- `cosθ` là horizontal coordinate;
- `sinθ` là vertical coordinate.

Với this viewpoint, dấu của sine/cosine tự nhiên thay đổi theo quadrant.

Trong quadrant II, x-coordinate âm nên cosine âm, trong khi y-coordinate dương nên sine dương. Không cần memorize bảng dấu nếu hình dung điểm (point / 지점) trên circle.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Pythagorean định danh (identity / 식별자) xuất hiện từ circle hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Đơn vị (unit / 단위) circle: definition cốt lõi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Radian: measure angle bằng hình học (geometry / 기하학) tự nhiên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pythagorean định danh (identity / 식별자) xuất hiện từ circle hình học (geometry / 기하학)

Mọi điểm (point / 지점) `(x,y)` trên đơn vị (unit / 단위) circle thỏa

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

Đây không phải định danh (identity / 식별자) để học thuộc riêng. Nó là Pythagorean theorem applied tới radius-1 triangle được tạo bởi điểm (point / 지점) trên đơn vị (unit / 단위) circle.

Từ đó,

```math
1+\tan^2\theta=\sec^2\theta
```

cũng follow bằng cách chia cho `cos²θ` khi `cosθ≠0`.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Radian: measure angle bằng hình học (geometry / 기하학) tự nhiên** tiếp nhận điểm tựa từ **Pythagorean định danh (identity / 식별자) xuất hiện từ circle hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao calculus muốn radians?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Radian: measure angle bằng hình học (geometry / 기하학) tự nhiên

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

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Vì sao calculus muốn radians?** tiếp nhận điểm tựa từ **Radian: measure angle bằng hình học (geometry / 기하학) tự nhiên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Periodicity đến từ quay trọn vòng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao calculus muốn radians?

Xét small angle `h` measured in radians. Trên đơn vị (unit / 단위) circle, arc length bằng `h`. Khi `h→0`, hình học (geometry / 기하학) cho

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

Vì vậy radian không chỉ là một đơn vị (unit / 단위) khác; nó là angle measure làm cục bộ (local / 로컬) hình học (geometry / 기하학) của circle có quy mô (scale / 규모) tự nhiên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Periodicity đến từ quay trọn vòng** tiếp nhận điểm tựa từ **Vì sao calculus muốn radians?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tham chiếu (reference / 참조) angles và symmetry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Periodicity đến từ quay trọn vòng

Sau full rotation `2π`, điểm (point / 지점) trở lại position cũ. Vì thế

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

Period không phải arbitrary thuộc tính (property / 속성) của đồ thị (graph / 그래프); nó đến từ rotational symmetry.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, sau nội dung của **Periodicity đến từ quay trọn vòng**, **Tham chiếu (reference / 참조) angles và symmetry** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Tangent như slope của direction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tham chiếu (reference / 참조) angles và symmetry

Đơn vị (unit / 단위) circle cho phép derive values ngoài first quadrant bằng symmetry.

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

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Tangent như slope của direction** tiếp nhận điểm tựa từ **Tham chiếu (reference / 참조) angles và symmetry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inverse trigonometric functions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tangent như slope của direction

Với điểm (point / 지점) on đơn vị (unit / 단위) circle,

```math
\tan\theta=\frac{\sin\theta}{\cos\theta}=\frac{y}{x}.
```

Đây chính là slope của ray từ origin đến điểm (point / 지점) khi `x≠0`.

Do đó tangent naturally link angle với slope.

Một line có direction angle `θ` relative x-axis có slope

```math
m=\tan\theta.
```

Khi line vertical, `cosθ=0` và tangent undefined — đúng với fact vertical line có undefined/infinite slope trong tiêu chuẩn (standard / 표준) Cartesian biểu diễn (representation / 표현).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Inverse trigonometric functions** tiếp nhận điểm tựa từ **Tangent như slope của direction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **From circle motion to sinusoidal motion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inverse trigonometric functions

Nếu sine/cosine map nhiều angles tới same giá trị (value / 값) do periodicity, chúng không invertible trên toàn `R`.

Để define inverse, ta restrict lĩnh vực (domain / 도메인).

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

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **From circle motion to sinusoidal motion** tiếp nhận điểm tựa từ **Inverse trigonometric functions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Amplitude, angular frequency, phase** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## From circle motion to sinusoidal motion

Imagine điểm (point / 지점) rotating uniformly around circle radius `A` với angular position

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

Đây là mô hình tư duy (mental model / 사고 모델) mạnh cho waves và oscillations.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Amplitude, angular frequency, phase** tiếp nhận điểm tựa từ **From circle motion to sinusoidal motion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phase không chỉ là “dịch đồ thị (graph / 그래프)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Amplitude, angular frequency, phase

General sinusoid:

```math
y(t)=A\sin(\omega t+\phi).
```

`A` là amplitude: maximum magnitude relative equilibrium.

`ω` là angular frequency measured radians/thời gian (time / 시간).

`φ` là phase offset: vị trí trong cycle tại `t=0`.

Full cycle xảy ra khi argument tăng `2π`:

```math
\omega T=2\pi,
```

nên period

```math
T=\frac{2\pi}{|\omega|}.
```

Frequency cycles/thời gian (time / 시간) là

```math
f=\frac1T=\frac{|\omega|}{2\pi}.
```

Do đó

```math
\omega=2\pi f.
```

`f` đếm cycles; `ω` đo radians accumulated per đơn vị (unit / 단위) thời gian (time / 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Phase không chỉ là “dịch đồ thị (graph / 그래프)”** tiếp nhận điểm tựa từ **Amplitude, angular frequency, phase** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Addition formulas từ rotation composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phase không chỉ là “dịch đồ thị (graph / 그래프)”

Hai signals

```math
y_1=A\sin(\omega t)
```

và

```math
y_2=A\sin(\omega t+\phi)
```

có same frequency/amplitude nhưng khác alignment trong cycle.

Trong AC circuits, phase difference giữa voltage/hiện tại (current / 현재) ảnh hưởng real power. Trong wave interference, relative phase quyết định constructive hay destructive combination.

Phase vì thế represent timing/orientation trong periodic trạng thái (state / 상태), không chỉ cosmetic horizontal shift.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Addition formulas từ rotation composition** tiếp nhận điểm tựa từ **Phase không chỉ là “dịch đồ thị (graph / 그래프)”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rotation ma trận (matrix / 행렬): vì sao entries là sine và cosine?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Addition formulas từ rotation composition

Rotation by `α` rồi `β` tương đương rotation by `α+β`.

Rotation ma trận (matrix / 행렬) là

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

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Rotation ma trận (matrix / 행렬): vì sao entries là sine và cosine?** tiếp nhận điểm tựa từ **Addition formulas từ rotation composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rotation bảo toàn length và angle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rotation ma trận (matrix / 행렬): vì sao entries là sine và cosine?

Tiêu chuẩn (standard / 표준) basis vectors là

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

Ma trận (matrix / 행렬) columns chính là images của basis vectors, nên

```math
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
```

Ma trận (matrix / 행렬) không phải formula được “phát minh” riêng; nó là coordinate biểu diễn (representation / 표현) của rotation transformation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Rotation bảo toàn length và angle** tiếp nhận điểm tựa từ **Rotation ma trận (matrix / 행렬): vì sao entries là sine và cosine?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dot sản phẩm (product / 제품) và cosine similarity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rotation bảo toàn length và angle

Rotation ma trận (matrix / 행렬) thỏa

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

Đây là cầu nối (bridge / 브리지) giữa trigonometry và orthogonal matrices trong tuyến tính (linear / 선형) algebra.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Dot sản phẩm (product / 제품) và cosine similarity** tiếp nhận điểm tựa từ **Rotation bảo toàn length và angle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Law of cosines: Pythagoras với non-right angle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dot sản phẩm (product / 제품) và cosine similarity

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

Cosine similarity trong thông tin (information / 정보) retrieval/embeddings dùng same hình học (geometry / 기하학), dù high-dimensional vectors không thể visualise trực tiếp như arrows 2D.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Law of cosines: Pythagoras với non-right angle** tiếp nhận điểm tựa từ **Dot sản phẩm (product / 제품) và cosine similarity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Law of sines** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Law of cosines: Pythagoras với non-right angle

Cho triangle sides `a,b,c`, angle `C` between sides `a,b`:

```math
c^2=a^2+b^2-2ab\cos C.
```

Nếu `C=π/2`, `cos C=0`, ta recover Pythagorean theorem:

```math
c^2=a^2+b^2.
```

Law of cosines có thể derive từ véc-tơ (vector / 벡터) subtraction:

```math
\|u-v\|^2
=\|u\|^2+\|v\|^2-2u\cdot v.
```

Substitute

```math
u\cdot v=\|u\|\|v\|\cos C.
```

Điều này cho thấy triangle hình học (geometry / 기하학) và véc-tơ (vector / 벡터) algebra là cùng cấu trúc (structure / 구조) được viết bằng hai languages.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Law of sines** tiếp nhận điểm tựa từ **Law of cosines: Pythagoras với non-right angle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Triangulation và localization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Law of sines useful khi biết angle-side pairs. Nó cũng nối triangle với circle vì constant `2R` đến từ circumcircle hình học (geometry / 기하학).

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Triangulation và localization** tiếp nhận điểm tựa từ **Law of sines** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Small-angle approximation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Triangulation và localization

Nếu biết baseline và angles tới mục tiêu (target / 대상), ta có thể infer position/distance qua trigonometric các ràng buộc (constraints / 제약조건들).

Surveying dùng triangulation từ lâu. Computer vision recover hình học (geometry / 기하학) từ camera rays. Robotics dùng bearings/ranges. GPS chính xác hơn là trilateration/pseudorange hình học (geometry / 기하학) chứ không đơn giản “triangulation”, nhưng cùng idea broader: position được infer từ geometric các ràng buộc (constraints / 제약조건들).

Modeling ngôn ngữ (language / 언어) quan trọng: angle measurements → trigonometric các ràng buộc (constraints / 제약조건들) → solve unknown hình học (geometry / 기하학).

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Small-angle approximation** tiếp nhận điểm tựa từ **Triangulation và localization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Harmonic oscillator và trigonometry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Small-angle approximations simplify pendulum equations, optics và điều khiển (control / 제어) các mô hình (models / 모델들), nhưng chỉ hợp lệ khi angle đủ nhỏ. Dùng degree giá trị (value / 값) trực tiếp sẽ sai vì approximation assume radians.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Harmonic oscillator và trigonometry** tiếp nhận điểm tựa từ **Small-angle approximation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Euler's formula: rotation bằng complex exponential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Harmonic oscillator và trigonometry

Simple harmonic equation

```math
x''+\omega^2x=0
```

có solutions

```math
x(t)=A\cos(\omega t)+B\sin(\omega t).
```

Tại sao sine/cosine xuất hiện? Vì differentiation hai lần cho lại negative original hàm (function / 함수):

```math
\frac{d^2}{dt^2}\sin(\omega t)
=-\omega^2\sin(\omega t).
```

Rotation hình học (geometry / 기하학) và differential equations gặp nhau tại cùng periodic cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Euler's formula: rotation bằng complex exponential** tiếp nhận điểm tựa từ **Harmonic oscillator và trigonometry** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fourier viewpoint: periodic mẫu (pattern / 패턴) như tổng của rotations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Euler's formula: rotation bằng complex exponential

Một liên kết (connection / 연결) sâu là

```math
e^{i\theta}=\cos\theta+i\sin\theta.
```

Complex multiplication by `e^{iθ}` rotate điểm (point / 지점) trên complex plane angle `θ` mà giữ magnitude.

Điều này làm sine/cosine, exponentials và rotations trở thành facets của cùng đối tượng (object / 객체).

Từ Euler's formula:

```math
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},
```

```math
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
```

Đây là nền cho Fourier phân tích (analysis / 분석) và tín hiệu (signal / 신호) processing.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Fourier viewpoint: periodic mẫu (pattern / 패턴) như tổng của rotations** tiếp nhận điểm tựa từ **Euler's formula: rotation bằng complex exponential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Aliasing: sampling phải tôn trọng frequency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fourier viewpoint: periodic mẫu (pattern / 패턴) như tổng của rotations

Fourier lý thuyết (theory / 이론) nói broad classes of signals có thể decompose thành sums của sine/cosine hoặc complex exponentials với different frequencies.

Một waveform phức tạp có thể được represent như combination:

```math
f(t)\approx
\sum_k
A_k\cos(\omega_k t+\phi_k).
```

Trigonometry vì thế không chỉ mô hình (model / 모델) one wave; nó cung cấp coordinate hệ thống (system / 시스템) cho whole tín hiệu (signal / 신호) không gian (space / 공간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Aliasing: sampling phải tôn trọng frequency** tiếp nhận điểm tựa từ **Fourier viewpoint: periodic mẫu (pattern / 패턴) như tổng của rotations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Angles trong 3D: cần vectors/matrices hơn là một θ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aliasing: sampling phải tôn trọng frequency

Nếu continuous sinusoid được mẫu (sample / 표본) quá chậm, different frequencies có thể produce same mẫu (sample / 표본) mẫu (pattern / 패턴). Đây là aliasing.

Nyquist principle yêu cầu sampling frequency lớn hơn twice highest frequency thành phần (component / 컴포넌트) trong ideal band-limited setting:

```math
f_s>2f_{max}.
```

Liên kết (connection / 연결) này cho thấy frequency/period không chỉ là textbook parameters; chúng quyết định digital biểu diễn (representation / 표현) có preserve tín hiệu (signal / 신호) thông tin (information / 정보) hay không.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Angles trong 3D: cần vectors/matrices hơn là một θ** tiếp nhận điểm tựa từ **Aliasing: sampling phải tôn trọng frequency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Degree/radian bug là model-unit bug** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Angles trong 3D: cần vectors/matrices hơn là một `θ`

Trong 2D, one angle đủ describe orientation. Trong 3D, rotation phức tạp hơn vì rotations quanh different axes không commute.

Euler angles, rotation matrices và quaternions là các representations phổ biến. Trigonometric functions vẫn xuất hiện trong matrices/quaternions, nhưng single-angle intuition không còn đủ.

Graphics, robotics và AR/VR vì thế nối trigonometry với tuyến tính (linear / 선형) algebra và group cấu trúc (structure / 구조) của rotations.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Degree/radian bug là model-unit bug** tiếp nhận điểm tựa từ **Angles trong 3D: cần vectors/matrices hơn là một θ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — trigonometry và embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Degree/radian bug là model-unit bug

Nếu API `sin()` mong radians nhưng mã (code / 코드) truyền degrees, formula algebraically đúng nhưng đơn vị (unit / 단위) ngữ nghĩa (semantics / 의미론) sai.

Ví dụ

```text
sin(90)
```

trong most programming libraries nghĩa `sin(90 radians)`, không phải `sin(90°)=1`.

Convert:

```math
\theta_{rad}=\theta_{deg}\frac{\pi}{180}.
```

Đơn vị (unit / 단위) mismatch là một trong những bugs dễ xảy ra nhất khi trigonometry đi vào mã (code / 코드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, sau nội dung của **Degree/radian bug là model-unit bug**, **Liên kết kiến thức (knowledge connection / 지식 연결) — trigonometry và embeddings** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결) — phase và phân tán (distributed / 분산)/tín hiệu (signal / 신호) các hệ thống (systems / 시스템들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결) — trigonometry và embeddings

Cosine similarity không quan tâm véc-tơ (vector / 벡터) magnitudes trực tiếp, chỉ normalized directional alignment:

```math
\operatorname{cosSim}(u,v)
=\frac{u\cdot v}{\|u\|\|v\|}.
```

Trong embedding không gian (space / 공간), “angle” không phải vật lý (physical / 물리적) angle nhưng hình học (geometry / 기하학) vẫn hợp lệ trong high-dimensional inner-product không gian (space / 공간).

Điều này là ví dụ classic của concept sinh ra từ circle/triangle nhưng generalize thành công cụ (tool / 도구) trong AI.

> **Chuyển mạch:** Trong **Lượng giác: từ tam giác đến rotation, phase và wave**, **Liên kết kiến thức (knowledge connection / 지식 연결) — phase và phân tán (distributed / 분산)/tín hiệu (signal / 신호) các hệ thống (systems / 시스템들)** tiếp nhận điểm tựa từ **Liên kết kiến thức (knowledge connection / 지식 연결) — trigonometry và embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết kiến thức (knowledge connection / 지식 연결) — phase và phân tán (distributed / 분산)/tín hiệu (signal / 신호) các hệ thống (systems / 시스템들)

Hai periodic processes có same frequency nhưng phase lệch có thể reinforce hoặc cancel khi combine. Trong AC power, communication và điều khiển (control / 제어), relative phase mang thông tin (information / 정보) về timing.

Trong software, ta không nên kéo analogy quá xa, nhưng periodic jobs với same cadence cũng có phase/offset concept: staggering phase có thể tránh synchronized tải (load / 로드) spikes. Mathematical phase ngôn ngữ (language / 언어) giúp reason về cyclic timing.

> **Chuyển mạch:** Ở chặng này của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Liên kết kiến thức (knowledge connection / 지식 연결) — phase và phân tán (distributed / 분산)/tín hiệu (signal / 신호) các hệ thống (systems / 시스템들)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Hãy xem sine và cosine như **coordinates của rotation**. Tam giác chỉ là một cục bộ (local / 로컬) geometric view; đơn vị (unit / 단위) circle mở rộng chúng cho mọi angle. Khi rotation diễn ra đều theo thời gian (time / 시간), projection tạo sinusoidal wave. Khi nhiều rotations/frequencies cộng lại, ta tiến tới Fourier phân tích (analysis / 분석). Trigonometry vì thế là cầu nối (bridge / 브리지) giữa hình học (geometry / 기하학), tuyến tính (linear / 선형) algebra, differential equations và tín hiệu (signal / 신호) processing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lượng giác: từ tam giác đến rotation, phase và wave**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Trigonometry chỉ dùng cho triangles.”** Triangle ratios là entry điểm (point / 지점). đơn vị (unit / 단위) circle/rotation mới là khung phần mềm (framework / 프레임워크) general cho periodic motion và waves.

**“Degree và radian chỉ khác cách ghi.”** Chúng convert được, nhưng calculus formulas và small-angle approximations có clean form khi angle measured radians.

**“`sin^{-1}` là `1/sin`.”** Trong dùng chung (common / 공통) notation, `sin^{-1}` nghĩa arcsin; reciprocal là `csc`.

**“Tangent luôn là một finite ratio.”** `tanθ` undefined khi `cosθ=0`, tương ứng vertical direction có undefined slope.

**“Amplitude lớn hơn nghĩa frequency cao hơn.”** Amplitude và frequency là independent parameters trong sinusoidal mô hình (model / 모델).

**“Hai waves cùng frequency thì giống nhau.”** Phase và amplitude vẫn có thể khác, tạo rất different combined hành vi (behavior / 동작).

**“Cosine similarity bằng 1 nghĩa vectors bằng nhau.”** Nó chỉ nói same direction; magnitudes có thể khác nếu vectors chưa normalized.

**“Rotation thứ tự (order / 순서) trong 3D không quan trọng.”** 3D rotations generally do not commute. Rotate X then Y thường khác Y then X.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
