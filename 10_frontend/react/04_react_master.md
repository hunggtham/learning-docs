# React Master Note — Master

> Mục tiêu của level Master không phải “thuộc mọi API”, mà là hiểu sâu invariants của React, compiler/runtime boundary, server architecture, library design, migration, observability, security và cách ra quyết định khi ecosystem tiếp tục thay đổi.

## 1. Version map React 15 → 19.3 và cách đọc version đúng

Tại thời điểm biên soạn, React 19.3 là stable hiện hành. Đây là chi tiết quan trọng vì React 19.x đã bổ sung feature qua minor release chứ không chỉ sửa bug. Vì vậy câu “project dùng React 19” chưa đủ để suy ra project có thể dùng API nào.

Khi review một codebase, hãy xác định đồng thời:

```text
React core version
React DOM version
framework version
bundler/compiler version
library peer dependency
runtime target
```

Một package import API chỉ có từ React 19.3 nhưng khai peer dependency `react >=19.0` có thể làm consumer 19.0 crash. Library author phải encode minimum version thật sự cần.

React docs hiện hành bám latest, trong khi enterprise codebase có thể vẫn ở React 18. Kỹ năng quan trọng là đọc API theo version thay vì ghi nhớ tuyệt đối.

### Version matrix dùng khi review architecture

Ở cấp Master, nên phân biệt ba loại version: **React runtime**, **React DOM/server packages**, và **tooling/framework**. Một feature chỉ thật sự dùng được khi cả ba lớp tương thích.

| Feature/capability | Minimum mốc nên nhớ | Ghi chú kiến trúc |
|---|---|---|
| Hooks | 16.8 | Function Component trở thành hướng chính cho stateful UI. |
| Modern root/concurrency foundation | 18 | `createRoot` là prerequisite thực tế cho semantics React 18 hiện đại. |
| Actions/`use`/`useActionState`/`useOptimistic` | 19.0 | Full-stack semantics còn phụ thuộc framework/server integration. |
| ref-as-prop và Context provider shorthand | 19.0 | Tác động trực tiếp đến component/library API compatibility. |
| `<Activity />`, `useEffectEvent`, `cacheSignal` | 19.2 | Không có trong 19.0/19.1. |
| Stable View Transitions, Fragment refs | 19.3 | Feature mới nhất trong baseline này; cần kiểm tra browser/framework support riêng. |
| React Compiler stable | Compiler 1.0 | Tooling version độc lập React; không suy ra từ `react` package version. |

Một nguyên tắc tốt khi review PR là yêu cầu developer nói rõ “API này xuất hiện từ version nào và package nào cung cấp”, thay vì chỉ nói “React hỗ trợ”.

## 1A. Timeline chi tiết React 15 → 19 để định vị API

### React 15.x

React 15 là thời kỳ nhiều codebase enterprise cũ bắt đầu ổn định. `React.createClass`, ES6 classes, `React.PropTypes`, lifecycle class và string refs đều có thể xuất hiện. React 15.5 là cột mốc migration lớn: `React.createClass` và `React.PropTypes` bị deprecate khỏi core, lần lượt chuyển hướng sang `create-react-class` và `prop-types`.

### React 16.0

React 16 đưa renderer Fiber mới vào production. Với application developer, các thay đổi dễ nhìn thấy gồm Error Boundaries, portals và khả năng render nhiều dạng React node linh hoạt hơn. Đây là nền tảng cho các cải tiến async/concurrent sau này.

### React 16.2

Fragment trở thành abstraction chính thức để group children mà không thêm DOM wrapper:

```jsx
<React.Fragment>
  <td>A</td>
  <td>B</td>
</React.Fragment>
```

Short syntax `<>...</>` trở thành cú pháp quen thuộc về sau.

### React 16.3

Đây là minor rất quan trọng đối với code legacy: new Context API (`createContext`), `createRef`, `forwardRef` và `StrictMode` xuất hiện. String refs bắt đầu đi vào deprecation path. Đây cũng là giai đoạn React giới thiệu lifecycle mới để thay assumptions từ `componentWill*`.

### React 16.6

`React.memo`, `React.lazy`, Suspense cho code splitting, `contextType` và `getDerivedStateFromError` xuất hiện. `findDOMNode` và legacy context bước sâu hơn vào deprecation path.

### React 16.8

Hooks xuất hiện: `useState`, `useEffect`, `useContext`, `useReducer`, `useMemo`, `useCallback`, `useRef`, `useImperativeHandle`, `useLayoutEffect`, `useDebugValue`. Đây là mốc lớn nhất khi so code class với code function hiện đại.

### React 16.9

Các lifecycle nguy hiểm được nhấn mạnh bằng tên `UNSAFE_*`; Profiler/tooling trưởng thành hơn. Module-pattern factory component cũng đi vào deprecation path.

### React 16.13–16.14

`React.createFactory` bị deprecate ở 16.13. React 16.14 chủ yếu là compatibility bridge trước React 17.

### React 17

React 17 là release chuyển tiếp hơn là một release feature-heavy. Gradual upgrade và thay đổi event system là các điểm quan trọng. Modern JSX transform xuất hiện trong cùng thời kỳ và cho phép JSX không bắt buộc `import React` chỉ để transform. Web SyntheticEvent pooling kiểu cũ không còn, nên `event.persist()` không còn cần cho mục đích chống pooling.

