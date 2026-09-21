# XML — Intermediate
## Namespace, DTD, XML Schema, XPath và các mô hình Parser

Tài liệu này tiếp nối phần Beginner. Ở phần trước, bạn đã biết XML là một cây dữ liệu strict, biết phần tử (element), thuộc tính (attribute), text, encoding, CDATA và khái niệm đúng cú pháp XML (well-formed). Tuy nhiên chỉ biết cú pháp XML chưa đủ để dùng XML trong hệ thống thật. Khi nhiều vocabulary được trộn với nhau, bạn cần không gian tên (namespace). Khi muốn kiểm tra XML có đúng cấu trúc hay không, bạn cần DTD hoặc XML Schema. Khi muốn tìm dữ liệu trong cây, bạn cần XPath. Khi document nhỏ hoặc rất lớn, bạn phải chọn DOM, SAX hoặc StAX phù hợp.

Phần Intermediate được viết theo đúng flow đó để bạn hiểu vì sao từng lớp tồn tại.


## Quy ước thuật ngữ trong tài liệu

Tài liệu ưu tiên tiếng Việt tự nhiên nhưng giữ thuật ngữ gốc ở những khái niệm cần tra cứu. Các thuật ngữ cốt lõi được dùng thống nhất như sau: **phần tử (element)** là đơn vị cấu trúc chính của XML; **thuộc tính (attribute)** là thông tin gắn trên phần tử; **không gian tên (namespace)** phân biệt các bộ từ vựng XML; **lược đồ (schema)** mô tả cấu trúc và kiểu dữ liệu hợp lệ; **phân tích cú pháp (parsing)** biến byte/text XML thành cây hoặc chuỗi sự kiện; **đúng cú pháp XML (well-formed)** nghĩa là thỏa các quy tắc cú pháp lõi; **kiểm tra tính hợp lệ (validation)** kiểm tra tài liệu theo DTD/XSD hoặc quy tắc khác; **xử lý theo luồng (streaming)** đọc dữ liệu tuần tự mà không giữ toàn bộ cây trong bộ nhớ; **tuần tự hóa (serialization)** biến cấu trúc XML trong bộ nhớ trở lại dạng text/byte; **chuẩn hóa chính tắc (canonicalization/C14N)** tạo biểu diễn ổn định phục vụ so sánh hoặc chữ ký số. Các tên chuẩn như XML, DTD, XSD, XPath, XSLT, XQuery, DOM, SAX, StAX, SOAP, WSDL, QName, PSVI và tên API cụ thể được giữ nguyên.


---

## 1. Vấn đề name collision và lý do XML Namespace xuất hiện

Giả sử hệ thống của bạn cần kết hợp dữ liệu từ hai domain. Một domain nói về HTML-like document và một domain nói về furniture inventory. Cả hai đều dùng phần tử (element) tên `table`:

```xml
<document>
  <table>...</table>
  <table>...</table>
</document>
```

Nhìn vào XML này, application không biết `table` đầu tiên và `table` thứ hai thuộc vocabulary nào.

XML Namespace giải quyết vấn đề bằng cách làm cho tên logic của phần tử (element) không còn chỉ là local name `table`. Identity thật được xem như cặp:

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

Bây giờ hai phần tử (element) có local name giống nhau nhưng không gian tên (namespace) khác nhau, vì vậy application phân biệt được hoàn toàn.

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

có tiền tố (prefix) khác nhau, nhưng cùng URI của không gian tên (không gian tên (namespace) URI) và local name. Về nhận biết không gian tên (namespace-aware) identity, cả hai là cùng một tên mở rộng (expanded name):

```text
{https://example.com/user}user
```

Điều này có nghĩa khi code Java, XPath, XSLT hoặc lược đồ (schema) xử lý XML, bạn không nên so sánh string tiền tố (prefix) `a` hoặc `u` để xác định business meaning. Prefix có thể đổi tự do miễn nó vẫn bind tới cùng URI của không gian tên (không gian tên (namespace) URI).

Một XML serializer thậm chí có thể đọc input tiền tố (prefix) `a` rồi serialize output thành `ns1` mà semantics vẫn không đổi.

---

## 3. Expanded name

Expanded name là mental model bạn nên dùng mọi lúc khi gặp không gian tên (namespace).

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

Khi bảo mật (security) hoặc business logic match phần tử (element), cách đúng về tư duy là match URI của không gian tên (không gian tên (namespace) URI) và local name, không match raw tag string.

