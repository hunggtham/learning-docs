# Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen

Thuyết tương đối rộng (General Relativity / 일반상대성이론) thay đổi cách ta hiểu hấp dẫn: thay vì xem hấp dẫn chỉ là một lực nằm trên nền không gian–thời gian cố định, lý thuyết cho metric của không-thời gian trở thành một trường động lực học chịu ảnh hưởng của năng lượng và động lượng.

Cấu trúc khái niệm có thể tóm tắt bằng chuỗi:

```text
năng lượng–động lượng
→ hình học không-thời gian
→ geodesic và causal structure
→ chuyển động quan sát được
```

## Từ nguyên lý tương đương đến hình học

Nguyên lý tương đương (equivalence principle / 등가 원리) bắt đầu từ thực nghiệm rằng khối lượng quán tính và khối lượng hấp dẫn bằng nhau với độ chính xác rất cao.

Trong cơ học Newton,

```math
m_i\mathbf a=m_g\mathbf g.
```

Nếu

```math
m_i=m_g,
```

thì

```math
\mathbf a=\mathbf g
```

độc lập với khối lượng vật thử.

Điều này giải thích vì sao mọi vật rơi tự do gần cùng gia tốc trong cùng trường hấp dẫn khi bỏ lực cản.

Einstein đẩy quan sát này sâu hơn: trong một vùng đủ nhỏ, một observer rơi tự do có thể chọn hệ quy chiếu mà hiệu ứng của trường hấp dẫn gần như biến mất cục bộ.

Một người trong thang máy kín không thể bằng thí nghiệm cục bộ lý tưởng phân biệt hoàn toàn giữa:

```text
đứng yên trong trường hấp dẫn đều
```

và

```text
được gia tốc trong không gian không hấp dẫn
```

Điều này gợi ý hấp dẫn liên quan tới cấu trúc của hệ quy chiếu và hình học không-thời gian, chứ không chỉ là một force field kiểu Newton.

## Cục bộ phẳng không có nghĩa toàn cục phẳng

Ta có thể chọn tọa độ rơi tự do để làm các Christoffel symbols biến mất tại một điểm.

Nhưng ta không thể loại bỏ **tidal effects** trên một vùng hữu hạn nếu spacetime thật sự cong.

Đây là khác biệt giữa:

```text
connection / coordinate acceleration
```

và

```text
curvature / tidal gravity
```

Một elevator nhỏ có thể gần như không cảm thấy gravity, nhưng hai vật rơi cách nhau một khoảng vẫn có thể hội tụ hoặc phân kỳ.

## Metric

Metric tensor `g_{\mu\nu}(x)` xác định cách đo interval trong spacetime:

```math
ds^2=g_{\mu\nu}dx^\mu dx^\nu.
```

Với timelike worldline và convention dấu `(-,+,+,+)`, proper time thỏa

```math
c^2d\tau^2=-ds^2.
```

Metric quyết định:

```text
proper time
proper distance
light cone
causal structure
geodesic
```

Trong special relativity, metric Minkowski là cố định. Trong GR, metric là một field cần được giải từ Einstein equation.

## Geodesic

Một free-falling test particle đi theo geodesic:

```math
\frac{d^2x^\mu}{d\tau^2}
+
\Gamma^\mu_{\alpha\beta}
\frac{dx^\alpha}{d\tau}
\frac{dx^\beta}{d\tau}
=0.
```

Christoffel symbol là

```math
\Gamma^\mu_{\alpha\beta}
=
\frac12g^{\mu\nu}
\left(
\partial_\alpha g_{\nu\beta}
+
\partial_\beta g_{\nu\alpha}
-
\partial_\nu g_{\alpha\beta}
\right).
```

Geodesic equation có thể được suy ra bằng extremizing proper time của free particle.

Điều này tương tự principle of stationary action trong mechanics, nhưng action bây giờ được xây từ spacetime geometry.

## Vì sao phi hành gia trên quỹ đạo thấy không trọng lượng?

Phi hành gia trên ISS vẫn ở trong trường hấp dẫn mạnh đáng kể.

Họ thấy gần weightless vì cả tàu và cơ thể đều free-fall theo geodesic gần nhau.

Không có normal force từ sàn giữ cơ thể đứng yên như trên mặt đất.

Do đó cảm giác “trọng lượng” thường liên quan proper acceleration do support force hơn là chỉ magnitude của gravitational field theo Newton.

## Geodesic deviation: độ cong đo được bằng tidal motion

Xét hai geodesic gần nhau có separation vector `\xi^\mu` và four-velocity `u^\mu`.

Sự thay đổi tương đối của chúng được mô tả bởi geodesic-deviation equation:

```math
\frac{D^2\xi^\mu}{D\tau^2}
=
- R^\mu_{\ \nu\alpha\beta}
 u^\nu\xi^\alpha u^\beta.
```

`R^\mu_{\ \nu\alpha\beta}` là Riemann curvature tensor.

Đây là một trong những phương trình có ý nghĩa vật lý trực tiếp nhất trong GR:

```text
curvature
→ relative acceleration của nearby free-fall particles
```

