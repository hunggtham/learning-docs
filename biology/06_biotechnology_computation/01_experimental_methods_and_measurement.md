# Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Từ biological concept đến biến thao tác (operational variable)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Độ hợp lệ của cấu trúc đo lường (construct validity): đo đúng thứ mình nghĩ đang đo chưa?** để đối chiếu nhận định với dữ liệu và nguồn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Cho đến đây, ta chủ yếu hỏi **sự sống hoạt động như thế nào**. Nhưng science còn một câu hỏi nền tảng khác: **làm sao ta biết điều đó?** Mọi khẳng định sinh học (biological claim) cuối cùng phải nối với observation, đo lường (measurement / 측정) hoặc experiment. Nếu không hiểu quy trình đo lường (measurement process), ta rất dễ nhầm sản phẩm tạo ra (artifact / 산출물) với biology, correlation với causation, hoặc tín hiệu (signal / 신호) máy đo với đại lượng sinh học (biological quantity) thực.

Chapter này không phải manual giao thức (protocol / 프로토콜). Mục tiêu là xây mô hình tư duy (mental model / 사고 모델) từ câu hỏi → thiết kế → đo → dữ liệu → suy luận (inference / 추론). Hiển vi (microscopy), PCR, western blot, đo tế bào dòng chảy (flow cytometry) và sequencing chỉ là những hiện thực (implementation / 구현) khác nhau của cùng một lô-gic (logic / 논리).

> **Mô hình tư duy:** experiment là một chuỗi xử lý (pipeline / 파이프라인) biến reality thành dữ liệu (data / 데이터). Mỗi bước — lấy mẫu (sampling), chuẩn bị (preparation), thiết bị đo (instrument), tiền xử lý (preprocessing), thống kê (statistic) — đều có thể làm mất thông tin (information / 정보) hoặc tạo sai lệch (bias). Vì vậy interpretation đúng cần hiểu cả biology lẫn hệ thống đo lường (measurement system).

## 1. Từ biological concept đến biến thao tác (operational variable)

Một câu hỏi như “gene X làm cell tăng trưởng nhanh hơn không?” vẫn quá mơ hồ để kiểm thử (test / 테스트). Ta phải chuyển concept thành **biến thao tác**.

“Gene X activity” có thể được thao tác bằng knockout, knockdown, CRISPRi, overexpression hoặc pharmacological inhibition. “Sinh trưởng (growth)” có thể đo bằng cell count, biomass, DNA synthesis, confluence, ATP tín hiệu (signal / 신호) hoặc proliferation marker.

Nhưng mỗi proxy đo một aspect khác nhau. Cell count tăng có thể do division nhanh hơn hoặc chết tế bào (cell death) ít hơn. ATP tín hiệu (signal / 신호) tăng có thể do metabolism tăng mà cell number không đổi.

Do đó câu hỏi experimental đầu tiên luôn là: **đo lường (measurement / 측정) này đại diện cho đại lượng sinh học nào, và những tiến trình (process / 프로세스) khác nào cũng có thể thay đo lường (measurement / 측정) đó?**

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **1. Từ biological concept đến biến thao tác (operational variable)** nêu điều cần giải thích; **2. Độ hợp lệ của cấu trúc đo lường (construct validity): đo đúng thứ mình nghĩ đang đo chưa?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. điều khiển (control / 제어) là lô-gic (logic / 논리) của nhân quả (causal / 인과적) suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Độ hợp lệ của cấu trúc đo lường (construct validity): đo đúng thứ mình nghĩ đang đo chưa?

Một assay có thể technically chính xác nhưng conceptually sai. Đây là vấn đề **độ hợp lệ của cấu trúc đo lường**.

Ví dụ dùng một marker protein (protein) để gọi “tế bào gốc (stem cell)” giả định marker đó đại diện đầy đủ cho stemness. Nhưng stemness là functional trạng thái (state / 상태) gồm self-renewal, differentiation potential và niche dependence. Một marker đơn lẻ có thể không capture hết.

Khi đọc paper, hãy tách hai câu: “instrument có đo chính xác fluorescence không?” và “huỳnh quang (fluorescence) đó có thật sự đại diện cho biological concept không?”.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **2. Độ hợp lệ của cấu trúc đo lường (construct validity): đo đúng thứ mình nghĩ đang đo chưa?** nêu điều cần giải thích; **3. điều khiển (control / 제어) là lô-gic (logic / 논리) của nhân quả (causal / 인과적) suy luận (inference / 추론)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Ngẫu nhiên hóa (randomization), blinding và yếu tố gây nhiễu (confounder)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. điều khiển (control / 제어) là lô-gic (logic / 논리) của nhân quả (causal / 인과적) suy luận (inference / 추론)

