# Hiện tượng vận chuyển: khuếch tán, dẫn nhiệt và dòng theo gradient

## Một cấu trúc lặp lại: gradient tạo thông lượng

Nhiều quá trình tưởng khác nhau có cùng cấu trúc toán học. Khi mật độ, nhiệt độ, nồng độ hoặc thế hóa học không đồng đều trong không gian, hệ thường tạo một thông lượng (flux / 선속) làm giảm chênh lệch đó.

Cấu trúc chung là

```math
\text{flux}
\propto
-\nabla(\text{driving field}).
```

Dấu âm nói dòng đi theo hướng làm giảm gradient.

Ý tưởng này nối cơ học chất lưu, nhiệt động lực học, hóa học, bán dẫn, vật lý vật liệu và cả một số mô hình dữ liệu ngẫu nhiên.

## Định luật Fick và khuếch tán

Với nồng độ `c(\mathbf r,t)`, định luật Fick thứ nhất là

```math
\mathbf J=-D\nabla c,
```

trong đó:

- `\mathbf J` là thông lượng hạt;
- `D` là hệ số khuếch tán có đơn vị `m^2/s`.

Nếu `c` đo số hạt trên một đơn vị thể tích, `\mathbf J` có đơn vị

```text
particles/(m²·s).
```

## Từ bảo toàn tới phương trình khuếch tán

Bảo toàn số hạt có dạng

```math
\frac{\partial c}{\partial t}
+\nabla\cdot\mathbf J=0.
```

Thay Fick vào:

```math
\frac{\partial c}{\partial t}
=D\nabla^2c
```

nếu `D` không đổi.

Đây là phương trình khuếch tán.

Nguồn gốc của nó có hai lớp:

```text
conservation law
+
constitutive relation J = -D∇c
```

Nếu `D` phụ thuộc vị trí hoặc nồng độ, không được kéo nó ra ngoài divergence một cách máy móc. Dạng tổng quát hơn là

```math
\frac{\partial c}{\partial t}
=\nabla\cdot(D\nabla c).
```

## Nghiệm của một nguồn điểm

Trong không gian 1D vô hạn, nếu ban đầu tất cả hạt tập trung gần `x=0`, nghiệm chuẩn hóa của phương trình khuếch tán là Gaussian:

```math
c(x,t)
=\frac{N}{\sqrt{4\pi Dt}}
\exp\left(-\frac{x^2}{4Dt}\right).
```

Độ rộng phân bố tăng theo

```math
\sigma^2=2Dt.
```

Do đó thang khoảng cách khuếch tán là

```math
\ell\sim\sqrt{Dt}.
```

Muốn khuếch tán xa gấp 10 lần cần thời gian khoảng 100 lần.

Đây là lý do khuếch tán cực hiệu quả ở thang tế bào nhưng rất chậm nếu phải vận chuyển vật chất nhiều mét mà không có dòng đối lưu.

## Random walk và nguồn gốc vi mô của scaling `\sqrt t`

Sau `N` bước ngẫu nhiên độc lập độ dài đặc trưng `a`, độ dời trung bình có thể bằng 0 nhưng mean-square displacement tăng như

```math
\langle x^2\rangle\sim Na^2.
```

Nếu mỗi bước mất thời gian `\tau`,

```math
N\sim\frac{t}{\tau},
```

nên

```math
x_{rms}
\sim a\sqrt{\frac{t}{\tau}}.
```

So với

```math
\langle x^2\rangle=2Dt,
```

ta thấy hệ số khuếch tán có bậc

```math
D\sim\frac{a^2}{\tau}
```

bỏ qua hệ số phụ thuộc số chiều.

Khuếch tán vĩ mô vì vậy có thể nổi lên từ chuyển động ngẫu nhiên vi mô và bảo toàn hạt.

## Dẫn nhiệt và định luật Fourier

Thông lượng nhiệt gần cân bằng thường thỏa

```math
\mathbf q=-k\nabla T,
```

trong đó `k` là độ dẫn nhiệt có đơn vị

```text
W/(m·K).
```

Bảo toàn năng lượng cho vật liệu đồng nhất cho

```math
\rho c_p
\frac{\partial T}{\partial t}
=k\nabla^2T,
```

nên

```math
\frac{\partial T}{\partial t}
=\alpha\nabla^2T,
```

với

```math
\alpha=\frac{k}{\rho c_p}.
```

`\alpha` là hệ số khuếch tán nhiệt có đơn vị `m^2/s`.

