# TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**. Route đi từ tsc pipeline → tsconfig project model → modules/emit/resolution → runtime environment và build tooling → diagnostics, để type-correct code không bị tách khỏi cách chạy thật.

> Prerequisite: [Type System Internals](typescript_02_type_system.md). Chapter này giải thích vì sao mã (code / 코드) type-correct vẫn có thể thất bại (fail / 실패) ở bản dựng (build / 빌드)/thời gian chạy (runtime / 런타임) nếu mô-đun (module / 모듈), emit hoặc môi trường (environment / 환경) mô hình (model / 모델) sai.

## 1. `tsc` thực sự làm những việc gì?

Một mô hình tư duy (mental model / 사고 모델) đơn giản là:

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

Trong môi trường vận hành (production / 운영 환경) toolchain hiện đại, các bước có thể tách. Vite/esbuild/SWC/Babel có thể transpile cú pháp (syntax / 문법) rất nhanh nhưng không thực hiện đầy đủ kiểu (type / 타입) checking như TypeScript checker. Vì vậy “bản dựng (build / 빌드) thành công” không luôn đồng nghĩa “type-check thành công”; CI thường cần một bước `tsc --noEmit` hoặc checker tích hợp riêng.

TypeScript 7.0 thay trình biên dịch (compiler / 컴파일러) foundation sang bản địa (native / 네이티브) Go hiện thực (implementation / 구현) và khai thác multithreading/dùng chung (shared / 공유) bộ nhớ (memory / 메모리). Thay đổi này chủ yếu cải thiện tốc độ và kiến trúc (architecture / 아키텍처) toolchain; tầng mã nguồn (source-level / 소스 수준) kiểu (type / 타입) mô hình tư duy (mental model / 사고 모델) vẫn cố tương thích chặt với 6.0.

> **Chuyển mạch:** `tsc` xác định compile pipeline và output; `tsconfig.json` biến pipeline đó thành project contract có include, module và strictness. `target`/`lib` tiếp theo tách runtime syntax khỏi API assumptions.

## 2. `tsconfig.json` là dự án (project / 프로젝트) mô hình (model / 모델), không chỉ là danh sách flags

`tsconfig` xác định tệp (file / 파일) đồ thị (graph / 그래프), môi trường (environment / 환경) libraries, mô-đun (module / 모듈) ngữ nghĩa (semantics / 의미론), strictness và emit hành vi (behavior / 동작). Khi một diagnostic kỳ lạ, hãy hỏi dự án (project / 프로젝트) đang compile tệp (file / 파일) nào và với các giả định (assumptions / 가정들) nào trước khi sửa nguồn (source / 소스).

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

Đây chỉ là ví dụ mô hình tư duy (mental model / 사고 모델), không phải cấu hình (config / 설정) copy-paste cho mọi dự án (project / 프로젝트). nút (node / 노드) app, trình duyệt (browser / 브라우저) app, thư viện (library / 라이브러리) gói (package / 패키지) và hybrid/WebView mục tiêu (target / 대상) có thời gian chạy (runtime / 런타임) khác nhau.

> **Chuyển mạch:** `tsconfig` defines project contract; target/lib separate emitted syntax from available platform APIs. Build pipeline tiếp theo bổ sung bundler, resolver và runtime steps mà TypeScript không sở hữu.

## 3. `target` và `lib` giải quyết hai câu hỏi khác nhau

`target` chủ yếu ảnh hưởng cú pháp (syntax / 문법)/đầu ra (output / 출력) mức (level / 수준) khi trình biên dịch (compiler / 컴파일러) emit JavaScript. `lib` nói checker giả định những built-in/môi trường (environment / 환경) declarations nào tồn tại.

Ví dụ bạn có thể mục tiêu (target / 대상) cú pháp (syntax / 문법) cũ nhưng include DOM declarations, hoặc mục tiêu (target / 대상) ES2022 mà thời gian chạy (runtime / 런타임) vẫn thiếu một Web API cụ thể. TypeScript declaration không polyfill thời gian chạy (runtime / 런타임).

```text
target = emitted JavaScript language level
lib    = static declaration universe compiler được phép biết
```

Nếu `Promise`, `Map`, `document` hay `fetch` báo kiểu (type / 타입) khác thường, kiểm tra `lib`; nếu thời gian chạy (runtime / 런타임) cũ crash vì cú pháp (syntax / 문법)/API không hỗ trợ (support / 지원), kiểm tra mục tiêu (target / 대상) + transpilation + polyfill + actual thời gian chạy (runtime / 런타임) tính tương thích (compatibility / 호환성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **3. target và lib giải quyết hai câu hỏi khác nhau** xác định đầu vào; **4. TypeScript không sở hữu toàn bộ bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. mô-đun (module / 모듈) specifier có ba đời sống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. TypeScript không sở hữu toàn bộ bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인)

Một frontend chuỗi xử lý (pipeline / 파이프라인) thường là:

```text
.ts/.tsx
  ↓ type check (tsc/TS language service)
  ↓ transform/transpile (tsc, esbuild, SWC, Babel...)
  ↓ bundle/code split
  ↓ minify
  ↓ browser/WebView
```

Công cụ (tool / 도구) có thể gộp nhiều bước, nhưng conceptually hãy tách. Bug tree-shaking thuộc bundler ngữ nghĩa (semantics / 의미론); mô-đun (module / 모듈) not found có thể là resolver mismatch; stale kiểu (type / 타입) declaration thuộc gói (package / 패키지)/declaration tầng (layer / 계층); thời gian chạy (runtime / 런타임) cú pháp (syntax / 문법) lỗi (error / 오류) có thể do mục tiêu (target / 대상)/trình duyệt (browser / 브라우저) mismatch.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **4. TypeScript không sở hữu toàn bộ bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **5. mô-đun (module / 모듈) specifier có ba đời sống** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **6. ESM và CommonJS: cú pháp (syntax / 문법) giống chưa chắc ngữ nghĩa (semantics / 의미론) giống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. mô-đun (module / 모듈) specifier có ba đời sống

Với:

```ts
import { parseUser } from "@domain/user";
```

specifier phải được hiểu bởi TypeScript resolver, bundler/dev máy chủ (server / 서버) và cuối cùng thời gian chạy (runtime / 런타임)/gói (package / 패키지) loader sau transform. `compilerOptions.paths` giúp TypeScript resolution nhưng **không tự động rewrite mọi thời gian chạy (runtime / 런타임) import**.

Đây là dạng thất bại (failure mode / 실패 모드) kinh điển:

```text
IDE không báo lỗi
TypeScript check pass
bundle/runtime: module not found
```

Fix đúng là đồng bộ alias/resolution across toolchain hoặc dùng gói (package / 패키지)/workspace ranh giới (boundary / 경계) thật, không cast hay thêm declaration giả.

> **Chuyển mạch:** Module specifier đi qua source, compiler và runtime; ESM/CommonJS có syntax gần nhau nhưng semantics khác, nên `moduleResolution` phải khớp environment thật.

