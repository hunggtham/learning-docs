# JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **ES5 — chuẩn hóa nền JavaScript web trước thời hiện đại (modern / 현대적) cú pháp (syntax / 문법)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **ES2015/ES6 — bước chuyển sang JavaScript cho ứng dụng (application / 애플리케이션) lớn** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> **Vai trò của tệp (file / 파일) này:** đây là phần thứ tư sau `Beginner → Intermediate → Senior`. tệp (file / 파일) không học lại cú pháp cơ bản mà nối toàn bộ kiến thức thành một mô hình tư duy (mental model / 사고 모델) thống nhất: mã nguồn (source code / 소스 코드) được khởi tạo và thực thi ra sao, phạm vi (scope / 범위)/closure/prototype/mô-đun (module / 모듈) liên hệ với nhau thế nào, trình duyệt (browser / 브라우저) vòng lặp sự kiện (event loop / 이벤트 루프) phối hợp tác vụ (task / 작업)/microtask/kết xuất (render / 렌더링) ra sao, vì sao JavaScript tiến hóa từ ES5 sang ES2015 rồi sang yearly ECMAScript, và nhà phát triển (developer / 개발자) môi trường vận hành (production / 운영 환경) phải đọc legacy/hiện đại (modern / 현대적) mã (code / 코드) như thế nào.
>
> **phiên bản (version / 버전) tham chiếu:** snapshot chính thức hiện hành là **ECMAScript 2026 — ECMA-262 17th edition**. Living specification trên TC39 có thể đã chứa các finished proposals hướng tới snapshot kế tiếp, vì vậy trong tài liệu này luôn tách bốn khái niệm: **tiêu chuẩn (standard / 표준) snapshot**, **proposal/living spec**, **engine hiện thực (implementation / 구현)** và **thời gian chạy (runtime / 런타임) mục tiêu (target / 대상) thực tế**.
>
> tệp (file / 파일) này là **supplement**, không thay thế ba tệp (file / 파일) trước. Khi một concept đã được dạy kỹ ở Beginner/Intermediate/cấp cao (senior / 시니어), phần Master chỉ nối nó với ngữ nghĩa (semantics / 의미론) sâu hơn hoặc môi trường vận hành (production / 운영 환경) consequences.

---

# 1. kiểm tra (audit / 감사) toàn bộ JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리)

Sau khi kiểm tra (audit / 감사) chuẩn gốc (canonical / 정본) notes từ Beginner đến cấp cao (senior / 시니어), mạch học (learning flow / 학습 흐름) hiện tại đã bao phủ đầy đủ các nhóm kiến thức chính. Beginner sở hữu phần values/types, coercion cơ bản, hàm (function / 함수), array/đối tượng (object / 객체), DOM, events, fetch, lưu trữ (storage / 저장소), Promise và async/await nhập môn. Intermediate sở hữu thực thi (execution / 실행) ngữ cảnh (context / 맥락), lexical môi trường (environment / 환경), closure, `this`, prototype chuỗi (chain / 사슬), lớp (class / 클래스) internals, mô-đun (module / 모듈) hệ thống (system / 시스템), Promise ngữ nghĩa (semantics / 의미론), vòng lặp sự kiện (event loop / 이벤트 루프), tasks/microtasks, iterator/generator và các programming patterns. cấp cao (senior / 시니어) sở hữu engine/thời gian chạy (runtime / 런타임) thinking, bộ nhớ (memory / 메모리)/garbage collection, tính đồng thời (concurrency / 동시성), streaming, hiệu năng (performance / 성능), bảo mật (security / 보안), kiến trúc (architecture / 아키텍처), khả năng quan sát (observability / 관측 가능성), testing và hiện đại (modern / 현대적) tooling.

Master vì vậy không nên trở thành “tệp (file / 파일) thứ tư lặp lại ba tệp (file / 파일) đầu”. Vai trò đúng của nó là xử lý những câu hỏi còn lại sau khi đã học ba mức (level / 수준) trước: **tại sao các cơ chế đó tồn tại, chúng nối với nhau thế nào, spec mô tả chúng ra sao, mã (code / 코드) legacy phản ánh thế hệ JavaScript nào, và tính năng (feature / 기능) mới nên được đưa vào môi trường vận hành (production / 운영 환경) theo tiêu chí nào**.

Một sơ đồ quyền sở hữu (ownership / 소유권) ngắn:

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

# 2. JavaScript mô hình thực thi (execution model / 실행 모델) — ghép toàn bộ bức tranh lại với nhau

Một trong những lỗi phổ biến khi học JavaScript là biết từng từ khóa riêng lẻ nhưng không có một mô hình thống nhất cho quá trình thực thi. Ta có thể bắt đầu từ một tệp (file / 파일) mô-đun (module / 모듈) đơn giản:

```js
const taxRate = 0.1;

export function calculateTotal(price) {
  const tax = price * taxRate;
  return price + tax;
}

console.log(calculateTotal(100));
```

Khi thời gian chạy (runtime / 런타임) xử lý nguồn (source / 소스), không nên hình dung rằng engine chỉ đọc dòng 1, chạy dòng 1, đọc dòng 2, chạy dòng 2. Trước khi evaluation thực sự đi qua statements, ngôn ngữ (language / 언어) thời gian chạy (runtime / 런타임) cần phân tích nguồn (source / 소스) và chuẩn bị những structures cần thiết để resolve identifiers, functions, imports, lexical bindings và điều khiển (control / 제어) luồng (flow / 흐름). Specification mô tả việc này bằng nhiều thuật ngữ formal như **thực thi (execution / 실행) ngữ cảnh (context / 맥락)**, **môi trường (environment / 환경) bản ghi (record / 레코드)**, **Lexical môi trường (environment / 환경)**, **mô-đun (module / 모듈) môi trường (environment / 환경) bản ghi (record / 레코드)** và các declaration-instantiation algorithms.

Ở mức practical mô hình tư duy (mental model / 사고 모델), có thể nghĩ thành hai pha lớn:

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

Đây là nền tảng để hiểu hoisting. “Hoisting” không phải engine cắt dòng `function` hoặc `var` rồi kéo chúng lên đầu tệp (file / 파일). Đó chỉ là cách nói lịch sử dễ nhớ. Chính xác hơn, **bindings được tạo trong quá trình môi trường (environment / 환경)/declaration setup trước khi statement evaluation đi qua vị trí nguồn (source / 소스) tương ứng**, nhưng từng loại declaration được khởi tạo khác nhau.

Hàm (function / 함수) declaration có hàm (function / 함수) đối tượng (object / 객체) sẵn sớm, vì vậy thường gọi trước textual declaration được:

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

không giống lỗi “variable chưa tồn tại”. Ngược lại `let`, `const` và `class` có lexical bindings nhưng chưa được initialized cho đến khi thực thi (execution / 실행) đạt declaration. Khoảng thời gian binding đã tồn tại nhưng chưa thể truy cập (access / 접근) được gọi là **Temporal Dead Zone (TDZ)**.

```js
console.log(value); // ReferenceError
const value = 10;
```

Mô hình tư duy (mental model / 사고 모델) này tốt hơn câu “`let` không hoist”, vì lexical declarations thực sự tham gia môi trường (environment / 환경) creation; điều khác biệt là **trạng thái initialization**.

### Ngăn xếp lời gọi (call stack / 호출 스택) và thực thi (execution / 실행) ngữ cảnh (context / 맥락)

Mỗi hàm (function / 함수) lời gọi (call / 호출) tạo một thực thi (execution / 실행) ngữ cảnh (context / 맥락) mới và được đặt lên ngăn xếp lời gọi (call stack / 호출 스택):

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

Khi `c()` return, ngữ cảnh (context / 맥락) của `c` rời ngăn xếp (stack / 스택); thực thi (execution / 실행) quay lại `b`. JavaScript synchronous thực thi (execution / 실행) về cơ bản đi theo ngăn xếp (stack / 스택) này. Infinite recursion làm ngăn xếp (stack / 스택) tăng cho đến giới hạn thời gian chạy (runtime / 런타임).

Điều cần nhớ là **ngăn xếp lời gọi (call stack / 호출 스택) không phải vòng lặp sự kiện (event loop / 이벤트 루프)**. ngăn xếp lời gọi (call stack / 호출 스택) biểu diễn synchronous lời gọi (call / 호출) chuỗi (chain / 사슬) đang chạy. vòng lặp sự kiện (event loop / 이벤트 루프) là cơ chế host dùng để quyết định **khi nào một tác vụ (task / 작업) hoặc continuation mới được phép đưa JavaScript quay lại chạy trên ngăn xếp (stack / 스택)**.

---

# 3. Lexical môi trường (environment / 환경), phạm vi (scope / 범위) chuỗi (chain / 사슬) và Closure thực chất là một hệ thống duy nhất

Phạm vi (scope / 범위), lexical môi trường (environment / 환경) và closure thường được học thành ba bài riêng, nhưng chúng mô tả cùng một cơ chế ở các góc nhìn khác nhau.

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

Khi `createCounter()` chạy, môi trường (environment / 환경) của lời gọi (call / 호출) đó chứa binding `count`. hàm (function / 함수) `increment` được tạo trong lexical ngữ cảnh (context / 맥락) đó, nên hàm (function / 함수) giữ khả năng resolve `count` qua outer lexical môi trường (environment / 환경). Sau khi `createCounter()` return, thực thi (execution / 실행) ngữ cảnh (context / 맥락) đã rời ngăn xếp lời gọi (call stack / 호출 스택), nhưng môi trường (environment / 환경) cần cho returned hàm (function / 함수) vẫn còn reachable. Đó chính là closure.

