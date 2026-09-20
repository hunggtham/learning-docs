# Hệ thần kinh, nội tiết và miễn dịch — Nervous, Endocrine and Immune Systems (신경계, 내분비계와 면역계)

Animal physiology vừa cho thấy toàn cơ thể phải liên tục điều chỉnh blood pressure, glucose, temperature, water balance và nhiều variable khác. Nhưng regulation không thể xảy ra nếu các tissue hoạt động độc lập. Cơ thể cần những hệ thống communication có tốc độ, phạm vi và logic khác nhau.

Ba network lớn là nervous system, endocrine system và immune system. Chúng thường được học thành ba chương riêng, nhưng trong cơ thể thật chúng cross-talk liên tục. Stress signal từ brain đổi hormone; hormone đổi immune state; cytokine từ immune cell ảnh hưởng brain và behavior. Chương này vì thế tập trung vào **communication architecture** chung trước khi đi vào từng hệ.

## 1. Communication cần sender, signal, receiver và response

Một signal chỉ có meaning khi receiver có receptor phù hợp.

Ta có generic pattern:

```text
sender
  ↓ releases
signal
  ↓ reaches
receptor-bearing target
  ↓
transduction
  ↓
response
```

Nervous system dùng electrical signal dọc neuron và neurotransmitter ở synapse. Endocrine system dùng hormone trong blood. Immune system dùng cytokine, receptor và cell-cell contact.

Khác nhau về medium, nhưng logic molecular tương tự cell signaling đã học.

## 2. Neuron: cell chuyên hóa cho truyền tín hiệu nhanh

**Neuron (뉴런)** có dendrite nhận input, cell body tích hợp signal và axon truyền output xa.

Long axon giải quyết spatial problem: signal không cần diffusion chậm qua toàn tissue.

Neuron dùng membrane potential — concept đã xây ở cell biology — để truyền information.

## 3. Resting membrane potential: nền điện của neuron

Neuron giữ Na⁺, K⁺ và các ion khác phân bố không đều hai bên membrane. Na⁺/K⁺ ATPase duy trì gradient lâu dài; ion channel quyết định permeability tức thời.

Resting membrane potential thường negative bên trong.

Điều này không phải “cell chứa điện” kiểu battery đơn giản. Nó là state xuất hiện từ ion gradient + selective permeability.

Metabolism cung cấp ATP để pump gradient; membrane biến gradient thành electrical potential. Một concept từ ba chapter trước bây giờ trở thành nervous function.

## 4. Action potential: positive feedback tạo signal all-or-none

Khi membrane depolarize tới threshold, voltage-gated Na⁺ channel mở. Na⁺ vào làm depolarization mạnh hơn, mở thêm channel — một positive feedback.

Sau đó Na⁺ channel inactivate và K⁺ channel mở, K⁺ ra ngoài, membrane repolarize.

```text
small depolarization
   ↓ threshold
Na+ channels open
   ↓
more depolarization
   ↓
more Na+ channels open
   ↓
rapid spike
```

Refractory period giúp action potential đi một chiều và giới hạn firing rate.

Action potential là ví dụ perfect của dynamical switch tạo từ membrane biophysics.

## 5. Myelin: tăng tốc bằng cách thay geometry của membrane

Myelin cách điện các đoạn axon. Action potential được regenerate chủ yếu ở node of Ranvier.

Signal vì thế “nhảy” theo saltatory conduction, nhanh và energy-efficient hơn conduction liên tục.

Structure–function principle lại xuất hiện: thay architecture membrane đổi communication speed.

## 6. Synapse: electrical signal trở lại chemical signal

Khi action potential tới axon terminal, voltage-gated Ca²⁺ channel mở. Ca²⁺ influx trigger vesicle fusion và neurotransmitter release.

Neurotransmitter diffuse qua synaptic cleft và bind receptor trên target cell.

Một synapse nối nhiều concept:

```text
action potential
 ↓
Ca2+ gradient
 ↓
vesicle exocytosis
 ↓
neurotransmitter diffusion
 ↓
receptor signaling
 ↓
postsynaptic response
```

Membrane transport, gradient, signaling và cytoskeleton đều gặp lại ở đây.

## 7. Neural circuit: behavior xuất hiện từ network

Một neuron đơn không tạo perception hay behavior phức tạp. Circuit gồm nhiều excitatory/inhibitory connection tích hợp input.

Network architecture ảnh hưởng output. Synaptic strength có thể thay đổi qua plasticity, tạo nền cho learning và memory.

Đây là emergence ở nervous-system scale.

## 8. Endocrine system: communication chậm hơn nhưng broadcast rộng

**Hormone (호르몬)** được secreted vào blood và có thể đi khắp body.

Nhưng chỉ target có receptor phù hợp phản ứng.

Peptide hormone thường bind membrane receptor. Steroid hormone lipid-soluble có thể vào cell và bind intracellular receptor.

Chemistry của hormone quyết định route signaling — cùng principle từ molecular chapter.

## 9. Hormone axis và negative feedback

Nhiều endocrine system tổ chức thành axis.

