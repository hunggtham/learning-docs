# Quang hình học: Fermat, phản xạ, khúc xạ, thấu kính và hệ tạo ảnh

Quang hình học (geometrical optics / 기하광학) mô tả ánh sáng bằng **tia (ray)**. Đây không phải mô hình cơ bản nhất của ánh sáng mà là xấp xỉ bước sóng ngắn: khi bước sóng nhỏ hơn nhiều kích thước đặc trưng của hệ, ta có thể bỏ qua phần lớn hiệu ứng nhiễu xạ và theo dõi hướng truyền năng lượng bằng các tia.

Chương này tập trung vào việc hiểu vì sao các định luật phản xạ, khúc xạ và công thức thấu kính xuất hiện, chúng dựa trên giả định nào và khi nào phải chuyển sang quang học sóng.

## Khi nào mô hình tia hợp lý?

Một tham số kiểm soát đơn giản là

```math
\frac{\lambda}{L}\ll1,
```

trong đó `\lambda` là bước sóng và `L` là thang hình học đặc trưng của khe, thấu kính hoặc vật cản.

Nếu `\lambda/L` không nhỏ, hiện tượng nhiễu xạ trở nên quan trọng và khái niệm “một tia đi qua một điểm” mất dần ý nghĩa.

Vì vậy quang hình học nên được xem là **giới hạn eikonal** của quang học sóng, không phải một lý thuyết hoàn toàn độc lập.

## Chỉ số khúc xạ

Trong môi trường, tốc độ pha của ánh sáng là

```math
v=\frac{c}{n},
```

nên

```math
n=\frac{c}{v}.
```

`n` thường phụ thuộc tần số, vì vậy cùng một vật liệu có thể khúc xạ các màu khác nhau. Hiện tượng này gọi là **tán sắc (dispersion)**.

Chỉ số khúc xạ không nên được hiểu đơn giản là “ánh sáng va vào nguyên tử nên chậm lại từng đoạn”. Trong mô tả điện từ cổ điển, trường kích thích phân cực vật chất và đáp ứng tập thể của môi trường làm thay đổi quan hệ pha giữa sóng và nguồn.

## Độ dài quang học

Độ dài quang học (optical path length, OPL) là

```math
\mathrm{OPL}=\int n\,ds.
```

Nếu `n` không đổi,

```math
\mathrm{OPL}=nL.
```

Vì thời gian truyền là

```math
t=\frac1c\int n\,ds,
```

độ dài quang học tỉ lệ trực tiếp với thời gian truyền.

## Nguyên lý Fermat

Nguyên lý Fermat phát biểu rằng đường đi vật lý của tia làm thời gian truyền, hay tương đương độ dài quang học, **dừng (stationary)** đối với những biến thiên nhỏ của đường đi:

```math
\delta\int n\,ds=0.
```

“Dừng” không nhất thiết luôn là “ngắn nhất”. Trong một số hệ, đường quang học có thể là cực đại hoặc điểm yên ngựa.

Đây là một nguyên lý biến phân giống về cấu trúc với nguyên lý tác dụng dừng trong cơ học Lagrange.

## Suy ra định luật phản xạ từ Fermat

Xét một điểm nguồn `A`, một điểm quan sát `B` và gương phẳng. Phản chiếu `B` qua mặt gương thành `B'`. Đường

```text
A → điểm phản xạ → B
```

có cùng độ dài với

```text
A → điểm phản xạ → B'.
```

Đường ngắn nhất từ `A` tới `B'` là đường thẳng, từ hình học suy ra

```math
\theta_i=\theta_r.
```

Định luật phản xạ vì vậy không cần được xem là một quy tắc độc lập phải học thuộc; nó là hệ quả của nguyên lý đường quang học dừng.

## Suy ra định luật Snell

Giả sử ánh sáng đi từ môi trường `n_1` sang `n_2`. Nếu điểm giao với mặt phân cách có tọa độ ngang `x`, thời gian truyền có dạng

```math
t(x)
=
\frac{n_1}{c}\sqrt{x^2+a^2}
+
\frac{n_2}{c}\sqrt{(L-x)^2+b^2}.
```

Điều kiện Fermat

```math
\frac{dt}{dx}=0
```

suy ra

```math
n_1\sin\theta_1=n_2\sin\theta_2.
```

Đây là định luật Snell.

