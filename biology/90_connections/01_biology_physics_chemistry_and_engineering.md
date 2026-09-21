# Sinh học nhìn qua Vật lý, Hóa học và Kỹ thuật — Biology through Physics, Chemistry and Engineering (생물학과 물리·화학·공학)

Sinh học không đứng ngoài các định luật Vật lý và Hóa học. Tế bào (cell), tissue và hệ sinh thái (ecosystem) đều dùng cùng matter, energy và force như mọi system khác. Điều đặc biệt ở living system là các interaction này được tổ chức thành network có ranh giới (boundary), phản hồi (feedback), thông tin (information), heredity và evolutionary history.

Chapter này không thay thế giáo trình Vật lý hoặc Hóa học. Nó gom những principle xuất hiện lặp lại trong Sinh học (biology) để người đọc nhìn thấy vì sao cùng một equation có thể giải thích membrane transport, nơron (neuron), tuần hoàn (circulation), morphogenesis hoặc ecosystem.

> **Mô hình tư duy (mental model):** Vật lý (physics) đặt constraint; Chemistry tạo reaction và tương tác phân tử (molecular interaction); Biology tổ chức chúng thành adaptive system; Engineering cung cấp ngôn ngữ về điều khiển (control), tính bền vững (robustness) và thiết kế (design). Không domain nào đủ một mình.

## 1. Phân tích thứ nguyên (dimensional analysis): kiểm tra một model trước khi tính

Trước khi dùng equation, hãy kiểm tra unit. Nếu rate có unit `mol/s` nhưng vế phải ra `mol²/s`, model chắc chắn có vấn đề.

Phân tích thứ nguyên còn giúp suy relationship. Hệ số khuếch tán (diffusion coefficient) \(D\) có unit \(L^2/T\); vì vậy thời gian khuếch tán đặc trưng (characteristic diffusion time) phải có dạng gần \(L^2/D\), không thể chỉ là \(L/D\).

Thói quen kiểm unit là một trong những cách rẻ nhất để bắt lỗi reasoning.

## 2. Random motion tạo directed flux ở population level

Một molecule trong liquid chuyển động ngẫu nhiên (random walk). Không molecule nào biết nơi concentration thấp. Nhưng nếu phía trái có nhiều molecule hơn, số molecule random bước sang phải mỗi giây trung bình cũng nhiều hơn số từ phải sang trái.

Kết quả macroscopic là **khuếch tán (diffusion)**.

Fick's first law:

\[
J=-D\frac{dC}{dx}
\]

Dấu âm cho biết flux đi theo chiều giảm concentration. Đây là emergence: motion microscopic không có direction nhưng dòng quần thể (population flux) có direction.

## 3. Thời gian khuếch tán (diffusion time) giải thích giới hạn kích thước

Thời gian khuếch tán đặc trưng:

\[
t\sim\frac{x^2}{2D}
\]

Distance tăng 10 lần làm time tăng khoảng 100 lần. Đây là lý do diffusion xuất sắc ở quy mô micromet (micron scale) nhưng tệ ở quy mô mét (metre scale).

Từ một equation này ta suy ra vì sao cell nhỏ, vì sao lung cần circulation, vì sao plant cần mô mạch (vascular tissue) và vì sao tumor lớn cần angiogenesis.

## 4. Surface-area-to-volume ratio là geometry trở thành physiology

Nếu characteristic size \(L\):

\[
A\propto L^2,\qquad V\propto L^3
\]

nên:

\[
\frac{A}{V}\propto\frac{1}{L}
\]

Organism lớn có ít exchange area relative volume hơn nếu chỉ scale đồng dạng. Vì vậy biology tạo gấp cuộn (folding), branching và internal transport.

Alveoli, intestinal villi, gill lamellae và root hair đều là geometric solution cho cùng constraint.

## 5. Osmosis và thế hóa học (chemical potential)

Water không “muốn đi về nơi nhiều muối”. Net water movement phản ánh thế hóa học và membrane permeability.

Với dilute solution, osmotic pressure gần:

\[
\Pi=iCRT
\]

Equation cho thấy particle concentration có thể tạo áp suất (pressure). Cell phải regulate osmolarity vì membrane mechanics có giới hạn.

Plant tận dụng turgor; animal cell tránh swelling bằng ion pump và extracellular regulation.

## 6. Chênh lệch nồng độ (concentration gradient) chưa đủ cho ion: cần electrochemical potential

Ion mang charge nên movement phụ thuộc cả chênh lệch hóa học (chemical gradient) và electric potential.

