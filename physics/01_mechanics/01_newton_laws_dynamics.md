# Định luật Newton, quán tính và động lực học

## Từ “chuyển động như thế nào?” sang “vì sao chuyển động thay đổi?”

Động học (kinematics) mô tả vị trí, vận tốc và gia tốc mà chưa cần hỏi nguyên nhân. Động lực học (dynamics / 동역학) đi thêm một bước: **tương tác nào làm động lượng của hệ thay đổi?**

Trực giác đời thường dễ dẫn tới ý nghĩ “muốn vật tiếp tục chuyển động thì phải tiếp tục đẩy”. Nhưng phần lớn trải nghiệm hàng ngày luôn có ma sát và lực cản. Khi loại các tương tác đó, Newton chỉ ra rằng chuyển động thẳng đều không cần một lực duy trì liên tục.

## Định luật I Newton và ý nghĩa của hệ quy chiếu quán tính

Định luật I Newton nói rằng tồn tại những hệ quy chiếu trong đó một vật cô lập giữ vận tốc không đổi:

```math
\sum\vec F=0
\quad\Rightarrow\quad
\frac{d\vec v}{dt}=0.
```

Những hệ như vậy được gọi là **hệ quy chiếu quán tính (inertial frame / 관성계)**.

Định luật I không chỉ là trường hợp đặc biệt của `F=ma`. Nó còn giúp định nghĩa loại hệ quy chiếu mà trong đó định luật II có dạng chuẩn không cần lực quán tính.

Một hệ chuyển động thẳng đều so với một hệ quán tính cũng là hệ quán tính trong cơ học Newton. Hệ đang gia tốc hoặc quay không còn thuộc loại này và cần các hạng quán tính bổ sung.

## Quán tính và khối lượng quán tính

Quán tính (inertia / 관성) là xu hướng giữ nguyên trạng thái chuyển động nếu không có tương tác bên ngoài làm thay đổi nó.

Trong cơ học Newton, khối lượng quán tính định lượng mức độ một vật chống lại sự thay đổi vận tốc.

Với cùng hợp lực,

```math
a=\frac{F}{m}.
```

Vật có khối lượng lớn hơn nhận gia tốc nhỏ hơn.

Điều này không có nghĩa khối lượng là một “lực cản”. Khối lượng là tham số liên hệ lực tổng với gia tốc hoặc liên hệ vận tốc với động lượng.

## Định luật II Newton ở dạng tổng quát

Dạng cơ bản nên ghi nhớ là

```math
\sum\vec F_{ext}
=\frac{d\vec p}{dt}.
```

Với

```math
\vec p=m\vec v.
```

Nếu khối lượng của vật đang xét không đổi,

```math
\sum\vec F_{ext}=m\vec a.
```

`F=ma` vì vậy là trường hợp rất quan trọng nhưng không phải dạng tổng quát nhất.

Đơn vị lực được xác định bởi

```math
1\,N=1\,kg\cdot m/s^2.
```

## Vì sao động lượng là cách nhìn tổng quát hơn?

Lực mô tả tốc độ trao đổi động lượng giữa hệ và môi trường.

Tích phân theo thời gian:

```math
\int_{t_1}^{t_2}\vec F\,dt
=\Delta\vec p.
```

Do đó cùng một biến thiên động lượng có thể được tạo bởi lực lớn trong thời gian ngắn hoặc lực nhỏ trong thời gian dài.

Cách nhìn này nối trực tiếp định luật II với xung lượng, va chạm, rocket và định luật bảo toàn động lượng.

## Lực là tương tác, không phải “thuộc tính đang nằm trong vật”

Lực (force / 힘) xuất hiện từ tương tác.

Ví dụ:

- hấp dẫn do tương tác hấp dẫn;
- lực điện do trường điện;
- phản lực pháp tuyến do tương tác điện từ giữa các bề mặt;
- ma sát do cấu trúc vi mô, biến dạng và tương tác điện từ;
- lực căng dây do vật liệu truyền ứng suất.

Khi nói “lực tác dụng lên vật”, ta đang mô tả ảnh hưởng của phần còn lại của hệ lên vật đã chọn.

## Sơ đồ vật thể tự do

Sơ đồ vật thể tự do (free-body diagram, FBD / 자유물체도) là công cụ mô hình hóa để tránh nhầm lực.

Quy trình:

1. Chọn **một vật hoặc một hệ** làm đối tượng.
2. Tách nó khỏi môi trường bằng một ranh giới tưởng tượng.
3. Liệt kê mọi tương tác đi qua ranh giới đó.
4. Vẽ lực theo hướng tác dụng lên hệ đã chọn.
5. Chọn hệ tọa độ thuận tiện.
6. Viết Newton II theo từng trục.

