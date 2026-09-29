# Thiên hà, sự giãn nở của vũ trụ và vũ trụ học hiện đại

> **Mạch đọc:** Đọc **Thiên hà, sự giãn nở của vũ trụ và vũ trụ học hiện đại** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ thiên hà đến bằng chứng vật chất tối** sang **Nguyên lý vũ trụ học**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Vũ trụ học (cosmology / 우주론) dùng thuyết tương đối rộng, vật lý nhiệt, vật lý hạt và dữ liệu quan sát để mô tả lịch sử động lực học của toàn bộ vũ trụ ở quy mô lớn. Điểm khó là ta chỉ quan sát vũ trụ từ một vị trí và một thời điểm, vì vậy phần lớn bài toán là bài toán nghịch đảo: từ photon, redshift, angular kích thước (size / 크기), spectrum và statistics của nhiều nguồn để suy ra hình học (geometry / 기하학) cùng thành phần vật chất–năng lượng.

## Từ thiên hà đến bằng chứng vật chất tối

Nếu phần lớn khối lượng một thiên hà tập trung trong vùng sáng trung tâm, cơ học Newton dự đoán ở bán kính lớn

```math
v(r)\sim\sqrt{\frac{GM(<r)}{r}}
```

nên khi `M(<r)` gần bão hòa, vận tốc quỹ đạo phải giảm gần `r^{-1/2}`.

Nhiều thiên hà xoắn ốc lại có rotation curves gần phẳng trong một miền rộng. Khi

```math
v(r)\approx const,
```

thì từ

```math
\frac{v^2}{r}\approx\frac{GM(<r)}{r^2}
```

suy ra

```math
M(<r)\propto r.
```

Tức khối lượng hấp dẫn tiếp tục tăng ngoài vùng chứa phần lớn ánh sáng.

Đây không phải bằng chứng duy nhất. Gravitational lensing, dynamics của clusters, CMB và large-scale cấu trúc (structure / 구조) cùng chỉ về một thành phần hấp dẫn không phát sáng đáng kể.

Vật chất tối (dark matter / 암흑물질) là tên cho thành phần đó trong mô hình chuẩn hiện nay. Bản chất vi mô chưa được xác định chắc chắn.

## Nguyên lý vũ trụ học

Ở quy mô đủ lớn, mô hình chuẩn giả định vũ trụ gần đồng nhất (homogeneous) và đẳng hướng (isotropic) theo nghĩa thống kê.

Hai giả định này không nói vũ trụ đồng đều ở mọi quy mô (scale / 규모). Thiên hà, cluster và void rõ ràng tạo cấu trúc. Ý nghĩa là sau khi average trên quy mô (scale / 규모) đủ lớn, không có vị trí hoặc hướng đặc biệt nổi bật trong phân bố vật chất.

Với các giả định đó, spacetime được mô tả bởi chỉ số (metric / 지표) Friedmann–Lemaître–Robertson–Walker (FLRW).

## Quy mô (scale / 규모) factor và tọa độ đồng chuyển

Khoảng cách vật lý giữa hai điểm đồng chuyển có thể viết

```math
d_{phys}(t)=a(t)\chi,
```

trong đó `\chi` là comoving coordinate và `a(t)` là quy mô (scale / 규모) factor.

Các thiên hà đi cùng Hubble luồng (flow / 흐름) có `\chi` gần cố định, còn vật lý (physical / 물리적) distance tăng vì `a(t)` tăng.

Hubble parameter là

```math
H(t)=\frac{\dot a}{a}.
```

Ở gần hiện tại,

```math
H_0=H(t_0).
```

Với khoảng cách nhỏ đủ để curvature và evolution chưa quan trọng mạnh,

```math
v\approx H_0d.
```

Đây là quan hệ Hubble–Lemaître gần đúng.

## Redshift vũ trụ học

Ánh sáng phát tại quy mô (scale / 규모) factor `a_{emit}` và quan sát tại `a_{obs}` có

```math
1+z
=\frac{\lambda_{obs}}{\lambda_{emit}}
=\frac{a_{obs}}{a_{emit}}.
```

Nếu quy ước

```math
a_{obs}=1,
```

thì

```math
a_{emit}=\frac{1}{1+z}.
```

