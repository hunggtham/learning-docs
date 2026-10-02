# 05 — dữ liệu (data / 데이터) modeling và transformation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **05 — dữ liệu (data / 데이터) modeling và transformation**. Route đi từ grain → identity và deduplication → history/slowly changing data → joins, aggregates và business meaning → contracts/tests, để transformation không làm mơ hồ dữ liệu.

Mô hình dữ liệu (data model / 데이터 모델) là cách biến bản ghi (record / 레코드) có nguồn gốc khác nhau thành một đặc tả hợp đồng (contract / 계약) mà bên tiêu thụ (consumer / 소비자) có thể hiểu. Mục tiêu không phải là tạo thật nhiều bảng (table / 테이블), mà là làm cho **grain, định danh (identity / 식별자), lịch sử (history / 이력) và nghiệp vụ (business / 비즈니스) meaning** không bị mơ hồ sau mỗi lần phép nối (join / 조인) hoặc aggregate.

## 1. Grain trước lược đồ (schema / 스키마)

Trước khi chọn column, viết một câu: “mỗi row đại diện cho ...”. Một row có thể là một `order`, một `order_item`, một `payment_attempt`, một sự kiện (event / 이벤트) bất biến, hoặc một snapshot của customer tại ngày D. Nếu không xác định grain, mọi chỉ số (metric / 지표) phía sau đều có nguy cơ bị nhân bản.

Ví dụ một thứ tự (order / 순서) có 3 item và 2 payment attempt. phép nối (join / 조인) trực tiếp ba bảng tạo 6 row; `SUM(order_amount)` sẽ sai dù SQL hợp lệ. Cách an toàn là aggregate mỗi nguồn về grain cần thiết trước khi phép nối (join / 조인), hoặc dùng bảng cầu nối (bridge / 브리지) có bất biến (invariant / 불변식) rõ ràng.

> **Chuyển mạch:** Trong **05 — dữ liệu (data / 데이터) modeling và transformation**, **2. định danh (identity / 식별자) và deduplication** tiếp nhận điểm tựa từ **1. Grain trước lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. sự kiện (event / 이벤트), trạng thái (state / 상태) và snapshot** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. định danh (identity / 식별자) và deduplication

`id` của nguồn (source / 소스) không luôn là định danh (identity / 식별자) của nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트). Một thử lại (retry / 재시도) có thể tạo cùng `event_id`, một hệ thống migrate có thể đổi key, hoặc hai nguồn cùng đại diện một customer. mô hình (model / 모델) phải phân biệt:

- technical key: định danh row trong lưu trữ (storage / 저장소);
- nghiệp vụ (business / 비즈니스) key: định danh thực thể theo lĩnh vực (domain / 도메인);
- sự kiện (event / 이벤트) định danh (identity / 식별자): định danh một occurrence bất biến;
- phiên bản (version / 버전)/effective thời gian (time / 시간): thứ tự và thời gian hiệu lực của trạng thái (state / 상태).

Deduplication không nên dùng “row mới nhất” một cách mù quáng. quy tắc (rule / 규칙) phải nêu rõ tie-breaker, cửa sổ nhận diện duplicate và xử lý khi hai payload cùng key nhưng khác nội dung.

> **Chuyển mạch:** Ở chặng này của **05 — dữ liệu (data / 데이터) modeling và transformation**, **3. sự kiện (event / 이벤트), trạng thái (state / 상태) và snapshot** tiếp nhận điểm tựa từ **2. định danh (identity / 식별자) và deduplication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Transformation deterministic** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. sự kiện (event / 이벤트), trạng thái (state / 상태) và snapshot

Sự kiện (event / 이벤트) trả lời “điều gì đã xảy ra”; trạng thái (state / 상태) trả lời “hiện tại đang là gì”; snapshot trả lời “tại thời điểm T hệ thống quan sát điều gì”. Không thể thay thế chúng cho nhau:

```text
event log → state projection → periodic snapshot
```

