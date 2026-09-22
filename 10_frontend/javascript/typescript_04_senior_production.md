# TypeScript 04 — Senior Production Engineering

> Prerequisite: [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md). Mục tiêu của chapter này là nối static model với evidence production thay vì dừng ở type-level elegance.

## 1. Trust boundary: mọi dữ liệu bên ngoài process đều bắt đầu như `unknown`

HTTP response, localStorage, URL params, postMessage, native bridge payload, database row qua untyped driver, queue event và JSON file đều có thể khác assumption. TypeScript chỉ biết declarations bạn cung cấp.

Một boundary trung thực:

```ts
type User = {
  id: string;
  age: number;
};

function decodeUser(value: unknown): User {
  if (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    typeof value.id === "string" &&
    "age" in value &&
    typeof value.age === "number"
  ) {
    return {
      id: value.id,
      age: value.age
    };
  }

  throw new Error("Invalid user payload");
}
```

Real project có thể dùng schema/validator library, nhưng mental model không đổi: **parse/validate external representation → create trusted domain value**. `as User` không thay parser.

## 2. DTO và domain model không nên bị đồng nhất tự động

API DTO thường phản ánh transport concerns: nullable fields, string dates, legacy names, partial data. Domain model nên phản ánh invariant application.

```ts
type UserDto = {
  user_id: string;
  created_at: string;
};

type User = {
  id: UserId;
  createdAt: Date;
};
```

Adapter boundary làm conversion + validation. Lợi ích là nếu backend đổi format, damage được cô lập; UI/business code không phải carry transport quirks khắp codebase.

## 3. Branded ID ngăn cross-domain mix-up nhưng không validate format

```ts
declare const userIdBrand: unique symbol;
type UserId = string & { readonly [userIdBrand]: true };
```

Pattern này giúp compiler phân biệt `UserId` và `OrderId`, nhưng runtime vẫn là string. Constructor/factory phải validate nếu ID có format invariant:

```ts
function parseUserId(value: string): UserId {
  if (!value.startsWith("usr_")) {
    throw new Error("Invalid UserId");
  }

  return value as UserId;
}
```

Assertion ở đây được đặt sau runtime evidence, nên proof obligation rõ.

## 4. Illegal state khó represent hơn bằng discriminated union

Checkout state, websocket connection, async mutation hay permission state thường tốt hơn khi model bằng finite states thay vì nhiều optional booleans.

```ts
type UploadState =
  | { kind: "idle" }
  | { kind: "uploading"; progress: number }
  | { kind: "done"; assetId: string }
  | { kind: "failed"; error: Error };
```

Một reducer/switch exhaustive có thể giữ transition logic rõ. Khi business thêm `cancelled`, compiler chỉ ra nơi cần review thay vì để state mới silently rơi qua default branch.

## 5. Error modeling: đừng biến mọi failure thành `Error | null | undefined`

Trong boundary quan trọng, error category có thể là domain data:

```ts
type LoginResult =
  | { ok: true; token: string }
  | { ok: false; reason: "invalid_credentials" }
  | { ok: false; reason: "locked"; retryAfterMs: number };
```

Nhưng không phải mọi exception cần union khổng lồ. Unexpected programmer/runtime faults vẫn có thể throw. Hãy phân biệt expected business outcome với exceptional failure; type model nên phản ánh recovery strategy.

## 6. React + TypeScript: type component contract, không type framework theo cảm giác

React component props là public API nhỏ. Discriminated props loại invalid combinations tốt hơn optional soup:

```ts
type ButtonProps =
  | {
      kind: "link";
      href: string;
      onClick?: never;
    }
  | {
      kind: "action";
      onClick: () => void;
      href?: never;
    };
```

State/reducer actions cũng hưởng lợi từ discriminated unions. Generic component chỉ nên generic khi relation thật cần giữ, ví dụ table `row` và accessor keys. Đừng biến mọi component thành `<TData, TValue, TMeta>` nếu component chỉ hiển thị vài fields cố định.

Các mental model render/state/effect thuộc [React canonical docs](../react/00_index.md); TypeScript không thay React runtime semantics.

## 7. Event và ref types: derive từ API thay vì nhớ bằng rote

Với framework/library types, ưu tiên derive/import canonical types từ library declarations. Nếu callback type quá phức tạp, hover/go-to-definition để xem contract thay vì tự viết gần giống. Copy type thủ công dễ drift theo version.

Khi inference đủ tốt, không cần annotate từng event. Annotation nên được dùng ở exported helpers hoặc chỗ contextual typing mất thông tin.

## 8. Node/backend TypeScript: static types không thay validation/authorization

Controller nhận request body không nên cast thẳng thành domain command. Auth claims cũng là external/security boundary. TypeScript không chứng minh user có permission; nó chỉ có thể giúp model output của một authorization step đã chạy.

```text
request bytes
→ parse
→ authenticate
→ authorize
→ validate command
→ domain operation
```

