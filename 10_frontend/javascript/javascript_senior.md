# JavaScript Senior — Runtime, Memory, Concurrency, Performance, Security và Architecture

> **Mục tiêu của phần này**: giúp developer đã hiểu JavaScript core có thể chịu trách nhiệm cho code production. Senior JavaScript không phải người nhớ nhiều API nhất; senior là người hiểu runtime behavior, quản lý lifecycle/resource, kiểm soát async/concurrency, đo performance, thiết kế security boundary, tổ chức architecture và debug production bằng evidence.
>
> Phần này nối trực tiếp từ Intermediate. Những concept như closure, `this`, prototype, Promise, event loop, state modeling và patterns được coi là nền tảng đã biết.

---

<!-- VERSION-GUIDE-BEGIN -->
# Version và compatibility ở level Senior: bốn lớp phải tách riêng

Ở level Senior, nói “feature này là JavaScript mới” là chưa đủ. Bạn phải tách **yearly standard snapshot**, **latest specification/proposal state**, **engine implementation**, và **deployment target thực tế**. Snapshot chính thức mới nhất hiện tại là **ECMAScript 2026, ECMA-262 17th edition**, được Ecma International phê duyệt ngày 30 tháng 6 năm 2026. Trong khi đó `tc39.es/ecma262` là tài liệu cập nhật liên tục và có thể chứa cả finished proposals đã Stage 4 sau snapshot gần nhất để chuẩn bị cho yearly snapshot tiếp theo.

Engine như V8, SpiderMonkey và JavaScriptCore có lịch triển khai riêng. Một feature có thể được engine triển khai trước khi yearly edition được xuất bản, nhưng một Android WebView embedded trong ứng dụng enterprise vẫn có thể không support nó nhiều năm sau. Vì thế câu hỏi production nên là: **feature đã final chưa; browser/Node/WebView targets của sản phẩm support đến đâu; build pipeline có thể transpile/polyfill phần nào; fallback có cần thiết không?**.

MDN thường dùng nhãn **Baseline** để mô tả độ phổ biến trên browser hiện đại. Baseline hữu ích hơn ECMAScript year khi đánh giá front-end compatibility, nhưng nó vẫn không thay target matrix của sản phẩm. “Baseline 2025” có thể vẫn quá mới đối với thiết bị doanh nghiệp khóa WebView cũ.

Stage của TC39 cũng phải được hiểu chính xác. Stage 3 là candidate đủ chín để implementation thử nghiệm rộng hơn. Stage 4 là finished proposal và là dấu mốc để proposal đi vào standard snapshot kế tiếp. Ví dụ **Temporal đạt Stage 4 vào tháng 7 năm 2026**, sau khi ES2026 đã được phê duyệt; vì vậy đừng gọi Temporal là “feature ES2026” chỉ vì nó hoàn tất trong năm 2026. Hãy gọi nó là post-ES2026 Stage-4/next-snapshot feature cho đến khi yearly snapshot tương ứng được xuất bản, đồng thời vẫn kiểm tra runtime support.

Senior cũng cần phân biệt **transpile syntax** với **polyfill runtime API**. Build tool có thể rewrite optional chaining thành syntax cũ, nhưng một built-in mới như `Promise.withResolvers()` hoặc `RegExp.escape()` cần implementation/polyfill tương ứng. Web APIs như Trusted Types, AbortSignal extensions hay Workers còn phụ thuộc browser platform và không thể được đánh giá chỉ bằng ECMA-262 edition.

Vì vậy version notes trong file Senior không nhằm biến tài liệu thành changelog. Chúng đánh dấu nơi version ảnh hưởng architectural choice, compatibility, security hoặc build strategy. Core ideas như ownership, cancellation, bounded concurrency, observability và failure modeling vẫn giữ nguyên dù ECMAScript tiếp tục ra yearly releases.
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — JavaScript Engine Mental Model

JavaScript source không được thực thi theo kiểu “browser đọc từng dòng và chạy ngay” một cách đơn giản. Engine như V8, SpiderMonkey hoặc JavaScriptCore parse source, tạo representation nội bộ, thực thi bằng interpreter/baseline compiler, thu thập runtime information và có thể JIT-optimize những hot paths.

Mental model high-level:

```text
Source Code
↓
Parse
↓
Internal Representation / AST-like structures
↓
Baseline execution
↓
Runtime profiling
↓
JIT optimization
↓
Optimized machine code
```

Bạn không cần phụ thuộc vào chi tiết một engine cụ thể. Điều quan trọng là hiểu engine có thể tối ưu code dựa trên assumptions và có thể deoptimize khi assumptions không còn đúng.

### Senior rule

Không micro-optimize dựa trên blog “V8 trick” nếu profiler chưa chứng minh hotspot. Stable data contracts, algorithms đúng và architecture rõ thường cho lợi ích lớn hơn hidden-engine tricks.

---

# Chương 2 — Parsing, startup work và top-level side effects

Khi module được load, top-level code chạy trong quá trình module evaluation.

```js
const index = buildHugeSearchIndex();
```

Nếu `buildHugeSearchIndex()` tốn 500ms, startup bị chậm dù feature chưa dùng index.

Lazy initialization:

```js
let index;

function getIndex() {
  index ??= buildHugeSearchIndex();
  return index;
}
```

Trade-off là chuyển cost từ startup sang first-use.

### Programming pattern — Lazy Initialization

Lazy init tốt khi resource expensive và có thể không được dùng. Nhưng nếu user chắc chắn cần ngay sau startup, lazy chỉ dời latency sang interaction đầu tiên. Senior phải tối ưu theo UX path, không theo metric đơn lẻ.

---

# Chương 3 — JIT, Shapes và predictable data

Modern engines thường optimize object access dựa trên internal shapes/hidden-class-like structures. Bạn không cần biết tên internal chính xác của từng engine, nhưng cần hiểu object được xây nhất quán thường dễ optimize hơn object thay shape ngẫu nhiên.

Consistent factory:

```js
function createUser(id, name) {
  return {
    id,
    name,
    active: true
  };
}
```

Thay vì nhiều call sites tạo cùng semantic object với property order/shape khác nhau và types thay đổi liên tục.

### Senior note

Stable shape là lợi ích phụ. Lý do chính vẫn là contract rõ, dễ maintain và dễ validate. Không reorder properties chỉ để chase microbenchmark.

---

# Chương 4 — Inline cache và megamorphic call-sites ở mức khái niệm

Property access `user.name` xảy ra hàng triệu lần trong app. Engine có thể cache lookup strategy dựa trên observed shapes. Nếu một call-site luôn nhận cùng shape, optimization dễ hơn. Nếu nhận rất nhiều object shapes không liên quan, engine có thể fallback sang generic path.

