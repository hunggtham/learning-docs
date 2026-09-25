# Frontend Coverage Audit

File này kiểm tra `10_frontend/` theo mental model cấp domain, không chỉ theo
số lượng file. Mục tiêu là phát hiện nơi người học có thể biết syntax nhưng
chưa hiểu boundary, ownership, ordering, failure, evidence hoặc deployment
artifact.

`CATALOG.md` vẫn dùng
[`javascript/javascript_beginner_rebuilt.md`](./javascript/javascript_beginner_rebuilt.md)
làm entrypoint. [`README.md`](./README.md) là map cấp domain và giải thích vì
sao entrypoint là JavaScript track trong khi learning model bắt đầu từ browser
request và Web Platform.

## Cách đọc trạng thái

- **Covered** — có canonical owner và có đủ explanation để đi từ mechanism đến
  production implication.
- **Deep** — canonical owner đã có, đồng thời có supplement/master/framework
  material hoặc case/lab để reasoning ở boundary khó.
- **Distributed** — coverage nằm ở nhiều track; người học phải theo cross-link,
  nhưng không phải thiếu nội dung.
- **Partial** — đã có nội dung đáng kể nhưng map cấp domain hoặc một invariant /
  evidence path còn mỏng; đây là candidate cho vòng update sau.
- **Intentional boundary** — không duplicate ở Frontend vì domain khác là owner;
  Frontend chỉ giữ contract cần để tích hợp.

## 1. Audit theo mental model

| Stage | Owner chính | Coverage | Bằng chứng / câu hỏi kiểm tra |
|---|---|---|---|
| URL / request | JavaScript + HTML Master; cross-link Computer Science/Backend | Deep | Có phân biệt URL, navigation, resource request, `fetch`, cache, CORS và API contract không? Theory được nối end-to-end bằng `90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md`. |
| Browser / network | JavaScript Senior/Master; HTML Master; WebSquare 15/21 | Deep | Có nhìn browser là host environment thay vì chỉ ECMAScript không? Có trace timeout, cancellation, retry, cache, cross-origin và stale response theo timeline không? |
| HTML parse | HTML Beginner + Master | Deep | Có phân biệt source markup, parser repair, DOM tree, optional end tag, raw text/RCDATA và SSR parser-stable markup không? |
| DOM | HTML + JavaScript Beginner/Intermediate | Deep | Có phân biệt DOM node, component object, attribute/live property, logical identity và physical DOM representation không? |
| CSS parse / CSSOM | CSS Beginner + Master | Deep | Có giải thích declaration → cascade → specified/computed/used/actual value và formatting tree khác DOM tree không? |
| Style / cascade | CSS Beginner + Master; SCSS/Tailwind authoring | Deep | Có reasoning về specificity, layers, inheritance, scope proximity, `!important`, token và source order thay vì tăng selector bừa không? |
| Layout | CSS Beginner + Master + Rendering Measurement Lab | Deep | Có hiểu normal flow, BFC/IFC, flex/grid, intrinsic sizing, fragmentation, container query, invalidation cost, forced synchronous layout và read/write ordering không? |
| Paint | CSS Master; JavaScript Senior; Rendering Measurement Lab | Deep | Có phân biệt style/layout/paint/composite và chứng minh repaint bằng trace/profile thay vì suy từ property folklore không? Có xem invalidated area, frequency và visual complexity không? |
| Composite | CSS Master; JavaScript Senior; Rendering Measurement Lab | Deep | Có hiểu compositing/layer là optimization có memory/resource cost, không phải `transform`/GPU = miễn phí? Có baseline → trace → change → re-measure không? |
| Interaction | HTML + CSS + JavaScript Beginner/Intermediate; React/WebSquare | Deep | Có phân biệt semantic HTML, keyboard/focus/pointer/input, bubbling/capturing/delegation, form state và framework event abstraction không? |
| JavaScript / event loop | JavaScript Beginner → Intermediate → Senior → Master | Deep | Có trace stack, task, microtask, render opportunity, timer, `requestAnimationFrame`, worker, stream, cancellation và reentrancy theo timeline không? |
| State / data | JavaScript Intermediate/Senior; React; WebSquare | Deep | Có xác định source of truth, state machine, derived state, DTO boundary, stale result, optimistic update, identity và ownership của async operation không? |
| Accessibility | HTML Master; CSS; React; WebSquare 09 | Deep | Có xem accessibility tree/semantic contract là correctness, không phải polish? Có kiểm tra accessible name, focus, keyboard, live region, `aria-*`, form error và screen-reader behavior không? |
| Performance | JavaScript Senior; CSS Master; React; WebSquare 24; `90_case_studies/` | Deep | Có đo network, main-thread, layout/paint, bundle, memory, large DOM, formatter/render amplification, RUM/profile và production budget thay vì tối ưu theo cảm giác không? |
| Security | HTML Master; JavaScript Senior/Master; React/WebSquare; Backend boundary | Deep | Có trace untrusted input → parser/DOM/URL/HTML sink, XSS, CSP/Trusted Types, CSRF, token, `postMessage`, bridge, supply chain và server authorization không? |
| Deployment | JavaScript Senior/Master; WebSquare 12/22; DevOps boundary; Request→Pixel case | Deep | Có phân biệt source, build artifact, bundle/source map, config, cache, deployment identity, rollback và browser đang chạy artifact nào không? Case end-to-end buộc nối commit/build/hash/config với resource browser thực sự nhận. |

