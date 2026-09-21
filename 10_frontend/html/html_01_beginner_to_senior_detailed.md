# HTML — Beginner → Senior
## Tài liệu học HTML từ số 0 đến mức có thể thiết kế và review mã đánh dấu môi trường thực tế

Tài liệu này được viết cho người học HTML từ đầu, không giả định bạn đã có kiến thức về giao diện web (frontend). Mục tiêu không phải là giúp bạn nhớ thật nhiều thẻ (tag), mà là xây một mô hình tư duy đủ chắc để hiểu trình duyệt xử lý HTML như thế nào, vì sao HTML ngữ nghĩa quan trọng, khi nào nên dùng một phần tử (element) thay vì `div`, biểu mẫu (form) thực sự gửi dữ liệu (submit) ra sao, vì sao khả năng tiếp cận và SEO liên quan trực tiếp tới mã đánh dấu, và HTML ảnh hưởng đến bảo mật lẫn hiệu năng như thế nào.

Nếu đọc tuần tự từ đầu đến cuối, bạn phải có thể đi từ việc viết một trang HTML cơ bản tới việc review mã đánh dấu ở mức senior: hiểu cấu trúc tài liệu, các phần tử mang ngữ nghĩa, links, images, tables, forms, khả năng tiếp cận, quá trình tải script, siêu dữ liệu, ảnh đáp ứng, iframe, các phần tử tương tác gốc của trình duyệt và những lỗi môi trường thực tế phổ biến.


## Quy ước thuật ngữ trong tài liệu

Tài liệu dùng tiếng Việt tự nhiên làm ngôn ngữ giải thích chính và giữ thuật ngữ gốc ở lần định nghĩa để tiện đối chiếu. Các cách gọi được dùng thống nhất gồm: **trình duyệt (browser)**, **mã đánh dấu (markup)**, **mã nguồn (source)**, **tài liệu (document)**, **phần tử (element)**, **thuộc tính (attribute)**, **biểu mẫu (form)**, **gửi biểu mẫu (submit)**, **bố cục (layout)**, **hành vi (behavior)**, **tính năng (feature)**, **mô hình tư duy (mental model)**, **phân tích cú pháp (parsing)**, **bộ phân tích cú pháp (parser)**, **HTML ngữ nghĩa (semantic HTML)**, **ngữ nghĩa (semantics)**, **khả năng tiếp cận (accessibility)**, **cây trợ năng (accessibility tree)**, **tên trợ năng (accessible name)**, **siêu dữ liệu (metadata)**, **kiểm tra ràng buộc của biểu mẫu (constraint validation)**, **mô hình nội dung (content model)**, **thuộc tính DOM (DOM property)**, **trạng thái hiện thời (live state)**, **lớp trên cùng (top layer)**, **hiệu năng (performance)**, **bảo mật (security)**, **đáp ứng (responsive)** và **môi trường thực tế (production)**. Sau khi thuật ngữ đã được định nghĩa, phần nội dung ưu tiên cách gọi tiếng Việt để câu văn nhẹ và dễ học. Những tên chuẩn được dùng phổ biến hơn bằng tiếng Anh như DOM, ARIA, CORS, CSP, Shadow DOM, Web Components, `iframe`, framework, tên tag, tên attribute và tên API cụ thể được giữ nguyên khi dịch sẽ làm mất nghĩa hoặc gây khó tra cứu.

---

# PHẦN 1 — HTML LÀ GÌ VÀ TRÌNH DUYỆT (BROWSER) HIỂU NÓ THẾ NÀO?

## 1. HTML không phải ngôn ngữ lập trình

HTML là viết tắt của **HyperText Markup Language**. Nó là ngôn ngữ đánh dấu dùng để mô tả cấu trúc và ý nghĩa của nội dung trên web.

Ví dụ:

```html
<h1>My Profile</h1>
<p>Hello, my name is Alice.</p>
```

HTML không chứa logic theo nghĩa như Java hoặc JavaScript. Nó không có vòng lặp, class business logic hay thuật toán. Vai trò chính của HTML là mô tả:

```text
đây là heading
đây là paragraph
đây là link
đây là image
đây là form
đây là button
```

Trình duyệt phân tích cú pháp (parse) HTML để tạo DOM. CSS dựa trên cấu trúc DOM/phần tử để quyết định cách trình bày (presentation), còn JavaScript tương tác với DOM để bổ sung hành vi (behavior).

Mental model đơn giản:

```text
HTML → structure + semantics
CSS  → presentation
JS   → behavior
```

Trong dự án hiện đại, ba tầng này có thể được xây dựng thông qua framework như React hoặc Vue, nhưng cuối cùng trình duyệt vẫn phải làm việc với DOM mang đúng ngữ nghĩa HTML.

---

## 2. `<!doctype html>`

Một HTML document hiện đại nên bắt đầu:

```html
<!doctype html>
```

DOCTYPE nói với trình duyệt rằng document phải được render theo standards mode hiện đại.

Nó không phải một HTML element và cũng không phải closing-tag syntax.

Nếu thiếu doctype, trình duyệt có thể rơi vào **quirks mode**, nơi một số bố cục/CSS các hành vi mô phỏng web rất cũ để tương thích với hệ thống cũ pages.

Vì vậy môi trường thực tế HTML gần như luôn có:

```html
<!doctype html>
```

ở dòng đầu.

---

## 3. Cấu trúc tối thiểu của một HTML document

Một document chuẩn thường có dạng:

```html
<!doctype html>

<html lang="vi">
<head>
  <meta charset="utf-8">
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1">

  <title>My Page</title>
</head>

<body>
  <h1>Hello</h1>
</body>
</html>
```

Bạn nên hiểu từng tầng thay vì chỉ copy skeleton.

`html` là document element. `head` chứa siêu dữ liệu và resources liên quan document. `body` chứa nội dung chính được render/interact.

---

# PHẦN 2 — ROOT DOCUMENT VÀ METADATA

## 4. `<html>`

`<html>` là root element của HTML document.

```html
<html lang="vi">
```

Attribute quan trọng nhất là `lang`.

Nếu page chủ yếu bằng tiếng Việt:

```html
<html lang="vi">
```

Nếu page chủ yếu bằng tiếng Hàn:

```html
<html lang="ko">
```

Nếu tiếng Anh:

```html
<html lang="en">
```

`lang` không chỉ dành cho search engines. Screen reader có thể dùng nó để chọn pronunciation rules. Trình duyệt translation, spell checking và khả năng tiếp cận tools cũng dựa vào language siêu dữ liệu.

Nếu chỉ một đoạn dùng ngôn ngữ khác, khai báo ở subtree:

```html
<p>
  Trong tiếng Hàn,
  <span lang="ko">안녕하세요</span>
  nghĩa là xin chào.
</p>
```

---

## 5. `dir`

`dir` mô tả text direction:

```html
<html dir="ltr">
```

Các giá trị quan trọng:

```text
ltr
rtl
auto
```

`rtl` thường dùng với Arabic/Hebrew contexts.

`auto` hữu ích với user-generated content khi language direction chưa biết trước.

Semantic direction nên được biểu diễn bằng `dir` khi nó thuộc nội dung, thay vì chỉ dựa vào CSS `direction`.

---

## 6. `<head>`

`head` chứa siêu dữ liệu và resources, không phải phần content chính mà user đọc.

Ví dụ:

```html
<head>
  <meta charset="utf-8">
  <title>Orders</title>
  <meta
    name="description"
    content="Order management dashboard">

  <link
    rel="stylesheet"
    href="/app.css">
</head>
```

Trình duyệt có thể discover CSS, scripts, icons, siêu dữ liệu và preload hints trong `head`.

Source order trong `head` cũng có thể ảnh hưởng hiệu năng vì trình duyệt discover resources theo thứ tự parse.

---

## 7. `<meta charset="utf-8">`

Khai báo encoding:

```html
<meta charset="utf-8">
```

UTF‑8 là encoding phù hợp gần như mọi web application hiện đại.

Đặt declaration sớm trong `head` để trình duyệt biết cách decode bytes đúng trước khi parse content.

Nếu encoding bị hiểu sai, tiếng Việt/Hàn/Nhật có thể trở thành mojibake.

---

## 8. Viewport siêu dữ liệu