**Đối chứng âm (negative control)** cho biết tín hiệu (signal / 신호) có xuất hiện khi thành phần nhân quả (causal component) bị bỏ không. **Đối chứng dương (positive control)** cho biết hệ thống (system / 시스템) có khả năng tạo tín hiệu mong đợi (expected signal). **Đối chứng dung môi (vehicle control)** tách tác động (effect / 효과) của solvent khỏi compound. **Đối chứng không khuôn (no-template control)** trong PCR giúp phát hiện contamination.

Điều khiển (control / 제어) không phải thủ tục phụ. Nó tạo comparison cần thiết để phân biệt cách giải thích thay thế (alternative explanation).

Nếu nhóm can thiệp (treatment group) tăng fluorescence nhưng đối chứng dung môi cũng tăng tương tự, diễn giải (interpretation) “drug có tác động (effect / 효과)” yếu đi mạnh. điều khiển (control / 제어) chính là cách experiment tạo tình huống phản thực (counterfactual) gần đúng: điều gì sẽ xảy ra nếu chỉ thiếu factor mà ta quan tâm?

> **Chuyển mạch:** Controls establish the causal comparison; randomization/blinding reduce confounding, while technical and biological replicates answer precision versus generalizability.

## 4. Ngẫu nhiên hóa (randomization), blinding và yếu tố gây nhiễu (confounder)

Một **yếu tố gây nhiễu (biến gây nhiễu / 교란 변수)** ảnh hưởng cả điều kiện (condition / 조건) và kết quả (outcome / 결과), làm ta nhầm association với causation.

Nếu toàn mẫu đối chứng (control sample) chạy sáng nay còn mẫu can thiệp (treatment sample) chạy ngày mai, độ trôi của máy (machine drift) hoặc lô thuốc thử (reagent batch) có thể bị nhầm thành hiệu ứng can thiệp (treatment effect). Ngẫu nhiên hóa giúp phân bố yếu tố gây nhiễu chưa biết (unknown confounder) giữa group. Làm mù (blinding) giảm độ lệch (bias / 편향) khi scoring có yếu tố subjective.

Good thiết kế thí nghiệm (experiment design) phải nghĩ trước về sai lệch, không đợi statistic “sửa” sau.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **5. Lần lặp kỹ thuật (technical replicate) và lần lặp sinh học (biological replicate) trả lời hai câu khác nhau** tiếp nhận điểm tựa từ **4. Ngẫu nhiên hóa (randomization), blinding và yếu tố gây nhiễu (confounder)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Độ chính xác (accuracy), độ chụm, độ nhạy (sensitivity), specificity và độ phân giải (resolution)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Lần lặp kỹ thuật (technical replicate) và lần lặp sinh học (biological replicate) trả lời hai câu khác nhau

**Lần lặp kỹ thuật** lặp đo lường (measurement / 측정) trên cùng vật liệu sinh học (biological material), giúp estimate nhiễu đo lường (measurement noise). **Lần lặp sinh học** dùng mẫu (sample / 표본) independent, giúp estimate biến thiên sinh học (biological variability).

Đo cùng mẫu (sample / 표본) 20 lần không tạo n=20 lần lặp sinh học. Nó chỉ cho ta biết instrument/quá trình (process) độ chụm (precision).

Đây là một lỗi rất phổ biến: pseudoreplication làm độ tin cậy thống kê (statistical confidence) bị phóng đại vì observation không independent.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **6. Độ chính xác (accuracy), độ chụm, độ nhạy (sensitivity), specificity và độ phân giải (resolution)** tiếp nhận điểm tựa từ **5. Lần lặp kỹ thuật (technical replicate) và lần lặp sinh học (biological replicate) trả lời hai câu khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Hiệu chuẩn (calibration): tín hiệu (signal / 신호) máy đo phải map sang quantity sinh học** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Độ chính xác (accuracy), độ chụm, độ nhạy (sensitivity), specificity và độ phân giải (resolution)

**Độ chính xác (정확도)** là gần giá trị thực (true value) đến đâu. **Độ chụm (정밀도)** là phép đo lặp lại (repeated measurement) gần nhau đến đâu. Một máy có thể precision cao nhưng sai calibration nên accuracy thấp.

**Độ nhạy** hỏi assay detect positive trường hợp (case / 사례) tốt đến đâu; **độ đặc hiệu (specificity)** hỏi tránh dương tính giả (false positive) tốt đến đâu. **Độ phân giải** hỏi phân biệt hai trạng thái (state / 상태) gần nhau được không.

Trong hiển vi, magnification không đồng nghĩa resolution. Trong giải trình tự (sequencing), high độ sâu (depth / 깊이) không tự bảo đảm accuracy nếu sai số hệ thống (systematic error) tồn tại. Các chỉ số (metric / 지표) phải được hiểu theo cơ chế đo lường (measurement mechanism).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **7. Hiệu chuẩn (calibration): tín hiệu (signal / 신호) máy đo phải map sang quantity sinh học** tiếp nhận điểm tựa từ **6. Độ chính xác (accuracy), độ chụm, độ nhạy (sensitivity), specificity và độ phân giải (resolution)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Tín hiệu trên nhiễu (signal-to-noise) và giới hạn phát hiện (detection limit)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Hiệu chuẩn (calibration): tín hiệu (signal / 신호) máy đo phải map sang quantity sinh học