Một vật có `k` cao dẫn nhiệt mạnh, nhưng tốc độ thay đổi nhiệt độ còn phụ thuộc cả mật độ và nhiệt dung. Vì vậy thermal conductivity và thermal diffusivity không phải cùng một đại lượng.

## Thời gian khuếch tán qua một chiều dài

Từ

```math
\ell\sim\sqrt{\alpha t}
```

suy ra thời gian truyền nhiệt khuếch tán qua chiều dài `L` có bậc

```math
t_D\sim\frac{L^2}{\alpha}.
```

Quan hệ `L^2` rất quan trọng trong engineering: làm một chi tiết dày gấp đôi có thể làm thời gian cân bằng nhiệt tăng gần bốn lần nếu cơ chế vẫn là dẫn nhiệt thuần.

## Vận chuyển động lượng và độ nhớt

Độ nhớt có thể được hiểu như vận chuyển động lượng giữa các lớp chất lưu.

Với chất lưu Newton,

```math
\tau_{xy}
=\mu\frac{\partial v_x}{\partial y}.
```

Độ nhớt động học là

```math
\nu=\frac{\mu}{\rho},
```

cũng có đơn vị `m^2/s`.

Sự giống đơn vị giữa `D`, `\alpha` và `\nu` không phải ngẫu nhiên: cả ba đều mô tả tốc độ một đại lượng được san bằng trong không gian bởi transport vi mô.

## Advection và diffusion

Nếu môi trường còn có dòng vận tốc `\mathbf v`, nồng độ không chỉ khuếch tán mà còn bị mang theo dòng.

Phương trình advection–diffusion điển hình là

```math
\frac{\partial c}{\partial t}
+\mathbf v\cdot\nabla c
=D\nabla^2c
```

cho dòng không nén và `D` hằng.

Hai cơ chế khác nhau:

- advection vận chuyển profile theo dòng có hướng;
- diffusion làm profile lan rộng và trơn hơn.

## Số Péclet

So sánh tốc độ advection với diffusion qua chiều dài `L`:

```math
Pe=\frac{vL}{D}.
```

Nếu

```math
Pe\ll1,
```

diffusion chi phối.

Nếu

```math
Pe\gg1,
```

advection chi phối vận chuyển trên thang đó.

Một hệ có thể diffusion-dominated ở thang nhỏ nhưng advection-dominated ở thang lớn vì `Pe` phụ thuộc `L`.

Đây là ví dụ điển hình của tư duy số vô thứ nguyên.

## Drift và diffusion trong bán dẫn

Dòng hạt tải trong bán dẫn có cả thành phần drift do điện trường và diffusion do gradient nồng độ.

Schematic:

```math
\mathbf J
\sim qn\mu\mathbf E
-qD\nabla n
```

với dấu cụ thể phụ thuộc loại hạt tải và quy ước dòng điện.

Trong tiếp giáp P–N, diffusion ban đầu do chênh nồng độ tạo vùng điện tích không gian. Điện trường bên trong sinh drift ngược lại. Ở cân bằng, hai cơ chế triệt tiêu dòng ròng.

Do đó transport không phải chủ đề tách biệt; nó là nền của electronics.

## Quan hệ Einstein

Gần cân bằng, mobility `\mu` và diffusion coefficient `D` liên hệ bởi

```math
D=\mu k_BT
```

nếu `\mu` được định nghĩa là vận tốc trôi trên một đơn vị lực.

Trong bán dẫn thường dùng mobility điện `\mu_e` với lực `qE`, dẫn tới

```math
D=\mu_e\frac{k_BT}{q}
```

cho hạt tải không suy biến trong điều kiện thích hợp.

Đây là một dạng của quan hệ thăng giáng–tiêu tán: cùng coupling vi mô gây drag cũng quyết định độ mạnh của diffusion nhiệt.

## Boundary conditions quyết định bài toán transport

Cùng phương trình diffusion nhưng biên khác cho nghiệm khác hoàn toàn.

Ví dụ:

### Nồng độ cố định

```math
c|_{boundary}=c_b.
```

### Biên không thông lượng

```math
\mathbf J\cdot\hat n=0.
```

### Trao đổi với môi trường

Thông lượng có thể tỉ lệ với chênh lệch nồng độ hoặc nhiệt độ ở biên.

Trong heat transfer, boundary condition kiểu đối lưu thường có dạng

```math
-k\frac{\partial T}{\partial n}
=h(T-T_\infty).
```

Nếu đặt boundary condition sai, solver có thể hội tụ rất đẹp tới nghiệm của **một bài toán khác**.

## Steady state không có nghĩa không có dòng

Nếu

```math
\frac{\partial c}{\partial t}=0,
```

