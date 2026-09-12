# XML — Senior
## XSLT, XQuery, schema evolution, streaming, security, canonicalization và enterprise integration

Phần này dành cho giai đoạn bạn đã hiểu cú pháp XML, namespace, XSD, XPath và parser models. Ở mức senior, việc “đọc được XML” không còn đủ. Bạn phải có khả năng thiết kế một XML contract có thể sống lâu trong hệ thống enterprise, xử lý file lớn mà không làm nổ memory, harden parser trước input không đáng tin, version schema mà không phá consumer, dùng transformation/query đúng chỗ, và hiểu vì sao canonicalization hoặc digital signature lại phức tạp hơn việc hash raw XML text.

Tư duy xuyên suốt của phần này là chuyển từ “XML như dữ liệu” sang “XML như một processing platform”.

---

## 1. XSLT là gì?

XSLT là viết tắt của **XSL Transformations**. Nó là ngôn ngữ dùng để transform XML/XDM input thành một output tree hoặc serialization khác.

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

nói rằng khi processor cần xử lý một node phù hợp với pattern `book`, template này có thể được áp dụng.

Khác với Java nơi bạn thường gọi method trực tiếp, XSLT có thể vận hành theo kiểu dispatch dựa trên pattern. Đây là một điểm mạnh vì stylesheet có thể được modular hóa theo node type hoặc concern.

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

Nó không có nghĩa “loop qua book rồi chạy block này” một cách imperative. Nó nói rằng processor hãy chọn các `book` rồi dispatch từng node qua template phù hợp.

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

Đừng dùng `value-of` như mặc định cho mọi nested content. Nếu source có mixed content:

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

Nếu same node cần nhiều rendering modes hoặc override behavior theo type, template dispatch thường flexible hơn.

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

Đừng nghĩ variable trong XSLT giống mutable variable trong Java. XSLT thiên functional/declarative. Một binding thường biểu diễn một value, không phải một ô nhớ bạn mutate theo loop.

Tư duy immutable binding giúp transformation dễ reason hơn và phù hợp streaming/parallel optimization hơn.

---

## 8. Modes

Modes cho phép cùng source node được xử lý khác nhau tùy concern.

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

Nhiều developer chỉ từng gặp XSLT 1.0 trong hệ thống legacy nên nghĩ XSLT là một ngôn ngữ cũ, yếu và khó dùng. XSLT 2.0/3.0 cùng XPath hiện đại có type system, functions, grouping, packages, maps, arrays và streaming features mạnh hơn rất nhiều.

Điểm quan trọng không phải bạn phải dùng XSLT 3.0 ở mọi nơi, mà là khi review một system, bạn phải biết processor đang support version nào. Syntax và capability có thể khác rất xa.

---

## 10. XSLT streaming

Nếu source XML là 20 GB, việc build toàn tree trước transformation có thể không khả thi. XSLT 3.0 có các streaming-oriented capabilities giúp processor xử lý dữ liệu theo stream trong những constraints nhất định.

Streaming stylesheet không thể tùy ý “quay lại ancestor xa”, query toàn descendants tương lai hoặc sort toàn dataset mà không buffer, vì processor chưa thấy toàn data.

Senior phải hiểu rằng streaming không chỉ là bật một flag. Transformation logic phải **streamable**.

---

# XQuery

## 11. XQuery là gì?

XQuery là ngôn ngữ query đầy đủ cho XML/XDM. Nếu XPath là expression language, XQuery bổ sung cấu trúc để query, filter, join, sort, group và construct result.

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

XQuery rất phù hợp với XML-native databases hoặc hệ thống cần query collections of XML documents.

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

Đây là một pipeline declarative. Modern XQuery có thêm nhiều clauses nhưng FLWOR là mental model cơ bản.

---

## 13. XPath và XQuery khác nhau ở đâu?

XPath thường được embed vào XSLT, Java API, schema assertions hoặc tools để select/calculate.

XQuery là một full language có thể tạo output mới, define functions và implement query logic lớn.

Nếu chỉ cần lấy `/order/item/price`, XPath là đủ. Nếu cần join hai collections, aggregate, sort rồi construct report XML, XQuery phù hợp hơn.

---

# XDM và XPath nâng cao

## 14. XDM là gì?

XDM là **XQuery and XPath Data Model**. Đây là data model nền của XPath/XQuery/XSLT hiện đại.

XDM không chỉ có XML nodes. Nó còn có atomic values, sequences và trong 3.1 còn có function items, maps và arrays.

Ví dụ XPath expression:

```xpath
(1, 2, 3)
```

trả về một sequence ba atomic values.

