# Đánh giá mô hình ngôn ngữ lớn

Đánh giá **mô hình ngôn ngữ lớn (Large Language Model — LLM)** khó hơn kiểm thử phần mềm truyền thống vì không gian đầu ra rất rộng, nhiều câu trả lời có thể cùng chấp nhận được, hành vi phụ thuộc mạnh vào lời nhắc (prompt), ngữ cảnh (context), tham số sinh và các thành phần bên ngoài như RAG hoặc công cụ. Vì vậy một hệ thống đánh giá tốt không hỏi chung chung “mô hình này tốt không?”, mà phải hỏi rõ: **tốt cho tác vụ nào, trên quần thể nào, theo tiêu chí nào, dưới phiên bản và ràng buộc nào**.

## Kiến thức cần có trước

Nên nắm [Mô hình ngôn ngữ](../07_natural_language_processing/02_language_models.md), [LLM và quá trình hậu huấn luyện](./00_from_language_models_to_llms.md), [Sampling và ngữ cảnh](./11_prompting_and_context_engineering.md), [Hallucination và Grounding](./13_hallucination_and_grounding.md) và [Đánh giá mô hình học máy](../04_machine_learning/15_model_evaluation.md).

## Bắt đầu từ hợp đồng đánh giá

Trước khi chọn metric, cần mô tả **hợp đồng đánh giá (evaluation contract)**:

```text
nhiệm vụ là gì?
input distribution nào đại diện production?
output nào được coi là đúng hoặc chấp nhận được?
loại lỗi nào có chi phí cao nhất?
model/prompt/context/tool version nào đang được đánh giá?
latency và cost budget là bao nhiêu?
có yêu cầu về safety, privacy hoặc citation không?
```

Nếu các câu hỏi này chưa rõ, một điểm benchmark cao chỉ tạo cảm giác chính xác giả.

## Perplexity chưa đủ

Tiền huấn luyện thường theo dõi cross-entropy và **perplexity**. Với chuỗi `x_1,...,x_N`:

\[
PPL=\exp\left(-\frac{1}{N}\sum_{i=1}^{N}\log P(x_i\mid x_{<i})\right)
\]

Perplexity thấp hơn nghĩa mô hình dự đoán token trên dữ liệu held-out tốt hơn. Tuy nhiên nó không trực tiếp đo khả năng làm theo chỉ dẫn, factuality, correctness của code, tool use hay safety.

Do đó cần tách **mục tiêu huấn luyện (training objective)** khỏi **chất lượng tác vụ (task quality)**.

## Benchmark năng lực

Benchmark thường đo từng lát cắt như toán, lập trình, tri thức, đọc hiểu hoặc đa ngôn ngữ. Chúng hữu ích để so sánh trong điều kiện chuẩn hóa nhưng dễ bị diễn giải quá mức.

Một benchmark score chỉ có ý nghĩa dưới:

```text
dataset version
prompt protocol
few-shot examples nếu có
decoding parameters
model version
evaluator version
scoring rule
```

Thay một trong các yếu tố trên có thể làm score thay đổi dù trọng số mô hình không đổi.

## Nhiễm dữ liệu đánh giá

Nếu ví dụ benchmark hoặc bản gần trùng đã xuất hiện trong dữ liệu huấn luyện, score có thể đánh giá quá cao khả năng khái quát hóa. Nhiễm dữ liệu (contamination) khó phát hiện hoàn toàn khi corpus huấn luyện không công khai.

Vì vậy production team nên giữ thêm:

- tập đánh giá riêng (private eval);
- holdout chưa dùng để tune;
- case mới lấy từ production failure;
- kiểm tra gần-trùng khi có thể.

## Exact Match, semantic score và verifier

Tác vụ có cấu trúc như classification hoặc code có thể dùng bộ kiểm tra xác định:

```text
exact match
schema validation
unit test
compiler
calculator
SQL parser
policy rule
```

Câu trả lời mở thường cần rubric ngữ nghĩa, human review hoặc LLM-as-a-judge. Nguyên tắc quan trọng là: **khi có verifier xác định thì nên ưu tiên verifier đó trước judge xác suất**.

## Đánh giá theo cặp

Thay vì gán điểm tuyệt đối, evaluator có thể chọn phản hồi A hay B tốt hơn. So sánh theo cặp thường ổn định hơn rubric 1–10, nhưng cần ngẫu nhiên hóa vị trí A/B và hỗ trợ kết quả hòa.

Nếu `p` là xác suất A thắng B trên một tập scenario, chênh lệch nhỏ quanh `p=0.5` cần số mẫu đủ lớn mới đáng tin. Vì vậy không nên tuyên bố “A tốt hơn” chỉ từ vài chục ví dụ.