Takeaway không phải “tránh polymorphism”. Takeaway là nếu một function nhận 20 kinds of unrelated objects, architecture/data modeling có thể đã quá broad. Fix design trước khi nghĩ JIT.

---

# Chương 5 — Deoptimization và nguyên tắc profile-before-optimize

Optimized assumptions có thể bị invalidated khi types/shapes/prototype behavior thay đổi. Nhưng deopt là implementation detail. Production optimization phải theo quy trình:

```text
measure
↓
identify hotspot
↓
form hypothesis
↓
change
↓
measure again
```

Nếu code unreadable hơn để tiết kiệm vài nanoseconds ở path không quan trọng, đó là optimization sai.

---

# Chương 6 — Memory Model và Reachability

Garbage Collector không biết “developer không còn cần object”. Nó chỉ biết object còn reachable từ roots hay không. Roots có thể gồm global references, call stack, active closures, DOM/runtime references, callbacks và các host resources.

```js
let user = {
  id: 1,
  hugeData: new Array(1_000_000)
};

user = null;
```

Nếu không còn reference khác, object có thể trở thành collectible. Nhưng GC timing không deterministic.

### Senior mental model

Memory leak trong garbage-collected language thường là **accidental reachability**: object vẫn còn một đường reference từ root dù business đã “không dùng nữa”.

---

# Chương 7 — Garbage Collection: điều cần biết và điều không nên đoán

Modern engines có generational/incremental/concurrent strategies khác nhau. Bạn không cần thuộc thuật toán GC cụ thể để viết application code tốt.

Bạn cần biết ba điều: allocation có cost, GC có cost, và timing GC không phải API contract. Không viết logic kiểu “đặt reference null rồi GC chắc chắn chạy trong 2 giây”. Không dùng finalizer để đảm bảo business cleanup.

---

# Chương 8 — Memory Leaks phổ biến trong frontend

Các leak phổ biến gồm event listener không remove, timer không clear, subscription không unsubscribe, Map/cache tăng vô hạn, detached DOM còn reference, Worker không terminate, WebSocket không close, closure giữ data lớn, pending async lifecycle tiếp tục giữ references.

Listener leak:

```js
function mount() {
  window.addEventListener(
    "resize",
    handleResize
  );
}
```

Nếu mount nhiều lần mà không cleanup:

```js
function unmount() {
  window.removeEventListener(
    "resize",
    handleResize
  );
}
```

Timer:

```js
const intervalId = setInterval(
  refresh,
  5000
);
```

cleanup:

```js
clearInterval(intervalId);
```

### Senior pattern — Resource Ownership

Ai tạo resource phải biết ai sở hữu và khi nào release. Lifecycle không nên phụ thuộc vào “developer nhớ cleanup”. API tốt làm cleanup path explicit.

---

# Chương 9 — WeakRef, FinalizationRegistry và vì sao chúng là niche tools

> **Version note — ES2021:** `WeakRef` và `FinalizationRegistry` được chuẩn hóa ở ES2021, mới hơn nhiều so với WeakMap/WeakSet ES2015. Support không phải lý do để dùng chúng; correctness vẫn không được phụ thuộc vào thời điểm GC/finalizer.

`WeakRef` cho phép giữ weak reference:

```js
const ref = new WeakRef(object);
const value = ref.deref();
```

Value có thể là object hoặc `undefined` nếu object đã bị GC.

`FinalizationRegistry` có thể nhận notification khi object được collected, nhưng timing không guarantee. Nó không phù hợp để release critical lock, payment state hay resource cần deterministic cleanup.

### Senior rule

Nếu business correctness phụ thuộc object “chắc còn sống” hoặc finalizer “chắc chạy”, design sai. Weak references chỉ phù hợp cho optional cache/metadata-like scenarios nơi absence vẫn hợp lệ.

---

# Chương 10 — Explicit Resource Management và deterministic cleanup

> **Version/proposal note:** Explicit Resource Management (`using`, `await using`, `Symbol.dispose`, `DisposableStack`...) là nhóm feature rất mới. Trước khi dùng production, hãy kiểm tra snapshot/proposal status hiện hành và browser/runtime support, đặc biệt với WebView. Đừng đánh đồng Stage 4/post-snapshot với universal availability.

JavaScript hiện đại có explicit resource-management concepts như `using`, `await using`, `Symbol.dispose`, `Symbol.asyncDispose`, `DisposableStack` và `AsyncDisposableStack` ở runtimes hỗ trợ.

Concept:

```js
{
  using resource = acquireResource();
  // use resource
}
// resource disposed at scope exit
```

Custom disposable:

```js
class Subscription {
  constructor(unsubscribe) {
    this.unsubscribe = unsubscribe;
  }

  [Symbol.dispose]() {
    this.unsubscribe();
  }
}
```

### Senior note

Feature này giúp deterministic cleanup nhưng không thay thế ownership design. Trong browser/WebView enterprise cũ, luôn check runtime/toolchain compatibility trước khi áp dụng syntax mới.

---

# Chương 11 — Event Loop sâu hơn và rendering opportunities

Browser event loop phối hợp tasks, microtasks và rendering. Simplified mental model:

```text
run a task
↓
run synchronous JS
↓
drain microtasks
↓
rendering opportunity
↓
next task
```

Nếu một task chạy 300ms synchronous, browser không thể phản hồi input/render mượt trong thời gian đó.

```js
const start = performance.now();

while (
  performance.now() - start < 300
) {
}
```

Result có thể là input lag và animation freeze.

### Senior note

`async function` không tự làm CPU-heavy loop non-blocking. Nếu computation synchronous nằm trong async function, nó vẫn block main thread cho tới khi code yield.

---

# Chương 12 — Long Tasks và chunking

Giả sử xử lý 100.000 records:

```js
for (const item of hugeData) {
  expensiveProcess(item);
}
```

Nếu task quá dài, UI freeze. Các strategy gồm algorithm improvement, chunking, Web Worker, lazy processing hoặc virtualization.

Illustrative chunking:

```js
async function processInChunks(
  items,
  chunkSize = 100
) {
  for (
    let i = 0;
    i < items.length;
    i += chunkSize
  ) {
    processChunk(
      items.slice(
        i,
        i + chunkSize
      )
    );

    await new Promise(
      (resolve) =>
        setTimeout(resolve, 0)
    );
  }
}
```

Đây chỉ là strategy minh họa; scheduling production cần cân nhắc UX, task priorities và available APIs.

---

# Chương 13 — Main-thread budget và performance thinking

