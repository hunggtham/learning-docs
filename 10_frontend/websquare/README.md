# WebSquare JavaScript Knowledge Library

WebSquare trong repository này được đặt tại `10_frontend/websquare/` vì đây là một nền tảng phát triển giao diện web doanh nghiệp (enterprise web UI platform / 엔터프라이즈 웹 UI 플랫폼) chạy trên nền browser, JavaScript, XML và HTTP. Nó không phải là một ngôn ngữ lập trình mới. Vì vậy library này không lặp lại JavaScript, XML, CSS hay kiến thức browser đã có canonical source; thay vào đó nó tập trung vào lớp abstraction riêng của WebSquare: page model, component object, Scope, `scwin`, `$p`, DataCollection, Submission, WFrame, GridView, popup, SPA, lifecycle và production practice.

Nếu JavaScript cơ bản còn chưa chắc, hãy đọc [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md). Khi cần hiểu event loop, async, browser runtime, memory, security và performance sâu hơn, dùng [JavaScript Senior](../javascript/javascript_senior.md) và [JavaScript Master](../javascript/javascript_master_supplement_detailed.md). XML syntax và parsing model nằm ở [XML Beginner](../xml/xml_01_beginner_detailed.md) và các chapter tiếp theo. Library WebSquare chỉ tóm tắt phần prerequisite đủ để đọc liền mạch rồi đi vào semantics của framework.

## Baseline và phạm vi version

Baseline thực hành chính của library là **WebSquare5 SP5**, vì đây là dòng tài liệu WebSquare5 có đầy đủ development guide, API reference, DataCollection, Submission, WFrame/Scope, GridView và production configuration. Tài liệu chính thức năm 2026 đồng thời đã có API reference cho dòng **6.0 / WebSquare AI**. Library không giả định API giữa các generation là drop-in replacement. Mental model ổn định được giải thích ở chapter chính; khác biệt generation, legacy behavior và cách kiểm chứng API theo engine build được gom ở chapter migration/reference.

Trong WebSquare, build engine cụ thể quan trọng hơn việc chỉ nhớ tên “WebSquare5”. Nhiều API/property tồn tại lâu nhưng behavior, default, deprecation hoặc rendering implementation có thể thay đổi giữa SP và build. Khi làm production, luôn đối chiếu API reference đúng build đang chạy trước khi áp dụng một property ít phổ biến.

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
8. [Glossary & Coverage Audit](GLOSSARY_AND_COVERAGE.md) dùng để tra thuật ngữ Việt–Anh–Hàn và tự kiểm tra xem đã hiểu library ở mức nào.

Luồng dependency nên nhớ là:

`JavaScript/browser → WebSquare page/component model → Scope → DataCollection → Submission → WFrame/SPA → Grid/CRUD → production reasoning`.

GridView được đặt sau DataCollection và Scope có chủ đích. Nếu học Grid API trước, người học thường thao tác bằng index và handler một cách máy móc nhưng không hiểu dữ liệu thật nằm ở đâu, row state thuộc object nào, hoặc tại sao cùng một component ID lại hoạt động ở nhiều WFrame.

## Coding style của library

Ví dụ mặc định dùng `scwin` cho page-scope function và `$p` cho page-aware WebSquare utility. Component ID như `inputUserId`, `grdUser`, DataMap như `dmSearch`, DataList như `dlUser`, Submission như `sbmSearchUser` nhằm làm rõ vai trò ngay từ tên.

Handler nên mỏng: đọc input cần thiết, validate, cập nhật model hoặc gọi một hàm orchestration. Business rule dài không nên bị nhét trực tiếp vào `onclick`. Network call phải có đường đi thành công, lỗi, retry/cancel khi cần và guard chống duplicate submission. Khi code cần đi qua nhiều Scope bằng chuỗi `parent().parent()` hoặc phụ thuộc mạnh vào component ID của page khác, đó là tín hiệu coupling cao cần xem lại boundary.

## First principles: WebSquare giải quyết vấn đề gì?

Ứng dụng enterprise thường có rất nhiều form, grid, popup, validation, request/response mapping và màn hình CRUD. Nếu mỗi màn hình tự làm DOM manipulation, serialization, AJAX, row-state tracking và popup coordination, code nhanh chóng trở nên không đồng nhất. WebSquare cung cấp một runtime và một tập component/data abstraction thống nhất để đội phát triển có thể xây nhiều màn hình nghiệp vụ theo cùng convention.

Lợi ích đó đi kèm một trade-off quan trọng: developer phải hiểu **framework state** chứ không chỉ JavaScript. Một `input1` không đơn thuần là DOM `<input>`, GridView không phải chỉ là HTML table, DataList không chỉ là Array, và một page trong WFrame không phải lúc nào cũng chia sẻ global scope với page cha. Những abstraction này giúp project lớn quản lý được complexity, nhưng cũng tạo ra failure mode riêng nếu developer coi chúng như DOM/JavaScript thuần.

## Cách học bằng project nhỏ

Sau chapter 01–03, hãy tự dựng một màn hình tra cứu gồm điều kiện tìm kiếm, một `DataMap` cho request, một `DataList` cho kết quả, một `Submission` và một GridView. Sau đó thêm chức năng sửa một dòng, theo dõi row status và lưu. Sau chapter 04, đặt màn hình đó trong WFrame và mở một popup chi tiết bằng parameter object. Sau chapter 06, dùng DevTools để giải thích được request nào chạy, scope nào chứa object, dữ liệu thay đổi ở DataList hay chỉ ở UI, và bottleneck nằm ở network, JavaScript hay rendering.

Mục tiêu không phải nhớ càng nhiều API càng tốt. Mục tiêu là nhìn một màn hình WebSquare và có thể mô tả được **state nằm ở đâu, event chạy ở scope nào, dữ liệu đi qua object nào, network call được điều phối ra sao, và evidence nào chứng minh giả thuyết khi có lỗi**.

## Nguồn chuẩn để kiểm chứng API

Library ưu tiên tài liệu chính thức của Inswave Systems: WebSquare5 SP5 Development Guide, SP5 API Reference, SP5 Release Notes và API reference của dòng 6.0/WebSquare AI. Những URL cụ thể thay đổi theo build, vì vậy chapter không hard-code một build làm “chân lý vĩnh viễn”. Với API/property version-sensitive, hãy tra đúng engine build của project.

Các nguồn nền tảng ngoài WebSquare được giữ ở canonical JavaScript/XML/Computer Science docs của repository để tránh duplicate.
