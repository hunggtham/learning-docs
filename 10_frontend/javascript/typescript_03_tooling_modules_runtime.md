# TypeScript 03 — Compiler, Modules & Tooling

> Prerequisite: [Type System Internals](typescript_02_type_system.md). Chapter này giải thích vì sao code type-correct vẫn có thể fail ở build/runtime nếu module, emit hoặc environment model sai.

## 1. `tsc` thực sự làm những việc gì?

Một mental model đơn giản là:

```text
files + tsconfig
  ↓ parse
syntax tree
  ↓ bind
symbols / scopes
  ↓ check
assignability + inference + diagnostics
  ↓ optional emit
JavaScript / declarations / source maps
```

Trong production toolchain hiện đại, các bước có thể tách. Vite/esbuild/SWC/Babel có thể transpile syntax rất nhanh nhưng không thực hiện đầy đủ type checking như TypeScript checker. Vì vậy “build thành công” không luôn đồng nghĩa “type-check thành công”; CI thường cần một bước `tsc --noEmit` hoặc checker tích hợp riêng.

TypeScript 7.0 thay compiler foundation sang native Go implementation và khai thác multithreading/shared memory. Thay đổi này chủ yếu cải thiện tốc độ và architecture toolchain; source-level type mental model vẫn cố tương thích chặt với 6.0.

## 2. `tsconfig.json` là project model, không chỉ là danh sách flags

`tsconfig` xác định file graph, environment libraries, module semantics, strictness và emit behavior. Khi một diagnostic kỳ lạ, hãy hỏi project đang compile file nào và với assumptions nào trước khi sửa source.

Một baseline hiện đại có thể trông như:

```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "target": "es2022",
    "lib": ["es2022", "dom"],
    "noEmit": true
  },
  "include": ["src"]
}
```

Đây chỉ là ví dụ mental model, không phải config copy-paste cho mọi project. Node app, browser app, library package và hybrid/WebView target có runtime khác nhau.

## 3. `target` và `lib` giải quyết hai câu hỏi khác nhau

`target` chủ yếu ảnh hưởng syntax/output level khi compiler emit JavaScript. `lib` nói checker giả định những built-in/environment declarations nào tồn tại.

Ví dụ bạn có thể target syntax cũ nhưng include DOM declarations, hoặc target ES2022 mà runtime vẫn thiếu một Web API cụ thể. TypeScript declaration không polyfill runtime.

```text
target = emitted JavaScript language level
lib    = static declaration universe compiler được phép biết
```

Nếu `Promise`, `Map`, `document` hay `fetch` báo type khác thường, kiểm tra `lib`; nếu runtime cũ crash vì syntax/API không support, kiểm tra target + transpilation + polyfill + actual runtime compatibility.

## 4. TypeScript không sở hữu toàn bộ build pipeline

Một frontend pipeline thường là:

```text
.ts/.tsx
  ↓ type check (tsc/TS language service)
  ↓ transform/transpile (tsc, esbuild, SWC, Babel...)
  ↓ bundle/code split
  ↓ minify
  ↓ browser/WebView
```

Tool có thể gộp nhiều bước, nhưng conceptually hãy tách. Bug tree-shaking thuộc bundler semantics; module not found có thể là resolver mismatch; stale type declaration thuộc package/declaration layer; runtime syntax error có thể do target/browser mismatch.

## 5. Module specifier có ba đời sống

Với:

```ts
import { parseUser } from "@domain/user";
```

specifier phải được hiểu bởi TypeScript resolver, bundler/dev server và cuối cùng runtime/package loader sau transform. `compilerOptions.paths` giúp TypeScript resolution nhưng **không tự động rewrite mọi runtime import**.

Đây là failure mode kinh điển:

```text
IDE không báo lỗi
TypeScript check pass
bundle/runtime: module not found
```

Fix đúng là đồng bộ alias/resolution across toolchain hoặc dùng package/workspace boundary thật, không cast hay thêm declaration giả.

## 6. ESM và CommonJS: syntax giống chưa chắc semantics giống

ECMAScript Modules dùng `import`/`export`, static graph và semantics khác CommonJS `require`/`module.exports`. Node, bundler và package metadata (`type`, `exports`, extensions) cùng quyết định file được interpret thế nào.

