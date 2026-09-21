# Dữ liệu Tổng hợp

**Dữ liệu tổng hợp (synthetic data / 합성 데이터)** là dữ liệu được tạo bởi simulator, rule hoặc generative model thay vì thu trực tiếp từ hiện tượng thật. Nó hữu ích để tăng coverage, hỗ trợ privacy, tạo rare scenario hoặc bootstrap label, nhưng không phải “dữ liệu miễn phí” vì synthetic data luôn kế thừa assumption và bias của generator.

## Các nguồn Synthetic Data

```text
rule-based generation
simulation / digital twin
generative model
text do LLM tạo
ảnh render
procedural environment
counterfactual transformation
```

Mỗi nguồn có mức fidelity và failure mode khác nhau.

## Simulation

Trong Robotics hoặc Autonomous Driving, simulator có thể tạo gần như không giới hạn trajectory, image và sensor data.

Ưu điểm:

- label có thể chính xác theo simulator state;
- rare hoặc dangerous case rẻ hơn nhiều để tạo;
- kiểm soát đầy đủ condition.

Nhược điểm lớn nhất là **khoảng cách mô phỏng–thực tế (sim-to-real gap)**. Renderer, physics engine hoặc sensor model không hoàn hảo nên distribution vẫn lệch production.

## Domain Randomization

**Domain randomization** thay đổi ngẫu nhiên texture, lighting, camera hoặc physics parameter để buộc model học structure bền vững hơn thay vì overfit vào một simulator cụ thể.

Mục tiêu không nhất thiết là làm simulation photorealistic nhất, mà là bao phủ đủ variation để model generalize sang real domain.

## Synthetic Data từ Generative Model

Diffusion model hoặc LLM có thể tạo example mới. Một số use case:

- augment rare class;
- tạo instruction–response pair;
- tạo paraphrase;
- mô phỏng edge case;
- tạo sample có cấu trúc gần giống dữ liệu thật.

Tuy nhiên generated data luôn phản ánh training distribution của generator.

## Self-Instruct và Synthetic Instruction

LLM có thể tự tạo task rồi tự tạo answer để scale instruction-tuning data.

Pipeline điển hình:

```text
seed task
→ sinh candidate instruction
→ lọc / deduplicate
→ sinh response
→ quality judge / human audit một phần
```

Rủi ro là error có thể tích lũy, và model family có thể truyền lại chính blind spot của nó cho student model.

## Teacher–Student Distillation

Một model mạnh đóng vai teacher có thể tạo label hoặc response cho model nhỏ hơn.

Student học xấp xỉ behavior của teacher, không phải tự động học ground truth tuyệt đối. Chất lượng cuối cùng bị giới hạn bởi teacher và filtering pipeline.

## Sinh Rare Event

Fraud, failure hoặc incident nghiêm trọng thường hiếm. Synthetic generation có thể tăng coverage nhưng nếu rare case được tạo quá phi thực tế, model sẽ học artifact phân biệt “synthetic” và “real” thay vì học phenomenon thật.

Cần đánh giá realism và luôn giữ real validation data làm mốc.

## Động cơ Privacy

Synthetic record có thể giảm việc expose trực tiếp record thật, nhưng privacy không tự động được bảo đảm.

Generator vẫn có thể memorize và reproduce training sample. Nếu privacy là yêu cầu nghiêm ngặt, cần attack test hoặc formal mechanism như **Differential Privacy (DP)**.

## Liên hệ với Differential Privacy

DP training giới hạn ảnh hưởng của từng training record lên model. Synthetic data sinh từ model được train bằng DP có thể kế thừa một số guarantee chính thức dưới các assumption nhất định.

Ordinary synthetic data không có guarantee này chỉ vì nó “không phải raw record”.

## Statistical Fidelity

Với tabular synthetic data, nên so sánh:

- marginal distribution;
- correlation;
- conditional distribution;
- rare-category frequency;
- temporal pattern;
- downstream model utility.

Khớp histogram đơn giản không chứng minh joint distribution đã đúng.

## Utility Evaluation

Một cách đánh giá thực dụng là **Train Synthetic, Test Real (TSTR)**:

```text
train trên synthetic data
→ test trên real holdout
```

Cách này kiểm tra synthetic data có giữ được task-relevant structure hay không.

Nên đồng thời so sánh model train trên real-only với model train trên real + synthetic.

## Diversity

