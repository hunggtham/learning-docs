# SCSS — Beginner → Senior Handbook (Modern Dart Sass, 2026)

> **Mục tiêu:** học SCSS như một **thời điểm biên dịch (compile-time) language để author CSS**, không dùng Sass để che việc chưa hiểu CSS.
>
> Tài liệu này nối tiếp:
>
> ```text
> CSS_Beginner_to_Senior_2026.md
> CSS_Master_Supplement_2026.md
> ```
>
> đường cơ sở (baseline) (audit 2026-09):
> - Dùng **Dart Sass 1.104.1** làm mốc tài liệu hiện tại.
> - Ưu tiên **`@use` / `@forward`**.
> - Không xây code mới dựa trên Sass `@import`.
> - Ưu tiên built-in modules: `sass:math`, `sass:color`, `sass:list`, `sass:map`, `sass:string`, `sass:selector`, `sass:meta`.
>
> Ký hiệu:
> - **[CORE]**: phải biết.
> - **[ADV]**: senior nên thành thạo.
> - **[ARCH]**: kiến trúc (architecture) / library design.
> - **⚠ PITFALL**: lỗi thường gặp.
> - **Idiom**: cách viết Sass quen thuộc.
> - **mẫu lập trình (coding pattern)**: pattern implementation.
> - **mẫu thiết kế (design pattern)**: kiến trúc (architecture) pattern.

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ Sass/SCSS được viết theo hướng tiếng Việt dễ hiểu nhưng vẫn giữ từ gốc để tra cứu. Ví dụ: **thời điểm biên dịch (compile-time)**, **thời gian chạy (runtime)**, **phạm vi (scope)**, **không gian tên (namespace)**, **đồ thị mô-đun (module graph)**, **nội suy (interpolation)**, **che khuất biến (shadowing)**, **luồng điều khiển (control flow)** và **hợp nhất bộ chọn (selector unification)**. Những tên directive, function, module và cú pháp Sass nằm trong mã vẫn được giữ nguyên.


# 0. SCSS thực sự là gì?

# 0A. mô hình tư duy (mental model) xuyên suốt: SCSS là chương trình chạy trước CSS

SCSS phải được học như một thời điểm biên dịch (compile-time) language dùng để author/generate CSS. `$variables`, các map khóa–giá trị (maps), loops, các khối trộn tái sử dụng (mixins), các hàm (functions) và đồ thị mô-đun (module graph) được Dart Sass xử lý trước khi browser nhìn thấy trang. Kết quả cuối cùng chỉ là CSS. Vì vậy Sass biến (variable) không cơ chế phân tầng (cascade), không inherit và không thay đổi thời gian chạy (runtime); CSS custom thuộc tính (property) thì có thể tham gia cơ chế phân tầng (cascade), kế thừa (inheritance) và thời gian chạy (runtime) overrides.

Trục học canonical của SCSS là:

```text
Sass values / variables
→ nesting + selector generation
→ mixins / functions như compile-time abstraction
→ lists / maps / control flow để generate CSS
→ @use / @forward tạo module graph
→ partials + entry points tổ chức source
→ @extend như selector unification, không phải OOP inheritance
→ architecture + public API
→ compiler deprecations / migration
→ CSS output quality + compile performance
```

Khi đọc SCSS, luôn hỏi trình biên dịch (compiler) sẽ emit CSS gì, bao nhiêu rule, bộ chọn (selector) nào và ở vị trí nào. khối trộn tái sử dụng (mixin) include nhiều lần có thể duplicate các khai báo (declarations). Loop có thể tạo hàng nghìn rules. lồng cú pháp (nesting) sâu có thể sinh bộ chọn (selector) độ đặc hiệu (specificity) cao và coupling với DOM. Source ngắn hơn không đồng nghĩa output tốt hơn.

các biến (variables) phù hợp với thời điểm biên dịch (compile-time) calculation/generation. CSS custom các thuộc tính (properties) phù hợp với thời gian chạy (runtime) theme, cascade-based component contracts và các giá trị (values) cần override trong DevTools/thời gian chạy (runtime). các khối trộn tái sử dụng (mixins) nên mô tả khai báo (declaration) set hoặc content wrapper có parameterization rõ. các hàm (functions) nên trả giá trị (value) và tránh tác dụng phụ (side effect). các map khóa–giá trị (maps) hữu ích khi thực sự biểu diễn structured cấu hình (configuration); map khóa–giá trị (map) lồng sâu chỉ để “gom mọi thứ” thường biến API thành khó dùng.

Modern hệ mô-đun (module system) là `@use` và `@forward`. `@use` tạo không gian tên (namespace), phạm vi (scope) members trong file dùng và load module một lần. `@forward` tạo facade/bề mặt công khai (public surface). các file thành phần (partials) chỉ là tổ chức source; chúng không tự tạo kiến trúc mô-đun (module architecture) nếu code vẫn nối bằng legacy `@import`. Sass `@import` và global built-ins đã đã ngừng khuyến nghị (deprecated) từ Dart Sass 1.80.0 nên code mới không nên xây trên global không gian tên (namespace) cũ.

`@extend` cũng không phải kế thừa (inheritance) kiểu Java. Sass thực hiện hợp nhất bộ chọn (selector unification) để các bộ chọn (selector) mở rộng cùng nhận rules, vì thế output có thể xuất hiện xa nơi gọi và khó dự đoán. Placeholder `%foo` có use case, nhưng khối trộn tái sử dụng (mixin), tiện ích (utility)/composition hoặc CSS kiến trúc (architecture) thường explicit hơn. SCSS tốt phải làm CSS output dễ hiểu hơn, không che CSS đi.


Sass là stylesheet language compile thành CSS.

SCSS là syntax của Sass có hình thức gần CSS:

```scss
$brand: #2563eb;

.button {
  color: $brand;

  &:hover {
    color: white;
  }
}
```

Compile thành:

```css
.button {
  color: #2563eb;
}

.button:hover {
  color: white;
}
```

## mô hình tư duy (mental model) quan trọng

```text
SCSS source
→ Sass compiler
→ CSS output
→ Browser
```

Browser **không biết**:
- `$variable`,
- `@mixin`,
- `@function`,
- Sass map khóa–giá trị (map),
- Sass loop.

Browser chỉ nhận CSS cuối.

## Senior rule

Nếu behavior phụ thuộc thời gian chạy (runtime):
- theme,
- cơ chế phân tầng (cascade),
- kế thừa (inheritance),
- container,
- user preference,

thường CSS custom thuộc tính (property) phù hợp hơn Sass biến (variable).

---

# 1. SCSS vs CSS Custom các thuộc tính (properties) [CORE]

## Sass biến (variable)

```scss
$space-4: 1rem;
```

thời điểm biên dịch (compile-time).

Sau compile:

```css
/* $space-4 biến mất */
```

## CSS custom thuộc tính (property)

```css
:root {
  --space-4: 1rem;
}
```

Tồn tại thời gian chạy (runtime).

Có:
- cơ chế phân tầng (cascade),
- kế thừa (inheritance),
- thời gian chạy (runtime) override,
- DevTools visibility.

## Pattern — thời điểm biên dịch (compile-time) constants + thời gian chạy (runtime) tokens

```scss
$prefix: "app";

:root {
  --color-brand: #2563eb;
}
```

Sass:
- generate structure,
- build token tables,
- tiện ích (utility) generation.

CSS các biến (variables):
- theme/thời gian chạy (runtime) hợp đồng thành phần (component contract).

---

# 2. Cài đặt và CLI [CORE]

Node project:

```bash
npm install --save-dev sass
```

Compile:

```bash
npx sass src/styles.scss dist/styles.css
```

Watch:

```bash
npx sass --watch src:dist
```

Compressed output:

```bash
npx sass src/styles.scss dist/styles.css --style=compressed
```

bản đồ mã nguồn (source map) behavior tùy CLI/build integration.

## Production rule

Trong app hiện đại thường Sass chạy thông qua:
- Vite,
- webpack,
- Angular CLI,
- framework bundler.

Không cần tự chạy CLI nếu công cụ build (build tool) đã quản lý.

---

# 3. File Naming: các file thành phần (partials) [CORE]

File private/internal thường bắt đầu `_`:

```text
_variables.scss
_mixins.scss
_button.scss
```

Load:

```scss
@use "variables";
```

Không cần viết:
- `_variables.scss`,
- extension `.scss`.

## Idiom

```text
styles/
├─ _tokens.scss
├─ _mixins.scss
├─ components/
│  ├─ _button.scss
│  └─ _card.scss
└─ main.scss
```

---

# 4. Comments [CORE]

Silent comment:

```scss
// only in SCSS source
```

Không xuất CSS.

Loud comment:

```scss
/* may be emitted */
```

Có thể xuất CSS tùy output mode.

License/preserved comment:

```scss
/*!
 * License
 */
```

Thường được giữ kể cả compressed output.

---