Điều này rất khác mental model XPath 1.0 kiểu “mọi thứ là node set, string, number hoặc boolean”.

---

## 15. Sequence

Sequence là ordered sequence of items.

Một expression có thể trả:

```text
zero items
one item
many items
```

Item có thể là node hoặc atomic value.

Không phải sequence nào cũng là list object như Java, nhưng mental model “ordered result of items” là đúng.

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

Axes giúp query rõ ràng và precise hơn việc dùng `//` rồi filter rộng.

---

## 17. Namespace-safe XPath

Đây là rule senior phải coi như phản xạ.

Input A:

```xml
<a:order xmlns:a="urn:order"/>
```

Input B:

```xml
<o:order xmlns:o="urn:order"/>
```

Hai input cùng semantics.

XPath application nên bind một prefix riêng:

```text
ord → urn:order
```

sau đó query:

```xpath
/ord:order
```

Không bao giờ coi prefix source là identity.

---

# Schema Design và Contract Evolution

## 18. Namespace phải stable

Namespace URI là identity của vocabulary. Đừng đổi namespace chỉ vì:

```text
website đổi domain
server migrate
XSD file chuyển folder
team đổi tên
```

Nếu bạn đổi namespace, consumer có thể coi toàn bộ element là vocabulary mới.

Namespace nên được version/govern như một API identity.

---

## 19. Version trong namespace

Một strategy là:

```text
urn:example:order:v1
urn:example:order:v2
```

Ưu điểm là breaking version boundary rất rõ. Consumer không thể vô tình coi v2 là v1.

Nhược điểm là mọi XPath, XSD import, binding, serializer và message đều phải đổi namespace khi version đổi.

Strategy này hợp khi major versions thực sự độc lập.

---

## 20. Stable namespace + version attribute

Một strategy khác:

```xml
<order
  xmlns="urn:example:order"
  version="2">
```

Namespace giữ ổn định, version nằm trong data.

Ưu điểm là query namespace và vocabulary identity ít churn hơn.

Nhược điểm là application phải có logic rõ để phân biệt version semantics, và schema validation/version routing có thể phức tạp hơn.

Không có một strategy luôn đúng.

---

## 21. Backward-compatible change

Thêm optional element thường dễ compatible hơn:

```xml
<xs:element
  name="memo"
  minOccurs="0"/>
```

Nếu consumer cũ tolerant đúng cách, nó có thể ignore field mới.

Những thay đổi dễ breaking gồm rename required field, đổi namespace, đổi type từ string sang decimal khi old values không hợp, đổi order trong strict sequence, hoặc làm optional field thành required.

Schema evolution phải được treat như API evolution.

---

## 22. Extension points

XSD có wildcard:

```xml
<xs:any
  namespace="##other"
  processContents="lax"
  minOccurs="0"
  maxOccurs="unbounded"/>
```

Nó tạo nơi extension namespaces khác có thể cắm vào.

Điều này rất hữu ích với protocol cần vendor extension.

Nhưng `xs:any` ở khắp nơi sẽ làm schema gần như không còn ý nghĩa. Một good extension point phải có location, namespace policy và validation policy rõ.

---

## 23. `processContents`

`strict`, `lax`, `skip` điều khiển wildcard processing.

`strict` yêu cầu content được validate theo schema rules phù hợp.

`lax` cho phép validate nếu có declaration/schema phù hợp, còn nếu không có thì có thể tiếp tục.

`skip` nói không schema-validate wildcard content.

Nếu bạn dùng `skip` cho security-sensitive extension, application vẫn phải validate business data ở layer khác.

---

## 24. Identity constraints

XSD có `xs:unique`, `xs:key`, `xs:keyref`.

Chúng cho phép enforce một số relational-like constraints trong document.

Ví dụ một list customer có ID unique, rồi order reference customer bằng keyref.

Điều này hữu ích khi XML document là một self-contained dataset có internal references.

---

## 25. `xs:unique`

`xs:unique` bảo đảm values được chọn bởi selector/field không trùng lặp theo schema semantics.

Nó thích hợp với business condition kiểu “mọi SKU trong list phải unique”.

---

## 26. `xs:key`

`xs:key` giống key constraint với semantics chặt hơn về presence/value theo XSD rules.

Nó có thể được reference bởi `xs:keyref`.

---

## 27. `xs:keyref`

`xs:keyref` cho phép một field trỏ tới key được định nghĩa.

Ví dụ:

```text
order/customerRef
```

phải match một customer ID tồn tại trong document.

Đây là integrity constraint ở schema layer.

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