Senior không chỉ nhìn Big-O. Một O(n) loop vẫn có thể chậm nếu n lớn và mỗi iteration expensive. Câu hỏi phải là: n bao nhiêu, chạy khi nào, trên device nào, có đang block input không, có thể precompute/worker/lazy không?

Performance là interaction giữa algorithm, workload, device và scheduling.

---

# Chương 14 — `requestAnimationFrame` và visual scheduling

`requestAnimationFrame` schedule callback cho visual update trước rendering opportunity phù hợp.

```js
function animate() {
  position += velocity;

  element.style.transform =
    `translateX(${position}px)`;

  requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
```

Animation logic nên dùng elapsed time nếu cần consistency giữa displays/frame rates.

### Senior note

`rAF` không phải exact 16.67ms timer. Background tabs bị throttle và refresh rate thiết bị khác nhau.

---

# Chương 15 — Web Workers: chuyển CPU work khỏi main thread

Worker chạy JavaScript ở thread riêng và không access DOM trực tiếp.

Main:

```js
const worker = new Worker(
  "./worker.js",
  {
    type: "module"
  }
);

worker.postMessage({
  type: "PROCESS",
  payload: data
});

worker.onmessage = (event) => {
  render(event.data);
};
```

Worker:

```js
self.onmessage = (event) => {
  const result = expensiveCompute(
    event.data.payload
  );

  self.postMessage(result);
};
```

Worker phù hợp CPU-heavy parsing, search/indexing, image/data processing. Nó không làm network fetch “nhanh hơn” chỉ vì ở thread khác.

### Trade-offs

Worker startup, message serialization và memory duplication có cost. Không spawn worker cho tiny operation.

---

# Chương 16 — Structured Clone và Transferable Objects

> **Version note:** Structured clone là web/platform algorithm đã tồn tại lâu; ES2024 chuẩn hóa thêm các resizable/transfer-related ArrayBuffer facilities ở language built-ins. `structuredClone()` bản thân có compatibility timeline của host/global API, nên không nên gán toàn chương này cho một ES year duy nhất.

`structuredClone()` clone nhiều JavaScript types tốt hơn JSON và hỗ trợ cycles.

```js
const copy = structuredClone(original);
```

Khi chuyển large binary data giữa worker/main, copy có thể expensive. Một số objects như ArrayBuffer có thể transfer ownership:

```js
worker.postMessage(
  { buffer },
  [buffer]
);
```

Sau transfer, original buffer có thể bị detached.

### Senior pattern — Move instead of Copy

Useful cho large binary payload/image/data processing. Nhưng ownership sau transfer phải rõ.

---

# Chương 17 — SharedArrayBuffer và Atomics: khi message passing không đủ

> **Version note — ES2017 core:** Shared Memory và Atomics được đưa vào ES2017. Trên web, `SharedArrayBuffer` còn chịu security/cross-origin-isolation requirements của web platform; “nằm trong ECMAScript” chưa đủ để kết luận deployment dùng được.

`SharedArrayBuffer` cho nhiều agents/workers access cùng memory. Điều này mở ra race conditions và memory-ordering complexity.

```js
const buffer = new SharedArrayBuffer(4);
const view = new Int32Array(buffer);

Atomics.add(view, 0, 1);
```

Shared memory chỉ nên dùng khi performance use case thật sự cần. Với phần lớn frontend, message passing dễ reasoning và an toàn hơn.

### Security/platform note

Shared memory trên web còn liên quan cross-origin isolation requirements trong nhiều scenarios.

---

# Chương 18 — Streams và vì sao load toàn bộ data trước không luôn tốt

Streams xử lý data theo chunks.

```js
const response = await fetch(url);
const reader = response.body.getReader();

while (true) {
  const { value, done } = await reader.read();

  if (done) {
    break;
  }

  processChunk(value);
}
```

Benefits: lower peak memory, progressive processing và latency tốt hơn cho large payloads.

Web Streams có `ReadableStream`, `WritableStream`, `TransformStream`. Senior cần hiểu producer/consumer relationship và backpressure.

---

# Chương 19 — Backpressure

Backpressure xảy ra khi producer tạo data nhanh hơn consumer xử lý. Nếu queue cứ tăng:

```text
memory tăng
latency tăng
GC pressure tăng
```

Stream APIs có mechanism để consumer signal pace. Cùng concept xuất hiện trong event queues, network pipelines và background jobs.

### Senior rule

Unbounded queue là một dạng memory leak có logic. Mọi thứ có thể tăng mãi — queue, cache, retry, concurrency, logs — cần boundary.

---

# Chương 20 — Async Iterators và streaming abstractions

Async generator có thể model paginated/streaming source:

```js
async function* pages() {
  let page = 1;

  while (true) {
    const result = await loadPage(page);

    if (result.items.length === 0) {
      return;
    }

    yield result.items;
    page += 1;
  }
}
```

Consumer:

```js
for await (const items of pages()) {
  process(items);
}
```

Async iteration cho consumer kiểm soát pace tốt hơn một API push vô hạn.

---

# Chương 21 — Bounded Concurrency

Đây là distinction rất quan trọng. `Promise.all(items.map(apiCall))` start toàn bộ operations gần như cùng lúc. Với 50.000 items, bạn có thể tạo 50.000 requests/tasks.

Cần concurrency limit:

```js
async function mapLimit(
  items,
  limit,
  worker
) {
  const results = new Array(
    items.length
  );

  let nextIndex = 0;

  async function run() {
    while (true) {
      const index = nextIndex;
      nextIndex += 1;

      if (index >= items.length) {
        return;
      }

      results[index] = await worker(
        items[index],
        index
      );
    }
  }

  const workers = Array.from(
    {
      length: Math.min(
        limit,
        items.length
      )
    },
    run
  );

  await Promise.all(workers);
  return results;
}
```

### Senior note

Concurrency limit khác rate limit. More concurrency không luôn faster; server/network/resource bottleneck quyết định optimum.

---

# Chương 22 — Cancellation Architecture

Cancellation nên đi xuyên abstraction layers thay vì service tự giữ hidden cancellation state nếu caller mới là owner lifecycle.

```js
async function loadUser(
  id,
  { signal } = {}
) {
  const response = await fetch(
    `/api/users/${id}`,
    { signal }
  );

  return response.json();
}
```

Caller:

```js
const controller = new AbortController();

loadUser(1, {
  signal: controller.signal
});

controller.abort();
```

### Composition

Modern AbortSignal APIs có thể compose timeout/manual cancellation ở runtimes hỗ trợ. Dù API cụ thể nào, architecture principle vẫn là caller sở hữu lifetime và downstream nhận signal.

