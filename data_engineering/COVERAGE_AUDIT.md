# Kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) — Coverage kiểm tra (audit / 감사)

> **Mạch đọc:** Đặt **kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) — Coverage kiểm tra (audit / 감사)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Trạng thái coverage** sang **bất biến (invariant / 불변식) checklist**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Cập nhật: 2026-09-23. `main` là nguồn chuẩn (source of truth / 정본) của kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링).

Kiểm tra (audit / 감사) này kiểm tra thư viện (library / 라이브러리) theo chuỗi:

```text
source → capture → storage → model → distributed/stream processing
       → orchestration → serving → governance → cost/recovery
```

Mỗi ranh giới (boundary / 경계) phải mô tả được cơ chế (mechanism / 메커니즘), bất biến (invariant / 불변식), dạng thất bại (failure mode / 실패 모드), bằng chứng (evidence / 증거) và sự đánh đổi (trade-off / 트레이드오프). Không đánh giá độ sâu bằng số lượng từ khóa (keyword / 키워드) công cụ (tool / 도구).

## Trạng thái coverage

| Chapter | ranh giới (boundary / 경계) chính | Trạng thái |
|---|---|---|
| 01 Foundations | vòng đời (lifecycle / 생명주기), OLTP/OLAP, tính đúng đắn (correctness / 정확성), bất biến (invariant / 불변식) | Strong |
| 02 chuỗi xử lý (pipeline / 파이프라인) kiến trúc (architecture / 아키텍처) | CDC, delivery, checkpoint, replay, backfill | Strong |
| 03 lưu trữ (storage / 저장소) and formats | bố cục (layout / 레이아웃), pruning, files, snapshots, lược đồ (schema / 스키마) evolution | Strong |
| 04 độ tin cậy (reliability / 신뢰성) and môi trường vận hành (production / 운영 환경) | chất lượng (quality / 품질), SLO, lineage, khôi phục (recovery / 복구), bảo mật (security / 보안), chi phí (cost / 비용) | Strong |
| 05 Modeling and transformation | grain, định danh (identity / 식별자), temporal phép nối (join / 조인), sự kiện (event / 이벤트)/trạng thái (state / 상태)/snapshot | Strong |
| 06 phân tán (distributed / 분산) processing | partition, shuffle, skew, spill, thử lại (retry / 재시도) determinism | Strong |
| 07 Streaming các hệ thống (systems / 시스템들) | sự kiện (event / 이벤트) thời gian (time / 시간), watermark, trạng thái (state / 상태), CDC handoff, backpressure | Strong |
| 08 Orchestration and backfill | manifest, fencing, partition completeness, thử lại (retry / 재시도) taxonomy | Strong |
| 09 Warehouse/lake/lakehouse | snapshot isolation, compaction, delete, maintenance | Strong |
| 10 Serving/ngữ nghĩa (semantic / 의미적) tầng (layer / 계층) | chỉ số (metric / 지표) algebra, versioning, point-in-time, bộ nhớ đệm (cache / 캐시) | Strong |
| 11 quản trị (governance / 거버넌스)/lineage/bảo mật (security / 보안) | đặc tả hợp đồng (contract / 계약), quyền sở hữu (ownership / 소유권), chính sách (policy / 정책), lineage confidence, deletion | Strong |
| 12 chi phí (cost / 비용)/hiệu năng (performance / 성능)/sức chứa (capacity / 용량) | queueing, saturation, attribution, ngữ nghĩa (semantic / 의미적) guardrails | Strong |
| 13 Approximate computation | sketches, sampling, mergeability, lỗi (error / 오류) bounds | Strong |
| 14 Multi-region/residency | replication lag, xung đột (conflict / 충돌), failover, RPO/RTO, residency | Strong |
| 15 ML tính năng (feature / 기능) nền tảng (platform / 플랫폼) | point-in-time joins, offline/online parity, deletion | Strong |
| 16 Privacy-preserving analytics | threat mô hình (model / 모델), differential privacy, composition, bản phát hành (release / 릴리스) chính sách (policy / 정책) | Strong |
| 17 đặc tả hợp đồng (contract / 계약) testing | tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), bên tiêu thụ (consumer / 소비자) contracts, thời gian chạy (runtime / 런타임) enforcement | Strong |
| 90 trường hợp (case / 사례) studies | end-to-end thất bại (failure / 실패) and bằng chứng (evidence / 증거) lập luận (reasoning / 추론) | Strong |


