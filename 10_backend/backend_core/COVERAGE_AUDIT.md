# Backend cốt lõi (core / 핵심) — coverage kiểm tra (audit / 감사)

> **Mạch đọc:** Đặt **Backend cốt lõi (core / 핵심) — coverage kiểm tra (audit / 감사)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Coverage ma trận (matrix / 행렬)** sang **ranh giới (boundary / 경계) cố ý không duplicate**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Ngày kiểm tra (audit / 감사): 2026-09-23. kiểm tra (audit / 감사) này kiểm tra **coverage của lập luận (reasoning / 추론)**, không đếm
số từ khóa (keyword / 키워드) hay số dòng. Một chủ đề được coi là covered khi có đặc tả hợp đồng (contract / 계약), bất biến (invariant / 불변식),
dạng thất bại (failure mode / 실패 모드) và cách thu bằng chứng (evidence / 증거); API/công cụ (tool / 도구) cụ thể có thể nằm ở hiện thực (implementation / 구현)
nhánh học (track / 트랙).

## Coverage ma trận (matrix / 행렬)

| Năng lực | đơn vị sở hữu (owner / 오너) | Trạng thái | bằng chứng (evidence / 증거) trong thư viện (library / 라이브러리) |
|---|---|---|---|
| yêu cầu (request / 요청) admission và vòng đời (lifecycle / 생명주기) | `00` | covered | máy trạng thái (state machine / 상태 머신), hết thời gian chờ (timeout / 타임아웃)/cancellation, admission điều khiển (control / 제어) |
| HTTP đặc tả hợp đồng (contract / 계약) và tính tương thích (compatibility / 호환성) | `01` | covered | status/lỗi (error / 오류), idempotency, ETag, phiên bản (version / 버전) ma trận (matrix / 행렬) |
| định danh (identity / 식별자)/session/authorization | `02` | covered | subject/tenant, rotation, revocation, async chính sách (policy / 정책) |
| persistence/giao dịch (transaction / 트랜잭션)/ORM | `03` | covered | giao dịch (transaction / 트랜잭션) ma trận (matrix / 행렬), lost cập nhật (update / 업데이트), di chuyển (migration / 마이그레이션) |
| bộ nhớ đệm (cache / 캐시)/vô hiệu hóa (invalidation / 무효화) | `04` | covered | staleness ngân sách (budget / 예산), key lược đồ (schema / 스키마), stampede |
| jobs/messaging | `05` | covered | delivery, outbox, thứ tự (ordering / 순서), replay, lease |
| hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도)/idempotency | `06` | covered | thử lại (retry / 재시도) topology, unknown kết quả (result / 결과), deadline |
| testing/contracts | `07` | covered | bất biến (invariant / 불변식) tests, fault injection, kiểm thử (test / 테스트) ma trận (matrix / 행렬) |
| khả năng quan sát (observability / 관측 가능성)/debugging | `08` | covered | nhân quả (causal / 인과적) đồ thị (graph / 그래프), sampling, cardinality, mitigation |
| kiến trúc (architecture / 아키텍처) boundaries | `09` | covered | mô-đun (module / 모듈) quyền sở hữu (ownership / 소유권), extraction fitness, read mô hình (model / 모델) |
| môi trường vận hành (production / 운영 환경) lập luận (reasoning / 추론) | `10` | covered | 8 cases + capstone |
| cấu hình (configuration / 구성)/secrets vòng đời (lifecycle / 생명주기) | `00`/`02` | covered at cốt lõi (core / 핵심) mức (level / 수준) | nguồn (source / 소스), precedence, kiểm tra hợp lệ (validation / 검증), rotation, truy cập (access / 접근) và drift |
| tải (load / 로드)/hiệu năng (performance / 성능)/sức chứa (capacity / 용량) testing | `06`/`07`/`08` | covered | pool/backpressure, tải công việc (workload / 워크로드) mô hình (model / 모델), SLO và saturation |
| API bảo mật (security / 보안) headers/CORS/tỷ lệ (rate / 비율) chính sách (policy / 정책) | `01`/`02` | covered | limiter đặc tả hợp đồng (contract / 계약), CORS ranh giới (boundary / 경계), kiểm tra hợp lệ (validation / 검증), auth |
| privacy/dữ liệu (data / 데이터) retention/erasure | `02`/`03`/`08` | covered at cốt lõi (core / 핵심) mức (level / 수준) | vòng đời (lifecycle / 생명주기), deletion phạm vi (scope / 범위), redaction và telemetry classification |


