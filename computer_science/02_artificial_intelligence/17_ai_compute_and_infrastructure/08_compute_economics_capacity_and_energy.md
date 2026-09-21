# Compute Economics, Capacity và Energy

Hạ tầng AI không chỉ là bài toán hiệu năng mà còn là bài toán kinh tế. Một hệ thống phải đạt quality và SLO trong giới hạn budget, power, availability và năng lực vận hành của team. **Kinh tế tính toán (compute economics)** hỏi: mỗi đơn vị công việc hữu ích tiêu tốn bao nhiêu tài nguyên và chi phí?

## Accelerator-Hour

Training cost thường được nhìn theo accelerator-hour:

\[
Cost\approx devices\times hours\times price/device-hour
\]

Nhưng raw device-hour chưa phản ánh utilization. Một training job dùng 100 GPU nhưng 40% thời gian idle vì communication vẫn phải trả toàn bộ chi phí.

## Chi phí trên Token, Inference và Task

Serving nên đo chi phí gần business unit hơn:

```text
cost / 1k tokens
cost / request
cost / completed task
cost / successful agent trajectory
```

Cost/request có thể gây hiểu sai nếu độ dài token giữa các request rất khác nhau.

## Chi phí đã điều chỉnh theo Chất lượng

Mô hình rẻ hơn chưa chắc thật sự rẻ nếu failure, retry hoặc escalation tăng.

Một metric khái niệm hữu ích:

\[
Cost\ per\ successful\ task=\frac{Total\ cost}{Verified\ successful\ tasks}
\]

## Utilization

Accelerator idle vẫn tiêu tốn capex hoặc cloud cost. Tuy nhiên online fleet cần headroom để giữ latency SLO.

Batch hoặc training cluster thường có thể chạy utilization cao hơn serving fleet.

## Reserved, On-Demand và Spot

Cloud economics thường có trade-off:

- on-demand: linh hoạt nhưng đắt;
- reserved/committed: rẻ hơn nhưng ít linh hoạt;
- spot/preemptible: rẻ nhưng có thể bị thu hồi.

Training workload có checkpoint phù hợp với spot hơn latency-sensitive serving.

## Tự xây hay Thuê

Cluster tự sở hữu:

```text
+ marginal cost thấp hơn khi utilization cao
+ kiểm soát hardware và vận hành
- capex lớn
- gánh nặng operations
- rủi ro underutilization và obsolescence
```

Cloud:

```text
+ elasticity
+ tiếp cận hardware mới nhanh
- unit price cao hơn
- phụ thuộc provider và egress cost
```

Quyết định phụ thuộc scale, khả năng dự đoán utilization và chuyên môn của team.

## Economics của Model Size

Mô hình lớn hơn thường làm tăng:

- weight memory;
- số accelerator cần thiết;
- inference latency;
- năng lượng;
- cost/token.

Quality gain từ scaling phải đủ lớn để biện minh cho total cost. Model routing hoặc specialized model có thể tạo Pareto improvement tốt hơn.

## Economics của Context Length

Long context làm prefill compute và KV cache tăng. “Hỗ trợ context 1M token” không nghĩa mọi request đều nên gửi 1M token.

Context engineering hoặc retrieval thường rẻ hơn việc append toàn bộ dữ liệu một cách brute-force.

## Economics của Agent

Agent loop có số bước biến động. Nên đặt budget:

```text
max LLM calls
max tokens
max tool spend
max wall time
```

Nếu không có guardrail, một số trajectory runaway hiếm có thể chiếm phần lớn hóa đơn.

## Economics của RAG

RAG làm phát sinh chi phí embedding, index và reranking, nhưng có thể giảm nhu cầu dùng model lớn hơn hoặc fine-tuning, đồng thời tăng grounding.

Có thể tách cost thành:

```text
ingestion được amortize
retrieval trên mỗi query
reranking
extra context tokens
generation
```

## Economics của Training

Pretraining từ đầu rất đắt. Domain adaptation thường ưu tiên:

- SFT;
- LoRA hoặc PEFT;
- distillation;
- retrieval.

Lựa chọn đúng phụ thuộc nhu cầu là behavior adaptation, knowledge freshness hay kiểm soát architecture.

## Opportunity Cost

GPU được dùng cho một experiment thì không còn sẵn cho production hoặc research khác. Priority của scheduler nên phản ánh business value thay vì chỉ first-come-first-served.

## Power

Power consumption ảnh hưởng trực tiếp operating cost và datacenter capacity. TDP của accelerator không phải toàn bộ system power; network, CPU và cooling cũng tiêu thụ năng lượng.

## Hiệu quả năng lượng

Các metric có thể gồm:

```text
tokens / joule
inferences / watt
training progress / energy
```

Precision thấp hơn và kernel tối ưu có thể cải thiện cả cost lẫn energy efficiency.

## Ràng buộc nhiệt

Accelerator mật độ cao cần hệ thống cooling phù hợp. Thermal throttling có thể làm performance giảm. Vì vậy infrastructure design phải xét power delivery và cooling, không chỉ server.

## Carbon Accounting

Environmental impact phụ thuộc nguồn điện, utilization, quá trình sản xuất hardware và workload efficiency. Chỉ nhìn operational energy là chưa đầy đủ nhưng vẫn có thể đo được.

Không nên gán một giá trị carbon cố định cho mọi model call vì region, hardware và utilization khác nhau.

## Depreciation và vòng đời Hardware

Accelerator lỗi thời nhanh khi thế hệ mới có performance/watt tốt hơn. Economics của cluster sở hữu cần tính depreciation và khả năng tái sử dụng hoặc resale sau vòng đời chính.

## Capacity Planning

Capacity forecast nên mô hình hóa:

```text
traffic growth
model growth
context / output length
batching efficiency
new features
failure headroom
training campaigns
```

Nếu model size tăng gấp đôi mỗi quý, chỉ nhìn số GPU dư hiện tại là không đủ để forecast.

## Unit Economics

Với sản phẩm AI, cần nối infrastructure cost với business outcome:

```text
revenue / value trên mỗi successful task
- compute / API / storage cost
- human review cost
- failure cost
```

Inference rẻ nhưng tạo ít giá trị không tự động là business tốt.

## Thứ tự tối ưu về Economics

Các đòn bẩy thường có hiệu quả cao theo thứ tự:

1. loại bỏ call không cần thiết;
2. cải thiện routing và caching;
3. giảm context và output;
4. chọn đúng model;
5. tăng batching và hardware utilization;
6. quantize hoặc compress;
7. tối ưu kernel thấp tầng.

## Mô hình tư duy

```text
Compute economics = lượng công việc hữu ích đã điều chỉnh theo chất lượng trên mỗi tài nguyên khan hiếm.
```

## Những nhầm lẫn thường gặp

### “API có giá rẻ nhất nghĩa là system rẻ nhất”

Không. Retry, quality, tool call và operational cost đều ảnh hưởng.

### “Utilization cao nhất luôn tối ưu về kinh tế”

Không. Serving cần headroom; vi phạm SLO cũng có chi phí.

### “Energy efficiency chỉ là chủ đề môi trường”

Không. Nó ảnh hưởng trực tiếp datacenter power, thermal limit và chi phí vận hành.

## Liên kết kiến thức

Xem [Latency/Throughput/Cost](../15_ai_engineering/09_latency_throughput_and_cost.md), [Model Compression](../15_ai_engineering/08_model_compression.md), [Cluster Scheduling](./07_cluster_scheduling_and_interconnect.md) và [Ethics/Governance](../20_ethics_governance_and_society/README.md).