> **Chuyển mạch:** Từ **Trạng thái coverage**, ta sang **bất biến (invariant / 불변식) checklist** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bất biến (invariant / 불변식) checklist

- **định danh (identity / 식별자):** duplicate, cập nhật (update / 업데이트), delete và correction có định danh (identity / 식별자)/phiên bản (version / 버전) rõ.
- **thời gian (time / 시간):** sự kiện (event / 이벤트) thời gian (time / 시간), processing thời gian (time / 시간), ingestion thời gian (time / 시간) và snapshot thời gian (time / 시간) không bị trộn.
- **Grain:** mỗi row/chỉ số (metric / 지표) có grain; phép nối (join / 조인) cardinality được kiểm tra trước aggregate.
- **Visibility:** đầu ra (output / 출력) chỉ công khai (public / 공개) qua lần ghi nhận (commit / 커밋) marker/snapshot hợp lệ.
- **Replay:** đầu vào (input / 입력), mã (code / 코드), lược đồ (schema / 스키마), trạng thái (state / 상태) và side tác động (effect / 효과) có phiên bản (version / 버전)/khôi phục (recovery / 복구) chính sách (policy / 정책).
- **Evolution:** lược đồ (schema / 스키마)/chỉ số (metric / 지표) thay đổi (change / 변경) có tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), đơn vị sở hữu (owner / 오너) và deprecation cửa sổ (window / 윈도우).
- **chất lượng (quality / 품질):** freshness, completeness, tính đúng đắn (correctness / 정확성) và availability có SLO riêng.
- **bảo mật (security / 보안):** raw/mô hình (model / 모델)/serving truy cập (access / 접근), masking, retention và deletion có bằng chứng (evidence / 증거).
- **Economics:** scan, shuffle, spill, lưu trữ (storage / 저장소), maintenance và tính đồng thời (concurrency / 동시성) có attribution.


> **Chuyển mạch:** Từ **bất biến (invariant / 불변식) checklist**, ta sang **Gaps còn lại** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Gaps còn lại

Các ranh giới (boundary / 경계) P2 phía trên đã có chapter chuẩn gốc (canonical / 정본). Những gap tiếp theo nên được mở chỉ khi có conceptual ranh giới (boundary / 경계) độc lập:

1. **Approximate truy vấn (query / 쿼리) operations:** lan truyền lỗi (error propagation / 오류 전파) qua nhiều chỉ số (metric / 지표) và calibration theo segment.
2. **Multi-region active-active:** nhân quả (causal / 인과적) thứ tự (ordering / 순서), conflict-free merge và residency-aware routing.
3. **ML tính năng (feature / 기능) operations:** drift, training-serving parity ở quy mô (scale / 규모) và mô hình (model / 모델) quay lui (rollback / 롤백) với tính năng (feature / 기능) phiên bản (version / 버전).
4. **Privacy composition:** privacy accountant liên lĩnh vực (domain / 도메인) và utility evaluation cho truy vấn (query / 쿼리) tải công việc (workload / 워크로드) thật.
5. **đặc tả hợp đồng (contract / 계약) nền tảng (platform / 플랫폼):** lược đồ (schema / 스키마)/ngữ nghĩa (semantic / 의미적) registry, exception expiry và automated blast-radius đồ thị (graph / 그래프).

Không mở chapter chỉ để liệt kê Kafka/Spark/Airflow/dbt. Mỗi gap phải có bất biến (invariant / 불변식)/thất bại (failure / 실패) mô hình (model / 모델) riêng, nhiều downstream phụ thuộc (dependency / 의존성) và bằng chứng (evidence / 증거) có thể kiểm chứng.


> **Chuyển mạch:** Từ **Gaps còn lại**, ta sang **rà soát (review / 검토) giao thức (protocol / 프로토콜)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Rà soát (review / 검토) giao thức (protocol / 프로토콜)

Khi sửa một chapter:

1. thêm hoặc cập nhật cơ chế (mechanism / 메커니즘) và bất biến (invariant / 불변식);
2. thêm ít nhất một thất bại (failure / 실패)/trường hợp biên (edge case / 경계 사례);
3. nêu bằng chứng (evidence / 증거)/chỉ số (metric / 지표) để phân biệt success giả với success thật;
4. kiểm tra link và phụ thuộc (dependency / 의존성) map;
5. chạy `npm run audit:library` và `npm run build:library` nếu thay đổi ảnh hưởng publishing.

> **Bàn giao:** Sau **rà soát (review / 검토) giao thức (protocol / 프로토콜)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 foundations](./01_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
