# Sinh học hệ thống, mô hình hóa và sinh học tổng hợp — Systems Biology, Modeling and Synthetic Biology (시스템 생물학, 모델링과 합성생물학)

Khi đã đo hàng nghìn gene, protein và metabolite, một giới hạn mới xuất hiện: **biết danh sách component không đồng nghĩa hiểu behavior của system**. Một signaling network có thể tạo công tắc (switch), oscillation hoặc adaptation tùy feedback. Hai gene có thể gần như không gây phenotype khi perturb riêng nhưng gây effect rất lớn khi perturb cùng nhau. Một metabolite có concentration gần như không đổi dù dòng chuyển hóa (flux) qua pathway tăng nhiều lần.

**Sinh học hệ thống (systems biology / 시스템 생물학)** tập trung vào interaction, dynamics và nổi trội (emergent) hành vi (behavior). **Sinh học tổng hợp (synthetic biology / 합성생물학)** đi thêm một bước: dùng hiểu biết về hệ thống (system) để thiết kế circuit hoặc metabolic state mới.

> **Mô hình tư duy (mental model):** sinh học phân tử (molecular biology) hỏi “part này làm gì?”. Sinh học hệ thống hỏi “network của nhiều part tạo dynamics gì?”. Sinh học tổng hợp hỏi “nếu thay topology hoặc parameter, ta có tạo behavior dự đoán được không?”.

## 1. Network diagram chưa phải dynamic model

Một pathway A → B → C chỉ nói direction tương tác. Nó chưa nói rate, delay, bão hòa (saturation), định vị (localization) hay phân giải (degradation).

Nếu A activate B rất chậm còn B degrade rất nhanh, behavior khác hẳn khi activation nhanh và degradation chậm. Vì vậy topology là skeleton; dynamics cần parameter.

Điểm này rất quan trọng khi đọc pathway figure: arrow là hypothesis về relation, không phải full prediction.

## 2. Rate of change là ngôn ngữ tự nhiên của dynamic biology

Nếu B được tạo theo A và degraded theo B hiện tại:

\[
\frac{dB}{dt}=k_{on}A-k_{off}B
\]

Equation không chỉ là toán. Nó buộc ta phát biểu rõ: production phụ thuộc gì, loss phụ thuộc gì, variable nào thay đổi theo time.

Khi \(dB/dt=0\), B ở **trạng thái ổn định (steady state)**, nhưng production và degradation vẫn có thể diễn ra liên tục.

## 3. Trạng thái ổn định không đồng nghĩa cân bằng nhiệt động (thermodynamic equilibrium)

Cell sống thường duy trì **non-equilibrium trạng thái ổn định**. ATP được tạo và tiêu thụ liên tục. Ion được pump ra rồi leak vào. Glucose blood có thể gần ổn định dù uptake và release xảy ra liên tục.

Cân bằng nhiệt động thực sự sẽ làm nhiều gradient collapse. Life cần dòng năng lượng (energy flow) để giữ system xa equilibrium.

Đây là connection trực tiếp giữa thermodynamics và cân bằng nội môi (homeostasis).

## 4. Sự tạo ra (production)–phân giải model và hằng số thời gian (time constant)

Mô hình (model) đơn giản:

\[
\frac{dX}{dt}=\alpha-\beta X
\]

Trạng thái ổn định:

\[
X^*=\frac{\alpha}{\beta}
\]

Nhưng còn một information khác: tốc độ system tiến tới trạng thái ổn định phụ thuộc \(\beta\). Molecule degrade nhanh phản ứng nhanh hơn với change, nhưng phải tốn energy để resynthesize liên tục.

Biology thường trade-off **responsiveness vs resource cost**.

## 5. Saturation làm response nonlinear

Enzym (enzyme), receptor và transporter có capacity hữu hạn. Michaelis–Menten-like relation:

\[
v=\frac{V_{max}[S]}{K_m+[S]}
\]

Ở substrate thấp, response gần linear. Ở cao, system saturate.

Tính phi tuyến (nonlinearity) là nền cho ngưỡng (threshold), ultrasensitivity và công tắc. Nếu cứ giả định relation tuyến tính, ta sẽ bỏ lỡ nhiều behavior quan trọng.

## 6. Phản hồi âm (negative feedback) tạo stability nhưng có thể tạo dao động (oscillation)

Phản hồi âm làm output giảm upstream drive. Metabolic end product inhibit enzyme đầu; glucose–insulin regulation giảm deviation; gene product có thể repress transcription của chính nó.

