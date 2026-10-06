# Truyền tín hiệu và Chu kỳ tế bào — Cell Signaling and Cell Cycle (세포 신호전달과 세포주기)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Truyền tín hiệu và Chu kỳ tế bào — Cell Signaling and Cell Cycle (세포 신호전달과 세포주기)**. Route đi từ signal/receptor → transduction và feedback → gene expression/response → checkpoints, growth và division, để quyết định của tế bào được nối với thông tin, thời gian và rủi ro sai lệch.

Ở chapter trước, tế bào (cell) đã có năng lượng (energy / 에너지) và mạng lưới chuyển hóa (metabolic network). Nhưng một hệ sống không thể chỉ có bộ máy (machinery); nó cần **điều khiển (control / 제어)**. Cell phải biết khi nào chất dinh dưỡng (nutrient) đủ, khi nào DNA bị hỏng, khi nào tế bào lân cận (neighboring cell) gửi tín hiệu (signal / 신호), khi nào cần tăng trưởng, khi nào nên divide và khi nào nên dừng.

Chapter này nghiên cứu **truyền tín hiệu tế bào (cell signaling / 세포 신호전달)** như hệ thống xử lý thông tin và **chu kỳ tế bào (cell cycle / 세포주기)** như một quyết định được kiểm soát chặt. Đây là cầu nối (bridge / 브리지) tự nhiên từ sinh học tế bào (cell biology) sang genetics: signaling có thể đổi protein hoạt động (activity) trong vài giây, nhưng phản hồi (response / 응답) dài hạn thường cần đổi biểu hiện gen (gene expression).

> **mô hình tư duy (mental model / 사고 모델):** signaling là quá trình biến một thay đổi ở bên ngoài hoặc bên trong thành một chuỗi thay đổi molecular có tổ chức. Chu kỳ tế bào (cell cycle) là một máy trạng thái (state machine / 상태 머신) sinh học chỉ chuyển trạng thái (state / 상태) khi các checkpoint cho phép.

## 1. Tại sao cell cần signaling?

Một sinh vật đơn bào (unicellular organism) phải sense nutrient, toxin, temperature và mating tín hiệu (signal / 신호). Trong sinh vật đa bào (multicellular organism), cell còn phải coordinate với tissue.

Nếu liver cell, muscle cell và nơron (neuron) đều tự quyết định độc lập, organism không thể giữ cân bằng nội môi (homeostasis). Hoóc-môn (hormone), neurotransmitter, yếu tố tăng trưởng (growth factor) và cytokine tạo communication tầng (layer / 계층) giúp nhiều cell hoạt động như một hệ thống (system / 시스템).

Tín hiệu (signal / 신호) không chỉ đến từ bên ngoài. Tổn thương DNA (DNA damage), low ATP, protein chưa gấp cuộn đúng (unfolded protein) hay thiếu oxy (low oxygen) cũng kích hoạt truyền tín hiệu nội bào (intracellular signaling).

> **Nối mạch:** Cell signaling solves coordination across distance; signal/receptor/response forms a chain, and receptor transduction converts ligand binding into intracellular language.

## 2. tín hiệu (signal / 신호), receptor và đáp ứng (response)

Một signaling hệ thống (system / 시스템) thường có ba lớp:

```text
signal
  ↓
receptor/sensor
  ↓
signal transduction network
  ↓
cellular response
```

**Ligand (리간드)** là molecule bind receptor. **Thụ thể (receptor) (수용체)** là protein nhận tín hiệu (signal / 신호). **Chuyển đổi tín hiệu (signal transduction) (신호전달)** là chuỗi sự kiện (event / 이벤트) chuyển tín hiệu (signal / 신호) thành phản hồi (response / 응답).

Phản hồi (response / 응답) có thể là mở kênh ion (ion channel), thay metabolism, di chuyển, tiết molecule, đổi biểu hiện gen, divide hoặc apoptosis.

> **Nối mạch:** **3. Receptor không chỉ “nhận” mà còn dịch ngôn ngữ** nối từ **2. tín hiệu (signal / 신호), receptor và đáp ứng (response)** sang **4. Các kiểu communication theo khoảng cách**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Receptor không chỉ “nhận” mà còn dịch ngôn ngữ

