# HTML — Master Implementation
## Trình duyệt phân tích cú pháp, cơ chế nội bộ của form, khả năng tiếp cận API, bảo mật, chuyển đổi hệ thống cũ và HTML khai báo hiện đại

Tài liệu này tiếp nối `html_01_beginner_to_senior_detailed.md`. File đầu xây nền tảng từ cấu trúc tài liệu, ngữ nghĩa, forms, media, khả năng tiếp cận, SEO và hiệu năng. File Master này đi sâu vào phần khiến HTML trở thành một **nền tảng trình duyệt** chứ không chỉ là tập hợp tag: bộ phân tích cú pháp có thể sửa markup như thế nào, trạng thái hiện thời của DOM khác source ra sao, biểu mẫu chủ quản và điều khiển gửi biểu mẫu hoạt động thế nào, cây trợ năng nhận ngữ nghĩa từ đâu, các phần tử tùy biến kết nối với Shadow DOM ra sao, và vì sao những feature mới như Popover hoặc Declarative Shadow DOM có thể thay thế một phần JavaScript thủ công.

Mục tiêu không phải thuộc mọi production trong HTML Living Standard. Mục tiêu là khi gặp một bug hoặc một đoạn markup lạ, bạn biết trình duyệt sẽ xử lý ở layer nào và biết câu hỏi cần đặt ra: source có valid không, bộ phân tích cú pháp có repair tree không, element có ngữ nghĩa gốc của phần tử gì, thuộc tính DOM hiện tại khác attribute ban đầu ra sao, control có tham gia form submission không, công nghệ hỗ trợ nhận tên trợ năng nào, và chính sách tài nguyên và bảo mật bị ảnh hưởng thế nào.


## Quy ước thuật ngữ trong tài liệu

Tài liệu dùng tiếng Việt tự nhiên làm ngôn ngữ giải thích chính và giữ thuật ngữ gốc ở lần định nghĩa để tiện tra cứu. Các cách gọi được dùng thống nhất gồm: **trình duyệt (browser)**, **phân tích cú pháp (parsing)**, **bộ phân tích cú pháp (parser)**, **HTML ngữ nghĩa (semantic HTML)**, **ngữ nghĩa (semantics)**, **khả năng tiếp cận (accessibility)**, **cây trợ năng (accessibility tree)**, **tên trợ năng (accessible name)**, **siêu dữ liệu (metadata)**, **kiểm tra ràng buộc của biểu mẫu (constraint validation)**, **mô hình nội dung (content model)**, **thuộc tính DOM (DOM property)**, **trạng thái hiện thời (live state)**, **lớp trên cùng (top layer)**, **hiệu năng (performance)** và **bảo mật (security)**. Sau khi đã định nghĩa ở đây, phần nội dung bên dưới ưu tiên dùng cách gọi tiếng Việt để câu văn không bị nặng. Các tên chuẩn như DOM, ARIA, CORS, CSP, Shadow DOM, Web Components, `iframe`, tên tag, attribute và API cụ thể được giữ nguyên nếu dịch sẽ làm mất nghĩa hoặc gây khó đối chiếu tài liệu kỹ thuật.

---

# PHẦN 1 — NHỮNG ELEMENT ÍT GẶP NHƯNG CẦN BIẾT

## 1. `<search>`

`search` biểu diễn một vùng của document dành cho chức năng tìm kiếm hoặc lọc. Nó không thực hiện search và cũng không thay thế `form`; semantic của nó chỉ giúp trình duyệt và khả năng tiếp cận layer biết subtree này có purpose là search.

```html
<search>
  <form action="/search" method="get">
    <label for="q">Search</label>
    <input id="q" name="q" type="search">
    <button type="submit">Search</button>
  </form>
</search>
```

Khi dùng, hãy nghĩ theo meaning thay vì visual layout. Một filter panel thực sự dùng để query một product list có thể phù hợp với `search`; một toolbar chứa random buttons thì không.

---

## 2. `<hgroup>`

`hgroup` group một heading với supporting text như subtitle hoặc tagline.

```html
<hgroup>
  <h1>HTML Platform</h1>
  <p>From semantic markup to browser behavior</p>
</hgroup>
```

Nó không phải shortcut để gộp `h1`, `h2`, `h3` thành một hierarchy. Heading hierarchy vẫn đến từ headings và cấu trúc tài liệu. Accessibility implication ở đây là supporting text không trở thành một heading chỉ vì đứng gần heading về mặt visual.

---

## 3. `<menu>`

`menu` hiện đại có thể biểu diễn một list các commands/actions.

```html
<menu>
  <li><button type="button">Copy</button></li>
  <li><button type="button">Paste</button></li>
</menu>
```

Trong application thông thường `ul` vẫn phổ biến hơn. Điều quan trọng là không nhầm element hiện tại với các context-menu APIs hệ thống cũ từng tồn tại trong HTML cũ.

---

## 4. `<wbr>`

`wbr` tạo **word break opportunity**. Trình duyệt chỉ xuống dòng tại đó khi layout cần, khác với `br` là line break bắt buộc.

```html
<p>
  verylong<wbr>generated<wbr>identifier
</p>
```

Nó hữu ích với URL, hash, identifier hoặc technical token dài. Về khả năng tiếp cận, `wbr` không nên được dùng để thay đổi meaning của text; nó chỉ giúp layout break line ở vị trí hợp lý.

---

## 5. `<dfn>` và `<u>`

`dfn` đánh dấu nơi một thuật ngữ đang được định nghĩa:

```html
<p>
  <dfn>Hydration</dfn>
  là quá trình JavaScript kết nối behavior với markup đã được render từ server.
</p>
```

`u` không đơn giản nghĩa là “underline”. Nó biểu diễn một annotation phi văn bản theo convention, ví dụ spelling annotation:

```html
<p>
  <u class="spelling-error">recieve</u>
</p>
```

Nếu mục tiêu chỉ là presentation, CSS phù hợp hơn. Underline còn có UX implication vì user thường liên tưởng underline với link.

---

## 6. `<map>` và `<area>`

Image map cho phép một image có nhiều vùng clickable:

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
</map>
```

Trình duyệt dùng `shape` và `coords` để hit-test vùng trên image. Feature này hiện khá niche vì responsive scaling và khả năng tiếp cận phức tạp. Nếu dùng, `area` cần alternative text phù hợp và tương tác phải vẫn hiểu được khi người dùng không nhìn image.

---

## 7. `<canvas>`

`canvas` cung cấp bitmap drawing surface cho JavaScript:

```html
<canvas id="chart" width="800" height="400">
  Sales chart
</canvas>
```

`width` và `height` attributes định nghĩa drawing buffer, không chỉ kích thước CSS. Nếu buffer nhỏ nhưng CSS phóng lớn, output dễ blur.

Canvas pixels không tự tạo semantic tree. Một chart quan trọng nên có alternative representation như table, text summary hoặc DOM controls. Senior cần nhớ rằng canvas kết xuất và cây trợ năng là hai hệ thống khác nhau.

---

## 8. SVG và MathML là foreign content

HTML có thể embed SVG:

```html
<svg viewBox="0 0 24 24" aria-hidden="true">
  <path d="..."></path>
</svg>
```

và MathML:

```html
<math>
  <mrow>
    <mi>x</mi>
    <mo>=</mo>
    <mn>10</mn>
  </mrow>