Tidal stretching gần black hole, relative displacement do gravitational wave và nhiều phép đo gravity gradient đều liên hệ với cấu trúc này.

## Einstein field equation

Phương trình trường là

```math
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
```

Trong đó:

- `T_{\mu\nu}` là stress-energy tensor;
- `G_{\mu\nu}` được xây từ curvature;
- `\Lambda` là cosmological constant.

Stress-energy tensor không chỉ chứa mass density. Nó còn chứa energy density, momentum density, energy flux, pressure và shear stress.

Do đó trong GR, pressure cũng góp vào gravitational source.

## Conservation trong GR

Bianchi identity dẫn tới

```math
\nabla_\mu G^{\mu\nu}=0.
```

Kết hợp Einstein equation cho

```math
\nabla_\mu T^{\mu\nu}=0.
```

Đây là local covariant conservation law của stress-energy.

Trong curved spacetime tổng energy toàn cục không phải lúc nào cũng định nghĩa được theo cách đơn giản như trong Newtonian mechanics. Vì vậy không nên áp trực giác “một scalar total energy luôn tồn tại” vào mọi spacetime tùy ý.

## Giới hạn trường yếu

Một consistency check quan trọng là GR phải khôi phục Newtonian gravity khi:

```text
gravity weak
velocity << c
pressure << energy density
field thay đổi chậm
```

Viết metric gần Minkowski:

```math
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},
\qquad |h_{\mu\nu}|\ll1.
```

Trong Newtonian limit, thành phần thời gian có dạng gần

```math
g_{00}
\approx
-\left(1+\frac{2\Phi}{c^2}\right),
```

với `\Phi` là Newtonian gravitational potential.

Geodesic equation khi velocity nhỏ dẫn tới

```math
\frac{d^2\mathbf r}{dt^2}
\approx -\nabla\Phi.
```

Einstein equation đồng thời giảm gần về Poisson equation:

```math
\nabla^2\Phi=4\pi G\rho.
```

Đây là cầu nối chính xác giữa GR và Newtonian gravity.

## Gravitational time dilation trong trường yếu

Từ

```math
g_{00}
\approx
-\left(1+\frac{2\Phi}{c^2}\right),
```

với observer gần đứng yên,

```math
d\tau
\approx
\left(1+\frac{\Phi}{c^2}\right)dt.
```

Nếu `\Phi` âm sâu hơn trong gravitational well, proper time tích lũy chậm hơn so với vị trí có potential cao hơn.

Gần mặt đất với height difference `\Delta h` nhỏ,

```math
\frac{\Delta f}{f}
\approx
\frac{g\Delta h}{c^2}.
```

Hiệu ứng rất nhỏ nhưng đo được bằng atomic clocks.

## GPS

Satellite clocks chịu hai correction chính:

```text
special-relativistic time dilation do velocity
+
general-relativistic gravitational time shift do altitude
```

Hai hiệu ứng có dấu khác nhau và phải được tính đồng thời.

GPS vì vậy là một ví dụ engineering nơi relativity không phải “correction triết học” mà là thành phần của system design.

## Schwarzschild spacetime

Bên ngoài một body spherical, nonrotating, vacuum solution có metric

```math
ds^2
=-\left(1-\frac{r_s}{r}\right)c^2dt^2
+\left(1-\frac{r_s}{r}\right)^{-1}dr^2
+r^2d\Omega^2,
```

với

```math
r_s=\frac{2GM}{c^2}.
```

`r_s` là Schwarzschild radius.

Nếu vật thể bị compact bên trong scale này trong ideal GR solution, `r=r_s` là event horizon.

## Event horizon là causal boundary

Event horizon không phải bề mặt vật liệu.

Nó được định nghĩa toàn cục bởi causal structure: tín hiệu phát từ bên trong không thể tới future null infinity.

Một free-falling observer qua horizon của sufficiently large black hole không nhất thiết thấy local curvature vô hạn ngay tại horizon.

Một số coordinate systems như Schwarzschild coordinates có singular-looking components tại `r_s`, nhưng đây là coordinate singularity, không phải curvature singularity.

## Curvature singularity

Ở `r=0` của ideal Schwarzschild solution, curvature invariant như Kretschmann scalar diverges.

Điều này khác horizon.

Classical GR dự đoán breakdown tại singularity và cho thấy cần physics sâu hơn, thường được kỳ vọng liên quan quantum gravity.

Không nên diễn giải singularity như một vật thể đã được hiểu đầy đủ.

## Quỹ đạo và perihelion precession

GR sửa Newtonian orbital dynamics bằng các correction nhỏ trong weak field.

Với orbit gần Keplerian quanh mass `M`, perihelion advance mỗi vòng gần

```math
\Delta\phi
\approx
\frac{6\pi GM}
{a(1-e^2)c^2},
```

trong đó `a` là semi-major axis và `e` eccentricity.

Correction này giải thích phần anomalous precession của Mercury mà Newtonian perturbations từ các planet khác không giải thích hết.

## Deflection of light

Light đi theo null geodesic:

