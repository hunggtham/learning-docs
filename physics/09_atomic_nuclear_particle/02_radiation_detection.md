# Bức xạ ion hóa, tương tác với vật chất và detector

Detector bức xạ không “nhìn thấy hạt” theo nghĩa trực tiếp. Nó đo hậu quả của việc bức xạ truyền năng lượng cho vật chất: ion hóa, kích thích, phát photon nhấp nháy, tạo cặp electron–lỗ trống, tạo phản ứng hạt nhân hoặc để lại vết tích trong vật liệu.

Vì vậy một hệ đo bức xạ luôn là một chuỗi chuyển đổi:

```text
bức xạ
→ tương tác với vật chất
→ năng lượng lắng đọng
→ điện tích hoặc ánh sáng
→ khuếch đại/xử lý tín hiệu
→ dữ liệu số
→ suy ra năng lượng, loại hạt, tốc độ đếm hoặc liều
```

## Đại lượng cơ bản: hoạt độ, năng lượng và liều

Hoạt độ (activity) đo số phân rã trong một giây:

```math
A=\lambda N,
```

với đơn vị becquerel

```text
1 Bq = 1 phân rã/s.
```

Năng lượng lắng đọng trong vật chất là nền tảng của liều hấp thụ:

```math
D=\frac{E_{dep}}{m},
```

đơn vị gray

```text
1 Gy = 1 J/kg.
```

Sievert `Sv` dùng cho liều tương đương hoặc hiệu dụng, trong đó năng lượng hấp thụ được nhân với các hệ số trọng số liên quan loại bức xạ và mô sinh học.

Một nguồn có activity lớn chưa chắc tạo dose lớn tại người quan sát. Khoảng cách, hình học, thời gian tiếp xúc, shielding và năng lượng phổ đều ảnh hưởng.

## Hạt mang điện mất năng lượng như thế nào?

Hạt mang điện tương tác Coulomb với electron và hạt nhân trong vật liệu. Suất hãm (stopping power)

```math
-\frac{dE}{dx}
```

mô tả năng lượng trung bình mất trên một đơn vị chiều dài.

Hạt nặng như alpha thường đi gần đường thẳng hơn electron và có mật độ ion hóa lớn hơn. Khi chúng chậm lại, stopping power có thể tăng mạnh trước khi dừng, tạo đỉnh Bragg (Bragg peak).

Đây là cơ sở vật lý quan trọng của proton/heavy-ion therapy: có thể đặt vùng lắng đọng năng lượng lớn gần độ sâu mục tiêu thay vì trên toàn đường đi như photon.

Electron beta nhẹ hơn nên chịu nhiều tán xạ góc và bức xạ hãm (bremsstrahlung), đặc biệt trong vật liệu có số nguyên tử `Z` lớn.

## Photon gamma tương tác với vật chất

Ba cơ chế quan trọng là:

1. hiệu ứng quang điện (photoelectric effect);
2. tán xạ Compton;
3. tạo cặp electron–positron khi

```math
E_\gamma>2m_ec^2\approx1.022\,MeV.
```

Tầm quan trọng tương đối của các cơ chế phụ thuộc năng lượng photon và nguyên tử số của vật liệu.

Trong mô hình attenuation đơn giản,

```math
I(x)=I_0e^{-\mu x}.
```

`\mu` là hệ số suy giảm tuyến tính với đơn vị `m^{-1}` hoặc `cm^{-1}`.

Bề dày bán giá trị (half-value layer, HVL) là

```math
x_{1/2}=\frac{\ln2}{\mu}.
```

Mô hình exponential giả định chùm tia và hình học đo đơn giản. Trong detector thật, scattered photons có thể quay lại vùng đo nên buildup và geometry corrections trở nên quan trọng.

## Neutron: phát hiện gián tiếp

Neutron không mang điện nên không trực tiếp ion hóa theo cách electron hay alpha làm. Detector neutron thường biến neutron thành charged secondary particles qua phản ứng hạt nhân.

Ví dụ, phản ứng với boron-10:

```math
{}^{10}B+n\rightarrow{}^7Li+\alpha.
```

Các hạt tích điện thứ cấp sau đó tạo ion hóa và sinh tín hiệu điện.

Với neutron nhanh, hydrogen-rich moderators giúp làm chậm neutron qua elastic scattering. Sau thermalization, vật liệu có cross section bắt neutron lớn như `^3He`, `^10B` hoặc `^6Li` có thể được dùng để detection.

## Detector khí: ion chamber, proportional counter và Geiger–Müller

Cùng một ống khí có thể hoạt động ở các chế độ khác nhau tùy điện áp.

### Ionization chamber

Điện trường chỉ đủ để thu các ion sơ cấp trước khi chúng recombine đáng kể. Charge thu được gần tỉ lệ với năng lượng lắng đọng, nhưng tín hiệu nhỏ.

### Proportional counter

Điện trường mạnh hơn tạo Townsend avalanche. Gain lớn hơn 1 nhưng vẫn gần tỉ lệ với số ion sơ cấp, nên pulse height còn mang thông tin năng lượng.

### Geiger–Müller counter

Avalanche lan rộng khiến pulse size gần như độc lập với ionization ban đầu. Detector rất nhạy để đếm sự kiện nhưng energy spectroscopy kém.

Do đó ba detector không chỉ khác tên; chúng là ba chế độ gain khác nhau của cùng physics ionization trong khí.

## Dead time và pile-up

Sau một event, detector và electronics cần thời gian hồi phục. Khoảng này gọi là dead time `\tau`.

Trong mô hình non-paralyzable đơn giản, rate quan sát `m` liên hệ với rate thật `n` gần bởi

```math
m=\frac{n}{1+n\tau}.
```

Suy ra

```math
n=\frac{m}{1-m\tau}.
```

Khi rate cao, nếu không hiệu chỉnh dead time thì số đếm bị đánh giá thấp.

Nếu hai sự kiện đến quá gần nhau, pulses có thể chồng lên nhau tạo pile-up. Điều này làm méo energy spectrum và đặc biệt quan trọng trong gamma spectroscopy hoặc synchrotron/high-flux measurements.

## Scintillator: từ năng lượng lắng đọng đến photon ánh sáng

Scintillator hấp thụ năng lượng rồi phát photon quang học. Ánh sáng được thu bởi photomultiplier tube (PMT) hoặc silicon photomultiplier (SiPM).

Chuỗi tín hiệu có thể hình dung:

```text
E_dep
→ excitations trong scintillator
→ N_photon
→ photoelectrons
→ gain
→ pulse điện
```

Nếu các bước gần tuyến tính, pulse height có thể dùng để suy năng lượng lắng đọng.

Scintillator vô cơ như NaI(Tl) có hiệu suất gamma cao nhờ mật độ và `Z` lớn. Scintillator hữu cơ thường nhanh và hữu ích trong timing, neutron detection hoặc pulse-shape discrimination.

## Detector bán dẫn

Trong silicon hoặc germanium, bức xạ tạo electron–hole pairs.

Nếu năng lượng trung bình để tạo một cặp là `w`, thì số cặp trung bình là

```math
N\approx\frac{E_{dep}}{w}.
```

Với silicon,

```math
w\approx3.6\,eV
```

ở nhiệt độ phòng.

Vì `w` nhỏ hơn năng lượng cần tạo photon hữu ích trong nhiều scintillators, semiconductor detectors có thể tạo nhiều charge carriers hơn trên cùng năng lượng lắng đọng và đạt energy resolution tốt.

Germanium tinh khiết có resolution gamma rất cao nhưng thường cần làm lạnh để giảm leakage current và electronic noise.

## Vì sao resolution không chỉ do số hạt tải?

Nếu quá trình tạo carriers tuân Poisson lý tưởng, variance số cặp sẽ gần `N`. Nhưng trong detector bán dẫn, fluctuations thường nhỏ hơn Poisson do năng lượng được phân chia có tương quan.

Ta dùng Fano factor `F`:

```math
\sigma_N^2=FN.
```

Với `F<1`, intrinsic energy resolution tốt hơn dự đoán Poisson thuần túy.

Nếu

```math
E=wN,
```

thì intrinsic standard deviation năng lượng gần

```math
\sigma_E=w\sqrt{FN}.
```

Detector thực còn chịu electronic noise, charge trapping, incomplete collection và calibration errors.

## Energy resolution và FWHM

Một line đơn năng lượng lý tưởng không xuất hiện thành delta function trong spectrum thật. Nó có finite width.

Energy resolution thường định nghĩa

```math
R=\frac{\Delta E_{FWHM}}{E_0}.
```

Resolution nhỏ hơn nghĩa detector phân biệt hai line gần nhau tốt hơn.

Nếu peak gần Gaussian,

```math
FWHM\approx2.355\sigma.
```

Resolution phụ thuộc statistical fluctuations, electronics noise và detector physics.

## Hiệu suất detector

Có nhiều loại efficiency khác nhau.

Intrinsic efficiency:

```math
\epsilon_{int}
=\frac{N_{detected}}{N_{incident\ on\ detector}}.
```

Absolute efficiency:

```math
\epsilon_{abs}
=\frac{N_{detected}}{N_{emitted\ by\ source}}.
```

Absolute efficiency còn phụ thuộc solid angle và geometry.

Một detector có intrinsic efficiency rất cao nhưng đặt xa nguồn vẫn có absolute efficiency thấp.

## Solid angle và hình học

Nếu nguồn đẳng hướng và detector nhỏ ở khoảng cách `r`, fraction photon đi vào diện tích `A` gần

```math
f\approx\frac{A}{4\pi r^2}
```

khi detector gần vuông góc với đường nối nguồn và `A\ll r^2`.

Đây là nguồn gốc của inverse-square behavior trong hình học điểm:

```math
I\propto\frac{1}{r^2}.
```

Nhưng gần nguồn mở rộng hoặc detector lớn, phải dùng solid-angle integration thay vì công thức điểm đơn giản.

## Background và signal-to-noise

Detector luôn có background: bức xạ môi trường, cosmic rays, radioactivity nội tại vật liệu, dark counts và electronic noise.

Nếu đo `N_{on}` trong vùng có source và `N_{bg}` từ background estimate với normalization phù hợp, signal ước lượng là hiệu hai số.

Khi counts đủ lớn và Poisson độc lập, variance của hiệu gần tổng variances:

```math
\sigma_S^2\approx\sigma_{on}^2+\sigma_{bg}^2.
```

Do đó tăng thời gian đo không chỉ tăng signal mà cũng tích lũy background. Thiết kế shielding, coincidence và event selection thường quan trọng không kém detector volume.

## Thống kê Poisson của số đếm

Nếu events độc lập với rate ổn định, số đếm `N` trong thời gian cố định gần phân bố Poisson:

```math
P(N|\lambda)=\frac{\lambda^N e^{-\lambda}}{N!}.
```

Mean và variance bằng nhau:

```math
\langle N\rangle=\lambda,
```

```math
\sigma_N=\sqrt{\lambda}\approx\sqrt N.
```

Do đó relative statistical uncertainty giảm theo

```math
\frac{\sigma_N}{N}\approx\frac{1}{\sqrt N}.
```

Muốn giảm statistical uncertainty tương đối từ `10%` xuống `1%`, số đếm cần tăng khoảng 100 lần.

## Detector response function

Một detector không ánh xạ “một năng lượng thật → một số đo hoàn hảo”. Ta có thể mô tả bằng response function

```math
R(E_{meas}|E_{true}).
```

Spectrum đo được là tích phân của spectrum thật qua response detector:

```math
M(E_m)
=
\int R(E_m|E)S(E)dE+B(E_m).
```

`S(E)` là spectrum thật, `B` là background.

Đây là một inverse problem. Unfolding spectrum cần calibration, regularization hoặc Bayesian inference; nếu response matrix gần suy biến thì không thể khôi phục tùy ý mọi chi tiết.