Phản hồi (feedback) giúp disturbance decay nhanh hơn và giảm variation. Nhưng nếu feedback có delay lớn hoặc gain quá mạnh, system có thể overshoot và oscillate.

Lý thuyết điều khiển (control theory) giúp ta thấy stability không chỉ phụ thuộc “có phản hồi hay không” mà cả strength và delay.

## 7. Phản hồi dương (positive feedback) tạo memory và tính lưỡng ổn (bistability)

Nếu X kích hoạt production của chính nó, system có thể có hai stable state: low và high.

Một transient signal có thể đẩy system qua ngưỡng, sau đó high state tự duy trì. Đây là **tính lưỡng ổn (쌍안정성)**.

Biệt hóa tế bào (cell differentiation) và tế bào (cell)-cycle transition thường có công tắc-like motif. Phản hồi dương biến graded input thành discrete decision.

## 8. Hiện tượng trễ (hysteresis): threshold bật và threshold tắt có thể khác nhau

Trong bistable system, input cần để bật state high có thể cao hơn input cần để giữ state high. Khi giảm input, system không quay lại ngay đường cũ.

Đây là **hiện tượng trễ**, cùng concept đã gặp ở ecosystem alternative states. Một motif mathematical có thể xuất hiện từ gene circuit đến lake ecology.

## 9. Feed-forward loop tạo filter thời gian

Nếu A activate C trực tiếp và cũng activate B, còn B activate C, C có thể yêu cầu signal A tồn tại đủ lâu để cả hai path cùng active.

Coherent feed-forward loop vì vậy có thể lọc pulse ngắn.

Mạng lưới (network) topology tự thực hiện computation về duration mà không cần central processor.

## 10. Oscillator cần feedback + delay + tính phi tuyến

Nhịp sinh học ngày đêm (circadian rhythm), tế bào-cycle oscillator và many mạch sinh học tổng hợp (synthetic circuit) tạo periodic dynamics.

Phản hồi âm với delay có thể làm output lên xuống. Phản hồi dương có thể sharpen transition. Degradation rate quyết định period.

Snapshot omics ở một time point có thể bỏ hoàn toàn phase information; time-series vì vậy quan trọng khi system oscillatory.

## 11. Tính ngẫu nhiên (stochasticity): khi molecule count thấp, average không đủ

Nếu chỉ có vài yếu tố phiên mã (transcription factor) phân tử (molecule), reaction event riêng lẻ gây fluctuation lớn. Continuous ODE approximation có thể không capture distribution.

**Stochastic model** mô tả reaction event probabilistically. Gillespie-style simulation chọn event và thời gian dựa trên propensity.

Noise có thể làm genetically identical cell vào state khác nhau. Trong bacterial persistence hoặc developmental fate, tính ngẫu nhiên có functional consequence.

## 12. Population average có thể che tính lưỡng ổn

Nếu nửa cell OFF và nửa ON, bulk measurement có thể cho average 50%. Nhưng không cell nào thật sự ở 50% trạng thái (state).

Single-tế bào measurement vì vậy cần thiết để phân biệt continuous shift với mixture state.

Đây là cầu nối (bridge) giữa sinh học hệ thống và đo tế bào dòng chảy (flow cytometry)/single-cell omics.

## 13. Phân tích độ nhạy (sensitivity analysis): parameter nào thật sự kiểm soát output?

Model có hàng chục parameter. **Phân tích độ nhạy** hỏi output thay đổi bao nhiêu khi parameter thay đổi.

Nếu small change ở parameter A làm output đổi lớn, A là sensitive control point. Nếu behavior robust qua range rộng, system có tính bền vững (robustness).

Độ nhạy (sensitivity) giúp chọn experiment nào đáng làm và node nào có tiềm năng intervention.

## 14. Identifiability: fit tốt không nghĩa parameter đúng

Nhiều combination parameter có thể tạo curve giống nhau. Đây là **khả năng nhận dạng tham số (parameter identifiability) vấn đề (problem) (매개변수 식별성)**.

Model có thể fit data đẹp nhưng individual parameter không uniquely determined.

Giải pháp có thể là thêm measurement intermediate, perturb system, dùng prior knowledge hoặc simplify model.

## 15. Overfitting cũng tồn tại trong mô hình cơ chế (mechanistic model)

Thêm nhiều parameter gần như luôn giúp fit training data. Nhưng model phức tạp có thể prediction kém ở condition mới.

