# Enthalpy và nhiệt hóa học — hạch toán năng lượng phản ứng ở áp suất gần không đổi

> **Enthalpy (entanpi, \(H\) / 엔탈피)** là hàm trạng thái được định nghĩa bởi:

\[
H=U+PV
\]

Trong nhiều thí nghiệm hóa học diễn ra ở áp suất gần không đổi và chỉ có công áp suất–thể tích đáng kể, nhiệt trao đổi thỏa:

\[
q_P=\Delta H
\]

Đây là lý do enthalpy xuất hiện khắp hóa học: nó biến một bài toán “internal energy + expansion work” thành một state function thuận tiện hơn cho điều kiện phòng thí nghiệm và process engineering.

# Từ định luật thứ nhất tới enthalpy

Bắt đầu với:

\[
dU=\delta q-P_{ext}dV
\]

Nếu quá trình chỉ có PV work và diễn ra ở pressure gần constant, xét:

\[
H=U+PV
\]

nên:

\[
dH=dU+PdV+VdP
\]

Ở constant P:

\[
dP=0
\]

và với reversible/quasi-static PV work thích hợp:

\[
dH=\delta q_P
\]

Do đó:

\[
\Delta H=q_P
\]

Điều quan trọng là equality này có **điều kiện áp dụng**, không phải định nghĩa “enthalpy = heat”. Enthalpy là state function; heat là path function.

# Vì sao hạng PV xuất hiện?

Một system tồn tại trong surroundings ở pressure P phải “chiếm chỗ” bằng một volume V. Khi tạo gas hoặc làm system nở ra, một phần energy accounting liên quan việc đẩy surroundings.

Hạng \(PV\) kết hợp phần đó với U, khiến H đặc biệt thuận tiện cho constant-pressure chemistry.

Trong open-flow systems, fluid còn phải làm **flow work** để đi vào/ra control volume, nên enthalpy cũng xuất hiện tự nhiên trong energy balance của reactor, turbine và heat exchanger.

# Intensive và extensive

Enthalpy là **đại lượng dung lượng (extensive)**: nếu gấp đôi amount của cùng state, H gấp đôi.

**Enthalpy mol (molar enthalpy)**:

\[
h=\frac{H}{n}
\]

là intensive.

Do đó nếu nhân toàn chemical equation lên 2 lần, \(\Delta H\) reaction cũng nhân 2.

# Tỏa nhiệt và thu nhiệt

Nếu:

\[
\Delta H<0
\]

quá trình **tỏa nhiệt (exothermic / 발열)** ở constant pressure: system chuyển heat ra surroundings.

Nếu:

\[
\Delta H>0
\]

quá trình **thu nhiệt (endothermic / 흡열)**.

Nhưng sign của \(\Delta H\) không tự quyết định spontaneity. Cần cả entropy:

\[
\Delta G=\Delta H-T\Delta S
\]

Một endothermic dissolution vẫn có thể spontaneous nếu entropy contribution đủ thuận lợi.

# Enthalpy phản ứng

Với:

\[
\sum_i \nu_i A_i=0
\]

với \(\nu_i<0\) cho reactants và \(\nu_i>0\) cho products:

\[
\Delta_rH=\sum_i\nu_iH_i
\]

Ở standard state:

\[
\Delta_rH^\circ
=\sum_i\nu_i\Delta_fH_i^\circ
\]

nếu dùng enthalpy tạo thành chuẩn.

Reaction enthalpy luôn gắn với một equation cụ thể. Đảo reaction đổi dấu; nhân coefficients đổi magnitude.

# Định luật Hess — path independence

Vì H là state function, nếu:

\[
A\to B\qquad\Delta H_1
\]

và:

\[
B\to C\qquad\Delta H_2
\]

thì:

\[
A\to C\qquad
\Delta H=\Delta H_1+\Delta H_2
\]

Không có yêu cầu real mechanism phải đi qua B.

Hess law là chemical implementation của state-function property.

# Ví dụ Hess bằng combustion data

Giả sử muốn reaction enthalpy của:

\[
C(graphite)+\frac12O_2\to CO
\]

nhưng khó đo trực tiếp vì CO có thể tiếp tục oxidize.

Ta có thể dùng:

\[
C+O_2\to CO_2
\]

và:

\[
CO+\frac12O_2\to CO_2
\]

Lấy reaction đầu trừ reaction thứ hai sẽ cho target reaction.

Đây là sức mạnh thực tế của Hess: đo những pathways dễ đo rồi ghép để suy quantity khó đo.

# Enthalpy tạo thành chuẩn

**Enthalpy tạo thành chuẩn (standard enthalpy of formation, \(\Delta_fH^\circ\))** là enthalpy change khi tạo 1 mol compound từ các nguyên tố ở **trạng thái chuẩn tham chiếu**.

Theo convention:

\[
\Delta_fH^\circ=0
\]

cho element ở reference state của nó.

Ví dụ carbon graphite là reference state thông thường của C ở 298 K, không phải diamond.

Điều này là convention đặt mốc; không có nghĩa element “không có enthalpy”.

