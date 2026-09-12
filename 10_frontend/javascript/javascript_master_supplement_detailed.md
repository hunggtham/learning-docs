# JavaScript Master Supplement — Phần bổ sung toàn bộ những mảng còn thiếu

> **Vai trò của file này:** đây là phần thứ tư sau `Beginner → Intermediate → Senior`. Nó không lặp lại ba phần trước mà tập trung vào các kiến thức còn thiếu, các edge case khó, semantics gần specification, interoperability, tooling và những vùng mà một JavaScript developer senior thường chỉ gặp khi debug hệ thống phức tạp hoặc thiết kế library/platform.
>
> **Version tham chiếu:** ECMAScript 2026 là yearly snapshot chính thức mới nhất tại thời điểm tài liệu này được cập nhật. Tuy nhiên một số finished proposals sau snapshot 2026, chẳng hạn Temporal và Explicit Resource Management, đang hướng tới snapshot tiếp theo. Vì vậy file luôn phân biệt rõ “đã nằm trong yearly standard”, “đã Stage 4 nhưng post-snapshot”, “Web API”, và “runtime/browser support”.

---

# 1. Cách đọc ECMAScript specification mà không bị ngợp

Ở ba level trước, bạn chủ yếu dùng documentation theo góc nhìn developer: syntax, method, behavior và production trade-off. Ở Master, bạn cần biết cách đọc **ECMA-262 specification** khi gặp một edge case mà MDN hoặc tutorial không giải thích đủ.

Specification không được viết như sách giáo khoa. Nó dùng ngôn ngữ thuật toán rất formal và nhiều khái niệm nội bộ như **Abstract Operations**, **Internal Slots**, **Completion Records**, **Environment Records**, **Reference Records**, **Realms**, **Jobs** và **Agents**. Những tên này không phải API bạn gọi trực tiếp; chúng là vocabulary để mô tả chính xác semantics của JavaScript.

Ví dụ khi bạn viết:

```js
1 + "2";
```

tutorial có thể nói “number bị chuyển sang string rồi concatenate”. Specification thì phải mô tả chính xác chuỗi operation nào xảy ra, giá trị được đưa qua conversion nào, trong trường hợp nào dùng numeric addition và trong trường hợp nào dùng string concatenation. Chính mức chi tiết này giúp giải thích các edge case mà “mẹo nhớ” không đủ.

Một cách đọc hiệu quả là không đọc spec từ trang đầu đến cuối. Hãy bắt đầu từ feature cụ thể. Nếu muốn hiểu `Promise.try()`, tìm section của method đó. Nếu muốn hiểu `==`, tìm Abstract Equality Comparison. Nếu muốn hiểu `this` của method call, lần theo Reference Record và Call semantics. Nếu muốn hiểu `Array.length`, tìm Array Exotic Objects.

### Master Note

Spec không nên thay documentation thực dụng. Dùng MDN để học và dùng API; dùng ECMA-262 để giải quyết semantics khó, kiểm tra edge case hoặc author library/runtime abstraction.

---

# 2. Abstract Operations: “function nội bộ” của specification

Abstract Operation là thuật toán specification dùng để mô tả behavior. Bạn không thể viết:

```js
ToNumber(value);
```

trong application code, nhưng nhiều JavaScript operations được định nghĩa bằng các abstract operations như:

```text
ToPrimitive
ToBoolean
ToNumber
ToNumeric
ToString
ToPropertyKey
Get
Set
Call
Construct
IsCallable
IsConstructor
SameValue
SameValueZero
```

Điều quan trọng là nhận ra nhiều syntax khác nhau thực ra reuse cùng internal operation.

Ví dụ khi object được dùng trong arithmetic hoặc string context, engine có thể cần gọi `ToPrimitive`. Khi dynamic property key được dùng, key đi qua `ToPropertyKey`. Khi `Set` hoặc `Map` compare values, equality semantics không nhất thiết giống `===`.

Hiểu abstract operations làm JavaScript bớt “ma thuật”. Thay vì nhớ hàng chục kết quả lạ, bạn có thể trace operation.

---

# 3. Completion Records và abrupt completion

Specification không chỉ coi execution result là một value. Một operation có thể hoàn thành bình thường hoặc **abruptly** vì `throw`, `return`, `break`, `continue`.

Ví dụ:

```js
function read() {
  try {
    return 10;
  } finally {
    console.log("cleanup");
  }
}
```

Để mô tả chính xác việc `return` đang xảy ra nhưng `finally` vẫn chạy, spec sử dụng Completion Records.

Điều này đặc biệt quan trọng khi học:

```text
try/finally
iterator closing
generator return
resource disposal
promise resolution around thrown errors
```

Bạn không cần implement Completion Record, nhưng mental model giúp hiểu tại sao cleanup vẫn xảy ra trong nhiều control-flow situations.

---

# 4. Reference Records và lý do `obj.method()` khác `const fn = obj.method; fn()`

Ở Intermediate bạn đã học `this` phụ thuộc call-site. Ở Master, ta nối điều đó với spec model.

Expression:

```js
obj.method
```

không chỉ ngay lập tức trở thành function value. Trong specification, property access có thể tạo một reference-like structure chứa base object và property key. Khi expression được gọi trực tiếp:

```js
obj.method();
```

call operation còn biết base là `obj`, nên `this` được set từ base.

Nhưng:

```js
const fn = obj.method;

fn();
```

khi function đã được lấy ra thành value độc lập, relationship với base object bị mất. Đây là lý do “detached method” mất `this`.

Mental model này cũng giải thích vì sao:

```js
(0, obj.method)();
```

khác:

```js
obj.method();
```

Đây không phải trivia cần dùng hằng ngày, nhưng rất hữu ích khi debug wrappers, callbacks hoặc method extraction.

---

# 5. Environment Records, Realms, Jobs và Agents

## Environment Records

Intermediate đã học Lexical Environment và Scope Chain. Specification dùng Environment Records để mô tả nơi bindings được lưu và cách resolve identifier.

Có nhiều loại environment, ví dụ declarative environment, function environment, module environment và global environment. Bạn không cần nhớ tên implementation detail, nhưng cần hiểu rằng lexical scoping là một system formal chứ không phải “function nhớ variable một cách thần bí”.

## Realms

Mỗi **Realm** có tập built-ins riêng:

```text
Object
Array
Promise
Error
Map
Set
```

Một iframe cùng origin thường vẫn có Realm riêng.

```js
const iframe =
  document.querySelector("iframe");

const OtherArray =
  iframe.contentWindow.Array;

const value =
  new OtherArray();
```

Bây giờ:

```js
value instanceof Array;
// có thể false
```

vì `Array.prototype` của parent Realm khác `Array.prototype` của iframe Realm.

Cross-realm robust check:

```js
Array.isArray(value);
```

được thiết kế để nhận array across realms tốt hơn.

## Jobs

Promise continuation được specification mô tả qua jobs. Browser host integrate jobs với microtask processing trong event loop.

Đây là lý do “ECMAScript Job” và “browser microtask queue” liên quan chặt nhưng không nên đồng nhất tuyệt đối như một khái niệm specification duy nhất.

## Agents