Instrument thường cho tín hiệu (signal / 신호) đơn vị (unit / 단위), không trực tiếp cho concentration. Calibration dùng tiêu chuẩn (standard / 표준) có known quantity để tạo ánh xạ (mapping / 매핑).

Nếu detector phản hồi (response / 응답) tuyến tính (linear / 선형) trong một phạm vi (range / 범위):

\[
tín hiệu (signal / 신호) = a\times Concentration + b
\]

Nhưng ngoài dải động (dynamic range), detector có thể saturate. Lúc đó tín hiệu (signal / 신호) không tăng tương ứng quantity nữa.

Vì vậy “band đậm gấp đôi” không tự động nghĩa protein gấp đôi nếu exposure saturated.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **7. Hiệu chuẩn (calibration): tín hiệu (signal / 신호) máy đo phải map sang quantity sinh học** đã nêu tiêu chí phân biệt, còn **8. Tín hiệu trên nhiễu (signal-to-noise) và giới hạn phát hiện (detection limit)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **9. Hiển vi: ảnh (image / 이미지) là phép đo (measurement) đã qua optics và processing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Tín hiệu trên nhiễu (signal-to-noise) và giới hạn phát hiện (detection limit)

Đo lường (measurement / 측정) luôn gồm tín hiệu (signal / 신호) + nhiễu (noise). Noise có thể đến từ photon counting, background fluorescence, nonspecific binding, mẫu (sample / 표본) heterogeneity hoặc instrument biến dị (variation).

**Tỉ lệ tín hiệu trên nhiễu (signal-to-noise ratio), SNR** cao giúp detect difference. Nhưng tăng tín hiệu (signal / 신호) bằng amplification cũng có thể amplify độ lệch (bias / 편향).

Giới hạn phát hiện không phải “zero biology dưới threshold”. Nó chỉ nghĩa assay không phân biệt tín hiệu (signal / 신호) khỏi noise đủ tin cậy ở mức đó.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **8. Tín hiệu trên nhiễu (signal-to-noise) và giới hạn phát hiện (detection limit)** đã nêu tiêu chí phân biệt, còn **9. Hiển vi: ảnh (image / 이미지) là phép đo (measurement) đã qua optics và processing** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **10. Diffraction limit và super-độ phân giải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Hiển vi: ảnh (image / 이미지) là phép đo (measurement) đã qua optics và processing

Light microscopy tạo ảnh (image / 이미지) từ tương tác (interaction / 상호작용) giữa light và mẫu (sample / 표본). Huỳnh quang microscopy dùng fluorophore để gắn tín hiệu (signal / 신호) vào cấu trúc (structure / 구조)/molecule cụ thể.

Label giúp specificity nhưng có thể perturb hệ thống (system / 시스템). Overexpress fluorescent fusion protein có thể làm concentration phi sinh lý. Fixation giữ morphology nhưng giết cell và tạo nhiễu giả (artifact). Chụp ảnh tế bào sống (live-cell imaging) giữ dynamics nhưng gặp phototoxicity và photobleaching.

Do đó ảnh (image / 이미지) không phải “nhìn trực tiếp reality”. Nó là đầu ra (output / 출력) của chuẩn bị mẫu (sample preparation) + optics + detector + reconstruction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **9. Hiển vi: ảnh (image / 이미지) là phép đo (measurement) đã qua optics và processing** đã nêu tiêu chí phân biệt, còn **10. Diffraction limit và super-độ phân giải** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. Electron microscopy: đổi live dynamics lấy ultrastructure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Diffraction limit và super-độ phân giải

Với conventional light microscopy, resolution gần bị giới hạn bởi diffraction. Abbe approximation:

\[
d\approx\frac{\lambda}{2NA}
\]

Muốn resolution tốt hơn có thể dùng wavelength ngắn hơn hoặc numerical aperture lớn hơn. Super-resolution technique dùng optical/statistical chiến lược (strategy / 전략) để vượt conventional limit trong điều kiện (condition / 조건) nhất định.

Quan trọng là “zoom” không tự tạo thông tin (information / 정보). Nếu hệ thống (system / 시스템) không resolve được hai đối tượng (object / 객체), phóng to chỉ làm blur lớn hơn.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **10. Diffraction limit và super-độ phân giải** đã nêu tiêu chí phân biệt, còn **11. Electron microscopy: đổi live dynamics lấy ultrastructure** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Fractionation và centrifugation: tách hệ thống (system / 시스템) để suy hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Electron microscopy: đổi live dynamics lấy ultrastructure

Electron có wavelength hiệu dụng rất ngắn nên EM đạt resolution cao. TEM cho ultrastructure bên trong mẫu (sample / 표본) mỏng; SEM mô tả surface morphology.

