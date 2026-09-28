# JavaScript Beginner — Giáo trình nền tảng từ con số 0

> **Mạch đọc:** Đọc **JavaScript Beginner — Giáo trình nền tảng từ con số 0** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Timeline tối thiểu nên hiểu** sang **Ví dụ đầu tiên**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


> **Mục tiêu của tài liệu này**: giúp người chưa có nền tảng JavaScript có thể đọc từ đầu đến cuối và hiểu được JavaScript theo đúng mô hình tư duy (mental model / 사고 모델), thay vì chỉ học thuộc cú pháp. Phần này đi chậm, giải thích vì sao một cú pháp tồn tại, cách nó hoạt động, khi nào nên dùng, lỗi người mới thường gặp, và liên hệ với cách viết mã (code / 코드) thực tế trong frontend/WebSquare/React sau này.
>
> **Nguyên tắc học**: không cố nhớ toàn bộ phương thức (method / 메서드). Hãy hiểu nhóm khái niệm, sau đó dùng ví dụ để hình thành phản xạ. Khi sang Intermediate, bạn sẽ đào sâu cơ chế bên trong như closure, `this`, prototype và vòng lặp sự kiện (event loop / 이벤트 루프).

---

<!-- VERSION-GUIDE-BEGIN -->
# Cách đọc “phiên bản (version / 버전) JavaScript” trong tài liệu này

JavaScript cốt lõi (core / 핵심) được chuẩn hóa dưới tên **ECMAScript** trong tiêu chuẩn ECMA-262. Trước năm 2015, cộng đồng thường gọi các phiên bản bằng số edition như ES3 và ES5. Phiên bản thứ sáu là trường hợp đặc biệt vì bạn sẽ gặp cả hai tên **ES6** và **ES2015**; hai tên này chỉ cùng một phiên bản. Từ ES2016 trở đi, TC39 chuyển sang chu kỳ phát hành hằng năm nên tên chính thức thường gắn với năm: ES2017, ES2018, ES2020, ES2025, ES2026. Tính đến tháng 9 năm 2026, snapshot chính thức mới nhất là **ECMAScript 2026, ECMA-262 17th edition**. Điều này không có nghĩa bạn phải học lại JavaScript mỗi năm; các phiên bản mới chủ yếu bổ sung tính năng (feature / 기능) và tinh chỉnh ngữ nghĩa (semantics / 의미론) trên nền ngôn ngữ cũ.

Khi một chương có ghi **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015** hay **phiên bản (version / 버전) ghi chú (note / 노트) — ES2020**, điều đó chỉ nói tính năng (feature / 기능) được đưa vào ECMAScript tiêu chuẩn (standard / 표준) ở edition nào. Nó **không đồng nghĩa mọi trình duyệt (browser / 브라우저) hoặc WebView đều hỗ trợ (support / 지원) tính năng (feature / 기능) đó ngay lập tức**. Một Android hệ thống (system / 시스템) WebView trong ứng dụng enterprise có thể cũ hơn Chrome desktop rất nhiều. Ngược lại, trình duyệt (browser / 브라우저) đôi khi thử triển khai proposal trước khi yearly tiêu chuẩn (standard / 표준) được phát hành. Vì thế phiên bản (version / 버전) chuẩn giúp bạn hiểu lịch sử và thế hệ của cú pháp (syntax / 문법)/API, còn quyết định môi trường vận hành (production / 운영 환경) phải dựa vào trình duyệt (browser / 브라우저)/WebView tính tương thích (compatibility / 호환성) thực tế.

Bạn cũng cần tách ECMAScript khỏi Web APIs. `const`, arrow hàm (function / 함수), Promise, Map, Set, optional chaining hay `toSorted()` là ECMAScript features. `document`, DOM events, `fetch`, `localStorage`, `URL`, `AbortController`, WebSocket và Web Workers là API do nền tảng Web (web platform / 웹 플랫폼) cung cấp, nên chúng không có “ES2020/ES2021 phiên bản (version / 버전)” theo cách tính năng (feature / 기능) của ECMA-262 có. Đây là lý do một dự án (project / 프로젝트) có thể hỗ trợ cú pháp (syntax / 문법) JavaScript mới nhưng vẫn thiếu một Web API, hoặc ngược lại.

Một từ khác thường gặp là **ESNext**. Đây không phải một phiên bản (version / 버전) cố định. Nó chỉ có nghĩa “những tính năng (feature / 기능) hướng tới phiên bản tiếp theo ở thời điểm bài viết được viết”. Vì vậy một bài năm 2020 và một bài năm 2026 dùng chữ ESNext có thể đang nói về hai nhóm tính năng (feature / 기능) khác nhau. Khi đọc mã (code / 코드) hoặc tài liệu, hãy quan tâm **tên tính năng (feature / 기능) + trạng thái chuẩn + tính tương thích (compatibility / 호환성)**, đừng chỉ nhìn chữ ESNext.

## Timeline tối thiểu nên hiểu

Bạn không cần học thuộc lịch sử, nhưng vài cột mốc giúp đọc mã (code / 코드) rất nhanh. **ES5 (2009)** đưa strict chế độ (mode / 모드), JSON hỗ trợ (support / 지원) và nhiều array/đối tượng (object / 객체) APIs vào chuẩn. **ES2015/ES6** là bước nhảy lớn với `let`, `const`, arrow functions, template literals, destructuring, classes, modules, Promise, Map/Set, Symbol, iterator và generator. **ES2016** thêm `**` và `Array.prototype.includes()`. **ES2017** đưa `async/await` vào chuẩn. **ES2018** thêm async iteration và đối tượng (object / 객체) rest/spread. **ES2019** thêm `flat()`, `flatMap()` và `Object.fromEntries()`. **ES2020** thêm BigInt, optional chaining, `??`, động (dynamic / 동적) `import()` và `Promise.allSettled()`. **ES2021** thêm `Promise.any()`, `AggregateError`, `replaceAll()`, logical assignment và WeakRef/FinalizationRegistry. **ES2022** thêm top-level `await`, lớp (class / 클래스) fields/private elements/static blocks, `Error.cause`, `.at()` và `Object.hasOwn()`. **ES2023** thêm nhóm copying array methods như `toSorted()`, `toReversed()`, `toSpliced()`, `with()`, cùng `findLast()`. **ES2024** thêm `Promise.withResolvers()`, `Object.groupBy()`, `Map.groupBy()` và resizable/transferable ArrayBuffer facilities. **ES2025** thêm Iterator Helpers, Set operations, `RegExp.escape()`, `Promise.try()` và import attributes/JSON-module hỗ trợ (support / 지원). **ES2026** là snapshot chính thức hiện hành; khi tính năng (feature / 기능) mới hơn xuất hiện, tài liệu nên ghi rõ proposal/post-snapshot thay vì đoán nó thuộc năm nào.

Mục tiêu của phiên bản (version / 버전) ghi chú (note / 노트) không phải để bạn đi thi thuộc “phương thức (method / 메서드) X ra năm Y”. Nó giúp bạn hiểu vì sao mã (code / 코드) cũ dùng cách dài hơn, vì sao Babel từng cần thiết cho một số cú pháp (syntax / 문법), và vì sao tính năng (feature / 기능) mới như `toSorted()` cần kiểm tra WebView mục tiêu (target / 대상) trong khi `map()` gần như không còn là vấn đề tính tương thích (compatibility / 호환성) trên thời gian chạy (runtime / 런타임) hiện đại.
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — JavaScript là gì và nó đứng ở đâu trong một ứng dụng web?

JavaScript là ngôn ngữ lập trình được dùng rộng rãi nhất ở phía trình duyệt. Nếu HTML mô tả cấu trúc của trang và CSS mô tả cách trang được trình bày, thì JavaScript xử lý hành vi và lô-gic (logic / 논리): click button, validate form, gọi API, cập nhật dữ liệu, mở popup, thay đổi trạng thái (state / 상태) của màn hình, xử lý timer, điều khiển WebView hoặc giao tiếp với bản địa (native / 네이티브) plugin trong ứng dụng hybrid.