## 6. ESM và CommonJS: cú pháp (syntax / 문법) giống chưa chắc ngữ nghĩa (semantics / 의미론) giống

ECMAScript Modules dùng `import`/`export`, static đồ thị (graph / 그래프) và ngữ nghĩa (semantics / 의미론) khác CommonJS `require`/`module.exports`. nút (node / 노드), bundler và gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터) (`type`, `exports`, extensions) cùng quyết định tệp (file / 파일) được interpret thế nào.

TypeScript phải mô hình (model / 모델) cả nguồn (source / 소스) mô-đun (module / 모듈) format lẫn đầu ra (output / 출력)/thời gian chạy (runtime / 런타임) expectations. Các options như `module`, `moduleResolution`, `verbatimModuleSyntax`, interop options và tệp (file / 파일) extensions `.mts`/`.cts` tồn tại vì “import cú pháp (syntax / 문법)” không đủ để suy ra toàn bộ ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론).

Cấp cao (senior / 시니어) debugging phải hỏi:

```text
Source đang viết theo module model nào?
Compiler resolve theo mode nào?
Emit giữ/chuyển syntax ra sao?
Package/runtime sẽ load file với semantics nào?
```

> **Chuyển mạch:** ESM/CommonJS chỉ đúng khi khớp semantics của runtime; `moduleResolution` phải mô phỏng môi trường đó, còn `import type` giữ type namespace tách khỏi runtime values.

## 7. `moduleResolution` nên khớp môi trường thật

Trình duyệt (browser / 브라우저) app qua bundler thường hợp với bundler-oriented resolution. nút (node / 노드) app cần mô hình (model / 모델) nút (node / 노드) gói (package / 패키지) resolution/phiên bản (version / 버전) tương ứng. Chọn resolver sai có thể khiến TypeScript nhìn thấy tệp (file / 파일) mà thời gian chạy (runtime / 런타임) không thấy, hoặc ngược lại.

