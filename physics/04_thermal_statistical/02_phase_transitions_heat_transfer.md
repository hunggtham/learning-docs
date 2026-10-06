# Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chuyển pha và truyền nhiệt**. Route đi từ phase/state variables → thermodynamic potentials → latent heat → conduction/convection/radiation → critical behavior, để nhiệt động nối cân bằng với dòng năng lượng.

## Pha là gì?

Pha (phase / 상) là một trạng thái vĩ mô có cấu trúc và tính chất đồng nhất theo những tham số trật tự (order parameters) thích hợp. Rắn, lỏng và khí là các ví dụ quen thuộc, nhưng từ tính sắt từ, siêu dẫn, siêu chảy và nhiều pha lượng tử cho thấy khái niệm “pha” rộng hơn nhiều so với ba trạng thái vật chất cổ điển.

Một chuyển pha xảy ra khi trạng thái cân bằng tối ưu của hệ thay đổi khi nhiệt độ, áp suất, trường ngoài hoặc một tham số điều khiển khác đi qua một miền nhất định.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Vai trò của thế nhiệt động lực học** nối từ **Pha là gì?** sang **Nhiệt ẩn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vai trò của thế nhiệt động lực học

Ở nhiệt độ và áp suất cố định, hệ cân bằng ưu tiên trạng thái làm giảm năng lượng tự do Gibbs

```math
G=H-TS.
```

Hai pha có thể cùng tồn tại khi thế hóa học của chúng bằng nhau:

```math
\mu_1=\mu_2.
```

Vì `\mu` chính là năng lượng tự do Gibbs trên mỗi hạt trong một hệ một thành phần, đường đồng tồn tại pha trên giản đồ `P-T` là nơi hai pha có cùng “chi phí nhiệt động lực học”.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Nhiệt ẩn** nối từ **Vai trò của thế nhiệt động lực học** sang **Phương trình Clausius–Clapeyron**, vì cơ chế trước tạo đầu vào cho bước sau.

## Nhiệt ẩn

Trong nóng chảy hoặc sôi ở áp suất cố định, hệ có thể hấp thụ nhiệt trong khi nhiệt độ gần như không đổi:

```math
Q=mL.
```

Năng lượng không biến mất. Nó được dùng để thay đổi cấu trúc vi mô, khoảng cách phân tử, liên kết và entropy thay vì tăng nhiệt độ.

Với chuyển pha bậc nhất,

```math
L=T\Delta S.
```

Do đó nhiệt ẩn liên hệ trực tiếp với bước nhảy entropy giữa hai pha.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Phương trình Clausius–Clapeyron** nối từ **Nhiệt ẩn** sang **Vì sao nồi áp suất làm thức ăn chín nhanh hơn?**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phương trình Clausius–Clapeyron

Trên đường đồng tồn tại giữa hai pha,

```math
\frac{dP}{dT}=\frac{\Delta S}{\Delta V}
=\frac{L}{T\Delta V}.
```

Đây là phương trình Clapeyron. Với chuyển pha lỏng–hơi, nếu thể tích hơi lớn hơn nhiều thể tích lỏng và hơi gần khí lý tưởng, có thể thu được dạng Clausius–Clapeyron gần đúng:

```math
\frac{d\ln P}{dT}\approx\frac{L}{RT^2}.
```

Tích phân khi `L` gần hằng số cho

```math
\ln P\approx -\frac{L}{RT}+C.
```

Quan hệ này giải thích vì sao áp suất hơi bão hòa tăng rất nhanh theo nhiệt độ.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Vì sao nồi áp suất làm thức ăn chín nhanh hơn?** nối từ **Phương trình Clausius–Clapeyron** sang **Điểm ba và điểm tới hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vì sao nồi áp suất làm thức ăn chín nhanh hơn?

Nước sôi khi áp suất hơi bão hòa bằng áp suất môi trường. Tăng áp suất bên ngoài làm nhiệt độ sôi tăng. Nước trong nồi áp suất có thể đạt nhiệt độ cao hơn `100°C`, tăng tốc nhiều quá trình truyền nhiệt và phản ứng hóa học trong thực phẩm.

Ở vùng núi cao, áp suất khí quyển thấp hơn nên nước sôi ở nhiệt độ thấp hơn và thời gian nấu có thể dài hơn.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Điểm ba và điểm tới hạn** nối từ **Vì sao nồi áp suất làm thức ăn chín nhanh hơn?** sang **Chuyển pha bậc nhất và chuyển pha liên tục**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điểm ba và điểm tới hạn

