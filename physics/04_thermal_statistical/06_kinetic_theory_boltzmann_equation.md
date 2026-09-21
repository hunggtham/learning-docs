# Lý thuyết động học và phương trình Boltzmann: cầu nối từ hạt tới vận chuyển

Nhiệt động lực học mô tả trạng thái vĩ mô. Cơ học thống kê cân bằng cho biết xác suất các trạng thái vi mô khi hệ đã cân bằng. Nhưng nhiều hiện tượng quan trọng xảy ra **trong quá trình hệ đang tiến tới cân bằng**: khí khuếch tán, nhiệt lan truyền, độ nhớt xuất hiện hay plasma thư giãn sau một nhiễu loạn.

Lý thuyết động học (kinetic theory / 운동론) xây cầu nối giữa chuyển động vi mô của hạt và các phương trình vận chuyển vĩ mô.

## Hàm phân bố một hạt

Thay vì theo dõi mọi hạt, ta mô tả hệ bằng hàm phân bố

```math
f(\mathbf x,\mathbf v,t).
```

Ý nghĩa của nó là số hạt trung bình trong phần tử không gian pha

```math
d^3x\,d^3v
```

tỉ lệ với

```math
f(\mathbf x,\mathbf v,t)d^3x\,d^3v.
```

Từ `f`, nhiều đại lượng vĩ mô được lấy bằng moment theo vận tốc.

Mật độ số hạt:

```math
n(\mathbf x,t)=\int f\,d^3v.
```

Vận tốc trung bình:

```math
\mathbf u
=\frac1n\int \mathbf v f\,d^3v.
```

Mật độ năng lượng động học cũng thu được từ moment bậc hai của `v`.

## Phương trình Boltzmann

Trong dạng khái quát,

```math
\frac{\partial f}{\partial t}
+\mathbf v\cdot\nabla_{\mathbf x}f
+\frac{\mathbf F}{m}\cdot\nabla_{\mathbf v}f
=
\left(\frac{\partial f}{\partial t}\right)_{coll}.
```

Vế trái mô tả hạt trôi trong không gian và bị lực làm thay đổi vận tốc. Vế phải mô tả va chạm làm tái phân bố các hạt trong không gian vận tốc.

Đây không phải phương trình chuyển động của một hạt riêng lẻ. Nó là phương trình tiến hóa của **phân bố thống kê**.

## Nếu không có va chạm

Khi vế va chạm bằng không,

```math
\frac{Df}{Dt}=0
```

dọc theo quỹ đạo hạt trong không gian pha. Điều đó có nghĩa mật độ phân bố được vận chuyển theo dòng Hamilton của các hạt.

Trong plasma không va chạm, phiên bản này dẫn tới phương trình Vlasov khi lực được xác định tự nhất quán bởi trường điện từ của chính phân bố hạt.

## Vai trò của va chạm

Va chạm không chỉ “làm hạt chậm đi”. Trong khí loãng, va chạm giữa các hạt bảo toàn tổng năng lượng và động lượng nhưng làm phân bố vận tốc tiến dần tới dạng cân bằng Maxwell–Boltzmann.

Phân bố cân bằng một chiều có dạng Gaussian, còn trong ba chiều

```math
f_M(\mathbf v)
\propto
\exp\left[-\frac{m(\mathbf v-\mathbf u)^2}{2k_BT}\right].
```

Tốc độ nhiệt đặc trưng có bậc

```math
v_{th}\sim\sqrt{\frac{k_BT}{m}}.
```

Hạt nhẹ có tốc độ nhiệt lớn hơn hạt nặng ở cùng nhiệt độ.

## Quãng đường tự do trung bình

Giữa các va chạm, một hạt đi quãng đường trung bình `\lambda` gọi là **quãng đường tự do trung bình (mean free path)**.

Với khí loãng gồm hạt có tiết diện va chạm hiệu dụng `\sigma`, bậc độ lớn là

```math
\lambda\sim\frac{1}{n\sigma}.
```

Thời gian va chạm đặc trưng là

```math
\tau\sim\frac{\lambda}{v_{th}}.
```

`\lambda` và `\tau` quyết định khi nào mô hình chất lưu liên tục là hợp lý.

## Số Knudsen

So sánh quãng đường tự do trung bình với kích thước hệ `L`:

```math
Kn=\frac{\lambda}{L}.
```

Nếu

```math
Kn\ll1,
```

một phần tử chất lưu chứa nhiều va chạm trước khi thay đổi đáng kể trên thang `L`, nên mô hình liên tục thường tốt.

Nếu `Kn` không nhỏ, các hiệu ứng phi liên tục và biên động học trở nên quan trọng. Trong chân không kỹ thuật, vi lưu khí và khí quyển rất loãng, Navier–Stokes có thể không còn đủ.

## Từ Boltzmann tới phương trình liên tục

Lấy tích phân phương trình Boltzmann trên toàn không gian vận tốc. Vì va chạm bảo toàn số hạt, moment bậc không của hạng va chạm bằng không. Kết quả là

```math
\frac{\partial n}{\partial t}
+\nabla\cdot(n\mathbf u)=0.
```

Nhân thêm khối lượng cho ta phương trình bảo toàn khối lượng.

Đây là một kết quả quan trọng: phương trình liên tục của chất lưu không phải quy tắc tách rời khỏi động học vi mô; nó xuất hiện như moment của phương trình phân bố.

## Moment bậc nhất: phương trình động lượng

Nhân phương trình Boltzmann với `m\mathbf v` rồi tích phân theo vận tốc, ta thu được phương trình bảo toàn động lượng.

Cấu trúc tổng quát là

```math
\rho\frac{D\mathbf u}{Dt}
=-\nabla p+\nabla\cdot\boldsymbol\tau+\rho\mathbf b.
```

Khi quan hệ cấu thành thích hợp được dùng, nó tiến tới phương trình Navier–Stokes.

Như vậy Navier–Stokes có thể được nhìn như mô tả thấp bậc của một lý thuyết động học giàu thông tin hơn.

## Vì sao có độ nhớt?

Tưởng tượng hai lớp khí có vận tốc trung bình khác nhau. Các phân tử từ lớp nhanh bay sang lớp chậm mang theo động lượng lớn hơn trung bình; phân tử từ lớp chậm đi ngược lại mang động lượng nhỏ hơn.

Sự trao đổi động lượng vi mô này làm giảm gradient vận tốc và tạo ứng suất nhớt.

Bậc độ lớn của độ nhớt động học có thể hiểu qua

```math
\nu\sim v_{th}\lambda.
```

Hệ số chính xác phụ thuộc mô hình va chạm, nhưng cấu trúc cho thấy vận chuyển mạnh hơn khi hạt đi xa hơn và nhanh hơn giữa các va chạm.

## Vì sao có dẫn nhiệt?

Trong vùng nóng, phân tử có năng lượng động học trung bình lớn hơn. Các hạt chuyển động sang vùng lạnh mang năng lượng theo; hạt từ vùng lạnh mang ít năng lượng hơn quay lại.

Dòng năng lượng ròng hướng xuống gradient nhiệt độ dẫn tới định luật Fourier ở mức vĩ mô:

```math
\mathbf q=-k\nabla T.
```

Một lần nữa, hệ số vận chuyển vĩ mô xuất hiện từ chuyển động và va chạm vi mô.

## Vì sao có khuếch tán?

Nếu nồng độ một loại hạt không đồng đều, chuyển động ngẫu nhiên làm nhiều hạt rời vùng mật độ cao hơn số hạt đi ngược lại. Ở giới hạn gần cân bằng, ta thu được định luật Fick:

```math
\mathbf J=-D\nabla n.
```

Độ khuếch tán có bậc

```math
D\sim v_{th}\lambda.
```

Điểm sâu là khuếch tán, độ nhớt và dẫn nhiệt đều là các hình thức **vận chuyển do chuyển động vi mô giữa những vùng có giá trị vĩ mô khác nhau**.

## H-theorem và xu hướng tới cân bằng

Boltzmann đưa ra đại lượng

```math
H=\int f\ln f\,d^3v.
```

Dưới các giả định của mô hình va chạm Boltzmann,

```math
\frac{dH}{dt}\le0.
```

Điều này liên hệ với entropy tăng và xu hướng hệ tiến tới phân bố Maxwell–Boltzmann.

