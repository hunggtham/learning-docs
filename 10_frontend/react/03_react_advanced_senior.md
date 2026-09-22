# React Master Note — Advanced / Senior

> React 19.3 là mốc stable hiện hành cho API mới; file này tập trung invariants xuyên version: reconciliation/identity, concurrency, Suspense, server/client boundary, architecture, performance, security và production practices.

## 1. Render architecture và Fiber mental model

React không cập nhật DOM ngay khi setter được gọi. Nó schedule work, thực hiện render để tính cây UI mới, rồi commit thay đổi host cần thiết. Implementation hiện đại dùng Fiber làm unit-of-work structure để hỗ trợ scheduling. Application developer không nên phụ thuộc field/internal API của Fiber, nhưng phải hiểu ba hệ quả: render có thể chạy lại; render có thể bắt đầu rồi bị bỏ; và chỉ commit mới làm thay đổi DOM trở thành hiệu lực.

Do đó render phải pure. Không gửi request thanh toán, mutate global object, log audit hay điều khiển DOM bên ngoài trong render.

## 2. Render phase và commit phase

Render phase chạy component function và tính React element tree. Commit phase áp dụng host changes, ref và Effect theo timing tương ứng.

```jsx
function Product({ product }) {
  const price = formatPrice(product.price);
  return <strong>{price}</strong>;
}
```

`formatPrice` nên pure. Analytics do user click đặt ở event. Analytics gắn với việc screen được đồng bộ/hiển thị có thể dùng Effect tùy semantics. Senior code review nên hỏi “logic này thuộc render, event hay synchronization?” trước khi hỏi “dùng Hook nào?”.

## 3. State identity, preserve và reset

State được lưu theo identity của component trong cây React, không “nằm trong function”.

```jsx
{mode === "a"
  ? <Editor key="a" />
  : <Editor key="b" />}
```

Hai key khác nhau ép identity khác và reset local state.

Nếu chỉ đổi prop:

```jsx
<Editor documentId={documentId} />
```

state thường được preserve. Nếu draft phải reset khi document đổi, có thể model draft theo ID, chủ động reset hoặc `key={documentId}` nếu muốn remount subtree. `key` là công cụ identity, không chỉ là list warning.

## 4. Concurrent rendering

Concurrent React không có nghĩa component JavaScript chạy multi-thread. Nó nghĩa React có thể làm render work theo cách interruptible/prioritized. Update có priority khác nhau, nên một render non-urgent có thể bị urgent input chen vào.

Concurrency API không thay kiến trúc tốt. Trước tiên giảm work, tránh waterfall và profile.

## 4A. Reconciliation dưới concurrent rendering

Concurrent rendering không thay identity rules; nó thay cách render work được schedule. React có thể bắt đầu, pause, restart hoặc abandon render trước commit, nên render phải pure. Reconciliation trả lời tree nào là cùng identity và cần thay gì; scheduling trả lời work nào ưu tiên và có thể ngắt. External store cần snapshot nhất quán với concurrency, là lý do React 18 có `useSyncExternalStore` thay cho subscription Effect tự chế dễ tearing.

## 5. `useTransition` và `startTransition`

```jsx
const [isPending, startTransition] = useTransition();

function handleChange(event) {
  const value = event.target.value;
  setQuery(value); // urgent

  startTransition(() => {
    setFilter(value); // non-urgent
  });
}
```

Transition không phải debounce. Debounce trì hoãn theo thời gian; transition biểu đạt priority. `startTransition` standalone dùng khi không cần pending state tại caller.

## 6. `useDeferredValue`

```jsx
const deferredQuery = useDeferredValue(query);
return <SearchResults query={deferredQuery} />;
```

Input cập nhật ngay theo `query`, subtree nặng có thể dùng value cũ tạm thời. Transition phù hợp khi bạn kiểm soát setter; deferred value hữu ích khi value đến từ parent hoặc cần defer consumer.

> ### Version Note — transition là nền tảng React 18
>
> `startTransition`, `useTransition` và `useDeferredValue` thuộc wave React 18. Chúng không phải “React 19 optimization”. React 19 tiếp tục xây Actions/Suspense/server features trên concurrent foundations này, nên hiểu transition trước khi học Actions và Activity sẽ giúp luồng học tự nhiên hơn.

## 6A. Transition, deferred value và debounce giải quyết ba vấn đề khác nhau

`startTransition`/`useTransition` gắn **priority semantic** cho update: input trực tiếp vẫn urgent, còn render kết quả nặng có thể non-urgent. `useDeferredValue` cho consumer dùng một value chậm hơn source hiện tại khi caller không kiểm soát setter. Debounce lại là kỹ thuật thời gian: chỉ thực hiện công việc sau một khoảng yên lặng. Ba công cụ có thể kết hợp nhưng không thay thế nhau.

Ví dụ search box có thể cập nhật text ngay, defer render danh sách lớn để typing mượt, đồng thời debounce network request để giảm traffic. Nếu chỉ debounce toàn bộ state input, UI có thể cảm giác lag; nếu chỉ transition request, bạn vẫn có thể gửi quá nhiều HTTP calls. Senior design phải tách **responsiveness**, **render priority** và **I/O rate limiting**.

## 7. Suspense nâng cao

```jsx
<Suspense fallback={<Skeleton />}>
  <Profile />
</Suspense>
```

Suspense là boundary cho rendering có thể suspend qua mechanism được React/framework hỗ trợ. Boundary placement là quyết định UX. Một boundary quá cao làm cả màn hình biến thành spinner; quá nhiều boundary nhỏ tạo “popcorn loading”. Skeleton nên giữ layout ổn định để giảm layout shift.

Suspense kết hợp transition cho phép giữ content cũ trong khi content mới chuẩn bị tùy architecture.

## 8. `use`

React 19 có `use(resource)` để đọc Promise hoặc Context theo semantics React hỗ trợ.

```jsx
function Comments({ commentsPromise }) {
  const comments = use(commentsPromise);
  return comments.map(c => <p key={c.id}>{c.text}</p>);
}
```

Promise pending làm component suspend. Không tạo Promise mới vô điều kiện mỗi client render vì dễ gây suspend loop/waterfall. Promise nên đến từ cache/framework/server hoặc một source có identity/lifecycle ổn định.

