# Điện tích, điện trường, định luật Gauss, điện thế và tụ điện

Điện tĩnh học nghiên cứu điện tích đứng yên hoặc các cấu hình thay đổi đủ chậm để có thể bỏ qua hiệu ứng cảm ứng và bức xạ. Đây là điểm khởi đầu tự nhiên của điện từ học vì nó cho phép xây dựng từng lớp: điện tích → lực → điện trường → thông lượng → điện thế → vật dẫn → tụ điện.

## Điện tích là gì?

Điện tích (electric charge / 전하) là một thuộc tính vật lý quyết định cách vật chất tương tác điện từ. Có hai dấu quy ước: dương và âm. Hai điện tích cùng dấu đẩy nhau, khác dấu hút nhau.

Điện tích có hai tính chất nền tảng.

### Bảo toàn điện tích

Trong mọi quá trình đã biết ở mức cơ bản,

```math
Q_{total}=\text{constant}.
```

Điện tích có thể di chuyển từ vật này sang vật khác hoặc xuất hiện dưới dạng cặp hạt–phản hạt, nhưng tổng điện tích của hệ kín không tự thay đổi.

### Lượng tử hóa điện tích

Điện tích quan sát được xuất hiện theo các đơn vị rời rạc gắn với điện tích cơ bản

```math
e\approx1.602\times10^{-19}\,\mathrm C.
```

Electron mang `-e`, proton mang `+e`. Quark có điện tích phân số `e`, nhưng quark tự do không được quan sát cô lập trong điều kiện thông thường.

## Định luật Coulomb

Hai điện tích điểm đứng yên `q_1` và `q_2` cách nhau khoảng `r` chịu lực có độ lớn

```math
F=\frac{1}{4\pi\varepsilon_0}
\frac{|q_1q_2|}{r^2}.
```

Dạng vectơ là

```math
\mathbf F_{1\to2}
=
\frac{1}{4\pi\varepsilon_0}
\frac{q_1q_2}{r^2}\hat{\mathbf r}.
```

Dấu của `q_1q_2` quyết định lực hút hay đẩy.

Cấu trúc `1/r^2` không phải ngẫu nhiên. Một nguồn điểm trong không gian ba chiều phân bố ảnh hưởng qua mặt cầu có diện tích

```math
4\pi r^2.
```

Nếu tổng thông lượng được bảo toàn, mật độ thông lượng tự nhiên giảm theo `1/r^2`.

## Nguyên lý chồng chập

Trong điện từ học cổ điển tuyến tính, lực hoặc điện trường do nhiều nguồn bằng tổng các đóng góp riêng:

```math
\mathbf E_{total}
=\sum_i\mathbf E_i.
```

Với phân bố điện tích liên tục,

```math
\mathbf E(\mathbf r)
=
\frac{1}{4\pi\varepsilon_0}
\int
\frac{\rho(\mathbf r')(\mathbf r-\mathbf r')}
{|\mathbf r-\mathbf r'|^3}
\,d^3r'.
```

Đây là bước chuyển từ bài toán vài điện tích điểm sang vật thể có phân bố điện tích liên tục.

## Điện trường

Điện trường (electric field / 전기장) tại một điểm được định nghĩa là lực trên một đơn vị điện tích thử dương rất nhỏ:

```math
\mathbf E=\frac{\mathbf F}{q_{test}}.
```

Với điện tích điểm `q`,

```math
\mathbf E
=
\frac{1}{4\pi\varepsilon_0}
\frac{q}{r^2}\hat{\mathbf r}.
```

Điện trường tách hai vai trò:

```text
nguồn điện tích → tạo trường
điện tích thử → phản ứng với trường
```

Một điện tích `q` đặt trong trường chịu lực

```math
\mathbf F=q\mathbf E.
```

Nếu `q<0`, lực ngược hướng điện trường.

## Đường sức điện không phải vật thể thật

Đường sức là công cụ hình dung. Tiếp tuyến với đường sức cho hướng của `\mathbf E`, còn mật độ tương đối của các đường gợi ý độ lớn trường.

Đường sức không phải dây vật lý và cũng không nhất thiết là quỹ đạo của hạt mang điện. Một hạt có quán tính; nếu vận tốc ban đầu không song song với trường, quỹ đạo có thể cắt các đường sức.

## Thông lượng điện

Thông lượng qua một mặt `S` là

```math
\Phi_E=\int_S\mathbf E\cdot d\mathbf A.
```

Thông lượng không phải “lượng điện trường bị tiêu thụ qua mặt”. Nó đo mức trường xuyên qua mặt có tính đến hướng của vectơ diện tích.

Với mặt kín,

```math
\Phi_E=\oint_S\mathbf E\cdot d\mathbf A.
```

