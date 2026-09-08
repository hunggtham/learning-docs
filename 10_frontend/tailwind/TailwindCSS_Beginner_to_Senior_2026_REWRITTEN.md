# Tailwind CSS — Beginner → Senior, bản giải thích đầy đủ
## Modern Tailwind CSS v4.3 — học từ nền tảng đến production architecture

> Đây là bản viết lại hoàn toàn của tài liệu Tailwind trước. Tài liệu được viết cho người muốn **học để hiểu**, không phải người đã biết Tailwind và chỉ cần cheat sheet.
>
> Baseline của tài liệu là **Tailwind CSS v4.3**. Khi một nội dung liên quan trực tiếp đến CSS, tài liệu sẽ giải thích CSS cần thiết ngay tại chỗ thay vì yêu cầu bạn quay về tài liệu CSS khác.
>
> Cách đọc xuyên suốt tài liệu:
>
> ```text
> Tailwind syntax
> → Tailwind hiểu class đó như thế nào
> → CSS được sinh ra có ý nghĩa gì
> → browser xử lý CSS đó ra sao
> → ví dụ thực tế
> → pattern / senior note
> ```
>
> Mục tiêu sau khi học xong file này là bạn có thể đọc một component Tailwind production, tự thiết kế layout, responsive UI, form, state, dark mode, container query, theme, custom utility và biết khi nào nên dùng Tailwind, khi nào nên quay về CSS thuần.

---

# PHẦN I — HIỂU TAILWIND TỪ GỐC

## 1. Tailwind CSS thực sự là gì?

Tailwind CSS là một framework CSS theo hướng **utility-first**. “Utility” ở đây có nghĩa là một class thường làm một nhiệm vụ tương đối nhỏ và rõ ràng. Ví dụ, `flex` bật Flexbox, `items-center` căn các flex item theo cross axis, `p-4` tạo padding, còn `rounded-xl` tạo bo góc. Thay vì đặt một class có tên theo component rồi viết toàn bộ CSS trong một file riêng, Tailwind khuyến khích bạn ghép các utility trực tiếp tại nơi bạn viết markup.

Ví dụ với CSS truyền thống, bạn có thể viết:

```css
.profile-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  border-radius: 0.75rem;
  background: white;
  box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
}
```

Sau đó HTML chỉ cần:

```html
<div class="profile-card">
  ...
</div>
```

Trong Tailwind, cùng ý tưởng đó có thể được viết:

```html
<div
  class="
    flex
    items-center
    gap-4
    rounded-xl
    bg-white
    p-6
    shadow-sm
  "
>
  ...
</div>
```

Điểm cần hiểu là Tailwind không tạo ra một cơ chế layout mới. `flex` vẫn trở thành CSS `display: flex`; `gap-4` vẫn trở thành CSS `gap`; browser vẫn chạy đúng các thuật toán Flexbox, Grid, cascade, sizing và painting của CSS. Tailwind chỉ thay đổi **cách bạn author CSS**.

Một mental model rất quan trọng là:

```text
Tailwind = ngôn ngữ đặt tên utility ở tầng authoring
CSS      = ngôn ngữ thực thi ở browser
```

Nếu một layout không hoạt động mặc dù class Tailwind đã được generate, nguyên nhân thường không còn là Tailwind nữa mà nằm ở CSS thật bên dưới. Senior Tailwind vì vậy phải biết khi nào debug framework và khi nào debug browser.

---

## 2. Utility-first khác “inline style” như thế nào?

Nhìn bề ngoài, một element có nhiều class Tailwind có thể làm bạn liên tưởng đến inline style:

```html
<button class="rounded-lg bg-blue-600 px-4 py-2 text-white">
```

Nhưng utility class không giống:

```html
<button
  style="
    border-radius: .5rem;
    background: blue;
    padding: .5rem 1rem;
    color: white;
  "
>
```

Inline style là declaration gắn trực tiếp trên element. Nó không có cách tự nhiên để viết `:hover`, `:focus-visible`, `@media`, `@container`, `prefers-reduced-motion` hoặc selector quan hệ như `:has()`.

Tailwind utility thì có thể kết hợp variant:

```html
<button
  class="
    rounded-lg
    bg-blue-600
    px-4
    py-2
    text-white
    hover:bg-blue-700
    focus-visible:outline-2
    md:px-6
    dark:bg-blue-500
  "
>
```

Tailwind sẽ generate CSS tương đương với các pseudo-class và media query cần thiết. Vì vậy utility-first vẫn là stylesheet-based CSS, chỉ khác cách bạn gọi các rule.

---

## 3. Tailwind v4.3 khác Tailwind v3 như thế nào?

Nếu bạn tìm tutorial cũ, bạn sẽ thấy Tailwind v3 thường cấu hình bằng `tailwind.config.js`:

```js
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

Tailwind v4 chuyển mạnh sang **CSS-first configuration**. Một project mới thường bắt đầu bằng:

```css
@import "tailwindcss";
```

Sau đó design token có thể được khai báo trực tiếp bằng `@theme`:

```css
@theme {
  --color-brand: #2563eb;
}
```

Khi token `--color-brand` thuộc namespace `--color-*`, Tailwind hiểu đây là color token và từ đó có thể tạo các utility như:

```text
bg-brand
text-brand
border-brand
fill-brand
stroke-brand
```

V4 cũng có automatic source detection, nghĩa là phần lớn project không còn cần liệt kê `content` glob như v3. Khi cần source đặc biệt, bạn dùng `@source`.

Custom utility và custom variant cũng chuyển sang CSS-first:

```css
@utility content-auto {
  content-visibility: auto;
}

@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Bạn vẫn có thể gặp `@config` và `@plugin` để tương thích với hệ sinh thái hoặc migrate project v3, nhưng tư duy nên học cho code mới là CSS-first.

---

## 4. Cài Tailwind và hiểu build pipeline

Với Vite, setup cơ bản hiện đại thường là:

```bash
npm install tailwindcss @tailwindcss/vite
```

Sau đó thêm plugin:

```js
import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [tailwindcss()],
});
```

Trong stylesheet chính:

```css
@import "tailwindcss";
```

Nếu dùng CLI:

```bash
npm install tailwindcss @tailwindcss/cli
```

và compile bằng:

```bash
npx @tailwindcss/cli \
  -i ./src/input.css \
  -o ./dist/output.css \
  --watch
```

Điểm cần hiểu là Tailwind không chạy trong browser để đọc class rồi style element. Tailwind chạy ở **build time**. Nó scan source code, nhận ra các class có khả năng là Tailwind utility, generate CSS cần thiết và browser chỉ nhận stylesheet cuối.

Pipeline có thể hình dung:

```text
HTML / JSX / Vue / Svelte
        │
        ▼
Tailwind source scanner
        │
        ▼
utility + variant resolver
        │
        ▼
generated CSS
        │
        ▼
browser
```

Vì vậy nếu bạn viết một class mà Tailwind không nhận ra ở build time, CSS tương ứng sẽ không tồn tại dù string đó xuất hiện runtime.

---

## 5. `@import "tailwindcss"` và các cascade layer

Một dòng:

```css
@import "tailwindcss";
```

không đơn giản là import một file CSS tĩnh khổng lồ. Tailwind v4 dùng các native CSS cascade layer quan trọng như:

```text
theme
base
components
utilities
```

`theme` chứa design tokens. `base` chứa Preflight và base rules. `components` dành cho component-level custom styles. `utilities` chứa utility rules.

CSS cascade layer giải quyết thứ tự ưu tiên giữa các nhóm rule. Trong cùng author origin với normal declarations, layer xuất hiện sau thường có priority cao hơn layer trước. Vì utilities nằm sau components, một utility như `p-6` có thể override padding được đặt trong component layer mà không cần tăng specificity.

Điều này giải thích một nguyên tắc senior: Tailwind cố gắng thắng bằng **architecture của cascade** thay vì tạo selector specificity rất cao.

---

## 6. Preflight là gì và tại sao HTML trông “khác bình thường”?

Tailwind import mặc định bao gồm một base reset gọi là **Preflight**. Browser vốn có user-agent stylesheet, nghĩa là `<h1>` tự có font-size và margin, `<ul>` tự có bullet, `<body>` có margin mặc định, button/input có một số style native.

Preflight normalize nhiều thứ để UI bắt đầu từ nền tảng dễ kiểm soát hơn. Vì vậy nếu bạn viết:

```html
<h1>Hello</h1>
```

và thấy nó không to, đậm, có margin giống HTML thuần, đó là behavior có chủ ý. Tailwind muốn bạn nói rõ design:

```html
<h1 class="text-3xl font-bold tracking-tight">
  Hello
</h1>
```

Preflight rất tiện trong app mới, nhưng có thể gây xung đột khi nhúng Tailwind vào một hệ thống cũ đã có reset hoặc một widget chạy bên trong host page. Trong trường hợp đó, senior cần cân nhắc import các phần Tailwind một cách có kiểm soát thay vì mặc định dùng full Preflight.

---

## 7. Cấu trúc một Tailwind class

Hãy phân tích:

```text
md:hover:bg-blue-600/80
```

Phần `bg-blue-600` là utility chính. `bg-` nói rằng utility ảnh hưởng background; `blue-600` là theme value. `/80` là modifier opacity/alpha trong family này. `hover:` thêm điều kiện hover. `md:` thêm điều kiện responsive breakpoint.

Bạn nên đọc từ ngoài vào trong theo ý nghĩa:

```text
khi viewport đạt md
và element đang hover
thì background dùng blue-600 với alpha 80%
```

Một class khác:

```text
w-[37rem]
```

có utility family `w-` và arbitrary value `[37rem]`.

Một class:

```text
text-(color:--label)
```

dùng CSS variable `--label` và type hint `color` để nói rõ rằng `text-*` ở đây là text color chứ không phải font-size.

Tailwind class vì vậy có grammar tương đối nhất quán. Khi hiểu grammar, bạn không cần thuộc mọi class.

---

## 8. Spacing scale và vì sao `p-4` không phải “4px”

Một trong những hiểu nhầm đầu tiên là nghĩ `p-4` bằng `padding: 4px`. Trong Tailwind v4, nhiều spacing utilities được derive từ base spacing theme. Mặc định, `--spacing` thường có basis là `0.25rem`.

Do đó:

```text
p-1 ≈ 0.25rem
p-2 ≈ 0.5rem
p-4 ≈ 1rem
p-6 ≈ 1.5rem
p-8 ≈ 2rem
```

Nếu root font-size mặc định là 16px thì `1rem` thường tương ứng 16 CSS pixels, nhưng hãy nhớ `rem` là font-relative unit, không phải hard-coded px.

Tailwind v4 linh hoạt hơn v3 trong nhiều numeric utility families. Những value như:

```text
mt-17
w-29
```

có thể được derive từ spacing system nếu utility family đó hỗ trợ. Điều này rất tiện, nhưng senior không nên biến sự linh hoạt của compiler thành một design system hỗn loạn. Framework cho phép `p-13` không có nghĩa UI nên có spacing 13 ở khắp nơi.

---

## 9. Arbitrary values: escape hatch cần thiết nhưng không phải design system

Khi utility token không có đúng value bạn cần, Tailwind cho phép arbitrary value:

```html
<div class="top-[117px]">
```

CSS được generate về bản chất là:

```css
top: 117px;
```

Bạn vẫn dùng variant bình thường:

```html
<div class="top-[117px] lg:top-[344px]">
```

Arbitrary value rất phù hợp cho những exception như vị trí một decorative illustration, một grid template phức tạp hoặc kích thước được quy định chính xác bởi asset.

Nhưng nếu toàn project có:

