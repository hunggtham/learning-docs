# TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. mô hình tư duy (mental model / 사고 모델): phiên bản (version / 버전) number không đồng nghĩa ngôn ngữ (language / 언어) generation** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **2. Timeline tổng quát** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

> Prerequisite: [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md). Chapter này không phải changelog. Mục tiêu là hiểu **vì sao TypeScript thay đổi**, thay đổi đó nằm ở hệ kiểu (type system / 타입 시스템), trình biên dịch (compiler / 컴파일러), mô-đun (module / 모듈) host hay tooling tầng (layer / 계층) nào, và một codebase môi trường vận hành (production / 운영 환경) phải lập luận (reasoning / 추론) thế nào khi nâng phiên bản (version / 버전).

Baseline của nhánh học (track / 트랙) hiện tại là **TypeScript 7.0**. Khi đọc tài liệu cũ hoặc maintain dự án (project / 프로젝트) legacy, đừng hỏi duy nhất “tính năng (feature / 기능) này có từ phiên bản (version / 버전) nào?”. Câu hỏi quan trọng hơn là: phiên bản (version / 버전) mới có làm thay đổi proof mà checker suy ra không, có đổi JavaScript emit không, có đổi mô-đun (module / 모듈) resolution không, có đổi declaration/API công khai (public API / 공개 API) không, hay chỉ thay trình biên dịch (compiler / 컴파일러) kiến trúc (architecture / 아키텍처) và hiệu năng (performance / 성능)?

## 1. mô hình tư duy (mental model / 사고 모델): phiên bản (version / 버전) number không đồng nghĩa ngôn ngữ (language / 언어) generation

TypeScript tiến hóa trên nhiều trục cùng lúc. Một bản phát hành (release / 릴리스) có thể thêm cú pháp (syntax / 문법)/type-system tính năng (feature / 기능) nhưng gần như không đổi thời gian chạy (runtime / 런타임) sản phẩm tạo ra (artifact / 산출물); bản phát hành (release / 릴리스) khác có thể giữ kiểu (type / 타입) ngữ nghĩa (semantics / 의미론) gần như nguyên vẹn nhưng thay toàn bộ trình biên dịch (compiler / 컴파일러) hiện thực (implementation / 구현). TypeScript 4.9 với `satisfies` là ví dụ của thay đổi type-model ergonomics. TypeScript 5.0 thay đổi decorator ngữ nghĩa (semantics / 의미론) và mô-đun (module / 모듈) emit controls. TypeScript 6.0 chủ yếu là chuyển tiếp (transition / 전이) bản phát hành (release / 릴리스) với default/deprecation cleanup. TypeScript 7.0 lại là architectural generation thay đổi (change / 변경): trình biên dịch (compiler / 컴파일러) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스) chuyển sang bản địa (native / 네이티브) Go hiện thực (implementation / 구현) trong khi cố giữ checking hành vi (behavior / 동작) tương thích với 6.0.

Vì vậy khi upgrade, hãy tách ít nhất năm câu hỏi:

```text
source syntax có đổi không?
→ checker/inference có đổi không?
→ emit có đổi không?
→ module/package resolution có đổi không?
→ compiler/editor/build architecture có đổi không?
```

Nếu không tách năm lớp này, nhóm (team / 팀) rất dễ gọi một thời gian chạy (runtime / 런타임) ESM thất bại (failure / 실패) là “TypeScript 7 bug”, hoặc ngược lại coi một suy luận (inference / 추론) tightening là “chỉ tooling thay đổi (change / 변경)”.

Một phiên bản (version / 버전) ghi chú (note / 노트) tốt vì thế không chỉ ghi “tính năng (feature / 기능) X xuất hiện ở 5.4”. Nó phải cho biết tính năng (feature / 기능) X thay đổi nguồn proof nào, có làm công khai (public / 공개) `.d.ts` đổi không, có phụ thuộc thời gian chạy (runtime / 런타임) không và có tạo di chuyển (migration / 마이그레이션) rủi ro (risk / 위험) ở đâu.

> **Chuyển mạch:** Trong **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **2. Timeline tổng quát** gom các mảnh từ **1. mô hình tư duy (mental model / 사고 모델): phiên bản (version / 버전) number không đồng nghĩa ngôn ngữ (language / 언어) generation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **3. TypeScript 1.x–3.x: legacy kiến thức (knowledge / 지식) vẫn xuất hiện trong môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Timeline tổng quát

| Giai đoạn | Chuyển dịch chính | Tác động mô hình tư duy (mental model / 사고 모델) |
|---|---|---|
| TypeScript 1.x | annotation, giao diện (interface / 인터페이스), lớp (class / 클래스), generic | JavaScript có thêm static đặc tả hợp đồng (contract / 계약) tầng (layer / 계층) |
| TypeScript 2.x | control-flow phân tích (analysis / 분석), strict nullability, mapped/conditional kiểu (type / 타입) foundations | kiểu (type / 타입) bắt đầu được suy ra từ điều khiển (control / 제어) luồng (flow / 흐름) và kiểu (type / 타입) transformation |
| TypeScript 3.x | `unknown`, dự án (project / 프로젝트) references, tuple/suy luận (inference / 추론) improvements, optional chaining/nullish coalescing ở cuối 3.x | trust ranh giới (boundary / 경계) và large-project bản dựng (build / 빌드) mô hình (model / 모델) trưởng thành |
| TypeScript 4.x | variadic tuple, template literal kiểu (type / 타입), stronger CFA, nút (node / 노드) ESM modeling, `satisfies` | type-level programming trở thành công cụ API modeling mạnh |
| TypeScript 5.x | tiêu chuẩn (standard / 표준) decorators, const kiểu (type / 타입) parameters, hiện đại (modern / 현대적) mô-đun (module / 모듈) controls, `NoInfer`, inferred predicates, isolated declarations, direct-TS thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원) | TypeScript dịch từ “transpiler + checker” sang một thành phần trong toolchain đa trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) |
| TypeScript 6.0 | chuyển tiếp (transition / 전이)/deprecation/default cleanup | ép dự án (project / 프로젝트) khai báo giả định (assumption / 가정) hiện đại trước bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러) |
| TypeScript 7.0 | bản địa (native / 네이티브) Go trình biên dịch (compiler / 컴파일러)/ngôn ngữ (language / 언어) dịch vụ (service / 서비스), parallel kiến trúc (architecture / 아키텍처) | ngữ nghĩa (semantics / 의미론) gần 6.0 nhưng quy mô (scale / 규모)/bản dựng (build / 빌드)/editor mô hình (model / 모델) thay đổi lớn |

Bảng này chỉ là map. Phần dưới tập trung vào các mốc làm thay đổi cách lập luận (reasoning / 추론) hoặc di chuyển (migration / 마이그레이션), không cố liệt kê mọi release-note item.

> **Chuyển mạch:** Timeline đặt các breaking change và capability vào đúng mốc; phần 1.x–3.x tập trung legacy behavior còn gặp trong production. Type-level programming của 4.x tiếp theo giải thích capability mới và migration cost.

## 3. TypeScript 1.x–3.x: legacy kiến thức (knowledge / 지식) vẫn xuất hiện trong môi trường vận hành (production / 운영 환경)

TypeScript 1.x đặt vocabulary cơ bản: annotation, giao diện (interface / 인터페이스), lớp (class / 클래스) và generic. Những concept này vẫn tồn tại, nhưng mã (code / 코드) hiện đại không nên học TypeScript như “Java/C# cú pháp (syntax / 문법) đặt lên JavaScript”. Structural typing, suy luận (inference / 추론) và JavaScript ngữ nghĩa thời gian chạy (runtime semantics / 런타임 의미론) quan trọng hơn việc ghi nhớ từ khóa (keyword / 키워드).

TypeScript 2.x là giai đoạn hệ kiểu trở nên gần với TypeScript hiện đại. Control-flow based kiểu (type / 타입) phân tích (analysis / 분석) khiến kiểu (type / 타입) của một variable có thể được narrow theo branch thay vì chỉ giữ declared kiểu (type / 타입). `strictNullChecks` biến `null`/`undefined` từ giá trị gần như có thể đi khắp nơi thành trạng thái phải mô hình (model / 모델). Mapped và conditional types mở đường cho kiểu (type / 타입) transformation thay vì chỉ khai báo shape thủ công.

TypeScript 3.x tiếp tục làm trust ranh giới (boundary / 경계) rõ hơn với `unknown`, đồng thời dự án (project / 프로젝트) references tạo mô hình bản dựng (build / 빌드) đồ thị (graph / 그래프) cho repository lớn. Optional chaining `?.` và nullish coalescing `??` xuất hiện cuối 3.x, nhưng cần nhớ đây là JavaScript thời gian chạy (runtime / 런타임) cú pháp (syntax / 문법) được TypeScript hỗ trợ, không phải bằng chứng rằng dữ liệu bên ngoài đã được validate.

