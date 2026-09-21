# JavaScript Master Supplement — Hoàn thiện Knowledge Library từ runtime semantics đến modern ECMAScript

> **Vai trò của file này:** đây là phần thứ tư sau `Beginner → Intermediate → Senior`. File không học lại cú pháp cơ bản mà nối toàn bộ kiến thức thành một mental model thống nhất: source code được khởi tạo và thực thi ra sao, scope/closure/prototype/module liên hệ với nhau thế nào, browser event loop phối hợp task/microtask/render ra sao, vì sao JavaScript tiến hóa từ ES5 sang ES2015 rồi sang yearly ECMAScript, và developer production phải đọc legacy/modern code như thế nào.
>
> **Version tham chiếu:** snapshot chính thức hiện hành là **ECMAScript 2026 — ECMA-262 17th edition**. Living specification trên TC39 có thể đã chứa các finished proposals hướng tới snapshot kế tiếp, vì vậy trong tài liệu này luôn tách bốn khái niệm: **standard snapshot**, **proposal/living spec**, **engine implementation** và **runtime target thực tế**.
>
> File này là **supplement**, không thay thế ba file trước. Khi một concept đã được dạy kỹ ở Beginner/Intermediate/Senior, phần Master chỉ nối nó với semantics sâu hơn hoặc production consequences.

---

# 1. Audit toàn bộ JavaScript Knowledge Library

Sau khi audit canonical notes từ Beginner đến Senior, learning flow hiện tại đã bao phủ đầy đủ các nhóm kiến thức chính. Beginner sở hữu phần values/types, coercion cơ bản, function, array/object, DOM, events, fetch, storage, Promise và async/await nhập môn. Intermediate sở hữu execution context, lexical environment, closure, `this`, prototype chain, class internals, module system, Promise semantics, event loop, tasks/microtasks, iterator/generator và các programming patterns. Senior sở hữu engine/runtime thinking, memory/garbage collection, concurrency, streaming, performance, security, architecture, observability, testing và modern tooling.

Master vì vậy không nên trở thành “file thứ tư lặp lại ba file đầu”. Vai trò đúng của nó là xử lý những câu hỏi còn lại sau khi đã học ba level trước: **tại sao các cơ chế đó tồn tại, chúng nối với nhau thế nào, spec mô tả chúng ra sao, code legacy phản ánh thế hệ JavaScript nào, và feature mới nên được đưa vào production theo tiêu chí nào**.

Một sơ đồ ownership ngắn:

```text
Beginner
  values / types / coercion
  function / array / object
  DOM / events / storage
  fetch / Promise / async-await cơ bản

Intermediate
  execution context / lexical environment
  hoisting / TDZ / closure
  this / prototype / class
  modules
  Promise semantics / task / microtask / event loop
  iterator / generator / architecture patterns

Senior
  engine / memory / GC
  concurrency / streams / workers
  performance
  security
  modules + tooling
  observability / testing / production architecture

Master
  specification semantics
  integrated execution model
  ES5 → ES2015 → modern evolution
  legacy ↔ modern mapping
  exotic objects / Proxy / binary / Unicode / Intl
  package/toolchain edge cases
  cross-realm / host-runtime boundaries
  compatibility strategy
```

Nếu một chương Master nhắc lại một khái niệm như closure hay Promise, mục tiêu là **nối tầng**, không phải bắt đầu lại từ định nghĩa.

---

# 2. JavaScript execution model — ghép toàn bộ bức tranh lại với nhau

Một trong những lỗi phổ biến khi học JavaScript là biết từng từ khóa riêng lẻ nhưng không có một mô hình thống nhất cho quá trình thực thi. Ta có thể bắt đầu từ một file module đơn giản:

```js
const taxRate = 0.1;

export function calculateTotal(price) {
  const tax = price * taxRate;
  return price + tax;
}

console.log(calculateTotal(100));
```

Khi runtime xử lý source, không nên hình dung rằng engine chỉ đọc dòng 1, chạy dòng 1, đọc dòng 2, chạy dòng 2. Trước khi evaluation thực sự đi qua statements, language runtime cần phân tích source và chuẩn bị những structures cần thiết để resolve identifiers, functions, imports, lexical bindings và control flow. Specification mô tả việc này bằng nhiều thuật ngữ formal như **Execution Context**, **Environment Record**, **Lexical Environment**, **Module Environment Record** và các declaration-instantiation algorithms.

Ở mức practical mental model, có thể nghĩ thành hai pha lớn:

```text
Source text
    ↓
Parse / validate syntax
    ↓
Create bindings + environments
    ↓
Evaluate statements / expressions
    ↓
Call functions → push execution contexts
    ↓
Return/throw → pop contexts
```

Đây là nền tảng để hiểu hoisting. “Hoisting” không phải engine cắt dòng `function` hoặc `var` rồi kéo chúng lên đầu file. Đó chỉ là cách nói lịch sử dễ nhớ. Chính xác hơn, **bindings được tạo trong quá trình environment/declaration setup trước khi statement evaluation đi qua vị trí source tương ứng**, nhưng từng loại declaration được khởi tạo khác nhau.

Function declaration có function object sẵn sớm, vì vậy thường gọi trước textual declaration được:

```js
run();

function run() {
  console.log("run");
}
```

`var` binding được tạo và initialized bằng `undefined`, vì thế:

```js
console.log(value); // undefined
var value = 10;
```

không giống lỗi “variable chưa tồn tại”. Ngược lại `let`, `const` và `class` có lexical bindings nhưng chưa được initialized cho đến khi execution đạt declaration. Khoảng thời gian binding đã tồn tại nhưng chưa thể access được gọi là **Temporal Dead Zone (TDZ)**.

```js
console.log(value); // ReferenceError
const value = 10;
```

Mental model này tốt hơn câu “`let` không hoist”, vì lexical declarations thực sự tham gia environment creation; điều khác biệt là **trạng thái initialization**.

### Call stack và execution context

Mỗi function call tạo một execution context mới và được đặt lên call stack:

```js
function c() {
  return 1;
}

function b() {
  return c() + 1;
}

function a() {
  return b() + 1;
}

a();
```

Có thể hình dung:

```text
Global / Module context
  ↓
a()
  ↓
b()
  ↓
c()
```

Khi `c()` return, context của `c` rời stack; execution quay lại `b`. JavaScript synchronous execution về cơ bản đi theo stack này. Infinite recursion làm stack tăng cho đến giới hạn runtime.

Điều cần nhớ là **call stack không phải event loop**. Call stack biểu diễn synchronous call chain đang chạy. Event loop là cơ chế host dùng để quyết định **khi nào một task hoặc continuation mới được phép đưa JavaScript quay lại chạy trên stack**.