```text
rounded-[11px]
text-[15px]
p-[13px]
gap-[18px]
```

lặp đi lặp lại, bạn đang mất lợi ích của design token. Khi một arbitrary value bắt đầu trở thành vocabulary lặp lại, hãy promote nó thành theme token.

Ví dụ:

```css
@theme {
  --radius-card: 11px;
}
```

Sau đó:

```html
<div class="rounded-card">
```

Đây là pattern:

```text
one-off exception
→ xuất hiện lặp lại
→ trở thành token
```

---

## 10. Arbitrary properties

Không phải mọi CSS property đều cần một named Tailwind utility. Bạn có thể viết property trực tiếp:

```html
<div class="[mask-type:luminance]">
```

Tailwind generate:

```css
mask-type: luminance;
```

Có thể kết hợp state:

```html
<div class="hover:[mask-type:alpha]">
```

Hoặc đặt CSS variable:

```html
<div class="[--header-offset:56px] lg:[--header-offset:72px]">
```

Arbitrary property là cách rất mạnh để dùng ngay CSS platform mà không phải viết custom plugin cho một case nhỏ.

Senior cần tránh một cực đoan khác: đừng biến class attribute thành một stylesheet hoàn chỉnh bằng hàng chục arbitrary properties. Nếu một rule phức tạp rõ ràng hơn khi viết CSS, hãy viết CSS.

---

## 11. Arbitrary variants

Arbitrary variant cho phép bạn viết selector condition trực tiếp.

```html
<div class="[&>p]:mt-4">
  <p>...</p>
</div>
```

`&` đại diện cho element hiện tại. Ý nghĩa gần:

```css
.current > p {
  margin-top: 1rem;
}
```

Một selector phức tạp hơn:

```html
<ul class="[&_li:nth-child(odd)]:bg-gray-50">
```

Tailwind thay `_` thành whitespace khi phù hợp, nên selector gần:

```css
.current li:nth-child(odd) {
  background-color: ...;
}
```

Arbitrary variants tuyệt vời cho integration ngắn hoặc markup bạn không kiểm soát. Nhưng nếu selector lặp đi lặp lại, hãy cân nhắc `@custom-variant`, component abstraction hoặc stylesheet integration riêng.

---

## 12. CSS variable shorthand và runtime value

Một pattern cực quan trọng là kết hợp Tailwind static utility với CSS variable dynamic value.

Ví dụ:

```html
<div class="w-(--panel-width)">
```

Tailwind hiểu gần như:

```css
width: var(--panel-width);
```

React có thể set variable:

```jsx
<div
  style={{ "--panel-width": `${width}px` }}
  className="w-(--panel-width)"
/>
```

Điểm mạnh là class `w-(--panel-width)` tồn tại hoàn chỉnh ở source nên Tailwind generate được CSS, trong khi giá trị `width` có thể thay đổi runtime.

Pattern này tốt hơn:

```jsx
className={`w-[${width}px]`}
```

vì string arbitrary class runtime có thể không được scanner nhìn thấy.

---

## 13. Tailwind scan source như text, không chạy code của bạn

Đây là kiến thức bắt buộc.

Code sai:

```jsx
function Button({ color }) {
  return (
    <button
      className={`bg-${color}-600`}
    />
  );
}
```

Khi scan source, Tailwind chỉ thấy các fragment `bg-`, `${color}`, `-600`. Nó không biết runtime prop sẽ là `blue`, `red` hay `green`.

Cách đúng:

```jsx
const colorVariants = {
  blue:
    "bg-blue-600 hover:bg-blue-700 text-white",
  red:
    "bg-red-600 hover:bg-red-700 text-white",
};

function Button({ color }) {
  return (
    <button className={colorVariants[color]} />
  );
}
```

Các complete class strings đã nằm trong source, nên scanner nhận được.

Đây đồng thời là component design tốt hơn: component chỉ cho phép một tập variant hữu hạn thay vì cho caller tạo arbitrary Tailwind class.

---

# PHẦN II — LAYOUT VÀ BOX MODEL TRONG TAILWIND

## 14. `display`: hiểu `block`, `inline`, `flex`, `grid` trước khi dùng

CSS `display` quyết định element tham gia layout theo kiểu nào. Tailwind cung cấp những utility trực tiếp như:

```text
block
inline
inline-block
flex
inline-flex
grid
inline-grid
flow-root
contents
hidden
```

`block` tạo block-level box, thường chiếm available inline width theo normal flow. `inline` chạy trong dòng text và width/height không hoạt động giống block. `inline-block` giữ khả năng đứng trong inline flow nhưng có box sizing giống block hơn.

`flex` tạo flex container. Children trực tiếp trở thành flex items. `grid` tạo grid container. `hidden` đặt `display: none`, nghĩa là element bị loại khỏi layout; đây khác hoàn toàn với `invisible` hay `opacity-0`.

Ví dụ responsive visibility:

```html
<nav class="hidden md:block">
  ...
</nav>
```

Ở base/mobile, nav không có box. Từ breakpoint `md`, Tailwind generate rule `display: block`.

---

## 15. `hidden`, `invisible`, `opacity-0` khác nhau

Ba utility này thường bị dùng như nhau nhưng behavior rất khác.

```text
hidden
```

tương đương `display:none`. Element không chiếm layout và thông thường không tham gia accessibility tree như element hiển thị.

```text
invisible
```

tương đương `visibility:hidden`. Box vẫn chiếm chỗ, nhưng không được vẽ/interaction bình thường.

```text
opacity-0
```

tương đương `opacity:0`. Element vẫn tồn tại trong layout và có thể vẫn nhận pointer/focus tùy semantics.

Nếu bạn muốn animate fade, `opacity-0` thường phù hợp hơn vì `display:none` không đơn giản transition như opacity. Nếu bạn muốn bỏ element khỏi layout, `hidden` phù hợp hơn.

---

## 16. Box sizing: `box-border` và `box-content`

CSS width mặc định theo content box có thể gây nhầm. Nếu element:

```css
width: 300px;
padding: 20px;
border: 1px solid;
```

với `content-box`, tổng outer width lớn hơn 300px.

Tailwind Preflight thường làm sizing predictable hơn, nhưng bạn vẫn nên hiểu:

```text
box-border
→ box-sizing:border-box
```

và:

```text
box-content
→ box-sizing:content-box
```

Với `border-box`, declared width đã bao gồm padding và border. Đây là model thường dễ dùng hơn trong UI.

---

## 17. Position: `relative`, `absolute`, `fixed`, `sticky`

`relative` thường được dùng để tạo positioning context cho `absolute` child:

```html
<div class="relative">
  <span
    class="
      absolute
      right-2
      top-2
    "
  >
    New
  </span>
</div>
```

Parent vẫn nằm trong normal flow. Child `absolute` được lấy ra khỏi normal flow và offset theo containing block phù hợp, ở đây thường là parent `relative`.

`fixed` thường gắn theo viewport và dùng cho full-screen overlay, floating button hoặc persistent UI.

`sticky` rất hay bị hiểu sai. Nó không đơn giản là “fixed khi scroll”. Sticky phụ thuộc scroll container và inset. Ví dụ:

```html
<header class="sticky top-0">
```

cần `top-0` làm sticky threshold. Nếu ancestor có overflow tạo scroll container khác, sticky sẽ liên quan container đó. Khi `sticky` không chạy, hãy kiểm tra scroll container trước khi thêm class ngẫu nhiên.

---

## 18. Inset và logical inset

Các class:

```text
top-4
right-4
bottom-4
left-4
inset-0
inset-x-4
inset-y-4
```

map trực tiếp tới CSS positional offsets.

V4.2+ có logical utilities như:

```text
inset-s-4
inset-e-4
inset-bs-4
inset-be-4
```

`inline-start` trong giao diện LTR thường là trái, nhưng trong RTL có thể là phải. Vì vậy logical utilities phù hợp với app đa ngôn ngữ.

Nếu mục tiêu là “icon ở cuối dòng” chứ không phải “icon luôn ở cạnh phải vật lý”, logical utility tốt hơn.

---

## 19. `z-*` và stacking context

Tailwind cung cấp:

```text
z-0
z-10
z-20
...
z-50
z-auto
z-[999]
```

Nhưng `z-index` chỉ có ý nghĩa trong stacking model của CSS. Một child `z-[9999]` vẫn có thể nằm dưới một element khác nếu parent của nó đang nằm trong stacking context thấp hơn.

Do đó khi modal/dropdown bị che, đừng tăng `z-index` vô hạn. Hãy kiểm tra ancestor có:
- transform,
- opacity,
- isolation,
- positioned + z-index,
- filter,
hay property khác tạo stacking context hay không.

Trong design system lớn, nên có semantic layer contract cho dropdown, sticky header, overlay, modal và toast thay vì mỗi component chọn số tùy ý.

---

## 20. Overflow và scroll container

Tailwind có:

```text
overflow-auto
overflow-hidden
overflow-clip
overflow-visible
overflow-scroll
overflow-x-auto
overflow-y-auto
```

`overflow-auto` tạo scroll khi content thực sự vượt box. `overflow-hidden` clip content và có scroll-container semantics khác `overflow-clip`. `overflow-clip` chỉ clip theo intent mạnh hơn, không phải là một scroll container như hidden.

Một pattern cực phổ biến cho bảng:

```html
<div class="overflow-x-auto">
  <table class="min-w-full">
    ...
  </table>
</div>
```

Wrapper chịu horizontal scroll thay vì làm cả page overflow.

Senior phải nhớ overflow ảnh hưởng nhiều thứ khác ngoài scrollbar, đặc biệt là sticky positioning và clipping.

---

## 21. Width: `w-*` không chỉ có px

Tailwind width family bao gồm spacing-derived values, fraction, percentages, viewport và intrinsic sizing.

```text
w-4
w-64
w-full
w-1/2
w-screen
w-dvw
w-min
w-max
w-fit
w-[37rem]
```

`w-full` thường là `width:100%` của containing block. `w-screen` là viewport width kiểu `100vw`; `w-dvw` dùng dynamic viewport width.

`w-min` tương ứng intrinsic `min-content`. `w-max` tương ứng `max-content`. `w-fit` dùng `fit-content`.

Khi bạn chọn width, hãy nghĩ “constraint nào cần?” thay vì mặc định đặt số px.

---

## 22. Height và viewport units: `h-screen` không phải lúc nào cũng tốt nhất

`h-screen` tương đương classic `100vh`. Trên mobile browser, UI chrome như address bar có thể làm viewport thay đổi và `100vh` gây layout không đúng như mong muốn.

Modern utilities:

```text
h-dvh
h-svh
h-lvh
min-h-dvh
```

liên hệ tới dynamic, small và large viewport units.

Một full-page mobile layout thường tốt hơn với:

```html
<div class="min-h-dvh">
```

thay vì ép `h-screen`, vì minimum height cho phép content dài thêm và `dvh` phản ánh viewport động tốt hơn.

---

## 23. `max-w-*` và readable content

Tailwind có các max width token như:

```text
max-w-sm
max-w-md
max-w-lg
max-w-7xl
max-w-prose
max-w-full
max-w-none
```

`max-w-prose` rất hữu ích cho text body vì một dòng quá dài sẽ khó đọc. Đây không phải magic “prose component”, mà chỉ là width constraint được thiết kế quanh readable line measure.

Page container thường:

```html
<div class="mx-auto w-full max-w-7xl px-4 sm:px-6 lg:px-8">
  ...
</div>
```

`w-full` cho phép full available width, `max-w-7xl` cap lại, `mx-auto` center khi còn free space, còn `px-*` tạo gutter.

---

