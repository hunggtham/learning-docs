# Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and Measurement (생물학 실험 방법과 측정)

Cho đến đây, ta chủ yếu hỏi **sự sống hoạt động như thế nào**. Nhưng science còn một câu hỏi nền tảng khác: **làm sao ta biết điều đó?** Mọi khẳng định sinh học (biological claim) cuối cùng phải nối với observation, measurement hoặc experiment. Nếu không hiểu quy trình đo lường (measurement process), ta rất dễ nhầm artifact với biology, correlation với causation, hoặc signal máy đo với đại lượng sinh học (biological quantity) thực.

Chapter này không phải manual protocol. Mục tiêu là xây mô hình tư duy (mental model) từ câu hỏi → thiết kế → đo → dữ liệu → suy luận (inference). Hiển vi (microscopy), PCR, western blot, đo tế bào dòng chảy (flow cytometry) và sequencing chỉ là những implementation khác nhau của cùng một logic.

> **Mô hình tư duy:** experiment là một pipeline biến reality thành data. Mỗi bước — lấy mẫu (sampling), chuẩn bị (preparation), thiết bị đo (instrument), tiền xử lý (preprocessing), thống kê (statistic) — đều có thể làm mất information hoặc tạo sai lệch (bias). Vì vậy interpretation đúng cần hiểu cả biology lẫn hệ thống đo lường (measurement system).

## 1. Từ biological concept đến biến thao tác (operational variable)

Một câu hỏi như “gene X làm cell tăng trưởng nhanh hơn không?” vẫn quá mơ hồ để test. Ta phải chuyển concept thành **biến thao tác**.

“Gene X activity” có thể được thao tác bằng knockout, knockdown, CRISPRi, overexpression hoặc pharmacological inhibition. “Sinh trưởng (growth)” có thể đo bằng cell count, biomass, DNA synthesis, confluence, ATP signal hoặc proliferation marker.

Nhưng mỗi proxy đo một aspect khác nhau. Cell count tăng có thể do division nhanh hơn hoặc chết tế bào (cell death) ít hơn. ATP signal tăng có thể do metabolism tăng mà cell number không đổi.

Do đó câu hỏi experimental đầu tiên luôn là: **measurement này đại diện cho đại lượng sinh học nào, và những process khác nào cũng có thể thay measurement đó?**

## 2. Độ hợp lệ của cấu trúc đo lường (construct validity): đo đúng thứ mình nghĩ đang đo chưa?

Một assay có thể technically chính xác nhưng conceptually sai. Đây là vấn đề **độ hợp lệ của cấu trúc đo lường**.

Ví dụ dùng một marker protein (protein) để gọi “tế bào gốc (stem cell)” giả định marker đó đại diện đầy đủ cho stemness. Nhưng stemness là functional state gồm self-renewal, differentiation potential và niche dependence. Một marker đơn lẻ có thể không capture hết.

Khi đọc paper, hãy tách hai câu: “instrument có đo chính xác fluorescence không?” và “huỳnh quang (fluorescence) đó có thật sự đại diện cho biological concept không?”.

## 3. Control là logic của causal inference

**Đối chứng âm (negative control)** cho biết signal có xuất hiện khi thành phần nhân quả (causal component) bị bỏ không. **Đối chứng dương (positive control)** cho biết system có khả năng tạo tín hiệu mong đợi (expected signal). **Đối chứng dung môi (vehicle control)** tách effect của solvent khỏi compound. **Đối chứng không khuôn (no-template control)** trong PCR giúp phát hiện contamination.

Control không phải thủ tục phụ. Nó tạo comparison cần thiết để phân biệt cách giải thích thay thế (alternative explanation).

Nếu nhóm can thiệp (treatment group) tăng fluorescence nhưng đối chứng dung môi cũng tăng tương tự, diễn giải (interpretation) “drug có effect” yếu đi mạnh. Control chính là cách experiment tạo tình huống phản thực (counterfactual) gần đúng: điều gì sẽ xảy ra nếu chỉ thiếu factor mà ta quan tâm?

## 4. Ngẫu nhiên hóa (randomization), blinding và yếu tố gây nhiễu (confounder)

Một **yếu tố gây nhiễu (biến gây nhiễu / 교란 변수)** ảnh hưởng cả condition và kết quả (outcome), làm ta nhầm association với causation.

