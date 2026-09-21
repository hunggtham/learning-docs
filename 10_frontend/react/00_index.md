# React Master Note — Index

Baseline của bộ tài liệu: React 19.3 (stable ngày 09/09/2026). Cách viết mặc định là Function Component + Hooks; Class Component được giữ lại ở phần Master để đọc và migrate code cũ.

## Thứ tự học

1. `01_react_beginner.md` — nền tảng, JSX, component, props, event, state, render, form, list, composition, styling và mental model cơ bản.
2. `02_react_intermediate.md` — Effect, ref, reducer, context, custom Hook, memoization, portal, Suspense, data fetching, routing, form production, accessibility và testing.
3. `03_react_advanced_senior.md` — concurrency, Actions, `use`, optimistic UI, `useEffectEvent`, Activity, View Transitions, Fragment refs, external store, SSR, hydration, RSC, performance và architecture production.
4. `04_react_master.md` — React Compiler 1.0, server architecture, cache/security, large-scale state, design system, library authoring, migration, observability, performance budget và Master/Senior idioms.

## Phạm vi version: học cả React cũ lẫn React hiện đại

Bộ tài liệu này không được tổ chức theo kiểu “chỉ học React 19.3 rồi ghi vài chú thích React 18”. React 19.3 vẫn là mốc hiện hành để biết cách viết code mới, nhưng các API cũ từ thời React 15, React 16 và React 17 được giữ lại ở đúng phần kiến thức tương ứng để người đọc có thể hiểu codebase legacy.

Khi một API đã lỗi thời, tài liệu vẫn giải thích cú pháp và cách hoạt động của nó nếu API đó đủ phổ biến để còn xuất hiện trong project thực tế. Sau phần giải thích sẽ có trạng thái như `Legacy`, `Deprecated` hoặc `Removed`, version liên quan và cách chuyển sang API hiện đại. Cách trình bày này có chủ đích: bạn học React theo một mental model liên tục, nhưng vẫn đọc được code được viết ở nhiều thế hệ.

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
| React 19.x | Actions, `use`, `useActionState`, `useOptimistic`, ref-as-prop, Context provider shorthand, RSC/server improvements và tiếp tục loại bỏ API legacy. |

## Cách đọc các Version Note trong bộ tài liệu

Bộ note lấy **React 19.3** làm baseline hiện hành, nhưng không giả định rằng mọi project bạn gặp đều đang ở 19.3. Khi một kiến thức thay đổi đáng kể theo version, tài liệu chèn một đoạn `Version Note` ngay sau phần giải thích chính. Quy tắc đọc là: trước tiên học mental model và cách dùng hiện đại; sau đó mới đọc khác biệt version để biết vì sao code cũ có cú pháp khác. Nhờ vậy lịch sử React không chen ngang luồng học.

Các mốc dưới đây đủ để đọc phần lớn code React hiện đại:

| Version | Ý nghĩa đối với người học |
|---|---|
| React 16.8 | Hooks như `useState`, `useEffect` xuất hiện. Đây là mốc quan trọng nhất khi đọc tutorial cũ vì code trước đó thường dựa nhiều vào Class Component. |
| React 17 | Chủ yếu là release chuyển tiếp; giai đoạn này phổ biến modern JSX transform, nên project hiện đại không cần `import React` chỉ để dùng JSX. |
| React 18 | `createRoot`, automatic batching, concurrency primitives như `startTransition`/`useTransition`, `useDeferredValue`, `useId`, streaming SSR và Strict Mode development checks mới trở thành nền tảng của React hiện đại. |
| React 18.3 | Bản cầu nối để nâng cấp lên React 19; hành vi gần React 18.2 nhưng thêm warning cho API/deprecation cần sửa trước React 19. |
| React 19.0 | Actions, `use`, `useActionState`, `useOptimistic`, form Actions, ref-as-prop, Context provider shorthand và nhiều thay đổi SSR/RSC. React 19 cũng yêu cầu modern JSX transform và loại bỏ một số API legacy đã deprecated từ trước. |
| React 19.1 | Chủ yếu tiếp tục cải thiện nhánh server/RSC/prerender và sửa lỗi. Với lộ trình học, có thể xem đây là bước tiến hóa giữa 19.0 và 19.2 thay vì một mental model mới cho beginner. |
| React 19.2 | Thêm `<Activity />`, `useEffectEvent`, `cacheSignal`, React Performance Tracks và các cải tiến server/SSR như Partial Pre-rendering. |
| React 19.3 | Baseline của bộ note này. View Transitions và Fragment refs trở thành stable; React DOM thêm các capability như `browser` và Trusted Types support; RSC tiếp tục được mở rộng. |
| React Compiler 1.0 | Stable từ năm 2025 và **có version độc lập với React core**. Compiler tự động tối ưu nhiều trường hợp memoization, vì vậy không nên hiểu “React 19.3” đồng nghĩa “Compiler 19.3”. |

Một nguyên tắc quan trọng là **major/minor của React không hoàn toàn thay thế patch version**. Đặc biệt với React Server Components, các security fix từng được backport vào nhiều nhánh 19.0.x, 19.1.x và 19.2.x. Trong production phải theo patch/security advisory của framework và React, không chỉ nhìn “19.x”.

## Nguyên tắc học sau audit

Luồng canonical là **render tree → props/state/context → state snapshot/update queue → reconciliation/identity/key → commit → event/Effect → Hooks nâng cao → concurrency/server architecture**. Hooks không được học như danh sách API trước khi hiểu rendering và state ownership.

Với kiến thức qua nhiều version, luôn đọc theo chuỗi **old pattern → new pattern → reason → migration → khi còn gặp old code**. Class Component, lifecycle, HOC, render props và legacy APIs được giữ lại vì vẫn xuất hiện trong code enterprise.

## Cách dùng bộ note

Đây là tài liệu học, không phải cheat sheet. Hãy đọc tuần tự. Sau mỗi level nên tự xây một project nhỏ và giải thích lại được các quyết định về state ownership, render purity, Effect synchronization và component identity trước khi đi tiếp.

5. `05_react_legacy_api_reference.md` — reference riêng cho API legacy React 15–18, dùng khi đọc/migrate project cũ.
