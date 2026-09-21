# Động lực học ngẫu nhiên và vật lý thống kê không cân bằng

## Cân bằng không phải toàn bộ vật lý thống kê

Cơ học thống kê cân bằng rất mạnh vì chỉ cần một số ràng buộc vĩ mô đã có thể xác định phân bố xác suất của hệ. Tuy nhiên, rất nhiều hệ thực luôn có dòng vận chuyển: nhiệt truyền qua vật, hạt khuếch tán theo gradient nồng độ, protein động cơ tiêu thụ năng lượng hóa học, khí quyển nhận năng lượng từ Mặt Trời rồi bức xạ ra không gian.

Vật lý thống kê không cân bằng (nonequilibrium statistical physics / 비평형 통계물리학) nghiên cứu các hệ có dòng, tác động ngoài hoặc quá trình thư giãn về trạng thái ổn định.

Một công cụ trung tâm là quá trình ngẫu nhiên (stochastic process): thay vì giả vờ rằng ta biết mọi va chạm vi mô, ta mô hình hóa phần chưa được phân giải bằng xác suất và nhiễu.

## Chuyển động Brown: ngẫu nhiên nhưng có quy luật

Một hạt nhỏ trong chất lưu chịu vô số va chạm phân tử. Trong mỗi khoảng thời gian ngắn, các va chạm không cân bằng chính xác nên vị trí của hạt dao động ngẫu nhiên dù chất lưu tổng thể đang ở cân bằng nhiệt.

Trong một chiều, quan hệ Einstein cho chuyển động khuếch tán là

```math
\langle[x(t)-x(0)]^2\rangle=2Dt.
```

Khác chuyển động đạn đạo, nơi quãng đường đặc trưng tỉ lệ với `t`, khuếch tán có thang chiều dài

```math
\ell\sim\sqrt{Dt}.
```

Do đó muốn khuếch tán xa gấp 10 lần thường phải chờ lâu hơn khoảng 100 lần.

## Phương trình Langevin: lực xác định + ma sát + nhiễu

Một mô hình điển hình cho hạt Brown là

```math
m\dot v=-\gamma v+F(x)+\xi(t).
```

Trong đó:

- `-\gamma v` là lực cản đã được coarse-grain từ nhiều va chạm vi mô;
- `F(x)` là lực hệ thống đã biết;
- `\xi(t)` là lực ngẫu nhiên do môi trường vi mô.

Trong mô hình nhiễu trắng lý tưởng,

```math
\langle\xi(t)\rangle=0,
```

và

```math
\langle\xi(t)\xi(t')\rangle
=2\gamma k_BT\,\delta(t-t').
```

Độ mạnh của nhiễu và ma sát không thể chọn độc lập tùy ý nếu hệ phải tiến tới cân bằng nhiệt ở nhiệt độ `T`.

Nếu chỉ có ma sát mà không có nhiễu, hạt sẽ mất động năng dần về 0, mâu thuẫn với cân bằng nhiệt ở `T>0`.

## Phương trình Fokker–Planck: từ quỹ đạo ngẫu nhiên đến mật độ xác suất

Thay vì mô phỏng từng quỹ đạo, ta có thể theo dõi mật độ xác suất `P(x,t)`.

Khuếch tán thuần thỏa

```math
\frac{\partial P}{\partial t}=D\nabla^2P.
```

Nếu có trường trôi `a(x)`, một dạng phương trình Fokker–Planck là

```math
\frac{\partial P}{\partial t}
=-\nabla\cdot(aP)+D\nabla^2P.
```

Hạng đầu vận chuyển xác suất có hướng; hạng sau làm phân bố lan rộng do nhiễu.

Đây là cầu nối giữa phương trình vi phân ngẫu nhiên và PDE. Cấu trúc toán học tương tự xuất hiện trong tài chính định lượng, động lực quần thể, neuroscience và diffusion model trong machine learning, dù ý nghĩa vật lý của biến khác nhau.

## Quá trình Markov và khái niệm bộ nhớ

Một quá trình Markov (Markov process / 마르코프 과정) có phân bố tương lai phụ thuộc trạng thái hiện tại, không cần toàn bộ lịch sử nếu trạng thái đã được định nghĩa đủ đầy.