---

# Chương 23 — Debounce và Throttle

Debounce đợi event im lặng một khoảng thời gian rồi chạy. Search input là example điển hình.

```js
function debounce(fn, delay) {
  let timeoutId;

  return (...args) => {
    clearTimeout(timeoutId);

    timeoutId = setTimeout(
      () => fn(...args),
      delay
    );
  };
}
```

Throttle giới hạn tần suất chạy, ví dụ scroll/mousemove.

### Senior note

Production debounce có thể cần leading/trailing/cancel/flush/maxWait. Nếu stack đã có implementation mature, đừng tự viết bản phức tạp rồi tạo subtle bug.

---

# Chương 24 — Retry, Exponential Backoff và Jitter

Naive retry ngay lập tức có thể làm server đang overload càng overload. Exponential backoff tăng delay:

```text
300ms
600ms
1200ms
2400ms
```

Jitter thêm randomness để hàng nghìn clients không retry đồng bộ.

```js
const delay =
  baseDelay * 2 ** attempt;

const jitter =
  Math.random() * delay * 0.25;
```

### Senior rule

Retry chỉ cho transient/retryable failures. Respect server hints như `Retry-After` khi contract hỗ trợ. Retry loop cũng phải cancellable.

---

# Chương 25 — Idempotency và vì sao retry payment rất nguy hiểm

Idempotent operation có thể repeat mà effect tương đương một lần. GET thường có idempotent intent. Payment creation hoặc transfer không thể blind retry nếu server có thể đã nhận request nhưng response bị mất.

Backend có thể hỗ trợ idempotency key. Frontend retry strategy phải hiểu endpoint semantics, không chỉ HTTP status.

### Senior note

“Request failed” không luôn có nghĩa “server chưa làm gì”. Network failure có thể xảy ra sau khi side effect đã commit server-side.

---

# Chương 26 — Circuit Breaker và Bulkhead concepts

Circuit breaker có states như closed/open/half-open. Khi dependency fail liên tục, system fail fast thay vì tiếp tục hammer dependency.

Browser app ít cần full circuit breaker như backend, nhưng concept hữu ích cho polling/native bridge/third-party SDK.

Bulkhead là failure isolation: analytics failure không được block payment nếu analytics non-critical; third-party widget lỗi không làm main flow crash.

### Senior note

Resilience pattern chỉ có giá trị nếu match failure mode. Đừng implement circuit breaker để “enterprise-looking”.

---

# Chương 27 — Cache Architecture

Cache cần trả lời: cache gì, key là gì, TTL bao lâu, invalidation khi nào, max size bao nhiêu, stale data có acceptable không, source of truth ở đâu.

Simple TTL cache:

```js
function createCache({ ttlMs }) {
  const map = new Map();

  return {
    get(key) {
      const entry = map.get(key);

      if (!entry) {
        return undefined;
      }

      if (
        Date.now() > entry.expiresAt
      ) {
        map.delete(key);
        return undefined;
      }

      return entry.value;
    },

    set(key, value) {
      map.set(key, {
        value,
        expiresAt: Date.now() + ttlMs
      });
    }
  };
}
```

### Senior note

Cache invalidation là correctness problem, không chỉ performance. Với data nhạy cảm như balance/permission, stale cache có thể nguy hiểm.

---

# Chương 28 — Memoization khác Cache như thế nào?

Memoization thường cache pure/deterministic function output theo input. Cache là concept rộng hơn, có TTL, stale semantics, authorization scope, source-of-truth concerns.

Đừng gọi mọi Map là “memoization”. Network cache và computed selector cache có failure modes rất khác nhau.

---

# Chương 29 — HTTP Cache và dùng platform trước custom cache

Browser/HTTP caching có `Cache-Control`, `ETag`, `Last-Modified`, `304`, `max-age`, `no-cache`, `no-store`. Nếu HTTP cache đã giải quyết static/resource/data use case, custom JS cache có thể chỉ thêm complexity.

Senior ưu tiên platform mechanisms trước khi tự xây cache nếu semantics phù hợp.

---

# Chương 30 — Stale-While-Revalidate concept

SWR-like flow:

```text
show cached/stale data immediately
↓
fetch fresh data
↓
update UI
```

Tốt cho content/profile/list nơi stale data ngắn hạn acceptable. Không phù hợp nếu stale permission hoặc transaction balance dẫn tới quyết định sai.

---

# Chương 31 — Performance Measurement: đo trước khi tối ưu

Dùng `performance.now()` cho duration:

```js
const start = performance.now();
run();
const duration = performance.now() - start;
```

Performance marks:

```js
performance.mark("load-start");

await load();

performance.mark("load-end");

performance.measure(
  "load-duration",
  "load-start",
  "load-end"
);
```

Microbenchmarks dễ bị JIT, GC, warmup và unrealistic workload làm lệch. User-perceived scenario quan trọng hơn tiny loop benchmark.

---

# Chương 32 — Layout, Paint, Composite và Layout Thrashing

High-level rendering pipeline:

```text
style
↓
layout
↓
paint
↓
composite
```

Interleave layout read/write:

```js
for (const item of items) {
  const width = item.offsetWidth;
  item.style.width =
    `${width * 2}px`;
}
```

có thể force repeated layout.

Better batch reads:

```js
const widths = items.map(
  (item) => item.offsetWidth
);

for (
  let i = 0;
  i < items.length;
  i += 1
) {
  items[i].style.width =
    `${widths[i] * 2}px`;
}
```

### Senior note

Modern browsers optimize nhiều thứ. Đừng cargo-cult “DOM luôn chậm”; profile realistic page.

---

# Chương 33 — Large DOM và virtualization

Render 100.000 rows vào DOM thường tạo cost layout, memory và interaction. Virtualization chỉ render visible window + buffer.

Concept:

```text
100,000 data rows
↓
viewport cần 30 rows
↓
render khoảng 40-60 rows
```

Đây là architecture optimization lớn hơn micro-optimizing loop syntax.

---

# Chương 34 — High-frequency events

Events như scroll, resize, pointermove có thể fire rất nhiều. Strategies gồm throttle/debounce, passive listeners khi đúng, rAF cho visual work và delegation.

```js
window.addEventListener(
  "scroll",
  handleScroll,
  {
    passive: true
  }
);
```

`passive: true` nói listener không gọi `preventDefault`; dùng sai sẽ làm behavior khác.

---

# Chương 35 — Network Performance và request waterfall

Independent requests không nên vô tình chạy sequential:

```js
const a = await loadA();
const b = await loadB();
const c = await loadC();
```