### React 18

Modern root (`createRoot`, `hydrateRoot`), automatic batching, transitions, `useDeferredValue`, `useId`, `useSyncExternalStore`, `useInsertionEffect` và streaming SSR đánh dấu thế hệ concurrent foundations. `ReactDOM.render`, `hydrate` và `unmountComponentAtNode` bị deprecate.

### React 18.3

Behavior chủ yếu tương thích 18.2 nhưng thêm warning để chuẩn bị React 19. Đây là version hợp lý làm bước migration trung gian.

### React 19.0

Actions, `use`, `useActionState`, `useOptimistic`, form Actions, ref-as-prop và Context provider shorthand xuất hiện. React 19 cũng remove hàng loạt deprecated APIs: legacy root APIs, string refs, legacy Context, `findDOMNode`, `createFactory`, module pattern factories và support cũ liên quan Function Component `propTypes/defaultProps`.

### React 19.1–19.3

Các minor này tiếp tục mở rộng server/RSC/prerender, rồi thêm `Activity`, `useEffectEvent`, performance/server capabilities và đến 19.3 có stable View Transition integration, Fragment refs cùng các capability React DOM mới. Vì feature có thể xuất hiện ở minor, library author phải khai minimum peer version chính xác.

## 2. React Compiler 1.0

React Compiler 1.0 đã stable. Đây là build-time optimizer hiểu Rules of React và có thể tự động memoize component/value để giảm nhu cầu tự viết `useMemo`, `useCallback` và `memo` trong nhiều trường hợp.

Compiler không nên được hiểu đơn giản là “plugin tự thêm memo”. Nó phân tích code React dựa trên purity/reactivity constraints rồi sinh output tối ưu. Babel plugin là một integration phổ biến, nhưng compiler core được thiết kế tách khỏi Babel và ecosystem đang tích hợp nhiều build pipeline khác nhau.

Compiler hỗ trợ React 17, 18 và 19 với cấu hình phù hợp, nhưng React 19 là baseline tự nhiên nhất cho code mới.

> ### Version Note — React Compiler không đi cùng số version React
>
> Trước khi stable, các package/compiler prerelease từng có cách đánh version dễ gây nhầm với React 19.x. Từ Compiler 1.0, hãy xem compiler là toolchain có lifecycle riêng. Khi nâng `react` từ 19.2 lên 19.3 không có nghĩa bạn tự động “nâng Compiler”; và ngược lại, nâng Compiler phải kiểm tra compatibility/configuration riêng.

## 3. Compiler mental model

Trước Compiler, developer thường tự tạo cache boundary:

```jsx
const value = useMemo(() => expensive(a, b), [a, b]);

const handleClick = useCallback(() => {
  submit(id);
}, [id]);

const Child = memo(...);
```

Compiler có thể phân tích dependency và tự tạo memoization phù hợp. Điều này làm thay đổi optimization idiom: code mới nên được viết pure, đơn giản và đúng Rules of React trước, rồi để compiler tối ưu.

Manual memoization vẫn hợp lệ khi cần identity contract cụ thể, effect dependency stability, hoặc khi profiler cho thấy compiler không tối ưu đúng bottleneck. Không xóa hàng loạt `useMemo`/`useCallback` trong code cũ chỉ vì bật Compiler; existing memoization có thể ảnh hưởng behavior hoặc output compilation.

## 4. Rules of React là compiler contract

Rules of React không chỉ là style convention. Chúng tạo điều kiện để runtime và compiler suy luận code an toàn.

Component/Hook phải pure trong render. Props/state được coi immutable theo model. Hook calls phải tuân rules. Không mutate value thuộc render khác. Không giấu side effect trong helper tưởng như pure.

Ví dụ không tốt:

```jsx
function calculateTotal(cart) {
  cart.sort(comparePrice);
  return cart.reduce(sum, 0);
}
```

Nếu `cart` là prop/state, helper mutate input. Tốt hơn:

```jsx
function calculateTotal(cart) {
  return [...cart]
    .sort(comparePrice)
    .reduce(sum, 0);
}
```

Hoặc dùng non-mutating API khi environment hỗ trợ:

```js
cart.toSorted(comparePrice)
```

## 5. Manual memoization trong thời đại Compiler

Manual memoization vẫn có chỗ đứng.

Một external integration có thể yêu cầu callback identity ổn định. Một Effect có thể cần object/function ổn định để không restart synchronization. Một phép tính rất nặng có thể cần cache mà profiler xác nhận. Library có thể chạy trong app không bật Compiler nên vẫn cần performance strategy riêng.

Senior code không được đánh giá bằng số lượng `useMemo`; thường code càng đơn giản càng tốt nếu compiler/runtime đã xử lý phần tối ưu.

## 6. Chiến lược adopt Compiler

Với codebase lớn, adoption nên incremental:

1. Bật lint rules liên quan React/Compiler.
2. Sửa purity và Hook rule violations.
3. Bật Compiler cho scope nhỏ hoặc theo cấu hình incremental.
4. Chạy test và so sánh behavior.
5. Profile performance critical flow.
6. Theo dõi build time và bundle/runtime regression.
7. Mở rộng phạm vi khi ổn định.

Không nên bật Compiler rồi bỏ qua warning. Một số code có thể bị skip; mục tiêu là codebase tuân Rules of React, không chỉ “build thành công”.

