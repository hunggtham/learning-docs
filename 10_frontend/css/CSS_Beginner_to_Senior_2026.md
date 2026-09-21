# CSS — Beginner → Senior Handbook (2026)

> Mục tiêu: đây không phải là danh sách thuộc tính (property) để học thuộc. Tài liệu được tổ chức theo **mô hình tư duy (mental model) của browser**, sau đó mới đến thuộc tính (property), layout, responsive, kiến trúc (architecture) và CSS hiện đại.  
> Nếu đọc + tự code lại toàn bộ ví dụ + làm các bài tập cuối mỗi phần, bạn sẽ có nền tảng CSS đủ để làm production frontend ở mức senior.
>
> Ký hiệu:
> - **[CORE]**: phải biết và dùng thường xuyên.
> - **[ADV]**: kiến thức nâng cao, senior cần hiểu bản chất.
> - **[MODERN]**: CSS hiện đại, nên dùng khi mức hỗ trợ trình duyệt (browser support) của project cho phép.
> - **⚠ Pitfall**: lỗi thường gặp.
> - **Senior note**: cách suy nghĩ/thiết kế CSS trong project thật.

---

## Quy ước thuật ngữ Việt–Anh

Trong tài liệu này, thuật ngữ chuyên môn được ưu tiên diễn đạt bằng tiếng Việt tự nhiên và giữ thuật ngữ gốc bên cạnh để dễ đối chiếu. Ví dụ: **cơ chế phân tầng (cascade)**, **độ đặc hiệu (specificity)**, **kế thừa (inheritance)**, **mô hình hộp (box model)**, **luồng bố cục thông thường (normal flow)**, **ngữ cảnh định dạng (formatting context)**, **khối chứa tham chiếu (containing block)**, **định cỡ nội tại (intrinsic sizing)** và **ngữ cảnh xếp chồng (stacking context)**. Tên property, value, selector, at-rule và API khi xuất hiện dưới dạng mã vẫn được giữ nguyên để không làm sai cú pháp.



# Cách đọc tài liệu canonical

Mỗi nhóm kiến thức quan trọng được đọc theo 4 tầng tư duy:

```text
Property / Syntax
→ Language Idiom
→ Coding / Programming Pattern
→ Design / Architecture Pattern
```

## 1. thuộc tính (property) / Syntax

Đây là tầng thấp nhất: thuộc tính (property) làm gì, nhận giá trị (value) nào, computed behavior ra sao.

Ví dụ:

```css
display: flex;
gap: 1rem;
```

## 2. CSS lối viết quen dùng của ngôn ngữ (language idiom)

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

## 4. CSS Design / kiến trúc (architecture) Pattern

Không nên hiểu "mẫu thiết kế (design pattern) trong CSS" theo nghĩa GoF của Java.

Trong CSS, mẫu thiết kế (design pattern) thường là:
- cách tổ chức cơ chế phân tầng (cascade),
- cách định nghĩa hợp đồng thành phần (component contract),
- cách thiết kế token,
- cách quản lý các biến thể (variants)/các trạng thái (states),
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

Mục tiêu là học được **cách senior ghép các thuộc tính (property) thành hệ thống**, không chỉ nhớ tên thuộc tính (property).

---

# 0. Bản đồ học CSS

# 0A. mô hình tư duy (mental model) xuyên suốt: từ khai báo (declaration) tới pixel trên màn hình

CSS dễ bị học thành một danh sách thuộc tính (property) rời rạc, nhưng browser không xử lý CSS theo cách đó. Khi HTML và stylesheet được load, browser trước tiên phải xác định bộ chọn (selector) nào match element. Sau đó cơ chế phân tầng (cascade) chọn khai báo (declaration) thắng cho từng thuộc tính (property). Chỉ sau khi cơ chế phân tầng (cascade)/defaulting hoàn tất, kế thừa (inheritance) mới cung cấp giá trị (value) cho những thuộc tính (property) có cơ chế thừa hưởng. Browser tiếp tục tạo box, xác định luồng bố cục thông thường (normal flow) và ngữ cảnh định dạng (formatting context), resolve khối chứa tham chiếu (containing block), intrinsic/available size và positioning, chạy thuật toán bố cục (layout algorithm) như Flexbox/Grid, rồi mới paint và composite.

Trục học canonical của CSS vì vậy là:

```text
selector matching
→ cascade
→ specificity / scope proximity / source order
→ inheritance + initial/defaulting
→ box model + sizing
→ normal flow
→ formatting context
→ positioning + containing block
→ Flexbox / Grid / other layout algorithms
→ responsive conditions
→ paint / composite / performance
```

Khi CSS “không chạy”, hãy truy theo đúng trục này thay vì đổi thuộc tính (property) ngẫu nhiên. Ví dụ `.card { width: 100% }` có thể không cho kết quả mong muốn vì bộ chọn (selector) không match, rule ở layer khác thắng, percentage resolve theo khối chứa tham chiếu (containing block) khác, phần tử Flex (flex item) bị kích thước tối thiểu tự động (automatic minimum size) chặn co, hoặc parent tạo overflow/ngữ cảnh định dạng (formatting context) khác với assumption. Thêm `!important` chỉ giải quyết một nhánh rất nhỏ của cây nguyên nhân.

## cơ chế phân tầng (cascade) trước, độ đặc hiệu (specificity) sau

độ đặc hiệu (specificity) không phải luật đầu tiên của CSS. cơ chế phân tầng (cascade) trước tiên xét relevance, nguồn và mức quan trọng (origin/importance) và lớp phân tầng (cascade layer). độ đặc hiệu (specificity) chỉ được so giữa những khai báo (declaration) vẫn còn cạnh tranh trong cùng context precedence. Nếu độ đặc hiệu (specificity) bằng nhau, `@scope` có thể đưa scoping proximity vào quyết định; thứ tự nguồn (source order) là tie-breaker cuối. Vì thế kiến trúc (architecture) với `@layer`, bộ chọn (selector) nhẹ và component boundary thường bền hơn cuộc chiến độ đặc hiệu (specificity war).

## kế thừa (inheritance) không phải “độ đặc hiệu (specificity) của parent truyền xuống con”

Một `color` trên parent thường truyền xuống child vì `color` là inherited thuộc tính (property); `padding` thì không. Nếu child có rule trực tiếp target nó, direct giá trị (value) thắng inherited giá trị (value) bất kể bộ chọn (selector) của parent mạnh đến đâu. Khi gỡ lỗi (debug) typography, custom thuộc tính (property) hoặc theme, hãy luôn phân biệt khai báo (declaration) thắng trên chính element với giá trị (value) inherited từ ancestor.

## mô hình hộp (box model) phải được đặt trong ngữ cảnh định dạng (formatting context)

`content`, `padding`, `border`, `margin` chỉ mô tả box. Cách box được đặt phụ thuộc ngữ cảnh định dạng (formatting context). ngữ cảnh định dạng khối (block formatting context) có rules về block flow, floats và margin interaction; ngữ cảnh định dạng nội dòng (inline formatting context) tạo các hộp dòng (line boxes) và đường cơ sở (baseline); Flexbox/Grid chạy sizing/placement algorithm riêng. Đây là lý do cùng `width`, `margin:auto` hay alignment thuộc tính (property) có thể hành xử khác ở các context khác nhau.

## luồng bố cục thông thường (normal flow) là đường cơ sở (baseline) của positioning

Trước `absolute`, `fixed`, `sticky`, cần hiểu luồng bố cục thông thường (normal flow). `position: relative` vẫn giữ slot trong flow rồi offset visual box. `absolute` rời luồng bố cục thông thường (normal flow) và tìm khối chứa tham chiếu (containing block). `fixed` thường liên hệ vùng nhìn (viewport)/top-level containing context. `sticky` vẫn tham gia flow nhưng bị ràng buộc bởi vùng chứa cuộn (scroll container), inset và scroll range. Khi positioning sai, câu hỏi đúng là “khối chứa tham chiếu (containing block)/vùng chứa cuộn (scroll container) là ai?” trước khi hỏi “top bao nhiêu px?”.

## Responsive chỉ đổi điều kiện; bộ máy bố cục (layout engine) vẫn là CSS layout

truy vấn môi trường (media query) bật/tắt các khai báo (declarations) theo vùng nhìn (viewport), input capability, motion preference hoặc color scheme. truy vấn vùng chứa (container query) làm điều tương tự nhưng query container thay vì vùng nhìn (viewport). Bên trong điều kiện đó, layout vẫn do luồng bố cục thông thường (normal flow), Flexbox, Grid và sizing algorithms thực thi. Responsive tốt thường bắt đầu bằng fluid/intrinsic constraints, rồi điểm ngắt (breakpoint) chỉ xuất hiện ở nơi behavior thực sự cần đổi.

## Rendering/hiệu năng (performance) là phần cuối của cùng mô hình tư duy (mental model)

Sau layout, browser paint text, background, border, shadow/effects rồi composite. Thay đổi geometry như `width` hoặc font metrics có thể kéo theo style/layout/paint; `transform` và `opacity` thường thuận lợi hơn cho compositor animation nhưng không miễn phí. Blur/backdrop-filter lớn, quá nhiều các lớp tổng hợp (compositing layers) hoặc `will-change` bừa bãi có thể tăng memory/render cost. hiệu năng (performance) phải được đo theo chuỗi xử lý kết xuất (rendering pipeline), không tối ưu bằng mẹo truyền miệng.

Khi gỡ lỗi (debug) production, trace chuẩn là: bộ chọn (selector) match → khai báo (declaration) valid → cơ chế phân tầng (cascade)/layer/độ đặc hiệu (specificity) → computed giá trị (value) → kế thừa (inheritance)/defaulting → ngữ cảnh định dạng (formatting context)/khối chứa tham chiếu (containing block) → intrinsic/min/max/overflow → stacking/paint/composite. Đây là xương sống nối mọi chapter còn lại.


## Thứ tự ưu tiên

1. **Syntax → bộ chọn (selector) → cơ chế phân tầng (cascade) → độ đặc hiệu (specificity) → kế thừa (inheritance)**
2. **mô hình hộp (box model) → Sizing → luồng bố cục thông thường (normal flow) → Display**
3. **Position → khối chứa tham chiếu (containing block) → ngữ cảnh xếp chồng (stacking context) → z-index**
4. **Typography → Color → Background → Border**
5. **Flexbox**
6. **Grid**
7. **thiết kế đáp ứng (responsive design) → truy vấn môi trường (media query) → truy vấn vùng chứa (container query)**
8. **Transform → Transition → Animation**
9. **Custom các thuộc tính (properties) → token thiết kế (design tokens)**
10. **kiến trúc (architecture) → khả năng tiếp cận (accessibility) → hiệu năng (performance) → gỡ lỗi (debugging)**
11. **CSS hiện đại:** lồng cú pháp (nesting), các lớp phân tầng (cascade layers), `@scope`, `:has()`, Subgrid, định vị theo điểm neo (anchor positioning), hoạt ảnh điều khiển bằng cuộn (scroll-driven animations), chuyển cảnh giao diện (view transitions), `@property`, modern color.