## 24. `min-w-0`: một class nhỏ nhưng cực kỳ senior

Hãy xem:

```html
<div class="flex gap-3">
  <img class="size-10 shrink-0">

  <div class="flex-1">
    <p class="truncate">
      A very very very long text...
    </p>
  </div>
</div>
```

Nhiều dev nghĩ `truncate` sẽ tự ellipsis. Nhưng flex item có automatic minimum size dựa trên intrinsic content. Child `.flex-1` có thể từ chối co nhỏ hơn content cần, khiến `truncate` không hoạt động như mong đợi.

Fix:

```html
<div class="min-w-0 flex-1">
```

`min-w-0` nói rằng minimum width được phép là 0 thay vì content-based automatic minimum. Sau đó overflow/ellipsis mới có không gian để hoạt động.

Đây là một trong những utility bạn nên hiểu bản chất thay vì học thuộc.

---

## 25. `min-h-0`: phiên bản vertical của cùng vấn đề

Một layout dashboard:

```html
<div class="flex h-dvh flex-col">
  <header class="shrink-0">
    ...
  </header>

  <main class="min-h-0 flex-1 overflow-auto">
    ...
  </main>
</div>
```

Nếu `main` không có `min-h-0`, automatic minimum size trong flex column có thể làm main không chịu co và toàn page overflow. `min-h-0` cho phép vùng còn lại co đúng để `overflow-auto` tạo scroller nội bộ.

Pattern này rất phổ biến trong:
- app shell,
- modal body,
- sidebar panel,
- chat interface.

---

## 26. Margin

Tailwind margin:

```text
m-4
mx-4
my-4
mt-4
mr-4
mb-4
ml-4
ms-4
me-4
-mt-4
mx-auto
```

`m-*` áp mọi cạnh. `mx-*` và `my-*` là shorthand hai trục. `ms-*` và `me-*` là logical inline start/end. Prefix `-` tạo negative margin khi CSS property cho phép.

`mx-auto` là idiom center một block đã có width/max-width:

```html
<div class="mx-auto max-w-4xl">
```

Negative margin nên dùng có chủ ý, thường cho overlap/visual composition. Nếu bạn liên tục cần negative margin để “sửa vị trí”, có thể layout architecture đang sai.

---

## 27. Padding

Padding utilities tương tự:

```text
p-4
px-4
py-4
pt-4
pr-4
pb-4
pl-4
ps-4
pe-4
```

Padding thuộc box của chính element và không thể âm. Khi button cần touch target, padding thường là phần làm component dễ bấm chứ không chỉ tạo khoảng cách đẹp.

Một button:

```html
<button class="min-h-11 rounded-lg px-4 py-2">
```

`min-h-11` đảm bảo chiều cao tối thiểu, còn `px/py` tạo internal space.

---

## 28. `gap-*` nên được ưu tiên cho Flex/Grid spacing

Ví dụ:

```html
<div class="flex flex-col gap-4">
```

`gap-4` map tới CSS `gap`, nghĩa là spacing thuộc **container layout**, không phải margin của từng child.

So với:

```html
<div>
  <div class="mb-4">...</div>
  <div class="mb-4">...</div>
</div>
```

`gap` dễ maintain hơn vì:
- không cần `last:mb-0`,
- spacing responsibility thuộc parent,
- hoạt động tốt với wrapping Flex/Grid.

Tailwind vẫn có `space-y-*` và `space-x-*`, sử dụng selector/margin để tạo spacing giữa siblings. Chúng hữu ích trong một số normal-flow cases, nhưng với Flex/Grid mới, `gap` thường là lựa chọn đầu tiên.

---

## 29. `divide-*` khác `gap-*`

```html
<ul class="divide-y divide-gray-200">
  ...
</ul>
```

`divide-y` tạo border giữa children. Nó không tạo khoảng trống như gap.

Bạn có thể hình dung:

```text
gap
→ empty space between items

divide
→ visual separator between items
```

Một list có thể dùng cả hai nếu design cần, nhưng thường `divide` đã đóng vai trò divider.

---

# PHẦN III — FLEXBOX TRONG TAILWIND

## 30. Flexbox: phải hiểu container và item

Khi viết:

```html
<div class="flex">
```

element này trở thành **flex container**, và các child trực tiếp trở thành **flex items**.

Flexbox có hai trục:
- main axis,
- cross axis.

`flex-row` đặt main axis theo row. `flex-col` đặt main axis theo column.

```html
<div class="flex flex-row">
```

children xếp theo hàng.

```html
<div class="flex flex-col">
```

children xếp theo cột.

Điều này rất quan trọng vì `justify-*` hoạt động theo main axis, còn `items-*` hoạt động theo cross axis. Nếu bạn đổi row thành column, ý nghĩa trực quan của justify/items cũng đổi.

---

## 31. `justify-*`

Các utility chính:

```text
justify-start
justify-center
justify-end
justify-between
justify-around
justify-evenly
```

Với `flex-row`, `justify-center` thường center theo ngang. Với `flex-col`, nó center theo dọc vì main axis đã đổi.

Ví dụ center hai chiều:

```html
<div class="flex items-center justify-center">
```

Nhưng nếu chỉ cần center content đơn giản, Grid thường ngắn hơn:

```html
<div class="grid place-items-center">
```

---

## 32. `items-*` và baseline

`items-center` rất phổ biến:

```html
<div class="flex items-center gap-2">
  <svg>...</svg>
  <span>Label</span>
</div>
```

Nó align item theo cross-axis center.

Nhưng text-heavy UI đôi khi phù hợp với:

```text
items-baseline
```

Baseline alignment căn dựa trên typography baseline chứ không phải geometric box center. Ví dụ hai text có font-size khác nhau có thể trông tự nhiên hơn với baseline.

---

## 33. `flex-wrap`

Mặc định Flexbox thường nowrap. Tailwind:

```text
flex-nowrap
flex-wrap
flex-wrap-reverse
```

Tags/chips:

```html
<div class="flex flex-wrap gap-2">
  ...
</div>
```

Nếu không wrap, content có thể overflow hoặc items shrink mạnh.

---

## 34. `flex-1` không giống `grow`

`grow` chỉ thay đổi `flex-grow`.

```text
grow
→ flex-grow:1
```

Trong khi `flex-1` là flex shorthand và thay đổi nhiều thành phần flex sizing, về khái niệm giúp item chia available space với basis kiểu zero-ish.

Ví dụ:

```html
<div class="flex">
  <aside class="w-64 shrink-0">...</aside>
  <main class="min-w-0 flex-1">...</main>
</div>
```

`aside` giữ width, `main` lấy phần còn lại.

Nếu bạn chỉ viết `grow`, basis vẫn có thể khác và behavior không luôn giống `flex-1`.

---

## 35. `shrink` và `shrink-0`

Mặc định flex item có thể shrink.

Avatar:

```html
<img class="size-12 shrink-0">
```

Nếu thiếu `shrink-0`, trong row quá chật avatar có thể bị co nhỏ hơn expected.

`shrink-0` đặc biệt phù hợp cho:
- icon,
- avatar,
- fixed sidebar,
- action button
mà bạn không muốn bị co để nhường chỗ cho text.

Sau đó text container thường dùng:

```text
min-w-0 flex-1
```

Đây là pair rất thực tế.

---

## 36. `basis-*`

`flex-basis` là kích thước khởi điểm theo main axis trước khi grow/shrink phân phối free space.

Tailwind:

```text
basis-64
basis-1/2
basis-auto
basis-full
```

Nếu bạn muốn sidebar “ban đầu khoảng 16rem nhưng có flex logic”, `basis-64` có thể thích hợp hơn `w-64` trong một số flex architecture.

Senior nên hiểu width và flex-basis có thể cùng tham gia sizing; không thêm cả hai nếu không biết cái nào đang quyết định.

---

## 37. `self-*`

Container đặt:

```text
items-center
```

nhưng một item có thể override:

```html
<div class="self-start">
```

`self-*` map tới `align-self`.

Use khi một child thật sự có cross-axis alignment khác phần còn lại, không dùng để vá alignment ngẫu nhiên.

---

## 38. Flex pattern: Media Object

```html
<div class="flex gap-4">
  <img
    class="
      size-12
      shrink-0
      rounded-full
      object-cover
    "
  >

  <div class="min-w-0 flex-1">
    <h3 class="truncate font-semibold">
      User name
    </h3>

    <p class="text-sm text-gray-600">
      Description
    </p>
  </div>
</div>
```

Đây là pattern avatar/media + content kinh điển. `shrink-0` bảo vệ media, `min-w-0 flex-1` làm body linh hoạt.

---

# PHẦN IV — CSS GRID TRONG TAILWIND

## 39. Grid khác Flexbox ở đâu?

Flexbox mạnh khi bạn nghĩ theo một trục chính: row hoặc column. Grid mạnh khi bạn cần kiểm soát hàng và cột như một hệ thống.

Bật Grid:

```html
<div class="grid">
```

Sau đó:

```text
grid-cols-1
grid-cols-2
grid-cols-3
...
grid-cols-12
```

định nghĩa số cột bằng equal fractional tracks.

Ví dụ card layout:

```html
<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
```

Base một cột, md hai cột, lg ba cột.

---

## 40. `grid-cols-*` và `minmax(0,1fr)`

Tailwind equal grid column utilities thường dùng track kiểu `minmax(0, 1fr)` thay vì plain `1fr`.

Điều này quan trọng vì Grid item có intrinsic minimum size. `minmax(0,1fr)` cho track permission co xuống 0 minimum, giúp giảm overflow do content dài.

Đây là tư duy tương tự `min-w-0` trong Flexbox.

---

## 41. Arbitrary grid template

Dashboard:

```html
<div
  class="
    grid
    grid-cols-[16rem_minmax(0,1fr)]
    gap-6
  "
>
  <aside>...</aside>
  <main class="min-w-0">...</main>
</div>
```

Tailwind `_` trong arbitrary value trở thành whitespace, nên CSS tương đương:

```css
grid-template-columns:
  16rem minmax(0, 1fr);
```

Arbitrary grid template là một trong những arbitrary value use cases tốt nhất vì layout template thường mang tính structure hơn design-token scale.

---

## 42. `col-span-*`, `col-start-*`, `col-end-*`

Nếu grid có 12 cột:

```html
<div class="grid grid-cols-12">
  <aside class="col-span-3">
  <main class="col-span-9">
</div>
```

`col-span-3` nói item span ba tracks. Bạn cũng có thể đặt line trực tiếp:

```text
col-start-2
col-end-6
```

`col-span-full` thường span từ first tới last explicit grid line.

---

## 43. Grid rows và row placement

Tương tự columns:

```text
grid-rows-3
row-span-2
row-start-1
row-end-3
```

Use khi layout thật sự cần row tracks rõ ràng. Nếu content height tự nhiên, không nên ép rows chỉ vì có utility.

---

## 44. Auto-placement và `grid-flow-dense`

Tailwind có:

```text
grid-flow-row
grid-flow-col
grid-flow-dense
```

`dense` cho browser backfill holes trong grid. Nó có thể làm **visual order khác DOM order**.

Vì screen reader/focus navigation thường dựa trên DOM order, hãy cẩn thận dùng dense cho interactive content. Decorative gallery có thể ổn; form hoặc navigation có thể gây confusion.

---

## 45. Subgrid

```html
<div class="grid-cols-subgrid">
```

map tới:

```css
grid-template-columns: subgrid;
```

Subgrid cho child grid reuse tracks của parent thay vì tự tạo một hệ cột độc lập.

Use khi nhiều cards cần:
- title,
- body,
- action
align theo shared tracks.

---

## 46. Intrinsic auto grid không cần breakpoint

