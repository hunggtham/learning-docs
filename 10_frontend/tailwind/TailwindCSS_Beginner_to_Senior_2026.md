# Tailwind CSS — Beginner → Senior Handbook
## Modern Tailwind CSS v4.3 (2026)

> Tài liệu này tự giải thích Tailwind đầy đủ, nhưng luôn liên hệ utility với CSS thật để bạn hiểu bản chất thay vì học thuộc class.
>
> Baseline: **Tailwind CSS v4.3**.
>
> Mental model:
>
> ```text
> Tailwind utility
> → CSS property / selector / at-rule
> → browser behavior
> ```
>
> Mục tiêu:
>
> ```text
> Beginner
> → utility fluency
> → responsive/state variants
> → components
> → design tokens
> → architecture
> → Senior Tailwind
> ```
>
> Ký hiệu:
> - **[CORE]**: bắt buộc.
> - **[ADV]**: senior cần biết.
> - **[V4]**: Tailwind v4 CSS-first.
> - **[V4.3]**: feature hiện tại của v4.3.
> - **Idiom**: cách viết thường gặp.
> - **Coding Pattern**: pattern implementation.
> - **Design Pattern**: architecture/design-system pattern.
> - **⚠ Pitfall**: lỗi phổ biến.

---

# 0. Tailwind CSS là gì?

Tailwind là **utility-first CSS framework**.

CSS truyền thống:

```css
.card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: .75rem;
  background: white;
}
```

Tailwind:

```html
<div class="flex items-center gap-4 rounded-xl bg-white p-6">
  ...
</div>
```

Tailwind build tool scan các class trong HTML/JSX/template và generate CSS tĩnh. Browser cuối cùng vẫn chỉ chạy CSS.

**Tailwind không thay CSS.** Ví dụ:

```text
flex         → display:flex
items-center → align-items:center
gap-4        → gap từ spacing theme
bg-blue-600  → background-color từ color theme
```

---

# 1. Tailwind v4.3 khác v3 [MUST]

Tutorial v3 thường dùng:

```js
// tailwind.config.js
export default {
  content: ["./src/**/*.{html,js,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: "#2563eb",
      },
    },
  },
};
```

V4 ưu tiên **CSS-first configuration**:

```css
@import "tailwindcss";

@theme {
  --color-brand: #2563eb;
}
```

Sau đó:

```html
<button class="bg-brand text-white">
  Save
</button>
```

Các concept v4 cần nắm:

```text
@import "tailwindcss"
@theme
@source
@utility
@variant
@custom-variant
@reference
--alpha()
--spacing()
automatic source detection
CSS theme variables
```

`@config` và `@plugin` còn cho compatibility/migration, không nên là kiến trúc mặc định mới.

---

# 2. Installation [CORE]

## Vite

```bash
npm install tailwindcss @tailwindcss/vite
```

```js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

CSS:

```css
@import "tailwindcss";
```

## CLI

```bash
npm install tailwindcss @tailwindcss/cli
```

```bash
npx @tailwindcss/cli \
  -i ./src/input.css \
  -o ./src/output.css \
  --watch
```

## PostCSS

```bash
npm install tailwindcss @tailwindcss/postcss postcss
```

## Webpack [v4.2+]

Có first-party package `@tailwindcss/webpack`.

## Play CDN

Chỉ dùng thử/demo, không dùng production.

---

# 3. `@import "tailwindcss"` [CORE]

Tailwind import mặc định sử dụng native cascade layers:

```text
theme
→ base
→ components
→ utilities
```

- `theme`: theme variables.
- `base`: Preflight/default base.
- `components`: custom component layer.
- `utilities`: Tailwind utilities.

Tailwind không có cascade riêng; cuối cùng browser vẫn áp dụng CSS cascade.

---

# 4. Utility syntax

```text
md:hover:bg-blue-600/80
```

Tách:

```text
md:        responsive variant
hover:     pseudo-class variant
bg-        utility family
blue-600   theme value
/80        modifier/alpha
```

Arbitrary:

```text
w-[37rem]
```

CSS:

```css
width:37rem;
```

---

# 5. Important modifier [V4]

Preferred v4:

```html
<div class="bg-red-500!"></div>
```

State:

```html
<div class="hover:bg-red-600!"></div>
```

`!` sinh declaration `!important`.

⚠ Không dùng để giải quyết architecture/specificity một cách tùy tiện.

---

# 6. Spacing scale [CORE]

V4 dùng spacing variable làm basis cho nhiều dynamic utilities.

Concept mặc định:

```css
--spacing: .25rem;
```

Nên thường:

```text
1 → .25rem
2 → .5rem
4 → 1rem
6 → 1.5rem
8 → 2rem
```

V4 có thể hỗ trợ numeric values linh hoạt:

```text
mt-17
w-29
```

được derive từ spacing system khi utility family support.

Framework cho phép số không có nghĩa design system cũng nên dùng mọi số.

---

# 7. Arbitrary values [CORE]

```html
<div class="top-[117px]"></div>
```

CSS:

```css
top:117px;
```

Có variant:

```html
<div class="top-[117px] lg:top-[344px]"></div>
```

**Pattern:** token trước, arbitrary value cho exception thật sự.

---

# 8. Arbitrary whitespace

```html
<div class="grid-cols-[1fr_500px_2fr]"></div>
```

Tailwind đổi `_` thành space khi grammar phù hợp.

```css
grid-template-columns:1fr 500px 2fr;
```

---

# 9. CSS variable shorthand

```html
<div class="fill-(--brand)"></div>
```

tương đương concept:

```css
fill:var(--brand);
```

Rất hữu ích với runtime values:

```jsx
<div
  style={{ "--width": `${width}px` }}
  className="w-(--width)"
/>
```

---

# 10. Arbitrary properties

```html
<div class="[mask-type:luminance]"></div>
```

CSS:

```css
mask-type:luminance;
```

State:

```html
<div class="hover:[mask-type:alpha]"></div>
```

CSS variables cũng có thể set:

```html
<div class="[--offset:56px] lg:[--offset:44px]"></div>
```

---

# 11. Arbitrary variants [ADV]

```html
<div class="[&>p]:mt-4">
```

Concept:

```css
.current > p {
  margin-top:1rem;
}
```

Complex:

```html
<li class="lg:[&:nth-child(-n+3)]:hover:underline">
```

Nếu selector này lặp lại nhiều lần, custom variant/custom CSS thường rõ hơn.

---

# 12. Type hints [ADV]

`text-*` có thể biểu diễn font-size hoặc color.

```html
<div class="text-(length:--value)"></div>
```

→ length/font-size context.

```html
<div class="text-(color:--value)"></div>
```

→ color context.

---

# 13. Static source detection [MUST]

Bad:

```jsx
<div className={`bg-${color}-600`} />
```

Tailwind scan text, không evaluate runtime template để xây mọi khả năng.

Good:

```jsx
const variants = {
  blue: "bg-blue-600 hover:bg-blue-500",
  red: "bg-red-600 hover:bg-red-500",
};

