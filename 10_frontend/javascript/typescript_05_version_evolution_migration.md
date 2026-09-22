# TypeScript 05 — Version Evolution & Migration

> Prerequisite: [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md). Chapter này không phải danh sách “feature mới theo version”. Mục tiêu là hiểu **vì sao TypeScript thay đổi**, thay đổi đó nằm ở type system, compiler, module host hay tooling layer nào, và một codebase production phải reasoning thế nào khi nâng version.

Baseline của track hiện tại là **TypeScript 7.0**. Khi đọc tài liệu cũ hoặc maintain project legacy, đừng hỏi duy nhất “feature này có từ version nào?”. Câu hỏi quan trọng hơn là: version mới có làm thay đổi proof mà checker suy ra không, có đổi JavaScript emit không, có đổi module resolution không, có đổi declaration/public API không, hay chỉ thay compiler architecture và performance?

## 1. Mental model: version number không đồng nghĩa language generation

TypeScript tiến hóa trên nhiều trục cùng lúc. Một release có thể thêm syntax/type-system feature nhưng gần như không đổi runtime artifact; release khác có thể giữ type semantics gần như nguyên vẹn nhưng thay toàn bộ compiler implementation. TypeScript 4.9 với `satisfies` là ví dụ của thay đổi type-model ergonomics. TypeScript 5.0 thay đổi decorator semantics và module emit controls. TypeScript 6.0 chủ yếu là transition release với default/deprecation cleanup. TypeScript 7.0 lại là architectural generation change: compiler và language service chuyển sang native Go implementation trong khi cố giữ checking behavior tương thích với 6.0.

Vì vậy khi upgrade, hãy tách ít nhất năm câu hỏi:

```text
source syntax có đổi không?
→ checker/inference có đổi không?
→ emit có đổi không?
→ module/package resolution có đổi không?
→ compiler/editor/build architecture có đổi không?
```

Nếu không tách năm lớp này, team rất dễ gọi một runtime ESM failure là “TypeScript 7 bug”, hoặc ngược lại coi một inference tightening là “chỉ tooling change”.

## 2. Timeline tổng quát

| Giai đoạn | Chuyển dịch chính | Tác động mental model |
|---|---|---|
| TypeScript 1.x | annotation, interface, class, generic | JavaScript có thêm static contract layer |
| TypeScript 2.x | control-flow analysis, strict nullability, mapped/conditional type foundations | type bắt đầu được suy ra từ control flow và type transformation |
| TypeScript 3.x | `unknown`, project references, tuple/inference improvements, optional chaining/nullish coalescing ở cuối 3.x | trust boundary và large-project build model trưởng thành |
| TypeScript 4.x | variadic tuple, template literal type, recursive conditional type, stronger CFA, `satisfies` | type-level programming trở thành công cụ API modeling mạnh |
| TypeScript 5.x | standard decorators, const type parameters, modern module controls, `NoInfer`, inferred predicates, isolated declarations, direct-TS runtime support | TypeScript dịch từ “transpiler + checker” sang một thành phần trong toolchain đa compiler/runtime |
| TypeScript 6.0 | transition/deprecation/default cleanup | ép project khai báo assumption hiện đại trước native compiler |
| TypeScript 7.0 | native Go compiler/language service, parallel architecture | semantics gần 6.0 nhưng scale/build/editor model thay đổi lớn |

Bảng này chỉ là map. Phần dưới giải thích các mốc có ảnh hưởng lâu dài đến code hiện đại.

## 3. TypeScript 1.x–3.x: legacy knowledge vẫn xuất hiện trong production

TypeScript 1.x đặt vocabulary cơ bản: annotation, interface, class và generic. Những concept này vẫn tồn tại, nhưng code hiện đại không nên học TypeScript như “Java/C# syntax đặt lên JavaScript”. Structural typing, inference và JavaScript runtime semantics quan trọng hơn việc ghi nhớ keyword.

