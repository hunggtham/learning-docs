# Thuyết tương đối hẹp: không-thời gian, biến đổi Lorentz và động lực học tương đối tính

Thuyết tương đối hẹp (special relativity / 특수상대성이론) không phải một bộ công thức bổ sung vào cơ học Newton. Nó thay đổi cấu trúc nền của không gian và thời gian để các định luật vật lý, đặc biệt điện từ học, có cùng dạng trong mọi hệ quy chiếu quán tính.

Mục tiêu của chương này là hiểu tại sao biến đổi Lorentz xuất hiện, vì sao sự đồng thời phụ thuộc hệ quy chiếu, cách các đại lượng bất biến tổ chức lý thuyết và tại sao cơ học Newton xuất hiện trở lại khi `v\ll c`.

## Vấn đề với phép biến đổi Galilei

Trong cơ học Newton, hai hệ quy chiếu quán tính có vận tốc tương đối `v` theo trục `x` liên hệ bởi

```math
x'=x-vt,
```

```math
t'=t.
```

Thời gian được coi là tuyệt đối. Nếu một vật có vận tốc `u`, hệ kia đo

```math
u'=u-v.
```

Nhưng phương trình Maxwell dự đoán sóng điện từ trong chân không có tốc độ

```math
c=\frac1{\sqrt{\mu_0\varepsilon_0}}.
```

Nếu áp dụng phép cộng vận tốc Galilei cho ánh sáng, các quan sát viên chuyển động khác nhau phải đo tốc độ ánh sáng khác nhau. Thực nghiệm không ủng hộ cấu trúc đó.

## Hai tiên đề

Thuyết tương đối hẹp được xây trên hai nguyên lý:

1. Các định luật vật lý có cùng dạng trong mọi hệ quy chiếu quán tính.
2. Tốc độ ánh sáng trong chân không có cùng giá trị `c` đối với mọi quan sát viên quán tính.

Hai tiên đề này buộc ta từ bỏ thời gian tuyệt đối chứ không phải “sửa” tốc độ ánh sáng.

## Đồng hồ ánh sáng và giãn thời gian

Một cách suy luận trực giác dùng đồng hồ ánh sáng gồm hai gương cách nhau `L`, photon đi lên xuống giữa chúng.

Trong hệ nghỉ của đồng hồ, một nửa chu kỳ thỏa

```math
\frac{\Delta\tau}{2}=\frac{L}{c}.
```

Với người quan sát thấy đồng hồ chuyển động ngang tốc độ `v`, photon đi theo đường chéo. Theo định lý Pythagoras,

```math
\left(c\frac{\Delta t}{2}\right)^2
=
L^2+
\left(v\frac{\Delta t}{2}\right)^2.
```

Thay

```math
L=c\frac{\Delta\tau}{2}
```

vào, ta được

```math
c^2\Delta t^2
=
c^2\Delta\tau^2+v^2\Delta t^2.
```

Suy ra

```math
\Delta t
=
\frac{\Delta\tau}{\sqrt{1-v^2/c^2}}
=
\gamma\Delta\tau,
```

với

```math
\gamma=\frac1{\sqrt{1-v^2/c^2}}.
```

Đây là giãn thời gian (time dilation).

`\Delta\tau` gọi là **thời gian riêng (proper time)**: thời gian đo bởi một đồng hồ đi cùng hai sự kiện.

## Vì sao giãn thời gian không phải lỗi đồng hồ?

Mọi quá trình vật lý trên hệ chuyển động đều tuân cùng cấu trúc không-thời gian: dao động nguyên tử, phân rã hạt, phản ứng hóa học hay quá trình sinh học.

Muon sinh ra trong khí quyển là ví dụ kinh điển. Trong hệ Trái Đất, tuổi thọ muon bị giãn nên nhiều muon sống đủ lâu để tới mặt đất. Trong hệ muon, thời gian riêng không đổi nhưng độ dày khí quyển bị co. Hai cách mô tả cho cùng dự đoán số lượng muon tới detector.