Cosmological redshift không nên bị giản lược hoàn toàn thành Doppler shift trong không gian tĩnh. Trong GR, nó phản ánh sự thay đổi chỉ số (metric / 지표) dọc đường truyền của photon.

Ở redshift rất nhỏ, Doppler intuition và Hubble law có thể gần tương đương về số, nhưng ở `z` lớn phải dùng cosmological mô hình (model / 모델) đầy đủ.

## Phương trình Friedmann

Với FLRW spacetime, Einstein equation dẫn tới

```math
H^2
=\left(\frac{\dot a}{a}\right)^2
=\frac{8\pi G}{3}\rho
-\frac{kc^2}{a^2}
+\frac{\Lambda c^2}{3}.
```

`\rho` là tổng năng lượng (energy / 에너지) density của matter/radiation và các thành phần phù hợp; `k` mô tả spatial curvature; `\Lambda` là cosmological constant.

Phương trình gia tốc là

```math
\frac{\ddot a}{a}
=-\frac{4\pi G}{3}
\left(\rho+\frac{3p}{c^2}\right)
+\frac{\Lambda c^2}{3}.
```

Pressure vì vậy tham gia trực tiếp vào gravity trong GR.

## Phương trình liên tục vũ trụ học

Bảo toàn năng lượng (energy / 에너지)–momentum cho fluid đồng nhất cho

```math
\dot\rho
+3H\left(\rho+\frac{p}{c^2}\right)=0.
```

Nếu equation of trạng thái (state / 상태) có dạng

```math
p=w\rho c^2,
```

thì

```math
\rho\propto a^{-3(1+w)}.
```

Do đó:

```math
\rho_m\propto a^{-3}
```

cho matter không tương đối tính;

```math
\rho_r\propto a^{-4}
```

cho radiation;

và với vacuum năng lượng (energy / 에너지)

```math
w=-1
```

thì

```math
\rho_\Lambda=const.
```

Radiation giảm nhanh hơn matter vì ngoài dilution theo volume `a^3`, photon còn redshift mất năng lượng thêm một factor `a`.

## Mật độ tới hạn và các tham số `Ω`

Định nghĩa trọng yếu (critical / 중요) density tại thời điểm `t`:

```math
\rho_c(t)=\frac{3H^2(t)}{8\pi G}.
```

Với mỗi thành phần,

```math
\Omega_i(t)=\frac{\rho_i(t)}{\rho_c(t)}.
```

Tại hiện tại, thường dùng

```math
\Omega_m,
\Omega_r,
\Omega_\Lambda,
\Omega_k.
```

Phương trình Friedmann có thể viết

```math
1=\Omega_m+\Omega_r+\Omega_\Lambda+\Omega_k
```

ở cùng epoch với quy ước phù hợp.

`\Omega=1` không có nghĩa “vũ trụ chứa đúng một đơn vị vật chất”; nó là tỉ số với trọng yếu (critical / 중요) density.

## Vì sao Big Bang không phải vụ nổ từ một điểm?

Big Bang mô hình (model / 모델) mô tả một trạng thái quá khứ nóng và đặc hơn khi quy mô (scale / 규모) factor nhỏ.

Nó không mô tả vật chất nổ từ một tâm vào không gian trống có sẵn. Trong FLRW cosmology, expansion là evolution của chỉ số (metric / 지표) giữa các comoving points.

Nếu không gian (space / 공간) đồng nhất, mọi comoving observer đều thấy các nguồn xa recede theo Hubble luồng (flow / 흐름); không có một center đặc biệt nằm trong không gian ba chiều.

## Lookback thời gian (time / 시간)

Ánh sáng từ redshift `z` được phát trong quá khứ. Quan hệ giữa cosmic thời gian (time / 시간) và redshift là

```math
dt
=-\frac{dz}{(1+z)H(z)}.
```

Do đó lookback thời gian (time / 시간) là

```math
t_L(z)
=
\int_0^z
\frac{dz'}{(1+z')H(z')}.
```

Ta không thể đổi redshift thành “bao nhiêu năm trước” nếu không có mô hình `H(z)`.

## Comoving distance

Trong vũ trụ phẳng, line-of-sight comoving distance là

```math
D_C(z)
=c\int_0^z\frac{dz'}{H(z')}.
```

Đây là một trong các distance measures cơ bản.

