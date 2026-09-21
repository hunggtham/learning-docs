# JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong

> **Mục tiêu của phần này**: chuyển từ mức “biết dùng JavaScript” sang mức “hiểu vì sao JavaScript hoạt động như vậy”. Bạn sẽ học execution context, lexical environment, closure, `this`, prototype, class internals, modules, Promise/event loop, iterator/generator, functional composition, state modeling, error architecture, API layer, testing và các programming/design patterns quan trọng.
>
> Phần này giả định bạn đã hoàn thành Beginner và có thể viết function, object, array, DOM, fetch và async/await cơ bản.

---

<!-- VERSION-GUIDE-BEGIN -->
# Version mindset ở level Intermediate: hiểu TC39 proposal process

Ở Beginner, version giúp bạn nhận ra syntax thuộc thế hệ nào. Sang Intermediate, bạn cần hiểu thêm **feature đi vào JavaScript bằng cách nào**. TC39 phát triển các đề xuất mới theo nhiều stage. Stage 1 nghĩa ý tưởng đã bước vào quy trình nhưng còn có thể đổi lớn. Stage 2 cho thấy problem/solution direction đã rõ hơn. Stage 3 là candidate khá chín và thường là lúc engine vendors triển khai để lấy feedback. Stage 4 là finished proposal: feature đã hoàn tất các yêu cầu chuẩn hóa và sẽ được đưa vào yearly snapshot tiếp theo phù hợp.

Điều này giải thích vì sao “browser đã support” và “yearly ECMAScript edition đã publish” không luôn cùng thời điểm. Một browser có thể ship Stage-3/Stage-4 feature trước yearly snapshot. Ngược lại, một feature đã Stage 4 vẫn có thể không chạy trên WebView cũ. Vì vậy quy trình production phải gồm hai câu hỏi tách biệt: **feature có final/stable chưa?** và **runtime target của tôi có support chưa?**.

`ESNext` cũng phải được hiểu là nhãn động. Nó không có nghĩa ES2027 hay một version cụ thể. Khi đọc một bài cũ nói “ESNext”, hãy tra tên proposal/feature hiện tại. Syntax proposal có thể đã đổi hoặc proposal có thể đã bị bỏ.

Ở Intermediate, bạn cũng sẽ gặp nhiều thứ phối hợp JavaScript với browser nhưng không thuộc ECMAScript yearly releases. `AbortController`, DOM event loop integration, rendering lifecycle và `requestAnimationFrame` là Web APIs/host behavior. Promise jobs, async functions, iterators, modules và class syntax mới là ECMA-262 concerns. Việc phân biệt hai nhóm này giúp bạn không gán nhầm “ES version” cho một platform API.

Tính đến lần cập nhật này, ECMAScript 2026 là yearly snapshot chính thức mới nhất. Những cơ chế nền như closure, `this`, prototype, descriptors và Promise resolution không trở nên lỗi thời chỉ vì yearly snapshot tăng; version notes chủ yếu quan trọng ở nơi syntax/API mới làm thay đổi compatibility hoặc style code.
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — Execution Context và Call Stack

Khi JavaScript gọi một function, engine không chỉ “nhảy vào đoạn code”. Nó tạo một **execution context**, có thể hiểu như môi trường chứa các binding local, parameters, thông tin scope, `this` binding và reference tới outer lexical environment.

```js
const globalValue = 10;

function add(a, b) {
  const result = a + b + globalValue;
  return result;
}

add(1, 2);
```

Khi file được chạy, có Global Execution Context. Khi `add(1, 2)` được gọi, một Function Execution Context mới được tạo với `a = 1`, `b = 2`, `result`, và outer environment trỏ về global lexical environment.

Execution contexts được quản lý bởi **call stack**. Ví dụ:

```js
function c() {
  console.log("c");
}

function b() {
  c();
}

function a() {
  b();
}

a();
```

Call stack conceptually:

```text
a
↓
b
↓
c
```

Khi `c` xong, context của `c` pop khỏi stack, execution quay lại `b`, rồi `a`.

Nếu recursion không dừng:

```js
function loop() {
  loop();
}

loop();
```

stack tăng liên tục tới `Maximum call stack size exceeded`.

## Execution context không đồng nghĩa lexical scope

Hai khái niệm này liên quan nhưng không nên trộn thành một. **Lexical scope** mô tả code ở vị trí nào có thể nhìn thấy binding nào và được quyết định chủ yếu bởi cấu trúc source. **Execution context** là trạng thái của một lần thực thi cụ thể. Một function chỉ có một lexical relationship trong source nhưng có thể được gọi hàng nghìn lần, và mỗi lần gọi tạo execution context riêng.

```js
function calculate(price, quantity) {
  const total = price * quantity;
  return total;
}

calculate(100, 2);
calculate(300, 4);
```

Hai lần gọi cùng dùng một function body và cùng lexical environment ngoài, nhưng `price`, `quantity`, `total` của hai lần gọi không phải cùng một execution state. Đây là lý do recursion hoạt động: cùng một function có thể xuất hiện nhiều lần trên call stack với parameters/local bindings khác nhau.

```js
function factorial(n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}
```

Với `factorial(3)`, stack có thể hình dung:

```text
factorial(3)
  ↓
factorial(2)
  ↓
factorial(1)
```

Mỗi frame giữ `n` riêng. Khi `factorial(1)` return, frame đó biến mất khỏi stack; kết quả được dùng để tiếp tục frame `factorial(2)`.

## Creation/initialization trước evaluation: nền tảng của hoisting

Một mental model rất quan trọng là engine phải chuẩn bị environment và bindings trước khi thực thi lần lượt các statements. Vì thế “hoisting” không nên được hiểu là engine thật sự cắt một dòng code rồi di chuyển nó lên đầu file. Đúng hơn, declaration được xử lý trong quá trình khởi tạo environment, nhưng **mỗi loại declaration được khởi tạo khác nhau**.

Function declaration có function value sẵn sớm:

```js
run();

function run() {
  console.log("run");
}
```

`var` có binding được initialized bằng `undefined` trước khi assignment chạy:

```js
console.log(value); // undefined
var value = 10;
```

`let`, `const` và `class` cũng có lexical binding, nhưng binding chưa được initialized để đọc cho đến khi evaluation đi tới declaration. Khoảng này là **Temporal Dead Zone (TDZ)**:

```js
console.log(value); // ReferenceError
const value = 10;
```

Vì vậy câu “`let` không hoist” là cách nói đơn giản nhưng không chính xác về mental model. Binding tồn tại trong lexical environment, nhưng chưa thể access trước initialization.

## Call stack chỉ chứa synchronous execution hiện tại

Khi một browser API như timer nhận callback, callback không nằm trên call stack trong suốt thời gian chờ.

```js
function run() {
  setTimeout(() => {
    console.log("later");
  }, 1000);
}

run();
```

Sau khi `setTimeout()` đăng ký timer và `run()` return, frame `run` đã rời stack. Khi timer đủ điều kiện và event loop chọn task tương ứng, **một lần gọi callback mới** mới được đẩy lên stack. Đây là điểm nối giữa call stack và event loop mà Chương 23 sẽ đào sâu.

### Cách trace execution thực tế

Khi code phức tạp, hãy trace theo ba câu hỏi thay vì đọc bằng cảm giác:

```text
1. Context/function nào đang chạy trên stack?
2. Identifier này được resolve qua lexical environment nào?
3. Công việc async này đang chạy ngay hay chỉ được schedule cho tương lai?
```

Ba câu hỏi này giải quyết phần lớn nhầm lẫn về closure, `this`, Promise và timer.

### Senior note

Stack trace trong error chính là dấu vết của call stack. Khi debug async code, stack có thể phức tạp hơn vì continuation được schedule qua Promise/event loop. Hiểu call stack là nền tảng cho mọi phần runtime sau này.

---

# Chương 2 — Lexical Environment và Scope Chain

JavaScript dùng **lexical scoping**. “Lexical” nghĩa là relationship giữa scopes chủ yếu được quyết định bởi vị trí code được viết, không phải nơi function được gọi.

```js
const value = "global";

function outer() {
  const value = "outer";

  function inner() {
    console.log(value);
  }

  return inner;
}

const fn = outer();

function run() {
  const value = "run";
  fn();
}

run();
```

Output là `outer`, không phải `run`. `inner` được định nghĩa trong scope của `outer`, nên khi tìm `value`, engine đi theo scope chain lexical: current scope → outer scope → global.

Scope chain có thể hình dung:

```text
inner scope
↓
outer scope
↓
global scope
```

Nếu cùng tên variable ở inner scope, nó **shadow** outer variable:

```js
const value = 1;

function run() {
  const value = 2;
  console.log(value); // 2
}
```

Shadowing không sai, nhưng quá nhiều biến cùng tên trong nested scopes làm cognitive load cao.

## Environment là nơi binding sống, không phải chỉ là một object thường

Khi học scope, nhiều người hình dung mỗi scope là một JavaScript object như `{ name: value }`. Mental model đó chỉ đúng rất sơ bộ. Specification dùng **Environment Records** để mô tả bindings. Điều này quan trọng vì binding có behavior riêng: TDZ, immutable `const`, function parameter bindings, module imports là live bindings, và global `var`/global lexical declarations không hoàn toàn giống nhau.

