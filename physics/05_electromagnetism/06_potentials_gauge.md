# Thế điện từ, tự do chuẩn và hiệu ứng Aharonov–Bohm

Trong điện tĩnh, điện trường có thể được mô tả hoàn toàn bằng điện thế vô hướng. Khi trường thay đổi theo thời gian, mô tả đó không còn đủ. Ta cần cả **điện thế vô hướng (scalar potential)** `\phi` và **thế vectơ (vector potential)** `\mathbf A`.

Điểm quan trọng của chương này không phải học thêm hai ký hiệu. Nó là bước chuyển từ cách nhìn “trường là đại lượng duy nhất có ý nghĩa” sang một cấu trúc sâu hơn: nhiều bộ thế khác nhau có thể mô tả cùng một trường vật lý. Sự dư thừa có cấu trúc đó gọi là **tự do chuẩn (gauge freedom / 게이지 자유도)**.

## Từ phương trình Maxwell tới các thế

Một trong các phương trình Maxwell là

```math
\nabla\cdot\mathbf B=0.
```

Một trường vectơ có divergence bằng không có thể được viết cục bộ dưới dạng curl của một trường vectơ khác:

```math
\mathbf B=\nabla\times\mathbf A.
```

Đây là lý do thế vectơ `\mathbf A` xuất hiện.

Thay biểu thức này vào định luật Faraday,

```math
\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},
```

thu được

```math
\nabla\times\left(
\mathbf E+\frac{\partial\mathbf A}{\partial t}
\right)=0.
```

Một trường có curl bằng không có thể viết dưới dạng gradient của một vô hướng. Do đó

```math
\mathbf E=-\nabla\phi-\frac{\partial\mathbf A}{\partial t}.
```

Hai công thức

```math
\mathbf B=\nabla\times\mathbf A,
```

```math
\mathbf E=-\nabla\phi-\frac{\partial\mathbf A}{\partial t}
```

không phải định nghĩa tùy ý. Chúng được chọn sao cho hai phương trình Maxwell đồng nhất được thỏa tự động.

## Vì sao các thế không duy nhất?

Giả sử ta thay

```math
\mathbf A' = \mathbf A+\nabla\chi,
```

và

```math
\phi'=\phi-\frac{\partial\chi}{\partial t},
```

với `\chi(\mathbf r,t)` là một hàm đủ trơn. Khi đó

```math
\nabla\times\mathbf A'
=
\nabla\times\mathbf A
+
\nabla\times\nabla\chi
=
\mathbf B,
```

vì curl của gradient bằng không.

Tương tự,

```math
-\nabla\phi'-\frac{\partial\mathbf A'}{\partial t}
=
-\nabla\phi-\frac{\partial\mathbf A}{\partial t},
```

nên `\mathbf E` cũng không đổi.

Đây là **biến đổi chuẩn (gauge transformation / 게이지 변환)**. Nhiều cặp `(\phi,\mathbf A)` khác nhau biểu diễn cùng một cấu hình trường vật lý.

## Tự do chuẩn không phải sự mơ hồ của Vật lý

Nếu hai mô tả khác nhau nhưng mọi đại lượng quan sát được đều giống nhau, sự khác biệt giữa chúng không phải một khác biệt vật lý độc lập. Nó là **dư thừa của cách biểu diễn (representational redundancy)**.

Điều này tương tự việc mô tả cùng một điểm bằng các hệ tọa độ khác nhau, nhưng phép so sánh chỉ mang tính gợi ý. Đối xứng chuẩn có cấu trúc toán học chính xác hơn một phép đổi tọa độ đơn giản.

Bài học tổng quát là: không phải mọi biến xuất hiện trong phương trình đều tương ứng một bậc tự do quan sát độc lập.

## Chuẩn Coulomb và chuẩn Lorenz

Vì thế không duy nhất, ta có thể áp thêm một điều kiện để chọn đại diện thuận tiện.

