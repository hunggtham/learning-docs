# XML — Senior
## XSLT, XQuery, tiến hóa lược đồ (lược đồ evolution), xử lý theo luồng, bảo mật (security), chuẩn hóa chính tắc và tích hợp doanh nghiệp

Phần này dành cho giai đoạn bạn đã hiểu cú pháp XML, không gian tên, XSD, XPath và bộ phân tích cú pháp models. Ở mức senior, việc “đọc được XML” không còn đủ. Bạn phải có khả năng thiết kế một XML contract có thể sống lâu trong hệ thống doanh nghiệp, xử lý file lớn mà không làm nổ memory, harden bộ phân tích cú pháp trước input không đáng tin, version lược đồ mà không phá bên tiêu thụ, dùng chuyển đổi/truy vấn đúng chỗ, và hiểu vì sao chuẩn hóa chính tắc hoặc chữ ký số lại phức tạp hơn việc hash raw XML văn bản.

Tư duy xuyên suốt của phần này là chuyển từ “XML như dữ liệu” sang “XML như một processing platform”.


## Quy ước thuật ngữ trong tài liệu

Tài liệu dùng tiếng Việt tự nhiên làm ngôn ngữ giải thích chính và giữ thuật ngữ gốc ở lần định nghĩa để tiện tra cứu. Các cách gọi được dùng thống nhất gồm: **tài liệu XML (XML document)**, **phần tử (element)**, **thuộc tính (attribute)**, **phần tử gốc (root element)**, **nút văn bản (text node)**, **không gian tên (namespace)**, **tiền tố (prefix)**, **tên mở rộng (expanded name)**, **bộ từ vựng (vocabulary)**, **lược đồ (schema)**, **giao thức (protocol)**, **quy tắc nghiệp vụ (business rule)**, **đúng cú pháp XML (well-formed)**, **kiểm tra tính hợp lệ (validation)**, **phân tích cú pháp (parsing)**, **bộ phân tích cú pháp (parser)**, **xử lý theo luồng (streaming)**, **luồng (stream)**, **truy vấn (query)**, **chuyển đổi (transformation)**, **ánh xạ/liên kết (binding)**, **tuần tự hóa (serialization)**, **bộ tuần tự hóa (serializer)** và **chuẩn hóa chính tắc (canonicalization/C14N)**. Sau khi đã định nghĩa ở đây, nội dung bên dưới ưu tiên cách gọi tiếng Việt để tránh lặp ngoặc tiếng Anh quá dày. Các tên chuẩn như XML, DTD, XSD, XPath, XSLT, XQuery, DOM, SAX, StAX, SOAP, WSDL, QName, PSVI, CDATA và tên API cụ thể được giữ nguyên.

---

## 1. XSLT là gì?

XSLT là viết tắt của **XSL Transformations**. Nó là ngôn ngữ dùng để transform XML/XDM input thành một output tree hoặc tuần tự hóa khác.

Ví dụ, source XML:

```xml
<book>
  <title>XML Fundamentals</title>
  <price>29.99</price>
</book>
```

Có thể được biến thành HTML bằng XSLT:

```xml
<xsl:stylesheet
  version="3.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <body>
        <h1>
          <xsl:value-of select="/book/title"/>
        </h1>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
```

XSLT không nên được học như một thứ “XML có if và for”. Mental model đúng là: source tree đi vào processor, processor chọn template dựa trên pattern, template dùng XPath để đọc dữ liệu, rồi xây result tree.

---

## 2. `xsl:template` và template dispatch

Một template:

```xml
<xsl:template match="book">
  ...
</xsl:template>
```

nói rằng khi processor cần xử lý một nút phù hợp với pattern `book`, template này có thể được áp dụng.

Khác với Java nơi bạn thường gọi method trực tiếp, XSLT có thể vận hành theo kiểu dispatch dựa trên pattern. Đây là một điểm mạnh vì stylesheet có thể được modular hóa theo nút type hoặc concern.

Ví dụ:

```xml
<xsl:template match="title">
  <h2>
    <xsl:apply-templates/>
  </h2>
</xsl:template>
```

Template này không cần biết title đến từ book nào. Nó chỉ biết cách biến một `title` thành `h2`.

---

## 3. `xsl:apply-templates`

`xsl:apply-templates` là idiom cốt lõi:

```xml
<xsl:apply-templates select="book"/>
```

Nó không có nghĩa “loop qua book rồi chạy block này” một cách imperative. Nó nói rằng processor hãy chọn các `book` rồi dispatch từng nút qua template phù hợp.

Cách nghĩ template-driven giúp stylesheet lớn có cấu trúc tốt hơn:

```text
match root
→ apply section templates
→ each section template delegates children
→ specialized templates override details
```

Nếu bạn dùng `xsl:for-each` cho mọi thứ, XSLT dễ biến thành imperative code khó maintain.

---

## 4. `xsl:value-of`

```xml
<xsl:value-of select="title"/>
```

lấy value theo XPath expression rồi output nó theo semantics của XSLT version.

Đừng dùng `value-of` như mặc định cho mọi lồng nhau content. Nếu source có nội dung hỗn hợp:

```xml
<p>Hello <em>world</em>!</p>
```

và bạn muốn preserve markup semantics, `apply-templates` thường phù hợp hơn việc chỉ lấy string value.

---

## 5. `xsl:for-each`

```xml
<xsl:for-each select="book">
  <p>
    <xsl:value-of select="title"/>
  </p>
</xsl:for-each>
```

`for-each` hoàn toàn hợp lệ và useful. Nhưng senior cần biết khi nào nó làm stylesheet trở nên procedural quá mức.

Nếu same nút cần nhiều kết xuất (rendering) modes hoặc override hành vi theo type, template dispatch thường flexible hơn.

---

## 6. Conditions

`xsl:if`:

```xml
<xsl:if test="@active = 'true'">
  <status>ACTIVE</status>
</xsl:if>
```

`xsl:choose`:

```xml
<xsl:choose>
  <xsl:when test="price gt 100">
    <category>expensive</category>
  </xsl:when>

  <xsl:otherwise>
    <category>normal</category>
  </xsl:otherwise>
</xsl:choose>
```