## mô hình tư duy (mental model) quan trọng nhất

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

Đây là khác biệt lớn giữa người "biết CSS" và người gỡ lỗi (debug) CSS nhanh.

---

# 1. CSS Syntax & cách browser áp dụng CSS [CORE]

## 1.1 Rule cơ bản

```css
.card {
  color: #222;
  padding: 16px;
}
```

- `.card`: bộ chọn (selector).
- `color`, `padding`: thuộc tính (property).
- `#222`, `16px`: giá trị (value).
- `color: #222`: khai báo (declaration).
- Toàn bộ `{ ... }`: khai báo (declaration) block.

Nếu một khai báo (declaration) sai, browser thường bỏ khai báo (declaration) đó:

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

Inline style có độ đặc hiệu (specificity) cao và khó maintain. Chỉ nên dùng khi:
- style được generate động thực sự,
- email HTML,
- framework/thời gian chạy (runtime) buộc phải dùng.

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

# 2. các bộ chọn (selectors) [CORE]

## Pattern notes — các bộ chọn (selectors)

### CSS Idiom — trạng thái (state) bằng attribute thay vì class tạm

```css
.tabs [aria-selected="true"] {
  font-weight: 700;
}

.menu[data-state="open"] {
  opacity: 1;
}
```

Ưu điểm:
- trạng thái (state) gần với ngữ nghĩa (semantics) hơn,
- JS không cần maintain thêm nhiều class,
- DevTools đọc trạng thái (state) rõ.

### mẫu lập trình (coding pattern) — Low-specificity component các bộ chọn (selectors)

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

### mẫu thiết kế (design pattern) — bộ chọn (selector) as API

Hãy coi bộ chọn (selector) như giao diện công khai (public API).

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

bộ chọn (selector) tốt thường:
- đủ cụ thể để không leak,
- đủ yếu để override,
- không encode quá nhiều DOM structure,
- phản ánh role/trạng thái (state) thay vì vị trí ngẫu nhiên.


# 2.1 Universal bộ chọn (selector)

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

# 2.2 Type bộ chọn (selector)

```css
button {}
p {}
article {}
```

độ đặc hiệu (specificity) thấp, phù hợp base styles.

# 2.3 Class bộ chọn (selector)

```css
.card {}
.btn-primary {}
```

Đây nên là bộ chọn (selector) chính trong component CSS.

# 2.4 ID bộ chọn (selector)

```css
#header {}
```

ID có độ đặc hiệu (specificity) rất cao.

**Senior rule:** tránh dùng ID cho styling reusable.

# 2.5 Attribute các bộ chọn (selectors)

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

**Thực tế:** trạng thái (state) styling rất tốt với `data-*`.

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

**Senior note:** bộ chọn (selector) càng phụ thuộc sâu vào DOM càng fragile.

Không nên:

```css
.page .main .content .card .header span {}
```

Nên:

```css
.card-title {}
```

---

# 4. các lớp giả (pseudo-classes) [CORE → ADV]

## 4.1 Interaction các trạng thái (states)

```css
a:hover {}
button:active {}
input:focus {}
input:focus-visible {}
```

### `:focus` vs `:focus-visible`

- `:focus`: element đang focus.
- `:focus-visible`: browser xác định cần hiện chỉ báo tiêu điểm (focus indicator), thường khi keyboard navigation.

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

vì phá keyboard khả năng tiếp cận (accessibility).

## 4.2 Form các trạng thái (states)

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

## 4.3 Structural các bộ chọn (selectors)

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

Có thể nhận bộ chọn (selector) danh sách (list):

```css
input:not([type="checkbox"], [type="radio"]) {}
```

## 4.5 `:is()` [ADV]

Gom bộ chọn (selector):

```css
:is(h1, h2, h3) {
  line-height: 1.2;
}
```

Thay cho:

```css
h1, h2, h3 {}
```

Hữu ích với bộ chọn (selector) dài:

```css
.article :is(h2, h3, h4) {}
```

độ đặc hiệu (specificity) của `:is()` lấy độ đặc hiệu (specificity) cao nhất trong arguments.

## 4.6 `:where()` [ADV]

Syntax tương tự `:is()` nhưng **độ đặc hiệu (specificity) = 0**.

```css
:where(.content) h2 {
  margin-block-start: 2rem;
}
```

Rất hữu ích khi xây base/theme dễ override.

## 4.7 `:has()` [ADV/MODERN]

bộ chọn (selector) "parent-aware":

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

**Senior note:** `:has()` giảm nhu cầu thêm class/trạng thái (state) bằng JavaScript cho nhiều UI trạng thái (state) đơn giản.

---

# 5. các phần tử giả (pseudo-elements) [CORE]

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

Không dùng phần tử giả (pseudo-element) cho content quan trọng về ngữ nghĩa (semantics).

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

# 6. cơ chế phân tầng (cascade) — nền tảng sống còn của CSS [CORE/ADV]

## Pattern notes — cơ chế phân tầng (cascade)

### CSS Idiom — Win by kiến trúc (architecture), not by độ đặc hiệu (specificity)

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

### mẫu lập trình (coding pattern) — Default → biến thể (variant) → trạng thái (state)

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

### mẫu thiết kế (design pattern) — Layered cơ chế phân tầng (cascade)

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
- không cuộc chiến độ đặc hiệu (specificity war),
- vendor CSS có chỗ riêng,
- component CSS dễ reason.

### Senior note

Nếu phải hỏi "bộ chọn (selector) nào mạnh hơn" quá thường xuyên, vấn đề thường nằm ở kiến trúc (architecture) chứ không phải thiếu kiến thức độ đặc hiệu (specificity).


cơ chế phân tầng (cascade) quyết định khai báo (declaration) nào thắng.

Các yếu tố chính:

1. nguồn và mức quan trọng (origin/importance).
2. lớp phân tầng (cascade layer).
3. độ đặc hiệu (specificity).
4. độ gần phạm vi (scope proximity) trong scoped CSS.
5. thứ tự nguồn (source order).

## 6.1 độ đặc hiệu (specificity)

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

## 6.2 thứ tự nguồn (source order)

Nếu độ đặc hiệu (specificity) bằng nhau, rule viết sau thắng:

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
- tiện ích (utility) API có chủ đích,
- override external styles khó kiểm soát,
- khả năng tiếp cận (accessibility)/user override đặc biệt.

## 6.4 Global keywords

Các thuộc tính (property) thường chấp nhận:

```css
inherit
initial
unset
revert
revert-layer
```

### `inherit`

Ép lấy computed giá trị (value) từ parent.

```css
button {
  font: inherit;
}
```

### `initial`

Về initial giá trị (value) theo specification.

### `unset`

- thuộc tính (property) có inherit → behave như `inherit`;
- không inherit → behave như `initial`.

### `revert`

Quay về style của cơ chế phân tầng (cascade) origin trước.

### `revert-layer`

Bỏ khai báo (declaration) trong lớp phân tầng (cascade layer) hiện tại để quay về layer thấp hơn.

---

# 7. các lớp phân tầng (cascade layers) `@layer` [ADV/MODERN]

Dùng để quản lý precedence theo kiến trúc thay vì cuộc chiến độ đặc hiệu (specificity war).

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

Layer khai báo sau trong order có precedence cao hơn trong normal các khai báo (declarations).

**Senior kiến trúc (architecture):**

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

# 8. kế thừa (inheritance) [CORE]

Một số thuộc tính (property) inherit mặc định:

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

Nhiều thuộc tính (property) layout không inherit:

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

# 9. các giá trị (values) & Units [CORE]

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

## vùng nhìn (viewport) units

```text
vw, vh
vmin, vmax
svw, svh
lvw, lvh
dvw, dvh
```

- `svh`: small vùng nhìn (viewport).
- `lvh`: large vùng nhìn (viewport).
- `dvh`: dynamic vùng nhìn (viewport).

Mobile full-screen:

```css
.page {
  min-height: 100dvh;
}
```

Thường tốt hơn `100vh` trên mobile browser có thanh address thay đổi kích thước.

## truy vấn vùng chứa (container query) units

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

Ý nghĩa `%` phụ thuộc thuộc tính (property).

```css
width: 50%;
```

thường dựa vào khối chứa tham chiếu (containing block) width.

Classic pitfall:

```css
padding-top: 10%;
```

Percentage padding truyền thống resolve theo inline size của khối chứa tham chiếu (containing block), không nhất thiết theo height.

---

# 11. CSS Math các hàm (functions) [CORE/ADV]

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

# 12. Custom các thuộc tính (properties) / CSS các biến (variables) [CORE]

## Pattern notes — Custom các thuộc tính (properties)

### CSS Idiom — phương án dự phòng (fallback) token

```css
.card {
  color: var(--card-color, var(--color-text));
}
```

### mẫu lập trình (coding pattern) — Token pipeline

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

### mẫu thiết kế (design pattern) — Theme by token override

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

Custom thuộc tính (property) mạnh nhất khi dùng như **thời gian chạy (runtime) contract**, không chỉ thay literal giá trị (value).


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

phương án dự phòng (fallback):

```css
color: var(--text-color, #222);
```

## Custom thuộc tính (property) có cơ chế phân tầng (cascade) + inherit

```css
.theme-dark {
  --surface: #111;
  --text: #fff;
}
```

## giao diện thành phần (component API)

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

**Senior note:** custom các thuộc tính (properties) nên là **token thiết kế (design tokens) + component tokens**, không chỉ là biến thay text.

---

# 13. `@property` [ADV/MODERN]

Khai báo kiểu cho custom thuộc tính (property):

```css
@property --progress {
  syntax: "<percentage>";
  inherits: false;
  initial-value: 0%;
}
```

Sau đó có thể animate typed giá trị (value):

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

# 14. mô hình hộp (box model) [CORE]

## Pattern notes — mô hình hộp (box model)

### CSS Idiom — Universal border-box

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

### mẫu lập trình (coding pattern) — Section + inner wrapper

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

### mẫu thiết kế (design pattern) — Box responsibility

Một box nên có responsibility rõ:

```text
outer box → positioning/layout
middle box → spacing/border/background
inner box → content flow
```

Không phải lúc nào cũng cần nhiều wrapper; đây là mô hình tư duy (mental model) để gỡ lỗi (debug).


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

### mẫu lập trình (coding pattern) — Intrinsic card width

```css
.card {
  inline-size: fit-content;
  max-inline-size: 100%;
}
```

### mẫu thiết kế (design pattern) — Constraint-based layout

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

## Common các giá trị (values)

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

Co giãn giữa min-content và max-content theo không gian khả dụng (available space).

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

## gộp lề (margin collapsing) [ADV]

Vertical margins của normal-flow block có thể collapse.

```css
h2 { margin-bottom: 20px; }
p  { margin-top: 30px; }
```

Khoảng cách không nhất thiết 50px; có thể collapse thành 30px.

Không collapse trong nhiều trường hợp như:
- flex/grid layout,
- padding/border tách parent-child,
- ngữ cảnh định dạng khối (block formatting context) khác.

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

Không nhận negative giá trị (value).

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
- rất phù hợp chỉ báo tiêu điểm (focus indicator).

---

# 20. Display & ngữ cảnh định dạng (formatting context) [CORE/ADV]

## Pattern notes — ngữ cảnh định dạng (formatting context)

### CSS Idiom — `flow-root` để isolate block flow

```css
.component {
  display: flow-root;
}
```

### mẫu lập trình (coding pattern) — Layout primitives

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

### mẫu thiết kế (design pattern) — Formatting-context boundary

Component phức tạp nên chủ động tạo boundary khi cần:
- `display: flow-root`,
- Flex,
- Grid,
- `contain`,
- `isolation`.

Điều này giảm tác dụng phụ (side effect) từ bên ngoài.


thuộc tính (property):

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

Loại khỏi layout và khả năng tiếp cận (accessibility) tree trong hầu hết trường hợp.

## `display: flow-root` [ADV]

Tạo ngữ cảnh định dạng khối (block formatting context) mới.

Useful clear float / isolate flow:

```css
.container {
  display: flow-root;
}
```

## `display: contents`

Box của element biến mất nhưng children vẫn participate layout.

⚠ Cẩn thận khả năng tiếp cận (accessibility)/browser behavior với ngữ nghĩa (semantics) đặc biệt.

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
- tạo ngữ cảnh xếp chồng (stacking context) khi opacity < 1.

---

# 22. luồng bố cục thông thường (normal flow) [CORE]

luồng bố cục thông thường (normal flow) gồm block flow + inline flow trước khi:
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

### mẫu lập trình (coding pattern) — Positioning context

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

### mẫu thiết kế (design pattern) — Overlay ownership

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

Element vẫn giữ vị trí trong luồng bố cục thông thường (normal flow), nhưng có thể offset.

Quan trọng hơn: thường tạo khối chứa tham chiếu (containing block) cho absolute child.

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

Ra khỏi luồng bố cục thông thường (normal flow).

Position dựa vào khối chứa tham chiếu (containing block) phù hợp.

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

Thường cố định theo vùng nhìn (viewport).

```css
.fab {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
}
```

⚠ ancestor có `transform`, `filter`, `perspective`... có thể thay khối chứa tham chiếu (containing block) behavior.

## `sticky`

Hybrid relative/fixed theo vùng chứa cuộn (scroll container).

```css
.header {
  position: sticky;
  top: 0;
}
```

Common failure:
- quên `top`,
- ancestor có overflow tạo vùng chứa cuộn (scroll container) khác,
- không đủ scroll space,
- layout constraints.

---

# 24. khối chứa tham chiếu (containing block) [ADV]

Nhiều `%`, absolute offsets và sizing được tính dựa vào **khối chứa tham chiếu (containing block)**.

Không phải lúc nào cũng là parent trực tiếp.

Absolute element thường tìm ancestor tạo khối chứa tham chiếu (containing block), ví dụ positioned ancestor.

gỡ lỗi (debug) absolute/fixed lỗi phải hỏi:

> "khối chứa tham chiếu (containing block) thực sự của element này là element nào?"

---

# 25. z-index & ngữ cảnh xếp chồng (stacking context) [CORE/ADV]

## Pattern notes — Stacking

### CSS Idiom — Local stacking cô lập (isolation)

```css
.component {
  isolation: isolate;
}
```

### mẫu lập trình (coding pattern) — mang tính ngữ nghĩa (semantic) z-index scale

```css
:root {
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 500;
  --z-modal: 1000;
  --z-toast: 1100;
}
```

### mẫu thiết kế (design pattern) — Layer contract

Không cho từng component tự tạo số `z-index`.

Định nghĩa mang tính ngữ nghĩa (semantic) layers:
- content,
- sticky,
- dropdown,
- overlay,
- modal,
- toast.

### Senior note

Khi `z-index` lỗi, gỡ lỗi (debug) parent ngữ cảnh xếp chồng (stacking context) trước khi tăng số.


`z-index` không phải global number ranking đơn giản.

```css
.modal {
  position: fixed;
  z-index: 1000;
}
```

Một ngữ cảnh xếp chồng (stacking context) có thể được tạo bởi nhiều điều kiện, ví dụ:
- root element,
- positioned element với `z-index`,
- `position: fixed/sticky`,
- `opacity < 1`,
- `transform != none`,
- `filter`,
- `isolation: isolate`,
- một số flex/phần tử Grid (grid item) có z-index,
- `contain` phù hợp.

Pitfall:

```text
child z-index: 999999
```

vẫn có thể nằm dưới element khác nếu parent ngữ cảnh xếp chồng (stacking context) thấp hơn.

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

các giá trị (values):

```text
visible
hidden
clip
scroll
auto
```

## `hidden`

Clip overflow và thường tạo vùng chứa cuộn (scroll container) ngữ nghĩa (semantics).

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

các giá trị (values) conceptually:
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

### mẫu lập trình (coding pattern) — Media Object

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

### mẫu lập trình (coding pattern) — Safe flexible content

Nếu flex child chứa text/ellipsis:

```css
.content {
  min-width: 0;
}
```

### mẫu thiết kế (design pattern) — One-dimensional composition

Flexbox phù hợp khi layout được mô tả bằng:

```text
items in a row
hoặc
items in a column
```

Nếu cần điều khiển nhiều rows + columns đồng thời, chuyển mô hình tư duy (mental model) sang Grid.


Flexbox là layout **1 chiều**: row hoặc column.

```css
.container {
  display: flex;
}
```

## 28.1 Container các thuộc tính (properties)

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

Align theo **trục chính (main axis)**.

Common các giá trị (values):

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

Align items trên **trục chéo (cross axis)**.

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

# 29. phần tử Flex (flex item) các thuộc tính (properties) [CORE]

## `flex-grow`

```css
.item {
  flex-grow: 1;
}
```

Phân chia **positive không gian dư (free space)** theo tỉ lệ.

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

⚠ Chỉ thay visual order, không nhất thiết thay DOM/read/focus order. Tránh dùng cho mang tính ngữ nghĩa (semantic) reordering.

---

# 30. Flexbox Pitfall: `min-width: auto` [ADV]

phần tử Flex (flex item) mặc định có minimum size dựa vào content.

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

### mẫu lập trình (coding pattern) — Sidebar layout

```css
.layout {
  display: grid;
  grid-template-columns:
    minmax(12rem, 18rem)
    minmax(0, 1fr);
  gap: 2rem;
}
```

### mẫu thiết kế (design pattern) — Track-first layout

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

## 32.1 các dải lưới (grid tracks)

```css
grid-template-columns: 1fr 1fr 1fr;
```

## `fr`

Fraction của available không gian dư (free space).

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

## Responsive grid không truy vấn môi trường (media query)

```css
grid-template-columns:
  repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
```

### `auto-fit` vs `auto-fill`

- `auto-fill`: giữ các hypothetical empty tracks.
- `auto-fit`: collapse empty tracks để existing items stretch.

---

# 33. Grid placement

các thuộc tính (properties):

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

các thuộc tính (properties):

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

⚠ `dense` có thể visually reorder items; cẩn thận khả năng tiếp cận (accessibility).

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

### mẫu lập trình (coding pattern) — Shared track contract

Parent định nghĩa track system; child reuse đúng track đó.

### mẫu thiết kế (design pattern) — Nested alignment without duplicated dimensions

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

các thuộc tính (properties):

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

### mẫu lập trình (coding pattern) — Fluid type scale

```css
:root {
  --step--1: clamp(.875rem, .84rem + .15vw, .95rem);
  --step-0: clamp(1rem, .95rem + .25vw, 1.125rem);
  --step-1: clamp(1.25rem, 1.05rem + .9vw, 1.75rem);
  --step-2: clamp(1.75rem, 1.25rem + 2vw, 3rem);
}
```

### mẫu thiết kế (design pattern) — Typographic hierarchy

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

Luôn có generic phương án dự phòng (fallback).

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

biến (variable) font có thể hỗ trợ range.

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

# 42. Text các thuộc tính (properties) [CORE]

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

Không dùng CSS uppercase thay cho dữ liệu nếu ngữ nghĩa (semantics)/copy thực sự cần uppercase.

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

Useful các giá trị (values):

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

hiệu năng (performance): ưu tiên WOFF2, subset khi cần, không load quá nhiều weights.

---

# 45. Color [CORE → MODERN]

## Pattern notes — Color

### CSS Idiom — `currentColor`

```css
.icon {
  fill: currentColor;
}
```

### mẫu lập trình (coding pattern) — mang tính ngữ nghĩa (semantic) color tokens

```css
--color-action: #2563eb;
--color-danger: #dc2626;
--color-text-muted: #6b7280;
```

### mẫu thiết kế (design pattern) — Primitive → mang tính ngữ nghĩa (semantic) → Component

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

`currentColor` = current giá trị (value) của `color`.

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

Oklch hữu ích cho hệ thống thiết kế (design system) vì lightness gần với perceived lightness hơn HSL.

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

Kết hợp color scheme-aware các giá trị (values) khi môi trường hỗ trợ:

```css
:root {
  color-scheme: light dark;
  --surface: light-dark(white, #111);
}
```

---

# 46. Backgrounds [CORE]

các thuộc tính (properties):

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

các hàm (functions):
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

Có cost rendering; test hiệu năng (performance).

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

# 53. thuộc tính logic (logical properties) [CORE/ADV]

## Pattern notes — thuộc tính logic (logical properties)

### CSS Idiom — Inline centering

```css
margin-inline: auto;
```

### CSS Idiom — Writing-mode-safe spacing