## Sự đồng thời là tương đối

Giả sử hai sự kiện xảy ra ở hai vị trí khác nhau và đồng thời trong hệ `S`. Nếu

```math
\Delta t=0,
```

biến đổi Lorentz cho

```math
\Delta t'
=
\gamma\left(
\Delta t-
\frac{v\Delta x}{c^2}
\right)
=
-\gamma\frac{v\Delta x}{c^2}.
```

Nếu `\Delta x\neq0`, nói chung `\Delta t'\neq0`.

Sự không đồng thời này không phải do tín hiệu tới mắt chậm khác nhau. Ngay cả sau khi hiệu chỉnh thời gian truyền ánh sáng, hai hệ quy chiếu vẫn gán thời gian tọa độ khác nhau cho các sự kiện xa nhau.

## Biến đổi Lorentz

Với `S'` chuyển động tốc độ `v` theo `x` so với `S`, biến đổi Lorentz là

```math
x'=\gamma(x-vt),
```

```math
t'=\gamma\left(t-\frac{vx}{c^2}\right),
```

```math
y'=y,
```

```math
z'=z.
```

Đây là phép biến đổi tuyến tính duy trì tốc độ ánh sáng và cấu trúc nhân quả.

Trong giới hạn

```math
\frac vc\ll1,
```

thì

```math
\gamma\approx1+
\frac12\frac{v^2}{c^2}
```

và hạng `vx/c^2` rất nhỏ, nên biến đổi Lorentz tiến về biến đổi Galilei.

## Khoảng không-thời gian bất biến

Giữa hai sự kiện,

```math
\Delta s^2
=
c^2\Delta t^2
-
\Delta x^2-
\Delta y^2-
\Delta z^2.
```

Mọi hệ quy chiếu quán tính đồng ý về `\Delta s^2` dù không đồng ý riêng về `\Delta t` và `\Delta\mathbf r`.

Đây là analog Lorentz của việc phép quay Euclid giữ

```math
x^2+y^2
```

không đổi.

Không-thời gian Minkowski có metric khác hình học Euclid, nhưng ý tưởng bất biến giúp tổ chức toàn bộ lý thuyết.

## Timelike, lightlike và spacelike

Nếu

```math
\Delta s^2>0,
```

hai sự kiện cách nhau kiểu thời gian (timelike). Có thể tồn tại vật chuyển động chậm hơn ánh sáng đi từ sự kiện này tới sự kiện kia.

Nếu

```math
\Delta s^2=0,
```

chúng cách nhau kiểu ánh sáng (lightlike).

Nếu

```math
\Delta s^2<0,
```

chúng cách nhau kiểu không gian (spacelike); không tín hiệu nhân quả nào truyền với tốc độ `\le c` có thể nối chúng.

Phân loại này là bất biến giữa các hệ quy chiếu.

## Nón ánh sáng và nhân quả

Tập các đường ánh sáng đi qua một sự kiện tạo nón ánh sáng (light cone). Phần bên trong nón tương lai chứa các sự kiện mà sự kiện hiện tại có thể ảnh hưởng nhân quả. Phần bên ngoài là spacelike và không thể nhận tín hiệu dưới hoặc bằng `c` từ sự kiện gốc.

Đây là lý do giới hạn tốc độ không chỉ là “giới hạn kỹ thuật của động cơ”; nó là cấu trúc nhân quả của không-thời gian.

## Thời gian riêng từ metric

Với một vật chuyển động,

```math
d\tau^2
=
dt^2-
\frac{1}{c^2}d\mathbf r^2.
```

Hay

```math
d\tau
=
dt\sqrt{1-\frac{v^2}{c^2}}.
```

Tích phân dọc worldline cho

```math
\tau
=
\int dt\sqrt{1-\frac{v^2(t)}{c^2}}.
```

