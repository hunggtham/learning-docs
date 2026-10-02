# 02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. chuỗi xử lý (pipeline / 파이프라인) là chuỗi chuyển tiếp trạng thái (state transition / 상태 전이)** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **2. ETL và ELT** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối pipeline architecture với ingestion, storage, processing và serving, để dữ liệu có đường đi và boundary rõ.

## 1. chuỗi xử lý (pipeline / 파이프라인) là chuỗi chuyển tiếp trạng thái (state transition / 상태 전이)

Sơ đồ `source → queue → processor → warehouse` che giấu phần khó nhất: ở mỗi mũi tên, hệ thống phải quyết định khi nào một piece of dữ liệu (data / 데이터) được coi là đã xử lý thành công.

Nếu nguồn (source / 소스) đã phát sự kiện (event / 이벤트) nhưng bên tiêu thụ (consumer / 소비자) chưa ghi được sink, sự kiện (event / 이벤트) phải còn khả năng replay. Nếu sink đã ghi thành công nhưng acknowledgement bị mất, thử lại (retry / 재시도) không được làm sai kết quả. Vì vậy kiến trúc chuỗi xử lý (pipeline / 파이프라인) nên được đọc như chuỗi chuyển tiếp trạng thái (state transition / 상태 전이) có thất bại (failure / 실패) ranh giới (boundary / 경계), không phải chuỗi logo sản phẩm.

> **Chuyển mạch:** Trong **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **1. chuỗi xử lý (pipeline / 파이프라인) là chuỗi chuyển tiếp trạng thái (state transition / 상태 전이)** xác định đầu vào; **2. ETL và ELT** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3. Full tải (load / 로드) và incremental tải (load / 로드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. ETL và ELT

ETL (Extract, Transform, Load) biến đổi dữ liệu trước khi nạp vào analytical store. ELT (Extract, Load, Transform) đưa raw hoặc near-raw dữ liệu (data / 데이터) vào nền tảng (platform / 플랫폼) trước rồi transformation chạy bên trong analytical engine.

ELT trở nên phổ biến khi warehouse/lakehouse có compute mạnh và lưu trữ (storage / 저장소) rẻ, nhưng đây không phải quy tắc rằng ELT luôn tốt hơn. Dữ liệu nhạy cảm có thể cần masking trước khi landing. Payload rất lớn có thể cần normalize/filter trước để tránh chi phí vận chuyển. Ngược lại, transform quá sớm có thể làm mất raw bằng chứng (evidence / 증거) cần cho replay hoặc kiểm tra (audit / 감사).

Sự đánh đổi (trade-off / 트레이드오프) thật sự nằm ở nơi đặt transformation ranh giới (boundary / 경계), khả năng replay và quản trị (governance / 거버넌스) chứ không nằm ở ba chữ viết tắt.

> **Chuyển mạch:** Ở chặng này của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **3. Full tải (load / 로드) và incremental tải (load / 로드)** tiếp nhận điểm tựa từ **2. ETL và ELT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. CDC và giao dịch (transaction / 트랜잭션) log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Full tải (load / 로드) và incremental tải (load / 로드)

Full tải (load / 로드) đọc lại toàn bộ dataset. Nó đơn giản về lập luận (reasoning / 추론) nhưng trở nên đắt khi dữ liệu lớn. Incremental tải (load / 로드) chỉ xử lý phần thay đổi, giảm I/O và compute nhưng đòi hỏi xác định chính xác "cái gì đã thay đổi".

Một filter kiểu `updated_at > last_run_time` có vẻ đơn giản nhưng có nhiều giả định (assumption / 가정): clock có đáng tin không, giao dịch (transaction / 트랜잭션) lần ghi nhận (commit / 커밋) sau khi timestamp được tạo có bị bỏ sót không, hai bản ghi (record / 레코드) cùng timestamp xử lý ra sao, job thử lại (retry / 재시도) sử dụng checkpoint nào, và nguồn (source / 소스) có cập nhật (update / 업데이트) timestamp cho mọi mutation hay không.

Một incremental ranh giới (boundary / 경계) tốt thường cần overlap cửa sổ (window / 윈도우) cộng deduplication, monotonically increasing cursor đáng tin cậy, hoặc CDC log thay vì chỉ dựa vào wall-clock timestamp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **4. CDC và giao dịch (transaction / 트랜잭션) log** tiếp nhận điểm tựa từ **3. Full tải (load / 로드) và incremental tải (load / 로드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. At-most-once, at-least-once và exactly-once** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. CDC và giao dịch (transaction / 트랜잭션) log

Thu thập thay đổi dữ liệu (Change Data Capture, CDC / 변경 데이터 캡처) theo giao dịch (transaction / 트랜잭션) log thường tốt hơn polling bảng (table / 테이블) vì cơ sở dữ liệu (database / 데이터베이스) đã có log để phục vụ durability/khôi phục (recovery / 복구). CDC connector có thể đọc chuỗi (sequence / 시퀀스) của insert/cập nhật (update / 업데이트)/delete mà không scan toàn bảng liên tục.

Nhưng CDC không phải magic. bên tiêu thụ (consumer / 소비자) cần hiểu snapshot ban đầu nối với log position nào, delete được biểu diễn thế nào, lược đồ (schema / 스키마) thay đổi (change / 변경) ảnh hưởng decoder ra sao, giao dịch (transaction / 트랜잭션) lớn gây lag thế nào và retention của nguồn (source / 소스) log có đủ dài để connector phục hồi sau downtime hay không.

Một thất bại (failure / 실패) môi trường vận hành (production / 운영 환경) phổ biến xảy ra khi connector ngừng lâu hơn log retention. Offset vẫn tồn tại nhưng log segment cần thiết đã bị xóa; lúc này không thể chỉ restart và mong chuỗi xử lý (pipeline / 파이프라인) tự bắt kịp. khôi phục (recovery / 복구) có thể cần snapshot/resync.

> **Chuyển mạch:** Trong **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **5. At-most-once, at-least-once và exactly-once** tiếp nhận điểm tựa từ **4. CDC và giao dịch (transaction / 트랜잭션) log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Offset không phải nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. At-most-once, at-least-once và exactly-once

At-most-once ưu tiên không xử lý duplicate nhưng chấp nhận mất message nếu thất bại (failure / 실패) xảy ra ở thời điểm xấu. At-least-once ưu tiên không mất dữ liệu bằng thử lại (retry / 재시도), đổi lại bên tiêu thụ (consumer / 소비자) phải chịu duplicate. Exactly-once cố gắng để tác động (effect / 효과) quan sát được tương đương một lần xử lý.

Trong thực tế, at-least-once cộng idempotent sink thường là mô hình dễ lập luận (reasoning / 추론) và robust. Ví dụ sink `MERGE` theo immutable `event_id` có thể hấp thụ thử lại (retry / 재시도). Tuy nhiên nếu nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트) không có định danh (identity / 식별자) ổn định, deduplication trở thành bài toán lĩnh vực (domain / 도메인) chứ không thể giải chỉ bằng khung phần mềm (framework / 프레임워크) setting.

> **Chuyển mạch:** Ở chặng này của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **6. Offset không phải nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **5. At-most-once, at-least-once và exactly-once** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Offset không phải nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)

