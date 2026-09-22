# React Master Note — Index

Baseline của bộ tài liệu: React 19.3 (stable ngày 09/09/2026). Cách viết mặc định là Function Component + Hooks; Class Component được giữ lại để đọc và migrate code cũ thay vì bị xóa khỏi lộ trình.

React không đứng một mình. Nếu chưa chắc về closure, object identity, Promise/event loop, module hoặc browser runtime, nên học [JavaScript Beginner](../javascript/javascript_beginner_rebuilt.md) và [JavaScript Intermediate](../javascript/javascript_intermediate.md) trước hoặc song song. Nếu project dùng TypeScript, học type system ở [TypeScript canonical track](../javascript/typescript_00_index.md). React docs chỉ giải thích type ở nơi type làm thay đổi component/API reasoning; structural typing, narrowing, generic, declaration, module resolution và runtime validation được giữ ở TypeScript canonical source để tránh duplicate.

## Thứ tự học canonical

1. [01 — React Beginner](01_react_beginner.md) — nền tảng, JSX, component, props, event, state, render, form, list, composition, styling và mental model cơ bản.
2. [02 — React Intermediate](02_react_intermediate.md) — Effect, ref, reducer, context, custom Hook, memoization, portal, Suspense, data fetching, routing, form production, accessibility và testing.
3. [03 — React Advanced / Senior](03_react_advanced_senior.md) — concurrency, Actions, `use`, optimistic UI, `useEffectEvent`, Activity, View Transitions, Fragment refs, external store, SSR, hydration, RSC, performance, security và architecture production.
4. [04 — React Master](04_react_master.md) — React Compiler 1.0, server architecture, cache/security, large-scale state, design system, library authoring, migration, observability, performance budget và Master/Senior idioms.
5. [05 — React Legacy API Reference](05_react_legacy_api_reference.md) — reference riêng cho React 15–18 và các API/pattern cũ, dùng khi đọc hoặc migrate project enterprise.

Luồng reasoning nên đi theo **render tree → props/state/context → state snapshot/update queue → reconciliation/identity/key → commit → event/Effect → concurrency/Suspense → server/client boundary → production evidence**. Hooks không được học như một danh sách API trước khi hiểu rendering và state ownership.

## Phạm vi version: học cả React cũ lẫn React hiện đại

Bộ tài liệu này không được tổ chức theo kiểu “chỉ học React 19.3 rồi ghi vài chú thích React 18”. React 19.3 vẫn là mốc hiện hành để biết cách viết code mới, nhưng các API cũ từ thời React 15, React 16 và React 17 được giữ lại ở đúng phần kiến thức tương ứng để người đọc có thể hiểu codebase legacy.

Khi một API đã lỗi thời, tài liệu vẫn giải thích cú pháp và cách hoạt động của nó nếu API đó đủ phổ biến để còn xuất hiện trong project thực tế. Sau phần giải thích sẽ có trạng thái như `Legacy`, `Deprecated` hoặc `Removed`, version liên quan và cách chuyển sang API hiện đại. Cách trình bày này có chủ đích: học React theo một mental model liên tục, nhưng vẫn đọc được code được viết ở nhiều thế hệ.

### Bản đồ lịch sử React nên nhớ

| Thời kỳ | Những thứ thường gặp trong code |
|---|---|
| React 0.x–14 | `React.createClass`, mixins, JSX transform cũ, string refs và nhiều API đời đầu. Đây chủ yếu là kiến thức đọc legacy. |
| React 15.x | Class Component đã phổ biến; `React.createClass` và `React.PropTypes` còn xuất hiện nhiều. React 15.5 tách `createClass` và `PropTypes` ra package riêng và bắt đầu deprecate cách cũ. |
| React 16.0–16.2 | Fiber trở thành renderer mới; Error Boundaries, portals và Fragment làm component composition linh hoạt hơn. |
| React 16.3–16.6 | New Context API, `createRef`, `forwardRef`, `StrictMode`, `memo`, `lazy`, Suspense cho code splitting, `contextType` và lifecycle mới xuất hiện. |
| React 16.8–16.14 | Hooks xuất hiện từ 16.8 và dần trở thành cách viết chính. Các lifecycle nguy hiểm được đổi tên `UNSAFE_*`; nhiều API legacy bắt đầu rời khỏi hướng học mới. |
| React 17 | Release chuyển tiếp. Modern JSX transform và gradual upgrade là các điểm quan trọng; event system cũng thay đổi so với các version trước. |
| React 18 | `createRoot`, automatic batching, concurrent foundations, transitions, `useDeferredValue`, `useId`, `useSyncExternalStore`, `useInsertionEffect`, streaming SSR. |
| React 19.x | Actions, `use`, `useActionState`, `useOptimistic`, ref-as-prop, Context provider shorthand, RSC/server improvements và tiếp tục loại bỏ API legacy; các minor 19.2/19.3 tiếp tục thêm public capability nên phải kiểm tra minimum minor version. |