Đừng sửa mô-đun (module / 모듈) resolution lỗi (error / 오류) bằng `declare module "x"` nếu gói (package / 패키지) thật sự không resolve. Ambient declaration giả có thể làm checker im trong khi môi trường vận hành (production / 운영 환경) vẫn thất bại (fail / 실패).

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **8. import type và kiểu (type / 타입)/giá trị (value / 값) không gian tên (namespace / 네임스페이스)** tiếp nhận điểm tựa từ **7. moduleResolution nên khớp môi trường thật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. .d.ts: đặc tả hợp đồng (contract / 계약) surface không có hiện thực (implementation / 구현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. `import type` và kiểu (type / 타입)/giá trị (value / 값) không gian tên (namespace / 네임스페이스)

Một identifier có thể tồn tại ở kiểu (type / 타입) không gian (space / 공간), giá trị (value / 값) không gian (space / 공간) hoặc cả hai. `interface` và kiểu (type / 타입) alias chỉ tồn tại ở kiểu (type / 타입) không gian (space / 공간); lớp (class / 클래스) có cả thời gian chạy (runtime / 런타임) constructor giá trị (value / 값) và instance kiểu (type / 타입) quan hệ (relation / 관계).

```ts
import type { User } from "./types";
```

`import type` nói import chỉ cần cho kiểu (type / 타입) checking và có thể bị loại khỏi thời gian chạy (runtime / 런타임) đầu ra (output / 출력). Điều này quan trọng với side effects, ESM tính đúng đắn (correctness / 정확성) và toolchains dùng isolated transforms.

Một lỗi phổ biến là dùng giá trị (value / 값) như kiểu (type / 타입) không qua `typeof`, hoặc tưởng kiểu (type / 타입) import tạo thời gian chạy (runtime / 런타임) mô-đun (module / 모듈) phụ thuộc (dependency / 의존성). TypeScript 7.0 còn làm JavaScript/JSDoc hỗ trợ (support / 지원) nhất quán hơn với distinction value-vs-type.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **9. .d.ts: đặc tả hợp đồng (contract / 계약) surface không có hiện thực (implementation / 구현)** tiếp nhận điểm tựa từ **8. import type và kiểu (type / 타입)/giá trị (value / 값) không gian tên (namespace / 네임스페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Ambient declarations và toàn cục (global / 전역) pollution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. `.d.ts`: đặc tả hợp đồng (contract / 계약) surface không có hiện thực (implementation / 구현)

Declaration tệp (file / 파일) mô tả shape/kiểu (type / 타입) của mô-đun (module / 모듈), toàn cục (global / 전역) hoặc thư viện (library / 라이브러리):

```ts
export interface ClientOptions {
  timeoutMs: number;
}

export declare function createClient(options: ClientOptions): Client;
```

`declare` nói hiện thực (implementation / 구현) tồn tại ở nơi khác. Nếu declaration sai, trình biên dịch (compiler / 컴파일러) có thể chứng minh dựa trên một đặc tả hợp đồng (contract / 계약) giả và thời gian chạy (runtime / 런타임) vẫn thất bại (fail / 실패).

Thư viện (library / 라이브러리) author phải coi `.d.ts` như API công khai (public API / 공개 API) sản phẩm tạo ra (artifact / 산출물). Breaking declaration thay đổi (change / 변경) có thể làm bên tiêu thụ (consumer / 소비자) bản dựng (build / 빌드) thất bại (fail / 실패) ngay cả khi hành vi thời gian chạy (runtime behavior / 런타임 동작) tương tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **10. Ambient declarations và toàn cục (global / 전역) pollution** tiếp nhận điểm tựa từ **9. .d.ts: đặc tả hợp đồng (contract / 계약) surface không có hiện thực (implementation / 구현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Declaration merging, không gian tên (namespace / 네임스페이스) và legacy mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Ambient declarations và toàn cục (global / 전역) pollution

Tệp (file / 파일) declaration không có top-level import/export có thể bổ sung toàn cục (global / 전역) phạm vi (scope / 범위). Điều này hữu ích cho trình duyệt (browser / 브라우저) globals hoặc legacy script, nhưng dễ tạo name collision và hidden phụ thuộc (dependency / 의존성).

Ứng dụng (application / 애플리케이션) hiện đại nên ưu tiên module-scoped declarations và tường minh (explicit / 명시적) imports. Nếu phải augment `Window`, third-party mô-đun (module / 모듈) hoặc toàn cục (global / 전역) không gian tên (namespace / 네임스페이스), tập trung augmentation ở tệp (file / 파일) dễ tìm và giải thích thời gian chạy (runtime / 런타임) nguồn (source / 소스) tạo giá trị (value / 값) tương ứng.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **11. Declaration merging, không gian tên (namespace / 네임스페이스) và legacy mã (code / 코드)** tiếp nhận điểm tựa từ **10. Ambient declarations và toàn cục (global / 전역) pollution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. dự án (project / 프로젝트) references: chia đồ thị (graph / 그래프) để quy mô (scale / 규모) bản dựng (build / 빌드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Declaration merging, không gian tên (namespace / 네임스페이스) và legacy mã (code / 코드)

TypeScript hỗ trợ không gian tên (namespace / 네임스페이스)/declaration merging vì lịch sử JavaScript trước ESM và ecosystem declaration files. Bạn vẫn cần đọc:

```ts
namespace LegacyApp {
  export interface Config {}
}
```

Nhưng mã (code / 코드) mới thường nên ưu tiên ES modules. không gian tên (namespace / 네임스페이스) không phải ranh giới bảo mật (security boundary / 보안 경계) và không thay gói (package / 패키지)/mô-đun (module / 모듈) kiến trúc (architecture / 아키텍처). Học nó để migrate legacy, không chọn nó mặc định cho new mã (code / 코드).

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, sau nội dung của **11. Declaration merging, không gian tên (namespace / 네임스페이스) và legacy mã (code / 코드)**, **12. dự án (project / 프로젝트) references: chia đồ thị (graph / 그래프) để quy mô (scale / 규모) bản dựng (build / 빌드)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **13. Incremental bản dựng (build / 빌드) và bộ nhớ đệm (cache / 캐시) không thay tính đúng đắn (correctness / 정확성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. dự án (project / 프로젝트) references: chia đồ thị (graph / 그래프) để quy mô (scale / 규모) bản dựng (build / 빌드)

Large repository có thể tách TypeScript projects với `composite`/references. Ý tưởng là biến một đồ thị (graph / 그래프) khổng lồ thành các units có tường minh (explicit / 명시적) phụ thuộc (dependency / 의존성) và reusable bản dựng (build / 빌드) thông tin (information / 정보).

```text
apps/web
   ↓
packages/ui
   ↓
packages/domain
```

Dự án (project / 프로젝트) references hữu ích khi boundaries thật sự ổn định. Nếu bạn tạo hàng chục projects theo folder tùy ý, cấu hình (config / 설정) độ phức tạp (complexity / 복잡도) và circular phụ thuộc (dependency / 의존성) có thể tăng hơn lợi ích incremental bản dựng (build / 빌드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **13. Incremental bản dựng (build / 빌드) và bộ nhớ đệm (cache / 캐시) không thay tính đúng đắn (correctness / 정확성)** tiếp nhận điểm tựa từ **12. dự án (project / 프로젝트) references: chia đồ thị (graph / 그래프) để quy mô (scale / 규모) bản dựng (build / 빌드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. bản đồ mã nguồn (source map / 소스 맵) nối emitted JavaScript về TypeScript nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Incremental bản dựng (build / 빌드) và bộ nhớ đệm (cache / 캐시) không thay tính đúng đắn (correctness / 정확성)

Trình biên dịch (compiler / 컴파일러) có thể lưu bản dựng (build / 빌드) thông tin (information / 정보) để tránh check/emit lại phần không đổi. bộ nhớ đệm (cache / 캐시) giúp độ trễ (latency / 지연 시간), nhưng stale/corrupt bộ nhớ đệm (cache / 캐시) hoặc mismatch giữa trình biên dịch (compiler / 컴파일러) versions có thể gây hành vi (behavior / 동작) khó hiểu. Khi bug chỉ xuất hiện cục bộ (local / 로컬)/editor mà clean CI không có, thử phân biệt nguồn (source / 소스) issue với bộ nhớ đệm (cache / 캐시)/tooling trạng thái (state / 상태) thay vì sửa mã (code / 코드) ngẫu nhiên.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **13. Incremental bản dựng (build / 빌드) và bộ nhớ đệm (cache / 캐시) không thay tính đúng đắn (correctness / 정확성)** nêu điều cần giải thích; **14. bản đồ mã nguồn (source map / 소스 맵) nối emitted JavaScript về TypeScript nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. allowJs và checkJs: di chuyển (migration / 마이그레이션) không cần big bang** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. bản đồ mã nguồn (source map / 소스 맵) nối emitted JavaScript về TypeScript nguồn (source / 소스)

Thời gian chạy (runtime / 런타임) dấu vết ngăn xếp (stack trace / 스택 트레이스) chạy trên JavaScript artifacts. nguồn (source / 소스) maps giúp debugger ánh xạ về `.ts/.tsx`. Nếu môi trường vận hành (production / 운영 환경) ngăn xếp (stack / 스택) line lệch, hãy kiểm tra bản dựng (build / 빌드) transform chuỗi (chain / 사슬), bản đồ mã nguồn (source map / 소스 맵) upload/deploy và minification, không kết luận “TypeScript dấu vết ngăn xếp (stack trace / 스택 트레이스) sai”.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **14. bản đồ mã nguồn (source map / 소스 맵) nối emitted JavaScript về TypeScript nguồn (source / 소스)** nêu điều cần giải thích; **15. allowJs và checkJs: di chuyển (migration / 마이그레이션) không cần big bang** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. TypeScript 6.0 → 7.0: hiểu di chuyển (migration / 마이그레이션) theo hai lớp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `allowJs` và `checkJs`: di chuyển (migration / 마이그레이션) không cần big bang

TypeScript có thể tham gia JavaScript dự án (project / 프로젝트) từng bước. `allowJs` cho JS vào dự án (project / 프로젝트) đồ thị (graph / 그래프); `checkJs` tăng static checking; JSDoc có thể cung cấp kiểu (type / 타입) info trước khi rename tệp (file / 파일) sang `.ts`.

Di chuyển (migration / 마이그레이션) tốt thường đi từ ranh giới (boundary / 경계) có giá trị (value / 값) cao: dùng chung (shared / 공유) lĩnh vực (domain / 도메인) types, API clients, utility cốt lõi (core / 핵심), thành phần (component / 컴포넌트) props. Đừng bắt đầu bằng việc cast toàn bộ legacy mã (code / 코드) sang `any` chỉ để đạt “100% .ts”. tệp (file / 파일) extension không phải chỉ số (metric / 지표) kiểu (type / 타입) an toàn (safety / 안전).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **16. TypeScript 6.0 → 7.0: hiểu di chuyển (migration / 마이그레이션) theo hai lớp** tiếp nhận điểm tựa từ **15. allowJs và checkJs: di chuyển (migration / 마이그레이션) không cần big bang** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. TypeScript 7.0 bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러): hiệu năng (performance / 성능) đổi, bằng chứng (evidence / 증거) vẫn cần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. TypeScript 6.0 → 7.0: hiểu di chuyển (migration / 마이그레이션) theo hai lớp

TypeScript 6.0 là bản phát hành (release / 릴리스) chuyển tiếp: hiện đại (modern / 현대적) defaults chặt hơn, nhiều legacy options bị deprecate/loại dần và ecosystem được đẩy về ESM/bundler/evergreen các giả định (assumptions / 가정들). TypeScript 7.0 tiếp nhận hành vi (behavior / 동작) đó trên bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러).

Những thay đổi cần đặc biệt kiểm tra (audit / 감사) khi upgrade gồm default `strict`, mô-đun (module / 모듈)/mục tiêu (target / 대상) các giả định (assumptions / 가정들), side-effect import checking, ambient `types` visibility và những options đã bị deprecate trong 6.0 rồi không còn được 7.0 hỗ trợ. Đừng upgrade bằng cách thêm `ignoreDeprecations` vĩnh viễn; đó chỉ là cầu di chuyển (migration / 마이그레이션) ở 6.0, không phải kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **16. TypeScript 6.0 → 7.0: hiểu di chuyển (migration / 마이그레이션) theo hai lớp** nêu điều cần giải thích; **17. TypeScript 7.0 bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러): hiệu năng (performance / 성능) đổi, bằng chứng (evidence / 증거) vẫn cần** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **18. gỡ lỗi (debug / 디버그) mô-đun (module / 모듈) resolution bằng bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. TypeScript 7.0 bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러): hiệu năng (performance / 성능) đổi, bằng chứng (evidence / 증거) vẫn cần

TypeScript 7.0 được cổng (port / 포트) sang Go, dùng bản địa (native / 네이티브) thực thi (execution / 실행) và shared-memory multithreading, nhắm vào speedup lớn ở full builds/editor workloads. Nhưng hiệu năng (performance / 성능) claim không thay yêu cầu đo trên repo thật. Monorepo nhỏ có thể không thấy cùng mức speedup; bottleneck có thể nằm ở bundler, lint, codegen hoặc tests chứ không phải checker.

Một điểm ecosystem quan trọng ở 7.0 là programmatic trình biên dịch (compiler / 컴파일러) API chưa ship như 6.x. Tooling cần API có thể phải chạy TypeScript 6 side-by-side trong giai đoạn chuyển tiếp. Điều này đặc biệt liên quan custom transforms, ESLint integrations hoặc nội bộ (internal / 내부) tooling phụ thuộc trình biên dịch (compiler / 컴파일러) API.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **17. TypeScript 7.0 bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러): hiệu năng (performance / 성능) đổi, bằng chứng (evidence / 증거) vẫn cần** nêu điều cần giải thích; **18. gỡ lỗi (debug / 디버그) mô-đun (module / 모듈) resolution bằng bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. gỡ lỗi (debug / 디버그) hiệu năng (performance / 성능) của checker** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. gỡ lỗi (debug / 디버그) mô-đun (module / 모듈) resolution bằng bằng chứng (evidence / 증거)

Khi `Cannot find module` hoặc kiểu (type / 타입) của gói (package / 패키지) sai, đừng chỉ restart IDE. Dùng dấu vết (trace / 추적)/resolution bằng chứng (evidence / 증거) phù hợp:

```bash
npx tsc --traceResolution
```

Sau đó kiểm tra gói (package / 패키지) `exports`, `types`, extension, resolution chế độ (mode / 모드) và đường dẫn (path / 경로) ánh xạ (mapping / 매핑). `--explainFiles` giúp hiểu tại sao tệp (file / 파일) vào compilation. `--showConfig` giúp thấy cấu hình (config / 설정) cuối sau `extends`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **18. gỡ lỗi (debug / 디버그) mô-đun (module / 모듈) resolution bằng bằng chứng (evidence / 증거)** nêu điều cần giải thích; **19. gỡ lỗi (debug / 디버그) hiệu năng (performance / 성능) của checker** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. bản dựng (build / 빌드) và CI: thất bại (fail / 실패) fast ở đặc tả hợp đồng (contract / 계약) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. gỡ lỗi (debug / 디버그) hiệu năng (performance / 성능) của checker

Các command hữu ích tùy trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전)/toolchain gồm:

```bash
npx tsc --extendedDiagnostics
npx tsc --generateTrace trace-output
```

Bạn cần bằng chứng (evidence / 증거) về parse/check/emit thời gian (time / 시간), tệp (file / 파일) count, kiểu (type / 타입) instantiation và bộ nhớ (memory / 메모리) trước khi tối ưu kiểu (type / 타입) definitions. Nếu check thời gian (time / 시간) tăng sau một PR, compare diagnostic metrics và narrow lần ghi nhận (commit / 커밋), đừng đoán do “TypeScript chậm”.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **20. bản dựng (build / 빌드) và CI: thất bại (fail / 실패) fast ở đặc tả hợp đồng (contract / 계약) tầng (layer / 계층)** tiếp nhận điểm tựa từ **19. gỡ lỗi (debug / 디버그) hiệu năng (performance / 성능) của checker** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. skipLibCheck là sự đánh đổi (trade-off / 트레이드오프), không phải “fix kiểu (type / 타입) lỗi (error / 오류)”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. bản dựng (build / 빌드) và CI: thất bại (fail / 실패) fast ở đặc tả hợp đồng (contract / 계약) tầng (layer / 계층)

Một chuỗi xử lý (pipeline / 파이프라인) môi trường vận hành (production / 운영 환경) nên có bước type-check độc lập nếu bundler không check đầy đủ:

```text
install reproducibly
→ generate required artifacts
→ type-check
→ lint/tests
→ build bundle/package
→ integration/e2e
```

Nếu mã (code / 코드) generation tạo types/lược đồ (schema / 스키마) clients, thứ tự (ordering / 순서) quan trọng: type-check trước codegen có thể báo hàng loạt lỗi giả; codegen từ stale lược đồ (schema / 스키마) lại tạo false confidence. chuỗi xử lý (pipeline / 파이프라인) phải encode phụ thuộc (dependency / 의존성) thật.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **21. skipLibCheck là sự đánh đổi (trade-off / 트레이드오프), không phải “fix kiểu (type / 타입) lỗi (error / 오류)”** tiếp nhận điểm tựa từ **20. bản dựng (build / 빌드) và CI: thất bại (fail / 실패) fast ở đặc tả hợp đồng (contract / 계약) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. thư viện (library / 라이브러리) bản dựng (build / 빌드): nguồn (source / 소스) mục tiêu (target / 대상) khác bên tiêu thụ (consumer / 소비자) surface** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. `skipLibCheck` là sự đánh đổi (trade-off / 트레이드오프), không phải “fix kiểu (type / 타입) lỗi (error / 오류)”

`skipLibCheck` giảm check trên declaration files và có thể giúp bản dựng (build / 빌드) hiệu năng (performance / 성능)/tính tương thích (compatibility / 호환성) khi phụ thuộc (dependency / 의존성) declarations xung đột. Nhưng nó cũng che lỗi ở `.d.ts`. Nếu issue đến từ duplicate types hoặc incompatible thư viện (library / 라이브러리) versions, hãy giải quyết phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) khi có thể. Dùng flag như một sự đánh đổi (trade-off / 트레이드오프) có chủ đích, không như reflex.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **21. skipLibCheck là sự đánh đổi (trade-off / 트레이드오프), không phải “fix kiểu (type / 타입) lỗi (error / 오류)”** nêu điều cần giải thích; **22. thư viện (library / 라이브러리) bản dựng (build / 빌드): nguồn (source / 소스) mục tiêu (target / 대상) khác bên tiêu thụ (consumer / 소비자) surface** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **23. Decorators: phân biệt tiêu chuẩn (standard / 표준) direction và legacy experimental chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. thư viện (library / 라이브러리) bản dựng (build / 빌드): nguồn (source / 소스) mục tiêu (target / 대상) khác bên tiêu thụ (consumer / 소비자) surface

