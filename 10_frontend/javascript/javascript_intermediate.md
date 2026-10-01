# JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Thực thi (execution / 실행) ngữ cảnh (context / 맥락) không đồng nghĩa lexical phạm vi (scope / 범위)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Creation/initialization trước evaluation: nền tảng của hoisting** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Mục tiêu của phần này**: chuyển từ mức “biết dùng JavaScript” sang mức “hiểu vì sao JavaScript hoạt động như vậy”. Bạn sẽ học thực thi (execution / 실행) ngữ cảnh (context / 맥락), lexical môi trường (environment / 환경), closure, `this`, prototype, lớp (class / 클래스) internals, modules, Promise/vòng lặp sự kiện (event loop / 이벤트 루프), iterator/generator, functional composition, trạng thái (state / 상태) modeling, lỗi (error / 오류) kiến trúc (architecture / 아키텍처), API tầng (layer / 계층), testing và các programming/thiết kế (design / 설계) patterns quan trọng.
>
> Phần này giả định bạn đã hoàn thành Beginner và có thể viết hàm (function / 함수), đối tượng (object / 객체), array, DOM, fetch và async/await cơ bản.

---

<!-- VERSION-GUIDE-BEGIN -->
# Phiên bản (version / 버전) mindset ở mức (level / 수준) Intermediate: hiểu TC39 proposal tiến trình (process / 프로세스)

Ở Beginner, phiên bản (version / 버전) giúp bạn nhận ra cú pháp (syntax / 문법) thuộc thế hệ nào. Sang Intermediate, bạn cần hiểu thêm **tính năng (feature / 기능) đi vào JavaScript bằng cách nào**. TC39 phát triển các đề xuất mới theo nhiều stage. Stage 1 nghĩa ý tưởng đã bước vào quy trình nhưng còn có thể đổi lớn. Stage 2 cho thấy bài toán (problem / 문제)/solution direction đã rõ hơn. Stage 3 là candidate khá chín và thường là lúc engine vendors triển khai để lấy phản hồi (feedback / 피드백). Stage 4 là finished proposal: tính năng (feature / 기능) đã hoàn tất các yêu cầu chuẩn hóa và sẽ được đưa vào yearly snapshot tiếp theo phù hợp.

Điều này giải thích vì sao “trình duyệt (browser / 브라우저) đã hỗ trợ (support / 지원)” và “yearly ECMAScript edition đã publish” không luôn cùng thời điểm. Một trình duyệt (browser / 브라우저) có thể ship Stage-3/Stage-4 tính năng (feature / 기능) trước yearly snapshot. Ngược lại, một tính năng (feature / 기능) đã Stage 4 vẫn có thể không chạy trên WebView cũ. Vì vậy quy trình môi trường vận hành (production / 운영 환경) phải gồm hai câu hỏi tách biệt: **tính năng (feature / 기능) có final/stable chưa?** và **thời gian chạy (runtime / 런타임) mục tiêu (target / 대상) của tôi có hỗ trợ (support / 지원) chưa?**.

`ESNext` cũng phải được hiểu là nhãn động. Nó không có nghĩa ES2027 hay một phiên bản (version / 버전) cụ thể. Khi đọc một bài cũ nói “ESNext”, hãy tra tên proposal/tính năng (feature / 기능) hiện tại. cú pháp (syntax / 문법) proposal có thể đã đổi hoặc proposal có thể đã bị bỏ.

Ở Intermediate, bạn cũng sẽ gặp nhiều thứ phối hợp JavaScript với trình duyệt (browser / 브라우저) nhưng không thuộc ECMAScript yearly releases. `AbortController`, DOM vòng lặp sự kiện (event loop / 이벤트 루프) tích hợp (integration / 통합), rendering vòng đời (lifecycle / 생명주기) và `requestAnimationFrame` là Web APIs/host hành vi (behavior / 동작). Promise jobs, async functions, iterators, modules và lớp (class / 클래스) cú pháp (syntax / 문법) mới là ECMA-262 concerns. Việc phân biệt hai nhóm này giúp bạn không gán nhầm “ES phiên bản (version / 버전)” cho một nền tảng (platform / 플랫폼) API.

Tính đến lần cập nhật này, ECMAScript 2026 là yearly snapshot chính thức mới nhất. Những cơ chế nền như closure, `this`, prototype, descriptors và Promise resolution không trở nên lỗi thời chỉ vì yearly snapshot tăng; phiên bản (version / 버전) notes chủ yếu quan trọng ở nơi cú pháp (syntax / 문법)/API mới làm thay đổi tính tương thích (compatibility / 호환성) hoặc style mã (code / 코드).
<!-- VERSION-GUIDE-END -->

---

# Chương 1 — thực thi (execution / 실행) ngữ cảnh (context / 맥락) và ngăn xếp lời gọi (call stack / 호출 스택)

Khi JavaScript gọi một hàm (function / 함수), engine không chỉ “nhảy vào đoạn mã (code / 코드)”. Nó tạo một **thực thi (execution / 실행) ngữ cảnh (context / 맥락)**, có thể hiểu như môi trường chứa các binding cục bộ (local / 로컬), parameters, thông tin phạm vi (scope / 범위), `this` binding và tham chiếu (reference / 참조) tới outer lexical môi trường (environment / 환경).

```js
const globalValue = 10;

function add(a, b) {
  const result = a + b + globalValue;
  return result;
}

add(1, 2);
```

Khi tệp (file / 파일) được chạy, có toàn cục (global / 전역) thực thi (execution / 실행) ngữ cảnh (context / 맥락). Khi `add(1, 2)` được gọi, một hàm (function / 함수) thực thi (execution / 실행) ngữ cảnh (context / 맥락) mới được tạo với `a = 1`, `b = 2`, `result`, và outer môi trường (environment / 환경) trỏ về toàn cục (global / 전역) lexical môi trường (environment / 환경).

Thực thi (execution / 실행) contexts được quản lý bởi **ngăn xếp lời gọi (call stack / 호출 스택)**. Ví dụ:

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

Ngăn xếp lời gọi (call stack / 호출 스택) conceptually:

```text
a
↓
b
↓
c
```

Khi `c` xong, ngữ cảnh (context / 맥락) của `c` pop khỏi ngăn xếp (stack / 스택), thực thi (execution / 실행) quay lại `b`, rồi `a`.

Nếu recursion không dừng:

```js
function loop() {
  loop();
}

loop();
```

Ngăn xếp (stack / 스택) tăng liên tục tới `Maximum call stack size exceeded`.

## Thực thi (execution / 실행) ngữ cảnh (context / 맥락) không đồng nghĩa lexical phạm vi (scope / 범위)

Hai khái niệm này liên quan nhưng không nên trộn thành một. **Lexical phạm vi (scope / 범위)** mô tả mã (code / 코드) ở vị trí nào có thể nhìn thấy binding nào và được quyết định chủ yếu bởi cấu trúc nguồn (source / 소스). **thực thi (execution / 실행) ngữ cảnh (context / 맥락)** là trạng thái của một lần thực thi cụ thể. Một hàm (function / 함수) chỉ có một lexical relationship trong nguồn (source / 소스) nhưng có thể được gọi hàng nghìn lần, và mỗi lần gọi tạo thực thi (execution / 실행) ngữ cảnh (context / 맥락) riêng.

```js
function calculate(price, quantity) {
  const total = price * quantity;
  return total;
}

calculate(100, 2);
calculate(300, 4);
```

Hai lần gọi cùng dùng một hàm (function / 함수) body và cùng lexical môi trường (environment / 환경) ngoài, nhưng `price`, `quantity`, `total` của hai lần gọi không phải cùng một thực thi (execution / 실행) trạng thái (state / 상태). Đây là lý do recursion hoạt động: cùng một hàm (function / 함수) có thể xuất hiện nhiều lần trên ngăn xếp lời gọi (call stack / 호출 스택) với parameters/cục bộ (local / 로컬) bindings khác nhau.

```js
function factorial(n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}
```

Với `factorial(3)`, ngăn xếp (stack / 스택) có thể hình dung:

```text
factorial(3)
  ↓
factorial(2)
  ↓
factorial(1)
```

Mỗi frame giữ `n` riêng. Khi `factorial(1)` return, frame đó biến mất khỏi ngăn xếp (stack / 스택); kết quả được dùng để tiếp tục frame `factorial(2)`.

> **Chuyển mạch:** Execution context xác định lexical environment và bindings; creation/initialization giải thích hoisting trước evaluation. Call stack tiếp theo cho thấy các bindings đó tồn tại trong synchronous execution nào.

## Creation/initialization trước evaluation: nền tảng của hoisting

Một mô hình tư duy (mental model / 사고 모델) rất quan trọng là engine phải chuẩn bị môi trường (environment / 환경) và bindings trước khi thực thi lần lượt các statements. Vì thế “hoisting” không nên được hiểu là engine thật sự cắt một dòng mã (code / 코드) rồi di chuyển nó lên đầu tệp (file / 파일). Đúng hơn, declaration được xử lý trong quá trình khởi tạo môi trường (environment / 환경), nhưng **mỗi loại declaration được khởi tạo khác nhau**.

Hàm (function / 함수) declaration có hàm (function / 함수) giá trị (value / 값) sẵn sớm:

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

Vì vậy câu “`let` không hoist” là cách nói đơn giản nhưng không chính xác về mô hình tư duy (mental model / 사고 모델). Binding tồn tại trong lexical môi trường (environment / 환경), nhưng chưa thể truy cập (access / 접근) trước initialization.

> **Chuyển mạch:** Hoisting được quyết định trong creation phase; call stack chỉ chứa execution hiện tại, còn environment record mới giữ binding sống qua các scope.

## Ngăn xếp lời gọi (call stack / 호출 스택) chỉ chứa synchronous thực thi (execution / 실행) hiện tại

Khi một trình duyệt (browser / 브라우저) API như timer nhận callback, callback không nằm trên ngăn xếp lời gọi (call stack / 호출 스택) trong suốt thời gian chờ.

```js
function run() {
  setTimeout(() => {
    console.log("later");
  }, 1000);
}

run();
```

Sau khi `setTimeout()` đăng ký timer và `run()` return, frame `run` đã rời ngăn xếp (stack / 스택). Khi timer đủ điều kiện và vòng lặp sự kiện (event loop / 이벤트 루프) chọn tác vụ (task / 작업) tương ứng, **một lần gọi callback mới** mới được đẩy lên ngăn xếp (stack / 스택). Đây là điểm nối giữa ngăn xếp lời gọi (call stack / 호출 스택) và vòng lặp sự kiện (event loop / 이벤트 루프) mà Chương 23 sẽ đào sâu.

### Cách dấu vết (trace / 추적) thực thi (execution / 실행) thực tế

Khi mã (code / 코드) phức tạp, hãy dấu vết (trace / 추적) theo ba câu hỏi thay vì đọc bằng cảm giác:

```text
1. Context/function nào đang chạy trên stack?
2. Identifier này được resolve qua lexical environment nào?
3. Công việc async này đang chạy ngay hay chỉ được schedule cho tương lai?
```