</math>
```

Khi bộ phân tích cú pháp đi vào SVG hoặc MathML, namespace và phân tích cú pháp rules thay đổi. Đây là lý do một node trong SVG không nên được coi như `div` có shape. Với icon decorative, `aria-hidden="true"` thường phù hợp; với graphic có meaning, cần accessible naming/alternative phù hợp.

---

# PHẦN 2 — HTML PARSER VÀ TREE CONSTRUCTION

## 9. HTML không phải XML

Trong `text/html`, `img` là phần tử rỗng đặc biệt:

```html
<img src="/a.png" alt="">
```

Viết:

```html
<img src="/a.png" alt="" />
```

không biến document thành XML. Parsing mode đến từ media type/context và bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp), không đến từ dấu slash. Đây là điểm quan trọng khi bạn học HTML và XML song song.

---

## 10. Optional end tags và bộ phân tích cú pháp repair

HTML cho phép omit một số end tags trong những conditions cụ thể:

```html
<ul>
  <li>A
  <li>B
</ul>
```

Trình duyệt vẫn có thể tạo hai `li`. Tuy nhiên source code production nên ưu tiên closing tags rõ ràng để formatter, reviewer và framework dễ reason hơn.

bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) còn có phục hồi lỗi (error recovery) mạnh. Việc trình duyệt render được markup không chứng minh markup author-conforming hoặc semantic đúng.

---

## 11. `<p>` auto-closing

Source:

```html
<p>
  Hello
  <div>World</div>
</p>
```

không tạo tree “div nằm trong p” như indentation gợi ý. Khi bộ phân tích cú pháp gặp content không được phép trong `p`, nó có thể đóng `p` trước. Resulting DOM vì vậy khác source.

Đây là một nguyên nhân rất thực tế của SSR hydration mismatch: server/template nghĩ một tree, trình duyệt repair thành tree thứ hai, framework hydrate dựa trên expectation thứ ba.

---

## 12. Insertion modes, foster parenting và adoption agency algorithm

bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) là context-sensitive. Nó có các insertion modes như `in head`, `in body`, `in table`, `in row`, `in cell`. Một token xuất hiện trong table context có thể được xử lý khác khi nó xuất hiện trong ordinary body flow.

Với malformed table content, trình duyệt có thể di chuyển node ra khỏi table theo rules thường được gọi là **foster parenting**. Với một số formatting elements bị nest sai, bộ phân tích cú pháp có algorithm đặc biệt thường được gọi là **adoption agency algorithm**.

Bạn không cần thuộc từng bước thuật toán. Điều cần hiểu là DOM được quyết định bởi bộ phân tích cú pháp algorithm, không phải indentation và cũng không phải “trình duyệt đoán ngẫu nhiên”.

---

## 13. View Source, parsed DOM và framework tree

Ba layer phải được phân biệt. View Source gần với original response. DOM là kết quả sau bộ tách token (tokenizer)/quá trình dựng cây DOM (tree construction) và sau các runtime mutations. React/Vue/Svelte lại có internal component/tree model riêng.

Khi debug hydration, table structure hoặc invalid nesting, hãy so sánh original HTML với Elements panel thay vì chỉ nhìn JSX/template.

---

## 14. Raw text, RCDATA và character references

`script` và `style` có phân tích cú pháp contexts khác ordinary text. `title` và `textarea` cũng có RCDATA-like phân tích cú pháp behavior. Vì vậy một escaping strategy đúng cho text node bình thường không tự động đúng cho JavaScript/CSS/script contexts.

Character references như `&amp;`, `&lt;`, `&gt;` và `&quot;` dùng khi cần biểu diễn special characters. `&nbsp;` là non-breaking space, không phải công cụ để tạo layout spacing; layout thuộc CSS.

---

# PHẦN 3 — FORM INTERNALS VÀ LIVE STATE

## 15. Form owner

Form-associated control có một **biểu mẫu chủ quản**. Bình thường owner là ancestor form:

```html
<form id="profile">
  <input name="email">
</form>
```

Nhưng control có thể associate từ bên ngoài:

```html
<form id="profile">
  ...
</form>

<button type="submit" form="profile">
  Save
</button>
```

Trình duyệt dùng `form="profile"` để liên kết control với form ID. Điều này hữu ích với sticky action bars hoặc component layouts nơi visual position không trùng DOM nesting.

Nested `form` không phải cách tạo form con. Hãy dùng sibling forms hoặc explicit `form` association.

---

## 16. Submitter và implicit submission

Button trigger form submission được gọi là điều khiển gửi biểu mẫu:

```html
<button
  type="submit"
  name="action"
  value="publish">
  Publish
</button>
```

Submitter có thể thêm `action=publish` vào form data và có thể override `formaction`, `formmethod`, `formenctype`, `formtarget`, `formnovalidate`.

Pressing Enter trong text control có thể trigger implicit submission tùy form structure. Vì vậy button không phải submit nên ghi `type="button"` rõ ràng.

---

## 17. Successful controls

Khi form submit, trình duyệt không đơn giản serialize mọi input nằm trong DOM. Control phải đáp ứng submission rules. `name` thường cần thiết; disabled controls thường không đóng góp entry; unchecked checkbox/radio thường không tạo entry; readonly value vẫn có thể submit; submit button chỉ đóng góp khi nó là điều khiển gửi biểu mẫu.

Đây là reason backend đôi khi “không nhận được field” dù field hiển thị trên UI. Debug bằng form-data ngữ nghĩa trước khi đổ lỗi network library.

---

## 18. Disabled, readonly và disabled fieldset

`disabled` thường khiến control không tiêu điểm/edit và không submit. `readonly` ngăn sửa ở các supported control types nhưng value vẫn có thể được submit.

```html
<input name="accountId" value="A123" readonly>
```

Không được coi readonly value là trusted; client vẫn có thể sửa request.

`fieldset disabled` disable phần lớn descendants nhưng first `legend` có special behavior. Đây là edge case hữu ích khi đọc native form algorithms, dù application bình thường không cần dựa vào nó như một trick.

---

## 19. Reset, trạng thái hiện tại và trạng thái mặc định

`type="reset"` không “xóa trắng form”; nó restore trạng thái mặc định.

```html
<input value="Alice">
```

sau khi user sửa thành `Bob`, `input.value` là trạng thái hiện tại còn `input.defaultValue` liên quan reset/trạng thái mặc định. Checkbox có `checked` và `defaultChecked`; option có `selected` và `defaultSelected`.

Đây là một ví dụ quan trọng cho relationship giữa markup attribute và thuộc tính DOM.

---

## 20. `dirname` và `capture`

`dirname` cho phép trình duyệt submit text direction siêu dữ liệu cùng field, hữu ích với international user-generated content.

`capture` trên file input là hint cho mobile capture source:

```html
<input
  type="file"
  accept="image/*"
  capture="environment">