# 5. Sass các biến (variables) [CORE]

```scss
$brand: #2563eb;
$radius: 0.75rem;
$spacing-unit: 0.25rem;
```

Use:

```scss
.button {
  border-radius: $radius;
}
```

## Naming

Hyphen và underscore lịch sử được Sass coi tương đương trong identifiers:

```scss
$font-size
$font_size
```

có thể refer cùng name ngữ nghĩa (semantics).

**Không lợi dụng điều này.** Chọn một convention: thường kebab-case.

---

# 6. biến (variable) phạm vi (scope) [CORE]

Top-level:

```scss
$brand: blue;

.button {
  color: $brand;
}
```

Local:

```scss
.component {
  $gap: 1rem;
  gap: $gap;
}
```

Local biến (variable) không nên assume available global.

---

# 7. che khuất biến (shadowing) [ADV]

```scss
$color: blue;

.card {
  $color: red;
  color: $color;
}

.link {
  color: $color;
}
```

Output:
- card red,
- link blue.

## Senior note

che khuất biến (shadowing) quá nhiều khiến SCSS khó reason.

Ưu tiên:
- local biến (variable) tên rõ,
- module các không gian tên (namespaces).

---

# 8. `!default` [CORE][ARCH]

Library biến (variable):

```scss
$button-radius: 0.5rem !default;
```

Ý nghĩa:
> set giá trị (value) nếu biến (variable) chưa được configured/set theo module ngữ nghĩa (semantics).

Dùng cho **configurable library defaults**.

Không dùng `!default` cho mọi biến (variable).

---

# 9. `!global` [ADV]

```scss
$flag: false;

@mixin enable {
  $flag: true !global;
}
```

Có thể modify global biến (variable).

## ⚠ PITFALL

`!global` tạo hidden trạng thái có thể thay đổi (mutable state).

Senior rule:
- tránh trong application SCSS,
- ưu tiên các hàm (functions) return giá trị (value),
- module config rõ ràng.

---

# 10. Sass Data Types [CORE]

Sass các giá trị (values) gồm:

```text
numbers
strings
colors
lists
maps
booleans
null
calculation values
function references
```

---

# 11. Numbers & Units [CORE]

```scss
$size: 16px;
$ratio: 1.5;
$angle: 45deg;
$duration: 200ms;
```

Sass hiểu units mathematically.

```scss
@use "sass:math";

$half: math.div(20px, 2);
```

Result:

```text
10px
```

---

# 12. Division — dùng `math.div()` [CORE]

Không viết Sass arithmetic mới:

```scss
$half: 20px / 2;
```

Dùng:

```scss
@use "sass:math";

$half: math.div(20px, 2);
```

Lý do:
- `/` trong CSS ngày càng là separator.
- Grid, modern colors, ratios dùng `/`.

CSS output vẫn có thể chứa slash:

```scss
.item {
  grid-row: span 3 / 7;
}
```

---

# 13. Numeric Operators [CORE]

```scss
$a: 10px + 5px;
$b: 10px - 2px;
$c: 4 * 3;
```

Division:
```scss
math.div(...)
```

Comparisons:

```scss
$a > $b
$a >= $b
$a == $b
$a != $b
```

---

# 14. Unit Compatibility [ADV]

Sass có unit arithmetic.

Valid:

```scss
1in + 96px
```

vì convertible.

Không phải mọi units compatible:

```text
px + s
```

là conceptual error.

Useful `sass:math`:

```scss
math.compatible(1cm, 10mm)
```

---

# 15. Strings [CORE]

Quoted:

```scss
$name: "Inter";
```

Unquoted:

```scss
$display: block;
```

nội suy (interpolation):

```scss
.#{$name} {}
```

## Rule

Không quote mọi identifier nếu CSS cần identifier.

---

# 16. nội suy (interpolation) `#{}` [CORE]

bộ chọn (selector):

```scss
$variant: danger;

.button-#{$variant} {
  color: red;
}
```

thuộc tính (property):

```scss
$side: left;

margin-#{$side}: 1rem;
```

String:

```scss
$url: "hero";

background-image:
  url("/images/#{$url}.jpg");
```

## ⚠ PITFALL

nội suy (interpolation) là powerful nhưng dễ biến Sass thành template spaghetti.

Đừng generate arbitrary các bộ chọn (selectors) nếu mang tính ngữ nghĩa (semantic) class rõ hơn.

---

# 17. Booleans [CORE]

```scss
$enabled: true;
$disabled: false;
```

Used:

```scss
@if $enabled {
  ...
}
```

---

# 18. `null` [CORE]

```scss
$value: null;
```

Sass thường không emit khai báo (declaration) nếu giá trị (value) là `null`.

```scss
$border: null;

.card {
  border: $border;
}
```

Có thể compile mà khai báo (declaration) không xuất.

## Pattern — Optional khai báo (declaration)

```scss
@mixin box($radius: null) {
  @if $radius != null {
    border-radius: $radius;
  }
}
```

---

# 19. các danh sách (lists) [CORE]

Space-separated:

```scss
$spacing: 4px 8px 16px;
```

Comma-separated:

```scss
$fonts: Inter, Arial, sans-serif;
```

Bracketed:

```scss
$list: [a, b, c];
```

Slash-separated các giá trị (values) cũng tồn tại.

## Important

Sass danh sách (list) không giống JS Array hoàn toàn.

- separator là metadata,
- bracketed/unbracketed matter,
- individual giá trị (value) cũng có list-like behavior.

---

# 20. `sass:list` [CORE]

```scss
@use "sass:list";

$items: red, green, blue;
```

Common:

```scss
list.length($items)
list.nth($items, 1)
list.append($items, orange)
list.index($items, green)
list.join($a, $b)
list.separator($items)
```

Modern module API ưu tiên không gian tên (namespace).

---

# 21. danh sách (list) Indexing [CORE]

Sass historically indexes từ **1**, không phải 0.

```scss
list.nth($items, 1)
```

→ first item.

Negative index có thể refer từ cuối tùy hàm (function) ngữ nghĩa (semantics).

## ⚠ PITFALL

Dev từ JS/Java dễ nhầm 0-based.

---

# 22. các map khóa–giá trị (maps) [CORE]

```scss
$colors: (
  primary: #2563eb,
  danger: #dc2626,
  success: #16a34a
);
```

map khóa–giá trị (map) = key/giá trị (value) collection.

Use:

```scss
@use "sass:map";

.button {
  color: map.get($colors, primary);
}
```

---

# 23. `sass:map` [CORE]

Common:

```scss
map.get($map, $key)
map.has-key($map, $key)
map.keys($map)
map.values($map)
map.merge($map1, $map2)
map.remove($map, $keys...)
map.set(...)
map.deep-merge(...)
map.deep-remove(...)
```

Availability của deep APIs cần Dart Sass hiện đại.

---

# 24. Nested các map khóa–giá trị (maps) [CORE/ADV]

```scss
$theme: (
  colors: (
    primary: #2563eb,
    danger: #dc2626
  ),
  radius: (
    sm: .25rem,
    md: .5rem
  )
);
```

Get:

```scss
map.get($theme, colors, primary)
```

Modern Dart Sass hỗ trợ nested keys ở module các hàm (functions) phù hợp.

---

# 25. map khóa–giá trị (map) as cấu hình (configuration) [ARCH]

```scss
$button-sizes: (
  sm: (
    padding: .375rem .625rem,
    font-size: .875rem
  ),
  md: (
    padding: .5rem .875rem,
    font-size: 1rem
  )
);
```

Generate styles:

```scss
@each $name, $config in $button-sizes {
  .button--#{$name} {
    padding: map.get($config, padding);
    font-size: map.get($config, font-size);
  }
}
```

## Senior rule

map khóa–giá trị (map) tốt khi:
- finite design data,
- generation có quy luật.

map khóa–giá trị (map) xấu khi:
- recreate entire DOM/component tree as cấu hình (configuration).

---

# 26. Colors [CORE]

Sass understands colors.

```scss
$brand: #2563eb;
```

Modern CSS color spaces:
- rgb,
- hsl,
- hwb,
- lab/lch,
- oklab/oklch,
- display-p3,
- others.

Modern Sass color APIs phải xét color space rõ hơn trước đây.

---

# 27. `sass:color` [CORE/ADV]

```scss
@use "sass:color";
```

Common modern APIs:

```scss
color.adjust(...)
color.scale(...)
color.change(...)
color.channel(...)
color.to-space(...)
color.is-powerless(...)
```

Example:

```scss
$hover:
  color.scale(
    #2563eb,
    $lightness: -12%,
    $space: oklch
  );
```

## ⚠ Legacy

Các global/legacy các hàm (functions) như:
- `lighten()`,
- `darken()`,
- old channel getters,

không nên là default cho code mới.

---

# 28. Sass vs CSS Color các hàm (functions) [ADV]

Nếu muốn thời gian chạy (runtime) color derived từ CSS biến (variable):