Một advanced pattern:

```html
<div
  class="
    grid
    grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]
    gap-6
  "
>
```

Ý nghĩa CSS: browser tự fit nhiều cột nhất có thể, mỗi cột tối thiểu khoảng 18rem nhưng không rộng hơn container ở mobile.

Điểm quan trọng: responsive không nhất thiết phải luôn `sm:`, `md:`, `lg:`. CSS intrinsic layout đôi khi responsive tự nhiên hơn breakpoint.

---

# PHẦN V — TYPOGRAPHY

## 47. Font family

Tailwind default families:

```text
font-sans
font-serif
font-mono
```

Chúng lấy value từ theme variables như `--font-sans`.

Custom:

```css
@theme {
  --font-brand:
    "Pretendard",
    "Noto Sans KR",
    sans-serif;
}
```

Use:

```html
<body class="font-brand">
```

Đừng chỉ nghĩ font family là tên font. Fallback chain rất quan trọng khi webfont chưa load hoặc glyph ngôn ngữ không có trong font đầu tiên.

---

## 48. Font size

Các utility:

```text
text-xs
text-sm
text-base
text-lg
text-xl
text-2xl
...
text-9xl
```

lấy từ theme type scale.

Arbitrary:

```text
text-[17px]
```

nhưng nếu 17px là body standard của product, hãy thêm token thay vì arbitrary ở mọi nơi.

Tailwind hỗ trợ compact syntax cho line-height:

```text
text-lg/7
```

nghĩa là font-size `text-lg` với leading value tương ứng `7`.

---

## 49. Font weight

```text
font-thin
font-light
font-normal
font-medium
font-semibold
font-bold
font-extrabold
font-black
```

Arbitrary:

```text
font-[650]
```

rất hữu ích với variable fonts hỗ trợ intermediate weights.

Không phải font nào cũng có thực glyph ở mọi weight. Browser có thể synthesize weight nếu file/font không support, nên design system cần load font variants đúng.

---

## 50. Line height

```text
leading-none
leading-tight
leading-snug
leading-normal
leading-relaxed
leading-loose
leading-6
leading-[1.65]
```

Line-height ảnh hưởng khoảng cách line box, không phải margin giữa paragraphs.

Heading thường cần tighter leading; body text thường cần rộng hơn.

Ví dụ:

```html
<h1 class="text-4xl font-bold leading-tight">
```

và:

```html
<p class="text-base leading-relaxed">
```

---

## 51. Letter spacing

```text
tracking-tighter
tracking-tight
tracking-normal
tracking-wide
tracking-wider
tracking-widest
```

Large display heading đôi khi đẹp hơn với tracking hơi âm, uppercase label đôi khi cần tracking dương.

Đừng áp `tracking-wide` global chỉ vì “trông thoáng”; Korean, English và font khác nhau có visual density khác nhau.

---

## 52. Text alignment và logical alignment

```text
text-left
text-center
text-right
text-justify
text-start
text-end
```

`text-start`/`text-end` phù hợp international UI hơn left/right khi alignment mang ý nghĩa theo reading direction.

---

## 53. White-space và text wrapping

Utilities quan trọng:

```text
whitespace-normal
whitespace-nowrap
whitespace-pre
whitespace-pre-line
whitespace-pre-wrap
```

`whitespace-nowrap` thường đi với single-line control/ellipsis.

`whitespace-pre-wrap` phù hợp user-generated text cần giữ newline/space nhưng vẫn wrap.

---

## 54. `truncate`: hiểu đầy đủ ba điều kiện

Tailwind `truncate` là bundle gần:

```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;
```

Nhưng nó chỉ hoạt động khi element có width constraint thực tế. Trong flex layout, bạn thường còn cần `min-w-0`.

Pattern:

```html
<div class="min-w-0 flex-1">
  <p class="truncate">
    ...
  </p>
</div>
```

Nếu text vẫn không ellipsis, kiểm tra sizing context thay vì thêm nhiều `overflow-hidden`.

---

## 55. Multi-line clamp

```html
<p class="line-clamp-3">
  ...
</p>
```

giới hạn nội dung theo số dòng.

Dùng tốt cho:
- card preview,
- search result summary,
- feed snippet.

Không dùng để giấu phần nội dung user bắt buộc phải đọc mà không có “Show more”.

---

## 56. Word breaking và Korean/CJK

Tailwind có các utilities liên quan:

```text
break-normal
break-words
break-all
break-keep
```

`break-keep` map tới behavior `word-break: keep-all` và thường hữu ích cho Korean/CJK khi bạn muốn tránh break giữa characters như `break-all`.

Ví dụ:

```html
<p class="break-keep text-pretty">
  한국어로 긴 문장을 표시합니다...
</p>
```

Nhưng text rất dài không có space như URL vẫn cần overflow strategy. Hãy test content thật thay vì áp một rule global cho mọi ngôn ngữ.

---

## 57. `text-balance` và `text-pretty`

`text-balance` map tới modern `text-wrap: balance`, hữu ích cho headings ngắn nhiều dòng vì browser cố cân độ dài các dòng.

```html
<h1 class="text-balance text-5xl font-bold">
```

`text-pretty` hướng tới line breaking đẹp hơn, thường phù hợp paragraph.

Đây là progressive enhancement; browser support target vẫn cần được xem xét nếu product hỗ trợ browser cũ.

---

## 58. Text decoration

Tailwind cung cấp utilities cho:
- underline,
- overline,
- line-through,
- decoration color,
- thickness,
- underline offset,
- decoration style.

Ví dụ link:

```html
<a
  class="
    underline
    decoration-blue-400
    decoration-2
    underline-offset-4
    hover:decoration-blue-600
  "
>
```

Text decoration tốt cho link accessibility hơn việc chỉ đổi màu khi link cần nhận biết rõ.

---

## 59. Text transform

```text
uppercase
lowercase
capitalize
normal-case
```

đây là visual transform. Source text/accessible name vẫn có semantics riêng.

Nếu acronym cần uppercase vì nội dung thật sự là acronym, tốt hơn source cũng đúng thay vì dựa hoàn toàn vào CSS transform.

---

## 60. OpenType numeric features

```text
tabular-nums
lining-nums
oldstyle-nums
slashed-zero
```

`tabular-nums` cực hữu ích cho:
- financial dashboard,
- table,
- countdown,
- metrics
vì mỗi chữ số có cùng advance width, giúp số không “nhảy” khi thay đổi.

V4.2+ có `font-features-*` cho low-level `font-feature-settings`, nhưng hãy ưu tiên high-level utility nếu có semantic equivalent.

---

# PHẦN VI — COLOR, BACKGROUND, BORDER, SHADOW

## 61. Color system và palette

Tailwind v4 dùng modern color system với palette rộng. Current release có các neutral families như:

```text
slate
gray
zinc
neutral
stone
mauve
olive
mist
taupe
```

và chromatic families như red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose.

Scale thường chạy từ `50` sáng tới `950` tối.

Ví dụ:

```text
bg-blue-600
text-gray-900
border-gray-200
```

Nhưng numeric shade không có semantic meaning business. Một design system lớn nên bổ sung semantic tokens như action, surface, danger thay vì để mọi component tự chọn palette.

---

## 62. Alpha modifier `/`

```html
<div class="bg-blue-600/50">
```

nghĩa là background blue-600 với alpha 50%.

Tương tự:

```text
text-black/70
border-gray-900/10
shadow-black/20
```

Arbitrary:

```text
bg-pink-500/[71.37%]
```

Alpha modifier giúp tránh cần tạo riêng hàng loạt opacity color token.

---

## 63. Background

Ngoài color:

```text
bg-cover
bg-contain
bg-center
bg-top
bg-no-repeat
bg-repeat
bg-fixed
```

map tới background-size, background-position, background-repeat và attachment.

Ảnh hero:

```html
<section
  class="
    bg-cover
    bg-center
    bg-no-repeat
  "
>
```

Nếu background image URL là one-off:

```html
<div class="bg-[url('/images/hero.webp')]">
```

Nhưng với dynamic URL từ API, inline style/CSS variable có thể thích hợp hơn source-generated arbitrary class.

---

## 64. Gradient

Tailwind hỗ trợ gradient utilities và gradient color stops. Tư duy quan trọng không phải thuộc mọi tên class mà hiểu:
- gradient là `background-image`,
- direction/shape là function argument,
- from/via/to xác định color stops.

Một gradient UI nên dùng token/semantic colors nếu là part của brand system, không hard-code arbitrary color khắp component.

---

## 65. Border width, style và color

Ví dụ:

```html
<div class="border border-gray-200">
```

`border` đặt default border width; `border-gray-200` đặt color.

Có directional utilities:

```text
border-t
border-b
border-x
border-y
```

và logical v4 utilities như block-start/end trong relevant naming families.

Styles:

```text
border-solid
border-dashed
border-dotted
border-double
border-none
```

Divider nên đặt ở parent với `divide-*` nếu mục tiêu là separator giữa children, thay vì mỗi child tự thêm border rồi xử lý `last:`.

---

## 66. Border radius

```text
rounded-none
rounded-sm
rounded
rounded-md
rounded-lg
rounded-xl
rounded-2xl
rounded-3xl
rounded-full
```

`rounded-full` tạo cực lớn radius, thường dùng pill hoặc circle nếu width/height bằng nhau.

Có directional/logical corner utilities. Khi app cần RTL, tránh chỉ suy nghĩ `rounded-l-*`/`rounded-r-*` nếu ý nghĩa là start/end.

---

## 67. Outline và focus

Accessible focus pattern:

```html
<button
  class="
    focus-visible:outline-2
    focus-visible:outline-offset-2
    focus-visible:outline-blue-600
  "
>
```

`focus-visible` khác `focus`: browser cố chỉ hiển thị focus treatment khi input modality phù hợp, ví dụ keyboard navigation, thay vì mọi mouse click.

Không viết:

```text
outline-none
```

mà không có replacement focus indicator. Làm mất focus visible là accessibility regression.

---

## 68. Ring utilities

Tailwind có `ring-*`, nhưng CSS không có property tên `ring`. Tailwind implement ring bằng shadow/custom properties.

Ví dụ:

```html
<div class="ring-1 ring-black/10">
```

Card subtle border-like effect rất đẹp bằng ring.

Focus có thể dùng ring:

```html
<input class="focus:ring-2 focus:ring-blue-500/30">
```

Nhưng outline có lợi thế semantic/direct và không bị box-shadow composition ảnh hưởng giống ring. Senior chọn theo design/interaction context.

---

## 69. Box shadow

```text
shadow-xs
shadow-sm
shadow-md
shadow-lg
shadow-xl
shadow-2xl
shadow-none
```

Shadow mô tả elevation hoặc visual separation. Đừng dùng càng lớn càng “premium”. Một design system nên có elevation scale rõ.

Tint:

```text
shadow-black/10
shadow-blue-500/20
```

---

## 70. Text shadow

Current Tailwind v4 có text-shadow utility family. Nó map trực tiếp tới CSS `text-shadow`.

Use:
- decorative display text,
- text trên ảnh khó đọc.

Không dùng heavy text shadow cho body text vì giảm readability.

---

## 71. Opacity

```text
opacity-0
opacity-50
opacity-100
```

`opacity` áp cho toàn rendered subtree, không chỉ background.

Nếu bạn muốn background trong suốt mà text vẫn opaque:

```text
bg-white/50
```

tốt hơn:

```text
opacity-50
```

trên container.

---

## 72. Blend và isolation

Tailwind có `mix-blend-*`, `bg-blend-*`, `isolate`.