Khi maintain mã (code / 코드) legacy, dấu hiệu của mô hình tư duy (mental model / 사고 모델) cũ thường là non-strict null handling, không gian tên (namespace / 네임스페이스)/ambient toàn cục (global / 전역) lớn, decorator legacy, CommonJS interop workaround và cast dày đặc. Không rewrite chỉ vì cú pháp (syntax / 문법) cũ; trước tiên xác định thời gian chạy (runtime / 런타임)/mô-đun (module / 모듈) các giả định (assumptions / 가정들) và công khai (public / 공개) ABI.

> **Chuyển mạch:** Legacy behavior từ 1.x–3.x giải thích migration constraints; 4.x đưa type-level programming vào mainstream. TypeScript 5.x tiếp theo mở rộng capability trong toolchain hiện đại.

## 4. TypeScript 4.x: type-level programming trở thành mainstream

### 4.1 TypeScript 4.0 — variadic tuple types

Variadic tuple types làm generic hàm (function / 함수) giữ được quan hệ giữa nhiều parameter/return positions mà trước đây cần overload dài. Giá trị của tính năng (feature / 기능) không phải “tuple cú pháp (syntax / 문법) mạnh hơn”, mà là khả năng biểu diễn quan hệ (relation / 관계) như concat, partial ứng dụng (application / 애플리케이션) hay middleware chuỗi xử lý (pipeline / 파이프라인) mà không làm mất positional thông tin (information / 정보).

```ts
function tail<T extends readonly unknown[]>(
  value: readonly [unknown, ...T]
): T {
  const [, ...rest] = value;
  return rest;
}
```

Đây là bước quan trọng dẫn tới API generic có suy luận (inference / 추론) tốt hơn, nhưng cũng mở cửa cho type-level lớp trừu tượng (abstraction / 추상화) quá phức tạp. môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙) vẫn là: quan hệ (relation / 관계) phải có giá trị lĩnh vực (domain / 도메인)/API rõ ràng mới đáng trả cognitive chi phí (cost / 비용).

### 4.2 TypeScript 4.1 — template literal types và key remapping

Template literal types cho phép tạo string union từ kiểu (type / 타입) thông tin (information / 정보); mapped kiểu (type / 타입) có thể remap key bằng `as`. Từ đây TypeScript có thể mô hình (model / 모델) sự kiện (event / 이벤트) names, tuyến (route / 경로) keys, getter/setter conventions và DSL nhỏ ở compile thời gian (time / 시간).

```ts
type EventName<T extends string> = `${T}Changed`;
type UserEvent = EventName<"name" | "email">;
// "nameChanged" | "emailChanged"
```

Power này có combinatorial chi phí (cost / 비용). Nếu union A có hàng trăm member và được nhân với union B/C, editor độ trễ (latency / 지연 시간) có thể trở thành môi trường vận hành (production / 운영 환경) bài toán (problem / 문제). TypeScript 7 nhanh hơn không làm exponential kiểu (type / 타입) shape biến mất.

### 4.3 TypeScript 4.4 — CFA qua alias, `unknown` trong `catch`, chính xác (exact / 정확한) optional properties

4.4 cải thiện control-flow phân tích (analysis / 분석) qua aliased conditions/discriminants. Một guard được lưu vào biến `const` có thể tiếp tục mang bằng chứng (evidence / 증거) cho checker thay vì bằng chứng (evidence / 증거) biến mất ngay khi expression được tách ra.

`useUnknownInCatchVariables` làm rõ một sự thật thời gian chạy (runtime / 런타임): JavaScript cho phép `throw` gần như bất kỳ giá trị (value / 값) nào, không chỉ `Error`. Với strict chế độ (mode / 모드), mã (code / 코드) phải narrow trước khi đọc `message` hay `stack`. Đây là ví dụ điển hình của TypeScript chuyển từ convenience unsoundness sang tường minh (explicit / 명시적) proof.

`exactOptionalPropertyTypes` phân biệt “thuộc tính (property / 속성) không tồn tại” với “thuộc tính (property / 속성) tồn tại nhưng giá trị (value / 값) là `undefined`” khi kiểu (type / 타입) không cho phép `undefined`. Hai trạng thái có thể khác nhau ở đối tượng (object / 객체) spread, serialization, `in` check và API patch ngữ nghĩa (semantics / 의미론).

```ts
interface Patch {
  nickname?: string;
}

// Với exactOptionalPropertyTypes:
const a: Patch = {};                    // absent
// const b: Patch = { nickname: undefined }; // không tương đương nếu type không chứa undefined
```

Đây không chỉ là strictness cosmetic. Với PATCH API, “không gửi trường dữ liệu (field / 필드)” có thể nghĩa là giữ nguyên, trong khi “gửi trường dữ liệu (field / 필드) = null/undefined” có thể mang ngữ nghĩa (semantic / 의미적) khác.

### 4.4 TypeScript 4.5 — `Awaited`, type-only imports và type-level hiệu năng (performance / 성능)

`Awaited<T>` mô hình (model / 모델) việc `await` recursively unwrap Promise/PromiseLike. Ý nghĩa lớn hơn utility kiểu (type / 타입) là TypeScript bắt đầu mô hình hóa async composition chính xác hơn trong các API như `Promise.all`.

4.5 cũng cho phép `type` modifier trên từng named import. Điều này rất quan trọng trong toolchain xử lý từng tệp (file / 파일) độc lập: nguồn (source / 소스) nói rõ binding nào chỉ tồn tại ở kiểu (type / 타입) không gian (space / 공간) và có thể erase.

```ts
import { createUser, type User } from "./user.js";
```

`preserveValueImports` ở giai đoạn này là một bước lịch sử dẫn tới mô hình tư duy (mental model / 사고 모델) rõ hơn của `verbatimModuleSyntax` sau này. Khi đọc cấu hình (config / 설정) cũ, đừng giữ option chỉ vì “đang chạy”; xác định nó từng giải quyết import-elision bài toán (problem / 문제) nào.

4.5 còn tối ưu một số tail-recursive conditional types. Bài học không phải “recursive kiểu (type / 타입) giờ miễn phí”: checker vẫn có độ sâu (depth / 깊이)/độ phức tạp (complexity / 복잡도) heuristics. Type-level parser hoặc giant recursive transform vẫn cần ngân sách (budget / 예산) như mã (code / 코드) thời gian chạy (runtime / 런타임) cần CPU ngân sách (budget / 예산).

### 4.5 TypeScript 4.7 — nút (node / 노드) ESM trở thành module-resolution concern chính thức

Các chế độ (mode / 모드) `node16`/`nodenext` khiến TypeScript phải mô hình (model / 모델) gần hơn hành vi (behavior / 동작) của nút (node / 노드): gói (package / 패키지) `type`, tệp (file / 파일) extension, conditional exports và ESM/CJS ranh giới (boundary / 경계). Đây là mốc quan trọng vì từ đây “IDE resolve được import” không còn đủ để chứng minh thời gian chạy (runtime / 런타임) host sẽ tải (load / 로드) mô-đun (module / 모듈) giống vậy.

4.7 cũng thêm instantiation expressions và `infer ... extends ...`, giúp API/type-level mã (code / 코드) biểu diễn specialization và mẫu (pattern / 패턴) matching gọn hơn. Nhưng với môi trường vận hành (production / 운영 환경) debugging, thay đổi mô-đun (module / 모듈) mô hình (model / 모델) quan trọng hơn cú pháp (syntax / 문법) mới: trình biên dịch (compiler / 컴파일러) phải biết host đang dùng `import` ngữ nghĩa (semantics / 의미론) hay `require` ngữ nghĩa (semantics / 의미론) để chọn điều kiện (condition / 조건) và declaration phù hợp.

### 4.6 TypeScript 4.8 — narrowing/intersection normalization chính xác hơn

4.8 cải thiện intersection reduction và narrowing quanh `unknown`, `null`, `undefined`, đồng thời tăng suy luận (inference / 추론) cho `infer` trong template string types. Đây là loại bản phát hành (release / 릴리스) dễ tạo di chuyển (migration / 마이그레이션) surprise: nguồn (source / 소스) cú pháp (syntax / 문법) không đổi nhưng checker có proof tốt hơn, nên inferred kiểu (type / 타입) hoặc lỗi (error / 오류) surface có thể đổi.

Mô hình tư duy (mental model / 사고 모델) cần giữ là **checker phiên bản (version / 버전) là một phần của proof engine**. Một generic utility compile ở 4.7 nhưng thất bại (fail / 실패) ở 4.8 không nhất thiết do ngôn ngữ (language / 언어) cú pháp (syntax / 문법) breaking; có thể do assignability hoặc normalization được sửa cho chính xác hơn.

### 4.7 TypeScript 4.9 — `satisfies`