<div className={variants[color]} />
```

**Design Pattern:**

```text
runtime prop
→ finite static class map
```

---

# 14. Preflight [CORE]

Preflight là Tailwind base reset. Nó thay đổi nhiều browser defaults:

- margins reset,
- heading không còn size/bold mặc định kiểu UA stylesheet,
- list styles reset,
- border behavior normalize,
- image behavior normalize.

Nếu `<h1>` không tự to/bold, đó có thể là Preflight chứ không phải lỗi.

---

# 15. `@theme` [CORE][V4]

```css
@theme {
  --color-brand-500: oklch(.62 .2 255);
  --font-display: "Inter", sans-serif;
  --breakpoint-3xl: 120rem;
}
```

Tạo utility:

```text
bg-brand-500
text-brand-500
font-display
3xl:...
```

Theme variable vừa là:
- compiler configuration,
- CSS custom property/token runtime.

---

# 16. Theme namespace mental model

Các namespace thường map tới utility families:

```text
--color-*       → bg/text/border/fill/stroke/...
--font-*        → font-family
--text-*        → font-size
--font-weight-* → font-weight
--tracking-*    → letter-spacing
--leading-*     → line-height
--breakpoint-*  → viewport responsive variants
--container-*   → container query variants
--radius-*      → rounded-*
--shadow-*      → shadow-*
--blur-*        → blur-*
--ease-*        → ease-*
--animate-*     → animate-*
```

`@theme` vì vậy là **utility API design**, không chỉ file chứa biến.

---

# 17. `@theme inline`

```css
@theme inline {
  --font-sans: var(--font-inter);
}
```

Dùng khi theme token reference variable khác và bạn muốn generated utility sử dụng referenced value trực tiếp để tránh CSS-variable scope resolution bất ngờ.

---

# 18. `@theme static`

```css
@theme static {
  --color-primary: var(--color-red-500);
}
```

Mặc định Tailwind có thể chỉ emit variables cần dùng. `static` yêu cầu emit đầy đủ.

Use:
- JS/library đọc token,
- shared token package.

Cost: CSS lớn hơn.

---

# 19. Reset theme namespace

```css
@theme {
  --color-*: initial;
}
```

Xóa default color theme API.

Reset toàn bộ:

```css
@theme {
  --*: initial;
}
```

Rất mạnh; chỉ dùng khi design system muốn strict token surface.

---

# 20. Colors [CORE]

Common palette families:

```text
slate gray zinc neutral stone
mauve olive mist taupe
red orange amber yellow lime
green emerald teal cyan sky blue
indigo violet purple fuchsia pink rose
```

V4.2 thêm:
```text
mauve olive mist taupe
```

Scale thường:
```text
50 100 200 ... 900 950
```

Color alpha:

```text
bg-blue-600/50
text-black/80
border-gray-900/10
```

Arbitrary alpha:

```text
bg-pink-500/[71.37%]
```

---

# 21. Color utility families

```text
bg-*         background-color
text-*       color
border-*     border-color
outline-*    outline-color
ring-*       Tailwind ring/shadow mechanism
fill-*       SVG fill
stroke-*     SVG stroke
accent-*     accent-color
caret-*      caret-color
```

---



---

# 22. Display & layout [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `block` | `display:block` | Block box. |
| `inline` | `display:inline` | Inline formatting. |
| `inline-block` | `display:inline-block` | Inline ngoài, block-like sizing. |
| `flex` | `display:flex` | Flex formatting context. |
| `inline-flex` | `display:inline-flex` | Inline flex. |
| `grid` | `display:grid` | Grid formatting context. |
| `inline-grid` | `display:inline-grid` | Inline grid. |
| `flow-root` | `display:flow-root` | Tạo BFC mới. |
| `contents` | `display:contents` | Element box biến mất, children vẫn layout. |
| `hidden` | `display:none` | Loại khỏi layout. |


---

# 23. Position [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `static` | `position:static` | Normal flow. |
| `relative` | `position:relative` | Giữ flow, làm positioning context. |
| `absolute` | `position:absolute` | Ra khỏi normal flow. |
| `fixed` | `position:fixed` | Thường theo viewport. |
| `sticky` | `position:sticky` | Sticky theo scroll container. |


---

# 24. Inset [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `inset-0` | `inset:0` | Bốn cạnh. |
| `top-4` | `top` từ spacing | Physical top. |
| `right-4` | `right` | Physical right. |
| `bottom-4` | `bottom` | Physical bottom. |
| `left-4` | `left` | Physical left. |
| `inset-x-4` | left/right pair | Horizontal physical. |
| `inset-y-4` | top/bottom pair | Vertical physical. |
| `inset-s-4` | `inset-inline-start` | Logical inline start [v4.2+]. |
| `inset-e-4` | `inset-inline-end` | Logical inline end [v4.2+]. |
| `inset-bs-4` | `inset-block-start` | Logical block start [v4.2+]. |
| `inset-be-4` | `inset-block-end` | Logical block end [v4.2+]. |


---

# 25. z-index [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `z-0` | `z-index:0` | Base. |
| `z-10` | `z-index:10` | Common step. |
| `z-50` | `z-index:50` | High conventional step. |
| `z-auto` | `z-index:auto` | Reset/default. |
| `z-[999]` | `z-index:999` | One-off. |


---

# 26. Overflow [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `overflow-auto` | `overflow:auto` | Scrollbar khi cần. |
| `overflow-hidden` | `overflow:hidden` | Clip + scroll semantics. |
| `overflow-clip` | `overflow:clip` | Clip không tạo scroll behavior như hidden. |
| `overflow-visible` | `overflow:visible` | Cho overflow paint. |
| `overflow-scroll` | `overflow:scroll` | Scroll container. |
| `overflow-x-auto` | `overflow-x:auto` | Horizontal scroll. |
| `overflow-y-auto` | `overflow-y:auto` | Vertical scroll. |


---

# 27. Visibility & opacity

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `visible` | `visibility:visible` | Visible. |
| `invisible` | `visibility:hidden` | Giữ layout space. |
| `collapse` | `visibility:collapse` | Collapse behavior. |
| `opacity-0` | `opacity:0` | Transparent nhưng vẫn layout. |
| `opacity-50` | `opacity:.5` | Half opacity. |
| `opacity-100` | `opacity:1` | Opaque. |


---

# 28. Aspect ratio

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `aspect-square` | `aspect-ratio:1/1` | Square. |
| `aspect-video` | theme video ratio | Video frame. |
| `aspect-3/2` | `aspect-ratio:3/2` | Dynamic ratio. |
| `aspect-[4/3]` | `aspect-ratio:4/3` | Arbitrary. |
| `aspect-auto` | `aspect-ratio:auto` | Intrinsic/default. |


---

# 29. Object fit/position

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `object-cover` | `object-fit:cover` | Fill/crop. |
| `object-contain` | `object-fit:contain` | Show full resource. |
| `object-fill` | `object-fit:fill` | Stretch. |
| `object-none` | `object-fit:none` | No resize. |
| `object-scale-down` | `object-fit:scale-down` | none/contain whichever smaller. |
| `object-center` | `object-position:center` | Center crop. |
| `object-top` | `object-position:top` | Top crop. |
| `object-[50%_20%]` | `object-position:50% 20%` | Fine focal point. |


---

# 30. Margin [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `m-4` | margin all | All sides. |
| `mx-4` | horizontal/inline margins | Horizontal. |
| `my-4` | vertical/block margins | Vertical. |
| `mt-4` | `margin-top` | Physical top. |
| `mr-4` | `margin-right` | Physical right. |
| `mb-4` | `margin-bottom` | Physical bottom. |
| `ml-4` | `margin-left` | Physical left. |
| `ms-4` | `margin-inline-start` | Logical start. |
| `me-4` | `margin-inline-end` | Logical end. |
| `mbs-4` | `margin-block-start` | Logical block start [v4.2+]. |
| `mbe-4` | `margin-block-end` | Logical block end [v4.2+]. |
| `mx-auto` | auto horizontal/inline margins | Center constrained block. |
| `-mt-4` | negative margin top | Pull upward. |


---

# 31. Padding [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `p-4` | padding all | All sides. |
| `px-4` | horizontal/inline padding | Horizontal. |
| `py-4` | vertical/block padding | Vertical. |
| `pt-4` | `padding-top` | Physical top. |
| `pr-4` | `padding-right` | Physical right. |
| `pb-4` | `padding-bottom` | Physical bottom. |
| `pl-4` | `padding-left` | Physical left. |
| `ps-4` | `padding-inline-start` | Logical start. |
| `pe-4` | `padding-inline-end` | Logical end. |
| `pbs-4` | `padding-block-start` | Logical block start [v4.2+]. |
| `pbe-4` | `padding-block-end` | Logical block end [v4.2+]. |


---

# 32. Width [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `w-4` | spacing-derived width | Token/dynamic scale. |
| `w-full` | `width:100%` | Fill containing block. |
| `w-screen` | `width:100vw` | Viewport. |
| `w-dvw` | `width:100dvw` | Dynamic viewport. |
| `w-min` | `width:min-content` | Intrinsic minimum. |
| `w-max` | `width:max-content` | Intrinsic maximum. |
| `w-fit` | `width:fit-content` | Fit content. |
| `w-1/2` | `width:50%` | Fraction. |
| `w-[37rem]` | `width:37rem` | Arbitrary. |


---

# 33. Min/max width

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `min-w-0` | `min-width:0` | Critical Flex/Grid shrink fix. |
| `min-w-full` | `min-width:100%` | At least full. |
| `min-w-min` | `min-width:min-content` | Intrinsic min. |
| `min-w-max` | `min-width:max-content` | Intrinsic max. |
| `max-w-none` | `max-width:none` | No cap. |
| `max-w-full` | `max-width:100%` | Cap at parent. |
| `max-w-prose` | theme prose measure | Readable text measure. |
| `max-w-[60ch]` | `max-width:60ch` | Arbitrary measure. |


---

# 34. Height [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `h-4` | spacing-derived height | Token/dynamic scale. |
| `h-full` | `height:100%` | Needs definite context in many cases. |
| `h-screen` | `height:100vh` | Classic viewport. |
| `h-dvh` | `height:100dvh` | Dynamic viewport. |
| `h-svh` | `height:100svh` | Small viewport. |
| `h-lvh` | `height:100lvh` | Large viewport. |
| `h-auto` | `height:auto` | Intrinsic/content. |
| `h-fit` | `height:fit-content` | Fit content. |


---

# 35. Min/max height

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `min-h-0` | `min-height:0` | Vertical flex/grid scroll fix. |
| `min-h-screen` | `min-height:100vh` | Classic page. |
| `min-h-dvh` | `min-height:100dvh` | Modern mobile page. |
| `max-h-full` | `max-height:100%` | Cap. |
| `max-h-dvh` | `max-height:100dvh` | Viewport cap. |
| `max-h-[80dvh]` | `max-height:80dvh` | Modal/panel. |


---

# 36. Logical sizing [v4.2+]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `inline-full` | `inline-size:100%` | Writing-mode aware width. |
| `inline-64` | spacing-based inline-size | Logical width. |
| `min-inline-0` | `min-inline-size:0` | Logical min-width. |
| `max-inline-lg` | theme max inline size | Logical cap. |
| `block-64` | `block-size` | Logical height. |
| `min-block-0` | `min-block-size:0` | Logical min-height. |
| `max-block-screen` | screen-like block cap | Writing-mode aware. |


---

# 37. Flex container [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `flex-row` | `flex-direction:row` | Row. |
| `flex-row-reverse` | `row-reverse` | Reverse row. |
| `flex-col` | `column` | Column. |
| `flex-col-reverse` | `column-reverse` | Reverse column. |
| `flex-wrap` | `flex-wrap:wrap` | Allow lines. |
| `flex-nowrap` | `nowrap` | Single line. |
| `flex-wrap-reverse` | `wrap-reverse` | Reverse cross lines. |


---

# 38. Flex item [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `flex-1` | flex shorthand grow/shrink zero-ish basis | Fill free space. |
| `flex-auto` | auto-basis flex shorthand | Grow/shrink from auto size. |
| `flex-initial` | initial flex behavior | Initial-like. |
| `flex-none` | `flex:none` | No grow/shrink. |
| `grow` | `flex-grow:1` | Grow. |
| `grow-0` | `flex-grow:0` | Don't grow. |
| `shrink` | `flex-shrink:1` | Shrink. |
| `shrink-0` | `flex-shrink:0` | Don't shrink. |
| `basis-64` | spacing flex-basis | Initial main size. |
| `basis-1/2` | `flex-basis:50%` | Fraction basis. |
| `basis-auto` | `flex-basis:auto` | Auto basis. |


---

# 39. Alignment [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `justify-start` | `justify-content:flex-start` | Main start. |
| `justify-center` | `justify-content:center` | Main center. |
| `justify-end` | `justify-content:flex-end` | Main end. |
| `justify-between` | `space-between` | Between. |
| `justify-around` | `space-around` | Around. |
| `justify-evenly` | `space-evenly` | Even. |
| `items-start` | `align-items:flex-start` | Cross start. |
| `items-center` | `align-items:center` | Cross center. |
| `items-end` | `align-items:flex-end` | Cross end. |
| `items-stretch` | `align-items:stretch` | Stretch. |
| `items-baseline` | `align-items:baseline` | Text baseline. |
| `self-center` | `align-self:center` | Per-item override. |
| `place-items-center` | `place-items:center` | Grid align+justify items. |


---

# 40. Gap [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `gap-4` | `gap` spacing | Both axes. |
| `gap-x-4` | `column-gap` | Column gap. |
| `gap-y-4` | `row-gap` | Row gap. |
| `gap-[3.5rem]` | `gap:3.5rem` | One-off. |


---

# 41. Grid columns [CORE]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `grid-cols-1` | 1 equal column | Single. |
| `grid-cols-2` | 2 equal minmax tracks | Two columns. |
| `grid-cols-12` | 12 equal tracks | Classic 12-col. |
| `grid-cols-15` | dynamic v4 column count | 15 equal tracks. |
| `grid-cols-none` | `grid-template-columns:none` | No explicit. |
| `grid-cols-subgrid` | `grid-template-columns:subgrid` | Reuse parent tracks. |
| `grid-cols-[240px_minmax(0,1fr)]` | arbitrary grid template | Sidebar. |


---

# 42. Grid rows/placement

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `grid-rows-3` | 3 equal rows | Three tracks. |
| `grid-rows-subgrid` | `subgrid` rows | Reuse parent. |
| `col-span-2` | span two columns | Placement. |
| `col-span-full` | `grid-column:1/-1` | Full explicit grid. |
| `col-start-2` | start line 2 | Placement. |
| `col-end-4` | end line 4 | Placement. |
| `row-span-2` | span two rows | Placement. |
| `row-start-1` | start row 1 | Placement. |
| `row-end-3` | end row 3 | Placement. |


---

# 43. Grid auto flow [ADV]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `grid-flow-row` | `grid-auto-flow:row` | Auto rows. |
| `grid-flow-col` | `grid-auto-flow:column` | Auto cols. |
| `grid-flow-dense` | dense auto-placement | Backfill holes; visual reorder risk. |
| `auto-cols-auto` | implicit columns auto | Content-based. |
| `auto-cols-fr` | equal fractional implicit cols | Equal. |
| `auto-rows-auto` | implicit rows auto | Content-based. |
| `auto-rows-fr` | equal fractional implicit rows | Equal. |


---

# 44. Order [ADV]

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `order-first` | negative/first order token | Visual first. |
| `order-last` | last order token | Visual last. |
| `order-none` | `order:0` | Default. |
| `order-1` | `order:1` | Relative order. |


---

# 45. Font family

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `font-sans` | `font-family:var(--font-sans)` | Sans theme. |
| `font-serif` | serif theme | Serif. |
| `font-mono` | mono theme | Monospace. |
| `font-(--brand-font)` | runtime CSS variable | Custom runtime font. |


---

# 46. Font size

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `text-xs` | theme xs font-size | Caption. |
| `text-sm` | theme small | Secondary. |
| `text-base` | theme base | Body. |
| `text-lg` | theme large | Lead. |
| `text-xl` | theme xl | Small heading. |
| `text-2xl` | theme 2xl | Heading. |
| `text-6xl` | large display | Hero. |
| `text-[17px]` | `font-size:17px` | Arbitrary. |
| `text-lg/7` | font size + line-height modifier | Compact size/leading. |


---

# 47. Font weight/style

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `font-light` | light weight | Light. |
| `font-normal` | normal weight | Body. |
| `font-medium` | medium | UI. |
| `font-semibold` | semibold | Button/heading. |
| `font-bold` | bold | Strong. |
| `font-black` | black | Display. |
| `font-[650]` | `font-weight:650` | Variable font. |
| `italic` | `font-style:italic` | Italic. |
| `not-italic` | `font-style:normal` | Reset. |


---

# 48. Line height / tracking

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `leading-none` | `line-height:1` | Tight. |
| `leading-tight` | tight theme leading | Heading. |
| `leading-normal` | normal theme | Body. |
| `leading-relaxed` | relaxed theme | Readable. |
| `leading-[1.65]` | arbitrary line-height | Custom. |
| `tracking-tight` | negative tracking token | Heading. |
| `tracking-normal` | normal | Reset. |
| `tracking-wide` | positive | Labels. |
| `tracking-[.08em]` | arbitrary letter-spacing | Custom. |


---

# 49. Text alignment/transform

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `text-left` | `text-align:left` | Physical left. |
| `text-center` | `text-align:center` | Center. |
| `text-right` | `text-align:right` | Physical right. |
| `text-start` | `text-align:start` | Logical start. |
| `text-end` | `text-align:end` | Logical end. |
| `text-justify` | `text-align:justify` | Justify. |
| `uppercase` | `text-transform:uppercase` | Visual uppercase. |
| `lowercase` | `lowercase` | Visual lowercase. |
| `capitalize` | `capitalize` | Capitalize. |
| `normal-case` | `none` | Reset. |


---

# 50. Text wrap/overflow

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `truncate` | overflow hidden + ellipsis + nowrap | Single-line truncate bundle. |
| `text-ellipsis` | `text-overflow:ellipsis` | Ellipsis piece. |
| `text-clip` | `text-overflow:clip` | No ellipsis. |
| `whitespace-normal` | `white-space:normal` | Normal. |
| `whitespace-nowrap` | `nowrap` | No wrapping. |
| `whitespace-pre` | `pre` | Preserve. |
| `whitespace-pre-wrap` | `pre-wrap` | Preserve + wrap. |
| `break-words` | overflow-wrap style breaking | Break long tokens. |
| `break-all` | `word-break:break-all` | Aggressive. |
| `break-keep` | `word-break:keep-all` | Useful CJK contexts. |
| `text-balance` | `text-wrap:balance` | Balance heading. |
| `text-pretty` | `text-wrap:pretty` | Improve body wrapping. |


---

# 51. Lists

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `list-none` | `list-style-type:none` | No marker. |
| `list-disc` | disc | Bullet. |
| `list-decimal` | decimal | Numbered. |
| `list-inside` | `list-style-position:inside` | Inside. |
| `list-outside` | outside | Outside. |


---

# 52. Background

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `bg-white` | theme background color | White. |
| `bg-transparent` | transparent | Transparent. |
| `bg-current` | `currentColor` | Follow color. |
| `bg-cover` | `background-size:cover` | Fill/crop image. |
| `bg-contain` | `contain` | Contain image. |
| `bg-center` | `background-position:center` | Center. |
| `bg-top` | top | Top. |
| `bg-no-repeat` | `background-repeat:no-repeat` | No repeat. |
| `bg-repeat` | repeat | Repeat. |
| `bg-fixed` | `background-attachment:fixed` | Fixed attachment. |


---

# 53. Border radius

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `rounded-none` | radius 0 | Square. |
| `rounded-sm` | small theme radius | Small. |
| `rounded` | default radius | Default. |
| `rounded-lg` | large | Card. |
| `rounded-xl` | extra large | Card. |
| `rounded-full` | very large/infinite | Pill/circle. |
| `rounded-s-lg` | logical start corners | RTL-aware. |


---

# 54. Border

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `border` | default border width | Usually thin. |
| `border-2` | 2px-like border width | Thicker. |
| `border-t` | top border | Divider. |
| `border-bs` | block-start border [v4.2+] | Logical. |
| `border-solid` | solid | Solid. |
| `border-dashed` | dashed | Dashed. |
| `border-dotted` | dotted | Dotted. |
| `border-none` | none | No border. |
| `border-gray-200` | theme border color | Neutral divider. |


---

# 55. Outline

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `outline` | outline default | Focus outline. |
| `outline-2` | outline 2px | Focus. |
| `outline-blue-500` | outline color | Brand. |
| `outline-offset-2` | `outline-offset` | Space. |
| `outline-none` | remove/reset outline | Only with replacement focus. |


---

# 56. Shadow/effects

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `shadow-none` | `box-shadow:none` | Reset. |
| `shadow-sm` | small theme shadow | Subtle. |
| `shadow-md` | medium | Card. |
| `shadow-lg` | large | Elevated. |
| `shadow-xl` | extra large | Overlay. |
| `opacity-50` | `opacity:.5` | Whole subtree opacity. |
| `mix-blend-multiply` | `mix-blend-mode:multiply` | Blend. |
| `bg-blend-multiply` | background blend | Background layers. |
| `isolate` | `isolation:isolate` | New local stacking/blending context. |


---

# 57. Filters

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `blur-sm` | `filter:blur(...)` | Small blur. |
| `brightness-110` | brightness filter | Brighten. |
| `contrast-125` | contrast filter | Contrast. |
| `grayscale` | grayscale 100% | Monochrome. |
| `hue-rotate-90` | hue rotate | Hue shift. |
| `invert` | invert | Invert. |
| `saturate-150` | saturate | More saturation. |
| `sepia` | sepia | Sepia. |
| `drop-shadow-md` | drop-shadow filter | Alpha-shape shadow. |
| `backdrop-blur-md` | backdrop-filter blur | Glass effect. |


---

# 58. Tables

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `border-collapse` | `border-collapse:collapse` | Merge borders. |
| `border-separate` | separate | Separate. |
| `border-spacing-2` | border spacing | Cell gaps. |
| `table-auto` | `table-layout:auto` | Content-driven. |
| `table-fixed` | `table-layout:fixed` | Predictable. |
| `caption-top` | caption top | Top. |
| `caption-bottom` | caption bottom | Bottom. |


---

# 59. Transform

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `translate-x-4` | translate x spacing | Move X. |
| `-translate-x-1/2` | translate -50% x | Center pattern. |
| `translate-y-2` | translate y | Move Y. |
| `scale-105` | scale 1.05 | Emphasis. |
| `rotate-45` | rotate 45deg | Rotate. |
| `-rotate-6` | negative rotate | Counterclockwise. |
| `skew-x-6` | skew x | Skew. |
| `origin-center` | transform-origin center | Pivot. |
| `backface-hidden` | backface hidden | 3D. |
| `transform-3d` | preserve-3d | 3D children. |


---

# 60. Transition

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `transition` | common property transition set | General UI. |
| `transition-all` | all properties | Broad; use carefully. |
| `transition-colors` | color-related | Interactive colors. |
| `transition-opacity` | opacity | Fade. |
| `transition-shadow` | shadow | Elevation. |
| `transition-transform` | transform | Motion. |
| `transition-none` | none | Disable. |
| `duration-150` | 150ms | Fast UI. |
| `duration-300` | 300ms | Moderate. |
| `ease-out` | ease-out | Decelerate. |
| `delay-75` | 75ms delay | Delay. |


---

# 61. Cursor/interactivity

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `cursor-pointer` | `cursor:pointer` | Pointer. |
| `cursor-not-allowed` | not-allowed | Disabled hint. |
| `pointer-events-none` | `pointer-events:none` | Ignore pointer. |
| `pointer-events-auto` | auto | Restore. |
| `select-none` | `user-select:none` | Prevent text selection. |
| `select-text` | text | Allow. |
| `appearance-none` | `appearance:none` | Remove native skin. |
| `accent-blue-600` | `accent-color` | Native controls. |
| `caret-blue-600` | `caret-color` | Caret. |
| `resize-y` | `resize:vertical` | Textarea vertical resize. |


---

# 62. Scroll

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `scroll-smooth` | `scroll-behavior:smooth` | Smooth scroll. |
| `snap-x` | horizontal scroll snap | Carousel. |
| `snap-y` | vertical scroll snap | Vertical. |
| `snap-mandatory` | mandatory strictness | Strong. |
| `snap-proximity` | proximity | Gentle. |
| `snap-start` | align snap start | Item. |
| `overscroll-contain` | `overscroll-behavior:contain` | Prevent scroll chain. |
| `scroll-mt-20` | `scroll-margin-top` | Sticky header anchors. |
| `touch-pan-y` | `touch-action:pan-y` | Allow vertical pan. |
| `will-change-transform` | `will-change:transform` | Optimization hint; use sparingly. |


---

# 63. SVG

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `fill-current` | `fill:currentColor` | Icon follows text. |
| `fill-none` | `fill:none` | No fill. |
| `stroke-current` | `stroke:currentColor` | Stroke follows text. |
| `stroke-2` | `stroke-width:2` | Icon stroke. |


---

# 64. Accessibility

| Tailwind | CSS / browser behavior | Giải thích Tailwind |
|---|---|---|
| `sr-only` | visually-hidden accessible CSS pattern | Keep for screen readers. |
| `not-sr-only` | restore visually visible positioning | Undo sr-only. |
| `forced-color-adjust-auto` | allow forced colors adaptation | Default accessible behavior. |
| `forced-color-adjust-none` | opt out forced color adjustment | Rare targeted use. |


---

# 65. `size-*` idiom

```html
<img class="size-12 rounded-full object-cover">
```

`size-12` sets width + height cùng token.

---

# 66. `min-w-0` — senior utility phải nhớ

```html
<div class="flex">
  <div class="shrink-0">Avatar</div>
  <div class="min-w-0 flex-1">
    <p class="truncate">
      Very long text...
    </p>
  </div>
