# TypeScript 02 — Type System Internals & Generic Modeling

> Prerequisite: [Foundations & Runtime Boundary](typescript_01_foundations.md). Chapter này tập trung vào cách checker reasoning, không phải sưu tầm type trick.

## 1. Structural typing: compatible vì shape, không phải vì tên

Trong nominal type system, hai class/type có thể khác nhau chỉ vì chúng mang identity khác. TypeScript chủ yếu dùng **kiểu cấu trúc (structural typing / 구조적 타이핑)** để phù hợp JavaScript ecosystem: nếu source có đủ capability target yêu cầu, assignment thường hợp lệ.

```ts
type Point = {
  x: number;
  y: number;
};

const pixel = {
  x: 10,
  y: 20,
  color: "red"
};

const point: Point = pixel;
```

`pixel` không cần `implements Point`; shape đủ là được. Điều này làm composition tự nhiên và library interoperability tốt, nhưng cũng có nghĩa type name không tự tạo domain identity.

Ví dụ `UserId` và `OrderId` cùng là `string` sẽ assign được cho nhau nếu chỉ alias:

```ts
type UserId = string;
type OrderId = string;
```

Khi domain cần phân biệt identity, có thể dùng branded/opaque-like pattern:

```ts
declare const userIdBrand: unique symbol;

type UserId = string & {
  readonly [userIdBrand]: "UserId";
};
```

Đây là compile-time modeling, không tự thêm runtime tag. Boundary tạo `UserId` vẫn phải validate string format nếu format có invariant.

## 2. Assignability là câu hỏi trung tâm của checker

Nhiều diagnostic thực chất hỏi: source type có **assignable** tới target type không? Với object, checker xét required properties, property types, readonly/optional rules, index signatures, call signatures và generic relationships.

Khi error quá dài, giảm nó thành source → target:

```text
Source<TActual>
     ↓ assignable?
Target<TExpected>
```

Sau đó tìm property/type parameter đầu tiên làm quan hệ vỡ. Đây hiệu quả hơn đọc hàng chục dòng nested diagnostic như prose.

## 3. Generic không phải “any có type đẹp hơn”

Generic dùng khi nhiều input/output có quan hệ mà bạn muốn giữ.

```ts
function identity<T>(value: T): T {
  return value;
}

const a = identity("hello"); // string
const b = identity(42);      // number
```

Nếu viết:

```ts
function badIdentity(value: any): any {
  return value;
}
```

relationship giữa input và output bị mất. Generic giữ information xuyên qua abstraction.

Một generic có ý nghĩa khi type parameter xuất hiện ở quan hệ thực. Function dưới đây không cần generic:

```ts
function logValue<T>(value: T): void {
  console.log(value);
}
```

Nếu `T` không giúp caller hay implementation duy trì relation nào, `unknown` có thể rõ hơn:

```ts
function logValue(value: unknown): void {
  console.log(value);
}
```

## 4. Constraint: abstraction vẫn cần capability

Generic `T` có thể quá rộng để dùng property cụ thể:

```ts
function getLength<T>(value: T) {
  // value.length không chắc tồn tại
}
```

Constraint nói mọi T hợp lệ phải có capability nào:

```ts
function getLength<T extends { length: number }>(value: T): number {
  return value.length;
}
```

`extends` ở đây không có nghĩa class inheritance runtime. Nó đặt relation ở type system.

Một pattern thường gặp:

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

`K` không phải string tùy ý; nó bị constraint bởi key space của T. Return type giữ chính xác type của property được chọn.

## 5. Generic inference lấy evidence từ nhiều phía

TypeScript suy type argument từ actual arguments, contextual target và constraints. Khi inference thất bại, đừng lập tức viết explicit `<SomeType>`; hãy hỏi information bị mất ở boundary nào.

```ts
function pair<T>(left: T, right: T): [T, T] {
  return [left, right];
}
```

Nếu two arguments không thể tìm common inference phù hợp, diagnostic cho thấy abstraction đang nói “hai giá trị cùng T” trong khi domain có thể cần hai type parameters:

```ts
function pair<A, B>(left: A, right: B): [A, B] {
  return [left, right];
}
```

Đừng nới generic chỉ để compiler im; sửa relationship cho đúng intent.

## 6. Variance: vì sao callback type có thể nguy hiểm

Giả sử `Dog` assignable tới `Animal`. Câu hỏi `Box<Dog>` có assignable tới `Box<Animal>` không phụ thuộc `Box` dùng T như thế nào.

Nếu T chỉ đi ra:

```ts
type Producer<T> = () => T;
```

Producer thường có xu hướng covariance: producer Dog có thể dùng nơi cần producer Animal.

Nếu T chỉ đi vào:

```ts
type Consumer<T> = (value: T) => void;
```

relation đi chiều khác vì một consumer chỉ biết xử lý Dog không an toàn ở nơi hệ thống có thể đưa bất kỳ Animal nào.

Nếu T vừa vào vừa ra, container thường cần invariant-like reasoning hơn.

