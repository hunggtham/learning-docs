# Động học: vị trí, vận tốc, gia tốc và quỹ đạo

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**. Route đi từ position/coordinate → velocity → acceleration → trajectory/constraints → frame-dependent description, để mô tả chuyển động tách khỏi nguyên nhân.

## Động học tách “chuyển động thế nào” khỏi “vì sao chuyển động”

Động học (Kinematics / 운동학) mô tả vị trí, vận tốc và gia tốc mà chưa cần biết lực nào gây ra chuyển động. Sự tách biệt này rất hữu ích: trước khi xây dựng mô hình nhân quả (causal model), ta cần ngôn ngữ chính xác để mô tả hành vi (behavior / 동작).

Giả sử vị trí của một vật trên trục `x` phụ thuộc thời gian:

```math
x=x(t)
```

Đây là một hàm (Function / 함수): mỗi thời điểm `t` được ánh xạ tới một vị trí `x`.

> **Chuyển mạch:** Trong **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Vận tốc: tốc độ biến thiên (rate) of thay đổi (change / 변경) của vị trí** tiếp nhận điểm tựa từ **Động học tách “chuyển động thế nào” khỏi “vì sao chuyển động”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tốc độ và vận tốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vận tốc: tốc độ biến thiên (rate) of thay đổi (change / 변경) của vị trí

Vận tốc trung bình:

```math
\bar v = \frac{\Delta x}{\Delta t}
```

Nếu chiếc xe đi từ `x=0` đến `x=100 m` trong 10 s, vận tốc trung bình là `10 m/s`. Nhưng xe có thể tăng tốc, phanh, dừng. Để hỏi vận tốc tại đúng thời điểm, ta thu nhỏ khoảng thời gian:

```math
v(t)=\lim_{\Delta t\to 0}\frac{x(t+\Delta t)-x(t)}{\Delta t}
=\frac{dx}{dt}
```

Đạo hàm (Derivative / 미분) ở đây không phải thủ thuật toán. Nó là câu trả lời toán học cho câu hỏi vật lý “vị trí đang thay đổi nhanh đến mức nào ngay bây giờ?”.

Đơn vị:

```math
[v]=m/s
```

Dấu của vận tốc cho biết hướng theo quy ước trục. `v=-5 m/s` không nghĩa “chậm hơn không (zero)”; nó nghĩa chuyển động theo hướng âm với tốc độ 5 m/s.

> **Chuyển mạch:** Ở chặng này của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Tốc độ và vận tốc** tiếp nhận điểm tựa từ **Vận tốc: tốc độ biến thiên (rate) of thay đổi (change / 변경) của vị trí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gia tốc: tốc độ biến thiên of thay đổi (change / 변경) của vận tốc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tốc độ và vận tốc

Tốc độ (Speed / 속력) là độ lớn của vận tốc:

```math
speed=|\vec v|
```