</div>
```

Flex item mặc định có automatic minimum size dựa vào content. `min-w-0` cho phép item co xuống dưới intrinsic content width để ellipsis/overflow hoạt động đúng.

---

# 67. `min-h-0` — vertical flex scroll

```html
<div class="flex h-dvh flex-col">
  <header class="shrink-0">...</header>
  <main class="min-h-0 flex-1 overflow-auto">
    ...
  </main>
</div>
```

Nếu quên `min-h-0`, vùng scroll trong flex column có thể overflow thay vì co.

---

# 68. `gap-*` vs `space-*`

`gap-*` dùng CSS gap và phù hợp nhất cho Flex/Grid:

```html
<div class="flex flex-col gap-4">
```

`space-y-*`/`space-x-*` tạo spacing giữa children bằng selector/margin logic.

Senior preference:
- Flex/Grid → `gap`.
- Normal flow hoặc legacy pattern đặc biệt → `space-*` nếu hợp lý.

---

# 69. `divide-*`

```html
<ul class="divide-y divide-gray-200">
```

Tạo border giữa siblings.

Khác:
- `gap` = khoảng trống,
- `divide` = đường phân tách.

---

# 70. Ring utilities

Ví dụ:

```html
<div class="ring-1 ring-gray-900/10">
```

Tailwind ring được tạo bằng box-shadow/custom-property composition, không phải CSS property `ring`.

Use:
- subtle card ring,
- focus effect,
- inset ring.

`outline` thường đơn giản/semantic hơn cho focus accessibility.

---

# 71. Line clamp

```html
<p class="line-clamp-3">
  ...