Chuẩn Coulomb (Coulomb gauge) đặt

```math
\nabla\cdot\mathbf A=0.
```

Chuẩn này thường hữu ích trong các bài gần điện tĩnh hoặc trong một số mô tả bức xạ.

Chuẩn Lorenz (Lorenz gauge) đặt

```math
\nabla\cdot\mathbf A+
\frac{1}{c^2}\frac{\partial\phi}{\partial t}=0.
```

Tên đúng là **Lorenz**, không phải Lorentz. Trong chuẩn này, phương trình cho `\phi` và `\mathbf A` có dạng đối xứng giống phương trình sóng:

```math
\Box\phi=-\frac{\rho}{\varepsilon_0},
```

```math
\Box\mathbf A=-\mu_0\mathbf J,
```

với toán tử d'Alembert

```math
\Box=\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}.
```

Cấu trúc này làm tính tương đối tính của điện từ học rõ hơn.

## Thế trễ và tốc độ truyền hữu hạn

Nghiệm của phương trình sóng không phụ thuộc tức thời vào nguồn hiện tại ở mọi nơi. Trường tại vị trí `\mathbf r` và thời điểm `t` phụ thuộc vào nguồn tại **thời gian trễ (retarded time)**

```math
t_r=t-\frac{|\mathbf r-\mathbf r'|}{c}.
```

Về mặt vật lý, thay đổi của điện tích hoặc dòng điện cần thời gian để ảnh hưởng tới vùng khác. Đây là cách nhân quả và tốc độ ánh sáng được mã hóa vào thế điện từ.

Nó cũng cho thấy hình ảnh “điện tích hiện tại quyết định tức thời trường ở mọi nơi” chỉ đúng trong xấp xỉ gần tĩnh.

## Từ thế tới Lagrangian của hạt tích điện

Một hạt điện tích `q` và khối lượng `m` chuyển động trong trường điện từ có thể được mô tả bằng Lagrangian

```math
L=
\frac12m v^2
+q\mathbf v\cdot\mathbf A
-q\phi.
```

Khi áp dụng phương trình Euler–Lagrange, ta thu được lực Lorentz

```math
m\frac{d\mathbf v}{dt}
=q(\mathbf E+\mathbf v\times\mathbf B).
```

Điều này rất quan trọng về mặt cấu trúc: các thế không chỉ là mẹo để tính `E` và `B`. Chúng xuất hiện tự nhiên trong cơ học giải tích.

Động lượng chính tắc là

```math
\mathbf p_{canonical}=m\mathbf v+q\mathbf A,
```

khác động lượng cơ học `m\mathbf v`. Phân biệt này trở nên đặc biệt quan trọng trong cơ học lượng tử và lý thuyết trường.

## Hiệu ứng Aharonov–Bohm

Trong cơ học lượng tử, pha của hàm sóng hạt tích điện có thể nhận đóng góp

```math
\Delta\varphi
=
\frac{q}{\hbar}
\oint\mathbf A\cdot d\mathbf l.
```

Theo định lý Stokes,

```math
\oint\mathbf A\cdot d\mathbf l
=
\int\mathbf B\cdot d\mathbf S
=
\Phi_B.
```

Do đó

```math
\Delta\varphi=\frac{q\Phi_B}{\hbar}.
```

Trong bố trí Aharonov–Bohm, hạt có thể đi qua vùng mà từ trường cục bộ gần bằng không nhưng vẫn tạo dịch chuyển vân giao thoa phụ thuộc từ thông bị bao quanh.

Điều này không có nghĩa `\mathbf A` tại một điểm đơn lẻ trở thành đại lượng quan sát tuyệt đối. Đại lượng đo được vẫn là tổ hợp chuẩn-bất biến liên hệ với pha quanh một vòng kín hoặc từ thông tổng.

## Cấu trúc topo xuất hiện ở đâu?