Vận tốc (Velocity / 속도) là vectơ (vector). Trong tiếng Hàn phổ thông đôi khi “속도” được dùng như tốc độ (speed), nhưng trong sách Vật lý Hàn Quốc thường phân biệt `속력` cho vô hướng (scalar) tốc độ và `속도` cho vectơ vận tốc (velocity).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Gia tốc: tốc độ biến thiên of thay đổi (change / 변경) của vận tốc** tiếp nhận điểm tựa từ **Tốc độ và vận tốc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tích phân: tái tạo trạng thái từ tốc độ biến thiên of thay đổi (change / 변경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gia tốc: tốc độ biến thiên of thay đổi (change / 변경) của vận tốc

Gia tốc (Acceleration / 가속도):

```math
a(t)=\frac{dv}{dt}=\frac{d^2x}{dt^2}
```

Đơn vị:

```math
[a]=m/s^2
```

`m/s²` thường gây khó hiểu khi học lần đầu. Nó nghĩa “mỗi giây, vận tốc thay đổi thêm bao nhiêu m/s”. Gia tốc `2 m/s²` nghĩa sau mỗi giây, vận tốc tăng thêm `2 m/s` nếu gia tốc giữ nguyên.

Một xe có thể gia tốc dù tốc độ không đổi nếu hướng vận tốc đổi. Chuyển động tròn đều là ví dụ: độ lớn (magnitude) của `v` không đổi nhưng vectơ `v` quay liên tục, nên `dv/dt` khác không.

> **Chuyển mạch:** Trong **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Tích phân: tái tạo trạng thái từ tốc độ biến thiên of thay đổi (change / 변경)** tiếp nhận điểm tựa từ **Gia tốc: tốc độ biến thiên of thay đổi (change / 변경) của vận tốc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển động gia tốc không đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tích phân: tái tạo trạng thái từ tốc độ biến thiên of thay đổi (change / 변경)

Nếu biết vận tốc, ta có thể phục hồi độ dịch chuyển (displacement) bằng tích phân:

```math
x(t)-x(t_0)=\int_{t_0}^{t}v(\tau)\,d\tau
```

Nếu biết gia tốc:

```math
v(t)-v(t_0)=\int_{t_0}^{t}a(\tau)\,d\tau
```

Tích phân (Integral / 적분) là phép cộng liên tục của vô số đóng góp cực nhỏ. Trên đồ thị (graph / 그래프) `v-t`, diện tích có dấu dưới đường cong bằng độ dịch chuyển.

Đây là một liên kết kiến thức (knowledge connection / 지식 연결) nền tảng: đạo hàm (derivative) hỏi cục bộ (local / 로컬) tốc độ biến thiên; tích phân (integral) tích lũy tốc độ biến thiên để ra tổng (total) thay đổi (change / 변경). Trong tài chính (finance), lãi suất tức thời tích lũy thành tăng trưởng; trong mạng máy tính (networking), thông lượng dữ liệu (throughput) tích lũy theo thời gian thành lượng dữ liệu (data / 데이터); trong physics, vận tốc tích lũy thành độ dịch chuyển.

> **Chuyển mạch:** Ở chặng này của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Chuyển động gia tốc không đổi** tiếp nhận điểm tựa từ **Tích phân: tái tạo trạng thái từ tốc độ biến thiên of thay đổi (change / 변경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rơi tự do** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển động gia tốc không đổi

Khi `a` không đổi:

```math
\frac{dv}{dt}=a
```

Tích phân theo thời gian:

```math
v(t)=v_0+at
```

Tiếp tục dùng `v=dx/dt`:

```math
\frac{dx}{dt}=v_0+at
```

Tích phân:

```math
x(t)=x_0+v_0t+\frac12at^2
```

Đây không phải hai công thức độc lập cần học thuộc. Chúng là hệ quả trực tiếp của giả định “gia tốc không đổi”.

Loại `t` khỏi hai phương trình:

```math
v^2=v_0^2+2a(x-x_0)
```

Phương trình này hữu ích khi không biết thời gian.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Rơi tự do** tiếp nhận điểm tựa từ **Chuyển động gia tốc không đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Projectile chuyển động (motion)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rơi tự do

Gần bề mặt Trái Đất, bỏ qua lực cản không khí, mọi vật có gia tốc hấp dẫn gần như:

```math
g\approx 9.81\,m/s^2
```

Nếu chọn chiều lên là dương:

```math
a=-g
```

Một vật thả từ nghỉ ở độ cao `h` có:

```math
h=\frac12gt^2
```

suy ra:

```math
t=\sqrt{\frac{2h}{g}}
```

Điểm sâu ở đây là khối lượng không xuất hiện. Trong mô hình bỏ qua lực cản (drag), vật nặng và nhẹ rơi cùng gia tốc (acceleration). Sự khác biệt trong đời sống chủ yếu đến từ lực cản khí động, không phải vì hấp dẫn (gravity) “kéo vật nặng nhanh hơn theo tỉ lệ khiến gia tốc tăng”.

> **Chuyển mạch:** Trong **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Projectile chuyển động (motion)** tiếp nhận điểm tựa từ **Rơi tự do** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển động tròn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Projectile chuyển động (motion)

Chuyển động ném xiên (Projectile Motion / 포물선 운동) minh họa sức mạnh của phân rã (decomposition) theo vectơ. Bỏ qua không khí, hấp dẫn chỉ tác dụng theo phương đứng:

```math
x(t)=x_0+v_0\cos\theta\,t
```

```math
y(t)=y_0+v_0\sin\theta\,t-\frac12gt^2
```

Phương ngang là chuyển động đều; phương đứng là rơi tự do. Hai chuyển động độc lập về phương trình nhưng chia sẻ cùng `t`.

Nếu `y_0=0` và vật rơi về cùng độ cao, thời gian bay:

```math
T=\frac{2v_0\sin\theta}{g}
```

Tầm xa:

```math
R=\frac{v_0^2\sin 2\theta}{g}
```

Kết quả `45°` tối ưu chỉ đúng trong mô hình (model / 모델) mặt phẳng ngang, cùng độ cao đầu-cuối và không có lực cản. Trong thực tế bóng đá, golf, đạn đạo và baseball, lực cản và lực nâng (lift) làm góc tối ưu thay đổi.

> **Chuyển mạch:** Ở chặng này của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Chuyển động tròn** tiếp nhận điểm tựa từ **Projectile chuyển động (motion)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bài toán mẫu: phanh xe** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển động tròn

Một vật chạy vòng tròn bán kính `r` với tốc độ `v` có gia tốc hướng tâm:

```math
a_c=\frac{v^2}{r}=\omega^2r
```

Trong đó `\omega` là tốc độ góc (Angular Velocity / 각속도), đơn vị `rad/s`, với:

```math
v=\omega r
```

Tại sao có gia tốc khi tốc độ không đổi? Vì vectơ vận tốc luôn tiếp tuyến với đường tròn, hướng của nó thay đổi. Khi lấy giới hạn `\Delta \vec v/\Delta t`, vectơ biến thiên hướng về tâm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Bài toán mẫu: phanh xe** tiếp nhận điểm tựa từ **Chuyển động tròn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **rời rạc (Discrete) thời gian (time / 시간) và số (numerical) mô phỏng (simulation)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bài toán mẫu: phanh xe

Một xe chạy `20 m/s` và phanh với gia tốc không đổi `-5 m/s²`. Hỏi quãng đường dừng.

Ta biết:

```math
v_0=20\,m/s,\quad v=0,\quad a=-5\,m/s^2
```

Không cần thời gian nên dùng:

```math
v^2=v_0^2+2a\Delta x
```

Thay số:

```math
0=20^2+2(-5)\Delta x
```

```math
\Delta x=40\,m
```

Điều đáng nhớ hơn đáp án là thu nhỏ quy mô (scaling):

```math
\Delta x\propto v_0^2
```

Nếu tốc độ ban đầu gấp đôi mà phanh (braking) gia tốc giữ nguyên, quãng đường phanh gấp bốn. Đây là lý do tăng tốc xe từ 50 lên 100 km/h nguy hiểm hơn nhiều so với trực giác tuyến tính “chỉ nhanh gấp đôi”.

> **Chuyển mạch:** Trong **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **rời rạc (Discrete) thời gian (time / 시간) và số (numerical) mô phỏng (simulation)** tiếp nhận điểm tựa từ **Bài toán mẫu: phanh xe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## rời rạc (Discrete) thời gian (time / 시간) và số (numerical) mô phỏng (simulation)

Máy tính không theo dõi thời gian liên tục vô hạn. Trong game physics hoặc mô phỏng, ta dùng bước `\Delta t`:

```math
v_{n+1}\approx v_n+a_n\Delta t
```

```math
x_{n+1}\approx x_n+v_n\Delta t
```

Đây là Euler tích phân (integration). Nó minh họa một liên hệ (connection) quan trọng giữa calculus liên tục và tính toán số (numerical computing). Nếu `\Delta t` quá lớn, sai số tích lũy và mô phỏng có thể mất ổn định. bộ máy vật lý (Physics engine) tốt dùng bộ tích phân (integrator) phù hợp như semi-implicit Euler, Verlet hoặc Runge-Kutta tùy mục tiêu.

> **Chuyển mạch:** Ở chặng này của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **rời rạc (Discrete) thời gian (time / 시간) và số (numerical) mô phỏng (simulation)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những ngộ nhận thường gặp (Common Misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Kinematics là việc xem chuyển động như một chuỗi “trạng thái theo thời gian”. Position là trạng thái hình học; vận tốc là tốc độ trạng thái thay đổi; gia tốc là tốc độ chính vận tốc thay đổi. đạo hàm đi từ trạng thái (state / 상태) xuống change-tốc độ biến thiên, tích phân đi ngược từ change-tốc độ biến thiên lên accumulated trạng thái.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, **Những ngộ nhận thường gặp (Common Misconceptions)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Gia tốc dương nghĩa là vật nhanh dần”

Không nhất thiết. Nếu `v<0` và `a>0`, gia tốc ngược hướng vận tốc nên tốc độ có thể giảm. Nhanh dần hay chậm dần phụ thuộc dấu tương đối giữa `v` và `a` trong một chiều, hoặc góc giữa hai vectơ trong nhiều chiều.

### “Tại điểm cao nhất của ném thẳng đứng, gia tốc bằng không”

Sai. Vận tốc tức thời bằng không nhưng hấp dẫn vẫn tác dụng, nên `a=-g`.

> **Chuyển mạch:** Trong **Động học: vị trí, vận tốc, gia tốc và quỹ đạo**, sau nội dung của **Những ngộ nhận thường gặp (Common Misconceptions)**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

**Nên hiểu trước:** [Vector và hệ quy chiếu](../00_foundations/02_space_time_vectors_frames.md), [Ngôn ngữ Toán](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Newtonian dynamics](01_newton_laws_dynamics.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