`satisfies` giải quyết tension giữa **kiểm tra hợp lệ (validation / 검증) của expression** và **giữ suy luận (inference / 추론) cụ thể của expression**.

```ts
type Route = "home" | "settings";

const paths = {
  home: "/",
  settings: "/settings"
} satisfies Record<Route, string>;
```

Khác với annotation rộng, `satisfies` kiểm tra tính tương thích (compatibility / 호환성) mà không ép resulting expression kiểu (type / 타입) thành mục tiêu (target / 대상) kiểu (type / 타입). Nó đặc biệt hữu ích cho cấu hình (config / 설정) đối tượng (object / 객체), tuyến (route / 경로) map, đơn vị từ (token / 토큰) map và registry. Nhưng `satisfies` vẫn là compile-time proof; nó không validate JSON/cấu hình (config / 설정) được đọc ở thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Type-level programming từ 4.x tạo nền cho toolchain 5.x; khi sang 6.0, migration cần xem release boundary cụ thể thay vì coi đó là “TypeScript 7 lite”.

## 5. TypeScript 5.x: hiện đại (modern / 현대적) TypeScript toolchain

TypeScript 5.x nên được xem như một chuỗi thay đổi làm rõ ranh giới giữa TypeScript checker và JavaScript ecosystem xung quanh nó.

### 5.1 TypeScript 5.0 — tiêu chuẩn (standard / 표준) decorators, const kiểu (type / 타입) parameters và mô-đun (module / 모듈) emit rõ hơn

5.0 hỗ trợ decorator ngữ nghĩa (semantics / 의미론) mới theo hướng ECMAScript proposal mà không cần legacy `experimentalDecorators`. Legacy decorators vẫn là một chế độ (mode / 모드) khác với hành vi (behavior / 동작)/type-checking khác; tiêu chuẩn (standard / 표준) decorators không đơn giản là rename API cũ. Codebase dùng khung phần mềm (framework / 프레임워크)/decorator siêu dữ liệu (metadata / 메타데이터) phải kiểm tra khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) trước di chuyển (migration / 마이그레이션).

`const` kiểu (type / 타입) parameters cho thư viện (library / 라이브러리) author yêu cầu suy luận (inference / 추론) literal-specific ngay từ API ranh giới (boundary / 경계):

```ts
function defineRoutes<const T extends readonly string[]>(routes: T) {
  return routes;
}

const routes = defineRoutes(["/", "/users"]);
```

5.0 cũng giới thiệu `verbatimModuleSyntax`. mô hình tư duy (mental model / 사고 모델) là: import/export không có `type` modifier được giữ theo mô-đun (module / 모듈) cú pháp (syntax / 문법); type-only import/export bị erase. Điều này giảm “trình biên dịch (compiler / 컴파일러) đoán hộ import nào là thời gian chạy (runtime / 런타임) giá trị (value / 값)” và làm mã nguồn (source code / 소스 코드) nói rõ hơn sản phẩm tạo ra (artifact / 산출물) intent.

`moduleResolution: "bundler"` phản ánh một host khác nút (node / 노드) trực tiếp. Đây không phải “nodenext dễ hơn”; nó mô hình (model / 모델) resolver các giả định (assumptions / 가정들) của bundler. thư viện (library / 라이브러리) publish cho nút (node / 노드) consumers vẫn phải kiểm thử (test / 테스트) bên tiêu thụ (consumer / 소비자) dưới `node16`/`nodenext` khi phù hợp.

### 5.2 TypeScript 5.1 — nhỏ về cú pháp (syntax / 문법), đáng chú ý về assignability

5.1 làm `undefined`-returning functions gần JavaScript ngữ nghĩa (semantics / 의미론) hơn: hàm (function / 함수) được kỳ vọng trả `undefined` không còn luôn phải có tường minh (explicit / 명시적) `return undefined`. Nó cũng cho getter và setter có tường minh (explicit / 명시적) types không liên quan trực tiếp với nhau.

Điểm cấp cao (senior / 시니어) cần chú ý là read kiểu (type / 타입) và ghi (write / 쓰기) kiểu (type / 타입) của một thuộc tính (property / 속성) có thể là hai đặc tả hợp đồng (contract / 계약) khác nhau. DOM/khung phần mềm (framework / 프레임워크) adapter có thể nhận đầu vào (input / 입력) dạng rộng nhưng expose normalized đầu ra (output / 출력) dạng hẹp. Đừng suy luận “đọc được kiểu (type / 타입) X thì chắc chắn cũng ghi được X” hoặc ngược lại.

### 5.3 TypeScript 5.2 — tường minh (explicit / 명시적) tài nguyên (resource / 자원) management

5.2 hỗ trợ `using`/`await using` theo tường minh (explicit / 명시적) tài nguyên (resource / 자원) management ngữ nghĩa (semantics / 의미론). Bản chất là đưa tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) vào cú pháp (syntax / 문법)/giao thức (protocol / 프로토콜) thay vì dựa hoàn toàn vào convention `try/finally`.

Đừng suy ra TypeScript tự quản lý mọi tài nguyên (resource / 자원). đối tượng (object / 객체) phải tham gia disposal giao thức (protocol / 프로토콜) phù hợp; cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션), khóa (lock / 잠금) hay tệp (file / 파일) handle vẫn cần API hiện thực (implementation / 구현) đúng. Đây là ví dụ nơi ngôn ngữ (language / 언어) cú pháp (syntax / 문법) làm vòng đời (lifecycle / 생명주기) tường minh (explicit / 명시적) nhưng thời gian chạy (runtime / 런타임) bất biến (invariant / 불변식) vẫn thuộc hiện thực (implementation / 구현).

### 5.4 TypeScript 5.3 — import attributes và resolution chế độ (mode / 모드)

5.3 hỗ trợ import attributes với `with`, ví dụ `import data from "./data.json" with { type: "json" }`. TypeScript không chứng minh host hiểu mọi attribute; attribute là thông tin (information / 정보) truyền cho thời gian chạy (runtime / 런타임)/loader. Vì vậy compile success không thay thế thời gian chạy (runtime / 런타임) tính tương thích (compatibility / 호환성) kiểm thử (test / 테스트).

`resolution-mode` cho kiểu (type / 타입) imports cho phép declaration/thư viện (library / 라이브러리) mã (code / 코드) nói rõ một kiểu (type / 타입) specifier cần được resolve theo `import` hay `require` ngữ nghĩa (semantics / 의미론). Đây là chi tiết quan trọng trong gói (package / 패키지) dual ESM/CJS: cùng gói (package / 패키지) name có thể expose kiểu (type / 타입) surface khác theo điều kiện (condition / 조건).

### 5.5 TypeScript 5.4 — `NoInfer`

`NoInfer<T>` cho phép API author chặn một vị trí trở thành nguồn candidate cho generic suy luận (inference / 추론). Nó hữu ích khi một parameter phải **được kiểm tra theo T đã suy ra từ nơi khác**, thay vì cùng tham gia quyết định T.

```ts
function choose<C extends string>(
  choices: C[],
  fallback: NoInfer<C>
) {}

choose(["red", "green"], "blue"); // error
```

Mô hình tư duy (mental model / 사고 모델): `NoInfer` điều khiển **direction of suy luận (inference / 추론)**, không tạo nominal kiểu (type / 타입) và không validate thời gian chạy (runtime / 런타임) giá trị (value / 값).

### 5.6 TypeScript 5.5 — inferred kiểu (type / 타입) predicates và isolated declarations

5.5 có thể infer kiểu (type / 타입) predicate cho một số boolean hàm (function / 함수) đủ rõ. Điều này làm patterns như `.filter(x => x !== undefined)` giữ kiểu (type / 타입) chính xác hơn mà không cần custom guard thủ công.

```ts
const values = [1, undefined, 2].filter(x => x !== undefined);
// 5.5 có thể suy ra number[]
```

Tính năng (feature / 기능) này cũng có di chuyển (migration / 마이그레이션) consequence: kiểu (type / 타입) có thể trở nên **hẹp hơn** so với phiên bản (version / 버전) cũ. Nếu downstream mã (code / 코드) cố push `undefined` trở lại array, mã (code / 코드) từng compile có thể bắt đầu thất bại (fail / 실패). “suy luận (inference / 추론) tốt hơn” vẫn có thể là source-breaking ở compile thời gian (time / 시간).

Cùng bản phát hành (release / 릴리스) này, `isolatedDeclarations` yêu cầu exported surface đủ annotation để declaration generation có thể được thực hiện mà không cần full cross-file kiểu (type / 타입) suy luận (inference / 추론). Đây là thay đổi kiến trúc quan trọng cho monorepo/bản dựng (build / 빌드) công cụ (tool / 도구): API công khai (public API / 공개 API) rõ hơn đổi lấy annotation burden lớn hơn, nhưng mở đường cho declaration emit song song hoặc công cụ (tool / 도구) khác ngoài TypeScript trình biên dịch (compiler / 컴파일러).

