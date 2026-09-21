# Năng lượng hoạt hóa và phương trình Arrhenius — nhiệt độ làm tốc độ thay đổi như thế nào?

> **Năng lượng hoạt hóa (activation energy, \(E_a\) / 활성화 에너지)** là tham số mô tả mức độ nhạy của hằng số tốc độ với nhiệt độ trong khuôn khổ Arrhenius. Nó liên quan tới hàng rào mà hệ phải vượt qua trên con đường từ chất phản ứng tới sản phẩm, nhưng không nên đồng nhất máy móc với “năng lượng phản ứng” hay một độ cao hình học duy nhất trong mọi cơ chế.

Đây là chương nối ba ý tưởng: phân bố năng lượng của một quần thể phân tử, hàng rào phản ứng và tốc độ quan sát được.

# Vì sao một phản ứng thuận lợi vẫn có thể rất chậm?

Nếu:

\[
\Delta G<0
\]

sản phẩm thuận lợi hơn về nhiệt động ở điều kiện đang xét. Tuy nhiên để chuyển từ cấu trúc ban đầu sang cấu trúc cuối, hệ phải tái phân bố electron và hạt nhân. Con đường này thường đi qua những cấu hình có năng lượng tự do cao hơn cả reactant lẫn product.

Xăng và oxygen là ví dụ quen thuộc. Cháy hydrocarbon rất thuận lợi về nhiệt động, nhưng hỗn hợp không tự bốc cháy ngay ở nhiệt độ phòng vì bước khởi đầu có barrier lớn. Tia lửa hoặc nhiệt tạo đủ population reactive để chain chemistry bắt đầu.

Do đó:

```text
ΔG phản ứng → chênh lệch trạng thái đầu/cuối
barrier → độ khó của con đường
```

Hai đại lượng trả lời hai câu hỏi khác nhau.

# Phương trình Arrhenius

Quan hệ thực nghiệm kinh điển:

\[
k=Ae^{-E_a/(RT)}
\]

Trong đó:

- \(k\): hằng số tốc độ;
- \(A\): **hệ số tiền hàm mũ (pre-exponential factor)**;
- \(E_a\): năng lượng hoạt hóa Arrhenius;
- \(R\): hằng số khí;
- \(T\): nhiệt độ tuyệt đối.

Điểm quan trọng nằm ở số mũ. Khi \(T\) tăng, giá trị âm \(-E_a/(RT)\) trở nên ít âm hơn nên \(k\) có thể tăng rất mạnh.

Đây là lý do chênh vài chục độ có thể làm tốc độ phản ứng khác nhau nhiều lần, dù năng lượng trung bình của mỗi phân tử chỉ thay đổi tương đối vừa phải.

# Logarithm biến quan hệ mũ thành đường gần thẳng

Lấy log tự nhiên:

\[
\ln k=\ln A-\frac{E_a}{R}\frac1T
\]

Nếu \(A\) và \(E_a\) gần hằng trong khoảng nhiệt độ xét, đồ thị:

\[
\ln k\;vs\;1/T
\]

có slope:

\[
-\frac{E_a}{R}
\]

Từ slope thực nghiệm có thể suy \(E_a\).

Nhưng “đường Arrhenius gần thẳng” là một quan sát cần kiểm tra, không phải giả định đúng cho mọi khoảng nhiệt độ.

# Quan hệ hai nhiệt độ

Loại \(A\) giữa hai nhiệt độ:

\[
\ln\frac{k_2}{k_1}
=-\frac{E_a}{R}
\left(\frac1{T_2}-\frac1{T_1}\right)
\]

Công thức này hữu ích khi biết \(k\) ở một nhiệt độ và muốn ước lượng ở nhiệt độ khác trong cùng vùng cơ chế.

## Ví dụ định tính

Nếu \(E_a\) lớn, cùng một thay đổi nhiệt độ tạo thay đổi \(k\) lớn hơn. Vì thế phản ứng có barrier cao thường nhạy nhiệt hơn phản ứng có barrier thấp trong khung Arrhenius.

Điều này cũng giải thích vì sao tăng nhiệt không chỉ “làm mọi phản ứng nhanh hơn như nhau”; các pathways cạnh tranh có thể tăng với mức khác nhau và selectivity có thể thay đổi.