`mix-blend-mode` cho element blend với backdrop. `isolation:isolate` tạo isolation context để giới hạn blending/stacking behavior.

Đây là advanced visual tool, không phải normal layout mechanism.

---

## 73. Filters

Common:

```text
blur-*
brightness-*
contrast-*
grayscale
hue-rotate-*
invert
saturate-*
sepia
drop-shadow-*
```

`drop-shadow` là filter dựa trên alpha shape của rendered element, khác `box-shadow` luôn dựa box.

Performance của filter lớn, đặc biệt blur trên vùng rộng/animate liên tục, có thể đáng kể. Test bằng DevTools thay vì assume.

---

## 74. Backdrop filter

Glass UI:

```html
<div
  class="
    bg-white/70
    backdrop-blur-xl
    ring-1
    ring-black/5
  "
>
```

`backdrop-blur-*` blur nội dung **phía sau** element, không phải element itself.

Backdrop filter có thể tốn render cost, đặc biệt trên vùng full-screen hoặc mobile. Use có chọn lọc.

---

## 75. Mask utilities

Mask kiểm soát transparency bằng image/gradient/luminance. Nó khác `clip-path`: clip thường quyết định vùng visible cứng hơn, mask cho phép alpha gradient.

Tailwind current docs có utility families cho:
- mask image,
- size,
- position,
- repeat,
- origin,
- clip,
- mode,
- composite,
- type.

Nếu một option hiếm không có named utility bạn nhớ, arbitrary property:

```html
<div class="[mask-type:luminance]">
```

là cách hợp lệ.

---

# PHẦN VII — IMAGES, SVG, TABLES VÀ CONTENT

## 76. `aspect-*`

```text
aspect-square
aspect-video
aspect-3/2
aspect-[4/3]
aspect-auto
```

map tới `aspect-ratio`.

Avatar:

```html
<img
  class="
    aspect-square
    w-16
    rounded-full
    object-cover
  "
>
```

Aspect ratio reserve shape của box; `object-cover` quyết định resource bên trong fit/crop như thế nào.

---

## 77. `object-cover` và `object-contain`

Ảnh 4:3 đặt trong box 1:1.

`object-cover` phóng resource đủ để phủ toàn box và crop phần dư.

`object-contain` thu/phóng để toàn resource nhìn thấy, có thể để khoảng trống.

```html
<img class="size-20 object-cover">
```

rất phù hợp thumbnail.

Focal point:

```text
object-top
object-center
object-[50%_20%]
```

giúp kiểm soát vùng crop.

---

## 78. `size-*`

```html
<div class="size-10">
```

là shorthand width + height cùng value.

Use cực nhiều cho:
- avatar,
- icon button,
- square placeholder.

Nó không thay `aspect-square` hoàn toàn: `size-*` đặt cả hai dimension; `aspect-square` chỉ giữ ratio khi một dimension được quyết định bởi context.

---

## 79. SVG

Một icon inline SVG thường:

```html
<svg
  class="size-5 text-blue-600"
  fill="currentColor"
>
```

`currentColor` làm fill follow CSS `color`.

Tailwind cũng có:

```text
fill-current
fill-blue-600
fill-none
stroke-current
stroke-blue-600
stroke-1
stroke-2
```

Inline SVG style được bởi CSS. SVG dùng qua `<img src="icon.svg">` là replaced resource và internal SVG không được stylesheet document target giống inline SVG.

---

## 80. Tables

Wrapper responsive:

```html
<div class="overflow-x-auto">
  <table class="min-w-full table-auto">
```

`table-auto` dùng content-sensitive table layout. `table-fixed` cho column sizing predictable hơn khi table width đã constrained.

`border-collapse` merge adjacent borders; `border-separate` giữ separate border model và có thể dùng `border-spacing-*`.

Data table lớn nên ưu tiên semantic `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` thay vì recreate bằng div chỉ để styling dễ.

---

## 81. Multi-column và fragmentation

Tailwind có `columns-*` cho CSS multi-column layout. Đây không phải Grid columns. Browser flow text/content từ cột này sang cột tiếp theo.

Fragmentation utilities như:

```text
break-inside-avoid
break-before-page
break-after-page
```

hữu ích cho print/editorial layout.

---

# PHẦN VIII — TRANSFORM, TRANSITION, ANIMATION

## 82. Translate

```text
translate-x-4
translate-y-2
-translate-x-1/2
-translate-y-1/2
```

Classic absolute center:

```html
<div
  class="
    absolute
    left-1/2
    top-1/2
    -translate-x-1/2
    -translate-y-1/2
  "
>
```

Ở đây `left-1/2 top-1/2` đặt top-left point vào center parent, còn negative translate 50% own size kéo element về center thật.

Nếu chỉ cần center normal layout, Grid:

```text
grid place-items-center
```

thường đơn giản hơn.

---

## 83. Scale, rotate, skew

```text
scale-95
scale-100
scale-105
rotate-45
-rotate-6
skew-x-6
```

Transform không giống layout sizing. Scale làm rendered element to/nhỏ nhưng normal layout space ban đầu thường không được reflow giống width/height.

Hover microinteraction:

```html
<button
  class="
    transition-transform
    hover:scale-105
  "
>
```

Nên respect reduced motion nếu movement đáng kể.

---

## 84. Transform origin, perspective và 3D

Utilities:

```text
origin-center
origin-top-left
perspective-*
perspective-origin-*
transform-3d
transform-flat
backface-hidden
```

3D transform nên dùng cho purposeful interaction như flip card, carousel hoặc visual editor. Đây không phải thứ cần rải khắp normal form/dashboard.

---

## 85. `zoom-*` trong v4.3

Tailwind v4.3 có:

```text
zoom-75
zoom-100
zoom-125
zoom-[1.1]
zoom-(--preview-zoom)
```

map tới CSS `zoom`.

`zoom` khác `transform: scale()` vì zoom ảnh hưởng layout metrics theo cách khác. Một document preview có thể hợp lý:

```html
<div class="zoom-(--preview-scale)">
```

Nhưng responsive app không nên dùng zoom để “thu nhỏ desktop UI cho mobile”.

CSS `zoom` cũng không phải browser user zoom. Không bao giờ cố chống lại user zoom vì accessibility.

---

## 86. Transition property

Tailwind có:

```text
transition
transition-all
transition-colors
transition-opacity
transition-shadow
transition-transform
transition-none
```

`transition-all` tiện nhưng quá rộng. Nếu width, top, filter hoặc expensive property vô tình thay đổi, tất cả đều animate.

Senior thường chọn target rõ:

```html
<button
  class="
    transition-colors
    duration-150
    ease-out
  "
>
```

---

## 87. Duration, delay và easing

```text
duration-75
duration-150
duration-300
delay-75
ease-linear
ease-in
ease-out
ease-in-out
```

Microinteraction UI thường ở khoảng nhanh. Modal/page transition có thể dài hơn.

Không có “thời lượng chuẩn Tailwind” cho mọi UX. Design motion system nên consistent.

---

## 88. Built-in animations

Common:

```text
animate-spin
animate-ping
animate-pulse
animate-bounce
animate-none
```

Loading spinner:

```html
<svg class="animate-spin">
```

Skeleton:

```html
<div class="animate-pulse">
  ...
</div>
```

Không phải animation nào cũng phải loop. Animation nên communicate state, không chỉ trang trí.

---

## 89. Custom animation bằng `@theme`

```css
@theme {
  --animate-fade-in:
    fade-in 180ms ease-out;

  @keyframes fade-in {
    from {
      opacity: 0;
      transform: translateY(.25rem);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
}
```

Use:

```html
<div class="animate-fade-in">
```

Theme token cho animation biến animation name/value thành reusable utility API.

---

## 90. Reduced motion

```html
<div
  class="
    transition-transform
    hover:scale-105
    motion-reduce:transition-none
    motion-reduce:hover:scale-100
  "
>
```

`motion-reduce:` map tới media query `prefers-reduced-motion: reduce`.

Nếu motion chỉ là decoration, giảm/tắt nó cho người dùng đã yêu cầu reduced motion.

---

# PHẦN IX — FORMS VÀ INTERACTION

## 91. Cursor không tạo semantics

```text
cursor-pointer
cursor-default
cursor-not-allowed
```

chỉ đổi mouse cursor.

Sai:

```html
<div class="cursor-pointer">
  Submit
</div>
```

nếu nó thật sự là button.

Đúng:

```html
<button class="cursor-pointer">
  Submit
</button>
```

Semantic HTML mang keyboard behavior, accessibility role và form semantics mà class không tạo được.

---

## 92. Pointer events

```text
pointer-events-none
pointer-events-auto
```

`pointer-events-none` khiến element không nhận pointer targeting.

Nó không phải semantic disabled. Một button disabled nên có:

```html
<button
  disabled
  class="
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

`disabled` attribute quyết định behavior; Tailwind chỉ style state đó.

---

## 93. User select

```text
select-none
select-text
select-all
select-auto
```

`select-none` hợp lý cho drag handle/icon control. Không disable selection toàn page vì user có thể cần copy text.

---

## 94. Appearance và native controls

```text
appearance-none
appearance-auto
```

`appearance-none` loại bỏ native skin của form control. Khi làm vậy, bạn nhận trách nhiệm style:
- focus,
- checked,
- disabled,
- forced colors,
- hover,
- high-contrast.

Đừng custom native controls sâu chỉ vì có thể.

---

## 95. `accent-*`

```html
<input
  type="checkbox"
  class="accent-blue-600"
>
```

`accent-color` là cách rất hiệu quả để theme checkbox/radio/range native mà vẫn giữ native behavior.

Nhiều case không cần recreate checkbox bằng div/SVG.

---

## 96. Field sizing

Modern Tailwind có utilities liên quan `field-sizing`.

`field-sizing: content` cho phép input/textarea trong browser support phù hợp size theo content.

Textarea:

```html
<textarea
  class="
    field-sizing-content
    min-h-24
    max-h-80
  "
></textarea>
```

Bạn vẫn nên đặt min/max constraint để content không làm layout phát triển vô hạn.

---

## 97. Resize

```text
resize
resize-x
resize-y
resize-none
```

Textarea thường nên cho phép ít nhất vertical resize:

```html
<textarea class="resize-y">
```

`resize-none` có thể làm UX kém nếu user cần mở rộng vùng nhập liệu.

---

# PHẦN X — SCROLL, TOUCH VÀ VIEWPORT INTERACTION

## 98. Smooth scroll

```text
scroll-smooth
scroll-auto
```

`scroll-smooth` đặt CSS `scroll-behavior: smooth`.

Nếu animation gây vấn đề motion preference, bạn có thể combine:

```text
motion-reduce:scroll-auto
```

---

## 99. Scroll snap

Carousel:

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

`scroll-snap-type` đặt trên scroll container; `snap-start`, `snap-center`, `snap-end` đặt trên items.

`mandatory` mạnh hơn `proximity`. Use carefully để không làm scrolling user khó chịu.

---

## 100. Overscroll

Nested modal scroller:

```html
<div
  class="
    max-h-[70dvh]
    overflow-auto
    overscroll-contain
  "
>
```

`overscroll-contain` giúp hạn chế scroll chaining ra page khi scroller bên trong đến boundary.

---

## 101. Scroll margin và sticky headers

Anchor target:

```html
<section
  id="billing"
  class="scroll-mt-20"
>
```

Khi browser scroll tới `#billing`, `scroll-margin-top` tạo khoảng tránh sticky header che mất heading.

Đây thường sạch hơn thêm fake padding/margin vào mọi section.

---

## 102. Touch action

```text
touch-auto
touch-none
touch-pan-x
touch-pan-y
touch-pinch-zoom
touch-manipulation
```