---

# 3. Lexical Environment, Scope Chain và Closure thực chất là một hệ thống duy nhất

Scope, lexical environment và closure thường được học thành ba bài riêng, nhưng chúng mô tả cùng một cơ chế ở các góc nhìn khác nhau.

```js
function createCounter() {
  let count = 0;

  return function increment() {
    count += 1;
    return count;
  };
}

const counter = createCounter();
```

Khi `createCounter()` chạy, environment của call đó chứa binding `count`. Function `increment` được tạo trong lexical context đó, nên function giữ khả năng resolve `count` qua outer lexical environment. Sau khi `createCounter()` return, execution context đã rời call stack, nhưng environment cần cho returned function vẫn còn reachable. Đó chính là closure.

Điểm này giúp sửa một hiểu nhầm quan trọng: **closure không có nghĩa “toàn bộ stack frame được đóng băng mãi mãi”**. Runtime chỉ phải giữ những environment/data còn reachable theo semantics. Implementation chi tiết có thể được engine tối ưu mạnh miễn behavior quan sát được vẫn đúng.

Closure trở thành vấn đề memory khi lifecycle của function dài hơn dự kiến và nó giữ reference tới data/resource lớn:

```js
function registerHandler(hugeData) {
  const handler = () => {
    console.log(hugeData.id);
  };

  window.addEventListener("message", handler);

  return () => {
    window.removeEventListener("message", handler);
  };
}
```

Nếu cleanup không xảy ra, listener giữ `handler`, closure giữ `hugeData`, nên object vẫn reachable. Đây là điểm nối trực tiếp giữa **closure → reachability → garbage collection → resource lifecycle**.

---

# 4. `this`, Reference semantics và lý do detached method mất receiver

Intermediate đã học quy tắc quan trọng: normal-function `this` chủ yếu phụ thuộc **call-site**. Master cần hiểu sâu hơn một bước.

```js
const user = {
  name: "Kim",

  greet() {
    return this.name;
  }
};

user.greet();
```

Expression `user.greet` trong một direct method call vẫn mang đủ thông tin để call operation biết receiver/base object là `user`. Vì vậy `this` được set thành `user`.

Nhưng:

```js
const greet = user.greet;
greet();
```

function value đã bị tách khỏi property-reference relationship ban đầu. Call mới là plain function call; receiver `user` không còn tự động được giữ.

Đây là nguyên nhân sâu của nhiều bug callback legacy:

```js
button.addEventListener("click", user.greet);
```

Nếu `greet` cần `this === user`, cần bind hoặc wrapper có chủ đích:

```js
const onClick = user.greet.bind(user);
button.addEventListener("click", onClick);
```

Arrow functions giải quyết một problem khác: chúng **không tạo own dynamic `this`**, mà sử dụng lexical `this` từ surrounding context. ES2015 thêm arrow syntax không chỉ để code ngắn hơn; nó giải quyết một pain point rất phổ biến của callback-heavy JavaScript trước ES2015.

Legacy code thường thấy:

```js
var self = this;

setTimeout(function () {
  self.refresh();
}, 1000);
```

Modern equivalent khi semantics phù hợp:

```js
setTimeout(() => {
  this.refresh();
}, 1000);
```

Đây là ví dụ quan trọng về **evolution có động cơ**, không chỉ là syntax mới.

---

# 5. Prototype chain và class syntax — JavaScript không biến thành Java ở ES2015

JavaScript là prototype-based language. Khi đọc:

```js
user.greet
```

runtime trước hết tìm own property. Nếu không có, lookup đi lên internal prototype chain cho đến khi tìm thấy property hoặc gặp `null`.

Legacy constructor style:

```js
function User(name) {
  this.name = name;
}

User.prototype.greet = function () {
  return `Hello ${this.name}`;
};

const user = new User("Kim");
```

Prototype chain:

```text
user
  ↓
User.prototype
  ↓
Object.prototype
  ↓
null
```

ES2015 class syntax:

```js
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello ${this.name}`;
  }
}
```

làm syntax dễ đọc và gần abstraction class quen thuộc hơn, nhưng method vẫn nằm trên prototype và inheritance vẫn xây trên prototype machinery. Vì vậy câu “ES6 đưa OOP vào JavaScript” là không chính xác; JavaScript đã có object/prototype inheritance từ trước. ES2015 chủ yếu cung cấp **syntax chuẩn, rõ và dễ tooling hơn** cho pattern constructor/prototype đã phổ biến.

Modern class tiếp tục được mở rộng với public fields, `#private` fields/methods và static blocks ở ES2022. Chúng giải quyết những pain points thực tế như runtime privacy và initialization rõ ràng, chứ không thay nền prototype.

---

# 6. Task, microtask và rendering — thứ tự async phải được hiểu như một timeline

Browser JavaScript thường chạy UI logic trên main thread. Khi synchronous stack trống, browser/event loop có thể lấy work tiếp theo. Một mental model hữu ích cho một turn là:

```text
1. Run one task
2. Run synchronous JavaScript until stack empty
3. Drain microtasks
4. Browser may perform rendering work
5. Move to another task
```

Ví dụ:

```js
console.log("A");

setTimeout(() => {
  console.log("timer");
}, 0);

Promise.resolve().then(() => {
  console.log("promise");
});

queueMicrotask(() => {
  console.log("microtask");
});

console.log("B");
```

Kết quả thông thường:

```text
A
B
promise
microtask
timer
```

`Promise.then(...)` và `queueMicrotask(...)` schedule microtasks. Timer callback là một task ở một task source thích hợp. Sau current synchronous execution, microtask queue được drain trước khi timer task có cơ hội chạy.

Điều quan trọng không chỉ là thuộc output. Hãy hiểu hậu quả:

```js
function loop() {
  queueMicrotask(loop);
}

loop();
```

Một chain microtasks không kết thúc có thể **starve** browser khỏi cơ hội xử lý task khác hoặc render. Vì vậy “microtask chạy sớm hơn” không có nghĩa “microtask luôn tốt hơn”.

### `await` nằm ở đâu?

```js
async function run() {
  console.log("before");
  await Promise.resolve();
  console.log("after");
}
```

`await` không block main thread kiểu sleep. Async function tạm dừng; continuation sau `await` được schedule theo Promise-job/microtask semantics. Đây là lý do synchronous code bên ngoài có thể chạy trước phần `after`.

### Rendering không phải ECMAScript semantics

ECMAScript định nghĩa Promise jobs và language behavior; browser HTML standard định nghĩa event loop/render integration. `requestAnimationFrame`, DOM event dispatch và rendering opportunities là host/browser concepts. Đây là ranh giới cần giữ rõ khi nói “JavaScript event loop”.