XSLT conditions dùng XPath expressions. Vì vậy hiểu XPath type model và sequence semantics rất quan trọng khi stylesheet phức tạp.

---

## 7. Variables trong XSLT

```xml
<xsl:variable
  name="total"
  select="sum(item/price)"/>
```

Đừng nghĩ variable trong XSLT giống mutable variable trong Java. XSLT thiên functional/declarative. Một ánh xạ/liên kết thường biểu diễn một value, không phải một ô nhớ bạn mutate theo loop.

Tư duy immutable ánh xạ/liên kết giúp chuyển đổi dễ reason hơn và phù hợp xử lý theo luồng/parallel optimization hơn.

---

## 8. Modes

Modes cho phép cùng source nút được xử lý khác nhau tùy concern.

Ví dụ cùng một `book` có thể cần:

```text
summary mode
detail mode
search-index mode
print mode
```

Bạn có thể thiết kế:

```xml
<xsl:apply-templates
  select="book"
  mode="summary"/>
```

và có template:

```xml
<xsl:template
  match="book"
  mode="summary">
  ...
</xsl:template>
```

Modes là một trong những công cụ quan trọng để chia một stylesheet lớn thành các processing pipelines rõ ràng.

---

## 9. XSLT hiện đại không dừng ở version 1.0

Nhiều developer chỉ từng gặp XSLT 1.0 trong hệ thống hệ thống cũ nên nghĩ XSLT là một ngôn ngữ cũ, yếu và khó dùng. XSLT 2.0/3.0 cùng XPath hiện đại có hệ kiểu, functions, grouping, packages, maps, arrays và xử lý theo luồng features mạnh hơn rất nhiều.

Điểm quan trọng không phải bạn phải dùng XSLT 3.0 ở mọi nơi, mà là khi review một system, bạn phải biết processor đang support version nào. Syntax và capability có thể khác rất xa.

---

## 10. XSLT xử lý theo luồng

Nếu source XML là 20 GB, việc build toàn tree trước chuyển đổi có thể không khả thi. XSLT 3.0 có các streaming-oriented capabilities giúp processor xử lý dữ liệu theo luồng trong những constraints nhất định.

Streaming stylesheet không thể tùy ý “quay lại ancestor xa”, truy vấn toàn descendants tương lai hoặc sort toàn dataset mà không buffer, vì processor chưa thấy toàn data.

Senior phải hiểu rằng xử lý theo luồng không chỉ là bật một cờ. Transformation logic phải **streamable**.

---

# XQuery

## 11. XQuery là gì?

XQuery là ngôn ngữ truy vấn đầy đủ cho XML/XDM. Nếu XPath là expression language, XQuery bổ sung cấu trúc để truy vấn, filter, join, sort, group và construct result.

Ví dụ:

```xquery
for $book in doc("books.xml")/library/book
where xs:decimal($book/price) > 20
order by $book/title
return
  <result>
    {$book/title}
  </result>
```

XQuery rất phù hợp với XML-native databases hoặc hệ thống cần truy vấn collections of XML documents.

---

## 12. FLWOR

FLWOR thường được đọc như:

```text
For
Let
Where
Order by
Return
```

Ví dụ:

```xquery
for $b in /library/book
let $p := xs:decimal($b/price)
where $p > 20
order by $p descending
return $b/title
```

Đây là một chuỗi xử lý declarative. Modern XQuery có thêm nhiều clauses nhưng FLWOR là mental model cơ bản.

---

## 13. XPath và XQuery khác nhau ở đâu?

XPath thường được embed vào XSLT, Java API, lược đồ assertions hoặc tools để select/calculate.

XQuery là một full language có thể tạo output mới, define functions và implement truy vấn logic lớn.

Nếu chỉ cần lấy `/order/item/price`, XPath là đủ. Nếu cần join hai collections, aggregate, sort rồi construct report XML, XQuery phù hợp hơn.

---

# XDM và XPath nâng cao

## 14. XDM là gì?

XDM là **XQuery and XPath Data Model**. Đây là mô hình dữ liệu nền của XPath/XQuery/XSLT hiện đại.

XDM không chỉ có XML các nút. Nó còn có atomic values, sequences và trong 3.1 còn có function items, maps và arrays.

Ví dụ XPath expression:

```xpath
(1, 2, 3)
```

trả về một sequence ba atomic values.

Điều này rất khác mental model XPath 1.0 kiểu “mọi thứ là nút set, string, number hoặc boolean”.

---

## 15. Sequence

Sequence là ordered sequence of items.

Một expression có thể trả:

```text
zero items
one item
many items
```

Item có thể là nút hoặc atomic value.

Không phải sequence nào cũng là list đối tượng như Java, nhưng mental model “ordered result of items” là đúng.

---

## 16. XPath axes

XPath có nhiều axes để di chuyển trong tree:

```text
child
parent
self
ancestor
ancestor-or-self
descendant
descendant-or-self
following-sibling
preceding-sibling
following
preceding
attribute
```

Ví dụ:

```xpath
ancestor::section
```

chọn ancestor section.

```xpath
following-sibling::item[1]
```

chọn next item sibling.

Axes giúp truy vấn rõ ràng và precise hơn việc dùng `//` rồi filter rộng.

---

## 17. Namespace-safe XPath

Đây là quy tắc senior phải coi như phản xạ.

Input A:

```xml
<a:order xmlns:a="urn:order"/>
```

Input B:

```xml
<o:order xmlns:o="urn:order"/>
```

Hai input cùng semantics.

XPath ứng dụng nên bind một tiền tố riêng:

```text
ord → urn:order
```

sau đó truy vấn:

```xpath
/ord:order
```

Không bao giờ coi tiền tố source là identity.

---

# Thiết kế lược đồ (Schema Design) và tiến hóa hợp đồng dữ liệu (Contract Evolution)

## 18. Namespace phải stable

Namespace URI là identity của bộ từ vựng. Đừng đổi không gian tên chỉ vì:

```text
website đổi domain
server migrate
XSD file chuyển folder
team đổi tên
```

Nếu bạn đổi không gian tên, bên tiêu thụ có thể coi toàn bộ phần tử là bộ từ vựng mới.

Namespace nên được version/govern như một API identity.

