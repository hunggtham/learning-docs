# Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Thuyết tương đối rộng: equivalence principle, curvature, geodesics và black holes**. Route đi từ local inertial frames → metric/curvature → geodesic motion → Einstein field equations → horizons/global geometry, để hấp dẫn trở thành hình học động.

Thuyết tương đối rộng (General Relativity / 일반상대성이론) thay đổi cách ta hiểu hấp dẫn: thay vì xem hấp dẫn chỉ là một lực nằm trên nền không gian–thời gian cố định, lý thuyết cho chỉ số (metric / 지표) của không-thời gian trở thành một trường động lực học chịu ảnh hưởng của năng lượng và động lượng.

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

Điều này gợi ý hấp dẫn liên quan tới cấu trúc của hệ quy chiếu và hình học không-thời gian, chứ không chỉ là một force trường dữ liệu (field / 필드) kiểu Newton.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Cục bộ phẳng không có nghĩa toàn cục phẳng** nối từ **Từ nguyên lý tương đương đến hình học** sang **Chỉ số (metric / 지표)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Chỉ số (metric / 지표)** nối từ **Cục bộ phẳng không có nghĩa toàn cục phẳng** sang **Geodesic**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chỉ số (metric / 지표)

Chỉ số (metric / 지표) tensor `g_{\mu\nu}(x)` xác định cách đo interval trong spacetime:

```math
ds^2=g_{\mu\nu}dx^\mu dx^\nu.
```

Với timelike worldline và convention dấu `(-,+,+,+)`, proper thời gian (time / 시간) thỏa

```math
c^2d\tau^2=-ds^2.
```

Chỉ số (metric / 지표) quyết định:

```text
proper time
proper distance
light cone
causal structure
geodesic
```

Trong special relativity, chỉ số (metric / 지표) Minkowski là cố định. Trong GR, chỉ số (metric / 지표) là một trường dữ liệu (field / 필드) cần được giải từ Einstein equation.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Geodesic** nối từ **Chỉ số (metric / 지표)** sang **Vì sao phi hành gia trên quỹ đạo thấy không trọng lượng?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Geodesic

Một free-falling kiểm thử (test / 테스트) particle đi theo geodesic:

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

Geodesic equation có thể được suy ra bằng extremizing proper thời gian (time / 시간) của free particle.

Điều này tương tự principle of stationary hành động (action / 동작) trong mechanics, nhưng hành động (action / 동작) bây giờ được xây từ spacetime hình học (geometry / 기하학).

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Vì sao phi hành gia trên quỹ đạo thấy không trọng lượng?** nối từ **Geodesic** sang **Geodesic deviation: độ cong đo được bằng tidal motion**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao phi hành gia trên quỹ đạo thấy không trọng lượng?

Phi hành gia trên ISS vẫn ở trong trường hấp dẫn mạnh đáng kể.

Họ thấy gần weightless vì cả tàu và cơ thể đều free-fall theo geodesic gần nhau.

Không có normal force từ sàn giữ cơ thể đứng yên như trên mặt đất.

Do đó cảm giác “trọng lượng” thường liên quan proper acceleration do hỗ trợ (support / 지원) force hơn là chỉ magnitude của gravitational trường dữ liệu (field / 필드) theo Newton.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Geodesic deviation: độ cong đo được bằng tidal motion** nối từ **Vì sao phi hành gia trên quỹ đạo thấy không trọng lượng?** sang **Einstein trường dữ liệu (field / 필드) equation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Geodesic deviation: độ cong đo được bằng tidal motion

Xét hai geodesic gần nhau có separation véc-tơ (vector / 벡터) `\xi^\mu` và four-velocity `u^\mu`.

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

Tidal stretching gần black hole, relative displacement do gravitational wave và nhiều phép đo gravity độ dốc (gradient / 기울기) đều liên hệ với cấu trúc này.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Geodesic deviation: độ cong đo được bằng tidal motion** đặt vấn đề; **Einstein trường dữ liệu (field / 필드) equation** đối chiếu bằng chứng, rồi **Conservation trong GR** mở rộng hệ quả hoặc giới hạn liên quan.

## Einstein trường dữ liệu (field / 필드) equation

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

Stress-energy tensor không chỉ chứa mass density. Nó còn chứa năng lượng (energy / 에너지) density, momentum density, năng lượng (energy / 에너지) flux, pressure và shear stress.