Thư viện (library / 라이브러리) author phải nghĩ tới JavaScript đầu ra (output / 출력) formats, declaration emit, gói (package / 패키지) exports, nguồn (source / 소스) maps, minimum thời gian chạy (runtime / 런타임) mục tiêu (target / 대상) và bên tiêu thụ (consumer / 소비자) resolution. Một gói (package / 패키지) có thể type-check nội bộ nhưng publish thiếu `.d.ts`, export đường dẫn (path / 경로) sai hoặc CJS/ESM siêu dữ liệu (metadata / 메타데이터) mismatch.

Kiểm thử (test / 테스트) gói (package / 패키지) nên bao gồm bên tiêu thụ (consumer / 소비자) fixture thật hoặc gói (package / 패키지) tarball install, không chỉ đơn vị (unit / 단위) tests trong nguồn (source / 소스) cây (tree / 트리).

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **22. thư viện (library / 라이브러리) bản dựng (build / 빌드): nguồn (source / 소스) mục tiêu (target / 대상) khác bên tiêu thụ (consumer / 소비자) surface** nêu điều cần giải thích; **23. Decorators: phân biệt tiêu chuẩn (standard / 표준) direction và legacy experimental chế độ (mode / 모드)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. cấp cao (senior / 시니어) ghi chú (note / 노트): trình biên dịch (compiler / 컴파일러) cấu hình (config / 설정) là executable kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Decorators: phân biệt tiêu chuẩn (standard / 표준) direction và legacy experimental chế độ (mode / 모드)