Tín hiệu (signal / 신호) ngoài cell thường không đi thẳng vào nucleus. Receptor làm nhiệm vụ transduce: biến một kiểu thông tin (information / 정보) thành kiểu molecular sự kiện (event / 이벤트) khác.

Ví dụ insulin bind insulin receptor ở màng (membrane). Receptor activation kích hoạt chuỗi phosphoryl hóa (phosphorylation cascade), thay transporter localization và metabolic enzyme hoạt động.

Một molecule peptide ngoài cell cuối cùng có thể đổi glucose uptake bên trong mà bản thân insulin không cần đi qua màng.

> **Nối mạch:** **4. Các kiểu communication theo khoảng cách** nối từ **3. Receptor không chỉ “nhận” mà còn dịch ngôn ngữ** sang **5. Màng (membrane) receptor và thụ thể nội bào (intracellular receptor)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Các kiểu communication theo khoảng cách

**Truyền tín hiệu tự tiết (autocrine signaling)**: cell tác động chính nó.

**Truyền tín hiệu cận tiết (paracrine signaling)**: tín hiệu (signal / 신호) tác động cell gần.

**Truyền tín hiệu nội tiết (endocrine signaling)**: hoóc-môn đi xa qua tuần hoàn (circulation).

**Truyền tín hiệu qua synap (synaptic signaling)**: neuron truyền tín hiệu (signal / 신호) nhanh và định hướng qua synapse.

**Truyền tín hiệu phụ thuộc tiếp xúc (contact-dependent signaling)**: receptor và ligand trên hai cell tiếp xúc trực tiếp.

Những kiểu này không phải category để học thuộc; chúng phản ánh bài toán distance, speed và độ đặc hiệu (specificity).

> **Nối mạch:** **5. Màng (membrane) receptor và thụ thể nội bào (intracellular receptor)** nối từ **4. Các kiểu communication theo khoảng cách** sang **6. G protein-coupled receptor: tín hiệu (signal / 신호) nhỏ, mạng (network / 네트워크) lớn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. Màng (membrane) receptor và thụ thể nội bào (intracellular receptor)

Ligand ưa nước (hydrophilic ligand) thường không xuyên membrane dễ nên dùng membrane thụ thể (receptor). Steroid hormone hoặc molecule lipid-soluble có thể đi qua membrane và bind **thụ thể nội bào**.

Thụ thể nội bào thường trực tiếp hoặc gián tiếp điều chỉnh transcription.

Cùng một mục tiêu “đổi cell hành vi (behavior / 동작)”, chemistry của ligand quyết định kiến trúc (architecture / 아키텍처) signaling phù hợp.

> **Nối mạch:** **6. G protein-coupled receptor: tín hiệu (signal / 신호) nhỏ, mạng (network / 네트워크) lớn** nối từ **5. Màng (membrane) receptor và thụ thể nội bào (intracellular receptor)** sang **7. Chất truyền tin thứ hai: đưa tín hiệu (signal / 신호) đi nhanh trong cytoplasm**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. G protein-coupled receptor: tín hiệu (signal / 신호) nhỏ, mạng (network / 네트워크) lớn

**GPCR (G protein-coupled receptor / G단백질 연결 수용체)** là family receptor lớn.

Ligand bind làm receptor đổi conformation, activation heterotrimeric G protein, rồi effector enzym (enzyme)/channel được điều chỉnh. GTP hydrolysis giúp reset hệ thống (system / 시스템).

Một receptor có thể activate nhiều G protein; một enzyme có thể tạo nhiều chất truyền tin thứ hai (second messenger). Đây là **tín hiệu (signal / 신호) khuếch đại (amplification)**.

> **Nối mạch:** **7. Chất truyền tin thứ hai: đưa tín hiệu (signal / 신호) đi nhanh trong cytoplasm** nối từ **6. G protein-coupled receptor: tín hiệu (signal / 신호) nhỏ, mạng (network / 네트워크) lớn** sang **8. Calcium: ion vừa structural vừa tín hiệu (signal / 신호)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Chất truyền tin thứ hai: đưa tín hiệu (signal / 신호) đi nhanh trong cytoplasm