Nếu toàn mẫu đối chứng (control sample) chạy sáng nay còn mẫu can thiệp (treatment sample) chạy ngày mai, độ trôi của máy (machine drift) hoặc lô thuốc thử (reagent batch) có thể bị nhầm thành hiệu ứng can thiệp (treatment effect). Ngẫu nhiên hóa giúp phân bố yếu tố gây nhiễu chưa biết (unknown confounder) giữa group. Làm mù (blinding) giảm bias khi scoring có yếu tố subjective.

Good thiết kế thí nghiệm (experiment design) phải nghĩ trước về sai lệch, không đợi statistic “sửa” sau.

## 5. Lần lặp kỹ thuật (technical replicate) và lần lặp sinh học (biological replicate) trả lời hai câu khác nhau

**Lần lặp kỹ thuật** lặp measurement trên cùng vật liệu sinh học (biological material), giúp estimate nhiễu đo lường (measurement noise). **Lần lặp sinh học** dùng sample independent, giúp estimate biến thiên sinh học (biological variability).

Đo cùng sample 20 lần không tạo n=20 lần lặp sinh học. Nó chỉ cho ta biết instrument/quá trình (process) độ chụm (precision).

Đây là một lỗi rất phổ biến: pseudoreplication làm độ tin cậy thống kê (statistical confidence) bị phóng đại vì observation không independent.

## 6. Độ chính xác (accuracy), độ chụm, độ nhạy (sensitivity), specificity và độ phân giải (resolution)

**Độ chính xác (정확도)** là gần giá trị thực (true value) đến đâu. **Độ chụm (정밀도)** là phép đo lặp lại (repeated measurement) gần nhau đến đâu. Một máy có thể precision cao nhưng sai calibration nên accuracy thấp.

**Độ nhạy** hỏi assay detect positive case tốt đến đâu; **độ đặc hiệu (specificity)** hỏi tránh dương tính giả (false positive) tốt đến đâu. **Độ phân giải** hỏi phân biệt hai state gần nhau được không.

Trong hiển vi, magnification không đồng nghĩa resolution. Trong giải trình tự (sequencing), high depth không tự bảo đảm accuracy nếu sai số hệ thống (systematic error) tồn tại. Các metric phải được hiểu theo cơ chế đo lường (measurement mechanism).

## 7. Hiệu chuẩn (calibration): signal máy đo phải map sang quantity sinh học

Instrument thường cho signal unit, không trực tiếp cho concentration. Calibration dùng standard có known quantity để tạo mapping.

Nếu detector response linear trong một range:

\[
Tín hiệu (signal) = a\times Concentration + b
\]

Nhưng ngoài dải động (dynamic range), detector có thể saturate. Lúc đó signal không tăng tương ứng quantity nữa.

Vì vậy “band đậm gấp đôi” không tự động nghĩa protein gấp đôi nếu exposure saturated.

## 8. Tín hiệu trên nhiễu (signal-to-noise) và giới hạn phát hiện (detection limit)

Measurement luôn gồm signal + nhiễu (noise). Noise có thể đến từ photon counting, background fluorescence, nonspecific binding, sample heterogeneity hoặc instrument biến dị (variation).

**Tỉ lệ tín hiệu trên nhiễu (signal-to-noise ratio), SNR** cao giúp detect difference. Nhưng tăng signal bằng amplification cũng có thể amplify bias.

Giới hạn phát hiện không phải “zero biology dưới threshold”. Nó chỉ nghĩa assay không phân biệt signal khỏi noise đủ tin cậy ở mức đó.

## 9. Hiển vi: image là phép đo (measurement) đã qua optics và processing

Light microscopy tạo image từ interaction giữa light và mẫu (sample). Huỳnh quang microscopy dùng fluorophore để gắn signal vào cấu trúc (structure)/molecule cụ thể.

Label giúp specificity nhưng có thể perturb system. Overexpress fluorescent fusion protein có thể làm concentration phi sinh lý. Fixation giữ morphology nhưng giết cell và tạo nhiễu giả (artifact). Chụp ảnh tế bào sống (live-cell imaging) giữ dynamics nhưng gặp phototoxicity và photobleaching.

Do đó image không phải “nhìn trực tiếp reality”. Nó là output của chuẩn bị mẫu (sample preparation) + optics + detector + reconstruction.

## 10. Diffraction limit và super-độ phân giải

Với conventional light microscopy, resolution gần bị giới hạn bởi diffraction. Abbe approximation:

\[
d\approx\frac{\lambda}{2NA}
\]

Muốn resolution tốt hơn có thể dùng wavelength ngắn hơn hoặc numerical aperture lớn hơn. Super-resolution technique dùng optical/statistical strategy để vượt conventional limit trong condition nhất định.

