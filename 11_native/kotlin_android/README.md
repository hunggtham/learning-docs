# Kotlin + Android Master Notes

> **Mạch đọc:** README này là owner của **Kotlin + Android Master Notes**. Route đi từ canonical learning spine và anti-duplicate rules → Kotlin/Android foundations → intermediate architecture/coroutines → advanced runtime/security/performance → version evolution và migration, để mỗi chapter có owner và prerequisite rõ.

Bộ tài liệu học Kotlin cho Android có **trục học (learning spine / 학습 축) chuẩn gốc (canonical / 정본) duy nhất** theo thứ tự:

1. `01_kotlin_beginner.md` — nền tảng Kotlin, Android Studio, Gradle, Android components, Compose và XML/View.
2. `02_kotlin_intermediate.md` — idioms, generics, coroutine/luồng (flow / 흐름), ViewModel, kiến trúc (architecture / 아키텍처), Room, mạng (network / 네트워크), DI, WorkManager, DataStore và testing.
3. `03_kotlin_advanced_senior.md` — coroutine/luồng (flow / 흐름) internals, Compose thời gian chạy (runtime / 런타임), modularization, offline-first, hiệu năng (performance / 성능), bảo mật (security / 보안), Java interop và môi trường vận hành (production / 운영 환경) thiết kế (design / 설계).
4. `04_kotlin_master.md` — Kotlin 1.x→2.x, K2, bytecode awareness, large-scale kiến trúc (architecture / 아키텍처)/bản dựng (build / 빌드)/bản phát hành (release / 릴리스), KMP awareness, khả năng quan sát (observability / 관측 가능성) và master heuristics.