## 7. Compiler directives và compilation boundary

React Compiler có directives/configuration để điều khiển compilation trong các trường hợp cần thiết. Đây là exception mechanism, không phải default coding style. Nếu codebase phải rải directive tắt compiler khắp nơi, thường cần refactor logic vi phạm Rules of React hoặc integration boundary chưa đúng.

Vì directives có thể tiến hóa, luôn đọc reference đúng compiler version thay vì copy config cũ từ blog.

## 8. Scheduling và priority ở mức application

Application developer không cần thao tác scheduler internal API. Public primitives như transitions và deferred value cho phép biểu đạt priority ở mức UX.

Có thể nghĩ thành hai nhóm:

```text
Urgent: typing, pointer feedback, direct manipulation
Non-urgent: render result lớn, đổi tab nặng, background refresh
```

Một lỗi là biến mọi update thành transition. Nếu user bấm toggle mà visual feedback bị trì hoãn, UX xấu. Priority là semantic UX, không chỉ performance knob.

## 9. Suspense architecture và reveal strategy

Suspense boundary nên phản ánh “reveal unit”: nhóm nội dung nào nên xuất hiện cùng nhau.

```jsx
<PageShell>
  <Header />

  <Suspense fallback={<ProductSkeleton />}>
    <Product />
  </Suspense>

  <Suspense fallback={<ReviewsSkeleton />}>
    <Reviews />
  </Suspense>
</PageShell>
```

Nếu product critical còn reviews secondary, hai boundary riêng cho phép progressive reveal. Boundary quá cao khiến toàn màn hình đổi spinner; boundary quá nhỏ tạo loading rời rạc. Skeleton nên giữ layout để tránh CLS.

## 10. Streaming architecture

SSR streaming gửi phần HTML sẵn sàng trước thay vì chờ toàn tree. Node thường dùng `renderToPipeableStream`; Web Streams environment dùng `renderToReadableStream`. React 19.x còn có nhóm prerender/resume cho architecture server phức tạp hơn.

Tự xây SSR framework đòi hỏi xử lý asset injection, abort, error status, CSP nonce, hydration data, cache, routing và deployment. Application team thường nên dùng framework thay vì tự viết toàn bộ protocol.

## 11. Partial pre-rendering và prerender/resume

React 19.x tiếp tục mở rộng server rendering để kết hợp pre-rendered shell với dynamic/resumable content. Master-level concern ở đây là phân biệt primitive của React DOM với feature marketing/implementation của framework.

Khi thiết kế server rendering/cache, cần trả lời:

```text
phần nào static ở build time?
phần nào static theo request?
phần nào personalized?
cache key là gì?
invalidated lúc nào?
HTML nào có thể dùng chung?
data nào tuyệt đối không được cache cross-user?
```

Nếu không trả lời rõ cache key và scope, chưa nên cache.

## 12. React Server Components architecture

RSC chuyển một phần component execution sang server/build environment và chỉ gửi client những gì cần cho interactivity.

Lợi ích tiềm năng: giảm client JavaScript; colocate server data access; stream composition; tránh gửi server-only dependency vào client bundle nếu boundary đúng.

Chi phí: mental model hai môi trường; serializability boundary; framework coupling; cache semantics phức tạp; security surface mới; debug/tooling khó hơn SPA thuần.

Không chọn RSC chỉ vì “mới”. Chọn khi product và framework thực sự hưởng lợi.

## 13. RSC payload và client boundary

Server Components không chỉ “render thành HTML”. Framework sử dụng RSC protocol/payload để biểu diễn rendered server tree, references tới Client Components và dữ liệu serializable. SSR có thể phối hợp để tạo initial HTML.

`"use client"` tạo client module boundary. Props từ server đi qua Client Component boundary phải serializable theo contract hỗ trợ. Không truyền tùy tiện class instance, DB connection hoặc function thường. Server Function reference là trường hợp protocol xử lý riêng.

## 14. Cache/data ownership trong RSC/full-stack React

Một hệ thống có thể có nhiều lớp cache:

```text
browser HTTP cache
CDN/edge cache
framework route/data cache
React request/cache primitive
database cache
client query cache
```

Sai lầm nghiêm trọng là cache global dữ liệu theo user nhưng key không chứa user identity, dẫn tới data leak. Mỗi cache phải có scope, key, lifetime và invalidation rõ.

Một idiom tốt: “Nếu không mô tả được cache key bằng một câu hoàn chỉnh, chưa nên cache.”

## 15. Security cho RSC và Server Functions

Server Function phải được coi là network entry point dù syntax trông như gọi function local.

Checklist tối thiểu:

```text
authenticate
authorize
validate input
rate-limit khi cần
protect theo CSRF/threat model của framework
avoid secret leakage
avoid mass assignment
sanitize/encode đúng context
log audit action quan trọng
patch security advisory
```

Không tin hidden field, role gửi từ client hay serialized object. Server Component cũng có thể leak secret nếu vô tình truyền secret thành Client Component prop.