## Đánh giá theo tác vụ thực tế

Production eval nên phản ánh workload thật. Ví dụ trợ lý hỗ trợ khách hàng có thể cần đo:

```text
xử lý đúng vấn đề
tuân thủ policy
citation được nguồn hỗ trợ
escalation chính xác
độ trễ
chi phí
```

Benchmark tổng quát không thay thế task-specific eval.

## Golden set và hidden holdout

Một **golden set** được tuyển chọn nên chứa case đại diện, edge case và failure đã biết. Nó cần versioning và chạy regression mỗi khi đổi model, prompt, RAG hoặc tool code.

Nếu đội phát triển liên tục tune theo cùng golden set, nó đã trở thành development set. Khi đó cần hidden holdout hoặc tập đánh giá mới để tiếp tục đo khả năng khái quát hóa.

## Phân loại lỗi

Aggregate score che giấu failure mode. Nên phân nhóm lỗi:

```text
FACTUAL_ERROR
INSTRUCTION_MISS
REASONING_ERROR
RETRIEVAL_MISS
CITATION_MISMATCH
FORMAT_ERROR
TOOL_ERROR
UNSAFE_BEHAVIOR
OVER_REFUSAL
LATENCY_TIMEOUT
```

Error taxonomy giúp xác định layer cần sửa thay vì phản xạ đổi model mỗi khi score giảm.

## Mô hình triển khai của eval harness

Một eval harness production nên có cấu trúc gần như sau:

```text
versioned eval cases
→ runner cố định model/prompt/tool/index version
→ thực thi N lần nếu output stochastic
→ deterministic validators
→ model/human judge khi cần
→ ghi trace + artifact
→ aggregate metrics + slices
→ regression gate
```

Mỗi kết quả nên gắn với một **behavior bundle** cụ thể:

```text
base model version
prompt version
sampling config
retrieval/index version
tool schema version
policy version
evaluator version
```

Nếu không lưu lineage này, một score cũ gần như không thể tái lập chính xác.

## Đánh giá stochastic output

Với temperature hoặc sampling khác 0, cùng input có thể cho nhiều output. Khi đó một lần chạy không phản ánh phân phối hành vi.

Nếu `S_i` là biến Bernoulli cho biết lần chạy thứ `i` thành công hay thất bại:

\[
\hat p=\frac{1}{n}\sum_{i=1}^{n}S_i
\]

thì `\hat p` ước lượng xác suất thành công. Với task quan trọng có thể cần nhiều lần chạy để ước lượng cả trung bình và variance, đặc biệt khi agent hoặc tool loop làm hành vi phân nhánh mạnh.

## Ngăn xếp đánh giá

Một ứng dụng LLM nên có nhiều tầng:

```text
unit test cho code xác định
retrieval test
model response eval
tool-call eval
trajectory eval nếu có agent
end-to-end workflow eval
online monitoring
human review
```

Không benchmark đơn lẻ nào bao phủ tất cả.

## Offline và online evaluation

**Đánh giá offline** dễ tái lập, an toàn và phù hợp làm release gate. **Đánh giá online** phản ánh traffic thật nhưng chịu confounding và có rủi ro production.

A/B testing có thể đo product outcome, nhưng phải có guardrail metric. Tăng engagement không được phép che việc tăng hallucination, escalation hoặc unsafe action.

## LLM-as-a-Judge

Judge model giúp mở rộng đánh giá cho text mở. Rubric phải rõ và nếu cần kiểm factuality, judge nên nhận reference hoặc evidence liên quan.

Rủi ro gồm:

```text
self-preference
thiên lệch theo độ dài
thiên lệch vị trí
blind spot chung giữa model và judge
độ nhạy với prompt đánh giá
```

Judge cần được hiệu chỉnh (calibration) bằng nhãn con người hoặc bộ reference. Khi judge thay phiên bản, chính evaluator cũng cần regression test.

## Đánh giá factuality và groundedness

Nếu câu trả lời phải grounded, evaluator nên tách phản hồi thành claim nguyên tử rồi kiểm tra claim theo evidence.

Một cách khái niệm:

\[
Groundedness=\frac{\text{số claim được evidence hỗ trợ}}{\text{tổng số factual claim}}
\]

Groundedness khác factual correctness đối với thế giới bên ngoài: một nguồn có thể hỗ trợ claim nhưng bản thân nguồn đã lỗi thời hoặc sai.

## Đánh giá tool use

Mô hình dùng công cụ cần được đo ít nhất ở các mức:

```text
có quyết định dùng tool đúng không?
chọn đúng tool không?
argument đúng schema và semantics không?
permission có được tuân thủ không?
result có được dùng đúng trong final answer không?
recovery khi tool lỗi có đúng không?
```