TypeScript phải model cả source module format lẫn output/runtime expectations. Các options như `module`, `moduleResolution`, `verbatimModuleSyntax`, interop options và file extensions `.mts`/`.cts` tồn tại vì “import syntax” không đủ để suy ra toàn bộ runtime semantics.

Senior debugging phải hỏi:

```text
Source đang viết theo module model nào?
Compiler resolve theo mode nào?
Emit giữ/chuyển syntax ra sao?
Package/runtime sẽ load file với semantics nào?
```

## 7. `moduleResolution` nên khớp môi trường thật

Browser app qua bundler thường hợp với bundler-oriented resolution. Node app cần model Node package resolution/version tương ứng. Chọn resolver sai có thể khiến TypeScript nhìn thấy file mà runtime không thấy, hoặc ngược lại.

Đừng sửa module resolution error bằng `declare module "x"` nếu package thật sự không resolve. Ambient declaration giả có thể làm checker im trong khi production vẫn fail.

## 8. `import type` và type/value namespace

Một identifier có thể tồn tại ở type space, value space hoặc cả hai. `interface` và type alias chỉ tồn tại ở type space; class có cả runtime constructor value và instance type relation.

```ts
import type { User } from "./types";
```

`import type` nói import chỉ cần cho type checking và có thể bị loại khỏi runtime output. Điều này quan trọng với side effects, ESM correctness và toolchains dùng isolated transforms.

Một lỗi phổ biến là dùng value như type không qua `typeof`, hoặc tưởng type import tạo runtime module dependency. TypeScript 7.0 còn làm JavaScript/JSDoc support nhất quán hơn với distinction value-vs-type.

## 9. `.d.ts`: contract surface không có implementation

Declaration file mô tả shape/type của module, global hoặc library:

```ts
export interface ClientOptions {
  timeoutMs: number;
}

export declare function createClient(options: ClientOptions): Client;
```

`declare` nói implementation tồn tại ở nơi khác. Nếu declaration sai, compiler có thể chứng minh dựa trên một contract giả và runtime vẫn fail.

Library author phải coi `.d.ts` như public API artifact. Breaking declaration change có thể làm consumer build fail ngay cả khi runtime behavior tương tự.

## 10. Ambient declarations và global pollution

File declaration không có top-level import/export có thể bổ sung global scope. Điều này hữu ích cho browser globals hoặc legacy script, nhưng dễ tạo name collision và hidden dependency.

Application hiện đại nên ưu tiên module-scoped declarations và explicit imports. Nếu phải augment `Window`, third-party module hoặc global namespace, tập trung augmentation ở file dễ tìm và giải thích runtime source tạo value tương ứng.

## 11. Declaration merging, namespace và legacy code

TypeScript hỗ trợ namespace/declaration merging vì lịch sử JavaScript trước ESM và ecosystem declaration files. Bạn vẫn cần đọc:

```ts
namespace LegacyApp {
  export interface Config {}
}
```

Nhưng code mới thường nên ưu tiên ES modules. Namespace không phải security boundary và không thay package/module architecture. Học nó để migrate legacy, không chọn nó mặc định cho new code.

## 12. Project references: chia graph để scale build

Large repository có thể tách TypeScript projects với `composite`/references. Ý tưởng là biến một graph khổng lồ thành các units có explicit dependency và reusable build information.

```text
apps/web
   ↓
packages/ui
   ↓
packages/domain
```

Project references hữu ích khi boundaries thật sự ổn định. Nếu bạn tạo hàng chục projects theo folder tùy ý, config complexity và circular dependency có thể tăng hơn lợi ích incremental build.

## 13. Incremental build và cache không thay correctness

Compiler có thể lưu build information để tránh check/emit lại phần không đổi. Cache giúp latency, nhưng stale/corrupt cache hoặc mismatch giữa compiler versions có thể gây behavior khó hiểu. Khi bug chỉ xuất hiện local/editor mà clean CI không có, thử phân biệt source issue với cache/tooling state thay vì sửa code ngẫu nhiên.

## 14. Source map nối emitted JavaScript về TypeScript source

Runtime stack trace chạy trên JavaScript artifacts. Source maps giúp debugger ánh xạ về `.ts/.tsx`. Nếu production stack line lệch, hãy kiểm tra build transform chain, source map upload/deploy và minification, không kết luận “TypeScript stack trace sai”.

