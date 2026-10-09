# Frontend — source ledger và browser/framework version boundary

> **Owner:** `10_frontend/` (canonical frontend content). Ledger này phân biệt web-platform standards, browser behavior, framework/tool semantics và sản phẩm build/deploy.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| FE-WHATWG-01 | WHATWG | HTML, DOM, URL và browser platform living standards | https://html.spec.whatwg.org/ | living standard; kiểm tra 2026-10-09 | Spec có thể thay đổi; ghi section/commit/date khi claim behavior, không coi spec là behavior của mọi browser cũ | `html/`, `javascript/`, web platform |
| FE-CSSWG-01 | W3C CSS Working Group | CSS specifications and drafts | https://drafts.csswg.org/ | draft/CR/REC status phải ghi | Draft không phải guarantee triển khai; ghi browser support/test evidence cho production claim | `css/`, `scss/`, `tailwind/` |
| FE-ECMA-01 | Ecma TC39 | ECMAScript language semantics | https://tc39.es/ecma262/ | living spec; kiểm tra 2026-10-09 | Language spec tách khỏi host/browser APIs; ghi edition/section khi cần, không suy browser support chỉ từ syntax | `javascript/` |
| FE-WCAG-01 | W3C Web Accessibility Initiative | WCAG success criteria và conformance guidance | https://www.w3.org/TR/WCAG22/ | WCAG 2.2; kiểm tra 2026-10-09 | Conformance còn phụ thuộc content, user agent, assistive technology và test scope; không gọi checklist là accessibility proof | HTML/React/UI |
| FE-MDN-01 | MDN Web Docs | developer-facing explanations, compatibility và API examples | https://developer.mozilla.org/en-US/docs/Web | docs live; browser compatibility data có date riêng | MDN là secondary explanatory source; claim normative phải quay về spec/browser test | all web-platform tracks |
| FE-REACT-01 | React project | React API, rendering, effects, server/client và framework semantics | https://react.dev/reference/react | docs live; React version phải ghi | Behavior phụ thuộc React version, renderer, build/framework; không suy từ docs mới sang legacy app | `react/` |
| FE-TS-01 | TypeScript project | type-system/compiler behavior và lib target | https://www.typescriptlang.org/docs/handbook/intro.html | compiler/version/lib target phải ghi | Type checking không đảm bảo runtime behavior; ghi `tsconfig`, target và runtime | JavaScript/TypeScript |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| FE-BROWSER-01 | `NEEDS_SOURCE` | Claim về compatibility, rendering, performance, storage hoặc security cần browser/version, platform và test evidence; spec alone không đủ. | Owner web-platform track |
| FE-FRAMEWORK-01 | `REVIEW_REQUIRED` | React/WebSquare behavior phải ghi version, renderer/runtime, build config và migration boundary; không áp framework semantics lên browser invariant. | Owner framework track |
| FE-A11Y-01 | `REVIEW_REQUIRED` | WCAG mapping cần test bằng keyboard/AT và context; không gắn “WCAG compliant” chỉ vì có ARIA hoặc semantic tag. | Owner accessibility/audit |
| FE-WEBSQUARE-01 | `NEEDS_SOURCE` | Tài liệu public/versioned của WebSquare runtime và W-Pack chưa đủ để xác nhận mọi claim; giữ claim implementation-specific ở trạng thái cần vendor/manual evidence. | Owner `websquare/`; bổ sung vendor docs/version hoặc lab output |
| FE-PERF-01 | `NEEDS_SOURCE` | Performance claim cần baseline, device/browser, workload, trace và repeatability; không dùng “GPU/transform nhanh hơn” như invariant. | Owner case-study/performance lab |

## Quy trình refresh

1. Ghi spec section, browser/OS, framework/compiler version, build config và ngày kiểm tra cho claim versioned.
2. Tách normative platform semantics, implementation quirks, application contract và observed trace.
3. Khi browser/framework/compiler release hoặc deprecate API, chạy compatibility/test lab rồi cập nhật affected chapters.
4. Accessibility/security/performance claims cần review thủ công; link/build audit không thay thế runtime evidence.
