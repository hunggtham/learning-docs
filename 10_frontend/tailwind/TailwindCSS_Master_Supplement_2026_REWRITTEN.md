# Tailwind CSS — Master Supplement, bản giải thích đầy đủ
## Tailwind CSS v4.3: trình biên dịch (compiler) model, design-system kiến trúc (architecture), phát hiện nguồn (source detection), custom APIs, chuyển đổi (migration) và production engineering

> File này đọc sau `TailwindCSS_Beginner_to_Senior_2026_REWRITTEN.md`.
>
> File Beginner → Senior giúp bạn dùng Tailwind rất chắc trong production. File này đi sâu hơn vào những phần mà một Tailwind specialist, design-system engineer hoặc frontend senior cần hiểu khi project lớn lên: Tailwind build engine nhìn source như thế nào, `@theme` trở thành giao diện công khai (public API) ra sao, custom các tiện ích (utilities) được resolve thế nào, source boundaries ảnh hưởng bundle như thế nào, vì sao class conflict không thể giải thích bằng thứ tự class trong HTML, và khi nào Tailwind bắt đầu trở thành một phần của package kiến trúc (architecture) chứ không chỉ là công cụ styling.

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Tailwind được diễn đạt bằng tiếng Việt trước rồi giữ từ gốc bên cạnh khi cần đối chiếu. Ví dụ: **mô hình ưu tiên tiện ích (utility-first)**, **tiện ích (utility)**, **biến thể trạng thái (state variant)**, **giá trị tùy ý (arbitrary value)**, **điểm ngắt (breakpoint)**, **truy vấn vùng chứa (container query)**, **phát hiện nguồn (source detection)**, **biên dịch tức thời (JIT, just-in-time)** và **cấu hình ưu tiên CSS (CSS-first configuration)**. Tên class, directive và utility literal trong code luôn được giữ nguyên.


# PHẦN I — TỪ “DÙNG TAILWIND” ĐẾN “HIỂU HỆ THỐNG TAILWIND”

## 1. Tại sao cần một Master Supplement riêng?

## 1A. Master diagnosis: tiện ích (utility) → generated CSS → browser behavior

Ở level master, một tiện ích (utility) phải trace được theo hai chiều. Chiều xuôi bắt đầu từ class candidate, qua source scanner, biến thể (variant)/theme resolver, tới generated CSS rồi browser layout/rendering. Chiều ngược bắt đầu từ UI bug trong DevTools, truy computed style và layout context để tìm candidate/build rule gây behavior.

Ví dụ `min-w-0` resolve thành `min-width: 0`; browser dùng giá trị (value) này khi tính minimum inline size của flex/phần tử Grid (grid item), cho phép item co nhỏ hơn intrinsic content width. Nếu ellipsis hoạt động sau khi thêm `min-w-0`, nguyên nhân là layout constraint thay đổi chứ không phải Tailwind có truncate magic. `md:hover:bg-brand` cũng phải tách thành điểm ngắt (breakpoint) condition + hover bộ chọn (selector) + theme color token. Nếu rule không được generate, gỡ lỗi (debug) source/theme; nếu rule có nhưng inactive, gỡ lỗi (debug) conditions; nếu apply nhưng visual vẫn sai, gỡ lỗi (debug) cơ chế phân tầng (cascade)/blending/browser CSS.

Version đường cơ sở (baseline) vẫn là **Tailwind CSS v4.3** tại audit 2026-09-21. Khi migrate v3/early-v4, hãy xem đây là kiến trúc (architecture) change: JS config-first → ưu tiên CSS (CSS-first) `@theme`; `content` globs → automatic detection/`@source`; simple custom plugin tiện ích (utility) → `@utility`; repeated bộ chọn (selector) trạng thái (state) → `@custom-variant` khi phù hợp. chuyển đổi (migration) cần diff generated CSS, browser đường cơ sở (baseline) và hồi quy giao diện (visual regression), không chỉ search/replace syntax.


Khi mới học Tailwind, vấn đề thường là “class nào tạo padding?”, “làm responsive thế nào?”, “dark mode viết ra sao?”. Khi đã làm production vài tháng, câu hỏi thay đổi. Bạn bắt đầu gặp những case như: class có trong JSX nhưng CSS không được generate; cùng một component hoạt động trong app A nhưng fail khi được publish thành package; một giá trị tùy ý (arbitrary value) nhìn đúng nhưng IntelliSense không hiểu vì không gian tên (namespace) ambiguous; `px-2` và `px-4` cùng xuất hiện nhưng class viết sau trong `className` không thắng; một stylesheet dùng `@apply` trong Vue scoped style không nhận custom theme; hoặc một microfrontend import Tailwind làm hỏng reset của host page.

Những vấn đề đó không còn là “học thêm tiện ích (utility)”. Chúng nằm ở ranh giới giữa source code, quy trình build (build pipeline), generated CSS và browser. Vì vậy ở cấp độ master, mô hình tư duy (mental model) phải mở rộng thành:

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

Tailwind v4 không nên được hình dung như một file `tailwind.css` chứa sẵn hàng chục nghìn class. Nó hoạt động giống một trình biên dịch (compiler) pipeline: đọc CSS entrypoint, đọc các Tailwind directives, phát hiện class candidates trong source, resolve candidate đó thành tiện ích (utility)/biến thể (variant) và generate CSS cần thiết.

Ví dụ source có:

```html
<div class="flex gap-4 rounded-xl">
```

Tailwind scanner phát hiện các token có khả năng là class. Resolver nhận ra `flex`, `gap-4`, `rounded-xl` là các tiện ích (utilities) hợp lệ. Sau đó Tailwind generate CSS rule tương ứng.

Nếu source chứa:

```text
something-that-looks-like-a-class
```

nhưng không map khóa–giá trị (map) tới tiện ích (utility) nào, nó bị bỏ qua.

Điểm quan trọng là Tailwind **không cần hiểu ngữ nghĩa (semantics) của React component hoặc business logic**. Nó chỉ cần complete candidate strings.

---

## 3. phát hiện ứng viên lớp (candidate detection) không phải JavaScript evaluation

Hãy xem code:

```jsx
const color = "blue";

return (
  <div className={`bg-${color}-600`} />
);
```

Một JavaScript thời gian chạy (runtime) có thể dễ dàng evaluate ra `bg-blue-600`. Nhưng Tailwind phát hiện nguồn (source detection) không chạy application như JavaScript interpreter. Nó nhìn source như text.

Vì string `bg-blue-600` không tồn tại nguyên vẹn trong source, scanner không thể dựa vào thời gian chạy (runtime) knowledge để generate class đó.

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

Đây không chỉ là limitation của scanner. Nó còn thúc đẩy kiến trúc (architecture) tốt hơn vì component có finite visual API.

---