Quan trọng là “zoom” không tự tạo thông tin (information). Nếu system không resolve được hai object, phóng to chỉ làm blur lớn hơn.

## 11. Electron microscopy: đổi live dynamics lấy ultrastructure

Electron có wavelength hiệu dụng rất ngắn nên EM đạt resolution cao. TEM cho ultrastructure bên trong sample mỏng; SEM mô tả surface morphology.

Nhưng preparation phức tạp và thường không quan sát quá trình sống (live process). Đây là trade-off measurement: chi tiết không gian (spatial detail) cao hơn đổi lấy tính sát sinh lý (physiological realism) thấp hơn.

Không có thiết bị đo “tốt nhất”; chỉ có instrument phù hợp câu hỏi.

## 12. Fractionation và centrifugation: tách system để suy function

Differential centrifugation tách component theo size/density/sedimentation. Density gradient tách tinh hơn.

Lịch sử sinh học tế bào (cell biology) cho thấy nhiều organelle function được khám phá bằng cách fractionate cell rồi assay activity từng fraction. Đây là strategy reductionist có ích: tách system thành component để hỏi function, sau đó phải quay lại integration để hiểu whole cell.

## 13. Electrophoresis: phân tách vật lý (physical separation) thành biological evidence

DNA mang charge âm nhờ phosphate backbone nên migrate trong điện trường (electric field). Gel matrix làm fragment nhỏ đi dễ hơn fragment lớn.

SDS-PAGE làm protein có charge-to-mass tương đối đồng đều, giúp separation chủ yếu theo size.

Band position là chỉ dấu thay thế (proxy) cho size; band intensity gần quantity chỉ trong dải động phù hợp (proper dynamic range). Một band không phải “molecule thật” mà là quần thể (population) phân tử (molecule) được transform thành spatial signal.

## 14. PCR: amplification và nguy cơ hiểu nhầm tăng trưởng theo hàm mũ (exponential growth)

PCR dùng denaturation → primer annealing → extension lặp nhiều cycle. Idealized:

\[
N_n=N_0 2^n
\]

Nhưng real efficiency thấp hơn 100% và giảm khi reagent cạn hoặc product cạnh tranh. PCR điểm cuối (endpoint PCR) vì vậy không quantitative tuyến tính tốt.

qPCR theo dõi signal trong exponential phase. Ct/Cq thấp thường tương ứng starting template nhiều hơn, nhưng comparison cần hiệu suất khuếch đại (amplification efficiency) và normalization hợp lý.

Amplification mạnh làm technique sensitive nhưng cũng làm contamination nhỏ trở thành signal lớn.

## 15. Reverse transcription: mRNA không đồng nghĩa protein

RT-qPCR chuyển RNA thành cDNA rồi amplify. Nó estimate mức độ phong phú của bản phiên mã (transcript abundance).

Nhưng biểu hiện gen (gene expression) có nhiều layer:

```text
DNA
→ transcription
→ RNA stability
→ translation
→ protein modification
→ protein degradation
→ function
```

mRNA tăng không bảo đảm protein tăng tương ứng. Phép đo ở một layer không tự động suy ra layer sau.

## 16. Western blot và kháng thể (antibody) độ đặc hiệu

Western blot separation protein rồi dùng antibody detect target. Interpretation phụ thuộc antibody độ đặc hiệu, loading control, transfer efficiency và exposure range.

Một antibody cross-react protein khác có thể tạo band giả. Loading control cũng có thể thay theo điều trị (treatment).

Strong conclusion thường cần orthogonal validation, ví dụ western + mass spectrometry + functional assay thay vì chỉ một band đẹp.

## 17. ELISA và đường chuẩn (standard curve)

ELISA dùng antibody–antigen interaction và enzym (enzyme)-generated signal. Đường chuẩn map signal sang concentration.

Curve thường nonlinear ở concentration extreme; sample phải nằm trong calibrated range. Dilution series giúp kiểm tra signal có behave hợp lý không.

Điều này là general lesson: **phép đo (measurement) model phải được validated trong phạm vi (range) ta dùng**.

## 18. Đo tế bào dòng chảy: average có thể che distribution

Flow cytometer đo property từng cell. Điều này rất mạnh vì hai sample có cùng mean fluorescence có thể có distribution khác hoàn toàn.

Gating xác định population nào được phân tích. Compensation xử lý spectral overlap. Doublet exclusion tránh hai cell dính nhau bị đọc như một event.

Single-tế bào (cell) measurement vì vậy giàu information hơn bulk average, nhưng analysis choice cũng ảnh hưởng result nhiều hơn.

## 19. FACS biến measurement thành intervention

