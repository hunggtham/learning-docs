# XML — Beginner
## Học XML từ con số 0: cú pháp, cấu trúc dữ liệu và cách parser thực sự hiểu tài liệu XML

Tài liệu này được viết cho người chưa có nền tảng XML. Mục tiêu không phải là giúp bạn “nhớ vài tag”, mà là giúp bạn hiểu XML đang giải quyết vấn đề gì, XML document được tổ chức ra sao, vì sao cú pháp của XML chặt chẽ hơn HTML, và một XML parser thực sự nhìn dữ liệu như thế nào. Nếu đọc hết phần này và tự làm các ví dụ đi kèm, bạn phải có thể tự viết một tài liệu XML đúng cú pháp, đọc được các file cấu hình XML trong Java hoặc hệ thống enterprise, phân biệt được lỗi cú pháp với lỗi schema, và hiểu vì sao XML vẫn tồn tại rất nhiều trong các hệ thống lớn dù JSON đã rất phổ biến.

---

## 1. XML là gì và vì sao nó tồn tại?

XML là viết tắt của **Extensible Markup Language**, tức là ngôn ngữ đánh dấu có khả năng mở rộng. Từ “markup” nghĩa là dữ liệu được bao quanh bởi các dấu hiệu cấu trúc như `<user>`, `<name>`, `<price>`. Từ “extensible” nghĩa là XML không ép bạn phải dùng một tập tag cố định. Bạn có thể tự định nghĩa vocabulary của riêng mình, miễn là toàn bộ tài liệu tuân theo quy tắc cú pháp XML.

Ví dụ sau là một XML document rất đơn giản:

```xml
<user>
  <name>Alice</name>
  <age>27</age>
</user>
```

XML chỉ biết đây là một cây có element `user`, bên trong có `name` và `age`. XML không biết `age` là tuổi con người, không biết giá trị `27` là số nguyên, và cũng không biết `name` có bắt buộc hay không. Những ý nghĩa đó phải được định nghĩa bởi application, schema, protocol hoặc business rule ở tầng khác.

Điểm này rất quan trọng. Khi học HTML, bạn có thể học rằng `<a>` là hyperlink, `<button>` là button, `<table>` là bảng. Với XML thì không có một ý nghĩa chuẩn như vậy cho `<user>` hay `<order>`. XML chỉ cung cấp **cú pháp chung để biểu diễn dữ liệu có cấu trúc**. Chính Maven định nghĩa ý nghĩa của `<groupId>`, SOAP định nghĩa ý nghĩa của `<Envelope>`, Spring định nghĩa ý nghĩa của các tag cấu hình cũ, và Android định nghĩa ý nghĩa của các tag XML trong layout.

---

## 2. XML document thực chất là một cây dữ liệu

Một XML document nên được hình dung như một cây, không nên hình dung như một chuỗi text có nhiều dấu `<` và `>`. Xét ví dụ sau:

```xml
<company>
  <employee id="E001">
    <name>Alice</name>
    <department>IT</department>
  </employee>
</company>
```

Nếu biểu diễn theo dạng cây, ta có thể hình dung như sau:

```text
Document
└── company
    └── employee
        ├── attribute id = "E001"
        ├── name
        │   └── text "Alice"
        └── department
            └── text "IT"
```

Một XML parser không chỉ “tìm text giữa hai tag”. Nó có thể tạo ra các đối tượng hoặc sự kiện tương ứng với document, element, attribute, text node, comment và processing instruction. Khi sau này bạn dùng DOM, SAX, StAX, XPath hay XSLT, tất cả đều dựa trên tư duy cây hoặc stream được sinh ra từ XML này.

Đây cũng là lý do tại sao việc parse XML bằng `split("<name>")` hay regex là sai về mặt kiến trúc. Một file XML có thể có namespace, CDATA, entity, comment, encoding khác nhau và nested element rất sâu. String slicing chỉ hoạt động với ví dụ đồ chơi, không phải với XML thực tế.

---

## 3. Root element là gì?

Một XML document đúng cú pháp phải có đúng **một document element**, thường được gọi đơn giản là root element. Ví dụ này hợp lệ:

```xml
<users>
  <user>Alice</user>
  <user>Bob</user>
</users>
```

Ở đây `users` là root element.

Ví dụ sau không hợp lệ:

```xml
<user>Alice</user>
<user>Bob</user>
```

Lý do là tài liệu có hai top-level elements. XML parser không thể coi cả hai cùng là document element.

Điều này không có nghĩa bên ngoài root hoàn toàn không được có gì. Một tài liệu vẫn có thể có XML declaration, comment, processing instruction hoặc DOCTYPE ở vị trí phù hợp. Nhưng về element tree thì chỉ có một element gốc.

---

## 4. Element là gì?

Element là thành phần cấu trúc chính của XML. Ví dụ:

```xml
<name>Alice</name>
```

Element này có start tag `<name>`, content là text `Alice`, và end tag `</name>`.

Element cũng có thể chứa các element khác:

```xml
<user>
  <name>Alice</name>
  <email>alice@example.com</email>
</user>
```

Khi đọc XML, bạn nên nghĩ rằng mỗi element là một node có tên và có thể có children. Children có thể là element khác, text hoặc các node đặc biệt khác.

Element name trong XML phân biệt chữ hoa chữ thường. Vì vậy:

```xml
<User/>
```

và:

```xml
<user/>
```

là hai tên khác nhau.

Đây là khác biệt quan trọng so với cách nhiều người quen suy nghĩ khi làm HTML.

---

## 5. Empty element và self-closing syntax

Nếu một element không có content, bạn có thể viết dạng đầy đủ:

```xml
<active></active>
```

hoặc viết dạng rút gọn:

```xml
<active/>
```

Trong XML, đây là empty-element syntax thực sự. Nó không phải chỉ là “cách formatter viết cho đẹp”.

Điểm này khác với HTML. Trong HTML, các void element như `<img>` hoặc `<br>` được quyết định bởi HTML parser và HTML specification. Việc bạn viết `<br />` trong một trang HTML thông thường không biến nó thành XML. XML và HTML có hai parsing model khác nhau.

---

## 6. XML phân biệt chữ hoa chữ thường

XML là case-sensitive. Ví dụ sau sai:

```xml
<User>
  <name>Alice</name>
</user>
```

Start tag là `User`, còn end tag là `user`. XML parser phải báo lỗi.

Bạn cũng cần hiểu rằng tên attribute cũng phân biệt hoa thường theo XML rules. Một thiết kế XML tốt nên dùng naming convention nhất quán, ví dụ toàn bộ dùng `camelCase`, hoặc toàn bộ dùng `kebab-case`, tránh trộn lẫn thiếu quy tắc.

---

## 7. Proper nesting: element phải đóng đúng thứ tự

XML không cho phép tag lồng chéo. Ví dụ đúng:

```xml
<a>
  <b>text</b>
</a>
```

Ví dụ sai:

```xml
<a>
  <b>text</a>
</b>
```

HTML browser có error recovery rất mạnh và thường cố “sửa” markup sai để vẫn render được. XML thì khác. XML parser được thiết kế để nghiêm ngặt hơn. Nếu tài liệu không well-formed, parser phải báo fatal error thay vì tự đoán cấu trúc theo kiểu browser HTML.

Điều này khiến XML thích hợp với các protocol hoặc file cấu hình nơi tính chính xác quan trọng hơn khả năng “render được dù sai”.

---

## 8. Attribute là gì?

Attribute gắn metadata hoặc giá trị bổ sung cho element.

```xml
<employee id="E001" active="true">
  Alice
</employee>
```

Ở đây `id` và `active` là attributes của element `employee`.

Trong XML, attribute value phải được đặt trong dấu nháy. Cả hai cách sau đều hợp lệ:

```xml
<user id="E001"/>
```

```xml
<user id='E001'/>
```

Cách sau đây không hợp lệ:

```xml
<user id=E001/>
```

Ngoài ra, cùng một element không được có duplicate attribute với cùng expanded name. Vì vậy:

```xml
<user id="1" id="2"/>
```

là lỗi.

---

## 9. Khi nào nên dùng element, khi nào nên dùng attribute?

Đây là câu hỏi thiết kế XML rất phổ biến. Ví dụ bạn có thể viết:

```xml
<user id="123">
  <name>Alice</name>
</user>
```

hoặc:

```xml
<user>
  <id>123</id>
  <name>Alice</name>
</user>
```

Cả hai đều đúng XML. XML specification không nói một cách luôn đúng hơn.

