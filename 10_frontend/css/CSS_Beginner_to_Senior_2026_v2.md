# CSS — Beginner → Senior Handbook (2026)

> Mục tiêu: đây không phải là danh sách property để học thuộc. Tài liệu được tổ chức theo **mental model của browser**, sau đó mới đến property, layout, responsive, architecture và CSS hiện đại.  
> Nếu đọc + tự code lại toàn bộ ví dụ + làm các bài tập cuối mỗi phần, bạn sẽ có nền tảng CSS đủ để làm production frontend ở mức senior.
>
> Ký hiệu:
> - **[CORE]**: phải biết và dùng thường xuyên.
> - **[ADV]**: kiến thức nâng cao, senior cần hiểu bản chất.
> - **[MODERN]**: CSS hiện đại, nên dùng khi browser support của project cho phép.
> - **⚠ Pitfall**: lỗi thường gặp.
> - **Senior note**: cách suy nghĩ/thiết kế CSS trong project thật.

---


# Cách đọc từng phần trong bản V2

Từ bản này, mỗi nhóm kiến thức quan trọng được bổ sung theo 4 tầng tư duy:

```text
Property / Syntax
→ Language Idiom
→ Coding / Programming Pattern
→ Design / Architecture Pattern
```

## 1. Property / Syntax

Đây là tầng thấp nhất: property làm gì, nhận value nào, computed behavior ra sao.

Ví dụ:

```css
display: flex;
gap: 1rem;
```

## 2. CSS Language Idiom

**Idiom** là một cách viết CSS ngắn, quen thuộc, lặp đi lặp lại vì nó phù hợp với cách browser layout hoạt động.

Ví dụ:

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

Đây là idiom **fluid centered container**.

## 3. Coding / Programming Pattern

Pattern ở tầng này giải quyết một bài toán implementation lặp lại.

Ví dụ **Media Object**:

```css
.media {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 1rem;
}
```

Dùng cho:
- avatar + content,
- icon + text,
- thumbnail + description.

## 4. CSS Design / Architecture Pattern

Không nên hiểu "Design Pattern trong CSS" theo nghĩa GoF của Java.

Trong CSS, design pattern thường là:
- cách tổ chức cascade,
- cách định nghĩa component contract,
- cách thiết kế token,
- cách quản lý variants/states,
- cách chia layout primitive,
- cách isolate style,
- cách responsive component.

Ví dụ:

```text
Global Token
→ Semantic Token
→ Component Token
→ Component Variant
```

Mỗi mục quan trọng có thêm:

```text
CSS Idiom
Coding Pattern
Design Pattern
Senior Note
Pitfall
```

Mục tiêu là học được **cách senior ghép các property thành hệ thống**, không chỉ nhớ tên property.

---

# 0. Bản đồ học CSS

## Thứ tự ưu tiên

1. **Syntax → Selector → Cascade → Specificity → Inheritance**
2. **Box model → Sizing → Normal flow → Display**
3. **Position → Containing block → Stacking context → z-index**
4. **Typography → Color → Background → Border**
5. **Flexbox**
6. **Grid**
7. **Responsive design → Media query → Container query**
8. **Transform → Transition → Animation**
9. **Custom properties → Design tokens**
10. **Architecture → Accessibility → Performance → Debugging**
11. **CSS hiện đại:** Nesting, Cascade Layers, `@scope`, `:has()`, Subgrid, Anchor Positioning, Scroll-driven Animations, View Transitions, `@property`, modern color.

## Mental model quan trọng nhất

Khi CSS "không chạy", đừng thử thêm `!important` ngay. Kiểm tra theo thứ tự:

```text
Selector có match không?
→ Declaration có valid không?
→ Cascade chọn declaration nào?
→ Specificity/source order/layer ra sao?
→ Property có inherit không?
→ Element đang ở formatting context nào?
→ Containing block là ai?
→ Kích thước available/intrinsic là bao nhiêu?
→ Có overflow/stacking context/transform nào ảnh hưởng không?
```

Đây là khác biệt lớn giữa người "biết CSS" và người debug CSS nhanh.

---

# 1. CSS Syntax & cách browser áp dụng CSS [CORE]

## 1.1 Rule cơ bản

```css
.card {
  color: #222;
  padding: 16px;
}
```

- `.card`: selector.
- `color`, `padding`: property.
- `#222`, `16px`: value.
- `color: #222`: declaration.
- Toàn bộ `{ ... }`: declaration block.

Nếu một declaration sai, browser thường bỏ declaration đó:

```css
.card {
  color: red;
  padding: abc; /* invalid → ignored */
}
```

## 1.2 Cách đưa CSS vào HTML

### External stylesheet — nên dùng production

```html
<link rel="stylesheet" href="/styles/app.css">
```

### Internal CSS

```html
<style>
  body { margin: 0; }
</style>
```

### Inline style

```html
<div style="color: red">...</div>
```

Inline style có specificity cao và khó maintain. Chỉ nên dùng khi:
- style được generate động thực sự,
- email HTML,
- framework/runtime buộc phải dùng.

## 1.3 Comment

```css
/* Comment */
```

CSS không hỗ trợ `//` như JavaScript/SCSS.

## 1.4 Shorthand và longhand

```css
margin: 10px 20px;
```

tương đương:

```css
margin-top: 10px;
margin-right: 20px;
margin-bottom: 10px;
margin-left: 20px;
```

### Quy tắc 1–4 giá trị

```css
margin: 10px;             /* all */
margin: 10px 20px;        /* top/bottom | left/right */
margin: 10px 20px 30px;   /* top | left/right | bottom */
margin: 10px 20px 30px 40px; /* top | right | bottom | left */
```

⚠ Shorthand có thể reset longhand mà bạn không để ý:

```css
.box {
  background-color: red;
  background: url(bg.png); /* background-color cũng bị reset */
}
```

**Senior note:** với component phức tạp, dùng shorthand khi bạn thực sự muốn set/reset cả nhóm.

---

# 2. Selectors [CORE]

## Pattern notes — Selectors

### CSS Idiom — State bằng attribute thay vì class tạm

```css
.tabs [aria-selected="true"] {
  font-weight: 700;
}

.menu[data-state="open"] {
  opacity: 1;
}
```

Ưu điểm:
- state gần với semantics hơn,
- JS không cần maintain thêm nhiều class,
- DevTools đọc state rõ.

### Coding Pattern — Low-specificity component selectors

Ưu tiên:

```css
.card {}
.card-title {}
.card-actions {}
```

thay vì:

```css
.page main section .card > header > h3 {}
```

Pattern này giảm coupling với DOM.

### Design Pattern — Selector as API

Hãy coi selector như public API.

Nếu CSS viết:

```css
.profile-card > div:nth-child(2) > span {}
```

thì DOM structure trở thành API ngầm và rất brittle.

Nếu viết:

```css
.profile-card__name {}
```

hoặc:

```css
.profile-card [data-slot="name"] {}
```

thì contract rõ hơn.

### Senior note

Selector tốt thường:
- đủ cụ thể để không leak,
- đủ yếu để override,
- không encode quá nhiều DOM structure,
- phản ánh role/state thay vì vị trí ngẫu nhiên.


# 2.1 Universal selector

```css
* {
  box-sizing: border-box;
}
```

`*` match mọi element.

Thường dùng trong reset:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

# 2.2 Type selector

```css
button {}
p {}
article {}
```

Specificity thấp, phù hợp base styles.

# 2.3 Class selector

```css
.card {}
.btn-primary {}
```

Đây nên là selector chính trong component CSS.

# 2.4 ID selector

```css
#header {}
```

ID có specificity rất cao.

**Senior rule:** tránh dùng ID cho styling reusable.

# 2.5 Attribute selectors

```css
input[type="text"] {}
button[disabled] {}
[data-state="open"] {}
```

Các operator:

```css
[attr]          /* tồn tại */
[attr="value"]  /* bằng chính xác */
[attr~="value"] /* word trong danh sách space-separated */
[attr|="en"]    /* en hoặc en-* */
[attr^="abc"]   /* bắt đầu bằng */
[attr$=".pdf"]  /* kết thúc bằng */
[attr*="foo"]   /* chứa substring */
```

Case-insensitive:

```css
a[href$=".PDF" i] {}
```

**Thực tế:** state styling rất tốt với `data-*`.

```css
.menu[data-state="open"] {
  opacity: 1;
}
```

---

# 3. Combinators [CORE]

## Descendant

```css
.card p {}
```

Match `p` ở bất kỳ depth nào trong `.card`.

## Child `>`

```css
.card > p {}
```

Chỉ match con trực tiếp.

## Adjacent sibling `+`

```css
label + input {}
```

Match `input` ngay sau `label`.

## General sibling `~`

```css
h2 ~ p {}
```

Match các `p` cùng parent đứng sau `h2`.

**Senior note:** selector càng phụ thuộc sâu vào DOM càng fragile.

Không nên:

```css
.page .main .content .card .header span {}
```

Nên:

```css
.card-title {}
```

---

# 4. Pseudo-classes [CORE → ADV]

## 4.1 Interaction states

```css
a:hover {}
button:active {}
input:focus {}
input:focus-visible {}
```

### `:focus` vs `:focus-visible`

- `:focus`: element đang focus.
- `:focus-visible`: browser xác định cần hiện focus indicator, thường khi keyboard navigation.

Production:

```css
.button:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Không nên:

```css
*:focus {
  outline: none;
}
```

vì phá keyboard accessibility.

## 4.2 Form states

```css
input:checked {}
input:disabled {}
input:enabled {}
input:required {}
input:optional {}
input:valid {}
input:invalid {}
input:placeholder-shown {}
input:read-only {}
```

Ví dụ:

```css
input:invalid:not(:placeholder-shown) {
  border-color: crimson;
}
```

## 4.3 Structural selectors

```css
:first-child
:last-child
:only-child
:first-of-type
:last-of-type
:nth-child(...)
:nth-of-type(...)
```

Ví dụ:

```css
tr:nth-child(even) {
  background: #f7f7f7;
}

.item:nth-child(3n + 1) {}
```

Công thức `an+b`:

```text
2n      → phần tử chẵn
2n+1    → phần tử lẻ
3n      → 3, 6, 9...
-n+3    → 3 phần tử đầu
n+4     → từ phần tử 4 trở đi
```

## 4.4 `:not()`

```css
button:not([disabled]) {}
```

Có thể nhận selector list:

```css
input:not([type="checkbox"], [type="radio"]) {}
```

## 4.5 `:is()` [ADV]

Gom selector:

```css
:is(h1, h2, h3) {
  line-height: 1.2;
}
```

Thay cho:

```css
h1, h2, h3 {}
```

Hữu ích với selector dài:

```css
.article :is(h2, h3, h4) {}
```

Specificity của `:is()` lấy specificity cao nhất trong arguments.

## 4.6 `:where()` [ADV]

Syntax tương tự `:is()` nhưng **specificity = 0**.

```css
:where(.content) h2 {
  margin-block-start: 2rem;
}
```

Rất hữu ích khi xây base/theme dễ override.

## 4.7 `:has()` [ADV/MODERN]

Selector "parent-aware":

```css
.card:has(img) {
  padding-top: 0;
}
```

Form group có input invalid:

```css
.field:has(input:invalid) .error {
  display: block;
}
```

Checkbox control parent:

```css
.row:has(input:checked) {
  background: #eef6ff;
}
```

**Senior note:** `:has()` giảm nhu cầu thêm class/state bằng JavaScript cho nhiều UI state đơn giản.

---

# 5. Pseudo-elements [CORE]

```css
::before
::after
::first-letter
::first-line
::selection
::marker
::placeholder
::file-selector-button
```

## `::before` / `::after`

Cần `content`:

```css
.badge::before {
  content: "NEW";
}
```

Decoration:

```css
.link::after {
  content: "";
  display: inline-block;
  width: 0.5em;
  height: 0.5em;
}
```

Không dùng pseudo-element cho content quan trọng về semantics.

## `::marker`

```css
li::marker {
  color: tomato;
  font-weight: 700;
}
```

## `::selection`

```css
::selection {
  background: gold;
  color: black;
}
```

---

# 6. Cascade — nền tảng sống còn của CSS [CORE/ADV]

## Pattern notes — Cascade

### CSS Idiom — Win by architecture, not by specificity

Không sửa kiểu:

```css
.page .dialog .button.primary {
  color: white !important;
}
```

nếu có thể sửa kiến trúc:

```css
@layer base, components, utilities;

@layer components {
  .button[data-variant="primary"] {
    color: white;
  }
}
```

### Coding Pattern — Default → Variant → State

```css
.button {
  /* default */
}

.button[data-variant="danger"] {
  /* variant */
}

.button:hover {
  /* interaction state */
}

