# Thư viện kiến thức kỹ thuật dữ liệu (data engineering knowledge library / 데이터 엔지니어링 지식 라이브러리)

> **Mạch đọc:** Đọc **thư viện kiến thức kỹ thuật dữ liệu (data engineering knowledge library / 데이터 엔지니어링 지식 라이브러리)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Chuẩn độ sâu của chapter** sang **P1 — Trạng thái triển khai**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) là lĩnh vực xây dựng các hệ thống biến dữ liệu thô, phân tán và thường không đáng tin cậy thành dữ liệu có cấu trúc, có ngữ nghĩa, có thể kiểm chứng và đủ ổn định để phục vụ phân tích, sản phẩm dữ liệu, machine học tập (learning / 학습) và vận hành doanh nghiệp.

Đọc [COVERAGE_AUDIT.md](COVERAGE_AUDIT.md) để xem cổng chất lượng (quality gate / 품질 게이트), bất biến (invariant / 불변식) checklist và các gap còn lại của toàn bộ thư viện (library / 라이브러리).

Thư viện (library / 라이브러리) này không được tổ chức như danh sách công cụ. Kafka, Spark, Airflow, dbt, một dữ liệu (data / 데이터) warehouse hay một cloud dịch vụ (service / 서비스) chỉ là các hiện thực cụ thể của những vấn đề sâu hơn: dữ liệu đến từ đâu, trạng thái nào là đúng, dữ liệu được lưu theo hình dạng nào, khi chạy lại chuỗi xử lý (pipeline / 파이프라인) có phá kết quả không, lược đồ (schema / 스키마) thay đổi thì điều gì xảy ra, một bản ghi (record / 레코드) đến muộn được xử lý thế nào, và khi dashboard sai thì làm sao lần ngược về nguyên nhân.

Mục tiêu học tập vì vậy đi theo chuỗi lập luận (reasoning / 추론):

`nguồn dữ liệu → ingestion → storage → modeling → transformation → serving → observation/governance`

Mỗi bước đều phải trả lời ba câu hỏi: bất biến (invariant / 불변식) nào cần được giữ, thất bại (failure / 실패) nào có thể phá bất biến (invariant / 불변식) đó, và bằng chứng (evidence / 증거) nào cho phép chứng minh hệ thống đang hoạt động đúng.

## Chuẩn độ sâu của chapter

Mỗi chapter chuẩn gốc (canonical / 정본) phải đi qua chuỗi:

```text
problem → mental model → mechanism → invariant
       → failure/edge case → evidence → trade-off → lower-layer connection
```

Nếu một phần chỉ mô tả API hoặc tên sản phẩm mà không nói guarantee và hành vi khi thất bại (failure behavior / 실패 동작), nó là hiện thực (implementation / 구현) ghi chú (note / 노트) chứ chưa phải kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) lập luận (reasoning / 추론).


> **Chuyển mạch:** Từ **Chuẩn độ sâu của chapter**, ta sang **P1 — Trạng thái triển khai** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## P1 — Trạng thái triển khai

P1 của kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) đã được triển khai, không còn là phần `Planned`. Bốn foundation chapter ban đầu được nối tiếp bằng các chapter dạng directory dưới đây. Tên trong rà soát (review / 검토) được giữ làm nhãn conceptual; tên chuẩn gốc (canonical / 정본) trong repository dài hơn để nêu rõ ranh giới (boundary / 경계) của từng chapter và tránh các thư mục mơ hồ.