Mobile trang đáp ứng thường dùng:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1">
```

Nếu thiếu viewport siêu dữ liệu, mobile trình duyệt có thể giả định một desktop-like khung nhìn bố cục (bố cục viewport) rồi scale page xuống. Khi đó CSS media queries và bố cục có thể không hoạt động như bạn mong đợi.

Không nên disable user zoom bừa bằng:

```text
user-scalable=no
maximum-scale=1
```

vì zoom là khả năng tiếp cận capability quan trọng.

---

## 9. `<title>`

`title` định nghĩa tên document:

```html
<title>Order #1234 – Admin Portal</title>
```

Nó xuất hiện ở trình duyệt tab, bookmark/history và có thể được search engine dùng làm result title.

Một page môi trường thực tế nên có title cụ thể và khác nhau giữa các page quan trọng.

Ví dụ yếu:

```html
<title>Home</title>
```

Ví dụ tốt hơn:

```html
<title>Dashboard – Acme Admin</title>
```

---

## 10. Meta description

```html
<meta
  name="description"
  content="Manage orders, refunds and payment status.">
```

Description có thể được search engine sử dụng làm snippet.

Nó không phải “keyword hack”. Nên viết một câu mô tả thật sự hữu ích cho người đang cân nhắc click result.

---

## 11. `<link>`

`link` kết nối document với external resource hoặc mô tả relationship.

Stylesheet:

```html
<link
  rel="stylesheet"
  href="/app.css">
```

Favicon:

```html
<link
  rel="icon"
  href="/favicon.svg">
```

Canonical URL:

```html
<link
  rel="canonical"
  href="https://example.com/products/123">
```

Preconnect:

```html
<link
  rel="preconnect"
  href="https://cdn.example.com">
```

Preload:

```html
<link
  rel="preload"
  href="/hero.webp"
  as="image">
```

Ở level beginner, chỉ cần hiểu `rel` mô tả relationship và `href` chỉ resource. Ở level senior, cần biết preload/preconnect có thể giúp hoặc làm hại hiệu năng nếu sử dụng bừa.

---

## 12. `<base>`

`base` thay đổi cách relative URLs được resolve:

```html
<base href="/app/">
```

Sau đó:

```html
<a href="users">
```

có thể resolve thành `/app/users`.

`base` ảnh hưởng rất rộng: links, images, forms, scripts và fragment navigation có thể bị tác động. Vì vậy môi trường thực tế application hiếm khi dùng nếu routing/toolchain đã quản lý URL tốt.

Khi debug một page có relative URLs kỳ lạ, hãy nhớ kiểm tra `<base>`.

---

# PHẦN 3 — BODY VÀ SEMANTIC STRUCTURE

## 13. `<body>`

`body` chứa content của document mà user chủ yếu nhìn thấy và tương tác:

```html
<body>
  <header>...</header>
  <main>...</main>
  <footer>...</footer>
</body>
```

Trình duyệt parse body mã đánh dấu thành DOM. JavaScript framework có thể mutate DOM sau đó, nhưng ngữ nghĩa cuối vẫn dựa trên elements thực tế.

---

## 14. Vì sao HTML ngữ nghĩa quan trọng?

Bạn có thể xây gần như mọi giao diện bằng:

```html
<div>
```

và CSS.

Nhưng mã đánh dấu:

```html
<div class="nav">
```

không nói với trình duyệt/cây trợ năng rằng đây là navigation.

Markup:

```html
<nav>
```

có semantic rõ.

Semantic HTML giúp các trình đọc màn hình, người dùng bàn phím, search engines và chính developer hiểu cấu trúc tài liệu.

Senior HTML không có nghĩa “không bao giờ dùng div”. Nó nghĩa là dùng phần tử mang ngữ nghĩa khi ngữ nghĩa phù hợp và dùng `div` khi chỉ cần generic grouping/bố cục.

---

## 15. `<header>`

`header` là phần giới thiệu/header của page hoặc một section.

Page-level:

```html
<header>
  <h1>Acme</h1>
  <nav>...</nav>
</header>
```

Article-level:

```html
<article>
  <header>
    <h2>How HTML Parsing Works</h2>
    <p>Published 12 Sep 2026</p>
  </header>
</article>
```

Một page có thể có nhiều `header` nếu chúng thuộc các sections/articles khác nhau.

---

## 16. `<main>`

`main` biểu diễn nội dung chính của document:

```html
<main>
  ...
</main>
```

Nó tạo landmark hữu ích cho công nghệ hỗ trợ. User dùng trình đọc màn hình có thể nhảy nhanh tới main content mà không phải tab/nghe toàn navigation.

Thông thường chỉ nên có một main đang active/visible cho document.

---

## 17. `<footer>`

Footer có thể thuộc toàn page hoặc article/section.

Page footer:

```html
<footer>
  <small>© 2026 Acme</small>
</footer>
```

Article footer có thể chứa:

```text
author
tags
publication metadata
related links
```

Đừng hiểu `footer` chỉ là “phần ở dưới màn hình”. Nó là semantic footer của sectioning context.

---

## 18. `<nav>`

`nav` dùng cho một nhóm navigation links quan trọng:

```html
<nav aria-label="Main navigation">
  <a href="/">Home</a>
  <a href="/products">Products</a>
</nav>
```

Nếu có nhiều navigation regions, accessible label giúp phân biệt:

```html
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Footer navigation">...</nav>
```

Không phải mọi nhóm links đều cần `nav`. Một list links nhỏ trong article có thể chỉ là list bình thường.

---

## 19. `<section>`

`section` dùng khi một phần nội dung có chủ đề riêng và thường có heading:

```html
<section>
  <h2>Features</h2>
  ...
</section>
```

Nếu bạn chỉ cần wrapper cho CSS grid/flex mà không có semantic section, `div` thường đúng hơn.

Một common beginner mistake là thay tất cả `div` bằng `section` vì nghĩ semantic luôn tốt hơn. Semantic sai không tốt hơn generic element.

---

## 20. `<article>`

`article` phù hợp với nội dung có thể tương đối độc lập:

```html
<article>
  <h2>Understanding HTML Forms</h2>
  <p>...</p>
</article>
```

Ví dụ:

```text
blog post
news item
forum post
comment
product listing unit
independent widget
```

Mental test: nếu copy phần này ra khỏi page, nó vẫn có ý nghĩa độc lập không? Nếu có, `article` có thể phù hợp.

---

## 21. `<aside>`

`aside` biểu diễn nội dung phụ hoặc tangentially related:

```html
<aside>
  <h2>Related articles</h2>
  ...
</aside>
```

Không dùng `aside` chỉ vì CSS đặt nó bên phải. Vị trí visual không quyết định ngữ nghĩa.

---

## 22. `<address>`

`address` dùng cho contact information liên quan tới page/article:

```html
<address>
  Contact
  <a href="mailto:support@example.com">
    support@example.com
  </a>
</address>
```

Nó không phải generic tag cho mọi postal address.

---

# PHẦN 4 — HEADINGS VÀ TEXT STRUCTURE

## 23. `<h1>` đến `<h6>`

Heading biểu diễn hierarchy.

```html
<h1>HTML Guide</h1>

<h2>Forms</h2>

<h3>Input Types</h3>
```

Đừng chọn heading theo font size. Nếu muốn text lớn hơn, dùng CSS.

Heading hierarchy giúp user scan page, trình đọc màn hình navigation và search engine hiểu structure.

Một senior review sẽ kiểm tra “heading có mô tả hierarchy nội dung đúng không?” chứ không chỉ “có h1 chưa?”.

---

## 24. `<p>`

Paragraph:

```html
<p>
  HTML describes the structure and semantics of a document.
</p>
```

`p` dành cho paragraph text, không phải generic container.

Không nên đặt block structures không phù hợp bên trong `p`; trình duyệt bộ phân tích cú pháp có thể tự đóng `p`, khiến DOM khác source bạn tưởng. Phần Master sẽ giải thích bộ phân tích cú pháp hành vi này kỹ hơn.

---

## 25. `<div>`

`div` là generic flow container:

```html
<div class="card">
  ...
</div>
```

Nó không mang semantic riêng.

Dùng `div` khi bạn chỉ cần grouping/bố cục hoặc khi không có phần tử mang ngữ nghĩa phù hợp.

Một senior không tránh `div`; senior tránh **div soup khi ngữ nghĩa gốc của phần tử đã tồn tại**.

---

## 26. `<span>`

`span` là generic inline/phrasing container:

```html
<p>
  Price:
  <span class="price">$100</span>
