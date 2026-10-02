# 90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Trường hợp (case / 사례) 1 — CDC duplicate sau thử lại (retry / 재시도)** đưa mô hình vào một trường hợp đủ cụ thể để quan sát; sau đó sang **Trường hợp (case / 사례) 2 — Late sự kiện (event / 이벤트) làm thay đổi cửa sổ (window / 윈도우)** để đem mô hình vào tình huống cụ thể. Mạch này dùng README làm bản đồ owner của data-engineering case studies, rồi nối từng tình huống với pipeline, SLA, cost và failure mode.

Trường hợp (case / 사례) study là nơi kiểm tra mô hình tư duy (mental model / 사고 모델) bằng thất bại (failure / 실패) thật, không phải nơi liệt kê sản phẩm.

## Trường hợp (case / 사례) 1 — CDC duplicate sau thử lại (retry / 재시도)

**Tình huống:** connector đọc giao dịch (transaction / 트랜잭션) log, sink đã ghi sự kiện (event / 이벤트) nhưng acknowledgement bị mất; connector đọc lại cùng sự kiện (event / 이벤트).

**bất biến (invariant / 불변식):** mỗi immutable `event_id` đóng góp đúng một lần vào fact doanh thu.

**Thiết kế:** landing append-only giữ raw sự kiện (event / 이벤트); modeled tầng (layer / 계층) `MERGE` theo sự kiện (event / 이벤트) định danh (identity / 식별자) và kiểm tra payload xung đột (conflict / 충돌); serving aggregate chạy từ modeled trạng thái (state / 상태). Offset chỉ là nguồn (source / 소스) position, không phải nghiệp vụ (business / 비즈니스) tính đúng đắn (correctness / 정확성).

**bằng chứng (evidence / 증거):** duplicate count, xung đột (conflict / 충돌) count, source-to-sink reconciliation và replay kiểm thử (test / 테스트) trên một khoảng offset.

> **Chuyển mạch:** Trong **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Trường hợp (case / 사례) 1 — CDC duplicate sau thử lại (retry / 재시도)** cho ta quy tắc; **Trường hợp (case / 사례) 2 — Late sự kiện (event / 이벤트) làm thay đổi cửa sổ (window / 윈도우)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 3 — Backfill lô-gic (logic / 논리) mới không được ghi đè dữ liệu hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 2 — Late sự kiện (event / 이벤트) làm thay đổi cửa sổ (window / 윈도우)

**Tình huống:** thiết bị offline gửi sự kiện (event / 이벤트) 09:05 lúc 11:00; dashboard 09:00–10:00 đã finalize theo watermark.

**bất biến (invariant / 불변식):** chỉ số (metric / 지표) provisional/final phải được phân biệt; correction không tạo duplicate.

**Thiết kế:** lưu sự kiện (event / 이벤트) thời gian (time / 시간) và ingestion thời gian (time / 시간); late sự kiện (event / 이벤트) đi vào correction đường dẫn (path / 경로) hoặc tạo phiên bản (version / 버전) mới của aggregate; downstream biết chính sách (policy / 정책) finalization. trạng thái (state / 상태) retention đủ dài để replay trong late-arrival bound.

**bằng chứng (evidence / 증거):** watermark lag phân phối (distribution / 분포), late-event tỷ lệ (rate / 비율), correction reconciliation và số chỉ số (metric / 지표) đã publish lại.

> **Chuyển mạch:** Ở chặng này của **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Trường hợp (case / 사례) 2 — Late sự kiện (event / 이벤트) làm thay đổi cửa sổ (window / 윈도우)** cho ta quy tắc; **Trường hợp (case / 사례) 3 — Backfill lô-gic (logic / 논리) mới không được ghi đè dữ liệu hiện tại** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 4 — Small files và compaction race** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 3 — Backfill lô-gic (logic / 논리) mới không được ghi đè dữ liệu hiện tại

**Tình huống:** sửa timezone bug cho 12 tháng lịch sử trong khi partition hôm nay vẫn được streaming job ghi.

