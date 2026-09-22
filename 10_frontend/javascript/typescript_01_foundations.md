# TypeScript 01 — Foundations & Runtime Boundary

> Canonical navigation: [TypeScript Index](typescript_00_index.md) → Foundations → [Type System Internals](typescript_02_type_system.md) → [Compiler & Tooling](typescript_03_tooling_modules_runtime.md) → [Senior Production](typescript_04_senior_production.md).

## 1. TypeScript giải quyết vấn đề nào?

JavaScript quyết định phần lớn lỗi theo runtime. Nếu một function mong nhận object có `email` nhưng caller truyền object khác shape, chương trình có thể chỉ phát hiện khi branch đó thật sự chạy. Với project nhỏ, developer có thể giữ contract trong đầu. Với project lớn, contract bị phân tán qua module, API, component, test và nhiều người cùng sửa; chi phí reasoning tăng nhanh hơn số dòng code.

TypeScript thêm một lớp mô hình tĩnh để compiler có thể hỏi trước khi chạy: expression này có thể tạo ra những value nào, property này có chắc tồn tại không, function này có thể return `undefined` không, caller có đang đưa đúng contract không? Giá trị lớn nhất không phải “viết thêm `: string`”, mà là biến implicit assumptions thành thứ toolchain có thể kiểm tra và refactor cùng bạn.

Điểm quan trọng nhất: TypeScript **không thay đổi bản chất runtime của JavaScript**. Ví dụ:

```ts
type User = {
  id: string;
  name: string;
};

function greet(user: User) {
  return `Hello ${user.name}`;
}
```

Sau khi compile, `type User` không trở thành một runtime class hay validation function. Runtime vẫn xử lý JavaScript object. Đây là **xóa kiểu (type erasure / 타입 소거)**. Vì thế một assertion như sau không kiểm tra gì ở runtime:

```ts
const data = JSON.parse(raw) as User;
```

Nếu `raw` thiếu `name`, compiler vẫn tin assertion của bạn. Bạn đã tự cung cấp “bằng chứng” mà không kiểm chứng nó.

## 2. Compile-time và runtime là hai thế giới nối nhau bằng contract

Hãy dùng mental model hai tầng:

```text
source .ts
  ↓
TypeScript parser + binder + checker
  ↓ diagnostics / inferred types
emit hoặc noEmit
  ↓
JavaScript + runtime environment
```

Compiler nhìn source và declaration files. Runtime nhìn values thật. Một HTTP response, row database hay message từ native bridge không tự nhiên đáng tin chỉ vì variable phía TypeScript được annotation đẹp.

Ví dụ production:

```ts
interface ProfileResponse {
  userId: string;
  age: number;
}

async function loadProfile(): Promise<ProfileResponse> {
  const response = await fetch("/api/profile");
  return response.json();
}
```

Signature trên chỉ mô tả điều developer mong muốn. `response.json()` có thể trả bất kỳ JSON value nào. Senior code cần tách `unknown external data` khỏi `validated domain data`; phần này sẽ được làm đầy đủ ở chapter Senior Production.

## 3. Annotation và inference: đừng annotate mọi thứ

TypeScript có **suy luận kiểu (type inference / 타입 추론)**. Với:

```ts
const retryCount = 3;
const endpoint = "/api/users";
const enabled = true;
```

compiler đã biết type cần thiết. Annotation lặp lại như `const retryCount: number = 3` thường không thêm thông tin.

Annotation có giá trị khi nó đặt contract tại boundary:

```ts
function calculateTotal(price: number, quantity: number): number {
  return price * quantity;
}
```

Hoặc khi muốn chống accidental widening hay xác nhận một public shape. Quy tắc thực dụng là: **để inference làm việc bên trong implementation, viết contract rõ ở public/module boundaries**.

## 4. Literal type, widening và `as const`

TypeScript phân biệt `string` với literal type như `"idle"`. Với mutable binding, compiler thường widen:

```ts
let status = "idle"; // string
status = "running";
```

Với `const`, compiler có thể giữ literal hẹp hơn vì binding không được reassign:

```ts
const status = "idle"; // "idle"
```

Object vẫn mutable nên property thường widen:

```ts
const request = {
  method: "GET"
};
// request.method thường là string
```

Khi muốn giữ literal structure sâu hơn:

```ts
const request = {
  method: "GET",
  retry: 2
} as const;
```

`as const` làm các literal được giữ hẹp và properties/tuple trở nên readonly ở type level. Nó không `Object.freeze()` runtime object; đây tiếp tục là type/runtime boundary.

## 5. Primitive, object và sự khác biệt giữa `string` với `String`

Trong TypeScript code hiện đại, dùng primitive types `string`, `number`, `boolean`, `bigint`, `symbol`. Các wrapper object types `String`, `Number`, `Boolean` đại diện cho boxed objects và gần như không phải thứ bạn muốn cho application contract.

```ts
function normalize(value: string) {
  return value.trim().toLowerCase();
}
```

