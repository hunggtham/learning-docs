# Frontend Development Knowledge Library

`10_frontend/` là namespace canonical cho Frontend Development. Đây không phải
là một danh sách framework rời rạc; nó là một lộ trình giải thích cách một yêu
cầu đi từ network đến pixel, từ pixel đến interaction, rồi từ interaction đến
state, accessibility, performance, security và deployment.

`CATALOG.md` dùng
[`javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md)
làm **entrypoint canonical** của Frontend. File này là bản đồ cấp domain: nó
giải thích thứ tự học và quan hệ giữa các track, nhưng không thay thế learning
spine JavaScript hay các canonical file của từng track.

## Mental model cấp domain

Frontend nên được đọc như một hệ thống có nhiều boundary nối tiếp và có thể
quay lại invalidation lẫn nhau:

```text
URL / request
→ browser / network
→ HTML parse
→ DOM
→ CSS parse
→ CSSOM
→ style / cascade
→ layout
→ paint
→ composite
→ interaction
→ JavaScript / event loop
→ state / data
→ accessibility
→ performance
→ security
→ deployment
```

Đây là một mental model (mô hình tư duy, 사고 모델), không phải một pipeline
chỉ chạy đúng một lần. Navigation mới, response mới, stylesheet thay đổi,
font load, resize, state update, user input hoặc session transition đều có thể
làm một phần pipeline chạy lại. Vì vậy khi debug, câu hỏi hữu ích không chỉ là
“component nào lỗi?” mà là: request nào tạo ra resource này, tree nào đang được
render, state nào là source of truth, work được schedule ở đâu, và artifact nào
đang thật sự phục vụ browser?

Mối quan hệ giữa các lớp được giữ cố ý như sau:

```text
HTML / CSS / JavaScript
            ↓
      Web Platform
            ↓
   React / WebSquare / ...
```

HTML, CSS và JavaScript không phải “legacy layer” nằm dưới framework. Chúng là
primitive và contract của Web Platform: parser, DOM, CSS cascade/layout,
event/input, browser storage, networking, accessibility tree và security
boundary. React, WebSquare và các framework khác tổ chức các primitive đó thành
application model riêng; chúng không xóa được semantics của browser.

## Cách đọc canonical

Khi cần một điểm bắt đầu duy nhất, mở
[`JavaScript Beginner`](./javascript/javascript_beginner_rebuilt.md). File này
được dùng làm catalog entrypoint vì nó nối syntax với execution model, DOM,
event, Promise, `fetch`, HTTP và module boundary; từ đó người học có thể đi
sang các track platform mà không bắt đầu bằng một abstraction framework.

Đường học đầy đủ nên đi theo các lớp sau:

1. **Nền tảng browser:** đọc HTML và CSS để hiểu document, semantics, DOM,
   cascade, layout và rendering. XML được học như một syntax/data/config
   boundary, không đồng nhất với HTML parser.
2. **Ngôn ngữ và runtime:** đi từ JavaScript Beginner → Intermediate → Senior,
   sau đó dùng Master Supplement để ghép runtime semantics, browser boundary,
   security, performance và compatibility thành một hệ thống.
3. **Type và styling tooling:** học TypeScript sau khi đã phân biệt static
   type với runtime behavior; học SCSS/Tailwind sau CSS để hiểu chúng là
   authoring/build choices, không phải renderer mới.
4. **Application frameworks:** chọn React hoặc WebSquare sau khi đã nắm
   platform primitive. Framework track phải được đọc như cách hiện thực state,
   rendering, composition, integration và lifecycle trên cùng browser.
5. **Production:** dùng coverage audit để kiểm tra identity, state ownership,
   async ordering, accessibility, performance evidence, security boundary,
   build artifact và deployment provenance.

Không bắt buộc mọi người phải đọc mọi file theo một đường thẳng. Tuy vậy,
không nên bỏ qua HTML/CSS/browser chỉ vì dự án dùng React hoặc WebSquare; làm
vậy sẽ biến lỗi parser, cascade, event loop, hydration, focus, cache hoặc
security thành “framework magic”.

## Bản đồ thư mục và owner

| Track | Canonical file bắt đầu | Vai trò trong domain |
|---|---|---|
| [`html/`](./html/) | [`html_01_beginner_to_senior_detailed.md`](./html/html_01_beginner_to_senior_detailed.md) | Document structure, semantics, parser/tree construction, forms, resource hints, accessibility, security và legacy markup. |
| [`css/`](./css/) | [`CSS_Beginner_to_Senior_2026.md`](./css/CSS_Beginner_to_Senior_2026.md) | Cascade, selectors, box/formatting model, responsive layout, animation, rendering và production CSS architecture. |
| [`scss/`](./scss/) | [`SCSS_Beginner_to_Senior_2026.md`](./scss/SCSS_Beginner_to_Senior_2026.md) | Sass như chương trình compile-time tạo CSS; module/configuration, mixin/function, compatibility và Dart Sass evolution. |
| [`tailwind/`](./tailwind/) | [`TailwindCSS_Beginner_to_Senior_2026.md`](./tailwind/TailwindCSS_Beginner_to_Senior_2026.md) | Utility-first authoring, design tokens, build/content detection, variants, responsive UI và production architecture trên nền CSS. |
| [`javascript/`](./javascript/) | [`javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md) | Ngôn ngữ, execution model, browser host, DOM/events, async/event loop, state, performance, security, testing và architecture. Đây là catalog entrypoint. |
| [`react/`](./react/) | [`00_index.md`](./react/00_index.md) | React application model từ render/reconciliation và state identity đến effects, concurrency, SSR/hydration, RSC, compiler, security và production. |
| [`websquare/`](./websquare/) | [`README.md`](./websquare/README.md) | Enterprise UI/runtime track: page/scope, DataCollection, Submission, GridView, lifecycle, reusable architecture, integration, observability, security và migration. |
| [`xml/`](./xml/) | [`xml_01_beginner_detailed.md`](./xml/xml_01_beginner_detailed.md) | XML syntax, tree/data model, namespaces, validation, transformation, security và các boundary nơi XML gặp HTML/WebSquare/backend. |

