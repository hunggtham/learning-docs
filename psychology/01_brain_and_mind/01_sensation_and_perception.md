# Cảm giác và tri giác — Sensation & Perception / 감각과 지각

Thế giới vật lý không đi thẳng vào tâm trí như camera ghi hình. **Sensation (cảm giác / 감각)** là quá trình receptor chuyển energy vật lý thành neural signal; **perception (tri giác / 지각)** là quá trình hệ thần kinh tổ chức và diễn giải signal thành meaningful experience.

## Transduction: từ thế giới sang mã thần kinh

Ánh sáng là electromagnetic energy, âm thanh là pressure wave, mùi liên quan molecules. Receptor chuyên biệt thực hiện **transduction**. Brain không nhận “màu đỏ” hay “giọng nói”; nó nhận pattern activity. Perception xuất hiện khi system suy luận nguồn bên ngoài có khả năng tạo pattern đó.

**Absolute threshold** và **difference threshold** cho thấy detection là probabilistic chứ không phải ranh giới cứng. lý thuyết phát hiện tín hiệu (signal detection theory) tách sensitivity khỏi decision criterion: cùng sensory evidence nhưng một người có thể chọn criterion “cẩn thận” khác khi cost của miss cao. Đây là connection trực tiếp với fraud detection, medical screening và anomaly detection.

## Bottom-up và xử lý từ trên xuống (top-down processing)

**xử lý từ dưới lên (bottom-up processing)** bắt đầu từ sensory features; **xử lý từ trên xuống** dùng expectation, knowledge và context. Khi đọc một câu có chữ mờ, context giúp lấp missing information. Điều này thường hữu ích nhưng cũng tạo illusion và bias. Perception vì vậy gần với Bayesian inference: brain kết hợp likelihood từ sensory input với prior expectation để ước lượng nguyên nhân.

Ta không cần tin brain “thực hiện công thức Bayes” literal để dùng mô hình tư duy (mental model) này. Ý chính là perception là inference dưới uncertainty.

## Attention định hình cái được thấy

Inattentional blindness cho thấy object có thể ở ngay trước mắt nhưng không đi vào conscious report khi attention bị chiếm. Điều đó không có nghĩa eyes không nhận signal; processing bị giới hạn ở các tầng sau. Interface design, driving safety và alert systems đều phải tôn trọng attentional bottleneck.

## Gestalt và organization

Các nguyên lý proximity, similarity, continuity và closure mô tả xu hướng tổ chức visual elements thành wholes. Chúng không phải luật tuyệt đối; chúng cho thấy perception tối ưu hóa cấu trúc thay vì xử lý từng pixel độc lập. UI grouping trong design thực tế dựa rất nhiều vào cùng các nguyên tắc.

## những hiểu lầm phổ biến (common misconceptions)

“Ta nhìn thế giới đúng như nó vốn có” là sai vì perception luôn là reconstruction. Nhưng “mọi perception đều chủ quan nên không có reality” cũng sai. Sensory systems được constraint bởi physical input và được calibrate qua action; chúng có thể sai có hệ thống nhưng vẫn cực kỳ hiệu quả trong môi trường bình thường.


## Sensation và perception là hai tầng khác nhau của cùng một problem

**Sensation (cảm giác / 감각)** bắt đầu khi receptors transduce physical energy thành neural signals. **Perception (tri giác / 지각)** là process tổ chức và diễn giải signals đó thành meaningful objects/events. Retina nhận wavelength distribution; ta trải nghiệm “quả táo đỏ trên bàn”. Khoảng cách giữa hai description chứa rất nhiều computation.

Perception không phải camera. Sensory data luôn incomplete, noisy và ambiguous, nên brain kết hợp bottom-up evidence với prior knowledge/context để infer likely causes.

## Psychophysics: nối physical stimulus với subjective experience

Psychophysics nghiên cứu relation giữa stimulus magnitude và perception. **Absolute threshold** không phải fixed line; detection probabilistic và phụ thuộc attention/criterion. **Difference threshold — just noticeable difference** thường tăng theo baseline magnitude, intuition được capture bởi Weber's law trong ranges phù hợp.

Ví dụ, thêm 1 kg vào balo 2 kg dễ nhận hơn thêm 1 kg vào 30 kg. Đây là relative sensitivity, không phải sensor đọc absolute change.

## lý thuyết phát hiện tín hiệu

phát hiện tín hiệu (signal detection) tách sensory sensitivity `d'` khỏi response criterion. Hai người có same sensitivity nhưng một người conservative hơn khi nói “có signal”. Trong medical screening, radar và security alert, distinction này cực quan trọng.

Hits, misses, false alarms và correct rejections là four outcomes. Không thể reduce false alarms về zero mà không thường tăng misses nếu distributions overlap.

## Vision: từ feature tới object

Visual system xử lý contrast, edge, orientation, motion, depth và color qua distributed pathways. Popular diagram “mắt gửi ảnh lên brain” bỏ qua active processing từ retina trở đi.

