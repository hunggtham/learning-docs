# Cân bằng, ứng suất (stress)–biến dạng tương đối (strain), đàn hồi và cơ học vật liệu

## Đứng yên không có nghĩa “không có lực”

Tĩnh học (Statics / 정역학) nghiên cứu hệ có gia tốc tuyến tính và gia tốc góc (angular acceleration) bằng không (zero). Điều kiện cân bằng (equilibrium) của cứng tuyệt đối (rigid) body:

```math
\sum\vec F=0
```

và:

```math
\sum\vec\tau=0
```

Hai điều kiện cần đồng thời. Một pair các lực (forces) equal-and-opposite có thể cho hợp lực (net force) không nhưng vẫn tạo mômen lực (torque) nếu lines of tác dụng (action) khác nhau.

Cầu, bàn, cần cẩu, xương và structural hệ quy chiếu (frame) đều có thể đứng yên trong khi bên trong (internal) ứng suất rất lớn.

## trọng tâm (Center of gravity) và độ ổn định (stability)

Trong approximately uniform gravitational trường (field), trọng tâm gần tâm khối (center of mass). Một vật thể (object) resting trên mặt đỡ (support) ổn định khi vertical projection của tâm khối nằm trong đa giác đỡ (support polygon) trong simple cứng tuyệt đối mô hình (model).

Nếu projection vượt boundary, hấp dẫn (gravity) tạo mômen lực làm vật thể tip.

Đó là lý do lowering tâm khối và widening base tăng độ ổn định. Robot walking và vehicle rollover analysis đều dựa trên generalized versions của idea này.

## cứng tuyệt đối body chỉ là xấp xỉ (approximation)

Không vật nào hoàn toàn cứng tuyệt đối. lực (Force) làm các nguyên tử (atoms) lệch khỏi cân bằng spacing, tạo biến dạng (deformation). Với small biến dạng, nhiều vật liệu (material) đáp ứng (response) gần tuyến tính (linear).

ứng suất (Ứng suất / Stress / 응력) đo bên trong lực per area. Normal ứng suất:

```math
\sigma=\frac{F_\perp}{A}
```

ứng suất cắt (Shear stress):

```math
\tau=\frac{F_\parallel}{A}
```

ứng suất không phải bên ngoài (external) áp suất (pressure) đơn giản; trong 3D nó là tensor vì lực direction trên một bề mặt (surface) phụ thuộc orientation của bề mặt.

## biến dạng tương đối

Biến dạng tương đối (Strain / 변형률) là dimensionless measure.

Normal biến dạng tương đối:

```math
\varepsilon=\frac{\Delta L}{L_0}
```

Shear biến dạng tương đối đo angular distortion.

ứng suất nói bên trong loading cường độ (intensity); biến dạng tương đối nói hình học (geometry) đáp ứng.

## Young's modulus

Trong tuyến tính miền đàn hồi (elastic regime):

```math
\sigma=E\varepsilon
```

`E` là Young's modulus (영률), đơn vị Pa.

`E` lớn nghĩa vật liệu stiff: cần ứng suất lớn để tạo cùng biến dạng tương đối. độ cứng (Stiffness) không đồng nghĩa độ bền (strength). Glass có thể stiff nhưng giòn (brittle); cao su (rubber) có low Young modulus nhưng chịu biến dạng tương đối lớn.

## Hooke định luật (law) như cục bộ (local) xấp xỉ của interatomic thế (potential)

Ở vi mô (microscopic) thang (scale), các nguyên tử trong chất rắn (solid) có cân bằng spacing `r_0` tại cực tiểu (minimum) thế `U(r)`.

Gần cực tiểu:

```math
U(r)\approx U(r_0)+\frac12k(r-r_0)^2
```

nên lực:

```math
F=-\frac{dU}{dr}\approx-k(r-r_0)
```

vĩ mô (Macroscopic) elasticity vì vậy có nguồn gốc từ cục bộ độ cong (curvature) của interatomic năng lượng (energy) landscape. tuyến tính elasticity là họa âm (harmonic) xấp xỉ ở tập thể (collective) thang.

## Poisson ratio

Kéo một thanh dài ra thường làm nó co ngang. Poisson ratio:

```math
\nu=-\frac{\varepsilon_{transverse}}{\varepsilon_{axial}}
```

Nó mô tả coupling giữa biến dạng tương đối directions. vật liệu gần incompressible như cao su có `\nu` gần `0.5` trong lý tưởng (ideal) đẳng hướng (isotropic) limit.

## Bulk modulus

Bulk modulus:

```math
K=-V\frac{dP}{dV}
```

đo điện trở (resistance) đối với uniform compression. `K` lớn nghĩa khó thay đổi thể tích (volume).

tốc độ (Speed) of âm thanh (sound) trong môi trường (medium) phụ thuộc đàn hồi (elastic) độ cứng và mật độ (density); ví dụ chất lưu (fluid):

```math
c_s\sim\sqrt{\frac{K}{\rho}}
```

cho thấy sóng (wave) sự lan truyền (propagation) là competition giữa restoring độ cứng và inertia.

## đàn hồi, plastic và phá hủy (failure)

Trong miền đàn hồi, bỏ tải (load) thì vật gần trở lại hình dạng (shape) cũ. Qua điểm chảy (yield point), biến dạng dẻo (plastic deformation) có thể vĩnh viễn (permanent) do dislocation chuyển động (motion) và microstructural rearrangement.

Ultimate độ bền, fracture độ dai (toughness) và fatigue là các concepts khác nhau:

- độ bền: ứng suất trước khi yield/fail theo criterion;
- độ dai: khả năng absorb năng lượng trước fracture;
- hardness: điện trở to localized biến dạng dẻo/scratch;
- fatigue: phá hủy dưới cyclic loading có thể xảy ra ở ứng suất thấp hơn tĩnh (static) độ bền.