</p>
```

Nó không mang ngữ nghĩa riêng.

Dùng để style hoặc attach hành vi/data cho một đoạn inline khi không có phần tử mang ngữ nghĩa thích hợp.

---

## 27. `<br>`

`br` tạo line break:

```html
123 Main Street<br>
Seoul
```

Phù hợp khi line break là một phần nội dung, ví dụ address hoặc poem.

Không dùng:

```html
<br><br><br>
```

để tạo spacing. Spacing thuộc CSS.

---

## 28. `<hr>`

`hr` biểu diễn thematic break:

```html
<section>Topic A</section>

<hr>

<section>Topic B</section>
```

Trình duyệt thường render một đường ngang, nhưng semantic chính không phải “vẽ line”.

---

# PHẦN 5 — TEXT SEMANTICS

## 29. `<strong>` và `<b>`

`strong` biểu diễn strong importance:

```html
<strong>Do not share your password.</strong>
```

`b` chủ yếu thu hút attention mà không nói nội dung quan trọng hơn về ngữ nghĩa:

```html
<b>Keyword:</b> HTML
```

Cả hai thường bold mặc định, nhưng ý nghĩa khác.

Nếu mục tiêu chỉ là font-weight, CSS mới là công cụ styling.

---

## 30. `<em>` và `<i>`

`em` biểu diễn stress emphasis:

```html
I <em>really</em> need this.
```

`i` dùng cho alternate voice, technical term, taxonomy, foreign phrase hoặc convention phù hợp:

```html
<i lang="la">Homo sapiens</i>
```

Trình duyệt thường italic cả hai, nhưng ngữ nghĩa khác.

---

## 31. `<mark>`

`mark` highlight content relevant trong context:

```html
Search result:
<mark>HTML</mark>
```

Rất phù hợp với search result highlighting hoặc đoạn được reference.

---

## 32. `<small>`

`small` dành cho side comments/small print:

```html
<small>Terms and conditions apply.</small>
```

Không nên dùng chỉ vì muốn font-size nhỏ.

---

## 33. `<s>`, `<del>` và `<ins>`

`s` biểu diễn content không còn accurate/relevant:

```html
<s>$100</s> $70
```

`del` và `ins` biểu diễn edit history:

```html
<del>$100</del>
<ins>$70</ins>
```

Có thể thêm siêu dữ liệu như `datetime`.

Nếu đang hiển thị old price, `s` thường hợp hơn `del`, vì bạn không nhất thiết đang mô tả document edit.

---

## 34. `<code>`, `<pre>`, `<kbd>`, `<samp>`, `<var>`

Inline code:

```html
<code>npm install</code>
```

Code block:

```html
<pre><code>const x = 1;</code></pre>
```

`pre` preserve whitespace.

`kbd` biểu diễn user input:

```html
Press <kbd>Ctrl</kbd> + <kbd>C</kbd>.
```

`samp` biểu diễn program output:

```html
<samp>404 Not Found</samp>
```

`var` biểu diễn variable:

```html
<var>x</var> + <var>y</var>
```

Những tags này giúp technical documentation có ngữ nghĩa rõ hơn.

---

## 35. `<abbr>`

```html
<abbr title="HyperText Markup Language">
  HTML
</abbr>
```

Dùng cho abbreviation.

`title` chỉ nên là supplemental information, không nên là nơi duy nhất chứa critical information vì touch/assistive environments không phải lúc nào expose tooltip giống desktop mouse.

---

## 36. `<blockquote>` và `<q>`

Block quote:

```html
<blockquote>
  The Web is for everyone.
</blockquote>
```

Inline quote:

```html
<p>He said <q>Hello</q>.</p>
```

`blockquote[cite]` có thể chứa source URI siêu dữ liệu, nhưng trình duyệt không tự hiển thị citation cho user.

---

## 37. `<cite>`

`cite` biểu diễn title của creative work:

```html
<cite>Clean Code</cite>
```

Không phải generic “nguồn URL” tag.

---

## 38. `<time>`

```html
<time datetime="2026-09-12">
  12 Sep 2026
</time>
```

`datetime` cung cấp machine-readable representation.

Date/time ngữ nghĩa hữu ích với structured content, parsers và machine processing.

---

## 39. `<data>`

```html
<data value="SKU-123">
  Blue Shirt
</data>
```

Visible text có thể khác machine value.

Hữu ích trong product/catalog/data-oriented mã đánh dấu.

---

## 40. `<sub>` và `<sup>`

```html
H<sub>2</sub>O
```

```html
x<sup>2</sup>
```

Dùng cho subscript/superscript ngữ nghĩa, không chỉ visual positioning.

---

## 41. `<bdi>` và `<bdo>`

`bdi` isolate bidirectional user-generated text:

```html
User: <bdi>اسم</bdi>
```

Nó hữu ích khi UI left-to-right chứa username right-to-left.

`bdo` force direction:

```html
<bdo dir="rtl">ABC</bdo>
```

`bdo` hiếm hơn và nên dùng có chủ đích.

---

## 42. Ruby annotations

East Asian pronunciation annotations:

```html
<ruby>
  漢
  <rt>かん</rt>
</ruby>
```

`rt` chứa annotation/pronunciation. `rp` hỗ trợ phương án dự phòng presentation cho old environments.

---

# PHẦN 6 — LISTS

## 43. `<ul>`, `<ol>`, `<li>`

Unordered list:

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

Ordered list:

```html
<ol>
  <li>Install</li>
  <li>Configure</li>
  <li>Run</li>
</ol>
```

Dùng `ol` khi order mang meaning, `ul` khi order không quan trọng.

Đừng tạo list visual bằng nhiều `div` nếu content thật sự là list.

---

## 44. Description list

```html
<dl>
  <dt>HTML</dt>
  <dd>Defines structure and semantics.</dd>

  <dt>CSS</dt>
  <dd>Defines presentation.</dd>
</dl>
```

`dl` rất phù hợp với glossary, siêu dữ liệu hoặc term-description pairs.

---

# PHẦN 7 — LINKS VÀ NAVIGATION

## 45. `<a>`

Anchor tạo hyperlink:

```html
<a href="/profile">
  Profile
</a>
```

`href` có thể là:

```text
relative URL
absolute URL
fragment
mailto:
tel:
```

Ví dụ:

```html
<a href="#pricing">Pricing</a>
<a href="mailto:support@example.com">Email</a>
<a href="tel:+821012345678">Call</a>
```

---

## 46. Link và button khác nhau ở bản chất

Nếu tương tác thay đổi URL/location hoặc navigate tới resource khác, dùng link:

```html
<a href="/profile">Profile</a>
```

Nếu tương tác thực hiện action trong current application state, dùng button:

```html
<button type="button">
  Open profile panel
</button>
```

Đây là một trong những rules quan trọng nhất của HTML ngữ nghĩa.

Không dùng `<a href="#">` để fake button nếu không có navigation ngữ nghĩa.

---

## 47. `target="_blank"`

```html
<a
  href="https://example.com"
  target="_blank">
  External site
</a>
```

Mở browsing context mới.

Khi dùng external links, `rel` có thể cần tùy bảo mật/privacy/relationship requirements.

Modern browsers có các hành vi bảo vệ opener tốt hơn trước, nhưng hiểu `noopener`/`noreferrer` vẫn quan trọng khi review hệ thống cũ hoặc explicit policies.

---

## 48. `rel`

`rel` mô tả relationship:

```html
<a
  href="..."
  rel="nofollow sponsored">
```

Common concepts:

```text
noopener
noreferrer
nofollow
ugc
sponsored
author
license
```

SEO relation tokens không phải bảo mật controls.

---

## 49. `download`

```html
<a
  href="/report.pdf"
  download>
  Download report
</a>
```

Nó là trình duyệt hint cho download hành vi trong applicable cases.

Đừng dùng nó như access-control/bảo mật mechanism.

---

# PHẦN 8 — IMAGES VÀ RESPONSIVE IMAGES

## 50. `<img>`

```html
<img
  src="/team.jpg"
  alt="Engineering team discussing a system diagram">
```

`src` chỉ resource.

`alt` cung cấp text alternative khi image không thể/không nên được consumed visually.

---

## 51. Viết `alt` đúng

Informative image:

```html
<img
  src="/growth-chart.png"
  alt="Revenue increased from 20 to 35 million dollars between Q1 and Q4">
```

Decorative image:

```html
<img
  src="/separator.svg"
  alt="">