---

## 19. Version trong không gian tên

Một strategy là:

```text
urn:example:order:v1
urn:example:order:v2
```

Ưu điểm là breaking version boundary rất rõ. Consumer không thể vô tình coi v2 là v1.

Nhược điểm là mọi XPath, XSD import, ánh xạ/liên kết, bộ tuần tự hóa và thông điệp đều phải đổi không gian tên khi version đổi.

Strategy này hợp khi major versions thực sự độc lập.

---

## 20. Stable không gian tên + version thuộc tính

Một strategy khác:

```xml
<order
  xmlns="urn:example:order"
  version="2">
```

Namespace giữ ổn định, version nằm trong data.

Ưu điểm là truy vấn không gian tên và bộ từ vựng identity ít churn hơn.

Nhược điểm là ứng dụng phải có logic rõ để phân biệt version semantics, và lược đồ kiểm tra tính hợp lệ (validation)/version routing có thể phức tạp hơn.

Không có một strategy luôn đúng.

---

## 21. Backward-compatible change

Thêm optional phần tử thường dễ compatible hơn:

```xml
<xs:element
  name="memo"
  minOccurs="0"/>
```

Nếu bên tiêu thụ cũ tolerant đúng cách, nó có thể ignore trường dữ liệu mới.

Những thay đổi dễ breaking gồm rename required trường dữ liệu, đổi không gian tên, đổi type từ string sang decimal khi old values không hợp, đổi order trong strict sequence, hoặc làm optional trường dữ liệu thành required.

Schema evolution phải được treat như API evolution.

---

## 22. Extension points

XSD có ký tự đại diện:

```xml
<xs:any
  namespace="##other"
  processContents="lax"
  minOccurs="0"
  maxOccurs="unbounded"/>
```

Nó tạo nơi extension các không gian tên khác có thể cắm vào.

Điều này rất hữu ích với giao thức cần vendor extension.

Nhưng `xs:any` ở khắp nơi sẽ làm lược đồ gần như không còn ý nghĩa. Một good điểm mở rộng phải có location, không gian tên policy và kiểm tra tính hợp lệ (validation) policy rõ.

---

## 23. `processContents`

`strict`, `lax`, `skip` điều khiển ký tự đại diện processing.

`strict` yêu cầu content được validate theo quy tắc lược đồ phù hợp.

`lax` cho phép validate nếu có declaration/lược đồ phù hợp, còn nếu không có thì có thể tiếp tục.

`skip` nói không schema-validate ký tự đại diện content.

Nếu bạn dùng `skip` cho security-sensitive extension, ứng dụng vẫn phải validate dữ liệu nghiệp vụ ở layer khác.

---

## 24. Identity constraints

XSD có `xs:unique`, `xs:key`, `xs:keyref`.

Chúng cho phép enforce một số relational-like constraints trong tài liệu.

Ví dụ một list customer có ID unique, rồi order reference customer bằng keyref.

Điều này hữu ích khi tài liệu XML là một self-contained dataset có internal references.

---

## 25. `xs:unique`

`xs:unique` bảo đảm values được chọn bởi selector/trường dữ liệu không trùng lặp theo lược đồ semantics.

Nó thích hợp với business condition kiểu “mọi SKU trong list phải unique”.

---

## 26. `xs:key`

`xs:key` giống key constraint với semantics chặt hơn về presence/value theo XSD các quy tắc.

Nó có thể được reference bởi `xs:keyref`.

---

## 27. `xs:keyref`

`xs:keyref` cho phép một trường dữ liệu trỏ tới key được định nghĩa.

Ví dụ:

```text
order/customerRef
```

phải match một customer ID tồn tại trong tài liệu.

Đây là integrity constraint ở lược đồ layer.

---

## 28. Complex type derivation

XSD có extension và restriction.

Ví dụ một `EmployeeType` có thể extend `PersonType`.

```xml
<xs:complexContent>
  <xs:extension base="PersonType">
    ...
  </xs:extension>
</xs:complexContent>
```

Giống OO inheritance, type derivation mạnh nhưng có thể bị lạm dụng.

Một lược đồ inheritance tree sâu làm bên tiêu thụ khó hiểu và code generation khó maintain. Composition thường dễ reason hơn nếu domain không thực sự cần polymorphism.

---

## 29. `xsi:type`

Instance có thể chọn derived type:

```xml
<person
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:type="EmployeeType">
```

nếu lược đồ cho phép.

`xsi:type` hữu ích nhưng làm instance tài liệu gắn chặt hơn với lược đồ hệ kiểu. Nếu contract cần simple khả năng liên vận, explicit các phần tử đôi khi dễ hơn.

---

## 30. Substitution groups

Substitution group cho phép phần tử declarations thay thế một head phần tử theo quy tắc lược đồ.

Nó hỗ trợ polymorphic XML bộ từ vựng.

Nhưng khi kết hợp với derived types và `xsi:type`, lược đồ có thể rất khó đọc. Senior phải cân bằng flexibility với maintainability.

---

## 31. Nil, empty và missing

Xét ba trường hợp:

```xml
<name xsi:nil="true"/>
```

```xml
<name></name>
```

và không có `name`.

Ba trạng thái có thể tương ứng với:

```text
explicit null
empty string
not provided
```

Nếu Java ánh xạ/liên kết map cả ba thành `null` hoặc `""`, business semantics có thể bị mất.

Contract phải định nghĩa rõ điều này.

---

# Ánh xạ XML (XML Binding) và Java

## 32. XML đối tượng ánh xạ/liên kết là convenience layer, không phải XML replacement

Framework như JAXB/Jakarta Ánh xạ XML (XML Binding) có thể map:

```xml
<user>
  <name>Alice</name>
</user>
```

thành:

```java
class User {
    String name;
}
```

Đây là developer-friendly abstraction.

Nhưng XML có nhiều concepts OO model không biểu diễn tự nhiên: nội dung hỗn hợp, thuộc tính vs phần tử, không gian tên, order, unknown extensions, substitution groups, nil-vs-missing.

Nếu integration phức tạp, đừng để được sinh tự động classes che mất contract semantics.

---

## 33. Contract-first vs object-first ở mức senior

