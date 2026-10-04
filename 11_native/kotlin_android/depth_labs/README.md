# Kotlin + Android độ sâu (depth / 깊이) Labs

> **Mạch đọc:** README này là owner của **Kotlin + Android độ sâu (depth / 깊이) Labs**. Giữ thứ tự **architecture invariants → offline sync → coroutine/Flow → Compose runtime → SDK boundary → build/release forensics → version migration**, rồi dùng production casebook để đối chiếu; mỗi lab mở một failure boundary cụ thể và quay lại README khi cần chọn owner.

`depth_labs/` là tầng đọc sâu nằm sau các tệp (file / 파일) chính, `deep_dive/` và môi trường vận hành (production / 운영 환경) Casebook. Mục tiêu của thư mục này không phải mở thêm lĩnh vực (domain / 도메인) Android mới, mà **đào sâu các chủ đề đã có tới mức có thể lập luận (reasoning / 추론) về tính đúng đắn (correctness / 정확성) khi môi trường vận hành (production / 운영 환경) không chạy theo happy đường dẫn (path / 경로)**.

Nếu môi trường vận hành (production / 운영 환경) Casebook trả lời “các subsystem ghép lại như thế nào?”, độ sâu (depth / 깊이) Labs trả lời “tại sao thiết kế đó vẫn đúng khi thứ tự thực thi (execution / 실행) thay đổi, có race, tiến trình (process / 프로세스) chết, yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) sau remote lần ghi nhận (commit / 커밋), trạng thái (state / 상태) bị stale, bản phát hành (release / 릴리스) bị quay lui (rollback / 롤백) hoặc SDK chạy trong app bên tiêu thụ (consumer / 소비자) khác?”.

## Thứ tự đọc

1. [`01_architecture_invariants_boundary_reasoning.md`](01_architecture_invariants_boundary_reasoning.md) — bắt đầu từ bất biến (invariant / 불변식), quyền sở hữu trạng thái (state ownership / 상태 소유권), nguồn chuẩn (source of truth / 정본), giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계), stale snapshot, ambiguous kết quả (outcome / 결과), điều hướng (navigation / 내비게이션) định danh (identity / 식별자) và kiến trúc (architecture / 아키텍처) timeline.
2. [`02_offline_sync_consistency_race_conditions.md`](02_offline_sync_consistency_race_conditions.md) — consistency mô hình (model / 모델), durable outbox, idempotency, thử lại (retry / 재시도)/jitter, thứ tự (ordering / 순서), hàng đợi (queue / 큐) compaction, phiên bản (version / 버전)/xung đột (conflict / 충돌), tombstone, sync cursor, account isolation và thất bại (failure / 실패) injection.
3. [`03_coroutine_flow_concurrency_failure_semantics.md`](03_coroutine_flow_concurrency_failure_semantics.md) — Job cây (tree / 트리), structured tính đồng thời (concurrency / 동시성), cancellation, dispatcher, Mutex/actor, cold/hot luồng (flow / 흐름), trạng thái (state / 상태)/sự kiện (event / 이벤트) distinction, backpressure, callbackFlow, stale-request race và deterministic coroutine kiểm thử (test / 테스트).
4. [`04_compose_runtime_state_performance_semantics.md`](04_compose_runtime_state_performance_semantics.md) — Snapshot trạng thái (state / 상태), định danh (identity / 식별자), tác động (effect / 효과) thời gian tồn tại (lifetime / 수명), composition/bố cục (layout / 레이아웃)/draw vô hiệu hóa (invalidation / 무효화), stability, modifier thứ tự (order / 순서), custom bố cục (layout / 레이아웃)/draw, ngữ nghĩa (semantics / 의미론)/khả năng tiếp cận (accessibility / 접근성) và evidence-based hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화).
5. [`05_testing_reliability_observability_failure_injection.md`](05_testing_reliability_observability_failure_injection.md) — invariant-based testing, fake/mock fidelity, di chuyển (migration / 마이그레이션)/quay lui (rollback / 롤백) kiểm thử (test / 테스트), race/thất bại (failure / 실패) injection, tiến trình (process / 프로세스) death, Macrobenchmark, SLI/SLO, telemetry, staged rollout và sự cố (incident / 인시던트) vòng phản hồi (feedback loop / 피드백 루프).
6. [`06_build_compatibility_startup_release_forensics.md`](06_build_compatibility_startup_release_forensics.md) — Gradle/variant/manifest/tài nguyên (resource / 자원) merge, generated mã (code / 코드), D8/R8, signing, API-level tính tương thích (compatibility / 호환성), SDK Extensions, OEM/WebView variation, cold-start đường găng (critical path / 임계 경로) và bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) forensics.
7. [`07_sdk_native_boundary_api_evolution_consumer_safety.md`](07_sdk_native_boundary_api_evolution_consumer_safety.md) — API công khai (public API / 공개 API)/ABI, phụ thuộc (dependency / 의존성) leakage, Java/Kotlin interop, SDK initialization/luồng thực thi (thread / 스레드)/lỗi (error / 오류) đặc tả hợp đồng (contract / 계약), bên tiêu thụ (consumer / 소비자) R8, JNI quyền sở hữu (ownership / 소유권), ABI/bản địa (native / 네이티브) crash, deprecation, SemVer và bên tiêu thụ (consumer / 소비자) tính tương thích (compatibility / 호환성) testing.
8. [`08_version_compatibility_migration_forensics.md`](08_version_compatibility_migration_forensics.md) — Kotlin siêu dữ liệu (metadata / 메타데이터), pre-release nhị phân (binary / 이진), ngôn ngữ (language / 언어)/API/JVM mục tiêu (target / 대상) đặc tả hợp đồng (contract / 계약), compiler-plugin lockstep, Compose trình biên dịch (compiler / 컴파일러) di chuyển (migration / 마이그레이션), KSP/kapt, công khai (public / 공개) inline/default-arg/const/value-class ABI, Android mục tiêu (target / 대상) di chuyển (migration / 마이그레이션), transitive phụ thuộc (dependency / 의존성) floor và version-upgrade forensic playbook.