```

`alt=""` không có nghĩa “quên alt”; nó cố ý nói image decorative và không cần trình đọc màn hình announce.

Alt tốt mô tả **purpose trong context**, không phải liệt kê mọi pixel.

---

## 52. `width` và `height`

```html
<img
  src="/hero.jpg"
  width="1200"
  height="800"
  alt="...">
```

Attributes này giúp trình duyệt biết intrinsic aspect ratio và reserve bố cục space trước khi image load.

Điều đó giúp giảm dịch chuyển bố cục (bố cục shift).

Bạn vẫn có thể resize responsive bằng CSS:

```css
img {
  max-width: 100%;
  height: auto;
}
```

---

## 53. `loading`

```html
<img
  loading="lazy"
  src="/below-fold.jpg"
  alt="...">
```

Lazy quá trình tải phù hợp với images ngoài viewport.

Không nên lazy-load hero/LCP image một cách máy móc vì trình duyệt có thể discover/fetch nó muộn hơn.

---

## 54. `srcset`

```html
<img
  src="/photo-800.jpg"
  srcset="
    /photo-400.jpg 400w,
    /photo-800.jpg 800w,
    /photo-1200.jpg 1200w"
  alt="...">
```

Bạn cung cấp image candidates; trình duyệt chọn candidate dựa trên viewport, device pixel ratio và expected render width.

---

## 55. `sizes`

```html
<img
  srcset="
    /photo-400.jpg 400w,
    /photo-800.jpg 800w,
    /photo-1200.jpg 1200w"
  sizes="
    (max-width: 600px) 100vw,
    800px"
  src="/photo-800.jpg"
  alt="...">
```

`sizes` nói trình duyệt image dự kiến render rộng bao nhiêu trong các viewport conditions.

Nếu `sizes` sai, trình duyệt có thể chọn resource quá lớn hoặc quá nhỏ.

---

## 56. `<picture>`

`picture` dùng khi source selection cần art direction hoặc format alternatives:

```html
<picture>
  <source
    srcset="/hero.avif"
    type="image/avif">

  <source
    srcset="/hero.webp"
    type="image/webp">

  <img
    src="/hero.jpg"
    width="1200"
    height="800"
    alt="Engineering team">
</picture>
```

`srcset` trên img thường giải quyết resolution/size selection. `picture` giải quyết source choice theo media/type/art direction.

---

## 57. `<figure>` và `<figcaption>`

```html
<figure>
  <img
    src="/architecture.png"
    alt="Three-layer system architecture">

  <figcaption>
    Figure 1. Application architecture
  </figcaption>
</figure>
```

Figure phù hợp với image, diagram, chart, code sample hoặc content có caption riêng.

---

# PHẦN 9 — AUDIO, VIDEO VÀ EMBEDDED CONTENT

## 58. `<audio>`

```html
<audio
  controls
  src="/lesson.mp3">
</audio>
```

Attributes phổ biến:

```text
controls
autoplay
loop
muted
preload
```

Autoplay có nhiều trình duyệt restrictions, đặc biệt nếu có audio.

`preload` là hint, không phải absolute command.

---

## 59. `<video>`

```html
<video
  controls
  width="800"
  poster="/poster.jpg"
  playsinline>

  <source
    src="/movie.mp4"
    type="video/mp4">

</video>
```

`poster` là preview image trước playback.

`playsinline` giúp playback inline trong supporting mobile environments.

---

## 60. `<source>`

Media có thể cung cấp nhiều sources:

```html
<video controls>
  <source
    src="/movie.webm"
    type="video/webm">

  <source
    src="/movie.mp4"
    type="video/mp4">
</video>
```

Trình duyệt dùng capability/type hints để chọn phù hợp.

---

## 61. `<track>`

```html
<track
  kind="captions"
  src="/captions-en.vtt"
  srclang="en"
  label="English">
```

`captions` thường chứa cả speech và relevant sound descriptions cho khả năng tiếp cận. `subtitles` chủ yếu dịch/transcribe dialogue cho người vẫn nghe được audio.

---

## 62. `<iframe>`

```html
<iframe
  src="https://example.com"
  title="Payment page">
</iframe>
```

Iframe embed một browsing context khác.

`title` giúp công nghệ hỗ trợ biết iframe dùng để làm gì.

---

## 63. `sandbox`

```html
<iframe
  src="https://third-party.example"
  sandbox>
</iframe>
```

Empty sandbox áp nhiều restrictions.

Bạn mở capability từng phần:

```html
sandbox="allow-scripts allow-forms"
```

Senior bảo mật principle là **least privilege**: chỉ allow capability thực sự cần.

---

## 64. `allow`

```html
<iframe
  src="..."
  allow="camera; microphone">
</iframe>
```

Permissions Policy cho iframe capabilities.

Đừng cấp camera/microphone/location-like capabilities nếu embedded app không cần.

---

## 65. `srcdoc`

```html
<iframe
  srcdoc="<h1>Hello</h1>">
</iframe>
```

`srcdoc` chứa HTML document inline.

Nếu content đến từ user/untrusted source, đây là HTML execution context và có XSS implications. Nó không phải plain text container.

---

# PHẦN 10 — TABLES

## 66. `<table>`

Table dùng cho tabular data, không dùng làm page bố cục.

```html
<table>
  ...
</table>
```

Modern bố cục dùng CSS Grid/Flexbox.

---

## 67. `<caption>`

```html
<table>
  <caption>Monthly Revenue</caption>
  ...
</table>
```

Caption mô tả mục đích/nội dung table và rất hữu ích cho khả năng tiếp cận.

---

## 68. Table structure

```html
<table>
  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Price</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <th scope="row">Keyboard</th>
      <td>$100</td>
    </tr>
  </tbody>
</table>
```

`tr` là row, `th` là header cell, `td` là data cell.

`thead`, `tbody`, `tfoot` tạo logical groups.

Trình duyệt bộ phân tích cú pháp có table-specific rules; source và resulting DOM có thể khác nếu mã đánh dấu thiếu/invalid. Phần Master sẽ giải thích.

---

## 69. `scope`

```html
<th scope="col">Price</th>
```

hoặc:

```html
<th scope="row">Keyboard</th>
```

Scope giúp associate header với cells trong table đơn giản.

Complex table có thể cần `headers`/`id` strategies, nhưng đừng làm table phức tạp hơn business requirement.

---

## 70. `rowspan` và `colspan`

```html
<td colspan="2">Total</td>
```

```html
<th rowspan="2">Region</th>
```

Dùng cho merged cells.

Merged table structures cần test khả năng tiếp cận cẩn thận vì association trở nên phức tạp.

---

# PHẦN 11 — FORMS: PHẦN QUAN TRỌNG NHẤT CỦA HTML APPLICATION

## 71. `<form>`

```html
<form
  action="/login"
  method="post">
  ...
</form>
```

Form không chỉ là visual wrapper. Nó là một mechanism browser-native để collect các điều khiển được đưa vào dữ liệu gửi đi và submit data tới URL.

Đây là lý do hiểu native form ngữ nghĩa cực kỳ quan trọng dù bạn dùng React.

---

## 72. `action`

```html
<form action="/users">
```

`action` là URL target khi form submit.

Nếu application intercept submit bằng JavaScript, native action vẫn có thể là tăng cường dần (tăng cường dần (progressive enhancement)) phương án dự phòng tùy architecture.

---

## 73. `method`

Common:

```html
method="get"
```

và:

```html
method="post"
```

GET phù hợp với safe query/search/filter navigation, nơi data có thể nằm trong URL.

POST phù hợp với state-changing submission hoặc payload không nên encoded như query.

HTML method ngữ nghĩa không thay HTTP authorization/bảo mật rules.

---

## 74. `enctype`

Default form encoding thường là:

```text
application/x-www-form-urlencoded
```

File upload cần:

```html
<form
  method="post"
  enctype="multipart/form-data">
```

Nếu quên multipart, file data sẽ không được submit đúng như bạn mong đợi.

---

## 75. `<label>`

```html
<label for="email">
  Email
</label>

<input
  id="email"
  name="email"
  type="email">
```

`for` match `id`.

Label không chỉ là text cạnh input. Nó tạo association khả năng tiếp cận và click/tap hành vi.

Bạn cũng có thể wrap control:

```html
<label>
  Email
  <input
    name="email"
    type="email">