Đừng nhầm `object` với “object có property nào đó”. `object` chỉ loại primitive ra. `{}` lại mang semantics khác và quá rộng cho nhiều use case. Khi chưa biết shape external data, `unknown` thường đúng hơn.

## 6. `any`, `unknown`, `never`: ba type dễ dùng sai nhất

`any` nói với checker: “đừng kiểm tra nữa”. Nó lan truyền rất nhanh:

```ts
let payload: any = getSomething();
payload.user.profile.name.toUpperCase(); // compiler im lặng
```

`unknown` nói: “có value, nhưng chưa có bằng chứng về shape”. Bạn buộc phải narrow trước:

```ts
function printLength(value: unknown) {
  if (typeof value === "string") {
    console.log(value.length);
  }
}
```

`never` đại diện cho tập value rỗng: branch không thể xảy ra nếu model đúng, hoặc function không hoàn tất bình thường.

```ts
function fail(message: string): never {
  throw new Error(message);
}
```

`never` đặc biệt hữu ích cho exhaustive checking của discriminated union.

Mental model:

```text
any     = tắt phần lớn bằng chứng
unknown = chưa biết, phải chứng minh
never   = không có value hợp lệ nào còn lại
```

## 7. Union type và narrowing bằng control flow

Union `A | B` nghĩa value có thể thuộc một trong nhiều possibility. Bạn chỉ được dùng operation an toàn cho mọi possibility cho tới khi có evidence.

```ts
function normalizeId(id: string | number) {
  if (typeof id === "number") {
    return id.toString();
  }

  return id.trim();
}
```

Checker theo dõi control flow, assignment, `typeof`, equality, `in`, `instanceof`, truthiness và user-defined type predicates để thu hẹp kiểu.

Một lỗi reasoning phổ biến là narrow xong rồi gọi callback có thể chạy sau, trong khi mutable state đã thay đổi. Hãy nhớ narrowing là proof gắn với control-flow assumptions của compiler; async/callback boundaries và mutation có thể khiến proof không còn mạnh như bạn tưởng. Cách tốt thường là capture value đã được validate vào immutable local binding.

## 8. Discriminated union: model state thay vì ghép boolean

Giả sử request state dùng ba field:

```ts
type BadState = {
  loading: boolean;
  data?: User[];
  error?: Error;
};
```

Shape này cho phép những combination vô lý như `loading: true` đồng thời có cả `data` và `error`.

Model tốt hơn:

```ts
type RequestState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: User[] }
  | { status: "error"; error: Error };
```

`status` là discriminant. Khi kiểm tra `status`, compiler narrow toàn object. Đây không chỉ là “type trick”; nó biến invariant business thành cấu trúc mà compiler giữ giúp bạn.

```ts
function renderState(state: RequestState) {
  switch (state.status) {
    case "idle":
      return "Idle";
    case "loading":
      return "Loading";
    case "success":
      return `${state.data.length} users`;
    case "error":
      return state.error.message;
    default: {
      const impossible: never = state;
      return impossible;
    }
  }
}
```

Nếu thêm state mới mà quên xử lý, `never` biến omission thành diagnostic.

## 9. Intersection type không phải object spread

`A & B` yêu cầu một value thỏa cả A và B. Nó không đồng nghĩa runtime merge hai objects.

```ts
type Timestamped = { createdAt: Date };
type Entity = { id: string };

type PersistedEntity = Entity & Timestamped;
```

Nếu hai type có property cùng tên nhưng incompatible, intersection có thể tạo property thành `never` hoặc type rất khó dùng. Đây là dấu hiệu model đang mâu thuẫn, không phải compiler “ngu”.

## 10. `interface` và `type`: chọn theo semantics, không theo giáo điều

Cả hai đều mô tả object shape tốt trong phần lớn trường hợp.

```ts
interface User {
  id: string;
  name: string;
}

type UserId = string;
type LoadState = "idle" | "loading" | "done";
```

`interface` có declaration merging và phù hợp public extensible object contracts trong một số library pattern. `type` diễn đạt union, intersection, primitive alias, tuple và type transformations linh hoạt hơn. Đừng biến lựa chọn này thành style war; hãy chọn cấu trúc phản ánh intent và tránh accidental merging ở application code nếu bạn không cần nó.

## 11. Optional property và `undefined` không hoàn toàn giống nhau

```ts
type A = { value?: string };
type B = { value: string | undefined };
```

A cho phép property không tồn tại. B yêu cầu property tồn tại nhưng value có thể là `undefined`. Sự khác biệt quan trọng khi serialize, spread, check `"value" in obj`, patch DTO và khi bật `exactOptionalPropertyTypes`.

Với strict modeling, đừng dùng optional chỉ để “cho compiler im”. Hỏi domain thật: field có thể absent hay luôn present nhưng unknown/empty?

## 12. `readonly` là compile-time restriction

```ts
type Config = {
  readonly apiUrl: string;
};
```

