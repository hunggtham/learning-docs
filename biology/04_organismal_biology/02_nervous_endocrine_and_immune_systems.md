# Hệ thần kinh, nội tiết và miễn dịch — Nervous, Endocrine and Immune Systems (신경계, 내분비계와 면역계)

Một organism lớn cần nhiều cell hoạt động như một whole system. Điều đó tạo ba bài toán khác nhau nhưng liên kết chặt:

- truyền information nhanh và chính xác;
- điều chỉnh state cơ thể trên khoảng cách xa và thời gian dài hơn;
- phát hiện damage hoặc biological threat mà không phá chính tissue của mình.

Hệ thần kinh, endocrine và immune là ba solution lớn cho các bài toán đó.

# Nervous system — information bằng điện và hóa học

Neuron đặc biệt vì membrane của nó duy trì electrochemical gradient và có thể thay membrane potential rất nhanh.

## Neuron structure

Một **neuron (tế bào thần kinh / 뉴런)** điển hình có dendrite nhận input, cell body tích hợp và axon truyền signal xa.

Neuron không hoạt động một mình. **Glia (tế bào thần kinh đệm / 신경교세포)** support metabolism, myelination, ion balance, immune function và synapse.

Mental model “brain chỉ là neuron” vì vậy quá hẹp.

## Resting membrane potential

Neuron có concentration K⁺ cao hơn bên trong, Na⁺ cao hơn bên ngoài, và membrane permeability không giống nhau cho mọi ion.

Na⁺/K⁺ ATPase duy trì gradient lâu dài; leak channel và charge distribution tạo **resting membrane potential (전위)**, thường negative bên trong.

Pump không trực tiếp tạo từng action potential; nó duy trì gradient để electrical signaling có thể tiếp tục.

## Action potential — signal all-or-none

Khi membrane depolarization đạt threshold, voltage-gated Na⁺ channel mở nhanh. Na⁺ vào cell làm depolarization tăng thêm — positive feedback.

Sau đó Na⁺ channel inactivate và voltage-gated K⁺ channel mở, K⁺ đi ra, membrane repolarize.

**Action potential (điện thế hoạt động / 활동전위)** là event all-or-none về amplitude trong một axon segment. Stronger stimulus thường được encode bằng firing frequency hoặc number of neuron recruited, không phải action potential “cao gấp đôi”.

## Refractory period và direction

Sau action potential, channel cần thời gian reset. **Refractory period (불응기)** làm segment vừa fired khó fire ngay lại, giúp signal propagate một chiều dọc axon trong normal condition.

## Myelin — tăng tốc bằng cách thay electrical architecture

**Myelin (수초)** cách điện axon. Voltage-gated channel tập trung nhiều ở node of Ranvier, nên action potential được regenerate từng node, gọi là **saltatory conduction (도약전도)**.

Signal không literal nhảy bỏ qua physics; current lan dưới myelin rồi trigger next node.

## Synapse — từ electrical signal sang chemical signal

Ở chemical synapse, action potential tới terminal mở voltage-gated Ca²⁺ channel. Ca²⁺ trigger vesicle fuse membrane và release **neurotransmitter (신경전달물질)**.

Neurotransmitter diffuse qua synaptic cleft, bind receptor ở postsynaptic cell.

Receptor có thể tạo excitatory hoặc inhibitory effect tùy ion/channel/pathway. Vì vậy neurotransmitter không tự thân “kích thích” hay “ức chế” tuyệt đối; receptor context matter.

## CNS và PNS

**Central nervous system (CNS / 중추신경계)** gồm brain và spinal cord.

**Peripheral nervous system (PNS / 말초신경계)** nối CNS với body.

Motor output thường được chia somatic và autonomic. Autonomic system gồm sympathetic và parasympathetic branch theo model cơ bản.

Sympathetic không đơn giản là “xấu/stress”, parasympathetic không chỉ “nghỉ”. Cả hai điều chỉnh organ tùy context và thường cùng maintain homeostasis.