```

Nó không phải bảo mật/permission guarantee và UX có thể khác theo trình duyệt/device.

---

# PHẦN 4 — DOM RELATION VÀ DOM CLOBBERING

## 21. Attribute không đồng nghĩa live property

Markup là initial declarative state; DOM object có live properties. Ví dụ user có thể thay đổi `input.value` mà `getAttribute("value")` vẫn phản ánh initial/default markup.

Tương tự, `a.getAttribute("href")` có thể là relative URL `/users`, còn `a.href` thường là URL đã được resolve thành absolute URL.

Senior cần biết attribute reflection rules khác nhau theo từng API thay vì assume attribute/property luôn sync hai chiều.

---

## 22. DOM clobbering

HTML có historical named-access behavior. Một form control có `name="method"` hoặc `name="submit"` có thể collide với property mà code tưởng là built-in member.

```html
<form id="user-form">
  <input name="method">
</form>
```

Với untrusted markup, named access có thể góp phần tạo bảo mật bugs. Tránh relying vào magic globals hoặc properties do `id`/`name` tự expose. Dùng explicit selectors, `form.elements.namedItem()` và APIs như `requestSubmit()`.

DOM không nên được dùng như trusted configuration store.

---

# PHẦN 5 — MICRODATA

## 23. Microdata

Microdata là structured-data mechanism native của HTML với `itemscope`, `itemtype`, `itemprop`, `itemid`, `itemref`.

```html
<article
  itemscope
  itemtype="https://schema.org/Book">

  <h1 itemprop="name">Example Book</h1>
  <span itemprop="author">Alice</span>
</article>
```

JSON-LD thường dễ quản lý hơn trong SEO architecture hiện đại, nhưng Microdata vẫn quan trọng khi audit CMS hoặc hệ thống cũ structured markup. Trình duyệt không biến Microdata thành visual behavior; nó bổ sung machine-readable relationships trên document.

---

# PHẦN 6 — TEMPLATE, CUSTOM ELEMENTS VÀ SHADOW DOM

## 24. `<template>`

`template` chứa inert fragment:

```html
<template id="row-template">
  <tr><td></td></tr>
</template>
```

Content không participate như ordinary rendered content cho tới khi được clone/insert, và template còn là foundation của Declarative Shadow DOM.

---

## 25. Declarative Shadow DOM

Server có thể gửi:

```html
<user-card>
  <template shadowrootmode="open">
    <style>
      :host { display: block; }
    </style>
    <slot></slot>
  </template>
  Alice
</user-card>
```

Trình duyệt có thể attach shadow root ngay trong parse stage. Điều này đặc biệt hữu ích cho SSR Web Components vì encapsulated DOM/style có thể tồn tại trước JavaScript boot.

`shadowrootmode="open"` cho phép normal `host.shadowRoot` access; `closed` không expose root qua getter thông thường nhưng không phải bảo mật sandbox. `shadowrootdelegatesfocus` ảnh hưởng tiêu điểm delegation; advanced options như clonable behavior cần check compatibility khi infrastructure phụ thuộc chúng.

---

## 26. Slots và composed tree

Shadow DOM dùng `slot` để phân phối light-DOM content:

```html
<slot name="title"></slot>
```

```html
<user-card>
  <h2 slot="title">Alice</h2>
</user-card>
```

Đây là lý do source/light DOM, shadow DOM, rendered flat/composed tree và cây trợ năng không phải lúc nào giống nhau. Khi debug tiêu điểm hoặc tên trợ năng trong Web Components, phải biết node đang tồn tại ở tree nào.

---

## 27. Custom elements và form-associated các phần tử tùy biến

Autonomous phần tử tùy biến phải có dấu `-`:

```html
<user-card></user-card>
```

JavaScript register qua `customElements.define()`. Customized built-in model còn có `is`, nhưng architecture/support cần được kiểm tra kỹ.

Advanced components có thể tham gia form model thông qua `ElementInternals`. Điều này powerful cho design systems nhưng không miễn bạn khỏi việc implement labels, validity, form value và khả năng tiếp cận ngữ nghĩa. Nếu native control đáp ứng requirement thì native element thường là lựa chọn ít lỗi hơn.

---

# PHẦN 7 — HIDDEN, POPOVER VÀ TOP LAYER

## 28. `hidden="until-found"`

Ordinary `hidden` nói content hiện tại không relevant/presented. `hidden="until-found"` cho phép content vẫn có thể được trình duyệt reveal khi find-in-page hoặc fragment navigation tìm thấy target trong supporting behavior.

```html
<section id="advanced" hidden="until-found">
  Advanced parser details
</section>
```

`beforematch` có thể được dispatch trước reveal để application prepare surrounding UI. Đây là ví dụ browser-native Find/navigation tích hợp với application state.

---

## 29. Popover modes

Popover API tạo floating UI mà trình duyệt quản lý show/hide/top-layer behavior.

```html
<button popovertarget="help">Help</button>
<div id="help" popover>...</div>
```

`auto` phù hợp với popovers có light dismiss; `manual` cho application control persistence; `hint` hướng tới transient hint/tooltip-like interactions trong supporting browsers. `popovertargetaction` có thể yêu cầu `show`, `hide` hoặc `toggle`.

Popover không tự quyết định business ngữ nghĩa của content. Một menu vẫn cần đúng menu/navigation/control ngữ nghĩa; Popover chỉ giải quyết overlay lifecycle/top-layer primitive.

---

## 30. Top layer

Top layer không phải `z-index` cực lớn. Nó là browser-managed layer dành cho một số UI như modal dialog và popover. Vì vậy nó tránh nhiều vấn đề ancestor stacking context hoặc overflow clipping mà custom overlay gặp.

Khi native top-layer primitive phù hợp, thường tốt hơn việc bắt đầu bằng `position: fixed; z-index: 999999`.

---

# PHẦN 8 — DIALOG VÀ DECLARATIVE COMMANDS

## 31. Modal và non-modal dialog

`dialog.show()` mở non-modal; `dialog.showModal()` mở modal. Modal dialog tham gia lớp trên cùng và trình duyệt quản lý surrounding tương tác theo modal model.

`cancel` liên quan platform close request như Escape; `close` xảy ra sau khi dialog đóng. `form method="dialog"` cho phép button submit đóng dialog mà không gửi network request.

Modern `closedby` cho phép mô tả close behavior như `any`, `closerequest` hoặc `none` trong supporting browsers. Vì đây là feature mới hơn, production cần check target-browser compatibility.

---

## 32. `command` và `commandfor`

Modern HTML đang mở rộng declarative tương tác:

```html
<button
  command="show-modal"
  commandfor="confirm-dialog">
  Open
</button>

<dialog id="confirm-dialog">
  <p>Delete?</p>
  <button
    command="close"
    commandfor="confirm-dialog">
    Close
  </button>
</dialog>
```

Các commands như `show-modal`, `close`, `request-close` có thể giảm JavaScript boilerplate. Ý nghĩa senior ở đây là luôn kiểm tra native platform trước khi tự xây một state machine custom, nhưng feature mới phải được progressive-enhance thay vì assume support universal.

---

# PHẦN 9 — CUSTOMIZABLE SELECT

## 33. `<selectedcontent>` và rich options

Classic select rất mạnh về keyboard/mobile/khả năng tiếp cận nhưng khó style. Customizable select model cho trình duyệt hỗ trợ richer markup trong select trong những môi trường phù hợp.

Concept:

```html
<select name="pet">
  <button>
    <selectedcontent></selectedcontent>
  </button>

  <option value="cat">
    <span aria-hidden="true">🐈</span>
    <span>Cat</span>
  </option>