Generator có thể bị mode collapse hoặc tạo nhiều near-duplicate.

Khi đó số lượng sample lớn chỉ làm tăng row count chứ không tăng effective diversity. Cần deduplication và diversity metric.

## Tỷ lệ Synthetic-to-Real

Dùng quá nhiều synthetic data có thể kéo model về artifact của generator.

Không có tỷ lệ universal. Nên chọn dựa trên real validation performance và theo dõi domain shift giữa synthetic với real data.

## Distribution Steering

Synthetic generator có thể cố ý tăng coverage cho subgroup hoặc category hiếm.

Tuy nhiên ép training distribution thành uniform không đồng nghĩa deployment prior cũng uniform. Training balancing và probability calibration cần được xử lý như hai bài toán khác nhau.

## Counterfactual Data Augmentation

Có thể thay đổi một thuộc tính trong khi cố giữ label semantics, ví dụ:

```text
he ↔ she
thay background color
style transfer
```

Cách này hữu ích để phá shortcut, nhưng counterfactual phải còn plausible và không vô tình thay đổi target concept.

## Adversarial Synthetic Data

Có thể tạo hard negative hoặc red-team prompt gần decision boundary để tăng robustness.

Nhưng generator có thể chỉ tập trung vào failure mode đã biết và bỏ sót vùng hoàn toàn chưa được khám phá.

## Synthetic Evaluation Set

Generated benchmark giúp mở rộng scenario nhanh, nhưng nếu cùng một model family vừa sinh test case vừa chấm điểm, evaluation dễ trở thành vòng lặp khép kín.

Cần real/human anchor để hiệu chỉnh.

## Data Contamination

Khi web ngày càng chứa nhiều nội dung AI-generated, foundation model tương lai có thể ingest synthetic data mà không biết.

Lặp lại model-generated distribution qua nhiều thế hệ có thể thu hẹp diversity hoặc khuếch đại lỗi. Provenance vì vậy ngày càng quan trọng.

## Trực giác về Model Collapse

Nếu synthetic generation dần thay thế real signal qua nhiều generation mà không có dữ liệu thật mới, phần tail của distribution có thể bị xói mòn.

Behavior chính xác tùy setup, nhưng nguyên lý bền vững là: feedback loop chỉ gồm synthetic data có thể làm mất thông tin.

## Watermark và Metadata

Synthetic media có thể mang provenance metadata hoặc watermark.

Tuy nhiên metadata có thể bị xóa, còn watermark detection thường chỉ là probabilistic signal chứ không phải proof hoàn hảo.

## Label trong Simulation và Label ngoài Thực tế

Simulator có thể cung cấp internal state chính xác, nhưng mapping từ simulated state sang real sensor semantics vẫn có thể khác.

“Perfect simulated ground truth” không đồng nghĩa “perfect real-world relevance”.

## Ví dụ: Document OCR

Có thể render synthetic document với nhiều font và background để có exact transcription, bounding box hoặc layout annotation.

Đây là dữ liệu pretraining rất hữu ích. Nhưng real scan còn có fold, glare, handwriting, compression và camera distortion nên vẫn cần real fine-tuning hoặc evaluation.

## Ví dụ: Code Data

LLM có thể tạo exercise, solution và test case cho code.

Tuy nhiên output nên được compiler, unit test hoặc static analysis verify vì code trông hợp lệ về syntax vẫn có thể sai hoặc không an toàn.

## Mô hình tư duy

> **Synthetic data là output của một mô hình về thế giới. Train trên synthetic nghĩa là học từ assumption của world-model đó; giá trị lớn nhất đến từ khả năng kiểm soát, không phải vì synthetic tự nhiên đúng hơn real data.**

## Những nhầm lẫn thường gặp

### “Synthetic data giải quyết privacy”

Không tự động. Memorization và re-identification vẫn có thể xảy ra.

### “Càng nhiều synthetic sample thì diversity càng cao”

Không. Generator có thể tạo near-duplicate hoặc mode bias.

### “Synthetic data nhìn giống thật thì chắc chắn statistically correct”

Không. Visual plausibility không bảo đảm joint distribution liên quan tới task đã đúng.

## Liên kết kiến thức

Synthetic data nối Generative AI, Simulation, Privacy, Reinforcement Learning Environment và Data Governance.

Xem tiếp: [Quản trị Dữ liệu](./08_data_governance.md).