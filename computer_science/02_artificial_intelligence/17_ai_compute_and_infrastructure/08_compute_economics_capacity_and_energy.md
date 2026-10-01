# Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Accelerator-Hour** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chi phí trên đơn vị từ (token / 토큰), suy luận (inference / 추론) và tác vụ (task / 작업)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hạ tầng AI không chỉ là bài toán hiệu năng mà còn là bài toán kinh tế. Một hệ thống phải đạt chất lượng (quality / 품질) và SLO trong giới hạn ngân sách (budget / 예산), power, availability và năng lực vận hành của nhóm (team / 팀). **Kinh tế tính toán (compute economics)** hỏi: mỗi đơn vị công việc hữu ích tiêu tốn bao nhiêu tài nguyên và chi phí?

## Accelerator-Hour

Huấn luyện (training / 학습) chi phí (cost / 비용) thường được nhìn theo accelerator-hour:

\[
chi phí (cost / 비용)\approx devices\times hours\times price/device-hour
\]

Nhưng raw device-hour chưa phản ánh utilization. Một huấn luyện (training / 학습) job dùng 100 GPU nhưng 40% thời gian idle vì communication vẫn phải trả toàn bộ chi phí.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Chi phí trên đơn vị từ (token / 토큰), suy luận (inference / 추론) và tác vụ (task / 작업)** tiếp nhận điểm tựa từ **Accelerator-Hour** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí đã điều chỉnh theo Chất lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí trên đơn vị từ (token / 토큰), suy luận (inference / 추론) và tác vụ (task / 작업)

Serving nên đo chi phí gần nghiệp vụ (business / 비즈니스) đơn vị (unit / 단위) hơn:

```text
cost / 1k tokens
cost / request
cost / completed task
cost / successful agent trajectory
```

Chi phí (cost / 비용)/yêu cầu (request / 요청) có thể gây hiểu sai nếu độ dài đơn vị từ (token / 토큰) giữa các yêu cầu (request / 요청) rất khác nhau.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Chi phí đã điều chỉnh theo Chất lượng** tiếp nhận điểm tựa từ **Chi phí trên đơn vị từ (token / 토큰), suy luận (inference / 추론) và tác vụ (task / 작업)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Utilization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí đã điều chỉnh theo Chất lượng

Mô hình rẻ hơn chưa chắc thật sự rẻ nếu thất bại (failure / 실패), thử lại (retry / 재시도) hoặc escalation tăng.

Một chỉ số (metric / 지표) khái niệm hữu ích:

\[
chi phí (cost / 비용)\ per\ successful\ tác vụ (task / 작업)=\frac{Total\ chi phí (cost / 비용)}{Verified\ successful\ tasks}
\]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Utilization** tiếp nhận điểm tựa từ **Chi phí đã điều chỉnh theo Chất lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reserved, On-Demand và Spot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Utilization

Accelerator idle vẫn tiêu tốn capex hoặc cloud chi phí (cost / 비용). Tuy nhiên online fleet cần headroom để giữ độ trễ (latency / 지연 시간) SLO.

Batch hoặc huấn luyện (training / 학습) cluster thường có thể chạy utilization cao hơn serving fleet.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Reserved, On-Demand và Spot** tiếp nhận điểm tựa từ **Utilization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tự xây hay Thuê** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reserved, On-Demand và Spot

Cloud economics thường có sự đánh đổi (trade-off / 트레이드오프):

- on-demand: linh hoạt nhưng đắt;
- reserved/committed: rẻ hơn nhưng ít linh hoạt;
- spot/preemptible: rẻ nhưng có thể bị thu hồi.

