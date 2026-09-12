# JavaScript Beginner — Giáo trình nền tảng từ con số 0

> **Mục tiêu của tài liệu này**: giúp người chưa có nền tảng JavaScript có thể đọc từ đầu đến cuối và hiểu được JavaScript theo đúng mental model, thay vì chỉ học thuộc cú pháp. Phần này đi chậm, giải thích vì sao một cú pháp tồn tại, cách nó hoạt động, khi nào nên dùng, lỗi người mới thường gặp, và liên hệ với cách viết code thực tế trong frontend/WebSquare/React sau này.
>
> **Nguyên tắc học**: không cố nhớ toàn bộ method. Hãy hiểu nhóm khái niệm, sau đó dùng ví dụ để hình thành phản xạ. Khi sang Intermediate, bạn sẽ đào sâu cơ chế bên trong như closure, `this`, prototype và event loop.

---

<!-- VERSION-GUIDE-BEGIN -->
# Cách đọc “version JavaScript” trong tài liệu này

JavaScript core được chuẩn hóa dưới tên **ECMAScript** trong tiêu chuẩn ECMA-262. Trước năm 2015, cộng đồng thường gọi các phiên bản bằng số edition như ES3 và ES5. Phiên bản thứ sáu là trường hợp đặc biệt vì bạn sẽ gặp cả hai tên **ES6** và **ES2015**; hai tên này chỉ cùng một phiên bản. Từ ES2016 trở đi, TC39 chuyển sang chu kỳ phát hành hằng năm nên tên chính thức thường gắn với năm: ES2017, ES2018, ES2020, ES2025, ES2026. Tính đến tháng 9 năm 2026, snapshot chính thức mới nhất là **ECMAScript 2026, ECMA-262 17th edition**. Điều này không có nghĩa bạn phải học lại JavaScript mỗi năm; các phiên bản mới chủ yếu bổ sung feature và tinh chỉnh semantics trên nền ngôn ngữ cũ.

Khi một chương có ghi **Version note — ES2015** hay **Version note — ES2020**, điều đó chỉ nói feature được đưa vào ECMAScript standard ở edition nào. Nó **không đồng nghĩa mọi browser hoặc WebView đều support feature đó ngay lập tức**. Một Android System WebView trong ứng dụng enterprise có thể cũ hơn Chrome desktop rất nhiều. Ngược lại, browser đôi khi thử triển khai proposal trước khi yearly standard được phát hành. Vì thế version chuẩn giúp bạn hiểu lịch sử và thế hệ của syntax/API, còn quyết định production phải dựa vào browser/WebView compatibility thực tế.

Bạn cũng cần tách ECMAScript khỏi Web APIs. `const`, arrow function, Promise, Map, Set, optional chaining hay `toSorted()` là ECMAScript features. `document`, DOM events, `fetch`, `localStorage`, `URL`, `AbortController`, WebSocket và Web Workers là API do web platform cung cấp, nên chúng không có “ES2020/ES2021 version” theo cách feature của ECMA-262 có. Đây là lý do một project có thể hỗ trợ syntax JavaScript mới nhưng vẫn thiếu một Web API, hoặc ngược lại.

Một từ khác thường gặp là **ESNext**. Đây không phải một version cố định. Nó chỉ có nghĩa “những feature hướng tới phiên bản tiếp theo ở thời điểm bài viết được viết”. Vì vậy một bài năm 2020 và một bài năm 2026 dùng chữ ESNext có thể đang nói về hai nhóm feature khác nhau. Khi đọc code hoặc tài liệu, hãy quan tâm **tên feature + trạng thái chuẩn + compatibility**, đừng chỉ nhìn chữ ESNext.

## Timeline tối thiểu nên hiểu

Bạn không cần học thuộc lịch sử, nhưng vài cột mốc giúp đọc code rất nhanh. **ES5 (2009)** đưa strict mode, JSON support và nhiều array/object APIs vào chuẩn. **ES2015/ES6** là bước nhảy lớn với `let`, `const`, arrow functions, template literals, destructuring, classes, modules, Promise, Map/Set, Symbol, iterator và generator. **ES2016** thêm `**` và `Array.prototype.includes()`. **ES2017** đưa `async/await` vào chuẩn. **ES2018** thêm async iteration và object rest/spread. **ES2019** thêm `flat()`, `flatMap()` và `Object.fromEntries()`. **ES2020** thêm BigInt, optional chaining, `??`, dynamic `import()` và `Promise.allSettled()`. **ES2021** thêm `Promise.any()`, `AggregateError`, `replaceAll()`, logical assignment và WeakRef/FinalizationRegistry. **ES2022** thêm top-level `await`, class fields/private elements/static blocks, `Error.cause`, `.at()` và `Object.hasOwn()`. **ES2023** thêm nhóm copying array methods như `toSorted()`, `toReversed()`, `toSpliced()`, `with()`, cùng `findLast()`. **ES2024** thêm `Promise.withResolvers()`, `Object.groupBy()`, `Map.groupBy()` và resizable/transferable ArrayBuffer facilities. **ES2025** thêm Iterator Helpers, Set operations, `RegExp.escape()`, `Promise.try()` và import attributes/JSON-module support. **ES2026** là snapshot chính thức hiện hành; khi feature mới hơn xuất hiện, tài liệu nên ghi rõ proposal/post-snapshot thay vì đoán nó thuộc năm nào.

Mục tiêu của version note không phải để bạn đi thi thuộc “method X ra năm Y”. Nó giúp bạn hiểu vì sao code cũ dùng cách dài hơn, vì sao Babel từng cần thiết cho một số syntax, và vì sao feature mới như `toSorted()` cần kiểm tra WebView target trong khi `map()` gần như không còn là vấn đề compatibility trên runtime hiện đại.
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — JavaScript là gì và nó đứng ở đâu trong một ứng dụng web?

JavaScript là ngôn ngữ lập trình được dùng rộng rãi nhất ở phía trình duyệt. Nếu HTML mô tả cấu trúc của trang và CSS mô tả cách trang được trình bày, thì JavaScript xử lý hành vi và logic: click button, validate form, gọi API, cập nhật dữ liệu, mở popup, thay đổi state của màn hình, xử lý timer, điều khiển WebView hoặc giao tiếp với native plugin trong ứng dụng hybrid.

Điều đầu tiên cần phân biệt là **JavaScript language** và **Browser APIs**. Những thứ như `let`, `const`, object, array, function, class hay Promise thuộc về ngôn ngữ JavaScript/ECMAScript. Trong khi đó `document`, `fetch`, `localStorage`, `setTimeout`, `WebSocket`, `AbortController` hay `MutationObserver` là API do môi trường chạy cung cấp. Trên browser, JavaScript được browser cung cấp những API này. Trên Node.js, bạn có một tập API khác. Trong WebView của hybrid app, bạn vừa có JavaScript, vừa có browser/WebView APIs, và đôi khi còn có bridge do native side expose.

Vì vậy khi một đoạn code không chạy, câu hỏi đầu tiên của developer có kinh nghiệm là: lỗi nằm ở **language**, **browser API**, **runtime**, **network**, hay **framework**? Tư duy tách layer này giúp bạn debug nhanh hơn rất nhiều.

