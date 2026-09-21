# Từ trường, lực Lorentz, cảm ứng điện từ và độ tự cảm

## Vì sao từ tính không tách rời khỏi điện?

Điện và từ từng được nghiên cứu như hai nhóm hiện tượng riêng. Lý thuyết Maxwell cho thấy chúng là hai mặt của cùng một trường điện từ (electromagnetic field). Thuyết tương đối hẹp còn làm mối liên hệ này sâu hơn: những người quan sát chuyển động tương đối với nhau có thể phân tách cùng một trường điện từ thành các thành phần điện và từ khác nhau.

Từ trường (Magnetic Field / 자기장) được ký hiệu `\vec B`, có đơn vị SI là tesla `T`.

## Lực Lorentz (Lorentz force)

Một điện tích `q` chuyển động với vận tốc `\vec v` trong điện trường `\vec E` và từ trường `\vec B` chịu lực Lorentz:

```math
\vec F=q(\vec E+\vec v\times\vec B)
```

Riêng thành phần lực từ là

```math
\vec F_B=q\vec v\times\vec B
```

với độ lớn

```math
F_B=|q|vB\sin\theta.
```

Lực từ luôn vuông góc với vận tốc khi chỉ có từ trường, vì vậy

```math
\vec F_B\cdot\vec v=0.
```

Do công suất cơ học thỏa `P=\vec F\cdot\vec v`, bản thân lực từ không sinh công lên một điện tích điểm. Nó có thể đổi hướng chuyển động nhưng không trực tiếp làm thay đổi độ lớn vận tốc trong trường hợp lý tưởng.

## Hạt mang điện trong từ trường đều

Nếu `\vec v\perp\vec B`, lực từ đóng vai trò lực hướng tâm:

```math
|q|vB=\frac{mv^2}{r}
```

suy ra

```math
r=\frac{mv}{|q|B}=\frac{p}{|q|B}.
```

Quan hệ này cho thấy bán kính quỹ đạo phụ thuộc động lượng trên điện tích. Máy quang phổ khối (mass spectrometer) dùng độ cong quỹ đạo để suy ra tỉ số khối lượng trên điện tích. Trong các máy va chạm hạt, detector cũng có thể tái dựng động lượng của hạt từ độ cong của vết hạt trong từ trường.

## Lực từ tác dụng lên dây dẫn có dòng điện

Một đoạn dây dẫn có dòng điện chịu lực

```math
\vec F=I\vec L\times\vec B.
```

Ở cấp vi mô, lực này là tổng lực Lorentz tác dụng lên các hạt tải điện đang chuyển động trong dây.

Động cơ điện (electric motor) khai thác lực và mômen lực tác dụng lên các dây dẫn có dòng điện để biến đổi năng lượng điện thành cơ năng.

## Nguồn của từ trường

Dòng điện ổn định tạo ra từ trường. Định luật Biot–Savart (Biot–Savart law) có dạng

```math
d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec\ell\times\hat r}{r^2}.
```

