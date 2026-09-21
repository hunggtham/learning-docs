# Nền tảng đánh giá hệ thống AI

**Đánh giá (evaluation / 평가)** là quá trình thu thập bằng chứng để xác định một mô hình hoặc hệ thống AI có đáp ứng đúng mục tiêu trên một nhóm người dùng, phân phối dữ liệu và điều kiện vận hành cụ thể hay không. Đánh giá không phải chỉ chạy một benchmark rồi đọc một con số. Nó phải nối yêu cầu sản phẩm với dữ liệu kiểm thử, thước đo, độ bất định, các lát dữ liệu quan trọng, lỗi hệ thống và quyết định triển khai.

Một cách nhìn ngắn gọn:

```text
Yêu cầu thật
→ hợp đồng hành vi
→ tập kiểm thử / kịch bản
→ phép đo
→ phân tích lỗi
→ quyết định phát hành / sửa / từ chối
```

## Kiến thức tiên quyết

Chapter này giả định đã hiểu các khái niệm về [đánh giá mô hình Machine Learning](../04_machine_learning/15_model_evaluation.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md), [Agent](../10_agents_and_ai_systems/00_from_llm_to_agent.md) và [AI Engineering](../15_ai_engineering/00_ai_engineering.md). Với hệ thống hiện đại, đánh giá phải diễn ra ở cả cấp mô hình lẫn cấp hệ thống.

## Bắt đầu từ quyết định, không bắt đầu từ metric

Trước khi chọn thước đo, cần trả lời:

```text
hệ thống phải hoàn thành nhiệm vụ gì?
đầu ra nào được coi là thành công?
lỗi nào có tác động lớn nhất?
ai hoặc nhóm nào bị ảnh hưởng?
độ trễ, chi phí và yêu cầu an toàn là gì?
điều kiện nào buộc hệ thống phải từ chối hoặc chuyển sang người xử lý?
```

Nếu doanh nghiệp quan tâm thiệt hại gian lận nhưng chỉ tối ưu accuracy, mục tiêu đánh giá đã lệch ngay từ đầu. Nếu Agent được phép gửi email hoặc sửa dữ liệu nhưng bộ kiểm thử chỉ chấm chất lượng câu trả lời cuối, phần quan trọng nhất của hệ thống chưa được đo.

## Hợp đồng đánh giá

Một **hợp đồng đánh giá (evaluation contract)** nên mô tả rõ:

```text
population / workload
input contract
expected behavior
allowed uncertainty
forbidden behavior
latency / cost budget
success criterion
fallback criterion
```

Ví dụ với trợ lý RAG nội bộ, thành công có thể yêu cầu đồng thời: truy xuất đúng tài liệu, câu trả lời được hỗ trợ bởi nguồn, citation trỏ đúng đoạn, không đọc tài liệu ngoài quyền và hoàn thành trong ngân sách độ trễ.

## Đánh giá thành phần và đánh giá đầu-cuối

Một ứng dụng có thể gồm:

```text
query processing
→ retrieval
→ reranking
→ context packing
→ LLM
→ tool
→ verifier
→ output
```

Mỗi thành phần cần metric riêng để chẩn đoán, nhưng người dùng trải nghiệm kết quả đầu-cuối.

Ví dụ:

```text
retrieval Recall@k cao
nhưng context packing cắt mất đoạn quyết định
→ câu trả lời cuối vẫn sai
```

Ngược lại, câu trả lời đúng một lần không chứng minh retriever tốt; mô hình có thể trả lời từ kiến thức sẵn có hoặc đoán đúng.

## Đánh giá offline và online

**Đánh giá offline (offline evaluation)** chạy trên dữ liệu hoặc môi trường mô phỏng cố định. Nó nhanh, có thể lặp lại và phù hợp để làm cổng phát hành.

**Đánh giá online (online evaluation)** đo hành vi trên lưu lượng thật thông qua shadow deployment, canary, A/B testing, outcome nghiệp vụ hoặc phản hồi có kiểm soát.

Luồng production hợp lý thường là:

```text
offline regression suite
→ adversarial / safety suite
→ shadow
→ canary
→ online monitoring
```

Không nên dùng production traffic như nơi đầu tiên phát hiện lỗi có thể tìm được bằng kiểm thử offline.

## Tập kiểm thử và rò rỉ đánh giá

Tập test phải đại diện cho phân phối sử dụng dự kiến và được tách khỏi vòng tối ưu. Nếu nhóm phát triển xem lỗi trên test rồi sửa prompt, model hoặc retrieval nhiều lần, tập đó đã trở thành tập phát triển.

Khi đó cần holdout mới hoặc tập kiểm thử ẩn.