Tuy nhiên cần hiểu giả định “molecular chaos”: trước va chạm, vận tốc của hai hạt được xem gần như không tương quan. Việc đưa giả định thống kê này vào là nơi mũi tên thời gian xuất hiện trong mô tả động học, dù động lực học vi mô cơ bản có thể thuận nghịch.

## Nghịch lý thuận nghịch

Nếu phương trình Newton cho các hạt thuận nghịch theo thời gian, tại sao entropy lại tăng?

Không có mâu thuẫn đơn giản. Mô tả vĩ mô bỏ đi thông tin chi tiết về tương quan vi mô, và H-theorem dựa trên giả định thống kê về trạng thái trước va chạm. Entropy tăng là phát biểu về những trạng thái vĩ mô cực kỳ điển hình trong một không gian trạng thái khổng lồ, không phải tuyên bố rằng phương trình vi mô mất tính thuận nghịch.

## Xấp xỉ thời gian thư giãn

Một mô hình đơn giản cho hạng va chạm là

```math
\left(\frac{\partial f}{\partial t}\right)_{coll}
\approx-
\frac{f-f_{eq}}{\tau}.
```

Nó nói phân bố có xu hướng thư giãn về cân bằng `f_{eq}` với thời gian đặc trưng `\tau`.

Mặc dù đơn giản, xấp xỉ này rất hữu ích trong vật lý bán dẫn, transport điện tử và plasma khi cần trực giác về cạnh tranh giữa lực ngoài và va chạm.

## Liên hệ với mô hình Drude

Trong kim loại, mô hình Drude có thể được hiểu như một xấp xỉ động học rất đơn giản: electron được gia tốc bởi điện trường giữa các sự kiện tán xạ có thời gian thư giãn `\tau`.

Độ dẫn điện khi đó là

```math
\sigma=\frac{ne^2\tau}{m}.
```

Mô hình lượng tử hiện đại tinh tế hơn, nhưng ý tưởng “trường tạo động lượng có hướng, va chạm làm thư giãn phân bố” vẫn là nền tảng của lý thuyết vận chuyển.

## Khi phương trình Boltzmann không đủ?

Mô hình Boltzmann cổ điển có giới hạn. Với khí lượng tử suy biến, phải xét thống kê Fermi–Dirac hoặc Bose–Einstein và các hệ số chặn/tăng cường trạng thái cuối.

Trong hệ tương tác mạnh, tương quan nhiều hạt có thể quan trọng. Với plasma không va chạm, trường tự nhất quán và hiệu ứng tập thể có thể chi phối hơn va chạm hai hạt đơn giản.

Ở thang nano, mô tả sóng lượng tử hoặc vận chuyển Landauer có thể phù hợp hơn mô hình khuếch tán cổ điển.

## Mô hình tư duy (Mental Model)

Lý thuyết động học nằm giữa cơ học hạt và cơ học chất lưu:

```text
quỹ đạo từng hạt
→ hàm phân bố f(x,v,t)
→ moment của phân bố
→ mật độ, vận tốc, nhiệt độ
→ phương trình vận chuyển vĩ mô
```

Nó giải thích **vì sao** các định luật khuếch tán, độ nhớt và dẫn nhiệt có dạng gradient: hạt mang các đại lượng vi mô qua những khoảng tự do hữu hạn giữa các vùng có trạng thái khác nhau.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nhiệt độ là vận tốc của một hạt”

Không. Nhiệt độ mô tả đặc trưng thống kê của phân bố vận tốc của cả quần thể.

### “Va chạm luôn làm vận tốc hạt giảm”

Không. Va chạm tái phân bố năng lượng và động lượng giữa các hạt; một hạt riêng lẻ có thể nhanh lên hoặc chậm đi.

### “Navier–Stokes và Boltzmann là hai lý thuyết không liên quan”

Không. Trong miền thích hợp, phương trình chất lưu có thể được suy ra như các moment gần cân bằng của mô tả động học.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Ensemble và hàm phân hoạch](03_ensembles_partition_functions.md), [Hiện tượng vận chuyển](../03_continuum/02_transport_diffusion_heat.md).

**Liên hệ tiếp:** [Cơ học chất lưu](../03_continuum/00_fluids.md), [Vận chuyển trong chất rắn](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md), [Vật lý plasma](../10_condensed_matter_devices/03_plasma_physics.md).