TypeScript 2.x là giai đoạn hệ kiểu trở nên gần với TypeScript hiện đại. Control-flow based type analysis khiến type của một variable có thể được narrow theo branch thay vì chỉ giữ declared type. `strictNullChecks` biến `null`/`undefined` từ giá trị gần như có thể đi khắp nơi thành trạng thái phải model. Mapped/conditional type family mở đường cho type transformation thay vì chỉ khai báo shape thủ công.

TypeScript 3.x tiếp tục làm trust boundary rõ hơn với `unknown`, đồng thời project references tạo mô hình build graph cho repository lớn. Optional chaining `?.` và nullish coalescing `??` xuất hiện cuối 3.x, nhưng cần nhớ đây là JavaScript runtime syntax được TypeScript hỗ trợ, không phải bằng chứng rằng dữ liệu bên ngoài đã được validate.

Khi maintain code legacy, dấu hiệu của mental model cũ thường là non-strict null handling, namespace/ambient global lớn, decorator legacy, CommonJS interop workaround và cast dày đặc. Không rewrite chỉ vì syntax cũ; trước tiên xác định runtime/module assumptions và public ABI.

## 4. TypeScript 4.x: type-level programming trở thành mainstream

### 4.1 TypeScript 4.0 — variadic tuple types

Variadic tuple types làm generic function giữ được quan hệ giữa nhiều parameter/return positions mà trước đây cần overload dài. Giá trị của feature không phải “tuple syntax mạnh hơn”, mà là khả năng biểu diễn relation như concat, partial application hay middleware pipeline mà không làm mất positional information.

```ts
function tail<T extends readonly unknown[]>(
  value: readonly [unknown, ...T]
): T {
  const [, ...rest] = value;
  return rest;
}
```

Đây là bước quan trọng dẫn tới API generic có inference tốt hơn, nhưng cũng mở cửa cho type-level abstraction quá phức tạp. Production rule vẫn là: relation phải có giá trị domain/API rõ ràng mới đáng trả cognitive cost.

### 4.2 TypeScript 4.1 — template literal types và key remapping

Template literal types cho phép tạo string union từ type information; mapped type có thể remap key bằng `as`. Từ đây TypeScript có thể model event names, route keys, getter/setter conventions và DSL nhỏ ở compile time.

```ts
type EventName<T extends string> = `${T}Changed`;

type UserEvent = EventName<"name" | "email">;
// "nameChanged" | "emailChanged"
```

Power này có combinatorial cost. Nếu union A có hàng trăm member và được nhân với union B/C, editor latency có thể trở thành production problem. TypeScript 7 nhanh hơn không làm exponential type shape biến mất.

### 4.3 TypeScript 4.4 — control-flow analysis và optional-property semantics trưởng thành hơn

4.4 cải thiện control-flow analysis qua aliased conditions/discriminants. Nó cũng đưa `exactOptionalPropertyTypes` và `useUnknownInCatchVariables` vào câu chuyện strictness hiện đại.

Điểm quan trọng của `exactOptionalPropertyTypes` là phân biệt “property không tồn tại” với “property tồn tại nhưng value là `undefined`” khi type không cho phép `undefined`. Hai trạng thái có thể khác nhau ở object spread, serialization, `in` check và API patch semantics.

### 4.4 TypeScript 4.7 — Node ESM trở thành module-resolution concern chính thức

Các mode `node16`/`nodenext` khiến TypeScript phải model gần hơn behavior của Node: package `type`, file extension, conditional exports và ESM/CJS boundary. Đây là mốc quan trọng vì từ đây “IDE resolve được import” không còn đủ để chứng minh runtime host sẽ load module giống vậy.

### 4.5 TypeScript 4.9 — `satisfies`

`satisfies` giải quyết tension giữa **validation của expression** và **giữ inference cụ thể của expression**.

```ts
type Route = "home" | "settings";

const paths = {
  home: "/",
  settings: "/settings"
} satisfies Record<Route, string>;
```

Khác với annotation rộng, `satisfies` kiểm tra compatibility mà không ép resulting expression type thành target type. Nó đặc biệt hữu ích cho config object, route map, token map và registry. Nhưng `satisfies` vẫn là compile-time proof; nó không validate JSON/config được đọc ở runtime.