## Reflex — behavior nhanh không cần conscious decision trước

Trong withdrawal reflex, sensory neuron detect painful stimulus, spinal circuit activate motor response trước khi cortical awareness hoàn tất.

Điều này cho thấy nervous system có nhiều control level, không phải mọi signal đều đi “lên brain rồi brain ra lệnh”.

# Endocrine system — broadcast bằng hormone

**Hormone (호르몬)** là signaling molecule được release bởi cell/gland và tác động target có receptor phù hợp, thường qua circulation.

Hormone signal chậm hơn synaptic transmission theo nhiều context nhưng có thể kéo dài hơn và ảnh hưởng nhiều tissue.

## Peptide và steroid hormone

Peptide hormone hydrophilic nên thường bind cell-surface receptor và activate second messenger.

Steroid hormone derived từ cholesterol, hydrophobic hơn nên có thể cross membrane và bind intracellular receptor, ảnh hưởng transcription.

Không phải hormone nào cũng fit hoàn hảo hai box này, nhưng distinction giúp hiểu mechanism.

## Hypothalamus và pituitary — bridge nervous–endocrine

**Hypothalamus (시상하부)** nhận neural/internal signal và điều khiển endocrine pathway.

**Pituitary gland (tuyến yên / 뇌하수체)** release hormone điều khiển nhiều gland khác.

Ví dụ hypothalamus → pituitary → thyroid là một axis có feedback. Thyroid hormone tăng có thể feedback giảm upstream signal.

Điểm chính là endocrine system thường được tổ chức thành **axis + feedback**, không phải gland độc lập.

## Insulin và glucagon — glucose regulation

Sau meal, blood glucose tăng. Pancreatic beta cell release **insulin**, thúc đẩy nhiều tissue uptake/store nutrient và giảm một số process tạo glucose.

Khi glucose thấp, alpha cell release **glucagon**, tăng hepatic glucose output qua glycogen breakdown và gluconeogenesis.

Đây là simplification; real glucose control có incretin, autonomic input, cortisol, catecholamine và tissue-specific response.

Điều quan trọng là insulin/glucagon tạo coordinated metabolic state.

## Stress response

Sympathetic nervous system và adrenal medulla tạo fast catecholamine response. Hypothalamic–pituitary–adrenal axis tạo cortisol response chậm hơn.

Stress response không mặc định có hại. Acute response giúp mobilize energy và cardiovascular resources. Problem có thể xuất hiện khi activation chronic hoặc dysregulated.

# Immune system — recognition dưới uncertainty

Immune system có bài toán đặc biệt: phải phản ứng đủ mạnh với pathogen/damage nhưng tránh tấn công tissue bình thường.

Nó không có một “database hoàn hảo” biết trước mọi threat. Thay vào đó, nhiều layer recognition và feedback phối hợp.

## Barrier — defense bắt đầu trước immune cell

Skin, mucus, cilia, stomach acid, antimicrobial molecule và resident microbiota tạo **barrier defense**.

Nếu pathogen không vượt barrier, immune response sâu hơn không cần activate mạnh.

## Innate immunity — nhanh và pattern-based

**Innate immunity (miễn dịch bẩm sinh / 선천면역)** nhận pattern phổ biến qua **pattern-recognition receptor (PRR)**.

Macrophage, neutrophil, dendritic cell, natural killer cell và complement system là các component quan trọng.

Innate immunity thường phản ứng nhanh và tạo inflammation.

### Inflammation

**Inflammation (viêm / 염증)** là coordinated response tăng blood flow, vascular permeability và recruitment immune cell.

Redness, heat, swelling và pain có thể là consequence của process này.

Inflammation giúp containment/repair nhưng nếu excessive/chronic có thể damage tissue.

## Phagocytosis

Macrophage và neutrophil có thể engulf particle/microbe bằng **phagocytosis (식균작용)**.

