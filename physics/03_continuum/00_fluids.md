# Cơ học chất lưu: áp suất, lực nổi, phương trình liên tục, Bernoulli và Navier–Stokes

## Từ các hạt riêng lẻ đến mô hình liên tục

Chất lưu (Fluid / 유체) gồm chất lỏng và chất khí, có khả năng biến dạng liên tục khi chịu ứng suất cắt. Ở cấp vi mô, chất lưu được cấu tạo từ các phân tử. Tuy nhiên theo dõi chuyển động của cỡ `10^23` hạt là bất khả thi và cũng không cần thiết cho phần lớn bài toán vĩ mô.

Cơ học chất lưu dùng xấp xỉ môi trường liên tục (Continuum Approximation / 연속체 근사): mật độ, áp suất và vận tốc được xem như các trường biến thiên trơn theo không gian và thời gian.

Đây là một ví dụ của phép lấy trung bình thô (coarse-graining) và tính nổi lên (emergence). Ta bỏ qua chi tiết chuyển động của từng phân tử nhưng giữ những đại lượng tập thể đủ để dự đoán dòng chảy ở quy mô vĩ mô.

## Mật độ

Mật độ (Density / 밀도) được định nghĩa cục bộ bởi:

```math
\rho=\frac{dm}{dV}
```

Nếu vật chất phân bố đều trong thể tích đang xét:

```math
\rho=\frac{m}{V}
```

Đơn vị SI là `kg/m³`.

## Áp suất

Áp suất (Pressure / 압력) là lực pháp tuyến trên một đơn vị diện tích:

```math
P=\frac{F_\perp}{A}
```

Đơn vị pascal:

```math
1\,Pa=1\,N/m^2
```

Trong một chất lưu đứng yên và cân bằng, áp suất tại một điểm được mô tả như một trường vô hướng. Lực do áp suất tác dụng lên một phần tử bề mặt luôn theo phương pháp tuyến của bề mặt đó.

### Áp suất thủy tĩnh

Xét một cột chất lưu có chiều cao `h` và tiết diện `A`. Khối lượng của cột chất lưu là `\rho Ah`, nên trọng lượng bằng:

```math
mg=\rho Ahg
```

Cân bằng lực dẫn tới:

```math
\Delta P=\rho gh
```

Do đó, nếu `P_0` là áp suất ở mặt trên:

```math
P=P_0+\rho gh
```

Áp suất tăng theo độ sâu vì lớp chất lưu ở dưới phải cân bằng trọng lượng của phần chất lưu nằm phía trên.

## Nguyên lý Pascal và hệ thủy lực

Trong một chất lưu gần như không nén được và được giữ trong hệ kín, thay đổi áp suất có thể được truyền qua chất lưu. Nếu hai pít-tông có diện tích `A_1` và `A_2`:

```math
\frac{F_1}{A_1}=\frac{F_2}{A_2}
```

nên:

```math
F_2=F_1\frac{A_2}{A_1}
```

Kích thủy lực (Hydraulic Jack / 유압 잭) có thể khuếch đại lực nhưng không tạo năng lượng miễn phí. Trong mô hình lý tưởng, pít-tông lớn di chuyển quãng đường nhỏ hơn sao cho công được bảo toàn:

```math
F_1d_1=F_2d_2
```

## Lực nổi Archimedes

Một vật chìm trong chất lưu chiếm chỗ một thể tích chất lưu. Vì áp suất tăng theo độ sâu, lực áp suất tác dụng lên mặt dưới thường lớn hơn lực trên mặt trên, tạo một hợp lực hướng lên:

```math
F_b=\rho_{fluid}gV_{displaced}
```

Đây là lực đẩy Archimedes (Buoyant Force / 부력).

Nếu mật độ trung bình của toàn vật nhỏ hơn mật độ chất lưu, vật có thể nổi ở trạng thái cân bằng. Một con tàu bằng thép nổi không phải vì thép nhẹ hơn nước, mà vì hình dạng rỗng của tàu làm mật độ trung bình của cả tàu, kể cả phần không khí bên trong, nhỏ hơn mật độ nước.