## Cách đọc các Version Note trong bộ tài liệu

Bộ note lấy **React 19.3** làm baseline hiện hành, nhưng không giả định rằng mọi project đều đang ở 19.3. Khi một kiến thức thay đổi đáng kể theo version, tài liệu chèn `Version Note` sau phần giải thích chính. Quy tắc đọc là: trước tiên hiểu mental model và cách dùng hiện đại; sau đó mới đọc khác biệt version để biết vì sao code cũ có cú pháp khác. Nhờ vậy lịch sử React không chen ngang luồng học.

Các mốc dưới đây đủ để đọc phần lớn code React hiện đại:

| Version | Ý nghĩa đối với người học |
|---|---|
| React 16.8 | Hooks như `useState`, `useEffect` xuất hiện. Đây là mốc quan trọng nhất khi đọc tutorial cũ vì code trước đó thường dựa nhiều vào Class Component. |
| React 17 | Chủ yếu là release chuyển tiếp; giai đoạn này phổ biến modern JSX transform, nên project hiện đại không cần `import React` chỉ để dùng JSX. |
| React 18 | `createRoot`, automatic batching, concurrency primitives như `startTransition`/`useTransition`, `useDeferredValue`, `useId`, streaming SSR và Strict Mode development checks mới trở thành nền tảng của React hiện đại. |
| React 18.3 | Bản cầu nối để nâng cấp lên React 19; hành vi gần React 18.2 nhưng thêm warning cho API/deprecation cần sửa trước React 19. |
| React 19.0 | Actions, `use`, `useActionState`, `useOptimistic`, form Actions, ref-as-prop, Context provider shorthand và nhiều thay đổi SSR/RSC. React 19 cũng yêu cầu modern JSX transform và loại bỏ một số API legacy đã deprecated từ trước. |
| React 19.1 | Chủ yếu tiếp tục cải thiện nhánh server/RSC/prerender và sửa lỗi. Với lộ trình học, có thể xem đây là bước tiến hóa giữa 19.0 và 19.2 thay vì một mental model mới cho beginner. |
| React 19.2 | Thêm `<Activity />`, `useEffectEvent`, `cacheSignal`, React Performance Tracks và Partial Pre-rendering/server improvements. |
| React 19.3 | Baseline của bộ note này. `<ViewTransition>` và Fragment refs trở thành stable; React DOM thêm `browser()` và Trusted Types support; RSC cho phép render Context trực tiếp trong Server Components theo boundary phù hợp. |
| React Compiler 1.0 | Stable từ năm 2025 và **có version độc lập với React core**. Compiler tự động tối ưu nhiều trường hợp memoization, vì vậy không nên hiểu “React 19.3” đồng nghĩa “Compiler 19.3”. |

Một nguyên tắc quan trọng là **major/minor của React không hoàn toàn thay thế patch version**. Đặc biệt với React Server Components, security fix từng được backport vào nhiều nhánh 19.0.x, 19.1.x và 19.2.x. Trong production phải theo patch/security advisory của framework và React, không chỉ nhìn “19.x”.

## Conceptual boundary với domain khác

React chịu trách nhiệm chính cho component/rendering model, state/effect/ref/context và các React-specific concurrency/server primitives. JavaScript canonical docs chịu trách nhiệm cho closure, promise, event loop, prototype, object identity và browser runtime. TypeScript canonical docs chịu trách nhiệm cho static type model. CSS domain chịu trách nhiệm layout/paint/styling mechanics. Computer Science và backend/server docs chịu trách nhiệm cho scheduling tổng quát, network/cache/database/security principles ở mức không phụ thuộc React.