.button:disabled {
  /* disabled state */
}
```

### Design Pattern — Layered Cascade

```text
reset
→ tokens
→ base
→ layout
→ components
→ utilities
→ overrides
```

Mục tiêu:
- override predictable,
- không specificity war,
- vendor CSS có chỗ riêng,
- component CSS dễ reason.

### Senior note

Nếu phải hỏi "selector nào mạnh hơn" quá thường xuyên, vấn đề thường nằm ở architecture chứ không phải thiếu kiến thức specificity.


Cascade quyết định declaration nào thắng.

Các yếu tố chính:

1. Origin/importance.
2. Cascade layer.
3. Specificity.
4. Scope proximity trong scoped CSS.
5. Source order.

## 6.1 Specificity

Có thể tư duy gần đúng:

```text
Inline      → 1-0-0-0
ID          → 0-1-0-0
Class,
attribute,
pseudo-class → 0-0-1-0
Element,
pseudo-element → 0-0-0-1
```

Ví dụ:

```css
#app .card p {}
```

cao hơn:

```css
.card p {}
```

## 6.2 Source order

Nếu specificity bằng nhau, rule viết sau thắng:

```css
.btn { color: blue; }
.btn { color: red; } /* thắng */
```

## 6.3 `!important`

```css
color: red !important;
```

Không nên dùng như cách fix mặc định.

Chỉ hợp lý khi:
- utility API có chủ đích,
- override external styles khó kiểm soát,
- accessibility/user override đặc biệt.

## 6.4 Global keywords

Các property thường chấp nhận:

```css
inherit
initial
unset
revert
revert-layer
```

### `inherit`

Ép lấy computed value từ parent.

```css
button {
  font: inherit;
}
```

### `initial`

Về initial value theo specification.

### `unset`

- property có inherit → behave như `inherit`;
- không inherit → behave như `initial`.

### `revert`

Quay về style của cascade origin trước.

### `revert-layer`

Bỏ declaration trong cascade layer hiện tại để quay về layer thấp hơn.

---

# 7. Cascade Layers `@layer` [ADV/MODERN]

Dùng để quản lý precedence theo kiến trúc thay vì specificity war.

```css
@layer reset, base, components, utilities;

@layer reset {
  * { box-sizing: border-box; }
}

@layer base {
  body { font-family: system-ui; }
}

@layer components {
  .button { padding: 0.75rem 1rem; }
}

@layer utilities {
  .hidden { display: none; }
}
```

Layer khai báo sau trong order có precedence cao hơn trong normal declarations.

**Senior architecture:**

```text
reset
tokens
base
layout
components
utilities
overrides
```

Ưu điểm:
- giảm `!important`,
- CSS từ vendor dễ kiểm soát,
- predictable override.

---

# 8. Inheritance [CORE]

Một số property inherit mặc định:

```text
color
font-family
font-size
font-style
font-weight
line-height
text-align
visibility
cursor
```

Nhiều property layout không inherit:

```text
margin
padding
border
width
height
display
position
```

Ví dụ:

```css
body {
  color: #222;
  font-family: system-ui;
}
```

Con thường tự kế thừa.

---

# 9. Values & Units [CORE]

# 9.1 Length units

## Absolute

```text
px
cm
mm
in
pt
pc
```

Web UI gần như chủ yếu dùng `px`.

## Font-relative

```text
em   → dựa trên font-size hiện tại/parent tùy property
rem  → dựa trên root font-size
ch   → width gần bằng ký tự "0"
ex   → x-height
lh   → line-height hiện tại
rlh  → root line-height
```

### `rem`

```css
.card {
  padding: 1rem;
}
```

Tốt cho spacing/type scale toàn app.

### `em`

Hữu ích khi component cần scale theo font:

```css
.icon {
  width: 1em;
  height: 1em;
}
```

⚠ nested `em` cho `font-size` có thể compound.

## Viewport units

```text
vw, vh
vmin, vmax
svw, svh
lvw, lvh
dvw, dvh
```

- `svh`: small viewport.
- `lvh`: large viewport.
- `dvh`: dynamic viewport.

Mobile full-screen:

```css
.page {
  min-height: 100dvh;
}
```

Thường tốt hơn `100vh` trên mobile browser có thanh address thay đổi kích thước.

## Container query units

```text
cqw, cqh
cqi, cqb
cqmin, cqmax
```

Ví dụ:

```css
.card-title {
  font-size: clamp(1rem, 5cqi, 2rem);
}
```

---

# 10. Percentages

Ý nghĩa `%` phụ thuộc property.

```css
width: 50%;
```

thường dựa vào containing block width.

Classic pitfall:

```css
padding-top: 10%;
```

Percentage padding truyền thống resolve theo inline size của containing block, không nhất thiết theo height.

---

# 11. CSS Math Functions [CORE/ADV]

## `calc()`

```css
width: calc(100% - 2rem);
```

## `min()`

```css
width: min(100%, 70rem);
```

## `max()`

```css
padding-inline: max(1rem, 5vw);
```

## `clamp(min, preferred, max)`

Responsive typography:

```css
font-size: clamp(1.5rem, 1rem + 2vw, 3rem);
```

Rất hữu ích cho:
- font-size,
- spacing,
- width,
- gap.

---

# 12. Custom Properties / CSS Variables [CORE]

## Pattern notes — Custom Properties

### CSS Idiom — Fallback token

```css
.card {
  color: var(--card-color, var(--color-text));
}
```

### Coding Pattern — Token pipeline

```css
:root {
  --blue-600: #2563eb;
  --color-action: var(--blue-600);
}

.button {
  --button-bg: var(--color-action);
  background: var(--button-bg);
}
```

Pipeline:

```text
Primitive token
→ Semantic token
→ Component token
```

### Design Pattern — Theme by token override

```css
:root {
  --surface: #fff;
  --text: #111;
}

[data-theme="dark"] {
  --surface: #111;
  --text: #f5f5f5;
}
```

Component không cần biết dark/light:

```css
.card {
  background: var(--surface);
  color: var(--text);
}
```

### Senior note

Custom property mạnh nhất khi dùng như **runtime contract**, không chỉ thay literal value.


```css
:root {
  --color-primary: #2563eb;
  --space-4: 1rem;
}

.button {
  background: var(--color-primary);
  padding: var(--space-4);
}
```

Fallback:

```css
color: var(--text-color, #222);
```

## Custom property có cascade + inherit

```css
.theme-dark {
  --surface: #111;
  --text: #fff;
}
```

## Component API

```css
.avatar {
  width: var(--avatar-size, 3rem);
  height: var(--avatar-size, 3rem);
}
```

Consumer:

```css
.profile-avatar {
  --avatar-size: 5rem;
}
```

**Senior note:** custom properties nên là **design tokens + component tokens**, không chỉ là biến thay text.

---

# 13. `@property` [ADV/MODERN]

Khai báo kiểu cho custom property:

```css
@property --progress {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}
```

Sau đó có thể animate typed value:

```css
.loader {
  --progress: 0%;
  transition: --progress 300ms;
}

.loader.done {
  --progress: 100%;
}
```

Descriptors:
- `syntax`: kiểu dữ liệu, ví dụ `<length>`, `<number>`, `<color>`, `<angle>`.
- `inherits`: `true | false`.
- `initial-value`: giá trị mặc định.

---

# 14. Box Model [CORE]

## Pattern notes — Box Model

### CSS Idiom — Universal border-box

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

### Coding Pattern — Section + inner wrapper

```css
.section {
  padding-block: 4rem;
}

.section__inner {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

Tách responsibility:
- outer section: vertical rhythm/background,
- inner wrapper: horizontal constraint.

### Design Pattern — Box responsibility

Một box nên có responsibility rõ:

```text
outer box → positioning/layout
middle box → spacing/border/background
inner box → content flow
```

Không phải lúc nào cũng cần nhiều wrapper; đây là mental model để debug.


Một box gồm:

```text
content
padding
border
margin
```

## `box-sizing`

### `content-box`

Default truyền thống:

```css
width: 200px;
padding: 20px;
border: 2px solid;
```

Rendered width = 244px.

### `border-box`

```css
box-sizing: border-box;
```

`width` đã bao gồm padding + border.

Global best practice:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

---

# 15. Width / Height / Sizing [CORE]

## Pattern notes — Sizing

### CSS Idiom — Fluid + capped width

```css
width: min(100%, 42rem);
```

### CSS Idiom — Prevent intrinsic overflow

```css
min-width: 0;
min-height: 0;
```

Đặc biệt quan trọng trong Flex/Grid.

### Coding Pattern — Intrinsic card width

```css
.card {
  inline-size: fit-content;
  max-inline-size: 100%;
}
```

### Design Pattern — Constraint-based layout

Senior thường không chỉ "set size" mà định nghĩa constraints:

```text
minimum
preferred
maximum
available space
intrinsic content size
```

Ví dụ:

```css
width: clamp(16rem, 40vw, 32rem);
```


```css
width
height
min-width
min-height
max-width
max-height
```

## Common values

```css
width: auto;
width: 100%;
width: 20rem;
width: min-content;
width: max-content;
width: fit-content;
width: fit-content(30rem);
```

### `min-content`

Kích thước nhỏ nhất content có thể co mà không overflow theo intrinsic rules.

### `max-content`

Kích thước content muốn có nếu không wrap.

### `fit-content`

Co giãn giữa min-content và max-content theo available space.

Thực tế:

```css
.tag {
  width: fit-content;
}
```

## `aspect-ratio`

```css
.video {
  aspect-ratio: 16 / 9;
}
```

Avatar:

```css
.avatar {
  width: 4rem;
  aspect-ratio: 1;
}
```

---

# 16. Margin [CORE]

```css
margin-top
margin-right
margin-bottom
margin-left
margin
```

Center block có width:

```css
.container {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
```

## Margin collapsing [ADV]

Vertical margins của normal-flow block có thể collapse.

```css
h2 { margin-bottom: 20px; }
p  { margin-top: 30px; }
```

Khoảng cách không nhất thiết 50px; có thể collapse thành 30px.

Không collapse trong nhiều trường hợp như:
- flex/grid layout,
- padding/border tách parent-child,
- block formatting context khác.

**Senior note:** dùng `gap` cho layout giữa các item thường predictable hơn margin choreography.

---

# 17. Padding [CORE]

```css
padding
padding-top
padding-right
padding-bottom
padding-left
```

Không nhận negative value.

---

# 18. Borders [CORE]

```css
border
border-width
border-style
border-color
border-radius
```

Style:

```text
none
solid
dashed
dotted
double
groove
ridge
inset
outset
```

Radius:

```css
border-radius: 12px;
border-radius: 50%;
```

Pill:

```css
border-radius: 9999px;
```

Individual corners:

```css
border-top-left-radius
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
```

---

# 19. Outline [CORE]

```css
outline: 2px solid currentColor;
outline-offset: 3px;
```

Khác border:
- không chiếm layout space,
- rất phù hợp focus indicator.

---

# 20. Display & Formatting Context [CORE/ADV]

## Pattern notes — Formatting Context

### CSS Idiom — `flow-root` để isolate block flow

```css
.component {
  display: flow-root;
}
```

### Coding Pattern — Layout primitives

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}

.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--cluster-gap, .75rem);
}
```

### Design Pattern — Formatting-context boundary

Component phức tạp nên chủ động tạo boundary khi cần:
- `display: flow-root`,
- Flex,
- Grid,
- `contain`,
- `isolation`.

Điều này giảm side effect từ bên ngoài.


Property:

```css
display
```

Các giá trị quan trọng:

```text
none
block
inline
inline-block
flex
inline-flex
grid
inline-grid
flow-root
contents
table
list-item
```

## `display: block`

- thường chiếm available inline width.
- bắt đầu dòng mới.

## `display: inline`

- flow cùng text.
- width/height không hoạt động như block.
- vertical margin/padding có behavior khác block.

## `inline-block`

Inline bên ngoài, block-like sizing bên trong.

## `display: none`

Loại khỏi layout và accessibility tree trong hầu hết trường hợp.

## `display: flow-root` [ADV]

Tạo Block Formatting Context mới.

Useful clear float / isolate flow:

```css
.container {
  display: flow-root;
}
```

## `display: contents`

Box của element biến mất nhưng children vẫn participate layout.

⚠ Cẩn thận accessibility/browser behavior với semantics đặc biệt.

---

# 21. Visibility & Opacity

## `visibility`

```css
visibility: visible;
visibility: hidden;
```

`hidden`: giữ layout space nhưng không paint.

## `opacity`

```css
opacity: 0;
opacity: 0.5;
opacity: 1;
```

`opacity: 0`:
- vẫn chiếm space,
- có thể vẫn nhận pointer/focus nếu không xử lý,
- tạo stacking context khi opacity < 1.

---

# 22. Normal Flow [CORE]

Normal flow gồm block flow + inline flow trước khi:
- float,
- absolute positioning,
- flex,
- grid,
- multicol
thay đổi cách layout.

Senior phải hiểu "default behavior" trước khi override.

---

# 23. Positioning [CORE/ADV]

## Pattern notes — Positioning

### CSS Idiom — Full inset overlay

```css
.overlay {
  position: absolute;
  inset: 0;
}
```

### CSS Idiom — Center absolute element

```css
.centered {
  position: absolute;
  inset: 50% auto auto 50%;
  translate: -50% -50%;
}
```

Nếu chỉ cần layout center, ưu tiên:

```css
.parent {
  display: grid;
  place-items: center;
}
```

### Coding Pattern — Positioning context

```css
.card {
  position: relative;
}