Trong tích hợp doanh nghiệp, một lược đồ được nhiều Java/.NET/vendor systems dùng thường nên được thiết kế như một language-neutral contract.

Nếu generate XSD trực tiếp từ Java class, lược đồ dễ mang theo những quyết định nội bộ của Java model như inheritance, collection wrapper hoặc naming conventions mà partner không cần biết.

Vì vậy contract-first thường phù hợp với long-lived cross-system XML interfaces.

---

# XML dung lượng lớn (Large XML) và Streaming

## 34. Vì sao DOM có thể rất tốn memory?

Raw XML 500 MB không có nghĩa DOM chỉ dùng 500 MB RAM.

Một DOM tree cần đối tượng cho mỗi phần tử, nút văn bản, thuộc tính, không gian tên ánh xạ/liên kết và collections/pointers. Memory footprint có thể tăng nhiều lần so với source.

Vì vậy large XML phải được benchmark bằng actual bộ phân tích cú pháp, không estimate từ file size.

---

## 35. Streaming Parser Pattern

Với record-oriented XML:

```xml
<records>
  <record>...</record>
  <record>...</record>
</records>
```

StAX chuỗi xử lý có thể:

```text
đọc tới <record>
→ parse fields
→ tạo domain object
→ process/write DB
→ discard object
→ đọc record tiếp theo
```

Memory gần như phụ thuộc size của một record thay vì size toàn file.

---

## 36. Partial Materialization

Bạn không bắt buộc phải luồng từng primitive trường dữ liệu bằng tay.

Một pattern tốt là luồng outer tài liệu, rồi khi tới một `<record>`, materialize riêng subtree đó thành đối tượng hoặc mini-DOM, xử lý xong rồi discard.

Flow:

```text
StAX outer loop
→ capture one record
→ JAXB/DOM record
→ business process
→ release
```

Đây là compromise rất practical.

---

## 37. Streaming không giải quyết mọi memory problem

Nếu requirement nói “mọi customer ID phải unique toàn file”, bạn vẫn cần state như HashSet hoặc external database.

Nếu cần sort toàn bộ record, bạn phải buffer hoặc dùng external sort.

Streaming chỉ giúp không giữ toàn tree. Nó không loại requirement lưu state toàn cục.

---

# Bảo mật (Security)

## 38. Vì sao XML có bảo mật (security) surface lớn?

XML processor lịch sử có nhiều capability:

```text
DTD
general entities
parameter entities
external system identifiers
schema import/include
XInclude
XSLT URI loading
extension functions
```

Các capability này rất hữu ích với trusted documents, nhưng nguy hiểm với attacker-controlled XML.

Senior phải coi bộ phân tích cú pháp như một component có filesystem/network capabilities cần được sandbox/harden.

---

## 39. XXE là gì?

XXE là XML External Entity attack.

Concept:

```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>

<data>&xxe;</data>
```

Nếu bộ phân tích cú pháp resolve thực thể `xxe`, nó có thể đọc local file và đưa content vào parsed data.

Trên server, attack có thể nhắm:

```text
local file disclosure
SSRF
internal service access
cloud metadata endpoints
denial of service
```

Không phải mọi bộ phân tích cú pháp mặc định vulnerable, nhưng bạn không được dựa vào assumption. Hãy configure theo bộ phân tích cú pháp/version thật.

---

## 40. External DTD và SSRF

Ngay cả không dùng thực thể trực tiếp, DOCTYPE:

```xml
<!DOCTYPE root SYSTEM
  "http://internal-service/private.dtd">
```

có thể khiến bộ phân tích cú pháp gửi network request nếu external subset resolution enabled.

Đó là SSRF-style hành vi.

---

## 41. Parameter các thực thể

DTD còn có parameter các thực thể, thường dùng bên trong DTD grammar.

External parameter thực thể cũng có thể trigger quá trình tải tài nguyên (resource loading).

Vì vậy gia cố bảo mật chỉ “disable external general các thực thể” nhưng bỏ parameter các thực thể vẫn có thể chưa đủ.

---

## 42. Billion Laughs

Billion Laughs tận dụng recursive/lồng nhau thực thể expansion.

Concept đơn giản:

```text
entity A = "lol"
entity B = A repeated many times
entity C = B repeated many times
...
```

Source rất nhỏ nhưng expanded văn bản có thể cực lớn, gây CPU/memory exhaustion.

Modern parsers thường có limits, nhưng ứng dụng nên chủ động có resource limits.

---

## 43. XInclude

XInclude cho phép include external XML/resource:

```xml
<xi:include
  xmlns:xi="http://www.w3.org/2001/XInclude"
  href="other.xml"/>
```

Nếu input untrusted và XInclude enabled, attacker có thể influence tài nguyên bên ngoài access.

Nếu ứng dụng không cần XInclude, disable nó.

---

## 44. Schema resolution cũng là external access

XSD có imports/includes. Instance có `schemaLocation`. Nếu validator tự fetch remote các lược đồ, attacker hoặc network dependency có thể ảnh hưởng hành vi.

Một production system tốt nên dùng trusted local lược đồ registry hoặc bộ phân giải.

---

## 45. XML Catalog

XML Catalog là cơ chế ánh xạ external các định danh/URIs tới local resources.

Ví dụ concept:

```text
https://vendor.com/schema/order.xsd
→ /opt/app/schema/vendor-order-v3.xsd
```

Benefits gồm deterministic builds, offline processing, giảm latency và giảm arbitrary network fetch.

Trong doanh nghiệp XML infrastructure, Catalog là tool rất giá trị.

---

## 46. Secure bộ phân tích cú pháp strategy

Với untrusted XML, default mental checklist là: tắt DTD nếu không cần; tắt external general các thực thể; tắt external parameter các thực thể; block external DTD/lược đồ resolution; tắt XInclude nếu không cần; giới hạn tài liệu size/depth/thực thể expansions; dùng secure processing options; và kiểm soát mọi URI bộ phân giải.

Exact cờ khác nhau giữa `DocumentBuilderFactory`, `SAXParserFactory`, `XMLInputFactory`, `SchemaFactory` và `TransformerFactory`.

Điều này có nghĩa không tồn tại một config snippet universal cho mọi Java XML API.