### 5.7 TypeScript 5.6 — side-effect imports, split emit/check và bản dựng (build / 빌드) đồ thị (graph / 그래프) hành vi (behavior / 동작)

`noUncheckedSideEffectImports` biến unresolved side-effect import từ hành vi (behavior / 동작) dễ bị bỏ qua thành diagnostic. Đây là tính đúng đắn (correctness / 정확성) improvement quan trọng vì typo trong `import "./setup.css"` hay `import "polyfill-x"` có thể trước đó không được checker báo như nhà phát triển (developer / 개발자) kỳ vọng. Với asset imports, dự án (project / 프로젝트) cần ambient mô-đun (module / 모듈) declaration phù hợp thay vì tắt kiểm tra vô thức.

`--noCheck` cho phép tách emit khỏi full ngữ nghĩa (semantic / 의미적) type-check. Kết hợp với `isolatedDeclarations`, toolchain có thể emit JavaScript/declaration theo đường nhanh và chạy `tsc --noEmit` như cổng chất lượng (quality gate / 품질 게이트) riêng. Nhưng tên `noCheck` không có nghĩa “trình biên dịch (compiler / 컴파일러) tuyệt đối không phân tích kiểu (type / 타입)”; nếu declaration emit cần suy luận (inference / 추론), trình biên dịch (compiler / 컴파일러) vẫn có thể làm phần ngữ nghĩa (semantic / 의미적) công việc (work / 작업) tối thiểu cần thiết.

5.6 cũng thay `--build`: dự án (project / 프로젝트) references có thể tiếp tục qua intermediate errors theo best-effort, thay vì luôn dừng ngay. CI muốn fail-fast phải hiểu và cấu hình chính sách (policy / 정책) tương ứng, ví dụ `--stopOnBuildErrors`. Đây là ví dụ rõ rằng **bản dựng (build / 빌드) orchestration ngữ nghĩa (semantics / 의미론)** có thể đổi dù nguồn (source / 소스) ngôn ngữ (language / 언어) không đổi.

### 5.8 TypeScript 5.7 — relative TypeScript import có thể được rewrite cho đầu ra (output / 출력)

`rewriteRelativeImportExtensions` giải quyết một phần friction khi nguồn (source / 소스) dùng extension `.ts`/`.tsx`/`.mts`/`.cts` nhưng emitted JavaScript cần extension thời gian chạy (runtime / 런타임) tương ứng.

```ts
import { parse } from "./parse.ts";
// với rewriteRelativeImportExtensions có thể emit thành ./parse.js
```

Option này chỉ rewrite relative specifier đủ điều kiện. Nó không tự biến `paths`, gói (package / 패키지) `imports`, gói (package / 패키지) `exports` hay arbitrary động (dynamic / 동적) imports thành runtime-valid paths. Nếu nguồn (source / 소스) import `@app/user`, TypeScript không thể chỉ từ option này biết bundler/thời gian chạy (runtime / 런타임) phải rewrite alias thành gì. mô-đun (module / 모듈) specifier vẫn là đặc tả hợp đồng (contract / 계약) với host.

### 5.9 TypeScript 5.8 — `erasableSyntaxOnly` và direct-TypeScript runtimes

Khi thời gian chạy (runtime / 런타임)/công cụ (tool / 도구) có thể strip kiểu (type / 타입) cú pháp (syntax / 문법) và chạy TypeScript trực tiếp, không phải mọi TypeScript construct đều an toàn. `enum`, parameter properties, không gian tên (namespace / 네임스페이스) có thời gian chạy (runtime / 런타임) mã (code / 코드) và một số TypeScript-specific mô-đun (module / 모듈) forms cần transformation chứ không chỉ erase kiểu (type / 타입).

`erasableSyntaxOnly` giúp dự án (project / 프로젝트) giới hạn nguồn (source / 소스) vào cú pháp (syntax / 문법) có thể bị type-strip mà không cần TypeScript-specific thời gian chạy (runtime / 런타임) transform. Đây là cầu nối (bridge / 브리지) quan trọng giữa checker và thời gian chạy (runtime / 런타임) như nút (node / 노드) có type-stripping hỗ trợ (support / 지원).

```text
TypeScript syntax
├─ erasable type syntax → runtime có thể strip
└─ syntax tạo runtime behavior → cần transform/emitter hiểu TypeScript
```

Khi bật chế độ (mode / 모드) này, mục tiêu không phải “mã (code / 코드) TypeScript thuần hơn”, mà là bảo đảm thời gian chạy (runtime / 런타임) chiến lược (strategy / 전략) **strip-only** có cùng giả định (assumption / 가정) với nguồn (source / 소스).

### 5.10 TypeScript 5.9 — `import defer`, stable nút (node / 노드) 20 mô hình (model / 모델) và suy luận (inference / 추론) tightening

5.9 tiếp tục chuẩn hóa setup hiện đại. `tsc --init` sinh cấu hình (config / 설정) gọn hơn với các giả định (assumptions / 가정들) như `strict`, `verbatimModuleSyntax`, `isolatedModules`, `noUncheckedSideEffectImports` và các stricter options đáng cân nhắc. bản sao (copy / 복사) generated cấu hình (config / 설정) vào legacy ứng dụng (application / 애플리케이션) mà không hiểu bundler/thời gian chạy (runtime / 런타임) không phải di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략).

`import defer` cho phép mô-đun (module / 모듈) được tải (load / 로드) nhưng trì hoãn evaluation cho tới lần đầu không gian tên (namespace / 네임스페이스) member được truy cập. TypeScript không downlevel cú pháp (syntax / 문법) này; thời gian chạy (runtime / 런타임) hoặc bundler phải hỗ trợ (support / 지원). Vì vậy đây là host năng lực (capability / 역량), không phải TypeScript thời gian chạy (runtime / 런타임) tính năng (feature / 기능).

```ts
import defer * as feature from "./expensive-feature.js";
// module evaluation bị trì hoãn cho tới khi đọc feature.someExport
```

5.9 cũng có stable `--module node20`, hữu ích khi dự án (project / 프로젝트) muốn mô hình (model / 모델) nút (node / 노드) 20 cố định thay vì `nodenext` floating hành vi (behavior / 동작). Đồng thời có type-argument suy luận (inference / 추론) changes để sửa leak của kiểu (type / 타입) variables; một số generic calls có thể cần tường minh (explicit / 명시적) kiểu (type / 타입) arguments sau upgrade. Đây là reminder rằng patching suy luận (inference / 추론) tính đúng đắn (correctness / 정확성) có thể làm compile surface đổi dù thời gian chạy (runtime / 런타임) mã (code / 코드) không đổi.

> **Chuyển mạch:** TypeScript 5.x là baseline tooling; 6.0 là ranh giới chuyển tiếp, nên bằng chứng migration quan trọng hơn nhãn “7 lite”. Hãy kiểm tra typecheck, emit, declarations và runtime consumer trước khi kết luận.

## 6. TypeScript 6.0: chuyển tiếp (transition / 전이) bản phát hành (release / 릴리스), không phải “TypeScript 7 lite”

TypeScript 6.0 phát hành ngày 23/03/2026 và là stable bản phát hành (release / 릴리스) cuối cùng trên trình biên dịch (compiler / 컴파일러) codebase JavaScript cũ. Vai trò lớn nhất của nó là **cầu nối (bridge / 브리지) từ 5.9 sang bản địa (native / 네이티브) TypeScript 7**.

6.0 tiếp tục loại bỏ/deprecate các giả định (assumptions / 가정들) không còn phù hợp với ecosystem hiện đại và chuẩn bị hành vi (behavior / 동작)/defaults cho 7.0. dự án (project / 프로젝트) đang ở 5.x nên coi 6.0 là di chuyển (migration / 마이그레이션) checkpoint: xử lý deprecation, tường minh (explicit / 명시적) hóa cấu hình (config / 설정) và kiểm tra mô-đun (module / 모듈)/gói (package / 패키지) hành vi (behavior / 동작) trước khi đổi trình biên dịch (compiler / 컴파일러) generation.

### 6.1 Default changes: implicit giả định (assumption / 가정) trở thành di chuyển (migration / 마이그레이션) surface

Các default đáng chú ý gồm:

| Option/hành vi (behavior / 동작) | TypeScript 6.0 default/hành vi (behavior / 동작) | di chuyển (migration / 마이그레이션) consequence |
|---|---|---|
| `strict` | `true` | legacy dự án (project / 프로젝트) dựa vào non-strict có thể xuất hiện nhiều diagnostic |
| `module` | `esnext` | nguồn (source / 소스) không pin mô-đun (module / 모듈) có thể emit/mô hình (model / 모델) mô-đun (module / 모듈) khác trước |
| `target` | hiện tại (current / 현재) stable ES, tại 6.0 là `es2025` | đầu ra (output / 출력) có thể ít downlevel hơn; thời gian chạy (runtime / 런타임) hỗ trợ (support / 지원) phải được biết rõ |
| `noUncheckedSideEffectImports` | `true` | typo/unresolved side-effect import trở thành lỗi (error / 오류) |
| `rootDir` | directory chứa `tsconfig.json` | đầu ra (output / 출력) cây (tree / 트리) có thể đổi nếu trước đây dựa vào inferred dùng chung (common / 공통) nguồn (source / 소스) gốc (root / 루트) |
| `types` | `[]` | ambient globals từ mọi `@types` gói (package / 패키지) không còn tự động tràn vào dự án (project / 프로젝트) |
| `libReplacement` | `false` | giảm unnecessary resolution/watch công việc (work / 작업) nếu dự án (project / 프로젝트) không dùng custom lib replacement |

Điểm cần học không phải thuộc bảng. **trình biên dịch (compiler / 컴파일러) defaults là hidden phụ thuộc (dependency / 의존성).** môi trường vận hành (production / 운영 환경) dự án (project / 프로젝트) nên pin những option quyết định mô-đun (module / 모듈)/thời gian chạy (runtime / 런타임)/công khai (public / 공개) bản dựng (build / 빌드) đặc tả hợp đồng (contract / 계약), để upgrade trình biên dịch (compiler / 컴파일러) không vô tình đổi giả định (assumption / 가정).

### 6.2 Deprecated/removed surface: ecosystem các giả định (assumptions / 가정들) được dọn lại

6.0 deprecate `target: es5` và `downlevelIteration`; lowest hiện đại (modern / 현대적) đường dẫn (path / 경로) dịch về ES2015 trở lên. `moduleResolution: node`/`node10` bị deprecate; direct nút (node / 노드) app nên xem `nodenext`, còn bundled app/Bun thường xem `bundler` theo host thực tế.

Các mô-đun (module / 모듈) targets legacy như `amd`, `umd`, `systemjs`, `none` không còn là hướng được trình biên dịch (compiler / 컴파일러) hiện đại hỗ trợ (support / 지원). `baseUrl` bị deprecate như lookup-root cơ chế (mechanism / 메커니즘); `paths` từ lâu không cần `baseUrl`, và ánh xạ (mapping / 매핑) nên tường minh (explicit / 명시적) prefix thay vì vô tình làm bare specifier resolve vào nguồn (source / 소스) cây (tree / 트리).

`moduleResolution: classic` bị loại bỏ. `esModuleInterop: false` và `allowSyntheticDefaultImports: false` không còn là chế độ (mode / 모드) được giữ; `outFile` bị loại bỏ để bundling thuộc trách nhiệm của bundler chuyên dụng. Legacy `module Foo {}` không gian tên (namespace / 네임스페이스) cú pháp (syntax / 문법) và import assertion cú pháp (syntax / 문법) cũ cũng cần migrate.

Đây là architectural cleanup, không phải stylistic cleanup: TypeScript đang thu hẹp số host mô hình (model / 모델)/trình biên dịch (compiler / 컴파일러) paths cần duy trì để bản địa (native / 네이티브) hiện thực (implementation / 구현) có hành vi (behavior / 동작) rõ và hiệu năng (performance / 성능) tốt hơn.

### 6.3 `stableTypeOrdering`: di chuyển (migration / 마이그레이션) công cụ (tool / 도구), không phải nghiệp vụ (business / 비즈니스) tính năng (feature / 기능)

Bản địa (native / 네이티브) trình biên dịch (compiler / 컴파일러) có thể encounter nội bộ (internal / 내부) types theo thứ tự (order / 순서) khác JavaScript trình biên dịch (compiler / 컴파일러). 6.0 cung cấp `stableTypeOrdering` để giảm khác biệt observable như declaration thứ tự (ordering / 순서) và giúp so sánh 6→7. Khi kiểm tra (audit / 감사) di chuyển (migration / 마이그레이션), nếu đầu ra (output / 출력) `.d.ts` diff chỉ vì thứ tự (ordering / 순서), cần phân biệt ngữ nghĩa (semantic / 의미적) API thay đổi (change / 변경) với deterministic biểu diễn (representation / 표현) thay đổi (change / 변경).

Một di chuyển (migration / 마이그레이션) đúng không nên làm:

```text
5.x → 7.0 → thấy hàng trăm error → thêm ignore/cast cho build xanh
```

Nên lập luận (reasoning / 추론):

```text
5.x
→ upgrade 6.0
→ bỏ deprecated config/behavior
→ pin effective assumptions
→ chạy typecheck + declaration + runtime/module tests
→ bật stableTypeOrdering khi cần so sánh output
→ ổn định consumer contracts
→ thử 7.0
```

6.0 vẫn giữ trình biên dịch (compiler / 컴파일러) API lineage của codebase cũ, trong khi 7.0 bản địa (native / 네이티브) kiến trúc (architecture / 아키텍처) không ship programmatic trình biên dịch (compiler / 컴파일러) API ở 7.0. công cụ (tool / 도구)/plugin phụ thuộc sâu vào trình biên dịch (compiler / 컴파일러) API vì thế cần được kiểm tra (audit / 감사) riêng với nguồn (source / 소스) ứng dụng (application / 애플리케이션).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **7. TypeScript 7.0: trình biên dịch (compiler / 컴파일러) generation thay đổi, kiểu (type / 타입) kiến thức (knowledge / 지식) không reset** tiếp nhận điểm tựa từ **6. TypeScript 6.0: chuyển tiếp (transition / 전이) bản phát hành (release / 릴리스), không phải “TypeScript 7 lite”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Vì sao upgrade TypeScript có thể tạo lỗi (error / 오류) dù thời gian chạy (runtime / 런타임) mã (code / 코드) “không đổi”?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. TypeScript 7.0: trình biên dịch (compiler / 컴파일러) generation thay đổi, kiểu (type / 타입) kiến thức (knowledge / 지식) không reset

TypeScript 7.0 stable từ 08/07/2026. Đây là bản địa (native / 네이티브) cổng (port / 포트) của trình biên dịch (compiler / 컴파일러) và ngôn ngữ (language / 언어) dịch vụ (service / 서비스) sang Go, sử dụng bản địa (native / 네이티브) thực thi (execution / 실행) và shared-memory parallelism. Type-checking lô-gic (logic / 논리) được cổng (port / 포트) có chủ đích để tương thích sát với TypeScript 6.0 thay vì thiết kế một hệ kiểu mới.

```text
TypeScript 6 → 7
language/type semantics: continuity
compiler architecture: major discontinuity
```

Do đó generic, conditional kiểu (type / 타입), narrowing, `satisfies`, `NoInfer` hay discriminated union không trở thành kiến thức “TypeScript cũ”. Thứ thay đổi mạnh là hiệu năng (performance / 성능) envelope, editor/language-service kiến trúc (architecture / 아키텍처), dự án (project / 프로젝트) bản dựng (build / 빌드) scheduling và tính tương thích (compatibility / 호환성) với tooling dựa vào trình biên dịch (compiler / 컴파일러) internals/API cũ.

### 7.1 Parallel checker không có nghĩa “càng nhiều worker càng tốt”

TypeScript 7 parallelize parsing, checking và emitting. Checker workers có thể duplicate một phần dùng chung (shared / 공유) công việc (work / 작업); tăng `--checkers` thường tăng thông lượng (throughput / 처리량) trên machine nhiều cốt lõi (core / 핵심) nhưng cũng tăng bộ nhớ (memory / 메모리). Default checker worker count là 4; CI runner ít CPU/RAM có thể tốt hơn với count thấp hơn.

Project-reference builds còn có `--builders`. Hai dimensions nhân nhau: `--checkers 4 --builders 4` có thể dẫn tới nhiều checker hoạt động đồng thời. Vì vậy tuning phải dựa trên wall-clock + peak RSS + CI tính đồng thời (concurrency / 동시성), không chỉ CPU utilization.

`--singleThreaded` hữu ích để gỡ lỗi (debug / 디버그) order-sensitive issue, so sánh TS6/TS7 hoặc khi outer hệ thống dựng (build system / 빌드 시스템) đã tự parallelize. Đây là môi trường vận hành (production / 운영 환경) hiệu năng (performance / 성능) lesson: parallelism có nhiều tầng (layer / 계층), và nested parallelism có thể làm hệ thống chậm hơn do contention.

### 7.2 Watch chế độ (mode / 모드) là một môi trường vận hành (production / 운영 환경) công cụ (tool / 도구), không chỉ editor convenience

7.0 rebuild `--watch` trên file-watching foundation mới. Large monorepo cần quan sát CPU, tệp (file / 파일) descriptor/tài nguyên (resource / 자원) usage, vô hiệu hóa (invalidation / 무효화) breadth và generated-file churn. Nếu một codegen tiến trình (process / 프로세스) liên tục chạm hàng nghìn tệp (file / 파일), trình biên dịch (compiler / 컴파일러) nhanh hơn vẫn có thể bị dự án (project / 프로젝트) đồ thị (graph / 그래프) vô hiệu hóa (invalidation / 무효화) áp đảo.