</label>
```

---

## 76. Placeholder không phải label

Sai:

```html
<input
  type="email"
  placeholder="Email">
```

nếu không có label.

Placeholder biến mất khi user nhập và thường có contrast/khả năng tiếp cận issues.

Tốt hơn:

```html
<label for="email">Email</label>

<input
  id="email"
  name="email"
  type="email"
  placeholder="name@example.com">
```

Placeholder nên là hint/example, không phải field name chính.

---

## 77. `<input>`

Input là form control đa năng:

```html
<input
  type="text"
  name="username">
```

Ba attributes phải hiểu sâu là:

```text
type
name
value
```

`type` chọn hành vi/ngữ nghĩa.

`name` là key trong form submission.

`value` liên quan current/default/submitted value tùy input type/state.

---

# PHẦN 12 — INPUT TYPES

## 78. `text`

```html
<input
  type="text"
  name="displayName">
```

General single-line text.

---

## 79. `password`

```html
<input
  type="password"
  name="password"
  autocomplete="current-password">
```

Nó che visual characters. Nó không encrypt network payload.

Security vẫn phụ thuộc HTTPS, server storage và authentication architecture.

---

## 80. `email`

```html
<input
  type="email"
  name="email"
  autocomplete="email"
  required>
```

Trình duyệt cung cấp email-specific kiểm tra tính hợp lệ (validation) ngữ nghĩa và mobile keyboard hints.

Server vẫn phải validate email/business rules.

---

## 81. `number`

```html
<input
  type="number"
  name="quantity"
  min="1"
  max="100"
  step="1">
```

Dùng cho quantity thực sự có numerical meaning.

Không dùng cho phone number, credit card, postal code hoặc ID vì chúng không phải quantities; leading zero và formatting có thể quan trọng.

---

## 82. `search`, `tel`, `url`

Search:

```html
<input type="search">
```

Telephone:

```html
<input type="tel">
```

URL:

```html
<input type="url">
```

`tel` không validate universal phone format vì formats quá đa dạng.

`url` có URL constraint ngữ nghĩa.

---

## 83. `checkbox`

```html
<input
  type="checkbox"
  name="agree"
  value="yes">
```

Nếu checked, form có thể submit:

```text
agree=yes
```

Nếu unchecked, field thường không có entry trong submitted data.

Đây là hành vi quan trọng khi backend phân biệt false và missing.

---

## 84. `radio`

```html
<label>
  <input
    type="radio"
    name="plan"
    value="basic">
  Basic
</label>

<label>
  <input
    type="radio"
    name="plan"
    value="pro">
  Pro
</label>
```

Radio cùng `name` tạo group và thường chỉ một item được selected.

---

## 85. Date/time types

```html
<input type="date">
<input type="time">
<input type="datetime-local">
<input type="month">
<input type="week">
```

`datetime-local` không tự mang timezone.

Nếu backend cần global instant, timezone phải được xác định ở tầng khác.

UI display cũng phụ thuộc locale/trình duyệt.

---

## 86. `range`

```html
<input
  type="range"
  min="0"
  max="100"
  value="50">
```

Slider tốt cho approximate range input.

Nếu exact value quan trọng, nên hiển thị value hiện tại bên cạnh.

---

## 87. `color`

```html
<input
  type="color"
  name="themeColor">
```

Native color picker trong supporting browsers.

---

## 88. `file`

```html
<input
  type="file"
  name="avatar"
  accept="image/*">
```

Multiple:

```html
<input
  type="file"
  name="attachments"
  multiple>
```

`accept` chỉ là file-picker hint. Server vẫn phải validate type, size, file signature/content và malware policy.

---

## 89. `hidden`

```html
<input
  type="hidden"
  name="csrf"
  value="...">
```

Hidden fields vẫn thuộc client DOM/request.

Không bao giờ coi hidden value là secret/trusted authorization data. User có thể sửa request bằng DevTools hoặc HTTP client.

---

# PHẦN 13 — INPUT ATTRIBUTES VÀ FORM VALIDATION

## 90. `name`

```html
<input
  name="email"
  value="a@example.com">
```

`name` tạo key cho form data.

Nếu control không có `name`, nó thường không đóng góp entry vào form submission.

---

## 91. `value`

Markup:

```html
<input value="Alice">
```

Đây là initial/default value relationship.

Sau user edit, thuộc tính DOM:

```js
input.value
```

có thể là `"Bob"` trong khi:

```js
input.getAttribute("value")
```

vẫn phản ánh mã đánh dấu attribute `"Alice"`.

Đây là bước đầu để hiểu difference giữa **thuộc tính nội dung** và **IDL/thuộc tính DOM**.

---

## 92. `required`

```html
<input
  type="email"
  required>
```

Trình duyệt native kiểm tra ràng buộc (constraint kiểm tra tính hợp lệ (validation)) có thể block submission nếu value missing/invalid.

Client kiểm tra tính hợp lệ (validation) giúp UX, không phải bảo mật boundary. Server bắt buộc validate lại.

---

## 93. `disabled`

```html
<input disabled>
```

Disabled control thường:

```text
không focus
không edit
không submit
```

Đây là thuộc tính boolean.

Sai:

```html
<input disabled="false">
```

Nó vẫn disabled vì thuộc tính boolean true khi attribute tồn tại.

Muốn false, remove attribute hoặc set thuộc tính DOM false.

---

## 94. `readonly`

```html
<input
  name="accountId"
  value="A123"
  readonly>
```

Readonly control không cho user sửa nhưng thường vẫn focusable/submittable tùy control type.

Khác disabled, disabled control thường bị loại khỏi form submission.

Đây là khác biệt backend quan trọng.

---

## 95. `checked` và `selected`

Initial checkbox/radio state:

```html
<input
  type="checkbox"
  checked>
```

Option initial state:

```html
<option selected>Korea</option>
```

Sau user tương tác, các thuộc tính DOM:

```js
input.checked
option.selected
```

phản ánh trạng thái hiện tại, còn mã đánh dấu attributes liên quan default/initial state.

---

## 96. `min`, `max`, `step`

```html
<input
  type="number"
  min="1"
  max="100"
  step="0.01">
```

Constraints này áp dụng phù hợp theo input type.

`step` mô tả allowed stepping/granularity.

---

## 97. `minlength`, `maxlength`

```html
<input
  minlength="8"
  maxlength="30">
```

Client constraint/hint.

Không thay server kiểm tra tính hợp lệ (validation).

---

## 98. `pattern`

```html
<input
  pattern="[A-Z]{3}">
```

Pattern constraint có thể hỗ trợ simple format kiểm tra tính hợp lệ (validation).

Không biến HTML regex thành bảo mật filter. Server phải validate domain value bằng rule của mình.

---

## 99. `multiple`

Có thể dùng với file, email hoặc select:

```html
<input
  type="file"
  multiple>
```

```html
<select
  name="skills"
  multiple>
```

Form data có thể có nhiều entries cùng name.

---

## 100. `autocomplete`

Ví dụ:

```html
<input
  name="email"
  autocomplete="email">
```

Các tokens quan trọng:

```text
name
given-name
family-name
username
new-password
current-password
one-time-code
email
tel
street-address
postal-code
organization
cc-name
cc-number
cc-exp
cc-csc
```

Autocomplete đúng giúp password manager, mobile keyboard và checkout UX.

Không tắt autofill bừa chỉ vì “UI nhìn sạch hơn”.

---

## 101. `inputmode`

```html
<input
  type="text"
  inputmode="numeric">
```

`inputmode` chủ yếu gợi ý keyboard/input UI.

`type` ảnh hưởng ngữ nghĩa/kiểm tra tính hợp lệ (validation).

Ví dụ postal code numeric-looking nhưng không phải number quantity; có thể dùng:

```html
<input
  type="text"
  inputmode="numeric">
```

---

## 102. `enterkeyhint`

```html
<input
  enterkeyhint="search">
```

Gợi ý label/action của Enter key trên mobile keyboard.

Common values gồm:

```text
enter
done
go
next
previous
search
send
```

---

## 103. `<datalist>`

```html
<label for="city">City</label>

<input
  id="city"
  name="city"
  list="cities">

<datalist id="cities">
  <option value="Seoul">
  <option value="Busan">
</datalist>
```

Datalist cung cấp suggestions, không phải strict selection như `select`.

User vẫn có thể nhập value khác nếu constraints không cấm.

---

# PHẦN 14 — TEXTAREA, SELECT, FIELDSET VÀ BUTTON

## 104. `<textarea>`

```html
<textarea
  name="description"
  rows="5"></textarea>
