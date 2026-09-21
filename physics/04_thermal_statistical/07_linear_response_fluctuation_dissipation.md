# Đáp ứng tuyến tính và định lý thăng giáng–tiêu tán

## Câu hỏi trung tâm

Khi một hệ đang gần cân bằng bị tác động rất yếu, đáp ứng của nó thường gần tuyến tính theo nhiễu loạn ngoài. Điều sâu hơn là **cách hệ tiêu tán năng lượng khi bị kích thích** liên hệ trực tiếp với **các thăng giáng tự phát của chính hệ khi không bị kích thích**.

Đây là nội dung trung tâm của lý thuyết đáp ứng tuyến tính (linear-response theory) và các quan hệ thăng giáng–tiêu tán (fluctuation–dissipation relations / 요동-소산 관계).

Khung này nối cơ học thống kê với hệ số vận chuyển, nhiễu điện, độ nhớt, khuếch tán, đáp ứng điện môi, quang phổ học và vật lý nhiều hạt.

## Đáp ứng tuyến tính như xấp xỉ bậc nhất

Giả sử một lực suy rộng ngoài `f(t)` ghép với đại lượng `A`. Với tác động đủ nhỏ, thay đổi của giá trị kỳ vọng đại lượng `B` có thể viết

```math
\delta\langle B(t)\rangle
=
\int_{-\infty}^{t}
\chi_{BA}(t-t')f(t')\,dt'.
```

`\chi_{BA}` là hàm đáp ứng hoặc susceptibility.

Giới hạn trên bằng `t` mã hóa nhân quả: tác động ở tương lai không thể ảnh hưởng đáp ứng hiện tại.

Trong miền tần số,

```math
\delta B(\omega)=\chi(\omega)f(\omega).
```

Phép tích chập theo thời gian trở thành phép nhân theo tần số. Đây là lý do Fourier là ngôn ngữ tự nhiên của hệ tuyến tính.

## Phần thực và phần ảo của susceptibility

Ta thường viết

```math
\chi(\omega)=\chi'(\omega)+i\chi''(\omega).
```

Trong nhiều hệ:

- `\chi'` mô tả phần đáp ứng gần đồng pha và tích trữ năng lượng;
- `\chi''` mô tả phần lệch pha gắn với tiêu tán.

Ví dụ, trong điện môi, phần ảo của hằng số điện môi liên hệ với hấp thụ. Trong dao động cơ học, phần ảo của compliance liên hệ với mất mát năng lượng.

Tiêu tán không phải một chi tiết phụ: nó quyết định entropy production, độ rộng cộng hưởng và thời gian sống của mode.

## Nhân quả và quan hệ Kramers–Kronig

Nếu hệ là nhân quả,

```math
\chi(t<0)=0.
```

Điều này buộc phần thực và phần ảo của đáp ứng tần số không độc lập.

Một trong các quan hệ Kramers–Kronig là

```math
\chi'(\omega)
=
\frac{1}{\pi}\,\mathcal P
\int_{-\infty}^{\infty}
\frac{\chi''(\omega')}{\omega'-\omega}\,d\omega'.
```

Có quan hệ ngược lại cho `\chi''`.

Về vật lý, tán sắc và hấp thụ là hai mặt của cùng một đáp ứng nhân quả. Trong quang học, sự thay đổi chiết suất gần một vạch hấp thụ là ví dụ trực tiếp.

## Trực giác của định lý thăng giáng–tiêu tán

Nếu một bậc tự do bị môi trường làm giảm chuyển động mạnh, cùng môi trường đó cũng phải gây các cú đá ngẫu nhiên ở nhiệt độ hữu hạn.

Với mô hình Langevin

```math
m\dot v=-\gamma v+\xi(t),
```

ma sát `\gamma` và nhiễu `\xi(t)` không thể được chọn độc lập nếu hệ phải tiến tới cân bằng nhiệt.

Trong mô hình nhiễu trắng cổ điển,

```math
\langle\xi(t)\xi(t')\rangle
=2\gamma k_BT\,\delta(t-t').
```

Nhiễu mạnh hơn khi nhiệt độ cao hơn hoặc coupling gây tiêu tán mạnh hơn.

## Quan hệ Einstein giữa khuếch tán và độ linh động

Một hạt có độ linh động `\mu` chịu lực nhỏ `F` sẽ có vận tốc trôi

