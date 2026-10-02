# Nền tảng đánh giá hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Evaluation foundations cho hệ thống AI**. Route đi từ decision/use case → target behavior → test data → metrics and thresholds → deployment feedback, để đánh giá bắt đầu từ điều cần quyết định chứ không từ một con số rời rạc.

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

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Bắt đầu từ quyết định, không bắt đầu từ chỉ số (metric / 지표)** tiếp nhận điểm tựa từ **Kiến thức tiên quyết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hợp đồng đánh giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bắt đầu từ quyết định, không bắt đầu từ chỉ số (metric / 지표)

Trước khi chọn thước đo, cần trả lời:

```text
hệ thống phải hoàn thành nhiệm vụ gì?
đầu ra nào được coi là thành công?
lỗi nào có tác động lớn nhất?
ai hoặc nhóm nào bị ảnh hưởng?
độ trễ, chi phí và yêu cầu an toàn là gì?
điều kiện nào buộc hệ thống phải từ chối hoặc chuyển sang người xử lý?
```

Nếu doanh nghiệp quan tâm thiệt hại gian lận nhưng chỉ tối ưu accuracy, mục tiêu đánh giá đã lệch ngay từ đầu. Nếu tác nhân (agent / 에이전트) được phép gửi email hoặc sửa dữ liệu nhưng bộ kiểm thử chỉ chấm chất lượng câu trả lời cuối, phần quan trọng nhất của hệ thống chưa được đo.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Hợp đồng đánh giá** tiếp nhận điểm tựa từ **Bắt đầu từ quyết định, không bắt đầu từ chỉ số (metric / 지표)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá thành phần và đánh giá đầu-cuối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Đánh giá thành phần và đánh giá đầu-cuối** tiếp nhận điểm tựa từ **Hợp đồng đánh giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá offline và online** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Mỗi thành phần cần chỉ số (metric / 지표) riêng để chẩn đoán, nhưng người dùng trải nghiệm kết quả đầu-cuối.

Ví dụ:

```text
retrieval Recall@k cao
nhưng context packing cắt mất đoạn quyết định
→ câu trả lời cuối vẫn sai
```

Ngược lại, câu trả lời đúng một lần không chứng minh retriever tốt; mô hình có thể trả lời từ kiến thức sẵn có hoặc đoán đúng.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Đánh giá offline và online** tiếp nhận điểm tựa từ **Đánh giá thành phần và đánh giá đầu-cuối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tập kiểm thử và rò rỉ đánh giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá offline và online

**Đánh giá offline (offline evaluation)** chạy trên dữ liệu hoặc môi trường mô phỏng cố định. Nó nhanh, có thể lặp lại và phù hợp để làm cổng phát hành.

**Đánh giá online (online evaluation)** đo hành vi trên lưu lượng thật thông qua shadow triển khai (deployment / 배포), canary, A/B testing, kết quả (outcome / 결과) nghiệp vụ hoặc phản hồi có kiểm soát.

Luồng môi trường vận hành (production / 운영 환경) hợp lý thường là:

```text
offline regression suite
→ adversarial / safety suite
→ shadow
→ canary
→ online monitoring
```

Không nên dùng môi trường vận hành (production / 운영 환경) traffic như nơi đầu tiên phát hiện lỗi có thể tìm được bằng kiểm thử offline.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Tập kiểm thử và rò rỉ đánh giá** tiếp nhận điểm tựa từ **Đánh giá offline và online** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thiết kế kịch bản thay vì chỉ thiết kế câu hỏi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tập kiểm thử và rò rỉ đánh giá

Tập kiểm thử (test / 테스트) phải đại diện cho phân phối sử dụng dự kiến và được tách khỏi vòng tối ưu. Nếu nhóm phát triển xem lỗi trên kiểm thử (test / 테스트) rồi sửa prompt, mô hình (model / 모델) hoặc retrieval nhiều lần, tập đó đã trở thành tập phát triển.

Khi đó cần holdout mới hoặc tập kiểm thử ẩn.