Điểm này giúp sửa một hiểu nhầm quan trọng: **closure không có nghĩa “toàn bộ ngăn xếp (stack / 스택) frame được đóng băng mãi mãi”**. thời gian chạy (runtime / 런타임) chỉ phải giữ những môi trường (environment / 환경)/dữ liệu (data / 데이터) còn reachable theo ngữ nghĩa (semantics / 의미론). hiện thực (implementation / 구현) chi tiết có thể được engine tối ưu mạnh miễn hành vi (behavior / 동작) quan sát được vẫn đúng.

Closure trở thành vấn đề bộ nhớ (memory / 메모리) khi vòng đời (lifecycle / 생명주기) của hàm (function / 함수) dài hơn dự kiến và nó giữ tham chiếu (reference / 참조) tới dữ liệu (data / 데이터)/tài nguyên (resource / 자원) lớn:

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

Nếu cleanup không xảy ra, listener giữ `handler`, closure giữ `hugeData`, nên đối tượng (object / 객체) vẫn reachable. Đây là điểm nối trực tiếp giữa **closure → reachability → garbage collection → tài nguyên (resource / 자원) vòng đời (lifecycle / 생명주기)**.

---

# 4. `this`, tham chiếu (reference / 참조) ngữ nghĩa (semantics / 의미론) và lý do detached phương thức (method / 메서드) mất receiver

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

Expression `user.greet` trong một direct phương thức (method / 메서드) lời gọi (call / 호출) vẫn mang đủ thông tin để lời gọi (call / 호출) thao tác (operation / 연산) biết receiver/cơ sở (base / 기반) đối tượng (object / 객체) là `user`. Vì vậy `this` được set thành `user`.

Nhưng:

```js
const greet = user.greet;
greet();
```

Hàm (function / 함수) giá trị (value / 값) đã bị tách khỏi property-reference relationship ban đầu. lời gọi (call / 호출) mới là plain hàm (function / 함수) lời gọi (call / 호출); receiver `user` không còn tự động được giữ.

Đây là nguyên nhân sâu của nhiều bug callback legacy:

```js
button.addEventListener("click", user.greet);
```

Nếu `greet` cần `this === user`, cần bind hoặc wrapper có chủ đích:

```js
const onClick = user.greet.bind(user);
button.addEventListener("click", onClick);
```

Arrow functions giải quyết một bài toán (problem / 문제) khác: chúng **không tạo own động (dynamic / 동적) `this`**, mà sử dụng lexical `this` từ surrounding ngữ cảnh (context / 맥락). ES2015 thêm arrow cú pháp (syntax / 문법) không chỉ để mã (code / 코드) ngắn hơn; nó giải quyết một pain điểm (point / 지점) rất phổ biến của callback-heavy JavaScript trước ES2015.

Legacy mã (code / 코드) thường thấy:

```js
var self = this;

setTimeout(function () {
  self.refresh();
}, 1000);
```

Hiện đại (modern / 현대적) equivalent khi ngữ nghĩa (semantics / 의미론) phù hợp:

```js
setTimeout(() => {
  this.refresh();
}, 1000);
```

Đây là ví dụ quan trọng về **evolution có động cơ**, không chỉ là cú pháp (syntax / 문법) mới.

---

# 5. Prototype chuỗi (chain / 사슬) và lớp (class / 클래스) cú pháp (syntax / 문법) — JavaScript không biến thành Java ở ES2015

JavaScript là prototype-based ngôn ngữ (language / 언어). Khi đọc:

```js
user.greet
```

Thời gian chạy (runtime / 런타임) trước hết tìm own thuộc tính (property / 속성). Nếu không có, lookup đi lên nội bộ (internal / 내부) prototype chuỗi (chain / 사슬) cho đến khi tìm thấy thuộc tính (property / 속성) hoặc gặp `null`.

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

Prototype chuỗi (chain / 사슬):

```text
user
  ↓
User.prototype
  ↓
Object.prototype
  ↓
null
```

ES2015 lớp (class / 클래스) cú pháp (syntax / 문법):

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

làm cú pháp (syntax / 문법) dễ đọc và gần lớp trừu tượng (abstraction / 추상화) lớp (class / 클래스) quen thuộc hơn, nhưng phương thức (method / 메서드) vẫn nằm trên prototype và inheritance vẫn xây trên prototype machinery. Vì vậy câu “ES6 đưa OOP vào JavaScript” là không chính xác; JavaScript đã có đối tượng (object / 객체)/prototype inheritance từ trước. ES2015 chủ yếu cung cấp **cú pháp (syntax / 문법) chuẩn, rõ và dễ tooling hơn** cho mẫu (pattern / 패턴) constructor/prototype đã phổ biến.

Hiện đại (modern / 현대적) lớp (class / 클래스) tiếp tục được mở rộng với công khai (public / 공개) fields, `#private` fields/methods và static blocks ở ES2022. Chúng giải quyết những pain points thực tế như thời gian chạy (runtime / 런타임) privacy và initialization rõ ràng, chứ không thay nền prototype.

---

# 6. tác vụ (task / 작업), microtask và rendering — thứ tự async phải được hiểu như một timeline

Trình duyệt (browser / 브라우저) JavaScript thường chạy UI lô-gic (logic / 논리) trên main luồng thực thi (thread / 스레드). Khi synchronous ngăn xếp (stack / 스택) trống, trình duyệt (browser / 브라우저)/vòng lặp sự kiện (event loop / 이벤트 루프) có thể lấy công việc (work / 작업) tiếp theo. Một mô hình tư duy (mental model / 사고 모델) hữu ích cho một turn là:

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

`Promise.then(...)` và `queueMicrotask(...)` schedule microtasks. Timer callback là một tác vụ (task / 작업) ở một tác vụ (task / 작업) nguồn (source / 소스) thích hợp. Sau hiện tại (current / 현재) synchronous thực thi (execution / 실행), microtask hàng đợi (queue / 큐) được drain trước khi timer tác vụ (task / 작업) có cơ hội chạy.

Điều quan trọng không chỉ là thuộc đầu ra (output / 출력). Hãy hiểu hậu quả:

```js
function loop() {
  queueMicrotask(loop);
}

loop();
```

Một chuỗi (chain / 사슬) microtasks không kết thúc có thể **starve** trình duyệt (browser / 브라우저) khỏi cơ hội xử lý tác vụ (task / 작업) khác hoặc kết xuất (render / 렌더링). Vì vậy “microtask chạy sớm hơn” không có nghĩa “microtask luôn tốt hơn”.

### `await` nằm ở đâu?
Phần này nối mạch bài học với “`await` nằm ở đâu?”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
async function run() {
  console.log("before");
  await Promise.resolve();
  console.log("after");
}
```

`await` không khối (block / 블록) main luồng thực thi (thread / 스레드) kiểu sleep. Async hàm (function / 함수) tạm dừng; continuation sau `await` được schedule theo Promise-job/microtask ngữ nghĩa (semantics / 의미론). Đây là lý do synchronous mã (code / 코드) bên ngoài có thể chạy trước phần `after`.

### Rendering không phải ECMAScript ngữ nghĩa (semantics / 의미론)

ECMAScript định nghĩa Promise jobs và ngôn ngữ (language / 언어) hành vi (behavior / 동작); trình duyệt (browser / 브라우저) HTML tiêu chuẩn (standard / 표준) định nghĩa vòng lặp sự kiện (event loop / 이벤트 루프)/kết xuất (render / 렌더링) tích hợp (integration / 통합). `requestAnimationFrame`, DOM sự kiện (event / 이벤트) dispatch và rendering opportunities là host/trình duyệt (browser / 브라우저) concepts. Đây là ranh giới cần giữ rõ khi nói “JavaScript vòng lặp sự kiện (event loop / 이벤트 루프)”.

---

# 7. Promise resolution sâu hơn — Promise không chỉ là callback có `.then()`

Promise được thêm vào ES2015 để chuẩn hóa một lớp trừu tượng (abstraction / 추상화) async mà ecosystem trước đó đã tự xây bằng callbacks, Deferred objects và nhiều Promise libraries khác nhau.

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

Promise chuỗi (chain / 사슬) biến phụ thuộc (dependency / 의존성) thành composition:

```js
loadUser()
  .then((user) => loadOrders(user.id))
  .then(renderOrders)
  .catch(handleError);
```

`async/await` ở ES2017 sau đó làm cú pháp (syntax / 문법) sequential-looking hơn:

```js
try {
  const user = await loadUser();
  const orders = await loadOrders(user.id);
  renderOrders(orders);
} catch (error) {
  handleError(error);
}
```

Nhưng `async/await` **không thay Promise mô hình (model / 모델)**. Async hàm (function / 함수) trả Promise; `await` dùng Promise/thenable assimilation ngữ nghĩa (semantics / 의미론); errors sau await vẫn trở thành rejected async kết quả (result / 결과).

Một detail Master quan trọng là thenable assimilation:

```js
const thenable = {
  then(resolve) {
    resolve(42);
  }
};