Broker offset chỉ nói bên tiêu thụ (consumer / 소비자) đã tiến tới đâu trong log. Nó không tự chứng minh downstream trạng thái (state / 상태) đúng.

Nếu bên tiêu thụ (consumer / 소비자) lần ghi nhận (commit / 커밋) offset trước khi sink lần ghi nhận (commit / 커밋), crash có thể làm mất tác động (effect / 효과). Nếu lần ghi nhận (commit / 커밋) sink trước offset, crash có thể tạo duplicate khi replay. Transactional tích hợp (integration / 통합) hoặc idempotency là cách nối hai chuyển tiếp trạng thái (state transition / 상태 전이) này.

Cấp cao (senior / 시니어) ghi chú (note / 노트): khi rà soát (review / 검토) chuỗi xử lý (pipeline / 파이프라인), luôn vẽ riêng `source position`, `processing state` và `sink commit`. Đừng gộp chúng thành một khái niệm "processed".

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **6. Offset không phải nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성)** xác định đầu vào; **7. sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **8. Backfill và replay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)

Processing thời gian (time / 시간) là lúc hệ thống xử lý sự kiện (event / 이벤트). sự kiện (event / 이벤트) thời gian (time / 시간) là lúc sự kiện thực sự xảy ra theo lĩnh vực (domain / 도메인). Hai thời điểm có thể lệch đáng kể.

Ví dụ điện thoại offline ghi nhận purchase lúc 09:00 nhưng upload lúc 11:00. Dashboard theo processing thời gian (time / 시간) sẽ đưa giao dịch vào 11:00; nghiệp vụ (business / 비즈니스) report theo sự kiện (event / 이벤트) thời gian (time / 시간) có thể cần đưa nó về 09:00.

