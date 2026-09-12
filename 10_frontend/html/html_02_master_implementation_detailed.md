# HTML — Master Implementation
## Browser parsing, form internals, advanced accessibility, DOM edge cases và modern declarative HTML

Tài liệu này tiếp nối `html_01_beginner_to_senior_detailed.md`. Nếu file đầu giúp bạn viết HTML production đúng và có semantic, file này tập trung vào phần mà nhiều frontend developer chỉ chạm tới khi debug edge case, làm component library, xử lý SSR/hydration, xây design system hoặc review security/accessibility ở mức senior.

Mục tiêu của phần Master không phải là thuộc mọi element lạ trong HTML Living Standard. Mục tiêu là hiểu **platform behavior**: browser parser có thể sửa markup ra sao, form owner/submitter hoạt động thế nào, DOM property có thể bị clobber bởi `name`, Shadow DOM và custom elements gắn với HTML ra sao, native dialog/popover có top-layer semantics gì, và các feature HTML mới nên được dùng theo progressive enhancement như thế nào.

---

# PHẦN 1 — NHỮNG ELEMENT ÍT GẶP NHƯNG CẦN BIẾT

## 1. `<search>`

`search` là semantic container cho search hoặc filtering controls.

```html
<search>
  <form action="/search" method="get">

    <label for="q">
      Search
    </label>

    <input
      id="q"
      name="q"
      type="search">

    <button type="submit">
      Search
    </button>

  </form>
</search>
```

Điểm quan trọng là `search` không tự thực hiện search. Nó chỉ nói với browser/accessibility semantics rằng subtree này đại diện cho search/filter functionality.

Một filter panel cũng có thể dùng `search` nếu chức năng thực tế là tìm/lọc dataset.

Senior nên xem đây là landmark semantic bổ sung, không phải một replacement cho `form`.

---

## 2. `<hgroup>`

`hgroup` dùng để group một heading chính với supporting text như subtitle/tagline.

```html
<hgroup>
  <h1>HTML Platform</h1>
  <p>From semantic markup to browser behavior</p>
</hgroup>
```

Đừng dùng `hgroup` để nhóm cả hierarchy:

```html
<hgroup>
  <h1>Page</h1>
  <h2>Section</h2>
  <h3>Subsection</h3>
</hgroup>
```

Heading hierarchy vẫn phải được thể hiện bằng document structure.

---

## 3. `<menu>`

`menu` hiện đại đại diện cho một list of commands/items:

```html
<menu>
  <li>
    <button type="button">Copy</button>
  </li>

  <li>
    <button type="button">Paste</button>
  </li>
</menu>
```

Trong thực tế `ul` vẫn phổ biến hơn. Điều cần biết là `menu` hiện tại không nên bị nhầm với những context-menu APIs legacy trước đây.

---

## 4. `<wbr>`

`wbr` tạo một **word break opportunity**, tức là browser được phép xuống dòng tại điểm đó nếu cần.

```html
<p>
  verylong<wbr>generated<wbr>identifier
</p>
```

Khác với `<br>`, `wbr` không bắt buộc line break.

Use case thực tế gồm URL dài, hash, technical identifier hoặc generated text.

---

## 5. `<dfn>`

`dfn` đánh dấu nơi một thuật ngữ được **định nghĩa**.

```html
<p>
  <dfn>Hydration</dfn>
  là quá trình client JavaScript kết nối behavior với HTML đã render từ server.
</p>
```

Không dùng chỉ để bold/italic một keyword. Nó có semantics “đây là defining instance của term”.

---

## 6. `<u>`

`u` không đơn giản nghĩa “underline”.

Nó biểu diễn non-textual annotation, ví dụ spelling annotation theo convention.

```html
<p>
  <u class="spelling-error">
    recieve
  </u>
</p>
```

Nếu bạn chỉ muốn underline vì design, hãy dùng CSS.

Underline có UX risk vì user thường associate underline với hyperlink, nên phải có lý do rõ.

---

## 7. `<map>` và `<area>`

Image map cho phép một image có nhiều clickable regions.

```html
<img
  src="/office-map.png"
  alt="Office floor plan"
  usemap="#office-map">

<map name="office-map">

  <area
    shape="rect"
    coords="0,0,200,200"
    href="/meeting-room"
    alt="Meeting room">

  <area
    shape="circle"
    coords="300,100,60"
    href="/cafeteria"
    alt="Cafeteria">

</map>
```

`shape` thường có `rect`, `circle`, `poly` hoặc `default`.

`coords` chứa coordinates tương ứng.

Feature này hiện ít dùng trong modern responsive UI vì scaling/accessibility phức tạp, nhưng senior cần nhận diện khi maintain old apps hoặc map diagrams.

---

## 8. `<canvas>`

Canvas là bitmap drawing surface được điều khiển chủ yếu bằng JavaScript.

```html
<canvas
  id="chart"
  width="800"
  height="400">
  Sales chart
</canvas>
```

Một điểm quan trọng là `width`/`height` HTML attributes định nghĩa **drawing buffer dimensions**.

Nếu chỉ CSS resize:

```css
canvas {
  width: 800px;
  height: 400px;
}
```

nhưng intrinsic drawing buffer có dimensions khác, canvas có thể bị blur/stretch.