Sự kiện (event / 이벤트) log giúp replay nhưng có thể đắt để truy vấn (query / 쿼리). trạng thái (state / 상태) projection phục vụ lookup nhanh nhưng mất lịch sử (history / 이력) nếu không lưu phiên bản (version / 버전). Snapshot thuận tiện cho point-in-time reporting nhưng phải định nghĩa completeness và late correction.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — dữ liệu (data / 데이터) modeling và transformation**, **4. Transformation deterministic** tiếp nhận điểm tựa từ **3. sự kiện (event / 이벤트), trạng thái (state / 상태) và snapshot** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Slowly changing lịch sử (history / 이력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Transformation deterministic

Transformation tốt nhận đầu vào (input / 입력) phiên bản (version / 버전) rõ ràng và tạo đầu ra (output / 출력) có thể tái tạo. Tránh đọc clock hiện tại, random giá trị (value / 값) hoặc bên ngoài (external / 외부) API không phiên bản (version / 버전) trong phép biến đổi recomputable. Nếu cần enrichment bên ngoài, lưu lại tham chiếu (reference / 참조)/phiên bản (version / 버전) của enrichment để backfill không tạo kết quả khác chỉ vì thời gian chạy khác.

Idempotent mô hình (model / 모델) thường dùng `MERGE` theo nghiệp vụ (business / 비즈니스)/sự kiện (event / 이벤트) key, overwrite theo partition, hoặc tạo đầu ra (output / 출력) phiên bản (version / 버전) mới rồi publish pointer. `INSERT` nối tiếp không đủ an toàn cho replay nếu không có uniqueness bất biến (invariant / 불변식).

> **Chuyển mạch:** Trong **05 — dữ liệu (data / 데이터) modeling và transformation**, **5. Slowly changing lịch sử (history / 이력)** tiếp nhận điểm tựa từ **4. Transformation deterministic** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Transformation ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Slowly changing lịch sử (history / 이력)

Với dimension thay đổi theo thời gian, phải chọn ngữ nghĩa (semantics / 의미론):

- kiểu (type / 타입) 1: chỉ giữ giá trị mới nhất;
- kiểu (type / 타입) 2: giữ các phiên bản với `valid_from`, `valid_to`, `is_current`;
- event-sourced: giữ mutation và dựng trạng thái (state / 상태) khi cần.

Không có lựa chọn “đúng tuyệt đối”. kiểu (type / 타입) 1 đơn giản nhưng không trả lời được câu hỏi lịch sử. kiểu (type / 타입) 2 dễ truy vấn (query / 쿼리) hơn sự kiện (event / 이벤트) log nhưng cần xử lý late correction, overlap và cùng thời điểm hiệu lực.

> **Chuyển mạch:** Ở chặng này của **05 — dữ liệu (data / 데이터) modeling và transformation**, **5. Slowly changing lịch sử (history / 이력)** đã nêu tiêu chí phân biệt, còn **6. Transformation ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. Checklist rà soát (review / 검토) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Transformation ranh giới (boundary / 경계)

Raw tầng (layer / 계층) giữ bằng chứng (evidence / 증거) gần nguồn (source / 소스); modeled tầng (layer / 계층) chuẩn hóa grain, key và ngữ nghĩa (semantics / 의미론); serving tầng (layer / 계층) tối ưu cho bên tiêu thụ (consumer / 소비자). Đừng làm sạch đến mức mất payload gốc trước khi xác định retention/kiểm tra (audit / 감사) yêu cầu (requirement / 요구사항). Ngược lại, đừng đẩy mọi lô-gic (logic / 논리) vào serving khiến mỗi dashboard tự định nghĩa chỉ số (metric / 지표) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — dữ liệu (data / 데이터) modeling và transformation**, **6. Transformation ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **7. Checklist rà soát (review / 검토) mô hình (model / 모델)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **8. Snapshot fact và temporal phép nối (join / 조인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Checklist rà soát (review / 검토) mô hình (model / 모델)

1. Grain của mỗi đầu vào (input / 입력)/đầu ra (output / 출력) là gì?
2. Key nào bảo đảm uniqueness và định danh (identity / 식별자)?
3. phép nối (join / 조인) cardinality có thể fan-out ở đâu?
4. Replay cùng đầu vào (input / 입력)/phiên bản (version / 버전) có tạo cùng đầu ra (output / 출력) không?
5. Late correction và delete được biểu diễn thế nào?
6. bên tiêu thụ (consumer / 소비자) nào phụ thuộc lược đồ (schema / 스키마)/chỉ số (metric / 지표) này?
7. Có thể reconcile đầu ra (output / 출력) với nguồn (source / 소스) hoặc upstream bất biến (invariant / 불변식) nào?

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [08 — Orchestration và backfill](../08_orchestration_and_backfill/README.md), [10 — Serving và semantic layer](../10_serving_semantic_layer/README.md).

> **Chuyển mạch:** Trong **05 — dữ liệu (data / 데이터) modeling và transformation**, **8. Snapshot fact và temporal phép nối (join / 조인)** tiếp nhận điểm tựa từ **7. Checklist rà soát (review / 검토) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Null, unknown và deleted** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Snapshot fact và temporal phép nối (join / 조인)

Một fact sự kiện (event / 이벤트) thường có `occurred_at`, `captured_at` và `loaded_at`. Khi dựng snapshot ngày D, filter theo `occurred_at` chưa đủ: sự kiện (event / 이벤트) có thể được capture sau khi snapshot đã publish. Cần chọn một trong hai ngữ nghĩa (semantics / 의미론):

- snapshot as-of sự kiện (event / 이벤트) thời gian (time / 시간): phản ánh lĩnh vực (domain / 도메인) tại D và chấp nhận late correction;
- snapshot as-observed: phản ánh nền tảng (platform / 플랫폼) đã biết gì tại D và không backdate sự kiện (event / 이벤트).

Hai ngữ nghĩa (semantics / 의미론) cho hai câu hỏi khác nhau. Không đặt tên chung như `daily_sales` nếu không ghi rõ kiểu snapshot.

Temporal phép nối (join / 조인) giữa fact và dimension phải chọn phiên bản (version / 버전) thỏa `valid_from <= event_time < valid_to`. Nếu dimension có hai phiên bản (version / 버전) cùng effective thời gian (time / 시간), cần tie-breaker deterministic. phép nối (join / 조인) với row `is_current = true` là shortcut nguy hiểm cho lịch sử.

> **Chuyển mạch:** Ở chặng này của **05 — dữ liệu (data / 데이터) modeling và transformation**, **9. Null, unknown và deleted** tiếp nhận điểm tựa từ **8. Snapshot fact và temporal phép nối (join / 조인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Transformation kiểm thử (test / 테스트) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Null, unknown và deleted

`NULL` có thể nghĩa là unknown, not-applicable, chưa nhận được hoặc đã bị redact. Nếu gom tất cả vào một giá trị, aggregate và chất lượng (quality / 품질) check sẽ sai. Nên dùng ngữ nghĩa (semantic / 의미적) enum/flags khi lĩnh vực (domain / 도메인) cần phân biệt.

Delete cũng có nhiều nghĩa: thực thể (entity / 엔터티) bị xóa thật, bản ghi (record / 레코드) bị retract, privacy deletion, hoặc nguồn (source / 소스) chỉ không còn trả row. mô hình (model / 모델) phải biết tombstone nào là nghiệp vụ (business / 비즈니스) sự kiện (event / 이벤트) và tombstone nào là lưu trữ (storage / 저장소) cleanup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **05 — dữ liệu (data / 데이터) modeling và transformation**, **10. Transformation kiểm thử (test / 테스트) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **9. Null, unknown và deleted** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 10. Transformation kiểm thử (test / 테스트) ma trận (matrix / 행렬)

Kiểm thử (test / 테스트) mô hình (model / 모델) không chỉ dùng một happy-path fixture. Tối thiểu cần có:

```text
duplicate event
late correction
missing dimension
duplicate dimension version
empty partition
timezone boundary / DST
currency or unit conversion
```

Mỗi fixture nên kiểm tra cả expected rows và bất biến (invariant / 불변식) tổng hợp. Một mô hình (model / 모델) có thể trả đúng mẫu (sample / 표본) row nhưng sai tổng vì fan-out hoặc filter null.

> **Bàn giao:** Sau **10. Transformation kiểm thử (test / 테스트) ma trận (matrix / 행렬)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
