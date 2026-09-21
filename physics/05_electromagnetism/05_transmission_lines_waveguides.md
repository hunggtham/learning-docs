# Đường truyền, lan truyền tín hiệu, phản xạ và ống dẫn sóng

Trong mạch tần số thấp, ta thường giả định một dây dẫn là một node có cùng điện áp tại mọi điểm ở cùng thời điểm. Giả định này chỉ đúng khi thời gian lan truyền dọc dây nhỏ hơn nhiều thang thời gian biến thiên của tín hiệu. Khi dây đủ dài hoặc cạnh tín hiệu đủ nhanh, điện áp và dòng điện trở thành các trường phụ thuộc cả vị trí lẫn thời gian. Khi đó phải dùng mô hình đường truyền (transmission line).

## Từ mạch tập trung đến hệ phân bố

Một đoạn rất ngắn `dx` của đường truyền có thể được mô hình bằng bốn tham số trên một đơn vị chiều dài:

- điện trở nối tiếp `R'` với đơn vị `Ω/m`;
- điện cảm nối tiếp `L'` với đơn vị `H/m`;
- điện dẫn rò song song `G'` với đơn vị `S/m`;
- điện dung song song `C'` với đơn vị `F/m`.

Áp dụng Kirchhoff cho phần tử vi phân rồi lấy giới hạn `dx→0` cho phương trình telegrapher:

```math
\frac{\partial V}{\partial x}
=-R'I-L'\frac{\partial I}{\partial t},
```

```math
\frac{\partial I}{\partial x}
=-G'V-C'\frac{\partial V}{\partial t}.
```

Đây là cầu nối giữa mạch điện và phương trình trường. `V(x,t)` và `I(x,t)` không còn là hai số duy nhất cho cả dây mà là các đại lượng phân bố dọc không gian.

## Đường truyền lý tưởng không tổn hao

Nếu

```math
R'=0,\qquad G'=0,
```

thì

```math
\frac{\partial V}{\partial x}
=-L'\frac{\partial I}{\partial t},
```

```math
\frac{\partial I}{\partial x}
=-C'\frac{\partial V}{\partial t}.
```

Lấy thêm đạo hàm và khử `I` hoặc `V` cho

```math
\frac{\partial^2V}{\partial x^2}
=L'C'\frac{\partial^2V}{\partial t^2},
```

```math
\frac{\partial^2I}{\partial x^2}
=L'C'\frac{\partial^2I}{\partial t^2}.
```

Đây là phương trình sóng với vận tốc

```math
v=\frac{1}{\sqrt{L'C'}}.
```

Trong đường truyền TEM nằm trong môi trường điện môi có `\mu,\varepsilon`, giá trị này thường gần

```math
v\approx\frac{1}{\sqrt{\mu\varepsilon}}.
```

Do đó tín hiệu không truyền tức thời dọc dây.

## Trở kháng đặc trưng

Với sóng chạy tới trên đường truyền lý tưởng, tỉ số điện áp trên dòng điện là

```math
Z_0=\sqrt{\frac{L'}{C'}}.
```

`Z_0` là trở kháng đặc trưng (characteristic impedance), không phải điện trở DC của sợi dây.

Một coax `50 Ω` có thể có điện trở DC rất nhỏ nhưng vẫn có `Z_0≈50 Ω`. Lý do là `Z_0` mô tả quan hệ giữa điện trường và từ trường của sóng lan truyền, tức cách năng lượng được chia giữa điện dung và điện cảm phân bố.

## Sóng tới và sóng phản xạ

Điện áp tổng trên đường truyền là tổng của sóng đi tới và sóng đi ngược:

```math
V(x)=V^+e^{-i\beta x}+V^-e^{i\beta x}.
```

Dòng điện tương ứng trong trường hợp lossless là

```math
I(x)=\frac{V^+}{Z_0}e^{-i\beta x}
-\frac{V^-}{Z_0}e^{i\beta x}.
```

Dấu trừ ở thành phần phản xạ của dòng phản ánh việc sóng này truyền theo hướng ngược.

## Hệ số phản xạ tại tải

Tại tải `Z_L`, hệ số phản xạ điện áp là

```math
\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0}.
```

Nếu

```math
Z_L=Z_0,
```

thì

```math
\Gamma_L=0,
```

và không có phản xạ lý tưởng.

Với hở mạch,

```math
Z_L\to\infty
\quad\Rightarrow\quad
\Gamma_L\to+1.
```

Với ngắn mạch,

```math
Z_L=0
\quad\Rightarrow\quad
\Gamma_L=-1.
```

Phản xạ không phải “lỗi số”. Nó là hệ quả của điều kiện biên: tải không chấp nhận đúng tỉ số `V/I` mà sóng tới mang theo, nên một sóng ngược phải xuất hiện để thỏa điều kiện tải.

