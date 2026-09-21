# Dao động, tắt dần, kích thích cưỡng bức và cộng hưởng

Dao động xuất hiện trong cơ học, điện từ, quang học, vật liệu, sinh học và kỹ thuật vì rất nhiều hệ có một trạng thái cân bằng ổn định. Khi hệ bị lệch khỏi cân bằng, một cơ chế hồi phục kéo nó trở lại; quán tính khiến hệ vượt qua vị trí cân bằng, và quá trình lặp lại tạo dao động.

Điểm sâu hơn là dao động điều hòa không chỉ là mô hình của lò xo. Nó là **xấp xỉ phổ quát gần một cân bằng ổn định**.

## Từ thế năng đến lực hồi phục

Giả sử thế năng `U(x)` có cực tiểu tại `x=0`. Quanh cực tiểu, khai triển Taylor cho

```math
U(x)=U(0)+U'(0)x+\frac12U''(0)x^2+\cdots.
```

Tại cực tiểu,

```math
U'(0)=0,
```

nên với dao động nhỏ,

```math
U(x)\approx U_0+\frac12kx^2,
```

với

```math
k=U''(0)>0.
```

Do

```math
F=-\frac{dU}{dx},
```

ta được

```math
F\approx-kx.
```

Vì vậy định luật Hooke xuất hiện tự nhiên như gần đúng bậc thấp nhất của rất nhiều thế năng trơn quanh cực tiểu. Đây là lý do cùng phương trình dao động điều hòa xuất hiện ở lò xo, con lắc góc nhỏ, dao động phân tử, mạch LC và mode của trường.

## Dao động điều hòa đơn

Phương trình Newton là

```math
m\ddot x=-kx,
```

hay

```math
\ddot x+\omega_0^2x=0,
```

với

```math
\omega_0=\sqrt{\frac{k}{m}}.
```

Nghiệm tổng quát có thể viết

```math
x(t)=A\cos(\omega_0t+\phi).
```

`A` là biên độ, `\phi` là pha ban đầu và `\omega_0` là tần số góc riêng. Chu kỳ là

```math
T=\frac{2\pi}{\omega_0},
```

còn tần số thông thường là

```math
f=\frac{1}{T},
\qquad
\omega_0=2\pi f.
```

Sine và cosine xuất hiện vì đạo hàm hai lần của chúng trả lại chính hàm với dấu âm:

```math
\frac{d^2}{dt^2}\cos(\omega t)=-\omega^2\cos(\omega t).
```

## Pha và không gian pha

Vận tốc là

```math
v(t)=-A\omega_0\sin(\omega_0t+\phi).
```

Trong mặt phẳng `x-v`, dao động điều hòa lý tưởng vẽ thành một đường kín. Nếu chuẩn hóa trục vận tốc theo `\omega_0`, quỹ đạo trở thành ellipse hoặc đường tròn tùy cách chọn tỉ lệ.

Cách nhìn này quan trọng vì một trạng thái của dao động tử không chỉ cần vị trí mà còn cần vận tốc. Hai hệ có cùng `x` nhưng khác `v` sẽ có tương lai khác nhau.

## Năng lượng trong dao động điều hòa

Tổng cơ năng là

```math
E=\frac12mv^2+\frac12kx^2.
```

Thay nghiệm vào, ta nhận được

```math
E=\frac12kA^2,
```

không đổi theo thời gian trong hệ lý tưởng.

Ở biên `x=\pm A`, vận tốc bằng không nên toàn bộ năng lượng là thế năng. Tại `x=0`, thế năng nhỏ nhất và tốc độ đạt cực đại nên năng lượng chủ yếu là động năng.

Dao động điều hòa có thể được hình dung như quá trình năng lượng liên tục trao đổi giữa hai “kho”: động năng và thế năng.

## Ví dụ: con lắc đơn và điều kiện góc nhỏ

Với con lắc dài `\ell`, phương trình chính xác là

```math
\ddot\theta+\frac{g}{\ell}\sin\theta=0.
```

Nếu `|\theta|\ll1` rad,

```math
\sin\theta\approx\theta,
```