Task success quan trọng hơn việc tool call chỉ đúng cú pháp.

## Đánh giá safety và over-refusal

Safety eval cần cả prompt vô hại, prompt đối kháng, biến thể đa ngôn ngữ và nhiều phép biến đổi. Đồng thời phải đo **từ chối quá mức (over-refusal)** trên tác vụ hợp lệ.

Một hệ thống từ chối mọi thứ có thể đạt một số safety metric nhưng thất bại hoàn toàn về usefulness.

## Robustness và sensitivity

Có thể paraphrase cùng yêu cầu, thêm typo, context dài, nhiễu hoặc evidence mâu thuẫn. Nếu chất lượng thay đổi lớn dưới biến đổi nhỏ, hành vi còn giòn (brittle).

Nên tách:

```text
invariance mong muốn → cách diễn đạt đổi nhưng đáp án nên giữ
sensitivity mong muốn → dữ kiện quan trọng đổi thì đáp án phải đổi
```

Cả hai đều quan trọng; một mô hình “ổn định” quá mức cũng có thể bỏ qua dữ kiện mới.

## Bất định thống kê

Metric quan sát được chỉ là ước lượng từ sample hữu hạn. Khi so hai hệ thống trên cùng case, nên dùng paired analysis khi có thể.

Bootstrap hoặc confidence interval giúp trả lời câu hỏi: chênh lệch quan sát được lớn tới mức nào so với nhiễu lấy mẫu?

Không nên dùng chênh lệch 0.2–0.3% trên tập nhỏ để quyết định migration production nếu không có bằng chứng thống kê hoặc ý nghĩa kinh doanh rõ.

## Slice evaluation

Điểm trung bình có thể che failure ở:

```text
ngôn ngữ
region
input length
document type
user segment
rare intent
high-risk workflow
```

Slice nên được chọn theo risk và production hypothesis, không phải tạo vô hạn nhóm chỉ vì có thể.

## Biên Pareto: chất lượng – độ trễ – chi phí

Chọn model production là bài toán đa mục tiêu:

\[
quality,\ latency,\ cost,\ reliability
\]

Không có model tốt nhất tuyệt đối nếu một model tăng 1% quality nhưng tăng 10 lần cost hoặc p99 latency. Nên so trên **biên Pareto (Pareto frontier)** và cost-per-successful-task.

## Failure mode của chính hệ thống đánh giá

**Benchmark overfitting.** Team tối ưu trực tiếp vào bộ test quen thuộc.

**Judge drift.** Đổi evaluator làm score thay đổi nhưng không phải model thay đổi.

**Hidden configuration drift.** Sampling, prompt hoặc tool schema đổi mà report vẫn dùng cùng tên model.

**Average hides tail risk.** Score trung bình tốt nhưng một slice quan trọng thất bại nghiêm trọng.

**Single-run optimism.** Một output may mắn được coi là behavior điển hình.

**Metric không phản ánh task.** Tối ưu style hoặc verbosity nhưng không đo outcome thật.

## Production usage và release gate

Một flow thực tế:

```text
candidate behavior bundle
→ smoke test
→ deterministic checks
→ offline capability + safety eval
→ critical-slice eval
→ cost/latency check
→ shadow hoặc canary
→ online monitoring
→ promote hoặc rollback
```

Mỗi production incident đáng kể nên tạo thêm regression case mới. Như vậy evaluation trở thành **bộ nhớ có cấu trúc về những gì hệ thống từng làm sai**.

## Mô hình tư duy

> Một LLM không có “chất lượng” tuyệt đối. Chất lượng là **phân phối hành vi trên một tập tác vụ và population dưới một protocol, phiên bản và ngân sách cụ thể**.

## Những hiểu lầm thường gặp

### “Benchmark cao hơn nghĩa model tốt hơn mọi mặt”

Không. Benchmark chỉ đo một số lát cắt năng lực.

### “LLM judge thay thế hoàn toàn con người”

Không. Judge cần calibration, kiểm tra và audit.

### “Một test set dùng mãi vẫn khách quan”

Khi đội phát triển liên tục tune theo nó, nó đã trở thành tín hiệu development.

### “Chỉ cần đánh giá model, không cần đánh giá prompt/RAG/tool”

Không. Production behavior là kết quả của toàn bộ behavior bundle.

## Liên kết kiến thức

Đánh giá LLM nối [Đánh giá học máy](../04_machine_learning/15_model_evaluation.md), [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Evaluation Foundations](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).

Xem tiếp: [Giới hạn của LLM](./15_llm_limitations.md).