```css
background:
  color-mix(
    in oklab,
    var(--brand),
    black 10%
  );
```

Sass không thể thời điểm biên dịch (compile-time) resolve thời gian chạy (runtime) custom thuộc tính (property).

## Pattern

```text
Static design generation → Sass color APIs
Runtime theme color       → CSS color functions
```

---

# 29. lồng cú pháp (nesting) [CORE]

```scss
.card {
  padding: 1rem;

  .title {
    font-weight: 700;
  }
}
```

Output:

```css
.card {
  padding: 1rem;
}

.card .title {
  font-weight: 700;
}
```

## Senior rule

lồng cú pháp (nesting) không phải mục tiêu của Sass.

lồng cú pháp (nesting) chỉ nên giúp:
- các trạng thái (states),
- pseudo các bộ chọn (selectors),
- local slots,
- contextual rules.

---

# 30. Parent bộ chọn (selector) `&` [CORE]

```scss
.button {
  &:hover {}
  &:focus-visible {}
}
```

Output:

```css
.button:hover {}
.button:focus-visible {}
```

biến thể (variant):

```scss
.button {
  &--danger {}
}
```

Output:

```css
.button--danger {}
```

---

# 31. Parent bộ chọn (selector) Context [ADV]

```scss
.button {
  .theme-dark & {
    color: white;
  }
}
```

Output:

```css
.theme-dark .button {}
```

## ⚠ PITFALL

Context inversion dễ tạo hidden coupling.

Theme hiện đại thường tốt hơn qua CSS các biến (variables):

```css
[data-theme="dark"] {
  --button-bg: ...;
}
```

---

# 32. thuộc tính (property) lồng cú pháp (nesting) [ADV/LEGACY AWARENESS]

Sass có syntax nested các thuộc tính (properties) lịch sử:

```scss
font: {
  family: Inter;
  size: 1rem;
}
```

Có thể compile thành:
- `font-family`,
- `font-size`.

## Recommendation

Không ưu tiên syntax này cho code mới.

Plain các khai báo (declarations) dễ search/read hơn.

---

# 33. Mixed các khai báo (declarations) + Nested Rules [CORE]

Modern Sass đã align behavior với CSS lồng cú pháp (nesting):
các khai báo (declarations) giữ thứ tự xuất hiện ngay cả khi interleaved với nested rules.

```scss
.example {
  color: red;

  &--serious {
    font-weight: bold;
  }

  font-weight: normal;
}
```

Đừng assume Sass tự hoist các khai báo (declarations) như historical versions.

## Senior rule

Viết các khai báo (declarations) có order rõ:
- base các khai báo (declarations) trước,
- nested các bộ chọn (selectors)/trạng thái (state) sau,

nếu không có lý do cần interleave.

---

# 34. Placeholder các bộ chọn (selectors) `%` [ADV]

```scss
%control-base {
  border: 1px solid;
  border-radius: .5rem;
}
```

Extend:

```scss
.button {
  @extend %control-base;
}
```

Placeholder tự nó không emit bộ chọn (selector) nếu không được extend.

---

# 35. `@extend` [ADV]

```scss
.error {
  color: red;
}

.validation-error {
  @extend .error;
}
```

Sass **merges các bộ chọn (selectors)**, không copy các khai báo (declarations) đơn giản.

Output có thể:

```css
.error,
.validation-error {
  color: red;
}
```

---

# 36. `@extend` mô hình tư duy (mental model) [ADV]

`@extend` nói:

> bộ chọn (selector) A phải behave như một instance của bộ chọn (selector) B.

Nó là hợp nhất bộ chọn (selector unification)/rewriting.

Không nghĩ:

> copy block CSS của B vào A.

---

# 37. `@extend` Pitfalls [ADV]

Có thể:
- tạo bộ chọn (selector) output lớn,
- nối các bộ chọn (selectors) xa nhau,
- coupling khó thấy,
- khó predict trong legacy global imports.

## Senior rule

Ưu tiên:
1. shared class,
2. khối trộn tái sử dụng (mixin),
3. tiện ích (utility),
4. token,

trước `@extend` nếu ngữ nghĩa (semantics) không thật sự là bộ chọn (selector) kế thừa (inheritance).

---

# 38. Placeholder + Extend Pattern [ADV]

Nếu cần extend, placeholder thường an toàn hơn extend concrete class:

```scss
%button-base {
  display: inline-flex;
  align-items: center;
}

.button {
  @extend %button-base;
}
```

Không làm `.button` trở thành mang tính ngữ nghĩa (semantic) extension của public class khác.

---

# 39. các khối trộn tái sử dụng (mixins) [CORE]

```scss
@mixin visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
}
```

Use:

```scss
.sr-only {
  @include visually-hidden;
}
```

---

# 40. khối trộn tái sử dụng (mixin) Arguments [CORE]

```scss
@mixin square($size) {
  width: $size;
  height: $size;
}
```

```scss
.avatar {
  @include square(3rem);
}
```

---

# 41. Default Arguments [CORE]

```scss
@mixin focus-ring(
  $width: 3px,
  $offset: 3px
) {
  outline: $width solid currentColor;
  outline-offset: $offset;
}
```

---

# 42. Keyword Arguments [CORE]

```scss
@include focus-ring(
  $offset: 4px,
  $width: 2px
);
```

Useful khi:
- nhiều optional params,
- boolean params,
- API clarity.

## Library compatibility

Renaming public khối trộn tái sử dụng (mixin) argument có thể là breaking change vì callers dùng keyword arguments.

---

# 43. Arbitrary Arguments `$args...` [ADV]

```scss
@mixin box-shadow($shadows...) {
  box-shadow: $shadows;
}
```

Call:

```scss
@include box-shadow(
  0 1px 2px #0002,
  0 8px 24px #0002
);
```

---

# 44. Passing các danh sách (lists)/các map khóa–giá trị (maps) as Arguments [ADV]

```scss
$args: 1rem, 2rem;

@include some-mixin($args...);
```

map khóa–giá trị (map) có thể expand keyword arguments:

```scss
$options: (
  $size: 2rem,
  $radius: .5rem
);

@include box($options...);
```

Use carefully; explicit arguments thường readable hơn.

---

# 45. Content Blocks `@content` [CORE/ADV]

```scss
@mixin hover-capable {
  @media (hover: hover) {
    &:hover {
      @content;
    }
  }
}
```

Use:

```scss
.button {
  @include hover-capable {
    transform: translateY(-1px);
  }
}
```

---

# 46. Content Block Arguments [ADV]

```scss
@mixin media-types($types...) {
  @each $type in $types {
    @media #{$type} {
      @content($type);
    }
  }
}
```

Caller:

```scss
@include media-types(screen, print)
using ($type) {
  ...
}
```

Advanced library technique.

---

# 47. Content phạm vi (scope) [ADV]

`@content` block is lexically scoped:
- sees các biến (variables) at include site,
- không automatically see khối trộn tái sử dụng (mixin) local các biến (variables) như dynamic phạm vi (scope).

## Design lesson

khối trộn tái sử dụng (mixin) content block giống thời điểm biên dịch (compile-time) higher-order style block.

---

# 48. các hàm (functions) [CORE]

```scss
@function rem($px, $base: 16px) {
  @return math.div($px, $base) * 1rem;
}
```

Use:

```scss
.title {
  font-size: rem(24px);
}
```

Need:

```scss
@use "sass:math";
```

---

# 49. hàm (function) vs khối trộn tái sử dụng (mixin) [CORE]

## hàm (function)

Return **giá trị (value)**:

```scss
@function space($step) {
  @return $step * .25rem;
}
```

## khối trộn tái sử dụng (mixin)

Emit **styles/rules**:

```scss
@mixin stack($gap) {
  display: flex;
  flex-direction: column;
  gap: $gap;
}
```

## Rule

```text
Value transformation → function
Style generation     → mixin
```

---

# 50. hàm (function) Design [ADV]

Good hàm (function):
- deterministic,
- return giá trị (value),
- validation rõ,
- tên nói mang tính ngữ nghĩa (semantic) intent.

Bad:

```scss
@function do-everything(...) { ... }
```

Không build mini application language trong Sass nếu CSS/custom các thuộc tính (properties) đủ.

---

# 51. Private Members [CORE][ARCH]

Names bắt đầu `_` hoặc `-` historically treated private module members:

```scss
$_internal-scale: ...;

@function _helper(...) {}
```

Consumer module không nên access.

## Pattern

```text
Public:
$tokens
@mixin button
@function space

Private:
$_raw-data
@function _normalize
```

---

# 52. `@if` / `@else` [CORE]

```scss
@mixin surface($elevated: false) {
  background: white;

  @if $elevated {
    box-shadow: 0 8px 24px #0002;
  }
}
```

Else:

```scss
@if $theme == dark {
  ...
} @else {
  ...
}
```

---

# 53. Truthiness [CORE]

