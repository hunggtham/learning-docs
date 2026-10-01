# WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Baseline và phạm vi phiên bản (version / 버전)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mô hình tư duy (mental model / 사고 모델) cốt lõi** để rút ra mô hình chung và giới hạn. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

WebSquare trong repository này nằm tại `10_frontend/websquare/` vì đây là một nền tảng giao diện web doanh nghiệp (enterprise web UI platform / 엔터프라이즈 웹 UI 플랫폼) chạy trên trình duyệt (browser / 브라우저), JavaScript, XML và HTTP. Nó không phải ngôn ngữ lập trình riêng. thư viện (library / 라이브러리) này vì vậy không lặp lại JavaScript, XML, CSS, HTTP hay backend fundamentals đã có chuẩn gốc (canonical / 정본) nguồn (source / 소스); nó tập trung vào lớp trừu tượng (abstraction / 추상화) và dạng thất bại (failure mode / 실패 모드) riêng của WebSquare: page/thành phần (component / 컴포넌트) mô hình (model / 모델), phạm vi (scope / 범위), `scwin`, `$p`, DataCollection, Submission, Workflow, WFrame, GridView, popup/SPA, reusable thành phần (component / 컴포넌트), rendering thời gian tồn tại (lifetime / 수명), W-Pack, hybrid cầu nối (bridge / 브리지), sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), hiệu năng (performance / 성능) profiling và môi trường vận hành (production / 운영 환경) thao tác (operation / 연산).

Nếu JavaScript cơ bản chưa chắc, đọc [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md). vòng lặp sự kiện (event loop / 이벤트 루프), async, trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임), bộ nhớ (memory / 메모리), bảo mật (security / 보안) và hiệu năng (performance / 성능) sâu hơn nằm ở [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md). XML cú pháp (syntax / 문법)/parsing mô hình (model / 모델) nằm ở [XML Beginner](../xml/xml_01_beginner_detailed.md) và nhánh học (track / 트랙) XML. WebSquare chapter chỉ nhắc prerequisite đủ để đọc liền mạch rồi đi vào ngữ nghĩa (semantics / 의미론) của nền tảng (platform / 플랫폼).

## Baseline và phạm vi phiên bản (version / 버전)

Baseline thực hành chính là **WebSquare5 SP5** vì dòng này có Development Guide, API tham chiếu (reference / 참조), bản phát hành (release / 릴리스) Notes, DataCollection/Submission, Workflow, WFrame/phạm vi (scope / 범위), GridView, W-Pack và máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (configuration / 구성) tương đối đầy đủ. Tài liệu chính thức hiện cũng có dòng 6.0/WebSquare AI. thư viện (library / 라이브러리) không giả định API giữa generation là drop-in replacement.

Trong môi trường vận hành (production / 운영 환경), **engine bản dựng (build / 빌드) cụ thể quan trọng hơn tên “SP5”**. thuộc tính (property / 속성), default, sự kiện (event / 이벤트) thứ tự (ordering / 순서), bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작), bảo mật (security / 보안) fix và private internals có thể đổi theo bản dựng (build / 빌드). chính xác (exact / 정확한) API/thuộc tính (property / 속성) phải đối chiếu API tham chiếu (reference / 참조) và bản phát hành (release / 릴리스) Notes đúng engine đang chạy. chuẩn gốc (canonical / 정본) chapter ưu tiên mô hình tư duy (mental model / 사고 모델) bền hơn phiên bản (version / 버전).

> **Chuyển mạch:** Trong **WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Mô hình tư duy (mental model / 사고 모델) cốt lõi** gom các mảnh từ **Baseline và phạm vi phiên bản (version / 버전)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Thứ tự học chuẩn gốc (canonical / 정본)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델) cốt lõi

Một page WebSquare thường được author bằng XML, chứa thành phần (component / 컴포넌트) cây (tree / 트리), DataCollection, Submission và script. W-Pack có thể chuyển page XML thành JavaScript sản phẩm tạo ra (artifact / 산출물) để WebSquare Engine tải (load / 로드)/kết xuất (render / 렌더링) trong trình duyệt (browser / 브라우저). Vì vậy cần tách ít nhất các lớp:

```text
Browser / JavaScript runtime
→ WebSquare Engine / component / Scope
→ Page & domain orchestration
→ Integration contract / HTTP / native bridge
→ Server / transaction / authorization
→ Artifact / config / cache / environment
```