## 15. `allowJs` và `checkJs`: migration không cần big bang

TypeScript có thể tham gia JavaScript project từng bước. `allowJs` cho JS vào project graph; `checkJs` tăng static checking; JSDoc có thể cung cấp type info trước khi rename file sang `.ts`.

Migration tốt thường đi từ boundary có value cao: shared domain types, API clients, utility core, component props. Đừng bắt đầu bằng việc cast toàn bộ legacy code sang `any` chỉ để đạt “100% .ts”. File extension không phải metric type safety.

## 16. TypeScript 6.0 → 7.0: hiểu migration theo hai lớp

TypeScript 6.0 là release chuyển tiếp: modern defaults chặt hơn, nhiều legacy options bị deprecate/loại dần và ecosystem được đẩy về ESM/bundler/evergreen assumptions. TypeScript 7.0 tiếp nhận behavior đó trên native compiler.

Những thay đổi cần đặc biệt audit khi upgrade gồm default `strict`, module/target assumptions, side-effect import checking, ambient `types` visibility và những options đã bị deprecate trong 6.0 rồi không còn được 7.0 hỗ trợ. Đừng upgrade bằng cách thêm `ignoreDeprecations` vĩnh viễn; đó chỉ là cầu migration ở 6.0, không phải architecture.

## 17. TypeScript 7.0 native compiler: performance đổi, evidence vẫn cần

TypeScript 7.0 được port sang Go, dùng native execution và shared-memory multithreading, nhắm vào speedup lớn ở full builds/editor workloads. Nhưng performance claim không thay yêu cầu đo trên repo thật. Monorepo nhỏ có thể không thấy cùng mức speedup; bottleneck có thể nằm ở bundler, lint, codegen hoặc tests chứ không phải checker.

Một điểm ecosystem quan trọng ở 7.0 là programmatic compiler API chưa ship như 6.x. Tooling cần API có thể phải chạy TypeScript 6 side-by-side trong giai đoạn chuyển tiếp. Điều này đặc biệt liên quan custom transforms, ESLint integrations hoặc internal tooling phụ thuộc compiler API.

## 18. Debug module resolution bằng evidence

Khi `Cannot find module` hoặc type của package sai, đừng chỉ restart IDE. Dùng trace/resolution evidence phù hợp:

```bash
npx tsc --traceResolution
```

Sau đó kiểm tra package `exports`, `types`, extension, resolution mode và path mapping. `--explainFiles` giúp hiểu tại sao file vào compilation. `--showConfig` giúp thấy config cuối sau `extends`.

## 19. Debug performance của checker

Các command hữu ích tùy compiler version/toolchain gồm:

```bash
npx tsc --extendedDiagnostics
npx tsc --generateTrace trace-output
```

Bạn cần evidence về parse/check/emit time, file count, type instantiation và memory trước khi tối ưu type definitions. Nếu check time tăng sau một PR, compare diagnostic metrics và narrow commit, đừng đoán do “TypeScript chậm”.

## 20. Build và CI: fail fast ở contract layer

Một pipeline production nên có bước type-check độc lập nếu bundler không check đầy đủ:

```text
install reproducibly
→ generate required artifacts
→ type-check
→ lint/tests
→ build bundle/package
→ integration/e2e
```

Nếu code generation tạo types/schema clients, ordering quan trọng: type-check trước codegen có thể báo hàng loạt lỗi giả; codegen từ stale schema lại tạo false confidence. Pipeline phải encode dependency thật.

## 21. `skipLibCheck` là trade-off, không phải “fix type error”

`skipLibCheck` giảm check trên declaration files và có thể giúp build performance/compatibility khi dependency declarations xung đột. Nhưng nó cũng che lỗi ở `.d.ts`. Nếu issue đến từ duplicate types hoặc incompatible library versions, hãy giải quyết dependency graph khi có thể. Dùng flag như một trade-off có chủ đích, không như reflex.

## 22. Library build: source target khác consumer surface

Library author phải nghĩ tới JavaScript output formats, declaration emit, package exports, source maps, minimum runtime target và consumer resolution. Một package có thể type-check nội bộ nhưng publish thiếu `.d.ts`, export path sai hoặc CJS/ESM metadata mismatch.