Array là ví dụ JavaScript thực dụng khiến variance có edge case. Mutable collection có write operations, nên relation subtype trực giác có thể dẫn tới unsafe mutation nếu system quá permissive. `readonly` collection giảm write capability và làm relation dễ reasoning hơn.

Senior lesson: variance không phải từ học thuật để nhớ. Nó trả lời “generic abstraction này cho phép data chảy vào hay ra theo hướng nào?”.

## 7. `keyof`, indexed access và `typeof` là cầu nối structure → type

`keyof` biến object type thành union keys:

```ts
type User = {
  id: string;
  age: number;
};

type UserKey = keyof User; // "id" | "age"
```

Indexed access lấy property type:

```ts
type Id = User["id"]; // string
```

`typeof` trong type position lấy static type của value binding:

```ts
const config = {
  retry: 3,
  mode: "safe"
} as const;

type Config = typeof config;
```

Đây là pattern tốt khi runtime config là source of truth và bạn muốn derive type từ nó, thay vì maintain hai definitions dễ drift.

## 8. Mapped type: transform từng property theo key space

Mapped type giống một phép biến đổi trên keys:

```ts
type Optional<T> = {
  [K in keyof T]?: T[K];
};
```

Mental model:

```text
key space của T
  ↓ iterate K
property mới cho từng K
  ↓
shape transformed
```

Built-in utilities như `Partial<T>`, `Required<T>`, `Readonly<T>` dựa trên cơ chế này. Học implementation conceptually giúp bạn tự thiết kế transformation nhưng không nên copy type gymnastics nếu utility chuẩn đã diễn đạt intent.

Key remapping cho phép đổi/lọc key:

```ts
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

Khi mapped type trở nên khó đọc hơn business rule nó mô tả, hãy cân nhắc explicit interface. Type-level abstraction cũng có maintenance cost.

## 9. Conditional type: branch ở tầng type

```ts
type ElementType<T> = T extends readonly (infer U)[] ? U : T;
```

Conditional type hỏi relation assignability và chọn branch. Với naked type parameter, nó có thể **phân phối (distribute)** qua union:

```ts
type ToArray<T> = T extends unknown ? T[] : never;
type Result = ToArray<string | number>;
// string[] | number[]
```

Nếu muốn đánh giá union như một khối, wrap hai phía:

```ts
type ToArrayNonDistributed<T> = [T] extends [unknown] ? T[] : never;
```

Distribution là nguồn của cả sức mạnh lẫn diagnostic complexity. Khi conditional type lồng sâu, luôn tự hỏi input domain có thật sự cần type-level branching đó không.

## 10. `infer`: đặt tên phần cấu trúc đang match

`infer` chỉ xuất hiện trong conditional type matching context. Nó không “đoán mọi thứ”; nó capture một phần của structure nếu relation match.

```ts
type Return<T> = T extends (...args: any[]) => infer R ? R : never;
```

Với Promise-like:

```ts
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;
```

Khi nested promise/thenable semantics phức tạp, built-in `Awaited<T>` thường đúng hơn custom utility vì nó model edge cases chuẩn hơn.

## 11. Template literal type: string pattern ở type level

```ts
type EventName = "created" | "updated";
type HandlerName = `on${Capitalize<EventName>}`;
// "onCreated" | "onUpdated"
```

Feature này hữu ích khi runtime API thật sự có naming convention ổn định. Nhưng nếu bạn tạo union hàng nghìn combination, compiler phải materialize/compare nhiều type hơn. Dùng template literal types để encode protocol nhỏ, không để tạo “type programming language” vô hạn.

## 12. Recursive type và giới hạn compiler

Type có thể tham chiếu cấu trúc lặp:

```ts
type Json =
  | null
  | boolean
  | number
  | string
  | Json[]
  | { [key: string]: Json };