nên

```math
\ddot\theta+\frac{g}{\ell}\theta=0.
```

Do đó

```math
\omega_0=\sqrt{\frac{g}{\ell}},
\qquad
T\approx2\pi\sqrt{\frac{\ell}{g}}.
```

Kết quả này không còn chính xác khi biên độ lớn. Khi đó chu kỳ tăng nhẹ theo biên độ và hệ trở thành phi tuyến. Đây là ví dụ quan trọng: **dao động điều hòa là xấp xỉ, không phải bản chất tuyệt đối của mọi dao động**.

## Dao động tắt dần

Hệ thực luôn có tổn hao. Một mô hình đơn giản cho lực cản tuyến tính theo vận tốc là

```math
F_d=-b\dot x.
```

Phương trình trở thành

```math
m\ddot x+b\dot x+kx=0.
```

Đặt

```math
\gamma=\frac{b}{2m},
\qquad
\omega_0=\sqrt{\frac{k}{m}}.
```

Ba chế độ xuất hiện.

### Tắt dần yếu

Nếu

```math
\gamma<\omega_0,
```

hệ vẫn dao động nhưng biên độ giảm theo hàm mũ:

```math
x(t)=Ae^{-\gamma t}\cos(\omega_dt+\phi),
```

với

```math
\omega_d=\sqrt{\omega_0^2-\gamma^2}.
```

Năng lượng giảm nhanh hơn biên độ vì `E\propto A^2`, nên gần đúng

```math
E(t)\propto e^{-2\gamma t}.
```

### Tắt dần tới hạn

Khi

```math
\gamma=\omega_0,
```

hệ trở về cân bằng nhanh nhất mà không dao động qua lại nhiều lần. Đây là chế độ hữu ích trong thiết kế cửa tự đóng, dụng cụ đo và một số hệ điều khiển.

### Tắt dần mạnh

Nếu

```math
\gamma>\omega_0,
```

hệ trở về cân bằng chậm mà không dao động. Lực cản quá lớn làm phản ứng ì hơn, chứ không phải lúc nào “nhiều damping hơn” cũng tốt hơn.

## Thời gian thư giãn và hệ số chất lượng

Với tắt dần yếu, thời gian đặc trưng để biên độ giảm đáng kể là bậc

```math
\tau\sim\frac{1}{\gamma}.
```

Hệ số chất lượng (quality factor, `Q`) thường được định nghĩa gần đúng bởi

```math
Q\approx\frac{\omega_0}{2\gamma}
```

cho hệ tắt dần yếu. `Q` lớn nghĩa hệ mất ít năng lượng trong mỗi chu kỳ và cộng hưởng hẹp, sắc. `Q` nhỏ nghĩa tổn hao lớn và đáp ứng theo tần số rộng hơn.

## Kích thích cưỡng bức

Nếu có lực tuần hoàn ngoài

```math
F(t)=F_0\cos(\omega t),
```

phương trình là

```math
m\ddot x+b\dot x+kx=F_0\cos(\omega t).
```

Nghiệm gồm hai phần:

```text
đáp ứng quá độ + đáp ứng xác lập
```

Phần quá độ phụ thuộc điều kiện ban đầu và giảm dần do tắt dần. Sau thời gian đủ lâu, chỉ còn đáp ứng xác lập với cùng tần số như lực cưỡng bức:

```math
x(t)=A(\omega)\cos(\omega t-\delta).
```

Biên độ phụ thuộc tần số:

```math
A(\omega)=
\frac{F_0}
{\sqrt{(k-m\omega^2)^2+(b\omega)^2}}.
```

Công thức này cho thấy cộng hưởng không chỉ là “tần số bằng nhau”. Nó là kết quả của sự cạnh tranh giữa quán tính, lực hồi phục và tổn hao.

## Cộng hưởng

Với tắt dần nhỏ, biên độ lớn nhất xảy ra gần

```math
\omega\approx\omega_0.
```

