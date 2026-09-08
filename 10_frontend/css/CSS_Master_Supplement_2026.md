# CSS Master Supplement 2026
## Những phần còn thiếu sau `CSS_Beginner_to_Senior_2026_v2.md`

> **Mục tiêu:** file này **không lặp lại** handbook V2.  
> Nó bổ sung những phần cần thiết để chuyển từ **“senior CSS thực chiến”** sang **“master CSS / hiểu browser-level behavior”**.
>
> Hãy đọc file này **sau** `CSS_Beginner_to_Senior_2026_v2.md`.
>
> Ký hiệu:
> - **[MUST]**: senior/master phải hiểu.
> - **[DEEP]**: browser internals / edge cases.
> - **[MODERN]**: CSS hiện đại.
> - **[2026]**: feature đặc biệt đáng chú ý trong web platform 2026.
> - **⚠**: browser support / accessibility / interoperability cần kiểm tra.
>
> Mental model:
>
> ```text
> V2
> ├─ biết CSS language
> ├─ layout
> ├─ component patterns
> └─ architecture
>
> Supplement
> ├─ browser formatting model
> ├─ property value lifecycle
> ├─ sizing algorithms
> ├─ top layer / advanced UI
> ├─ CSS APIs
> ├─ Shadow DOM / SVG
> ├─ advanced typography / scroll / print
> ├─ testing / compatibility
> └─ modern 2026 features
> ```

---

# 0. V2 đã đủ đến đâu?

## V2 đã cover rất tốt

```text
selectors
cascade fundamentals
specificity
inheritance
box model
position
stacking context
Flexbox
Grid
Subgrid
responsive
container queries
custom properties
@layer
@scope
nesting
animation
transition
scroll-driven animations
view transitions
anchor positioning
modern colors
accessibility
performance
architecture
idioms
coding patterns
design patterns
```

Đó là đủ để:
- làm production UI,
- đọc CSS framework,
- debug phần lớn layout bugs,
- thiết kế component system,
- review CSS ở mức senior.

## Nhưng “master CSS” còn cần

```text
1. Visual Formatting Model sâu hơn
2. Property value processing
3. Intrinsic sizing algorithms
4. Replaced elements
5. Line boxes / inline formatting
6. Formatting contexts / fragmentation
7. Cascade origins + animation/transition precedence
8. Modern pseudo-classes / pseudo-elements
9. Dialog / Popover / Top Layer
10. Customizable native controls
11. Scroll containers / scrollbars / overscroll
12. Environment variables / safe areas / foldable screens
13. Advanced typography
14. Wide-gamut color / contrast-color()
15. Motion Path / additive animation
16. Advanced View Transition
17. CSSOM / Typed OM
18. Constructable Stylesheets
19. Shadow DOM styling
20. Custom Highlight API
21. SVG + CSS
22. Print / paged media / fragmentation
23. Counters / custom counter styles
24. Advanced feature queries
25. Browser compatibility strategy
26. Visual regression / CSS testing
27. CSS linting / dead-CSS strategy
28. Performance profiling methodology
```

---

# 1. Property Value Lifecycle [MUST][DEEP]

Một declaration không đi thẳng từ source code đến pixels.

Mental model:

```text
Declared Value
→ Cascaded Value
→ Specified Value
→ Computed Value
→ Used Value
→ Actual Value
```

## 1.1 Declared value

Tất cả declarations có thể áp dụng:

```css
.card {
  width: 50%;
}

.card {
  width: 20rem;
}
```

Cả hai là declared values.

## 1.2 Cascaded value

Cascade chọn declaration thắng.

```css
.card {
  width: 20rem;
}
```

có thể trở thành cascaded value.

## 1.3 Specified value

Nếu không có declaration:
- inherit nếu property inherited,
- initial nếu không inherited,
- hoặc các defaulting rule khác.

## 1.4 Computed value

Browser resolve những gì có thể resolve trước layout.

Ví dụ:

```css
font-size: 2em;
```

có thể computed thành:

```text
32px
```

nếu parent font-size = 16px.

Nhưng:

```css
width: 50%;
```

có thể chưa resolve thành px cho đến khi layout context rõ.

## 1.5 Used value

Browser thực sự dùng trong layout.

Ví dụ:

```css
width: 50%;
```

container 800px:

```text
used width = 400px
```

## 1.6 Actual value

Giá trị cuối sau:
- rounding,
- device pixel constraints,
- rendering implementation.

---

# 2. Invalid at Computed-Value Time [DEEP]

Custom property có thể khiến declaration **parse hợp lệ nhưng computed invalid**.

Ví dụ:

```css
:root {
  --size: red;
}

.box {
  width: var(--size);
}
```

`var(--size)` parse được, nhưng:

```text
width: red
```

không hợp lệ.

Browser không nhất thiết fallback về declaration trước theo cách beginner thường nghĩ.

## Senior lesson

Fallback phải nằm trong `var()` khi cần:

```css
.box {
  width: var(--size, 10rem);
}
```

Nhưng fallback chỉ dùng nếu custom property:
- không tồn tại,
- hoặc invalid theo custom property semantics phù hợp.

`@property` giúp type custom property từ sớm.

---

# 3. Cascade Origins — Full Mental Model [MUST]

V2 nói cascade nhưng master cần hiểu **origin precedence**.

Nguồn CSS:

```text
User-agent styles
User styles
Author styles
Animations
Important declarations
Transitions
```

Simplified precedence từ thấp → cao:

```text
user-agent normal
user normal
author normal
keyframe animations
author !important
user !important
user-agent !important
transitions
```

Điểm rất dễ quên:

> Transition values có precedence cực cao trong cascade khi transition đang chạy.

---

# 4. Cascade Layers và `!important` đảo thứ tự [DEEP]

Normal layer order:

```css
@layer reset, base, components, utilities;
```

Normal declarations:

```text
reset
< base
< components
< utilities
< unlayered
```

Nhưng với `!important`, thứ tự layer **đảo lại**.

Điều này tồn tại để:
- bảo vệ foundational important rules,
- tránh layer mới dễ override important defaults.

## Senior pattern

Nếu buộc phải maintain third-party important CSS:

```css
@layer importantOverrides {
  ...
}
```

Đừng rải `!important` vào mọi layer.

---

# 5. Scope Proximity [MODERN][DEEP]

Trong `@scope`, nếu:
- origin bằng nhau,
- layer bằng nhau,
- specificity bằng nhau,

browser có thể xét **scope proximity** trước source order.

Concept:

```css
@scope (.outer) {
  .title {
    color: blue;
  }
}

@scope (.inner) {
  .title {
    color: red;
  }
}
```

Nếu `.title` gần `.inner` scope root hơn, scoped rule gần hơn có thể thắng.

## Important

`@scope` **không tự tăng specificity**.

Nhưng explicit `:scope` thì có specificity như pseudo-class.

---

# 6. Direct Target vs Inheritance [DEEP]

Rule trực tiếp target element luôn thắng inherited value.

```css
#parent {
  color: green;
}

h1 {
  color: purple;
}
```

`h1` màu purple.

Không quan trọng:

```text
#parent specificity rất cao
```

vì inherited value không cạnh tranh specificity trực tiếp với rule target `h1`.

---

# 7. Formatting Tree vs DOM Tree [MUST][DEEP]

CSS layout không hoàn toàn chạy trên DOM tree.

Browser tạo **box tree / formatting structure**.

Một element có thể:
- tạo một box,
- tạo nhiều boxes,
- không tạo box,
- tạo anonymous boxes.

Ví dụ:

```css
display: contents;
```

element box có thể biến mất nhưng children vẫn layout.

Pseudo-elements:

```css
::before
::after
```

tạo generated boxes dù không có DOM node tương ứng như element bình thường.

---

# 8. Anonymous Boxes [DEEP]

Browser có thể tạo box không có corresponding HTML element.

Ví dụ mixed block/inline content có thể tạo anonymous block boxes.

Bạn hiếm khi style trực tiếp anonymous box, nhưng nó giải thích:
- layout behavior khó hiểu,
- line boxes,
- table anonymous wrappers.

## Master lesson

DOM tree ≠ layout tree.

Khi CSS behavior lạ, đừng assume mỗi HTML element = đúng 1 rectangle.

---

# 9. Formatting Contexts [MUST]

Các formatting contexts quan trọng:

```text
Block Formatting Context (BFC)
Inline Formatting Context (IFC)
Flex Formatting Context
Grid Formatting Context
Table Formatting Context
Ruby Formatting Context
```

Formatting context định nghĩa:
- children layout như thế nào,
- margin interaction,
- float behavior,
- alignment,
- baseline.

---

# 10. Block Formatting Context (BFC) [MUST]

BFC là một vùng layout block tương đối độc lập.

Một số cách tạo BFC:

```css
display: flow-root;
overflow: auto;
overflow: hidden;
float: left;
position: absolute;
display: inline-block;
display: flex; /* flex container creates its own context */
display: grid;
```

Không phải mọi cách tạo BFC đều có semantics giống nhau.

## BFC giải quyết

### Float containment

```css
.container {
  display: flow-root;
}
```

### Tránh text wrap quanh float ngoài ý muốn

BFC mới không wrap quanh external float theo cách normal block có thể làm.

### Margin interaction

BFC ảnh hưởng margin collapsing behavior.