Ba câu hỏi này giải quyết phần lớn nhầm lẫn về closure, `this`, Promise và timer.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Dấu vết ngăn xếp (stack trace / 스택 트레이스) trong lỗi (error / 오류) chính là dấu vết của ngăn xếp lời gọi (call stack / 호출 스택). Khi gỡ lỗi (debug / 디버그) async mã (code / 코드), ngăn xếp (stack / 스택) có thể phức tạp hơn vì continuation được schedule qua Promise/vòng lặp sự kiện (event loop / 이벤트 루프). Hiểu ngăn xếp lời gọi (call stack / 호출 스택) là nền tảng cho mọi phần thời gian chạy (runtime / 런타임) sau này.

---

# Chương 2 — Lexical môi trường (environment / 환경) và phạm vi (scope / 범위) chuỗi (chain / 사슬)

JavaScript dùng **lexical scoping**. “Lexical” nghĩa là relationship giữa scopes chủ yếu được quyết định bởi vị trí mã (code / 코드) được viết, không phải nơi hàm (function / 함수) được gọi.

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

Đầu ra (output / 출력) là `outer`, không phải `run`. `inner` được định nghĩa trong phạm vi (scope / 범위) của `outer`, nên khi tìm `value`, engine đi theo phạm vi (scope / 범위) chuỗi (chain / 사슬) lexical: hiện tại (current / 현재) phạm vi (scope / 범위) → outer phạm vi (scope / 범위) → toàn cục (global / 전역).

Phạm vi (scope / 범위) chuỗi (chain / 사슬) có thể hình dung:

```text
inner scope
↓
outer scope
↓
global scope
```

Nếu cùng tên variable ở inner phạm vi (scope / 범위), nó **shadow** outer variable:

```js
const value = 1;

function run() {
  const value = 2;
  console.log(value); // 2
}
```

Shadowing không sai, nhưng quá nhiều biến cùng tên trong nested scopes làm cognitive tải (load / 로드) cao.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Môi trường (environment / 환경) là nơi binding sống, không phải chỉ là một đối tượng (object / 객체) thường** tiếp nhận điểm tựa từ **Ngăn xếp lời gọi (call stack / 호출 스택) chỉ chứa synchronous thực thi (execution / 실행) hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Identifier resolution là một quá trình tìm từ trong ra ngoài** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường (environment / 환경) là nơi binding sống, không phải chỉ là một đối tượng (object / 객체) thường

Khi học phạm vi (scope / 범위), nhiều người hình dung mỗi phạm vi (scope / 범위) là một JavaScript đối tượng (object / 객체) như `{ name: value }`. mô hình tư duy (mental model / 사고 모델) đó chỉ đúng rất sơ bộ. Specification dùng **môi trường (environment / 환경) Records** để mô tả bindings. Điều này quan trọng vì binding có hành vi (behavior / 동작) riêng: TDZ, immutable `const`, hàm (function / 함수) parameter bindings, mô-đun (module / 모듈) imports là live bindings, và toàn cục (global / 전역) `var`/toàn cục (global / 전역) lexical declarations không hoàn toàn giống nhau.

Bạn không thể làm:

```js
console.log(currentLexicalEnvironment);
```

vì lexical môi trường (environment / 환경) là khái niệm thời gian chạy (runtime / 런타임)/spec, không phải ordinary đối tượng (object / 객체) được expose trực tiếp.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Identifier resolution là một quá trình tìm từ trong ra ngoài** tiếp nhận điểm tựa từ **Môi trường (environment / 환경) là nơi binding sống, không phải chỉ là một đối tượng (object / 객체) thường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khối (block / 블록) phạm vi (scope / 범위) và per-iteration binding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu identifier không tìm thấy trong toàn chuỗi (chain / 사슬), đọc nó gây `ReferenceError`.

Đây khác với đọc thuộc tính (property / 속성) không tồn tại:

```js
const user = {};

console.log(user.name); // undefined
console.log(name);      // ReferenceError nếu không có binding name
```

Một bên là **thuộc tính (property / 속성) lookup trên đối tượng (object / 객체)**, một bên là **identifier resolution qua lexical environments**. Phân biệt này rất quan trọng khi gỡ lỗi (debug / 디버그).

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Khối (block / 블록) phạm vi (scope / 범위) và per-iteration binding** tiếp nhận điểm tựa từ **Identifier resolution là một quá trình tìm từ trong ra ngoài** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Toàn cục (global / 전역) phạm vi (scope / 범위) không đơn giản là window** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khối (block / 블록) phạm vi (scope / 범위) và per-iteration binding

`let`/`const` có khối (block / 블록) phạm vi (scope / 범위):

```js
if (true) {
  const token = "abc";
}

// token không tồn tại ở đây
```

Trong `for (let ...)`, JavaScript còn tạo ngữ nghĩa (semantics / 의미론) phù hợp để mỗi iteration có binding riêng cho closure:

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

Trước ES2015, legacy mã (code / 코드) thường dùng IIFE để tạo binding riêng từng iteration:

```js
for (var i = 0; i < 3; i += 1) {
  (function (current) {
    callbacks.push(function () {
      return current;
    });
  })(i);
}
```

Đây là ví dụ điển hình cho **hiện đại (modern / 현대적) cú pháp (syntax / 문법) xuất hiện để diễn đạt intent mà legacy JavaScript phải mô phỏng bằng mẫu (pattern / 패턴)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Toàn cục (global / 전역) phạm vi (scope / 범위) không đơn giản là window** tiếp nhận điểm tựa từ **Khối (block / 블록) phạm vi (scope / 범위) và per-iteration binding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closure giữ binding, không phải snapshot giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Toàn cục (global / 전역) phạm vi (scope / 범위) không đơn giản là `window`

Trong trình duyệt (browser / 브라우저) classic script, một số toàn cục (global / 전역) declarations có relationship với toàn cục (global / 전역) đối tượng (object / 객체), nhưng lexical declarations như `let`/`const` không đơn giản trở thành properties của `window`.

```js
var legacyGlobal = 1;
let lexicalGlobal = 2;
```

Tùy ngữ cảnh (context / 맥락) classic script/mô-đun (module / 모듈), ngữ nghĩa (semantics / 의미론) khác nhau; đặc biệt ES modules có mô-đun (module / 모듈) phạm vi (scope / 범위) riêng. Vì vậy mã (code / 코드) hiện đại không nên dựa vào việc “khai báo top-level rồi chắc chắn có `window.xxx`”. Nếu cần toàn cục (global / 전역) tích hợp (integration / 통합), expose tường minh (explicit / 명시적) API.

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — lexical encapsulation

Helper chỉ dùng bên trong một use trường hợp (case / 사례) có thể được giữ trong phạm vi (scope / 범위) đó thay vì export/toàn cục (global / 전역):

```js
function buildReport(rows) {
  function formatRow(row) {
    return `${row.id}: ${row.name}`;
  }

  return rows.map(formatRow);
}
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Lexical phạm vi (scope / 범위) làm nguồn (source / 소스) cấu trúc (structure / 구조) trở thành một phần của phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조). `this` là một điểm khác biệt lớn: normal hàm (function / 함수) `this` thường phụ thuộc call-site chứ không đi theo lexical phạm vi (scope / 범위); arrow hàm (function / 함수) thì lexical `this`.

---

# Chương 3 — Closure: hàm (function / 함수) nhớ môi trường (environment / 환경) nơi nó được tạo

Closure là một trong những concept cốt lõi nhất của JavaScript. Một hàm (function / 함수) có thể tiếp tục truy cập (access / 접근) variables trong lexical môi trường (environment / 환경) nơi nó được tạo, kể cả khi outer hàm (function / 함수) đã return.

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

`createCounter()` đã kết thúc, nhưng returned hàm (function / 함수) vẫn giữ truy cập (access / 접근) tới binding `count`. Đây là closure.

Closure không đơn giản là “hàm (function / 함수) nằm trong hàm (function / 함수)”. Điểm cốt lõi là hàm (function / 함수) giữ lexical truy cập (access / 접근) tới variables mà nó cần.

Closure cho phép private trạng thái (state / 상태):

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

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Closure giữ binding, không phải snapshot giá trị (value / 값)** tiếp nhận điểm tựa từ **Toàn cục (global / 전역) phạm vi (scope / 범위) không đơn giản là window** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mỗi factory call có một private environment khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closure giữ binding, không phải snapshot giá trị (value / 값)

Đây là một distinction rất quan trọng. Closure thường không “bản sao (copy / 복사) giá trị (value / 값) tại thời điểm hàm (function / 함수) được tạo”; nó giữ khả năng truy cập **binding**.

```js
let status = "idle";

function readStatus() {
  return status;
}

status = "loading";

console.log(readStatus()); // "loading"
```

Nếu closure chỉ snapshot `"idle"`, đầu ra (output / 출력) đã là `"idle"`. Nhưng nó đọc binding hiện tại.

Điều này giải thích cả sức mạnh lẫn bug của closure. Một callback có thể thấy trạng thái (state / 상태) mới nếu binding bị mutate; nhưng một hệ thống kết xuất (render / 렌더링) tạo **binding mới cho mỗi kết xuất (render / 렌더링)/lời gọi (call / 호출)** có thể khiến callback giữ binding cũ, tạo stale closure.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Mỗi factory call có một private environment khác nhau** tiếp nhận điểm tựa từ **Closure giữ binding, không phải snapshot giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closure và vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mỗi factory call có một private environment khác nhau
Phần này nối mạch bài học với “Mỗi factory call có một private environment khác nhau”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`a` và `b` không share `count`, vì chúng được tạo từ hai lần gọi khác nhau, mỗi lần có môi trường (environment / 환경) riêng. Đây là nền tảng của factory/mô-đun (module / 모듈) patterns dựa closure.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Mỗi factory call có một private environment khác nhau** xác định đầu vào; **Closure và vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Stale closure: timing + vòng đời (lifecycle / 생명주기), không phải closure “hỏng”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closure và vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리)

Nếu closure reachable, những bindings/đối tượng (object / 객체) mà closure thật sự cần cũng có thể tiếp tục reachable.

```js
function createHandler(bigData) {
  return function () {
    return bigData.id;
  };
}
```

Nếu handler được gắn vào một toàn cục (global / 전역) listener và không bao giờ remove, `bigData` có thể sống lâu hơn nghiệp vụ (business / 비즈니스) vòng đời (lifecycle / 생명주기) dự kiến.

Nhưng câu “closure gây bộ nhớ (memory / 메모리) leak” là sai. Closure chỉ giữ dữ liệu (data / 데이터) khi còn đường reachability. Vấn đề thực tế thường là **tài nguyên (resource / 자원) đơn vị sở hữu (owner / 오너) không cleanup callback/subscription**.

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

Ở đây closure có thời gian tồn tại (lifetime / 수명) tường minh (explicit / 명시적) qua cleanup hàm (function / 함수).

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Closure và vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리)** xác định đầu vào; **Stale closure: timing + vòng đời (lifecycle / 생명주기), không phải closure “hỏng”** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Bốn binding rules thực dụng cho normal hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stale closure: timing + vòng đời (lifecycle / 생명주기), không phải closure “hỏng”

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

`logOld` đúng khi in `"old"`; nó giữ môi trường (environment / 환경) của lần gọi cũ. khung phần mềm (framework / 프레임워크) kết xuất (render / 렌더링) các hệ thống (systems / 시스템들) có thể tạo tình huống tương tự: callback cũ sống sau khi UI đã có trạng thái (state / 상태) mới. Cách giải quyết không phải “tránh closure”, mà là thiết kế phụ thuộc (dependency / 의존성)/vòng đời (lifecycle / 생명주기) đúng.

### Closure và bộ nhớ (memory / 메모리)

Nếu closure giữ tham chiếu (reference / 참조) tới đối tượng (object / 객체) lớn, đối tượng (object / 객체) đó tiếp tục reachable:

```js
function createHandler(bigData) {
  return function () {
    return bigData.id;
  };
}
```

Closure không “gây leak” tự động. Vấn đề xảy ra khi vòng đời (lifecycle / 생명주기) của closure dài hơn vòng đời (lifecycle / 생명주기) mà bạn tưởng, làm dữ liệu (data / 데이터)/tài nguyên (resource / 자원) tiếp tục sống.

### Closure và vòng lặp (loop / 루프)

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

### Mẫu thiết kế (design pattern / 디자인 패턴) connections

Closure là nền tảng cho mô-đun (module / 모듈) mẫu (pattern / 패턴), Factory với private trạng thái (state / 상태), memoization, decorators, currying, hooks và middleware wrappers.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Stale closure là lỗi rất phổ biến trong React-like các hệ thống (systems / 시스템들): closure giữ giá trị (value / 값) của một kết xuất (render / 렌더링)/vòng đời (lifecycle / 생명주기) trước đó. hệ kiểu (type system / 타입 시스템) không tự cứu bạn khỏi timing ngữ nghĩa (semantics / 의미론) này.

---

# Chương 4 — hàm (function / 함수) là first-class giá trị (value / 값) và Higher-Order hàm (function / 함수)

Hàm (function / 함수) có thể được truyền, return, lưu trong đối tượng (object / 객체)/array. Điều này làm JavaScript cực kỳ linh hoạt.

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

`withLogging` là Higher-Order hàm (function / 함수) vì nó nhận hàm (function / 함수) và trả hàm (function / 함수).

### Programming pattern — decorator-like wrapper
Phần này nối mạch bài học với “Programming pattern — decorator-like wrapper”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Mẫu (pattern / 패턴) này xuất hiện trong logging, thử lại (retry / 재시도), auth wrapper, metrics và middleware.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

JavaScript không cần lớp (class / 클래스) cho mọi mẫu thiết kế (design pattern / 디자인 패턴). chiến lược (strategy / 전략), Command, Decorator, Observer và Middleware rất tự nhiên với first-class functions. Nhưng wrapper nesting quá sâu có thể làm dấu vết ngăn xếp (stack trace / 스택 트레이스) khó đọc; đặt tên lớp trừu tượng (abstraction / 추상화) rõ và đừng wrap chỉ để “đúng mẫu (pattern / 패턴)”.

---

# Chương 5 — `this`: hiểu theo call-site, không theo nơi hàm (function / 함수) được viết

`this` là một trong những chủ đề gây nhiều bug nhất. Với normal hàm (function / 함수), `this` chủ yếu được xác định bởi **cách hàm (function / 함수) được gọi**.

Phương thức (method / 메서드) lời gọi (call / 호출):

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

Detached phương thức (method / 메서드):

```js
const greet = user.greet;

