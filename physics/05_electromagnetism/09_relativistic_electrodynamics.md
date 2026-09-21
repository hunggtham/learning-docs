# Điện động lực học tương đối tính: điện trường và từ trường như một trường thống nhất

Điện động lực học tương đối tính (relativistic electrodynamics / 상대론적 전기동역학) viết điện trường, từ trường, điện tích và dòng điện trong ngôn ngữ không-thời gian để các định luật giữ cùng dạng dưới biến đổi Lorentz.

Trong cách nhìn này, tensor trường điện từ (electromagnetic field tensor / 전자기장 텐서) gom `\mathbf E` và `\mathbf B` thành một đối tượng hình học thống nhất.

## Vì sao từ trường phụ thuộc hệ quy chiếu?

Xét một dây dẫn trung hòa điện trong hệ phòng thí nghiệm nhưng có dòng điện vì các điện tích chuyển động. Một điện tích thử chuyển động song song dây có thể chịu lực từ.

Trong hệ quy chiếu chuyển động cùng điện tích thử, vận tốc tức thời của nó có thể bằng 0 nên hạng `q\mathbf v\times\mathbf B` thay đổi. Tuy nhiên dự đoán vật lý cuối cùng về chuyển động phải nhất quán giữa các hệ quán tính.

Thuyết tương đối hẹp giải quyết điều này bằng cách cho thấy `\mathbf E` và `\mathbf B` không phải hai trường hoàn toàn độc lập. Chúng là các thành phần khác nhau của cùng tensor điện từ; người quan sát chuyển động tương đối với nhau sẽ phân tách tensor đó thành điện trường và từ trường khác nhau.

## Bốn-thế điện từ

Điện thế vô hướng `\phi` và thế vectơ `\mathbf A` có thể ghép thành bốn-thế

```math
A^\mu=\left(\frac{\phi}{c},\mathbf A\right),
```

với dấu cụ thể phụ thuộc quy ước metric.

Biến đổi gauge có dạng hiệp biến

```math
A^\mu\to A^\mu+\partial^\mu\chi.
```

Gauge Lorenz là

```math
\partial_\mu A^\mu=0.
```

Viết bằng bốn-vectơ làm đối xứng Lorentz của điện từ học hiện ra rõ hơn nhiều so với biểu diễn chỉ bằng các vectơ ba chiều.

## Tensor trường điện từ

Tensor điện từ được định nghĩa bởi

```math
F^{\mu\nu}
=\partial^\mu A^\nu-\partial^\nu A^\mu.
```

Các thành phần thời gian–không gian chứa điện trường, còn các thành phần không gian–không gian chứa từ trường, với dấu phụ thuộc quy ước.

Dưới biến đổi Lorentz,

```math
F'^{\mu\nu}
=\Lambda^\mu_{\ \alpha}
\Lambda^\nu_{\ \beta}
F^{\alpha\beta}.
```

Do đó một phép boost có thể trộn điện trường và từ trường.

## Một ví dụ định tính về biến đổi trường

Nếu trong một hệ `S` chỉ có điện trường, một người quan sát chuyển động ngang so với trường thường sẽ thấy cả điện trường và từ trường.

Vì vậy câu “tại đây có từ trường hay không?” có thể phụ thuộc hệ quy chiếu, giống như khái niệm đồng thời trong thuyết tương đối.

Đối tượng hình học chung là `F^{\mu\nu}`; cách tách thành `\mathbf E` và `\mathbf B` phụ thuộc người quan sát.

## Lực Lorentz ở dạng hiệp biến

Với bốn-vận tốc `u^\mu` và bốn-động lượng `p^\mu`, phương trình chuyển động là

```math
\frac{dp^\mu}{d\tau}
=qF^{\mu\nu}u_\nu.
```

Phần không gian của phương trình này trở về

```math
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B).
```

Dạng hiệp biến cho thấy lực điện và lực từ chỉ là các thành phần của một định luật không-thời gian thống nhất.

## Bốn-dòng điện

Mật độ điện tích `\rho` và mật độ dòng điện `\mathbf J` ghép thành

```math
J^\mu=(c\rho,\mathbf J).
```

Phương trình liên tục