## Idiom

Nếu chỉ muốn tạo BFC:

```css
display: flow-root;
```

thường rõ nghĩa hơn:

```css
overflow: hidden;
```

vì `overflow:hidden` có thêm clipping side effect.

---

# 11. Inline Formatting Context & Line Boxes [MUST][DEEP]

Text inline không layout như Flexbox.

Browser tạo **line boxes**.

Trong một paragraph:

```html
<p>
  Hello <strong>world</strong> this is text.
</p>
```

Browser:
- split inline content,
- tạo line boxes,
- align inline-level boxes theo baseline.

Các properties quan trọng:

```text
line-height
vertical-align
font metrics
white-space
word-break
overflow-wrap
text-align
```

---

# 12. `vertical-align` — property thường bị hiểu sai [MUST]

`vertical-align` **không phải general-purpose vertical centering property**.

Nó chủ yếu áp dụng cho:
- inline-level boxes,
- table cells.

Values:

```text
baseline
middle
top
bottom
text-top
text-bottom
sub
super
<length>
<percentage>
```

## Inline icon alignment

```css
.icon {
  vertical-align: -0.125em;
}
```

có thể dùng để optical align icon với text.

## Không nên

```css
div {
  vertical-align: middle;
}
```

mong block element tự center trong parent.

Dùng Flex/Grid cho layout center.

---

# 13. Baseline Alignment [DEEP]

Flex/Grid hỗ trợ:

```css
align-items: baseline;
```

Nhưng baseline được lấy từ content/font/box rules.

Đây là lý do:

```css
.icon + label
```

có thể trông không thẳng dù geometric center giống nhau.

## Senior note

Typography alignment ≠ geometric center.

UI có text thường cần **baseline alignment** hơn center alignment.

---

# 14. Replaced Elements [MUST]

Replaced element là element mà nội dung render bên trong được thay bởi external resource/content.

Common:

```text
<img>
<video>
<iframe>
<embed>
```

Một số cases khác tùy element/type.

## Điểm đặc biệt

Replaced elements có thể có:
- intrinsic width,
- intrinsic height,
- intrinsic aspect ratio.

Ví dụ image file:

```text
1200 × 800
```

intrinsic ratio:

```text
3 / 2
```

---

# 15. Intrinsic Dimensions [MUST]

Đối với `<img>`:

```html
<img src="photo.jpg" alt="">
```

nếu không CSS sizing, browser có thể dùng intrinsic dimensions.

Nếu HTML có:

```html
<img
  src="photo.jpg"
  width="1200"
  height="800"
  alt=""
>
```

browser có thể reserve aspect ratio sớm, giảm CLS.

## Pattern

```css
img {
  max-width: 100%;
  height: auto;
}
```

giữ intrinsic aspect ratio khi co.

---

# 16. Replaced Element + `object-fit` [DEEP]

```css
.media {
  width: 300px;
  height: 200px;
  object-fit: cover;
}
```

Phân biệt:

```text
element box size
vs
content object size
```

`object-fit` thay đổi cách **resource bên trong box** fit.

Nó không thay layout size của element như `width`/`height`.

## `object-position`

```css
img {
  object-fit: cover;
  object-position: 50% 20%;
}
```

Useful giữ khuôn mặt ở vùng crop mong muốn.

---

# 17. Definite vs Indefinite Size [MUST][DEEP]

Một size có thể là **definite** hoặc không.

Điều này ảnh hưởng:
- percentage resolution,
- Grid/Flex sizing,
- percentage height,
- intrinsic sizing.

Ví dụ:

```css
.parent {
  height: auto;
}

.child {
  height: 50%;
}
```

`50%` có thể không resolve như user mong đợi vì parent block-size không definite.

## Senior debugging question

> Containing block có definite size trên axis này không?

---

# 18. Intrinsic vs Extrinsic Sizing [MUST]

## Intrinsic

Size dựa trên content:

```text
min-content
max-content
fit-content
```

## Extrinsic

Size bị external constraint quyết định:

```css
width: 20rem;
width: 50%;
```

Senior cần hiểu hai loại đang cạnh tranh.

---

# 19. `min-content` sâu hơn [DEEP]

`min-content` gần với:

> kích thước nhỏ nhất content có thể co theo wrapping opportunities tự nhiên.

Text:

```text
CSS is awesome
```

min-content width thường gần longest unbreakable segment.

Nếu có:

```css
overflow-wrap: anywhere;
```

min-content contribution có thể khác.

---

# 20. `max-content` sâu hơn [DEEP]

`max-content` gần với:

> size nếu content không wrap vì available space.

Có thể gây overflow mạnh với:
- long labels,
- tables,
- code,
- URLs.

---

# 21. `fit-content` sâu hơn [DEEP]

Conceptually nó clamp giữa intrinsic extremes và available space.

Mental model gần:

```text
min(
  max-content,
  max(min-content, available-size)
)
```

Đây không phải replacement chính xác cho mọi spec formula, nhưng là model học tốt.

---

# 22. Shrink-to-fit Sizing [DEEP]

Một số boxes như:
- floats,
- absolute positioned elements với auto width,
- inline-block,

có thể dùng behavior gần **shrink-to-fit**.

Mental model:

```text
không rộng hơn available space
không nhỏ hơn min-content
không vượt quá max-content nếu không cần
```

Đây là lý do:

```css
display: inline-block;
```

không chiếm full width như block.

---

# 23. Automatic Minimum Size in Flex/Grid [MUST]

V2 đã có `min-width:0`.

Master cần hiểu **vì sao**.

Flex/Grid item có automatic minimum size behavior để tránh content bị ép quá mức.

Do đó:

```css
.item {
  min-width: auto;
}
```

có thể effectively dựa vào content contribution.

Fix:

```css
.item {
  min-width: 0;
}
```

nói với sizing algorithm:

> item được phép co xuống dưới content-based automatic minimum.

---

# 24. Percentage Resolution Edge Cases [DEEP]

`%` không có một rule universal.

Nó phụ thuộc property.

Ví dụ:
- width `%` thường relative containing block inline size.
- percentage transforms relative transform reference box.
- percentage border-radius relative box dimension.
- percentage translate relative element itself.
- percentage background-position có algorithm riêng.

## Senior rule

Không học `%` như unit.

Học `%` **theo từng property family**.

---

# 25. Margin Collapse — Deep Cases [DEEP]

Vertical margins có thể collapse:
- adjacent siblings,
- parent + first/last child trong conditions phù hợp,
- empty blocks.

Negative margins cũng tham gia collapsing algorithm.

## Không collapse giữa flex/grid items

```css
.container {
  display: flex;
}
```

child margins không collapse như normal block flow.

## Pattern

Cho spacing system:

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
```

`gap` predictable hơn margin collapse.

---

# 26. Float — đúng bản chất [DEEP]

Float không chỉ là legacy layout.

Use case thực sự:

> cho text inline wrap xung quanh object.

```css
.article img {
  float: inline-start;
  margin-inline-end: 1rem;
  margin-block-end: .5rem;
}
```

`shape-outside` có thể thay vùng wrap:

```css
figure {
  float: left;
  shape-outside: circle(50%);
}
```

---

# 27. Fragmentation [DEEP]

Content có thể bị split qua:
- pages,
- columns,
- regions/fragmentainers.

Properties:

```text
break-before
break-after
break-inside
orphans
widows
```

## Print / columns

```css
.card {
  break-inside: avoid;
}
```

Có thể giúp card không bị chia giữa cột/page.

Không phải browser luôn đảm bảo 100% nếu constraint không thể thỏa.

---

# 28. `orphans` và `widows` [ADV]

Dùng trong paged/multicol typography.

```css
p {
  orphans: 3;
  widows: 3;
}
```

- `orphans`: minimum lines ở cuối fragment trước break.
- `widows`: minimum lines ở đầu fragment sau break.

Useful:
- print,
- long-form publishing.

---

# 29. Advanced Selectors — `:nth-child(... of S)` [MODERN]

Có thể filter subset trước khi đếm.

```css
.item:nth-child(2n of .visible) {
  background: #f5f5f5;
}
```

Khác:

```css
.item.visible:nth-child(2n)
```

Câu đầu:
- đếm **chỉ `.visible`**.

Đây là rất hữu ích cho zebra stripes khi có hidden/filter rows.

---

# 30. `:dir()` [ADV]

Match directionality:

```css
:dir(rtl) .icon-next {
  rotate: 180deg;
}
```

Tốt hơn tự gắn `.rtl` trong nhiều case.

---

# 31. `:lang()` [ADV]

```css
:lang(ko) {
  word-break: keep-all;
}