# Vì sao quy tắc “tăng 10 °C thì tốc độ gấp đôi” không phải định luật?

Nếu \(E_a\), \(T\) và mechanism khác nhau, ratio \(k(T+10)/k(T)\) cũng khác nhau.

Quy tắc này chỉ là **quy tắc kinh nghiệm (heuristic)** trong một số hệ sinh học hoặc hóa học ở một vùng nhiệt độ. Dùng nó ngoài phạm vi kiểm chứng có thể sai lớn.

# Hệ số tiền hàm mũ A có ý nghĩa gì?

Một giải thích quá đơn giản thường gọi \(A\) là “tần suất va chạm”. Điều này chỉ đúng một phần trong một số mô hình pha khí.

\(A\) còn chứa thông tin về:

- khả năng hai reactants gặp nhau;
- orientation;
- degrees of freedom;
- solvent cage;
- entropy của activated configuration;
- cơ chế reaction.

Do đó hai reactions có cùng \(E_a\) vẫn có thể có tốc độ rất khác nếu \(A\) khác mạnh.

# Arrhenius và phân bố Boltzmann

Một trực giác quan trọng là quần thể phân tử không có cùng một năng lượng. Chúng phân bố trên nhiều trạng thái.

Xác suất của trạng thái năng lượng cao giảm gần theo factor Boltzmann:

\[
p\propto e^{-E/(RT)}
\]

Khi nhiệt độ tăng, phần population có khả năng tiếp cận vùng năng lượng cao tăng rất mạnh. Đây là nguồn gốc trực giác của số hạng mũ trong Arrhenius.

Tuy nhiên reaction coordinate không chỉ là “một phân tử có đủ kinetic energy”. Nó còn gồm orientation, solvation và collective coordinates, nên transition-state theory cho bức tranh sâu hơn.

# Lý thuyết trạng thái chuyển tiếp

**Lý thuyết trạng thái chuyển tiếp (transition-state theory, TST)** mô tả reactants và activated configuration bằng cân bằng thống kê gần đúng.

Phương trình Eyring:

\[
k=\kappa\frac{k_BT}{h}
e^{-\Delta G^\ddagger/(RT)}
\]

với \(\kappa\) là hệ số truyền gần 1 trong mô hình đơn giản.

Vì:

\[
\Delta G^\ddagger
=\Delta H^\ddagger-T\Delta S^\ddagger
\]

nên:

\[
k
=\kappa\frac{k_BT}{h}
e^{\Delta S^\ddagger/R}
e^{-\Delta H^\ddagger/(RT)}
\]

Công thức này làm rõ rằng barrier có hai thành phần:

```text
ΔH‡ → chi phí năng lượng/enthalpy
ΔS‡ → mức độ hiếm của cấu hình có tổ chức cần thiết
```

# Entropy hoạt hóa — phản ứng có thể chậm vì phải “xếp đúng tư thế”

Hai phân tử có thể va chạm rất nhiều nhưng chỉ một fraction nhỏ có geometry phù hợp để reaction coordinate tiến tới transition state.

Nếu activated complex đòi hỏi hai phân tử mất nhiều tự do tịnh tiến/quay, \(\Delta S^\ddagger\) có thể âm đáng kể, làm \(k\) nhỏ hơn.

Điều này đặc biệt quan trọng trong association reactions, enzyme binding và supramolecular chemistry.

# Quan hệ giữa Arrhenius Ea và Eyring parameters

\(E_a\) và \(\Delta H^\ddagger\) liên quan nhưng không hoàn toàn giống nhau. Với một elementary process đơn giản ở pha phù hợp, thường có relation gần:

\[
E_a\approx\Delta H^\ddagger+RT
\]

Do đó không nên thay ký hiệu này cho ký hiệu kia mà không xem model đang dùng.

Arrhenius là mô hình thực nghiệm rất mạnh; Eyring cung cấp diễn giải nhiệt động–thống kê sâu hơn.

# Activation free energy quyết định tốc độ theo hàm mũ

Từ Eyring:

\[
k\propto e^{-\Delta G^\ddagger/(RT)}
\]

một chênh lệch nhỏ trong \(\Delta G^\ddagger\) có thể tạo ratio tốc độ rất lớn.