Huấn luyện (training / 학습) tải công việc (workload / 워크로드) có checkpoint phù hợp với spot hơn latency-sensitive serving.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Tự xây hay Thuê** tiếp nhận điểm tựa từ **Reserved, On-Demand và Spot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của mô hình (model / 모델) kích thước (size / 크기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Quyết định phụ thuộc quy mô (scale / 규모), khả năng dự đoán utilization và chuyên môn của nhóm (team / 팀).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Economics của mô hình (model / 모델) kích thước (size / 크기)** tiếp nhận điểm tựa từ **Tự xây hay Thuê** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của ngữ cảnh (context / 맥락) Length** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của mô hình (model / 모델) kích thước (size / 크기)

Mô hình lớn hơn thường làm tăng:

- weight bộ nhớ (memory / 메모리);
- số accelerator cần thiết;
- suy luận (inference / 추론) độ trễ (latency / 지연 시간);
- năng lượng;
- chi phí (cost / 비용)/đơn vị từ (token / 토큰).

Chất lượng (quality / 품질) gain từ scaling phải đủ lớn để biện minh cho total chi phí (cost / 비용). mô hình (model / 모델) routing hoặc specialized mô hình (model / 모델) có thể tạo Pareto improvement tốt hơn.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Economics của ngữ cảnh (context / 맥락) Length** tiếp nhận điểm tựa từ **Economics của mô hình (model / 모델) kích thước (size / 크기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của ngữ cảnh (context / 맥락) Length

Long ngữ cảnh (context / 맥락) làm prefill compute và KV bộ nhớ đệm (cache / 캐시) tăng. “Hỗ trợ ngữ cảnh (context / 맥락) 1M đơn vị từ (token / 토큰)” không nghĩa mọi yêu cầu (request / 요청) đều nên gửi 1M đơn vị từ (token / 토큰).

Ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링) hoặc retrieval thường rẻ hơn việc append toàn bộ dữ liệu một cách brute-force.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Economics của tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Economics của ngữ cảnh (context / 맥락) Length** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) có số bước biến động. Nên đặt ngân sách (budget / 예산):

```text
max LLM calls
max tokens
max tool spend
max wall time
```

Nếu không có guardrail, một số trajectory runaway hiếm có thể chiếm phần lớn hóa đơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Economics của RAG** tiếp nhận điểm tựa từ **Economics của tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của RAG

RAG làm phát sinh chi phí embedding, chỉ mục (index / 인덱스) và reranking, nhưng có thể giảm nhu cầu dùng mô hình (model / 모델) lớn hơn hoặc fine-tuning, đồng thời tăng grounding.

Có thể tách chi phí (cost / 비용) thành:

```text
ingestion được amortize
retrieval trên mỗi query
reranking
extra context tokens
generation
```

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Economics của huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Economics của RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Opportunity chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của huấn luyện (training / 학습)

Pretraining từ đầu rất đắt. lĩnh vực (domain / 도메인) adaptation thường ưu tiên:

- SFT;
- LoRA hoặc PEFT;
- distillation;
- retrieval.

Lựa chọn đúng phụ thuộc nhu cầu là hành vi (behavior / 동작) adaptation, kiến thức (knowledge / 지식) freshness hay kiểm soát kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Opportunity chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Economics của huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Power** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Opportunity chi phí (cost / 비용)

GPU được dùng cho một experiment thì không còn sẵn cho môi trường vận hành (production / 운영 환경) hoặc research khác. Priority của scheduler nên phản ánh nghiệp vụ (business / 비즈니스) giá trị (value / 값) thay vì chỉ first-come-first-served.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Power** tiếp nhận điểm tựa từ **Opportunity chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hiệu quả năng lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Power

Power consumption ảnh hưởng trực tiếp operating chi phí (cost / 비용) và datacenter sức chứa (capacity / 용량). TDP của accelerator không phải toàn bộ hệ thống (system / 시스템) power; mạng (network / 네트워크), CPU và cooling cũng tiêu thụ năng lượng.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Hiệu quả năng lượng** tiếp nhận điểm tựa từ **Power** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ràng buộc nhiệt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hiệu quả năng lượng

Các chỉ số (metric / 지표) có thể gồm:

```text
tokens / joule
inferences / watt
training progress / energy
```

Precision thấp hơn và kernel tối ưu có thể cải thiện cả chi phí (cost / 비용) lẫn năng lượng (energy / 에너지) efficiency.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Ràng buộc nhiệt** tiếp nhận điểm tựa từ **Hiệu quả năng lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Carbon Accounting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ràng buộc nhiệt