Điều đầu tiên cần phân biệt là **JavaScript ngôn ngữ (language / 언어)** và **trình duyệt (browser / 브라우저) APIs**. Những thứ như `let`, `const`, đối tượng (object / 객체), array, hàm (function / 함수), lớp (class / 클래스) hay Promise thuộc về ngôn ngữ JavaScript/ECMAScript. Trong khi đó `document`, `fetch`, `localStorage`, `setTimeout`, `WebSocket`, `AbortController` hay `MutationObserver` là API do môi trường chạy cung cấp. Trên trình duyệt (browser / 브라우저), JavaScript được trình duyệt (browser / 브라우저) cung cấp những API này. Trên nút (node / 노드).js, bạn có một tập API khác. Trong WebView của hybrid app, bạn vừa có JavaScript, vừa có trình duyệt (browser / 브라우저)/WebView APIs, và đôi khi còn có cầu nối (bridge / 브리지) do bản địa (native / 네이티브) side expose.

Vì vậy khi một đoạn mã (code / 코드) không chạy, câu hỏi đầu tiên của nhà phát triển (developer / 개발자) có kinh nghiệm là: lỗi nằm ở **ngôn ngữ (language / 언어)**, **trình duyệt (browser / 브라우저) API**, **thời gian chạy (runtime / 런타임)**, **mạng (network / 네트워크)**, hay **khung phần mềm (framework / 프레임워크)**? Tư duy tách tầng (layer / 계층) này giúp bạn gỡ lỗi (debug / 디버그) nhanh hơn rất nhiều.

Tên chuẩn của lõi ngôn ngữ là ECMAScript. Khi tài liệu nhắc ES2015, ES2020 hay ES2025, đó là các phiên bản của chuẩn. Bạn không cần thuộc năm của từng tính năng (feature / 기능), nhưng cần hiểu JavaScript hiện đại được bổ sung dần qua các phiên bản ECMAScript.

### Ví dụ đầu tiên

```js
const userName = "Kim";

function greet(name) {
  return `Hello ${name}`;
}

console.log(greet(userName));
```

Đoạn mã (code / 코드) này chỉ dùng JavaScript cốt lõi (core / 핵심). Nếu thêm:

```js
document.querySelector("#message").textContent = greet(userName);
```

thì `document` và `querySelector` thuộc trình duyệt (browser / 브라우저) DOM API.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Đừng học JavaScript theo kiểu “mọi thứ tôi thấy trong trình duyệt (browser / 브라우저) đều là JavaScript”. Sau này khi học React, WebSquareJS hoặc nút (node / 노드).js, việc biết ranh giới giữa ngôn ngữ (language / 언어) và thời gian chạy (runtime / 런타임) giúp bạn biết phần nào là kiến thức dùng chung, phần nào là khung phần mềm (framework / 프레임워크)/platform-specific.

---

# Chương 2 — Cách JavaScript thực thi mã (code / 코드) ở mức nền tảng

Ở mức Beginner, bạn chưa cần hiểu Trình biên dịch JIT (JIT compiler / JIT 컴파일러) hay engine tối ưu hóa (optimization / 최적화). Nhưng bạn cần biết rằng JavaScript thực thi các câu lệnh synchronous theo thứ tự, hàm (function / 함수) được gọi thì thực thi (execution / 실행) đi vào hàm (function / 함수), sau đó quay lại vị trí gọi khi hàm (function / 함수) kết thúc.

```js
console.log("A");

function run() {
  console.log("B");
}

run();

console.log("C");
```

Đầu ra (output / 출력) là:

```text
A
B
C
```

Điều đáng chú ý là asynchronous công việc (work / 작업) không phá ngang đoạn synchronous đang chạy. Ví dụ:

```js
console.log("A");

setTimeout(() => {
  console.log("B");
}, 0);

console.log("C");
```

Đầu ra (output / 출력) thông thường là:

```text
A
C
B
```

`setTimeout(..., 0)` không có nghĩa “chạy ngay bây giờ”. Nó có nghĩa gần hơn với “hãy schedule callback này để có cơ hội chạy sau hiện tại (current / 현재) công việc (work / 작업)”. Tại sao Promise callback lại chạy trước timer callback sẽ được giải thích kỹ ở Intermediate khi học vòng lặp sự kiện (event loop / 이벤트 루프) và microtask.

Mô hình tư duy (mental model / 사고 모델) quan trọng nhất ở đây là: **synchronous mã (code / 코드) chạy trước, asynchronous callback được schedule**. Khi mã (code / 코드) frontend bị “đơ”, rất nhiều khi nguyên nhân là synchronous tác vụ (task / 작업) chạy quá lâu trên main luồng thực thi (thread / 스레드).

---

# Chương 3 — Statement, expression, khối (block / 블록) và comment

Một **expression** là đoạn mã (code / 코드) tạo ra giá trị (value / 값). Ví dụ `1 + 2`, `user.name`, `isActive ? "Y" : "N"` đều là expression. Một **statement** là câu lệnh điều khiển hoặc thực hiện hành động, ví dụ khai báo biến, `if`, `for`, `return`.

```js
const total = 10 + 20;
```

Ở đây `10 + 20` là expression, còn toàn bộ khai báo `const total = ...` là statement.

Khối (block / 블록) là phần mã (code / 코드) nằm trong `{}`:

```js
if (total > 20) {
  const message = "large";
  console.log(message);
}
```

Khối (block / 블록) quan trọng vì `let` và `const` có **khối (block / 블록) phạm vi (scope / 범위)**. Variable `message` chỉ tồn tại trong khối (block / 블록) đó.

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

Một thói quen tốt là comment **lý do** hoặc ràng buộc (constraint / 제약조건), không comment thứ mã (code / 코드) đã quá rõ. Comment kiểu `// increment count` ngay trên `count += 1` không thêm giá trị.

---

# Chương 4 — `const`, `let`, `var`: cách khai báo biến đúng trong JavaScript hiện đại

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** `var` đã tồn tại từ JavaScript rất sớm. `let` và `const` được chuẩn hóa ở ES2015 cùng lexical khối (block / 블록) phạm vi (scope / 범위). Vì vậy legacy mã (code / 코드) trước ES2015 thường dùng `var` ở mọi nơi, còn mã (code / 코드) hiện đại ưu tiên `const` rồi mới đến `let`.

JavaScript hiện đại có ba từ khóa khai báo biến: `const`, `let`, `var`. Quy tắc thực dụng cho mã (code / 코드) mới là: **dùng `const` mặc định, dùng `let` khi cần reassign, tránh `var` trừ khi đọc legacy mã (code / 코드)**.

```js
const apiUrl = "/api/users";
```

`apiUrl` không thể được gán sang giá trị (value / 값) khác:

```js
// apiUrl = "/api/orders"; // lỗi
```

Nếu giá trị (value / 값) cần thay đổi:

```js
let retryCount = 0;

retryCount += 1;
```

Một hiểu nhầm phổ biến là `const` làm đối tượng (object / 객체) immutable. Thực tế `const` chỉ khóa **binding**, không khóa nội dung đối tượng (object / 객체).

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

`var` có hàm (function / 함수) phạm vi (scope / 범위) và hoisting ngữ nghĩa (semantics / 의미론) cũ. Bạn sẽ gặp nó trong mã (code / 코드) WebSquare/legacy JavaScript, nhưng không nên dùng cho mã (code / 코드) mới nếu không có lý do đặc biệt.

### Lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)