Do đó trong GR, pressure cũng góp vào gravitational nguồn (source / 소스).

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Einstein trường dữ liệu (field / 필드) equation** đặt vấn đề; **Conservation trong GR** đối chiếu bằng chứng, rồi **Giới hạn trường yếu** mở rộng hệ quả hoặc giới hạn liên quan.

## Conservation trong GR

Bianchi định danh (identity / 식별자) dẫn tới

```math
\nabla_\mu G^{\mu\nu}=0.
```

Kết hợp Einstein equation cho

```math
\nabla_\mu T^{\mu\nu}=0.
```

Đây là cục bộ (local / 로컬) covariant conservation law của stress-energy.

Trong curved spacetime tổng năng lượng (energy / 에너지) toàn cục không phải lúc nào cũng định nghĩa được theo cách đơn giản như trong Newtonian mechanics. Vì vậy không nên áp trực giác “một scalar total năng lượng (energy / 에너지) luôn tồn tại” vào mọi spacetime tùy ý.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Conservation trong GR** đặt tiêu chí; **Giới hạn trường yếu** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Gravitational thời gian (time / 시간) dilation trong trường yếu** mở rộng hệ quả.

## Giới hạn trường yếu

Một consistency check quan trọng là GR phải khôi phục Newtonian gravity khi:

```text
gravity weak
velocity << c
pressure << energy density
field thay đổi chậm
```

Viết chỉ số (metric / 지표) gần Minkowski:

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Giới hạn trường yếu** đặt tiêu chí; **Gravitational thời gian (time / 시간) dilation trong trường yếu** dùng tiêu chí đó để kiểm tra ranh giới, rồi **GPS** mở rộng hệ quả.

## Gravitational thời gian (time / 시간) dilation trong trường yếu

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

Nếu `\Phi` âm sâu hơn trong gravitational well, proper thời gian (time / 시간) tích lũy chậm hơn so với vị trí có potential cao hơn.

Gần mặt đất với height difference `\Delta h` nhỏ,

```math
\frac{\Delta f}{f}
\approx
\frac{g\Delta h}{c^2}.
```

Hiệu ứng rất nhỏ nhưng đo được bằng atomic clocks.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **GPS** nối từ **Gravitational thời gian (time / 시간) dilation trong trường yếu** sang **Schwarzschild spacetime**, vì cơ chế trước tạo đầu vào cho bước sau.

## GPS

Satellite clocks chịu hai correction chính:

```text
special-relativistic time dilation do velocity
+
general-relativistic gravitational time shift do altitude
```

Hai hiệu ứng có dấu khác nhau và phải được tính đồng thời.

GPS vì vậy là một ví dụ kỹ thuật (engineering / 엔지니어링) nơi relativity không phải “correction triết học” mà là thành phần của hệ thống (system / 시스템) thiết kế (design / 설계).

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Schwarzschild spacetime** nối từ **GPS** sang **Sự kiện (event / 이벤트) horizon là nhân quả (causal / 인과적) ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Schwarzschild spacetime

Bên ngoài một body spherical, nonrotating, vacuum solution có chỉ số (metric / 지표)

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

Nếu vật thể bị compact bên trong quy mô (scale / 규모) này trong ideal GR solution, `r=r_s` là sự kiện (event / 이벤트) horizon.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Schwarzschild spacetime** đặt tiêu chí; **Sự kiện (event / 이벤트) horizon là nhân quả (causal / 인과적) ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Curvature singularity** mở rộng hệ quả.

## Sự kiện (event / 이벤트) horizon là nhân quả (causal / 인과적) ranh giới (boundary / 경계)

Sự kiện (event / 이벤트) horizon không phải bề mặt vật liệu.

Nó được định nghĩa toàn cục bởi nhân quả (causal / 인과적) cấu trúc (structure / 구조): tín hiệu phát từ bên trong không thể tới future null infinity.

Một free-falling observer qua horizon của sufficiently large black hole không nhất thiết thấy cục bộ (local / 로컬) curvature vô hạn ngay tại horizon.

