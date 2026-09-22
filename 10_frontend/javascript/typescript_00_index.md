# TypeScript — Canonical Knowledge Track

TypeScript trong repository này **không phải một library độc lập tách khỏi JavaScript**. Nó là track canonical nằm ngay trong `10_frontend/javascript/` vì mọi TypeScript program cuối cùng vẫn phải sống trên semantics và runtime của JavaScript. Cách tổ chức này cố ý giữ ranh giới rõ: JavaScript giải thích runtime, execution model, object model, async/event loop và browser/Node behavior; TypeScript giải thích lớp kiểm tra kiểu tĩnh, compiler/tooling và cách mô hình hóa contract trước khi code chạy.

Baseline hiện hành của track này là **TypeScript 7.0**, stable từ ngày 08/07/2026. TypeScript 7 chuyển compiler và language service sang native implementation bằng Go, dùng shared-memory multithreading và tập trung mạnh vào build/editor performance. Về semantics kiểm tra kiểu, 7.0 chủ đích tương thích rất sát với 6.0; vì vậy cần hiểu TypeScript 6.0 như release cầu nối, rồi mới hiểu tại sao 7.0 thay đổi toolchain nhưng không làm những mental model nền tảng như structural typing, narrowing hay generic trở nên lỗi thời.

## Conceptual boundary

TypeScript không “thay JavaScript bằng một ngôn ngữ khác”. Nó thêm một static analysis layer lên syntax và semantics JavaScript, sau đó phần lớn thông tin type bị xóa trước runtime. Vì vậy một lỗi có thể thuộc bốn lớp khác nhau: JavaScript runtime semantics, TypeScript type model, module/build tooling, hoặc framework/library declarations. Track này luôn cố tách bốn lớp đó thay vì gom mọi lỗi `.ts` thành “lỗi TypeScript”.

Nếu chưa chắc về JavaScript runtime, hãy quay lại [JavaScript Beginner](javascript_beginner_rebuilt.md) và [JavaScript Intermediate](javascript_intermediate.md). Khi cần internals, performance, browser/runtime production behavior, đọc tiếp [JavaScript Senior](javascript_senior.md) và [JavaScript Master](javascript_master_supplement_detailed.md). Sau TypeScript, track React nằm tại [React Index](../react/00_index.md).

## Thứ tự học canonical

1. [01 — Foundations & Runtime Boundary](typescript_01_foundations.md) giải thích TypeScript là gì, type erasure, inference, annotation, `unknown`/`any`/`never`, union/intersection, object/function types, narrowing, discriminated union, `satisfies`, assertion và các failure mode cơ bản.
2. [02 — Type System Internals & Generic Modeling](typescript_02_type_system.md) đào sâu structural typing, assignability, variance, generic constraints/inference, `keyof`, indexed access, mapped/conditional types, `infer`, template literal types, recursive types và cách API design ảnh hưởng compiler complexity.
3. [03 — Compiler, Modules & Tooling](typescript_03_tooling_modules_runtime.md) giải thích `tsconfig`, `target`/`lib`, module/module resolution, ESM/CJS, declaration files, emit pipeline, bundler, project references, monorepo, TypeScript 6 → 7 migration và debugging compiler/tooling.
4. [04 — Senior Production Engineering](typescript_04_senior_production.md) đưa type model vào boundary thật: API payload, runtime validation, domain modeling, React/Node, library authoring, security, performance, migration legacy JavaScript và production diagnostics.

Luồng reasoning xuyên suốt là **JavaScript value/runtime → TypeScript model → compiler proof/diagnostic → emitted/runtime code → production evidence**. Nếu một type trick làm code “thông minh hơn” nhưng che khuất runtime behavior hoặc tạo compiler cost không đáng có, track này ưu tiên code dễ reasoning hơn.

## Mental model cốt lõi

TypeScript cố chứng minh một số thuộc tính của chương trình **trước runtime** dựa trên source code và declaration information mà compiler nhìn thấy. Nó không quan sát database thật, HTTP response thật hay user input thật. Do đó type safety chỉ mạnh bằng contract và evidence bạn cung cấp. `fetch(...).json()` đến từ bên ngoài trust boundary; cast dữ liệu thành `User` không làm dữ liệu trở thành `User`. Validation runtime và TypeScript phục vụ hai tầng khác nhau nhưng bổ trợ nhau.

