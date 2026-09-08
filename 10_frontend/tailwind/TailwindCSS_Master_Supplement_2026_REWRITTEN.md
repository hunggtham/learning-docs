# Tailwind CSS — Master Supplement, bản giải thích đầy đủ
## Tailwind CSS v4.3: compiler model, design-system architecture, source detection, custom APIs, migration và production engineering

> File này đọc sau `TailwindCSS_Beginner_to_Senior_2026_REWRITTEN.md`.
>
> File Beginner → Senior giúp bạn dùng Tailwind rất chắc trong production. File này đi sâu hơn vào những phần mà một Tailwind specialist, design-system engineer hoặc frontend senior cần hiểu khi project lớn lên: Tailwind build engine nhìn source như thế nào, `@theme` trở thành public API ra sao, custom utilities được resolve thế nào, source boundaries ảnh hưởng bundle như thế nào, vì sao class conflict không thể giải thích bằng thứ tự class trong HTML, và khi nào Tailwind bắt đầu trở thành một phần của package architecture chứ không chỉ là công cụ styling.

---

# PHẦN I — TỪ “DÙNG TAILWIND” ĐẾN “HIỂU HỆ THỐNG TAILWIND”

## 1. Tại sao cần một Master Supplement riêng?

Khi mới học Tailwind, vấn đề thường là “class nào tạo padding?”, “làm responsive thế nào?”, “dark mode viết ra sao?”. Khi đã làm production vài tháng, câu hỏi thay đổi. Bạn bắt đầu gặp những case như: class có trong JSX nhưng CSS không được generate; cùng một component hoạt động trong app A nhưng fail khi được publish thành package; một arbitrary value nhìn đúng nhưng IntelliSense không hiểu vì namespace ambiguous; `px-2` và `px-4` cùng xuất hiện nhưng class viết sau trong `className` không thắng; một stylesheet dùng `@apply` trong Vue scoped style không nhận custom theme; hoặc một microfrontend import Tailwind làm hỏng reset của host page.

Những vấn đề đó không còn là “học thêm utility”. Chúng nằm ở ranh giới giữa source code, build pipeline, generated CSS và browser. Vì vậy ở cấp độ master, mental model phải mở rộng thành:

```text
Application source
→ Candidate detection
→ Tailwind utility/variant resolution
→ CSS generation
→ Cascade layers
→ Browser style/layout/rendering
```

Mỗi lỗi cần được định vị vào đúng tầng trước khi sửa. Đây là kỹ năng giúp bạn tránh mất hàng giờ thay class ngẫu nhiên.

---

## 2. Tailwind v4 là một compiler-oriented authoring system

Tailwind v4 không nên được hình dung như một file `tailwind.css` chứa sẵn hàng chục nghìn class. Nó hoạt động giống một compiler pipeline: đọc CSS entrypoint, đọc các Tailwind directives, phát hiện class candidates trong source, resolve candidate đó thành utility/variant và generate CSS cần thiết.

Ví dụ source có:

```html
<div class="flex gap-4 rounded-xl">
```

Tailwind scanner phát hiện các token có khả năng là class. Resolver nhận ra `flex`, `gap-4`, `rounded-xl` là utilities hợp lệ. Sau đó Tailwind generate CSS rule tương ứng.

Nếu source chứa:

```text
something-that-looks-like-a-class
```

nhưng không map tới utility nào, nó bị bỏ qua.

Điểm quan trọng là Tailwind **không cần hiểu semantics của React component hoặc business logic**. Nó chỉ cần complete candidate strings.

---

## 3. Candidate detection không phải JavaScript evaluation

Hãy xem code:

```jsx
const color = "blue";

return (
  <div className={`bg-${color}-600`} />
);
```

Một JavaScript runtime có thể dễ dàng evaluate ra `bg-blue-600`. Nhưng Tailwind source detection không chạy application như JavaScript interpreter. Nó nhìn source như text.

Vì string `bg-blue-600` không tồn tại nguyên vẹn trong source, scanner không thể dựa vào runtime knowledge để generate class đó.

Cách đúng:

```jsx
const backgroundClasses = {
  blue: "bg-blue-600",
  green: "bg-green-600",
  red: "bg-red-600",
};

return (
  <div className={backgroundClasses[color]} />
);
```

Ở đây các complete candidates tồn tại literal trong source.

Đây không chỉ là limitation của scanner. Nó còn thúc đẩy architecture tốt hơn vì component có finite visual API.

---

## 4. Static mapping là một design pattern chứ không chỉ workaround

Giả sử Button nhận:

```tsx
<Button variant="danger" />
```

Bạn map:

```ts
const variants = {
  primary:
    "bg-blue-600 text-white hover:bg-blue-700",

  danger:
    "bg-red-600 text-white hover:bg-red-700",

  secondary:
    "bg-white text-gray-900 ring-1 ring-gray-300",
};
```

Pattern này tạo ra ba lợi ích cùng lúc.

Thứ nhất, Tailwind scanner nhìn thấy toàn bộ complete class names. Thứ hai, TypeScript có thể biến key thành finite union. Thứ ba, consumer chỉ biết semantic variant chứ không phụ thuộc palette implementation.

Nếu mai design đổi `danger` từ `red-600` sang `rose-700`, component consumer không cần sửa.

Ở cấp độ master, bạn nên nhìn static class mapping như **public API boundary**, không chỉ scanner hack.

---

# PHẦN II — SOURCE DETECTION NHƯ MỘT PHẦN CỦA ARCHITECTURE

## 5. Automatic source detection thực sự mang lại điều gì?

Tailwind v4 tự động scan project trong phần lớn setup. Nó cố tình bỏ qua nhiều nguồn không có giá trị cho utility detection như binary files, CSS files, common lockfiles, `node_modules` và nhiều path bị ignore bởi Git.

Điều này tốt cho performance và setup đơn giản. Nhưng khi app bắt đầu dùng monorepo hoặc package chứa component source, automatic detection không còn đủ.

Ví dụ:

```text
apps/web
packages/ui
```

Nếu `packages/ui` chứa JSX với Tailwind classes nhưng app build không tự scan package đó, CSS cần cho UI package có thể thiếu.

Khi đó source boundary trở thành một phần của kiến trúc build.

---

## 6. `@source` không chỉ là “fix class bị thiếu”

Bạn có thể register source:

```css
@import "tailwindcss";

@source "../../packages/ui/src";
```

Hoặc dependency:

```css
@source "../node_modules/@acme/ui-lib";
```

Tư duy beginner là: “class không generate thì thêm `@source`”.

Tư duy senior/master là: “stylesheet này chịu trách nhiệm generate CSS cho source domain nào?”