| Nhãn trong rà soát (review / 검토) | Chapter chuẩn gốc (canonical / 정본) | Trạng thái |
|---|---|---|
| `05_data_modeling/` | [05 — Data modeling và transformation](05_data_modeling_and_transformation/README.md) | Implemented |
| `06_distributed_processing/` | [06 — Distributed processing](06_distributed_processing/README.md) | Implemented |
| `07_streaming/` | [07 — Streaming systems](07_streaming_systems/README.md) | Implemented |
| `08_orchestration_backfill/` | [08 — Orchestration và backfill](08_orchestration_and_backfill/README.md) | Implemented |
| `09_warehouse_lakehouse/` | [09 — Warehouse, lake và lakehouse](09_warehouse_lake_lakehouse/README.md) | Implemented |
| `10_semantic_serving/` | [10 — Serving và semantic layer](10_serving_semantic_layer/README.md) | Implemented |
| `11_governance_lineage/` | [11 — Governance, lineage và security](11_governance_lineage_security/README.md) | Implemented |
| `12_cost_capacity/` | [12 — Cost, performance và capacity](12_cost_performance_capacity/README.md) | Implemented |
| `90_case_studies/` | [90 — Case studies](90_case_studies/README.md) | Implemented |

Mỗi chapter có mô hình tư duy (mental model / 사고 모델), cơ chế (mechanism / 메커니즘), bất biến (invariant / 불변식), thất bại (failure / 실패)/trường hợp biên (edge case / 경계 사례), bằng chứng (evidence / 증거), sự đánh đổi (trade-off / 트레이드오프) và liên kết phụ thuộc (dependency / 의존성); `COVERAGE_AUDIT.md` là checklist kiểm tra coverage và bất biến (invariant / 불변식) của toàn bộ ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **P1 — Trạng thái triển khai**, ta sang **Lộ trình chuẩn gốc (canonical / 정본)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lộ trình chuẩn gốc (canonical / 정본)

Bắt đầu với [01 — Data Engineering từ first principles](01_foundations.md). Chapter này thiết lập mô hình tư duy (mental model / 사고 모델) về dữ liệu (data / 데이터) vòng đời (lifecycle / 생명주기), batch/streaming, OLTP/OLAP, tính đúng đắn (correctness / 정확성) và vì sao chuỗi xử lý (pipeline / 파이프라인) không đơn giản là "bản sao (copy / 복사) dữ liệu từ A sang B".

Tiếp theo đọc [02 — Kiến trúc pipeline và semantics](02_pipeline_architecture.md) để hiểu ingestion, ETL/ELT, CDC, idempotency, replay, delivery ngữ nghĩa (semantics / 의미론), sự kiện (event / 이벤트) thời gian (time / 시간) và backfill. Đây là lớp kiến thức cần có trước khi học một orchestration khung phần mềm (framework / 프레임워크) hoặc streaming engine cụ thể.

Sau đó đọc [03 — Storage, file format và analytical layout](03_storage_and_formats.md). Phần này giải thích row/column bố cục (layout / 레이아웃), Parquet, compression, partitioning, small-file bài toán (problem / 문제) và tại sao cách đặt dữ liệu vật lý ảnh hưởng trực tiếp đến truy vấn (query / 쿼리) chi phí (cost / 비용).

Cuối cùng đọc [04 — Reliability, quality và production reasoning](04_reliability_and_production.md), nơi chuỗi xử lý (pipeline / 파이프라인) được nhìn như một môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템): dữ liệu (data / 데이터) chất lượng (quality / 품질), contracts, lineage, khả năng quan sát (observability / 관측 가능성), thử lại (retry / 재시도), khôi phục (recovery / 복구), bảo mật (security / 보안) và chi phí (cost / 비용).


> **Chuyển mạch:** Từ **Lộ trình chuẩn gốc (canonical / 정본)**, ta sang **Lộ trình mở rộng theo conceptual ranh giới (boundary / 경계)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Lộ trình mở rộng theo conceptual ranh giới (boundary / 경계)

Sau bốn foundation chapters, đi theo các ranh giới (boundary / 경계) sau. Mỗi phần bắt đầu từ bất biến (invariant / 불변식) và dạng thất bại (failure mode / 실패 모드) rồi mới ánh xạ sang công cụ (tool / 도구):