Tên chuẩn của lõi ngôn ngữ là ECMAScript. Khi tài liệu nhắc ES2015, ES2020 hay ES2025, đó là các phiên bản của chuẩn. Bạn không cần thuộc năm của từng feature, nhưng cần hiểu JavaScript hiện đại được bổ sung dần qua các phiên bản ECMAScript.

### Ví dụ đầu tiên

```js
const userName = "Kim";

function greet(name) {
  return `Hello ${name}`;
}

console.log(greet(userName));
```

Đoạn code này chỉ dùng JavaScript core. Nếu thêm:

```js
document.querySelector("#message").textContent = greet(userName);
```

thì `document` và `querySelector` thuộc Browser DOM API.

### Senior note

Đừng học JavaScript theo kiểu “mọi thứ tôi thấy trong browser đều là JavaScript”. Sau này khi học React, WebSquareJS hoặc Node.js, việc biết ranh giới giữa language và runtime giúp bạn biết phần nào là kiến thức dùng chung, phần nào là framework/platform-specific.

---

# Chương 2 — Cách JavaScript thực thi code ở mức nền tảng

Ở mức Beginner, bạn chưa cần hiểu JIT compiler hay engine optimization. Nhưng bạn cần biết rằng JavaScript thực thi các câu lệnh synchronous theo thứ tự, function được gọi thì execution đi vào function, sau đó quay lại vị trí gọi khi function kết thúc.

```js
console.log("A");

function run() {
  console.log("B");
}

run();

console.log("C");
```

Output là:

```text
A
B
C
```

Điều đáng chú ý là asynchronous work không phá ngang đoạn synchronous đang chạy. Ví dụ:

```js
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

console.log("C");
```

Output thông thường là:

```text
A
C
B
```

`setTimeout(..., 0)` không có nghĩa “chạy ngay bây giờ”. Nó có nghĩa gần hơn với “hãy schedule callback này để có cơ hội chạy sau current work”. Tại sao Promise callback lại chạy trước timer callback sẽ được giải thích kỹ ở Intermediate khi học event loop và microtask.

Mental model quan trọng nhất ở đây là: **synchronous code chạy trước, asynchronous callback được schedule**. Khi code frontend bị “đơ”, rất nhiều khi nguyên nhân là synchronous task chạy quá lâu trên main thread.

---

# Chương 3 — Statement, expression, block và comment

Một **expression** là đoạn code tạo ra value. Ví dụ `1 + 2`, `user.name`, `isActive ? "Y" : "N"` đều là expression. Một **statement** là câu lệnh điều khiển hoặc thực hiện hành động, ví dụ khai báo biến, `if`, `for`, `return`.

```js
const total = 10 + 20;
```

Ở đây `10 + 20` là expression, còn toàn bộ khai báo `const total = ...` là statement.

Block là phần code nằm trong `{}`:

```js
if (total > 20) {
  const message = "large";
  console.log(message);
}
```

Block quan trọng vì `let` và `const` có **block scope**. Variable `message` chỉ tồn tại trong block đó.

Comment một dòng:

```js
// calculate final total
```

Comment nhiều dòng:

```js
/*
  temporary workaround
  remove after API v2 rollout
*/
```

Một thói quen tốt là comment **lý do** hoặc constraint, không comment thứ code đã quá rõ. Comment kiểu `// increment count` ngay trên `count += 1` không thêm giá trị.

---

# Chương 4 — `const`, `let`, `var`: cách khai báo biến đúng trong JavaScript hiện đại

> **Version note — ES2015/ES6:** `var` đã tồn tại từ JavaScript rất sớm. `let` và `const` được chuẩn hóa ở ES2015 cùng lexical block scope. Vì vậy legacy code trước ES2015 thường dùng `var` ở mọi nơi, còn code hiện đại ưu tiên `const` rồi mới đến `let`.

JavaScript hiện đại có ba từ khóa khai báo biến: `const`, `let`, `var`. Quy tắc thực dụng cho code mới là: **dùng `const` mặc định, dùng `let` khi cần reassign, tránh `var` trừ khi đọc legacy code**.

```js
const apiUrl = "/api/users";
```

`apiUrl` không thể được gán sang value khác:

```js
// apiUrl = "/api/orders"; // lỗi
```

Nếu value cần thay đổi:

```js
let retryCount = 0;

retryCount += 1;
```

Một hiểu nhầm phổ biến là `const` làm object immutable. Thực tế `const` chỉ khóa **binding**, không khóa nội dung object.

```js
const user = {
  name: "Kim"
};

user.name = "Lee"; // hợp lệ
```

Nhưng:

```js
// user = {}; // không hợp lệ
```

`var` có function scope và hoisting semantics cũ. Bạn sẽ gặp nó trong code WebSquare/legacy JavaScript, nhưng không nên dùng cho code mới nếu không có lý do đặc biệt.

### Language idiom

```js
const users = [];
const config = {};
const MAX_RETRY = 3;

let currentPage = 1;
let loading = false;
```

### Senior note

Ưu tiên `const` giúp giảm số chỗ binding có thể thay đổi. Điều này làm reasoning dễ hơn và giảm bug, chứ không phải vì `const` “tối ưu nhanh hơn”.

---

# Chương 5 — Primitive types và object types

JavaScript có bảy primitive types: `string`, `number`, `boolean`, `undefined`, `null`, `bigint`, `symbol`. Ngoài những primitive này, còn lại về bản chất thuộc nhóm object, bao gồm object literal, array, function, Date, Map và Set.

```js
const name = "Kim";       // string
const age = 30;           // number
const active = true;      // boolean
const missing = undefined;
const empty = null;
const huge = 9007199254740993n; // bigint
const idKey = Symbol("id");
```

Object:

```js
const user = {
  id: 1,
  name: "Kim"
};
```

Array:

```js
const users = ["Kim", "Lee"];
```

Function:

```js
function greet() {
  return "hello";
}
```

Điểm quan trọng là JavaScript dynamic typing: variable không bị gắn type cố định như Java variable. Bạn có thể viết:

```js
let value = 10;
value = "ten";
```

Code hợp lệ ở runtime JavaScript, dù TypeScript sau này có thể ngăn bạn nếu type đã được xác định.

---

# Chương 6 — `typeof`, `Array.isArray()` và các trường hợp đặc biệt

`typeof` trả một string mô tả category runtime của value.

```js
typeof "hello";    // "string"
typeof 10;         // "number"
typeof true;       // "boolean"
typeof undefined;  // "undefined"
typeof 10n;        // "bigint"
typeof Symbol();   // "symbol"
```

Function:

```js
typeof function () {};
// "function"
```

Array lại cho:

```js
typeof [];
// "object"
```

Vì vậy để check array, dùng:

```js
Array.isArray(value);
```

Một legacy quirk nổi tiếng:

```js
typeof null;
// "object"
```

Do đó check object thường phải loại null:

```js
if (
  typeof value === "object" &&
  value !== null
) {
  // object-like value
}
```

### Senior note

Các edge case như `typeof null` là lý do senior không viết validation bằng cảm giác. Khi validate external data, cần check đúng semantics thay vì chỉ một `typeof` đơn giản.

---

