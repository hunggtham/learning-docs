# Động lượng, xung lượng, va chạm và tâm khối

## Tại sao cần động lượng khi đã có động năng?

Động lượng (Momentum / 운동량) mô tả trạng thái chuyển động theo cách gắn trực tiếp với tác động của lực:

```math
\vec p=m\vec v
```

Nó là vector. Trong cơ học Newton:

```math
\sum\vec F=\frac{d\vec p}{dt}
```

Energy rất mạnh với scalar conservation; momentum giữ thông tin hướng và đặc biệt hữu ích trong va chạm, recoil và hệ nhiều vật.

## Xung lượng

Xung lượng (Impulse / 충격량) là tích phân lực theo thời gian:

```math
\vec J=\int_{t_1}^{t_2}\vec F\,dt
```

Từ Newton II:

```math
\vec J=\Delta\vec p
```

Nếu lực trung bình:

```math
\vec J\approx \vec F_{avg}\Delta t
```

Cùng một `\Delta p`, kéo dài thời gian va chạm làm lực trung bình giảm. Airbag, vùng crumple zone của xe, thảm gym và động tác co tay khi bắt bóng đều khai thác nguyên lý này.

## Bảo toàn động lượng

Cho một hệ nhiều vật:

```math
\vec P=\sum_i\vec p_i
```

Các internal force theo Newton III triệt tiêu theo cặp trong tổng. Do đó:

```math
\frac{d\vec P}{dt}=\vec F_{external}
```

Nếu external force tổng bằng zero:

```math
\vec P=constant
```

Bảo toàn momentum không phụ thuộc collision có đàn hồi hay không. Nó xuất phát từ isolation của hệ và sâu hơn nữa từ translational symmetry của không gian.

## Va chạm đàn hồi và không đàn hồi

Trong va chạm đàn hồi (Elastic Collision / 탄성 충돌), cả total momentum và kinetic energy được bảo toàn.

Trong va chạm không đàn hồi (Inelastic Collision / 비탄성 충돌), momentum vẫn bảo toàn nếu hệ isolated, nhưng kinetic energy chuyển sang internal energy, deformation, nhiệt, sound…

Va chạm hoàn toàn không đàn hồi (Perfectly Inelastic Collision / 완전 비탄성 충돌) là trường hợp các vật dính lại.

### Ví dụ hai vật dính nhau

`m_1` có velocity `v_1`, `m_2` ban đầu đứng yên. Sau collision dính nhau với `v_f`:

```math
m_1v_1=(m_1+m_2)v_f
```

suy ra:

```math
v_f=\frac{m_1}{m_1+m_2}v_1
```

Kinetic energy trước và sau không bằng nhau nói chung. Phần giảm không “biến mất” mà chuyển dạng.

## Tâm khối

Tâm khối (Center of Mass / 질량중심) là weighted average của vị trí theo mass:

```math
\vec R_{cm}=\frac{\sum_i m_i\vec r_i}{\sum_i m_i}
```

Với distribution liên tục:

```math
\vec R_{cm}=\frac{1}{M}\int \vec r\,dm
```

Tại sao khái niệm này mạnh? Bởi vì chuyển động của center of mass obey:

```math
M\vec A_{cm}=\vec F_{external}
```

Internal force có thể làm hệ biến dạng, quay, nổ, nhưng không tự accelerate center of mass của isolated system.

Nếu một người đứng trên skateboard ném một quả bóng về trước, người và skateboard lùi lại. Internal rearrangement bảo toàn center-of-mass motion.

## Rocket và hệ biến khối lượng

Tên lửa là trường hợp cần cẩn thận với `F=ma`. Khối lượng của rocket thay đổi do eject fuel. Conservation of momentum dẫn tới phương trình tên lửa Tsiolkovsky:

```math
\Delta v=v_e\ln\frac{m_0}{m_f}
```

Trong đó `v_e` là exhaust velocity tương đối với rocket, `m_0` mass ban đầu, `m_f` mass cuối.

Logarithm xuất hiện vì mỗi increment velocity đạt được bằng cách giảm một fraction của mass còn lại. Khi integration:

```math
\int \frac{dm}{m}=\ln m
```

Đây là connection giữa exponential/logarithmic structure và các quá trình multiplicative.

## Bài toán: recoil

Một súng và đạn ban đầu đứng yên. Nếu đạn mass `m` bay ra velocity `v`, súng mass `M` recoil velocity `V`:

```math
0=mv+MV
```

```math
V=-\frac{m}{M}v
```

Dấu âm thể hiện recoil ngược hướng. Vì `M` lớn hơn `m`, magnitude recoil velocity nhỏ hơn bullet velocity.

## Knowledge Connection: conservation như accounting invariant

Trong database transaction hay accounting system, một invariant là điều kiện phải giữ sau mọi thao tác hợp lệ. Momentum conservation hoạt động tương tự ở mức mô hình: internal transactions có thể chuyển momentum giữa components, nhưng total của isolated system không thay đổi.

Điểm khác biệt là conservation law không phải convention do con người thiết kế; nó là pattern thực nghiệm sâu gắn với symmetry của tự nhiên.

## Mental Model

> Momentum là “sổ cái chuyển động có hướng”. Force bên ngoài là dòng vào/ra của sổ cái đó. Internal interactions chỉ chuyển momentum giữa các phần của hệ. Khi boundary của hệ được chọn đúng, nhiều va chạm phức tạp trở thành bài toán accounting vector.

## Common Misconceptions

### “Momentum và kinetic energy là cùng một thứ”

Không. `p=mv` là vector và tuyến tính theo `v`; `K=mv²/2` là scalar và quadratic. Một hệ có total momentum bằng zero vẫn có kinetic energy lớn, như hai vật cùng mass chạy ngược hướng.

### “Momentum chỉ bảo toàn trong va chạm đàn hồi”

Sai. Momentum bảo toàn cho isolated system trong mọi loại collision; kinetic energy chỉ bảo toàn trong elastic collision.

## Knowledge Connection

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Thuyết tương đối hẹp](../07_relativity/00_special_relativity.md), [Lượng tử](../08_quantum/00_quantum_foundations.md).