Nernst equation cho điện thế cân bằng (equilibrium potential) của ion:

\[
E=\frac{RT}{zF}\ln\frac{[ion]_{out}}{[ion]_{in}}
\]

Đây là voltage tại đó lực điện (electrical force) cân bằng concentration drive cho một ion.

Nơron điện thế màng (membrane potential) và động lực proton (proton motive force) ở mitochondria cùng dùng một principle: **charge separation + concentration difference lưu năng lượng tự do (free energy)**.

## 7. Membrane capacitance: màng tế bào (cell membrane) cũng có đặc tính (property) điện học

Lớp kép lipid (lipid bilayer) cách điện tương đối giữa hai conductive fluid. Vì vậy membrane có thể được model như capacitor.

\[
Q=CV
\]

Kênh ion (ion channel) giống conductance pathway; membrane capacitance làm voltage không đổi instant khi current xuất hiện.

RC-like hằng số thời gian (time constant) giúp hiểu vì sao neuron integrate input qua time thay vì phản ứng tức thì với từng ion riêng.

Engineering circuit analogy không nói neuron là wire; nó giúp formalize một phần biophysics.

## 8. Thermodynamics: favorable không đồng nghĩa fast

Gibbs năng lượng tự do:

\[
\Delta G=\Delta H-T\Delta S
\]

\(\Delta G<0\) cho thermodynamic tendency trong condition cụ thể. Nhưng reaction có thể vẫn rất chậm nếu activation barrier cao.

Enzym (enzyme) giảm activation barrier, thay kinetics, nhưng không đổi equilibrium \(\Delta G\) của overall reaction.

Đây là distinction nền tảng giữa thermodynamics và kinetics.

## 9. ATP: coupling chứ không phải “năng lượng nằm trong một bond” theo nghĩa đơn giản

ATP hydrolysis favorable trong cellular condition vì product state có lower năng lượng tự do tổng thể. Cell coupling ATP hydrolysis với unfavorable process qua shared intermediate hoặc conformational change.

Vận chuyển chủ động (active transport), biosynthesis và protein vận động (motor protein) đều dùng logic này.

ATP không phải battery độc lập; nó là **currency trong mạng lưới phản ứng (reaction network)** được regenerate liên tục.

## 10. Redox potential và electron flow

Electron chuyển giữa donor và acceptor có redox potential khác nhau. Hô hấp (respiration) đưa electron từ chất dinh dưỡng (nutrient) qua chain đến terminal acceptor; năng lượng tự do giải phóng từng step được dùng pump proton.

Quang hợp (photosynthesis) dùng photon để nâng electron lên energy state cao rồi tạo khả năng khử (reducing power).

Do đó metabolism có thể đọc như **controlled electron flow → chênh lệch ion (ion gradient) → chemical work**.

## 11. Thẩm thấu hóa học (chemiosmosis): gradient nối Chemistry với mechanics phân tử

Chuỗi chuyền electron (electron transport chain) tạo chênh lệch proton (proton gradient). Proton quay về qua ATP synthase (ATP synthase) và drive rotary/conformational mechanism tạo ATP.

Đây là một concept đặc biệt quan trọng vì cùng architecture xuất hiện ở bacteria, mitochondria và chloroplast.

Tiến hóa (evolution) đã tái sử dụng membrane gradient như universal energy transducer.

## 12. Động học enzym (enzyme kinetics) và bão hòa (saturation)

Michaelis–Menten:

\[
v=\frac{V_{max}[S]}{K_m+[S]}
\]

Ở substrate thấp, rate gần linear. Ở substrate cao, enzyme saturated nên rate tiến tới \(V_{max}\).

Saturation xuất hiện rộng hơn enzyme: transporter, thụ thể (receptor), oxy (oxygen) binding và many physiological response đều có ceiling.

## 13. Hill equation và cooperativity

Một response cooperative thường được model bằng:

\[
Y=\frac{[L]^n}{K^n+[L]^n}
\]

Khi \(n>1\), curve steep hơn. Hemoglobin oxygen binding là classic context cho cooperative intuition.

Nhưng Hill coefficient là phenomenological summary, không tự nói full molecular mechanism.

## 14. Binding affinity và occupancy

Simple one-site binding:

\[
\theta=\frac{[L]}{K_d+[L]}
\]

\(K_d\) thấp thường nghĩa affinity cao hơn. Tuy nhiên receptor thật có conformational state, competition và downstream amplification.

Occupancy không đồng nghĩa response; few occupied receptor có thể tạo large downstream signal nếu amplification mạnh.