Một app admin có thể không cần scan storefront. Một storefront bundle không nên generate utility cho internal admin tool. Vì vậy `@source` giúp xác định ownership của CSS bundle.

---

## 7. Base path với `source()`

Trong monorepo, build command thường chạy từ root:

```text
repo/
├─ apps/
│  ├─ web/
│  └─ admin/
└─ packages/
```

Nếu source detection phụ thuộc current working directory một cách vô tình, build có thể khác giữa local và CI.

Bạn có thể xác định base path:

```css
@import "tailwindcss"
  source("../src");
```

Điều này làm source resolution gần stylesheet hơn và predictable hơn.

---

## 8. `@source not` và việc loại bỏ source không cần thiết

```css
@source not "../src/legacy";
```

Không phải mọi folder chứa HTML/JS đều nên scan.

Một folder legacy lớn có thể:
- không dùng Tailwind,
- chứa strings giống class khiến candidate noise,
- tăng file-watching/invalidation cost.

Explicitly exclude làm intent rõ và build boundary sạch hơn.

---

## 9. `source(none)` và multiple Tailwind bundles

Một app lớn có thể cần:

```text
admin.css
storefront.css
marketing.css
```

Nếu mỗi stylesheet automatic scan toàn repo, ba bundle có thể generate nhiều CSS overlap.

Admin:

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

Storefront:

```css
@import "tailwindcss"
  source(none);

@source "../storefront";
@source "../shared";
```

Bây giờ mỗi bundle có explicit candidate universe.

Đây là một bước chuyển từ “framework config” sang **asset architecture**.

---

## 10. Safelist bằng `@source inline()`

Có những utility không xuất hiện trong normal source nhưng bạn vẫn muốn generate.

Ví dụ HTML được tạo bởi hệ thống template bên ngoài biết class `underline`.

Bạn có thể force candidate bằng `@source inline(...)`.

Điều quan trọng ở cấp độ master là hiểu safelist làm tăng **candidate set**. Nếu bạn safelist mọi color, breakpoint, hover, focus, dark variant “cho chắc”, bạn đang chủ động bỏ usage-driven generation.

Safelist nên finite và business-driven.

---

## 11. Brace expansion và combinatorial explosion

Current source-inline APIs có khả năng generate ranges/variants rất mạnh. Nhưng syntax mạnh thường dẫn tới abuse.

Nếu bạn generate:

```text
20 colors
× 10 shades
× 5 breakpoints
× 4 states
```

bạn đã tạo hàng nghìn candidates trước khi application thực sự dùng.

Compiler làm đúng; architecture sai.

Senior cần luôn hỏi:

```text
Có bao nhiêu candidate thực tế?
Có bao nhiêu CSS rules?
Bundle tăng bao nhiêu?
```

---

# PHẦN III — `@theme` NHƯ PUBLIC DESIGN-SYSTEM API

## 12. Theme variable không chỉ là CSS custom property

Normal CSS:

```css
:root {
  --brand: #2563eb;
}
```

chỉ tạo runtime variable.

Tailwind:

```css
@theme {
  --color-brand: #2563eb;
}
```

có hai tác dụng.

Tác dụng đầu tiên là Tailwind compiler hiểu `brand` thuộc color namespace, nên generate APIs như:

```text
bg-brand
text-brand
border-brand
fill-brand
```

Tác dụng thứ hai là CSS variable theme cũng tồn tại trong generated CSS để browser hoặc custom CSS sử dụng.

Vì vậy `@theme` vừa là:
- compiler configuration,
- runtime token declaration.

---

## 13. Theme namespace quyết định vocabulary

Nếu bạn tạo:

```css
@theme {
  --radius-card: .75rem;
}
```

bạn đang thêm utility:

```text
rounded-card
```

Nếu tạo:

```css
@theme {
  --breakpoint-wide: 90rem;
}
```

bạn đang tạo responsive vocabulary liên quan breakpoint.

Vì thế token name trong Tailwind không chỉ là internal implementation. Nó xuất hiện trong markup trên toàn project.

Đổi:

```text
--radius-card
```

thành:

```text
--radius-panel
```

có thể yêu cầu sửa hàng trăm `rounded-card`.

Đó là lý do theme namespace là **public API**.

---

## 14. Versioning theme vocabulary

Nếu design system được publish như package, theme token rename có thể là breaking change.

Một semantic versioning mindset hợp lý là:
- thêm token mới nhưng giữ cũ: thường backward-compatible,
- đổi value nhẹ: có thể visual change nhưng không API break,
- xóa/rename token: API break,
- đổi breakpoint token: behavior break rộng.

CSS không có TypeScript compiler báo mọi consumer bị vỡ, nên deprecation/versioning càng quan trọng.

---

## 15. Primitive và semantic token nên coexist thế nào?

Primitive:

```text
blue-500
blue-600
gray-100
gray-900
```

mô tả visual scale.

Semantic:

```text
action-bg
action-fg
surface
text-muted
danger-border
```

mô tả role.

Một app nhỏ có thể dùng primitive directly:

```text
bg-blue-600
hover:bg-blue-700
```

Một design system nhiều brand/theme thường cần semantic layer:

```css
:root {
  --action-bg:
    var(--color-blue-600);

  --action-fg:
    var(--color-white);
}
```

Component:

```html
<button
  class="
    bg-(--action-bg)
    text-(color:--action-fg)
  "
>
```

Điểm mạnh là component không còn biết palette implementation.

---

## 16. Semantic token cần đủ chính xác

Một token:

```text
danger
```

có vẻ semantic nhưng quá rộng.

Nếu map tới `--color-danger`, Tailwind có thể cho dev viết:

```text
bg-danger
text-danger
border-danger
```

Trong design thực tế, danger background có thể là red rất nhạt, text là red đậm, border ở giữa.

Nên vocabulary có thể cần:

```text
danger-bg
danger-fg
danger-border
```

Semantic token tốt không phải token ít; nó là token có role rõ.

---

## 17. Reset namespace để enforce design system

Tailwind mặc định có palette lớn. Developer rất dễ chọn:

```text
blue-500
indigo-600
violet-500
```

theo cảm tính.

Strict system có thể reset:

```css
@theme {
  --color-*: initial;

  --color-surface: ...;
  --color-text: ...;
  --color-action: ...;
  --color-danger-bg: ...;
  --color-danger-fg: ...;
}
```

Bây giờ các utility default không được backed bởi token sẽ biến mất.

Đây là cách biến Tailwind từ “huge toolbox” thành **constrained design language**.

---

## 18. Cost của strict theme

Strict theme làm consistency tốt hơn nhưng có cost.

Component example từ internet:

```text
bg-slate-100
text-gray-700
```

có thể không hoạt động.

Third-party Tailwind source package có thể assume default tokens.

Do đó strict namespace phù hợp khi:
- design system đã mature,
- package ownership rõ,
- team muốn enforce vocabulary.

---

## 19. `@theme inline` và CSS variable resolution

Giả sử:

```css
@theme {
  --font-sans:
    var(--font-inter);
}
```

CSS custom properties resolve theo cascade/scope của element nơi chúng được dùng. Indirection đôi khi khiến variable referenced không có value ở scope expected.

`@theme inline` cho Tailwind generate utility với referenced expression trực tiếp hơn:

```css
@theme inline {
  --font-sans:
    var(--font-inter);
}
```

Đây là công cụ để kiểm soát **runtime CSS variable indirection**, không chỉ performance syntax.

---

## 20. `@theme static`

Tailwind có thể tối ưu theme variable output theo usage.

Nếu một external JavaScript library cần:

```text
--color-brand
```

nhưng không utility nào dùng brand trong scanned source, variable có thể không được emit theo normal usage-driven strategy.

`@theme static` ép generate đầy đủ theme declarations.

Use:
- theme package,
- JS reads tokens,
- documentation tool,
- animation system.

Đổi lại CSS output lớn hơn.

---

# PHẦN IV — CUSTOM UTILITY Ở CẤP COMPILER API

## 21. `@utility` là gì ở mức sâu hơn?

Simple:

```css
@utility content-auto {
  content-visibility: auto;
}
```

Bạn không chỉ viết một CSS class. Bạn đăng ký một utility với Tailwind để nó tham gia:
- variant system,
- candidate generation,
- utility sorting.

Use:

```text
content-auto
lg:content-auto
hover:content-auto
```

nếu condition hợp lý.

---

## 22. Utility tốt phải “atomic” theo nghĩa semantic

Atomic không có nghĩa đúng một CSS declaration trong mọi trường hợp. Tailwind core có utilities dùng custom properties hoặc nhiều declaration để tạo một effect.

Điều quan trọng là utility biểu diễn **một concern**.

Ví dụ:
- `truncate` có nhiều declarations nhưng một concern: single-line truncation.
- `ring-2` có implementation phức tạp nhưng một concern: ring width.

Một custom utility tên `dashboard-card-primary` chứa layout, color, hover và typography cùng lúc không còn atomic. Nó là component.

---

## 23. Functional utility

```css
@utility tab-* {
  tab-size:
    --value(
      --tab-size-*,
      integer,
      [integer]
    );
}
```

Tailwind nhìn candidate `tab-github`, `tab-4` hoặc `tab-[12]`, rồi thử resolver.

Bạn có thể hình dung functional utility như một mini grammar:

```text
prefix
+ value grammar
+ optional modifier grammar
→ CSS declaration
```

---

## 24. Theme value resolver

Nếu:

```css
@theme {
  --tab-size-github: 8;
}
```

và utility resolver có:

```css
--value(--tab-size-*)
```

candidate:

```text
tab-github
```

map tới theme token.

Điều này giúp custom utility family integrate với design-token system thay vì hard-code lookup table riêng.

---

## 25. Bare value resolver

```css
--value(integer)
```

cho phép candidate như:

```text
tab-2
tab-4
tab-8
```

resolve trực tiếp integer.

Bare values nên được giới hạn theo CSS/property semantics. Không phải mọi arbitrary text nên được accepted.

---

## 26. Arbitrary value resolver

```css
--value([integer])
```

cho bracket syntax.

Tailwind functional utility có thể hiểu các type CSS-oriented như:
- length,
- color,
- percentage,
- angle,
- ratio,
- number,
- integer.

Typed arbitrary value giúp parser biết bạn muốn gì và tránh ambiguity.

---

## 27. Nhiều resolver trong cùng utility

```css
@utility tab-* {
  tab-size:
    --value(
      --tab-size-*,
      integer,
      [integer]
    );
}
```

Tailwind thử các resolution forms theo grammar.

Khi tự thiết kế API, hãy chọn order/accepted forms sao cho developer dự đoán được. Một utility quá “thông minh” nhận 10 loại value khác nhau có thể trở nên khó dùng hơn raw CSS.

---

## 28. Transform value theo nguồn

Bạn có thể cần:
- percentage arbitrary giữ nguyên,
- integer bare chuyển sang percentage,
- theme token dùng trực tiếp.

Multiple declarations với `--value()` có thể được Tailwind resolve selectively.

Đây là feature dành cho framework-level utility authoring. Normal app hiếm khi cần custom parser phức tạp.

---

## 29. Negative custom utility

Tailwind không tự cho rằng mọi property có negative variant.

Ví dụ padding không thể âm, opacity không có nghĩa âm.

Nếu custom utility đại diện inset, bạn có thể đăng ký:
- positive family,
- negative family.

Điều này làm API explicit và phù hợp CSS validity.

---

## 30. `--default()` trong v4.3

Một utility:

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

có thể hỗ trợ bare:

```text
tab
```

với default 4.

`tab-2` vẫn explicit 2.

Bare default chỉ nên được thêm khi người đọc utility có thể đoán reasonable meaning. Nếu `surface` không rõ default màu gì, đừng tạo implicit default chỉ vì framework support.

---

## 31. Modifier

Một utility:

```text
text-lg/7
```

có:
- main value `lg`,
- modifier `7`.

Modifier phù hợp khi có relationship rõ giữa primary và secondary value.

Custom API có thể dùng `--modifier()`, nhưng senior cần tránh syntax clever. Utility grammar nên gần cách core Tailwind được đọc.

---

## 32. Custom utility sorting

Một hiểu nhầm là custom utility được cascade đúng theo vị trí bạn viết trong file.

Tailwind có utility-layer ordering/sorting behavior riêng để utilities compose predictable hơn, và v4 có logic liên quan số lượng properties cho custom utilities.

Do đó:
- không dựa vào source order local để giải conflict,
- inspect generated CSS nếu behavior quan trọng,
- component override nên dùng architecture rõ.

---

# PHẦN V — VARIANT ALGEBRA

## 33. Variant không phải text prefix

`hover:` không chỉ “thêm chữ hover vào class”. Nó transform CSS selector.

`md:` không transform selector, mà wrap rule trong media query.

`supports-*:` wrap trong `@supports`.

`group-hover:` tạo ancestor relationship.

`peer-invalid:` tạo sibling relationship.

Một variant vì vậy có thể được hiểu như **function biến đổi CSS context**.

---

## 34. Variant stacking

```text
dark:md:hover:bg-blue-600
```