Một schema inheritance tree sâu làm consumer khó hiểu và code generation khó maintain. Composition thường dễ reason hơn nếu domain không thực sự cần polymorphism.

---

## 29. `xsi:type`

Instance có thể chọn derived type:

```xml
<person
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:type="EmployeeType">
```

nếu schema cho phép.

`xsi:type` hữu ích nhưng làm instance document gắn chặt hơn với schema type system. Nếu contract cần simple interoperability, explicit elements đôi khi dễ hơn.

---

## 30. Substitution groups

Substitution group cho phép element declarations thay thế một head element theo schema rules.

Nó hỗ trợ polymorphic XML vocabulary.

Nhưng khi kết hợp với derived types và `xsi:type`, schema có thể rất khó đọc. Senior phải cân bằng flexibility với maintainability.

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

Nếu Java binding map cả ba thành `null` hoặc `""`, business semantics có thể bị mất.

Contract phải định nghĩa rõ điều này.

---

# XML Binding và Java

## 32. XML object binding là convenience layer, không phải XML replacement

Framework như JAXB/Jakarta XML Binding có thể map:

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

Nhưng XML có nhiều concepts OO model không biểu diễn tự nhiên: mixed content, attribute vs element, namespace, order, unknown extensions, substitution groups, nil-vs-missing.

Nếu integration phức tạp, đừng để generated classes che mất contract semantics.

---

## 33. Contract-first vs object-first ở mức senior

Trong enterprise integration, một schema được nhiều Java/.NET/vendor systems dùng thường nên được thiết kế như một language-neutral contract.

Nếu generate XSD trực tiếp từ Java class, schema dễ mang theo những quyết định nội bộ của Java model như inheritance, collection wrapper hoặc naming conventions mà partner không cần biết.

Vì vậy contract-first thường phù hợp với long-lived cross-system XML interfaces.

---

# Large XML và Streaming

## 34. Vì sao DOM có thể rất tốn memory?

Raw XML 500 MB không có nghĩa DOM chỉ dùng 500 MB RAM.

Một DOM tree cần object cho mỗi element, text node, attribute, namespace binding và collections/pointers. Memory footprint có thể tăng nhiều lần so với source.

Vì vậy large XML phải được benchmark bằng actual parser, không estimate từ file size.

---

## 35. Streaming Parser Pattern

Với record-oriented XML:

```xml
<records>
  <record>...</record>
  <record>...</record>
</records>
```

StAX pipeline có thể:

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

Bạn không bắt buộc phải stream từng primitive field bằng tay.

Một pattern tốt là stream outer document, rồi khi tới một `<record>`, materialize riêng subtree đó thành object hoặc mini-DOM, xử lý xong rồi discard.

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

# Security

## 38. Vì sao XML có security surface lớn?

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

Senior phải coi parser như một component có filesystem/network capabilities cần được sandbox/harden.

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

Nếu parser resolve entity `xxe`, nó có thể đọc local file và đưa content vào parsed data.

Trên server, attack có thể nhắm:

```text
local file disclosure
SSRF
internal service access
cloud metadata endpoints
denial of service
```

Không phải mọi parser mặc định vulnerable, nhưng bạn không được dựa vào assumption. Hãy configure theo parser/version thật.

---

## 40. External DTD và SSRF

Ngay cả không dùng entity trực tiếp, DOCTYPE:

```xml
<!DOCTYPE root SYSTEM
  "http://internal-service/private.dtd">
```

có thể khiến parser gửi network request nếu external subset resolution enabled.

Đó là SSRF-style behavior.

---

## 41. Parameter entities

DTD còn có parameter entities, thường dùng bên trong DTD grammar.

External parameter entity cũng có thể trigger resource loading.

Vì vậy hardening chỉ “disable external general entities” nhưng bỏ parameter entities vẫn có thể chưa đủ.

---

## 42. Billion Laughs

Billion Laughs tận dụng recursive/nested entity expansion.

Concept đơn giản:

```text
entity A = "lol"
entity B = A repeated many times
entity C = B repeated many times
...
```

Source rất nhỏ nhưng expanded text có thể cực lớn, gây CPU/memory exhaustion.

Modern parsers thường có limits, nhưng application nên chủ động có resource limits.

---

## 43. XInclude

XInclude cho phép include external XML/resource:

```xml
<xi:include
  xmlns:xi="http://www.w3.org/2001/XInclude"
  href="other.xml"/>
```

Nếu input untrusted và XInclude enabled, attacker có thể influence external resource access.

Nếu application không cần XInclude, disable nó.

---

## 44. Schema resolution cũng là external access