## 5. TypeScript 5.x: modern TypeScript toolchain

TypeScript 5.x nên được xem như một chuỗi thay đổi làm rõ ranh giới giữa TypeScript checker và JavaScript ecosystem xung quanh nó.

### 5.1 TypeScript 5.0 — decorators, const type parameters và module emit rõ hơn

5.0 hỗ trợ decorator semantics mới theo hướng ECMAScript proposal mà không cần legacy `experimentalDecorators`. Legacy decorators vẫn là một mode khác với behavior/type-checking khác; standard decorators không đơn giản là rename API cũ. Codebase dùng framework/decorator metadata phải kiểm tra framework support trước migration.

`const` type parameters cho library author yêu cầu inference literal-specific ngay từ API boundary:

```ts
function defineRoutes<const T extends readonly string[]>(routes: T) {
  return routes;
}

const routes = defineRoutes(["/", "/users"]);
```

5.0 cũng giới thiệu `verbatimModuleSyntax`. Mental model là: import/export không có `type` modifier được giữ theo module syntax; type-only import/export bị erase. Điều này giảm “compiler đoán hộ import nào là runtime value” và làm source code nói rõ hơn artifact intent.

`moduleResolution: "bundler"` phản ánh một host khác Node trực tiếp. Đây không phải “nodenext dễ hơn”; nó model resolver assumptions của bundler. Library publish cho Node consumers vẫn phải test consumer dưới `node16`/`nodenext` khi phù hợp.

### 5.2 TypeScript 5.2 — explicit resource management

5.2 hỗ trợ `using`/`await using` theo explicit resource management semantics. Bản chất là đưa resource lifetime vào syntax/protocol thay vì dựa hoàn toàn vào convention `try/finally`.

Đừng suy ra TypeScript tự quản lý mọi resource. Object phải tham gia disposal protocol phù hợp; database transaction, lock hay file handle vẫn cần API implementation đúng. Đây là ví dụ nơi language syntax làm lifecycle explicit nhưng runtime invariant vẫn thuộc implementation.

### 5.3 TypeScript 5.4 — `NoInfer`

`NoInfer<T>` cho phép API author chặn một vị trí trở thành nguồn candidate cho generic inference. Nó hữu ích khi một parameter phải **được kiểm tra theo T đã suy ra từ nơi khác**, thay vì cùng tham gia quyết định T.

```ts
function choose<C extends string>(
  choices: C[],
  fallback: NoInfer<C>
) {}

choose(["red", "green"], "blue"); // error
```

Mental model: `NoInfer` điều khiển **direction of inference**, không tạo nominal type và không validate runtime value.

### 5.4 TypeScript 5.5 — inferred type predicates và isolated declarations

5.5 có thể infer type predicate cho một số boolean function đủ rõ. Điều này làm patterns như `.filter(x => x !== undefined)` giữ type chính xác hơn mà không cần custom guard thủ công.

Cùng release này, `isolatedDeclarations` yêu cầu exported surface đủ annotation để declaration generation có thể được thực hiện mà không cần full cross-file type inference. Đây là một thay đổi kiến trúc quan trọng cho monorepo/build tool: public API rõ hơn đổi lấy annotation burden lớn hơn, nhưng mở đường cho declaration emit song song hoặc tool khác ngoài TypeScript compiler.

### 5.5 TypeScript 5.7 — relative TypeScript import có thể được rewrite cho output

`rewriteRelativeImportExtensions` giải quyết một phần friction khi source dùng extension `.ts`/`.tsx`/`.mts`/`.cts` nhưng emitted JavaScript cần extension runtime tương ứng. Đây là emit convenience, không giải quyết package alias hay arbitrary runtime resolver.

Nếu source import `@app/user`, TypeScript không thể chỉ từ option này biết bundler/runtime phải rewrite alias thành gì. Module specifier vẫn là contract với host.

