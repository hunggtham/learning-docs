# Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**. Route đi từ kích thích và transduction → mã hóa thần kinh → tích hợp trung ương → đáp ứng vận động, học tập và hành vi, để phân biệt năng lượng đầu vào với thông tin mà hệ thần kinh thực sự biểu diễn.

Một organism không chỉ phải giữ môi trường bên trong cơ thể (internal environment) ổn định. Nó còn phải liên tục trả lời ba câu hỏi: **điều gì đang xảy ra bên ngoài, cơ thể hiện đang ở trạng thái nào, và nên làm gì tiếp theo?** Nếu hệ thần kinh (nervous system) là mạng xử lý thông tin (information / 정보) còn muscle là hệ tạo force, thì sensory–motor tích hợp (integration / 통합) là vòng lặp nối perception với hành động (action / 동작).

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

> **mô hình tư duy (mental model / 사고 모델):** hệ thần kinh là một hệ điều khiển dựa trên thông tin không đầy đủ (incomplete information). Nó phải estimate trạng thái (state / 상태), dự đoán consequence, hành động trước khi mọi phản hồi (feedback / 피드백) quay về, rồi liên tục sửa prediction bằng tín hiệu sai số (error signal).

## 1. Thụ thể cảm giác (sensory receptor) không “nhận thế giới”; nó biến năng lượng (energy / 에너지) thành electrical tín hiệu (signal / 신호)

Môi trường không gửi khái niệm “ánh sáng”, “âm thanh” hay “mùi” vào brain. Nó gửi photon, sóng áp suất (pressure wave), chemical molecule, temperature thay đổi (change / 변경) hoặc biến dạng cơ học (mechanical deformation).

**Chuyển đổi cảm giác (sensory transduction) (chuyển đổi cảm giác / 감각 변환)** là quá trình receptor biến năng lượng vật lý (physical energy) thành thay đổi độ dẫn ion (ion conductance) và điện thế màng (membrane potential). Photoreceptor thay đổi molecular conformation khi absorb photon. Mechanoreceptor mở channel khi membrane bị kéo. Chemoreceptor bind ligand và kích hoạt signaling cascade.

Điều này rất quan trọng về mặt nhận thức: hệ thần kinh không truy cập reality trực tiếp. Nó chỉ truy cập **tín hiệu (signal / 신호) được receptor cho phép đo**. Mỗi hệ cảm giác (sensory system) vì vậy giống một instrument có bandwidth, threshold và noise riêng.

> **Chuyển mạch:** Sensory receptor transduces energy into signal; receptor potential grades input, action potential carries spikes, and dynamic range determines usable coding resolution.

## 2. Điện thế thụ thể (receptor potential) và điện thế hoạt động (action potential) đóng vai trò khác nhau

Thụ thể cảm giác thường tạo **điện thế thụ thể** dạng graded: stimulus mạnh hơn có thể tạo khử cực (depolarization) lớn hơn. Nhưng điện thế hoạt động của neuron gần all-or-none.

Vậy intensity được encode thế nào? Một cơ chế (mechanism / 메커니즘) phổ biến là **mã hóa bằng tần số (rate coding)**: điện thế thụ thể lớn hơn làm tần số phát xung (firing frequency) cao hơn. Ngoài ra, stimulus mạnh hơn có thể recruit thêm receptor hoặc neuron, tạo **mã hóa theo quần thể nơron (population coding)**.

Do đó thông tin (information / 정보) không nằm đơn giản ở “độ cao spike”, mà ở tần số (frequency), thời điểm (timing), synchrony và mẫu hình (pattern) qua mạng lưới (network).

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **3. Dải động (dynamic range) và logarithmic intuition** tiếp nhận điểm tựa từ **2. Điện thế thụ thể (receptor potential) và điện thế hoạt động (action potential) đóng vai trò khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Thích nghi (adaptation): hệ thần kinh ưu tiên thay đổi (change / 변경) hơn constant background** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Dải động (dynamic range) và logarithmic intuition

Hệ cảm giác thường phải xử lý stimulus thay đổi qua nhiều thứ tự (order / 순서) of magnitude. Nếu phản hồi (response / 응답) tăng tuyến tính vô hạn với intensity, neuron sẽ saturate rất nhanh.

Nhiều hệ cảm giác dùng compression: thay đổi relative ratio đôi khi quan trọng hơn absolute difference. Đây là intuition phía sau các psychophysical quan hệ (relation / 관계) kiểu logarithmic trong một số phạm vi (range / 범위).