TypeScript cũng không hướng tới một hệ kiểu sound tuyệt đối theo nghĩa học thuật. Nó cố cân bằng correctness, compatibility với JavaScript và developer ergonomics. Vì JavaScript cho phép nhiều pattern động, TypeScript có những escape hatch như `any`, assertion, non-null assertion, declaration merging và một số assignment rules mang tính thực dụng. Senior developer cần biết compiler đang bảo đảm điều gì, không bảo đảm điều gì và chỗ nào chính mình đã “tắt bằng chứng”.

## Version evolution nên hiểu

TypeScript 1.x đặt nền với annotation, interface, class và generic. TypeScript 2.x làm hệ kiểu trưởng thành hơn với control-flow based analysis, `strictNullChecks`, mapped types và conditional types ở các mốc khác nhau trong nhánh 2.x. TypeScript 3.x bổ sung `unknown`, project references và optional chaining/nullish coalescing ở giai đoạn cuối 3.x. TypeScript 4.x phát triển mạnh type-level programming với variadic tuple, template literal types, nhiều cải tiến inference và `satisfies` ở 4.9. TypeScript 5.x hiện đại hóa decorator semantics, module options và generic ergonomics. TypeScript 6.0 thay đổi nhiều default/deprecation để chuẩn bị cho native compiler. TypeScript 7.0 là bước chuyển kiến trúc compiler lớn nhất: native Go implementation, LSP-oriented editor integration và build performance cao hơn đáng kể, trong khi cố giữ type-checking behavior tương thích với 6.0.

Một consequence thực tế là khi đọc bài cũ, phải tách **language feature** khỏi **compiler/toolchain generation**. `satisfies`, conditional type hay discriminated union vẫn là kiến thức type-system; native compiler 7.0 chủ yếu thay đổi cách tool chạy và scale chứ không làm những concept đó thành legacy.

## Thuật ngữ chính

| Tiếng Việt | English term | 한국어 용어 | Ý nghĩa ngắn |
|---|---|---|---|
| kiểm tra kiểu tĩnh | static type checking | 정적 타입 검사 | Phân tích type trước runtime. |
| suy luận kiểu | type inference | 타입 추론 | Compiler suy ra type từ expression/context thay vì buộc viết annotation. |
| thu hẹp kiểu | type narrowing | 타입 좁히기 | Dùng control flow/evidence để giảm tập type khả dĩ. |
| kiểu cấu trúc | structural typing | 구조적 타이핑 | Compatibility dựa chủ yếu trên shape/capabilities thay vì tên class/type. |
| khả năng gán | assignability | 할당 가능성 | Quy tắc quyết định value/type A có thể dùng ở vị trí cần B hay không. |
| kiểu hợp | union type | 유니온 타입 | Value có thể thuộc một trong nhiều type. |
| kiểu giao | intersection type | 인터섹션 타입 | Kết hợp yêu cầu của nhiều type vào cùng value. |
| tham số kiểu | type parameter | 타입 매개변수 | “Biến” ở tầng type dùng cho generic abstraction. |
| phương sai | variance | 변성 | Quan hệ giữa `Container<A>` và `Container<B>` khi `A`/`B` có quan hệ subtype/assignability. |
| file khai báo | declaration file | 선언 파일 | `.d.ts` mô tả public type surface mà không cung cấp runtime implementation. |
| xóa kiểu | type erasure | 타입 소거 | Type syntax/info không còn tồn tại như runtime check sau emit trong đa số trường hợp. |

## Coverage audit

Track này coi coverage đủ khi người đọc có thể giải thích được: tại sao TypeScript không validate dữ liệu runtime; vì sao structural typing vừa mạnh vừa có edge case; compiler narrow union bằng evidence nào; generic inference lấy constraint từ đâu; conditional type phân phối khi nào; `infer` đang capture cấu trúc gì; `tsconfig` nào thay đổi type-checking và option nào chỉ thay emit/module behavior; vì sao `paths` không tự rewrite runtime imports; `.d.ts` là contract chứ không phải implementation; ESM/CJS khác nhau ở đâu; TypeScript 7.0 thay đổi compiler architecture như thế nào; và phải quan sát bằng diagnostic nào khi build chậm hoặc module resolution sai.

Không tạo chapter riêng chỉ để liệt kê syntax mới. Feature mới chỉ được thêm khi nó thay đổi mental model, migration behavior hoặc production practice.

## Nguồn chuẩn để đối chiếu version

- TypeScript Handbook và release notes trên `typescriptlang.org`.
- TypeScript Team blog trên `devblogs.microsoft.com/typescript/`.
- ECMAScript/JavaScript runtime semantics được giữ ở JavaScript canonical docs của repository này.

Track được audit lại theo trạng thái TypeScript 7.0, tháng 09/2026.