# Chương 7 — Primitive copy và object reference

Primitive thường được copy theo value:

```js
let a = 10;
let b = a;

b = 20;

console.log(a); // 10
```

Object variable giữ reference tới object. Khi gán object variable sang variable khác, hai variable có thể trỏ cùng object:

```js
const user1 = {
  name: "Kim"
};

const user2 = user1;

user2.name = "Lee";

console.log(user1.name);
// "Lee"
```

Đây là kiến thức nền tảng cực kỳ quan trọng cho frontend. Nhiều bug state xảy ra vì developer nghĩ mình “copy object” nhưng thực chất chỉ copy reference.

Spread tạo shallow copy:

```js
const user2 = {
  ...user1
};
```

Nhưng nếu object có nested object:

```js
const user1 = {
  profile: {
    name: "Kim"
  }
};

const user2 = {
  ...user1
};

user2.profile.name = "Lee";

console.log(user1.profile.name);
// "Lee"
```

`profile` vẫn cùng reference.

### Programming pattern — immutable update

Nếu muốn đổi nested property mà giữ object cũ:

```js
const nextUser = {
  ...user1,
  profile: {
    ...user1.profile,
    name: "Lee"
  }
};
```

React state update, reducers và nhiều state-management patterns dựa trên concept này.

---

# Chương 8 — Number, `NaN`, Infinity và floating-point

JavaScript dùng `number` cho cả integer và floating-point thông thường.

```js
const count = 10;
const price = 19.99;
```

Một điều bắt buộc phải biết là binary floating-point không thể biểu diễn chính xác mọi decimal fraction.

```js
0.1 + 0.2;
// 0.30000000000000004
```

Vì vậy:

```js
0.1 + 0.2 === 0.3;
// false
```

`NaN` nghĩa là “Not-a-Number”, nhưng chính nó có type `number`:

```js
typeof NaN;
// "number"
```

Đừng check:

```js
value === NaN;
```

vì `NaN` không equal chính nó. Dùng:

```js
Number.isNaN(value);
```

Kiểm tra số hữu hạn:

```js
Number.isFinite(value);
```

Parse:

```js
Number("123");        // 123
parseInt("123px", 10); // 123
parseFloat("3.14kg");  // 3.14
```

`Number("123px")` lại ra `NaN`, vì toàn bộ string không phải numeric literal hợp lệ.

### Senior note

Với tiền, lãi suất hoặc dữ liệu tài chính cần precision cao, đừng mặc định `number` là representation đúng. Có thể cần minor units hoặc decimal library/backend decimal handling.

---

# Chương 9 — String và template literal

> **Version note — ES2015/ES6:** Backtick template literals, `${expression}` interpolation và multiline template strings được chuẩn hóa trong ES2015. String là type rất cũ; feature mới ở đây là template-literal syntax.

String có thể viết bằng single quote, double quote hoặc backtick.

```js
const a = "hello";
const b = 'hello';
const c = `hello`;
```

Backtick cho template literal:

```js
const name = "Kim";
const message = `Hello ${name}`;
```

Nó cũng hỗ trợ multi-line string:

```js
const text = `line 1
line 2`;
```

Các method thường dùng gồm `trim`, `includes`, `startsWith`, `endsWith`, `slice`, `replace`, `split`, `toLowerCase`, `toUpperCase`.

```js
const email = "  USER@EXAMPLE.COM ";

const normalized = email
  .trim()
  .toLowerCase();
```

String immutable. Các method không sửa original string.

### Senior note

`string.length` đo UTF-16 code units, không luôn bằng số ký tự người dùng nhìn thấy. Khi xử lý emoji, grapheme hoặc multilingual text sâu, cần APIs/techniques khác. Beginner chỉ cần biết limitation tồn tại.

---

# Chương 10 — Boolean, truthy và falsy

Khi JavaScript cần quyết định điều kiện, value được convert sang boolean. Các falsy values quan trọng là `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. Hầu hết value khác là truthy, bao gồm object rỗng và array rỗng.

```js
if ([]) {
  console.log("array is truthy");
}
```

Một guard phổ biến:

```js
if (!user) {
  return;
}
```

Nhưng phải cẩn thận khi `0` hoặc empty string là value hợp lệ:

```js
if (!quantity) {
  // quantity = 0 cũng vào đây
}
```

Nếu chỉ muốn check nullish:

```js
if (
  quantity === null ||
  quantity === undefined
) {
}
```

### Senior note

Truthy/falsy là tiện, nhưng business logic cần explicit khi falsy values có nghĩa riêng.

---

# Chương 11 — Type conversion và coercion

Explicit conversion:

```js
String(123);
Number("123");
Boolean(value);
```

Implicit coercion xảy ra khi operator yêu cầu một loại value nhất định.

```js
"5" + 1;
// "51"
```

Với `+`, nếu một operand trở thành string, phép nối chuỗi có thể xảy ra.

```js
"5" - 1;
// 4
```

`-` lại buộc numeric conversion.

Người mới thường cố học thuộc các câu đố coercion. Cách học tốt hơn là: tại boundary, convert explicit và validate ngay.

Ví dụ query param:

```js
const rawPage = params.get("page");
const page = Number(rawPage);

if (
  !Number.isInteger(page) ||
  page < 1
) {
  throw new Error("Invalid page");
}
```

### Senior note

Senior code tránh phụ thuộc vào coercion khó đọc khi một conversion explicit làm intent rõ hơn.

---

# Chương 12 — Equality: `===`, `==`, `Object.is`

Strict equality `===` không thực hiện type coercion:

```js
5 === 5;   // true
5 === "5"; // false
```

Loose equality `==` có coercion:

```js
5 == "5";
// true
```

Trong application code hiện đại, `===` và `!==` là lựa chọn mặc định vì dễ reasoning hơn.

`Object.is` có edge case khác:

```js
Object.is(NaN, NaN);
// true

Object.is(0, -0);
// false
```

Bạn chưa cần dùng `Object.is` thường xuyên, nhưng cần biết nó tồn tại. Sau này React-style state comparison cũng liên quan identity/equality semantics.

---

# Chương 13 — Operators và cách dùng có chủ đích

> **Version note:** Exponentiation `**` thuộc ES2016. Optional chaining `?.` và nullish coalescing `??` thuộc ES2020. Logical assignment `&&=`, `||=` và `??=` thuộc ES2021. Đây là ví dụ rõ về cách JavaScript giữ nguyên operators cũ rồi bổ sung syntax diễn đạt intent an toàn hơn.

Arithmetic operators gồm `+`, `-`, `*`, `/`, `%`, `**`. Assignment có `=`, `+=`, `-=`, `*=`, `/=`. Comparison có `>`, `<`, `>=`, `<=`, `===`, `!==`.

Logical operators `&&`, `||`, `!` không chỉ trả boolean; chúng trả operand theo short-circuit semantics.

```js
const displayName = user.name || "Guest";
```

Nhưng `||` coi `""`, `0`, `false` là falsy. Khi chỉ muốn fallback cho `null` hoặc `undefined`, dùng `??`:

```js
const timeout = config.timeout ?? 5000;
```

Nếu `timeout = 0`, `??` giữ 0 còn `||` thay bằng 5000.

Optional chaining:

```js
const city = user.profile?.address?.city;
```

Method call:

```js
onComplete?.();
```

### Senior note

Optional chaining là convenience, không phải thuốc chữa data model sai. Nếu property bắt buộc mà bạn chain `?.` xuyên suốt, lỗi contract có thể bị biến thành silent `undefined`.

---

# Chương 14 — `if`, `else` và Guard Clause

Câu điều kiện cơ bản:

```js
if (age >= 18) {
  allowAccess();
} else {
  denyAccess();
}
```

Nested conditions làm code khó đọc:

```js
if (user) {
  if (user.active) {
    if (user.permission) {
      processUser(user);
    }
  }
}
```

Guard clauses rõ hơn:

```js
if (!user) {
  return;
}