</p>
```

Giới hạn text nhiều dòng bằng line-clamp implementation.

```text
line-clamp-none
```

reset.

Không truncate nội dung quan trọng mà user không có cách mở đầy đủ.

---

# 72. Numeric typography

```text
tabular-nums
lining-nums
oldstyle-nums
slashed-zero
```

Các utility này map tới OpenType font numeric feature settings ở mức high-level.

V4.2+ có:

```html
<div class='font-features-["tnum"]'>
```

cho low-level `font-feature-settings`.

Ưu tiên `tabular-nums` hơn raw `"tnum"` khi equivalent.

---

# 73. Text shadow [current v4]

Utility family:

```text
text-shadow-none
text-shadow-sm
text-shadow-md
text-shadow-lg
text-shadow-...
```

Maps tới `text-shadow`.

Dùng tiết chế vì heavy shadow có thể làm typography khó đọc.

---

# 74. Masks

Current Tailwind docs có utility families cho:
- mask-image,
- mask-size,
- mask-position,
- mask-repeat,
- mask-origin,
- mask-clip,
- mask-mode,
- mask-composite,
- mask-type.

Escape hatch:

```html
<div class="[mask-type:luminance]">
```

Masks dùng cho:
- edge fades,
- icon systems,
- gradient reveals.

---

# 75. Animations

Built-in common:

```text
animate-none
animate-spin
animate-ping
animate-pulse
animate-bounce
```

Custom theme animation:

```css
@theme {
  --animate-fade-in: fade-in .2s ease-out;

  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }
}
```

Use:

```html
<div class="animate-fade-in">
```

---

# 76. Reduced motion

```html
<div
  class="
    transition-transform
    motion-reduce:transition-none
  "