## Bảo toàn khối lượng và phương trình liên tục

Với dòng chảy ổn định của chất lưu không nén được qua một ống:

```math
A_1v_1=A_2v_2
```

Quan hệ này xuất phát từ bảo toàn khối lượng. Trong khoảng thời gian `\Delta t`, thể tích chất lưu đi qua một tiết diện là:

```math
\Delta V=Av\Delta t
```

Nếu mật độ không đổi, lưu lượng thể tích phải như nhau qua các tiết diện nối tiếp của cùng một dòng chảy ổn định.

Dạng cục bộ và tổng quát hơn của bảo toàn khối lượng là:

```math
\frac{\partial \rho}{\partial t}+\nabla\cdot(\rho\vec v)=0
```

Đây là phương trình liên tục (Continuity Equation / 연속방정식). Nó biểu diễn một định luật bảo toàn dưới dạng phương trình vi phân cho trường mật độ và trường vận tốc.

## Phương trình Bernoulli

Với dòng chảy ổn định, không nén được và không nhớt dọc theo một đường dòng, phương trình Bernoulli có dạng:

```math
P+\frac12\rho v^2+\rho gy=constant
```

Ba hạng tử đều có thứ nguyên năng lượng trên một đơn vị thể tích:

- `P`: phần liên quan tới áp suất;
- `\frac12\rho v^2`: mật độ động năng;
- `\rho gy`: mật độ thế năng hấp dẫn.

Có thể xem phương trình Bernoulli như một dạng bảo toàn cơ năng của một phần tử chất lưu dưới những giả định cụ thể.

### Tại sao dòng chảy nhanh có thể đi kèm áp suất tĩnh thấp hơn?

Trên một đường dòng nằm ngang, `y` không đổi nên:

```math
P+\frac12\rho v^2=constant
```

Trong mô hình này, nếu vận tốc tăng thì áp suất tĩnh giảm. Tuy nhiên câu “dòng chảy càng nhanh thì áp suất luôn càng thấp” là quá đơn giản. Trong hệ thực, còn phải xét hình học, công do bơm hoặc tua-bin, độ nhớt, tính nén được và việc các điểm có nằm trên cùng một đường dòng hay không.

## Độ nhớt

Độ nhớt (Viscosity / 점성) đặc trưng cho khả năng chất lưu chống lại biến dạng trượt giữa các lớp. Với chất lưu Newton:

```math
\tau=\mu\frac{du}{dy}
```

Trong đó `\mu` là độ nhớt động lực học (dynamic viscosity / 동점성계수와 구별되는 점성계수).

Mật ong có độ nhớt lớn hơn nước. Độ nhớt làm cơ năng có tổ chức của dòng chảy chuyển dần thành nội năng thông qua ma sát nội tại giữa các lớp chất lưu.

## Số Reynolds

Số Reynolds (Reynolds Number / 레이놀즈 수) là:

```math
Re=\frac{\rho vL}{\mu}
```

Đây là một tỉ số vô thứ nguyên so sánh độ quan trọng tương đối của hiệu ứng quán tính với hiệu ứng nhớt.

Khi `Re` nhỏ, độ nhớt thường chi phối và dòng chảy có xu hướng tầng, trơn và ổn định hơn. Khi `Re` lớn, hiệu ứng quán tính mạnh hơn và dòng chảy dễ xuất hiện bất ổn hoặc rối, mặc dù ngưỡng chuyển tiếp cụ thể còn phụ thuộc hình học và nhiễu ban đầu.

Các số vô thứ nguyên là công cụ rất mạnh trong vật lý và kỹ thuật. Hai hệ có kích thước rất khác nhau vẫn có thể có động lực học tương tự nếu những tỉ số vô thứ nguyên chi phối chúng giống nhau.

## Dòng chảy tầng trong ống