---

## 4. Default không gian tên (namespace)

Nếu không muốn viết tiền tố (prefix) lặp lại, XML cho phép không gian tên mặc định (default không gian tên (namespace)):

```xml
<catalog xmlns="https://example.com/catalog">
  <book>
    <title>XML</title>
  </book>
</catalog>
```

Trong subtree này, các unprefixed các phần tử (elements) `catalog`, `book`, `title` thuộc không gian tên (namespace) `https://example.com/catalog`.

Điều này làm XML dễ đọc hơn, nhưng cũng gây một trong những bug XPath phổ biến nhất: developer thấy source không có tiền tố (prefix) nên tưởng phần tử (element) “không không gian tên (namespace)”. Thực tế chúng đang nằm trong không gian tên mặc định (default không gian tên (namespace)).

---

## 5. Default không gian tên (namespace) không áp dụng cho unprefixed các thuộc tính (attributes)

Đây là rule phải thuộc lòng.

Xét:

```xml
<book
  xmlns="https://example.com/catalog"
  id="B001"/>
```

Element `book` thuộc không gian tên (namespace):

```text
https://example.com/catalog
```

Nhưng thuộc tính (attribute) `id` không có không gian tên (namespace).

Nếu bạn muốn namespaced thuộc tính (attribute), phải viết tiền tố (prefix) rõ:

```xml
<book
  xmlns="https://example.com/catalog"
  xmlns:app="https://example.com/app"
  app:id="B001"/>
```

Bây giờ `app:id` thuộc không gian tên (namespace) `https://example.com/app`.

Điểm này rất quan trọng với XPath, DOM, XML Signature và ánh xạ/liên kết (binding) frameworks.

---

## 6. Namespace scope và redeclaration

Namespace tiền tố (prefix) ánh xạ/liên kết (binding) có scope.

```xml
<root xmlns:p="urn:a">
  <p:item/>

  <section xmlns:p="urn:b">
    <p:item/>
  </section>
</root>
```

`p:item` đầu tiên thuộc `urn:a`, còn `p:item` bên trong `section` thuộc `urn:b`.

Vì vậy không được scan một file rồi kết luận “tiền tố (prefix) `p` luôn nghĩa urn:a”. Binding phải được resolve theo context.

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

Processor không bắt buộc phải download lược đồ (schema) từ URI của không gian tên (không gian tên (namespace) URI).

Một sai lầm phổ biến là nghĩ rằng `xmlns="https://example.com/order"` nghĩa trình duyệt (browser) hoặc bộ phân tích cú pháp (parser) sẽ truy cập URL này. Không phải. Schema location và không gian tên (namespace) identity là hai khái niệm khác nhau.

---

## 8. Prefix `xml`

Prefix `xml` được dành sẵn cho XML không gian tên (namespace) chuẩn và dùng trong:

```xml
xml:lang
xml:space
xml:base
xml:id
```

Bạn không được tự redefine `xml` sang không gian tên (namespace) của mình.

---

## 9. Tại sao chỉ đúng cú pháp XML (well-formed) vẫn chưa đủ?

XML core chỉ kiểm tra cú pháp. Ví dụ:

```xml
<order>
  <banana>Hello</banana>
  <total>abc</total>
</order>
```

có thể hoàn toàn đúng cú pháp XML (well-formed).

Nhưng application có thể yêu cầu `order` phải có `id`, `customer`, `total`, và `total` phải là decimal. Để diễn tả grammar hoặc contract đó, XML ecosystem dùng các lược đồ (schema) languages. Hai công nghệ bạn cần hiểu trước tiên là DTD và XSD.

---

# DTD

## 10. DTD là gì?

DTD là **Document Type Definition**. Đây là cơ chế lược đồ (schema) cổ điển đi cùng XML từ rất sớm.

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

External DTD rất quan trọng về bảo mật (security). Nếu bộ phân tích cú pháp (parser) được phép tự fetch URI hoặc file từ DTD của untrusted input, attacker có thể lợi dụng thực thể ngoài (external thực thể (entity)) hoặc external subset để đọc file, SSRF hoặc gây denial of service. Phần Senior sẽ đi sâu vào XXE.

---

## 12. `ELEMENT` declaration

DTD có thể định nghĩa child sequence:

```dtd
<!ELEMENT user (name,email)>
```

Điều này có nghĩa `user` cần `name` rồi đến `email`.