Điểm ba (triple point) là điều kiện duy nhất nơi ba pha có thể đồng tồn tại cân bằng.

Điểm tới hạn (critical point) kết thúc đường đồng tồn tại lỏng–hơi. Gần điểm này, sự khác biệt giữa lỏng và khí dần biến mất; mật độ của hai pha tiến lại gần nhau và các thăng giáng trở nên lớn.

Khái niệm điểm tới hạn quan trọng vì nó cho thấy chuyển pha không phải lúc nào cũng là một “bước nhảy sắc nét” kiểu nóng chảy.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Chuyển pha bậc nhất và chuyển pha liên tục** nối từ **Điểm ba và điểm tới hạn** sang **Tham số trật tự**, vì cơ chế trước tạo đầu vào cho bước sau.

## Chuyển pha bậc nhất và chuyển pha liên tục

Trong chuyển pha bậc nhất, một đạo hàm bậc nhất của thế nhiệt động như entropy hoặc thể tích có bước nhảy. Nhiệt ẩn khác không.

Trong chuyển pha liên tục, tham số trật tự thay đổi liên tục nhưng độ nhạy của hệ có thể tăng mạnh hoặc phân kỳ trong giới hạn nhiệt động.

Ví dụ điển hình là chuyển pha sắt từ tại nhiệt độ Curie.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Tham số trật tự** nối từ **Chuyển pha bậc nhất và chuyển pha liên tục** sang **Độ dài tương quan và hành vi tới hạn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tham số trật tự

Tham số trật tự (order parameter) là đại lượng phân biệt hai pha.

Ví dụ với sắt từ, độ từ hóa `M` có thể bằng không ở pha thuận từ nhưng khác không dưới nhiệt độ Curie.

Một mô hình Landau đơn giản có năng lượng tự do

```math
F(M)=F_0+a(T-T_c)M^2+bM^4
```

với `b>0`.

Khi `T>T_c`, hệ số của `M^2` dương và cực tiểu nằm tại `M=0`. Khi `T<T_c`, hệ số đổi dấu và hai cực tiểu mới xuất hiện tại `M\neq0`.

Mô hình này minh họa cách phá vỡ đối xứng tự phát (spontaneous symmetry breaking) có thể tạo pha mới.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Độ dài tương quan và hành vi tới hạn** nối từ **Tham số trật tự** sang **Mầm pha và năng lượng bề mặt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Độ dài tương quan và hành vi tới hạn

Gần điểm tới hạn, thăng giáng ở những vùng rất xa nhau có thể trở nên tương quan. Độ dài tương quan `\xi` tăng mạnh và có thể tuân dạng

```math
\xi\sim |T-T_c|^{-\nu}.
```

Nhiều đại lượng tuân các luật lũy thừa với số mũ tới hạn (critical exponents).

Điều đặc biệt là các hệ vi mô rất khác nhau có thể chia sẻ cùng số mũ tới hạn. Đây là hiện tượng phổ quát (universality), một trong những ý tưởng sâu của vật lý thống kê.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Mầm pha và năng lượng bề mặt** nối từ **Độ dài tương quan và hành vi tới hạn** sang **Dẫn nhiệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Mầm pha và năng lượng bề mặt

Một pha mới không nhất thiết xuất hiện ngay khi nó có năng lượng tự do thấp hơn. Để hình thành một giọt mầm bán kính `r`, hệ phải trả chi phí năng lượng bề mặt nhưng nhận lợi ích năng lượng thể tích.

Một mô hình đơn giản:

```math
\Delta G(r)=4\pi r^2\gamma-\frac43\pi r^3\Delta g.
```

Hạng đầu là chi phí bề mặt, hạng sau là lợi ích thể tích. Vì vậy tồn tại bán kính tới hạn

```math
r_c=\frac{2\gamma}{\Delta g}.
```

Mầm nhỏ hơn `r_c` thường co lại; lớn hơn `r_c` có thể tiếp tục phát triển.

Điều này giải thích hiện tượng quá lạnh, quá nhiệt và vì sao bụi hay khuyết tật bề mặt có thể hỗ trợ tạo mầm.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Dẫn nhiệt** nối từ **Mầm pha và năng lượng bề mặt** sang **Điện trở nhiệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dẫn nhiệt