```js
const users = [];
const config = {};
const MAX_RETRY = 3;

let currentPage = 1;
let loading = false;
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Ưu tiên `const` giúp giảm số chỗ binding có thể thay đổi. Điều này làm lập luận (reasoning / 추론) dễ hơn và giảm bug, chứ không phải vì `const` “tối ưu nhanh hơn”.

---

# Chương 5 — thành phần nguyên thủy (primitive / 기본 요소) types và đối tượng (object / 객체) types

JavaScript có bảy thành phần nguyên thủy (primitive / 기본 요소) types: `string`, `number`, `boolean`, `undefined`, `null`, `bigint`, `symbol`. Ngoài những thành phần nguyên thủy (primitive / 기본 요소) này, còn lại về bản chất thuộc nhóm đối tượng (object / 객체), bao gồm đối tượng (object / 객체) literal, array, hàm (function / 함수), Date, Map và Set.

```js
const name = "Kim";       // string
const age = 30;           // number
const active = true;      // boolean
const missing = undefined;
const empty = null;
const huge = 9007199254740993n; // bigint
const idKey = Symbol("id");
```

Đối tượng (object / 객체):

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

Hàm (function / 함수):

```js
function greet() {
  return "hello";
}
```

Điểm quan trọng là JavaScript động (dynamic / 동적) typing: variable không bị gắn kiểu (type / 타입) cố định như Java variable. Bạn có thể viết:

```js
let value = 10;
value = "ten";
```

Mã (code / 코드) hợp lệ ở thời gian chạy (runtime / 런타임) JavaScript, dù TypeScript sau này có thể ngăn bạn nếu kiểu (type / 타입) đã được xác định.

---

# Chương 6 — `typeof`, `Array.isArray()` và các trường hợp đặc biệt

`typeof` trả một string mô tả category thời gian chạy (runtime / 런타임) của giá trị (value / 값).

```js
typeof "hello";    // "string"
typeof 10;         // "number"
typeof true;       // "boolean"
typeof undefined;  // "undefined"
typeof 10n;        // "bigint"
typeof Symbol();   // "symbol"
```

Hàm (function / 함수):

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

Do đó check đối tượng (object / 객체) thường phải loại null:

```js
if (
  typeof value === "object" &&
  value !== null
) {
  // object-like value
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Các trường hợp biên (edge case / 경계 사례) như `typeof null` là lý do cấp cao (senior / 시니어) không viết kiểm tra hợp lệ (validation / 검증) bằng cảm giác. Khi validate bên ngoài (external / 외부) dữ liệu (data / 데이터), cần check đúng ngữ nghĩa (semantics / 의미론) thay vì chỉ một `typeof` đơn giản.

---

# Chương 7 — thành phần nguyên thủy (primitive / 기본 요소) bản sao (copy / 복사) và đối tượng (object / 객체) tham chiếu (reference / 참조)

Thành phần nguyên thủy (primitive / 기본 요소) thường được bản sao (copy / 복사) theo giá trị (value / 값):

```js
let a = 10;
let b = a;

b = 20;

console.log(a); // 10
```

Đối tượng (object / 객체) variable giữ tham chiếu (reference / 참조) tới đối tượng (object / 객체). Khi gán đối tượng (object / 객체) variable sang variable khác, hai variable có thể trỏ cùng đối tượng (object / 객체):

```js
const user1 = {
  name: "Kim"
};

const user2 = user1;

user2.name = "Lee";

console.log(user1.name);
// "Lee"
```

Đây là kiến thức nền tảng cực kỳ quan trọng cho frontend. Nhiều bug trạng thái (state / 상태) xảy ra vì nhà phát triển (developer / 개발자) nghĩ mình “bản sao (copy / 복사) đối tượng (object / 객체)” nhưng thực chất chỉ bản sao (copy / 복사) tham chiếu (reference / 참조).

Spread tạo shallow bản sao (copy / 복사):

```js
const user2 = {
  ...user1
};
```

Nhưng nếu đối tượng (object / 객체) có nested đối tượng (object / 객체):

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

`profile` vẫn cùng tham chiếu (reference / 참조).

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — immutable cập nhật (update / 업데이트)

Nếu muốn đổi nested thuộc tính (property / 속성) mà giữ đối tượng (object / 객체) cũ:

```js
const nextUser = {
  ...user1,
  profile: {
    ...user1.profile,
    name: "Lee"
  }
};
```

React trạng thái (state / 상태) cập nhật (update / 업데이트), reducers và nhiều state-management patterns dựa trên concept này.

---

# Chương 8 — Number, `NaN`, Infinity và floating-point

JavaScript dùng `number` cho cả integer và floating-point thông thường.

```js
const count = 10;
const price = 19.99;
```

Một điều bắt buộc phải biết là nhị phân (binary / 이진) floating-point không thể biểu diễn chính xác mọi decimal fraction.

```js
0.1 + 0.2;
// 0.30000000000000004
```

Vì vậy:

```js
0.1 + 0.2 === 0.3;
// false
```

`NaN` nghĩa là “Not-a-Number”, nhưng chính nó có kiểu (type / 타입) `number`:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Với tiền, lãi suất hoặc dữ liệu tài chính cần precision cao, đừng mặc định `number` là biểu diễn (representation / 표현) đúng. Có thể cần minor units hoặc decimal thư viện (library / 라이브러리)/backend decimal handling.

---

# Chương 9 — String và template literal

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** Backtick template literals, `${expression}` interpolation và multiline template strings được chuẩn hóa trong ES2015. String là kiểu (type / 타입) rất cũ; tính năng (feature / 기능) mới ở đây là template-literal cú pháp (syntax / 문법).

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

Các phương thức (method / 메서드) thường dùng gồm `trim`, `includes`, `startsWith`, `endsWith`, `slice`, `replace`, `split`, `toLowerCase`, `toUpperCase`.

```js
const email = "  USER@EXAMPLE.COM ";

const normalized = email
  .trim()
  .toLowerCase();
```

String immutable. Các phương thức (method / 메서드) không sửa original string.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

`string.length` đo UTF-16 mã (code / 코드) units, không luôn bằng số ký tự người dùng nhìn thấy. Khi xử lý emoji, grapheme hoặc multilingual văn bản (text / 텍스트) sâu, cần APIs/techniques khác. Beginner chỉ cần biết limitation tồn tại.

---

# Chương 10 — Boolean, truthy và falsy

Khi JavaScript cần quyết định điều kiện, giá trị (value / 값) được convert sang boolean. Các falsy values quan trọng là `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. Hầu hết giá trị (value / 값) khác là truthy, bao gồm đối tượng (object / 객체) rỗng và array rỗng.

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

Nhưng phải cẩn thận khi `0` hoặc empty string là giá trị (value / 값) hợp lệ:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Truthy/falsy là tiện, nhưng lô-gic nghiệp vụ (business logic / 비즈니스 로직) cần tường minh (explicit / 명시적) khi falsy values có nghĩa riêng.

---

# Chương 11 — kiểu (type / 타입) conversion và coercion

Tường minh (explicit / 명시적) conversion:

```js
String(123);
Number("123");
Boolean(value);
```

Implicit coercion xảy ra khi operator yêu cầu một loại giá trị (value / 값) nhất định.

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

Người mới thường cố học thuộc các câu đố coercion. Cách học tốt hơn là: tại ranh giới (boundary / 경계), convert tường minh (explicit / 명시적) và validate ngay.

Ví dụ truy vấn (query / 쿼리) param:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Cấp cao (senior / 시니어) mã (code / 코드) tránh phụ thuộc vào coercion khó đọc khi một conversion tường minh (explicit / 명시적) làm intent rõ hơn.

---

# Chương 12 — Equality: `===`, `==`, `Object.is`

Strict equality `===` không thực hiện kiểu (type / 타입) coercion:

```js
5 === 5;   // true
5 === "5"; // false
```

Loose equality `==` có coercion:

```js
5 == "5";
// true
```

Trong ứng dụng (application / 애플리케이션) mã (code / 코드) hiện đại, `===` và `!==` là lựa chọn mặc định vì dễ lập luận (reasoning / 추론) hơn.

`Object.is` có trường hợp biên (edge case / 경계 사례) khác:

```js
Object.is(NaN, NaN);
// true

Object.is(0, -0);
// false
```

Bạn chưa cần dùng `Object.is` thường xuyên, nhưng cần biết nó tồn tại. Sau này React-style trạng thái (state / 상태) comparison cũng liên quan định danh (identity / 식별자)/equality ngữ nghĩa (semantics / 의미론).

---

# Chương 13 — Operators và cách dùng có chủ đích

> **phiên bản (version / 버전) ghi chú (note / 노트):** Exponentiation `**` thuộc ES2016. Optional chaining `?.` và nullish coalescing `??` thuộc ES2020. Logical assignment `&&=`, `||=` và `??=` thuộc ES2021. Đây là ví dụ rõ về cách JavaScript giữ nguyên operators cũ rồi bổ sung cú pháp (syntax / 문법) diễn đạt intent an toàn hơn.

Arithmetic operators gồm `+`, `-`, `*`, `/`, `%`, `**`. Assignment có `=`, `+=`, `-=`, `*=`, `/=`. Comparison có `>`, `<`, `>=`, `<=`, `===`, `!==`.

Logical operators `&&`, `||`, `!` không chỉ trả boolean; chúng trả operand theo short-circuit ngữ nghĩa (semantics / 의미론).

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

Phương thức (method / 메서드) lời gọi (call / 호출):

```js
onComplete?.();
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Optional chaining là convenience, không phải thuốc chữa mô hình dữ liệu (data model / 데이터 모델) sai. Nếu thuộc tính (property / 속성) bắt buộc mà bạn chuỗi (chain / 사슬) `?.` xuyên suốt, lỗi đặc tả hợp đồng (contract / 계약) có thể bị biến thành silent `undefined`.

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

Nested conditions làm mã (code / 코드) khó đọc:

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

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — Guard Clause

Đây là một mẫu lập trình (programming pattern / 프로그래밍 패턴) rất thực dụng. Nó làm invalid paths nằm ở đầu hàm (function / 함수), giữ happy đường dẫn (path / 경로) ít indentation.

---

# Chương 15 — `switch` và lựa chọn thay thế

`switch` phù hợp khi một giá trị (value / 값) có một số trường hợp rời rạc.

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

Nếu quên `break`, thực thi (execution / 실행) có thể fall through sang trường hợp (case / 사례) tiếp theo.

Khi mỗi trường hợp (case / 사례) chỉ map sang hàm (function / 함수), lookup đối tượng (object / 객체) có thể gọn:

```js
const handlers = {
  idle: showIdle,
  loading: showLoading,
  success: showSuccess
};

handlers[status]?.();
```

Đây bắt đầu chạm tới chiến lược (strategy / 전략)/Command-like mẫu (pattern / 패턴), nhưng không cần ép mọi switch thành đối tượng (object / 객체) registry.

---

# Chương 16 — Loops: `for`, `while`, `for...of`, `for...in`

Classic `for` phù hợp khi cần chỉ mục (index / 인덱스) hoặc kiểm soát iteration chi tiết.

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

`for...in` iterate enumerable thuộc tính (property / 속성) keys:

```js
for (const key in user) {
  console.log(key);
}
```

Không nên dùng `for...in` cho array trong ứng dụng (application / 애플리케이션) mã (code / 코드) thông thường.

`while` phù hợp khi số vòng chưa biết trước:

```js
while (queue.length > 0) {
  const task = queue.shift();
  processTask(task);
}
```

`break` thoát vòng lặp (loop / 루프), `continue` bỏ qua iteration hiện tại.

---

# Chương 17 — hàm (function / 함수) declaration, expression và arrow hàm (function / 함수)

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** Arrow hàm (function / 함수) xuất hiện trong ES2015. Nó không chỉ rút gọn `function`; lexical `this` là ngữ nghĩa (semantics / 의미론) riêng. hàm (function / 함수) declaration/expression truyền thống đã tồn tại từ các phiên bản JavaScript trước đó rất lâu.

Hàm (function / 함수) declaration:

```js
function add(a, b) {
  return a + b;
}
```

Hàm (function / 함수) expression:

```js
const add = function (a, b) {
  return a + b;
};
```

Arrow hàm (function / 함수):

```js
const add = (a, b) => a + b;
```

Ba style không hoàn toàn giống nhau. Arrow hàm (function / 함수) không có own `this`, không có own `arguments`, không thể dùng làm constructor với `new`. Chi tiết này sẽ được giải thích ở Intermediate.

Ở Beginner, quy tắc đơn giản là arrow hàm (function / 함수) rất hợp cho callback nhỏ:

```js
users.map((user) => user.name);
```

Normal phương thức (method / 메서드)/hàm (function / 함수) phù hợp khi muốn hàm (function / 함수) name rõ, declaration ngữ nghĩa (semantics / 의미론) rõ hoặc cần `this` động.

---

# Chương 18 — Parameters, default parameters, rest parameters và options đối tượng (object / 객체)

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** Default parameters và rest parameters `...args` được chuẩn hóa trong ES2015. Options đối tượng (object / 객체) là mẫu lập trình (programming pattern / 프로그래밍 패턴) do nhà phát triển (developer / 개발자) thiết kế, không phải tính năng (feature / 기능) ECMAScript có một phiên bản (version / 버전) riêng.

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

Options đối tượng (object / 객체) rõ hơn:

```js
request({
  url: "/api",
  auth: true,
  timeoutMs: 5000,
  cache: false
});
```

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — Options đối tượng (object / 객체)

Mẫu (pattern / 패턴) này đặc biệt hữu ích khi hàm (function / 함수) có từ 3 tham số trở lên, có nhiều optional values hoặc có boolean flags.

---

# Chương 19 — Return giá trị (value / 값) và early return

Một hàm (function / 함수) return giá trị (value / 값) bằng `return`:

```js
function calculateTotal(price, quantity) {
  return price * quantity;
}
```

Nếu không return tường minh (explicit / 명시적), kết quả (result / 결과) là `undefined`.

```js
function logMessage(message) {
  console.log(message);
}
```

Early return giữ mã (code / 코드) phẳng:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Nếu invalid đầu vào (input / 입력) là programmer lỗi (error / 오류) hoặc nghiệp vụ (business / 비즈니스) lỗi (error / 오류) quan trọng, có thể `throw` thay vì silent return. Guard clause không có nghĩa lúc nào cũng bỏ lỗi đi.

---

# Chương 20 — First-class functions, callbacks và higher-order thinking

JavaScript coi hàm (function / 함수) như giá trị (value / 값). Bạn có thể lưu hàm (function / 함수) vào variable, truyền hàm (function / 함수) làm argument, return hàm (function / 함수) từ hàm (function / 함수) khác.

```js
function execute(callback) {
  callback();
}

execute(() => {
  console.log("run");
});
```

Hàm (function / 함수) nhận hoặc trả hàm (function / 함수) gọi là higher-order hàm (function / 함수).

```js
function createMultiplier(factor) {
  return (value) => value * factor;
}

const double = createMultiplier(2);

console.log(double(5));
// 10
```

Bạn vừa chạm tới closure, dù phần cơ chế sâu sẽ học ở Intermediate.

First-class functions làm nhiều thiết kế (design / 설계) patterns trong JavaScript nhẹ hơn Java. chiến lược (strategy / 전략) không nhất thiết cần giao diện (interface / 인터페이스) + lớp (class / 클래스); chỉ cần hàm (function / 함수) cùng đặc tả hợp đồng (contract / 계약).

```js
const discountStrategies = {
  normal: (price) => price,
  vip: (price) => price * 0.9
};
```

---

# Chương 21 — phạm vi (scope / 범위) và vì sao phạm vi (scope / 범위) nhỏ tốt hơn

Toàn cục (global / 전역) phạm vi (scope / 범위) tồn tại rộng nhất. hàm (function / 함수) phạm vi (scope / 범위) tồn tại trong hàm (function / 함수). khối (block / 블록) phạm vi (scope / 범위) tồn tại trong `{}` với `let`/`const`.

```js
const globalValue = 1;

function run() {
  const functionValue = 2;

  if (true) {
    const blockValue = 3;
  }
}
```

`blockValue` không tồn tại ngoài `if` khối (block / 블록).

Phạm vi (scope / 범위) nhỏ giúp giảm nơi giá trị (value / 값) có thể bị đọc/mutate. Vì vậy đừng đặt mọi thứ lên `window` hay toàn cục (global / 전역) đối tượng (object / 객체) chỉ để “dễ gọi”.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Toàn cục (global / 전역) mutable trạng thái (state / 상태) là một trong những nguồn coupling khó kiểm soát nhất trong frontend legacy mã (code / 코드). mô-đun (module / 모듈) phạm vi (scope / 범위), closures và tường minh (explicit / 명시적) phụ thuộc (dependency / 의존성) injection giúp thay thế nó.

---

# Chương 22 — Hoisting và Temporal Dead Zone

Hàm (function / 함수) declaration có thể gọi trước textual declaration:

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

`let` và `const` cũng có binding trước declaration nhưng ở Temporal Dead Zone, nên truy cập (access / 접근) trước declaration throw lỗi (error / 오류):

```js
console.log(value);

const value = 10;
```

### Beginner quy tắc (rule / 규칙)

Đừng dựa vào hoisting trick. Tổ chức mã (code / 코드) để declaration dễ thấy và dùng `const`/`let` cho mã (code / 코드) mới.

---

# Chương 23 — Array: collection cơ bản nhất

> **phiên bản (version / 버전) ghi chú (note / 노트):** Array là phần nền tảng rất cũ, nhưng phương thức (method / 메서드) của Array đến từ nhiều thế hệ. `forEach`, `map`, `filter`, `some`, `every`, `reduce` được chuẩn hóa từ ES5, nên chúng đã có độ tương thích rất cao.

Array tạo bằng:

```js
const users = [
  "Kim",
  "Lee"
];
```

Truy cập (access / 접근) theo chỉ mục (index / 인덱스) bắt đầu từ 0:

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

Các phương thức (method / 메서드) đầu array thường phải dịch chuyển chỉ mục (index / 인덱스) nhiều phần tử và có thể kém hiệu quả hơn operations cuối array với collection lớn, nhưng đừng tối ưu nếu không có vấn đề thật.

---

# Chương 24 — `map`, `filter`, `find`, `some`, `every`, `includes`

> **phiên bản (version / 버전) ghi chú (note / 노트):** `map`, `filter`, `some`, `every` thuộc ES5; `find()` thuộc ES2015; `includes()` thuộc ES2016. Legacy mã (code / 코드) đôi khi dùng `indexOf(...) !== -1` vì được viết trước khi `includes()` trở thành lựa chọn chuẩn.

`map` transform mỗi element sang giá trị (value / 값) mới:

```js
const names = users.map(
  (user) => user.name
);
```

`filter` giữ element thỏa điều kiện (condition / 조건):

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

`every` hỏi “tất cả đều đúng không?”. `includes` check giá trị (value / 값) có tồn tại không.

### Lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)

```js
const activeNames = users
  .filter((user) => user.active)
  .map((user) => user.name);
```

Chuỗi (chain / 사슬) ngắn, rõ rất tốt. chuỗi (chain / 사슬) quá dài nên tách named helpers.

---

# Chương 25 — `forEach` và sự khác nhau với `map`

`forEach` dùng để chạy side tác động (effect / 효과) cho từng element:

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

Đừng dùng `map` chỉ để side tác động (effect / 효과):

```js
users.map((user) => {
  console.log(user);
});
```

nếu bạn không dùng kết quả (result / 결과) array. Khi đó `forEach` hoặc `for...of` rõ intent hơn.

Một trap quan trọng sẽ học sâu ở Intermediate: `forEach(async () => ...)` không chờ callback promises theo cách người mới thường tưởng.

---

# Chương 26 — `reduce`: mạnh nhưng không phải lúc nào cũng nên dùng

`reduce` gộp array thành một kết quả (result / 결과).

```js
const total = prices.reduce(
  (sum, price) => sum + price,
  0
);
```

Group dữ liệu (data / 데이터):

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

Nhưng nếu callback vừa filter, map, mutate, side tác động (effect / 효과) và bản dựng (build / 빌드) đối tượng (object / 객체) phức tạp, mã (code / 코드) khó đọc. Không có điểm cộng cấp cao (senior / 시니어) nào vì dùng `reduce` thay `for...of`.

---

# Chương 27 — Mutating và non-mutating array APIs

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2023:** `toSorted()`, `toReversed()`, `toSpliced()` và `with()` được chuẩn hóa ở ES2023 để cung cấp copying versions thay cho các thao tác mutate tương ứng. Chúng rất hợp với immutable-state style nhưng vẫn cần check WebView cũ.

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

hoặc `toSorted()` khi mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) hỗ trợ.