## Định luật Gauss

Định luật Gauss phát biểu

```math
\oint_S\mathbf E\cdot d\mathbf A
=
\frac{Q_{enc}}{\varepsilon_0}.
```

Dạng vi phân là

```math
\nabla\cdot\mathbf E
=
\frac{\rho}{\varepsilon_0}.
```

Nó nói mật độ điện tích là nguồn của divergence điện trường.

Điểm rất quan trọng: định luật Gauss luôn đúng trong điện từ học cổ điển, nhưng **chỉ trở thành công cụ tính trường đơn giản khi đối xứng đủ mạnh**.

## Ví dụ: điện tích điểm từ định luật Gauss

Với điện tích điểm ở tâm, đối xứng cầu cho điện trường cùng độ lớn trên mặt cầu bán kính `r` và luôn theo pháp tuyến.

Do đó

```math
\oint\mathbf E\cdot d\mathbf A
=E(4\pi r^2).
```

Định luật Gauss cho

```math
E(4\pi r^2)=\frac{q}{\varepsilon_0},
```

suy ra

```math
E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}.
```

Ta thu lại định luật Coulomb.

## Ví dụ: mặt phẳng điện tích vô hạn

Một mặt phẳng lớn có mật độ điện tích bề mặt `\sigma` có trường đối xứng vuông góc mặt phẳng. Dùng một hộp Gauss mỏng cắt qua mặt phẳng,

```math
2EA=\frac{\sigma A}{\varepsilon_0},
```

nên

```math
E=\frac{\sigma}{2\varepsilon_0}.
```

Kết quả không phụ thuộc khoảng cách. Điều này không mâu thuẫn với `1/r^2` của điện tích điểm vì hình học nguồn hoàn toàn khác.

## Điện thế và thế năng

Điện thế (electric potential / 전위) là thế năng trên một đơn vị điện tích:

```math
V=\frac{U}{q}.
```

Hiệu điện thế giữa hai điểm là

```math
V_b-V_a
=-\int_a^b\mathbf E\cdot d\mathbf l.
```

Trong điện tĩnh,

```math
\nabla\times\mathbf E=0,
```

nên tích phân đường không phụ thuộc đường đi mà chỉ phụ thuộc hai đầu mút.

Đó là lý do ta có thể định nghĩa một điện thế vô hướng duy nhất.

## Quan hệ giữa điện trường và điện thế

Điện trường là gradient âm của điện thế:

```math
\mathbf E=-\nabla V.
```

Điện trường chỉ hướng điện thế giảm nhanh nhất. Một điện tích dương tự do có xu hướng gia tốc về phía điện thế thấp hơn, trong khi điện tích âm chịu lực theo hướng ngược lại.

Điện thế có lợi vì là đại lượng vô hướng. Thay vì cộng ba thành phần vectơ của điện trường, ta có thể cộng các điện thế rồi lấy gradient ở cuối.

## Điện thế của điện tích điểm

Chọn

```math
V(\infty)=0,
```

thì điện tích điểm có điện thế

```math
V(r)=
\frac{1}{4\pi\varepsilon_0}
\frac{q}{r}.
```

Thế năng của hai điện tích điểm là

```math
U(r)
=
\frac{1}{4\pi\varepsilon_0}
\frac{q_1q_2}{r}.
```

Nếu `q_1q_2>0`, đưa hai điện tích cùng dấu lại gần cần cung cấp công. Nếu `q_1q_2<0`, thế năng giảm khi chúng tiến gần nhau.

## Mặt đẳng thế

Mặt đẳng thế là tập hợp điểm có cùng `V`. Vì

```math
\mathbf E=-\nabla V,
```

điện trường vuông góc với mặt đẳng thế.

Di chuyển một điện tích dọc mặt đẳng thế không làm thay đổi thế năng điện trong điện tĩnh.

## Vật dẫn ở cân bằng điện tĩnh

Trong vật dẫn có hạt tải tự do. Nếu điện trường bên trong khác không, chúng sẽ tiếp tục di chuyển. Vì vậy ở cân bằng điện tĩnh lý tưởng,

```math
\mathbf E_{inside}=0.
```

Hệ quả:

1. toàn bộ vật dẫn có cùng điện thế;
2. điện tích dư nằm trên bề mặt;
3. điện trường ngay ngoài bề mặt vuông góc mặt dẫn;
4. mật độ điện tích bề mặt lớn hơn ở vùng có độ cong lớn.

## Vì sao điện tích tập trung ở đầu nhọn?

Một vùng có bán kính cong nhỏ cần trường ngoài lớn hơn để duy trì cùng điều kiện đẳng thế với phần còn lại của vật dẫn. Vì

