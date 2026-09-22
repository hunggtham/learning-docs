# WebSquare JavaScript Knowledge Library

WebSquare trong repository này được đặt tại `10_frontend/websquare/` vì đây là một nền tảng phát triển giao diện web doanh nghiệp (enterprise web UI platform / 엔터프라이즈 웹 UI 플랫폼) chạy trên nền browser, JavaScript, XML và HTTP. Nó không phải là một ngôn ngữ lập trình mới. Vì vậy library này không lặp lại JavaScript, XML, CSS hay kiến thức browser đã có canonical source; thay vào đó nó tập trung vào lớp abstraction riêng của WebSquare: page model, component object, Scope, `scwin`, `$p`, DataCollection, Submission, WFrame, GridView, popup, SPA, lifecycle, reusable component architecture và production practice.

Nếu JavaScript cơ bản còn chưa chắc, hãy đọc [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md). Khi cần hiểu event loop, async, browser runtime, memory, security và performance sâu hơn, dùng [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md). XML syntax và parsing model nằm ở [XML Beginner](../xml/xml_01_beginner_detailed.md) và các chapter tiếp theo. Library WebSquare chỉ tóm tắt phần prerequisite đủ để đọc liền mạch rồi đi vào semantics của framework.

## Baseline và phạm vi version

Baseline thực hành chính của library là **WebSquare5 SP5**, vì đây là dòng tài liệu WebSquare5 có đầy đủ development guide, API reference, DataCollection, Submission, WFrame/Scope, GridView và production configuration. Tài liệu chính thức năm 2026 đồng thời đã có API reference cho dòng **6.0 / WebSquare AI**. Library không giả định API giữa các generation là drop-in replacement. Mental model ổn định được giải thích ở chapter chính; khác biệt generation, legacy behavior và cách kiểm chứng API theo engine build được gom ở chapter migration/reference.

Trong WebSquare, build engine cụ thể quan trọng hơn việc chỉ nhớ tên “WebSquare5”. Nhiều API/property tồn tại lâu nhưng behavior, default, deprecation hoặc rendering implementation có thể thay đổi giữa SP và build. Release notes 2026 tiếp tục bổ sung behavior Scope/WFrame như `scopeInherit="recursive"`, cho thấy ngay cả những primitive cốt lõi vẫn tiến hóa. Khi làm production, luôn đối chiếu API reference và release note đúng build đang chạy trước khi áp dụng property ít phổ biến.

## Mental model cốt lõi

Một page WebSquare thường được author dưới dạng XML. XML này mô tả component tree, DataCollection, Submission và script. W-Pack có thể chuyển page source thành JavaScript tối ưu để engine tải và render trong browser. Vì vậy code bạn viết nhìn giống “XML + JavaScript”, nhưng runtime cuối cùng vẫn là JavaScript chạy trong browser dưới sự điều phối của WebSquare Engine.

Có bốn lớp cần tách rõ khi debug:

**Lớp browser/JavaScript** quyết định lexical scope, closure, event loop, Promise, HTTP, DOM, memory và exception semantics.

**Lớp WebSquare Engine** tạo component object, quản lý lifecycle, Scope, page loading, binding, Submission và rendering abstraction.

**Lớp page/domain** chứa `scwin.*`, validation, orchestration, mapping dữ liệu và business interaction.

**Lớp server** xử lý HTTP endpoint, session, authentication, transaction, database và business rules thật sự. WebSquare không thay thế server-side correctness hay authorization.

Khi một lỗi xảy ra, câu hỏi đầu tiên không nên là “API nào sai?” mà là “lỗi đang thuộc lớp nào?”. Cách chia này giảm rất nhiều thời gian debug các project enterprise lớn.

## Thứ tự học canonical