`readonly` ngăn một số assignment qua type surface đó, nhưng không biến object thành immutable runtime object. Nếu cùng object được tham chiếu qua type mutable khác, runtime vẫn có thể thay đổi. Đây là ví dụ khác về việc static model không tự tạo runtime guarantee.

## 13. Function types, optional parameter và callback contract

```ts
type Formatter = (value: number, locale?: string) => string;
```

Function type là contract về parameter và return. Callback assignability có các rule riêng để phù hợp JavaScript ecosystem; khi `strictFunctionTypes` hoạt động, function parameter variance được kiểm tra chặt hơn ở nhiều context. Chi tiết variance nằm ở chapter 02.

Một anti-pattern là khai báo return type quá rộng:

```ts
function findUser(id: string): User | null | undefined {
  // ...
}
```

Nếu domain thực chỉ có “found hoặc not found”, chọn một representation duy nhất. Type càng rộng, mọi caller càng phải carry ambiguity.

## 14. Type assertion và non-null assertion là lời hứa của developer

```ts
const input = document.querySelector("#name") as HTMLInputElement;
const token = maybeToken!;
```

Assertion không thêm runtime check. `!` cũng không làm value bớt `null`. Nó chỉ nói checker tin bạn. Dùng assertion hợp lý khi bạn có evidence compiler không biểu diễn được, nhưng mỗi assertion nên được nhìn như một **proof obligation**: evidence nằm ở đâu? test nào giữ invariant? runtime nào có thể phá assumption?

Khi assertion xuất hiện hàng loạt, thường model hoặc boundary validation đang yếu.

## 15. `satisfies`: kiểm tra shape mà vẫn giữ inference hữu ích

Giả sử muốn config phải khớp một contract nhưng vẫn giữ literal keys/value để dùng tiếp:

```ts
type RouteConfig = Record<string, {
  method: "GET" | "POST";
  secure: boolean;
}>;

const routes = {
  users: { method: "GET", secure: true },
  login: { method: "POST", secure: false }
} satisfies RouteConfig;
```

`satisfies` kiểm tra expression có assignable tới target type hay không nhưng không ép variable nhận chính target type như annotation thường làm. Đây là công cụ rất mạnh cho config maps, route tables và metadata khi bạn muốn validation + rich inference.

## 16. Excess property checking và “tại sao cùng object mà lúc lỗi, lúc không?”

TypeScript có kiểm tra đặc biệt với object literal ở một số context:

```ts
type User = { id: string };

const direct: User = {
  id: "u1",
  name: "Kim" // diagnostic
};
```

Nhưng nếu object đi qua variable trước, structural assignability có thể chấp nhận extra fields:

```ts
const source = { id: "u1", name: "Kim" };
const user: User = source; // thường hợp lệ
```

Đây không phải inconsistency ngẫu nhiên. Fresh object literal được kiểm tra excess property để bắt typo/config mistake, trong khi structural typing nói object có thể có nhiều capability hơn target yêu cầu. Hiểu hai rule này giúp tránh “fix” bằng `as User` chỉ để tắt lỗi.

## 17. Strict mode là baseline reasoning

Project hiện đại nên coi strict checking là baseline. `strictNullChecks` buộc `null`/`undefined` trở thành phần explicit của model. Các strict-family flags giúp compiler giữ invariant thay vì cho implicit `any` hoặc unsafe access lọt qua.

TypeScript 6.0/7.0 còn đi xa hơn về default strictness và modern module assumptions. Tuy nhiên project upgrade phải đọc release notes và config hiện hữu, vì đổi compiler version có thể thay diagnostic mà không đổi runtime code.

## 18. Debugging một type error theo tầng

Khi gặp diagnostic dài, đừng đọc từ câu cuối rồi cast. Hãy trace:

```text
1. Value/runtime intent thật là gì?
2. Type hiện tại được infer từ đâu?
3. Target contract yêu cầu gì?
4. Union/generic nào đã mở rộng hoặc mất thông tin?
5. Diagnostic đầu tiên nơi information bị mất là đâu?
```

Ví dụ một React prop error có thể bắt nguồn từ API DTO typed `any` quá sớm; một module type error có thể đến từ wrong resolution mode chứ không phải interface. Chapter sau sẽ đào sâu assignability và generic inference để trace các error kiểu này có hệ thống.

## 19. Failure modes cần nhớ

TypeScript không cứu được bạn khỏi logic sai nhưng type-correct, race condition, stale cache, SQL bug, authorization bug hay malformed external data nếu bạn tự cast. Nó cũng không làm object immutable runtime chỉ vì `readonly`, không làm array bounds-safe mặc định, và không biến `private` type semantics thành security boundary.

Giá trị của TypeScript xuất hiện mạnh nhất khi model phản ánh invariant thật và escape hatch được giữ ở boundary nhỏ, có evidence rõ.

---

Tiếp theo: [TypeScript 02 — Type System Internals & Generic Modeling](typescript_02_type_system.md).