---

# Chương 28 — đối tượng (object / 객체) literal và thuộc tính (property / 속성) truy cập (access / 접근)

Đối tượng (object / 객체):

```js
const user = {
  id: 1,
  name: "Kim",
  active: true
};
```

Dot truy cập (access / 접근):

```js
user.name;
```

Bracket truy cập (access / 접근) dùng động (dynamic / 동적) key:

```js
const key = "name";
user[key];
```

Cập nhật (update / 업데이트):

```js
user.active = false;
```

Add thuộc tính (property / 속성):

```js
user.role = "admin";
```

Delete:

```js
delete user.role;
```

Phương thức (method / 메서드) shorthand:

```js
const user = {
  name: "Kim",

  greet() {
    return `Hello ${this.name}`;
  }
};
```

`this` của phương thức (method / 메서드) sẽ được giải thích sâu ở Intermediate.

---

# Chương 29 — đối tượng (object / 객체) utilities

> **phiên bản (version / 버전) ghi chú (note / 노트):** đối tượng (object / 객체) APIs trải qua nhiều thế hệ: `Object.keys()` và descriptor APIs gắn với ES5; `Object.assign()` thuộc ES2015; `Object.values()`, `Object.entries()`, `Object.getOwnPropertyDescriptors()` thuộc ES2017; `Object.fromEntries()` thuộc ES2019; `Object.hasOwn()` thuộc ES2022; `Object.groupBy()` thuộc ES2024.

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