Nhưng preparation phức tạp và thường không quan sát quá trình sống (live process). Đây là sự đánh đổi (trade-off / 트레이드오프) đo lường (measurement / 측정): chi tiết không gian (spatial detail) cao hơn đổi lấy tính sát sinh lý (physiological realism) thấp hơn.

Không có thiết bị đo “tốt nhất”; chỉ có instrument phù hợp câu hỏi.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **12. Fractionation và centrifugation: tách hệ thống (system / 시스템) để suy hàm (function / 함수)** tiếp nhận điểm tựa từ **11. Electron microscopy: đổi live dynamics lấy ultrastructure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Electrophoresis: phân tách vật lý (physical separation) thành biological bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Fractionation và centrifugation: tách hệ thống (system / 시스템) để suy hàm (function / 함수)

Differential centrifugation tách thành phần (component / 컴포넌트) theo kích thước (size / 크기)/density/sedimentation. Density độ dốc (gradient / 기울기) tách tinh hơn.

Lịch sử sinh học tế bào (cell biology) cho thấy nhiều organelle hàm (function / 함수) được khám phá bằng cách fractionate cell rồi assay activity từng fraction. Đây là chiến lược (strategy / 전략) reductionist có ích: tách hệ thống (system / 시스템) thành thành phần (component / 컴포넌트) để hỏi hàm (function / 함수), sau đó phải quay lại tích hợp (integration / 통합) để hiểu whole cell.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **12. Fractionation và centrifugation: tách hệ thống (system / 시스템) để suy hàm (function / 함수)** nêu điều cần giải thích; **13. Electrophoresis: phân tách vật lý (physical separation) thành biological bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. PCR: amplification và nguy cơ hiểu nhầm tăng trưởng theo hàm mũ (exponential growth)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Electrophoresis: phân tách vật lý (physical separation) thành biological bằng chứng (evidence / 증거)

DNA mang charge âm nhờ phosphate backbone nên migrate trong điện trường (electric field). Gel ma trận (matrix / 행렬) làm fragment nhỏ đi dễ hơn fragment lớn.

SDS-PAGE làm protein có charge-to-mass tương đối đồng đều, giúp separation chủ yếu theo kích thước (size / 크기).

Band position là chỉ dấu thay thế (proxy) cho kích thước (size / 크기); band intensity gần quantity chỉ trong dải động phù hợp (proper dynamic range). Một band không phải “molecule thật” mà là quần thể (population) phân tử (molecule) được transform thành spatial tín hiệu (signal / 신호).

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **13. Electrophoresis: phân tách vật lý (physical separation) thành biological bằng chứng (evidence / 증거)** đã nêu tiêu chí phân biệt, còn **14. PCR: amplification và nguy cơ hiểu nhầm tăng trưởng theo hàm mũ (exponential growth)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **15. Reverse transcription: mRNA không đồng nghĩa protein** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. PCR: amplification và nguy cơ hiểu nhầm tăng trưởng theo hàm mũ (exponential growth)

PCR dùng denaturation → primer annealing → extension lặp nhiều cycle. Idealized:

\[
N_n=N_0 2^n
\]

Nhưng real efficiency thấp hơn 100% và giảm khi reagent cạn hoặc sản phẩm (product / 제품) cạnh tranh. PCR điểm cuối (endpoint PCR) vì vậy không quantitative tuyến tính tốt.

qPCR theo dõi tín hiệu (signal / 신호) trong exponential phase. Ct/Cq thấp thường tương ứng starting template nhiều hơn, nhưng comparison cần hiệu suất khuếch đại (amplification efficiency) và normalization hợp lý.

Amplification mạnh làm technique sensitive nhưng cũng làm contamination nhỏ trở thành tín hiệu (signal / 신호) lớn.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **14. PCR: amplification và nguy cơ hiểu nhầm tăng trưởng theo hàm mũ (exponential growth)** đã nêu tiêu chí phân biệt, còn **15. Reverse transcription: mRNA không đồng nghĩa protein** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **16. Western blot và kháng thể (antibody) độ đặc hiệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Reverse transcription: mRNA không đồng nghĩa protein

RT-qPCR chuyển RNA thành cDNA rồi amplify. Nó estimate mức độ phong phú của bản phiên mã (transcript abundance).

Nhưng biểu hiện gen (gene expression) có nhiều tầng (layer / 계층):

```text
DNA
→ transcription
→ RNA stability
→ translation
→ protein modification
→ protein degradation
→ function
```

mRNA tăng không bảo đảm protein tăng tương ứng. Phép đo ở một tầng (layer / 계층) không tự động suy ra tầng (layer / 계층) sau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **16. Western blot và kháng thể (antibody) độ đặc hiệu** tiếp nhận điểm tựa từ **15. Reverse transcription: mRNA không đồng nghĩa protein** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. ELISA và đường chuẩn (standard curve)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Western blot và kháng thể (antibody) độ đặc hiệu

