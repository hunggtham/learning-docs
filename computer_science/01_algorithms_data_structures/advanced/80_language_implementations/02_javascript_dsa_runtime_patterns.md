# JavaScript Runtime Patterns cho DSA
**JavaScript 자료구조와 런타임 패턴**

JavaScript cho phép viết DSA rất nhanh, nhưng cùng một algorithm có thể có correctness/performance caveat khác C hoặc Java vì `Number`, dynamic arrays, object identity, garbage collection, UTF-16 strings và JIT runtime behavior.

Mental model cần giữ là:

> Algorithmic invariant không đổi, nhưng **representation semantics + runtime cost model** đổi theo ngôn ngữ.

Vì vậy học DSA bằng JavaScript không chỉ là chuyển syntax từ Java/C; cần hiểu các điểm runtime có thể làm assumptions cũ sai.

## `Number` và integer precision

JavaScript `Number` là IEEE-754 double. Integers chỉ được biểu diễn chính xác tới:

\[
2^{53}-1
\]

```js
Number.MAX_SAFE_INTEGER
```

Nếu prefix sum, shortest-path distance, combinatorial count hoặc ID arithmetic có thể vượt safe integer range, result có thể mất exactness dù không overflow kiểu fixed-width.

Ví dụ:

```js
Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2
```

có thể cho behavior gây ngạc nhiên do precision.

## `BigInt`

`BigInt` cho arbitrary-size integer:

```js
const x = 12345678901234567890n;
```

Nhưng không trộn trực tiếp arithmetic với `Number`:

```js
1n + 1 // TypeError
```

Comparator cho BigInt nên dùng relational logic:

```js
(a, b) => a < b ? -1 : a > b ? 1 : 0
```

thay vì `a - b` nếu callback cần Number return.

## Infinity và BigInt

`Infinity` phù hợp Number-based shortest paths:

```js
const dist = Array(n).fill(Infinity);
```

BigInt không có `BigInt Infinity`. Nếu dùng BigInt distance, cần explicit sentinel:

```text
null
undefined
separate reachable boolean
hoặc known upper-bound BigInt
```

Representation choice ảnh hưởng algorithm boilerplate.

## Array là dynamic object, không phải C array

JavaScript `Array` hỗ trợ dynamic length và mixed element types.

```js
const a = [];
a.push(1);
a.push(2);
```

Runtime có thể optimize dense homogeneous arrays tốt, nhưng sparse/mixed shapes có thể dùng representation khác.

Đừng assume mỗi Array element luôn là raw contiguous 8-byte slot như C `double[]`.

## Dense array và sparse array

```js
const a = [];
a[1_000_000] = 1;
```

`a.length` trở thành 1,000,001 dù chỉ một entry được set.

Runtime có thể switch sang sparse/dictionary-like representation.

Với DSA numeric dense storage, tránh index jumps hoặc `delete a[i]` nếu không cần.

## Hole khác `undefined`

```js
const a = new Array(3);
```

tạo holes.

```js
const b = [undefined, undefined, undefined];
```

có explicit elements.

Một số array methods xử lý holes khác explicit undefined.

Nếu algorithm cần initialized numeric storage, dùng:

```js
Array(n).fill(0)
```

hoặc TypedArray.

## Array làm stack rất tự nhiên

```js
stack.push(x);
stack.pop();
```

Operations ở cuối thường là natural choice.

## Queue và `shift()`

Repeated:

```js
queue.shift();
```

có thể gây reindex/copy/internal work tùy engine/representation. Với queue lớn, dùng head index:

```js
const q = [];
let head = 0;

q.push(start);
while (head < q.length) {
  const u = q[head++];
}
```

Đây là pattern cực phổ biến cho BFS.

## Queue compaction

Nếu queue sống lâu, processed prefix giữ array references và logical memory tới khi array released.

Có thể compact theo threshold:

```js
if (head > 4096 && head * 2 > q.length) {
  q.splice(0, head);
  head = 0;
}
```

hoặc `q = q.slice(head)`.

Threshold là engineering choice; không cần compact sau mỗi dequeue.

## Custom deque

Nếu cần push/pop cả hai đầu thường xuyên, có thể implement ring buffer thay vì dựa `unshift/shift`.