Khi hệ có đối xứng thích hợp, định luật Ampère (Ampère's law) thường thuận tiện hơn:

```math
\oint\vec B\cdot d\vec\ell=\mu_0I_{enc}.
```

Biểu thức trên áp dụng trực tiếp trong từ tĩnh học (magnetostatics). Với điện trường biến thiên theo thời gian, Maxwell bổ sung dòng điện dịch (displacement current), tạo thành định luật Ampère–Maxwell đầy đủ.

## Vì sao các đường sức từ tạo thành vòng kín?

Định luật Gauss cho từ trường (Gauss's law for magnetism) viết

```math
\oint\vec B\cdot d\vec A=0
```

hay ở dạng vi phân

```math
\nabla\cdot\vec B=0.
```

Trong điện từ học cổ điển và trong các quan sát hiện nay, chưa phát hiện đơn cực từ (magnetic monopole) cô lập. Vì vậy các đường sức từ không bắt đầu hay kết thúc tại một “điện tích từ” đơn lẻ mà tạo thành các vòng kín.

## Cảm ứng điện từ Faraday

Từ thông (magnetic flux) qua một mặt được định nghĩa bởi

```math
\Phi_B=\int\vec B\cdot d\vec A.
```

Định luật Faraday (Faraday's law) cho suất điện động cảm ứng:

```math
\mathcal E=-\frac{d\Phi_B}{dt}.
```

Dấu âm thể hiện định luật Lenz (Lenz's law): dòng điện hoặc suất điện động cảm ứng xuất hiện theo chiều chống lại sự biến thiên từ thông đã tạo ra nó. Điều này không có nghĩa hệ “chống lại mọi thay đổi” theo nghĩa chủ ý; đó là hệ quả của cấu trúc điện từ và bảo toàn năng lượng.

Cảm ứng điện từ là nền tảng của máy phát điện (generator), máy biến áp (transformer), sạc cảm ứng (inductive charging), cảm biến và nhiều thiết bị điện hiện đại.

### Vì sao điện trường cảm ứng khác điện trường tĩnh?

Điện trường tĩnh có tính không xoáy:

```math
\nabla\times\vec E=0.
```

Nhưng từ trường biến thiên theo thời gian tạo ra điện trường thỏa

```math
\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}.
```

Điện trường cảm ứng vì thế có tuần hoàn và nói chung không thể được mô tả toàn cục chỉ bằng một điện thế vô hướng đơn trị như trong bài toán điện tĩnh đơn giản.

## Độ tự cảm (inductance)

Cuộn cảm (inductor / 인덕터) chống lại sự biến thiên dòng điện bằng suất điện động cảm ứng. Với một cuộn cảm lý tưởng:

```math
V_L=L\frac{dI}{dt}
```

với dấu cụ thể phụ thuộc quy ước điện áp và chiều dòng điện trong mạch. Về bản chất, định luật Lenz khiến suất điện động cảm ứng chống lại sự thay đổi dòng điện đã tạo ra nó.

Năng lượng lưu trong từ trường của cuộn cảm là

```math
U_B=\frac12LI^2.
```

Mật độ năng lượng từ trong chân không là

```math
u_B=\frac{B^2}{2\mu_0}.
```

## Máy biến áp (transformer)

Dòng điện biến thiên trong cuộn sơ cấp tạo từ thông biến thiên, từ đó cảm ứng suất điện động trong cuộn thứ cấp. Với máy biến áp lý tưởng:

```math
\frac{V_s}{V_p}=\frac{N_s}{N_p}
```

và công suất gần như được bảo toàn:

```math
V_pI_p\approx V_sI_s.
```

Truyền tải điện ở điện áp cao cho phép giảm dòng điện khi truyền cùng một công suất. Vì tổn hao Joule trên đường dây có dạng

```math
P_{loss}=I^2R,
```

việc giảm dòng điện làm giảm mạnh tổn hao nhiệt. Đây là lý do lưới điện sử dụng máy biến áp để nâng điện áp khi truyền tải xa rồi hạ điện áp trước khi phân phối cho người dùng.

## Mô hình tư duy (Mental Model)

Từ trường không trực tiếp sinh công lên một điện tích điểm vì lực từ vuông góc với vận tốc, nhưng nó có thể đổi hướng chuyển động và truyền lực cho dây dẫn, nam châm hay cấu trúc vật chất khác. Cảm ứng điện từ bổ sung nửa còn lại của bức tranh: từ trường biến thiên tạo ra điện trường có tính tuần hoàn.

Vì vậy điện và từ không phải hai chủ đề ghép lại một cách tình cờ. Chúng là hai thành phần liên kết của trường điện từ, và các phương trình Maxwell mô tả cách điện tích, dòng điện, điện trường và từ trường ràng buộc lẫn nhau.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Từ trường làm hạt mang điện chạy nhanh hơn”

Không phải nếu chỉ có từ trường và bỏ qua các tương tác khác. Lực từ vuông góc với vận tốc nên làm đổi hướng động lượng chứ không trực tiếp làm tăng động năng của hạt.

### “Định luật Lenz nói từ trường luôn chống lại từ trường ngoài”

Không chính xác. Hệ cảm ứng chống lại **sự biến thiên từ thông**, không đơn giản chống lại giá trị tức thời của từ trường ngoài.

### “Máy biến áp tạo thêm năng lượng khi tăng điện áp”

Không. Máy biến áp lý tưởng tăng điện áp bằng cách giảm dòng điện tương ứng để công suất đầu vào và đầu ra gần bằng nhau. Máy thực còn có thêm tổn hao.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Điện tĩnh học](00_electrostatics.md).

**Liên hệ tiếp:** [Các phương trình Maxwell và sóng điện từ](04_maxwell_em_waves.md).