Western blot separation protein rồi dùng antibody detect mục tiêu (target / 대상). Interpretation phụ thuộc antibody độ đặc hiệu, loading điều khiển (control / 제어), transfer efficiency và exposure phạm vi (range / 범위).

Một antibody cross-react protein khác có thể tạo band giả. Loading điều khiển (control / 제어) cũng có thể thay theo điều trị (treatment).

Strong conclusion thường cần orthogonal kiểm tra hợp lệ (validation / 검증), ví dụ western + mass spectrometry + functional assay thay vì chỉ một band đẹp.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **17. ELISA và đường chuẩn (standard curve)** tiếp nhận điểm tựa từ **16. Western blot và kháng thể (antibody) độ đặc hiệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Đo tế bào dòng chảy: average có thể che phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. ELISA và đường chuẩn (standard curve)

ELISA dùng antibody–antigen tương tác (interaction / 상호작용) và enzym (enzyme)-generated tín hiệu (signal / 신호). Đường chuẩn map tín hiệu (signal / 신호) sang concentration.

Curve thường nonlinear ở concentration extreme; mẫu (sample / 표본) phải nằm trong calibrated phạm vi (range / 범위). Dilution series giúp kiểm tra tín hiệu (signal / 신호) có behave hợp lý không.

Điều này là general lesson: **phép đo (measurement) mô hình (model / 모델) phải được validated trong phạm vi (range / 범위) ta dùng**.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **18. Đo tế bào dòng chảy: average có thể che phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **17. ELISA và đường chuẩn (standard curve)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. FACS biến đo lường (measurement / 측정) thành intervention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Đo tế bào dòng chảy: average có thể che phân phối (distribution / 분포)

Luồng (flow / 흐름) cytometer đo thuộc tính (property / 속성) từng cell. Điều này rất mạnh vì hai mẫu (sample / 표본) có cùng mean fluorescence có thể có phân phối (distribution / 분포) khác hoàn toàn.

Gating xác định population nào được phân tích. Compensation xử lý spectral overlap. Doublet exclusion tránh hai cell dính nhau bị đọc như một sự kiện (event / 이벤트).

Single-tế bào (cell) đo lường (measurement / 측정) vì vậy giàu thông tin (information / 정보) hơn bulk average, nhưng phân tích (analysis / 분석) choice cũng ảnh hưởng kết quả (result / 결과) nhiều hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **18. Đo tế bào dòng chảy: average có thể che phân phối (distribution / 분포)** nêu điều cần giải thích; **19. FACS biến đo lường (measurement / 측정) thành intervention** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Giải trình tự: cơ sở (base / 기반) lời gọi (call / 호출) là suy luận (inference / 추론) từ vật lý (physical / 물리적) tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. FACS biến đo lường (measurement / 측정) thành intervention

Huỳnh quang-Activated Cell Sorting vừa đo vừa tách cell. Ta có thể isolate rare immune subset hoặc reporter-positive cell rồi culture/chuỗi (sequence / 시퀀스) tiếp.

Điều này tạo experimental vòng lặp (loop / 루프):

```text
measure phenotype
→ select subpopulation
→ perturb / culture
→ measure again
```

Đo lường (measurement / 측정) không chỉ quan sát; nó có thể trở thành bước thiết kế (design / 설계) cho experiment tiếp theo.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **19. FACS biến đo lường (measurement / 측정) thành intervention** nêu điều cần giải thích; **20. Giải trình tự: cơ sở (base / 기반) lời gọi (call / 호출) là suy luận (inference / 추론) từ vật lý (physical / 물리적) tín hiệu (signal / 신호)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. FASTQ và Phred score** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Giải trình tự: cơ sở (base / 기반) lời gọi (call / 호출) là suy luận (inference / 추론) từ vật lý (physical / 물리적) tín hiệu (signal / 신호)

Sequencer không nhìn thấy chữ A/C/G/T. Nó đo optical hoặc electrical sự kiện (event / 이벤트) rồi thuật toán (algorithm / 알고리즘) gọi cơ sở (base / 기반).

Sanger sequencing suy chuỗi (sequence / 시퀀스) từ chuỗi (chain / 사슬) termination. Short-read high-throughput nền tảng (platform / 플랫폼) đọc hàng triệu cluster song song. Long-read nền tảng (platform / 플랫폼) đọc molecule dài hơn nhưng có lỗi (error / 오류) profile và thông lượng (throughput / 처리량) sự đánh đổi (trade-off / 트레이드오프) khác.

Mỗi nền tảng (platform / 플랫폼) có sai lệch. Chọn nền tảng (platform / 플랫폼) là chọn loại bất định (uncertainty / 불확실성) phù hợp biological question.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **21. FASTQ và Phred score** tiếp nhận điểm tựa từ **20. Giải trình tự: cơ sở (base / 기반) lời gọi (call / 호출) là suy luận (inference / 추론) từ vật lý (physical / 물리적) tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Quan hệ liều–đáp ứng (dose–response): tác động (effect / 효과) thường nonlinear** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. FASTQ và Phred score

