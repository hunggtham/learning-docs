# Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral Integration (감각, 운동과 행동 통합)

Một organism không chỉ phải giữ môi trường bên trong cơ thể (internal environment) ổn định. Nó còn phải liên tục trả lời ba câu hỏi: **điều gì đang xảy ra bên ngoài, cơ thể hiện đang ở trạng thái nào, và nên làm gì tiếp theo?** Nếu hệ thần kinh (nervous system) là mạng xử lý information còn muscle là hệ tạo force, thì sensory–motor integration là vòng lặp nối perception với action.

Hành vi vì vậy không nên được hình dung như chuỗi một chiều “stimulus vào não → brain ra lệnh → muscle làm theo”. Thực tế là một vòng kín (closed loop):

```text
environment + internal state
→ sensory transduction
→ neural encoding
→ integration + prediction
→ action selection
→ motor command
→ movement
→ sensory feedback
→ learning / updated state
```

> **Mô hình tư duy (mental model):** hệ thần kinh là một hệ điều khiển dựa trên thông tin không đầy đủ (incomplete information). Nó phải estimate state, dự đoán consequence, hành động trước khi mọi feedback quay về, rồi liên tục sửa prediction bằng tín hiệu sai số (error signal).

## 1. Thụ thể cảm giác (sensory receptor) không “nhận thế giới”; nó biến energy thành electrical signal

Môi trường không gửi khái niệm “ánh sáng”, “âm thanh” hay “mùi” vào brain. Nó gửi photon, sóng áp suất (pressure wave), chemical molecule, temperature change hoặc biến dạng cơ học (mechanical deformation).

**Chuyển đổi cảm giác (sensory transduction) (chuyển đổi cảm giác / 감각 변환)** là quá trình receptor biến năng lượng vật lý (physical energy) thành thay đổi độ dẫn ion (ion conductance) và điện thế màng (membrane potential). Photoreceptor thay đổi molecular conformation khi absorb photon. Mechanoreceptor mở channel khi membrane bị kéo. Chemoreceptor bind ligand và kích hoạt signaling cascade.

Điều này rất quan trọng về mặt nhận thức: hệ thần kinh không truy cập reality trực tiếp. Nó chỉ truy cập **tín hiệu (signal) được receptor cho phép đo**. Mỗi hệ cảm giác (sensory system) vì vậy giống một instrument có bandwidth, threshold và noise riêng.

## 2. Điện thế thụ thể (receptor potential) và điện thế hoạt động (action potential) đóng vai trò khác nhau

Thụ thể cảm giác thường tạo **điện thế thụ thể** dạng graded: stimulus mạnh hơn có thể tạo khử cực (depolarization) lớn hơn. Nhưng điện thế hoạt động của neuron gần all-or-none.

Vậy intensity được encode thế nào? Một mechanism phổ biến là **mã hóa bằng tần số (rate coding)**: điện thế thụ thể lớn hơn làm tần số phát xung (firing frequency) cao hơn. Ngoài ra, stimulus mạnh hơn có thể recruit thêm receptor hoặc neuron, tạo **mã hóa theo quần thể nơron (population coding)**.

Do đó information không nằm đơn giản ở “độ cao spike”, mà ở tần số (frequency), thời điểm (timing), synchrony và mẫu hình (pattern) qua mạng lưới (network).

## 3. Dải động (dynamic range) và logarithmic intuition

Hệ cảm giác thường phải xử lý stimulus thay đổi qua nhiều order of magnitude. Nếu response tăng tuyến tính vô hạn với intensity, neuron sẽ saturate rất nhanh.

Nhiều hệ cảm giác dùng compression: thay đổi relative ratio đôi khi quan trọng hơn absolute difference. Đây là intuition phía sau các psychophysical relation kiểu logarithmic trong một số phạm vi (range).

Điều này giải thích tại sao human hearing có thể xử lý sound intensity spanning range rất rộng, và vì sao decibel dùng logarithm thay vì scale tuyến tính đơn giản.

Connection với Mathematics ở đây là practical: logarithm nén dải động rất lớn thành scale xử lý được.

## 4. Thích nghi (adaptation): hệ thần kinh ưu tiên change hơn constant background

Nếu mặc áo, sau vài phút pressure của cloth gần như biến khỏi awareness. Nhiều receptor giảm response khi stimulus không đổi. Đây là **thích nghi cảm giác (sensory adaptation) (감각 적응)**.