greet();
```

Hàm (function / 함수) không còn được gọi qua `user`, nên `this` không còn tự là `user`.

Trong strict chế độ (mode / 모드), plain hàm (function / 함수) lời gọi (call / 호출) thường có `this === undefined`.

Constructor lời gọi (call / 호출):

```js
function User(name) {
  this.name = name;
}

const user = new User("Kim");
```

`new` tạo đối tượng (object / 객체) mới và bind `this` vào đối tượng (object / 객체) đó trong quá trình constructor chạy.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Stale closure: timing + vòng đời (lifecycle / 생명주기), không phải closure “hỏng”** xác định đầu vào; **Bốn binding rules thực dụng cho normal hàm (function / 함수)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Thuộc tính (property / 속성) lookup là chuỗi (chain / 사슬) traversal, không phải bản sao (copy / 복사) phương thức (method / 메서드) vào từng instance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bốn binding rules thực dụng cho normal hàm (function / 함수)

Khi nhìn một normal hàm (function / 함수), hãy xác định `this` bằng lời gọi (call / 호출) expression chứ không nhìn nơi hàm (function / 함수) được khai báo. Một mô hình tư duy (mental model / 사고 모델) thực dụng là:

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

Arrow hàm (function / 함수) là exception lớn vì không tạo own động (dynamic / 동적) `this`; nó dùng lexical `this` của surrounding ngữ cảnh (context / 맥락).

### Implicit receiver là expression ngay trước dấu `.`/`[]`
Phần này nối mạch bài học với “Implicit receiver là expression ngay trước dấu `.`/`[]`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

receiver vẫn là đơn vị sở hữu (owner / 오너) đối tượng (object / 객체).

### Detached method làm mất receiver
Phần này nối mạch bài học với “Detached method làm mất receiver”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
const show = account.owner.show;
show();
```

Điều bị mất không phải “phương thức (method / 메서드) thuộc lớp (class / 클래스)”, mà là **tham chiếu (reference / 참조)/lời gọi (call / 호출) form chứa receiver**. Vì vậy callback API rất hay làm lộ bug này:

```js
button.addEventListener("click", account.owner.show);
```

Trình duyệt (browser / 브라우저) gọi callback theo event-listener ngữ nghĩa (semantics / 의미론), không phải bằng `account.owner.show()`. Nếu phương thức (method / 메서드) thật sự cần instance receiver, hãy wrap hoặc bind có chủ đích và giữ tham chiếu (reference / 참조) cleanup.

```js
const handleClick = account.owner.show.bind(account.owner);
button.addEventListener("click", handleClick);
```

### `this` và lexical variables là hai cơ chế khác nhau
Phần này nối mạch bài học với “`this` và lexical variables là hai cơ chế khác nhau”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`name` được resolve qua lexical phạm vi (scope / 범위). `this.name` bắt đầu từ thời gian chạy (runtime / 런타임) receiver rồi thuộc tính (property / 속성) lookup. Nếu trộn hai mô hình tư duy (mental models / 사고 모델들), `this` sẽ luôn cảm giác “bí ẩn”.

### Class không thay đổi quy tắc cốt lõi của detached method
Phần này nối mạch bài học với “Class không thay đổi quy tắc cốt lõi của detached method”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

`greet()` vẫn mất receiver. lớp (class / 클래스) cú pháp (syntax / 문법) không tự auto-bind methods như một số khung phần mềm (framework / 프레임워크)/ngôn ngữ (language / 언어) khác.

### Cấp cao (senior / 시니어) quy tắc (rule / 규칙)

Đừng hỏi “hàm (function / 함수) này thuộc đối tượng (object / 객체) nào?”. Hãy nhìn lời gọi (call / 호출) expression. `obj.method()` khác `const fn = obj.method; fn()`.

---

# Chương 6 — `call`, `apply`, `bind`

`call` gọi hàm (function / 함수) ngay với tường minh (explicit / 명시적) `this`:

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

`bind` tạo hàm (function / 함수) mới, chưa chạy ngay:

```js
const boundGreet = greet.bind(user);

boundGreet("Hello");
```

Một detail quan trọng: `bind()` tạo hàm (function / 함수) định danh (identity / 식별자) mới. Vì vậy:

```js
element.addEventListener(
  "click",
  handler.bind(obj)
);
```

sau này bạn không thể remove listener bằng một `handler.bind(obj)` khác, vì đó là hàm (function / 함수) mới. Hãy giữ tham chiếu (reference / 참조):

```js
const boundHandler = handler.bind(obj);

element.addEventListener(
  "click",
  boundHandler
);
```

### Partial application
Phần này nối mạch bài học với “Partial application”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

# Chương 7 — Arrow hàm (function / 함수) ngữ nghĩa (semantics / 의미론)

Arrow hàm (function / 함수) không chỉ là hàm (function / 함수) cú pháp (syntax / 문법) ngắn. Nó **không có own `this`**; nó lấy `this` lexical từ surrounding ngữ cảnh (context / 맥락).

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

Arrow callback dùng `this` của `delayedGreeting` phương thức (method / 메서드) lời gọi (call / 호출).

Nếu dùng arrow làm đối tượng (object / 객체) phương thức (method / 메서드) khi cần động (dynamic / 동적) `this`:

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

### Lối viết quen dùng của ngôn ngữ (language idiom / 언어 관용구)

Arrow rất tốt cho callback transformations:

```js
users.map(
  (user) => user.name
);
```

Phương thức (method / 메서드) shorthand tốt khi cần instance/đối tượng (object / 객체) `this`:

```js
const user = {
  greet() {
    return this.name;
  }
};
```

---

# Chương 8 — đối tượng (object / 객체) thuộc tính (property / 속성) lookup và own/inherited thuộc tính (property / 속성)

Khi bạn đọc:

```js
user.name
```

engine tìm own thuộc tính (property / 속성) `name`. Nếu không có, nó có thể đi lên prototype chuỗi (chain / 사슬).

Own thuộc tính (property / 속성) check:

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

Đây là lý do `for...in` có thể thấy inherited enumerable properties, và tại sao arbitrary đối tượng (object / 객체) dictionaries có bảo mật (security / 보안) concerns như prototype pollution.

---

# Chương 9 — Prototype và prototype chuỗi (chain / 사슬)

JavaScript là prototype-based ngôn ngữ (language / 언어). Mỗi ordinary đối tượng (object / 객체) có nội bộ (internal / 내부) prototype link tới đối tượng (object / 객체) khác hoặc `null`.

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

Các methods như `map`, `filter`, `push` được tìm thông qua prototype chuỗi (chain / 사슬).

Constructor hàm (function / 함수):

```js
function User(name) {
  this.name = name;
}

User.prototype.greet = function () {
  return `Hello ${this.name}`;
};

const user = new User("Kim");
```

Chuỗi (chain / 사슬):

```text
user
↓
User.prototype
↓
Object.prototype
↓
null
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Bốn binding rules thực dụng cho normal hàm (function / 함수)** xác định đầu vào; **Thuộc tính (property / 속성) lookup là chuỗi (chain / 사슬) traversal, không phải bản sao (copy / 복사) phương thức (method / 메서드) vào từng instance** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Shadowing inherited property** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thuộc tính (property / 속성) lookup là chuỗi (chain / 사슬) traversal, không phải bản sao (copy / 복사) phương thức (method / 메서드) vào từng instance

Với:

```js
const user = new User("Kim");
user.greet();
```

`user` thường không có own thuộc tính (property / 속성) `greet`. Engine tìm:

```text
user
↓ no own greet
User.prototype
↓ found greet
```

Sau đó hàm (function / 함수) được gọi với receiver `user`, nên bên trong phương thức (method / 메서드) `this` vẫn là `user`, **không phải `User.prototype`**. Đây là chỗ `this` và prototype chuỗi (chain / 사슬) giao nhau: prototype quyết định **tìm hàm (function / 함수) ở đâu**; call-site quyết định **receiver là ai**.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Thuộc tính (property / 속성) lookup là chuỗi (chain / 사슬) traversal, không phải bản sao (copy / 복사) phương thức (method / 메서드) vào từng instance** xác định đầu vào; **Shadowing inherited property** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **instanceof kiểm tra prototype relationship** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Shadowing inherited property
Phần này nối mạch bài học với “Shadowing inherited property”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Assignment thường tạo own thuộc tính (property / 속성) trên receiver thay vì sửa inherited dữ liệu (data / 데이터) thuộc tính (property / 속성) ở prototype. Khi gỡ lỗi (debug / 디버그) “tại sao đối tượng (object / 객체) A đổi mà prototype không đổi”, hãy kiểm tra:

```js
Object.hasOwn(account, "role");
Object.getPrototypeOf(account);
```

Accessor descriptors có thể làm assignment ngữ nghĩa (semantics / 의미론) phức tạp hơn, vì inherited setter có thể được gọi. Chương thuộc tính (property / 속성) Descriptors giải thích cơ chế đó.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **instanceof kiểm tra prototype relationship** tiếp nhận điểm tựa từ **Shadowing inherited property** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prototype mutation là global-ish behavior change cho descendants** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `instanceof` kiểm tra prototype relationship
Phần này nối mạch bài học với “`instanceof` kiểm tra prototype relationship”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
user instanceof User;
```