Nếu independent:

```js
const [a, b, c] = await Promise.all([
  loadA(),
  loadB(),
  loadC()
]);
```

Nhưng parallelism cũng cần limit nếu số lượng lớn. Network performance còn phụ thuộc payload size, compression, caching, duplicate requests, request dependency graph và backend latency.

---

# Chương 36 — Bundle Strategy, Code Splitting và Lazy Loading

> **Version note:** Static modules có nền từ ES2015; dynamic `import()` thuộc ES2020; import attributes/JSON-module support thuộc ES2025. Code splitting và tree shaking là build-tool behavior, không phải guarantee trực tiếp của ECMAScript.

Dynamic import:

```js
const { openEditor } = await import(
  "./editor.js"
);
```

Bundler có thể tạo separate chunk. Lợi ích initial bundle nhỏ; trade-off first-use latency/chunk failure complexity.

Tree shaking loại unused exports khi static analysis cho phép. Side effects, CommonJS/dynamic behavior có thể hạn chế tree shaking.

### Senior note

Tree shaking là bundler behavior, không phải guarantee của JavaScript language. Bundle strategy phải đo trên real loading waterfall.

---

# Chương 37 — Serialization Cost

`JSON.stringify` và `JSON.parse` là synchronous CPU work. Large payload có thể block main thread.

Cross-worker structured clone cũng có cost. Transferable giúp một số binary cases.

Nếu serialization cost lớn, xem xét smaller payload, pagination, streams, workers hoặc binary representation tùy use case.

---

# Chương 38 — Security Mental Model

Security boundary bắt đầu từ assumption: bất kỳ dữ liệu nào từ user, URL, storage, network, `postMessage`, third-party script hoặc native bridge đều có thể malformed hoặc malicious.

Mental model:

```text
source
↓
transformations
↓
sink
↓
privilege/effect
```

Senior phải biết data đi vào từ đâu và cuối cùng được dùng ở sink nào.

---

# Chương 39 — XSS và DOM XSS

Dangerous:

```js
element.innerHTML = userInput;
```

Safer plain text:

```js
element.textContent = userInput;
```

Sources có thể là `location.search`, `location.hash`, API response, localStorage, postMessage. Sinks gồm `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, eval-like APIs.

DOM XSS không cần backend template; chỉ cần frontend đưa untrusted string vào executable/HTML sink.

### Senior rule

API response không tự trusted chỉ vì “do server mình trả”. Compromised data, stored payload hoặc backend escaping assumptions vẫn có thể tạo XSS.

---

# Chương 40 — CSP và defense-in-depth

Content Security Policy là browser security control qua HTTP header, giúp giới hạn scripts/styles/resources và giảm impact của XSS.

Strict CSP thường dựa trên nonce/hash và hạn chế unsafe inline script. Deploy cần report-only/testing strategy vì CSP sai có thể break app.

### Senior note

CSP không thay safe rendering. Nó là defense-in-depth, không phải lý do để tiếp tục dùng unsafe sinks.

---

# Chương 41 — Trusted Types

> **Platform version note:** Trusted Types là Web security API/CSP integration, không phải ECMAScript language feature. Support phụ thuộc browser/WebView và deployment policy, nên target runtime quan trọng hơn ES edition.

Trusted Types giúp kiểm soát dangerous DOM injection sinks. Mental model:

```text
untrusted string
↓
approved policy/sanitizer
↓
TrustedHTML-like value
↓
dangerous sink
```

Nếu enforce đúng, raw string assignment vào protected sink bị chặn.

### Senior note

Trusted Types policy viết sai vẫn có thể nguy hiểm. Tốt nhất giảm số dangerous sinks trước, sau đó dùng policy có kiểm soát.

---

# Chương 42 — Prototype Pollution

Unsafe dynamic property assignment/deep merge có thể cho attacker chạm keys như `__proto__`, `constructor`, `prototype`.

```js
function setValue(
  target,
  key,
  value
) {
  target[key] = value;
}
```

Nếu `key` arbitrary external input, cần schema/key validation.

Defenses gồm validate allowed keys, tránh generic unsafe deep merge, dùng Map cho arbitrary dictionaries khi phù hợp, Object.create(null) trong một số cases, keep dependencies updated.

### Senior note

Prototype pollution là lý do prototype internals từ Intermediate có security value thực tế.

---

# Chương 43 — CSRF mental model

CSRF lợi dụng browser tự gửi credentials/cookies tới target origin để thực hiện state-changing request ngoài ý muốn user.

Mitigations thuộc architecture backend/browser: SameSite cookies, CSRF tokens, Origin/Referer checks, API design. Frontend cần gửi token/header theo contract, nhưng backend phải enforce trust boundary.

---

# Chương 44 — Token Storage: không có câu trả lời một dòng

“localStorage luôn xấu” hoặc “cookie luôn tốt” đều quá đơn giản. Trade-off phụ thuộc XSS threat model, CSRF model, same-origin architecture, refresh-token design, backend support và hybrid container.

Senior không chọn token storage bằng blog snippet; nó là system security decision.

---

# Chương 45 — `postMessage` Security

Sender:

```js
window.postMessage(
  data,
  "https://trusted.example.com"
);
```

Tránh `"*"` cho sensitive data.

Receiver:

```js
window.addEventListener(
  "message",
  (event) => {
    if (
      event.origin !==
      "https://trusted.example.com"
    ) {
      return;
    }

    validateMessage(event.data);
  }
);
```

Cần validate `origin`, `source`, message type/schema và authorization/capability. Origin đúng không tự chứng minh operation requested là allowed.

---

# Chương 46 — Native Bridge / WebView Security Boundary

Hybrid app bridge có privileges vượt web page. Nếu web có thể gọi native method để mở camera, eKYC, file system hoặc payment, đó là privileged API.

Wrap bridge:

```js
const kycBridge = {
  start(params) {
    validateKycParams(params);
    return nativeBridge.startKyc(
      params
    );
  }
};
```

Questions senior phải hỏi: page/origin nào được gọi bridge, payload được validate ở đâu, navigation restriction có ở native side không, callback/deep link có request ID không, bridge expose capabilities tối thiểu chưa.

---

# Chương 47 — `eval`, `Function` và dynamic code execution

Avoid:

```js
eval(userInput);
new Function(userInput);
```

Risks gồm code injection, CSP incompatibility, hard-to-audit flow và optimization/debug problems.

Nếu cần dynamic behavior, thường dùng data-driven strategy registry/parser/config thay vì dynamic code execution.

---

# Chương 48 — RegExp Safety

> **Version note — ES2025:** `RegExp.escape()` được chuẩn hóa ở ES2025 để escape string dùng như literal trong dynamic RegExp. Nó xử lý nhiều edge cases hơn helper tự viết; với WebView cũ, hãy dùng maintained polyfill/helper thay vì tự thêm backslash vài ký tự.

Dynamic regex từ user input:

```js
new RegExp(userInput);
```

có thể thay semantics hoặc throw invalid pattern. Với intent literal search, modern runtimes có `RegExp.escape()`; older targets cần compatible escaping strategy.

Ngoài injection còn có ReDoS/catastrophic backtracking khi pattern developer viết có nested ambiguous quantifiers.

### Senior note

Nếu chỉ cần substring search, `includes()` thường đơn giản và safer hơn regex.

---

# Chương 49 — Supply-chain Security

Third-party package chạy với privileges của app. Risks: malicious package, compromised maintainer, typosquatting, vulnerable transitive dependency, postinstall scripts, CDN compromise.

Practices: lockfile, dependency review, vulnerability scanning, update policy, giảm random micro-packages, package provenance/reputation, SRI khi phù hợp cho CDN resources.

Senior hiểu dependency không chỉ là convenience; nó là trusted code added vào attack surface.

---

# Chương 50 — API Design: public surface phải nhỏ và khó dùng sai

Một API tốt trả lời rõ inputs, outputs, mutability, errors, cancellation, lifecycle, ownership.

```js
export function createUserService({
  repository,
  logger
}) {
  return {
    load,
    update
  };
}
```

Không export mọi helper internal. Public API nhỏ cho phép refactor implementation mà không phá consumers.

### Senior question

Caller cần biết gì? Caller có thể misuse gì? Resource ai sở hữu? Operation cancel thế nào? Error contract là gì?

---

# Chương 51 — Module Boundaries và Dependency Direction

Feature structure:

```text
user/
  domain.js
  api.js
  service.js
  view.js
  index.js