if (!user.active) {
  return;
}

if (!user.permission) {
  return;
}

processUser(user);
```

### Programming pattern — Guard Clause

Đây là một programming pattern rất thực dụng. Nó làm invalid paths nằm ở đầu function, giữ happy path ít indentation.

---

# Chương 15 — `switch` và lựa chọn thay thế

`switch` phù hợp khi một value có một số trường hợp rời rạc.

```js
switch (status) {
  case "idle":
    showIdle();
    break;

  case "loading":
    showLoading();
    break;

  case "success":
    showSuccess();
    break;

  default:
    showUnknown();
}
```

Nếu quên `break`, execution có thể fall through sang case tiếp theo.

Khi mỗi case chỉ map sang function, lookup object có thể gọn:

```js
const handlers = {
  idle: showIdle,
  loading: showLoading,
  success: showSuccess
};

handlers[status]?.();
```

Đây bắt đầu chạm tới Strategy/Command-like pattern, nhưng không cần ép mọi switch thành object registry.

---

# Chương 16 — Loops: `for`, `while`, `for...of`, `for...in`

Classic `for` phù hợp khi cần index hoặc kiểm soát iteration chi tiết.

```js
for (
  let i = 0;
  i < users.length;
  i += 1
) {
  console.log(users[i]);
}
```

`for...of` đọc tự nhiên hơn khi chỉ cần values:

```js
for (const user of users) {
  console.log(user.name);
}
```

`for...in` iterate enumerable property keys:

```js
for (const key in user) {
  console.log(key);
}
```

Không nên dùng `for...in` cho array trong application code thông thường.

`while` phù hợp khi số vòng chưa biết trước:

```js
while (queue.length > 0) {
  const task = queue.shift();
  processTask(task);
}
```

`break` thoát loop, `continue` bỏ qua iteration hiện tại.

---

# Chương 17 — Function declaration, expression và arrow function

> **Version note — ES2015/ES6:** Arrow function xuất hiện trong ES2015. Nó không chỉ rút gọn `function`; lexical `this` là semantics riêng. Function declaration/expression truyền thống đã tồn tại từ các phiên bản JavaScript trước đó rất lâu.

Function declaration:

```js
function add(a, b) {
  return a + b;
}
```

Function expression:

```js
const add = function (a, b) {
  return a + b;
};
```

Arrow function:

```js
const add = (a, b) => a + b;
```

Ba style không hoàn toàn giống nhau. Arrow function không có own `this`, không có own `arguments`, không thể dùng làm constructor với `new`. Chi tiết này sẽ được giải thích ở Intermediate.

Ở Beginner, quy tắc đơn giản là arrow function rất hợp cho callback nhỏ:

```js
users.map((user) => user.name);
```

Normal method/function phù hợp khi muốn function name rõ, declaration semantics rõ hoặc cần `this` động.

---

# Chương 18 — Parameters, default parameters, rest parameters và options object

> **Version note — ES2015/ES6:** Default parameters và rest parameters `...args` được chuẩn hóa trong ES2015. Options Object là programming pattern do developer thiết kế, không phải feature ECMAScript có một version riêng.

Default parameter:

```js
function greet(name = "Guest") {
  return `Hello ${name}`;
}
```

Rest parameter gom nhiều arguments thành array:

```js
function sum(...numbers) {
  return numbers.reduce(
    (total, value) => total + value,
    0
  );
}
```

Một API có nhiều positional arguments dễ khó đọc:

```js
request("/api", true, 5000, false);
```

Options object rõ hơn:

```js
request({
  url: "/api",
  auth: true,
  timeoutMs: 5000,
  cache: false
});
```

### Programming pattern — Options Object

Pattern này đặc biệt hữu ích khi function có từ 3 tham số trở lên, có nhiều optional values hoặc có boolean flags.

---

# Chương 19 — Return value và early return

Một function return value bằng `return`:

```js
function calculateTotal(price, quantity) {
  return price * quantity;
}
```

Nếu không return explicit, result là `undefined`.

```js
function logMessage(message) {
  console.log(message);
}
```

Early return giữ code phẳng:

```js
function saveUser(user) {
  if (!user) {
    return;
  }

  if (!user.name) {
    return;
  }

  persistUser(user);
}
```

### Senior note

Nếu invalid input là programmer error hoặc business error quan trọng, có thể `throw` thay vì silent return. Guard clause không có nghĩa lúc nào cũng bỏ lỗi đi.

---

# Chương 20 — First-class functions, callbacks và higher-order thinking

JavaScript coi function như value. Bạn có thể lưu function vào variable, truyền function làm argument, return function từ function khác.

```js
function execute(callback) {
  callback();
}

execute(() => {
  console.log("run");
});
```

Function nhận hoặc trả function gọi là higher-order function.

```js
function createMultiplier(factor) {
  return (value) => value * factor;
}

const double = createMultiplier(2);

console.log(double(5));
// 10
```

Bạn vừa chạm tới closure, dù phần cơ chế sâu sẽ học ở Intermediate.

First-class functions làm nhiều design patterns trong JavaScript nhẹ hơn Java. Strategy không nhất thiết cần interface + class; chỉ cần function cùng contract.

```js
const discountStrategies = {
  normal: (price) => price,
  vip: (price) => price * 0.9
};
```

---

# Chương 21 — Scope và vì sao scope nhỏ tốt hơn

Global scope tồn tại rộng nhất. Function scope tồn tại trong function. Block scope tồn tại trong `{}` với `let`/`const`.

```js
const globalValue = 1;

function run() {
  const functionValue = 2;

  if (true) {
    const blockValue = 3;
  }
}
```

`blockValue` không tồn tại ngoài `if` block.

Scope nhỏ giúp giảm nơi value có thể bị đọc/mutate. Vì vậy đừng đặt mọi thứ lên `window` hay global object chỉ để “dễ gọi”.

### Senior note

Global mutable state là một trong những nguồn coupling khó kiểm soát nhất trong frontend legacy code. Module scope, closures và explicit dependency injection giúp thay thế nó.

---

# Chương 22 — Hoisting và Temporal Dead Zone

Function declaration có thể gọi trước textual declaration:

```js
greet();

function greet() {
  console.log("hello");
}
```

`var` binding được hoist và initialized bằng `undefined`:

```js
console.log(value);
// undefined

var value = 10;
```

`let` và `const` cũng có binding trước declaration nhưng ở Temporal Dead Zone, nên access trước declaration throw error:

```js
console.log(value);