> ### Version Note — patch version là một phần của architecture security
>
> Các advisory React Server Components cuối năm 2025 cho thấy một major/minor label như `19.1` không đủ để đánh giá an toàn; fix đã được backport qua nhiều patch branch và một số bản fix ban đầu còn tiếp tục được cập nhật. Với RSC, quy trình release phải bao gồm dependency/security monitoring và upgrade theo advisory chính thức của React/framework. Baseline 19.3 của tài liệu giúp học API mới nhất, nhưng production vẫn phải theo patch release hiện hành thay vì “đóng băng vì đã ở 19.3”.

## 16. Trusted Types và XSS boundary

React escape text mặc định nhưng XSS vẫn có thể xuất hiện qua `dangerouslySetInnerHTML`, URL nguy hiểm, third-party DOM library, raw HTML renderer hoặc server output không sanitize.

React 19.3 có cải tiến liên quan Trusted Types. Trusted Types + CSP + sanitization là defense-in-depth; không nên coi React escaping là lớp bảo vệ toàn diện.

## 17. Large-scale state architecture

Ở scale lớn, state nên theo domain và ownership thay vì theo một library duy nhất.

```text
Route / URL
 ├─ search / filter / page
Feature server data
 ├─ query cache / RSC
Feature form
 ├─ local / form library
Feature UI state
 ├─ local reducer
Cross-feature client state
 └─ external store
```

Giant global store chứa route, API cache, modal, form draft, user profile và mọi entity trở thành coupling hub. Maturity architecture thể hiện ở khả năng không globalize dữ liệu không cần global.

## 18. State machine và reducer design

Boolean state dễ tạo impossible states:

```js
{
  loading: true,
  success: true,
  error: true
}
```

Tốt hơn:

```ts
type State =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: Data }
  | { status: "error"; error: Error };
```

Workflow phức tạp có thể dùng state machine. State machine phù hợp khi transition rule chặt, nhiều side effect và cần model rõ. Không dùng cho counter đơn giản.

## 19. Event-driven UI architecture

Event-driven model tách “điều gì xảy ra” khỏi “state thay đổi ra sao”:

```js
dispatch({
  type: "checkout_submitted",
  payload: formData,
});
```

Reducer/state machine xử lý transition; effect/service layer xử lý I/O. Pattern này hữu ích ở workflow enterprise nhưng không nên tự xây framework event bus riêng nếu library hiện có đã giải quyết tốt.

## 20. Design system architecture

Một design system production có nhiều lớp:

```text
design tokens
primitive components
accessible behavior
composite components
patterns/templates
documentation
visual regression
versioning
```

Primitive như Button/Input/Dialog phải rất ổn định vì hàng trăm consumer phụ thuộc. API quá mở làm phá consistency; API quá đóng làm team fork component. Headless primitive + token/variant layer thường cân bằng tốt.

## 21. Library authoring

React library phải cân nhắc public type surface, peer dependency, SSR compatibility, ESM/CJS strategy, tree shaking, side effects, styling injection, accessibility, ref API, compiler compatibility và version support.

Không nên bundle React vào library thông thường; React thường là peer dependency để tránh duplicate React và Hook failure. Không truy cập `window` ở module top level nếu library cần SSR.

## 22. Package exports và peer dependencies

Ví dụ conceptual:

```json
{
  "name": "@acme/ui",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "peerDependencies": {
    "react": ">=19.3.0",
    "react-dom": ">=19.3.0"
  }
}
```

Nếu dùng API 19.3-only, minimum peer version phải phản ánh điều đó. Dual ESM/CJS cần test trên bundler/Node/test runner thật; package resolution khác nhau giữa toolchains.

## 23. React version migration

Migration tốt gồm:

```text
đọc official upgrade guide
update react + react-dom đồng bộ
update types
update framework
chạy codemod nếu được khuyến nghị
fix deprecated API
run test
run production build
profile critical flow
canary release
monitor production errors
```

Với RSC framework, React có thể bị framework pin. Không force React upgrade độc lập nếu framework chưa support.

### Migration path thực tế giữa các thế hệ

Nếu đang ở React 17, bước đầu là chuyển root API và ecosystem tương thích React 18, sau đó kiểm tra Strict Mode/automatic batching/concurrency assumptions. Nếu đang ở React 18.2, có thể đi qua **18.3** để nhận warning migration rồi mới lên React 19. Với React 19, phải cập nhật `react` và `react-dom` đồng bộ, TypeScript types tương ứng, chạy codemod được React team khuyến nghị và kiểm tra framework peer dependency.

Một migration không nên được đánh giá thành công chỉ vì app “render được”. Các thay đổi như batching, hydration, ref callback cleanup, TypeScript typings, removed legacy APIs hoặc third-party library dựa vào React internals có thể chỉ lộ trong test, SSR hoặc production.

Đối với framework RSC, không force một React minor/patch mới hơn framework support matrix. Framework có thể pin hoặc thử nghiệm một build React cụ thể để đồng bộ protocol/server runtime.

## 23A. Migration là behavior-preserving transformation, không phải đổi syntax hàng loạt

Một migration React tốt giữ behavior và ownership ổn định trước khi đổi abstraction. Với class code, hãy inventory state, derived values, subscriptions, DOM refs, async requests, error boundaries và public component contract. Sau đó tách logic theo intent: render derivation ở render, user-caused work ở event handler, external synchronization ở Effect, complex state transition ở reducer, shared cross-tree dependency ở Context/store.