**Chất truyền tin thứ hai (2차 전달자)** là small intracellular molecule/ion như cAMP, Ca²⁺, IP₃.

Một receptor activation có thể tạo rất nhiều cAMP; cAMP activate protein kinase A; kinase phosphorylate nhiều mục tiêu (target / 대상).

Tín hiệu khuếch đại giúp lượng ligand nhỏ tạo phản hồi (response / 응답) lớn, nhưng cũng đòi hỏi shutdown cơ chế (mechanism / 메커니즘) để tránh runaway activation.

> **Nối mạch:** **8. Calcium: ion vừa structural vừa tín hiệu (signal / 신호)** nối từ **7. Chất truyền tin thứ hai: đưa tín hiệu (signal / 신호) đi nhanh trong cytoplasm** sang **9. Receptor tyrosine kinase và sinh trưởng (growth) tín hiệu**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Calcium: ion vừa structural vừa tín hiệu (signal / 신호)

Cytosolic Ca²⁺ thường được giữ thấp so với extracellular không gian (space / 공간) và ER. độ dốc (gradient / 기울기) này cho phép Ca²⁺ tăng tạm thời trở thành tín hiệu (signal / 신호) mạnh.

Ca²⁺ có thể bind calmodulin, activate enzyme, trigger co cơ (muscle contraction) hoặc vesicle bản phát hành (release / 릴리스).

Sau đáp ứng, pump đưa Ca²⁺ trở lại store/outside. Nếu Ca²⁺ cao kéo dài không kiểm soát, cell có thể bị damage.

Một độ dốc (gradient / 기울기) được membrane chapter tạo ra giờ trở thành thông tin (information / 정보) channel.

> **Nối mạch:** **9. Receptor tyrosine kinase và sinh trưởng (growth) tín hiệu** nối từ **8. Calcium: ion vừa structural vừa tín hiệu (signal / 신호)** sang **10. Phosphorylation: molecular switch linh hoạt**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Receptor tyrosine kinase và sinh trưởng (growth) tín hiệu

**Receptor tyrosine kinase, RTK (수용체 티로신 키나아제)** thường activate khi ligand như yếu tố tăng trưởng bind và receptor dimerize/cluster.

Autophosphorylation tạo docking site cho truyền tín hiệu (signaling) protein (protein), mở pathway như Ras–MAPK hoặc PI3K–Akt.

Các pathway này điều chỉnh growth, survival, metabolism và biểu hiện gen.

Mutation làm RTK/pathway active liên tục có thể góp phần cancer.

> **Nối mạch:** **10. Phosphorylation: molecular switch linh hoạt** nối từ **9. Receptor tyrosine kinase và sinh trưởng (growth) tín hiệu** sang **11. Signaling cascade và lôgic (logic) mạng lưới (network)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Phosphorylation: molecular switch linh hoạt

**Protein kinase (단백질 키나아제)** transfer phosphate lên protein; **phosphatase (인산가수분해효소)** bỏ phosphate.

Phosphorylation có thể tăng hoặc giảm activity, đổi localization hoặc tương tác (interaction / 상호작용).

Một điểm cần tránh là nghĩ “phosphorylation luôn bật”. tác động (effect / 효과) phụ thuộc protein/site.

Kinase–phosphatase pair tạo reversible điều khiển (control / 제어) rất phù hợp cho hệ động (dynamic system / 동적 시스템).

> **Nối mạch:** **11. Signaling cascade và lôgic (logic) mạng lưới (network)** nối từ **10. Phosphorylation: molecular switch linh hoạt** sang **12. Độ đặc hiệu: cùng tín hiệu (signal / 신호) nhưng cell khác phản ứng khác**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Signaling cascade và lôgic (logic) mạng lưới (network)

Pathway thường được vẽ tuyến tính A → B → C, nhưng cell thật là mạng lưới (network). Một nút (node / 노드) có thể nhận nhiều đầu vào (input / 입력), branch ra nhiều đầu ra (output / 출력) và có phản hồi (feedback / 피드백).

```mermaid
flowchart TD
A[Receptor] --> B[Kinase 1]
B --> C[Kinase 2]
C --> D[Metabolism]
C --> E[Gene expression]
E -. feedback .-> B
F[Stress signal] --> C
```