là composition của ba transformations:
- dark condition,
- responsive media condition,
- hover selector.

Khi stacked variant không chạy, debug từng condition:
- dark state active?
- viewport đạt md?
- device hỗ trợ hover?
- element thật sự hover?

Đừng coi toàn class như một black box.

---

## 35. `@custom-variant` là reusable condition API

Nếu project lặp selector:

```text
[&:where([data-density=compact] *)]
```

nhiều nơi, hãy tạo:

```css
@custom-variant density-compact
  (&:where([data-density="compact"] *));
```

Markup:

```text
density-compact:py-1
```

Bây giờ design vocabulary biểu diễn semantic state thay vì raw selector.

---

## 36. Naming custom variant

Một project nội bộ có thể dùng:

```text
compact:
midnight:
authenticated:
```

Một design-system package được dùng ngoài project nên cân nhắc namespace:

```text
ds-compact:
ds-brand-a:
```

vì Tailwind core có thể thêm variants trong tương lai.

---

## 37. `@variant` trong custom CSS

Bạn đã quyết định custom selector là rõ nhất:

```css
.third-party-button {
  ...
}
```

nhưng vẫn muốn dark state giống Tailwind:

```css
.third-party-button {
  @variant dark {
    ...
  }
}
```

V4.3 nâng cấp stacked/compound `@variant`, nên Tailwind variant system có thể được reuse bên trong CSS chứ không chỉ markup.

---

# PHẦN VI — CASCADE VÀ CONFLICT Ở MỨC MASTER

## 38. Vì sao class order trong HTML không đảm bảo winner?

```html
<div class="px-2 px-4">
```

Nhiều người nghĩ `px-4` viết sau nên thắng. Nhưng CSS cascade không biết thứ tự token trong class attribute như source order của declarations.

Browser nhìn stylesheet:

```css
.px-2 { ... }
.px-4 { ... }
```

Rule nào được generate ở vị trí/layer nào mới ảnh hưởng source order.

Vì thế dynamic class composition không nên dựa vào string append order.

---

## 39. Conflict-aware merge libraries giải quyết vấn đề gì?

Trong component:

```text
base: px-4
caller: px-2
```

Bạn muốn caller override.

Một Tailwind-aware merge helper có thể nhận ra `px-4` và `px-2` thuộc cùng utility group rồi giữ intended winner trong normalized class string.

Nó không thay CSS engine; nó xử lý conflict trước khi markup render.

Use phù hợp ở reusable component library boundaries.

---

## 40. Prettier Tailwind class sorting không phải conflict engine

Tailwind-aware formatter sắp class để readability ổn định.

Nếu formatter đổi thứ tự text mà UI đổi behavior, bạn đang dựa vào một assumption không an toàn. Hãy kiểm tra conflict/cascade.

---

## 41. Cascade layers

Tailwind v4 dùng native layers:

```text
theme
base
components
utilities
```

Một rule trong utilities có layer priority cao hơn components trong normal cascade.

Điều này cho phép:

```css
@layer components {
  .card {
    padding: 1rem;
  }
}
```

và markup:

```html
<div class="card p-8">
```

utility override component without specificity war.

---

## 42. Unlayered CSS có thể gây surprise

Native CSS cascade có behavior đặc biệt khi layered và unlayered author styles coexist. Normal unlayered rule có thể có priority cao hơn layered normal styles.

Nếu bạn import một vendor CSS unlayered sau/bên cạnh Tailwind, utility có thể không override như bạn dự đoán.

Senior phải inspect:
- layer,
- origin,
- specificity,
- importance.

Không tăng `!important` ngay.

---

## 43. Per-utility important

V4 preferred:

```text
bg-red-500!
```

Use targeted exception.

Nếu bạn dùng important modifier khắp app, bạn đã phá advantage của predictable layered cascade.

---

## 44. Global important strategy

Tailwind có architecture options để generate utilities important trong một bundle/import scenario.

Đây có thể là migration tool khi host legacy CSS cực kỳ specific.

Nhưng global important làm:
- third-party override khó,
- component theming khó,
- user styles interaction phức tạp.

Hãy xem nó như temporary anti-corruption layer, không phải default.

---

# PHẦN VII — PREFLIGHT, EMBEDDING VÀ MICROFRONTENDS

## 45. Preflight trong greenfield app

Trong app mới, Preflight giúp:
- normalize defaults,
- predictable border box/reset behavior,
- Tailwind utilities có nền consistent.

Ở đây full import là hợp lý.

---

## 46. Preflight trong legacy host

Legacy app có thể assume:
- h1 mặc định lớn,
- ul có bullet,
- button có native border,
- body có margin/reset khác.

Import Tailwind Preflight có thể thay đổi toàn host.

Đừng sửa bằng hàng trăm override trước khi xác nhận root cause là reset collision.

---

## 47. Disable Preflight cho embedded widget

Một widget được inject vào host page nên tránh global reset.

Architecture có thể:
- import theme,
- import utilities,
- omit Preflight,
- prefix classes,
- scope source detection.

Mục tiêu là widget không làm thay đổi host typography/forms.

---

## 48. Prefixing

Prefix giúp:
- tránh class collisions,
- tránh CSS variable naming collisions tùy import strategy,
- coexist nhiều Tailwind systems.

Cost:
- markup dài,
- docs/examples khác standard,
- component packages phải biết prefix contract.

Dùng cho isolation requirement thật, không phải mặc định.

---

## 49. Microfrontend

Nếu nhiều microfrontend cùng chạy trên một document, ba nguy cơ lớn là:
- nhiều Preflight,
- duplicate theme variables,
- layer ordering không thống nhất.

Ba chiến lược phổ biến là:
- share một Tailwind/theme build,
- mỗi app dùng prefixed isolated bundle,
- Shadow DOM isolation.

Không có một đáp án universal; quyết định phụ thuộc deployment ownership.

---

# PHẦN VIII — RUNTIME VALUES VÀ TAILWIND BUILD-TIME

## 50. Runtime data không nên trở thành runtime class grammar

API trả về:

```json
{
  "progress": 73
}
```

Bad:

```jsx
className={`w-[${progress}%]`}
```

Good:

```jsx
<div
  style={{ "--progress": `${progress}%` }}
  className="w-(--progress)"
/>
```

Class remains static, value runtime.

Đây là một trong những boundary pattern quan trọng nhất.

---

## 51. Runtime color

```jsx
<div
  style={{
    "--card-bg": color,
  }}
  className="bg-(--card-bg)"
/>
```

Nếu namespace ambiguous:

```text
text-(color:--text)
```

nói rõ parser context.

---

## 52. Khi nào inline style vẫn hoàn toàn hợp lý?