```css
padding-inline: 1rem;
padding-block: .75rem;
```

### mẫu lập trình (coding pattern) — International-ready component

```css
margin-inline-start: auto;
border-inline-start: 1px solid;
```

### mẫu thiết kế (design pattern) — Direction-agnostic UI

Component tránh hard-code LTR assumptions để hỗ trợ RTL/localization tốt hơn.


Thay vì phụ thuộc `left/right/top/bottom`, dùng writing-mode-aware các thuộc tính (properties).

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

**Senior note:** thuộc tính logic (logical properties) giúp RTL/i18n tốt hơn.

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

# 55. thiết kế đáp ứng (responsive design) [CORE]

## Pattern notes — thiết kế đáp ứng (responsive design)

### CSS Idiom — Content-driven điểm ngắt (breakpoint)

Không chọn điểm ngắt (breakpoint) vì tên thiết bị. Chọn tại điểm layout cần thay đổi.

### mẫu lập trình (coding pattern) — Fluid first, query second

```text
1. intrinsic sizing
2. flex/grid wrapping
3. clamp/min/max
4. media/container query khi cần
```

### mẫu thiết kế (design pattern) — Responsive component

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


Responsive không chỉ là "mobile điểm ngắt (breakpoint)".

Senior approach:
1. content-first,
2. bố cục nội tại (intrinsic layout),
3. fluid sizing,
4. truy vấn môi trường (media query) khi layout thực sự cần đổi,
5. truy vấn vùng chứa (container query) khi component cần thích ứng theo container.

---

# 56. các truy vấn môi trường (media queries) [CORE]

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

Không bắt buộc mọi project phải mobile-first, nhưng thường giúp cải tiến lũy tiến (progressive enhancement) và CSS đơn giản.

---

# 58. User Preference các truy vấn môi trường (media queries) [CORE/ADV]

## Dark mode

```css
@media (prefers-color-scheme: dark) {
  :root {
    --surface: #111;
    --text: #eee;
  }
}
```

## giảm chuyển động (reduced motion)

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

# 59. các truy vấn vùng chứa (container queries) [ADV/MODERN]

## Pattern notes — truy vấn vùng chứa (container query)

### CSS Idiom — Named container contract

```css
.panel {
  container: panel / inline-size;
}
```

### mẫu lập trình (coding pattern) — Component mode switch

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

### mẫu thiết kế (design pattern) — Contextual responsiveness

Component hỏi:

> "Không gian tôi thực sự nhận được rộng bao nhiêu?"

thay vì chỉ hỏi vùng nhìn (viewport).


truy vấn môi trường (media query) hỏi vùng nhìn (viewport).

truy vấn vùng chứa (container query) hỏi **container của component**.

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

**Senior use case:** component dùng trong main, sidebar, modal, dashboard card mà không phụ thuộc vùng nhìn (viewport).

---

# 60. Container Style Queries [MODERN]

Có thể query custom thuộc tính (property)/computed style trạng thái (state) của container trong mức hỗ trợ trình duyệt (browser support) phù hợp.

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

## Individual transform các thuộc tính (properties)

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

### CSS Idiom — Animate explicit các thuộc tính (properties)

```css
transition:
  opacity 150ms ease,
  transform 150ms ease;
```

### mẫu lập trình (coding pattern) — trạng thái (state) transition

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

### mẫu thiết kế (design pattern) — Motion as trạng thái (state) feedback

Motion nên giải thích trạng thái (state) change, không chỉ để trang "đẹp hơn".


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
- animate thuộc tính (property) ngoài ý muốn,
- khó predict,
- có thể gây hiệu năng (performance) issues.

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

### mẫu lập trình (coding pattern) — Enter / Open / Leave trạng thái (state)

```css
.toast[data-state="entering"] {}
.toast[data-state="open"] {}
.toast[data-state="leaving"] {}
```

### mẫu thiết kế (design pattern) — Separate behavior from presentation

```text
Application state → data/aria attribute
CSS → visual state
```

JS không nên hard-code visual details; CSS không nên tự quyết định business trạng thái (state).


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

các thuộc tính (properties):

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

# 65. hiệu năng (performance) của animation [ADV]

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

Tôn trọng giảm chuyển động (reduced motion).

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

# 68. hoạt ảnh điều khiển bằng cuộn (scroll-driven animations) [MODERN]

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

Kiểm tra mức hỗ trợ trình duyệt (browser support) trước khi dùng cho critical UX; cải tiến lũy tiến (progressive enhancement) là hướng tốt.

---

# 69. chuyển cảnh giao diện (view transitions) [MODERN]

Cho phép browser animate visual transition giữa UI các trạng thái (states)/pages tùy API/context.

CSS side thường liên quan các phần tử giả (pseudo-elements):

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
- SPA trạng thái (state) change.

Đừng làm animation cản thao tác hoặc quá dài.

---

# 70. định vị theo điểm neo (anchor positioning) [MODERN]

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

Hệ sinh thái còn gồm các concept/thuộc tính (property) như:
- `anchor-name`
- `position-anchor`
- `anchor()`
- `anchor-size()`
- phương án dự phòng (fallback)/position try features.

Use case:
- tooltip,
- dropdown,
- menu,
- popover.

Senior rule: kiểm tra browser target và phương án dự phòng (fallback) cho UI critical.

---

# 71. CSS lồng cú pháp (nesting) [MODERN]

## Pattern notes — lồng cú pháp (nesting)

### CSS Idiom — Nest các trạng thái (states), not DOM depth

Tốt:

```css
.button {
  &:hover {}
  &:focus-visible {}
  &[data-variant="danger"] {}
}
```

Tránh lồng cú pháp (nesting) theo toàn bộ DOM tree.

### mẫu lập trình (coding pattern) — Component-local grouping

lồng cú pháp (nesting) phù hợp cho:
- các trạng thái (states),
- các phần tử giả (pseudo-elements),
- truy vấn môi trường (media query),
- truy vấn vùng chứa (container query),
- direct component slots.

### mẫu thiết kế (design pattern) — Flat giao diện công khai (public API), nested implementation

Public các bộ chọn (selectors) vẫn nên đơn giản; lồng cú pháp (nesting) chỉ hỗ trợ tổ chức source.


Native CSS lồng cú pháp (nesting):

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

`&` đại diện bộ chọn (selector) hiện tại.

**Không nên lồng cú pháp (nesting) quá sâu:**

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

Vì tạo bộ chọn (selector) coupling và độ đặc hiệu (specificity) complexity.

Rule thực tế: 1–3 levels là đủ trong đa số component.

---

# 72. `@scope` [MODERN/ADV]

## Pattern notes — phạm vi (scope)

### CSS Idiom — Scoped typography

```css
@scope (.article) {
  h2 {}
  p {}
  a {}
}
```

### mẫu lập trình (coding pattern) — Scoped defaults

Dùng cho:
- article,
- widget,
- embedded app,
- third-party content area.

### mẫu thiết kế (design pattern) — Controlled ranh giới style (style boundary)

`@scope` nằm giữa global CSS và full đóng gói (encapsulation) như Shadow DOM (cây DOM đóng gói)/CSS Modules.


Giới hạn bộ chọn (selector) trong vùng DOM.

Concept:

```css
@scope (.article) {
  h2 {
    color: var(--heading-color);
  }
}
```

Có thể phạm vi (scope) đến boundary trong syntax phù hợp.

Use case:
- component/themed subtree,
- tránh các bộ chọn (selectors) leak,
- giảm nhu cầu BEM prefix trong một số kiến trúc.

---

# 73. `@supports` — các truy vấn hỗ trợ tính năng (feature queries) [ADV]

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

cải tiến lũy tiến (progressive enhancement):

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
| `@media` | môi trường/vùng nhìn (viewport)/user preference | responsive page, dark mode |
| `@container` | kích thước/trạng thái (state) container | responsive component |
| `@supports` | browser có support feature không | cải tiến lũy tiến (progressive enhancement) |

---

# 75. các danh sách (lists) [CORE]

các thuộc tính (properties):

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

các thuộc tính (properties):

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

`fixed` giúp predictable widths/hiệu năng (performance) cho bảng lớn khi width xác định.

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
- checked trạng thái (state),
- disabled,
- độ tương phản cao (high contrast),
- khả năng tiếp cận (accessibility) visuals.

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

các giá trị (values):
- `none`
- `both`
- `horizontal`
- `vertical`

## `field-sizing` [MODERN]

Trong mức hỗ trợ trình duyệt (browser support) phù hợp, giúp form controls size theo content.

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

Đừng dùng `cursor:pointer` cho non-interactive element nếu ngữ nghĩa (semantics) không click được.

## `pointer-events`

```css
.overlay-decoration {
  pointer-events: none;
}
```

các giá trị (values) web UI thường:
- `auto`
- `none`

⚠ `pointer-events:none` không đồng nghĩa disabled mang tính ngữ nghĩa (semantic).

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

phần tử giả (pseudo-element):

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

Concept các thuộc tính (properties):
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

Tạo ngữ cảnh xếp chồng (stacking context) mới và isolate blending.

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

Tuy nhiên production thường ưu tiên bundler/quy trình build (build pipeline) hoặc `<link>` vì `@import` có thể tạo dependency/loading considerations.

---

# 86. `@starting-style` [MODERN]

Hỗ trợ transition từ trạng thái element mới xuất hiện / discrete-state scenarios trong mức hỗ trợ trình duyệt (browser support) phù hợp.

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

Một số discrete thuộc tính (property) có thể tham gia transitions với:

```css
transition-behavior: allow-discrete;
```

Use case:
- `display`,
- overlay/dialog/popover lifecycle
trong các mức hỗ trợ trình duyệt (browser support) phù hợp.

---

# 88. kiến trúc (architecture): tổ chức CSS như senior [ADV]

## Pattern notes — kiến trúc (architecture)

### CSS Idiom — One responsibility per layer

```text
tokens      → values
base        → element defaults
layout      → spatial primitives
components  → UI components
utilities   → atomic helpers
```

### mẫu lập trình (coding pattern) — Composition over overrides

```html
<div class="stack card">...</div>
```

thay vì tạo nhiều component biến thể (variant) chỉ để đổi spacing.

### mẫu thiết kế (design pattern) — CUBE-like thinking

```text
Composition
Utility
Block
Exception
```

### mẫu thiết kế (design pattern) — ITCSS-like ordering

Từ global/general → local/specific:
- settings/tokens,
- tools,
- generic,
- elements,
- objects,
- components,
- các tiện ích (utilities).

Có thể kết hợp với `@layer`.

### Senior note