Representation:

```text
buffer
head
tail
size
capacity
```

Grow giống dynamic circular array.

## Object vs Map

Plain object:

```js
const obj = {};
```

có property semantics và keys chủ yếu strings/symbols.

`Map` hỗ trợ arbitrary key identity:

```js
const map = new Map();
map.set(objectKey, value);
```

General DSA mapping thường `Map` rõ semantics hơn object hacks.

## Object key coercion

```js
const o = {};
o[1] = 'a';
o['1'] = 'b';
```

hai accesses liên quan same string property key `"1"`.

Nếu domain phân biệt key types, `Map` safer.

## Prototype caveat

Plain object có prototype chain trừ object đặc biệt:

```js
const dict = Object.create(null);
```

Dù vậy, `Map` vẫn thường là choice rõ ràng hơn cho algorithmic dictionary.

## `Map` key equality và object identity

```js
const m = new Map();
m.set({x: 1}, 'value');
console.log(m.get({x: 1})); // undefined
```

Hai object literals có identity khác nhau.

Với state `(x,y,mask)`, options:

```text
encode integer
encode string
nested Maps
intern canonical object
```

Đừng tạo object mới rồi expect value equality.

## Canonical state encoding

Nếu ranges nhỏ:

```js
const key = ((x * width + y) << bits) | mask;
```

nhưng bitwise operators có 32-bit semantics, nên range cần chắc chắn fit.

Safer generic:

```js
const key = `${x},${y},${mask}`;
```

String encoding đơn giản nhưng allocation/hash overhead cao hơn.

Nested arrays/maps có thể tốt hơn tùy bounds.

## `Set`

`Set` là default tốt cho visited/membership khi key identity semantics phù hợp.

```js
const seen = new Set();
seen.add(key);
if (seen.has(key)) { ... }
```

Nếu vertices là dense integer `0..n-1`, boolean/typed array thường memory/performance tốt hơn.

## Boolean visited bằng Array vs TypedArray

```js
const seen = new Uint8Array(n);
```

cho dense numeric IDs, compact và predictable.

```js
seen[v] = 1;
```

Thường phù hợp graph algorithms lớn hơn `Array(n).fill(false)` object semantics.

## TypedArray

Common types:

```text
Int32Array
Uint32Array
Float64Array
BigInt64Array
BigUint64Array
```

Advantages:

```text
fixed length
compact numeric storage
predictable coercion
interop với binary buffers
```

Trade-offs:

```text
không dynamic push/pop
numeric range fixed
assignment có coercion/wrap semantics
```

## `Int32Array` overflow semantics

Assign large Number vào `Int32Array` sẽ convert/wrap theo 32-bit integer semantics.

Nếu Dijkstra distance có thể > 2^31-1, `Int32Array` sai dù Number algorithm đúng.

Use `Float64Array` cho Number range hoặc different representation.

## `Uint8Array` cho flags

Visited, color, state nhỏ rất hợp:

```js
const state = new Uint8Array(n);
// 0 unvisited, 1 visiting, 2 done
```

compact hơn objects/strings.

## BigInt typed arrays

`BigInt64Array` và `BigUint64Array` hỗ trợ 64-bit bigint storage, nhưng values vẫn limited 64-bit modulo semantics, không arbitrary-size như standalone BigInt.

Đừng nhầm “BigInt type” với unlimited typed-array cell.

## Bitwise operators là 32-bit

Number bitwise operators convert operands sang signed/unsigned 32-bit.

```js
1 << 31
```

có signed behavior.

Bitmask với >31 useful bits cần caution. `BigInt` bitwise operators có thể hỗ trợ larger masks:

```js
1n << 60n
```

nhưng code/collections/comparators phải consistent BigInt.

## `>>> 0`

Pattern:

```js
x >>> 0
```

convert về unsigned 32-bit Number.

Useful trong hashing/bit operations, nhưng silently truncates higher bits. Không dùng như generic “make positive” nếu data >32-bit.

## Numeric sort comparator

Default:

```js
[2, 10, 3].sort()
```

sort theo string-like ordering semantics, không numeric ascending như thường mong đợi.

Use:

```js
arr.sort((a, b) => a - b);
```

cho Number safe domain.