Bạn không thể làm:

```js
console.log(currentLexicalEnvironment);
```

vì lexical environment là khái niệm runtime/spec, không phải ordinary object được expose trực tiếp.

## Identifier resolution là một quá trình tìm từ trong ra ngoài

Với:

```js
const taxRate = 0.1;

function createCalculator(discount) {
  return function calculate(price) {
    const subtotal = price * (1 - discount);
    return subtotal * (1 + taxRate);
  };
}
```

Trong `calculate`, engine resolve:

```text
price
→ current function environment

discount
→ outer createCalculator environment

taxRate
→ outer global/module environment
```

Nếu identifier không tìm thấy trong toàn chain, đọc nó gây `ReferenceError`.

Đây khác với đọc property không tồn tại:

```js
const user = {};

console.log(user.name); // undefined
console.log(name);      // ReferenceError nếu không có binding name
```

Một bên là **property lookup trên object**, một bên là **identifier resolution qua lexical environments**. Phân biệt này rất quan trọng khi debug.

## Block scope và per-iteration binding

`let`/`const` có block scope:

```js
if (true) {
  const token = "abc";
}

// token không tồn tại ở đây
```

Trong `for (let ...)`, JavaScript còn tạo semantics phù hợp để mỗi iteration có binding riêng cho closure:

```js
const callbacks = [];

for (let i = 0; i < 3; i += 1) {
  callbacks.push(() => i);
}

console.log(callbacks[0]()); // 0
console.log(callbacks[1]()); // 1
console.log(callbacks[2]()); // 2
```

Legacy `var` dùng một function-scoped binding:

```js
const callbacks = [];

for (var i = 0; i < 3; i += 1) {
  callbacks.push(() => i);
}

console.log(callbacks[0]()); // 3
```

Trước ES2015, legacy code thường dùng IIFE để tạo binding riêng từng iteration:

```js
for (var i = 0; i < 3; i += 1) {
  (function (current) {
    callbacks.push(function () {
      return current;
    });
  })(i);
}
```

Đây là ví dụ điển hình cho **modern syntax xuất hiện để diễn đạt intent mà legacy JavaScript phải mô phỏng bằng pattern**.

## Global scope không đơn giản là `window`

Trong browser classic script, một số global declarations có relationship với global object, nhưng lexical declarations như `let`/`const` không đơn giản trở thành properties của `window`.

```js
var legacyGlobal = 1;
let lexicalGlobal = 2;
```

Tùy context classic script/module, semantics khác nhau; đặc biệt ES modules có module scope riêng. Vì vậy code hiện đại không nên dựa vào việc “khai báo top-level rồi chắc chắn có `window.xxx`”. Nếu cần global integration, expose explicit API.

### Programming pattern — lexical encapsulation

Helper chỉ dùng bên trong một use case có thể được giữ trong scope đó thay vì export/global:

```js
function buildReport(rows) {
  function formatRow(row) {
    return `${row.id}: ${row.name}`;
  }

  return rows.map(formatRow);
}
```

### Senior note

Lexical scope làm source structure trở thành một phần của dependency structure. `this` là một điểm khác biệt lớn: normal function `this` thường phụ thuộc call-site chứ không đi theo lexical scope; arrow function thì lexical `this`.

---

# Chương 3 — Closure: function nhớ environment nơi nó được tạo

Closure là một trong những concept cốt lõi nhất của JavaScript. Một function có thể tiếp tục access variables trong lexical environment nơi nó được tạo, kể cả khi outer function đã return.

```js
function createCounter() {
  let count = 0;

  return function () {
    count += 1;
    return count;
  };
}

const counter = createCounter();

counter(); // 1
counter(); // 2
counter(); // 3
```

`createCounter()` đã kết thúc, nhưng returned function vẫn giữ access tới binding `count`. Đây là closure.

Closure không đơn giản là “function nằm trong function”. Điểm cốt lõi là function giữ lexical access tới variables mà nó cần.

Closure cho phép private state:

```js
function createUserStore() {
  let user = null;

  return {
    getUser() {
      return user;
    },

    setUser(nextUser) {
      user = nextUser;
    }
  };
}
```

`user` không exposed trực tiếp ra ngoài.

## Closure giữ binding, không phải snapshot value

Đây là một distinction rất quan trọng. Closure thường không “copy value tại thời điểm function được tạo”; nó giữ khả năng truy cập **binding**.

```js
let status = "idle";

function readStatus() {
  return status;
}

status = "loading";

console.log(readStatus()); // "loading"
```

Nếu closure chỉ snapshot `"idle"`, output đã là `"idle"`. Nhưng nó đọc binding hiện tại.

Điều này giải thích cả sức mạnh lẫn bug của closure. Một callback có thể thấy state mới nếu binding bị mutate; nhưng một hệ thống render tạo **binding mới cho mỗi render/call** có thể khiến callback giữ binding cũ, tạo stale closure.

## Mỗi factory call có một private environment khác nhau

```js
function createCounter() {
  let count = 0;

  return () => ++count;
}

const a = createCounter();
const b = createCounter();

console.log(a()); // 1
console.log(a()); // 2
console.log(b()); // 1
```

`a` và `b` không share `count`, vì chúng được tạo từ hai lần gọi khác nhau, mỗi lần có environment riêng. Đây là nền tảng của factory/module patterns dựa closure.

## Closure và lifecycle/memory

Nếu closure reachable, những bindings/object mà closure thật sự cần cũng có thể tiếp tục reachable.

```js
function createHandler(bigData) {
  return function () {
    return bigData.id;
  };
}
```

Nếu handler được gắn vào một global listener và không bao giờ remove, `bigData` có thể sống lâu hơn business lifecycle dự kiến.

Nhưng câu “closure gây memory leak” là sai. Closure chỉ giữ data khi còn đường reachability. Vấn đề thực tế thường là **resource owner không cleanup callback/subscription**.

Ví dụ:

```js
function mount(bigData) {
  const handler = () => {
    console.log(bigData.id);
  };

  window.addEventListener("resize", handler);

  return () => {
    window.removeEventListener("resize", handler);
  };
}
```

Ở đây closure có lifetime explicit qua cleanup function.

## Stale closure: timing + lifecycle, không phải closure “hỏng”

Hãy xem một factory tạo callback:

```js
function createLogger(message) {
  return () => {
    console.log(message);
  };
}

const logOld = createLogger("old");
const logNew = createLogger("new");
```

`logOld` đúng khi in `"old"`; nó giữ environment của lần gọi cũ. Framework render systems có thể tạo tình huống tương tự: callback cũ sống sau khi UI đã có state mới. Cách giải quyết không phải “tránh closure”, mà là thiết kế dependency/lifecycle đúng.

### Closure và memory

Nếu closure giữ reference tới object lớn, object đó tiếp tục reachable:

```js
function createHandler(bigData) {
  return function () {
    return bigData.id;
  };
}
```

Closure không “gây leak” tự động. Vấn đề xảy ra khi lifecycle của closure dài hơn lifecycle mà bạn tưởng, làm data/resource tiếp tục sống.

### Closure và loop

Với `let`, mỗi iteration có binding phù hợp:

```js
const handlers = [];

for (let i = 0; i < 3; i += 1) {
  handlers.push(() => i);
}

handlers[0](); // 0
handlers[1](); // 1
handlers[2](); // 2
```

Legacy `var` có thể khiến tất cả callbacks nhìn cùng binding và cuối cùng cùng trả 3.

### Design pattern connections

Closure là nền tảng cho Module Pattern, Factory với private state, memoization, decorators, currying, hooks và middleware wrappers.

### Senior note

Stale closure là lỗi rất phổ biến trong React-like systems: closure giữ value của một render/lifecycle trước đó. Type system không tự cứu bạn khỏi timing semantics này.

---

# Chương 4 — Function là first-class value và Higher-Order Function

Function có thể được truyền, return, lưu trong object/array. Điều này làm JavaScript cực kỳ linh hoạt.

```js
function withLogging(fn) {
  return (...args) => {
    console.log("args", args);
    const result = fn(...args);
    console.log("result", result);
    return result;
  };
}
```

```js
const add = (a, b) => a + b;
const loggedAdd = withLogging(add);
loggedAdd(1, 2);
```

`withLogging` là Higher-Order Function vì nó nhận function và trả function.

### Programming pattern — decorator-like wrapper

```js
function withTiming(fn) {
  return (...args) => {
    const start = performance.now();

    try {
      return fn(...args);
    } finally {
      console.log(
        performance.now() - start
      );
    }
  };
}
```

Pattern này xuất hiện trong logging, retry, auth wrapper, metrics và middleware.

### Senior note

JavaScript không cần class cho mọi design pattern. Strategy, Command, Decorator, Observer và Middleware rất tự nhiên với first-class functions. Nhưng wrapper nesting quá sâu có thể làm stack trace khó đọc; đặt tên abstraction rõ và đừng wrap chỉ để “đúng pattern”.

---

# Chương 5 — `this`: hiểu theo call-site, không theo nơi function được viết

