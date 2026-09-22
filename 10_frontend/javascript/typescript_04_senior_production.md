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

## 28. Validation là protocol transition, không chỉ là `schema.parse()`

Một boundary tốt không chỉ hỏi “shape có đúng không?” mà còn hỏi data đang ở **protocol version nào**, semantic invariant có đúng không, và sau parse value có được normalize về representation ổn định hay không.

Ví dụ timestamp string có thể đúng shape nhưng invalid date; amount có thể là number nhưng âm trong domain không cho phép; status có thể là string hợp schema cũ nhưng không còn được business chấp nhận.

```text
bytes / unknown value
→ syntactic parse
→ structural validation
→ semantic validation
→ normalization
→ domain value
```

TypeScript thường bắt đầu có giá trị mạnh nhất từ domain value trở đi. Nếu team gọi schema validator nhưng schema quá permissive hoặc bỏ semantic step, static type phía sau vẫn có thể trở thành false confidence.

## 29. Serialization boundary: TypeScript type không bảo đảm value truyền qua JSON được

Một object TypeScript có thể chứa `Date`, `Map`, `Set`, `bigint`, function, class instance hoặc cyclic references. `JSON.stringify` không preserve toàn bộ semantics đó; `bigint` còn gây lỗi nếu không có strategy riêng.

Vì vậy DTO qua HTTP/storage nên dùng representation serialization-safe có chủ đích:

```ts
type UserDto = {
  id: string;
  createdAt: string;
};

type User = {
  id: UserId;
  createdAt: Date;
};
```

Nếu dùng cùng một `User` type cho domain object lẫn transport payload, bạn đang che mất một state transition thật. Mapper không phải boilerplate vô ích; nó là nơi ownership của representation được xác định.

## 30. Schema evolution: backward/forward compatibility không nằm trong union type đơn lẻ

Event/queue payload thường sống lâu hơn một deploy. Producer v2 có thể gửi field mới khi consumer v1 vẫn chạy. Một type alias mới nhất không mô tả deployment topology này.

Có thể model version rõ:

```ts
type UserCreatedV1 = {
  version: 1;
  userId: string;
};

type UserCreatedV2 = {
  version: 2;
  userId: string;
  source: string;
};

type UserCreatedEvent = UserCreatedV1 | UserCreatedV2;
```

Decoder xử lý version, normalize về domain command hiện tại. Khi xóa support V1, đó là compatibility decision có telemetry/migration evidence, không chỉ là “remove union member cho code sạch”.

## 31. Generated types: generated không đồng nghĩa verified

OpenAPI, GraphQL, Protobuf hoặc database codegen có thể tạo TypeScript rất chính xác **so với schema input**, nhưng schema input có thể stale so với deployed producer. Code generation chứng minh consistency giữa code và schema snapshot, không chứng minh production system đang chạy đúng snapshot đó.

Pipeline đáng tin hơn thường có:

```text
source schema có ownership/version
→ deterministic codegen
→ generated diff review
→ compile
→ contract/integration test với producer hoặc fixture chuẩn
```

Đừng edit generated file bằng tay để “fix TypeScript”; hãy sửa source schema/generator hoặc adapter layer. Nếu phải patch generated output tạm thời, patch phải có owner và test để không biến mất âm thầm ở lần regenerate sau.

## 32. Domain utility type có thể vô tình phá invariant

`Partial<User>` rất tiện, nhưng một business PATCH command không nhất thiết là “mọi property của User đều optional”. Có field không được đổi, field đổi theo nhóm, hoặc null/absent có semantics khác nhau.

```ts
type UpdateUserCommand = {
  displayName?: string;
  locale?: Locale;
};
```

Explicit command thường tốt hơn:

```ts
type UpdateUserCommand = Partial<User>;
```

nếu `User` còn chứa `id`, audit metadata hoặc derived fields.

Utility types nên transform technical shapes; domain command quan trọng nên encode operation semantics trực tiếp.

## 33. Capability typing cho security tốt hơn role string lan khắp codebase

Một `role: "admin"` không tự bảo đảm action đã được authorize. Một pattern tốt hơn là authorization layer tạo capability/token object chỉ khi policy pass:

```ts
declare const deleteUserCapability: unique symbol;

type DeleteUserCapability = {
  readonly [deleteUserCapability]: true;
  actorId: UserId;
};
```

Domain operation nhận capability thay vì raw role. TypeScript giúp API khó gọi sai hơn, nhưng capability chỉ đáng tin nếu constructor/factory nằm sau runtime authorization và không export escape hatch assertion.

Đây là ví dụ TypeScript hỗ trợ security architecture, không thay thế security check.

## 34. React Server/Client boundary: serializability và execution placement là runtime constraint

Trong React ecosystem hiện đại, server/client component boundary có rules về nơi code chạy và value nào được truyền qua protocol của framework. TypeScript prop type có thể đúng nhưng value vẫn không serializable hoặc object identity/runtime API không tồn tại phía bên kia.

TypeScript nên model DTO/server action result rõ, nhưng canonical semantics của render, RSC, hydration và Actions vẫn thuộc [React docs](../react/00_index.md). Khi lỗi chỉ xuất hiện server build/hydration, đừng thêm assertion vào prop; kiểm tra execution boundary và framework serialization rules trước.

## 35. Monorepo: internal import path có thể phá package boundary dù type-check pass

Trong workspace, developer dễ import sâu:

```ts
import { internalHelper } from "../../packages/domain/src/internal";
```

TypeScript resolve được nên mọi thứ xanh, nhưng architecture boundary đã bị bypass. Khi package đổi layout, build/publish tách riêng hoặc project references được siết, dependency vỡ.

Production practice là import qua public package surface và dùng `exports`/lint/dependency rules để enforce. TypeScript graph chỉ nói dependency **có thể resolve**, không nói dependency **được phép tồn tại theo architecture**.

## 36. Public type change cần compatibility matrix, không chỉ semantic version intuition

Một type refactor có thể breaking theo nhiều chiều:

```text
consumer compiler version
× moduleResolution mode
× ESM/CJS package condition
× strict flags
× runtime target
```

Ví dụ `.d.ts` dùng syntax mới có thể làm TypeScript cũ parse fail; conditional export có thể khiến `bundler` thấy type khác `nodenext`; thêm required generic parameter có thể phá inference dù JavaScript runtime API không đổi.

Library release quan trọng nên có consumer fixtures ở minimum supported TypeScript + current TypeScript và module modes được tuyên bố hỗ trợ.

## 37. `satisfies` cho config tốt khi config vẫn cần runtime validation

`satisfies` rất hữu ích với in-repo config do developer viết vì nó giữ literal inference và bắt typo. Nhưng config đến từ environment variable, JSON deploy file hoặc remote feature flag vẫn là external input.

```ts
const routes = {
  users: { method: "GET", secure: true }
} satisfies RouteConfig;
```

Đây là static proof cho source literal. Nếu cùng structure được load từ JSON, cần parser/validator riêng. Đừng copy type và tin data chỉ vì shape “giống config trong source”.

## 38. Environment variables: `process.env.X as string` là một production smell

Environment variable có thể absent, malformed hoặc khác giữa local/CI/container. Cast từng chỗ phân tán proof giả khắp codebase.

Tốt hơn là parse một lần ở startup:

```ts
type AppConfig = {
  apiBaseUrl: URL;
  timeoutMs: number;
};

function loadConfig(env: Record<string, string | undefined>): AppConfig {
  // validate + normalize, fail fast nếu cấu hình sai
  // ...
  throw new Error("example");
}
```

Sau bootstrap, application nhận `AppConfig` trusted. Điều này biến lỗi config từ random runtime branch thành startup failure có log rõ.

## 39. Async result type không model cancellation, deadline hay ownership

`Promise<User>` không nói operation có thể bị cancel, timeout hay request nào owns result. Nếu API lifecycle quan trọng, contract runtime nên expose `AbortSignal`, deadline/context hoặc state machine phù hợp.

```ts
function loadUser(id: UserId, signal: AbortSignal): Promise<User> {
  // ...
}
```

Ngay cả signature này cũng không “chứng minh cancellation”; nó chỉ tạo capability để runtime implementation phối hợp. TypeScript giúp call site không quên channel, còn temporal correctness vẫn phải test bằng concurrency behavior.

## 40. Observability cho validation/type boundary cần cardinality và privacy discipline

Validation error rất hữu ích nếu log `schemaVersion`, error code/path, producer, endpoint, request ID. Nhưng log toàn raw payload có thể rò PII/secret và tăng cardinality/cost.

Một pattern production tốt là validator trả structured failure reason đã sanitize. Metrics aggregate theo reason/version; trace gắn correlation ID; sample payload chỉ khi policy cho phép. TypeScript có thể type structured diagnostic để logging API không nhận raw domain secret ngoài ý muốn.

## 41. TypeScript 7 adoption: CLI, editor và embedded tooling có thể không cùng version

TypeScript 7.0 có native CLI/language server nhưng chưa có stable programmatic compiler API. Vì vậy framework/tooling nhúng TypeScript có thể vẫn cần TypeScript 6 trong một thời gian.

Một repo có thể chạy:

```text
TS7 tsc trong CI
TS7 language server cho file .ts/.tsx thông thường
TS6 compatibility/API cho typescript-eslint hoặc embedded framework tooling
```

Điều này không sai nếu được quản lý rõ. Failure mode là tưởng tất cả diagnostics đến từ cùng compiler rồi chase khác biệt behavior như bug source code. Upgrade plan phải ghi tool → compiler-version mapping và chỉ bỏ TS6 khi dependency ecosystem đã hỗ trợ API mới.

## 42. Production debugging runbook: đi từ evidence runtime ngược về proof source

Khi một lỗi “TypeScript lẽ ra phải bắt” xuất hiện, trace ngược:

```text
runtime failure
↑ artifact/module actually deployed
↑ serialized/external value actually received
↑ validator/adapter that created trusted value
↑ assertion/declaration/generic proof source
↑ source type model
```

Nếu proof source là `as`, `any`, ambient `.d.ts` hoặc generated declaration, ưu tiên audit nó trước khi làm type phức tạp hơn. Nếu proof hoàn toàn do checker suy ra nhưng runtime vẫn khác, kiểm tra artifact/version/module mismatch. Nếu model đúng mà temporal behavior sai, quay về JavaScript concurrency/runtime.

Senior TypeScript là khả năng nối **proof tĩnh** với **evidence động** và biết chính xác chỗ hai thế giới tách nhau.

---

Hoàn tất track: quay lại [TypeScript Index](typescript_00_index.md) để review coverage và glossary.
