# 10 — Serving tầng (layer / 계층) và ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)

> **Mạch đọc:** Đọc **10 — Serving tầng (layer / 계층) và ngữ nghĩa (semantic / 의미적) tầng (layer / 계층)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Các serving shape** sang **2. chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Serving biến modeled dữ liệu (data / 데이터) thành giao diện (interface / 인터페이스) mà người khác dùng: dashboard, chỉ số (metric / 지표) API, tính năng (feature / 기능) chuỗi xử lý (pipeline / 파이프라인), reverse ETL hoặc operational read mô hình (model / 모델). ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) bảo đảm hai bên tiêu thụ (consumer / 소비자) không tự định nghĩa “revenue”, “active người dùng (user / 사용자)” và “thứ tự (order / 순서)” theo ba cách khác nhau.

## 1. Các serving shape

- analytical bảng (table / 테이블): scan và aggregate lớn;
- dimensional mô hình (model / 모델): phép nối (join / 조인) theo dimension/fact với grain rõ;
- materialized aggregate: độ trễ (latency / 지연 시간) thấp cho chỉ số (metric / 지표) ổn định;
- ngữ nghĩa (semantic / 의미적) chỉ số (metric / 지표): định nghĩa measure, dimension, filter và thời gian (time / 시간) grain;
- API/read mô hình (model / 모델): shape theo truy cập (access / 접근) mẫu (pattern / 패턴) của ứng dụng;
- tính năng (feature / 기능) view: point-in-time correct cho machine học tập (learning / 학습).

Không có serving shape tốt cho mọi bên tiêu thụ (consumer / 소비자). Dùng cùng một bảng cho BI ad-hoc và online API thường tạo xung đột (conflict / 충돌) về độ trễ (latency / 지연 시간), cập nhật (update / 업데이트) và lược đồ (schema / 스키마).


> **Chuyển mạch:** Từ **1. Các serving shape**, ta sang **2. chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약)

Một chỉ số (metric / 지표) cần nêu:

```text
name + grain + numerator/denominator + time semantics
→ filters + null policy + late-data policy
→ owner + freshness SLO + version/deprecation
```

“Revenue” có tính refund không? Dùng sự kiện (event / 이벤트) thời gian (time / 시간) hay paid_at? Currency conversion ở đâu? Câu hỏi này là đặc tả hợp đồng (contract / 계약), không phải chi tiết dashboard.


> **Chuyển mạch:** Từ **2. chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약)**, ta sang **3. Point-in-time tính đúng đắn (correctness / 정확성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Point-in-time tính đúng đắn (correctness / 정확성)

Tính năng (feature / 기능) hoặc report lịch sử không được dùng dimension của tương lai. Khi phép nối (join / 조인) fact sự kiện (event / 이벤트) với customer trạng thái (state / 상태), phải chọn phiên bản (version / 버전) có `effective_time <= event_time` và xử lý tie-breaker. phép nối (join / 조인) theo trạng thái hiện tại có thể tạo dữ liệu (data / 데이터) leakage trong ML và lịch sử sai trong analytics.


> **Chuyển mạch:** Từ **3. Point-in-time tính đúng đắn (correctness / 정확성)**, ta sang **4. Materialization và freshness** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Materialization và freshness

Materialized kết quả (result / 결과) giảm độ trễ (latency / 지연 시간) nhưng cần refresh chính sách (policy / 정책), vô hiệu hóa (invalidation / 무효화), backfill và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프). Freshness timestamp chỉ cho biết lúc job chạy; cần thêm completeness và nguồn (source / 소스) watermark để biết dữ liệu (data / 데이터) có đủ hay chưa.

Serving nên công khai (public / 공개) một phiên bản (version / 버전)/snapshot atomically. bên tiêu thụ (consumer / 소비자) không nên thấy nửa đầu ra (output / 출력) cũ/nửa đầu ra (output / 출력) mới.


> **Chuyển mạch:** Từ **4. Materialization và freshness**, ta sang **5. ngữ nghĩa (semantic / 의미적) consistency** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. ngữ nghĩa (semantic / 의미적) consistency

Chỉ số (metric / 지표) lô-gic (logic / 논리) nên được định nghĩa một lần và reuse, nhưng ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) không nên che giấu grain hoặc truy vấn (query / 쿼리) chi phí (cost / 비용). Nếu chỉ số (metric / 지표) phép nối (join / 조인) nhiều fact khác grain, đặc tả hợp đồng (contract / 계약) phải nêu pre-aggregation hoặc allowed dimensions.

Versioning chỉ số (metric / 지표) là cần thiết khi nghiệp vụ (business / 비즈니스) meaning thay đổi. Đổi lô-gic (logic / 논리) âm thầm làm thời gian (time / 시간) series discontinuity mà không có lược đồ (schema / 스키마) lỗi (error / 오류).


> **Chuyển mạch:** Từ **5. ngữ nghĩa (semantic / 의미적) consistency**, ta sang **6. thất bại (failure / 실패) modes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. thất bại (failure / 실패) modes