Custom carousel drag ngang trong page scroll dọc có thể dùng `touch-pan-y` để browser biết vertical scroll vẫn được phép.

`touch-none` rất mạnh và có thể phá native scroll/zoom accessibility. Chỉ dùng nếu component thực sự implement gesture thay thế đúng.

---

## 103. Scrollbar utilities v4.3

Tailwind v4.3 thêm first-party scrollbar utilities.

Width:

```text
scrollbar-auto
scrollbar-thin
scrollbar-none
```

Color:

```text
scrollbar-thumb-slate-700
scrollbar-track-slate-100
```

Alpha modifier cũng có thể được dùng trong relevant color utilities.

Gutter:

```text
scrollbar-gutter-auto
scrollbar-gutter-stable
scrollbar-gutter-both
```

`stable` reserve space cho classic scrollbar để giảm layout shift khi scrollbar xuất hiện.

Scrollbar rendering vẫn phụ thuộc browser/OS. Tailwind không biến scrollbar thành pixel-identical cross-platform control.

---

# PHẦN XI — RESPONSIVE DESIGN

## 104. Mobile-first thật sự nghĩa là gì?

```html
<div
  class="
    grid
    grid-cols-1
    md:grid-cols-2
    xl:grid-cols-4
  "
>
```

Base style chạy ở mọi width trừ khi bị override.

`md:grid-cols-2` nghĩa:

```text
từ md trở lên
→ 2 columns
```

Nó không nghĩa “chỉ ở md”.

`xl:grid-cols-4` tiếp tục override từ xl trở lên.

Đây là mobile-first min-width model.

---

## 105. Breakpoint names không phải device names

Default Tailwind có:

```text
sm
md
lg
xl
2xl
```

Bạn không nên học chúng như:

```text
sm = phone
md = tablet
lg = laptop
```

Layout nên chuyển khi **content cần**, không phải khi gặp tên device.

Custom breakpoint:

```css
@theme {
  --breakpoint-content-wide: 72rem;
}
```

Nếu team muốn semantic breakpoint name, có thể dùng, nhưng đừng tạo `iphone-15:` hoặc `ipad-pro:` nếu product không thật sự phụ thuộc một device cụ thể.

---

## 106. Range responsive variants

```html
<div class="md:max-xl:grid">
```

nghĩa là rule active từ `md` đến dưới `xl`.

One-off:

```text
min-[520px]:
max-[760px]:
```

Arbitrary breakpoint hợp lý cho local exception, nhưng nếu cùng threshold lặp ở nhiều component, promote thành theme breakpoint hoặc container token.

---

# PHẦN XII — CONTAINER QUERIES

## 107. Vì sao container query quan trọng hơn thêm breakpoint

Một Card có thể được render:
- full-width main content,
- narrow sidebar,
- modal,
- dashboard grid.

Nếu Card chỉ nhìn viewport bằng `md:`, nó có thể nghĩ “desktop” dù chính Card chỉ rộng 300px.

Container query hỏi:

> container của component hiện rộng bao nhiêu?

Mark container:

```html
<div class="@container">
```

Child:

```html
<article
  class="
    flex
    flex-col
    @md:flex-row
  "
>
```

`@md:` ở đây không phải viewport `md:`. Nó là container query threshold.

---

## 108. Container query breakpoints

Tailwind có các container size variants như:

```text
@3xs
@2xs
@xs
@sm
@md
@lg
@xl
...
```

Current default container scale bắt đầu từ các size nhỏ như 16rem và tăng dần.

Bạn không cần thuộc từng số ngay. Điều quan trọng là hiểu namespace `--container-*` quyết định container query variants.

Custom:

```css
@theme {
  --container-card-wide: 36rem;
}
```

Sau đó API container có thể dùng token đó theo supported naming semantics.

---

## 109. Container max/range

Bạn có thể viết:

```text
@max-md:
@sm:@max-md:
@min-[475px]:
@max-[960px]:
```

Điều này cho component-local ranges.

Đừng lạm dụng range nếu layout có thể được giải bằng intrinsic Grid/Flex.

---

## 110. `@container-size` trong v4.3

Regular:

```text
@container
```

tạo inline-size container, chủ yếu query width/inline dimension.

V4.3:

```text
@container-size
```

tạo size container, cho phép dimension liên quan block-size/height.

Ví dụ:

```html
<div class="@container-size">
  <div class="h-[50cqb]">
```

`cqb` cần block size của query container.

Size containment có ảnh hưởng sizing mạnh hơn inline containment, nên đừng đổi tất cả container sang `@container-size` chỉ vì nó “mạnh hơn”.

---

# PHẦN XIII — STATE VARIANTS

## 111. Hover

```html
<button class="bg-blue-600 hover:bg-blue-700">
```

Tailwind generate hover selector cùng handling cho hover-capable environment.

Điều này quan trọng trên touch device vì “hover” không có cùng nghĩa như mouse desktop.

---

## 112. Focus và `focus-visible`

```text
focus:
focus-visible:
focus-within:
```

`focus:` style chính element khi focused.

`focus-visible:` style khi browser xác định cần visible focus indicator.

`focus-within:` style parent khi chính nó hoặc descendant focus.

Form group:

```html
<label
  class="
    rounded-lg
    focus-within:ring-2
    focus-within:ring-blue-500/20
  "
>
```

---

## 113. Active

```text
active:
```

map tới `:active`, thường là thời điểm pointer/button đang được activate.

Micro feedback:

```html
<button class="active:scale-[.98]">
```

Nếu motion không cần thiết, respect reduced motion.

---

## 114. Structural variants

Tailwind có variants như:

```text
first:
last:
only:
odd:
even:
empty:
first-of-type:
last-of-type:
```

List divider:

```html
<li class="border-b last:border-b-0">
```

Những selector này nên mô tả structure thật. Nếu state business là “selected row”, hãy dùng `data-selected`/ARIA chứ không dùng `nth-child` để giả state.

---

## 115. `nth-*`

Current Tailwind supports expressive nth variants.

```text
nth-3:
nth-last-2:
nth-of-type-4:
```

Arbitrary:

```text
nth-[2n+1_of_li]:
```

map tới CSS `:nth-child(...)` family.

Use cho zebra striping hoặc layout pattern dựa structural order.

---

## 116. Form state variants

Tailwind có nhiều state variants:

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

Ví dụ:

```html
<input
  class="
    border-gray-300
    user-invalid:border-red-500
    disabled:cursor-not-allowed
    disabled:bg-gray-100
    disabled:text-gray-500
  "
>
```

`user-invalid` thường tạo UX tốt hơn `invalid` trong form vì tránh hiển thị lỗi quá sớm trước khi user interaction, tùy browser semantics.

---

## 117. `group-*`: style child theo parent state

Parent:

```html
<a class="group">
```

Child:

```html
<span class="group-hover:text-blue-600">
```

Tailwind generate selector liên hệ child với `.group:hover`.

Nested components nên dùng named group:

```html
<div class="group/card">
  <button class="group-hover/card:opacity-100">
```

Nếu không name, một child sâu có thể vô tình react với wrong ancestor group.

---

## 118. `peer-*`: style sibling theo sibling state

```html
<input
  type="email"
  class="peer"
/>

<p
  class="
    invisible
    peer-invalid:visible
  "
>
  Invalid email
</p>
```

CSS sibling selector hoạt động từ element trước sang element sau, nên target phải xuất hiện sau peer trong DOM.

Nếu target cần style previous sibling, dùng parent `has-*` hoặc restructure DOM thay vì cố ép peer.

---

## 119. `has-*`: parent-aware styling

```html
<label class="has-checked:bg-blue-50">
  <input type="radio">
  ...
</label>
```

Maps conceptually tới:

```css
label:has(:checked)
```

`:has()` giúp style parent dựa trên child state mà không cần JS class toggle.

Use tốt cho:
- checked control,
- invalid child,
- optional slot existence,
- focus child.

Business state không tồn tại trong DOM vẫn cần application logic.

---

## 120. `in-*`

`in-*` cho phép respond tới ancestor state mà không mark explicit `.group`.

Điều này tiện trong shallow UI, nhưng càng nested càng khó biết ancestor nào kích hoạt.

Senior preference: nếu ownership quan trọng, named `group` rõ hơn implicit `in-*`.

---

## 121. Child variants `*:` và `**:`

```html
<ul class="*:rounded-md *:px-3">
```

`*:` target direct children.

`**:` target descendants sâu hơn.

Đây là convenience khi parent kiểm soát uniform child style. Nếu một child cần nhiều exception, class đặt trực tiếp trên child thường dễ reasoning hơn.

---

## 122. ARIA variants

```html
<button
  aria-pressed="true"
  class="
    aria-pressed:bg-blue-600
    aria-pressed:text-white
  "
>
```

ARIA state vừa có semantics accessibility vừa là selector hook.

Nhưng không được set ARIA sai chỉ để style. Ví dụ random `<div aria-selected="true">` không nằm trong widget semantics có thể misleading cho assistive technology.

---

## 123. Data variants

```html
<div
  data-state="open"
  class="
    opacity-0
    data-[state=open]:opacity-100
  "
>
```

Pattern senior:

```text
business/application state
→ data-* attribute

accessibility semantic state
→ aria-* attribute

Tailwind
→ presentation
```

JS không cần hard-code visual CSS; Tailwind/CSS không cần biết business logic.

---

# PHẦN XIV — DARK MODE VÀ USER PREFERENCES

## 124. Dark mode mặc định

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

By default, `dark:` có thể dựa trên system `prefers-color-scheme` theo Tailwind configuration/default strategy hiện hành.

---

## 125. Manual dark mode

Nếu app có theme switcher:

```css
@custom-variant dark
  (&:where(.dark, .dark *));
```

Sau đó root:

```html
<html class="dark">
```

activate `dark:*`.

Data attribute variant:

```css
@custom-variant dark
  (&:where(
    [data-theme=dark],
    [data-theme=dark] *
  ));
```

Root:

```html
<html data-theme="dark">
```

---

## 126. System / Light / Dark ba trạng thái

Một app thường có:
- light,
- dark,
- system.

Tailwind không quản lý storage hay app preference cho bạn. JS/server xác định root state. Tailwind chỉ style theo condition.

Architecture:

```text
user preference
→ storage/server
→ root class/data attribute
→ dark variant
→ generated CSS
```

Nếu root state set quá muộn sau first paint, bạn có thể thấy flash sai theme. Đó là theme initialization issue, không phải Tailwind utility issue.

---

## 127. `motion-reduce`, contrast, forced colors

Tailwind variants cho user/environment preferences như:

```text
motion-reduce:
motion-safe:
contrast-more:
contrast-less:
forced-colors:
print:
portrait:
landscape:
pointer-fine:
pointer-coarse:
```

Use những condition phản ánh capability/preference thật thay vì đoán loại device.

---

# PHẦN XV — `@theme` VÀ DESIGN TOKENS

## 128. `@theme` khác `:root` như thế nào?

Normal CSS:

```css
:root {
  --brand: #2563eb;
}
```

browser biết `--brand`, nhưng Tailwind không tự hiểu nó là color token để tạo `bg-brand`.

Tailwind:

```css
@theme {
  --color-brand: #2563eb;
}
```

`--color-*` thuộc color namespace, nên Tailwind vừa emit CSS variable vừa tạo relevant utility APIs.

Đây là lý do `@theme` không chỉ là “CSS variables syntax khác”.

---

## 129. Namespace là API

Một số namespace quan trọng:

```text
--color-*
--font-*
--text-*
--font-weight-*
--tracking-*
--leading-*
--spacing-*
--radius-*
--shadow-*
--blur-*
--ease-*
--animate-*
--breakpoint-*
--container-*
--tab-size-*
```