Trong thực tế, attribute thường phù hợp với metadata ngắn, identifier, flag, qualifier hoặc các giá trị mô tả element. Element thường phù hợp với business data, nested structure, repeating values và dữ liệu có khả năng mở rộng.

Ví dụ:

```xml
<price currency="USD">29.99</price>
```

thường đọc tự nhiên hơn việc viết cả `currency` thành một element con nếu `currency` chỉ mô tả cách hiểu giá trị `29.99`.

Ngược lại, nếu customer có nhiều địa chỉ, dùng element rõ ràng hơn:

```xml
<customer>
  <addresses>
    <address>...</address>
    <address>...</address>
  </addresses>
</customer>
```

Senior XML design không dựa trên một luật “attribute luôn tốt hơn element” hay ngược lại. Thiết kế phụ thuộc domain, schema, khả năng versioning và cách dữ liệu được query/transform.

---

## 10. Text content thực chất vẫn là character data

Xét:

```xml
<age>27</age>
```

Ở mức XML core, `27` chỉ là text. XML parser không tự biết đó là integer.

Tương tự:

```xml
<active>true</active>
```

không tự động trở thành boolean.

Kiểu dữ liệu có thể được gán ở tầng XML Schema hoặc application. Điều này rất quan trọng khi bạn làm Java binding hoặc validate XML. Nếu không có schema hoặc mapping rule, parser chỉ trả về character data.

---

## 11. Escaping: vì sao một số ký tự không được viết trực tiếp?

Ký tự `<` được XML dùng để bắt đầu markup. Vì vậy nếu bạn muốn lưu nội dung text `5 < 10`, bạn không thể viết trực tiếp:

```xml
<value>5 < 10</value>
```

Bạn phải viết:

```xml
<value>5 &lt; 10</value>
```

Tương tự, dấu `&` bắt đầu entity reference nên phải viết thành `&amp;` khi bạn thực sự muốn ký tự `&`.

XML định nghĩa sẵn năm entity quan trọng:

```text
&lt;    <
&gt;    >
&amp;   &
&quot;  "
&apos;  '
```

Ví dụ:

```xml
<company>AT&amp;T</company>
```

hoặc trong attribute:

```xml
<message text="He said &quot;Hello&quot;"/>
```

Bạn không cần encode mọi Unicode character thành entity. Nếu file là UTF‑8, bạn có thể viết tiếng Việt, tiếng Hàn, tiếng Nhật trực tiếp miễn ký tự đó hợp lệ theo XML version.

---

## 12. Numeric character references

Ngoài named entity, XML còn cho phép numeric character reference.

Decimal:

```xml
&#169;
```

Hexadecimal:

```xml
&#x00A9;
```

Cả hai biểu diễn ký tự ©.

Numeric reference hữu ích khi cần biểu diễn ký tự theo code point hoặc trong một số toolchain đặc biệt, nhưng trong UTF‑8 XML hiện đại thường không cần lạm dụng.

---

## 13. XML declaration

Bạn thường thấy đầu file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

`version="1.0"` cho biết XML version. Trong thực tế XML 1.0 là lựa chọn phổ biến nhất.

`encoding="UTF-8"` mô tả encoding của bytes trong file.

Một điểm rất quan trọng là declaration không “chuyển đổi encoding”. Nếu file thực tế được lưu bằng một encoding khác nhưng declaration ghi UTF‑8, parser có thể decode sai hoặc báo lỗi. Vì vậy encoding declaration phải phản ánh đúng bytes thực tế.

Trong hệ thống mới, UTF‑8 gần như luôn là lựa chọn tốt nhất trừ khi protocol hoặc hệ thống legacy yêu cầu khác.

---

## 14. XML declaration có bắt buộc không?

Không phải lúc nào XML declaration cũng bắt buộc. Ví dụ sau vẫn có thể là XML hợp lệ trong context UTF‑8:

```xml
<user>
  <name>Alice</name>
</user>
```

Tuy nhiên trong file cấu hình, integration file hoặc tài liệu cần trao đổi qua nhiều hệ thống, việc ghi rõ:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

giúp giảm ambiguity và làm intent rõ hơn.

---

## 15. BOM là gì và có cần không?

BOM là Byte Order Mark. Với UTF‑16, BOM từng rất quan trọng để xác định byte order. Với UTF‑8, BOM không cần thiết.

