# Công, năng lượng, thế năng và công suất

## Tại sao cần năng lượng nếu đã có lực và gia tốc?

Newton II cho phép ta mô tả chuyển động bằng lực và gia tốc. Nhưng với nhiều hệ, theo dõi mọi vector lực theo từng thời điểm là cách giải dài và che mất cấu trúc. Năng lượng (Energy / 에너지) cung cấp một cách nhìn khác: thay vì theo dõi “chuyển động thay đổi từng giây thế nào”, ta theo dõi khả năng hệ chuyển đổi trạng thái và một đại lượng có thể được truyền, tích trữ hoặc chuyển dạng.

Năng lượng không phải một “chất lỏng vô hình”. Nó là một đại lượng trạng thái hoặc đại lượng gắn với hệ, được định nghĩa sao cho các định luật bảo toàn tạo ra constraint rất mạnh cho quá trình vật lý.

Đơn vị năng lượng là joule:

```math
1\,J=1\,N\cdot m=1\,kg\cdot m^2/s^2
```

## Công: lực truyền năng lượng qua độ dời

Công (Work / 일) của một lực không đổi khi vật dịch chuyển `\Delta \vec r`:

```math
W=\vec F\cdot\Delta\vec r
=F\Delta r\cos\theta
```

Tích vô hướng xuất hiện vì chỉ thành phần lực song song displacement mới làm công theo định nghĩa cơ học này.

Nếu ta xách một vali đi ngang với tốc độ không đổi, tay tạo lực chủ yếu hướng lên còn displacement hướng ngang. Trong idealized model:

```math
W_{hand}=0
```

Điều này không có nghĩa cơ bắp không tiêu hao năng lượng sinh học; nó chỉ nói mechanical work của lực ngoài tác dụng lên center of mass của vali theo hướng dịch chuyển bằng zero. Sinh học cơ bắp có quá trình hóa học và nội lực phức tạp hơn.

### Lực thay đổi theo vị trí

Nếu lực thay đổi:

```math
W=\int_{\vec r_1}^{\vec r_2}\vec F\cdot d\vec r
```

Tích phân cộng tất cả đóng góp vi phân:

```math
dW=\vec F\cdot d\vec r
```

Đây là ví dụ rõ ràng về việc calculus được sinh ra bởi cấu trúc vật lý: khi tác động thay đổi liên tục, tổng finite cần tích phân.

## Động năng và định lý công–động năng

Động năng (Kinetic Energy / 운동에너지) của vật khối lượng `m`, speed `v` trong cơ học Newton:

```math
K=\frac12mv^2
```

Tại sao có `v²` và `1/2`?

Từ Newton II trong một chiều:

```math
F=ma=m\frac{dv}{dt}
```

Vì:

```math
v=\frac{dx}{dt}
```

nên:

```math
a=\frac{dv}{dt}=\frac{dv}{dx}\frac{dx}{dt}=v\frac{dv}{dx}
```

Do đó:

```math
F=m v\frac{dv}{dx}
```

Nhân `dx`:

```math
F\,dx=mv\,dv
```

Tích phân từ trạng thái đầu đến cuối:

```math
\int F\,dx=\int_{v_1}^{v_2}mv\,dv
```

```math
W=\frac12mv_2^2-\frac12mv_1^2
```

Vậy:

```math
W_{net}=\Delta K
```

Định lý công–động năng (Work–Energy Theorem / 일-에너지 정리) không phải một luật tách rời; nó được suy ra từ Newton II dưới các giả định cơ học cổ điển.

### Tại sao tốc độ gấp đôi tạo động năng gấp bốn?

Vì:

```math
K\propto v^2
```

Nếu xe chạy nhanh gấp đôi, để dừng xe cần loại bỏ bốn lần động năng. Điều này nối trực tiếp với quãng đường phanh tăng theo `v²` nếu lực phanh gần như không đổi.

## Thế năng và lực bảo toàn

Một lực bảo toàn (Conservative Force / 보존력) là lực mà công giữa hai điểm chỉ phụ thuộc điểm đầu và cuối, không phụ thuộc đường đi. Ta có thể định nghĩa thế năng (Potential Energy / 위치에너지):

```math
\Delta U=-W_{conservative}
```

Dấu âm nghĩa là khi lực bảo toàn làm công dương, thế năng giảm.

Trong một chiều:

```math
F_x=-\frac{dU}{dx}
```

Công thức này rất sâu: lực là “độ dốc âm” của landscape thế năng. Hệ có xu hướng accelerate về phía thế năng giảm.

Trong nhiều chiều:

```math
\vec F=-\nabla U
```

Gradient (Gradient / 그래디언트) chỉ hướng tăng nhanh nhất của scalar field `U`; dấu âm khiến force hướng về giảm nhanh nhất. Đây là connection trực tiếp sang Machine Learning: gradient descent cũng đi theo `-\nabla L` để giảm loss function, dù “loss” không phải physical energy.

## Thế năng hấp dẫn gần mặt đất

Với gravity gần mặt đất, `F_y=-mg`. Ta muốn `F_y=-dU/dy`, nên:

```math
\frac{dU}{dy}=mg
```

Tích phân:

```math
U=mgy+C
```

Ta thường chọn mốc để `C=0`:

```math
U=mgh
```

Giá trị tuyệt đối của thế năng phụ thuộc mốc; chênh lệch mới có ý nghĩa động lực học.

## Thế năng lò xo

Hooke:

```math
F=-kx
```

và:

```math
F=-\frac{dU}{dx}
```

nên:

```math
\frac{dU}{dx}=kx
```

Tích phân:

```math
U(x)=\frac12kx^2+C
```

Chọn `U(0)=0`:

```math
U=\frac12kx^2
```

Dạng parabola này sẽ dẫn tự nhiên tới dao động điều hòa.

## Bảo toàn cơ năng

Nếu chỉ có lực bảo toàn làm công:

```math
E_{mech}=K+U=constant
```

Hay:

```math
K_1+U_1=K_2+U_2
```

Ví dụ vật rơi từ độ cao `h`, bắt đầu nghỉ:

```math
mgh=\frac12mv^2
```

Khối lượng triệt tiêu:

```math
v=\sqrt{2gh}
```

Kết quả trùng với kinematics, nhưng energy method không cần tính thời gian.

## Lực không bảo toàn và “mất năng lượng”

Khi có ma sát, mechanical energy giảm:

```math
\Delta(K+U)=W_{nonconservative}
```

Nhưng tổng năng lượng của hệ rộng hơn không biến mất. Mechanical energy chuyển thành internal energy, nhiệt, âm, deformation hoặc các dạng khác.

Cụm từ “năng lượng bị mất” thường chỉ nghĩa “năng lượng rời khỏi dạng mà ta đang theo dõi”. Conservation of energy nói tổng năng lượng của một hệ cô lập không tự sinh ra hay biến mất.

## Công suất

Công suất (Power / 일률, 전력 trong context điện) là tốc độ truyền hoặc chuyển đổi năng lượng:

```math
P=\frac{dW}{dt}
```

Đơn vị watt:

```math
1\,W=1\,J/s
```

Nếu lực và velocity:

```math
P=\vec F\cdot\vec v
```

Một động cơ 100 kW không nhất thiết có tổng năng lượng nhiều hơn một động cơ 50 kW; nó có khả năng chuyển năng lượng nhanh hơn.

Trong computing, power consumption cũng là energy per time. Một CPU dùng 100 W tiêu thụ 100 J mỗi giây ở mức công suất đó. Nhiệt sinh ra, battery life và thermal throttling đều liên quan tới energy conversion rate.

## Efficiency

Hiệu suất (Efficiency / 효율):

```math
\eta=\frac{E_{useful}}{E_{input}}
```

hoặc với steady process:

```math
\eta=\frac{P_{useful}}{P_{input}}
```

`\eta<1` trong máy thực vì energy phân tán thành nhiệt, âm, friction, electrical loss… nhưng energy total vẫn được bảo toàn.

## Potential well và equilibrium

Nếu `U(x)` có minimum tại `x_0`, thì:

```math
\left.\frac{dU}{dx}\right|_{x_0}=0
```

và force bằng zero. Nếu curvature dương:

```math
\left.\frac{d^2U}{dx^2}\right|_{x_0}>0
```

đó là equilibrium ổn định. Gần minimum, nhiều thế năng smooth có thể xấp xỉ bằng parabola Taylor:

```math
U(x)\approx U(x_0)+\frac12k(x-x_0)^2
```

Đây là lý do harmonic oscillator xuất hiện ở rất nhiều hệ vật lý: bất kỳ stable equilibrium smooth nào, khi perturbation nhỏ, thường có behavior gần lò xo.

## Bài toán mẫu: tàu lượn

Một xe tàu lượn bắt đầu nghỉ ở độ cao `20 m`, bỏ qua friction. Hỏi speed ở độ cao `5 m`.

Chọn mốc thế năng tùy ý. Conservation:

```math
m g(20)=\frac12mv^2+mg(5)
```

```math
mg(15)=\frac12mv^2
```

```math
v=\sqrt{2g(15)}\approx17.1\,m/s
```

Không cần biết hình dạng đường ray. Đây là sức mạnh của conservative force: path information được nén vào potential difference.

## Mental Model

> Force view hỏi “tại mỗi khoảnh khắc, tương tác đang bẻ trajectory thế nào?”. Energy view hỏi “hệ có thể chuyển từ trạng thái này sang trạng thái kia hay không, và lượng khả năng chuyển đổi được phân phối giữa những dạng nào?”. Hai view không cạnh tranh; chúng là hai phép chiếu của cùng dynamics.

## Common Misconceptions

### “Năng lượng là lực”

Không. Force có đơn vị N và là vector; energy có đơn vị J và thường là scalar. Force liên hệ với gradient của potential energy.

### “Công bằng lực nhân quãng đường trong mọi trường hợp”

Chỉ khi force cùng hướng displacement và constant. Dạng tổng quát là dot product và tích phân đường.

## Knowledge Connection

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Nhiệt động lực học](../04_thermal_statistical/00_thermodynamics.md).
