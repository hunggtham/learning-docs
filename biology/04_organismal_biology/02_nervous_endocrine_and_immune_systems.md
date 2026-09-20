# Hệ thần kinh, Nội tiết và Miễn dịch — Nervous, Endocrine and Immune Systems (신경계, 내분비계와 면역계)

Animal physiology vừa cho thấy organism cần coordination giữa nhiều organ. Nhưng coordination có ít nhất ba kiểu bài toán khác nhau. Có response phải cực nhanh và định vị chính xác, như rút tay khỏi vật nóng. Có response cần chậm hơn nhưng kéo dài toàn thân, như điều chỉnh growth hay metabolism. Có response phải phân biệt “self–nonself”, nhận diện pathogen và tạo memory. Ba lớp control tương ứng nổi bật là **nervous system, endocrine system và immune system**.

> **Mental model:** nervous system tối ưu cho tốc độ và wiring; endocrine system tối ưu cho broadcast chemical signal; immune system tối ưu cho recognition + adaptive memory. Chúng không độc lập mà liên tục tương tác.

## 1. Neuron là cell chuyên hóa cho information flow

**Neuron (뉴런)** có dendrite nhận input, soma tích hợp và axon truyền output tới cell khác.

Thông tin trong neuron không phải electron chạy như dây đồng. Nó được mã hóa bằng thay đổi **membrane potential** do ion channel mở/đóng.

Membrane chapter đã xây electrochemical gradient; nervous system khai thác gradient đó như communication medium.

## 2. Resting membrane potential

Neuron giữ K⁺ cao bên trong, Na⁺ cao bên ngoài nhờ transporter/pump và selective permeability.

Resting potential thường âm vì membrane permeable với K⁺ và distribution ion/protein charge.

Na⁺/K⁺-ATPase duy trì gradient dài hạn; leak channel quyết định nhiều resting conductance.

Pump không trực tiếp tạo từng spike; nó giữ “battery” ion để spike có thể xảy ra.

## 3. Action potential

Khi depolarization đạt threshold, voltage-gated Na⁺ channel mở nhanh → Na⁺ vào → depolarization mạnh. Sau đó Na⁺ channel inactivate và voltage-gated K⁺ channel mở → K⁺ ra → repolarization.

Refractory period giúp spike đi một chiều và giới hạn firing frequency.

Action potential là **all-or-none event** ở một segment membrane; intensity stimulus thường được encode nhiều hơn bằng firing frequency/pattern chứ không phải spike “cao hơn”.

## 4. Myelin và saltatory conduction

Myelin cách điện axon, làm current lan xa hơn giữa node of Ranvier. Action potential được regenerate tại node, tạo **saltatory conduction** nhanh và energy-efficient hơn.

Multiple sclerosis làm myelin CNS bị damage, cho thấy structure–function của myelin trực tiếp ảnh hưởng signal propagation.

## 5. Synapse: từ electrical signal sang chemical signal rồi quay lại electrical

Ở chemical synapse, action potential tới terminal → voltage-gated Ca²⁺ channel mở → Ca²⁺ trigger vesicle exocytosis → neurotransmitter release → bind receptor postsynaptic.

Một lần nữa, Ca²⁺ gradient + vesicle transport + receptor signaling từ cell biology được tái sử dụng.

Synapse có delay nhỏ nhưng cho phép amplification, modulation và plasticity.

## 6. Excitatory và inhibitory input

Postsynaptic receptor có thể làm membrane dễ hoặc khó đạt threshold hơn.

Neuron tích hợp hàng nghìn input theo space/time. Output spike là result của network integration.

Điều này gần với weighted-sum idea trong artificial neural network, nhưng biological neuron phức tạp hơn nhiều về dynamics, chemistry và plasticity.

## 7. Neurotransmitter không có một “ý nghĩa” cố định

Glutamate thường excitatory ở CNS, GABA thường inhibitory, nhưng effect cuối cùng phụ thuộc receptor subtype và ion gradient.

Acetylcholine làm skeletal muscle contract nhưng có thể giảm heart rate qua receptor khác.

Signal molecule không quyết định outcome một mình; receptor/context quyết định interpretation.

## 8. Sensory transduction

Sensory receptor chuyển light, pressure, chemical, temperature hoặc sound thành electrical signal.

Photoreceptor dùng opsin signaling; hair cell inner ear dùng mechanical channel; olfactory receptor thường dùng GPCR.

