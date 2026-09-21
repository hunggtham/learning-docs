# Pin Galvani — biến năng lượng tự do hóa học thành công điện

> **Pin Galvani hay pin Volta (galvanic/voltaic cell / 갈바니 전지)** tách một phản ứng oxy hóa–khử tự phát thành hai vùng không gian khác nhau để electron buộc phải đi qua mạch ngoài. Nhờ vậy, một phần độ giảm năng lượng tự do Gibbs của phản ứng có thể được thu dưới dạng **công điện**, thay vì chủ yếu biến thành nhiệt tại cùng một vị trí phản ứng.

Pin điện hóa vì thế không tạo ra năng lượng từ hư không. Nó chỉ **định tuyến dòng electron** của một phản ứng redox theo một con đường hữu ích.

# Tại sao phải tách hai bán phản ứng?

Nếu nhúng Zn trực tiếp vào dung dịch \(Cu^{2+}\):

\[
Zn+Cu^{2+}\rightarrow Zn^{2+}+Cu
\]

electron được truyền ngay tại bề mặt tiếp xúc và năng lượng hóa học khó được thu thành dòng điện có kiểm soát.

Nếu tách:

Anode:

\[
Zn\rightarrow Zn^{2+}+2e^-
\]

Cathode:

\[
Cu^{2+}+2e^-\rightarrow Cu
\]

vào hai bán pin nối bằng dây dẫn và đường dẫn ion, electron phải đi qua mạch ngoài. Một tải điện đặt trên đường đó có thể nhận công.

Đây là ý tưởng nền của mọi pin: **tách đường đi của electron khỏi đường đi của ion**.

# Anode và cathode phải nhớ bằng phản ứng, không bằng dấu

**Anode (điện cực oxy hóa / 산화 전극)** là nơi oxy hóa.

**Cathode (điện cực khử / 환원 전극)** là nơi khử.

Quy tắc này luôn đúng.

Dấu điện cực phụ thuộc chế độ vận hành:

```text
pin Galvani:
anode  → cực âm
cathode→ cực dương

bình điện phân:
anode  → thường cực dương
cathode→ thường cực âm
```

Vì vậy học “anode = âm” sẽ gây lỗi khi chuyển từ pin sang điện phân.

# Electron và dòng điện quy ước đi ngược chiều nhau

Trong dây kim loại của pin Galvani, electron đi:

```text
anode → cathode
```

Dòng điện quy ước được định nghĩa theo chiều chuyển động của điện tích dương nên đi:

```text
cathode → anode
```

Sự khác nhau này là quy ước lịch sử của điện học, không phải mâu thuẫn vật lý.

# Chất điện ly giữ đường dẫn ion

Mỗi bán pin thường chứa chất điện ly để ion có thể di chuyển.

Nếu electron rời anode mà không có chuyển động ion bù điện tích, phía anode sẽ tích điện dương còn phía cathode tích điện âm, tạo electric field chống lại electron flow và dòng nhanh chóng dừng.

Vì vậy một pin cần hai circuit đồng thời:

```text
electronic circuit → electron trong dây/điện cực
ionic circuit       → ion trong điện ly/màng/cầu muối
```

Chỉ có một trong hai circuit thì pin không thể duy trì dòng lâu.

# Cầu muối

**Cầu muối (salt bridge / 염다리)** cho phép ion di chuyển giữa hai ngăn nhưng hạn chế trộn trực tiếp nhanh của hai dung dịch.

Trong pin Zn/Cu:

- ở anode, \(Zn^{2+}\) được tạo → cần anion đi tới để duy trì gần trung hòa;
- ở cathode, \(Cu^{2+}\) bị tiêu thụ → cation từ cầu muối có thể đi tới để bù thay đổi charge distribution.

Cầu muối **không phải đường electron**.

Electron đi qua conductor; ion đi qua electrolyte.

# Junction potential — cầu muối không hoàn toàn “vô hình”

Tại ranh giới hai dung dịch khác composition, cation và anion có mobility khác nhau nên có thể khuếch tán với tốc độ khác, tạo **thế nối lỏng (liquid junction potential)**.

