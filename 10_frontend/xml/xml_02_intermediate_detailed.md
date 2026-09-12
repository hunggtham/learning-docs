# XML — Intermediate
## Namespace, DTD, XML Schema, XPath và các mô hình Parser

Tài liệu này tiếp nối phần Beginner. Ở phần trước, bạn đã biết XML là một cây dữ liệu strict, biết element, attribute, text, encoding, CDATA và khái niệm well-formed. Tuy nhiên chỉ biết cú pháp XML chưa đủ để dùng XML trong hệ thống thật. Khi nhiều vocabulary được trộn với nhau, bạn cần namespace. Khi muốn kiểm tra XML có đúng cấu trúc hay không, bạn cần DTD hoặc XML Schema. Khi muốn tìm dữ liệu trong cây, bạn cần XPath. Khi document nhỏ hoặc rất lớn, bạn phải chọn DOM, SAX hoặc StAX phù hợp.

Phần Intermediate được viết theo đúng flow đó để bạn hiểu vì sao từng lớp tồn tại.

---

## 1. Vấn đề name collision và lý do XML Namespace xuất hiện

Giả sử hệ thống của bạn cần kết hợp dữ liệu từ hai domain. Một domain nói về HTML-like document và một domain nói về furniture inventory. Cả hai đều dùng element tên `table`:

```xml
<document>
  <table>...</table>
  <table>...</table>
</document>
```

Nhìn vào XML này, application không biết `table` đầu tiên và `table` thứ hai thuộc vocabulary nào.

XML Namespace giải quyết vấn đề bằng cách làm cho tên logic của element không còn chỉ là local name `table`. Identity thật được xem như cặp:

```text
namespace URI + local name
```

Ví dụ:

```xml
<root
  xmlns:html="http://www.w3.org/1999/xhtml"
  xmlns:f="https://example.com/furniture">

  <html:table>...</html:table>
  <f:table>...</f:table>

</root>
```

Bây giờ hai element có local name giống nhau nhưng namespace khác nhau, vì vậy application phân biệt được hoàn toàn.

---

## 2. Prefix chỉ là alias, không phải identity thật

Đây là một trong những kiến thức quan trọng nhất của XML.

Hai tài liệu:

```xml
<a:user xmlns:a="https://example.com/user"/>
```

và:

```xml
<u:user xmlns:u="https://example.com/user"/>
```

có prefix khác nhau, nhưng cùng namespace URI và local name. Về namespace-aware identity, cả hai là cùng một expanded name:

```text
{https://example.com/user}user
```

Điều này có nghĩa khi code Java, XPath, XSLT hoặc schema xử lý XML, bạn không nên so sánh string prefix `a` hoặc `u` để xác định business meaning. Prefix có thể đổi tự do miễn nó vẫn bind tới cùng namespace URI.

Một XML serializer thậm chí có thể đọc input prefix `a` rồi serialize output thành `ns1` mà semantics vẫn không đổi.

---

## 3. Expanded name

Expanded name là mental model bạn nên dùng mọi lúc khi gặp namespace.

Ví dụ:

```xml
<app:user xmlns:app="https://example.com/app"/>
```

Element này có:

```text
namespace URI = https://example.com/app
local name    = user
```

Prefix `app` chỉ là cách viết lexical.

Khi security hoặc business logic match element, cách đúng về tư duy là match namespace URI và local name, không match raw tag string.

---

## 4. Default namespace

Nếu không muốn viết prefix lặp lại, XML cho phép default namespace:

```xml
<catalog xmlns="https://example.com/catalog">
  <book>
    <title>XML</title>
  </book>
</catalog>
```

Trong subtree này, các unprefixed elements `catalog`, `book`, `title` thuộc namespace `https://example.com/catalog`.

Điều này làm XML dễ đọc hơn, nhưng cũng gây một trong những bug XPath phổ biến nhất: developer thấy source không có prefix nên tưởng element “không namespace”. Thực tế chúng đang nằm trong default namespace.

---

## 5. Default namespace không áp dụng cho unprefixed attributes

Đây là rule phải thuộc lòng.

Xét:

```xml
<book
  xmlns="https://example.com/catalog"
  id="B001"/>
```

Element `book` thuộc namespace:

```text
https://example.com/catalog
```

Nhưng attribute `id` không có namespace.

Nếu bạn muốn namespaced attribute, phải viết prefix rõ:

```xml
<book
  xmlns="https://example.com/catalog"
  xmlns:app="https://example.com/app"
  app:id="B001"/>
```

Bây giờ `app:id` thuộc namespace `https://example.com/app`.

Điểm này rất quan trọng với XPath, DOM, XML Signature và binding frameworks.

---

## 6. Namespace scope và redeclaration

Namespace prefix binding có scope.

```xml
<root xmlns:p="urn:a">
  <p:item/>

  <section xmlns:p="urn:b">
    <p:item/>
  </section>
</root>
```

`p:item` đầu tiên thuộc `urn:a`, còn `p:item` bên trong `section` thuộc `urn:b`.

Vì vậy không được scan một file rồi kết luận “prefix `p` luôn nghĩa urn:a”. Binding phải được resolve theo context.

---

## 7. Namespace URI có bắt buộc phải mở được như URL không?

Không. Namespace URI là identifier. Nó có thể nhìn giống URL:

```text
https://example.com/order
```

hoặc là URN:

```text
urn:example:order
```

Processor không bắt buộc phải download schema từ namespace URI.

Một sai lầm phổ biến là nghĩ rằng `xmlns="https://example.com/order"` nghĩa browser hoặc parser sẽ truy cập URL này. Không phải. Schema location và namespace identity là hai khái niệm khác nhau.

---

## 8. Prefix `xml`

Prefix `xml` được dành sẵn cho XML namespace chuẩn và dùng trong:

```xml
xml:lang
xml:space
xml:base
xml:id
```

Bạn không được tự redefine `xml` sang namespace của mình.

---

## 9. Tại sao chỉ well-formed vẫn chưa đủ?

XML core chỉ kiểm tra cú pháp. Ví dụ:

```xml
<order>
  <banana>Hello</banana>
  <total>abc</total>
</order>
```

có thể hoàn toàn well-formed.

Nhưng application có thể yêu cầu `order` phải có `id`, `customer`, `total`, và `total` phải là decimal. Để diễn tả grammar hoặc contract đó, XML ecosystem dùng các schema languages. Hai công nghệ bạn cần hiểu trước tiên là DTD và XSD.

---

# DTD

## 10. DTD là gì?

DTD là **Document Type Definition**. Đây là cơ chế schema cổ điển đi cùng XML từ rất sớm.

Ví dụ:

```xml
<!DOCTYPE note [
  <!ELEMENT note (to,from,body)>
  <!ELEMENT to (#PCDATA)>
  <!ELEMENT from (#PCDATA)>
  <!ELEMENT body (#PCDATA)>
]>
```

Document:

```xml
<note>
  <to>Alice</to>
  <from>Bob</from>
  <body>Hello</body>
</note>
```

DTD nói rằng `note` phải chứa `to`, sau đó `from`, sau đó `body`.

Điểm đáng chú ý là syntax DTD không phải XML syntax thông thường. Đây là một lý do XSD sau này được thiết kế với syntax XML.

---

## 11. Internal DTD và external DTD

DTD có thể nằm trong chính document:

```xml
<!DOCTYPE note [
  <!ELEMENT note (#PCDATA)>
]>
```

hoặc reference external file:

```xml
<!DOCTYPE note SYSTEM "note.dtd">
```

External DTD rất quan trọng về security. Nếu parser được phép tự fetch URI hoặc file từ DTD của untrusted input, attacker có thể lợi dụng external entity hoặc external subset để đọc file, SSRF hoặc gây denial of service. Phần Senior sẽ đi sâu vào XXE.

---

## 12. `ELEMENT` declaration

DTD có thể định nghĩa child sequence:

```dtd
<!ELEMENT user (name,email)>
```

Điều này có nghĩa `user` cần `name` rồi đến `email`.

Nếu order đảo lại, document có thể invalid theo DTD dù vẫn well-formed.

---

## 13. Cardinality trong DTD

Các ký hiệu:

```text
?  zero or one
*  zero or more
+  one or more
```

Ví dụ:

```dtd
<!ELEMENT library (book*)>
```

nghĩa là `library` có thể không có book hoặc có nhiều book.

```dtd
<!ELEMENT user (phone?)>
```

nghĩa là phone optional.

---

## 14. Choice

```dtd
<!ELEMENT contact (email|phone)>
```

nghĩa là contact chứa một trong hai branch.

---

## 15. `#PCDATA`