---

## 47. Hardening một bộ phân tích cú pháp không harden toàn chuỗi xử lý

Bạn có thể đã secure DOM bộ phân tích cú pháp nhưng sau đó XSLT `TransformerFactory` vẫn được phép `document()` tới external URI.

Hoặc `SchemaFactory` vẫn fetch imports.

Hoặc untrusted stylesheet dùng extension function.

Senior phải threat-model từng component:

```text
parser
validator
XPath/XQuery engine
XSLT engine
serializer
signature verifier
```

---

## 48. XSLT bảo mật (security)

XSLT có thể include/import stylesheets và trong một số processor có khả năng access external documents hoặc extension functions.

Do đó “untrusted XML” và “untrusted XSLT” là hai threat models khác nhau.

Không execute stylesheet do user upload với unrestricted server-side processor nếu không có sandbox/policy.

---

## 49. XPath Injection

Nếu code build expression:

```java
String xpath =
    "/users/user[name='" + input + "']";
```

thì input chứa quotes hoặc XPath syntax có thể thay đổi truy vấn.

Concept giống SQL Injection.

Defense là dùng variable ánh xạ/liên kết nếu engine hỗ trợ, không cho user cung cấp arbitrary expression fragments, hoặc validate input theo allowlist rõ ràng.

---

# Canonicalization và XML Signature

## 50. Vì sao không thể hash raw XML văn bản một cách ngây thơ?

Hai serializations:

```xml
<user id="1" active="true"/>
```

và:

```xml
<user active="true" id="1"></user>
```

có thể mang cùng information theo XML mô hình dữ liệu nhưng raw bytes khác.

Nếu signature phụ thuộc raw formatting, chỉ cần bộ định dạng đổi thuộc tính order hoặc empty phần tử notation là hash fail.

Canonical XML giải quyết bằng cách tạo representation deterministic theo algorithm chuẩn.

---

## 51. Canonicalization không phải pretty-print

Pretty-print làm XML dễ đọc bằng indentation.

Canonicalization chuẩn hóa những lexical differences theo đặc tả để phục vụ comparison/signature.

Không thể thay C14N bằng:

```text
trim spaces
sort attributes
normalize quotes
```

tự viết.

---

## 52. XML Digital Signature

XML Signature có thể sign whole tài liệu hoặc một phần tài liệu.

Signature thường chứa references, transforms, digest và signature value.

Điểm quan trọng là “signature valid” không có nghĩa toàn bộ tài liệu XML được business ứng dụng tin tưởng. Nó chỉ chứng minh references đã verify theo signature semantics và trusted key.

Application phải hiểu signed scope.

---

## 53. Signature Wrapping Attack

Một attack class quan trọng là tấn công bọc chữ ký.

Concept:

```text
signed element A hợp lệ
attacker thêm element B
signature verifier xác nhận A
business code query nhầm B
```

Ví dụ verifier verify phần tử có ID `signed-order`, nhưng ứng dụng sau đó chạy:

```java
getElementsByTagName("Order").item(0)
```

và nhận một attacker-controlled `Order` khác.

Defense là ứng dụng phải process **exact nút đã được signature verifier xác nhận**, không verify xong rồi truy vấn tài liệu một lần nữa bằng selector mơ hồ.

---

## 54. ID semantics và signature

Reference kiểu:

```text
#order123
```

cần processor biết thuộc tính nào là ID.

ID semantics có thể đến từ DTD, XSD, `xml:id` hoặc API/library cấu hình.

Một thuộc tính tên `id` không tự động có ID semantics trong mọi XML API.

Đây là một chi tiết nhỏ nhưng cực kỳ quan trọng với XML Signature bảo mật (security).

---

# Kiến trúc tích hợp (Integration Architecture)

## 55. Boundary Validation Pattern

Một inbound chuỗi xử lý tốt có thể là:

```text
network/file bytes
→ max-size check
→ secure parser
→ schema validation
→ normalized/canonical internal representation
→ domain mapping
→ business validation
→ authorization
```

Mỗi stage giải quyết một vấn đề riêng.

XSD không thay authorization. Parser bảo mật (security) không thay business kiểm tra tính hợp lệ (validation). Mapping không thay lược đồ kiểm tra tính hợp lệ (validation).

---

## 56. Schema compilation cache

XSD compilation có cost. Nếu mỗi request đều đọc XSD từ disk, resolve imports và compile lại, latency và CPU sẽ tăng.

Pattern tốt:

```text
load trusted schemas at startup
→ compile
→ cache compiled schema
→ create validator instances theo library contract
```

Tương tự, XSLT stylesheet có thể được compile/cache nếu processor API cho phép.

---

## 57. Strict Reader vs Tolerant Reader

Strict reader reject trường dữ liệu lạ.

Ưu điểm là contract predictable và bảo mật (security) dễ reason.

Nhược điểm là forward khả năng tương thích thấp.

Tolerant reader cho phép unknown optional extensions.

Ưu điểm là tiến hóa lược đồ (lược đồ evolution) tốt hơn.

Nhược điểm là bên tiêu thụ có thể silently ignore semantic quan trọng.

Một senior contract phải nói rõ unknown phần tử policy, thay vì để hành vi bộ phân tích cú pháp quyết định ngẫu nhiên.

---

## 58. “Be liberal in what you accept” không phải lúc nào tốt

Postel's Law từng rất phổ biến trong giao thức design, nhưng với security-critical contracts, quá tolerant có thể che lỗi hoặc bypass kiểm tra tính hợp lệ (validation).

Một strategy hiện đại hơn là:

```text
strict core
explicit versioning
explicit extension points
known tolerance policy
```

---

## 59. Envelope Pattern

Nhiều XML các giao thức dùng envelope:

```xml
<message>
  <header>
    ...
  </header>

  <body>
    ...
  </body>
</message>
```

Header chứa cross-cutting siêu dữ liệu (metadata) như correlation ID, routing, version, bảo mật (security) information. Body chứa business dữ liệu tải (payload).

SOAP là ví dụ nổi tiếng của pattern này.

---

## 60. Namespace Extension Pattern

Core bộ từ vựng:

```text
urn:example:order
```