Không cần đổi toàn bộ tree trong một PR. Leaf component ít dependency là điểm bắt đầu tốt; wrapper/HOC có thể tiếp tục bao quanh Function Component mới. Error Boundary class có thể được giữ lại nếu đang hoạt động ổn. Snapshot/integration/E2E tests dùng làm safety net cho behavior, còn codemod chỉ giải quyết mechanical API changes.

Khi nâng version đồng thời với refactor component model, rủi ro tăng vì khó phân biệt lỗi do runtime behavior change hay do rewrite. Với codebase lớn, tách **version migration**, **deprecated API removal** và **architecture refactor** thành các bước quan sát được thường an toàn hơn.

## 24. Legacy Class Component

Enterprise code vẫn có class:

```jsx
class Counter extends React.Component {
  state = { count: 0 };

  componentDidMount() {
    // setup
  }

  componentWillUnmount() {
    // cleanup
  }

  render() {
    return (
      <button
        onClick={() =>
          this.setState(s => ({ count: s.count + 1 }))
        }
      >
        {this.state.count}
      </button>
    );
  }
}
```

Các API cần biết để đọc code cũ: `props`, `state`, `setState`, `render`, `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`, `getDerivedStateFromProps`, `getSnapshotBeforeUpdate`, `componentDidCatch`.

Không migrate lifecycle sang `useEffect` theo mapping một-một máy móc. Hook model dựa trên synchronization và data flow khác lifecycle model của class.

## 24A. Legacy React Reference — đủ để đọc project React 15–18

Phần này là reference có giải thích cho các API đời cũ quan trọng. Mục tiêu không phải khuyên viết code mới bằng chúng mà để khi mở một project enterprise lâu năm, bạn hiểu chính xác code đang làm gì.

### Component creation

#### `React.createClass(spec)`

Tạo component theo object specification. Các key phổ biến gồm `render`, `getInitialState`, `getDefaultProps`, lifecycle methods, custom methods và `mixins`. Methods được autobind. Từ React 15.5 API được đưa ra khỏi core; package `create-react-class` tồn tại cho migration.

#### `React.Component`

Base class cho ES6 Class Component:

```jsx
class App extends React.Component {
  render() {
    return <div />;
  }
}
```

Các instance field quan trọng là `this.props`, `this.state`, `this.context`; API update chính là `this.setState` và `this.forceUpdate`.

#### `React.PureComponent`

Giống `Component` nhưng có shallow props/state comparison tương đương một implementation thông thường của `shouldComponentUpdate`.

### Class state APIs

#### `this.setState(nextStateOrUpdater, callback?)`

Object form shallow-merges state. Updater form nhận previous state và props:

```jsx
this.setState(
  (state, props) => ({
    count:
      state.count +
      props.step,
  }),
  () => {
    console.log("committed");
  }
);
```

Callback tồn tại trong class API cũ nhưng Hook setter không có callback tương đương. Với Hooks, logic “sau state commit” phải được model theo Effect/event semantics chứ không truyền callback vào setter.

#### `this.forceUpdate(callback?)`

Yêu cầu component re-render dù React không được báo state change thông thường. Đây là escape hatch. Nếu app cần `forceUpdate` thường xuyên, có thể data source nằm ngoài React mà không có subscription đúng. Với external store hiện đại, `useSyncExternalStore` là abstraction phù hợp hơn.

### Class lifecycle reference

```text
constructor
static getDerivedStateFromProps
render
componentDidMount

shouldComponentUpdate
static getDerivedStateFromProps
render
getSnapshotBeforeUpdate
componentDidUpdate

componentWillUnmount

static getDerivedStateFromError
componentDidCatch
```

Legacy names:

```text
UNSAFE_componentWillMount
UNSAFE_componentWillReceiveProps
UNSAFE_componentWillUpdate
```

Các tên không có `UNSAFE_` từng tồn tại trong code cũ và dần bị deprecate. “UNSAFE” nói về incompatibility của assumptions trong async/concurrent rendering, không có nghĩa method luôn gây crash.

### Error Boundary class APIs

`static getDerivedStateFromError(error)` dùng để cập nhật fallback state từ lỗi render. `componentDidCatch(error, info)` dùng side effect như logging. Error Boundary class vẫn là kiến thức thực tế vì React core chưa cung cấp một Hook thay thế trực tiếp cho toàn bộ Error Boundary behavior.

### React element APIs

`createElement` vẫn là primitive hợp lệ. `cloneElement`, `isValidElement` và nhóm `Children` vẫn xuất hiện trong library code. Tuy nhiên `Children`/`cloneElement` thường làm component structure opaque hơn và nên được cân nhắc so với explicit composition/context.

`createFactory` và old DOM factories là legacy/removed như đã giải thích.

### Ref APIs theo thời đại

```text
string ref
→ callback ref
→ createRef
→ forwardRef
→ useRef
→ React 19 ref-as-prop
```

Không phải bước sau luôn “xóa” bước trước. Callback ref vẫn hữu ích; `createRef` vẫn phù hợp class; `forwardRef` vẫn quan trọng cho React 18 compatibility; ref-as-prop là API mới cho Function Component React 19.

### ReactDOM legacy root APIs

```jsx
ReactDOM.render(element, container);
ReactDOM.hydrate(element, container);
ReactDOM.unmountComponentAtNode(container);
ReactDOM.findDOMNode(component);
```