Material nằm trong vesicle rồi được xử lý cùng lysosomal machinery.

Dendritic cell còn nối innate với adaptive immunity qua antigen presentation.

## Adaptive immunity — specificity và memory

**Adaptive immunity (miễn dịch thích ứng / 적응면역)** dựa chủ yếu trên B cell và T cell.

Mỗi lymphocyte lineage có receptor specificity khác nhau được tạo qua gene rearrangement. Khi receptor phù hợp antigen và nhận đủ activation context, cell clone expand.

Đây gọi là **clonal selection (선택)**.

## B cell và antibody

B cell có thể differentiate thành plasma cell tiết **antibody (kháng thể / 항체)**.

Antibody bind antigen cụ thể và có thể neutralize, opsonize hoặc activate other immune mechanism.

Antibody specificity đến từ variable region; constant region quyết định nhiều effector property.

## T cell

T cell thường nhận peptide antigen được trình bày bởi **MHC (major histocompatibility complex / 주조직적합복합체)**.

CD4 T cell điều phối immune response qua cytokine và interaction với cell khác.

CD8 T cell có thể kill infected/abnormal cell khi nhận peptide phù hợp trong MHC I context.

T cell không “nhìn” nguyên pathogen giống antibody; nó đọc peptide fragment được cell trình bày.

## Immunological memory

Sau infection hoặc vaccination, một phần B/T cell trở thành memory population. Khi antigen tương tự xuất hiện lại, response thường nhanh/mạnh hơn.

Vaccination khai thác principle này bằng cách đưa immune system gặp antigen hoặc instruction tạo antigen trong controlled context mà không cần trải qua disease tự nhiên đầy đủ.

## Self-tolerance — tại sao immune system không luôn đánh chính mình?

Lymphocyte receptor được tạo đa dạng nên inevitably có receptor nhận self molecule.

Developmental selection và peripheral regulatory mechanism giúp loại/inactivate/control self-reactive clone.

Khi tolerance fail, autoimmune disease có thể xuất hiện.

## Allergy — response không tương xứng với threat

**Allergy (dị ứng / 알레르기)** là immune response với substance thường không nguy hiểm ở đa số người, ví dụ pollen hoặc food protein.

IgE, mast cell và histamine thường liên quan một số allergic reaction.

Điều này cho thấy immune system không phải detector hoàn hảo “xấu/tốt”; nó là inference/control system có trade-off false positive và false negative.

## Nervous, endocrine và immune không tách rời

Stress hormone ảnh hưởng immune activity. Cytokine từ immune cell ảnh hưởng brain và behavior. Vagus nerve và autonomic pathway ảnh hưởng inflammation. Sleep/circadian rhythm ảnh hưởng hormone và immune state.

Vì vậy việc chia thành ba system chủ yếu để học; trong organism chúng là một network.

## Common misconceptions

### “Neuron truyền điện giống dây đồng”

Không. Axon dùng ion gradient và voltage-gated channel để regenerate signal dọc membrane.

### “Hormone chỉ liên quan giới tính”

Hormone điều hòa glucose, growth, stress, water balance, thyroid function, reproduction và nhiều process khác.

### “Immune mạnh hơn luôn tốt hơn”

Không. Overactive immune response có thể gây allergy, autoimmunity hoặc tissue damage. Goal là appropriate regulation.

### “Antibody giết mọi pathogen trực tiếp”

Antibody có nhiều mechanism và thường phối hợp với complement, phagocyte hoặc neutralization. Không phải mọi pathogen được xử lý cùng cách.

## Mental Model

> Nervous system truyền signal nhanh theo circuit; endocrine system broadcast chemical signal để điều chỉnh state; immune system thực hiện distributed recognition và defense. Cả ba dùng receptor, signaling, feedback và memory ở những dạng khác nhau.

File [[03_reproduction_and_development]] sẽ cho thấy signaling và gene regulation được dùng để xây cả organism từ một fertilized cell.