Công thức này rất quan trọng vì nó xử lý cả vận tốc thay đổi theo thời gian. Nó cũng là cầu nối tự nhiên sang cơ học relativistic bằng nguyên lý tác dụng dừng.

## Co độ dài

Giả sử một thanh có chiều dài riêng `L_0` trong hệ nghỉ của nó. Người quan sát thấy thanh chuyển động phải đo hai đầu **cùng lúc trong hệ của mình**.

Biến đổi Lorentz dẫn tới

```math
L=\frac{L_0}{\gamma}.
```

Điểm cốt lõi nằm ở điều kiện “cùng lúc”. Co độ dài không độc lập với tính tương đối của sự đồng thời.

## Nghịch lý song sinh

Một người ở Trái Đất, người kia đi xa rồi quay lại. Khi gặp lại, người du hành có thể trẻ hơn.

Đây không phải nghịch lý logic. Hai worldline giữa cùng hai sự kiện đầu–cuối có thời gian riêng khác nhau:

```math
\tau=\int dt\sqrt{1-v^2/c^2}.
```

Người ở Trái Đất và người du hành không có lịch sử chuyển động đối xứng; người du hành đổi hệ quán tính khi quay đầu.

Cách nhìn bằng thời gian riêng tổng quát hơn việc chỉ nói “ai thấy đồng hồ kia chậm”.

## Cộng vận tốc tương đối tính

Nếu một vật có tốc độ `u` trong `S` và `S'` chuyển động tốc độ `v`, tốc độ dọc trục trong `S'` là

```math
u'
=
\frac{u-v}{1-uv/c^2}.
```

Nếu `u=c`, ta luôn thu được

```math
u'=c.
```

Khi `u,v\ll c`, mẫu số gần 1 và công thức trở về Galilei.

## Rapidity

Ta có thể đặt

```math
\tanh\eta=\frac vc.
```

`\eta` gọi là rapidity. Khi ghép hai boost cùng phương, rapidity cộng tuyến tính:

```math
\eta_{total}=\eta_1+\eta_2.
```

Điều này cho thấy biến đổi Lorentz có cấu trúc giống phép quay hyperbolic trong không-thời gian.

Rapidity đặc biệt hữu ích trong vật lý hạt vì nó tổ chức động học collider gọn hơn vận tốc thông thường.

## Bốn-vectơ vận tốc và động lượng

Bốn-vận tốc là

```math
U^\mu=\frac{dx^\mu}{d\tau}.
```

Bốn-động lượng là

```math
P^\mu=mU^\mu.
```

Trong một hệ quán tính,

```math
P^\mu=
\left(
\frac Ec,
\mathbf p
\right).
```

với

```math
\mathbf p=\gamma m\mathbf v
```

và

```math
E=\gamma mc^2.
```

Bình phương Minkowski của bốn-động lượng là bất biến:

```math
P^\mu P_\mu=m^2c^2.
```

Suy ra

```math
E^2=p^2c^2+m^2c^4.
```

## Khối lượng không cần “tăng theo vận tốc”

Trong cách trình bày hiện đại, khối lượng bất biến `m` giữ nguyên. Năng lượng và động lượng tăng theo `\gamma`.

Với `v\ll c`,

```math
E
=
mc^2+
\frac12mv^2+
\frac38m\frac{v^4}{c^2}+\cdots.
```

Hạng đầu là năng lượng nghỉ; hạng thứ hai chính là động năng Newton.

Như vậy cơ học cổ điển xuất hiện như khai triển bậc thấp của động lực học relativistic.

## Photon

Với photon,

```math
m=0,
```

nên

```math
E=pc.
```

Kết hợp với

```math
E=hf
```

cho

```math
p=\frac h\lambda.
```

Photon có động lượng dù không có khối lượng nghỉ.

## Bất biến khối lượng của một hệ

