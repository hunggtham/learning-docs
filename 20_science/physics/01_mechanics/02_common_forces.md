# Các lực thường gặp: trọng lực, pháp tuyến, ma sát, dây, lò xo và lực cản

## Trọng lực gần mặt đất

Trọng lực tác dụng lên vật khối lượng `m`:

```math
\vec F_g=m\vec g
```

Dùng Newton II:

```math
m\vec a=m\vec g
```

rút gọn `m`:

```math
\vec a=\vec g
```

Đây là lý do mọi vật có cùng free-fall acceleration trong model không drag.

## Lực pháp tuyến

Lực pháp tuyến (Normal Force / 수직항력) là lực tiếp xúc vuông góc bề mặt. Nó không mặc định bằng `mg`.

Một vật đặt yên trên sàn ngang không có acceleration theo phương đứng:

```math
N-mg=0 \Rightarrow N=mg
```

Nhưng trong thang máy tăng tốc lên:

```math
N-mg=ma
```

nên:

```math
N=m(g+a)
```

Cân đo `N`, không đo trực tiếp `mg`; vì vậy ta cảm thấy “nặng hơn” khi thang máy tăng tốc lên.

## Ma sát

Ma sát tĩnh (Static Friction / 정지 마찰력) điều chỉnh để chống xu hướng trượt đến một giá trị tối đa:

```math
f_s\le \mu_sN
```

Không phải lúc nào cũng bằng `\mu_sN`.

Ma sát trượt (Kinetic Friction / 운동 마찰력) trong mô hình đơn giản:

```math
f_k=\mu_kN
```

và hướng ngược chuyển động tương đối của hai bề mặt.

Tại sao cần friction để chạy? Khi chân chạm đất mà không trượt, static friction từ mặt đất có thể đẩy cơ thể về trước. Băng trơn có `\mu_s` nhỏ nên lực ngang tối đa nhỏ, khó tạo acceleration.

Mô hình Coulomb friction này là gần đúng. Ở hệ thật, ma sát phụ thuộc vật liệu, nhiệt độ, tốc độ, độ nhám, lubrication và deformation.

## Lực căng dây

Lực căng (Tension / 장력) là lực do dây, cáp hoặc rope kéo dọc theo chiều của nó. Trong dây lý tưởng không khối lượng, không giãn và qua pulley lý tưởng, tension thường được coi như nhau trên toàn dây. Nếu pulley có moment quán tính hoặc dây có mass, assumption này có thể hỏng.

## Lực đàn hồi Hooke

Với lò xo gần vị trí cân bằng:

```math
F=-kx
```

Trong đó `k` là độ cứng (spring constant / 용수철 상수), đơn vị `N/m`, và dấu âm cho biết lực phục hồi ngược hướng displacement.

Hooke law là linear approximation. Nếu kéo quá xa, vật liệu có thể phi tuyến hoặc vượt giới hạn đàn hồi.

## Lực cản và terminal velocity

Trong chất lưu, drag thường tăng theo tốc độ. Ở tốc độ thấp có thể gần tuyến tính:

```math
F_d\propto v
```

Ở nhiều tình huống khí động đời thường:

```math
F_d\approx \frac12\rho C_dAv^2
```

Trong đó `\rho` là mật độ chất lưu, `C_d` hệ số cản, `A` diện tích cản.

Khi rơi, gravity kéo xuống còn drag tăng theo speed. Terminal velocity xảy ra khi:

```math
mg=F_d
```

khi đó tổng lực bằng zero và acceleration về zero dù vật vẫn đang rơi với vận tốc khác zero.

## Mặt phẳng nghiêng như phép chiếu vector

Trên mặt phẳng nghiêng góc `\theta`, ta chọn trục song song và vuông góc mặt phẳng. Trọng lực có thành phần:

```math
mg\sin\theta
```

dọc mặt phẳng và:

```math
mg\cos\theta
```

vuông góc.

Không có lực mới xuất hiện; ta chỉ đang chiếu cùng vector `m\vec g` lên basis phù hợp. Đây là lý do kỹ năng vector quan trọng hơn ghi nhớ công thức riêng cho mỗi hình vẽ.

## Bài toán mẫu: kéo hộp trên sàn có ma sát

Một hộp `m=10 kg`, `\mu_k=0.2`, kéo ngang bằng `F=30 N`. Lấy `g=9.8 m/s²`.

Theo phương đứng không acceleration:

```math
N=mg=98\,N
```

Ma sát trượt:

```math
f_k=\mu_kN=19.6\,N
```

Tổng lực ngang:

```math
F_{net}=30-19.6=10.4\,N
```

Gia tốc:

```math
a=\frac{F_{net}}{m}=1.04\,m/s^2
```

Insight quan trọng: `30 N` không tạo trực tiếp acceleration `3 m/s²` vì đó không phải net force. Dynamics luôn quan tâm tổng vector của mọi tương tác bên ngoài.

## Mental Model

Tên gọi của lực cho biết cơ chế tương tác hoặc constraint, không phải “loại chuyển động”. Bước cốt lõi khi giải bài là cô lập vật, vẽ mọi tương tác thực sự lên nó rồi chiếu vector lên các trục thích hợp.

## Knowledge Connection

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md).

**Liên hệ tiếp:** [Đàn hồi vật liệu](07_statics_elasticity_materials.md).