Không vẽ đồng thời lực mà vật tác dụng lên môi trường trong cùng FBD, vì đó là lực trên vật khác.

## Ví dụ: vật trên mặt phẳng nghiêng

Một vật khối lượng `m` trên mặt phẳng nghiêng góc `\theta`, bỏ ma sát.

Chọn trục `x` dọc dốc và `y` vuông góc mặt phẳng.

Trọng lực phân tích thành

```math
mg\sin\theta
```

dọc dốc và

```math
mg\cos\theta
```

vuông góc mặt phẳng.

Theo phương pháp tuyến, nếu vật không rời mặt:

```math
N-mg\cos\theta=0,
```

nên

```math
N=mg\cos\theta.
```

Theo phương dốc:

```math
ma=mg\sin\theta,
```

suy ra

```math
a=g\sin\theta.
```

Khối lượng triệt tiêu. Đây không phải phép màu: cả lực hấp dẫn và quán tính trong mô hình Newton cùng tỉ lệ với `m`.

## Định luật III Newton

Nếu A tác dụng lực lên B,

```math
\vec F_{A\to B}
=-\vec F_{B\to A}.
```

Hai lực có cùng độ lớn, ngược hướng nhưng tác dụng lên **hai vật khác nhau**.

Do đó chúng không tự triệt tiêu trong phương trình chuyển động của một vật riêng lẻ.

Ví dụ khi đi bộ, chân đẩy mặt đất về sau. Mặt đất thông qua ma sát tĩnh đẩy người về trước. Lực làm tâm khối người gia tốc là lực bên ngoài từ mặt đất.

## Định luật III và bảo toàn động lượng

Xét hai vật cô lập tương tác với nhau:

```math
\frac{d\vec p_1}{dt}=\vec F_{2\to1},
```

```math
\frac{d\vec p_2}{dt}=\vec F_{1\to2}.
```

Nếu

```math
\vec F_{2\to1}=-\vec F_{1\to2},
```

thì

```math
\frac{d}{dt}(\vec p_1+\vec p_2)=0.
```

Tổng động lượng được bảo toàn.

Trong điện từ học tương đối tính, việc phân chia động lượng giữa hạt và trường tinh tế hơn; trường điện từ cũng mang động lượng. Vì vậy dạng “hai lực tức thời bằng nhau và ngược nhau” không phải cách diễn đạt sâu nhất cho mọi tương tác hiện đại, còn bảo toàn tổng động lượng của hệ đầy đủ vẫn là cấu trúc cơ bản.

## Ràng buộc cơ học

Hai vật nối bằng dây không dãn không có gia tốc tùy ý độc lập. Chiều dài dây tạo phương trình ràng buộc.

Một bài ròng rọc lý tưởng thường cần ba lớp:

```text
Newton II cho từng vật
+ constraint do chiều dài dây
+ assumptions về dây/ròng rọc
```

Ví dụ với dây không khối lượng và ròng rọc lý tưởng, lực căng có thể được coi bằng nhau ở hai nhánh. Nếu ròng rọc có mômen quán tính đáng kể, lực căng hai phía nói chung khác nhau vì cần mômen lực để làm ròng rọc quay.

Assumption vì vậy quyết định phương trình nào được phép dùng.

## Trường lực

Một trường (field / 장) gán đại lượng vật lý cho từng điểm không gian–thời gian.

Trường hấp dẫn

```math
\vec g(\vec r)
```

cho lực trên một khối lượng thử:

```math
\vec F_g=m\vec g.
```

Điện trường cho

```math
\vec F=q\vec E.
```

Ngôn ngữ trường tách hai phần:

```text
nguồn tạo trường
→ trường tồn tại trong không gian
→ vật thử phản ứng với trường
```

Đây là mô hình trung tâm của hấp dẫn, điện từ học và lý thuyết trường hiện đại.

## Lực phụ thuộc vận tốc

Không phải mọi lực chỉ phụ thuộc vị trí.

Lực cản có thể có dạng

```math
\vec F_d=-b\vec v
```

ở một số chế độ Reynolds thấp, hoặc gần

```math
\vec F_d
=-\frac12\rho C_DA v^2\hat v
```

ở chế độ khác.

Lực Lorentz có thành phần

```math
q\vec v\times\vec B.
```

Vì vậy phương trình tổng quát có thể là

```math
m\ddot{\vec r}
=\vec F(\vec r,\dot{\vec r},t).
```