Ví dụ hypothalamus → pituitary → peripheral gland. Hormone cuối thường feedback lên upstream center.

```text
hypothalamus
   ↓ releasing hormone
pituitary
   ↓ tropic hormone
endocrine gland
   ↓ final hormone
body tissues
   ↖ negative feedback
```

Cấu trúc nhiều tầng cho phép amplification và multiple control point.

## 10. Insulin–glucagon: endocrine regulation của metabolism

Sau meal, blood glucose tăng. Insulin tăng uptake/storage glucose và anabolic process.

Trong fasting, glucagon thúc đẩy liver release glucose và huy động energy store.

Hai hormone không đơn giản “một tăng, một giảm”; chúng coordinate whole-body fuel distribution theo nutritional state.

Cellular metabolism ở chapter trước được điều khiển bởi organism-level endocrine signal.

## 11. Stress response: nervous và endocrine system phối hợp

Acute threat activate sympathetic nervous system nhanh. Adrenal medulla release catecholamine, tăng heart rate và mobilize fuel.

Longer stress response có thể liên quan hypothalamic–pituitary–adrenal axis và cortisol.

Cùng một event environment được xử lý ở nhiều time scale.

## 12. Immune system: bài toán self, non-self và damage

Immune system không chỉ “diệt vi khuẩn”. Nó phải phát hiện threat, phân biệt context, loại pathogen nhưng hạn chế damage cho host, và đôi khi tạo memory.

Đây là classification/control problem cực khó vì pathogen evolution liên tục thay đổi target.

## 13. Innate immunity: response nhanh dựa trên pattern

**Innate immunity (miễn dịch bẩm sinh / 선천면역)** dùng barrier, phagocyte, complement và receptor nhận các pattern phổ biến liên quan pathogen hoặc tissue damage.

Response nhanh vì receptor đã được encoded sẵn trong germline.

Nhưng specificity hạn chế hơn adaptive immunity.

## 14. Inflammation: defense có cost

Injury hoặc infection làm cell release mediator, tăng blood flow và vascular permeability, recruit immune cell.

Inflammation giúp đưa defense tới site nhưng cũng có thể gây tissue damage nếu quá mạnh hoặc kéo dài.

Đây là trade-off: defense mạnh có benefit nhưng không miễn phí.

## 15. Adaptive immunity: tạo specificity bằng receptor diversity

B cell và T cell có receptor diversity khổng lồ được tạo qua gene rearrangement.

Khi clone có receptor phù hợp antigen được activate, clone expand.

Ta có selection process ở cell population:

```text
many lymphocyte clones
      ↓ antigen exposure
matching clone activated
      ↓
clonal expansion
      ↓
effector + memory cells
```

Logic này giống evolution theo nghĩa selection among variants, nhưng diễn ra trong immune repertoire của một organism.

## 16. Antibody: structure quyết định specificity

Antibody có variable region bind antigen và constant region recruit effector function.

Binding phụ thuộc shape/charge complementarity, quay lại protein structure–function.

Class switching có thể giữ antigen specificity nhưng đổi constant region, làm effector function khác.

## 17. T cell: nhận antigen qua context của host cell

T cell thường không bind free antigen như antibody. Chúng nhận peptide được trình bày trên MHC molecule.

Điều này cho immune system biết cả identity antigen và context cell presenting it.

Cytotoxic T cell có thể kill infected cell; helper T cell coordinate response qua cytokine.

## 18. Immune memory và vaccine

Sau primary response, một số memory cell tồn tại. Khi gặp antigen tương tự, response thường nhanh và mạnh hơn.

Vaccination khai thác principle này bằng cách expose immune system tới antigen hoặc instruction tạo antigen trong condition controlled.

Vaccine không “tăng immunity chung”; nó train adaptive memory đối với target cụ thể.

## 19. Autoimmunity, allergy và immunodeficiency: regulation failure theo ba hướng

Autoimmunity: response hướng vào self component.

Allergy: response mạnh với antigen thường ít nguy hiểm.

Immunodeficiency: defense không đủ.

Ba case cho thấy immune system không chỉ cần power; nó cần calibration.

## 20. Neuro–endocrine–immune cross-talk

Cortisol có thể suppress nhiều immune response. Cytokine trong infection có thể tạo fever, fatigue và behavior change qua brain. Autonomic nerve ảnh hưởng organ immune environment.

Do đó ba system tạo một integrated regulatory network.

Cơ thể không có “module thần kinh” hoạt động độc lập “module miễn dịch”.

## 21. Từ regulation sang reproduction và development

Nervous/endocrine system cũng điều khiển reproductive physiology. Immune tolerance thay đổi trong pregnancy. Hormone và gene regulation điều khiển puberty, gamete maturation và development.

Câu hỏi kế tiếp là một trong những câu hỏi lớn nhất Sinh học:

**Từ một fertilized cell chứa một genome, làm thế nào organism tạo ra hàng trăm cell type, body axis và organ có cấu trúc khác nhau?**

Tiếp tục với [[03_reproduction_and_development]].