## Luminosity distance

Nếu nguồn có luminosity `L` và flux quan sát `F`, ta định nghĩa luminosity distance `D_L` bằng

```math
F=\frac{L}{4\pi D_L^2}.
```

Trong FLRW,

```math
D_L=(1+z)D_M,
```

với `D_M` là transverse comoving distance.

Factor `(1+z)` xuất hiện do photon năng lượng (energy / 에너지) redshift và arrival tỷ lệ (rate / 비율) bị thời gian (time / 시간) dilation.

## Angular-diameter distance

Nếu vật có vật lý (physical / 물리적) transverse kích thước (size / 크기) `\ell` và angular kích thước (size / 크기) `\theta`, định nghĩa

```math
D_A=\frac{\ell}{\theta}.
```

Quan hệ Etherington distance duality là

```math
D_L=(1+z)^2D_A
```

nếu photon number được bảo toàn và ánh sáng truyền trên null geodesics trong chỉ số (metric / 지표) lý thuyết (theory / 이론) phù hợp.

Điểm thú vị là `D_A` không tăng đơn điệu với redshift trong cosmology chuẩn; vật ở rất xa có thể bắt đầu có angular kích thước (size / 크기) lớn hơn khi `z` tăng thêm.

## Supernova Ia và lịch sử giãn nở

Kiểu (type / 타입) Ia supernovae có thể chuẩn hóa luminosity từ light curve và spectral properties. Từ observed flux suy ra luminosity distance; từ spectrum suy ra redshift.

Quan hệ

```text
D_L(z)
```

sau đó được so với các cosmological các mô hình (models / 모델들).

Dữ liệu cuối thế kỷ XX chỉ ra expansion gần hiện tại đang accelerating trong khung phần mềm (framework / 프레임워크) GR + FLRW, dẫn tới thành phần dark-energy-like trong mô hình chuẩn.

## CMB

Khi vũ trụ nguội tới khoảng vài nghìn kelvin, electron và nuclei kết hợp thành neutral atoms và photon decouple hiệu quả hơn khỏi baryonic matter.

Ngày nay bức xạ này xuất hiện dưới dạng Cosmic Microwave Background (CMB) gần blackbody ở khoảng `2.7 K`.

Temperature anisotropies cỡ `10^{-5}` chứa thông tin về density perturbations, hình học (geometry / 기하학) và composition của early universe.

Angular power spectrum

```math
C_\ell
```

mô tả variance của anisotropy theo angular quy mô (scale / 규모).

Acoustic peaks phản ánh oscillations của photon–baryon plasma trước recombination và cung cấp các ràng buộc (constraints / 제약조건들) mạnh lên `\Omega_b`, `\Omega_m`, curvature và nhiều parameters khác.

## BAO như thước chuẩn

Baryon Acoustic Oscillations (BAO) là dấu vết của cùng acoustic physics trong phân bố matter muộn hơn.

Sound horizon tạo một characteristic comoving quy mô (scale / 규모). Đo quy mô (scale / 규모) này theo transverse và radial directions cung cấp các ràng buộc (constraints / 제약조건들) lên

```math
D_M(z)
```

và

```math
H(z).
```

BAO là ví dụ rõ của cách một hiện tượng plasma sớm trở thành ruler cho late-time cosmology.

## Vật chất tối và cấu trúc (structure / 구조) growth

Dark matter không tương tác điện từ mạnh nên có thể bắt đầu tạo gravitational potential wells trước khi baryonic gas decouple hoàn toàn khỏi radiation.

Density contrast

```math
\delta
=\frac{\rho-\bar\rho}{\bar\rho}
```

phát triển theo gravity.

Trong tuyến tính (linear / 선형) regime ở matter-dominated universe đơn giản,

```math
\delta\propto a.
```

Dark năng lượng (energy / 에너지) dominance về sau làm cấu trúc (structure / 구조) growth chậm lại.

Chi tiết được học sâu hơn trong chapter gravitational instability/cấu trúc (structure / 구조) formation.

## Năng lượng tối và equation of trạng thái (state / 상태)

Cosmological constant tương ứng

```math
p_\Lambda=-\rho_\Lambda c^2,
```

hay

```math
w=-1.
```

Một mô hình dark năng lượng (energy / 에너지) tổng quát thường tham số hóa bằng