Tailwind không có mục tiêu cấm inline styles.

Dynamic:
- x/y coordinate,
- progress,
- user color,
- canvas dimension
có thể hợp lý qua inline custom properties.

Utility class dùng để consume variable và kết hợp states/responsive.

---

## 53. CSP

Một security policy nghiêm ngặt có thể hạn chế inline style attributes.

Khi đó runtime CSS variable strategy cần phối hợp CSP:
- nonce,
- safe stylesheet injection,
- predefined class states,
tùy app.

Tailwind không bypass Content Security Policy.

---

# PHẦN IX — DARK MODE VÀ MULTI-THEME Ở SCALE LỚN

## 54. Utility-pair dark mode

```html
<div
  class="
    bg-white
    text-gray-950
    dark:bg-gray-950
    dark:text-gray-50
  "
>
```

Rất explicit và tốt trong app nhỏ/trung bình.

---

## 55. Khi dark pairs bắt đầu lặp quá nhiều

Nếu mọi component có 8 cặp:

```text
bg-x dark:bg-y
text-a dark:text-b
border-c dark:border-d
```

và bạn còn brand A, brand B, high contrast, theme seasonal, class strings phình mạnh.

Lúc đó semantic runtime tokens có thể tốt hơn:

```css
[data-theme="light"] {
  --surface: ...;
}

[data-theme="dark"] {
  --surface: ...;
}
```

Component chỉ:

```text
bg-(--surface)
```

---

## 56. FOUC

Manual theme thường cần JS đọc local storage.

Nếu script chạy sau page paint:
- browser render light,
- JS thêm `.dark`,
- page nhảy dark.

Đây là Flash of Unstyled/Incorrect Theme.

Fix ở initialization/SSR layer:
- server knows theme,
- early script,
- system preference fallback.

Tailwind generated CSS không thể tự quyết định persisted app preference.

---

# PHẦN X — ARIA, DATA, GROUP, PEER, HAS Ở MỨC ARCHITECTURE

## 57. ARIA là semantic contract

```text
aria-expanded
aria-selected
aria-pressed
```

không phải chỉ là convenient CSS states.

Nếu component có true accessibility semantics, Tailwind aria variant là tuyệt vời.

Nếu state chỉ là “loading skeleton visible”, dùng `data-loading` có thể đúng hơn `aria-*` tùy semantics.

---

## 58. Data attribute là presentation/application state hook

```html
<div
  data-state="open"
  class="data-[state=open]:opacity-100"
>
```

JS:

```text
state=open
```

Tailwind:

```text
visual response
```

Đây là separation tốt.

---

## 59. Group ownership

`group` là ancestor marker.

Trong nested UIs:

```text
group/card
group/menu
group/tooltip
```

giúp child target đúng ancestor.

Không name groups trong structure phức tạp có thể làm hover/focus style bị kích hoạt bởi ancestor xa.

---

## 60. `in-*` convenience vs precision

`in-*` bỏ explicit marker và tìm ancestor state.

Nó giảm markup nhưng tăng implicit dependency.

Senior chọn:
- shallow/simple → `in-*` okay,
- nested reusable component → named group.

---

## 61. Peer là sibling direction

CSS sibling selector không quay ngược.

```html
<input class="peer">
<p class="peer-invalid:block">
```

works.

Nếu paragraph đứng trước input, peer pattern không thể target backward.

Use:
- parent `has-*`,
- DOM restructure,
- application state
tùy case.

---

## 62. `has-*` không thay business logic

`:has()` nhìn DOM relationship.

Good:
- parent contains checked input,
- form group contains invalid input.

Không dùng `:has()` để suy business state không được biểu diễn trong DOM. State business vẫn phải đến từ app model.

---

# PHẦN XI — THIRD-PARTY INTEGRATION

## 63. Arbitrary variants phù hợp với integration nhỏ

```text
[&_.vendor-item]:p-2
```

một hoặc vài selector là fine.

---

## 64. Khi integration nên có stylesheet riêng

Nếu bạn có:

```text
vendor root
vendor item
vendor active item
vendor dropdown
vendor search
vendor disabled
vendor nested menu
```

class attribute sẽ trở thành selector language khó đọc.

Tạo:

```text
styles/integrations/vendor.css
```

và viết normal CSS hoặc `@apply` targeted.

---

## 65. `@apply` ở integration layer

```css
.vendor-dropdown {
  @apply rounded-xl bg-white shadow-xl;
}
```

Trong case markup không control, `@apply` thực sự có giá trị vì giúp use same Tailwind theme/utility values.

Đây khác với việc tự recreate mọi internal app component bằng `.btn-primary`.

---

## 66. `@reference` trong isolated style contexts

Nếu integration CSS/component style được xử lý riêng, `@reference` có thể expose theme/custom APIs mà không duplicate CSS.

Điều này đặc biệt hữu ích trong:
- Vue SFC,
- Svelte,
- CSS Modules.

Nhưng nếu chỉ dùng one token, direct `var(--color-...)` đơn giản hơn.

---

# PHẦN XII — TAILWIND + SCSS / CSS MODULES / SHADOW DOM

## 67. Một project có thể có quá nhiều styling layers

Ví dụ:

```text
SCSS variable
→ emits CSS var
→ Tailwind @theme alias
→ custom utility
→ @apply
→ CSS Module
→ component className
```

Kỹ thuật thì có thể hoạt động, nhưng debugging trở nên khó.

Mastery là biết **bỏ bớt layer**.

---

## 68. Tailwind + SCSS

SCSS vẫn mạnh nếu project cần:
- compile-time maps,
- functions,
- legacy Sass library configuration.

Tailwind v4 đã có:
- theme CSS vars,
- CSS-first utilities,
- native nesting ecosystem,
- variants.

Greenfield Tailwind project có thể không cần Sass.

Nếu dùng cả hai, hãy chọn một source of truth cho tokens.

---

## 69. Tailwind + CSS Modules

Tailwind:
- atomic styling in markup.

CSS Modules:
- local scoped selector.

Cả hai coexist tốt khi responsibilities khác nhau.

Nếu CSS Module chỉ có:

```css
.title {
  @apply text-red-500;
}
```

thì bạn đang thêm một abstraction mà không có value.

---

## 70. Shadow DOM

Tailwind generated stylesheet ở document không pierce shadow root.

Web Component cần:
- own stylesheet,
- adopted stylesheet,
- custom properties,
- `::part`
tùy API.

Tailwind không thay Shadow DOM encapsulation.

---

# PHẦN XIII — PACKAGE DESIGN

## 71. Design-system package có thể ship cái gì?