Nếu order đảo lại, document có thể invalid theo DTD dù vẫn đúng cú pháp XML (well-formed).

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

DTD cũng hỗ trợ nội dung hỗn hợp (mixed content), ví dụ:

```dtd
<!ELEMENT p (#PCDATA|em|strong)*>
```

cho phép text xen `em` và `strong`.

---

## 16. `ATTLIST`

DTD có thể định nghĩa các thuộc tính (attributes):

```dtd
<!ATTLIST user
  id ID #REQUIRED
  active (true|false) "true">
```

Ở đây `id` là thuộc tính (attribute) có type `ID` và bắt buộc. `active` chỉ nhận `true` hoặc `false`, mặc định là `true`.

Các từ khóa thường gặp gồm `#REQUIRED`, `#IMPLIED` và `#FIXED`.

---

## 17. Entities trong DTD

Bạn có thể define thực thể (entity):

```dtd
<!ENTITY company "Acme Corporation">
```

sau đó dùng:

```xml
<name>&company;</name>
```

Parser có thể expand `&company;` thành text.

Entity system rất mạnh nhưng cũng là lý do DTD trở thành bề mặt tấn công (attack surface). External các thực thể (entities), parameter các thực thể (entities) và thực thể (entity) expansion đều cần được control trong production.

---

## 18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?

DTD có khả năng mô tả structure nhưng hệ kiểu (type system) hạn chế, không gian tên (namespace) integration không tự nhiên và syntax riêng. Khi cần decimal, dateTime, typed các thuộc tính (attributes), reusable complex type hoặc advanced constraints, XSD thường phù hợp hơn.

DTD vẫn tồn tại trong nhiều publishing/document systems và legacy standards, nên senior phải đọc được, nhưng với application contract mới, XSD phổ biến hơn.

---

# Lược đồ XML (XML Schema/XSD)

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

XSD không chỉ nói phần tử (element) nào được nằm ở đâu. Nó còn có hệ thống data types, reusable types, restrictions, không gian tên (namespace) integration và ràng buộc định danh (identity constraints).

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

Bây giờ `price` không còn chỉ là arbitrary text về mặt lược đồ (schema). Schema validator có thể kiểm tra lexical value có hợp `xs:decimal` hay không.

---

## 21. Simple type và complex type

Một simple phần tử (element) có thể khai báo trực tiếp:

```xml
<xs:element
  name="name"
  type="xs:string"/>
```

Complex type dùng khi phần tử (element) có children hoặc các thuộc tính (attributes):

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

`xs:sequence` nói rằng child các phần tử (elements) phải xuất hiện theo thứ tự.

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

Đây là điều cần nhớ khi version XML contract: nếu lược đồ (schema) dùng strict sequence, chèn phần tử (element) mới vào sai vị trí có thể làm consumer cũ fail.

---

## 23. `xs:choice`

```xml
<xs:choice>
  <xs:element name="email"/>
  <xs:element name="phone"/>
</xs:choice>
```

Nghĩa là chọn một branch.

Choice rất hữu ích cho union-like structures nhưng nếu nested choice quá sâu, lược đồ (schema) sẽ khó đọc và ánh xạ/liên kết (binding) code cũng phức tạp.

---

## 24. `xs:all`

`xs:all` được dùng khi một nhóm các phần tử (elements) có thể xuất hiện với order linh hoạt hơn `sequence`, trong constraints mà XSD version quy định.

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

Đây là lý do khi đọc XSD bạn phải chú ý defaults, không chỉ những thuộc tính (attribute) xuất hiện.

---

## 26. XSD thuộc tính (attribute) declaration

```xml
<xs:attribute
  name="id"
  type="xs:string"
  use="required"/>
```

`use="required"` bắt buộc thuộc tính (attribute) tồn tại.

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

Nếu pattern là business-critical, đọc rules của XSD regex và test bằng đúng lược đồ (schema) processor.

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

Việc chọn kiểu nào là một phần của lược đồ (schema) design pattern, phần Master sẽ nói sâu hơn.

---

## 31. `targetNamespace`

Một lược đồ (schema) thường định nghĩa vocabulary trong một không gian tên (namespace) cụ thể:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="https://example.com/order"
  xmlns:o="https://example.com/order">
