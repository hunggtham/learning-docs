# Sự kiện (event / 이벤트) streams: partitions, watermarks, replay và stateful processing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Event streams, partitions, watermarks, replay và stateful processing**. Route đi từ partition/order → consumer groups → event time/watermarks → replay/state snapshots → late data và backpressure, để processing semantics được kiểm chứng qua recovery.

Sự kiện (event / 이벤트) stream không chỉ là hàng đợi (queue / 큐) dài. Nó là ordered lịch sử (history / 이력) được chia partition, có retention và có thể replay. Điều này cho phép nhiều consumers xây trạng thái (state / 상태) riêng từ cùng sự kiện (event / 이벤트) log, nhưng cũng đưa thứ tự (ordering / 순서), thời gian (time / 시간) và khôi phục (recovery / 복구) thành vấn đề kiến trúc.

## Partition là đơn vị thứ tự (ordering / 순서)

Broker thường chỉ đảm bảo total thứ tự (order / 순서) trong một partition, không phải toàn topic. Partition key quyết định events nào phải cùng thứ tự (order / 순서).

Nếu mọi sự kiện (event / 이벤트) dùng cùng key để có toàn cục (global / 전역) thứ tự (order / 순서), thông lượng (throughput / 처리량) bị giới hạn bởi một partition. Nếu partition quá rộng, nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) cần thứ tự (order / 순서) có thể bị tách.

> **Nối mạch:** **Bên tiêu thụ (consumer / 소비자) group** nối từ **Partition là đơn vị thứ tự (ordering / 순서)** sang **Offset**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bên tiêu thụ (consumer / 소비자) group

Trong bên tiêu thụ (consumer / 소비자) group, partitions được phân cho consumers để parallel processing. Số consumers vượt số partitions không tăng parallelism hữu ích cho group đó.

Rebalance khi bên tiêu thụ (consumer / 소비자) phép nối (join / 조인)/leave có thể tạm dừng công việc (work / 작업) hoặc chuyển quyền sở hữu (ownership / 소유권) trạng thái (state / 상태), nên frequent churn ảnh hưởng độ trễ (latency / 지연 시간).

> **Nối mạch:** **Offset** nối từ **Bên tiêu thụ (consumer / 소비자) group** sang **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Offset

Offset là vị trí trong log, không phải nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) ID. lần ghi nhận (commit / 커밋) offset trước side tác động (effect / 효과) có thể mất processing khi crash; lần ghi nhận (commit / 커밋) sau side tác động (effect / 효과) có thể duplicate side tác động (effect / 효과).

Vì vậy at-least-once processing thường kết hợp idempotency/deduplication.

> **Nối mạch:** **Offset** đặt đầu vào cho **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)**, rồi **Watermark** mở rộng hệ quả.

## Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)

Sự kiện (event / 이벤트) có thể xảy ra lúc 10:00 nhưng tới processor lúc 10:05 vì mobile offline/mạng (network / 네트워크) delay. **sự kiện (event / 이벤트) thời gian (time / 시간)** phản ánh thời điểm nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트); **processing thời gian (time / 시간)** phản ánh lúc hệ thống (system / 시스템) xử lý.

Cửa sổ (window / 윈도우) analytics cần chọn ngữ nghĩa (semantics / 의미론) đúng, nếu không late events làm số liệu sai.

> **Nối mạch:** **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** đặt đầu vào cho **Watermark**, rồi **Stateful processing** mở rộng hệ quả.

## Watermark

Watermark là estimate rằng phần lớn events trước một event-time threshold đã tới. Nó cho phép engine đóng cửa sổ (window / 윈도우) mà không chờ vô hạn.

Watermark luôn là sự đánh đổi (trade-off / 트레이드오프) completeness và độ trễ (latency / 지연 시간). Chờ lâu bắt được late dữ liệu (data / 데이터) nhưng đầu ra (output / 출력) trễ; đóng sớm cần correction/retraction khi sự kiện (event / 이벤트) muộn tới.

> **Nối mạch:** **Watermark** đặt đầu vào cho **Stateful processing**, rồi **Replay** mở rộng hệ quả.

## Stateful processing

Phép nối (join / 조인) streams, aggregate cửa sổ (window / 윈도우) và detect patterns cần trạng thái (state / 상태). trạng thái (state / 상태) phải checkpoint cùng progress/offset để khôi phục (recovery / 복구) không tạo mismatch.

Exactly-once trong stream processor thường là coordination giữa trạng thái (state / 상태) snapshot và nguồn (source / 소스)/sink positions, không phải magical mạng (network / 네트워크) guarantee.

> **Nối mạch:** **Stateful processing** đặt đầu vào cho **Replay**, rồi **Hot partition** mở rộng hệ quả.

## Replay

Retention cho phép bên tiêu thụ (consumer / 소비자) mới hoặc bug-fixed job replay lịch sử (history / 이력). Nhưng replay có thể gọi lại bên ngoài (external / 외부) side effects nếu kiến trúc (architecture / 아키텍처) không phân biệt rebuilding trạng thái (state / 상태) với live hành động (action / 동작).

Sự kiện (event / 이벤트) sourcing đặc biệt cần versioning: mã (code / 코드) mới phải hiểu old sự kiện (event / 이벤트) schemas hoặc có di chuyển (migration / 마이그레이션)/upcasting chiến lược (strategy / 전략).

> **Nối mạch:** **Hot partition** nối từ **Replay** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hot partition

Key phân phối (distribution / 분포) skew làm một partition overload dù cluster tổng thể còn sức chứa (capacity / 용량). Celebrity người dùng (user / 사용자), tenant lớn hoặc timestamp-based key có thể tạo hotspot.

Partition thiết kế (design / 설계) vì vậy là data-model quyết định (decision / 결정), không chỉ broker cấu hình (config / 설정).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Hot partition**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Mô hình tư duy (mental model / 사고 모델)

> Stream là lịch sử (history / 이력) được partition. Partition xác định thứ tự (ordering / 순서) và parallelism; offset xác định progress; watermark quản lý bất định (uncertainty / 불확실성) về thời gian (time / 시간); checkpoint gắn trạng thái (state / 상태) với progress. Replay mạnh vì lịch sử (history / 이력) còn đó, nhưng side effects phải được thiết kế để chịu replay.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