const value = 10;
```

### Beginner rule

Đừng dựa vào hoisting trick. Tổ chức code để declaration dễ thấy và dùng `const`/`let` cho code mới.

---

# Chương 23 — Array: collection cơ bản nhất

> **Version note:** Array là phần nền tảng rất cũ, nhưng method của Array đến từ nhiều thế hệ. `forEach`, `map`, `filter`, `some`, `every`, `reduce` được chuẩn hóa từ ES5, nên chúng đã có độ tương thích rất cao.

Array tạo bằng:

```js
const users = [
  "Kim",
  "Lee"
];
```

Access theo index bắt đầu từ 0:

```js
users[0];
```

Length:

```js
users.length;
```

Add/remove cuối:

```js
users.push("Park");
users.pop();
```

Đầu array:

```js
users.unshift("Choi");
users.shift();
```

Các method đầu array thường phải dịch chuyển index nhiều phần tử và có thể kém hiệu quả hơn operations cuối array với collection lớn, nhưng đừng tối ưu nếu không có vấn đề thật.

---

# Chương 24 — `map`, `filter`, `find`, `some`, `every`, `includes`

> **Version note:** `map`, `filter`, `some`, `every` thuộc ES5; `find()` thuộc ES2015; `includes()` thuộc ES2016. Legacy code đôi khi dùng `indexOf(...) !== -1` vì được viết trước khi `includes()` trở thành lựa chọn chuẩn.

`map` transform mỗi element sang value mới:

```js
const names = users.map(
  (user) => user.name
);
```

`filter` giữ element thỏa condition:

```js
const activeUsers = users.filter(
  (user) => user.active
);
```

`find` lấy element đầu tiên phù hợp:

```js
const target = users.find(
  (user) => user.id === id
);
```

`some` hỏi “có ít nhất một cái đúng không?”:

```js
const hasAdmin = users.some(
  (user) => user.role === "admin"
);
```

`every` hỏi “tất cả đều đúng không?”. `includes` check value có tồn tại không.

### Language idiom

```js
const activeNames = users
  .filter((user) => user.active)
  .map((user) => user.name);
```

Chain ngắn, rõ rất tốt. Chain quá dài nên tách named helpers.

---

# Chương 25 — `forEach` và sự khác nhau với `map`

`forEach` dùng để chạy side effect cho từng element:

```js
users.forEach((user) => {
  console.log(user.name);
});
```

`map` tạo array mới:

```js
const names = users.map(
  (user) => user.name
);
```

Đừng dùng `map` chỉ để side effect:

```js
users.map((user) => {
  console.log(user);
});
```

nếu bạn không dùng result array. Khi đó `forEach` hoặc `for...of` rõ intent hơn.

Một trap quan trọng sẽ học sâu ở Intermediate: `forEach(async () => ...)` không chờ callback promises theo cách người mới thường tưởng.

---

# Chương 26 — `reduce`: mạnh nhưng không phải lúc nào cũng nên dùng

`reduce` gộp array thành một result.

```js
const total = prices.reduce(
  (sum, price) => sum + price,
  0
);
```

Group data:

```js
const byRole = users.reduce(
  (result, user) => {
    result[user.role] ??= [];
    result[user.role].push(user);
    return result;
  },
  {}
);
```

Nhưng nếu callback vừa filter, map, mutate, side effect và build object phức tạp, code khó đọc. Không có điểm cộng senior nào vì dùng `reduce` thay `for...of`.

---

# Chương 27 — Mutating và non-mutating array APIs

> **Version note — ES2023:** `toSorted()`, `toReversed()`, `toSpliced()` và `with()` được chuẩn hóa ở ES2023 để cung cấp copying versions thay cho các thao tác mutate tương ứng. Chúng rất hợp với immutable-state style nhưng vẫn cần check WebView cũ.

Mutating methods thay array hiện tại:

```text
push
pop
shift
unshift
splice
sort
reverse
```

Non-mutating methods phổ biến:

```text
map
filter
slice
concat
```

JavaScript hiện đại còn có các non-mutating alternatives như `toSorted`, `toReversed`, `toSpliced`, `with` trên runtimes hỗ trợ.

Ví dụ `sort()` mutate:

```js
const numbers = [3, 1, 2];

numbers.sort(
  (a, b) => a - b
);
```

Nếu cần giữ original:

```js
const sorted = [...numbers].sort(
  (a, b) => a - b
);
```

hoặc `toSorted()` khi target runtime hỗ trợ.

---

# Chương 28 — Object literal và property access

Object:

```js
const user = {
  id: 1,
  name: "Kim",
  active: true
};
```

Dot access:

```js
user.name;
```

Bracket access dùng dynamic key:

```js
const key = "name";
user[key];
```

Update:

```js
user.active = false;
```

Add property:

```js
user.role = "admin";
```

Delete:

```js
delete user.role;
```

Method shorthand:

```js
const user = {
  name: "Kim",

  greet() {
    return `Hello ${this.name}`;
  }
};
```

`this` của method sẽ được giải thích sâu ở Intermediate.

---

# Chương 29 — Object utilities

> **Version note:** Object APIs trải qua nhiều thế hệ: `Object.keys()` và descriptor APIs gắn với ES5; `Object.assign()` thuộc ES2015; `Object.values()`, `Object.entries()`, `Object.getOwnPropertyDescriptors()` thuộc ES2017; `Object.fromEntries()` thuộc ES2019; `Object.hasOwn()` thuộc ES2022; `Object.groupBy()` thuộc ES2024.

`Object.keys` lấy own enumerable string keys:

```js
Object.keys(user);
```

`Object.values` lấy values. `Object.entries` lấy `[key, value]` pairs.

```js
for (const [key, value] of Object.entries(user)) {
  console.log(key, value);
}
```

`Object.fromEntries` làm chiều ngược lại.

```js
const object = Object.fromEntries([
  ["a", 1],
  ["b", 2]
]);
```

Own property check:

```js
Object.hasOwn(user, "name");
```

`Object.assign(target, source)` copy properties và mutate target.

---

# Chương 30 — Destructuring

Object destructuring:

```js
const {
  id,
  name
} = user;
```

Rename:

```js
const {
  name: userName
} = user;
```

Default:

```js
const {
  role = "user"
} = user;
```

Array:

```js
const [first, second] = values;
```

Function parameter destructuring:

```js
function saveUser({ id, name }) {
}
```

### Senior note

Destructuring tốt khi làm dependency/data usage rõ. Nhưng destructure quá nhiều fields từ một object lớn có thể làm mất context, vì sau đó đọc variable `id`, `name`, `status` không còn thấy nó thuộc object nào.

---

# Chương 31 — Spread và rest

> **Version note:** Rest parameters và array spread được chuẩn hóa ở ES2015. Object rest/spread `{ ...obj }` đến sau ở ES2018. Vì vậy toolchain cũ từng có giai đoạn hỗ trợ array spread nhưng vẫn cần transform cho object spread.

Spread object:

```js
const nextUser = {
  ...user,
  active: true
};
```

Spread array:

```js
const allUsers = [
  ...oldUsers,
  ...newUsers
];
```

Function call:

```js
Math.max(...numbers);
```

Rest parameter:

```js
function log(level, ...messages) {
}
```

Rest object:

```js
const {
  password,
  ...publicUser
} = user;
```

Spread/rest nhìn giống nhau về syntax `...` nhưng context quyết định nghĩa: spread “mở ra”, rest “gom lại”.

---

# Chương 32 — Set và Map

> **Version note — ES2015 và ES2025:** Map/Set/WeakMap/WeakSet được chuẩn hóa ở ES2015. ES2025 bổ sung Set operations như `union()`, `intersection()`, `difference()`, `symmetricDifference()`, `isSubsetOf()` và `isSupersetOf()`. Codebase support runtime cũ thường vẫn tự viết các helper này.

`Set` giữ unique values.

```js
const ids = new Set();