```

`targetNamespace` trả lời câu hỏi: “Các global lược đồ (schema) components này thuộc vocabulary không gian tên (namespace) nào?”

Nếu hiểu sai `targetNamespace`, bạn sẽ gặp lỗi kiểu lược đồ (schema) nói `order` tồn tại nhưng validator báo “cannot find declaration” vì instance phần tử (element) không ở không gian tên (namespace) đúng.

---

## 32. `elementFormDefault`

Một lược đồ (schema) có thể khai báo:

```xml
elementFormDefault="qualified"
```

Điều này ảnh hưởng local các phần tử (elements) có cần không gian tên (namespace) qualification hay không.

Đây là một trong những điểm gây lỗi nhiều nhất khi làm SOAP/XSD Java ánh xạ/liên kết (binding). Một instance nhìn gần giống nhau nhưng khác không gian tên (namespace) qualification có thể invalid hoàn toàn.

Khi debug, luôn xem cùng lúc:

```text
targetNamespace
elementFormDefault
namespace declarations của instance
```

---

## 33. `xs:include` và `xs:import`

`xs:include` thường dùng để compose lược đồ (schema) components trong cùng không gian tên (namespace) family/context:

```xml
<xs:include schemaLocation="common.xsd"/>
```

`xs:import` dùng để đưa lược đồ (schema) components thuộc không gian tên (namespace) khác vào:

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

XML instance có thể chứa lược đồ (schema) location hints:

```xml
<order
  xmlns="https://example.com/order"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
    https://example.com/order
    order.xsd">
```

Đây là hint ánh xạ (mapping) không gian tên (namespace) tới lược đồ (schema) location.

Điều quan trọng về bảo mật (security) là application không nên mặc định tin và fetch arbitrary lược đồ (schema) URL từ untrusted document. Resolver và lược đồ (schema) source nên do application kiểm soát.

---

## 35. `xsi:noNamespaceSchemaLocation`

Nếu vocabulary không có không gian tên (namespace), instance có thể dùng:

```xml
xsi:noNamespaceSchemaLocation="note.xsd"
```

Nó vẫn là lược đồ (schema) location hint, không biến untrusted URL thành trusted dependency.

---

## 36. `xsi:nil`

Ví dụ:

```xml
<middleName
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:nil="true"/>
```

Nếu lược đồ (schema) declaration cho phép `nillable`, phần tử (element) có thể biểu diễn nil.

Bạn phải phân biệt ba trạng thái:

```xml
<middleName xsi:nil="true"/>
```

```xml
<middleName></middleName>
```

và phần tử (element) hoàn toàn không xuất hiện.

Nil, empty và missing có thể có business meaning khác nhau. Đây là lý do object ánh xạ (mapping) XML sang Java `null` đôi khi làm mất thông tin nếu ánh xạ (mapping) không cẩn thận.

---

# XPath

## 37. XPath là gì?

XPath là ngôn ngữ expression/truy vấn (query) dùng để chọn hoặc tính toán dựa trên XML/XDM.

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

chọn các `title` các phần tử (elements).

Bạn nên hình dung XPath như “đường đi + điều kiện” trên tree, nhưng modern XPath còn mạnh hơn nhiều và có hệ kiểu (type system), functions, sequences.

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

Nó rất tiện nhưng dễ bị lạm dụng. Trên XML lớn, truy vấn (query) quá rộng khó reason và có thể tốn tài nguyên. Nếu biết path rõ, path explicit thường tốt hơn.

---

## 40. Attribute selection

```xpath
/library/book/@id
```

chọn `id` các thuộc tính (attributes).

---

## 41. Predicate

```xpath
/library/book[@id='2']
```

chọn book có thuộc tính (attribute) id bằng `2`.

Predicate có thể dùng expression phức tạp hơn, không chỉ thuộc tính (attribute) equality.

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

Trong nội dung hỗn hợp (mixed content):

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

chọn phần tử (element) children.

```xpath
//@*
```

có thể chọn rất rộng các các thuộc tính (attributes).

Wildcard useful nhưng làm truy vấn (query) ít explicit hơn, nên chỉ dùng khi vocabulary thực sự cần generic handling.

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

## 46. Default không gian tên (namespace) và bug XPath nổi tiếng

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

Lý do là `library` và `book` thuộc không gian tên (namespace) `https://example.com/books`. Trong nhiều XPath host APIs, unprefixed name trong expression không tự map tới không gian tên mặc định (default không gian tên (namespace)) của source document.

Bạn cần bind một tiền tố (prefix) của riêng mình:

```text
b → https://example.com/books
```

sau đó truy vấn (query):

