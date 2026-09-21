# Bất ổn hấp dẫn và hình thành cấu trúc: từ dao động mật độ tới sao và cosmic web

## Hấp dẫn có một đặc tính đặc biệt: overdensity có thể tự khuếch đại

Trong chất khí thông thường, áp suất có xu hướng san bằng chênh lệch mật độ. Hấp dẫn lại tạo phản hồi dương: vùng hơi đậm đặc hơn có lực hút mạnh hơn, kéo thêm vật chất vào và trở nên đậm đặc hơn nữa.

Cạnh tranh giữa **áp suất hoặc cơ chế nâng đỡ** và **tự hấp dẫn (self-gravity)** quyết định một đám mây sẽ ổn định, dao động hay sụp đổ.

Bất ổn hấp dẫn (gravitational instability / 중력 불안정성) vì vậy là cầu nối tự nhiên giữa cơ học chất lưu, nhiệt động lực học và vật lý thiên văn.

## Phân tích Jeans: nhiễu loạn một môi trường gần đồng nhất

Xét khí lý tưởng có mật độ nền `\rho_0`, áp suất `P_0` và vận tốc nền bằng 0. Đặt nhiễu loạn nhỏ:

```math
\rho=\rho_0+\delta\rho,
\qquad
P=P_0+\delta P,
\qquad
\mathbf v=\delta\mathbf v.
```

Phương trình liên tục tuyến tính hóa là

```math
\frac{\partial\delta\rho}{\partial t}
+\rho_0\nabla\cdot\delta\mathbf v=0.
```

Phương trình Euler tuyến tính hóa:

```math
\frac{\partial\delta\mathbf v}{\partial t}
=-\frac{1}{\rho_0}\nabla\delta P
-\nabla\delta\Phi.
```

Thế hấp dẫn thỏa phương trình Poisson

```math
\nabla^2\delta\Phi
=4\pi G\delta\rho.
```

Với vận tốc âm đoạn nhiệt

```math
c_s^2
=\left(\frac{\partial P}{\partial\rho}\right)_s,
```

ta có

```math
\delta P=c_s^2\delta\rho.
```

## Quan hệ tán sắc Jeans

Thử nghiệm nhiễu loạn sóng phẳng

```math
\delta\rho
\propto e^{i(\mathbf k\cdot\mathbf x-\omega t)}.
```

Kết hợp ba phương trình cho

```math
\omega^2
=c_s^2k^2-4\pi G\rho_0.
```

Biểu thức này cho thấy hai cơ chế cạnh tranh trực tiếp.

Nếu

```math
c_s^2k^2>4\pi G\rho_0,
```

thì `\omega^2>0`: áp suất thắng và nhiễu loạn dao động gần như sóng âm đã bị hấp dẫn hiệu chỉnh.

Nếu

```math
c_s^2k^2<4\pi G\rho_0,
```

thì `\omega^2<0`: `\omega` trở thành số ảo và một nghiệm tăng theo hàm mũ xuất hiện. Đây là dấu hiệu bắt đầu sụp đổ hấp dẫn.

## Chiều dài Jeans

Số sóng tới hạn là

```math
k_J
=\frac{\sqrt{4\pi G\rho_0}}{c_s}.
```

Chiều dài Jeans có bậc

```math
\lambda_J
\sim c_s\sqrt{\frac{\pi}{G\rho_0}}.
```

Dưới các giả định lý tưởng:

- cấu trúc lớn hơn `\lambda_J` có xu hướng bất ổn hấp dẫn;
- cấu trúc nhỏ hơn có thể được áp suất nâng đỡ.

Khí nóng có `c_s` lớn nên chiều dài Jeans lớn hơn. Khí đậm đặc hơn có thời gian hấp dẫn ngắn hơn và chiều dài Jeans nhỏ hơn.

## Khối lượng Jeans

Khối lượng chứa trong vùng cỡ chiều dài Jeans cho thang khối lượng

