# HTML — Master hiện thực (implementation / 구현)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **HTML — Master hiện thực (implementation / 구현)**. Route đi từ browser parser và DOM → forms, accessibility tree và security → custom elements/Shadow DOM → modern declarative features và legacy migration → performance/debugging, để markup được hiểu như browser platform.

## Trình duyệt (browser / 브라우저) parsing, form internals, khả năng tiếp cận (accessibility / 접근성) API, bảo mật (security / 보안), legacy di chuyển (migration / 마이그레이션) và hiện đại (modern / 현대적) declarative HTML

Tài liệu này tiếp nối `html_01_beginner_to_senior_detailed.md`. tệp (file / 파일) đầu xây nền tảng từ document cấu trúc (structure / 구조), ngữ nghĩa (semantics / 의미론), forms, media, khả năng tiếp cận (accessibility / 접근성), SEO và hiệu năng (performance / 성능). tệp (file / 파일) Master này đi sâu vào phần khiến HTML trở thành một **nền tảng trình duyệt (browser platform / 브라우저 플랫폼)** chứ không chỉ là tập hợp tag: parser có thể sửa markup như thế nào, DOM live trạng thái (state / 상태) khác nguồn (source / 소스) ra sao, form đơn vị sở hữu (owner / 오너) và submitter hoạt động thế nào, cây khả năng tiếp cận (accessibility tree / 접근성 트리) nhận ngữ nghĩa (semantics / 의미론) từ đâu, custom elements kết nối với Shadow DOM ra sao, và vì sao những tính năng (feature / 기능) mới như Popover hoặc Declarative Shadow DOM có thể thay thế một phần JavaScript thủ công.

Mục tiêu không phải thuộc mọi môi trường vận hành (production / 운영 환경) trong HTML Living tiêu chuẩn (standard / 표준). Mục tiêu là khi gặp một bug hoặc một đoạn markup lạ, bạn biết trình duyệt (browser / 브라우저) sẽ xử lý ở tầng (layer / 계층) nào và biết câu hỏi cần đặt ra: nguồn (source / 소스) có valid không, parser có repair cây (tree / 트리) không, element có bản địa (native / 네이티브) ngữ nghĩa (semantics / 의미론) gì, DOM thuộc tính (property / 속성) hiện tại khác attribute ban đầu ra sao, điều khiển (control / 제어) có tham gia form submission không, assistive technology nhận accessible name nào, và tài nguyên (resource / 자원)/bảo mật (security / 보안) chính sách (policy / 정책) bị ảnh hưởng thế nào.

---

# PHẦN 1 — NHỮNG ELEMENT ÍT GẶP NHƯNG CẦN BIẾT

> **Chuyển mạch:** Browser parsing, form, accessibility và security là các constraint chung; `<search>` minh họa một element hiện đại trong các constraint đó, còn `<hgroup>` tiếp theo kiểm tra semantics heading.

## 1. `<search>`

`search` biểu diễn một vùng của document dành cho chức năng tìm kiếm hoặc lọc. Nó không thực hiện tìm kiếm (search / 검색) và cũng không thay thế `form`; ngữ nghĩa (semantic / 의미적) của nó chỉ giúp trình duyệt (browser / 브라우저) và khả năng tiếp cận (accessibility / 접근성) tầng (layer / 계층) biết subtree này có purpose là tìm kiếm (search / 검색).

```html
<search>
  <form action="/search" method="get">
    <label for="q">Search</label>
    <input id="q" name="q" type="search">
    <button type="submit">Search</button>
  </form>
</search>
```

Khi dùng, hãy nghĩ theo meaning thay vì visual bố cục (layout / 레이아웃). Một filter panel thực sự dùng để truy vấn (query / 쿼리) một sản phẩm (product / 제품) danh sách (list / 목록) có thể phù hợp với `search`; một toolbar chứa random buttons thì không.

---

> **Chuyển mạch:** `<search>` diễn đạt vùng tìm kiếm; `<hgroup>` tiếp theo nhóm heading có quan hệ, còn `<menu>` mở rộng semantic cho nhóm thao tác.

## 2. `<hgroup>`

`hgroup` group một heading với supporting văn bản (text / 텍스트) như subtitle hoặc tagline.

```html
<hgroup>
  <h1>HTML Platform</h1>
  <p>From semantic markup to browser behavior</p>
</hgroup>
```

Nó không phải shortcut để gộp `h1`, `h2`, `h3` thành một hierarchy. Heading hierarchy vẫn đến từ headings và document cấu trúc (structure / 구조). khả năng tiếp cận (accessibility / 접근성) implication ở đây là supporting văn bản (text / 텍스트) không trở thành một heading chỉ vì đứng gần heading về mặt visual.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **3. <menu>** tiếp nhận điểm tựa từ **2. <hgroup>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. <wbr>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. `<menu>`

`menu` hiện đại có thể biểu diễn một danh sách (list / 목록) các commands/actions.

```html
<menu>
  <li><button type="button">Copy</button></li>
  <li><button type="button">Paste</button></li>
</menu>
```

Trong ứng dụng (application / 애플리케이션) thông thường `ul` vẫn phổ biến hơn. Điều quan trọng là không nhầm element hiện tại với các context-menu APIs legacy từng tồn tại trong HTML cũ.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **4. <wbr>** tiếp nhận điểm tựa từ **3. <menu>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. <dfn> và <u>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. `<wbr>`

`wbr` tạo **word break opportunity**. trình duyệt (browser / 브라우저) chỉ xuống dòng tại đó khi bố cục (layout / 레이아웃) cần, khác với `br` là line break bắt buộc.

```html
<p>
  verylong<wbr>generated<wbr>identifier
</p>
```

Nó hữu ích với URL, băm (hash / 해시), identifier hoặc technical đơn vị từ (token / 토큰) dài. Về khả năng tiếp cận (accessibility / 접근성), `wbr` không nên được dùng để thay đổi meaning của văn bản (text / 텍스트); nó chỉ giúp bố cục (layout / 레이아웃) break line ở vị trí hợp lý.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **5. <dfn> và <u>** tiếp nhận điểm tựa từ **4. <wbr>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. <map> và <area>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Nếu mục tiêu chỉ là presentation, CSS phù hợp hơn. Underline còn có UX implication vì người dùng (user / 사용자) thường liên tưởng underline với link.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **6. <map> và <area>** tiếp nhận điểm tựa từ **5. <dfn> và <u>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. <canvas>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `<map>` và `<area>`

Ảnh (image / 이미지) map cho phép một ảnh (image / 이미지) có nhiều vùng clickable:

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

Trình duyệt (browser / 브라우저) dùng `shape` và `coords` để hit-test vùng trên ảnh (image / 이미지). tính năng (feature / 기능) này hiện khá niche vì responsive scaling và khả năng tiếp cận (accessibility / 접근성) phức tạp. Nếu dùng, `area` cần alternative văn bản (text / 텍스트) phù hợp và tương tác (interaction / 상호작용) phải vẫn hiểu được khi người dùng không nhìn ảnh (image / 이미지).

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **7. <canvas>** tiếp nhận điểm tựa từ **6. <map> và <area>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. SVG và MathML là foreign content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. `<canvas>`

`canvas` cung cấp bitmap drawing surface cho JavaScript:

```html
<canvas id="chart" width="800" height="400">
  Sales chart
</canvas>
```

`width` và `height` attributes định nghĩa drawing buffer, không chỉ kích thước CSS. Nếu buffer nhỏ nhưng CSS phóng lớn, đầu ra (output / 출력) dễ blur.

Canvas pixels không tự tạo ngữ nghĩa (semantic / 의미적) cây (tree / 트리). Một chart quan trọng nên có alternative biểu diễn (representation / 표현) như bảng (table / 테이블), văn bản (text / 텍스트) summary hoặc DOM controls. cấp cao (senior / 시니어) cần nhớ rằng canvas rendering và cây khả năng tiếp cận (accessibility tree / 접근성 트리) là hai hệ thống khác nhau.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **8. SVG và MathML là foreign content** tiếp nhận điểm tựa từ **7. <canvas>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. HTML không phải XML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Khi parser đi vào SVG hoặc MathML, không gian tên (namespace / 네임스페이스) và parsing rules thay đổi. Đây là lý do một nút (node / 노드) trong SVG không nên được coi như `div` có shape. Với icon decorative, `aria-hidden="true"` thường phù hợp; với graphic có meaning, cần accessible naming/alternative phù hợp.

---

# PHẦN 2 — HTML PARSER VÀ cây (tree / 트리) CONSTRUCTION

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **9. HTML không phải XML** tiếp nhận điểm tựa từ **8. SVG và MathML là foreign content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Optional end tags và parser repair** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. HTML không phải XML

Trong `text/html`, `img` là void element:

```html
<img src="/a.png" alt="">
```

Viết:

```html
<img src="/a.png" alt="" />
```

không biến document thành XML. Parsing chế độ (mode / 모드) đến từ media kiểu (type / 타입)/ngữ cảnh (context / 맥락) và HTML parser, không đến từ dấu slash. Đây là điểm quan trọng khi bạn học HTML và XML song song.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **10. Optional end tags và parser repair** tiếp nhận điểm tựa từ **9. HTML không phải XML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. <p> auto-closing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Optional end tags và parser repair

HTML cho phép omit một số end tags trong những conditions cụ thể:

```html
<ul>
  <li>A
  <li>B
</ul>
```

Trình duyệt (browser / 브라우저) vẫn có thể tạo hai `li`. Tuy nhiên mã nguồn (source code / 소스 코드) môi trường vận hành (production / 운영 환경) nên ưu tiên closing tags rõ ràng để formatter, reviewer và khung phần mềm (framework / 프레임워크) dễ reason hơn.

HTML parser còn có lỗi (error / 오류) khôi phục (recovery / 복구) mạnh. Việc trình duyệt (browser / 브라우저) kết xuất (render / 렌더링) được markup không chứng minh markup author-conforming hoặc ngữ nghĩa (semantic / 의미적) đúng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **11. <p> auto-closing** tiếp nhận điểm tựa từ **10. Optional end tags và parser repair** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Insertion modes, foster parenting và adoption agency thuật toán (algorithm / 알고리즘)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. `<p>` auto-closing

Nguồn (source / 소스):

```html
<p>
  Hello
  <div>World</div>
</p>
```

không tạo cây (tree / 트리) “div nằm trong p” như indentation gợi ý. Khi parser gặp content không được phép trong `p`, nó có thể đóng `p` trước. Resulting DOM vì vậy khác nguồn (source / 소스).

Đây là một nguyên nhân rất thực tế của SSR hydration mismatch: máy chủ (server / 서버)/template nghĩ một cây (tree / 트리), trình duyệt (browser / 브라우저) repair thành cây (tree / 트리) thứ hai, khung phần mềm (framework / 프레임워크) hydrate dựa trên expectation thứ ba.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **12. Insertion modes, foster parenting và adoption agency thuật toán (algorithm / 알고리즘)** tiếp nhận điểm tựa từ **11. <p> auto-closing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. View nguồn (source / 소스), parsed DOM và khung phần mềm (framework / 프레임워크) cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Insertion modes, foster parenting và adoption agency thuật toán (algorithm / 알고리즘)