1. [01 — Platform, Runtime & Page Model](01_platform_runtime_page_model.md) xây mental model từ Studio → XML page → W-Pack → Engine → browser; giải thích component object, page lifecycle, `scwin`, `$p`, DOM boundary và cách JavaScript thật sự sống trong WebSquare.
2. [02 — Components, Events & Data Binding](02_components_events_binding.md) giải thích component API, value/display value, event flow, binding, validation, ID, state ownership và coding idiom khi viết handler.
3. [03 — DataCollection & Submission](03_data_collection_submission.md) đi sâu DataMap, DataList, LinkedDataList, row status, request/response mapping, Submission lifecycle, async/race condition, error handling và transaction boundary.
4. [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md) là chapter quan trọng nhất để đọc codebase lớn: Scope isolation, `scwin`, `$p`, `parent/main/top/getWindow`, parameter passing, WFrame, TabControl, WindowContainer, popup và SPA navigation.
5. [05 — GridView, CRUD & Enterprise Screen Patterns](05_gridview_crud_patterns.md) nối GridView với DataList, row status, query/edit/save flow, large dataset, Excel, validation và các anti-pattern thường gặp trong màn hình nghiệp vụ.
6. [06 — Debugging, Performance, Security & Production](06_debugging_performance_security.md) trình bày evidence-driven debugging, network trace, scope inspection, submission diagnostics, rendering cost, memory, XSS, authorization boundary, config, observability và incident reasoning.
7. [07 — Legacy, Modern Evolution & Migration](07_legacy_modern_migration.md) giúp đọc project WebSquare nhiều thế hệ: global-style code, IFrame SPA, `$w` → `$p`, Scope adoption, SP behavior, WebSquare5 SP5 và hướng 6.0/WebSquare AI.
8. [08 — Reusable Architecture, UDC & Common Modules](08_reusable_architecture_udc_common_modules.md) giải thích khi nào dùng UDC, WFrame, common module, template hay snippet; cách thiết kế property/method/event contract, state ownership, dynamic component, Generator và versioning reusable layer.
9. [09 — Forms, Validation, Internationalization & Accessibility](09_forms_validation_i18n_accessibility.md) tách input filtering khỏi validation và security; đi sâu canonical value, cross-field rules, focus/tab order, language pack, locale key, Grid accessibility, upload/Excel trust boundary và multilingual layout.
10. [10 — Rendering, Lazy Loading & Resource Lifetime](10_rendering_lazy_loading_lifetime.md) xây state model `source → object → render → active → data-ready → disposed`; giải thích TabControl `alwaysDraw`, `wframePreload`, lazy cost, stale async result, timer/listener cleanup, W-Pack/cache và lifecycle performance.
11. [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md) chuyển mental model thành executable evidence: pure/page/UDC/integration/E2E boundaries, deterministic async, race/lifecycle test, DataList row-status regression, accessibility/i18n/security negative test, memory/performance regression và CI strategy.
12. [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md) đi từ canonical source → W-Pack artifact → config → deployment → cache/browser runtime; giải thích reproducible build, `client.config.xml`/`server.config.xml`, context root, engine build, artifact identity, cache invalidation, rollback, smoke test và config drift.
13. [13 — GridView Editing, Identity & View Internals](13_gridview_editing_identity_internals.md) đi sâu editor state so với DataList state, edit commit lifecycle, view/model index, sort/filter/group identity, selection, bulk mutation, formatter/summary cost, server paging và Excel import/export semantics.
14. [14 — Application Shell, Navigation & Multi-Screen State](14_application_shell_navigation_state.md) nâng Scope/WFrame lên architecture app shell: screen definition/instance identity, TabControl/WindowContainer host, navigation key, reuse policy, global state, unsaved-close protocol, deep link, cross-screen communication và shell observability.
15. [15 — Backend Contract, Transaction & Concurrency Integration](15_backend_contract_transaction_concurrency.md) làm rõ ranh giới WebSquare–server: C/U/D contract, writable fields, null semantics, error taxonomy, idempotency, optimistic locking, all-or-nothing/partial batch, created-row correlation, session expiration và contract versioning.
16. [16 — Master Production Playbook & End-to-End Case Studies](16_master_production_playbook.md) hợp nhất toàn bộ library thành các graph reasoning, identity, readiness/trust/state ownership, design/debug/performance/memory/security/migration/release playbook và case study production end-to-end. Chapter này được cập nhật tiếp khi Master track mở rộng.
17. [17 — File, Excel, Upload & Download Pipeline](17_file_excel_upload_download_pipeline.md) tách business data, binary content và metadata; đi sâu upload trust boundary, staging/orphan cleanup, Excel/CSV ingestion, encoding, large export, DRM, mobile download và file consistency.
18. [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md) coi native bridge như RPC boundary; giải thích capability adapter, request identity, page/native lifecycle, permission, deep link, bridge versioning, auth synchronization, eKYC workflow, offline/retry và hybrid security.
19. [19 — Observability, Logging & Incident Response](19_observability_incident_response.md) biến mental model thành production evidence: correlation ID, `$p.log`, WebSquare client/server log, scope-aware debugging, engine/build identity, Submission telemetry, performance/memory evidence, runbook, RCA và regression guard.
20. [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) dùng để tra thuật ngữ Việt–Anh–Hàn và tự kiểm tra xem đã hiểu library ở mức nào.