Canvas pixels không tự tạo accessible semantics. Nếu chart biểu diễn dữ liệu quan trọng, hãy cung cấp alternative text/table/DOM representation phù hợp.

---

## 9. Inline SVG

HTML có thể embed SVG trực tiếp:

```html
<svg
  viewBox="0 0 24 24"
  aria-hidden="true">

  <path d="..."></path>

</svg>
```

SVG subtree thuộc SVG namespace, không phải HTML namespace.

Điều này quan trọng khi xử lý parser, DOM APIs, element names và attributes.

Decorative icon nên tránh làm screen reader đọc noise:

```html
<svg aria-hidden="true">
```

Nếu SVG mang meaning độc lập, cần accessible naming strategy.

---

## 10. MathML

HTML có thể embed MathML:

```html
<math>
  <mrow>
    <mi>x</mi>
    <mo>=</mo>
    <mn>10</mn>
  </mrow>
</math>
```

Giống SVG, MathML là foreign content có namespace/data model riêng.

Điểm quan trọng không phải bạn phải học toàn MathML, mà phải hiểu HTML document có thể chuyển parser context vào foreign namespaces.

---

# PHẦN 2 — HTML SYNTAX VÀ PARSER MASTERY

## 11. HTML không phải XML

HTML source:

```html
<img src="/a.png" alt="">
```

`img` là void element.

Bạn có thể thấy:

```html
<img src="/a.png" alt="" />
```

nhưng slash không biến document `text/html` thành XML.

HTML parsing mode được quyết định bởi MIME/context và HTML parsing algorithm.

Đây là khác biệt quan trọng nếu bạn vừa học XML: đừng mang XML self-closing rules vào ordinary HTML.

---

## 12. Optional end tags

HTML syntax cho phép omit một số end tags trong conditions cụ thể.

Ví dụ:

```html
<ul>
  <li>A
  <li>B
</ul>
```

Browser vẫn có thể tạo hai list items.

Tuy nhiên production application code nên thường viết explicit closing tags vì readability, formatter compatibility và SSR stability.

HTML minifier có thể omit theo spec; developer source không cần tối ưu vài bytes bằng cách làm code khó đọc.

---

## 13. `<p>` auto-closing behavior

Xét source:

```html
<p>
  Hello
  <div>World</div>
</p>
```

Nhiều beginner nghĩ `div` nằm trong `p`.

Nhưng HTML content model/parser rules không cho `div` nằm như vậy. Browser có thể tự đóng `p` trước `div`.

Resulting DOM có thể gần:

```html
<p>Hello</p>

<div>World</div>

<p></p>
```

tùy parse context.

Điều này giải thích nhiều hydration mismatch trong React SSR: JSX source nhìn nested nhưng browser parser đã sửa DOM trước khi React hydrate.

---

## 14. Browser error recovery

XML parser thường fail khi markup không well-formed.

HTML parser được thiết kế để repair rất nhiều malformed markup theo standardized algorithms.

Ví dụ tag đóng sai, table structure sai hoặc formatting elements misnested có thể vẫn tạo DOM.

Vì vậy “browser render được” không phải proof rằng HTML valid.

Validator và DOM inspection vẫn cần thiết.

---

## 15. Insertion modes

HTML parser có concept insertion modes, ví dụ:

```text
before html
in head
after head
in body
in table
in row
in cell
```

Parser behavior thay đổi theo context.

Cùng text/tag xuất hiện trong normal flow và table context có thể được xử lý khác.

Bạn không cần thuộc toàn state machine, nhưng senior phải biết HTML parser là context-sensitive.

---

## 16. Foster parenting

Table parsing có special error recovery.

Invalid content inside `table` có thể bị browser move ra ngoài table.

Ví dụ:

```html
<table>
  Some text

  <tr>
    <td>A</td>
  </tr>
</table>
```

Text placement trong resulting DOM có thể không giống indentation.

Concept này thường được gọi là foster parenting.

Use case thực tế: debug SSR hydration mismatch hoặc sanitizer/template output trong tables.

---

## 17. Adoption agency algorithm

HTML parser còn có algorithm đặc biệt cho misnested formatting elements như `b`, `i`, `em`, `strong` trong complex invalid markup.

Bạn không cần memorize algorithm.

Điều cần hiểu là malformed formatting markup có thể tạo tree rất khác source, và browser behavior là standardized chứ không random.

---

## 18. View Source, DOM và framework tree

Bạn cần phân biệt ba thứ.

**View Source** phản ánh original HTML response/source.

**DOM** là tree sau HTML parser repair/normalization và runtime mutations.

**Framework tree** là React/Vue/Svelte internal representation.

Khi hydration fail, hãy inspect cả ba.

Nếu server render invalid HTML, browser có thể sửa tree trước khi framework bắt đầu, khiến framework thấy DOM không khớp output nó dự kiến.

---

## 19. Raw text và RCDATA contexts

Một số HTML elements có parsing rules đặc biệt.

`script` và `style` thuộc nhóm raw-text-like contexts.

`title` và `textarea` có RCDATA-like behavior.

Điều này quan trọng khi embed untrusted/generated data. Escaping rule của text trong `div` không tự động áp dụng giống hệt trong `script`.

Security phải dùng context-aware encoding/safe serialization.

---

## 20. Character references

Common:

```text
&amp;   &
&lt;    <
&gt;    >
&quot;  "
&nbsp;  non-breaking space
```

`&nbsp;` không phải layout spacing tool.

Sai:

```html
Hello&nbsp;&nbsp;&nbsp;&nbsp;World
```

Dùng CSS `gap`, `margin`, `padding`.

`nbsp` chỉ hợp khi non-breaking behavior có meaning typography thực sự.

---

# PHẦN 3 — FORM INTERNALS

## 21. Form owner

Form-associated control có **form owner**.

Thông thường:

```html
<form id="profile">
  <input name="email">
</form>
```

Input thuộc ancestor form.

Nhưng control có thể nằm ngoài form:

```html
<form id="profile">
  ...
</form>

<input
  name="nickname"
  form="profile">
```

`form="profile"` associate input với form ID.

Use case thực tế là sticky footer action bar hoặc layout nơi button nằm ngoài DOM subtree của form.

---

## 22. Nested forms là invalid design

Đừng viết:

```html
<form>
  ...

  <form>
    ...
  </form>

</form>
```

Browser parser/form association rules không tạo “form trong form” theo cách developer thường tưởng.

Nếu cần sections independent, dùng sibling forms hoặc external controls với `form="id"`.

---

## 23. Submitter

Khi form submit bởi một button, button đó được gọi là **submitter**.

```html
<button
  type="submit"
  name="action"
  value="publish">
  Publish
</button>
```

Form data có thể bao gồm:

```text
action=publish
```

Submitter còn có thể override form settings:

```text
formaction
formmethod
formenctype
formtarget
formnovalidate
```

Đây là reason HTML native support multi-action forms rất tốt.

---

## 24. Implicit submission

Trong form có text controls, pressing Enter có thể trigger implicit submission tùy structure.

Nếu bạn có non-submit UI button nhưng quên:

```html
type="button"
```

default button behavior có thể submit form.

Đây là bug rất common.

Rule production đơn giản: mọi button trong form nên khai báo `type` rõ.

---

## 25. Successful controls

Khi form submit, không phải mọi control đều góp dữ liệu.

Control thường cần `name`.

```html
<input
  name="email"
  value="a@example.com">
```

sẽ tạo entry.

Control không có `name` thường không tạo form data entry.

Disabled controls thường bị loại.

Unchecked checkbox/radio thường không tạo entry.

Readonly input vẫn có thể submit.

Submitter button chỉ đóng góp value nếu chính nó trigger submit.

Hiểu successful controls giúp debug backend “tại sao field không gửi lên”.

---

## 26. Disabled vs readonly trong submission

Disabled:

```html
<input
  name="country"
  value="KR"
  disabled>
```

thường không được submit.

Readonly:

```html
<input
  name="country"
  value="KR"
  readonly>
```

thường vẫn submit.

Nếu backend cần account ID nhưng UI không cho sửa, `readonly` có thể giữ submission, nhưng bạn vẫn không được trust value đó về authorization. Client có thể sửa request.

---

## 27. Disabled `<fieldset>`

```html
<fieldset disabled>
  <legend>
    Account
  </legend>

  <input name="name">
</fieldset>
```

Controls trong disabled fieldset thường bị disabled.

Điểm edge case đáng biết là descendants nằm trong first `legend` có special behavior.

Ví dụ enable-edit button có thể đặt trong first legend để vẫn usable trong certain cases.

Bạn không cần dựa vào trick này hàng ngày, nhưng cần nhận diện khi debugging native forms.

---

## 28. Reset semantics

```html
<button type="reset">
  Reset
</button>
```

Reset không có nghĩa “set mọi field thành empty”.

Nó restore **default state**.

Input:

```html
<input value="Alice">
```

User sửa thành `Bob`.

Reset trở về `Alice`.

Checkbox:

```html
<input
  type="checkbox"
  checked>
```

User uncheck, reset trở về checked.

---

## 29. `value` vs `defaultValue`

```html
<input value="A">
```

DOM:

```js
input.value
input.defaultValue
```

`value` là current value.

`defaultValue` liên quan default/reset state.

Tương tự:

```js
checkbox.checked
checkbox.defaultChecked
```

và:

```js
option.selected
option.defaultSelected
```

Đây là cách browser bridge markup initial state với live UI state.

---

## 30. `dirname`

```html
<input
  name="comment"
  dirname="comment.dir">
```

Browser có thể submit text direction metadata kèm field.

Use case là international user-generated text.

Feature này niche nhưng cho thấy form model của HTML sâu hơn “name/value pairs”.

---

## 31. `capture`

```html
<input
  type="file"
  accept="image/*"
  capture="environment">
```

`capture` là mobile capture hint, không phải permission guarantee.

Values thường gặp:

```text
user
environment
```

Support/UX tùy device/browser.

---

# PHẦN 4 — NAMED ACCESS VÀ DOM CLOBBERING

## 32. DOM clobbering là gì?

HTML có historical named access behavior.

Một form control có `name` có thể xuất hiện như property trên form object.

Ví dụ:

```html
<form id="user-form">
  <input name="method">
</form>
```

Developer có thể nghĩ:

```js
form.method
```

luôn là HTTP form method.

Nhưng named form controls có thể collide/clobber built-in properties trong certain access patterns.

