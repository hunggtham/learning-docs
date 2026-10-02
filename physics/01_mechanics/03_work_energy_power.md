# Công, năng lượng, thế năng và công suất

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Công, năng lượng, thế năng và công suất**. Route đi từ force/displacement → work-energy theorem → potential/conservation → nonconservative losses → power/rate, để năng lượng đổi góc nhìn nhưng giữ cùng động lực học.

## Tại sao cần năng lượng nếu đã có lực và gia tốc?

Newton II cho phép ta mô tả chuyển động bằng lực và gia tốc. Nhưng với nhiều hệ, theo dõi mọi vectơ (vector) lực theo từng thời điểm là cách giải dài và che mất cấu trúc. Năng lượng (Energy / 에너지) cung cấp một cách nhìn khác: thay vì theo dõi “chuyển động thay đổi từng giây thế nào”, ta theo dõi khả năng hệ chuyển đổi trạng thái và một đại lượng có thể được truyền, tích trữ hoặc chuyển dạng.

Năng lượng không phải một “chất lỏng vô hình”. Nó là một đại lượng trạng thái hoặc đại lượng gắn với hệ, được định nghĩa sao cho các định luật bảo toàn tạo ra ràng buộc (constraint / 제약조건) rất mạnh cho quá trình vật lý.

Đơn vị năng lượng là joule:

```math
1\,J=1\,N\cdot m=1\,kg\cdot m^2/s^2
```

> **Chuyển mạch:** Trong **Công, năng lượng, thế năng và công suất**, **Công: lực truyền năng lượng qua độ dời** tiếp nhận điểm tựa từ **Tại sao cần năng lượng nếu đã có lực và gia tốc?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động năng và định lý công–động năng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Công: lực truyền năng lượng qua độ dời

Công (Work / 일) của một lực không đổi khi vật dịch chuyển `\Delta \vec r`:

```math
W=\vec F\cdot\Delta\vec r
=F\Delta r\cos\theta
```

Tích vô hướng xuất hiện vì chỉ thành phần lực song song độ dịch chuyển (displacement) mới làm công theo định nghĩa cơ học này.

Nếu ta xách một vali đi ngang với tốc độ không đổi, tay tạo lực chủ yếu hướng lên còn độ dịch chuyển hướng ngang. Trong idealized mô hình (model / 모델):

```math
W_{hand}=0
```

Điều này không có nghĩa cơ bắp không tiêu hao năng lượng sinh học; nó chỉ nói mechanical công việc (work / 작업) của lực ngoài tác dụng lên tâm khối (center of mass) của vali theo hướng dịch chuyển bằng không (zero). Sinh học cơ bắp có quá trình hóa học và nội lực phức tạp hơn.

### Lực thay đổi theo vị trí

Nếu lực thay đổi:

```math
W=\int_{\vec r_1}^{\vec r_2}\vec F\cdot d\vec r
```

Tích phân cộng tất cả đóng góp vi phân:

```math
dW=\vec F\cdot d\vec r
```

Đây là ví dụ rõ ràng về việc calculus được sinh ra bởi cấu trúc vật lý: khi tác động thay đổi liên tục, tổng hữu hạn (finite) cần tích phân.

> **Chuyển mạch:** Ở chặng này của **Công, năng lượng, thế năng và công suất**, **Động năng và định lý công–động năng** tiếp nhận điểm tựa từ **Công: lực truyền năng lượng qua độ dời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế năng và lực bảo toàn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động năng và định lý công–động năng

Động năng (Kinetic Energy / 운동에너지) của vật khối lượng `m`, tốc độ (speed) `v` trong cơ học Newton:

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công, năng lượng, thế năng và công suất**, **Thế năng và lực bảo toàn** tiếp nhận điểm tựa từ **Động năng và định lý công–động năng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế năng hấp dẫn gần mặt đất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Độ dốc (gradient / 기울기) chỉ hướng tăng nhanh nhất của vô hướng (scalar) trường (field) `U`; dấu âm khiến lực (force) hướng về giảm nhanh nhất. Đây là liên hệ (connection) trực tiếp sang học máy (Machine Learning): độ dốc (gradient / 기울기) descent cũng đi theo `-\nabla L` để giảm tổn hao (loss) hàm (function / 함수), dù “tổn hao” không phải vật lý (physical / 물리적) năng lượng (energy / 에너지).

> **Chuyển mạch:** Trong **Công, năng lượng, thế năng và công suất**, **Thế năng hấp dẫn gần mặt đất** tiếp nhận điểm tựa từ **Thế năng và lực bảo toàn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thế năng lò xo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thế năng hấp dẫn gần mặt đất

Với hấp dẫn (gravity) gần mặt đất, `F_y=-mg`. Ta muốn `F_y=-dU/dy`, nên:

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

> **Chuyển mạch:** Ở chặng này của **Công, năng lượng, thế năng và công suất**, **Thế năng lò xo** tiếp nhận điểm tựa từ **Thế năng hấp dẫn gần mặt đất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo toàn cơ năng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công, năng lượng, thế năng và công suất**, **Bảo toàn cơ năng** tiếp nhận điểm tựa từ **Thế năng lò xo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lực không bảo toàn và “mất năng lượng”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Kết quả trùng với kinematics, nhưng năng lượng phương thức (method / 메서드) không cần tính thời gian.

> **Chuyển mạch:** Trong **Công, năng lượng, thế năng và công suất**, **Lực không bảo toàn và “mất năng lượng”** tiếp nhận điểm tựa từ **Bảo toàn cơ năng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Công suất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lực không bảo toàn và “mất năng lượng”

Khi có ma sát, cơ năng (mechanical energy) giảm:

```math
\Delta(K+U)=W_{nonconservative}
```

Nhưng tổng năng lượng của hệ rộng hơn không biến mất. cơ năng chuyển thành nội năng (internal energy), nhiệt, âm, biến dạng (deformation) hoặc các dạng khác.

Cụm từ “năng lượng bị mất” thường chỉ nghĩa “năng lượng rời khỏi dạng mà ta đang theo dõi”. bảo toàn (Conservation) of năng lượng nói tổng năng lượng của một hệ cô lập không tự sinh ra hay biến mất.

> **Chuyển mạch:** Ở chặng này của **Công, năng lượng, thế năng và công suất**, **Công suất** tiếp nhận điểm tựa từ **Lực không bảo toàn và “mất năng lượng”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Efficiency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Công suất

Công suất (Power / 일률, 전력 trong context điện) là tốc độ truyền hoặc chuyển đổi năng lượng:

```math
P=\frac{dW}{dt}
```

Đơn vị watt:

```math
1\,W=1\,J/s
```

Nếu lực và vận tốc (velocity):

```math
P=\vec F\cdot\vec v
```

Một động cơ 100 kW không nhất thiết có tổng năng lượng nhiều hơn một động cơ 50 kW; nó có khả năng chuyển năng lượng nhanh hơn.

Trong điện toán (computing), công suất (power) consumption cũng là năng lượng per thời gian (time / 시간). Một CPU dùng 100 W tiêu thụ 100 J mỗi giây ở mức công suất đó. Nhiệt sinh ra, thời lượng pin (battery life) và giảm xung do nhiệt (thermal throttling) đều liên quan tới tốc độ chuyển đổi năng lượng (energy conversion rate).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công, năng lượng, thế năng và công suất**, **Efficiency** tiếp nhận điểm tựa từ **Công suất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **thế (Potential) well và cân bằng (equilibrium)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Efficiency

Hiệu suất (Efficiency / 효율):

```math
\eta=\frac{E_{useful}}{E_{input}}
```

hoặc với steady tiến trình (process / 프로세스):

```math
\eta=\frac{P_{useful}}{P_{input}}
```

`\eta<1` trong máy thực vì năng lượng phân tán thành nhiệt, âm, ma sát (friction), tổn hao điện (electrical loss)… nhưng năng lượng tổng (total) vẫn được bảo toàn.

> **Chuyển mạch:** Trong **Công, năng lượng, thế năng và công suất**, **thế (Potential) well và cân bằng (equilibrium)** tiếp nhận điểm tựa từ **Efficiency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bài toán mẫu: tàu lượn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## thế (Potential) well và cân bằng (equilibrium)

Nếu `U(x)` có cực tiểu (minimum) tại `x_0`, thì:

```math
\left.\frac{dU}{dx}\right|_{x_0}=0
```

và lực bằng không. Nếu độ cong (curvature) dương:

```math
\left.\frac{d^2U}{dx^2}\right|_{x_0}>0
```

đó là cân bằng ổn định. Gần cực tiểu, nhiều thế năng trơn (smooth) có thể xấp xỉ bằng parabola Taylor:

```math
U(x)\approx U(x_0)+\frac12k(x-x_0)^2
```

Đây là lý do họa âm (harmonic) bộ dao động (oscillator) xuất hiện ở rất nhiều hệ vật lý: bất kỳ cân bằng ổn định (stable equilibrium) trơn nào, khi nhiễu loạn (perturbation) nhỏ, thường có hành vi (behavior / 동작) gần lò xo.

> **Chuyển mạch:** Ở chặng này của **Công, năng lượng, thế năng và công suất**, **Bài toán mẫu: tàu lượn** tiếp nhận điểm tựa từ **thế (Potential) well và cân bằng (equilibrium)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bài toán mẫu: tàu lượn

Một xe tàu lượn bắt đầu nghỉ ở độ cao `20 m`, bỏ qua ma sát. Hỏi tốc độ ở độ cao `5 m`.

Chọn mốc thế năng tùy ý. bảo toàn:

```math
m g(20)=\frac12mv^2+mg(5)
```

```math
mg(15)=\frac12mv^2
```

```math
v=\sqrt{2g(15)}\approx17.1\,m/s
```

Không cần biết hình dạng đường ray. Đây là sức mạnh của lực bảo toàn (conservative force): đường đi (path) thông tin (information / 정보) được nén vào thế độ chênh (difference).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Công, năng lượng, thế năng và công suất**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bài toán mẫu: tàu lượn** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> lực view hỏi “tại mỗi khoảnh khắc, tương tác đang bẻ quỹ đạo (trajectory) thế nào?”. năng lượng view hỏi “hệ có thể chuyển từ trạng thái này sang trạng thái kia hay không, và lượng khả năng chuyển đổi được phân phối giữa những dạng nào?”. Hai view không cạnh tranh; chúng là hai phép chiếu của cùng động lực học (dynamics).

> **Chuyển mạch:** Trong **Công, năng lượng, thế năng và công suất**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Năng lượng là lực”

Không. lực có đơn vị N và là vectơ; năng lượng có đơn vị J và thường là vô hướng. lực liên hệ với độ dốc (gradient / 기울기) của thế năng (potential energy).

### “Công bằng lực nhân quãng đường trong mọi trường hợp”

Chỉ khi lực cùng hướng độ dịch chuyển và hằng số (constant). Dạng tổng quát là dot sản phẩm (product / 제품) và tích phân đường.

> **Chuyển mạch:** Ở chặng này của **Công, năng lượng, thế năng và công suất**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Nhiệt động lực học](../04_thermal_statistical/00_thermodynamics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