Với LLM, contamination còn có thể đến từ pretraining hoặc dữ liệu tổng hợp. Vì vậy benchmark công khai chỉ là một bằng chứng, không phải phép đo tuyệt đối về năng lực tổng quát.

## Thiết kế kịch bản thay vì chỉ thiết kế câu hỏi

Hệ thống production cần **kịch bản (scenario)** bao phủ trạng thái và failure mode thật:

```text
happy path
thiếu dữ liệu
nguồn mâu thuẫn
tài liệu lỗi thời
retrieval rỗng
tool timeout
permission denied
context quá dài
prompt injection gián tiếp
user đổi mục tiêu giữa chừng
```

Mỗi kịch bản nên có invariant và acceptance criterion rõ. Với Agent, không nhất thiết yêu cầu trajectory giống hệt nhau; có thể yêu cầu các invariant như “không ghi dữ liệu trước approval” hoặc “mọi mutation phải được verify”.

## Chọn metric theo loại bài toán

Classification thường dùng accuracy, precision, recall, F1, ROC-AUC, PR-AUC, log loss và calibration.

Regression thường dùng MAE, MSE/RMSE hoặc quantile loss.

Ranking và retrieval thường dùng Recall@k, Precision@k, MRR và nDCG.

Generation cần các phép đo như tính đúng ngữ nghĩa, mức hỗ trợ bởi nguồn, tính đầy đủ, tuân thủ schema và đánh giá của con người.

Agent cần đo thêm task success, số bước, lỗi công cụ, verified completion, số mutation, rollback, latency và cost.

Không có metric đơn lẻ nào đủ cho hệ thống đa thành phần.

## Trực giác toán học về expected loss

Đánh giá nên gắn với chi phí lỗi. Với ma trận chi phí `C`, tổn thất kỳ vọng có thể viết:

\[
E[C]=\sum_{i,j}P(y=i,\hat y=j)C_{ij}
\]

Điều này giải thích vì sao hai mô hình có cùng accuracy vẫn có giá trị kinh doanh rất khác nhau nếu loại lỗi của chúng khác nhau.

Với workflow hoặc Agent, có thể mở rộng trực giác:

\[
Utility = Value(success)-Cost(compute)-Cost(latency)-Expected\ Loss(failure)
\]

Không cần một công thức duy nhất cho mọi sản phẩm; điều quan trọng là đưa trade-off ra thành biến có thể quan sát.

## Threshold là một phần của policy

Mô hình xác suất chưa trực tiếp tạo quyết định. Policy còn cần threshold hoặc rule.

Một model có thể giữ nguyên nhưng precision/recall thay đổi mạnh khi threshold đổi. Vì vậy version của threshold phải được quản lý cùng deployment, không nên coi `0.5` là mặc định tự nhiên.

## Calibration và khả năng từ chối

Nếu hệ thống dự đoán xác suất 0.8 cho nhiều trường hợp, khoảng 80% trong nhóm đó có đúng không? Đây là câu hỏi về **hiệu chỉnh xác suất (calibration)**.

Calibration đặc biệt hữu ích khi hệ thống có vùng từ chối:

```text
độ tin cậy cao   → tự động xử lý
độ tin cậy trung bình → thêm verifier
độ tin cậy thấp → human review / abstain
```

Với LLM sinh văn bản, token probability không phải xác suất “câu trả lời đúng”. Cần verifier, evidence và thước đo đặc thù task thay vì dùng logit làm confidence trực tiếp.

## Slice và long tail

Average score dễ che lỗi ở nhóm nhỏ nhưng quan trọng. Nên đánh giá theo các lát có ý nghĩa:

```text
ngôn ngữ
khu vực
thiết bị
độ dài input
loại tài liệu
khách hàng mới / cũ
rare class
mức rủi ro nghiệp vụ
```

Rare case có tác động cao cần kịch bản riêng. Ví dụ payment agent đạt 99% task success vẫn chưa đủ nếu 1% lỗi có thể gây giao dịch trùng.

## Độ bất định thống kê

Metric là ước lượng từ mẫu hữu hạn. Khi chênh lệch nhỏ, nên dùng confidence interval, bootstrap hoặc repeated run.

Với tỷ lệ thành công `p` được ước lượng từ `n` trường hợp độc lập, sai số chuẩn trực giác gần:

\[
SE\approx\sqrt{\frac{p(1-p)}{n}}
\]

Do đó cải thiện 0.2% trên tập nhỏ có thể chỉ là nhiễu.

Với hệ thống sinh ngẫu nhiên, cần chạy nhiều sample hoặc seed để đo cả trung bình lẫn variance.

