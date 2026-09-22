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

---

Tiếp theo: [TypeScript 04 — Senior Production Engineering](typescript_04_senior_production.md).