`this` là một trong những chủ đề gây nhiều bug nhất. Với normal function, `this` chủ yếu được xác định bởi **cách function được gọi**.

Method call:

```js
const user = {
  name: "Kim",

  greet() {
    return this.name;
  }
};

user.greet();
```

Call-site là `user.greet()`, nên `this` là `user`.

Detached method:

```js
const greet = user.greet;

greet();
```

Function không còn được gọi qua `user`, nên `this` không còn tự là `user`.

Trong strict mode, plain function call thường có `this === undefined`.

Constructor call:

```js
function User(name) {
  this.name = name;
}

const user = new User("Kim");
```

`new` tạo object mới và bind `this` vào object đó trong quá trình constructor chạy.

## Bốn binding rules thực dụng cho normal function

Khi nhìn một normal function, hãy xác định `this` bằng call expression chứ không nhìn nơi function được khai báo. Một mental model thực dụng là:

```text
1. new binding
   new Fn()

2. explicit binding
   fn.call(obj)
   fn.apply(obj)
   fn.bind(obj)

3. implicit binding
   obj.fn()

4. default binding
   fn()
```

Arrow function là exception lớn vì không tạo own dynamic `this`; nó dùng lexical `this` của surrounding context.

### Implicit receiver là expression ngay trước dấu `.`/`[]`

```js
const account = {
  owner: {
    name: "Kim",

    show() {
      return this.name;
    }
  }
};

account.owner.show();
```

`this` là `account.owner`, không phải `account`.

Tương tự:

```js
account["owner"].show();
```

receiver vẫn là owner object.

### Detached method làm mất receiver

```js
const show = account.owner.show;
show();
```

Điều bị mất không phải “method thuộc class”, mà là **reference/call form chứa receiver**. Vì vậy callback API rất hay làm lộ bug này:

```js
button.addEventListener("click", account.owner.show);
```

Browser gọi callback theo event-listener semantics, không phải bằng `account.owner.show()`. Nếu method thật sự cần instance receiver, hãy wrap hoặc bind có chủ đích và giữ reference cleanup.

```js
const handleClick = account.owner.show.bind(account.owner);
button.addEventListener("click", handleClick);
```

### `this` và lexical variables là hai cơ chế khác nhau

```js
const name = "outer";

const user = {
  name: "object",

  show() {
    console.log(name);
    console.log(this.name);
  }
};
```

`name` được resolve qua lexical scope. `this.name` bắt đầu từ runtime receiver rồi property lookup. Nếu trộn hai mental models, `this` sẽ luôn cảm giác “bí ẩn”.

### Class không thay đổi quy tắc cốt lõi của detached method

```js
class User {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return this.name;
  }
}

const user = new User("Kim");
const greet = user.greet;
```

`greet()` vẫn mất receiver. Class syntax không tự auto-bind methods như một số framework/language khác.

### Senior rule

Đừng hỏi “function này thuộc object nào?”. Hãy nhìn call expression. `obj.method()` khác `const fn = obj.method; fn()`.

---

# Chương 6 — `call`, `apply`, `bind`

`call` gọi function ngay với explicit `this`:

```js
function greet(message) {
  return `${message}, ${this.name}`;
}

const user = {
  name: "Kim"
};

greet.call(
  user,
  "Hello"
);
```

`apply` tương tự nhưng arguments được truyền dạng array-like:

```js
greet.apply(
  user,
  ["Hello"]
);
```

`bind` tạo function mới, chưa chạy ngay:

```js
const boundGreet = greet.bind(user);

boundGreet("Hello");
```

Một detail quan trọng: `bind()` tạo function identity mới. Vì vậy:

```js
element.addEventListener(
  "click",
  handler.bind(obj)
);
```

sau này bạn không thể remove listener bằng một `handler.bind(obj)` khác, vì đó là function mới. Hãy giữ reference:

```js
const boundHandler = handler.bind(obj);

element.addEventListener(
  "click",
  boundHandler
);
```

### Partial application

```js
function multiply(a, b) {
  return a * b;
}

const double = multiply.bind(
  null,
  2
);

double(5); // 10
```

---

# Chương 7 — Arrow function semantics

Arrow function không chỉ là function syntax ngắn. Nó **không có own `this`**; nó lấy `this` lexical từ surrounding context.

```js
const user = {
  name: "Kim",

  delayedGreeting() {
    setTimeout(() => {
      console.log(this.name);
    }, 100);
  }
};
```

Arrow callback dùng `this` của `delayedGreeting` method call.

Nếu dùng arrow làm object method khi cần dynamic `this`:

```js
const user = {
  name: "Kim",

  greet: () => {
    console.log(this.name);
  }
};
```

`this` không phải `user`.

Arrow cũng không có own `arguments` và không dùng với `new`.

### Language idiom

Arrow rất tốt cho callback transformations:

```js
users.map(
  (user) => user.name
);
```

Method shorthand tốt khi cần instance/object `this`:

```js
const user = {
  greet() {
    return this.name;
  }
};
```

---

# Chương 8 — Object property lookup và own/inherited property

Khi bạn đọc:

```js
user.name
```

engine tìm own property `name`. Nếu không có, nó có thể đi lên prototype chain.

Own property check:

```js
Object.hasOwn(
  user,
  "name"
);
```

`in` kiểm tra cả own và inherited:

```js
"toString" in user;
```

thường true vì `toString` nằm trên `Object.prototype`.

Đây là lý do `for...in` có thể thấy inherited enumerable properties, và tại sao arbitrary object dictionaries có security concerns như prototype pollution.

---

# Chương 9 — Prototype và prototype chain

JavaScript là prototype-based language. Mỗi ordinary object có internal prototype link tới object khác hoặc `null`.

```js
const user = {
  name: "Kim"
};

Object.getPrototypeOf(user);
```

thường là `Object.prototype`.

Array:

```js
const items = [];

Object.getPrototypeOf(items)
  === Array.prototype;
```

Các methods như `map`, `filter`, `push` được tìm thông qua prototype chain.

Constructor function:

```js
function User(name) {
  this.name = name;
}

User.prototype.greet = function () {
  return `Hello ${this.name}`;
};

const user = new User("Kim");
```

Chain:

```text
user
↓
User.prototype
↓
Object.prototype
↓
null
```

## Property lookup là chain traversal, không phải copy method vào từng instance

Với:

```js
const user = new User("Kim");
user.greet();
```

`user` thường không có own property `greet`. Engine tìm:

```text
user
↓ no own greet
User.prototype
↓ found greet
```

Sau đó function được gọi với receiver `user`, nên bên trong method `this` vẫn là `user`, **không phải `User.prototype`**. Đây là chỗ `this` và prototype chain giao nhau: prototype quyết định **tìm function ở đâu**; call-site quyết định **receiver là ai**.

## Shadowing inherited property

```js
const proto = {
  role: "user"
};

const account = Object.create(proto);

console.log(account.role); // "user"

account.role = "admin";

console.log(account.role); // "admin"
console.log(proto.role);   // "user"
```

Assignment thường tạo own property trên receiver thay vì sửa inherited data property ở prototype. Khi debug “tại sao object A đổi mà prototype không đổi”, hãy kiểm tra:

```js
Object.hasOwn(account, "role");
Object.getPrototypeOf(account);
```

Accessor descriptors có thể làm assignment semantics phức tạp hơn, vì inherited setter có thể được gọi. Chương Property Descriptors giải thích cơ chế đó.

## `instanceof` kiểm tra prototype relationship

```js
user instanceof User;
```

Ở mental-model level, `instanceof` kiểm tra liệu object được tham chiếu bởi `User.prototype` có xuất hiện trên prototype chain của `user` hay không. Nó không kiểm tra “shape object có giống User không”.

Vì thế prototype mutation có thể thay đổi result, và cross-realm objects có thể làm `instanceof Array`/`instanceof Error` không hoạt động như bạn kỳ vọng. Với arrays, `Array.isArray()` thường robust hơn cross-realm.

## Prototype mutation là global-ish behavior change cho descendants

```js
User.prototype.greet = function () {
  return "changed";
};
```

Các instances đang dùng prototype đó có thể thấy method mới ngay vì lookup xảy ra qua chain. Đây là sức mạnh của prototype model nhưng cũng là lý do patch built-in prototypes trong application code nguy hiểm:

```js
Array.prototype.last = function () {
  return this[this.length - 1];
};
```

Bạn đã thay behavior của mọi array trong realm và có nguy cơ conflict với library/standard tương lai.

## Class syntax không xóa prototype model

```js
class User {
  greet() {
    return this.name;
  }
}
```

Method `greet` vẫn nằm trên `User.prototype`. `class` chủ yếu cung cấp syntax/semantics rõ hơn cho constructor, inheritance, methods, private fields..., nhưng lookup model vẫn là prototype-based.

### Senior note

Prototype knowledge giúp debug method lookup, `instanceof`, inheritance và security. Không mutate built-in prototype trong application code như `Array.prototype.myMethod = ...` vì có thể gây conflict và hidden global effects.

---

# Chương 10 — `new` và constructor function