Mô hình (model) selection cần balance fit và complexity. AIC/BIC, cross-validation và held-out perturbation giúp, nhưng biological plausibility vẫn quan trọng.

Mục tiêu không phải “fit mọi điểm” mà là capture mechanism đủ để generalize.

## 16. Perturbation phân biệt correlation với causality

Co-expression A và B không cho biết A→B, B→A hay cả hai cùng do C.

Knockout A rồi đo B tạo causal evidence mạnh hơn. Dose perturbation nhiều mức giúp infer nonlinear response. Time-resolved perturbation giúp infer direction.

Sinh học hệ thống mạnh nhất khi model tạo prediction rồi experiment perturb để cố làm prediction sai.

## 17. Genetic interaction: whole lớn hơn hoặc nhỏ hơn tổng effect riêng

Nếu mutation A làm fitness giảm 10% và B giảm 10%, double mutant có thể không đơn giản giảm 20%.

**Genetic interaction (유전적 상호작용)** xảy ra khi double effect khác expectation từ single effect.

**Synthetic lethality** là trường hợp A hoặc B riêng vẫn sống nhưng A+B chết. Đây là network dependency quan trọng trong cancer therapy.

## 18. Epistasis nối genetics cổ điển với network hiện đại

Trong classical genetics, **epistasis** mô tả alen (allele) ở gene này che hoặc thay effect gene khác. Sinh học hệ thống diễn giải điều đó bằng pathway cấu trúc liên kết (topology).

Nếu A tạo cơ chất (substrate) cho B, loss A có thể làm status của B không còn matter. Kiểu hình (phenotype) pattern từ cross có thể giúp suy order pathway.

Một concept Mendel-era vì vậy nối trực tiếp network inference hiện đại.

## 19. Metabolic concentration và flux không giống nhau

Một metabolite concentration ổn định có thể có flux rất cao nếu production và consumption cùng nhanh.

Ví dụ bathtub giữ water level constant dù faucet và drain flow lớn.

Do đó metabolomics đo concentration chưa đủ để biết metabolic rate. Isotope tracing và dòng chuyển hóa model cần khi muốn biết material thực sự đi đâu.

## 20. Stoichiometric matrix và Phân tích cân bằng dòng chuyển hóa (flux balance analysis)

Mạng lưới chuyển hóa (metabolic network) có thể biểu diễn bằng stoichiometric matrix \(S\) và flux vector \(v\). Ở steady-state approximation:

\[
Sv=0
\]

Sau đó ràng buộc (constraint) đặt upper/lower bound cho dòng chuyển hóa, và optimization chọn solution theo objective như biomass production.

**Phân tích cân bằng dòng chuyển hóa, FBA** mạnh vì không cần mọi kinetic parameter, nhưng objective assumption là giới hạn (limitation). Microbe trong natural ecosystem không luôn maximize growth như lab culture.

## 21. Control coefficient phân bố qua mạng lưới (network)

Một misconception cổ điển là “một enzyme rate-limiting duy nhất kiểm soát whole pathway”. Trong network thật, control thường phân bố.

Tăng enzyme A 10× có thể không tăng flux nếu enzyme B hoặc substrate supply trở thành bottleneck mới.

Kỹ thuật chuyển hóa (metabolic engineering) vì vậy cần systems view, không chỉ overexpress một gene.

## 22. Multi-scale modeling: molecular state phải gặp tissue geometry

Tumor growth có molecular signaling trong tế bào, phân chia tế bào (cell division)/sự di chuyển (migration) ở mô (tissue), oxy (oxygen) diffusion từ vessel và immune-cell movement.

Mỗi scale dùng variable/time step khác nhau. Mô hình đa quy mô (multi-scale model) nối ODE, agent-based model và diffusion equation.

Khó khăn chính không chỉ computational; nó là quyết định information nào cần pass giữa scale.

## 23. Sinh học tổng hợp: xây circuit để kiểm tra principle

Sinh học tổng hợp dùng promoter, repressor, ribosome binding site, enzyme và sensor như module.

Nếu hai repressor inhibit nhau, circuit có thể tạo toggle switch. Nếu phản hồi âm có delay, circuit có thể oscillate.

Engineering circuit là cách mạnh để test sufficiency: topology dự đoán có thật sự tạo behavior không?

## 24. Tính mô-đun (modularity) trong cell không sạch như electronics

Electronic component có interface khá ổn định. Biological circuit share ribosome, polymerase, ATP, axit amin (amino acid) và membrane space.

Khi synthetic construct expression quá mạnh, nó tạo **resource burden**, làm host growth giảm và indirectly thay circuit behavior.