>
```

Variants:
```text
motion-safe:
motion-reduce:
```

Maps to `prefers-reduced-motion`.

---

# 77. Scrollbars [V4.3]

Width:

```text
scrollbar-auto
scrollbar-thin
scrollbar-none
```

Colors:

```text
scrollbar-thumb-sky-700
scrollbar-track-sky-100
scrollbar-thumb-slate-900/60
```

Gutter:

```text
scrollbar-gutter-auto
scrollbar-gutter-stable
scrollbar-gutter-both
```

`stable` giúp reserve scrollbar space và giảm layout shift.

---

# 78. `zoom-*` [V4.3]

```html
<div class="zoom-75"></div>
<div class="zoom-100"></div>
<div class="zoom-125"></div>
<div class="zoom-[1.1]"></div>
<div class="zoom-(--preview-zoom)"></div>
```

Maps tới CSS `zoom`.

Khác `scale`:
- `zoom` ảnh hưởng layout sizing,
- transform scale chủ yếu transform visual result.

Không dùng `zoom` thay responsive design.

---

# 79. `tab-*` [V4.3]

```text
tab-2
tab-4
tab-[12px]
tab-(--tab-size)
```

Maps tới CSS `tab-size`.

Use:
- code editors,
- `<pre>`,
- rendered source code.

---

# 80. Responsive design [CORE]

Tailwind responsive mặc định mobile-first:

```html
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4">
```

Meaning:

```text
base → 1
md and up → 2
xl and up → 4
```

`md:` không nghĩa “chỉ md”.

---

# 81. Custom breakpoints

```css
@theme {
  --breakpoint-*: initial;
  --breakpoint-tablet: 40rem;
  --breakpoint-laptop: 64rem;
  --breakpoint-desktop: 80rem;
}
```

Use:

```text
tablet:
laptop:
desktop:
```

Breakpoint nên xuất phát từ content/layout, không từ tên device marketing.

---

# 82. Range variants

```html
<div class="md:max-xl:flex">
```

Target khoảng `md` tới trước `xl`.

Arbitrary:

```text
max-[600px]:
min-[320px]:
```

---

# 83. Container Queries [CORE/ADV]

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row">
    ...
  </div>
</div>
```

