# Sức căng bề mặt, thấm ướt và mao dẫn

Bề mặt của chất lỏng có hành vi khác phần vật chất nằm sâu bên trong vì môi trường quanh các phân tử ở mặt phân cách không đối xứng. Từ sự bất đối xứng vi mô đó xuất hiện các hiện tượng vĩ mô như giọt nước gần hình cầu, côn trùng đứng trên mặt nước, chất lỏng leo lên ống nhỏ, mực bám giấy và sự hình thành bọt.

## Vì sao tạo bề mặt cần năng lượng?

Một phân tử nằm sâu trong chất lỏng tương tác với các phân tử xung quanh theo nhiều hướng. Ở gần mặt phân cách, số hàng xóm ở một phía giảm, nên trạng thái năng lượng của phân tử thay đổi. Vì vậy tạo thêm diện tích bề mặt thường cần công.

Sức căng bề mặt (surface tension / 표면장력) `\gamma` có thể nhìn theo hai cách tương đương:

```math
[\gamma]=\mathrm{J/m^2}=\mathrm{N/m}.
```

Cách nhìn năng lượng nói rằng tăng diện tích `dA` cần công gần

```math
dW=\gamma\,dA
```

nếu `\gamma` gần như không đổi. Cách nhìn lực nói rằng mặt phân cách tác dụng lực tiếp tuyến với độ lớn `\gamma` trên một đơn vị chiều dài đường biên.

Hai cách nhìn là cùng một vật lý, vì `1\,J=1\,N\cdot m`.

## Vì sao giọt nhỏ gần hình cầu?

Với thể tích cố định, hình cầu có diện tích bề mặt nhỏ nhất. Nếu năng lượng bề mặt xấp xỉ

```math
E_s=\gamma A,
```

hệ có xu hướng giảm `A`, nên giọt tự do nhỏ thường tiến gần hình cầu.

Tuy nhiên giọt lớn bị trọng lực làm biến dạng. Điều này cho thấy hình dạng không do một “quy luật hình cầu” riêng lẻ mà do cạnh tranh giữa năng lượng bề mặt và năng lượng hấp dẫn.

Một số vô thứ nguyên hữu ích là **số Bond (Bond number)**:

```math
Bo=\frac{\Delta\rho\,gL^2}{\gamma}.
```

Khi `Bo\ll1`, sức căng bề mặt chi phối hình dạng. Khi `Bo\gg1`, trọng lực quan trọng hơn.

## Độ cong và chênh lệch áp suất: phương trình Young–Laplace

Một mặt phân cách cong tạo chênh lệch áp suất giữa hai phía. Dạng tổng quát là

```math
\Delta P=\gamma\left(\frac1{R_1}+\frac1{R_2}\right),
```

trong đó `R_1` và `R_2` là hai bán kính cong chính.

Với giọt hình cầu,

```math
R_1=R_2=R,
```

nên

```math
\Delta P=\frac{2\gamma}{R}.
```

Với bong bóng xà phòng mỏng có hai mặt phân cách gần giống nhau, chênh lệch áp suất gần

```math
\Delta P=\frac{4\gamma}{R}.
```

Kết quả cho thấy bong bóng nhỏ có áp suất bên trong lớn hơn bong bóng lớn. Nếu hai bong bóng nối với nhau, khí có xu hướng đi từ bong bóng nhỏ sang bong bóng lớn, khiến bong bóng nhỏ co lại thêm.

## Suy ra Young–Laplace cho giọt cầu bằng cân bằng lực

Cắt tưởng tượng giọt cầu thành hai nửa. Chênh lệch áp suất tạo lực trên mặt cắt tròn:

```math
F_P=\Delta P\,\pi R^2.
```

Sức căng bề mặt kéo dọc chu vi:

```math
F_\gamma=\gamma\,2\pi R.
```

Cân bằng lực cho

```math
\Delta P\,\pi R^2=2\pi R\gamma,
```

suy ra

```math
\Delta P=\frac{2\gamma}{R}.
```

Suy dẫn này cho thấy chênh lệch áp suất xuất hiện vì lực bề mặt tác dụng trên chu vi phải cân bằng lực áp suất tác dụng trên diện tích.

## Thấm ướt và góc tiếp xúc

Khi chất lỏng tiếp xúc với chất rắn và khí, có ba năng lượng mặt phân cách cạnh tranh:

- chất rắn–khí;
- chất rắn–lỏng;
- lỏng–khí.

Góc tiếp xúc (contact angle / 접촉각) `\theta` mô tả hình học cân bằng tại đường ba pha. Quan hệ Young có dạng

```math
\gamma_{SV}-\gamma_{SL}=\gamma_{LV}\cos\theta.
```

Nếu `\theta` nhỏ, chất lỏng thấm ướt bề mặt tốt. Nếu `\theta` lớn, bề mặt có tính kỵ chất lỏng hơn.

Cách nói “nước thích kính” chỉ là ẩn dụ. Về vật lý, góc tiếp xúc là kết quả của sự cân bằng năng lượng bề mặt giữa các mặt phân cách.

## Bề mặt kỵ nước và siêu kỵ nước

Trên bề mặt nhám, góc tiếp xúc biểu kiến có thể khác đáng kể bề mặt phẳng. Nếu chất lỏng điền đầy cấu trúc nhám, mô hình Wenzel có thể phù hợp. Nếu giọt nằm trên đỉnh cấu trúc và giữ túi khí bên dưới, trạng thái Cassie–Baxter có thể xuất hiện.