> ### Version Note — `use` là React 19
>
> API `use` thuộc React 19. Nếu project React 18, bạn không thể copy code `use(promise)` từ docs React mới vào trực tiếp. Ngoài ra `use` không biến mọi Promise tùy ý thành data layer production; cách tạo/cache Promise và integration với framework vẫn quyết định tính đúng đắn.

## 9. Actions và form APIs React 19

React 19 mở rộng async mutation qua Actions. Trong môi trường hỗ trợ, form `action` có thể nhận function:

```jsx
<form action={saveAction}>
  <input name="title" />
  <button type="submit">Lưu</button>
</form>
```

Không phải cứ viết `"use server"` trong Vite SPA là có server runtime. Server Actions/Functions cần RSC/framework integration.

## 10. `useActionState`

```jsx
const [state, submitAction, isPending] =
  useActionState(action, initialState);

return (
  <form action={submitAction}>
    <input name="email" />
    <button disabled={isPending}>
      {isPending ? "Đang gửi..." : "Gửi"}
    </button>
    {state?.error && <p>{state.error}</p>}
  </form>
);
```

Dùng khi kết quả mutation cần trở thành form/action state có pending/error/result rõ ràng.

## 11. `useFormStatus`

Từ `react-dom`:

```jsx
import { useFormStatus } from "react-dom";

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" disabled={pending}>
      {pending ? "Đang lưu..." : "Lưu"}
    </button>
  );
}
```

Component đọc status phải nằm trong form context đúng cấu trúc.

## 12. `useOptimistic`

```jsx
const [optimisticMessages, addOptimisticMessage] =
  useOptimistic(
    messages,
    (current, newMessage) => [
      ...current,
      { ...newMessage, sending: true },
    ]
  );
```

Optimistic UI chỉ nên dùng khi rollback/reconciliation rõ. Với giao dịch tài chính hoặc thao tác không thể hoàn tác, UI phải phân biệt “đã gửi yêu cầu” với “đã xác nhận thành công”.

## 13. `useEffectEvent`

React 19.2 thêm `useEffectEvent` để tách logic event-like không reactive khỏi Effect synchronization.

```jsx
const onConnected = useEffectEvent(() => {
  showNotification("Connected", theme);
});

useEffect(() => {
  const connection = createConnection(roomId);
  connection.on("connected", onConnected);
  connection.connect();
  return () => connection.disconnect();
}, [roomId]);
```

Connection phụ thuộc `roomId`; notification đọc `theme` mới nhất mà không reconnect chỉ vì theme đổi. Không dùng API này để lách dependency sai.

### 13A. Effect Event là event do Effect phát ra, không phải “callback ổn định để khỏi thêm dependency”

Điểm khó của `useEffectEvent` là nó giải quyết **hai loại reactivity khác nhau trong cùng một Effect**. Phần setup connection phải reactive theo `roomId`: đổi room thì resource bên ngoài phải disconnect/reconnect. Callback notification lại chỉ cần đọc `theme` mới nhất tại thời điểm sự kiện `connected` xảy ra; `theme` không phải configuration của connection. Nếu cho `theme` vào dependency, đổi theme làm reconnect vô nghĩa. Nếu cố tình bỏ `theme` khỏi dependency, closure có thể stale và linter mất khả năng bảo vệ.

Effect Event tách hai semantics đó. Callback được khai báo bằng `useEffectEvent` luôn đọc props/state mới nhất khi được gọi, nhưng chính Effect Event **không được đưa vào dependency array**. Nó cũng chỉ được khai báo trong cùng component hoặc Custom Hook với Effect sở hữu nó. Vì đây là contract correctness, project dùng API này nên chạy phiên bản `eslint-plugin-react-hooks` đủ mới để linter hiểu Effect Events.

Một dấu hiệu dùng sai là bọc gần như mọi function bằng `useEffectEvent` chỉ để dependency array ngắn lại. Hãy hỏi trước: “Đây có thật sự là một event phát sinh từ synchronization process không?” Nếu value quyết định resource nào được mở, URL nào được subscribe, timer interval bao nhiêu hoặc observer theo dõi node nào, value đó vẫn là dependency của Effect.

## 14. `<Activity />`

React 19.2 giới thiệu Activity để quản lý subtree visible/hidden theo semantics React hiểu, cho phép giữ state trong những flow phù hợp thay vì unmount hoàn toàn.

```jsx
<Activity mode={tab === "messages" ? "visible" : "hidden"}>
  <Messages />
</Activity>
```

Khác conditional rendering vì conditional có thể unmount và mất state. API mới cần kiểm tra version compatibility trước khi dùng trong library public.

### 14A. Hidden không có nghĩa “component vẫn chạy bình thường nhưng CSS `display:none`”

Khi Activity chuyển sang `hidden`, React ẩn children, unmount các Effect của subtree và trì hoãn các update của phần ẩn tới lúc scheduler không còn việc quan trọng hơn. State của subtree vẫn được giữ, nên khi quay lại `visible`, người dùng có thể nhận lại draft/input state thay vì bắt đầu từ đầu. Đây là điểm khác cả với conditional rendering — vốn unmount subtree — lẫn một wrapper CSS đơn thuần — vốn thường để subscriptions, timers và Effects tiếp tục chạy dù UI không nhìn thấy.

Mental model hữu ích là **“preserve state, suspend active side effects, lower scheduling priority”**. Điều này làm Activity phù hợp cho tab/screen có khả năng quay lại, hoặc pre-render màn hình có khả năng được mở tiếp theo. Nhưng giữ state và tree cũng tiêu tốn memory; nếu subtree chứa dữ liệu lớn và xác suất quay lại thấp, unmount thật có thể rẻ hơn. Activity là một trade-off giữa resume latency, background work và memory footprint chứ không phải mặc định thay thế mọi `condition ? <Page /> : null`.

> ### Version Note — React 19.2
>
> `useEffectEvent` và `<Activity />` được thêm ở **React 19.2**. Nếu package khai hỗ trợ React 19.0+, không được import chúng vô điều kiện rồi kỳ vọng consumer 19.0/19.1 chạy được. Đây là ví dụ điển hình cho việc minor version React 19 có thể bổ sung public feature chứ không chỉ bug fix.

## 15. View Transitions trong React 19.3

React 19.3 đưa `<ViewTransition>` thành API stable để React phối hợp với browser View Transition API khi UI enter, exit, thay đổi hoặc một named element được “share” giữa hai vị trí.