Trong Sass:
- `false`,
- `null`

là falsey.

Nhiều giá trị (value) khác truthy, kể cả:
- `0`,
- empty strings/các danh sách (lists) theo Sass ngữ nghĩa (semantics).

Đừng assume JS truthiness.

---

# 54. `@each` [CORE]

danh sách (list):

```scss
$sizes: sm, md, lg;

@each $size in $sizes {
  .text-#{$size} {
    ...
  }
}
```

map khóa–giá trị (map):

```scss
@each $name, $value in $colors {
  .text-#{$name} {
    color: $value;
  }
}
```

---

# 55. `@for` [CORE]

Exclusive `to`:

```scss
@for $i from 1 to 4 {
  ...
}
```

→ 1,2,3.

Inclusive `through`:

```scss
@for $i from 1 through 4 {
  ...
}
```

→ 1,2,3,4.

---

# 56. `@while` [ADV]

```scss
$i: 1;

@while $i <= 3 {
  .order-#{$i} {
    order: $i;
  }

  $i: $i + 1;
}
```

## Senior rule

`@while` hiếm khi cần.

Nếu `@each`/`@for` đủ, dùng chúng vì predictable hơn.

---

# 57. Loop Generation Pitfall [ADV]

Có thể generate:

```scss
@for $i from 1 through 1000 {
  .m-#{$i} { ... }
}
```

Nhưng compile được ≠ nên làm.

Concern:
- CSS size,
- dead các tiện ích (utilities),
- API explosion.

## mẫu thiết kế (design pattern)

Generate từ **bounded design scale**, không từ mọi possible number.

---

# 58. Error Handling: `@error` [CORE/ADV]

```scss
@function spacing($step) {
  @if $step < 0 {
    @error "spacing step must be >= 0";
  }

  @return $step * .25rem;
}
```

Good library API:
- fail fast,
- message useful.

---

# 59. `@warn` [ADV]

```scss
@warn "Deprecated mixin. Use new-name().";
```

Use:
- chuyển đổi (migration) notice,
- suspicious but compilable input.

Không spam warning cho normal usage.

---

# 60. `@debug` [CORE]

```scss
@debug $tokens;
```

Useful:
- inspect các map khóa–giá trị (maps)/các danh sách (lists),
- hàm (function) development.

Không xem output format như stable production API.

---

# 61. `@use` — Modern hệ mô-đun (module system) [CORE]

```scss
@use "tokens";
```

Members accessed by không gian tên (namespace):

```scss
.button {
  color: tokens.$brand;
}
```

khối trộn tái sử dụng (mixin):

```scss
@include tokens.some-mixin;
```

hàm (function):

```scss
width: tokens.some-function(...);
```

---

# 62. Module Loaded Once [CORE]

`@use` module:
- execute once,
- CSS emit once,
- shared module identity.

Đây là khác biệt lớn so với legacy `@import`.

---

# 63. không gian tên (namespace) Alias [CORE]

```scss
@use "design/tokens" as t;
```

```scss
.button {
  color: t.$brand;
}
```

Good khi module name dài.

---

# 64. `as *` [ADV]

```scss
@use "tokens" as *;
```

Members vào local không gian tên (namespace).

## ⚠ PITFALL

Làm mất provenance:

```scss
color: $brand;
```

Không biết `$brand` từ đâu.

Senior rule:
- application small file có thể dùng có kiểm soát,
- library/large codebase nên giữ không gian tên (namespace).

---

# 65. Module cấu hình (configuration) `with` [CORE][ARCH]

Module:

```scss
// _theme.scss
$brand: #2563eb !default;
$radius: .5rem !default;
```

Consumer:

```scss
@use "theme" with (
  $brand: rebeccapurple,
  $radius: 1rem
);
```

## Important

Module must be configured **before first load**.

Module is loaded once.

---

# 66. cấu hình (configuration) Contract [ARCH]

Configurable biến (variable):
- giao diện công khai (public API),
- nên có `!default`,
- naming stable,
- docs rõ.

Đừng expose every internal constant.

---

# 67. `@forward` [CORE][ARCH]

Library facade:

```scss
// _index.scss
@forward "tokens";
@forward "mixins";
@forward "functions";
```

Consumer:

```scss
@use "design-system";
```

Có một entrypoint thay vì 20 imports.

---

# 68. `@forward` vs `@use` [CORE]

`@forward`:
- re-export public members cho downstream.

`@use`:
- use members trong current module.

Nếu file cần cả hai:

```scss
@forward "theme";
@use "theme";
```

Thường forward trước để cấu hình (configuration) flow predictable.

---

# 69. Forward Prefix [ADV]

```scss
@forward "list" as list-*;
```

Module member:

```scss
reset
```

Downstream:

```scss
library.list-reset
```

Useful:
- giao diện công khai (public API) clarity,
- avoid collisions.

---

# 70. `show` / `hide` [ADV]

```scss
@forward "internal"
  show $brand, button;
```

Hoặc:

```scss
@forward "internal"
  hide _helper;
```

Use giao diện công khai (public API) curation.

---

# 71. Forward cấu hình (configuration) [ADV][ARCH]

Facade có thể set opinionated defaults:

```scss
@forward "library" with (
  $radius: .75rem !default
);
```

Downstream vẫn có thể override nếu forward config cho phép.

Pattern:
```text
Core library
→ opinionated facade
→ application config
```

---

# 72. Index Files [CORE]

Directory:

```text
tokens/
├─ _color.scss
├─ _spacing.scss
└─ _index.scss
```

`_index.scss`:

```scss
@forward "color";
@forward "spacing";
```

Consumer:

```scss
@use "tokens";
```

---

# 73. Load Paths [ADV]

trình biên dịch (compiler) có thể configure load paths.

Thay vì:

```scss
@use "../../../shared/tokens";
```

có thể:

```scss
@use "shared/tokens";
```

cấu hình (configuration) tùy:
- CLI,
- bundler,
- JS API.

## Senior rule

Avoid ambiguous module resolution.
Document load paths.

---

# 74. Built-in Modules Overview [CORE]

```scss
@use "sass:math";
@use "sass:string";
@use "sass:color";
@use "sass:list";
@use "sass:map";
@use "sass:selector";
@use "sass:meta";
```

Global built-ins là legacy direction.
Dùng namespaced module APIs cho code mới.

---

# 75. `sass:math` [CORE]

Useful:

```text
math.div
math.max
math.min
math.round
math.ceil
math.floor
math.abs
math.clamp
math.compatible
math.is-unitless
math.unit
math.percentage
```

Có thêm constants/các hàm (functions) nâng cao tùy Dart Sass version.

Example:

```scss
@use "sass:math";

@function fluid-step($min, $max, $ratio) {
  @return $min + ($max - $min) * $ratio;
}
```

---

# 76. CSS `min()` vs Sass `math.min()` [ADV]

CSS:

```css
width: min(100%, 70rem);
```

thời gian chạy (runtime) browser calculation.

Sass:

```scss
math.min(10px, 20px)
```

thời điểm biên dịch (compile-time) numeric hàm (function).

## mô hình tư duy (mental model)

```text
Known at compile time → sass:math
Depends on layout     → CSS math function
```

---

# 77. `sass:string` [ADV]

Common:

```text
string.quote
string.unquote
string.index
string.insert
string.slice
string.to-upper-case
string.to-lower-case
string.unique-id
```

Use cases:
- generated names,
- parsing limited thời điểm biên dịch (compile-time) tokens,
- library các tiện ích (utilities).

Don't build complex text processing engine in Sass.

---

# 78. `sass:selector` [ADV]

Powerful bộ chọn (selector) engine API:

```text
selector.is-superselector
selector.append
selector.extend
selector.nest
selector.parse
selector.replace
selector.unify
selector.simple-selectors
```

Example:

```scss
@use "sass:selector";

$result:
  selector.unify(
    ".alert",
    ".danger"
  );
```

Useful for library-level bộ chọn (selector) metaprogramming.

---

# 79. bộ chọn (selector) các hàm (functions) — Use Carefully [ADV]

If you frequently need dynamic bộ chọn (selector) manipulation:
- kiến trúc (architecture) may be too clever.

Good:
- framework/library abstraction.

Bad:
- normal app component.

---

# 80. `sass:meta` [ADV]

Reflection/introspection.

Useful APIs include concepts:

```text
meta.type-of
meta.inspect
meta.module-variables
meta.module-functions
meta.module-mixins
meta.function-exists
meta.mixin-exists
meta.variable-exists
meta.global-variable-exists
meta.get-function
meta.call
meta.apply
meta.keywords
meta.load-css
```

Availability depends Dart Sass version.

---

# 81. `meta.type-of()` [ADV]

```scss
@use "sass:meta";

@debug meta.type-of(10px); // number
@debug meta.type-of(#fff); // color
```

Useful validation.

---

# 82. Dynamic hàm (function) References [ADV]