```math
ds^2=0.
```

Một light ray đi gần spherical mass với impact parameter `b` bị deflect gần

```math
\alpha
\approx
\frac{4GM}{bc^2}
```

trong weak field.

Gravitational lensing ngày nay là công cụ quan trọng để đo mass distribution, dark matter và distant galaxies.

## Shapiro time delay

Tín hiệu điện từ đi qua vùng gravitational potential sâu có travel time lớn hơn giá trị Euclidean-flat expectation.

Hiệu ứng Shapiro là một trong các classical tests của GR và hiện được đo với radar ranging cùng pulsar timing.

## Gravitational redshift

Photon phát sâu trong gravitational potential được quan sát ở vị trí cao hơn với frequency thấp hơn.

Ta có thể hiểu nó nhất quán qua comparison of local clock rates thay vì nói photon “mất energy một cách tuyệt đối” khi leo khỏi gravity.

Frequency luôn được đo bởi observer cụ thể.

## Gravitational waves

Linearize metric:

```math
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}.
```

Trong vacuum và gauge thích hợp, perturbation thỏa wave equation gần

```math
\Box h_{\mu\nu}=0.
```

Sóng hấp dẫn lan với tốc độ `c`.

Do conservation of mass-energy và momentum, lowest radiative multipole cho isolated source không phải monopole hay dipole mà là quadrupole.

Binary compact objects vì vậy là nguồn gravitational-wave mạnh.

## Strain

Detector thường mô tả signal bằng dimensionless strain

```math
h\sim\frac{\Delta L}{L}.
```

Interferometer đo differential change giữa hai arm.

LIGO không đo “force của sóng” theo cách cảm biến gia tốc cổ điển; nó đo relative spacetime distortion giữa freely suspended test masses.

## Cosmology từ Einstein equation

Nếu giả sử universe homogeneous và isotropic ở scale lớn, metric FLRW cùng Einstein equation dẫn tới Friedmann equations.

Một dạng là

```math
H^2
=\left(\frac{\dot a}{a}\right)^2
=
\frac{8\pi G}{3}\rho
-\frac{kc^2}{a^2}
+\frac{\Lambda c^2}{3}.
```

Đây là cầu nối từ local geometric gravity sang expansion history của toàn universe.

Chi tiết cosmology được phát triển ở chapter riêng.

## Assumptions và phạm vi của GR classical

GR là classical field theory của spacetime.

Nó hoạt động cực kỳ tốt từ solar-system tests đến binary pulsars và gravitational waves.

Nhưng nó chưa bao gồm quantum gravity.

Các miền kỳ vọng cần mô tả sâu hơn gồm:

```text
curvature gần Planck scale
classical singularities
early quantum spacetime regimes
```

Ngoài ra để giải một bài GR cụ thể, cần specification của matter model, symmetry và boundary/initial conditions. Einstein equation một mình không tự chọn solution duy nhất.

## Mô hình tư duy (Mental Model)

GR có thể giữ trong đầu bằng ba tầng:

```text
metric
→ cách spacetime đo interval và causal structure

curvature
→ tidal gravity đo được

stress-energy
→ nguồn động lực học của geometry
```

Free-fall không phải “vật bị kéo khỏi đường thẳng”; trong geometry phù hợp, geodesic chính là đường chuyển động tự do tự nhiên.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Gravity biến mất trong free-fall nên spacetime phẳng”

Không. Connection có thể triệt tiêu cục bộ, nhưng curvature/tidal effects có thể vẫn khác zero.

### “Event horizon là singularity”

Không. Với Schwarzschild black hole, horizon là causal boundary; curvature singularity nằm ở `r=0` trong classical solution.

### “Black hole hút mạnh bất thường ở mọi khoảng cách”

Không. Xa một spherical black hole, exterior gravity gần giống mass khác có cùng `M`.

### “Einstein equation nói vật chất trực tiếp tạo force hấp dẫn”

Chính xác hơn, stress-energy liên hệ với curvature, còn test particle free-fall theo geodesic của metric.

### “Newtonian gravity sai hoàn toàn”

Không. Nó là weak-field, low-velocity limit cực kỳ tốt của GR.

### “Energy luôn có một total scalar global rõ ràng trong mọi spacetime”

Không. Local covariant conservation luôn quan trọng, nhưng global energy definition phụ thuộc symmetry/boundary structure của spacetime.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Thuyết tương đối hẹp](00_special_relativity.md), [Hấp dẫn Newton và quỹ đạo](../01_mechanics/06_gravitation_orbits.md), [Tensor và PDE](../00_foundations/05_pde_boundary_green_tensors.md).

**Liên hệ tiếp:** [Sao và thiên thể đặc](../11_astrophysics_cosmology/00_stars_compact_objects.md), [Thiên hà và vũ trụ học](../11_astrophysics_cosmology/01_galaxies_cosmology.md), [Vũ trụ sơ khai](../11_astrophysics_cosmology/03_early_universe_dark_components.md), [Vật lý thiên văn quan sát](../11_astrophysics_cosmology/02_observational_astrophysics_radiative_transfer.md).