TypeScript từng phổ biến `experimentalDecorators` dựa trên proposal cũ, đặc biệt trong Angular/Nest-like ecosystems. TypeScript 5.x hỗ trợ tiêu chuẩn (standard / 표준) decorators ngữ nghĩa (semantics / 의미론) mới. Hai hệ có differences về typing/thời gian chạy (runtime / 런타임) emit và siêu dữ liệu (metadata / 메타데이터) các giả định (assumptions / 가정들). Khi migrate khung phần mềm (framework / 프레임워크) mã (code / 코드), đừng chỉ xóa flag; xác nhận khung phần mềm (framework / 프레임워크) phiên bản (version / 버전), decorator đặc tả hợp đồng (contract / 계약) và siêu dữ liệu (metadata / 메타데이터) chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **24. cấp cao (senior / 시니어) ghi chú (note / 노트): trình biên dịch (compiler / 컴파일러) cấu hình (config / 설정) là executable kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **23. Decorators: phân biệt tiêu chuẩn (standard / 표준) direction và legacy experimental chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. trình biên dịch (compiler / 컴파일러) internals: parser, binder, checker và emit giữ những bất biến (invariant / 불변식) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. cấp cao (senior / 시니어) ghi chú (note / 노트): trình biên dịch (compiler / 컴파일러) cấu hình (config / 설정) là executable kiến trúc (architecture / 아키텍처)

`tsconfig`, gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터) và bundler cấu hình (config / 설정) cùng mô tả cách nguồn (source / 소스) biến thành thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물). Chúng không phải “setup một lần rồi quên”. Khi thời gian chạy (runtime / 런타임)/nền tảng (platform / 플랫폼) thay đổi, cấu hình (config / 설정) phải được kiểm tra (audit / 감사) như mã nguồn (source code / 소스 코드): giả định (assumption / 가정) nào còn đúng, option nào legacy, alias nào drift, declaration nào không còn match hiện thực (implementation / 구현)?

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **25. trình biên dịch (compiler / 컴파일러) internals: parser, binder, checker và emit giữ những bất biến (invariant / 불변식) khác nhau** tiếp nhận điểm tựa từ **24. cấp cao (senior / 시니어) ghi chú (note / 노트): trình biên dịch (compiler / 컴파일러) cấu hình (config / 설정) là executable kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Program đồ thị (graph / 그래프) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스): editor không chỉ check tệp (file / 파일) đang mở** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. trình biên dịch (compiler / 컴파일러) internals: parser, binder, checker và emit giữ những bất biến (invariant / 불변식) khác nhau

Chuỗi xử lý (pipeline / 파이프라인) trình biên dịch (compiler / 컴파일러) không phải một “hàm compile” nguyên khối. Parser biến đơn vị từ (token / 토큰)/nguồn (source / 소스) thành cú pháp (syntax / 문법) cây (tree / 트리). Binder đi qua cây (tree / 트리) để tạo symbol relationships và nối declarations vào scopes. Checker dùng symbols, types, control-flow facts và assignability relations để tạo diagnostics/suy luận (inference / 추론). Emit tạo JavaScript, declarations và nguồn (source / 소스) maps tùy cấu hình (config / 설정).

Mô hình tư duy (mental model / 사고 모델) này giải thích nhiều lỗi tưởng như vô lý. cú pháp (syntax / 문법) hợp lệ nhưng symbol trùng có thể thất bại (fail / 실패) ở binding. Symbol resolve được nhưng quan hệ (relation / 관계) kiểu (type / 타입) không hợp lệ thất bại (fail / 실패) ở checker. Type-check hoàn toàn sạch vẫn có thể emit/import sản phẩm tạo ra (artifact / 산출물) không chạy nếu thời gian chạy (runtime / 런타임)/mô-đun (module / 모듈) các giả định (assumptions / 가정들) sai.

Trong debugging trình biên dịch (compiler / 컴파일러) issue, hãy phân loại trước:

```text
parse/syntax
→ name/symbol resolution
→ type relation/control flow
→ emit/declaration generation
→ host/runtime loading
```

Nếu không phân tầng (layer / 계층), rất dễ dùng kiểu (type / 타입) assertion để “sửa” một module-resolution bug hoặc thay tsconfig để che một modeling bug.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **26. Program đồ thị (graph / 그래프) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스): editor không chỉ check tệp (file / 파일) đang mở** tiếp nhận điểm tựa từ **25. trình biên dịch (compiler / 컴파일러) internals: parser, binder, checker và emit giữ những bất biến (invariant / 불변식) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. verbatimModuleSyntax: nguồn (source / 소스) phải nói rõ import nào tồn tại ở thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Program đồ thị (graph / 그래프) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스): editor không chỉ check tệp (file / 파일) đang mở