Ta cũng có thể suy ra cùng kết quả từ điều kiện liên tục pha tại biên: thành phần song song với mặt phân cách của vectơ sóng được bảo toàn.

## Tần số không đổi, bước sóng thay đổi

Tại mặt phân cách đứng yên, tần số của sóng không đổi vì pha phải khớp theo thời gian. Do

```math
v=f\lambda,
```

khi `v` thay đổi thì `\lambda` thay đổi.

Vì vậy khi ánh sáng từ không khí đi vào thủy tinh, tần số và màu không tự đổi chỉ vì tốc độ pha giảm; bước sóng trong môi trường mới thay đổi.

## Phản xạ toàn phần

Nếu `n_1>n_2`, định luật Snell cho

```math
\sin\theta_2=\frac{n_1}{n_2}\sin\theta_1.
```

Khi vế phải vượt 1, không còn nghiệm góc truyền lan thực. Góc giới hạn thỏa

```math
\sin\theta_c=\frac{n_2}{n_1}.
```

Với `\theta_1>\theta_c`, xảy ra phản xạ toàn phần.

Tuy nhiên trường phía môi trường thứ hai không hoàn toàn bằng không. Một **trường suy giảm mũ (evanescent field)** vẫn tồn tại gần biên. Điều này quan trọng trong cảm biến, ghép quang và kính hiển vi trường gần.

## Mặt cầu và công thức tạo ảnh

Với một mặt khúc xạ cầu bán kính `R`, trong xấp xỉ paraxial ta có quan hệ gần đúng

```math
\frac{n_1}{s}+
\frac{n_2}{s'}
=
\frac{n_2-n_1}{R}.
```

Đây là công thức cơ bản để suy ra hành vi của thấu kính từ hai mặt khúc xạ.

Paraxial nghĩa là các tia nằm gần trục quang học và góc đủ nhỏ để dùng

```math
\sin\theta\approx\tan\theta\approx\theta.
```

Nếu góc lớn, các hạng bậc cao tạo quang sai.

## Công thức Lens-maker

Với thấu kính mỏng trong không khí có chỉ số `n`, hai bán kính cong `R_1,R_2`, tiêu cự gần đúng là

```math
\frac1f
=
(n-1)
\left(
\frac1{R_1}-\frac1{R_2}
\right).
```

Công thức này cho thấy tiêu cự không chỉ phụ thuộc vật liệu mà còn phụ thuộc hình học của hai mặt.

Một thấu kính hội tụ không “hút tia vào trục”. Nó thay đổi pha của sóng theo vị trí xuyên qua độ dày vật liệu, tạo một wavefront mới có xu hướng hội tụ.

## Phương trình thấu kính mỏng

Trong quy ước dấu thích hợp,

```math
\frac1f=\frac1{d_o}+\frac1{d_i}.
```

Độ phóng đại ngang là

```math
m=\frac{h_i}{h_o}=-\frac{d_i}{d_o}.
```

Dấu âm cho biết ảnh thật thường bị đảo chiều trong quy ước chuẩn.

Công thức này chỉ đúng tốt cho thấu kính mỏng và tia paraxial. Với hệ nhiều thấu kính hoặc lens dày, nên dùng ma trận truyền tia hoặc quang học Gaussian tổng quát.

## Ma trận ABCD

Trong quang học paraxial, một tia có thể mô tả bởi

```math
\begin{pmatrix}y\\\theta\end{pmatrix}.
```

Mỗi phần tử quang học tuyến tính tác dụng bằng ma trận

```math
\begin{pmatrix}y_2\\\theta_2\end{pmatrix}
=
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\begin{pmatrix}y_1\\\theta_1\end{pmatrix}.
```

Ví dụ truyền tự do khoảng `L`:

```math
\begin{pmatrix}1&L\\0&1\end{pmatrix},
```

còn thấu kính mỏng:

```math
\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}.
```

Cách này cho phép phân tích hệ nhiều thấu kính bằng đại số ma trận thay vì vẽ tia từng bước.

## Camera tạo ảnh như thế nào?

Một điểm vật phát nhiều tia. Hệ thấu kính biến wavefront phân kỳ từ điểm đó thành wavefront hội tụ về một điểm ảnh gần tương ứng.

Nếu sensor đặt đúng mặt phẳng ảnh, các tia của một điểm hội tụ gần cùng vị trí và ảnh sắc nét. Nếu sensor lệch khỏi mặt phẳng này, điểm biến thành một vùng mờ gọi là **circle of confusion**.