XML processor chuẩn có rules xử lý BOM, nhưng một số toolchain hoặc build system có thể có behavior riêng. Trong nhiều dự án hiện đại, `UTF‑8 without BOM` là lựa chọn đơn giản và ít rắc rối nhất, trừ khi hệ thống cụ thể yêu cầu BOM.

---

## 16. Comment

Comment XML có dạng:

```xml
<!-- This is a comment -->
```

Comment không phải business data. Parser có thể expose comment node hoặc bỏ qua tùy API/configuration.

Một lỗi tư duy thường gặp là để secret trong comment vì “không hiển thị”. Comment vẫn nằm trong file và vẫn có thể được đọc bằng text editor, log, package hoặc network capture. Không bao giờ dùng XML comment để chứa password, API key hoặc token.

Ngoài ra XML comment có restrictions riêng về chuỗi `--`, vì vậy không nên dùng comment như nơi lưu arbitrary text.

---

## 17. CDATA section

CDATA giúp viết một đoạn character data chứa nhiều `<` hoặc `&` mà không phải escape từng ký tự.

Ví dụ:

```xml
<code>
  <![CDATA[
    if (a < b && c > d) {
      return true;
    }
  ]]>
</code>
```

Điểm quan trọng là CDATA không tạo một loại dữ liệu mới. Trong nhiều data model, phần bên trong CDATA vẫn trở thành character data giống như khi bạn viết:

```xml
<text>5 &lt; 10</text>
```

so với:

```xml
<text><![CDATA[5 < 10]]></text>
```

Application thường nhận nội dung logic là `5 < 10`.

CDATA cũng không phải security feature. Nó chỉ là một cách lexical để viết text.

---

## 18. Vì sao `]]>` đặc biệt trong CDATA?

Chuỗi:

```text
]]>
```

là delimiter kết thúc CDATA section. Vì vậy bạn không thể chứa nguyên sequence này bên trong một CDATA section mà không split hoặc serialize lại.

Nếu bạn dùng XML serializer đúng chuẩn, serializer sẽ xử lý chuyện này tốt hơn việc tự nối string.

---

## 19. Processing Instruction

Processing instruction có syntax:

```xml
<?target data?>
```

Ví dụ cổ điển:

```xml
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
```

PI dùng để truyền instruction cho processor hoặc application. Nó không phải business data thông thường.

XML declaration nhìn giống PI nhưng có grammar và vị trí đặc biệt. Không nên coi `<?xml ...?>` đơn giản là một PI tên `xml`.

---

## 20. Whitespace trong XML có thực sự tồn tại không?

Có. Ví dụ:

```xml
<user>
  <name>Alice</name>
  <age>27</age>
</user>
```

Giữa các child element có newline và spaces dùng để indent. Tùy parser và data model, các khoảng trắng đó có thể xuất hiện dưới dạng text node.

Điều này dẫn tới một bug kinh điển khi dùng DOM: developer nghĩ `childNodes` chỉ chứa element, nhưng thực tế có thể có cả whitespace text nodes.

Vì vậy khi bạn muốn “lấy child elements”, hãy dùng API chọn element thay vì giả định mọi child node đều là element.

---

## 21. `xml:space`

`xml:space` truyền intent về cách whitespace nên được xử lý.

Ví dụ:

```xml
<text xml:space="preserve">
  A
    B
</text>
```

Hai giá trị phổ biến là:

```text
default
preserve
```

`preserve` nói rằng whitespace trong subtree có ý nghĩa và nên được giữ theo XML processing expectations. Điều này đặc biệt quan trọng với document-centric XML, code snippets hoặc text formatting.

---

## 22. `xml:lang`

`xml:lang` khai báo ngôn ngữ của nội dung.

```xml
<message xml:lang="ko">
  안녕하세요
</message>
```

Nó hữu ích với document processing, accessibility, transformation hoặc hệ thống đa ngôn ngữ.

---

## 23. `xml:base`

`xml:base` đặt base URI cho relative URIs trong subtree.

```xml
<catalog xml:base="https://example.com/assets/">
  <image href="a.png"/>
</catalog>
```

Application có thể resolve `a.png` thành URL tuyệt đối dựa trên base URI này.

Ở mức senior, base URI còn ảnh hưởng XSLT, URI resolution và security, vì một relative path cuối cùng có thể trỏ tới external resource.