Điều này không có nghĩa hệ vật lý “không có ký ức”. Nó có nghĩa sau coarse-graining, tập biến trạng thái ta chọn đủ để động lực học gần đúng trở thành không nhớ.

Nếu môi trường có tương quan dài theo thời gian, xấp xỉ Markov có thể thất bại. Khi đó cần phương trình Langevin tổng quát hoặc kernel nhớ (memory kernel).

## Detailed balance và dòng xác suất

Ở cân bằng, nếu hệ có tính thuận nghịch vi mô thích hợp, tốc độ chuyển trạng thái có thể thỏa detailed balance:

```math
p_i^{eq}W_{i\to j}=p_j^{eq}W_{j\to i}.
```

Dòng xác suất ròng giữa hai trạng thái khi đó bằng 0.

Một trạng thái dừng không cân bằng có thể có phân bố xác suất không đổi theo thời gian nhưng vẫn tồn tại dòng xác suất tuần hoàn.

Vì vậy:

> trạng thái dừng (steady state) không đồng nghĩa với cân bằng (equilibrium).

Một điện trở có dòng điện không đổi là ví dụ: các đại lượng vĩ mô ổn định, nhưng năng lượng vẫn liên tục tiêu tán thành nhiệt.

## Entropy production trong hệ không cân bằng

Trong nhiệt động lực học không thuận nghịch, các dòng thường được điều khiển bởi các lực nhiệt động.

Ví dụ định luật Fourier:

```math
\mathbf q=-k\nabla T,
```

và định luật Fick:

```math
\mathbf J=-D\nabla c.
```

Gần cân bằng, tốc độ sinh entropy thường có thể viết như tổng tích giữa dòng và lực liên hợp, với điều kiện

```math
\dot S_{prod}\ge0.
```

Không cân bằng không phá định luật II. Ngược lại, entropy production trở thành một đại lượng động lực học quan trọng để định lượng tính không thuận nghịch.

## Fluctuation theorem và các dao động hiếm

Trong hệ vi mô hoặc khoảng thời gian rất ngắn, ta có thể quan sát những quỹ đạo mà entropy production tức thời có giá trị âm.

Điều này không phủ định định luật II ở quy mô vĩ mô. Các định lý thăng giáng (fluctuation theorem) định lượng xác suất tương đối giữa quỹ đạo “thuận” và “ngược”. Khi kích thước hệ hoặc thời gian quan sát tăng, các dao động ngược hiếm trở nên cực kỳ ít khả năng.

## Ví dụ: mạch RC và quá trình Ornstein–Uhlenbeck

Nhiễu điện áp trên hệ điện trở–tụ có thể được mô hình hóa như một biến ngẫu nhiên bị kéo về cân bằng bởi quá trình thư giãn, đồng thời liên tục bị kích thích bởi nhiễu Johnson–Nyquist.

Cấu trúc toán học giống quá trình Ornstein–Uhlenbeck:

```math
dX=-\lambda X\,dt+\sigma\,dW_t.
```

Nó xuất hiện trong vận tốc của hạt Brown, nhiễu điện tử, điều khiển ngẫu nhiên và nhiều mô hình mean-reverting.

## Active matter: hệ tự tiêu thụ năng lượng

Vi khuẩn, colloid tự đẩy và protein động cơ không chỉ chịu nhiễu nhiệt. Chúng tiêu thụ năng lượng để tạo chuyển động có tính bền theo thời gian.

Active matter (active matter / 활성 물질) vì vậy không tuân đơn giản quan hệ thăng giáng–tiêu tán của cân bằng.

Một hệ active có thể có chuyển động rất mạnh nhưng không thể được mô tả chính xác chỉ bằng cách gán cho nó một “nhiệt độ hiệu dụng” duy nhất.

## Quan hệ thăng giáng–tiêu tán

Trong cân bằng, cùng tương tác vi mô với môi trường vừa gây damping vừa gây các cú đá ngẫu nhiên.

Với

```math
m\dot v=-\gamma v+\xi(t),
```

độ mạnh của nhiễu phải liên hệ với `\gamma` và `T` để phân bố dài hạn trở về Maxwell–Boltzmann:

```math
\langle\xi(t)\xi(t')\rangle
=2\gamma k_BT\,\delta(t-t').
```

Đây là một dạng của quan hệ thăng giáng–tiêu tán (fluctuation–dissipation relation / 요동-소산 관계).

## Mean-square displacement và các chế độ vận chuyển

Với hạt Brown ở thời gian đủ dài,

```math
\langle|x(t)-x(0)|^2\rangle=2Dt
```

trong 1D.

Ở thời gian rất ngắn trước khi nhiều va chạm xảy ra, chuyển động có thể gần đạn đạo:

```math
\langle\Delta x^2\rangle\propto t^2.
```

Vì vậy đồ thị log–log của mean-square displacement có thể giúp nhận biết chế độ vận chuyển.

Nếu

```math
\langle\Delta x^2\rangle\propto t^\alpha
```

với `\alpha\neq1`, ta có khuếch tán bất thường, thường liên hệ với bẫy, bộ nhớ, môi trường phức tạp hoặc động lực active.

## Bài toán first-passage

Nhiều câu hỏi không hỏi vị trí tại một thời điểm cố định mà hỏi:

> mất bao lâu để hệ chạm một biên lần đầu?

Ví dụ:

- phân tử tìm tới receptor;
- ion thoát khỏi pore;
- tọa độ phản ứng vượt rào năng lượng;
- tín hiệu vượt một ngưỡng.

Thời gian first-passage phụ thuộc cả động lực ngẫu nhiên lẫn điều kiện biên. Đây là ví dụ rõ cho thấy boundary condition tạo ra đại lượng quan sát mới.

## Miền áp dụng và giới hạn

Mô hình nhiễu trắng giả sử tương quan thời gian của môi trường ngắn hơn nhiều thang thời gian của biến ta quan sát. Nếu môi trường có bộ nhớ dài, mô hình này không còn phù hợp.

Fokker–Planck chuẩn cũng giả sử quá trình có tính Markov và hệ số drift/diffusion được xác định thích hợp. Với bước nhảy lớn, phân bố đuôi nặng hoặc dynamics có bộ nhớ, cần các mô hình tổng quát hơn.

## Mô hình tư duy (Mental Model)

Cơ học thống kê cân bằng hỏi phân bố nào xuất hiện khi các dòng vĩ mô đã chết đi. Vật lý không cân bằng hỏi xác suất, dòng và entropy production thay đổi thế nào khi hệ đang bị tác động, đang thư giãn hoặc liên tục trao đổi tài nguyên với môi trường.

Một chuỗi tư duy hữu ích là

```text
microscopic interactions
→ coarse-graining
→ friction + noise
→ stochastic trajectory
→ probability distribution
→ current / entropy production / first-passage observables
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Ngẫu nhiên nghĩa là không có phương trình”

Sai. Động lực học ngẫu nhiên có phương trình chính xác cho phân bố, tương quan và xác suất quỹ đạo. Ta thay dự đoán tất định từng đường đi bằng dự đoán xác suất có cấu trúc.

### “Trạng thái dừng là cân bằng”

Không. Hệ có thể có đại lượng vĩ mô không đổi nhưng vẫn duy trì dòng nhiệt, vật chất hoặc điện và liên tục sinh entropy.

### “Nhiễu chỉ là lỗi phép đo”

Không. Chuyển động Brown và nhiễu nhiệt điện áp là động lực vật lý thật của hệ. Nhiễu phép đo chỉ là một nguồn khác.

### “Mọi hệ không cân bằng đều có thể mô tả bằng nhiệt độ hiệu dụng”

Không. Khái niệm này chỉ hữu ích trong một số chế độ và không thay thế mô tả đầy đủ của hệ active hoặc far-from-equilibrium.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Hiện tượng vận chuyển](../03_continuum/02_transport_diffusion_heat.md), [Ensemble thống kê](03_ensembles_partition_functions.md).

**Liên hệ tiếp:** [Thăng giáng–tiêu tán](07_linear_response_fluctuation_dissipation.md), [Vật chất mềm](../03_continuum/03_turbulence_rheology_soft_matter.md), [Tín hiệu và nhiễu](../12_experimental_computational/01_signals_sampling_noise.md).