Định luật Fourier cho mật độ dòng nhiệt

```math
\vec q=-k\nabla T.
```

Dấu âm cho biết nhiệt đi theo hướng nhiệt độ giảm.

Kết hợp với bảo toàn năng lượng trong vật đồng nhất có thể dẫn tới phương trình nhiệt:

```math
\frac{\partial T}{\partial t}=\alpha\nabla^2T,
```

với

```math
\alpha=\frac{k}{\rho c_p}
```

là hệ số khuếch tán nhiệt.

Thang thời gian dẫn nhiệt trên chiều dài `L` có bậc

```math
t_{diff}\sim\frac{L^2}{\alpha}.
```

Vì phụ thuộc `L^2`, làm lạnh một vật dày gấp đôi có thể mất thời gian lớn hơn nhiều chứ không chỉ gấp đôi.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Điện trở nhiệt** nối từ **Dẫn nhiệt** sang **Đối lưu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Điện trở nhiệt

Với tấm phẳng dày `L`, diện tích `A`, dẫn nhiệt ổn định một chiều:

```math
R_{th}=\frac{L}{kA}.
```

Nếu nhiều lớp nối tiếp,

```math
R_{total}=\sum_iR_i.
```

Dòng nhiệt khi đó gần

```math
\dot Q=\frac{\Delta T}{R_{total}}.
```

Cấu trúc toán học giống mạch điện trở vì cả hai là bài toán dòng tuyến tính do chênh thế điều khiển.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Đối lưu** nối từ **Điện trở nhiệt** sang **Các số vô thứ nguyên trong truyền nhiệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Đối lưu

Đối lưu kết hợp chuyển động chất lưu với truyền năng lượng. Trong kỹ thuật thường dùng

```math
\dot Q=hA(T_s-T_\infty).
```

`h` không phải hằng số vật liệu cơ bản. Nó phụ thuộc vận tốc dòng, hình học, tính chất chất lưu và trạng thái lớp biên.

Đối lưu cưỡng bức dùng quạt hoặc bơm. Đối lưu tự nhiên xuất hiện do chênh lệch mật độ trong trường hấp dẫn.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Các số vô thứ nguyên trong truyền nhiệt** nối từ **Đối lưu** sang **Bức xạ nhiệt**, vì cơ chế trước tạo đầu vào cho bước sau.

## Các số vô thứ nguyên trong truyền nhiệt

Số Nusselt

```math
Nu=\frac{hL}{k}
```

so sánh truyền nhiệt đối lưu với dẫn nhiệt qua chất lưu.

Số Prandtl

```math
Pr=\frac{\nu}{\alpha}
```

so sánh khuếch tán động lượng với khuếch tán nhiệt.

Số Rayleigh kết hợp độ nổi và khuếch tán để đánh giá khả năng xuất hiện đối lưu tự nhiên.

Các số này cho phép phân loại chế độ truyền nhiệt mà không phụ thuộc hệ đơn vị.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Bức xạ nhiệt** nối từ **Các số vô thứ nguyên trong truyền nhiệt** sang **Định luật Kirchhoff về bức xạ**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bức xạ nhiệt

Một vật đen lý tưởng phát thông lượng năng lượng

```math
j^*=\sigma T^4.
```

Với vật thực có hệ số phát xạ `\varepsilon`, trao đổi bức xạ đơn giản với môi trường lớn ở nhiệt độ `T_{env}` là

```math
P=\varepsilon\sigma A(T^4-T_{env}^4).
```

Bức xạ không cần môi trường vật chất, vì vậy trong chân không nó trở thành cơ chế trao đổi nhiệt quan trọng.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Định luật Kirchhoff về bức xạ** nối từ **Bức xạ nhiệt** sang **Phổ vật đen và sự ra đời của lượng tử**, vì cơ chế trước tạo đầu vào cho bước sau.

## Định luật Kirchhoff về bức xạ

Ở cân bằng nhiệt, khả năng hấp thụ và phát xạ tại cùng bước sóng và góc liên hệ với nhau. Một vật hấp thụ tốt ở một dải phổ cũng có xu hướng phát tốt ở dải đó khi ở cân bằng.