1. [05 — Data modeling và transformation](05_data_modeling_and_transformation/README.md): grain, định danh (identity / 식별자), sự kiện (event / 이벤트)/trạng thái (state / 상태)/snapshot, lịch sử (history / 이력) và deterministic transformation.
2. [06 — Distributed processing](06_distributed_processing/README.md): partition → shuffle → skew → spill, phép nối (join / 조인) ngữ nghĩa (semantics / 의미론) và fault khôi phục (recovery / 복구).
3. [07 — Streaming systems](07_streaming_systems/README.md): sự kiện (event / 이벤트) thời gian (time / 시간) → watermark → trạng thái (state / 상태) → late sự kiện (event / 이벤트), CDC, lược đồ (schema / 스키마) evolution và replay.
4. [08 — Orchestration và backfill](08_orchestration_and_backfill/README.md): phụ thuộc (dependency / 의존성), partition completeness, thử lại (retry / 재시도), catchup và backfill tính đúng đắn (correctness / 정확성).
5. [09 — Warehouse, lake và lakehouse](09_warehouse_lake_lakehouse/README.md): snapshot, lần ghi nhận (commit / 커밋) giao thức (protocol / 프로토콜), compaction, lược đồ (schema / 스키마) evolution và object-storage boundaries.
6. [10 — Serving và semantic layer](10_serving_semantic_layer/README.md): chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약), point-in-time tính đúng đắn (correctness / 정확성), materialization và bên tiêu thụ (consumer / 소비자) shape.
7. [11 — Governance, lineage và security](11_governance_lineage_security/README.md): quyền sở hữu (ownership / 소유권), dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약), lineage, truy cập (access / 접근), retention và deletion.
8. [12 — Cost, performance và capacity](12_cost_performance_capacity/README.md): scan, shuffle, spill, small files, tính đồng thời (concurrency / 동시성) và đơn vị (unit / 단위) economics.
9. [13 — Approximate computation](13_approximate_computation/README.md): sketches, sampling, mergeability, quantile/cardinality lỗi (error / 오류) và bất định (uncertainty / 불확실성) đặc tả hợp đồng (contract / 계약).
10. [14 — Multi-region và residency](14_multi_region_and_residency/README.md): replication lag, xung đột (conflict / 충돌), failover, RPO/RTO và dữ liệu (data / 데이터) residency.
11. [15 — ML feature platform](15_ml_feature_platform/README.md): point-in-time tính đúng đắn (correctness / 정확성), offline/online parity, freshness và tính năng (feature / 기능) deletion.
12. [16 — Privacy-preserving analytics](16_privacy_preserving_analytics/README.md): threat mô hình (model / 모델), differential privacy, composition và aggregate bản phát hành (release / 릴리스) chính sách (policy / 정책).
13. [17 — Contract testing](17_contract_testing_and_compatibility/README.md): machine-readable đặc tả hợp đồng (contract / 계약), tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), consumer-driven kiểm thử (test / 테스트) và thời gian chạy (runtime / 런타임) enforcement.
14. [90 — Case studies](90_case_studies/README.md): CDC duplicate, late sự kiện (event / 이벤트), backfill race, compaction race và ngữ nghĩa (semantic / 의미적) fan-out.

### Phụ thuộc (dependency / 의존성) map
Phần “Phụ thuộc (dependency / 의존성) map” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
01 foundations
  ├── 02 pipeline semantics ──┬── 07 streaming ────────┐
  ├── 03 storage/layout ──────┴── 09 warehouse/lakehouse ┤
  └── 04 reliability ───────────────┬── 08 orchestration ─┤
                                    ├── 11 governance ────┤
05 modeling/transformation ─────────┴── 10 serving ───────┤
06 distributed processing ───────────── 12 cost/capacity ─┤
13 approximate ── 14 multi-region ── 16 privacy ─────────┤
15 ML features ─── 17 contracts ─────────────────────────┤
                                                         90 case studies