Test package nên bao gồm consumer fixture thật hoặc package tarball install, không chỉ unit tests trong source tree.

## 23. Decorators: phân biệt standard direction và legacy experimental mode

TypeScript từng phổ biến `experimentalDecorators` dựa trên proposal cũ, đặc biệt trong Angular/Nest-like ecosystems. TypeScript 5.x hỗ trợ standard decorators semantics mới. Hai hệ có differences về typing/runtime emit và metadata assumptions. Khi migrate framework code, đừng chỉ xóa flag; xác nhận framework version, decorator contract và metadata pipeline.

## 24. Senior note: compiler config là executable architecture

`tsconfig`, package metadata và bundler config cùng mô tả cách source biến thành runtime artifact. Chúng không phải “setup một lần rồi quên”. Khi runtime/platform thay đổi, config phải được audit như source code: assumption nào còn đúng, option nào legacy, alias nào drift, declaration nào không còn match implementation?

## 25. Compiler internals: parser, binder, checker và emit giữ những invariant khác nhau

Pipeline compiler không phải một “hàm compile” nguyên khối. Parser biến token/source thành syntax tree. Binder đi qua tree để tạo symbol relationships và nối declarations vào scopes. Checker dùng symbols, types, control-flow facts và assignability relations để tạo diagnostics/inference. Emit tạo JavaScript, declarations và source maps tùy config.

Mental model này giải thích nhiều lỗi tưởng như vô lý. Syntax hợp lệ nhưng symbol trùng có thể fail ở binding. Symbol resolve được nhưng relation type không hợp lệ fail ở checker. Type-check hoàn toàn sạch vẫn có thể emit/import artifact không chạy nếu runtime/module assumptions sai.

Trong debugging compiler issue, hãy phân loại trước:

```text
parse/syntax
→ name/symbol resolution
→ type relation/control flow
→ emit/declaration generation
→ host/runtime loading
```

Nếu không phân layer, rất dễ dùng type assertion để “sửa” một module-resolution bug hoặc thay tsconfig để che một modeling bug.

## 26. Program graph và language service: editor không chỉ check file đang mở

IDE phải duy trì một **project graph** gồm source files, dependencies, declaration files, config inheritance và package metadata. Auto-complete, rename, find references và diagnostics đều phụ thuộc graph này.

Một thay đổi ở shared `.d.ts`, `tsconfig`, package `exports` hoặc generated file có thể làm hàng nghìn files invalidate dù bạn chỉ sửa một dòng. Đây là lý do editor latency thường liên quan graph topology chứ không chỉ độ dài file đang mở.

TypeScript 7 chuyển editor foundation sang Language Server Protocol (LSP) và native multithreaded implementation. Điều này giúp nhiều editor dùng cùng protocol và cho phép language server xử lý nhiều request đồng thời. Tuy vậy, embedded-language ecosystems như Vue/Svelte/Astro/MDX hoặc framework tooling cần compiler API có thể vẫn phụ thuộc TypeScript 6 trong giai đoạn 7.0 vì TypeScript 7.0 chưa có stable programmatic API.

## 27. `verbatimModuleSyntax`: source phải nói rõ import nào tồn tại ở runtime

Trước đây import elision có nhiều rule khó đoán: compiler có thể bỏ import nếu nó chỉ được dùng như type. `verbatimModuleSyntax` làm mental model đơn giản hơn:

```ts
import type { User } from "./user.js";
import { createUser } from "./user.js";
```

Type-only syntax bị xóa; import/export không có `type` được giữ theo module semantics thay vì compiler “đoán intent”. Điều này đặc biệt quan trọng khi module có side effects hoặc toolchain transpile từng file độc lập.

Senior practice là dùng type/value distinction rõ ở source. Một import bị giữ hay xóa có thể thay runtime side effect, tree-shaking và cycle behavior; đây không chỉ là style.

## 28. `isolatedModules` và `isolatedDeclarations`: khi mỗi file phải tự đủ thông tin

Một số transpiler xử lý từng file mà không có toàn program graph. `isolatedModules` cảnh báo những pattern không thể transform an toàn theo kiểu per-file.