Đây không chỉ là code style issue; với untrusted markup, nó có thể góp phần tạo security vulnerabilities.

---

## 33. Tránh names đụng built-in members

Names như:

```text
method
action
submit
reset
elements
length
```

có thể gây confusion nếu code access properties trực tiếp.

Ví dụ old code:

```js
form.submit()
```

có thể gặp vấn đề nếu form chứa control `name="submit"` trong certain environments/patterns.

Safer architecture là dùng explicit APIs như:

```js
form.requestSubmit()
```

và:

```js
form.elements.namedItem("fieldName")
```

thay vì dựa quá nhiều vào named property magic.

---

## 34. Không dựa vào global variable từ `id`

Historical browser behavior có thể expose element ID trên `window`.

Ví dụ:

```html
<div id="app"></div>
```

Không viết:

```js
app.textContent = "Hello";
```

chỉ vì browser hiện tại cho phép.

Hãy dùng:

```js
document.getElementById("app")
```

hoặc selector/module reference rõ.

Named globals dễ collision và làm dependency implicit.

---

# PHẦN 5 — MICRODATA

## 35. Microdata là gì?

HTML có một native structured-data mechanism gọi là Microdata.

Attributes gồm:

```text
itemscope
itemtype
itemprop
itemid
itemref
```

Ví dụ:

```html
<article
  itemscope
  itemtype="https://schema.org/Book">

  <h1 itemprop="name">
    Example Book
  </h1>

  <span itemprop="author">
    Alice
  </span>

</article>
```

Trong SEO thực tế, JSON-LD thường dễ maintain hơn, nhưng Microdata vẫn thuộc HTML platform và senior nên hiểu khi đọc markup cũ hoặc structured-content systems.

---

## 36. `itemscope` và `itemtype`

`itemscope` tạo một item.

`itemtype` định nghĩa vocabulary/type:

```html
<div
  itemscope
  itemtype="https://schema.org/Person">
```

---

## 37. `itemprop`

```html
<span itemprop="name">
  Alice
</span>
```

Nó khai báo property của item hiện tại.

---

## 38. `itemid`

Có thể cung cấp global identifier cho item khi vocabulary semantics phù hợp.

```html
<div
  itemscope
  itemtype="https://schema.org/Book"
  itemid="https://example.com/books/123">
```

---

## 39. `itemref`

`itemref` cho phép properties nằm ngoài descendant subtree vẫn thuộc item.

Nó reference element IDs, không phải `itemid`.

Đây là edge case cần biết khi inspect structured data generated bởi CMS.

---

# PHẦN 6 — WEB COMPONENTS VÀ DECLARATIVE SHADOW DOM

## 40. `<template>`

Template chứa inert DOM fragment:

```html
<template id="row-template">
  <tr>
    <td></td>
  </tr>
</template>
```

Content không render như ordinary content cho tới khi được clone/insert.

Template cũng là foundation của Declarative Shadow DOM.

---

## 41. Declarative Shadow DOM

Modern HTML cho phép tạo shadow root bằng markup:

```html
<user-card>

  <template shadowrootmode="open">

    <style>
      :host {
        display: block;
      }
    </style>

    <slot></slot>

  </template>

  Alice

</user-card>
```

Browser có thể attach ShadowRoot trong parsing stage.

Điều này rất quan trọng với SSR Web Components vì shadow tree có thể tồn tại trước khi JavaScript boot.

---

## 42. `shadowrootmode`

```html
<template shadowrootmode="open">
```

hoặc:

```html
<template shadowrootmode="closed">
```

Với `open`, consumer code có thể thường access:

```js
host.shadowRoot
```

Với `closed`, normal `shadowRoot` getter không expose root.

Tuy nhiên `closed` không phải security boundary. Code cùng origin/runtime vẫn có nhiều ways influence component, và encapsulation không tương đương sandbox.

---

## 43. `shadowrootdelegatesfocus`

```html
<template
  shadowrootmode="open"
  shadowrootdelegatesfocus>
```

Nó ảnh hưởng focus delegation behavior cho shadow tree.

Use case là host component có internal focusable control nhưng muốn host-level focus interaction/style phù hợp.

Đây là design-system detail, không phải beginner feature.

---

## 44. `shadowrootclonable`

Advanced declarative shadow root option liên quan cloning behavior.

Bạn không cần dùng thường xuyên, nhưng nếu đọc SSR/Web Components infrastructure hiện đại, cần nhận diện.

---

## 45. `<slot>`

Inside shadow tree:

```html
<slot name="title"></slot>
```

Light DOM:

```html
<user-card>
  <h2 slot="title">
    Alice
  </h2>
</user-card>
```

Browser distributes light DOM node vào slot.

Điều này dẫn tới nhiều tree concepts:

```text
light DOM
shadow DOM
composed tree
flat tree
```

Source tree không phải luôn là rendered/accessibility tree.

---

## 46. Custom elements

Autonomous custom element name phải chứa `-`:

```html
<user-card></user-card>
```

JavaScript:

```js
customElements.define(
  "user-card",
  UserCard
);
```

Dấu `-` giúp tránh collision với future native HTML element names.

---

## 47. `is`

Customized built-in element pattern có thể dùng:

```html
<button is="fancy-button">
  Save
</button>
```

Support/architecture trade-offs khiến autonomous custom elements thường dễ deploy hơn.