`new User("Kim")` conceptually làm bốn việc: tạo object mới, link prototype của object tới `User.prototype`, gọi `User` với `this` là object mới, rồi return object đó trừ một số edge cases khi constructor return object explicit.

Đây là lý do methods nên nằm trên prototype thay vì tạo lại mỗi instance trong legacy constructor style.

```js
function User(name) {
  this.name = name;
}

User.prototype.greet = function () {
  return this.name;
};
```

Modern code thường dùng class syntax cho readability, nhưng class vẫn dựa trên prototype machinery bên dưới.

---

# Chương 11 — `class`, instance fields, static và private fields

> **Version note:** Class declarations/expressions và `extends` được chuẩn hóa ở ES2015. Public/private instance fields, private methods/accessors, static fields và static blocks được chuẩn hóa ở ES2022. Vì vậy một runtime “support class” chưa chắc support toàn bộ modern class syntax.

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

Method vẫn nằm trên `User.prototype`:

```js
user.greet === User.prototype.greet;
```

Instance field:

```js
class User {
  active = true;
}
```

Static method thuộc class, không thuộc instance:

```js
class User {
  static createGuest() {
    return new User("Guest");
  }
}
```

Private field runtime-level:

```js
class Counter {
  #count = 0;

  increment() {
    this.#count += 1;
  }

  value() {
    return this.#count;
  }
}
```

### Senior note

Đừng dùng class chỉ vì quen Java. Class phù hợp khi abstraction có identity, state, lifecycle hoặc polymorphic behavior rõ. Stateless utility thường đơn giản hơn bằng function/module.

---

# Chương 12 — Inheritance và composition over inheritance

```js
class Employee extends User {
  constructor(name, department) {
    super(name);
    this.department = department;
  }
}
```

Override:

```js
class Admin extends User {
  greet() {
    return `Admin ${this.name}`;
  }
}
```

Inheritance hữu ích khi subtype relationship thật sự là “is-a”. Nhưng deep inheritance hierarchy làm behavior bị phân tán qua nhiều parent classes.

Composition thường rõ hơn:

```js
function calculatePrice(
  price,
  discountStrategy
) {
  return discountStrategy(price);
}
```

Thay vì tạo `VipUser extends DiscountUser extends UserBase...` chỉ để thay discount behavior.

### Design pattern connection

Composition đi tự nhiên với Strategy, Adapter, Decorator và Dependency Injection.

---

# Chương 13 — Property descriptors

> **Version note — ES5 nền tảng:** `Object.defineProperty()` và descriptor model là một phần quan trọng của ES5. ES2017 bổ sung `Object.getOwnPropertyDescriptors()`. Cơ chế này rất cũ nhưng vẫn nằm dưới nhiều framework/library abstractions hiện đại.

Property không chỉ có key/value. Data property còn có metadata: `writable`, `enumerable`, `configurable`.

```js
const user = {};

Object.defineProperty(
  user,
  "id",
  {
    value: 1,
    writable: false,
    enumerable: true,
    configurable: false
  }
);
```

Inspect:

```js
Object.getOwnPropertyDescriptor(
  user,
  "id"
);
```

Descriptors quan trọng khi đọc framework/library internals và hiểu freeze/seal. Application code thường không cần dùng `defineProperty` thường xuyên.

---

# Chương 14 — Getter và Setter

Getter:

```js
const user = {
  firstName: "Kim",
  lastName: "Min",

  get fullName() {
    return `${this.firstName} ${this.lastName}`;
  }
};
```

Caller đọc như property:

```js
user.fullName;
```

Setter:

```js
const account = {
  _name: "",

  set name(value) {
    this._name = value.trim();
  }
};
```

### Senior note

Getter syntax nhìn như property read, nên getter expensive, network call hoặc side effect nặng là surprising API design. Nếu operation có cost/side effect đáng kể, method rõ hơn.

---

# Chương 15 — `Object.create`, `Object.assign`, freeze/seal

> **Version note:** `Object.create()`, `freeze()`, `seal()` và descriptor-oriented controls thuộc thế hệ ES5. `Object.assign()` thuộc ES2015. Object spread `{...obj}` được chuẩn hóa sau ở ES2018 và không nên được coi là hoàn toàn đồng nghĩa với `Object.assign()` trong mọi edge case.

Prototype trực tiếp:

```js
const proto = {
  greet() {
    return "hello";
  }
};

const obj = Object.create(proto);
```

Null-prototype dictionary:

```js
const dict = Object.create(null);
```

Object không có `Object.prototype`, useful cho một số dictionary/security cases, nhưng `Map` thường ergonomic hơn.

`Object.assign(target, source)` mutate target. Spread thường rõ hơn cho shallow copy.

`Object.preventExtensions` ngăn add property mới. `Object.seal` thêm non-configurable. `Object.freeze` thêm non-writable data properties. Nhưng freeze là shallow.

```js
const config = Object.freeze({
  nested: {
    enabled: true
  }
});

config.nested.enabled = false;
// nested object vẫn có thể mutate
```

---

# Chương 16 — Symbol và protocol hooks

> **Version note — ES2015/ES6:** `Symbol` và well-known symbols như `Symbol.iterator` được đưa vào ES2015. Chúng mở đường cho standardized language protocols thay vì chỉ dựa vào naming convention.

`Symbol()` tạo unique primitive.

```js
const id = Symbol("id");

const user = {
  [id]: 123
};
```

Hai symbols có cùng description vẫn khác nhau:

```js
Symbol("id") === Symbol("id");
// false
```

Well-known symbols như `Symbol.iterator` là hooks vào language protocols. Bạn sẽ dùng nó khi học iterable.

`Symbol.toPrimitive` cho phép object customize conversion.

### Senior note

Symbol không phải privacy mechanism. Symbol properties vẫn inspect được bằng `Object.getOwnPropertySymbols`.

---

# Chương 17 — Map/Set ở mức Intermediate

> **Version note:** Map/Set xuất hiện ở ES2015. ES2025 bổ sung các Set operations chuẩn như `union`, `intersection`, `difference`, `symmetricDifference`, `isSubsetOf`, `isSupersetOf`, `isDisjointFrom`. Hãy kiểm tra target runtime trước khi refactor legacy helper sang API mới.

Map đặc biệt hữu ích để tạo index cho repeated lookup.

```js
const userById = new Map(
  users.map(
    (user) => [
      user.id,
      user
    ]
  )
);
```

Sau đó:

```js
userById.get(id);
```

Nếu trước đó bạn gọi `.find()` hàng nghìn lần trên array lớn, index Map có thể giảm complexity từ repeated linear search xuống gần constant-time lookup average, đổi lại dùng thêm memory và cần giữ index đồng bộ.

Set useful cho membership và uniqueness.

```js
const permissions = new Set([
  "READ",
  "WRITE"
]);

permissions.has("READ");
```

### Senior note

Chọn data structure theo access pattern. Đừng dùng Map vì “senior hơn object”.

---

# Chương 18 — WeakMap và WeakSet

> **Version note — ES2015:** WeakMap/WeakSet thuộc ES2015. `WeakRef` và `FinalizationRegistry` là nhóm khác, đến ở ES2021 và có semantics GC tinh tế hơn nên được để ở level Senior.

WeakMap keys là object/non-registered symbol trong modern semantics và không giữ object key sống chỉ vì entry tồn tại.

```js
const metadata = new WeakMap();

const user = {};

metadata.set(
  user,
  {
    dirty: true
  }
);
```

WeakMap không iterable vì GC timing không deterministic.

Use cases: metadata tied to object lifetime, object-keyed memoization, private state legacy patterns.

### Senior note

Weak không có nghĩa “GC sẽ xóa ngay”. Đừng dùng WeakMap nếu bạn cần enumeration hoặc deterministic cleanup.

---

# Chương 19 — ES Modules sâu hơn

> **Version note:** Static modules thuộc ES2015; dynamic `import()` và `import.meta` thuộc ES2020; import attributes/JSON modules thuộc ES2025. Module records của ECMAScript và cách browser/Node/bundler resolve module là hai lớp khác nhau.

Named exports:

```js
export function loadUser() {
}

export const MAX_RETRY = 3;
```

Import:

```js
import {
  loadUser,
  MAX_RETRY
} from "./user.js";
```

Module scope riêng, strict mode semantics và static dependency graph giúp bundler/tooling phân tích tốt.

Imports là **live bindings**. Nếu module export variable và thay đổi variable, importer đọc binding cập nhật.

Circular dependencies được language hỗ trợ nhưng initialization order có thể gây bugs. Nếu A import B và B import A, hãy xem đó là architecture smell trước khi tìm workaround.

### Programming pattern — Public Module API

Feature có thể expose qua `index.js` một API nhỏ, còn internal files không nên bị consumers deep-import tùy tiện.

---

# Chương 20 — Dynamic import và lazy loading concept

> **Version note — ES2020:** Dynamic `import()` là feature ES2020. Code splitting là behavior mà bundler có thể xây trên syntax này, không phải một guarantee của ECMAScript standard.

```js
const module = await import(
  "./heavyFeature.js"
);
```

Dynamic import trả Promise và cho phép load code theo nhu cầu. Bundlers có thể dùng nó làm code-splitting boundary.

