# Case — AI-generated claim: câu trả lời hợp lý chưa phải câu trả lời đã xác minh

AI/LLM có thể tạo một câu trả lời trôi chảy, có cấu trúc và nghe rất hợp lý ngay cả khi provenance thiếu, citation không tồn tại hoặc inference vượt quá evidence. Case này không dạy cách huấn luyện model; nó luyện workflow kiểm tra claim trước khi đưa output vào research, code, policy, health, legal hoặc decision có stakes.

## Situation

Một assistant trả lời:

> “Nghiên cứu cho thấy intervention X giảm risk Y 40%, nên bạn có thể áp dụng ngay.”

Tempting shortcut là tin vì câu trả lời rõ ràng, hoặc bác bỏ toàn bộ vì AI có thể hallucinate. Cả hai đều bỏ qua câu hỏi cần kiểm tra: claim chính xác là gì, nguồn ở đâu và action nào đang được đề xuất.

## Step 1 — Freeze output thành claim nhỏ

Tách câu trả lời thành các mệnh đề:

```text
study tồn tại?
population nào?
intervention/comparator là gì?
40% là relative hay absolute?
effect là association hay causal?
recommendation có vượt evidence không?
```

Không audit cả đoạn văn như một khối. Mỗi claim cần một đường evidence và boundary riêng.

## Step 2 — Truy provenance, không chấm văn phong

Yêu cầu title, authors, DOI/URL, ngày và đoạn nguồn hỗ trợ claim. Mở nguồn gốc thay vì tin citation do model sinh. Nếu link không tồn tại, study không nói con số đó, hoặc nguồn thứ cấp đã đổi nghĩa, đánh dấu `unverified`.

Provenance cũng gồm version/model, thời điểm hỏi, prompt/context và dữ liệu đầu vào khi output phụ thuộc chúng. Một câu trả lời có source thật vẫn có thể suy luận sai; source là điều kiện cần để audit, không phải giấy chứng nhận correctness.

## Step 3 — Evidence map và alternative

Dùng [Argument & Evidence Mapping](../practice/06_argument_and_evidence_mapping.md):

```text
claim
├── source / provenance
├── evidence for
├── evidence against / missing
├── inference made by model
├── alternative explanation
├── confidence
└── evidence that would change action
```

Nếu claim causal, chạy [Causal Reasoning](../causal-reasoning/README.md) để kiểm tra confounder, comparator, outcome và external validity. Nếu claim chỉ là summary, không nâng nó thành causal recommendation.

## Step 4 — Steelman và red-team câu trả lời

Viết phiên bản mạnh nhất mà model có thể đúng: “Trong population P, study S quan sát effect E dưới điều kiện C”. Sau đó hỏi:

```text
Nếu model hallucinate, dấu hiệu nào sẽ lộ ra?
Nếu source thật nhưng inference sai, step nào nhảy cóc?
Nếu claim đúng trong study, điều gì ngăn nó generalize sang user này?
```

[Red-team, Steelman & Disconfirmation](../practice/07_red_team_steelman_and_disconfirmation.md) giúp định trước test và update rule. Không dùng sự trôi chảy hoặc độ dài câu trả lời làm likelihood evidence.

## Step 5 — Chọn mức hành động theo stakes

```text
low stakes / reversible → kiểm tra nhanh, dùng như hypothesis
material decision → verify source, assumptions, alternatives và sensitivity
medical/legal/financial/safety → handoff chuyên môn, nguồn owner và không hành động chỉ từ output AI
```

Nếu verification cost cao, dùng [Value of Information](../value-of-information/README.md) để xem claim nào có khả năng đổi action. Không cần kiểm tra mọi câu trivia sâu như nhau; cần kiểm tra câu có thể gây hại hoặc khóa một quyết định khó đảo ngược.

## Step 6 — Output audit record

Lưu record thay vì chỉ lưu câu trả lời:

```text
Prompt / context / model version:
Exact claim:
Source requested:
Source opened and date:
Evidence actually supports:
Unverified leap:
Alternative explanation:
Confidence:
Action allowed / prohibited:
Human or domain owner:
Review trigger:
```

Record này tạo feedback loop: lần sau biết lỗi nằm ở retrieval, provenance, inference, prompt ambiguity hay domain boundary. Nếu source không thể xác minh, output đúng nhất có thể là “chưa biết”.

## Failure modes

- **Fluency = truth:** câu văn tự nhiên bị nhầm với evidence.
- **Citation laundering:** link thật được dùng để che một claim không nằm trong nguồn.
- **Authority transfer:** model nói tự tin nên người dùng bỏ qua owner chuyên môn.
- **Binary reaction:** tin toàn bộ hoặc bác bỏ toàn bộ thay vì tách claim.
- **No update record:** sửa prompt nhưng không ghi output/version, nên không biết failure có lặp lại không.

## Handoff

- Source, argument và evidence → [Philosophy](../../philosophy/README.md), [Research Methods](../../research_methods/README.md).
- Statistics/causal/health claim → [Mathematics](../../mathematics/README.md), [Biology](../../biology/README.md), [Causal Reasoning](../causal-reasoning/README.md).
- Code/system claim → [Computer Science](../../computer_science/README.md), [DevOps / Platform Engineering](../../devops_platform_engineering/README.md).
- Quyết định material → [Risk](../risk/README.md), [Decision Making](../decision-making/README.md) và domain owner phù hợp.

Nguyên tắc chốt là: **plausible answer ≠ verified answer**. AI có thể giúp tạo hypothesis và tìm đường kiểm tra; provenance, evidence, boundary và người chịu trách nhiệm mới quyết định output có được dùng để hành động hay không.
