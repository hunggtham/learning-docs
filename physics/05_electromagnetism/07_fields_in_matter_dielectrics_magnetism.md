# Điện từ trường trong vật chất: điện môi (dielectric), phân cực (polarization), magnetization và vật liệu từ

## Vì sao điện từ học trong vacuum chưa đủ?

Khi viết Coulomb định luật (law) hoặc Maxwell các phương trình (equations) trong chân không, ta đang mô tả điện tích (electric charge) và dòng điện (current) như những nguồn (source) có thể chỉ ra trực tiếp. Nhưng vật liệu thật chứa electron và hạt nhân (nucleus) liên kết trong nguyên tử (atom), phân tử (molecule) hoặc tinh thể (crystal). Khi đặt vật liệu vào điện trường hay từ trường, những điện tích (charge) vi mô (microscopic) này dịch chuyển hoặc tái sắp xếp một chút. Kết quả là trường mà ta đo ở thang (scale) vĩ mô (macroscopic) không còn chỉ do “tự do (free) điện tích” bên ngoài tạo ra; vật liệu tự sinh thêm đáp ứng (response) của chính nó.

Đây là lý do xuất hiện các khái niệm **phân cực điện (Polarization / 분극)**, **điện môi (Dielectric / 유전체)**, **từ hóa (Magnetization / 자화)** và các auxiliary các trường (fields) `D`, `H`. Chúng không phải những trường (field) hoàn toàn mới độc lập với `E` và `B`; chúng là cách tổ chức đáp ứng của vật chất để bài toán vĩ mô dễ đọc hơn.

## phân cực: điện trường làm gì bên trong vật chất?

Xét một nguyên tử trung hòa. Nếu không có bên ngoài (external) trường, center của positive hạt nhân (nuclear) điện tích và electron cloud có thể trùng nhau theo đối xứng (symmetry). Khi đặt điện trường (electric field) `\vec E`, electron cloud và hạt nhân bị kéo theo hai hướng ngược nhau. Nếu độ dịch chuyển (displacement) nhỏ, nguyên tử có electric dipole mômen (moment) cảm ứng.

Electric dipole mômen (Electric Dipole Moment / 전기 쌍극자 모멘트) của hai điện tích `+q` và `-q` cách nhau vectơ (vector) `\vec d` là

```math
\vec p=q\vec d.
```

Ở vật liệu có nhiều dipoles, ta định nghĩa phân cực vectơ là dipole mômen trên một đơn vị thể tích:

```math
\vec P = \frac{d\vec p_{\mathrm{total}}}{dV}.
```

Điểm quan trọng là phân cực biến sự dịch chuyển vi mô của rất nhiều điện tích thành một trường vĩ mô. Sự thay đổi của `P` tạo ra **bound điện tích**. Trong bulk,

```math
\rho_b=-\nabla\cdot\vec P,
```

còn trên bề mặt (surface) có

```math
\sigma_b=\vec P\cdot\hat n.
```

Các công thức này nói rằng bound điện tích xuất hiện nơi phân cực “bắt đầu, kết thúc hoặc thay đổi mật độ”. mô hình tư duy (Mental model) này gần với divergence của một thông lượng (flux) trường: nếu các dipole các vectơ (vectors) xếp đều trong bulk thì positive end của dipole này gần cancel negative end của dipole kế bên; điện tích còn lộ ra rõ nhất ở boundary hoặc vùng `P` thay đổi.

## Điện môi tuyến tính và permittivity

Trong nhiều điện môi ở trường không quá mạnh, đáp ứng gần tuyến tính:

```math
\vec P=\varepsilon_0\chi_e\vec E,
```

với `\chi_e` là electric susceptibility (전기 감수율). Khi đó độ dịch chuyển trường

```math
\vec D=\varepsilon_0\vec E+\vec P
```

trở thành

```math
\vec D=\varepsilon\vec E,
```

trong đồng nhất (homogeneous) đẳng hướng (isotropic) tuyến tính (linear) vật liệu (material), với

```math
\varepsilon=\varepsilon_0\varepsilon_r
=\varepsilon_0(1+\chi_e).
```

`\varepsilon_r` là relative permittivity, thường được gọi điện môi hằng số (constant) trong context đơn giản. Nhưng “hằng số” có thể phụ thuộc tần số (frequency), nhiệt độ (temperature) và trường độ bền (strength), nên trong vật liệu science cách gọi permittivity chính xác hơn.

Gauss định luật vĩ mô được viết

```math
\nabla\cdot\vec D=\rho_f,
```

với `\rho_f` là tự do điện tích mật độ (density). Đây là bookkeeping rất hữu ích: bound điện tích đã được hấp thụ vào `P` và `D`, còn nguồn explicit trong phương trình là tự do điện tích.

## Tại sao tụ điện tăng điện dung (capacitance) khi chèn điện môi?

Với parallel-plate capacitor lý tưởng diện tích `A`, separation `d`, vacuum điện dung là