---

# 7. Promise resolution sâu hơn — Promise không chỉ là callback có `.then()`

Promise được thêm vào ES2015 để chuẩn hóa một abstraction async mà ecosystem trước đó đã tự xây bằng callbacks, Deferred objects và nhiều Promise libraries khác nhau.

Legacy callback pyramid:

```js
loadUser(function (error, user) {
  if (error) {
    handleError(error);
    return;
  }

  loadOrders(user.id, function (error, orders) {
    if (error) {
      handleError(error);
      return;
    }

    renderOrders(orders);
  });
});
```

Promise chain biến dependency thành composition:

```js
loadUser()
  .then((user) => loadOrders(user.id))
  .then(renderOrders)
  .catch(handleError);
```

`async/await` ở ES2017 sau đó làm syntax sequential-looking hơn:

```js
try {
  const user = await loadUser();
  const orders = await loadOrders(user.id);
  renderOrders(orders);
} catch (error) {
  handleError(error);
}
```

Nhưng `async/await` **không thay Promise model**. Async function trả Promise; `await` dùng Promise/thenable assimilation semantics; errors sau await vẫn trở thành rejected async result.

Một detail Master quan trọng là thenable assimilation:

```js
const thenable = {
  then(resolve) {
    resolve(42);
  }
};

const value = await thenable;
```

Không cần object phải là native Promise; Promise resolution có thể assimilate object có callable `then`. Đây là khả năng interoperability mạnh, nhưng cũng có nghĩa getter/`then` từ untrusted object có thể chạy code.

---

# 8. Module system — vì sao ES Modules xuất hiện và nó khác IIFE/CommonJS ở đâu

Trước native modules, browser code thường dùng global scripts và IIFE:

```js
(function () {
  var privateState = 0;

  window.app = {
    increment: function () {
      privateState += 1;
    }
  };
})();
```

Node ecosystem phổ biến CommonJS:

```js
const userService = require("./user-service");
module.exports = createController;
```

Các patterns này giải quyết vấn đề thật, nhưng dependency graph không phải lúc nào cũng statically analyzable. ES2015 modules đưa `import`/`export` vào language:

```js
import { loadUser } from "./user-service.js";

export function start() {
  return loadUser();
}
```

Static imports cho tooling/bundlers biết dependency graph trước khi chạy module, hỗ trợ analysis, tree shaking và tooling tốt hơn. Module scope cũng tránh việc declarations tự động trở thành globals và module code chạy theo strict-mode semantics.

Imports là **live bindings**, không phải copy snapshot đơn giản. Circular module graphs hợp lệ nhưng initialization order có thể gây temporal access problems. Vì vậy circular dependency nên được xem trước hết là một design signal.

Dynamic `import()` ở ES2020 giải quyết nhu cầu dependency không cần load eagerly:

```js
const editor = await import("./heavy-editor.js");
```

Tuy nhiên “dynamic import tạo chunk riêng” là bundler behavior, không phải promise của ECMAScript specification.

Top-level `await` ở ES2022 làm module initialization có thể async, nhưng cũng có thể trì hoãn dependent module graph. Dùng khi module-level dependency thực sự cần, không phải thay mọi startup function bằng top-level await.

---

# 9. ES5 → ES2015 → modern ECMAScript — học bằng vấn đề, không học release notes

Version evolution có ý nghĩa nhất khi hỏi: **developer lúc đó đang gặp vấn đề gì, và feature mới làm code rõ hơn hoặc an toàn hơn thế nào?**

## ES5 — chuẩn hóa nền JavaScript web trước thời modern syntax

ES5 (2009) là một mốc lớn vì nó củng cố JavaScript đã được dùng rộng rãi trên web: strict mode, JSON support, property descriptors/reflection và nhiều array helpers như `map`, `filter`, `reduce`, `forEach`, `some`, `every` trở thành nền tảng chuẩn.

Legacy ES5-style code thường có:

```js
var names = users
  .filter(function (user) {
    return user.active;
  })
  .map(function (user) {
    return user.name;
  });
```

Code này không “sai” chỉ vì cũ. Modern syntax có thể làm intent ngắn hơn:

```js
const names = users
  .filter((user) => user.active)
  .map((user) => user.name);
```

Điểm thay đổi thật nằm ở lexical bindings và arrow semantics, không chỉ số ký tự.

## ES2015/ES6 — bước chuyển sang JavaScript cho application lớn

ES2015 là bước nhảy lớn nhất của modern JavaScript. Những feature như `let`/`const`, classes, modules, Promise, destructuring, rest/spread, Map/Set, Symbol, iterator/generator và arrow functions cùng xuất hiện vì ecosystem cần code dễ tổ chức hơn cho application/library lớn.

Một số legacy → modern mappings nên hiểu theo động cơ:

```text
var
→ let / const
lý do: block scope + binding intent rõ hơn

function callback + var self = this
→ arrow callback
lý do: lexical this cho callback

arguments
→ rest parameter
lý do: array-like legacy object → real parameter collection rõ hơn

string concatenation
→ template literals
lý do: interpolation/multiline dễ đọc

constructor + prototype assignments
→ class syntax
lý do: cùng prototype model nhưng syntax/heritage rõ hơn

IIFE/global namespace
→ ES modules
lý do: module scope + explicit dependency graph

callback/deferred libraries
→ native Promise
lý do: standardized async composition

plain object used as arbitrary key map
→ Map
lý do: arbitrary keys + collection semantics rõ
```

Không phải mọi legacy form đều phải rewrite. `function` vẫn cần khi dynamic `this` phù hợp; object vẫn tốt cho record-shaped data; ordinary loops vẫn rõ hơn functional chains trong nhiều algorithms.

## Sau ES2015 — yearly evolution nhỏ và đều hơn

Từ ES2016, ECMAScript chuyển sang yearly cadence. Tư duy đúng không phải “mỗi năm là một JavaScript mới”, mà là **language được bổ sung incremental**. Những bổ sung đáng nhớ thường giảm boilerplate hoặc encode intent mà developer trước đó phải tự viết.

Ví dụ `async/await` (ES2017) làm Promise-based sequential flow dễ đọc. Object rest/spread (ES2018) làm immutable-style object transformations ergonomic hơn. Optional chaining và nullish coalescing (ES2020) làm optional access/default semantics rõ hơn. Class fields/private elements và top-level await (ES2022) mở rộng class/module model. Copying array methods như `toSorted()` (ES2023) giải quyết nhu cầu non-mutating collection updates. `Promise.withResolvers()`, `Object.groupBy()` và resizable ArrayBuffer facilities (ES2024) chuẩn hóa recurring patterns. Iterator Helpers, Set operations, `RegExp.escape()` và `Promise.try()` (ES2025) tiếp tục đưa common library patterns vào standard.