Ở nhiệt độ phòng, thay đổi barrier chỉ vài kJ/mol đã có thể thay tốc độ nhiều lần. Đây là lý do catalyst hoặc substituent thay đổi rất nhỏ về electronic structure vẫn có thể làm reaction dramatically faster/slower.

# Chất xúc tác làm gì với barrier?

Catalyst mở một network các elementary steps mới có barrier hiệu dụng thấp hơn.

Nó không thay đổi:

\[
\Delta G_{reaction}
\]

và vì vậy không thay equilibrium constant của cùng overall reaction.

Catalyst tăng tốc cả forward và reverse routes tương thích với microscopic reversibility, giúp hệ đạt equilibrium nhanh hơn.

# Reaction coordinate có thể có nhiều barrier

Một phản ứng nhiều bước có profile:

```text
R → TS1 → I1 → TS2 → I2 → TS3 → P
```

Không tồn tại một \(E_a\) duy nhất theo nghĩa cấu trúc cơ bản nếu nhiều steps cùng kiểm soát. Giá trị Arrhenius fit được từ overall rate là **apparent activation energy** và có thể là combination của nhiều enthalpy, equilibria và coverages.

Trong heterogeneous catalysis, apparent \(E_a\) thậm chí có thể nhỏ hoặc âm nếu adsorption equilibrium thay đổi mạnh với temperature.

# Apparent activation energy có thể thay đổi theo điều kiện

Nếu mechanism hoặc resting state thay đổi với temperature, slope Arrhenius cũng thay đổi.

Ví dụ ở nhiệt độ thấp surface coverage của reactant có thể cao; ở nhiệt độ cao desorption tăng và controlling regime thay đổi. Khi fit toàn bộ dải bằng một đường, \(E_a\) suy ra không có một physical interpretation đơn giản.

Đây là lý do cần kiểm tra residuals và từng temperature regime.

# Non-Arrhenius behavior

Đồ thị Arrhenius có thể cong vì:

- mechanism chuyển đổi;
- catalyst phase/state thay đổi;
- enzyme bị biến tính;
- diffusion trở thành rate-limiting;
- solvent structure thay đổi;
- quantum tunneling;
- nhiều pathways cạnh tranh.

Độ cong không phải “dữ liệu xấu” mặc định. Nó có thể là evidence rằng model Arrhenius đơn giản thiếu một phần physics.

# Xuyên hầm lượng tử

Các hạt nhẹ, đặc biệt proton và hydrogen atom, có thể **xuyên hầm lượng tử (quantum tunneling)** qua barrier thay vì cần năng lượng cổ điển cao hơn barrier.

Tunneling probability giảm rất mạnh khi barrier rộng hoặc particle nặng hơn. Vì vậy isotope substitution H → D có thể làm rate giảm đáng kể.

Ở nhiệt độ thấp, tunneling có thể làm rate ít phụ thuộc temperature hơn prediction Arrhenius.

# Hiệu ứng đồng vị động học

**Hiệu ứng đồng vị động học (kinetic isotope effect, KIE)** thường viết:

\[
KIE=\frac{k_H}{k_D}
\]

Nếu bond tới H bị thay đổi mạnh trong rate-sensitive transition state, KIE có thể đáng kể.

KIE giúp suy mechanism, nhưng không được đọc như “KIE lớn = tunneling chắc chắn”. Zero-point energy và equilibrium isotope effects cũng đóng góp.

# Diffusion-controlled limit

Trong solution, hai reactants trước hết phải khuếch tán tới gần nhau. Nếu intrinsic chemical step cực nhanh, overall rate không thể vượt xa tốc độ tạo encounter pair.

Khi đó reaction trở thành **giới hạn khuếch tán (diffusion-controlled)**.

Tăng reactivity electronic thêm nữa có thể gần như không làm observed rate tăng vì transport đã trở thành bottleneck.

Đây là ví dụ rõ ràng cho việc barrier hóa học không phải lúc nào cũng là yếu tố duy nhất quyết định tốc độ quan sát.

# Enzyme và Q10

Trong physiology, người ta đôi khi dùng:

\[
Q_{10}=\frac{k(T+10)}{k(T)}
\]