```

### Công cụ (tool / 도구) ranh giới (boundary / 경계)

Kafka, Spark, Flink, Airflow, dbt, warehouse và cloud services chỉ nên xuất hiện như hiện thực (implementation / 구현) ánh xạ (mapping / 매핑) sau khi các chapter tương ứng đã giải thích mô hình tư duy (mental model / 사고 모델). Một công cụ (tool / 도구) mới phải trả lời được: nó duy trì bất biến (invariant / 불변식) nào, thất bại (failure / 실패) ranh giới (boundary / 경계) ở đâu, và bằng chứng (evidence / 증거) nào chứng minh guarantee đó trong môi trường vận hành (production / 운영 환경).


> **Chuyển mạch:** Từ **Lộ trình mở rộng theo conceptual ranh giới (boundary / 경계)**, ta sang **ranh giới (boundary / 경계) với SQL và cơ sở dữ liệu (database / 데이터베이스)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ranh giới (boundary / 경계) với SQL và cơ sở dữ liệu (database / 데이터베이스)

Repository hiện có `sql/` chứa tài liệu SQL và mô hình dữ liệu. Không di chuyển thư mục đó một cách cơ học. SQL sau này sẽ được consolidate vào kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) theo ranh giới (boundary / 경계) sau.

Kiến thức về relational mô hình (model / 모델), truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론), joins, aggregation, cửa sổ (window / 윈도우) functions, analytical SQL và cách SQL tham gia transformation thuộc lộ trình học (learning path / 학습 경로) kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링). Kiến thức về giao dịch (transaction / 트랜잭션) engine, MVCC, WAL, B-tree, buffer pool, optimizer internals và tính đồng thời (concurrency / 동시성) điều khiển (control / 제어) là nền tảng cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들); kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링) sẽ cross-link thay vì bản sao (copy / 복사) lại toàn bộ.

Trong giai đoạn di chuyển (migration / 마이그레이션), `sql/` vẫn là nguồn chuẩn gốc (canonical / 정본) cho nội dung SQL hiện có. Khi di chuyển (migration / 마이그레이션) diễn ra, link cũ phải được kiểm tra trước khi đổi đường dẫn (path / 경로) và raw/nguồn (source / 소스) material không được xóa chỉ vì chuẩn gốc (canonical / 정본) reading material đã chuyển nơi.


> **Chuyển mạch:** Từ **ranh giới (boundary / 경계) với SQL và cơ sở dữ liệu (database / 데이터베이스)**, ta sang **mô hình tư duy (mental model / 사고 모델) xuyên suốt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델) xuyên suốt

Một chuỗi xử lý (pipeline / 파이프라인) tốt không được định nghĩa bởi việc job "chạy xanh". Một job có thể thành công về mặt tiến trình (process / 프로세스) nhưng tạo dữ liệu sai. tính đúng đắn (correctness / 정확성) phải được nhìn ở nhiều lớp: bản ghi (record / 레코드) có bị mất hoặc duplicate không, lược đồ (schema / 스키마) có đúng không, nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) có còn đúng không, dữ liệu có đủ fresh không, và downstream bên tiêu thụ (consumer / 소비자) có đang đọc đúng phiên bản (version / 버전) hay không.

Vì vậy thư viện (library / 라이브러리) này ưu tiên lập luận (reasoning / 추론) về tính đúng đắn (correctness / 정확성), replayability, khả năng quan sát (observability / 관측 가능성) và quyền sở hữu (ownership / 소유권) trước cú pháp (syntax / 문법) của công cụ. Khi hiểu các bất biến (invariant / 불변식) đó, việc học Spark, Kafka, Airflow, dbt hoặc một cloud dữ liệu (data / 데이터) nền tảng (platform / 플랫폼) trở thành việc ánh xạ một công cụ vào mô hình tư duy (mental model / 사고 모델) đã có thay vì ghi nhớ hàng loạt API.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델) xuyên suốt**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 foundations](./01_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