Vì vậy module interaction có thể tồn tại dù diagram không vẽ edge.

## 25. Context dependence là challenge central của sinh học tổng hợp

Cùng promoter có thể hoạt động khác tùy host strain, copy number, tốc độ tăng trưởng (growth rate) và genomic insertion site.

Biological part có history và môi trường (environment). Standardization hữu ích nhưng không xóa context.

Điều này dạy ngược lại về natural biology: function của gene cũng phụ thuộc network bối cảnh (context).

## 26. Kỹ thuật chuyển hóa là optimization dưới constraint

Muốn cell tạo product P, ta có thể tăng precursor supply, knock out competing pathway, balance redox cofactor, improve transporter hoặc reduce toxicity.

Nhưng mỗi modification có trade-off với growth và stability.

Engineering problem thường multi-objective: maximize product nhưng giữ cell sống đủ lâu và circuit không bị evolution phá nhanh.

## 27. Biosensor: biology như measurement device

Biosensor có input module nhận molecule, processing module và output như huỳnh quang (fluorescence)/electrical signal.

Metric gồm sensitivity, độ đặc hiệu (specificity), dải động (dynamic range), response time, leak và nhiễu (noise).

Biosensor nối experimental measurement với synthetic design: ta dùng biology để đo biology hoặc environment.

## 28. Tế bào-free system: giảm context để prototype nhanh

Tế bào-free expression dùng extract hoặc purified machinery ngoài living cell. Nó bỏ ràng buộc growth và màng (membrane), dễ control reagent.

Nhưng result không tự translate sang cell vì resource competition, degradation và compartment khác.

Tế bào-free giống simplified model: useful để isolate principle, nhưng phải validate lại in vivo.

## 29. Evolution là một “failure mode” của engineered circuit — và cũng là thiết kế (design) áp suất (pressure)

Synthetic construct gây burden có thể bị mutation làm mất function; mutant grow nhanh hơn và chiếm population.

Do đó engineered biology phải nghĩ đến **độ ổn định tiến hóa (evolutionary stability)**. Design tốt không chỉ hoạt động ngày đầu mà còn phải giữ chức năng (function) qua generation.

Sinh học tổng hợp vì vậy buộc engineering phải học evolution.

## 30. Digital twin và predictive biology

Ý tưởng digital twin là mô hình đủ tốt để predict state của cell, tissue hoặc patient dưới intervention.

Nhưng hệ thống sinh học (biological system) high-dimensional, partially observed và history-dependent. Vì vậy current “digital twin” nên được hiểu như hierarchy model với uncertainty, không phải bản sao hoàn hảo.

Prediction useful vẫn có thể đạt được mà không cần model mọi molecule.

## 31. Dữ liệu (data)-driven và mô hình cơ chế bổ sung nhau

ML mạnh khi pattern phức tạp và data lớn. Mô hình cơ chế mạnh khi relation causal/physical đã biết.

Hybrid model có thể dùng neural network estimate unknown function nhưng giữ mass balance hoặc thermodynamic constraint.

Tương lai quantitative biology nhiều khả năng là integration, không phải “AI thay thế cơ chế (mechanism)”.

## 32. Xác thực mô hình (model validation) phải dựa trên prediction chưa dùng để fit

Một model fit data dùng để xây nó chỉ chứng minh compatibility. Stronger test là predict perturbation hoặc condition mới.

Ví dụ mô hình signaling predict knockout A sẽ tăng B sau 30 phút. Nếu experiment mới confirm temporal response, confidence tăng mạnh.

Science tiến bộ bằng cycle prediction → test → revision.

## 33. Uncertainty phải đi cùng prediction

Mô hình parameter không chắc, measurement noisy, structure có thể sai. Prediction nên có interval hoặc scenario range khi phù hợp.

Một point estimate duy nhất dễ tạo false precision.

Uncertainty không làm model yếu; explicit uncertainty làm decision tốt hơn.

## 34. Ethics và biosafety không phải appendix ngoài science

Gene drive, engineered vi sinh vật (microorganism) và clinical gene editing có benefit nhưng cũng ecological/social risk.

Question cần xem containment, reversibility, off-target, horizontal transfer, informed consent và governance.

Technical feasibility không tự quyết định acceptability. Thiết kế process cần risk model cùng lúc với performance mô hình.

## 35. Tình huống phân tích (case study): lactose-like genetic switch như exercise tư duy hệ thống (systems thinking)