### 5.6 TypeScript 5.8 — `erasableSyntaxOnly` và direct-TypeScript runtimes

Khi runtime/tool có thể strip type syntax và chạy TypeScript trực tiếp, không phải mọi TypeScript construct đều an toàn. `enum`, parameter properties, namespace có runtime code và một số TypeScript-specific module forms cần transformation chứ không chỉ erase type.

`erasableSyntaxOnly` giúp project giới hạn source vào syntax có thể bị type-strip mà không cần TypeScript-specific runtime transform. Đây là bridge quan trọng giữa checker và runtime như Node có type-stripping support.

Mental model:

```text
TypeScript syntax
├─ erasable type syntax → runtime có thể strip
└─ syntax tạo runtime behavior → cần transform/emitter hiểu TypeScript
```

### 5.7 TypeScript 5.9 — config/module ergonomics trước transition lớn

5.9 tiếp tục chuẩn hóa setup hiện đại. `tsc --init` sinh config gọn hơn nhưng với các assumption hiện đại như `strict`, `verbatimModuleSyntax`, `isolatedModules`, `noUncheckedSideEffectImports` và các stricter options đáng cân nhắc. Đây là tín hiệu rằng “default project shape” đã dịch xa khỏi TypeScript legacy target/module assumptions.

Điều quan trọng khi đọc generated config là hiểu từng option thuộc checker, emit hay host model nào. Copy một `tsconfig` mới vào legacy application mà không hiểu bundler/runtime không phải migration strategy.

## 6. TypeScript 6.0: transition release, không phải “TypeScript 7 lite”

TypeScript 6.0 phát hành ngày 23/03/2026 và là stable release cuối cùng trên compiler codebase JavaScript cũ. Vai trò lớn nhất của nó là **bridge từ 5.9 sang native TypeScript 7**.

6.0 tiếp tục loại bỏ/deprecate assumptions không còn phù hợp với ecosystem hiện đại và chuẩn bị behavior/defaults cho 7.0. Project đang ở 5.x nên coi 6.0 là migration checkpoint: xử lý deprecation, explicit hóa config và kiểm tra module/package behavior trước khi đổi compiler generation.

Một migration đúng không nên làm:

```text
5.x → 7.0 → thấy hàng trăm error → thêm ignore/cast cho build xanh
```

Nên reasoning:

```text
5.x
→ upgrade 6.0
→ bỏ deprecated config/behavior
→ chạy typecheck + declaration + runtime/module tests
→ ổn định consumer contracts
→ thử 7.0
```

6.0 vẫn giữ compiler API compatibility lineage của 5.x, trong khi 7.0 native architecture không cung cấp programmatic API giống 6.x ở cùng hình thức. Tool/plugin phụ thuộc sâu vào compiler API vì thế cần được audit riêng với source application.

## 7. TypeScript 7.0: compiler generation thay đổi, type knowledge không reset

TypeScript 7.0 stable từ 08/07/2026. Đây là native port của compiler và language service sang Go, sử dụng native execution và shared-memory parallelism. Type-checking logic được port có chủ đích để tương thích sát với TypeScript 6.0 thay vì thiết kế một hệ kiểu mới.

Đây là distinction quan trọng:

```text
TypeScript 6 → 7
language/type semantics: continuity
compiler architecture: major discontinuity
```

Do đó generic, conditional type, narrowing, `satisfies`, `NoInfer` hay discriminated union không trở thành kiến thức “TypeScript cũ”. Thứ thay đổi mạnh là performance envelope, editor/language-service architecture, project build scheduling và compatibility với tooling dựa vào compiler internals/API cũ.

7.0 nhận các default/cleanup đã được chuẩn bị từ 6.0. Ví dụ đáng chú ý gồm `strict` mặc định `true`, `module` mặc định `esnext`, và `target` mặc định dịch về ECMAScript stable gần `esnext` thay vì legacy target. Điều này có nghĩa một project phụ thuộc vào default ngầm có thể đổi behavior dù source không đổi.

