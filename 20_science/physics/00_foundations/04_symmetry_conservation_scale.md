# Đối xứng, bảo toàn, xấp xỉ và thang đo

## Symmetry và conservation: một connection sâu

Đối xứng (Symmetry / 대칭성) nghĩa là ta thay đổi một khía cạnh mô tả mà quy luật vẫn giữ nguyên. Trong vật lý hiện đại, đối xứng liên hệ sâu với định luật bảo toàn qua định lý Noether.

Nếu các định luật không thay đổi theo thời gian, năng lượng được bảo toàn. Nếu chúng không phụ thuộc vị trí tuyệt đối trong không gian, động lượng tuyến tính được bảo toàn. Nếu không phụ thuộc hướng quay tuyệt đối, động lượng góc được bảo toàn.

Ta chưa cần chứng minh định lý Noether ở đây, nhưng mental model rất quan trọng: conservation law không phải những “mẹo giải bài”. Chúng phản ánh sự đồng nhất sâu của tự nhiên.

## 5. Symmetry → Conservation

Noether theorem formalizes:

- time-translation symmetry → energy conservation;
- space-translation symmetry → linear momentum conservation;
- rotational symmetry → angular momentum conservation.

Điều này thay đổi cách nhìn conservation law. Chúng không phải ba công thức tình cờ độc lập; chúng là shadows của spacetime symmetries.

Trong particle physics, internal gauge symmetries cũng organize interactions và conserved charges.

## 15. Approximation là một phần của theory, không phải lỗi

Một chuỗi model điển hình:

```text
real system
→ isolate subsystem
→ identify dominant effects
→ choose small parameter
→ neglect higher-order terms
→ solve approximate model
→ estimate error / regime
```

Ví dụ:

```math
\sin\theta\approx\theta
```

chỉ khi `|\theta|\ll1` rad.

```math
\gamma\approx1+\frac12\frac{v^2}{c^2}
```

chỉ khi `v\ll c`.

Ideal gas chỉ tốt ở density/interaction regimes phù hợp.

Physics maturity không phải tránh approximation; là biết mình approximate cái gì, controlled parameter là gì và error có thể lớn ở đâu.

## 16. Scale và effective theory

Ta không giải smartphone bằng Standard Model của quarks. Không phải vì Standard Model sai, mà vì description đó quá microscopic và không hữu ích.

Mỗi scale có effective degrees of freedom:

```text
quarks/gluons
↓
nucleons
↓
nuclei + electrons
↓
atoms/molecules
↓
materials
↓
devices
↓
circuits
↓
computers/software
```

Mỗi layer compresses lower-level complexity thành parameters: mass, charge, dielectric constant, resistance, threshold voltage, timing constraints…

Đây là cùng abstraction principle trong Software Engineering. Một API không cần expose transistor physics, nhưng hardware abstraction cuối cùng vẫn bị physics giới hạn bởi latency, heat, noise và energy.

## 14. Dimensionless numbers: physics không quan tâm đơn vị bạn chọn

Reynolds number:

```math
Re=\frac{\rho vL}{\mu}
```

Mach number:

```math
Ma=\frac{v}{c_s}
```

Relativistic ratio:

```math
\beta=\frac{v}{c}
```

Quantum/classical regimes thường so action scale với `\hbar`.

Dimensionless ratios quyết định regime. Một con cá nhỏ và tàu lớn có cùng shape nhưng flow behavior không giống nếu Reynolds number khác.

Trong engineering simulation, similarity requires matching relevant dimensionless parameters, không chỉ geometry scale.

## Mental Model

Đối xứng cho biết điều gì không thay đổi khi ta thay cách nhìn; bảo toàn cho biết đại lượng nào không đổi khi hệ tiến hóa. Scale cho biết chi tiết nào còn quan trọng. Hai ý tưởng này giúp ta quyết định nên giữ gì và bỏ gì trong một model.

## Knowledge Connection

**Nên hiểu trước:** [Tư duy Vật lý](00_physical_thinking.md).

**Liên hệ tiếp:** [Lagrange và Hamilton](../01_mechanics/08_analytical_mechanics.md).
