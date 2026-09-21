# Batch Inference và Online Inference

Một hệ thống AI có thể chạy cùng một mô hình theo hai chế độ thực thi rất khác nhau: **suy luận theo lô (batch inference / 배치 추론)** và **suy luận trực tuyến (online inference / 온라인 추론)**. Sự khác nhau không nằm ở mô hình mà ở hợp đồng thời gian (timing contract) giữa hệ thống và consumer.

Batch inference xử lý một tập record lớn theo lịch hoặc theo job. Online inference xử lý request ngay khi chúng đến và phải đáp ứng latency SLO. Chọn sai chế độ có thể làm hệ thống phức tạp và đắt hơn rất nhiều mà không tạo thêm giá trị.

## Batch Inference

Luồng điển hình:

```text
snapshot dữ liệu
→ chia partition
→ worker song song
→ inference
→ tổng hợp
→ ghi kết quả
```

Ví dụ:

- tính churn probability cho toàn bộ customer mỗi đêm;
- tạo embedding cho document corpus;
- tính recommendation candidate score offline;
- phân loại tài liệu lưu trữ.

Batch ưu tiên throughput và hiệu quả chi phí hơn latency của từng record riêng lẻ.

## Online Inference

Luồng điển hình:

```text
request
→ lấy feature / context
→ inference
→ policy / postprocessing
→ response
```

Ví dụ gồm fraud decision trong transaction flow, search ranking, chatbot và real-time recommendation.

Online system phải quan tâm p95/p99 latency, request burst, timeout, availability và fallback.

## Nearline và Streaming

Giữa batch và online có **nearline** hoặc **streaming**. Event được xử lý liên tục nhưng người dùng không nhất thiết đang block để chờ response.

Ví dụ: cập nhật embedding/index sau khi document thay đổi hoặc cập nhật risk score vài phút một lần.

## Độ mới của dữ liệu

Batch thường có snapshot semantics rõ ràng. Online cần feature/context đủ mới tại đúng thời điểm request.

Nếu training dùng feature đúng theo thời điểm nhưng serving lại lấy current database state sai timestamp, **training-serving skew** sẽ xuất hiện.

## Throughput và Latency

Batch có thể tăng batch size để tận dụng hardware. Online phải cân bằng batching với thời gian chờ.

Thông lượng:

\[
\text{throughput}=\frac{\text{requests completed}}{\text{time}}
\]

Latency là thời gian xử lý của từng request. Tối ưu throughput tuyệt đối có thể làm latency xấu hơn.

## Semantics về Reliability

Batch job dễ checkpoint và rerun theo partition. Online request cần timeout, retry và idempotency.

Exactly-once thường khó và đắt; nhiều hệ thống thực tế dùng **at-least-once processing + idempotent write**.

## Mô hình chi phí

Batch có thể tận dụng off-peak capacity, spot/preemptible compute hoặc batch lớn hiệu quả. Online phải giữ sẵn capacity để đáp ứng burst, từ đó phát sinh idle cost.

Vì vậy không nên dùng online inference nếu business chỉ cần score theo ngày.

## Kiến trúc Hybrid

Nhiều production system kết hợp cả hai:

```text
mô hình offline → tính trước representation đắt tiền
lớp online      → kết hợp tín hiệu mới + representation đã cache
```

Recommendation thường precompute candidate hoặc embedding rồi online rerank.

RAG có thể precompute document embedding offline nhưng retrieve và generate online.

## Ví dụ với LLM

Tóm tắt hàng triệu document phù hợp với batch. Interactive assistant cần online hoặc streaming. Evaluation suite thường nên chạy batch dù production model được expose qua online endpoint.

## Failure Mode: Batch Result bị cũ

Kết quả batch có thể không còn đủ mới. Cần TTL hoặc freshness policy. Nếu chi phí cho phép, online fallback có thể tính lại khi phát hiện kết quả đã stale.

## Checklist lựa chọn

Nên hỏi:

```text
Consumer có đang chờ trực tiếp không?
Yêu cầu freshness là bao nhiêu?
Volume có gom thành batch được không?
Kết quả có tái sử dụng được không?
Failure có thể retry sau không?
```

## Mô hình tư duy

```text
Batch  = tối ưu hiệu quả tài nguyên trên cả dataset
Online = tối ưu thời gian phản hồi bị giới hạn cho từng request
```

## Những nhầm lẫn thường gặp

### “Real-time luôn tốt hơn”

Không. Real-time thường đắt và phức tạp hơn về vận hành. Nếu decision không cần dữ liệu mới từng giây, batch có thể phù hợp hơn.

### “Batch không cần production engineering”

Không. Batch quy mô lớn vẫn cần checkpointing, lineage, retry, partitioning, backfill và cost control.

## Liên kết kiến thức

Xem [Model Serving](./03_model_serving.md), [Caching and Batching](./05_caching_and_batching.md) và [Data for AI](../14_data_for_ai/README.md).