## Mô hình triển khai của một evaluation pipeline

Một pipeline thực dụng có thể là:

```text
versioned eval dataset
→ scenario runner
→ system under test
→ deterministic checks
→ model-based / human judge khi cần
→ aggregate + slice metrics
→ failure taxonomy
→ release gate
```

Mỗi kết quả phải truy được về version của model, prompt, retrieval index, tool schema và policy. Nếu không, regression rất khó tái hiện.

## LLM-as-Judge và giới hạn

Mô hình làm giám khảo (LLM-as-Judge) hữu ích cho relevance, style hoặc completeness, nhưng có thể bị thiên lệch vị trí, độ dài, phong cách và lỗi tương quan với model được chấm.

Dùng nó như một evaluator có sai số, không phải oracle. Nên hiệu chỉnh với human/reference set và ưu tiên deterministic validator cho các property có thể kiểm trực tiếp.

## Regression testing

Evaluation suite phải trở thành cổng phát hành. Mỗi incident production hoặc bug nghiêm trọng nên được chuyển thành regression case mới.

Luồng học từ lỗi:

```text
incident
→ root cause
→ reproducible scenario
→ thêm vào eval suite
→ fix
→ xác nhận không regress
```

Nhờ đó knowledge vận hành tích lũy thành test thay vì chỉ nằm trong postmortem.

## Failure taxonomy

Không chỉ ghi “wrong answer”. Nên phân loại:

```text
RETRIEVAL_MISS
RERANKING_ERROR
CONTEXT_PACKING
MODEL_REASONING
UNSUPPORTED_CLAIM
FORMAT_ERROR
TOOL_SELECTION
TOOL_EXECUTION
STATE_STALE
PERMISSION
VERIFICATION_MISS
TIMEOUT
ORCHESTRATION
```

Taxonomy giúp biết cần sửa data, retriever, prompt, model, tool hay runtime.

## Trade-off trong đánh giá

Bộ kiểm thử càng rộng thì chi phí chạy càng cao. Human evaluation chất lượng cao nhưng chậm; automated judge nhanh nhưng có bias. Hidden set tốt cho tính khách quan nhưng khó debug. Production A/B phản ánh thực tế nhưng có rủi ro ảnh hưởng người dùng.

Do đó nên dùng nhiều tầng:

```text
nhanh/rẻ → chạy mỗi commit
trung bình → chạy trước release
đắt/sâu → chạy định kỳ hoặc trước thay đổi lớn
online → xác nhận sau rollout có kiểm soát
```

## Failure mode của chính hệ thống đánh giá

Evaluation cũng có thể sai vì:

- benchmark contamination;
- label hoặc rubric mơ hồ;
- test set không đại diện;
- evaluator model thiên lệch;
- metric bị tối ưu quá mức;
- thiếu slice có rủi ro cao;
- dữ liệu eval lỗi thời;
- test chỉ kiểm happy path.

Một score cao chỉ có ý nghĩa trong phạm vi coverage mà evaluation thực sự kiểm tra.

## Dùng trong production

Evaluation phục vụ ba mục tiêu khác nhau:

```text
phát triển      → so sánh giả thuyết
phát hành       → release gate
vận hành        → phát hiện regression và drift
```

Không nên chỉ xây benchmark một lần rồi bỏ. Eval suite phải có version, owner, coverage map và lịch cập nhật dựa trên workload thực tế.

## Mô hình tư duy

> **Evaluation là bằng chứng về hành vi dưới một phân phối và một hợp đồng đã xác định; nó không phải chứng nhận rằng hệ thống “thông minh” hoặc “an toàn” trong mọi tình huống.**

## Những nhầm lẫn thường gặp

### “Benchmark cao nghĩa production tốt”

Không. Production data, tool, state và latency contract có thể khác benchmark.

### “Một metric là đủ”

Không. Chất lượng, calibration, latency, cost, reliability và safety là nhiều trục khác nhau.

### “Final answer đúng là đủ cho Agent”

Không. Trajectory có thể dùng sai quyền, tạo side effect rồi rollback hoặc vượt ngân sách.

### “LLM judge thay thế được test xác định”

Không. File tồn tại hay không, schema hợp lệ hay không, transaction đã commit hay chưa nên được kiểm bằng hệ thống xác định.

## Liên kết kiến thức

Đọc tiếp [Metrics, Benchmarks và Test Design](./01_metrics_benchmarks_and_test_design.md), [Uncertainty và Calibration](./02_uncertainty_and_calibration.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md) và [Reliability Engineering](./07_reliability_engineering.md).

Các evaluation chuyên biệt nằm tại [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).