Điểm quan trọng là **không phải mọi state update đều animate**. React chỉ kích hoạt View Transition khi thay đổi đó thuộc một Transition, ví dụ update bên trong `startTransition`, reveal của Suspense hoặc update đi qua `useDeferredValue`. Urgent update không bị buộc chờ animation vì phản hồi trực tiếp với input vẫn phải xuất hiện ngay.

```jsx
import {
  startTransition,
  ViewTransition,
} from "react";

function ProductSwitcher() {
  const [productId, setProductId] = useState("a");

  function openProduct(nextId) {
    startTransition(() => {
      setProductId(nextId);
    });
  }

  return (
    <>
      <ProductPicker onSelect={openProduct} />
      <ViewTransition>
        <ProductDetails productId={productId} />
      </ViewTransition>
    </>
  );
}
```

Default behavior là cross-fade; production UI có thể cấu hình riêng enter/exit/update/share và, khi cần, gắn **transition type** bằng `addTransitionType` để phân biệt nguyên nhân như next/previous. Đây là semantic tốt hơn việc animation code tự suy luận direction từ DOM cũ. Tuy vậy View Transition hiện là DOM capability: phải kiểm tra browser support, tôn trọng `prefers-reduced-motion`, và đảm bảo correctness không phụ thuộc animation có chạy hay không.

Senior review cũng cần kiểm tra interruption. User có thể click tiếp khi transition trước chưa kết thúc, Suspense có thể reveal ở thời điểm khác dự kiến, hoặc navigation có thể fail. Animation layer phải là progressive enhancement bên trên state/navigation architecture, không được trở thành source of truth.

## 16. Fragment refs trong React 19.3

Fragment refs giải quyết trường hợp một behavior cần thao tác với **một nhóm sibling DOM nodes** nhưng không muốn thêm wrapper chỉ để có ref, hoặc children đến từ component không expose raw DOM ref.

```jsx
import {
  Fragment,
  useEffect,
  useRef,
} from "react";

function FocusableGroup({ children }) {
  const groupRef = useRef(null);

  useEffect(() => {
    groupRef.current?.focus();
  }, []);

  return (
    <Fragment ref={groupRef}>
      {children}
    </Fragment>
  );
}
```

Ref này nhận một `FragmentInstance`, không phải một DOM element ảo. Instance cung cấp một tập capability giới hạn trên DOM children: quản lý event ở first-level children, di chuyển focus bằng `focus`/`focusLast`/`blur`, gắn `IntersectionObserver` hoặc `ResizeObserver` qua `observeUsing`, lấy geometry bằng `getClientRects`, xác định root/relative position và scroll group vào view. Nhờ vậy component có thể thêm focus/measurement/observation behavior mà không phá semantic HTML hoặc CSS layout bằng một wrapper thừa.

Đừng suy ra Fragment ref là “query selector mới”. Nó cố ý chỉ expose capability React có thể duy trì qua một group children. Nếu abstraction nghiệp vụ cần một node cụ thể, explicit ref vào node đó vẫn rõ hơn. Library public dùng Fragment refs cũng phải khai minimum React 19.3 thay vì nói chung chung `>=19`.

## 17. External store và `useSyncExternalStore`

```jsx
const snapshot = useSyncExternalStore(
  store.subscribe,
  store.getSnapshot,
  store.getServerSnapshot
);
```

API này cung cấp contract để React đọc store ngoài React nhất quán với concurrency/SSR. Library state management thường bọc nó. `getSnapshot` phải trả snapshot ổn định khi store không đổi; trả object mới mọi lần dễ gây render loop hoặc render dư.

Một external store có thể thay đổi giữa lúc React đang render. Nếu component tự `subscribe` bằng Effect rồi đọc mutable singleton trực tiếp, hai component trong cùng một render có thể quan sát hai phiên bản store khác nhau — hiện tượng thường được gọi là tearing. `useSyncExternalStore` tồn tại để store cung cấp snapshot/subscribe contract mà React có thể phối hợp với concurrent rendering và hydration.

`getServerSnapshot` không chỉ là “fallback cho SSR”. Giá trị server snapshot phải tương thích với initial client snapshot dùng trong hydration; nếu server trả `0` nhưng client ngay lần đầu trả `42`, bạn lại tạo mismatch ở một layer khó nhìn thấy. Với selector library, identity của snapshot và equality semantics cũng là một phần performance contract.

### 17A. `cacheSignal`: lifetime của RSC cache phải đi xuống I/O

React 19.2 thêm `cacheSignal()` cho **React Server Components**. Khi một operation nằm trong lifetime của `cache()`, signal cho phép I/O bên dưới biết lúc kết quả cache không còn được dùng — ví dụ render đã hoàn thành, bị abort hoặc fail — để dừng request/resource tương ứng.

```jsx
import {
  cache,
  cacheSignal,
} from "react";

const load = cache(async url => {
  const response = await fetch(url, {
    signal: cacheSignal(),
  });

  return response.json();
});
```

Điểm bản chất không phải API `AbortSignal` mới, mà là **resource lifetime propagation**. Nếu render/cached computation bị hủy nhưng database/HTTP call vẫn chạy đến cùng, server vẫn tiêu connection, CPU và upstream quota cho kết quả không còn consumer. Khi framework hỗ trợ, cancellation signal nên được truyền sâu qua client HTTP, database adapter hoặc service call có khả năng abort. `cacheSignal` không dành cho Client Component fetch Effect; ở client vẫn dùng lifecycle/cancellation của data layer hoặc `AbortController` phù hợp.

## 18. `useInsertionEffect`

`useInsertionEffect` chủ yếu dành cho CSS-in-JS library cần insert styles ở timing đặc biệt trước layout effects. Application business logic gần như không nên dùng.

> ### Version Note — library Hooks của React 18
>
> `useSyncExternalStore` và `useInsertionEffect` được giới thiệu cùng React 18 chủ yếu để external store và CSS-in-JS library tương thích tốt với concurrent rendering. Application code bình thường hiếm khi cần tự dùng `useInsertionEffect`, còn `useSyncExternalStore` thường nằm phía dưới các state-management libraries.

## 19. `useImperativeHandle`

```jsx
function MyInput({ ref }) {
  const inputRef = useRef(null);

  useImperativeHandle(ref, () => ({
    focus() {
      inputRef.current?.focus();
    },
  }), []);

  return <input ref={inputRef} />;
}
```