IDE phải duy trì một **dự án (project / 프로젝트) đồ thị (graph / 그래프)** gồm nguồn (source / 소스) files, dependencies, declaration files, cấu hình (config / 설정) inheritance và gói (package / 패키지) siêu dữ liệu (metadata / 메타데이터). Auto-complete, rename, find references và diagnostics đều phụ thuộc đồ thị (graph / 그래프) này.

Một thay đổi ở dùng chung (shared / 공유) `.d.ts`, `tsconfig`, gói (package / 패키지) `exports` hoặc generated tệp (file / 파일) có thể làm hàng nghìn files invalidate dù bạn chỉ sửa một dòng. Đây là lý do editor độ trễ (latency / 지연 시간) thường liên quan đồ thị (graph / 그래프) topology chứ không chỉ độ dài tệp (file / 파일) đang mở.

TypeScript 7 chuyển editor foundation sang ngôn ngữ (language / 언어) máy chủ (server / 서버) giao thức (protocol / 프로토콜) (LSP) và bản địa (native / 네이티브) multithreaded hiện thực (implementation / 구현). Điều này giúp nhiều editor dùng cùng giao thức (protocol / 프로토콜) và cho phép ngôn ngữ (language / 언어) máy chủ (server / 서버) xử lý nhiều yêu cầu (request / 요청) đồng thời. Tuy vậy, embedded-language ecosystems như Vue/Svelte/Astro/MDX hoặc khung phần mềm (framework / 프레임워크) tooling cần trình biên dịch (compiler / 컴파일러) API có thể vẫn phụ thuộc TypeScript 6 trong giai đoạn 7.0 vì TypeScript 7.0 chưa có stable programmatic API.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **26. Program đồ thị (graph / 그래프) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스): editor không chỉ check tệp (file / 파일) đang mở** nêu điều cần giải thích; **27. verbatimModuleSyntax: nguồn (source / 소스) phải nói rõ import nào tồn tại ở thời gian chạy (runtime / 런타임)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **28. isolatedModules và isolatedDeclarations: khi mỗi tệp (file / 파일) phải tự đủ thông tin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. `verbatimModuleSyntax`: nguồn (source / 소스) phải nói rõ import nào tồn tại ở thời gian chạy (runtime / 런타임)

Trước đây import elision có nhiều quy tắc (rule / 규칙) khó đoán: trình biên dịch (compiler / 컴파일러) có thể bỏ import nếu nó chỉ được dùng như kiểu (type / 타입). `verbatimModuleSyntax` làm mô hình tư duy (mental model / 사고 모델) đơn giản hơn:

```ts
import type { User } from "./user.js";
import { createUser } from "./user.js";
```

Type-only cú pháp (syntax / 문법) bị xóa; import/export không có `type` được giữ theo mô-đun (module / 모듈) ngữ nghĩa (semantics / 의미론) thay vì trình biên dịch (compiler / 컴파일러) “đoán intent”. Điều này đặc biệt quan trọng khi mô-đun (module / 모듈) có side effects hoặc toolchain transpile từng tệp (file / 파일) độc lập.

Cấp cao (senior / 시니어) practice là dùng kiểu (type / 타입)/giá trị (value / 값) distinction rõ ở nguồn (source / 소스). Một import bị giữ hay xóa có thể thay thời gian chạy (runtime / 런타임) side tác động (effect / 효과), tree-shaking và cycle hành vi (behavior / 동작); đây không chỉ là style.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **27. verbatimModuleSyntax: nguồn (source / 소스) phải nói rõ import nào tồn tại ở thời gian chạy (runtime / 런타임)** nêu điều cần giải thích; **28. isolatedModules và isolatedDeclarations: khi mỗi tệp (file / 파일) phải tự đủ thông tin** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **29. gói (package / 패키지) exports là allow-list, không phải siêu dữ liệu (metadata / 메타데이터) trang trí** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `isolatedModules` và `isolatedDeclarations`: khi mỗi tệp (file / 파일) phải tự đủ thông tin

Một số transpiler xử lý từng tệp (file / 파일) mà không có toàn program đồ thị (graph / 그래프). `isolatedModules` cảnh báo những mẫu (pattern / 패턴) không thể transform an toàn theo kiểu per-file.

`isolatedDeclarations` đi vào công khai (public / 공개) kiểu (type / 타입) surface: nó buộc exported API cung cấp đủ annotation để declaration emit có thể được thực hiện mà không cần full ngữ nghĩa (semantic / 의미적) check toàn program. Điều này hữu ích cho hệ thống dựng (build system / 빌드 시스템) muốn song song hóa declaration generation hoặc bộ nhớ đệm (cache / 캐시) theo tệp (file / 파일)/gói (package / 패키지).

Sự đánh đổi (trade-off / 트레이드오프) là author phải viết tường minh (explicit / 명시적) công khai (public / 공개) annotations nhiều hơn. Đây là ví dụ tốt của kiến trúc (architecture / 아키텍처) pressure làm coding style thay đổi: annotation không phải vì trình biên dịch (compiler / 컴파일러) “không suy luận (inference / 추론) được”, mà vì bản dựng (build / 빌드) chuỗi xử lý (pipeline / 파이프라인) muốn giảm coupling giữa files.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **28. isolatedModules và isolatedDeclarations: khi mỗi tệp (file / 파일) phải tự đủ thông tin** nêu điều cần giải thích; **29. gói (package / 패키지) exports là allow-list, không phải siêu dữ liệu (metadata / 메타데이터) trang trí** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **30. typesVersions và versioned types conditions: phục vụ trình biên dịch (compiler / 컴파일러) cũ có chủ đích** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. gói (package / 패키지) `exports` là allow-list, không phải siêu dữ liệu (metadata / 메타데이터) trang trí

Khi resolver hiện đại đọc `package.json` có `exports`, subpath không match có thể bị chặn dù tệp (file / 파일) vật lý tồn tại.

```json
{
  "name": "my-lib",
  "exports": {
    ".": "./dist/index.js",
    "./client": "./dist/client.js"
  }
}
```

`import "my-lib/internal.js"` có thể thất bại (fail / 실패) dù `dist/internal.js` tồn tại. `exports` định nghĩa công khai (public / 공개) gói (package / 패키지) surface.

TypeScript ở `node16`/`nodenext`/`bundler` còn ưu tiên tìm điều kiện (condition / 조건) `types` khi resolve declaration surface. gói (package / 패키지) author vì thế phải kiểm thử (test / 테스트) cả JavaScript thời gian chạy (runtime / 런타임) resolution và TypeScript kiểu (type / 타입) resolution; publish đúng tệp (file / 파일) nhưng sai điều kiện (condition / 조건) vẫn có thể làm bên tiêu thụ (consumer / 소비자) mất types.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **29. gói (package / 패키지) exports là allow-list, không phải siêu dữ liệu (metadata / 메타데이터) trang trí** nêu điều cần giải thích; **30. typesVersions và versioned types conditions: phục vụ trình biên dịch (compiler / 컴파일러) cũ có chủ đích** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **31. Bundler-compatible nguồn (source / 소스) có thể tạo .d.ts không tương thích nodenext** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. `typesVersions` và versioned `types` conditions: phục vụ trình biên dịch (compiler / 컴파일러) cũ có chủ đích