Một Tailwind design system có thể ship:
- source React/Vue components chứa Tailwind classes,
- compiled CSS,
- theme CSS,
- custom utilities.

Mỗi lựa chọn có coupling khác nhau.

---

## 72. Ship source components

Consumer build Tailwind dựa trên package source.

Ưu:
- utility generation theo usage.

Yêu cầu:
- consumer `@source` package,
- compatible Tailwind version,
- compatible theme vocabulary.

Tailwind trở thành peer/build contract.

---

## 73. Ship compiled CSS

Consumer không cần scan package.

Ưu:
- framework-neutral dễ dùng.

Nhược:
- CSS bundle static,
- potential duplicate reset/theme,
- theming cần public CSS vars,
- layer integration cần design.

---

## 74. Ship theme-only package

V4 rất phù hợp:

```text
@company/theme.css
```

chứa `@theme`.

Nhiều apps share:
- colors,
- typography,
- breakpoints,
- radii.

Theme package có thể version độc lập với component package.

---

## 75. Version compatibility

Nếu library dùng feature v4.3 như:
- `@container-size`,
- scrollbar utilities,
- `zoom-*`,
- new functional utility defaults,

docs nên nói rõ minimum Tailwind version.

Nếu không, consumer v4.1 có thể compile fail hoặc thiếu class.

---

# PHẦN XIV — V4.3 FEATURES VÀ Ý NGHĨA KIẾN TRÚC

## 76. Scrollbar utilities

V4.3 đưa scrollbar styling vào core tốt hơn.

Điều này có hai tác dụng:
- giảm nhu cầu community plugin/custom utility,
- làm design token integration dễ hơn.

Nhưng scrollbar vẫn là platform UI. Visual behavior cross-browser/OS không tuyệt đối giống nhau.

---

## 77. `@container-size`

Đây không chỉ là thêm một class. Nó phản ánh CSS platform đã đi sâu hơn vào component-local responsiveness.

Bạn có thể query block size/height-dependent contexts, nhưng size containment có layout consequences. Vì vậy đây là tool advanced.

---

## 78. `zoom-*`

V4.3 utility cho CSS `zoom` xuất hiện sau khi browser interoperability tốt hơn.

Use cases:
- preview,
- editor canvas,
- document miniature.

Không thay responsive layout.

---

## 79. `tab-*`

`tab-size` trở thành first-class utility.

Use:
- code rendering,
- source editor,
- preformatted blocks.

Một feature nhỏ nhưng minh họa triết lý Tailwind: khi CSS property trở nên đủ phổ biến, core utility API mở rộng để giảm custom CSS.

---

## 80. Stacked/compound `@variant`

Trước đây nhiều developer nghĩ variants chỉ dành class markup. V4.3 làm custom CSS variant reuse mạnh hơn.

Điều này giúp third-party/custom component CSS vẫn participate cùng state vocabulary của project.

---

# PHẦN XV — MIGRATION V3 → V4 SÂU HƠN

## 81. Migration không phải chỉ search-and-replace

V3 architecture thường gom:
- content paths,
- theme,
- plugins,
- safelist
vào JS config.

V4 đưa nhiều phần về CSS.

Do đó migration là cơ hội hỏi:
- theme tokens public nào?
- source ownership thế nào?
- custom plugin nào giờ chỉ cần `@utility`?
- safelist nào là technical debt?
- component nào đang dynamic class synthesis?

---

## 82. Upgrade tool

Official upgrade tooling có thể tự động phần lớn migration mechanics.

Nhưng tool không thể quyết định:
- semantic token design,
- monorepo source ownership,
- public component API,
- custom utility architecture.

Run tool, sau đó review.

---

## 83. Browser support trước khi migrate

Tailwind v4 dùng modern CSS baseline và có minimum browser targets cao hơn v3.

Nếu product còn hỗ trợ browser cũ, upgrade có thể là product decision chứ không chỉ package update.

Đây là lý do framework major version phải được đánh giá cùng browser policy.

---

## 84. `@config` như migration bridge

```css
@config "../../tailwind.config.js";
```

giúp giữ legacy JS config.

Nếu 2 năm sau project vẫn có:
- half CSS theme,
- half JS config,
- half plugins
thì migration chưa hoàn thành về architecture.

---

## 85. Custom plugin migration

Một v3 plugin chỉ tạo simple utility có thể chuyển sang `@utility`.

Plugin chỉ tạo variant có thể chuyển sang `@custom-variant`.

Complex JS plugin có logic/package integration vẫn có thể giữ plugin.

Mục tiêu không phải loại bỏ JS plugin bằng mọi giá, mà dùng simplest mechanism.

---

## 86. Safelist migration

Old safelist thường tích tụ “mysterious classes” qua năm tháng.

Khi chuyển sang `@source inline()`, hãy audit từng set:
- source thật sự ở đâu?
- CMS có finite values không?
- có thể static map không?

Đừng mechanically copy universe safelist.

---

# PHẦN XVI — PERFORMANCE

## 87. Tailwind performance cần đo ở đâu?

Có ba loại cost:
- source scanning,
- CSS generation/build time,
- final CSS bytes.

Ngoài ra browser vẫn chịu CSS/render cost như bình thường.

Một source tree lớn nhưng candidate ít có cost scanning. Một safelist lớn có cost generation/output. Một giant CSS bundle có network/parse cost.

---

## 88. Cold build và incremental build

Khi project lớn, đo:
- first clean build,
- rebuild khi đổi file không tạo candidate mới,
- rebuild khi thêm candidate,
- CI build.

V4 được tối ưu mạnh cho incremental generation, nhưng monorepo/file-watching config sai vẫn có thể dominate.

---

## 89. Unique arbitrary values

```text
top-[117px]
```

one-off không vấn đề.

Data-driven generation của hàng nghìn values mới là vấn đề.

Pattern đúng cho data:
- CSS variable,
- one static utility consumer.

---

## 90. `@theme static` và output size

Static theme giúp consumers ngoài utility system nhìn thấy tất cả tokens.

Nhưng nếu theme có hàng nghìn variables, output tăng.

Hãy quyết định dựa usage:
- design-token package cần full surface → hợp lý,
- app nhỏ chỉ dùng vài token → normal emission tốt hơn.

---

## 91. Nhiều CSS entrypoint

Hai entrypoint đều:

```css
@import "tailwindcss";
```

có thể mỗi cái chứa:
- Preflight,
- theme,
- overlapping utilities.

Nếu cả hai load cùng page, CSS duplicate.

Master cần audit stylesheet graph giống audit JS bundle graph.

---

## 92. `@apply` trong hàng nghìn component style blocks

Mỗi isolated style context cần Tailwind processing/reference resolution.