Không cần thuộc danh sách này. Cần nhớ **problem → abstraction mới → compatibility**.

---

# 10. ECMAScript 2026 — những bổ sung nào đáng biết và tại sao chúng xuất hiện

ECMAScript 2026 là 17th edition. Không nên biến learning notes thành changelog, nhưng một vài additions minh họa rất rõ cách modern ECMAScript tiếp tục chuẩn hóa recurring patterns.

## `Array.fromAsync()`

Trước đây để collect async iterable thành array, bạn thường phải tự loop:

```js
const result = [];

for await (const item of source) {
  result.push(item);
}
```

`Array.fromAsync()` cung cấp built-in abstraction cho async iterables và async sources:

```js
const result = await Array.fromAsync(source);
```

Điểm mới không phải async iteration — nó đã có từ trước — mà là **collection constructor có hiểu async source**.

## `Math.sumPrecise()`

Cộng floating-point values có thể tích lũy precision error, đặc biệt khi magnitude khác nhau. ES2026 thêm một operation chuẩn để sum iterable Numbers theo cách giảm precision loss so với naive accumulation trong nhiều trường hợp.

Điều này không biến IEEE-754 thành decimal arithmetic; financial code vẫn cần domain strategy riêng.

## `Iterator.concat()`

Sau Iterator Helpers ES2025, `Iterator.concat()` tiếp tục làm lazy iteration pipelines dễ compose hơn mà không phải tự viết generator chỉ để nối nhiều iterables.

Legacy pattern:

```js
function* concat(...iterables) {
  for (const iterable of iterables) {
    yield* iterable;
  }
}
```

Modern built-in giảm boilerplate khi runtime support.

## `Error.isError()`

Cross-realm error detection là một pain point vì:

```js
errorFromIframe instanceof Error
```

có thể fail khi constructors thuộc khác Realm. `Error.isError()` cung cấp standardized error-object detection tốt hơn cho các trường hợp này.

## `Map`/`WeakMap` get-or-insert operations

Một pattern cache/index quen thuộc:

```js
let value = map.get(key);

if (value === undefined) {
  value = createValue(key);
  map.set(key, value);
}
```

có edge case nếu `undefined` là stored value hợp lệ và tạo boilerplate repeated. ES2026 chuẩn hóa get-or-insert style operations để express “lấy nếu có, nếu không tạo/default rồi lưu” rõ hơn.

## `Uint8Array` ↔ Base64/Hex

Code web trước đây thường phải đi qua `btoa`/`atob`, manual byte loops hoặc utility library để chuyển binary bytes sang hex/base64. ES2026 bổ sung built-in conversion methods trực tiếp quanh `Uint8Array`, phù hợp hơn với binary data model hiện đại và tránh nhiều binary-string pitfalls của APIs lịch sử.

## JSON source/raw facilities

ES2026 bổ sung khả năng reviver của `JSON.parse()` tiếp cận source context và `JSON.rawJSON()` để kiểm soát primitive JSON output ở mức thấp hơn. Đây là advanced serialization feature, hữu ích khi exact numeric/source representation quan trọng; ordinary application JSON không cần đổi cách viết chỉ vì API mới tồn tại.

### Compatibility rule

“Thuộc ES2026” không có nghĩa WebView production của bạn đã có API. Với project hybrid/WebSquare, luôn kiểm tra Android System WebView và WKWebView versions thực tế trước khi dùng built-in mới mà không fallback.

---

# 11. Object model sâu hơn — descriptors, exotic objects và Proxy invariants

Plain object property không chỉ là `key → value`. Data property còn có descriptor flags `writable`, `enumerable`, `configurable`; accessor property có `get`, `set`, `enumerable`, `configurable`.

```js
const user = {};

Object.defineProperty(user, "id", {
  value: "u1",
  writable: false,
  enumerable: false,
  configurable: false
});
```

Nhiều built-ins không có hoàn toàn ordinary object behavior. Specification dùng khái niệm **exotic objects** cho những objects có internal method behavior đặc biệt, ví dụ Arrays, TypedArrays, String objects, Module Namespace objects, some `arguments` objects và Proxies.

Array là ví dụ dễ thấy: `length` không phải property bình thường hoàn toàn.

```js
const values = [10, 20, 30];
values.length = 1;

console.log(values); // [10]
```

Setting smaller length có thể delete indexed elements.

Sparse array hole cũng khác explicit `undefined`:

```js
const sparse = [,];
const explicit = [undefined];

0 in sparse;   // false
0 in explicit; // true
```

Proxy cho phép intercept object internal operations:

```js
const proxy = new Proxy(target, {
  get(target, key, receiver) {
    return Reflect.get(target, key, receiver);
  }
});
```

Nhưng Proxy không được “nói dối tùy ý”. Specification có **invariants** quanh non-configurable properties, prototype/extensibility và descriptors. Vi phạm invariant có thể throw `TypeError`. Đây là lý do reactivity/metaprogramming library author phải hiểu descriptors và object internals chứ không chỉ thuộc trap names.

---

# 12. Equality algorithms và coercion ở level specification

Beginner đã học `==`, `===`, `Object.is()`. Master cần biết JavaScript có nhiều equality algorithms vì các APIs cần semantics khác nhau.

`===`:

```js
NaN === NaN; // false
0 === -0;    // true
```

`Object.is()`:

```js
Object.is(NaN, NaN); // true
Object.is(0, -0);    // false
```

Collections như Set và nhiều membership operations dùng **SameValueZero**, nơi NaN được coi là bằng chính nó và +0/-0 được coi tương đương.

```js
[NaN].includes(NaN); // true
new Set([NaN, NaN]).size; // 1
```

Coercion cũng nên được hiểu qua internal conversion concepts như `ToPrimitive`, `ToNumber`, `ToString`, `ToBoolean`, `ToPropertyKey` thay vì học câu đố.

Object có thể customize primitive conversion:

```js
const money = {
  amount: 100,

  [Symbol.toPrimitive](hint) {
    if (hint === "string") {
      return `${this.amount} KRW`;
    }

    return this.amount;
  }
};
```

Mục tiêu của knowledge này là debug library/edge cases, không phải viết production code dựa trên clever implicit coercion.

---

# 13. Binary data — ArrayBuffer, TypedArray và DataView

JSON/string không phải representation phù hợp cho mọi data. Image bytes, crypto, compression, WebSocket binary protocol và file parsing thường dùng binary primitives.

`ArrayBuffer` là raw byte storage:

```js
const buffer = new ArrayBuffer(16);
```