Partner extension:

```text
urn:partner:custom
```

XML Namespace giúp hai bên mở rộng cùng tài liệu mà tránh collision.

Nếu lược đồ có controlled ký tự đại diện điểm mở rộng, partner có thể thêm siêu dữ liệu (metadata) mà không đổi core không gian tên.

---

## 61. Schema Registry Pattern

Một tổ chức lớn nên quản lý lược đồ giống API artifacts.

Registry/repository nên biết:

```text
schema version
owner
status
compatibility
checksum
dependencies
deprecation
release date
```

Không nên để mỗi team copy `common.xsd` khác nhau rồi tự sửa.

---

## 62. Canonical Data Model Pattern

Nếu hệ thống nhận:

```text
Partner A XML
Partner B XML
Legacy SOAP XML
```

business code không nên hiểu từng external lược đồ.

Bạn có thể transform/map tất cả thành internal canonical model.

Flow:

```text
external XML
→ adapter / XSLT / mapper
→ canonical internal model
→ business services
```

Điều này giảm coupling.

Nhưng một canonical model quá generic cho toàn doanh nghiệp có thể thành “god model”. Nên scope theo bounded ngữ cảnh/domain.

---

## 63. Anti-Corruption Layer

DDD gọi layer bảo vệ domain khỏi external model là Anti-Corruption Layer.

XML hệ thống cũ thường rất phù hợp pattern này:

```text
vendor XML
→ parser
→ validation
→ transformation
→ internal DTO/domain
```

Legacy naming, không gian tên, null semantics và lược đồ quirks dừng lại ở boundary.

---

# Quy ước thiết kế XML (XML Design Idioms)

## 64. Explicit units

Nếu number không có globally fixed unit, nên biểu diễn rõ:

```xml
<weight unit="kg">64</weight>
```

thay vì:

```xml
<weight>64</weight>
```

và để bên tiêu thụ đoán.

---

## 65. Stable các định danh

Nếu có:

```xml
<customer id="C123">
```

contract phải làm rõ ID unique ở scope nào, có phân biệt chữ hoa chữ thường không, có tái sử dụng không và tồn tại bao lâu.

Không nên chỉ nói “id là string”.

---

## 66. Wrapper collection

Bạn có thể viết:

```xml
<order>
  <items>
    <item/>
    <item/>
  </items>
</order>
```

hoặc trực tiếp:

```xml
<order>
  <item/>
  <item/>
</order>
```

Wrapper giúp collection có chỗ chứa siêu dữ liệu (metadata) như count, pagination hoặc future options. Nhưng nó làm lược đồ verbose hơn.

Chọn dựa trên khả năng evolution.

---

## 67. Discriminator thuộc tính vs distinct các phần tử

Option A:

```xml
<contact type="email">
  alice@example.com
</contact>
```

Option B:

```xml
<email>
  alice@example.com
</email>
```

Option A giúp lược đồ compact, option B làm phần tử semantics explicit hơn.

Nếu mỗi contact type có cấu trúc khác nhau, distinct các phần tử hoặc hệ kiểu thường rõ hơn discriminator string.

---

# Các phản mẫu ở mức Senior (Senior Anti-patterns)

## 68. Đổi không gian tên cho mọi minor release

Nếu `v1.1`, `v1.2`, `v1.3` đều có không gian tên mới, bên tiêu thụ phải update XPath/ánh xạ/liên kết liên tục.

Chỉ version không gian tên khi strategy thực sự yêu cầu breaking identity.

---

## 69. `xs:any` ở mọi nơi

Schema nhìn flexible nhưng không validate được gì đáng kể.

Extension phải có boundary rõ.

---

## 70. Deep inheritance tree

Schema type inheritance 7 tầng có thể làm được sinh tự động code cực khó hiểu.

Nếu composition đủ, composition thường dễ maintain hơn.

---

## 71. Monolithic XSD

Một file XSD chứa mọi domain, version và extension trở thành bottleneck governance.

Chia module theo bộ từ vựng/domain và quản lý imports rõ ràng.

---

## 72. Everything required

Nếu mọi trường dữ liệu bắt buộc, thêm feature mới gần như luôn breaking.

---

## 73. Everything optional

Nếu mọi trường dữ liệu optional, lược đồ không còn enforce business shape.

Senior phải cân bằng evolvability và correctness.

---

# Hiệu năng (hiệu năng (performance)) và khả năng quan sát (observability)

## 74. Performance limits

Production XML processing nên nghĩ tới max bytes, depth, number of các phần tử, number of các thuộc tính, max nút văn bản size, thực thể expansion limits và processing timeout.

Security và hiệu năng (performance) ở đây liên quan chặt nhau vì attacker có thể dùng XML complexity để tiêu tốn CPU/RAM.

---

## 75. Logging

Khi kiểm tra tính hợp lệ (validation) fail, log nên giúp debug:

```text
message type
namespace
schema version
correlation ID
line/column
validation path
error code
```

Nhưng không dump toàn XML nếu dữ liệu tải (payload) chứa password, PII hoặc financial data.

Một log “đủ để debug” không đồng nghĩa “log toàn dữ liệu tải (payload)”.

---

## 76. Golden tài liệu tests

Một XML contract tốt nên có sample tests cho minimum valid, full valid, old version, future extension, missing trường dữ liệu, nil trường dữ liệu, empty trường dữ liệu, wrong order, invalid type, very large dữ liệu tải (payload) và malicious XXE input.

Các fixtures này giúp regression test lược đồ, cấu hình bộ phân tích cú pháp và ánh xạ code.

---

## 77. Mental model sau Senior

Sau phần này, flow hoàn chỉnh hơn là:

```text
raw bytes
→ encoding
→ secure parser
→ well-formedness
→ namespace expansion
→ controlled DTD/schema resolution
→ schema validation
→ DOM / stream / XDM
→ XPath / XQuery / XSLT
→ canonical internal mapping
→ business validation
→ authorization
→ serialization
→ optional canonicalization/signature
```

Nếu bạn hiểu được flow này và biết mỗi stage giải quyết vấn đề gì, bạn đã vượt khỏi mức “developer biết XML” và bắt đầu xử lý XML như một senior integration engineer.