Use case: editor lớn, chart library, route ít dùng, modal feature nặng.

Trade-off: initial bundle nhỏ hơn nhưng first-use latency có thể tăng. Senior cần đo UX thay vì lazy load mọi thứ.

---

# Chương 21 — Promise semantics sâu hơn

> **Version note:** Native Promise thuộc ES2015; `Promise.prototype.finally()` thuộc ES2018. Core resolution/chaining semantics trong chương này quan trọng và bền vững hơn việc nhớ năm của từng helper.

Promise có ba states: pending, fulfilled, rejected. Khi settle, state không thay đổi lại.

```js
Promise.resolve(10)
  .then((value) => value * 2)
  .then(console.log);
```

`.then()` luôn trả Promise mới. Nếu callback return plain value, Promise mới fulfill với value đó. Nếu return Promise, chain adopts Promise đó. Nếu throw, Promise mới reject.

```js
loadUser()
  .then((user) => {
    return loadOrders(user.id);
  })
  .then(renderOrders)
  .catch(handleError);
```

Missing return:

```js
loadUser()
  .then((user) => {
    loadOrders(user.id);
  })
  .then(() => {
    // không chờ loadOrders
  });
```

Đây là một async bug rất phổ biến.

## Settled không đồng nghĩa fulfilled

“Settled” nghĩa Promise không còn pending; nó có thể **fulfilled** hoặc **rejected**.

```text
pending
  ├─→ fulfilled(value)
  └─→ rejected(reason)
```

Một khi settled, Promise không chuyển state lần nữa. Nếu executor gọi nhiều lần:

```js
new Promise((resolve, reject) => {
  resolve(1);
  resolve(2);
  reject(new Error("late"));
});
```

settlement đầu tiên quyết định state.

## Resolution khác fulfillment

Đây là nuance quan trọng khi Promise nhận một Promise/thenable khác.

```js
const inner = new Promise((resolve) => {
  setTimeout(() => resolve(42), 1000);
});

const outer = Promise.resolve(inner);
```

`outer` được **resolved to** `inner`, nghĩa là nó adopt eventual state của `inner`. Nó chưa necessarily fulfilled ngay tại thời điểm relationship được thiết lập.

Mental model hữu ích:

```text
return plain value
→ next Promise fulfill với value

throw error
→ next Promise reject

return Promise/thenable
→ next Promise adopt eventual state
```

## `.then()` không sửa Promise cũ

```js
const p1 = Promise.resolve(10);
const p2 = p1.then((value) => value * 2);
```

`p1` và `p2` là hai Promise khác nhau. Đây là nền tảng của chaining. Mỗi `.then()` tạo một continuation và một Promise cho kết quả continuation đó.

## Promise handlers luôn asynchronous so với current synchronous stack

```js
console.log("A");

Promise.resolve().then(() => {
  console.log("B");
});

console.log("C");
```

Output:

```text
A
C
B
```

Ngay cả Promise đã fulfilled sẵn, handler `.then()` vẫn không chạy inline giữa `A` và `C`; nó được enqueue để chạy ở microtask checkpoint.

## Thenable assimilation

Promise resolution không chỉ nhận native Promise. Object có callable `then` cũng có thể được assimilate:

```js
const thenable = {
  then(resolve) {
    resolve(123);
  }
};

const value = await Promise.resolve(thenable);
console.log(value); // 123
```

Điều này cho interoperability với Promise-like implementations, nhưng cũng có nghĩa “đọc/resolve một thenable” có thể invoke user-defined behavior. Ở application code bình thường bạn không cần tự implement thenable; chỉ cần hiểu tại sao Promise có thể adopt non-native Promise-like values.

## `.catch()` và `.finally()` cũng tiếp tục chain

`.catch(onRejected)` về cơ bản là một form của `.then(undefined, onRejected)` và trả Promise mới. Nếu catch return value, chain có thể recover:

```js
const value = await Promise.reject(
  new Error("failed")
).catch(() => {
  return "fallback";
});
```

`value` là `"fallback"`.

`finally()` chủ yếu dùng cleanup không phụ thuộc success/failure. Nếu finally callback không throw/return rejected Promise, original outcome đi tiếp.

### Senior note

Promise chain nên phản ánh ownership của async flow. Catch quá sớm rồi biến mọi error thành `null` thường phá error semantics; catch ở nơi bạn thật sự có thể recover, translate hoặc add context.

---

# Chương 22 — `async` / `await` semantics

> **Version note — ES2017:** Async functions/`await` thuộc ES2017. Top-level `await` trong modules thuộc ES2022; một runtime support `await` bên trong async function chưa chắc support top-level await nếu quá cũ.

`async function` luôn trả Promise. `throw` trong async function trở thành rejected Promise.

```js
async function run() {
  throw new Error("failed");
}
```

`await expression` đợi Promise-like completion và suspend continuation của async function; nó không block browser main thread theo kiểu sleep.

Sequential dependency:

```js
const user = await loadUser();
const orders = await loadOrders(user.id);
```

Independent operations:

```js
const [profile, settings] = await Promise.all([
  loadProfile(),
  loadSettings()
]);
```

## `await` tạm dừng function, không tạm dừng thread

```js
async function load() {
  console.log("before");
  const user = await loadUser();
  console.log("after", user);
}
```

Khi `loadUser()` chưa hoàn thành, phần continuation sau `await` được suspend. JavaScript main thread có thể xử lý event/task khác. Khi awaited value settle thành công, continuation được schedule để chạy lại qua Promise-job/microtask semantics.

Vì vậy `await` không tương đương:

```text
sleep thread cho đến khi xong
```

mà gần hơn với:

```text
start/obtain async value
return control to runtime
resume function later with result
```

## Async function luôn wrap return value thành Promise outcome

```js
async function getNumber() {
  return 10;
}
```

Caller nhận Promise fulfillment với 10:

```js
getNumber().then(console.log);
```

Nếu return một Promise:

```js
async function getUser() {
  return fetchUser();
}
```

async function adopt eventual result, không tạo “Promise bên trong Promise” theo cách caller phải await hai lần.

Nếu throw:

```js
async function fail() {
  throw new Error("boom");
}
```

caller nhận rejected Promise.

## `try/catch` chỉ bắt rejection của phần bạn thật sự `await`

```js
async function run() {
  try {
    startAsyncWork();
  } catch (error) {
    // không nhất thiết bắt rejection của startAsyncWork
  }
}
```

Nếu `startAsyncWork()` trả Promise reject sau đó mà bạn không `await`/return nó, rejection tách khỏi synchronous `try` flow.

```js
async function run() {
  try {
    await startAsyncWork();
  } catch (error) {
    // bắt được rejection ở đây
  }
}
```

Đây là nguồn phổ biến của unhandled rejections trong code tưởng rằng đã có try/catch.

## Start concurrent work trước, await sau

Hai operation independent nhưng viết:

```js
const profile = await loadProfile();
const settings = await loadSettings();
```

thì request thứ hai chỉ bắt đầu sau request đầu xong. Nếu independent, có thể start cả hai trước:

```js
const profilePromise = loadProfile();
const settingsPromise = loadSettings();

const profile = await profilePromise;
const settings = await settingsPromise;
```

hoặc rõ hơn:

```js
const [profile, settings] = await Promise.all([
  loadProfile(),
  loadSettings()
]);
```

Senior concern ở đây là **dependency graph**, không phải “await chậm”. Sequential là đúng khi operation B cần result A; concurrent là đúng khi chúng độc lập và concurrency level hợp lý.

### Async `forEach` trap

```js
items.forEach(async (item) => {
  await saveItem(item);
});
```

`forEach` không await callbacks. Nếu cần sequential:

```js
for (const item of items) {
  await saveItem(item);
}
```

Nếu independent parallel:

```js
await Promise.all(
  items.map(saveItem)
);
```

Nhưng với collection rất lớn, `Promise.all(items.map(...))` có thể tạo unbounded concurrency. Senior sẽ dùng pool/semaphore/mapLimit khi cần bound resource pressure.

---

# Chương 23 — Event Loop: synchronous stack, tasks và microtasks

Browser JavaScript thường chạy UI JS trên main thread. Event loop phối hợp call stack, tasks, microtasks và rendering opportunities.

```js
console.log("A");

Promise.resolve().then(() => {
  console.log("B");
});

setTimeout(() => {
  console.log("C");
}, 0);

console.log("D");
```

Typical output:

```text
A
D
B
C
```

Current synchronous stack chạy trước. Promise continuation được schedule như microtask. Timer callback là task và thường chạy sau microtasks của current turn.

`queueMicrotask`:

```js
queueMicrotask(() => {
  console.log("microtask");
});
```

## Browser event loop không phải một “queue duy nhất”

Mental model beginner thường nói “callback queue”. Đủ để bắt đầu, nhưng ở Intermediate nên nâng lên:

```text
run one task
↓
execute synchronous call stack until empty
↓
perform microtask checkpoint
↓
possibly update rendering
↓
select next task
```

“Task” có thể đến từ timer, user interaction, networking/other host sources tùy browser specification. Không nên dựa vào một thứ tự tổng quát giữa mọi task source ngoài guarantees cụ thể.