Agents trở nên quan trọng khi có SharedArrayBuffer và Atomics. Nó mô tả execution entities có thể share memory.

---

# 6. Coercion ở spec-level: `ToPrimitive`, `ToPropertyKey` và equality algorithms

## `ToPrimitive`

Object có thể custom primitive conversion:

```js
const price = {
  amount:
    100,

  [Symbol.toPrimitive](hint) {
    if (
      hint === "string"
    ) {
      return `${this.amount} KRW`;
    }

    return this.amount;
  }
};
```

```js
Number(price);
// 100
```

```js
String(price);
// "100 KRW"
```

Nếu không có `Symbol.toPrimitive`, engine có fallback liên quan `valueOf()`/`toString()` tùy hint.

Đây là lý do object coercion không nên được coi là random behavior.

## `ToPropertyKey`

Object property key cuối cùng chủ yếu là string hoặc Symbol.

```js
const object =
  {};

object[1] =
  "one";

Object.keys(object);
// ["1"]
```

`1` được convert thành `"1"` như property key.

## Equality families

JavaScript có nhiều equality semantics.

`===` coi:

```js
NaN === NaN;
// false

0 === -0;
// true
```

`Object.is()`:

```js
Object.is(
  NaN,
  NaN
);
// true

Object.is(
  0,
  -0
);
// false
```

`SameValueZero`, được dùng bởi nhiều collection APIs, coi NaN bằng NaN và +0/-0 tương đương.

```js
[NaN].includes(
  NaN
);
// true
```

```js
new Set([
  NaN,
  NaN
]).size;
// 1
```

### Master Note

Khi collection lookup có behavior khác equality expression bạn nhớ, hãy hỏi “API này dùng equality algorithm nào?” thay vì đoán.

---

# 7. Property Descriptors sâu hơn và Ordinary vs Exotic Objects

Object property không chỉ có `key → value`. Data property có descriptor:

```text
value
writable
enumerable
configurable
```

Accessor property có:

```text
get
set
enumerable
configurable
```

Example:

```js
const user =
  {};

Object.defineProperty(
  user,
  "id",
  {
    value:
      "u1",

    writable:
      false,

    enumerable:
      false,

    configurable:
      false
  }
);
```

`Object.keys(user)` không thấy `id` vì non-enumerable.

### Ordinary vs Exotic

Phần lớn plain objects là ordinary objects. Một số built-ins có internal behavior đặc biệt và được specification gọi là exotic objects, ví dụ:

```text
Array exotic objects
String exotic objects
arguments objects
Module Namespace objects
TypedArrays
Proxy exotic objects
```

Điểm quan trọng là không phải mọi “object property operation” đều hoàn toàn giống plain object.

---

# 8. Array internals: length, sparse arrays, holes và copying methods

Array có `length` behavior đặc biệt:

```js
const values =
  [
    10,
    20,
    30
  ];

values.length =
  1;

console.log(values);
// [10]
```

Setting length nhỏ hơn có thể delete elements.

## Sparse array

```js
const values =
  [];

values[100] =
  "x";

values.length;
// 101
```

Array có length 101 nhưng phần lớn indices không tồn tại.

## Hole khác `undefined`

```js
const a =
  [
    ,
    ,
  ];

const b =
  [
    undefined,
    undefined
  ];
```

```js
0 in a;
// false

0 in b;
// true
```

Một số array methods skip holes, nên sparse arrays tạo behavior khó đoán.

### Senior Rule

Ordinary application state nên tránh sparse arrays. Nếu cần map integer key → value với sparse keyspace, `Map` hoặc object dictionary thường rõ hơn.

## Version note

ES2023 bổ sung `toSorted()`, `toReversed()`, `toSpliced()` và `with()` để có copying versions không mutate original array. Chúng giúp immutable style rõ hơn nhưng vẫn phải kiểm tra target runtime.

---

# 9. Object integrity: `preventExtensions`, `seal`, `freeze` và giới hạn của deep freeze

`Object.preventExtensions(obj)` ngăn add property mới nhưng không nhất thiết ngăn sửa/xóa existing property.

`Object.seal(obj)` làm object non-extensible và existing properties non-configurable.

`Object.freeze(obj)` đi xa hơn: data properties trở thành non-writable và object được seal.

```js
const config =
  Object.freeze({
    apiUrl:
      "/api",

    retry:
      3
  });
```

Nhưng freeze là shallow.

```js
const config =
  Object.freeze({
    nested: {
      enabled:
        true
    }
  });

config.nested.enabled =
  false;
```

Nested object vẫn mutable.

Naive recursive deep freeze có vấn đề với cycles, special built-ins, class instances, typed arrays và performance. Vì vậy “deep freeze everything” không phải default senior design.

---

# 10. Proxy và Reflect: metaprogramming thật sự hoạt động thế nào

Proxy cho phép intercept operations trên object.

```js
const target = {
  name:
    "Kim"
};

const proxy =
  new Proxy(
    target,
    {
      get(
        target,
        property,
        receiver
      ) {
        console.log(
          "read",
          property
        );

        return Reflect.get(
          target,
          property,
          receiver
        );
      }
    }
  );
```

Common traps:

```text
get
set
has
deleteProperty
ownKeys
defineProperty
getOwnPropertyDescriptor
getPrototypeOf
setPrototypeOf
apply
construct
```

`Reflect` cung cấp các operations gần với internal operations hơn:

```js
Reflect.get(
  target,
  key,
  receiver
);
```

thường là lựa chọn tốt trong Proxy handler thay vì tự emulate default behavior.

## Proxy invariants

Proxy không được phép nói dối mọi thứ. Nếu target có property non-configurable/non-writable, một số traps phải tôn trọng invariants. Vi phạm sẽ gây TypeError.

Điều này rất quan trọng cho reactivity frameworks, validators và virtual objects. Proxy không phải unrestricted “magic interception”.

## Revocable Proxy

```js
const {
  proxy,
  revoke
} =
  Proxy.revocable(
    target,
    handler
  );
```

Sau `revoke()`, operations throw. Đây là một primitive thú vị cho capability lifetime.

### Master Note

Proxy mạnh nhưng có cost về predictability, debugging và optimization. Nếu plain function hoặc explicit API giải quyết được problem, đừng dùng Proxy chỉ để code trông clever.

---

# 11. TypedArray, ArrayBuffer, DataView và binary data

JavaScript không chỉ xử lý JSON/text. Khi làm image, crypto, compression, WebSocket binary protocol, worker transfer hoặc file parsing, bạn cần binary APIs.

## ArrayBuffer

```js
const buffer =
  new ArrayBuffer(
    16
  );
```

ArrayBuffer là block raw bytes. Bạn thường không đọc từng byte trực tiếp mà tạo view.

## TypedArray

```js
const bytes =
  new Uint8Array(
    buffer
  );

const ints =
  new Int32Array(
    buffer
  );
```

Hai views có thể nhìn cùng buffer nhưng interpret bytes khác nhau.

TypedArray families gồm:

```text
Int8Array
Uint8Array
Uint8ClampedArray
Int16Array
Uint16Array
Int32Array
Uint32Array
Float32Array
Float64Array
BigInt64Array
BigUint64Array
Float16Array (ES2025)
```

## DataView