const value = await thenable;
```

Không cần đối tượng (object / 객체) phải là bản địa (native / 네이티브) Promise; Promise resolution có thể assimilate đối tượng (object / 객체) có callable `then`. Đây là khả năng interoperability mạnh, nhưng cũng có nghĩa getter/`then` từ untrusted đối tượng (object / 객체) có thể chạy mã (code / 코드).

---

# 8. mô-đun (module / 모듈) hệ thống (system / 시스템) — vì sao ES Modules xuất hiện và nó khác IIFE/CommonJS ở đâu

Trước bản địa (native / 네이티브) modules, trình duyệt (browser / 브라우저) mã (code / 코드) thường dùng toàn cục (global / 전역) scripts và IIFE:

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

Nút (node / 노드) ecosystem phổ biến CommonJS:

```js
const userService = require("./user-service");
module.exports = createController;
```

Các patterns này giải quyết vấn đề thật, nhưng phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) không phải lúc nào cũng statically analyzable. ES2015 modules đưa `import`/`export` vào ngôn ngữ (language / 언어):

```js
import { loadUser } from "./user-service.js";

export function start() {
  return loadUser();
}
```

Static imports cho tooling/bundlers biết phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) trước khi chạy mô-đun (module / 모듈), hỗ trợ phân tích (analysis / 분석), cây (tree / 트리) shaking và tooling tốt hơn. mô-đun (module / 모듈) phạm vi (scope / 범위) cũng tránh việc declarations tự động trở thành globals và mô-đun (module / 모듈) mã (code / 코드) chạy theo strict-mode ngữ nghĩa (semantics / 의미론).

Imports là **live bindings**, không phải bản sao (copy / 복사) snapshot đơn giản. Circular mô-đun (module / 모듈) graphs hợp lệ nhưng initialization thứ tự (order / 순서) có thể gây temporal truy cập (access / 접근) problems. Vì vậy circular phụ thuộc (dependency / 의존성) nên được xem trước hết là một thiết kế (design / 설계) tín hiệu (signal / 신호).

Động (dynamic / 동적) `import()` ở ES2020 giải quyết nhu cầu phụ thuộc (dependency / 의존성) không cần tải (load / 로드) eagerly:

```js
const editor = await import("./heavy-editor.js");
```

Tuy nhiên “động (dynamic / 동적) import tạo chunk riêng” là bundler hành vi (behavior / 동작), không phải promise của ECMAScript specification.

Top-level `await` ở ES2022 làm mô-đun (module / 모듈) initialization có thể async, nhưng cũng có thể trì hoãn dependent mô-đun (module / 모듈) đồ thị (graph / 그래프). Dùng khi module-level phụ thuộc (dependency / 의존성) thực sự cần, không phải thay mọi startup hàm (function / 함수) bằng top-level await.

---

# 9. ES5 → ES2015 → hiện đại (modern / 현대적) ECMAScript — học bằng vấn đề, không học bản phát hành (release / 릴리스) notes

Phiên bản (version / 버전) evolution có ý nghĩa nhất khi hỏi: **nhà phát triển (developer / 개발자) lúc đó đang gặp vấn đề gì, và tính năng (feature / 기능) mới làm mã (code / 코드) rõ hơn hoặc an toàn hơn thế nào?**

## ES5 — chuẩn hóa nền JavaScript web trước thời hiện đại (modern / 현대적) cú pháp (syntax / 문법)

ES5 (2009) là một mốc lớn vì nó củng cố JavaScript đã được dùng rộng rãi trên web: strict chế độ (mode / 모드), JSON hỗ trợ (support / 지원), thuộc tính (property / 속성) descriptors/reflection và nhiều array helpers như `map`, `filter`, `reduce`, `forEach`, `some`, `every` trở thành nền tảng chuẩn.

Legacy ES5-style mã (code / 코드) thường có:

```js
var names = users
  .filter(function (user) {
    return user.active;
  })
  .map(function (user) {
    return user.name;
  });
```

Mã (code / 코드) này không “sai” chỉ vì cũ. hiện đại (modern / 현대적) cú pháp (syntax / 문법) có thể làm intent ngắn hơn:

```js
const names = users
  .filter((user) => user.active)
  .map((user) => user.name);
```

Điểm thay đổi thật nằm ở lexical bindings và arrow ngữ nghĩa (semantics / 의미론), không chỉ số ký tự.

> **Chuyển mạch:** ES5 đặt baseline web semantics; ES2015/ES6 thay đổi module, class, iterator và async foundations để ứng dụng lớn có boundary rõ hơn. Yearly evolution tiếp theo đọc các capability mới trên baseline đó.

## ES2015/ES6 — bước chuyển sang JavaScript cho ứng dụng (application / 애플리케이션) lớn

ES2015 là bước nhảy lớn nhất của hiện đại (modern / 현대적) JavaScript. Những tính năng (feature / 기능) như `let`/`const`, classes, modules, Promise, destructuring, rest/spread, Map/Set, Symbol, iterator/generator và arrow functions cùng xuất hiện vì ecosystem cần mã (code / 코드) dễ tổ chức hơn cho ứng dụng (application / 애플리케이션)/thư viện (library / 라이브러리) lớn.

Một số legacy → hiện đại (modern / 현대적) mappings nên hiểu theo động cơ:

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

Không phải mọi legacy form đều phải rewrite. `function` vẫn cần khi động (dynamic / 동적) `this` phù hợp; đối tượng (object / 객체) vẫn tốt cho record-shaped dữ liệu (data / 데이터); ordinary loops vẫn rõ hơn functional chains trong nhiều algorithms.

> **Chuyển mạch:** Sau ES2015, mỗi yearly release bổ sung capability nhỏ hơn nhưng vẫn có runtime/support boundary. `Array.fromAsync()` là một case cụ thể để đọc proposal status, behavior và compatibility cùng nhau.

## Sau ES2015 — yearly evolution nhỏ và đều hơn

Từ ES2016, ECMAScript chuyển sang yearly cadence. Tư duy đúng không phải “mỗi năm là một JavaScript mới”, mà là **ngôn ngữ (language / 언어) được bổ sung incremental**. Những bổ sung đáng nhớ thường giảm boilerplate hoặc encode intent mà nhà phát triển (developer / 개발자) trước đó phải tự viết.

Ví dụ `async/await` (ES2017) làm Promise-based sequential luồng (flow / 흐름) dễ đọc. đối tượng (object / 객체) rest/spread (ES2018) làm immutable-style đối tượng (object / 객체) transformations ergonomic hơn. Optional chaining và nullish coalescing (ES2020) làm optional truy cập (access / 접근)/default ngữ nghĩa (semantics / 의미론) rõ hơn. lớp (class / 클래스) fields/private elements và top-level await (ES2022) mở rộng lớp (class / 클래스)/mô-đun (module / 모듈) mô hình (model / 모델). Copying array methods như `toSorted()` (ES2023) giải quyết nhu cầu non-mutating collection updates. `Promise.withResolvers()`, `Object.groupBy()` và resizable ArrayBuffer facilities (ES2024) chuẩn hóa recurring patterns. Iterator Helpers, Set operations, `RegExp.escape()` và `Promise.try()` (ES2025) tiếp tục đưa dùng chung (common / 공통) thư viện (library / 라이브러리) patterns vào tiêu chuẩn (standard / 표준).

Không cần thuộc danh sách này. Cần nhớ **bài toán (problem / 문제) → lớp trừu tượng (abstraction / 추상화) mới → tính tương thích (compatibility / 호환성)**.

---

# 10. ECMAScript 2026 — những bổ sung nào đáng biết và tại sao chúng xuất hiện

ECMAScript 2026 là 17th edition. Không nên biến học tập (learning / 학습) notes thành changelog, nhưng một vài additions minh họa rất rõ cách hiện đại (modern / 현대적) ECMAScript tiếp tục chuẩn hóa recurring patterns.

> **Chuyển mạch:** Yearly cadence cung cấp capability mới để giải quyết recurring patterns; `Array.fromAsync()` minh họa async collection semantics. `Math.sumPrecise()` tiếp theo xử lý một vấn đề khác: numeric precision và error bounds.

## `Array.fromAsync()`

Trước đây để collect async iterable thành array, bạn thường phải tự vòng lặp (loop / 루프):

```js
const result = [];

for await (const item of source) {
  result.push(item);
}
```

`Array.fromAsync()` cung cấp built-in lớp trừu tượng (abstraction / 추상화) cho async iterables và async sources:

```js
const result = await Array.fromAsync(source);
```

Điểm mới không phải async iteration — nó đã có từ trước — mà là **collection constructor có hiểu async nguồn (source / 소스)**.

> **Chuyển mạch:** `Array.fromAsync()` thu các async iterable thành mảng; `Math.sumPrecise()` đặt lại câu hỏi về ngữ nghĩa cộng số; `Iterator.concat()` tiếp tục thay đổi cách ghép iterator lười. Đọc liền ba mục để theo dõi ranh giới collection → numeric precision → lazy composition.

## `Math.sumPrecise()`

Cộng floating-point values có thể tích lũy precision lỗi (error / 오류), đặc biệt khi magnitude khác nhau. ES2026 thêm một thao tác (operation / 연산) chuẩn để sum iterable Numbers theo cách giảm precision mất mát (loss / 손실) so với naive accumulation trong nhiều trường hợp.

Điều này không biến IEEE-754 thành decimal arithmetic; financial mã (code / 코드) vẫn cần lĩnh vực (domain / 도메인) chiến lược (strategy / 전략) riêng.

> **Chuyển mạch:** Ở chặng này của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Iterator.concat()** tiếp nhận điểm tựa từ **Math.sumPrecise()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Error.isError()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Iterator.concat()`