Các API này là dấu hiệu rõ nhất của codebase pre-modern root. React 18 deprecate root legacy APIs và React 19 remove chúng. Migration target là `createRoot`, `hydrateRoot`, `root.unmount` và explicit refs.

### Legacy Context

```text
childContextTypes
getChildContext()
contextTypes
```

Legacy Context bị remove ở React 19. New Context API có từ React 16.3, sau đó Function Component đọc bằng `useContext`; React 19 cho render Context object trực tiếp như provider.

### Type/runtime checking legacy

`React.PropTypes` chuyển sang `prop-types` từ React 15.5. Function-component `propTypes` không còn được React 19 xử lý. Điều này không có nghĩa runtime validation luôn vô dụng: dữ liệu ở network/form boundary vẫn có thể cần schema validation; TypeScript chỉ kiểm tra compile time.

### Legacy reuse patterns

Mixins → HOC → render props → Custom Hooks là một lịch sử composition dễ gặp. Không có nghĩa HOC/render props bị remove. Redux `connect`, decorators hoặc component APIs cũ vẫn có thể dùng HOC hợp lệ.

### Legacy testing

Enzyme/shallow-rendering-style test từng rất phổ biến vì class component và implementation detail dễ inspect. React hiện đại khuyến nghị test behavior qua DOM/native environment hơn. Khi migrate, đừng chỉ đổi test API; hãy chuyển assertion từ internal state/instance method sang output và user interaction khi có thể.

## 25. Legacy APIs và deprecation mindset

Code cũ có thể chứa string refs, old context, `findDOMNode`, legacy root hoặc lifecycle `UNSAFE_...`. Không chỉ thay tên API; cần hiểu vì sao API cũ xung đột với concurrent architecture, encapsulation hoặc new rendering model.

Migration tốt sửa mental model, không chỉ làm warning biến mất.

## 26. Hydration at scale

Hydration cost lớn nếu page có quá nhiều Client Components. Các chiến lược gồm giảm client boundary, server render static content, code split, defer non-critical interaction, stream, tránh root provider quá lớn và không serialize data khổng lồ.

Hydration mismatch nên được monitor ở production. Lỗi timezone/locale/ngẫu nhiên có thể rất khó tái hiện local.

## 27. Performance budget

Team nên có performance budget thay vì “cảm giác nhanh”:

```text
initial JS
route JS
LCP
INP
CLS
API latency
interaction readiness
long tasks
React commit duration
```

Budget phải dựa trên device/network target thật. Máy desktop mạnh của developer không đại diện user mobile mid-range.

## 28. Interaction performance

INP/interaction latency có thể xấu khi event kích hoạt JS/render/layout dài. Các hướng xử lý: giảm work trong event; chuyển non-urgent work sang transition; virtualize; split computation; tránh layout thrash; dùng Web Worker nếu CPU-heavy thích hợp; tối ưu algorithm trước memo.

React optimization không thay algorithmic optimization.

## 29. Memory leak và resource lifecycle

Leak thường đến từ resource không cleanup: listener, timer, observer, subscription, WebSocket, retained cache hoặc DOM reference lớn.

```jsx
useEffect(() => {
  const observer = new ResizeObserver(handleResize);
  observer.observe(node);

  return () => observer.disconnect();
}, [node]);
```

Cleanup phải đối xứng setup. Abort request cũng giảm resource/network lãng phí khi phù hợp.

## 30. Observability

Production React cần error tracking và performance telemetry. Một error event hữu ích có thể chứa release version, route, feature, pseudonymous session/user identifier nếu policy cho phép, correlation/request ID, component boundary, stack, browser/device và network context.

Không log token, password, PII nhạy cảm hoặc toàn bộ form payload. Error Boundary nên report unexpected render error nhưng tránh duplicate flood.

## 31. Testing pyramid ở scale lớn

Một platform trưởng thành thường có:

```text
Static      -> TypeScript, ESLint, React/Compiler lint
Unit        -> domain functions, reducers
Component   -> accessible interaction
Integration -> feature + network mock
E2E         -> critical journeys
Visual      -> design system/pages
Performance -> budget regression
A11y        -> automated + manual
```

Mục tiêu là confidence/time ratio, không phải số test tối đa.

## 32. Accessibility governance

Ở organization scale, accessibility phải được encode vào primitive/design system và CI thay vì phụ thuộc từng developer nhớ ARIA. Design system nên cung cấp Dialog, Menu, Tabs, Tooltip, Combobox có behavior accessible.

PR checklist nên bao gồm keyboard, focus và accessible name. Automated accessibility test chỉ bắt một phần lỗi; manual testing vẫn cần.

## 33. Internationalization

React chỉ render text; i18n cần architecture riêng. Cần xử lý translation message, plural, number/currency, date/time/timezone, RTL, text expansion, locale route và server/client locale consistency.

Không nối string kiểu:

```js
`${count} items`
```

nếu cần plural đa ngôn ngữ. Dùng message formatter. SSR/hydration phải dùng locale/timezone nhất quán hoặc có render strategy rõ.

## 34. Forms ở scale lớn

Large form không nhất thiết dùng một state object khổng lồ khiến toàn form render mỗi keystroke. Có thể dùng uncontrolled/native FormData, field-level subscription, schema validation, Server Actions hoặc state machine cho multi-step flow.