DataView cho phép đọc field tại offset và chọn endianness:

```js
const view =
  new DataView(
    buffer
  );

view.setUint32(
  0,
  123456,
  true
);
```

`true` nghĩa little-endian.

### Binary protocol pattern

```text
network/file bytes
↓
ArrayBuffer
↓
DataView / TypedArray
↓
decode fields
↓
validated DTO/domain object
```

Đừng trộn binary parsing với business logic.

## Resizable/transferable ArrayBuffer

ES2024 mở rộng ArrayBuffer với resizing/transfer facilities. Đây là nhóm API mới hơn và cần target compatibility check.

---

# 12. Number, BigInt và integer safety

JavaScript `number` dùng binary floating point. Nó có safe integer range:

```js
Number.MIN_SAFE_INTEGER
Number.MAX_SAFE_INTEGER
```

Check:

```js
Number.isSafeInteger(
  value
);
```

Database BIGINT hoặc Java `long` có thể vượt range chính xác của Number.

```js
Number.MAX_SAFE_INTEGER
// 9007199254740991
```

Nếu backend ID có thể lớn hơn, serialize ID thành string thường an toàn hơn.

## BigInt

```js
const id =
  9007199254740993n;
```

Không mix trực tiếp:

```js
1n + 1;
// TypeError
```

Phải:

```js
1n + 1n;
```

BigInt division là integer division:

```js
5n / 2n;
// 2n
```

JSON không serialize BigInt mặc định:

```js
JSON.stringify({
  id:
    1n
});
// throws
```

Cần explicit wire-format strategy.

### Financial Note

BigInt không giải quyết decimal money tự động. 10.25 không phải integer. Với money, minor units hoặc decimal/arbitrary-precision strategy phù hợp hơn.

---

# 13. Unicode, String internals, TextEncoder/TextDecoder và Base64

JavaScript string dùng UTF-16 code units. Điều này có nghĩa:

```js
"😀".length
```

có thể là 2 dù user nhìn thấy một grapheme.

Nếu xử lý text quốc tế, cần phân biệt:

```text
code unit
code point
grapheme cluster
```

`for...of` trên string iterate code points tốt hơn index-based loop cho nhiều Unicode characters.

```js
for (
  const char
  of "A😀B"
) {
  console.log(char);
}
```

## `TextEncoder`

```js
const encoder =
  new TextEncoder();

const bytes =
  encoder.encode(
    "안녕하세요"
  );
```

Default Web TextEncoder dùng UTF-8.

## `TextDecoder`

```js
const decoder =
  new TextDecoder(
    "utf-8"
  );

const text =
  decoder.decode(
    bytes
  );
```

## Base64 caveat

`btoa()`/`atob()` historically operate on binary-string assumptions. Không nên truyền arbitrary Unicode trực tiếp rồi giả định đúng. Với binary data, chuyển qua bytes rõ ràng.

---

# 14. RegExp nâng cao: Unicode, statefulness và ReDoS

RegExp có state khi dùng `g` hoặc `y`.

```js
const pattern =
  /a/g;

pattern.test(
  "a"
);
// true

pattern.lastIndex;
// changed
```

Reuse cùng RegExp object có thể gây behavior khó hiểu nếu không reset `lastIndex`.

Named groups:

```js
const match =
  /(?<year>\d{4})-(?<month>\d{2})/
    .exec(
      "2026-09"
    );

match.groups.year;
```

Lookahead/lookbehind cho contextual matching.

Unicode property escapes:

```js
/\p{Letter}+/u
```

hữu ích cho multilingual text.

## ReDoS

Regex có pattern ambiguous nested quantifiers có thể gây catastrophic backtracking với crafted input. Đây là vấn đề security/performance thật.

## Dynamic regex

Nếu user text phải được chèn như literal:

```js
const escaped =
  RegExp.escape(
    userInput
  );

const regex =
  new RegExp(
    escaped,
    "i"
  );
```

`RegExp.escape()` được chuẩn hóa trong ES2025. Với runtime cũ, dùng maintained polyfill/helper đúng spec behavior.

---

# 15. `Intl`: localization đúng cách thay vì tự format

Internationalization không chỉ là thêm dấu phẩy.

## NumberFormat

```js
const currency =
  new Intl.NumberFormat(
    "ko-KR",
    {
      style:
        "currency",

      currency:
        "KRW"
    }
  );

currency.format(
  1000000
);
```

## DateTimeFormat

```js
const formatter =
  new Intl.DateTimeFormat(
    "vi-VN",
    {
      dateStyle:
        "medium",

      timeStyle:
        "short",

      timeZone:
        "Asia/Seoul"
    }
  );
```

## Collator

```js
const collator =
  new Intl.Collator(
    "ko"
  );

names.sort(
  collator.compare
);
```

Locale-aware sorting khác code-point sorting.

## PluralRules

Một số ngôn ngữ có nhiều plural categories hơn English. `Intl.PluralRules` giúp localization engine chọn message form đúng.

## RelativeTimeFormat

```js
new Intl.RelativeTimeFormat(
  "en",
  {
    numeric:
      "auto"
  }
).format(
  -1,
  "day"
);
// "yesterday"
```

## Segmenter

`Intl.Segmenter` có thể segment graphemes, words và sentences.

### Master Note

Không hard-code giả định rằng decimal separator luôn `.` hay word boundary luôn space. Khi app đa ngôn ngữ, localization là domain riêng.

---

# 16. Modules ở mức Master: live bindings, cycles, top-level await và import attributes

## Live bindings

Exporter:

```js
export let count =
  0;

export function increment() {
  count += 1;
}
```

Importer:

```js
import {
  count,
  increment
} from "./counter.js";

increment();

console.log(count);
// updated
```

Import không phải snapshot copy đơn giản; nó phản ánh live binding.

## Circular modules

```text
A → B
↑   ↓
└───┘
```

Cycles được standard cho phép, nhưng initialization ordering có thể expose uninitialized binding.

Nếu module cycles khiến code khó reasoning, thường architecture nên extract shared lower-level module.

## Top-level await

ES2022 cho phép module:

```js
const config =
  await loadConfig();

export {
  config
};
```

Nhưng dependent module evaluation có thể bị trì hoãn. Top-level await trong module graph có performance/coordination implications; đừng dùng cho mọi startup request.

## Dynamic import

```js
const module =
  await import(
    "./editor.js"
  );
```

thuộc ES2020.

Bundlers thường dùng dynamic import làm code-splitting hint, nhưng chunk strategy là bundler behavior.

## `import.meta`

```js
import.meta.url
```

cho module metadata.

## Import attributes

ES2025 chuẩn hóa import attributes/JSON module support.

```js
import data
  from "./data.json"
  with {
    type:
      "json"
  };
```

Target runtime/bundler support vẫn phải được kiểm tra.

---

# 17. Package boundaries, CommonJS interop và tree-shaking reality

JavaScript ecosystem không chỉ ESM. Node legacy packages dùng CommonJS:

```js
const library =
  require(
    "library"
  );

module.exports =
  value;
```

ESM và CommonJS có khác biệt về evaluation, live bindings, default import interop và package resolution.

