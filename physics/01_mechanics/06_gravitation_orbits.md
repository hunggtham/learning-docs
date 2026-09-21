# Hấp dẫn Newton, trường hấp dẫn và cơ học quỹ đạo

Hấp dẫn là một trong những ví dụ đẹp nhất cho cách Vật lý nối nhiều tầng mô hình: từ lực nghịch đảo bình phương, trường và thế năng đến quỹ đạo, thủy triều, chuyển quỹ đạo và cuối cùng là giới hạn nơi thuyết tương đối rộng trở nên cần thiết.

## Định luật hấp dẫn phổ quát

Hai khối lượng điểm `m_1` và `m_2` cách nhau `r` hút nhau với độ lớn

```math
F=G\frac{m_1m_2}{r^2}.
```

Dạng vectơ có thể viết

```math
\vec F_{12}
=-G\frac{m_1m_2}{r^2}\hat r,
```

nếu `\hat r` hướng từ nguồn tới vật thử.

Lực luôn hút trong cơ học Newton vì khối lượng hấp dẫn thông thường có cùng dấu.

## Vì sao xuất hiện `1/r²`?

Nếu một trường xuyên tâm có tổng thông lượng qua mọi mặt cầu bao quanh nguồn là như nhau, diện tích mặt cầu tăng theo

```math
A=4\pi r^2.
```

Do đó mật độ thông lượng phải giảm theo `1/r^2`. Đây không phải phép suy ra đầy đủ định luật hấp dẫn từ nguyên lý sâu hơn, nhưng giải thích vì sao quy luật nghịch đảo bình phương gắn tự nhiên với nguồn điểm trong không gian ba chiều.

Cùng hình học này cũng xuất hiện trong điện trường Coulomb.

## Trường hấp dẫn

Trường hấp dẫn được định nghĩa là lực trên một đơn vị khối lượng thử:

```math
\vec g=\frac{\vec F}{m_{test}}.
```

Với khối lượng điểm `M`,

```math
\vec g=-G\frac{M}{r^2}\hat r.
```

Gần bề mặt Trái Đất,

```math
g=\frac{GM_E}{R_E^2}.
```

Nếu độ cao `h\ll R_E`, thay đổi của `g` nhỏ và ta có thể xem `g` gần hằng số.

## Định luật Gauss cho hấp dẫn Newton

Đối với trường hấp dẫn,

```math
\oint \vec g\cdot d\vec A=-4\pi G M_{enc}.
```

Dạng vi phân là

```math
\nabla\cdot\vec g=-4\pi G\rho.
```

Nó cho thấy khối lượng là nguồn của trường hấp dẫn, tương tự cấu trúc Gauss trong điện tĩnh nhưng với dấu khác do hấp dẫn luôn hút.

## Định lý vỏ cầu

Một vỏ cầu mỏng có mật độ đều tạo trường bên ngoài giống như toàn bộ khối lượng tập trung tại tâm. Bên trong vỏ, trường hấp dẫn tổng bằng không.

Kết quả này giải thích vì sao một vật thể đối xứng cầu như hành tinh có thể được mô hình gần như khối lượng điểm đối với chuyển động bên ngoài nó.

Bên trong một quả cầu đồng nhất bán kính `R`, khối lượng chứa trong bán kính `r` là

```math
M(r)=M\frac{r^3}{R^3}.
```

Do đó

```math
g(r)=G\frac{M(r)}{r^2}
=\frac{GM}{R^3}r.
```

Trường tăng tuyến tính theo `r` từ tâm tới bề mặt trong mô hình mật độ đều.

## Thế hấp dẫn

Ta định nghĩa thế hấp dẫn `\Phi` sao cho

```math
\vec g=-\nabla\Phi.
```

Với khối lượng điểm,

```math
\Phi(r)=-\frac{GM}{r},
```

nếu chọn `\Phi(\infty)=0`.

Thế năng của vật khối lượng `m` là

```math
U=m\Phi=-\frac{GMm}{r}.
```

Dấu âm nghĩa trạng thái liên kết có năng lượng thấp hơn trạng thái hai vật ở xa vô hạn.

## Vì sao `mgh` chỉ là xấp xỉ cục bộ?

Đặt

```math
r=R_E+h
```

với `h\ll R_E`. Khai triển

```math
-\frac{GMm}{R_E+h}
\approx -\frac{GMm}{R_E}+\frac{GMm}{R_E^2}h.
```

Vì

```math
g=\frac{GM}{R_E^2},
```

nên

```math
\Delta U\approx mgh.
```

Do đó `mgh` là giới hạn gần mặt đất của thế hấp dẫn Newton tổng quát.

## Quỹ đạo tròn

Với vệ tinh chuyển động tròn bán kính `r`, hấp dẫn cung cấp gia tốc hướng tâm:

```math
\frac{v^2}{r}=\frac{GM}{r^2}.
```

