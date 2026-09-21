# Entropy, cơ học thống kê (Statistical Mechanics) và giới hạn của biến đổi năng lượng

## Định luật II: tại sao một số quá trình chỉ đi một chiều?

Định luật I chỉ nói năng lượng (energy) phải bảo toàn. Nó không cấm nhiệt (heat) tự chảy từ vật lạnh sang nóng nếu tổng (total) năng lượng vẫn đúng. Nhưng tự nhiên có arrow of spontaneous process.

Định luật II nhiệt động lực học (Second Law / 열역학 제2법칙) đưa entropy (Entropy / 엔트로피) vào:

```math
\Delta S_{universe}\ge 0
```

Equality cho lý tưởng (ideal) reversible process; `>` cho irreversible spontaneous process.

### Entropy là gì?

Trong thermodynamics reversible definition:

```math
dS=\frac{\delta Q_{rev}}{T}
```

Trong cơ học thống kê, Boltzmann quan hệ (relation):

```math
S=k_B\ln\Omega
```

`\Omega` là số microstates tương thích với macrostate.

Entropy không nên đơn giản hóa thành “độ hỗn loạn”. mô hình tư duy (Mental model) tốt hơn: entropy đo logarithm của số cách vi mô mà trạng thái vĩ mô có thể được realized. Macrostate có multiplicity lớn hơn overwhelmingly likely hơn vì có nhiều microstates tương ứng hơn.

## Tại sao khí tự lan ra nhưng không tự gom lại?

Giả sử `N` các phân tử (molecules) có xác suất gần `1/2` nằm ở mỗi nửa box. Xác suất tất cả tự nằm vào nửa trái ở một instant xấp xỉ:

```math
P\sim\left(\frac12\right)^N
```

Với `N` cỡ Avogadro, con số nhỏ đến mức về thực tế không quan sát được. vi mô (Microscopic) các định luật (laws) có thể gần time-reversible, nhưng statistical weight của high-entropy macrostates áp đảo.

Arrow of time vĩ mô vì vậy xuất hiện từ thống kê (statistics) và các điều kiện biên (boundary conditions), không cần một “lực entropy” đẩy hệ.

## nhiệt engine và giới hạn Carnot

Một nhiệt engine lấy nhiệt `Q_H` từ hot reservoir, tạo work `W`, và thải `Q_C` sang cold reservoir:

```math
W=Q_H-Q_C
```

Efficiency:

```math
\eta=\frac{W}{Q_H}=1-\frac{Q_C}{Q_H}
```

cực đại (Maximum) reversible Carnot efficiency giữa temperatures `T_H` và `T_C`:

```math
\eta_{Carnot}=1-\frac{T_C}{T_H}
```

Không thể đạt 100% nếu `T_C>0`. Đây không phải limitation của kỹ thuật (engineering) kém; nó là thermodynamic ràng buộc (constraint).

## Refrigerator và nhiệt pump

Tủ lạnh không “tạo lạnh”; nó dùng work để chuyển nhiệt từ cold region sang hot surroundings. Điều này không vi phạm second định luật (law) vì entropy generation và work input bù lại xu hướng tự nhiên.

Coefficient of performance không giống efficiency thông thường và có thể lớn hơn 1 vì output mục tiêu là nhiệt moved, không phải năng lượng created.

## tự do (Free) năng lượng

Ở hằng số (constant) nhiệt độ (temperature) và áp suất (pressure), Gibbs tự do năng lượng:

```math
G=H-TS
```

với enthalpy:

```math
H=U+PV
```

Spontaneous process ở fixed `T,P` có:

```math
\Delta G<0
```

Đây là cầu nối sâu sang hóa học (chemistry), chuyển pha (phase transition), batteries và biochemistry. `\Delta G` nén competition giữa năng lượng lowering và entropy increase dưới các ràng buộc (constraints) cụ thể.

## thông tin (Information) và entropy

Shannon entropy:

```math
H=-\sum_i p_i\log p_i
```

có cấu trúc toán gần statistical entropy. Cả hai đo spread/uncertainty qua phân bố xác suất (probability distribution), dù cách diễn giải (interpretation) vật lý và thông tin cần phân biệt.