</select>
```

`selectedcontent` hiển thị content tương ứng với selected option theo platform model. Đây là feature hiện đại nên phải test trình duyệt/framework/SSR compatibility. Progressive enhancement là strategy đúng: trình duyệt mới được richer styling, trình duyệt cũ vẫn dùng usable native select.

---

# PHẦN 10 — ADVANCED RESOURCE, LINK VÀ REQUEST ATTRIBUTES

## 34. `referrerpolicy`

`referrerpolicy` có thể xuất hiện trên link, anchor, image, script, iframe và một số resource elements. Nó kiểm soát lượng referrer information trình duyệt gửi cùng request.

```html
<a
  href="https://external.example"
  referrerpolicy="no-referrer">
  External
</a>
```

Policies như `no-referrer`, `origin`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin` thuộc privacy/bảo mật request behavior. Chúng không thay authorization.

---

## 35. `crossorigin` và CORS mode

`crossorigin` không chỉ là một string decoration. Trên các resource elements phù hợp, nó thay đổi CORS request/response handling.

Ví dụ:

```html
<img
  src="https://cdn.example.com/photo.png"
  crossorigin="anonymous"
  alt="Product">
```

Nếu khác nguồn image được draw vào canvas mà CORS không cho phép, canvas có thể trở thành **tainted**, khiến trình duyệt block pixel-reading/export APIs. Vì vậy `crossorigin` có browser-processing consequence rõ ràng.

Trên script/link/font/SRI scenarios, CORS mode cũng có thể ảnh hưởng việc resource được chấp nhận. Hãy cấu hình cùng server response headers; attribute một mình không magically cấp quyền khác nguồn.

---

## 36. `ping` và hyperlink auditing

Anchor có thể có `ping`:

```html
<a href="/product" ping="/analytics/link-click">
  Product
</a>
```

Trình duyệt có thể gửi auditing requests khi navigation xảy ra. Vì có privacy implication và analytics ecosystem còn nhiều cách khác, senior chủ yếu cần biết để audit network behavior thay vì coi đây là default tracking solution.

---

## 37. `hreflang`, alternate resources và SEO

```html
<link
  rel="alternate"
  hreflang="ko"
  href="https://example.com/ko/page">
```

`hreflang` mô tả language relationship cho alternate page/resource. Trình duyệt/search systems có thể dùng siêu dữ liệu này; nó không tự dịch content và không thay `lang` trên document.

---

## 38. Responsive preload và priority hints

Nếu LCP image có `srcset`, preload một hard-coded candidate có thể khiến trình duyệt fetch resource không phù hợp. Responsive image preload có thể cần `imagesrcset`/`imagesizes` tương ứng.

`fetchpriority` là hint, không phải scheduler command tuyệt đối. Nếu mọi resource đều `high`, priority signal mất ý nghĩa.

Performance decisions nên đo bằng Network panel, Core Web Vitals/RUM hoặc profiler thay vì thêm preload/preconnect theo cảm giác.

---

## 39. Parser-blocking, chặn kết xuất (render-blocking) và preload scanner

Parser-blocking nghĩa main bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) phải dừng/coordinate với script/resource. Render-blocking nghĩa trình duyệt trì hoãn paint vì resource cần thiết. Hai concepts không phải synonym.

Trình duyệt còn có speculative/preload scanner để discover resource URLs sớm. Vì vậy source order và việc URL có xuất hiện trực tiếp trong HTML hay chỉ được JavaScript tạo sau đó có thể ảnh hưởng thời điểm fetch.

---

# PHẦN 11 — METADATA ADVANCED

## 40. `meta http-equiv` không phải replacement hoàn chỉnh cho HTTP headers

`http-equiv` tạo một số pragma/directive-like effects trong HTML document:

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'">
```

hoặc hệ thống cũ refresh behavior:

```html
<meta
  http-equiv="refresh"
  content="5;url=/next">
```

Trình duyệt chỉ hỗ trợ những directives cụ thể. Khi bạn kiểm soát server, real HTTP response headers thường là layer rõ và mạnh hơn cho bảo mật/network policy, đặc biệt với CSP. Đừng nhìn `http-equiv` rồi nghĩ bất kỳ HTTP header nào cũng có thể được mô phỏng trong HTML.

---

## 41. `meta name="color-scheme"`

```html
<meta
  name="color-scheme"
  content="light dark">
```

Metadata này nói document hỗ trợ những color schemes nào, giúp trình duyệt chọn default kết xuất cho form controls, scrollbars hoặc canvas/background-related trình duyệt UI trong applicable contexts. Nó không thay CSS theme system; CSS vẫn chịu trách nhiệm presentation cụ thể.

Accessibility implication là UA controls có thể hòa hợp tốt hơn với light/dark environment và tránh contrast mismatch do trình duyệt default khác theme app.

---

## 42. Document-level referrer policy

Ngoài element-level `referrerpolicy`, document có thể dùng siêu dữ liệu phù hợp để đặt referrer policy chung. Senior nên hiểu policy có thể đến từ HTTP header, document siêu dữ liệu hoặc element-level override tùy mechanism.

Nguyên tắc thiết kế là policy toàn site/document nên được đặt ở boundary dễ audit; element-level override chỉ dùng khi resource/link có requirement riêng.

---

# PHẦN 12 — ACCESSIBILITY VÀ ARIA NHƯ MỘT API LAYER

## 43. Native HTML trước ARIA

Nguyên tắc quan trọng nhất là: nếu native HTML element đã có ngữ nghĩa và behavior cần thiết, hãy dùng nó trước khi tạo phần tử tùy biến bằng role.

```html
<button type="button">Save</button>
```

thường tốt hơn:

```html
<div role="button" tabindex="0">Save</div>
```

`role="button"` có thể làm khả năng tiếp cận API expose node như button, nhưng nó không tự thêm Space/Enter activation, disabled ngữ nghĩa, form behavior hoặc keyboard handling. ARIA thay đổi semantic exposure; nó không tự tạo trình duyệt behavior tương ứng.

---

## 44. Accessible name và description

Native `<label>` hoặc element text thường là nguồn tên trợ năng tốt nhất. `aria-labelledby` cho phép name đến từ node khác; `aria-label` cung cấp explicit string khi visible label không phù hợp, ví dụ icon-only button.

Sai:

```html
<button aria-label="Delete">Save</button>
```

Visual user thấy `Save` còn công nghệ hỗ trợ có thể announce `Delete`, tạo severe mismatch.

Description là channel khác name:

```html
<label for="password">Password</label>
<input
  id="password"
  aria-describedby="password-help">
<p id="password-help">At least 12 characters.</p>
```

Name trả lời “control là gì”; description cung cấp hướng dẫn bổ sung.

---

## 45. `aria-expanded` và `aria-controls`

```html
<button
  aria-expanded="false"
  aria-controls="filters">
  Filters
</button>
```

`aria-expanded` expose state cho khả năng tiếp cận API nhưng JavaScript hoặc native behavior phải cập nhật nó khi state thay đổi. `aria-controls` mô tả relationship với element được control; nó không tự open/close target.

Nếu native `details/summary` hoặc Popover đáp ứng use case, chúng thường giảm nguy cơ state visual và ARIA state bị lệch nhau.

---

## 46. `aria-invalid` và `aria-errormessage`

Khi kiểm tra tính hợp lệ (validation) error xuất hiện, control có thể expose invalid state và reference error text:

```html
<label for="email">Email</label>
<input
  id="email"
  name="email"
  aria-invalid="true"
  aria-errormessage="email-error">