Expose capability nhỏ giúp giữ encapsulation tốt hơn việc expose raw DOM node. Imperative API là escape hatch; declarative API vẫn nên là mặc định.

## 20. Error architecture

Phân biệt render error, async mutation error, loading error, expected domain validation và unexpected infrastructure error. Expected validation thường nên trở thành state/action result thay vì ném lên global Error Boundary. Unexpected render failure nên bị boundary ở scope phù hợp bắt và report.

Production app cần observability, correlation ID và fallback theo route/feature. Một boundary duy nhất ở root thường quá thô.

## 20A. Async UI cần phân biệt pending, expected error và unexpected render failure

Suspense boundary xử lý “chưa sẵn sàng để render” theo protocol được hỗ trợ; Error Boundary xử lý lỗi render bất ngờ trong subtree; form/action state thường biểu diễn validation hoặc expected mutation failure. Gộp tất cả thành `try/catch + global toast` làm mất semantics và khiến recovery khó dự đoán.

Với data layer production, cần xác định boundary nào retry, boundary nào giữ stale content, boundary nào reset khi route/key đổi và lỗi nào phải report observability. Transition có thể giữ UI cũ trong lúc navigation/data mới chuẩn bị; nhưng nếu request thất bại, UX cần route/action-specific recovery thay vì chỉ spinner biến mất.

## 21. SSR, streaming và hydration

SSR tạo HTML trên server. Browser nhận HTML trước, sau đó React hydrate để gắn interactivity. Streaming cho phép gửi HTML từng phần thay vì chờ toàn tree.

Các API server hiện đại gồm `renderToReadableStream`, `renderToPipeableStream` và nhóm prerender/resume tùy environment/version. Application framework thường gọi thay bạn.

SSR không đồng nghĩa Server Components. SSR là render thành HTML initial; RSC là mô hình component chạy server/build và compose qua protocol với Client Components.

### 21A. React DOM `browser()` trong React 19.3: opt-out SSR bằng Suspense thay vì đoán environment

Phần lớn component SSR phải tạo initial HTML tương thích với initial client render. Nhưng có component thực sự không thể tạo UI có nghĩa trên server, ví dụ nó cần `localStorage`, browser timezone hoặc một browser-only data source. Trước đây developer thường thêm `mounted` state trong Effect hoặc rải `typeof window !== "undefined"`, dễ tạo hai render path thiếu cấu trúc và dễ che hydration bug.

React DOM 19.3 thêm `browser()` để biểu đạt boundary này trực tiếp qua `use`:

```jsx
import {
  Suspense,
  use,
} from "react";
import { browser } from "react-dom";

function LocalTimeZone() {
  use(browser());

  const zone = new Intl.DateTimeFormat()
    .resolvedOptions()
    .timeZone;

  return <p>{zone}</p>;
}

function Page() {
  return (
    <Suspense fallback={<p>Đang xác định múi giờ...</p>}>
      <LocalTimeZone />
    </Suspense>
  );
}
```

Trên server, `use(browser())` suspend nên nearest Suspense fallback đi vào HTML. Trên client nó không suspend, vì vậy component tiếp tục render khi hydrate. Vì đây là `use`, call có thể nằm sau early return hoặc trong condition theo Rules của `use`; ví dụ nếu server đã có `initialData`, component có thể render ngay và chỉ opt-out SSR khi thiếu dữ liệu ban đầu.

Trade-off phải được nhìn rõ: opt-out nghĩa server không gửi content thật của subtree đó, nên có thể làm initial content/SEO kém hơn và đẩy work sang client. `browser()` vì vậy không phải cách “sửa nhanh mọi hydration mismatch”; trước tiên hãy làm render deterministic. Chỉ dùng khi browser environment thật sự là một phần của dữ liệu cần render.

## 22. Hydration mismatch

Initial client render phải tương thích server HTML. Các nguồn mismatch phổ biến:

```jsx
<div>{Date.now()}</div>
<div>{Math.random()}</div>
```

hoặc đọc browser-only state khi server không có. Hãy làm initial render deterministic hoặc dùng framework pattern thích hợp. `suppressHydrationWarning` chỉ là escape hatch phạm vi nhỏ, không phải cách che bug hệ thống.

### 22A. Debug hydration bằng evidence, không bằng việc thêm `suppressHydrationWarning`

Hydration bug thường chỉ xuất hiện ở production vì server và browser khác timezone, locale, cookie, extension, CDN mutation hoặc release artifact. Cách debug tốt là so ba thứ: **HTML server thực sự gửi**, **input serialized dùng cho initial client render**, và **output client ở lần render đầu tiên trước Effect**. Nếu ba lớp này không cùng một snapshot, React chỉ đang phơi ra inconsistency đã tồn tại.

Các nguồn cần kiểm tra theo thứ tự gồm dữ liệu nondeterministic (`Date.now`, random, ID tự sinh), locale/timezone, invalid HTML nesting bị browser tự sửa, conditional dựa vào `window`, cache trả hai version data khác nhau, và deployment nơi HTML cũ trỏ tới JS bundle mới. Đừng chỉ nhìn component stack; Network/View Source/CDN headers và release ID thường mới là evidence quyết định.

Một nguyên tắc production hữu ích là server render và initial client render phải cùng một **logical snapshot**. Sau hydration, Effect hoặc normal update có thể chuyển sang browser-specific state. Nếu component không thể tuân invariant đó một cách có nghĩa, `browser()`/Suspense hoặc framework client-only boundary mới là lựa chọn rõ ràng hơn.

## 23. Server Components

Server Components chạy trong server/build environment và không nhất thiết gửi code của chính chúng vào client bundle.

```jsx
async function ProductPage({ id }) {
  const product = await db.products.get(id);

  return (
    <article>
      <h1>{product.name}</h1>
      <AddToCartButton productId={id} />
    </article>
  );
}
```

`ProductPage` có thể chạy server; `AddToCartButton` là Client Component để có state/event browser.

Server Components có thể `await` trong render. Model RSC trong React 19 stable cho application usage, nhưng bundler/framework implementation APIs có versioning constraints riêng; app nên dùng framework hỗ trợ chính thức.

