# In-Context Learning

**In-Context Learning (ICL / 문맥 내 학습 / học trong ngữ cảnh)** là hiện tượng model thay đổi behavior dựa trên examples hoặc instructions nằm trong context **mà không cần update weights**.

Ví dụ:

```text
Input: 2 + 3
Output: five

Input: 4 + 1
Output: five

Input: 7 + 2
Output:
```

Model có thể infer pattern output bằng chữ và trả `nine` dù không có gradient step nào xảy ra.

## “Learning” nhưng không update parameters

Tên gọi dễ gây nhầm. Trong ICL, model weights giữ nguyên trong inference session. Điều thay đổi là hidden states và attention patterns được condition bởi context.

Vì vậy cần phân biệt:

```text
Training-time learning → update parameters
In-context learning     → temporary behavior conditioned on prompt/context
```

Context hết thì adaptation đó không được lưu vĩnh viễn vào weights.

## Zero-shot, one-shot, few-shot

**Zero-shot** chỉ cung cấp instruction, không examples.

**One-shot** cung cấp một demonstration.

**Few-shot** cung cấp vài demonstrations để model infer task/format.

Few-shot hữu ích khi task khó mô tả bằng rule nhưng dễ minh họa bằng examples.

## Demonstrations làm gì?

Demonstrations có thể truyền nhiều loại information cùng lúc:

- task mapping;
- output format;
- labels semantics;
- tone/style;
- edge-case handling;
- reasoning pattern.

Vì vậy example quality quan trọng hơn chỉ số lượng.

## Order sensitivity

ICL có thể sensitive với thứ tự examples. Recent examples đôi khi ảnh hưởng mạnh hơn, label imbalance có thể bias output, và một bad demonstration có thể kéo model sai hướng.

Đây là lý do prompt eval cần test multiple example sets, không chỉ một handcrafted prompt.

## Label semantics

Nếu labels là arbitrary strings như `A`, `B`, `C`, few-shot examples giúp model map semantic class sang label token.

Nếu example labels sai, model có thể follow demonstration thay vì internal prior.

ICL vì vậy vừa là capability vừa là attack surface: malicious context có thể steer behavior.

## Context as temporary program

Một mental model hữu ích là xem prompt như một **temporary program**:

```text
instructions
+ examples
+ retrieved facts
+ tool outputs
→ temporary computation context
```

Model weights là interpreter learned; context định nghĩa local task state.

Analogy này không hoàn hảo vì LLM execution probabilistic và không có formal semantics như programming language, nhưng hữu ích cho system design.

## Why ICL emerges

Trong pretraining, model quan sát rất nhiều text patterns nơi previous text defines local conventions: tutorials, examples, dialogues, code, question-answer sequences. Transformer học dùng context để predict next tokens under those local patterns.

Scale và task diversity làm capability này mạnh hơn, nhưng exact mechanism vẫn là active research topic. Không cần giả định model chạy hidden gradient descent để sử dụng ICL hiệu quả trong engineering.

## ICL vs Fine-Tuning

ICL thích hợp khi task thay đổi nhanh, examples ít, cần no-training deployment hoặc user-specific customization theo session.

Fine-tuning thích hợp khi behavior phải consistent trên rất nhiều requests và pattern stable.

Trade-off:

```text
ICL          → flexible, no weight update, consumes context tokens
Fine-tuning  → persistent behavior, training cost, less prompt overhead
```

## ICL vs RAG

RAG đưa external **knowledge/evidence** vào context. ICL đưa examples/instructions để định nghĩa **task behavior**.

Một RAG application có thể dùng cả hai:

```text
few-shot examples
+ retrieved documents
+ user query
→ answer
```

## Context length is not free

Few-shot examples consume context window và inference cost. Too many examples có thể dilute relevant information hoặc push important content ra khỏi window.

Selection therefore becomes retrieval problem: chọn demonstrations relevant nhất thay vì nhét toàn bộ examples.

## Dynamic few-shot selection

Có thể embed user query, retrieve similar labeled examples và insert chúng vào prompt. Đây là hybrid giữa retrieval và ICL.

Nhưng similarity không luôn đồng nghĩa examples tốt nhất. Sometimes diversity hoặc coverage quan trọng hơn nearest neighbor.

## Prompt contamination

Retrieved/user-provided text có thể chứa instructions. Nếu application blindly mixes data và instructions, model có thể follow untrusted content.

ICL capability chính là lý do **prompt injection** nguy hiểm: model naturally learns behavior from context.

## ICL và reasoning

Few-shot reasoning examples có thể improve performance bằng cách demonstrate decomposition pattern. Nhưng model cũng có thể copy superficial style mà không internalize correct logic.

Evaluation cần check answer correctness, not presence of reasoning-like prose.

## Mental Model

> In-context learning là **temporary adaptation through context**, không phải parameter update.

Model đọc prompt vừa như data vừa như task specification, vì vậy context design là một phần của programming AI system.

## Common Misconceptions

### “Few-shot examples train model ngay lúc inference”

Không có standard weight update. Behavior change là context conditioning.

### “Càng nhiều examples càng tốt”

Không. Context cost, redundancy và conflicting examples có thể làm performance giảm.

### “Long context thay thế fine-tuning”

Không. Persistent behavior và session-specific conditioning giải quyết different problems.

## Knowledge Connection

ICL nối [Pretraining](./04_pretraining.md), [Attention/Transformer](../06_deep_learning_architectures/04_attention.md), RAG và Agent context management.

Xem tiếp: [Prompting and Context Engineering](./11_prompting_and_context_engineering.md).