Suy ra

```math
v_c=\sqrt{\frac{GM}{r}}.
```

Chu kỳ quỹ đạo là

```math
T=\frac{2\pi r}{v_c}
=2\pi\sqrt{\frac{r^3}{GM}}.
```

Do đó

```math
T^2\propto r^3,
```

là dạng của định luật Kepler III cho quỹ đạo tròn.

## Năng lượng của quỹ đạo tròn

Động năng là

```math
K=\frac12mv_c^2
=\frac{GMm}{2r}.
```

Thế năng là

```math
U=-\frac{GMm}{r}.
```

Tổng năng lượng:

```math
E=-\frac{GMm}{2r}.
```

Năng lượng âm cho biết quỹ đạo liên kết.

Một điều có vẻ nghịch trực giác là nếu vệ tinh mất một ít năng lượng do lực cản khí quyển, quỹ đạo hạ thấp và tốc độ quỹ đạo tròn mới lại **lớn hơn** vì `v_c\propto r^{-1/2}`. Vệ tinh mất cơ năng nhưng có thể tăng động năng trong quá trình rơi vào quỹ đạo thấp hơn.

## Quỹ đạo ellipse và bán trục lớn

Với quỹ đạo Kepler ellipse có bán trục lớn `a`, tổng năng lượng chỉ phụ thuộc `a`:

```math
E=-\frac{GMm}{2a}.
```

Công thức vis-viva cho vận tốc tại khoảng cách `r` là

```math
v^2=GM\left(\frac{2}{r}-\frac{1}{a}\right).
```

Nó thống nhất nhiều trường hợp: quỹ đạo tròn có `a=r`; quỹ đạo ellipse nhanh hơn gần cận điểm và chậm hơn gần viễn điểm.

## Định luật Kepler và bảo toàn mômen động lượng

Lực hấp dẫn hướng theo bán kính nên mômen lực quanh tâm bằng không:

```math
\vec\tau=\vec r\times\vec F=0.
```

Do đó mômen động lượng bảo toàn:

```math
\vec L=\text{hằng số}.
```

Diện tích quét bởi bán kính vectơ trong thời gian `dt` là

```math
dA=\frac12r^2d\theta.
```

Suy ra tốc độ quét diện tích

```math
\frac{dA}{dt}=\frac{L}{2m}
```

là hằng số. Đây chính là định luật Kepler II: bán kính nối hành tinh với Mặt Trời quét những diện tích bằng nhau trong những khoảng thời gian bằng nhau.

## Thế hiệu dụng

Với chuyển động trong trường xuyên tâm, ta có thể tách động năng thành phần bán kính và góc. Thế hiệu dụng là

```math
U_{eff}(r)
=-\frac{GMm}{r}
+\frac{L^2}{2mr^2}.
```

Hạng thứ hai thường gọi là rào cản ly tâm. Nó không phải một thế tương tác mới; nó xuất hiện khi bảo toàn mômen động lượng được dùng để giảm bài toán hai chiều thành chuyển động theo bán kính.

Cực tiểu của `U_{eff}` tương ứng với quỹ đạo tròn ổn định trong hấp dẫn Newton.

## Vận tốc thoát

Để vật đi ra vô hạn với vận tốc cuối bằng không, cần tổng năng lượng bằng không:

```math
\frac12mv_e^2-\frac{GMm}{R}=0.
```

Suy ra

```math
v_e=\sqrt{\frac{2GM}{R}}.
```

So với vận tốc quỹ đạo tròn tại cùng bán kính,

```math
v_e=\sqrt2\,v_c.
```

Khối lượng vật phóng triệt tiêu trong mô hình hai vật lý tưởng.

## Chuyển quỹ đạo Hohmann

Để chuyển giữa hai quỹ đạo tròn đồng tâm bán kính `r_1<r_2`, một chiến lược tiết kiệm nhiên liệu trong mô hình xung tức thời là quỹ đạo chuyển Hohmann.

Tàu tăng vận tốc tại `r_1` để đi vào ellipse có cận điểm `r_1`, viễn điểm `r_2`, rồi tăng vận tốc lần nữa tại `r_2` để tròn hóa quỹ đạo.

Năng lượng và vis-viva cho phép tính hai thay đổi vận tốc `\Delta v`. Đây là ví dụ cho thấy cơ học quỹ đạo thực tế là bài toán điều khiển **năng lượng và mômen động lượng**, không đơn giản là “bay thẳng lên”.

## Vì sao muốn lên quỹ đạo cần nhiều vận tốc ngang?

Để “lên cao” chỉ cần thắng thế năng. Nhưng để **ở lại quỹ đạo**, tàu phải có vận tốc ngang đủ lớn. Với quỹ đạo thấp quanh Trái Đất, vận tốc ngang cỡ nhiều km/s mới là phần lớn ngân sách `\Delta v`.