**bất biến (invariant / 불변식):** writer lịch sử và writer hiện tại không làm mất cập nhật (update / 업데이트) của nhau; đầu ra (output / 출력) chỉ công khai (public / 공개) khi reconciliation đạt.

**Thiết kế:** chạy backfill theo snapshot/phiên bản (version / 버전) không gian tên (namespace / 네임스페이스), ghi mục tiêu (target / 대상) partitions riêng, so sánh row count/chỉ số (metric / 지표), rồi publish atomic pointer hoặc partition lần ghi nhận (commit / 커밋). Side tác động (effect / 효과) ngoài dữ liệu (data / 데이터) tầng (layer / 계층) bị tắt hoặc deduplicate.

**bằng chứng (evidence / 증거):** đầu vào (input / 입력)/mã (code / 코드) phiên bản (version / 버전), mục tiêu (target / 대상) phạm vi (range / 범위), diff metrics, quay lui (rollback / 롤백) marker và bên tiêu thụ (consumer / 소비자) cutover thời gian (time / 시간).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Trường hợp (case / 사례) 3 — Backfill lô-gic (logic / 논리) mới không được ghi đè dữ liệu hiện tại** cho ta quy tắc; **Trường hợp (case / 사례) 4 — Small files và compaction race** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Trường hợp (case / 사례) 5 — ngữ nghĩa (semantic / 의미적) chỉ số (metric / 지표) fan-out** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 4 — Small files và compaction race

**Tình huống:** micro-batch tạo hàng triệu tệp (file / 파일) nhỏ; compaction chạy đồng thời với reader và writer.

**bất biến (invariant / 불변식):** reader thấy một snapshot hợp lệ; tệp (file / 파일) chưa lần ghi nhận (commit / 커밋) không được đọc; tệp (file / 파일) cũ chỉ xóa sau retention.

**Thiết kế:** siêu dữ liệu (metadata / 메타데이터) lần ghi nhận (commit / 커밋) xác định snapshot, compaction tạo files mới trước, publish pointer sau kiểm tra hợp lệ (validation / 검증), garbage collection tách khỏi lần ghi nhận (commit / 커밋). truy vấn (query / 쿼리)/compaction có sức chứa (capacity / 용량) ngân sách (budget / 예산) riêng.

**bằng chứng (evidence / 증거):** snapshot lineage, tệp (file / 파일) count/kích thước (size / 크기) phân phối (distribution / 분포), reader lỗi (error / 오류) tỷ lệ (rate / 비율), compaction ghi (write / 쓰기) amplification và restore kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Trường hợp (case / 사례) 4 — Small files và compaction race** cho ta quy tắc; **Trường hợp (case / 사례) 5 — ngữ nghĩa (semantic / 의미적) chỉ số (metric / 지표) fan-out** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cách viết trường hợp (case / 사례) study mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) 5 — ngữ nghĩa (semantic / 의미적) chỉ số (metric / 지표) fan-out

**Tình huống:** dashboard doanh thu phép nối (join / 조인) thứ tự (order / 순서), item và payment attempt ở grain khác nhau.

**bất biến (invariant / 불변식):** chỉ số (metric / 지표) amount được tính đúng grain và có definition phiên bản (version / 버전).

**Thiết kế:** aggregate mỗi fact về grain chỉ số (metric / 지표) trước khi phép nối (join / 조인); chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약) nêu refund, currency, sự kiện (event / 이벤트) thời gian (time / 시간) và null chính sách (policy / 정책); ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) không cho phép phép nối (join / 조인) đường dẫn (path / 경로) mơ hồ.

**bằng chứng (evidence / 증거):** reconciliation với ledger, cardinality check, golden queries và chỉ số (metric / 지표) phiên bản (version / 버전) diff.

> **Chuyển mạch:** Ở chặng này của **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Trường hợp (case / 사례) 5 — ngữ nghĩa (semantic / 의미적) chỉ số (metric / 지표) fan-out** cho ta quy tắc; **Cách viết trường hợp (case / 사례) study mới** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Ma trận đối chiếu trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách viết trường hợp (case / 사례) study mới