Senior rule là **pin assumptions**. Production `tsconfig` quan trọng nên explicit những option quyết định runtime/module contract thay vì dựa vào default chỉ vì default hiện tại phù hợp.

## 8. Vì sao upgrade TypeScript có thể tạo error dù runtime code “không đổi”?

Có bốn nguồn phổ biến.

Thứ nhất là inference/correctness fix. Checker mới có thể suy ra type chính xác hơn, khiến code từng compile nhờ type rộng hoặc unsound edge case bắt đầu fail. Đây không nhất thiết là regression.

Thứ hai là `lib.d.ts`/DOM types thay đổi theo platform standards. Application code không đổi nhưng ambient platform contract đổi.

Thứ ba là module resolution/config defaults thay đổi. Type-check pass/fail có thể khác vì compiler model package `exports`, extension hoặc host condition khác.

Thứ tư là declaration ecosystem. Dependency update hoặc TypeScript version mới có thể parse/check `.d.ts` khác, dù JavaScript dependency runtime vẫn giống trước.

Vì vậy migration bug report nên ghi rõ ít nhất:

```text
old TS version / new TS version
old tsconfig / effective new tsconfig
runtime + bundler version
module/package mode
exact diagnostic
whether JS emit changed
whether .d.ts emit changed
whether runtime test changed
```

## 9. Version compatibility của library khác application

Application có thể pin một TypeScript version và compiler config. Library publish ra ecosystem phải sống với nhiều consumer versions và nhiều module hosts.

Nếu public `.d.ts` dùng syntax/type feature mới, minimum TypeScript version của consumer tăng ngay cả khi JavaScript runtime output vẫn tương thích browser cũ. Đây là **type-level breaking compatibility**.

Library author nên test ít nhất ba surfaces:

```text
runtime artifact
public declaration artifact
consumer compilation
```

Nếu package hỗ trợ nhiều TypeScript generation, `typesVersions` hoặc versioned `types` conditions có thể cần thiết. Nhưng mỗi compatibility branch là maintenance cost; đừng support compiler quá cũ chỉ bằng một claim trong README mà không có consumer fixture.

## 10. Migration playbook từ 5.x/6.x lên 7.0

### Bước 1 — ghi lại baseline trước upgrade

Chạy typecheck/build/test hiện tại và lưu effective config. Với codebase lớn, đo cold check, incremental check, editor latency và memory để có evidence so sánh.

### Bước 2 — tách application source khỏi tooling dependency

Search các package/plugin có import từ `typescript`, custom transformer, language-service plugin hoặc compiler API integration. Source `.ts` có thể migrate dễ nhưng tooling này có compatibility story khác với native 7.0.

### Bước 3 — đi qua 6.0 nếu project còn ở 5.x

Xử lý deprecation và config assumptions ở 6.0 trước. Không dùng `ignoreDeprecations` như trạng thái cuối; nó chỉ trì hoãn work mà 7.0 có thể biến thành hard incompatibility.

### Bước 4 — kiểm tra module boundary bằng runtime thật

Typecheck không đủ. Chạy Node/browser/bundler tests, package consumer fixtures và SSR/build path thật. Đặc biệt kiểm tra ESM/CJS, package `exports`, file extensions, side-effect imports và path aliases.

### Bước 5 — diff declaration output

Nếu project publish package, diff `.d.ts`. Một upgrade compiler có thể làm declaration surface thay đổi do inference/emit improvements dù runtime JavaScript gần như không đổi.

### Bước 6 — phân loại diagnostic thay vì suppress hàng loạt

Mỗi error mới nên thuộc một nhóm: real bug được checker mới bắt, inference behavior change, declaration dependency incompatibility, config/module mismatch hoặc tooling incompatibility. Chỉ sau khi biết category mới chọn fix.

### Bước 7 — đo performance sau khi correctness ổn

TypeScript 7 thường nhanh hơn đáng kể nhờ native architecture và parallelism, nhưng benchmark phải trên repository thật. Generated types, giant unions, recursive conditional types và project graph xấu vẫn có thể tạo hotspot.