Bạn không cần nhớ mọi namespace ngay. Nhưng cần hiểu pattern: namespace quyết định utility family.

---

## 130. Primitive token và semantic token

Primitive:

```text
blue-600
gray-200
radius-lg
```

Semantic:

```text
action-primary
surface-default
text-muted
danger-bg
danger-fg
```

Primitive thuận tiện cho composition nhanh. Semantic thuận tiện cho rebrand/theme.

Một hệ thống lớn có thể dùng:

```css
@theme {
  --color-brand-500: ...;
  --color-brand-600: ...;
}
```

và thêm runtime semantic vars:

```css
:root {
  --button-primary-bg:
    var(--color-brand-600);
}
```

---

## 131. Theme token không nhất thiết nên dùng cho mọi property role

Nếu:

```css
@theme {
  --color-danger: red;
}
```

Tailwind có thể expose:
- `bg-danger`,
- `text-danger`,
- `border-danger`.

Nhưng design system có thể cần:
- danger background nhạt,
- danger text đậm,
- danger border trung gian.

Khi đó token nên chi tiết:

```text
danger-bg
danger-fg
danger-border
```

Senior token design quan tâm semantics, không chỉ màu.

---

## 132. Reset namespace cho strict design system

```css
@theme {
  --color-*: initial;

  --color-surface: ...;
  --color-text: ...;
  --color-action: ...;
  --color-danger: ...;
}
```

Điều này remove default palette API và chỉ giữ approved colors.

Lợi là dev không “chọn đại blue-500”. Hại là generic examples/library code dựa default palette có thể không work.

Strict theme phù hợp design system mature hơn beginner app.

---

# PHẦN XVI — CUSTOMIZATION API CỦA TAILWIND V4

## 133. `@utility`: đăng ký utility riêng

```css
@utility content-auto {
  content-visibility: auto;
}
```

Use:

```html
<div class="content-auto">
```

Vì đã đăng ký bằng `@utility`, bạn có thể dùng variants:

```text
lg:content-auto
```

Khác với:

```css
.content-auto {
  content-visibility:auto;
}
```

là một normal class, không nhất thiết tham gia Tailwind utility resolution giống nhau.

---

## 134. Khi nào nên tạo custom utility?

Custom utility phù hợp khi concern:
- atomic,
- reusable,
- project/core chưa có utility rõ,
- cần variants.

Ví dụ `content-visibility` primitive là utility tốt.

Một `super-dashboard-card` chứa 15 properties, hover, child selectors và state thì không còn là atomic utility; đó là component/custom CSS.

---

## 135. Functional `@utility`

V4 cho phép utility family:

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

Một definition có thể support:
- theme token,
- bare numeric value,
- arbitrary value.

`--value()` là **Tailwind build-time resolver**. Browser không biết function này.

---

## 136. `--default()` trong v4.3

```css
@utility tab-* {
  tab-size:
    --value(
      integer,
      --default(4)
    );
}
```

Now:

```text
tab
```

có default 4, còn:

```text
tab-2
```

resolve 2.

Use bare utility default khi ý nghĩa mặc định thật sự tự nhiên.

---

## 137. Modifier và `--modifier()`

Một candidate như:

```text
text-lg/7
```

có main value `lg` và modifier `7`.

Custom utility cũng có thể dùng modifier cho secondary dimension.

Đừng tạo API với slash modifier nếu relationship không intuitive, vì utility sẽ trở nên khó đoán.

---

## 138. `@custom-variant`

Nếu app có theme/state repeated:

```css
@custom-variant theme-midnight
  (&:where([data-theme="midnight"] *));
```

Use:

```html
<div class="theme-midnight:bg-black">
```

Bạn đã biến một selector phức tạp thành semantic variant.

---

## 139. `@variant`

Trong custom CSS:

```css
.button-shell {
  @variant dark {
    background: black;
  }
}
```

V4.3 support compound/stacked variant forms tốt hơn, ví dụ:

```css
@variant hover:focus {
  ...
}
```

và multiple:

```css
@variant hover, focus {
  ...
}
```

`@variant` hữu ích khi bạn đã chọn custom CSS nhưng vẫn muốn reuse Tailwind variant logic.

---

## 140. `@apply`

```css
.select2-dropdown {
  @apply rounded-lg bg-white shadow-lg;
}
```

`@apply` inline Tailwind utilities vào custom CSS selector.

Use case tốt:
- third-party markup,
- CMS/editor output,
- legacy selector,
- component style context không thể đặt utility trực tiếp.

Use case xấu là tạo lại toàn bộ semantic CSS architecture cũ:

```css
.btn-primary {
  @apply ...;
}
```

cho mọi button trong React app, rồi markup lại quay về `.btn-primary`. Nếu component abstraction đã tồn tại, hãy compose utilities trong component.

---

## 141. `@reference`

Trong Vue/Svelte/CSS Modules, một style block riêng có thể không nhìn thấy custom theme/utilities của main stylesheet.

```css
@reference "../../app.css";

.title {
  @apply text-2xl font-bold;
}
```

`@reference` cho Tailwind processing context biết definitions mà không duplicate CSS output.

Nếu chỉ cần một token:

```css
.title {
  color: var(--color-red-500);
}
```

thường đơn giản hơn.

---

# PHẦN XVII — SOURCE DETECTION

## 142. Automatic source detection

Tailwind v4 scan project nhưng bỏ qua nhiều loại source không cần thiết như `node_modules`, binary, CSS file, ignored files.

Vì vậy dependency chứa Tailwind classes có thể cần explicit source registration.

---

## 143. `@source`

```css
@source "../node_modules/@acme/ui-lib";
```

nói Tailwind scan package đó.

Monorepo:

```css
@source "../../packages/ui/src";
```

---

## 144. `source()` base path

```css
@import "tailwindcss"
  source("../src");
```

Dùng khi current working directory của build khác application source root.

---

## 145. Ignore path

```css
@source not "../src/legacy";
```

Nếu folder lớn không có Tailwind candidates, loại khỏi scan có thể giúp source ownership rõ và giảm work.

---

## 146. `source(none)`

```css
@import "tailwindcss"
  source(none);

@source "../admin";
@source "../shared";
```

Tắt automatic detection để bundle chỉ scan explicit roots.

Rất hữu ích khi project có:
- admin.css,
- storefront.css,
- nhiều microfrontend.

---

## 147. Safelist bằng `@source inline()`

Khi cần force generate class không nằm literal trong normal source, v4 dùng source inline API.

Ví dụ conceptual:

```css
@source inline("underline");
```

Bạn có thể safelist variants/ranges bằng brace expansion theo docs.

Nhưng broad safelist làm Tailwind mất lợi ích usage-driven CSS generation.

---

# PHẦN XVIII — COMPONENT ARCHITECTURE

## 148. Khi nào class dài là bình thường?

Một button:

```html
<button
  class="
    inline-flex
    items-center
    justify-center
    gap-2
    rounded-lg
    bg-blue-600
    px-4
    py-2
    text-sm
    font-semibold
    text-white
    transition-colors
    hover:bg-blue-700
    focus-visible:outline-2
    focus-visible:outline-offset-2
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

không tự động là “bad” chỉ vì nhiều class. Bạn đang nhìn toàn bộ visual behavior ngay tại component.

Nó trở thành vấn đề khi same structure + same style + same states được copy vào nhiều nơi.

---

## 149. Extract component chứ không nhất thiết extract CSS class

React:

```jsx
function Button({
  variant = "primary",
  size = "md",
  children,
}) {
  const variants = {
    primary:
      "bg-blue-600 text-white hover:bg-blue-700",
    danger:
      "bg-red-600 text-white hover:bg-red-700",
  };

  const sizes = {
    sm:
      "min-h-9 px-3 text-sm",
    md:
      "min-h-10 px-4 text-sm",
    lg:
      "min-h-12 px-5 text-base",
  };

  return (
    <button
      className={`
        inline-flex
        items-center
        justify-center
        rounded-lg
        font-semibold
        focus-visible:outline-2
        ${variants[variant]}
        ${sizes[size]}
      `}
    >
      {children}
    </button>
  );
}
```

Consumer:

```jsx
<Button variant="danger" size="lg">
  Delete
</Button>
```

Consumer không cần biết Tailwind classes.

---

## 150. Variant API nên semantic

Bad:

```jsx
<Button color="red-600">
```

Better:

```jsx
<Button variant="danger">
```

Nếu design đổi từ red-600 sang rose-700, caller không thay đổi.

Tương tự:

```text
density="compact"
```

tốt hơn:

```text
padding="p-2"
```

nếu component là public design-system component.

---

## 151. Class conflict

Bạn có thể compose:

```text
px-4
```

ở base và caller truyền:

```text
px-2
```

Một lỗi tư duy là nghĩ class viết sau trong attribute chắc chắn thắng.

CSS cascade dùng order của generated stylesheet, specificity và layers, không đơn giản dùng token order trong HTML class attribute.

Component library thường dùng conflict-aware merge helper để normalize Tailwind utility groups nếu muốn caller override.

---

## 152. `className` escape hatch

Một reusable component thường vẫn nhận:

```jsx
<Button className="w-full">
```

Semantic variant quyết định core visual contract. `className` cho local layout override.

Bạn cần document:
- caller override gì,
- conflict merge thế nào,
- internal classes hay caller classes ưu tiên.

---

# PHẦN XIX — ACCESSIBILITY

## 153. Tailwind không tạo accessibility semantics

Tailwind có utilities tuyệt vời cho focus, motion, ARIA state, nhưng nó không biến:

```html
<div class="cursor-pointer">
```

thành button.

Semantic HTML vẫn phải chọn đúng element.

---

## 154. `sr-only`

```html
<button>
  <svg aria-hidden="true">...</svg>
  <span class="sr-only">
    Close dialog
  </span>
</button>
```

`sr-only` dùng visually-hidden CSS pattern để text không nhìn thấy nhưng vẫn có accessible content.

`not-sr-only` restore style.

---

## 155. Focus visible

Đừng xóa focus indicator.

Good:

```html
<button
  class="
    focus-visible:outline-2
    focus-visible:outline-offset-2
    focus-visible:outline-blue-600
  "
>
```

Focus ring color phải có contrast đủ với surrounding background.

---

## 156. Disabled

Use:

```html
<button
  disabled
  class="
    disabled:cursor-not-allowed
    disabled:opacity-50
  "