.card__badge {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-end: .5rem;
}
```

### Design Pattern — Overlay ownership

```text
local overlay → relative + absolute
viewport overlay → fixed
scroll-affixed UI → sticky
top-layer UI → dialog/popover
```


```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;
```

Offsets:

```css
top
right
bottom
left
inset
```

## `static`

Default. Offset không áp dụng.

## `relative`

Element vẫn giữ vị trí trong normal flow, nhưng có thể offset.

Quan trọng hơn: thường tạo containing block cho absolute child.

```css
.card {
  position: relative;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
}
```

## `absolute`

Ra khỏi normal flow.

Position dựa vào containing block phù hợp.

Modern shorthand:

```css
inset: 0;
```

tương đương:

```css
top: 0;
right: 0;
bottom: 0;
left: 0;
```

## `fixed`

Thường cố định theo viewport.

```css
.fab {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

⚠ ancestor có `transform`, `filter`, `perspective`... có thể thay containing block behavior.

## `sticky`

Hybrid relative/fixed theo scroll container.

```css
.header {
  position: sticky;
  top: 0;
}
```

Common failure:
- quên `top`,
- ancestor có overflow tạo scroll container khác,
- không đủ scroll space,
- layout constraints.

---

# 24. Containing Block [ADV]

Nhiều `%`, absolute offsets và sizing được tính dựa vào **containing block**.

Không phải lúc nào cũng là parent trực tiếp.

Absolute element thường tìm ancestor tạo containing block, ví dụ positioned ancestor.

Debug absolute/fixed lỗi phải hỏi:

> "Containing block thực sự của element này là element nào?"

---

# 25. z-index & Stacking Context [CORE/ADV]

## Pattern notes — Stacking

### CSS Idiom — Local stacking isolation

```css
.component {
  isolation: isolate;
}
```

### Coding Pattern — Semantic z-index scale

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 500;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

### Design Pattern — Layer contract

Không cho từng component tự tạo số `z-index`.

Định nghĩa semantic layers:
- content,
- sticky,
- dropdown,
- overlay,
- modal,
- toast.

### Senior note

Khi `z-index` lỗi, debug parent stacking context trước khi tăng số.


`z-index` không phải global number ranking đơn giản.

```css
.modal {
  position: fixed;
  z-index: 1000;
}
```

Một stacking context có thể được tạo bởi nhiều điều kiện, ví dụ:
- root element,
- positioned element với `z-index`,
- `position: fixed/sticky`,
- `opacity < 1`,
- `transform != none`,
- `filter`,
- `isolation: isolate`,
- một số flex/grid item có z-index,
- `contain` phù hợp.

Pitfall:

```text
child z-index: 999999
```

vẫn có thể nằm dưới element khác nếu parent stacking context thấp hơn.

**Senior strategy:** define z-index tokens:

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

Không dùng random `999999`.

---

# 26. Overflow [CORE]

```css
overflow
overflow-x
overflow-y
```

Values:

```text
visible
hidden
clip
scroll
auto
```

## `hidden`

Clip overflow và thường tạo scroll container semantics.

## `clip`

Clip mà không cung cấp scrolling như `hidden`.

## `auto`

Scrollbars khi cần.

Text single-line ellipsis:

```css
.truncate {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

Multiline line clamp:

```css
.clamp-3 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}
```

---

# 27. `contain` & `content-visibility` [ADV]

## `contain`

Giới hạn ảnh hưởng của subtree tới bên ngoài.

```css
.widget {
  contain: layout paint;
}
```

Values conceptually:
- `size`
- `inline-size`
- `layout`
- `style`
- `paint`
- combinations / `strict` / `content`

Dùng cẩn thận vì có thể thay sizing/positioning behavior.

## `content-visibility`

```css
.article-section {
  content-visibility: auto;
}
```

Browser có thể skip rendering off-screen content.

Có thể kết hợp:

```css
contain-intrinsic-size: auto 500px;
```

để giảm layout jump.

---

# 28. Flexbox [CORE]

## Pattern notes — Flexbox

### CSS Idiom — Cluster

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
}
```

Dùng cho:
- tags,
- actions,
- navbar,
- button groups.

### CSS Idiom — Push one item to edge

```css
.actions {
  margin-inline-start: auto;
}
```

### Coding Pattern — Media Object

```css
.media {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.media__body {
  min-width: 0;
  flex: 1;
}
```

### Coding Pattern — Safe flexible content

Nếu flex child chứa text/ellipsis:

```css
.content {
  min-width: 0;
}
```

### Design Pattern — One-dimensional composition

Flexbox phù hợp khi layout được mô tả bằng:

```text
items in a row
hoặc
items in a column
```

Nếu cần điều khiển nhiều rows + columns đồng thời, chuyển mental model sang Grid.


Flexbox là layout **1 chiều**: row hoặc column.

```css
.container {
  display: flex;
}
```

## 28.1 Container properties

### `flex-direction`

```text
row
row-reverse
column
column-reverse
```

```css
.toolbar {
  display: flex;
  flex-direction: row;
}
```

### `flex-wrap`

```text
nowrap
wrap
wrap-reverse
```

```css
.tags {
  display: flex;
  flex-wrap: wrap;
}
```

### `flex-flow`

Shorthand:

```css
flex-flow: row wrap;
```

### `justify-content`

Align theo **main axis**.

Common values:

```text
flex-start
flex-end
center
space-between
space-around
space-evenly
start
end
```

```css
.nav {
  display: flex;
  justify-content: space-between;
}
```

### `align-items`

Align items trên **cross axis**.

```text
stretch
flex-start
flex-end
center
baseline
```

### `align-content`

Chỉ có ý nghĩa khi có nhiều flex lines (`wrap`) và có dư cross-axis space.

```text
stretch
flex-start
flex-end
center
space-between
space-around
space-evenly
```

### `gap`

```css
gap: 1rem;
row-gap: 1rem;
column-gap: 2rem;
```

Ưu tiên `gap` thay vì margin giữa child.

---

# 29. Flex Item Properties [CORE]

## `flex-grow`

```css
.item {
  flex-grow: 1;
}
```

Phân chia **positive free space** theo tỉ lệ.

## `flex-shrink`

```css
.item {
  flex-shrink: 0;
}
```

Quyết định item co khi thiếu space.

## `flex-basis`

Initial main-size trước grow/shrink.

```css
.item {
  flex-basis: 20rem;
}
```

## `flex`

Shorthand:

```css
flex: 1;
```

thường behave gần:

```css
flex: 1 1 0%;
```

Các pattern:

```css
flex: none;       /* 0 0 auto */
flex: auto;       /* 1 1 auto */
flex: 1;          /* grow */
flex: 0 0 200px;  /* fixed basis */
```

## `align-self`

Override `align-items` cho một item.

## `order`

```css
order: 2;
```

⚠ Chỉ thay visual order, không nhất thiết thay DOM/read/focus order. Tránh dùng cho semantic reordering.

---

# 30. Flexbox Pitfall: `min-width: auto` [ADV]

Flex item mặc định có minimum size dựa vào content.

Do đó text dài có thể làm item không co:

```css
.row {
  display: flex;
}

.content {
  min-width: 0;
}
```

Đây là fix rất thường gặp.

Tương tự vertical flex:

```css
.content {
  min-height: 0;
  overflow: auto;
}
```

---

# 31. Flex Patterns

## Center