### Kết luận pipeline

Pipeline hiện có coverage mạnh từ request tới deployment. Gap trước đây ở
paint/composite đã được đóng bằng một evidence path riêng: theory vẫn thuộc CSS
Master và JavaScript Senior, còn
[`90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md`](./90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md)
buộc người học tạo baseline, record trace, phân loại scripting/style/layout/
paint/composite, xác định invalidation rồi re-measure sau một thay đổi duy nhất.

Tương tự, [`Request → Pixel → Interaction Trace`](./90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md)
đã nối navigation/resource discovery, parser, DOM/CSSOM, event loop, state,
accessibility, security và source→build→cache→deployed artifact thành một case
duy nhất. Vì vậy hai P1 gap này không còn cần thêm theory file; vòng sau chỉ nên
mở rộng khi có capability/evidence mới.

## 2. Audit theo track

| Track | Learning spine | Đã cover tốt | Boundary cần giữ |
|---|---|---|---|
| HTML | Beginner → Master Implementation | Semantics, parser, forms, DOM relation, resources, a11y, security, legacy và SSR | Không biến HTML thành XML; không dùng ARIA thay native semantics khi native element đã đủ. |
| CSS | Beginner → Senior → Master Supplement | Cascade, selectors, box/formatting, sizing, responsive, animation, rendering và modern CSS | CSS authoring không đồng nghĩa rendering; SCSS/Tailwind không thay CSS mental model. |
| SCSS | Beginner → Senior → Master Supplement | Compile-time language, module/configuration, mixin/function, selector algebra, colors và Dart Sass evolution | Output canonical vẫn là CSS; runtime token nên tách khỏi compile-time config. |
| Tailwind | Beginner → Senior → Master Supplement | Utility-first, v4 build model, tokens, variants, responsive, component boundary và production governance | Utility class không loại bỏ cascade, accessibility, design semantics hoặc performance review. |
| JavaScript | Beginner → Intermediate → Senior → Master Supplement | Language/runtime, browser host, DOM/event, async, state, memory, concurrency, performance, security, testing và architecture | Đây là catalog entrypoint; không để React/WebSquare thay thế JavaScript semantics. |
| TypeScript | Foundations → Type System → Tooling/Modules → Senior Production → Version/Migration | Static/runtime boundary, structural typing, generics, compiler/tooling, declarations, validation và migration | Type annotation không phải runtime validation và không tạo authorization. |
| React | Beginner → Intermediate → Advanced/Senior → Master + Legacy Reference | Render/reconciliation, identity, state/effects, concurrency, SSR/hydration/RSC, compiler, performance, security và migration | React là consumer của Web Platform; debug DOM/CSS/event/network trước khi gán lỗi cho React. |
| WebSquare | 01 → 24 + glossary/coverage | Runtime/page/scope, DataCollection/Submission, Grid, reusable architecture, lifecycle, test, build, auth, integration, observability, workflow và profiling | Framework contract có thể build/version-dependent; XML source, runtime engine và W-Pack artifact phải tách. |
| XML | Beginner → Intermediate → Senior → Master Supplement | Syntax/tree, namespace, validation, transformation, security và integration | XML là data/config/document boundary; không dùng XML parser assumptions để giải thích HTML parser. |
| Case/Lab | Request→Pixel trace → Rendering Measurement Lab | Cross-owner causal trace, production evidence, layout/paint/composite profiling, artifact identity | Không biến case thành owner theory mới; framework-specific profiler chỉ bổ sung browser/platform evidence. |