Khi công khai (public / 공개) `.d.ts` dùng cú pháp (syntax / 문법) chỉ trình biên dịch (compiler / 컴파일러) mới hiểu, thư viện (library / 라이브러리) có thể cung cấp declaration khác theo TypeScript phiên bản (version / 버전). `typesVersions` là cơ chế legacy/phổ biến cho việc này, còn resolver qua `exports` có thể dùng versioned `types@...` conditions.

Điểm dễ nhầm: khi `exports` được đọc, `typesVersions` không phải lúc nào cũng quyết định resolution như bạn kỳ vọng. gói (package / 패키지) càng nhiều conditions càng cần bên tiêu thụ (consumer / 소비자) fixtures trên nhiều trình biên dịch (compiler / 컴파일러)/mô-đun (module / 모듈) modes.

Cấp cao (senior / 시니어) lesson: đừng hứa “hỗ trợ (support / 지원) TypeScript >= X” chỉ dựa trên nguồn (source / 소스) bản dựng (build / 빌드) của chính gói (package / 패키지). Hãy install tarball vào bên tiêu thụ (consumer / 소비자) dự án (project / 프로젝트) thật với minimum trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) và check công khai (public / 공개) imports.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **30. typesVersions và versioned types conditions: phục vụ trình biên dịch (compiler / 컴파일러) cũ có chủ đích** nêu điều cần giải thích; **31. Bundler-compatible nguồn (source / 소스) có thể tạo .d.ts không tương thích nodenext** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Chạy .ts trực tiếp và erasableSyntaxOnly: “kiểu (type / 타입) erasure” trở thành thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Bundler-compatible nguồn (source / 소스) có thể tạo `.d.ts` không tương thích `nodenext`

Một thư viện (library / 라이브러리) bản dựng (build / 빌드) bằng bundler có thể viết:

```ts
import { Component } from "./component";
```

Bundler hiểu extensionless relative import và xóa/ghép nó trong JavaScript đầu ra (output / 출력). Nhưng nếu `tsc` đồng thời emit nhiều declaration files, `.d.ts` có thể giữ specifier `./component`. bên tiêu thụ (consumer / 소비자) chạy `nodenext` có thể từ chối specifier đó vì ESM nút (node / 노드) yêu cầu extension phù hợp.

Đây là dạng thất bại (failure mode / 실패 모드) quan trọng: **JavaScript bundle chạy được nhưng declaration đồ thị (graph / 그래프) của bên tiêu thụ (consumer / 소비자) thất bại (fail / 실패)**.

Nếu thư viện (library / 라이브러리) không bundle declarations, cấu hình declaration emit cần mô hình (model / 모델) bên tiêu thụ (consumer / 소비자) thời gian chạy (runtime / 런타임) đủ chặt; với thư viện (library / 라이브러리) cho nút (node / 노드) consumers, `nodenext` thường cung cấp an toàn (safety / 안전) tốt hơn. Cách chắc chắn nhất vẫn là kiểm thử (test / 테스트) gói (package / 패키지) sản phẩm tạo ra (artifact / 산출물) trong bên tiêu thụ (consumer / 소비자) fixtures với mô-đun (module / 모듈) modes bạn tuyên bố hỗ trợ.

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **31. Bundler-compatible nguồn (source / 소스) có thể tạo .d.ts không tương thích nodenext** nêu điều cần giải thích; **32. Chạy .ts trực tiếp và erasableSyntaxOnly: “kiểu (type / 타입) erasure” trở thành thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. .ts extension trong import: nguồn (source / 소스) host và đầu ra (output / 출력) host có thể là hai thế giới khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Chạy `.ts` trực tiếp và `erasableSyntaxOnly`: “kiểu (type / 타입) erasure” trở thành thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약)

Một số thời gian chạy (runtime / 런타임) hiện đại có thể strip TypeScript cú pháp (syntax / 문법) và chạy tệp (file / 파일) `.ts` trực tiếp. Nhưng strip-only thời gian chạy (runtime / 런타임) chỉ hỗ trợ cú pháp (syntax / 문법) TypeScript có thể xóa mà không cần transform ngữ nghĩa (semantics / 의미론).

Các construct như `enum`, không gian tên (namespace / 네임스페이스) có thời gian chạy (runtime / 런타임) mã (code / 코드), parameter properties, `import =`/`export =` không chỉ là kiểu (type / 타입) cú pháp (syntax / 문법); chúng cần emit transform. `erasableSyntaxOnly` giúp trình biên dịch (compiler / 컴파일러) báo sớm những construct không phù hợp với strip-only thực thi (execution / 실행).

Nếu kiến trúc (architecture / 아키텍처) chọn direct-TypeScript thời gian chạy (runtime / 런타임), hãy xem đây là một **source-language subset** có chủ đích. Thường cần kết hợp với `verbatimModuleSyntax`, mô-đun (module / 모듈) settings đúng host và kiểm thử (test / 테스트) thời gian chạy (runtime / 런타임) thật. Không nên suy từ “tsc type-check pass” sang “nút (node / 노드)/Bun/Deno chắc chắn chạy nguồn (source / 소스) này”.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **32. Chạy .ts trực tiếp và erasableSyntaxOnly: “kiểu (type / 타입) erasure” trở thành thời gian chạy (runtime / 런타임) đặc tả hợp đồng (contract / 계약)** nêu điều cần giải thích; **33. .ts extension trong import: nguồn (source / 소스) host và đầu ra (output / 출력) host có thể là hai thế giới khác nhau** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **34. TypeScript 7 parallelism: nhiều CPU hơn không phải luôn nhanh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. `.ts` extension trong import: nguồn (source / 소스) host và đầu ra (output / 출력) host có thể là hai thế giới khác nhau

`allowImportingTsExtensions` hữu ích khi bundler/thời gian chạy (runtime / 런타임) đọc `.ts` trực tiếp hoặc dự án (project / 프로젝트) `noEmit`. Nhưng nếu cuối cùng phát hành `.js`, specifier `.ts` cần được host/bundler rewrite hoặc TypeScript dùng `rewriteRelativeImportExtensions` cho relative imports phù hợp.

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

Không trả lời đủ ba câu sẽ tạo dự án (project / 프로젝트) chạy trong dev loader nhưng thất bại (fail / 실패) sau bản dựng (build / 빌드), hoặc thư viện (library / 라이브러리) chạy kiểm thử (test / 테스트) nguồn (source / 소스) nhưng gói (package / 패키지) publish hỏng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **33. .ts extension trong import: nguồn (source / 소스) host và đầu ra (output / 출력) host có thể là hai thế giới khác nhau** nêu điều cần giải thích; **34. TypeScript 7 parallelism: nhiều CPU hơn không phải luôn nhanh hơn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **35. TypeScript 7 --watch: file-system hành vi (behavior / 동작) cũng là hiệu năng (performance / 성능) tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. TypeScript 7 parallelism: nhiều CPU hơn không phải luôn nhanh hơn