Khẩu độ nhỏ tăng độ sâu trường nhưng đồng thời tăng ảnh hưởng nhiễu xạ. Vì vậy không thể làm ảnh sắc vô hạn bằng cách đóng khẩu vô hạn.

## F-number và numerical aperture

F-number của hệ camera gần đúng là

```math
N=\frac{f}{D},
```

trong đó `D` là đường kính khẩu độ.

Trong kính hiển vi thường dùng numerical aperture

```math
NA=n\sin\theta.
```

`NA` càng lớn, hệ thu được góc không gian lớn hơn và có khả năng phân giải chi tiết nhỏ hơn, nhưng giới hạn cuối vẫn là nhiễu xạ chứ không phải hình học tia thuần túy.

## Quang sai

Thấu kính thực không hội tụ mọi tia và mọi màu vào cùng một điểm.

**Quang sai cầu (spherical aberration)** xuất hiện vì tia xa trục không tuân xấp xỉ paraxial tốt.

**Quang sai sắc (chromatic aberration)** xuất hiện vì `n=n(\lambda)` nên tiêu cự phụ thuộc màu.

Ngoài ra còn coma, astigmatism và field curvature.

Hệ quang học thực thường dùng nhiều phần tử với vật liệu và hình dạng khác nhau để bù các sai lệch này.

## Mắt người

Giác mạc cung cấp phần lớn công suất khúc xạ của mắt, còn thủy tinh thể điều chỉnh tiêu cự qua accommodation.

Cận thị thường làm ảnh của vật xa hội tụ trước võng mạc và được chỉnh bằng thấu kính phân kỳ. Viễn thị hoặc lão thị cần tăng công suất hội tụ trong các điều kiện tương ứng.

Mắt không chỉ là camera sinh học. Võng mạc và hệ thần kinh xử lý tín hiệu mạnh trước khi thông tin trở thành nhận thức thị giác.

## Sợi quang: từ ray picture tới mode picture

Mô hình tia nói ánh sáng bị giữ trong lõi nhờ phản xạ toàn phần. Mô hình sóng nói chỉ những mode thỏa điều kiện biên mới lan truyền ổn định.

Số mode phụ thuộc kích thước lõi, bước sóng và numerical aperture. Trong truyền thông tốc độ cao, dispersion mode, dispersion vật liệu, suy hao và hiệu ứng phi tuyến đều có thể giới hạn băng thông.

Vì vậy ray optics là trực giác ban đầu, còn thiết kế hệ sợi chính xác cần quang học sóng và điện từ học.

## Khi nào quang hình học thất bại?

Quang hình học trở nên không đủ khi:

- kích thước khe hoặc chi tiết gần bước sóng;
- cần tính nhiễu xạ và giới hạn phân giải;
- cần pha và giao thoa;
- cần phân cực;
- cần mô tả trường evanescent;
- cần photon statistics hoặc tương tác lượng tử.

Khi đó phải chuyển sang quang học sóng, Maxwell hoặc quang học lượng tử tùy thang bài toán.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Tia sáng là quỹ đạo thật của photon”

Không nên đồng nhất hai khái niệm. Tia là cấu trúc của xấp xỉ quang hình học; photon là đối tượng của mô tả lượng tử trường điện từ.

### “Ánh sáng luôn chọn đường ngắn nhất”

Nguyên lý Fermat nói đường quang học là stationary, không phải lúc nào cũng là cực tiểu tuyệt đối của chiều dài hình học.

### “Giảm khẩu độ luôn làm ảnh sắc hơn”

Ban đầu giảm khẩu có thể giảm quang sai hình học, nhưng khi khẩu quá nhỏ, nhiễu xạ làm độ phân giải xấu đi.

## Mô hình tư duy (Mental Model)

Quang hình học là bài toán tối ưu pha và đường truyền trong giới hạn `\lambda/L\ll1`. Tia sáng hữu ích vì nó nén thông tin của wavefront thành hướng truyền cục bộ. Khi hệ bắt đầu nhạy với pha, bước sóng hoặc khẩu độ, phải quay lại mô hình sóng đầy đủ hơn.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Sóng điện từ](../05_electromagnetism/04_maxwell_em_waves.md), [Ngôn ngữ toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Quang học sóng](01_wave_optics.md), [Quang học Fourier và hệ tạo ảnh](04_fourier_imaging_instrumentation.md).