Mỗi arrow là một boundary có failure mode riêng. Type alias `AdminUser` không tự biến JWT thành admin.

## 9. Security: những gì TypeScript không bảo vệ

TypeScript không ngăn XSS, CSRF, SQL injection, prototype pollution, SSRF hay broken access control chỉ bằng static types. Nó có thể giúp tạo safer APIs—ví dụ tách `TrustedHtml` khỏi raw string hoặc parameterize query builder—nhưng runtime sanitization/escaping/authorization vẫn phải tồn tại.

Assertion, `any`, `@ts-ignore` và declaration giả đặc biệt nguy hiểm ở security-sensitive boundary vì chúng làm checker im đúng nơi evidence yếu nhất.

## 10. `@ts-expect-error` tốt hơn `@ts-ignore` khi test known invalid code

Nếu intentionally test compile-time rejection:

```ts
// @ts-expect-error invalid id type must be rejected
loadUser(123);
```

`@ts-expect-error` sẽ báo nếu dòng đó không còn error, giúp test không silently obsolete. `@ts-ignore` chỉ suppress và dễ sống mãi. Comment phải nói invariant gì đang được test, không chỉ “fix TS”.

## 11. Compile-time contract tests cho library

Library có thể cần test cả runtime behavior và type surface. Một API generic có thể runtime pass nhưng inference regression phá consumer. Test fixtures nên cover valid inference, expected invalid calls và declaration output.

Public type changes cần semantic-version reasoning tương tự runtime API. Một “refactor type only” có thể là breaking change nếu consumer source không compile.

## 12. Public API type nên nhỏ, stable và explainable

Exporting giant inferred internal type làm implementation leak ra public contract. Khi internal refactor đổi inferred shape, consumer bị break ngoài ý muốn.

Nên đặt explicit public aliases/interfaces ở boundary và giữ helper conditional/mapped types private khi có thể. Public generic constraints phải phản ánh concept domain, không expose checker implementation details.

## 13. Runtime schema và static type nên có một source of truth khi có thể

Nếu maintain schema runtime và TypeScript type độc lập, chúng có thể drift. Tùy stack, có thể derive type từ schema hoặc schema từ model/codegen. Nhưng “single source” cũng có trade-off: generated output khó đọc, tool lock-in, runtime bundle size hoặc schema expressiveness khác type system.

Quyết định đúng dựa trên trust boundary và ownership. Quan trọng nhất là có automated evidence rằng runtime validator và static contract không lệch.

## 14. API client: normalize error và data một lần

Thay vì mỗi component tự `fetch` rồi cast:

```ts
async function getUser(id: UserId): Promise<User> {
  const response = await fetch(`/api/users/${id}`);

  if (!response.ok) {
    throw new HttpError(response.status);
  }

  const raw: unknown = await response.json();
  return decodeUser(raw);
}
```

Boundary này tập trung HTTP status, JSON parse, validation và mapping. Downstream code làm việc với trusted `User` thay vì lặp defensive checks.

## 15. Async type không loại race condition

`Promise<User>` nói eventual value type, không nói request nào thắng nếu hai request chạy song song. TypeScript không ngăn stale response overwrite newer state. Runtime concurrency control vẫn cần AbortController, request identity, state machine hoặc framework-level data layer.

Đây là ví dụ điển hình của connection với JavaScript async runtime: static type đúng nhưng temporal behavior sai.

## 16. Performance: type-check time là production developer experience

Large codebase phải theo dõi cold check, incremental check, editor latency và memory. TypeScript 7.0 giảm đáng kể compiler cost trong nhiều workload nhờ native architecture, nhưng pathological type definitions vẫn có thể đắt.

Khi một file tạo giant union/recursive conditional, không nên nói “compiler 7 nhanh rồi nên bỏ qua”. Fast compiler tăng budget, không xóa asymptotic/problem-shape cost.

Evidence nên gồm `--extendedDiagnostics`, trace khi cần, diff before/after PR và editor reproduction. Tối ưu bằng cách giảm type instantiation, chia public surface, tránh huge generated unions, hoặc chuyển validation logic phù hợp về runtime.

## 17. `any` debt phải được quản lý như migration debt

`any` ở một leaf adapter có thể chấp nhận tạm thời; `any` ở shared library boundary có blast radius lớn. Khi migrate legacy code, track số `any` thôi chưa đủ. Phân loại:

```text
boundary any     → ưu tiên thay bằng unknown + validation
library any      → ưu tiên cao vì lan sang consumer
local migration  → có thể tạm chấp nhận với TODO/owner
third-party gap  → isolate bằng adapter/declaration patch
```

Mục tiêu là containment và evidence, không phải “zero any” bằng cast tinh vi hơn.

## 18. Migration JavaScript → TypeScript theo risk, không theo folder alphabet

Một chiến lược thực dụng:

```text
1. bật project graph / allowJs
2. type shared contracts và domain boundaries
3. type API/data adapters
4. type utilities/core logic
5. migrate feature modules dần
6. tighten strict flags theo evidence
7. loại escape hatches còn lại
```