Ở tần số thấp, hệ gần như theo kịp lực ngoài và biến dạng chủ yếu do độ cứng quyết định. Ở tần số rất cao, quán tính chi phối và hệ không thể theo kịp lực. Gần tần số riêng, năng lượng được truyền vào hệ hiệu quả qua nhiều chu kỳ và biên độ tăng mạnh.

Tắt dần ngăn biên độ tăng vô hạn. Trong mô hình lý tưởng không có damping và kích thích đúng tần số riêng, nghiệm có thể tăng theo thời gian; hệ thực luôn có phi tuyến, tổn hao hoặc giới hạn cấu trúc trước khi điều đó xảy ra.

## Pha của đáp ứng

Không chỉ biên độ mà pha cũng thay đổi theo tần số. Ở tần số thấp, đáp ứng gần cùng pha với lực. Quanh cộng hưởng, độ trễ pha khoảng `\pi/2`. Ở tần số rất cao, đáp ứng gần ngược pha.

Pha là thông tin quan trọng trong mạch điện, hệ điều khiển, cơ học kết cấu và phép đo đáp ứng tần số. Hai hệ có biên độ giống nhau nhưng pha khác nhau có thể hành xử rất khác khi ghép với hệ khác.

## Cộng hưởng không phải lúc nào cũng có hại

Cộng hưởng được khai thác trong nhạc cụ, bộ lọc điện, đồng hồ quartz, MRI, anten, khoang laser và nhiều cảm biến. Ngược lại, cộng hưởng không mong muốn có thể làm tăng rung trong cầu, tòa nhà, máy quay hoặc rotor.

Bài toán kỹ thuật không phải “loại bỏ mọi cộng hưởng” mà là xác định mode nào tồn tại, chúng được kích thích bởi phổ lực nào, độ tắt dần bao nhiêu và biên độ có vượt giới hạn an toàn hay không.

## Từ một dao động tử đến nhiều mode

Một hệ nhiều bậc tự do không có chỉ một tần số riêng. Nó có nhiều mode chuẩn, mỗi mode có tần số riêng. Lực ngoài kích thích mạnh mode nào phụ thuộc không chỉ tần số mà còn **hình dạng lực có ghép với hình dạng mode hay không**.

Đây là cầu nối từ dao động đơn tới rung động kết cấu, âm học, phonon và lý thuyết trường.

## Mô hình tư duy (Mental Model)

Một dao động cần ba thành phần: **xu hướng hồi phục, quán tính và điều kiện ban đầu**. Tắt dần thêm cơ chế mất năng lượng. Kích thích ngoài thêm nguồn năng lượng. Cộng hưởng xuất hiện khi nhịp cấp năng lượng phù hợp với nhịp tự nhiên của hệ và cơ chế ghép đủ mạnh.

Dao động điều hòa là mô hình tuyến tính gần cân bằng. Khi biên độ lớn hoặc lực hồi phục phi tuyến, ta phải chuyển sang động lực học phi tuyến thay vì cố kéo dài công thức điều hòa quá miền áp dụng.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Cộng hưởng xảy ra chính xác tại `\omega=\omega_0` trong mọi trường hợp”

Không hoàn toàn. Tắt dần làm tần số biên độ cực đại dịch nhẹ, và các đại lượng như biên độ dịch chuyển, vận tốc hay công suất hấp thụ có thể đạt cực đại ở các tần số hơi khác nhau.

### “Damping càng lớn thì hệ trở về cân bằng càng nhanh”

Sai khi đi quá chế độ tới hạn. Hệ tắt dần mạnh có thể trở về cân bằng chậm hơn hệ tắt dần tới hạn.

### “Cộng hưởng tạo năng lượng”

Không. Năng lượng đến từ nguồn kích thích ngoài. Cộng hưởng chỉ làm truyền năng lượng hiệu quả hơn vào một mode của hệ.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Công, năng lượng và thế năng](../01_mechanics/03_work_energy_power.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Dao động ghép và mode chuẩn](02_coupled_oscillators_normal_modes.md), [Sóng và Fourier](01_waves_fourier_sound.md), [Mạch RLC và cộng hưởng](../05_electromagnetism/02_ac_rlc_circuits.md).