<p id="email-error">
  Enter a valid email address.
</p>
```

`aria-invalid` nói current value invalid; `aria-errormessage` identifies error message. Hai attributes không validate value và không automatically show text. Application/native kiểm tra tính hợp lệ (validation) vẫn phải quyết định lỗi và manage lifecycle của message.

Nếu input đang valid, đừng để stale `aria-invalid="true"` chỉ vì UI đã từng có error.

---

## 47. `aria-busy`, live regions và dynamic updates

`aria-busy="true"` có thể báo rằng một region đang được cập nhật và công nghệ hỗ trợ có thể trì hoãn xử lý announcements phù hợp. `aria-live` dùng cho dynamic messages cần announce mà tiêu điểm không chuyển tới đó.

Không biến toàn app thành `aria-live`. Live region quá rộng hoặc `assertive` quá nhiều sẽ gây noise/interruptions. Accessibility tốt là chọn đúng event cần announce, không phải thêm nhiều ARIA nhất có thể.

---

## 48. `aria-hidden`, `hidden`, `inert` và `disabled` khác nhau

`aria-hidden="true"` chủ yếu ảnh hưởng cây trợ năng; element vẫn có thể visible. `hidden` nói content không được present/relevant theo HTML state. `inert` làm subtree non-interactive/focusable theo platform behavior. `disabled` áp cho supported controls và còn ảnh hưởng form submission.

Đặc biệt không đặt `aria-hidden="true"` trên ancestor chứa focusable controls; bạn có thể tạo UI mà keyboard tiêu điểm tới được nhưng trình đọc màn hình không thấy semantic tương ứng.

---

# PHẦN 13 — SECURITY DEEPER

## 49. Sanitization không phải remove `<script>`

Untrusted HTML attack surface gồm event-handler attributes, dangerous URL schemes, SVG/foreign content, `srcdoc`, DOM clobbering và nhiều bộ phân tích cú pháp contexts khác. Regex remove `<script>` không phải sanitizer.

Nếu application thực sự cho phép rich HTML input, dùng sanitizer được thiết kế cho bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) model và áp CSP/Trusted Types hoặc các defense phù hợp architecture. Nếu chỉ cần text, dùng text APIs thay vì HTML phân tích cú pháp APIs.

---

## 50. URL-valued attributes

Escaping HTML characters không tự làm URL safe. Nếu user-controlled value đi vào `href`, `src`, `action` hoặc tương tự, application còn phải validate allowed schemes/origins theo use case.

Ví dụ nếu feature chỉ cho external web links, allowlist `https:`/`http:` phù hợp hơn việc chấp nhận bất kỳ scheme nào. `javascript:` URL là lý do URL kiểm tra tính hợp lệ (validation) và HTML escaping là hai defense khác nhau.

---

## 51. `iframe srcdoc`, sandbox và permissions

`srcdoc` là một HTML document execution context, không phải text container. Untrusted content cần sanitization và sandbox strategy.

`sandbox` nên theo least privilege. `allow`/Permissions Policy chỉ cấp capabilities cần thiết. `referrerpolicy` kiểm soát referrer leakage. Một third-party iframe là browsing/bảo mật boundary chứ không chỉ là visual box.

---

# PHẦN 14 — SSR, FRAMEWORKS VÀ PARSER-STABLE MARKUP

## 52. Valid HTML quan trọng đặc biệt với SSR

JSX có thể viết structure mà trình duyệt bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) sẽ repair. Nếu server output và trình duyệt DOM khác nhau trước khi React/Vue hydrate, framework có thể báo hydration mismatch hoặc replace nodes.

Trình duyệt không parse JSX; trình duyệt parse generated HTML. Vì vậy framework developer vẫn phải hiểu HTML các mô hình nội dung, optional tags, table phân tích cú pháp và interactive-content restrictions.

---

## 53. Declarative Shadow DOM và SSR

Server-rendered custom component có thể gửi declarative shadow template để trình duyệt tạo shadow root trong parse stage. Điều này làm encapsulation/styles tồn tại trước JavaScript upgrade và giảm flash/mismatch trong một số Web Component architectures.

Khi dùng, test bộ phân tích cú pháp behavior, framework support và serialization pipeline; tooling cũ có thể chưa hiểu mô hình nội dung/attributes mới.

---

# PHẦN 15 — LEGACY, DEPRECATED VÀ OBSOLETE HTML

## 54. “Trình duyệt vẫn render” không có nghĩa markup còn hợp chuẩn để author

Web phải giữ backward compatibility với hàng chục năm nội dung cũ. Vì vậy trình duyệt engines vẫn có thể parse/render nhiều lỗi thời elements. Điều này không biến chúng thành lựa chọn đúng cho code mới.

Khi maintain hệ thống cũ system, hãy phân biệt hai câu hỏi: trình duyệt có compatibility behavior cho markup này không, và developer hiện đại có nên author markup này không. Câu trả lời có thể là “có render nhưng không nên viết mới”.

---

## 55. Presentational elements: `<font>`, `<center>`, `<big>` và `<tt>`

Legacy HTML thường trộn structure với presentation:

```html
<center>
  <font color="red" size="5">
    Important
  </font>