Đây là một ODE bậc hai cùng điều kiện ban đầu về vị trí và vận tốc.

## Cảnh báo với hệ biến khối lượng

Không nên lấy một hệ như rocket rồi viết máy móc

```math
F=m(t)a
```

cho một “vật” đang liên tục phun khối lượng mà không xét dòng động lượng đi qua biên hệ.

Dạng

```math
\sum F_{ext}=\frac{dP_{system}}{dt}
```

phải được áp dụng với định nghĩa hệ và flux động lượng phù hợp.

Phương trình rocket xuất hiện từ bookkeeping động lượng của tên lửa và nhiên liệu phụt ra, không chỉ bằng cách thay `m(t)` vào `F=ma`.

## Hệ phi quán tính

Trong xe tăng tốc hoặc hệ quay, nếu muốn giữ dạng phương trình Newton trong chính hệ đó, cần thêm lực quán tính như:

- lực tịnh tiến `-m\mathbf A`;
- Coriolis;
- ly tâm;
- Euler.

Do đó trước khi viết FBD cần hỏi:

> hệ tọa độ đang dùng có gần quán tính không?

Nếu không, thiếu lực quán tính sẽ làm phương trình sai dù mọi lực thật đã được vẽ đúng.

## Miền áp dụng của cơ học Newton

Cơ học Newton hoạt động rất tốt khi:

- vận tốc nhỏ so với `c`;
- hiệu ứng lượng tử không quan trọng;
- trường hấp dẫn không cần mô tả bằng độ cong không-thời gian;
- vật có thể được coarse-grain thành chất điểm hoặc vật rắn theo bài toán.

Khi `v/c` không còn nhỏ, cần thuyết tương đối hẹp. Ở thang nguyên tử, cần cơ học lượng tử. Với hấp dẫn mạnh hoặc độ chính xác cao, thuyết tương đối rộng có thể cần thiết.

Newton không “sai hoàn toàn”; nó là lý thuyết hiệu dụng cực kỳ chính xác trong miền thích hợp.

## Liên hệ với Kỹ thuật và Computer Science

Trong robotics và game physics, động lực học thường được viết dưới dạng

```math
M(q)\ddot q+C(q,\dot q)\dot q+g(q)=\tau.
```

Đây là phiên bản nhiều bậc tự do của cùng logic Newton/Lagrange.

Trong simulation, sai dấu lực, frame hoặc constraint có thể gây instability hoặc motion phi vật lý. Vì vậy unit test vật lý có thể kiểm tra:

- bảo toàn động lượng khi không có ngoại lực;
- giới hạn không ma sát;
- đối xứng trái–phải;
- đơn vị và bậc độ lớn.

## Mô hình tư duy (Mental Model)

Newton II không nói “lực tạo ra vận tốc”. Nó nói **hợp lực bên ngoài là tốc độ thay đổi động lượng**.

Một quy trình ổn định là

```text
chọn system
→ chọn frame
→ xác định interactions qua boundary
→ vẽ FBD
→ thêm constraints
→ viết ΣF = dp/dt
→ kiểm tra units và limiting cases
```

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Vật đang chuyển động phải có lực cùng chiều vận tốc”

Không. Nếu hợp lực bằng 0, vận tốc giữ nguyên.

### “Action–reaction triệt tiêu nhau nên không vật nào gia tốc”

Sai. Hai lực tác dụng lên hai vật khác nhau.

### “Phản lực pháp tuyến luôn bằng `mg`”

Không. Nó phụ thuộc hình học và gia tốc ràng buộc. Trên mặt phẳng nghiêng lý tưởng, `N=mg\cos\theta`; trong thang máy nó có thể lớn hoặc nhỏ hơn `mg`.

### “Lực hướng tâm là một lực mới”

Không. “Hướng tâm” chỉ mô tả hợp lực cần có thành phần hướng vào tâm để tạo gia tốc cong. Lực đó có thể do ma sát, dây, hấp dẫn hoặc lực khác.

### “`F=ma` dùng nguyên xi cho mọi hệ biến khối lượng”

Không. Phải xét flux động lượng qua biên hệ.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Động học](00_kinematics.md), [Đơn vị và độ bất định](../00_foundations/01_measurement_units_uncertainty.md).

**Liên hệ tiếp:** [Các lực thường gặp](02_common_forces.md), [Công và năng lượng](03_work_energy_power.md), [Động lượng](04_momentum_collisions.md), [Hệ quy chiếu phi quán tính](11_non_inertial_frames_rotating_systems.md).