Senior chỉ cần biết `is` thuộc custom-element ecosystem và phải check compatibility/requirements trước khi chọn.

---

## 48. Form-associated custom elements

Advanced custom element có thể integrate với form semantics thông qua platform APIs như `ElementInternals`.

Concept:

```html
<currency-input
  name="amount">
</currency-input>
```

có thể behave như form control nếu component implementation hỗ trợ đúng.

Đây là powerful capability cho design systems nhưng rất advanced: bạn phải implement form value, validity, labels/accessibility và lifecycle đúng.

Nếu native input đã đủ, đừng custom chỉ vì muốn style.

---

# PHẦN 7 — `hidden="until-found"`

## 49. `hidden`

Basic:

```html
<section hidden>
  ...
</section>
```

Content bị hidden vì không relevant hiện tại.

---

## 50. `hidden="until-found"`

```html
<section
  id="advanced"
  hidden="until-found">

  Advanced HTML parser details

</section>
```

Content hidden nhưng browser có thể reveal nó khi user dùng find-in-page hoặc fragment navigation trong supporting behavior.

Use case rất hay là documentation accordion/collapsed content mà vẫn muốn browser Find hoạt động.

---

## 51. `beforematch`

Browser có thể dispatch `beforematch` trước khi reveal until-found content.

Concept:

```js
section.addEventListener(
  "beforematch",
  () => {
    // prepare surrounding UI
  }
);
```

Điều này cho thấy native browser search/navigation có thể interact với application UI declaratively.

---

# PHẦN 8 — POPOVER DEEPER

## 52. `popover="auto"`

```html
<div
  id="menu"
  popover="auto">
  ...
</div>
```

Shorthand:

```html
<div popover>
```

Auto popover thường hỗ trợ light dismiss, Escape/close requests và managed stacking behavior.

---

## 53. `popover="manual"`

```html
<div popover="manual">
  ...
</div>
```

Manual popover không tự light-dismiss như auto.

Application phải show/hide explicitly.

Useful khi nhiều persistent floating panels có thể tồn tại cùng lúc.

---

## 54. `popover="hint"`

```html
<div popover="hint">
  Shortcut: Ctrl + K
</div>
```

Hint popover được thiết kế cho transient hints/tooltip-like UI với stacking rules khác auto.

Đây là modern feature; production phải check browser matrix thay vì assume universal support.

---

## 55. `popovertarget`

```html
<button
  type="button"
  popovertarget="menu">
  Menu
</button>
```

Tạo declarative relationship giữa invoker và popover.

Browser có thể quản lý control relationship/accessibility behavior tốt hơn custom onclick-only implementation.

---

## 56. `popovertargetaction`

```html
<button
  popovertarget="menu"
  popovertargetaction="show">
  Open
</button>
```

Common actions:

```text
show
hide
toggle
```

---

## 57. Top layer

Open popovers và modal dialogs có thể nằm trong browser-managed **top layer**.

Top layer khác `z-index: 999999`.

Nó không bị ancestor stacking context hoặc overflow clipping theo cách ordinary positioned element bị.

Đây là lý do native overlay primitives giải quyết nhiều “z-index wars”.

---

# PHẦN 9 — DIALOG DEEPER

## 58. Modal vs non-modal

```js
dialog.show()
```

mở non-modal dialog.

```js
dialog.showModal()
```

mở modal dialog.

Modal dialog tham gia top layer và browser quản lý surrounding interaction/inertness theo platform semantics.

---

## 59. `cancel` event

Khi user thực hiện platform close request như Escape trên modal dialog, dialog có thể fire `cancel`.

Application có thể dùng event để intercept unsaved-change scenario tùy behavior.

---

## 60. `close` event

`close` xảy ra khi dialog đã đóng.

Bạn có thể đọc `returnValue` hoặc update application state sau đó.

Đừng nhầm `cancel` là “user click cancel button” trong business sense; nó là platform close-request event semantics.

---

## 61. `closedby`

Modern dialog có `closedby` để mô tả user close behaviors được phép.

Conceptual values:

```text
any
closerequest
none
```

`any` cho phép broad close behaviors, có thể bao gồm light-dismiss theo platform support.

`closerequest` cho phép close request mechanisms.

`none` hạn chế tới developer-defined close path.

Đây là feature mới hơn; hãy check browser compatibility trước khi architecture phụ thuộc hoàn toàn vào nó.

---

# PHẦN 10 — INVOKER COMMANDS

## 62. `commandfor`

Button có thể declaratively target element:

```html
<button
  commandfor="confirm-dialog"
  command="show-modal">
  Open dialog
</button>
```

---

## 63. `command`

Dialog commands hiện đại có thể gồm:

```text
show-modal
close
request-close
```

Ví dụ:

```html
<button
  command="show-modal"
  commandfor="confirm-dialog">
  Open
</button>

<dialog id="confirm-dialog">

  <p>Delete this item?</p>

  <button
    command="close"
    commandfor="confirm-dialog">
    Close
  </button>

</dialog>
```

Ý nghĩa lớn hơn syntax là web platform đang hỗ trợ **declarative interaction** để giảm JavaScript boilerplate.

Tuy nhiên đây là modern capability và browser support phải được kiểm tra cho target audience.

---