Phân biệt:

```text
md:
→ viewport media query

@md:
→ ancestor container query
```

Container query rất phù hợp reusable component trong:
- sidebar,
- main,
- modal,
- dashboard card.

---

# 84. Container max/range

```text
@max-md:
@sm:@max-md:
@min-[475px]:
@max-[960px]:
```

Tailwind container queries cũng mobile-first theo container size.

---

# 85. `@container-size` [V4.3]

```html
<div class="@container-size">
  <div class="h-[50cqb]">
```

- `@container`: inline-size container.
- `@container-size`: size container, cho phép block-size-related queries/units.

Named form cũng tồn tại:

```text
@container-size/name
```

---

# 86. Hover/focus/active variants

```html
<button
  class="
    bg-blue-600
    hover:bg-blue-700
    focus:outline-2
    active:bg-blue-800
  "
>
```

Mapping:

```text
hover: → :hover + hover capability handling
focus: → :focus
active: → :active
```

---

# 87. `focus-visible` / `focus-within`

```text
focus-visible:
```

→ keyboard-like visible focus indicator cases.

```text
focus-within:
```

→ parent matches khi nó hoặc descendant focus.

Accessible pattern:

```html
<button
  class="
    focus-visible:outline-2
    focus-visible:outline-offset-2
    focus-visible:outline-blue-600
  "
>
```

---

# 88. Structural variants

```text
first:
last:
only:
odd:
even:
first-of-type:
last-of-type:
empty:
```

Example:

```html
<li class="border-b last:border-b-0">
```

---

# 89. `nth-*` variants

```text
nth-3:
nth-last-5:
nth-of-type-4:
```

Complex:

```text
nth-[2n+1_of_li]:
```

Maps tới CSS `:nth-*`.

---

# 90. Form variants

Important:

```text
required:
optional:
valid:
invalid:
user-valid:
user-invalid:
disabled:
enabled:
checked:
indeterminate:
read-only:
placeholder-shown:
in-range:
out-of-range:
autofill:
```

Example:

```html
<input
  class="
    border-gray-300
    user-invalid:border-red-500
    disabled:bg-gray-100
    disabled:text-gray-500
  "
>
```

---

# 91. `has-*`

```html
<label class="has-checked:bg-blue-50">
  <input type="radio">
</label>
```

Maps tới CSS parent-aware `:has()`.

Also:

```text
has-[img]:
has-[:focus]:
```

Use browser state instead of JS class nếu state đã biểu diễn trong DOM.

---

# 92. `group-*`

Parent:

```html
<a class="group">
```

Child:

```html
<span class="group-hover:text-blue-600">
```

Supports:
- hover,
- focus,
- active,
- has-related conditions.

Named groups:

```text
group/card
group-hover/card:
```

rất quan trọng khi nested groups.

---

# 93. `peer-*`

```html
<input class="peer" type="email">
<p class="invisible peer-invalid:visible">
  Invalid
</p>
```

Peer target phải nằm **sau peer** vì CSS sibling-selector direction.

---

# 94. `in-*`

`in-focus:*` có thể react với matching ancestor mà không cần explicit `group`.

Convenient nhưng ít precise hơn named `group`.

---

# 95. `not-*`

```html
<button class="hover:not-focus:bg-blue-700">
```

Maps tới CSS `:not()` composition.

---

# 96. Child variants

Direct children:

```html
<ul class="*:rounded-full *:px-2">
```

Concept:
```css
:is(& > *)
```

All descendants:

```text
**:
```

Nếu bạn control child markup, class trực tiếp trên child thường dễ override/debug hơn.

---

# 97. ARIA variants

```html
<button
  aria-pressed="true"
  class="aria-pressed:bg-blue-600"
>
```

Useful common states:

```text
aria-busy
aria-checked
aria-disabled
aria-expanded
aria-hidden
aria-pressed
aria-readonly
aria-required
aria-selected
```

ARIA phải phản ánh semantic/accessibility state thật, không chỉ là CSS hook.

---

# 98. Data variants

```html
<div
  data-state="open"
  class="data-[state=open]:opacity-100"
>
```

Pattern:

```text
application state
→ data/ARIA attribute
→ Tailwind variant
```

Use:
- `aria-*` khi semantic accessibility state,
- `data-*` cho application/presentation state.

---

# 99. Dark mode [CORE]

Default:

```html
<div class="bg-white text-gray-950 dark:bg-gray-950 dark:text-white">
```

`dark:` mặc định theo `prefers-color-scheme`.

Manual class-driven:

```css
@custom-variant dark
  (&:where(.dark, .dark *));
```

Data attribute:

```css
@custom-variant dark
  (&:where(
    [data-theme=dark],
    [data-theme=dark] *
  ));
```

---

# 100. User/environment variants

Important:

```text
motion-safe:
motion-reduce:
contrast-more:
contrast-less:
forced-colors:
print:
portrait:
landscape:
pointer-fine:
pointer-coarse:
any-pointer-fine:
any-pointer-coarse:
noscript:
```

Target capability/preference thay vì đoán device.

---

# 101. `supports-*`

```html
<div class="supports-[display:grid]:grid">
```

Negative:

```html
<div class="not-supports-[display:grid]:flex">
```

Maps tới CSS `@supports`.

---

# 102. Variant stacking

```html
<button class="dark:md:hover:bg-fuchsia-600">
```

Mỗi variant transform selector/at-rule context. Đây không chỉ là prefix trang trí.

---

# 103. `@variant` [ADV]

Trong custom CSS:

```css
.button {
  background: var(--color-sky-500);

  @variant dark {
    background: black;
  }
}
```

V4.3 supports stacked:

```css
@variant hover:focus {
  ...
}
```

Multiple:

```css
@variant hover, focus {
  ...
}
```

---

# 104. `@custom-variant`

```css
@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Use:

```html
<div class="theme-midnight:bg-black">
```

Complex:

```css
@custom-variant any-hover {
  @media (any-hover:hover) {
    &:hover {
      @slot;
    }
  }
}
```

---

# 105. `@utility`

```css
@utility content-auto {
  content-visibility: auto;
}
```

Use:

```text
content-auto
hover:content-auto
lg:content-auto
```

`@utility` đăng ký utility thật trong Tailwind utility layer.

---

# 106. Functional utility

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

`--value()` là Tailwind **build-time resolver**, không phải browser CSS function.

Có thể match:
- theme values,
- bare values,
- literal values,
- arbitrary values.

---

# 107. `--default()` [V4.3]

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

Supports:

```text
tab   → 4
tab-2 → 2
```

---

# 108. `--modifier()`

Functional utility modifier:

```text
text-lg/7
```

Value:
```text
lg
```

Modifier:
```text
7
```

Custom APIs có thể dùng `--modifier()` để resolve secondary value.

---

# 109. `@apply`

```css
.select2-dropdown {
  @apply rounded-b-lg shadow-md;
}
```

Good:
- third-party markup,
- custom selector cần Tailwind token/utility.

Avoid:
- recreate mọi reusable component thành `.btn { @apply ... }` khi component/template abstraction tốt hơn.

---

# 110. `@reference` [V4]

Trong Vue/Svelte/CSS Module style context riêng:

```css
@reference "../../app.css";