Một số coordinate các hệ thống (systems / 시스템들) như Schwarzschild coordinates có singular-looking components tại `r_s`, nhưng đây là coordinate singularity, không phải curvature singularity.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Sự kiện (event / 이벤트) horizon là nhân quả (causal / 인과적) ranh giới (boundary / 경계)** đặt tiêu chí; **Curvature singularity** dùng tiêu chí đó để kiểm tra ranh giới, rồi **Quỹ đạo và perihelion precession** mở rộng hệ quả.

## Curvature singularity

Ở `r=0` của ideal Schwarzschild solution, curvature bất biến (invariant / 불변식) như Kretschmann scalar diverges.

Điều này khác horizon.

Classical GR dự đoán breakdown tại singularity và cho thấy cần physics sâu hơn, thường được kỳ vọng liên quan quantum gravity.

Không nên diễn giải singularity như một vật thể đã được hiểu đầy đủ.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Quỹ đạo và perihelion precession** nối từ **Curvature singularity** sang **Deflection of light**, vì cơ chế trước tạo đầu vào cho bước sau.

## Quỹ đạo và perihelion precession

GR sửa Newtonian orbital dynamics bằng các correction nhỏ trong weak trường dữ liệu (field / 필드).

Với orbit gần Keplerian quanh mass `M`, perihelion advance mỗi vòng gần

```math
\Delta\phi
\approx
\frac{6\pi GM}
{a(1-e^2)c^2},
```

trong đó `a` là semi-major axis và `e` eccentricity.

Correction này giải thích phần anomalous precession của Mercury mà Newtonian perturbations từ các planet khác không giải thích hết.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Deflection of light** nối từ **Quỹ đạo và perihelion precession** sang **Shapiro thời gian (time / 시간) delay**, vì cơ chế trước tạo đầu vào cho bước sau.

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

trong weak trường dữ liệu (field / 필드).

Gravitational lensing ngày nay là công cụ quan trọng để đo mass phân phối (distribution / 분포), dark matter và distant galaxies.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Shapiro thời gian (time / 시간) delay** nối từ **Deflection of light** sang **Gravitational redshift**, vì cơ chế trước tạo đầu vào cho bước sau.

## Shapiro thời gian (time / 시간) delay

Tín hiệu điện từ đi qua vùng gravitational potential sâu có travel thời gian (time / 시간) lớn hơn giá trị Euclidean-flat expectation.

Hiệu ứng Shapiro là một trong các classical tests của GR và hiện được đo với radar ranging cùng pulsar timing.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Gravitational redshift** nối từ **Shapiro thời gian (time / 시간) delay** sang **Gravitational waves**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gravitational redshift

Photon phát sâu trong gravitational potential được quan sát ở vị trí cao hơn với frequency thấp hơn.

Ta có thể hiểu nó nhất quán qua comparison of cục bộ (local / 로컬) clock rates thay vì nói photon “mất năng lượng (energy / 에너지) một cách tuyệt đối” khi leo khỏi gravity.

Frequency luôn được đo bởi observer cụ thể.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Gravitational waves** nối từ **Gravitational redshift** sang **Strain**, vì cơ chế trước tạo đầu vào cho bước sau.

## Gravitational waves

Linearize chỉ số (metric / 지표):

```math
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}.
```

Trong vacuum và gauge thích hợp, perturbation thỏa wave equation gần

```math
\Box h_{\mu\nu}=0.
```

Sóng hấp dẫn lan với tốc độ `c`.

Do conservation of mass-energy và momentum, lowest radiative multipole cho isolated nguồn (source / 소스) không phải monopole hay dipole mà là quadrupole.

Nhị phân (binary / 이진) compact objects vì vậy là nguồn gravitational-wave mạnh.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Strain** nối từ **Gravitational waves** sang **Cosmology từ Einstein equation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Strain

Detector thường mô tả tín hiệu (signal / 신호) bằng dimensionless strain

```math
h\sim\frac{\Delta L}{L}.
```

Interferometer đo differential thay đổi (change / 변경) giữa hai arm.

LIGO không đo “force của sóng” theo cách cảm biến gia tốc cổ điển; nó đo relative spacetime distortion giữa freely suspended kiểm thử (test / 테스트) masses.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Cosmology từ Einstein equation** nối từ **Strain** sang **Các giả định (assumptions / 가정들) và phạm vi của GR classical**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cosmology từ Einstein equation

