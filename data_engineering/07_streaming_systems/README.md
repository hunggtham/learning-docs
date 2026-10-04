# 07 — Streaming các hệ thống (systems / 시스템들): sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태) và replay

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **07 — Streaming các hệ thống (systems / 시스템들): sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태) và replay**. Route đi từ event/processing/ingestion time → windows và watermarks → state, late events và corrections → replay, exactly/at-least-once semantics → monitoring, để streaming luôn giải thích được kết quả thay đổi theo thời gian.

Streaming là bài toán duy trì computation trên đầu vào (input / 입력) chưa bao giờ thực sự “đóng”. Vì vậy trọng tâm là thời gian, trạng thái (state / 상태), late sự kiện (event / 이벤트) và cách kết quả được sửa khi giả định (assumption / 가정) ban đầu thay đổi.

## 1. Ba loại thời gian

- sự kiện (event / 이벤트) thời gian (time / 시간): thời điểm sự kiện xảy ra theo lĩnh vực (domain / 도메인);
- ingestion thời gian (time / 시간): lúc nền tảng (platform / 플랫폼) nhận sự kiện (event / 이벤트);
- processing thời gian (time / 시간): lúc worker xử lý sự kiện (event / 이벤트).

Dashboard vận hành thường cần processing/ingestion thời gian (time / 시간); nghiệp vụ (business / 비즈니스) cửa sổ (window / 윈도우) thường cần sự kiện (event / 이벤트) thời gian (time / 시간). Trộn chúng làm số liệu lệch mà không nhất thiết tạo lỗi.

> **Chuyển mạch:** **Ba loại thời gian** tách event, processing và ingestion time; **Window và watermark** dùng distinction đó để quyết định state nào còn mở.

## 2. cửa sổ (window / 윈도우) và watermark

Cửa sổ (window / 윈도우) biến stream vô hạn thành nhóm hữu hạn để aggregate. Với event-time cửa sổ (window / 윈도우), hệ thống phải chờ sự kiện (event / 이벤트) đến muộn. Watermark là một frontier tiến dần, thể hiện mức event-time mà engine tin rằng phần lớn dữ liệu đã đến.

Watermark không phải sự thật tuyệt đối. Nó là chính sách (policy / 정책) đánh đổi độ trễ (latency / 지연 시간), completeness và trạng thái (state / 상태) kích thước (size / 크기). Late sự kiện (event / 이벤트) sau watermark cần quy tắc (rule / 규칙) rõ: cập nhật (update / 업데이트) kết quả, ghi correction, đưa vào quarantine, hay bỏ qua có kiểm tra (audit / 감사).

> **Chuyển mạch:** Ở chặng này của **07 — Streaming các hệ thống (systems / 시스템들): sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태) và replay**, **2. cửa sổ (window / 윈도우) và watermark** xác định đầu vào; **3. trạng thái (state / 상태) vòng đời (lifecycle / 생명주기)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. Late dữ liệu (data / 데이터) và corrections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. trạng thái (state / 상태) vòng đời (lifecycle / 생명주기)

Trạng thái (state / 상태) có thể là count theo key, session, deduplication set, phép nối (join / 조인) buffer hoặc hiện tại (current / 현재) projection. Mỗi trạng thái (state / 상태) cần:

```text
key → value/schema → update rule → retention → checkpoint → recovery behavior
```

Trạng thái (state / 상태) vô hạn là bộ nhớ (memory / 메모리) leak ở cấp dữ liệu (data / 데이터) sản phẩm (product / 제품). TTL phải dựa trên nghiệp vụ (business / 비즈니스) late-arrival bound và replay yêu cầu (requirement / 요구사항), không chỉ default của engine.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **07 — Streaming các hệ thống (systems / 시스템들): sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태) và replay**, cơ chế trong **3. trạng thái (state / 상태) vòng đời (lifecycle / 생명주기)** cần được kiểm chứng bằng dấu vết cụ thể; **4. Late dữ liệu (data / 데이터) và corrections** đưa dữ liệu và nguồn vào đúng điểm đó. Từ đây, **5. CDC, thứ tự (ordering / 순서) và lược đồ (schema / 스키마) evolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Late dữ liệu (data / 데이터) và corrections