kiến trúc (architecture) tốt là kiến trúc (architecture) mà dev mới có thể dự đoán:
- style nằm ở đâu,
- override thế nào,
- trạng thái (state) viết ở đâu,
- token nào được dùng,
- component nào chịu trách nhiệm layout.


CSS production không chỉ là biết thuộc tính (property).

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

## ưu tiên tiện ích (utility-first)

```html
<div class="flex items-center gap-4">
```

Ưu:
- nhanh,
- constrained token thiết kế (design tokens),
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
- local phạm vi (scope),
- giảm collision.

## CSS-in-JS

Có nhiều thời gian chạy (runtime)/build-time approach. Không nên coi đây là "CSS replacement"; vẫn cần hiểu cơ chế phân tầng (cascade)/layout/browser.

---

# 90. Recommended Layer kiến trúc (architecture)

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

# 91. token thiết kế (design tokens)

## Pattern notes — token thiết kế (design tokens)

### CSS Idiom — mang tính ngữ nghĩa (semantic) alias

```css
--gray-700: #374151;
--color-text-default: var(--gray-700);
```

### mẫu lập trình (coding pattern) — phân cấp token (token hierarchy)

```text
Foundation token
→ Semantic token
→ Component token
→ State token
```

### mẫu thiết kế (design pattern) — hợp đồng chủ đề (theme contract)

Theme ưu tiên override mang tính ngữ nghĩa (semantic) tokens. Component tokens chỉ override khi component có requirement riêng.


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
- **token ngữ nghĩa (semantic token)**: `--color-text-muted`
- **token thành phần (component token)**: `--button-bg`

---

# 92. Theme kiến trúc (architecture)

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

# 93. Component trạng thái (state)

## Pattern notes — Component trạng thái (state)

### CSS Idiom — Attribute-driven trạng thái (state)

```css
.accordion[data-state="open"] {}
.tabs [aria-selected="true"] {}
.button[aria-pressed="true"] {}
```

### mẫu lập trình (coding pattern) — trạng thái (state) matrix

```text
variant: primary | secondary | danger
size: sm | md | lg
state: default | hover | focus | disabled | loading
```

### mẫu thiết kế (design pattern) — biến thể (variant)/trạng thái (state) separation

biến thể (variant) = identity/style mode.

trạng thái (state) = tình trạng thời gian chạy (runtime)/interaction.

Không trộn thành class kiểu `.button-danger-disabled`.


Nên encode trạng thái (state) rõ:

```css
.button[data-variant="danger"] {}
.tabs [aria-selected="true"] {}
.accordion[data-state="open"] {}
```

Ưu tiên trạng thái (state) từ mang tính ngữ nghĩa (semantic) attributes khi có:

```css
button:disabled {}
input:checked {}
[aria-current="page"] {}
```

---

# 94. độ đặc hiệu (specificity) Strategy [ADV]

Target:
- phần lớn các bộ chọn (selectors) low độ đặc hiệu (specificity),
- tránh ID,
- tránh lồng cú pháp (nesting) sâu,
- dùng layer,
- dùng `:where()` cho defaults,
- không "đấu độ đặc hiệu (specificity)".

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

dễ thắng vì `:where()` = zero độ đặc hiệu (specificity) cho phần đó.

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

# 96. khả năng tiếp cận (accessibility) [CORE/SENIOR]

## Pattern notes — khả năng tiếp cận (accessibility)

### CSS Idiom — Focus-visible ring

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

### mẫu lập trình (coding pattern) — Accessible hidden text

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

### mẫu thiết kế (design pattern) — cải tiến lũy tiến (progressive enhancement)

Base experience phải dùng được trước; animation/filter/view-transition là enhancement.

### Senior note

Style đẹp nhưng làm mất focus, cắt text khi zoom hoặc reorder visual khác DOM là regression.


CSS có thể phá khả năng tiếp cận (accessibility) dù HTML đúng.

## Focus

Phải có visible focus:

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

## Contrast

Text/background phải có contrast phù hợp theo khả năng tiếp cận (accessibility) requirements của project.

Không chỉ dựa vào màu để truyền information:

Sai:

```text
red = error
green = success
```

Nên có icon/text/trạng thái (state) thêm.

## giảm chuyển động (reduced motion)

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

Các kỹ thuật khác nhau có ngữ nghĩa (semantics) khác:

```css
display: none;
visibility: hidden;
opacity: 0;
```

Không interchangeable.

---

# 97. Visually Hidden tiện ích (utility)

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

# 98. màu cưỡng bức (forced colors) / độ tương phản cao (high contrast) [ADV]

```css
@media (forced-colors: active) {
  .custom-control {
    border: 1px solid CanvasText;
  }
}
```

Không assume colors/shadows luôn được render như design.

---

# 99. hiệu năng (performance) [ADV/SENIOR]

## Pattern notes — hiệu năng (performance)

### CSS Idiom — Skip off-screen rendering khi phù hợp

```css
.long-section {
  content-visibility: auto;
  contain-intrinsic-size: auto 600px;
}
```

### mẫu lập trình (coding pattern) — Animate compositor-friendly các thuộc tính (properties)

Ưu tiên `opacity` và `transform` khi UX tương đương.

### mẫu thiết kế (design pattern) — hiệu năng (performance) budget

Theo dõi:
- CSS bundle size,
- font bytes,
- chi phí kết xuất (rendering cost),
- dịch chuyển bố cục (layout shift),
- long animation,
- large filter/backdrop regions.


CSS hiệu năng (performance) thường liên quan:
- stylesheet size,
- unused CSS,
- expensive rendering,
- font loading,
- image/background,
- dao động bố cục do đọc/ghi xen kẽ (layout thrashing) từ JS + CSS,
- huge DOM,
- animation,
- tính lại style (style recalculation).

## Không micro-optimize bộ chọn (selector) vô nghĩa

Modern browser bộ chọn (selector) engine rất tối ưu. Vấn đề maintainability thường lớn hơn việc `.a > .b` nhanh hơn hay chậm hơn vài microsecond.

## Tập trung vào

1. ship ít CSS hơn,
2. remove unused CSS,
3. split critical/non-critical khi phù hợp,
4. avoid massive global rules,
5. optimize font/image,
6. avoid layout-heavy animation loops,
7. use DevTools hiệu năng (performance).

---

# 100. chuỗi xử lý kết xuất (rendering pipeline) mô hình tư duy (mental model) [ADV]

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

# 101. dịch chuyển bố cục (layout shift) [ADV]

Tránh dịch chuyển bố cục (layout shift) bằng:
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

# 102. Font hiệu năng (performance)

Checklist:
- WOFF2.
- Chỉ load weights cần dùng.
- biến (variable) font nếu có lợi.
- `font-display` phù hợp.
- preload only critical font.
- subset unicode nếu large font family.
- system fonts khi design cho phép.

---

# 103. CSS gỡ lỗi (debugging) Workflow [SENIOR]

## Pattern notes — gỡ lỗi (debugging)

### mẫu lập trình (coding pattern) — Constraint tracing

```text
computed width
→ max/min constraints
→ containing block
→ intrinsic content
→ flex/grid track
→ overflow
```

### mẫu lập trình (coding pattern) — cơ chế phân tầng (cascade) tracing

```text
matched selector?
→ declaration valid?
→ layer?
→ specificity?
→ source order?
→ inheritance?
```

### mẫu thiết kế (design pattern) — gỡ lỗi (debug) from model, not trial-and-error

Tìm system quyết định behavior:
- cơ chế phân tầng (cascade),
- ngữ cảnh định dạng (formatting context),
- sizing algorithm,
- positioning,
- stacking.


Khi layout sai:

## Step 1 — Inspect element

DevTools:
- bộ chọn (selector) matched?
- thuộc tính (property) bị strike-through?
- computed giá trị (value)?
- inherited từ đâu?

## Step 2 — mô hình hộp (box model)

Check:
- content size,
- padding,
- border,
- margin.

## Step 3 — Layout context

Element là:
- block?
- phần tử Flex (flex item)?
- phần tử Grid (grid item)?
- positioned?
- vùng chứa cuộn (scroll container)?

## Step 4 — Constraints

Check:
- min/max width/height,
- `min-width:auto`,
- định cỡ nội tại (intrinsic sizing),
- overflow,
- aspect ratio.

## Step 5 — Position context

Check:
- khối chứa tham chiếu (containing block),
- ngữ cảnh xếp chồng (stacking context),
- clipping ancestor.

## Step 6 — Browser responsive modes

Test:
- narrow vùng nhìn (viewport),
- zoom,
- long text,
- translated text,
- keyboard focus,
- giảm chuyển động (reduced motion),
- dark mode.

---

# 104. gỡ lỗi (debug) Helpers

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
- ngữ cảnh xếp chồng (stacking context) parent,
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
- vùng chứa cuộn (scroll container) nào?
- parent height?

## Bug 5 — `height:100%` không có tác dụng

Percentage height cần khối chứa tham chiếu (containing block) có definite height trong nhiều layout cases.

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

Auto margins hoạt động khác nhau tùy ngữ cảnh định dạng (formatting context)/axis/available không gian dư (free space).

## Bug 8 — absolute element "bay" sai nơi

khối chứa tham chiếu (containing block) không phải ancestor bạn nghĩ.

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

Trong production ưu tiên native `<dialog>`/popover khi ngữ nghĩa (semantics) phù hợp thay vì recreate mọi behavior bằng div.

---

# 108. Tooltip / Dropdown — senior considerations

CSS layout chỉ là một phần.

Cần nghĩ:
- định vị theo điểm neo (anchor positioning),
- vùng nhìn (viewport) collision,
- keyboard,
- quản lý tiêu điểm (focus management),
- escape key,
- ARIA ngữ nghĩa (semantics),
- portal/lớp trên cùng (top layer),
- scroll clipping.

Không giải quyết complex overlay chỉ bằng `position:absolute; z-index:99999`.

---

# 109. lớp trên cùng (top layer) [ADV]

Một số browser-managed UI như dialog/popover có thể được đặt vào **lớp trên cùng (top layer)**, vượt các ngữ cảnh xếp chồng (stacking contexts) bình thường.

Điều này giải thích tại sao z-index model của native dialog/popover khác div modal bình thường.

phần tử giả (pseudo-element) liên quan backdrop:

```css
dialog::backdrop {
  background: rgb(0 0 0 / .5);
}
```

---

# 110. CSS and Shadow DOM (cây DOM đóng gói) [ADV]

Shadow DOM (cây DOM đóng gói) tạo style đóng gói (encapsulation).