Ở mental-model mức (level / 수준), `instanceof` kiểm tra liệu đối tượng (object / 객체) được tham chiếu bởi `User.prototype` có xuất hiện trên prototype chuỗi (chain / 사슬) của `user` hay không. Nó không kiểm tra “shape đối tượng (object / 객체) có giống người dùng (user / 사용자) không”.

Vì thế prototype mutation có thể thay đổi kết quả (result / 결과), và cross-realm objects có thể làm `instanceof Array`/`instanceof Error` không hoạt động như bạn kỳ vọng. Với arrays, `Array.isArray()` thường robust hơn cross-realm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Prototype mutation là global-ish behavior change cho descendants** tiếp nhận điểm tựa từ **instanceof kiểm tra prototype relationship** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Class syntax không xóa prototype model** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prototype mutation là global-ish behavior change cho descendants
Phần này nối mạch bài học với “Prototype mutation là global-ish behavior change cho descendants”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
User.prototype.greet = function () {
  return "changed";
};
```

Các instances đang dùng prototype đó có thể thấy phương thức (method / 메서드) mới ngay vì lookup xảy ra qua chuỗi (chain / 사슬). Đây là sức mạnh của prototype mô hình (model / 모델) nhưng cũng là lý do patch built-in prototypes trong ứng dụng (application / 애플리케이션) mã (code / 코드) nguy hiểm:

```js
Array.prototype.last = function () {
  return this[this.length - 1];
};
```

Bạn đã thay hành vi (behavior / 동작) của mọi array trong realm và có nguy cơ xung đột (conflict / 충돌) với thư viện (library / 라이브러리)/tiêu chuẩn (standard / 표준) tương lai.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Class syntax không xóa prototype model** tiếp nhận điểm tựa từ **Prototype mutation là global-ish behavior change cho descendants** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Settled không đồng nghĩa fulfilled** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Class syntax không xóa prototype model
Phần này nối mạch bài học với “Class syntax không xóa prototype model”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
class User {
  greet() {
    return this.name;
  }
}
```

Phương thức (method / 메서드) `greet` vẫn nằm trên `User.prototype`. `class` chủ yếu cung cấp cú pháp (syntax / 문법)/ngữ nghĩa (semantics / 의미론) rõ hơn cho constructor, inheritance, methods, private fields..., nhưng lookup mô hình (model / 모델) vẫn là prototype-based.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Prototype kiến thức (knowledge / 지식) giúp gỡ lỗi (debug / 디버그) phương thức (method / 메서드) lookup, `instanceof`, inheritance và bảo mật (security / 보안). Không mutate built-in prototype trong ứng dụng (application / 애플리케이션) mã (code / 코드) như `Array.prototype.myMethod = ...` vì có thể gây xung đột (conflict / 충돌) và hidden toàn cục (global / 전역) effects.

---

# Chương 10 — `new` và constructor hàm (function / 함수)

`new User("Kim")` conceptually làm bốn việc: tạo đối tượng (object / 객체) mới, link prototype của đối tượng (object / 객체) tới `User.prototype`, gọi `User` với `this` là đối tượng (object / 객체) mới, rồi return đối tượng (object / 객체) đó trừ một số edge cases khi constructor return đối tượng (object / 객체) tường minh (explicit / 명시적).

Đây là lý do methods nên nằm trên prototype thay vì tạo lại mỗi instance trong legacy constructor style.

```js
function User(name) {
  this.name = name;
}

User.prototype.greet = function () {
  return this.name;
};
```

Hiện đại (modern / 현대적) mã (code / 코드) thường dùng lớp (class / 클래스) cú pháp (syntax / 문법) cho readability, nhưng lớp (class / 클래스) vẫn dựa trên prototype machinery bên dưới.

---

# Chương 11 — `class`, instance fields, static và private fields

> **phiên bản (version / 버전) ghi chú (note / 노트):** lớp (class / 클래스) declarations/expressions và `extends` được chuẩn hóa ở ES2015. công khai (public / 공개)/private instance fields, private methods/accessors, static fields và static blocks được chuẩn hóa ở ES2022. Vì vậy một thời gian chạy (runtime / 런타임) “hỗ trợ (support / 지원) lớp (class / 클래스)” chưa chắc hỗ trợ (support / 지원) toàn bộ hiện đại (modern / 현대적) lớp (class / 클래스) cú pháp (syntax / 문법).

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

Phương thức (method / 메서드) vẫn nằm trên `User.prototype`:

```js
user.greet === User.prototype.greet;
```

Instance trường dữ liệu (field / 필드):

```js
class User {
  active = true;
}
```

Static phương thức (method / 메서드) thuộc lớp (class / 클래스), không thuộc instance:

```js
class User {
  static createGuest() {
    return new User("Guest");
  }
}
```

Private trường dữ liệu (field / 필드) runtime-level:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Đừng dùng lớp (class / 클래스) chỉ vì quen Java. lớp (class / 클래스) phù hợp khi lớp trừu tượng (abstraction / 추상화) có định danh (identity / 식별자), trạng thái (state / 상태), vòng đời (lifecycle / 생명주기) hoặc polymorphic hành vi (behavior / 동작) rõ. Stateless utility thường đơn giản hơn bằng hàm (function / 함수)/mô-đun (module / 모듈).

---

# Chương 12 — Inheritance và composition over inheritance
Phần này nối mạch bài học với “Chương 12 — Inheritance và composition over inheritance”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Inheritance hữu ích khi subtype relationship thật sự là “is-a”. Nhưng deep inheritance hierarchy làm hành vi (behavior / 동작) bị phân tán qua nhiều parent classes.

Composition thường rõ hơn:

```js
function calculatePrice(
  price,
  discountStrategy
) {
  return discountStrategy(price);
}
```

Thay vì tạo `VipUser extends DiscountUser extends UserBase...` chỉ để thay discount hành vi (behavior / 동작).

### Mẫu thiết kế (design pattern / 디자인 패턴) liên kết (connection / 연결)

Composition đi tự nhiên với chiến lược (strategy / 전략), Adapter, Decorator và phụ thuộc (dependency / 의존성) Injection.

---

# Chương 13 — thuộc tính (property / 속성) descriptors

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES5 nền tảng:** `Object.defineProperty()` và descriptor mô hình (model / 모델) là một phần quan trọng của ES5. ES2017 bổ sung `Object.getOwnPropertyDescriptors()`. Cơ chế này rất cũ nhưng vẫn nằm dưới nhiều khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) abstractions hiện đại.

Thuộc tính (property / 속성) không chỉ có key/giá trị (value / 값). dữ liệu (data / 데이터) thuộc tính (property / 속성) còn có siêu dữ liệu (metadata / 메타데이터): `writable`, `enumerable`, `configurable`.

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

Descriptors quan trọng khi đọc khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) internals và hiểu freeze/seal. ứng dụng (application / 애플리케이션) mã (code / 코드) thường không cần dùng `defineProperty` thường xuyên.

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

Caller đọc như thuộc tính (property / 속성):

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Getter cú pháp (syntax / 문법) nhìn như thuộc tính (property / 속성) read, nên getter expensive, mạng (network / 네트워크) lời gọi (call / 호출) hoặc side tác động (effect / 효과) nặng là surprising API thiết kế (design / 설계). Nếu thao tác (operation / 연산) có chi phí (cost / 비용)/side tác động (effect / 효과) đáng kể, phương thức (method / 메서드) rõ hơn.

---

# Chương 15 — `Object.create`, `Object.assign`, freeze/seal

> **phiên bản (version / 버전) ghi chú (note / 노트):** `Object.create()`, `freeze()`, `seal()` và descriptor-oriented controls thuộc thế hệ ES5. `Object.assign()` thuộc ES2015. đối tượng (object / 객체) spread `{...obj}` được chuẩn hóa sau ở ES2018 và không nên được coi là hoàn toàn đồng nghĩa với `Object.assign()` trong mọi trường hợp biên (edge case / 경계 사례).

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

Đối tượng (object / 객체) không có `Object.prototype`, useful cho một số dictionary/bảo mật (security / 보안) cases, nhưng `Map` thường ergonomic hơn.

`Object.assign(target, source)` mutate mục tiêu (target / 대상). Spread thường rõ hơn cho shallow bản sao (copy / 복사).

`Object.preventExtensions` ngăn add thuộc tính (property / 속성) mới. `Object.seal` thêm non-configurable. `Object.freeze` thêm non-writable dữ liệu (data / 데이터) properties. Nhưng freeze là shallow.

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

# Chương 16 — Symbol và giao thức (protocol / 프로토콜) hooks

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** `Symbol` và well-known symbols như `Symbol.iterator` được đưa vào ES2015. Chúng mở đường cho standardized ngôn ngữ (language / 언어) protocols thay vì chỉ dựa vào naming convention.

`Symbol()` tạo unique thành phần nguyên thủy (primitive / 기본 요소).

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

Well-known symbols như `Symbol.iterator` là hooks vào ngôn ngữ (language / 언어) protocols. Bạn sẽ dùng nó khi học iterable.

`Symbol.toPrimitive` cho phép đối tượng (object / 객체) customize conversion.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Symbol không phải privacy cơ chế (mechanism / 메커니즘). Symbol properties vẫn inspect được bằng `Object.getOwnPropertySymbols`.

---

# Chương 17 — Map/Set ở mức Intermediate

> **phiên bản (version / 버전) ghi chú (note / 노트):** Map/Set xuất hiện ở ES2015. ES2025 bổ sung các Set operations chuẩn như `union`, `intersection`, `difference`, `symmetricDifference`, `isSubsetOf`, `isSupersetOf`, `isDisjointFrom`. Hãy kiểm tra mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) trước khi refactor legacy helper sang API mới.

Map đặc biệt hữu ích để tạo chỉ mục (index / 인덱스) cho repeated lookup.

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

Nếu trước đó bạn gọi `.find()` hàng nghìn lần trên array lớn, chỉ mục (index / 인덱스) Map có thể giảm độ phức tạp (complexity / 복잡도) từ repeated tuyến tính (linear / 선형) tìm kiếm (search / 검색) xuống gần constant-time lookup average, đổi lại dùng thêm bộ nhớ (memory / 메모리) và cần giữ chỉ mục (index / 인덱스) đồng bộ.

Set useful cho membership và uniqueness.