---

# PHẦN BỔ SUNG — SOAP, WSDL VÀ XML TRONG ENTERPRISE INTEGRATION

## 78. SOAP là gì và vì sao nó gắn chặt với XML?

SOAP là một **messaging framework** dùng XML để đóng gói thông điệp. Khi nói SOAP, đừng chỉ nghĩ “API trả XML thay vì JSON”. SOAP định nghĩa một processing model với envelope, header blocks, body, faults, các không gian tên và khả năng mở rộng theo modules. XML phù hợp với SOAP vì không gian tên cho phép nhiều chuẩn hoặc vendor extensions cùng xuất hiện trong một thông điệp mà không đụng tên, còn XSD cung cấp contract type/cấu trúc rất mạnh.

Một SOAP 1.2 thông điệp tối giản có thể có dạng:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<env:Envelope
    xmlns:env="http://www.w3.org/2003/05/soap-envelope"
    xmlns:o="urn:example:order">

    <env:Header>
        <o:CorrelationId>
            8a5f-1234
        </o:CorrelationId>
    </env:Header>

    <env:Body>
        <o:GetOrder>
            <o:orderId>1001</o:orderId>
        </o:GetOrder>
    </env:Body>

</env:Envelope>
```

`Envelope` là outermost SOAP phần tử. `Header` là optional và chứa zero hoặc nhiều header blocks. `Body` là nơi mang information hướng tới ultimate receiver. Business dữ liệu tải (payload) như `o:GetOrder` không thuộc SOAP không gian tên; nó thuộc bộ từ vựng `urn:example:order`. Chính sự tách không gian tên này làm SOAP extensible.

SOAP 1.1 và SOAP 1.2 có không gian tên/giao thức details khác nhau. SOAP 1.2 dùng envelope không gian tên `http://www.w3.org/2003/05/soap-envelope`; hệ thống SOAP 1.1 hệ thống cũ thường dùng `http://schemas.xmlsoap.org/soap/envelope/`. Vì vậy khi debug một SOAP integration, version không phải chi tiết nhỏ: không gian tên, HTTP ánh xạ/liên kết và fault format có thể khác.

---

## 79. SOAP Header không chỉ là chỗ đặt siêu dữ liệu (metadata) tùy ý

SOAP Header được thiết kế để mang các blocks có semantics xử lý riêng, ví dụ bảo mật (security), transaction, routing, correlation hoặc addressing. Header block có thể target một nút/intermediary cụ thể trên thông điệp path.

SOAP còn có concept `mustUnderstand`. Nếu một header block bắt buộc phải được hiểu mà nút nhận thông điệp không hiểu semantics của block đó, nút không nên im lặng bỏ qua rồi xử lý business body như bình thường; SOAP processing model có fault hành vi cho tình huống này.

Điểm này cho thấy SOAP khác một JSON đối tượng có trường dữ liệu `headers`. Header trong SOAP là một phần của processing model, không chỉ là convention do ứng dụng tự nghĩ ra.

---

## 80. SOAP Body và business dữ liệu tải (payload)

Body thường chứa application-specific XML. Ví dụ:

```xml
<env:Body>
    <pay:Transfer
        xmlns:pay="urn:bank:payment">

        <pay:from>100-001</pay:from>
        <pay:to>200-002</pay:to>
        <pay:amount>50000</pay:amount>

    </pay:Transfer>
</env:Body>
```

SOAP chỉ định envelope/body cấu trúc, còn `Transfer`, `from`, `to`, `amount` là contract của payment service. Các các phần tử business này thường được mô tả bằng XSD và được reference/import từ WSDL.

Điều đó tạo một layering rất rõ:

```text
XML syntax
→ SOAP envelope vocabulary
→ application namespace/vocabulary
→ XSD types
→ business semantics
```

Khi lỗi xảy ra, phải xác định lỗi nằm ở layer nào thay vì chỉ nhìn “SOAP request invalid”.

---

## 81. SOAP Fault

SOAP dùng `Fault` để biểu diễn lỗi theo thông điệp format chuẩn. Với SOAP 1.2, Fault có các phần như Code, Reason và optional Detail.

Ví dụ rút gọn:

```xml
<env:Envelope
    xmlns:env="http://www.w3.org/2003/05/soap-envelope">

    <env:Body>
        <env:Fault>
            <env:Code>
                <env:Value>env:Sender</env:Value>
            </env:Code>

            <env:Reason>
                <env:Text xml:lang="en">
                    Invalid order id
                </env:Text>
            </env:Reason>
        </env:Fault>
    </env:Body>

</env:Envelope>
```

Điểm senior cần hiểu là HTTP status và SOAP Fault là hai layers khác nhau. Một integration framework có thể map transport failure, SOAP giao thức fault và business lỗi theo cách khác nhau. Khi log/debug, phải giữ distinction này.

---

## 82. WSDL là gì?

WSDL là **Web Services Description Language**. Trong các SOAP systems truyền thống, WSDL đóng vai trò contract mô tả service để client/server tooling biết service cung cấp operations nào, thông điệp shape ra sao, ánh xạ/liên kết/giao thức nào được dùng và endpoint ở đâu.

Bạn có thể hình dung WSDL 1.1 theo mental model:

```text
XML Schema / types
→ messages
→ operations / portType
→ binding
→ service / endpoint
```

Trong thực tế WSDL thường import hoặc embed XSD. XSD định nghĩa business các phần tử/types; WSDL ghép chúng thành service operations và transport ánh xạ/liên kết.

Đây là lý do khi một SOAP client generate Java classes từ WSDL, bạn có thể thấy rất nhiều được sinh tự động DTOs, service interfaces và QName constants. Tooling đang biến XML contract thành programming-language artifacts.

---

## 83. Contract-first SOAP flow

Trong một hệ thống contract-first, team có thể thiết kế XSD/WSDL trước rồi generate client/server stubs.

Flow khái niệm như sau:

```text
WSDL + XSD
→ code generation
→ Java client proxy / DTO classes
→ marshal object thành XML
→ wrap trong SOAP Envelope
→ HTTP transport
→ server SOAP stack
→ parse + validate + unmarshal
→ business service
→ marshal response
→ SOAP response hoặc SOAP Fault
```