Async validation cần debounce/cancel. Validation schema có thể dùng chung client/server nếu hợp lý, nhưng authorization luôn ở server. Error summary và focus tới field lỗi là accessibility requirement quan trọng.

## 35. React + TypeScript advanced patterns

Polymorphic component:

```tsx
type BoxProps<T extends React.ElementType> = {
  as?: T;
  children?: React.ReactNode;
} & Omit<
  React.ComponentPropsWithoutRef<T>,
  "as" | "children"
>;

function Box<T extends React.ElementType = "div">(
  props: BoxProps<T>
) {
  const { as, children, ...rest } = props;
  const Component = as ?? "div";
  return <Component {...rest}>{children}</Component>;
}
```

Pattern mạnh nhưng type complexity cao; chỉ dùng khi design system thật sự cần.

Discriminated prop union:

```tsx
type AlertProps =
  | { kind: "success"; retry?: never }
  | { kind: "error"; retry: () => void };
```

Generic list:

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => React.Key;
  renderItem: (item: T) => React.ReactNode;
};
```

Generic abstraction chỉ nên dùng khi có reuse thật; application domain code không cần generic hóa mọi thứ.

## 36. API stability và semantic versioning

Public component API là contract. Breaking change không chỉ là đổi prop name. Thay DOM structure, focus behavior, default controlled mode, CSS specificity hoặc event timing cũng có thể break consumer.

Design system cần changelog, migration guide và codemod cho breaking change lớn. Feature flag/canary deployment giảm blast radius.

## 37. Senior/Master coding idioms

### Derive, do not synchronize

Nếu value tính được từ render inputs, tính trực tiếp thay vì state + Effect.

### Event logic stays in event

Nếu logic xảy ra vì user action, xử lý trong event/Action thay vì state flag + Effect.

### State colocation

State ở gần consumer nhất, chỉ lift khi cần phối hợp.

### Composition over boolean explosion

Cho consumer ghép structure thay vì hàng chục boolean layout props.

### Boundary-oriented architecture

Route, Suspense, Error, Client/Server, data và feature đều là boundary. Boundary rõ giúp kiểm soát failure/performance/security.

### Make impossible states impossible

Dùng reducer, discriminated union hoặc state machine.

### Measure before memo

Không tối ưu theo intuition.

### Framework APIs are not React APIs

Cache/revalidate/router semantics của một framework không nên được mô tả là behavior chung của React.

## 38. Anti-pattern catalog

### Effect như event bus

Không nên:

```jsx
setShouldSave(true);