h1 {
  @apply text-2xl font-bold;
}
```

`@reference` cho Tailwind biết theme/custom utility/custom variant context mà **không duplicate CSS**.

Nếu chỉ cần một token:

```css
color:var(--color-red-500);
```

thường đơn giản và nhanh hơn `@apply`.

---

# 111. `@source`

External/shared source:

```css
@source "../node_modules/@acme/ui-lib";
```

Set base path:

```css
@import "tailwindcss" source("../src");
```

Ignore:

```css
@source not "../src/legacy";
```

Disable automatic:

```css
@import "tailwindcss" source(none);
@source "../admin";
@source "../shared";
```

---

# 112. Safelist v4

Dùng `@source inline()` để force generate class candidates không xuất hiện trong scanned source.

Đừng safelist một universe utilities lớn “phòng khi cần”.

---

# 113. Component extraction [SENIOR]

Repeated button nên thành component:

```jsx
function Button({ variant, children }) {
  const variants = {
    primary:
      "bg-blue-600 text-white hover:bg-blue-700",
    danger:
      "bg-red-600 text-white hover:bg-red-700",
  };

  return (
    <button
      className={`
        inline-flex items-center
        rounded-lg px-4 py-2
        text-sm font-semibold
        focus-visible:outline-2
        ${variants[variant]}
      `}
    >
      {children}
    </button>
  );
}
```

Semantic API outside, Tailwind composition inside.

---

# 114. Component variant design

Recommended dimensions:

```text
variant:
primary | secondary | danger

size:
sm | md | lg

state:
disabled | loading | selected
```

Avoid class/API names combining every dimension:
```text
dangerLargeLoadingOutlined
```

---

# 115. Class conflict

```text
px-2 px-4
```

HTML class token order không đồng nghĩa CSS source order.

Khi dynamic composition phức tạp:
- finite variant maps,
- conflict-aware merge tooling,
- clear override API.

Không dựa vào “class viết sau chắc thắng”.

---

# 116. Conditional helper

Common pattern:

```js
cn(
  "base",
  active && "bg-blue-600",
  disabled && "opacity-50",
)
```

`clsx`-like tools giúp conditional concatenation.

Tailwind conflict-merging libraries là ecosystem, không phải core requirement.

---

# 117. Token vs arbitrary value

Arbitrary tốt:

```text
top-[117px]
```

cho một decoration one-off.

Nếu lặp:

```text
rounded-[11px]
```

nhiều nơi, promote thành token:

```css
@theme {
  --radius-card: 11px;
}
```

Then:

```text
rounded-card
```

---

# 118. Primitive vs semantic token

Primitive:

```text
blue-600
gray-200
space-4
```

Semantic:

```text
action
danger
surface
text-muted
```

Large design system nên cân nhắc semantic layer để theme/rebrand dễ hơn.

---

# 119. Runtime semantic variables

```css
:root {
  --app-surface: var(--color-white);
  --app-text: var(--color-gray-950);
}

[data-theme="dark"] {
  --app-surface: var(--color-gray-950);
  --app-text: var(--color-white);
}
```

Component:

```html
<div class="bg-(--app-surface) text-(color:--app-text)">
```

Rất hiệu quả cho multi-theme design system.

---

# 120. Custom CSS decision

Plain CSS tốt hơn khi:
- selector quá phức tạp,
- third-party markup lớn,
- utility expression khó đọc,
- native feature không cần reusable utility API.

Tailwind không cấm CSS.

---

# 121. `@layer components`

```css
@layer components {
  .card {
    background: var(--color-white);
    border-radius: var(--radius-lg);
  }
}
```

Utilities layer có thể override component layer theo cascade-layer architecture.

V4 `@layer` là native CSS layer; custom Tailwind utility nên dùng `@utility`.

---

# 122. Accessibility [SENIOR]

Tailwind giúp biểu diễn state:

```text
focus-visible:
disabled:
aria-*:
motion-reduce:
forced-colors:
```

Nhưng semantic HTML vẫn phải đúng.

Bad:
```html
<div class="cursor-pointer">
```
thay button.

Good:
```html
<button class="...">
```

---

# 123. Accessible icon button

```html
<button
  class="
    inline-grid
    size-10
    place-items-center
    rounded-full
    hover:bg-gray-100
    focus-visible:outline-2
  "
>
  <svg class="size-5" aria-hidden="true"></svg>
  <span class="sr-only">Close</span>
</button>
```

---

# 124. Responsive page container idiom

```html
<div
  class="
    mx-auto
    w-full
    max-w-7xl
    px-4
    sm:px-6
    lg:px-8
  "
>
```

Self-contained behavior:
- `w-full`: fill available width.
- `max-w-7xl`: cap content width.
- `mx-auto`: center.
- responsive padding: mobile/tablet/desktop gutters.

---

# 125. Stack pattern

```html
<div class="flex flex-col gap-4">
```

Use:
- vertical forms,
- sections,
- lists.

---

# 126. Cluster pattern

```html
<div class="flex flex-wrap items-center gap-2">
```

Use:
- chips,
- button group,
- toolbar.

---

# 127. Media object pattern

```html
<div class="flex gap-4">
  <img class="size-12 shrink-0 rounded-full object-cover">

  <div class="min-w-0 flex-1">
    ...
  </div>
</div>
```

`shrink-0` giữ avatar, `min-w-0 flex-1` cho content co đúng.

---

# 128. Responsive grid

```html
<div
  class="
    grid
    grid-cols-1
    gap-6
    sm:grid-cols-2
    lg:grid-cols-3
  "
>
```

Intrinsic alternative:

```html
<div
  class="
    grid
    grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]
    gap-6
  "
>
```

---

# 129. Container-responsive card

```html
<div class="@container">
  <article
    class="
      flex flex-col
      @md:grid
      @md:grid-cols-[8rem_minmax(0,1fr)]
    "
  >
```

Use khi card sống ở nhiều parent widths.

---

# 130. Sticky header

```html
<header
  class="
    sticky top-0 z-40
    border-b
    bg-white/90
    backdrop-blur
  "
>
```

Nếu không sticky:
- kiểm tra ancestor overflow,
- scroll container,
- inset,
- scroll space.

---

# 131. Modal styling

Ưu tiên native `<dialog>`/proper accessible primitive.

```html
<dialog
  class="
    m-auto
    max-h-[80dvh]
    w-[min(90vw,40rem)]
    overflow-auto
    rounded-2xl
    bg-white
    p-0
    shadow-2xl
    backdrop:bg-black/50
  "
>
```

`backdrop:*` target `::backdrop`.

Tailwind không tự cung cấp focus trap/dialog behavior chỉ vì có classes.

---

# 132. Form field

```html
<label class="grid gap-1.5">
  <span class="text-sm font-medium">Email</span>

  <input
    type="email"
    class="
      rounded-lg
      border border-gray-300
      px-3 py-2
      outline-none
      focus:border-blue-500
      focus:ring-2
      focus:ring-blue-500/20
      user-invalid:border-red-500
      disabled:bg-gray-100
    "
  >
</label>
```

---

# 133. Carousel

```html
<div
  class="
    flex
    snap-x
    snap-mandatory
    gap-4
    overflow-x-auto
  "
>
  <article class="min-w-80 snap-start">
    ...
  </article>
</div>
```

---

# 134. Tailwind + React

Rules:
- complete class strings,
- variant map,
- component extraction,
- `className`.

Avoid:

```jsx
`p-${size}`
```

unless every result is explicitly present/safelisted.

---

# 135. Tailwind + Vue/Svelte

Template classes work naturally.

Separate `<style>` block with `@apply` may cần `@reference`.

Nếu chỉ cần token, dùng CSS variable trực tiếp.

---

# 136. Tailwind + CSS Modules

Có thể coexist.

Tailwind utilities:
- layout/visual composition in markup.

CSS Modules:
- scoped complex CSS.

Không cần dùng cả hai cho cùng một đơn giản concern nếu không có lợi ích.

---

# 137. Tailwind + SCSS

Tailwind v4 là CSS-first.

SCSS có thể coexist nhưng hãy phân trách nhiệm:

```text
Tailwind:
utilities/theme/variants