### 7.3 7.0 chưa ship trình biên dịch (compiler / 컴파일러) API: nguồn (source / 소스) tính tương thích (compatibility / 호환성) khác tooling tính tương thích (compatibility / 호환성)

TypeScript 7.0 không ship programmatic trình biên dịch (compiler / 컴파일러) API tương đương 6.0; API mới được dự kiến ở generation sau. Vì vậy ứng dụng (application / 애플리케이션) nguồn (source / 소스) có thể typecheck hoàn hảo bằng 7.0 trong khi ESLint plugin, transformer, codegen hoặc custom language-service tích hợp (integration / 통합) vẫn cần TypeScript 6 API.

TypeScript nhóm (team / 팀) cung cấp `@typescript/typescript6`/`tsc6` để chạy side-by-side. mô hình tư duy (mental model / 사고 모델) là:

```text
application typecheck/build → TS7 native tsc
legacy compiler-API consumer → TS6 compatibility package
```

Đây không phải workaround đáng xấu hổ; nó là di chuyển (migration / 마이그레이션) kiến trúc (architecture / 아키텍처) chính thức khi ecosystem chưa chuyển đồng thời.

### 7.4 tính tương thích (compatibility / 호환성) đặc tả hợp đồng (contract / 계약) 6 → 7

TypeScript nhóm (team / 팀) đặt mục tiêu mã (code / 코드) compile sạch ở 6.0 với `stableTypeOrdering` và không dựa vào `ignoreDeprecations` sẽ compile tương đương ở 7.0. Vì thế deprecation ở 6.0 phải được xem như **future hard ranh giới (boundary / 경계)**, không phải warning có thể để vô thời hạn.

7.0 nhận các default/cleanup đã được chuẩn bị từ 6.0. cấp cao (senior / 시니어) quy tắc (rule / 규칙) là **pin các giả định (assumptions / 가정들)**: môi trường vận hành (production / 운영 환경) `tsconfig` quan trọng nên tường minh (explicit / 명시적) những option quyết định thời gian chạy (runtime / 런타임)/mô-đun (module / 모듈) đặc tả hợp đồng (contract / 계약) thay vì dựa vào default chỉ vì default hiện tại phù hợp.

> **Chuyển mạch:** Trong **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **8. Vì sao upgrade TypeScript có thể tạo lỗi (error / 오류) dù thời gian chạy (runtime / 런타임) mã (code / 코드) “không đổi”?** tiếp nhận điểm tựa từ **7. TypeScript 7.0: trình biên dịch (compiler / 컴파일러) generation thay đổi, kiểu (type / 타입) kiến thức (knowledge / 지식) không reset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) của thư viện (library / 라이브러리) khác ứng dụng (application / 애플리케이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Vì sao upgrade TypeScript có thể tạo lỗi (error / 오류) dù thời gian chạy (runtime / 런타임) mã (code / 코드) “không đổi”?

Có năm nguồn phổ biến.

Thứ nhất là suy luận (inference / 추론)/tính đúng đắn (correctness / 정확성) fix. Checker mới có thể suy ra kiểu (type / 타입) chính xác hơn, khiến mã (code / 코드) từng compile nhờ kiểu (type / 타입) rộng hoặc unsound trường hợp biên (edge case / 경계 사례) bắt đầu thất bại (fail / 실패). Đây không nhất thiết là regression.

Thứ hai là `lib.d.ts`/DOM types thay đổi theo nền tảng (platform / 플랫폼) standards. ứng dụng (application / 애플리케이션) mã (code / 코드) không đổi nhưng ambient nền tảng (platform / 플랫폼) đặc tả hợp đồng (contract / 계약) đổi.

Thứ ba là mô-đun (module / 모듈) resolution/cấu hình (config / 설정) defaults thay đổi. Type-check pass/thất bại (fail / 실패) có thể khác vì trình biên dịch (compiler / 컴파일러) mô hình (model / 모델) gói (package / 패키지) `exports`, extension hoặc host điều kiện (condition / 조건) khác.

Thứ tư là declaration ecosystem. phụ thuộc (dependency / 의존성) cập nhật (update / 업데이트) hoặc TypeScript phiên bản (version / 버전) mới có thể parse/check `.d.ts` khác, dù JavaScript phụ thuộc (dependency / 의존성) thời gian chạy (runtime / 런타임) vẫn giống trước.

Thứ năm là bản dựng (build / 빌드) orchestration/tooling. dự án (project / 프로젝트) references, watch vô hiệu hóa (invalidation / 무효화), declaration thứ tự (ordering / 순서) hoặc trình biên dịch (compiler / 컴파일러) API tích hợp (integration / 통합) có thể đổi mà nguồn (source / 소스) ngữ nghĩa (semantics / 의미론) vẫn tương đương.

Vì vậy di chuyển (migration / 마이그레이션) bug report nên ghi rõ ít nhất:

```text
old TS version / new TS version
old tsconfig / effective new tsconfig
runtime + bundler version
module/package mode
exact diagnostic
whether JS emit changed
whether .d.ts emit changed
whether runtime test changed
whether tooling imports TypeScript compiler API
```

> **Chuyển mạch:** Ở chặng này của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **9. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) của thư viện (library / 라이브러리) khác ứng dụng (application / 애플리케이션)** tiếp nhận điểm tựa từ **8. Vì sao upgrade TypeScript có thể tạo lỗi (error / 오류) dù thời gian chạy (runtime / 런타임) mã (code / 코드) “không đổi”?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. di chuyển (migration / 마이그레이션) playbook từ 5.x/6.x lên 7.0** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) của thư viện (library / 라이브러리) khác ứng dụng (application / 애플리케이션)

Ứng dụng (application / 애플리케이션) có thể pin một TypeScript phiên bản (version / 버전) và trình biên dịch (compiler / 컴파일러) cấu hình (config / 설정). thư viện (library / 라이브러리) publish ra ecosystem phải sống với nhiều bên tiêu thụ (consumer / 소비자) versions và nhiều mô-đun (module / 모듈) hosts.

Nếu công khai (public / 공개) `.d.ts` dùng cú pháp (syntax / 문법)/kiểu (type / 타입) tính năng (feature / 기능) mới, minimum TypeScript phiên bản (version / 버전) của bên tiêu thụ (consumer / 소비자) tăng ngay cả khi JavaScript thời gian chạy (runtime / 런타임) đầu ra (output / 출력) vẫn tương thích trình duyệt (browser / 브라우저) cũ. Đây là **type-level breaking tính tương thích (compatibility / 호환성)**.

Thư viện (library / 라이브러리) author nên kiểm thử (test / 테스트) ít nhất ba surfaces:

```text
runtime artifact
public declaration artifact
consumer compilation
```

Tốt hơn nữa, bên tiêu thụ (consumer / 소비자) fixture nên có ít nhất một dự án (project / 프로젝트) `nodenext` và một dự án (project / 프로젝트) `bundler` nếu gói (package / 패키지) claim hỗ trợ (support / 지원) cả nút (node / 노드) direct consumption lẫn bundler ecosystem. gói (package / 패키지) có thể “works in Vite” nhưng `.d.ts` hoặc `exports` thất bại (fail / 실패) trong nút (node / 노드) bên tiêu thụ (consumer / 소비자).