> ### Version Note — React 19 và RSC
>
> React 19 đưa React Server Components/Server Functions vào thế hệ production hiện đại, nhưng **application-facing model ổn định không đồng nghĩa implementation protocol cho bundler/framework là một API bất biến giữa mọi minor/patch**. Nếu dùng Next.js hoặc framework RSC khác, version framework và patch React Server DOM packages quan trọng không kém version `react` chính.

## 24. `'use client'` và `'use server'`

`'use client'` tạo client module boundary:

```jsx
"use client";

import { useState } from "react";

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
```

`'use server'` không đánh dấu Server Component. Nó đánh dấu Server Function trong môi trường hỗ trợ:

```jsx
async function updateUser(formData) {
  "use server";
  // ...
}
```

Server Component không cần directive `"use server"`.

## 24A. Server/Client boundary là dependency graph

Trong RSC, `'use client'` tạo module boundary; dependency dưới client boundary có khả năng đi vào client bundle. Vì vậy không import database SDK, filesystem hay secret-bearing module vào client graph. Props server → client phải tuân serialization contract; Server Function reference là trường hợp protocol riêng, không có nghĩa function JavaScript bất kỳ truyền được qua network.

Evolution đi từ SPA mọi component chạy client, qua SSR render HTML server rồi hydrate client, tới RSC nơi một phần component chỉ chạy server. Migration nên đặt interactive boundary nhỏ nhất hợp lý thay vì thêm `'use client'` lên root cho hết lỗi.

## 24B. SSR, hydration và RSC là các trục khác nhau

SSR trả HTML từ server để có initial content sớm; hydration gắn React client runtime vào HTML đó; React Server Components cho phép một phần component tree chạy server và truyền payload để compose với Client Components. Một app có thể SSR mà không dùng RSC, và RSC framework vẫn phải quyết định phần nào hydrate trên client.

Khi debug, cần hỏi đúng boundary: mismatch là vấn đề server HTML khác initial client render; bundle lớn là vấn đề client dependency graph; secret leak là vấn đề module boundary/serialization; waterfall có thể nằm ở routing/data architecture. Gọi tất cả là “SSR issue” làm migration và profiling thiếu chính xác.

### 24C. Context qua RSC boundary trong React 19.3

Server Component không thể tự gọi `createContext` để tạo một Context server-native. Nhưng từ React 19.3, nó có thể import một Context được khai báo trong module `'use client'` rồi render Context đó trực tiếp làm provider.

```jsx
// user-context.js
"use client";

import { createContext } from "react";

export const UserContext = createContext(null);
```

```jsx
// Layout.server.jsx
import { UserContext } from "./user-context.js";

export async function Layout({ children }) {
  const currentUser = await getCurrentUser();

  return (
    <UserContext value={currentUser}>
      {children}
    </UserContext>
  );
}
```

Trước đó framework/app thường cần một Client wrapper chỉ để nhận prop từ server rồi render provider. Capability mới giảm wrapper nhưng không xóa client boundary: Context vẫn được tạo từ module client và giá trị truyền qua boundary vẫn phải phù hợp serialization/security constraints. Đừng truyền database entity chứa secret hoặc object lớn chỉ vì provider syntax ngắn hơn.

## 25. Server Functions và security

Server Function phải được coi như public network surface dù syntax trông giống function call. Dữ liệu từ client luôn là untrusted input.

Không đủ an toàn:

```js
async function deleteUser(userId) {
  "use server";
  await db.user.delete(userId);
}
```

Cần authenticate, authorize resource/action, validate input, giới hạn error leakage và bảo vệ secrets. Serialized argument từ client không chứng minh user có quyền. Client UI có thể ẩn button nhưng authorization thật phải nằm ở server.

RSC ecosystem từng có security advisory quan trọng, vì vậy production framework/React package phải được patch theo advisory chính thức, không chỉ “đúng major version”.

### 25A. Trusted Types trong React 19.3: React hỗ trợ policy, không thay bạn sanitize

React vốn escape text node/attribute thông thường, nhưng XSS boundary thay đổi khi app cố ý đi vào injection sink như `innerHTML`. Browser Trusted Types cho phép CSP yêu cầu những sink này chỉ nhận object đã đi qua policy, chẳng hạn `TrustedHTML`, thay vì raw string.

Trước React 19.3, React có thể coerce Trusted Types object thành string trước khi đưa xuống DOM, làm browser mất evidence rằng value đã qua policy. React 19.3 truyền object Trusted Types xuống injection sink mà không phá type marker đó, nên app có thể dùng CSP như `require-trusted-types-for 'script'` cùng policy/sanitizer của mình.

Điều này **không có nghĩa `dangerouslySetInnerHTML` trở nên an toàn tự động**. React không chứng minh HTML của bạn sạch; Trusted Types cũng chỉ mạnh bằng policy tạo ra object trusted. Production security vẫn cần sanitize đúng context, CSP hợp lý, tránh URL/script sink nguy hiểm và audit third-party code. Hãy coi React 19.3 là sửa plumbing để browser security boundary hoạt động đúng, không phải một sanitizer mới.

## 26. Data architecture production

Một architecture khỏe mạnh phân biệt rõ:

```text
remote/server state -> query cache hoặc framework data layer
URL state           -> router/search params
form state          -> form abstraction/local state
UI ephemeral state  -> component state
shared client state -> Context/external store khi cần
derived state       -> tính từ source of truth
```

Quyết định “Redux, Zustand hay Context?” chỉ nên đặt sau khi phân loại state. Nhiều app không cần giant global store nếu server data đã ở query cache và navigation state đã ở URL.

## 27. State management decision framework

Local state là mặc định vì locality dễ hiểu và dễ xóa. Context phù hợp dependency/value theo subtree. Reducer phù hợp state transition phức tạp trong một scope. External store như Zustand/Redux phù hợp khi nhiều nhánh xa nhau cùng đọc/ghi client state, cần selector, middleware, devtools hoặc convention mạnh.

Redux Toolkit hợp với domain/action flow lớn và team cần cấu trúc chặt. Zustand nhẹ hơn nhưng convention do team tự quyết định nhiều hơn. Không nên tự xây HTTP cache bên trong global store khi server-state library đã giải quyết stale/retry/invalidation tốt hơn.

## 27A. State-management evolution