```xpath
/b:library/b:book
```

Prefix `b` không cần xuất hiện trong source XML. Nó chỉ cần map tới đúng URI của không gian tên (không gian tên (namespace) URI).

Đây là nguyên tắc quan trọng nhất khi debug XPath không gian tên (namespace).

---

# Các mô hình phân tích cú pháp (Parser Models)

## 47. Vì sao phải có nhiều loại bộ phân tích cú pháp (parser)?

Một file XML 20 KB và một file XML 10 GB có cùng cú pháp, nhưng cách xử lý tối ưu khác hoàn toàn.

Nếu load 10 GB thành DOM tree, memory usage có thể lớn hơn raw file nhiều lần. Vì vậy XML ecosystem có cả tree bộ phân tích cú pháp (parser) và xử lý theo luồng (streaming) bộ phân tích cú pháp (parser).

Ba mô hình bạn nên biết là DOM, SAX và StAX.

---

## 48. DOM

DOM bộ phân tích cú pháp (parser) đọc toàn bộ document rồi tạo tree trong memory.

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

Nhược điểm là memory cost. Mỗi phần tử (element) không chỉ chiếm bytes của source; còn có object overhead, strings, pointers, không gian tên (namespace) siêu dữ liệu (metadata) và child collections.

---

## 49. SAX

SAX là event-driven push bộ phân tích cú pháp (parser).

Thay vì đưa bạn tree, bộ phân tích cú pháp (parser) gọi callbacks kiểu:

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

Ưu điểm của SAX là memory rất thấp vì bộ phân tích cú pháp (parser) không cần giữ toàn tree. Nhược điểm là state management khó hơn. Nếu muốn biết “đang ở trong user nào, đã đọc field gì”, bạn phải tự giữ state.

---

## 50. StAX

StAX là xử lý theo luồng (streaming) pull bộ phân tích cú pháp (parser) phổ biến trong Java ecosystem.

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

Không nên chọn bộ phân tích cú pháp (parser) chỉ theo “cái nào nhanh nhất”. Hãy chọn theo access pattern và memory requirement.

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

`setNamespaceAware(true)` cực kỳ quan trọng nếu XML dùng các không gian tên (namespaces).

Tuy nhiên đoạn code này chưa phải secure bộ phân tích cú pháp (parser) configuration. External DTD/thực thể (entity) processing có thể cần disable hoặc control tùy implementation. Phần Senior sẽ giải thích vì sao.

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

Với namespaced XML, bạn cần `NamespaceContext` hoặc cơ chế tương đương để tiền tố (prefix) trong XPath map tới URI của không gian tên (không gian tên (namespace) URI).

Không hardcode tiền tố (prefix) source làm business identity.

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

Nếu output có cryptographic requirement, bạn còn phải phân biệt ordinary tuần tự hóa (serialization) với chuẩn hóa chính tắc (canonicalization).

Một XML serializer được thiết kế đúng tốt hơn nhiều so với nối string thủ công.

---

## 55. Marshal và unmarshal

Trong object ánh xạ/liên kết (binding) frameworks, bạn thường gặp hai từ:

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

Nhưng object model thường đơn giản hơn XML model. Mixed content, các không gian tên (namespaces), nil-vs-missing, order, repeating các phần tử (elements) và unknown extension đều có thể làm ánh xạ (mapping) mất nuance.

Vì vậy senior không nên nghĩ “có JAXB thì không cần hiểu XML”.

---

## 56. Schema kiểm tra tính hợp lệ (validation) nằm ở đâu trong flow?

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

Ví dụ lược đồ (schema) có thể nói `amount` là decimal dương, nhưng không biết user hiện tại có quyền transfer số tiền đó hay không. Authorization vẫn thuộc application.

---

## 57. Lỗi “lược đồ (schema) không tìm thấy declaration”

Đây là lỗi rất phổ biến. Bạn có lược đồ (schema) định nghĩa:

```text
{urn:order}order
```

nhưng input thực tế là:

```xml
<order>
```

không không gian tên (namespace).

Dù local name đều là `order`, tên mở rộng (expanded name) khác nhau.

Hoặc input có không gian tên mặc định (default không gian tên (namespace)) đúng nhưng XPath/lược đồ (schema) config không nhận biết không gian tên (namespace-aware).

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

và bộ phân tích cú pháp (parser)/validator tự fetch URL đó, attacker có thể ảnh hưởng network access.