```

Initial value nằm giữa start/end tags:

```html
<textarea>Hello</textarea>
```

không phải `value` attribute như input.

---

## 105. `<select>` và `<option>`

```html
<select name="country">
  <option value="KR">Korea</option>
  <option value="VN">Vietnam</option>
</select>
```

Visible label có thể khác submitted `value`.

Native select cung cấp keyboard/mobile/khả năng tiếp cận các hành vi mà custom `div` dropdown phải tự implement rất nhiều.

---

## 106. `<optgroup>`

```html
<select name="country">
  <optgroup label="Asia">
    <option value="KR">Korea</option>
    <option value="VN">Vietnam</option>
  </optgroup>
</select>
```

Dùng để group options theo category.

---

## 107. `<fieldset>` và `<legend>`

```html
<fieldset>
  <legend>Payment method</legend>

  <label>
    <input
      type="radio"
      name="payment"
      value="card">
    Card
  </label>
</fieldset>
```

`fieldset` group related controls.

`legend` cung cấp accessible group label.

Đặc biệt hữu ích với radio groups và related checkbox sections.

---

## 108. `<button>`

```html
<button type="button">
  Open
</button>
```

Các types:

```text
button
submit
reset
```

Trong form, nếu button không phải submit, hãy khai báo:

```html
type="button"
```

rõ ràng để tránh accidental submission.

---

## 109. Multi-action form

HTML native có thể làm:

```html
<form
  action="/article"
  method="post">

  <button
    type="submit"
    name="action"
    value="save">
    Save
  </button>

  <button
    type="submit"
    name="action"
    value="publish">
    Publish
  </button>

</form>
```

Backend nhận value của điều khiển gửi biểu mẫu được click.

Button còn có thể override `formaction`, `formmethod`, `formenctype`, `formtarget` và `formnovalidate`.

Phần Master sẽ giải thích sâu điều khiển gửi biểu mẫu/biểu mẫu chủ quản ngữ nghĩa.

---

# PHẦN 15 — NATIVE OUTPUT VÀ INTERACTIVE ELEMENTS

## 110. `<output>`

```html
<output for="price quantity">
  100
</output>
```

Biểu diễn result của calculation/user action.

---

## 111. `<progress>`

```html
<progress
  value="70"
  max="100">
  70%
</progress>
```

Dùng cho task progress.

---

## 112. `<meter>`

```html
<meter
  min="0"
  max="100"
  value="80">
  80
</meter>
```

Dùng cho measurement trong known range.

`progress` là tiến độ task; `meter` là một measurement/value.

---

## 113. `<details>` và `<summary>`

```html
<details>
  <summary>Advanced settings</summary>

  <p>...</p>
</details>
```

Đây là native disclosure widget.

Trước khi tự viết accordion bằng `div + onclick + aria-expanded`, hãy xem `details/summary` có đáp ứng requirement không.

---

## 114. `<dialog>`

```html
<dialog id="confirm">
  <h2>Delete item?</h2>

  <button type="button">
    Cancel
  </button>

  <button type="button">
    Delete
  </button>
</dialog>
```

JavaScript có:

```js
dialog.show()
```

cho non-modal và:

```js
dialog.showModal()
```

cho modal.

Native dialog có top-layer/modal/tiêu điểm ngữ nghĩa tốt hơn một `div.modal` tự chế, dù môi trường thực tế vẫn phải test tiêu điểm flow và khả năng tiếp cận.

---

## 115. `<form method="dialog">`

Trong dialog:

```html
<dialog id="confirm">
  <form method="dialog">
    <button value="cancel">
      Cancel
    </button>

    <button value="ok">
      OK
    </button>
  </form>
</dialog>
```

Submit form có thể đóng dialog thay vì gửi HTTP request.

Đây là ví dụ tốt về HTML native hành vi thay thế JavaScript boilerplate.

---

## 116. Popover

Một element có thể trở thành popover:

```html
<div
  id="menu"
  popover>
  ...
</div>
```

Invoker:

```html
<button
  type="button"
  popovertarget="menu">
  Open menu
</button>
```

Trình duyệt quản lý show/hide, lớp trên cùng và light-dismiss hành vi theo popover mode.

Feature này sẽ được giải thích sâu ở Master Implementation.

---

# PHẦN 16 — GLOBAL ATTRIBUTES

## 117. `id`

```html
<section id="pricing">
```

`id` phải unique trong document.

Nó được dùng cho fragment navigation, label association, ARIA relationships, CSS và JS.

Duplicate IDs có thể gây khả năng tiếp cận/query bugs khó debug.

---

## 118. `class`

```html
<div class="card active">
```

Class là space-separated tokens thường dùng cho CSS và component state styling.

JavaScript thường thao tác qua:

```js
element.classList
```

---

## 119. `style`

```html
<div style="display:none">
```

Inline style hợp lệ, nhưng large application thường tránh sử dụng rộng vì maintainability, reuse và CSP architecture.

---

## 120. `title`

```html
<abbr title="HyperText Markup Language">
  HTML
</abbr>
```

`title` là advisory information.

Không dùng nó làm tên trợ năng duy nhất cho critical control.

---

## 121. `hidden`

```html
<section hidden>
```

Đánh dấu content hiện tại không relevant/không được present.

JavaScript:

```js
element.hidden = true;
```

Phần Master sẽ phân biệt `hidden`, `hidden="until-found"`, CSS hiding và khả năng tiếp cận implications.

---

## 122. `inert`

```html
<main inert>
  ...
</main>
```

`inert` làm subtree non-interactive trong nhiều user tương tác paths, bao gồm tiêu điểm.

Useful với custom overlay workflows, nhưng native modal dialog đã có browser-managed inertness hành vi cho surrounding content.

---

## 123. `tabindex`

```html
tabindex="0"
```

đưa element vào tab order theo document position.

```html
tabindex="-1"
```

cho phép programmatic tiêu điểm nhưng không natural tab.

Positive tabindex như:

```html
tabindex="5"
```

thường là anti-pattern vì phá natural tiêu điểm order và rất khó maintain.

---

## 124. `data-*`

```html
<button
  data-user-id="42">
```

JavaScript:

```js
button.dataset.userId
```

Phù hợp với lightweight application siêu dữ liệu.

Không chứa secret/token vì DOM thuộc client.

---

## 125. `contenteditable`

```html
<div contenteditable="true">
  Editable text
</div>
```

Nó biến content thành editable region, nhưng không tự trở thành rich-text editor môi trường thực tế.

Selection, paste sanitization, undo, trình duyệt differences và khả năng tiếp cận làm editor implementation phức tạp hơn nhiều.

---

## 126. `draggable`

```html
<div draggable="true">
```

Cho native drag hành vi.

Nếu drag action là critical, hãy cung cấp alternative không phụ thuộc pointer drag cho khả năng tiếp cận.

---

## 127. `spellcheck`, `translate`, `autofocus`

Spell checking hint:

```html
<textarea spellcheck="true">
```

Không dịch:

```html
<code translate="no">
  npm install
</code>
```

Autofocus:

```html
<input autofocus>
```

Autofocus phải dùng cẩn thận vì có thể bật mobile keyboard hoặc làm trình đọc màn hình context nhảy bất ngờ.

---

# PHẦN 17 — SCRIPT LOADING

## 128. `<script>`

Classic external script:

```html
<script src="/app.js"></script>
```

Script quá trình tải strategy ảnh hưởng bộ phân tích cú pháp và hiệu năng.

---

## 129. `defer`

```html
<script
  defer
  src="/app.js">
</script>
```

Classic deferred script được download song song và execute sau document phân tích cú pháp, đồng thời giữ relative execution order giữa deferred scripts.

Đây là good default cho nhiều classic application scripts.

---

## 130. `async`

```html
<script
  async
  src="/analytics.js">
</script>
```

Async script download song song và execute khi ready; execution order với scripts khác không đảm bảo.

Phù hợp với independent scripts như analytics.

---

## 131. `type="module"`

```html
<script
  type="module"
  src="/main.js">
</script>
```

ES Module hỗ trợ `import`/`export` và module graph.

Module scripts có quá trình tải/execution hành vi riêng, gần deferred by default trong nhiều respects.

Modern frontend cần hiểu module quá trình tải thay vì chỉ học `async/defer`.

---

## 132. `nomodule`

```html
<script
  nomodule
  src="/legacy.js">