HTML parser là context-sensitive. Nó có các insertion modes như `in head`, `in body`, `in table`, `in row`, `in cell`. Một đơn vị từ (token / 토큰) xuất hiện trong bảng (table / 테이블) ngữ cảnh (context / 맥락) có thể được xử lý khác khi nó xuất hiện trong ordinary body luồng (flow / 흐름).

Với malformed bảng (table / 테이블) content, trình duyệt (browser / 브라우저) có thể di chuyển nút (node / 노드) ra khỏi bảng (table / 테이블) theo rules thường được gọi là **foster parenting**. Với một số formatting elements bị nest sai, parser có thuật toán (algorithm / 알고리즘) đặc biệt thường được gọi là **adoption agency thuật toán (algorithm / 알고리즘)**.

Bạn không cần thuộc từng bước thuật toán. Điều cần hiểu là DOM được quyết định bởi parser thuật toán (algorithm / 알고리즘), không phải indentation và cũng không phải “trình duyệt (browser / 브라우저) đoán ngẫu nhiên”.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **12. Insertion modes, foster parenting và adoption agency thuật toán (algorithm / 알고리즘)** nêu điều cần giải thích; **13. View nguồn (source / 소스), parsed DOM và khung phần mềm (framework / 프레임워크) cây (tree / 트리)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Raw văn bản (text / 텍스트), RCDATA và character references** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. View nguồn (source / 소스), parsed DOM và khung phần mềm (framework / 프레임워크) cây (tree / 트리)

Ba tầng (layer / 계층) phải được phân biệt. View nguồn (source / 소스) gần với original phản hồi (response / 응답). DOM là kết quả sau tokenizer/cây (tree / 트리) construction và sau các thời gian chạy (runtime / 런타임) mutations. React/Vue/Svelte lại có nội bộ (internal / 내부) thành phần (component / 컴포넌트)/cây (tree / 트리) mô hình (model / 모델) riêng.