## 4. Static mapping là một mẫu thiết kế (design pattern) chứ không chỉ workaround

Giả sử Button nhận:

```tsx
<Button variant="danger" />
```

Bạn map khóa–giá trị (map):

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

Thứ nhất, Tailwind scanner nhìn thấy toàn bộ complete class names. Thứ hai, TypeScript có thể biến key thành finite union. Thứ ba, consumer chỉ biết mang tính ngữ nghĩa (semantic) biến thể (variant) chứ không phụ thuộc palette implementation.

Nếu mai design đổi `danger` từ `red-600` sang `rose-700`, component consumer không cần sửa.

Ở cấp độ master, bạn nên nhìn static class mapping như **giao diện công khai (public API) boundary**, không chỉ scanner hack.

---

# PHẦN II — phát hiện nguồn (source detection) NHƯ MỘT PHẦN CỦA kiến trúc (architecture)

## 5. Automatic phát hiện nguồn (source detection) thực sự mang lại điều gì?

Tailwind v4 tự động scan project trong phần lớn setup. Nó cố tình bỏ qua nhiều nguồn không có giá trị cho tiện ích (utility) detection như binary files, CSS files, common lockfiles, `node_modules` và nhiều path bị ignore bởi Git.

Điều này tốt cho hiệu năng (performance) và setup đơn giản. Nhưng khi app bắt đầu dùng monorepo hoặc package chứa component source, automatic detection không còn đủ.

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

Một app admin có thể không cần scan storefront. Một storefront bundle không nên generate tiện ích (utility) cho internal admin tool. Vì vậy `@source` giúp xác định ownership của CSS bundle.

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

Nếu phát hiện nguồn (source detection) phụ thuộc current working directory một cách vô tình, build có thể khác giữa local và CI.

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

Đây là một bước chuyển từ “framework config” sang **asset kiến trúc (architecture)**.

---

## 10. danh sách ép giữ (safelist) bằng `@source inline()`

Có những tiện ích (utility) không xuất hiện trong normal source nhưng bạn vẫn muốn generate.

Ví dụ HTML được tạo bởi hệ thống template bên ngoài biết class `underline`.

Bạn có thể force candidate bằng `@source inline(...)`.

Điều quan trọng ở cấp độ master là hiểu danh sách ép giữ (safelist) làm tăng **candidate set**. Nếu bạn danh sách ép giữ (safelist) mọi color, điểm ngắt (breakpoint), hover, focus, dark biến thể (variant) “cho chắc”, bạn đang chủ động bỏ usage-driven generation.

danh sách ép giữ (safelist) nên finite và business-driven.

---

## 11. Brace expansion và combinatorial explosion

Current source-inline APIs có khả năng generate ranges/các biến thể (variants) rất mạnh. Nhưng syntax mạnh thường dẫn tới abuse.

Nếu bạn generate:

```text
20 colors
× 10 shades
× 5 breakpoints
× 4 states
```

bạn đã tạo hàng nghìn candidates trước khi application thực sự dùng.

trình biên dịch (compiler) làm đúng; kiến trúc (architecture) sai.

Senior cần luôn hỏi:

```text
Có bao nhiêu candidate thực tế?
Có bao nhiêu CSS rules?
Bundle tăng bao nhiêu?
```

---

# PHẦN III — `@theme` NHƯ PUBLIC DESIGN-SYSTEM API

## 12. biến chủ đề (theme variable) không chỉ là CSS custom thuộc tính (property)

Normal CSS:

```css
:root {
  --brand: #2563eb;
}
```

chỉ tạo thời gian chạy (runtime) biến (variable).

Tailwind:

```css
@theme {
  --color-brand: #2563eb;
}
```

có hai tác dụng.

Tác dụng đầu tiên là Tailwind trình biên dịch (compiler) hiểu `brand` thuộc color không gian tên (namespace), nên generate APIs như:

```text
bg-brand
text-brand
border-brand
fill-brand
```

Tác dụng thứ hai là CSS biến (variable) theme cũng tồn tại trong generated CSS để browser hoặc custom CSS sử dụng.

Vì vậy `@theme` vừa là:
- trình biên dịch (compiler) cấu hình (configuration),
- thời gian chạy (runtime) token khai báo (declaration).

---

## 13. không gian tên chủ đề (theme namespace) quyết định vocabulary

Nếu bạn tạo:

```css
@theme {
  --radius-card: .75rem;
}
```

bạn đang thêm tiện ích (utility):

```text
rounded-card
```

Nếu tạo:

```css
@theme {
  --breakpoint-wide: 90rem;
}
```

bạn đang tạo responsive vocabulary liên quan điểm ngắt (breakpoint).

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

Đó là lý do không gian tên chủ đề (theme namespace) là **giao diện công khai (public API)**.

---

## 14. Versioning theme vocabulary

Nếu hệ thống thiết kế (design system) được publish như package, theme token rename có thể là breaking change.

Một mang tính ngữ nghĩa (semantic) versioning mindset hợp lý là:
- thêm token mới nhưng giữ cũ: thường backward-compatible,
- đổi giá trị (value) nhẹ: có thể visual change nhưng không API break,
- xóa/rename token: API break,
- đổi điểm ngắt (breakpoint) token: behavior break rộng.

CSS không có TypeScript trình biên dịch (compiler) báo mọi consumer bị vỡ, nên trạng thái ngừng khuyến nghị (deprecation)/versioning càng quan trọng.

---

## 15. Primitive và token ngữ nghĩa (semantic token) nên coexist thế nào?

Primitive:

```text
blue-500
blue-600
gray-100
gray-900
```

mô tả visual scale.

mang tính ngữ nghĩa (semantic):

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

Một hệ thống thiết kế (design system) nhiều brand/theme thường cần mang tính ngữ nghĩa (semantic) layer:

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

## 16. token ngữ nghĩa (semantic token) cần đủ chính xác

Một token:

```text
danger
```

có vẻ mang tính ngữ nghĩa (semantic) nhưng quá rộng.

Nếu map khóa–giá trị (map) tới `--color-danger`, Tailwind có thể cho dev viết:

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

token ngữ nghĩa (semantic token) tốt không phải token ít; nó là token có role rõ.

---

## 17. Reset không gian tên (namespace) để enforce hệ thống thiết kế (design system)

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

Bây giờ các tiện ích (utility) default không được backed bởi token sẽ biến mất.

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

Do đó strict không gian tên (namespace) phù hợp khi:
- hệ thống thiết kế (design system) đã mature,
- package ownership rõ,
- team muốn enforce vocabulary.

---

## 19. `@theme inline` và CSS biến (variable) resolution

Giả sử:

```css
@theme {
  --font-sans:
    var(--font-inter);
}
```