```math
E_n=\frac{\sigma}{\varepsilon_0}
```

ngay ngoài vật dẫn lý tưởng trong chân không, trường lớn tương ứng mật độ điện tích bề mặt `\sigma` lớn.

Hiệu ứng này liên quan tới phóng điện corona và thiết kế đầu kim cao áp.

## Lồng Faraday

Một vỏ dẫn kín có thể làm suy giảm mạnh điện trường tĩnh bên trong vì điện tích tự do phân bố lại trên bề mặt sao cho trường trong phần kim loại bằng không.

Nếu khoang bên trong không chứa điện tích và hệ ở cân bằng điện tĩnh, điện thế trong khoang có thể trở thành hằng số.

Tuy nhiên “lồng Faraday chặn mọi sóng điện từ ở mọi tần số” là cách nói quá mạnh. Hiệu quả che chắn động phụ thuộc vật liệu, độ dày, khe hở và tần số.

## Tụ điện

Tụ điện gồm hai vật dẫn mang điện tích `+Q` và `-Q`. Điện dung được định nghĩa

```math
C=\frac{Q}{\Delta V}.
```

Điện dung phụ thuộc hình học và môi trường điện môi, không phụ thuộc trực tiếp `Q` trong hệ tuyến tính lý tưởng.

Với hai bản song song diện tích `A`, khoảng cách `d` và bỏ qua hiệu ứng mép,

```math
E\approx\frac{\sigma}{\varepsilon},
```

với

```math
\sigma=\frac{Q}{A}.
```

Hiệu điện thế là

```math
V=Ed
=\frac{Qd}{\varepsilon A}.
```

Do đó

```math
C=\varepsilon\frac{A}{d}.
```

## Năng lượng của tụ điện

Công cần để tích điện tụ dẫn tới

```math
U=\frac12CV^2
=\frac{Q^2}{2C}
=\frac12QV.
```

Trong chân không, năng lượng có thể được xem là lưu trong điện trường với mật độ

```math
u_E=\frac12\varepsilon_0E^2.
```

Đây là bước quan trọng về mặt tư duy: năng lượng điện không nhất thiết nên hình dung là “nằm trên các điện tích”; trường trong không gian mang năng lượng.

## Điện môi làm tăng điện dung như thế nào?

Khi đặt điện môi giữa hai bản, vật liệu bị phân cực. Điện tích liên kết tạo trường ngược một phần trường ngoài, làm hiệu điện thế nhỏ hơn với cùng điện tích tự do.

Vì

```math
C=\frac{Q}{V},
```

nên điện dung tăng.

Trong môi trường tuyến tính,

```math
\varepsilon=\varepsilon_r\varepsilon_0.
```

Cơ chế này được phát triển sâu hơn trong chương trường điện từ trong vật chất.

## Lực điện và năng lượng: chọn cách giải nào?

Nếu cần quỹ đạo tức thời, lực và điện trường thường trực tiếp hơn. Nếu chỉ quan tâm trạng thái đầu–cuối trong điện tĩnh, năng lượng và điện thế thường gọn hơn.

Đây là cùng sự phân chia từng xuất hiện trong cơ học:

```text
force picture ↔ energy picture
E-field ↔ potential
```

## Mô hình tư duy (Mental Model)

Điện tích tạo cấu trúc trường trong không gian. Trường cho lực cục bộ lên điện tích thử. Trong điện tĩnh, trường bảo toàn nên có thể nén thông tin thành điện thế vô hướng. Định luật Gauss nối nguồn với thông lượng, còn điều kiện biên của vật dẫn quyết định cách điện tích tái phân bố.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Điện thế khác không thì điện trường phải khác không”

Không. Điện trường phụ thuộc gradient của điện thế, không phụ thuộc giá trị tuyệt đối của `V`.

### “Định luật Gauss chỉ đúng cho hệ đối xứng”

Sai. Nó luôn đúng; đối xứng chỉ quyết định nó có giúp tính trường dễ hay không.

### “Bên trong mọi vật dẫn luôn có `E=0`”

Chỉ đúng trong cân bằng điện tĩnh lý tưởng. Dây đang dẫn dòng cần một điện trường nhỏ bên trong để duy trì dòng trong mô hình Ohm.

### “Tụ điện lưu điện tích trong điện môi”

Điện tích tự do chủ yếu nằm trên các bản dẫn; điện môi phân cực và thay đổi trường cùng điện dung.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Mạch DC](01_dc_circuits.md), [Điện tĩnh dạng bài toán biên](08_boundary_value_image_multipoles.md), [Trường điện từ trong vật chất](07_fields_in_matter_dielectrics_magnetism.md), [Maxwell và sóng điện từ](04_maxwell_em_waves.md).