## Calibration

Energy calibration thường dùng nguồn có line năng lượng đã biết. Nếu ADC channel `C` liên hệ gần tuyến tính với energy,

```math
E=aC+b.
```

Hai điểm calibration có thể xác định `a,b`, nhưng detector thật có thể cần polynomial hoặc nonlinear correction.

Calibration không chỉ là fit một đường. Cần kiểm tra residuals, stability theo nhiệt độ/thời gian và uncertainty của reference energies.

## Coincidence và timing

Nếu hai detector ghi sự kiện trong một cửa sổ thời gian ngắn, ta có thể dùng coincidence để giảm background hoặc xác định decay cascade.

Random coincidence rate tăng khi singles rates và time window tăng. Do đó timing resolution tốt giúp tách true coincidences khỏi accidental coincidences.

PET là ví dụ ứng dụng: hai photon annihilation `511 keV` gần đối hướng được phát hiện gần đồng thời để xác định line of response.

## Shielding không chỉ là “chọn vật liệu nặng nhất”

Gamma thường cần vật liệu mật độ cao/Z lớn như lead để tăng attenuation. Neutron thường cần hydrogen-rich moderator rồi absorber như boron.

Electron beta năng lượng cao chiếu trực tiếp vào vật liệu Z lớn có thể tạo bremsstrahlung mạnh; đôi khi cần lớp low-Z để làm chậm electron rồi lớp high-Z để chặn photon thứ cấp.

Vì vậy shielding là bài toán transport nhiều bước, không phải chỉ tối đa density.

## Ví dụ: dead-time correction

Giả sử counter đo

```math
m=2.0\times10^4\,s^{-1}
```

với non-paralyzable dead time

```math
\tau=10\,\mu s.
```

Ta có

```math
m\tau=0.20.
```

Rate thật ước lượng

```math
n=\frac{m}{1-m\tau}
=\frac{2.0\times10^4}{0.8}
=2.5\times10^4\,s^{-1}.
```

Nếu bỏ dead-time correction, rate bị đánh giá thấp 20%.

## Mô hình tư duy (Mental Model)

Một detector là **hệ thống suy luận vật lý**, không chỉ là cảm biến. Bức xạ tạo tương tác vi mô; vật liệu chuyển tương tác thành charge/light; electronics biến tín hiệu thành numbers; calibration và statistics biến numbers thành physical quantities.

Khi đọc một spectrum, luôn hỏi: detector response là gì, efficiency bao nhiêu, dead time thế nào, background đến từ đâu và observable cuối cùng liên hệ với source qua mô hình nào.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Detector đếm trực tiếp mọi hạt đi qua”

Không. Detection probability nhỏ hơn 1 và phụ thuộc interaction cross section, geometry, threshold và efficiency.

### “Peak rộng nghĩa nguồn phát nhiều năng lượng khác nhau”

Không nhất thiết. Một monoenergetic line vẫn có finite detector resolution.

### “Nhiều count luôn nghĩa measurement chính xác”

Statistical uncertainty giảm khi counts tăng, nhưng systematic uncertainty, calibration error hoặc background model sai có thể vẫn chi phối.

### “Activity và dose là cùng một đại lượng”

Không. Activity mô tả decay rate của source; dose mô tả năng lượng được hấp thụ trên khối lượng vật chất, có phụ thuộc geometry và interaction.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Vật lý hạt nhân](01_nuclear_physics.md), [Cơ học thống kê](../04_thermal_statistical/01_entropy_statistical_mechanics.md), [Bán dẫn và thiết bị](../10_condensed_matter_devices/01_semiconductors_devices.md).

**Liên hệ tiếp:** [Đo lường và độ bất định](../12_experimental_computational/00_measurement_experiment.md), [Tín hiệu, lấy mẫu và nhiễu](../12_experimental_computational/01_signals_sampling_noise.md), [Suy luận dữ liệu và bài toán nghịch đảo](../12_experimental_computational/03_data_inference_inverse_problems.md).