TypeScript 7 có thể chạy parsing/checking/emitting song song. `--checkers` điều khiển số checker workers; `--builders` điều khiển số project-reference builders; `--singleThreaded` hữu ích khi gỡ lỗi (debug / 디버그), benchmark hoặc CI ít tài nguyên.

Tăng workers làm tăng parallelism nhưng có thể tăng aggregate bộ nhớ (memory / 메모리) và duplicate công việc (work / 작업). Trong monorepo, `--checkers 4 --builders 4` có thể tạo áp lực gần như nhiều checker đồng thời hơn dự kiến. Vì vậy tuning phải dựa trên CPU, RAM, đồ thị (graph / 그래프) shape và CI contention.

Một dạng thất bại (failure mode / 실패 모드) hiếm nhưng quan trọng là order-dependent checking có thể lộ ra khi thay số checker. Nếu nhóm (team / 팀) gặp diagnostic khác giữa môi trường, cố định worker count trong điều tra và dùng `--singleThreaded` làm điều khiển (control / 제어) trường hợp (case / 사례) trước khi quy lỗi cho nguồn (source / 소스).

> **Chuyển mạch:** Trong **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **35. TypeScript 7 --watch: file-system hành vi (behavior / 동작) cũng là hiệu năng (performance / 성능) tầng (layer / 계층)** tiếp nhận điểm tựa từ **34. TypeScript 7 parallelism: nhiều CPU hơn không phải luôn nhanh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. TypeScript 6/7 defaults: upgrade phải kiểm tra (audit / 감사) các giả định (assumptions / 가정들), không chỉ sửa diagnostics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. TypeScript 7 `--watch`: file-system hành vi (behavior / 동작) cũng là hiệu năng (performance / 성능) tầng (layer / 계층)

Watch chế độ (mode / 모드) không chỉ là “chạy trình biên dịch (compiler / 컴파일러) lại khi save”. Nó phụ thuộc tệp (file / 파일) watcher, vô hiệu hóa (invalidation / 무효화) đồ thị (graph / 그래프), gói (package / 패키지) directories và OS hành vi (behavior / 동작). TypeScript 7 rebuild watch foundation để giảm polling/tài nguyên (resource / 자원) overhead và cải thiện cross-platform stability.

Nếu watch chế độ (mode / 모드) ngốn CPU, đừng chỉ profile checker. Hãy xem workspace có symlink/worktree lớn, generated directories, phụ thuộc (dependency / 의존성) trees hoặc công cụ (tool / 도구) khác cùng theo dõi quá nhiều files không. môi trường vận hành (production / 운영 환경) nhà phát triển (developer / 개발자) experience là tổng của tệp (file / 파일) watching + dự án (project / 프로젝트) đồ thị (graph / 그래프) vô hiệu hóa (invalidation / 무효화) + checking + bundling, không phải một con số `tsc` duy nhất.

> **Chuyển mạch:** Ở chặng này của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **36. TypeScript 6/7 defaults: upgrade phải kiểm tra (audit / 감사) các giả định (assumptions / 가정들), không chỉ sửa diagnostics** tiếp nhận điểm tựa từ **35. TypeScript 7 --watch: file-system hành vi (behavior / 동작) cũng là hiệu năng (performance / 성능) tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. TypeScript 7 không có trình biên dịch (compiler / 컴파일러) API: side-by-side không phải hack tạm bợ vô tổ chức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. TypeScript 6/7 defaults: upgrade phải kiểm tra (audit / 감사) các giả định (assumptions / 가정들), không chỉ sửa diagnostics

Các default hiện đại thay đổi mạnh: `strict` bật mặc định, `module` hướng `esnext`, `target` theo ECMAScript stable gần nhất, `noUncheckedSideEffectImports` bật, `rootDir` mặc định theo dự án (project / 프로젝트) gốc (root / 루트) và `types` mặc định thành `[]`. TypeScript 7 còn biến nhiều deprecation của 6.0 thành hard lỗi (error / 오류).

Điều nguy hiểm là một số thay đổi không tạo cùng dạng lỗi (error / 오류). `types: []` có thể làm toàn cục (global / 전역) `process`, `describe` hay `jest` biến mất; `rootDir` mới có thể làm đầu ra (output / 출력) đường dẫn (path / 경로) đổi; `moduleResolution node10` không còn hợp lệ; `baseUrl` legacy không còn là nền nên `paths` cần được hiểu relative theo dự án (project / 프로젝트) cấu hình (config / 설정) hiện đại.

Upgrade runbook đúng nên là:

```text
1. Chốt runtime/module host thật.
2. Nâng lên TS 6 và xử lý toàn bộ deprecation.
3. Ghi explicit những defaults mà project muốn sở hữu lâu dài.
4. Chạy clean type-check + package consumer tests.
5. Chuyển sang TS 7.
6. Benchmark build/editor/watch trên workload thật.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 03 — trình biên dịch (compiler / 컴파일러), Modules & Tooling**, **37. TypeScript 7 không có trình biên dịch (compiler / 컴파일러) API: side-by-side không phải hack tạm bợ vô tổ chức** tiếp nhận điểm tựa từ **36. TypeScript 6/7 defaults: upgrade phải kiểm tra (audit / 감사) các giả định (assumptions / 가정들), không chỉ sửa diagnostics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 37. TypeScript 7 không có trình biên dịch (compiler / 컴파일러) API: side-by-side không phải hack tạm bợ vô tổ chức

TypeScript 7.0 chưa ship stable programmatic trình biên dịch (compiler / 컴파일러) API. nhóm (team / 팀) TypeScript cung cấp đường chạy side-by-side với TypeScript 6 cho tooling còn phụ thuộc API. Điều này có nghĩa một repository có thể hợp lệ khi `tsc` CLI dùng 7.0 nhưng linter/khung phần mềm (framework / 프레임워크) plugin dùng 6.x tính tương thích (compatibility / 호환성) tầng (layer / 계층).

Điều cần quản lý là **phiên bản (version / 버전) quyền sở hữu (ownership / 소유권)**: công cụ (tool / 도구) nào dùng trình biên dịch (compiler / 컴파일러) nào, diagnostics nào là nguồn chuẩn (source of truth / 정본), và CI step nào bảo vệ ngữ nghĩa (semantics / 의미론) tương thích. Đừng để phụ thuộc (dependency / 의존성) resolver vô tình đổi toàn bộ ecosystem sang một trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) rồi coi lỗi plugin là lỗi ứng dụng (application / 애플리케이션).

---

Tiếp theo: [TypeScript 04 — Senior Production Engineering](typescript_04_senior_production.md).

> **Bàn giao:** Sau **37. TypeScript 7 không có trình biên dịch (compiler / 컴파일러) API: side-by-side không phải hack tạm bợ vô tổ chức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