Nếu gói (package / 패키지) hỗ trợ nhiều TypeScript generation, `typesVersions` hoặc versioned `types` conditions có thể cần thiết. Nhưng mỗi tính tương thích (compatibility / 호환성) branch là maintenance chi phí (cost / 비용); đừng hỗ trợ (support / 지원) trình biên dịch (compiler / 컴파일러) quá cũ chỉ bằng một claim trong README mà không có bên tiêu thụ (consumer / 소비자) fixture.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **10. di chuyển (migration / 마이그레이션) playbook từ 5.x/6.x lên 7.0** tiếp nhận điểm tựa từ **9. phiên bản (version / 버전) tính tương thích (compatibility / 호환성) của thư viện (library / 라이브러리) khác ứng dụng (application / 애플리케이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Worked di chuyển (migration / 마이그레이션) example: gói (package / 패키지) từ TS 5.4 lên TS 7** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. di chuyển (migration / 마이그레이션) playbook từ 5.x/6.x lên 7.0

### Bước 1 — ghi lại baseline trước upgrade

Chạy typecheck/bản dựng (build / 빌드)/kiểm thử (test / 테스트) hiện tại và lưu effective cấu hình (config / 설정). Với codebase lớn, đo cold check, incremental check, editor độ trễ (latency / 지연 시간) và bộ nhớ (memory / 메모리) để có bằng chứng (evidence / 증거) so sánh.

### Bước 2 — tách ứng dụng (application / 애플리케이션) nguồn (source / 소스) khỏi tooling phụ thuộc (dependency / 의존성)

Tìm kiếm (search / 검색) các gói (package / 패키지)/plugin có import từ `typescript`, custom transformer, language-service plugin hoặc trình biên dịch (compiler / 컴파일러) API tích hợp (integration / 통합). nguồn (source / 소스) `.ts` có thể migrate dễ nhưng tooling này có tính tương thích (compatibility / 호환성) story khác với bản địa (native / 네이티브) 7.0.

### Bước 3 — đi qua 6.0 nếu dự án (project / 프로젝트) còn ở 5.x

Xử lý deprecation và cấu hình (config / 설정) các giả định (assumptions / 가정들) ở 6.0 trước. Không dùng `ignoreDeprecations` như trạng thái cuối; nó chỉ trì hoãn công việc (work / 작업) mà 7.0 biến thành hard incompatibility.

### Bước 4 — snapshot effective cấu hình (config / 설정), không chỉ nguồn (source / 소스) `tsconfig`

Dùng `tsc --showConfig` hoặc equivalent tooling để biết cấu hình (config / 설정) sau `extends`, defaults và inherited settings. di chuyển (migration / 마이그레이션) rà soát (review / 검토) dựa vào tệp (file / 파일) `tsconfig.json` thô có thể bỏ sót giả định (assumption / 가정) đến từ cơ sở (base / 기반) cấu hình (config / 설정)/gói (package / 패키지) preset.

### Bước 5 — kiểm tra ranh giới mô-đun (module boundary / 모듈 경계) bằng thời gian chạy (runtime / 런타임) thật

Typecheck không đủ. Chạy nút (node / 노드)/trình duyệt (browser / 브라우저)/bundler tests, gói (package / 패키지) bên tiêu thụ (consumer / 소비자) fixtures và SSR/bản dựng (build / 빌드) đường dẫn (path / 경로) thật. Đặc biệt kiểm tra ESM/CJS, gói (package / 패키지) `exports`, tệp (file / 파일) extensions, side-effect imports và đường dẫn (path / 경로) aliases.

### Bước 6 — diff declaration đầu ra (output / 출력)

Nếu dự án (project / 프로젝트) publish gói (package / 패키지), diff `.d.ts`. Một upgrade trình biên dịch (compiler / 컴파일러) có thể làm declaration surface thay đổi do suy luận (inference / 추론)/emit improvements dù thời gian chạy (runtime / 런타임) JavaScript gần như không đổi. Phân biệt ngữ nghĩa (semantic / 의미적) diff với ordering-only diff.

### Bước 7 — phân loại diagnostic thay vì suppress hàng loạt

Mỗi lỗi (error / 오류) mới nên thuộc một nhóm: real bug được checker mới bắt, suy luận (inference / 추론) hành vi (behavior / 동작) thay đổi (change / 변경), declaration phụ thuộc (dependency / 의존성) incompatibility, cấu hình (config / 설정)/mô-đun (module / 모듈) mismatch hoặc tooling incompatibility. Chỉ sau khi biết category mới chọn fix.

### Bước 8 — chạy dual trình biên dịch (compiler / 컴파일러) khi di chuyển (migration / 마이그레이션) lớn

Trong giai đoạn 6→7, có thể chạy TS6 và TS7 song song trên CI để so diagnostic/declaration đầu ra (output / 출력) trước khi cut over. Với tooling cần trình biên dịch (compiler / 컴파일러) API, giữ TS6 tính tương thích (compatibility / 호환성) gói (package / 패키지) trong khi ứng dụng (application / 애플리케이션) bản dựng (build / 빌드) chuyển sang TS7.

### Bước 9 — đo hiệu năng (performance / 성능) sau khi tính đúng đắn (correctness / 정확성) ổn

TypeScript 7 thường nhanh hơn đáng kể nhờ bản địa (native / 네이티브) kiến trúc (architecture / 아키텍처) và parallelism, nhưng benchmark phải trên repository thật. Generated types, giant unions, recursive conditional types và dự án (project / 프로젝트) đồ thị (graph / 그래프) xấu vẫn có thể tạo hotspot. Ghi cả wall-clock, CPU và peak bộ nhớ (memory / 메모리); speedup làm CI OOM không phải improvement.

> **Chuyển mạch:** Trong **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **10. di chuyển (migration / 마이그레이션) playbook từ 5.x/6.x lên 7.0** cho ta quy tắc; **11. Worked di chuyển (migration / 마이그레이션) example: gói (package / 패키지) từ TS 5.4 lên TS 7** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **12. Khi đọc mã (code / 코드) cũ, phiên bản (version / 버전) clue nói gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Worked di chuyển (migration / 마이그레이션) example: gói (package / 패키지) từ TS 5.4 lên TS 7

Giả sử một gói (package / 패키지) thư viện (library / 라이브러리) đang ở 5.4, dùng `moduleResolution: node`, `baseUrl`, side-effect CSS import, publish `.d.ts`, và một custom script import `typescript` trình biên dịch (compiler / 컴파일러) API.

Nếu nhảy thẳng lên 7.0, nhóm (team / 팀) có thể gặp module-resolution errors, missing ambient types, cấu hình (config / 설정) hard errors và custom script không chạy. Cách lập luận (reasoning / 추론) tốt hơn là tách di chuyển (migration / 마이그레이션) thành các independent boundaries.

Đầu tiên nâng lên latest 5.x để bắt suy luận (inference / 추론)/mô-đun (module / 모듈) hành vi (behavior / 동작) mới mà chưa đổi trình biên dịch (compiler / 컴파일러) generation. Sau đó sang 6.0, thay `node` bằng host-appropriate resolver, bỏ phụ thuộc (dependency / 의존성) vào `baseUrl`, khai báo asset ambient mô-đun (module / 모듈) nếu cần, pin `types` và `rootDir`, xử lý deprecation. Chạy thời gian chạy (runtime / 런타임) bên tiêu thụ (consumer / 소비자) fixtures và diff `.d.ts`.

Tiếp theo bật `stableTypeOrdering` để so declaration với TS7. Custom script dùng trình biên dịch (compiler / 컴파일러) API được giữ trên `@typescript/typescript6`, trong khi gói (package / 패키지) typecheck/bản dựng (build / 빌드) thử bằng TS7. Sau khi tính đúng đắn (correctness / 정확성) ổn mới benchmark `--checkers`/`--builders` theo CI machine.

Điểm quan trọng là không có “một lỗi upgrade TypeScript”. Có nhiều ranh giới (boundary / 경계) độc lập được trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) mới làm lộ ra.

> **Chuyển mạch:** Ở chặng này của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **11. Worked di chuyển (migration / 마이그레이션) example: gói (package / 패키지) từ TS 5.4 lên TS 7** cho ta quy tắc; **12. Khi đọc mã (code / 코드) cũ, phiên bản (version / 버전) clue nói gì?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **13. Khi nào nên dùng tính năng (feature / 기능) mới?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Khi đọc mã (code / 코드) cũ, phiên bản (version / 버전) clue nói gì?

Nếu thấy `namespace` lớn và triple-slash references, mã (code / 코드) có thể đến từ thời pre-ESM TypeScript hoặc từ thư viện (library / 라이브러리) cần ambient tích hợp (integration / 통합). Nếu thấy `importsNotUsedAsValues`/`preserveValueImports`, đó là module-emit cấu hình (configuration / 구성) trước `verbatimModuleSyntax`. Nếu thấy decorator dựa vào `experimentalDecorators` + `emitDecoratorMetadata`, đừng tự động chuyển sang tiêu chuẩn (standard / 표준) decorators. Nếu thấy nhiều overload chỉ để giữ tuple positions, có thể mã (code / 코드) được viết trước variadic tuple types. Nếu thấy helper guard thủ công quanh `.filter`, mã (code / 코드) có thể predates inferred kiểu (type / 타입) predicates hoặc cần hành vi (behavior / 동작) mà suy luận (inference / 추론) không đủ.

Nếu thấy `moduleResolution: node`, `target: es5`, `outFile`, `baseUrl` như lookup gốc (root / 루트) hoặc AMD/UMD đầu ra (output / 출력), đó là dấu hiệu di chuyển (migration / 마이그레이션) tới 6/7 cần kiểm tra (audit / 감사) host các giả định (assumptions / 가정들) chứ không chỉ đổi phiên bản (version / 버전) trong `package.json`.

Phiên bản (version / 버전) archaeology không nhằm rewrite cho “mới”. Nó giúp hiểu **ràng buộc (constraint / 제약조건) lịch sử nào đã tạo ra thiết kế (design / 설계) hiện tại**, rồi quyết định ràng buộc (constraint / 제약조건) đó còn tồn tại không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **13. Khi nào nên dùng tính năng (feature / 기능) mới?** tiếp nhận điểm tựa từ **12. Khi đọc mã (code / 코드) cũ, phiên bản (version / 버전) clue nói gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. phiên bản (version / 버전) chính sách (policy / 정책) cho môi trường vận hành (production / 운영 환경) repository** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Khi nào nên dùng tính năng (feature / 기능) mới?