# PHẦN 11 — CUSTOMIZABLE SELECT

## 64. Vì sao native select khó style?

Classic `select` delegate phần lớn picker UI cho browser/OS.

Điều này cho accessibility/mobile UX tốt nhưng hạn chế visual customization.

Modern customizable select model cố mở rộng styling mà vẫn giữ select semantics.

---

## 65. `<selectedcontent>`

Concept:

```html
<select name="pet">

  <button>
    <selectedcontent></selectedcontent>
  </button>

  <option value="cat">
    Cat
  </option>

  <option value="dog">
    Dog
  </option>

</select>
```

`selectedcontent` nằm trong first child button và hiển thị clone của selected option content trong supporting browsers.

Điểm quan trọng là clone semantics. Nếu bạn mutate selected option content sau selection, selectedcontent update behavior không phải luôn “live mirror” theo cách beginner tưởng.

---

## 66. Rich option content

Customizable select có thể cho richer option markup trong supporting browsers:

```html
<option value="cat">
  <span aria-hidden="true">🐈</span>
  <span>Cat</span>
</option>
```

Điều này mở khả năng icon + label options.

Nhưng đây là area browser/framework compatibility còn cần kiểm tra kỹ.

SSR parser/hydration với framework cũ có thể gặp issues nếu framework chưa biết content model mới.

---

## 67. Progressive enhancement cho customizable select

Strategy tốt là source vẫn có valid/useful select/options.

Browser support feature thì enhance styling.

Browser không support thì fallback classic select.

Đừng biến một native select đang accessible thành custom JavaScript combobox phức tạp chỉ để đạt vài pixel style nếu requirement không thực sự cần.

---

# PHẦN 12 — LINKS, META VÀ RESOURCE LOADING ADVANCED

## 68. `ping`

Anchor có thể có:

```html
<a
  href="/product"
  ping="/analytics/link-click">
  Product
</a>
```

Browser có thể gửi hyperlink auditing requests.

Feature này có privacy implications và không phải analytics solution bắt buộc.

Senior chỉ cần nhận diện khi audit outbound requests.

---

## 69. `referrerpolicy`

Có thể dùng trên anchors, images, iframes, scripts hoặc links.

```html
<a
  href="https://external.example"
  referrerpolicy="no-referrer">
  External
</a>
```

Policies có thể kiểm soát lượng referrer information gửi sang destination.

Common names:

```text
no-referrer
origin
same-origin
strict-origin
strict-origin-when-cross-origin
unsafe-url
```

Đây là privacy/security leakage control.

---

## 70. `hreflang`

Alternative language relation:

```html
<link
  rel="alternate"
  hreflang="ko"
  href="https://example.com/ko/page">
```

Hữu ích với multilingual SEO/content architecture.

---

## 71. Responsive image preload

Nếu preload LCP image có `srcset`, naive preload một file cố định có thể tải sai candidate.

Modern link preload có related image candidate attributes như `imagesrcset`/`imagesizes` trong relevant contexts.

Concept:

```html
<link
  rel="preload"
  as="image"
  imagesrcset="
    /hero-480.webp 480w,
    /hero-960.webp 960w"
  imagesizes="100vw">
```

Senior performance optimization phải verify bằng network panel để tránh duplicate downloads.

---

## 72. Parser-blocking và render-blocking khác nhau

Parser-blocking nghĩa HTML parser phải dừng/coordinate với resource/script.

Render-blocking nghĩa browser trì hoãn first paint/render vì resource cần thiết.

Một script có thể parser-block.

Một stylesheet có thể render-block.

Đừng dùng hai thuật ngữ như synonym.

---

## 73. Preload scanner

Browser có speculative/preload scanning để discover resource URLs trước khi main parser đến execution point.

HTML source order và discoverability ảnh hưởng network scheduling.

Ví dụ hero image viết trực tiếp trong HTML thường được discover sớm hơn image chỉ được tạo sau khi JavaScript chạy.

Đây là một lý do SSR/HTML-first markup có performance lợi ích.

---

# PHẦN 13 — ACCESSIBILITY DEEPER

## 74. Accessible name precedence

Accessible name có thể đến từ native label, element content, `aria-labelledby`, `aria-label`, `alt` hoặc rules element-specific.

Một bug nghiêm trọng:

```html
<button aria-label="Delete">
  Save
</button>
```

Visual user thấy `Save`, screen reader nghe `Delete`.

ARIA có thể override native text naming theo algorithm.

Vì vậy không thêm `aria-label` “cho chắc”.

---

## 75. Accessible description khác name

```html
<label for="password">
  Password
</label>

<input
  id="password"
  aria-describedby="password-help">

<p id="password-help">
  At least 12 characters.
</p>
```

Accessible name là `Password`.

Description là `At least 12 characters`.

Đây là hai channels khác nhau.

---

## 76. `aria-hidden`

```html
<span aria-hidden="true">
  ★
</span>
```

Element vẫn có thể visible nhưng bị bỏ khỏi accessibility tree.

Đừng đặt `aria-hidden="true"` trên ancestor chứa focusable controls. Bạn có thể tạo UI mà keyboard focus tới được nhưng screen reader không biết nó tồn tại.

---

## 77. `hidden` khác `aria-hidden`

`hidden` ảnh hưởng rendering/relevance rộng hơn.