Tên lửa vì thế ban đầu bay lên để rời khí quyển dày, sau đó nghiêng dần để tăng vận tốc ngang.

## Lực thủy triều

Trường hấp dẫn không đồng đều theo không gian. Hai điểm cách nhau một khoảng nhỏ `\Delta r` cảm nhận gia tốc hơi khác nhau.

Với

```math
g(r)=\frac{GM}{r^2},
```

ta có độ biến thiên gần đúng

```math
|\Delta g|\sim\frac{2GM}{r^3}\Delta r.
```

Đây là nguồn của lực thủy triều. Thủy triều đại dương, biến dạng vệ tinh và hiện tượng kéo dài gần vật thể hấp dẫn mạnh đều liên quan đến gradient của trường hấp dẫn chứ không chỉ độ lớn của `g` tại một điểm.

## Điểm Lagrange

Trong hệ hai vật lớn quay quanh nhau, có những vị trí trong hệ quy chiếu quay nơi một vật nhỏ có thể giữ vị trí tương đối gần cố định. Chúng được gọi là các điểm Lagrange `L1`–`L5`.

`L4` và `L5` có thể ổn định trong điều kiện tỉ lệ khối lượng thích hợp; `L1`, `L2`, `L3` là các điểm cân bằng không ổn định nhưng rất hữu ích cho nhiệm vụ không gian với điều khiển hiệu chỉnh nhỏ.

## Gravity assist

Khi tàu vũ trụ bay qua một hành tinh đang chuyển động quanh Mặt Trời, trong hệ quy chiếu hành tinh tốc độ xa trước và sau tương tác có thể gần bằng nhau, nhưng hướng vận tốc đổi. Khi chuyển lại sang hệ quy chiếu Mặt Trời, vector vận tốc của hành tinh được cộng vào khác nhau trước và sau, nên tàu có thể tăng hoặc giảm năng lượng quỹ đạo quanh Mặt Trời.

Năng lượng không được tạo ra miễn phí; có trao đổi một lượng rất nhỏ với năng lượng quỹ đạo của hành tinh.

## Bài toán hai vật và khối lượng rút gọn

Nếu cả hai vật đều có khối lượng đáng kể, không vật nào thực sự đứng yên. Cả hai quay quanh tâm khối.

Bài toán có thể rút về chuyển động tương đối của một hạt có khối lượng rút gọn

```math
\mu=\frac{m_1m_2}{m_1+m_2}
```

trong thế

```math
U(r)=-\frac{Gm_1m_2}{r}.
```

Cách này cho thấy mô hình “một vật nhỏ quay quanh một vật đứng yên” chỉ là giới hạn `m_2\ll m_1`.

## Khi cơ học Newton không đủ?

Hấp dẫn Newton hoạt động rất tốt khi trường yếu và vận tốc nhỏ so với `c`. Nhưng nó không mô tả đầy đủ:

- tiến động cận điểm của Sao Thủy;
- giãn thời gian hấp dẫn;
- độ lệch ánh sáng bởi hấp dẫn;
- sóng hấp dẫn;
- hình học gần lỗ đen.

Trong các miền này cần thuyết tương đối rộng.

## Mô hình tư duy (Mental Model)

Quỹ đạo là chuyển động rơi tự do có mômen động lượng. Năng lượng quyết định hệ liên kết hay không và thang kích thước quỹ đạo; mômen động lượng quyết định hình học quay quanh nguồn; gradient của trường tạo hiệu ứng thủy triều. Cơ học quỹ đạo là bài toán tổ chức các định luật bảo toàn, không phải ghi nhớ từng công thức vệ tinh riêng lẻ.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Vệ tinh ở quỹ đạo vì không còn trọng lực”

Sai. Chính trọng lực cung cấp gia tốc hướng tâm.

### “Vận tốc thoát phải được giữ bằng động cơ mãi mãi”

Không. Trong mô hình không lực cản, đó là vận tốc ban đầu tối thiểu để tổng năng lượng không âm.

### “Lên quỹ đạo chỉ cần bay đủ cao”

Không. Vận tốc ngang là thành phần quyết định để liên tục rơi vòng quanh hành tinh.

### “Mất năng lượng thì vệ tinh luôn chậm lại”

Không nhất thiết. Khi rơi xuống quỹ đạo tròn thấp hơn, vận tốc quỹ đạo có thể tăng dù tổng cơ năng giảm.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Động lực học Newton](01_newton_laws_dynamics.md), [Công và năng lượng](03_work_energy_power.md), [Chuyển động quay và mômen động lượng](05_rotation_rigid_body.md).

**Liên hệ tiếp:** [Cơ học giải tích](08_analytical_mechanics.md), [Thuyết tương đối rộng](../07_relativity/01_general_relativity.md), [Vật lý sao](../11_astrophysics_cosmology/00_stars_compact_objects.md).