```math
M_J
\sim\rho_0\lambda_J^3
\propto
\frac{c_s^3}{G^{3/2}\rho_0^{1/2}}.
```

Với khí lý tưởng có thành phần hóa học cố định,

```math
c_s\propto\sqrt T,
```

nên gần đúng

```math
M_J\propto T^{3/2}\rho^{-1/2}.
```

Làm lạnh khí giảm áp suất nhiệt và giảm `M_J`, cho phép đám mây phân mảnh thành các vùng nhỏ hơn có thể tiếp tục sụp đổ.

Do đó hóa học làm lạnh, bụi, phân tử và bức xạ đều có ảnh hưởng trực tiếp tới hình thành sao.

## Thời gian rơi tự do

Tự hấp dẫn tạo một thang thời gian tự nhiên

```math
t_{ff}\sim\frac{1}{\sqrt{G\rho}}.
```

Với quả cầu đồng nhất, hệ số chính xác chỉ khác một hằng số bậc 1.

Vùng mật độ cao có thời gian rơi tự do ngắn hơn. Để hiểu tiến hóa đám mây, cần so sánh `t_ff` với:

- thời gian làm lạnh;
- thời gian truyền âm;
- thời gian khuếch tán từ;
- thời gian quay;
- thời gian feedback từ sao.

## Định lý virial và vì sao co lại có thể làm khí nóng hơn

Với hệ tự hấp dẫn gần cân bằng,

```math
2K+U\approx0,
```

trong đó thế năng hấp dẫn `U<0`.

Nếu hệ bức xạ năng lượng ra ngoài, tổng năng lượng trở nên âm hơn. Hệ co lại và một phần thế năng hấp dẫn được chuyển thành động năng hoặc nhiệt.

Đây là trực giác của **nhiệt dung âm** trong một số hệ tự hấp dẫn: mất năng lượng có thể làm nhiệt độ bên trong tăng.

Do đó sụp đổ không đồng nghĩa với khí phải lạnh đi. Làm lạnh bức xạ cho phép hệ tiếp tục co, nhưng quá trình co có thể đồng thời sinh nhiệt.

## Mômen động lượng và sự hình thành đĩa

Đám mây phân tử hiếm khi có mômen động lượng bằng đúng 0.

Nếu bán kính giảm mà mômen động lượng gần bảo toàn, tốc độ quay tăng. Cuối cùng hỗ trợ ly tâm trở nên quan trọng và vật chất dễ hình thành đĩa.

Để vật chất tiếp tục accrete về tâm, mômen động lượng phải được vận chuyển ra ngoài qua các cơ chế như:

- torque hấp dẫn;
- nhiễu loạn;
- magnetic braking;
- instability của đĩa;
- cơ chế giống độ nhớt hiệu dụng.

Đây là lý do hình thành sao và accretion disk không thể được hiểu chỉ bằng “gravity kéo mọi thứ vào tâm”.

## Từ trường trong đám mây phân tử

Ngay cả một phần ion hóa nhỏ cũng có thể ghép khí với từ trường.

Áp suất từ và lực căng từ có thể nâng đỡ hoặc tái phân bố vật chất theo hướng nhất định.

Trong khí ion hóa một phần, ambipolar diffusion cho phép hạt trung hòa trôi tương đối so với ion và đường sức từ.

Vì vậy tiêu chuẩn Jeans chỉ là baseline. Lý thuyết hình thành sao thực cần thêm từ trường, turbulence, hóa học và radiation feedback.

## Dòng rối vừa chống sụp đổ vừa tạo vùng sụp đổ

Turbulence siêu âm có thể tăng velocity dispersion ở thang lớn, cung cấp hỗ trợ động học tạm thời.

Nhưng shock do turbulence cũng nén khí thành filament và core đậm đặc. Mật độ tăng làm `M_J` giảm và `t_ff` ngắn hơn.

Do đó hai câu:

- “turbulence hỗ trợ chống gravity”;
- “turbulence kích hoạt hình thành sao”

không mâu thuẫn. Tác dụng phụ thuộc thang đo và cấu trúc dòng cục bộ.

## Từ nhiễu loạn nguyên thủy tới cấu trúc vũ trụ

Trong Vũ trụ giãn nở, độ tương phản mật độ được định nghĩa

```math
\delta(\mathbf x,t)
=\frac{\rho-\bar\rho}{\bar\rho}.
```

Ban đầu `|\delta|` rất nhỏ.

Trong chế độ vật chất chi phối đơn giản, nhiễu loạn tuyến tính thỏa phương trình gần dạng

```math
\ddot\delta
+2H\dot\delta
-4\pi G\bar\rho_m\delta=0.
```

Hạng

```math
2H\dot\delta
```

là hiệu ứng “Hubble drag”: sự giãn nở làm tốc độ tăng trưởng nhiễu loạn chậm hơn so với môi trường tĩnh.

Trong Vũ trụ Einstein–de Sitter lý tưởng, mode tăng gần

```math
\delta\propto a(t).
```

## Vật chất tối và hình thành cấu trúc phân cấp

Cold dark matter có áp suất hiệu dụng rất nhỏ trên các thang liên quan nên có thể kết tụ hấp dẫn sớm.

Halo vật chất tối tạo giếng thế; khí baryon rơi vào, shock, làm lạnh và hình thành thiên hà cùng sao.

Trong mô hình phân cấp, các halo nhỏ hình thành trước rồi hợp nhất thành hệ lớn hơn.

Cosmic web gồm sheet, filament, node và void xuất hiện từ sự sụp đổ hấp dẫn không đẳng hướng của trường nhiễu loạn ban đầu.

## Phổ công suất

Trường nhiễu loạn thường được mô tả thống kê bằng phổ công suất `P(k)`:

```math
\langle
\delta_{\mathbf k}
\delta^*_{\mathbf k'}
\rangle
\propto
P(k)\delta_D(\mathbf k-\mathbf k').
```

`P(k)` cho biết variance của nhiễu loạn theo thang không gian.

Phổ nguyên thủy được biến đổi bởi vật lý bức xạ–vật chất trong Vũ trụ sớm; sau đó hấp dẫn phi tuyến làm thay đổi phổ ở thời kỳ muộn.

Quan sát clustering thiên hà, weak lensing và CMB dùng `P(k)` hoặc các đại lượng liên hệ để ràng buộc mô hình.

## Baryon Acoustic Oscillations

Trước recombination, baryon và photon tạo plasma ghép có sóng âm.

Sau decoupling, sóng acoustic ngừng được duy trì và để lại một thang comoving đặc trưng trong phân bố vật chất.

Baryon Acoustic Oscillation (BAO) đóng vai trò **standard ruler** trong cosmology.

Đây là cầu nối đẹp giữa:

```text
sóng âm plasma sơ khai
→ CMB
→ phân bố vật chất
→ clustering thiên hà thời kỳ muộn
```

## Khi lý thuyết tuyến tính thất bại

Khi

```math
|\delta|\ll1,
```

lý thuyết nhiễu loạn tuyến tính hoạt động tốt.

Khi `\delta` tiến tới bậc 1, các mode bắt đầu ghép mạnh. Ta cần các phương pháp phi tuyến như:

- spherical collapse;
- perturbation theory bậc cao;
- N-body simulation;
- hydrodynamic cosmological simulation.

Một halo virial hóa không tiếp tục co vô hạn vì chuyển động ngẫu nhiên của hạt, mômen động lượng và cấu trúc động lực tạo hỗ trợ hiệu dụng.

## Mô phỏng N-body

Vật chất tối thường được mô hình hóa bằng nhiều “simulation particles” lấy mẫu phân bố pha liên tục.

Tính lực hấp dẫn trực tiếp giữa mọi cặp có chi phí gần