Sau Iterator Helpers ES2025, `Iterator.concat()` tiếp tục làm lazy iteration pipelines dễ compose hơn mà không phải tự viết generator chỉ để nối nhiều iterables.

Legacy mẫu (pattern / 패턴):

```js
function* concat(...iterables) {
  for (const iterable of iterables) {
    yield* iterable;
  }
}
```

Hiện đại (modern / 현대적) built-in giảm boilerplate khi thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Error.isError()** tiếp nhận điểm tựa từ **Iterator.concat()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Map/WeakMap get-or-insert operations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Error.isError()`

Cross-realm lỗi (error / 오류) detection là một pain điểm (point / 지점) vì:

```js
errorFromIframe instanceof Error
```

có thể thất bại (fail / 실패) khi constructors thuộc khác Realm. `Error.isError()` cung cấp standardized error-object detection tốt hơn cho các trường hợp này.

> **Chuyển mạch:** Trong **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Map/WeakMap get-or-insert operations** tiếp nhận điểm tựa từ **Error.isError()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Uint8Array ↔ Base64/Hex** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Map`/`WeakMap` get-or-insert operations

Một mẫu (pattern / 패턴) bộ nhớ đệm (cache / 캐시)/chỉ mục (index / 인덱스) quen thuộc:

```js
let value = map.get(key);

if (value === undefined) {
  value = createValue(key);
  map.set(key, value);
}
```

có trường hợp biên (edge case / 경계 사례) nếu `undefined` là stored giá trị (value / 값) hợp lệ và tạo boilerplate repeated. ES2026 chuẩn hóa get-or-insert style operations để express “lấy nếu có, nếu không tạo/default rồi lưu” rõ hơn.

> **Chuyển mạch:** Ở chặng này của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Uint8Array ↔ Base64/Hex** tiếp nhận điểm tựa từ **Map/WeakMap get-or-insert operations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **JSON nguồn (source / 소스)/raw facilities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `Uint8Array` ↔ Base64/Hex

Mã (code / 코드) web trước đây thường phải đi qua `btoa`/`atob`, manual byte loops hoặc utility thư viện (library / 라이브러리) để chuyển nhị phân (binary / 이진) bytes sang hex/base64. ES2026 bổ sung built-in conversion methods trực tiếp quanh `Uint8Array`, phù hợp hơn với nhị phân (binary / 이진) mô hình dữ liệu (data model / 데이터 모델) hiện đại và tránh nhiều binary-string pitfalls của APIs lịch sử.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Uint8Array ↔ Base64/Hex** nêu điều cần giải thích; **JSON nguồn (source / 소스)/raw facilities** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **IIFE thay module scope** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## JSON nguồn (source / 소스)/raw facilities

ES2026 bổ sung khả năng reviver của `JSON.parse()` tiếp cận nguồn (source / 소스) ngữ cảnh (context / 맥락) và `JSON.rawJSON()` để kiểm soát thành phần nguyên thủy (primitive / 기본 요소) JSON đầu ra (output / 출력) ở mức thấp hơn. Đây là advanced serialization tính năng (feature / 기능), hữu ích khi chính xác (exact / 정확한) numeric/nguồn (source / 소스) biểu diễn (representation / 표현) quan trọng; ordinary ứng dụng (application / 애플리케이션) JSON không cần đổi cách viết chỉ vì API mới tồn tại.

### Tính tương thích (compatibility / 호환성) quy tắc (rule / 규칙)

“Thuộc ES2026” không có nghĩa WebView môi trường vận hành (production / 운영 환경) của bạn đã có API. Với dự án (project / 프로젝트) hybrid/WebSquare, luôn kiểm tra Android hệ thống (system / 시스템) WebView và WKWebView versions thực tế trước khi dùng built-in mới mà không fallback.

---

# 11. mô hình đối tượng (object model / 객체 모델) sâu hơn — descriptors, exotic objects và Proxy invariants

Plain đối tượng (object / 객체) thuộc tính (property / 속성) không chỉ là `key → value`. dữ liệu (data / 데이터) thuộc tính (property / 속성) còn có descriptor flags `writable`, `enumerable`, `configurable`; accessor thuộc tính (property / 속성) có `get`, `set`, `enumerable`, `configurable`.

```js
const user = {};

Object.defineProperty(user, "id", {
  value: "u1",
  writable: false,
  enumerable: false,
  configurable: false
});
```

Nhiều built-ins không có hoàn toàn ordinary đối tượng (object / 객체) hành vi (behavior / 동작). Specification dùng khái niệm **exotic objects** cho những objects có nội bộ (internal / 내부) phương thức (method / 메서드) hành vi (behavior / 동작) đặc biệt, ví dụ Arrays, TypedArrays, String objects, mô-đun (module / 모듈) không gian tên (namespace / 네임스페이스) objects, some `arguments` objects và Proxies.

Array là ví dụ dễ thấy: `length` không phải thuộc tính (property / 속성) bình thường hoàn toàn.

```js
const values = [10, 20, 30];
values.length = 1;

console.log(values); // [10]
```

Setting smaller length có thể delete indexed elements.

Sparse array hole cũng khác tường minh (explicit / 명시적) `undefined`:

```js
const sparse = [,];
const explicit = [undefined];

0 in sparse;   // false
0 in explicit; // true
```

Proxy cho phép intercept đối tượng (object / 객체) nội bộ (internal / 내부) operations:

```js
const proxy = new Proxy(target, {
  get(target, key, receiver) {
    return Reflect.get(target, key, receiver);
  }
});
```

Nhưng Proxy không được “nói dối tùy ý”. Specification có **invariants** quanh non-configurable properties, prototype/extensibility và descriptors. Vi phạm bất biến (invariant / 불변식) có thể throw `TypeError`. Đây là lý do reactivity/metaprogramming thư viện (library / 라이브러리) author phải hiểu descriptors và đối tượng (object / 객체) internals chứ không chỉ thuộc trap names.

---

# 12. Equality algorithms và coercion ở mức (level / 수준) specification

Beginner đã học `==`, `===`, `Object.is()`. Master cần biết JavaScript có nhiều equality algorithms vì các APIs cần ngữ nghĩa (semantics / 의미론) khác nhau.

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

Coercion cũng nên được hiểu qua nội bộ (internal / 내부) conversion concepts như `ToPrimitive`, `ToNumber`, `ToString`, `ToBoolean`, `ToPropertyKey` thay vì học câu đố.

Đối tượng (object / 객체) có thể customize thành phần nguyên thủy (primitive / 기본 요소) conversion:

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

Mục tiêu của kiến thức (knowledge / 지식) này là gỡ lỗi (debug / 디버그) thư viện (library / 라이브러리)/edge cases, không phải viết môi trường vận hành (production / 운영 환경) mã (code / 코드) dựa trên clever implicit coercion.

---

# 13. nhị phân (binary / 이진) dữ liệu (data / 데이터) — ArrayBuffer, TypedArray và DataView

JSON/string không phải biểu diễn (representation / 표현) phù hợp cho mọi dữ liệu (data / 데이터). ảnh (image / 이미지) bytes, crypto, compression, WebSocket nhị phân (binary / 이진) giao thức (protocol / 프로토콜) và tệp (file / 파일) parsing thường dùng nhị phân (binary / 이진) primitives.

`ArrayBuffer` là raw byte lưu trữ (storage / 저장소):

```js
const buffer = new ArrayBuffer(16);
```

TypedArray là typed view:

```js
const bytes = new Uint8Array(buffer);
const numbers = new Int32Array(buffer);
```

Hai views có thể nhìn cùng backing buffer nhưng interpret bytes khác nhau.

`DataView` phù hợp khi nhị phân (binary / 이진) giao thức (protocol / 프로토콜) có fields khác nhau và cần kiểm soát endianness:

```js
const view = new DataView(buffer);
view.setUint32(0, 123456, true);
```

`true` ở đây yêu cầu little-endian.

Một kiến trúc (architecture / 아키텍처) tốt tách:

```text
network/file bytes
↓
decoder
↓
validated transport object
↓
domain model
```

Không để nhị phân (binary / 이진) offsets/endianness tràn vào lô-gic nghiệp vụ (business logic / 비즈니스 로직).

---

# 14. Unicode và internationalization — `string.length` không phải “số ký tự người dùng nhìn thấy”

JavaScript string dựa trên UTF-16 mã (code / 코드) units. Một emoji có thể chiếm nhiều mã (code / 코드) units:

```js
"😀".length; // thường là 2
```

Vì vậy cần phân biệt **mã (code / 코드) đơn vị (unit / 단위)**, **mã (code / 코드) điểm (point / 지점)** và **grapheme cluster**. `for...of` trên string xử lý mã (code / 코드) points tốt hơn vòng lặp (loop / 루프) theo UTF-16 chỉ mục (index / 인덱스) trong nhiều trường hợp, nhưng grapheme clusters phức tạp vẫn cần segmentation-aware lô-gic (logic / 논리).

`Intl` cung cấp locale-aware formatting/sorting/segmentation:

```js
const currency = new Intl.NumberFormat("ko-KR", {
  style: "currency",
  currency: "KRW"
});

currency.format(1000000);
```

`Intl.DateTimeFormat`, `Intl.Collator`, `Intl.PluralRules`, `Intl.RelativeTimeFormat` và `Intl.Segmenter` giải quyết những vấn đề mà manual formatting bằng string concatenation rất dễ sai.