Concept cần biết:
- shadow tree,
- `:host`,
- `:host(...)`,
- `::part(...)`,
- CSS custom các thuộc tính (properties) xuyên boundary theo kế thừa (inheritance)/cơ chế phân tầng (cascade) rules phù hợp.

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

# 112. CSS các hàm (functions) nên biết

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

## các biến (variables)/environment

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

# 114. thuộc tính (property) Index theo nhóm

Đây chỉ là appendix để tra cứu sau khi đã hiểu mô hình tư duy (mental model) ở các phần trước. Không dùng section này như learning path và không học thuộc thuộc tính (property) theo kiểu danh sách.

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

## danh sách (list) / counters

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

## thuộc tính logic (logical properties)

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

# 115. bộ chọn (selector) Index cần thành thạo

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

- bộ chọn (selector) có quá rộng không?
- Có dựa vào DOM lồng cú pháp (nesting) fragile không?
- Có độ đặc hiệu (specificity) escalation không?
- Có `!important` không cần thiết không?
- Có global tác dụng phụ (side effect) không?
- Long text có break layout không?
- Loading trạng thái (state)/empty trạng thái (state)/error trạng thái (state) ổn không?

## Responsive

- 320px-ish narrow layout?
- Tablet?
- Wide screen?
- Content translated dài hơn?
- Zoom 200%?
- orientation change?
- component trong container khác?

## khả năng tiếp cận (accessibility)

- focus visible?
- keyboard?
- giảm chuyển động (reduced motion)?
- độ tương phản cao (high contrast)?
- trạng thái (state) không chỉ dựa vào color?
- visual order = logical order?

## hiệu năng (performance)

- animation thuộc tính (property) hợp lý?
- có giant shadow/filter/backdrop blur trên vùng lớn?
- unused CSS?
- font weights thừa?
- image dimensions reserved?

## kiến trúc (architecture)

- dùng token thay hard-code khi mang tính ngữ nghĩa (semantic)?
- component trạng thái (state) API rõ?
- tiện ích (utility)/component responsibility rõ?
- layer đúng?
- có thể override mà không cuộc chiến độ đặc hiệu (specificity war)?

---

# 118. Những phản mẫu (anti-pattern) cần bỏ

## 1. `!important` everywhere

Sai:

```css
.btn {
  color: red !important;
}
```

Hãy sửa cơ chế phân tầng (cascade) kiến trúc (architecture).

## 2. Magic z-index

```css
z-index: 999999999;
```

Không sửa được ngữ cảnh xếp chồng (stacking context) cha.

## 3. Fixed pixel everything

```css
width: 1200px;
height: 600px;
```

Dễ phá responsive/zoom/content.

## 4. DOM-coupled bộ chọn (selector)

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

## 8. truy vấn môi trường (media query) theo device names

```css
@media (...) /* iPhone 14 */
```

Hãy chọn điểm ngắt (breakpoint) theo content/layout, không theo tên thiết bị.

## 9. JavaScript cho vấn đề CSS giải được

Ví dụ nhiều layout responsive/trạng thái (state) hiện có thể dùng:
- `:has()`
- truy vấn vùng chứa (container query)
- Grid
- `clamp()`
- native lồng cú pháp (nesting)
- định vị theo điểm neo (anchor positioning).

---

# 119. Học CSS như senior: 20 bài tập bắt buộc

1. Recreate card từ screenshot không dùng framework.
2. Navbar responsive bằng Flexbox.
3. Dashboard layout bằng Grid.
4. Product grid auto-fit không điểm ngắt (breakpoint).
5. Sticky header + sticky sidebar.
6. Modal scroll đúng khi content dài.
7. Truncate text trong flex child.
8. Table responsive.
9. Form validation styles.
10. Accessible focus các trạng thái (states).
11. Dark theme bằng custom các thuộc tính (properties).
12. token thiết kế (design token) system.
13. Component responsive bằng truy vấn vùng chứa (container query).
14. Tooltip/dropdown với định vị theo điểm neo (anchor positioning) + phương án dự phòng (fallback).
15. Card row alignment bằng subgrid.
16. Animation respect giảm chuyển động (reduced motion).
17. Scroll snap carousel.
18. Scroll-driven reading progress.
19. Native CSS lồng cú pháp (nesting) refactor.
20. `@layer` refactor project có vendor CSS.

---

# 120. Roadmap 30 ngày

## Ngày 1–3 — Core mechanics

Học:
- syntax,
- các bộ chọn (selectors),
- cơ chế phân tầng (cascade),
- độ đặc hiệu (specificity),
- kế thừa (inheritance),
- các giá trị (values)/units.

Output:
- 20 bộ chọn (selector) examples,
- độ đặc hiệu (specificity) playground.

## Ngày 4–6 — Box/layout fundamentals

Học:
- mô hình hộp (box model),
- sizing,
- display,
- luồng bố cục thông thường (normal flow),
- overflow.

Output:
- article layout,
- cards,
- truncation cases.

## Ngày 7–9 — Positioning

Học:
- relative/absolute/fixed/sticky,
- khối chứa tham chiếu (containing block),
- z-index,
- ngữ cảnh xếp chồng (stacking context).

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
- các truy vấn môi trường (media queries),
- user preferences,
- các truy vấn vùng chứa (container queries).

## Ngày 22–23 — Motion

Học:
- transforms,
- transition,
- keyframes,
- scroll snap,
- giảm chuyển động (reduced motion).

## Ngày 24–25 — Tokens & kiến trúc (architecture)

Học:
- custom các thuộc tính (properties),
- `@property`,
- naming,
- layers,
- component trạng thái (state).

## Ngày 26–27 — Modern CSS

Học:
- lồng cú pháp (nesting),
- `:has()`,
- `@scope`,
- định vị theo điểm neo (anchor positioning),
- chuyển cảnh giao diện (view transitions),
- hoạt ảnh điều khiển bằng cuộn (scroll-driven animations),
- modern colors.

## Ngày 28 — khả năng tiếp cận (accessibility)

Test:
- keyboard,
- zoom,
- focus,
- giảm chuyển động (reduced motion),
- contrast,
- RTL/logical props.

## Ngày 29 — hiệu năng (performance)/gỡ lỗi (debugging)

DevTools:
- Computed styles,
- Flex/Grid overlay,
- Layers,
- hiệu năng (performance),
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

Sau khi nắm CSS này, tài liệu SCSS không cần lặp lại Flex/Grid/mô hình hộp (box model).

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

vẫn tồn tại trong browser thời gian chạy (runtime) và override được.

---

# 122. Kiến thức bạn phải giải thích được nếu muốn tự đánh giá "Senior CSS"

Bạn nên trả lời rõ được các câu sau:

1. cơ chế phân tầng (cascade) chọn rule thắng như thế nào?
2. `:is()` và `:where()` khác độ đặc hiệu (specificity) ra sao?
3. Tại sao `z-index:999999` vẫn có thể nằm dưới element khác?
4. khối chứa tham chiếu (containing block) của absolute/fixed được xác định thế nào?
5. Tại sao phần tử Flex (flex item) cần `min-width:0`?
6. `1fr` khác `minmax(0,1fr)` trong edge case nào?
7. `auto-fit` và `auto-fill` khác nhau thế nào?
8. Grid khác Flex theo mô hình tư duy (mental model) nào?
9. Tại sao `height:100%` thường "không chạy"?
10. gộp lề (margin collapse) là gì?
11. `overflow:hidden` ảnh hưởng scroll/sticky như thế nào?
12. BFC/ngữ cảnh định dạng (formatting context) giải quyết vấn đề gì?
13. ngữ cảnh xếp chồng (stacking context) được tạo bởi những gì?
14. truy vấn vùng chứa (container query) tốt hơn truy vấn môi trường (media query) ở trường hợp nào?
15. `rem`, `em`, `dvh`, `cqi` dùng khi nào?
16. `min-content`, `max-content`, `fit-content` là gì?
17. `@layer` giải quyết độ đặc hiệu (specificity) kiến trúc (architecture) thế nào?
18. `@scope` khác CSS Modules/Shadow DOM (cây DOM đóng gói) như thế nào về concept?
19. `@property` hơn custom thuộc tính (property) thường ở đâu?
20. `oklch()` có lợi gì cho hệ thống thiết kế (design system)?
21. CSS lồng cú pháp (nesting) native khác SCSS lồng cú pháp (nesting) về thời gian chạy (runtime)/build tooling thế nào?
22. Animation nào dễ gây layout/chi phí vẽ (paint cost)?
23. `opacity:0`, `visibility:hidden`, `display:none` khác nhau gì?
24. Focus khả năng tiếp cận (accessibility) nên style thế nào?
25. thuộc tính logic (logical properties) giải quyết vấn đề gì?
26. Khi nào nên dùng `contain`/`content-visibility`?
27. Cách gỡ lỗi (debug) sticky?
28. Cách gỡ lỗi (debug) text overflow trong flex/grid?
29. Cách thiết kế token thiết kế (design tokens)?
30. Cách chia layer/components/các tiện ích (utilities) để không cuộc chiến độ đặc hiệu (specificity war)?

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

# 124. Appendix — syntax recap cực ngắn

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

## 125.5 Cover vùng nhìn (viewport)

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

## 125.21 trạng thái (state) via data attribute

```css
.panel[data-state="open"] {}
```

## 125.22 mang tính ngữ nghĩa (semantic) trạng thái (state) via ARIA

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

## 125.24 giảm chuyển động (reduced motion)

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

## 126.2 trạng thái (state) Attribute Pattern

JS/trạng thái (state) layer:

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

Useful khi muốn expose mang tính ngữ nghĩa (semantic) component slots.

## 126.4 biến thể (variant) Pattern

```css
.button[data-variant="primary"] {}
.button[data-variant="secondary"] {}
.button[data-variant="danger"] {}
```

## 126.5 Size biến thể (variant) Pattern

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

## 126.8 cải tiến lũy tiến (progressive enhancement) Pattern

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

## 126.9 Container-responsive mẫu thành phần (component pattern)

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

## 126.10 trạng thái (state) + Transition Pattern

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

## 126.11 mang tính ngữ nghĩa (semantic) CSS API Pattern

Expose:
- `data-variant`,
- `data-size`,
- mang tính ngữ nghĩa (semantic)/ARIA trạng thái (state),
- selected custom thuộc tính (property) hooks.

Không expose internal DOM depth như API.

---

# 127. Catalog — CSS Design / kiến trúc (architecture) Patterns

## 127.1 Layered cơ chế phân tầng (cascade) Pattern

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

## 127.2 phân cấp token (token hierarchy) Pattern

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

## 127.4 đóng gói (encapsulation) Pattern