```scss
$fn: meta.get-function("some-function");
$result: meta.call($fn, ...);
```

Useful:
- generic token transforms,
- plugin-like thời điểm biên dịch (compile-time) patterns.

Use sparingly.

---

# 83. `meta.load-css()` [ADV]

Load module CSS dynamically in khối trộn tái sử dụng (mixin)/context.

Use case:
- conditional CSS emission,
- advanced library kiến trúc (architecture).

Not replacement for normal `@use`.

---

# 84. Sass kiến trúc (architecture) — 7-1 Awareness [ARCH]

Classic 7-1 pattern:

```text
abstracts/
base/
components/
layout/
pages/
themes/
vendors/
main.scss
```

Useful as historical organization model.

But don't apply mechanically.

Modern modules allow more feature/component-oriented structure.

---

# 85. Recommended Modern SCSS Structure [ARCH]

```text
styles/
├─ settings/
│  ├─ _tokens.scss
│  ├─ _config.scss
│  └─ _index.scss
│
├─ tools/
│  ├─ _functions.scss
│  ├─ _mixins.scss
│  └─ _index.scss
│
├─ base/
│  ├─ _reset.scss
│  └─ _typography.scss
│
├─ layout/
│  ├─ _stack.scss
│  ├─ _cluster.scss
│  └─ _container.scss
│
├─ components/
│  ├─ _button.scss
│  ├─ _card.scss
│  └─ _dialog.scss
│
├─ utilities/
│  └─ _index.scss
│
└─ main.scss
```

---

# 86. Feature-oriented Structure [ARCH]

Trong component app:

```text
features/
├─ profile/
│  ├─ _tokens.scss
│  ├─ _profile-card.scss
│  └─ _index.scss
└─ checkout/
   └─ ...
```

Good khi:
- component/domain ownership quan trọng hơn global style categories.

---

# 87. Entry Point Pattern [ARCH]

`main.scss` chỉ compose modules:

```scss
@use "base/reset";
@use "base/typography";
@use "layout";
@use "components";
@use "utilities";
```

Đừng đặt 1000 lines component CSS trong `main.scss`.

---

# 88. Library Facade Pattern [ARCH]

```text
design-system/
├─ _index.scss
├─ _tokens.scss
├─ _mixins.scss
├─ _functions.scss
└─ components/
```

`_index.scss`:

```scss
@forward "tokens";
@forward "mixins";
@forward "functions";
```

Consumer:

```scss
@use "design-system" as ds;
```

---

# 89. Sass Token map khóa–giá trị (map) Pattern [CORE/ARCH]

```scss
$spacing: (
  0: 0,
  1: .25rem,
  2: .5rem,
  3: .75rem,
  4: 1rem,
  6: 1.5rem
);
```

hàm (function):

```scss
@function space($step) {
  @if not map.has-key($spacing, $step) {
    @error "Unknown spacing step: #{$step}";
  }

  @return map.get($spacing, $step);
}
```

---

# 90. Generate CSS các biến (variables) from Sass map khóa–giá trị (map) [CORE/ARCH]

```scss
@use "sass:map";

$colors: (
  brand: #2563eb,
  danger: #dc2626,
  surface: #fff
);

:root {
  @each $name, $value in $colors {
    --color-#{$name}: #{$value};
  }
}
```

Output thời gian chạy (runtime) tokens.

## Pattern

```text
Sass data source
→ generated CSS custom properties
→ browser runtime theming
```

---

# 91. Nested Token Generation [ADV]

```scss
$tokens: (
  color: (
    brand: #2563eb,
    danger: #dc2626
  ),
  space: (
    1: .25rem,
    2: .5rem
  )
);
```

Có thể viết recursive generator.

Nhưng recursion belongs more in master supplement.

---

# 92. tiện ích (utility) Generation Pattern [CORE/ADV]

```scss
$spaces: (
  1: .25rem,
  2: .5rem,
  4: 1rem
);

@each $name, $value in $spaces {
  .gap-#{$name} {
    gap: $value;
  }
}
```

Senior concern:
- CSS output size,
- design-system phạm vi (scope),
- naming consistency.

---

# 93. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin) Pattern [CORE]

Config:

```scss
$breakpoints: (
  sm: 36rem,
  md: 48rem,
  lg: 64rem
);
```

khối trộn tái sử dụng (mixin):

```scss
@mixin up($name) {
  $value: map.get($breakpoints, $name);

  @if $value == null {
    @error "Unknown breakpoint #{$name}";
  }

  @media (width >= $value) {
    @content;
  }
}
```

Use:

```scss
.card {
  @include up(md) {
    display: grid;
  }
}
```

---

# 94. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin) — Senior Caveat [ADV]

Không biến mọi truy vấn môi trường (media query) thành opaque khối trộn tái sử dụng (mixin).

Native:

```scss
@media (width >= 48rem) {}
```

đôi khi rõ hơn.

khối trộn tái sử dụng (mixin) đáng dùng khi:
- enforce design điểm ngắt (breakpoint) contract,
- shared ngữ nghĩa (semantics),
- validation.

---

# 95. Responsive Modern Pattern [ADV]

Sass điểm ngắt (breakpoint) map khóa–giá trị (map) cho **page các điểm ngắt (breakpoints)**.

các truy vấn vùng chứa (container queries) vẫn nên viết CSS:

```scss
.card-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  ...
}
```

Không compile container dimensions thành vùng nhìn (viewport) kiến trúc (architecture).

---

# 96. khối trộn tái sử dụng (mixin) for Repeated khai báo (declaration) Set [CORE]

Good:

```scss
@mixin focus-ring {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Bad:

```scss
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

không hẳn luôn bad, nhưng tiện ích (utility)/layout class có thể reusable thời gian chạy (runtime) tốt hơn nếu dùng nhiều.

## Decision

```text
Need CSS class composition? → utility/layout primitive
Need compile-time inline style set? → mixin
```

---

# 97. truy vấn môi trường (media query) Content khối trộn tái sử dụng (mixin) Idiom [CORE]

```scss
@mixin reduced-motion {
  @media (prefers-reduced-motion: reduce) {
    @content;
  }
}
```

```scss
.motion {
  animation: pulse 1s infinite;

  @include reduced-motion {
    animation: none;
  }
}
```

Readable nếu team dùng convention này.

---

# 98. trạng thái (state) khối trộn tái sử dụng (mixin) phản mẫu (anti-pattern) [ADV]

Avoid:

```scss
@mixin hover-active-focus-disabled-loading {
  ...
}
```

Nếu khối trộn tái sử dụng (mixin) abstracts mang tính ngữ nghĩa (semantic) trạng thái (state) quá sâu, output khó inspect.

CSS các trạng thái (states) nên remain visible trong component source khi có thể.

---

# 99. Function-based Scale Pattern [ADV]

```scss
@function pow-scale($base, $ratio, $step) {
  $value: $base;

  @for $i from 1 through $step {
    $value: $value * $ratio;
  }

  @return $value;
}
```

Could generate type scale.

But static token thiết kế (design tokens) may be easier to review.

Senior asks:
> generation adds giá trị (value) or hides design decisions?

---

# 100. BEM + SCSS [CORE/ADV]

```scss
.card {
  &__title {}
  &__body {}
  &--featured {}
}
```

Works.

## ⚠ Caveat

Renaming `.card` changes generated các bộ chọn (selectors):
- convenient,
- but searchability less direct.

For large teams, explicit các bộ chọn (selectors) may sometimes be clearer:

```scss
.card {}
.card__title {}
.card__body {}
```

SCSS does not require BEM lồng cú pháp (nesting).

---

# 101. CUBE / tiện ích (utility) Composition + SCSS [ARCH]

SCSS can define:
- design scales,
- tiện ích (utility) generator,
- component tools.

But actual kiến trúc (architecture) may prefer:
- composition classes,
- các tiện ích (utilities),
- blocks,
- exceptions.

Don't let Sass lồng cú pháp (nesting) push project toward deeply coupled BEM trees.

---

# 102. SCSS mẫu thiết kế (design pattern) — thời điểm biên dịch (compile-time) API [ARCH]

Treat module members as API:

Public:
```text
$configuration !default
mixins
functions
forwarded tokens
```

Private:
```text
helper functions
raw maps
implementation mixins
temporary data
```

Consumers should not depend on private internals.

---

# 103. SCSS mẫu thiết kế (design pattern) — Facade Module [ARCH]

Internal modules:

```text
_color.scss
_spacing.scss
_type.scss
```

Facade:

```scss
@forward "color";
@forward "spacing";
@forward "type";
```

Consumer:

```scss
@use "tokens";
```

Equivalent kiến trúc (architecture) concept:
- Facade Pattern.

---

# 104. SCSS mẫu thiết kế (design pattern) — cấu hình (configuration) Object [ARCH]

Instead of 20 globals:

```scss
$theme: (
  radius: .5rem,
  density: comfortable,
  features: (
    shadows: true,
    gradients: false
  )
);
```