CSS custom các thuộc tính (properties) resolve theo cơ chế phân tầng (cascade)/phạm vi (scope) của element nơi chúng được dùng. Indirection đôi khi khiến biến (variable) referenced không có giá trị (value) ở phạm vi (scope) expected.

`@theme inline` cho Tailwind generate tiện ích (utility) với referenced expression trực tiếp hơn:

```css
@theme inline {
  --font-sans:
    var(--font-inter);
}
```

Đây là công cụ để kiểm soát **thời gian chạy (runtime) CSS biến (variable) indirection**, không chỉ hiệu năng (performance) syntax.

---

## 20. `@theme static`

Tailwind có thể tối ưu biến chủ đề (theme variable) output theo usage.

Nếu một external JavaScript library cần:

```text
--color-brand
```

nhưng không tiện ích (utility) nào dùng brand trong scanned source, biến (variable) có thể không được emit theo normal usage-driven strategy.

`@theme static` ép generate đầy đủ theme các khai báo (declarations).

Use:
- theme package,
- JS reads tokens,
- documentation tool,
- animation system.

Đổi lại CSS output lớn hơn.

---

# PHẦN IV — CUSTOM tiện ích (utility) Ở CẤP trình biên dịch (compiler) API

## 21. `@utility` là gì ở mức sâu hơn?

Simple:

```css
@utility content-auto {
  content-visibility: auto;
}
```

Bạn không chỉ viết một CSS class. Bạn đăng ký một tiện ích (utility) với Tailwind để nó tham gia:
- biến thể (variant) system,
- candidate generation,
- tiện ích (utility) sorting.

Use:

```text
content-auto
lg:content-auto
hover:content-auto
```

nếu condition hợp lý.

---

## 22. tiện ích (utility) tốt phải “atomic” theo nghĩa mang tính ngữ nghĩa (semantic)

Atomic không có nghĩa đúng một CSS khai báo (declaration) trong mọi trường hợp. Tailwind core có các tiện ích (utilities) dùng custom các thuộc tính (properties) hoặc nhiều khai báo (declaration) để tạo một effect.

Điều quan trọng là tiện ích (utility) biểu diễn **một concern**.

Ví dụ:
- `truncate` có nhiều các khai báo (declarations) nhưng một concern: single-line truncation.
- `ring-2` có implementation phức tạp nhưng một concern: ring width.

Một custom tiện ích (utility) tên `dashboard-card-primary` chứa layout, color, hover và typography cùng lúc không còn atomic. Nó là component.

---

## 23. Functional tiện ích (utility)

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

Bạn có thể hình dung functional tiện ích (utility) như một mini grammar:

```text
prefix
+ value grammar
+ optional modifier grammar
→ CSS declaration
```

---

## 24. Theme giá trị (value) resolver

Nếu:

```css
@theme {
  --tab-size-github: 8;
}
```

và tiện ích (utility) resolver có:

```css
--value(--tab-size-*)
```

candidate:

```text
tab-github
```

map khóa–giá trị (map) tới theme token.

Điều này giúp custom tiện ích (utility) family integrate với design-token system thay vì hard-code lookup table riêng.

---

## 25. Bare giá trị (value) resolver

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

Bare các giá trị (values) nên được giới hạn theo CSS/thuộc tính (property) ngữ nghĩa (semantics). Không phải mọi arbitrary text nên được accepted.

---

## 26. giá trị tùy ý (arbitrary value) resolver

```css
--value([integer])
```

cho bracket syntax.

Tailwind functional tiện ích (utility) có thể hiểu các type CSS-oriented như:
- length,
- color,
- percentage,
- angle,
- ratio,
- number,
- integer.

Typed giá trị tùy ý (arbitrary value) giúp parser biết bạn muốn gì và tránh ambiguity.

---

## 27. Nhiều resolver trong cùng tiện ích (utility)

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

Khi tự thiết kế API, hãy chọn order/accepted forms sao cho developer dự đoán được. Một tiện ích (utility) quá “thông minh” nhận 10 loại giá trị (value) khác nhau có thể trở nên khó dùng hơn raw CSS.

---

## 28. Transform giá trị (value) theo nguồn

Bạn có thể cần:
- percentage arbitrary giữ nguyên,
- integer bare chuyển sang percentage,
- theme token dùng trực tiếp.

Multiple các khai báo (declarations) với `--value()` có thể được Tailwind resolve selectively.

Đây là feature dành cho framework-level tiện ích (utility) authoring. Normal app hiếm khi cần custom parser phức tạp.

---

## 29. Negative custom tiện ích (utility)

Tailwind không tự cho rằng mọi thuộc tính (property) có negative biến thể (variant).

Ví dụ padding không thể âm, opacity không có nghĩa âm.

Nếu custom tiện ích (utility) đại diện inset, bạn có thể đăng ký:
- positive family,
- negative family.

Điều này làm API explicit và phù hợp CSS validity.

---

## 30. `--default()` trong v4.3

Một tiện ích (utility):

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

Bare default chỉ nên được thêm khi người đọc tiện ích (utility) có thể đoán reasonable meaning. Nếu `surface` không rõ default màu gì, đừng tạo implicit default chỉ vì framework support.

---

## 31. Modifier

Một tiện ích (utility):

```text
text-lg/7
```

có:
- main giá trị (value) `lg`,
- modifier `7`.

Modifier phù hợp khi có relationship rõ giữa primary và secondary giá trị (value).

Custom API có thể dùng `--modifier()`, nhưng senior cần tránh syntax clever. tiện ích (utility) grammar nên gần cách core Tailwind được đọc.

---

## 32. Custom tiện ích (utility) sorting

Một hiểu nhầm là custom tiện ích (utility) được cơ chế phân tầng (cascade) đúng theo vị trí bạn viết trong file.

Tailwind có utility-layer ordering/sorting behavior riêng để các tiện ích (utilities) compose predictable hơn, và v4 có logic liên quan số lượng các thuộc tính (properties) cho custom các tiện ích (utilities).

Do đó:
- không dựa vào thứ tự nguồn (source order) local để giải conflict,
- inspect generated CSS nếu behavior quan trọng,
- component override nên dùng kiến trúc (architecture) rõ.

---

# PHẦN V — biến thể (variant) ALGEBRA

## 33. biến thể (variant) không phải text prefix

`hover:` không chỉ “thêm chữ hover vào class”. Nó transform CSS bộ chọn (selector).

`md:` không transform bộ chọn (selector), mà wrap rule trong truy vấn môi trường (media query).

`supports-*:` wrap trong `@supports`.

`group-hover:` tạo ancestor relationship.

`peer-invalid:` tạo sibling relationship.

Một biến thể (variant) vì vậy có thể được hiểu như **hàm (function) biến đổi CSS context**.

---

## 34. biến thể (variant) stacking

```text
dark:md:hover:bg-blue-600
```

là composition của ba transformations:
- dark condition,
- responsive media condition,
- hover bộ chọn (selector).

