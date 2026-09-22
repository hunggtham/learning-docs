# WebSquare JavaScript Knowledge Library

WebSquare trong repository này nằm tại `10_frontend/websquare/` vì đây là một nền tảng giao diện web doanh nghiệp (enterprise web UI platform / 엔터프라이즈 웹 UI 플랫폼) chạy trên browser, JavaScript, XML và HTTP. Nó không phải ngôn ngữ lập trình riêng. Library này vì vậy không lặp lại JavaScript, XML, CSS, HTTP hay backend fundamentals đã có canonical source; nó tập trung vào abstraction và failure mode riêng của WebSquare: page/component model, Scope, `scwin`, `$p`, DataCollection, Submission, WFrame, GridView, popup/SPA, reusable component, rendering lifetime, W-Pack, hybrid bridge và production operation.

Nếu JavaScript cơ bản chưa chắc, đọc [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md). Event loop, async, browser runtime, memory, security và performance sâu hơn nằm ở [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md). XML syntax/parsing model nằm ở [XML Beginner](../xml/xml_01_beginner_detailed.md) và track XML. WebSquare chapter chỉ nhắc prerequisite đủ để đọc liền mạch rồi đi vào semantics của platform.

## Baseline và phạm vi version

Baseline thực hành chính là **WebSquare5 SP5** vì dòng này có Development Guide, API Reference, Release Notes, DataCollection/Submission, WFrame/Scope, GridView, W-Pack và client/server configuration tương đối đầy đủ. Tài liệu chính thức hiện cũng có dòng 6.0/WebSquare AI. Library không giả định API giữa generation là drop-in replacement.

Trong production, **engine build cụ thể quan trọng hơn tên “SP5”**. Property, default, event ordering, cache behavior, security fix và private internals có thể đổi theo build. Exact API/property phải đối chiếu API Reference và Release Notes đúng engine đang chạy. Canonical chapter ưu tiên mental model bền hơn version.

## Mental model cốt lõi

Một page WebSquare thường được author bằng XML, chứa component tree, DataCollection, Submission và script. W-Pack có thể chuyển page XML thành JavaScript artifact để WebSquare Engine load/render trong browser. Vì vậy cần tách ít nhất các lớp:

```text
Browser / JavaScript runtime
→ WebSquare Engine / component / Scope
→ Page & domain orchestration
→ Integration contract / HTTP / native bridge
→ Server / transaction / authorization
→ Artifact / config / cache / environment
```

Khi lỗi xảy ra, câu hỏi đầu tiên không phải “API nào sai?” mà là **boundary nào đang vi phạm invariant**.

## Thứ tự học canonical

1. [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md) — Studio → XML → W-Pack → Engine → browser; component object, lifecycle, `scwin`, `$p`, DOM boundary.
2. [02 — Components, Events & Data Binding](02_components_events_binding.md) — component API, value/display value, event flow, binding, validation, ID và state ownership.
3. [03 — DataCollection & Submission](03_data_collection_submission.md) — DataMap, DataList, LinkedDataList, row status, request/response mapping, Submission lifecycle, async/race/error.
4. [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) — Scope isolation, `parent/main/top/getWindow`, parameter contract, WFrame, TabControl, WindowContainer, popup và SPA.
5. [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) — GridView/DataList, query/edit/save, row status, large dataset, validation và CRUD pattern.
6. [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md) — evidence-driven debugging, network/scope/submission evidence, rendering cost, memory, XSS và trust boundary.
7. [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md) — global-style code, IFrame SPA, `$w` → `$p`, Scope adoption, legacy/modern compatibility.
8. [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md) — UDC/WFrame/common module/template/snippet, public contract, dynamic component và reusable ownership.
9. [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md) — canonical value, validation boundary, focus/tab, language pack, locale, accessibility và input/file trust.
10. [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md) — `source → object → render → active → data-ready → disposed`, preload/lazy, stale async, timer/listener cleanup.
11. [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md) — pure/page/UDC/integration/E2E boundary, deterministic async, race/lifecycle/memory/performance regression.
12. [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md) — W-Pack artifact, config, context root, build provenance, cache invalidation, rollback và config drift.
13. [13 — GridView Editing, Identity & View Internals](13_gridview_editing_identity_internals.md) — editor vs model state, edit commit, view/model index, sort/filter identity, bulk update, paging và Excel semantics.
14. [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md) — screen definition/instance, navigation key, global state, unsaved-close, deep link và cross-screen communication.
15. [15 — Backend Contract, Transaction & Concurrency Integration](15_backend_contract_transaction_concurrency.md) — writable fields, null semantics, idempotency, optimistic locking, batch transaction, created-row correlation và contract versioning.
16. [16 — Master Production Playbook & End-to-End Case Studies](16_master_production_playbook.md) — synthesis các graph reasoning, identity, readiness/trust/state ownership, debugging/performance/memory/security/release playbook.
17. [17 — File, Excel, Upload & Download Pipeline](17_file_excel_upload_download_pipeline.md) — binary/metadata/business state, staging/orphan cleanup, Excel/CSV ingestion, encoding, large export và file consistency.
18. [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md) — bridge như RPC boundary, capability/version, native request identity, permission, deep link, eKYC, offline/retry và hybrid security.
19. [19 — Observability, Logging & Incident Response](19_observability_incident_response.md) — correlation ID, WebSquare/browser/server evidence, Submission telemetry, performance/memory evidence, runbook và RCA.
20. [20 — Authentication, Session, SSO & Security Lifecycle](20_authentication_session_sso_security_lifecycle.md) — auth/session/authorization state machine, expiry/reauth, 401/403, CSRF boundary, permission snapshot, principal switch, multi-tab và hybrid auth reconciliation.
21. [21 — Integration Topology, MSA, Real-Time & Resilience](21_integration_topology_msa_realtime_resilience.md) — gateway/BFF/microservice topology, SP5 MSA resource concepts, timeout/retry ownership, partial failure, polling/SSE/WebSocket mental model, event ordering, backpressure và client/server version skew.
22. [22 — Engine, Configuration, Cache & Upgrade Internals](22_engine_config_cache_upgrade_internals.md) — runtime composition, engine build, client/server config, W-Pack internals, cache layers/postfix, provenance, upgrade matrix, public/private API boundary và rollback reasoning.
23. [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) — glossary Việt–Anh–Hàn và coverage/mastery audit.