Landauer's nguyên lý (principle) nối thông tin processing với thermodynamics: xóa một bit logic irreversibly có cực tiểu (minimum) nhiệt cost lý tưởng liên quan `k_BT\ln2`. điện toán (Computing) không hoàn toàn tách khỏi physics; thông tin phải được embodied trong vật lý (physical) các hệ (systems).

## Microstate, macrostate và Boltzmann entropy

cơ học thống kê (Thống kê cơ học / 통계역학) nối vi mô các định luật với thermodynamics bằng xác suất (probability). Một microstate mô tả chi tiết bậc tự do (degrees of freedom); một macrostate chỉ giữ vài đại lượng như `E,V,N`. Nếu `Ω` là số microstates tương thích với macrostate, Boltzmann cho

```math
S=k_B\ln\Omega.
```

Logarithm xuất hiện vì entropy của hai hệ độc lập phải cộng, trong khi số microstates nhân: `Ω_total=Ω_AΩ_B`, nên `ln Ω_total=lnΩ_A+lnΩ_B`.

## Boltzmann hệ số (factor)

Khi một subsystem trao đổi năng lượng với reservoir ở nhiệt độ `T`, xác suất của trạng thái (state) năng lượng `E_i` có dạng

```math
p_i\propto e^{-E_i/(k_BT)}.
```

năng lượng cao không “bị cấm”; nó chỉ ít probable hơn. nhiệt độ lớn làm phân bố (distribution) phẳng hơn, nghĩa là high-năng lượng các trạng thái (states) được populate đáng kể hơn.

## Partition function

Chuẩn hóa xác suất dẫn tới partition function

```math
Z=\sum_i e^{-\beta E_i},\qquad \beta=\frac{1}{k_BT}.
```

`Z` trông như một tổng kỹ thuật nhưng thực chất là phần tử sinh (generator) của thermodynamic thông tin. Từ `ln Z` có thể suy ra trung bình (average) năng lượng, tự do năng lượng, entropy và đáp ứng (response) functions. Đây là lý do cơ học thống kê biến “đếm các trạng thái” thành thermodynamics.

## Fluctuation không biến mất hoàn toàn

vĩ mô (Macroscopic) variables ổn định vì relative các thăng giáng (fluctuations) thường giảm xấp xỉ như `1/√N`. Với `N~10^23`, fluctuation fraction cực nhỏ, nhưng ở nano-thang (scale) chúng có thể quan trọng. Brownian chuyển động (motion), Johnson nhiễu (noise) và single-phân tử (molecule) biophysics đều làm ta nhìn thấy thống kê vi mô trực tiếp hơn.

## Mô hình tư duy (Mental Model)

> Nhiệt động lực học là khoa học của điều ta có thể biết và dự đoán khi không theo dõi từng vi trạng thái. năng lượng bảo toàn (conservation) nói “sổ cái tổng không mất”; entropy nói “trong số các cách giữ sổ cái đó, hệ gần như chắc chắn trôi về macrostate có nhiều cách vi mô hơn”.

## Những ngộ nhận thường gặp (Common Misconceptions)

### “Entropy luôn là hỗn loạn”

Từ “hỗn loạn” dễ gây sai. Một tinh thể (crystal) có entropy thấp hơn chất lỏng (liquid) ở cùng conditions vì số microstate khả dĩ hạn chế hơn, nhưng “trông có trật tự” chỉ là biểu hiện trực quan, không phải definition.

### “Second định luật nói năng lượng bị mất”

năng lượng không bị mất. Chất lượng hay khả năng chuyển toàn bộ năng lượng thành useful work giảm khi entropy tăng.

### “nhiệt và nhiệt độ là cùng một thứ”

nhiệt độ là trạng thái variable; nhiệt là năng lượng transfer do nhiệt độ độ chênh (difference).

## Liên kết kiến thức (Knowledge Connection)

**Nên hiểu trước:** [Thermodynamics](00_thermodynamics.md), [Probability và exponential](../00_foundations/03_mathematical_language.md).

**Liên hệ tiếp:** [Quantum statistics và chất rắn](../10_condensed_matter_devices/00_crystals_bands.md), [Information](../13_connections/00_knowledge_connections.md).