**mạch học (learning flow / 학습 흐름) luôn là Beginner → Intermediate → Advanced/cấp cao (senior / 시니어) → Master.** Không có “mức (level / 수준) 5”. [`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md) là **cross-cutting tham chiếu (reference / 참조) về phiên bản (version / 버전)/evolution**, dùng song song khi gặp dự án (project / 프로젝트) cũ, di chuyển (migration / 마이그레이션)/toolchain tính tương thích (compatibility / 호환성) hoặc muốn hiểu vì sao API/bản dựng (build / 빌드) setup thay đổi theo thời gian.

Các thư mục bổ sung không thay thế chuẩn gốc (canonical / 정본) spine:

```text
01–04 canonical
= nơi concept bắt buộc phải đủ rõ để học theo level

deep_dive/
= completion layer cùng level; đào thêm chi tiết nhưng không tạo learning path cạnh tranh

production_casebook/
= nối nhiều concept thành system/scenario production end-to-end

depth_labs/
= reasoning lab về invariant, race, failure, compatibility và forensic

05_kotlin_android_version_evolution.md
= reference xuyên level cho timeline/version/migration
```

## Quy tắc chống duplicate ghi chú (note / 노트)

Khi cập nhật (update / 업데이트) thư viện (library / 라이브러리), **ưu tiên sửa tệp chuẩn gốc (canonical file / 정본 파일) đang sở hữu concept**. Không tạo ghi chú (note / 노트) mới chỉ vì phần hiện tại còn mỏng.

Một tệp (file / 파일) bổ sung chỉ hợp lý nếu nó có vai trò khác hẳn chuẩn gốc (canonical / 정본), ví dụ casebook mô phỏng một hệ thống end-to-end hoặc độ sâu (depth / 깊이) lab đào thất bại (failure / 실패) thứ tự (ordering / 순서). Nếu cùng câu hỏi học tập, cùng mức (level / 수준) và cùng mục tiêu giải thích đã tồn tại trong `01–04`, hãy cập nhật tệp (file / 파일) đó thay vì tạo `*_v2`, `*_complete`, `*_extra` hoặc một Master ghi chú (note / 노트) song song.

Khi nội dung quan trọng chỉ tồn tại ở supplement nhưng cần thiết để đi từ Beginner → Master, hãy kéo **mô hình tư duy (mental model / 사고 모델) tối thiểu bắt buộc** trở lại chuẩn gốc (canonical / 정본) rồi giữ supplement cho phần forensic/trường hợp biên (edge case / 경계 사례). Đây là nguyên tắc được áp dụng cho phiên bản (version / 버전) evolution, modern-vs-legacy API, vòng đời (lifecycle / 생명주기)/tính đồng thời (concurrency / 동시성), coroutine/luồng (flow / 흐름) và Compose trong các vòng kiểm tra (audit / 감사) gần đây.

Không xóa tệp (file / 파일) chỉ vì có overlap từ khóa. Overlap có chủ đích giữa chuẩn gốc (canonical / 정본) → deep dive → casebook → độ sâu (depth / 깊이) lab được giữ khi mỗi tầng trả lời câu hỏi khác nhau. Chỉ xóa/merge khi hai tệp (file / 파일) cùng đơn vị sở hữu (owner / 오너), cùng học tập (learning / 학습) mục tiêu (objective / 목표) và một tệp (file / 파일) không còn giá trị riêng.

> **Nối mạch:** **Quy tắc chống duplicate** giữ nội dung ở đúng owner; **Version evolution** dùng boundary đó để đọc project cũ và toolchain hiện đại, rồi mở **Deep dives theo level**.

## Phiên bản (version / 버전) evolution — đọc dự án (project / 프로젝트) cũ và hiểu toolchain hiện đại

[`05_kotlin_android_version_evolution.md`](05_kotlin_android_version_evolution.md) nên được mở như tham chiếu (reference / 참조) khi cần trả lời:

- dự án (project / 프로젝트) Kotlin 1.3/1.5/1.9 khác dự án (project / 프로젝트) Kotlin 2.x ở đâu;
- K1 và K2 trình biên dịch (compiler / 컴파일러) khác nhau về thế hệ như thế nào;
- khi nào JVM IR trở thành mặc định;
- `sealed interface`, giá trị (value / 값) lớp (class / 클래스), `data object`, enum `entries`, ngữ cảnh (context / 맥락) parameters và tường minh (explicit / 명시적) backing fields xuất hiện/stable ở phiên bản (version / 버전) nào;
- vì sao Compose trình biên dịch (compiler / 컴파일러) trước Kotlin 2.0 cần tính tương thích (compatibility / 호환성) ánh xạ (mapping / 매핑) nhưng Kotlin 2.0+ dùng plugin cùng Kotlin phiên bản (version / 버전);
- khác biệt giữa Kotlin phiên bản (version / 버전), `languageVersion`, `apiVersion`, `jvmTarget`, JDK toolchain, KGP/AGP và Gradle;
- khác biệt giữa `minSdk`, `compileSdk`, `targetSdk` và Android OS thực tế;
- cách nhận diện synthetic view, `AsyncTask`, LiveData/Rx-heavy, `kotlinOptions {}`, kapt-heavy và map sang hiện đại (modern / 현대적) ngăn xếp (stack / 스택) mà không rewrite máy móc;
- cách upgrade toolchain bằng tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬), full-variant bản dựng (build / 빌드), generated-code kiểm thử (test / 테스트) và bản phát hành (release / 릴리스) kiểm tra hợp lệ (validation / 검증).

Khi học chuẩn gốc (canonical / 정본), có thể mở tệp (file / 파일) này theo nhu cầu; khi làm di chuyển (migration / 마이그레이션) thực tế, đọc thêm `production_casebook/18_android_compatibility_api_levels_sdk_extensions.md` và `depth_labs/08_version_compatibility_migration_forensics.md`.

> **Nối mạch:** **Version evolution** xác định compiler, runtime và API boundary; **Deep dives theo level** lần lượt mở cơ chế theo độ sâu thay vì lặp lại lịch sử version.

## Deep dives theo từng level
Phần này nối mạch Android vừa học với “Deep dives theo từng level”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

> **Nối mạch:** Hai mức deep dive tách overview khỏi implementation detail; **Depth Labs** dùng cùng mental model để kiểm tra reasoning và runtime evidence.

## Deep dives theo từng mức (level / 수준)

- [`deep_dive/01_beginner_completion.md`](deep_dive/01_beginner_completion.md) — gói (package / 패키지)/import, equality, phạm vi (range / 범위)/array, collection transformation, nested/inner lớp (class / 클래스), precondition, data-class định danh (identity / 식별자), ngữ cảnh (context / 맥락)/Intent/Uri, Compose bố cục (layout / 레이아웃) và testing căn bản.
- [`deep_dive/02_intermediate_completion.md`](deep_dive/02_intermediate_completion.md) — CoroutineContext/Job hierarchy, supervision, luồng (flow / 흐름) cold/hot/ngữ cảnh (context / 맥락), `stateIn`/`shareIn`, `callbackFlow`, tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명), mạng (network / 네트워크) lỗi (error / 오류) mô hình (model / 모델), Room source-of-truth, Compose tác động (effect / 효과)/trạng thái (state / 상태), coroutine testing, DI phạm vi (scope / 범위) và điều hướng (navigation / 내비게이션) đặc tả hợp đồng (contract / 계약).
- [`deep_dive/03_advanced_senior_completion.md`](deep_dive/03_advanced_senior_completion.md) — generic/type-erasure, cancellation an toàn (safety / 안전), luồng (flow / 흐름) backpressure, Compose Snapshot/CompositionLocal/định danh (identity / 식별자), background thực thi (execution / 실행), thử lại (retry / 재시도)/idempotency/TLS, lưu trữ (storage / 저장소)/backup, kiểm thử (test / 테스트) layers, benchmark và static phân tích (analysis / 분석).
- [`deep_dive/04_master_completion.md`](deep_dive/04_master_completion.md) — Gradle/bản dựng (build / 빌드) quản trị (governance / 거버넌스), phụ thuộc (dependency / 의존성) locking/SBOM, ABI/mô-đun (module / 모듈) đặc tả hợp đồng (contract / 계약), target-SDK di chuyển (migration / 마이그레이션), khả năng quan sát (observability / 관측 가능성), hiệu năng (performance / 성능) ngân sách (budget / 예산), bảo mật (security / 보안)/integrity, privacy, khả năng tiếp cận (accessibility / 접근성)/adaptive UI, ADR/quyền sở hữu (ownership / 소유권), bản phát hành (release / 릴리스)/quay lui (rollback / 롤백), KMP và operating mô hình (model / 모델).

[`coverage_audit.md`](coverage_audit.md) là ma trận coverage và checklist dùng để chọn **chuẩn gốc (canonical / 정본) gap yếu nhất** cho vòng cập nhật (update / 업데이트) tiếp theo.

> **Nối mạch:** Trong **Kotlin + Android Master Notes**, **Deep dives theo từng mức (level / 수준)** nêu quy tắc; **Độ sâu (depth / 깊이) Labs — tăng độ sâu lập luận (reasoning / 추론)** thử quy tắc trong tình huống, rồi **Môi trường vận hành (production / 운영 환경) Casebook — nối kiến thức thành hệ thống thực tế** mở rộng hệ quả.

## Độ sâu (depth / 깊이) Labs — tăng độ sâu lập luận (reasoning / 추론)

Sau khi chuẩn gốc (canonical / 정본) concept đã rõ, dùng [`depth_labs/README.md`](depth_labs/README.md) để đào tính đúng đắn (correctness / 정확성) ở ranh giới (boundary / 경계) khó. độ sâu (depth / 깊이) Labs không mở học tập (learning / 학습) mức (level / 수준) mới; chúng đi sâu bất biến (invariant / 불변식), race điều kiện (condition / 조건), giao dịch (transaction / 트랜잭션) ngữ nghĩa (semantics / 의미론), cancellation, stale trạng thái (state / 상태), consistency, tác động (effect / 효과) thời gian tồn tại (lifetime / 수명), bằng chứng hiệu năng (performance evidence / 성능 증거), thất bại (failure / 실패) injection, tính tương thích (compatibility / 호환성), sản phẩm tạo ra (artifact / 산출물) forensics và API/ABI evolution.

Các lab hiện có:

1. [`depth_labs/01_architecture_invariants_boundary_reasoning.md`](depth_labs/01_architecture_invariants_boundary_reasoning.md) — kiến trúc (architecture / 아키텍처) bất biến (invariant / 불변식), quyền sở hữu trạng thái (state ownership / 상태 소유권), stale snapshot, giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và ambiguous kết quả (outcome / 결과).
2. [`depth_labs/02_offline_sync_consistency_race_conditions.md`](depth_labs/02_offline_sync_consistency_race_conditions.md) — sync tính đúng đắn (correctness / 정확성), outbox, idempotency, thứ tự (ordering / 순서), xung đột (conflict / 충돌), cursor, account isolation và thất bại (failure / 실패) injection.
3. [`depth_labs/03_coroutine_flow_concurrency_failure_semantics.md`](depth_labs/03_coroutine_flow_concurrency_failure_semantics.md) — Job cây (tree / 트리), cancellation, supervision, backpressure, stream thời gian tồn tại (lifetime / 수명) và tính đồng thời (concurrency / 동시성) race.
4. [`depth_labs/04_compose_runtime_state_performance_semantics.md`](depth_labs/04_compose_runtime_state_performance_semantics.md) — Snapshot trạng thái (state / 상태), định danh (identity / 식별자), tác động (effect / 효과) thời gian tồn tại (lifetime / 수명), phase vô hiệu hóa (invalidation / 무효화), ngữ nghĩa (semantics / 의미론) và hiệu năng (performance / 성능) lập luận (reasoning / 추론).
5. [`depth_labs/05_testing_reliability_observability_failure_injection.md`](depth_labs/05_testing_reliability_observability_failure_injection.md) — invariant-based testing, di chuyển (migration / 마이그레이션)/quay lui (rollback / 롤백), race kiểm thử (test / 테스트), Macrobenchmark, telemetry, SLI/SLO và rollout guardrail.
6. [`depth_labs/06_build_compatibility_startup_release_forensics.md`](depth_labs/06_build_compatibility_startup_release_forensics.md) — Gradle/variant/R8, API tính tương thích (compatibility / 호환성), startup đường găng (critical path / 임계 경로) và bản phát hành (release / 릴리스) sản phẩm tạo ra (artifact / 산출물) forensics.
7. [`depth_labs/07_sdk_native_boundary_api_evolution_consumer_safety.md`](depth_labs/07_sdk_native_boundary_api_evolution_consumer_safety.md) — API công khai (public API / 공개 API)/ABI, SDK bên tiêu thụ (consumer / 소비자) an toàn (safety / 안전), JNI/bản địa (native / 네이티브) quyền sở hữu (ownership / 소유권), tính tương thích (compatibility / 호환성) và publishing evolution.
8. [`depth_labs/08_version_compatibility_migration_forensics.md`](depth_labs/08_version_compatibility_migration_forensics.md) — Kotlin siêu dữ liệu (metadata / 메타데이터), producer/bên tiêu thụ (consumer / 소비자) trình biên dịch (compiler / 컴파일러) ranh giới (boundary / 경계), JVM mục tiêu (target / 대상) mismatch, compiler-plugin lockstep, di chuyển (migration / 마이그레이션) forensics, CI tính tương thích (compatibility / 호환성) gates và sản phẩm tạo ra (artifact / 산출물) traceability.

> **Nối mạch:** Ở chặng này của **Kotlin + Android Master Notes**, **Độ sâu (depth / 깊이) Labs — tăng độ sâu lập luận (reasoning / 추론)** nêu quy tắc; **Môi trường vận hành (production / 운영 환경) Casebook — nối kiến thức thành hệ thống thực tế** thử quy tắc trong tình huống, rồi **Baseline version** mở rộng hệ quả.

## Môi trường vận hành (production / 운영 환경) Casebook — nối kiến thức thành hệ thống thực tế

> **Nối mạch:** Đặt trong câu hỏi lớn của **Kotlin + Android Master Notes**, **Môi trường vận hành (production / 운영 환경) Casebook — nối kiến thức thành hệ thống thực tế** nêu quy tắc; **Baseline version** thử quy tắc trong tình huống, rồi **Cách học** mở rộng hệ quả.

## Baseline version
Phần này nối mạch Android vừa học với “Baseline version”, giải thích mục đích, vòng đời hoặc ràng buộc để người mới hiểu vì sao ví dụ tiếp theo hoạt động.

- Kotlin: **2.4.20** stable (2026-09-07).
- Android Studio: **Quail 4 / 2026.1.4 Patch 1** stable.
- Android Gradle Plugin baseline: **9.4.1** với Quail 4 Patch 1.
- Compose stable BOM snapshot: **2026.09.00**.
- Android nền tảng (platform / 플랫폼) tham chiếu (reference / 참조): **Android 17 = API 37**.
- Google Play mục tiêu (target / 대상) yêu cầu (requirement / 요구사항) từ 2026-08-31: app/cập nhật (update / 업데이트) Android thông thường phải mục tiêu (target / 대상) **Android 16 / API 36+**, với ngoại lệ riêng cho một số form factor.
- UI direction: Jetpack Compose cho mã (code / 코드) hiện đại; XML/View hệ thống (system / 시스템) và API legacy quan trọng vẫn được cover để đọc, maintain và migrate dự án (project / 프로젝트) cũ.

Phiên bản (version / 버전) ở đây là snapshot để đọc dự án (project / 프로젝트) tại thời điểm biên soạn, không phải con số phải bản sao (copy / 복사) cứng mãi mãi. Khi upgrade cần đọc tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬) và bản phát hành (release / 릴리스) notes của Kotlin, Android Studio/AGP, Android nền tảng (platform / 플랫폼), Google Play chính sách (policy / 정책) và từng Jetpack/thư viện (library / 라이브러리) phụ thuộc (dependency / 의존성).

> **Nối mạch:** **Baseline version** khóa toolchain và API assumptions; **Cách học** biến chúng thành route, rồi **Phạm vi đã cover** ghi rõ phần nào đã có evidence.

## Cách học

Đường học chính không đổi:

```text
01 Beginner
→ 02 Intermediate
→ 03 Advanced/Senior
→ 04 Master
```

Ở mỗi mức (level / 수준), sau khi hiểu tệp chuẩn gốc (canonical file / 정본 파일) có thể đọc `deep_dive/0N` để mở rộng. `05_kotlin_android_version_evolution.md` là tham chiếu (reference / 참조) ngang: mở khi gặp phiên bản (version / 버전)/API generation/toolchain question, không phải một mức (level / 수준) bắt buộc sau Master.

Sau Master, Casebook và độ sâu (depth / 깊이) Labs chuyển trọng tâm từ “học concept” sang “ghép hệ thống (system / 시스템) và chứng minh tính đúng đắn (correctness / 정확성)”:

```text
Canonical Beginner → Master
→ Production Casebook: system integration
→ Depth Labs: invariant/race/failure/forensics
→ tự thiết kế, build, release và giải thích trade-off production
```

Khi học Casebook và độ sâu (depth / 깊이) Labs, không chỉ bản sao (copy / 복사) mã (code / 코드). Với mỗi trường hợp (case / 사례) hãy tự trả lời: trạng thái (state / 상태) đơn vị sở hữu (owner / 오너) là ai; nguồn chuẩn (source of truth / 정본) ở đâu; tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드)/vòng đời (lifecycle / 생명주기) nào đang chạy; bất biến (invariant / 불변식) nào bắt buộc luôn đúng; thất bại (failure / 실패) nào thử lại (retry / 재시도) được; kết quả (result / 결과) nào có thể stale; thao tác (operation / 연산) nào có ambiguous kết quả (outcome / 결과); permission/năng lực (capability / 역량) nào có thể biến mất; sản phẩm tạo ra (artifact / 산출물) nào thật sự tới thiết bị (device / 장치); bản địa (native / 네이티브)/tài nguyên (resource / 자원)/bản dựng (build / 빌드) ranh giới (boundary / 경계) nào có thể leak; dữ liệu nào nhạy cảm; thao tác (operation / 연산) nào cần idempotency; kiểm thử (test / 테스트) nào chứng minh bất biến (invariant / 불변식); bản phát hành (release / 릴리스) gặp lỗi thì quay lui (rollback / 롤백) hoặc disable bằng cách nào.

> **Nối mạch:** **Phạm vi đã cover** khép README bằng owner, version và depth boundary; phần thiếu quay về chapter Kotlin/Android tương ứng thay vì mở bản sao.

## Phạm vi đã cover

Bộ tài liệu không chỉ dạy cú pháp (syntax / 문법) Kotlin. Nó nối Kotlin ngôn ngữ (language / 언어) với Android thời gian chạy (runtime / 런타임), vòng đời (lifecycle / 생명주기), Compose lẫn XML/View, Gradle/AGP, coroutine/luồng (flow / 흐름), persistence/networking, DI, điều hướng (navigation / 내비게이션), background công việc (work / 작업), testing, hiệu năng (performance / 성능), bảo mật (security / 보안), bản dựng (build / 빌드)/bản phát hành (release / 릴리스), AAB/delivery, bản địa (native / 네이티브) NDK/JNI, nền tảng (platform / 플랫폼) tính tương thích (compatibility / 호환성), startup, thư viện (library / 라이브러리) authoring, legacy di chuyển (migration / 마이그레이션), hệ thống (system / 시스템) components, hardware năng lực (capability / 역량) và kiến trúc vận hành (production architecture / 운영 아키텍처).

Mục tiêu cuối cùng không phải nhớ mọi API, mà là khi gặp yêu cầu (requirement / 요구사항) mới có thể tự suy luận theo các trục:

```text
invariant
→ lifetime
→ ownership
→ source of truth
→ execution context
→ capability
→ build variant / artifact
→ concurrency / ordering
→ failure / compatibility
→ security
→ observability
→ release / recovery
```

và khi cần có thể hạ xuống trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임)/nền tảng (platform / 플랫폼)/bản địa (native / 네이티브)/hệ thống dựng (build system / 빌드 시스템) để giải thích hành vi (behavior / 동작) thay vì dựa vào “magic”.

> **Bàn giao:** Sau **Phạm vi đã cover**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