```math
C_0=\frac{\varepsilon_0 A}{d}.
```

Khi chèn điện môi đầy khoảng giữa hai bản, phân cực tạo bound charges có trường đối nghịch một phần với trường do tự do điện tích trên plate. Nếu giữ fixed tự do điện tích `Q`, net `E` giảm, nên điện áp (voltage) độ chênh (difference) giảm. Vì

```math
C=\frac{Q}{V},
```

điện dung tăng:

```math
C=\frac{\varepsilon A}{d}=\varepsilon_r C_0.
```

Điều này không có nghĩa điện môi “tạo thêm điện tích miễn phí”. Nó cho phép cùng một điện áp hỗ trợ nhiều tự do điện tích hơn trên plates nhờ phân cực làm thay đổi quan hệ (relation) giữa điện tích và trường.

Trong electronics, đây là physics cốt lõi của capacitor, oxide cổng (gate oxide) trong MOSFET và high-`k` dielectrics. Khi transistor thu nhỏ, muốn gate control mạnh mà dòng rò (leakage) không quá lớn, các vật liệu (materials) có permittivity cao cho phép tăng hiệu dụng (effective) điện dung mà không bắt buộc oxide vật lý (physical) thickness nhỏ tương ứng.

## Năng lượng điện trường trong điện môi

Với tuyến tính môi trường (medium), năng lượng (energy) mật độ thường được viết

```math
u_E=\frac12\vec E\cdot\vec D.
```

Cần cẩn thận: trong dispersive hoặc phi tuyến (nonlinear) media, cách phân chia năng lượng giữa trường và vật liệu bậc tự do (degrees of freedom) phức tạp hơn. Công thức trên là mô hình (model) hữu ích trong miền tuyến tính, quasi-tĩnh (static) phù hợp.

## tần số dependence và điện môi tổn hao (loss)

phân cực không phản ứng tức thời ở mọi tần số. điện tử (Electronic) cloud có timescale khác ionic độ dịch chuyển, phân tử (molecular) quay (rotation) hoặc interfacial phân cực. Khi trường oscillate quá nhanh, một cơ chế đáp ứng có thể không theo kịp. Vì thế `\varepsilon` phụ thuộc tần số và có thể được biểu diễn bằng phức (complex) permittivity:

```math
\varepsilon(\omega)=\varepsilon'(\omega)-i\varepsilon''(\omega).
```

Phần thực (real) liên hệ stored đáp ứng, phần imaginary liên hệ dissipation/loss. Đây là lý do điện môi tổn hao quan trọng trong RF, microwave PCB, antenna substrate và high-tốc độ (speed) tín hiệu (signal) integrity. Một vật liệu “cách điện tốt ở DC” chưa chắc là môi trường ít tổn hao ở GHz.

## Ferroelectric: phân cực có thể tự tồn tại

Một số các vật liệu có spontaneous phân cực ngay cả khi bên ngoài trường bằng không (zero). Ferroelectric các vật liệu (강유전체) có hysteresis giữa `P` và `E`; domain phân cực có thể được đảo bằng trường. Chúng được dùng trong các cảm biến (sensors), actuators, high-permittivity capacitors và một số nonvolatile memories.

liên hệ (Connection) sâu ở đây là **chuyển pha (phase transition) + đối xứng breaking**: trên một nhiệt độ đặc trưng, tinh thể có thể có đối xứng cao; dưới chuyển mức (transition), hệ (system) chọn một phân cực direction, làm đối xứng giảm và tạo order tham số (parameter) khác không.

## Magnetization: đáp ứng từ của vật chất

Magnetic đáp ứng có nguồn vi mô từ orbital mômen động lượng (angular momentum) và spin của charged các hạt (particles). Ta định nghĩa magnetization (Magnetization / 자화)

```math
\vec M=\frac{d\vec \mu_{\mathrm{mag,total}}}{dV},
```

là magnetic dipole mômen trên unit thể tích (volume).

Magnetization có thể được biểu diễn như bound currents:

```math
\vec J_b=\nabla\times\vec M,
```

và bề mặt bound dòng điện

```math
\vec K_b=\vec M\times\hat n.
```

Ta đưa vào auxiliary từ trường (magnetic field)

```math
\vec H=\frac{1}{\mu_0}\vec B-\vec M.
```

Ampère–Maxwell định luật vĩ mô khi đó có thể viết sao cho nguồn explicit là tự do dòng điện.

## nghịch từ (Diamagnetism), thuận từ (paramagnetism) và sắt từ (ferromagnetism)

**nghịch từ (반자성)** là đáp ứng tạo magnetic mômen ngược trường applied. Về cơ học lượng tử (quantum mechanics), đây không chỉ là “electron loop chống lại trường” theo cổ điển (classical) picture; orbital các trạng thái (states) thay đổi dưới vectơ thế (potential) và induced currents tạo susceptibility âm nhỏ.