## Microtask checkpoint drain đến khi queue rỗng

Nếu một microtask enqueue microtask khác, runtime tiếp tục xử lý trước khi quay về task/render opportunity.

```js
queueMicrotask(() => {
  console.log("M1");

  queueMicrotask(() => {
    console.log("M2");
  });
});
```

Điều này giải thích **microtask starvation**: code liên tục enqueue microtasks có thể trì hoãn timers, input và rendering.

```js
function loop() {
  queueMicrotask(loop);
}

loop();
```

Đây là code pathological; browser không có cơ hội bình thường để tiến tới task/rendering tiếp theo.

## Promise continuation và `queueMicrotask()` cùng thuộc microtask-level scheduling

```js
console.log("A");

queueMicrotask(() => {
  console.log("microtask 1");
});

Promise.resolve().then(() => {
  console.log("promise");
});

queueMicrotask(() => {
  console.log("microtask 2");
});

console.log("B");
```

Các microtasks được enqueue theo order runtime tạo chúng, nên mental trace quan trọng là **thời điểm enqueue**, không phải syntax trông “Promise quan trọng hơn queueMicrotask”.

## Rendering không xảy ra sau mọi dòng code

Browser thường có rendering opportunities giữa event-loop turns/checkpoints khi phù hợp. Nếu một task synchronous dài 200ms, browser không thể paint UI giữa các dòng JavaScript đó dù bạn vừa thay DOM ở đầu task.

```js
button.textContent = "Working...";

heavySynchronousWork();
```

Nếu `heavySynchronousWork()` block lâu, user có thể chưa nhìn thấy text mới cho đến khi task kết thúc và browser có cơ hội render.

Đây là lý do long task ảnh hưởng responsiveness.

## `requestAnimationFrame()` không phải microtask hay timer replacement chung

`requestAnimationFrame()` là Web API để schedule callback phù hợp với rendering cycle. Nó hữu ích cho animation/DOM visual update coordination, không phải mechanism để chạy mọi business async work.

```js
requestAnimationFrame(() => {
  element.style.transform = "translateX(100px)";
});
```

Trong background tab, rendering/rAF có thể throttled hoặc pause tùy browser. Vì vậy đừng dùng rAF làm business clock.

## Trace một ví dụ đầy đủ

```js
console.log("script start");

setTimeout(() => {
  console.log("timer");
}, 0);

Promise.resolve()
  .then(() => {
    console.log("promise 1");
  })
  .then(() => {
    console.log("promise 2");
  });

queueMicrotask(() => {
  console.log("queued microtask");
});

console.log("script end");
```

Trace:

```text
current task:
  script start
  schedule timer task
  schedule promise 1 microtask
  schedule queued microtask
  script end

microtask checkpoint:
  promise 1
    → schedules promise 2
  queued microtask
  promise 2

later task:
  timer
```

Output:

```text
script start
script end
promise 1
queued microtask
promise 2
timer
```

Cách trace này đáng tin cậy hơn học thuộc một vài câu “Promise trước setTimeout”.

### Senior note

Microtasks có priority cao đến mức một chain microtasks dài có thể trì hoãn rendering/tasks. Không dùng scheduling tricks nếu không hiểu reason.

---

# Chương 24 — Timer không phải clock chính xác

`setTimeout(fn, 1000)` nghĩa gần như “đừng chạy callback trước khoảng delay này, sau đó schedule khi event loop có cơ hội”, không phải guarantee 1000ms chính xác.

Main thread bị block 3 giây thì timer 1 giây cũng chạy muộn.

`setInterval` có thể không phù hợp cho async polling nếu operation kéo dài. Recursive `setTimeout` giúp schedule lần sau sau khi lần hiện tại hoàn thành:

```js
async function poll() {
  await refresh();

  setTimeout(
    poll,
    5000
  );
}

poll();
```

---

# Chương 25 — Promise combinators

> **Version note:** `all()`/`race()` đi với Promise ES2015; `allSettled()` là ES2020; `any()` + `AggregateError` là ES2021; `withResolvers()` là ES2024; `try()` là ES2025. Chọn combinator theo failure semantics chứ không theo độ mới.

`Promise.all` đợi tất cả và reject khi một promise reject.

```js
const [user, orders] = await Promise.all([
  loadUser(),
  loadOrders()
]);
```

`Promise.allSettled` đợi tất cả, useful cho batch nơi partial failure hợp lệ.

`Promise.race` settle theo promise đầu tiên settle. Nhưng losing promises **không tự cancel**.

`Promise.any` fulfill theo promise đầu tiên fulfill; nếu tất cả reject thì `AggregateError`.

### Senior note

Chọn combinator theo business semantics. `all` nghĩa “tất cả cần thành công”. `allSettled` nghĩa “tôi quan tâm result từng task kể cả failure”.

---

# Chương 26 — AbortController và cancellation

> **Platform version note:** `AbortController`/`AbortSignal` là Web APIs, không phải ECMAScript yearly feature. `AbortSignal.timeout()` và `AbortSignal.any()` cũng có browser-compatibility timeline riêng. Vì vậy hãy kiểm tra target WebView/browser thay vì hỏi chúng thuộc ES version nào.

Promise tự thân không có universal cancellation. Browser APIs như fetch nhận `AbortSignal`.

```js
const controller = new AbortController();

fetch("/api/users", {
  signal: controller.signal
});

controller.abort();
```

Service API nên nhận signal từ caller:

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

### Programming pattern — caller owns lifetime

Page/component tạo controller và abort khi navigation/unmount/new request làm operation cũ obsolete.

### Senior note

Cancellation và “ignore stale result” là hai strategies khác nhau. Có operations không cancel được, khi đó request versioning vẫn cần.

---

# Chương 27 — Race condition và stale results

Autocomplete example:

```text
request A: "ja"
request B: "java"
B trả về trước
A trả về sau
```

Nếu render result cuối cùng nhận được, UI có thể quay về kết quả cũ của A.

Strategy 1: abort old request.

Strategy 2: request version:

```js
let requestId = 0;

async function search(keyword) {
  const id = ++requestId;
  const result = await api.search(keyword);

  if (id !== requestId) {
    return;
  }

  render(result);
}
```

Race condition là vấn đề timing, không phải syntax.

---

# Chương 28 — Iterator protocol

> **Version note — ES2015 và ES2025:** Iterator protocol, `Symbol.iterator`, `for...of` và generators thuộc ES2015. ES2025 bổ sung global `Iterator` cùng helpers như `map`, `filter`, `take`, `drop`, `flatMap`, `reduce` và `toArray` cho lazy pipelines.

Iterable object có `Symbol.iterator` trả iterator. Iterator có `next()` trả `{ value, done }`.

```js
const iterator = [10, 20][Symbol.iterator]();

iterator.next();
// { value: 10, done: false }
```

`for...of` sử dụng iterable protocol.

Array, String, Map, Set đều iterable. Plain object không iterable mặc định.

Custom iterable:

```js
const range = {
  start: 1,
  end: 3,

  [Symbol.iterator]() {
    let current = this.start;
    const end = this.end;

    return {
      next() {
        if (current <= end) {
          return {
            value: current++,
            done: false
          };
        }

        return {
          done: true
        };
      }
    };
  }
};
```

### Design pattern

Đây chính là Iterator Pattern ở language level.

---

# Chương 29 — Generator và lazy evaluation

> **Version note — ES2015/ES6:** Generator `function*`/`yield` thuộc ES2015. Async generators là bước phát triển tiếp theo và thuộc ES2018.

Generator function:

```js
function* range(start, end) {
  for (
    let value = start;
    value <= end;
    value += 1
  ) {
    yield value;
  }
}
```

```js
for (const value of range(1, 3)) {
  console.log(value);
}
```

Generator tạo values lazily, khi consumer yêu cầu.

Infinite sequence:

```js
function* ids() {
  let id = 1;

  while (true) {
    yield id;
    id += 1;
  }
}
```

Không tạo infinite array trong memory.

### Senior note

Generator rất hữu ích cho lazy pipelines nhưng array methods đơn giản hơn cho ordinary small collections. Đừng dùng generator chỉ để thể hiện advanced skill.

---

# Chương 30 — Async iterator và `for await...of`

> **Version note — ES2018:** Async iteration, async iterator protocol, async generators và `for await...of` được chuẩn hóa ở ES2018. Legacy runtimes trước đó thường dùng event/callback/Promise loops cho các flow tương tự.