Không thể nói một vật liệu “mạnh hơn” chỉ bằng một con số mà không nói phá hủy mode (mode) và environment.

## uốn (Bending) dầm (beam)

Khi dầm bend, một side chịu lực căng (tension), side kia compression, giữa có trục trung hòa (neutral axis). uốn ứng suất trong Euler–Bernoulli dầm mô hình:

```math
\sigma=\frac{My}{I}
```

`M` là uốn mômen (moment), `y` khoảng cách (distance) khỏi trục trung hòa, `I` second mômen of area.

Ở đây `I` không phải khối lượng (mass) mômen quán tính (moment of inertia). Nó là geometric area mômen:

```math
I=\int y^2dA
```

vật liệu đặt xa trục trung hòa tăng uốn độ cứng rất hiệu quả. Đây là lý do I-dầm đưa nhiều vật liệu ra xa center thay vì làm chất rắn rectangle cùng khối lượng.

## mất ổn định uốn dọc (Buckling): phá hủy không cần vật liệu bị nghiền

Một slender column chịu compression có thể mất độ ổn định và buckle. Euler critical tải cho lý tưởng pinned column:

```math
P_{cr}=\frac{\pi^2EI}{L^2}
```

Điều đáng chú ý là tải critical phụ thuộc `1/L²`; column dài hơn dễ buckle mạnh. phá hủy ở đây là sự mất ổn định (instability) của hình học, không nhất thiết ứng suất vượt vật liệu crushing độ bền.

## áp suất vessels

Thin-walled cylindrical vessel có hoop ứng suất xấp xỉ:

```math
\sigma_h=\frac{Pr}{t}
```

và longitudinal ứng suất:

```math
\sigma_l=\frac{Pr}{2t}
```

Nên hoop ứng suất gấp đôi longitudinal trong mô hình. Tank, pipe và blood vessel có related ứng suất structures, dù biological tissue phi tuyến (nonlinear)/anisotropic hơn.

## giãn nở nhiệt (Thermal expansion)

Nhiệt làm trung bình (average) interatomic separation thay đổi vì thế không đối xứng hoàn hảo quanh cực tiểu.

tuyến tính giãn nở nhiệt:

```math
\Delta L=\alpha L_0\Delta T
```

Nếu sự giãn nở (expansion) bị ràng buộc (constraint), nhiệt (thermal) ứng suất phát sinh. Railway tracks, bridges, PCB, chip packaging và độ chụm (precision) instruments phải account giãn nở nhiệt mismatch.

## Fracture và ứng suất concentration

Crack tip làm cục bộ ứng suất amplify. Một small defect có thể quyết định phá hủy dù trung bình ứng suất thấp.

Fracture cơ học (mechanics) dùng ứng suất cường độ hệ số (factor) `K_I` và fracture độ dai `K_{IC}` trong suitable tuyến tính-đàn hồi khung lý thuyết (framework).

kỹ thuật (Engineering) design vì vậy không chỉ hỏi vật liệu độ bền danh định (nominal strength); còn hỏi flaw size, hình học, tải tuần hoàn (cyclic load), nhiệt độ (temperature), corrosion và biến thiên sản xuất (manufacturing variability).

## vật liệu composite (Composite) và dị hướng (anisotropy)

vật liệu composite vật liệu kết hợp constituents để có properties không vật liệu đơn lẻ nào cung cấp. Carbon sợi (fiber) vật liệu composite rất stiff/strong dọc sợi nhưng dị hướng (anisotropic).

Tensor mô tả (description) cần thiết vì đáp ứng phụ thuộc direction. tinh thể (Crystal) điện (electrical)/thermal/mechanical properties cũng có dị hướng.

## MEMS và cảm biến (sensor)

Micro-electromechanical các hệ (systems) (MEMS / 미세전자기계시스템) dùng beams, springs, proof masses và capacitive/piezoresistive sensing ở microscale.

điện thoại thông minh (Smartphone) cảm biến gia tốc (accelerometer) thường đo độ dịch chuyển (displacement) của khối lượng thử (proof mass) under inertial lực. Từ `F=ma`, spring đáp ứng và thay đổi điện dung (capacitance change), electronics suy ra (infer) gia tốc (acceleration).

Vậy một app đọc cảm biến gia tốc thực ra đứng trên chuỗi physics: cơ học → elasticity → electrostatics → analog electronics → ADC → software.

## Mô hình tư duy (Mental Model)

> “Vật đứng yên” chỉ nói gia tốc bằng không, không nói bên trong các tương tác (interactions) bằng không. Structural cơ học là bài toán cân bằng lực/torque cộng với việc vật liệu biến dạng để tạo bên trong ứng suất. cứng tuyệt đối body là abstraction đầu tiên; elasticity cho biết abstraction đó bắt đầu hỏng như thế nào.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Cứng, bền, dai là cùng một tính chất”

Không. độ cứng, độ bền và độ dai trả lời ba câu hỏi khác nhau: khó biến dạng đến đâu, chịu ứng suất đến đâu, và absorb năng lượng trước fracture đến đâu.

### “Nếu ứng suất nhỏ hơn breaking độ bền thì dùng mãi không sao”

Cyclic fatigue, creep, corrosion và flaws có thể gây phá hủy theo thời gian ở ứng suất thấp hơn tĩnh phá hủy value.

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Định luật Newton](01_newton_laws_dynamics.md), [Các lực thường gặp](02_common_forces.md).

**Liên hệ tiếp:** [Chất rắn và crystal](../10_condensed_matter_devices/00_crystals_bands.md).