```dtd
<!ELEMENT name (#PCDATA)>
```

`#PCDATA` nghĩa là parsed character data.

DTD cũng hỗ trợ mixed content, ví dụ:

```dtd
<!ELEMENT p (#PCDATA|em|strong)*>
```

cho phép text xen `em` và `strong`.

---

## 16. `ATTLIST`

DTD có thể định nghĩa attributes:

```dtd
<!ATTLIST user
  id ID #REQUIRED
  active (true|false) "true">
```

Ở đây `id` là attribute có type `ID` và bắt buộc. `active` chỉ nhận `true` hoặc `false`, mặc định là `true`.

Các từ khóa thường gặp gồm `#REQUIRED`, `#IMPLIED` và `#FIXED`.

---

## 17. Entities trong DTD

Bạn có thể define entity:

```dtd
<!ENTITY company "Acme Corporation">
```

sau đó dùng:

```xml
<name>&company;</name>
```

Parser có thể expand `&company;` thành text.

Entity system rất mạnh nhưng cũng là lý do DTD trở thành attack surface. External entities, parameter entities và entity expansion đều cần được control trong production.

---

## 18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?

DTD có khả năng mô tả structure nhưng type system hạn chế, namespace integration không tự nhiên và syntax riêng. Khi cần decimal, dateTime, typed attributes, reusable complex type hoặc advanced constraints, XSD thường phù hợp hơn.

DTD vẫn tồn tại trong nhiều publishing/document systems và legacy standards, nên senior phải đọc được, nhưng với application contract mới, XSD phổ biến hơn.

---

# XML Schema / XSD

## 19. XSD là gì?

XSD là XML Schema Definition. Khác DTD, XSD được viết bằng XML.

Ví dụ:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:element
    name="age"
    type="xs:integer"/>

</xs:schema>
```

Namespace `http://www.w3.org/2001/XMLSchema` là vocabulary của XML Schema.

XSD không chỉ nói element nào được nằm ở đâu. Nó còn có hệ thống data types, reusable types, restrictions, namespace integration và identity constraints.

---

## 20. Built-in data types

Một số types phải biết:

```text
xs:string
xs:boolean
xs:decimal
xs:integer
xs:int
xs:long
xs:date
xs:dateTime
xs:time
xs:anyURI
xs:base64Binary
xs:hexBinary
```

Ví dụ:

```xml
<xs:element name="price" type="xs:decimal"/>
```

Bây giờ `price` không còn chỉ là arbitrary text về mặt schema. Schema validator có thể kiểm tra lexical value có hợp `xs:decimal` hay không.

---

## 21. Simple type và complex type

Một simple element có thể khai báo trực tiếp:

```xml
<xs:element
  name="name"
  type="xs:string"/>
```

Complex type dùng khi element có children hoặc attributes:

```xml
<xs:element name="user">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="name" type="xs:string"/>
      <xs:element name="age" type="xs:integer"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

`user` không chỉ là một scalar value; nó là một structure.

---

## 22. `xs:sequence`

`xs:sequence` nói rằng child elements phải xuất hiện theo thứ tự.

```xml
<xs:sequence>
  <xs:element name="name"/>
  <xs:element name="email"/>
</xs:sequence>
```

Document:

```xml
<name>Alice</name>
<email>a@example.com</email>
```

hợp order.

Nếu đổi `email` trước `name`, có thể invalid.

Đây là điều cần nhớ khi version XML contract: nếu schema dùng strict sequence, chèn element mới vào sai vị trí có thể làm consumer cũ fail.

---

## 23. `xs:choice`

```xml
<xs:choice>
  <xs:element name="email"/>
  <xs:element name="phone"/>
</xs:choice>
```

Nghĩa là chọn một branch.

Choice rất hữu ích cho union-like structures nhưng nếu nested choice quá sâu, schema sẽ khó đọc và binding code cũng phức tạp.

---

## 24. `xs:all`

`xs:all` được dùng khi một nhóm elements có thể xuất hiện với order linh hoạt hơn `sequence`, trong constraints mà XSD version quy định.

Điểm quan trọng là đừng nghĩ `xs:all` nghĩa “bất kỳ thứ gì, bao nhiêu lần cũng được”. Nó vẫn có rule về children và occurrence. Nếu cần repeating arbitrary structures, bạn phải đọc đúng XSD model thay vì suy từ tên `all`.

---

## 25. `minOccurs` và `maxOccurs`

```xml
<xs:element
  name="item"
  minOccurs="0"
  maxOccurs="unbounded"/>