hệ ở trạng thái dừng.

Nhưng `\mathbf J` không nhất thiết bằng 0.

Một gradient nhiệt ổn định qua thanh kim loại có thể duy trì thông lượng nhiệt không đổi. Đây là trạng thái dừng không cân bằng: profile không đổi theo thời gian nhưng năng lượng vẫn liên tục đi qua hệ.

## Transport coefficients phụ thuộc trạng thái vật liệu

Các hệ số `D,k,\mu,\nu` thường không phải hằng số tuyệt đối.

Chúng có thể phụ thuộc:

- nhiệt độ;
- áp suất;
- nồng độ;
- cấu trúc pha;
- tần số;
- phương tinh thể.

Trong tinh thể dị hướng, conductivity có thể là tensor thay vì scalar:

```math
q_i=-k_{ij}\partial_jT.
```

Do đó dùng một hệ số hằng chỉ là xấp xỉ trong một miền vận hành.

## Liên hệ với Hóa học

Diffusion là nền của:

- phản ứng bị giới hạn bởi transport;
- điện hóa;
- pin;
- corrosion;
- membrane;
- catalyst pore.

Nếu phản ứng hóa học nhanh hơn nhiều diffusion, tốc độ quan sát được có thể bị giới hạn bởi việc reactant tới được vùng phản ứng, không phải bởi kinetic barrier của phản ứng.

Các số vô thứ nguyên như Damköhler so sánh reaction timescale với transport timescale.

## Liên hệ với Computer Science và mô phỏng

Phương trình diffusion là PDE parabolic.

Với finite difference explicit một chiều,

```math
T_i^{n+1}
=T_i^n
+r(T_{i+1}^n-2T_i^n+T_{i-1}^n),
```

trong đó

```math
r=\frac{\alpha\Delta t}{\Delta x^2}.
```

Phương pháp explicit đơn giản có điều kiện ổn định; trong trường hợp chuẩn 1D thường cần

```math
r\le\frac12.
```

Nếu timestep quá lớn, mô phỏng có thể dao động và phát nổ dù hệ nhiệt thật luôn làm trơn gradient.

Do đó numerical stability là tính chất của scheme, không phải bằng chứng hệ vật lý bất ổn.

## Miền áp dụng và giới hạn

Định luật Fick và Fourier là quan hệ tuyến tính gần cân bằng và giả sử local equilibrium đủ tốt.

Ở thang rất nhỏ hoặc thời gian cực ngắn, transport có thể không còn khuếch tán cổ điển. Trong ballistic transport, mean free path có thể so sánh kích thước thiết bị.

Khi gradient rất lớn, vật liệu phi tuyến hoặc có memory, flux có thể không còn tỉ lệ tức thời với gradient.

## Mô hình tư duy (Mental Model)

Hiện tượng vận chuyển có thể được tổ chức thành hai lớp:

```text
conservation law
+
constitutive law linking flux to driving gradient
```

Từ đó sinh ra evolution equation.

Một câu tóm tắt hữu ích là:

> mất cân bằng cục bộ tạo dòng; bảo toàn biến dòng đó thành sự tiến hóa của trường.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Diffusion tạo chuyển động trung bình theo một hướng”

Không nhất thiết. Trong diffusion thuần, mean displacement có thể bằng 0 trong khi variance tăng.

### “Steady state nghĩa không có transport”

Không. Một dòng không đổi có thể tồn tại dù profile không thay đổi theo thời gian.

### “Thermal conductivity lớn nghĩa vật sẽ nóng lên nhanh nhất”

Chưa đủ. Tốc độ cân bằng nhiệt còn phụ thuộc `\rho c_p`, hình học và boundary condition; thermal diffusivity `\alpha` mới phản ánh thang thời gian diffusion nhiệt trực tiếp hơn.

### “Hệ số diffusion luôn là một hằng số vật liệu cố định”

Không. Nó có thể phụ thuộc nhiệt độ, nồng độ và cấu trúc vi mô.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Gradient và PDE](../00_foundations/03_mathematical_language.md), [PDE và điều kiện biên](../00_foundations/05_pde_boundary_green_tensors.md), [Nhiệt động lực học](../04_thermal_statistical/00_thermodynamics.md).

**Liên hệ tiếp:** [Động lực ngẫu nhiên](../04_thermal_statistical/04_stochastic_nonequilibrium.md), [Thăng giáng–tiêu tán](../04_thermal_statistical/07_linear_response_fluctuation_dissipation.md), [Thiết bị bán dẫn](../10_condensed_matter_devices/01_semiconductors_devices.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md).