</script>
```

Legacy phương án dự phòng pattern cho browsers không support modules.

Ngày nay nhiều projects không cần nữa, nhưng senior nên nhận diện khi maintain old bundles.

---

## 133. `integrity`

```html
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-..."
  crossorigin="anonymous">
</script>
```

Subresource Integrity cho trình duyệt verify fetched resource khớp expected hash.

Hữu ích với pinned third-party CDN resources.

---

## 134. `nonce`

```html
<script nonce="RANDOM_PER_RESPONSE">
```

Nonce có thể được Content Security Policy dùng để allow specific inline script.

Nonce phải unpredictable và phù hợp policy. Hardcode same nonce mãi làm mất bảo mật intent.

---

## 135. `<noscript>`

```html
<noscript>
  JavaScript is required for this application.
</noscript>
```

Nếu base tính năng có thể hoạt động native/server-side, tăng cường dần (tăng cường dần (progressive enhancement)) thường tốt hơn chỉ hiển thị warning.

---

# PHẦN 18 — SEO, SOCIAL METADATA VÀ STRUCTURED DATA

## 136. SEO bắt đầu từ nội dung và ngữ nghĩa

HTML SEO không chỉ là meta tags.

Các foundations gồm:

```text
title
description
semantic headings
meaningful links
crawlable content
lang
alt
canonical URL
structured data khi phù hợp
```

Search engine phải hiểu content thật.

---

## 137. Canonical

```html
<link
  rel="canonical"
  href="https://example.com/product/123">
```

Dùng để chỉ preferred URL khi nhiều URLs đại diện cùng/similar content.

Nó không phải redirect và không phải bảo mật rule.

---

## 138. Robots siêu dữ liệu

```html
<meta
  name="robots"
  content="noindex,nofollow">
```

`noindex` là search indexing instruction/hint trong applicable crawler context.

Nó không bảo vệ private admin page. Private page phải có authentication/authorization.

---

## 139. Open Graph

```html
<meta
  property="og:title"
  content="HTML Guide">

<meta
  property="og:description"
  content="Learn semantic HTML">

<meta
  property="og:image"
  content="https://example.com/preview.png">
```

Dùng để tạo social sharing previews trong supporting platforms.

---

## 140. JSON-LD structured data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acme"
}
</script>
```

Structured data giúp machine/search engines hiểu entity/content theo vocabulary.

Nó phải phản ánh content thật, không phải nơi khai báo thông tin giả để “hack SEO”.

---

# PHẦN 19 — ACCESSIBILITY

## 141. Native HTML trước ARIA

Sai nếu không có lý do:

```html
<div
  role="button"
  tabindex="0">
  Save
</div>
```

Đúng hơn:

```html
<button type="button">
  Save
</button>
```

Native button đã có keyboard/tiêu điểm/role/form ngữ nghĩa.

ARIA không tạo native hành vi. Nếu dùng `role="button"` trên div, bạn còn phải implement keyboard activation và tiêu điểm hành vi.

---

## 142. Accessible name

Một control cần tên mà cây trợ năng hiểu.

Text button:

```html
<button>Save</button>
```

đã có tên trợ năng.

Icon-only:

```html
<button
  type="button"
  aria-label="Close">
  ×
</button>
```

Nếu visible text tồn tại, ưu tiên để tên trợ năng phù hợp visible text.

---

## 143. `aria-labelledby`

```html
<h2 id="dialog-title">
  Delete account
</h2>

<div
  role="dialog"
  aria-labelledby="dialog-title">
  ...
</div>
```

Accessible name lấy từ element khác.

---

## 144. `aria-describedby`

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

Label/name trả lời “control này là gì?”. Description bổ sung “cần biết gì thêm?”.

---

## 145. Dynamic ARIA state

Expandable button:

```html
<button
  aria-expanded="false"
  aria-controls="menu">
  Menu
</button>
```

Khi menu mở, `aria-expanded` phải update thành `true`.

ARIA state không tự sync với visual state nếu JavaScript không cập nhật.

---

## 146. `aria-current`

```html
<a
  href="/orders"
  aria-current="page">
  Orders
</a>
```

Cho công nghệ hỗ trợ biết item hiện tại.

---

## 147. Live regions

```html
<div
  aria-live="polite">
  Saved successfully
</div>
```

Dùng cho dynamic updates cần announce.

Không dùng `assertive` cho mọi notification vì có thể interrupt user liên tục.

---

## 148. Keyboard test

Một senior review phải thử page chỉ bằng keyboard:

```text
Tab
Shift+Tab
Enter
Space
Escape
arrow keys ở controls phù hợp
```

Kiểm tra tiêu điểm order, visible tiêu điểm và khả năng activate controls.

HTML ngữ nghĩa tốt thường giảm rất nhiều custom keyboard code.

---

# PHẦN 20 — ATTRIBUTE VS DOM PROPERTY

## 149. Hai tầng khác nhau

Markup:

```html
<input
  value="A"
  checked>
```

Trình duyệt parse thành DOM object có properties:

```js
input.value
input.checked
```

Content attribute và thuộc tính DOM có thể reflect lẫn nhau nhưng không phải lúc nào cũng cùng trạng thái hiện tại.

---

## 150. `value`

Markup:

```html
<input value="A">
```

User sửa thành `B`.

```js
input.value
```

→ `"B"`

Nhưng:

```js
input.getAttribute("value")
```

có thể vẫn → `"A"`.

Attribute thể hiện mã đánh dấu/default value relationship; property thể hiện current trạng thái hiện thời.

---

## 151. `checked`

```html
<input
  type="checkbox"
  checked>
```

User uncheck.

```js
input.checked
```

→ false.

`checked` thuộc tính nội dung vẫn có thể tồn tại và liên quan default checked state.

---

## 152. `href`

```html
<a href="/users">
```

```js
a.getAttribute("href")
```

có thể trả `/users`.

```js
a.href
```

thường trả fully resolved absolute URL.

Đây là ví dụ reflection/resolution hành vi rất phổ biến.

---

## 153. Boolean attributes

Boolean attribute true theo presence:

```html
<input disabled>
```

```html
<input disabled="">
```

```html
<input disabled="false">
```

cả ba đều disabled.

False nghĩa remove attribute hoặc set property false:

```js
input.disabled = false;
```

Common boolean attrs gồm `disabled`, `checked`, `selected`, `required`, `readonly`, `multiple`, `autofocus`, `hidden`, `open`, `controls`, `loop`, `muted`.

---

# PHẦN 21 — CONTENT MODEL VÀ VALID HTML

## 154. Không phải element nào cũng chứa gì cũng được

HTML có các mô hình nội dung.

Ví dụ `ul` có list items phù hợp.

Interactive element không nên nest interactive element một cách invalid/problematic.

Sai:

```html
<button>
  <a href="/profile">
    Profile
  </a>
</button>
```

Nếu navigation, dùng link. Nếu action, dùng button.

---

## 155. Void elements

Các HTML các phần tử rỗng đặc biệt quan trọng:

```text
area
base
br
col
embed
hr
img
input
link
meta
source
track
wbr
```

Chúng không có end tag/children trong HTML syntax.

```html
<img
  src="/a.png"
  alt="">
```

Không viết:

```html
<img>text</img>
```

HTML các phần tử rỗng đặc biệt khác XML self-closing model.

---

# PHẦN 22 — BROWSER PARSER CƠ BẢN

## 156. bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) không giống XML bộ phân tích cú pháp

bộ phân tích cú pháp HTML (HTML bộ phân tích cú pháp) được thiết kế với phục hồi lỗi (error recovery) mạnh.

Invalid mã đánh dấu có thể vẫn tạo DOM và render.

Điều đó không nghĩa mã đánh dấu đúng.

Trình duyệt có standardized algorithms để sửa/normalize nhiều cases.

---

## 157. Trình duyệt có thể thêm nodes

Source:

```html
<table>
  <tr>
    <td>A</td>
  </tr>
</table>
```

DOM inspector có thể thấy `tbody` được bộ phân tích cú pháp tạo.

Đây là ví dụ văn bản nguồn không phải luôn giống resulting DOM tree.

---

## 158. View Source vs Elements

**View Source** gần với original response/mã đánh dấu nguồn.

**Elements panel** cho current parsed DOM sau trình duyệt normalization và JavaScript mutations.