Accelerator mật độ cao cần hệ thống cooling phù hợp. Thermal throttling có thể làm hiệu năng (performance / 성능) giảm. Vì vậy hạ tầng (infrastructure / 인프라) thiết kế (design / 설계) phải xét power delivery và cooling, không chỉ máy chủ (server / 서버).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Carbon Accounting** tiếp nhận điểm tựa từ **Ràng buộc nhiệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Depreciation và vòng đời Hardware** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Carbon Accounting

Environmental impact phụ thuộc nguồn điện, utilization, quá trình sản xuất hardware và tải công việc (workload / 워크로드) efficiency. Chỉ nhìn operational năng lượng (energy / 에너지) là chưa đầy đủ nhưng vẫn có thể đo được.

Không nên gán một giá trị carbon cố định cho mọi mô hình (model / 모델) lời gọi (call / 호출) vì region, hardware và utilization khác nhau.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Depreciation và vòng đời Hardware** tiếp nhận điểm tựa từ **Carbon Accounting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) Planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Depreciation và vòng đời Hardware

Accelerator lỗi thời nhanh khi thế hệ mới có hiệu năng (performance / 성능)/watt tốt hơn. Economics của cluster sở hữu cần tính depreciation và khả năng tái sử dụng hoặc resale sau vòng đời chính.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Sức chứa (capacity / 용량) Planning** tiếp nhận điểm tựa từ **Depreciation và vòng đời Hardware** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị (unit / 단위) Economics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) Planning

Sức chứa (capacity / 용량) forecast nên mô hình hóa:

```text
traffic growth
model growth
context / output length
batching efficiency
new features
failure headroom
training campaigns
```

Nếu mô hình (model / 모델) kích thước (size / 크기) tăng gấp đôi mỗi quý, chỉ nhìn số GPU dư hiện tại là không đủ để forecast.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Đơn vị (unit / 단위) Economics** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) Planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ tự tối ưu về Economics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị (unit / 단위) Economics

Với sản phẩm AI, cần nối hạ tầng (infrastructure / 인프라) chi phí (cost / 비용) với nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과):

```text
revenue / value trên mỗi successful task
- compute / API / storage cost
- human review cost
- failure cost
```

Suy luận (inference / 추론) rẻ nhưng tạo ít giá trị không tự động là nghiệp vụ (business / 비즈니스) tốt.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Thứ tự tối ưu về Economics** tiếp nhận điểm tựa từ **Đơn vị (unit / 단위) Economics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự tối ưu về Economics

Các đòn bẩy thường có hiệu quả cao theo thứ tự:

1. loại bỏ lời gọi (call / 호출) không cần thiết;
2. cải thiện routing và caching;
3. giảm ngữ cảnh (context / 맥락) và đầu ra (output / 출력);
4. chọn đúng mô hình (model / 모델);
5. tăng batching và hardware utilization;
6. quantize hoặc compress;
7. tối ưu kernel thấp tầng.

> **Chuyển mạch:** Ở chặng này của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Mô hình tư duy** gom các mảnh từ **Thứ tự tối ưu về Economics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Compute economics = lượng công việc hữu ích đã điều chỉnh theo chất lượng trên mỗi tài nguyên khan hiếm.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “API có giá rẻ nhất nghĩa là hệ thống (system / 시스템) rẻ nhất”

Không. thử lại (retry / 재시도), chất lượng (quality / 품질), công cụ (tool / 도구) lời gọi (call / 호출) và operational chi phí (cost / 비용) đều ảnh hưởng.

### “Utilization cao nhất luôn tối ưu về kinh tế”

Không. Serving cần headroom; vi phạm SLO cũng có chi phí.

### “năng lượng (energy / 에너지) efficiency chỉ là chủ đề môi trường”

Không. Nó ảnh hưởng trực tiếp datacenter power, thermal limit và chi phí vận hành.

> **Chuyển mạch:** Trong **Compute Economics, sức chứa (capacity / 용량) và năng lượng (energy / 에너지)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Latency/Throughput/Cost](../15_ai_engineering/09_latency_throughput_and_cost.md), [Model Compression](../15_ai_engineering/08_model_compression.md), [Cluster Scheduling](./07_cluster_scheduling_and_interconnect.md) và [Ethics/Governance](../19_ai_safety_security_alignment/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