Giả sử nutrient S activate regulator, regulator bật transporter T, transporter làm S đi vào cell nhanh hơn. Đây là positive loop. Nhưng khi S được metabolize, intracellular S giảm, tạo negative effect.

Chỉ bằng topology, ta đã có thể hỏi: system có threshold không, adaptation không, tính lưỡng ổn không? Sau đó measurement time-course giúp phân biệt model.

Sinh học hệ thống biến “pathway diagram” thành câu hỏi prediction.

## 36. Tình huống phân tích: drug combination và network redundancy

Drug A block pathway 1 nhưng cell sống nhờ con đường (pathway) 2. Drug B block pathway 2 nhưng pathway 1 đủ bù. Combination A+B gây collapse.

Nếu chỉ study single drug, ta có thể kết luận cả hai target “không quan trọng”. Network view reveal redundancy.

Đây là lý do combination therapy và genetic interaction map quan trọng trong cancer/infectious disease research.

## 37. Các hiểu lầm phổ biến (common misconceptions)

“Có network diagram nghĩa đã hiểu system” là sai; topology không đủ động lực học (dynamics).

“Model fit data nghĩa mechanism đúng” sai; nhiều model có thể fit cùng output.

“Sinh học tổng hợp biến cell thành machine deterministic” sai; nhiễu, evolution và context vẫn tồn tại.

“AI càng lớn thì không cần experiment” sai; prediction causal và distribution shift vẫn cần validation.

## 38. Mô hình tư duy tổng hợp

Modern sinh học hệ thống vận hành như vòng lặp:

```text
measure
→ represent network
→ formulate model
→ estimate parameter
→ predict
→ perturb system
→ compare prediction with reality
→ revise model
```

Sinh học tổng hợp thêm một nhánh:

```text
model principle
→ design circuit
→ build
→ test
→ learn context/constraint
→ redesign
```

Đây là biology dưới dạng iterative science + engineering.

## 39. Synthesis với toàn Knowledge Library

Nhìn lại từ đầu, same motifs xuất hiện ở mọi scale: gradient tạo vận chuyển (transport); feedback tạo điều khiển (control); selection tạo thích nghi (adaptation); network tạo emergence; constraint tạo trade-off.

Sinh học hệ thống chỉ làm các motif đó explicit bằng equation và thí nghiệm (experiment). Nó không thay thế sinh học tế bào (cell biology), di truyền học (genetics) hay sinh thái học (ecology); nó cung cấp một language chung để nối chúng.

Đi tiếp sang [Biology × Mathematics × Computation × Scale](../90_connections/00_biology_math_computation_and_scale.md) và [Sinh học nhìn qua Vật lý, Hóa học và Kỹ thuật](../90_connections/01_biology_physics_chemistry_and_engineering.md) để tổng hợp các pattern định lượng xuyên toàn thư viện.

<!-- depth-audit-2026:control-observability-evolution -->
## Observability và controllability: biết state không đồng nghĩa điều khiển được system

Trong control theory, **khả năng quan sát (observability)** hỏi internal state có thể suy ra từ measurement hay không; **khả năng điều khiển (controllability)** hỏi input có thể đưa system tới state mong muốn hay không. Biology thường thiếu cả hai: ta chỉ đo một subset molecule, còn intervention tác động nhiều pathway ngoài ý muốn.

Điều này giải thích vì sao model fit data tốt chưa chắc useful cho intervention. Hai parameter set có thể tạo output giống nhau (**non-identifiability**), nhưng phản ứng khác khi perturb. Experiment tốt phải được thiết kế để phân biệt model, không chỉ thu thêm cùng loại data.

Robustness và evolvability cũng tạo trade-off. Feedback âm giúp giữ output trước disturbance, nhưng redundancy có thể che mutation; modularity hạn chế damage lan rộng nhưng tạo interface mới cho evolution. Synthetic circuit chạy tốt ngày đầu có thể bị mutation phá nếu circuit gây cost cho cell; selection ưu tiên host clone tăng trưởng nhanh hơn chứ không ưu tiên mục tiêu engineer.

Vì vậy synthetic biology cần nghĩ theo hai vòng feedback: engineering control trong một cell và evolutionary selection giữa nhiều cell qua generation. Design bền phải xét cả hai scale.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Bioinformatics, thuật toán và Omics Workflow](02_bioinformatics_algorithms_and_omics_workflows.md) · [Mục lục Biology](../README.md) · [Biology × Mathematics × Computation × Scale →](../90_connections/00_biology_math_computation_and_scale.md)