Cross-talk giúp cell integrate ngữ cảnh (context / 맥락) thay vì phản ứng mechanical với một tín hiệu (signal / 신호) duy nhất.

> **Nối mạch:** **12. Độ đặc hiệu: cùng tín hiệu (signal / 신호) nhưng cell khác phản ứng khác** nối từ **11. Signaling cascade và lôgic (logic) mạng lưới (network)** sang **13. Desensitization: tại sao tín hiệu (signal / 신호) kéo dài không luôn tạo phản hồi (response / 응답) kéo dài?**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Độ đặc hiệu: cùng tín hiệu (signal / 신호) nhưng cell khác phản ứng khác

Adrenaline có thể tác động nhiều tissue nhưng phản hồi (response / 응답) khác vì receptor subtype và downstream protein khác.

Một cell chỉ “nghe” tín hiệu (signal / 신호) nếu có receptor phù hợp và truyền tín hiệu machinery tương ứng.

Đây là principle quan trọng của multicellularity: organism có thể dùng cùng hormone nhưng nhiều tissue interpret khác nhau.

> **Nối mạch:** **13. Desensitization: tại sao tín hiệu (signal / 신호) kéo dài không luôn tạo phản hồi (response / 응답) kéo dài?** nối từ **12. Độ đặc hiệu: cùng tín hiệu (signal / 신호) nhưng cell khác phản ứng khác** sang **14. phản hồi (feedback / 피드백) và feedforward trong truyền tín hiệu (signaling)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Desensitization: tại sao tín hiệu (signal / 신호) kéo dài không luôn tạo phản hồi (response / 응답) kéo dài?

Cell có thể giảm sensitivity bằng receptor internalization, phosphorylation receptor, degrade chất truyền tin thứ hai hoặc tăng inhibitor.

Đây là **thích nghi (adaptation)/desensitization**.

Ví dụ odor receptor đáp ứng (response) giảm khi mùi kéo dài. hệ thống (system / 시스템) quan tâm thay đổi (change / 변경) mới hơn là absolute tín hiệu (signal / 신호) cố định.

Điều khiển hệ thống (system / 시스템) luôn cần reset.

> **Nối mạch:** **14. phản hồi (feedback / 피드백) và feedforward trong truyền tín hiệu (signaling)** nối từ **13. Desensitization: tại sao tín hiệu (signal / 신호) kéo dài không luôn tạo phản hồi (response / 응답) kéo dài?** sang **15. Biểu hiện gen là phản hồi (response / 응답) chậm nhưng bền hơn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. phản hồi (feedback / 피드백) và feedforward trong truyền tín hiệu (signaling)

Phản hồi âm (negative feedback) giúp ổn định hoặc tạo thích nghi. Phản hồi dương (positive feedback) có thể tạo công tắc (switch)-like hành vi (behavior / 동작). Feedforward giúp anticipation hoặc lọc noise.

Mạng lưới sinh học (biological network) đôi khi tạo **tính lưỡng ổn (bistability)**: hệ thống (system / 시스템) có hai stable trạng thái (state / 상태) và tín hiệu đủ mạnh mới chuyển trạng thái (state / 상태).

Tế bào-cycle commitment là ví dụ nơi phản hồi dương giúp quyết định (decision / 결정) trở nên rõ ràng thay vì lưng chừng.

> **Nối mạch:** **15. Biểu hiện gen là phản hồi (response / 응답) chậm nhưng bền hơn** nối từ **14. phản hồi (feedback / 피드백) và feedforward trong truyền tín hiệu (signaling)** sang **16. Chu kỳ tế bào: division không phải default trạng thái (state / 상태)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Biểu hiện gen là phản hồi (response / 응답) chậm nhưng bền hơn

Signaling có thể phosphorylate enzyme trong vài giây. Nhưng nếu cell cần thay program nhiều giờ/ngày, pathway thường activate yếu tố phiên mã (transcription factor).

Yếu tố phiên mã vào nucleus/bind DNA và thay biểu hiện gen. Protein mới được tạo, làm trạng thái (state / 상태) cell thay đổi lâu hơn.

Đây là cầu nối (bridge / 브리지) trực tiếp sang molecular genetics.