Quy tắc (rule / 규칙) môi trường vận hành (production / 운영 환경): **locale/date/currency ngữ nghĩa (semantics / 의미론) là lĩnh vực (domain / 도메인) concern**, không phải cosmetic detail.

---

# 15. RegExp advanced — statefulness, Unicode và bảo mật (security / 보안)

RegExp có thể mang mutable trạng thái (state / 상태) khi dùng flags như `g` hoặc `y` thông qua `lastIndex`.

```js
const pattern = /a/g;

pattern.test("a");
pattern.lastIndex;
```

Reuse same RegExp instance mà không hiểu `lastIndex` có thể tạo bugs khó thấy.

Động (dynamic / 동적) regex từ người dùng (user / 사용자) đầu vào (input / 입력) là bảo mật (security / 보안) concern. ES2025 thêm `RegExp.escape()` để biến arbitrary văn bản (text / 텍스트) thành literal-safe fragment cho RegExp:

```js
const regex = new RegExp(RegExp.escape(keyword), "i");
```

Trước đó codebase thường có custom escape helpers. Khi mục tiêu (target / 대상) thời gian chạy (runtime / 런타임) cũ chưa hỗ trợ (support / 지원), dùng maintained polyfill/helper phù hợp thay vì tự escape vài characters và tưởng đã an toàn.

Một bảo mật (security / 보안) lớp (class / 클래스) khác là **ReDoS**: mẫu (pattern / 패턴) có catastrophic backtracking có thể tiêu tốn CPU với crafted đầu vào (input / 입력). Regex bảo mật (security / 보안) không chỉ là escaping.

---

# 16. bộ nhớ (memory / 메모리), garbage collection và reachability — nối với closure, DOM và bộ nhớ đệm (cache / 캐시)

Garbage collector không biết nghiệp vụ (business / 비즈니스) đã “xong với đối tượng (object / 객체)”. Nó chỉ quan tâm đối tượng (object / 객체) còn reachable từ roots hay không.

Dùng chung (common / 공통) accidental reachability paths:

```text
global → cache → old data
window → listener → closure → large object
DOM/runtime → detached node → handler → state
interval → callback → service → page state
pending async operation → continuation → captured data
```

Đây là lý do cleanup phải theo quyền sở hữu (ownership / 소유권).

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

WeakMap/WeakSet hữu ích khi siêu dữ liệu (metadata / 메타데이터)/bộ nhớ đệm (cache / 캐시) thời gian tồn tại (lifetime / 수명) nên phụ thuộc key reachability. WeakRef/FinalizationRegistry là niche tools; tính đúng đắn (correctness / 정확성) không được phụ thuộc vào GC timing.

GC hiện thực (implementation / 구현) có thể generational, incremental, concurrent và thay đổi theo engine phiên bản (version / 버전). ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) nên học **reachability, allocation tỷ lệ (rate / 비율), thời gian tồn tại (lifetime / 수명) và profiler bằng chứng (evidence / 증거)**, không optimize theo một GC blog cũ.

---

# 17. trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) không phải chỉ ECMAScript

Trình duyệt (browser / 브라우저) ứng dụng (application / 애플리케이션) chạy trên nhiều lớp:

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

`fetch`, DOM, Web lưu trữ (storage / 저장소), Web Workers, `AbortController`, `BroadcastChannel`, `requestAnimationFrame`, Trusted Types và Web Locks không phải ECMA-262 APIs. Chúng có specifications và tính tương thích (compatibility / 호환성) timelines riêng.

Điều này đặc biệt quan trọng với hybrid app. Chrome desktop mới nhất hỗ trợ (support / 지원) một Web API không có nghĩa Android WebView mà app đang ship cũng hỗ trợ (support / 지원). Và iOS WKWebView phiên bản (version / 버전) bị gắn với hệ điều hành/engine phân phối (distribution / 분포) khác Chrome.

### Compatibility matrix nên là project artifact
Phần này nối mạch bài học với “Compatibility matrix nên là project artifact”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

Không dùng `ES2026` như một proxy duy nhất cho trình duyệt (browser / 브라우저) năng lực (capability / 역량).

---

# 18. Toolchain — transpile, polyfill, bundle và thời gian chạy (runtime / 런타임) là bốn câu chuyện khác nhau

Hiện đại (modern / 현대적) frontend nguồn (source / 소스) có thể đi qua:

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

**Transpilation** đổi cú pháp (syntax / 문법). Optional chaining có thể được rewrite sang cú pháp (syntax / 문법) cũ.

**Polyfill** cung cấp thời gian chạy (runtime / 런타임) API còn thiếu như một built-in approximation.

**Bundler** resolve mô-đun (module / 모듈) đồ thị (graph / 그래프), split chunks, tiến trình (process / 프로세스) assets và perform cây (tree / 트리) shaking.

**thời gian chạy (runtime / 런타임)** cuối cùng quyết định nền tảng (platform / 플랫폼) APIs và engine hành vi (behavior / 동작) thực tế.

Vì vậy “Babel compile được” không chứng minh `structuredClone`, `RegExp.escape()` hoặc Web Worker tính năng (feature / 기능) nào đó tồn tại ở thời gian chạy (runtime / 런타임).

Cây (tree / 트리) shaking cũng không phải guarantee chỉ vì mã (code / 코드) dùng ES modules. Top-level side effects, động (dynamic / 동적) truy cập (access / 접근) và gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터) có thể ngăn dead-code elimination.

Nguồn (source / 소스) maps là môi trường vận hành (production / 운영 환경) khả năng quan sát (observability / 관측 가능성) công cụ (tool / 도구): chúng map generated/minified stacks về nguồn (source / 소스). Với sensitive nguồn (source / 소스), upload private nguồn (source / 소스) maps cho lỗi (error / 오류) dịch vụ (service / 서비스) thường tốt hơn công khai (public / 공개) serving.

---

# 19. Legacy JavaScript literacy — mã (code / 코드) cũ nên được đọc bằng lịch sử của ngôn ngữ

Enterprise các hệ thống (systems / 시스템들) thường chứa nhiều thế hệ JavaScript cùng lúc. cấp cao (senior / 시니어) nhà phát triển (developer / 개발자) không nên nhìn legacy cú pháp (syntax / 문법) rồi kết luận “mã (code / 코드) xấu” trước khi hiểu thời gian chạy (runtime / 런타임)/tooling các ràng buộc (constraints / 제약조건들) lúc nó được viết.

> **Chuyển mạch:** Trong **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **JSON nguồn (source / 소스)/raw facilities** nêu điều cần giải thích; **IIFE thay module scope** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **arguments thay rest parameters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IIFE thay module scope
Phần này nối mạch bài học với “IIFE thay module scope”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```js
(function () {
  var state = {};

  window.app = {
    start: function () {}
  };
})();
```

Hiện đại (modern / 현대적) equivalent thường là ES mô-đun (module / 모듈), nhưng IIFE từng là giải pháp đúng để tạo private phạm vi (scope / 범위) trong trình duyệt (browser / 브라우저) script world.

> **Chuyển mạch:** Ở chặng này của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **arguments thay rest parameters** tiếp nhận điểm tựa từ **IIFE thay module scope** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prototype constructor thay lớp (class / 클래스) cú pháp (syntax / 문법)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Hiện đại (modern / 현대적):