## 3. Cross-cutting invariant audit

Người học đạt coverage thực dụng khi có thể trả lời các câu hỏi sau mà không
đổi câu trả lời theo framework:

### Identity và ownership

- Resource nào được định danh bởi URL/cache key/build ID; entity nào được định
  danh bởi business key thay vì array index hoặc DOM position?
- Component, DOM node, screen instance, request, session, workflow và artifact
  có lifetime nào; ai tạo, ai sở hữu, ai dispose?
- State canonical nằm ở đâu; state nào chỉ là derived view, cache, optimistic
  projection hoặc UI affordance?

### Ordering và async

- Một event đi qua capture → target → bubble hay framework dispatch nào?
- Promise continuation, timer, rendering opportunity, user input và network
  response có thể xen kẽ như thế nào?
- Khi response cũ về sau intent mới, operation bị cancel, session đổi hoặc
  screen bị dispose, invariant nào ngăn stale update?

### Semantics và accessibility

- Native HTML element đã biểu diễn đúng semantics chưa, hay code đang thêm ARIA
  để che markup sai?
- Focus, keyboard, accessible name, error announcement và reduced motion có
  được xem là public behavior cần regression test không?
- React/WebSquare abstraction có giữ được semantics khi render conditionally,
  lazy, portal, popup, WFrame hoặc hydration không?

### Performance và evidence

- Độ trễ được chia thành DNS/connect/response/parse/script/style/layout/paint/
  interaction hay chỉ gọi chung là “frontend chậm”?
- Work có bị khuếch đại theo rows × cells × listeners × renders không?
- Kết luận tối ưu dựa trên trace/profile/metric nào; có guard trong test hoặc
  release gate không?
- Có phân biệt framework render/reconciliation với browser rendering không?
- Có ghi scenario, environment, build ID và run variance trước khi so before/after không?

### Security và trust boundary

- Dữ liệu đến từ URL, HTML, storage, postMessage, iframe, WebView bridge,
  backend hay user input được coi là untrusted ở đâu?
- Validation/encoding/sanitization khác nhau thế nào; vì sao UI validation
  không thay server authorization?
- CSP, cookie/token, CSRF, CORS và dependency/build supply chain thuộc boundary
  nào; evidence nào chứng minh policy đang active?

### Artifact và deployment

- Source markup/code, generated CSS/JS, bundle, source map, config, cache và
  deployed resource liên hệ với nhau ra sao?
- Khi chỉ production lỗi, có biết build ID, engine/browser, feature flag,
  config và cache version để tái tạo không?
- Rollback có trả đúng artifact/config/schema contract hay chỉ quay lại Git
  branch?