Nếu React/Vue hydrate DOM, bạn còn có framework internal tree/state.

Khi debug hydration mismatch, phải phân biệt ba tầng này.

---

# PHẦN 23 — SECURITY VÀ PERFORMANCE FOUNDATION

## 159. Client HTML không đáng tin

Hidden field, `data-*`, disabled control và client kiểm tra tính hợp lệ (validation) đều có thể bị user sửa/bypass.

Server phải validate và authorize independent of HTML.

---

## 160. Untrusted HTML

Concept nguy hiểm:

```js
element.innerHTML = userInput;
```

Nếu `userInput` không được sanitize/encode đúng context, XSS có thể xảy ra.

Security phải dựa trên contextual encoding/sanitization/CSP strategy, không phải regex remove `<script>`.

---

## 161. Iframe bảo mật

Use sandbox/allow/referrer policies có chủ đích.

Third-party iframe là bảo mật boundary, không phải chỉ bố cục box.

---

## 162. Resource quá trình tải ảnh hưởng hiệu năng

HTML quyết định trình duyệt discover CSS, JS, images, fonts, iframes sớm hay muộn.

Do đó hiệu năng không chỉ là JavaScript optimization.

Good mã đánh dấu có thể:

```text
discover LCP image sớm
reserve image dimensions
defer non-critical scripts
lazy-load below-fold images/iframes
preconnect đúng origin
```

---

## 163. `fetchpriority`

```html
<img
  src="/hero.jpg"
  fetchpriority="high"
  width="1200"
  height="800"
  alt="...">
```

Đây là priority hint cho trình duyệt.

Không đặt mọi thứ `high`; nếu mọi resource đều high thì signal mất giá trị và scheduling có thể xấu hơn.

---

## 164. Preconnect và preload

Preconnect:

```html
<link
  rel="preconnect"
  href="https://cdn.example.com">
```

Preload:

```html
<link
  rel="preload"
  href="/critical.woff2"
  as="font"
  crossorigin>
```

Preload sai `as`, wrong URL hoặc resource không thực sự critical có thể tạo duplicate/unnecessary fetch.

Performance hints phải được đo bằng DevTools/Lighthouse/RUM chứ không dùng theo cảm giác.

---

# PHẦN 24 — PROGRESSIVE ENHANCEMENT VÀ SENIOR MINDSET

## 165. Native-first design

Trước khi tự viết JavaScript widget, kiểm tra HTML đã có native primitive chưa:

```text
button
details/summary
dialog
popover
select
input date
form validation
progress
meter
```

Native controls thường có keyboard, tiêu điểm, khả năng tiếp cận và trình duyệt integration tốt hơn custom div.

---

## 166. Progressive enhancement

Search form:

```html
<form
  action="/search"
  method="get">

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
```

Nếu JavaScript không chạy, form vẫn submit được.

JavaScript có thể enhance suggestions, quá trình tải state và client kiểm tra tính hợp lệ (validation).

Đây là tăng cường dần (tăng cường dần (progressive enhancement)): base functionality tồn tại trước, JS cải thiện trải nghiệm.

---

## 167. Senior HTML review questions

Khi review mã đánh dấu, senior nên hỏi theo flow.

Element này có semantic đúng không? Nếu dùng `div`, có native element phù hợp hơn không? Heading hierarchy có đúng không? Links và buttons có bị dùng lẫn không? Form controls có label không? Form submission thực tế sẽ gửi những fields nào? Interactive controls có keyboard accessible không? Image alt có đúng purpose không? Resource quá trình tải có làm chậm LCP không? Iframe có sandbox quá rộng không? Client data có bị coi là trusted không? HTML có valid/parser-stable không?

Nếu bạn có thể trả lời những câu này, bạn đang review HTML ở level engineering chứ không chỉ syntax.

---

# PHẦN 25 — PRODUCTION PAGE HOÀN CHỈNH

```html
<!doctype html>

<html lang="vi">
<head>
  <meta charset="utf-8">

  <meta
    name="viewport"
    content="width=device-width, initial-scale=1">

  <title>
    HTML Learning Portal
  </title>

  <meta
    name="description"
    content="Learn semantic HTML from beginner to senior.">

  <link
    rel="canonical"
    href="https://example.com/html">

  <link
    rel="stylesheet"
    href="/app.css">
</head>

<body>

  <header>

    <nav aria-label="Main navigation">
      <a href="/">Home</a>
      <a href="/courses">Courses</a>
    </nav>

  </header>

  <main>

    <article>

      <header>
        <h1>HTML Beginner → Senior</h1>

        <p>
          Updated:
          <time datetime="2026-09-12">
            12 Sep 2026
          </time>
        </p>
      </header>

      <section>
        <h2>Overview</h2>

        <p>
          HTML defines document structure and semantics.
        </p>
      </section>

      <figure>

        <img
          src="/semantic-html.webp"
          width="1200"
          height="800"
          alt="Diagram showing header, navigation, main content and footer">

        <figcaption>
          Example semantic page structure
        </figcaption>

      </figure>

      <section>

        <h2>Create account</h2>

        <form
          action="/signup"
          method="post">

          <p>

            <label for="email">
              Email
            </label>

            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required>

          </p>

          <p>

            <label for="password">
              Password
            </label>

            <input
              id="password"
              name="password"
              type="password"
              autocomplete="new-password"
              minlength="12"
              aria-describedby="password-help"
              required>

            <span id="password-help">
              Use at least 12 characters.
            </span>

          </p>

          <button type="submit">
            Create account
          </button>

        </form>

      </section>

      <details>

        <summary>
          Advanced information
        </summary>

        <p>
          Native HTML can replace a surprising amount of custom JavaScript.
        </p>

      </details>

    </article>

  </main>

  <footer>
    <small>© 2026 Example</small>
  </footer>

  <script
    type="module"
    src="/app.js">
  </script>

</body>
</html>
```

Document này cố tình dùng ngữ nghĩa gốc của phần tử trước custom hành vi. Heading hierarchy rõ, navigation dùng links, form controls có labels, image có dimensions/alt, time machine-readable và JS dùng module quá trình tải.

---

# PHẦN 26 — ROADMAP HỌC

Ở giai đoạn Beginner, bạn cần nắm cấu trúc tài liệu, text, links, images, lists, tables và form basics. Bạn nên tự viết vài trang không framework để trình duyệt ngữ nghĩa trở thành phản xạ.

Ở Intermediate, tập trung semantic bố cục, ảnh đáp ứng, form kiểm tra tính hợp lệ (validation), `autocomplete`, các phần tử tương tác gốc của trình duyệt và khả năng tiếp cận fundamentals.

Ở Advanced, học attribute/property, quá trình tải script, các gợi ý tải tài nguyên (các gợi ý tải tài nguyên), SEO, iframe bảo mật, responsive hiệu năng và tăng cường dần (tăng cường dần (progressive enhancement)).

Ở Senior, mục tiêu là hiểu bộ phân tích cú pháp, form submission ngữ nghĩa, tiêu điểm/cây trợ năng, bảo mật trust boundaries và browser-native platform hành vi. Những phần sâu hơn như foster parenting, DOM clobbering, Declarative Shadow DOM, advanced Popover/Dialog và customizable select được tách sang file Master Implementation để file này vẫn có flow học rõ ràng.

---

# KẾT LUẬN

Một developer “biết HTML” có thể nhớ hàng chục tags. Một developer senior phải hiểu trình duyệt sẽ làm gì với mã đánh dấu đó.

Khi thấy:

```html
<button>
```

senior nghĩ tới action ngữ nghĩa, keyboard activation, tiêu điểm hành vi, form điều khiển gửi biểu mẫu hành vi và khả năng tiếp cận role.

Khi thấy:

```html
<img>
```

senior nghĩ tới alt purpose, intrinsic dimensions, responsive source selection, LCP và dịch chuyển bố cục (bố cục shift).

Khi thấy:

```html
<form>
```

senior nghĩ tới các điều khiển được đưa vào dữ liệu gửi đi, điều khiển gửi biểu mẫu, GET/POST, encoding, native kiểm tra tính hợp lệ (validation), autocomplete và server-side trust boundary.

Khi thấy:

```html
<script>
```

senior nghĩ tới bộ phân tích cú pháp blocking, module quá trình tải, CSP, integrity và critical kết xuất path.

Đó là cách chuyển từ “học tag HTML” sang **engineering HTML**.
