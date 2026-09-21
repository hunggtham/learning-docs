# Các phương trình Maxwell, sóng điện từ và dòng năng lượng

Maxwell hợp nhất điện học, từ học và quang học thành một lý thuyết trường duy nhất. Bốn phương trình không chỉ mô tả “điện trường và từ trường tồn tại như thế nào”; chúng còn cho biết trường biến thiên tự tạo lẫn nhau ra sao, tại sao sóng điện từ lan truyền được trong chân không và vì sao ánh sáng là một nghiệm của điện từ học.

## Bốn phương trình Maxwell

Trong chân không có mật độ điện tích `\rho` và mật độ dòng `\mathbf J`, dạng vi phân là

```math
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0},
```

```math
\nabla\cdot\mathbf B=0,
```

```math
\nabla\times\mathbf E
=-\frac{\partial\mathbf B}{\partial t},
```

```math
\nabla\times\mathbf B
=\mu_0\mathbf J
+\mu_0\varepsilon_0
\frac{\partial\mathbf E}{\partial t}.
```

Mỗi phương trình có một vai trò riêng.

## Gauss cho điện trường

```math
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0}.
```

Mật độ điện tích là nguồn của divergence điện trường. Ở dạng tích phân,

```math
\oint_S\mathbf E\cdot d\mathbf A
=
\frac{Q_{enc}}{\varepsilon_0}.
```

Nó nối nguồn điện tích bên trong một mặt kín với tổng thông lượng điện qua mặt đó.

## Gauss cho từ trường

```math
\nabla\cdot\mathbf B=0.
```

Tổng thông lượng từ qua mọi mặt kín bằng không:

```math
\oint_S\mathbf B\cdot d\mathbf A=0.
```

Trong điện từ học cổ điển, điều này phản ánh việc chưa quan sát thấy đơn cực từ tự do. Đường sức từ không bắt đầu hoặc kết thúc ở một điện tích từ riêng lẻ; chúng tạo các vòng kín hoặc kéo dài vô hạn.

## Định luật Faraday

```math
\nabla\times\mathbf E
=-\frac{\partial\mathbf B}{\partial t}.
```

Dạng tích phân là

```math
\oint_C\mathbf E\cdot d\mathbf l
=-\frac{d\Phi_B}{dt}.
```

Một từ thông biến thiên tạo điện trường xoáy. Đây là cơ sở của máy phát điện, máy biến áp và cảm ứng điện từ.

Điểm quan trọng là điện trường cảm ứng này không nhất thiết có điện thế vô hướng toàn cục đơn giản như trong điện tĩnh, vì

```math
\nabla\times\mathbf E\neq0.
```

## Ampère–Maxwell

Ampère ban đầu cho rằng dòng điện tạo từ trường:

```math
\nabla\times\mathbf B
=\mu_0\mathbf J.
```

Nhưng biểu thức này gặp vấn đề với tụ điện đang nạp. Dòng dẫn đi trong dây nhưng không chạy xuyên qua lớp điện môi giữa hai bản.

Maxwell bổ sung hạng dòng dịch:

```math
\mu_0\varepsilon_0
\frac{\partial\mathbf E}{\partial t}.
```

Phương trình đầy đủ là

```math
\nabla\times\mathbf B
=
\mu_0\mathbf J
+
\mu_0\varepsilon_0
\frac{\partial\mathbf E}{\partial t}.
```

Một điện trường biến thiên cũng tạo từ trường xoáy.

## Vì sao hạng dòng dịch là cần thiết?

Lấy divergence hai vế:

```math
\nabla\cdot(\nabla\times\mathbf B)=0.
```

Do đó

```math
0
=
\mu_0\nabla\cdot\mathbf J
+
\mu_0\varepsilon_0
\frac{\partial}{\partial t}
(\nabla\cdot\mathbf E).
```

Dùng định luật Gauss,

```math
\nabla\cdot\mathbf E=\frac{\rho}{\varepsilon_0},
```

ta được

```math
\frac{\partial\rho}{\partial t}
+\nabla\cdot\mathbf J=0.
```

Đó chính là phương trình bảo toàn điện tích.

Hạng dòng dịch vì vậy không phải “mẹo sửa công thức”; nó làm hệ Maxwell tương thích với bảo toàn điện tích.

## Từ Maxwell tới phương trình sóng

Trong chân không không có nguồn,

```math
\rho=0,
\qquad
\mathbf J=0.
```

Ta có

```math
\nabla\cdot\mathbf E=0,
```

```math
\nabla\times\mathbf E
=-\frac{\partial\mathbf B}{\partial t},
```

```math
\nabla\times\mathbf B
=\mu_0\varepsilon_0
\frac{\partial\mathbf E}{\partial t}.
```

Lấy curl của phương trình Faraday:

```math
\nabla\times(\nabla\times\mathbf E)
=-\frac{\partial}{\partial t}
(\nabla\times\mathbf B).
```

Dùng đồng nhất thức vectơ