Khi stacked biến thể (variant) không chạy, gỡ lỗi (debug) từng condition:
- dark trạng thái (state) active?
- vùng nhìn (viewport) đạt md?
- device hỗ trợ hover?
- element thật sự hover?

Đừng coi toàn class như một black box.

---

## 35. `@custom-variant` là reusable condition API

Nếu project lặp bộ chọn (selector):

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

Bây giờ design vocabulary biểu diễn mang tính ngữ nghĩa (semantic) trạng thái (state) thay vì raw bộ chọn (selector).

---

## 36. Naming custom biến thể (variant)

Một project nội bộ có thể dùng:

```text
compact:
midnight:
authenticated:
```

Một design-system package được dùng ngoài project nên cân nhắc không gian tên (namespace):

```text
ds-compact:
ds-brand-a:
```

vì Tailwind core có thể thêm các biến thể (variants) trong tương lai.

---

## 37. `@variant` trong custom CSS

Bạn đã quyết định custom bộ chọn (selector) là rõ nhất:

```css
.third-party-button {
  ...
}
```

nhưng vẫn muốn dark trạng thái (state) giống Tailwind:

```css
.third-party-button {
  @variant dark {
    ...
  }
}
```

V4.3 nâng cấp stacked/compound `@variant`, nên Tailwind biến thể (variant) system có thể được reuse bên trong CSS chứ không chỉ markup.

---

# PHẦN VI — cơ chế phân tầng (cascade) VÀ CONFLICT Ở MỨC MASTER

## 38. Vì sao class order trong HTML không đảm bảo winner?

```html
<div class="px-2 px-4">
```

Nhiều người nghĩ `px-4` viết sau nên thắng. Nhưng CSS cơ chế phân tầng (cascade) không biết thứ tự token trong class attribute như thứ tự nguồn (source order) của các khai báo (declarations).

Browser nhìn stylesheet:

```css
.px-2 { ... }
.px-4 { ... }
```

Rule nào được generate ở vị trí/layer nào mới ảnh hưởng thứ tự nguồn (source order).

Vì thế dynamic class composition không nên dựa vào string append order.

---

## 39. Conflict-aware merge libraries giải quyết vấn đề gì?

Trong component:

```text
base: px-4
caller: px-2
```

Bạn muốn caller override.

Một Tailwind-aware merge helper có thể nhận ra `px-4` và `px-2` thuộc cùng tiện ích (utility) group rồi giữ intended winner trong normalized class string.

Nó không thay CSS engine; nó xử lý conflict trước khi markup render.

Use phù hợp ở reusable component library boundaries.

---

## 40. Prettier Tailwind class sorting không phải conflict engine

Tailwind-aware formatter sắp class để readability ổn định.

Nếu formatter đổi thứ tự text mà UI đổi behavior, bạn đang dựa vào một assumption không an toàn. Hãy kiểm tra conflict/cơ chế phân tầng (cascade).

---

## 41. các lớp phân tầng (cascade layers)

Tailwind v4 dùng native layers:

```text
theme
base
components
utilities
```

Một rule trong các tiện ích (utilities) có layer priority cao hơn components trong normal cơ chế phân tầng (cascade).

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

tiện ích (utility) override component without cuộc chiến độ đặc hiệu (specificity war).

---

## 42. Unlayered CSS có thể gây surprise

Native CSS cơ chế phân tầng (cascade) có behavior đặc biệt khi layered và unlayered author styles coexist. Normal unlayered rule có thể có priority cao hơn layered normal styles.

Nếu bạn import một vendor CSS unlayered sau/bên cạnh Tailwind, tiện ích (utility) có thể không override như bạn dự đoán.

Senior phải inspect:
- layer,
- origin,
- độ đặc hiệu (specificity),
- importance.

Không tăng `!important` ngay.

---

## 43. Per-utility important

V4 preferred:

```text
bg-red-500!
```

Use targeted exception.

Nếu bạn dùng important modifier khắp app, bạn đã phá advantage của predictable layered cơ chế phân tầng (cascade).

---

## 44. Global important strategy

Tailwind có kiến trúc (architecture) options để generate các tiện ích (utilities) important trong một bundle/import scenario.

Đây có thể là chuyển đổi (migration) tool khi host legacy CSS cực kỳ specific.

Nhưng global important làm:
- third-party override khó,
- component theming khó,
- user styles interaction phức tạp.

Hãy xem nó như temporary anti-corruption layer, không phải default.

---

# PHẦN VII — Preflight (lớp reset nền của Tailwind), EMBEDDING VÀ MICROFRONTENDS

## 45. Preflight (lớp reset nền của Tailwind) trong greenfield app

Trong app mới, Preflight (lớp reset nền của Tailwind) giúp:
- normalize defaults,
- predictable border box/reset behavior,
- Tailwind các tiện ích (utilities) có nền consistent.

Ở đây full import là hợp lý.

---

## 46. Preflight (lớp reset nền của Tailwind) trong legacy host

Legacy app có thể assume:
- h1 mặc định lớn,
- ul có bullet,
- button có native border,
- body có margin/reset khác.

Import Tailwind Preflight (lớp reset nền của Tailwind) có thể thay đổi toàn host.

Đừng sửa bằng hàng trăm override trước khi xác nhận root cause là reset collision.

---

## 47. Disable Preflight (lớp reset nền của Tailwind) cho embedded widget

Một widget được inject vào host page nên tránh global reset.

kiến trúc (architecture) có thể:
- import theme,
- import các tiện ích (utilities),
- omit Preflight (lớp reset nền của Tailwind),
- prefix classes,
- phạm vi (scope) phát hiện nguồn (source detection).

Mục tiêu là widget không làm thay đổi host typography/forms.

---

## 48. Prefixing

Prefix giúp:
- tránh class collisions,
- tránh CSS biến (variable) naming collisions tùy import strategy,
- coexist nhiều Tailwind systems.

Cost:
- markup dài,
- docs/examples khác standard,
- component packages phải biết prefix contract.

Dùng cho cô lập (isolation) requirement thật, không phải mặc định.

---

## 49. Microfrontend

Nếu nhiều microfrontend cùng chạy trên một document, ba nguy cơ lớn là:
- nhiều Preflight (lớp reset nền của Tailwind),
- duplicate các biến chủ đề (theme variables),
- layer ordering không thống nhất.

Ba chiến lược phổ biến là:
- share một Tailwind/theme build,
- mỗi app dùng prefixed isolated bundle,
- Shadow DOM (cây DOM đóng gói) cô lập (isolation).

Không có một đáp án universal; quyết định phụ thuộc deployment ownership.

---

# PHẦN VIII — thời gian chạy (runtime) các giá trị (values) VÀ TAILWIND BUILD-TIME