Chọn electrolyte có ions mobility tương đối gần nhau như KCl thường giúp giảm hiệu ứng này.

Trong phép đo chính xác, junction potential là một nguồn độ không đảm bảo thật, không thể bỏ qua bằng câu “cầu muối chỉ để cân bằng điện tích”.

# Ký hiệu pin

Pin Daniell:

\[
Zn(s)|Zn^{2+}(aq)||Cu^{2+}(aq)|Cu(s)
\]

Quy ước:

```text
|   → ranh giới pha
||  → cầu muối/màng ngăn
trái  → anode theo cách viết thông dụng
phải  → cathode
```

Nếu bán phản ứng không có kim loại dẫn điện riêng, cần điện cực trơ như Pt hoặc graphite để truyền electron.

Ví dụ:

\[
Pt|Fe^{2+},Fe^{3+}||Ce^{4+},Ce^{3+}|Pt
\]

Điện cực Pt không phải reactant chính; nó cung cấp bề mặt dẫn điện cho electron transfer.

# Không thể đo một thế điện cực tuyệt đối

Volt kế đo **hiệu điện thế**, không đo thế tuyệt đối của một điện cực cô lập.

Vì vậy electrochemistry xây thang bằng điện cực tham chiếu. **Điện cực hydro chuẩn (standard hydrogen electrode, SHE)** được quy ước:

\[
E^\circ=0.000\;V
\]

Các thế điện cực khác được đo tương đối so với reference này.

Trong thực hành dùng nhiều reference thuận tiện hơn như Ag/AgCl hoặc calomel.

# Thế khử chuẩn

Bảng điện hóa thường ghi bán phản ứng theo chiều khử:

\[
Ox+ne^-\rightarrow Red
\]

với **thế khử chuẩn (standard reduction potential)**.

Thế càng dương nghĩa chiều khử thuận lợi hơn so với reference trong điều kiện chuẩn tương ứng.

Để tính pin:

\[
E_{cell}^\circ
=E_{cathode}^\circ-E_{anode}^\circ
\]

vì cathode là quá trình khử, còn anode thực tế chạy ngược chiều bán phản ứng khử ghi trong bảng.

# Không nhân thế điện cực với hệ số hóa lượng

Giả sử phải nhân một bán phản ứng lên 2 để cân electron. Không được nhân \(E^\circ\) lên 2.

Điện thế là đại lượng cường độ. Đại lượng dung lượng là Gibbs energy:

\[
\Delta G^\circ=-nFE^\circ
\]

Nếu nhân reaction lên 2:

```text
n tăng gấp đôi
ΔG° tăng gấp đôi
E° giữ nguyên
```

Đây là một lỗi phổ biến khi ghép bán phản ứng.

# Từ điện thế tới Gibbs free energy

Với phản ứng pin tổng:

\[
\Delta G=-nFE
\]

Nếu:

\[
E>0
\]

thì:

\[
\Delta G<0
\]

và chiều viết của pin Galvani thuận lợi về nhiệt động.

Điện áp có thể hiểu là **free-energy change trên một đơn vị điện tích**.

Một volt:

\[
1\;V=1\;J/C
\]

Do đó điện hóa biến một chênh lệch chemical potential thành một đại lượng điện có thể đo trực tiếp.

# Open-circuit voltage

Khi không nối tải và gần như không có dòng, pin có thể tiến gần trạng thái local electrochemical equilibrium ở hai interfaces.

Điện áp đo được là **điện áp hở mạch (open-circuit voltage, OCV)**.

OCV phản ánh thermodynamic state tốt hơn loaded voltage, nhưng chỉ khi:

- pin đã đủ thời gian thư giãn;
- side reactions nhỏ;
- không có large concentration gradients;
- reference/contact effects được kiểm soát.

Trong battery diagnostics, đo OCV ngay sau high-current pulse có thể chưa phản ánh equilibrium composition vì gradients vẫn còn.

# Phương trình Nernst — composition làm điện áp thay đổi

Ngoài điều kiện chuẩn:

\[
E=E^\circ-rac{RT}{nF}\ln Q
\]

Khi pin discharge, reactants giảm và products tăng, Q thay đổi nên voltage thay đổi.