```

Recursive conditional/mapped types mạnh hơn nhưng có thể chạm instantiation depth, tăng memory/check time hoặc tạo diagnostic rất khó đọc. Đây là nơi performance pressure thay đổi design: type chính xác hơn một chút chưa chắc đáng đổi build latency và cognitive load.

## 13. Utility types nên hiểu từ primitive operation

`Pick<T, K>` giữ subset keys. `Omit<T, K>` loại keys. `Record<K, V>` tạo map shape. `Exclude<A, B>` loại union members assignable tới B. `Extract<A, B>` giữ phần assignable. `Parameters<F>` và `ReturnType<F>` phân tích function signature. `Awaited<T>` unwrap async/thenable semantics.

Không học utilities như flashcard. Hãy hỏi utility đang thao tác trên key space, union space hay function structure.

## 14. `never` trong conditional type và union filtering

`never` biến mất khỏi union:

```ts
type OnlyString<T> = T extends string ? T : never;
type R = OnlyString<string | number | boolean>; // string
```

Đây là nền của nhiều filter utilities. Khi kết quả bất ngờ thành `never`, trace từng branch: input type đã bị constraint quá hẹp, property intersection mâu thuẫn, hay conditional đã distribute ngoài ý muốn?

## 15. `unknown` trong generic boundary tốt hơn `any`

Ví dụ parser generic thường bị viết sai:

```ts
function parse<T>(raw: string): T {
  return JSON.parse(raw);
}
```

Function này hứa rằng caller chọn T nào cũng được và implementation sẽ tạo đúng T, nhưng implementation không có validation. Generic đang tạo false proof.

API trung thực hơn:

```ts
function parse(raw: string): unknown {
  return JSON.parse(raw);
}
```

Sau đó validate/narrow ở boundary. Generic không nên được dùng để “teleport” external data vào domain type.

## 16. Function overload và union/generic: chọn theo relationship

Overload hữu ích khi API có vài call shapes rời rạc với return relation rõ:

```ts
function parseValue(value: string): number;
function parseValue(value: number): string;
function parseValue(value: string | number): string | number {
  return typeof value === "string" ? Number(value) : String(value);
}
```

Nếu call shapes có một generic relation liên tục, generic thường scale tốt hơn. Nếu chỉ cần “A hoặc B” mà output không phụ thuộc input member, union đơn giản hơn overload. Đừng chọn overload chỉ vì trông “senior”.

## 17. Declaration merging và module augmentation: sức mạnh có global cost

`interface` có thể merge khi declarations cùng tên/scope:

```ts
interface Window {
  appVersion: string;
}
```

Module augmentation cho phép bổ sung type vào module bên ngoài. Đây hữu ích cho plugin ecosystem nhưng có thể làm contract xuất hiện “từ xa”, khó trace. Application code nên giữ augmentation tập trung, tên file rõ, test compile và tránh dùng nó thay cho explicit adapter.

## 18. Exactness: TypeScript object type thường là minimum requirements, không phải sealed object

`type User = { id: string }` thường có nghĩa “ít nhất có id string” trong structural relation, không có nghĩa object runtime chỉ được đúng một property. Excess property checking trên fresh literal là diagnostic convenience, không biến object type thành exact/sealed record.

Nếu protocol cần reject extra properties, đó là runtime validation/schema concern. Đừng kỳ vọng type alias thay parser.

## 19. `noUncheckedIndexedAccess` thay đổi mental model của lookup

Mặc định, indexed access vào `Record<string, User>` có thể cho cảm giác key luôn tồn tại. Khi bật `noUncheckedIndexedAccess`, lookup thường thêm `undefined`, phản ánh đúng hơn runtime map access:

```ts
const user = usersById[id];
if (!user) {
  // handle missing
}
```

Strict flag này làm code verbose hơn nhưng buộc missing-key invariant trở thành explicit. Với data structure thật sự total, hãy model key space hữu hạn hoặc xây abstraction chứng minh invariant thay vì cast sau mỗi lookup.

## 20. `exactOptionalPropertyTypes` làm optional gần semantics runtime hơn

Khi bật option này, `{ value?: string }` không còn tự động đồng nghĩa “value có thể được gán undefined” theo cách rộng trước đây. Nó nhấn mạnh distinction giữa absent property và present-with-undefined, rất hữu ích cho PATCH payload, config merge và serialization.

## 21. Type performance: compiler cũng là một consumer của API design

Một type definition có thể correct nhưng đắt. Dấu hiệu: editor hover chậm, autocomplete delay, `tsc` check time tăng mạnh, diagnostic có type khổng lồ. Nguyên nhân thường gặp gồm giant unions, deeply recursive conditional types, distributive transformations trên union lớn, repeated anonymous intersections và generic APIs bắt checker suy luận quá nhiều path.

Senior practice là profile trước khi tối ưu, rồi đơn giản hóa public types, đặt alias cho intermediate result, tránh union explosion, và đôi khi chấp nhận type ít “ma thuật” hơn để build predictable hơn.

## 22. API design: giữ generic ở boundary nhỏ nhất có ích

Type parameter quá nhiều làm caller phải giải puzzle. Một library API tốt thường để caller truyền data tự nhiên, inference lấy phần lớn thông tin, và chỉ expose explicit generic khi thật sự cần control.

Ví dụ repository interface:

```ts
interface Repository<TEntity, TId> {
  getById(id: TId): Promise<TEntity | null>;
  save(entity: TEntity): Promise<void>;
}
```

Hai parameters có relationship rõ. Nếu thêm `TContext`, `TError`, `TOptions`, `TTransport`, `TMeta` chỉ để “future proof”, abstraction có thể đang vượt quá domain evidence hiện có.

## 23. Senior note: type system là công cụ mô hình hóa invariant

Một advanced type chỉ có giá trị nếu nó làm illegal state khó represent hơn, giữ relationship quan trọng qua abstraction, hoặc giúp refactor an toàn. Nếu người đọc phải chạy mental compiler để hiểu business rule, bạn đã chuyển complexity từ runtime sang source mà chưa chắc giảm tổng complexity.

---

Tiếp theo: [TypeScript 03 — Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md).