các hàm (functions) access config.

But module cấu hình (configuration) via explicit các biến (variables) may be clearer for giao diện công khai (public API).

Use map khóa–giá trị (map) when cấu hình (configuration) is naturally hierarchical.

---

# 105. SCSS mẫu thiết kế (design pattern) — Generator [ARCH]

Data:

```scss
$utilities: (...);
```

Generator:

```scss
@mixin generate-utilities($config) {
  ...
}
```

Output:
```text
CSS utility classes
```

Useful for:
- internal tiện ích (utility) framework,
- token-derived APIs.

Risk:
- framework within framework.

---

# 106. SCSS mẫu thiết kế (design pattern) — Adapter [ARCH]

Third-party library expects config:

```scss
$library-primary: ...;
```

Your system uses:
```scss
$tokens: (...);
```

Create adapter module:

```scss
$library-primary:
  map.get($tokens, color, brand);
```

Keep vendor mapping isolated.

---

# 107. SCSS mẫu thiết kế (design pattern) — Anti-Corruption Layer [ARCH]

Do not let Bootstrap/vendor names spread across app token system.

```text
App semantic tokens
→ vendor adapter
→ third-party Sass config
```

This keeps replacement possible later.

---

# 108. `@at-root` [ADV]

Moves nested rule out of current lồng cú pháp (nesting) context.

```scss
.component {
  @at-root .global-helper {
    ...
  }
}
```

Advanced query forms can control which at-rules/các bộ chọn (selectors) stay.

## Use cases

- library bộ chọn (selector) generation,
- escape contextual lồng cú pháp (nesting).

## ⚠

Frequent `@at-root` means lồng cú pháp (nesting) kiến trúc (architecture) may be wrong.

---

# 109. At-rule lồng cú pháp (nesting) [CORE]

```scss
.card {
  @media (width >= 48rem) {
    display: grid;
  }
}
```

Sass handles nested at-rules.

Modern CSS lồng cú pháp (nesting) now supports much of this natively, so Sass giá trị (value) here is less unique than before.

---

# 110. Unknown At-rules [CORE]

Sass generally passes through CSS at-rules it doesn't specially interpret:

```scss
@container ...
@layer ...
@scope ...
@property ...
@starting-style ...
```

SCSS should remain CSS-compatible.

## Senior rule

Don't invent Sass workaround for native CSS feature if Sass already passes it through.

---

# 111. CSS Custom các thuộc tính (properties) in SCSS [CORE]

```scss
:root {
  --brand: #{$brand};
}
```

nội suy (interpolation) may be needed when embedding Sass các giá trị (values) in custom thuộc tính (property) text, depending expression/giá trị (value) context.

Example:

```scss
$brand: #2563eb;

:root {
  --brand: #{$brand};
}
```

---

# 112. Custom thuộc tính (property) Gotcha [ADV]

CSS custom thuộc tính (property) các giá trị (values) are parsed with CSS custom-property ngữ nghĩa (semantics).

When mixing Sass các biến (variables)/các hàm (functions):
- nội suy (interpolation) may be necessary,
- preserve thời gian chạy (runtime) syntax like `var()`, `calc()`, `color-mix()`.

Don't accidentally make Sass evaluate something intended for browser.

---

# 113. Sass Calculations vs CSS Calculations [ADV]

Modern Sass understands CSS calculations more intelligently.

Examples:

```scss
width: calc(100% - 2rem);
font-size: clamp(1rem, 2vw, 2rem);
```

Sass may simplify only when mathematically safe/known.

Senior rule:
> Keep layout-dependent math in CSS thời gian chạy (runtime).

---

# 114. Sass Color 4 Awareness [ADV]

Modern Sass supports CSS Color 4 spaces.

Legacy assumptions:
```text
every color convertible to simple RGB/HSL
```

are no longer universally safe.

Prefer:
```scss
color.channel(..., $space: ...)
color.adjust(..., $space: ...)
color.scale(..., $space: ...)
color.to-space(...)
```

when color-space ngữ nghĩa (semantics) matter.

---

# 115. trạng thái ngừng khuyến nghị (deprecation): Sass `@import` [MUST]

Legacy:

```scss
@import "variables";
@import "mixins";
```

Problems:
- global không gian tên (namespace),
- repeated execution,
- unclear provenance,
- extend coupling.

Modern:

```scss
@use "variables";
@use "mixins";
```

For library facade:

```scss
@forward ...
```

---

# 116. Global Built-in hàm (function) trạng thái ngừng khuyến nghị (deprecation) [MUST]

Legacy:

```scss
map-get($map, key);
lighten($color, 10%);
```

Modern:

```scss
@use "sass:map";
@use "sass:color";

map.get($map, key);
color.scale(...);
```

Benefits:
- provenance,
- less CSS hàm (function) collision,
- future compatibility.

---

# 117. Legacy Slash Division [MUST]

Legacy:

```scss
$half: $size / 2;
```

Modern:

```scss
@use "sass:math";

$half: math.div($size, 2);
```

---

# 118. Legacy Color các hàm (functions) [MUST]

Avoid building new APIs around:

```text
red()
green()
blue()
hue()
saturation()
lightness()
lighten()
darken()
```

Use `sass:color` modern APIs with explicit color-space thinking.

---

# 119. Sass Migrator [CORE/ADV]

Official Sass Migrator helps migrate:
- `@import` → hệ mô-đun (module system),
- division,
- other deprecations/features supported by migrator.

Typical command ecosystem:

```bash
sass-migrator module ...
```

Exact installation/flags should be checked against current docs.

## Rule

chuyển đổi (migration) tool:
- accelerates mechanical changes,
- does not replace kiến trúc (architecture) review.

---

# 120. trạng thái ngừng khuyến nghị (deprecation) Warnings [CORE]

Treat warnings as future build failures.

CI strategy:
```text
warnings visible
→ inventory
→ migrate
→ optionally fatal for selected deprecations
```

Don't permanently silence all deprecations.

---

# 121. Dependency Warnings [ADV]

Build can distinguish:
- your code,
- dependency code.

Useful to silence noisy dependency warnings selectively while keeping first-party warnings.

But update dependencies rather than hiding warnings forever.

---

# 122. các bản đồ mã nguồn (source maps) [CORE]

SCSS gỡ lỗi (debugging) needs mapping:

```text
compiled CSS line
↔ SCSS source line
```

Bundlers usually generate các bản đồ mã nguồn (source maps) in dev.

Without them:
- DevTools points to generated CSS,
- kiến trúc (architecture) gỡ lỗi (debugging) harder.

---

# 123. Output Styles [CORE]

Typical:
- expanded,
- compressed.

Development:
```text
expanded + source map
```

Production:
```text
compressed/minified via pipeline
```

Your bundler may minify after Sass.

---

# 124. Sass Does Not Autoprefix [MUST]

Sass trình biên dịch (compiler):
- compiles Sass to CSS.

It does **not inherently replace**:
- Autoprefixer,
- browserslist-based transforms,
- CSS minifier,
- PostCSS pipeline.

Typical:

```text
SCSS
→ Sass
→ PostCSS/Autoprefixer
→ minifier
→ CSS
```

depending stack.

---

# 125. SCSS + PostCSS [ADV]

Complementary:

Sass:
- modules,
- các map khóa–giá trị (maps),
- các hàm (functions),
- thời điểm biên dịch (compile-time) generation.

PostCSS ecosystem:
- vendor prefixes,
- transformations,
- lint/plugins,
- build processing.

Don't treat them as competitors by default.

---

# 126. SCSS + CSS Modules [ADV]

Example:

```text
Button.module.scss
```

Two layers:

```text
SCSS
→ compile CSS
→ CSS Modules scopes class names
```

Still can use:
- `@use`,
- tokens,
- các hàm (functions).

Senior note:
CSS Modules already gives scoping; don't overbuild BEM naming solely for collision avoidance.

---

# 127. SCSS + Component Frameworks [ADV]

React/Vue/Svelte/etc:

Prefer styles close to ownership.

Possible:
```text
component.scss
Component.module.scss
feature/_index.scss
```

Global Sass:
- tokens,
- tools,
- base.

Component Sass:
- component-specific CSS.

---

# 128. Sass các biến (variables) vs token thiết kế (design tokens) [MUST]

Bad:

```scss
$blue: #2563eb;
```

everywhere.

Better:

```scss
$color-action-primary: #2563eb;
```

Best for thời gian chạy (runtime) themes:
generate:

```css
--color-action-primary: ...
```

## Token layers

```text
primitive Sass data
→ semantic token
→ CSS custom property
→ component token
```

---

# 129. Theme Generation Pattern [ADV]

```scss
$themes: (
  light: (
    surface: white,
    text: #111
  ),
  dark: (
    surface: #111,
    text: #f5f5f5
  )
);

@each $theme-name, $tokens in $themes {
  [data-theme="#{$theme-name}"] {
    @each $token, $value in $tokens {
      --#{$token}: #{$value};
    }
  }
}
```