FASTQ lưu chuỗi (sequence / 시퀀스) + chất lượng (quality / 품질). Phred score:

\[
Q=-10\log_{10}P(error)
\]

Q30 tương ứng estimated cơ sở (base / 기반) xác suất lỗi (error probability) khoảng \(10^{-3}\), tức 0.1%.

Log quy mô (scale / 규모) giúp biểu diễn xác suất (probability / 확률) nhỏ. Nhưng điểm chất lượng (quality score) vẫn là mô hình (model / 모델) estimate, không phải bảo đảm tuyệt đối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **22. Quan hệ liều–đáp ứng (dose–response): tác động (effect / 효과) thường nonlinear** tiếp nhận điểm tựa từ **21. FASTQ và Phred score** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Diễn tiến theo thời gian (time course) quan trọng không kém endpoint** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Quan hệ liều–đáp ứng (dose–response): tác động (effect / 효과) thường nonlinear

Drug hoặc hormone phản hồi (response / 응답) thường không tăng tuyến tính vô hạn theo liều (dose). Thụ thể (receptor) saturation và downstream phản hồi (feedback / 피드백) tạo sigmoid-like curve.

Hill-type mô hình (model / 모델):

\[
Đáp ứng (response) = \frac{E_{max}[L]^n}{EC_{50}^n+[L]^n}
\]

\(EC_{50}\) là concentration tạo khoảng half-maximal tác động (effect / 효과) trong mô hình (model / 모델); \(n\) mô tả steepness/cooperativity-like hành vi (behavior / 동작).

Đây là cầu nối (bridge / 브리지) giữa pharmacology, thụ thể biology và quantitative modeling.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **23. Diễn tiến theo thời gian (time course) quan trọng không kém endpoint** tiếp nhận điểm tựa từ **22. Quan hệ liều–đáp ứng (dose–response): tác động (effect / 효과) thường nonlinear** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Loss-of-chức năng (function), gain-of-function và rescue** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Diễn tiến theo thời gian (time course) quan trọng không kém endpoint

Hai treatment có thể cho cùng endpoint ở 24 giờ nhưng dynamics khác: một phản hồi (response / 응답) tăng nhanh rồi giảm, một phản hồi (response / 응답) tăng từ từ.

Time-series giúp phân biệt adaptation, delay và phản hồi (feedback / 피드백). Snapshot có thể bỏ lỡ cơ chế (mechanism / 메커니즘).

Trong signaling và điều hòa gen (gene regulation), **when** thường quan trọng ngang **how much**.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **24. Loss-of-chức năng (function), gain-of-function và rescue** tiếp nhận điểm tựa từ **23. Diễn tiến theo thời gian (time course) quan trọng không kém endpoint** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Hiệu ứng lô (batch effect): technical cấu trúc (structure / 구조) có thể giả biological mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Loss-of-chức năng (function), gain-of-function và rescue

Knockout cho biết thành phần (component / 컴포넌트) có cần thiết không. Overexpression hỏi tăng thành phần (component / 컴포넌트) có đủ tạo phenotype không. Nhưng cả hai có limitation vì adaptation hoặc nonphysiological mức (level / 수준).

**Thí nghiệm phục hồi (rescue experiment)** rất mạnh: perturb gene gây phenotype, sau đó restore functional phiên bản (version / 버전) và phenotype hồi phục. lô-gic (logic / 논리) này giảm cách giải thích thay thế rằng tác động (effect / 효과) đến từ off-target hoặc unrelated stress.

Cơ chế nhân quả (causal mechanism) mạnh thường cần necessity + sufficiency + rescue, dù không phải lúc nào cũng thực hiện được đủ ba.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **25. Hiệu ứng lô (batch effect): technical cấu trúc (structure / 구조) có thể giả biological mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **24. Loss-of-chức năng (function), gain-of-function và rescue** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Statistical significance, tác động (effect / 효과) kích thước (size / 크기) và độ bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Hiệu ứng lô (batch effect): technical cấu trúc (structure / 구조) có thể giả biological mẫu (pattern / 패턴)

Omics mẫu (sample / 표본) xử lý ở ngày khác, reagent lot khác hoặc operator khác có thể tạo systematic shift.

Nếu điều khiển (control / 제어) toàn ở batch A và treatment toàn ở batch B, điều kiện (condition / 조건) và batch confounded; statistic khó disentangle.

Thiết kế (design / 설계) tốt phải balance mẫu (sample / 표본) giữa batch ngay từ đầu. Computational correction hữu ích nhưng không thay thế được thiết kế (design / 설계).

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **26. Statistical significance, tác động (effect / 효과) kích thước (size / 크기) và độ bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **25. Hiệu ứng lô (batch effect): technical cấu trúc (structure / 구조) có thể giả biological mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Kiểm định nhiều lần (multiple testing): omics tạo dương tính giả nếu dùng threshold ngây thơ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Statistical significance, tác động (effect / 효과) kích thước (size / 크기) và độ bất định (uncertainty / 불확실성)