Mỗi trường hợp (case / 사례) phải có `context → invariant → failure boundary → design → evidence → trade-off`. Không biến trường hợp (case / 사례) study thành tutorial API; mục tiêu là chứng minh lập luận (reasoning / 추론) có thể chuyển giữa các công cụ (tool / 도구) và nền tảng (platform / 플랫폼).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Cách viết trường hợp (case / 사례) study mới** cho ta quy tắc; **Ma trận đối chiếu trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Câu hỏi cấp cao (senior / 시니어) cho mọi trường hợp (case / 사례)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ma trận đối chiếu trường hợp (case / 사례)

| trường hợp (case / 사례) | Primary thời gian (time / 시간) | trạng thái (state / 상태) | khôi phục (recovery / 복구) đơn vị (unit / 단위) | bằng chứng (evidence / 증거) |
|---|---|---|---|---|
| CDC duplicate | nguồn (source / 소스) giao dịch (transaction / 트랜잭션) thời gian (time / 시간) | dedup projection | offset phạm vi (range / 범위) / snapshot | source-to-sink reconciliation |
| late sự kiện (event / 이벤트) | sự kiện (event / 이벤트) thời gian (time / 시간) | cửa sổ (window / 윈도우) trạng thái (state / 상태) | watermark phạm vi (range / 범위) | late-rate + correction diff |
| backfill race | partition effective thời gian (time / 시간) | đầu ra (output / 출력) phiên bản (version / 버전) | manifest phạm vi (range / 범위) | chỉ số (metric / 지표)/golden diff |
| compaction race | snapshot lần ghi nhận (commit / 커밋) thời gian (time / 시간) | siêu dữ liệu (metadata / 메타데이터) snapshot | snapshot id | tệp (file / 파일)/snapshot kiểm tra hợp lệ (validation / 검증) |
| ngữ nghĩa (semantic / 의미적) fan-out | chỉ số (metric / 지표) thời gian (time / 시간) | aggregate trạng thái (state / 상태) | mô hình (model / 모델) phiên bản (version / 버전) | grain/cardinality check |

> **Chuyển mạch:** Trong **90 — trường hợp (case / 사례) studies: lập luận (reasoning / 추론) end-to-end**, **Ma trận đối chiếu trường hợp (case / 사례)** cho ta quy tắc; **Câu hỏi cấp cao (senior / 시니어) cho mọi trường hợp (case / 사례)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Câu hỏi cấp cao (senior / 시니어) cho mọi trường hợp (case / 사례)

1. Điều gì xảy ra nếu tiến trình (process / 프로세스) chết ngay sau bên ngoài (external / 외부) side tác động (effect / 효과)?
2. Có thể replay cùng đầu vào (input / 입력) nhưng khác mã (code / 코드)/lược đồ (schema / 스키마) phiên bản (version / 버전) không?
3. bên tiêu thụ (consumer / 소비자) nhìn thấy provisional, partial hay stale đầu ra (output / 출력) thế nào?
4. bất biến (invariant / 불변식) nào được kiểm tra online và bất biến (invariant / 불변식) nào chỉ kiểm tra offline?
5. Chi phí khôi phục (recovery / 복구) tăng theo đầu vào (input / 입력) volume, trạng thái (state / 상태) kích thước (size / 크기) hay phụ thuộc (dependency / 의존성) count?

Trường hợp (case / 사례) study chỉ hoàn thành khi trả lời được cả tính đúng đắn (correctness / 정확성) và operability. Một sơ đồ đẹp nhưng không có thất bại (failure / 실패) timeline, quay lui (rollback / 롤백) bằng chứng (evidence / 증거) và đơn vị sở hữu (owner / 오너) không phải môi trường vận hành (production / 운영 환경) thiết kế (design / 설계).

> **Bàn giao:** Sau **Câu hỏi cấp cao (senior / 시니어) cho mọi trường hợp (case / 사례)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