</center>
```

Modern HTML chuyển responsibility về đúng layer:

```html
<p class="important">Important</p>
```

và CSS chịu font, color, alignment, size.

`tt` từng tạo teletype/monospace presentation. Khi migrate, hãy chọn semantic replacement theo meaning: `code` cho source code, `kbd` cho user input, `samp` cho program output, `var` cho variable; nếu chỉ muốn monospace visual thì dùng CSS.

`big` không có semantic “quan trọng”; nếu nội dung quan trọng dùng `strong`, nếu chỉ cần cỡ chữ dùng CSS.

---

## 56. `<strike>` và `<acronym>`

`strike` là presentational hệ thống cũ. Nếu content chỉ “không còn đúng/relevant”, `s` thường phù hợp:

```html
<s>$100</s> $70
```

Nếu bạn đang biểu diễn một edit/deletion trong document history, dùng `del`:

```html
<del>$100</del>
<ins>$70</ins>
```

`acronym` không còn là element nên author. Dùng `abbr` khi nội dung là abbreviation/acronym và expansion hữu ích:

```html
<abbr title="Application Programming Interface">API</abbr>
```

Migration tốt không chỉ đổi tên tag; phải xác định meaning ban đầu rồi chọn phần tử mang ngữ nghĩa mới.

---

## 57. `<marquee>`, `<blink>`, `<bgsound>` và motion/audio hệ thống cũ

Các elements kiểu `marquee`, `blink`, `bgsound` xuất phát từ era browser-specific/presentational HTML. Không dùng chúng trong application mới.

Nếu animation thực sự cần thiết, CSS/Web Animations/JavaScript cung cấp control tốt hơn và có thể tôn trọng user preference như reduced motion. Auto-playing background audio thường là UX/khả năng tiếp cận anti-pattern và trình duyệt autoplay policies cũng hạn chế behavior này.

---

## 58. `<frameset>`, `<frame>` và `<noframes>`

Legacy frames chia một trình duyệt window thành nhiều browsing contexts bằng cấu trúc tài liệu đặc biệt. Chúng gây vấn đề với URLs/history, khả năng tiếp cận, navigation, printing và application architecture.

Modern page layout dùng CSS. Nếu thực sự cần embed một independent browsing context, `iframe` là element tương ứng nhưng phải dùng với `title`, sandbox/permissions và bảo mật review. `iframe` không phải replacement cho layout frameset; nó là embedding primitive.

---

## 59. `<applet>`, `<param>`, `<object>` và plugin-era content

`applet` thuộc era Java trình duyệt plugins và không còn là nền tảng web hiện đại. Migration thường là rewrite functionality bằng HTML/CSS/JavaScript/Web APIs hoặc chuyển sang application architecture khác.

`param` gắn với old plugin/object parameter mechanisms và không phải lựa chọn authoring hiện đại. `object` vẫn có những embedding ngữ nghĩa riêng nhưng không nên được dùng để hồi sinh plugin architecture cũ.

---

## 60. `<isindex>`, `<keygen>`, `<listing>`, `<xmp>`, `<plaintext>` và các parser-era relics

Một số lỗi thời elements tồn tại vì lịch sử HTML rất dài. `isindex` từng đại diện input/search primitive cũ; `keygen` từng liên quan key-generation UI; `listing`, `xmp`, `plaintext` gắn với những cách xử lý text/bộ phân tích cú pháp rất cũ.

Khi gặp chúng trong code hệ thống cũ, mục tiêu không phải học cách author lại mà là hiểu intent rồi migrate sang modern form controls hoặc `pre`/`code`/text escaping đúng context.

---

## 61. `<dir>` element khác `dir` thuộc tính toàn cục

Legacy `<dir>` element từng đại diện directory list và không nên dùng mới. Nhưng thuộc tính toàn cục `dir="rtl"`, `dir="ltr"`, `dir="auto"` vẫn là modern, quan trọng cho bidirectional text.

Đây là ví dụ điển hình cho việc cùng spelling có thể xuất hiện ở hai khái niệm lịch sử khác nhau. Đừng xóa `dir` attribute chỉ vì thấy `<dir>` element lỗi thời.

---

## 62. Presentational/hệ thống cũ attributes

Old HTML thường có attributes như `align`, `bgcolor`, `cellpadding`, `cellspacing`, `frameborder` hoặc presentational `border`. Modern authoring nên chuyển presentation sang CSS.

Ví dụ hệ thống cũ:

```html
<table
  border="1"
  cellpadding="8"
  cellspacing="0">
```

Modern markup giữ table ngữ nghĩa còn CSS quản lý border/padding/spacing.

Một số hệ thống cũ attributes vẫn có bộ phân tích cú pháp compatibility hoặc special obsolete-but-conforming exceptions vì web compatibility. Đừng dựa vào việc validator/trình duyệt “vẫn nhận” để quyết định authoring style.

---

## 63. Legacy JavaScript attributes

HTML cũ thường có:

```html
<script
  language="javascript"
  type="text/javascript">
```

Trong modern HTML, classic JavaScript không cần `language` và thường không cần `type="text/javascript"`:

```html
<script src="/app.js"></script>
```

ES modules dùng:

```html
<script type="module" src="/main.js"></script>
```

Khi migrate, phân biệt “hệ thống cũ syntax bỏ được” với “module ngữ nghĩa khác classic script”; không xóa `type="module"` vì tưởng mọi `type` đều lỗi thời.

---

## 64. Anchor `name` và fragment IDs

Legacy markup có thể dùng:

```html
<a name="chapter-1"></a>
```

Modern fragment target nên dùng `id` trên element có meaning:

```html
<section id="chapter-1">
  <h2>Chapter 1</h2>
</section>
```

Điều này tạo URL fragment target mà không cần empty anchor, đồng thời document ngữ nghĩa rõ hơn.

---

## 65. Legacy migration strategy

Đừng chạy search-replace theo tag name mà không hiểu meaning. Quy trình tốt là xác định intent cũ, tìm native modern semantic, chuyển presentation sang CSS, thay plugin/frames architecture nếu cần, sau đó test DOM, keyboard, trình đọc màn hình và trình duyệt compatibility.

Legacy markup thường có hidden coupling với JavaScript selectors hoặc server templates. Vì vậy migration phải có regression tests chứ không chỉ làm validator hết warning.

---

# PHẦN 16 — NATIVE HTML TRƯỚC CUSTOM JAVASCRIPT

## 66. Disclosure, dialog, popover và forms

Nếu requirement chỉ là disclosure, `details/summary` có thể đủ. Nếu là modal, `dialog` thường tốt hơn generic div. Nếu là floating transient UI, Popover có thể cung cấp top-layer/light-dismiss primitive. Nếu là kiểm tra tính hợp lệ (validation), hãy bắt đầu với `required`, type constraints, min/max/pattern trước khi replace toàn bộ bằng JavaScript.

Native-first không có nghĩa “không được custom”. Nó nghĩa bạn tận dụng behavior/khả năng tiếp cận trình duyệt đã implement, rồi enhance nơi business requirement thật sự vượt quá native primitive.

---

# PHẦN 17 — DEBUG EXERCISES

## 67. Parser repair

Đưa source sau vào trình duyệt rồi so sánh View Source với Elements:

```html
<p>
  Hello
  <div>World</div>
</p>
```

Mục tiêu là thấy source indentation không quyết định DOM.

---

## 68. Attribute/property state

```html
<form id="f">
  <input id="name" value="Alice">