```css
.center {
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Navbar

```css
.nav {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav__actions {
  margin-inline-start: auto;
}
```

## Equal cards

```css
.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.card {
  flex: 1 1 18rem;
}
```

---

# 32. CSS Grid [CORE]

## Pattern notes — Grid

### CSS Idiom — Responsive auto grid

```css
.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}
```

### CSS Idiom — Safe fractional track

```css
grid-template-columns: minmax(0, 1fr);
```

Thường an toàn hơn plain `1fr` khi child có intrinsic width lớn.

### Coding Pattern — Sidebar layout

```css
.layout {
  display: grid;
  grid-template-columns:
    minmax(12rem, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

### Design Pattern — Track-first layout

Grid phù hợp khi structure quan trọng:

```text
sidebar | main
header
content rows
card matrix
```

Bạn thiết kế tracks trước rồi đặt content vào.


Grid là layout **2 chiều**.

```css
.grid {
  display: grid;
}
```

## 32.1 Grid tracks

```css
grid-template-columns: 1fr 1fr 1fr;
```

## `fr`

Fraction của available free space.

```css
grid-template-columns: 240px 1fr;
```

Sidebar + content.

## `repeat()`

```css
grid-template-columns: repeat(3, 1fr);
```

## `minmax()`

```css
grid-template-columns: repeat(3, minmax(0, 1fr));
```

`minmax(0, 1fr)` thường chống intrinsic overflow tốt hơn plain `1fr`.

## Responsive grid không media query

```css
grid-template-columns:
  repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
```

### `auto-fit` vs `auto-fill`

- `auto-fill`: giữ các hypothetical empty tracks.
- `auto-fit`: collapse empty tracks để existing items stretch.

---

# 33. Grid placement

Properties:

```text
grid-column-start
grid-column-end
grid-row-start
grid-row-end
grid-column
grid-row
grid-area
```

Example:

```css
.hero {
  grid-column: 1 / -1;
}
```

`-1` = last grid line.

Span:

```css
.card {
  grid-column: span 2;
}
```

---

# 34. Named Grid Areas

```css
.layout {
  display: grid;
  grid-template:
    "header header" auto
    "sidebar main" 1fr
    "footer footer" auto
    / 16rem 1fr;
}

header { grid-area: header; }
aside  { grid-area: sidebar; }
main   { grid-area: main; }
footer { grid-area: footer; }
```

Rất readable cho page layout.

---

# 35. Grid alignment

Container:

```text
justify-items
align-items
place-items
justify-content
align-content
place-content
```

Item:

```text
justify-self
align-self
place-self
```

Shorthand:

```css
place-items: center;
```

= `align-items` + `justify-items`.

---

# 36. Implicit Grid

Nếu item nằm ngoài explicit grid, browser tạo implicit tracks.

Properties:

```css
grid-auto-columns
grid-auto-rows
grid-auto-flow
```

Example:

```css
.grid {
  grid-auto-rows: minmax(6rem, auto);
}
```

`grid-auto-flow`:

```text
row
column
dense
row dense
column dense
```

⚠ `dense` có thể visually reorder items; cẩn thận accessibility.

---

# 37. Subgrid [ADV/MODERN]

## Pattern notes — Subgrid

### CSS Idiom — Aligned card internals

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.card {
  display: grid;
  grid-template-rows: subgrid;
  grid-row: span 3;
}
```

### Coding Pattern — Shared track contract

Parent định nghĩa track system; child reuse đúng track đó.

### Design Pattern — Nested alignment without duplicated dimensions

Subgrid giảm duplicate layout constants và giữ alignment xuyên hierarchy.


Child grid có thể kế thừa tracks từ parent.

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;
}
```

Use case:
- card title/body/footer cần align across cards,
- nested layout cần cùng column grid.

---

# 38. Grid vs Flexbox — chọn đúng

Dùng **Flexbox** khi:
- layout chủ yếu 1 axis,
- content quyết định size,
- navbar, toolbar, chips, row.

Dùng **Grid** khi:
- cần row + column,
- page layout,
- cards matrix,
- precise placement,
- tracks quan trọng hơn content.

Senior không hỏi "Grid hay Flex cái nào tốt hơn", mà hỏi:

> Layout này được điều khiển bởi **content flow** hay bởi **track structure**?

---

# 39. Float [LEGACY nhưng cần biết]

```css
img {
  float: left;
  margin-right: 1rem;
}
```

Float ngày nay chủ yếu hữu ích cho text wrapping quanh media.

Không nên dùng float để làm page layout hiện đại.

Clear:

```css
clear: both;
```

---

# 40. Multi-column Layout [ADV]

```css
.article {
  columns: 3 18rem;
  column-gap: 2rem;
}
```

Properties:

```text
column-count
column-width
columns
column-gap
column-rule
column-span
break-before
break-after
break-inside
```

Useful cho newspaper/text-heavy layouts.

---

# 41. Typography [CORE]

## Pattern notes — Typography

### CSS Idiom — Unitless line-height

```css
body {
  line-height: 1.5;
}
```

### CSS Idiom — Readable measure

```css
.prose {
  max-inline-size: 65ch;
}
```

### Coding Pattern — Fluid type scale

```css
:root {
  --step--1: clamp(.875rem, .84rem + .15vw, .95rem);
  --step-0: clamp(1rem, .95rem + .25vw, 1.125rem);
  --step-1: clamp(1.25rem, 1.05rem + .9vw, 1.75rem);
  --step-2: clamp(1.75rem, 1.25rem + 2vw, 3rem);
}
```

### Design Pattern — Typographic hierarchy

Xây một type system:
- body,
- small,
- label,
- heading,
- display.

Không chọn từng font-size ngẫu nhiên.


## `font-family`

```css
body {
  font-family:
    Inter,
    system-ui,
    -apple-system,
    "Segoe UI",
    sans-serif;
}
```

Luôn có generic fallback.

Generic families:
- `serif`
- `sans-serif`
- `monospace`
- `cursive`
- `fantasy`
- `system-ui`

## `font-size`

```css
font-size: 1rem;
```

Fluid:

```css
font-size: clamp(1rem, 0.95rem + 0.4vw, 1.25rem);
```

## `font-weight`

```text
normal ≈ 400
bold ≈ 700
100 ... 900
```

Variable font có thể hỗ trợ range.

## `font-style`

```text
normal
italic
oblique
```

## `line-height`

```css
body {
  line-height: 1.5;
}
```

Unitless thường tốt vì inherit theo multiplier.

Heading:

```css
h1 {
  line-height: 1.1;
}
```

## `font` shorthand

```css
font: italic 600 1rem/1.5 Inter, sans-serif;
```

⚠ Shorthand reset nhiều font sub-properties.

---

# 42. Text properties [CORE]

## `text-align`

```text
start
end
left
right
center
justify
```

Ưu tiên `start/end` cho internationalization.

## `text-decoration`

```css
a {
  text-decoration: underline;
  text-decoration-thickness: 0.08em;
  text-underline-offset: 0.2em;
}
```

Sub-properties:
- `text-decoration-line`
- `text-decoration-color`
- `text-decoration-style`
- `text-decoration-thickness`

## `text-transform`

```text
none
uppercase
lowercase
capitalize
```

Không dùng CSS uppercase thay cho dữ liệu nếu semantics/copy thực sự cần uppercase.

## `letter-spacing`

```css
.title {
  letter-spacing: -0.02em;
}
```

## `word-spacing`

Điều chỉnh space giữa từ.

## `text-indent`

Indent dòng đầu.

---

# 43. Wrapping / Breaking [CORE]

## `white-space`

Common:

```text
normal
nowrap
pre
pre-wrap
pre-line
break-spaces
```

### `nowrap`

Không wrap tại normal whitespace.

### `pre`

Giữ whitespace + newline, không wrap tự nhiên.

### `pre-wrap`

Giữ whitespace/newline nhưng cho wrap.

## `overflow-wrap`

```css
overflow-wrap: anywhere;
```

Cho phép break long URL/token.

## `word-break`

```text
normal
break-all
keep-all
```

Cẩn thận `break-all` vì có thể break rất xấu.

## `hyphens`

```css
p {
  hyphens: auto;
}
```

Cần `lang` đúng trong HTML để browser hyphenate tốt.

## `text-overflow`

```css
text-overflow: ellipsis;
```

Thường đi cùng `overflow:hidden` + `white-space:nowrap`.

## `text-wrap` [MODERN]

Useful values:

```text
wrap
nowrap
balance
pretty
```

Heading:

```css
h1 {
  text-wrap: balance;
}
```

Body copy:

```css
p {
  text-wrap: pretty;
}
```

---

# 44. Web Fonts `@font-face` [CORE/ADV]

```css
@font-face {
  font-family: "MyFont";
  src: url("/fonts/myfont.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

Descriptors quan trọng:
- `font-family`
- `src`
- `font-weight`
- `font-style`
- `font-display`
- `unicode-range`

`font-display` common:
- `auto`
- `block`
- `swap`
- `fallback`
- `optional`

Performance: ưu tiên WOFF2, subset khi cần, không load quá nhiều weights.

---

# 45. Color [CORE → MODERN]

## Pattern notes — Color

### CSS Idiom — `currentColor`

```css
.icon {
  fill: currentColor;
}
```

### Coding Pattern — Semantic color tokens

```css
--color-action: #2563eb;
--color-danger: #dc2626;
--color-text-muted: #6b7280;
```

### Design Pattern — Primitive → Semantic → Component

```text
blue-600
→ action-primary
→ button-primary-bg
```

### Senior note

Oklch phù hợp khi cần tạo palette có lightness dễ kiểm soát hơn HSL.


## Keywords

```css
color: red;
color: transparent;
color: currentColor;
```

`currentColor` = current value của `color`.

```css
.icon {
  border: 1px solid currentColor;
}
```

## Hex

```css
#ff0000
#f00
#ff000080 /* alpha */
```

## `rgb()`

Modern syntax:

```css
color: rgb(255 0 0 / 80%);
```

## `hsl()`

```css
color: hsl(220 90% 56%);
```

## `oklch()` [MODERN]

```css
color: oklch(62% 0.2 250);
```

Oklch hữu ích cho design system vì lightness gần với perceived lightness hơn HSL.

```css
:root {
  --brand: oklch(62% 0.20 255);
}
```

## Relative colors [MODERN]

```css
--brand-hover:
  oklch(from var(--brand) calc(l - 0.08) c h);
```

## `color-mix()`

```css
background:
  color-mix(in oklab, var(--brand) 20%, white);
```

## `light-dark()`

Kết hợp color scheme-aware values khi môi trường hỗ trợ:

```css
:root {
  color-scheme: light dark;
  --surface: light-dark(white, #111);
}
```

---

# 46. Backgrounds [CORE]

Properties:

```text
background-color
background-image
background-repeat
background-position
background-size
background-origin
background-clip
background-attachment
background
```

Example:

```css
.hero {
  background:
    linear-gradient(rgb(0 0 0 / .45), rgb(0 0 0 / .45)),
    url("/hero.jpg")
    center / cover
    no-repeat;
}
```

## `background-size`

```text
auto
cover
contain
<length>
<percentage>
```

- `cover`: cover box, có thể crop.
- `contain`: show toàn bộ image, có thể dư khoảng trống.

---

# 47. Gradients [CORE/ADV]

## Linear

```css
background:
  linear-gradient(135deg, #2563eb, #7c3aed);
```

## Radial

```css
background:
  radial-gradient(circle at top, white, #ddd);
```

## Conic

```css
background:
  conic-gradient(red, yellow, lime, cyan, blue, magenta, red);
```

Useful:
- charts,
- color wheels,
- decorative UI.

---

# 48. Shadows [CORE]

## `box-shadow`

```css
box-shadow: 0 8px 24px rgb(0 0 0 / 12%);
```

Syntax concept:

```text
offset-x offset-y blur spread color inset?
```

Multiple shadows:

```css
box-shadow:
  0 1px 2px rgb(0 0 0 / .08),
  0 8px 24px rgb(0 0 0 / .10);
```

## `text-shadow`

```css
text-shadow: 0 1px 2px rgb(0 0 0 / .3);
```

---

# 49. Object sizing: images/video [CORE]

## `object-fit`

```text
fill
contain
cover
none
scale-down
```

```css
.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## `object-position`

```css
object-position: center top;
```

---

# 50. `image-rendering`

Có thể điều khiển scaling image pixel art.

Common:
```text
auto
crisp-edges
pixelated
```

---

# 51. Filters [ADV]

```css
filter: blur(4px);
filter: brightness(1.1);
filter: contrast(1.2);
filter: grayscale(1);
filter: drop-shadow(0 4px 8px rgb(0 0 0 / .2));
```

Functions:
- `blur()`
- `brightness()`
- `contrast()`
- `drop-shadow()`
- `grayscale()`
- `hue-rotate()`
- `invert()`
- `opacity()`
- `saturate()`
- `sepia()`

## `backdrop-filter`

```css
.glass {
  background: rgb(255 255 255 / 70%);
  backdrop-filter: blur(16px);
}
```

Có cost rendering; test performance.

---

# 52. Blend Modes [ADV]

```css
mix-blend-mode: multiply;
background-blend-mode: multiply;
```

Common blend modes:
- `normal`
- `multiply`
- `screen`
- `overlay`
- `darken`
- `lighten`
- `difference`

---

# 53. Logical Properties [CORE/ADV]

## Pattern notes — Logical Properties

### CSS Idiom — Inline centering

```css
margin-inline: auto;
```

### CSS Idiom — Writing-mode-safe spacing

```css
padding-inline: 1rem;
padding-block: .75rem;
```

### Coding Pattern — International-ready component

```css
margin-inline-start: auto;
border-inline-start: 1px solid;
```

### Design Pattern — Direction-agnostic UI

Component tránh hard-code LTR assumptions để hỗ trợ RTL/localization tốt hơn.


Thay vì phụ thuộc `left/right/top/bottom`, dùng writing-mode-aware properties.

Physical:

```css
margin-left
padding-right
border-top
width
height
```

Logical:

```css
margin-inline-start
margin-inline-end
margin-block-start
margin-block-end

padding-inline
padding-block

border-inline-start
border-block-end

inline-size
block-size
```

Example:

```css
.card {
  padding-inline: 1rem;
  padding-block: 1.5rem;
  margin-inline: auto;
  max-inline-size: 70rem;
}
```

**Senior note:** logical properties giúp RTL/i18n tốt hơn.

---

# 54. Writing Modes [ADV]

```css
writing-mode: horizontal-tb;
writing-mode: vertical-rl;
writing-mode: vertical-lr;
```

Related:

```css
direction: rtl;
text-orientation: mixed;
```

Không nên dùng `direction` chỉ để reorder UI tùy tiện.

---

# 55. Responsive Design [CORE]

## Pattern notes — Responsive Design

### CSS Idiom — Content-driven breakpoint

Không chọn breakpoint vì tên thiết bị. Chọn tại điểm layout cần thay đổi.

### Coding Pattern — Fluid first, query second

```text
1. intrinsic sizing
2. flex/grid wrapping
3. clamp/min/max
4. media/container query khi cần
```

### Design Pattern — Responsive component

```css
.widget-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  .widget {
    grid-template-columns: 8rem 1fr;
  }
}
```

Component tự thích ứng theo không gian nó thực sự nhận được.


Responsive không chỉ là "mobile breakpoint".

Senior approach:
1. content-first,
2. intrinsic layout,
3. fluid sizing,
4. media query khi layout thực sự cần đổi,
5. container query khi component cần thích ứng theo container.

---

# 56. Media Queries [CORE]

```css
@media (min-width: 768px) {
  .layout {
    grid-template-columns: 16rem 1fr;
  }
}
```

Modern range syntax:

```css
@media (width >= 48rem) {}
```

Có thể:

```css
@media (48rem <= width < 80rem) {}
```

## Media features quan trọng

```text
width
height
orientation
aspect-ratio
resolution
hover
any-hover
pointer
any-pointer
prefers-color-scheme
prefers-reduced-motion
prefers-contrast
forced-colors
display-mode
```

---

# 57. Mobile-first

Base = mobile:

```css
.card {
  display: block;
}

@media (width >= 48rem) {
  .card {
    display: grid;
    grid-template-columns: 12rem 1fr;
  }
}
```

Không bắt buộc mọi project phải mobile-first, nhưng thường giúp progressive enhancement và CSS đơn giản.

---

# 58. User Preference Media Queries [CORE/ADV]

## Dark mode

```css
@media (prefers-color-scheme: dark) {
  :root {
    --surface: #111;
    --text: #eee;
  }
}
```

## Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto;
    animation-duration: 0.01ms;
    animation-iteration-count: 1;
    transition-duration: 0.01ms;
  }
}
```

Trong production có thể viết targeted hơn thay vì kill toàn bộ motion.

## Pointer

```css
@media (pointer: coarse) {
  .button {
    min-height: 44px;
  }
}
```

Đừng detect "mobile" bằng width nếu điều bạn thực sự quan tâm là input modality.

---

# 59. Container Queries [ADV/MODERN]

## Pattern notes — Container Query

### CSS Idiom — Named container contract

```css
.panel {
  container: panel / inline-size;
}
```

### Coding Pattern — Component mode switch

```css
@container panel (width < 24rem) {
  .profile {
    display: block;
  }
}

@container panel (width >= 24rem) {
  .profile {
    display: grid;
    grid-template-columns: auto 1fr;
  }
}
```

### Design Pattern — Contextual responsiveness

Component hỏi:

> "Không gian tôi thực sự nhận được rộng bao nhiêu?"

thay vì chỉ hỏi viewport.


Media query hỏi viewport.

Container query hỏi **container của component**.

Setup:

```css
.card-list {
  container-type: inline-size;
}
```

Query:

```css
@container (width >= 32rem) {
  .card {
    display: grid;
    grid-template-columns: 10rem 1fr;
  }
}
```

Named container:

```css
.sidebar {
  container-name: sidebar;
  container-type: inline-size;
}

@container sidebar (width >= 25rem) {
  .widget {
    grid-template-columns: 1fr 1fr;
  }
}
```

Shorthand:

```css
container: sidebar / inline-size;
```

**Senior use case:** component dùng trong main, sidebar, modal, dashboard card mà không phụ thuộc viewport.

---

# 60. Container Style Queries [MODERN]

Có thể query custom property/computed style state của container trong browser support phù hợp.

Concept:

```css
.card-wrapper {
  --density: compact;
}

@container style(--density: compact) {
  .card {
    padding: .5rem;
  }
}
```

Nên xem compatibility của browser targets trước khi dùng production.

---

# 61. Responsive Media [CORE]

Images:

```css
img,
video {
  max-width: 100%;
  height: auto;
}
```

Container:

```css
.wrapper {
  width: min(100% - 2rem, 75rem);
  margin-inline: auto;
}
```

---

# 62. CSS Transforms [CORE]

```css
transform: translateX(10px);
transform: translate(10px, 20px);
transform: scale(1.05);
transform: rotate(5deg);
transform: skewX(10deg);
```

Multiple:

```css
transform: translateY(-2px) scale(1.02);
```

⚠ transform order matters.

## Individual transform properties

```css
translate: 10px 0;
rotate: 5deg;
scale: 1.05;
```

## `transform-origin`

```css
transform-origin: center;
transform-origin: top left;
```

## 3D

```css
perspective: 1000px;
transform: rotateY(20deg);
transform-style: preserve-3d;
backface-visibility: hidden;
```

---

# 63. Transitions [CORE]

## Pattern notes — Transition

### CSS Idiom — Animate explicit properties

```css
transition:
  opacity 150ms ease,
  transform 150ms ease;
```

### Coding Pattern — State transition

```css
.menu {
  opacity: 0;
  translate: 0 -.5rem;
  transition:
    opacity 150ms ease,
    translate 150ms ease;
}

.menu[data-state="open"] {
  opacity: 1;
  translate: 0;
}
```

### Design Pattern — Motion as state feedback

Motion nên giải thích state change, không chỉ để trang "đẹp hơn".


```css
.button {
  transition:
    background-color 150ms ease,
    transform 150ms ease;
}
```

Sub-properties:

```text
transition-property
transition-duration
transition-timing-function
transition-delay
transition
```

Timing:

```text
linear
ease
ease-in
ease-out
ease-in-out
cubic-bezier(...)
steps(...)
```

### Không nên

```css
transition: all .3s;
```

trong component lớn vì:
- animate property ngoài ý muốn,
- khó predict,
- có thể gây performance issues.

Nên chỉ định:

```css
transition: opacity 150ms ease, transform 150ms ease;
```

---

# 64. Animations [CORE/ADV]

## Pattern notes — Animation

### CSS Idiom — Reduced-motion override

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-motion {
    animation: none;
  }
}
```

### Coding Pattern — Enter / Open / Leave state

```css
.toast[data-state="entering"] {}
.toast[data-state="open"] {}
.toast[data-state="leaving"] {}
```

### Design Pattern — Separate behavior from presentation

```text
Application state → data/aria attribute
CSS → visual state
```

JS không nên hard-code visual details; CSS không nên tự quyết định business state.


```css
@keyframes spin {
  to {
    transform: rotate(1turn);
  }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

Properties:

```text
animation-name
animation-duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction
animation-fill-mode
animation-play-state
animation
```

## `animation-iteration-count`

```text
1
2
infinite
```

## `animation-direction`

```text
normal
reverse
alternate
alternate-reverse
```

## `animation-fill-mode`

```text
none
forwards
backwards
both
```

## `animation-play-state`

```text
running
paused
```

---

# 65. Performance của animation [ADV]

Ưu tiên animate:
- `transform`
- `opacity`

Cẩn thận animation liên tục của:
- `width`
- `height`
- `top/left`
- `margin`
vì có thể trigger layout nhiều hơn.

Nhưng đừng biến "transform always fast" thành luật tuyệt đối; profiling với DevTools khi animation phức tạp.

## `will-change`

```css
.card:hover {
  will-change: transform;
}
```

⚠ Không set `will-change` cho hàng trăm elements hoặc global. Nó là hint có resource cost.

---

# 66. Scroll Behavior [CORE]

```css
html {
  scroll-behavior: smooth;
}
```

Tôn trọng reduced motion.

---

# 67. Scroll Snap [ADV]

Container:

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
```

Items:

```css
.carousel > * {
  scroll-snap-align: start;
}
```

Related:

```text
scroll-snap-type
scroll-snap-align
scroll-snap-stop
scroll-padding
scroll-margin
```

---

# 68. Scroll-driven Animations [MODERN]

Cho animation progress theo scroll thay vì time.

Concept:

```css
.progress {
  transform-origin: left;
  animation: grow linear;
  animation-timeline: scroll();
}

@keyframes grow {
  from { scale: 0 1; }
  to   { scale: 1 1; }
}
```

View timeline cho element:

```css
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}
```

Kiểm tra browser support trước khi dùng cho critical UX; progressive enhancement là hướng tốt.

---

# 69. View Transitions [MODERN]

Cho phép browser animate visual transition giữa UI states/pages tùy API/context.

CSS side thường liên quan pseudo-elements:

```css
::view-transition-old(root) {}
::view-transition-new(root) {}
```

Named transition:

```css
.hero {
  view-transition-name: hero-image;
}
```

Use case:
- route transitions,
- shared element transition,
- SPA state change.

Đừng làm animation cản thao tác hoặc quá dài.

---

# 70. Anchor Positioning [MODERN]

Dùng CSS để đặt popover/tooltip dựa trên anchor.

Anchor:

```css
.trigger {
  anchor-name: --trigger;
}
```

Positioned element:

```css
.tooltip {
  position: fixed;
  position-anchor: --trigger;
  left: anchor(right);
  top: anchor(bottom);
}
```

Hệ sinh thái còn gồm các concept/property như:
- `anchor-name`
- `position-anchor`
- `anchor()`
- `anchor-size()`
- fallback/position try features.

Use case:
- tooltip,
- dropdown,
- menu,
- popover.

Senior rule: kiểm tra browser target và fallback cho UI critical.

---

# 71. CSS Nesting [MODERN]

## Pattern notes — Nesting

### CSS Idiom — Nest states, not DOM depth

Tốt:

```css
.button {
  &:hover {}
  &:focus-visible {}
  &[data-variant="danger"] {}
}
```

Tránh nesting theo toàn bộ DOM tree.

### Coding Pattern — Component-local grouping

Nesting phù hợp cho:
- states,
- pseudo-elements,
- media query,
- container query,
- direct component slots.

### Design Pattern — Flat public API, nested implementation

Public selectors vẫn nên đơn giản; nesting chỉ hỗ trợ tổ chức source.


Native CSS nesting:

```css
.card {
  padding: 1rem;

  & .title {
    font-weight: 700;
  }

  &:hover {
    transform: translateY(-2px);
  }

  @media (width >= 48rem) {
    padding: 1.5rem;
  }
}
```

`&` đại diện selector hiện tại.

**Không nên nesting quá sâu:**

```css
.page {
  .section {
    .card {
      .header {
        .title {}
      }
    }
  }
}
```

Vì tạo selector coupling và specificity complexity.

Rule thực tế: 1–3 levels là đủ trong đa số component.

---

# 72. `@scope` [MODERN/ADV]

## Pattern notes — Scope

### CSS Idiom — Scoped typography

```css
@scope (.article) {
  h2 {}
  p {}
  a {}
}
```

### Coding Pattern — Scoped defaults

Dùng cho:
- article,
- widget,
- embedded app,
- third-party content area.

### Design Pattern — Controlled style boundary

`@scope` nằm giữa global CSS và full encapsulation như Shadow DOM/CSS Modules.


Giới hạn selector trong vùng DOM.

Concept:

```css
@scope (.article) {
  h2 {
    color: var(--heading-color);
  }
}
```

Có thể scope đến boundary trong syntax phù hợp.

Use case:
- component/themed subtree,
- tránh selectors leak,
- giảm nhu cầu BEM prefix trong một số kiến trúc.

---

# 73. `@supports` — Feature Queries [ADV]

```css
@supports (display: grid) {
  .layout {
    display: grid;
  }
}
```

Negation:

```css
@supports not (backdrop-filter: blur(1rem)) {
  .glass {
    background: #fff;
  }
}
```

Complex:

```css
@supports (display: grid) and (gap: 1rem) {}
```

Progressive enhancement:

```css
.card {
  background: #fff;
}

@supports (background: color-mix(in oklab, white, black)) {
  .card {
    background:
      color-mix(in oklab, var(--surface), var(--brand) 5%);
  }
}
```

---

# 74. `@media`, `@container`, `@supports` — khác nhau

| At-rule | Hỏi điều gì? | Use case |
|---|---|---|
| `@media` | môi trường/viewport/user preference | responsive page, dark mode |
| `@container` | kích thước/state container | responsive component |
| `@supports` | browser có support feature không | progressive enhancement |

---

# 75. Lists [CORE]

Properties:

```text
list-style-type
list-style-position
list-style-image
list-style
```

```css
ul {
  list-style: disc outside;
}
```

Custom marker:

```css
li::marker {
  color: var(--brand);
}
```

Counter advanced:

```css
.steps {
  counter-reset: step;
}

.steps li {
  counter-increment: step;
}

.steps li::before {
  content: counter(step) ". ";
}
```

---

# 76. Tables [CORE]

Properties:

```text
border-collapse
border-spacing
table-layout
caption-side
empty-cells
```

```css
table {
  width: 100%;
  border-collapse: collapse;
}
```

`table-layout`:

```text
auto
fixed
```

`fixed` giúp predictable widths/performance cho bảng lớn khi width xác định.

Responsive table thường cần wrapper:

```css
.table-scroll {
  overflow-x: auto;
}
```

---

# 77. Forms & Controls [CORE]

## `appearance`

```css
input,
button,
select {
  font: inherit;
}

.custom-checkbox {
  appearance: none;
}
```

⚠ Khi bỏ native appearance, bạn chịu trách nhiệm về:
- focus,
- checked state,
- disabled,
- high contrast,
- accessibility visuals.

## `accent-color`

```css
:root {
  accent-color: var(--brand);
}
```

Style native:
- checkbox,
- radio,
- range,
- progress (tùy browser).

## `caret-color`

```css
input {
  caret-color: var(--brand);
}
```

## `resize`

```css
textarea {
  resize: vertical;
}
```

Values:
- `none`
- `both`
- `horizontal`
- `vertical`

## `field-sizing` [MODERN]

Trong browser support phù hợp, giúp form controls size theo content.

---

# 78. Cursor & Pointer Behavior

## `cursor`

Common:

```text
auto
default
pointer
text
move
not-allowed
grab
grabbing
wait
progress
crosshair
```

Đừng dùng `cursor:pointer` cho non-interactive element nếu semantics không click được.

## `pointer-events`

```css
.overlay-decoration {
  pointer-events: none;
}
```

Values web UI thường:
- `auto`
- `none`

⚠ `pointer-events:none` không đồng nghĩa disabled semantic.

## `user-select`

```css
.user-select-none {
  user-select: none;
}
```

Chỉ dùng khi selection gây hại UX; text content thường nên select được.

---

# 79. Generated Content [ADV]

```css
content
quotes
counter-reset
counter-increment
counter-set
```

Pseudo-element:

```css
a.external::after {
  content: " ↗";
}
```

Không nhét information quan trọng chỉ trong CSS-generated content.

---

# 80. Shapes, Clip & Mask [ADV/MODERN]

## `clip-path`

```css
.avatar {
  clip-path: circle(50%);
}
```

Polygon:

```css
clip-path:
  polygon(50% 0, 100% 100%, 0 100%);
```

## `shape-outside`

Text wrap quanh shape, thường với float.

## Masks

Concept properties:
- `mask`
- `mask-image`
- `mask-size`
- `mask-position`
- `mask-repeat`

Useful cho icons/effects.

---

# 81. `isolation`

```css
.component {
  isolation: isolate;
}
```

Tạo stacking context mới và isolate blending.

Rất hữu ích để tránh negative z-index child "rơi" ra ngoài component.

---

# 82. `box-decoration-break`

Điều khiển decoration của fragmented inline/multiline boxes.

```css
.highlight {
  box-decoration-break: clone;
}
```

Có thể cần prefixed form trong một số target.

---

# 83. `writing-mode`, `direction`, international UI [ADV]

Đừng hard-code:

```css
margin-left: 16px;
text-align: left;
```

nếu project có RTL.

Nên:

```css
margin-inline-start: 1rem;
text-align: start;
```

---

# 84. At-rules cần biết

## [CORE]

```text
@media
@supports
@font-face
@keyframes
```

## [ADV/MODERN]

```text
@layer
@container
@property
@scope
@starting-style
@view-transition
@counter-style
@page
@import
@namespace
```

---

# 85. `@import`

```css
@import url("./theme.css");
```

Có thể kết hợp layer/support/media tùy syntax.

Tuy nhiên production thường ưu tiên bundler/build pipeline hoặc `<link>` vì `@import` có thể tạo dependency/loading considerations.

---

# 86. `@starting-style` [MODERN]

Hỗ trợ transition từ trạng thái element mới xuất hiện / discrete-state scenarios trong browser support phù hợp.

Concept:

```css
.dialog {
  opacity: 1;
  transition: opacity .2s;
}

@starting-style {
  .dialog {
    opacity: 0;
  }
}
```

Useful cho popover/dialog entry transitions.

---

# 87. Discrete transitions & `transition-behavior` [MODERN]

Một số discrete property có thể tham gia transitions với:

```css
transition-behavior: allow-discrete;
```

Use case:
- `display`,
- overlay/dialog/popover lifecycle
trong các browser support phù hợp.

---

# 88. Architecture: tổ chức CSS như senior [ADV]

## Pattern notes — Architecture

### CSS Idiom — One responsibility per layer

```text
tokens      → values
base        → element defaults
layout      → spatial primitives
components  → UI components
utilities   → atomic helpers
```

### Coding Pattern — Composition over overrides

```html
<div class="stack card">...</div>
```

thay vì tạo nhiều component variant chỉ để đổi spacing.

### Design Pattern — CUBE-like thinking

```text
Composition
Utility
Block
Exception
```

### Design Pattern — ITCSS-like ordering

Từ global/general → local/specific:
- settings/tokens,
- tools,
- generic,
- elements,
- objects,
- components,
- utilities.

Có thể kết hợp với `@layer`.

### Senior note

Architecture tốt là architecture mà dev mới có thể dự đoán:
- style nằm ở đâu,
- override thế nào,
- state viết ở đâu,
- token nào được dùng,
- component nào chịu trách nhiệm layout.


CSS production không chỉ là biết property.

Bạn cần quản lý:

```text
cascade
scope
tokens
component boundaries
variants
states
responsive rules
utilities
third-party CSS
dead CSS
build output
```

---

# 89. Naming Strategies

## BEM

```css
.card {}
.card__title {}
.card__body {}
.card--featured {}
```

Ưu:
- explicit,
- ít collision,
- dễ đọc trong plain CSS.

Nhược:
- verbose.

## Utility-first

```html
<div class="flex items-center gap-4">
```

Ưu:
- nhanh,
- constrained design tokens,
- ít custom CSS.

Nhược:
- markup nhiều class,
- cần convention/tooling.

## CSS Modules

```css
.title {}
```

Build system tạo scoped class names.

Ưu:
- local scope,
- giảm collision.

## CSS-in-JS

Có nhiều runtime/build-time approach. Không nên coi đây là "CSS replacement"; vẫn cần hiểu cascade/layout/browser.

---

# 90. Recommended Layer Architecture

```css
@layer reset, tokens, base, layout, components, utilities, overrides;
```

Ví dụ responsibility:

```text
reset       → normalize browser defaults
tokens      → design tokens
base        → body, headings, links
layout      → generic page/grid primitives
components  → button/card/modal
utilities   → single-purpose helpers
overrides   → rare integration overrides
```

---

# 91. Design Tokens

## Pattern notes — Design Tokens

### CSS Idiom — Semantic alias

```css
--gray-700: #374151;
--color-text-default: var(--gray-700);
```

### Coding Pattern — Token hierarchy

```text
Foundation token
→ Semantic token
→ Component token
→ State token
```

### Design Pattern — Theme contract

Theme ưu tiên override semantic tokens. Component tokens chỉ override khi component có requirement riêng.


```css
:root {
  --color-brand-500: oklch(62% .2 255);
  --color-text: oklch(25% .02 255);
  --color-surface: white;

  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;

  --radius-sm: .375rem;
  --radius-md: .75rem;

  --shadow-sm: 0 1px 2px rgb(0 0 0 / .08);
  --shadow-md: 0 8px 24px rgb(0 0 0 / .12);

  --duration-fast: 120ms;
  --duration-normal: 200ms;
}
```

Senior distinction:
- **Global token**: `--space-4`
- **Semantic token**: `--color-text-muted`
- **Component token**: `--button-bg`

---

# 92. Theme Architecture

```css
:root {
  --surface: #fff;
  --text: #171717;
}

[data-theme="dark"] {
  --surface: #111;
  --text: #f5f5f5;
}

body {
  background: var(--surface);
  color: var(--text);
}
```

Đừng copy toàn bộ component rules trong dark mode; override tokens trước.

---

# 93. Component State

## Pattern notes — Component State

### CSS Idiom — Attribute-driven state

```css
.accordion[data-state="open"] {}
.tabs [aria-selected="true"] {}
.button[aria-pressed="true"] {}
```

### Coding Pattern — State matrix

```text
variant: primary | secondary | danger
size: sm | md | lg
state: default | hover | focus | disabled | loading
```

### Design Pattern — Variant/state separation

Variant = identity/style mode.

State = tình trạng runtime/interaction.

Không trộn thành class kiểu `.button-danger-disabled`.


Nên encode state rõ:

```css
.button[data-variant="danger"] {}
.tabs [aria-selected="true"] {}
.accordion[data-state="open"] {}
```

Ưu tiên state từ semantic attributes khi có:

```css
button:disabled {}
input:checked {}
[aria-current="page"] {}
```

---

# 94. Specificity Strategy [ADV]

Target:
- phần lớn selectors low specificity,
- tránh ID,
- tránh nesting sâu,
- dùng layer,
- dùng `:where()` cho defaults,
- không "đấu specificity".

Base API:

```css
:where(.prose) h2 {
  margin-block: 2em .75em;
}
```

User override:

```css
.article h2 {
  margin-top: 3rem;
}
```

dễ thắng vì `:where()` = zero specificity cho phần đó.

---

# 95. Reset / Normalize

Minimal reset:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  hanging-punctuation: first last;
}

body {
  margin: 0;
  min-height: 100dvh;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}

input,
button,
textarea,
select {
  font: inherit;
}

p,
h1,
h2,
h3,
h4,
h5,
h6 {
  overflow-wrap: break-word;
}
```

Không blindly copy reset từ internet; hiểu từng line.

---

# 96. Accessibility [CORE/SENIOR]

## Pattern notes — Accessibility

### CSS Idiom — Focus-visible ring

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

### Coding Pattern — Accessible hidden text

```css
.visually-hidden {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
```

### Design Pattern — Progressive enhancement

Base experience phải dùng được trước; animation/filter/view-transition là enhancement.

### Senior note

Style đẹp nhưng làm mất focus, cắt text khi zoom hoặc reorder visual khác DOM là regression.


CSS có thể phá accessibility dù HTML đúng.

## Focus

Phải có visible focus:

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

## Contrast

Text/background phải có contrast phù hợp theo accessibility requirements của project.

Không chỉ dựa vào màu để truyền information:

Sai:

```text
red = error
green = success
```

Nên có icon/text/state thêm.

## Reduced motion

Support:

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-animation {
    animation: none;
  }
}
```

## Zoom

Tránh fixed heights làm text bị cut khi user zoom/font enlarge.

Sai:

```css
.button {
  height: 30px;
}
```

Tốt hơn:

```css
.button {
  min-height: 2.75rem;
  padding-block: .5rem;
}
```

## Visual order

Đừng dùng Flex/Grid `order` để tạo visual order khác hoàn toàn DOM order.

## Hidden content

Các kỹ thuật khác nhau có semantics khác:

```css
display: none;
visibility: hidden;
opacity: 0;
```

Không interchangeable.

---

# 97. Visually Hidden Utility

Cho content dành cho screen reader nhưng không muốn hiển thị visual:

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}
```

Đừng dùng `display:none` nếu bạn muốn assistive technology đọc content.

---

# 98. Forced Colors / High Contrast [ADV]

```css
@media (forced-colors: active) {
  .custom-control {
    border: 1px solid CanvasText;
  }
}
```

Không assume colors/shadows luôn được render như design.

---

# 99. Performance [ADV/SENIOR]

## Pattern notes — Performance

### CSS Idiom — Skip off-screen rendering khi phù hợp

```css
.long-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px;
}
```

### Coding Pattern — Animate compositor-friendly properties

Ưu tiên `opacity` và `transform` khi UX tương đương.

### Design Pattern — Performance budget

Theo dõi:
- CSS bundle size,
- font bytes,
- rendering cost,
- layout shift,
- long animation,
- large filter/backdrop regions.


CSS performance thường liên quan:
- stylesheet size,
- unused CSS,
- expensive rendering,
- font loading,
- image/background,
- layout thrashing từ JS + CSS,
- huge DOM,
- animation,
- style recalculation.

## Không micro-optimize selector vô nghĩa

Modern browser selector engine rất tối ưu. Vấn đề maintainability thường lớn hơn việc `.a > .b` nhanh hơn hay chậm hơn vài microsecond.

## Tập trung vào

1. ship ít CSS hơn,
2. remove unused CSS,
3. split critical/non-critical khi phù hợp,
4. avoid massive global rules,
5. optimize font/image,
6. avoid layout-heavy animation loops,
7. use DevTools Performance.

---

# 100. Rendering Pipeline Mental Model [ADV]

Simplified:

```text
DOM + CSSOM
→ Style
→ Layout
→ Paint
→ Composite
```

Một CSS change có thể ảnh hưởng các stage khác nhau.

Ví dụ conceptual:
- `width` → có thể layout + paint + composite.
- `background` → paint + composite.
- `transform` → thường có thể composite-friendly.
- `opacity` → thường composite-friendly.

Không phải guarantee tuyệt đối; browser implementation/context matters.

---

# 101. Layout Shift [ADV]

Tránh layout shift bằng:
- `width`/`height` hoặc `aspect-ratio` cho images/media,
- reserve space cho async content,
- font strategy phù hợp,
- không inject banner bất ngờ phía trên content.

```css
.card-image {
  aspect-ratio: 16 / 9;
}
```

---

# 102. Font Performance

Checklist:
- WOFF2.
- Chỉ load weights cần dùng.
- Variable font nếu có lợi.
- `font-display` phù hợp.
- preload only critical font.
- subset unicode nếu large font family.
- system fonts khi design cho phép.

---

# 103. CSS Debugging Workflow [SENIOR]

## Pattern notes — Debugging

### Coding Pattern — Constraint tracing

```text
computed width
→ max/min constraints
→ containing block
→ intrinsic content
→ flex/grid track
→ overflow
```

### Coding Pattern — Cascade tracing

```text
matched selector?
→ declaration valid?
→ layer?
→ specificity?
→ source order?
→ inheritance?
```

### Design Pattern — Debug from model, not trial-and-error

Tìm system quyết định behavior:
- cascade,
- formatting context,
- sizing algorithm,
- positioning,
- stacking.


Khi layout sai:

## Step 1 — Inspect element

DevTools:
- selector matched?
- property bị strike-through?
- computed value?
- inherited từ đâu?

## Step 2 — Box model

Check:
- content size,
- padding,
- border,
- margin.

## Step 3 — Layout context

Element là:
- block?
- flex item?
- grid item?
- positioned?
- scroll container?

## Step 4 — Constraints

Check:
- min/max width/height,
- `min-width:auto`,
- intrinsic sizing,
- overflow,
- aspect ratio.

## Step 5 — Position context

Check:
- containing block,
- stacking context,
- clipping ancestor.

## Step 6 — Browser responsive modes

Test:
- narrow viewport,
- zoom,
- long text,
- translated text,
- keyboard focus,
- reduced motion,
- dark mode.

---

# 104. Debug Helpers

```css
* {
  outline: 1px solid rgb(255 0 0 / .1);
}
```

Hoặc targeted:

```css
.debug {
  outline: 2px solid magenta !important;
}
```

Grid/Flex overlays trong Chrome/Firefox DevTools cực hữu ích.

---

# 105. Common CSS Bugs Senior phải nhận ra ngay

## Bug 1 — `z-index` không chạy

Cause thường:
- stacking context parent,
- `z-index` chưa applicable theo context,
- clipping.

## Bug 2 — Flex child overflow

Fix thường:

```css
.child {
  min-width: 0;
}
```

## Bug 3 — Vertical flex scroll không chạy

```css
.panel {
  display: flex;
  flex-direction: column;
  height: 100dvh;
}

.content {
  min-height: 0;
  overflow: auto;
}
```

## Bug 4 — `position: sticky` không stick

Check:
- có inset `top`?
- ancestor overflow?
- scroll container nào?
- parent height?

## Bug 5 — `height:100%` không có tác dụng

Percentage height cần containing block có definite height trong nhiều layout cases.

Dùng đúng context hoặc:

```css
min-height: 100dvh;
```

## Bug 6 — Ellipsis không chạy

Cần constraints:

```css
.text {
  min-width: 0;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
```

## Bug 7 — `margin:auto` tưởng luôn center

Auto margins hoạt động khác nhau tùy formatting context/axis/available free space.

## Bug 8 — absolute element "bay" sai nơi

Containing block không phải ancestor bạn nghĩ.

---

# 106. Responsive Layout Recipes

## Fluid container

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

## Auto-responsive cards

```css
.cards {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}
```

## Sidebar

```css
.layout {
  display: grid;
  grid-template-columns:
    minmax(0, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

## Sticky sidebar

```css
.sidebar {
  align-self: start;
  position: sticky;
  top: 1rem;
}
```

---

# 107. Modal Recipe

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 1rem;
  background: rgb(0 0 0 / .5);
}

.modal {
  width: min(100%, 36rem);
  max-height: min(80dvh, 50rem);
  overflow: auto;
  border-radius: 1rem;
  background: white;
}
```

Trong production ưu tiên native `<dialog>`/popover khi semantics phù hợp thay vì recreate mọi behavior bằng div.

---

# 108. Tooltip / Dropdown — senior considerations

CSS layout chỉ là một phần.

Cần nghĩ:
- anchor positioning,
- viewport collision,
- keyboard,
- focus management,
- escape key,
- ARIA semantics,
- portal/top layer,
- scroll clipping.

Không giải quyết complex overlay chỉ bằng `position:absolute; z-index:99999`.

---

# 109. Top Layer [ADV]

Một số browser-managed UI như dialog/popover có thể được đặt vào **top layer**, vượt stacking contexts bình thường.

Điều này giải thích tại sao z-index model của native dialog/popover khác div modal bình thường.

Pseudo-element liên quan backdrop:

```css
dialog::backdrop {
  background: rgb(0 0 0 / .5);
}
```

---

# 110. CSS and Shadow DOM [ADV]

Shadow DOM tạo style encapsulation.

Concept cần biết:
- shadow tree,
- `:host`,
- `:host(...)`,
- `::part(...)`,
- CSS custom properties xuyên boundary theo inheritance/cascade rules phù hợp.

Example:

```css
:host {
  display: block;
}

button {
  color: var(--button-color, currentColor);
}
```

Consumer có thể style exposed part:

```css
my-component::part(button) {}
```

---

# 111. Print CSS [ADV]

```css
@media print {
  nav,
  .ads {
    display: none;
  }

  a {
    color: black;
    text-decoration: underline;
  }
}
```

`@page` có thể điều khiển page-related styles trong print contexts.

---

# 112. CSS Functions nên biết

## Layout/math

```text
calc()
min()
max()
clamp()
minmax()
repeat()
fit-content()
```

## Variables/environment

```text
var()
env()
attr()
```

## Color

```text
rgb()
hsl()
hwb()
lab()
lch()
oklab()
oklch()
color()
color-mix()
light-dark()
```

## Images

```text
linear-gradient()
radial-gradient()
conic-gradient()
image-set()
```

## Transform

```text
translate()
scale()
rotate()
matrix()
perspective()
```

## Filters

```text
blur()
brightness()
contrast()
drop-shadow()
grayscale()
hue-rotate()
invert()
saturate()
sepia()
```

## Shapes

```text
circle()
ellipse()
inset()
polygon()
path()
```

---

# 113. CSS Global Keywords — phải nhớ

```text
inherit
initial
unset
revert
revert-layer
```

Ngoài ra CSS-wide keyword thường có `initial`, `inherit`, `unset`, `revert`, `revert-layer`.

---

# 114. Property Index theo nhóm

Đây là index để review nhanh. Không cần học thuộc tất cả trong một lần.

## Layout / Box

```text
display
box-sizing
width
height
min-width
min-height
max-width
max-height
aspect-ratio
margin
margin-top/right/bottom/left
padding
padding-top/right/bottom/left
overflow
overflow-x
overflow-y
overflow-anchor
visibility
opacity
contain
content-visibility
contain-intrinsic-size
```

## Position / stacking

```text
position
top
right
bottom
left
inset
z-index
isolation
```

## Flexbox

```text
flex
flex-basis
flex-grow
flex-shrink
flex-direction
flex-wrap
flex-flow
justify-content
align-items
align-content
align-self
order
gap
row-gap
column-gap
```

## Grid

```text
grid
grid-template
grid-template-columns
grid-template-rows
grid-template-areas
grid-auto-columns
grid-auto-rows
grid-auto-flow
grid-column
grid-column-start
grid-column-end
grid-row
grid-row-start
grid-row-end
grid-area
justify-items
align-items
place-items
justify-self
align-self
place-self
justify-content
align-content
place-content
gap
```

## Typography

```text
font
font-family
font-size
font-style
font-weight
font-stretch
font-variant
font-feature-settings
font-variation-settings
line-height
letter-spacing
word-spacing
text-align
text-transform
text-indent
text-decoration
text-decoration-line
text-decoration-style
text-decoration-color
text-decoration-thickness
text-underline-offset
text-shadow
text-overflow
text-wrap
white-space
word-break
overflow-wrap
hyphens
vertical-align
```

## Color / background

```text
color
background
background-color
background-image
background-size
background-position
background-repeat
background-attachment
background-origin
background-clip
color-scheme
accent-color
```

## Border / visual

```text
border
border-width
border-style
border-color
border-radius
border-top/right/bottom/left
outline
outline-width
outline-style
outline-color
outline-offset
box-shadow
filter
backdrop-filter
mix-blend-mode
background-blend-mode
```

## Images / replaced content

```text
object-fit
object-position
image-rendering
aspect-ratio
```

## Transform / animation

```text
transform
transform-origin
transform-style
translate
rotate
scale
perspective
perspective-origin
backface-visibility
transition
transition-property
transition-duration
transition-timing-function
transition-delay
transition-behavior
animation
animation-name
animation-duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction
animation-fill-mode
animation-play-state
animation-timeline
animation-range
will-change
```

## Scroll

```text
scroll-behavior
scroll-snap-type
scroll-snap-align
scroll-snap-stop
scroll-margin
scroll-padding
overscroll-behavior
scrollbar-color
scrollbar-width
```

## UI

```text
appearance
cursor
pointer-events
user-select
resize
caret-color
touch-action
```

## List / counters

```text
list-style
list-style-type
list-style-position
list-style-image
counter-reset
counter-increment
counter-set
content
quotes
```

## Table

```text
border-collapse
border-spacing
table-layout
caption-side
empty-cells
```

## Columns / fragmentation

```text
columns
column-count
column-width
column-gap
column-rule
column-span
break-before
break-after
break-inside
```

## Logical properties

```text
inline-size
block-size
min-inline-size
max-inline-size
min-block-size
max-block-size
margin-inline
margin-block
padding-inline
padding-block
inset-inline
inset-block
border-inline
border-block
```

## Writing / direction

```text
writing-mode
direction
unicode-bidi
text-orientation
```

## Shape / clipping / mask

```text
clip-path
shape-outside
shape-margin
mask
mask-image
mask-size
mask-position
mask-repeat
```

## Modern component/responsive

```text
container
container-name
container-type
anchor-name
position-anchor
view-transition-name
```

---

# 115. Selector Index cần thành thạo

```text
*
element
.class
#id
[attr]
[attr=value]
A B
A > B
A + B
A ~ B

:hover
:active
:focus
:focus-visible
:focus-within
:checked
:disabled
:enabled
:required
:optional
:valid
:invalid
:first-child
:last-child
:nth-child()
:nth-of-type()
:not()
:is()
:where()
:has()
:empty
:target
:root
:scope
:lang()

::before
::after
::marker
::selection
::placeholder
::first-letter
::first-line
::file-selector-button
::backdrop
```

---

# 116. At-rule Index cần thành thạo

```text
@media
@supports
@container
@layer
@scope
@property
@font-face
@keyframes
@starting-style
@view-transition
@counter-style
@page
@import
```

---

# 117. CSS Senior Checklist trước khi merge PR

## Correctness

- Selector có quá rộng không?
- Có dựa vào DOM nesting fragile không?
- Có specificity escalation không?
- Có `!important` không cần thiết không?
- Có global side effect không?
- Long text có break layout không?
- Loading state/empty state/error state ổn không?

## Responsive

- 320px-ish narrow layout?
- Tablet?
- Wide screen?
- Content translated dài hơn?
- Zoom 200%?
- orientation change?
- component trong container khác?

## Accessibility

- focus visible?
- keyboard?
- reduced motion?
- high contrast?
- state không chỉ dựa vào color?
- visual order = logical order?

## Performance

- animation property hợp lý?
- có giant shadow/filter/backdrop blur trên vùng lớn?
- unused CSS?
- font weights thừa?
- image dimensions reserved?

## Architecture

- dùng token thay hard-code khi semantic?
- component state API rõ?
- utility/component responsibility rõ?
- layer đúng?
- có thể override mà không specificity war?

---

# 118. Những anti-pattern cần bỏ

## 1. `!important` everywhere

Sai:

```css
.btn {
  color: red !important;
}
```

Hãy sửa cascade architecture.

## 2. Magic z-index

```css
z-index: 999999999;
```

Không sửa được stacking context cha.

## 3. Fixed pixel everything

```css
width: 1200px;
height: 600px;
```

Dễ phá responsive/zoom/content.

## 4. DOM-coupled selector

```css
main > div > div:nth-child(2) span {}
```

Rất fragile.

## 5. `transition: all`

Animate unintended changes.

## 6. Remove focus outline

```css
outline: none;
```

mà không replacement.

## 7. Absolute positioning để làm toàn bộ layout

Dùng Grid/Flex trước.

## 8. Media query theo device names

```css
@media (...) /* iPhone 14 */
```

Hãy chọn breakpoint theo content/layout, không theo tên thiết bị.

## 9. JavaScript cho vấn đề CSS giải được

Ví dụ nhiều layout responsive/state hiện có thể dùng:
- `:has()`
- container query
- Grid
- `clamp()`
- native nesting
- anchor positioning.

---

# 119. Học CSS như senior: 20 bài tập bắt buộc

1. Recreate card từ screenshot không dùng framework.
2. Navbar responsive bằng Flexbox.
3. Dashboard layout bằng Grid.
4. Product grid auto-fit không breakpoint.
5. Sticky header + sticky sidebar.
6. Modal scroll đúng khi content dài.
7. Truncate text trong flex child.
8. Table responsive.
9. Form validation styles.
10. Accessible focus states.
11. Dark theme bằng custom properties.
12. Design token system.
13. Component responsive bằng container query.
14. Tooltip/dropdown với anchor positioning + fallback.
15. Card row alignment bằng subgrid.
16. Animation respect reduced motion.
17. Scroll snap carousel.
18. Scroll-driven reading progress.
19. Native CSS nesting refactor.
20. `@layer` refactor project có vendor CSS.

---

# 120. Roadmap 30 ngày

## Ngày 1–3 — Core mechanics

Học:
- syntax,
- selectors,
- cascade,
- specificity,
- inheritance,
- values/units.

Output:
- 20 selector examples,
- specificity playground.

## Ngày 4–6 — Box/layout fundamentals

Học:
- box model,
- sizing,
- display,
- normal flow,
- overflow.

Output:
- article layout,
- cards,
- truncation cases.

## Ngày 7–9 — Positioning

Học:
- relative/absolute/fixed/sticky,
- containing block,
- z-index,
- stacking context.

Output:
- sticky header,
- modal,
- dropdown.

## Ngày 10–13 — Flexbox

Output:
- navbar,
- toolbar,
- media object,
- responsive card row.

## Ngày 14–17 — Grid

Output:
- dashboard,
- gallery,
- auto-fit cards,
- named areas,
- subgrid.

## Ngày 18–19 — Typography & visual

Học:
- fonts,
- wrapping,
- colors,
- backgrounds,
- borders,
- shadows,
- gradients.

## Ngày 20–21 — Responsive

Học:
- fluid design,
- media queries,
- user preferences,
- container queries.

## Ngày 22–23 — Motion

Học:
- transforms,
- transition,
- keyframes,
- scroll snap,
- reduced motion.

## Ngày 24–25 — Tokens & architecture

Học:
- custom properties,
- `@property`,
- naming,
- layers,
- component state.

## Ngày 26–27 — Modern CSS

Học:
- nesting,
- `:has()`,
- `@scope`,
- anchor positioning,
- view transitions,
- scroll-driven animations,
- modern colors.

## Ngày 28 — Accessibility

Test:
- keyboard,
- zoom,
- focus,
- reduced motion,
- contrast,
- RTL/logical props.

## Ngày 29 — Performance/debugging

DevTools:
- Computed styles,
- Flex/Grid overlay,
- Layers,
- Performance,
- Rendering.

## Ngày 30 — Final project

Build:
- responsive dashboard,
- dark/light theme,
- modal/dialog,
- dropdown/popover,
- cards,
- forms,
- table,
- motion,
- no CSS framework.

---

# 121. CSS → SCSS: phần nào để dành cho tài liệu SCSS sau

Sau khi nắm CSS này, tài liệu SCSS không cần lặp lại Flex/Grid/box model.

SCSS nên tập trung vào:

```text
Sass syntax
variables
nesting
parent selector &
partials/modules
@use
@forward
mixins
@include
functions
@if / @else
@for
@each
@while
maps
lists
interpolation
placeholder selectors
@extend
Sass module architecture
design token generation
utility generation
compile/build pipeline
migration từ @import → @use
CSS custom properties vs Sass variables
khi nào KHÔNG nên dùng Sass feature
```

**Senior distinction quan trọng:**

```text
Sass variable
→ compile-time

CSS custom property
→ runtime, cascade, inheritance, themeable
```

Ví dụ:

```scss
$spacing: 16px;
```

compile xong không còn `$spacing`.

Trong khi:

```css
--spacing: 1rem;
```

vẫn tồn tại trong browser runtime và override được.

---

# 122. Kiến thức bạn phải giải thích được nếu muốn tự đánh giá "Senior CSS"

Bạn nên trả lời rõ được các câu sau:

1. Cascade chọn rule thắng như thế nào?
2. `:is()` và `:where()` khác specificity ra sao?
3. Tại sao `z-index:999999` vẫn có thể nằm dưới element khác?
4. Containing block của absolute/fixed được xác định thế nào?
5. Tại sao flex item cần `min-width:0`?
6. `1fr` khác `minmax(0,1fr)` trong edge case nào?
7. `auto-fit` và `auto-fill` khác nhau thế nào?
8. Grid khác Flex theo mental model nào?
9. Tại sao `height:100%` thường "không chạy"?
10. Margin collapse là gì?
11. `overflow:hidden` ảnh hưởng scroll/sticky như thế nào?
12. BFC/formatting context giải quyết vấn đề gì?
13. Stacking context được tạo bởi những gì?
14. Container query tốt hơn media query ở trường hợp nào?
15. `rem`, `em`, `dvh`, `cqi` dùng khi nào?
16. `min-content`, `max-content`, `fit-content` là gì?
17. `@layer` giải quyết specificity architecture thế nào?
18. `@scope` khác CSS Modules/Shadow DOM như thế nào về concept?
19. `@property` hơn custom property thường ở đâu?
20. `oklch()` có lợi gì cho design system?
21. CSS nesting native khác SCSS nesting về runtime/build tooling thế nào?
22. Animation nào dễ gây layout/paint cost?
23. `opacity:0`, `visibility:hidden`, `display:none` khác nhau gì?
24. Focus accessibility nên style thế nào?
25. Logical properties giải quyết vấn đề gì?
26. Khi nào nên dùng `contain`/`content-visibility`?
27. Cách debug sticky?
28. Cách debug text overflow trong flex/grid?
29. Cách thiết kế design tokens?
30. Cách chia layer/components/utilities để không specificity war?

Nếu chưa giải thích được các câu này, hãy quay lại phần tương ứng thay vì học thêm framework CSS.

---

# 123. Tài liệu tham khảo chuẩn nên bookmark

- MDN CSS Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
- MDN CSS Guides: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides
- web.dev Learn CSS: https://web.dev/learn/css/
- W3C CSS specifications: https://www.w3.org/Style/CSS/
- Can I Use: https://caniuse.com/

Khi dùng feature hiện đại, luôn kiểm tra **browser targets của project**, không chỉ nhìn thấy syntax mới rồi dùng ngay.

---

# 124. Cheat Sheet cực ngắn

```css
/* Reset */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Tokens */
:root {
  --brand: oklch(62% .2 255);
  --space: 1rem;
}

/* Fluid container */
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}

/* Flex */
.flex {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* Grid */
.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 1rem;
}

/* Truncate flex child */
.min-w-0 {
  min-width: 0;
}

/* Sticky */
.sticky {
  position: sticky;
  top: 0;
}

/* Aspect ratio */
.media {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

/* Fluid type */
.title {
  font-size: clamp(1.5rem, 1rem + 2vw, 3rem);
  text-wrap: balance;
}

/* Focus */
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}

/* Component query */
.wrapper {
  container-type: inline-size;
}

@container (width >= 32rem) {
  .card {
    display: grid;
    grid-template-columns: 10rem 1fr;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .motion {
    animation: none;
    transition: none;
  }
}
```

---


# 125. Catalog — CSS Language Idioms quan trọng phải nhớ

## 125.1 Fluid centered container

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

## 125.2 Stack

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}
```

## 125.3 Cluster

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--cluster-gap, .75rem);
}
```

## 125.4 Center

```css
.center {
  display: grid;
  place-items: center;
}
```

## 125.5 Cover viewport

```css
.cover {
  min-height: 100dvh;
  display: grid;
  place-items: center;
}
```

## 125.6 Sidebar

```css
.with-sidebar {
  display: grid;
  grid-template-columns:
    minmax(12rem, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

## 125.7 Auto grid

```css
.auto-grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: 1rem;
}
```

## 125.8 Media object

```css
.media {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: 1rem;
}
```

## 125.9 Push action right

```css
.actions {
  margin-inline-start: auto;
}
```

## 125.10 Safe flex text

```css
.flex-child {
  min-width: 0;
}
```

## 125.11 Safe vertical flex scroll

```css
.panel {
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.panel__body {
  min-height: 0;
  overflow: auto;
}
```

## 125.12 Single-line truncate

```css
.truncate {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
```

## 125.13 Ratio media

```css
.media-frame {
  aspect-ratio: 16 / 9;
  overflow: hidden;
}

.media-frame > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## 125.14 Sticky region

```css
.sticky {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
}
```

## 125.15 Local overlay

```css
.wrapper {
  position: relative;
}

.wrapper__overlay {
  position: absolute;
  inset: 0;
}
```

## 125.16 Modal shell

```css
.modal-shell {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 1rem;
}
```

## 125.17 Intrinsic button

```css
.button {
  inline-size: fit-content;
  min-block-size: 2.75rem;
  padding-inline: 1rem;
}
```

## 125.18 Fluid font

```css
.title {
  font-size: clamp(1.75rem, 1rem + 3vw, 4rem);
}
```

## 125.19 Readable prose

```css
.prose {
  max-inline-size: 65ch;
  line-height: 1.65;
}
```

## 125.20 Theme token consumption

```css
.component {
  background: var(--surface);
  color: var(--text);
}
```

## 125.21 State via data attribute

```css
.panel[data-state="open"] {}
```

## 125.22 Semantic state via ARIA

```css
.tab[aria-selected="true"] {}
```

## 125.23 Focus ring

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

## 125.24 Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .animated {
    animation: none;
    transition: none;
  }
}
```

---

# 126. Catalog — Coding / Programming Patterns

## 126.1 Primitive → Component composition

Primitive:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--stack-gap, 1rem);
}
```

Component:

```html
<article class="card stack">
  ...
</article>
```

## 126.2 State Attribute Pattern

JS/state layer:

```js
element.dataset.state = "open";
```

CSS:

```css
.dropdown[data-state="open"] {}
```

Boundary:

```text
JS → state
CSS → presentation
```

## 126.3 Slot Pattern

```html
<div class="card">
  <div data-slot="header">...</div>
  <div data-slot="body">...</div>
</div>
```

```css
.card [data-slot="header"] {}
```

Useful khi muốn expose semantic component slots.

## 126.4 Variant Pattern

```css
.button[data-variant="primary"] {}
.button[data-variant="secondary"] {}
.button[data-variant="danger"] {}
```

## 126.5 Size Variant Pattern

```css
.button[data-size="sm"] {}
.button[data-size="md"] {}
.button[data-size="lg"] {}
```

## 126.6 Token Override Pattern

```css
.button {
  --button-bg: var(--color-action);
  background: var(--button-bg);
}

.hero .button {
  --button-bg: white;
}
```

Override token thường ổn hơn override nhiều internals.

## 126.7 Layout Wrapper Pattern

```html
<section class="section">
  <div class="container">
    ...
  </div>
</section>
```

Responsibility:
- `section`: background + vertical rhythm,
- `container`: horizontal constraint.

## 126.8 Progressive Enhancement Pattern

```css
.card {
  background: white;
}

@supports (backdrop-filter: blur(1rem)) {
  .card {
    backdrop-filter: blur(1rem);
  }
}
```

## 126.9 Container-responsive Component Pattern

```css
.component-shell {
  container-type: inline-size;
}

@container (width >= 30rem) {
  .component {
    display: grid;
  }
}
```

## 126.10 State + Transition Pattern

```css
.popover {
  opacity: 0;
  translate: 0 -.25rem;
}

.popover[data-state="open"] {
  opacity: 1;
  translate: 0;
}
```

## 126.11 Semantic CSS API Pattern

Expose:
- `data-variant`,
- `data-size`,
- semantic/ARIA state,
- selected custom property hooks.

Không expose internal DOM depth như API.

---

# 127. Catalog — CSS Design / Architecture Patterns

## 127.1 Layered Cascade Pattern

```text
reset
tokens
base
objects/layout
components
utilities
overrides
```

Implement tốt bằng `@layer`.

## 127.2 Token Hierarchy Pattern

```text
Foundation
→ Semantic
→ Component
→ State
```

Ví dụ:

```text
blue-600
→ color-action-primary
→ button-bg
→ button-bg-hover
```

## 127.3 Composition Pattern

Component compose các primitives:

```text
Stack
Cluster
Center
Grid
Sidebar
Container
```

thay vì mỗi component viết lại layout.

## 127.4 Encapsulation Pattern

Mức isolation tăng dần:

```text
naming convention
→ @scope
→ CSS Modules
→ Shadow DOM
```

Chọn đúng mức thay vì luôn dùng mức mạnh nhất.

## 127.5 Exception Pattern

Base:

```css
.card {}
```

Exception:

```css
.card[data-emphasis="high"] {}
```

Không duplicate thành `.special-card-v2`.

## 127.6 Theme-by-contract Pattern

```css
[data-theme="dark"] {
  --surface-default: #111;
  --text-default: #fff;
}
```

Components consume semantic tokens.

## 127.7 Responsive Ownership Pattern

```text
Page-level layout        → @media
Component-level layout   → @container
User preference          → media features
Feature availability     → @supports
```

## 127.8 Overlay Ownership Pattern

```text
local decoration → absolute
viewport UI      → fixed
scroll-affixed   → sticky
top-layer UI     → dialog/popover
anchor UI        → Anchor Positioning
```

## 127.9 Accessibility-first Styling Pattern

Base component phải:
- keyboard visible,
- readable khi zoom,
- không color-only state,
- reduced-motion compatible.

Visual enhancement đến sau.

## 127.10 Constraint-driven Layout Pattern

Không chỉ nghĩ:

```text
desktop = 1200px
tablet = 768px
mobile = 375px
```

Hãy nghĩ:

```text
content minimum
preferred size
maximum readable size
available space
wrapping threshold
```

CSS hiện đại (`min`, `max`, `clamp`, Grid, Container Query) hỗ trợ cách nghĩ này tốt hơn.

---

# 128. Senior Pattern Map — Property nào thường đi cùng property nào

## Ellipsis

```text
min-width: 0
+ overflow: hidden
+ white-space: nowrap
+ text-overflow: ellipsis
```

## Responsive image

```text
width/max-width
+ height:auto
+ object-fit
+ aspect-ratio
```

## Sticky

```text
position: sticky
+ top/inset
+ correct scroll container
+ enough scrollable space
```

## Absolute overlay

```text
parent position:relative
+ child position:absolute
+ inset
+ z-index nếu cần
```

## Modal

```text
fixed/top-layer
+ inset
+ center layout
+ max-height
+ overflow:auto
```

## Flexible text row

```text
display:flex/grid
+ minmax(0,1fr) hoặc min-width:0
+ gap
```

## Accessible interactive control

```text
minimum target size
+ padding
+ font:inherit
+ focus-visible
+ disabled state
+ hover as enhancement
```

## Theme

```text
custom properties
+ semantic tokens
+ data-theme/color-scheme
+ prefers-color-scheme optional
```

## Animation

```text
state attribute
+ transform/opacity
+ transition/animation
+ prefers-reduced-motion
```

## Component responsive

```text
container-type
+ @container
+ intrinsic layout
```

---

# 129. Khi nào Pattern trở thành Anti-pattern?

## BEM

Tốt khi:
- global/plain CSS,
- cần explicit naming.

Có thể dư khi:
- CSS Modules/Shadow DOM đã scope.

## Utility classes

Tốt khi:
- design constraints rõ,
- team quen composition.

Có thể xấu khi:
- utility naming tùy tiện,
- không có token system,
- dùng utility để encode business state.

## Nesting

Tốt:
- states,
- pseudo-elements,
- local media/container query.

Xấu:
- phản chiếu toàn bộ DOM tree.

## Custom properties

Tốt:
- runtime theme,
- component API,
- semantic tokens.

Xấu:
- hàng trăm variables không có semantics,
- abstraction cho value chỉ dùng một lần.

## `@layer`

Tốt:
- codebase lớn,
- vendor CSS,
- predictable cascade.

Có thể overkill:
- một component/file cực nhỏ.

## Container Query

Tốt:
- reusable component ở nhiều container.

Không cần thiết:
- page-level breakpoint đơn giản.

Senior không chỉ biết pattern; senior biết **khi nào không dùng pattern**.

---

# 130. Cách đọc CSS production như senior

Khi mở component, đọc theo thứ tự:

```text
1. Layout context
2. Component tokens
3. Base styles
4. Slots/elements
5. Variants
6. Runtime states
7. Responsive behavior
8. Motion
9. Accessibility
10. Browser fallback
```

Ví dụ:

```css
.card {
  --card-padding: 1rem;

  display: grid;
  gap: var(--card-padding);

  border-radius: .75rem;
  background: var(--surface);
}

.card[data-variant="featured"] {
  --card-padding: 1.5rem;
}

.card:focus-within {
  outline: 2px solid var(--focus);
}

@container (width >= 30rem) {
  .card {
    grid-template-columns: auto minmax(0, 1fr);
  }
}
```

Một file CSS dễ maintain khi dev khác đọc được flow này mà không phải reverse-engineer.

---

# 131. Learning Checkpoints theo cấp độ

## Beginner

Phải làm được:
- selector,
- cascade,
- box model,
- typography,
- spacing,
- Flexbox,
- Grid cơ bản,
- responsive media query.

Patterns cần nhớ:
- container,
- stack,
- cluster,
- center,
- truncate,
- responsive image.

## Intermediate

Phải hiểu:
- intrinsic sizing,
- min/max constraints,
- sticky,
- stacking context,
- Grid placement,
- custom properties,
- component variants,
- container queries.

Patterns cần biết:
- media object,
- sidebar,
- auto-grid,
- token override,
- state attribute,
- responsive component.

## Senior

Phải thiết kế được:
- cascade architecture,
- token hierarchy,
- component API,
- scope/layer strategy,
- accessibility behavior,
- performance strategy,
- browser fallback,
- debugging methodology.

Patterns cần thành thạo:
- layered cascade,
- semantic tokens,
- composition primitives,
- responsive ownership,
- overlay ownership,
- progressive enhancement,
- constraint-driven layout.

---


# Kết luận

Để lên senior CSS, mục tiêu không phải là nhớ 500 property.

Bạn cần đạt 5 tầng:

```text
1. Syntax + property
2. Cascade + inheritance
3. Layout mental model
4. Component/responsive architecture
5. Accessibility + performance + browser/debugging
```

Một senior frontend gặp UI bug không random đổi `display`, `position`, `z-index`, `width` cho đến khi "chạy".

Họ xác định:

```text
formatting context
→ sizing constraint
→ containing block
→ cascade
→ stacking context
→ rendering/accessibility impact
```

rồi sửa đúng nguyên nhân.

Đó là cách nên học CSS.