Flux/Redux giải quyết predictable shared state trong thời class. Hooks giảm nhu cầu container/HOC cho local logic; Context lo dependency theo subtree; query/router/form layers tách server, URL và form state khỏi global store. Redux không obsolete: external store vẫn phù hợp khi domain client state lớn, nhiều nhánh cùng đọc/ghi và cần selector, middleware, event log hoặc convention tổ chức mạnh. Chọn theo ownership/update topology, không theo thời thượng.

## 28. Component API design

API component nên composable và tránh boolean explosion.

Không tốt:

```jsx
<Card
  isBlue
  isCompact
  isClickable
  isLoading
  specialCase2
/>
```

Tốt hơn có thể dùng variant:

```jsx
<Card variant="info" size="compact" interactive />
```

hoặc composition:

```jsx
<Card>
  <Card.Header>...</Card.Header>
  <Card.Body>...</Card.Body>
</Card>
```

Boolean props nhiều tạo state space khổng lồ và combination vô nghĩa. API design phải cân bằng convenience với extensibility.

## 29. Các design pattern phổ biến

React hiện đại ưu tiên composition hơn inheritance. Pattern thường gặp gồm custom hooks, provider pattern, compound components, controlled component, headless component, render props và state reducer pattern.

HOC vẫn tồn tại trong code cũ/library:

```jsx
const Enhanced = withSomething(Component);
```

Nhưng custom Hook thường dễ compose hơn cho reusable stateful logic.

Render prop vẫn hữu ích khi consumer cần kiểm soát output:

```jsx
<DataProvider>
  {data => <View data={data} />}
</DataProvider>
```

## 30. Headless và compound components

Headless component quản lý behavior/state/accessibility nhưng không ép style. Compound component tạo API có quan hệ rõ:

```jsx
<Tabs defaultValue="account">
  <Tabs.List>
    <Tabs.Trigger value="account">Account</Tabs.Trigger>
    <Tabs.Trigger value="security">Security</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="account">...</Tabs.Content>
  <Tabs.Content value="security">...</Tabs.Content>
</Tabs>
```

Implementation có thể dùng Context nội bộ, roving tabindex, keyboard navigation và state machine. Đây là pattern mạnh cho design system.

## 31. Controlled và uncontrolled component API

Controlled:

```jsx
<Dialog open={open} onOpenChange={setOpen} />
```

Uncontrolled:

```jsx
<Dialog defaultOpen />
```

Controlled nghĩa parent là source of truth; uncontrolled nghĩa component giữ state nội bộ. Không nên chuyển qua lại hai mode mơ hồ trong cùng lifetime. Library phải document precedence và callback behavior.

## 32. Performance engineering

React performance không chỉ là re-render. Bottleneck lớn thường là network waterfall, initial bundle lớn, list hàng nghìn item, algorithm nặng, image/font, layout thrash hoặc backend latency.

Quy trình đúng: đo trải nghiệm, profile bằng React DevTools và browser Performance, xác định bottleneck, giảm work ở layer đúng, rồi đo lại. Memo một component 0.1 ms trong khi tải 4 MB JS là tối ưu sai chỗ.

## 32A. Performance cost model: render work, commit work và external work

Trước khi memoize, xác định bottleneck thuộc loại nào. **Render work** là thời gian gọi component và tính tree; **commit work** là DOM mutation, layout effect/ref work; **external work** gồm network, parse dữ liệu, image, third-party widget và browser layout/paint. `memo` không sửa request waterfall, còn code splitting không giúp một Effect loop vô hạn.

Một workflow tối ưu hợp lý là: tái hiện interaction chậm → đo bằng React DevTools Profiler và browser performance tools → xác định component hoặc external task chiếm thời gian → sửa architecture trước → chỉ thêm memoization khi identity ổn định và render thực sự đắt → đo lại. Performance optimization không được trở thành dependency cho correctness.

Các tối ưu structural thường thắng memoization rải rác: giữ state gần nơi dùng, tránh Effect chain set state, chia context theo volatility, virtualize list lớn, tránh render subtree không cần thiết, và đặt Suspense/code-split boundary theo interaction thực tế.

## 33. Profiling

React DevTools Profiler cho biết component render/commit cost và các thông tin liên quan. Browser Performance panel cần dùng khi bottleneck gồm scripting, layout, paint, network. Hãy profile production-like build vì development mode có Strict Mode/debug overhead.

### 33A. React Performance Tracks: nối Scheduler evidence với browser timeline

Từ React 19.2, Chrome DevTools Performance có React-specific tracks giúp nhìn scheduling thay vì chỉ thấy một khối JavaScript dài. **Scheduler track** cho biết work nào thuộc blocking/user interaction, work nào thuộc transition, update nào đang bị work priority khác chặn và React đang chờ paint ở đâu. **Components track** cho thấy component tree đang render hoặc chạy Effects, kèm các trạng thái như mount/blocked và thời gian tương ứng.

Điều này thay đổi cách debug câu “transition không giúp gì”. React DevTools Profiler trả lời tốt câu hỏi component nào render tốn thời gian; browser Performance trả lời main thread còn bận bởi layout/paint/third-party task nào; React Performance Tracks nối thêm câu hỏi scheduler đã phân loại và xen kẽ React work ra sao. Senior investigation nên đối chiếu cả ba thay vì nhìn một flame chart rồi đoán.

Một worked reasoning đơn giản: nếu Scheduler cho thấy transition work thường xuyên yield đúng cách nhưng INP vẫn xấu vì event handler tự parse 20 MB JSON trước khi gọi setter, đổi thêm `startTransition` không giải quyết được. Ngược lại, nếu CPU cost nằm trong một render subtree non-urgent và input bị cạnh tranh với nó, transition/structural split mới là hướng có evidence.

## 34. List virtualization

Danh sách hàng nghìn item không nên render toàn bộ nếu viewport chỉ thấy vài chục. Virtualization render một window gần viewport. Thư viện hiện hành như TanStack Virtual hoặc giải pháp tương tự có thể dùng tùy stack.

Cần kiểm tra dynamic row height, keyboard navigation, accessibility, sticky rows, browser find và measurement. Virtualization không “miễn phí”.

## 35. Referential equality và identity

Trong JavaScript:

```js
{} !== {}
(() => {}) !== (() => {})
```

Object/function mới có identity mới, ảnh hưởng dependency, memo và selector. Nhưng không vì vậy mà mọi function cần `useCallback`. Nếu child không memo và function không làm dependency cần stability thì callback memo thường không mang lợi ích.