Điều này giải thích tại sao human hearing có thể xử lý sound intensity spanning phạm vi (range / 범위) rất rộng, và vì sao decibel dùng logarithm thay vì quy mô (scale / 규모) tuyến tính đơn giản.

Liên kết (connection / 연결) với Mathematics ở đây là practical: logarithm nén dải động rất lớn thành quy mô (scale / 규모) xử lý được.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **4. Thích nghi (adaptation): hệ thần kinh ưu tiên thay đổi (change / 변경) hơn constant background** tiếp nhận điểm tựa từ **3. Dải động (dynamic range) và logarithmic intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Trường tiếp nhận (receptive field): neuron không encode toàn world, nó encode một vùng và tính năng (feature / 기능) cụ thể** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Thích nghi (adaptation): hệ thần kinh ưu tiên thay đổi (change / 변경) hơn constant background

Nếu mặc áo, sau vài phút pressure của cloth gần như biến khỏi awareness. Nhiều receptor giảm phản hồi (response / 응답) khi stimulus không đổi. Đây là **thích nghi cảm giác (sensory adaptation) (감각 적응)**.

Adaptation làm hệ thần kinh dành bandwidth cho thay đổi (change / 변경). Về tín hiệu (signal / 신호) processing, nó gần một high-pass hành vi (behavior / 동작): constant background bị giảm trọng số, chuyển tiếp (transition / 전이) được làm nổi bật.

Nhưng adaptation tỷ lệ (rate / 비율) khác nhau giữa receptor. Pain receptor thường duy trì phản hồi (response / 응답) lâu hơn vì sustained tissue damage vẫn biologically relevant. Do đó “quen stimulus” không phải một thuộc tính (property / 속성) chung mà phụ thuộc hàm (function / 함수).

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **5. Trường tiếp nhận (receptive field): neuron không encode toàn world, nó encode một vùng và tính năng (feature / 기능) cụ thể** tiếp nhận điểm tựa từ **4. Thích nghi (adaptation): hệ thần kinh ưu tiên thay đổi (change / 변경) hơn constant background** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Vision: từ photon (photon) đến biểu diễn đối tượng (object representation / 객체 표현) là nhiều tầng lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Trường tiếp nhận (receptive field): neuron không encode toàn world, nó encode một vùng và tính năng (feature / 기능) cụ thể

Một sensory neuron thường phản ứng mạnh với stimulus ở một subset của không gian (space / 공간) gọi là **trường tiếp nhận (수용장)**. Trong retina, ganglion cell có center-surround organization: light ở center và surround có tác động (effect / 효과) đối lập.

Điều này tạo **ức chế bên (lateral inhibition)**, làm edge và contrast nổi bật. Retina vì vậy không phải camera chỉ truyền điểm ảnh (pixel / 픽셀); nó thực hiện preprocessing trước khi tín hiệu (signal / 신호) lên cortex.

Một lesson lớn xuất hiện: perception là **tính năng (feature / 기능) extraction**, không phải photocopy của môi trường (environment / 환경).

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **6. Vision: từ photon (photon) đến biểu diễn đối tượng (object representation / 객체 표현) là nhiều tầng lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **5. Trường tiếp nhận (receptive field): neuron không encode toàn world, nó encode một vùng và tính năng (feature / 기능) cụ thể** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Hearing: vật lý (physical / 물리적) frequency được map thành spatial organization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Vision: từ photon (photon) đến biểu diễn đối tượng (object representation / 객체 표현) là nhiều tầng lớp trừu tượng (abstraction / 추상화)

Photoreceptor chuyển photon thành electrical phản hồi (response / 응답). Retinal circuit tạo contrast. Visual pathway tiếp tục extract orientation, motion, độ sâu (depth / 깊이) và object-related tính năng (feature / 기능) qua nhiều mức (level / 수준).

Không có một neuron đơn lẻ chứa “hình ảnh hoàn chỉnh”. biểu diễn (representation / 표현) emerge từ phân tán (distributed / 분산) activity across mạng (network / 네트워크).