```

Nghĩa là `item` xuất hiện từ 0 tới vô hạn lần.

Nếu không ghi, nhiều declarations mặc định 1 occurrence.

Đây là lý do khi đọc XSD bạn phải chú ý defaults, không chỉ những attribute xuất hiện.

---

## 26. XSD attribute declaration

```xml
<xs:attribute
  name="id"
  type="xs:string"
  use="required"/>
```

`use="required"` bắt buộc attribute tồn tại.

Các cases khác có thể là optional hoặc prohibited tùy context.

---

## 27. Restriction và facets

Bạn có thể tạo type mới dựa trên type có sẵn:

```xml
<xs:simpleType name="PositiveAmount">
  <xs:restriction base="xs:decimal">
    <xs:minExclusive value="0"/>
  </xs:restriction>
</xs:simpleType>
```

Các facets quan trọng gồm:

```text
minInclusive
maxInclusive
minExclusive
maxExclusive
length
minLength
maxLength
pattern
enumeration
totalDigits
fractionDigits
whiteSpace
```

Facets là cách XSD biến generic type thành domain-specific value space.

---

## 28. Enumeration

```xml
<xs:simpleType name="Status">
  <xs:restriction base="xs:string">
    <xs:enumeration value="NEW"/>
    <xs:enumeration value="PAID"/>
    <xs:enumeration value="CANCELLED"/>
  </xs:restriction>
</xs:simpleType>
```

Schema validator sẽ reject value ngoài tập này.

Nhưng hãy nhớ rằng thêm hoặc xóa enum value có thể là breaking contract đối với generated clients.

---

## 29. Pattern

```xml
<xs:pattern value="[A-Z]{2}[0-9]{4}"/>
```

Pattern trong XML Schema dùng regex dialect riêng. Bạn không nên copy Java regex hoặc JavaScript regex rồi assume chúng tương đương hoàn toàn.

Nếu pattern là business-critical, đọc rules của XSD regex và test bằng đúng schema processor.

---

## 30. Named type và anonymous type

Named type:

```xml
<xs:complexType name="AddressType">
  ...
</xs:complexType>
```

sau đó reuse:

```xml
<xs:element
  name="billingAddress"
  type="AddressType"/>
```

Anonymous type:

```xml
<xs:element name="user">
  <xs:complexType>
    ...
  </xs:complexType>
</xs:element>
```

Named type hợp khi structure được reuse hoặc version độc lập. Anonymous type hợp với one-off local structure.

Việc chọn kiểu nào là một phần của schema design pattern, phần Master sẽ nói sâu hơn.

---

## 31. `targetNamespace`

Một schema thường định nghĩa vocabulary trong một namespace cụ thể:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="https://example.com/order"
  xmlns:o="https://example.com/order">
```

`targetNamespace` trả lời câu hỏi: “Các global schema components này thuộc vocabulary namespace nào?”

Nếu hiểu sai `targetNamespace`, bạn sẽ gặp lỗi kiểu schema nói `order` tồn tại nhưng validator báo “cannot find declaration” vì instance element không ở namespace đúng.

---

## 32. `elementFormDefault`

Một schema có thể khai báo:

```xml
elementFormDefault="qualified"
```

Điều này ảnh hưởng local elements có cần namespace qualification hay không.

Đây là một trong những điểm gây lỗi nhiều nhất khi làm SOAP/XSD Java binding. Một instance nhìn gần giống nhau nhưng khác namespace qualification có thể invalid hoàn toàn.

Khi debug, luôn xem cùng lúc:

```text
targetNamespace
elementFormDefault
namespace declarations của instance
```

---

## 33. `xs:include` và `xs:import`

`xs:include` thường dùng để compose schema components trong cùng namespace family/context:

```xml
<xs:include schemaLocation="common.xsd"/>
```

`xs:import` dùng để đưa schema components thuộc namespace khác vào:

```xml
<xs:import
  namespace="https://example.com/common"
  schemaLocation="common.xsd"/>
```

Một rule mental model dễ nhớ là:

```text
same namespace → include
different namespace → import
```

Dù thực tế XSD có thêm details, mental model này đủ tốt để bắt đầu.

---

## 34. `xsi:schemaLocation`

XML instance có thể chứa schema location hints:

```xml
<order
  xmlns="https://example.com/order"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
    https://example.com/order
    order.xsd">
```

Đây là hint mapping namespace tới schema location.

Điều quan trọng về security là application không nên mặc định tin và fetch arbitrary schema URL từ untrusted document. Resolver và schema source nên do application kiểm soát.

---

## 35. `xsi:noNamespaceSchemaLocation`

Nếu vocabulary không có namespace, instance có thể dùng:

```xml
xsi:noNamespaceSchemaLocation="note.xsd"
```

Nó vẫn là schema location hint, không biến untrusted URL thành trusted dependency.

---

## 36. `xsi:nil`

Ví dụ:

```xml
<middleName
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:nil="true"/>
```

Nếu schema declaration cho phép `nillable`, element có thể biểu diễn nil.

Bạn phải phân biệt ba trạng thái:

```xml
<middleName xsi:nil="true"/>
```

```xml
<middleName></middleName>
```

và element hoàn toàn không xuất hiện.

Nil, empty và missing có thể có business meaning khác nhau. Đây là lý do object mapping XML sang Java `null` đôi khi làm mất thông tin nếu mapping không cẩn thận.

---

# XPath

## 37. XPath là gì?

XPath là ngôn ngữ expression/query dùng để chọn hoặc tính toán dựa trên XML/XDM.

Ví dụ document:

```xml
<library>
  <book id="1">
    <title>XML</title>
  </book>

  <book id="2">
    <title>Java</title>
  </book>
</library>
```

XPath:

```xpath
/library/book/title
```

chọn các `title` elements.

Bạn nên hình dung XPath như “đường đi + điều kiện” trên tree, nhưng modern XPath còn mạnh hơn nhiều và có type system, functions, sequences.

---

## 38. Absolute path

```xpath
/library/book
```

đi từ document/root context tới `library`, sau đó child `book`.

---

## 39. `//`

```xpath
//book
```

là shorthand liên quan descendant-or-self traversal.

Nó rất tiện nhưng dễ bị lạm dụng. Trên XML lớn, query quá rộng khó reason và có thể tốn tài nguyên. Nếu biết path rõ, path explicit thường tốt hơn.

---

## 40. Attribute selection

```xpath
/library/book/@id
```

chọn `id` attributes.

---

## 41. Predicate

```xpath
/library/book[@id='2']
```

chọn book có attribute id bằng `2`.

Predicate có thể dùng expression phức tạp hơn, không chỉ attribute equality.

---

## 42. Position

```xpath
/library/book[1]
```

chọn first book trong context phù hợp.

```xpath
/library/book[last()]
```

chọn last book.

Khi dùng position với `//` hoặc grouped expressions, context có thể khác điều bạn nghĩ. Đây là lý do senior XPath cần hiểu expression evaluation thay vì chỉ ghi nhớ syntax.

---

## 43. `text()`

```xpath
/library/book/title/text()
```

chọn direct text nodes của `title`.

Trong mixed content:

```xml
<p>Hello <b>world</b>!</p>
```

`p/text()` chỉ chọn direct text nodes `"Hello "` và `"!"`, không tự trả text trong `<b>`.

String-value của `p` có thể là `"Hello world!"` theo XPath data model.

Đây là khác biệt rất quan trọng.

---

## 44. Wildcard

```xpath
/library/*
```

chọn element children.

```xpath
//@*
```

có thể chọn rất rộng các attributes.

Wildcard useful nhưng làm query ít explicit hơn, nên chỉ dùng khi vocabulary thực sự cần generic handling.

---

## 45. Các XPath functions thường gặp

Bạn sẽ thường thấy:

```xpath
count(/library/book)
```

```xpath
normalize-space(title)
```

```xpath
contains(title, 'XML')
```

```xpath
starts-with(@id, 'B')
```

Ngoài ra còn có `string()`, `position()`, `last()`, `name()`, `local-name()`, `namespace-uri()`.

Exact set phụ thuộc XPath version. Phần Senior/Master sẽ chuyển từ XPath 1.0 mental model sang XPath 3.x/XDM.

---

## 46. Default namespace và bug XPath nổi tiếng

Document:

```xml
<library xmlns="https://example.com/books">
  <book/>
</library>
```

Developer viết:

```xpath
/library/book
```

và không nhận được result.

Lý do là `library` và `book` thuộc namespace `https://example.com/books`. Trong nhiều XPath host APIs, unprefixed name trong expression không tự map tới default namespace của source document.