```js
const permissions = new Set([
  "READ",
  "WRITE"
]);

permissions.has("READ");
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Chọn cấu trúc dữ liệu (data structure / 자료구조) theo truy cập (access / 접근) mẫu (pattern / 패턴). Đừng dùng Map vì “cấp cao (senior / 시니어) hơn đối tượng (object / 객체)”.

---

# Chương 18 — WeakMap và WeakSet

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015:** WeakMap/WeakSet thuộc ES2015. `WeakRef` và `FinalizationRegistry` là nhóm khác, đến ở ES2021 và có ngữ nghĩa (semantics / 의미론) GC tinh tế hơn nên được để ở mức (level / 수준) cấp cao (senior / 시니어).

WeakMap keys là đối tượng (object / 객체)/non-registered symbol trong hiện đại (modern / 현대적) ngữ nghĩa (semantics / 의미론) và không giữ đối tượng (object / 객체) key sống chỉ vì entry tồn tại.

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

Use cases: siêu dữ liệu (metadata / 메타데이터) tied to đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명), object-keyed memoization, private trạng thái (state / 상태) legacy patterns.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Weak không có nghĩa “GC sẽ xóa ngay”. Đừng dùng WeakMap nếu bạn cần enumeration hoặc deterministic cleanup.

---

# Chương 19 — ES Modules sâu hơn

> **phiên bản (version / 버전) ghi chú (note / 노트):** Static modules thuộc ES2015; động (dynamic / 동적) `import()` và `import.meta` thuộc ES2020; import attributes/JSON modules thuộc ES2025. mô-đun (module / 모듈) records của ECMAScript và cách trình duyệt (browser / 브라우저)/nút (node / 노드)/bundler resolve mô-đun (module / 모듈) là hai lớp khác nhau.

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

Mô-đun (module / 모듈) phạm vi (scope / 범위) riêng, strict chế độ (mode / 모드) ngữ nghĩa (semantics / 의미론) và static phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) giúp bundler/tooling phân tích tốt.

Imports là **live bindings**. Nếu mô-đun (module / 모듈) export variable và thay đổi variable, importer đọc binding cập nhật.

Circular dependencies được ngôn ngữ (language / 언어) hỗ trợ nhưng initialization thứ tự (order / 순서) có thể gây bugs. Nếu A import B và B import A, hãy xem đó là kiến trúc (architecture / 아키텍처) smell trước khi tìm workaround.

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — công khai (public / 공개) mô-đun (module / 모듈) API

Tính năng (feature / 기능) có thể expose qua `index.js` một API nhỏ, còn nội bộ (internal / 내부) files không nên bị consumers deep-import tùy tiện.

---

# Chương 20 — động (dynamic / 동적) import và lazy loading concept

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2020:** động (dynamic / 동적) `import()` là tính năng (feature / 기능) ES2020. mã (code / 코드) splitting là hành vi (behavior / 동작) mà bundler có thể xây trên cú pháp (syntax / 문법) này, không phải một guarantee của ECMAScript tiêu chuẩn (standard / 표준).

```js
const module = await import(
  "./heavyFeature.js"
);
```

Động (dynamic / 동적) import trả Promise và cho phép tải (load / 로드) mã (code / 코드) theo nhu cầu. Bundlers có thể dùng nó làm code-splitting ranh giới (boundary / 경계).

Use trường hợp (case / 사례): editor lớn, chart thư viện (library / 라이브러리), tuyến (route / 경로) ít dùng, modal tính năng (feature / 기능) nặng.

Sự đánh đổi (trade-off / 트레이드오프): initial bundle nhỏ hơn nhưng first-use độ trễ (latency / 지연 시간) có thể tăng. cấp cao (senior / 시니어) cần đo UX thay vì lazy tải (load / 로드) mọi thứ.

---

# Chương 21 — Promise ngữ nghĩa (semantics / 의미론) sâu hơn

> **phiên bản (version / 버전) ghi chú (note / 노트):** bản địa (native / 네이티브) Promise thuộc ES2015; `Promise.prototype.finally()` thuộc ES2018. cốt lõi (core / 핵심) resolution/chaining ngữ nghĩa (semantics / 의미론) trong chương này quan trọng và bền vững hơn việc nhớ năm của từng helper.

Promise có ba states: pending, fulfilled, rejected. Khi settle, trạng thái (state / 상태) không thay đổi lại.

```js
Promise.resolve(10)
  .then((value) => value * 2)
  .then(console.log);
```

`.then()` luôn trả Promise mới. Nếu callback return plain giá trị (value / 값), Promise mới fulfill với giá trị (value / 값) đó. Nếu return Promise, chuỗi (chain / 사슬) adopts Promise đó. Nếu throw, Promise mới reject.

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

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Settled không đồng nghĩa fulfilled** tiếp nhận điểm tựa từ **Class syntax không xóa prototype model** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Resolution khác fulfillment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Settled không đồng nghĩa fulfilled

“Settled” nghĩa Promise không còn pending; nó có thể **fulfilled** hoặc **rejected**.

```text
pending
  ├─→ fulfilled(value)
  └─→ rejected(reason)
```

Một khi settled, Promise không chuyển trạng thái (state / 상태) lần nữa. Nếu executor gọi nhiều lần:

```js
new Promise((resolve, reject) => {
  resolve(1);
  resolve(2);
  reject(new Error("late"));
});
```

settlement đầu tiên quyết định trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Resolution khác fulfillment** tiếp nhận điểm tựa từ **Settled không đồng nghĩa fulfilled** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **.then() không sửa Promise cũ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Resolution khác fulfillment

Đây là nuance quan trọng khi Promise nhận một Promise/thenable khác.

```js
const inner = new Promise((resolve) => {
  setTimeout(() => resolve(42), 1000);
});

const outer = Promise.resolve(inner);
```

`outer` được **resolved to** `inner`, nghĩa là nó adopt eventual trạng thái (state / 상태) của `inner`. Nó chưa necessarily fulfilled ngay tại thời điểm relationship được thiết lập.

Mô hình tư duy (mental model / 사고 모델) hữu ích:

```text
return plain value
→ next Promise fulfill với value

throw error
→ next Promise reject

return Promise/thenable
→ next Promise adopt eventual state
```

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **.then() không sửa Promise cũ** tiếp nhận điểm tựa từ **Resolution khác fulfillment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Promise handlers luôn asynchronous so với current synchronous stack** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `.then()` không sửa Promise cũ
Phần này nối mạch bài học với “`.then()` không sửa Promise cũ”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
const p1 = Promise.resolve(10);
const p2 = p1.then((value) => value * 2);
```

`p1` và `p2` là hai Promise khác nhau. Đây là nền tảng của chaining. Mỗi `.then()` tạo một continuation và một Promise cho kết quả continuation đó.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Promise handlers luôn asynchronous so với current synchronous stack** tiếp nhận điểm tựa từ **.then() không sửa Promise cũ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thenable assimilation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Promise handlers luôn asynchronous so với current synchronous stack
Phần này nối mạch bài học với “Promise handlers luôn asynchronous so với current synchronous stack”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
console.log("A");

Promise.resolve().then(() => {
  console.log("B");
});

console.log("C");
```

Đầu ra (output / 출력):

```text
A
C
B
```

Ngay cả Promise đã fulfilled sẵn, handler `.then()` vẫn không chạy inline giữa `A` và `C`; nó được enqueue để chạy ở microtask checkpoint.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Thenable assimilation** tiếp nhận điểm tựa từ **Promise handlers luôn asynchronous so với current synchronous stack** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **.catch() và .finally() cũng tiếp tục chuỗi (chain / 사슬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thenable assimilation

Promise resolution không chỉ nhận bản địa (native / 네이티브) Promise. đối tượng (object / 객체) có callable `then` cũng có thể được assimilate:

```js
const thenable = {
  then(resolve) {
    resolve(123);
  }
};

const value = await Promise.resolve(thenable);
console.log(value); // 123
```

Điều này cho interoperability với Promise-like implementations, nhưng cũng có nghĩa “đọc/resolve một thenable” có thể invoke user-defined hành vi (behavior / 동작). Ở ứng dụng (application / 애플리케이션) mã (code / 코드) bình thường bạn không cần tự implement thenable; chỉ cần hiểu tại sao Promise có thể adopt non-native Promise-like values.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Thenable assimilation** xác định đầu vào; **.catch() và .finally() cũng tiếp tục chuỗi (chain / 사슬)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **await tạm dừng function, không tạm dừng thread** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `.catch()` và `.finally()` cũng tiếp tục chuỗi (chain / 사슬)

`.catch(onRejected)` về cơ bản là một form của `.then(undefined, onRejected)` và trả Promise mới. Nếu catch return giá trị (value / 값), chuỗi (chain / 사슬) có thể recover:

```js
const value = await Promise.reject(
  new Error("failed")
).catch(() => {
  return "fallback";
});
```

`value` là `"fallback"`.

`finally()` chủ yếu dùng cleanup không phụ thuộc success/thất bại (failure / 실패). Nếu finally callback không throw/return rejected Promise, original kết quả (outcome / 결과) đi tiếp.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Promise chuỗi (chain / 사슬) nên phản ánh quyền sở hữu (ownership / 소유권) của async luồng (flow / 흐름). Catch quá sớm rồi biến mọi lỗi (error / 오류) thành `null` thường phá lỗi (error / 오류) ngữ nghĩa (semantics / 의미론); catch ở nơi bạn thật sự có thể recover, translate hoặc add ngữ cảnh (context / 맥락).

---

# Chương 22 — `async` / `await` ngữ nghĩa (semantics / 의미론)

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2017:** Async functions/`await` thuộc ES2017. Top-level `await` trong modules thuộc ES2022; một thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원) `await` bên trong async hàm (function / 함수) chưa chắc hỗ trợ (support / 지원) top-level await nếu quá cũ.

`async function` luôn trả Promise. `throw` trong async hàm (function / 함수) trở thành rejected Promise.

```js
async function run() {
  throw new Error("failed");
}
```

`await expression` đợi Promise-like completion và suspend continuation của async hàm (function / 함수); nó không khối (block / 블록) trình duyệt (browser / 브라우저) main luồng thực thi (thread / 스레드) theo kiểu sleep.

Sequential phụ thuộc (dependency / 의존성):

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

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **.catch() và .finally() cũng tiếp tục chuỗi (chain / 사슬)** xác định đầu vào; **await tạm dừng function, không tạm dừng thread** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Async function luôn wrap return value thành Promise outcome** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `await` tạm dừng function, không tạm dừng thread
Phần này nối mạch bài học với “`await` tạm dừng function, không tạm dừng thread”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
async function load() {
  console.log("before");
  const user = await loadUser();
  console.log("after", user);
}
```

Khi `loadUser()` chưa hoàn thành, phần continuation sau `await` được suspend. JavaScript main luồng thực thi (thread / 스레드) có thể xử lý sự kiện (event / 이벤트)/tác vụ (task / 작업) khác. Khi awaited giá trị (value / 값) settle thành công, continuation được schedule để chạy lại qua Promise-job/microtask ngữ nghĩa (semantics / 의미론).

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Async function luôn wrap return value thành Promise outcome** tiếp nhận điểm tựa từ **await tạm dừng function, không tạm dừng thread** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **try/catch chỉ bắt rejection của phần bạn thật sự await** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Async function luôn wrap return value thành Promise outcome
Phần này nối mạch bài học với “Async function luôn wrap return value thành Promise outcome”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

async hàm (function / 함수) adopt eventual kết quả (result / 결과), không tạo “Promise bên trong Promise” theo cách caller phải await hai lần.

Nếu throw:

```js
async function fail() {
  throw new Error("boom");
}
```