```js
function sum(...values) {
  return values.reduce((total, value) => total + value, 0);
}
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **Prototype constructor thay lớp (class / 클래스) cú pháp (syntax / 문법)** tiếp nhận điểm tựa từ **arguments thay rest parameters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **XMLHttpRequest / callback APIs thay fetch/Promise style** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prototype constructor thay lớp (class / 클래스) cú pháp (syntax / 문법)

Legacy constructor/prototype mã (code / 코드) không phải “fake lớp (class / 클래스)”; nó dùng prototype mô hình (model / 모델) trực tiếp. lớp (class / 클래스) cú pháp (syntax / 문법) chỉ cung cấp lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층) rõ hơn.

> **Chuyển mạch:** Trong **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **XMLHttpRequest / callback APIs thay fetch/Promise style** tiếp nhận điểm tựa từ **Prototype constructor thay lớp (class / 클래스) cú pháp (syntax / 문법)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CommonJS / bundler-specific modules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## XMLHttpRequest / callback APIs thay fetch/Promise style

Legacy trình duyệt (browser / 브라우저) mã (code / 코드) có thể dùng XHR/sự kiện (event / 이벤트) callbacks. hiện đại (modern / 현대적) fetch/Promise mã (code / 코드) composable hơn, nhưng di chuyển (migration / 마이그레이션) phải bảo toàn hết thời gian chờ (timeout / 타임아웃), cancellation, credentials, progress và lỗi (error / 오류) ngữ nghĩa (semantics / 의미론); không chỉ đổi API names.

> **Chuyển mạch:** Ở chặng này của **JavaScript Master Supplement — Hoàn thiện thư viện kiến thức (knowledge library / 지식 라이브러리) từ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) đến hiện đại (modern / 현대적) ECMAScript**, **CommonJS / bundler-specific modules** tiếp nhận điểm tựa từ **XMLHttpRequest / callback APIs thay fetch/Promise style** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## CommonJS / bundler-specific modules

Nút (node / 노드)/legacy bản dựng (build / 빌드) các hệ thống (systems / 시스템들) có thể dùng `require`, AMD hoặc UMD. ESM di chuyển (migration / 마이그레이션) cần hiểu gói (package / 패키지)/thời gian chạy (runtime / 런타임) resolution, không chỉ tìm kiếm (search / 검색)/replace `require` thành `import`.

Mastery gồm khả năng **đọc mã (code / 코드) cũ, hiểu lý do lịch sử, rồi modernize theo hành vi (behavior / 동작) chứ không theo cú pháp (syntax / 문법) fashion**.

---

# 20. bảo mật (security / 보안) ở mức (level / 수준) Master — dấu vết (trace / 추적) luồng dữ liệu (data flow / 데이터 흐름) và năng lực (capability / 역량)

Thay vì học attack names rời rạc, dấu vết (trace / 추적):

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

Sources có thể là URL, form, API phản hồi (response / 응답), localStorage, `postMessage`, bản địa (native / 네이티브) callback hoặc third-party SDK. Sinks có thể là `innerHTML`, điều hướng (navigation / 내비게이션) URL, động (dynamic / 동적) đối tượng (object / 객체) key, `eval`, bản địa (native / 네이티브) cầu nối (bridge / 브리지) command, mạng (network / 네트워크) yêu cầu (request / 요청) hoặc logging hệ thống (system / 시스템).

### URL kiểm tra hợp lệ (validation / 검증)

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

Sau đó vẫn phải validate đường dẫn (path / 경로)/hành động (action / 동작) nếu privilege phụ thuộc chúng.

### `postMessage`

Receiver nên kiểm tra `origin`, expected `source`, lược đồ (schema / 스키마), message kiểu (type / 타입) và authorization/năng lực (capability / 역량). Check origin một mình không ngăn confused-deputy scenario nếu trusted sender bị lợi dụng để yêu cầu privileged hành động (action / 동작).

### Prototype/đối tượng (object / 객체) injection

Arbitrary bên ngoài (external / 외부) string không nên tự động trở thành phương thức (method / 메서드)/thuộc tính (property / 속성) năng lực (capability / 역량):

```js
handlers[userInput]();
```

Prefer allowlisted `Map`/validated discriminant.

### Bản địa (native / 네이티브) cầu nối (bridge / 브리지)

Cầu nối (bridge / 브리지) nên expose minimum năng lực (capability / 역량) surface. Một god-object kiểu `nativeBridge.execute(command, payload)` làm kiểm tra hợp lệ (validation / 검증)/authorization khó hơn tường minh (explicit / 명시적) APIs như `startKyc`, `closeKyc`, `openSecureDocument`.

---

# 21. hiệu năng (performance / 성능) — engine kiến thức (knowledge / 지식) chỉ có giá trị sau đo lường (measurement / 측정)

Engine có parser, trình thông dịch (interpreter / 인터프리터)/baseline compilation, profiling và JIT tối ưu hóa (optimization / 최적화) strategies. Concepts như shapes/hidden classes, inline caches và deoptimization giúp giải thích một số hành vi (behavior / 동작), nhưng môi trường vận hành (production / 운영 환경) tối ưu hóa (optimization / 최적화) phải bắt đầu từ user-visible bài toán (problem / 문제).

Correct tiến trình (process / 프로세스):

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

Main-thread UI hiệu năng (performance / 성능) thường bị ảnh hưởng nhiều hơn bởi long synchronous tasks, DOM/bố cục (layout / 레이아웃) công việc (work / 작업), serialization, mạng (network / 네트워크) waterfalls, large bundles và allocation churn so với micro-optimizing arithmetic cú pháp (syntax / 문법).

Bộ nhớ (memory / 메모리) profiling nên tìm **retainer đường dẫn (path / 경로)**, không chỉ nhìn đối tượng (object / 객체) count. CPU profiling nên tìm hot lời gọi (call / 호출) paths/flame-chart widths, không chỉ hàm (function / 함수) bạn nghi ngờ trước.

Cold-start và warm hành vi (behavior / 동작) cũng khác nhau: first tải (load / 로드) có parse/compile/mạng (network / 네트워크)/bộ nhớ đệm (cache / 캐시) costs mà repeated tương tác (interaction / 상호작용) không có.

---

# 22. Streams, workers và tính đồng thời (concurrency / 동시성) — JavaScript không đồng nghĩa “chỉ làm một việc”

Trình duyệt (browser / 브라우저) main-thread JavaScript thực thi (execution / 실행) thường single-threaded theo một tác nhân (agent / 에이전트), nhưng ứng dụng (application / 애플리케이션) có tính đồng thời (concurrency / 동시성) qua async I/O, multiple contexts và workers.

Web Workers cho CPU-heavy công việc (work / 작업) rời main luồng thực thi (thread / 스레드). Message passing mặc định dùng structured clone; Transferable objects có thể chuyển quyền sở hữu (ownership / 소유권) của certain buffers để tránh bản sao (copy / 복사) chi phí (cost / 비용).

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

Backpressure nghĩa producer không nên tiếp tục tạo dữ liệu (data / 데이터) vô hạn khi bên tiêu thụ (consumer / 소비자) xử lý chậm.

SharedArrayBuffer/Atomics cho dùng chung (shared / 공유) bộ nhớ (memory / 메모리) nhưng tăng lập luận (reasoning / 추론) độ phức tạp (complexity / 복잡도) mạnh. Nếu nhóm (team / 팀) không thể mô tả synchronization giao thức (protocol / 프로토콜) rõ ràng, message passing thường là kiến trúc (architecture / 아키텍처) an toàn hơn.

Bounded tính đồng thời (concurrency / 동시성) cũng quan trọng. `Promise.all(items.map(request))` trên 10.000 items có thể tạo 10.000 operations gần như cùng lúc. môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) thường cần pool/semaphore/tính đồng thời (concurrency / 동시성) limit.

---

# 23. lỗi (error / 오류) handling — từ `try/catch` tới lỗi (error / 오류) taxonomy và chuỗi nhân quả (causal chain / 인과 사슬)

`try/catch` chỉ là cú pháp (syntax / 문법). môi trường vận hành (production / 운영 환경) lỗi (error / 오류) thiết kế (design / 설계) cần phân biệt:

```text
programmer/invariant error
validation error
network failure
HTTP/domain failure
timeout/cancellation
external dependency failure
```

`Error.cause` (ES2022) giúp preserve chuỗi nhân quả (causal chain / 인과 사슬):

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

Lỗi (error / 오류) serialization cần tường minh (explicit / 명시적) vì `JSON.stringify(new Error(...))` thường không đưa `message`/`stack` như nhà phát triển (developer / 개발자) tưởng. Logging tầng (layer / 계층) cũng phải redact secrets và PII.

Expected nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) đôi khi nên được mô hình (model / 모델) như kết quả (result / 결과)/trạng thái (state / 상태) thay vì exception. Đây là kiến trúc (architecture / 아키텍처) quyết định (decision / 결정), không có quy tắc (rule / 규칙) “mọi thất bại (failure / 실패) đều throw”.

---

# 24. Serialization — JSON không phải universal đối tượng (object / 객체) cloning

JSON phù hợp vì portable và backend-friendly, nhưng nó không preserve mọi JavaScript biểu diễn (representation / 표현). `Date` trở thành string, BigInt không stringify trực tiếp theo ordinary hành vi (behavior / 동작), functions/undefined/cycles không được represent như đối tượng (object / 객체) đồ thị (graph / 그래프) gốc.

`structuredClone()` phù hợp hơn khi clone/transfer structured dữ liệu (data / 데이터) trong trình duyệt (browser / 브라우저) contexts và hỗ trợ nhiều built-ins/cycles hơn, nhưng nó không phải HTTP wire format.

`FormData`, `URLSearchParams` và nhị phân (binary / 이진) formats giải quyết những vận chuyển (transport / 전송) problems khác nhau. Chọn serialization dựa trên ranh giới (boundary / 경계) đặc tả hợp đồng (contract / 계약), không dựa vào thói quen “mọi thứ stringify JSON”.

---

# 25. Java/Spring interoperability — JavaScript kiểu (type / 타입) ngữ nghĩa (semantics / 의미론) gặp backend kiểu (type / 타입) ngữ nghĩa (semantics / 의미론)

Một frontend JavaScript môi trường vận hành (production / 운영 환경) thường không thể giả định Java types map 1:1 sang JavaScript.

Java/cơ sở dữ liệu (database / 데이터베이스) `long` hoặc BIGINT có thể vượt `Number.MAX_SAFE_INTEGER`. ID lớn thường nên serialize thành string nếu chính xác (exact / 정확한) integer định danh (identity / 식별자) quan trọng.

`BigDecimal` không nên đổi mù quáng sang `number` nếu lĩnh vực (domain / 도메인) cần decimal precision. Money có thể dùng decimal string hoặc minor-unit integer chiến lược (strategy / 전략).

Date/thời gian (time / 시간) cần phân biệt rõ:

```text
LocalDate
LocalDateTime
Instant
OffsetDateTime
ZonedDateTime
```

`LocalDateTime` không mang timezone/offset; `Instant` là absolute điểm (point / 지점). Wire format phải tường minh (explicit / 명시적).

Backend enum có thể thêm member mới. Frontend exhaustive lô-gic (logic / 논리) chỉ an toàn nếu bên ngoài (external / 외부) payload được validated/versioned và có forward-compatibility chiến lược (strategy / 전략).

`null`, missing trường dữ liệu (field / 필드) và empty string không nên được dùng lẫn nhau tùy endpoint; chúng phải có đặc tả hợp đồng (contract / 계약) rõ.

---

# 26. WebSquare và bản địa (native / 네이티브) WebView — khung phần mềm (framework / 프레임워크) ranh giới (boundary / 경계) phải được cô lập

Trong WebSquare codebase, một sự kiện (event / 이벤트) handler lớn dễ trộn DataMap/DataList, submission, bản địa (native / 네이티브) cầu nối (bridge / 브리지), UI trạng thái (state / 상태) và nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙). Master kiến trúc (architecture / 아키텍처) nên tách:

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

DataList/DataMap là hạ tầng (infrastructure / 인프라) biểu diễn (representation / 표현), không nên trở thành lĩnh vực (domain / 도메인) mô hình (model / 모델) ở mọi tầng (layer / 계층).

Bản địa (native / 네이티브) WebView communication nên có versioned message contracts:

```js
{
  version: 1,
  type: "KYC_COMPLETED",
  requestId: "abc",
  payload: { ... }
}
```

Đặc tả hợp đồng (contract / 계약) nên định nghĩa phiên bản (version / 버전), message kiểu (type / 타입), correlation/yêu cầu (request / 요청) ID, payload lược đồ (schema / 스키마), lỗi (error / 오류) lược đồ (schema / 스키마), hết thời gian chờ (timeout / 타임아웃)/cancellation và backward tính tương thích (compatibility / 호환성). Deep-link scheme như `ekyc://...` cũng phải parse/validate structured fields, không chỉ prefix check.