Với LLM, contamination còn có thể đến từ pretraining hoặc dữ liệu tổng hợp. Vì vậy benchmark công khai chỉ là một bằng chứng, không phải phép đo tuyệt đối về năng lực tổng quát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Thiết kế kịch bản thay vì chỉ thiết kế câu hỏi** tiếp nhận điểm tựa từ **Tập kiểm thử và rò rỉ đánh giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chọn chỉ số (metric / 지표) theo loại bài toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thiết kế kịch bản thay vì chỉ thiết kế câu hỏi

Hệ thống môi trường vận hành (production / 운영 환경) cần **kịch bản (scenario)** bao phủ trạng thái và dạng thất bại (failure mode / 실패 모드) thật:

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

Mỗi kịch bản nên có bất biến (invariant / 불변식) và acceptance criterion rõ. Với tác nhân (agent / 에이전트), không nhất thiết yêu cầu trajectory giống hệt nhau; có thể yêu cầu các bất biến (invariant / 불변식) như “không ghi dữ liệu trước approval” hoặc “mọi mutation phải được verify”.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Chọn chỉ số (metric / 지표) theo loại bài toán** tiếp nhận điểm tựa từ **Thiết kế kịch bản thay vì chỉ thiết kế câu hỏi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác toán học về expected mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chọn chỉ số (metric / 지표) theo loại bài toán

Classification thường dùng accuracy, precision, recall, F1, ROC-AUC, PR-AUC, log mất mát (loss / 손실) và calibration.

Regression thường dùng MAE, MSE/RMSE hoặc quantile mất mát (loss / 손실).

Ranking và retrieval thường dùng Recall@k, Precision@k, MRR và nDCG.

Generation cần các phép đo như tính đúng ngữ nghĩa, mức hỗ trợ bởi nguồn, tính đầy đủ, tuân thủ lược đồ (schema / 스키마) và đánh giá của con người.

Tác nhân (agent / 에이전트) cần đo thêm tác vụ (task / 작업) success, số bước, lỗi công cụ, verified completion, số mutation, quay lui (rollback / 롤백), độ trễ (latency / 지연 시간) và chi phí (cost / 비용).

Không có chỉ số (metric / 지표) đơn lẻ nào đủ cho hệ thống đa thành phần.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Trực giác toán học về expected mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Chọn chỉ số (metric / 지표) theo loại bài toán** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Threshold là một phần của chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác toán học về expected mất mát (loss / 손실)

Đánh giá nên gắn với chi phí lỗi. Với ma trận chi phí `C`, tổn thất kỳ vọng có thể viết:

\[
E[C]=\sum_{i,j}P(y=i,\hat y=j)C_{ij}
\]

Điều này giải thích vì sao hai mô hình có cùng accuracy vẫn có giá trị kinh doanh rất khác nhau nếu loại lỗi của chúng khác nhau.

Với workflow hoặc tác nhân (agent / 에이전트), có thể mở rộng trực giác:

\[
Utility = giá trị (value / 값)(success)-Cost(compute)-Cost(latency)-Expected\ mất mát (loss / 손실)(failure)
\]

Không cần một công thức duy nhất cho mọi sản phẩm; điều quan trọng là đưa sự đánh đổi (trade-off / 트레이드오프) ra thành biến có thể quan sát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Threshold là một phần của chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Trực giác toán học về expected mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Calibration và khả năng từ chối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Threshold là một phần của chính sách (policy / 정책)

Mô hình xác suất chưa trực tiếp tạo quyết định. chính sách (policy / 정책) còn cần threshold hoặc quy tắc (rule / 규칙).

Một mô hình (model / 모델) có thể giữ nguyên nhưng precision/recall thay đổi mạnh khi threshold đổi. Vì vậy phiên bản (version / 버전) của threshold phải được quản lý cùng triển khai (deployment / 배포), không nên coi `0.5` là mặc định tự nhiên.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Calibration và khả năng từ chối** tiếp nhận điểm tựa từ **Threshold là một phần của chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Slice và long tail** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration và khả năng từ chối

Nếu hệ thống dự đoán xác suất 0.8 cho nhiều trường hợp, khoảng 80% trong nhóm đó có đúng không? Đây là câu hỏi về **hiệu chỉnh xác suất (calibration)**.

Calibration đặc biệt hữu ích khi hệ thống có vùng từ chối:

```text
độ tin cậy cao   → tự động xử lý
độ tin cậy trung bình → thêm verifier
độ tin cậy thấp → human review / abstain
```