```

Consumer import public API từ `index.js`, không deep-import arbitrary internals.

Dependency direction lý tưởng thường giữ domain/pure logic không phụ thuộc DOM/fetch/framework khi benefit rõ.

Bad:

```js
// domain/pricing.js
import {
  getCurrentUser
} from "../api.js";
```

Better:

```js
function calculatePrice(
  order,
  user
) {
}
```

Caller đưa data vào.

---

# Chương 52 — Domain Modeling

Primitive soup:

```js
transfer(
  from,
  to,
  value,
  status,
  type,
  flag
);
```

Khó hiểu. Cohesive object:

```js
createTransfer({
  sourceAccount,
  destinationAccount,
  amount,
  currency
});
```

Domain modeling tập trung identities, valid states, transitions, units và invariants.

### Senior note

Architecture không bắt đầu bằng folder structure. Nó bắt đầu bằng boundaries và dependencies phản ánh domain.

---

# Chương 53 — State Machines cho complex UI flow

eKYC/payment/multi-step form có nhiều states và transitions. Explicit state machine:

```text
idle
↓ START
opening
↓ OPENED
waiting
├ SUCCESS → success
└ FAIL    → error
```

Object transition table:

```js
const transitions = {
  idle: {
    START: "opening"
  },

  opening: {
    OPENED: "waiting",
    FAIL: "error"
  },

  waiting: {
    SUCCESS: "success",
    FAIL: "error"
  }
};
```

State machine giảm impossible transitions và giúp test flow.

---

# Chương 54 — Event-driven Architecture: lợi ích và chi phí

Events hữu ích khi nhiều consumers phản ứng với “something happened”. Nhưng event-driven systems có hidden flow, ordering assumptions, duplicate handling và debugging complexity.

Senior rule: dùng direct function call khi direct dependency rõ và đơn giản. Event không tự làm architecture tốt hơn.

---

# Chương 55 — Repository / Gateway và Anti-Corruption Layer

Repository boundary:

```js
function createUserRepository({
  api
}) {
  return {
    async findById(id) {
      const dto = await api.getUser(id);
      return mapUser(dto);
    }
  };
}
```

App/domain không biết transport DTO.

### Senior note

Nếu repository chỉ forward 1:1 API call không thêm abstraction benefit, layer có thể thừa. Hãy thêm layer khi nó bảo vệ semantics, mapping hoặc substitutability thực tế.

---

# Chương 56 — Command / Query Separation

Command thay đổi state; Query đọc state.

```js
await updateUser(command);
const user = await getUser(query);
```

Separation giúp reasoning side effects, caching và retry safety. Không cần full CQRS architecture cho frontend nhỏ; chỉ cần API intent rõ.

---

# Chương 57 — Middleware / Pipeline Architecture

HTTP pipeline có thể là:

```text
trace
↓
auth
↓
retry
↓
transport
↓
response mapping
```

Order là behavior. Retry nằm ngoài/inside auth refresh cho semantics khác. Logging phải redact secrets. Hidden mutation request object gây bugs; immutable-ish transformation thường dễ reason hơn.

---

# Chương 58 — Plugin Architecture

Plugin systems cần contract: name, version, capabilities, init/run/dispose, compatibility và error isolation.

```js
const plugins = new Map();