SCSS:
compile-time maps/functions/mixins
```

Tránh 3 source-of-truth token:
- Sass map,
- Tailwind theme,
- CSS vars
độc lập.

---

# 138. Migration v3 → v4 mindset

```text
JS config-first
→ CSS-first

content globs
→ automatic detection/@source

theme.extend
→ @theme

custom @layer utility
→ @utility

safelist
→ @source inline()

leading important prefix
→ trailing !
```

`@config` / `@plugin` là bridge cho migration.

---

# 139. `@config`

```css
@config "../../tailwind.config.js";
```

Load legacy JS config.

Use để migrate từng bước, không phải target cuối cho project mới.

---

# 140. `@plugin`

```css
@plugin "@tailwindcss/typography";
```

Load legacy JS plugin ecosystem.

Project-owned simple extension nên ưu tiên CSS-first APIs khi hợp lý.

---

# 141. Production architecture

```text
theme.css
→ design vocabulary

app.css
→ Tailwind import + shared base/integrations

components/
→ semantic reusable UI

features/
→ app composition

data/ARIA attributes
→ runtime state

@source
→ build ownership
```

---

# 142. Performance mental model

Tailwind output dựa trên detected candidates.

Main risks:
- huge safelist,
- scanning irrelevant monorepo trees,
- multiple Tailwind bundles,
- massive unique arbitrary values,
- excessive separate `@apply` processing.

Class-heavy HTML không đồng nghĩa CSS bundle huge.

---

# 143. Debug missing class

Checklist:

```text
1. class complete/static?
2. file scanned?
3. file ignored?
4. theme token exists?
5. utility valid?
6. @source needed?
7. custom utility registered?
8. separate style context needs @reference?
9. generated CSS contains rule?
```

---

# 144. Debug class exists but no effect

Chuyển sang CSS debugging:

```text
computed style
→ cascade/layer
→ specificity
→ layout context
→ parent constraint
→ overflow
→ stacking context
→ browser support
```

---

# 145. Anti-patterns

## Dynamic synthesis

```text
bg-${color}-600
```

## Arbitrary everything

```text
p-[13px]
rounded-[11px]
text-[15.3px]
```

lặp lại.

## `@apply` everything

Biến Tailwind thành semantic CSS indirection layer.

## Device breakpoints

```text
iphone:
ipad:
```

thay vì content-driven.

## Utility soup duplicated everywhere

Extract component.

## Tailwind replacing semantics

`div.cursor-pointer` ≠ button.

---

# 146. Senior PR checklist

## Utility correctness
- utility map đúng CSS?
- `min-w-0` / `min-h-0` cần không?
- physical hay logical?
- viewport hay container?
- arbitrary có thật sự one-off?

## Architecture
- static detectable?
- repeated combination nên component?
- token nên promote?
- custom CSS rõ hơn?
- `@apply` cần không?

## Accessibility
- semantic HTML?
- focus visible?
- disabled real?
- reduced motion?
- contrast?
- DOM order?

## Performance
- source scope?
- safelist?
- duplicate bundle?
- custom utilities output?

---

# 147. Learning roadmap

## Beginner
```text
spacing
sizing
display
Flexbox
Grid
typography
colors
borders
responsive
hover/focus
```

## Intermediate
```text
arbitrary values
group/peer/has
dark
container queries
@theme
@source
@utility
component variants
```

## Senior
```text
CSS-first architecture
theme API
static detection
custom variants
functional utilities
runtime semantic tokens
monorepo/package sources
migration
accessibility
performance
```

---

# 148. Senior self-test

1. Tailwind utility khác inline style?
2. Zero-runtime nghĩa gì?
3. `@theme` khác `:root` variable?
4. Namespace tạo utility thế nào?
5. Vì sao dynamic class interpolation lỗi?
6. `@source` dùng khi nào?
7. `source(none)` dùng khi nào?
8. Arbitrary value/property/variant khác nhau?
9. CSS variable shorthand là gì?
10. Type hint dùng khi nào?
11. `md:` khác `@md:`?
12. `@container-size` khác `@container`?
13. `group` vs `peer`?
14. Vì sao peer phải trước target?
15. `has-*` map tới CSS gì?
16. `*:` vs `**:`?
17. Dark mặc định dựa vào gì?
18. Manual dark cấu hình sao?
19. `@utility` khác `.class`?
20. `--value()` là gì?
21. `--modifier()` là gì?
22. `@variant` dùng khi nào?
23. `@custom-variant` dùng khi nào?
24. `@reference` giải quyết gì?
25. `@apply` nên dùng khi nào?
26. Preflight làm gì?
27. Cascade layers Tailwind?
28. `min-w-0` fix gì?
29. `min-h-0` fix gì?
30. `gap` vs `space-*`?
31. Ring vs outline?
32. hidden/invisible/opacity-0?
33. h-screen vs h-dvh?
34. Logical utilities có lợi gì?
35. Scrollbar utilities v4.3?
36. zoom vs scale?
37. font-features khi nào?
38. Token vs arbitrary?
39. Promote arbitrary thành token khi nào?
40. Component extraction vs @apply?
41. CSS Modules coexist?
42. SCSS coexist?
43. @config/@plugin là gì?
44. HTML class order có quyết định conflict?
45. Runtime values bridge bằng CSS var thế nào?
46. ARIA vs data variant?
47. Tailwind có polyfill CSS feature không?
48. Tailwind senior cần hiểu CSS gì?
49. Khi nào plain CSS tốt hơn?
50. Architecture production nên phân responsibility thế nào?

---

# 149. Quick cheat sheet

```html
<div class="flex items-center gap-4">
<div class="grid grid-cols-3 gap-6">

<div class="w-full max-w-7xl">
<div class="min-w-0 flex-1">

<div class="mx-auto px-4 py-6">

<h1 class="text-3xl font-bold tracking-tight">
<p class="text-sm leading-relaxed text-gray-600">

<div class="rounded-xl border border-gray-200 bg-white shadow-sm">

<button class="hover:bg-blue-700 focus-visible:outline-2 disabled:opacity-50">

<div class="grid-cols-1 md:grid-cols-2 xl:grid-cols-4">

<div class="@container">
  <div class="@md:flex-row">

<div class="bg-white dark:bg-gray-950">

<div class="w-[37rem]">
<div class="[mask-type:luminance]">

<div class="bg-(--surface)">

<a class="group">
  <span class="group-hover:underline">

<input class="peer">
<p class="peer-invalid:block">

<label class="has-checked:bg-blue-50">
```

---

# 150. Official references

- https://tailwindcss.com/docs
- https://tailwindcss.com/docs/installation
- https://tailwindcss.com/docs/styling-with-utility-classes
- https://tailwindcss.com/docs/hover-focus-and-other-states
- https://tailwindcss.com/docs/responsive-design
- https://tailwindcss.com/docs/dark-mode
- https://tailwindcss.com/docs/theme
- https://tailwindcss.com/docs/adding-custom-styles
- https://tailwindcss.com/docs/detecting-classes-in-source-files
- https://tailwindcss.com/docs/functions-and-directives
- https://tailwindcss.com/docs/preflight
- https://tailwindcss.com/docs/upgrade-guide
- https://tailwindcss.com/blog/tailwindcss-v4-3

---

# Kết luận

Học Tailwind theo chuỗi:

```text
utility
→ CSS behavior
→ token
→ variant
→ component
→ architecture
```

Senior không hỏi chỉ:
> “class nào làm việc này?”

Senior còn hỏi:
> “behavior CSS là gì, state thuộc ai, token có đúng không, responsive theo viewport hay container, và abstraction nên nằm ở utility hay component?”