Good when themes static thời điểm biên dịch (compile-time) set.

---

# 130. Theme Generation Caveat [ADV]

If theme data comes thời gian chạy (runtime)/server/user:
Sass cannot help after compile.

Use CSS các biến (variables)/thời gian chạy (runtime) JS/server CSS.

---

# 131. Validation hàm (function) Pattern [ADV]

```scss
@function token($map, $key) {
  @if not map.has-key($map, $key) {
    @error "Unknown token `#{$key}`.";
  }

  @return map.get($map, $key);
}
```

Fail fast prevents silent inconsistent design.

---

# 132. Recursive map khóa–giá trị (map) Access Pattern [ADV]

Could write helper:

```scss
@function get-in($map, $keys...) {
  $current: $map;

  @each $key in $keys {
    $current: map.get($current, $key);
  }

  @return $current;
}
```

But modern `sass:map` nested APIs may already solve this.

Don't reinvent standard các hàm (functions).

---

# 133. Recursive CSS biến (variable) Generator [ADV]

Concept:

```scss
@mixin emit-vars(
  $map,
  $prefix: ""
) {
  @each $key, $value in $map {
    $name:
      if(
        $prefix == "",
        $key,
        "#{$prefix}-#{$key}"
      );

    @if meta.type-of($value) == "map" {
      @include emit-vars($value, $name);
    } @else {
      --#{$name}: #{$value};
    }
  }
}
```

Use:
```scss
:root {
  @include emit-vars($tokens);
}
```

Master supplement sẽ nói deeper về recursion/meta/deprecations.

---

# 134. bộ chọn (selector) Explosion [ADV]

lồng cú pháp (nesting) + `@extend` + loops có thể multiply các bộ chọn (selectors).

Example risk:

```scss
@each ...
  @extend ...
```

Output may be far larger than source.

Always inspect compiled CSS.

---

# 135. Source Size ≠ Output Size [MUST]

10 lines SCSS có thể generate 10,000 lines CSS.

Senior review:
- compile output,
- bundle report,
- coverage.

SCSS abstraction cost phải đo ở **CSS output**.

---

# 136. khối trộn tái sử dụng (mixin) Duplication Cost [ADV]

khối trộn tái sử dụng (mixin):

```scss
@mixin card-base {
  padding: 1rem;
  border: 1px solid;
}
```

Included 100 times:
→ các khai báo (declarations) emitted 100 times.

Shared class:
```css
.card-base {}
```
→ one ruleset, but markup composes class.

Tradeoff:
- CSS size,
- ngữ nghĩa (semantics),
- thời gian chạy (runtime) class composition,
- đóng gói (encapsulation).

---

# 137. Extend vs khối trộn tái sử dụng (mixin) vs tiện ích (utility) [MUST]

## `@extend`

bộ chọn (selector) relationship.

## `@mixin`

khai báo (declaration)/rule duplication at compile time.

## tiện ích (utility) class

Shared thời gian chạy (runtime) class.

Decision:

```text
Same semantic selector identity? → extend maybe
Need generated declarations?     → mixin
Reusable runtime behavior?       → utility/class
```

---

# 138. SCSS Code Review Checklist [SENIOR]

Check:

```text
Does Sass add real value?
Could native CSS do this more clearly?
Are module namespaces clear?
Any deprecated APIs?
Any global mutable state?
Nested > 3 levels?
Map too complex?
Generated CSS too large?
Mixin duplicated heavily?
@extend output predictable?
Public configuration documented?
Runtime concerns wrongly solved compile-time?
```

---

# 139. lồng cú pháp (nesting) Depth Budget [SENIOR]

Suggested:

```text
0–2 levels: normal
3: review
4+: strong smell
```

Not hard rule.

các trạng thái (states)/at-rules don't count the same as DOM descendant lồng cú pháp (nesting) conceptually.

---

# 140. giao diện công khai (public API) Stability [ARCH]

If building Sass library:

Changing:
- public biến (variable),
- khối trộn tái sử dụng (mixin) name,
- hàm (function) name,
- keyword argument name,
- forwarded prefix,
- default cấu hình (configuration),

can be breaking change.

Treat Sass module like code library.

---

# 141. mang tính ngữ nghĩa (semantic) Versioning [ARCH]

Library releases:

```text
PATCH
bugfix output without API break

MINOR
new backward-compatible mixin/function/token

MAJOR
rename/remove/change public config/output contract
```

CSS visual changes may also be breaking even if Sass API same.

---

# 142. Naming Public các khối trộn tái sử dụng (mixins) [ARCH]

Bad:
```scss
@mixin blue-shadow-12 {}
```

Better:
```scss
@mixin elevated-surface {}
```

Expose ngữ nghĩa (semantics), not current implementation details.

---

# 143. Avoid Boolean Explosion [ADV]

Bad:

```scss
@mixin button(
  $small: false,
  $rounded: false,
  $danger: false,
  $loading: false,
  $outline: false
) {}
```

Combinations explode.

Better:
- separate biến thể (variant)/trạng thái (state) tokens,
- các map khóa–giá trị (maps),
- CSS các bộ chọn (selectors)/data attributes,
- smaller các khối trộn tái sử dụng (mixins).

---

# 144. Sass Isn't a Component máy trạng thái (state machine) [MUST]

thời gian chạy (runtime) các trạng thái (states):
```text
open
loading
selected
disabled
error
```

belong in HTML/JS attributes/classes.

Sass can generate style APIs but cannot know thời gian chạy (runtime) trạng thái (state).

---

# 145. Prefer Native CSS Features [SENIOR]

Historically Sass solved:
- các biến (variables),
- lồng cú pháp (nesting),
- color transforms,
- calculations.

Modern CSS now has:
- custom các thuộc tính (properties),
- native lồng cú pháp (nesting),
- `color-mix`,
- `calc`,
- `min/max/clamp`,
- các truy vấn vùng chứa (container queries).

Use Sass only where thời điểm biên dịch (compile-time) abstraction adds giá trị (value).

---

# 146. When Sass Is Still Strong [SENIOR]

Excellent use cases:

```text
module organization
library public APIs
token data processing
bounded utility generation
compile-time validation
maps/lists
mixins with content blocks
functions
third-party Sass configuration
build-time adapters
```

---

# 147. When Sass Is Overkill [SENIOR]

If project only needs:

```text
nesting
variables
simple imports
```

modern native CSS + bundler may be enough.

Do not choose Sass only from habit.

---

# 148. Beginner Practice

Build:
1. các biến (variables),
2. nested các bộ chọn (selectors),
3. các khối trộn tái sử dụng (mixins),
4. simple hàm (function),
5. map khóa–giá trị (map),
6. `@each`,
7. `@use`.

Project:
- button các biến thể (variants) from map khóa–giá trị (map),
- spacing các tiện ích (utilities),
- compile to CSS.

---

# 149. Intermediate Practice

Build:
1. token module,
2. điểm ngắt (breakpoint) khối trộn tái sử dụng (mixin),
3. component facade,
4. biến chủ đề (theme variable) generator,
5. CSS Modules + SCSS,
6. chuyển đổi (migration) from `@import`.

---

# 150. Senior Practice

Build:
1. Sass library giao diện công khai (public API),
2. configurable module,
3. `@forward show/hide/prefix`,
4. vendor adapter,
5. token validation,
6. tiện ích (utility) generator with output budget,
7. các bản đồ mã nguồn (source maps)/quy trình build (build pipeline),
8. deprecation-clean CI.

---

# 151. 30-Day SCSS Roadmap

## Days 1–3
- syntax,
- các biến (variables),
- data types,
- lồng cú pháp (nesting).

## Days 4–6
- các danh sách (lists),
- các map khóa–giá trị (maps),
- built-in modules.

## Days 7–9
- các khối trộn tái sử dụng (mixins),
- arguments,
- `@content`.

## Days 10–12
- các hàm (functions),
- luồng điều khiển (control flow),
- validation.

## Days 13–15
- `@use`,
- không gian tên (namespace),
- cấu hình (configuration).

## Days 16–18
- `@forward`,
- facade,
- public/private API.

## Days 19–21
- token system,
- generators.

## Days 22–23
- CSS các biến (variables) integration,
- thời gian chạy (runtime)/thời điểm biên dịch (compile-time) boundary.

## Days 24–25
- kiến trúc (architecture),
- component ownership.

## Days 26–27
- legacy chuyển đổi (migration),
- deprecations.

## Day 28
- output/hiệu năng (performance) inspection.

## Day 29
- library API review.

## Day 30
- final design-system project.

---

# 152. Senior Self-Test

Bạn phải trả lời được:

1. Sass biến (variable) khác CSS custom thuộc tính (property) thế nào?
2. SCSS compile ở thời điểm nào?
3. Vì sao `@import` đã ngừng khuyến nghị (deprecated)?
4. `@use` load module mấy lần?
5. `@forward` khác `@use`?
6. `!default` dùng cho gì?
7. không gian tên (namespace) giúp gì?
8. Vì sao `as *` nên hạn chế?
9. Public/private Sass member là gì?
10. khối trộn tái sử dụng (mixin) khác hàm (function)?
11. `@content` dùng khi nào?
12. Keyword args ảnh hưởng API compatibility thế nào?
13. `@extend` thực sự làm gì?
14. Placeholder bộ chọn (selector) có lợi gì?
15. `math.div()` vì sao thay `/`?
16. `sass:map` khác old `map-get`?
17. Modern color API vì sao cần explicit space?
18. map khóa–giá trị (map) phù hợp cho loại data nào?
19. Khi nào loop generation là phản mẫu (anti-pattern)?
20. Source SCSS nhỏ có đảm bảo CSS nhỏ?
21. khối trộn tái sử dụng (mixin) có duplication cost gì?
22. tiện ích (utility) class khác khối trộn tái sử dụng (mixin) ra sao?
23. Sass config và thời gian chạy (runtime) theme khác nhau?
24. `@forward show/hide` giải quyết gì?
25. Forward prefix dùng khi nào?
26. Sass không thay Autoprefixer vì sao?
27. CSS Modules và SCSS có conflict không?
28. Native CSS lồng cú pháp (nesting) có làm Sass vô dụng không?
29. Khi nào nên chọn plain CSS thay Sass?
30. Sass library giao diện công khai (public API) nên version thế nào?

---

# 153. Cheat Sheet

```scss
@use "sass:math";
@use "sass:map";
@use "sass:color";