Tính năng (feature / 기능) mới đáng adoption khi nó loại một lớp (class / 클래스) bug, làm đặc tả hợp đồng (contract / 계약) rõ hơn hoặc giảm độ phức tạp (complexity / 복잡도) mà không tăng tính tương thích (compatibility / 호환성) chi phí (cost / 비용) quá mức. `satisfies` thường có ROI cao cho cấu hình (config / 설정). `NoInfer` hữu ích trong API generic có suy luận (inference / 추론) direction rõ. `isolatedDeclarations` đáng cân nhắc khi monorepo/bản dựng (build / 빌드) kiến trúc (architecture / 아키텍처) thực sự hưởng lợi. `erasableSyntaxOnly` phù hợp khi thời gian chạy (runtime / 런타임) chiến lược (strategy / 전략) là direct kiểu (type / 타입) stripping.

Không nên adoption chỉ vì trình biên dịch (compiler / 컴파일러) hỗ trợ. Nếu gói (package / 패키지) phải hỗ trợ (support / 지원) bên tiêu thụ (consumer / 소비자) TypeScript cũ, công khai (public / 공개) kiểu (type / 타입) cú pháp (syntax / 문법) mới có thể phá downstream. Nếu nhóm (team / 팀) chưa dùng direct `.ts` thời gian chạy (runtime / 런타임), bật ràng buộc (constraint / 제약조건) phục vụ kiểu (type / 타입) stripping có thể chỉ tăng friction. Version-aware kỹ thuật (engineering / 엔지니어링) là chọn tính năng (feature / 기능) theo hệ thống (system / 시스템) ràng buộc (constraint / 제약조건), không theo release-note excitement.

> **Chuyển mạch:** Trong **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **14. phiên bản (version / 버전) chính sách (policy / 정책) cho môi trường vận hành (production / 운영 환경) repository** tiếp nhận điểm tựa từ **13. Khi nào nên dùng tính năng (feature / 기능) mới?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Checklist lập luận (reasoning / 추론) khi nâng phiên bản (version / 버전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. phiên bản (version / 버전) chính sách (policy / 정책) cho môi trường vận hành (production / 운영 환경) repository

Một repository nên pin TypeScript bằng lockfile và package-manager chính sách (policy / 정책), không dựa vào toàn cục (global / 전역) `tsc`. CI nên in `tsc --version` trong diagnostic ngữ cảnh (context / 맥락) khi bản dựng (build / 빌드) thất bại (failure / 실패) cần điều tra.

Ứng dụng (application / 애플리케이션) có thể upgrade trình biên dịch (compiler / 컴파일러) nhanh hơn thư viện (library / 라이브러리) vì không phải hỗ trợ (support / 지원) downstream trình biên dịch (compiler / 컴파일러). thư viện (library / 라이브러리) nên công bố minimum supported TypeScript phiên bản (version / 버전) nếu công khai (public / 공개) declarations phụ thuộc tính năng (feature / 기능) mới và nên kiểm thử (test / 테스트) minimum đó trong CI nếu claim tính tương thích (compatibility / 호환성) thực sự quan trọng.

Không nên coi `skipLibCheck` là version-compatibility chiến lược (strategy / 전략). Nó có thể giảm noise/bản dựng (build / 빌드) chi phí (cost / 비용) trong một số dự án (project / 프로젝트), nhưng cũng có thể che declaration incompatibility giữa dependencies. Khi upgrade trình biên dịch (compiler / 컴파일러), nếu chỉ bản dựng (build / 빌드) xanh khi bật `skipLibCheck`, cần xác định chính xác declaration nào đang xung đột (conflict / 충돌) trước khi chấp nhận sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **15. Checklist lập luận (reasoning / 추론) khi nâng phiên bản (version / 버전)** tiếp nhận điểm tựa từ **14. phiên bản (version / 버전) chính sách (policy / 정책) cho môi trường vận hành (production / 운영 환경) repository** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Cross-links trong chuẩn gốc (canonical / 정본) nhánh học (track / 트랙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Checklist lập luận (reasoning / 추론) khi nâng phiên bản (version / 버전)

Trước khi merge upgrade, reviewer phải trả lời được: trình biên dịch (compiler / 컴파일러) phiên bản (version / 버전) đổi từ đâu sang đâu; bản phát hành (release / 릴리스) nào ở giữa có deprecation/breaking hành vi (behavior / 동작); effective `tsconfig` thay đổi gì; mô-đun (module / 모듈) resolver đang mô hình (model / 모델) nút (node / 노드) hay bundler; JavaScript emit có diff không; declaration emit có diff không; phụ thuộc (dependency / 의존성) `.d.ts` có yêu cầu minimum TS mới không; trình biên dịch (compiler / 컴파일러) API/plugin nào bị ảnh hưởng; thời gian chạy (runtime / 런타임)/bên tiêu thụ (consumer / 소비자) fixture đã chạy chưa; và hiệu năng (performance / 성능) đo lường (measurement / 측정) có so với baseline không.

Nếu không trả lời được các câu trên, “CI xanh” chỉ chứng minh kiểm thử (test / 테스트) hiện có chưa thấy lỗi, không chứng minh di chuyển (migration / 마이그레이션) ranh giới (boundary / 경계) đã được hiểu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, sau nội dung của **15. Checklist lập luận (reasoning / 추론) khi nâng phiên bản (version / 버전)**, **16. Cross-links trong chuẩn gốc (canonical / 정본) nhánh học (track / 트랙)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **17. Nguồn chuẩn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Cross-links trong chuẩn gốc (canonical / 정본) nhánh học (track / 트랙)

Để hiểu tính năng (feature / 기능) theo bản chất thay vì theo timeline, quay lại [Type System Internals](typescript_02_type_system.md) cho suy luận (inference / 추론), predicate, `NoInfer`, tuple và type-level độ phức tạp (complexity / 복잡도); đọc [Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md) cho mô-đun (module / 모듈) resolution, declaration, direct-TypeScript thời gian chạy (runtime / 런타임), dự án (project / 프로젝트) đồ thị (graph / 그래프) và TypeScript 7 internals; đọc [Senior Production Engineering](typescript_04_senior_production.md) cho di chuyển (migration / 마이그레이션), thư viện (library / 라이브러리) tính tương thích (compatibility / 호환성), thời gian chạy (runtime / 런타임) kiểm tra hợp lệ (validation / 검증) và bằng chứng vận hành (production evidence / 운영 증거).

Phiên bản (version / 버전) guide này chỉ trả lời câu hỏi **“kiến thức (knowledge / 지식) đó xuất hiện/thay đổi qua các bản phát hành (release / 릴리스) như thế nào và di chuyển (migration / 마이그레이션) consequence là gì?”**. Nó không duplicate giải thích đầy đủ của các chuẩn gốc (canonical / 정본) chapter kia.

> **Chuyển mạch:** Trong **TypeScript 05 — phiên bản (version / 버전) Evolution & di chuyển (migration / 마이그레이션)**, **16. Cross-links trong chuẩn gốc (canonical / 정본) nhánh học (track / 트랙)** nêu điều cần giải thích; **17. Nguồn chuẩn** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 17. Nguồn chuẩn

Phiên bản (version / 버전) facts trong chapter này ưu tiên tài liệu chính thức của TypeScript nhóm (team / 팀):

- TypeScript Handbook — bản phát hành (release / 릴리스) Notes: `https://www.typescriptlang.org/docs/handbook/release-notes/`
- TSConfig tham chiếu (reference / 참조): `https://www.typescriptlang.org/tsconfig/`
- Announcing TypeScript 6.0: `https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/`
- Announcing TypeScript 7.0: `https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/`

Khi bản phát hành (release / 릴리스) mới xuất hiện, không append mọi tính năng (feature / 기능) vào đây. Chỉ thêm tính năng (feature / 기능) nếu nó thay đổi mô hình tư duy (mental model / 사고 모델), di chuyển (migration / 마이그레이션) hành vi (behavior / 동작), trình biên dịch (compiler / 컴파일러)/tooling kiến trúc (architecture / 아키텍처), thời gian chạy (runtime / 런타임)/mô-đun (module / 모듈) đặc tả hợp đồng (contract / 계약) hoặc tính tương thích (compatibility / 호환성) surface.

---

Tiếp theo: quay lại [TypeScript Index](typescript_00_index.md) hoặc dùng chapter này như di chuyển (migration / 마이그레이션) map khi đọc codebase ở phiên bản (version / 버전) cũ.

> **Bàn giao:** Sau **17. Nguồn chuẩn**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