p-value nhỏ không nói tác động (effect / 효과) lớn. Với mẫu (sample / 표본) rất lớn, tiny difference có thể significant.

Interpretation tốt cần tác động (effect / 효과) kích thước (size / 크기), confidence interval, biological relevance và tính bền vững (robustness) across replicate.

Science không hỏi chỉ “có difference không?” mà còn “difference bao nhiêu, bất định (uncertainty / 불확실성) thế nào, có lần lặp (replicate) được không, và cơ chế (mechanism / 메커니즘) có hợp lý không?”.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **27. Kiểm định nhiều lần (multiple testing): omics tạo dương tính giả nếu dùng threshold ngây thơ** tiếp nhận điểm tựa từ **26. Statistical significance, tác động (effect / 효과) kích thước (size / 크기) và độ bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Tương quan (correlation), intervention và nhân quả (causal / 인과적) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Kiểm định nhiều lần (multiple testing): omics tạo dương tính giả nếu dùng threshold ngây thơ

Nếu kiểm thử (test / 테스트) hàng chục nghìn gene, một số p-value nhỏ xuất hiện chỉ do chance. Multiple-testing correction như FDR giúp kiểm soát false discovery trong khung phần mềm (framework / 프레임워크) nhất định.

Điều này minh họa rằng dữ liệu (data / 데이터) volume lớn không tự động làm suy luận (inference / 추론) tốt hơn; nó tạo bài toán (problem / 문제) statistical mới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **28. Tương quan (correlation), intervention và nhân quả (causal / 인과적) đồ thị (graph / 그래프)** tiếp nhận điểm tựa từ **27. Kiểm định nhiều lần (multiple testing): omics tạo dương tính giả nếu dùng threshold ngây thơ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Reproducibility và nguồn gốc dữ liệu (provenance)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Tương quan (correlation), intervention và nhân quả (causal / 인과적) đồ thị (graph / 그래프)

Tương quan cho biết hai variable covary. Quan hệ nhân quả (causation) đòi hỏi direction và alternative pathway được xem xét.

Perturbation giúp mạnh hơn, nhưng vẫn cần điều khiển (control / 제어). Knockout A làm B giảm có thể vì A trực tiếp regulate B, hoặc vì A làm cell sick và mọi transcription giảm.

Suy luận nhân quả (causal reasoning) tốt hỏi intermediate cơ chế (mechanism / 메커니즘) và dùng multiple bằng chứng (evidence / 증거) tầng (layer / 계층).

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **28. Tương quan (correlation), intervention và nhân quả (causal / 인과적) đồ thị (graph / 그래프)** nêu điều cần giải thích; **29. Reproducibility và nguồn gốc dữ liệu (provenance)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. Tình huống phân tích (case study): “gene X tăng sau điều trị” cần bao nhiêu lớp suy luận?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Reproducibility và nguồn gốc dữ liệu (provenance)

Hiện đại (modern / 현대적) experiment không chỉ cần giao thức (protocol / 프로토콜). Ta cần siêu dữ liệu (metadata / 메타데이터): mẫu (sample / 표본) nguồn (source / 소스), batch, thiết bị đo, reagent phiên bản (version / 버전), tiền xử lý tham số (parameter), mã (code / 코드) phiên bản (version / 버전) và tham chiếu (reference / 참조) cơ sở dữ liệu (database / 데이터베이스).

**dữ liệu (data / 데이터) provenance** là khả năng dấu vết (trace / 추적) figure cuối ngược về dữ liệu thô (raw data).