Async generator:

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
  render(items);
}
```

Concept này useful cho pagination, streams và progressive data. Senior sẽ học backpressure sâu hơn.

---

# Chương 31 — Functional programming thực dụng

Bạn không cần biến JavaScript thành pure-functional language. Các ý hữu ích nhất là pure function, immutability, composition, declarative transformations và side-effect boundaries.

```js
function calculateTax(
  subtotal,
  rate
) {
  return subtotal * rate;
}
```

Pure function dễ test vì output chỉ phụ thuộc input.

Side effects như network/storage/DOM vẫn cần, nhưng nên explicit ở boundary.

### Programming pattern — Functional Core / Imperative Shell

```text
read input
↓
normalize pure
↓
calculate pure
↓
save/network
↓
render
```

---

# Chương 32 — Immutability và structural sharing

Immutable update:

```js
const nextUser = {
  ...user,
  active: true
};
```

Nested:

```js
const nextState = {
  ...state,
  profile: {
    ...state.profile,
    name: "Kim"
  }
};
```

Chỉ branches thay đổi có object mới; branches khác giữ reference cũ. Đây là **structural sharing**.

Nó hữu ích cho reference equality và change detection trong UI state systems.

### Senior note

Immutability không miễn phí. Copy object graph cực lớn có cost. Local mutation trong isolated algorithm vẫn có thể hợp lý. Mục tiêu là kiểm soát shared state, không phải cấm assignment.

---

# Chương 33 — Function composition, pipe và partial application

Composition nối output của function này vào input function khác.

```js
const trim = (value) => value.trim();
const lower = (value) => value.toLowerCase();

const normalizeEmail = (value) =>
  lower(trim(value));
```

Generic pipe:

```js
const pipe = (...functions) =>
  (value) =>
    functions.reduce(
      (result, fn) => fn(result),
      value
    );
```

```js
const normalize = pipe(
  trim,
  lower
);
```

Partial application preconfigures arguments:

```js
function request(baseUrl, path) {
  return fetch(`${baseUrl}${path}`);
}

const apiRequest = request.bind(
  null,
  "/api"
);
```

### Senior note

Composition tốt khi contracts nhỏ/rõ. Pipeline quá abstract có thể khó debug hơn vài statements bình thường.

---

# Chương 34 — Memoization và caching computation

Memoization cache output theo input.

```js
function memoize(fn) {
  const cache = new Map();

  return (key) => {
    if (cache.has(key)) {
      return cache.get(key);
    }

    const result = fn(key);
    cache.set(key, result);
    return result;
  };
}
```

Phù hợp khi computation expensive, deterministic và same inputs lặp lại.

### Risks

Cache có thể tăng memory vô hạn nếu key space không bounded. Object keys dựa identity, nên hai `{ id: 1 }` khác nhau là keys khác. Đừng memoize cheap function chỉ vì có thể.

---

# Chương 35 — Event bubbling, capturing và delegation

DOM event thường travel qua capture phase, target phase và bubble phase. `addEventListener` mặc định nghe bubble phase.

Event delegation tận dụng bubbling để gắn một listener ở parent thay vì từng child.

```js
list.addEventListener(
  "click",
  (event) => {
    const button = event.target.closest(
      "[data-action]"
    );

    if (!button) {
      return;
    }

    handleAction(
      button.dataset.action
    );
  }
);
```

Benefits: ít listeners hơn, dynamic children vẫn được handle.

### Senior note

`event.target` có thể là nested child. `closest()` cần guard để không match element ngoài intended subtree trong complex DOM.

---

# Chương 36 — DOM lifecycle: init và cleanup

```js
function init() {
  window.addEventListener(
    "resize",
    handleResize
  );
}

function destroy() {
  window.removeEventListener(
    "resize",
    handleResize
  );
}
```

Lifecycle pattern phải áp dụng cho listener, timer, observer, subscription, worker và network cancellation.

### Senior note

Memory leak frontend thường là **ownership/lifecycle bug**, không phải “GC kém”. Ai tạo resource thì architecture phải biết ai cleanup và khi nào.

---

# Chương 37 — Browser rendering pipeline ở mức Intermediate

High-level:

```text
JavaScript
↓
style calculation
↓
layout
↓
paint
↓
composite
```

DOM read như `offsetWidth` có thể cần layout data. DOM write như thay `style.width` có thể invalidate layout. Interleave read/write nhiều lần có thể gây layout thrashing.

Batch reads rồi writes:

```js
const widths = items.map(
  (item) => item.offsetWidth
);