Nervous system bắt đầu bằng transduction physical world → membrane signal.

## 9. Reflex arc

Một reflex cơ bản có sensory neuron → spinal integration → motor neuron → muscle response.

Brain vẫn nhận information, nhưng fast response có thể được tổ chức local ở spinal cord.

Architecture phân cấp giảm latency.

## 10. Central và peripheral nervous system

CNS gồm brain/spinal cord; PNS nối CNS với body.

Somatic system liên quan voluntary skeletal muscle/sensory; autonomic system điều chỉnh smooth muscle, cardiac muscle, gland.

Sympathetic/parasympathetic không nên học kiểu “một cái stress, một cái relax” quá cứng; chúng có organ-specific pattern và phối hợp.

## 11. Neuroplasticity

Synapse strength có thể thay theo activity. Long-term potentiation/depression là model của synaptic plasticity liên quan learning/memory.

Memory không nằm trong một “file” neuron; nó liên quan distributed network change.

Gene expression và protein synthesis tham gia long-term plasticity, nối neuroscience với molecular genetics.

## 12. Endocrine system: communication bằng hormone

**Hormone (호르몬)** là signaling molecule được release và tác động target có receptor phù hợp, thường qua circulation.

Hormone concentration thấp vẫn có effect vì receptor/signaling amplification.

Endocrine signal chậm hơn synaptic signal nhưng có thể kéo dài và tác động nhiều tissue.

## 13. Peptide và steroid hormone

Peptide hormone hydrophilic thường bind membrane receptor và activate second messenger.

Steroid hormone lipid-soluble có thể xuyên membrane, bind intracellular receptor và điều chỉnh transcription.

Chemistry của signal quyết định signaling architecture.

## 14. Hypothalamus–pituitary axis

Hypothalamus nối nervous và endocrine system. Nó sense neural/internal state và điều khiển pituitary hormone.

Axis như HPA (stress) hay HPT (thyroid) dùng nhiều tầng hormone + negative feedback.

```text
hypothalamus
→ pituitary
→ peripheral gland
→ hormone
↘ negative feedback upstream
```

Cascade cho amplification và multi-level control.

## 15. Thyroid hormone và metabolic rate

TSH từ pituitary stimulate thyroid; thyroid hormone ảnh hưởng gene expression/metabolism ở nhiều tissue.

Negative feedback của T3/T4 lên hypothalamus/pituitary giúp giữ range.

Clinical interpretation hormone vì vậy cần nhìn cả upstream/downstream, không chỉ một number.

## 16. Stress response

Acute stress có sympathetic activation và adrenal catecholamine; HPA axis tạo cortisol response chậm hơn.

Stress response giúp mobilize energy và adjust physiology ngắn hạn, nhưng chronic dysregulation có consequence khác.

Biological stress không đơn giản là “cảm thấy lo”; nó là multi-system state.

## 17. Immune system: recognition problem

Immune system phải phát hiện threat nhưng tránh attack tissue bình thường quá mức.

**Innate immunity (선천면역)** nhận conserved pattern và phản ứng nhanh. **Adaptive immunity (적응면역)** tạo receptor diversity, clonal expansion và memory.

Hai nhánh phối hợp, không phải two separate armies.

## 18. Barrier immunity

Skin, mucus, stomach acid, antimicrobial peptide và microbiota là first line defense.

Ngăn entry thường hiệu quả hơn tiêu diệt pathogen sau invasion.

Barrier nối anatomy, chemistry và ecology microbiome.

## 19. Pattern recognition và inflammation

Innate immune receptor nhận PAMP/DAMP, kích hoạt cytokine, vascular change và immune-cell recruitment.

**Inflammation (염증)** giúp containment/repair nhưng nếu quá mạnh hoặc chronic có thể gây tissue damage.

Inflammation vì vậy là regulated defense, không đồng nghĩa “infection”.

## 20. Phagocyte và complement

Neutrophil/macrophage có thể phagocytose microbe. Complement protein trong blood có thể opsonize, amplify inflammation và làm damage membrane pathogen.

Innate system dùng recognition tương đối broad nhưng response nhanh.

## 21. Antigen presentation nối innate với adaptive

Dendritic cell uptake/process antigen rồi present peptide trên MHC cho T cell.

T cell không “nhìn thấy nguyên virus” theo cách kháng thể; receptor T cell nhận peptide–MHC complex.