Vì vậy pin không có một “điện áp hóa học cố định” hoàn toàn độc lập với state of charge.

# Pin nồng độ

Một cell có thể tạo điện áp dù hai điện cực cùng chất, chỉ vì activity khác nhau.

Ví dụ hai \(Ag|Ag^+\) half-cells có nồng độ khác nhau.

Driving force là xu hướng làm chemical potentials cân bằng giữa hai bên.

**Pin nồng độ (concentration cell)** là bằng chứng rất rõ rằng điện áp không cần hai “kim loại khác nhau”; chỉ cần electrochemical potential difference.

# Electrochemical potential

Với ion charge \(z_i\):

\[
\tilde\mu_i=\mu_i+z_iF\phi
\]

Pin hoạt động vì các electrochemical potentials không đồng đều giữa electrodes/electrolyte phases.

Voltage là manifestation vĩ mô của chênh lệch này.

Cách nhìn này thống nhất Nernst, membrane potentials và battery thermodynamics.

# Khi nối tải, pin rời khỏi equilibrium

Nếu nối một điện trở ngoài, electron bắt đầu chạy. Lúc đó system không còn ở trạng thái reversible equilibrium.

Điện áp đầu cực thực:

\[
V_{terminal}
=E_{eq}
-\eta_{anode}
-\eta_{cathode}
-I R_{ohmic}
-\text{tổn thất vận chuyển khối}
\]

ở dạng khái niệm.

Vì vậy:

```text
OCV → gần thermodynamic limit
loaded voltage → thermodynamics − losses
```

# Quá thế

**Quá thế (overpotential, \(\eta\))** là phần điện áp bổ sung liên quan kinetics của electrode reaction.

Ngay cả khi reaction thermodynamically favorable, electron transfer có thể cần electrode potential lệch khỏi equilibrium value để tạo current đáng kể.

Butler–Volmer mô tả relation giữa current density và \(\eta\) trong model cơ bản.

# Tổn thất ohmic

Ion đi qua electrolyte và electron đi qua solid conductor đều gặp resistance.

Voltage loss gần:

\[
\Delta V_{ohmic}=IR
\]

Resistance tăng khi:

- electrolyte conductivity thấp;
- separator dày;
- contact kém;
- temperature thấp.

Tổn thất này biến một phần free energy thành heat.

# Phân cực nồng độ

Khi current cao, reactant gần electrode có thể bị tiêu thụ nhanh hơn tốc độ vận chuyển từ bulk.

Surface concentration khác bulk concentration, nên local Nernst potential thay đổi và xuất hiện **phân cực nồng độ (concentration polarization)**.

Nếu surface concentration tiến gần zero, current có thể chạm limiting value.

Đây là cầu nối giữa electrochemistry và diffusion.

# Công suất và năng lượng không giống nhau

Energy capacity cho biết pin có thể cung cấp tổng năng lượng bao nhiêu.

Power:

\[
P=IV
\]

cho biết tốc độ cung cấp năng lượng.

Một battery có high capacity vẫn có thể không cấp high power nếu kinetics hoặc transport chậm.

Đây là lý do electrode particle size, conductivity và electrolyte transport quan trọng bên cạnh thermodynamic voltage.

# Dung lượng lý thuyết

Nếu một active material trao đổi \(n_e\) mol electron trên mỗi mol material:

\[
Q_{theoretical}=n_eF
\]

trên mol material.

Đổi sang mAh/g:

\[
C_{specific}
=\frac{n_eF}{3.6M}
\]

với \(M\) là molar mass theo g/mol.

Dung lượng vì vậy là bài toán stoichiometry electron, còn voltage là bài toán free energy per charge.

# State of charge và electrode chemical potential

Trong intercalation battery, composition của electrode thay đổi khi Li được chèn/rút.

Chemical potential của Li trong host thay đổi theo composition, nên electrode potential cũng thay đổi.

Plateau voltage thường liên quan two-phase coexistence hoặc vùng chemical potential thay đổi chậm.

Sloping voltage phản ánh solid-solution behavior hoặc nhiều contributions khác.