Huỳnh quang-Activated Cell Sorting vừa đo vừa tách cell. Ta có thể isolate rare immune subset hoặc reporter-positive cell rồi culture/sequence tiếp.

Điều này tạo experimental loop:

```text
measure phenotype
→ select subpopulation
→ perturb / culture
→ measure again
```

Measurement không chỉ quan sát; nó có thể trở thành bước design cho experiment tiếp theo.

## 20. Giải trình tự: base call là inference từ physical signal

Sequencer không nhìn thấy chữ A/C/G/T. Nó đo optical hoặc electrical event rồi algorithm gọi base.

Sanger sequencing suy sequence từ chain termination. Short-read high-throughput platform đọc hàng triệu cluster song song. Long-read platform đọc molecule dài hơn nhưng có error profile và throughput trade-off khác.

Mỗi platform có sai lệch. Chọn platform là chọn loại uncertainty phù hợp biological question.

## 21. FASTQ và Phred score

FASTQ lưu sequence + chất lượng (quality). Phred score:

\[
Q=-10\log_{10}P(error)
\]

Q30 tương ứng estimated base xác suất lỗi (error probability) khoảng \(10^{-3}\), tức 0.1%.

Log scale giúp biểu diễn probability nhỏ. Nhưng điểm chất lượng (quality score) vẫn là model estimate, không phải bảo đảm tuyệt đối.

## 22. Quan hệ liều–đáp ứng (dose–response): effect thường nonlinear

Drug hoặc hormone response thường không tăng tuyến tính vô hạn theo liều (dose). Thụ thể (receptor) saturation và downstream feedback tạo sigmoid-like curve.

Hill-type model:

\[
Đáp ứng (response) = \frac{E_{max}[L]^n}{EC_{50}^n+[L]^n}
\]

\(EC_{50}\) là concentration tạo khoảng half-maximal effect trong mô hình (model); \(n\) mô tả steepness/cooperativity-like behavior.

Đây là cầu nối (bridge) giữa pharmacology, thụ thể biology và quantitative modeling.

## 23. Diễn tiến theo thời gian (time course) quan trọng không kém endpoint

Hai treatment có thể cho cùng endpoint ở 24 giờ nhưng dynamics khác: một response tăng nhanh rồi giảm, một response tăng từ từ.

Time-series giúp phân biệt adaptation, delay và phản hồi (feedback). Snapshot có thể bỏ lỡ cơ chế (mechanism).

Trong signaling và điều hòa gen (gene regulation), **when** thường quan trọng ngang **how much**.

## 24. Loss-of-chức năng (function), gain-of-function và rescue

Knockout cho biết component có cần thiết không. Overexpression hỏi tăng component có đủ tạo phenotype không. Nhưng cả hai có limitation vì adaptation hoặc nonphysiological level.

**Thí nghiệm phục hồi (rescue experiment)** rất mạnh: perturb gene gây phenotype, sau đó restore functional version và phenotype hồi phục. Logic này giảm cách giải thích thay thế rằng effect đến từ off-target hoặc unrelated stress.

Cơ chế nhân quả (causal mechanism) mạnh thường cần necessity + sufficiency + rescue, dù không phải lúc nào cũng thực hiện được đủ ba.

## 25. Hiệu ứng lô (batch effect): technical structure có thể giả biological pattern

Omics sample xử lý ở ngày khác, reagent lot khác hoặc operator khác có thể tạo systematic shift.

Nếu control toàn ở batch A và treatment toàn ở batch B, condition và batch confounded; statistic khó disentangle.

Design tốt phải balance sample giữa batch ngay từ đầu. Computational correction hữu ích nhưng không thay thế được design.

## 26. Statistical significance, effect size và độ bất định (uncertainty)

p-value nhỏ không nói effect lớn. Với sample rất lớn, tiny difference có thể significant.

Interpretation tốt cần effect size, confidence interval, biological relevance và tính bền vững (robustness) across replicate.

Science không hỏi chỉ “có difference không?” mà còn “difference bao nhiêu, uncertainty thế nào, có lần lặp (replicate) được không, và mechanism có hợp lý không?”.

## 27. Kiểm định nhiều lần (multiple testing): omics tạo dương tính giả nếu dùng threshold ngây thơ

Nếu test hàng chục nghìn gene, một số p-value nhỏ xuất hiện chỉ do chance. Multiple-testing correction như FDR giúp kiểm soát false discovery trong framework nhất định.

Điều này minh họa rằng data volume lớn không tự động làm inference tốt hơn; nó tạo problem statistical mới.