## 50. thời gian chạy (runtime) data không nên trở thành thời gian chạy (runtime) class grammar

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

Class remains static, giá trị (value) thời gian chạy (runtime).

Đây là một trong những boundary pattern quan trọng nhất.

---

## 51. thời gian chạy (runtime) color

```jsx
<div
  style={{
    "--card-bg": color,
  }}
  className="bg-(--card-bg)"
/>
```

Nếu không gian tên (namespace) ambiguous:

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
có thể hợp lý qua inline custom các thuộc tính (properties).

tiện ích (utility) class dùng để consume biến (variable) và kết hợp các trạng thái (states)/responsive.

---

## 53. CSP

Một security policy nghiêm ngặt có thể hạn chế inline style attributes.

Khi đó thời gian chạy (runtime) CSS biến (variable) strategy cần phối hợp CSP:
- nonce,
- safe stylesheet injection,
- predefined class các trạng thái (states),
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

và bạn còn brand A, brand B, độ tương phản cao (high contrast), theme seasonal, class strings phình mạnh.

Lúc đó mang tính ngữ nghĩa (semantic) thời gian chạy (runtime) tokens có thể tốt hơn:

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
- system preference phương án dự phòng (fallback).

Tailwind generated CSS không thể tự quyết định persisted app preference.

---

# PHẦN X — ARIA, DATA, GROUP, PEER, HAS Ở MỨC kiến trúc (architecture)

## 57. ARIA là mang tính ngữ nghĩa (semantic) contract

```text
aria-expanded
aria-selected
aria-pressed
```

không phải chỉ là convenient CSS các trạng thái (states).

Nếu component có true khả năng tiếp cận (accessibility) ngữ nghĩa (semantics), Tailwind aria biến thể (variant) là tuyệt vời.

Nếu trạng thái (state) chỉ là “loading skeleton visible”, dùng `data-loading` có thể đúng hơn `aria-*` tùy ngữ nghĩa (semantics).

---

## 58. Data attribute là presentation/application trạng thái (state) hook

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

`in-*` bỏ explicit marker và tìm ancestor trạng thái (state).

Nó giảm markup nhưng tăng implicit dependency.

Senior chọn:
- shallow/simple → `in-*` okay,
- nested reusable component → named group.

---

## 61. Peer là sibling direction

CSS sibling bộ chọn (selector) không quay ngược.

```html
<input class="peer">
<p class="peer-invalid:block">
```

works.

Nếu paragraph đứng trước input, peer pattern không thể target backward.

Use:
- parent `has-*`,
- DOM restructure,
- application trạng thái (state)
tùy case.

---

## 62. `has-*` không thay business logic

`:has()` nhìn DOM relationship.

Good:
- parent contains checked input,
- form group contains invalid input.

Không dùng `:has()` để suy business trạng thái (state) không được biểu diễn trong DOM. trạng thái (state) business vẫn phải đến từ app model.

---

# PHẦN XI — THIRD-PARTY INTEGRATION

## 63. các biến thể tùy ý (arbitrary variants) phù hợp với integration nhỏ

```text
[&_.vendor-item]:p-2
```

một hoặc vài bộ chọn (selector) là fine.

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

class attribute sẽ trở thành bộ chọn (selector) language khó đọc.

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

Trong case markup không control, `@apply` thực sự có giá trị vì giúp use same Tailwind theme/tiện ích (utility) các giá trị (values).

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

# PHẦN XII — TAILWIND + SCSS / CSS MODULES / Shadow DOM (cây DOM đóng gói)

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

Kỹ thuật thì có thể hoạt động, nhưng gỡ lỗi (debugging) trở nên khó.

Mastery là biết **bỏ bớt layer**.

---

## 68. Tailwind + SCSS

SCSS vẫn mạnh nếu project cần:
- thời điểm biên dịch (compile-time) các map khóa–giá trị (maps),
- các hàm (functions),
- legacy Sass library cấu hình (configuration).

Tailwind v4 đã có:
- theme CSS vars,
- ưu tiên CSS (CSS-first) các tiện ích (utilities),
- native lồng cú pháp (nesting) ecosystem,
- các biến thể (variants).

Greenfield Tailwind project có thể không cần Sass.

Nếu dùng cả hai, hãy chọn một source of truth cho tokens.

---

## 69. Tailwind + CSS Modules

Tailwind:
- atomic styling in markup.

CSS Modules:
- local scoped bộ chọn (selector).

Cả hai coexist tốt khi responsibilities khác nhau.

Nếu CSS Module chỉ có:

```css
.title {
  @apply text-red-500;
}
```

thì bạn đang thêm một abstraction mà không có giá trị (value).

---

## 70. Shadow DOM (cây DOM đóng gói)

Tailwind generated stylesheet ở document không pierce shadow root.

Web Component cần:
- own stylesheet,
- adopted stylesheet,
- custom các thuộc tính (properties),
- `::part`
tùy API.

Tailwind không thay Shadow DOM (cây DOM đóng gói) đóng gói (encapsulation).

---

# PHẦN XIII — PACKAGE DESIGN

## 71. Design-system package có thể ship cái gì?

Một Tailwind hệ thống thiết kế (design system) có thể ship:
- source React/Vue components chứa Tailwind classes,
- compiled CSS,
- theme CSS,
- custom các tiện ích (utilities).

Mỗi lựa chọn có coupling khác nhau.

---

## 72. Ship source components

Consumer build Tailwind dựa trên package source.

Ưu:
- tiện ích (utility) generation theo usage.

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
- các điểm ngắt (breakpoints),
- radii.

Theme package có thể version độc lập với component package.

---

## 75. Version compatibility

Nếu library dùng feature v4.3 như:
- `@container-size`,
- scrollbar các tiện ích (utilities),
- `zoom-*`,
- new functional tiện ích (utility) defaults,

docs nên nói rõ minimum Tailwind version.

Nếu không, consumer v4.1 có thể compile fail hoặc thiếu class.

---

# PHẦN XIV — V4.3 FEATURES VÀ Ý NGHĨA KIẾN TRÚC

## 76. Scrollbar các tiện ích (utilities)

V4.3 đưa scrollbar styling vào core tốt hơn.

Điều này có hai tác dụng:
- giảm nhu cầu community plugin/custom tiện ích (utility),
- làm token thiết kế (design token) integration dễ hơn.

Nhưng scrollbar vẫn là platform UI. Visual behavior đa trình duyệt (cross-browser)/OS không tuyệt đối giống nhau.

---

## 77. `@container-size`

Đây không chỉ là thêm một class. Nó phản ánh CSS platform đã đi sâu hơn vào component-local responsiveness.

Bạn có thể query block size/height-dependent contexts, nhưng size containment có layout consequences. Vì vậy đây là tool advanced.

---

## 78. `zoom-*`