:lang(ja) {
  line-break: strict;
}
```

Styling theo document language semantics.

---

# 32. Link pseudo-classes sâu hơn

Common:

```text
:any-link
:link
:visited
```

`:any-link` match link có href bất kể visited state.

```css
:any-link {
  text-underline-offset: .15em;
}
```

## Privacy note

`:visited` bị browser hạn chế style/query vì history privacy.

Đừng dựa vào computed visited styles cho application logic.

---

# 33. Form State Pseudo-classes mở rộng [ADV]

Ngoài V2:

```text
:user-valid
:user-invalid
:indeterminate
:default
:in-range
:out-of-range
:read-write
:autofill
```

## `:user-invalid`

Khác `:invalid`:

- `:invalid` có thể match ngay.
- `:user-invalid` phản ánh invalidity sau user interaction theo browser behavior.

Pattern:

```css
input:user-invalid {
  border-color: var(--color-danger);
}
```

UX thường tốt hơn đỏ form ngay khi page load.

---

# 34. Element Display State Pseudo-classes [2026]

Quan trọng:

```text
:open
:popover-open
:modal
:fullscreen
:picture-in-picture
```

## `:open`

Match element có open/closed state và hiện đang open.

Ví dụ:

```css
details:open > summary {
  font-weight: 700;
}
```

Hoặc modern native controls/open UI khi applicable.

## `:popover-open`

```css
[popover]:popover-open {
  opacity: 1;
}
```

## `:modal`

```css
dialog:modal {
  border: 0;
}
```

---

# 35. Media State Pseudo-classes [2026]

Interop 2026 chú ý tới media pseudo-classes:

```text
:playing
:paused
:seeking
:buffering
:stalled
:muted
:volume-locked
```

Concept:

```css
video:playing {
  outline-color: green;
}
```

Use case:
- custom media UI,
- declarative visual state.

⚠ Kiểm tra browser target vì đây là vùng interoperability đang tiếp tục cải thiện.

---

# 36. Highlight Pseudo-elements [MODERN]

Ngoài `::selection`:

```text
::target-text
::spelling-error
::grammar-error
::highlight(name)
```

Ví dụ:

```css
::spelling-error {
  text-decoration: wavy red underline;
}
```

Support/allowed properties có giới hạn tùy highlight type.

---

# 37. CSS Custom Highlight API [MODERN]

Cho phép style arbitrary text ranges **không cần wrap thêm span**.

JS:

```js
const range = new Range();
range.setStart(textNode, 10);
range.setEnd(textNode, 20);

const highlight = new Highlight(range);
CSS.highlights.set("search-result", highlight);
```

CSS:

```css
::highlight(search-result) {
  background: gold;
  color: black;
}
```

Use cases:
- editor,
- search results,
- syntax tooling,
- collaboration annotations.

## Design Pattern — Presentation Range

Không mutate DOM chỉ để highlight text.

```text
Range model
→ Highlight registry
→ CSS presentation
```

⚠ Highlight không tự tạo semantic meaning cho accessibility.

---

# 38. Top Layer [MUST][MODERN]

Browser có một rendering concept gọi là **top layer**.

Elements như:
- modal dialog,
- popovers,
- fullscreen element,

có thể nằm ở top layer.

Điều này giúp tránh:

```text
z-index war
overflow clipping ancestor
stacking context traps
```

## Important

Top layer không phải:

```css
z-index: 999999;
```

Nó là riêng một browser-managed layer ngoài document stacking contexts thông thường.

---

# 39. `<dialog>` Styling sâu hơn [MUST]

```css
dialog {
  border: 0;
  border-radius: 1rem;
}

dialog::backdrop {
  background: rgb(0 0 0 / .5);
}
```

State:

```css
dialog:modal {}
dialog:open {}
```

## Dialog sizing pattern

```css
dialog {
  inline-size: min(90vw, 40rem);
  max-block-size: 80dvh;
  overflow: auto;
}
```

---

# 40. Popover Styling [MUST][MODERN]

Popover:

```html
<div id="menu" popover>...</div>
```

CSS:

```css
[popover] {
  border: 0;
}

[popover]:popover-open {
  opacity: 1;
}
```

Popover được browser xử lý:
- top layer,
- dismiss behavior tùy mode,
- stacking.

2026 còn có hướng mở rộng như `popover="hint"` cho tooltip-like hierarchy.

---

# 41. Entry / Exit Transition cho Top Layer [MODERN]

Vấn đề:

```text
display:none
→ element xuất hiện
```

trước đây khó transition clean.

Modern toolset:

```text
@starting-style
transition-behavior: allow-discrete
overlay
display
```

Concept:

```css
dialog {
  opacity: 1;
  transition:
    opacity .2s,
    display .2s allow-discrete,
    overlay .2s allow-discrete;
}

@starting-style {
  dialog:open {
    opacity: 0;
  }
}
```

Exit/entry exact syntax cần test theo target browsers.

## Senior lesson

Đừng fake dialog transition bằng JS timeout nếu platform đã support lifecycle declaratively.

---

# 42. Customizable `<select>` [2026][MODERN]

Modern CSS cho phép opt-in vào customizable select trong browser support phù hợp.

```css
select,
::picker(select) {
  appearance: base-select;
}
```

Key pieces:

```text
appearance: base-select
::picker(select)
::picker-icon
::checkmark
:open
:checked
```

## Picker

```css
::picker(select) {
  border: 1px solid #ddd;
  border-radius: .75rem;
}
```

Picker hoạt động giống top-layer popover.

## Option

```css
option:checked {
  font-weight: 700;
}
```

## Pattern — Native-first customization

Trước:
- recreate select bằng div + JS + ARIA.

Modern strategy:
1. dùng native `<select>`,
2. customize khi support,
3. fallback native style khi không support.

---

# 43. Feature-detect Custom Select

```css
@supports (appearance: base-select) {
  select,
  ::picker(select) {
    appearance: base-select;
  }
}
```

Design Pattern:

```text
Native semantics
→ progressive visual enhancement
```

Rất đáng ưu tiên hơn custom widget nếu requirements cho phép.

---

# 44. `field-sizing` [MODERN]

Cho form control size theo content trong support phù hợp.

Concept:

```css
textarea {
  field-sizing: content;
}
```

Use cases:
- auto-growing textarea,
- content-sized input.

⚠ Cần constraints:

```css
textarea {
  field-sizing: content;
  min-height: 4lh;
  max-height: 12lh;
}
```

---

# 45. Scroll Container Mental Model [MUST]

Element có overflow có thể trở thành scroll container.

Điều này ảnh hưởng:
- sticky,
- scroll snap,
- scroll-driven animation,
- overscroll,
- scroll padding.

Debug:

```text
Element nào thực sự scroll?
Viewport hay ancestor?
```

---

# 46. `overflow: hidden` vs `clip` [DEEP]

## `hidden`

```css
overflow: hidden;
```

- clip content,
- có scroll container semantics trong nhiều contexts,
- programmatic scrolling có thể liên quan.

## `clip`

```css
overflow: clip;
```

- clip overflow,
- không tạo scroll container giống `hidden`.

Nếu mục tiêu chỉ là clipping:

```css
overflow: clip;
```

có thể semantic hơn.

---

# 47. Overscroll Behavior [ADV]

Properties:

```text
overscroll-behavior
overscroll-behavior-x
overscroll-behavior-y
overscroll-behavior-inline
overscroll-behavior-block
```

Values:

```text
auto
contain
none
```

## Pattern — Modal scroll containment

```css
.modal-body {
  overflow: auto;
  overscroll-behavior: contain;
}
```

Ngăn scroll chain ra page trong nhiều cases.

---

# 48. Scrollbar Gutter [MODERN]

```css
html {
  scrollbar-gutter: stable;
}
```

Mục tiêu:
- reserve scrollbar space,
- giảm layout shift khi scrollbar xuất hiện.

Value hữu ích:

```text
auto
stable
stable both-edges
```

⚠ Overlay scrollbar platforms có behavior khác classic scrollbar platforms.

---

# 49. Scrollbar Styling

Standard properties:

```css
* {
  scrollbar-width: thin;
  scrollbar-color: #888 transparent;
}
```

Browser-specific legacy pseudo-elements như:

```css
::-webkit-scrollbar
```

vẫn thấy trong code cũ nhưng không phải portable standard API.

## Senior rule

Scrollbar styling là enhancement, không được làm scrollbar khó nhìn/khó dùng.

---

# 50. Scroll Anchoring [ADV]

Browser có thể giữ viewport ổn định khi content phía trên thay đổi.

Property:

```css
overflow-anchor
```

Ví dụ opt-out:

```css
.dynamic-region {
  overflow-anchor: none;
}
```

Chỉ dùng khi scroll anchoring tự động gây UX sai.

Đừng disable global.

---

# 51. `scroll-margin` vs `scroll-padding` [MUST]

## `scroll-margin`

Set trên target:

```css
section {
  scroll-margin-top: 5rem;
}
```

Useful khi sticky header che anchor.

## `scroll-padding`

Set trên scroll container:

```css
html {
  scroll-padding-top: 5rem;
}
```

Nói:

> optimal visible scrollport bắt đầu sau 5rem.

---

# 52. `touch-action` [ADV]

```css
.carousel {
  touch-action: pan-y;
}
```

Cho browser biết gestures nào được phép.

Values common:

```text
auto
none
pan-x
pan-y
pinch-zoom
manipulation
```

Cực quan trọng với custom drag/gesture components.

⚠ `touch-action:none` có thể phá native zoom/scroll accessibility.

---

# 53. Environment Variables `env()` [MUST][MODERN]

Khác CSS custom property:

```css
var(--token)
```

`env()` lấy environment variable từ browser/device.

Example:

```css
padding-bottom:
  env(safe-area-inset-bottom);