Với một hệ nhiều hạt, tổng bốn-động lượng

```math
P^\mu_{tot}=\sum_iP_i^\mu
```

xác định khối lượng bất biến của toàn hệ:

```math
M^2c^4
=
E_{tot}^2-p_{tot}^2c^2.
```

Trong hệ tâm động lượng `p_{tot}=0`, ta có

```math
E_{CM}=Mc^2.
```

Đây là lý do collider được phân tích bằng năng lượng tâm khối lượng thay vì chỉ nhìn năng lượng từng chùm trong phòng thí nghiệm.

## Hiệu ứng Doppler tương đối tính

Với nguồn và người quan sát chuyển động dọc cùng phương, tần số biến đổi theo

```math
f_{obs}
=
f_{src}
\sqrt{\frac{1-\beta}{1+\beta}}
```

cho trường hợp nguồn rời xa theo quy ước thích hợp.

Doppler tương đối tính kết hợp cả hiệu ứng chuyển động lẫn giãn thời gian, khác công thức Doppler âm thanh vốn dựa trên môi trường truyền sóng.

## `E=mc^2` nên hiểu thế nào?

`E=mc^2` là năng lượng nghỉ của một hệ có khối lượng bất biến `m`.

Khối lượng của một vật hợp thành bao gồm năng lượng nội tại của toàn hệ: động năng tương đối giữa các thành phần, năng lượng trường và năng lượng liên kết. Vì vậy khối lượng của hệ không luôn bằng tổng khối lượng nghỉ của các thành phần tách rời.

Trong phản ứng hạt nhân, chênh lệch khối lượng nghỉ giữa trạng thái đầu và cuối xuất hiện dưới dạng năng lượng động học hoặc bức xạ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Mọi thứ đều tương đối”

Không. Lý thuyết dựa mạnh vào các bất biến: `c`, khoảng không-thời gian, thời gian riêng, khối lượng bất biến và dạng hiệp biến của định luật vật lý.

### “Giãn thời gian là do ánh sáng mất thời gian tới mắt”

Không. Hiệu ứng còn tồn tại sau khi hiệu chỉnh thời gian truyền tín hiệu và được đo trực tiếp bằng đồng hồ nguyên tử cùng phân rã hạt.

### “Nếu mỗi người thấy đồng hồ kia chậm thì có mâu thuẫn”

Không. So sánh đồng hồ ở xa phụ thuộc tính tương đối của sự đồng thời. Khi hai người tái ngộ, thời gian riêng tích lũy trên worldline cho kết quả không mơ hồ.

### “Vật có khối lượng có thể tăng tốc vượt `c` nếu cấp đủ năng lượng”

Không. Khi `v\rightarrow c`, `\gamma\rightarrow\infty`, nên năng lượng cần thiết tăng không giới hạn trong lý thuyết.

## Mô hình tư duy (Mental Model)

Thuyết tương đối hẹp thay “không gian + thời gian tuyệt đối” bằng một không-thời gian bốn chiều có cấu trúc Minkowski. Các quan sát viên chia không-thời gian thành phần không gian và phần thời gian khác nhau, nhưng đồng ý về các bất biến và quan hệ nhân quả.

Một cách học hiệu quả là chuyển từ câu hỏi “đồng hồ nào thật sự chậm?” sang ba câu hỏi chính xác hơn:

1. Hai sự kiện nào đang được so sánh?
2. Worldline của từng vật là gì?
3. Đại lượng bất biến nào có thể tính mà không phụ thuộc hệ tọa độ?

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Hệ quy chiếu và vectơ](../00_foundations/02_space_time_vectors_frames.md), [Phương trình Maxwell](../05_electromagnetism/04_maxwell_em_waves.md).

**Liên hệ tiếp:** [Thuyết tương đối rộng](01_general_relativity.md), [Vật lý hạt](../09_atomic_nuclear_particle/03_particle_standard_model.md).