Production application nên chủ động chọn lược đồ (schema) trusted, dùng local registry hoặc bộ phân giải (resolver). Instance hint không nên tự trở thành authority.

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

xử lý theo luồng (streaming) bộ phân tích cú pháp (parser) là lựa chọn tự nhiên.

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

Đặc biệt trong security-sensitive code, truy vấn (query) broad có thể chọn wrong node.

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

`o:order` thuộc không gian tên (namespace) `urn:order`. Attribute `id` không có không gian tên (namespace) vì nó unprefixed. `c:customer` và `c:name` thuộc `urn:common`. `sku` cũng không có không gian tên (namespace). `o:item` và `o:price` thuộc `urn:order`.

Nếu dùng XPath, bạn có thể tự bind:

```text
ord → urn:order
com → urn:common
```

rồi dùng:

```xpath
/ord:order/ord:item/ord:price
```

Prefix trong truy vấn (query) không cần giống tiền tố (prefix) source.

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

Bạn cũng phải hiểu rằng không gian tên (namespace) và lược đồ (schema) là hai lớp riêng. Namespace định danh vocabulary; lược đồ (schema) mô tả grammar/type của vocabulary.

Ở phần Senior, chúng ta sẽ thêm chuyển đổi (transformation), XQuery, tiến hóa lược đồ (lược đồ (schema) evolution), xử lý theo luồng (streaming) architecture, XXE, XML Catalog, chuẩn hóa chính tắc (canonicalization) và XML Signature.

---

# PHẦN BỔ SUNG SAU AUDIT — VALIDATION, NAMESPACE VÀ PARSER Ở MỨC THỰC CHIẾN

## 63. `xmlns=""`: reset không gian tên mặc định (default không gian tên (namespace)) trong subtree

Default không gian tên (namespace) có scope và có thể được reset. Ví dụ:

```xml
<root xmlns="urn:outer">
  <item>Outer</item>

  <legacy xmlns="">
    <item>Inner without namespace</item>
  </legacy>
</root>
```

`root` và `item` đầu thuộc `urn:outer`. Khi `legacy` khai báo `xmlns=""`, không gian tên mặc định (default không gian tên (namespace)) bị xóa cho subtree đó, nên `legacy` và `item` bên trong không còn không gian tên (namespace).

Đây là một source bug rất khó nhìn bằng mắt vì local names vẫn giống nhau. Khi DOM/XPath/lược đồ (schema) báo không match, hãy inspect URI của không gian tên (không gian tên (namespace) URI) thực thay vì chỉ nhìn tag text.

---

## 64. `attributeFormDefault` và local các thuộc tính (attributes)

Ngoài `elementFormDefault`, XSD còn có `attributeFormDefault`. Nó ảnh hưởng việc local các thuộc tính (attributes) có phải namespace-qualified hay không.

Nếu lược đồ (schema) có target không gian tên (namespace) nhưng một local thuộc tính (attribute) vẫn unqualified, instance có thể trông như:

```xml
<o:order
  xmlns:o="urn:order"
  id="123">
```

thay vì:

```xml
<o:order
  xmlns:o="urn:order"
  o:id="123">
```

Hai forms có expanded-name khác nhau. Khi validator báo thuộc tính (attribute) “không được phép” dù spelling `id` có vẻ đúng, hãy kiểm tra declaration là global/local và `attributeFormDefault`/`form` override của thuộc tính (attribute).

---

## 65. Global phần tử (element) và local phần tử (element) không chỉ khác vị trí trong file XSD

Element được khai báo trực tiếp dưới `xs:schema` là global declaration và có thể được reference/reuse theo lược đồ (schema) rules. Element nằm trong `complexType`/model group thường là local declaration.

Điều này ảnh hưởng không gian tên (namespace) qualification, reuse, substitution, code generation và cách bạn đọc lược đồ (schema) dependency graph. Khi debug Java generated classes, việc two các phần tử (elements) cùng local name nhưng đến từ declarations khác nhau có thể dẫn tới types/annotations khác nhau.

Senior lược đồ (schema) reading vì vậy nên đi từ root/global declarations rồi follow type/reference graph, không đọc XSD như một file XML tuyến tính từ trên xuống.

---

## 66. XPath có static context và dynamic context

Một XPath expression không tồn tại trong vacuum. Processor evaluate nó với **static context** và **dynamic context**.