React Compiler có thể tự xử lý nhiều memoization, nhưng identity contract với external system vẫn cần hiểu rõ.

## 35A. Memoization boundary trong thời React Compiler

`memo`, `useMemo` và `useCallback` đều có chi phí về dependency reasoning và cache bookkeeping. Chúng hữu ích khi một expensive subtree thường nhận cùng props, một calculation thực sự đắt, hoặc external API yêu cầu stable identity. Chúng không nên được dùng như nghi thức cho mọi object/function.

React Compiler có thể tự động hóa nhiều memoization, nhưng điều đó làm **purity và data flow** quan trọng hơn chứ không ít đi. Compiler không sửa state ownership sai, Effect loop, context value thay đổi vô ích hay network waterfall. Library cũng không thể giả định mọi consumer bật Compiler, nên public API vẫn cần identity contract rõ và benchmark trên runtime support thực tế.

## 36. Code splitting strategy

Không split từng component nhỏ. Boundary tốt thường theo route, feature nặng hoặc widget hiếm dùng.

```jsx
const AdminPage = lazy(() => import("./AdminPage.jsx"));
```

Preload/prefetch theo intent hoặc framework capability có thể giảm delay. Bundle analysis nên kiểm tra dependency lớn, duplicate package, locale data và dead code.

## 37. Accessibility production

Accessibility là behavior, không chỉ ARIA. Review phải kiểm tra semantic structure, heading hierarchy, keyboard, focus, screen-reader announcement, error association, contrast và reduced motion.

Dialog cần focus containment/trap phù hợp, focus restore, accessible title và escape semantics. Dùng primitive accessibility đã được kiểm chứng thường tốt hơn tự implement widget phức tạp.

## 38. Testing strategy production

Test theo risk. Critical flow cần integration/E2E; reducer/formatter có edge case cần unit; design system có thể cần visual regression; accessibility cần automated axe cộng manual keyboard/screen-reader testing.

Mock quá sâu tạo test “xanh” nhưng không phản ánh integration. Network mocking ở boundary HTTP thường tốt hơn mock từng custom Hook implementation.

## 39. TypeScript với React

Props:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary";
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
};

function Button({
  variant = "primary",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button data-variant={variant} disabled={disabled} onClick={onClick}>
      {children}
    </button>
  );
}
```

Discriminated union giúp loại impossible state:

```tsx
type LoadState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };
```

Ref:

```tsx
const inputRef = useRef<HTMLInputElement>(null);
```

Không cần dùng `React.FC` cho mọi component; typed props trực tiếp thường đơn giản hơn.

## 40. Version compatibility: React 16.8 → 19.3

Ở level Senior, versioning không nên chỉ là “version mới hơn có nhiều API hơn”. Mỗi mốc thay đổi một phần mental model hoặc compatibility surface.

| Mốc | Thay đổi đáng học | Ý nghĩa khi đọc code |
|---|---|---|
| React 16.8 | Hooks | Code hiện đại chuyển dần từ class lifecycle sang Function Component + Hooks. |
| React 17 | Release chuyển tiếp, gradual upgrade, modern JSX transform phổ biến | Nhiều code React 17 trông gần React 18 về component syntax nhưng entry root và batching vẫn khác. |
| React 18 | `createRoot`, automatic batching, transitions, `useDeferredValue`, `useId`, streaming SSR, Strict Mode checks | Đây là nền concurrency hiện đại. App dùng legacy `ReactDOM.render` không có đầy đủ semantics root mới. |
| React 18.3 | Warning bridge trước React 19 | Rất hữu ích cho migration vì chỉ ra API/deprecation phải sửa trước khi nâng major. |
| React 19.0 | Actions, `use`, `useActionState`, `useOptimistic`, function form Actions, ref-as-prop, Context shorthand, modern JSX transform required, removal của một số legacy APIs | Bắt đầu thế hệ async mutation/RSC API mới. |
| React 19.1 | Chủ yếu cải thiện server/RSC/prerender và độ ổn định của nhánh 19 | Ít thay đổi mental model phía beginner; vẫn phải theo patch nếu dùng RSC. |
| React 19.2 | `<Activity />`, `useEffectEvent`, `cacheSignal`, Performance Tracks, Partial Pre-rendering/server improvements | App/library phải kiểm tra minimum minor version nếu dùng các API này. |
| React 19.3 | Stable View Transitions, Fragment refs; React DOM `browser` và Trusted Types support; RSC Context capability mới | Baseline hiện tại của tài liệu. Các API 19.3 không nên vô tình lọt vào package tuyên bố support 19.0. |
| React Compiler 1.0 | Automatic memoization, stable từ 2025; version độc lập React core | Không đồng nhất version compiler với React. Có thể hỗ trợ nhiều React major theo configuration. |

### Cách đọc tutorial cũ

Nếu thấy `ReactDOM.render`, hãy nghĩ “pre-React-18 root API”. Nếu thấy Class Component với `componentDidMount`, đừng dịch máy móc từng lifecycle sang một `useEffect`; hãy xác định synchronization thật sự. Nếu thấy `forwardRef`, code chưa chắc cũ hoặc sai: đó vẫn là lựa chọn cần thiết cho compatibility React 18. Nếu thấy `useEffectEvent` hay `<Activity>`, project phải ít nhất ở React 19.2. Nếu thấy stable View Transition integration hoặc Fragment ref API mới, project cần React 19.3.

### Version và security không phải cùng một việc

React 19 từng có các security advisory nghiêm trọng liên quan React Server Components và các bản sửa được backport vào nhiều nhánh patch. Bài học production là không chỉ nói “chúng ta đang ở React 19.1/19.2”; phải theo **patch version đã được framework/React khuyến nghị**, đặc biệt khi dùng `react-server-dom-*`.

## 40A. Ma trận API cũ, trạng thái và cách thay thế

Bảng này dùng để tra cứu khi gặp code legacy. `Removed` nghĩa là API không còn được hỗ trợ ở version được nêu; `Deprecated` nghĩa là có thể còn hoạt động ở một số version nhưng không nên dùng cho code mới.

| API / pattern cũ | Thường gặp ở | Trạng thái | Thay thế / cách hiểu hiện đại |
|---|---|---|---|
| `React.createClass` | React 0.x–15 | Deprecated khỏi core từ 15.5 | ES6 class; hiện nay ưu tiên Function Component |
| mixins trong `createClass` | React cũ | Legacy | Composition, HOC/render props, Custom Hooks |
| `React.PropTypes` | Trước 15.5 | Deprecated 15.5 | package `prop-types`; với code mới thường TypeScript |
| `propTypes` trên Function Component | 15.x–18 | React 19 không còn xử lý | TypeScript/schema/runtime validation ở boundary |
| `defaultProps` trên Function Component | 15.x–18 | Removed behavior trong React 19 | default parameters |
| string refs `ref="x"` | React cũ | Deprecated 16.3, removed 19 | callback refs, `createRef`, `useRef` |
| `findDOMNode` | Class/library cũ | Deprecated 16.6, removed 19 | explicit DOM refs |
| legacy context `contextTypes`, `getChildContext` | Trước 16.3 | Deprecated 16.6, removed 19 | `createContext`, `contextType`, `useContext` |
| `componentWillMount` | Class cũ | Deprecated name; `UNSAFE_*` legacy | initialization + mount synchronization phù hợp |
| `componentWillReceiveProps` | Class cũ | Deprecated name; `UNSAFE_*` legacy | derive during render, reducer, controlled model, rare `getDerivedStateFromProps` |
| `componentWillUpdate` | Class cũ | Deprecated name; `UNSAFE_*` legacy | `componentDidUpdate`, `getSnapshotBeforeUpdate`, layout/effect logic |
| `ReactDOM.render` | React 17 trở xuống | Deprecated 18, removed 19 | `createRoot(...).render(...)` |
| `ReactDOM.hydrate` | SSR React 17 trở xuống | Deprecated 18, removed 19 | `hydrateRoot` |
| `unmountComponentAtNode` | ReactDOM legacy root | Deprecated 18, removed 19 | `root.unmount()` |
| render callback của `ReactDOM.render` | Legacy root | Không có one-to-one replacement | Effect/ref/callback theo semantics thực sự cần |
| `React.createFactory` | Pre-JSX / legacy | Deprecated 16.13, removed 19 | JSX / `createElement` |
| module pattern factory component | Rare legacy | Deprecated 16.9, removed 19 | Function Component bình thường |
| `react-dom/test-utils` helpers | test cũ | Hầu hết removed/deprecated trong 19 | `act` từ `react`, Testing Library |
| `react-test-renderer` | unit/component test cũ | Deprecated trong React 19 | Testing Library hoặc environment gần user hơn |
| `react-test-renderer/shallow` | shallow test | Removed khỏi React 19 package path | Tránh shallow nếu có thể |
| old JSX transform yêu cầu `import React` | React/toolchain cũ | React 19 yêu cầu modern transform | modern JSX transform |
| UMD React builds | script-tag legacy | React 19 ngừng phát hành UMD | ESM/CDN hoặc build tool |
| `element.ref` | element introspection | Deprecated React 19 | đọc `element.props.ref` nếu thật sự cần introspection |

### Cách dùng bảng này

Không nên nhìn cột “thay thế” như một bảng search-and-replace. Ví dụ `componentWillReceiveProps` có thể đã được dùng để đồng bộ prop vào state, gọi API, reset draft hoặc tính derived value; mỗi intent có một hướng migrate khác nhau. Senior migration luôn bắt đầu bằng việc xác định **semantics**, sau đó mới chọn API mới.

## 40B. Migration thực tế: cùng một feature qua ba thế hệ

Giả sử cần subscribe một room theo `roomId`.

### React Class Component

```jsx
class ChatRoom extends React.Component {
  componentDidMount() {
    this.connect(
      this.props.roomId
    );
  }