**Gestalt principles** như proximity, similarity và closure mô tả tendencies grouping. Chúng không phải arbitrary aesthetic rules; chúng phản ánh how visual system infer object structure from fragmented input.

## Depth perception

Depth được infer từ binocular disparity, convergence và monocular cues như occlusion, perspective, texture gradient và motion parallax. Không cue nào luôn sufficient; system integrates multiple cues weighted by độ tin cậy (reliability).

Computer vision gặp problem tương tự: 2D pixels không trực tiếp chứa 3D world structure. Perception là inverse problem.

## Color perception

Color không phải property đơn giản “nằm trong object”. Surface reflectance, illumination và visual adaptation interact. **Color constancy** giúp object appear relatively stable dưới ánh sáng khác nhau, nhưng optical illusions cho thấy inference có thể fail khi context unusual.

## Audition và speech

Cochlea decomposes sound frequencies spatially; auditory system dùng timing/intensity differences giữa hai ears để localize. Speech perception thêm knowledge of language và context. Continuous speech waveform không có clear spaces như written text; listener segment stream bằng learned statistical/phonological cues.

## Multisensory integration

Perception kết hợp modalities. **McGurk effect** cho thấy visual mouth movement có thể thay heard syllable. Đây không phải “brain bị lừa” theo nghĩa defect; integration thường adaptive vì sources trong đời sống correlated.

## Pain như perception

Pain liên quan nociceptive signals nhưng không equal tissue damage meter. Attention, expectation, context và prior experience modulate pain. Điều này không có nghĩa pain “chỉ tâm lý”; pain là embodied perceptual experience với biological và psychological modulation.

## xử lý dự đoán (predictive processing) như một family of ideas

Một số modern theories mô tả brain như system continuously predicts sensory input và updates từ sai số dự đoán (prediction error). Đây là influential framework, nhưng không nên biến thành single settled theory giải thích mọi cognition. Useful intuition là perception depends on both evidence and expectations.

## những hiểu lầm phổ biến

### “Thấy bằng mắt, nghe bằng tai”

Eyes/ears transduce signals; perceptual experience được constructed bởi nervous system.

### “Optical illusion chứng minh mắt kém”

Illusion thường reveal assumptions normally useful trong natural environment.

### “Nếu hai người thấy khác nhau thì một người nói dối”

Ambiguous input, attention và prior knowledge có thể tạo genuine perceptual difference.

## kết nối kiến thức (knowledge connection)

Perception đặt nền cho [[02_consciousness_sleep_and_attention]], [[../02_learning_and_cognition/01_memory]] và [[../06_applied/02_hci_ai_and_human_decision_support]].


## Perceptual confidence: thấy rõ không đồng nghĩa đúng chắc

Perception không chỉ tạo estimate về world; brain còn tạo **confidence** về estimate đó. Đây là bridge giữa perception và **siêu nhận thức (metacognition)**. Hai người có thể cùng chọn đáp án đúng nhưng confidence khác, hoặc cùng confidence cao nhưng một người hiệu chỉnh (calibration) tốt hơn.

Trong đời sống, confidence của perception dễ bị nhầm với accuracy: `tôi thấy rõ ràng mà`. Eyewitness research cho thấy memory/perception chịu ảnh hưởng bởi attention, lighting, stress, suggestion và reconstruction. Subjective vividness không phải guarantee về fidelity.

## mù thay đổi (change blindness) và inattentional blindness

**Inattentional blindness** xảy ra khi salient event có thể không được consciously noticed nếu attention đang engaged ở task khác. **mù thay đổi** cho thấy người ta có thể bỏ qua thay đổi lớn khi visual continuity bị gián đoạn.

Các phenomenon này không chứng minh vision “tệ”; chúng cho thấy visual system ưu tiên task-relevant information thay vì xây full high-resolution copy của toàn scene. Đây là nguyên lý rất quan trọng trong UI design, driving và safety engineering.

Xem thêm: [[../06_applied/02_hci_ai_and_human_decision_support]], [[../06_applied/02_hci_ai_and_human_decision_support]].

## xử lý dự đoán: useful framework nhưng chưa phải một theory duy nhất đã đóng

Predictive-processing family mô tả perception như interaction giữa incoming sensory evidence và prior/model. Nhưng phrase `brain chỉ hallucinate reality` dễ gây hiểu sai. Sensory input vẫn constrain inference rất mạnh; prediction không cho phép tùy ý thấy bất cứ thứ gì.

Các version mã hóa dự đoán (predictive coding) khác nhau về computational details, neural implementation và phạm vi claim. Vì vậy nên dùng nó như framework giúp hỏi `prior nào đang hoạt động, error nào đang update model?`, không như slogan giải thích mọi phenomenon.

## kết nối kiến thức: perception → HCI → error prevention

Một interface an toàn không nên assume user sẽ thấy mọi warning. Nếu alert xuất hiện giữa visual clutter, giống màu background hoặc cần sustained attention, perceptual limitation trở thành system risk. yếu tố con người (human factors) vì thế dùng redundancy, salience, spacing, hierarchy và confirmation design để giảm dependence vào perfect attention.