```

---

# 54. Safe Area Insets [MUST]

Trên devices có notch/home indicator:

```text
safe-area-inset-top
safe-area-inset-right
safe-area-inset-bottom
safe-area-inset-left
```

Pattern:

```css
.bottom-bar {
  padding-bottom:
    max(1rem, env(safe-area-inset-bottom));
}
```

Đảm bảo controls không chạm home indicator.

---

# 55. Foldable / Multi-segment Viewports [ADV]

Environment variables có thể expose:

```text
viewport-segment-width
viewport-segment-height
viewport-segment-top
viewport-segment-right
viewport-segment-bottom
viewport-segment-left
```

Use case:
- foldable device,
- dual-screen layout.

Không cần ưu tiên học sớm, nhưng master CSS phải biết platform có concept này.

---

# 56. Advanced Typography — Font Feature Control [ADV]

## `font-variant-*`

Ưu tiên high-level properties khi có:

```css
font-variant-numeric: tabular-nums;
```

Options thường gặp:

```text
lining-nums
oldstyle-nums
proportional-nums
tabular-nums
diagonal-fractions
slashed-zero
```

Dashboard:

```css
.metric {
  font-variant-numeric: tabular-nums;
}
```

giúp số align đẹp.

---

# 57. `font-feature-settings` [DEEP]

Low-level OpenType controls:

```css
font-feature-settings: "liga" 1, "tnum" 1;
```

Chỉ dùng khi high-level `font-variant-*` không đủ.

## Senior rule

Ưu tiên semantic/high-level property.

Low-level feature tags:
- khó đọc,
- font-dependent,
- dễ làm portability kém.

---

# 58. Variable Fonts [ADV]

Properties:

```text
font-weight
font-stretch
font-style
font-variation-settings
```

Low-level custom axes:

```css
.title {
  font-variation-settings:
    "wght" 650,
    "wdth" 90;
}
```

High-level properties nên được ưu tiên nếu axis standard.

---

# 59. `font-optical-sizing`

```css
body {
  font-optical-sizing: auto;
}
```

Variable fonts có optical size axis có thể tự tối ưu glyph theo rendered font size.

---

# 60. `font-size-adjust`

Giúp fallback font giữ perceived x-height tương đối gần.

Useful giảm visual jump khi custom font load.

Concept:

```css
body {
  font-size-adjust: 0.5;
}
```

Cần calibrate theo font.

---

# 61. East Asian Typography [ADV]

Properties cần biết khi làm Korean/Japanese/Chinese UI:

```text
word-break
line-break
text-emphasis
text-combine-upright
writing-mode
text-orientation
ruby-position
```

## Korean line breaking

```css
:lang(ko) {
  word-break: keep-all;
  overflow-wrap: break-word;
}
```

Cần test content thực tế; không áp blindly cho mọi site.

---

# 62. `text-emphasis` [ADV]

East Asian emphasis marks:

```css
.emphasis {
  text-emphasis: filled dot;
}
```

Có:
- `text-emphasis-style`
- `text-emphasis-color`
- `text-emphasis-position`

---

# 63. Ruby Annotation [ADV]

Ruby markup dùng cho pronunciation/annotation trong East Asian text.

CSS:
- `ruby-position`
- ruby display model.

Không phải daily CSS, nhưng quan trọng cho international publishing.

---

# 64. Wide-Gamut Color [ADV]

Modern displays có thể render ngoài sRGB.

Example:

```css
color: color(display-p3 1 0.2 0.1);
```

Fallback:

```css
.button {
  background: rgb(255 70 60);
  background: color(display-p3 1 .25 .18);
}
```

Unsupported declaration bị bỏ; fallback trước vẫn còn.

---

# 65. `color-gamut` Media Query [ADV]

```css
@media (color-gamut: p3) {
  .hero {
    --brand: color(display-p3 1 .2 .3);
  }
}
```

Values:
- `srgb`
- `p3`
- `rec2020`

Use only when extra gamut thực sự mang giá trị.

---

# 66. Color Interpolation Space [DEEP]

Gradient/color mixing có thể trông khác tùy interpolation color space.

Example:

```css
background:
  linear-gradient(
    in oklab,
    blue,
    red
  );
```

Modern design system nên hiểu:
- sRGB interpolation,
- perceptual spaces như Oklab/Oklch.

---

# 67. `contrast-color()` [2026]

Interop 2026 tập trung function này.

Concept:

```css
.button {
  background: var(--button-bg);
  color: contrast-color(var(--button-bg));
}
```

Mục tiêu:
- chọn contrasting color cho background/foreground.

⚠ Đây là feature hiện đại; browser compatibility phải được check trước production.

## Pattern

Fallback:

```css
.button {
  color: white;
}

@supports (color: contrast-color(black)) {
  .button {
    color: contrast-color(var(--button-bg));
  }
}
```

---

# 68. Typed `attr()` [2026]

Classic:

```css
.badge::after {
  content: attr(data-label);
}
```

Modern typed `attr()` cho phép đọc attribute như typed CSS value.

Concept:

```css
.progress {
  width: attr(data-progress type(<percentage>), 0%);
}
```

Hoặc unit/type syntax theo browser support.

## Use case

```text
HTML data
→ CSS typed value
```

giảm JS glue trong presentation-only cases.

⚠ 2026 là focus interoperability; luôn feature-test.

---

# 69. Advanced CSS Math [ADV]

Ngoài:

```text
calc
min
max
clamp
```

CSS specs/platform hiện đại có thêm nhiều math functions tùy support:

```text
round()
mod()
rem()
abs()
sign()
sin()
cos()
tan()
asin()
acos()
atan()
atan2()
sqrt()
pow()
hypot()
log()
exp()
```

Không cần thuộc mọi function.

Master lesson:

> CSS ngày càng trở thành constraint/math language, không chỉ property list.

Check compatibility trước khi dùng non-core math functions.

---

# 70. `interpolate-size` [MODERN]

Cho phép interpolation tới/from intrinsic size keywords trong support phù hợp.

Concept:

```css
:root {
  interpolate-size: allow-keywords;
}
```

Sau đó transitions có thể animate size tới:

```text
auto
min-content
max-content
fit-content
```

tùy support/spec.

---

# 71. `calc-size()` [EXPERIMENTAL]

Cho calculation với intrinsic size keywords.

Concept:

```css
height: calc-size(auto, size + 2rem);
```

Nó giải quyết case `calc()` thường không làm được với `auto`.

⚠ Limited availability: không dùng critical production UI nếu targets chưa support.

---

# 72. Motion Path [ADV]

Properties:

```text
offset-path
offset-distance
offset-position
offset-anchor
offset-rotate
offset
```

Example:

```css
.dot {
  offset-path:
    path("M 0 0 C 100 0 100 100 200 100");
  animation: move 3s linear infinite;
}

@keyframes move {
  to {
    offset-distance: 100%;
  }
}
```

---

# 73. `shape()` Function [2026]

Modern CSS `shape()` cho basic shapes/path-like commands bằng CSS syntax.

Example concept:

```css
.element {
  clip-path:
    shape(
      from 0 0,
      line to 100% 0,
      line to 50% 100%,
      close
    );
}
```

Có thể dùng với:
- `clip-path`,
- `offset-path`,
- shape-related properties trong support tương ứng.

Ưu điểm so với SVG `path()` syntax:
- CSS units,
- percentages,
- CSS math.

---

# 74. Animation Composition [ADV]

Khi nhiều animations ảnh hưởng cùng property:

```css
animation-composition:
  replace;
```

Values:

```text
replace
add
accumulate
```

## `replace`

Effect mới thay underlying value.

## `add`

Build trên underlying value.

## `accumulate`

Combine theo animation type.

Example:

```css
.icon {
  transform: rotate(10deg);
  animation: pulse 1s infinite;
  animation-composition: add;
}
```

Useful cho composable animation systems.

---

# 75. Multiple Animation Lists [DEEP]

```css
animation:
  fade 200ms ease,
  slide 300ms ease,
  pulse 2s linear infinite;
```

Mỗi animation-* property là comma-separated list.

Nếu list lengths khác nhau, values có thể cycle theo spec rules.

Senior bug source:
- animation-name có 3 values,
- duration có 2 values,
- browser maps/cycles unexpectedly với dev.

---

# 76. Negative Animation Delay [ADV]

```css
animation-delay: -500ms;
```

Animation bắt đầu như thể đã chạy 500ms.

Useful:
- stagger simulations,
- synchronized loaders,
- initial progress.

---

# 77. `steps()` Deep Dive

```css
animation-timing-function:
  steps(5, end);
```

Useful:
- sprite animation,
- frame-by-frame UI.

Variations include jump behavior.

Không dùng `steps()` nếu bạn thực sự cần smooth interpolation.

---

# 78. Named Scroll Timelines [ADV]

Thay vì anonymous:

```css
animation-timeline: scroll();
```

có thể define timeline conceptually:

```css
.scroller {
  scroll-timeline-name: --page-scroll;
  scroll-timeline-axis: block;
}