---

# 27. React interoperability — khung phần mềm (framework / 프레임워크) hành vi (behavior / 동작) vẫn dựa trên JavaScript ngữ nghĩa (semantics / 의미론)

React không thay thế JavaScript thời gian chạy (runtime / 런타임) mô hình (model / 모델). Nhiều concept React map trực tiếp:

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

TypeScript giúp static contracts nhưng không sửa thời gian chạy (runtime / 런타임) timing. Nếu nhà phát triển (developer / 개발자) không hiểu closure, định danh (identity / 식별자) và vòng lặp sự kiện (event loop / 이벤트 루프), React-specific rules sẽ chỉ trở thành mẹo thuộc lòng.

---

# 28. Cross-realm hành vi (behavior / 동작) — iframe/cửa sổ (window / 윈도우) làm `instanceof` không tuyệt đối

Mỗi Realm có own built-ins như `Array`, `Error`, `Promise` constructors. đối tượng (object / 객체) được tạo ở iframe Realm có prototype chuỗi (chain / 사슬) dựa constructors của iframe.

Vì vậy:

```js
value instanceof Array
```

có thể false với array từ iframe khác, trong khi:

```js
Array.isArray(value)
```

được thiết kế để nhận array across realms.

Đây cũng là lý do ES2026 `Error.isError()` có giá trị: lỗi (error / 오류) detection bằng `instanceof Error` có cross-realm limitation.

Thư viện (library / 라이브러리) nhận values từ iframe/worker/plugin ranh giới (boundary / 경계) nên hiểu Realm ngữ nghĩa (semantics / 의미론) thay vì dựa blind vào nominal-looking checks.

---

# 29. API thiết kế (design / 설계) ở mức Master — dữ liệu (data / 데이터), quyền sở hữu (ownership / 소유권), async, errors, bảo mật (security / 보안)

Khi rà soát (review / 검토) một API/mô-đun (module / 모듈), hỏi theo thứ tự:

**dữ liệu (data / 데이터) đặc tả hợp đồng (contract / 계약):** đầu vào (input / 입력)/đầu ra (output / 출력) là gì, bên ngoài (external / 외부) đầu vào (input / 입력) được parse ở đâu, missing/null/empty khác nhau thế nào?

**quyền sở hữu (ownership / 소유권):** ai được mutate đối tượng (object / 객체), ai tạo tài nguyên (resource / 자원), ai cleanup?

**Async:** thao tác (operation / 연산) có hết thời gian chờ (timeout / 타임아웃)/cancellation không, race/stale kết quả (result / 결과) xử lý ở đâu, tính đồng thời (concurrency / 동시성) có bounded không?

**Errors:** expected thất bại (failure / 실패) hay programmer bug, chuỗi nhân quả (causal chain / 인과 사슬) có giữ không, lỗi (error / 오류) mã (code / 코드) có stable cho bên tiêu thụ (consumer / 소비자) không?

**bảo mật (security / 보안):** caller được năng lực (capability / 역량) gì, trust ranh giới (boundary / 경계) ở đâu, sink nào có privilege?

**Versioning:** đặc tả hợp đồng (contract / 계약) có chạy giữa web/bản địa (native / 네이티브)/plugin/backend qua nhiều bản phát hành (release / 릴리스) không?

**khả năng quan sát (observability / 관측 가능성):** môi trường vận hành (production / 운영 환경) thất bại (fail / 실패) thì có correlation ID, structured log, bản phát hành (release / 릴리스) phiên bản (version / 버전) và bản đồ mã nguồn (source map / 소스 맵) không?

**tính tương thích (compatibility / 호환성):** tính năng (feature / 기능) mới có thật sự chạy trên mục tiêu (target / 대상) WebView/thời gian chạy (runtime / 런타임) không?

**Testability:** mạng (network / 네트워크)/lưu trữ (storage / 저장소)/clock/random/bản địa (native / 네이티브) cầu nối (bridge / 브리지) có phụ thuộc (dependency / 의존성) seams không?

Một API tốt phải **khó dùng sai**, không chỉ có tên phương thức (method / 메서드) đẹp.

---

# 30. Testing ở mức (level / 수준) Master — kiểm thử bất biến (invariant / 불변식) và timing chứ không chỉ examples

Đơn vị (unit / 단위)/tích hợp (integration / 통합)/E2E vẫn là nền, nhưng advanced testing thêm nhiều góc.

**Property-based testing** kiểm tra bất biến (invariant / 불변식) trên nhiều generated inputs, ví dụ `decode(encode(x))` phải round-trip đúng trong valid lĩnh vực (domain / 도메인).

**Fuzzing** đặc biệt hữu ích cho parsers, cầu nối (bridge / 브리지) payloads, URL handling, nhị phân (binary / 이진) decoders và regex-sensitive inputs.

**Mutation testing** cố thay đổi operators/branches để xem tests có thật sự phát hiện hành vi (behavior / 동작) thay đổi (change / 변경) không.

**Deterministic async tests** tránh phụ thuộc real timer/mạng (network / 네트워크) scheduling bằng fake clock, controlled promises hoặc scheduler seam.

Clock nên inject khi lô-gic nghiệp vụ (business logic / 비즈니스 로직) phụ thuộc thời gian (time / 시간):

```js
function createService({ now = Date.now } = {}) {
  return {
    expired(expiresAt) {
      return now() >= expiresAt;
    }
  };
}
```

Kiểm thử (test / 테스트) có thể inject deterministic `now`.

---

# 31. Cách đọc hiện đại (modern / 현대적) JavaScript mà không chạy theo tính năng (feature / 기능) mới

Một tính năng (feature / 기능) mới chỉ nên vào codebase khi nó thỏa ba điều: **ngữ nghĩa (semantics / 의미론) tốt hơn hoặc mã (code / 코드) rõ hơn**, **mục tiêu (target / 대상) runtimes hỗ trợ (support / 지원) hoặc có fallback đúng**, và **nhóm (team / 팀)/toolchain hiểu nó**.

Không refactor:

```js
for (const item of items) {
  total += item;
}
```

sang API mới chỉ vì API mới hơn nếu vòng lặp (loop / 루프) đang rõ và đúng.

Ngược lại, nếu `toSorted()` diễn đạt chính xác “sorted bản sao (copy / 복사), không mutate nguồn (source / 소스)”, nó có ngữ nghĩa (semantic / 의미적) giá trị (value / 값) thực sự so với:

```js
[...items].sort(compare)
```

khi mục tiêu (target / 대상) hỗ trợ (support / 지원).

Hiện đại (modern / 현대적) JavaScript mastery không phải dùng newest cú pháp (syntax / 문법) nhiều nhất. Nó là khả năng chọn lớp trừu tượng (abstraction / 추상화) đúng với bài toán (problem / 문제) và tính tương thích (compatibility / 호환성) ma trận (matrix / 행렬).

---

# 32. tính tương thích (compatibility / 호환성) workflow sau ES2026

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

`ESNext` không phải phiên bản (version / 버전) cố định. Một bài năm 2020 và một bài năm 2026 nói ESNext có thể nói về các tính năng (feature / 기능) hoàn toàn khác nhau.

Living spec tại `tc39.es/ecma262` có thể đi trước snapshot chính thức vì nó tích hợp finished proposals cho edition tiếp theo. Historical yearly snapshots mới là mốc edition ổn định.

---

# 33. Master gotchas — hiểu bằng ngữ nghĩa (semantics / 의미론), không học thuộc câu đố

Các hành vi (behavior / 동작) sau nên quen vì chúng nối nhiều phần của ngôn ngữ (language / 언어) mô hình (model / 모델):

```js
typeof null === "object";
NaN !== NaN;
Object.is(NaN, NaN);
Object.is(0, -0);
```