## BigInt sort comparator

Không trả `a-b` BigInt trực tiếp vì comparator return expected Number-like sign contract; relational comparator an toàn:

```js
arr.sort((a, b) => a < b ? -1 : a > b ? 1 : 0);
```

## Sort stability

Modern ECMAScript specifies stable `Array.prototype.sort`, nhưng nếu code targeting old/nonstandard environments cần check runtime. Library docs/runtime target vẫn là source of truth.

Stability matters khi secondary order relies on original order.

## Custom priority queue

JavaScript standard library không có built-in general `PriorityQueue` giống Java.

DSA code thường implement binary heap:

```js
class MinHeap {
  constructor(compare = (a, b) => a - b) {
    this.a = [];
    this.compare = compare;
  }

  push(x) { /* sift up */ }
  pop() { /* swap root/last + sift down */ }
  peek() { return this.a[0]; }
}
```

Comparator semantics phải consistent.

## Object allocation trong heap

Dijkstra:

```js
heap.push({ node: v, dist: nd });
```

rất readable nhưng có nhiều object allocations.

Nếu performance/memory critical, alternatives:

```text
parallel arrays
small tuples
encoded integer states
custom struct-of-arrays heap
```

Profile trước khi complexity hóa code.

## Stale-entry Dijkstra

Do custom heap thường không support decrease-key:

```js
heap.push([newDist, v]);
```

khi pop:

```js
if (d !== dist[v]) continue;
```

Pattern này đơn giản và robust.

## Recursion depth

Recursive DFS/backtracking có thể vượt call stack.

Runtime limit không standardized portable theo number cụ thể. Đừng assume một depth cố định từ browser/Node version khác.

Deep graph/tree nên iterative.

## Tail-call optimization

ECMAScript có proper-tail-call history/spec semantics trong strict contexts, nhưng mainstream runtime support/practical portability không nên được giả định cho DSA stack safety.

Use explicit stack khi depth uncontrolled.

## Async không giải recursion stack tự động theo cách miễn phí

Chuyển code sang Promise/`async` thay scheduling semantics, allocation/overhead lớn và không phải general substitute cho iterative DFS.

DSA CPU traversal nên explicit stack nếu stack-safe cần thiết.

## Event loop và long-running algorithms

JavaScript trên browser/Node thường chạy user JS trên event-loop thread context. Một `O(n^2)` loop dài có thể block UI/event processing.

Algorithm complexity vì thế ảnh hưởng responsiveness, không chỉ throughput.

Large CPU-bound task có thể cần:

```text
chunking/yielding
Web Worker
worker_threads
native/WASM
```

nhưng concurrency design là separate concern.

## Microtasks và yielding

`await Promise.resolve()` yield vào microtask queue nhưng có thể vẫn starve other event phases nếu loop poorly designed.

Không dùng async scheduling như substitute cho correct algorithm selection.

## Garbage collection

JS runtime reclaim unreachable objects, nhưng Map/Set/cache/closure có thể giữ references sống lâu.

Unbounded memoization:

```js
const cache = new Map();
```

có thể trở thành logical memory leak.

GC tự động không nghĩa memory lifecycle không cần design.

## WeakMap và WeakSet

WeakMap keys phải là objects/non-primitive appropriate according to runtime semantics; entries không giữ key alive như strong map.

Useful cho metadata gắn với object lifetime.

Không enumerable, không suitable cho general algorithm state table cần iteration.

## Closures và retention

Closure có thể giữ reference tới large array/tree dù outer function đã return.

Event listeners/timers cũng giữ callbacks và captured state.

Memory leaks JS thường là reachability leaks hơn manual-free errors.

## Object shape và hidden classes

JIT engines có internal object-shape optimizations. Objects được tạo cùng property order/shape thường optimization-friendly hơn objects thay đổi fields tùy hứng.

Trong hot loops, stable data shape có thể giúp performance.

Nhưng exact hidden-class behavior là engine-specific; đừng code phụ thuộc internal undocumented thresholds.

## `delete` property và shapes

Repeated add/delete dynamic properties có thể degrade optimized shape.

For DSA fixed record, initialize known fields upfront:

```js
const node = { key, left: null, right: null, size: 1 };
```