Adaptation làm hệ thần kinh dành bandwidth cho change. Về signal processing, nó gần một high-pass behavior: constant background bị giảm trọng số, transition được làm nổi bật.

Nhưng adaptation rate khác nhau giữa receptor. Pain receptor thường duy trì response lâu hơn vì sustained tissue damage vẫn biologically relevant. Do đó “quen stimulus” không phải một property chung mà phụ thuộc function.

## 5. Trường tiếp nhận (receptive field): neuron không encode toàn world, nó encode một vùng và feature cụ thể

Một sensory neuron thường phản ứng mạnh với stimulus ở một subset của space gọi là **trường tiếp nhận (수용장)**. Trong retina, ganglion cell có center-surround organization: light ở center và surround có effect đối lập.

Điều này tạo **ức chế bên (lateral inhibition)**, làm edge và contrast nổi bật. Retina vì vậy không phải camera chỉ truyền pixel; nó thực hiện preprocessing trước khi signal lên cortex.

Một lesson lớn xuất hiện: perception là **feature extraction**, không phải photocopy của environment.

## 6. Vision: từ photon (photon) đến object representation là nhiều tầng abstraction

Photoreceptor chuyển photon thành electrical response. Retinal circuit tạo contrast. Visual pathway tiếp tục extract orientation, motion, depth và object-related feature qua nhiều level.

Không có một neuron đơn lẻ chứa “hình ảnh hoàn chỉnh”. Representation emerge từ distributed activity across network.

Điều này nối lại concept **emergence** ở [Cách tư duy trong Sinh học](../00_foundations/00_scientific_thinking_scale_and_models.md): higher-level perception không phải property của một molecule hay một neuron riêng lẻ, mà của network organization.

## 7. Hearing: physical frequency được map thành spatial organization

Sound wave làm tympanic membrane rung; ossicle truyền vibration vào cochlea. Basilar membrane có mechanical property thay đổi dọc chiều dài nên frequency khác nhau tạo maximal vibration ở region khác nhau.

Hair cell biến movement thành electrical signal. Vì vậy frequency được map thành location — **tonotopic organization (주파수 지형 조직)**.

Đây là cấu trúc (structure)–function rất đẹp: anatomy của cochlea thực hiện một dạng frequency decomposition trước khi higher neural circuit xử lý âm thanh (sound) mẫu hình (pattern).

## 8. Proprioception và vestibular signal: controller phải biết body state

Movement chính xác đòi hỏi biết không chỉ target mà cả current state. **Proprioception (cảm giác bản thể / 고유감각)** cung cấp information về muscle length, tension và joint position. Vestibular system cung cấp information về head motion và orientation relative gravity.

Nếu proprioception mất nhưng motor neuron vẫn khỏe, movement vẫn trở nên rất khó nếu không dùng vision để compensate. Điều này cho thấy force generation và ước lượng trạng thái (state estimation) là hai vấn đề khác nhau.

Trong lý thuyết điều khiển (control theory), controller không thể điều khiển một system tốt nếu không có feedback hoặc estimate về trạng thái (state).

## 9. Reflex: local control giảm latency

**Reflex arc (cung phản xạ / 반사궁)** cho phép response được tổ chức ở spinal hoặc brainstem circuit mà không chờ conscious processing.

Stretch reflex giúp ổn định muscle length. Khi muscle bị kéo, spindle tăng firing; sensory input kích hoạt motor response giúp chống lại stretch.

Reflex không có nghĩa brain hoàn toàn không tham gia. Higher center có thể modulate gain của reflex và nhận signal song song. Architecture này giống điều khiển phân tán (distributed control): local controller xử lý task nhanh, global controller điều chỉnh context.

## 10. Đơn vị vận động (motor unit) và nguyên lý recruitment

Một **đơn vị vận động (운동단위)** gồm một motor neuron và muscle fibers nó innervate. Fine-control muscle thường có đơn vị vận động nhỏ; large-force muscle có unit lớn hơn.

Force tăng qua recruitment thêm unit và tăng tần số phát xung. Small unit thường được recruit trước, rồi larger unit khi demand tăng — một nguyên lý giúp output tăng mượt và tiết kiệm energy.