> **Chuyển mạch:** Từ **Coverage ma trận (matrix / 행렬)**, ta sang **ranh giới (boundary / 경계) cố ý không duplicate** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ranh giới (boundary / 경계) cố ý không duplicate

- cơ sở dữ liệu (database / 데이터베이스) internals (MVCC, WAL, indexes, query optimizer) thuộc
  [`computer_science/05_data_databases/`](../../computer_science/05_data_databases/).
- TCP/TLS/DNS, hàng đợi (queue / 큐) internals, thứ tự (ordering / 순서) và phân tán (distributed / 분산) consensus thuộc
  [`computer_science/06_networks_distributed_systems/`](../../computer_science/06_networks_distributed_systems/).
- tiến trình (process / 프로세스), bộ nhớ (memory / 메모리), filesystem và tài nguyên (resource / 자원) isolation thuộc các chapter các hệ thống (systems / 시스템들)
  trong [`computer_science/`](../../computer_science/README.md).
- Threat mô hình (model / 모델), cryptography và secure software vòng đời (lifecycle / 생명주기) thuộc
  [`computer_science/07_security_reliability/`](../../computer_science/07_security_reliability/).
- Java/Python ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) và Spring API thuộc các nhánh học (track / 트랙) hiện thực (implementation / 구현)
  bên cạnh, không trở thành prerequisite ngầm của Backend cốt lõi (core / 핵심).


> **Chuyển mạch:** Từ **ranh giới (boundary / 경계) cố ý không duplicate**, ta sang **Backlog có thứ tự** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Backlog có thứ tự

1. Bổ sung một thiết kế (design / 설계) worksheet cho cấu hình (configuration / 구성)/secrets vòng đời (lifecycle / 생명주기) nếu các
   hiện thực (implementation / 구현) nhánh học (track / 트랙) bắt đầu dùng chung một chính sách (policy / 정책).
2. Tạo thêm trường hợp (case / 사례) về multi-region/dữ liệu (data / 데이터) residency chỉ khi repository có đơn vị sở hữu (owner / 오너) rõ
   cho triển khai (deployment / 배포) và legal ranh giới (boundary / 경계); không kéo topic này vào cốt lõi (core / 핵심) quá sớm.
3. Chỉ tạo chapter riêng khi các phần trên đủ lớn và có bất biến (invariant / 불변식) khác biệt;
   không tách tệp (file / 파일) chỉ để tăng số lượng.


> **Chuyển mạch:** Từ **Backlog có thứ tự**, ta sang **Tiêu chí hoàn tất một cập nhật (update / 업데이트)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tiêu chí hoàn tất một cập nhật (update / 업데이트)

Mỗi cập nhật (update / 업데이트) mới cần:

1. chỉ rõ đơn vị sở hữu chuẩn gốc (canonical owner / 정본 소유자) và ranh giới (boundary / 경계);
2. thêm ít nhất một dạng thất bại (failure mode / 실패 모드) hoặc sự đánh đổi (trade-off / 트레이드오프), không chỉ thêm định nghĩa;
3. nối thiết kế (design / 설계) với kiểm thử (test / 테스트) và telemetry;
4. có trường hợp (case / 사례) hoặc bài tập để kiểm tra lập luận nhân quả (causal reasoning / 인과적 추론);
5. chạy link/whitespace check trước khi merge.

> **Bàn giao:** Sau **Tiêu chí hoàn tất một cập nhật (update / 업데이트)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 backend request lifecycle](./00_backend_request_lifecycle.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