Khi gỡ lỗi (debug / 디버그) hydration, bảng (table / 테이블) cấu trúc (structure / 구조) hoặc invalid nesting, hãy so sánh original HTML với Elements panel thay vì chỉ nhìn JSX/template.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **13. View nguồn (source / 소스), parsed DOM và khung phần mềm (framework / 프레임워크) cây (tree / 트리)** nêu điều cần giải thích; **14. Raw văn bản (text / 텍스트), RCDATA và character references** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **15. Form đơn vị sở hữu (owner / 오너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Raw văn bản (text / 텍스트), RCDATA và character references

`script` và `style` có parsing contexts khác ordinary văn bản (text / 텍스트). `title` và `textarea` cũng có RCDATA-like parsing hành vi (behavior / 동작). Vì vậy một escaping chiến lược (strategy / 전략) đúng cho văn bản (text / 텍스트) nút (node / 노드) bình thường không tự động đúng cho JavaScript/CSS/script contexts.

Character references như `&amp;`, `&lt;`, `&gt;` và `&quot;` dùng khi cần biểu diễn special characters. `&nbsp;` là non-breaking không gian (space / 공간), không phải công cụ để tạo bố cục (layout / 레이아웃) spacing; bố cục (layout / 레이아웃) thuộc CSS.

---

# PHẦN 3 — FORM INTERNALS VÀ LIVE trạng thái (state / 상태)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **15. Form đơn vị sở hữu (owner / 오너)** tiếp nhận điểm tựa từ **14. Raw văn bản (text / 텍스트), RCDATA và character references** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Submitter và implicit submission** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Form đơn vị sở hữu (owner / 오너)

Form-associated điều khiển (control / 제어) có một **form đơn vị sở hữu (owner / 오너)**. Bình thường đơn vị sở hữu (owner / 오너) là ancestor form:

```html
<form id="profile">
  <input name="email">
</form>
```

Nhưng điều khiển (control / 제어) có thể associate từ bên ngoài:

```html
<form id="profile">
  ...
</form>

<button type="submit" form="profile">
  Save
</button>
```

Trình duyệt (browser / 브라우저) dùng `form="profile"` để liên kết điều khiển (control / 제어) với form ID. Điều này hữu ích với sticky hành động (action / 동작) bars hoặc thành phần (component / 컴포넌트) layouts nơi visual position không trùng DOM nesting.

Nested `form` không phải cách tạo form con. Hãy dùng sibling forms hoặc tường minh (explicit / 명시적) `form` association.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **16. Submitter và implicit submission** tiếp nhận điểm tựa từ **15. Form đơn vị sở hữu (owner / 오너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Successful controls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Submitter và implicit submission

Button trigger form submission được gọi là submitter:

```html
<button
  type="submit"
  name="action"
  value="publish">
  Publish
</button>
```

Submitter có thể thêm `action=publish` vào form dữ liệu (data / 데이터) và có thể override `formaction`, `formmethod`, `formenctype`, `formtarget`, `formnovalidate`.

Pressing Enter trong văn bản (text / 텍스트) điều khiển (control / 제어) có thể trigger implicit submission tùy form cấu trúc (structure / 구조). Vì vậy button không phải submit nên ghi `type="button"` rõ ràng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **17. Successful controls** tiếp nhận điểm tựa từ **16. Submitter và implicit submission** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Disabled, readonly và disabled fieldset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Successful controls

Khi form submit, trình duyệt (browser / 브라우저) không đơn giản serialize mọi đầu vào (input / 입력) nằm trong DOM. điều khiển (control / 제어) phải đáp ứng submission rules. `name` thường cần thiết; disabled controls thường không đóng góp entry; unchecked checkbox/radio thường không tạo entry; readonly giá trị (value / 값) vẫn có thể submit; submit button chỉ đóng góp khi nó là submitter.

Đây là reason backend đôi khi “không nhận được trường dữ liệu (field / 필드)” dù trường dữ liệu (field / 필드) hiển thị trên UI. gỡ lỗi (debug / 디버그) bằng form-data ngữ nghĩa (semantics / 의미론) trước khi đổ lỗi mạng (network / 네트워크) thư viện (library / 라이브러리).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **18. Disabled, readonly và disabled fieldset** tiếp nhận điểm tựa từ **17. Successful controls** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Reset, trạng thái hiện tại (current state / 현재 상태) và default trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Disabled, readonly và disabled fieldset

`disabled` thường khiến điều khiển (control / 제어) không focus/edit và không submit. `readonly` ngăn sửa ở các supported điều khiển (control / 제어) types nhưng giá trị (value / 값) vẫn có thể được submit.

```html
<input name="accountId" value="A123" readonly>
```

Không được coi readonly giá trị (value / 값) là trusted; máy khách (client / 클라이언트) vẫn có thể sửa yêu cầu (request / 요청).

`fieldset disabled` disable phần lớn descendants nhưng first `legend` có special hành vi (behavior / 동작). Đây là trường hợp biên (edge case / 경계 사례) hữu ích khi đọc bản địa (native / 네이티브) form algorithms, dù ứng dụng (application / 애플리케이션) bình thường không cần dựa vào nó như một trick.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **19. Reset, trạng thái hiện tại (current state / 현재 상태) và default trạng thái (state / 상태)** tiếp nhận điểm tựa từ **18. Disabled, readonly và disabled fieldset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. dirname và capture** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Reset, trạng thái hiện tại (current state / 현재 상태) và default trạng thái (state / 상태)

`type="reset"` không “xóa trắng form”; nó restore default trạng thái (state / 상태).

```html
<input value="Alice">
```

sau khi người dùng (user / 사용자) sửa thành `Bob`, `input.value` là trạng thái hiện tại (current state / 현재 상태) còn `input.defaultValue` liên quan reset/default trạng thái (state / 상태). Checkbox có `checked` và `defaultChecked`; option có `selected` và `defaultSelected`.

Đây là một ví dụ quan trọng cho relationship giữa markup attribute và DOM thuộc tính (property / 속성).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **20. dirname và capture** tiếp nhận điểm tựa từ **19. Reset, trạng thái hiện tại (current state / 현재 상태) và default trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Attribute không đồng nghĩa live thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. `dirname` và `capture`

`dirname` cho phép trình duyệt (browser / 브라우저) submit văn bản (text / 텍스트) direction siêu dữ liệu (metadata / 메타데이터) cùng trường dữ liệu (field / 필드), hữu ích với international user-generated content.

`capture` trên tệp (file / 파일) đầu vào (input / 입력) là hint cho mobile capture nguồn (source / 소스):

```html
<input
  type="file"
  accept="image/*"
  capture="environment">
```

Nó không phải bảo mật (security / 보안)/permission guarantee và UX có thể khác theo trình duyệt (browser / 브라우저)/thiết bị (device / 장치).

---

# PHẦN 4 — DOM quan hệ (relation / 관계) VÀ DOM CLOBBERING

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **21. Attribute không đồng nghĩa live thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **20. dirname và capture** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. DOM clobbering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Attribute không đồng nghĩa live thuộc tính (property / 속성)

Markup là initial declarative trạng thái (state / 상태); DOM đối tượng (object / 객체) có live properties. Ví dụ người dùng (user / 사용자) có thể thay đổi `input.value` mà `getAttribute("value")` vẫn phản ánh initial/default markup.

Tương tự, `a.getAttribute("href")` có thể là relative URL `/users`, còn `a.href` thường là URL đã được resolve thành absolute URL.

Cấp cao (senior / 시니어) cần biết attribute reflection rules khác nhau theo từng API thay vì assume attribute/thuộc tính (property / 속성) luôn sync hai chiều.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **22. DOM clobbering** tiếp nhận điểm tựa từ **21. Attribute không đồng nghĩa live thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Microdata** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. DOM clobbering

HTML có historical named-access hành vi (behavior / 동작). Một form điều khiển (control / 제어) có `name="method"` hoặc `name="submit"` có thể collide với thuộc tính (property / 속성) mà mã (code / 코드) tưởng là built-in member.

```html
<form id="user-form">
  <input name="method">
</form>
```

Với untrusted markup, named truy cập (access / 접근) có thể góp phần tạo bảo mật (security / 보안) bugs. Tránh relying vào magic globals hoặc properties do `id`/`name` tự expose. Dùng tường minh (explicit / 명시적) selectors, `form.elements.namedItem()` và APIs như `requestSubmit()`.

DOM không nên được dùng như trusted cấu hình (configuration / 구성) store.

---

# PHẦN 5 — MICRODATA

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **23. Microdata** tiếp nhận điểm tựa từ **22. DOM clobbering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. <template>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Microdata

Microdata là structured-data cơ chế (mechanism / 메커니즘) bản địa (native / 네이티브) của HTML với `itemscope`, `itemtype`, `itemprop`, `itemid`, `itemref`.

```html
<article
  itemscope
  itemtype="https://schema.org/Book">

  <h1 itemprop="name">Example Book</h1>
  <span itemprop="author">Alice</span>
</article>
```

JSON-LD thường dễ quản lý hơn trong SEO kiến trúc (architecture / 아키텍처) hiện đại, nhưng Microdata vẫn quan trọng khi kiểm tra (audit / 감사) CMS hoặc legacy structured markup. trình duyệt (browser / 브라우저) không biến Microdata thành visual hành vi (behavior / 동작); nó bổ sung machine-readable relationships trên document.

---

# PHẦN 6 — TEMPLATE, CUSTOM ELEMENTS VÀ SHADOW DOM

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **24. <template>** tiếp nhận điểm tựa từ **23. Microdata** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Declarative Shadow DOM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `<template>`

`template` chứa inert fragment:

```html
<template id="row-template">
  <tr><td></td></tr>
</template>
```

Content không participate như ordinary rendered content cho tới khi được clone/insert, và template còn là foundation của Declarative Shadow DOM.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **25. Declarative Shadow DOM** tiếp nhận điểm tựa từ **24. <template>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Slots và composed cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Declarative Shadow DOM

Máy chủ (server / 서버) có thể gửi:

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

Trình duyệt (browser / 브라우저) có thể attach shadow gốc (root / 루트) ngay trong parse stage. Điều này đặc biệt hữu ích cho SSR Web Components vì encapsulated DOM/style có thể tồn tại trước JavaScript boot.

`shadowrootmode="open"` cho phép normal `host.shadowRoot` truy cập (access / 접근); `closed` không expose gốc (root / 루트) qua getter thông thường nhưng không phải bảo mật (security / 보안) sandbox. `shadowrootdelegatesfocus` ảnh hưởng focus delegation; advanced options như clonable hành vi (behavior / 동작) cần check tính tương thích (compatibility / 호환성) khi hạ tầng (infrastructure / 인프라) phụ thuộc chúng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **26. Slots và composed cây (tree / 트리)** tiếp nhận điểm tựa từ **25. Declarative Shadow DOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Custom elements và form-associated custom elements** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Slots và composed cây (tree / 트리)

Shadow DOM dùng `slot` để phân phối light-DOM content:

```html
<slot name="title"></slot>
```

```html
<user-card>
  <h2 slot="title">Alice</h2>
</user-card>
```

Đây là lý do nguồn (source / 소스)/light DOM, shadow DOM, rendered flat/composed cây (tree / 트리) và cây khả năng tiếp cận (accessibility tree / 접근성 트리) không phải lúc nào giống nhau. Khi gỡ lỗi (debug / 디버그) focus hoặc accessible name trong Web Components, phải biết nút (node / 노드) đang tồn tại ở cây (tree / 트리) nào.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **27. Custom elements và form-associated custom elements** tiếp nhận điểm tựa từ **26. Slots và composed cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. hidden="until-found"** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Custom elements và form-associated custom elements

Autonomous custom element phải có dấu `-`:

```html
<user-card></user-card>
```

JavaScript register qua `customElements.define()`. Customized built-in mô hình (model / 모델) còn có `is`, nhưng kiến trúc (architecture / 아키텍처)/hỗ trợ (support / 지원) cần được kiểm tra kỹ.

Advanced components có thể tham gia form mô hình (model / 모델) thông qua `ElementInternals`. Điều này powerful cho thiết kế (design / 설계) các hệ thống (systems / 시스템들) nhưng không miễn bạn khỏi việc implement labels, validity, form giá trị (value / 값) và khả năng tiếp cận (accessibility / 접근성) ngữ nghĩa (semantics / 의미론). Nếu bản địa (native / 네이티브) điều khiển (control / 제어) đáp ứng yêu cầu (requirement / 요구사항) thì bản địa (native / 네이티브) element thường là lựa chọn ít lỗi hơn.

---

# PHẦN 7 — HIDDEN, POPOVER VÀ TOP tầng (layer / 계층)

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **28. hidden="until-found"** tiếp nhận điểm tựa từ **27. Custom elements và form-associated custom elements** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Popover modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `hidden="until-found"`

Ordinary `hidden` nói content hiện tại không relevant/presented. `hidden="until-found"` cho phép content vẫn có thể được trình duyệt (browser / 브라우저) reveal khi find-in-page hoặc fragment điều hướng (navigation / 내비게이션) tìm thấy mục tiêu (target / 대상) trong supporting hành vi (behavior / 동작).

```html
<section id="advanced" hidden="until-found">
  Advanced parser details
</section>
```

`beforematch` có thể được dispatch trước reveal để ứng dụng (application / 애플리케이션) prepare surrounding UI. Đây là ví dụ browser-native Find/điều hướng (navigation / 내비게이션) tích hợp với ứng dụng (application / 애플리케이션) trạng thái (state / 상태).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **29. Popover modes** tiếp nhận điểm tựa từ **28. hidden="until-found"** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Top tầng (layer / 계층)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Popover modes

Popover API tạo floating UI mà trình duyệt (browser / 브라우저) quản lý show/hide/top-layer hành vi (behavior / 동작).

```html
<button popovertarget="help">Help</button>
<div id="help" popover>...</div>
```

`auto` phù hợp với popovers có light dismiss; `manual` cho ứng dụng (application / 애플리케이션) điều khiển (control / 제어) persistence; `hint` hướng tới transient hint/tooltip-like interactions trong supporting browsers. `popovertargetaction` có thể yêu cầu `show`, `hide` hoặc `toggle`.

Popover không tự quyết định nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) của content. Một menu vẫn cần đúng menu/điều hướng (navigation / 내비게이션)/điều khiển (control / 제어) ngữ nghĩa (semantics / 의미론); Popover chỉ giải quyết overlay vòng đời (lifecycle / 생명주기)/top-layer thành phần nguyên thủy (primitive / 기본 요소).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **30. Top tầng (layer / 계층)** tiếp nhận điểm tựa từ **29. Popover modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Modal và non-modal dialog** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Top tầng (layer / 계층)

Top tầng (layer / 계층) không phải `z-index` cực lớn. Nó là browser-managed tầng (layer / 계층) dành cho một số UI như modal dialog và popover. Vì vậy nó tránh nhiều vấn đề ancestor ngữ cảnh xếp chồng (stacking context / 쌓임 맥락) hoặc overflow clipping mà custom overlay gặp.

Khi bản địa (native / 네이티브) top-layer thành phần nguyên thủy (primitive / 기본 요소) phù hợp, thường tốt hơn việc bắt đầu bằng `position: fixed; z-index: 999999`.

---

# PHẦN 8 — DIALOG VÀ DECLARATIVE COMMANDS

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **31. Modal và non-modal dialog** tiếp nhận điểm tựa từ **30. Top tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. command và commandfor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Modal và non-modal dialog

`dialog.show()` mở non-modal; `dialog.showModal()` mở modal. Modal dialog tham gia top tầng (layer / 계층) và trình duyệt (browser / 브라우저) quản lý surrounding tương tác (interaction / 상호작용) theo modal mô hình (model / 모델).

`cancel` liên quan nền tảng (platform / 플랫폼) close yêu cầu (request / 요청) như Escape; `close` xảy ra sau khi dialog đóng. `form method="dialog"` cho phép button submit đóng dialog mà không gửi mạng (network / 네트워크) yêu cầu (request / 요청).

Hiện đại (modern / 현대적) `closedby` cho phép mô tả close hành vi (behavior / 동작) như `any`, `closerequest` hoặc `none` trong supporting browsers. Vì đây là tính năng (feature / 기능) mới hơn, môi trường vận hành (production / 운영 환경) cần check target-browser tính tương thích (compatibility / 호환성).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **32. command và commandfor** tiếp nhận điểm tựa từ **31. Modal và non-modal dialog** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. <selectedcontent> và rich options** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. `command` và `commandfor`

Hiện đại (modern / 현대적) HTML đang mở rộng declarative tương tác (interaction / 상호작용):

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

Các commands như `show-modal`, `close`, `request-close` có thể giảm JavaScript boilerplate. Ý nghĩa cấp cao (senior / 시니어) ở đây là luôn kiểm tra bản địa (native / 네이티브) nền tảng (platform / 플랫폼) trước khi tự xây một máy trạng thái (state machine / 상태 머신) custom, nhưng tính năng (feature / 기능) mới phải được progressive-enhance thay vì assume hỗ trợ (support / 지원) universal.

---

# PHẦN 9 — CUSTOMIZABLE SELECT

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **33. <selectedcontent> và rich options** tiếp nhận điểm tựa từ **32. command và commandfor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. referrerpolicy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. `<selectedcontent>` và rich options

Classic select rất mạnh về keyboard/mobile/khả năng tiếp cận (accessibility / 접근성) nhưng khó style. Customizable select mô hình (model / 모델) cho trình duyệt (browser / 브라우저) hỗ trợ richer markup trong select trong những môi trường phù hợp.

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

`selectedcontent` hiển thị content tương ứng với selected option theo nền tảng (platform / 플랫폼) mô hình (model / 모델). Đây là tính năng (feature / 기능) hiện đại nên phải kiểm thử (test / 테스트) trình duyệt (browser / 브라우저)/khung phần mềm (framework / 프레임워크)/SSR tính tương thích (compatibility / 호환성). Progressive enhancement là chiến lược (strategy / 전략) đúng: trình duyệt (browser / 브라우저) mới được richer styling, trình duyệt (browser / 브라우저) cũ vẫn dùng usable bản địa (native / 네이티브) select.

---

# PHẦN 10 — ADVANCED tài nguyên (resource / 자원), LINK VÀ yêu cầu (request / 요청) ATTRIBUTES

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **34. referrerpolicy** tiếp nhận điểm tựa từ **33. <selectedcontent> và rich options** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. crossorigin và CORS chế độ (mode / 모드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. `referrerpolicy`

`referrerpolicy` có thể xuất hiện trên link, anchor, ảnh (image / 이미지), script, iframe và một số tài nguyên (resource / 자원) elements. Nó kiểm soát lượng referrer thông tin (information / 정보) trình duyệt (browser / 브라우저) gửi cùng yêu cầu (request / 요청).

```html
<a
  href="https://external.example"
  referrerpolicy="no-referrer">
  External
</a>
```

Policies như `no-referrer`, `origin`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin` thuộc privacy/bảo mật (security / 보안) yêu cầu (request / 요청) hành vi (behavior / 동작). Chúng không thay authorization.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **35. crossorigin và CORS chế độ (mode / 모드)** tiếp nhận điểm tựa từ **34. referrerpolicy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. ping và hyperlink auditing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. `crossorigin` và CORS chế độ (mode / 모드)

`crossorigin` không chỉ là một string decoration. Trên các tài nguyên (resource / 자원) elements phù hợp, nó thay đổi CORS yêu cầu (request / 요청)/phản hồi (response / 응답) handling.

Ví dụ:

```html
<img
  src="https://cdn.example.com/photo.png"
  crossorigin="anonymous"
  alt="Product">
```

Nếu cross-origin ảnh (image / 이미지) được draw vào canvas mà CORS không cho phép, canvas có thể trở thành **tainted**, khiến trình duyệt (browser / 브라우저) khối (block / 블록) pixel-reading/export APIs. Vì vậy `crossorigin` có browser-processing consequence rõ ràng.

Trên script/link/font/SRI scenarios, CORS chế độ (mode / 모드) cũng có thể ảnh hưởng việc tài nguyên (resource / 자원) được chấp nhận. Hãy cấu hình cùng máy chủ (server / 서버) phản hồi (response / 응답) headers; attribute một mình không magically cấp quyền cross-origin.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **36. ping và hyperlink auditing** tiếp nhận điểm tựa từ **35. crossorigin và CORS chế độ (mode / 모드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. hreflang, alternate resources và SEO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. `ping` và hyperlink auditing

Anchor có thể có `ping`:

```html
<a href="/product" ping="/analytics/link-click">
  Product
</a>
```

Trình duyệt (browser / 브라우저) có thể gửi auditing requests khi điều hướng (navigation / 내비게이션) xảy ra. Vì có privacy implication và analytics ecosystem còn nhiều cách khác, cấp cao (senior / 시니어) chủ yếu cần biết để kiểm tra (audit / 감사) mạng (network / 네트워크) hành vi (behavior / 동작) thay vì coi đây là default tracking solution.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **36. ping và hyperlink auditing** nêu điều cần giải thích; **37. hreflang, alternate resources và SEO** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **38. Responsive preload và priority hints** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. `hreflang`, alternate resources và SEO
Phần này nối mạch bài học với “37. `hreflang`, alternate resources và SEO”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<link
  rel="alternate"
  hreflang="ko"
  href="https://example.com/ko/page">
```

`hreflang` mô tả ngôn ngữ (language / 언어) relationship cho alternate page/tài nguyên (resource / 자원). trình duyệt (browser / 브라우저)/tìm kiếm (search / 검색) các hệ thống (systems / 시스템들) có thể dùng siêu dữ liệu (metadata / 메타데이터) này; nó không tự dịch content và không thay `lang` trên document.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **37. hreflang, alternate resources và SEO** nêu điều cần giải thích; **38. Responsive preload và priority hints** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **39. Parser-blocking, render-blocking và preload scanner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Responsive preload và priority hints

Nếu LCP ảnh (image / 이미지) có `srcset`, preload một hard-coded candidate có thể khiến trình duyệt (browser / 브라우저) fetch tài nguyên (resource / 자원) không phù hợp. Responsive ảnh (image / 이미지) preload có thể cần `imagesrcset`/`imagesizes` tương ứng.

`fetchpriority` là hint, không phải scheduler command tuyệt đối. Nếu mọi tài nguyên (resource / 자원) đều `high`, priority tín hiệu (signal / 신호) mất ý nghĩa.

Hiệu năng (performance / 성능) decisions nên đo bằng mạng (network / 네트워크) panel, cốt lõi (core / 핵심) Web Vitals/RUM hoặc profiler thay vì thêm preload/preconnect theo cảm giác.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **39. Parser-blocking, render-blocking và preload scanner** tiếp nhận điểm tựa từ **38. Responsive preload và priority hints** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. meta http-equiv không phải replacement hoàn chỉnh cho HTTP headers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Parser-blocking, render-blocking và preload scanner

Parser-blocking nghĩa main HTML parser phải dừng/coordinate với script/tài nguyên (resource / 자원). Render-blocking nghĩa trình duyệt (browser / 브라우저) trì hoãn paint vì tài nguyên (resource / 자원) cần thiết. Hai concepts không phải synonym.

Trình duyệt (browser / 브라우저) còn có speculative/preload scanner để discover tài nguyên (resource / 자원) URLs sớm. Vì vậy nguồn (source / 소스) thứ tự (order / 순서) và việc URL có xuất hiện trực tiếp trong HTML hay chỉ được JavaScript tạo sau đó có thể ảnh hưởng thời điểm fetch.

---

# PHẦN 11 — siêu dữ liệu (metadata / 메타데이터) ADVANCED

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **40. meta http-equiv không phải replacement hoàn chỉnh cho HTTP headers** tiếp nhận điểm tựa từ **39. Parser-blocking, render-blocking và preload scanner** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. meta name="color-scheme"** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. `meta http-equiv` không phải replacement hoàn chỉnh cho HTTP headers

`http-equiv` tạo một số pragma/directive-like effects trong HTML document:

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'">
```

hoặc legacy refresh hành vi (behavior / 동작):

```html
<meta
  http-equiv="refresh"
  content="5;url=/next">
```

Trình duyệt (browser / 브라우저) chỉ hỗ trợ những directives cụ thể. Khi bạn kiểm soát máy chủ (server / 서버), real HTTP phản hồi (response / 응답) headers thường là tầng (layer / 계층) rõ và mạnh hơn cho bảo mật (security / 보안)/chính sách mạng (network policy / 네트워크 정책), đặc biệt với CSP. Đừng nhìn `http-equiv` rồi nghĩ bất kỳ HTTP header nào cũng có thể được mô phỏng trong HTML.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **41. meta name="color-scheme"** tiếp nhận điểm tựa từ **40. meta http-equiv không phải replacement hoàn chỉnh cho HTTP headers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Document-level referrer chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. `meta name="color-scheme"`
Phần này nối mạch bài học với “41. `meta name="color-scheme"`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<meta
  name="color-scheme"
  content="light dark">
```

Siêu dữ liệu (metadata / 메타데이터) này nói document hỗ trợ những color schemes nào, giúp trình duyệt (browser / 브라우저) chọn default rendering cho form controls, scrollbars hoặc canvas/background-related trình duyệt (browser / 브라우저) UI trong applicable contexts. Nó không thay CSS theme hệ thống (system / 시스템); CSS vẫn chịu trách nhiệm presentation cụ thể.

Khả năng tiếp cận (accessibility / 접근성) implication là UA controls có thể hòa hợp tốt hơn với light/dark môi trường (environment / 환경) và tránh contrast mismatch do trình duyệt (browser / 브라우저) default khác theme app.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **42. Document-level referrer chính sách (policy / 정책)** tiếp nhận điểm tựa từ **41. meta name="color-scheme"** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. bản địa (native / 네이티브) HTML trước ARIA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Document-level referrer chính sách (policy / 정책)

Ngoài element-level `referrerpolicy`, document có thể dùng siêu dữ liệu (metadata / 메타데이터) phù hợp để đặt referrer chính sách (policy / 정책) chung. cấp cao (senior / 시니어) nên hiểu chính sách (policy / 정책) có thể đến từ HTTP header, document siêu dữ liệu (metadata / 메타데이터) hoặc element-level override tùy cơ chế (mechanism / 메커니즘).

Nguyên tắc thiết kế là chính sách (policy / 정책) toàn site/document nên được đặt ở ranh giới (boundary / 경계) dễ kiểm tra (audit / 감사); element-level override chỉ dùng khi tài nguyên (resource / 자원)/link có yêu cầu (requirement / 요구사항) riêng.

---

# PHẦN 12 — khả năng tiếp cận (accessibility / 접근성) VÀ ARIA NHƯ MỘT API tầng (layer / 계층)

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **43. bản địa (native / 네이티브) HTML trước ARIA** tiếp nhận điểm tựa từ **42. Document-level referrer chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Accessible name và description** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. bản địa (native / 네이티브) HTML trước ARIA

Nguyên tắc quan trọng nhất là: nếu bản địa (native / 네이티브) HTML element đã có ngữ nghĩa (semantics / 의미론) và hành vi (behavior / 동작) cần thiết, hãy dùng nó trước khi tạo custom element bằng role.

```html
<button type="button">Save</button>
```

thường tốt hơn:

```html
<div role="button" tabindex="0">Save</div>
```

`role="button"` có thể làm khả năng tiếp cận (accessibility / 접근성) API expose nút (node / 노드) như button, nhưng nó không tự thêm không gian (space / 공간)/Enter activation, disabled ngữ nghĩa (semantics / 의미론), form hành vi (behavior / 동작) hoặc keyboard handling. ARIA thay đổi ngữ nghĩa (semantic / 의미적) exposure; nó không tự tạo trình duyệt (browser / 브라우저) hành vi (behavior / 동작) tương ứng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **44. Accessible name và description** tiếp nhận điểm tựa từ **43. bản địa (native / 네이티브) HTML trước ARIA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. aria-expanded và aria-controls** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Accessible name và description

Bản địa (native / 네이티브) `<label>` hoặc element văn bản (text / 텍스트) thường là nguồn accessible name tốt nhất. `aria-labelledby` cho phép name đến từ nút (node / 노드) khác; `aria-label` cung cấp tường minh (explicit / 명시적) string khi visible label không phù hợp, ví dụ icon-only button.

Sai:

```html
<button aria-label="Delete">Save</button>
```

Visual người dùng (user / 사용자) thấy `Save` còn assistive technology có thể announce `Delete`, tạo severe mismatch.

Description là channel khác name:

```html
<label for="password">Password</label>
<input
  id="password"
  aria-describedby="password-help">
<p id="password-help">At least 12 characters.</p>
```

Name trả lời “điều khiển (control / 제어) là gì”; description cung cấp hướng dẫn bổ sung.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **45. aria-expanded và aria-controls** tiếp nhận điểm tựa từ **44. Accessible name và description** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. aria-invalid và aria-errormessage** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. `aria-expanded` và `aria-controls`
Phần này nối mạch bài học với “45. `aria-expanded` và `aria-controls`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<button
  aria-expanded="false"
  aria-controls="filters">
  Filters
</button>
```

`aria-expanded` expose trạng thái (state / 상태) cho khả năng tiếp cận (accessibility / 접근성) API nhưng JavaScript hoặc bản địa (native / 네이티브) hành vi (behavior / 동작) phải cập nhật nó khi trạng thái (state / 상태) thay đổi. `aria-controls` mô tả relationship với element được điều khiển (control / 제어); nó không tự open/close mục tiêu (target / 대상).

Nếu bản địa (native / 네이티브) `details/summary` hoặc Popover đáp ứng use trường hợp (case / 사례), chúng thường giảm nguy cơ trạng thái (state / 상태) visual và ARIA trạng thái (state / 상태) bị lệch nhau.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **46. aria-invalid và aria-errormessage** tiếp nhận điểm tựa từ **45. aria-expanded và aria-controls** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. aria-busy, live regions và động (dynamic / 동적) updates** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. `aria-invalid` và `aria-errormessage`

Khi kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) xuất hiện, điều khiển (control / 제어) có thể expose invalid trạng thái (state / 상태) và tham chiếu (reference / 참조) lỗi (error / 오류) văn bản (text / 텍스트):

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

`aria-invalid` nói hiện tại (current / 현재) giá trị (value / 값) invalid; `aria-errormessage` identifies lỗi (error / 오류) message. Hai attributes không validate giá trị (value / 값) và không automatically show văn bản (text / 텍스트). ứng dụng (application / 애플리케이션)/bản địa (native / 네이티브) kiểm tra hợp lệ (validation / 검증) vẫn phải quyết định lỗi và manage vòng đời (lifecycle / 생명주기) của message.

Nếu đầu vào (input / 입력) đang valid, đừng để stale `aria-invalid="true"` chỉ vì UI đã từng có lỗi (error / 오류).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **47. aria-busy, live regions và động (dynamic / 동적) updates** tiếp nhận điểm tựa từ **46. aria-invalid và aria-errormessage** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. aria-hidden, hidden, inert và disabled khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. `aria-busy`, live regions và động (dynamic / 동적) updates

`aria-busy="true"` có thể báo rằng một region đang được cập nhật và assistive technology có thể trì hoãn xử lý announcements phù hợp. `aria-live` dùng cho động (dynamic / 동적) messages cần announce mà focus không chuyển tới đó.

Không biến toàn app thành `aria-live`. Live region quá rộng hoặc `assertive` quá nhiều sẽ gây noise/interruptions. khả năng tiếp cận (accessibility / 접근성) tốt là chọn đúng sự kiện (event / 이벤트) cần announce, không phải thêm nhiều ARIA nhất có thể.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **48. aria-hidden, hidden, inert và disabled khác nhau** tiếp nhận điểm tựa từ **47. aria-busy, live regions và động (dynamic / 동적) updates** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Sanitization không phải remove <script>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. `aria-hidden`, `hidden`, `inert` và `disabled` khác nhau

`aria-hidden="true"` chủ yếu ảnh hưởng cây khả năng tiếp cận (accessibility tree / 접근성 트리); element vẫn có thể visible. `hidden` nói content không được present/relevant theo HTML trạng thái (state / 상태). `inert` làm subtree non-interactive/focusable theo nền tảng (platform / 플랫폼) hành vi (behavior / 동작). `disabled` áp cho supported controls và còn ảnh hưởng form submission.

Đặc biệt không đặt `aria-hidden="true"` trên ancestor chứa focusable controls; bạn có thể tạo UI mà keyboard focus tới được nhưng screen reader không thấy ngữ nghĩa (semantic / 의미적) tương ứng.

---

# PHẦN 13 — bảo mật (security / 보안) DEEPER

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **49. Sanitization không phải remove <script>** tiếp nhận điểm tựa từ **48. aria-hidden, hidden, inert và disabled khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. URL-valued attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Sanitization không phải remove `<script>`

Untrusted HTML attack surface gồm event-handler attributes, dangerous URL schemes, SVG/foreign content, `srcdoc`, DOM clobbering và nhiều parser contexts khác. Regex remove `<script>` không phải sanitizer.

Nếu ứng dụng (application / 애플리케이션) thực sự cho phép rich HTML đầu vào (input / 입력), dùng sanitizer được thiết kế cho HTML parser mô hình (model / 모델) và áp CSP/Trusted Types hoặc các defense phù hợp kiến trúc (architecture / 아키텍처). Nếu chỉ cần văn bản (text / 텍스트), dùng văn bản (text / 텍스트) APIs thay vì HTML parsing APIs.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **50. URL-valued attributes** tiếp nhận điểm tựa từ **49. Sanitization không phải remove <script>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. iframe srcdoc, sandbox và permissions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. URL-valued attributes

Escaping HTML characters không tự làm URL safe. Nếu user-controlled giá trị (value / 값) đi vào `href`, `src`, `action` hoặc tương tự, ứng dụng (application / 애플리케이션) còn phải validate allowed schemes/origins theo use trường hợp (case / 사례).

Ví dụ nếu tính năng (feature / 기능) chỉ cho bên ngoài (external / 외부) web links, allowlist `https:`/`http:` phù hợp hơn việc chấp nhận bất kỳ scheme nào. `javascript:` URL là lý do URL kiểm tra hợp lệ (validation / 검증) và HTML escaping là hai defense khác nhau.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **51. iframe srcdoc, sandbox và permissions** tiếp nhận điểm tựa từ **50. URL-valued attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Valid HTML quan trọng đặc biệt với SSR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. `iframe srcdoc`, sandbox và permissions

`srcdoc` là một HTML document thực thi (execution / 실행) ngữ cảnh (context / 맥락), không phải văn bản (text / 텍스트) bộ chứa (container / 컨테이너). Untrusted content cần sanitization và sandbox chiến lược (strategy / 전략).

`sandbox` nên theo least privilege. `allow`/Permissions chính sách (policy / 정책) chỉ cấp capabilities cần thiết. `referrerpolicy` kiểm soát referrer leakage. Một third-party iframe là browsing/ranh giới bảo mật (security boundary / 보안 경계) chứ không chỉ là visual box.

---

# PHẦN 14 — SSR, FRAMEWORKS VÀ PARSER-STABLE MARKUP

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **52. Valid HTML quan trọng đặc biệt với SSR** tiếp nhận điểm tựa từ **51. iframe srcdoc, sandbox và permissions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Declarative Shadow DOM và SSR** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Valid HTML quan trọng đặc biệt với SSR

JSX có thể viết cấu trúc (structure / 구조) mà trình duyệt (browser / 브라우저) HTML parser sẽ repair. Nếu máy chủ (server / 서버) đầu ra (output / 출력) và trình duyệt (browser / 브라우저) DOM khác nhau trước khi React/Vue hydrate, khung phần mềm (framework / 프레임워크) có thể báo hydration mismatch hoặc replace nodes.

Trình duyệt (browser / 브라우저) không parse JSX; trình duyệt (browser / 브라우저) parse generated HTML. Vì vậy khung phần mềm (framework / 프레임워크) nhà phát triển (developer / 개발자) vẫn phải hiểu HTML content các mô hình (models / 모델들), optional tags, bảng (table / 테이블) parsing và interactive-content restrictions.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **53. Declarative Shadow DOM và SSR** tiếp nhận điểm tựa từ **52. Valid HTML quan trọng đặc biệt với SSR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **54. “trình duyệt (browser / 브라우저) vẫn kết xuất (render / 렌더링)” không có nghĩa markup còn hợp chuẩn để author** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Declarative Shadow DOM và SSR

Server-rendered custom thành phần (component / 컴포넌트) có thể gửi declarative shadow template để trình duyệt (browser / 브라우저) tạo shadow gốc (root / 루트) trong parse stage. Điều này làm encapsulation/styles tồn tại trước JavaScript upgrade và giảm flash/mismatch trong một số Web thành phần (component / 컴포넌트) architectures.

Khi dùng, kiểm thử (test / 테스트) parser hành vi (behavior / 동작), khung phần mềm (framework / 프레임워크) hỗ trợ (support / 지원) và serialization chuỗi xử lý (pipeline / 파이프라인); tooling cũ có thể chưa hiểu content mô hình (model / 모델)/attributes mới.

---

# PHẦN 15 — LEGACY, DEPRECATED VÀ OBSOLETE HTML

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **54. “trình duyệt (browser / 브라우저) vẫn kết xuất (render / 렌더링)” không có nghĩa markup còn hợp chuẩn để author** tiếp nhận điểm tựa từ **53. Declarative Shadow DOM và SSR** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **55. Presentational elements: <font>, <center>, <big> và <tt>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. “trình duyệt (browser / 브라우저) vẫn kết xuất (render / 렌더링)” không có nghĩa markup còn hợp chuẩn để author

Web phải giữ backward tính tương thích (compatibility / 호환성) với hàng chục năm nội dung cũ. Vì vậy trình duyệt (browser / 브라우저) engines vẫn có thể parse/kết xuất (render / 렌더링) nhiều obsolete elements. Điều này không biến chúng thành lựa chọn đúng cho mã (code / 코드) mới.

Khi maintain legacy hệ thống (system / 시스템), hãy phân biệt hai câu hỏi: trình duyệt (browser / 브라우저) có tính tương thích (compatibility / 호환성) hành vi (behavior / 동작) cho markup này không, và nhà phát triển (developer / 개발자) hiện đại có nên author markup này không. Câu trả lời có thể là “có kết xuất (render / 렌더링) nhưng không nên viết mới”.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **55. Presentational elements: <font>, <center>, <big> và <tt>** tiếp nhận điểm tựa từ **54. “trình duyệt (browser / 브라우저) vẫn kết xuất (render / 렌더링)” không có nghĩa markup còn hợp chuẩn để author** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. <strike> và <acronym>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Presentational elements: `<font>`, `<center>`, `<big>` và `<tt>`

Legacy HTML thường trộn cấu trúc (structure / 구조) với presentation:

```html
<center>
  <font color="red" size="5">
    Important
  </font>
</center>
```

Hiện đại (modern / 현대적) HTML chuyển responsibility về đúng tầng (layer / 계층):

```html
<p class="important">Important</p>
```

và CSS chịu font, color, alignment, kích thước (size / 크기).

`tt` từng tạo teletype/monospace presentation. Khi migrate, hãy chọn ngữ nghĩa (semantic / 의미적) replacement theo meaning: `code` cho mã nguồn (source code / 소스 코드), `kbd` cho người dùng (user / 사용자) đầu vào (input / 입력), `samp` cho program đầu ra (output / 출력), `var` cho variable; nếu chỉ muốn monospace visual thì dùng CSS.

`big` không có ngữ nghĩa (semantic / 의미적) “quan trọng”; nếu nội dung quan trọng dùng `strong`, nếu chỉ cần cỡ chữ dùng CSS.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **56. <strike> và <acronym>** tiếp nhận điểm tựa từ **55. Presentational elements: <font>, <center>, <big> và <tt>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. <marquee>, <blink>, <bgsound> và motion/audio legacy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. `<strike>` và `<acronym>`

`strike` là presentational legacy. Nếu content chỉ “không còn đúng/relevant”, `s` thường phù hợp:

```html
<s>$100</s> $70
```

Nếu bạn đang biểu diễn một edit/deletion trong document lịch sử (history / 이력), dùng `del`:

```html
<del>$100</del>
<ins>$70</ins>
```

`acronym` không còn là element nên author. Dùng `abbr` khi nội dung là abbreviation/acronym và expansion hữu ích:

```html
<abbr title="Application Programming Interface">API</abbr>
```

Di chuyển (migration / 마이그레이션) tốt không chỉ đổi tên tag; phải xác định meaning ban đầu rồi chọn ngữ nghĩa (semantic / 의미적) element mới.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **57. <marquee>, <blink>, <bgsound> và motion/audio legacy** tiếp nhận điểm tựa từ **56. <strike> và <acronym>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **58. <frameset>, <frame> và <noframes>** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. `<marquee>`, `<blink>`, `<bgsound>` và motion/audio legacy

Các elements kiểu `marquee`, `blink`, `bgsound` xuất phát từ era browser-specific/presentational HTML. Không dùng chúng trong ứng dụng (application / 애플리케이션) mới.

Nếu animation thực sự cần thiết, CSS/Web Animations/JavaScript cung cấp điều khiển (control / 제어) tốt hơn và có thể tôn trọng người dùng (user / 사용자) preference như reduced motion. Auto-playing background audio thường là UX/khả năng tiếp cận (accessibility / 접근성) anti-pattern và trình duyệt (browser / 브라우저) autoplay policies cũng hạn chế hành vi (behavior / 동작) này.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **58. <frameset>, <frame> và <noframes>** tiếp nhận điểm tựa từ **57. <marquee>, <blink>, <bgsound> và motion/audio legacy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. <applet>, <param>, <object> và plugin-era content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. `<frameset>`, `<frame>` và `<noframes>`

Legacy frames chia một trình duyệt (browser / 브라우저) cửa sổ (window / 윈도우) thành nhiều browsing contexts bằng document cấu trúc (structure / 구조) đặc biệt. Chúng gây vấn đề với URLs/lịch sử (history / 이력), khả năng tiếp cận (accessibility / 접근성), điều hướng (navigation / 내비게이션), printing và ứng dụng (application / 애플리케이션) kiến trúc (architecture / 아키텍처).

Hiện đại (modern / 현대적) page bố cục (layout / 레이아웃) dùng CSS. Nếu thực sự cần embed một independent browsing ngữ cảnh (context / 맥락), `iframe` là element tương ứng nhưng phải dùng với `title`, sandbox/permissions và bảo mật (security / 보안) rà soát (review / 검토). `iframe` không phải replacement cho bố cục (layout / 레이아웃) frameset; nó là embedding thành phần nguyên thủy (primitive / 기본 요소).

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **59. <applet>, <param>, <object> và plugin-era content** tiếp nhận điểm tựa từ **58. <frameset>, <frame> và <noframes>** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. <isindex>, <keygen>, <listing>, <xmp>, <plaintext> và các parser-era relics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. `<applet>`, `<param>`, `<object>` và plugin-era content

`applet` thuộc era Java trình duyệt (browser / 브라우저) plugins và không còn là nền tảng web hiện đại. di chuyển (migration / 마이그레이션) thường là rewrite functionality bằng HTML/CSS/JavaScript/Web APIs hoặc chuyển sang ứng dụng (application / 애플리케이션) kiến trúc (architecture / 아키텍처) khác.

`param` gắn với old plugin/đối tượng (object / 객체) parameter mechanisms và không phải lựa chọn authoring hiện đại. `object` vẫn có những embedding ngữ nghĩa (semantics / 의미론) riêng nhưng không nên được dùng để hồi sinh plugin kiến trúc (architecture / 아키텍처) cũ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **60. <isindex>, <keygen>, <listing>, <xmp>, <plaintext> và các parser-era relics** tiếp nhận điểm tựa từ **59. <applet>, <param>, <object> và plugin-era content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **61. <dir> element khác dir toàn cục (global / 전역) attribute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. `<isindex>`, `<keygen>`, `<listing>`, `<xmp>`, `<plaintext>` và các parser-era relics

Một số obsolete elements tồn tại vì lịch sử HTML rất dài. `isindex` từng đại diện đầu vào (input / 입력)/tìm kiếm (search / 검색) thành phần nguyên thủy (primitive / 기본 요소) cũ; `keygen` từng liên quan key-generation UI; `listing`, `xmp`, `plaintext` gắn với những cách xử lý văn bản (text / 텍스트)/parser rất cũ.

Khi gặp chúng trong mã (code / 코드) legacy, mục tiêu không phải học cách author lại mà là hiểu intent rồi migrate sang hiện đại (modern / 현대적) form controls hoặc `pre`/`code`/văn bản (text / 텍스트) escaping đúng ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **61. <dir> element khác dir toàn cục (global / 전역) attribute** tiếp nhận điểm tựa từ **60. <isindex>, <keygen>, <listing>, <xmp>, <plaintext> và các parser-era relics** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **62. Presentational/legacy attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. `<dir>` element khác `dir` toàn cục (global / 전역) attribute

Legacy `<dir>` element từng đại diện directory danh sách (list / 목록) và không nên dùng mới. Nhưng toàn cục (global / 전역) attribute `dir="rtl"`, `dir="ltr"`, `dir="auto"` vẫn là hiện đại (modern / 현대적), quan trọng cho bidirectional văn bản (text / 텍스트).

Đây là ví dụ điển hình cho việc cùng spelling có thể xuất hiện ở hai khái niệm lịch sử khác nhau. Đừng xóa `dir` attribute chỉ vì thấy `<dir>` element obsolete.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **62. Presentational/legacy attributes** tiếp nhận điểm tựa từ **61. <dir> element khác dir toàn cục (global / 전역) attribute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **63. Legacy JavaScript attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. Presentational/legacy attributes

Old HTML thường có attributes như `align`, `bgcolor`, `cellpadding`, `cellspacing`, `frameborder` hoặc presentational `border`. hiện đại (modern / 현대적) authoring nên chuyển presentation sang CSS.

Ví dụ legacy:

```html
<table
  border="1"
  cellpadding="8"
  cellspacing="0">
```

Hiện đại (modern / 현대적) markup giữ bảng (table / 테이블) ngữ nghĩa (semantics / 의미론) còn CSS quản lý border/padding/spacing.

Một số legacy attributes vẫn có parser tính tương thích (compatibility / 호환성) hoặc special obsolete-but-conforming exceptions vì web tính tương thích (compatibility / 호환성). Đừng dựa vào việc validator/trình duyệt (browser / 브라우저) “vẫn nhận” để quyết định authoring style.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **63. Legacy JavaScript attributes** tiếp nhận điểm tựa từ **62. Presentational/legacy attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **64. Anchor name và fragment IDs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. Legacy JavaScript attributes

HTML cũ thường có:

```html
<script
  language="javascript"
  type="text/javascript">
```

Trong hiện đại (modern / 현대적) HTML, classic JavaScript không cần `language` và thường không cần `type="text/javascript"`:

```html
<script src="/app.js"></script>
```

ES modules dùng:

```html
<script type="module" src="/main.js"></script>
```

Khi migrate, phân biệt “legacy cú pháp (syntax / 문법) bỏ được” với “mô-đun (module / 모듈) ngữ nghĩa (semantics / 의미론) khác classic script”; không xóa `type="module"` vì tưởng mọi `type` đều obsolete.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **64. Anchor name và fragment IDs** tiếp nhận điểm tựa từ **63. Legacy JavaScript attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. Legacy di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. Anchor `name` và fragment IDs

Legacy markup có thể dùng:

```html
<a name="chapter-1"></a>
```

Hiện đại (modern / 현대적) fragment mục tiêu (target / 대상) nên dùng `id` trên element có meaning:

```html
<section id="chapter-1">
  <h2>Chapter 1</h2>
</section>
```

Điều này tạo URL fragment mục tiêu (target / 대상) mà không cần empty anchor, đồng thời document ngữ nghĩa (semantics / 의미론) rõ hơn.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **65. Legacy di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **64. Anchor name và fragment IDs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. Disclosure, dialog, popover và forms** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. Legacy di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)

Đừng chạy search-replace theo tag name mà không hiểu meaning. Quy trình tốt là xác định intent cũ, tìm bản địa (native / 네이티브) hiện đại (modern / 현대적) ngữ nghĩa (semantic / 의미적), chuyển presentation sang CSS, thay plugin/frames kiến trúc (architecture / 아키텍처) nếu cần, sau đó kiểm thử (test / 테스트) DOM, keyboard, screen reader và trình duyệt (browser / 브라우저) tính tương thích (compatibility / 호환성).

Legacy markup thường có hidden coupling với JavaScript selectors hoặc máy chủ (server / 서버) templates. Vì vậy di chuyển (migration / 마이그레이션) phải có regression tests chứ không chỉ làm validator hết warning.

---

# PHẦN 16 — bản địa (native / 네이티브) HTML TRƯỚC CUSTOM JAVASCRIPT

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **66. Disclosure, dialog, popover và forms** tiếp nhận điểm tựa từ **65. Legacy di chuyển (migration / 마이그레이션) chiến lược (strategy / 전략)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **67. Parser repair** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. Disclosure, dialog, popover và forms

Nếu yêu cầu (requirement / 요구사항) chỉ là disclosure, `details/summary` có thể đủ. Nếu là modal, `dialog` thường tốt hơn generic div. Nếu là floating transient UI, Popover có thể cung cấp top-layer/light-dismiss thành phần nguyên thủy (primitive / 기본 요소). Nếu là kiểm tra hợp lệ (validation / 검증), hãy bắt đầu với `required`, kiểu (type / 타입) các ràng buộc (constraints / 제약조건들), min/max/mẫu (pattern / 패턴) trước khi replace toàn bộ bằng JavaScript.

Native-first không có nghĩa “không được custom”. Nó nghĩa bạn tận dụng hành vi (behavior / 동작)/khả năng tiếp cận (accessibility / 접근성) trình duyệt (browser / 브라우저) đã implement, rồi enhance nơi nghiệp vụ (business / 비즈니스) yêu cầu (requirement / 요구사항) thật sự vượt quá bản địa (native / 네이티브) thành phần nguyên thủy (primitive / 기본 요소).

---

# PHẦN 17 — gỡ lỗi (debug / 디버그) EXERCISES

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **67. Parser repair** tiếp nhận điểm tựa từ **66. Disclosure, dialog, popover và forms** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **68. Attribute/property state** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. Parser repair

Đưa nguồn (source / 소스) sau vào trình duyệt (browser / 브라우저) rồi so sánh View nguồn (source / 소스) với Elements:

```html
<p>
  Hello
  <div>World</div>
</p>
```

Mục tiêu là thấy nguồn (source / 소스) indentation không quyết định DOM.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **68. Attribute/property state** tiếp nhận điểm tựa từ **67. Parser repair** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. Checkbox trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. Attribute/property state
Phần này nối mạch bài học với “68. Attribute/property state”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```html
<form id="f">
  <input id="name" value="Alice">
</form>
```

Trong console, sửa `el.value = "Bob"`, rồi so sánh `el.value`, `el.defaultValue`, `el.getAttribute("value")`; cuối cùng chạy `f.reset()`. Bài này giúp hiểu trạng thái hiện tại (current state / 현재 상태), default trạng thái (state / 상태) và content attribute bằng trải nghiệm trực tiếp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **69. Checkbox trạng thái (state / 상태)** tiếp nhận điểm tựa từ **68. Attribute/property state** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **70. Form đơn vị sở hữu (owner / 오너)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. Checkbox trạng thái (state / 상태)

Với:

```html
<input id="agree" type="checkbox" checked>
```

Người dùng (user / 사용자) uncheck rồi so sánh `checked`, `defaultChecked`, `getAttribute("checked")`. Đây là một trong những ví dụ rõ nhất cho DOM quan hệ (relation / 관계).

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, sau nội dung của **69. Checkbox trạng thái (state / 상태)**, **70. Form đơn vị sở hữu (owner / 오너)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **71. DOM clobbering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. Form đơn vị sở hữu (owner / 오너)

Đặt submit button ngoài form nhưng dùng `form="profile"`, rồi quan sát trình duyệt (browser / 브라우저) vẫn submit đúng đơn vị sở hữu (owner / 오너). Sau đó thử disabled/readonly/unchecked controls và inspect `FormData` để thấy successful-controls rules.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **71. DOM clobbering** tiếp nhận điểm tựa từ **70. Form đơn vị sở hữu (owner / 오너)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. Popover và until-found** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. DOM clobbering

Tạo form có `<input name="method">` và inspect `form.method`. Mục tiêu không phải exploit, mà là thấy tại sao named truy cập (access / 접근) không nên được dùng như trusted đối tượng (object / 객체) thuộc tính (property / 속성) mô hình (model / 모델).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **72. Popover và until-found** tiếp nhận điểm tựa từ **71. DOM clobbering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **73. <colgroup> và <col>: mô tả nhóm cột, không phải header thay thế** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. Popover và until-found

Tạo một bản địa (native / 네이티브) popover rồi so sánh lượng JavaScript cần thiết với custom overlay. Sau đó tạo section `hidden="until-found"`, dùng Find in page hoặc fragment điều hướng (navigation / 내비게이션) trên trình duyệt (browser / 브라우저) hỗ trợ và quan sát trình duyệt (browser / 브라우저) reveal content.

---

# PHẦN 18 — MASTER rà soát (review / 검토) mô hình tư duy (mental model / 사고 모델)

Khi rà soát (review / 검토) môi trường vận hành (production / 운영 환경) HTML, hãy đi theo một luồng (flow / 흐름) ổn định. Trước hết kiểm tra parser/content mô hình (model / 모델): nguồn (source / 소스) sẽ tạo DOM gì, trình duyệt (browser / 브라우저) có repair không, SSR có hydration rủi ro (risk / 위험) không. Sau đó kiểm tra ngữ nghĩa (semantics / 의미론): element có biểu diễn đúng meaning không, link và button có đúng role bản địa (native / 네이티브) không, headings và landmarks có cấu trúc (structure / 구조) hợp lý không.

Tiếp theo kiểm tra khả năng tiếp cận (accessibility / 접근성): accessible name đến từ đâu, description có đúng không, keyboard thứ tự (order / 순서) có tự nhiên không, ARIA trạng thái (state / 상태) có sync visual trạng thái (state / 상태) không, custom role có đang thay bản địa (native / 네이티브) element vô lý không. Với form, xác định form đơn vị sở hữu (owner / 오너), submitter và điều khiển (control / 제어) nào thực sự được submit.

Với bảo mật (security / 보안), xác định user-controlled dữ liệu (data / 데이터) đi vào văn bản (text / 텍스트), URL, raw HTML, iframe hay script ngữ cảnh (context / 맥락); kiểm tra sandbox, referrer/CORS, sanitization/CSP chiến lược (strategy / 전략). Với hiệu năng (performance / 성능), xem trọng yếu (critical / 중요) resources được discover khi nào, LCP ảnh (image / 이미지) có intrinsic dimensions không, script có parser-blocking không và gợi ý tài nguyên (resource hints / 리소스 힌트) có được đo thực tế không.

Cuối cùng, nếu gặp markup legacy, đừng hỏi “Chrome còn kết xuất (render / 렌더링) không?” mà hỏi “meaning cũ là gì và hiện đại (modern / 현대적) ngữ nghĩa (semantic / 의미적)/CSS/API nào thay thế đúng?”.

---

# PHẦN 19 — FULL HTML nền tảng (platform / 플랫폼) mô hình tư duy (mental model / 사고 모델)

HTML nguồn (source / 소스) chỉ là điểm bắt đầu:

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

Một tag quan trọng vì nó tham gia một hoặc nhiều layers trong luồng (flow / 흐름) này. `button` không chỉ là rectangle: nó có activation, focus, khả năng tiếp cận (accessibility / 접근성) và form ngữ nghĩa (semantics / 의미론). `img` không chỉ hiển thị pixels: nó có alternative văn bản (text / 텍스트), intrinsic dimensions, tài nguyên (resource / 자원) selection và mạng (network / 네트워크) priority implications. `script` không chỉ tải (load / 로드) JavaScript: nó tương tác parser, mô-đun (module / 모듈) đồ thị (graph / 그래프), CSP/SRI và rendering đường dẫn (path / 경로).

---

# PHẦN 20 — kiểm tra (audit / 감사) HOÀN THIỆN COVERAGE CÒN THIẾU

Phần này khép những khoảng nhỏ còn lại sau khi kiểm tra (audit / 감사) toàn bộ chuẩn gốc (canonical / 정본) HTML notes theo document cấu trúc (structure / 구조), ngữ nghĩa (semantics / 의미론), siêu dữ liệu (metadata / 메타데이터), tables, forms, kiểm tra hợp lệ (validation / 검증), DOM, khả năng tiếp cận (accessibility / 접근성), hiệu năng (performance / 성능), bảo mật (security / 보안), hiện đại (modern / 현대적) HTML và legacy HTML. Các mục dưới đây không phải danh sách thuộc lòng; mục tiêu vẫn là hiểu **meaning → trình duyệt (browser / 브라우저) processing → lúc dùng → ngữ nghĩa (semantic / 의미적)/khả năng tiếp cận (accessibility / 접근성) implication**.

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **73. <colgroup> và <col>: mô tả nhóm cột, không phải header thay thế** tiếp nhận điểm tựa từ **72. Popover và until-found** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **74. Những input type dễ bị bỏ sót: submit, reset, button, image** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. `<colgroup>` và `<col>`: mô tả nhóm cột, không phải header thay thế

Trong bảng (table / 테이블), `colgroup` và `col` cho phép author mô tả hoặc style một nhóm cột mà không cần lặp lớp (class / 클래스) trên từng cell:

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

Trình duyệt (browser / 브라우저) dùng column mô hình (model / 모델) của bảng (table / 테이블) để áp dụng một số presentation/column properties phù hợp. Nhưng `col` không thay `th`: nó không tạo accessible header relationship cho dữ liệu (data / 데이터) cells. Nếu column có meaning cần screen reader hiểu, vẫn dùng `th`, `scope`, và với bảng (table / 테이블) phức tạp có thể cần `headers`/`id` association. cấp cao (senior / 시니어) rà soát (review / 검토) vì vậy phải tách **column structural grouping** khỏi **header ngữ nghĩa (semantics / 의미론)**.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **74. Những input type dễ bị bỏ sót: submit, reset, button, image** tiếp nhận điểm tựa từ **73. <colgroup> và <col>: mô tả nhóm cột, không phải header thay thế** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **75. form, novalidate, formnovalidate và accept-charset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. Những `input type` dễ bị bỏ sót: `submit`, `reset`, `button`, `image`

`<input type="submit">` tạo submit điều khiển (control / 제어) tương tự submit button nhưng label đến từ `value`. `<input type="button">` tạo generic push button nhưng không có rich child content như `<button>`. `<input type="reset">` restore default form trạng thái (state / 상태), không phải “xóa tất cả về rỗng”. Với ứng dụng (application / 애플리케이션) UI hiện đại, `<button>` thường expressive hơn vì chứa được markup và văn bản (text / 텍스트) linh hoạt.

`<input type="image">` là submit điều khiển (control / 제어) dùng ảnh (image / 이미지). Nếu phải dùng, `alt` có khả năng tiếp cận (accessibility / 접근성) meaning rất quan trọng vì ảnh (image / 이미지) là label của điều khiển (control / 제어):

```html
<input
  type="image"
  src="/pay.png"
  alt="Pay now">
```

Trình duyệt (browser / 브라우저) còn có thể submit click coordinates theo form ngữ nghĩa (semantics / 의미론). Vì hành vi (behavior / 동작) khá đặc thù, đừng dùng `type="image"` chỉ để có một button đẹp; ordinary `<button>` + CSS thường rõ ràng hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **75. form, novalidate, formnovalidate và accept-charset** tiếp nhận điểm tựa từ **74. Những input type dễ bị bỏ sót: submit, reset, button, image** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **76. bản địa (native / 네이티브) ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) thực sự hoạt động thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 75. `form`, `novalidate`, `formnovalidate` và `accept-charset`

`form="id"` cho phép một form-associated điều khiển (control / 제어) thuộc form ngay cả khi nó không nằm trong subtree form đó. trình duyệt (browser / 브라우저) resolve ID tới form đơn vị sở hữu (owner / 오너), vì vậy visual bố cục (layout / 레이아웃) và form quyền sở hữu (ownership / 소유권) không nhất thiết trùng nhau.

`novalidate` trên `<form>` tắt interactive ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) của trình duyệt (browser / 브라우저) cho submission đó:

```html
<form action="/save" method="post" novalidate>
```

`formnovalidate` trên submitter cho phép bỏ kiểm tra hợp lệ (validation / 검증) chỉ với một hành động (action / 동작), ví dụ “Save draft” trong khi “Publish” vẫn validate:

```html
<button type="submit">Publish</button>
<button type="submit" formnovalidate>Save draft</button>
```

Hai attributes này không có nghĩa máy chủ (server / 서버) được bỏ kiểm tra hợp lệ (validation / 검증). Chúng chỉ thay đổi browser-side constraint-validation step.

`accept-charset` mô tả encoding dùng cho form submission. Trong hiện đại (modern / 현대적) HTML, UTF-8 là encoding cần nghĩ tới; đừng xây kiến trúc (architecture / 아키텍처) phụ thuộc legacy encodings nếu không có đặc tả hợp đồng (contract / 계약) bắt buộc.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **76. bản địa (native / 네이티브) ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) thực sự hoạt động thế nào?** tiếp nhận điểm tựa từ **75. form, novalidate, formnovalidate và accept-charset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **77. accept, list, size, placeholder: hint, association và presentation khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 76. bản địa (native / 네이티브) ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) thực sự hoạt động thế nào?

Các attributes như `required`, `type="email"`, `min`, `max`, `step`, `pattern`, `minlength` và `maxlength` tham gia **ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) mô hình (model / 모델)**. trình duyệt (browser / 브라우저) không chỉ “đọc attribute rồi đổi viền đỏ”; điều khiển (control / 제어) có live validity trạng thái (state / 상태) trong DOM.

Ví dụ:

```js
const email = document.querySelector('#email');

email.checkValidity();
email.reportValidity();
console.log(email.validity);
console.log(email.validationMessage);
```

`checkValidity()` kiểm tra và trả boolean; `reportValidity()` còn có thể yêu cầu trình duyệt (browser / 브라우저) present kiểm tra hợp lệ (validation / 검증) UI. `ValidityState` cho biết lý do như `valueMissing`, `typeMismatch`, `patternMismatch`, `tooLong`, `rangeUnderflow` hoặc `stepMismatch` tùy điều khiển (control / 제어).

Custom quy tắc (rule / 규칙) có thể dùng:

```js
email.setCustomValidity('Email is already registered');
```

Nhưng khi lỗi đã hết phải reset bằng empty string, nếu không điều khiển (control / 제어) sẽ tiếp tục invalid. Accessibility-wise, bản địa (native / 네이티브) kiểm tra hợp lệ (validation / 검증) message không thay thế yêu cầu (requirement / 요구사항) làm lỗi (error / 오류) trạng thái (state / 상태) rõ, associate helper/lỗi (error / 오류) văn bản (text / 텍스트) phù hợp và bảo đảm keyboard/screen-reader người dùng (user / 사용자) hiểu lỗi. Server-side kiểm tra hợp lệ (validation / 검증) vẫn là authority cuối cùng.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **77. accept, list, size, placeholder: hint, association và presentation khác nhau** tiếp nhận điểm tựa từ **76. bản địa (native / 네이티브) ràng buộc (constraint / 제약조건) kiểm tra hợp lệ (validation / 검증) thực sự hoạt động thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **78. accesskey, autocapitalize và autocorrect** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 77. `accept`, `list`, `size`, `placeholder`: hint, association và presentation khác nhau

`accept` trên tệp (file / 파일) đầu vào (input / 입력) là hint cho tệp (file / 파일) picker về MIME kiểu (type / 타입)/extension mong muốn:

```html
<input
  type="file"
  accept="image/png,image/jpeg">
```

Trình duyệt (browser / 브라우저) có thể lọc picker UI, nhưng attacker vẫn có thể gửi tệp (file / 파일) khác bằng yêu cầu (request / 요청) thủ công, nên máy chủ (server / 서버) phải inspect content/kiểu (type / 타입)/kích thước (size / 크기) độc lập.

`list="id"` nối đầu vào (input / 입력) với `datalist` để trình duyệt (browser / 브라우저) cung cấp suggestions. Nó không biến đầu vào (input / 입력) thành closed enum; người dùng (user / 사용자) vẫn có thể nhập giá trị (value / 값) khác nếu kiểm tra hợp lệ (validation / 검증) không cấm.

`size` ảnh hưởng kích thước hiển thị ở một số văn bản (text / 텍스트)/select controls nhưng không giới hạn độ dài dữ liệu; `maxlength` mới liên quan length ràng buộc (constraint / 제약조건). `placeholder` là hint ngắn, không phải label. Các attributes trông giống “UI cấu hình (config / 설정)”, nhưng mỗi cái tác động một tầng (layer / 계층) khác nên không được dùng thay thế lẫn nhau.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **78. accesskey, autocapitalize và autocorrect** tiếp nhận điểm tựa từ **77. accept, list, size, placeholder: hint, association và presentation khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **79. loading="lazy" trên iframe và trách nhiệm khả năng tiếp cận (accessibility / 접근성) vẫn còn nguyên** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 78. `accesskey`, `autocapitalize` và `autocorrect`

`accesskey` có thể gán shortcut activation/focus, nhưng actual key combination phụ thuộc trình duyệt (browser / 브라우저) và operating hệ thống (system / 시스템). Shortcut tự chọn còn có thể xung đột (conflict / 충돌) với trình duyệt (browser / 브라우저), assistive technology hoặc người dùng (user / 사용자) conventions. Vì vậy đây không phải attribute nên rải khắp ứng dụng (application / 애플리케이션) chỉ để “hỗ trợ keyboard”. Natural tab thứ tự (order / 순서) và bản địa (native / 네이티브) controls quan trọng hơn.

`autocapitalize` và `autocorrect` là hints cho supported đầu vào (input / 입력) methods, đặc biệt mobile keyboards. Ví dụ username hoặc mã (code / 코드) trường dữ liệu (field / 필드) có thể không muốn automatic capitalization/correction, trong khi prose trường dữ liệu (field / 필드) có thể hưởng lợi. Chúng không validate content và không thay nghiệp vụ (business / 비즈니스) normalization.

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **79. loading="lazy" trên iframe và trách nhiệm khả năng tiếp cận (accessibility / 접근성) vẫn còn nguyên** tiếp nhận điểm tựa từ **78. accesskey, autocapitalize và autocorrect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **80. meta name="theme-color" và link rel="manifest"** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 79. `loading="lazy"` trên iframe và trách nhiệm khả năng tiếp cận (accessibility / 접근성) vẫn còn nguyên

Không chỉ ảnh (image / 이미지), iframe phù hợp cũng có thể dùng lazy loading để trì hoãn fetch khi nó còn xa viewport:

```html
<iframe
  src="https://example.com/embed"
  title="Interactive map"
  loading="lazy">
</iframe>
```

Trình duyệt (browser / 브라우저) quyết định scheduling dựa trên heuristics. `loading="lazy"` là hiệu năng (performance / 성능) hint, không phải guarantee chính xác thời điểm yêu cầu (request / 요청).

Lazy loading không thay ngữ nghĩa (semantic / 의미적) yêu cầu (requirement / 요구사항). Iframe vẫn cần `title` hữu ích; nếu third-party content trọng yếu (critical / 중요) cho tác vụ (task / 작업), phải kiểm thử (test / 테스트) keyboard/focus/loading states và fallback UX. Đừng lazy-load content ngay đầu viewport nếu điều đó làm người dùng (user / 사용자) chờ phần chính của page.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **80. meta name="theme-color" và link rel="manifest"** tiếp nhận điểm tựa từ **79. loading="lazy" trên iframe và trách nhiệm khả năng tiếp cận (accessibility / 접근성) vẫn còn nguyên** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **81. blocking="render": khi author chủ động đánh dấu render-blocking** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 80. `meta name="theme-color"` và `link rel="manifest"`

`theme-color` cho phép page gợi ý màu trình duyệt (browser / 브라우저) UI trong supporting environments:

```html
<meta
  name="theme-color"
  content="#ffffff">
```

Có thể dùng `media` trong relevant siêu dữ liệu (metadata / 메타데이터) scenarios để có giá trị (value / 값) phù hợp light/dark preferences. Đây là browser-chrome siêu dữ liệu (metadata / 메타데이터), không phải substitute cho CSS background hay accessible contrast trong page content.

PWA/web-app siêu dữ liệu (metadata / 메타데이터) còn có thể liên kết manifest:

```html
<link rel="manifest" href="/site.webmanifest">
```

Trình duyệt (browser / 브라우저) fetch manifest như một bên ngoài (external / 외부) tài nguyên (resource / 자원) khi tính năng (feature / 기능)/nền tảng (platform / 플랫폼) cần. Manifest chứa app-level siêu dữ liệu (metadata / 메타데이터) như name, icons, display hành vi (behavior / 동작); HTML `link` chỉ khai báo relationship. SEO không tự tốt hơn vì có manifest, và khả năng tiếp cận (accessibility / 접근성) của page vẫn phụ thuộc markup/content thực tế.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **HTML — Master hiện thực (implementation / 구현)**, **81. blocking="render": khi author chủ động đánh dấu render-blocking** tiếp nhận điểm tựa từ **80. meta name="theme-color" và link rel="manifest"** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **82. Declarative Shadow DOM 2026: không chỉ có shadowrootmode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 81. `blocking="render"`: khi author chủ động đánh dấu render-blocking

HTML hiện đại có `blocking` trên các element tài nguyên (resource / 자원) phù hợp như `link`, `script`, `style`; đơn vị từ (token / 토큰) hiện tại đáng quan tâm là `render`.

Concept:

```html
<link
  rel="stylesheet"
  href="/critical.css"
  blocking="render">
```

Attribute này tham gia trình duyệt (browser / 브라우저) rendering chuỗi xử lý (pipeline / 파이프라인), không phải mạng (network / 네트워크) priority flag chung. `blocking="render"` và `fetchpriority="high"` giải quyết hai concerns khác nhau: một cái liên quan việc thao tác (operation / 연산) nào có thể bị khối (block / 블록) chờ tài nguyên (resource / 자원), cái kia là scheduling hint cho fetch.

Không thêm `blocking="render"` bừa. Render-blocking tài nguyên (resource / 자원) kéo dài đường găng (critical path / 임계 경로) nếu tài nguyên (resource / 자원) chậm. Chỉ dùng khi bạn hiểu chính xác vì sao page phải đợi tài nguyên (resource / 자원) đó trước rendering và đã đo hiệu năng (performance / 성능).

---

> **Chuyển mạch:** Trong **HTML — Master hiện thực (implementation / 구현)**, **82. Declarative Shadow DOM 2026: không chỉ có shadowrootmode** tiếp nhận điểm tựa từ **81. blocking="render": khi author chủ động đánh dấu render-blocking** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **83. interestfor: hiểu hướng phát triển nhưng chưa coi là baseline môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 82. Declarative Shadow DOM 2026: không chỉ có `shadowrootmode`

Ngoài `shadowrootmode`, nền tảng (platform / 플랫폼) hiện còn định nghĩa thêm các attributes cho declarative shadow-root cấu hình (configuration / 구성). `shadowrootdelegatesfocus` liên quan focus delegation; `shadowrootclonable` cho biết shadow gốc (root / 루트) có thể tham gia cloning hành vi (behavior / 동작); `shadowrootserializable` liên quan việc shadow gốc (root / 루트) có thể được serialize bởi các HTML serialization APIs phù hợp; `shadowrootslotassignment` chọn named hay manual slot assignment; `shadowrootcustomelementregistry` phục vụ kiến trúc (architecture / 아키텍처) dùng custom-element registry gắn với shadow gốc (root / 루트).

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

Đây là infrastructure-level HTML. Beginner không cần dùng, nhưng cấp cao (senior / 시니어) làm Web Components/SSR phải biết chúng tác động **browser-created ShadowRoot**, không phải chỉ là arbitrary dữ liệu (data / 데이터) attributes. trình duyệt (browser / 브라우저)/tooling hỗ trợ (support / 지원) vẫn phải được kiểm tra theo mục tiêu (target / 대상) môi trường (environment / 환경), đặc biệt với options mới hơn.

---

> **Chuyển mạch:** Ở chặng này của **HTML — Master hiện thực (implementation / 구현)**, **83. interestfor: hiểu hướng phát triển nhưng chưa coi là baseline môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **82. Declarative Shadow DOM 2026: không chỉ có shadowrootmode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 83. `interestfor`: hiểu hướng phát triển nhưng chưa coi là baseline môi trường vận hành (production / 운영 환경)

Interest invoker là một hướng mới cho phép điều khiển (control / 제어) biểu diễn “interest” như hover/focus để mục tiêu (target / 대상) có thể phản ứng, thường kết hợp với `popover="hint"`. Một concept markup có thể trông như:

```html
<button interestfor="user-preview">
  Alice
</button>

<div id="user-preview" popover="hint">
  Profile preview
</div>
```

Ý tưởng nền tảng (platform / 플랫폼) là trình duyệt (browser / 브라우저) có thể giúp chuẩn hóa hover/focus-interest relationship thay vì mỗi khung phần mềm (framework / 프레임워크) tự viết timers, pointer/focus coordination và tooltip máy trạng thái (state machine / 상태 머신).

Tuy nhiên ở thời điểm kiểm tra (audit / 감사) tháng 9/2026, `interestfor`/related DOM APIs vẫn cần được xem là **experimental/limited-availability** chứ không phải năng lực (capability / 역량) mà môi trường vận hành (production / 운영 환경) mã (code / 코드) có thể assume cross-browser. Hãy dùng nó như kiến thức về hướng phát triển của nền tảng (platform / 플랫폼); nếu triển khai thực tế, feature-detect/progressive-enhance và giữ fallback ngữ nghĩa (semantics / 의미론) hoạt động được.

---

# KẾT LUẬN

HTML mastery không phải khả năng thuộc một danh sách 150 tags. Nó là khả năng giải thích **meaning → trình duyệt (browser / 브라우저) processing → use trường hợp (case / 사례) → ngữ nghĩa (semantic / 의미적) consequence → khả năng tiếp cận (accessibility / 접근성)/bảo mật (security / 보안)/hiệu năng (performance / 성능) implication** của markup quan trọng.

Khi bạn hiểu vì sao trình duyệt (browser / 브라우저) tự đóng `p`, vì sao invalid bảng (table / 테이블) markup có thể đổi DOM, vì sao `input.value` khác `getAttribute("value")`, vì sao disabled controls không submit, vì sao `role="button"` không tự tạo keyboard hành vi (behavior / 동작), vì sao Popover/Dialog nằm trong top tầng (layer / 계층), vì sao DOM clobbering tồn tại, và vì sao `<font>` vẫn có thể kết xuất (render / 렌더링) nhưng không còn là authoring practice đúng, bạn đã chuyển từ “biết HTML cú pháp (syntax / 문법)” sang **hiểu HTML nền tảng (platform / 플랫폼)**.

> **Bàn giao:** Sau **83. interestfor: hiểu hướng phát triển nhưng chưa coi là baseline môi trường vận hành (production / 운영 환경)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