Static context chứa những thứ như không gian tên (namespace) tiền tố (prefix) bindings, available functions, default function không gian tên (namespace) hoặc base URI tùy host/version. Dynamic context chứa context item/node, position, size, variable values và runtime data.

Vì vậy cùng expression:

```xpath
book/title
```

có thể trả kết quả khác hoàn toàn nếu context node khác. Đây là lý do code gọi XPath trên `Document` và code gọi cùng expression trên một `Element` không nhất thiết tương đương.

Khi debug XPath, đừng chỉ hỏi “expression đúng chưa?”. Hãy hỏi thêm “expression đang được evaluate từ node nào và không gian tên (namespace) context nào?”.

---

## 67. `local-name()` không phải cách chữa không gian tên (namespace) đúng mặc định

Developer đôi khi gặp default-namespace bug rồi viết:

```xpath
//*[local-name()='book']
```

Expression này có thể làm truy vấn (query) trả result, nhưng nó bỏ qua không gian tên (namespace) identity. Nếu document trộn `urn:catalog:book` và `urn:malicious:book`, cả hai đều có local name `book`.

Trong generic tooling, `local-name()` có use case thật. Nhưng business/bảo mật (security) truy vấn (query) nên bind URI của không gian tên (không gian tên (namespace) URI) đúng và dùng qualified XPath. “Làm cho truy vấn (query) chạy” không đồng nghĩa “truy vấn (query) đúng semantic”.

---

## 68. SAX `characters()` có thể được gọi nhiều lần cho một đoạn text

Một lỗi SAX rất phổ biến là nghĩ bộ phân tích cú pháp (parser) sẽ gọi `characters()` đúng một lần cho mỗi phần tử (element) text. API không đảm bảo như vậy. Text:

```xml
<name>Alice Wonderland</name>
```

có thể được deliver thành nhiều chunks tùy buffer/thực thể (entity)/bộ phân tích cú pháp (parser) implementation.

Handler đúng thường accumulate text trong `StringBuilder` giữa `startElement` và `endElement`, rồi xử lý khi phần tử (element) kết thúc. Không viết business logic giả định một callback tương ứng một value hoàn chỉnh.

Điểm này cho thấy xử lý theo luồng (streaming) bộ phân tích cú pháp (parser) expose **events/chunks**, không expose object fields sẵn như ánh xạ/liên kết (binding) framework.

---

## 69. StAX event model và nhận biết không gian tên (namespace-aware) reading

Với StAX, application chủ động pull events như `START_ELEMENT`, `CHARACTERS`, `END_ELEMENT`. Khi gặp `START_ELEMENT`, hãy đọc `QName`/URI của không gian tên (không gian tên (namespace) URI)/local part thay vì chỉ `getLocalName()` nếu vocabulary có không gian tên (namespace).

Text cũng có thể cần accumulate qua nhiều character events. Whitespace events, comments hoặc CDATA representation có thể xuất hiện tùy reader API/config. Vì vậy một state machine tốt xác định rõ “đang ở phần tử (element) nào”, “đang thu field nào”, và chỉ finalize value khi gặp end phần tử (element) tương ứng.

Streaming code có ít memory nhưng đổi lại bạn phải quản lý state chính xác hơn DOM.

---

## 70. XSD kiểm tra tính hợp lệ (validation) trong Java: `SchemaFactory` → `Schema` → `Validator`

Mental model Java điển hình là compile XSD thành `Schema`, rồi tạo `Validator` cho kiểm tra tính hợp lệ (validation) operation:

```java
SchemaFactory factory =
    SchemaFactory.newInstance(
        XMLConstants.W3C_XML_SCHEMA_NS_URI
    );

Schema schema = factory.newSchema(xsdFile);
Validator validator = schema.newValidator();

validator.validate(new StreamSource(xmlFile));
```

`SchemaFactory` xử lý lược đồ (schema) language/compilation. `Schema` đại diện compiled lược đồ (schema) model có thể được reuse theo contract của implementation/API. `Validator` là object dùng để validate một source và thường không nên được share tùy tiện giữa concurrent operations nếu API không cam kết thread-safety.

Production code còn phải kiểm soát external lược đồ (schema)/DTD access và bộ phân giải (resolver); ví dụ code ngắn ở trên chỉ minh họa lifecycle, chưa phải security-hardening recipe hoàn chỉnh.

---

## 71. Validation error model: warning, error, fatal error và line/column

XML APIs thường expose lỗi kèm locator information như line và column. Với SAX-style `ErrorHandler`, bạn có các mức như warning, error và fatal error theo bộ phân tích cú pháp (parser)/validator semantics.