## 4. Framework placement audit

Framework track được xem là đạt khi mỗi chương trả lời được ba câu hỏi:

1. Browser primitive nào đang được dùng (DOM, CSS, event, history, fetch,
   storage, accessibility hoặc Web Worker)?
2. Framework thêm state/lifecycle/rendering abstraction nào, và abstraction đó
   sở hữu identity, subscription, cleanup, error và scheduling ra sao?
3. Application phải kiểm chứng contract nào bằng test, telemetry và artifact
   evidence?

React và WebSquare đều đã có canonical index riêng và đều cross-link về
JavaScript/XML/platform. Không coi framework README là domain entrypoint là
điều kiện bắt buộc để tránh “framework-first drift”.

## 5. Gaps và ưu tiên vòng audit tiếp theo

Backlog hiện chuyển từ thiếu foundation sang **integration/compatibility và
regression evidence**. Không nên mở thêm framework chapter chỉ để tăng breadth.

| Priority | Cơ hội cải thiện | Trạng thái / hướng xử lý |
|---|---|---|
| P0 | Giữ một canonical domain map và một catalog entrypoint duy nhất | Đã xử lý bằng `README.md`; giữ catalog entrypoint là JavaScript Beginner. |
| P1 | Nối URL/navigation/resource request với DOM/CSS/render trace trong một browser case | **Đã xử lý** bằng `90_case_studies/00_REQUEST_TO_PIXEL_AND_INTERACTION_TRACE.md`. |
| P1 | Làm rõ paint/composite evidence và layout invalidation bằng profile production-like | **Đã xử lý** bằng `90_case_studies/01_RENDERING_PERFORMANCE_MEASUREMENT_LAB.md`; theory owner vẫn là CSS/JavaScript. |
| P1 | Chuẩn hóa source → build → cache → deployed artifact vocabulary giữa React/WebSquare/vanilla | **Đã có canonical chain** trong Request→Pixel case; có thể bổ sung glossary nhỏ chỉ khi track-specific vocabulary lệch nhau. |
| P2 | Tạo capability matrix cho browser, WebView, React và WebSquare | Chỉ thêm khi có migration/compatibility use case thực; matrix phải có version/evidence, không phải feature checklist chung. |
| P2 | Bổ sung end-to-end accessibility regression example xuyên native HTML và framework | Đây là candidate depth tiếp theo nếu cần; đặt case ở layer integration và cross-link owner, không duplicate a11y theory. |
| P2 | Tạo one-screen production incident drill | Candidate cao: artifact mismatch + stale request + performance + accessibility/security checks trong một incident, nếu muốn luyện vận hành thay vì thêm theory. |

## 6. Exit criteria cho Frontend domain

Coverage cấp domain được xem là đủ mạnh khi người học có thể:

1. vẽ request → parser → tree → style → layout → paint → composite → event →
   state → deployment timeline cho một màn hình thật;
2. chỉ ra canonical owner của một concept và không giải thích browser behavior
   bằng framework folklore;
3. đặt tên identity, owner, lifetime, ordering và invariant của async state;
4. kiểm tra accessibility như semantics và public behavior;
5. đo performance bằng evidence, phân biệt client work với network/server work;
6. trace untrusted data qua HTML/DOM/URL/message/bridge/backend boundary;
7. nối source commit với generated artifact, config, cache, deployed resource và
   rollback plan;
8. đọc code legacy, chọn migration boundary và giữ nguyên invariant thay vì
   rewrite theo trend;
9. tạo performance report có scenario, baseline, trace observation, hypothesis,
   one-change experiment, variance và regression check.

Hiện domain đã có canonical owner cho toàn bộ các exit criteria trên. Nội dung
mới chỉ nên được thêm khi tạo **new capability, migration evidence, production
incident drill hoặc regression artifact**, không nên mở rộng chỉ vì xuất hiện
một framework hay CSS API mới.