Own thuộc tính (property / 속성) check:

```js
Object.hasOwn(user, "name");
```

`Object.assign(target, source)` bản sao (copy / 복사) properties và mutate mục tiêu (target / 대상).

---

# Chương 30 — Destructuring

Đối tượng (object / 객체) destructuring:

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

Hàm (function / 함수) parameter destructuring:

```js
function saveUser({ id, name }) {
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Destructuring tốt khi làm phụ thuộc (dependency / 의존성)/dữ liệu (data / 데이터) usage rõ. Nhưng destructure quá nhiều fields từ một đối tượng (object / 객체) lớn có thể làm mất ngữ cảnh (context / 맥락), vì sau đó đọc variable `id`, `name`, `status` không còn thấy nó thuộc đối tượng (object / 객체) nào.

---

# Chương 31 — Spread và rest

> **phiên bản (version / 버전) ghi chú (note / 노트):** Rest parameters và array spread được chuẩn hóa ở ES2015. đối tượng (object / 객체) rest/spread `{ ...obj }` đến sau ở ES2018. Vì vậy toolchain cũ từng có giai đoạn hỗ trợ array spread nhưng vẫn cần transform cho đối tượng (object / 객체) spread.

Spread đối tượng (object / 객체):

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

Hàm (function / 함수) lời gọi (call / 호출):

```js
Math.max(...numbers);
```

Rest parameter:

```js
function log(level, ...messages) {
}
```

Rest đối tượng (object / 객체):

```js
const {
  password,
  ...publicUser
} = user;
```

Spread/rest nhìn giống nhau về cú pháp (syntax / 문법) `...` nhưng ngữ cảnh (context / 맥락) quyết định nghĩa: spread “mở ra”, rest “gom lại”.

---

# Chương 32 — Set và Map

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015 và ES2025:** Map/Set/WeakMap/WeakSet được chuẩn hóa ở ES2015. ES2025 bổ sung Set operations như `union()`, `intersection()`, `difference()`, `symmetricDifference()`, `isSubsetOf()` và `isSupersetOf()`. Codebase hỗ trợ (support / 지원) thời gian chạy (runtime / 런타임) cũ thường vẫn tự viết các helper này.

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

Map key có thể là đối tượng (object / 객체), hàm (function / 함수) hoặc thành phần nguyên thủy (primitive / 기본 요소).

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Dùng đối tượng (object / 객체) khi bạn mô hình (model / 모델) một bản ghi (record / 레코드) có fixed properties. Dùng Map khi ngữ nghĩa (semantics / 의미론) thật sự là động (dynamic / 동적) dictionary/key-value collection.

---

# Chương 33 — Date và timezone basics

Hiện tại (current / 현재) date/thời gian (time / 시간):

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

vì format có thể được hiểu khác. Prefer tường minh (explicit / 명시적) ISO đặc tả hợp đồng (contract / 계약) từ API:

```text
2026-09-12T10:30:00+09:00
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Frontend/backend date-time bugs thường đến từ việc không phân biệt cục bộ (local / 로컬) thời gian (time / 시간), UTC và timezone offset. Beginner chỉ cần giữ quy tắc (rule / 규칙): wire format phải tường minh (explicit / 명시적).