Sparse hole khác `undefined`. `delete array[index]` tạo hole chứ không shift array. `sort()` mutate, `toSorted()` không mutate. đối tượng (object / 객체) spread và `Object.freeze()` đều shallow. `Map` đối tượng (object / 객체) keys dùng đối tượng (object / 객체) định danh (identity / 식별자). Regex `g`/`y` có `lastIndex` trạng thái (state / 상태). `Promise.race()` không cancel losing công việc (work / 작업). `forEach(async () => ...)` không đợi callbacks. `JSON.stringify(new Error())` không serialize useful lỗi (error / 오류) fields mặc định. `JSON.stringify(BigInt(...))` cần tường minh (explicit / 명시적) chiến lược (strategy / 전략). động (dynamic / 동적) import có thể thất bại (fail / 실패) vì triển khai (deployment / 배포)/chunk mismatch dù nguồn (source / 소스) compile đúng. `instanceof` có cross-realm limitation. Getter và Proxy trap có thể khiến ordinary-looking thuộc tính (property / 속성) truy cập (access / 접근) thực thi arbitrary lô-gic (logic / 논리).

Mục tiêu không phải ghi nhớ như trivia. Khi gặp một hành vi (behavior / 동작) lạ, hãy phân loại nó về **coercion/equality**, **mô hình đối tượng (object model / 객체 모델)**, **async scheduling**, **serialization**, **mô-đun (module / 모듈)/thời gian chạy (runtime / 런타임)**, hoặc **host ranh giới (boundary / 경계)** rồi điều tra đúng tầng.

---

# 34. Coverage matrix sau audit
Phần này nối mạch bài học với “34. Coverage matrix sau audit”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

| Nhóm kiến thức | chuẩn gốc (canonical / 정본) mức (level / 수준) chính | Trạng thái sau kiểm tra (audit / 감사) |
| --- | --- | --- |
| mô hình thực thi (execution model / 실행 모델) / ngăn xếp lời gọi (call stack / 호출 스택) | Intermediate + Master | Đã cover sâu và nối spec/thời gian chạy (runtime / 런타임) |
| Values / types / coercion | Beginner + Master | Đã cover từ practical đến abstract operations |
| phạm vi (scope / 범위) / lexical môi trường (environment / 환경) | Intermediate | Đã cover |
| Hoisting / TDZ | Beginner + Master | Đã làm rõ bằng binding initialization |
| hàm (function / 함수) / closure | Beginner → Intermediate → Master | Đã cover sâu vòng đời (lifecycle / 생명주기)/bộ nhớ (memory / 메모리) |
| `this` | Intermediate + Master | Đã cover call-site + receiver ngữ nghĩa (semantics / 의미론) |
| Prototype / lớp (class / 클래스) | Intermediate + Master | Đã cover legacy constructor ↔ lớp (class / 클래스) evolution |
| đối tượng (object / 객체) / array | Beginner → Master | Đã cover ordinary/exotic/sparse/copying APIs |
| Iteration | Intermediate/cấp cao (senior / 시니어)/Master | Đã cover sync/async/lazy/hiện đại (modern / 현대적) helpers |
| Modules | Beginner → Intermediate → Master | Đã cover ESM, legacy, cycles, động (dynamic / 동적) import, tooling |
| lỗi (error / 오류) handling | Beginner/cấp cao (senior / 시니어)/Master | Đã cover cú pháp (syntax / 문법) → taxonomy → cause/serialization |
| Promise / async-await | Beginner → Intermediate → Master | Đã cover resolution, scheduling và legacy callbacks |
| tác vụ (task / 작업) / microtask / vòng lặp sự kiện (event loop / 이벤트 루프) | Intermediate + Master | Đã cover timeline + kết xuất (render / 렌더링)/host ranh giới (boundary / 경계) |
| trình duyệt (browser / 브라우저) thời gian chạy (runtime / 런타임) / DOM / events | Beginner/Intermediate/cấp cao (senior / 시니어) | Đã cover |
| Fetch / lưu trữ (storage / 저장소) | Beginner + cấp cao (senior / 시니어) bảo mật (security / 보안) | Đã cover |
| bộ nhớ (memory / 메모리) / GC | cấp cao (senior / 시니어) + Master | Đã cover reachability/vòng đời (lifecycle / 생명주기)/profiling |
| hiệu năng (performance / 성능) | cấp cao (senior / 시니어) + Master | Đã cover methodology/tooling |
| bảo mật (security / 보안) | cấp cao (senior / 시니어) + Master | Đã cover source-to-sink/năng lực (capability / 역량) boundaries |
| Modules/tooling | cấp cao (senior / 시니어) + Master | Đã cover transpile/polyfill/bundle/nguồn (source / 소스) maps |
| hiện đại (modern / 현대적) JavaScript | Tất cả levels | Đã cover evolution và tính tương thích (compatibility / 호환성) mindset |
| Legacy JavaScript | Beginner notes + Master | Đã cover ánh xạ (mapping / 매핑) IIFE/var/callback/prototype/CommonJS |
| ES5 → ES2015 → hiện đại (modern / 현대적) | Beginner + Master | Đã chuyển từ timeline sang giải thích động cơ |
| ECMAScript 2026 | Master | Đã bổ sung selected meaningful features |

Kiểm tra (audit / 감사) này cố ý không tạo thêm tệp chuẩn gốc (canonical file / 정본 파일). học tập (learning / 학습) thư viện (library / 라이브러리) tiếp tục dùng đúng bốn notes hiện có.

---

# 35. Master exit criteria

Bạn không cần thuộc ECMA-262. Nhưng sau toàn bộ thư viện (library / 라이브러리), bạn nên có thể giải thích bằng lời:

Một hàm (function / 함수) lời gọi (call / 호출) tạo ngữ cảnh (context / 맥락) gì và ngăn xếp lời gọi (call stack / 호출 스택) thay đổi thế nào. Lexical môi trường (environment / 환경) quyết định phạm vi (scope / 범위) chuỗi (chain / 사슬) ra sao. Hoisting/TDZ phản ánh declaration initialization khác nhau thế nào. Closure giữ môi trường (environment / 환경) vì reachability chứ không phải vì “hàm (function / 함수) nhớ magic”. `this` khác lexical phạm vi (scope / 범위) vì receiver/call-site ngữ nghĩa (semantics / 의미론). Prototype lookup diễn ra thế nào và lớp (class / 클래스) chỉ là lớp trừu tượng (abstraction / 추상화) trên prototype mô hình (model / 모델). Promise/`await` continuation liên hệ microtask ra sao. tác vụ (task / 작업)/microtask/kết xuất (render / 렌더링) sequencing ảnh hưởng UI thế nào. ES modules khác toàn cục (global / 전역)/IIFE/CommonJS ở phụ thuộc (dependency / 의존성) mô hình (model / 모델) nào. Garbage collector nhìn reachability, không nhìn nghiệp vụ (business / 비즈니스) intent. trình duyệt (browser / 브라우저) APIs khác ECMAScript built-ins ở specification/tính tương thích (compatibility / 호환성) tầng (layer / 계층) nào. Transpilation khác polyfill thế nào. Và khi một tính năng (feature / 기능) mới xuất hiện, bạn biết đánh giá tiêu chuẩn (standard / 표준) status, thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원) và bài toán (problem / 문제) solved thay vì chỉ hỏi “tính năng (feature / 기능) này mới không?”.

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

rồi giải thích chính xác **những lớp trừu tượng (abstraction / 추상화) nào đã thay đổi**, chứ không chỉ nói đoạn dưới “hiện đại (modern / 현대적) hơn”.

---

# Appendix A — Nguồn authoritative để cập nhật thư viện (library / 라이브러리)

Khi cần xác minh ngôn ngữ (language / 언어) ngữ nghĩa (semantics / 의미론)/phiên bản (version / 버전), ưu tiên:

```text
ECMA-262 living specification
https://tc39.es/ecma262/

Ecma International yearly ECMA-262 editions
https://ecma-international.org/publications-and-standards/standards/ecma-262/

TC39 proposals
https://github.com/tc39/proposals
```

Khi cần developer-facing trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성), dùng MDN JavaScript/Web APIs và tính tương thích (compatibility / 호환성) tables. Khi dự án (project / 프로젝트) là hybrid app, trình duyệt (browser / 브라우저) tables vẫn phải được đối chiếu với WebView versions thực tế mà ứng dụng ship.

Không dùng một blog cũ hoặc một transpiler preset như nguồn duy nhất để kết luận tính năng (feature / 기능) đã tiêu chuẩn (standard / 표준) hay thời gian chạy (runtime / 런타임) đã hỗ trợ (support / 지원).

---

# Kết luận

JavaScript thư viện kiến thức (knowledge library / 지식 라이브러리) hoàn chỉnh không nên kết thúc ở việc nhớ nhiều APIs. Mục tiêu cuối là nhìn một vấn đề và đặt nó vào đúng tầng:

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

ES5, ES2015 và hiện đại (modern / 현대적) ECMAScript không phải ba ngôn ngữ khác nhau. Chúng là ba giai đoạn trong quá trình cùng một ngôn ngữ (language / 언어) trưởng thành: ES5 chuẩn hóa nền web đã tồn tại, ES2015 cung cấp những abstractions cần cho applications/modules lớn, và yearly ECMAScript sau đó bổ sung dần các patterns đã chứng minh giá trị trong ecosystem.

Khi bạn hiểu **vì sao** một feature xuất hiện, bạn có thể đọc cả legacy và modern code mà không bị phụ thuộc vào thời điểm syntax được viết. Đó mới là mục tiêu của Master level.

> **Bàn giao:** Sau **CommonJS / bundler-specific modules**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