`isolatedDeclarations` đi vào public type surface: nó buộc exported API cung cấp đủ annotation để declaration emit có thể được thực hiện mà không cần full semantic check toàn program. Điều này hữu ích cho build system muốn song song hóa declaration generation hoặc cache theo file/package.

Trade-off là author phải viết explicit public annotations nhiều hơn. Đây là ví dụ tốt của architecture pressure làm coding style thay đổi: annotation không phải vì compiler “không inference được”, mà vì build pipeline muốn giảm coupling giữa files.

## 29. Package `exports` là allow-list, không phải metadata trang trí

Khi resolver hiện đại đọc `package.json` có `exports`, subpath không match có thể bị chặn dù file vật lý tồn tại.

```json
{
  "name": "my-lib",
  "exports": {
    ".": "./dist/index.js",
    "./client": "./dist/client.js"
  }
}
```

`import "my-lib/internal.js"` có thể fail dù `dist/internal.js` tồn tại. `exports` định nghĩa public package surface.

TypeScript ở `node16`/`nodenext`/`bundler` còn ưu tiên tìm condition `types` khi resolve declaration surface. Package author vì thế phải test cả JavaScript runtime resolution và TypeScript type resolution; publish đúng file nhưng sai condition vẫn có thể làm consumer mất types.

## 30. `typesVersions` và versioned `types` conditions: phục vụ compiler cũ có chủ đích

Khi public `.d.ts` dùng syntax chỉ compiler mới hiểu, library có thể cung cấp declaration khác theo TypeScript version. `typesVersions` là cơ chế legacy/phổ biến cho việc này, còn resolver qua `exports` có thể dùng versioned `types@...` conditions.

Điểm dễ nhầm: khi `exports` được đọc, `typesVersions` không phải lúc nào cũng quyết định resolution như bạn kỳ vọng. Package càng nhiều conditions càng cần consumer fixtures trên nhiều compiler/module modes.

Senior lesson: đừng hứa “support TypeScript >= X” chỉ dựa trên source build của chính package. Hãy install tarball vào consumer project thật với minimum compiler version và check public imports.

## 31. Bundler-compatible source có thể tạo `.d.ts` không tương thích `nodenext`

Một library build bằng bundler có thể viết:

```ts
import { Component } from "./component";
```

Bundler hiểu extensionless relative import và xóa/ghép nó trong JavaScript output. Nhưng nếu `tsc` đồng thời emit nhiều declaration files, `.d.ts` có thể giữ specifier `./component`. Consumer chạy `nodenext` có thể từ chối specifier đó vì ESM Node yêu cầu extension phù hợp.

Đây là failure mode quan trọng: **JavaScript bundle chạy được nhưng declaration graph của consumer fail**.

Nếu library không bundle declarations, cấu hình declaration emit cần model consumer runtime đủ chặt; với library cho Node consumers, `nodenext` thường cung cấp safety tốt hơn. Cách chắc chắn nhất vẫn là test package artifact trong consumer fixtures với module modes bạn tuyên bố hỗ trợ.

## 32. Chạy `.ts` trực tiếp và `erasableSyntaxOnly`: “type erasure” trở thành runtime contract

Một số runtime hiện đại có thể strip TypeScript syntax và chạy file `.ts` trực tiếp. Nhưng strip-only runtime chỉ hỗ trợ syntax TypeScript có thể xóa mà không cần transform semantics.

Các construct như `enum`, namespace có runtime code, parameter properties, `import =`/`export =` không chỉ là type syntax; chúng cần emit transform. `erasableSyntaxOnly` giúp compiler báo sớm những construct không phù hợp với strip-only execution.

Nếu architecture chọn direct-TypeScript runtime, hãy xem đây là một **source-language subset** có chủ đích. Thường cần kết hợp với `verbatimModuleSyntax`, module settings đúng host và test runtime thật. Không nên suy từ “tsc type-check pass” sang “Node/Bun/Deno chắc chắn chạy source này”.

## 33. `.ts` extension trong import: source host và output host có thể là hai thế giới khác nhau

`allowImportingTsExtensions` hữu ích khi bundler/runtime đọc `.ts` trực tiếp hoặc project `noEmit`. Nhưng nếu cuối cùng phát hành `.js`, specifier `.ts` cần được host/bundler rewrite hoặc TypeScript dùng `rewriteRelativeImportExtensions` cho relative imports phù hợp.