Đây là cơ sở của lá sen, lớp phủ chống bám nước và nhiều bề mặt chức năng. Điều quan trọng là tính thấm ướt không chỉ phụ thuộc “vật liệu là gì” mà còn phụ thuộc cấu trúc bề mặt ở thang vi mô.

## Mao dẫn

Trong ống tròn bán kính `r`, sức căng bề mặt tác dụng dọc đường tiếp xúc có thành phần thẳng đứng

```math
F_\gamma=2\pi r\gamma\cos\theta.
```

Trọng lượng cột chất lỏng cao `h` là

```math
F_g=\rho g\pi r^2h.
```

Cân bằng cho

```math
2\pi r\gamma\cos\theta
=ho g\pi r^2h,
```

nên

```math
h=\frac{2\gamma\cos\theta}{\rho gr}.
```

Ống càng nhỏ, độ dâng càng lớn. Đây là ví dụ nổi bật cho việc hiệu ứng bề mặt trở nên quan trọng ở thang nhỏ.

Nếu `\cos\theta<0`, chất lỏng bị hạ xuống thay vì dâng lên. Vì vậy mao dẫn phụ thuộc cả sức căng bề mặt và khả năng thấm ướt.

## Vì sao hiệu ứng bề mặt mạnh ở vi mô?

Diện tích tỉ lệ gần với `L^2`, còn thể tích và khối lượng tỉ lệ với `L^3`. Khi giảm kích thước đặc trưng `L`, tỉ số diện tích trên thể tích tăng như

```math
\frac{A}{V}\sim\frac1L.
```

Do đó ở thang micromet, lực bề mặt có thể áp đảo trọng lực. Đây là lý do trực giác từ dòng nước quy mô lớn không còn phù hợp hoàn toàn trong vi lưu (microfluidics).

## Số capillary và cạnh tranh với độ nhớt

Khi chất lỏng chuyển động, một số vô thứ nguyên khác là **số capillary (capillary number)**:

```math
Ca=\frac{\mu v}{\gamma}.
```

`Ca` so sánh ứng suất nhớt với sức căng bề mặt. Khi `Ca\ll1`, mặt phân cách có xu hướng giữ hình dạng do sức căng bề mặt. Khi `Ca` tăng, dòng nhớt có thể kéo giãn và biến dạng mạnh giọt hoặc bong bóng.

Trong vi lưu, `Bo` và `Ca` giúp quyết định liệu hình học chịu chi phối bởi trọng lực, độ nhớt hay bề mặt.

## Áp suất mao dẫn trong lỗ rỗng

Trong vật liệu xốp, bán kính cong của mặt phân cách trong các lỗ nhỏ tạo áp suất mao dẫn. Cơ chế này tham gia vào việc nước di chuyển trong đất, giấy, vải, bê tông và mô sinh học.

Tuy nhiên không nên đơn giản hóa toàn bộ việc nước đi lên trong cây thành “chỉ nhờ mao dẫn”. Trong cây cao, sức căng trong cột nước, bốc hơi ở lá và cơ chế cohesion–tension đóng vai trò thiết yếu.

## Động lực học thấm vào ống nhỏ

Công thức chiều cao mao dẫn ở trên mô tả cân bằng cuối. Nhưng quá trình chất lỏng đi vào ống còn phụ thuộc độ nhớt. Ở giai đoạn mà quán tính nhỏ, định luật Washburn cho xu hướng

```math
L^2\propto t.
```

Điều này xuất hiện vì áp suất mao dẫn kéo chất lỏng vào, còn ma sát nhớt tăng khi cột chất lỏng dài hơn. Kết quả là quãng đường thấm tăng theo căn thời gian thay vì tuyến tính theo thời gian.

## Surfactant và sự thay đổi sức căng bề mặt

Chất hoạt động bề mặt (surfactant) tập trung ở mặt phân cách và có thể làm giảm `\gamma`. Xà phòng vì vậy giúp nước dễ lan trên bề mặt và ổn định bọt.

Nếu nồng độ surfactant không đều, gradient của sức căng bề mặt có thể tạo dòng gọi là **hiệu ứng Marangoni (Marangoni effect)**. Chất lỏng có xu hướng bị kéo từ vùng có sức căng bề mặt thấp sang vùng có sức căng cao hơn.

Hiệu ứng này xuất hiện trong sấy màng mỏng, hàn, giọt bay hơi và “nước mắt rượu vang”.

## Mô hình tư duy (Mental Model)

Mặt phân cách không phải một lớp trang trí không có động lực học. Nó mang năng lượng, tạo lực và ghép hình học độ cong với áp suất. Ở thang nhỏ, nơi tỉ số diện tích/thể tích lớn, vật lý bề mặt có thể trở thành cơ chế chi phối toàn hệ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Sức căng bề mặt là một lớp màng vật chất thật phủ lên nước”

Không. Nó là hệ quả của năng lượng và lực tại mặt phân cách, không phải một màng riêng biệt được đặt lên chất lỏng.

### “Mao dẫn luôn làm chất lỏng dâng lên”

Không. Dấu của `\cos\theta` quyết định chất lỏng dâng hay hạ so với mức ngoài ống.

### “Giọt luôn là hình cầu”

Chỉ khi sức căng bề mặt chi phối. Trọng lực, dòng chảy, điện trường hoặc tiếp xúc với bề mặt rắn có thể làm giọt biến dạng mạnh.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Cơ học chất lưu](00_fluids.md), [Công và năng lượng](../01_mechanics/03_work_energy_power.md).

**Liên hệ tiếp:** [Hiện tượng vận chuyển](02_transport_diffusion_heat.md), [Dòng rối, lưu biến và vật chất mềm](03_turbulence_rheology_soft_matter.md).