> **Nối mạch:** **16. Chu kỳ tế bào: division không phải default trạng thái (state / 상태)** nối từ **15. Biểu hiện gen là phản hồi (response / 응답) chậm nhưng bền hơn** sang **17. Cyclin và CDK: oscillator molecular của chu kỳ tế bào**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. Chu kỳ tế bào: division không phải default trạng thái (state / 상태)

**Chu kỳ tế bào** gồm G1, S, G2 và M phase. Một số cell rời cycle vào G0.

- G1: sinh trưởng, sensing, chuẩn bị (preparation);
- S: DNA replication;
- G2: kiểm tra và chuẩn bị mitosis;
- M: chromosome segregation và cytokinesis.

Điều quan trọng là cell không đơn giản “đủ lớn rồi chia”. Nó phải integrate nutrient, sinh trưởng tín hiệu, DNA integrity và mô (tissue) bối cảnh (context).

> **Nối mạch:** **17. Cyclin và CDK: oscillator molecular của chu kỳ tế bào** nối từ **16. Chu kỳ tế bào: division không phải default trạng thái (state / 상태)** sang **18. Checkpoint: “đi tiếp hay dừng?”**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Cyclin và CDK: oscillator molecular của chu kỳ tế bào

**Cyclin-dependent kinase, CDK** là kinase được activate bởi cyclin. Cyclin mức (level / 수준) thay đổi theo cycle, tạo thời điểm (timing).

CDK phosphorylate mục tiêu (target / 대상) để drive chuyển tiếp (transition / 전이) giữa phase. Cyclin được synthesize và degraded có kiểm soát.

Điều khiển (control / 제어) bằng synthesis + destruction cho cycle có directionality.

> **Nối mạch:** **18. Checkpoint: “đi tiếp hay dừng?”** nối từ **17. Cyclin và CDK: oscillator molecular của chu kỳ tế bào** sang **19. Tổn thương DNA phản hồi (response / 응답) và p53**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Checkpoint: “đi tiếp hay dừng?”

Checkpoint là mạng (network / 네트워크) quyết định chuyển tiếp (transition / 전이) có an toàn không.

G1/S checkpoint đánh giá growth điều kiện (condition / 조건) và Tổn thương DNA trước replication. G2/M kiểm tra DNA replication/damage. Spindle checkpoint kiểm tra chromosome attachment trước segregation.

Checkpoint không phải vật lý (physical / 물리적) gate; nó là mạng lưới điều hòa (regulatory network).

> **Nối mạch:** **19. Tổn thương DNA phản hồi (response / 응답) và p53** nối từ **18. Checkpoint: “đi tiếp hay dừng?”** sang **20. Mitosis: mục tiêu là chia chromosome đã bản sao (copy / 복사) chính xác**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Tổn thương DNA phản hồi (response / 응답) và p53

Tổn thương DNA activate sensor con đường (pathway). **p53** có thể induce cell-cycle arrest, repair program, senescence hoặc apoptosis tùy ngữ cảnh (context / 맥락).

p53 thường được gọi “guardian of the genome”, nhưng mô hình tư duy tốt hơn là transcriptional quyết định (decision / 결정) nút (node / 노드) nhận stress tín hiệu.

Mutation p53 pathway có thể cho damaged cell tiếp tục proliferate, tăng cancer rủi ro (risk / 위험).

> **Nối mạch:** **20. Mitosis: mục tiêu là chia chromosome đã bản sao (copy / 복사) chính xác** nối từ **19. Tổn thương DNA phản hồi (response / 응답) và p53** sang **21. Meiosis khác vì mục tiêu khác**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Mitosis: mục tiêu là chia chromosome đã bản sao (copy / 복사) chính xác

Sau S phase, mỗi chromosome có nhiễm sắc tử chị em (sister chromatid). Trong mitosis, spindle microtubule attach kinetochore, align và kéo nhiễm sắc tử chị em sang hai pole.

Phases như prophase, metaphase, anaphase, telophase hữu ích để mô tả, nhưng cơ chế (mechanism / 메커니즘) quan trọng hơn tên phase: chromosome condense, attach, tension được kiểm tra, cohesion bị bản phát hành (release / 릴리스), segregation diễn ra.