V4.3 tiện ích (utility) cho CSS `zoom` xuất hiện sau khi browser interoperability tốt hơn.

Use cases:
- preview,
- editor canvas,
- document miniature.

Không thay responsive layout.

---

## 79. `tab-*`

`tab-size` trở thành first-class tiện ích (utility).

Use:
- code rendering,
- source editor,
- preformatted blocks.

Một feature nhỏ nhưng minh họa triết lý Tailwind: khi CSS thuộc tính (property) trở nên đủ phổ biến, core tiện ích (utility) API mở rộng để giảm custom CSS.

---

## 80. Stacked/compound `@variant`

Trước đây nhiều developer nghĩ các biến thể (variants) chỉ dành class markup. V4.3 làm custom CSS biến thể (variant) reuse mạnh hơn.

Điều này giúp third-party/custom component CSS vẫn participate cùng trạng thái (state) vocabulary của project.

---

# PHẦN XV — chuyển đổi (migration) V3 → V4 SÂU HƠN

## 81. chuyển đổi (migration) không phải chỉ search-and-replace

V3 kiến trúc (architecture) thường gom:
- content paths,
- theme,
- plugins,
- danh sách ép giữ (safelist)
vào JS config.

V4 đưa nhiều phần về CSS.

Do đó chuyển đổi (migration) là cơ hội hỏi:
- theme tokens public nào?
- source ownership thế nào?
- custom plugin nào giờ chỉ cần `@utility`?
- danh sách ép giữ (safelist) nào là technical debt?
- component nào đang dynamic class synthesis?

---

## 82. Upgrade tool

Official upgrade tooling có thể tự động phần lớn chuyển đổi (migration) mechanics.

Nhưng tool không thể quyết định:
- token ngữ nghĩa (semantic token) design,
- monorepo source ownership,
- public giao diện thành phần (component API),
- custom tiện ích (utility) kiến trúc (architecture).

Run tool, sau đó review.

---

## 83. mức hỗ trợ trình duyệt (browser support) trước khi migrate

Tailwind v4 dùng modern CSS đường cơ sở (baseline) và có minimum browser targets cao hơn v3.

Nếu product còn hỗ trợ browser cũ, upgrade có thể là product decision chứ không chỉ package update.

Đây là lý do framework major version phải được đánh giá cùng browser policy.

---

## 84. `@config` như chuyển đổi (migration) bridge

```css
@config "../../tailwind.config.js";
```

giúp giữ legacy JS config.

Nếu 2 năm sau project vẫn có:
- half CSS theme,
- half JS config,
- half plugins
thì chuyển đổi (migration) chưa hoàn thành về kiến trúc (architecture).

---

## 85. Custom plugin chuyển đổi (migration)

Một v3 plugin chỉ tạo simple tiện ích (utility) có thể chuyển sang `@utility`.

Plugin chỉ tạo biến thể (variant) có thể chuyển sang `@custom-variant`.

Complex JS plugin có logic/package integration vẫn có thể giữ plugin.

Mục tiêu không phải loại bỏ JS plugin bằng mọi giá, mà dùng simplest mechanism.

---

## 86. danh sách ép giữ (safelist) chuyển đổi (migration)

Old danh sách ép giữ (safelist) thường tích tụ “mysterious classes” qua năm tháng.

Khi chuyển sang `@source inline()`, hãy audit từng set:
- source thật sự ở đâu?
- CMS có finite các giá trị (values) không?
- có thể static map khóa–giá trị (map) không?

Đừng mechanically copy universe danh sách ép giữ (safelist).

---

# PHẦN XVI — hiệu năng (performance)

## 87. Tailwind hiệu năng (performance) cần đo ở đâu?

Có ba loại cost:
- source scanning,
- CSS generation/build time,
- final CSS bytes.

Ngoài ra browser vẫn chịu CSS/render cost như bình thường.

Một source tree lớn nhưng candidate ít có cost scanning. Một danh sách ép giữ (safelist) lớn có cost generation/output. Một giant CSS bundle có network/parse cost.

---

## 88. Cold build và incremental build

Khi project lớn, đo:
- first clean build,
- rebuild khi đổi file không tạo candidate mới,
- rebuild khi thêm candidate,
- CI build.

V4 được tối ưu mạnh cho incremental generation, nhưng monorepo/file-watching config sai vẫn có thể dominate.

---

## 89. Unique các giá trị tùy ý (arbitrary values)

```text
top-[117px]
```

one-off không vấn đề.

Data-driven generation của hàng nghìn các giá trị (values) mới là vấn đề.

Pattern đúng cho data:
- CSS biến (variable),
- one static tiện ích (utility) consumer.

---

## 90. `@theme static` và output size

Static theme giúp consumers ngoài tiện ích (utility) system nhìn thấy tất cả tokens.

Nhưng nếu theme có hàng nghìn các biến (variables), output tăng.

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
- Preflight (lớp reset nền của Tailwind),
- theme,
- overlapping các tiện ích (utilities).

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

Không micro-optimize một component; nhưng kiến trúc (architecture) hàng nghìn components thì khác.

---

# PHẦN XVII — gỡ lỗi (debugging) Ở CẤP MASTER

## 93. Bước 1: xác định CSS có tồn tại không

DevTools/Search generated CSS.

Nếu `.bg-brand` không tồn tại:
- scanner,
- theme token,
- source,
- tiện ích (utility) registration.

Nếu tồn tại:
- Tailwind build đã làm việc,
- chuyển sang cơ chế phân tầng (cascade)/layout gỡ lỗi (debugging).

---

## 94. gỡ lỗi (debug) phát hiện nguồn (source detection)

Kiểm tra class có literal complete không.

Kiểm tra file:
- có bị ignored?
- nằm dependency?
- nằm ngoài base path?
- stylesheet bundle này có scan source đó?

Nếu package source, kiểm tra `@source`.

---

## 95. gỡ lỗi (debug) custom theme

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

thì thời gian chạy (runtime) biến (variable) tồn tại nhưng Tailwind không gian tên chủ đề (theme namespace) có thể không đăng ký tiện ích (utility) như bạn tưởng.

---

## 96. gỡ lỗi (debug) custom tiện ích (utility)

Candidate correct nhưng rule không có?

Check:
- `@utility` syntax,
- functional resolver type,
- theme key,
- default/modifier,
- giá trị (value) có resolve được không.

Build-time Tailwind có thể drop khai báo (declaration) không resolve.

---

## 97. gỡ lỗi (debug) biến thể (variant)

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
- bộ chọn (selector) relation.

---

## 98. gỡ lỗi (debug) container

`@md:` không chạy?

Kiểm tra:
- ancestor có `@container`,
- nearest container có đủ width,
- nếu named query thì name đúng,
- `@container-size` chỉ cần cho block-size use case.

