# Supervised Fine-Tuning (SFT)

**Supervised Fine-Tuning (SFT / 지도 미세조정 / tinh chỉnh có giám sát)** là giai đoạn tiếp tục train một pretrained model trên tập examples có input và desired output rõ ràng. Với chat model, một sample có thể gồm system message, user request và assistant response chuẩn.

Nếu pretraining học distribution rộng của language, SFT ép gradient tập trung vào **behavior distribution mong muốn**.

## Objective

Về mặt toán học, SFT thường vẫn dùng next-token cross-entropy trên target response:

\[
\mathcal L_{SFT}=-\sum_{t\in response}\log P_\theta(y_t\mid x,y_{<t})
\]

`x` là instruction/context, còn `y` là desired answer.

Nhiều pipeline mask loss trên user/system tokens và chỉ optimize assistant tokens. Như vậy model không bị train để “predict user” mà tập trung tái tạo response behavior.

## SFT khác pretraining ở đâu?

Mechanism optimizer/backprop có thể giống, nhưng **data distribution và supervision signal** khác.

Pretraining:

```text
raw corpus → predict next token everywhere
```

SFT:

```text
instruction/context → imitate curated target response
```

SFT vì vậy gần behavior cloning hơn raw language modeling.

## Data quality quyết định behavior quality

Một SFT dataset nhỏ nhưng curated có thể thay đổi behavior mạnh vì pretrained model đã có capability nền. Nhưng nếu target responses verbose, evasive, overconfident hoặc inconsistent, model sẽ bắt chước pattern đó.

SFT data cần represent nhiều dimensions:

- correctness;
- instruction adherence;
- style/depth;
- refusal behavior;
- tool format;
- multilingual coverage;
- ambiguity handling.

## Loss masking và conversation templates

Chat template quyết định token nào đại diện role boundaries. Một mismatch giữa training template và serving template có thể làm model behavior giảm dù weights không đổi.

Ví dụ model được train với special tokens:

```text
<|system|> ...
<|user|> ...
<|assistant|> ...
```

nhưng inference dùng format khác, model có thể không recognize role semantics đúng như training.

## Full fine-tuning vs parameter-efficient fine-tuning

**Full fine-tuning** cập nhật gần như toàn bộ model weights. Nó linh hoạt nhưng tốn memory/compute và có risk catastrophic forgetting.

**Parameter-Efficient Fine-Tuning (PEFT)** chỉ train một subset parameters hoặc adapters. LoRA là ví dụ nổi tiếng:

\[
W' = W + BA
\]

với rank nhỏ `r`, nên số trainable parameters giảm mạnh.

LoRA không “compress toàn bộ model”; nó học một low-rank update trên một số matrices được chọn.

## Domain fine-tuning

Nếu task yêu cầu terminology và output style đặc thù, SFT domain có thể rất hữu ích. Ví dụ financial support assistant cần response format, tone và escalation logic ổn định.

Nhưng facts thường xuyên thay đổi vẫn nên đến từ database/RAG, không nên hard-code qua weights nếu provenance quan trọng.

## Curriculum và mixture

SFT dataset thường là mixture của general instruction, domain tasks, safety data và tool use. Weighting ảnh hưởng gradient.

Nếu safety examples quá nhiều và simplistic, over-refusal tăng. Nếu domain data quá mạnh, general capability có thể giảm.

## Response-only loss

Trong chat SFT, một practice phổ biến là tính loss chỉ trên assistant response. Điều này tránh model học reproduce user text.

Tuy nhiên system prompt structure vẫn ảnh hưởng hidden representation vì nó nằm trong context dù không chịu loss trực tiếp.

## Sequence packing

Nhiều short SFT samples có thể pack vào một training sequence để tăng utilization. Attention/loss masks phải đảm bảo samples không leak context lẫn nhau ngoài intended packing semantics.

## Overfitting trong SFT

SFT dataset thường nhỏ hơn pretraining corpus rất nhiều. Model lớn có thể memorize formatting hoặc exact answers nhanh.

Validation cần đo:

```text
training loss
validation loss
behavior evals
out-of-template generalization
```

SFT loss thấp không đồng nghĩa assistant tốt.

## SFT và reasoning traces

Dataset có thể chứa rationale hoặc chain-like solution steps. Model có thể học pattern giải từng bước, nhưng quality phụ thuộc correctness của traces.

Nếu traces chứa plausible nhưng incorrect reasoning, model cũng bắt chước.

Không nên assume dài hơn = reasoning tốt hơn.

## Distillation bằng SFT

Một teacher model mạnh có thể generate responses, sau đó student train bằng SFT. Đây là một dạng knowledge distillation ở behavior level.

Student học distribution output của teacher, nhưng không nhất thiết copy internal mechanism.

## Tool-use SFT

Để model gọi tools, dataset có thể chứa examples:

```text
user request
→ tool call JSON
→ tool result
→ final answer
```

SFT giúp model học syntax và decision patterns. Nhưng production vẫn cần schema validation, permissions và runtime error handling.

## SFT và calibration

SFT có thể làm model answers trông tự tin hơn mà không cải thiện factual calibration tương ứng. Vì vậy preference về “confident helpful style” có thể tạo overconfidence.

Evaluation phải tách style và correctness.

## Mental Model

> SFT là **behavior imitation trên top của pretrained capability**.

Nó không thay thế pretraining, retrieval hay runtime verification.

## Common Misconceptions

### “SFT train model từ đầu cho task”

Không. Với LLM, SFT thường là small post-training phase trên pretrained model.

### “LoRA luôn cho kết quả giống full fine-tuning”

Không. Hiệu quả phụ thuộc rank, target modules, data và mức thay đổi behavior cần thiết.

### “SFT dataset càng lớn càng tốt”

Bad/inconsistent examples có thể degrade behavior. Curated quality và coverage quan trọng hơn raw count.

## Knowledge Connection

SFT là cầu giữa [Instruction Tuning](./06_instruction_tuning.md) và preference optimization. Khi multiple acceptable answers tồn tại, imitation một target không đủ để encode preference ordering. Đó là lý do RLHF/DPO xuất hiện.

Xem tiếp: [RLHF](./08_rlhf.md).