Cytokinesis sau đó chia cytoplasm.

> **Nối mạch:** **21. Meiosis khác vì mục tiêu khác** nối từ **20. Mitosis: mục tiêu là chia chromosome đã bản sao (copy / 복사) chính xác** sang **22. Apoptosis: chết tế bào (cell death) có thể là chương trình có lợi cho sinh vật (organism)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. Meiosis khác vì mục tiêu khác

Mitosis duy trì số lượng nhiễm sắc thể (chromosome number) và tạo cell tương tự. **Meiosis (감수분열)** tạo gamete haploid và biến dị (variation).

Meiosis có một lần DNA replication nhưng hai lần division. Nhiễm sắc thể tương đồng (homologous chromosome) pair và recombine ở meiosis I, sau đó homolog tách; meiosis II tách nhiễm sắc tử chị em.

Trao đổi chéo (crossing-over) và phân ly độc lập (independent assortment) tạo combination allele mới.

Meiosis là cầu nối (bridge / 브리지) giữa chu kỳ tế bào và di truyền (inheritance) di truyền học (genetics).

> **Nối mạch:** **22. Apoptosis: chết tế bào (cell death) có thể là chương trình có lợi cho sinh vật (organism)** nối từ **21. Meiosis khác vì mục tiêu khác** sang **23. Cancer: thất bại (failure / 실패) của multi-layer điều khiển (control / 제어)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 22. Apoptosis: chết tế bào (cell death) có thể là chương trình có lợi cho sinh vật (organism)

**Apoptosis (세포자멸사)** là regulated chết tế bào. Cell shrink, DNA fragmented có kiểm soát và debris được clear tương đối ít inflammation.

Apoptosis loại damaged cell và sculpt tissue trong phát triển (development). Ví dụ mô giữa developing digits bị loại để tạo ngón tách biệt.

Ở sinh vật đa bào, survival của individual cell không phải mục tiêu tối cao; integrity của organism mới là ngữ cảnh (context / 맥락) lớn hơn.

> **Nối mạch:** **23. Cancer: thất bại (failure / 실패) của multi-layer điều khiển (control / 제어)** nối từ **22. Apoptosis: chết tế bào (cell death) có thể là chương trình có lợi cho sinh vật (organism)** sang **24. Tình huống phân tích (case study): insulin tín hiệu (signal / 신호) nối organism với cell chuyển hóa (metabolism)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 23. Cancer: thất bại (failure / 실패) của multi-layer điều khiển (control / 제어)

Cancer không đơn giản là “cell chia nhanh”. Nó là evolutionary tiến trình (process / 프로세스) trong mô, thường cần nhiều alteration ảnh hưởng growth tín hiệu, checkpoint, apoptosis, độ ổn định hệ gen (genome stability), metabolism và tương tác (interaction / 상호작용) với microenvironment.

Một tumor cell có mutation tăng proliferation; clone đó expand; thêm mutation có thể tiếp tục được selection trong tumor môi trường (environment / 환경).

Cancer nối truyền tín hiệu tế bào (cell signaling) với genetics và tiến hóa (evolution).

> **Nối mạch:** **23. Cancer: thất bại (failure / 실패) của multi-layer điều khiển (control / 제어)** nêu quy tắc; **24. Tình huống phân tích (case study): insulin tín hiệu (signal / 신호) nối organism với cell chuyển hóa (metabolism)** thử quy tắc trong tình huống, rồi **25. Tình huống phân tích: yếu tố tăng trưởng và proliferation** mở rộng hệ quả.

## 24. Tình huống phân tích (case study): insulin tín hiệu (signal / 신호) nối organism với cell chuyển hóa (metabolism)

Sau meal, đường huyết (blood glucose) tăng. Pancreatic beta cell bản phát hành (release / 릴리스) insulin. Insulin receptor trên mục tiêu (target / 대상) cell activate signaling cascade. Ở muscle/adipose ngữ cảnh (context / 맥락), GLUT4 vesicle được đưa ra màng, tăng glucose uptake. Enzym metabolism cũng được regulation.

Chuỗi nhiều quy mô (scale / 규모):

```text
meal
→ blood glucose
→ endocrine signal
→ receptor
→ kinase network
→ transporter/metabolic enzyme
→ glucose flux
```