ids.add(1);
ids.add(1);

console.log(ids.size);
// 1
```

Deduplicate array:

```js
const unique = [
  ...new Set(values)
];
```

`Map` là key-value collection:

```js
const userById = new Map();

userById.set("u1", {
  name: "Kim"
});

userById.get("u1");
```

Map key có thể là object, function hoặc primitive.

### Senior note

Dùng object khi bạn model một record có fixed properties. Dùng Map khi semantics thật sự là dynamic dictionary/key-value collection.

---

# Chương 33 — Date và timezone basics

Current date/time:

```js
const now = new Date();
```

Timestamp milliseconds:

```js
Date.now();
```

ISO:

```js
now.toISOString();
```

Tránh ambiguous date strings như:

```js
new Date("01/02/2026");
```

vì format có thể được hiểu khác. Prefer explicit ISO contract từ API:

```text
2026-09-12T10:30:00+09:00
```

### Senior note

Frontend/backend date-time bugs thường đến từ việc không phân biệt local time, UTC và timezone offset. Beginner chỉ cần giữ rule: wire format phải explicit.

---

# Chương 34 — Math và random

Common APIs:

```js
Math.round(3.5);
Math.floor(3.9);
Math.ceil(3.1);
Math.trunc(3.9);
Math.abs(-10);
Math.min(1, 2, 3);
Math.max(1, 2, 3);
Math.random();
```

`Math.random()` không dành cho security token. Với ID phổ thông hiện đại, `crypto.randomUUID()` thường phù hợp hơn nếu runtime hỗ trợ.

---

# Chương 35 — Error, `throw`, `try`, `catch`, `finally`

Throw:

```js
if (!email) {
  throw new Error("Email is required");
}
```

Catch:

```js
try {
  await saveUser();
} catch (error) {
  console.error(error);
}
```

Finally:

```js
setLoading(true);

try {
  await saveUser();
} catch (error) {
  showError(error);
} finally {
  setLoading(false);
}
```

`finally` chạy cả success và failure, phù hợp cleanup/loading state.

### Anti-pattern

```js
try {
  await saveUser();
} catch (error) {
  // ignore
}
```

Swallowing error chỉ phù hợp nếu failure thật sự không quan trọng và được chủ đích document/observe ở nơi khác.

---

# Chương 36 — Custom Error cơ bản

```js
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}
```

Use:

```js
throw new ValidationError(
  "Invalid email",
  "email"
);
```

Caller:

```js
if (error instanceof ValidationError) {
  showFieldError(
    error.field,
    error.message
  );
}
```

Custom error giúp phân biệt failure bằng structure/type thay vì parse text message.

---

# Chương 37 — JSON

> **Version note — ES5:** `JSON.parse()` và `JSON.stringify()` được chuẩn hóa trong ES5. JSON là data format riêng; JavaScript object literal chỉ trông giống JSON ở một số trường hợp chứ không phải cùng grammar.

Serialize object sang JSON string:

```js
const text = JSON.stringify(user);
```

Parse:

```js
const user = JSON.parse(text);
```

JSON không giữ mọi JavaScript type. Function bị bỏ, `undefined` không được represent như normal value trong object, BigInt không stringify trực tiếp, circular object throw.

Do đó JSON không phải “deep clone universal”. `structuredClone()` ở modern runtimes clone được nhiều type hơn và cycles, nhưng clone cũng có cost và semantics riêng.

---

# Chương 38 — DOM: chọn element

Browser DOM API cho phép JavaScript đọc và thay đổi document.

```js
const button = document.querySelector("#save");
```

Selector đầu tiên match hoặc `null`.

```js
const buttons = document.querySelectorAll(".action");
```

`getElementById`:

```js
const root = document.getElementById("app");
```

Luôn nhớ DOM có lifecycle. Nếu script chạy trước element tồn tại, selector có thể trả null.

---

# Chương 39 — DOM: tạo và cập nhật nội dung an toàn

Plain text:

```js
element.textContent = user.name;
```

HTML:

```js
element.innerHTML = "<strong>Hello</strong>";
```

Không đưa untrusted input trực tiếp vào `innerHTML`:

```js
// nguy hiểm nếu userInput chứa HTML/script payload
result.innerHTML = userInput;
```

Create element:

```js
const li = document.createElement("li");
li.textContent = user.name;
list.append(li);
```

### Security note

`textContent` là lựa chọn mặc định cho plain text. Khi thật sự cần render HTML từ external source, cần strategy sanitize/trusted rendering chứ không concatenate string tùy tiện.

---

# Chương 40 — `classList`, attributes và style

```js
element.classList.add("active");
element.classList.remove("hidden");
element.classList.toggle("open");
```

Attribute:

```js
element.setAttribute("aria-expanded", "true");
```

Inline style:

```js
element.style.display = "none";
```

Trong codebase lớn, state → CSS class thường dễ maintain hơn việc set hàng loạt style inline.

---

# Chương 41 — Events và event object

```js
button.addEventListener("click", (event) => {
  console.log(event);
});
```

`event.target` là element nơi event bắt đầu; `event.currentTarget` là element listener hiện tại gắn vào.

Prevent browser default behavior:

```js
event.preventDefault();
```

Stop propagation:

```js
event.stopPropagation();
```

Không dùng `stopPropagation()` như default habit vì event bubbling là cơ chế rất hữu ích cho delegation.

---

# Chương 42 — Event listener lifecycle và cleanup

```js
function handleClick() {
  save();
}