Điều này nối nhiệt động lực học với điện từ học và tính chất quang học của vật liệu.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Phổ vật đen và sự ra đời của lượng tử** nối từ **Định luật Kirchhoff về bức xạ** sang **Bộ trao đổi nhiệt và hiệu suất thực tế**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phổ vật đen và sự ra đời của lượng tử

Mô hình cổ điển dẫn tới thảm họa tử ngoại khi áp dụng định lý phân bố đều năng lượng cho các chế độ (mode / 모드) điện từ trong hốc.

Planck giả sử trao đổi năng lượng theo lượng tử

```math
E=nh\nu.
```

Từ đó thu được phổ phù hợp thực nghiệm. Đây là một trong những bước mở đầu của cơ học lượng tử.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Bộ trao đổi nhiệt và hiệu suất thực tế** nối từ **Phổ vật đen và sự ra đời của lượng tử** sang **Thermal runaway**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bộ trao đổi nhiệt và hiệu suất thực tế

Trong thiết bị thực tế, truyền nhiệt thường kết hợp dẫn, đối lưu và bức xạ. Ví dụ CPU:

```text
junction chip
→ package
→ thermal interface material
→ heatsink
→ boundary layer không khí
→ môi trường
```

Mỗi bước có điện trở nhiệt riêng. Tối ưu một thành phần không đảm bảo toàn chuỗi tốt nếu nút thắt nằm ở giao diện khác.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Thermal runaway** nối từ **Bộ trao đổi nhiệt và hiệu suất thực tế** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Thermal runaway

Nếu một thiết bị tiêu tán nhiều công suất hơn khi nhiệt độ tăng, ta có phản hồi dương:

```text
nhiệt độ tăng
→ tổn hao tăng
→ công suất nhiệt tăng
→ nhiệt độ tăng thêm
```

Nếu khả năng tản nhiệt không đủ, hệ có thể chạy vào trạng thái mất ổn định nhiệt. Khái niệm này xuất hiện trong transistor, pin và nhiều hệ phản ứng hóa học.

> **Nối mạch:** Trong **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Thermal runaway** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Chuyển pha là sự thay đổi cấu trúc cân bằng của toàn hệ, còn truyền nhiệt là cách năng lượng di chuyển giữa các vùng. Nhiệt độ không phải thước đo duy nhất của năng lượng: trong chuyển pha, năng lượng có thể thay đổi cấu hình vi mô mà không làm nhiệt độ đổi đáng kể.

Gần điểm tới hạn, chi tiết vi mô có thể trở nên ít quan trọng hơn cấu trúc thang lớn và tính đối xứng, dẫn tới phổ quát.

> **Nối mạch:** Ở chặng này của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, **Những ngộ nhận thường gặp (Common Misconceptions)** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** mở rộng hệ quả hoặc giới hạn liên quan.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Nước đang sôi nhận nhiệt nhưng nhiệt độ không tăng nên năng lượng biến mất”

Không. Năng lượng đi vào thay đổi pha và entropy của hệ.

### “Đối lưu chỉ là dẫn nhiệt nhanh hơn”

Không. Đối lưu có vận chuyển khối lượng của chất lưu kết hợp với dẫn/khuếch tán nhiệt.

### “Vật màu đen luôn nóng hơn”

Màu nhìn thấy không đủ để kết luận toàn bộ tính chất bức xạ nhiệt. Hệ số hấp thụ và phát xạ phụ thuộc bước sóng, bề mặt và vật liệu.

### “Mọi chuyển pha đều có nhiệt ẩn”

Không. Chuyển pha liên tục có thể không có nhiệt ẩn nhưng có thăng giáng và độ nhạy rất mạnh gần điểm tới hạn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Chuyển pha và truyền nhiệt: năng lượng ẩn, đối lưu, bức xạ và hành vi tới hạn**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Nhiệt động lực học](00_thermodynamics.md), [Entropy và cơ học thống kê](01_entropy_statistical_mechanics.md), [Vận chuyển và khuếch tán](../03_continuum/02_transport_diffusion_heat.md).

**Liên hệ tiếp:** [Ensemble và hàm phân hoạch](03_ensembles_partition_functions.md), [Vật chất ngưng tụ và siêu dẫn](../10_condensed_matter_devices/02_transport_magnetism_superconductivity.md), [Quang học và vật đen](../06_optics/02_photons_lasers_coherence.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
