# 17 — Machine-readable dữ liệu (data / 데이터) contracts và tính tương thích (compatibility / 호환성) testing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **17 — Machine-readable dữ liệu (data / 데이터) contracts và tính tương thích (compatibility / 호환성) testing**. Route đi từ contract layers → compatibility matrix → schema, grain, identity, freshness và quality → CI/CD/runtime checks → producer/consumer ownership, để contract trở thành hàng rào vận hành có thể kiểm thử.

Dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약) biến expectation về lược đồ (schema / 스키마) và ngữ nghĩa (semantics / 의미론) thành sản phẩm tạo ra (artifact / 산출물) có thể kiểm tra trong CI/CD và thời gian chạy (runtime / 런타임). Nó không chỉ là một JSON lược đồ (schema / 스키마); grain, định danh (identity / 식별자), freshness, chất lượng (quality / 품질) và quyền sở hữu (ownership / 소유권) cũng là đặc tả hợp đồng (contract / 계약).

## 1. đặc tả hợp đồng (contract / 계약) layers

```text
syntax → schema/type/nullability/enum
semantics → grain, units, timezone, event/state meaning
behavior → ordering, delivery, retry, delete, late correction
service → freshness, completeness, availability, owner
```

Lược đồ (schema / 스키마) pass mà ngữ nghĩa (semantics / 의미론) thất bại (fail / 실패) vẫn là breaking thay đổi (change / 변경).

> **Chuyển mạch:** **Contract layers** xác định interface và owner; **Compatibility matrix** đối chiếu producer/consumer versions trước khi mở **consumer-driven contract**.

## 2. tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬)

Kiểm tra producer mới với bên tiêu thụ (consumer / 소비자) cũ, producer cũ với bên tiêu thụ (consumer / 소비자) mới, tệp (file / 파일)/snapshot cũ với reader mới và replay mã (code / 코드) cũ với lược đồ (schema / 스키마) mới. Add optional trường dữ liệu (field / 필드) có thể backward compatible; rename, enum narrowing và kiểu (type / 타입) reinterpretation thường không.

Tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트) cần fixture thật có duplicate, null, delete, late sự kiện (event / 이벤트), timezone và large giá trị (value / 값)—không chỉ một bản ghi (record / 레코드) tối giản.

> **Chuyển mạch:** **Consumer-driven contract** đưa nhu cầu thật của bên dùng vào test; **Semantic versioning và deprecation** biến kết quả test thành policy phát hành.

## 3. Consumer-driven đặc tả hợp đồng (contract / 계약)

Bên tiêu thụ (consumer / 소비자) khai báo trường dữ liệu (field / 필드)/chỉ số (metric / 지표)/độ trễ (latency / 지연 시간) mà mình phụ thuộc. Producer chạy kiểm thử (test / 테스트) trước deploy và biết blast radius. Cần tránh bên tiêu thụ (consumer / 소비자) khai báo mọi hiện thực (implementation / 구현) detail, nếu không đặc tả hợp đồng (contract / 계약) trở nên cứng và cản evolution.

> **Chuyển mạch:** **Semantic versioning và deprecation** ghi rõ compatibility promise; **Runtime enforcement** bảo vệ promise đó khi dữ liệu đi qua pipeline thật.

## 4. ngữ nghĩa (semantic / 의미적) versioning và deprecation

Breaking ngữ nghĩa (semantic / 의미적) thay đổi (change / 변경) phải tạo phiên bản (version / 버전)/effective date, dual-run hoặc di chuyển (migration / 마이그레이션). Telemetry bên tiêu thụ (consumer / 소비자) dùng để quyết định khi nào xóa v1; không xóa vì danh mục (catalog / 카탈로그) không thấy bên tiêu thụ (consumer / 소비자).

> **Chuyển mạch:** **Runtime enforcement** bắt lỗi drift tại boundary; **Evidence** ghi lại contract version, failure và quyết định xử lý.

## 5. thời gian chạy (runtime / 런타임) enforcement

CI không đủ vì nguồn (source / 소스) có thể drift sau deploy. thời gian chạy (runtime / 런타임) cần lược đồ (schema / 스키마)/đặc tả hợp đồng (contract / 계약) check, quarantine hoặc stop-the-line cho breaking thay đổi (change / 변경), cùng chỉ số (metric / 지표) đặc tả hợp đồng (contract / 계약) violation và đơn vị sở hữu (owner / 오너) routing. Enforcement nên phân biệt hard thất bại (failure / 실패) với warning có expiry.

> **Chuyển mạch:** **Evidence** khép contract route bằng compatibility matrix, runtime result và owner; chi tiết schema quay về canonical data chapter.

## 6. bằng chứng (evidence / 증거)

Lưu đặc tả hợp đồng (contract / 계약) phiên bản (version / 버전), kiểm thử (test / 테스트) kết quả (result / 결과), producer lần ghi nhận (commit / 커밋), bên tiêu thụ (consumer / 소비자) danh sách (list / 목록), tính tương thích (compatibility / 호환성) quyết định (decision / 결정), exception expiry và observed lược đồ (schema / 스키마). Đây là đầu vào (input / 입력) cho lineage, sự cố (incident / 인시던트) triage và thay đổi (change / 변경) approval.

Đọc tiếp: [02 — Pipeline](../02_pipeline_architecture.md), [08 — Orchestration](../08_orchestration_and_backfill/README.md), [11 — Governance](../11_governance_lineage_security/README.md).

> **Bàn giao:** Sau **6. bằng chứng (evidence / 증거)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