button.addEventListener(
  "click",
  handleClick
);
```

Remove:

```js
button.removeEventListener(
  "click",
  handleClick
);
```

Phải cùng function reference. Vì vậy nếu bạn viết anonymous callback trực tiếp, sau này cleanup khó hơn nếu không giữ reference.

### Programming pattern — lifecycle pair

```text
addEventListener ↔ removeEventListener
setInterval      ↔ clearInterval
subscribe        ↔ unsubscribe
open             ↔ close
```

Tư duy ownership này sẽ trở thành chủ đề lớn ở Senior.

---

# Chương 43 — Form và FormData

```js
const form = document.querySelector("form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const data = new FormData(form);
  const email = data.get("email");
});
```

HTML built-in validation:

```js
input.checkValidity();
form.reportValidity();
```

Client validation giúp UX, không thay backend validation.

---

# Chương 44 — Timers

Timeout:

```js
const timeoutId = setTimeout(() => {
  refresh();
}, 1000);
```

Cancel:

```js
clearTimeout(timeoutId);
```

Interval:

```js
const intervalId = setInterval(
  refresh,
  5000
);
```

Cancel:

```js
clearInterval(intervalId);
```

Timer delay không guarantee callback chạy đúng millisecond; main thread bận thì callback chạy muộn.

---

# Chương 45 — localStorage và sessionStorage

Store string:

```js
localStorage.setItem(
  "theme",
  "dark"
);
```

Read:

```js
const theme = localStorage.getItem("theme");
```

Store object:

```js
localStorage.setItem(
  "user",
  JSON.stringify(user)
);
```

Read:

```js
const raw = localStorage.getItem("user");
const user = raw ? JSON.parse(raw) : null;
```

### Security note

localStorage có thể bị JavaScript cùng origin đọc. Đừng mặc định đây là nơi an toàn cho mọi token/secret. Auth storage strategy phải được thiết kế cùng backend và security model.

---

# Chương 46 — Promise: mental model đầu tiên

> **Version note — ES2015/ES6:** Native Promise được chuẩn hóa ở ES2015. Trước đó ecosystem dùng callback và nhiều Promise/Deferred libraries, nên legacy enterprise code thường có abstractions async khác native Promise.

Promise đại diện một operation có kết quả trong tương lai. Trạng thái cơ bản là pending, fulfilled, rejected.

```js
fetch("/api/users")
  .then((response) => {
    return response.json();
  })
  .then((users) => {
    renderUsers(users);
  })
  .catch((error) => {
    showError(error);
  });
```

Promise chaining phụ thuộc return:

```js
loadUser()
  .then((user) => {
    return loadOrders(user.id);
  })
  .then((orders) => {
    renderOrders(orders);
  });
```

Nếu quên `return`, chain tiếp theo không chờ inner Promise.

---

# Chương 47 — `async` / `await`

> **Version note — ES2017:** `async function` và `await` được chuẩn hóa ở ES2017 và xây trên Promise, không thay Promise. Top-level `await` là feature riêng xuất hiện muộn hơn ở ES2022.

```js
async function loadUsers() {
  const response = await fetch("/api/users");

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    );
  }

  return response.json();
}
```

`async` function luôn trả Promise, kể cả bạn return primitive:

```js
async function getValue() {
  return 10;
}
```

caller vẫn nhận Promise.

`await` chỉ dùng trong async contexts phù hợp. Nó làm code asynchronous nhìn gần như sequential, nhưng operation không trở thành synchronous block toàn browser.

---

# Chương 48 — Sequential và concurrent async work

> **Version note:** `Promise.all()`/`race()` thuộc bộ Promise ES2015. `Promise.allSettled()` đến ở ES2020, `Promise.any()` và `AggregateError` ở ES2021, `Promise.withResolvers()` ở ES2024, còn `Promise.try()` ở ES2025.

Nếu step B phụ thuộc result A:

```js
const user = await loadUser();
const orders = await loadOrders(user.id);
```

Sequential là đúng.

Nếu independent:

```js
const profile = await loadProfile();
const settings = await loadSettings();
```

có thể chạy đồng thời:

```js
const [profile, settings] = await Promise.all([
  loadProfile(),
  loadSettings()
]);
```

Beginner cần hiểu distinction, nhưng đừng chạy hàng nghìn task bằng `Promise.all()` mà chưa hiểu concurrency control. Chủ đề đó thuộc Senior.

---

# Chương 49 — `fetch` và HTTP căn bản

```js
const response = await fetch("/api/users");
```

`fetch` không reject chỉ vì server trả 404 hoặc 500. Cần check:

```js
if (!response.ok) {
  throw new Error(
    `HTTP ${response.status}`
  );
}
```

Parse JSON:

```js
const users = await response.json();
```

POST JSON:

```js
await fetch("/api/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(user)
});
```

HTTP methods bạn nên hiểu ở mức ý nghĩa: GET đọc, POST tạo/action, PUT/PATCH update theo contract, DELETE xóa. Status 2xx thành công, 4xx thường request/auth/client side issues, 5xx server side issues.

---

# Chương 50 — URL và query parameters

String concatenation dễ sai encoding:

```js
const url = "/search?q=" + keyword;
```

Prefer structured API:

```js
const url = new URL(
  "/search",
  location.origin
);

url.searchParams.set(
  "q",
  keyword
);
```

Browser tự encode query parameter đúng hơn.

---

# Chương 51 — ES Modules

> **Version note — ES2015 trở đi:** Static `import`/`export` được chuẩn hóa ở ES2015. Dynamic `import()` và `import.meta` thuộc ES2020; import attributes và JSON-module support được chuẩn hóa ở ES2025. Module syntax là ECMAScript, còn cách browser/Node/bundler resolve và tải module là một lớp khác.

Module export:

```js
// math.js
export function add(a, b) {
  return a + b;
}
```

Import:

```js
import {
  add
} from "./math.js";
```

Default export:

```js
export default function createUser() {
}
```

Import:

```js
import createUser from "./createUser.js";
```

Named exports thường dễ rename/refactor/search trong codebase lớn. Module có own scope, nên variable không tự trở thành global.

---

# Chương 52 — Pure functions và side effects

Pure function cùng input cho cùng output và không sửa external state:

```js
function calculateTax(amount, rate) {
  return amount * rate;
}
```

Side effect function:

```js
function saveUser(user) {
  localStorage.setItem(
    "user",
    JSON.stringify(user)
  );
}
```

Side effect không xấu. UI application bắt buộc cần DOM, network, storage. Vấn đề là nếu business calculations bị trộn với side effects, testing và reasoning khó hơn.

### Programming pattern — Functional Core / Imperative Shell

```text
read input
↓
normalize
↓
calculate pure result
↓
network/storage
↓
render
```

Pattern này rất hữu ích khi sang React/WebSquare architecture.

---

# Chương 53 — Naming, readability và code style

Bad:

```js
const x = a.filter((b) => b.c);
```

Better:

```js
const activeUsers = users.filter(
  (user) => user.active
);
```

Function names nên thể hiện action/domain intent:

```text
calculateTotal
validateOrder
loadUser
mapUserDto
renderUsers
```

Đừng viết comment mô tả lại syntax. Hãy comment constraints, workaround hoặc business reason.

---

# Chương 54 — Magic values và constants

Bad:

```js
if (retryCount >= 3) {
}
```

nếu `3` là policy có ý nghĩa.

Better:

```js
const MAX_RETRY_COUNT = 3;

