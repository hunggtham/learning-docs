# Định luật Newton, quán tính và động lực học

## Vì sao cần khái niệm lực?

Kinematics cho biết vật chuyển động như thế nào. Dynamics (Dynamics / 동역학) hỏi vì sao trạng thái chuyển động thay đổi.

Trong trực giác đời thường, người ta dễ nghĩ “muốn vật tiếp tục chuyển động phải tiếp tục có lực”. Đây là trực giác hình thành từ thế giới có ma sát. Newton chỉ ra cấu trúc ngược lại: trạng thái tự nhiên của một vật cô lập không phải đứng yên, mà là giữ nguyên vận tốc.

## Định luật I Newton và quán tính

Định luật I Newton (Newton's First Law / 뉴턴 제1법칙, 관성의 법칙) nói rằng trong một inertial frame, nếu tổng lực bằng zero, vận tốc của vật không đổi.

```math
\sum \vec F=0 \Rightarrow \frac{d\vec v}{dt}=0
```

Quán tính (Inertia / 관성) là xu hướng duy trì trạng thái chuyển động. Khối lượng là thước đo định lượng mức “khó thay đổi vận tốc” của vật trong cơ học Newton.

Khi xe phanh gấp, cơ thể có xu hướng tiếp tục vận tốc cũ nên người bị lao về trước so với xe. Dây an toàn tạo lực để thay đổi momentum của cơ thể cùng với xe.

## Định luật II Newton

Dạng tổng quát:

```math
\sum \vec F=\frac{d\vec p}{dt}
```

với động lượng:

```math
\vec p=m\vec v
```

Nếu khối lượng không đổi:

```math
\sum \vec F=m\vec a
```

Đây là `F=ma` quen thuộc.

### Tại sao lực, khối lượng và gia tốc có quan hệ này?

Ta có thể nhìn `F` như định lượng tốc độ tương tác làm thay đổi momentum. Với cùng tổng lực, vật có khối lượng lớn thay đổi vận tốc chậm hơn vì cùng một thay đổi momentum tương ứng với thay đổi velocity nhỏ hơn:

```math
\Delta v=\frac{\Delta p}{m}
```

Vì vậy `m` đóng vai trò “inertial resistance”.

Đơn vị newton được định nghĩa để:

```math
1\,N=1\,kg\cdot m/s^2
```

Một lực 1 N tác dụng lên vật 1 kg tạo gia tốc `1 m/s²` nếu không có lực khác.

## Lực là tương tác, không phải tài sản của vật

Lực (Force / 힘) phát sinh do tương tác. Gravity là tương tác giữa mass-energy; lực điện giữa charge; normal force là tương tác điện từ vi mô giữa bề mặt; friction cũng bắt nguồn chủ yếu từ electromagnetic interaction và cấu trúc bề mặt.

Khi vẽ free-body diagram (자유물체도), ta chọn một vật và chỉ vẽ các lực tác dụng lên chính vật đó. Đây là kỹ thuật mô hình hóa, không phải trang trí bài giải.

## Định luật III Newton

Nếu vật A tác dụng lực lên B, B tác dụng lực ngược lại lên A:

```math
\vec F_{A\to B}=-\vec F_{B\to A}
```

Hai lực này không triệt tiêu nhau trên cùng một free-body diagram vì chúng tác dụng lên hai vật khác nhau.

Khi đi bộ, chân đẩy mặt đất về sau; mặt đất thông qua static friction đẩy người về trước. Không phải ta “tự đẩy cơ thể” bằng lực nội bộ; acceleration của center of mass cần external force.

## Hệ nhiều vật và constraint

Giả sử hai vật nối bằng dây. Dây không dãn tạo constraint hình học khiến acceleration của chúng có quan hệ. Vật lý của pulley problem thực chất là kết hợp:

1. Newton II cho từng vật.
2. Quan hệ constraint do dây.
3. Assumption về dây và pulley.

Đây là pattern rất chung trong mechanics và engineering: equation of motion + constraint equation.

## Force field và mô hình local

Một field (Field / 장) gán giá trị vật lý cho mỗi điểm trong không gian và thời gian. Gravitational field `\vec g(\vec r)` cho biết acceleration mà một test mass sẽ nhận tại vị trí đó. Electric field làm điều tương tự cho force per charge.

Field cho phép ta tách “source tạo môi trường tương tác” khỏi “test object phản ứng với môi trường”. Đây sẽ là mental model trung tâm của electromagnetism.

## Mental Model

Newton II không nói rằng “lực tạo ra vận tốc”; nó nói net force quyết định tốc độ thay đổi của momentum. Vận tốc có thể tồn tại mà không cần lực duy trì, còn lực chỉ cần khi momentum phải đổi.

## Common Misconceptions

Một vật đang chuyển động không cần một lực “đẩy về phía trước” nếu tổng lực bằng không. Cặp action–reaction không triệt tiêu nhau trên cùng một vật vì chúng tác dụng lên hai vật khác nhau.

## Knowledge Connection

**Nên hiểu trước:** [Động học](00_kinematics.md).

**Liên hệ tiếp:** [Các lực thường gặp](02_common_forces.md), [Động lượng](04_momentum_collisions.md).