Trong computational biology, bộ chứa (container / 컨테이너), workflow manager và phiên bản (version / 버전) điều khiển (control / 제어) là một phần của scientific rigor, không chỉ software convenience.

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **29. Reproducibility và nguồn gốc dữ liệu (provenance)** cho ta quy tắc; **30. Tình huống phân tích (case study): “gene X tăng sau điều trị” cần bao nhiêu lớp suy luận?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **31. Các hiểu lầm phổ biến (common misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Tình huống phân tích (case study): “gene X tăng sau điều trị” cần bao nhiêu lớp suy luận?

Giả sử RNA-seq thấy gene X tăng. Điều đó trước hết nghĩa read assigned cho transcript X tăng sau normalization. Ta còn phải hỏi mẫu (sample / 표본) balance, batch, ánh xạ (mapping / 매핑) ambiguity, kiểm định nhiều lần và tác động (effect / 효과) kích thước (size / 크기).

Nếu muốn nói treatment activate gene X, cần thêm bằng chứng (evidence / 증거) về transcription regulation. Nếu muốn nói X gây phenotype, cần perturbation X và functional readout.

Một statement tưởng đơn giản có thể cần nhiều tầng bằng chứng (evidence / 증거). Đây chính là cách scientific lập luận (reasoning / 추론) tránh overclaim.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **30. Tình huống phân tích (case study): “gene X tăng sau điều trị” cần bao nhiêu lớp suy luận?** cho ta quy tắc; **31. Các hiểu lầm phổ biến (common misconceptions)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **32. Mô hình tư duy tổng hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Các hiểu lầm phổ biến (common misconceptions)

“Máy trả số nên số khách quan tuyệt đối” là sai; hiệu chuẩn, threshold và thuật toán (algorithm / 알고리즘) ảnh hưởng đầu ra (output / 출력).

“p < 0.05 chứng minh hypothesis đúng” là sai; statistic không cứu confounding hoặc bad thiết kế (design / 설계).

“Giải trình tự đọc genome thật 100%” là sai; read và variant là suy luận (inference / 추론) có lỗi (error / 오류) mô hình (model / 모델).

“Thêm replicate technical làm study có nhiều biological mẫu (sample / 표본) hơn” cũng sai.

> **Chuyển mạch:** Trong **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **32. Mô hình tư duy tổng hợp** gom các mảnh từ **31. Các hiểu lầm phổ biến (common misconceptions)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Đo lường (measurement / 측정) mô hình (model / 모델): observed tín hiệu (signal / 신호) không phải biological truth** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **32. Mô hình tư duy tổng hợp** nêu điều cần giải thích; **Đo lường (measurement / 측정) mô hình (model / 모델): observed tín hiệu (signal / 신호) không phải biological truth** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. cầu nối (bridge / 브리지) sang Bioinformatics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đo lường (measurement / 측정) mô hình (model / 모델): observed tín hiệu (signal / 신호) không phải biological truth

Một mô hình tối giản là:

\[
Y_{obs}=Y_{true}+độ lệch (bias / 편향)+noise
\]

Noise làm đo lường (measurement / 측정) dao động ngẫu nhiên; độ lệch (bias / 편향) đẩy estimate theo một hướng có hệ thống. Lặp kỹ thuật giúp estimate noise nhưng không sửa calibration độ lệch (bias / 편향). Tăng cỡ mẫu (sample size / 표본 크기) giảm tiêu chuẩn (standard / 표준) lỗi (error / 오류) của random variation nhưng không cứu thiết kế bị confounding.

Mỗi assay còn có động (dynamic / 동적) phạm vi (range / 범위), limit of detection và saturation. tín hiệu (signal / 신호) dưới detection limit không đồng nghĩa “zero”; tín hiệu (signal / 신호) ở saturation không còn phân biệt amount cao hơn. Vì vậy raw number chỉ có nghĩa sau khi hiểu transfer hàm (function / 함수) của instrument và mẫu (sample / 표본) preparation.

Nhân quả (causal / 인과적) experiment nên được vẽ như đồ thị (graph / 그래프): treatment → mediator → kết quả (outcome / 결과), cùng các confounder có thể ảnh hưởng treatment/kết quả (outcome / 결과). Randomization phá association hệ thống với nhiều confounder; blinding giảm đo lường (measurement / 측정)/quyết định (decision / 결정) độ lệch (bias / 편향); rescue experiment kiểm tra cơ chế (mechanism / 메커니즘) bằng cách khôi phục nút (node / 노드) dự đoán. Statistics nằm sau nhân quả (causal / 인과적) thiết kế (design / 설계), không thay nhân quả (causal / 인과적) thiết kế (design / 설계).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phương pháp thực nghiệm và đo lường trong Sinh học — Experimental Methods and đo lường (measurement / 측정)**, **Đo lường (measurement / 측정) mô hình (model / 모델): observed tín hiệu (signal / 신호) không phải biological truth** nêu điều cần giải thích; **33. cầu nối (bridge / 브리지) sang Bioinformatics** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 33. cầu nối (bridge / 브리지) sang Bioinformatics

Giải trình tự hiện đại (modern sequencing), imaging và single-tế bào assay tạo millions đến billions đo lường (measurement / 측정). Từ đây bài toán (problem / 문제) chuyển từ **“làm sao đo?”** sang **“làm sao lưu, kiểm tra, align, count, mô hình (model / 모델) và diễn giải lượng dữ liệu (data / 데이터) đó mà không đánh mất bất định (uncertainty / 불확실성)?”**

Bioinformatics chính là continuation của experimental đo lường (measurement / 측정) khi biological dữ liệu (data / 데이터) vượt khả năng xử lý thủ công.

Xem tiếp [Bioinformatics, thuật toán và Omics Workflow](02_bioinformatics_algorithms_and_omics_workflows.md).

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Công nghệ sinh học, Tin sinh học và Systems Biology](00_biotechnology_bioinformatics_and_systems_biology.md) · [Mục lục Biology](../README.md) · [Bioinformatics, thuật toán và Omics Workflow →](02_bioinformatics_algorithms_and_omics_workflows.md)

> **Bàn giao:** Sau **33. cầu nối (bridge / 브리지) sang Bioinformatics**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