Luồng dependency nên nhớ là:

`JavaScript/browser → WebSquare page/component model → Scope → DataCollection → Submission → WFrame/SPA → Grid/CRUD → reusable contracts → form/accessibility boundaries → rendering/lifetime → testable contracts → build/config/deployment → Grid identity internals → application shell → backend transaction contract → file/data-exchange boundary → hybrid/native boundary → observability/incident reasoning → Master production reasoning`.

GridView được đặt sau DataCollection và Scope có chủ đích. Nếu học Grid API trước, người học thường thao tác bằng index và handler một cách máy móc nhưng không hiểu dữ liệu thật nằm ở đâu, row state thuộc object nào, hoặc tại sao cùng một component ID lại hoạt động ở nhiều WFrame.

Các chapter 08–12 giải quyết các vấn đề architecture chỉ lộ ra khi project lớn: abstraction dùng chung bắt đầu coupling mọi page, UI validation bị nhầm với trust boundary, lazy/preload/render lifecycle tạo race hoặc memory leak, regression test trở nên flaky vì không có observable contract, và production chạy artifact/config khác thứ developer đang nhìn.

Các chapter 13–19 là **Master track**. Chúng không phải danh sách API nâng cao. Chúng nối row/entity identity trong Grid, screen-instance identity trong app shell, request/transaction identity ở server, artifact/file identity, native-operation identity và correlation identity trong production telemetry. Chapter 16 đóng vai trò synthesis/playbook và được mở rộng cùng các chapter Master mới, thay vì trở thành một tài liệu tách rời rồi lỗi thời.

## Coding style của library

Ví dụ mặc định dùng `scwin` cho page-scope function và `$p` cho page-aware WebSquare utility. Component ID như `inputUserId`, `grdUser`, DataMap như `dmSearch`, DataList như `dlUser`, Submission như `sbmSearchUser` nhằm làm rõ vai trò ngay từ tên.

Handler nên mỏng: đọc input cần thiết, validate, cập nhật model hoặc gọi một hàm orchestration. Business rule dài không nên bị nhét trực tiếp vào `onclick`. Network call phải có đường đi thành công, lỗi, retry/cancel khi cần và guard chống duplicate submission. Khi code cần đi qua nhiều Scope bằng chuỗi `parent().parent()` hoặc phụ thuộc mạnh vào component ID của page khác, đó là tín hiệu coupling cao cần xem lại boundary.

Reusable component nên expose contract theo capability thay vì internals. Một UDC tốt cho consumer biết property nào cấu hình behavior, method nào là command và event nào trả kết quả; consumer không cần biết ID Input/Grid/DataMap bên trong. Common function càng thuần và càng ít phụ thuộc page Scope càng dễ test và tái sử dụng.

Ở Master track, tên biến phải thể hiện identity và coordinate system. `rowIndex` dùng lâu dài là mơ hồ; `viewRowIndex`, `modelRowIndex`, `orderId`, `screenInstanceKey`, `requestId`, `uploadSessionId` và `nativeRequestId` làm dependency rõ hơn. Tương tự, từ “loaded” nên được thay bằng source-ready, object-ready, render-ready, data-ready, native-ready hoặc artifact-ready khi lifecycle là nguyên nhân của behavior.

## First principles: WebSquare giải quyết vấn đề gì?

Ứng dụng enterprise thường có rất nhiều form, grid, popup, validation, request/response mapping và màn hình CRUD. Nếu mỗi màn hình tự làm DOM manipulation, serialization, AJAX, row-state tracking và popup coordination, code nhanh chóng trở nên không đồng nhất. WebSquare cung cấp một runtime và một tập component/data abstraction thống nhất để đội phát triển có thể xây nhiều màn hình nghiệp vụ theo cùng convention.

Lợi ích đó đi kèm một trade-off quan trọng: developer phải hiểu **framework state** chứ không chỉ JavaScript. Một `input1` không đơn thuần là DOM `<input>`, GridView không phải chỉ là HTML table, DataList không chỉ là Array, và một page trong WFrame không phải lúc nào cũng chia sẻ global scope với page cha. Những abstraction này giúp project lớn quản lý được complexity, nhưng cũng tạo ra failure mode riêng nếu developer coi chúng như DOM/JavaScript thuần.