Streaming cửa sổ (window / 윈도우) theo sự kiện (event / 이벤트) thời gian (time / 시간) vì vậy phải chấp nhận dữ liệu đến muộn (late data / 지연 데이터). Watermark là tuyên bố thực dụng rằng hệ thống tin phần lớn sự kiện (event / 이벤트) trước một mốc đã đến và có thể finalize/cleanup trạng thái (state / 상태) theo chính sách (policy / 정책). Watermark không làm late sự kiện (event / 이벤트) biến mất; nó quyết định cách hệ thống đánh đổi completeness, độ trễ (latency / 지연 시간) và trạng thái (state / 상태) kích thước (size / 크기).

> **Chuyển mạch:** Trong **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **7. sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** xác định đầu vào; **8. Backfill và replay** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **9. Orchestration không phải processing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Backfill và replay

Backfill chạy lại dữ liệu lịch sử để sửa lô-gic (logic / 논리), bổ sung trường dữ liệu (field / 필드) hoặc khôi phục gap. chuỗi xử lý (pipeline / 파이프라인) không được thiết kế cho replay thường trở nên nguy hiểm khi backfill: nó có thể gửi lại email, overwrite snapshot mới bằng dữ liệu cũ hoặc nhân đôi fact.

Một transformation thuần túy từ immutable đầu vào (input / 입력) sang deterministic đầu ra (output / 출력) dễ backfill hơn. bên ngoài (external / 외부) side tác động (effect / 효과) cần được tách khỏi recomputable dữ liệu (data / 데이터) transformation hoặc bảo vệ bằng idempotency key.

Trước một backfill lớn phải xác định đầu vào (input / 입력) phiên bản (version / 버전), mã (code / 코드) phiên bản (version / 버전), mục tiêu (target / 대상) partitions, ghi (write / 쓰기) chế độ (mode / 모드), expected row counts, reconciliation quy tắc (rule / 규칙) và chiến lược quay lui (rollback strategy / 롤백 전략). "Chạy lại job" không phải một khôi phục (recovery / 복구) plan.

> **Chuyển mạch:** Ở chặng này của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **8. Backfill và replay** xác định đầu vào; **9. Orchestration không phải processing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **10. Failure-oriented thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Orchestration không phải processing

Orchestrator quản lý phụ thuộc (dependency / 의존성), scheduling, thử lại (retry / 재시도) và trạng thái (state / 상태) của workflow. Nó không nên được nhầm với compute engine.

Một DAG xanh chỉ chứng minh tác vụ (task / 작업) tiến trình (process / 프로세스) trả về success theo điều kiện của nó. DAG không chứng minh nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) đúng. Vì vậy dữ liệu (data / 데이터) cổng chất lượng (quality gate / 품질 게이트) và reconciliation phải là một phần tường minh (explicit / 명시적) của workflow khi dataset quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **9. Orchestration không phải processing** xác định đầu vào; **10. Failure-oriented thiết kế (design / 설계)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **11. Checkpoint, watermark và lần ghi nhận (commit / 커밋) marker không giống nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Failure-oriented thiết kế (design / 설계)

Thiết kế chuỗi xử lý (pipeline / 파이프라인) nên bắt đầu bằng câu hỏi "nếu tiến trình (process / 프로세스) chết ở từng dòng mã (code / 코드) thì sao?". Thử thất bại (failure / 실패) trước và sau read, trước và sau ghi (write / 쓰기), trước và sau acknowledgement. Sau đó kiểm tra restart có tạo mất mát (loss / 손실), duplicate, corruption hoặc inconsistent checkpoint không.

Cách lập luận (reasoning / 추론) này mạnh hơn việc chỉ đọc happy-path kiến trúc (architecture / 아키텍처) diagram, bởi môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) được định nghĩa phần lớn bởi hành vi (behavior / 동작) khi một phần của nó thất bại.

> **Chuyển mạch:** Trong **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **11. Checkpoint, watermark và lần ghi nhận (commit / 커밋) marker không giống nhau** tiếp nhận điểm tựa từ **10. Failure-oriented thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약) và đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Checkpoint, watermark và lần ghi nhận (commit / 커밋) marker không giống nhau

Ba khái niệm thường bị gộp thành “đã chạy tới đâu”:

- checkpoint: processing trạng thái (state / 상태) để engine tiếp tục computation;
- watermark: frontier về thời gian hoặc completeness của đầu vào (input / 입력);
- lần ghi nhận (commit / 커밋) marker: bằng chứng rằng đầu ra (output / 출력) partition/snapshot đã công khai (public / 공개) atomically.