> **Nối mạch:** Trong **Kotlin + Android độ sâu (depth / 깊이) Labs**, **Thứ tự đọc** nêu quy tắc; **Cách dùng cùng môi trường vận hành (production / 운영 환경) Casebook** thử quy tắc trong tình huống, rồi **Quy tắc học** mở rộng hệ quả.

## Cách dùng cùng môi trường vận hành (production / 운영 환경) Casebook

Độ sâu (depth / 깊이) Labs không thay Casebook. Nên đọc chúng theo cặp:

```text
Case 01 Architecture
→ Depth Lab 01 Architecture invariants

Case 03 Offline-first
→ Depth Lab 02 Sync correctness

Case 02/08/09 Coroutine + runtime
→ Depth Lab 03 Concurrency semantics

Case 11 Compose UI system
→ Depth Lab 04 Compose runtime reasoning

Case 05/13 Reliability/release
→ Depth Lab 05 Testing + observability

Case 15/18/19 Build/compat/startup
→ Depth Lab 06 Build + release forensics

Case 17/20 NDK + SDK authoring
→ Depth Lab 07 Consumer/native safety

05 Version Evolution + Case 08/15/18/20
→ Depth Lab 08 Version compatibility + migration forensics
```

> **Nối mạch:** Ở chặng này của **Kotlin + Android độ sâu (depth / 깊이) Labs**, **Cách dùng cùng môi trường vận hành (production / 운영 환경) Casebook** nêu quy tắc; **Quy tắc học** thử quy tắc trong tình huống, rồi **Mental model chung** mở rộng hệ quả.

## Quy tắc học

Không đọc độ sâu (depth / 깊이) Lab như danh sách best practice để học thuộc. Với mỗi section, hãy tự tạo một timeline hoặc thất bại (failure / 실패) scenario rồi trả lời:

```text
invariant nào phải giữ?
owner là ai?
state nào authoritative?
operation có thể bị replay không?
outcome có thể ambiguous không?
process death xảy ra ở đây thì sao?
request/result cũ có thể overwrite state mới không?
release cũ có đọc data/artifact mới không?
metric/log nào chứng minh behavior production?
version change nào làm producer/consumer contract thay đổi?
artifact hoặc metadata nào thật sự khác trước?
```

Nếu chỉ biết tên API nhưng không trả lời được các câu trên, kiến thức vẫn đang ở mức hiện thực (implementation / 구현) chứ chưa tới mức kỹ thuật (engineering / 엔지니어링) lập luận (reasoning / 추론).

> **Nối mạch:** Quy tắc học đặt mục tiêu của lab; mental model chung tiếp theo dùng invariant, race, failure và evidence để kiểm tra production reasoning.

## Mental model chung
Phần này nối mạch Android vừa học với “Mental model chung”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

```text
Requirement
-> Invariant
-> Ownership
-> State / Source of Truth
-> Execution Context
-> Concurrency / Ordering
-> Failure / Cancellation / Retry
-> Persistence / Reconstruction
-> Compatibility
-> Version / Artifact Contract
-> Observability
-> Release / Recovery
```

Đây là lớp kiến thức cuối cùng trước khi chuyển từ “biết Android” sang “có thể giải thích và vận hành một hệ thống Android production”.

> **Bàn giao:** Sau **Mental model chung**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