thường clearer và shape-stable.

## Class vs object literal

`class Node` và object literal đều ultimately use object semantics. Class giúp consistent construction/API, không tự guarantee compact C-like layout.

For millions nodes, representation choice arrays vs objects matters more than class syntax.

## Private fields

`#field` cung cấp language-level privacy nhưng có runtime/tooling considerations. Không cần dùng trong performance DSA unless encapsulation matters.

## CSR graph trong JavaScript

Static dense-ID graph có thể dùng TypedArrays:

```text
Uint32Array offsets
Uint32Array edges
```

để giảm object/array overhead.

Building CSR có thể cần two-pass:

```text
count degrees
prefix-sum offsets
fill edges
```

Đây là bridge giữa JS convenience và systems-style compact representation.

## Dynamic adjacency lists

Readable:

```js
const g = Array.from({length: n}, () => []);
g[u].push(v);
```

Good default cho moderate graphs.

If millions edges, nested array object overhead cần benchmark.

## String là UTF-16 code units

```js
s.length
s[i]
s.charCodeAt(i)
```

operate largely on UTF-16 code units.

Emoji/code point ngoài BMP có surrogate pairs.

```js
'😀'.length === 2
```

String algorithm phải define unit:

```text
UTF-16 code unit
Unicode code point
grapheme cluster
```

## Iterating code points

```js
for (const ch of s) {
    // iterates Unicode code points-ish strings via iterator semantics
}
```

better than index for surrogate pairs, nhưng grapheme cluster vẫn có thể gồm nhiều code points.

`Intl.Segmenter` có thể segment graphemes khi UI/user-perceived chars cần thiết.

## String immutability

JavaScript strings immutable. Repeated concatenation runtime có optimizations nhưng large construction thường better dùng array pieces + `join` trong some workloads.

Benchmark if hot.

## Map iteration order

`Map` giữ insertion order by spec. Nhưng order đó không phải sorted key order.

Nếu algorithm needs sorted map semantics, Map + sort keys mỗi time không equivalent TreeMap performance.

JavaScript standard library thiếu built-in balanced ordered map; custom/library structure có thể cần.

## Object property iteration order

Property enumeration có specified ordering categories nhưng subtle integer-like key rules. Đừng dùng plain object iteration như generic sorted/insertion-order map assumption.

Map semantics clearer.

## Stable state encoding bằng string

```js
const key = `${r}|${c}|${mask}`;
```

simple but allocates string.

Alternative nested arrays if bounds known:

```js
const seen = Array.from({length: rows}, () =>
  Array.from({length: cols}, () => new Uint8Array(1 << k))
);
```

Memory may explode. Estimate state space first.

## Big state and hash Map

For sparse reachable states, `Map`/`Set` with canonical string/BigInt keys may be better than dense tensor allocation.

Same sparse-vs-dense DP trade-off as Java/C.

## TypedArray initialization

Typed arrays initialize numeric zeros automatically:

```js
const dist = new Float64Array(n);
```

but zero may not be desired sentinel.

```js
dist.fill(Infinity);
```

for shortest-path Number domain.

## `NaN` caveats

`NaN` comparisons are unusual:

```js
NaN === NaN // false
```

`Map`/Set use SameValueZero-like semantics where NaN keys can behave differently from `===` intuition.

Algorithm numeric domain should avoid NaN unless explicitly meaningful.

## `-0`

JavaScript has `0` and `-0` at Number level. Most equality/map semantics treat them equivalent enough for DSA, but numeric edge cases can matter in low-level math.

Usually normalize/ignore unless domain distinguishes sign-zero behavior.

## Floating-point sums

Prefix sum of decimals can accumulate rounding:

```js
0.1 + 0.2 !== 0.3
```

If domain is money, integer minor units or decimal library may be needed.

Algorithm mathematical correctness depends numeric representation.

## Sorting objects

Comparator should avoid inconsistent results:

```js
items.sort((a, b) =>
  a.score !== b.score ? a.score - b.score : a.id - b.id
);
```

If fields may exceed safe range, relational comparisons instead of subtraction.

Comparator should be transitive to avoid undefined-like sorting behavior/results.

## Performance measurement

JS JIT has warm-up/tiering/deoptimization. Microbenchmark should:

```text
run warm-up
use realistic data shapes
consume result để tránh dead-work artifacts
measure multiple iterations
observe memory/GC
avoid comparing cold run only
```

Node `performance.now()`/`process.hrtime.bigint()` can measure timing, but methodology matters more than timer resolution.

## Hidden benchmark trap: polymorphic data

Benchmark array of all numbers rồi production array mixed number/object/string có thể represent differently.

Benchmark same shape as workload.

## Browser vs Node runtime

Same ECMAScript semantics, but engine version, memory limits, GC tuning và environment differ.

Do not claim universal performance numbers for “JavaScript” without runtime context.

## Web Worker / worker_threads

CPU-bound algorithms có thể move to worker to avoid blocking main thread.

Data transfer/serialization/shared memory adds cost.

Parallelism only helps if workload partitionable and overhead justified.

## SharedArrayBuffer và Atomics

Low-level shared-memory concurrency exists but correct lock-free algorithms require memory-order/coordination understanding.

Just using `Atomics` does not make arbitrary data structure thread-safe.

## WebAssembly connection

For performance-critical numeric/graph operations, C/Rust/WASM may offer compact memory/control. But boundary crossing and data conversion can dominate if calls too fine-grained.

Batch work across boundary.

## Common misconceptions

“Array index access luôn như C array” — abstraction/runtime representation khác.

“Bitmask bằng Number có 53 bits vì Number safe integer 53 bits” — JS bitwise operators coerce to 32-bit, nên ordinary bitwise mask không dùng all 53 bits.

“Map object keys compare by fields” — chúng compare identity.

“`shift()` luôn O(1)” — không nên assume; head-index queue safer predictable pattern.

“BigInt chỉ là Number lớn hơn” — arithmetic mixing/API semantics khác.

“GC nghĩa là không leak” — strong references/caches/closures vẫn giữ memory.

“Async recursion tránh stack issue free” — scheduling/overhead semantics khác, không general DSA fix.

## Testing DSA trong JavaScript

Use reference simple implementation trên small random inputs.

Heap:

```text
push random values
compare popped sequence với [...values].sort((a,b)=>a-b)
```

Graph shortest path:

```text
small graphs
compare Dijkstra/BFS with Floyd-Warshall reference
```

String algorithms:

```text
compare KMP matches với naive index checks
include Unicode/code-unit cases according to chosen semantics
```

## Property tests

Binary search lower bound:

```text
all i < ans: a[i] < target
all i >= ans: a[i] >= target
```

DSU:

```text
connectivity partition equivalent reference graph components
```

Segment tree:

```text
random update/query compare brute-force array
```

JS dynamic language makes property testing particularly valuable.

## Memory profiling

Chrome DevTools/Node heap snapshots can reveal retained Maps, object-heavy nodes, listeners/closures.

CPU profiles identify hot loops/comparators/hash/string encoding.

Optimize based on evidence.

## Representation checklist

```text
Dense integer IDs?       -> Array/TypedArray
Sparse arbitrary keys?   -> Map/Set
Need queue?               -> array + head index / custom deque
Need priority queue?      -> custom heap/library
Need >32-bit bitmask?     -> BigInt or alternate representation
Need exact >2^53 int?     -> BigInt
Huge static graph?        -> consider CSR TypedArrays
Deep DFS?                 -> iterative stack
Unicode text?             -> define code unit/code point/grapheme semantics
```

## Mental Model

> JavaScript DSA mạnh nhất khi ta giữ algorithmic invariant rõ nhưng **không giả định runtime giống C/Java**. Array, Map, Number, BigInt, TypedArray và objects mỗi loại có semantic boundary riêng. Correctness trước hết cần numeric/equality/string semantics đúng; performance sau đó cần stable data shape, compact representation và measurement dưới runtime thật.

Khi implementation bắt đầu lớn, hãy hỏi:

```text
Number range có exact không?
Bitwise có bị 32-bit coercion không?
State key dùng value hay identity?
Array có dense không?
Queue có tránh shift/unshift hot path không?
Recursion depth có bounded không?
Object allocation/GC có dominate không?
TypedArray type có đủ range không?
Unicode unit có đúng domain không?
```

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).