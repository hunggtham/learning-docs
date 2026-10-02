# Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Latency, throughput và cost trong hệ thống AI**. Route đi từ request path → p50/p95/p99 latency → concurrency/throughput → accelerator and token cost → capacity planning, để con số vận hành gắn với trải nghiệm và ngân sách.

Môi trường vận hành (production / 운영 환경) AI không chỉ hỏi “mô hình có chính xác không?” mà còn phải hỏi **mất bao lâu, phục vụ được bao nhiêu yêu cầu (request / 요청) và tốn bao nhiêu tiền**. Ba đại lượng `latency`, `throughput` và `cost` liên hệ chặt chẽ nhưng không cùng hướng tối ưu.

## Độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) là thời gian từ yêu cầu (request / 요청) tới phản hồi (response / 응답). Với Generative AI cần tách:

```text
queue time
preprocessing / context assembly
prefill
TTFT (time to first token)
decode time
postprocessing / tool verification
network overhead
```

Total độ trễ (latency / 지연 시간) có thể cao dù riêng mô hình (model / 모델) suy luận (inference / 추론) rất nhanh.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Tail độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thông lượng (throughput / 처리량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tail độ trễ (latency / 지연 시간)

Average độ trễ (latency / 지연 시간) không đủ. môi trường vận hành (production / 운영 환경) thường theo dõi `p50`, `p95`, `p99`.

Nếu p99 bằng 8 giây, một nhóm người dùng vẫn có trải nghiệm rất kém dù average chỉ 1 giây.

Tail độ trễ (latency / 지연 시간) thường đến từ queueing, straggler, cold start, prompt dài, công cụ (tool / 도구) chậm hoặc noisy neighbor.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Thông lượng (throughput / 처리량)** tiếp nhận điểm tựa từ **Tail độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) và Utilization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thông lượng (throughput / 처리량)

Thông lượng (throughput / 처리량) là lượng công việc hoàn thành trong một đơn vị thời gian:

\[
thông lượng (throughput / 처리량)=\frac{Completed\ công việc (work / 작업)}{thời gian (time / 시간)}
\]

Với LLM có thể đo bằng requests/s hoặc tokens/s.

Batching thường giúp tăng thông lượng (throughput / 처리량) nhưng có thể tăng hàng đợi (queue / 큐) độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Sức chứa (capacity / 용량) và Utilization** tiếp nhận điểm tựa từ **Thông lượng (throughput / 처리량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí trên mỗi yêu cầu (request / 요청)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sức chứa (capacity / 용량) và Utilization

Nếu utilization quá thấp, tài nguyên bị lãng phí. Nếu utilization quá cao, queueing tăng mạnh.

Sức chứa (capacity / 용량) planning cần chừa headroom cho burst và thất bại (failure / 실패).

Autoscaling cũng cần đúng tín hiệu (signal / 신호). CPU utilization không phải lúc nào cũng phản ánh bottleneck ở GPU hoặc KV bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí trên mỗi yêu cầu (request / 요청)** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) và Utilization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của đầu vào (input / 입력) và đầu ra (output / 출력) đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí trên mỗi yêu cầu (request / 요청)

Xấp xỉ:

\[
chi phí (cost / 비용)/yêu cầu (request / 요청)\approx\frac{hạ tầng (infrastructure / 인프라)\ chi phí (cost / 비용)\ per\ thời gian (time / 시간)}{requests\ per\ thời gian (time / 시간)}
\]

Nhưng generative tải công việc (workload / 워크로드) biến động mạnh theo đơn vị từ (token / 토큰) count, vì vậy chi phí (cost / 비용)/đơn vị từ (token / 토큰) hoặc chi phí (cost / 비용)/tác vụ (task / 작업) đôi khi có ý nghĩa hơn chi phí (cost / 비용)/yêu cầu (request / 요청).

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Economics của đầu vào (input / 입력) và đầu ra (output / 출력) đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Chi phí trên mỗi yêu cầu (request / 요청)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí của Chất lượng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của đầu vào (input / 입력) và đầu ra (output / 출력) đơn vị từ (token / 토큰)