</form>
```

Trong console, sửa `el.value = "Bob"`, rồi so sánh `el.value`, `el.defaultValue`, `el.getAttribute("value")`; cuối cùng chạy `f.reset()`. Bài này giúp hiểu trạng thái hiện tại, trạng thái mặc định và thuộc tính nội dung bằng trải nghiệm trực tiếp.

---

## 69. Checkbox state

Với:

```html
<input id="agree" type="checkbox" checked>
```

user uncheck rồi so sánh `checked`, `defaultChecked`, `getAttribute("checked")`. Đây là một trong những ví dụ rõ nhất cho DOM relation.

---

## 70. Form owner

Đặt submit button ngoài form nhưng dùng `form="profile"`, rồi quan sát trình duyệt vẫn submit đúng owner. Sau đó thử disabled/readonly/unchecked controls và inspect `FormData` để thấy successful-controls rules.

---

## 71. DOM clobbering

Tạo form có `<input name="method">` và inspect `form.method`. Mục tiêu không phải exploit, mà là thấy tại sao named access không nên được dùng như trusted object property model.

---

## 72. Popover và until-found

Tạo một native popover rồi so sánh lượng JavaScript cần thiết với custom overlay. Sau đó tạo section `hidden="until-found"`, dùng Find in page hoặc fragment navigation trên trình duyệt hỗ trợ và quan sát trình duyệt reveal content.

---

# PHẦN 18 — MASTER REVIEW MENTAL MODEL

Khi review production HTML, hãy đi theo một flow ổn định. Trước hết kiểm tra bộ phân tích cú pháp/mô hình nội dung: source sẽ tạo DOM gì, trình duyệt có repair không, SSR có hydration risk không. Sau đó kiểm tra ngữ nghĩa: element có biểu diễn đúng meaning không, link và button có đúng role native không, headings và landmarks có structure hợp lý không.

Tiếp theo kiểm tra khả năng tiếp cận: tên trợ năng đến từ đâu, description có đúng không, keyboard order có tự nhiên không, ARIA state có sync visual state không, custom role có đang thay native element vô lý không. Với form, xác định biểu mẫu chủ quản, điều khiển gửi biểu mẫu và control nào thực sự được submit.

Với bảo mật, xác định user-controlled data đi vào text, URL, raw HTML, iframe hay script context; kiểm tra sandbox, referrer/CORS, sanitization/CSP strategy. Với hiệu năng, xem critical resources được discover khi nào, LCP image có intrinsic dimensions không, script có chặn bộ phân tích cú pháp (parser-blocking) không và các gợi ý tải tài nguyên (resource hints) có được đo thực tế không.

Cuối cùng, nếu gặp markup hệ thống cũ, đừng hỏi “Chrome còn render không?” mà hỏi “meaning cũ là gì và modern semantic/CSS/API nào thay thế đúng?”.

---

# PHẦN 19 — FULL HTML PLATFORM MENTAL MODEL

HTML source chỉ là điểm bắt đầu:

```text
HTTP response / bytes
↓
character decoding
↓
HTML tokenizer
↓
tree construction + parser recovery
↓
DOM + live IDL properties
↓
CSSOM / layout / paint
↓
accessibility tree
↓
resource loading / scripts / CORS policies
↓
form and native interaction algorithms
↓
framework hydration/mutation
↓
user interaction
```

Một tag quan trọng vì nó tham gia một hoặc nhiều layers trong flow này. `button` không chỉ là rectangle: nó có activation, tiêu điểm, khả năng tiếp cận và form ngữ nghĩa. `img` không chỉ hiển thị pixels: nó có alternative text, intrinsic dimensions, resource selection và network priority implications. `script` không chỉ load JavaScript: nó tương tác bộ phân tích cú pháp, module graph, CSP/SRI và kết xuất path.

---

# PHẦN 20 — AUDIT HOÀN THIỆN COVERAGE CÒN THIẾU

Phần này khép những khoảng nhỏ còn lại sau khi audit toàn bộ canonical HTML notes theo cấu trúc tài liệu, ngữ nghĩa, siêu dữ liệu, tables, forms, kiểm tra tính hợp lệ (validation), DOM, khả năng tiếp cận, hiệu năng, bảo mật, modern HTML và hệ thống cũ HTML. Các mục dưới đây không phải danh sách thuộc lòng; mục tiêu vẫn là hiểu **meaning → trình duyệt processing → lúc dùng → semantic/khả năng tiếp cận implication**.

## 73. `<colgroup>` và `<col>`: mô tả nhóm cột, không phải header thay thế

Trong table, `colgroup` và `col` cho phép author mô tả hoặc style một nhóm cột mà không cần lặp class trên từng cell:

```html
<table>
  <caption>Monthly sales</caption>

  <colgroup>
    <col>
    <col class="money-column">
  </colgroup>

  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Revenue</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Keyboard</th>
      <td>$10,000</td>
    </tr>
  </tbody>
</table>
```

Trình duyệt dùng column model của table để áp dụng một số presentation/column properties phù hợp. Nhưng `col` không thay `th`: nó không tạo accessible header relationship cho data cells. Nếu column có meaning cần trình đọc màn hình hiểu, vẫn dùng `th`, `scope`, và với table phức tạp có thể cần `headers`/`id` association. Senior review vì vậy phải tách **column structural grouping** khỏi **header ngữ nghĩa**.

---

## 74. Những `input type` dễ bị bỏ sót: `submit`, `reset`, `button`, `image`

`<input type="submit">` tạo submit control tương tự submit button nhưng label đến từ `value`. `<input type="button">` tạo generic push button nhưng không có rich child content như `<button>`. `<input type="reset">` restore default form state, không phải “xóa tất cả về rỗng”. Với application UI hiện đại, `<button>` thường expressive hơn vì chứa được markup và text linh hoạt.

`<input type="image">` là submit control dùng image. Nếu phải dùng, `alt` có khả năng tiếp cận meaning rất quan trọng vì image là label của control:

```html
<input
  type="image"
  src="/pay.png"
  alt="Pay now">
```

Trình duyệt còn có thể submit click coordinates theo form ngữ nghĩa. Vì behavior khá đặc thù, đừng dùng `type="image"` chỉ để có một button đẹp; ordinary `<button>` + CSS thường rõ ràng hơn.

---

## 75. `form`, `novalidate`, `formnovalidate` và `accept-charset`

`form="id"` cho phép một form-associated control thuộc form ngay cả khi nó không nằm trong subtree form đó. Trình duyệt resolve ID tới biểu mẫu chủ quản, vì vậy visual layout và form ownership không nhất thiết trùng nhau.

`novalidate` trên `<form>` tắt interactive kiểm tra ràng buộc (constraint kiểm tra tính hợp lệ (validation)) của trình duyệt cho submission đó:

```html
<form action="/save" method="post" novalidate>
```

`formnovalidate` trên điều khiển gửi biểu mẫu cho phép bỏ kiểm tra tính hợp lệ (validation) chỉ với một action, ví dụ “Save draft” trong khi “Publish” vẫn validate:

```html
<button type="submit">Publish</button>
<button type="submit" formnovalidate>Save draft</button>
```

Hai attributes này không có nghĩa server được bỏ kiểm tra tính hợp lệ (validation). Chúng chỉ thay đổi browser-side constraint-validation step.

`accept-charset` mô tả encoding dùng cho form submission. Trong modern HTML, UTF-8 là encoding cần nghĩ tới; đừng xây architecture phụ thuộc hệ thống cũ encodings nếu không có contract bắt buộc.

---

## 76. Native kiểm tra ràng buộc (constraint kiểm tra tính hợp lệ (validation)) thực sự hoạt động thế nào?

Các attributes như `required`, `type="email"`, `min`, `max`, `step`, `pattern`, `minlength` và `maxlength` tham gia **kiểm tra ràng buộc (constraint kiểm tra tính hợp lệ (validation)) model**. Trình duyệt không chỉ “đọc attribute rồi đổi viền đỏ”; control có live validity state trong DOM.

Ví dụ:

```js
const email = document.querySelector('#email');

email.checkValidity();
email.reportValidity();
console.log(email.validity);
console.log(email.validationMessage);
```

`checkValidity()` kiểm tra và trả boolean; `reportValidity()` còn có thể yêu cầu trình duyệt present kiểm tra tính hợp lệ (validation) UI. `ValidityState` cho biết lý do như `valueMissing`, `typeMismatch`, `patternMismatch`, `tooLong`, `rangeUnderflow` hoặc `stepMismatch` tùy control.

Custom rule có thể dùng:

```js
email.setCustomValidity('Email is already registered');
```

Nhưng khi lỗi đã hết phải reset bằng empty string, nếu không control sẽ tiếp tục invalid. Accessibility-wise, native kiểm tra tính hợp lệ (validation) message không thay thế requirement làm error state rõ, associate helper/error text phù hợp và bảo đảm keyboard/screen-reader user hiểu lỗi. Server-side kiểm tra tính hợp lệ (validation) vẫn là authority cuối cùng.

---

## 77. `accept`, `list`, `size`, `placeholder`: hint, association và presentation khác nhau

`accept` trên file input là hint cho file picker về MIME type/extension mong muốn:

```html
<input
  type="file"
  accept="image/png,image/jpeg">