  componentDidUpdate(
    prevProps
  ) {
    if (
      prevProps.roomId !==
      this.props.roomId
    ) {
      this.disconnect();

      this.connect(
        this.props.roomId
      );
    }
  }

  componentWillUnmount() {
    this.disconnect();
  }

  connect(roomId) {
    this.connection =
      createConnection(roomId);

    this.connection.connect();
  }

  disconnect() {
    this.connection
      ?.disconnect();
  }

  render() {
    return <Chat />;
  }
}
```

### Function Component với Hooks

```jsx
function ChatRoom({
  roomId,
}) {
  useEffect(() => {
    const connection =
      createConnection(roomId);

    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <Chat />;
}
```

Hooks không chỉ “rút ngắn class”. Chúng gom logic của cùng một synchronization concern lại thay vì chia `connect`/`disconnect` qua ba lifecycle.

### React 19.2+ với `useEffectEvent`

Nếu Effect chỉ cần restart khi `roomId` đổi nhưng callback muốn đọc `theme` mới nhất:

```jsx
function ChatRoom({
  roomId,
  theme,
}) {
  const onConnected =
    useEffectEvent(() => {
      showToast(
        "Connected",
        theme
      );
    });

  useEffect(() => {
    const connection =
      createConnection(roomId);

    connection.on(
      "connected",
      onConnected
    );

    connection.connect();

    return () => {
      connection.disconnect();
    };
  }, [roomId]);

  return <Chat />;
}
```

Điểm cần học không phải “version mới luôn ngắn hơn”, mà là mỗi thế hệ React biểu đạt dependency và side effect chính xác hơn.

## 41. Senior Notes

**Ownership quan trọng hơn Hook.** Khi bug state xảy ra, hỏi dữ liệu thuộc ai trước khi đổi Hook.

**Effect là integration boundary.** Mỗi Effect nên có một external synchronization story rõ.

**Server state không phải global client state.** Query cache có stale/retry/invalidate semantics riêng.

**Design system là API product.** Component library có versioning, accessibility, composition và backward compatibility.

**Performance phải đo.** Memoization không có profiler evidence thường chỉ là phỏng đoán.

**Security boundary nằm ở server.** Client không tạo authorization.

**Framework matters.** RSC, router, cache và deployment semantics thường do framework quyết định; không nên gọi tất cả là “React behavior”.

## Checklist Advanced/Senior

Bạn nên có thể thiết kế app production với boundary rõ, chọn đúng local/context/store/server-state/URL state, giải thích concurrency/Suspense, viết optimistic mutation có failure semantics, hiểu SSR/hydration/RSC, profile bottleneck thật, thiết kế reusable component API, xử lý accessibility và test theo risk.

Bạn cũng phải phân biệt được API thuộc React core, React DOM, RSC hay framework trước khi đưa vào codebase.