caller nhận rejected Promise.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **try/catch chỉ bắt rejection của phần bạn thật sự await** tiếp nhận điểm tựa từ **Async function luôn wrap return value thành Promise outcome** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Start concurrent công việc (work / 작업) trước, await sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `try/catch` chỉ bắt rejection của phần bạn thật sự `await`
Phần này nối mạch bài học với “`try/catch` chỉ bắt rejection của phần bạn thật sự `await`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
async function run() {
  try {
    startAsyncWork();
  } catch (error) {
    // không nhất thiết bắt rejection của startAsyncWork
  }
}
```

Nếu `startAsyncWork()` trả Promise reject sau đó mà bạn không `await`/return nó, rejection tách khỏi synchronous `try` luồng (flow / 흐름).

```js
async function run() {
  try {
    await startAsyncWork();
  } catch (error) {
    // bắt được rejection ở đây
  }
}
```

Đây là nguồn phổ biến của unhandled rejections trong mã (code / 코드) tưởng rằng đã có try/catch.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Start concurrent công việc (work / 작업) trước, await sau** tiếp nhận điểm tựa từ **try/catch chỉ bắt rejection của phần bạn thật sự await** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) không phải một “hàng đợi (queue / 큐) duy nhất”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Start concurrent công việc (work / 작업) trước, await sau

Hai thao tác (operation / 연산) independent nhưng viết:

```js
const profile = await loadProfile();
const settings = await loadSettings();
```

thì yêu cầu (request / 요청) thứ hai chỉ bắt đầu sau yêu cầu (request / 요청) đầu xong. Nếu independent, có thể start cả hai trước:

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

Cấp cao (senior / 시니어) concern ở đây là **phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프)**, không phải “await chậm”. Sequential là đúng khi thao tác (operation / 연산) B cần kết quả (result / 결과) A; concurrent là đúng khi chúng độc lập và tính đồng thời (concurrency / 동시성) mức (level / 수준) hợp lý.

### Async `forEach` trap
Phần này nối mạch bài học với “Async `forEach` trap”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Nhưng với collection rất lớn, `Promise.all(items.map(...))` có thể tạo unbounded tính đồng thời (concurrency / 동시성). cấp cao (senior / 시니어) sẽ dùng pool/semaphore/mapLimit khi cần bound tài nguyên (resource / 자원) pressure.

---

# Chương 23 — vòng lặp sự kiện (event loop / 이벤트 루프): synchronous ngăn xếp (stack / 스택), tasks và microtasks

Trình duyệt (browser / 브라우저) JavaScript thường chạy UI JS trên main luồng thực thi (thread / 스레드). vòng lặp sự kiện (event loop / 이벤트 루프) phối hợp ngăn xếp lời gọi (call stack / 호출 스택), tasks, microtasks và rendering opportunities.

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

Typical đầu ra (output / 출력):

```text
A
D
B
C
```

Hiện tại (current / 현재) synchronous ngăn xếp (stack / 스택) chạy trước. Promise continuation được schedule như microtask. Timer callback là tác vụ (task / 작업) và thường chạy sau microtasks của hiện tại (current / 현재) turn.

`queueMicrotask`:

```js
queueMicrotask(() => {
  console.log("microtask");
});
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) không phải một “hàng đợi (queue / 큐) duy nhất”** tiếp nhận điểm tựa từ **Start concurrent công việc (work / 작업) trước, await sau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Microtask checkpoint drain đến khi hàng đợi (queue / 큐) rỗng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) không phải một “hàng đợi (queue / 큐) duy nhất”

Mô hình tư duy (mental model / 사고 모델) beginner thường nói “callback hàng đợi (queue / 큐)”. Đủ để bắt đầu, nhưng ở Intermediate nên nâng lên:

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

“tác vụ (task / 작업)” có thể đến từ timer, người dùng (user / 사용자) tương tác (interaction / 상호작용), networking/other host sources tùy trình duyệt (browser / 브라우저) specification. Không nên dựa vào một thứ tự tổng quát giữa mọi tác vụ (task / 작업) nguồn (source / 소스) ngoài guarantees cụ thể.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Microtask checkpoint drain đến khi hàng đợi (queue / 큐) rỗng** tiếp nhận điểm tựa từ **Trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) không phải một “hàng đợi (queue / 큐) duy nhất”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Promise continuation và queueMicrotask() cùng thuộc microtask-level scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Microtask checkpoint drain đến khi hàng đợi (queue / 큐) rỗng

Nếu một microtask enqueue microtask khác, thời gian chạy (runtime / 런타임) tiếp tục xử lý trước khi quay về tác vụ (task / 작업)/kết xuất (render / 렌더링) opportunity.

```js
queueMicrotask(() => {
  console.log("M1");

  queueMicrotask(() => {
    console.log("M2");
  });
});
```

Điều này giải thích **microtask starvation**: mã (code / 코드) liên tục enqueue microtasks có thể trì hoãn timers, đầu vào (input / 입력) và rendering.

```js
function loop() {
  queueMicrotask(loop);
}

loop();
```

Đây là mã (code / 코드) pathological; trình duyệt (browser / 브라우저) không có cơ hội bình thường để tiến tới tác vụ (task / 작업)/rendering tiếp theo.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Promise continuation và queueMicrotask() cùng thuộc microtask-level scheduling** tiếp nhận điểm tựa từ **Microtask checkpoint drain đến khi hàng đợi (queue / 큐) rỗng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Rendering không xảy ra sau mọi dòng mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Promise continuation và `queueMicrotask()` cùng thuộc microtask-level scheduling
Phần này nối mạch bài học với “Promise continuation và `queueMicrotask()` cùng thuộc microtask-level scheduling”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Các microtasks được enqueue theo thứ tự (order / 순서) thời gian chạy (runtime / 런타임) tạo chúng, nên mental dấu vết (trace / 추적) quan trọng là **thời điểm enqueue**, không phải cú pháp (syntax / 문법) trông “Promise quan trọng hơn queueMicrotask”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **Rendering không xảy ra sau mọi dòng mã (code / 코드)** tiếp nhận điểm tựa từ **Promise continuation và queueMicrotask() cùng thuộc microtask-level scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **requestAnimationFrame() không phải microtask hay timer replacement chung** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Rendering không xảy ra sau mọi dòng mã (code / 코드)

Trình duyệt (browser / 브라우저) thường có rendering opportunities giữa event-loop turns/checkpoints khi phù hợp. Nếu một tác vụ (task / 작업) synchronous dài 200ms, trình duyệt (browser / 브라우저) không thể paint UI giữa các dòng JavaScript đó dù bạn vừa thay DOM ở đầu tác vụ (task / 작업).

```js
button.textContent = "Working...";

heavySynchronousWork();
```

Nếu `heavySynchronousWork()` khối (block / 블록) lâu, người dùng (user / 사용자) có thể chưa nhìn thấy văn bản (text / 텍스트) mới cho đến khi tác vụ (task / 작업) kết thúc và trình duyệt (browser / 브라우저) có cơ hội kết xuất (render / 렌더링).

Đây là lý do long tác vụ (task / 작업) ảnh hưởng responsiveness.

> **Chuyển mạch:** Trong **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **requestAnimationFrame() không phải microtask hay timer replacement chung** tiếp nhận điểm tựa từ **Rendering không xảy ra sau mọi dòng mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trace một ví dụ đầy đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `requestAnimationFrame()` không phải microtask hay timer replacement chung

`requestAnimationFrame()` là Web API để schedule callback phù hợp với rendering cycle. Nó hữu ích cho animation/DOM visual cập nhật (update / 업데이트) coordination, không phải cơ chế (mechanism / 메커니즘) để chạy mọi nghiệp vụ (business / 비즈니스) async công việc (work / 작업).

```js
requestAnimationFrame(() => {
  element.style.transform = "translateX(100px)";
});
```

Trong background tab, rendering/rAF có thể throttled hoặc pause tùy trình duyệt (browser / 브라우저). Vì vậy đừng dùng rAF làm nghiệp vụ (business / 비즈니스) clock.

> **Chuyển mạch:** Ở chặng này của **JavaScript Intermediate — Hiểu ngôn ngữ từ bên trong**, **requestAnimationFrame() không phải microtask hay timer replacement chung** cho ta quy tắc; **Trace một ví dụ đầy đủ** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Trace một ví dụ đầy đủ
Phần này nối mạch bài học với “Trace một ví dụ đầy đủ”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Dấu vết (trace / 추적):

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

Đầu ra (output / 출력):

```text
script start
script end
promise 1
queued microtask
promise 2
timer
```

Cách dấu vết (trace / 추적) này đáng tin cậy hơn học thuộc một vài câu “Promise trước setTimeout”.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Microtasks có priority cao đến mức một chuỗi (chain / 사슬) microtasks dài có thể trì hoãn rendering/tasks. Không dùng scheduling tricks nếu không hiểu reason.

---

# Chương 24 — Timer không phải clock chính xác

`setTimeout(fn, 1000)` nghĩa gần như “đừng chạy callback trước khoảng delay này, sau đó schedule khi vòng lặp sự kiện (event loop / 이벤트 루프) có cơ hội”, không phải guarantee 1000ms chính xác.

Main luồng thực thi (thread / 스레드) bị khối (block / 블록) 3 giây thì timer 1 giây cũng chạy muộn.

`setInterval` có thể không phù hợp cho async polling nếu thao tác (operation / 연산) kéo dài. Recursive `setTimeout` giúp schedule lần sau sau khi lần hiện tại hoàn thành:

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

> **phiên bản (version / 버전) ghi chú (note / 노트):** `all()`/`race()` đi với Promise ES2015; `allSettled()` là ES2020; `any()` + `AggregateError` là ES2021; `withResolvers()` là ES2024; `try()` là ES2025. Chọn combinator theo thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론) chứ không theo độ mới.

`Promise.all` đợi tất cả và reject khi một promise reject.

```js
const [user, orders] = await Promise.all([
  loadUser(),
  loadOrders()
]);
```

`Promise.allSettled` đợi tất cả, useful cho batch nơi partial thất bại (failure / 실패) hợp lệ.

`Promise.race` settle theo promise đầu tiên settle. Nhưng losing promises **không tự cancel**.

`Promise.any` fulfill theo promise đầu tiên fulfill; nếu tất cả reject thì `AggregateError`.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Chọn combinator theo nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론). `all` nghĩa “tất cả cần thành công”. `allSettled` nghĩa “tôi quan tâm kết quả (result / 결과) từng tác vụ (task / 작업) kể cả thất bại (failure / 실패)”.

---

# Chương 26 — AbortController và cancellation

> **nền tảng (platform / 플랫폼) phiên bản (version / 버전) ghi chú (note / 노트):** `AbortController`/`AbortSignal` là Web APIs, không phải ECMAScript yearly tính năng (feature / 기능). `AbortSignal.timeout()` và `AbortSignal.any()` cũng có browser-compatibility timeline riêng. Vì vậy hãy kiểm tra mục tiêu (target / 대상) WebView/trình duyệt (browser / 브라우저) thay vì hỏi chúng thuộc ES phiên bản (version / 버전) nào.

Promise tự thân không có universal cancellation. trình duyệt (browser / 브라우저) APIs như fetch nhận `AbortSignal`.

```js
const controller = new AbortController();

fetch("/api/users", {
  signal: controller.signal
});

controller.abort();
```

Dịch vụ (service / 서비스) API nên nhận tín hiệu (signal / 신호) từ caller:

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