Hiệu ứng Aharonov–Bohm cho thấy hai vùng có cùng trường cục bộ `\mathbf B=0` vẫn có thể khác nhau về cấu trúc toàn cục nếu topology của miền không đơn liên (not simply connected).

Đây là một bước quan trọng từ Vật lý trường cổ điển sang tư duy topo: thông tin vật lý không phải lúc nào cũng được xác định hoàn toàn bởi các đại lượng cục bộ tại một điểm.

## Từ `U(1)` tới đối xứng chuẩn trong Vật lý hạt

Trong cơ học lượng tử, biến đổi pha cục bộ

```math
\psi(x)\rightarrow e^{iq\chi(x)/\hbar}\psi(x)
```

làm đạo hàm thông thường của `\psi` thay đổi theo cách không còn bất biến. Để xây lý thuyết bất biến dưới biến đổi pha cục bộ, ta đưa vào đạo hàm hiệp biến (covariant derivative)

```math
D_\mu=\partial_\mu+\frac{iq}{\hbar}A_\mu.
```

Trường điện từ xuất hiện như trường chuẩn cần thiết để duy trì đối xứng cục bộ `U(1)`.

Đây là nguyên mẫu cho cách Mô hình Chuẩn dùng các nhóm chuẩn phức tạp hơn như `SU(2)` và `SU(3)`. Tuy nhiên ở mức này, mục tiêu chỉ là thấy logic: **yêu cầu đối xứng cục bộ dẫn tới cấu trúc tương tác**.

## Khi nào nên dùng `E,B`, khi nào nên dùng `\phi,A`?

Nếu bài toán là lực cổ điển trên hạt hoặc năng lượng dòng trường, `E` và `B` thường trực quan hơn. Nếu bài toán liên quan phương trình sóng, bức xạ, cơ học giải tích, lượng tử hoặc đối xứng chuẩn, `\phi` và `\mathbf A` thường là cách biểu diễn tự nhiên hơn.

Không có một biểu diễn “thật” duy nhất phải dùng cho mọi bài toán. Chọn biến tốt là một phần của tư duy vật lý.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Thế không duy nhất nên thế không có ý nghĩa vật lý”

Không đúng. Giá trị của một đại diện chuẩn riêng lẻ không phải đại lượng quan sát tuyệt đối, nhưng các tổ hợp chuẩn-bất biến xây từ thế có hệ quả vật lý đo được.

### “Hiệu ứng Aharonov–Bohm chứng minh `A` tại từng điểm là quan sát được trực tiếp”

Không. Hiệu ứng đo pha toàn cục phụ thuộc vòng tích phân hoặc từ thông, không đo một giá trị `\mathbf A` tuyệt đối tại một điểm.

### “Chọn gauge khác nhau nghĩa là chọn vật lý khác nhau”

Không. Gauge khác nhau mô tả cùng cấu hình vật lý nếu liên hệ bởi biến đổi chuẩn hợp lệ.

## Mô hình tư duy (Mental Model)

Trường `\mathbf E` và `\mathbf B` mô tả cường độ điện từ cục bộ. Các thế `\phi` và `\mathbf A` tổ chức cấu trúc trường ở mức sâu hơn, đặc biệt khi có thời gian, lượng tử và topology. Tự do chuẩn nhắc rằng một lý thuyết có thể chứa dư thừa biểu diễn nhưng vẫn có nội dung vật lý hoàn toàn xác định.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Phương trình Maxwell và sóng điện từ](04_maxwell_em_waves.md), [Ngôn ngữ toán học](../00_foundations/03_mathematical_language.md), [Cơ học giải tích](../01_mechanics/08_analytical_mechanics.md).

**Liên hệ tiếp:** [Nền tảng lượng tử](../08_quantum/00_quantum_foundations.md), [Mô hình Chuẩn](../09_atomic_nuclear_particle/03_particle_standard_model.md).
