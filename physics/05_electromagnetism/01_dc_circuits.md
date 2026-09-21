# Dòng điện, điện trở, Kirchhoff và mạch DC

Mạch điện một chiều là mô hình mức hệ thống của điện từ học. Nó thay các trường phân bố trong không gian bằng một số biến như điện áp, dòng điện, điện trở và điện dung. Mô hình này cực kỳ hữu ích, nhưng chỉ đúng khi kích thước mạch và tốc độ biến thiên cho phép bỏ qua độ trễ lan truyền đáng kể.

## Dòng điện là tốc độ truyền điện tích

Dòng điện (electric current / 전류) được định nghĩa

```math
I=\frac{dQ}{dt}.
```

Đơn vị là ampere:

```math
1\,A=1\,C/s.
```

Chiều dòng điện quy ước là chiều chuyển động của điện tích dương. Trong kim loại, electron mang điện âm nên vận tốc trôi của electron ngược chiều dòng điện quy ước.

## Vận tốc trôi và tốc độ truyền tín hiệu

Trong dây kim loại, electron có chuyển động nhiệt rất nhanh nhưng vận tốc trôi trung bình do điện trường thường nhỏ. Điều này không có nghĩa bóng đèn phải chờ electron đi từ công tắc tới bóng mới sáng.

Khi đóng mạch, thay đổi điện trường lan qua cấu trúc mạch với tốc độ liên quan tới tốc độ sóng điện từ trong môi trường, thường là một phần đáng kể của `c`. Các electron tại nhiều vị trí trong dây bắt đầu thay đổi chuyển động gần như cùng lúc theo trường địa phương mới.

Vì vậy cần phân biệt:

```text
vận tốc trôi của hạt tải
≠
tốc độ lan truyền tín hiệu điện từ
```

## Mật độ dòng điện

Ở mức cục bộ,

```math
\mathbf J=\rho_q\mathbf v_d,
```

hoặc với mật độ hạt tải `n` và điện tích mỗi hạt `q`,

```math
\mathbf J=nq\mathbf v_d.
```

Dòng qua một mặt là

```math
I=\int_A\mathbf J\cdot d\mathbf A.
```

Điện tích bảo toàn theo phương trình liên tục

```math
\frac{\partial\rho_q}{\partial t}
+\nabla\cdot\mathbf J=0.
```

Đây là cùng cấu trúc bảo toàn xuất hiện trong chất lưu: lượng trong một vùng thay đổi do dòng qua biên.

## Quan hệ Ohm ở mức vĩ mô

Với một phần tử ohmic trong miền hoạt động tuyến tính,

```math
V=IR.
```

Điện trở của dây đều dài `L`, tiết diện `A` và điện trở suất `\rho` là

```math
R=\rho\frac{L}{A}.
```

Dây dài hơn có điện trở lớn hơn vì hạt tải phải đi qua quãng đường dài hơn. Tiết diện lớn hơn giảm điện trở vì có nhiều kênh dẫn song song hơn.

## Quan hệ Ohm ở mức vi mô

Trong vật liệu tuyến tính đẳng hướng,

```math
\mathbf J=\sigma\mathbf E,
```

với `\sigma` là độ dẫn điện và

```math
\sigma=\frac1\rho.
```

Quan hệ này cho thấy `V=IR` là kết quả vĩ mô của một quan hệ cục bộ giữa trường và mật độ dòng.

Ohm không phải định luật phổ quát cho mọi linh kiện. Diode, transistor, bóng đèn dây tóc và nhiều điện cực hóa học có đặc tuyến `I-V` phi tuyến.

## Nguồn điện áp và sức điện động

Pin hoặc nguồn lý tưởng được mô hình như thiết bị cung cấp chênh lệch thế điện hóa. Suất điện động (electromotive force, emf) `\mathcal E` có đơn vị volt dù tên chứa chữ “force”. Nó biểu diễn năng lượng được cung cấp trên mỗi đơn vị điện tích:

```math
\mathcal E=\frac{W_{non-electrostatic}}{q}.
```

Trong pin, năng lượng hóa học duy trì sự tách điện tích và chênh lệch thế.

## Điện trở trong của nguồn

Nguồn thực không lý tưởng. Mô hình đơn giản dùng emf `\mathcal E` nối tiếp điện trở trong `r`.

Nếu cấp dòng `I`, điện áp cực nguồn là

```math
V_{terminal}=\mathcal E-Ir.
```

Khi tải yêu cầu dòng lớn, sụt áp trong nguồn tăng và một phần năng lượng bị tỏa nhiệt bên trong pin.

## Công suất điện

Công suất mà một phần tử hấp thụ là