.progress {
  animation-timeline: --page-scroll;
}
```

Similarly view timelines:
- `view-timeline-name`
- `view-timeline-axis`
- `view-timeline-inset`

Check exact support/current syntax.

---

# 79. `animation-range` [MODERN]

Cho scroll/view timeline biết animation active trong đoạn nào.

```css
.card {
  animation-timeline: view();
  animation-range:
    entry 0%
    cover 40%;
}
```

Senior use:
- reveal animation,
- parallax,
- reading progress.

Accessibility:
- respect reduced motion.

---

# 80. Cross-document View Transitions [2026]

View Transitions không chỉ SPA state.

Modern platform hướng tới cross-document transitions giữa pages cùng origin/eligible navigation.

CSS concepts:
- `view-transition-name`
- transition pseudo-elements
- `@view-transition`
- transition types/state selectors theo support.

⚠ 2026 vẫn là focus interoperability.

---

# 81. View Transition Pseudo-element Tree [DEEP]

Conceptual tree:

```text
::view-transition
└─ ::view-transition-group(name)
   └─ ::view-transition-image-pair(name)
      ├─ ::view-transition-old(name)
      └─ ::view-transition-new(name)
```

Hiểu tree này giúp:
- animate old/new snapshots khác nhau,
- control shared element transition.

---

# 82. Anchor Positioning — Deeper Model [ADV]

V2 giới thiệu anchor positioning.

Master cần biết ecosystem:

```text
anchor-name
position-anchor
anchor()
anchor-size()
position-area
position-try-fallbacks
position-try-order
@position-try
```

Concept:
- reference anchor,
- preferred placement,
- fallback placement khi collision.

Use case:
- tooltip,
- dropdown,
- context menu.

---

# 83. Position Fallback Pattern [MODERN]

Mental pattern:

```text
prefer bottom
→ nếu không đủ space: top
→ nếu vẫn không đủ: side
```

Anchor positioning hướng tới declarative collision fallback thay vì JS đo viewport + set coordinates.

---

# 84. Container Style Queries — Deeper [2026]

Size query:

```css
@container (width > 30rem) {}
```

Style query:

```css
@container style(--density: compact) {}
```

Pattern:

```css
.panel {
  --density: compact;
}

@container style(--density: compact) {
  .row {
    padding-block: .25rem;
  }
}
```

## Design Pattern — Style context

Component behavior có thể phụ thuộc semantic style state của ancestor, không chỉ width.

---

# 85. `@supports selector()` [ADV]

V2 có `@supports` nhưng master cần function query.

```css
@supports selector(:has(*)) {
  .card:has(img) {
    ...
  }
}
```

Dùng để detect selector syntax.

---

# 86. `@supports font-tech()` / `font-format()` [ADV]

Concept:

```css
@supports font-tech(color-COLRv1) {
  ...
}
```

Useful khi:
- color fonts,
- advanced font tech,
- variable font scenarios.

Không cần daily CSS nhưng có giá trị cho design/publishing products.

---

# 87. CSSOM [MUST for frontend senior]

CSS không chỉ là stylesheet text.

JavaScript có **CSS Object Model**.

Common APIs:

```text
document.styleSheets
CSSStyleSheet
CSSRule
CSSStyleRule
CSSMediaRule
CSSSupportsRule
getComputedStyle()
CSS.supports()
```

---

# 88. `getComputedStyle()` [MUST]

```js
const styles =
  getComputedStyle(element);

console.log(styles.width);
console.log(styles.color);
```

Nó expose resolved computed style representation.

## Pitfall

Đừng dùng liên tục trong tight loop sau DOM writes.

Có thể force style/layout synchronization tùy property/context.

Pattern:

```text
batch reads
→ batch writes
```

---

# 89. `CSS.supports()` [ADV]

JS equivalent của feature query:

```js
CSS.supports("display", "grid");
```

Selector:

```js
CSS.supports("selector(:has(*))");
```

Useful khi JS behavior cũng phụ thuộc platform capability.

---

# 90. Stylesheet Manipulation

```js
const sheet =
  document.styleSheets[0];
```

Rules:

```js
sheet.cssRules;
```

Có:
- `insertRule()`
- `deleteRule()`

Use carefully:
- cross-origin stylesheet access restrictions,
- maintainability.

---

# 91. Constructable Stylesheets [ADV]

Concept:

```js
const sheet =
  new CSSStyleSheet();

sheet.replaceSync(`
  :host {
    display: block;
  }
`);

shadowRoot.adoptedStyleSheets = [sheet];
```

Useful:
- Web Components,
- share one stylesheet object giữa nhiều shadow roots.

Pattern:

```text
Create once
→ adopt many
```

---

# 92. CSS Typed OM [ADV]

Traditional:

```js
element.style.width = "10px";
```

Typed OM:

```js
element.attributeStyleMap.set(
  "width",
  CSS.px(10)
);
```

Computed:

```js
element.computedStyleMap();
```

Mục tiêu:
- CSS values như typed JS objects,
- ít string parsing,
- clearer numerical manipulation.

---

# 93. Typed OM Example

```js
const map =
  element.computedStyleMap();

const width =
  map.get("width");

console.log(width.value);
console.log(width.unit);
```

Useful cho:
- editor tools,
- animation systems,
- layout tooling,
- browser-heavy UI frameworks.

Không phải requirement cho mọi frontend app.

---

# 94. Shadow DOM Styling [MUST for Web Components]

Shadow DOM tạo style boundary.

Inside component:

```css
:host {
  display: block;
}
```

Host state:

```css
:host([disabled]) {
  opacity: .5;
}
```

---

# 95. `::slotted()` [ADV]

Style distributed light-DOM children qua `<slot>`.

```css
::slotted(img) {
  border-radius: 50%;
}
```

## Limitation

`::slotted()` target slotted element, không arbitrary deep descendants.

Đừng expect:

```css
::slotted(div span)
```

hoạt động như normal descendant selector.

---

# 96. `::part()` [MUST]

Component expose internal part:

```html
<button part="control">
```

Consumer:

```css
my-button::part(control) {
  border-radius: 999px;
}
```

## Design Pattern — Explicit Styling Surface

Web Component không expose toàn internal DOM.

Nó expose:
- CSS custom properties,
- `::part()` hooks.

Đây là component CSS API.

---

# 97. Custom Properties qua Shadow Boundary

CSS custom properties inherit qua shadow boundary theo normal inheritance model phù hợp.

Host consumer:

```css
my-button {
  --button-bg: rebeccapurple;
}
```

Inside shadow:

```css
button {
  background: var(--button-bg);
}
```

Pattern:

```text
Custom property = theming API
::part = structural styling API
```

---

# 98. SVG + CSS [MUST]

Inline SVG có thể style bằng CSS:

```css
.icon {
  fill: currentColor;
  stroke: none;
}
```

SVG properties:
- `fill`
- `stroke`
- `stroke-width`
- `stroke-linecap`
- `stroke-linejoin`

---

# 99. SVG `currentColor` Pattern

```svg
<svg class="icon" ...>
  ...
</svg>
```

```css
.icon {
  color: var(--icon-color);
  fill: currentColor;
}
```

Icon follow text color/theme automatically.

---

# 100. Inline SVG vs `<img src="icon.svg">`

## Inline SVG

CSS có thể target nội bộ SVG.

## SVG qua `<img>`

Document CSS không style internal SVG DOM như inline tree.

Đây là replaced-resource boundary.

## Senior choice

Inline SVG khi:
- dynamic fill/stroke,
- animation,
- accessible interactive graphic.

Image SVG khi:
- static asset,
- cache/resource simplicity.

---

# 101. SVG `viewBox` và CSS Size

SVG internal coordinate system:

```html
<svg viewBox="0 0 24 24">
```

CSS:

```css
.icon {
  width: 1em;
  height: 1em;
}
```

Pattern icon:

```css
.icon {
  inline-size: 1em;
  block-size: 1em;
  flex: none;
}
```

---

# 102. Mask-based Icon Pattern [ADV]

```css
.icon {
  width: 1em;
  height: 1em;
  background: currentColor;
  mask:
    url("/icons/search.svg")
    center / contain
    no-repeat;
}
```

Useful:
- monochrome icon system,
- color via `currentColor`.

---

# 103. Advanced Masks [ADV]

Properties:

```text
mask-image
mask-mode
mask-repeat
mask-position
mask-size
mask-origin
mask-clip
mask-composite
mask
```

Mask khác clip:
- clip = binary-ish visible region.
- mask = có alpha/luminance gradients.

---

# 104. `clip-path` vs `mask`

## `clip-path`

Good:
- hard geometric boundary.

## `mask`

Good:
- feathered transparency,
- gradient reveal,
- alpha image shapes.

---

# 105. Print CSS [MUST for master]

CSS không chỉ screen.

```css
@media print {
  nav,
  button {
    display: none;
  }
}
```

## Common print adjustments

```css
@media print {
  body {
    color: black;
    background: white;
  }

  a[href]::after {
    content: " (" attr(href) ")";
  }
}
```

Đừng append URL cho internal navigation/buttons blindly.

---

# 106. `@page` [ADV]

Concept:

```css
@page {
  size: A4;
  margin: 20mm;
}
```

Paged media control khác nhau theo browser/print engine.

Use case:
- reports,
- invoices,
- printable documents.

---

# 107. `print-color-adjust` [ADV]

```css
.report-chart {
  print-color-adjust: exact;
}
```

Nói browser cố gắng giữ colors.

⚠ User/browser vẫn có quyền print preferences; không assume tuyệt đối.

---

# 108. Multi-column Advanced [ADV]

```css
.article {
  column-width: 18rem;
  column-gap: 2rem;
}
```

Fragmentation controls:

```css
h2 {
  break-after: avoid;
}

