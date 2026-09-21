# AI Engineering

**Kỹ thuật AI (AI Engineering / AI 엔지니어링)** là lĩnh vực biến mô hình (model), dữ liệu và các thành phần AI thành một hệ thống có thể vận hành ổn định, nhanh, có chi phí kiểm soát được, quan sát được (observable) và bảo trì được trong môi trường production. Chất lượng mô hình chỉ là một thành phần; trải nghiệm người dùng và độ tin cậy của hệ thống còn phụ thuộc toàn bộ pipeline xung quanh.

```text
Dữ liệu / yêu cầu
→ tiền xử lý / truy xuất
→ suy luận của mô hình
→ hậu xử lý / chính sách
→ phản hồi / hành động
→ ghi log / phản hồi học tập
```

## Mô hình không đồng nghĩa sản phẩm

Một mô hình có điểm benchmark cao vẫn có thể tạo ra sản phẩm kém nếu:

- độ trễ (latency) quá cao;
- ngữ cảnh hoặc truy xuất sai;
- timeout xảy ra thường xuyên;
- chi phí trên mỗi yêu cầu không bền vững;
- schema đầu ra không ổn định;
- deployment thiếu cơ chế dự phòng (fallback);
- vi phạm quyền riêng tư hoặc bảo mật.

Kỹ thuật AI tối ưu **toàn bộ hệ thống end-to-end**, không chỉ metric của mô hình.

## Huấn luyện Offline và phục vụ Online

Huấn luyện (training) thường tối ưu thông lượng (throughput) trên batch lớn và có thể chạy nhiều giờ hoặc nhiều ngày. Phục vụ suy luận (serving) thường cần độ trễ thấp, traffic biến động và yêu cầu availability nghiêm ngặt.

Cùng một mô hình nhưng các ràng buộc runtime có thể hoàn toàn khác nhau.

## Các thành phần của hệ thống AI

Một kiến trúc điển hình:

```text
API Gateway
→ kiểm tra yêu cầu
→ đặc trưng / ngữ cảnh / truy xuất
→ bộ định tuyến mô hình (model router)
→ dịch vụ suy luận
→ kiểm tra đầu ra / guardrail
→ cache / lưu trữ
→ quan sát hệ thống (observability)
```

Hệ thống Agent hoặc RAG còn bổ sung công cụ (tool), kho trạng thái (state store), tìm kiếm vector và orchestration.

## Contract-First Inference

Mô hình production nên có hợp đồng input/output rõ ràng:

```json
{
  "model_version": "fraud-v12",
  "input": {"transaction_id":"...", "features": {...}},
  "output": {"score":0.87, "decision":"review"}
}
```

Kiểm tra schema giúp tránh trường hợp hệ thống âm thầm chấp nhận dữ liệu sai định dạng.

## Lớp xác định và lớp xác suất

Một kiến trúc đáng tin cậy thường có dạng:

```text
Kiểm tra có tính xác định
→ mô hình xác suất
→ chính sách / ràng buộc có tính xác định
```

Ví dụ mô hình trả về xác suất gian lận; business rule quyết định threshold và luồng approval.

## AI đồng bộ và bất đồng bộ

Chat hoặc search tương tác thường cần phản hồi đồng bộ (synchronous). Phân tích tài liệu lớn, xử lý video hoặc tạo embedding theo lô thường phù hợp với job bất đồng bộ (asynchronous).

Không nên ép tác vụ dài chạy trọn trong một HTTP request duy nhất.

## Định tuyến mô hình

Các loại task khác nhau có thể dùng các mô hình khác nhau:

```text
mô hình nhỏ, rẻ → classification / extraction
mô hình lớn → reasoning khó
embedding model → retrieval
vision model → image
```

Bộ định tuyến (router) có thể dựa trên loại task, confidence, latency budget hoặc cost budget.

## Cơ chế dự phòng

Hệ thống AI production nên định nghĩa rõ đường đi khi lỗi xảy ra:

- mô hình hoặc provider thứ hai;
- fallback dựa trên rule;
- kết quả đã cache;
- human review;
- phản hồi giảm cấp có kiểm soát (graceful degradation).

Fallback không nên âm thầm thay đổi semantics của tác vụ.

## Độ tin cậy và khả năng từ chối trả lời

Với classification, hệ thống có thể từ chối quyết định khi uncertainty cao. Với Generative AI, confidence khó đo hơn; nên dựa vào bằng chứng được grounding, validator và kiểm tra đặc thù theo task thay vì chỉ dùng xác suất token thô.

## Data Plane và Control Plane

**Mặt phẳng dữ liệu (data plane)** xử lý request và inference của người dùng.

**Mặt phẳng điều khiển (control plane)** quản lý model version, rollout, configuration, routing, policy và monitoring.

Tách hai lớp này giúp deployment và rollback an toàn hơn.

## Model Artifact

Artifact dùng để triển khai không chỉ gồm weights:

```text
weights
architecture / config
tokenizer / preprocessor
feature schema
label mapping
runtime dependencies
quantization config
model card / version metadata
```