// variable
$space-unit: .25rem;

// map
$spaces: (
  1: .25rem,
  2: .5rem,
  4: 1rem
);

// function
@function space($step) {
  @if not map.has-key($spaces, $step) {
    @error "Unknown spacing: #{$step}";
  }

  @return map.get($spaces, $step);
}

// mixin
@mixin focus-ring(
  $width: 3px,
  $offset: 3px
) {
  outline: $width solid currentColor;
  outline-offset: $offset;
}

// content mixin
@mixin up($width) {
  @media (width >= $width) {
    @content;
  }
}

// generation
@each $name, $value in $spaces {
  .gap-#{$name} {
    gap: $value;
  }
}

// CSS runtime token
:root {
  --space-card: #{space(4)};
}

.card {
  gap: var(--space-card);

  &:focus-visible {
    @include focus-ring;
  }

  @include up(48rem) {
    display: grid;
  }
}
```

---

# 154. Recommended Production kiến trúc (architecture)

```text
SCSS
│
├─ settings
│  ├─ primitive design data
│  └─ library config
│
├─ tools
│  ├─ functions
│  └─ mixins
│
├─ CSS runtime tokens
│
├─ base
│
├─ layout primitives
│
├─ components
│
├─ utilities
│
└─ entrypoint
```

Rules:

```text
@use namespaces
@forward facades
no Sass @import
no global built-in API
no slash division
low nesting
bounded generators
runtime state stays in CSS/HTML/JS
```

---

# 155. References

Official Sass:
- https://sass-lang.com/documentation/
- https://sass-lang.com/documentation/at-rules/use/
- https://sass-lang.com/documentation/at-rules/forward/
- https://sass-lang.com/documentation/at-rules/mixin/
- https://sass-lang.com/documentation/at-rules/function/
- https://sass-lang.com/documentation/modules/
- https://sass-lang.com/documentation/breaking-changes/
- https://sass-lang.com/documentation/breaking-changes/import/
- https://sass-lang.com/documentation/breaking-changes/slash-div/
- https://sass-lang.com/documentation/breaking-changes/color-functions/

---

---

# 156. SCSS kiến trúc (architecture) — thiết kế đồ thị mô-đun (module graph) trước khi thiết kế folder [SENIOR/ARCH]

Một codebase SCSS lớn không nên bắt đầu từ câu hỏi “dùng 7-1 hay chia folder thế nào?”, mà từ câu hỏi **module nào sở hữu API nào và module nào được phép emit CSS**. Folder chỉ là representation của dependency graph. Nếu mọi file có thể truy cập global các biến (variables)/các khối trộn tái sử dụng (mixins) và emit rules khi import, structure nhìn đẹp nhưng kiến trúc (architecture) vẫn global.

Modern Sass với `@use` và `@forward` cho phép bạn thiết kế graph rõ hơn. Một tool module chứa các biến (variables)/các hàm (functions)/các khối trộn tái sử dụng (mixins) nên lý tưởng không emit CSS. Một style module cố ý emit base/component rules. Một facade module dùng `@forward` để expose bề mặt công khai (public surface) ổn định. Entry point `@use`s các facade/style modules theo dependency order mà application cần.

```text
_tokens.scss      → values / configuration
_math.scss        → functions, no CSS output
_button-tools.scss→ mixins, no CSS output
_button.scss      → emits component CSS
_index.scss       → @forward public API
app.scss          → entry point, @use style/facade modules
```

Điểm quan trọng là “file thành phần (partial)” không tự làm code modular. `_tokens.scss` vẫn có thể là global soup nếu được kéo bằng legacy `@import`. Module boundary đến từ không gian tên (namespace), private members, single evaluation và giao diện công khai (public API) discipline của `@use`/`@forward`.

## giao diện công khai (public API) và cấu hình (configuration) boundary

Library Sass nên expose ít thứ hơn internal implementation. Nếu consumer cần configure brand color, spacing scale hoặc feature flag thời điểm biên dịch (compile-time), expose `$variable: default !default` có chủ đích và configure qua `@use ... with (...)`. Đừng expose mọi internal map khóa–giá trị (map) chỉ vì “sau này có thể cần”; khi consumer phụ thuộc vào shape của nested map khóa–giá trị (map), refactor nội bộ biến thành breaking change.

`@forward ... show/hide` hoặc prefixing giúp facade chỉ xuất phần ổn định. Private members nên thực sự private. Public khối trộn tái sử dụng (mixin)/hàm (function) name, parameter ngữ nghĩa (semantics) và generated CSS contract đều là API cần versioning.

## Side-effect CSS phải có ownership

Một common bug là `@use` một helper module chỉ để gọi hàm (function) nhưng module đó cũng emit reset/components. Vì module load một lần, duplication được giảm so với `@import`, nhưng tác dụng phụ (side effect) vẫn tồn tại. Tách tool modules khỏi style modules làm dependency graph predictable hơn và giúp library consumer dùng logic mà không kéo CSS ngoài ý muốn.

## `@extend` không phải kế thừa (inheritance) kiến trúc (architecture)

`@extend` hợp nhất các bộ chọn (selectors) trong trình biên dịch (compiler). Nó không copy các khai báo (declarations) như khối trộn tái sử dụng (mixin) và không tạo type hierarchy như Java. Vì hợp nhất bộ chọn (selector unification) có thể tạo output ở nơi xa call site và coupling giữa modules, hãy giới hạn `@extend` cho placeholder contracts rất controlled. Nếu bạn cần parameterization, khối trộn tái sử dụng (mixin) thường rõ hơn; nếu chỉ cần shared visual primitives, composition/tiện ích (utility) class hoặc native CSS layer/token thường dễ dự đoán hơn.

## Sass vs native CSS responsibility

Sass mạnh ở thời điểm biên dịch (compile-time) generation: transform data structures, validate config, tạo repetitive API và package reusable authoring tools. Native CSS mạnh ở thời gian chạy (runtime): custom các thuộc tính (properties), các lớp phân tầng (cascade layers), lồng cú pháp (nesting), các truy vấn vùng chứa (container queries), `:has()`, thuộc tính logic (logical properties) và theming theo environment/trạng thái (state). Một kiến trúc (architecture) hiện đại nên để thời gian chạy (runtime) concerns ở CSS nếu browser đã giải được trực tiếp, thay vì generate hàng trăm các biến thể (variants) thời điểm biên dịch (compile-time) bằng loops.

SCSS tốt không làm CSS biến mất khỏi mô hình tư duy (mental model). Nó làm source dễ maintain hơn trong khi generated CSS vẫn nhỏ, độ đặc hiệu (specificity) thấp và dễ inspect.

---

# Kết luận

SCSS senior không phải người viết lồng cú pháp (nesting)/khối trộn tái sử dụng (mixin) nhiều nhất.

SCSS senior biết:

```text
what should happen at compile time
vs
what should remain runtime CSS
```

và dùng Sass để:

```text
organize
validate
generate
encapsulate
configure
```

mà không làm compiled CSS:
- khó đọc,
- quá lớn,
- coupling,
- đã ngừng khuyến nghị (deprecated),
- khó migrate.

mô hình tư duy (mental model) cuối:

```text
CSS knowledge first
→ Sass as authoring language
→ module API
→ controlled generation
→ inspect compiled output
```