```math
w=\frac{p}{\rho c^2}.
```

Nếu `w<-1/3`, thành phần đó có thể tạo accelerated expansion nếu đủ dominant.

Hiện `\Lambda`CDM với `w=-1` là baseline mô hình (model / 모델) rất thành công, nhưng bản chất microscopic của vacuum năng lượng (energy / 에너지) và cosmological constant bài toán (problem / 문제) vẫn mở.

## Hubble tension là gì về mặt phương pháp?

Các phương pháp “cục bộ (local / 로컬) distance ladder” và suy luận (inference / 추론) từ early-universe dữ liệu (data / 데이터) trong `\Lambda`CDM có thể cho giá trị `H_0` khác nhau ở mức đáng chú ý.

Đây là ví dụ tốt cho khoa học thực nghiệm: trước khi kết luận có new physics, phải kiểm tra calibration, population effects, covariance, mô hình (model / 모델) các giả định (assumptions / 가정들) và hidden systematics.

Một tension thống kê không tự động là bằng chứng vật lý mới; nó là tín hiệu cần kiểm tra (audit / 감사) cả dữ liệu (data / 데이터) lẫn mô hình (model / 모델).

## Parameter suy luận (inference / 추론) trong cosmology

Cosmological parameters không được “đọc trực tiếp” từ một observable duy nhất. Ta có dữ liệu (data / 데이터) `D`, mô hình (model / 모델) parameters `\theta` và likelihood

```math
p(D|\theta).
```

Bayes theorem cho

```math
p(\theta|D)
\propto
p(D|\theta)p(\theta).
```

Parameters có thể degeneracy: hai tổ hợp khác nhau tạo observables gần giống nhau. Vì vậy kết hợp independent probes như CMB + BAO + supernovae + lensing giúp phá degeneracy.

Covariance giữa dữ liệu (data / 데이터) points phải được giữ trong likelihood; nếu xem các điểm tương quan như độc lập, bất định (uncertainty / 불확실성) sẽ bị đánh giá quá nhỏ.

## Selection effects

Telescope có flux limit nên dễ phát hiện nguồn (source / 소스) sáng hơn nguồn (source / 소스) yếu. Survey hình học (geometry / 기하학), observing cadence và mục tiêu (target / 대상) selection tạo selection hàm (function / 함수).

Một population quan sát được không nhất thiết đại diện trực tiếp population thật. Đây là lý do cosmology và astrophysics phải mô hình hóa completeness và selection độ lệch (bias / 편향).

## Gravitational lensing như probe cosmology

Matter làm cong spacetime và bẻ null geodesics. Weak lensing tạo statistical distortion nhỏ trong hình ảnh nhiều galaxy.

Cosmic shear phụ thuộc integrated matter phân phối (distribution / 분포) dọc line of sight, nên cung cấp ràng buộc (constraint / 제약조건) lên matter density và cấu trúc (structure / 구조) growth.

Strong lensing thời gian (time / 시간) delays có thể dùng như một distance probe nếu lens mass mô hình (model / 모델) được kiểm soát đủ tốt.

## Sóng hấp dẫn và tiêu chuẩn (standard / 표준) siren

Gravitational-wave waveform cho phép suy luminosity distance trực tiếp từ amplitude/chirp cấu trúc (structure / 구조) mà không cần cosmic distance ladder truyền thống.

Nếu có redshift từ electromagnetic counterpart hoặc statistical host association, nguồn (source / 소스) trở thành tiêu chuẩn (standard / 표준) siren để ràng buộc (constraint / 제약조건) expansion lịch sử (history / 이력).

Đây là một ví dụ multi-messenger nơi GR, nuclear physics, detector calibration và cosmology nối trực tiếp nhau.

## Multi-messenger astronomy

Một sự kiện có thể được quan sát qua photon, gravitational wave, neutrino và cosmic ray.

Mỗi messenger chịu tương tác (interaction / 상호작용) khác nhau và probe regions khác nhau của nguồn (source / 소스).

GW170817 nối neutron-star dynamics, gravitational waves, gamma-ray burst, kilonova và heavy-element nucleosynthesis trong cùng một sự kiện (event / 이벤트).

## Điều kiện áp dụng của mô hình FLRW