Với LLM sinh văn bản, đơn vị từ (token / 토큰) xác suất (probability / 확률) không phải xác suất “câu trả lời đúng”. Cần verifier, bằng chứng (evidence / 증거) và thước đo đặc thù tác vụ (task / 작업) thay vì dùng logit làm confidence trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Slice và long tail** tiếp nhận điểm tựa từ **Calibration và khả năng từ chối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ bất định thống kê** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Rare trường hợp (case / 사례) có tác động cao cần kịch bản riêng. Ví dụ payment tác nhân (agent / 에이전트) đạt 99% tác vụ (task / 작업) success vẫn chưa đủ nếu 1% lỗi có thể gây giao dịch trùng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Độ bất định thống kê** tiếp nhận điểm tựa từ **Slice và long tail** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai của một evaluation chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ bất định thống kê

Chỉ số (metric / 지표) là ước lượng từ mẫu hữu hạn. Khi chênh lệch nhỏ, nên dùng confidence interval, bootstrap hoặc repeated run.

Với tỷ lệ thành công `p` được ước lượng từ `n` trường hợp độc lập, sai số chuẩn trực giác gần:

\[
SE\approx\sqrt{\frac{p(1-p)}{n}}
\]

Do đó cải thiện 0.2% trên tập nhỏ có thể chỉ là nhiễu.

Với hệ thống sinh ngẫu nhiên, cần chạy nhiều mẫu (sample / 표본) hoặc seed để đo cả trung bình lẫn variance.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Độ bất định thống kê** xác định đầu vào; **Mô hình triển khai của một evaluation chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **LLM-as-Judge và giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai của một evaluation chuỗi xử lý (pipeline / 파이프라인)

Một chuỗi xử lý (pipeline / 파이프라인) thực dụng có thể là:

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

Mỗi kết quả phải truy được về phiên bản (version / 버전) của mô hình (model / 모델), prompt, retrieval chỉ mục (index / 인덱스), công cụ (tool / 도구) lược đồ (schema / 스키마) và chính sách (policy / 정책). Nếu không, regression rất khó tái hiện.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Mô hình triển khai của một evaluation chuỗi xử lý (pipeline / 파이프라인)** đã nêu tiêu chí phân biệt, còn **LLM-as-Judge và giới hạn** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Regression testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM-as-Judge và giới hạn

Mô hình làm giám khảo (LLM-as-Judge) hữu ích cho relevance, style hoặc completeness, nhưng có thể bị thiên lệch vị trí, độ dài, phong cách và lỗi tương quan với mô hình (model / 모델) được chấm.

Dùng nó như một evaluator có sai số, không phải oracle. Nên hiệu chỉnh với human/tham chiếu (reference / 참조) set và ưu tiên deterministic validator cho các thuộc tính (property / 속성) có thể kiểm trực tiếp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **LLM-as-Judge và giới hạn** đã nêu tiêu chí phân biệt, còn **Regression testing** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Thất bại (failure / 실패) taxonomy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Regression testing

Evaluation suite phải trở thành cổng phát hành. Mỗi sự cố (incident / 인시던트) môi trường vận hành (production / 운영 환경) hoặc bug nghiêm trọng nên được chuyển thành regression trường hợp (case / 사례) mới.

Luồng học từ lỗi:

```text
incident
→ root cause
→ reproducible scenario
→ thêm vào eval suite
→ fix
→ xác nhận không regress
```

Nhờ đó kiến thức (knowledge / 지식) vận hành tích lũy thành kiểm thử (test / 테스트) thay vì chỉ nằm trong postmortem.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Thất bại (failure / 실패) taxonomy** tiếp nhận điểm tựa từ **Regression testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프) trong đánh giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) taxonomy

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

Taxonomy giúp biết cần sửa dữ liệu (data / 데이터), retriever, prompt, mô hình (model / 모델), công cụ (tool / 도구) hay thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Sự đánh đổi (trade-off / 트레이드오프) trong đánh giá** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) taxonomy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) của chính hệ thống đánh giá** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프) trong đánh giá