## Bảo toàn năng lượng và công suất phản xạ

Nếu `Z_0` và tải đều thực, tỉ lệ công suất phản xạ là

```math
\frac{P_r}{P_i}=|\Gamma|^2.
```

Tỉ lệ công suất truyền vào tải là

```math
\frac{P_L}{P_i}=1-|\Gamma|^2.
```

Trong hệ không tổn hao, năng lượng không biến mất tại mismatch; phần không đi vào tải quay trở lại nguồn hoặc tiếp tục phản xạ ở các discontinuities khác.

## Sóng đứng và VSWR

Sóng tới và sóng phản xạ chồng chập tạo mẫu sóng đứng. Điện áp cực đại và cực tiểu thay đổi theo vị trí.

Voltage standing-wave ratio (VSWR) là

```math
VSWR=\frac{V_{max}}{V_{min}}
=\frac{1+|\Gamma|}{1-|\Gamma|}.
```

Nếu `\Gamma=0`, VSWR bằng 1. VSWR lớn cho biết mismatch mạnh.

Trong RF, antenna feedline và microwave systems, VSWR là một phép đo thực dụng của chất lượng matching.

## Đường truyền có tổn hao

Trong trạng thái điều hòa `e^{i\omega t}`, hằng số lan truyền là

```math
\gamma=\alpha+i\beta
=\sqrt{(R'+i\omega L')(G'+i\omega C')}.
```

`\alpha` là hệ số suy hao, `\beta` là hằng số pha.

Trở kháng đặc trưng tổng quát là

```math
Z_0=
\sqrt{\frac{R'+i\omega L'}{G'+i\omega C'}}.
```

Khi loss nhỏ,

```math
R'\ll\omega L',
\qquad
G'\ll\omega C',
```

thì `Z_0` gần giá trị lossless và `\alpha` nhỏ nhưng không bằng không.

Skin effect, dielectric loss và surface roughness làm suy hao tăng ở tần số cao.

## Khi nào phải bỏ mô hình lumped circuit?

Điều kiện không chỉ phụ thuộc carrier frequency. Tín hiệu số có cạnh nhanh chứa nhiều thành phần Fourier cao tần.

Nếu propagation delay một chiều

```math
t_d=\frac{\ell}{v}
```

không còn rất nhỏ so với rise time `t_r`, đường nối nên được xem là transmission line.

Một quy tắc kỹ thuật thường dùng là khi

```math
t_d\gtrsim\frac{t_r}{6}
```

hoặc cùng bậc với `t_r`, reflection và distributed effects có thể đáng kể. Hệ số chính xác phụ thuộc yêu cầu signal integrity, nhưng tư tưởng cốt lõi là **edge speed quan trọng hơn clock frequency đơn thuần**.

## Ví dụ: PCB trace dài 15 cm

Giả sử vận tốc truyền trên PCB khoảng

```math
v=1.7\times10^8\,m/s.
```

Với chiều dài

```math
\ell=0.15\,m,
```

delay một chiều là

```math
t_d=\frac{0.15}{1.7\times10^8}
\approx0.88\,ns.
```

Nếu driver có rise time `5 ns`, lumped approximation có thể còn tạm chấp nhận tùy yêu cầu. Nhưng nếu rise time chỉ `0.5 ns`, delay đã lớn hơn rise time; trace chắc chắn phải được xem như một đường truyền.

## Trở kháng nhìn vào của đường truyền hữu hạn

Đường truyền lossless dài `\ell`, tải `Z_L`, có input impedance

```math
Z_{in}
=Z_0
\frac{Z_L+iZ_0\tan(\beta\ell)}
{Z_0+iZ_L\tan(\beta\ell)}.
```

Điều này cho thấy một đường truyền không chỉ “nối tải đến nguồn”; nó có thể biến đổi trở kháng theo chiều dài và pha.

Với đoạn quarter-wave

```math
\ell=\frac{\lambda}{4},
```

trong trường hợp lý tưởng,

```math
Z_{in}=\frac{Z_0^2}{Z_L}.
```

Nếu muốn match nguồn `Z_S` với tải `Z_L`, có thể chọn

```math
Z_0=\sqrt{Z_SZ_L}.
```

Đây là quarter-wave transformer. Nó hoạt động tốt quanh một dải tần hữu hạn chứ không broadband vô hạn.

## Smith chart là gì về mặt vật lý?

Smith chart biểu diễn trở kháng chuẩn hóa và hệ số phản xạ trên cùng một hình học phức. Nó không phải công cụ “đoán mạch” bí ẩn; nó là ánh xạ hình học của phép biến đổi Möbius

```math
\Gamma=\frac{z-1}{z+1},
```