Checkpoint có thể tiến trong khi sink chưa lần ghi nhận (commit / 커밋). Watermark có thể tiến dù một late sự kiện (event / 이벤트) còn đang trên đường đến. lần ghi nhận (commit / 커밋) marker chỉ nên được ghi sau reconciliation. Thiết kế sai ranh giới (boundary / 경계) này tạo chuỗi xử lý (pipeline / 파이프라인) xanh nhưng đầu ra (output / 출력) thiếu hoặc không thể replay.

> **Chuyển mạch:** Ở chặng này của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **12. đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약) và đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **11. Checkpoint, watermark và lần ghi nhận (commit / 커밋) marker không giống nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Sink mẫu (pattern / 패턴) theo loại đầu ra (output / 출력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약) và đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)

Đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약) phải mô tả nguồn (source / 소스) authority, định danh (identity / 식별자), thứ tự (ordering / 순서), lược đồ (schema / 스키마) phiên bản (version / 버전), delete/tombstone và retention. đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약) phải mô tả grain, freshness, completeness, late correction, quyền sở hữu (ownership / 소유권) và tính tương thích (compatibility / 호환성).

Một chuỗi xử lý (pipeline / 파이프라인) có thể “đọc được” payload nhưng vẫn vi phạm đặc tả hợp đồng (contract / 계약) nếu nguồn (source / 소스) đổi timezone, đổi currency hoặc đổi ý nghĩa enum. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) nên kiểm tra ngữ nghĩa (semantics / 의미론) representative, không chỉ parser.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **13. Sink mẫu (pattern / 패턴) theo loại đầu ra (output / 출력)** tiếp nhận điểm tựa từ **12. đầu vào (input / 입력) đặc tả hợp đồng (contract / 계약) và đầu ra (output / 출력) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. chuỗi xử lý (pipeline / 파이프라인) rà soát (review / 검토) bằng máy trạng thái (state machine / 상태 머신)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Sink mẫu (pattern / 패턴) theo loại đầu ra (output / 출력)

| đầu ra (output / 출력) | ghi (write / 쓰기) mẫu (pattern / 패턴) thường phù hợp | Rủi ro chính |
|---|---|---|
| immutable sự kiện (event / 이벤트) | append + dedup key | duplicate/reorder |
| trạng thái hiện tại (current state / 현재 상태) | upsert theo key/phiên bản (version / 버전) | stale cập nhật (update / 업데이트) ghi đè trạng thái (state / 상태) mới |
| partition aggregate | overwrite/replace partition | partial publish |
| correction | append adjustment/phiên bản (version / 버전) | bên tiêu thụ (consumer / 소비자) không áp dụng correction |
| bên ngoài (external / 외부) side tác động (effect / 효과) | outbox + idempotency key | thử lại (retry / 재시도) lặp side tác động (effect / 효과) |

Chọn sink mẫu (pattern / 패턴) trước khi chọn khung phần mềm (framework / 프레임워크). Cùng một engine có thể implement mọi mẫu (pattern / 패턴) nhưng guarantee và khôi phục (recovery / 복구) khác nhau.

> **Chuyển mạch:** Trong **02 — Kiến trúc chuỗi xử lý (pipeline / 파이프라인) và processing ngữ nghĩa (semantics / 의미론)**, **13. Sink mẫu (pattern / 패턴) theo loại đầu ra (output / 출력)** xác định đầu vào; **14. chuỗi xử lý (pipeline / 파이프라인) rà soát (review / 검토) bằng máy trạng thái (state machine / 상태 머신)** giải thích bước vận hành tạo ra kết quả kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 14. chuỗi xử lý (pipeline / 파이프라인) rà soát (review / 검토) bằng máy trạng thái (state machine / 상태 머신)

Vẽ trạng thái (state / 상태) của một bản ghi (record / 레코드) hoặc partition thay vì chỉ vẽ thành phần (component / 컴포넌트):

```text
discovered → captured → transformed → validated → committed → published
                   ↘ quarantined / retryable / expired
```

Mỗi chuyển tiếp (transition / 전이) cần sự kiện (event / 이벤트) log hoặc chỉ số (metric / 지표) đủ để điều tra. Nếu không biết bản ghi (record / 레코드) đang ở trạng thái (state / 상태) nào, sự cố (incident / 인시던트) phản hồi (response / 응답) sẽ phải đoán từ log rời rạc.

> **Bàn giao:** Sau **14. chuỗi xử lý (pipeline / 파이프라인) rà soát (review / 검토) bằng máy trạng thái (state machine / 상태 머신)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