Sai tokenizer có thể phá hỏng toàn bộ deployment LLM dù weights hoàn toàn đúng.

## Build có khả năng tái lập

Version của container và môi trường nên được cố định đủ chặt để runtime có thể tái lập. Khả năng tương thích giữa GPU driver và library cũng là một phần của compatibility của artifact.

## API và Backpressure

Inference API cần có:

- giới hạn kích thước request;
- timeout;
- giới hạn queue;
- rate limiting;
- cancellation;
- backpressure.

Queue không giới hạn chỉ che giấu tình trạng quá tải cho đến khi latency tăng đột biến.

## SLO

Cần định nghĩa **mục tiêu mức dịch vụ (Service-Level Objective — SLO)** như:

```text
availability
p50 / p95 / p99 latency
error rate
quality metric
cost per request
freshness
```

Quality SLO thường khó đo hơn latency SLO vì label có thể đến trễ.

## Chất lượng AI phụ thuộc ngữ cảnh hệ thống

Độ đúng end-to-end phụ thuộc vào nhiều thành phần:

\[
P(system\ success)=f(data,retrieval,model,policy,tools,environment)
\]

Cải thiện mô hình 2% có thể ít giá trị hơn việc sửa lỗi retrieval recall hoặc lỗi schema.

## Tính nhất quán giữa Offline và Online

Logic feature engineering, tokenization và preprocessing nên được chia sẻ hoặc version hóa giữa training và serving. **Training-serving skew** có thể tạo lỗi âm thầm rất khó phát hiện.

## Shadow Deployment

Mô hình mới nhận bản sao của production traffic nhưng output chưa được dùng để ra quyết định. Nhờ đó có thể so sánh chất lượng và latency trước khi chuyển traffic thật.

## Canary Release

Chỉ route một tỷ lệ traffic nhỏ sang mô hình mới, theo dõi các chỉ số rồi tăng dần nếu ổn định. Cần định nghĩa trigger rollback rõ ràng.

## A/B Testing

A/B testing nên đo cả outcome của người dùng hoặc business, không chỉ offline metric. Guardrail cần bao gồm latency, safety và cost.

## Versioning cho mô hình và cấu hình

Mọi prediction và log nên truy vết được tới model/config version chính xác. Với ứng dụng LLM, nên ghi thêm version của prompt/template, retrieval config và tool khi cần.

## Observability

Cần trace một request xuyên suốt các thành phần:

```text
request
→ latency của feature / retrieval
→ latency của model
→ token usage
→ tool call
→ output validation
```

Metric không đi cùng trace khiến việc tìm root cause trở nên khó khăn.

## Failure Mode đặc thù của AI

- distribution shift;
- model unavailable;
- tokenizer mismatch;
- GPU OOM;
- context overflow;
- structured output bị hallucination;
- embedding hoặc index cũ;
- tool call không hợp lệ;
- batch queue bị bão hòa.

## Chi phí là một ràng buộc kiến trúc

Tổng chi phí gồm:

```text
compute inference
retrieval / storage
network
model API token
human review
training / retraining
idle capacity
```

Mô hình rẻ nhất trên mỗi token chưa chắc tạo ra task hoàn thành rẻ nhất nếu tỷ lệ retry hoặc failure cao.

## Human-in-the-Loop

Human review nên được thiết kế thành workflow có queue, context và escalation rõ ràng, không phải biện pháp chữa cháy thủ công. Nếu governance cho phép, các nhãn review có thể trở thành dữ liệu cải thiện hệ thống về sau.

## Build hay Buy

Dùng external model API giúp triển khai nhanh và giảm gánh nặng hạ tầng; self-hosting cho nhiều quyền kiểm soát hơn và có thể rẻ hơn ở quy mô lớn, nhưng tăng chi phí vận hành.

Quyết định phụ thuộc vào:

- volume;
- privacy;
- latency;
- model customization;
- năng lực phần cứng;
- rủi ro phụ thuộc provider.

## Mô hình tư duy

> **Kỹ thuật AI là Software Engineering trong một hệ thống có thành phần xác suất và hành vi phụ thuộc dữ liệu.**

Mô hình không phải toàn bộ hệ thống; hệ thống phải giới hạn, vận hành và quan sát mô hình.

## Những nhầm lẫn thường gặp

### “Production AI chỉ là deploy một model endpoint”

Không. Hệ thống thực tế còn cần dữ liệu, routing, validation, observability và lifecycle management.

### “Mô hình benchmark cao nhất luôn là lựa chọn production tốt nhất”

Không. Latency, cost và reliability có thể quan trọng hơn.

### “Inference chạy được trên máy local nghĩa là serving đã giải quyết xong”

Không. Concurrency, memory, queueing và các lỗi vận hành chỉ bộc lộ rõ khi có tải thật.

## Liên kết kiến thức

Kỹ thuật AI kết nối [Kiến trúc hệ thống AI](../00_foundations/04_ai_system_architecture.md), Data, Agent/RAG và Software Engineering.

Xem tiếp: [Training Pipeline](./01_training_pipeline.md).