# Standard state không nghĩa STP

Trong thermodynamics, standard state thường dùng reference pressure 1 bar và một quy ước composition/activity cụ thể.

Nó không đồng nghĩa với “0 °C, 1 atm” của một số định nghĩa STP lịch sử.

Ký hiệu \(^\circ\) nói về **reference state**, không tự xác định temperature; temperature phải được nêu hoặc ngầm hiểu từ bảng dữ liệu, thường 298.15 K.

# Enthalpy cháy

**Enthalpy cháy (enthalpy of combustion)** là enthalpy change khi một substance cháy hoàn toàn theo products được quy định.

Ví dụ methane:

\[
CH_4(g)+2O_2(g)
\to CO_2(g)+2H_2O(l)
\]

State của water rất quan trọng. Nếu product là \(H_2O(g)\), \(\Delta H\) ít âm hơn vì chưa giải phóng latent heat của condensation.

Đây là nguyên nhân **higher heating value (HHV)** và **lower heating value (LHV)** khác nhau trong energy engineering.

# Nhiệt trị và đời sống

Khi nói một fuel “chứa nhiều năng lượng”, ý chính xác hơn là combustion reaction của fuel với oxidant tạo products có lower enthalpy/free energy và có thể chuyển chênh lệch đó thành heat/work.

Fuel không phải hộp chứa heat. Chemical energy là **relative state energy** của một chemical system gồm cả fuel và oxidant.

# Bond enthalpy — mô hình vi mô gần đúng

Phá một gas-phase bond:

\[
A-B(g)\to A(g)+B(g)
\]

cần **bond dissociation enthalpy (BDE)** dương.

Reaction enthalpy có thể estimate:

\[
\Delta H_{rxn}
\approx
\sum D(\text{bonds broken})
-
\sum D(\text{bonds formed})
\]

Nhưng average bond enthalpies:

- thường là gas-phase averages;
- phụ thuộc molecular environment;
- không capture solvation, ionic lattice, resonance đầy đủ.

Vì vậy dùng BDE để reasoning định tính hoặc estimate, không thay tabulated formation enthalpies khi cần accuracy cao.

# “Phá liên kết giải phóng năng lượng” vì sao sai?

Một stable bond tương ứng với energy minimum relative to separated fragments.

Muốn đi từ minimum lên fragments phải cung cấp energy.

Reaction tỏa nhiệt vì **new bonds/interactions formed giải phóng nhiều energy hơn energy cần phá old bonds**.

Đây là một misconception phổ biến cần sửa sớm vì nó ảnh hưởng cách hiểu ATP, combustion và metabolism.

# Calorimetry ở constant pressure

Trong coffee-cup calorimeter đơn giản:

\[
q_{solution}=mc\Delta T
\]

Nếu calorimeter gần isolated:

\[
q_{rxn}+q_{solution}+q_{cal}=0
\]

nên:

\[
q_{rxn}=-(q_{solution}+q_{cal})
\]

Với pressure gần constant:

\[
\Delta H_{rxn}\approx q_{rxn}
\]

cho amount reaction đã diễn ra.

Muốn report per mole reaction, chia cho extent tương ứng.

# Calorimeter constant

Không chỉ solution hấp thụ heat; cup, lid, probe và stirrer cũng có heat capacity.

Ta có thể calibrate:

\[
q_{cal}=C_{cal}\Delta T
\]

Bỏ calorimeter constant khi nó không nhỏ có thể tạo systematic bias.

# Bomb calorimeter: ΔU trước, ΔH sau

Bomb calorimeter gần constant volume:

\[
q_V=\Delta U
\]

Nếu reaction có gas stoichiometry change, có thể chuyển gần đúng:

\[
\Delta H=\Delta U+\Delta n_gRT
\]

cho ideal gases và cùng temperature.

Vì vậy combustion calorimetry minh họa trực tiếp distinction giữa U và H.

# Enthalpy chuyển pha

Các phase transitions có latent enthalpy:

\[
\Delta H_{fus},\quad
\Delta H_{vap},\quad
\Delta H_{sub}
\]

Hess cho:

\[
\Delta H_{sub}
=\Delta H_{fus}+
\Delta H_{vap}
\]

ở compatible states/temperatures.

Tại phase transition equilibrium:

\[
\Delta G_{tr}=0
\]

nên:

\[
\Delta S_{tr}=rac{\Delta H_{tr}}{T_{tr}}
\]

đây là cầu nối trực tiếp enthalpy → entropy → phase equilibrium.

# Enthalpy hòa tan

Khi solute tan, có nhiều contribution:

```text
phá tương tác solute–solute
+ phá/reorganize solvent–solvent
+ tạo solute–solvent interactions
```

Net:

\[
\Delta H_{soln}
\]

có thể dương hoặc âm.

Vì vậy “tan được” không đồng nghĩa “tỏa nhiệt”; dissolution spontaneity còn có entropy.

# Ionic dissolution — lattice vs hydration

Với ionic solid, có competition giữa:

- lattice disruption cost;
- ion hydration stabilization.