Ở cấp cao hơn, WebSquare còn buộc developer reasoning về **lifetime**, **identity**, **trust boundary** và **artifact provenance**. Một object có thể được preload nhưng UI chưa render; một tab có thể bị ẩn nhưng page instance vẫn sống; một Submission có thể trả response sau khi user đã chuyển page; một Grid row có thể đổi index sau sort; file có thể đã ghi xuống storage nhưng DB transaction chưa commit; native camera có thể callback sau khi page bị destroy; source XML trên Git có thể mới nhưng browser vẫn chạy W-Pack artifact cũ. Vì vậy “đã load chưa?”, “row nào?”, “file đã lưu chưa?”, “native đã xong chưa?” và “đã deploy chưa?” đều phải được thay bằng câu hỏi chính xác hơn.

## Cách học bằng project nhỏ

Sau chapter 01–03, hãy tự dựng một màn hình tra cứu gồm điều kiện tìm kiếm, một `DataMap` cho request, một `DataList` cho kết quả, một `Submission` và một GridView. Sau đó thêm chức năng sửa một dòng, theo dõi row status và lưu. Sau chapter 04, đặt màn hình đó trong WFrame và mở một popup chi tiết bằng parameter object. Sau chapter 06, dùng DevTools để giải thích được request nào chạy, scope nào chứa object, dữ liệu thay đổi ở DataList hay chỉ ở UI, và bottleneck nằm ở network, JavaScript hay rendering.

Sau chapter 08, tách employee selector hoặc date-range selector thành UDC có public property/method/event mà page cha không biết internal IDs. Sau chapter 09, chạy cùng screen bằng Korean/English hoặc Vietnamese text dài hơn, thao tác hoàn toàn bằng keyboard và fault-inject server validation error. Sau chapter 10, đặt screen vào TabControl lazy, mở/đóng lặp 30 lần, kiểm tra Network/heap/listener và chứng minh không có stale request ghi đè page mới.

Sau chapter 11, biến các invariant đó thành regression suite: đảo thứ tự response, double-click Save, đóng page khi request pending, dùng nested WFrame topology và kiểm tra UDC qua public contract. Sau chapter 12, chạy W-Pack bằng build pipeline, gắn build identity, deploy cùng artifact qua environment, rồi chứng minh browser thực sự nhận đúng version bằng Network/evidence thay vì dựa vào việc source đã merge.

Với Master track 13–16, nâng project thành mini enterprise app: server paging, Grid bulk edit, multi-tab detail theo business key, unsaved-close guard, optimistic locking, partial/all-or-nothing batch contract, session expiration, correlation ID và fault injection. Sau chapter 17, thêm attachment staging, Excel import preview/error report và asynchronous large export. Sau chapter 18, giả lập native bridge cho camera/file/deep link và test late callback khi page đã đóng. Sau chapter 19, gắn request/build identity, timing mark và viết runbook cho ba incident: Grid trống sau Search, Save quay mãi và hybrid callback không về.

Mục tiêu cuối cùng không phải nhớ càng nhiều API càng tốt. Mục tiêu là nhìn một màn hình WebSquare và mô tả được **state nằm ở đâu, identity nào đang được dùng, event chạy ở scope nào, dữ liệu đi qua object nào, network/native/file operation được điều phối ra sao, abstraction nào sở hữu lifecycle, readiness hiện tại là gì, trust boundary ở đâu, transaction contract là gì, artifact/config nào đang chạy, test nào bảo vệ invariant và evidence nào chứng minh giả thuyết khi có lỗi**.

## Nguồn chuẩn để kiểm chứng API

Library ưu tiên tài liệu chính thức của Inswave Systems: WebSquare5 SP5 Development Guide, SP5 API Reference, SP5 Release Notes và API reference của dòng 6.0/WebSquare AI. Những URL cụ thể thay đổi theo build, vì vậy chapter không hard-code một build làm “chân lý vĩnh viễn”. Với API/property version-sensitive, hãy tra đúng engine build của project.

Các chapter 08–19 ghi rõ boundary cần đối chiếu official guide cho UDC, multilingual configuration, TabControl/WindowContainer, Grid editing/event ordering, Excel/CSV, upload/download, performance, debugging/logging, W-Pack, client/server configuration, file transfer, hybrid behavior và WFrame lifecycle để người đọc kiểm tra exact property theo build thay vì biến library thành bản sao API reference.

Các nguồn nền tảng ngoài WebSquare được giữ ở canonical JavaScript/XML/Computer Science/backend docs của repository để tránh duplicate.