```math
\frac{\partial\rho}{\partial t}
+\nabla\cdot\mathbf J=0
```

trở thành

```math
\partial_\mu J^\mu=0.
```

Bảo toàn điện tích vì vậy có dạng hình học tương đối tính tự nhiên.

## Phương trình Maxwell ở dạng hiệp biến

Hai phương trình Maxwell chứa nguồn có thể gộp thành

```math
\partial_\mu F^{\mu\nu}=\mu_0J^\nu.
```

Hai phương trình Maxwell không chứa nguồn có thể viết bằng tensor đối ngẫu hoặc từ đồng nhất thức đạo hàm của tensor phản đối xứng.

Việc bốn phương trình Maxwell được gom thành các phương trình tensor không chỉ làm ký hiệu ngắn hơn. Nó cho thấy cấu trúc của lý thuyết tương thích tự nhiên với đối xứng Lorentz.

## Hai bất biến điện từ

Hai tổ hợp quan trọng giữ nguyên dưới biến đổi Lorentz là

```math
I_1=\mathbf E^2-c^2\mathbf B^2,
```

và

```math
I_2=\mathbf E\cdot\mathbf B.
```

Các bất biến này giúp phân loại cấu hình trường và trả lời những câu hỏi như: có tồn tại hệ quy chiếu nào trong đó `\mathbf B'=0` hay `\mathbf E'=0` hay không?

Không thể tùy ý boost để loại bỏ cả điện trường và từ trường trong mọi cấu hình.

## Tensor năng lượng–động lượng của trường điện từ

Trường điện từ mang năng lượng, động lượng và ứng suất. Các đại lượng này được gom trong tensor năng lượng–động lượng `T^{\mu\nu}`.

Mật độ năng lượng điện từ là

```math
u=\frac12\left(
\varepsilon_0E^2+\frac{B^2}{\mu_0}
\right).
```

Mật độ động lượng liên hệ với vector Poynting:

```math
\mathbf g=\frac{\mathbf S}{c^2}.
```

Áp suất bức xạ vì vậy không phải phép ẩn dụ. Ánh sáng mang dòng động lượng và có thể truyền lực lên vật chất.

## Relativistic beaming

Một nguồn chuyển động tương đối tính không nhất thiết phát đẳng hướng trong hệ phòng thí nghiệm, ngay cả khi phát xạ đơn giản trong hệ nghỉ của nguồn.

Hiệu ứng aberration và Doppler tập trung bức xạ về phía chuyển động.

Hệ số Doppler thường viết

```math
\delta
=\frac{1}{\gamma(1-\beta\cos\theta)}.
```

Nó xuất hiện trong jet tương đối tính và thiên văn năng lượng cao.

Độ sáng quan sát và thang thời gian có thể bị thay đổi mạnh bởi beaming, nên suy ra tính chất nội tại của nguồn phải xét đúng phép biến đổi hệ quy chiếu.

## Có thể nói “từ tính là hiệu ứng tương đối tính của điện học” không?

Có những ví dụ sư phạm cho thấy lực từ giữa các dòng điện có thể được phân tích lại bằng điện trường và co độ dài trong một hệ khác.

Điều này hữu ích để thấy mối liên hệ giữa điện học, từ học và tương đối tính.

Tuy nhiên không nên rút gọn thành câu “từ trường chỉ là điện trường giả”. Đối tượng thống nhất là trường điện từ; cách phân tách thành phần điện và từ phụ thuộc người quan sát. Cả hai đều có ý nghĩa vật lý đầy đủ trong hệ đang xét.

## Minimal coupling và hạt tương đối tính

Tác dụng của một hạt tích điện tương đối tính chứa hạng tương tác

```math
S_{int}=q\int A_\mu dx^\mu.
```

Lấy biến phân tác dụng dẫn tới lực Lorentz.

Cấu trúc minimal coupling này xuất hiện lại trong cơ học lượng tử và lý thuyết trường lượng tử qua đạo hàm hiệp biến.

Đây là cầu nối trực tiếp giữa thuyết tương đối, gauge potential và vật lý hạt.

## Worked reasoning: dây dẫn có dòng điện

Một dây trung hòa trong hệ phòng thí nghiệm gồm mạng ion dương gần đứng yên và electron dẫn chuyển động.