XSD có imports/includes. Instance có `schemaLocation`. Nếu validator tự fetch remote schemas, attacker hoặc network dependency có thể ảnh hưởng behavior.

Một production system tốt nên dùng trusted local schema registry hoặc resolver.

---

## 45. XML Catalog

XML Catalog là cơ chế mapping external identifiers/URIs tới local resources.

Ví dụ concept:

```text
https://vendor.com/schema/order.xsd
→ /opt/app/schema/vendor-order-v3.xsd
```

Benefits gồm deterministic builds, offline processing, giảm latency và giảm arbitrary network fetch.

Trong enterprise XML infrastructure, Catalog là tool rất giá trị.

---

## 46. Secure parser strategy

Với untrusted XML, default mental checklist là: tắt DTD nếu không cần; tắt external general entities; tắt external parameter entities; block external DTD/schema resolution; tắt XInclude nếu không cần; giới hạn document size/depth/entity expansions; dùng secure processing options; và kiểm soát mọi URI resolver.

Exact flag khác nhau giữa `DocumentBuilderFactory`, `SAXParserFactory`, `XMLInputFactory`, `SchemaFactory` và `TransformerFactory`.

Điều này có nghĩa không tồn tại một config snippet universal cho mọi Java XML API.

---

## 47. Hardening một parser không harden toàn pipeline

Bạn có thể đã secure DOM parser nhưng sau đó XSLT `TransformerFactory` vẫn được phép `document()` tới external URI.

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

## 48. XSLT security

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

thì input chứa quotes hoặc XPath syntax có thể thay đổi query.

Concept giống SQL Injection.

Defense là dùng variable binding nếu engine hỗ trợ, không cho user cung cấp arbitrary expression fragments, hoặc validate input theo allowlist rõ ràng.

---

# Canonicalization và XML Signature

## 50. Vì sao không thể hash raw XML text một cách ngây thơ?

Hai serializations:

```xml
<user id="1" active="true"/>
```

và:

```xml
<user active="true" id="1"></user>
```

có thể mang cùng information theo XML data model nhưng raw bytes khác.

Nếu signature phụ thuộc raw formatting, chỉ cần formatter đổi attribute order hoặc empty element notation là hash fail.

Canonical XML giải quyết bằng cách tạo representation deterministic theo algorithm chuẩn.

---

## 51. Canonicalization không phải pretty-print

Pretty-print làm XML dễ đọc bằng indentation.

Canonicalization chuẩn hóa những lexical differences theo specification để phục vụ comparison/signature.

Không thể thay C14N bằng:

```text
trim spaces
sort attributes
normalize quotes
```

tự viết.

---

## 52. XML Digital Signature

XML Signature có thể sign whole document hoặc một phần document.

Signature thường chứa references, transforms, digest và signature value.

Điểm quan trọng là “signature valid” không có nghĩa toàn bộ XML document được business application tin tưởng. Nó chỉ chứng minh references đã verify theo signature semantics và trusted key.

Application phải hiểu signed scope.

---

## 53. Signature Wrapping Attack

Một attack class quan trọng là signature wrapping.

Concept:

```text
signed element A hợp lệ
attacker thêm element B
signature verifier xác nhận A
business code query nhầm B
```

Ví dụ verifier verify element có ID `signed-order`, nhưng application sau đó chạy:

```java
getElementsByTagName("Order").item(0)
```

và nhận một attacker-controlled `Order` khác.

Defense là application phải process **exact node đã được signature verifier xác nhận**, không verify xong rồi query document một lần nữa bằng selector mơ hồ.

---

## 54. ID semantics và signature

Reference kiểu:

```text
#order123
```

cần processor biết attribute nào là ID.

ID semantics có thể đến từ DTD, XSD, `xml:id` hoặc API/library configuration.

Một attribute tên `id` không tự động có ID semantics trong mọi XML API.

Đây là một chi tiết nhỏ nhưng cực kỳ quan trọng với XML Signature security.

---

# Integration Architecture

## 55. Boundary Validation Pattern

Một inbound pipeline tốt có thể là:

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

XSD không thay authorization. Parser security không thay business validation. Mapping không thay schema validation.

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

Strict reader reject field lạ.

Ưu điểm là contract predictable và security dễ reason.

Nhược điểm là forward compatibility thấp.

Tolerant reader cho phép unknown optional extensions.

Ưu điểm là schema evolution tốt hơn.

Nhược điểm là consumer có thể silently ignore semantic quan trọng.

Một senior contract phải nói rõ unknown element policy, thay vì để parser behavior quyết định ngẫu nhiên.

---

## 58. “Be liberal in what you accept” không phải lúc nào tốt