## Dependency map

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
→ Master end-to-end reasoning
```

GridView được đặt sau DataCollection và Scope có chủ đích. Học Grid API trước model/identity thường dẫn đến code giữ row index, sửa UI thay vì model và không hiểu cùng component ID trong nhiều WFrame.

Các chapter 08–12 xử lý complexity chỉ lộ khi project lớn: abstraction dùng chung coupling screen, UI validation bị nhầm trust boundary, lazy/preload tạo race/leak, regression test flaky và production chạy artifact/config khác source developer đang nhìn.

Các chapter 13–22 là **Master track**. Chúng nối nhiều identity: row/entity, screen instance, request/transaction, upload/file, native request, correlation, principal/session, event/version và runtime artifact/build. Master không phải nhớ nhiều property hơn; Master là giữ đúng identity, ownership, lifecycle và evidence qua nhiều boundary.

## Coding style của library

Ví dụ mặc định dùng `scwin` cho page-scope function và `$p` cho page-aware WebSquare utility. Component/DataCollection/Submission được đặt tên theo vai trò như `grdUser`, `dmSearch`, `dlUser`, `sbmSearchUser`.

Handler nên mỏng: đọc input, validate, cập nhật canonical client model hoặc gọi orchestration function. Business rule dài không nên nằm trực tiếp trong `onclick`. Network/native/file operation phải có success/error/timeout/cancel hoặc stale-result policy phù hợp.

Reusable component expose capability qua property/method/event thay vì internal ID. Cross-screen code đi qua chuỗi `parent().parent()` hoặc tìm component của page khác là tín hiệu coupling cần xem lại.

Ở Master track, tên phải thể hiện identity/coordinate system: `viewRowIndex`, `modelRowIndex`, `orderId`, `screenInstanceKey`, `requestId`, `uploadSessionId`, `nativeRequestId`, `eventId`, `principalId`, `buildId`. Từ “loaded” nên được thay bằng source-ready, object-ready, render-ready, data-ready, auth-ready, native-ready hoặc artifact-ready khi lifecycle quan trọng.

## First principles

WebSquare chuẩn hóa những việc ứng dụng enterprise phải làm lặp lại: form, grid, popup, binding, validation, communication, page composition và reusable UI. Trade-off là developer phải hiểu **framework state** chứ không chỉ JavaScript.

Ở mức production, còn phải reasoning về **lifetime, identity, trust boundary, integration topology và artifact provenance**. Page có thể còn sống khi session đã chết; response có thể về sau user intent mới; row index đổi sau sort; file có thể tồn tại nhưng DB chưa commit; native callback có thể về sau page disposed; event real-time có thể duplicate/out-of-order; source Git có thể mới nhưng browser chạy W-Pack/config cũ.

Vì vậy câu hỏi “đã load chưa?”, “row nào?”, “đã login chưa?”, “API nào?”, “đã deploy chưa?” đều phải được thay bằng câu hỏi có identity và evidence cụ thể.

## Cách học bằng project nhỏ

Sau 01–06, dựng Search → `dmSearch` → `sbmSearch` → `dlUser` → GridView → edit/save và debug được request/model/render boundary.

Sau 08–12, tách một selector thành UDC contract, thêm i18n/accessibility, đặt screen trong lazy TabControl, viết regression race/lifecycle và build W-Pack có artifact identity.

Sau 13–19, nâng thành mini enterprise app có server paging, bulk edit, multi-tab detail theo business key, optimistic locking, upload/Excel, hybrid capability, correlation ID và incident runbook.

Sau 20–22, fault-inject thêm:

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
```

Mỗi case phải giải thích được invariant, owner, identity, retry safety, invalidation, evidence và regression guard.

## Nguồn chuẩn để kiểm chứng

Library ưu tiên tài liệu chính thức của Inswave Systems: WebSquare5 SP5 Development Guide, SP5 API Reference, SP5 Release Notes và API reference của dòng 6.0/WebSquare AI. Exact URL/build thay đổi theo thời gian nên canonical note không coi một property/version là chân lý vĩnh viễn.

Các chapter Master ghi rõ khi behavior/API build-dependent. Kiến thức nền về browser security, HTTP, OAuth/OIDC/SAML, WebSocket/SSE, microservices, database transaction và backend authorization được cross-link theo conceptual boundary thay vì duplicate thành tutorial ngoài phạm vi WebSquare.

Mục tiêu cuối cùng là nhìn một màn hình WebSquare và mô tả được **state nằm ở đâu, identity nào đang dùng, event chạy ở scope nào, dữ liệu đi qua object nào, security/session state nào đang active, request đi qua topology nào, abstraction nào sở hữu lifetime, artifact/config/engine nào đang chạy, test nào bảo vệ invariant và evidence nào chứng minh root cause**.