```

Trình duyệt có thể lọc picker UI, nhưng attacker vẫn có thể gửi file khác bằng request thủ công, nên server phải inspect content/type/size độc lập.

`list="id"` nối input với `datalist` để trình duyệt cung cấp suggestions. Nó không biến input thành closed enum; user vẫn có thể nhập value khác nếu kiểm tra tính hợp lệ (validation) không cấm.

`size` ảnh hưởng kích thước hiển thị ở một số text/select controls nhưng không giới hạn độ dài dữ liệu; `maxlength` mới liên quan length constraint. `placeholder` là hint ngắn, không phải label. Các attributes trông giống “UI config”, nhưng mỗi cái tác động một layer khác nên không được dùng thay thế lẫn nhau.

---

## 78. `accesskey`, `autocapitalize` và `autocorrect`

`accesskey` có thể gán shortcut activation/tiêu điểm, nhưng actual key combination phụ thuộc trình duyệt và operating system. Shortcut tự chọn còn có thể conflict với trình duyệt, công nghệ hỗ trợ hoặc user conventions. Vì vậy đây không phải attribute nên rải khắp application chỉ để “hỗ trợ keyboard”. Natural tab order và native controls quan trọng hơn.

`autocapitalize` và `autocorrect` là hints cho supported input methods, đặc biệt mobile keyboards. Ví dụ username hoặc code field có thể không muốn automatic capitalization/correction, trong khi prose field có thể hưởng lợi. Chúng không validate content và không thay business normalization.

---

## 79. `loading="lazy"` trên iframe và trách nhiệm khả năng tiếp cận vẫn còn nguyên

Không chỉ image, iframe phù hợp cũng có thể dùng lazy quá trình tải để trì hoãn fetch khi nó còn xa viewport:

```html
<iframe
  src="https://example.com/embed"
  title="Interactive map"
  loading="lazy">
</iframe>
```

Trình duyệt quyết định scheduling dựa trên heuristics. `loading="lazy"` là hiệu năng hint, không phải guarantee chính xác thời điểm request.

Lazy quá trình tải không thay semantic requirement. Iframe vẫn cần `title` hữu ích; nếu third-party content critical cho task, phải test keyboard/tiêu điểm/quá trình tải states và phương án dự phòng UX. Đừng lazy-load content ngay đầu viewport nếu điều đó làm user chờ phần chính của page.

---

## 80. `meta name="theme-color"` và `link rel="manifest"`

`theme-color` cho phép page gợi ý màu trình duyệt UI trong supporting environments:

```html
<meta
  name="theme-color"
  content="#ffffff">
```

Có thể dùng `media` trong relevant siêu dữ liệu scenarios để có value phù hợp light/dark preferences. Đây là browser-chrome siêu dữ liệu, không phải substitute cho CSS background hay accessible contrast trong page content.

PWA/web-app siêu dữ liệu còn có thể liên kết manifest:

```html
<link rel="manifest" href="/site.webmanifest">
```

Trình duyệt fetch manifest như một external resource khi feature/platform cần. Manifest chứa app-level siêu dữ liệu như name, icons, display behavior; HTML `link` chỉ khai báo relationship. SEO không tự tốt hơn vì có manifest, và khả năng tiếp cận của page vẫn phụ thuộc markup/content thực tế.

---

## 81. `blocking="render"`: khi author chủ động đánh dấu chặn kết xuất (render-blocking)

HTML hiện đại có `blocking` trên các element resource phù hợp như `link`, `script`, `style`; token hiện tại đáng quan tâm là `render`.

Concept:

```html
<link
  rel="stylesheet"
  href="/critical.css"
  blocking="render">
```

Attribute này tham gia trình duyệt kết xuất pipeline, không phải network priority flag chung. `blocking="render"` và `fetchpriority="high"` giải quyết hai concerns khác nhau: một cái liên quan việc operation nào có thể bị block chờ resource, cái kia là scheduling hint cho fetch.

Không thêm `blocking="render"` bừa. Render-blocking resource kéo dài critical path nếu resource chậm. Chỉ dùng khi bạn hiểu chính xác vì sao page phải đợi resource đó trước kết xuất và đã đo hiệu năng.

---

## 82. Declarative Shadow DOM 2026: không chỉ có `shadowrootmode`

Ngoài `shadowrootmode`, platform hiện còn định nghĩa thêm các attributes cho declarative shadow-root configuration. `shadowrootdelegatesfocus` liên quan tiêu điểm delegation; `shadowrootclonable` cho biết shadow root có thể tham gia cloning behavior; `shadowrootserializable` liên quan việc shadow root có thể được serialize bởi các HTML serialization APIs phù hợp; `shadowrootslotassignment` chọn named hay manual slot assignment; `shadowrootcustomelementregistry` phục vụ architecture dùng custom-element registry gắn với shadow root.

Ví dụ concept:

```html
<template
  shadowrootmode="open"
  shadowrootserializable
  shadowrootclonable
  shadowrootslotassignment="named">
  <slot></slot>
</template>
```

Đây là infrastructure-level HTML. Beginner không cần dùng, nhưng senior làm Web Components/SSR phải biết chúng tác động **browser-created ShadowRoot**, không phải chỉ là arbitrary data attributes. Trình duyệt/tooling support vẫn phải được kiểm tra theo target environment, đặc biệt với options mới hơn.

---

## 83. `interestfor`: hiểu hướng phát triển nhưng chưa coi là baseline production

Interest invoker là một hướng mới cho phép control biểu diễn “interest” như hover/tiêu điểm để target có thể phản ứng, thường kết hợp với `popover="hint"`. Một concept markup có thể trông như:

```html
<button interestfor="user-preview">
  Alice
</button>

<div id="user-preview" popover="hint">
  Profile preview
</div>
```

Ý tưởng platform là trình duyệt có thể giúp chuẩn hóa hover/focus-interest relationship thay vì mỗi framework tự viết timers, pointer/tiêu điểm coordination và tooltip state machine.

Tuy nhiên ở thời điểm audit tháng 9/2026, `interestfor`/related DOM APIs vẫn cần được xem là **experimental/limited-availability** chứ không phải capability mà production code có thể assume cross-browser. Hãy dùng nó như kiến thức về hướng phát triển của platform; nếu triển khai thực tế, feature-detect/progressive-enhance và giữ phương án dự phòng ngữ nghĩa hoạt động được.

---

# KẾT LUẬN

HTML mastery không phải khả năng thuộc một danh sách 150 tags. Nó là khả năng giải thích **meaning → trình duyệt processing → use case → semantic consequence → khả năng tiếp cận/bảo mật/hiệu năng implication** của markup quan trọng.

Khi bạn hiểu vì sao trình duyệt tự đóng `p`, vì sao invalid table markup có thể đổi DOM, vì sao `input.value` khác `getAttribute("value")`, vì sao disabled controls không submit, vì sao `role="button"` không tự tạo keyboard behavior, vì sao Popover/Dialog nằm trong lớp trên cùng, vì sao DOM clobbering tồn tại, và vì sao `<font>` vẫn có thể render nhưng không còn là authoring practice đúng, bạn đã chuyển từ “biết HTML syntax” sang **hiểu HTML platform**.