Well-formedness violation thường là fatal ở XML phân tích cú pháp (parsing) layer: bộ phân tích cú pháp (parser) không thể tiếp tục như HTML trình duyệt (browser) phục hồi lỗi (error recovery). Schema kiểm tra tính hợp lệ (validation) error nghĩa document đã có thể parse XML nhưng không thỏa contract XSD/DTD.

Khi đưa error ra application log/API response, nên preserve layer và location nếu an toàn:

```text
XML_PARSE_ERROR at line 12, column 18
XSD_VALIDATION_ERROR at /order/item[3]/price
```

để developer không mất thời gian tìm lỗi lược đồ (schema) trong khi document còn chưa đúng cú pháp XML (well-formed). Với sensitive payload, log context vừa đủ chứ không dump toàn document.

---

## 72. Validation không nên bị trộn với business kiểm tra tính hợp lệ (validation)

Một chuỗi xử lý (pipeline) rõ ràng thường phân tầng:

```text
bytes / transport checks
→ secure XML parsing
→ namespace-aware processing
→ XSD/DTD validation nếu contract yêu cầu
→ object/domain mapping
→ business validation
→ authorization
```

XSD có thể kiểm tra `amount` là decimal, positive và đúng cardinality. Nhưng nó không biết account hiện tại có đủ balance hay user có quyền chuyển tiền. Ngược lại, business validator không nên phải tự kiểm tra XML tag đóng đúng hay không gian tên (namespace) có đúng contract hay không.

Phân tầng làm error message rõ hơn, test dễ hơn và giảm nguy cơ một layer “tin” dữ liệu mà layer trước chưa kiểm tra.

---

## 73. Validate trước ánh xạ (mapping) hay validate trong lúc ánh xạ (mapping)?

Không có một chuỗi xử lý (pipeline) duy nhất cho mọi library. Có hệ thống parse/validate rồi mới unmarshal; có ánh xạ/liên kết (binding) framework tích hợp lược đồ (schema) kiểm tra tính hợp lệ (validation) trong unmarshal; có xử lý theo luồng (streaming) chuỗi xử lý (pipeline) validate và consume gần như cùng lúc.

Điều quan trọng là outcome phải rõ: **business layer chỉ nhận data sau khi structural contract cần thiết đã được kiểm tra**. Nếu hiệu năng (performance) khiến bạn tránh parse hai lần, hãy thiết kế chuỗi xử lý (pipeline) xử lý theo luồng (streaming)/Source/handler phù hợp thay vì bỏ kiểm tra tính hợp lệ (validation) mà không nhận ra.

Với file cực lớn, việc build DOM chỉ để validate rồi build lần hai để process là dấu hiệu architecture cần xem lại.

---

## 74. Test XML bộ phân tích cú pháp (parser)/validator bằng negative cases, không chỉ happy path

Một test suite tốt không chỉ có một file valid. Hãy có fixtures cho wrong không gian tên (namespace), missing required phần tử (element), wrong order, invalid datatype, nil/empty/missing, duplicate ID, unexpected extension, malformed XML, huge text node, deep nesting và external-entity payload.

Mục tiêu không phải “test XML Standard”, mà là verify **exact bộ phân tích cú pháp (parser) + exact configuration + exact lược đồ (schema) version** của application xử lý boundary như bạn nghĩ. Parser defaults và implementation version khác nhau có thể thay behavior bảo mật (security)/hiệu năng (performance).

---

## 75. Mental model Intermediate sau audit

Sau khi bổ sung các phần trên, flow nên được hiểu như sau:

```text
bytes
→ decode
→ well-formed XML parse
→ namespace expansion
→ optional DTD/schema resolution có kiểm soát
→ optional structural/type validation
→ DOM hoặc SAX/StAX event stream
→ XPath/query với đúng context
→ mapping/domain
→ business validation
```

Namespace trả lời **node thuộc vocabulary nào**. Schema trả lời **vocabulary đó cho phép cấu trúc/type nào**. Parser model trả lời **application nhận tree hay stream events**. XPath trả lời **cách chọn/tính trên model đó**. Business kiểm tra tính hợp lệ (validation) trả lời **data hợp domain và quyền hay không**.

Nếu bạn tách được năm câu hỏi này trong đầu, bạn đã qua được phần dễ nhầm nhất của XML Intermediate.