Điện tích thử đứng yên có thể không chịu lực từ. Nếu nó chuyển động song song dây, nó chịu lực `q\mathbf v\times\mathbf B`.

Trong hệ chuyển động cùng điện tích thử, mật độ điện tích của ion và electron biến đổi khác nhau do cấu trúc Lorentz của mật độ và dòng. Kết quả có thể xuất hiện điện trường ròng.

Hai hệ quy chiếu vẫn cho cùng dự đoán vật lý nếu trường và lực được biến đổi đúng.

Ví dụ này cho trực giác rằng từ tính có nguồn gốc tương đối tính, nhưng không thay thế formalism tensor đầy đủ.

## Trường điện từ ở giới hạn vận tốc thấp

Ở vận tốc nhỏ so với `c`, một số hiệu ứng từ có thể có bậc nhỏ hơn hiệu ứng điện với hệ số kiểu `v/c` hoặc `(v/c)^2`, tùy cấu hình.

Đây là lý do từ học đôi khi trông giống một hiệu chỉnh nhỏ của điện học trong hệ điện tích chậm. Nhưng trong plasma tương đối tính, beam năng lượng cao hay bức xạ, điện và từ phải được xử lý ngang hàng.

## Kiểm tra bất biến trước khi biến đổi từng thành phần

Trong nhiều bài toán, thay vì biến đổi từng thành phần của `\mathbf E` và `\mathbf B`, ta có thể kiểm tra trước

```math
I_1=E^2-c^2B^2,
```

```math
I_2=\mathbf E\cdot\mathbf B.
```

Nếu `I_2\neq0`, chẳng hạn, không thể tìm hệ trong đó một trường biến mất hoàn toàn đồng thời vẫn giữ cấu trúc tùy ý của trường còn lại.

Bất biến giúp loại bỏ nhiều khả năng trước khi làm đại số chi tiết.

## Miền áp dụng và quy ước

Dấu trong `F^{\mu\nu}`, `A^\mu` và tensor metric phụ thuộc quy ước ký hiệu. Khi so sánh giáo trình, cần kiểm tra metric signature và định nghĩa thành phần.

Điện động lực học cổ điển tương đối tính vẫn là lý thuyết cổ điển. Khi phát xạ từng photon, hiệu ứng chân không lượng tử hoặc quá trình tạo–hủy hạt quan trọng, cần điện động lực học lượng tử.

## Mô hình tư duy (Mental Model)

Thuyết tương đối không chỉ “sửa thêm vài công thức” cho điện từ học. Nó cho thấy điện trường và từ trường là hai cách người quan sát phân tách cùng một tensor không-thời gian.

Có thể nhìn cấu trúc như sau:

```text
four-potential Aμ
→ field tensor Fμν
→ Maxwell equations
→ Lorentz force
→ stress-energy tensor
→ energy / momentum / radiation in different frames
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Đổi hệ quy chiếu luôn có thể làm từ trường biến mất”

Không. Chỉ một số cấu hình trường cho phép điều đó. Các bất biến điện từ quyết định khả năng này.

### “Điện trường và từ trường không thật vì phụ thuộc người quan sát”

Sai. Nhiều đại lượng vật lý phụ thuộc hệ quy chiếu. Điều quan trọng là quy luật biến đổi giữa các người quan sát nhất quán.

### “Tương đối tính chỉ có ý nghĩa khi vận tốc gần tốc độ ánh sáng”

Hiệu chỉnh số có thể nhỏ ở vận tốc thấp, nhưng cấu trúc khái niệm của từ trường và dòng điện vẫn gắn với đối xứng Lorentz.

### “Dạng tensor chỉ là ký hiệu sang trọng”

Không. Nó làm các bất biến và tính hiệp biến hiện rõ, đồng thời giảm nguy cơ áp dụng sai công thức ba-vectơ giữa các hệ quy chiếu.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md), [Maxwell](04_maxwell_em_waves.md), [Thế điện từ và gauge](06_potentials_gauge.md).

**Liên hệ tiếp:** [Bức xạ và anten](08_radiation_scattering_antennas.md), [Trường lượng tử](../09_atomic_nuclear_particle/05_quantum_fields_symmetry_interactions.md).