export function registerPlugin(
  name,
  plugin
) {
  if (plugins.has(name)) {
    throw new Error(
      `Plugin already registered: ${name}`
    );
  }

  plugins.set(name, plugin);
}
```

Senior phải version interface và giới hạn privileges nếu plugin không fully trusted.

---

# Chương 59 — Feature Flags và lifecycle của flag

```js
if (flags.newCheckout) {
  runNewCheckout();
} else {
  runOldCheckout();
}
```

Flag tốt cho rollout/experiments nhưng long-lived flags tạo dead code và combinatorial testing states.

Lifecycle:

```text
create
rollout
observe
complete
remove
```

---

# Chương 60 — Configuration Architecture

Config là input, cần validate ở boundary.

```js
const config = {
  apiBaseUrl:
    runtimeConfig.apiBaseUrl,

  timeoutMs:
    runtimeConfig.timeoutMs
};
```

Validation startup:

```js
function validateConfig(config) {
  if (!config.apiBaseUrl) {
    throw new Error(
      "apiBaseUrl required"
    );
  }
}
```

Frontend bundle không thể giữ secret thực sự chỉ bằng environment variable; browser cuối cùng phải nhận value để dùng.

---

# Chương 61 — Error Taxonomy

Categories có thể gồm validation, business rule, authentication, authorization, not found, conflict, network, timeout, cancellation, server/dependency errors.

```js
class AppError extends Error {
  constructor(
    message,
    {
      code,
      cause,
      retryable = false,
      details
    } = {}
  ) {
    super(message, { cause });
    this.code = code;
    this.retryable = retryable;
    this.details = details;
  }
}
```

Stable machine-readable code tốt hơn parse message.

---

# Chương 62 — Resilience Toolbox

Timeout, cancellation, retry, backoff, jitter, fallback, cache, circuit breaker, bulkhead, graceful degradation không phải checklist cần áp dụng hết. Chọn theo failure mode, criticality, idempotency, latency budget và UX expectation.

Senior design resilience bằng scenarios, không bằng pattern count.

---

# Chương 63 — Observability: production phải trả lời được “chuyện gì đã xảy ra?”

Observability gồm logs, metrics, traces, error reports và performance telemetry.

Một production incident cần biết: release/version nào, page/route nào, request nào, dependency nào fail, mất bao lâu, user action nào dẫn tới đó.

Nếu feature critical nhưng không có cách quan sát production, đó là design thiếu.

---

# Chương 64 — Structured Logging

Bad:

```js
console.log("error");
```

Better:

```js
logger.error(
  "user_load_failed",
  {
    userId,
    status: error.status,
    requestId
  }
);
```

Không log password, access token, refresh token hoặc sensitive PII không cần thiết.

### Senior note

Logging là data governance concern. Log quá nhiều tạo noise/cost/privacy risk.

---

# Chương 65 — Metrics và high-cardinality problem

Metrics examples: request success rate, latency, JS error rate, search failure rate, checkout failure rate, long-task frequency.

Metric labels cần kiểm soát cardinality. Dùng user ID làm metric label có thể tạo hàng triệu series. Per-request detail phù hợp log/trace hơn.

---

# Chương 66 — Tracing và Correlation ID

Distributed flow:

```text
user click
↓
frontend request
↓
gateway
↓
service
↓
database
```

Correlation/request ID giúp nối logs giữa layers.

```js
const requestId = crypto.randomUUID();
```

Nếu organization đã dùng standard tracing headers, follow standard thay vì tự tạo hệ thống cạnh tranh.

---

# Chương 67 — Production Error Reporting và Source Maps

Minified stack `app.abcd.js:1:20291` khó debug. Source maps map generated code về source.

Error report nên có stack, release version, route, browser/runtime, breadcrumbs và relevant network context, nhưng phải filter sensitive data.

Source maps có thể private upload vào error platform thay vì public expose tùy security policy.

---

# Chương 68 — Testing Strategy ở level Senior

Câu hỏi là “risk nào cần test?”, không phải “coverage 100% chưa?”. Layers có unit, integration, contract, E2E, visual, performance và security testing.

Pure business rules có unit tests rẻ. API/service integration có mock server. Critical user journeys có E2E. Contract tests bắt backend/native/plugin schema drift.

Test strategy tối ưu confidence / maintenance cost.

---

# Chương 69 — Contract Testing

Frontend ↔ backend contract có shape, types, error codes, optional fields và version.

Nếu backend đổi `user_nm` thành `name` mà frontend mapper vẫn expect cũ, contract/integration test nên fail trước production.

Hybrid app càng cần contract tests giữa WebView JS và native bridge vì release cycles có thể khác nhau.

---

# Chương 70 — Integration Testing và Mock Server

Thay vì mock `fetch` implementation details, test service + mapper + state cùng mock HTTP server thường gần production hơn.

Bạn verify URL, method, payload, response parsing, error mapping và cancellation behavior như một integration unit.

---

# Chương 71 — E2E Testing

E2E test critical journey: login → search → select → submit → confirmation. Nó cho integration confidence cao nhưng chậm/flaky nếu design poor.

Keep E2E focused vào business-critical paths, đừng duplicate toàn bộ unit test cases qua browser.

---

# Chương 72 — Property-based và Mutation Testing concepts

Property-based testing generate nhiều inputs để test invariant, ví dụ normalize idempotence hoặc encode/decode round-trip.

Mutation testing thay operator/code để xem tests có bắt không. Nếu `>` thành `>=` mà tests vẫn pass, suite có thể yếu.

Đây là tools nâng cao, dùng cho logic critical chứ không phải mọi function.

---

# Chương 73 — Deterministic Async Tests

Avoid test sleep thật 2 giây. Dùng fake timers, controllable promises, mock server và explicit events/state conditions.

Race condition tests cần chủ động điều khiển response order để reproduce stale result. Cancellation tests verify abort signal và cleanup.

---

# Chương 74 — Modern JavaScript Toolbox và compatibility mindset

> **Current-version note:** File này được cập nhật khi ES2026 là snapshot chính thức mới nhất. Các modern APIs trong phần sau chủ yếu đến từ ES2024–ES2025 vì đây là nhóm đã vào standard nhưng vẫn có compatibility gap đáng chú ý. Khi đọc lại sau vài năm, hãy giữ cách đánh giá này và kiểm tra spec/MDN hiện tại.

Modern ECMAScript/runtime có các features như immutable array methods, Iterator helpers, Set operations, `Promise.withResolvers`, `Promise.try`, `RegExp.escape`, explicit resource management và ngày càng nhiều Intl/ArrayBuffer APIs.

Senior không cần chạy theo mọi feature mới. Với browser/WebView enterprise, luôn hỏi target runtime versions, transpiler/polyfill feasibility và fallback. Stage-4/standardized không có nghĩa mọi WebView cũ đã support.

---

# Chương 75 — `Promise.withResolvers()` và external completion

> **Version note — ES2024:** `Promise.withResolvers()` thuộc ES2024. `Promise.try()` là API khác và thuộc ES2025; nó normalize callback có thể return value, throw synchronously hoặc return Promise.

Traditional pattern:

```js
let resolve;
let reject;