Nếu chỉ cần token color:

```css
color: var(--color-red-500);
```

rẻ và rõ hơn `@apply text-red-500`.

Không micro-optimize một component; nhưng architecture hàng nghìn components thì khác.

---

# PHẦN XVII — DEBUGGING Ở CẤP MASTER

## 93. Bước 1: xác định CSS có tồn tại không

DevTools/Search generated CSS.

Nếu `.bg-brand` không tồn tại:
- scanner,
- theme token,
- source,
- utility registration.

Nếu tồn tại:
- Tailwind build đã làm việc,
- chuyển sang cascade/layout debugging.

---

## 94. Debug source detection

Kiểm tra class có literal complete không.

Kiểm tra file:
- có bị ignored?
- nằm dependency?
- nằm ngoài base path?
- stylesheet bundle này có scan source đó?

Nếu package source, kiểm tra `@source`.

---

## 95. Debug custom theme

`bg-brand` không generate?

Check:

```css
@theme {
  --color-brand: ...
}
```

Nếu bạn chỉ đặt:

```css
:root {
  --color-brand: ...
}
```

thì runtime variable tồn tại nhưng Tailwind theme namespace có thể không đăng ký utility như bạn tưởng.

---

## 96. Debug custom utility

Candidate correct nhưng rule không có?

Check:
- `@utility` syntax,
- functional resolver type,
- theme key,
- default/modifier,
- value có resolve được không.

Build-time Tailwind có thể drop declaration không resolve.

---

## 97. Debug variant

`group-hover` không chạy?

Kiểm tra:
- ancestor thật sự có `group`,
- named group match,
- child trong correct descendant relationship,
- hover environment.

`peer-invalid` không chạy?

Kiểm tra:
- peer trước target,
- input thật sự invalid,
- selector relation.

---

## 98. Debug container

`@md:` không chạy?

Kiểm tra:
- ancestor có `@container`,
- nearest container có đủ width,
- nếu named query thì name đúng,
- `@container-size` chỉ cần cho block-size use case.

Không nhìn viewport width để kết luận container variant.

---

## 99. Debug class conflict

Mở computed style.

Tìm property:

```text
padding-left
padding-right
```

xem rule nào winner.

Đừng chỉ nhìn:

```html
class="px-4 px-2"
```

rồi đoán.

---

## 100. Debug z-index

Nếu utility rule `z-50` apply mà modal vẫn dưới:
- parent stacking context,
- top layer,
- transform/filter/opacity/isolation.

Tailwind không thể phá CSS stacking rules.

---

# PHẦN XVIII — ACCESSIBILITY VÀ UI STATE Ở SCALE

## 101. Accessibility phải được thiết kế thành component contract

Button component nên có:
- actual `<button>`,
- disabled behavior,
- focus-visible style,
- loading semantics,
- accessible label khi icon-only.

Tailwind utilities làm implementation concise, nhưng contract nằm ở component design.

---

## 102. State matrix

Một mature component không chỉ test default.

Button có thể có:

```text
variant × size ×
hover/focus/active/disabled/loading
× light/dark
× forced colors
```

Tailwind giúp encode combinations, nhưng state space vẫn tồn tại.

Visual regression rất hữu ích.

---

## 103. Reduced motion không phải optional polish

Nếu component có transform/animation lớn:
- add `motion-reduce`,
- hoặc thiết kế motion system global.

User preference là input giống viewport/theme, không phải afterthought.

---

## 104. Forced colors

Colors có thể bị browser override.

Nếu custom control chỉ biểu diễn selected state bằng subtle background color, forced colors mode có thể mất distinction.

Test actual forced-colors behavior và use semantic border/system color fallback khi cần.

---

# PHẦN XIX — TESTING

## 105. Static tests

Static tooling có thể bắt:
- invalid class,
- deprecated class,
- dynamic concatenation patterns,
- arbitrary-value policy.

IDE IntelliSense giúp feedback sớm.

---

## 106. Component tests

Test behavior:
- disabled thật sự không click,
- aria-expanded thay đổi,
- data-state transition đúng.

Đừng test chỉ class string nếu behavior mới là contract.

---

## 107. Visual regression

CSS bug thường không throw exception.

Capture screenshots cho:
- mobile,
- tablet,
- desktop,
- dark,
- focus,
- long text,
- RTL.

Với component library, thêm:
- loading,
- empty,
- error,
- disabled.

---

## 108. Tại sao exact class snapshot thường brittle?

Nếu test:

```text
expect(button.className)
  .toBe("flex px-4 ...")
```

formatter hoặc harmless refactor làm test fail.

Prefer semantic/visual tests.

Class snapshot chỉ hợp lý nếu class output là public API hoặc bạn đang test class-merging utility.

---

# PHẦN XX — SECURITY VÀ CMS

## 109. Không nhận raw Tailwind class từ user nếu không cần

CMS có option “danger”.

Bad data:

```text
bg-red-500
```

Better data:

```text
danger
```

App map:

```text
danger → bg-red-500 text-white
```

Bạn giữ:
- design governance,
- scanner visibility,
- security boundary.

---

## 110. Arbitrary value từ untrusted input

Không concatenate user input vào:

```text
[background:url(...)]
```

hoặc arbitrary property.

Tailwind không sanitize CSS intent.

Whitelist values hoặc validate data rồi expose qua safe runtime variable.

---

# PHẦN XXI — TƯ DUY PACKAGE VÀ ENTERPRISE

## 111. CSS source of truth phải là một nơi

Một hệ thống dễ hỏng nếu cùng color tồn tại độc lập trong:
- Tailwind `@theme`,
- Sass `$map`,
- CSS `:root`,
- TypeScript constants,
- Figma export.

Enterprise nên có một token source chính, sau đó generate/alias cho các platform.

Tailwind v4 phù hợp làm consumer/output của token pipeline.

---

## 112. External design token pipeline

Ví dụ:

```text
tokens.json
→ build transform
→ theme.css
→ @theme
→ Tailwind utilities
```

và cùng source có thể generate:
- iOS tokens,
- Android resources,
- TypeScript constants.

Không nên parse JSON bằng CSS/Tailwind tricks.

---

## 113. Tailwind là implementation detail của component library

Consumer:

```tsx
<Button variant="primary" />
```

không nên cần biết:

```text
bg-blue-600
```

Nếu sau này team đổi sang CSS Modules hoặc vanilla CSS, component API vẫn giữ.

Đây là abstraction boundary khỏe mạnh.

---

# PHẦN XXII — KHI NÀO KHÔNG NÊN DÙNG TAILWIND

## 114. Complex rich-text styling