với

```math
z=\frac{Z}{Z_0}.
```

Di chuyển dọc đường truyền tương ứng quay pha của `\Gamma`. Vì vậy Smith chart trực quan hóa quá trình reflection và impedance transformation.

## Ống dẫn sóng khác đường truyền TEM như thế nào?

Trong coax hoặc hai dây lý tưởng, mode TEM có điện trường và từ trường đều ngang với hướng truyền và không có cutoff lý tưởng.

Trong ống dẫn sóng kim loại rỗng, điều kiện biên không cho mode TEM đơn giản. Các mode TE và TM có cấu trúc trường riêng và có tần số cutoff.

Với một mode,

```math
\beta^2
=\frac{\omega^2}{c^2}-k_c^2.
```

Nếu

```math
\omega<\omega_c,
```

thì `\beta` trở thành thuần ảo và trường suy giảm theo chiều dài thay vì lan truyền tự do. Đây là mode evanescent.

## Ống dẫn sóng chữ nhật

Với waveguide chữ nhật kích thước `a×b`, cutoff của mode `TE_{mn}` hoặc `TM_{mn}` có dạng

```math
f_{c,mn}
=\frac{c}{2}
\sqrt{
\left(\frac{m}{a}\right)^2+
\left(\frac{n}{b}\right)^2
}.
```

Mode cơ bản thường là `TE_{10}` nếu `a>b`, nên

```math
f_c\approx\frac{c}{2a}.
```

Điều kiện biên hình học đã biến bài toán Maxwell thành bài toán trị riêng. Cùng cấu trúc toán học xuất hiện ở dây đàn, cavity, particle in a box và phonon modes.

## Vận tốc pha và vận tốc nhóm trong waveguide

Trên cutoff,

```math
v_p=\frac{\omega}{\beta}
```

có thể lớn hơn `c`.

Điều này không vi phạm tương đối tính vì vận tốc pha không phải vận tốc truyền tín hiệu hoặc năng lượng.

Trong waveguide lý tưởng,

```math
v_pv_g=c^2,
```

nên khi `v_p>c`, vận tốc nhóm `v_g<c`.

## Liên hệ với signal integrity và Computer Engineering

Một bit trên PCIe, DDR hay Ethernet cuối cùng vẫn là một cấu trúc trường điện từ lan truyền trong interconnect. Protocol có thể là rời rạc, nhưng physical layer phải tuân Maxwell, Fourier, noise và boundary conditions.

Reflection có thể tạo ringing, overshoot, undershoot, crossing-time shift và eye-diagram closure. Do đó nhiều “bug digital” ở tốc độ cao thực chất là vấn đề vật lý tương tự sóng trên dây.

Termination resistor, controlled impedance PCB trace, differential pair và return-path design đều là cách kiểm soát điều kiện biên của trường điện từ.

## Giới hạn của mô hình transmission line

Mô hình một chiều giả định chỉ một mode đáng kể và tiết diện ngang nhỏ so với bước sóng tương ứng. Khi tần số đủ cao để kích thích higher-order modes, hoặc discontinuity có hình học ba chiều phức tạp, cần full-wave electromagnetic simulation.

Các tham số `R',L',G',C'` cũng có thể phụ thuộc tần số do skin effect, dispersion và dielectric loss. Vì vậy dùng hằng số cố định trên dải rất rộng có thể sai.

## Mô hình tư duy (Mental Model)

Một interconnect tốc độ cao không phải “dây mang điện áp tức thời”. Nó là **một cấu trúc dẫn sóng có năng lượng điện trường và từ trường phân bố**. `Z_0` mô tả tỉ số trường của sóng chạy; tải đặt điều kiện biên; mismatch tạo phản xạ; hình học đặt mode và cutoff.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Clock thấp thì không cần transmission-line analysis”

Không nhất thiết. Rise/fall time quyết định thành phần tần số cao của cạnh số và thường quan trọng hơn tần số clock danh nghĩa.

### “50 Ω là điện trở DC của coax”

Không. Đây là characteristic impedance của mode truyền, bắt nguồn từ `L'` và `C'` phân bố.

### “Phase velocity lớn hơn `c` nghĩa là truyền thông tin nhanh hơn ánh sáng”

Không. Phase velocity không trực tiếp là signal velocity. Nhân quả vẫn được bảo toàn.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Maxwell và sóng điện từ](04_maxwell_em_waves.md), [Mạch AC/RLC](02_ac_rlc_circuits.md), [Sóng và Fourier](../02_oscillations_waves/01_waves_fourier_sound.md).

**Liên hệ tiếp:** [Quang sóng](../06_optics/01_wave_optics.md), [Bán dẫn và thiết bị](../10_condensed_matter_devices/01_semiconductors_devices.md).