const promise = new Promise(
  (res, rej) => {
    resolve = res;
    reject = rej;
  }
);
```

Modern `Promise.withResolvers()` ở supporting runtimes trả `{ promise, resolve, reject }` trực tiếp. Useful cho event-to-promise bridges/queues, nhưng external resolver làm lifecycle phức tạp. Prefer ordinary async composition nếu không cần.

---

# Chương 76 — Iterator Helpers và lazy pipelines

> **Version note — ES2025:** Global `Iterator` và helpers như `map`, `filter`, `take`, `drop`, `flatMap`, `some`, `every`, `reduce`, `toArray` thuộc ES2025. Chúng mới hơn iterator protocol ES2015 một thập kỷ, nên compatibility check vẫn có ý nghĩa với embedded runtimes.

Iterator helpers cho phép operations lazy như map/filter/take trên iterators ở supporting runtimes. Lợi ích là tránh intermediate arrays và stop early.

Đừng rewrite ordinary arrays chỉ để dùng iterator helpers. Use khi lazy semantics/data volume thật sự có giá trị.

---

# Chương 77 — RegExp.escape và literal dynamic regex

> **Version note — ES2025:** `RegExp.escape()` là ES2025. Trên browser hiện đại nó đã trở nên broadly available, nhưng embedded/enterprise WebViews có thể chậm hơn; security-sensitive code không nên silently assume support.

Nếu user nhập keyword và bạn muốn regex literal search, escaping metacharacters là bắt buộc. `RegExp.escape()` cung cấp native solution ở modern runtimes. Với older WebViews, cần compatibility strategy.

```js
const regex = new RegExp(
  RegExp.escape(keyword),
  "i"
);
```

Nếu chỉ cần substring, `includes()` đơn giản hơn.

---

# Chương 78 — Senior Anti-patterns

Framework-shaped thinking: dùng React/WebSquare concept cho mọi JavaScript problem. Premature optimization: viết unreadable code vì benchmark giả. Architecture astronaut: Factory/Repository/Manager cho 10 dòng CRUD. God Service: một service biết mọi domain, DOM, storage, network. Fire-and-forget async không ownership. Unbounded Promise.all. Retry mọi failure. Cache không invalidation. Event bus như global goto. Shared mutable global state. Deep inheritance. Generic deep merge trên untrusted data. `eval`. Logging secrets. 15 booleans thay state model. Optional chaining để che invariant violation.

Senior code không phải code nhiều pattern nhất; là code có **minimum necessary complexity** cho reliability và changeability cần thiết.

---

# Chương 79 — Production Review Checklist dưới dạng tư duy

Khi review feature, hãy tự hỏi: startup có heavy top-level work không; listener/timer/worker/request ai cleanup; cache/queue/concurrency có bound không; async operation có cancellation và stale-result protection không; retry có idempotency không; DOM có unsafe sink không; postMessage/native bridge có validation không; module boundary có rõ không; DTO có leak khắp domain không; error taxonomy có stable không; production failure có logs/correlation/source maps không; tests cover critical behavior không.

Checklist không thay reasoning, nhưng giúp tránh bỏ sót category quan trọng.

---

# Chương 80 — Senior Exit Criteria

Bạn có thể coi mình đạt senior-ready JavaScript khi có thể xử lý các case sau bằng reasoning chứ không bằng đoán. UI freeze: phân biệt CPU/main-thread/render/network và biết profile. Memory tăng sau navigation: tìm listener/timer/subscription/DOM/cache/closure retainer. Search hiện result cũ: nhận ra race và dùng abort/versioning. 5.000 requests cùng lúc: hiểu bounded concurrency. Payment timeout: hỏi idempotency trước retry. API string đưa vào innerHTML: nhận ra XSS. Native bridge: nghĩ origin/capability/schema/version/lifecycle. Production bug không reproduce local: dùng release logs, correlation, network context và source maps. Complex state: dùng reducer/state machine thay boolean explosion. Architecture review: biết dependency direction, public API, ownership, error/cancellation/observability/testing contracts.

Senior không cần nhớ mọi API. Senior cần biết **problem thuộc layer nào, failure mode nào có thể xảy ra và cách chứng minh hypothesis bằng evidence**.

---

# Chương 81 — Từ JavaScript Senior sang React/WebSquare/TypeScript

Khi sang React, closure trở thành hook/stale-closure issue, immutability thành state update discipline, lifecycle thành effect cleanup, state machine/reducer thành UI state management, cancellation thành effect/request lifetime.

Khi sang WebSquareJS, JavaScript scope map sang page/script scope, event lifecycle map sang component/page lifecycle, adapter map sang submission/native plugin wrappers, state modeling map sang DataList/DataMap/page state, hybrid security map sang native bridge/WebView/deep link contracts.

Khi sang TypeScript, runtime concepts không thay đổi. TypeScript chỉ cho bạn encode static relationships tốt hơn. Nếu chưa hiểu JavaScript closure, prototype, async và runtime boundary, TypeScript types không thể thay thế nền tảng đó.

---

# Phụ lục — Cách tự cập nhật version notes sau ES2026 mà không phải học lại JavaScript

Khi ES2027, ES2028 hoặc phiên bản sau xuất hiện, bạn không cần tạo lại một khóa “JavaScript mới” từ đầu. Hãy xem yearly edition như lớp bổ sung trên nền đã học. Nếu feature mới giải quyết problem của Array, nó được ghi thêm vào chương Array; nếu là Promise helper, thêm ở Promise/concurrency; nếu là module syntax, thêm ở module chapter. Closure, prototype, `this`, object identity, event loop mental model và resource ownership không mất giá trị chỉ vì số năm tăng.

Quy trình cập nhật chuẩn là: trước hết xem TC39/ECMA-262 để biết feature đã final và nằm ở snapshot nào; tiếp theo xem MDN compatibility/Baseline để biết mức support browser; cuối cùng đối chiếu target matrix của project. Với hybrid app, target matrix phải bao gồm Android System WebView/WKWebView thật mà app ship, không chỉ Chrome mới trên máy developer.

Khi một bài viết nói “ESNext”, hãy chuyển câu hỏi thành: feature tên gì, proposal Stage mấy, đã Stage 4 chưa, đã nằm trong yearly snapshot nào, và runtime của tôi support chưa? Chỉ cần giữ workflow này, tài liệu sẽ vẫn dễ đọc dù JavaScript thay đổi qua nhiều yearly releases.

Nguồn nên dùng để cập nhật là `https://tc39.es/ecma262/` cho specification cập nhật, Ecma International cho yearly snapshots đã phê duyệt, TC39 proposals repository cho proposal status, và MDN cho browser compatibility/Baseline.

---

# Kết luận

JavaScript Senior không phải level “học thêm cú pháp nâng cao”. Đây là level production engineering. Bạn phải nhìn một feature và đồng thời nghĩ về runtime cost, lifecycle, memory, cancellation, stale data, security boundaries, dependency direction, error semantics, observability và testing.

Một câu hỏi senior không dừng ở “code chạy chưa?”. Nó tiếp tục: nếu user rời page thì sao, request cũ trả về muộn thì sao, server overloaded thì sao, cache stale thì sao, input malicious thì sao, worker không terminate thì sao, production fail thì biết bằng cách nào, và team khác sửa sau một năm có hiểu ownership/dependencies không.

Nếu bạn có thể trả lời những câu hỏi đó một cách có hệ thống, JavaScript core của bạn đã đủ mạnh để đi sâu vào framework và system architecture mà không bị phụ thuộc vào “framework magic”.