Package hiện đại thường dùng `"exports"` trong `package.json` để xác định public subpaths. Consumer không nên deep-import private file nếu package không export nó.

Tree shaking không phải magic guarantee của `import/export`. Bundler phải prove code unused và side effects không cần giữ.

Module có top-level side effect:

```js
registerGlobalPlugin();
```

có thể buộc bundler giữ module.

`package.json` metadata như `"sideEffects"` có thể ảnh hưởng dead-code elimination. Khai báo sai `"sideEffects": false` có thể làm bundler xóa code cần thiết.

### Senior Rule

Public module boundary và bundler boundary phải align. Đừng expose internal path vô tình rồi sau này không thể refactor.

---

# 18. Transpilation, polyfills, ponyfills và feature detection

## Transpilation

Babel, SWC, TypeScript hoặc bundler có thể transform syntax mới xuống syntax cũ.

Ví dụ optional chaining:

```js
user?.profile?.name
```

có thể được transform cho runtime không support syntax.

Nhưng transform syntax không tạo mọi built-in API.

Runtime cũ có thể vẫn không có:

```text
Promise
Map
Set
Object.groupBy
RegExp.escape
Iterator Helpers
```

## Polyfill

Polyfill patch global/runtime để feature trông như built-in.

## Ponyfill

Ponyfill export local implementation mà không patch global.

Ponyfill thường safer cho library vì không mutate global environment.

## Feature detection

```js
if (
  "structuredClone"
  in globalThis
) {
}
```

tốt hơn browser-sniffing kiểu check user-agent.

### Compatibility Engineering

Hybrid app nên maintain matrix:

```text
feature
minimum Android WebView
minimum iOS/WKWebView
browser desktop minimum
polyfill/fallback
tested devices
```

ES year chỉ là metadata; deployment matrix mới là production truth.

---

# 19. Promise internals: thenables, resolution procedure và unhandled rejection

## Thenable assimilation

Promise không chỉ adopt native Promise. Object có callable `.then` cũng có thể được assimilate.

```js
const thenable = {
  then(resolve) {
    resolve(
      42
    );
  }
};

Promise.resolve(
  thenable
).then(
  console.log
);
```

result:

```text
42
```

Điều này giúp interoperability nhưng cũng nghĩa accessing/using thenable có thể execute arbitrary code.

## Resolution procedure

Khi `.then()` callback return promise/thenable, outer promise adopts state của returned value. Đây là lý do:

```js
loadUser()
  .then(
    (user) =>
      loadOrders(
        user.id
      )
  )
  .then(
    renderOrders
  );
```

works như chain.

Nếu callback throw:

```js
Promise.resolve()
  .then(() => {
    throw new Error(
      "failed"
    );
  })
```

next promise becomes rejected.

## Unhandled rejection

Browser có:

```js
window.addEventListener(
  "unhandledrejection",
  (event) => {
    report(
      event.reason
    );
  }
);
```

Đây là observability safety net, không phải excuse để bỏ local error ownership.

## Version notes

`Promise.withResolvers()` thuộc ES2024. `Promise.try()` thuộc ES2025. Core Promise semantics vẫn dựa trên foundation từ ES2015.

---

# 20. Async generators, iterator closing và cleanup

Async generator:

```js
async function* pages() {
  let page =
    1;

  try {
    while (true) {
      const response =
        await loadPage(
          page
        );

      if (
        response.items.length
          === 0
      ) {
        return;
      }

      yield response.items;

      page += 1;
    }
  } finally {
    console.log(
      "cleanup"
    );
  }
}
```

Consumer:

```js
for await (
  const items
  of pages()
) {
  if (
    shouldStop(
      items
    )
  ) {
    break;
  }
}
```

Breaking iteration can trigger iterator closing semantics và generator `finally`.

Đây là lý do generator/async generator rất phù hợp với resources hoặc lazy streams khi lifecycle được thiết kế đúng.

---

# 21. Web Streams sâu hơn: ReadableStream, WritableStream, TransformStream và BYOB

## ReadableStream

```js
const stream =
  new ReadableStream({
    start(
      controller
    ) {
      controller.enqueue(
        "hello"
      );

      controller.close();
    }
  });
```

## WritableStream

```js
const sink =
  new WritableStream({
    write(chunk) {
      console.log(
        chunk
      );
    }
  });
```

## TransformStream

```js
const upper =
  new TransformStream({
    transform(
      chunk,
      controller
    ) {
      controller.enqueue(
        chunk.toUpperCase()
      );
    }
  });
```

Pipeline:

```js
readable
  .pipeThrough(
    upper
  )
  .pipeTo(
    writable
  );
```

## Locking

Calling:

```js
const reader =
  stream.getReader();
```

locks stream to reader until lock released.

## Cancellation

```js
await reader.cancel();
```

Custom streams cần propagate cancellation upstream hợp lý.

## `tee()`

```js
const [
  a,
  b
] =
  stream.tee();
```

Hai branch đọc cùng source logic, nhưng nếu một consumer chậm hơn, buffering behavior có thể tăng memory.

## BYOB

Bring Your Own Buffer reader cho byte streams có thể giảm allocation bằng cách consumer cung cấp buffer.

Đây là optimization niche cho binary streaming, không phải default API cho ordinary JSON fetch.

---

# 22. Workers, MessageChannel, BroadcastChannel và multi-context coordination

## Dedicated Worker

Đã học ở Senior: phù hợp CPU-heavy work.

## MessageChannel

```js
const channel =
  new MessageChannel();
```

`port1` và `port2` tạo private communication channel.

Có thể transfer `MessagePort` giữa iframe/worker.

## BroadcastChannel

```js
const channel =
  new BroadcastChannel(
    "app-events"
  );

channel.postMessage({
  type:
    "LOGOUT"
});
```

Same-origin tabs/windows có thể nhận.

Use cases:

```text
logout sync giữa tabs
cache invalidation
theme/profile synchronization
coordinating tab roles
```

## Cross-tab races

Nếu hai tabs cùng refresh token hoặc update shared draft, event channel không tự giải quyết consistency. Bạn có thể cần Web Locks API, server-side coordination hoặc leader-election protocol.

### Platform Note

MessageChannel/BroadcastChannel/Web Locks là Web APIs, không phải ECMAScript yearly features.

---

# 23. Shared memory, Atomics và happens-before mental model

SharedArrayBuffer cho multiple agents cùng access memory. Khi share mutable memory, ordinary reasoning “dòng này chạy trước dòng kia” không còn đủ.

Atomics cung cấp operations có synchronization guarantees:

```js
Atomics.add(
  view,
  0,
  1
);
```

```js
Atomics.load(
  view,
  0
);
```

```js
Atomics.store(
  view,
  0,
  10
);
```

`Atomics.wait`/`notify` cho coordination ở worker contexts phù hợp. ES2024 thêm `Atomics.waitAsync()`.

“Happens-before” mental model nghĩa là bạn phải biết synchronization nào guarantee một write visible trước một read khác.

### Master Rule

Nếu team không thể mô tả synchronization protocol bằng lời rõ ràng, message passing tốt hơn shared mutable memory.

---

# 24. Error objects nâng cao: `cause`, `AggregateError`, `SuppressedError` và serialization

## Error cause

ES2022:

```js
try {
  await request();
} catch (error) {
  throw new Error(
    "Load user failed",
    {
      cause:
        error
    }
  );
}
```

Giữ causal chain thay vì replace original context.

## AggregateError

`Promise.any()` có thể reject với AggregateError.

```js
try {
  await Promise.any(
    attempts
  );
} catch (error) {
  if (
    error
    instanceof AggregateError
  ) {
    console.log(
      error.errors
    );
  }
}
```

## SuppressedError

Explicit Resource Management cần represent trường hợp main body throw nhưng cleanup cũng throw. `SuppressedError` giữ cả primary và suppressed error context.

### Version note

Explicit Resource Management đạt Stage 4 sau snapshot ES2026 và được kỳ vọng cho edition tiếp theo; production compatibility vẫn phải kiểm tra.

## Error serialization

```js
JSON.stringify(
  new Error("x")
);
```

thường không chứa message/stack như bạn kỳ vọng vì many Error properties non-enumerable.

Explicit mapper:

```js
function serializeError(
  error
) {
  return {
    name:
      error.name,

    message:
      error.message,

    stack:
      error.stack,

    cause:
      error.cause
  };
}
```

Nhưng production logging phải redact secrets và PII.

---

# 25. Serialization strategies: JSON, structured clone, FormData và binary

Không có một serialization mechanism đúng cho mọi case.

## JSON

Ưu điểm:

```text
portable
human-readable
backend-friendly
```

Nhược điểm:

```text
limited types
no cycles
BigInt problem
Date becomes string
functions/undefined not represented normally
```

## Structured Clone

Hỗ trợ nhiều built-ins và cycles:

```text
Map
Set
Date
RegExp
ArrayBuffer
TypedArray
cycles
```

nhưng không phải wire format cho HTTP.

## FormData

Phù hợp form/file upload.

## URLSearchParams

Phù hợp URL/query/form-encoded simple fields.

## Binary formats

Protobuf/CBOR/custom binary có thể giảm size hoặc tăng performance nhưng tăng tooling/interop complexity.

### Senior Rule

Chọn serialization theo contract boundaries, không chỉ theo “cái nhanh nhất”.

---

# 26. URL security và parser semantics

Bad validation:

```js
if (
  url.startsWith(
    "https://trusted.com"
  )
) {
}
```

Attacker có thể dùng:

```text
https://trusted.com.evil.example
```

Correct approach:

```js
const parsed =
  new URL(
    url
  );

if (
  parsed.origin ===
  "https://trusted.com"
) {
}
```

Nhưng even origin check chưa đủ nếu app cho arbitrary path/query dẫn đến open redirect hoặc privileged action.

### Master Security Note

Security validation nên dựa structured parser và exact allowlist semantics, không dùng substring/prefix guesses.

---

# 27. DOM clobbering và object injection

## DOM clobbering

Browser historically expose certain named DOM elements qua globals/document properties. Code kiểu:

```js
if (
  window.config
) {
}
```

có thể bị DOM element cùng id/name ảnh hưởng trong một số patterns.

Prefer explicit module variables và selectors; không dựa vào implicit globals từ element IDs.

## Object injection

```js
handlers[
  userInput
]();
```

Nếu object prototype có property không mong đợi hoặc input không allowlisted, bạn có thể gọi unintended value.

Safer:

```js
const handler =
  allowedHandlers.get(
    action
  );

if (!handler) {
  throw new Error(
    "Unknown action"
  );
}
```

Map + explicit validation thường rõ hơn cho arbitrary external keys.

---

# 28. postMessage “confused deputy” và capability security

Chỉ check `event.origin` chưa đủ nếu trusted sender có thể bị attacker khiến gửi một privileged command.

Receiver:

```js
window.addEventListener(
  "message",
  (event) => {
    if (
      event.origin !==
      TRUSTED_ORIGIN
    ) {
      return;
    }

    if (
      event.source !==
      expectedWindow
    ) {
      return;
    }

    const message =
      parseMessage(
        event.data
      );

    authorizeMessage(
      message
    );

    handleMessage(
      message
    );
  }
);
```

Validate:

```text
origin
source
schema
message type
payload
authorization
requested capability
```

### Capability-oriented design

Thay vì expose bridge god-object:

```js
window.nativeBridge.doAnything(...)
```

hãy expose minimal capabilities:

```text
startKyc
closeKyc
openSecureDocument
```

với validation riêng.

---

# 29. Plugin sandboxing và versioned contracts

Plugin architecture ở Senior mới tập trung structure. Ở Master, cần nhìn compatibility/security.

Plugin contract:

```js
{
  apiVersion:
    2,

  name:
    "csv-export",

  capabilities:
    [
      "export"
    ],

  init(context) {},

  dispose() {}
}
```

Host cần:

```text
version compatibility
capability negotiation
lifecycle
error isolation
telemetry
permissions
```

Untrusted plugin không nên chạy cùng privilege với app. Sandboxing options có thể gồm:

```text
sandboxed iframe
worker
separate origin
server-side isolation
capability-limited message API
```

### Master Note

Plugin system tạo long-term compatibility burden. Chỉ build khi extensibility thật sự là requirement.

---

# 30. Functional patterns nâng cao: Result/Option style, transducers và lenses

JavaScript không có native algebraic data types như một số FP languages, nhưng tagged objects có thể model Result:

```js
function success(
  value
) {
  return {
    type:
      "success",

    value
  };
}

function failure(
  error
) {
  return {
    type:
      "failure",

    error
  };
}
```

TypeScript làm pattern này mạnh hơn bằng discriminated unions, nhưng JavaScript runtime concept vẫn hợp lệ.

## Transducers

Transducer là cách compose transformations mà không tạo intermediate arrays cho mỗi `map`/`filter`.

Conceptually:

```text
filter
+
map
+
reduce
→ một reducer pipeline
```

Nó hữu ích ở library/high-volume pipelines nhưng thường quá abstract cho ordinary application code. Iterator Helpers ES2025 cũng giải quyết nhiều use case lazy pipeline ergonomic hơn.

## Lenses

Lens là FP abstraction cho immutable nested get/update. Nó phổ biến trong một số ecosystems nhưng hiếm khi cần cho enterprise JavaScript thông thường.

### Master Rule

Biết pattern tồn tại không đồng nghĩa dùng pattern. Mastery bao gồm khả năng bỏ qua abstraction không tạo enough value.

---

# 31. Capability-oriented API và resource-owning API

API nên expose tối thiểu quyền caller cần.

Bad:

```js
runFeature(
  app
);
```

trong đó `app` có network, storage, auth, analytics, DOM, config, native bridge.

Better:

```js
runFeature({
  loadUser,
  saveUser
});
```

Feature không có quyền truy cập thứ khác.

Resource-owning API phải nói rõ ownership:

```js
const subscription =
  subscribe();

subscription.dispose();
```

hoặc:

```js
const unsubscribe =
  subscribe();
```

Caller biết phải cleanup.

Cancellation-aware API:

```js
async function load(
  {
    signal
  } = {}
) {
}
```

Error-stable API nên map vendor-specific errors sang contract ứng dụng khi cần, thay vì cho `AxiosError`, WebSquare callback code hoặc native exception leak khắp hệ thống.