Bạn cần bind một prefix của riêng mình:

```text
b → https://example.com/books
```

sau đó query:

```xpath
/b:library/b:book
```

Prefix `b` không cần xuất hiện trong source XML. Nó chỉ cần map tới đúng namespace URI.

Đây là nguyên tắc quan trọng nhất khi debug XPath namespace.

---

# Parser Models

## 47. Vì sao phải có nhiều loại parser?

Một file XML 20 KB và một file XML 10 GB có cùng cú pháp, nhưng cách xử lý tối ưu khác hoàn toàn.

Nếu load 10 GB thành DOM tree, memory usage có thể lớn hơn raw file nhiều lần. Vì vậy XML ecosystem có cả tree parser và streaming parser.

Ba mô hình bạn nên biết là DOM, SAX và StAX.

---

## 48. DOM

DOM parser đọc toàn bộ document rồi tạo tree trong memory.

Lợi ích là bạn có thể nhảy tới bất kỳ node nào, dùng XPath thuận tiện, mutate tree và serialize lại.

Ví dụ mental model Java:

```java
Document doc = builder.parse(file);
```

sau đó:

```java
Element root = doc.getDocumentElement();
```

DOM rất dễ dùng với XML nhỏ và vừa.

Nhược điểm là memory cost. Mỗi element không chỉ chiếm bytes của source; còn có object overhead, strings, pointers, namespace metadata và child collections.

---

## 49. SAX

SAX là event-driven push parser.

Thay vì đưa bạn tree, parser gọi callbacks kiểu:

```text
startDocument
startElement
characters
endElement
endDocument
```

Ví dụ khi đọc:

```xml
<user>
  <name>Alice</name>
</user>
```

application có thể nhận một chuỗi events tương ứng.

Ưu điểm của SAX là memory rất thấp vì parser không cần giữ toàn tree. Nhược điểm là state management khó hơn. Nếu muốn biết “đang ở trong user nào, đã đọc field gì”, bạn phải tự giữ state.

---

## 50. StAX

StAX là streaming pull parser phổ biến trong Java ecosystem.

Khác SAX gọi ngược vào application, StAX cho application chủ động yêu cầu event tiếp theo.

Mental model:

```java
while (reader.hasNext()) {
    int event = reader.next();
}
```

Điều này thường khiến control flow dễ reason hơn SAX, đặc biệt khi parse record-oriented XML lớn.

---

## 51. Chọn DOM, SAX hay StAX

Nếu XML nhỏ hoặc vừa và bạn cần random access, XPath hoặc mutation, DOM thường đơn giản nhất.

Nếu XML rất lớn và bạn chỉ cần đọc một lần từ đầu tới cuối, SAX hoặc StAX tốt hơn.

Trong Java business application, StAX thường là lựa chọn thuận tiện cho large XML vì pull model dễ viết state machine.

Không nên chọn parser chỉ theo “cái nào nhanh nhất”. Hãy chọn theo access pattern và memory requirement.

---

## 52. Java DOM cơ bản

Ví dụ:

```java
DocumentBuilderFactory factory =
    DocumentBuilderFactory.newInstance();

factory.setNamespaceAware(true);

DocumentBuilder builder =
    factory.newDocumentBuilder();

Document document =
    builder.parse(file);
```

`setNamespaceAware(true)` cực kỳ quan trọng nếu XML dùng namespaces.

Tuy nhiên đoạn code này chưa phải secure parser configuration. External DTD/entity processing có thể cần disable hoặc control tùy implementation. Phần Senior sẽ giải thích vì sao.

---

## 53. Java XPath cơ bản

```java
XPath xpath =
    XPathFactory.newInstance().newXPath();

String value =
    xpath.evaluate(
        "/library/book[1]/title",
        document
    );
```

Với namespaced XML, bạn cần `NamespaceContext` hoặc cơ chế tương đương để prefix trong XPath map tới namespace URI.

Không hardcode prefix source làm business identity.

---

## 54. Serialization

Sau khi tạo hoặc sửa XML tree, bạn có thể serialize nó thành bytes/text.

Serialization phải xử lý đúng:

```text
encoding
escaping
namespace declarations
XML declaration
empty elements
text
```

Nếu output có cryptographic requirement, bạn còn phải phân biệt ordinary serialization với canonicalization.