```math
\nabla\times(\nabla\times\mathbf E)
=
\nabla(\nabla\cdot\mathbf E)
-\nabla^2\mathbf E,
```

và `\nabla\cdot\mathbf E=0`, ta được

```math
\nabla^2\mathbf E
=
\mu_0\varepsilon_0
\frac{\partial^2\mathbf E}{\partial t^2}.
```

Tương tự,

```math
\nabla^2\mathbf B
=
\mu_0\varepsilon_0
\frac{\partial^2\mathbf B}{\partial t^2}.
```

So với phương trình sóng chuẩn

```math
\nabla^2\psi
=
\frac{1}{v^2}
\frac{\partial^2\psi}{\partial t^2},
```

suy ra

```math
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}.
```

Giá trị này trùng tốc độ ánh sáng. Đây là bước hợp nhất lịch sử: ánh sáng là sóng điện từ.

## Sóng phẳng

Một sóng điện từ phẳng truyền theo `+z` có thể viết

```math
\mathbf E(z,t)
=E_0\hat{\mathbf x}
\cos(kz-\omega t),
```

```math
\mathbf B(z,t)
=B_0\hat{\mathbf y}
\cos(kz-\omega t).
```

Trong chân không,

```math
B_0=\frac{E_0}{c}.
```

Ba hướng

```text
E-field
B-field
propagation direction
```

vuông góc lẫn nhau.

Sóng điện từ trong chân không là sóng ngang.

## Quan hệ tần số và bước sóng

Trong chân không,

```math
c=f\lambda,
```

hoặc

```math
\omega=ck.
```

Quan hệ tuyến tính `\omega(k)` cho biết vận tốc pha và vận tốc nhóm đều bằng `c` trong chân không lý tưởng.

Trong vật liệu phân tán, `\omega(k)` không còn tuyến tính và vận tốc pha, vận tốc nhóm có thể khác nhau.

## Phân cực

Hướng dao động của điện trường xác định phân cực của sóng.

Nếu `\mathbf E` luôn nằm theo một đường thẳng, ta có phân cực tuyến tính. Nếu hai thành phần vuông góc có cùng biên độ và lệch pha `\pi/2`, đầu vectơ `\mathbf E` quay theo vòng tròn và tạo phân cực tròn.

Phân cực không phải “hướng photon quay như vật thể cổ điển”; nó là cấu trúc của trường điện từ và, trong mô tả lượng tử, liên hệ với trạng thái spin/helicity của photon.

## Phổ điện từ

Radio, microwave, hồng ngoại, ánh sáng nhìn thấy, tử ngoại, tia X và gamma đều là các vùng khác nhau của cùng phổ điện từ.

Chúng khác chủ yếu ở tần số và bước sóng:

```math
c=f\lambda.
```

Khi mô tả lượng tử cần thiết, photon có năng lượng

```math
E=hf.
```

Vì vậy tần số cao hơn tương ứng photon năng lượng lớn hơn.

Sự khác biệt trong cách các dải phổ tương tác với vật chất đến từ năng lượng photon, kích thước cấu trúc vật chất và các mức chuyển năng lượng cho phép.

## Năng lượng của trường điện từ

Trong chân không, mật độ năng lượng là

```math
u
=
\frac12\varepsilon_0E^2
+
\frac{1}{2\mu_0}B^2.
```

Với sóng phẳng,

```math
E=cB,
```

nên năng lượng điện và từ đóng góp bằng nhau theo trung bình.

## Vectơ Poynting

Dòng năng lượng điện từ được mô tả bởi vectơ Poynting

```math
\mathbf S
=
\frac{1}{\mu_0}
\mathbf E\times\mathbf B.
```

Đơn vị là công suất trên diện tích:

```math
W/m^2.
```

`\mathbf S` chỉ hướng năng lượng lan truyền.

Với sóng điều hòa phẳng, cường độ trung bình là

```math
\langle S\rangle
=\frac12c\varepsilon_0E_0^2.
```

Cường độ tỉ lệ bình phương biên độ trường.

## Định lý Poynting

Bảo toàn năng lượng điện từ có dạng

```math
\frac{\partial u}{\partial t}
+\nabla\cdot\mathbf S
=-\mathbf J\cdot\mathbf E.
```

Ý nghĩa:

- `\partial u/\partial t`: thay đổi năng lượng lưu trong trường;
- `\nabla\cdot\mathbf S`: năng lượng rời khỏi một vùng;
- `\mathbf J\cdot\mathbf E`: tốc độ trường làm công lên vật chất.

Đây là phiên bản điện từ của cấu trúc conservation law chung.

## Năng lượng đi trong mạch ở đâu?

Trong mô hình mạch, ta thường nói pin “gửi năng lượng qua dây” tới điện trở. Ở mức trường, năng lượng được mang bởi trường điện từ trong không gian quanh dây và đi vào điện trở theo vectơ Poynting.