Khi lỗi xảy ra, câu hỏi đầu tiên không phải “API nào sai?” mà là **ranh giới (boundary / 경계) nào đang vi phạm bất biến (invariant / 불변식)**.

> **Chuyển mạch:** Ở chặng này của **WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Thứ tự học chuẩn gốc (canonical / 정본)** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델) cốt lõi** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Phụ thuộc (dependency / 의존성) map** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự học chuẩn gốc (canonical / 정본)

1. [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md) — Studio → XML → W-Pack → Engine → trình duyệt (browser / 브라우저); thành phần (component / 컴포넌트) đối tượng (object / 객체), vòng đời (lifecycle / 생명주기), `scwin`, `$p`, DOM ranh giới (boundary / 경계).
2. [02 — Components, Events & Data Binding](02_components_events_binding.md) — thành phần (component / 컴포넌트) API, giá trị (value / 값)/display giá trị (value / 값), sự kiện (event / 이벤트) luồng (flow / 흐름), binding, kiểm tra hợp lệ (validation / 검증), ID và quyền sở hữu trạng thái (state ownership / 상태 소유권).
3. [03 — DataCollection & Submission](03_data_collection_submission.md) — DataMap, DataList, LinkedDataList, row status, yêu cầu (request / 요청)/phản hồi (response / 응답) ánh xạ (mapping / 매핑), Submission vòng đời (lifecycle / 생명주기), async/race/lỗi (error / 오류).
4. [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) — phạm vi (scope / 범위) isolation, `parent/main/top/getWindow`, parameter đặc tả hợp đồng (contract / 계약), WFrame, TabControl, WindowContainer, popup và SPA.
5. [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) — GridView/DataList, truy vấn (query / 쿼리)/edit/save, row status, large dataset, kiểm tra hợp lệ (validation / 검증) và CRUD mẫu (pattern / 패턴).
6. [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md) — evidence-driven debugging, mạng (network / 네트워크)/phạm vi (scope / 범위)/submission bằng chứng (evidence / 증거), rendering chi phí (cost / 비용), bộ nhớ (memory / 메모리), XSS và trust ranh giới (boundary / 경계).
7. [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md) — global-style mã (code / 코드), IFrame SPA, `$w` → `$p`, phạm vi (scope / 범위) adoption, legacy/hiện đại (modern / 현대적) tính tương thích (compatibility / 호환성).
8. [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md) — UDC/WFrame/dùng chung (common / 공통) mô-đun (module / 모듈)/template/snippet, công khai (public / 공개) đặc tả hợp đồng (contract / 계약), động (dynamic / 동적) thành phần (component / 컴포넌트) và reusable quyền sở hữu (ownership / 소유권).
9. [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md) — chuẩn gốc (canonical / 정본) giá trị (value / 값), kiểm tra hợp lệ (validation / 검증) ranh giới (boundary / 경계), focus/tab, ngôn ngữ (language / 언어) pack, locale, khả năng tiếp cận (accessibility / 접근성) và đầu vào (input / 입력)/tệp (file / 파일) trust.
10. [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md) — `source → object → render → active → data-ready → disposed`, preload/lazy, stale async, timer/listener cleanup.
11. [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md) — pure/page/UDC/tích hợp (integration / 통합)/E2E ranh giới (boundary / 경계), deterministic async, race/vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리)/hiệu năng (performance / 성능) regression.
12. [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md) — W-Pack sản phẩm tạo ra (artifact / 산출물), cấu hình (config / 설정), ngữ cảnh (context / 맥락) gốc (root / 루트), bản dựng (build / 빌드) provenance, bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화), quay lui (rollback / 롤백) và cấu hình (config / 설정) drift.
13. [13 — GridView Editing, Identity & View Internals](13_gridview_editing_identity_internals.md) — editor vs mô hình (model / 모델) trạng thái (state / 상태), edit lần ghi nhận (commit / 커밋), view/mô hình (model / 모델) chỉ mục (index / 인덱스), sort/filter định danh (identity / 식별자), bulk cập nhật (update / 업데이트), paging và Excel ngữ nghĩa (semantics / 의미론).
14. [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md) — screen definition/instance, điều hướng (navigation / 내비게이션) key, toàn cục (global / 전역) trạng thái (state / 상태), unsaved-close, deep link và cross-screen communication.
15. [15 — Backend Contract, Transaction & Concurrency Integration](15_backend_contract_transaction_concurrency.md) — writable fields, null ngữ nghĩa (semantics / 의미론), idempotency, optimistic locking, batch giao dịch (transaction / 트랜잭션), created-row correlation và đặc tả hợp đồng (contract / 계약) versioning.
16. [16 — Master Production Playbook & End-to-End Case Studies](16_master_production_playbook.md) — synthesis các đồ thị (graph / 그래프) lập luận (reasoning / 추론), định danh (identity / 식별자), readiness/trust/quyền sở hữu trạng thái (state ownership / 상태 소유권), debugging/hiệu năng (performance / 성능)/bộ nhớ (memory / 메모리)/bảo mật (security / 보안)/bản phát hành (release / 릴리스) playbook.
17. [17 — File, Excel, Upload & Download Pipeline](17_file_excel_upload_download_pipeline.md) — nhị phân (binary / 이진)/siêu dữ liệu (metadata / 메타데이터)/nghiệp vụ (business / 비즈니스) trạng thái (state / 상태), staging/orphan cleanup, Excel/CSV ingestion, encoding, large export và tệp (file / 파일) consistency.
18. [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md) — cầu nối (bridge / 브리지) như RPC ranh giới (boundary / 경계), năng lực (capability / 역량)/phiên bản (version / 버전), bản địa (native / 네이티브) yêu cầu (request / 요청) định danh (identity / 식별자), permission, deep link, eKYC, offline/thử lại (retry / 재시도) và hybrid bảo mật (security / 보안).
19. [19 — Observability, Logging & Incident Response](19_observability_incident_response.md) — correlation ID, WebSquare/trình duyệt (browser / 브라우저)/máy chủ (server / 서버) bằng chứng (evidence / 증거), Submission telemetry, hiệu năng (performance / 성능)/bộ nhớ (memory / 메모리) bằng chứng (evidence / 증거), runbook và RCA.
20. [20 — Authentication, Session, SSO & Security Lifecycle](20_authentication_session_sso_security_lifecycle.md) — auth/session/authorization máy trạng thái (state machine / 상태 머신), expiry/reauth, 401/403, CSRF ranh giới (boundary / 경계), permission snapshot, principal switch, multi-tab và hybrid auth reconciliation.
21. [21 — Integration Topology, MSA, Real-Time & Resilience](21_integration_topology_msa_realtime_resilience.md) — gateway/BFF/microservice topology, SP5 MSA tài nguyên (resource / 자원) concepts, hết thời gian chờ (timeout / 타임아웃)/thử lại (retry / 재시도) quyền sở hữu (ownership / 소유권), partial thất bại (failure / 실패), polling/SSE/WebSocket mô hình tư duy (mental model / 사고 모델), sự kiện (event / 이벤트) thứ tự (ordering / 순서), backpressure và máy khách (client / 클라이언트)/máy chủ (server / 서버) phiên bản (version / 버전) skew.
22. [22 — Engine, Configuration, Cache & Upgrade Internals](22_engine_config_cache_upgrade_internals.md) — thời gian chạy (runtime / 런타임) composition, engine bản dựng (build / 빌드), máy khách (client / 클라이언트)/máy chủ (server / 서버) cấu hình (config / 설정), W-Pack internals, bộ nhớ đệm (cache / 캐시) layers/postfix, provenance, upgrade ma trận (matrix / 행렬), công khai (public / 공개)/private API ranh giới (boundary / 경계) và quay lui (rollback / 롤백) lập luận (reasoning / 추론).
23. [23 — Workflow Orchestration, Advanced Data State & Enterprise Error Architecture](23_workflow_orchestration_data_state_error_architecture.md) — phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), serial/parallel Workflow, workflow-run định danh (identity / 식별자), cancellation/atomicity, DataList dirty-state acknowledgement, null/kiểu (type / 타입) ngữ nghĩa (semantics / 의미론), lỗi (error / 오류) taxonomy, thử lại (retry / 재시도)/idempotency và compensation.
24. [24 — Event Semantics, Reentrancy & Performance Profiling](24_event_semantics_performance_profiling.md) — người dùng (user / 사용자)/programmatic sự kiện (event / 이벤트) ngữ nghĩa (semantics / 의미론), build-sensitive thứ tự (ordering / 순서), reentrancy/sự kiện (event / 이벤트) storm, binding amplification, formatter đường xử lý nóng (hot path / 핫 패스), WebSquare/trình duyệt (browser / 브라우저) profiling, large-data bộ nhớ (memory / 메모리) và hiệu năng (performance / 성능) regression kỹ thuật (engineering / 엔지니어링).
25. [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) — glossary Việt–Anh–Hàn và coverage/mastery kiểm tra (audit / 감사). Khi học chapter 23–24, bổ sung mô hình tư duy (mental model / 사고 모델) `workflow run identity`, `state acknowledgement`, `event reentrancy`, `work amplification` và `performance budget` vào checklist Master hiện có.