---

# Chương 34 — Math và random

Dùng chung (common / 공통) APIs:

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

`Math.random()` không dành cho bảo mật (security / 보안) đơn vị từ (token / 토큰). Với ID phổ thông hiện đại, `crypto.randomUUID()` thường phù hợp hơn nếu thời gian chạy (runtime / 런타임) hỗ trợ.

---

# Chương 35 — lỗi (error / 오류), `throw`, `try`, `catch`, `finally`

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

`finally` chạy cả success và thất bại (failure / 실패), phù hợp cleanup/loading trạng thái (state / 상태).

### Anti-pattern

```js
try {
  await saveUser();
} catch (error) {
  // ignore
}
```

Swallowing lỗi (error / 오류) chỉ phù hợp nếu thất bại (failure / 실패) thật sự không quan trọng và được chủ đích document/observe ở nơi khác.

---

# Chương 36 — Custom lỗi (error / 오류) cơ bản

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

Custom lỗi (error / 오류) giúp phân biệt thất bại (failure / 실패) bằng cấu trúc (structure / 구조)/kiểu (type / 타입) thay vì parse văn bản (text / 텍스트) message.

---

# Chương 37 — JSON

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES5:** `JSON.parse()` và `JSON.stringify()` được chuẩn hóa trong ES5. JSON là dữ liệu (data / 데이터) format riêng; JavaScript đối tượng (object / 객체) literal chỉ trông giống JSON ở một số trường hợp chứ không phải cùng grammar.

Serialize đối tượng (object / 객체) sang JSON string:

```js
const text = JSON.stringify(user);
```

Parse:

```js
const user = JSON.parse(text);
```

JSON không giữ mọi JavaScript kiểu (type / 타입). hàm (function / 함수) bị bỏ, `undefined` không được represent như normal giá trị (value / 값) trong đối tượng (object / 객체), BigInt không stringify trực tiếp, circular đối tượng (object / 객체) throw.

Do đó JSON không phải “deep clone universal”. `structuredClone()` ở hiện đại (modern / 현대적) runtimes clone được nhiều kiểu (type / 타입) hơn và cycles, nhưng clone cũng có chi phí (cost / 비용) và ngữ nghĩa (semantics / 의미론) riêng.

---

# Chương 38 — DOM: chọn element

Trình duyệt (browser / 브라우저) DOM API cho phép JavaScript đọc và thay đổi document.

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

Luôn nhớ DOM có vòng đời (lifecycle / 생명주기). Nếu script chạy trước element tồn tại, selector có thể trả null.

---

# Chương 39 — DOM: tạo và cập nhật nội dung an toàn

Plain văn bản (text / 텍스트):

```js
element.textContent = user.name;
```

HTML:

```js
element.innerHTML = "<strong>Hello</strong>";
```

Không đưa untrusted đầu vào (input / 입력) trực tiếp vào `innerHTML`:

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

### Bảo mật (security / 보안) ghi chú (note / 노트)

`textContent` là lựa chọn mặc định cho plain văn bản (text / 텍스트). Khi thật sự cần kết xuất (render / 렌더링) HTML từ bên ngoài (external / 외부) nguồn (source / 소스), cần chiến lược (strategy / 전략) sanitize/trusted rendering chứ không concatenate string tùy tiện.

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

Trong codebase lớn, trạng thái (state / 상태) → CSS lớp (class / 클래스) thường dễ maintain hơn việc set hàng loạt style inline.

---

# Chương 41 — Events và sự kiện (event / 이벤트) đối tượng (object / 객체)

```js
button.addEventListener("click", (event) => {
  console.log(event);
});
```

`event.target` là element nơi sự kiện (event / 이벤트) bắt đầu; `event.currentTarget` là element listener hiện tại gắn vào.

Prevent trình duyệt (browser / 브라우저) default hành vi (behavior / 동작):

```js
event.preventDefault();
```

Stop propagation:

```js
event.stopPropagation();
```

Không dùng `stopPropagation()` như default habit vì sự kiện (event / 이벤트) bubbling là cơ chế rất hữu ích cho delegation.

---

# Chương 42 — sự kiện (event / 이벤트) listener vòng đời (lifecycle / 생명주기) và cleanup

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

Phải cùng hàm (function / 함수) tham chiếu (reference / 참조). Vì vậy nếu bạn viết anonymous callback trực tiếp, sau này cleanup khó hơn nếu không giữ tham chiếu (reference / 참조).

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — vòng đời (lifecycle / 생명주기) pair

```text
addEventListener ↔ removeEventListener
setInterval      ↔ clearInterval
subscribe        ↔ unsubscribe
open             ↔ close
```

Tư duy quyền sở hữu (ownership / 소유권) này sẽ trở thành chủ đề lớn ở cấp cao (senior / 시니어).

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

HTML built-in kiểm tra hợp lệ (validation / 검증):

```js
input.checkValidity();
form.reportValidity();
```

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) giúp UX, không thay backend kiểm tra hợp lệ (validation / 검증).

---

# Chương 44 — Timers

Hết thời gian chờ (timeout / 타임아웃):

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

Timer delay không guarantee callback chạy đúng millisecond; main luồng thực thi (thread / 스레드) bận thì callback chạy muộn.

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

Store đối tượng (object / 객체):

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

### Bảo mật (security / 보안) ghi chú (note / 노트)

localStorage có thể bị JavaScript cùng origin đọc. Đừng mặc định đây là nơi an toàn cho mọi đơn vị từ (token / 토큰)/secret. Auth lưu trữ (storage / 저장소) chiến lược (strategy / 전략) phải được thiết kế cùng backend và bảo mật (security / 보안) mô hình (model / 모델).

---

# Chương 46 — Promise: mô hình tư duy (mental model / 사고 모델) đầu tiên

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** bản địa (native / 네이티브) Promise được chuẩn hóa ở ES2015. Trước đó ecosystem dùng callback và nhiều Promise/Deferred libraries, nên legacy enterprise mã (code / 코드) thường có abstractions async khác bản địa (native / 네이티브) Promise.