---

## 24. `xml:id`

`xml:id` cung cấp standardized ID semantics trong XML ecosystem:

```xml
<section xml:id="intro">
  ...
</section>
```

Điều này khác với việc bạn tự đặt:

```xml
<section id="intro">
```

Vì một attribute có tên `id` không tự động có ID type ở mọi XML processing context. ID semantics có thể đến từ DTD, XSD, `xml:id` hoặc API configuration.

---

## 25. Well-formed XML là gì?

“Well-formed” nghĩa là tài liệu tuân toàn bộ cú pháp cơ bản của XML.

Những điều beginner phải nhớ gồm có một root element, tag phải đóng đúng thứ tự, tên phân biệt hoa thường, attribute value phải có quote, không có duplicate attribute, ký tự đặc biệt phải escape đúng, và document chỉ chứa các ký tự hợp lệ theo XML version.

Ví dụ sau không well-formed:

```xml
<user>
  <name>Alice</user>
</name>
```

XML parser phải báo fatal error.

---

## 26. Valid XML khác well-formed như thế nào?

Một XML document có thể well-formed nhưng không valid.

Ví dụ:

```xml
<user>
  <banana>123</banana>
</user>
```

Tài liệu này có thể hoàn toàn đúng cú pháp XML. Nhưng nếu schema quy định rằng `user` chỉ được chứa `name` và `email`, thì nó invalid theo schema.

Vì vậy hãy nhớ:

```text
well-formed = đúng cú pháp XML
valid       = đúng thêm grammar/schema áp dụng cho vocabulary đó
```

Mọi valid XML phải well-formed, nhưng well-formed XML chưa chắc valid.

---

## 27. XML Names có quy tắc riêng

Tên element hoặc attribute không phải một chuỗi tùy ý. XML có grammar dành cho Name và QName.

Trong thực tế bạn thường gặp các tên như:

```xml
<user>
<user-name>
<_internal>
<ns:user>
```

Nhưng không nên tự viết một regex ASCII đơn giản rồi nghĩ đã validate được đầy đủ XML Name. XML hỗ trợ Unicode name characters rộng hơn nhiều. Parser hoặc schema library nên đảm nhiệm phần này.

---

## 28. Mixed content

Mixed content là khi text và child elements xen kẽ nhau.

```xml
<p>
  XML is <em>extensible</em> and strict.
</p>
```

Đây là pattern rất quan trọng trong publishing, books, manuals và các document format.

Trong mixed content, whitespace và text node order có ý nghĩa lớn hơn nhiều so với data-centric XML. Nếu bạn tùy tiện pretty-print hoặc trim text, bạn có thể làm thay đổi nội dung.

---

## 29. Data-centric XML

Data-centric XML giống object/record:

```xml
<order>
  <id>123</id>
  <total>99.50</total>
</order>
```

Mỗi child element gần giống một field. Loại XML này thường dễ map sang Java object hoặc database row.

---

## 30. Document-centric XML

Document-centric XML thiên về nội dung văn bản:

```xml
<article>
  <title>XML</title>
  <p>
    XML is <em>extensible</em>.
  </p>
</article>
```

Ở đây text flow và mixed content quan trọng.

Điều này ảnh hưởng cách bạn thiết kế schema, XPath, XSLT và parser. Một serializer phù hợp với record-like XML chưa chắc xử lý document XML tốt nếu nó vô tình normalize whitespace hoặc reorder content.

---

## 31. XML khác HTML như thế nào?

XML và HTML có syntax bề ngoài giống nhau, nhưng mục tiêu và parsing model khác.

XML strict hơn: case-sensitive, proper nesting bắt buộc, attribute value phải quote, self-closing syntax có nghĩa thực sự, và parser không có HTML-style error recovery.

HTML có vocabulary và semantics do HTML Standard định nghĩa. `<button>` tự có behavior, `<a>` tự có navigation semantics. XML thì tag chỉ có meaning khi vocabulary/application định nghĩa.

Đây là lý do không nên lấy kinh nghiệm HTML rồi suy thẳng sang XML.

---

## 32. XHTML là gì?

XHTML là HTML vocabulary được biểu diễn theo XML syntax/process model trong các context tương ứng.

Ví dụ:

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
  <body>
    <br/>
  </body>