> **Chuyển mạch:** Canonical route xác định prerequisite; dependency map chuyển route đó thành các module/runtime boundary cụ thể. Coding style tiếp theo giữ các boundary ấy nhất quán trong codebase WebSquare.

## Phụ thuộc (dependency / 의존성) map

```text
JavaScript/browser
→ page/component model
→ Scope
→ DataCollection
→ Submission
→ WFrame/SPA
→ Grid/CRUD
→ reusable contracts
→ forms/i18n/accessibility
→ rendering/lifetime
→ regression engineering
→ build/deployment
→ Grid identity internals
→ application shell
→ backend transaction contract
→ file/data-exchange
→ hybrid/native
→ observability
→ authentication/session lifecycle
→ integration topology/real-time
→ engine/config/cache/upgrade internals
→ workflow/data-state/error orchestration
→ event semantics/performance profiling
→ Master end-to-end reasoning
```

GridView được đặt sau DataCollection và phạm vi (scope / 범위) có chủ đích. Học Grid API trước mô hình (model / 모델)/định danh (identity / 식별자) thường dẫn đến mã (code / 코드) giữ row chỉ mục (index / 인덱스), sửa UI thay vì mô hình (model / 모델) và không hiểu cùng thành phần (component / 컴포넌트) ID trong nhiều WFrame.