Điều này không làm mô hình mạch sai; nó cho thấy mô hình mạch là một trừu tượng hóa nén trường thành `V`, `I`, `R`.

## Áp suất bức xạ

Sóng điện từ mang động lượng. Khi bị hấp thụ hoặc phản xạ, nó có thể truyền động lượng cho vật.

Với hấp thụ hoàn toàn, áp suất bức xạ trung bình gần

```math
P_{rad}=\frac{I}{c}.
```

Với phản xạ hoàn toàn vuông góc,

```math
P_{rad}=\frac{2I}{c}.
```

Áp suất bức xạ nhỏ trong đời sống nhưng quan trọng trong vật lý laser, buồm Mặt Trời và động lực học bụi thiên văn.

## Bức xạ từ điện tích gia tốc

Điện tích chuyển động đều không nhất thiết phát bức xạ trong mọi hệ quy chiếu quán tính. Nhưng điện tích gia tốc có thể tạo nhiễu động trường lan ra xa dưới dạng bức xạ.

Ở giới hạn không tương đối tính, công suất Larmor có dạng

```math
P
=
\frac{q^2a^2}
{6\pi\varepsilon_0c^3}.
```

Bức xạ vì vậy gắn với gia tốc của nguồn.

Đây là cơ sở của anten, synchrotron radiation và nhiều quá trình bức xạ thiên văn.

## Anten phát sóng như thế nào?

Dòng điện xoay chiều trong anten làm điện tích gia tốc qua lại. Trường gần nguồn thay đổi theo thời gian và một phần trường tách ra thành sóng lan truyền ra xa.

Ở vùng xa, điện trường và từ trường giảm gần như `1/r`, nên mật độ năng lượng giảm như `1/r^2`.

Hình dạng và kích thước anten quyết định pattern bức xạ và mức ghép với các mode trường.

## Near field và far field

Gần anten, trường có các thành phần phản ứng (reactive) lưu năng lượng tạm thời quanh nguồn và có phụ thuộc khoảng cách nhanh hơn `1/r`.

Xa nguồn, thành phần bức xạ `1/r` chi phối và năng lượng chảy ròng ra ngoài.

Do đó không nên dùng trực giác sóng phẳng far-field ngay sát anten.

## Sóng trong vật liệu

Trong môi trường tuyến tính đơn giản,

```math
v=\frac{1}{\sqrt{\mu\varepsilon}}.
```

Chiết suất là

```math
n=\frac{c}{v}.
```

Vật liệu thật thường có `\varepsilon` phụ thuộc tần số, gây dispersion. Nếu có tổn hao, `\varepsilon` có thể phức và sóng bị suy giảm khi lan truyền.

Đây là cầu nối tới quang học, điện môi và đường truyền.

## Maxwell và thuyết tương đối

Các phương trình Maxwell dự đoán một tốc độ sóng `c` không phụ thuộc chuyển động của nguồn theo cách cơ học Newton đơn giản mong đợi.

Sự bất biến của tốc độ ánh sáng là một trong những động lực lịch sử dẫn tới thuyết tương đối hẹp. Trong ngôn ngữ tương đối tính, `\mathbf E` và `\mathbf B` không phải hai thực thể hoàn toàn tách biệt; chúng là các thành phần khác nhau của cùng tensor điện từ.

## Mô hình tư duy (Mental Model)

Maxwell nối ba ý tưởng lớn:

```text
nguồn điện tích/dòng điện
↕
trường E và B động
↕
sóng mang năng lượng và động lượng
```

Điện trường biến thiên tạo từ trường; từ trường biến thiên tạo điện trường. Trong chân không, cấu trúc này tự duy trì và lan truyền như sóng với tốc độ `c`.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Sóng điện từ cần ether hoặc môi trường vật chất”

Không. Maxwell cho phép nghiệm sóng trong chân không.

### “Điện trường tạo từ trường và từ trường tạo điện trường nên sóng tự tăng năng lượng vô hạn”

Không. Năng lượng được xác định bởi điều kiện ban đầu hoặc nguồn; trường trao đổi cấu trúc trong khi tổng năng lượng tuân theo định lý Poynting.

### “Mọi trường biến thiên đều là bức xạ”

Không. Gần nguồn có thành phần near-field lưu trữ năng lượng và không mang công suất ròng ra vô hạn như thành phần bức xạ.

### “Từ trường luôn làm công lên điện tích”

Lực từ `q\mathbf v\times\mathbf B` vuông góc vận tốc tức thời nên không trực tiếp đổi động năng của một hạt điểm. Điện trường mới trực tiếp thực hiện công `q\mathbf E\cdot\mathbf v`.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Điện tĩnh học](00_electrostatics.md), [Từ trường và cảm ứng](03_magnetism_induction.md), [Ngôn ngữ Toán học](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Quang học sóng](../06_optics/01_wave_optics.md), [Quang học Fourier](../06_optics/04_fourier_imaging_instrumentation.md), [Đường truyền và ống dẫn sóng](05_transmission_lines_waveguides.md), [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md).
