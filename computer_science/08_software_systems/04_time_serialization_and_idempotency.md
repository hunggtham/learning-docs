# Thời gian (time / 시간), clocks, serialization và idempotency

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Time, clocks, serialization và idempotency**. Route đi từ wall/monotonic clock → UTC/timezone → distributed time → serialization/schema evolution → idempotency/deduplication/versioning, để retry không biến thành side effect lặp.

Three deceptively simple things cause many môi trường vận hành (production / 운영 환경) bugs: thời gian (time / 시간) zones/clocks, biểu diễn (representation / 표현) crossing boundaries, and retries. They meet whenever a yêu cầu (request / 요청)/sự kiện (event / 이벤트) is serialized, transmitted, stored and possibly repeated later.

## Wall clock vs monotonic clock

Wall clock tells civil timestamp and can jump due NTP correction/manual/timezone rules. Monotonic clock only moves forward relative duration and is appropriate hết thời gian chờ (timeout / 타임아웃)/elapsed đo lường (measurement / 측정).

Using wall clock subtraction for hết thời gian chờ (timeout / 타임아웃) can thất bại (fail / 실패) if clock adjusts backward/forward. Use thời gian chạy (runtime / 런타임) monotonic thời gian (time / 시간) for duration.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), clocks, serialization và idempotency**, **UTC, timezone và calendar** tiếp nhận điểm tựa từ **Wall clock vs monotonic clock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân tán (distributed / 분산) clocks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## UTC, timezone và calendar

Instant is điểm (point / 지점) on toàn cục (global / 전역) timeline. cục bộ (local / 로컬) date-time is biểu diễn (representation / 표현) under timezone rules. `2026-11-01 01:30` may be ambiguous in DST region. Asia/Seoul currently has no DST but software toàn cục (global / 전역) should not assume.

Store events as instant/timestamp with clear timezone ngữ nghĩa (semantics / 의미론); preserve người dùng (user / 사용자) timezone separately when nghiệp vụ (business / 비즈니스) concept is cục bộ (local / 로컬) schedule. “Every day at 9AM Seoul” is not same as fixed UTC offset forever in all zones.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Phân tán (distributed / 분산) clocks** tiếp nhận điểm tựa từ **UTC, timezone và calendar** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Serialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân tán (distributed / 분산) clocks

Máy chủ (server / 서버) timestamps from different machines can skew. For thứ tự (ordering / 순서) nhân quả (causal / 인과적) operations, cơ sở dữ liệu (database / 데이터베이스) chuỗi (sequence / 시퀀스)/log offset/logical clock may be more meaningful than wall thời gian (time / 시간). Time-based IDs need collision/clock-regression chiến lược (strategy / 전략).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Serialization** tiếp nhận điểm tựa từ **Phân tán (distributed / 분산) clocks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lược đồ (schema / 스키마) evolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Serialization

Serialization maps in-memory/logical values to wire/lưu trữ (storage / 저장소) format. JSON has văn bản (text / 텍스트), numbers, strings, arrays/objects but limited chính xác (exact / 정확한) numeric typing; JavaScript numbers are binary64, so 64-bit integer IDs can lose precision in JS if sent as JSON number beyond safe integer phạm vi (range / 범위).

Giao thức (protocol / 프로토콜) Buffers/Avro schemas define trường dữ liệu (field / 필드) numbers/types and tính tương thích (compatibility / 호환성) rules. nhị phân (binary / 이진) formats compact/typed but require lược đồ (schema / 스키마) discipline.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), clocks, serialization và idempotency**, **Lược đồ (schema / 스키마) evolution** tiếp nhận điểm tựa từ **Serialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Idempotency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lược đồ (schema / 스키마) evolution

Messages outlive mã (code / 코드) during rolling deploys, queues or stored events. Additive optional fields are generally safer; deleting/reusing trường dữ liệu (field / 필드) numbers/types can break old readers.

Readers should often tolerate unknown fields; writers may need defaults. tính tương thích (compatibility / 호환성) can be backward (new reader old data), forward (old reader new data) or full depending ecosystem.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Idempotency** tiếp nhận điểm tựa từ **Lược đồ (schema / 스키마) evolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exactly-once tác động (effect / 효과) through deduplication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Idempotency

Thao tác (operation / 연산) f is idempotent if applying same intended thao tác (operation / 연산) multiple times has same tác động (effect / 효과) as once:

\[
f(f(x)) = f(x)
\]

HTTP PUT intended ngữ nghĩa (semantics / 의미론) often idempotent; POST not inherently. nghiệp vụ (business / 비즈니스) hành động (action / 동작) can be made idempotent with key.

Payment yêu cầu (request / 요청) with `idempotency_key = order-123-charge-1`: máy chủ (server / 서버) atomically records key→kết quả (result / 결과) and returns same kết quả (result / 결과) on thử lại (retry / 재시도) instead of charge again.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Exactly-once tác động (effect / 효과) through deduplication** tiếp nhận điểm tựa từ **Idempotency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Optimistic versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exactly-once tác động (effect / 효과) through deduplication

Mạng (network / 네트워크) cannot always tell máy khách (client / 클라이언트) if timed-out yêu cầu (request / 요청) executed. thử lại (retry / 재시도) + dedup store/giao dịch (transaction / 트랜잭션) creates exactly-once-like tác động (effect / 효과) for scoped thao tác (operation / 연산). Key must represent same logical yêu cầu (request / 요청), retained long enough, and payload mismatch handled.

Dedup bản ghi (record / 레코드) creation and side tác động (effect / 효과) must be atomic or coordinated; otherwise crash between tác động (effect / 효과) and key recording still duplicates.

> **Chuyển mạch:** Trong **Thời gian (time / 시간), clocks, serialization và idempotency**, **Optimistic versioning** tiếp nhận điểm tựa từ **Exactly-once tác động (effect / 효과) through deduplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IDs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Optimistic versioning

Tài nguyên (resource / 자원) cập nhật (update / 업데이트) can include phiên bản (version / 버전)/ETag. máy khách (client / 클라이언트) reads v5, sends cập nhật (update / 업데이트) “if phiên bản (version / 버전)=5”; máy chủ (server / 서버) atomically updates to v6. Concurrent stale writer fails instead of silently overwrite. HTTP `If-Match`/ETag and DB phiên bản (version / 버전) columns use same compare-and-swap mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), clocks, serialization và idempotency**, **IDs** tiếp nhận điểm tựa từ **Optimistic versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IDs

Auto-increment gives ordered cục bộ (local / 로컬) IDs but coordination/hotspot in phân tán (distributed / 분산) setting. UUID random/time-ordered variants trade locality, generation independence and thông tin (information / 정보) leakage differently. ID should encode only ngữ nghĩa (semantics / 의미론) needed; don't assume chronological thứ tự (ordering / 순서) unless format guarantees and clock các ràng buộc (constraints / 제약조건들) understood.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **IDs** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Crossing a ranh giới (boundary / 경계) requires **tường minh (explicit / 명시적) biểu diễn (representation / 표현) + phiên bản (version / 버전) đặc tả hợp đồng (contract / 계약)**. Repeating a ranh giới (boundary / 경계) lời gọi (call / 호출) requires **idempotency/dedup đặc tả hợp đồng (contract / 계약)**. Measuring duration requires **monotonic thời gian (time / 시간)**, while nghiệp vụ (business / 비즈니스) calendars require timezone-aware civil thời gian (time / 시간).

> **Chuyển mạch:** Trong **Thời gian (time / 시간), clocks, serialization và idempotency**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“UTC solves every thời gian (time / 시간) bài toán (problem / 문제).”** It solves toàn cục (global / 전역) instant biểu diễn (representation / 표현), not cục bộ (local / 로컬) calendar recurrence/nghiệp vụ (business / 비즈니스) timezone ngữ nghĩa (semantics / 의미론).

**“JSON number safely stores any cơ sở dữ liệu (database / 데이터베이스) integer.”** JavaScript interoperability can lose integers beyond 2^53−1.

**“HTTP thử lại (retry / 재시도) is safe if vận chuyển (transport / 전송) says yêu cầu (request / 요청) failed.”** hết thời gian chờ (timeout / 타임아웃) can happen after máy chủ (server / 서버) lần ghi nhận (commit / 커밋) but before phản hồi (response / 응답) arrives.

> **Chuyển mạch:** Ở chặng này của **Thời gian (time / 시간), clocks, serialization và idempotency**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Encoding](../00_computation_information/01_information_bits_and_encoding.md), [distributed time/failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md), [transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) and [fault-tolerant retry](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md) converge here.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