Điều này nối lại concept **emergence** ở [Cách tư duy trong Sinh học](../00_foundations/00_scientific_thinking_scale_and_models.md): higher-level perception không phải thuộc tính (property / 속성) của một molecule hay một neuron riêng lẻ, mà của mạng (network / 네트워크) organization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **7. Hearing: vật lý (physical / 물리적) frequency được map thành spatial organization** tiếp nhận điểm tựa từ **6. Vision: từ photon (photon) đến biểu diễn đối tượng (object representation / 객체 표현) là nhiều tầng lớp trừu tượng (abstraction / 추상화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Proprioception và vestibular tín hiệu (signal / 신호): controller phải biết body trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Hearing: vật lý (physical / 물리적) frequency được map thành spatial organization

Sound wave làm tympanic membrane rung; ossicle truyền vibration vào cochlea. Basilar membrane có mechanical thuộc tính (property / 속성) thay đổi dọc chiều dài nên frequency khác nhau tạo maximal vibration ở region khác nhau.

Hair cell biến movement thành electrical tín hiệu (signal / 신호). Vì vậy frequency được map thành location — **tonotopic organization (주파수 지형 조직)**.

Đây là cấu trúc (structure / 구조)–hàm (function / 함수) rất đẹp: anatomy của cochlea thực hiện một dạng frequency decomposition trước khi higher neural circuit xử lý âm thanh (sound) mẫu hình (pattern).

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **8. Proprioception và vestibular tín hiệu (signal / 신호): controller phải biết body trạng thái (state / 상태)** tiếp nhận điểm tựa từ **7. Hearing: vật lý (physical / 물리적) frequency được map thành spatial organization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Reflex: cục bộ (local / 로컬) điều khiển (control / 제어) giảm độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Proprioception và vestibular tín hiệu (signal / 신호): controller phải biết body trạng thái (state / 상태)

Movement chính xác đòi hỏi biết không chỉ mục tiêu (target / 대상) mà cả trạng thái hiện tại (current state / 현재 상태). **Proprioception (cảm giác bản thể / 고유감각)** cung cấp thông tin (information / 정보) về muscle length, tension và joint position. Vestibular hệ thống (system / 시스템) cung cấp thông tin (information / 정보) về head motion và orientation relative gravity.

Nếu proprioception mất nhưng motor neuron vẫn khỏe, movement vẫn trở nên rất khó nếu không dùng vision để compensate. Điều này cho thấy force generation và ước lượng trạng thái (state estimation) là hai vấn đề khác nhau.

Trong lý thuyết điều khiển (control theory), controller không thể điều khiển một hệ thống (system / 시스템) tốt nếu không có phản hồi (feedback / 피드백) hoặc estimate về trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **9. Reflex: cục bộ (local / 로컬) điều khiển (control / 제어) giảm độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **8. Proprioception và vestibular tín hiệu (signal / 신호): controller phải biết body trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Đơn vị vận động (motor unit) và nguyên lý recruitment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Reflex: cục bộ (local / 로컬) điều khiển (control / 제어) giảm độ trễ (latency / 지연 시간)

**Reflex arc (cung phản xạ / 반사궁)** cho phép phản hồi (response / 응답) được tổ chức ở spinal hoặc brainstem circuit mà không chờ conscious processing.

Stretch reflex giúp ổn định muscle length. Khi muscle bị kéo, spindle tăng firing; sensory đầu vào (input / 입력) kích hoạt motor phản hồi (response / 응답) giúp chống lại stretch.

Reflex không có nghĩa brain hoàn toàn không tham gia. Higher center có thể modulate gain của reflex và nhận tín hiệu (signal / 신호) song song. kiến trúc (architecture / 아키텍처) này giống điều khiển phân tán (distributed control): cục bộ (local / 로컬) controller xử lý tác vụ (task / 작업) nhanh, toàn cục (global / 전역) controller điều chỉnh ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **10. Đơn vị vận động (motor unit) và nguyên lý recruitment** tiếp nhận điểm tựa từ **9. Reflex: cục bộ (local / 로컬) điều khiển (control / 제어) giảm độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Neuromuscular junction nối thông tin (information / 정보) với mechanics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Đơn vị vận động (motor unit) và nguyên lý recruitment

Một **đơn vị vận động (운동단위)** gồm một motor neuron và muscle fibers nó innervate. Fine-control muscle thường có đơn vị vận động nhỏ; large-force muscle có đơn vị (unit / 단위) lớn hơn.

Force tăng qua recruitment thêm đơn vị (unit / 단위) và tăng tần số phát xung. Small đơn vị (unit / 단위) thường được recruit trước, rồi larger đơn vị (unit / 단위) khi demand tăng — một nguyên lý giúp đầu ra (output / 출력) tăng mượt và tiết kiệm năng lượng (energy / 에너지).

Movement vì vậy không phải một command “co 40%”. Nó là quần thể (population) điều khiển (control / 제어) của nhiều đơn vị (unit / 단위) với timing khác nhau.

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **11. Neuromuscular junction nối thông tin (information / 정보) với mechanics** tiếp nhận điểm tựa từ **10. Đơn vị vận động (motor unit) và nguyên lý recruitment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Lực–chiều dài (force–length) và lực–vận tốc (force–velocity): muscle không tạo lực giống nhau ở mọi trạng thái** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Neuromuscular junction nối thông tin (information / 정보) với mechanics

Điện thế hoạt động đến motor terminal mở voltage-gated Ca²⁺ channel, kích thích acetylcholine bản phát hành (release / 릴리스). Acetylcholine depolarize muscle membrane. tín hiệu (signal / 신호) lan theo T-tubule và làm sarcoplasmic reticulum bản phát hành (release / 릴리스) Ca²⁺. Ca²⁺ bind troponin, thay vị trí tropomyosin và cho phép actin–myosin cross-bridge cycling.

ATP được dùng trực tiếp trong myosin cycle.

```text
neural spike
→ Ca²⁺ signaling
→ protein conformational change
→ ATP hydrolysis
→ force
```

Đây là nơi dòng thông tin (information flow) và dòng năng lượng (energy flow) gặp nhau trong một mechanical đầu ra (output / 출력).

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **12. Lực–chiều dài (force–length) và lực–vận tốc (force–velocity): muscle không tạo lực giống nhau ở mọi trạng thái** tiếp nhận điểm tựa từ **11. Neuromuscular junction nối thông tin (information / 정보) với mechanics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Central mẫu (pattern / 패턴) Generator: rhythm có thể emerge từ mạng lưới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Lực–chiều dài (force–length) và lực–vận tốc (force–velocity): muscle không tạo lực giống nhau ở mọi trạng thái

Muscle force phụ thuộc overlap actin–myosin và contraction velocity. Ở sarcomere quá ngắn hoặc quá dài, cross-bridge hình học (geometry / 기하학) kém tối ưu. Khi shortening quá nhanh, force giảm vì ít thời gian hình thành cross-bridge hiệu quả.

Điều này giải thích vì sao body mechanics không thể hiểu chỉ từ “neuron firing mạnh hơn”. đầu ra (output / 출력) phụ thuộc hiện tại (current / 현재) mechanical trạng thái (state / 상태) của muscle.

Điều khiển vận động (motor control) phải xử lý một plant — theo ngôn ngữ điều khiển (control / 제어) kỹ thuật (engineering / 엔지니어링) — có thuộc tính (property / 속성) nonlinear và trạng thái-dependent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **13. Central mẫu (pattern / 패턴) Generator: rhythm có thể emerge từ mạng lưới** tiếp nhận điểm tựa từ **12. Lực–chiều dài (force–length) và lực–vận tốc (force–velocity): muscle không tạo lực giống nhau ở mọi trạng thái** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Feedforward và điều khiển phản hồi (feedback control) cùng tồn tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Central mẫu (pattern / 패턴) Generator: rhythm có thể emerge từ mạng lưới

Walking, swimming và breathing có rhythmic mẫu (pattern / 패턴). Hệ thần kinh không cần phát một instruction riêng cho từng contraction.

**Central mẫu (pattern / 패턴) Generator, CPG (중추 패턴 발생기)** là neural circuit có thể tự tạo oscillatory mẫu (pattern / 패턴), sau đó được sensory phản hồi (feedback / 피드백) và higher center modulate.

CPG cho thấy mạng (network / 네트워크) cấu trúc liên kết (topology) + màng (membrane) dynamics có thể tạo hành vi (behavior / 동작) periodic mà không cần “clock neuron” duy nhất điều khiển toàn bộ.

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **14. Feedforward và điều khiển phản hồi (feedback control) cùng tồn tại** tiếp nhận điểm tựa từ **13. Central mẫu (pattern / 패턴) Generator: rhythm có thể emerge từ mạng lưới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Cerebellum và error-based học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Feedforward và điều khiển phản hồi (feedback control) cùng tồn tại

Nếu controller chỉ chờ phản hồi (feedback / 피드백) sau mỗi movement, phản hồi (response / 응답) sẽ chậm. Brain vì vậy dùng cả **feedforward**: dự đoán command cần thiết dựa trên nội bộ (internal / 내부) mô hình (model / 모델) và past experience.

Ví dụ khi nhấc một cup đã quen trọng lượng, grip force được chuẩn bị trước khi slip phản hồi (feedback / 피드백) xuất hiện. Nếu cup bất ngờ nhẹ hơn, movement ban đầu có thể overshoot, rồi sensory lỗi (error / 오류) giúp sửa ở lần sau.

Đây là cốt lõi (core / 핵심) lô-gic (logic / 논리) của motor học tập (learning / 학습):

```text
prediction
→ action
→ observed outcome
→ prediction error
→ update internal model
```

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **15. Cerebellum và error-based học tập (learning / 학습)** tiếp nhận điểm tựa từ **14. Feedforward và điều khiển phản hồi (feedback control) cùng tồn tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Basal ganglia: không chỉ tạo movement mà còn chọn hành động (action / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Cerebellum và error-based học tập (learning / 학습)

Cerebellum đóng vai trò lớn trong thời điểm, coordination và hiệu chuẩn (calibration). Một mô hình tư duy hữu ích là nó hỗ trợ compare predicted consequence với sensory kết quả (outcome / 결과) rồi dùng lỗi (error / 오류) để điều chỉnh future command.

Damage cerebellum có thể làm movement vẫn có strength nhưng mất smooth coordination và độ chính xác (accuracy). Điều này cho thấy movement chất lượng (quality / 품질) không chỉ phụ thuộc motor neuron và muscle, mà còn phụ thuộc computational correction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **16. Basal ganglia: không chỉ tạo movement mà còn chọn hành động (action / 동작)** tiếp nhận điểm tựa từ **15. Cerebellum và error-based học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Perception cũng là suy luận (inference / 추론) dưới bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Basal ganglia: không chỉ tạo movement mà còn chọn hành động (action / 동작)

Organism thường có nhiều hành động (action / 동작) possible cùng lúc. Basal ganglia tham gia **lựa chọn hành động (action selection)** và học tập (learning / 학습) liên quan reward.

Dopamine tín hiệu (signal / 신호) trong nhiều ngữ cảnh (context / 맥락) có thể được mô tả gần với **sai số dự đoán phần thưởng (reward prediction error)**: difference giữa kết quả (outcome / 결과) nhận được và kết quả (outcome / 결과) được kỳ vọng.

Một form đơn giản:

\[
\delta = r + \gamma V(s') - V(s)
\]

Trong đó \(r\) là reward hiện tại, \(V(s)\) là expected giá trị (value / 값) của trạng thái (state / 상태), và \(\delta\) là sai số dự đoán (prediction error) dùng để cập nhật (update / 업데이트) expectation. Đây là cầu nối (bridge / 브리지) tự nhiên giữa neuroscience và reinforcement học tập (learning / 학습) trong AI.

Equation là mô hình (model / 모델), không phải claim rằng neuron “chạy đúng công thức” theo nghĩa literal; nó là cách formalize relationship giữa expectation, kết quả (outcome / 결과) và học tập (learning / 학습) tín hiệu (signal / 신호).

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **17. Perception cũng là suy luận (inference / 추론) dưới bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **16. Basal ganglia: không chỉ tạo movement mà còn chọn hành động (action / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. học tập (learning / 학습) thay đổi circuit ở nhiều quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Perception cũng là suy luận (inference / 추론) dưới bất định (uncertainty / 불확실성)

Sensory tín hiệu (signal / 신호) noisy và ambiguous. Một retinal ảnh (image / 이미지) 2D có thể tương ứng nhiều scene 3D khác nhau. Âm thanh đến hai ear với timing/intensity khác nhau nhưng môi trường (environment / 환경) phức tạp.

Hệ thần kinh kết hợp hiện tại (current / 현재) bằng chứng (evidence / 증거) với prior experience để estimate likely trạng thái (state / 상태). Đây là lý do **Bayesian intuition** hữu ích:

\[
P(H|D)\propto P(D|H)P(H)
\]

Ta không cần giả định brain tính Bayes equation tường minh (explicit / 명시적) ở mọi tác vụ (task / 작업). Nhưng khung phần mềm (framework / 프레임워크) giúp hiểu perception như suy luận (inference / 추론) chứ không phải direct readout.

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **18. học tập (learning / 학습) thay đổi circuit ở nhiều quy mô (scale / 규모)** tiếp nhận điểm tựa từ **17. Perception cũng là suy luận (inference / 추론) dưới bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Homeostasis và motivation: giá trị (value / 값) phụ thuộc trạng thái nội bộ (internal state / 내부 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. học tập (learning / 학습) thay đổi circuit ở nhiều quy mô (scale / 규모)

Habituation, sensitization, classical conditioning và operant conditioning không chỉ là label hành vi (behavior / 동작). Chúng phản ánh thay đổi (change / 변경) trong synaptic efficacy, receptor trafficking, truyền tín hiệu nội bào (intracellular signaling), biểu hiện gen (gene expression) và đôi khi structural remodeling của synapse.

Vì vậy học tập (learning / 학습) là một cross-scale tiến trình (process / 프로세스):

```text
experience
→ neural activity pattern
→ synaptic / molecular change
→ circuit dynamics thay đổi
→ future behavior thay đổi
```

Một concept psychological có thể dấu vết (trace / 추적) xuống sinh học tế bào (cell biology) mà không cần reduce toàn bộ psychology thành một molecule duy nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **19. Homeostasis và motivation: giá trị (value / 값) phụ thuộc trạng thái nội bộ (internal state / 내부 상태)** tiếp nhận điểm tựa từ **18. học tập (learning / 학습) thay đổi circuit ở nhiều quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. quyết định (decision / 결정) luôn có chi phí (cost / 비용), delay và độ bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Homeostasis và motivation: giá trị (value / 값) phụ thuộc trạng thái nội bộ (internal state / 내부 상태)

Food cue không có cùng “giá trị” khi satiated và hungry. Water cue khác khi dehydrated. Threat phản hồi (response / 응답) khác khi stress axis đã active.

Trạng thái nội bộ (internal state / 내부 상태) từ hypothalamic, endocrine và tín hiệu tự chủ (autonomic signal) điều chỉnh lựa chọn hành động. Vì vậy hành vi (behavior / 동작) là đầu ra (output / 출력) của **bên ngoài (external / 외부) bằng chứng (evidence / 증거) × nội bộ (internal / 내부) need × learned expectation**.

Đây là lý do hệ thần kinh, hệ nội tiết (endocrine system) và metabolism không thể học như ba mô-đun (module / 모듈) tách biệt.

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **20. quyết định (decision / 결정) luôn có chi phí (cost / 비용), delay và độ bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **19. Homeostasis và motivation: giá trị (value / 값) phụ thuộc trạng thái nội bộ (internal state / 내부 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Sinh thái học hành vi (behavioral ecology): hành vi có consequence về mức thích nghi sinh sản (fitness)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. quyết định (decision / 결정) luôn có chi phí (cost / 비용), delay và độ bất định (uncertainty / 불확실성)

Organism hiếm khi có đủ thông tin (information / 정보) hoàn hảo. Chờ thêm thông tin (information / 정보) có thể tăng accuracy nhưng mất thời gian (time / 시간). Chạy trốn ngay giảm thông tin (information / 정보) gathering nhưng có thể cứu mạng.

Đây là sự đánh đổi (trade-off / 트레이드오프) giữa **speed–độ chính xác**, giữa exploration–exploitation và giữa immediate reward–future reward. Những sự đánh đổi (trade-off / 트레이드오프) này xuất hiện ở hành vi (behavior / 동작), đáp ứng miễn dịch (immune response) và evolutionary chiến lược (strategy / 전략).

Biology vì vậy thường không tạo “quyết định (decision / 결정) tối ưu tuyệt đối”, mà giải pháp (solution) đủ tốt dưới ràng buộc (constraint / 제약조건) năng lượng (energy / 에너지), thời gian (time / 시간) và độ bất định.

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **21. Sinh thái học hành vi (behavioral ecology): hành vi có consequence về mức thích nghi sinh sản (fitness)** tiếp nhận điểm tựa từ **20. quyết định (decision / 결정) luôn có chi phí (cost / 비용), delay và độ bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. xã hội (social / 사회적) hành vi (behavior / 동작) và inclusive fitness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Sinh thái học hành vi (behavioral ecology): hành vi có consequence về mức thích nghi sinh sản (fitness)

Foraging, mating, chăm sóc con non (parental care) và territorial hành vi (behavior / 동작) có chi phí (cost / 비용)–benefit. **Kiếm ăn tối ưu (optimal foraging) lý thuyết (theory / 이론)** dùng mô hình (model / 모델) để hỏi chiến lược (strategy / 전략) nào có thể được selection favor khi năng lượng (energy / 에너지) gain, thời gian (time / 시간) chi phí (cost / 비용) và predation rủi ro (risk / 위험) khác nhau.

Một mô hình tư duy đơn giản:

\[
Net\ Benefit = năng lượng (energy / 에너지)\ Gain - Năng lượng\ chi phí (cost / 비용) - Nguy cơ (risk)\ chi phí (cost / 비용)
\]

Animal không cần consciously solve equation. Selection có thể favor neural/behavioral cơ chế (mechanism / 메커니즘) tạo kết quả (outcome / 결과) tương tự trong relevant môi trường (environment / 환경).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **22. xã hội (social / 사회적) hành vi (behavior / 동작) và inclusive fitness** tiếp nhận điểm tựa từ **21. Sinh thái học hành vi (behavioral ecology): hành vi có consequence về mức thích nghi sinh sản (fitness)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Tình huống phân tích (case study): bắt bóng như một bài toán (problem / 문제) điều khiển (control / 제어) hoàn chỉnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. xã hội (social / 사회적) hành vi (behavior / 동작) và inclusive fitness

Cooperation có thể tồn tại dù actor chịu chi phí (cost / 비용) nếu recipient có dùng chung (shared / 공유) genetic interest đủ lớn. Hamilton's quy tắc (rule / 규칙):

\[
rB > C
\]

với \(r\) là relatedness, \(B\) benefit cho recipient và \(C\) chi phí (cost / 비용) cho actor.

Equation này là mô hình để suy luận kin selection, không phải explanation duy nhất của cooperation. Reciprocity, mutualism, group cấu trúc (structure / 구조) và repeated tương tác (interaction / 상호작용) cũng có thể tạo cooperative dynamics.

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **22. xã hội (social / 사회적) hành vi (behavior / 동작) và inclusive fitness** cho ta quy tắc; **23. Tình huống phân tích (case study): bắt bóng như một bài toán (problem / 문제) điều khiển (control / 제어) hoàn chỉnh** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **24. Tình huống phân tích: pain là perception bảo vệ, không phải meter đo damage đơn giản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Tình huống phân tích (case study): bắt bóng như một bài toán (problem / 문제) điều khiển (control / 제어) hoàn chỉnh

Khi bắt bóng, eye estimate trajectory; head/body movement thay visual đầu vào (input / 입력); brain predicts interception điểm (point / 지점); motor hệ thống (system / 시스템) điều chỉnh arm; proprioception cho biết limb trạng thái (state / 상태); grip force phải timed với contact.

Nếu chỉ “phản ứng sau khi thấy bóng tới tay”, độ trễ (latency / 지연 시간) sẽ quá lớn. hệ thống (system / 시스템) phải predict. Nếu chỉ predict mà không phản hồi (feedback / 피드백), lỗi (error / 오류) tích lũy. Skill xuất hiện từ feedforward + phản hồi + repeated calibration.

Một hành vi tưởng đơn giản vì vậy tích hợp optics, neural coding, nội bộ (internal / 내부) mô hình (model / 모델), cơ học cơ (muscle mechanics) và học tập (learning / 학습).

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **23. Tình huống phân tích (case study): bắt bóng như một bài toán (problem / 문제) điều khiển (control / 제어) hoàn chỉnh** cho ta quy tắc; **24. Tình huống phân tích: pain là perception bảo vệ, không phải meter đo damage đơn giản** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **25. Các hiểu lầm phổ biến (common misconceptions)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Tình huống phân tích: pain là perception bảo vệ, không phải meter đo damage đơn giản

Nociceptor detect potentially damaging stimulus, nhưng trải nghiệm đau (pain experience) còn bị modulate bởi ngữ cảnh (context / 맥락), attention, expectation và descending pathway.

Điều này không có nghĩa pain “chỉ ở trong đầu”. Nó có nghĩa biological hàm (function / 함수) của pain là guide protective hành vi (behavior / 동작), không phải trực tiếp báo số lượng tissue damage theo thang tuyến tính.

Trường hợp (case / 사례) này giúp tránh lỗi phổ biến khi đồng nhất receptor activity với conscious perception.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **24. Tình huống phân tích: pain là perception bảo vệ, không phải meter đo damage đơn giản** cho ta quy tắc; **25. Các hiểu lầm phổ biến (common misconceptions)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **26. Mô hình tư duy tổng hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Các hiểu lầm phổ biến (common misconceptions)

“Brain gửi lệnh, muscle chỉ thực hiện” bỏ qua continuous sensory phản hồi (feedback / 피드백) và body mechanics.

“Reflex không liên quan brain” quá đơn giản; reflex có cục bộ (local / 로컬) circuit nhưng bị descending modulation và tín hiệu (signal / 신호) vẫn đi lên higher center.

“Gene quyết định hành vi (behavior / 동작)” sai ở mức hệ thống. Gen (gene) ảnh hưởng receptor, development và plasticity, nhưng hành vi (behavior / 동작) emerge từ gen × phát triển (development) × môi trường (environment / 환경) × trạng thái hiện tại (current state / 현재 상태) × lịch sử (history / 이력) học tập (learning / 학습).

“Perception là reality được bản sao (copy / 복사) vào brain” cũng sai. Hệ cảm giác transform và infer từ partial tín hiệu (signal / 신호).

> **Chuyển mạch:** Trong **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **26. Mô hình tư duy tổng hợp** gom các mảnh từ **25. Các hiểu lầm phổ biến (common misconceptions)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Sensory hệ thống (system / 시스템) ước lượng trạng thái (state / 상태) chứ không sao chép thế giới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Vòng lặp này không dừng. Mỗi hành động (action / 동작) thay world, world mới tạo sensory đầu vào (input / 입력) mới. hành vi (behavior / 동작) là dynamics của coupling organism–môi trường.

<!-- depth-audit-2026:predictive-control -->

> **Chuyển mạch:** Ở chặng này của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **Sensory hệ thống (system / 시스템) ước lượng trạng thái (state / 상태) chứ không sao chép thế giới** gom các mảnh từ **26. Mô hình tư duy tổng hợp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **27. cầu nối (bridge / 브리지) sang Ecology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sensory hệ thống (system / 시스템) ước lượng trạng thái (state / 상태) chứ không sao chép thế giới

Receptor chỉ mẫu (sample / 표본) một phần tín hiệu và luôn có noise. Brain vì vậy phải kết hợp sensory bằng chứng (evidence / 증거) với ngữ cảnh (context / 맥락) và prior experience để ước lượng nguyên nhân khả dĩ. Có thể mô tả trực giác này bằng Bayes:

\[
P(H\mid D)\propto P(D\mid H)P(H)
\]

Đây không có nghĩa neuron “chạy công thức Bayes” từng bước; nó là mô hình toán học cho nguyên lý rằng perception phụ thuộc cả bằng chứng (evidence / 증거) hiện tại lẫn expectation học được. Illusion hữu ích vì cho thấy suy luận (inference / 추론) có thể hợp lý theo statistics quen thuộc nhưng sai trong stimulus nhân tạo.

Motor điều khiển (control / 제어) cũng cần prediction vì phản hồi (feedback / 피드백) có delay. nội bộ (internal / 내부) mô hình (model / 모델) ước lượng hậu quả command trước khi sensory phản hồi (feedback / 피드백) hoàn tất; lỗi (error / 오류) sau đó sửa command và cập nhật học tập (learning / 학습). Cerebellar học tập (learning / 학습), adaptation khi đeo prism hoặc điều chỉnh posture đều minh họa vòng `prediction → action → error → update`.

Đây là cầu nối (bridge / 브리지) trực tiếp sang Psychology và AI: perception có thể được xem như trạng thái (state / 상태) estimation dưới bất định (uncertainty / 불확실성), còn hành vi (behavior / 동작) là chính sách (policy / 정책) dưới ràng buộc (constraint / 제약조건). Nhưng biological hệ thống (system / 시스템) có embodiment, năng lượng (energy / 에너지) chi phí (cost / 비용), development và evolutionary lịch sử (history / 이력) mà mô hình (model / 모델) AI thuần dữ liệu không tự động có.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tích hợp cảm giác, vận động và hành vi — Sensory, Motor and Behavioral tích hợp (integration / 통합)**, **27. cầu nối (bridge / 브리지) sang Ecology** tiếp nhận điểm tựa từ **Sensory hệ thống (system / 시스템) ước lượng trạng thái (state / 상태) chứ không sao chép thế giới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 27. cầu nối (bridge / 브리지) sang Ecology

Khi một organism chọn food, mate, shelter hoặc tuyến (route / 경로) di chuyển, quyết định (decision / 결정) đó thay survival và reproduction. Khi nhiều individual cùng ra quyết định (decision / 결정), chúng tạo competition, sự phối hợp (cooperation), sự di chuyển (migration / 마이그레이션), vật săn mồi–con mồi (predator–prey) tương tác (interaction / 상호작용) và mating cấu trúc (structure / 구조).

Vì vậy ecology không bắt đầu ở “môi trường (environment / 환경) bên ngoài organism”. Nó bắt đầu từ **nhiều closed-loop organism cùng hành động trong một dùng chung (shared / 공유) môi trường (environment / 환경)**.

Xem tiếp [Quần thể, Quần xã và Hành vi](../05_ecology/00_population_community_and_behavior.md). Sinh thái học quần thể (population ecology) sẽ lấy đầu ra (output / 출력) hành vi (behavior / 동작) của individual làm đầu vào (input / 입력) cho động lực học (dynamics) ở quy mô (scale / 규모) lớn hơn.

---

<!-- biology-learning-navigation -->
**Điều hướng học:** [← Sinh sản và Phát triển](03_reproduction_and_development.md) · [Mục lục Biology](../README.md) · [Nguyên lý cơ thể người và quản lý sức khỏe →](05_human_body_principles_and_health_management.md)

> **Bàn giao:** Sau **27. cầu nối (bridge / 브리지) sang Ecology**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