Một sự kiện (event / 이벤트) đến muộn có thể thay đổi aggregate đã publish. Nếu bên tiêu thụ (consumer / 소비자) chỉ đọc append-only đầu ra (output / 출력), correction cần một bản ghi (record / 레코드) điều chỉnh hoặc phiên bản (version / 버전) mới. Nếu bên tiêu thụ (consumer / 소비자) đọc snapshot, cần publish atomic snapshot pointer.

Không nên giả vờ stream là immutable khi lĩnh vực (domain / 도메인) cho phép correction. Hãy mô tả rõ chỉ số (metric / 지표) là provisional hay final và khi nào finalization xảy ra.

> **Chuyển mạch:** Trong **07 — Streaming các hệ thống (systems / 시스템들): sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태) và replay**, **4. Late dữ liệu (data / 데이터) và corrections** nêu điều cần giải thích; **5. CDC, thứ tự (ordering / 순서) và lược đồ (schema / 스키마) evolution** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Delivery và sink** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. CDC, thứ tự (ordering / 순서) và lược đồ (schema / 스키마) evolution

CDC stream thường có giao dịch (transaction / 트랜잭션)/thứ tự (order / 순서) siêu dữ liệu (metadata / 메타데이터). bên tiêu thụ (consumer / 소비자) cần biết thứ tự (ordering / 순서) guarantee là per-key, per-partition hay toàn cục (global / 전역); delete có payload hay tombstone; snapshot nối vào log position nào; lược đồ (schema / 스키마) phiên bản (version / 버전) đi cùng bản ghi (record / 레코드) hay được tra ngoài.

Lược đồ (schema / 스키마) evolution an toàn thường theo trình tự: add optional trường dữ liệu (field / 필드) → nâng bên tiêu thụ (consumer / 소비자) → producer bắt đầu ghi trường dữ liệu (field / 필드) → deprecate trường dữ liệu (field / 필드) cũ sau tính tương thích (compatibility / 호환성) cửa sổ (window / 윈도우). Rename trực tiếp có thể làm reader cũ hiểu sai hoặc tạo drop+add.

> **Chuyển mạch:** **CDC, ordering và schema evolution** xác định event contract; **Delivery và sink** thực thi contract đó, rồi **Replay** kiểm tra khả năng tái tạo output.

## 6. Delivery và sink

At-least-once là lựa chọn phổ biến vì replay an toàn hơn mất mát (loss / 손실), nhưng sink phải idempotent theo `event_id`/phiên bản (version / 버전). “Exactly-once” của processor không tự mở rộng qua bên ngoài (external / 외부) API, email, payment hoặc cơ sở dữ liệu (database / 데이터베이스) không tham gia giao dịch (transaction / 트랜잭션).

Tách pure projection khỏi side tác động (effect / 효과):

```text
stream → deterministic projection → durable output
                         └──────→ side-effect dispatcher với idempotency key
```

> **Chuyển mạch:** **Replay** xác nhận event log đủ và deterministic đến đâu; **Streaming checklist** gom delivery, state, watermark và recovery evidence.

## 7. Replay

Replay cần xác định offset/thời gian (time / 시간) phạm vi (range / 범위), lược đồ (schema / 스키마) phiên bản (version / 버전), mã (code / 코드) phiên bản (version / 버전), trạng thái (state / 상태) reset chiến lược (strategy / 전략) và đầu ra (output / 출력) ghi (write / 쓰기) chế độ (mode / 모드). Replay vào cùng sink có thể duplicate hoặc ghi đè kết quả mới nếu không có không gian tên (namespace / 네임스페이스)/phiên bản (version / 버전).

Một hệ thống trưởng thành có thể chạy replay nhỏ trên mẫu (sample / 표본), đối chiếu aggregate với snapshot/tham chiếu (reference / 참조) và chỉ promote đầu ra (output / 출력) sau reconciliation.

> **Chuyển mạch:** **Streaming checklist** đặt tiêu chí vận hành; **Window result state machine** biến tiêu chí đó thành transition và output có thể kiểm tra.

## 8. Streaming checklist

1. chỉ số (metric / 지표) dùng sự kiện (event / 이벤트) thời gian (time / 시간) hay processing thời gian (time / 시간)?
2. Watermark dựa trên bound nào và late sự kiện (event / 이벤트) sau đó đi đâu?
3. trạng thái (state / 상태) key, retention và checkpoint có bất biến (invariant / 불변식) gì?
4. Duplicate, delete, correction và lược đồ (schema / 스키마) phiên bản (version / 버전) biểu diễn thế nào?
5. Replay có tái tạo đúng kết quả và không lặp side tác động (effect / 효과) không?