- dashboard fresh nhưng thiếu partition;
- API trả số liệu stale vì bộ nhớ đệm (cache / 캐시) không invalidate;
- aggregate double-count do fan-out;
- ML tính năng (feature / 기능) dùng future trạng thái (state / 상태);
- chỉ số (metric / 지표) đổi filter nhưng giữ cùng tên;
- bên tiêu thụ (consumer / 소비자) đọc đầu ra (output / 출력) khi materialization chưa atomic.


> **Chuyển mạch:** Từ **6. thất bại (failure / 실패) modes**, ta sang **7. Serving rà soát (review / 검토)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Serving rà soát (review / 검토)

1. bên tiêu thụ (consumer / 소비자) cần độ trễ (latency / 지연 시간), freshness và consistency nào?
2. Grain và point-in-time quy tắc (rule / 규칙) có tường minh (explicit / 명시적) không?
3. chỉ số (metric / 지표) phiên bản (version / 버전), đơn vị sở hữu (owner / 오너) và deprecation có tồn tại không?
4. đầu ra (output / 출력) publish, bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화) và quay lui (rollback / 롤백) ra sao?
5. Có reconcile serving kết quả (result / 결과) với modeled/nguồn (source / 소스) tầng (layer / 계층) không?

Đọc tiếp: [05 — Modeling](../05_data_modeling_and_transformation/README.md), [04 — Reliability](../04_reliability_and_production.md), [11 — Governance](../11_governance_lineage_security/README.md).


> **Chuyển mạch:** Từ **7. Serving rà soát (review / 검토)**, ta sang **8. chỉ số (metric / 지표) algebra và composability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. chỉ số (metric / 지표) algebra và composability

Chỉ số (metric / 지표) nên có tính chất cho phép biết khi nào được aggregate tiếp. `SUM(revenue)` thường composable; `AVG(price)` phải giữ cả `sum` và `count`; `COUNT(DISTINCT user)` cần trạng thái (state / 상태)/merge thuật toán (algorithm / 알고리즘); percentile không thể cộng trực tiếp.

Ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) phải lưu measure definition và aggregation hành vi (behavior / 동작), không chỉ SQL expression. Nếu một dashboard aggregate chỉ số (metric / 지표) non-additive như additive, kết quả có thể sai mà không có lược đồ (schema / 스키마) lỗi (error / 오류).


> **Chuyển mạch:** Từ **8. chỉ số (metric / 지표) algebra và composability**, ta sang **9. ngữ nghĩa (semantic / 의미적) versioning** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. ngữ nghĩa (semantic / 의미적) versioning

Đổi filter, timezone, refund chính sách (policy / 정책) hoặc dimension phép nối (join / 조인) có thể làm chỉ số (metric / 지표) discontinuity. chỉ số (metric / 지표) phiên bản (version / 버전) cần có effective date, di chuyển (migration / 마이그레이션) ghi chú (note / 노트) và cách so sánh old/new:

```text
metric_v1 → dual-run → reconcile delta → metric_v2 → deprecate v1
```

Dual-run tốn compute nhưng tạo bằng chứng (evidence / 증거) cho bên tiêu thụ (consumer / 소비자). Không đổi tên chỉ số (metric / 지표) để che một thay đổi ngữ nghĩa (semantics / 의미론).


> **Chuyển mạch:** Từ **9. ngữ nghĩa (semantic / 의미적) versioning**, ta sang **10. bộ nhớ đệm (cache / 캐시) và vô hiệu hóa (invalidation / 무효화)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. bộ nhớ đệm (cache / 캐시) và vô hiệu hóa (invalidation / 무효화)

Bộ nhớ đệm (cache / 캐시) key phải bao gồm chỉ số (metric / 지표) phiên bản (version / 버전), filter, thời gian (time / 시간) phạm vi (range / 범위) và nguồn (source / 소스) snapshot/freshness ranh giới (boundary / 경계). Invalidate theo thời gian cố định có thể trả stale giá trị (value / 값) sau correction; invalidate mỗi sự kiện (event / 이벤트) có thể quá đắt.

Serving đặc tả hợp đồng (contract / 계약) nên nêu `as_of`, freshness và correction hành vi (behavior / 동작) để bên tiêu thụ (consumer / 소비자) biết giá trị đang provisional hay final. bộ nhớ đệm (cache / 캐시) không được trở thành một bản bản sao (copy / 복사) không có lineage.


> **Chuyển mạch:** Từ **10. bộ nhớ đệm (cache / 캐시) và vô hiệu hóa (invalidation / 무효화)**, ta sang **11. Golden dataset** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 11. Golden dataset

Mỗi chỉ số (metric / 지표) quan trọng nên có golden fixture nhỏ với expected đầu ra (output / 출력) cho timezone ranh giới (boundary / 경계), refund, duplicate, late correction, null và multi-currency. Chạy golden truy vấn (query / 쿼리) trong CI và sau materialization giúp phát hiện ngữ nghĩa (semantic / 의미적) regression mà row-count check không thấy.

> **Bàn giao:** Sau **11. Golden dataset**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