---

# 32. Advanced Performance Methodology: benchmark đúng, profile đúng

Microbenchmark:

```js
const start =
  performance.now();

for (
  let i = 0;
  i < 1_000_000;
  i += 1
) {
  fn();
}

console.log(
  performance.now()
    - start
);
```

có thể misleading vì JIT warmup, GC, branch prediction, dead code, hardware, background tabs.

### Correct process

```text
define user-visible problem
↓
capture representative workload
↓
profile
↓
identify hotspot
↓
form hypothesis
↓
change
↓
measure again
↓
regression budget
```

## Allocation profiling

Look for:

```text
temporary arrays
large strings
JSON parse/stringify
object churn
closures retaining data
DOM nodes
```

## Memory profiling

Heap snapshots + retainer path answer question:

```text
“Object này vẫn reachable qua chain nào?”
```

## Flame charts

Wide blocks cho biết function/task chiếm nhiều thời gian. Đừng chỉ nhìn function name; tìm repeated path, layout, GC, scripting, painting.

## GC pressure

High allocation rate có thể tăng GC cost. Nhưng object pooling thủ công trong application code hiếm khi nên làm trước profiler evidence.

## Cold vs warm

Measure cả:

```text
first load
first interaction
cache empty
JIT cold
```

và:

```text
subsequent use
cache warm
optimized code
```

---

# 33. Testing Mastery: fuzzing, deterministic scheduling và type of risk

Testing strategy không chỉ unit/integration/E2E.

## Fuzzing

Feed malformed/unexpected values vào:

```text
URL parsers
message handlers
binary decoders
bridge payloads
regex
JSON schemas
```

Fuzzing tốt để tìm crash và security edge cases.

## Property-based testing

Thay vì chỉ vài examples, define invariant:

```text
decode(encode(x)) == x
sort preserves length
normalize(normalize(x)) == normalize(x)
```

framework generate many cases.

## Mutation testing

Tool cố tình đổi code:

```text
>
→
>=
```

Nếu tests vẫn pass, suite có thể chưa bắt business distinction.

## Deterministic scheduler

Race-condition tests khó nếu dựa real timing. Advanced harness có thể kiểm soát timers/events/completion ordering để reproduce sequence.

## Time abstraction

Thay vì dùng `Date.now()` trong domain khắp nơi:

```js
function createService({
  now =
    Date.now
}) {
}
```

Test inject:

```js
now:
  () =>
    123456
```

### Senior Rule

Testability tăng khi external effects có dependency seam rõ: clock, randomness, network, storage, bridge, workers.

---

# 34. Legacy JavaScript literacy: IIFE, `arguments`, constructor prototypes và callback APIs

Master JavaScript không chỉ hiểu code mới. Enterprise code thường có style pre-ES2015.

## IIFE

```js
(function () {
  const privateValue =
    1;

  window.app = {
    run() {}
  };
})();
```

Trước native modules, IIFE tạo private scope.

## `arguments`

```js
function sum() {
  let total =
    0;

  for (
    let i = 0;
    i < arguments.length;
    i += 1
  ) {
    total +=
      arguments[i];
  }

  return total;
}
```

Modern rest parameters dễ dùng hơn, nhưng bạn phải đọc được legacy code.

## Constructor + prototype

```js
function User(
  name
) {
  this.name =
    name;
}

User.prototype.greet =
  function () {
    return `Hello ${this.name}`;
  };
```

Class syntax chỉ là modern syntax trên prototype model.

## Callback API

```js
loadData(
  (
    error,
    data
  ) => {
  }
);
```

Adapter to Promise:

```js
function loadDataAsync() {
  return new Promise(
    (
      resolve,
      reject
    ) => {
      loadData(
        (
          error,
          data
        ) => {
          if (error) {
            reject(
              error
            );
            return;
          }

          resolve(
            data
          );
        }
      );
    }
  );
}
```

---

# 35. Toolchain semantics: Babel, SWC, TypeScript, bundlers và source maps

Code source có thể đi qua:

```text
TypeScript
↓
Babel/SWC
↓
bundler
↓
minifier
↓
polyfill/runtime helpers
↓
browser
```

Khi production bug xảy ra, cần biết layer nào transform gì.

## Babel/SWC

Transform syntax/plugins theo target.

## TypeScript

Có thể type-check và transpile syntax, nhưng TypeScript types erased.

## Bundler

Resolve modules, combine chunks, code split, asset pipeline.

## Minifier

Rename locals, fold constants, remove dead code, compress syntax.

Code không nên dựa vào `function.name`/`class.name` nếu minifier có thể đổi và contract không bảo toàn.

## Source maps

Map minified generated location về source. Production error reporting gần như cần source maps để stack useful.

Security policy có thể yêu cầu private source-map upload thay vì public serving.

---

# 36. Java backend interoperability ở mức Master

Wire contract giữa Java và JavaScript có các mismatch quan trọng.

## `long` / BIGINT

Serialize large IDs as string khi có thể vượt safe integer.

## `BigDecimal`

Serialize decimal string hoặc integer minor units tùy domain.

## Date/Time

Java types:

```text
LocalDate
LocalDateTime
OffsetDateTime
Instant
ZonedDateTime
```

không có cùng semantics.

`LocalDateTime` không mang timezone. `Instant` là absolute point. `OffsetDateTime` mang offset.

Frontend DTO phải biết backend đang gửi gì:

```json
"2026-09-12T15:30:00+09:00"
```

khác:

```json
"2026-09-12T15:30:00"
```

## Enum evolution

Backend thêm enum member mới có thể làm frontend exhaustive switch đi vào default/unhandled path. External data phải được parsed với forward-compatibility strategy.

## Nullability

Java annotations/Optional/database nullability phải map rõ sang JSON. Đừng dùng `null`, missing field và empty string thay nhau tùy endpoint.

---

# 37. WebSquare interoperability: typed boundary ngay cả khi JavaScript thuần

Dù chưa migrate sang TypeScript, bạn vẫn có thể kiến trúc theo typed contract mental model.

Bad:

```text
scwin event handler
→ đọc DataMap
→ mutate DataList
→ gọi submission
→ handle native plugin
→ render popup
```

tất cả trong một function.

Better:

```text
WebSquare Event
↓
Page Controller
↓
Feature Service
↓
Submission Adapter
↓
Mapper
↓
Domain logic
```

Submission callback legacy có thể wrap thành Promise.

```js
function executeSubmission(
  submission
) {
  return new Promise(
    (
      resolve,
      reject
    ) => {
      // translate framework callback
      // into stable Promise contract
    }
  );
}
```

DataList/DataMap should be treated as infrastructure representation, not domain model.

---

# 38. Native WebView contract versioning

Native ↔ JavaScript communication là distributed-system-like boundary.

Message nên có:

```js
{
  version:
    1,

  type:
    "KYC_COMPLETED",

  requestId:
    "abc",

  payload: {
    ...
  }
}
```

Error:

```js
{
  version:
    1,

  type:
    "KYC_FAILED",

  requestId:
    "abc",

  error: {
    code:
      "CAMERA_DENIED",

    message:
      "..."
  }
}
```

Contract cần:

```text
version
message type
request/correlation id
payload schema
error schema
backward compatibility
timeout/cancellation semantics
```

Deep links như `ekyc://...` phải được native side validate scheme/host/path/payload chặt, không chỉ string-prefix matching.

---

# 39. React interoperability: JavaScript mastery phía dưới framework

React concepts map vào JavaScript:

```text
hook closure
→ closure semantics

dependency array
→ identity + closure capture

state updates
→ reference identity + immutability

effect cleanup
→ resource ownership

reducer
→ state machine/reducer pattern

event callback
→ function identity

memoization
→ cache with dependency semantics
```

Một bug React stale closure không phải vì “React random”; nó thường bắt đầu từ lexical closure + render lifecycle.

TypeScript sau đó bổ sung static contracts, nhưng runtime semantics vẫn là JavaScript.

---

# 40. Cross-realm, cross-window và `instanceof` review

Các built-in constructors thuộc Realm.

```js
value instanceof Error
```

có thể fail với Error từ iframe Realm.

Trong library code nhận cross-context values, structural validation hoặc brand-specific helpers đáng tin hơn `instanceof` cho nhiều types.

Examples:

```js
Array.isArray(
  value
);
```

được thiết kế cross-realm.

For Error-like:

```js
function isErrorLike(
  value
) {
  return (
    value !== null
    &&
    typeof value
      === "object"
    &&
    typeof value.message
      === "string"
  );
}
```

Dùng structural check chỉ khi semantics phù hợp; không phải mọi object có `message` đều thật sự Error.

---

# 41. Temporal: Date successor và cách đọc feature post-snapshot

Temporal là case study hoàn hảo về versioning.

Temporal giải quyết nhiều hạn chế của `Date`:

```text
immutable types
time-zone aware operations
date-only / time-only types
DST-safe arithmetic
explicit calendar/timezone semantics
```

Examples concepts:

```text
Temporal.Instant
Temporal.PlainDate
Temporal.PlainDateTime
Temporal.ZonedDateTime
Temporal.Duration
```

Temporal đạt **Stage 4 vào tháng 7/2026**, sau khi ECMAScript 2026 snapshot đã được phê duyệt cuối tháng 6/2026. Vì vậy tại thời điểm này, cách gọi chính xác không phải “Temporal là ES2026”, mà là “finished proposal post-ES2026, expected for a later yearly edition, with implementation rollout still in progress”.

Đây là mental model bạn nên áp dụng cho mọi feature mới:

```text
proposal stage
↓
finished?
↓
which yearly snapshot?
↓
browser engines?
↓
actual app targets?
```

---

# 42. Explicit Resource Management: `using`, `await using`, `DisposableStack`

Explicit Resource Management đưa deterministic disposal semantics vào JavaScript.

Concept:

```js
{
  using resource =
    acquireResource();

  use(
    resource
  );
}
// dispose khi scope kết thúc
```

Async:

```js
{
  await using resource =
    await acquireAsyncResource();

  await use(
    resource
  );
}
```

Protocols:

```text
Symbol.dispose
Symbol.asyncDispose
DisposableStack
AsyncDisposableStack
SuppressedError
```

Điều này đưa pattern:

```text
acquire
try
use
finally release
```

thành language-level syntax/protocol.

### Version note

Proposal này đã đạt Stage 4 sau snapshot ECMAScript 2026 và đang hướng tới edition tiếp theo. Vì syntax rất mới, production phải check parser/toolchain/browser support.

### Master Note

Đây không phải Rust ownership system. Nó giúp deterministic cleanup, nhưng aliasing/resource architecture vẫn phải được thiết kế đúng.

---

# 43. Joint Iteration và những feature “post-ES2026” khác nên nhìn thế nào

TC39 tiếp tục chuẩn hóa iteration ergonomics sau Iterator Helpers ES2025. Những proposal đạt Stage 4 sau snapshot 2026 có thể xuất hiện ở edition kế tiếp. Bạn không cần học thuộc danh sách này trong main curriculum.

Cách đúng là giữ một **post-snapshot watchlist** riêng:

```text
Temporal
Explicit Resource Management
Atomics.pause
Joint Iteration
...
```

Chỉ đưa feature vào production guidelines khi status final và target compatibility đủ.

Đây là lý do Master file không cố “đóng băng JavaScript ở năm 2026”. Nó dạy quy trình cập nhật.

---

# 44. Master Security Checklist theo data flow

Thay vì memorize attack names, trace:

```text
Source
↓
Transformation
↓
Sink
↓
Privilege
```

Sources:

```text
URL
API response
postMessage
localStorage
native callback
user form
third-party SDK
```

Sinks:

```text
innerHTML
eval
Function
location/navigation
dynamic object key
native bridge command
network request
logging system
```

Questions:

```text
Source có trust được không?
Có schema/allowlist không?
Transformation có decode/normalize đúng không?
Sink có interpret value như code/HTML/URL/key không?
Privilege của sink là gì?
```

Mental model này bao phủ XSS, object injection, URL injection, prototype pollution, confused deputy và nhiều bridge vulnerabilities.

---

# 45. Master API Review Checklist

Khi thiết kế API/library/module, hãy hỏi theo thứ tự.

**Data contract:** input/output chính xác là gì? Có nullable/missing distinctions không? Có external data cần runtime validation không?

**Ownership:** object/resource thuộc ai? Caller có được mutate không? Cleanup ở đâu?

**Async:** operation sequential/concurrent? có timeout/cancellation? race/stale handling?

**Errors:** expected failure vs programmer error? error code stable? original cause preserved?

**Security:** caller được capability gì? input trust boundary ở đâu?

**Versioning:** contract có phải dùng lâu dài giữa native/web/plugin/service không?

**Observability:** nếu fail production, có request ID, release ID, logs/traces không?

**Compatibility:** syntax/API có chạy trên target WebView không?

**Testability:** clock/network/storage/random/native dependencies có seam không?

Một API senior không chỉ “type signature đẹp”; nó phải khó dùng sai.

---

# 46. Master Gotchas cần hiểu bằng semantics, không học thuộc

`typeof null === "object"` là legacy quirk.

`NaN !== NaN`; dùng `Number.isNaN` hoặc `Object.is` tùy intent.

`0 === -0` nhưng `Object.is(0, -0)` false.

Sparse-array hole khác `undefined`.

`delete array[index]` tạo hole, không shift/shrink length.

`Array.prototype.sort()` mutate original; `toSorted()` không mutate.

Object spread là shallow.

`Object.freeze()` shallow.

`Map` object keys dùng identity:

```js
const map =
  new Map();

map.set(
  {},
  1
);

map.get(
  {}
);
// undefined
```

Regex với `g`/`y` có `lastIndex` state.

`Promise.race()` không cancel losing promises.

`async forEach` không await callbacks theo cách nhiều người kỳ vọng.

`JSON.stringify(Error)` thường không serialize useful fields.

`JSON.stringify(BigInt)` throw.

Top-level await có thể trì hoãn entire dependent module graph.

Dynamic import có thể fail vì chunk deployment mismatch dù source code đúng.

`instanceof` có cross-realm pitfalls.

Getter/property access có thể chạy arbitrary code.

Proxy làm ordinary-looking property operation chạy custom trap.