>
```

Style không thay semantic disabled.

Nếu custom control không support native `disabled`, ARIA/business logic cần được thiết kế đúng chứ không chỉ thêm `opacity-50`.

---

## 157. Forced colors

High contrast/forced colors mode có thể override colors.

Tailwind có forced-color related variants/utilities. Default nên cho browser adapt.

Chỉ dùng `forced-color-adjust-none` targeted khi automatic override thực sự làm mất meaning.

---

# PHẦN XX — PERFORMANCE VÀ DEBUGGING

## 158. Tailwind CSS output không tỷ lệ trực tiếp với số class trong HTML

Nếu 100 buttons đều có `px-4`, generated CSS chỉ cần một `.px-4` utility rule, không phải 100 copies.

Điều làm CSS tăng là số **unique candidates** và variants.

Ví dụ:

```text
bg-red-500
hover:bg-red-500
md:bg-red-500
dark:bg-red-500
```

là các generated contexts khác nhau.

---

## 159. Arbitrary value cardinality

Một:

```text
w-[317px]
```

không phải performance disaster.

Nhưng nếu data tạo:

```text
w-[1px]
w-[2px]
...
w-[1000px]
```

thì bạn có hàng nghìn unique rules.

Dynamic numeric data nên dùng CSS variable.

---

## 160. Monorepo scanning

Không scan cả monorepo khổng lồ nếu app chỉ dùng một phần.

Use:
- `source()`,
- `@source`,
- `@source not`,
- `source(none)`.

Source detection không chỉ là config; nó là bundle ownership architecture.

---

## 161. Debug class không được generate

Hỏi lần lượt:

```text
Class có xuất hiện complete trong source không?
File có được scan không?
File có nằm node_modules/ignored path không?
Có cần @source không?
Utility có tồn tại ở v4.3 không?
Theme token cần thiết có tồn tại không?
Custom @utility có được register không?
```

Nếu generated CSS không có rule, chưa cần debug browser layout.

---

## 162. Debug class có rule nhưng UI sai

Khi DevTools cho thấy utility CSS tồn tại, chuyển mental model sang CSS:

```text
computed style
cascade/layer
specificity
parent layout
min/max sizing
overflow
stacking context
browser support
```

Đây là ranh giới giữa Tailwind debugging và CSS debugging.

---

# PHẦN XXI — TAILWIND + FRAMEWORKS

## 163. Tailwind + React

React dùng `className`.

Static mapping pattern:

```jsx
const sizeClasses = {
  sm: "px-3 py-1.5 text-sm",
  md: "px-4 py-2 text-base",
  lg: "px-5 py-3 text-lg",
};
```

Tránh runtime class synthesis.

Extract component khi combination lặp lại.

---

## 164. Tailwind + Vue/Svelte

Utilities trong template hoạt động tương tự HTML.

Nếu dùng component-scoped `<style>` và `@apply`, bạn có thể cần `@reference` để Tailwind biết theme/custom APIs của stylesheet chính.

Nhưng đừng dùng scoped CSS + `@apply` chỉ để thay một color; CSS variable trực tiếp thường đơn giản hơn.

---

## 165. Tailwind + CSS Modules

Bạn có thể dùng Tailwind trong markup và CSS Modules cho selector phức tạp/local style.

Không có luật bắt buộc phải chọn một trong hai.

Nhưng nếu cùng một concern được bọc qua:

```text
CSS Module
→ @apply
→ Tailwind utility
→ theme token
```

chỉ để đặt một `color`, abstraction đã quá nhiều.

---

## 166. Tailwind + SCSS

Tailwind v4 là CSS-first, nên nhiều project Tailwind-heavy không còn cần SCSS.

Nếu vẫn dùng SCSS, phân trách nhiệm rõ:

```text
Tailwind
→ utilities, variants, theme API

SCSS
→ compile-time maps/functions/mixins nếu project thực sự cần
```

Đừng maintain cùng một color token độc lập ở:
- Sass map,
- Tailwind `@theme`,
- CSS `:root`
cùng lúc.

---

# PHẦN XXII — MIGRATION TỪ V3

## 167. Tư duy migration

V3:

```text
tailwind.config.js
content
theme.extend
plugin
safelist
```

V4 hướng tới:

```text
@theme
automatic source detection
@source
@utility
@custom-variant
@source inline()
```

Migration không chỉ đổi syntax; nó là cơ hội gom configuration về CSS-first architecture.

---

## 168. `@config`

```css
@config "../../tailwind.config.js";
```

cho phép dùng legacy JS config trong v4 migration.

Nó là bridge, không nhất thiết là target cuối cho greenfield project.

---

## 169. `@plugin`

```css
@plugin "@tailwindcss/typography";
```

dùng legacy plugin ecosystem khi cần.

Project-owned simple custom utility/variant nên cân nhắc API CSS-first trước.

---

## 170. Important syntax

V4 preferred:

```text
flex!
bg-red-500!
```

thay vì old leading `!` style trong code cũ.

---

# PHẦN XXIII — PRODUCTION PATTERNS

## 171. Page container

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

Đây là composition của:
- fluid width,
- max constraint,
- centering,
- responsive gutters.

Bạn không cần `.container-custom` nếu pattern chỉ dùng vài nơi, nhưng nếu app có universal page shell thì extract component là hợp lý.

---

## 172. Stack

```html
<div class="flex flex-col gap-4">
```

Stack là vertical composition primitive.

Use cho:
- form,
- settings section,
- card body.

---

## 173. Cluster

```html
<div class="flex flex-wrap items-center gap-2">
```

Cluster là inline-like flexible group.

Use cho:
- tags,
- actions,
- filters,
- toolbar.

---

## 174. Responsive card grid

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

Simple viewport-responsive grid.

Nếu component context thay đổi mạnh, cân nhắc container query hoặc intrinsic auto-fit grid.

---

## 175. Sticky app header

```html
<header
  class="
    sticky
    top-0
    z-40
    border-b
    border-gray-200
    bg-white/90
    backdrop-blur
  "
>
```

Senior checks:
- sticky scroll container,
- backdrop performance,
- z-index contract,
- dark mode token.

---

## 176. Dialog shell

Use native `<dialog>` hoặc accessible dialog primitive.

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

Tailwind style không tự cung cấp focus management hay application state. Behavior vẫn thuộc native/platform/component layer.

---

## 177. Form field

```html
<label class="grid gap-1.5">
  <span class="text-sm font-medium">
    Email
  </span>

  <input
    type="email"
    class="
      rounded-lg
      border
      border-gray-300
      px-3
      py-2
      outline-none
      transition
      focus:border-blue-500
      focus:ring-2
      focus:ring-blue-500/20
      user-invalid:border-red-500
      disabled:bg-gray-100
      disabled:text-gray-500
    "
  >
</label>
```

Mỗi class có responsibility rõ: box, spacing, focus, validation, disabled.

---

## 178. Truncated row

```html
<div class="flex items-center gap-3">
  <img
    class="
      size-10
      shrink-0
      rounded-full
      object-cover
    "
  >

  <div class="min-w-0 flex-1">
    <p class="truncate font-medium">
      Long customer name...
    </p>
  </div>

  <button class="shrink-0">
    ...
  </button>
</div>
```

Đây là pattern production bạn nên thuộc vì nó kết hợp đúng intrinsic sizing và flex behavior.

---

# PHẦN XXIV — TƯ DUY SENIOR

## 179. Khi nào dùng utility, arbitrary value, theme, custom CSS?

Dùng core utility khi concern đã có vocabulary chuẩn:

```text
flex
gap-4
rounded-lg
```

Dùng arbitrary value khi value thực sự one-off:

```text
top-[117px]
```

Dùng `@theme` khi value lặp lại và thuộc design vocabulary:

```text
--radius-card
--color-action
```

Dùng CSS variable khi value phải thay đổi runtime.

Dùng `@utility` khi muốn thêm atomic reusable utility family.

Dùng plain CSS khi selector/behavior đọc dễ hơn bằng CSS.

Dùng component abstraction khi structure + style + state lặp lại.

---

## 180. Tailwind không thay design system

Tailwind cho rất nhiều class, nhưng một product tốt vẫn cần quyết định:
- color roles,
- typography scale,
- spacing rhythm,
- border radius,
- shadows,
- component variants,
- states.

Nếu mọi developer tùy ý chọn `blue-500`, `blue-600`, `indigo-500`, `violet-600`, Tailwind vẫn compile hoàn hảo nhưng design không nhất quán.

Framework là tool; design governance là architecture.

---

## 181. Tailwind senior phải biết khi nào không dùng Tailwind

Một selector:

```css
.rich-text
  > h2
  + p:first-letter {
  ...
}
```

có thể rõ hơn rất nhiều so với arbitrary variant dài.

Một third-party editor có hàng chục internal selectors nên có integration stylesheet.

Một custom CSS animation phức tạp có thể rõ hơn 20 utilities.

Senior Tailwind không theo ideology “không được viết CSS”. Senior chọn representation dễ hiểu, dễ test và dễ maintain nhất.

---

# PHẦN XXV — ROADMAP HỌC

## 182. Beginner phase

Ở giai đoạn đầu, hãy tập trung layout và visual foundation. Bạn cần có thể nhìn một mockup và tự viết được spacing, sizing, typography, color, border, Flexbox, Grid và responsive variants mà không liên tục copy từ example.

Một bài tập tốt là build ba component từ đầu: profile card, navbar và login form. Không dùng component library. Sau đó resize viewport và sửa overflow bằng chính kiến thức sizing đã học.

---

## 183. Intermediate phase

Sau khi basic utilities đã tự nhiên, học:
- arbitrary values,
- group/peer/has,
- dark mode,
- container queries,
- `@theme`,
- source detection,
- component variants.

Ở giai đoạn này mục tiêu không còn là “làm cho đẹp”, mà là tạo component reusable trong nhiều context.

---

## 184. Senior phase

Senior cần thiết kế:
- semantic component APIs,
- theme/token vocabulary,
- source ownership,
- monorepo/package integration,
- accessibility states,
- runtime CSS variable bridge,
- custom utilities/variants,
- CSS architecture.

Bạn cũng phải đọc DevTools generated CSS và giải thích vì sao một utility đang thắng/thua trong cascade.

---

# PHẦN XXVI — SELF TEST

## 185. Kiểm tra kiến thức

Sau khi học xong, bạn nên tự trả lời được bằng lời của mình: Tailwind khác inline style ở điểm nào; tại sao dynamic class string có thể không được generate; `@theme` khác normal CSS variable ra sao; tại sao `min-w-0` sửa ellipsis trong Flexbox; tại sao `md:` và `@md:` là hai loại responsive condition khác nhau; `group`, `peer`, `has` khác nhau theo selector relationship ra sao; `aria-*` và `data-*` nên dùng cho loại state nào; khi nào arbitrary value nên trở thành token; tại sao HTML class order không tự quyết định CSS winner; `@utility`, `@custom-variant`, `@apply`, `@reference` giải quyết các vấn đề khác nhau thế nào; và khi nào plain CSS tốt hơn Tailwind.

Nếu bạn chỉ nhớ class nhưng không trả lời được “CSS bên dưới đang làm gì?”, bạn chưa đạt senior. Nếu bạn có thể dự đoán behavior, thiết kế API component, debug generated CSS và chọn đúng abstraction, bạn đã có nền Tailwind rất mạnh.

---

# PHẦN XXVII — TÀI LIỆU CHÍNH THỨC

Tailwind CSS documentation:

https://tailwindcss.com/docs

Tailwind v4.3 release:

https://tailwindcss.com/blog/tailwindcss-v4-3

Theme variables:

https://tailwindcss.com/docs/theme

Source detection:

https://tailwindcss.com/docs/detecting-classes-in-source-files

Functions and directives:

https://tailwindcss.com/docs/functions-and-directives

Responsive design and container queries:

https://tailwindcss.com/docs/responsive-design

States and variants:

https://tailwindcss.com/docs/hover-focus-and-other-states

Upgrade guide:

https://tailwindcss.com/docs/upgrade-guide

---

# KẾT LUẬN

Cách học sai là:

```text
flex = flex
p-4 = padding
bg-blue-500 = blue
```

rồi cố nhớ hàng nghìn class.

Cách học đúng là:

```text
UI requirement
→ CSS behavior cần thiết
→ Tailwind utility biểu diễn behavior đó
→ variants/token/component architecture
```

Khi đạt senior, bạn nhìn:

```html
<div class="min-w-0 flex-1 truncate">
```

và không chỉ biết “đây là vài class Tailwind”. Bạn hiểu rằng Flexbox có automatic minimum size, `min-w-0` thay constraint, `flex-1` nhận available space, còn `truncate` chỉ có thể ellipsis khi box thật sự được phép co.

Đó là mức hiểu Tailwind mà tài liệu này hướng tới.