## 15. Fluid flow: áp suất chênh lệch (gradient) biến thành bulk transport

Diffusion tốt ở short distance; dòng chảy khối (bulk flow) tốt ở long distance.

Với ideal laminar flow trong cylindrical tube, Poiseuille relation:

\[
Q=\frac{\pi\Delta P r^4}{8\eta L}
\]

Radius xuất hiện lũy thừa 4. Vì vậy thay đổi nhỏ arteriole radius có effect rất lớn lên flow/resistance.

Điều này giải thích tại sao smooth muscle quanh vessel là control point mạnh của circulation.

## 16. Số Reynolds (Reynolds number): khi flow laminar hay turbulent?

Một dimensionless number quan trọng:

\[
Re=\frac{\rho vL}{\mu}
\]

Nó so inertial force với viscous force. Low Re thường laminar hơn; high Re tăng tendency turbulent tùy geometry.

Dòng máu (blood flow) ở nhiều small vessel laminar, nhưng turbulence có thể tăng ở high velocity hoặc irregular geometry.

Dimensionless number giúp compare system khác scale.

## 17. Compliance: vessel không phải pipe cứng

Mạch máu (blood vessel) deform dưới pressure. **Compliance** gần:

\[
C=\frac{\Delta V}{\Delta P}
\]

Artery elasticity giúp smooth pulsatile output của heart. Stiff vessel làm pulse pressure thay đổi và tăng load lên heart.

Mechanics của material vì vậy trực tiếp thành physiology.

## 18. Căng thẳng (stress), strain và viscoelastic tissue

Stress gần force/area; strain là relative deformation.

Bone, tendon, cartilage và vessel không phải ideal spring. Nhiều tissue **viscoelastic**: response phụ thuộc cả deformation và tốc độ (rate)/time.

Cartilage có thể creep dưới load lâu; tendon store elastic energy; cell cảm ECM stiffness qua integrin.

Mechanical property đi thẳng vào signaling và biểu hiện gen (gene expression) qua mechanotransduction.

## 19. Laplace-like reasoning trong alveoli và vessel

Surface tension và curvature tạo áp suất mối quan hệ (relationship). Trong simplified spherical model:

\[
\Delta P\propto\frac{2\gamma}{r}
\]

Small alveolus sẽ cần pressure cao hơn nếu surface tension giống nhau. Pulmonary surfactant giảm surface tension, giúp ổn định alveoli và giảm work of breathing.

Một relation physics giải thích vì sao một biochemical secretion là essential cho lung function.

## 20. Điều khiển phản hồi (feedback control): homeostasis như điều hòa động (dynamic regulation)

Phản hồi âm (negative feedback) gồm sensor, điều khiển logic và bộ phận đáp ứng (effector). Nhưng biological điểm đặt (set point) có thể shift; control distributed; delay và nonlinear response phổ biến.

Glucose, nhiệt độ (temperature), huyết áp (blood pressure) và trục nội tiết (endocrine axis) đều có feedback motif.

Engineering language giúp hỏi: bộ cảm nhận (sensor) ở đâu? delay bao nhiêu? gain mạnh quá có oscillate không? nhiễu động (disturbance) đi vào point nào?

## 21. Phản hồi dương (positive feedback) và ngưỡng (threshold)

Điện thế hoạt động (action potential) khử cực (depolarization) mở thêm Na⁺ channel; clotting cascade activate thêm component; labor contraction tăng oxytocin.

Phản hồi dương amplifies response nhưng cần stop condition. Nếu không, runaway xảy ra.

Kết hợp positive + phản hồi âm thường tạo công tắc (switch) ổn định hơn.

## 22. Dao động (oscillation): rhythm có thể emerge từ feedback delay

Circadian clock, respiratory rhythm và chu kỳ tế bào (cell cycle) có periodic dynamics.

Phản hồi âm + delay + tính phi tuyến (nonlinearity) là motif chung tạo oscillator.

Một static diagram không thể cho biết period hoặc phase. Sinh học động cần time dimension.

## 23. Phản ứng–khuếch tán (reaction–diffusion): local chemistry có thể tạo spatial pattern

Activator và inhibitor có sự tạo ra (production)/diffusion khác nhau có thể tự tạo mẫu hình (pattern). Turing-type phản ứng–khuếch tán model minh họa cách stripe/spot có thể emerge từ local rule.

Developmental pattern không nhất thiết cần mỗi cell có coordinate prewritten. Gradient và local interaction có thể tạo spatial information.

## 24. Scaling law và allometry