Mục tiêu của danh sách này không phải học thuộc, mà là nhớ rằng JavaScript có semantics sâu dưới syntax.

---

# 47. Compatibility Mastery: yearly ECMAScript, Baseline và enterprise WebView

Ba loại thông tin thường bị trộn:

```text
ECMAScript Edition
Browser Baseline
Project Target Matrix
```

**ECMAScript Edition** trả lời feature thuộc standard snapshot nào.

**Baseline/browser compatibility** trả lời feature có broadly available trong modern browsers không.

**Target matrix** trả lời sản phẩm của bạn có dùng được không.

Ví dụ feature Baseline 2025 vẫn có thể unusable nếu corporate Android device ship WebView version khóa từ 2023.

Đối với hybrid banking app, target matrix nên được version-controlled cùng project docs.

Ví dụ:

```text
Feature: RegExp.escape
Standard: ES2025
Chrome target: supported?
Android WebView min: ?
iOS WKWebView min: ?
Fallback: helper/polyfill
Tests: device list
```

Đây là cách để version notes sống lâu mà không biến codebase thành archaeology.

---

# 48. Khi nào JavaScript core có thể coi là “master-ready”?

Không có nghĩa bạn nhớ toàn bộ ECMA-262.

Bạn nên có thể làm những việc sau:

Khi gặp coercion edge case, bạn biết tìm `ToPrimitive`, equality algorithm hoặc property-key conversion thay vì Google một câu đố ngẫu nhiên.

Khi gặp `instanceof` fail trong iframe, bạn nghĩ tới Realm.

Khi browser memory tăng sau navigation, bạn tìm retainer path, detached DOM, listener, closure, cache, worker và resource lifecycle.

Khi async result sai thứ tự, bạn nghĩ tới race/cancellation/versioning.

Khi network payload lớn, bạn cân nhắc streaming/backpressure/worker/serialization cost.

Khi feature mới xuất hiện, bạn phân biệt proposal stage, yearly standard, engine support và deployment target.

Khi module build fail, bạn phân biệt language module semantics, package exports, bundler resolution, CommonJS interop và tree shaking.

Khi security bug liên quan bridge/postMessage, bạn trace source → validation → capability → sink.

Khi type/tooling layer phức tạp, bạn vẫn quay lại JavaScript runtime semantics để xác định truth.

---

# 49. Cách học file Master này

Không nên đọc toàn bộ một lần rồi cố nhớ.

**Pass 1 — Spec mental model:** đọc các chương về abstract operations, realms, property descriptors và exotic objects. Mục tiêu là biết vocabulary và biết tra spec.

**Pass 2 — Data representations:** học arrays internals, binary data, Unicode, BigInt, RegExp và Intl.

**Pass 3 — Modules/runtime:** học modules, CommonJS/toolchain, promise internals, streams, workers và shared memory.

**Pass 4 — Security/architecture:** học URL security, object injection, capability API, plugin contracts và native bridge versioning.

**Pass 5 — Production mastery:** học performance methodology, testing advanced, compatibility engineering và interop.

Sau mỗi pass, lấy một module thật trong project và hỏi: “Chủ đề này có hiện diện ở đây không?”. Học Master bằng code thật hiệu quả hơn đọc như dictionary.

---

# 50. Bộ JavaScript hoàn chỉnh sau khi thêm Master

```text
01. JavaScript Beginner
    cú pháp + foundation + DOM/API cơ bản

02. JavaScript Intermediate
    semantics + prototype + event loop + patterns

03. JavaScript Senior
    runtime + memory + concurrency
    performance + security + architecture

04. JavaScript Master Supplement
    spec-level semantics
    exotic objects / Proxy
    binary / Unicode / Intl
    modules/toolchain
    cross-realm
    streams/workers/shared memory
    advanced security
    advanced testing/performance
    compatibility/versioning
    Java/WebSquare/native interoperability
```

Bốn file này nên được coi là một progression duy nhất. Master không thay Senior; nó chỉ cover những vùng quá sâu hoặc quá niche để nhét vào learning flow chính.

---

# Appendix A — Version map cho những feature Master thường gặp

Không cần học thuộc bảng này; dùng để định vị lịch sử.

| Feature | Standard / status |
| --- | --- |
| Proxy / Reflect | ES2015 |
| Symbol / iterators / generators | ES2015 |
| SharedArrayBuffer / Atomics | ES2017 core |
| Async iterators / async generators | ES2018 |
| Dynamic `import()` / `import.meta` | ES2020 |
| WeakRef / FinalizationRegistry | ES2021 |
| Class fields/private elements, top-level await, Error cause | ES2022 |
| Copying Array methods (`toSorted`...) | ES2023 |
| Resizable/transferable ArrayBuffer, `Promise.withResolvers`, `Object.groupBy`, `Map.groupBy`, `Atomics.waitAsync` | ES2024 |
| Iterator Helpers, Set operations, `RegExp.escape`, `Promise.try`, import attributes/JSON modules, Float16Array family | ES2025 |
| ECMAScript 2026 | Current approved yearly snapshot |
| Temporal | Stage 4 after ES2026 snapshot; expected later edition |
| Explicit Resource Management | Stage 4 after ES2026 snapshot; expected later edition |

---

# Appendix B — Nguồn authoritative nên dùng

Khi cần xác minh standard/version:

```text
ECMA-262 latest specification
https://tc39.es/ecma262/

Ecma International ECMA-262 editions
https://ecma-international.org/publications-and-standards/standards/ecma-262/

TC39 finished proposals
https://github.com/tc39/proposals/blob/main/finished-proposals.md
```

Khi cần browser compatibility:

```text
MDN JavaScript Reference
https://developer.mozilla.org/en-US/docs/Web/JavaScript

MDN Web APIs
https://developer.mozilla.org/en-US/docs/Web/API/
```

Khi cần proposal draft:

```text
TC39 proposal repository/spec page
```

Không dùng một blog cũ làm nguồn duy nhất cho proposal status hoặc syntax experimental.

---

# Kết luận

Sau Beginner, Intermediate và Senior, phần còn thiếu của JavaScript không còn nằm ở việc học thêm vài method. Nó nằm ở khả năng **đọc semantics, hiểu runtime boundaries, xử lý representation khác JSON, thiết kế module/package contract, làm việc với multiple execution contexts, đo performance đúng cách, bảo vệ capability boundaries và quản lý compatibility qua nhiều version/runtime**.

Đây cũng là điểm khác biệt giữa người “biết JavaScript rất nhiều API” và người có thể chịu trách nhiệm một hệ thống JavaScript lớn.

Mental model cuối cùng nên là:

```text
Specification
    giải thích language truth

Runtime / Engine / Host
    quyết định cách truth đó được thực thi

Toolchain
    biến source thành code deployment

Architecture
    kiểm soát dependency, state và ownership

Security
    kiểm soát trust và capability

Observability / Testing
    kiểm chứng behavior production

Compatibility
    quyết định feature nào thực sự dùng được
```

Khi bạn có thể nhìn một bug hoặc một feature mới và xác định đúng nó thuộc lớp nào trong sơ đồ trên, JavaScript core của bạn đã ở mức master-ready.