if (
  retryCount >=
  MAX_RETRY_COUNT
) {
}
```

String states có thể centralize:

```js
const STATUS = {
  IDLE: "idle",
  LOADING: "loading",
  SUCCESS: "success"
};
```

Sau này TypeScript có thể derive literal union từ object này.

---

# Chương 55 — Defensive programming

Validation có giá trị nhất ở boundaries.

```js
function calculateTotal(
  price,
  quantity
) {
  if (!Number.isFinite(price)) {
    throw new Error(
      "Invalid price"
    );
  }

  if (
    !Number.isInteger(quantity) ||
    quantity < 0
  ) {
    throw new Error(
      "Invalid quantity"
    );
  }

  return price * quantity;
}
```

Tuy nhiên không cần validate lặp lại ở mọi private helper nếu boundary đã guarantee invariant. Defensive programming tốt không phải thêm `if` vô hạn; nó là đặt validation đúng nơi.

---

# Chương 56 — Debugging cơ bản bằng DevTools

Browser DevTools có các tab quan trọng: Console để xem logs/errors, Network để xem HTTP requests, Elements để xem DOM/CSS, Sources để breakpoint và step code, Application để xem storage/cache, Performance và Memory để phân tích sâu hơn.

`debugger` statement:

```js
function calculate(value) {
  debugger;
  return value * 2;
}
```

Khi DevTools mở, code pause để bạn inspect local variables, call stack và scope.

Một thói quen tốt là **debug bằng evidence**, không sửa ngẫu nhiên. Đầu tiên reproduce, xác định layer, inspect inputs/outputs rồi mới đưa hypothesis.

---

# Chương 57 — Từ code chạy được đến code có cấu trúc

Một event handler kiểu beginner thường gom mọi thứ:

```js
async function handleClick() {
  const keyword = document
    .querySelector("#keyword")
    .value;

  const response = await fetch(
    "/api/users?q=" + keyword
  );

  const users = await response.json();

  document.querySelector("#result")
    .innerHTML = users
      .map((user) => `<li>${user.name}</li>`)
      .join("");
}
```

Nó trộn DOM read, URL building, network, parsing, rendering và security sink. Refactor từng responsibility:

```js
function readKeyword() {
  return document
    .querySelector("#keyword")
    .value
    .trim();
}
```

```js
async function searchUsers(keyword) {
  const url = new URL(
    "/api/users",
    location.origin
  );

  url.searchParams.set(
    "q",
    keyword
  );

  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`
    );
  }

  return response.json();
}
```

```js
function renderUsers(users) {
  const list = document.querySelector(
    "#result"
  );

  list.textContent = "";

  for (const user of users) {
    const item = document.createElement(
      "li"
    );

    item.textContent = user.name;
    list.append(item);
  }
}
```

Controller:

```js
async function handleSearch() {
  const keyword = readKeyword();

  if (!keyword) {
    renderUsers([]);
    return;
  }

  try {
    const users = await searchUsers(
      keyword
    );

    renderUsers(users);
  } catch (error) {
    console.error(error);
  }
}
```

Đây là bước đầu tiên của architecture thinking: mỗi function có trách nhiệm tương đối rõ.

---

# Chương 58 — Language Idioms ở level Beginner

Một JavaScript developer đã qua Beginner nên thấy các idioms sau là tự nhiên. Guard clause giúp invalid cases thoát sớm. `const` dùng mặc định để giảm reassignment. `map` dành cho transformation, `filter` dành cho selection, `find` dành cho lookup first match. `??` dùng khi fallback chỉ cho nullish values. `?.` dùng khi relationship thật sự optional. Spread dùng cho shallow immutable update. Options object dùng cho API có nhiều arguments. `try/catch/finally` quản lý success/failure/cleanup. ES Modules dùng để phân chia dependency thay vì global namespace.

Điểm quan trọng là bạn không học idiom như câu thần chú; bạn hiểu vì sao nó làm intent rõ hơn.

---

# Chương 59 — Programming Patterns ở level Beginner

Ở level này, bạn đã thực tế dùng nhiều pattern dù chưa gọi tên. **Guard Clause** giúp làm flow phẳng. **Options Object** giúp API dễ mở rộng. **Mapper** chuyển object từ shape này sang shape khác. **Factory Function** tạo object với construction rule. **Strategy bằng function** thay behavior dựa trên policy. **Functional Core / Imperative Shell** tách calculation khỏi side effects. **Lifecycle Pair** giúp nhớ resource đã acquire thì phải release. **Immutable Update** giảm mutation của shared state.

Hãy học pattern từ problem. Nếu một `if` đơn giản giải quyết đủ rõ, không cần Strategy. Nếu object construction chỉ là `{ name }`, không cần Factory layer. Seniority nằm ở lựa chọn đúng mức abstraction.

---

# Chương 60 — Design Pattern Connections

JavaScript first-class functions làm Strategy, Command, Observer và Decorator nhẹ hơn nhiều ngôn ngữ class-centric. Event listener là một dạng Observer-like relationship. Function registry là Strategy/Command-like dispatch. Module public API có thể đóng vai trò Facade. Factory function là Factory Pattern ở dạng nhẹ. Khi sang Intermediate, bạn sẽ thấy closure tạo private state, module pattern, reducer/state pattern và middleware/chain rõ hơn.

---

# Chương 61 — Anti-patterns cần bỏ từ sớm

Không đưa shared mutable state lên `window` chỉ để mọi nơi access. Không dùng `innerHTML` cho untrusted data. Không dùng `var` cho code mới. Không dùng `map` khi chỉ cần side effect. Không swallow error không lý do. Không dùng `==` nếu team không chủ đích semantics coercion. Không deep-nest `if` nếu guard clauses rõ hơn. Không viết giant event handler chứa DOM, network, business logic và rendering cùng lúc. Không dùng `JSON.parse(JSON.stringify(...))` như universal deep clone. Không assume `fetch` 500 sẽ tự throw. Không assume timer 0ms chạy ngay.

---

# Chương 62 — Mini Project 1: Todo List

Todo List nên có add, delete, toggle complete, filter, localStorage và render. Hãy giữ state dưới dạng array objects, viết pure functions cho add/toggle/remove, viết storage functions riêng và render function riêng. Event handlers chỉ đọc input và gọi use-case functions. Đây là project rất tốt để luyện array/object/reference/DOM/event/storage.

---

# Chương 63 — Mini Project 2: User Search

User Search nên có keyword input, loading state, API fetch, error state và result rendering. Beginner version chỉ cần gọi search khi submit/click. Intermediate version sau này thêm debounce, AbortController và stale-result handling. Project này luyện fetch, URL, Promise, async/await, try/catch và DOM rendering an toàn.

---

# Chương 64 — Mini Project 3: Shopping Cart

Cart item có thể có `id`, `name`, `price`, `quantity`. Hãy viết `addItem`, `removeItem`, `changeQuantity`, `calculateSubtotal`, `calculateTotal`. Các calculation functions nên pure. UI handler chỉ dispatch intent. Đây là bridge tốt sang state management và reducer ở Intermediate.

---

# Chương 65 — Exit Criteria trước khi sang Intermediate

Bạn nên tự giải thích được vì sao `const` object vẫn mutate được, vì sao object assignment copy reference, vì sao spread chỉ shallow, vì sao `0 || 100` khác `0 ?? 100`, vì sao `fetch` cần check `response.ok`, vì sao `map` khác `forEach`, vì sao `setTimeout(..., 0)` không chạy ngay, vì sao `innerHTML` có XSS risk, vì sao listener cần cleanup, và vì sao business logic không nên nằm hết trong DOM event handler.

Bạn cũng nên tự viết được một feature nhỏ có input, validation, pure logic, API/storage và render mà không cần copy nguyên mẫu từ tài liệu. Khi đã đạt mức này, bạn sẵn sàng sang Intermediate — nơi mục tiêu không còn là biết cú pháp mà là hiểu **runtime semantics** của JavaScript.
