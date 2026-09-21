# Scaling Laws trong Large Language Models

Khi Large Language Model lớn hơn, câu hỏi không chỉ là “thêm parameters có tốt hơn không?” mà là **nên phân bổ compute giữa model size, data và training duration như thế nào**. **Scaling laws (스케일링 법칙)** nghiên cứu relationship thực nghiệm giữa model performance và những resource đó.

Một pattern thường thấy là loss giảm theo power law khi tăng scale trong một khoảng rộng. Điều này không có nghĩa performance mọi benchmark tăng giống nhau, nhưng nó cho phép dự đoán trend và planning training runs tốt hơn.

## Ba trục scale chính

Pretraining cost có thể nhìn gần đúng qua ba quantities:

```text
N = số parameters
D = số training tokens
C = compute budget
```

Nếu model rất lớn nhưng data quá ít, model bị **under-trained**. Nếu data rất nhiều nhưng model quá nhỏ, capacity có thể là bottleneck. Compute-optimal training tìm balance tốt hơn giữa `N` và `D` dưới budget cố định.

## Parameters không phải capacity hữu ích duy nhất

Tăng parameters mở rộng function class và representation capacity, nhưng capability còn phụ thuộc architecture, data quality, optimizer, context length và training recipe. Hai models cùng parameter count có thể khác đáng kể.

**Active parameters** cũng khác total parameters trong architectures như Mixture-of-Experts (MoE), nơi mỗi token chỉ đi qua một subset experts. Vì vậy “model 100B” không luôn có inference cost tương đương model dense 100B.

## Compute-optimal intuition

Giả sử có budget compute cố định. Nếu dùng tất cả budget để tăng `N` nhưng giữ `D` thấp, mỗi parameter nhìn thấy quá ít evidence. Ngược lại, train model nhỏ trên quá nhiều data có thể waste data because capacity giới hạn.

Mental model:

> Scale hiệu quả là **model đủ lớn để hấp thụ structure trong data, và data đủ nhiều để train model lớn đó đúng mức**.

## Training tokens và epochs

Trong web-scale pretraining, corpus có thể được traversed một hoặc vài lần tùy recipe. Repeating data quá nhiều tăng memorization và diminishing returns. Nhưng curated high-quality data đôi khi được intentionally upsampled.

Do đó raw token count không bằng unique information content.

## Loss scaling vs capability scaling

Pretraining loss có thể giảm smooth, trong khi benchmark capability nhìn discontinuous. Ví dụ benchmark pass/fail có threshold; model từ 49% lên 51% có thể trông như capability “xuất hiện”.

Một số task thực sự có nonlinear behavior do composition of learned skills, nhưng không nên gọi mọi jump là emergence mà không kiểm tra metric granularity.

## Context length là một scale dimension khác

Longer context cho phép model condition trên nhiều tokens hơn nhưng attention và KV cache cost tăng. Training model ở context 4k không tự động bảo đảm model dùng hiệu quả 128k chỉ bằng thay config.

Long-context capability còn phụ thuộc positional method, training distribution, attention implementation và evaluation.

## Inference-time compute

Scale không chỉ nằm ở pretraining. Model có thể dùng thêm compute lúc inference qua:

- sampling nhiều candidates;
- search/verification;
- longer reasoning trajectories;
- tool calls;
- retrieval;
- self-consistency hoặc reranking.

Điều này tạo trade-off mới: cùng một base model, tăng inference-time compute có thể cải thiện accuracy nhưng tăng latency/cost.

## Distillation và small models

Scale lớn có thể dùng để tạo teacher, sau đó distill capability vào smaller model. Small models vẫn quan trọng khi latency, privacy, edge deployment hoặc cost là constraint.

Scaling laws không hàm ý mọi application nên dùng model lớn nhất.

## Economics của scale

Training frontier model cần hardware, energy, networking và engineering rất lớn. Nhưng production cost thường dominated bởi inference nếu user volume cao.

Một architecture tối ưu training cost chưa chắc tối ưu serving. KV cache, batchability, sequence length và decoding speed trở thành economic variables.

## Diminishing returns

Power-law improvement nghĩa improvement tiếp theo thường đắt hơn. Nếu giảm loss từ 2.0 xuống 1.8 cần X compute, giảm từ 1.8 xuống 1.6 có thể cần nhiều hơn đáng kể.

Vì vậy system engineering thường thắng raw scaling khi problem là freshness, grounding, tool access hoặc policy. RAG có thể hiệu quả hơn train model lớn hơn chỉ để nhớ private documents.

## Scaling và data quality

Khi model nhỏ, capacity có thể che bớt bad data vì model không memorize everything. Model lớn có khả năng hấp thụ cả useful patterns lẫn noise, duplicated misinformation và undesirable styles.

Do đó scale làm data governance quan trọng hơn, không ít hơn.

## Scaling và alignment

Base capability tăng không tự động kéo instruction following, truthfulness hay safety tăng đồng đều. Alignment/post-training phải scale theo capability và attack surface.

Một model mạnh hơn có thể vừa hữu ích hơn vừa có failure modes phức tạp hơn.

## Mental Model

```text
Scale ≠ chỉ parameters
Scale = model capacity + data + compute + context + inference strategy
```

Câu hỏi đúng không phải “bao nhiêu B parameters?”, mà là **resource nào hiện là bottleneck của task/system này?**

## Common Misconceptions

### “Model lớn hơn luôn tốt hơn cho production”

Không nếu cost, latency, privacy hoặc task simplicity dominate.

### “Loss giảm nghĩa mọi capability đều tăng”

Loss là aggregate language modeling signal; downstream capability có thể tăng với rate khác nhau.

### “Context window lớn = model nhớ và reasoning tốt trên toàn context”

Window capacity và effective context use là hai vấn đề khác nhau.

## Knowledge Connection

Scaling nối trực tiếp với [AI Compute](../17_ai_compute_and_infrastructure/00_compute_foundations.md), [Optimization](../01_mathematical_foundations/06_optimization.md) và [Pretraining](./04_pretraining.md).

Xem tiếp: [Instruction Tuning](./06_instruction_tuning.md).