requestAnimationFrame(() => {
  items.forEach((item, index) => {
    item.style.width =
      `${widths[index] * 2}px`;
  });
});
```

### Senior note

Không assume mọi DOM write đều expensive ngang nhau. Performance phải profile trên workload thật.

---

# Chương 38 — API client abstraction

Raw fetch rải khắp project gây duplicate headers, auth, error handling, JSON parsing.

Một wrapper transport-level:

```js
async function requestJson(
  url,
  options = {}
) {
  const response = await fetch(
    url,
    {
      ...options,
      headers: {
        Accept: "application/json",
        ...options.headers
      }
    }
  );

  if (!response.ok) {
    throw new HttpError(
      response.status,
      "Request failed"
    );
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}
```

Feature-specific service:

```js
const userApi = {
  getUser(id) {
    return requestJson(
      `/api/users/${id}`
    );
  }
};
```

### Design pattern connection

HTTP wrapper có thể đóng vai Adapter/Facade/Gateway. Generic transport client không nên chứa business rules của User/Order.

---

# Chương 39 — Error architecture và custom error taxonomy

Không phải mọi error nên được catch ngay nơi phát sinh. Infrastructure layer có thể tạo stable error structure; UI layer chuyển error thành user message.

```js
class HttpError extends Error {
  constructor(status, message, body) {
    super(message);
    this.name = "HttpError";
    this.status = status;
    this.body = body;
  }
}
```

Service:

```js
async function loadUser(id) {
  try {
    return await userApi.getUser(id);
  } catch (error) {
    throw new Error(
      "Failed to load user",
      { cause: error }
    );
  }
}
```

`cause` giữ causal chain.

### Senior note

Error type/code là API contract. Đừng parse message string để quyết định logic. User-facing message và diagnostic details nên tách.

---

# Chương 40 — Retry và timeout fundamentals

Timeout với AbortController:

```js
async function fetchWithTimeout(
  url,
  timeoutMs = 5000
) {
  const controller = new AbortController();

  const timeoutId = setTimeout(
    () => controller.abort(),
    timeoutMs
  );

  try {
    return await fetch(url, {
      signal: controller.signal
    });
  } finally {
    clearTimeout(timeoutId);
  }
}
```

Retry chỉ phù hợp cho transient failures. Validation 400 hoặc permission 403 không tự hết vì retry.

Naive retry:

```js
async function retry(operation, attempts = 3) {
  let lastError;

  for (
    let i = 0;
    i < attempts;
    i += 1
  ) {
    try {
      return await operation();
    } catch (error) {
      lastError = error;
    }
  }

  throw lastError;
}
```

Senior sẽ học exponential backoff, jitter, idempotency và retry storm.

---

# Chương 41 — DTO Mapping và Anti-Corruption Boundary

Backend legacy có thể trả:

```js
{
  user_no: "1001",
  user_nm: "Kim",
  use_yn: "Y"
}
```

Frontend domain muốn:

```js
{
  id: "1001",
  name: "Kim",
  active: true
}
```

Mapper:

```js
function mapUserDto(dto) {
  return {
    id: dto.user_no,
    name: dto.user_nm,
    active: dto.use_yn === "Y"
  };
}
```

Đây là Adapter/Mapper/Anti-Corruption Layer. Nó rất hữu ích cho Java/Spring legacy backend, WebSquare DataMap/DataList và vendor/native APIs.

### Senior note

Không cần mapper nếu external và internal shapes thật sự giống và không có semantic benefit. Layer chỉ có giá trị khi nó bảo vệ boundary hoặc chuyển meaning.

---

# Chương 42 — State modeling và Boolean Explosion

Bad:

```js
let isLoading = false;
let isSuccess = false;
let hasError = false;
```

Bạn có thể tạo state vô lý: cả ba true.

Tốt hơn:

```js
const state = {
  status: "idle",
  data: null,
  error: null
};
```

Allowed transitions:

```text
idle → loading
loading → success
loading → error
error → loading
```

### Programming pattern — explicit state machine lite

```js
const STATUS = {
  IDLE: "idle",
  LOADING: "loading",
  SUCCESS: "success",
  ERROR: "error"
};
```

### Senior note

Nhiều “React/WebSquare state bug” thật ra là modeling bug, không phải framework bug.

---

# Chương 43 — Reducer Pattern

Reducer là pure-ish state transition function:

```js
function reducer(state, action) {
  switch (action.type) {
    case "LOAD_START":
      return {
        ...state,
        status: "loading"
      };

    case "LOAD_SUCCESS":
      return {
        ...state,
        status: "success",
        data: action.payload
      };

    default:
      return state;
  }
}
```

Mental model:

```text
previous state
+
action
=
next state
```

Reducer không nên tự fetch/network. Side effect orchestration nên ở layer khác.

### Design connections

Reducer liên quan State Pattern, Command-like actions và event-driven state transitions.

---

# Chương 44 — Observer và Pub/Sub

Observer: subject giữ list observers/subscribers và notify họ.

```js
function createStore() {
  const listeners = new Set();

  return {
    subscribe(listener) {
      listeners.add(listener);

      return () => {
        listeners.delete(listener);
      };
    },

    notify(value) {
      for (const listener of listeners) {
        listener(value);
      }
    }
  };
}
```

Pub/Sub thường có broker/event bus ở giữa, publisher không biết subscribers trực tiếp.

### Senior note

Event bus giảm coupling trực tiếp nhưng tạo hidden dependency. Event names trở thành implicit API và debug flow khó hơn. Direct function call tốt hơn khi dependency explicit không phải vấn đề.

---

# Chương 45 — Strategy Pattern bằng function

```js
const discountStrategies = {
  normal: (price) => price,
  vip: (price) => price * 0.9,
  employee: (price) => price * 0.8
};

function calculatePrice(
  price,
  strategy
) {
  return strategy(price);
}
```

Select:

```js
const strategy =
  discountStrategies[user.type] ??
  discountStrategies.normal;
```

Strategy phù hợp khi behaviors thật sự interchangeable. Hai branches nhỏ bằng `if` chưa cần pattern.

---

# Chương 46 — Factory Pattern

Factory centralizes construction rules:

```js
function createUser({
  role,
  name
}) {
  const base = {
    id: crypto.randomUUID(),
    name
  };

  if (role === "admin") {
    return {
      ...base,
      permissions: ["ALL"]
    };
  }

  return {
    ...base,
    permissions: []
  };
}
```

Factory có thể return plain object, function hoặc class instance. Không cần Factory chỉ để wrap `{ name }` nếu không có construction logic.

---

# Chương 47 — Adapter Pattern

Legacy callback API:

```js
legacyApi.loadUser(
  id,
  callback
);
```

App muốn Promise:

```js
function loadUser(id) {
  return new Promise(
    (resolve, reject) => {
      legacyApi.loadUser(
        id,
        (error, user) => {
          if (error) {
            reject(error);
            return;
          }

          resolve(user);
        }
      );
    }
  );
}
```

Adapter cực kỳ phổ biến trong enterprise integration, WebSquare submission/native plugin/vendor SDK.

---

# Chương 48 — Facade Pattern

Facade đưa API đơn giản cho subsystem phức tạp:

```js
const checkoutFacade = {
  async checkout(order) {
    validateOrder(order);
    const payment = await pay(order);
    const saved = await saveOrder(
      order,
      payment
    );
    await sendReceipt(saved);
    return saved;
  }
};
```

Facade giảm knowledge caller cần biết. Nhưng nếu facade chứa toàn hệ thống, nó biến thành God Service.

---

# Chương 49 — Command Pattern

Function registry:

```js
const commands = {
  save: () => save(),
  cancel: () => cancel(),
  refresh: () => refresh()
};
```

Command object:

```js
const command = {
  type: "UPDATE_USER",
  payload: {
    id: 1,
    name: "Kim"
  }
};
```

Command-as-data hữu ích cho queue, logging, undo/redo, reducers và distributed/event systems.

---

# Chương 50 — Middleware Pattern

Middleware wrap next operation:

```js
function withLogging(next) {
  return async (request) => {
    console.log("request", request);
    return next(request);
  };
}
```

Auth:

```js
function withAuth(next) {
  return async (request) => {
    const token = getToken();

    return next({
      ...request,
      headers: {
        ...request.headers,
        Authorization:
          `Bearer ${token}`
      }
    });
  };
}
```

Compose:

```js
const request = withLogging(
  withAuth(rawRequest)
);
```

Middleware kết hợp ideas của Decorator và Chain of Responsibility.

### Senior note

Order matters. Retry/auth/logging wrappers không thể reorder tùy tiện. Middleware contract và mutation policy phải rõ.

---

# Chương 51 — Dependency Injection không cần framework

Hard-coded dependency:

```js
async function loadUser() {
  return fetch("/api/user");
}
```

Inject:

```js
function createUserService({
  httpClient
}) {
  return {
    getUser(id) {
      return httpClient.get(
        `/users/${id}`
      );
    }
  };
}
```

Test fake:

```js
const fakeHttpClient = {
  get() {
    return Promise.resolve({
      id: 1,
      name: "Kim"
    });
  }
};
```

### Senior note

DI không đồng nghĩa Spring container. Function parameter hoặc factory dependency object thường đủ cho frontend.

---

# Chương 52 — Testing fundamentals

Pure function:

```js
function addTax(price, rate) {
  return price * (1 + rate);
}
```

Test:

```js
expect(
  addTax(100, 0.1)
).toBe(110);
```

Arrange / Act / Assert:

```text
Arrange setup
Act execute
Assert verify
```

Ưu tiên test business rules, boundary cases, error paths, state transitions và mappings.

### Senior note

Coverage % không bằng confidence. Code khó test thường cho thấy coupling hoặc hidden side effects.

---

# Chương 53 — Mock, Stub, Spy và Fake

Stub trả canned value. Spy theo dõi call. Mock thường là test double có expectations. Fake là implementation đơn giản nhưng functional.

Frontend code thường benefit từ simple fakes hơn heavy mocking.

```js
const fakeApi = {
  async loadUser() {
    return {
      id: 1,
      name: "Kim"
    };
  }
};
```

### Senior note

Mock boundaries, đừng mock mọi helper nội bộ. Nếu test biết implementation call order quá chi tiết, refactor implementation có thể làm test fail dù behavior không đổi.

---

# Chương 54 — Async testing principles

Không nên test bằng arbitrary sleep:

```js
await new Promise(
  (resolve) =>
    setTimeout(resolve, 2000)
);
```

Prefer chờ actual promise/event/state hoặc dùng fake timers.

Test cancellation cần verify operation abort/cleanup đúng. Race condition tests cần control ordering.

---

# Chương 55 — Debugging runtime ở mức Intermediate

DevTools Sources cho breakpoint, conditional breakpoint, call stack, scope, closure, watch expressions. Network tab cho request/response/timing. Performance cho long tasks/rendering. Memory cho heap/retainer paths.

Một quy trình debug tốt:

```text
reproduce
↓
isolate layer
↓
form hypothesis
↓
collect evidence
↓
change one thing
↓
verify
```

Không đổi năm chỗ code cùng lúc rồi đoán chỗ nào fix.

---

# Chương 56 — Intermediate Anti-patterns

Promise nesting thay vì chaining/await; missing return trong `.then`; async `forEach`; unbounded `Promise.all`; event bus cho mọi giao tiếp; deep inheritance; class cho stateless utilities; catch rồi return null mọi nơi; optional chaining để che required data; bound callback inline mà không cleanup; service object biết DOM, network, state và analytics cùng lúc; over-abstraction nhiều layer cho CRUD đơn giản; under-abstraction event handler hàng trăm dòng.

Mục tiêu của Intermediate là bắt đầu thấy **shape của complexity**, không chỉ syntax.

---

# Chương 57 — Mini Project: Search Page có cancellation và state

State:

```js
const state = {
  status: "idle",
  keyword: "",
  users: [],
  error: null
};
```

Search service giữ controller hiện tại:

```js
function createUserSearchService({
  httpClient
}) {
  let controller = null;

  return {
    async search(keyword) {
      controller?.abort();
      controller = new AbortController();

      return httpClient.get(
        `/users?q=${encodeURIComponent(keyword)}`,
        {
          signal: controller.signal
        }
      );
    },

    cancel() {
      controller?.abort();
    }
  };
}
```

Project này kết hợp closure, cancellation, service, state modeling, error handling và lifecycle.

---

# Chương 58 — Mini Project: Event-driven Store

```js
function createStore(
  reducer,
  initialState
) {
  let state = initialState;
  const listeners = new Set();

  return {
    getState() {
      return state;
    },

    dispatch(action) {
      const nextState = reducer(
        state,
        action
      );

      if (Object.is(
        nextState,
        state
      )) {
        return;
      }

      state = nextState;

      for (const listener of listeners) {
        listener(state);
      }
    },

    subscribe(listener) {
      listeners.add(listener);

      return () => {
        listeners.delete(listener);
      };
    }
  };
}
```

Bạn đang kết hợp closure, private state, reducer, Observer, immutable state và cleanup. Mental model này rất gần nhiều state-management libraries.

---

# Chương 59 — Intermediate Exit Criteria

Trước khi lên Senior, bạn phải giải thích được closure sống thế nào, `this` được bind bởi call-site ra sao, arrow khác normal function ở điểm nào, property lookup đi qua prototype chain thế nào, class liên quan prototype ra sao, Promise chain adopt returned Promise như thế nào, event loop xếp synchronous/microtask/task ra sao, sequential và concurrent khác nhau thế nào, vì sao Promise.race không cancel loser, AbortController nên thuộc lifecycle nào, state machine tốt hơn nhiều booleans ở đâu, và Dependency Injection không cần framework thế nào.

Bạn cũng phải có thể refactor một feature trộn DOM + network + business logic thành view/controller/service/pure logic ở mức vừa đủ mà không over-engineer.

---

# Chương 60 — Hướng sang Senior

Senior JavaScript sẽ không tập trung thêm syntax. Nó tập trung runtime/engine, memory/GC, resource ownership, bounded concurrency, Workers/Streams/backpressure, performance profiling, security, XSS/CSP/Trusted Types, prototype pollution, architecture boundaries, resilience, caching, observability và production testing. Đây là bước chuyển từ “developer hiểu language” sang “developer chịu trách nhiệm hệ thống chạy ổn trong production”.