Mức cô lập (isolation) tăng dần:

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

Không duplicate thành `.special-card-special`.

## 127.6 Theme-by-contract Pattern

```css
[data-theme="dark"] {
  --surface-default: #111;
  --text-default: #fff;
}
```

Components consume mang tính ngữ nghĩa (semantic) tokens.

## 127.7 quyền sở hữu hành vi đáp ứng (responsive ownership) Pattern

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
- không color-only trạng thái (state),
- reduced-motion compatible.

Visual enhancement đến sau.

## 127.10 bố cục theo ràng buộc (constraint-driven layout) Pattern

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

CSS hiện đại (`min`, `max`, `clamp`, Grid, truy vấn vùng chứa (container query)) hỗ trợ cách nghĩ này tốt hơn.

---

# 128. Senior Pattern map khóa–giá trị (map) — thuộc tính (property) nào thường đi cùng thuộc tính (property) nào

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

# 129. Khi nào Pattern trở thành phản mẫu (anti-pattern)?

## BEM

Tốt khi:
- global/plain CSS,
- cần explicit naming.

Có thể dư khi:
- CSS Modules/Shadow DOM (cây DOM đóng gói) đã phạm vi (scope).

## tiện ích (utility) classes

Tốt khi:
- design constraints rõ,
- team quen composition.

Có thể xấu khi:
- tiện ích (utility) naming tùy tiện,
- không có token system,
- dùng tiện ích (utility) để encode business trạng thái (state).

## lồng cú pháp (nesting)

Tốt:
- các trạng thái (states),
- các phần tử giả (pseudo-elements),
- local media/truy vấn vùng chứa (container query).

Xấu:
- phản chiếu toàn bộ DOM tree.

## Custom các thuộc tính (properties)

Tốt:
- thời gian chạy (runtime) theme,
- giao diện thành phần (component API),
- mang tính ngữ nghĩa (semantic) tokens.

Xấu:
- hàng trăm các biến (variables) không có ngữ nghĩa (semantics),
- abstraction cho giá trị (value) chỉ dùng một lần.

## `@layer`

Tốt:
- codebase lớn,
- vendor CSS,
- predictable cơ chế phân tầng (cascade).

Có thể overkill:
- một component/file cực nhỏ.

## truy vấn vùng chứa (container query)

Tốt:
- reusable component ở nhiều container.

Không cần thiết:
- page-level điểm ngắt (breakpoint) đơn giản.

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
- bộ chọn (selector),
- cơ chế phân tầng (cascade),
- mô hình hộp (box model),
- typography,
- spacing,
- Flexbox,
- Grid cơ bản,
- responsive truy vấn môi trường (media query).

Patterns cần nhớ:
- container,
- stack,
- cluster,
- center,
- truncate,
- responsive image.

## Intermediate

Phải hiểu:
- định cỡ nội tại (intrinsic sizing),
- min/max constraints,
- sticky,
- ngữ cảnh xếp chồng (stacking context),
- Grid placement,
- custom các thuộc tính (properties),
- component các biến thể (variants),
- các truy vấn vùng chứa (container queries).

Patterns cần biết:
- media object,
- sidebar,
- auto-grid,
- token override,
- trạng thái (state) attribute,
- responsive component.

## Senior

Phải thiết kế được:
- cơ chế phân tầng (cascade) kiến trúc (architecture),
- phân cấp token (token hierarchy),
- giao diện thành phần (component API),
- phạm vi (scope)/layer strategy,
- khả năng tiếp cận (accessibility) behavior,
- hiệu năng (performance) strategy,
- browser phương án dự phòng (fallback),
- gỡ lỗi (debugging) methodology.

Patterns cần thành thạo:
- layered cơ chế phân tầng (cascade),
- mang tính ngữ nghĩa (semantic) tokens,
- composition primitives,
- quyền sở hữu hành vi đáp ứng (responsive ownership),
- overlay ownership,
- cải tiến lũy tiến (progressive enhancement),
- bố cục theo ràng buộc (constraint-driven layout).

---

---

# 132. cơ chế phân tầng (cascade) & độ đặc hiệu (specificity) — trace quyết định khai báo (declaration) thắng [CORE/SENIOR]

Một trong những sai lầm phổ biến nhất khi học CSS là coi độ đặc hiệu (specificity) như “định luật cao nhất”. Trên thực tế, browser chỉ so độ đặc hiệu (specificity) sau khi đã loại những khai báo (declaration) không cùng precedence. Vì vậy một bộ chọn (selector) rất mạnh vẫn có thể thua rule ở origin/layer/importance khác. mô hình tư duy (mental model) tốt hơn là coi cơ chế phân tầng (cascade) như một chuỗi bộ lọc.

Giả sử cùng một `button` nhận nhiều rule từ reset, component CSS, tiện ích (utility) layer và inline style. Browser trước tiên xét rule có relevant với element/media condition hay không. Sau đó nó xét origin và `!important`, rồi lớp phân tầng (cascade layer). Chỉ những khai báo (declaration) còn cùng tầng precedence mới so độ đặc hiệu (specificity); nếu vẫn bằng nhau thì độ gần phạm vi (scope proximity) có thể tham gia với `@scope`, cuối cùng mới đến thứ tự nguồn (source order).

```text
relevance
→ origin + importance
→ cascade layer
→ specificity
→ scoping proximity
→ source order
```

Điểm thực tế quan trọng là `@layer` cho phép bạn thay đổi precedence mà không tăng bộ chọn (selector) strength. Nếu `components` đứng trước `utilities`, một tiện ích (utility) bộ chọn (selector) đơn giản có thể override component rule dù component bộ chọn (selector) nhìn “dài” hơn. Đây là lý do kiến trúc (architecture) cơ chế phân tầng (cascade) tốt bền hơn việc nối thêm class/ID vào bộ chọn (selector).

độ đặc hiệu (specificity) của các lớp giả (pseudo-class) hiện đại cũng cần hiểu theo cơ chế chứ không học số rời rạc. `:where()` luôn đóng góp độ đặc hiệu (specificity) bằng 0, vì vậy rất phù hợp cho defaults. `:is()`, `:not()` và `:has()` lấy độ đặc hiệu (specificity) từ bộ chọn (selector) có độ đặc hiệu (specificity) cao nhất trong argument danh sách (list). Điều này có thể làm một rule mạnh hơn bạn tưởng nếu vô tình đưa ID vào argument.

```css
/* phần :where(...) không tăng specificity */
:where(.article) h2 {
  margin-block: 2rem 1rem;
}

/* specificity chịu ảnh hưởng bởi #app trong :is(...) */
:is(.page, #app) .title {
  color: var(--heading);
}
```

Khi cần override, hãy sửa đúng tầng. Nếu vấn đề là layer order, sửa `@layer`; nếu bộ chọn (selector) quá mạnh, giảm độ đặc hiệu (specificity); nếu trạng thái (state) thuộc component, dùng attribute/biến thể (variant) rõ; nếu third-party CSS dùng `!important`, isolate nó vào layer hoặc integration boundary. `!important` không phải công cụ đầu tiên vì nó đổi một khai báo (declaration) sang một precedence class khác và dễ tạo cuộc chiến mới.

Một production gỡ lỗi (debugging) trace nên bắt đầu trong DevTools: xác nhận bộ chọn (selector) match, xem khai báo (declaration) nào bị crossed-out, nhìn layer/origin, rồi mới tính độ đặc hiệu (specificity). Nếu bạn đang tính độ đặc hiệu (specificity) trước khi biết layer nào đang thắng, bạn đang gỡ lỗi (debug) sai thứ tự.

---

# 133. Layout mô hình tư duy (mental model) — từ không gian khả dụng (available space) tới geometry [CORE/SENIOR]

Layout không phải “đặt `width`, rồi browser vẽ đúng con số đó”. Browser phải giải một hệ constraints. Mỗi box có intrinsic contribution từ content, min/max constraints, preferred size, không gian khả dụng (available space) từ khối chứa tham chiếu (containing block) và rules của ngữ cảnh định dạng (formatting context). Flexbox và Grid chỉ là hai các thuật toán bố cục (layout algorithms) khác nhau chạy trên cùng những inputs cơ bản đó.

Một cách đọc layout hữu ích là:

```text
box được tạo bởi display nào?
→ formatting context nào đang quản lý children?
→ containing block / available size là gì?
→ intrinsic min/max-content contributions là gì?
→ min/max/width/height/aspect-ratio giới hạn ra sao?
→ algorithm phân phối free space như thế nào?
→ overflow/clipping/scroll xảy ra ở đâu?
```

Ví dụ `width: 100%` không đảm bảo element vừa màn hình. Nếu parent có padding theo `content-box`, child có min-content lớn, hoặc child là flex/phần tử Grid (grid item) với kích thước tối thiểu tự động (automatic minimum size), geometry cuối cùng có thể overflow. Ngược lại, một element không có explicit width vẫn có thể có size rất cụ thể do dải lưới (grid track) hoặc Flex algorithm quyết định.

luồng bố cục thông thường (normal flow) là đường cơ sở (baseline). Block boxes thường xếp theo block flow; inline content tạo các hộp dòng (line boxes). Khi `display:flex` hoặc `display:grid` xuất hiện, children trực tiếp trở thành flex/các phần tử Grid (grid items) và sizing rules thay đổi. Khi `position:absolute` xuất hiện, box rời luồng bố cục thông thường (normal flow) và geometry phụ thuộc khối chứa tham chiếu (containing block) mới. Vì vậy “thuộc tính (property) nào đang sai?” thường là câu hỏi kém hơn “algorithm nào đang quyết định geometry này?”.

định cỡ nội tại (intrinsic sizing) là chìa khóa của nhiều bug senior. `min-content` mô tả kích thước nhỏ nhất content có thể co theo wrapping rules; `max-content` mô tả size content muốn có nếu không wrap; `fit-content` nằm giữa intrinsic desire và không gian khả dụng (available space). `minmax(0, 1fr)` trong Grid và `min-width:0` trong Flex đều là cách nói với browser rằng content được phép co nhỏ hơn automatic intrinsic minimum trong những context cụ thể.

---

# 134. Flexbox — đọc algorithm thay vì thuộc thuộc tính (property) [CORE/SENIOR]

Flexbox giải bài toán một chiều. Browser xác định trục chính (main axis) từ `flex-direction`, lấy flex base size của từng item, so tổng hypothetical size với available main-axis space, rồi quyết định đang có positive không gian dư (free space) hay negative không gian dư (free space). Sau đó `flex-grow` hoặc `flex-shrink` phân phối phần dư/thiếu theo factor và constraints.