Các chapter 08–12 xử lý độ phức tạp (complexity / 복잡도) chỉ lộ khi dự án (project / 프로젝트) lớn: lớp trừu tượng (abstraction / 추상화) dùng chung coupling screen, UI kiểm tra hợp lệ (validation / 검증) bị nhầm trust ranh giới (boundary / 경계), lazy/preload tạo race/leak, regression kiểm thử (test / 테스트) flaky và môi trường vận hành (production / 운영 환경) chạy sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정) khác nguồn (source / 소스) nhà phát triển (developer / 개발자) đang nhìn.

Các chapter 13–24 là **Master nhánh học (track / 트랙)**. Chúng nối nhiều định danh (identity / 식별자): row/thực thể (entity / 엔터티), screen instance, yêu cầu (request / 요청)/giao dịch (transaction / 트랜잭션), upload/tệp (file / 파일), bản địa (native / 네이티브) yêu cầu (request / 요청), correlation, principal/session, sự kiện (event / 이벤트)/phiên bản (version / 버전), thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물)/bản dựng (build / 빌드) và workflow run. Master không phải nhớ nhiều thuộc tính (property / 속성) hơn; Master là giữ đúng định danh (identity / 식별자), quyền sở hữu (ownership / 소유권), vòng đời (lifecycle / 생명주기), thứ tự (ordering / 순서), chi phí (cost / 비용) và bằng chứng (evidence / 증거) qua nhiều ranh giới (boundary / 경계).

> **Chuyển mạch:** Dependency map cho biết module nào được phép gọi module nào; coding style biến rule đó thành convention có thể review. First principles tiếp theo giải thích vì sao convention phục vụ lifecycle và state ownership.

## Coding style của thư viện (library / 라이브러리)

Ví dụ mặc định dùng `scwin` cho page-scope hàm (function / 함수) và `$p` cho page-aware WebSquare utility. thành phần (component / 컴포넌트)/DataCollection/Submission được đặt tên theo vai trò như `grdUser`, `dmSearch`, `dlUser`, `sbmSearchUser`.

Handler nên mỏng: đọc đầu vào (input / 입력), validate, cập nhật chuẩn gốc (canonical / 정본) máy khách (client / 클라이언트) mô hình (model / 모델) hoặc gọi orchestration hàm (function / 함수). nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dài không nên nằm trực tiếp trong `onclick`. mạng (network / 네트워크)/bản địa (native / 네이티브)/tệp (file / 파일) thao tác (operation / 연산) phải có success/lỗi (error / 오류)/hết thời gian chờ (timeout / 타임아웃)/cancel hoặc stale-result chính sách (policy / 정책) phù hợp.

