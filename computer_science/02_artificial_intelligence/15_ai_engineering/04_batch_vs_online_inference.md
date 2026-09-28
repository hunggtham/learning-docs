# Batch suy luận (inference / 추론) và Online suy luận (inference / 추론)

> **Mạch đọc:** Đặt **Batch suy luận (inference / 추론) và Online suy luận (inference / 추론)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Batch suy luận (inference / 추론)** sang **Online suy luận (inference / 추론)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một hệ thống AI có thể chạy cùng một mô hình theo hai chế độ thực thi rất khác nhau: **suy luận theo lô (batch inference / 배치 추론)** và **suy luận trực tuyến (online inference / 온라인 추론)**. Sự khác nhau không nằm ở mô hình mà ở hợp đồng thời gian (timing contract) giữa hệ thống và bên tiêu thụ (consumer / 소비자).

Batch suy luận (inference / 추론) xử lý một tập bản ghi (record / 레코드) lớn theo lịch hoặc theo job. Online suy luận (inference / 추론) xử lý yêu cầu (request / 요청) ngay khi chúng đến và phải đáp ứng độ trễ (latency / 지연 시간) SLO. Chọn sai chế độ có thể làm hệ thống phức tạp và đắt hơn rất nhiều mà không tạo thêm giá trị.

## Batch suy luận (inference / 추론)

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

- tính churn xác suất (probability / 확률) cho toàn bộ customer mỗi đêm;
- tạo embedding cho document corpus;
- tính recommendation candidate score offline;
- phân loại tài liệu lưu trữ.

Batch ưu tiên thông lượng (throughput / 처리량) và hiệu quả chi phí hơn độ trễ (latency / 지연 시간) của từng bản ghi (record / 레코드) riêng lẻ.

## Online suy luận (inference / 추론)

Luồng điển hình:

```text
request
→ lấy feature / context
→ inference
→ policy / postprocessing
→ response
```

Ví dụ gồm fraud quyết định (decision / 결정) trong giao dịch (transaction / 트랜잭션) luồng (flow / 흐름), tìm kiếm (search / 검색) ranking, chatbot và real-time recommendation.

Online hệ thống (system / 시스템) phải quan tâm p95/p99 độ trễ (latency / 지연 시간), yêu cầu (request / 요청) burst, hết thời gian chờ (timeout / 타임아웃), availability và fallback.

## Nearline và Streaming

Giữa batch và online có **nearline** hoặc **streaming**. sự kiện (event / 이벤트) được xử lý liên tục nhưng người dùng không nhất thiết đang khối (block / 블록) để chờ phản hồi (response / 응답).

Ví dụ: cập nhật embedding/chỉ mục (index / 인덱스) sau khi document thay đổi hoặc cập nhật rủi ro (risk / 위험) score vài phút một lần.

## Độ mới của dữ liệu

Batch thường có snapshot ngữ nghĩa (semantics / 의미론) rõ ràng. Online cần tính năng (feature / 기능)/ngữ cảnh (context / 맥락) đủ mới tại đúng thời điểm yêu cầu (request / 요청).

Nếu huấn luyện (training / 학습) dùng tính năng (feature / 기능) đúng theo thời điểm nhưng serving lại lấy hiện tại (current / 현재) cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태) sai timestamp, **training-serving skew** sẽ xuất hiện.

## Thông lượng (throughput / 처리량) và độ trễ (latency / 지연 시간)

Batch có thể tăng batch kích thước (size / 크기) để tận dụng hardware. Online phải cân bằng batching với thời gian chờ.

Thông lượng:

\[
\văn bản (text / 텍스트){thông lượng (throughput / 처리량)}=\frac{\văn bản (text / 텍스트){requests completed}}{\văn bản (text / 텍스트){thời gian (time / 시간)}}
\]

Độ trễ (latency / 지연 시간) là thời gian xử lý của từng yêu cầu (request / 요청). Tối ưu thông lượng (throughput / 처리량) tuyệt đối có thể làm độ trễ (latency / 지연 시간) xấu hơn.

## Ngữ nghĩa (semantics / 의미론) về độ tin cậy (reliability / 신뢰성)

Batch job dễ checkpoint và rerun theo partition. Online yêu cầu (request / 요청) cần hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도) và idempotency.

Exactly-once thường khó và đắt; nhiều hệ thống thực tế dùng **at-least-once processing + idempotent ghi (write / 쓰기)**.

## Mô hình chi phí

Batch có thể tận dụng off-peak sức chứa (capacity / 용량), spot/preemptible compute hoặc batch lớn hiệu quả. Online phải giữ sẵn sức chứa (capacity / 용량) để đáp ứng burst, từ đó phát sinh idle chi phí (cost / 비용).

Vì vậy không nên dùng online suy luận (inference / 추론) nếu nghiệp vụ (business / 비즈니스) chỉ cần score theo ngày.

## Kiến trúc Hybrid

Nhiều môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) kết hợp cả hai:

```text
mô hình offline → tính trước representation đắt tiền
lớp online      → kết hợp tín hiệu mới + representation đã cache
```

Recommendation thường precompute candidate hoặc embedding rồi online rerank.

RAG có thể precompute document embedding offline nhưng retrieve và generate online.

## Ví dụ với LLM

Tóm tắt hàng triệu document phù hợp với batch. Interactive assistant cần online hoặc streaming. Evaluation suite thường nên chạy batch dù môi trường vận hành (production / 운영 환경) mô hình (model / 모델) được expose qua online endpoint.

## Dạng thất bại (failure mode / 실패 모드): Batch kết quả (result / 결과) bị cũ

Kết quả batch có thể không còn đủ mới. Cần TTL hoặc freshness chính sách (policy / 정책). Nếu chi phí cho phép, online fallback có thể tính lại khi phát hiện kết quả đã stale.

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

Không. Real-time thường đắt và phức tạp hơn về vận hành. Nếu quyết định (decision / 결정) không cần dữ liệu mới từng giây, batch có thể phù hợp hơn.

### “Batch không cần môi trường vận hành (production / 운영 환경) kỹ thuật (engineering / 엔지니어링)”

Không. Batch quy mô lớn vẫn cần checkpointing, lineage, thử lại (retry / 재시도), partitioning, backfill và chi phí (cost / 비용) điều khiển (control / 제어).

## Liên kết kiến thức

Xem [Model Serving](./03_model_serving.md), [Caching and Batching](./05_caching_and_batching.md) và [Data for AI](../14_data_for_ai/README.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai engineering](./00_ai_engineering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