</html>
```

Một file HTML thông thường có `<br />` vẫn có thể đang được parse bằng HTML parser nếu media type là `text/html`. Dấu `/` không tự chuyển parsing mode.

---

## 33. XML khác JSON như thế nào?

JSON có mô hình object, array, number, boolean, null và string rất phù hợp với API hiện đại. XML có element, attribute, namespace, mixed content và một hệ sinh thái schema/query/transform rất mạnh.

XML phù hợp đặc biệt tốt với document formats, namespace-rich protocols, enterprise integration, transformation pipeline, SOAP, SVG và các file cấu hình lâu đời.

JSON thường nhẹ và dễ dùng hơn cho API object-oriented thông thường.

Vì vậy không nên kết luận “XML cũ nên luôn thay bằng JSON”. Câu hỏi đúng là: domain nào đang cần mixed content, namespaces, XSD/XSLT, existing enterprise contracts hoặc document-centric processing?

---

## 34. Ví dụ thực tế: Maven `pom.xml`

Một phần Maven POM có thể trông như sau:

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId>
  <artifactId>demo</artifactId>
  <version>1.0.0</version>
</project>
```

XML chỉ nói đây là một cây. Maven mới hiểu rằng `groupId`, `artifactId`, `version` có ý nghĩa trong dependency/build model.

Tư duy này giúp bạn đọc mọi XML framework: trước tiên hiểu XML syntax, sau đó tìm vocabulary semantics của framework đó.

---

## 35. Tại sao không parse XML bằng regex?

Giả sử bạn muốn lấy `<name>`. Một cách ngây thơ là tìm substring giữa `<name>` và `</name>`. Nhưng ngay lập tức sẽ gặp vấn đề với namespace:

```xml
<u:name xmlns:u="urn:user">Alice</u:name>
```

hoặc CDATA, comments, entity references, nested content và encoding.

XML là grammar có cấu trúc. Regex/string split không hiểu tree, namespace và parser rules. Hãy dùng XML parser.

---

## 36. DOM mental model

Một DOM-like parser có thể materialize toàn bộ tree thành objects:

```text
Document
Element
Attr
Text
Comment
ProcessingInstruction
```

DOM phù hợp khi document nhỏ hoặc vừa, bạn cần truy cập nhiều vị trí ngẫu nhiên, cần XPath hoặc cần sửa tree rồi serialize lại.

Ở phần Intermediate, bạn sẽ học vì sao SAX/StAX tốt hơn khi XML rất lớn.

---

## 37. Bài tập tổng hợp Beginner

Hãy đọc tài liệu sau:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<library>
  <book id="B001" available="true">
    <title>XML Fundamentals</title>
    <author>Alice</author>
    <price currency="USD">29.99</price>
  </book>
</library>
```

Bạn phải tự trả lời được rằng `library` là root element, `book` có hai attributes, `title` chứa text node, `29.99` ở mức XML core vẫn chỉ là character data, và `currency` là metadata mô tả cách hiểu price.

Nếu title cần chứa chuỗi `A < B`, bạn phải viết:

```xml
<title>A &lt; B</title>
```

Nếu bạn đổi end tag `</book>` thành `</Book>`, tài liệu sẽ không còn well-formed vì XML case-sensitive.

---

## 38. Mental model cần giữ lại sau Beginner

Sau khi học xong phần này, bạn không nên nhìn XML như một file text có tag nữa. Bạn phải nhìn nó như một representation của cây dữ liệu được sinh ra từ bytes thông qua decoding và parsing.

Flow đơn giản nhất là:

```text
bytes
→ decode theo encoding
→ XML parser
→ well-formedness checking
→ tree hoặc stream events
→ application hiểu vocabulary
```

Ở các phần sau, flow này sẽ được mở rộng thêm namespace, DTD, XSD, XPath, XSLT, security, canonicalization và signatures.

---

## 39. Những lỗi beginner phải tránh

Không nối XML bằng string nếu có serializer phù hợp. Không parse XML bằng regex. Không coi text `"27"` là integer nếu chưa có type layer. Không nghĩ CDATA là encryption. Không để secret trong comment. Không bỏ qua encoding. Không coi XML và HTML là cùng parser. Không quên rằng whitespace có thể là dữ liệu thật.

Nếu các nguyên tắc này trở thành phản xạ, bạn đã có nền tảng đúng để học XML nghiêm túc.