figure {
  break-inside: avoid;
}
```

---

# 109. CSS Counters [ADV]

```css
.chapter {
  counter-reset: section;
}

.chapter h2 {
  counter-increment: section;
}

.chapter h2::before {
  content:
    counter(section)
    ". ";
}
```

Useful:
- legal docs,
- documentation,
- generated numbering.

---

# 110. Nested Counters

```css
ol {
  counter-reset: item;
}

li {
  counter-increment: item;
}

li::marker {
  content:
    counters(item, ".")
    ". ";
}
```

Can generate:

```text
1.
1.1
1.1.1
```

---

# 111. `@counter-style` [ADV]

Custom marker system:

```css
@counter-style thumbs {
  system: cyclic;
  symbols: "👍" "🔥" "⭐";
  suffix: " ";
}
```

Use:

```css
ul {
  list-style: thumbs;
}
```

Niche nhưng useful cho publishing/design systems.

---

# 112. Tables — Deep Layout [ADV]

`table-layout`:

```css
table {
  table-layout: fixed;
}
```

## `auto`

Column width influenced bởi content.

## `fixed`

Column sizing dựa nhiều hơn vào explicit table/column widths và first-row info; layout predictable hơn.

Useful:
- large data table,
- fixed dashboard columns.

---

# 113. Border Collapsing Model [DEEP]

```css
table {
  border-collapse: collapse;
}
```

Adjacent cell borders compete theo border conflict resolution rules.

Đây là lý do:
- border của th/td có lúc không giống simple box stacking.

Nếu muốn fully predictable spacing:

```css
border-collapse: separate;
border-spacing: .5rem;
```

---

# 114. Advanced Grid — Baseline / Masonry Awareness

Grid có baseline alignment và advanced track sizing rất sâu.

Master không cần memorize toàn spec algorithm, nhưng phải biết:

```text
track sizing
intrinsic contributions
spanning items
min/max track sizing
automatic minimums
baseline alignment
```

Khi grid width bất ngờ:
- check `min-content`,
- `minmax(0,1fr)`,
- spanning item contributions.

---

# 115. Subpixel Layout / Pixel Rounding [DEEP]

CSS pixels có thể thành fractional values:

```text
33.333333px
```

Browser cuối cùng map tới device pixels.

3-column grid:

```css
grid-template-columns:
  repeat(3, 1fr);
```

container width không chia hết → track render có thể rounding.

## Senior lesson

Đừng assume:

```text
layout luôn integer px
```

Tránh JS comparison strict với rounded dimensions nếu không cần.

---

# 116. Device Pixel Ratio Mental Model

```text
CSS pixel
≠
physical device pixel
```

High-DPI:

```text
1 CSS px có thể map tới nhiều physical pixels
```

Điều này ảnh hưởng:
- hairline rendering,
- canvas,
- screenshots,
- visual regression tolerance.

---

# 117. CSS `zoom` [2026]

`zoom` scale element và ảnh hưởng layout khác `transform: scale()`.

Concept:

```css
.preview {
  zoom: 0.8;
}
```

## `zoom` vs transform

`transform: scale()`:
- transforms painted result,
- normal layout space thường không co tương ứng.

`zoom`:
- ảnh hưởng layout sizing.

Interop 2026 tiếp tục cải thiện cross-browser behavior.

⚠ Chỉ dùng khi hiểu accessibility/layout consequences.

---

# 118. `forced-color-adjust` [ADV]

High-contrast / forced colors mode:

```css
.logo {
  forced-color-adjust: none;
}
```

`none` nói browser không override colors.

⚠ Dùng rất ít.

Chỉ opt-out khi automatic forced colors thực sự phá meaning, ví dụ:
- brand image,
- color-coded graphic có alternate accessible cue.

---

# 119. Forced Colors Design Pattern

Default:
- để browser adapt.

Sau đó targeted fixes:

```css
@media (forced-colors: active) {
  .control {
    border: 1px solid CanvasText;
  }
}
```

System colors:
- `Canvas`
- `CanvasText`
- `ButtonFace`
- `ButtonText`
- `Highlight`
- `HighlightText`

---

# 120. Browser Compatibility Strategy [MUST]

Master CSS không hỏi:

> "Feature này support không?"

mà hỏi:

```text
Target browsers nào?
Feature là critical hay enhancement?
Fallback tự nhiên có acceptable không?
Có thể feature-detect không?
Baseline status?
Interop risk?
```

---

# 121. Progressive Enhancement Matrix

Ví dụ glass effect:

```css
.card {
  background: rgb(255 255 255 / .95);
}

@supports (backdrop-filter: blur(1rem)) {
  .card {
    background: rgb(255 255 255 / .7);
    backdrop-filter: blur(1rem);
  }
}
```

Nếu feature fail:
- UI vẫn usable.

Đó là progressive enhancement đúng.

---

# 122. Graceful Degradation vs Progressive Enhancement

## Progressive enhancement

Start simple:
```text
usable base
→ add advanced behavior
```

## Graceful degradation

Start advanced:
```text
advanced app
→ ensure acceptable fallback
```

CSS modern thường rất phù hợp progressive enhancement vì unsupported declaration/rule có thể bị ignore.

---

# 123. Browser Support Tiers

Có thể định nghĩa trong project:

```text
Tier A
latest evergreen browsers

Tier B
older supported enterprise browsers

Tier C
unsupported but readable fallback
```

Sau đó feature policy rõ:

```text
Anchor positioning:
Tier A enhancement

Dialog:
required

View transition:
optional
```

---

# 124. Baseline Strategy [2026]

Khi research modern CSS:
- xem MDN Baseline status,
- xem Web Platform Status,
- xem project browser matrix.

Không sử dụng feature chỉ vì:
```text
Chrome của dev chạy được
```

---

# 125. CSS Testing Pyramid [MUST]

## Level 1 — Static checks

- stylelint,
- syntax,
- naming,
- banned patterns.

## Level 2 — Component tests

Check states:
- default,
- hover,
- focus,
- disabled,
- loading,
- long text,
- RTL.

## Level 3 — Visual regression

Screenshot compare.

## Level 4 — Cross-browser / device

- Chromium,
- Firefox,
- Safari,
- mobile.

## Level 5 — Accessibility

- keyboard,
- zoom,
- forced colors,
- reduced motion.

---

# 126. Visual Regression Testing [MUST]

CSS bugs thường không throw exception.

Visual regression catches:
- 2px shifts,
- wrapping,
- missing border,
- color token regression,
- responsive break.

Typical tools/ecosystems:
- Playwright screenshots,
- Storybook visual workflows,
- hosted diff services.

Pattern:

```text
component states
× viewport widths
× themes
```

---

# 127. CSS Test Fixture Design

Một component test page nên có:

```text
short text
long text
very long unbreakable string
0 items
1 item
many items
large image
missing image
loading
error
RTL
200% zoom-like constraints
```

Senior không chỉ test happy path.

---

# 128. Stylelint Strategy [MUST]

Useful rule categories:

```text
invalid syntax
duplicate properties
unknown properties
selector complexity
specificity limits
!important restrictions
naming convention
property ordering
browser compatibility plugin if needed
```

Đừng bật 100 rules chỉ để CI đỏ.

Rules phải enforce architecture.

---

# 129. Specificity Budget [ADV]

Có thể enforce guideline:

```text
No IDs in component CSS
Max 2 classes per selector
Max nesting depth 2–3
No !important except designated layer
```

Không cần exactly như trên.

Quan trọng là **team contract measurable**.

---

# 130. Dead CSS / Unused CSS [MUST]

Sources:
- old components,
- dynamic class generation,
- abandoned experiments,
- third-party styles.

Strategies:
- component-scoped CSS,
- CSS Modules,
- build analysis,
- coverage,
- utility tree shaking,
- delete styles with code.

⚠ Automatic unused CSS tools có thể miss dynamic runtime selectors.

---

# 131. CSS Coverage in DevTools [ADV]

Browser DevTools Coverage có thể cho thấy stylesheet bytes unused trong scenario đang chạy.

Không đồng nghĩa:
```text
unused = safe delete
```

Vì state/page khác có thể dùng.

Use as investigation signal.

---

# 132. Critical CSS [ADV]

Above-the-fold CSS có thể inline/extract để giảm render blocking.

Nhưng modern apps cần balance:
- caching,
- complexity,
- hydration,
- duplicate CSS.

Không automatically inline toàn CSS.

---

# 133. Style Recalculation Cost [DEEP]

Browser có thể cần recompute styles khi:
- class changes,
- DOM changes,
- state changes,
- inherited custom property changes.

High-level concern:
- huge DOM,
- broad invalidations,
- frequent mutations.

Đừng micro-optimize `.class` vs `div.class` trước khi profile.

---

# 134. Layout Thrashing [MUST]

Pattern xấu JS:

```js
element.style.width = "100px";
const width = element.offsetWidth;