TypedArray là typed view:

```js
const bytes = new Uint8Array(buffer);
const numbers = new Int32Array(buffer);
```

Hai views có thể nhìn cùng backing buffer nhưng interpret bytes khác nhau.

`DataView` phù hợp khi binary protocol có fields khác nhau và cần kiểm soát endianness:

```js
const view = new DataView(buffer);
view.setUint32(0, 123456, true);
```

`true` ở đây yêu cầu little-endian.

Một architecture tốt tách:

```text
network/file bytes
↓
decoder
↓
validated transport object
↓
domain model
```

Không để binary offsets/endianness tràn vào business logic.

---

# 14. Unicode và internationalization — `string.length` không phải “số ký tự người dùng nhìn thấy”

JavaScript string dựa trên UTF-16 code units. Một emoji có thể chiếm nhiều code units:

```js
"😀".length; // thường là 2
```

Vì vậy cần phân biệt **code unit**, **code point** và **grapheme cluster**. `for...of` trên string xử lý code points tốt hơn loop theo UTF-16 index trong nhiều trường hợp, nhưng grapheme clusters phức tạp vẫn cần segmentation-aware logic.

`Intl` cung cấp locale-aware formatting/sorting/segmentation:

```js
const currency = new Intl.NumberFormat("ko-KR", {
  style: "currency",
  currency: "KRW"
});

currency.format(1000000);
```

`Intl.DateTimeFormat`, `Intl.Collator`, `Intl.PluralRules`, `Intl.RelativeTimeFormat` và `Intl.Segmenter` giải quyết những vấn đề mà manual formatting bằng string concatenation rất dễ sai.

Rule production: **locale/date/currency semantics là domain concern**, không phải cosmetic detail.

---

# 15. RegExp advanced — statefulness, Unicode và security

RegExp có thể mang mutable state khi dùng flags như `g` hoặc `y` thông qua `lastIndex`.

```js
const pattern = /a/g;

pattern.test("a");
pattern.lastIndex;
```

Reuse same RegExp instance mà không hiểu `lastIndex` có thể tạo bugs khó thấy.

Dynamic regex từ user input là security concern. ES2025 thêm `RegExp.escape()` để biến arbitrary text thành literal-safe fragment cho RegExp:

```js
const regex = new RegExp(RegExp.escape(keyword), "i");
```

Trước đó codebase thường có custom escape helpers. Khi target runtime cũ chưa support, dùng maintained polyfill/helper phù hợp thay vì tự escape vài characters và tưởng đã an toàn.

Một security class khác là **ReDoS**: pattern có catastrophic backtracking có thể tiêu tốn CPU với crafted input. Regex security không chỉ là escaping.

---

# 16. Memory, garbage collection và reachability — nối với closure, DOM và cache

Garbage collector không biết business đã “xong với object”. Nó chỉ quan tâm object còn reachable từ roots hay không.

Common accidental reachability paths:

```text
global → cache → old data
window → listener → closure → large object
DOM/runtime → detached node → handler → state
interval → callback → service → page state
pending async operation → continuation → captured data
```

Đây là lý do cleanup phải theo ownership.

```js
function mount() {
  const controller = new AbortController();

  window.addEventListener("resize", handleResize);

  return () => {
    controller.abort();
    window.removeEventListener("resize", handleResize);
  };
}
```

WeakMap/WeakSet hữu ích khi metadata/cache lifetime nên phụ thuộc key reachability. WeakRef/FinalizationRegistry là niche tools; correctness không được phụ thuộc vào GC timing.

GC implementation có thể generational, incremental, concurrent và thay đổi theo engine version. Application developer nên học **reachability, allocation rate, lifetime và profiler evidence**, không optimize theo một GC blog cũ.

---

# 17. Browser runtime không phải chỉ ECMAScript

Browser application chạy trên nhiều lớp:

```text
ECMAScript language
↓
JavaScript engine
↓
Web APIs
↓
HTML event loop / rendering
↓
DOM / network / storage / workers
↓
OS / native WebView container
```

`fetch`, DOM, Web Storage, Web Workers, `AbortController`, `BroadcastChannel`, `requestAnimationFrame`, Trusted Types và Web Locks không phải ECMA-262 APIs. Chúng có specifications và compatibility timelines riêng.

Điều này đặc biệt quan trọng với hybrid app. Chrome desktop mới nhất support một Web API không có nghĩa Android WebView mà app đang ship cũng support. Và iOS WKWebView version bị gắn với hệ điều hành/engine distribution khác Chrome.

### Compatibility matrix nên là project artifact

```text
feature
standard/platform
minimum Chrome
minimum Android WebView
minimum Safari/WKWebView
Node requirement nếu có
polyfill/fallback
real-device tests
```

Không dùng `ES2026` như một proxy duy nhất cho browser capability.

---

# 18. Toolchain — transpile, polyfill, bundle và runtime là bốn câu chuyện khác nhau

Modern frontend source có thể đi qua:

```text
TypeScript / JavaScript source
↓
Babel / SWC / TypeScript transform
↓
Bundler
↓
Minifier
↓
Browser/WebView
```

**Transpilation** đổi syntax. Optional chaining có thể được rewrite sang syntax cũ.

**Polyfill** cung cấp runtime API còn thiếu như một built-in approximation.

**Bundler** resolve module graph, split chunks, process assets và perform tree shaking.

**Runtime** cuối cùng quyết định platform APIs và engine behavior thực tế.

Vì vậy “Babel compile được” không chứng minh `structuredClone`, `RegExp.escape()` hoặc Web Worker feature nào đó tồn tại ở runtime.

Tree shaking cũng không phải guarantee chỉ vì code dùng ES modules. Top-level side effects, dynamic access và package metadata có thể ngăn dead-code elimination.

Source maps là production observability tool: chúng map generated/minified stacks về source. Với sensitive source, upload private source maps cho error service thường tốt hơn public serving.

---

# 19. Legacy JavaScript literacy — code cũ nên được đọc bằng lịch sử của ngôn ngữ

Enterprise systems thường chứa nhiều thế hệ JavaScript cùng lúc. Senior developer không nên nhìn legacy syntax rồi kết luận “code xấu” trước khi hiểu runtime/tooling constraints lúc nó được viết.

## IIFE thay module scope

```js
(function () {
  var state = {};

  window.app = {
    start: function () {}
  };
})();
```

Modern equivalent thường là ES module, nhưng IIFE từng là giải pháp đúng để tạo private scope trong browser script world.

## `arguments` thay rest parameters

Legacy:

```js
function sum() {
  var total = 0;

  for (var i = 0; i < arguments.length; i += 1) {
    total += arguments[i];
  }

  return total;
}
```