Nếu bật toàn bộ strict flags trên codebase lớn rồi thêm hàng nghìn `as any`, bạn đạt config strict nhưng không đạt type safety.

## 19. Legacy patterns phải biết đọc

Bạn vẫn có thể gặp `namespace`, triple-slash references, ambient globals, old decorator mode, `enum`-heavy code, non-strict null handling, `moduleResolution` legacy modes và CommonJS interop workaround. Mục tiêu không phải rewrite ngay; trước tiên hiểu runtime/package assumptions, thêm tests, rồi migrate theo seam nhỏ.

`enum` là ví dụ cần reasoning. Nó có runtime representation khác type-only union. Literal union + `as const` object thường phù hợp config/domain constants hiện đại, nhưng existing enum có thể là public ABI hoặc dependency expectation. Đừng đổi chỉ vì style.

## 20. Debugging production type/runtime mismatch

Khi production crash dù CI type-check pass, trace theo boundary:

```text
1. runtime value thật là gì?
2. value đi vào typed world qua chỗ nào?
3. có assertion/any/declaration nào tạo false proof?
4. validator/schema version có khớp producer không?
5. emitted/bundled artifact có khác source assumptions không?
```

Ví dụ stack `Cannot read properties of undefined` trên `user.profile.name` thường không cần “type phức tạp hơn”; cần tìm nơi `user` được tạo từ external data mà không validate.

## 21. Observability: log boundary facts, không log type name

Runtime không biết `User` interface. Khi debug, log safe metadata thực: schema/version, endpoint, status, discriminant, validation error path, request ID. Đừng log sensitive payload chỉ để chứng minh “type sai”. Security và observability phải phối hợp.

## 22. Package/library authoring với TypeScript 7

TypeScript 7.0 tập trung mạnh vào native compiler/tooling và hiện tại không cung cấp programmatic API giống 6.x. Nếu library build chain hoặc plugin cần compiler API, có thể phải chạy 6.0 compatibility package side-by-side trong migration period. Đây là toolchain concern, không có nghĩa source library phải hạ type-system knowledge về 6.0.

Khi publish, kiểm tra declarations, ESM/CJS exports, runtime target, package conditions và consumer compile fixture. TypeScript version minimum nên được document khi public types dùng feature mới mà compiler cũ không parse/understand.

## 23. Senior code review checklist dưới dạng reasoning

Thay vì checklist máy móc, review TypeScript nên hỏi theo chuỗi: type này mô hình invariant thật hay chỉ mô tả data hiện tại; external value đã được validate chưa; generic giữ relation nào; assertion có evidence ở đâu; config/module behavior có khớp runtime không; public type có expose implementation detail không; và advanced type có đáng cost compiler/cognitive không?

Một PR tốt có thể xóa type-level complexity nếu runtime model đã đơn giản hơn. “Nhiều type” không đồng nghĩa “type-safe hơn”.

## 24. Production case — API field đổi từ required sang nullable

Giả sử backend đổi `middleName: string` thành `string | null`. Nếu generated/handwritten DTO được cập nhật đúng, compiler sẽ đẩy diagnostic tới mapper và consumer. Mapper có thể quyết định domain representation là `string | null`, `Option`-like union, hoặc normalize thành empty display text ở UI boundary.

Nếu team chỉ sửa bằng `as string`, build xanh nhưng runtime evidence bị bỏ. TypeScript có giá trị khi change propagation ép team ra quyết định tại đúng layer.

## 25. Production case — module type pass, runtime import fail

IDE resolve alias `@domain/user` nhờ `paths`, nhưng bundler/Node không có alias tương ứng. Static type graph pass, runtime fail. Debug đúng là inspect resolver configs/package exports, không chỉnh interface. Đây là lý do chapter tooling nằm trong TypeScript track: type correctness và module execution phải khớp.

## 26. Production case — type-level abstraction làm editor lag

Một design-system utility tạo template literal union từ hàng trăm token × variants × breakpoints. Type auto-complete rất “thông minh” nhưng editor latency tăng. Senior response là đo checker trace, giảm combinatorial union, chuyển một phần validation sang runtime/schema hoặc giới hạn key space. Developer experience là một production constraint của type design.

## 27. Kết nối với JavaScript và React canonical docs

TypeScript không thay scope/closure, prototype, event loop, Promise ordering hay browser security model; xem [JavaScript Intermediate](javascript_intermediate.md) và [JavaScript Senior](javascript_senior.md). TypeScript cũng không thay React render/commit/effect semantics; xem [React Index](../react/00_index.md).

Nếu một bug xảy ra sau khi code đã compile, quay lại runtime layer trước khi thêm type annotation. Nếu bug là invalid state được compiler cho qua, quay lại model/invariant. Nếu IDE và runtime disagree về import, quay lại module/tooling layer. Đây là cách tách failure mode có hệ thống.

---

Hoàn tất track: quay lại [TypeScript Index](typescript_00_index.md) để review coverage và glossary.