Một hormone không “hạ đường” trực tiếp; nó thay cell hành vi.

> **Nối mạch:** **24. Tình huống phân tích (case study): insulin tín hiệu (signal / 신호) nối organism với cell chuyển hóa (metabolism)** nêu quy tắc; **25. Tình huống phân tích: yếu tố tăng trưởng và proliferation** thử quy tắc trong tình huống, rồi **26. Các hiểu lầm phổ biến (common misconceptions)** mở rộng hệ quả.

## 25. Tình huống phân tích: yếu tố tăng trưởng và proliferation

Yếu tố tăng trưởng bind receptor → MAPK signaling → yếu tố phiên mã → cyclin expression → tế bào-cycle entry.

Nếu receptor/con đường mutation làm tín hiệu (signal / 신호) “on” ngay cả không có ligand, cell có thể nhận false message rằng môi trường đang cho phép growth.

Đây là ví dụ thông tin (information / 정보) processing thất bại (failure / 실패).

> **Nối mạch:** **25. Tình huống phân tích: yếu tố tăng trưởng và proliferation** nêu quy tắc; **26. Các hiểu lầm phổ biến (common misconceptions)** thử quy tắc trong tình huống, rồi **Định lượng tín hiệu (signal / 신호)–phản hồi (response / 응답): receptor occupancy không phải toàn bộ câu chuyện** mở rộng hệ quả.

## 26. Các hiểu lầm phổ biến (common misconceptions)

“tín hiệu (signal / 신호) mạnh hơn luôn phản hồi (response / 응답) lớn hơn tuyến tính” sai; pathway có bão hòa (saturation), ngưỡng (threshold), phản hồi (feedback / 피드백) và thích nghi.

“Một receptor chỉ có một pathway” thường sai; cross-talk và branching phổ biến.

“Phosphorylation luôn activate” sai.

“Chu kỳ tế bào chạy như đồng hồ độc lập” sai; nó tích hợp environmental/nội bộ (internal / 내부) tín hiệu (signal / 신호).

“Cancer do một gene duy nhất” thường sai; cancer thường là multistep evolutionary tiến trình (process / 프로세스).

“Apoptosis luôn xấu” sai; controlled chết tế bào cần cho development và tissue health.

<!-- depth-audit-2026:signal-quantitation -->

> **Nối mạch:** **Định lượng tín hiệu (signal / 신호)–phản hồi (response / 응답): receptor occupancy không phải toàn bộ câu chuyện** nối từ **26. Các hiểu lầm phổ biến (common misconceptions)** sang **Tế bào mã hóa thông tin bằng thời gian**, vì cơ chế trước tạo đầu vào cho bước sau.

## Định lượng tín hiệu (signal / 신호)–phản hồi (response / 응답): receptor occupancy không phải toàn bộ câu chuyện

Nếu ligand \(L\) gắn receptor với hằng số phân ly \(K_d\), phần receptor được chiếm trong mô hình đơn giản là:

\[
f=\frac{[L]}{K_d+[L]}
\]

Quan hệ này bão hòa: tăng ligand từ rất thấp tới gần \(K_d\) tạo thay đổi lớn, nhưng khi receptor gần bão hòa, thêm ligand tạo ít khác biệt hơn. Downstream mạng (network / 네트워크) còn có amplification, phosphatase, phản hồi (feedback / 피드백) và threshold nên **đáp ứng tế bào không đồng nhất với receptor occupancy**.

Với hệ có tính hiệp đồng, phương trình Hill thường được dùng như mô hình hiện tượng:

\[
phản hồi (response / 응답)=\frac{[L]^n}{K^n+[L]^n}
\]

\(n>1\) tạo đường cong dốc hơn và có thể giúp quyết định trở nên switch-like. Nhưng \(n\) là tham số mô tả; không nên tự động diễn giải nó như đúng số phân tử cùng gắn.

> **Nối mạch:** **Tế bào mã hóa thông tin bằng thời gian** nối từ **Định lượng tín hiệu (signal / 신호)–phản hồi (response / 응답): receptor occupancy không phải toàn bộ câu chuyện** sang **Commitment của cell cycle cần cơ chế làm quyết định khó đảo ngược**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tế bào mã hóa thông tin bằng thời gian