Một XML serializer được thiết kế đúng tốt hơn nhiều so với nối string thủ công.

---

## 55. Marshal và unmarshal

Trong object binding frameworks, bạn thường gặp hai từ:

```text
marshal   object → XML
unmarshal XML → object
```

Ví dụ XML:

```xml
<user>
  <name>Alice</name>
</user>
```

có thể map thành Java object `User`.

Nhưng object model thường đơn giản hơn XML model. Mixed content, namespaces, nil-vs-missing, order, repeating elements và unknown extension đều có thể làm mapping mất nuance.

Vì vậy senior không nên nghĩ “có JAXB thì không cần hiểu XML”.

---

## 56. Schema validation nằm ở đâu trong flow?

Một inbound XML flow đơn giản có thể là:

```text
bytes
→ secure parse
→ namespace-aware tree/stream
→ XSD validation
→ mapping
→ business validation
```

XSD kiểm tra structural/type rules. Nó không thay business logic.

Ví dụ schema có thể nói `amount` là decimal dương, nhưng không biết user hiện tại có quyền transfer số tiền đó hay không. Authorization vẫn thuộc application.

---

## 57. Lỗi “schema không tìm thấy declaration”

Đây là lỗi rất phổ biến. Bạn có schema định nghĩa:

```text
{urn:order}order
```

nhưng input thực tế là:

```xml
<order>
```

không namespace.

Dù local name đều là `order`, expanded name khác nhau.

Hoặc input có default namespace đúng nhưng XPath/schema config không namespace-aware.

Khi debug, luôn kiểm tra:

```text
namespace URI
local name
targetNamespace
elementFormDefault
schema source
```

---

## 58. Anti-pattern: trust `schemaLocation`

Nếu untrusted XML nói:

```xml
xsi:schemaLocation="
  urn:order
  http://internal-server/schema.xsd"
```

và parser/validator tự fetch URL đó, attacker có thể ảnh hưởng network access.

Production application nên chủ động chọn schema trusted, dùng local registry hoặc resolver. Instance hint không nên tự trở thành authority.

---

## 59. Anti-pattern: DOM cho file khổng lồ

Nếu input 5 GB, DOM có thể consume memory nhiều lần 5 GB và gây OutOfMemoryError.

Khi data có structure kiểu:

```xml
<records>
  <record>...</record>
  <record>...</record>
  ...
</records>
```

streaming parser là lựa chọn tự nhiên.

---

## 60. Anti-pattern: XPath `//` ở mọi nơi

Query:

```xpath
//price
```

có thể match price ở nhiều context ngoài ý muốn.

Nếu vocabulary biết rõ:

```xpath
/order/items/item/price
```

thường an toàn và dễ review hơn.

Đặc biệt trong security-sensitive code, query broad có thể chọn wrong node.

---

## 61. Bài tập tổng hợp Intermediate

Cho XML:

```xml
<o:order
  xmlns:o="urn:order"
  xmlns:c="urn:common"
  id="123">

  <c:customer>
    <c:name>Alice</c:name>
  </c:customer>

  <o:item sku="A1">
    <o:price>10.50</o:price>
  </o:item>

</o:order>
```

`o:order` thuộc namespace `urn:order`. Attribute `id` không có namespace vì nó unprefixed. `c:customer` và `c:name` thuộc `urn:common`. `sku` cũng không có namespace. `o:item` và `o:price` thuộc `urn:order`.

Nếu dùng XPath, bạn có thể tự bind:

```text
ord → urn:order
com → urn:common
```

rồi dùng:

```xpath
/ord:order/ord:item/ord:price
```

Prefix trong query không cần giống prefix source.

Nếu file có 5 triệu `item`, StAX hoặc SAX thường hợp hơn DOM.

---

## 62. Mental model sau Intermediate

Sau phần này, XML processing flow của bạn nên mở rộng thành:

```text
raw bytes
→ encoding
→ XML parser
→ well-formedness
→ namespace expansion
→ optional DTD/schema processing
→ DOM hoặc stream
→ XPath/query
→ application/domain
```

Bạn cũng phải hiểu rằng namespace và schema là hai lớp riêng. Namespace định danh vocabulary; schema mô tả grammar/type của vocabulary.

Ở phần Senior, chúng ta sẽ thêm transformation, XQuery, schema evolution, streaming architecture, XXE, XML Catalog, canonicalization và XML Signature.