Không nhìn vùng nhìn (viewport) width để kết luận container biến thể (variant).

---

## 99. gỡ lỗi (debug) class conflict

Mở computed style.

Tìm thuộc tính (property):

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

## 100. gỡ lỗi (debug) z-index

Nếu tiện ích (utility) rule `z-50` apply mà modal vẫn dưới:
- parent ngữ cảnh xếp chồng (stacking context),
- lớp trên cùng (top layer),
- transform/filter/opacity/cô lập (isolation).

Tailwind không thể phá CSS stacking rules.

---

# PHẦN XVIII — khả năng tiếp cận (accessibility) VÀ UI trạng thái (state) Ở SCALE

## 101. khả năng tiếp cận (accessibility) phải được thiết kế thành hợp đồng thành phần (component contract)

Button component nên có:
- actual `<button>`,
- disabled behavior,
- focus-visible style,
- loading ngữ nghĩa (semantics),
- accessible label khi icon-only.

Tailwind các tiện ích (utilities) làm implementation concise, nhưng contract nằm ở component design.

---

## 102. trạng thái (state) matrix

Một mature component không chỉ test default.

Button có thể có:

```text
variant × size ×
hover/focus/active/disabled/loading
× light/dark
× forced colors
```

Tailwind giúp encode combinations, nhưng trạng thái (state) space vẫn tồn tại.

hồi quy giao diện (visual regression) rất hữu ích.

---

## 103. giảm chuyển động (reduced motion) không phải optional polish

Nếu component có transform/animation lớn:
- add `motion-reduce`,
- hoặc thiết kế motion system global.

User preference là input giống vùng nhìn (viewport)/theme, không phải afterthought.

---

## 104. màu cưỡng bức (forced colors)

Colors có thể bị browser override.

Nếu custom control chỉ biểu diễn selected trạng thái (state) bằng subtle background color, màu cưỡng bức (forced colors) mode có thể mất distinction.

Test actual forced-colors behavior và use mang tính ngữ nghĩa (semantic) border/system color phương án dự phòng (fallback) khi cần.

---

# PHẦN XIX — TESTING

## 105. Static tests

Static tooling có thể bắt:
- invalid class,
- đã ngừng khuyến nghị (deprecated) class,
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

## 107. hồi quy giao diện (visual regression)

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

Prefer mang tính ngữ nghĩa (semantic)/visual tests.

Class snapshot chỉ hợp lý nếu class output là giao diện công khai (public API) hoặc bạn đang test class-merging tiện ích (utility).

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

App map khóa–giá trị (map):

```text
danger → bg-red-500 text-white
```

Bạn giữ:
- design governance,
- scanner visibility,
- security boundary.

---

## 110. giá trị tùy ý (arbitrary value) từ untrusted input

Không concatenate user input vào:

```text
[background:url(...)]
```

hoặc thuộc tính tùy ý (arbitrary property).

Tailwind không sanitize CSS intent.

Whitelist các giá trị (values) hoặc validate data rồi expose qua safe thời gian chạy (runtime) biến (variable).

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

## 112. External token thiết kế (design token) pipeline

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

Nếu sau này team đổi sang CSS Modules hoặc vanilla CSS, giao diện thành phần (component API) vẫn giữ.

Đây là abstraction boundary khỏe mạnh.

---

# PHẦN XXII — KHI NÀO KHÔNG NÊN DÙNG TAILWIND

## 114. Complex rich-text styling

Một article renderer có nested:
- h2,
- blockquote,
- tables,
- code,
- các danh sách (lists),
- links
từ CMS.

Viết class vào từng generated element không practical.

Scoped mang tính ngữ nghĩa (semantic) CSS hoặc typography solution hợp lý hơn.

---

## 115. Third-party DOM sâu

Một editor library có internal DOM tree thay đổi theo version. Một stylesheet integration rõ ràng tốt hơn biến thể tùy ý (arbitrary variant) cực dài trong root class.

---

## 116. CSS feature có syntax phức tạp

Animation keyframes, advanced bộ chọn (selector) hoặc print stylesheet có thể đọc tốt hơn khi viết CSS trực tiếp.

Tailwind hỗ trợ arbitrary/custom API, nhưng không phải mọi CSS nên được convert thành tiện ích (utility).

---

# PHẦN XXIII — MASTER DECISION FRAMEWORK

## 117. Chọn đúng abstraction

Nếu vấn đề là atomic styling với core CSS thuộc tính (property), dùng tiện ích (utility).

Nếu giá trị (value) là exception một lần, dùng giá trị tùy ý (arbitrary value).

Nếu giá trị (value) lặp thành design vocabulary, dùng `@theme`.

Nếu giá trị (value) thay đổi thời gian chạy (runtime), dùng CSS custom thuộc tính (property).

Nếu project thiếu một atomic tiện ích (utility) reusable, dùng `@utility`.

Nếu condition bộ chọn (selector) lặp lại, dùng `@custom-variant`.

Nếu bộ chọn (selector) phức tạp nhưng local/mang tính ngữ nghĩa (semantic), dùng CSS.

Nếu structure + style + trạng thái (state) lặp lại, extract component.

Nếu source nằm ngoài automatic scan, dùng `@source`.

Đây là cách senior tránh “mọi thứ thành tiện ích (utility)” hoặc “mọi thứ thành custom CSS”.

---

# PHẦN XXIV — MASTER LABS

## 118. Lab: scanner

Tạo bốn trường hợp:
- literal `bg-blue-600`,
- dynamic ``bg-${color}-600``,
- static map khóa–giá trị (map),
- class trong workspace package.

Build và inspect generated CSS. Mục tiêu là tự nhìn thấy scanner boundary.

---

## 119. Lab: strict theme

Reset color không gian tên (namespace), chỉ define:
- surface,
- text,
- action,
- danger.

Sau đó thử dùng `bg-blue-500` và quan sát API không còn. Mục tiêu là hiểu `@theme` điều khiển tiện ích (utility) vocabulary.

---

## 120. Lab: functional tiện ích (utility)

Tạo `tab-*` hỗ trợ:
- theme giá trị (value),
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

Mục tiêu là hiểu phát hiện nguồn (source detection) như bundle kiến trúc (architecture).

---

## 122. Lab: thời gian chạy (runtime) CSS biến (variable)

API giá trị (value):
- width,
- color.

Không dùng dynamic arbitrary class.

Bridge bằng CSS vars và static các tiện ích (utilities).

---

## 123. Lab: container component

Cùng một ProfileCard đặt trong:
- sidebar 280px,
- content 600px,
- modal 900px.

Dùng truy vấn vùng chứa (container query) thay vùng nhìn (viewport) điểm ngắt (breakpoint) cho internal layout.

---

## 124. Lab: v3 chuyển đổi (migration)