### Mẫu lập trình (programming pattern / 프로그래밍 패턴) — caller owns thời gian tồn tại (lifetime / 수명)

Page/thành phần (component / 컴포넌트) tạo controller và abort khi điều hướng (navigation / 내비게이션)/unmount/new yêu cầu (request / 요청) làm thao tác (operation / 연산) cũ obsolete.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Cancellation và “ignore stale kết quả (result / 결과)” là hai strategies khác nhau. Có operations không cancel được, khi đó yêu cầu (request / 요청) versioning vẫn cần.

---

# Chương 27 — Race điều kiện (condition / 조건) và stale results

Autocomplete example:

```text
request A: "ja"
request B: "java"
B trả về trước
A trả về sau
```

Nếu kết xuất (render / 렌더링) kết quả (result / 결과) cuối cùng nhận được, UI có thể quay về kết quả cũ của A.

Chiến lược (strategy / 전략) 1: abort old yêu cầu (request / 요청).

Chiến lược (strategy / 전략) 2: yêu cầu (request / 요청) phiên bản (version / 버전):

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

Race điều kiện (condition / 조건) là vấn đề timing, không phải cú pháp (syntax / 문법).

---

# Chương 28 — Iterator giao thức (protocol / 프로토콜)

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015 và ES2025:** Iterator giao thức (protocol / 프로토콜), `Symbol.iterator`, `for...of` và generators thuộc ES2015. ES2025 bổ sung toàn cục (global / 전역) `Iterator` cùng helpers như `map`, `filter`, `take`, `drop`, `flatMap`, `reduce` và `toArray` cho lazy pipelines.

Iterable đối tượng (object / 객체) có `Symbol.iterator` trả iterator. Iterator có `next()` trả `{ value, done }`.

```js
const iterator = [10, 20][Symbol.iterator]();

iterator.next();
// { value: 10, done: false }
```

`for...of` sử dụng iterable giao thức (protocol / 프로토콜).

Array, String, Map, Set đều iterable. Plain đối tượng (object / 객체) không iterable mặc định.

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

### Mẫu thiết kế (design pattern / 디자인 패턴)

Đây chính là Iterator mẫu (pattern / 패턴) ở ngôn ngữ (language / 언어) mức (level / 수준).

---

# Chương 29 — Generator và lazy evaluation

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2015/ES6:** Generator `function*`/`yield` thuộc ES2015. Async generators là bước phát triển tiếp theo và thuộc ES2018.

Generator hàm (function / 함수):

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

Generator tạo values lazily, khi bên tiêu thụ (consumer / 소비자) yêu cầu.

Infinite chuỗi (sequence / 시퀀스):

```js
function* ids() {
  let id = 1;

  while (true) {
    yield id;
    id += 1;
  }
}
```

Không tạo infinite array trong bộ nhớ (memory / 메모리).

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Generator rất hữu ích cho lazy pipelines nhưng array methods đơn giản hơn cho ordinary small collections. Đừng dùng generator chỉ để thể hiện advanced skill.

---

# Chương 30 — Async iterator và `for await...of`

> **phiên bản (version / 버전) ghi chú (note / 노트) — ES2018:** Async iteration, async iterator giao thức (protocol / 프로토콜), async generators và `for await...of` được chuẩn hóa ở ES2018. Legacy runtimes trước đó thường dùng sự kiện (event / 이벤트)/callback/Promise loops cho các luồng (flow / 흐름) tương tự.

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

Bên tiêu thụ (consumer / 소비자):

```js
for await (const items of pages()) {
  render(items);
}
```

Concept này useful cho pagination, streams và progressive dữ liệu (data / 데이터). cấp cao (senior / 시니어) sẽ học backpressure sâu hơn.

---

# Chương 31 — Functional programming thực dụng

Bạn không cần biến JavaScript thành pure-functional ngôn ngữ (language / 언어). Các ý hữu ích nhất là pure hàm (function / 함수), immutability, composition, declarative transformations và side-effect boundaries.

```js
function calculateTax(
  subtotal,
  rate
) {
  return subtotal * rate;
}
```

Pure hàm (function / 함수) dễ kiểm thử (test / 테스트) vì đầu ra (output / 출력) chỉ phụ thuộc đầu vào (input / 입력).

Side effects như mạng (network / 네트워크)/lưu trữ (storage / 저장소)/DOM vẫn cần, nhưng nên tường minh (explicit / 명시적) ở ranh giới (boundary / 경계).

### Programming pattern — Functional Core / Imperative Shell
Phần này nối mạch bài học với “Programming pattern — Functional Core / Imperative Shell”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Immutable cập nhật (update / 업데이트):

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

Chỉ branches thay đổi có đối tượng (object / 객체) mới; branches khác giữ tham chiếu (reference / 참조) cũ. Đây là **structural sharing**.

Nó hữu ích cho tham chiếu (reference / 참조) equality và thay đổi (change / 변경) detection trong UI trạng thái (state / 상태) các hệ thống (systems / 시스템들).

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Immutability không miễn phí. bản sao (copy / 복사) đối tượng (object / 객체) đồ thị (graph / 그래프) cực lớn có chi phí (cost / 비용). cục bộ (local / 로컬) mutation trong isolated thuật toán (algorithm / 알고리즘) vẫn có thể hợp lý. Mục tiêu là kiểm soát trạng thái dùng chung (shared state / 공유 상태), không phải cấm assignment.

---

# Chương 33 — hàm (function / 함수) composition, pipe và partial ứng dụng (application / 애플리케이션)

Composition nối đầu ra (output / 출력) của hàm (function / 함수) này vào đầu vào (input / 입력) hàm (function / 함수) khác.

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

Partial ứng dụng (application / 애플리케이션) preconfigures arguments:

```js
function request(baseUrl, path) {
  return fetch(`${baseUrl}${path}`);
}

const apiRequest = request.bind(
  null,
  "/api"
);
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Composition tốt khi contracts nhỏ/rõ. chuỗi xử lý (pipeline / 파이프라인) quá abstract có thể khó gỡ lỗi (debug / 디버그) hơn vài statements bình thường.

---

# Chương 34 — Memoization và caching computation

Memoization bộ nhớ đệm (cache / 캐시) đầu ra (output / 출력) theo đầu vào (input / 입력).

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

Bộ nhớ đệm (cache / 캐시) có thể tăng bộ nhớ (memory / 메모리) vô hạn nếu key không gian (space / 공간) không bounded. đối tượng (object / 객체) keys dựa định danh (identity / 식별자), nên hai `{ id: 1 }` khác nhau là keys khác. Đừng memoize cheap hàm (function / 함수) chỉ vì có thể.

---

# Chương 35 — sự kiện (event / 이벤트) bubbling, capturing và delegation

DOM sự kiện (event / 이벤트) thường travel qua capture phase, mục tiêu (target / 대상) phase và bubble phase. `addEventListener` mặc định nghe bubble phase.

Sự kiện (event / 이벤트) delegation tận dụng bubbling để gắn một listener ở parent thay vì từng child.

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

Benefits: ít listeners hơn, động (dynamic / 동적) children vẫn được handle.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

`event.target` có thể là nested child. `closest()` cần guard để không match element ngoài intended subtree trong complex DOM.

---

# Chương 36 — DOM lifecycle: init và cleanup
Phần này nối mạch bài học với “Chương 36 — DOM lifecycle: init và cleanup”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Vòng đời (lifecycle / 생명주기) mẫu (pattern / 패턴) phải áp dụng cho listener, timer, observer, subscription, worker và mạng (network / 네트워크) cancellation.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Bộ nhớ (memory / 메모리) leak frontend thường là **quyền sở hữu (ownership / 소유권)/vòng đời (lifecycle / 생명주기) bug**, không phải “GC kém”. Ai tạo tài nguyên (resource / 자원) thì kiến trúc (architecture / 아키텍처) phải biết ai cleanup và khi nào.

---

# Chương 37 — trình duyệt (browser / 브라우저) rendering chuỗi xử lý (pipeline / 파이프라인) ở mức Intermediate

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

DOM read như `offsetWidth` có thể cần bố cục (layout / 레이아웃) dữ liệu (data / 데이터). DOM ghi (write / 쓰기) như thay `style.width` có thể invalidate bố cục (layout / 레이아웃). Interleave read/ghi (write / 쓰기) nhiều lần có thể gây bố cục (layout / 레이아웃) thrashing.

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Không assume mọi DOM ghi (write / 쓰기) đều expensive ngang nhau. hiệu năng (performance / 성능) phải profile trên tải công việc (workload / 워크로드) thật.

---

# Chương 38 — API máy khách (client / 클라이언트) lớp trừu tượng (abstraction / 추상화)

Raw fetch rải khắp dự án (project / 프로젝트) gây duplicate headers, auth, lỗi (error / 오류) handling, JSON parsing.

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

Feature-specific dịch vụ (service / 서비스):

```js
const userApi = {
  getUser(id) {
    return requestJson(
      `/api/users/${id}`
    );
  }
};
```

### Mẫu thiết kế (design pattern / 디자인 패턴) liên kết (connection / 연결)

HTTP wrapper có thể đóng vai Adapter/Facade/Gateway. Generic vận chuyển (transport / 전송) máy khách (client / 클라이언트) không nên chứa nghiệp vụ (business / 비즈니스) rules của người dùng (user / 사용자)/thứ tự (order / 순서).

---

# Chương 39 — lỗi (error / 오류) kiến trúc (architecture / 아키텍처) và custom lỗi (error / 오류) taxonomy

Không phải mọi lỗi (error / 오류) nên được catch ngay nơi phát sinh. hạ tầng (infrastructure / 인프라) tầng (layer / 계층) có thể tạo stable lỗi (error / 오류) cấu trúc (structure / 구조); UI tầng (layer / 계층) chuyển lỗi (error / 오류) thành người dùng (user / 사용자) message.

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

Dịch vụ (service / 서비스):

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

`cause` giữ chuỗi nhân quả (causal chain / 인과 사슬).

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Lỗi (error / 오류) kiểu (type / 타입)/mã (code / 코드) là Đặc tả API (API contract / API 계약). Đừng parse message string để quyết định lô-gic (logic / 논리). User-facing message và diagnostic details nên tách.

---

# Chương 40 — thử lại (retry / 재시도) và hết thời gian chờ (timeout / 타임아웃) fundamentals

Hết thời gian chờ (timeout / 타임아웃) với AbortController:

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

Thử lại (retry / 재시도) chỉ phù hợp cho transient failures. kiểm tra hợp lệ (validation / 검증) 400 hoặc permission 403 không tự hết vì thử lại (retry / 재시도).

Naive thử lại (retry / 재시도):

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

Cấp cao (senior / 시니어) sẽ học exponential backoff, jitter, idempotency và thử lại (retry / 재시도) storm.

---

# Chương 41 — DTO ánh xạ (mapping / 매핑) và Anti-Corruption ranh giới (boundary / 경계)

Backend legacy có thể trả:

```js
{
  user_no: "1001",
  user_nm: "Kim",
  use_yn: "Y"
}
```

Frontend lĩnh vực (domain / 도메인) muốn:

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

Đây là Adapter/Mapper/Anti-Corruption tầng (layer / 계층). Nó rất hữu ích cho Java/Spring legacy backend, WebSquare DataMap/DataList và vendor/bản địa (native / 네이티브) APIs.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Không cần mapper nếu bên ngoài (external / 외부) và nội bộ (internal / 내부) shapes thật sự giống và không có ngữ nghĩa (semantic / 의미적) benefit. tầng (layer / 계층) chỉ có giá trị khi nó bảo vệ ranh giới (boundary / 경계) hoặc chuyển meaning.

---

# Chương 42 — trạng thái (state / 상태) modeling và Boolean Explosion

Bad:

```js
let isLoading = false;
let isSuccess = false;
let hasError = false;
```

Bạn có thể tạo trạng thái (state / 상태) vô lý: cả ba true.

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
Phần này nối mạch bài học với “Programming pattern — explicit state machine lite”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
const STATUS = {
  IDLE: "idle",
  LOADING: "loading",
  SUCCESS: "success",
  ERROR: "error"
};
```

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Nhiều “React/WebSquare trạng thái (state / 상태) bug” thật ra là modeling bug, không phải khung phần mềm (framework / 프레임워크) bug.