Hai tín hiệu (signal / 신호) có cùng nồng độ trung bình vẫn có thể tạo kết quả khác nếu một tín hiệu (signal / 신호) liên tục còn tín hiệu (signal / 신호) kia phát xung. Ca²⁺, ERK, NF-κB và nhiều pathway có thể dùng **tần số, độ dài xung và lịch sử kích thích (signal history)** để mã hóa trạng thái. phản hồi (feedback / 피드백) âm tạo adaptation; phản hồi (feedback / 피드백) dương tạo commitment; degradation và phosphatase xác định bộ nhớ (memory / 메모리) của pathway.

> **Nối mạch:** Cell mã hóa information bằng thời gian; cell-cycle commitment làm quyết định khó đảo ngược. **Cầu nối** kiểm tra cách signal ngắn hạn thành chương trình dài hạn.

## Commitment của cell cycle cần cơ chế làm quyết định khó đảo ngược

G1/S chuyển tiếp (transition / 전이) không chỉ là “cyclin đủ cao”. Trục RB–E2F tạo phản hồi (feedback / 피드백) giúp cell vượt **điểm hạn chế (restriction point)** khi tín hiệu tăng trưởng, dinh dưỡng và genome integrity phù hợp. Sau đó, ubiquitin ligase như SCF và APC/C phá hủy protein điều hòa theo thứ tự, làm chuyển tiếp (transition / 전이) có tính hướng và giảm khả năng quay ngược tùy tiện.

Cơ chế này giải thích vì sao thất bại (failure / 실패) ở cell cycle thường là thất bại (failure / 실패) của mạng (network / 네트워크) chứ không phải một nút đơn. Oncogene có thể tăng drive, tumor suppressor mất mát (loss / 손실) làm mất brake, repair defect tăng variation; selection trong mô sau đó giữ clone có lợi thế tăng trưởng. Cancer vì vậy nối trực tiếp **regulation → thất bại (failure / 실패) → somatic evolution**.

> **Nối mạch:** Cell-cycle commitment tạo trạng thái khó đảo ngược; cầu nối cuối giải thích cách signal ngắn hạn chuyển thành chương trình dài hạn.

## 27. Cầu nối: tín hiệu (signal / 신호) ngắn hạn trở thành chương trình dài hạn bằng cách nào?

Truyền tín hiệu cho phép cell sense và respond. Nhưng khi yếu tố phiên mã được activate, nó phải đọc một vật lý (physical / 물리적) thông tin (information / 정보) hệ thống (system / 시스템). DNA chuỗi (sequence / 시퀀스) ở đâu? Gene là gì? Làm sao trình tự (sequence) được bản sao (copy / 복사), transcribed và translated? Làm sao mutation thay protein?

Đó là câu hỏi của [DNA, Gene và Biểu hiện gene](../02_genetics_molecular_biology/00_dna_genes_and_gene_expression.md).

Sau đó, meiosis vừa học sẽ được nối với Mendelian inheritance trong [Di truyền, Biến dị và Đột biến](../02_genetics_molecular_biology/01_inheritance_variation_and_mutation.md).

> **Mô hình tư duy cuối chapter:** truyền tín hiệu tế bào là computation bằng molecule: receptor nhận đầu vào (input / 입력), mạng (network / 네트워크) transform/integrate tín hiệu (signal / 신호), effector tạo đầu ra (output / 출력), phản hồi điều chỉnh gain. Chu kỳ tế bào là một quyết định (decision / 결정) hệ thống (system / 시스템) gắn chặt với signaling và genome integrity; genetics là tầng (layer / 계층) thông tin (information / 정보) giúp các quyết định (decision / 결정) này được duy trì qua thời gian.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Chuyển hóa, Hô hấp tế bào và Quang hợp](01_metabolism_respiration_photosynthesis.md) · [Mục lục Biology](../README.md) · [Đa bào, mô và chất nền ngoại bào →](03_multicellularity_tissues_and_extracellular_matrix.md)

> **Bàn giao:** Sau **27. Cầu nối: tín hiệu (signal / 신호) ngắn hạn trở thành chương trình dài hạn bằng cách nào?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