## 28. Tương quan (correlation), intervention và causal graph

Tương quan cho biết hai variable covary. Quan hệ nhân quả (causation) đòi hỏi direction và alternative pathway được xem xét.

Perturbation giúp mạnh hơn, nhưng vẫn cần control. Knockout A làm B giảm có thể vì A trực tiếp regulate B, hoặc vì A làm cell sick và mọi transcription giảm.

Suy luận nhân quả (causal reasoning) tốt hỏi intermediate mechanism và dùng multiple evidence layer.

## 29. Reproducibility và nguồn gốc dữ liệu (provenance)

Modern experiment không chỉ cần protocol. Ta cần metadata: sample source, batch, thiết bị đo, reagent version, tiền xử lý tham số (parameter), code version và reference database.

**Data provenance** là khả năng trace figure cuối ngược về dữ liệu thô (raw data).

Trong computational biology, container, workflow manager và version control là một phần của scientific rigor, không chỉ software convenience.

## 30. Tình huống phân tích (case study): “gene X tăng sau điều trị” cần bao nhiêu lớp suy luận?

Giả sử RNA-seq thấy gene X tăng. Điều đó trước hết nghĩa read assigned cho transcript X tăng sau normalization. Ta còn phải hỏi sample balance, batch, mapping ambiguity, kiểm định nhiều lần và effect size.

Nếu muốn nói treatment activate gene X, cần thêm evidence về transcription regulation. Nếu muốn nói X gây phenotype, cần perturbation X và functional readout.

Một statement tưởng đơn giản có thể cần nhiều tầng evidence. Đây chính là cách scientific reasoning tránh overclaim.

## 31. Các hiểu lầm phổ biến (common misconceptions)

“Máy trả số nên số khách quan tuyệt đối” là sai; hiệu chuẩn, threshold và thuật toán (algorithm) ảnh hưởng output.

“p < 0.05 chứng minh hypothesis đúng” là sai; statistic không cứu confounding hoặc bad design.

“Giải trình tự đọc genome thật 100%” là sai; read và variant là inference có error model.

“Thêm replicate technical làm study có nhiều biological sample hơn” cũng sai.

## 32. Mô hình tư duy tổng hợp

Mọi experiment có thể đọc theo dòng chảy (flow):

```text
biological question
→ operational variable
→ sampling + control
→ measurement mechanism
→ calibration + QC
→ data representation
→ statistical inference
→ causal interpretation
→ replication / validation
```

Nếu một step yếu, downstream sophistication không hoàn toàn cứu được.

<!-- depth-audit-2026:measurement-model -->
## Measurement model: observed signal không phải biological truth

Một mô hình tối giản là:

\[
Y_{obs}=Y_{true}+bias+noise
\]

Noise làm measurement dao động ngẫu nhiên; bias đẩy estimate theo một hướng có hệ thống. Lặp kỹ thuật giúp estimate noise nhưng không sửa calibration bias. Tăng sample size giảm standard error của random variation nhưng không cứu thiết kế bị confounding.

Mỗi assay còn có dynamic range, limit of detection và saturation. Signal dưới detection limit không đồng nghĩa “zero”; signal ở saturation không còn phân biệt amount cao hơn. Vì vậy raw number chỉ có nghĩa sau khi hiểu transfer function của instrument và sample preparation.

Causal experiment nên được vẽ như graph: treatment → mediator → outcome, cùng các confounder có thể ảnh hưởng treatment/outcome. Randomization phá association hệ thống với nhiều confounder; blinding giảm measurement/decision bias; rescue experiment kiểm tra mechanism bằng cách khôi phục node dự đoán. Statistics nằm sau causal design, không thay causal design.

## 33. Bridge sang Bioinformatics

Giải trình tự hiện đại (modern sequencing), imaging và single-tế bào assay tạo millions đến billions measurement. Từ đây problem chuyển từ **“làm sao đo?”** sang **“làm sao lưu, kiểm tra, align, count, model và diễn giải lượng data đó mà không đánh mất uncertainty?”**

Bioinformatics chính là continuation của experimental measurement khi biological data vượt khả năng xử lý thủ công.

Xem tiếp [Bioinformatics, thuật toán và Omics Workflow](02_bioinformatics_algorithms_and_omics_workflows.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Công nghệ sinh học, Tin sinh học và Systems Biology](00_biotechnology_bioinformatics_and_systems_biology.md) · [Mục lục Biology](../README.md) · [Bioinformatics, thuật toán và Omics Workflow →](02_bioinformatics_algorithms_and_omics_workflows.md)