```math
P=VI.
```

Với điện trở ohmic,

```math
P=I^2R
=\frac{V^2}{R}.
```

Năng lượng điện chuyển thành nhiệt qua tương tác giữa hạt tải và mạng tinh thể hoặc các cơ chế tán xạ khác.

Công suất không phải “dòng điện bị tiêu thụ”. Điện tích vẫn được bảo toàn; thứ được chuyển đổi là năng lượng.

## Quy tắc dấu công suất

Nếu dòng đi vào cực được chọn là điện áp dương của một phần tử, quy ước thụ động cho

```math
P=VI>0
```

khi phần tử hấp thụ năng lượng.

Nếu `P<0`, phần tử đang cung cấp năng lượng cho phần còn lại của mạch. Quy tắc dấu giúp tránh nhầm lẫn khi nguồn có thể vừa nạp vừa xả như pin sạc.

## Định luật Kirchhoff về dòng điện

Tại một nút mạch trong mô hình tập trung,

```math
\sum I_{in}=\sum I_{out}.
```

Đây là KCL (Kirchhoff's Current Law / 키르히호프 전류 법칙) và xuất phát từ bảo toàn điện tích.

Nếu điện tích đáng kể đang tích tụ tại nút, dạng tổng quát hơn là

```math
\sum I_{in}-\sum I_{out}
=\frac{dQ_{node}}{dt}.
```

Trong mạch tập trung thông thường, điện tích nút ổn định rất nhanh nên vế phải được xem gần bằng không.

## Định luật Kirchhoff về điện áp

Trong một vòng kín quasi-static,

```math
\sum_{loop}\Delta V=0.
```

Đây là KVL (Kirchhoff's Voltage Law / 키르히호프 전압 법칙).

Tuy nhiên KVL không phải một chân lý tách khỏi Maxwell. Nếu từ thông qua vòng thay đổi đáng kể,

```math
\oint\mathbf E\cdot d\mathbf l
=-\frac{d\Phi_B}{dt},
```

nên tổng “voltage drops” electrostatic đơn giản cần được sửa bằng emf cảm ứng.

Điều này cho thấy Kirchhoff là xấp xỉ mạch của điện từ học đầy đủ.

## Điện trở nối tiếp và song song

Với điện trở nối tiếp, cùng dòng đi qua mọi phần tử và hiệu điện thế cộng:

```math
R_{eq}=R_1+R_2+\cdots.
```

Với điện trở song song, cùng hiệu điện thế đặt lên các nhánh và dòng cộng:

```math
\frac1{R_{eq}}
=\frac1{R_1}+\frac1{R_2}+\cdots.
```

Đây không nên học như hai công thức biệt lập. Chúng đi trực tiếp từ topology của mạch cộng với KCL/KVL và quan hệ `V=IR`.

## Chia áp

Hai điện trở nối tiếp `R_1,R_2` với nguồn `V` có cùng dòng

```math
I=\frac{V}{R_1+R_2}.
```

Điện áp trên `R_2` là

```math
V_2
=IR_2
=V\frac{R_2}{R_1+R_2}.
```

Đây là mạch chia áp (voltage divider).

Khi nối thêm tải vào đầu ra, tải làm thay đổi điện trở tương đương và tỉ số chia áp. Vì vậy công thức chia áp lý tưởng chỉ đúng khi tải không làm mạch thay đổi đáng kể hoặc đã được đưa vào mô hình.

## Chia dòng

Với hai nhánh song song,

```math
I_1=\frac{V}{R_1},
\qquad
I_2=\frac{V}{R_2}.
```

Nhánh có điện trở nhỏ hơn nhận dòng lớn hơn. Với tổng dòng `I`, hai điện trở có quan hệ

```math
I_1
=I\frac{R_2}{R_1+R_2}.
```

Công thức có vẻ “ngược” vì dòng qua `R_1` chứa `R_2`, nhưng điều này chỉ phản ánh việc nhánh điện trở lớn hơn cạnh tranh kém hơn trong chia dòng.

## Tụ điện trong mạch DC

Tụ điện thỏa

```math
Q=CV,
```

nên

```math
I=C\frac{dV}{dt}.
```

Nếu điện áp không đổi theo thời gian,

```math
I=0.
```

Vì vậy ở trạng thái DC xác lập, tụ lý tưởng không cho dòng dẫn liên tục đi qua. Nhưng trong quá trình chuyển tiếp, nó có thể nhận hoặc nhả dòng lớn.

## Mạch RC nạp điện

Xét nguồn `V_0`, điện trở `R` và tụ `C` nối tiếp. KVL cho

```math
V_0=IR+\frac{Q}{C}.
```

Vì

```math
I=\frac{dQ}{dt},
```

ta có

```math
R\frac{dQ}{dt}+\frac{Q}{C}=V_0.
```

Nghiệm là

```math
Q(t)=CV_0\left(1-e^{-t/RC}\right).
```

Điện áp trên tụ:

```math
V_C(t)=V_0\left(1-e^{-t/RC}\right).
```

Dòng điện:

```math
I(t)=\frac{V_0}{R}e^{-t/RC}.
```

## Hằng số thời gian

Đặt

```math
\tau=RC.
```

Sau `t=\tau`, tụ đạt

```math
1-e^{-1}\approx63.2\%
```

của điện áp cuối.

Sau khoảng `5\tau`, hệ thường được xem gần trạng thái xác lập trong nhiều ứng dụng kỹ thuật.

`RC` có đơn vị thời gian:

```math
[\Omega][F]=s.
```

Phân tích thứ nguyên giúp kiểm tra ngay công thức.

## Xả tụ

Nếu bỏ nguồn và cho tụ xả qua điện trở,

```math
R\frac{dQ}{dt}+\frac{Q}{C}=0,
```

nên

```math
Q(t)=Q_0e^{-t/RC}.
```

Hàm mũ xuất hiện vì tốc độ thay đổi tỉ lệ với lượng còn lại.

Cùng cấu trúc này xuất hiện trong phân rã phóng xạ, làm nguội tuyến tính hóa và nhiều hệ bậc nhất.

## Năng lượng khi nạp tụ

Năng lượng lưu trên tụ cuối cùng là

```math
U_C=\frac12CV_0^2.
```

Nếu nạp tụ từ nguồn áp lý tưởng qua điện trở, tổng năng lượng nguồn cung cấp là

```math
CV_0^2.
```

Một nửa được lưu trong tụ, một nửa bị tỏa nhiệt trên điện trở, bất kể giá trị `R` trong mô hình lý tưởng. `R` chỉ thay đổi tốc độ nạp, không thay đổi tỉ lệ năng lượng cuối.

Đây là một kết quả đáng chú ý và nhắc rằng cần phân biệt động lực học theo thời gian với cân bằng năng lượng tổng.

## Mạch tập trung có giới hạn

Mô hình lumped circuit giả sử điện áp và dòng có thể gán cho phần tử mà không cần theo dõi độ trễ lan truyền bên trong chúng.

Khi kích thước mạch trở nên đáng kể so với bước sóng tín hiệu hoặc cạnh xung quá nhanh, cần dùng đường truyền (transmission line) và điện từ học phân bố.

Một dây dài ở GHz không thể luôn được xem chỉ là một điện trở hoặc một kết nối lý tưởng.

## Mô hình tư duy (Mental Model)

Mạch DC là cách nén điện từ học thành một mạng các phần tử. Dòng điện là thông lượng điện tích, điện áp là chênh lệch năng lượng trên mỗi điện tích, KCL là bảo toàn điện tích và KVL là xấp xỉ quasi-static của trường điện bảo toàn.

Điện trở mô tả mất năng lượng có hướng của hạt tải vào dao động vi mô; tụ điện lưu năng lượng trong trường; nguồn chuyển năng lượng từ hóa học hoặc cơ chế khác thành năng lượng điện.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Pin đẩy ra một dòng cố định”

Không. Nguồn gần lý tưởng cố định điện áp; dòng phụ thuộc toàn bộ tải và điện trở trong.

### “Dòng điện bị dùng hết sau điện trở”

Không. Ở mạch nối tiếp xác lập, cùng dòng đi vào và đi ra điện trở. Năng lượng bị chuyển hóa, không phải điện tích biến mất.

### “Tụ điện là hở mạch trong mọi thời điểm”

Chỉ ở DC xác lập lý tưởng. Trong quá trình nạp/xả hoặc tín hiệu thay đổi, tụ có dòng `I=C\,dV/dt`.

### “Kirchhoff luôn đúng chính xác cho mọi dây và mọi tần số”

Không. Quy tắc mạch tập trung là xấp xỉ của Maxwell; ở tần số cao hoặc kích thước lớn phải tính lan truyền và cảm ứng.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Điện tĩnh học](00_electrostatics.md), [Bảo toàn và thang đo](../00_foundations/04_symmetry_conservation_scale.md).

**Liên hệ tiếp:** [Mạch AC và RLC](02_ac_rlc_circuits.md), [Đường truyền và ống dẫn sóng](05_transmission_lines_waveguides.md), [Bán dẫn và thiết bị](../10_condensed_matter_devices/01_semiconductors_devices.md).