Ion nhỏ/charge cao thường có hydration enthalpy rất âm nhưng cũng có lattice energy lớn nếu solid counterion tương ứng.

Solubility không thể dự đoán chỉ bằng một trong hai terms.

# Enthalpy pha loãng

Diluting concentrated acid/base hoặc electrolyte có thể tỏa/thu heat vì solvation environment thay đổi.

Đây là lý do pha acid đậm đặc với nước có thể sinh nhiệt mạnh và cần thêm acid vào lượng nước lớn từ từ với cooling/control phù hợp.

Safety practice ở đây có nền thermochemistry rõ ràng.

# Kirchhoff — reaction enthalpy thay đổi theo temperature

Reaction enthalpy không hẳn constant với T.

\[
\left(\frac{d\Delta H}{dT}\right)_P
=\Delta C_P
\]

Do đó:

\[
\Delta H(T_2)
=
\Delta H(T_1)
+
\int_{T_1}^{T_2}\Delta C_PdT
\]

Nếu \(\Delta C_P\) gần constant:

\[
\Delta H(T_2)
\approx\Delta H(T_1)+
\Delta C_P(T_2-T_1)
\]

Điều này quan trọng khi extrapolate equilibrium/process data qua dải temperature rộng.

# Sensible heat và latent heat

**Nhiệt hiện (sensible heat)** làm temperature thay đổi trong cùng phase:

\[
q=\int C_PdT
\]

**Nhiệt ẩn (latent heat)** gắn với phase transition ở condition equilibrium.

Trong heating curve, temperature có thể gần constant trong transition dù system vẫn hấp thụ energy đáng kể.

Đây là ví dụ cho thấy heat input không nhất thiết làm temperature tăng ngay.

# Reaction enthalpy trong flow reactor

Trong steady-flow process, energy balance chứa molar enthalpy streams:

\[
\dot Q-\dot W_s
+\sum_{in}\dot n_i h_i
-\sum_{out}\dot n_i h_i=0
\]

nếu bỏ kinetic/potential changes.

Reaction heat release có thể làm reactor temperature tăng, từ đó rate constants tăng theo Arrhenius. Với exothermic reaction, coupling này có thể tạo thermal runaway.

Thermochemistry vì thế nối trực tiếp tới reactor safety.

# Thermal runaway

Nếu heat generation tăng với T nhanh hơn heat removal:

```text
T tăng
→ reaction nhanh hơn
→ sinh nhiệt nhanh hơn
→ T tăng thêm
```

feedback dương có thể dẫn runaway.

Đây là reason scale-up nguy hiểm: volume tăng theo \(L^3\), surface heat-transfer area theo \(L^2\).

Một reaction an toàn ở vial nhỏ không tự động an toàn ở reactor lớn.

# Enthalpy và battery

Cell reaction có enthalpy \(\Delta H\), nhưng maximum electrical work liên hệ \(\Delta G\).

Phần:

\[
T\Delta S=\Delta H-\Delta G
\]

liên hệ reversible heat với electrical work.

Battery thermal management vì thế phụ thuộc không chỉ ohmic heating mà còn entropy change của electrochemical reaction.

# Enthalpy và sinh học

Metabolism cuối cùng chuyển chemical free energy thành:

- work;
- gradients;
- biosynthesis;
- heat.

Calorimetry có thể đo heat production của organisms, nhưng heat release không bằng toàn bộ usable free energy vì Gibbs và enthalpy khác nhau.

Đây là lý do nutrition “calories” và biochemical free-energy coupling là hai cách nhìn liên quan nhưng không đồng nhất.

# Sai số và độ không đảm bảo trong thermochemistry

Một \(\Delta H\) experimental có uncertainty từ:

- mass/concentration;
- heat capacity;
- heat loss;
- thermometer calibration;
- incomplete reaction;
- evaporation;
- side reactions.

Nếu subtract hai large enthalpies để lấy một small difference, relative uncertainty của result có thể lớn.

Hess-law arithmetic không xóa experimental uncertainty.

# Những hiểu lầm thường gặp

### “Enthalpy là heat chứa trong system”

Không. H là state function; heat là transfer mode.

### “ΔH âm nghĩa reaction nhanh và spontaneous”

Không. Rate thuộc kinetics; spontaneity cần ΔG.

### “Phá bond giải phóng energy”

Không. Bond dissociation cần energy.

### “Standard state nghĩa 0 °C và 1 atm”

Không. Standard state là thermodynamic reference convention; temperature phải được nêu riêng.

### “Bond enthalpy cho exact reaction enthalpy”

Không. Nó thường là gas-phase average approximation.

## Mô hình tư duy

Enthalpy là **energy accounting optimized cho constant-pressure chemistry**:

```text
U + PV
→ H
→ reaction enthalpy
→ calorimetry / Hess / formation data
→ temperature correction / process energy balance
```

Nó trả lời “bao nhiêu heat tương ứng với state change dưới constraint thích hợp?”, nhưng muốn biết direction tự diễn ra phải thêm entropy và Gibbs.

Xem tiếp: [Entropy](./02_entropy.md).