Modern:

```js
function sum(...values) {
  return values.reduce((total, value) => total + value, 0);
}
```

## Prototype constructor thay class syntax

Legacy constructor/prototype code không phải “fake class”; nó dùng prototype model trực tiếp. Class syntax chỉ cung cấp abstraction layer rõ hơn.

## XMLHttpRequest / callback APIs thay fetch/Promise style

Legacy browser code có thể dùng XHR/event callbacks. Modern fetch/Promise code composable hơn, nhưng migration phải bảo toàn timeout, cancellation, credentials, progress và error semantics; không chỉ đổi API names.

## CommonJS / bundler-specific modules

Node/legacy build systems có thể dùng `require`, AMD hoặc UMD. ESM migration cần hiểu package/runtime resolution, không chỉ search/replace `require` thành `import`.

Mastery gồm khả năng **đọc code cũ, hiểu lý do lịch sử, rồi modernize theo behavior chứ không theo syntax fashion**.

---

# 20. Security ở level Master — trace data flow và capability

Thay vì học attack names rời rạc, trace:

```text
Source
↓
Normalization / Parsing
↓
Validation / Authorization
↓
Transformation
↓
Sink
↓
Privilege / Side Effect
```

Sources có thể là URL, form, API response, localStorage, `postMessage`, native callback hoặc third-party SDK. Sinks có thể là `innerHTML`, navigation URL, dynamic object key, `eval`, native bridge command, network request hoặc logging system.

### URL validation

Bad:

```js
if (url.startsWith("https://trusted.com")) {
}
```

Attacker có thể dùng hostname nhìn tương tự. Parse structured URL:

```js
const parsed = new URL(url);

if (parsed.origin === "https://trusted.com") {
}
```

Sau đó vẫn phải validate path/action nếu privilege phụ thuộc chúng.

### `postMessage`

Receiver nên kiểm tra `origin`, expected `source`, schema, message type và authorization/capability. Check origin một mình không ngăn confused-deputy scenario nếu trusted sender bị lợi dụng để yêu cầu privileged action.

### Prototype/object injection

Arbitrary external string không nên tự động trở thành method/property capability:

```js
handlers[userInput]();
```

Prefer allowlisted `Map`/validated discriminant.

### Native bridge

Bridge nên expose minimum capability surface. Một god-object kiểu `nativeBridge.execute(command, payload)` làm validation/authorization khó hơn explicit APIs như `startKyc`, `closeKyc`, `openSecureDocument`.

---

# 21. Performance — engine knowledge chỉ có giá trị sau measurement

Engine có parser, interpreter/baseline compilation, profiling và JIT optimization strategies. Concepts như shapes/hidden classes, inline caches và deoptimization giúp giải thích một số behavior, nhưng production optimization phải bắt đầu từ user-visible problem.

Correct process:

```text
problem / budget
↓
representative measurement
↓
profile
↓
identify hotspot
↓
hypothesis
↓
change
↓
measure again
```

Main-thread UI performance thường bị ảnh hưởng nhiều hơn bởi long synchronous tasks, DOM/layout work, serialization, network waterfalls, large bundles và allocation churn so với micro-optimizing arithmetic syntax.

Memory profiling nên tìm **retainer path**, không chỉ nhìn object count. CPU profiling nên tìm hot call paths/flame-chart widths, không chỉ function bạn nghi ngờ trước.

Cold-start và warm behavior cũng khác nhau: first load có parse/compile/network/cache costs mà repeated interaction không có.

---

# 22. Streams, workers và concurrency — JavaScript không đồng nghĩa “chỉ làm một việc”

Browser main-thread JavaScript execution thường single-threaded theo một agent, nhưng application có concurrency qua async I/O, multiple contexts và workers.

Web Workers cho CPU-heavy work rời main thread. Message passing mặc định dùng structured clone; Transferable objects có thể chuyển ownership của certain buffers để tránh copy cost.

Streams giải quyết progressive processing và backpressure:

```text
source
↓
ReadableStream
↓
TransformStream
↓
WritableStream
```

Backpressure nghĩa producer không nên tiếp tục tạo data vô hạn khi consumer xử lý chậm.

SharedArrayBuffer/Atomics cho shared memory nhưng tăng reasoning complexity mạnh. Nếu team không thể mô tả synchronization protocol rõ ràng, message passing thường là architecture an toàn hơn.

Bounded concurrency cũng quan trọng. `Promise.all(items.map(request))` trên 10.000 items có thể tạo 10.000 operations gần như cùng lúc. Production system thường cần pool/semaphore/concurrency limit.

---

# 23. Error handling — từ `try/catch` tới error taxonomy và causal chain

`try/catch` chỉ là syntax. Production error design cần phân biệt:

```text
programmer/invariant error
validation error
network failure
HTTP/domain failure
timeout/cancellation
external dependency failure
```

`Error.cause` (ES2022) giúp preserve causal chain:

```js
try {
  await repository.load();
} catch (error) {
  throw new Error("Load user failed", {
    cause: error
  });
}
```

`AggregateError` biểu diễn multiple errors, ví dụ khi `Promise.any()` thất bại toàn bộ.

Error serialization cần explicit vì `JSON.stringify(new Error(...))` thường không đưa `message`/`stack` như developer tưởng. Logging layer cũng phải redact secrets và PII.

Expected business failure đôi khi nên được model như result/state thay vì exception. Đây là architecture decision, không có rule “mọi failure đều throw”.

---

# 24. Serialization — JSON không phải universal object cloning

JSON phù hợp vì portable và backend-friendly, nhưng nó không preserve mọi JavaScript representation. `Date` trở thành string, BigInt không stringify trực tiếp theo ordinary behavior, functions/undefined/cycles không được represent như object graph gốc.

`structuredClone()` phù hợp hơn khi clone/transfer structured data trong browser contexts và hỗ trợ nhiều built-ins/cycles hơn, nhưng nó không phải HTTP wire format.

`FormData`, `URLSearchParams` và binary formats giải quyết những transport problems khác nhau. Chọn serialization dựa trên boundary contract, không dựa vào thói quen “mọi thứ stringify JSON”.

---

# 25. Java/Spring interoperability — JavaScript type semantics gặp backend type semantics

Một frontend JavaScript production thường không thể giả định Java types map 1:1 sang JavaScript.

Java/database `long` hoặc BIGINT có thể vượt `Number.MAX_SAFE_INTEGER`. ID lớn thường nên serialize thành string nếu exact integer identity quan trọng.

`BigDecimal` không nên đổi mù quáng sang `number` nếu domain cần decimal precision. Money có thể dùng decimal string hoặc minor-unit integer strategy.

Date/time cần phân biệt rõ:

```text
LocalDate
LocalDateTime
Instant
OffsetDateTime
ZonedDateTime
```

`LocalDateTime` không mang timezone/offset; `Instant` là absolute point. Wire format phải explicit.

Backend enum có thể thêm member mới. Frontend exhaustive logic chỉ an toàn nếu external payload được validated/versioned và có forward-compatibility strategy.

`null`, missing field và empty string không nên được dùng lẫn nhau tùy endpoint; chúng phải có contract rõ.

---

# 26. WebSquare và Native WebView — framework boundary phải được cô lập

Trong WebSquare codebase, một event handler lớn dễ trộn DataMap/DataList, submission, native bridge, UI state và business rule. Master architecture nên tách:

```text
WebSquare event
↓
page/controller adapter
↓
feature service
↓
submission/native gateway
↓
DTO mapper
↓
domain logic
```

DataList/DataMap là infrastructure representation, không nên trở thành domain model ở mọi layer.

Native WebView communication nên có versioned message contracts:

```js
{
  version: 1,
  type: "KYC_COMPLETED",
  requestId: "abc",
  payload: { ... }
}
```

Contract nên định nghĩa version, message type, correlation/request ID, payload schema, error schema, timeout/cancellation và backward compatibility. Deep-link scheme như `ekyc://...` cũng phải parse/validate structured fields, không chỉ prefix check.

---

# 27. React interoperability — framework behavior vẫn dựa trên JavaScript semantics

React không thay thế JavaScript runtime model. Nhiều concept React map trực tiếp:

```text
stale closure
→ lexical closure + render lifecycle

dependency array
→ value/reference identity + closure capture

state immutability
→ reference identity + predictable updates

effect cleanup
→ resource ownership

reducer
→ state transition model

memoization
→ cache + dependency semantics
```

TypeScript giúp static contracts nhưng không sửa runtime timing. Nếu developer không hiểu closure, identity và event loop, React-specific rules sẽ chỉ trở thành mẹo thuộc lòng.

---

# 28. Cross-realm behavior — iframe/window làm `instanceof` không tuyệt đối

Mỗi Realm có own built-ins như `Array`, `Error`, `Promise` constructors. Object được tạo ở iframe Realm có prototype chain dựa constructors của iframe.

Vì vậy:

```js
value instanceof Array
```

có thể false với array từ iframe khác, trong khi:

```js
Array.isArray(value)
```

được thiết kế để nhận array across realms.

Đây cũng là lý do ES2026 `Error.isError()` có giá trị: error detection bằng `instanceof Error` có cross-realm limitation.

Library nhận values từ iframe/worker/plugin boundary nên hiểu Realm semantics thay vì dựa blind vào nominal-looking checks.

---

# 29. API design ở mức Master — data, ownership, async, errors, security

Khi review một API/module, hỏi theo thứ tự:

**Data contract:** input/output là gì, external input được parse ở đâu, missing/null/empty khác nhau thế nào?

**Ownership:** ai được mutate object, ai tạo resource, ai cleanup?

**Async:** operation có timeout/cancellation không, race/stale result xử lý ở đâu, concurrency có bounded không?

**Errors:** expected failure hay programmer bug, causal chain có giữ không, error code có stable cho consumer không?

**Security:** caller được capability gì, trust boundary ở đâu, sink nào có privilege?

**Versioning:** contract có chạy giữa web/native/plugin/backend qua nhiều release không?

**Observability:** production fail thì có correlation ID, structured log, release version và source map không?

**Compatibility:** feature mới có thật sự chạy trên target WebView/runtime không?

**Testability:** network/storage/clock/random/native bridge có dependency seams không?

Một API tốt phải **khó dùng sai**, không chỉ có tên method đẹp.

---

# 30. Testing ở level Master — kiểm thử invariant và timing chứ không chỉ examples

Unit/integration/E2E vẫn là nền, nhưng advanced testing thêm nhiều góc.

**Property-based testing** kiểm tra invariant trên nhiều generated inputs, ví dụ `decode(encode(x))` phải round-trip đúng trong valid domain.

**Fuzzing** đặc biệt hữu ích cho parsers, bridge payloads, URL handling, binary decoders và regex-sensitive inputs.

**Mutation testing** cố thay đổi operators/branches để xem tests có thật sự phát hiện behavior change không.

**Deterministic async tests** tránh phụ thuộc real timer/network scheduling bằng fake clock, controlled promises hoặc scheduler seam.

Clock nên inject khi business logic phụ thuộc time:

```js
function createService({ now = Date.now } = {}) {
  return {
    expired(expiresAt) {
      return now() >= expiresAt;
    }
  };
}
```

Test có thể inject deterministic `now`.

---

# 31. Cách đọc modern JavaScript mà không chạy theo feature mới

Một feature mới chỉ nên vào codebase khi nó thỏa ba điều: **semantics tốt hơn hoặc code rõ hơn**, **target runtimes support hoặc có fallback đúng**, và **team/toolchain hiểu nó**.

Không refactor:

```js
for (const item of items) {
  total += item;
}
```

sang API mới chỉ vì API mới hơn nếu loop đang rõ và đúng.

Ngược lại, nếu `toSorted()` diễn đạt chính xác “sorted copy, không mutate source”, nó có semantic value thực sự so với:

```js
[...items].sort(compare)
```

khi target support.

Modern JavaScript mastery không phải dùng newest syntax nhiều nhất. Nó là khả năng chọn abstraction đúng với problem và compatibility matrix.

---

# 32. Compatibility workflow sau ES2026

Khi ES2027, ES2028 hoặc các snapshot sau xuất hiện, không tạo một course JavaScript mới. Hãy dùng quy trình:

```text
1. Feature cụ thể là gì?
2. Proposal đã Stage 4/final chưa?
3. Nó nằm trong yearly snapshot nào?
4. Engine/browser nào implement?
5. Target WebView của project có support?
6. Syntax có transpile được không?
7. Runtime API có polyfill/fallback đáng tin không?
8. Feature giải quyết problem gì trong code hiện tại?
```

`ESNext` không phải version cố định. Một bài năm 2020 và một bài năm 2026 nói ESNext có thể nói về các feature hoàn toàn khác nhau.

Living spec tại `tc39.es/ecma262` có thể đi trước snapshot chính thức vì nó tích hợp finished proposals cho edition tiếp theo. Historical yearly snapshots mới là mốc edition ổn định.

---

# 33. Master gotchas — hiểu bằng semantics, không học thuộc câu đố

Các behavior sau nên quen vì chúng nối nhiều phần của language model:

```js
typeof null === "object";
NaN !== NaN;
Object.is(NaN, NaN);
Object.is(0, -0);
```