**thuận từ (상자성)** xuất hiện khi nguyên tử/ion có vĩnh viễn (permanent) magnetic moments nhưng nhiệt (thermal) agitation làm chúng định hướng ngẫu nhiên khi không có trường. Applied trường độ chệch (bias) phân bố (distribution) một chút, tạo magnetization cùng chiều trường. Khi nhiệt độ tăng, alignment khó duy trì hơn; simple Curie-like hành vi (behavior) có susceptibility giảm theo `1/T` trong một số chế độ (regime).

**sắt từ (강자성)** sâu hơn nhiều: trao đổi (exchange) tương tác (interaction) — lượng tử (quantum) hiệu ứng (effect) liên hệ hàm sóng (wavefunction) đối xứng và Coulomb tương tác — làm neighboring moments có xu hướng order collectively. vật liệu chia thành domains để giảm tổng năng lượng. vĩnh viễn magnet hình thành khi domain cấu hình (configuration) và dị hướng (anisotropy) giữ được remanent magnetization.

Vì vậy câu “magnet là do tất cả electron quay cùng chiều” là quá thô và có thể sai. từ tính (Magnetism) của chất rắn (solid) là many-body lượng tử phenomenon gắn cấu trúc vùng năng lượng (band structure), trao đổi, tinh thể dị hướng và domains.

## B–H curve và hysteresis

Trong ferromagnet, quan hệ giữa `B` và `H` không tuyến tính đơn giản. Khi cycle applied trường, hệ có hysteresis loop. Remanence cho biết magnetization còn lại khi bên ngoài trường trở về không; coercive trường cho biết trường ngược cần để xóa/đảo magnetization.

Soft magnetic các vật liệu có coercivity thấp, phù hợp transformer cores vì dễ đảo magnetization với low tổn hao. Hard magnetic các vật liệu có coercivity cao, phù hợp vĩnh viễn magnets. Đây là ví dụ rất rõ rằng “cùng là magnetic vật liệu” nhưng desired tính chất vật lý (physical property) phụ thuộc application.

## các điều kiện biên (Boundary conditions) và mặt phân cách (interface)

Khi trường đi qua mặt phân cách giữa hai media, normal/tangential các thành phần (components) tuân Maxwell các điều kiện biên. Ví dụ, nếu không có tự do bề mặt điện tích,

```math
\hat n\cdot(\vec D_2-\vec D_1)=0.
```

Nếu không có tự do bề mặt dòng điện,

```math
\hat n\times(\vec H_2-\vec H_1)=0.
```

Các điều kiện này là nền cho capacitor hình học (geometry), điện môi ống dẫn sóng (waveguide), quang học (optical) refraction và điện từ (electromagnetic) mô phỏng (simulation). hữu hạn (Finite)-element solvers trong kỹ thuật (engineering) thực chất đang giải PDE + constitutive relations + các điều kiện biên trên hình học phức tạp.

## Mô hình tư duy (Mental Model)

> `E` và `B` mô tả trường điện từ (electromagnetic field) vật lý. `P` và `M` mô tả cách vật chất phản ứng ở thang vĩ mô. `D` và `H` là cách tổ chức các nguồn “tự do” và đáp ứng “bound” để Maxwell các phương trình dễ giải hơn trong các vật liệu.

Khi nhìn một capacitor, MOSFET gate, ferrite lõi (core) hay magnetic memory, đừng nghĩ vật liệu chỉ là “thứ đặt vào giữa trường”. vật liệu là một dynamical collection của điện tích và magnetic moments; chính đáp ứng tập thể (collective) của chúng thay đổi quan hệ giữa nguồn và trường.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “điện môi chỉ là vật cách điện, nên nó không làm gì với trường”

Sai. Nó có thể không dẫn DC dòng điện đáng kể nhưng vẫn phân cực mạnh. Chính đáp ứng này thay đổi điện dung, sóng (wave) vận tốc (velocity), trở kháng (impedance) và năng lượng storage.

### “`D` là điện trường mới và độc lập với `E`”

Không. `D` là auxiliary trường được định nghĩa từ `E` và phân cực. vật lý cách diễn giải (interpretation) cần luôn gắn constitutive quan hệ của vật liệu.

### “sắt từ chỉ là cổ điển dipoles tự xếp hàng”

cổ điển dipole tương tác một mình không đủ giải thích thang và độ ổn định (stability) của ferromagnetic order. trao đổi tương tác và thống kê lượng tử (quantum statistics) là phần cốt lõi.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Electrostatics](00_electrostatics.md), [Magnetism & induction](03_magnetism_induction.md), [Quantum angular momentum & spin](../08_quantum/02_angular_momentum_spin.md).

**Liên hệ tiếp:** [Wave optics](../06_optics/01_wave_optics.md), [Transmission lines](05_transmission_lines_waveguides.md), [Solid-state magnetism](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md), [Semiconductor devices](../10_condensed_matter_devices/01_semiconductors_devices.md).