```math
O(N^2).
```

Các kỹ thuật như tree code, particle-mesh và hybrid method giảm chi phí đáng kể.

Mô phỏng phải cân bằng:

- độ phân giải không gian;
- độ phân giải khối lượng;
- bước thời gian;
- gravitational softening;
- kích thước hộp.

Một cosmic web nhìn đẹp không tự động chứng minh mô phỏng đã hội tụ hoặc mô hình vật lý đúng.

## Ví dụ định lượng: vì sao khí lạnh và đậm đặc dễ sụp đổ hơn?

Với

```math
M_J\propto T^{3/2}\rho^{-1/2},
```

nếu nhiệt độ giảm 4 lần,

```math
M_J\to\frac{M_J}{4^{3/2}}
=\frac{M_J}{8}.
```

Nếu đồng thời mật độ tăng 100 lần,

```math
M_J\to\frac{M_J}{10}.
```

Tổng hợp hai hiệu ứng, khối lượng Jeans giảm khoảng 80 lần.

Làm lạnh và nén vì vậy có thể tạo runaway fragmentation rất hiệu quả.

## “Jeans swindle” và giới hạn của derivation đơn giản

Một môi trường tự hấp dẫn đồng nhất vô hạn có thế hấp dẫn nền không xác định tốt. Phân tích Jeans giáo khoa thực chất bỏ qua trường nền rồi chỉ xét nhiễu loạn.

Trong cosmology, perturbation theory trên nền FLRW xử lý vấn đề nhất quán hơn.

Đám mây thật còn có:

- hình học hữu hạn;
- rotation;
- từ trường;
- turbulence;
- cooling chemistry;
- feedback bức xạ và stellar wind.

Vì vậy Jeans criterion là **diagnostic về thang**, không phải quy tắc yes/no tuyệt đối cho mọi đám mây.

## Mô hình tư duy (Mental Model)

Gravity tạo feedback dương cho overdensity. Áp suất, velocity dispersion, mômen động lượng, từ trường và cosmic expansion tạo các cơ chế chống hoặc làm chậm collapse.

Structure formation có thể được nhìn như cạnh tranh giữa các thang thời gian:

```text
self-gravity
vs
sound / cooling / rotation / magnetic support / Hubble expansion
```

Jeans length là biểu thức đơn giản nhất của cuộc cạnh tranh này.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Mọi overdensity đều sụp đổ ngay”

Không. Áp suất, quay, từ trường, turbulence và expansion có thể ổn định hoặc trì hoãn collapse.

### “Vật chất tối chỉ được thêm để khớp đường cong quay thiên hà”

Không. Giả thuyết dark matter được kiểm tra bởi lensing, CMB, cluster dynamics, large-scale structure và tốc độ tăng trưởng cấu trúc.

### “Hình thành cấu trúc là một vụ nổ tạo thiên hà”

Không. Nó là sự tăng trưởng hấp dẫn của nhiễu loạn ban đầu trong nền Vũ trụ giãn nở qua hàng tỷ năm.

### “Jeans mass là một ngưỡng chính xác không phụ thuộc môi trường”

Không. Nó đến từ mô hình lý tưởng và chỉ là thang tham khảo khi nhiều cơ chế khác cùng tồn tại.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cơ học chất lưu](../03_continuum/00_fluids.md), [Hấp dẫn](../01_mechanics/06_gravitation_orbits.md), [Ensemble và thăng giáng](../04_thermal_statistical/03_ensembles_partition_functions.md), [Vũ trụ học](01_galaxies_cosmology.md).

**Liên hệ tiếp:** [Sao và thiên thể đặc](00_stars_compact_objects.md), [Vũ trụ sơ khai](03_early_universe_dark_components.md), [Vật lý tính toán](../12_experimental_computational/02_computational_physics.md), [Suy luận dữ liệu](../12_experimental_computational/03_data_inference_inverse_problems.md).