Sparse hole khác `undefined`. `delete array[index]` tạo hole chứ không shift array. `sort()` mutate, `toSorted()` không mutate. Object spread và `Object.freeze()` đều shallow. `Map` object keys dùng object identity. Regex `g`/`y` có `lastIndex` state. `Promise.race()` không cancel losing work. `forEach(async () => ...)` không đợi callbacks. `JSON.stringify(new Error())` không serialize useful error fields mặc định. `JSON.stringify(BigInt(...))` cần explicit strategy. Dynamic import có thể fail vì deployment/chunk mismatch dù source compile đúng. `instanceof` có cross-realm limitation. Getter và Proxy trap có thể khiến ordinary-looking property access thực thi arbitrary logic.

Mục tiêu không phải ghi nhớ như trivia. Khi gặp một behavior lạ, hãy phân loại nó về **coercion/equality**, **object model**, **async scheduling**, **serialization**, **module/runtime**, hoặc **host boundary** rồi điều tra đúng tầng.

---

# 34. Coverage matrix sau audit

| Nhóm kiến thức | Canonical level chính | Trạng thái sau audit |
| --- | --- | --- |
| Execution model / call stack | Intermediate + Master | Đã cover sâu và nối spec/runtime |
| Values / types / coercion | Beginner + Master | Đã cover từ practical đến abstract operations |
| Scope / lexical environment | Intermediate | Đã cover |
| Hoisting / TDZ | Beginner + Master | Đã làm rõ bằng binding initialization |
| Function / closure | Beginner → Intermediate → Master | Đã cover sâu lifecycle/memory |
| `this` | Intermediate + Master | Đã cover call-site + receiver semantics |
| Prototype / class | Intermediate + Master | Đã cover legacy constructor ↔ class evolution |
| Object / array | Beginner → Master | Đã cover ordinary/exotic/sparse/copying APIs |
| Iteration | Intermediate/Senior/Master | Đã cover sync/async/lazy/modern helpers |
| Modules | Beginner → Intermediate → Master | Đã cover ESM, legacy, cycles, dynamic import, tooling |
| Error handling | Beginner/Senior/Master | Đã cover syntax → taxonomy → cause/serialization |
| Promise / async-await | Beginner → Intermediate → Master | Đã cover resolution, scheduling và legacy callbacks |
| Task / microtask / event loop | Intermediate + Master | Đã cover timeline + render/host boundary |
| Browser runtime / DOM / events | Beginner/Intermediate/Senior | Đã cover |
| Fetch / storage | Beginner + Senior security | Đã cover |
| Memory / GC | Senior + Master | Đã cover reachability/lifecycle/profiling |
| Performance | Senior + Master | Đã cover methodology/tooling |
| Security | Senior + Master | Đã cover source-to-sink/capability boundaries |
| Modules/tooling | Senior + Master | Đã cover transpile/polyfill/bundle/source maps |
| Modern JavaScript | Tất cả levels | Đã cover evolution và compatibility mindset |
| Legacy JavaScript | Beginner notes + Master | Đã cover mapping IIFE/var/callback/prototype/CommonJS |
| ES5 → ES2015 → modern | Beginner + Master | Đã chuyển từ timeline sang giải thích động cơ |
| ECMAScript 2026 | Master | Đã bổ sung selected meaningful features |

Audit này cố ý không tạo thêm canonical file. Learning Library tiếp tục dùng đúng bốn notes hiện có.

---

# 35. Master exit criteria

Bạn không cần thuộc ECMA-262. Nhưng sau toàn bộ library, bạn nên có thể giải thích bằng lời:

Một function call tạo context gì và call stack thay đổi thế nào. Lexical environment quyết định scope chain ra sao. Hoisting/TDZ phản ánh declaration initialization khác nhau thế nào. Closure giữ environment vì reachability chứ không phải vì “function nhớ magic”. `this` khác lexical scope vì receiver/call-site semantics. Prototype lookup diễn ra thế nào và class chỉ là abstraction trên prototype model. Promise/`await` continuation liên hệ microtask ra sao. Task/microtask/render sequencing ảnh hưởng UI thế nào. ES modules khác global/IIFE/CommonJS ở dependency model nào. Garbage collector nhìn reachability, không nhìn business intent. Browser APIs khác ECMAScript built-ins ở specification/compatibility layer nào. Transpilation khác polyfill thế nào. Và khi một feature mới xuất hiện, bạn biết đánh giá standard status, runtime support và problem solved thay vì chỉ hỏi “feature này mới không?”.

Bạn cũng nên có thể đọc cả hai đoạn:

```js
var self = this;
request(function (error, value) {
  if (!error) {
    self.render(value);
  }
});
```

và:

```js
const value = await request();
this.render(value);
```

rồi giải thích chính xác **những abstraction nào đã thay đổi**, chứ không chỉ nói đoạn dưới “modern hơn”.

---

# Appendix A — Nguồn authoritative để cập nhật library

Khi cần xác minh language semantics/version, ưu tiên:

```text
ECMA-262 living specification
https://tc39.es/ecma262/

Ecma International yearly ECMA-262 editions
https://ecma-international.org/publications-and-standards/standards/ecma-262/

TC39 proposals
https://github.com/tc39/proposals
```

Khi cần developer-facing browser compatibility, dùng MDN JavaScript/Web APIs và compatibility tables. Khi project là hybrid app, browser tables vẫn phải được đối chiếu với WebView versions thực tế mà ứng dụng ship.

Không dùng một blog cũ hoặc một transpiler preset như nguồn duy nhất để kết luận feature đã standard hay runtime đã support.

---

# Kết luận

JavaScript Knowledge Library hoàn chỉnh không nên kết thúc ở việc nhớ nhiều APIs. Mục tiêu cuối là nhìn một vấn đề và đặt nó vào đúng tầng:

```text
Language semantics
↓
Execution / scope / object model
↓
Async scheduling
↓
Host/browser runtime
↓
Memory / performance
↓
Toolchain / modules
↓
Security / architecture
↓
Compatibility / deployment
```

ES5, ES2015 và modern ECMAScript không phải ba ngôn ngữ khác nhau. Chúng là ba giai đoạn trong quá trình cùng một language trưởng thành: ES5 chuẩn hóa nền web đã tồn tại, ES2015 cung cấp những abstractions cần cho applications/modules lớn, và yearly ECMAScript sau đó bổ sung dần các patterns đã chứng minh giá trị trong ecosystem.

Khi bạn hiểu **vì sao** một feature xuất hiện, bạn có thể đọc cả legacy và modern code mà không bị phụ thuộc vào thời điểm syntax được viết. Đó mới là mục tiêu của Master level.