Định luật Hagen–Poiseuille cho dòng chảy tầng của chất lưu Newton không nén được trong một ống trụ dài:

```math
Q=\frac{\pi R^4\Delta P}{8\mu L}
```

Sự phụ thuộc vào `R^4` rất mạnh. Chỉ cần bán kính ống giảm một chút, lưu lượng có thể giảm đáng kể. Điều này quan trọng trong mạch máu và các hệ vi lưu (microfluidics / 미세유체역학).

Định luật chỉ áp dụng trong miền dòng chảy tầng và dưới các giả định hình học, điều kiện biên cụ thể.

## Lực cản, lực nâng và lớp biên

Trong chất lưu thực, gần bề mặt vật rắn hình thành lớp biên (Boundary Layer / 경계층), nơi vận tốc thay đổi từ gần bằng vận tốc bề mặt do điều kiện không trượt (no-slip condition) tới vận tốc của dòng chảy bên ngoài.

Sự tách lớp biên có thể làm thay đổi mạnh lực cản. Vì vậy lực cản không chỉ phụ thuộc diện tích đối diện dòng chảy mà còn phụ thuộc hình dạng, số Reynolds và trạng thái của lớp biên.

Lực nâng của cánh máy bay cũng không thể được giải thích đầy đủ bằng câu chuyện “không khí phía trên phải đi nhanh hơn để gặp lại không khí phía dưới”. Một mô tả vật lý đúng phải xét phân bố áp suất, tuần hoàn, độ lệch động lượng của dòng khí và nghiệm của các phương trình Euler hoặc Navier–Stokes ở mức mô hình thích hợp.

## Phương trình Navier–Stokes

Một dạng của phương trình Navier–Stokes cho chất lưu Newton không nén được là:

```math
\rho\left(\frac{\partial\vec v}{\partial t}+(\vec v\cdot\nabla)\vec v\right)
=-\nabla P+\mu\nabla^2\vec v+\rho\vec g
```

Có thể đọc đây là định luật II Newton cho môi trường liên tục: mật độ khối lượng nhân với gia tốc của trường vận tốc bằng tổng mật độ lực do gradient áp suất, độ nhớt và lực khối như trọng lực.

Hạng tử đối lưu phi tuyến:

```math
(\vec v\cdot\nabla)\vec v
```

là một nguồn quan trọng của độ phức tạp trong động lực học chất lưu và đóng vai trò trung tâm trong dòng rối.

Động lực học chất lưu tính toán (Computational Fluid Dynamics, CFD / 전산유체역학) rời rạc hóa các phương trình trên lưới hoặc mesh để mô phỏng dòng khí, làm mát, quá trình cháy, khí động học, thời tiết và nhiều hệ kỹ thuật khác.

## Mô hình tư duy (Mental Model)

> Cơ học chất lưu có thể được xem như cơ học Newton sau khi ta thay mô tả “mỗi vật có một vị trí và vận tốc” bằng mô tả “mỗi điểm trong không gian có mật độ, áp suất và vận tốc”. Các định luật bảo toàn vẫn là cốt lõi; cách biểu diễn chuyển từ hạt riêng lẻ sang các trường liên tục.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Áp suất là một lực”

Không. Áp suất là lực trên một đơn vị diện tích. Muốn tính lực tổng do áp suất, phải tích phân phân bố áp suất trên bề mặt và tính đúng hướng pháp tuyến của từng phần tử diện tích.

### “Bernoulli áp dụng cho mọi dòng chảy”

Không. Phương trình Bernoulli đơn giản dựa trên các giả định cụ thể. Tổn thất nhớt, bơm, tua-bin, dòng không ổn định hoặc tính nén được có thể yêu cầu phương trình năng lượng tổng quát hơn.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Định luật Newton](../01_mechanics/01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Hiện tượng vận chuyển](02_transport_diffusion_heat.md), [Dòng rối và lưu biến](03_turbulence_rheology_soft_matter.md).
