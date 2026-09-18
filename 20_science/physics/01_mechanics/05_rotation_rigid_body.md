# Chuyển động quay, torque và động lượng góc

## Từ chuyển động thẳng sang chuyển động quay

Chuyển động quay không cần một “bộ vật lý hoàn toàn mới”. Nhiều cấu trúc của translation có analog quay:

| Translation | Rotation |
|---|---|
| vị trí `x` | góc `\theta` |
| velocity `v` | angular velocity `\omega` |
| acceleration `a` | angular acceleration `\alpha` |
| mass `m` | moment of inertia `I` |
| force `F` | torque `\tau` |
| momentum `p` | angular momentum `L` |
| `K=mv²/2` | `K_{rot}=I\omega²/2` |

Sự tương tự này không phải coincidence. Nó phản ánh cách geometry của rotation biến đổi trạng thái.

## Góc và radian

Radian (Radian / 라디안) được định nghĩa:

```math
\theta=\frac{s}{r}
```

với `s` là arc length. Vì là tỉ số hai chiều dài, radian dimensionless. Nó là đơn vị tự nhiên của calculus vì:

```math
\frac{d}{d\theta}\sin\theta=\cos\theta
```

chỉ đúng trực tiếp khi `\theta` đo bằng radian.

## Angular velocity và acceleration

```math
\omega=\frac{d\theta}{dt}
```

```math
\alpha=\frac{d\omega}{dt}
```

Một điểm cách trục distance `r` có tangential speed:

```math
v=\omega r
```

và tangential acceleration:

```math
a_t=\alpha r
```

Nếu quay đều, vẫn có centripetal acceleration:

```math
a_c=\omega^2r
```

## Torque

Moment lực hay torque (Torque / 돌림힘, 토크):

```math
\vec\tau=\vec r\times\vec F
```

Độ lớn:

```math
\tau=rF\sin\theta
```

Tại sao lực đặt xa hinge dễ mở cửa hơn? Vì torque phụ thuộc lever arm. Cùng một force tạo hiệu ứng rotational lớn hơn nếu line of action xa trục.

## Moment of inertia

Moment quán tính (Moment of Inertia / 관성모멘트):

```math
I=\sum_i m_ir_i^2
```

hoặc:

```math
I=\int r^2\,dm
```

Mass đo resistance đối với translational acceleration; `I` đo resistance đối với angular acceleration. Nhưng `I` không chỉ phụ thuộc tổng mass mà còn cách mass phân bố so với axis.

Mass ở xa trục đóng góp theo `r²`, nên một hoop và disk cùng mass/radius có `I` khác nhau.

## Newton II cho rotation

Với rigid body quanh fixed axis:

```math
\sum\tau=I\alpha
```

Cấu trúc giống `F=ma`, nhưng `I` chứa geometry của mass distribution.

## Rotational kinetic energy

Mỗi mass element có speed `v_i=\omega r_i`:

```math
K=\sum_i\frac12m_i v_i^2
```

```math
=\sum_i\frac12m_i\omega^2r_i^2
```

```math
=\frac12\omega^2\sum_i m_ir_i^2
```

Do đó:

```math
K_{rot}=\frac12I\omega^2
```

Công thức không phải analog đoán mò; nó được derivation từ kinetic energy tuyến tính của từng phần tử.

## Angular momentum

Động lượng góc (Angular Momentum / 각운동량) của particle:

```math
\vec L=\vec r\times\vec p
```

Với rigid body quay quanh principal fixed axis:

```math
L=I\omega
```

Torque là rate of change:

```math
\vec\tau_{ext}=\frac{d\vec L}{dt}
```

Nếu external torque bằng zero:

```math
\vec L=constant
```

Một figure skater kéo tay vào làm `I` giảm, nên `\omega` tăng để `L` giữ nguyên. Không cần có “lực bí ẩn” tăng rotation; energy có thể thay đổi vì cơ thể thực hiện internal work khi kéo tay.

## Rolling without slipping

Một bánh xe lăn không trượt thỏa constraint:

```math
v_{cm}=\omega R
```

Total kinetic energy:

```math
K=\frac12Mv_{cm}^2+\frac12I_{cm}\omega^2
```

Do một phần energy đi vào rotation, vật lăn xuống dốc thường tăng translational speed chậm hơn một point mass trượt không ma sát cùng độ cao.

## Mental Model

Rotation không cần một “bộ công thức khác” tách biệt khỏi translation; nó là cùng logic state–rate–response nhưng với góc, angular velocity, torque và moment of inertia. Moment of inertia phụ thuộc cả khối lượng lẫn cách khối lượng phân bố quanh trục.

## Common Misconceptions

Moment of inertia không phải thuộc tính chỉ của vật mà còn phụ thuộc trục quay. Torque lớn không nhất thiết tạo angular acceleration lớn nếu moment of inertia cũng lớn.

## Knowledge Connection

**Nên hiểu trước:** [Động học](00_kinematics.md), [Năng lượng](03_work_energy_power.md).

**Liên hệ tiếp:** [Đối xứng và bảo toàn](../00_foundations/04_symmetry_conservation_scale.md).