Các file `Master`, `Supplement`, `Legacy` hoặc `GLOSSARY_AND_COVERAGE` mở
rộng một owner đã có. Chúng không tạo ra một learning path cạnh tranh với
entrypoint của domain. Ví dụ, `react/00_index.md` là index của React track,
không phải entrypoint của toàn Frontend.

## Boundary với domain khác

Frontend cần dùng mental model từ các domain lân cận nhưng không duplicate
toàn bộ nội dung của chúng:

- [Computer Science](../computer_science/README.md) sở hữu nền tảng network,
  operating systems, security, databases, algorithms và software engineering.
- [Backend Development](../10_backend/README.md) sở hữu server-side request,
  API contract, identity, persistence, transaction, messaging và backend
  observability. Frontend chỉ giữ client contract, loading/error state,
  cancellation, stale result và trust-boundary implications.
- [DevOps / Platform Engineering](../devops_platform_engineering/README.md)
  sở hữu CI/CD, artifact delivery, infrastructure và operating platform.
  Frontend giữ build graph, bundle, cache, source map và deployment evidence ở
  mức cần thiết để hiểu artifact chạy trong browser.
- [Native Mobile Development](../11_native/00_INDEX.md) là boundary khi một
  WebView/hybrid app đưa browser content vào native lifecycle. WebSquare có
  track riêng cho bridge nhưng không biến native API thành browser API.

## Nguyên tắc chống duplicate và framework-first

Một concept nên có một owner canonical. Nếu câu hỏi là “DOM event được schedule
như thế nào?”, owner là JavaScript/browser platform; React hoặc WebSquare chỉ
giải thích framework thêm abstraction nào và contract nào cần giữ. Nếu câu hỏi
là “server xác thực quyền Save ra sao?”, owner là Backend/security; frontend
chỉ mô tả cách hiển thị capability, xử lý `401/403`, stale session và không tin
UI validation như authorization.

Khi framework có behavior riêng, tài liệu phải tách ba lớp:

1. browser/platform semantics;
2. framework semantics và state ownership;
3. application contract, artifact và production evidence.

Tách lớp như vậy giúp đọc code legacy, migrate framework và kiểm tra lỗi production
mà không cần học lại toàn bộ domain từ đầu.

## Case studies và evidence lab

[`90_case_studies/README.md`](./90_case_studies/README.md) là lớp integration cấp
domain. Nó không tạo owner theory mới mà buộc người học nối các owner hiện có
thành causal trace có thể đo và review.

Bắt đầu với:

- [`Request → Pixel → Interaction Trace`](./90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md) để trace một màn hình từ document request, parser, DOM/CSSOM và rendering tới async state, security boundary và deployed artifact.
- [`Rendering Performance Measurement Lab`](./90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md) để đo scripting/style/layout/paint/composite, layout invalidation và framework/browser rendering bằng baseline → trace → hypothesis → one change → re-measure.

Hai case này là evidence path cho các gap cấp domain mà theory riêng lẻ khó kiểm
tra: người đọc phải chứng minh browser đang làm work gì thay vì suy nguyên nhân
từ tên CSS property hoặc framework abstraction.

## Kiểm tra coverage

[`COVERAGE_AUDIT.md`](./COVERAGE_AUDIT.md) là checklist cấp domain. Audit không
chỉ đếm số file; nó kiểm tra mỗi stage có owner, boundary, invariant, failure
mode, test/evidence và đường dẫn học rõ ràng hay chưa. Khi thêm file mới, ưu
tiên bổ sung vào canonical owner hoặc audit trước khi mở một title framework
mới.