Framework che đi rất nhiều bước, nhưng khi production lỗi bạn phải có khả năng mở wire thông điệp và kiểm tra không gian tên, QName, phần tử order, `xsi:nil`, lược đồ type và SOAP version.

Một exception Java kiểu “unexpected phần tử” thường thực chất là mismatch giữa tên mở rộng trong XML và được sinh tự động ánh xạ/liên kết expectation.

---

## 84. WSDL/XSD code generation giúp nhanh nhưng có coupling

Generated classes giúp developer không phải tự viết bộ phân tích cú pháp cho mỗi SOAP thông điệp. Tuy nhiên code generation cũng làm ứng dụng coupling mạnh với contract. Khi WSDL thay không gian tên, type hierarchy hoặc required trường dữ liệu, được sinh tự động code có thể thay đổi hàng loạt.

Vì vậy long-lived doanh nghiệp service cần quản lý WSDL/XSD version như public API. Không sửa lược đồ âm thầm rồi regenerate cả hai bên nếu còn external các bên tiêu thụ.

Nếu được sinh tự động classes quá phức tạp, nên map chúng sang internal DTO/domain model ở boundary thay vì để WSDL-generated types chạy xuyên business layer.

---

## 85. SOAP, WS-* và vì sao doanh nghiệp systems vẫn dùng

SOAP thường xuất hiện trong banking, insurance, telecom, government, B2B integration và các hệ thống được xây trong thời kỳ doanh nghiệp service bus. Một lý do là ecosystem xung quanh SOAP có nhiều specifications cho concerns như bảo mật (security), addressing, reliability và transactions. Những hệ thống đã đầu tư vào WSDL/XSD governance, code generation và integration middleware không có lý do kỹ thuật để rewrite chỉ vì JSON phổ biến hơn.

Điều này không có nghĩa SOAP nên là default cho mọi API mới. Với một public/internal CRUD API đơn giản, HTTP + JSON thường nhẹ và dễ vận hành hơn. Nhưng nếu bạn maintain core banking hoặc B2B gateway, việc hiểu SOAP/WSDL/XSD là kỹ năng thực tế chứ không phải kiến thức lịch sử.

---

## 86. SOAP so với REST/JSON phải so ở đúng tầng

SOAP là messaging framework/giao thức family; REST là architectural style; JSON là data tuần tự hóa format. Vì vậy câu “SOAP hay JSON cái nào tốt hơn” đang so các khái niệm khác tầng.

Một SOAP service thường dùng XML dữ liệu tải (payload) và WSDL contract. Một REST-like HTTP API thường dùng JSON, URLs, HTTP methods/status codes và OpenAPI. Nhưng về mặt architecture, lựa chọn còn phụ thuộc governance, hệ thống cũ khả năng tương thích, bảo mật (security) requirements, tooling và partner contracts.

Senior không chọn công nghệ chỉ vì verbosity. Bạn phải đánh giá contract lifecycle và ecosystem của hệ thống.

---

## 87. Enterprise integration flow nên cô lập XML ở boundary

Nếu service nhận SOAP từ external partner, một architecture tốt thường là:

```text
SOAP transport
→ secure XML parser / SOAP framework
→ schema validation
→ generated/bound request object
→ adapter / anti-corruption layer
→ internal domain command
→ business logic
```

Response đi ngược lại qua mapper và SOAP layer.

Điểm quan trọng là business domain không nên phụ thuộc trực tiếp vào SOAP-specific types nếu không có lý do. Nếu ngày mai partner đổi SOAP version hoặc một channel mới dùng JSON, core domain không cần rewrite.

---

## 88. Debug SOAP theo layer thay vì nhìn một XML khổng lồ

Khi SOAP request fail, hãy bắt đầu từ transport: endpoint, HTTP headers/content type, TLS và authentication có đúng không. Sau đó kiểm tra SOAP version bằng envelope không gian tên. Tiếp theo kiểm tra `Envelope`, `Header`, `Body` và Fault cấu trúc. Sau đó mới đi vào business dữ liệu tải (payload) không gian tên và XSD order/type. Cuối cùng kiểm tra ánh xạ/liên kết code hoặc được sinh tự động classes.

Flow debug này giúp tránh việc sửa ngẫu nhiên tiền tố. Trong XML, tiền tố có thể khác nhưng URI của không gian tên (không gian tên URI) mới quyết định identity. Một service kỳ vọng `{urn:bank:v1}Transfer` sẽ không chấp nhận `{urn:bank:v2}Transfer` chỉ vì cả hai đều viết tiền tố `pay`.

---

## 89. SOAP bảo mật (security) vẫn bắt đầu từ XML bảo mật (security)

Dù SOAP framework xử lý envelope, XML bộ phân tích cú pháp và external resolution vẫn là phần threat surface. Ngoài ra SOAP systems còn có thể dùng message-level bảo mật (security) standards như WS-Security/XML Signature. Khi đó nhận biết không gian tên signature verification, chuẩn hóa chính tắc và verified-node ánh xạ/liên kết từ các phần trước trở nên đặc biệt quan trọng.

Không nên tự parse SOAP bằng string hoặc tự implement XML Signature. Hãy dùng framework/library đã được review, cấu hình bộ phân tích cú pháp/resource resolution chặt, rồi giữ business logic tách khỏi raw XML.

---

## 90. Mental model doanh nghiệp cuối cùng

Khi gặp một hệ thống XML doanh nghiệp, hãy nhìn nó như một chuỗi contracts và processors:

```text
transport
→ XML bytes
→ secure parse
→ namespace model
→ schema/WSDL contract
→ validation/binding
→ transformation/integration layer
→ domain model
→ business logic
```

Nếu có SOAP, SOAP envelope nằm giữa XML layer và ứng dụng dữ liệu tải (payload). Nếu có XSLT, chuyển đổi nằm ở boundary hoặc integration chuỗi xử lý. Nếu có XML Signature, chuẩn hóa chính tắc/reference verification phải xảy ra theo giao thức trước khi business code tin dữ liệu.

Đây là điểm mà toàn bộ kiến thức XML từ Beginner tới Senior kết nối lại thành một hệ thống duy nhất.