Một article renderer có nested:
- h2,
- blockquote,
- tables,
- code,
- lists,
- links
từ CMS.

Viết class vào từng generated element không practical.

Scoped semantic CSS hoặc typography solution hợp lý hơn.

---

## 115. Third-party DOM sâu

Một editor library có internal DOM tree thay đổi theo version. Một stylesheet integration rõ ràng tốt hơn arbitrary variant cực dài trong root class.

---

## 116. CSS feature có syntax phức tạp

Animation keyframes, advanced selector hoặc print stylesheet có thể đọc tốt hơn khi viết CSS trực tiếp.

Tailwind hỗ trợ arbitrary/custom API, nhưng không phải mọi CSS nên được convert thành utility.

---

# PHẦN XXIII — MASTER DECISION FRAMEWORK

## 117. Chọn đúng abstraction

Nếu vấn đề là atomic styling với core CSS property, dùng utility.

Nếu value là exception một lần, dùng arbitrary value.

Nếu value lặp thành design vocabulary, dùng `@theme`.

Nếu value thay đổi runtime, dùng CSS custom property.

Nếu project thiếu một atomic utility reusable, dùng `@utility`.

Nếu condition selector lặp lại, dùng `@custom-variant`.

Nếu selector phức tạp nhưng local/semantic, dùng CSS.

Nếu structure + style + state lặp lại, extract component.

Nếu source nằm ngoài automatic scan, dùng `@source`.

Đây là cách senior tránh “mọi thứ thành utility” hoặc “mọi thứ thành custom CSS”.

---

# PHẦN XXIV — MASTER LABS

## 118. Lab: scanner

Tạo bốn trường hợp:
- literal `bg-blue-600`,
- dynamic ``bg-${color}-600``,
- static map,
- class trong workspace package.

Build và inspect generated CSS. Mục tiêu là tự nhìn thấy scanner boundary.

---

## 119. Lab: strict theme

Reset color namespace, chỉ define:
- surface,
- text,
- action,
- danger.

Sau đó thử dùng `bg-blue-500` và quan sát API không còn. Mục tiêu là hiểu `@theme` điều khiển utility vocabulary.

---

## 120. Lab: functional utility

Tạo `tab-*` hỗ trợ:
- theme value,
- integer,
- arbitrary,
- bare default.

Sau đó inspect generated CSS cho từng form.

---

## 121. Lab: source split

Tạo admin/storefront bundles với `source(none)`.

Đo:
- CSS raw size,
- overlap,
- candidate count.

Mục tiêu là hiểu source detection như bundle architecture.

---

## 122. Lab: runtime CSS variable

API value:
- width,
- color.

Không dùng dynamic arbitrary class.

Bridge bằng CSS vars và static utilities.

---

## 123. Lab: container component

Cùng một ProfileCard đặt trong:
- sidebar 280px,
- content 600px,
- modal 900px.

Dùng container query thay viewport breakpoint cho internal layout.

---

## 124. Lab: v3 migration

Lấy project có:
- `tailwind.config.js`,
- content,
- safelist,
- custom utility plugin.

Migrate từng phần sang v4 CSS-first, nhưng giữ visual regression snapshots để đảm bảo behavior không đổi.

---

## 125. Lab: embedded widget

Nhúng widget vào một legacy page.

Thử:
- full Tailwind import,
- disable Preflight,
- prefix,
- isolate sources.

Quan sát host page bị ảnh hưởng thế nào.

---

# PHẦN XXV — MASTER SELF-CHECK

## 126. Bạn đã đạt mức master khi nào?

Bạn chưa cần nhớ mọi utility. Thay vào đó, bạn nên có thể giải thích bằng lời của mình vì sao Tailwind không generate dynamic interpolated class; tại sao `@theme` là compiler API chứ không chỉ CSS variables; tại sao theme token rename có thể là breaking change; tại sao source boundaries nên thiết kế theo bundle ownership; vì sao `@container-size` không nên thay toàn bộ `@container`; functional utility resolver hoạt động ở build time ra sao; vì sao HTML class order không phải CSS source order; `@reference` có role gì trong isolated stylesheet; tại sao runtime data nên đi qua CSS variable; vì sao ARIA và data attributes không interchangeable về semantics; và khi nào Tailwind abstraction bắt đầu làm code khó hiểu hơn plain CSS.

Bạn cũng nên debug được một issue theo pipeline:

```text
source
→ candidate
→ generated rule
→ cascade
→ layout
```

thay vì thêm class thử từng cái.

---

# PHẦN XXVI — PRODUCTION CHECK

## 127. Trước khi merge một Tailwind feature lớn

Hãy đọc component như một hệ thống. Xác định responsive ownership thuộc viewport hay container. Xác định state là native, ARIA, data hay business state. Kiểm tra arbitrary values có đang lặp thành hidden token hay không. Kiểm tra focus, disabled, reduced motion. Với component reusable, xác định class override policy. Với monorepo/package, xác định source scanner có nhìn thấy class hay không. Sau cùng, inspect generated CSS khi có custom utility/variant hoặc conflict khó.

Đây không phải checklist để tick máy móc; đây là cách senior đọc implementation trước khi PR trở thành technical debt.

---

# PHẦN XXVII — TÀI LIỆU CHÍNH THỨC

Tailwind CSS documentation:

https://tailwindcss.com/docs

Tailwind CSS v4.3 release:

https://tailwindcss.com/blog/tailwindcss-v4-3

Theme variables:

https://tailwindcss.com/docs/theme

Detecting classes in source files:

https://tailwindcss.com/docs/detecting-classes-in-source-files

Functions and directives:

https://tailwindcss.com/docs/functions-and-directives

Responsive design and container queries:

https://tailwindcss.com/docs/responsive-design

Styling utilities:

https://tailwindcss.com/docs/styling-with-utility-classes

Upgrade guide:

https://tailwindcss.com/docs/upgrade-guide

---

# KẾT LUẬN

Ở level beginner, Tailwind có vẻ là:

```text
class → CSS property
```

Ở level senior, Tailwind trở thành:

```text
utility composition
+ state variants
+ component architecture
+ design tokens
```

Ở level master, bạn nhìn thấy toàn pipeline:

```text
source ownership
→ candidate detection
→ theme/public API
→ custom utility grammar
→ variant algebra
→ cascade layers
→ browser
```

Điểm quan trọng nhất là không để Tailwind trở thành black box. Nếu framework làm bạn khó hiểu CSS hơn, abstraction đang bị dùng sai. Nếu Tailwind giúp design vocabulary rõ hơn, source gần component hơn, responsive/state declarative hơn và build output predictable hơn, bạn đang dùng nó đúng ở mức senior/master.