Prompt dài làm prefill compute và KV bộ nhớ (memory / 메모리) tăng. đầu ra (output / 출력) dài làm số bước decode tăng.

Hai yêu cầu (request / 요청) đều được tính là “một chat message” nhưng chi phí (cost / 비용) có thể khác nhau hàng chục lần.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí của Chất lượng** tiếp nhận điểm tựa từ **Economics của đầu vào (input / 입력) và đầu ra (output / 출력) đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ trễ (latency / 지연 시간) ngân sách (budget / 예산)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí của Chất lượng

Mô hình lớn hơn có thể tăng chất lượng nhưng đắt hơn. môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) thường dùng:

```text
small/default model
→ confidence/router
→ escalate sang expensive model khi cần
```

Mô hình (model / 모델) routing biến sự đánh đổi (trade-off / 트레이드오프) giữa chất lượng (quality / 품질) và chi phí (cost / 비용) thành một chính sách (policy / 정책) động.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Độ trễ (latency / 지연 시간) ngân sách (budget / 예산)** tiếp nhận điểm tựa từ **Chi phí của Chất lượng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Little's Law và Queueing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ trễ (latency / 지연 시간) ngân sách (budget / 예산)

SLO end-to-end nên chia ngân sách (budget / 예산) theo stage:

```text
API gateway        50 ms
retrieval         150 ms
reranking         100 ms
model TTFT        500 ms
tool call         700 ms
postprocess       100 ms
```

Nếu không có ngân sách (budget / 예산) cho từng stage, đội ngũ dễ tối ưu nhầm chỗ.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Little's Law và Queueing** tiếp nhận điểm tựa từ **Độ trễ (latency / 지연 시간) ngân sách (budget / 예산)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프) của Batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Little's Law và Queueing

\[
L=\lambda W
\]

Khi arrival tỷ lệ (rate / 비율) tiến gần dịch vụ (service / 서비스) sức chứa (capacity / 용량), `W` tăng mạnh. Vì vậy “GPU luôn chạy 100%” có thể làm người dùng (user / 사용자) độ trễ (latency / 지연 시간) tệ hơn đáng kể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Sự đánh đổi (trade-off / 트레이드오프) của Batching** tiếp nhận điểm tựa từ **Little's Law và Queueing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memory-Bound và Compute-Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프) của Batching

Batch lớn hơn thường có:

```text
+ accelerator utilization
+ throughput
- memory headroom
- latency có thể tăng
```

Online scheduler cần tìm operating điểm (point / 지점) phù hợp với SLO.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Memory-Bound và Compute-Bound** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프) của Batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí của RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memory-Bound và Compute-Bound

Một kernel có thể bị giới hạn bởi **compute** hoặc **bộ nhớ (memory / 메모리) bandwidth**.

Quantization hữu ích nhất khi bộ nhớ (memory / 메모리) bandwidth là bottleneck. Nếu compute kernel chiếm ưu thế, compression có thể mang lợi ích khác.

Tư duy kiểu roofline giúp tránh tối ưu mù.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí của RAG** tiếp nhận điểm tựa từ **Memory-Bound và Compute-Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí của tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí của RAG

RAG không chỉ tốn chi phí (cost / 비용) cho embedding tìm kiếm (search / 검색). chuỗi xử lý (pipeline / 파이프라인) còn có:

```text
query rewrite
retrieval
reranking
context tokens
LLM generation
```

Retrieve nhiều chunk có thể tăng recall nhưng đồng thời làm ngữ cảnh (context / 맥락) chi phí (cost / 비용) và độ trễ (latency / 지연 시간) tăng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí của tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Chi phí của RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Economics của Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí của tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) có số bước biến động. Một tác vụ (task / 작업) tưởng như đơn giản có thể vòng lặp (loop / 루프) qua nhiều mô hình (model / 모델)/công cụ (tool / 도구) lời gọi (call / 호출).