Nếu giả sử universe homogeneous và isotropic ở quy mô (scale / 규모) lớn, chỉ số (metric / 지표) FLRW cùng Einstein equation dẫn tới Friedmann equations.

Một dạng là

```math
H^2
=\left(\frac{\dot a}{a}\right)^2
=
\frac{8\pi G}{3}\rho
-\frac{kc^2}{a^2}
+\frac{\Lambda c^2}{3}.
```

Đây là cầu nối từ cục bộ (local / 로컬) geometric gravity sang expansion lịch sử (history / 이력) của toàn universe.

Chi tiết cosmology được phát triển ở chapter riêng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Các giả định (assumptions / 가정들) và phạm vi của GR classical** nối từ **Cosmology từ Einstein equation** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các giả định (assumptions / 가정들) và phạm vi của GR classical

GR là classical trường dữ liệu (field / 필드) lý thuyết (theory / 이론) của spacetime.

Nó hoạt động cực kỳ tốt từ solar-system tests đến nhị phân (binary / 이진) pulsars và gravitational waves.

Nhưng nó chưa bao gồm quantum gravity.

Các miền kỳ vọng cần mô tả sâu hơn gồm:

```text
curvature gần Planck scale
classical singularities
early quantum spacetime regimes
```

Ngoài ra để giải một bài GR cụ thể, cần specification của matter mô hình (model / 모델), symmetry và ranh giới (boundary / 경계)/initial conditions. Einstein equation một mình không tự chọn solution duy nhất.

> **Nối mạch:** Trong **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Các giả định (assumptions / 가정들) và phạm vi của GR classical** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

GR có thể giữ trong đầu bằng ba tầng:

```text
metric
→ cách spacetime đo interval và causal structure

curvature
→ tidal gravity đo được

stress-energy
→ nguồn động lực học của geometry
```

Free-fall không phải “vật bị kéo khỏi đường thẳng”; trong hình học (geometry / 기하학) phù hợp, geodesic chính là đường chuyển động tự do tự nhiên.

> **Nối mạch:** Ở chặng này của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Gravity biến mất trong free-fall nên spacetime phẳng”

Không. liên kết (connection / 연결) có thể triệt tiêu cục bộ, nhưng curvature/tidal effects có thể vẫn khác zero.

### “sự kiện (event / 이벤트) horizon là singularity”

Không. Với Schwarzschild black hole, horizon là nhân quả (causal / 인과적) ranh giới (boundary / 경계); curvature singularity nằm ở `r=0` trong classical solution.

### “Black hole hút mạnh bất thường ở mọi khoảng cách”

Không. Xa một spherical black hole, exterior gravity gần giống mass khác có cùng `M`.

### “Einstein equation nói vật chất trực tiếp tạo force hấp dẫn”

Chính xác hơn, stress-energy liên hệ với curvature, còn kiểm thử (test / 테스트) particle free-fall theo geodesic của chỉ số (metric / 지표).

### “Newtonian gravity sai hoàn toàn”

Không. Nó là weak-field, low-velocity limit cực kỳ tốt của GR.

### “năng lượng (energy / 에너지) luôn có một total scalar toàn cục (global / 전역) rõ ràng trong mọi spacetime”

Không. cục bộ (local / 로컬) covariant conservation luôn quan trọng, nhưng toàn cục (global / 전역) năng lượng (energy / 에너지) definition phụ thuộc symmetry/ranh giới (boundary / 경계) cấu trúc (structure / 구조) của spacetime.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Thuyết tương đối rộng: nguyên lý tương đương, độ cong, đường trắc địa và lỗ đen**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Thuyết tương đối hẹp](00_special_relativity.md), [Hấp dẫn Newton và quỹ đạo](../01_mechanics/06_gravitation_orbits.md), [Tensor và PDE](../00_foundations/05_pde_boundary_green_tensors.md).

**Liên hệ tiếp:** [Sao và thiên thể đặc](../11_astrophysics_cosmology/00_stars_compact_objects.md), [Thiên hà và vũ trụ học](../11_astrophysics_cosmology/01_galaxies_cosmology.md), [Vũ trụ sơ khai](../11_astrophysics_cosmology/03_early_universe_dark_components.md), [Vật lý thiên văn quan sát](../11_astrophysics_cosmology/02_observational_astrophysics_radiative_transfer.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
