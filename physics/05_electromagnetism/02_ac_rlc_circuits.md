# Mạch AC, phasor, trở kháng (impedance), RLC và cộng hưởng (resonance)

## Vì sao AC cần ngôn ngữ mới?

Trong DC trạng thái xác lập (steady state), điện áp (voltage) và dòng điện (current) gần hằng số (constant). Với alternating dòng điện (AC / 교류), nguồn (source) thay đổi theo thời gian, thường xấp xỉ sinusoid:

```math
v(t)=V_0\cos(\omega t+\phi).
```

Resistor phản ứng tức thời trong lý tưởng (ideal) mô hình (model), nhưng capacitor và inductor lưu năng lượng (energy) trong electric và magnetic các trường (fields). Vì vậy dòng điện có thể lệch pha (phase) so với điện áp.

## phức (Complex) number và phasor

Dùng Euler danh tính (identity) `e^{i\omega t}`, ta biểu diễn sinusoid bằng phức phasor. đạo hàm (Derivative) theo time biến thành multiplication bởi `iω`, giúp các phương trình vi phân (differential equations) của mạch điện (circuit) thành algebra.

trở kháng (Trở kháng / 임피던스) tổng quát hóa điện trở (resistance):

```math
Z_R=R,
\qquad
Z_C=\frac{1}{i\omega C},
\qquad
Z_L=i\omega L.
```

độ lớn (Magnitude) của trở kháng cho ratio biên độ (amplitude) `V/I`; argument cho pha shift.

## Series RLC

Với series RLC:

```math
Z=R+i\left(\omega L-\frac{1}{\omega C}\right).
```

Khi

```math
\omega_0=\frac{1}{\sqrt{LC}},
```

reactive parts cancel. Đây là điện (electrical) cộng hưởng. Nó cùng mathematical cấu trúc (structure) với driven damped bộ dao động (oscillator): `L` đóng vai inertia, `1/C` đóng vai restoring độ cứng (stiffness), `R` đóng vai tắt dần (damping).

## Quality hệ số (factor) và bandwidth

Một resonator tổn hao (loss) thấp có peak đáp ứng (response) hẹp. Quality hệ số `Q` đo rough ratio giữa năng lượng stored và năng lượng lost mỗi cycle. High-Q useful cho tần số (frequency) selection và bộ dao động, nhưng đáp ứng time cũng dài hơn. tần số selectivity và time localization có trade-off kiểu Fourier.

## RMS và công suất (power)

Với sinusoid, RMS điện áp

```math
V_{rms}=\frac{V_0}{\sqrt 2}
```

cho cùng trung bình (average) công suất trên resistor như DC điện áp bằng `V_rms`. Trong general AC tải (load), thực (real) công suất phụ thuộc pha:

```math
P=V_{rms}I_{rms}\cos\phi.
```

`cosφ` là công suất hệ số. Reactive dòng điện có thể làm dây và equipment phải chịu dòng điện dù không tạo net work trung bình trên tải.

## Filters

RC, RL và RLC networks tạo low-pass, high-pass, dải (band)-pass hay notch hành vi (behavior). Đây là bridge từ physics sang xử lý tín hiệu (signal processing): mạch điện transfer function `H(ω)` nói tần số thành phần (component) nào đi qua và thành phần nào bị suy giảm.

## Mô hình tư duy (Mental Model)

AC mạch điện lý thuyết (theory) là sóng (wave)/oscillation lý thuyết ở dạng lumped network. phức trở kháng không phải “điện trở tưởng tượng”; nó mã hóa đồng thời biên độ đáp ứng và pha đáp ứng.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [DC circuits](01_dc_circuits.md), [Dao động và resonance](../02_oscillations_waves/00_oscillations_resonance.md), [Số phức](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Transmission lines](05_transmission_lines_waveguides.md).

## phức trở kháng không phải “điện trở tưởng tượng”

Trong sinusoidal trạng thái xác lập, ta biểu diễn điện áp/current bằng phasor để biến đạo hàm theo thời gian thành phép nhân `iω`. Khi đó resistor, inductor và capacitor có trở kháng:

```math
Z_R=R,
\qquad
Z_L=i\omega L,
\qquad
Z_C=\frac{1}{i\omega C}=-\frac{i}{\omega C}.
```

Phần imaginary không có nghĩa linh kiện có “điện trở ảo”. Nó encode pha quan hệ (relation) giữa điện áp và dòng điện. Resistor tiêu tán năng lượng trung bình; lý tưởng inductor/capacitor luân phiên lưu năng lượng trong magnetic/electric trường (field) rồi trả lại nguồn.

Với series RLC:

```math
Z=R+i\left(\omega L-\frac{1}{\omega C}\right).
```

biên độ dòng điện là `I=V/|Z|`, còn pha shift là argument của `Z`. Đây là một ứng dụng tự nhiên của phức number: một vật thể (object) đại số mang đồng thời độ lớn và pha.

## cộng hưởng, bandwidth và quality hệ số

Series cộng hưởng xảy ra khi reactances cancel:

```math
\omega_0L=\frac{1}{\omega_0C}
```

nên

```math
\omega_0=\frac{1}{\sqrt{LC}}.
```

Tại cộng hưởng, lý tưởng series RLC có trở kháng nhỏ nhất `R`, dòng điện lớn nhất. Nhưng cộng hưởng không tạo năng lượng từ không khí; biên độ lớn vì năng lượng được trao đổi nhiều lần giữa `L` và `C`, còn nguồn chỉ cần bù losses mỗi cycle.

Quality hệ số của weakly damped series resonator gần

```math
Q=\frac{\omega_0L}{R}
=\frac{1}{\omega_0RC}.
```

`Q` lớn nghĩa năng lượng stored lớn so với năng lượng dissipated mỗi cycle, cộng hưởng hẹp hơn. Bandwidth gần `Δω≈ω_0/Q` trong simple chế độ (regime). Filter design, RF tuning, tinh thể (crystal) bộ dao động và cavity cộng hưởng đều dùng mô hình tư duy (mental model) “stored năng lượng / tổn hao / bandwidth”.

## trung bình công suất và công suất hệ số

Nếu RMS điện áp/current lệch pha `φ`, trung bình thực công suất là

```math
P=V_{rms}I_{rms}\cos\phi.
```

`cosφ` là công suất hệ số trong simple sinusoidal case. Reactive dòng điện vẫn làm tăng dòng điện qua dây và losses `I^2R` dù net năng lượng mỗi cycle có thể được trả về nguồn. Vì vậy công suất-hệ số correction có ý nghĩa thực tế trong điện công suất các hệ (systems).

phức công suất thường được tổ chức thành

```math
S=P+iQ_r,
```

trong đó `P` là thực công suất và `Q_r` là reactive công suất; ký hiệu `Q_r` ở đây tránh nhầm với quality hệ số `Q`.

## Transient và trạng thái xác lập (steady-state) là hai câu hỏi khác nhau

Phasor method chỉ mô tả sinusoidal trạng thái xác lập. Khi vừa đóng switch, mạch điện còn transient determined bởi phương trình vi phân (differential equation) và các điều kiện ban đầu (initial conditions). Natural đáp ứng của RLC có tắt dần các chế độ (regimes) giống mechanical bộ dao động: overdamped, critically damped và underdamped.

Đây là cùng một mathematical cấu trúc:

```math
\frac{d^2x}{dt^2}+2\gamma\frac{dx}{dt}+\omega_0^2x=f(t)
```

có thể đại diện độ dịch chuyển (displacement) cơ học hoặc điện tích (charge)/current mạch điện sau khi map các tham số (parameters). liên hệ (Connection) này cho phép intuition về cộng hưởng/damping chuyển giữa cơ học (mechanics), acoustics, electronics và control các hệ.

## tần số đáp ứng, filters và Bode thinking

Thay vì hỏi mạch điện phản ứng với một tần số duy nhất, ta định nghĩa transfer function `H(iω)=V_out/V_in`. Low-pass, high-pass, dải-pass và notch filters là cách shaping biên độ/phase theo tần số.

Bode plot dùng logarithmic tần số trục (axis) vì các hệ thường trải nhiều orders of độ lớn và poles/zeros tạo độ dốc (slope) đơn giản theo dB/decade. Đây là liên hệ trực tiếp giữa logarithm, phương trình vi phân, Fourier analysis và practical electronics.

## các ngộ nhận thường gặp (Common Misconceptions) bổ sung

### “Ở cộng hưởng, điện áp ở mọi linh kiện đều bằng nguồn điện áp”

Không. Trong series RLC có `Q` cao, điện áp across `L` hoặc `C` riêng lẻ có thể lớn hơn nguồn nhiều lần nhưng gần opposite pha nên tổng phasor vẫn phù hợp Kirchhoff định luật (law).

### “AC dòng điện thật sự chạy qua điện môi (dielectric) của capacitor như dẫn (conduction) dòng điện”

Trong lý tưởng capacitor không có các hạt tải điện (charge carriers) xuyên qua điện môi theo kiểu resistor. dòng điện ở leads gắn việc điện tích plates thay đổi; Maxwell độ dịch chuyển dòng điện giữ consistency của trường mô tả (description) trong vùng điện môi.