Lấy project có:
- `tailwind.config.js`,
- content,
- danh sách ép giữ (safelist),
- custom tiện ích (utility) plugin.

Migrate từng phần sang v4 ưu tiên CSS (CSS-first), nhưng giữ hồi quy giao diện (visual regression) snapshots để đảm bảo behavior không đổi.

---

## 125. Lab: embedded widget

Nhúng widget vào một legacy page.

Thử:
- full Tailwind import,
- disable Preflight (lớp reset nền của Tailwind),
- prefix,
- isolate sources.

Quan sát host page bị ảnh hưởng thế nào.

---

# PHẦN XXV — MASTER SELF-CHECK

## 126. Bạn đã đạt mức master khi nào?

Bạn chưa cần nhớ mọi tiện ích (utility). Thay vào đó, bạn nên có thể giải thích bằng lời của mình vì sao Tailwind không generate dynamic interpolated class; tại sao `@theme` là trình biên dịch (compiler) API chứ không chỉ CSS các biến (variables); tại sao theme token rename có thể là breaking change; tại sao source boundaries nên thiết kế theo bundle ownership; vì sao `@container-size` không nên thay toàn bộ `@container`; functional tiện ích (utility) resolver hoạt động ở build time ra sao; vì sao HTML class order không phải CSS thứ tự nguồn (source order); `@reference` có role gì trong isolated stylesheet; tại sao thời gian chạy (runtime) data nên đi qua CSS biến (variable); vì sao ARIA và data attributes không interchangeable về ngữ nghĩa (semantics); và khi nào Tailwind abstraction bắt đầu làm code khó hiểu hơn plain CSS.

Bạn cũng nên gỡ lỗi (debug) được một issue theo pipeline:

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

Hãy đọc component như một hệ thống. Xác định quyền sở hữu hành vi đáp ứng (responsive ownership) thuộc vùng nhìn (viewport) hay container. Xác định trạng thái (state) là native, ARIA, data hay business trạng thái (state). Kiểm tra các giá trị tùy ý (arbitrary values) có đang lặp thành hidden token hay không. Kiểm tra focus, disabled, giảm chuyển động (reduced motion). Với component reusable, xác định class override policy. Với monorepo/package, xác định source scanner có nhìn thấy class hay không. Sau cùng, inspect generated CSS khi có custom tiện ích (utility)/biến thể (variant) hoặc conflict khó.

Đây không phải checklist để tick máy móc; đây là cách senior đọc implementation trước khi PR trở thành technical debt.

---

# PHẦN XXVII — TÀI LIỆU CHÍNH THỨC

Tailwind CSS documentation:

https://tailwindcss.com/docs

Tailwind CSS v4.3 release:

https://tailwindcss.com/blog/tailwindcss-v4-3

các biến chủ đề (theme variables):

https://tailwindcss.com/docs/theme

Detecting classes in source files:

https://tailwindcss.com/docs/detecting-classes-in-source-files

các hàm (functions) and directives:

https://tailwindcss.com/docs/functions-and-directives

thiết kế đáp ứng (responsive design) and các truy vấn vùng chứa (container queries):

https://tailwindcss.com/docs/responsive-design

Styling các tiện ích (utilities):

https://tailwindcss.com/docs/styling-with-utility-classes

Upgrade guide:

https://tailwindcss.com/docs/upgrade-guide

---

---

# PHẦN XXVIII — VERSION BOUNDARIES VÀ CSS MAPPING Ở MỨC MASTER

## 128. Compatibility boundaries: v3 codebase, v4 codebase và package contracts

Một design-system/package không nên chỉ nói “dùng Tailwind”. Nếu source package dựa `@theme`, functional `@utility`, `@container-size` hoặc v4.3 các tiện ích (utilities), consumer minimum version là một phần của package contract. Ngược lại, một package viết cho v3 có thể phụ thuộc JS plugin/config/content ngữ nghĩa (semantics) mà v4 consumer cần chuyển đổi (migration) bridge.

V3 và v4 khác ở ownership model. V3 thường tập trung cấu hình (configuration) trong JavaScript; v4 đưa theme/source/customization vào CSS entrypoint. Vì vậy library chuyển đổi (migration) phải quyết định package ship source components, compiled CSS hay theme-only CSS. Mỗi lựa chọn tạo coupling khác nhau với consumer Tailwind version.

## 129. tiện ích (utility) mapping phải dừng ở CSS khi framework đã hoàn thành nhiệm vụ

Master gỡ lỗi (debugging) cần một “handoff rule”: nếu tiện ích (utility) candidate được generate và computed khai báo (declaration) đúng, dừng gỡ lỗi (debug) Tailwind. Từ thời điểm đó, dùng CSS mô hình tư duy (mental model): lớp phân tầng (cascade layer), khối chứa tham chiếu (containing block), định cỡ nội tại (intrinsic sizing), ngữ cảnh định dạng (formatting context), stacking, overflow, paint/composite. Framework không có layer bí mật phía sau browser.

Điều này đặc biệt quan trọng với `flex-1`, `min-w-0`, `grid-cols-*`, `sticky`, `z-*`, `truncate`, `aspect-*`, container các biến thể (variants) và motion các tiện ích (utilities). Mỗi class chỉ là authoring API cho CSS behavior đã tồn tại. Biết handoff point giúp team phân loại bug nhanh và viết docs/components không thần bí hóa Tailwind.

## 130. Upgrade strategy cho Tailwind production

Khi nâng minor/major version, hãy audit theo ba lớp. Lớp trình biên dịch (compiler) gồm phát hiện ứng viên lớp (candidate detection), source ownership, custom các tiện ích (utilities)/các biến thể (variants) và plugin integration. Lớp generated CSS gồm Preflight (lớp reset nền của Tailwind), layers, các biến chủ đề (theme variables), naming/trạng thái ngừng khuyến nghị (deprecation) và bundle size. Lớp browser gồm hồi quy giao diện (visual regression), khả năng tiếp cận (accessibility) các trạng thái (states) và mức hỗ trợ trình duyệt (browser support) của CSS feature mới.

Tính đến 21/09/2026, Tailwind blog vẫn ghi v4.3 là release framework mới nhất; vì vậy canonical note giữ v4.3 làm đường cơ sở (baseline) nhưng version evolution phải được hiểu theo generation, không hard-code assumption rằng API hôm nay sẽ bất biến. Mỗi lần upgrade, đọc chuyển đổi (migration)/release notes và diff output thay vì chỉ chạy `npm install`.

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

Điểm quan trọng nhất là không để Tailwind trở thành black box. Nếu framework làm bạn khó hiểu CSS hơn, abstraction đang bị dùng sai. Nếu Tailwind giúp design vocabulary rõ hơn, source gần component hơn, responsive/trạng thái (state) declarative hơn và build output predictable hơn, bạn đang dùng nó đúng ở mức senior/master.