để mô tả sensitivity gần một vùng temperature.

Nhưng enzyme có folding equilibria, conformational dynamics và denaturation. Vì vậy ở temperature cao, rate có thể giảm dù elementary chemistry đáng lẽ nhanh hơn.

Một đường activity–temperature của enzyme là kết quả của nhiều quá trình ghép, không phải Arrhenius đơn thuần.

# Bảo quản thực phẩm và tuổi thọ vật liệu

Tốc độ oxidation, hydrolysis và degradation thường giảm khi temperature thấp. Đây là nền của refrigeration và accelerated aging tests.

Trong thử độ bền vật liệu, dữ liệu ở temperature cao đôi khi được extrapolate xuống room temperature bằng Arrhenius model. Phép extrapolation chỉ đáng tin nếu **cùng mechanism chi phối ở hai vùng**.

Nếu high-temperature test kích hoạt mechanism khác, tuổi thọ extrapolated có thể sai nghiêm trọng.

# Battery — nhiệt độ giúp kinetics nhưng cũng tăng degradation

Ở pin, tăng temperature có thể:

- tăng ionic conductivity;
- tăng charge-transfer rate;
- tăng diffusion trong electrode;
- đồng thời tăng side reactions và SEI growth.

Vì vậy “pin hoạt động nhanh hơn khi ấm” không đồng nghĩa “nhiệt độ càng cao càng tốt”. Kinetics mong muốn và degradation kinetics cùng tăng nhưng với activation parameters khác nhau.

Đây là ví dụ thực tế của competing Arrhenius processes.

# Cách suy Ea từ dữ liệu đúng hơn

Một workflow hợp lý:

```text
đo k ở nhiều T
→ bảo đảm cùng composition/catalyst state
→ vẽ ln k theo 1/T
→ kiểm tra residuals/curvature
→ fit vùng có cùng regime
→ báo uncertainty của slope
→ diễn giải Ea trong phạm vi model
```

Không nên chỉ lấy hai điểm nếu có khả năng đo nhiều điểm, vì hai điểm luôn tạo một đường thẳng và không thể phát hiện curvature.

# Độ không đảm bảo của Ea

Vì:

\[
E_a=-R\times slope
\]

uncertainty của slope truyền trực tiếp sang \(E_a\). Temperature uncertainty cũng đáng chú ý vì variable hồi quy là \(1/T\).

Nếu T chỉ được đọc từ setpoint thay vì actual sample temperature, systematic bias có thể lớn trong exothermic systems.

# Những hiểu lầm thường gặp

### “Ea là năng lượng phản ứng hấp thụ rồi biến mất”

Không. Nó là parameter của temperature dependence và liên quan barrier, không phải net energy cost.

### “Phản ứng có ΔG âm thì Ea cũng nhỏ”

Không. Driving force và barrier là hai chiều khác nhau của energy landscape.

### “A chỉ là collision frequency”

Không. Nó chứa cả configurational và entropic factors.

### “Arrhenius plot thẳng chứng minh mechanism”

Không. Nhiều mechanisms có thể cho vùng gần tuyến tính; cần evidence khác.

### “Tăng temperature 10 °C luôn làm rate gấp đôi”

Không. Ratio phụ thuộc \(E_a\), temperature và mechanism.

### “Catalyst làm ΔG phản ứng âm hơn”

Không. Catalyst đổi pathway/barrier, không đổi equilibrium thermodynamics.

## Mô hình tư duy

Hãy hình dung một ensemble phân tử đứng trước một dãy đèo trên **bề mặt năng lượng tự do**:

```text
nhiệt độ → phân bố trạng thái có thể tiếp cận
barrier → độ hiếm của đường đi reactive
entropy hoạt hóa → yêu cầu tổ chức hình học
catalyst → mở đường đèo khác
transport → quyết định hệ có tới cửa đèo đủ nhanh hay không
```

Arrhenius nén toàn bộ bức tranh đó thành một relation thực nghiệm rất hữu ích. TST mở relation đó ra thành enthalpy, entropy và transition-state population.

Xem tiếp: [Xúc tác](./04_catalysis.md) và [Năng lượng tự do Gibbs](../05_thermodynamics/03_gibbs_free_energy.md).