Voltage curve vì thế chứa thông tin thermodynamics của material.

# Entropy contribution vào điện áp

Vì:

\[
\Delta G=\Delta H-T\Delta S
\]

nên cell voltage phụ thuộc temperature.

Derivative:

\[
\left(\frac{\partial E}{\partial T}\right)_P
=\frac{\Delta S}{nF}
\]

với convention phù hợp.

Battery có thể sinh hoặc hấp thụ **reversible entropic heat** ngoài Joule heating.

Điều này quan trọng trong thermal management.

# Tự phóng điện

Ngay cả khi không nối tải, side reactions có thể tiêu thụ charged species, làm state of charge giảm theo thời gian.

Đó là **tự phóng điện (self-discharge)**.

Thermodynamic instability của charged state có thể tồn tại nhưng kinetics chậm; electrolyte/electrode interfaces được thiết kế để side reactions đủ chậm trong thời gian sử dụng.

Pin vì thế là ví dụ điển hình của việc khai thác **metastability có kiểm soát**.

# Ăn mòn như pin Galvani không mong muốn

Khi hai metals khác nhau tiếp xúc qua electrolyte, metal hoạt động hơn có thể trở thành anode và ăn mòn nhanh.

Ngay trên một metal duy nhất, differences về oxygen concentration, stress hoặc microstructure có thể tạo local galvanic cells.

Pin và corrosion dùng cùng thermodynamics; khác nhau chủ yếu ở việc electron flow có được khai thác hữu ích hay gây phá hủy vật liệu.

# Pin sinh học

Màng tế bào duy trì gradients ion và điện thế.

Proton motive force có electrochemical free energy:

\[
\Delta\tilde\mu_{H^+}
=RT\ln\frac{a_2}{a_1}+F\Delta\phi
\]

ATP synthase khai thác gradient đó tương tự một molecular energy converter.

Điều này cho thấy electrochemical potential không chỉ dành cho pin kim loại; nó là nguyên lý nền của bioenergetics.

# Fuel cell

Fuel cell cũng là galvanic device, nhưng reactants được cung cấp liên tục từ bên ngoài thay vì lưu toàn bộ trong cell.

Ví dụ H₂/O₂ fuel cell:

\[
2H_2+O_2\rightarrow2H_2O
\]

Thermodynamics giống combustion, nhưng electron được buộc qua external circuit để tạo work.

Fuel cell vì thế là cầu nối trực tiếp giữa chemical energy và electrical energy conversion.

# Những hiểu lầm thường gặp

### “Electron đi qua cầu muối”

Không. Electron đi qua conductor; ions đi qua electrolyte.

### “Anode luôn âm”

Không. Anode luôn là nơi oxy hóa; dấu phụ thuộc chế độ pin/điện phân.

### “Nhân bán phản ứng lên 2 thì nhân E° lên 2”

Không. E là intensive; \(\Delta G=-nFE\) mới extensive.

### “Pin dưới tải có điện áp đúng bằng Nernst”

Không. Có kinetic, ohmic và mass-transfer losses.

### “Thêm nhiều active material làm voltage tăng”

Không trực tiếp. Nó chủ yếu tăng capacity/energy amount; equilibrium voltage phụ thuộc chemical potentials.

### “Pin hết điện nghĩa electron đã hết”

Không. State of charge và available chemical free-energy difference đã giảm; electrons vẫn tồn tại trong vật chất.

## Mô hình tư duy

Pin Galvani là một **bộ chuyển đổi chemical-potential difference thành electron flow có kiểm soát**:

```text
redox free-energy difference
→ tách oxidation/reduction thành hai điện cực
→ electron qua mạch ngoài
→ ion qua điện ly
→ điện áp × điện lượng = công điện
```

Khi có tải, kinetics và transport lấy đi một phần voltage khỏi thermodynamic maximum. Vì vậy hiểu pin cần đồng thời thermodynamics, kinetics, diffusion và materials chemistry.

Xem tiếp: [Điện thế pin và phương trình Nernst](./03_cell_potential_and_nernst_equation.md), [Điện hóa động học và trở kháng](./06_electrochemical_kinetics_and_impedance.md).