Reusable thành phần (component / 컴포넌트) expose năng lực (capability / 역량) qua thuộc tính (property / 속성)/phương thức (method / 메서드)/sự kiện (event / 이벤트) thay vì nội bộ (internal / 내부) ID. Cross-screen mã (code / 코드) đi qua chuỗi `parent().parent()` hoặc tìm thành phần (component / 컴포넌트) của page khác là tín hiệu coupling cần xem lại.

Ở Master nhánh học (track / 트랙), tên phải thể hiện định danh (identity / 식별자)/coordinate hệ thống (system / 시스템): `viewRowIndex`, `modelRowIndex`, `orderId`, `screenInstanceKey`, `requestId`, `workflowRunId`, `uploadSessionId`, `nativeRequestId`, `eventId`, `principalId`, `buildId`. Từ “loaded” nên được thay bằng source-ready, object-ready, render-ready, data-ready, auth-ready, native-ready hoặc artifact-ready khi vòng đời (lifecycle / 생명주기) quan trọng.

> **Chuyển mạch:** Coding convention chỉ có giá trị khi bảo vệ nguyên lý về page, event, data và state. Project nhỏ tiếp theo dùng các nguyên lý đó trong một flow có thể chạy và review.

## Nguyên lý nền tảng (first principles / 제일 원리)

WebSquare chuẩn hóa những việc ứng dụng enterprise phải làm lặp lại: form, grid, popup, binding, kiểm tra hợp lệ (validation / 검증), communication, page composition và reusable UI. sự đánh đổi (trade-off / 트레이드오프) là nhà phát triển (developer / 개발자) phải hiểu **khung phần mềm (framework / 프레임워크) trạng thái (state / 상태)** chứ không chỉ JavaScript.

Ở mức môi trường vận hành (production / 운영 환경), còn phải lập luận (reasoning / 추론) về **thời gian tồn tại (lifetime / 수명), định danh (identity / 식별자), trust ranh giới (boundary / 경계), tích hợp (integration / 통합) topology, sự kiện (event / 이벤트) thứ tự (ordering / 순서), công việc (work / 작업) amplification và sản phẩm tạo ra (artifact / 산출물) provenance**. Page có thể còn sống khi session đã chết; phản hồi (response / 응답) có thể về sau người dùng (user / 사용자) intent mới; row chỉ mục (index / 인덱스) đổi sau sort; tệp (file / 파일) có thể tồn tại nhưng DB chưa lần ghi nhận (commit / 커밋); bản địa (native / 네이티브) callback có thể về sau page disposed; sự kiện (event / 이벤트) real-time có thể duplicate/out-of-order; workflow có thể partial-commit; nguồn (source / 소스) Git có thể mới nhưng trình duyệt (browser / 브라우저) chạy W-Pack/cấu hình (config / 설정) cũ.