```math
v_d=\mu F.
```

Cùng môi trường vi mô gây lực cản cũng gây khuếch tán với hệ số `D`. Gần cân bằng,

```math
D=\mu k_BT.
```

Nếu dùng hệ số ma sát `\gamma` với

```math
\mu=\frac{1}{\gamma},
```

thì

```math
D=\frac{k_BT}{\gamma}.
```

Khuếch tán ngẫu nhiên và lực cản tiêu tán vì vậy là hai biểu hiện của cùng coupling với môi trường nhiệt.

## Nhiễu Johnson–Nyquist

Một điện trở ở nhiệt độ `T` có dao động điện áp ngay cả khi không đặt điện áp ngoài.

Trong giới hạn cổ điển tần số thấp, mật độ phổ nhiễu điện áp là

```math
S_V(f)=4k_BTR.
```

Điện trở `R` đo mức tiêu tán của mạch; chính `R` và `T` cũng quyết định độ mạnh của nhiễu nhiệt.

Ở tần số cao hoặc nhiệt độ rất thấp, cần hiệu chỉnh lượng tử và không thể tiếp tục dùng biểu thức cổ điển một cách máy móc.

## Quan hệ Green–Kubo

Các hệ số vận chuyển có thể được biểu diễn qua hàm tương quan theo thời gian ở cân bằng.

Ví dụ hệ số khuếch tán trong `d` chiều:

```math
D=\frac{1}{d}\int_0^\infty
\langle\mathbf v(0)\cdot\mathbf v(t)\rangle\,dt.
```

Độ nhớt và hệ số dẫn nhiệt cũng có công thức Green–Kubo tương ứng dùng tự tương quan của tensor ứng suất hoặc dòng nhiệt.

Đây là một kết quả sâu: hệ số mô tả đáp ứng không thuận nghịch ở quy mô vĩ mô có thể được tính từ cách các dao động cân bằng vi mô mất tương quan theo thời gian.

## Công thức Kubo trong cơ học lượng tử

Nếu nhiễu loạn Hamiltonian có dạng

```math
H'(t)=-f(t)A,
```

thì đáp ứng lượng tử có dạng

```math
\chi_{BA}(t)
=
\frac{i}{\hbar}\theta(t)
\langle[B(t),A(0)]\rangle_{eq}.
```

Hàm bước `\theta(t)` bảo đảm nhân quả. Commutator xuất hiện vì các đại lượng quan sát lượng tử không nhất thiết giao hoán.

Độ dẫn điện, susceptibility từ và đáp ứng quang học của hệ nhiều hạt thường được suy ra bằng formalism Kubo.

## Dynamic structure factor và quang phổ học

Dao động mật độ trong vật chất có thể được mô tả bằng dynamic structure factor `S(q,\omega)`.

Tán xạ neutron, tia X và ánh sáng đo các đại lượng liên quan đến `S`. Vị trí peak cho biết mode tập thể, còn độ rộng peak liên hệ với damping và thời gian sống.

FDT nối phổ thăng giáng với phần tiêu tán của susceptibility. Vì vậy đo nhiễu tự phát và đo đáp ứng cưỡng bức có thể cung cấp thông tin về cùng động lực vi mô.

## Quan hệ thuận nghịch Onsager

Gần cân bằng, các dòng suy rộng `J_i` có thể liên hệ tuyến tính với các lực nhiệt động `X_j`:

```math
J_i=\sum_jL_{ij}X_j.
```

Tính thuận nghịch vi mô dẫn tới các quan hệ Onsager trong điều kiện đối xứng phù hợp:

```math
L_{ij}=L_{ji}.
```

Khi có từ trường hoặc biến đổi có tính lẻ dưới đảo thời gian, quan hệ cần thêm dấu hoặc phép đảo trường thích hợp.

Hiệu ứng Seebeck–Peltier trong nhiệt điện là ví dụ quan trọng về vận chuyển ghép chéo.

## Entropy production trong nhiệt động lực học không thuận nghịch tuyến tính

Tốc độ sinh entropy thường có dạng

```math
\dot S_{prod}=\sum_iJ_iX_i\ge0.
```

Điều kiện ma trận vận chuyển dương bán xác định bảo đảm định luật II ở mức đáp ứng tuyến tính.

Đây là cầu nối giữa nhiệt động lực học không cân bằng dạng hiện tượng luận và lý thuyết tương quan vi mô.