Promise đại diện một thao tác (operation / 연산) có kết quả trong tương lai. Trạng thái cơ bản là pending, fulfilled, rejected.

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

Nếu quên `return`, chuỗi (chain / 사슬) tiếp theo không chờ inner Promise.

---

# Chương 47 — `async` / `await`

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2017:** `async function` và `await` được chuẩn hóa ở ES2017 và xây trên Promise, không thay Promise. Top-level `await` là tính năng (feature / 기능) riêng xuất hiện muộn hơn ở ES2022.

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

`async` hàm (function / 함수) luôn trả Promise, kể cả bạn return thành phần nguyên thủy (primitive / 기본 요소):

```js
async function getValue() {
  return 10;
}
```

caller vẫn nhận Promise.

`await` chỉ dùng trong async contexts phù hợp. Nó làm mã (code / 코드) asynchronous nhìn gần như sequential, nhưng thao tác (operation / 연산) không trở thành synchronous khối (block / 블록) toàn trình duyệt (browser / 브라우저).

---

# Chương 48 — Sequential và concurrent async công việc (work / 작업)

> **phiên bản (version / 버전) ghi chú (note / 노트):** `Promise.all()`/`race()` thuộc bộ Promise ES2015. `Promise.allSettled()` đến ở ES2020, `Promise.any()` và `AggregateError` ở ES2021, `Promise.withResolvers()` ở ES2024, còn `Promise.try()` ở ES2025.

Nếu step B phụ thuộc kết quả (result / 결과) A:

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

Beginner cần hiểu distinction, nhưng đừng chạy hàng nghìn tác vụ (task / 작업) bằng `Promise.all()` mà chưa hiểu tính đồng thời (concurrency / 동시성) điều khiển (control / 제어). Chủ đề đó thuộc cấp cao (senior / 시니어).

---

# Chương 49 — `fetch` và HTTP căn bản

```js
const response = await fetch("/api/users");
```

`fetch` không reject chỉ vì máy chủ (server / 서버) trả 404 hoặc 500. Cần check:

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

HTTP methods bạn nên hiểu ở mức ý nghĩa: GET đọc, POST tạo/hành động (action / 동작), PUT/PATCH cập nhật (update / 업데이트) theo đặc tả hợp đồng (contract / 계약), DELETE xóa. Status 2xx thành công, 4xx thường yêu cầu (request / 요청)/auth/máy khách (client / 클라이언트) side issues, 5xx máy chủ (server / 서버) side issues.

---

# Chương 50 — URL và truy vấn (query / 쿼리) parameters

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

Trình duyệt (browser / 브라우저) tự encode truy vấn (query / 쿼리) parameter đúng hơn.

---

# Chương 51 — ES Modules

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015 trở đi:** Static `import`/`export` được chuẩn hóa ở ES2015. động (dynamic / 동적) `import()` và `import.meta` thuộc ES2020; import attributes và JSON-module hỗ trợ (support / 지원) được chuẩn hóa ở ES2025. mô-đun (module / 모듈) cú pháp (syntax / 문법) là ECMAScript, còn cách trình duyệt (browser / 브라우저)/nút (node / 노드)/bundler resolve và tải mô-đun (module / 모듈) là một lớp khác.

Mô-đun (module / 모듈) export:

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

Named exports thường dễ rename/refactor/tìm kiếm (search / 검색) trong codebase lớn. mô-đun (module / 모듈) có own phạm vi (scope / 범위), nên variable không tự trở thành toàn cục (global / 전역).

---

# Chương 52 — Pure functions và side effects

Pure hàm (function / 함수) cùng đầu vào (input / 입력) cho cùng đầu ra (output / 출력) và không sửa bên ngoài (external / 외부) trạng thái (state / 상태):

```js
function calculateTax(amount, rate) {
  return amount * rate;
}
```

Side tác động (effect / 효과) hàm (function / 함수):

```js
function saveUser(user) {
  localStorage.setItem(
    "user",
    JSON.stringify(user)
  );
}
```

Side tác động (effect / 효과) không xấu. UI ứng dụng (application / 애플리케이션) bắt buộc cần DOM, mạng (network / 네트워크), lưu trữ (storage / 저장소). Vấn đề là nếu nghiệp vụ (business / 비즈니스) calculations bị trộn với side effects, testing và lập luận (reasoning / 추론) khó hơn.

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — Functional cốt lõi (core / 핵심) / Imperative Shell

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

Mẫu (pattern / 패턴) này rất hữu ích khi sang React/WebSquare kiến trúc (architecture / 아키텍처).

---

# Chương 53 — Naming, readability và mã (code / 코드) style

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

Hàm (function / 함수) names nên thể hiện hành động (action / 동작)/lĩnh vực (domain / 도메인) intent:

```text
calculateTotal
validateOrder
loadUser
mapUserDto
renderUsers
```

Đừng viết comment mô tả lại cú pháp (syntax / 문법). Hãy comment các ràng buộc (constraints / 제약조건들), workaround hoặc nghiệp vụ (business / 비즈니스) reason.

---

# Chương 54 — Magic values và constants

Bad:

```js
if (retryCount >= 3) {
}
```

nếu `3` là chính sách (policy / 정책) có ý nghĩa.

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

Sau này TypeScript có thể derive literal union từ đối tượng (object / 객체) này.

---

# Chương 55 — Defensive programming

Kiểm tra hợp lệ (validation / 검증) có giá trị nhất ở boundaries.

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

Tuy nhiên không cần validate lặp lại ở mọi private helper nếu ranh giới (boundary / 경계) đã guarantee bất biến (invariant / 불변식). Defensive programming tốt không phải thêm `if` vô hạn; nó là đặt kiểm tra hợp lệ (validation / 검증) đúng nơi.

---

# Chương 56 — Debugging cơ bản bằng DevTools

Trình duyệt (browser / 브라우저) DevTools có các tab quan trọng: Console để xem logs/errors, mạng (network / 네트워크) để xem HTTP requests, Elements để xem DOM/CSS, Sources để breakpoint và step mã (code / 코드), ứng dụng (application / 애플리케이션) để xem lưu trữ (storage / 저장소)/bộ nhớ đệm (cache / 캐시), hiệu năng (performance / 성능) và bộ nhớ (memory / 메모리) để phân tích sâu hơn.

`debugger` statement:

```js
function calculate(value) {
  debugger;
  return value * 2;
}
```

Khi DevTools mở, mã (code / 코드) pause để bạn inspect cục bộ (local / 로컬) variables, ngăn xếp lời gọi (call stack / 호출 스택) và phạm vi (scope / 범위).

Một thói quen tốt là **gỡ lỗi (debug / 디버그) bằng bằng chứng (evidence / 증거)**, không sửa ngẫu nhiên. Đầu tiên reproduce, xác định tầng (layer / 계층), inspect inputs/outputs rồi mới đưa hypothesis.

---

# Chương 57 — Từ mã (code / 코드) chạy được đến mã (code / 코드) có cấu trúc

Một sự kiện (event / 이벤트) handler kiểu beginner thường gom mọi thứ:

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

Nó trộn DOM read, URL building, mạng (network / 네트워크), parsing, rendering và bảo mật (security / 보안) sink. Refactor từng responsibility:

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

Đây là bước đầu tiên của kiến trúc (architecture / 아키텍처) thinking: mỗi hàm (function / 함수) có trách nhiệm tương đối rõ.

---

# Chương 58 — ngôn ngữ (language / 언어) Idioms ở mức (level / 수준) Beginner