Bộ kiểm thử càng rộng thì chi phí chạy càng cao. Human evaluation chất lượng cao nhưng chậm; automated judge nhanh nhưng có độ lệch (bias / 편향). Hidden set tốt cho tính khách quan nhưng khó gỡ lỗi (debug / 디버그). môi trường vận hành (production / 운영 환경) A/B phản ánh thực tế nhưng có rủi ro ảnh hưởng người dùng.

Do đó nên dùng nhiều tầng:

```text
nhanh/rẻ → chạy mỗi commit
trung bình → chạy trước release
đắt/sâu → chạy định kỳ hoặc trước thay đổi lớn
online → xác nhận sau rollout có kiểm soát
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Dạng thất bại (failure mode / 실패 모드) của chính hệ thống đánh giá** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프) trong đánh giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng trong môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) của chính hệ thống đánh giá

Evaluation cũng có thể sai vì:

- benchmark contamination;
- label hoặc rubric mơ hồ;
- kiểm thử (test / 테스트) set không đại diện;
- evaluator mô hình (model / 모델) thiên lệch;
- chỉ số (metric / 지표) bị tối ưu quá mức;
- thiếu slice có rủi ro cao;
- dữ liệu eval lỗi thời;
- kiểm thử (test / 테스트) chỉ kiểm happy đường dẫn (path / 경로).

Một score cao chỉ có ý nghĩa trong phạm vi coverage mà evaluation thực sự kiểm tra.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Dùng trong môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Dạng thất bại (failure mode / 실패 모드) của chính hệ thống đánh giá** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng trong môi trường vận hành (production / 운영 환경)

Evaluation phục vụ ba mục tiêu khác nhau:

```text
phát triển      → so sánh giả thuyết
phát hành       → release gate
vận hành        → phát hiện regression và drift
```

Không nên chỉ xây benchmark một lần rồi bỏ. Eval suite phải có phiên bản (version / 버전), đơn vị sở hữu (owner / 오너), coverage map và lịch cập nhật dựa trên tải công việc (workload / 워크로드) thực tế.

> **Chuyển mạch:** Ở chặng này của **Nền tảng đánh giá hệ thống AI**, **Mô hình tư duy** gom các mảnh từ **Dùng trong môi trường vận hành (production / 운영 환경)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Evaluation là bằng chứng về hành vi dưới một phân phối và một hợp đồng đã xác định; nó không phải chứng nhận rằng hệ thống “thông minh” hoặc “an toàn” trong mọi tình huống.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Nền tảng đánh giá hệ thống AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Benchmark cao nghĩa môi trường vận hành (production / 운영 환경) tốt”

Không. môi trường vận hành (production / 운영 환경) dữ liệu (data / 데이터), công cụ (tool / 도구), trạng thái (state / 상태) và độ trễ (latency / 지연 시간) đặc tả hợp đồng (contract / 계약) có thể khác benchmark.

### “Một chỉ số (metric / 지표) là đủ”

Không. Chất lượng, calibration, độ trễ (latency / 지연 시간), chi phí (cost / 비용), độ tin cậy (reliability / 신뢰성) và an toàn (safety / 안전) là nhiều trục khác nhau.

### “Final answer đúng là đủ cho tác nhân (agent / 에이전트)”

Không. Trajectory có thể dùng sai quyền, tạo side tác động (effect / 효과) rồi quay lui (rollback / 롤백) hoặc vượt ngân sách.

### “LLM judge thay thế được kiểm thử (test / 테스트) xác định”

Không. tệp (file / 파일) tồn tại hay không, lược đồ (schema / 스키마) hợp lệ hay không, giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) hay chưa nên được kiểm bằng hệ thống xác định.

> **Chuyển mạch:** Trong **Nền tảng đánh giá hệ thống AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Đọc tiếp [Metrics, Benchmarks và Test Design](./01_metrics_benchmarks_and_test_design.md), [Uncertainty và Calibration](./02_uncertainty_and_calibration.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md), [Red Teaming](./06_red_teaming_and_adversarial_evaluation.md) và [Reliability Engineering](./07_reliability_engineering.md).

Các evaluation chuyên biệt nằm tại [RAG Evaluation](../09_retrieval_and_rag/09_rag_evaluation.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [LLMOps](../16_mlops_and_llmops/08_llmops.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