Movement vì vậy không phải một command “co 40%”. Nó là quần thể (population) control của nhiều unit với timing khác nhau.

## 11. Neuromuscular junction nối information với mechanics

Điện thế hoạt động đến motor terminal mở voltage-gated Ca²⁺ channel, kích thích acetylcholine release. Acetylcholine depolarize muscle membrane. Signal lan theo T-tubule và làm sarcoplasmic reticulum release Ca²⁺. Ca²⁺ bind troponin, thay vị trí tropomyosin và cho phép actin–myosin cross-bridge cycling.

ATP được dùng trực tiếp trong myosin cycle.

```text
neural spike
→ Ca²⁺ signaling
→ protein conformational change
→ ATP hydrolysis
→ force
```

Đây là nơi dòng thông tin (information flow) và dòng năng lượng (energy flow) gặp nhau trong một mechanical output.

## 12. Lực–chiều dài (force–length) và lực–vận tốc (force–velocity): muscle không tạo lực giống nhau ở mọi trạng thái

Muscle force phụ thuộc overlap actin–myosin và contraction velocity. Ở sarcomere quá ngắn hoặc quá dài, cross-bridge geometry kém tối ưu. Khi shortening quá nhanh, force giảm vì ít thời gian hình thành cross-bridge hiệu quả.

Điều này giải thích vì sao body mechanics không thể hiểu chỉ từ “neuron firing mạnh hơn”. Output phụ thuộc current mechanical state của muscle.

Điều khiển vận động (motor control) phải xử lý một plant — theo ngôn ngữ control engineering — có property nonlinear và trạng thái-dependent.

## 13. Central Pattern Generator: rhythm có thể emerge từ mạng lưới

Walking, swimming và breathing có rhythmic pattern. Hệ thần kinh không cần phát một instruction riêng cho từng contraction.

**Central Pattern Generator, CPG (중추 패턴 발생기)** là neural circuit có thể tự tạo oscillatory pattern, sau đó được sensory feedback và higher center modulate.

CPG cho thấy network cấu trúc liên kết (topology) + màng (membrane) dynamics có thể tạo behavior periodic mà không cần “clock neuron” duy nhất điều khiển toàn bộ.

## 14. Feedforward và điều khiển phản hồi (feedback control) cùng tồn tại

Nếu controller chỉ chờ phản hồi (feedback) sau mỗi movement, response sẽ chậm. Brain vì vậy dùng cả **feedforward**: dự đoán command cần thiết dựa trên internal model và past experience.

Ví dụ khi nhấc một cup đã quen trọng lượng, grip force được chuẩn bị trước khi slip feedback xuất hiện. Nếu cup bất ngờ nhẹ hơn, movement ban đầu có thể overshoot, rồi sensory error giúp sửa ở lần sau.

Đây là core logic của motor learning:

```text
prediction
→ action
→ observed outcome
→ prediction error
→ update internal model
```

## 15. Cerebellum và error-based learning

Cerebellum đóng vai trò lớn trong thời điểm, coordination và hiệu chuẩn (calibration). Một mô hình tư duy hữu ích là nó hỗ trợ compare predicted consequence với sensory outcome rồi dùng error để điều chỉnh future command.

Damage cerebellum có thể làm movement vẫn có strength nhưng mất smooth coordination và độ chính xác (accuracy). Điều này cho thấy movement quality không chỉ phụ thuộc motor neuron và muscle, mà còn phụ thuộc computational correction.

## 16. Basal ganglia: không chỉ tạo movement mà còn chọn action

Organism thường có nhiều action possible cùng lúc. Basal ganglia tham gia **lựa chọn hành động (action selection)** và learning liên quan reward.

Dopamine signal trong nhiều context có thể được mô tả gần với **sai số dự đoán phần thưởng (reward prediction error)**: difference giữa outcome nhận được và kết quả (outcome) được kỳ vọng.

Một form đơn giản:

\[
\delta = r + \gamma V(s') - V(s)
\]

Trong đó \(r\) là reward hiện tại, \(V(s)\) là expected value của state, và \(\delta\) là sai số dự đoán (prediction error) dùng để update expectation. Đây là bridge tự nhiên giữa neuroscience và reinforcement learning trong AI.

Equation là mô hình (model), không phải claim rằng neuron “chạy đúng công thức” theo nghĩa literal; nó là cách formalize relationship giữa expectation, outcome và learning signal.

## 17. Perception cũng là inference dưới uncertainty

Sensory signal noisy và ambiguous. Một retinal image 2D có thể tương ứng nhiều scene 3D khác nhau. Âm thanh đến hai ear với timing/intensity khác nhau nhưng environment phức tạp.

Hệ thần kinh kết hợp current evidence với prior experience để estimate likely state. Đây là lý do **Bayesian intuition** hữu ích:

\[
P(H|D)\propto P(D|H)P(H)
\]

Ta không cần giả định brain tính Bayes equation explicit ở mọi task. Nhưng framework giúp hiểu perception như inference chứ không phải direct readout.

## 18. Learning thay đổi circuit ở nhiều scale

Habituation, sensitization, classical conditioning và operant conditioning không chỉ là label behavior. Chúng phản ánh change trong synaptic efficacy, receptor trafficking, truyền tín hiệu nội bào (intracellular signaling), biểu hiện gen (gene expression) và đôi khi structural remodeling của synapse.

Vì vậy learning là một cross-scale process:

```text
experience
→ neural activity pattern
→ synaptic / molecular change
→ circuit dynamics thay đổi
→ future behavior thay đổi
```

Một concept psychological có thể trace xuống sinh học tế bào (cell biology) mà không cần reduce toàn bộ psychology thành một molecule duy nhất.

## 19. Homeostasis và motivation: value phụ thuộc internal state

Food cue không có cùng “giá trị” khi satiated và hungry. Water cue khác khi dehydrated. Threat response khác khi stress axis đã active.

Internal state từ hypothalamic, endocrine và tín hiệu tự chủ (autonomic signal) điều chỉnh lựa chọn hành động. Vì vậy behavior là output của **external evidence × internal need × learned expectation**.

Đây là lý do hệ thần kinh, hệ nội tiết (endocrine system) và metabolism không thể học như ba module tách biệt.

## 20. Decision luôn có cost, delay và độ bất định (uncertainty)

Organism hiếm khi có đủ information hoàn hảo. Chờ thêm information có thể tăng accuracy nhưng mất time. Chạy trốn ngay giảm information gathering nhưng có thể cứu mạng.

Đây là trade-off giữa **speed–độ chính xác**, giữa exploration–exploitation và giữa immediate reward–future reward. Những trade-off này xuất hiện ở hành vi (behavior), đáp ứng miễn dịch (immune response) và evolutionary strategy.

Biology vì vậy thường không tạo “decision tối ưu tuyệt đối”, mà giải pháp (solution) đủ tốt dưới constraint năng lượng (energy), time và độ bất định.

## 21. Sinh thái học hành vi (behavioral ecology): hành vi có consequence về mức thích nghi sinh sản (fitness)

Foraging, mating, chăm sóc con non (parental care) và territorial behavior có cost–benefit. **Kiếm ăn tối ưu (optimal foraging) theory** dùng model để hỏi strategy nào có thể được selection favor khi energy gain, time cost và predation risk khác nhau.

Một mô hình tư duy đơn giản:

\[
Net\ Benefit = Năng lượng (energy)\ Gain - Năng lượng\ Cost - Nguy cơ (risk)\ Cost
\]

Animal không cần consciously solve equation. Selection có thể favor neural/behavioral mechanism tạo outcome tương tự trong relevant environment.

## 22. Social behavior và inclusive fitness

Cooperation có thể tồn tại dù actor chịu cost nếu recipient có shared genetic interest đủ lớn. Hamilton's rule:

\[
rB > C
\]

với \(r\) là relatedness, \(B\) benefit cho recipient và \(C\) cost cho actor.

Equation này là mô hình để suy luận kin selection, không phải explanation duy nhất của cooperation. Reciprocity, mutualism, group structure và repeated interaction cũng có thể tạo cooperative dynamics.

## 23. Tình huống phân tích (case study): bắt bóng như một problem control hoàn chỉnh

Khi bắt bóng, eye estimate trajectory; head/body movement thay visual input; brain predicts interception point; motor system điều chỉnh arm; proprioception cho biết limb state; grip force phải timed với contact.

Nếu chỉ “phản ứng sau khi thấy bóng tới tay”, latency sẽ quá lớn. System phải predict. Nếu chỉ predict mà không feedback, error tích lũy. Skill xuất hiện từ feedforward + phản hồi + repeated calibration.

Một hành vi tưởng đơn giản vì vậy tích hợp optics, neural coding, internal model, cơ học cơ (muscle mechanics) và learning.

## 24. Tình huống phân tích: pain là perception bảo vệ, không phải meter đo damage đơn giản

Nociceptor detect potentially damaging stimulus, nhưng trải nghiệm đau (pain experience) còn bị modulate bởi context, attention, expectation và descending pathway.

Điều này không có nghĩa pain “chỉ ở trong đầu”. Nó có nghĩa biological function của pain là guide protective behavior, không phải trực tiếp báo số lượng tissue damage theo thang tuyến tính.

Case này giúp tránh lỗi phổ biến khi đồng nhất receptor activity với conscious perception.

## 25. Các hiểu lầm phổ biến (common misconceptions)

“Brain gửi lệnh, muscle chỉ thực hiện” bỏ qua continuous sensory feedback và body mechanics.

“Reflex không liên quan brain” quá đơn giản; reflex có local circuit nhưng bị descending modulation và signal vẫn đi lên higher center.

“Gene quyết định behavior” sai ở mức hệ thống. Gen (gene) ảnh hưởng receptor, development và plasticity, nhưng behavior emerge từ gen × phát triển (development) × môi trường (environment) × current state × history learning.

“Perception là reality được copy vào brain” cũng sai. Hệ cảm giác transform và infer từ partial signal.

## 26. Mô hình tư duy tổng hợp

Toàn chapter có thể nén thành vòng lặp:

```text
environment + body state
→ receptor transduction
→ encoding
→ state estimation / prediction
→ action selection
→ motor command
→ force and movement
→ changed environment
→ sensory prediction error
→ learning
```

Vòng lặp này không dừng. Mỗi action thay world, world mới tạo sensory input mới. Behavior là dynamics của coupling organism–môi trường.

<!-- depth-audit-2026:predictive-control -->
## Sensory system ước lượng state chứ không sao chép thế giới

Receptor chỉ sample một phần tín hiệu và luôn có noise. Brain vì vậy phải kết hợp sensory evidence với context và prior experience để ước lượng nguyên nhân khả dĩ. Có thể mô tả trực giác này bằng Bayes:

\[
P(H\mid D)\propto P(D\mid H)P(H)
\]

Đây không có nghĩa neuron “chạy công thức Bayes” từng bước; nó là mô hình toán học cho nguyên lý rằng perception phụ thuộc cả evidence hiện tại lẫn expectation học được. Illusion hữu ích vì cho thấy inference có thể hợp lý theo statistics quen thuộc nhưng sai trong stimulus nhân tạo.

Motor control cũng cần prediction vì feedback có delay. Internal model ước lượng hậu quả command trước khi sensory feedback hoàn tất; error sau đó sửa command và cập nhật learning. Cerebellar learning, adaptation khi đeo prism hoặc điều chỉnh posture đều minh họa vòng `prediction → action → error → update`.

Đây là bridge trực tiếp sang Psychology và AI: perception có thể được xem như state estimation dưới uncertainty, còn behavior là policy dưới constraint. Nhưng biological system có embodiment, energy cost, development và evolutionary history mà model AI thuần dữ liệu không tự động có.

## 27. Bridge sang Ecology

Khi một organism chọn food, mate, shelter hoặc route di chuyển, decision đó thay survival và reproduction. Khi nhiều individual cùng ra decision, chúng tạo competition, sự phối hợp (cooperation), sự di chuyển (migration), vật săn mồi–con mồi (predator–prey) interaction và mating structure.

Vì vậy ecology không bắt đầu ở “environment bên ngoài organism”. Nó bắt đầu từ **nhiều closed-loop organism cùng hành động trong một shared environment**.

Xem tiếp [Quần thể, Quần xã và Hành vi](../05_ecology/00_population_community_and_behavior.md). Sinh thái học quần thể (population ecology) sẽ lấy output behavior của individual làm input cho động lực học (dynamics) ở scale lớn hơn.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Sinh sản và Phát triển](03_reproduction_and_development.md) · [Mục lục Biology](../README.md) · [Nguyên lý cơ thể người và quản lý sức khỏe →](05_human_body_principles_and_health_management.md)