---

# Chương 43 — Reducer mẫu (pattern / 패턴)

Reducer là pure-ish chuyển tiếp trạng thái (state transition / 상태 전이) hàm (function / 함수):

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

Mô hình tư duy (mental model / 사고 모델):

```text
previous state
+
action
=
next state
```

Reducer không nên tự fetch/mạng (network / 네트워크). Side tác động (effect / 효과) orchestration nên ở tầng (layer / 계층) khác.

### Thiết kế (design / 설계) connections

Reducer liên quan trạng thái (state / 상태) mẫu (pattern / 패턴), Command-like actions và event-driven trạng thái (state / 상태) transitions.

---

# Chương 44 — Observer và Pub/Sub

Observer: subject giữ danh sách (list / 목록) observers/subscribers và notify họ.

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

Pub/Sub thường có broker/sự kiện (event / 이벤트) bus ở giữa, publisher không biết subscribers trực tiếp.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Sự kiện (event / 이벤트) bus giảm coupling trực tiếp nhưng tạo hidden phụ thuộc (dependency / 의존성). sự kiện (event / 이벤트) names trở thành implicit API và gỡ lỗi (debug / 디버그) luồng (flow / 흐름) khó hơn. Direct hàm (function / 함수) lời gọi (call / 호출) tốt hơn khi phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적) không phải vấn đề.

---

# Chương 45 — Strategy Pattern bằng function
Phần này nối mạch bài học với “Chương 45 — Strategy Pattern bằng function”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Chiến lược (strategy / 전략) phù hợp khi behaviors thật sự interchangeable. Hai branches nhỏ bằng `if` chưa cần mẫu (pattern / 패턴).

---

# Chương 46 — Factory mẫu (pattern / 패턴)

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

Factory có thể return plain đối tượng (object / 객체), hàm (function / 함수) hoặc lớp (class / 클래스) instance. Không cần Factory chỉ để wrap `{ name }` nếu không có construction lô-gic (logic / 논리).

---

# Chương 47 — Adapter mẫu (pattern / 패턴)

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

Adapter cực kỳ phổ biến trong enterprise tích hợp (integration / 통합), WebSquare submission/bản địa (native / 네이티브) plugin/vendor SDK.

---

# Chương 48 — Facade mẫu (pattern / 패턴)

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

Facade giảm kiến thức (knowledge / 지식) caller cần biết. Nhưng nếu facade chứa toàn hệ thống, nó biến thành God dịch vụ (service / 서비스).

---

# Chương 49 — Command mẫu (pattern / 패턴)

Hàm (function / 함수) registry:

```js
const commands = {
  save: () => save(),
  cancel: () => cancel(),
  refresh: () => refresh()
};
```

Command đối tượng (object / 객체):

```js
const command = {
  type: "UPDATE_USER",
  payload: {
    id: 1,
    name: "Kim"
  }
};
```

Command-as-data hữu ích cho hàng đợi (queue / 큐), logging, undo/redo, reducers và phân tán (distributed / 분산)/sự kiện (event / 이벤트) các hệ thống (systems / 시스템들).

---

# Chương 50 — Middleware mẫu (pattern / 패턴)

Middleware wrap next thao tác (operation / 연산):

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

Middleware kết hợp ideas của Decorator và chuỗi (chain / 사슬) of Responsibility.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Thứ tự (order / 순서) matters. thử lại (retry / 재시도)/auth/logging wrappers không thể reorder tùy tiện. Middleware đặc tả hợp đồng (contract / 계약) và mutation chính sách (policy / 정책) phải rõ.

---

# Chương 51 — phụ thuộc (dependency / 의존성) Injection không cần khung phần mềm (framework / 프레임워크)

Hard-coded phụ thuộc (dependency / 의존성):

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

Kiểm thử (test / 테스트) fake:

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

DI không đồng nghĩa Spring bộ chứa (container / 컨테이너). hàm (function / 함수) parameter hoặc factory phụ thuộc (dependency / 의존성) đối tượng (object / 객체) thường đủ cho frontend.

---

# Chương 52 — Testing fundamentals

Pure hàm (function / 함수):

```js
function addTax(price, rate) {
  return price * (1 + rate);
}
```

Kiểm thử (test / 테스트):

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

Ưu tiên kiểm thử (test / 테스트) nghiệp vụ (business / 비즈니스) rules, ranh giới (boundary / 경계) cases, lỗi (error / 오류) paths, trạng thái (state / 상태) transitions và mappings.

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Coverage % không bằng confidence. mã (code / 코드) khó kiểm thử (test / 테스트) thường cho thấy coupling hoặc hidden side effects.

---

# Chương 53 — Mock, Stub, Spy và Fake

Stub trả canned giá trị (value / 값). Spy theo dõi lời gọi (call / 호출). Mock thường là kiểm thử (test / 테스트) double có expectations. Fake là hiện thực (implementation / 구현) đơn giản nhưng functional.

Frontend mã (code / 코드) thường benefit từ simple fakes hơn heavy mocking.

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

### Cấp cao (senior / 시니어) ghi chú (note / 노트)

Mock boundaries, đừng mock mọi helper nội bộ. Nếu kiểm thử (test / 테스트) biết hiện thực (implementation / 구현) lời gọi (call / 호출) thứ tự (order / 순서) quá chi tiết, refactor hiện thực (implementation / 구현) có thể làm kiểm thử (test / 테스트) thất bại (fail / 실패) dù hành vi (behavior / 동작) không đổi.

---

# Chương 54 — Async testing principles

Không nên kiểm thử (test / 테스트) bằng arbitrary sleep:

```js
await new Promise(
  (resolve) =>
    setTimeout(resolve, 2000)
);
```

Prefer chờ actual promise/sự kiện (event / 이벤트)/trạng thái (state / 상태) hoặc dùng fake timers.

Kiểm thử (test / 테스트) cancellation cần verify thao tác (operation / 연산) abort/cleanup đúng. Race điều kiện (condition / 조건) tests cần điều khiển (control / 제어) thứ tự (ordering / 순서).

---

# Chương 55 — Debugging thời gian chạy (runtime / 런타임) ở mức Intermediate

DevTools Sources cho breakpoint, conditional breakpoint, ngăn xếp lời gọi (call stack / 호출 스택), phạm vi (scope / 범위), closure, watch expressions. mạng (network / 네트워크) tab cho yêu cầu (request / 요청)/phản hồi (response / 응답)/timing. hiệu năng (performance / 성능) cho long tasks/rendering. bộ nhớ (memory / 메모리) cho vùng nhớ động (heap / 힙)/retainer paths.

Một quy trình gỡ lỗi (debug / 디버그) tốt:

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

Không đổi năm chỗ mã (code / 코드) cùng lúc rồi đoán chỗ nào fix.

---

# Chương 56 — Intermediate Anti-patterns

Promise nesting thay vì chaining/await; missing return trong `.then`; async `forEach`; unbounded `Promise.all`; sự kiện (event / 이벤트) bus cho mọi giao tiếp; deep inheritance; lớp (class / 클래스) cho stateless utilities; catch rồi return null mọi nơi; optional chaining để che required dữ liệu (data / 데이터); bound callback inline mà không cleanup; dịch vụ (service / 서비스) đối tượng (object / 객체) biết DOM, mạng (network / 네트워크), trạng thái (state / 상태) và analytics cùng lúc; over-abstraction nhiều tầng (layer / 계층) cho CRUD đơn giản; under-abstraction sự kiện (event / 이벤트) handler hàng trăm dòng.

Mục tiêu của Intermediate là bắt đầu thấy **shape của độ phức tạp (complexity / 복잡도)**, không chỉ cú pháp (syntax / 문법).

---

# Chương 57 — Mini dự án (project / 프로젝트): tìm kiếm (search / 검색) Page có cancellation và trạng thái (state / 상태)

Trạng thái (state / 상태):

```js
const state = {
  status: "idle",
  keyword: "",
  users: [],
  error: null
};
```

Tìm kiếm (search / 검색) dịch vụ (service / 서비스) giữ controller hiện tại:

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

Dự án (project / 프로젝트) này kết hợp closure, cancellation, dịch vụ (service / 서비스), trạng thái (state / 상태) modeling, lỗi (error / 오류) handling và vòng đời (lifecycle / 생명주기).

---

# Chương 58 — Mini Project: Event-driven Store
Phần này nối mạch bài học với “Chương 58 — Mini Project: Event-driven Store”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Bạn đang kết hợp closure, private trạng thái (state / 상태), reducer, Observer, immutable trạng thái (state / 상태) và cleanup. mô hình tư duy (mental model / 사고 모델) này rất gần nhiều state-management libraries.

---

# Chương 59 — Intermediate Exit Criteria

Trước khi lên cấp cao (senior / 시니어), bạn phải giải thích được closure sống thế nào, `this` được bind bởi call-site ra sao, arrow khác normal hàm (function / 함수) ở điểm nào, thuộc tính (property / 속성) lookup đi qua prototype chuỗi (chain / 사슬) thế nào, lớp (class / 클래스) liên quan prototype ra sao, Promise chuỗi (chain / 사슬) adopt returned Promise như thế nào, vòng lặp sự kiện (event loop / 이벤트 루프) xếp synchronous/microtask/tác vụ (task / 작업) ra sao, sequential và concurrent khác nhau thế nào, vì sao Promise.race không cancel loser, AbortController nên thuộc vòng đời (lifecycle / 생명주기) nào, máy trạng thái (state machine / 상태 머신) tốt hơn nhiều booleans ở đâu, và phụ thuộc (dependency / 의존성) Injection không cần khung phần mềm (framework / 프레임워크) thế nào.

Bạn cũng phải có thể refactor một tính năng (feature / 기능) trộn DOM + mạng (network / 네트워크) + lô-gic nghiệp vụ (business logic / 비즈니스 로직) thành view/controller/dịch vụ (service / 서비스)/pure lô-gic (logic / 논리) ở mức vừa đủ mà không over-engineer.

---

# Chương 60 — Hướng sang cấp cao (senior / 시니어)

Senior JavaScript sẽ không tập trung thêm syntax. Nó tập trung runtime/engine, memory/GC, resource ownership, bounded concurrency, Workers/Streams/backpressure, performance profiling, security, XSS/CSP/Trusted Types, prototype pollution, architecture boundaries, resilience, caching, observability và production testing. Đây là bước chuyển từ “developer hiểu language” sang “developer chịu trách nhiệm hệ thống chạy ổn trong production”.

> **Bàn giao:** Sau **Trace một ví dụ đầy đủ**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