Ví dụ:

```ts
import { parse } from "./parse.ts";
```

Có ba câu hỏi riêng:

```text
Dev runtime có load .ts trực tiếp không?
Compiler có emit .js không?
Published/runtime specifier cuối cùng là gì?
```

Không trả lời đủ ba câu sẽ tạo project chạy trong dev loader nhưng fail sau build, hoặc library chạy test source nhưng package publish hỏng.

## 34. TypeScript 7 parallelism: nhiều CPU hơn không phải luôn nhanh hơn

TypeScript 7 có thể chạy parsing/checking/emitting song song. `--checkers` điều khiển số checker workers; `--builders` điều khiển số project-reference builders; `--singleThreaded` hữu ích khi debug, benchmark hoặc CI ít tài nguyên.

Tăng workers làm tăng parallelism nhưng có thể tăng aggregate memory và duplicate work. Trong monorepo, `--checkers 4 --builders 4` có thể tạo áp lực gần như nhiều checker đồng thời hơn dự kiến. Vì vậy tuning phải dựa trên CPU, RAM, graph shape và CI contention.

Một failure mode hiếm nhưng quan trọng là order-dependent checking có thể lộ ra khi thay số checker. Nếu team gặp diagnostic khác giữa môi trường, cố định worker count trong điều tra và dùng `--singleThreaded` làm control case trước khi quy lỗi cho source.

## 35. TypeScript 7 `--watch`: file-system behavior cũng là performance layer

Watch mode không chỉ là “chạy compiler lại khi save”. Nó phụ thuộc file watcher, invalidation graph, package directories và OS behavior. TypeScript 7 rebuild watch foundation để giảm polling/resource overhead và cải thiện cross-platform stability.

Nếu watch mode ngốn CPU, đừng chỉ profile checker. Hãy xem workspace có symlink/worktree lớn, generated directories, dependency trees hoặc tool khác cùng theo dõi quá nhiều files không. Production developer experience là tổng của file watching + project graph invalidation + checking + bundling, không phải một con số `tsc` duy nhất.

## 36. TypeScript 6/7 defaults: upgrade phải audit assumptions, không chỉ sửa diagnostics

Các default hiện đại thay đổi mạnh: `strict` bật mặc định, `module` hướng `esnext`, `target` theo ECMAScript stable gần nhất, `noUncheckedSideEffectImports` bật, `rootDir` mặc định theo project root và `types` mặc định thành `[]`. TypeScript 7 còn biến nhiều deprecation của 6.0 thành hard error.

Điều nguy hiểm là một số thay đổi không tạo cùng dạng error. `types: []` có thể làm global `process`, `describe` hay `jest` biến mất; `rootDir` mới có thể làm output path đổi; `moduleResolution node10` không còn hợp lệ; `baseUrl` legacy không còn là nền nên `paths` cần được hiểu relative theo project config hiện đại.

Upgrade runbook đúng nên là:

```text
1. Chốt runtime/module host thật.
2. Nâng lên TS 6 và xử lý toàn bộ deprecation.
3. Ghi explicit những defaults mà project muốn sở hữu lâu dài.
4. Chạy clean type-check + package consumer tests.
5. Chuyển sang TS 7.
6. Benchmark build/editor/watch trên workload thật.
```

## 37. TypeScript 7 không có compiler API: side-by-side không phải hack tạm bợ vô tổ chức

TypeScript 7.0 chưa ship stable programmatic compiler API. Team TypeScript cung cấp đường chạy side-by-side với TypeScript 6 cho tooling còn phụ thuộc API. Điều này có nghĩa một repository có thể hợp lệ khi `tsc` CLI dùng 7.0 nhưng linter/framework plugin dùng 6.x compatibility layer.

Điều cần quản lý là **version ownership**: tool nào dùng compiler nào, diagnostics nào là source of truth, và CI step nào bảo vệ semantics tương thích. Đừng để dependency resolver vô tình đổi toàn bộ ecosystem sang một compiler version rồi coi lỗi plugin là lỗi application.

---

Tiếp theo: [TypeScript 04 — Senior Production Engineering](typescript_04_senior_production.md).