useEffect(() => {
  if (shouldSave) save();
}, [shouldSave]);
```

Thường nên gọi `save()` từ event/action.

### Mirrored props

```jsx
const [value, setValue] = useState(propValue);
```

mà không có semantics local draft rõ.

### Global mutable singleton

```js
export const state = {};
```

component đọc trực tiếp rồi mong React tự biết update.

### Giant context

Một provider chứa hàng chục field update với tần suất khác nhau.

### Premature abstraction

Tạo framework generic sau use case đầu tiên.

### Memo cargo cult

Mọi function đều `useCallback`, mọi object đều `useMemo`.

### Index key trong editable/reorderable list

Dễ gây state identity bug.

### Side effect trong render

Gọi API, analytics, mutate global.

### Browser API trong server render

Đọc `window`/`localStorage` không guard.

### Authentication-only UI

Ẩn nút nhưng server không authorize.

## 38A. Production deployment: build → canary → rollback

Deployment React không chỉ là `npm run build`. SPA/static hosting cần asset hashing, cache policy khác nhau giữa HTML entry và immutable JS/CSS, cùng history fallback để deep link không 404. Giá trị environment bundle vào client phải xem là public; secret chỉ ở server runtime.

SSR/RSC còn có server runtime, streaming, server/client manifests, cache/invalidation và compatibility giữa framework với React server packages. CDN cache key phải phân biệt public với personalized data để tránh cross-user leak.

Pipeline production nên có lint/typecheck/test/build, dependency/security scan, accessibility/performance checks cho critical flow, preview/canary, release ID cho source maps/logs, health check, error/Web Vitals monitoring và rollback artifact known-good. Feature flag tách deploy code khỏi enable behavior. Khi migrate CRA → Vite/framework cần audit env semantics, public path, router fallback, dynamic imports, service worker/PWA, test runner và deployment base path.

## 38B. Production architecture phải có boundary, budget và recovery path

Một React production architecture nên mô tả rõ ít nhất năm boundary: **render boundary** (component/Suspense/Error Boundary), **state ownership boundary**, **network/cache boundary**, **server/client module boundary**, và **deployment/observability boundary**. Nếu mọi concern hội tụ ở root provider hoặc một global store, failure blast radius và invalidation scope thường quá lớn.

Mỗi critical flow nên có budget và recovery path: loading bao lâu thì đổi UX, retry ở đâu, stale data được giữ bao lâu, lỗi nào user có thể sửa, lỗi nào cần report, bundle/interaction budget là bao nhiêu, rollback version nào là known-good. Feature flag giúp tách deploy khỏi release behavior; release ID nối source map, log và metric với đúng artifact.

Production review cũng phải kiểm tra cache ownership. Browser/CDN/server/query cache cùng tồn tại có thể tạo nhiều lớp stale data. Không cache personalized HTML/data bằng key chung. Mutation phải xác định invalidation hoặc optimistic reconciliation rõ; nếu không, UI có thể “nhanh” nhưng sai consistency.

## 39. Architecture review checklist

Khi review feature React production, phải trả lời được các câu dưới đây bằng architecture cụ thể thay vì chỉ tên library.

**Data:** source of truth ở đâu, cache ở đâu, invalidation ra sao, ownership là ai.

**Rendering:** CSR/SSR/RSC, boundary nào suspend, route nào code split.

**State:** local/URL/form/server/global nào thực sự cần.

**Effects:** mỗi Effect đang synchronize resource nào.

**Errors:** expected error hiển thị đâu, unexpected error boundary nào bắt.

**Security:** authn/authz/validation ở server nào.

**Performance:** critical path, bundle, list, interaction và profiler evidence.

**Accessibility:** keyboard, focus, semantic, live announcement.

**Testing:** risk nào được test ở layer nào.

**Versioning:** API có tương thích React/framework target không.

## 40. Lộ trình sau React core

SPA enterprise nên học sâu router, TanStack Query hoặc server-state equivalent, form library, accessibility primitives, TypeScript, testing và observability.

Full-stack React nên học framework có SSR/RSC/streaming phù hợp và hiểu caching/deployment của chính framework đó.

Design system engineer nên học ARIA Authoring Practices, headless primitives, CSS architecture, tokens, package publishing và visual regression.

Performance engineer nên học browser rendering, Core Web Vitals, Performance API, network protocol, bundler và profiling.

React Native cần học host environment riêng; DOM knowledge không áp dụng nguyên xi.

## 41. Bản đồ API quan trọng

| Nhóm | API / thành phần | Vai trò |
|---|---|---|
| Component | Function Component, Fragment | Mô tả UI |
| State | `useState`, `useReducer` | Local state / transition |
| Context | `createContext`, `useContext`, `use` | Dữ liệu theo subtree |
| Effect | `useEffect`, `useLayoutEffect`, `useEffectEvent`, `useInsertionEffect` | External synchronization |
| Ref | `useRef`, `useImperativeHandle` | Mutable value / imperative API |
| Identity | `key`, `useId` | Component identity / stable ID |
| Memoization | `memo`, `useMemo`, `useCallback` | Manual optimization |
| Concurrency | `startTransition`, `useTransition`, `useDeferredValue` | Priority |
| Async UI | `Suspense`, `lazy`, `use` | Suspension / code-data coordination |
| Actions | `useActionState`, `useOptimistic`, form action | Mutation workflow |
| React DOM form | `useFormStatus` | Form pending/status |
| DOM | `createPortal` | Render sang host node khác |
| Root | `createRoot`, `hydrateRoot` | Client root / hydration |
| Server DOM | `renderToPipeableStream`, `renderToReadableStream`, prerender/resume family | SSR/streaming |
| External store | `useSyncExternalStore` | Store ngoài React |
| RSC | `"use client"`, `"use server"` | Client boundary / Server Function |
| React 19.2+ | `<Activity />` | Visible/hidden activity subtree |
| React 19.3 | View Transitions, Fragment refs và capability mới theo release | Modern UI/server primitives |
| Build-time | React Compiler 1.0 | Automatic memoization/optimization |

## Versioning principles cần mang theo sau khi học xong

React versioning nên được nhìn như một ma trận capability chứ không phải một chuỗi tutorial riêng biệt. Component/props/state/purity vẫn là nền xuyên version; React 18 thay đổi nền scheduling/root; React 19 mở rộng async/server model; minor 19.2 và 19.3 tiếp tục thêm public API. Vì vậy lộ trình đúng là học mental model bền vững trước, sau đó gắn version vào đúng API.

Khi gặp code lạ, hãy kiểm tra theo thứ tự: `react` → `react-dom` → framework → compiler/bundler → library peer dependency → patch/security advisory. Cách này đáng tin hơn việc nhớ “React 19 có gì” vì ecosystem và patch level có thể thay đổi độc lập.

## 42. Kết luận

Master React không phải nhớ càng nhiều Hook càng tốt. Cốt lõi là hiểu React như một hệ thống render khai báo có invariants về purity, identity, ownership và synchronization.

Người mới thường hỏi “Hook nào giải quyết việc này?”. Engineer có kinh nghiệm hơn hỏi “dữ liệu này thuộc ai, transition nào xảy ra, external system nào cần synchronize, boundary nào chịu trách nhiệm và failure/performance/security semantics là gì?”. Khi câu hỏi thay đổi theo hướng đó, React thường trở nên đơn giản hơn vì Hook chỉ còn là công cụ biểu đạt architecture.

## Version Notes

Bộ tài liệu lấy React 19.3 làm baseline. React 19.3 phát hành ngày 09/09/2026. React Compiler 1.0 đã stable và production-ready. Server Components trong React 19 có model ổn định cho application usage, trong khi APIs dành cho bundler/framework implement RSC có versioning constraints riêng. Security advisory phải được theo dõi theo patch/minor thực tế, không chỉ major version.

## Nguồn chuẩn để kiểm chứng

Ưu tiên tài liệu chính thức React: React Versions, React Blog release notes, Learn, API Reference, React DOM Server, React Server Components và React Compiler. Với framework, phải đọc tài liệu đúng version của framework vì router, cache, deployment và RSC integration không hoàn toàn thuộc React core.