Vì vậy câu hỏi “đã tải (load / 로드) chưa?”, “row nào?”, “đã login chưa?”, “API nào?”, “sự kiện (event / 이벤트) nào?”, “đã deploy chưa?” đều phải được thay bằng câu hỏi có định danh (identity / 식별자) và bằng chứng (evidence / 증거) cụ thể.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Cách học bằng dự án (project / 프로젝트) nhỏ** tiếp nhận điểm tựa từ **Nguyên lý nền tảng (first principles / 제일 원리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nguồn chuẩn để kiểm chứng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cách học bằng dự án (project / 프로젝트) nhỏ

Sau 01–06, dựng tìm kiếm (search / 검색) → `dmSearch` → `sbmSearch` → `dlUser` → GridView → edit/save và gỡ lỗi (debug / 디버그) được yêu cầu (request / 요청)/mô hình (model / 모델)/kết xuất (render / 렌더링) ranh giới (boundary / 경계).

Sau 08–12, tách một selector thành UDC đặc tả hợp đồng (contract / 계약), thêm i18n/khả năng tiếp cận (accessibility / 접근성), đặt screen trong lazy TabControl, viết regression race/vòng đời (lifecycle / 생명주기) và bản dựng (build / 빌드) W-Pack có sản phẩm tạo ra (artifact / 산출물) định danh (identity / 식별자).

Sau 13–19, nâng thành mini enterprise app có máy chủ (server / 서버) paging, bulk edit, multi-tab detail theo nghiệp vụ (business / 비즈니스) key, optimistic locking, upload/Excel, hybrid năng lực (capability / 역량), correlation ID và sự cố (incident / 인시던트) runbook.

Sau 20–24, fault-inject thêm:

```text
session expire giữa Save
permission revoke khi screen đang mở
user A logout → user B login trong cùng runtime
Gateway timeout sau downstream commit
polling overlap sau resume
duplicate/out-of-order real-time event
browser giữ W-Pack/config cũ sau deploy
UAT/PROD khác engine build
hybrid native version cũ + web build mới
Workflow step 1 commit nhưng step 2 fail
user edit thêm DataList trong lúc Save snapshot đang pending
parallel Workflow ghi vào cùng target state
programmatic setValue tạo event/reentrancy bất ngờ
Grid formatter tạo O(rows × cells × lookupRows) work
page open/close lặp lại làm listener invocation tăng dần
```

Mỗi trường hợp (case / 사례) phải giải thích được bất biến (invariant / 불변식), đơn vị sở hữu (owner / 오너), định danh (identity / 식별자), thứ tự (ordering / 순서), thử lại (retry / 재시도) an toàn (safety / 안전), vô hiệu hóa (invalidation / 무효화), chi phí (cost / 비용) mô hình (model / 모델), bằng chứng (evidence / 증거) và regression guard.

> **Chuyển mạch:** Trong **WebSquare JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)**, **Cách học bằng dự án (project / 프로젝트) nhỏ** nêu điều cần giải thích; **Nguồn chuẩn để kiểm chứng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Nguồn chuẩn để kiểm chứng

Thư viện (library / 라이브러리) ưu tiên tài liệu chính thức của Inswave các hệ thống (systems / 시스템들): WebSquare5 SP5 Development Guide, SP5 API tham chiếu (reference / 참조), SP5 bản phát hành (release / 릴리스) Notes và API tham chiếu (reference / 참조) của dòng 6.0/WebSquare AI. chính xác (exact / 정확한) URL/bản dựng (build / 빌드) thay đổi theo thời gian nên chuẩn gốc (canonical / 정본) ghi chú (note / 노트) không coi một thuộc tính (property / 속성)/phiên bản (version / 버전) là chân lý vĩnh viễn.

Các chapter Master ghi rõ khi hành vi (behavior / 동작)/API build-dependent. Đặc biệt Workflow signature, Grid sự kiện (event / 이벤트) thứ tự (ordering / 순서), DataList null/kiểu (type / 타입) hành vi (behavior / 동작), hiệu năng (performance / 성능) instrumentation và engine rendering hành vi (behavior / 동작) phải được kiểm tra theo bản dựng (build / 빌드). Kiến thức nền về trình duyệt (browser / 브라우저) bảo mật (security / 보안), HTTP, OAuth/OIDC/SAML, WebSocket/SSE, microservices, cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션), algorithmic độ phức tạp (complexity / 복잡도) và backend authorization được cross-link theo conceptual ranh giới (boundary / 경계) thay vì duplicate thành tutorial ngoài phạm vi WebSquare.

Mục tiêu cuối cùng là nhìn một màn hình WebSquare và mô tả được **trạng thái (state / 상태) nằm ở đâu, định danh (identity / 식별자) nào đang dùng, sự kiện (event / 이벤트) chạy ở phạm vi (scope / 범위) nào, người dùng (user / 사용자) tín hiệu (signal / 신호) được chuyển thành command nào, workflow/yêu cầu (request / 요청) đồ thị (graph / 그래프) ra sao, dữ liệu đi qua đối tượng (object / 객체) nào, bảo mật (security / 보안)/session trạng thái (state / 상태) nào đang active, yêu cầu (request / 요청) đi qua topology nào, công việc (work / 작업) bị khuếch đại ở đâu, lớp trừu tượng (abstraction / 추상화) nào sở hữu thời gian tồn tại (lifetime / 수명), sản phẩm tạo ra (artifact / 산출물)/cấu hình (config / 설정)/engine nào đang chạy, kiểm thử (test / 테스트) nào bảo vệ bất biến (invariant / 불변식) và bằng chứng (evidence / 증거) nào chứng minh nguyên nhân gốc (root cause / 근본 원인)**.

> **Bàn giao:** Sau **Nguồn chuẩn để kiểm chứng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