## Critical slowing down

Gần chuyển pha liên tục, độ dài tương quan tăng và thời gian thư giãn cũng có thể tăng mạnh.

Hệ không chỉ dao động mạnh hơn mà còn mất nhiều thời gian hơn để quên một fluctuation. Do đó susceptibility cân bằng, biên độ thăng giáng và động lực không cân bằng liên hệ với nhau qua scaling tới hạn.

## Khi đáp ứng tuyến tính thất bại

Nếu tác động ngoài không còn nhỏ, đáp ứng chứa các hạng phi tuyến:

```math
B=\chi^{(1)}f+\chi^{(2)}f^2+\chi^{(3)}f^3+\cdots.
```

Hệ xa cân bằng, có hysteresis mạnh, active driving hoặc bộ nhớ dài có thể không tuân FDT cân bằng chuẩn.

Khi đó cần các khung tổng quát hơn như đáp ứng phi tuyến, stochastic thermodynamics hoặc phương trình động học đầy đủ.

## Ví dụ: bậc tự do overdamped chịu lực bậc thang

Xét

```math
\gamma\dot x+kx=f(t)+\xi(t).
```

Bỏ nhiễu và đặt lực bậc thang `f(t)=f_0` từ `t=0`, nghiệm là

```math
x(t)=\frac{f_0}{k}
\left(1-e^{-t/\tau}\right),
\qquad
\tau=\frac{\gamma}{k}.
```

Cùng hệ số `\gamma` quyết định thời gian thư giãn và, qua FDT, độ mạnh nhiễu `2\gamma k_BT`.

Vì vậy đo thăng giáng tự phát có thể giúp suy ra tham số đáp ứng mà không cần kích thích hệ mạnh.

## Đơn vị và kiểm tra thứ nguyên

Susceptibility có đơn vị phụ thuộc cặp đại lượng đầu vào–đầu ra. Ví dụ độ linh động `\mu` có đơn vị vận tốc chia lực.

Trong quan hệ Einstein

```math
D=\mu k_BT,
```

`k_BT` có đơn vị năng lượng, nên tích với `\mu` phải cho đơn vị `m^2/s` của hệ số khuếch tán.

Các kiểm tra thứ nguyên như vậy đặc biệt hữu ích vì linear response thường chứa nhiều hệ số hiện tượng luận.

## Mô hình tư duy (Mental Model)

Cân bằng không phải trạng thái “im lặng”. Các bậc tự do vi mô luôn thăng giáng.

Nếu một hệ dễ bị môi trường kích thích ngẫu nhiên qua một kênh, chính coupling đó cũng làm năng lượng đưa vào qua kênh ấy bị tiêu tán.

Có thể tóm tắt:

```text
microscopic coupling
→ equilibrium fluctuations
→ correlation functions
→ susceptibility
→ dissipation / transport
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiễu chỉ là lỗi thiết bị”

Không. Nhiễu nhiệt và lượng tử là tín hiệu vật lý nội tại và có thể chứa thông tin về vật liệu hoặc hệ.

### “FDT đúng cho mọi hệ không cân bằng”

Không. Dạng chuẩn là kết quả của cân bằng hoặc gần cân bằng với các giả định rõ. Hệ active hoặc xa cân bằng có thể vi phạm dạng đơn giản này.

### “Tiêu tán nghĩa định luật vi mô phải không thuận nghịch”

Không nhất thiết. Tính không thuận nghịch vĩ mô có thể nổi lên từ coarse-graining, nhiều bậc tự do và sự mất tương quan dù động lực vi mô gần đối xứng theo đảo thời gian.

### “Phần ảo của susceptibility chỉ là thủ thuật số phức”

Không. Nó thường mang thông tin trực tiếp về hấp thụ và mất mát năng lượng.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Ensemble thống kê](03_ensembles_partition_functions.md), [Động lực ngẫu nhiên](04_stochastic_nonequilibrium.md), [Tín hiệu và mật độ phổ](../12_experimental_computational/01_signals_sampling_noise.md).

**Liên hệ tiếp:** [Hiện tượng vận chuyển](../03_continuum/02_transport_diffusion_heat.md), [Vận chuyển trong vật chất ngưng tụ](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md), [Quang học phi tuyến và tán sắc](../06_optics/03_polarization_dispersion_nonlinear_optics.md).
