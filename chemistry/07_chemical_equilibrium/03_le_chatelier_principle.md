# Nguyên lý Le Châtelier — từ quy tắc định tính tới suy luận bằng Q, K và chemical potential

> **Nguyên lý Le Châtelier (Le Châtelier's principle / 르샤틀리에 원리)** nói rằng khi điều kiện của một hệ đang cân bằng bị thay đổi, thành phần thường dịch theo chiều làm giảm tác động của nhiễu loạn đó. Đây là một quy tắc trực giác hữu ích, nhưng không phải định luật nền tảng. Cách suy luận đáng tin cậy hơn là hỏi: perturbation làm **Q** thay đổi thế nào, **K** có đổi không, và chemical potential của các species thay đổi ra sao?

Nếu chỉ nhớ “hệ chống lại thay đổi”, rất dễ áp dụng sai cho chất rắn tinh khiết, khí trơ, áp suất, pha loãng hoặc hệ không lý tưởng. Vì vậy chương này dùng Le Châtelier như lớp trực giác phía trên thermodynamics, không dùng nó thay cho thermodynamics.

# Ba bước reasoning chuẩn

Khi một hệ đang ở equilibrium bị perturb:

```text
1. trước perturbation: Q = K
2. perturbation làm Q hoặc K thay đổi
3. hệ phản ứng theo chiều làm Q tiến về K mới
```

Nếu temperature không đổi, K giữ nguyên và chỉ Q thay đổi.

Nếu temperature thay đổi, chính K cũng thay đổi.

Đây là phân biệt quan trọng nhất của toàn chương.

# Thêm chất phản ứng

Xét:

\[
A+B\rightleftharpoons C
\]

\[
Q=\frac{a_C}{a_Aa_B}
\]

Ban đầu:

\[
Q=K
\]

Thêm A làm \(a_A\) tăng tức thời nên:

\[
Q<K
\]

và:

\[
\Delta_rG=RT\ln(Q/K)<0
\]

chiều thuận trở nên thuận lợi cho tới khi composition mới làm Q trở lại K.

Câu “hệ tiêu thụ A vừa thêm” là cách nói rút gọn của lập luận này.

# Loại sản phẩm

Nếu giảm \(a_C\), Q giảm và chiều thuận được thúc đẩy.

Đây là nguyên lý của nhiều quá trình công nghiệp: tách sản phẩm khi nó hình thành có thể kéo conversion tiến xa hơn.

Tuy nhiên tách sản phẩm không làm K đổi. Nó liên tục đưa hệ ra khỏi equilibrium, sau đó reaction tiến để tái lập equilibrium mới.

Trong reactor dòng liên tục, quá trình này có thể được duy trì lâu dài nên hệ không nhất thiết ở equilibrium toàn cục.

# Thêm chất nhưng Q có thể không đổi

Le Châtelier dễ gây sai khi species thêm vào không xuất hiện trong reaction quotient.

Ví dụ:

\[
CaCO_3(s)\rightleftharpoons CaO(s)+CO_2(g)
\]

với hai chất rắn tinh khiết:

\[
Q\approx\frac{P_{CO_2}}{P^\circ}
\]

Thêm nhiều \(CaCO_3(s)\) hơn khi pha rắn đó đã hiện diện không làm Q đổi và không dịch equilibrium composition của gas.

Lý do: activity của pure solid gần 1, không phụ thuộc lượng solid miễn pha vẫn tồn tại.

Đây là ví dụ cho thấy khẩu hiệu “thêm reactant → shift product” không phải quy tắc tuyệt đối.

# Thay đổi thể tích của khí

Xét reaction khí lý tưởng:

\[
N_2+3H_2\rightleftharpoons2NH_3
\]

Nếu volume giảm đột ngột ở T không đổi, mọi partial pressure tăng cùng factor \(f\).

Q mới:

\[
Q'=
\frac{(fP_{NH_3})^2}
{(fP_{N_2})(fP_{H_2})^3}
=Qf^{-2}
\]

Vì \(f>1\):

\[
Q'<K
\]

nên reaction tiến về phía NH₃.

Kết luận “nén ưu tiên phía ít mol khí hơn” xuất hiện trực tiếp từ exponent tổng trong Q.

## Công thức tổng quát

Nếu tất cả partial pressures thay đổi cùng factor \(f\):

\[
Q'=Qf^{\Delta n_{gas}}
\]

với:

\[
\Delta n_{gas}=
\sum \nu_{gas,products}-
\sum \nu_{gas,reactants}
\]

Nếu \(\Delta n_{gas}=0\), compression lý tưởng không làm Q thay đổi.

# Áp suất không phải lúc nào cũng đồng nghĩa với nén

Có nhiều cách làm total pressure tăng.

## Giảm thể tích

Partial pressures của reactive gases tăng → Q thường thay đổi.

## Thêm khí trơ ở thể tích không đổi

Total pressure tăng nhưng:

\[
P_i=\frac{n_iRT}{V}
\]

của reactive species không đổi.

Do đó Q không đổi và equilibrium không shift trong mô hình ideal gas.

## Thêm khí trơ ở áp suất tổng không đổi

Hệ phải nở thể tích, làm partial pressures reactive gases giảm. Khi đó Q có thể thay đổi và equilibrium có thể dịch tùy \(\Delta n_{gas}\).

Vì thế câu “tăng pressure làm shift về phía ít mol gas” thiếu thông tin. Phải biết **pressure được thay đổi bằng cách nào**.

# Nhiệt độ là perturbation khác bản chất

Concentration hoặc pressure perturbations ở fixed T làm **Q đổi trong khi K không đổi**.

Temperature perturbation làm **K đổi** vì standard chemical potentials thay đổi.

Từ van ’t Hoff:

\[
\frac{d\ln K}{dT}=
\frac{\Delta H^\circ}{RT^2}
\]

Nếu \(\Delta H^\circ>0\), tăng T thường làm K tăng.

Nếu \(\Delta H^\circ<0\), tăng T thường làm K giảm.

Đây là cách hiểu chính xác hơn câu “heat behaves like reactant/product”. Nhiệt không phải một species được thêm vào reaction quotient.

# Vì sao reaction tỏa nhiệt có K giảm khi T tăng?

Với reaction tỏa nhiệt, product side được ổn định enthalpically so với reactants. Khi T tăng, entropy contribution \(-T\Delta S\) thay đổi trọng số và equilibrium free-energy difference biến đổi.

Quan hệ van ’t Hoff định lượng sự thay đổi đó; không cần tưởng tượng “heat molecule” xuất hiện trong phương trình.

# Catalyst không thay equilibrium

Catalyst mở pathway có lower activation barrier nhưng không đổi Gibbs free energy của reactants và products.

Do microscopic reversibility, catalyst tăng cả forward và reverse flux theo một network tương thích.

Nếu hệ đang ngoài equilibrium, catalyst làm nó đạt equilibrium nhanh hơn.

Nếu hệ đã equilibrium, catalyst làm molecular exchange nhanh hơn nhưng net composition giữ nguyên.

# Pha loãng dung dịch

Pha loãng thay concentration và thường làm activity giảm, nhưng direction không nên suy bằng câu “hệ tạo thêm nhiều hạt”.

Ví dụ:

\[
AB\rightleftharpoons A+B
\]

trong dilute ideal solution:

\[
Q=\frac{[A][B]}{[AB]c^\circ}
\]

Nếu tất cả concentrations giảm cùng factor \(f<1\): numerator giảm theo \(f^2\), denominator theo \(f\), nên Q giảm. Hệ tiến thuận để Q trở về K.

Đây là origin của xu hướng dissociation tăng khi dilute trong một số hệ weak electrolyte.

# Common-ion effect là một trường hợp Le Châtelier định lượng

Với:

\[
HA\rightleftharpoons H^++A^-
\]

thêm salt chứa \(A^-\) làm Q tăng:

\[
Q=\frac{a_Ha_A}{a_{HA}}
\]

Nếu Q>K, reaction đi nghịch và fraction HA tăng.

Hiệu ứng ion chung không cần học như một quy tắc riêng; nó là application của Q/K.

# Precipitation và common ion

Với:

\[
MX(s)\rightleftharpoons M^++X^-
\]

\[
Q_{sp}=a_Ma_X
\]

thêm X⁻ làm \(Q_{sp}\) tăng. Nếu vượt \(K_{sp}\), precipitation thermodynamically favored.

Nhưng precipitation có thể chậm nếu nucleation barrier lớn. Đây là giới hạn quan trọng của reasoning equilibrium: nó cho direction, không cho timescale.

# pH có thể điều khiển solubility gián tiếp

Nếu anion của solid được proton hóa:

\[
A^-+H^+\rightleftharpoons HA
\]

acid loại bớt free \(A^-\), làm dissolution equilibrium dịch để tạo thêm A⁻. Vì vậy một salt ít tan có thể tan mạnh hơn ở low pH.

Đây là **coupled equilibrium**, sâu hơn câu “acid hòa tan muối”.

# Complexation cũng kéo equilibrium

Nếu \(M^{2+}\) được ligand L giữ dưới dạng complex:

\[
M^{2+}+L\rightleftharpoons ML^{2+}
\]

free \(M^{2+}\) giảm. Một precipitate chứa M có thể hòa tan thêm để bù.

Đây là lý do ammonia có thể hòa tan một số precipitates bạc thông qua complex formation.

Le Châtelier ở đây là network effect, không chỉ một single equation.

# Hệ nhiều equilibrium: khẩu hiệu trở nên nguy hiểm

Nếu một perturbation tác động đồng thời lên acid-base, complexation và precipitation, từng “shift” riêng có thể cạnh tranh.

Ví dụ tăng pH có thể:

- deprotonate ligand → tăng complexation;
- đồng thời tạo OH⁻ → tăng metal hydroxide precipitation.

Muốn biết species cuối cùng phải giải coupled balances, không thể dựa vào một khẩu hiệu đơn.

# Phase rule và appearance/disappearance của pha

Trong heterogeneous equilibrium, khi một pure phase xuất hiện hoặc biến mất, số degrees of freedom của hệ thay đổi.

Ví dụ solange solid vẫn present, dissolved concentration có thể bị buffer bởi solubility equilibrium. Khi solid hết hoàn toàn, constraint đó biến mất và composition có thể thay đổi theo cách khác.

Do đó amount of solid “không ảnh hưởng K” nhưng việc solid **còn hay hết** vẫn rất quan trọng.

# Nonideality — concentration không phải activity

Ở ionic strength cao:

\[
a_i=\gamma_i c_i/c^\circ
\]

Một perturbation concentration có thể đồng thời làm \(\gamma_i\) thay đổi. Vì vậy Q concentration-based không phản ánh đầy đủ driving force.

Trong gas áp suất cao, fugacity thay partial pressure:

\[
a_i=\frac{f_i}{f^\circ}
\]

Le Châtelier vẫn đúng ở tầng thermodynamic nếu dùng chemical potentials đúng, nhưng shortcut lý tưởng có thể sai.

# Haber–Bosch — equilibrium tốt nhất không phải operating point tốt nhất

\[
N_2+3H_2\rightleftharpoons2NH_3
\]

Reaction tỏa nhiệt và giảm số mol gas.

Thermodynamics gợi ý:

```text
pressure cao → conversion equilibrium tốt hơn
T thấp → K lớn hơn
```

Nhưng T thấp làm kinetics chậm. Pressure cao làm compression cost và engineering burden tăng.

Process thực dùng catalyst, moderate-high temperature, high pressure, product separation và recycle.

Đây là ví dụ điển hình rằng **engineering optimum là trade-off giữa thermodynamics, kinetics, transport, separation và economics**.

# Battery — Le Châtelier dưới dạng Nernst

Khi battery discharge, reactants bị tiêu thụ và products tích lũy, nên Q thay đổi.

Phương trình Nernst:

\[
E=E^\circ-\frac{RT}{nF}\ln Q
\]

cho thấy voltage thay đổi liên tục theo state of charge.

Thay vì nói “battery equilibrium shifts”, electrochemistry định lượng trực tiếp thay đổi chemical potential bằng voltage.

# Biology — hệ sống chủ động không cho equilibrium thiết lập

Nếu tế bào để nhiều metabolic reactions đạt equilibrium hoàn toàn, nó mất khả năng sinh công có hướng.

Tế bào liên tục:

- nạp chất dinh dưỡng;
- loại sản phẩm;
- duy trì ion gradients;
- ghép reactions với ATP/redox chemistry.

Đây là ví dụ ngược hữu ích: sự sống vận hành bằng cách duy trì **non-equilibrium steady states**, chứ không “tuân Le Châtelier để luôn về equilibrium” một cách thụ động.

# Những hiểu lầm thường gặp

### “Hệ chống lại mọi thay đổi để quay về trạng thái cũ”

Không. Nó đi tới **equilibrium mới** dưới conditions mới.

### “Thêm reactant luôn shift product”

Không nếu reactant là pure solid/liquid có activity không đổi hoặc perturbation không làm Q đổi.

### “Tăng total pressure luôn shift về phía ít mol gas”

Không. Phải biết partial pressures thay đổi ra sao.

### “Heat là một reactant thật”

Không. Temperature thay đổi K qua thermodynamics.

### “Catalyst shift equilibrium”

Không. Catalyst thay kinetics.

### “Le Châtelier dự đoán được tốc độ”

Không. Nó chỉ là equilibrium direction heuristic.

## Mô hình tư duy

Đừng bắt đầu bằng câu “hệ chống lại thay đổi”. Hãy hỏi:

```text
T có đổi không?
↓
Nếu không: K giữ nguyên
Perturbation làm Q đổi thế nào?
↓
Q<K → thuận
Q>K → nghịch

Nếu T đổi:
K đổi theo thermodynamics
→ so Q hiện tại với K mới
```

Nguyên lý Le Châtelier khi đó trở thành một shortcut có nền tảng, không phải một câu thần chú.

Xem tiếp: [Nhiệt động lực học của cân bằng](./04_thermodynamics_of_equilibrium.md).