Postel's Law từng rất phổ biến trong protocol design, nhưng với security-critical contracts, quá tolerant có thể che lỗi hoặc bypass validation.

Một strategy hiện đại hơn là:

```text
strict core
explicit versioning
explicit extension points
known tolerance policy
```

---

## 59. Envelope Pattern

Nhiều XML protocols dùng envelope:

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

Header chứa cross-cutting metadata như correlation ID, routing, version, security information. Body chứa business payload.

SOAP là ví dụ nổi tiếng của pattern này.

---

## 60. Namespace Extension Pattern

Core vocabulary:

```text
urn:example:order
```

Partner extension:

```text
urn:partner:custom
```

XML Namespace giúp hai bên mở rộng cùng document mà tránh collision.

Nếu schema có controlled wildcard extension point, partner có thể thêm metadata mà không đổi core namespace.

---

## 61. Schema Registry Pattern

Một tổ chức lớn nên quản lý schema giống API artifacts.

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

business code không nên hiểu từng external schema.

Bạn có thể transform/map tất cả thành internal canonical model.

Flow:

```text
external XML
→ adapter / XSLT / mapper
→ canonical internal model
→ business services
```

Điều này giảm coupling.

Nhưng một canonical model quá generic cho toàn enterprise có thể thành “god model”. Nên scope theo bounded context/domain.

---

## 63. Anti-Corruption Layer

DDD gọi layer bảo vệ domain khỏi external model là Anti-Corruption Layer.

XML legacy thường rất phù hợp pattern này:

```text
vendor XML
→ parser
→ validation
→ transformation
→ internal DTO/domain
```

Legacy naming, namespace, null semantics và schema quirks dừng lại ở boundary.

---

# XML Design Idioms

## 64. Explicit units

Nếu number không có globally fixed unit, nên biểu diễn rõ:

```xml
<weight unit="kg">64</weight>
```

thay vì:

```xml
<weight>64</weight>
```

và để consumer đoán.

---

## 65. Stable identifiers

Nếu có:

```xml
<customer id="C123">
```

contract phải làm rõ ID unique ở scope nào, có case-sensitive không, có tái sử dụng không và tồn tại bao lâu.

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

Wrapper giúp collection có chỗ chứa metadata như count, pagination hoặc future options. Nhưng nó làm schema verbose hơn.

Chọn dựa trên khả năng evolution.

---

## 67. Discriminator attribute vs distinct elements

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

Option A giúp schema compact, option B làm element semantics explicit hơn.

Nếu mỗi contact type có structure khác nhau, distinct elements hoặc type system thường rõ hơn discriminator string.

---

# Senior Anti-patterns

## 68. Đổi namespace cho mọi minor release

Nếu `v1.1`, `v1.2`, `v1.3` đều có namespace mới, consumer phải update XPath/binding liên tục.

Chỉ version namespace khi strategy thực sự yêu cầu breaking identity.

---

## 69. `xs:any` ở mọi nơi

Schema nhìn flexible nhưng không validate được gì đáng kể.

Extension phải có boundary rõ.

---

## 70. Deep inheritance tree

Schema type inheritance 7 tầng có thể làm generated code cực khó hiểu.

Nếu composition đủ, composition thường dễ maintain hơn.

---

## 71. Monolithic XSD

Một file XSD chứa mọi domain, version và extension trở thành bottleneck governance.

Chia module theo vocabulary/domain và quản lý imports rõ ràng.

---

## 72. Everything required

Nếu mọi field bắt buộc, thêm feature mới gần như luôn breaking.

---

## 73. Everything optional

Nếu mọi field optional, schema không còn enforce business shape.

Senior phải cân bằng evolvability và correctness.

---

# Performance và Observability

## 74. Performance limits

Production XML processing nên nghĩ tới max bytes, depth, number of elements, number of attributes, max text node size, entity expansion limits và processing timeout.

Security và performance ở đây liên quan chặt nhau vì attacker có thể dùng XML complexity để tiêu tốn CPU/RAM.

---

## 75. Logging

Khi validation fail, log nên giúp debug:

```text
message type
namespace
schema version
correlation ID
line/column
validation path
error code
```

Nhưng không dump toàn XML nếu payload chứa password, PII hoặc financial data.

Một log “đủ để debug” không đồng nghĩa “log toàn payload”.

---

## 76. Golden document tests

Một XML contract tốt nên có sample tests cho minimum valid, full valid, old version, future extension, missing field, nil field, empty field, wrong order, invalid type, very large payload và malicious XXE input.

Các fixtures này giúp regression test schema, parser config và mapping code.

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