Nên có:

- step ngân sách (budget / 예산);
- đơn vị từ (token / 토큰) ngân sách (budget / 예산);
- công cụ (tool / 도구) chi phí (cost / 비용) ngân sách (budget / 예산);
- hết thời gian chờ (timeout / 타임아웃);
- vòng lặp (loop / 루프) detection.

Nếu không có ngân sách (budget / 예산), phân phối chi phí (cost / 비용) có thể có heavy tail rất lớn.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Economics của Caching** tiếp nhận điểm tựa từ **Chi phí của tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) Offline và Online** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Economics của Caching

Bộ nhớ đệm (cache / 캐시) hit tránh expensive compute nhưng cần lưu trữ (storage / 저장소) và vô hiệu hóa (invalidation / 무효화). Giá trị của bộ nhớ đệm (cache / 캐시) phụ thuộc tần suất tái sử dụng và mức freshness mà hệ thống chấp nhận.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí (cost / 비용) Offline và Online** tiếp nhận điểm tựa từ **Economics của Caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) Attribution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) Offline và Online

Batch processing thường tận dụng hardware tốt hơn. Nếu kết quả có thể tái sử dụng, precompute giúp chuyển chi phí ra khỏi đường xử lý nóng (hot path / 핫 패스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Chi phí (cost / 비용) Attribution** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) Offline và Online** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ tự tối ưu hợp lý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) Attribution

Nền tảng multi-tenant nên quy chi phí theo tenant, tính năng (feature / 기능), mô hình (model / 모델) và workflow. Nếu chỉ nhìn tổng GPU bill, rất khó biết tính năng (feature / 기능) nào thực sự tạo giá trị.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Thứ tự tối ưu hợp lý** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) Attribution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự tối ưu hợp lý

Trước khi tune kernel thấp tầng:

```text
1. profile end-to-end
2. bỏ các call không cần thiết
3. giảm data/token movement
4. cache / reuse
5. batching
6. chọn mô hình nhỏ hoặc chuyên biệt hơn
7. quantize / compress
8. tối ưu kernel thấp tầng
```

Tối ưu hóa (optimization / 최적화) ở cấp kiến trúc (architecture / 아키텍처) thường tạo gain lớn hơn micro-optimization.

> **Chuyển mạch:** Ở chặng này của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Mô hình tư duy** gom các mảnh từ **Thứ tự tối ưu hợp lý** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Latency    = thời gian người dùng trải nghiệm cho một task
Throughput = lượng công việc hoàn thành trong một đơn vị thời gian
Cost       = tài nguyên tiêu thụ cho một outcome hữu ích
```

Mục tiêu cuối không phải tối thiểu từng chỉ số (metric / 지표) riêng lẻ mà là đạt **chất lượng và độ tin cậy yêu cầu trong giới hạn ngân sách**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Tokens/second cao nghĩa là người dùng (user / 사용자) experience tốt”

Không. TTFT hoặc hàng đợi (queue / 큐) thời gian (time / 시간) vẫn có thể rất tệ.

### “Mô hình nhỏ hơn luôn rẻ hơn”

Không. Nếu chất lượng thấp làm thử lại (retry / 재시도) hoặc escalation tăng, end-to-end chi phí (cost / 비용) có thể cao hơn.

### “Chỉ cần tối ưu mô hình (model / 모델) suy luận (inference / 추론) là đủ”

Không. Retrieval, công cụ (tool / 도구), parsing và mạng (network / 네트워크) có thể mới là bottleneck chính.

> **Chuyển mạch:** Trong **Độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량) và chi phí (cost / 비용) trong hệ thống AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Caching and Batching](./05_caching_and_batching.md), [Model Compression](./08_model_compression.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [AI Compute](../17_ai_compute_and_infrastructure/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