`aria-hidden` chủ yếu ảnh hưởng accessibility tree.

CSS `display:none`, `visibility:hidden`, `opacity:0`, HTML `hidden` và `inert` đều có semantics khác.

Senior không dùng khái niệm “hide” như thể mọi technique giống nhau.

---

## 78. `inert` vs `disabled`

`disabled` chủ yếu dành cho supported form controls.

`inert` làm cả subtree non-interactive/focusable theo platform behavior.

Nếu custom overlay mở, `inert` có thể disable background subtree.

Nhưng với modal `<dialog>`, browser đã manage modal interaction model; đừng duplicate logic nếu không cần.

---

# PHẦN 14 — SECURITY DEEPER

## 79. Sanitization không phải remove `<script>`

Untrusted HTML có attack surface vượt xa script tag.

Possible vectors gồm:

```text
event handler attributes
dangerous URL schemes
SVG
srcdoc
form/named DOM clobbering
CSS-related contexts
foreign content
```

Một regex remove `<script>` không phải HTML sanitizer.

Dùng battle-tested sanitizer phù hợp threat model.

---

## 80. `javascript:` URLs

Nếu user-controlled URL được đặt vào:

```html
<a href="...">
```

HTML escaping alone không đảm bảo URL safe.

Application cần validate URL scheme.

Conceptual allowlist:

```text
https:
http:
```

và những schemes cụ thể business thực sự cần.

---

## 81. `srcdoc`

`iframe[srcdoc]` là một document execution context.

Nếu đưa untrusted HTML vào, cần sanitize và sandbox theo threat model.

Đừng coi nó như `textContent`.

---

## 82. DOM clobbering như security issue

Nếu attacker control markup, họ có thể tạo named elements làm thay đổi property lookup trong vulnerable code.

Defense gồm:

```text
sanitize untrusted HTML
avoid global/named-property magic
use explicit selectors
validate object/property types
keep security config outside DOM
```

DOM không phải trusted configuration store.

---

# PHẦN 15 — SSR VÀ FRAMEWORK INTEGRATION

## 83. Valid HTML quan trọng hơn với SSR

JSX:

```jsx
<p>
  <div>Hello</div>
</p>
```

có thể compile thành markup browser sẽ repair.

Server render string một tree.

Browser parser tạo một tree khác.

React hydrate tree thứ ba theo expected component structure.

Kết quả là hydration mismatch.

Vì vậy React developer vẫn phải master HTML content models.

---

## 84. JSX syntax không phải HTML parser rules

JSX cho phép syntax dựa trên JavaScript tooling.

Browser không parse JSX; browser parse generated HTML.

Việc JSX compiler chấp nhận nesting không chứng minh browser resulting DOM giống component nesting.

Validator và rendered DOM inspection vẫn quan trọng.

---

## 85. Declarative Shadow DOM + SSR

Server có thể gửi:

```html
<my-card>

  <template shadowrootmode="open">
    ...
  </template>

</my-card>
```

Browser attach shadow root trong parse stage.

Điều này cho component encapsulation tồn tại trước JavaScript hydration/upgrade.

Đây là bridge quan trọng giữa HTML parser và Web Components SSR.

---

# PHẦN 16 — NATIVE HTML TRƯỚC CUSTOM JAVASCRIPT

## 86. Accordion/disclosure

Nếu requirement chỉ là show/hide section:

```html
<details>
  <summary>More</summary>
  ...
</details>
```

có thể đủ.

Đừng mặc định cần React state + div + ARIA.

---

## 87. Modal

Nếu cần modal dialog:

```html
<dialog>
```

thường tốt hơn generic `div`.

Browser cung cấp top layer, modal semantics và close-request behavior.

---

## 88. Floating UI

Popover API giải quyết nhiều menu/help overlay cases.

Bạn vẫn có thể cần positioning/design logic, nhưng show/hide/stack/light-dismiss có thể native.

---

## 89. Form validation

Trước custom validation framework, xem native constraints:

```text
required
type=email
min
max
step
pattern
minlength
maxlength
```

Custom JS có thể improve messages/business checks, không cần replace mọi native behavior.

---

# PHẦN 17 — MASTER DEBUG EXERCISES

## 90. Parser repair exercise

Source:

```html
<p>
  Hello
  <div>World</div>
</p>
```

Mở DevTools Elements và so sánh DOM với source.

Mục tiêu là thấy indentation không quyết định tree.

---

## 91. Attribute/property exercise

```html
<input
  id="name"
  value="Alice">
```

Trong console:

```js
const el =
  document.getElementById("name");

el.value = "Bob";

console.log(el.value);
console.log(el.defaultValue);
console.log(
  el.getAttribute("value")
);
```

Sau đó đặt input vào form và gọi:

```js
form.reset();
```

Quan sát current/default state.

---

## 92. Checkbox state exercise

```html
<input
  id="agree"
  type="checkbox"
  checked>
```

User uncheck rồi compare:

```js
el.checked
el.defaultChecked
el.getAttribute("checked")
```

Đây là cách học attribute/property reflection thực tế.

---

## 93. Form owner exercise

```html
<form
  id="profile"
  action="/save"
  method="post">

  <input
    name="email"
    value="a@example.com">

</form>

<button
  type="submit"
  form="profile">
  Save
</button>
```