element.style.width = "200px";
const width2 = element.offsetWidth;
```

Read-after-write có thể force synchronous layout.

Better:

```text
batch reads
→ compute
→ batch writes
```

CSS performance không thể tách rời JS layout behavior.

---

# 135. Containment Strategy [ADV]

`contain` là performance + architecture tool.

Possible:
- `layout`
- `paint`
- `size`
- `inline-size`
- `style`

Dùng khi component:
- tương đối independent,
- có known sizing strategy.

⚠ `size` containment có thể làm intrinsic sizing biến mất.

---

# 136. `content-visibility` Deep Usage [ADV]

```css
.section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px;
}
```

Good:
- long document,
- large off-screen sections.

Bad:
- tiny list items,
- content requiring immediate measurement,
- cases khiến focus/search UX bất ngờ nếu implementation/browser constraints.

Profile before/after.

---

# 137. Paint Cost [ADV]

Expensive visual effects có thể gồm:
- huge blur,
- backdrop-filter,
- giant box-shadow,
- large fixed backgrounds,
- complex masks,
- frequently animating filters.

Không có universal rule.

DevTools Performance/Paint flashing mới là source of truth.

---

# 138. Layer Promotion Myth

Không phải cứ:

```css
transform: translateZ(0);
```

là "tối ưu".

Unnecessary compositing:
- tốn GPU memory,
- tạo layers dư,
- có thể blur text/produce artifacts.

`will-change` cũng tương tự:
- hint,
- không phải magic speed switch.

---

# 139. Component CSS Contract [MASTER]

Một reusable component nên xác định:

```text
DOM contract
styling hooks
tokens
variants
states
slots
responsive owner
focus behavior
overflow behavior
motion policy
browser fallback
```

Ví dụ Button API:

```text
data-variant
data-size
disabled
aria-pressed
--button-bg
--button-fg
--button-radius
```

Internal implementation không nên bị consumer phụ thuộc.

---

# 140. Public vs Private CSS API

## Public

```text
documented class
data variant
ARIA state
custom property
::part
```

## Private

```text
internal wrapper classes
DOM depth
anonymous child order
temporary utility
```

Senior review:
> Consumer có đang override private implementation không?

---

# 141. Override Hooks Pattern

Bad:

```css
.app .third-party-widget
  > div:nth-child(2)
  > span {
  ...
}
```

Better nếu component controlled:

```css
.widget {
  --widget-accent: var(--brand);
}
```

Hoặc Web Component:

```css
widget-x::part(title) {}
```

---

# 142. CSS Architecture for Micro-frontends [ADV]

Problem:
- nhiều teams,
- nhiều frameworks,
- global CSS collision.

Strategies:
- cascade layers,
- namespace/root scope,
- CSS Modules,
- Shadow DOM,
- token contract,
- no global resets inside child app.

Example:

```css
@scope (#payments-app) {
  ...
}
```

Hoặc root namespace:

```css
.payments-app .button {}
```

depending platform/support.

---

# 143. Third-party CSS Containment Pattern

Import vendor vào low-priority layer:

```css
@layer vendor, app;

@import url("vendor.css")
  layer(vendor);