MHC diversity ảnh hưởng repertoire antigen presentation ở population.

## 22. B cell và antibody

B cell receptor bind antigen; sau activation thích hợp, clone expand và differentiate thành plasma cell/memory cell.

Antibody có variable region nhận antigen và constant region recruit effector function.

Class switching thay constant region mà giữ antigen specificity tương đối, điều chỉnh loại response.

## 23. T cell

CD4 T cell điều phối immune response qua cytokine/help; CD8 cytotoxic T cell có thể kill infected/cancer cell presenting target peptide.

Adaptive immunity là network cell–signal, không chỉ antibody.

## 24. Clonal selection: evolution-like logic trong cơ thể

B/T cell repertoire chứa nhiều receptor variation. Antigen “select” clone phù hợp để expand.

Somatic hypermutation/affinity maturation ở B cell còn tạo variation và selection trong germinal center.

Logic variation → selection → expansion giống evolutionary motif nhưng xảy ra trong immune cell population của một organism.

## 25. Immune memory và vaccine

Sau response, memory B/T cell tồn tại lâu hơn, giúp secondary response nhanh/mạnh hơn.

Vaccine đưa antigen/instruction theo cách kiểm soát để tạo adaptive memory mà giảm risk disease so với natural infection.

Vaccine không tạo “hàng rào tuyệt đối” trong mọi case; effectiveness phụ thuộc pathogen, antigen, immune state và time.

## 26. Tolerance và autoimmunity

Immune system phải loại/kiểm soát lymphocyte phản ứng self qua central/peripheral tolerance.

Nếu tolerance fail, autoimmunity có thể xảy ra.

Nếu response quá yếu, infection/cancer surveillance giảm. Immune regulation là trade-off sensitivity–self-damage.

## 27. Allergy

Allergy là inappropriate immune response với antigen thường harmless, thường liên quan IgE/mast cell trong nhiều type.

Histamine gây vascular permeability, itch, mucus và symptom khác.

Allergy không phải immune system “yếu”; đó là misdirected response.

## 28. Nervous–endocrine–immune interaction

Stress hormone ảnh hưởng immune cell; cytokine ảnh hưởng brain/behavior; vagal/autonomic signal ảnh hưởng inflammation; immune activation gây fatigue/fever.

Ba system tạo network feedback.

Không nên học chúng như ba chapter hoàn toàn độc lập của anatomy.

## 29. Case study: fever

Pathogen/immune signal → cytokine → hypothalamic prostaglandin signaling → set point tăng → vasoconstriction/shivering → body temperature tăng.

Fever là output nervous–immune–endocrine-like integration chứ không chỉ “cơ thể nóng vì infection”.

## 30. Case study: epinephrine khi chạy

Exercise/stress → sympathetic/adrenal signal → epinephrine → heart rate/contractility tăng, glycogen breakdown tăng ở context, blood flow redistribute.

Hormone đưa same message toàn body nhưng tissue response khác tùy receptor/signaling network.

## 31. Common misconceptions

“Neuron truyền điện như dây điện” quá đơn giản; ion gradient và channel tạo signal.

“Neurotransmitter X luôn excitatory” sai; receptor/context quyết định.

“Hormone chỉ liên quan sinh dục” sai; hormone điều khiển metabolism, growth, water balance, stress và nhiều process.

“Immune mạnh hơn luôn tốt hơn” sai; overactivation gây allergy/autoimmunity/tissue damage.

“Antibody là toàn bộ adaptive immunity” sai.

## 32. Bridge: một organism được xây từ một fertilized cell như thế nào?

Nervous, endocrine và immune system đều yêu cầu nhiều specialized cell type. Nhưng tất cả bắt đầu từ zygote và gần cùng genome. Vậy cell biết trở thành neuron, muscle hay immune cell bằng cách nào? Body axis, organ và tissue pattern hình thành ra sao?

[[03_reproduction_and_development]] sẽ nối meiosis/fertilization với gene regulation, morphogen, stem cell và developmental pattern.

> **Mental model cuối chapter:** coordination của organism là information problem. Nervous system dùng spike/synapse cho tốc độ; endocrine dùng hormone cho broadcast lâu dài; immune dùng receptor diversity cho recognition và memory. Cả ba tái sử dụng cùng nguyên lý receptor, gradient, feedback và gene expression từ cell biology.