Button nằm ngoài form nhưng vẫn submit form.

Đây là browser-native feature hữu ích cho layout components.

---

## 94. Popover exercise

```html
<button
  popovertarget="help">
  Help
</button>

<div
  id="help"
  popover>

  Native popover content

</div>
```

So sánh lượng code với custom overlay gồm state, outside-click listener, Escape handler và z-index.

---

## 95. `hidden="until-found"` exercise

```html
<section
  id="advanced"
  hidden="until-found">

  UNIQUE_SEARCH_TEXT_123

</section>
```

Dùng browser Find hoặc fragment navigation trong supporting browser và quan sát reveal behavior.

---

## 96. DOM clobbering exercise

```html
<form id="f">
  <input name="method">
</form>
```

Trong console inspect:

```js
const f =
  document.getElementById("f");

console.log(f.method);
```

Mục tiêu không phải exploit mà là hiểu tại sao named property access có thể surprise.

---

# PHẦN 18 — MASTER REVIEW CHECKLIST DẠNG MENTAL MODEL

Khi bạn nhìn một đoạn HTML production, đừng review chỉ bằng mắt xem tag có đóng chưa.

Đầu tiên hãy nghĩ tới parser: source này sẽ tạo DOM nào? Có invalid nesting khiến browser repair không? Có SSR/hydration risk không?

Sau đó nghĩ tới semantics: element có đúng meaning không? Link/button có dùng đúng không? Heading/landmark có rõ không?

Tiếp theo nghĩ tới accessibility: accessible name đến từ đâu? Keyboard flow có tự nhiên không? Có custom role nào đang thay native element vô lý không?

Với forms, hãy hỏi form owner là gì, submitter là gì, field nào thực sự submit, disabled/readonly/checkbox behavior ra sao và reset state có đúng không.

Với security, hãy hỏi user-controlled data đi vào text, URL, iframe, `srcdoc`, attribute hay raw HTML context nào. Có sandbox/CSP/sanitization strategy không? DOM có bị dùng làm trusted config không?

Với performance, hãy hỏi browser discover critical resources lúc nào, image dimensions đã có chưa, LCP image có bị lazy-load không, script có block parser không và resource hints có thực sự cần không.

Đó là cách một senior/master review HTML.

---

# PHẦN 19 — NHỮNG THỨ KHÔNG CẦN HỌC THUỘC

Bạn không cần thuộc toàn bộ HTML parser state machine, mọi obsolete attribute hoặc mọi DOM interface.

Bạn cần biết **chúng tồn tại**, biết category vấn đề, và biết khi nào phải mở HTML Living Standard/MDN để xác minh edge case.

Mastery không phải memory contest.

Một developer master HTML có khả năng nhìn bug và đặt đúng câu hỏi:

```text
đây là source problem hay parser-repair problem?
đây là attribute hay property state?
đây là form owner hay DOM nesting problem?
đây là accessible-name problem hay visual CSS problem?
đây là browser support issue hay invalid markup?
đây là JS bug hay native behavior đã tồn tại?
```

---

# PHẦN 20 — FULL HTML PLATFORM MENTAL MODEL

Mental model cuối cùng:

```text
HTTP response / bytes
↓
character decoding
↓
HTML tokenizer
↓
tree construction / parser error recovery
↓
DOM
↓
CSSOM + style/layout
↓
accessibility tree
↓
resource loading / scripts
↓
native form/interaction algorithms
↓
framework hydration/mutation
↓
user interaction
```

HTML source chỉ là điểm bắt đầu.

Khi hiểu browser biến source thành DOM, accessibility tree và interactive behavior thế nào, bạn không còn học HTML như danh sách tags nữa. Bạn đang học **web platform**.

---

# PHẦN 21 — TRÌNH TỰ HỌC MASTER IMPLEMENTATION

Đầu tiên hãy học parser/content model và form internals, vì đây là những thứ dễ tạo bug nhất dù bạn dùng framework.

Tiếp theo học DOM clobbering, accessibility naming và security context, vì đây là phần nâng code review từ “functional” lên “robust”.

Sau đó học Web Components, Declarative Shadow DOM, Popover/Dialog commands và customizable select để hiểu hướng phát triển của HTML platform hiện đại.

Các feature mới không cần deploy ngay. Điều quan trọng là biết native platform đang cung cấp gì và check compatibility trước khi tự xây abstraction riêng.

---

# KẾT LUẬN

HTML mastery không nằm ở việc nhớ được 150 tag.

Nó nằm ở việc hiểu browser.

Nếu bạn hiểu vì sao browser tự đóng `<p>`, vì sao default namespace không liên quan ở HTML nhưng SVG namespace lại quan trọng, vì sao `input.value` khác `getAttribute("value")`, vì sao disabled field không submit, vì sao form button ngoài form vẫn có thể submit qua `form=id`, vì sao modal dialog có top layer, vì sao DOM clobbering tồn tại và vì sao native components thường accessibility tốt hơn custom div, thì bạn đã vượt xa mức “biết HTML”.

Khi kết hợp file Beginner → Senior với file Master Implementation này, bạn đã có một nền tảng HTML đủ sâu để tiếp tục học CSS, JavaScript, React, Web Components và browser internals mà không bị thiếu phần nền tảng markup.