FLRW mô tả universe đã coarse-grain ở quy mô (scale / 규모) lớn. Nó không mô tả chi tiết cục bộ (local / 로컬) spacetime gần black hole hay bên trong galaxy.

Trong cục bộ (local / 로컬) bound hệ thống (system / 시스템), expansion của universe thường không được cộng máy móc vào quỹ đạo hành tinh; cục bộ (local / 로컬) gravitational binding dominates.

Homogeneity/isotropy là statistical approximations cần được kiểm tra bằng survey observations.

## Những gì `ΛCDM` giải thích và không giải thích

`ΛCDM` mô tả rất tốt nhiều observations với một số ít parameters: CMB, BAO, supernova expansion lịch sử (history / 이력) và large-scale cấu trúc (structure / 구조) ở mức rộng.

Nhưng mô hình không xác định microscopic định danh (identity / 식별자) của dark matter; không giải quyết sâu cosmological constant bài toán (problem / 문제); không phải quantum gravity lý thuyết (theory / 이론); và có thể có tensions giữa datasets hoặc small-scale modeling cần nghiên cứu tiếp.

Một mô hình thành công không có nghĩa mọi câu hỏi nền tảng đã đóng.

## Ví dụ: redshift `z=1` có nghĩa gì?

Nếu

```math
z=1,
```

thì

```math
1+z=2.
```

Do đó

```math
a_{emit}=\frac12
```

nếu `a_0=1`.

Photon quan sát có bước sóng gấp đôi lúc phát.

Nhưng không thể từ riêng `z=1` kết luận “nguồn cách đúng X tỷ năm ánh sáng”. Comoving distance, luminosity distance, angular-diameter distance và lookback thời gian (time / 시간) là các đại lượng khác nhau và cần `H(z)` để tính.

## Mô hình tư duy (mental model / 사고 모델)

Vũ trụ học không chỉ là “những vật rất xa”. Nó là bài toán động lực học của **quy mô (scale / 규모) factor và hình học (geometry / 기하학) của spacetime**, kết hợp với một bài toán suy luận thống kê từ ánh sáng và các messenger khác.

Khi đọc một kết quả cosmology, nên hỏi ba lớp:

```text
observable được đo là gì?
cosmological distance/model nào nối observable với parameter?
assumption và covariance nào được dùng trong inference?
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Big Bang là vụ nổ từ một tâm”

Không. Trong FLRW mô hình (model / 모델), expansion là thay đổi quy mô (scale / 규모) factor của không gian; không cần một center đặc biệt nằm trong không gian ba chiều.

### “Recession velocity lớn hơn `c` luôn vi phạm tương đối tính”

Không. Với cosmological distances, recession tỷ lệ (rate / 비율) từ chỉ số (metric / 지표) expansion không giống cục bộ (local / 로컬) inertial velocity đo tại cùng một sự kiện. Không thể áp dụng trực tiếp công thức SR Doppler cho mọi khoảng cách vũ trụ.

### “Dark matter đã biết chắc là một loại hạt cụ thể”

Không. Gravitational bằng chứng (evidence / 증거) cho một thành phần dark matter rất mạnh trong mô hình chuẩn, nhưng microscopic định danh (identity / 식별자) vẫn chưa xác định.

### “Một giá trị `H_0` là observable trực tiếp không phụ thuộc mô hình”

Không hoàn toàn. Các phương pháp khác nhau dùng calibration và mô hình (model / 모델) các giả định (assumptions / 가정들) khác nhau; suy luận (inference / 추론) phải ghi rõ population, covariance và cosmological khung phần mềm (framework / 프레임워크).

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Thuyết tương đối rộng](../07_relativity/01_general_relativity.md), [Nhiệt động lực học và thống kê](../04_thermal_statistical/01_entropy_statistical_mechanics.md), [Suy luận dữ liệu và bài toán nghịch đảo](../12_experimental_computational/03_data_inference_inverse_problems.md).

**Liên hệ tiếp:** [Quan sát thiên văn và truyền bức xạ](02_observational_astrophysics_radiative_transfer.md), [Vũ trụ sơ khai và thành phần tối](03_early_universe_dark_components.md), [Bất ổn hấp dẫn và hình thành cấu trúc](04_gravitational_instability_structure_formation.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 stars compact objects](./00_stars_compact_objects.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