Một JavaScript nhà phát triển (developer / 개발자) đã qua Beginner nên thấy các idioms sau là tự nhiên. Guard clause giúp invalid cases thoát sớm. `const` dùng mặc định để giảm reassignment. `map` dành cho transformation, `filter` dành cho selection, `find` dành cho lookup first match. `??` dùng khi fallback chỉ cho nullish values. `?.` dùng khi relationship thật sự optional. Spread dùng cho shallow immutable cập nhật (update / 업데이트). Options đối tượng (object / 객체) dùng cho API có nhiều arguments. `try/catch/finally` quản lý success/thất bại (failure / 실패)/cleanup. ES Modules dùng để phân chia phụ thuộc (dependency / 의존성) thay vì toàn cục (global / 전역) không gian tên (namespace / 네임스페이스).

Điểm quan trọng là bạn không học idiom như câu thần chú; bạn hiểu vì sao nó làm intent rõ hơn.

---

# Chương 59 — Programming Patterns ở mức (level / 수준) Beginner

Ở mức (level / 수준) này, bạn đã thực tế dùng nhiều mẫu (pattern / 패턴) dù chưa gọi tên. **Guard Clause** giúp làm luồng (flow / 흐름) phẳng. **Options đối tượng (object / 객체)** giúp API dễ mở rộng. **Mapper** chuyển đối tượng (object / 객체) từ shape này sang shape khác. **Factory hàm (function / 함수)** tạo đối tượng (object / 객체) với construction quy tắc (rule / 규칙). **chiến lược (strategy / 전략) bằng hàm (function / 함수)** thay hành vi (behavior / 동작) dựa trên chính sách (policy / 정책). **Functional cốt lõi (core / 핵심) / Imperative Shell** tách calculation khỏi side effects. **vòng đời (lifecycle / 생명주기) Pair** giúp nhớ tài nguyên (resource / 자원) đã acquire thì phải bản phát hành (release / 릴리스). **Immutable cập nhật (update / 업데이트)** giảm mutation của trạng thái dùng chung (shared state / 공유 상태).

Hãy học mẫu (pattern / 패턴) từ bài toán (problem / 문제). Nếu một `if` đơn giản giải quyết đủ rõ, không cần chiến lược (strategy / 전략). Nếu đối tượng (object / 객체) construction chỉ là `{ name }`, không cần Factory tầng (layer / 계층). Seniority nằm ở lựa chọn đúng mức lớp trừu tượng (abstraction / 추상화).

---

# Chương 60 — mẫu thiết kế (design pattern / 디자인 패턴) Connections

JavaScript first-class functions làm chiến lược (strategy / 전략), Command, Observer và Decorator nhẹ hơn nhiều ngôn ngữ class-centric. sự kiện (event / 이벤트) listener là một dạng Observer-like relationship. hàm (function / 함수) registry là chiến lược (strategy / 전략)/Command-like dispatch. mô-đun (module / 모듈) API công khai (public API / 공개 API) có thể đóng vai trò Facade. Factory hàm (function / 함수) là Factory mẫu (pattern / 패턴) ở dạng nhẹ. Khi sang Intermediate, bạn sẽ thấy closure tạo private trạng thái (state / 상태), mô-đun (module / 모듈) mẫu (pattern / 패턴), reducer/trạng thái (state / 상태) mẫu (pattern / 패턴) và middleware/chuỗi (chain / 사슬) rõ hơn.

---

# Chương 61 — Anti-patterns cần bỏ từ sớm

Không đưa dùng chung (shared / 공유) mutable trạng thái (state / 상태) lên `window` chỉ để mọi nơi truy cập (access / 접근). Không dùng `innerHTML` cho untrusted dữ liệu (data / 데이터). Không dùng `var` cho mã (code / 코드) mới. Không dùng `map` khi chỉ cần side tác động (effect / 효과). Không swallow lỗi (error / 오류) không lý do. Không dùng `==` nếu nhóm (team / 팀) không chủ đích ngữ nghĩa (semantics / 의미론) coercion. Không deep-nest `if` nếu guard clauses rõ hơn. Không viết giant sự kiện (event / 이벤트) handler chứa DOM, mạng (network / 네트워크), lô-gic nghiệp vụ (business logic / 비즈니스 로직) và rendering cùng lúc. Không dùng `JSON.parse(JSON.stringify(...))` như universal deep clone. Không assume `fetch` 500 sẽ tự throw. Không assume timer 0ms chạy ngay.

---

# Chương 62 — Mini dự án (project / 프로젝트) 1: Todo danh sách (list / 목록)

Todo danh sách (list / 목록) nên có add, delete, toggle complete, filter, localStorage và kết xuất (render / 렌더링). Hãy giữ trạng thái (state / 상태) dưới dạng array objects, viết pure functions cho add/toggle/remove, viết lưu trữ (storage / 저장소) functions riêng và kết xuất (render / 렌더링) hàm (function / 함수) riêng. sự kiện (event / 이벤트) handlers chỉ đọc đầu vào (input / 입력) và gọi use-case functions. Đây là dự án (project / 프로젝트) rất tốt để luyện array/đối tượng (object / 객체)/tham chiếu (reference / 참조)/DOM/sự kiện (event / 이벤트)/lưu trữ (storage / 저장소).

---

# Chương 63 — Mini dự án (project / 프로젝트) 2: người dùng (user / 사용자) tìm kiếm (search / 검색)

Người dùng (user / 사용자) tìm kiếm (search / 검색) nên có từ khóa (keyword / 키워드) đầu vào (input / 입력), loading trạng thái (state / 상태), API fetch, lỗi (error / 오류) trạng thái (state / 상태) và kết quả (result / 결과) rendering. Beginner phiên bản (version / 버전) chỉ cần gọi tìm kiếm (search / 검색) khi submit/click. Intermediate phiên bản (version / 버전) sau này thêm debounce, AbortController và stale-result handling. dự án (project / 프로젝트) này luyện fetch, URL, Promise, async/await, try/catch và DOM rendering an toàn.

---

# Chương 64 — Mini dự án (project / 프로젝트) 3: Shopping Cart

Cart item có thể có `id`, `name`, `price`, `quantity`. Hãy viết `addItem`, `removeItem`, `changeQuantity`, `calculateSubtotal`, `calculateTotal`. Các calculation functions nên pure. UI handler chỉ dispatch intent. Đây là cầu nối (bridge / 브리지) tốt sang trạng thái (state / 상태) management và reducer ở Intermediate.

---

# Chương 65 — Exit Criteria trước khi sang Intermediate

Bạn nên tự giải thích được vì sao `const` đối tượng (object / 객체) vẫn mutate được, vì sao đối tượng (object / 객체) assignment bản sao (copy / 복사) tham chiếu (reference / 참조), vì sao spread chỉ shallow, vì sao `0 || 100` khác `0 ?? 100`, vì sao `fetch` cần check `response.ok`, vì sao `map` khác `forEach`, vì sao `setTimeout(..., 0)` không chạy ngay, vì sao `innerHTML` có XSS rủi ro (risk / 위험), vì sao listener cần cleanup, và vì sao lô-gic nghiệp vụ (business logic / 비즈니스 로직) không nên nằm hết trong DOM sự kiện (event / 이벤트) handler.

Bạn cũng nên tự viết được một tính năng (feature / 기능) nhỏ có đầu vào (input / 입력), kiểm tra hợp lệ (validation / 검증), pure lô-gic (logic / 논리), API/lưu trữ (storage / 저장소) và kết xuất (render / 렌더링) mà không cần bản sao (copy / 복사) nguyên mẫu từ tài liệu. Khi đã đạt mức này, bạn sẵn sàng sang Intermediate — nơi mục tiêu không còn là biết cú pháp mà là hiểu **ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론)** của JavaScript.

> **Bàn giao:** Sau **mẫu lập trình (programming pattern / 프로그래밍 패턴) — Functional cốt lõi (core / 핵심) / Imperative Shell**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [javascript intermediate](./javascript_intermediate.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