Nhiều đại lượng sinh học (biological quantity) scale theo body mass:

\[
Y=aM^b
\]

Log transform:

\[
\log Y=\log a+b\log M
\]

Giúp estimate exponent \(b\). Nhưng exponent có thể khác taxon/phạm vi (range); không nên biến một empirical scaling thành universal law không context.

Scale thay constraint sinh lý học (physiology), life history và sinh thái học (ecology).

## 25. Lý thuyết thông tin (information theory): uncertainty chứ không phải semantic meaning

Shannon entropy:

\[
H=-\sum_i p_i\log_2p_i
\]

đo uncertainty của distribution. Nó hữu ích cho sequence diversity, coding và communication.

Nhưng Shannon information không tự chứa ý nghĩa sinh học (biological meaning). DNA sequence có function vì molecular system interpret nó; lý thuyết thông tin chỉ formalize uncertainty/năng lực (capacity).

## 26. Nhiễu (noise): intrinsic, extrinsic và phép đo (measurement)

Biểu hiện gen fluctuates vì reaction stochastic. Cell khác size/state tạo extrinsic variability. Instrument thêm nhiễu đo lường (measurement noise).

Ba loại variation phải tách nếu muốn hiểu mechanism.

System có thể buffer noise bằng phản hồi âm, averaging molecule hoặc redundancy; đôi khi noise lại tạo bet-hedging.

## 27. Tính bền vững, redundancy và fragility

Redundant pathway giúp system survive failure. Nhưng redundancy có energy cost và có thể tạo hidden vulnerability.

Một network robust với single perturbation có thể fragile với combination perturbation.

Đây là logic của synthetic lethality và khả năng phục hồi hệ sinh thái (ecosystem resilience).

## 28. Trade-off: không có optimization một chiều

Hệ miễn dịch (immune system) nhạy tăng pathogen defense nhưng tăng autoimmunity risk. Tốc độ đột biến (mutation rate) cao tăng adaptation speed nhưng tăng deleterious load. Thick armor tăng protection nhưng giảm mobility.

Biological design gần như luôn multi-objective dưới constraint.

Evolution không tìm global optimum; nó thay đổi local population qua available variation và history.

## 29. Optimization và fitness landscape

Ta có thể hình dung genotype/phenotype như point trên fitness landscape. Selection làm population có tendency tăng representation ở region fitness cao, nhưng drift, mutation và constraint vẫn tác động.

Landscape cũng thay khi environment hoặc species khác thay đổi. Vì vậy optimum không cố định.

Engineering optimization hữu ích như analogy, nhưng biological objective không được engineer định trước.

## 30. Điều khiển, khả năng quan sát (observability) và hidden state

Trong engineering, hệ thống (system) **observable** nếu internal state có thể infer từ đầu ra (output) đủ tốt. Biology thường partially observable: hormone concentration không cho toàn state; biểu hiện gen snapshot không cho full history.

Điều này giải thích vì sao multiple measurement layer và time-series quan trọng. Hidden state là challenge central của physiology và sinh học hệ thống (systems biology).

## 31. Network theory: cấu trúc liên kết (topology) ảnh hưởng dynamics nhưng không quyết định hết

Nút (node)–edge graph giúp mô tả truyền tín hiệu (signaling), protein interaction hoặc lưới thức ăn (food web). Degree, motif và quần xã (community) structure hữu ích.

Nhưng edge type, strength, sign và delay cũng quan trọng. Cùng topology với parameter khác có thể behavior khác.

Graph là representation, không phải full system.

## 32. Engineering modularity và biological context

Module giúp reasoning: receptor module, signaling module, metabolic module. Nhưng module share ATP, ribosome, membrane và metabolite.

Mạch sinh học tổng hợp (synthetic circuit) có thể fail vì resource competition dù logical diagram đúng.

Biology dạy một lesson engineering ngược lại: interface không bao giờ hoàn toàn context-free trong living system.

## 33. Tình huống phân tích (case study): vận chuyển oxy (oxygen delivery) nối 5 principle cùng lúc

Oxygen diffuses qua alveolar membrane theo chênh lệch (gradient). Large alveolar area và hàng rào mỏng (thin barrier) tăng transfer. Blood dòng chảy khối mang O₂ xa. Hemoglobin binding tăng sức chứa môi trường (carrying capacity). Cung lượng tim (cardiac output) và vessel radius điều chỉnh delivery.

Một physiological function duy nhất nối diffusion + geometry + binding equilibrium + động lực học chất lưu (fluid dynamics) + điều khiển phản hồi.