```

App:

```css
@layer app {
  ...
}
```

Giảm specificity fighting.

---

# 144. Legacy CSS Migration Pattern

Khi codebase có:

```text
IDs
!important
nested selectors
global element overrides
```

Không rewrite toàn bộ một lần.

Migration:

```text
1. establish layer order
2. put legacy into layer
3. write new components low-specificity
4. expose tokens
5. gradually remove old overrides
```

---

# 145. CSS Refactor Safety

Trước refactor:
- screenshot states,
- capture major routes,
- record computed styles for sensitive components.

Sau refactor:
- visual diff,
- keyboard test,
- responsive test.

CSS refactor không có compiler bảo vệ semantics.

---

# 146. Modern Native UI Strategy [MASTER]

Trước đây frontend thường recreate:
- dialog,
- dropdown,
- tooltip,
- select.

2026 platform có:
- `<dialog>`,
- Popover API,
- anchor positioning,
- customizable select,
- `:open`,
- top layer,
- `@starting-style`.

Senior decision:

```text
Use platform primitive
→ style/enhance
→ custom JS only for missing behavior
```

---

# 147. Modern CSS vs JavaScript Boundary

Use CSS khi problem là:

```text
layout
presentation
responsive adaptation
visual state
animation
style condition
```

Use JS khi problem là:

```text
business state
data
network
complex measurement unavailable declaratively
focus management logic
application workflow
```

Modern CSS đang kéo boundary xa hơn với:
- `:has()`
- container queries
- anchor positioning
- typed `attr()`
- scroll timelines.

---

# 148. Common “Master-Level” Debug Questions

Khi bug khó, hỏi:

```text
1. Declaration đang ở origin/layer nào?
2. Computed value thực tế là gì?
3. Value có invalid ở computed-value time không?
4. Element tạo box nào?
5. Formatting context nào đang active?
6. Containing block là ai?
7. Size definite hay indefinite?
8. Intrinsic contribution là bao nhiêu?
9. Item có automatic minimum không?
10. Element là replaced element không?
11. Scroll container thật sự là ai?
12. Stacking context nào chứa nó?
13. Nó có đang ở top layer không?
14. Writing mode / direction là gì?
15. Fragmentation context có tồn tại không?
16. Browser có support syntax/value này không?
17. User preference có override expectation không?
18. Có forced colors/reduced motion không?
19. JS có đang force layout không?
20. Bug có chỉ xuất hiện do rounding/subpixel không?
```

---

# 149. Master CSS Practical Lab — 25 bài nâng cao

## Lab 1 — Cascade origins

Tạo cùng property từ:
- inline,
- stylesheet,
- animation,
- transition,
- `!important`.

Quan sát DevTools winner.

## Lab 2 — Layer inversion

Test normal + important across 3 layers.

## Lab 3 — Scope proximity

Tạo nested scopes và equal specificity.

## Lab 4 — Computed value

So sánh:
- source declaration,
- computed style,
- used pixel size.

## Lab 5 — Replaced image

Test:
- intrinsic image,
- width only,
- height only,
- aspect-ratio,
- object-fit.

## Lab 6 — Flex automatic minimum

Long unbreakable content:
- trước `min-width:0`,
- sau `min-width:0`.

## Lab 7 — Grid intrinsic track

Compare:
```css
1fr
```

với:

```css
minmax(0,1fr)
```

## Lab 8 — Inline baseline

Align icon + text:
- center,
- baseline,
- vertical-align.

## Lab 9 — BFC

Float image + text:
- normal block,
- `flow-root`.

## Lab 10 — Fragmentation

3-column article:
- `break-inside`,
- heading breaks.

## Lab 11 — Top layer

Compare:
- div modal z-index,
- native dialog.

## Lab 12 — Popover

Build menu dùng Popover API + `:popover-open`.

## Lab 13 — Entry transition

Use:
- `@starting-style`,
- discrete transition.

## Lab 14 — Custom select

Progressively enhance native select với `base-select`.

## Lab 15 — Scroll chaining

Nested scroller + `overscroll-behavior`.

## Lab 16 — Safe area

Build fixed mobile bottom nav dùng `env()`.

## Lab 17 — Variable font

Animate/change standard font axis.

## Lab 18 — Display P3 color

Create fallback + wide-gamut enhancement.

## Lab 19 — Custom Highlight

Search match without adding `<mark>` nodes.

## Lab 20 — Motion path

Animate element along `offset-path`.

## Lab 21 — Additive animation

Use `animation-composition:add`.

## Lab 22 — Shadow DOM

Expose:
- custom property,
- `::part`,
- slotted content.

## Lab 23 — CSSOM

Read computed values + construct stylesheet.

## Lab 24 — Print

Create printable report:
- A4,
- page margins,
- avoid split cards.

## Lab 25 — Visual regression

Capture component matrix:
- light/dark,
- 320/768/1440,
- long text,
- focus,
- RTL.

---

# 150. Master CSS Interview / Self-test Questions

Bạn nên trả lời được không nhìn tài liệu:

1. Declared, cascaded, specified, computed, used, actual value khác gì?
2. Khi nào custom property gây invalid at computed-value time?
3. Origin precedence khác specificity như thế nào?
4. Tại sao `!important` đảo cascade layer order?
5. `@scope` proximity được xét khi nào?
6. DOM tree và box tree khác nhau ở đâu?
7. Anonymous box là gì?
8. BFC là gì? `flow-root` giải quyết gì?
9. Inline formatting context hoạt động theo line box thế nào?
10. `vertical-align` thực sự áp dụng cho gì?
11. Replaced element là gì?
12. Intrinsic dimension/ratio khác CSS aspect-ratio thế nào?
13. Definite size ảnh hưởng percentage height thế nào?
14. `min-content`, `max-content`, `fit-content` khác nhau thế nào?
15. Shrink-to-fit xuất hiện trong những layout nào?
16. Vì sao `min-width:0` fix flex overflow?
17. Vì sao `%` không thể học như một unit universal?
18. Float ngày nay còn use case gì?
19. Fragmentation là gì?
20. `:nth-child(2n of .x)` khác `.x:nth-child(2n)`?
21. `:user-invalid` hơn `:invalid` ở UX nào?
22. `:open`, `:popover-open`, `:modal` khác nhau?
23. Top layer khác z-index thế nào?
24. `@starting-style` giải quyết problem nào?
25. `appearance:base-select` là gì?
26. Scroll container ảnh hưởng sticky thế nào?
27. `overflow:hidden` và `overflow:clip` khác nhau gì?
28. `overscroll-behavior` dùng khi nào?
29. `scrollbar-gutter` giải quyết problem gì?
30. `env(safe-area-inset-bottom)` dùng làm gì?
31. `font-variant-numeric:tabular-nums` hữu ích khi nào?
32. Wide gamut P3 khác sRGB?
33. `contrast-color()` giải quyết gì?
34. Typed `attr()` mở ra use case nào?
35. `interpolate-size` và `calc-size()` là gì?
36. Motion Path gồm property nào?
37. `animation-composition` values là gì?
38. View Transition pseudo-element tree hoạt động conceptually thế nào?
39. Anchor positioning fallback giải quyết collision ra sao?
40. Container style query khác size query?
41. `@supports selector()` dùng khi nào?
42. CSSOM là gì?
43. Typed OM khác `element.style` string API?
44. Constructable Stylesheet là gì?
45. `:host`, `::slotted`, `::part` khác nhau?
46. CSS custom property qua Shadow DOM dùng như API thế nào?
47. Inline SVG khác SVG `<img>` khi styling?
48. `mask` khác `clip-path`?
49. `@page` dùng khi nào?
50. `break-inside` ảnh hưởng print/multicol ra sao?
51. CSS counter dùng cho case gì?
52. `zoom` khác `transform:scale()`?
53. forced colors nên xử lý thế nào?
54. Progressive enhancement khác graceful degradation?
55. Visual regression test CSS ra sao?
56. Specificity budget là gì?
57. Dead CSS detect sao mà không xoá nhầm dynamic classes?
58. Layout thrashing liên quan CSS ra sao?
59. `contain:size` có side effect gì?
60. Public CSS API của component nên gồm gì?

Nếu trả lời chắc khoảng **50+/60 câu** và làm được 20+/25 labs mà không copy solution, nền CSS của bạn đã ở mức rất cao.

---

# 151. Mastery Rubric

## Level 1 — Syntax User

Biết:
- property,
- selector,
- Flex/Grid.

## Level 2 — UI Developer

Biết:
- responsive,
- component,
- forms,
- animation.

## Level 3 — Senior CSS

Biết:
- cascade,
- intrinsic sizing,
- stacking,
- architecture,
- accessibility,
- performance.

## Level 4 — CSS Specialist

Biết:
- formatting model,
- line boxes,
- replaced elements,
- top layer,
- advanced sizing,
- browser APIs,
- Shadow DOM.

## Level 5 — CSS Master

Có thể:
- đọc specification khi docs không đủ,
- explain browser layout behavior,
- design CSS architecture cho multi-team system,
- debug cross-browser edge case,
- chọn progressive enhancement strategy,
- build component CSS APIs,
- profile rendering,
- review platform changes mà không chạy theo trend.

---

# 152. Những thứ KHÔNG cần học thuộc để master CSS

Không cần memorize:

```text
mọi property hiếm
mọi formal grammar
mọi vendor pseudo-element
mọi browser quirk lịch sử
mọi CSS Working Draft
```

Cần biết:
- concept tồn tại,
- khi nào cần lookup,
- tài liệu chuẩn ở đâu,
- cách đọc syntax/formal definition.

---

# 153. Cách đọc MDN property page như senior

Khi lookup property, đừng chỉ đọc example.

Check:

```text
Initial value
Applies to
Inherited?
Percentage basis
Computed value
Animation type
Creates stacking context?
Formal syntax
Browser compatibility
Specifications
```

Ví dụ `offset-path`:
- applies to transformable elements,
- creates stacking context,
- animation type theo computed type.

Các metadata này giải thích nhiều edge cases.

---

# 154. Cách đọc CSS Specification

Không cần đọc spec từ đầu đến cuối.

Workflow:

```text
1. MDN để hiểu overview.
2. Reproduce bug nhỏ.
3. DevTools computed styles.
4. Search spec section đúng concept.
5. Đọc definitions / algorithm / notes.
6. Check browser bug trackers nếu behavior lệch.
```

---

# 155. Source-of-truth hierarchy

Khi tài liệu mâu thuẫn:

```text
1. Current CSS specification / WHATWG integration specs
2. Web Platform Tests / implementation reality
3. MDN
4. web.dev / browser vendor docs
5. high-quality articles
6. StackOverflow/blog posts
```

Không copy old CSS hacks từ article 2015 nếu không hiểu vì sao.

---

# 156. 2026 Modern CSS Watchlist

Các feature đáng theo dõi trong 2026:

```text
Anchor positioning interoperability
Container style queries
Dialog / Popover improvements
:open
popover="hint"
Scroll-driven animations
Cross-document View Transitions
:active-view-transition-type()
Typed attr()
contrast-color()
Custom Highlight API
Media state pseudo-classes
shape()
zoom interoperability
Customizable select
Intrinsic-size interpolation
```

Không đồng nghĩa tất cả đều nên dùng ngay production.

Rule:

```text
Baseline / project support
→ progressive enhancement
→ fallback
```

---

# 157. CSS + SCSS Boundary

Sau supplement này, SCSS không giúp bạn hiểu browser thêm.

SCSS giải quyết **authoring/build-time abstraction**:

```text
modules
mixins
functions
loops
maps
generation
compile-time variables
```

CSS giải quyết **runtime styling model**:

```text
cascade
inheritance
layout
browser state
custom properties
media/container queries
animation
```

Senior phải phân biệt:

```text
SCSS abstraction problem
vs
CSS runtime problem
```

Không dùng mixin để che việc chưa hiểu Flex/Grid/cascade.

---

# 158. Final CSS Knowledge Map

```text
CSS MASTER
│
├─ LANGUAGE
│  ├─ syntax
│  ├─ selectors
│  ├─ cascade
│  ├─ values
│  └─ functions
│
├─ FORMATTING MODEL
│  ├─ box tree
│  ├─ BFC / IFC
│  ├─ line boxes
│  ├─ replaced elements
│  └─ fragmentation
│
├─ SIZING
│  ├─ definite / indefinite
│  ├─ intrinsic
│  ├─ min/max-content
│  ├─ fit-content
│  └─ automatic minimum
│
├─ LAYOUT
│  ├─ normal flow
│  ├─ position
│  ├─ float
│  ├─ flex
│  ├─ grid
│  ├─ table
│  └─ multicol
│
├─ RENDERING
│  ├─ paint
│  ├─ stacking
│  ├─ top layer
│  ├─ clipping
│  ├─ masks
│  └─ compositing
│
├─ RESPONSIVE
│  ├─ media
│  ├─ container
│  ├─ env()
│  ├─ writing modes
│  └─ user preferences
│
├─ MOTION
│  ├─ transition
│  ├─ keyframes
│  ├─ additive composition
│  ├─ motion paths
│  ├─ scroll timelines
│  └─ view transitions
│
├─ COMPONENT PLATFORM
│  ├─ dialog
│  ├─ popover
│  ├─ customizable controls
│  ├─ Shadow DOM
│  └─ CSS APIs
│
├─ ARCHITECTURE
│  ├─ layers
│  ├─ scope
│  ├─ tokens
│  ├─ component API
│  └─ override contract
│
└─ ENGINEERING
   ├─ accessibility
   ├─ performance
   ├─ compatibility
   ├─ linting
   ├─ testing
   └─ visual regression
```

---

# 159. Đánh giá cuối cùng

Sau khi học:

1. `CSS_Beginner_to_Senior_2026_v2.md`
2. `CSS_Master_Supplement_2026.md`

thì phần kiến thức lý thuyết đã **gần đầy đủ cho CSS từ beginner → senior → specialist/master**.

Nhưng “master” không thể chỉ đạt bằng đọc.

Phải có vòng:

```text
Read
→ Implement
→ Break
→ Debug
→ Inspect browser
→ Compare browsers
→ Refactor
→ Review
```

Mốc thực tế:

```text
V2
→ đủ để làm senior production CSS

V2 + Supplement
→ đủ knowledge map để hướng tới CSS specialist/master

V2 + Supplement + 20–30 advanced labs + project thật
→ mastery thực tế
```

---

# 160. Tài liệu chuẩn để tiếp tục tra cứu

## MDN

- CSS Reference  
  https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

- CSS Guides  
  https://developer.mozilla.org/en-US/docs/Web/CSS/Guides

- CSS Cascade  
  https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade

- CSS Custom Highlight API  
  https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_Highlight_API

- CSS Typed OM  
  https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API

- Customizable Select  
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select

## web.dev

- Learn CSS  
  https://web.dev/learn/css/

- Interop 2026  
  https://web.dev/blog/interop-2026/

## Specifications / Compatibility

- W3C CSS  
  https://www.w3.org/Style/CSS/

- Web Platform Tests  
  https://wpt.fyi/

- Web Platform Status  
  https://webstatus.dev/

- Can I Use  
  https://caniuse.com/

---

# Kết luận ngắn

Nếu chỉ đọc V2:

```text
Beginner → Senior: YES
Master CSS: chưa hoàn toàn
```

Nếu học thêm file supplement này:

```text
Language
+ Browser model
+ Advanced layout
+ Modern platform
+ CSS APIs
+ Architecture
+ Testing
+ Compatibility
```

thì **knowledge coverage đã đủ rộng để gọi là roadmap master CSS**.

Phần còn lại không phải thêm property nữa.

Phần còn lại là:

```text
practice
browser bugs
cross-browser behavior
large-codebase experience
spec reading
```