Đọc tiếp: [02 — Pipeline semantics](../02_pipeline_architecture.md), [06 — Distributed processing](../06_distributed_processing/README.md), [08 — Orchestration và backfill](../08_orchestration_and_backfill/README.md).

> **Chuyển mạch:** **Window result state machine** xác định state transition; **State store và checkpoint** bảo đảm transition không mất khi process restart hoặc scale.

## 9. cửa sổ (window / 윈도우) kết quả (result / 결과) là máy trạng thái (state machine / 상태 머신)

Một cửa sổ (window / 윈도우) không chỉ có giá trị số; nó có vòng đời (lifecycle / 생명주기):

```text
open → updating → provisional → finalized → corrected/expired
```

Watermark chuyển cửa sổ (window / 윈도우) từ open sang provisional/finalized theo chính sách (policy / 정책). Late sự kiện (event / 이벤트) sau finalized không được âm thầm mutate kết quả mà không phát phiên bản (version / 버전)/correction bằng chứng (evidence / 증거).

> **Chuyển mạch:** **State store và checkpoint** giữ durability của window state; **CDC snapshot handoff** dùng durability đó để nối batch snapshot với stream.

## 10. trạng thái (state / 상태) store và checkpoint

Checkpoint phải bao phủ cả đầu vào (input / 입력) position và trạng thái (state / 상태) snapshot. Chỉ lưu offset mà không lưu trạng thái (state / 상태) tương ứng có thể làm restart tính lại với trạng thái (state / 상태) cũ hoặc bỏ mất sự kiện (event / 이벤트). trạng thái (state / 상태) lược đồ (schema / 스키마) evolution cần di chuyển (migration / 마이그레이션)/phiên bản (version / 버전), đặc biệt khi operator đổi key hoặc cửa sổ (window / 윈도우) definition.

Checkpoint interval là sự đánh đổi (trade-off / 트레이드오프): interval ngắn giảm replay công việc (work / 작업) nhưng tăng I/O; interval dài giảm overhead nhưng khôi phục (recovery / 복구) lâu hơn. Đo khôi phục (recovery / 복구) điểm (point / 지점), checkpoint kích thước (size / 크기), restore thời gian (time / 시간) và duplicate/correction hành vi (behavior / 동작).

> **Chuyển mạch:** **CDC snapshot handoff** khóa điểm bắt đầu và ordering; **Backpressure** kiểm tra hệ thống phản ứng ra sao khi producer nhanh hơn consumer.

## 11. CDC snapshot handoff

Snapshot + log CDC cần một cutover điểm (point / 지점) atomic. Nếu snapshot đọc lúc T1 nhưng log bắt đầu từ T2, mutation giữa T1 và T2 bị mất; nếu log bắt đầu trước T1, sự kiện (event / 이벤트) có thể bị duplicate và phải dedup theo giao dịch (transaction / 트랜잭션) position.

Bên tiêu thụ (consumer / 소비자) nên lưu `snapshot_id`, `log_position`, lược đồ (schema / 스키마) phiên bản (version / 버전) và nguồn (source / 소스) giao dịch (transaction / 트랜잭션) siêu dữ liệu (metadata / 메타데이터). Đây là bằng chứng (evidence / 증거) để chứng minh không có gap trong handoff.

> **Chuyển mạch:** **Backpressure** khép README bằng capacity, lag và recovery evidence; chi tiết engine quay về canonical streaming owner.

## 12. Backpressure

Khi sink chậm hơn nguồn (source / 소스), lag tăng. Backpressure có thể làm giảm ingest tỷ lệ (rate / 비율), tăng trạng thái (state / 상태)/retention pressure hoặc đẩy dữ liệu sang durable buffer. Không nên chỉ tăng bên tiêu thụ (consumer / 소비자) count nếu bottleneck là sink partition, mạng (network / 네트워크) hoặc skew key.

Theo dõi lag theo partition, arrival tỷ lệ (rate / 비율), processing tỷ lệ (rate / 비율), watermark delay, trạng thái (state / 상태) kích thước (size / 크기) và sink độ trễ (latency / 지연 시간). Một average lag thấp có thể che một partition bị kẹt.

> **Bàn giao:** Sau **12. Backpressure**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