Khi một chapter React cần những kiến thức đó, tài liệu giải thích đủ để người đọc tiếp tục reasoning tại chỗ, nhưng không copy toàn bộ domain khác. Cách này giữ React là canonical source cho **React semantics**, còn cross-domain knowledge được link về nơi sở hữu khái niệm.

## Coverage audit — 22/09/2026

Canonical track hiện đã phủ bốn lớp liên tục. Beginner xây mental model declarative rendering, state snapshot, update queue, identity/key và immutable update. Intermediate đào sâu Effect như synchronization process, closure/dependency, reducer/context/custom Hook, refs, Error Boundary, Suspense cơ bản, server-state ownership, routing/form/testing. Advanced/Senior nối các invariant đó với concurrent rendering, Actions, external stores, SSR/hydration/RSC, security, accessibility và performance evidence. Master chuyển sang compiler/runtime boundary, server architecture, library/design-system authoring, large-scale migration, observability và production governance.

Audit mới nhất đã đào sâu những capability React 19.2/19.3 trước đây chỉ được nhắc tên: `useEffectEvent` được đặt trong reactive-vs-event semantics; `<Activity />` được giải thích theo state preservation, Effect lifecycle, priority và memory trade-off; `cacheSignal` được nối với resource-lifetime cancellation trong RSC; React Performance Tracks được dùng như production evidence; `<ViewTransition>` được nối với Transition semantics; Fragment refs được giải thích theo capability thay vì “ref cho nhiều node”; `browser()` được đặt trong SSR/Suspense/hydration boundary; Trusted Types được đặt đúng vị trí defense-in-depth thay vì hiểu thành sanitizer; RSC Context 19.3 được giải thích theo dependency/client boundary.

Những phần cố ý **không duplicate** gồm implementation chi tiết của JavaScript runtime, TypeScript type system, router/framework cache semantics cụ thể, CSS rendering engine và backend authorization/storage. Khi cần học sâu các phần đó, dùng canonical domain tương ứng thay vì mở React chapter mới.

Coverage được coi là đạt mục tiêu khi người đọc có thể tự trả lời bằng reasoning, không chỉ nhớ API: state thuộc identity nào; update được schedule/commit ra sao; Effect đang synchronize resource gì; khi nào closure phải reactive và khi nào logic là Effect Event; tại sao external store cần snapshot contract; Suspense/Error/Activity/ViewTransition giải quyết boundary nào; SSR, hydration và RSC khác nhau ở đâu; browser-only subtree nên model thế nào; server/client boundary ảnh hưởng bundle và secret ra sao; performance bottleneck nằm ở render, commit, browser hay I/O; và evidence nào chứng minh giả thuyết production.

## Nguyên tắc học sau audit

Với kiến thức qua nhiều version, luôn đọc theo chuỗi **old pattern → new pattern → reason → migration → khi còn gặp old code**. Class Component, lifecycle, HOC, render props và legacy APIs được giữ lại vì vẫn xuất hiện trong code enterprise.

Không tối ưu theo nghi thức. `memo`, `useMemo`, `useCallback`, transitions, Compiler hay virtualization chỉ có giá trị khi đúng bottleneck/contract. Không dùng Effect để chữa state model sai. Không dùng client UI để thay authorization server. Không coi framework-specific router/cache behavior là React core.

## Cách dùng bộ note

Đây là tài liệu học, không phải cheat sheet. Hãy đọc tuần tự. Sau mỗi level nên tự xây một project nhỏ và giải thích lại được các quyết định về state ownership, render purity, Effect synchronization và component identity trước khi đi tiếp.

Ở Advanced/Senior trở lên, project luyện tập nên có ít nhất một external subscription, một async mutation có failure semantics, một SSR/hydration boundary hoặc framework data boundary, profiling bằng production-like build và một quyết định kiến trúc được ghi lại theo “problem → invariant → mechanism → trade-off → evidence”.

## Nguồn chuẩn để kiểm chứng version

Ưu tiên React Learn/API Reference và React Blog release notes. Với React Compiler, đọc documentation/release tương ứng của Compiler vì lifecycle version độc lập React core. Với RSC/framework integration, đọc support matrix và security advisory của framework đang dùng; không suy ra compatibility chỉ từ version `react`.