## 11. Khi đọc code cũ, version clue nói gì?

Nếu thấy `namespace` lớn và triple-slash references, code có thể đến từ thời pre-ESM TypeScript hoặc từ library cần ambient integration. Nếu thấy `importsNotUsedAsValues`/`preserveValueImports`, đó là module-emit configuration trước `verbatimModuleSyntax`. Nếu thấy decorator dựa vào `experimentalDecorators` + `emitDecoratorMetadata`, đừng tự động chuyển sang standard decorators. Nếu thấy nhiều overload chỉ để giữ tuple positions, có thể code được viết trước variadic tuple types. Nếu thấy helper guard thủ công quanh `.filter`, code có thể predates inferred type predicates hoặc cần behavior mà inference không đủ.

Version archaeology không nhằm rewrite cho “mới”. Nó giúp hiểu **constraint lịch sử nào đã tạo ra design hiện tại**, rồi quyết định constraint đó còn tồn tại không.

## 12. Khi nào nên dùng feature mới?

Feature mới đáng adoption khi nó loại một class bug, làm contract rõ hơn hoặc giảm complexity mà không tăng compatibility cost quá mức. `satisfies` thường có ROI cao cho config. `NoInfer` hữu ích trong API generic có inference direction rõ. `isolatedDeclarations` đáng cân nhắc khi monorepo/build architecture thực sự hưởng lợi. `erasableSyntaxOnly` phù hợp khi runtime strategy là direct type stripping.

Không nên adoption chỉ vì compiler hỗ trợ. Nếu package phải support consumer TypeScript cũ, public type syntax mới có thể phá downstream. Nếu team chưa dùng direct `.ts` runtime, bật constraint phục vụ type stripping có thể chỉ tăng friction. Version-aware engineering là chọn feature theo system constraint, không theo release-note excitement.

## 13. Checklist reasoning khi nâng version

Trước khi merge upgrade, reviewer phải trả lời được: compiler version đổi từ đâu sang đâu; release nào ở giữa có deprecation/breaking behavior; effective `tsconfig` thay đổi gì; module resolver đang model Node hay bundler; JavaScript emit có diff không; declaration emit có diff không; dependency `.d.ts` có yêu cầu minimum TS mới không; compiler API/plugin nào bị ảnh hưởng; runtime/consumer fixture đã chạy chưa; và performance measurement có so với baseline không.

Nếu không trả lời được các câu trên, “CI xanh” chỉ chứng minh test hiện có chưa thấy lỗi, không chứng minh migration boundary đã được hiểu.

## 14. Cross-links trong canonical track

Để hiểu feature theo bản chất thay vì theo timeline, quay lại [Type System Internals](typescript_02_type_system.md) cho inference, predicate, `NoInfer`, tuple và type-level complexity; đọc [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md) cho module resolution, declaration, direct-TypeScript runtime, project graph và TypeScript 7 internals; đọc [Senior Production Engineering](typescript_04_senior_production.md) cho migration, library compatibility, runtime validation và production evidence.

Version guide này chỉ trả lời câu hỏi **“knowledge đó xuất hiện/thay đổi qua các release như thế nào và migration consequence là gì?”**. Nó không duplicate giải thích đầy đủ của các canonical chapter kia.

## 15. Nguồn chuẩn

Version facts trong chapter này ưu tiên tài liệu chính thức của TypeScript Team:

- TypeScript Handbook — Release Notes: `https://www.typescriptlang.org/docs/handbook/release-notes/`
- TSConfig Reference: `https://www.typescriptlang.org/tsconfig/`
- Announcing TypeScript 6.0: `https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/`
- Announcing TypeScript 7.0: `https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/`

Khi release mới xuất hiện, không append mọi feature vào đây. Chỉ thêm feature nếu nó thay đổi mental model, migration behavior, compiler/tooling architecture, runtime/module contract hoặc compatibility surface.

---

Tiếp theo: quay lại [TypeScript Index](typescript_00_index.md) hoặc dùng chapter này như migration map khi đọc codebase ở version cũ.