Đây là kiểu synthesis nên hướng tới thay vì thuộc riêng từng equation.

## 34. Tình huống phân tích: điện thế hoạt động nối electrochemistry và phản hồi

Na⁺ gradient chứa electrochemical energy. Khử cực mở voltage-gated Na⁺ channel, gây thêm khử cực — phản hồi dương. K⁺ channel và Na⁺ channel inactivation terminate spike. Pump về lâu dài restore gradients.

Điện thế hoạt động vì vậy là dynamic event của gradient + nonlinear conductance + phản hồi, không phải “electricity chạy dọc dây”.

## 35. Tình huống phân tích: ecosystem tipping point và tế bào switch dùng cùng math intuition

Gene circuit có tính lưỡng ổn (bistability); shallow lake cũng có trạng thái ổn định thay thế (alternative stable state). Scale khác nhau nhưng cả hai có phản hồi dương, threshold và hiện tượng trễ (hysteresis).

Đây là sức mạnh của mathematical abstraction: không nói hai hệ thống giống nhau về vật chất, mà nhận ra **cùng dynamical motif**.

## 36. Các hiểu lầm phổ biến (common misconceptions)

“Biology chỉ là applied chemistry” bỏ qua organization, history và emergence.

“Equation có nghĩa system deterministic hoàn toàn” sai; tính ngẫu nhiên (stochasticity) và độ bất định của mô hình (model uncertainty) vẫn tồn tại.

“Engineering analogy chứng minh organism được thiết kế” sai; analogy chỉ giúp phân tích control/chức năng (function).

“Mô hình đơn giản là sai vì reality phức tạp” cũng sai. Mô hình (model) đơn giản hữu ích nếu giữ đúng relationship cho câu hỏi cụ thể.

## 37. Mô hình tư duy tổng hợp

Các principle xuyên library có thể map như sau:

```text
gradient
→ diffusion / osmosis / membrane potential / chemiosmosis

feedback
→ enzyme control / signaling / homeostasis / ecosystem resilience

flow
→ metabolism / circulation / nutrient cycle

information
→ DNA / neural coding / signaling / measurement

constraint
→ morphology / trade-off / evolutionary adaptation

network
→ gene regulation / metabolism / nervous system / food web
```

Mục tiêu cuối cùng không phải nhớ thêm hàng chục formula, mà biết **formula nào là model của relation nào và tại sao relation đó tái xuất ở scale khác**.

<!-- depth-audit-2026:structure-mechanism-failure -->
## Một template reasoning dùng từ molecule tới ecosystem

Khi gặp bất kỳ system sinh học nào, hãy đi theo sáu câu hỏi liên tục. **Structure** xác định degree of freedom và constraint vật lý. **Mechanism** mô tả flow của matter/energy/information. **Regulation** cho biết feedback nào giữ state trong vùng hoạt động. **Function** là capability xuất hiện ở scale cao hơn. **Failure** cho thấy boundary condition bị vượt hoặc control mất ổn định. **Adaptation/evolution** giải thích vì sao architecture hiện tại tồn tại và trade-off nào nó chấp nhận.

Ví dụ membrane có phospholipid bilayer (structure) → selective diffusion/transport (mechanism) → pump/channel regulation (regulation) → giữ internal environment (function) → ATP depletion gây gradient collapse (failure) → lipid composition và transporter family thay đổi theo môi trường qua adaptation/evolution.

Cùng template áp dụng cho kidney, immune system, development, food web và synthetic circuit. Nó ngăn library trở thành atlas tên gọi vì mỗi component chỉ có ý nghĩa khi được đặt trong causal system.

## 38. Bridge về toàn bộ Knowledge Library

Nếu quay lại chapter đầu [Cách tư duy trong Sinh học](../00_foundations/00_scientific_thinking_scale_and_models.md), ta thấy vòng tròn khép lại. Ban đầu ta học cách hỏi về scale, vật chất (matter), năng lượng (energy), information và phản hồi. Sau toàn library, những từ đó không còn abstract: chúng có equation, mechanism và tình huống phân tích cụ thể.

Đó là mô hình tư duy cuối cùng của Biology Knowledge Library: sự sống là hệ vật chất xa equilibrium, dùng gradient và reaction để duy trì organization, dùng information để điều phối và truyền heredity, dùng feedback để điều khiển, và thay đổi qua evolution dưới constraint của Physics, Chemistry và history.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Biology × Mathematics × Computation × Scale](00_biology_math_computation_and_scale.md) · [Mục lục Biology](../README.md)