Vì thế `flex: 1` không đơn giản có nghĩa “chiếm 100%”. Nó thay grow/shrink/basis để item tham gia phân phối space. Hai item `flex:1` thường chia không gian dư (free space) cân bằng, nhưng intrinsic min-size vẫn có thể chặn item co. Đây là lý do pattern production rất thường là:

```css
.row {
  display: flex;
  gap: 1rem;
}

.avatar {
  flex: none;
}

.body {
  flex: 1;
  min-width: 0;
}
```

`min-width:0` không phải mẹo Tailwind/CSS bí ẩn; nó thay mức tối thiểu tự động (automatic minimum) constraint để phần tử Flex (flex item) được phép co và để `overflow`, `text-overflow` hoặc child wrapping phát huy tác dụng.

Cross-axis alignment được tính sau main-axis sizing và phụ thuộc `align-items`, `align-self`, đường cơ sở (baseline) rules và available cross size. `justify-content` chỉ phân phối remaining không gian dư (free space) trên trục chính (main axis); nếu items đã grow lấp hết không gian dư (free space) thì `justify-content:space-between` không tạo thêm “ma thuật”. Vì vậy khi alignment không như mong đợi, trước tiên xác định axis và không gian dư (free space) có thật sự tồn tại hay không.

Senior pattern là dùng Flex cho composition một chiều như toolbar, cluster, media object, action row. Nếu bạn bắt đầu điều khiển nhiều row/column alignment đồng thời bằng width calc, margin và order, hãy kiểm tra xem Grid có đúng mô hình tư duy (mental model) hơn không.

---

# 135. Grid — định cỡ dải lưới (track sizing) trước, placement sau [CORE/SENIOR]

Grid mạnh vì browser giải tracks trước rồi đặt items vào hệ tracks đó. Bạn nên đọc Grid theo thứ tự: explicit grid được định nghĩa thế nào, implicit tracks nào có thể phát sinh, intrinsic contributions của items ảnh hưởng định cỡ dải lưới (track sizing) ra sao, sau đó mới nhìn item placement.

`1fr` không đơn giản là “một phần trăm”. Fraction unit phân phối **không gian dư (free space) còn lại** sau khi fixed/intrinsic constraints đã được giải. Vì phần tử Grid (grid item) có mức tối thiểu tự động (automatic minimum) contribution, `1fr` đôi khi không co nhỏ như bạn kỳ vọng. `minmax(0, 1fr)` mở minimum xuống 0 và vì thế là pattern an toàn cho content area có thể chứa text dài hoặc nested layout.

```css
.shell {
  display: grid;
  grid-template-columns: 16rem minmax(0, 1fr);
}
```

`repeat(auto-fit, minmax(min(100%, 18rem), 1fr))` là ví dụ rất tốt của intrinsic thiết kế đáp ứng (responsive design). Không cần đoán “tablet điểm ngắt (breakpoint)”; browser tự tạo số track vừa với không gian khả dụng (available space) và collapse empty tracks. Đây là responsive layout do constraints quyết định, không phải do device categories.

Grid placement (`grid-column`, named areas, spans) nên được dùng sau khi track system đã rõ. `grid-auto-flow:dense` có thể backfill visual gaps nhưng có thể làm visual order khác DOM order, nên không phù hợp khi thứ tự tương tác/đọc có ý nghĩa. Subgrid phù hợp khi nested component cần chia sẻ parent tracks thay vì duplicate width constants.

---

# 136. Responsive — quyết định bằng constraint, không bằng tên thiết bị [CORE/SENIOR]

thiết kế đáp ứng (responsive design) tốt bắt đầu từ content và không gian khả dụng (available space). Trước khi thêm truy vấn môi trường (media query), hãy xem layout có thể tự thích ứng bằng wrapping, định cỡ nội tại (intrinsic sizing), `min()`, `max()`, `clamp()`, `auto-fit` hoặc Flex/Grid hay không. Query nên xuất hiện khi **behavior cần đổi**, không phải vì vùng nhìn (viewport) chạm một tên device.

truy vấn môi trường (media query) phù hợp với page/environment-level concerns: vùng nhìn (viewport) size, orientation, hover capability, pointer precision, giảm chuyển động (reduced motion), color scheme hoặc print. truy vấn vùng chứa (container query) phù hợp khi một reusable component cần biết không gian nó thực sự nhận được trong sidebar, modal hoặc main content. Hai loại query có thể dùng cùng nhau nhưng ownership phải rõ: page shell thường theo vùng nhìn (viewport), component internals thường theo container.

```css
.dashboard {
  display: grid;
  gap: 1rem;
}

@media (width >= 64rem) {
  .dashboard {
    grid-template-columns: 18rem minmax(0, 1fr);
  }
}

.widget-host {
  container-type: inline-size;
}

@container (width >= 32rem) {
  .widget {
    grid-template-columns: auto minmax(0, 1fr);
  }
}
```

Đừng quên responsive còn gồm zoom, translated text, user font size, coarse pointer, keyboard, giảm chuyển động (reduced motion) và dynamic vùng nhìn (viewport). Một layout chỉ đẹp ở ba screenshot width chưa thể gọi là robust responsive UI.

---

# 137. Modern CSS — adoption strategy thay vì chạy theo feature [ADV/MODERN]

Modern CSS hiện đã có nhiều công cụ từng cần preprocessor hoặc JavaScript: native lồng cú pháp (nesting), `:has()`, các lớp phân tầng (cascade layers), `@scope`, các truy vấn vùng chứa (container queries), subgrid, thuộc tính logic (logical properties), `@property`, định vị theo điểm neo (anchor positioning), lớp trên cùng (top layer), popover/dialog styling, hoạt ảnh điều khiển bằng cuộn (scroll-driven animations) và chuyển cảnh giao diện (view transitions). Cách học đúng không phải ghi nhớ release danh sách (list) mà hiểu **vấn đề cũ nào được thay thế**.

các lớp phân tầng (cascade layers) thay độ đặc hiệu (specificity) conventions; các truy vấn vùng chứa (container queries) giảm component các điểm ngắt (breakpoints) phụ thuộc vùng nhìn (viewport); `:has()` giảm trạng thái (state) class chỉ để style DOM relationship; native lồng cú pháp (nesting) giảm một phần nhu cầu SCSS lồng cú pháp (nesting); thuộc tính logic (logical properties) giảm hard-coded LTR assumptions; lớp trên cùng (top layer) giải nhiều stacking problems của modal/popover; định vị theo điểm neo (anchor positioning) giảm manual coordinate JS cho overlay trong mức hỗ trợ trình duyệt (browser support) phù hợp.

Production adoption nên chia feature thành ba nhóm. Nhóm critical-layout phải có browser đường cơ sở (baseline) phù hợp hoặc phương án dự phòng (fallback) rõ. Nhóm enhancement như balanced text, visual transitions hay scroll-driven decoration có thể progressive enhance. Nhóm experimental/rapidly evolving phải được feature-query/test trước khi trở thành foundation của hệ thống thiết kế (design system).

`@supports` không phải công cụ để bọc mọi thuộc tính (property) mới. Nếu unsupported browser đơn giản ignore khai báo (declaration) và phương án dự phòng (fallback) tự nhiên vẫn usable, bạn không cần query. Dùng truy vấn hỗ trợ tính năng (feature query) khi cần thay **một strategy hoàn chỉnh** tùy support.

---

# 138. hiệu năng (performance) + khả năng tiếp cận (accessibility) là layout constraints, không phải bước cuối [SENIOR]

hiệu năng (performance) và khả năng tiếp cận (accessibility) thường bị đặt cuối checklist, nhưng chúng ảnh hưởng design decision từ đầu. Một fixed-height card có thể đẹp với sample text nhưng cắt content khi zoom 200%. Visual reorder bằng `order`/Grid placement có thể làm keyboard/screen-reader order khác visual order. `opacity:0` có thể giấu hình nhưng để focus target tồn tại. Heavy backdrop blur trên full vùng nhìn (viewport) có thể đẹp nhưng tốn paint/composite cost trên mobile.

Motion nên bắt đầu từ mang tính ngữ nghĩa (semantic) trạng thái (state) và có reduced-motion path. Interactive control phải có visible focus và target size phù hợp. Component phải chịu được long content, locale khác, màu cưỡng bức (forced colors)/độ tương phản cao (high contrast) và font loading. Đây là functional correctness, không phải optional polish.

Về hiệu năng (performance), hãy đo invalidation. Thay đổi font metrics có thể gây layout; thay `width`/`height` trong animation thường kéo geometry recalculation; large shadows/filters tăng paint; quá nhiều promoted layers tăng memory. `transform`/`opacity` thường compositor-friendly nhưng không phải miễn phí. `contain`, `content-visibility` và `will-change` chỉ nên dùng khi bạn hiểu tác dụng phụ (side effect) và đã đo bottleneck.

---

# 139. các mẫu dùng trong production (production patterns) — compose behavior từ primitives [SENIOR]

Production CSS nên có một vocabulary nhỏ nhưng mạnh thay vì hàng trăm component rules trùng nhau. `Stack` biểu diễn vertical rhythm bằng column flex + gap. `Cluster` biểu diễn inline group có wrap. `Container` chịu horizontal constraint. `Sidebar` dùng Grid/Flex với một fixed/intrinsic region và `minmax(0,1fr)` cho content. `Media Object` giữ media không shrink và body có `min-width:0`. App shell vertical dùng `min-height:100dvh`, fixed header region và `min-height:0; overflow:auto` cho body.

Overlay cũng cần ownership rõ. Decoration local dùng positioned ancestor + absolute child. Sticky controls dùng `position:sticky` và vùng chứa cuộn (scroll container) rõ. Modal/popover critical nên ưu tiên native top-layer primitives khi ngữ nghĩa (semantics) phù hợp thay vì đẩy `z-index` lên vô hạn. Theme nên đi qua mang tính ngữ nghĩa (semantic) custom các thuộc tính (properties) để component không duplicate dark/light rules. Component trạng thái (state) nên đi qua native lớp giả (pseudo-class), ARIA trạng thái (state) hoặc `data-*` contract thay vì class tên theo từng combination.

Một pattern chỉ đáng dùng khi nó làm constraints và ownership dễ đọc hơn. Nếu abstraction khiến developer phải mở ba file để biết `padding` cuối cùng đến từ đâu, hãy giảm abstraction. Senior CSS không tối đa số pattern; senior CSS tối đa khả năng dự đoán behavior.

---

# Kết luận

Để lên senior CSS, mục tiêu không phải là nhớ 500 thuộc tính (property).

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
