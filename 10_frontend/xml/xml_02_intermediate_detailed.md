# XML — Intermediate
## Namespace, DTD, XML Schema, XPath và các mô hình Parser

Tài liệu này tiếp nối phần Beginner. Ở phần trước, bạn đã biết XML là một cây dữ liệu strict, biết phần tử, thuộc tính, văn bản, mã hóa ký tự, CDATA và khái niệm đúng cú pháp XML. Tuy nhiên chỉ biết cú pháp XML chưa đủ để dùng XML trong hệ thống thật. Khi nhiều bộ từ vựng được trộn với nhau, bạn cần không gian tên. Khi muốn kiểm tra XML có đúng cấu trúc hay không, bạn cần DTD hoặc XML Schema. Khi muốn tìm dữ liệu trong cây, bạn cần XPath. Khi tài liệu nhỏ hoặc rất lớn, bạn phải chọn DOM, SAX hoặc StAX phù hợp.

Phần Intermediate được viết theo đúng flow đó để bạn hiểu vì sao từng lớp tồn tại.


## Quy ước thuật ngữ trong tài liệu

Tài liệu dùng tiếng Việt tự nhiên làm ngôn ngữ giải thích chính và giữ thuật ngữ gốc ở lần định nghĩa để tiện tra cứu. Các cách gọi được dùng thống nhất gồm: **tài liệu XML (XML document)**, **phần tử (element)**, **thuộc tính (attribute)**, **phần tử gốc (root element)**, **nút văn bản (text node)**, **không gian tên (namespace)**, **tiền tố (prefix)**, **tên mở rộng (expanded name)**, **bộ từ vựng (vocabulary)**, **lược đồ (schema)**, **giao thức (protocol)**, **quy tắc nghiệp vụ (business rule)**, **đúng cú pháp XML (well-formed)**, **kiểm tra tính hợp lệ (validation)**, **phân tích cú pháp (parsing)**, **bộ phân tích cú pháp (parser)**, **xử lý theo luồng (streaming)**, **luồng (stream)**, **truy vấn (query)**, **chuyển đổi (transformation)**, **ánh xạ/liên kết (binding)**, **tuần tự hóa (serialization)**, **bộ tuần tự hóa (serializer)** và **chuẩn hóa chính tắc (canonicalization/C14N)**. Sau khi đã định nghĩa ở đây, nội dung bên dưới ưu tiên cách gọi tiếng Việt để tránh lặp ngoặc tiếng Anh quá dày. Các tên chuẩn như XML, DTD, XSD, XPath, XSLT, XQuery, DOM, SAX, StAX, SOAP, WSDL, QName, PSVI, CDATA và tên API cụ thể được giữ nguyên.

---

## 1. Vấn đề name collision và lý do XML Namespace xuất hiện

Giả sử hệ thống của bạn cần kết hợp dữ liệu từ hai domain. Một domain nói về HTML-like tài liệu và một domain nói về furniture inventory. Cả hai đều dùng phần tử tên `table`:

```xml
<document>
  <table>...</table>
  <table>...</table>
</document>
```

Nhìn vào XML này, ứng dụng không biết `table` đầu tiên và `table` thứ hai thuộc bộ từ vựng nào.

XML Namespace giải quyết vấn đề bằng cách làm cho tên logic của phần tử không còn chỉ là local name `table`. Identity thật được xem như cặp:

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

Bây giờ hai phần tử có local name giống nhau nhưng không gian tên khác nhau, vì vậy ứng dụng phân biệt được hoàn toàn.

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

có tiền tố khác nhau, nhưng cùng URI của không gian tên (không gian tên URI) và local name. Về nhận biết định danh không gian tên, cả hai là cùng một tên mở rộng:

```text
{https://example.com/user}user
```

Điều này có nghĩa khi code Java, XPath, XSLT hoặc lược đồ xử lý XML, bạn không nên so sánh string tiền tố `a` hoặc `u` để xác định business meaning. Prefix có thể đổi tự do miễn nó vẫn bind tới cùng URI của không gian tên (không gian tên URI).

Một XML bộ tuần tự hóa thậm chí có thể đọc input tiền tố `a` rồi serialize output thành `ns1` mà semantics vẫn không đổi.

---

## 3. Expanded name

Expanded name là mental model bạn nên dùng mọi lúc khi gặp không gian tên.

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

Khi bảo mật (security) hoặc business logic match phần tử, cách đúng về tư duy là match URI của không gian tên (không gian tên URI) và local name, không match raw tag string.

---

## 4. Default không gian tên

Nếu không muốn viết tiền tố lặp lại, XML cho phép không gian tên mặc định (default không gian tên):

```xml
<catalog xmlns="https://example.com/catalog">
  <book>
    <title>XML</title>
  </book>
</catalog>
```

Trong subtree này, các unprefixed các phần tử `catalog`, `book`, `title` thuộc không gian tên `https://example.com/catalog`.

Điều này làm XML dễ đọc hơn, nhưng cũng gây một trong những bug XPath phổ biến nhất: developer thấy source không có tiền tố nên tưởng phần tử “không không gian tên”. Thực tế chúng đang nằm trong không gian tên mặc định (default không gian tên).

---

## 5. Default không gian tên không áp dụng cho unprefixed các thuộc tính

Đây là quy tắc phải thuộc lòng.

Xét:

```xml
<book
  xmlns="https://example.com/catalog"
  id="B001"/>
```

Element `book` thuộc không gian tên:

```text
https://example.com/catalog
```

Nhưng thuộc tính `id` không có không gian tên.

Nếu bạn muốn namespaced thuộc tính, phải viết tiền tố rõ:

```xml
<book
  xmlns="https://example.com/catalog"
  xmlns:app="https://example.com/app"
  app:id="B001"/>
```

Bây giờ `app:id` thuộc không gian tên `https://example.com/app`.

Điểm này rất quan trọng với XPath, DOM, XML Signature và ánh xạ/liên kết các framework.

---

## 6. Namespace scope và redeclaration

Namespace tiền tố ánh xạ/liên kết có scope.

```xml
<root xmlns:p="urn:a">
  <p:item/>

  <section xmlns:p="urn:b">
    <p:item/>
  </section>
</root>
```

`p:item` đầu tiên thuộc `urn:a`, còn `p:item` bên trong `section` thuộc `urn:b`.

Vì vậy không được scan một file rồi kết luận “tiền tố `p` luôn nghĩa urn:a”. Binding phải được resolve theo ngữ cảnh.

---

## 7. Namespace URI có bắt buộc phải mở được như URL không?

Không. Namespace URI là định danh. Nó có thể nhìn giống URL:

```text
https://example.com/order
```

hoặc là URN:

```text
urn:example:order
```

Processor không bắt buộc phải download lược đồ từ URI của không gian tên (không gian tên URI).

Một sai lầm phổ biến là nghĩ rằng `xmlns="https://example.com/order"` nghĩa trình duyệt (browser) hoặc bộ phân tích cú pháp sẽ truy cập URL này. Không phải. Schema location và định danh không gian tên là hai khái niệm khác nhau.

---

## 8. Prefix `xml`

Prefix `xml` được dành sẵn cho XML không gian tên chuẩn và dùng trong:

```xml
xml:lang
xml:space
xml:base
xml:id
```

Bạn không được tự redefine `xml` sang không gian tên của mình.

---

## 9. Tại sao chỉ đúng cú pháp XML vẫn chưa đủ?

XML core chỉ kiểm tra cú pháp. Ví dụ:

```xml
<order>
  <banana>Hello</banana>
  <total>abc</total>
</order>
```

có thể hoàn toàn đúng cú pháp XML.

Nhưng ứng dụng có thể yêu cầu `order` phải có `id`, `customer`, `total`, và `total` phải là decimal. Để diễn tả grammar hoặc contract đó, XML ecosystem dùng các lược đồ languages. Hai công nghệ bạn cần hiểu trước tiên là DTD và XSD.

---

# DTD

## 10. DTD là gì?

DTD là **Document Type Definition**. Đây là cơ chế lược đồ cổ điển đi cùng XML từ rất sớm.

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

DTD có thể nằm trong chính tài liệu:

```xml
<!DOCTYPE note [
  <!ELEMENT note (#PCDATA)>
]>
```

hoặc reference external file:

```xml
<!DOCTYPE note SYSTEM "note.dtd">
```

External DTD rất quan trọng về bảo mật (security). Nếu bộ phân tích cú pháp được phép tự fetch URI hoặc file từ DTD của untrusted input, attacker có thể lợi dụng thực thể ngoài (external thực thể) hoặc external subset để đọc file, SSRF hoặc gây denial of service. Phần Senior sẽ đi sâu vào XXE.

---

## 12. `ELEMENT` declaration

DTD có thể định nghĩa child sequence:

```dtd
<!ELEMENT user (name,email)>
```

Điều này có nghĩa `user` cần `name` rồi đến `email`.

Nếu order đảo lại, tài liệu có thể invalid theo DTD dù vẫn đúng cú pháp XML.

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

DTD cũng hỗ trợ nội dung hỗn hợp, ví dụ:

```dtd
<!ELEMENT p (#PCDATA|em|strong)*>
```

cho phép văn bản xen `em` và `strong`.

---

## 16. `ATTLIST`

DTD có thể định nghĩa các thuộc tính:

```dtd
<!ATTLIST user
  id ID #REQUIRED
  active (true|false) "true">
```

Ở đây `id` là thuộc tính có type `ID` và bắt buộc. `active` chỉ nhận `true` hoặc `false`, mặc định là `true`.

Các từ khóa thường gặp gồm `#REQUIRED`, `#IMPLIED` và `#FIXED`.

---

## 17. Entities trong DTD

Bạn có thể define thực thể:

```dtd
<!ENTITY company "Acme Corporation">
```

sau đó dùng:

```xml
<name>&company;</name>
```

Parser có thể expand `&company;` thành văn bản.

Entity system rất mạnh nhưng cũng là lý do DTD trở thành bề mặt tấn công. External các thực thể, parameter các thực thể và thực thể expansion đều cần được control trong production.

---

## 18. Vì sao DTD không đủ cho nhiều hệ thống doanh nghiệp?

DTD có khả năng mô tả cấu trúc nhưng hệ kiểu hạn chế, không gian tên integration không tự nhiên và syntax riêng. Khi cần decimal, dateTime, typed các thuộc tính, reusable complex type hoặc advanced constraints, XSD thường phù hợp hơn.

DTD vẫn tồn tại trong nhiều publishing/tài liệu systems và hệ thống cũ standards, nên senior phải đọc được, nhưng với ứng dụng contract mới, XSD phổ biến hơn.

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

Namespace `http://www.w3.org/2001/XMLSchema` là bộ từ vựng của XML Schema.

XSD không chỉ nói phần tử nào được nằm ở đâu. Nó còn có hệ thống data types, reusable types, restrictions, không gian tên integration và ràng buộc định danh.

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

Bây giờ `price` không còn chỉ là arbitrary văn bản về mặt lược đồ. Schema validator có thể kiểm tra lexical value có hợp `xs:decimal` hay không.

---

## 21. Simple type và complex type

Một simple phần tử có thể khai báo trực tiếp:

```xml
<xs:element
  name="name"
  type="xs:string"/>
```

Complex type dùng khi phần tử có các phần tử con hoặc các thuộc tính:

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

`user` không chỉ là một scalar value; nó là một cấu trúc.

---

## 22. `xs:sequence`

`xs:sequence` nói rằng child các phần tử phải xuất hiện theo thứ tự.

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

Đây là điều cần nhớ khi version XML contract: nếu lược đồ dùng strict sequence, chèn phần tử mới vào sai vị trí có thể làm bên tiêu thụ cũ fail.

---

## 23. `xs:choice`

```xml
<xs:choice>
  <xs:element name="email"/>
  <xs:element name="phone"/>
</xs:choice>
```

Nghĩa là chọn một branch.

Choice rất hữu ích cho union-like structures nhưng nếu lồng nhau choice quá sâu, lược đồ sẽ khó đọc và ánh xạ/liên kết code cũng phức tạp.

---

## 24. `xs:all`

`xs:all` được dùng khi một nhóm các phần tử có thể xuất hiện với order linh hoạt hơn `sequence`, trong constraints mà XSD version quy định.

Điểm quan trọng là đừng nghĩ `xs:all` nghĩa “bất kỳ thứ gì, bao nhiêu lần cũng được”. Nó vẫn có quy tắc về các phần tử con và occurrence. Nếu cần repeating arbitrary structures, bạn phải đọc đúng XSD model thay vì suy từ tên `all`.

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

Đây là lý do khi đọc XSD bạn phải chú ý defaults, không chỉ những thuộc tính xuất hiện.

---

## 26. XSD thuộc tính declaration

```xml
<xs:attribute
  name="id"
  type="xs:string"
  use="required"/>
```

`use="required"` bắt buộc thuộc tính tồn tại.

Các cases khác có thể là optional hoặc prohibited tùy ngữ cảnh.

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

Nhưng hãy nhớ rằng thêm hoặc xóa enum value có thể là breaking contract đối với được sinh tự động clients.

---

## 29. Pattern

```xml
<xs:pattern value="[A-Z]{2}[0-9]{4}"/>
```

Pattern trong XML Schema dùng regex dialect riêng. Bạn không nên copy Java regex hoặc JavaScript regex rồi assume chúng tương đương hoàn toàn.

Nếu pattern là business-critical, đọc các quy tắc của XSD regex và test bằng đúng bộ xử lý lược đồ.

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

Named type hợp khi cấu trúc được reuse hoặc version độc lập. Anonymous type hợp với one-off local cấu trúc.

Việc chọn kiểu nào là một phần của lược đồ design pattern, phần Master sẽ nói sâu hơn.

---

## 31. `targetNamespace`

Một lược đồ thường định nghĩa bộ từ vựng trong một không gian tên cụ thể:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="https://example.com/order"
  xmlns:o="https://example.com/order">
```

`targetNamespace` trả lời câu hỏi: “Các global lược đồ components này thuộc bộ từ vựng không gian tên nào?”

Nếu hiểu sai `targetNamespace`, bạn sẽ gặp lỗi kiểu lược đồ nói `order` tồn tại nhưng validator báo “cannot find declaration” vì instance phần tử không ở không gian tên đúng.

---

## 32. `elementFormDefault`

Một lược đồ có thể khai báo:

```xml
elementFormDefault="qualified"
```

Điều này ảnh hưởng local các phần tử có cần không gian tên qualification hay không.

Đây là một trong những điểm gây lỗi nhiều nhất khi làm SOAP/XSD Java ánh xạ/liên kết. Một instance nhìn gần giống nhau nhưng khác không gian tên qualification có thể invalid hoàn toàn.

Khi debug, luôn xem cùng lúc:

```text
targetNamespace
elementFormDefault
namespace declarations của instance
```

---

## 33. `xs:include` và `xs:import`

`xs:include` thường dùng để compose lược đồ components trong cùng không gian tên family/ngữ cảnh:

```xml
<xs:include schemaLocation="common.xsd"/>
```

`xs:import` dùng để đưa lược đồ components thuộc không gian tên khác vào:

```xml
<xs:import
  namespace="https://example.com/common"
  schemaLocation="common.xsd"/>
```

Một quy tắc mental model dễ nhớ là:

```text
same namespace → include
different namespace → import
```

Dù thực tế XSD có thêm details, mental model này đủ tốt để bắt đầu.

---

## 34. `xsi:schemaLocation`

XML instance có thể chứa lược đồ location hints:

```xml
<order
  xmlns="https://example.com/order"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
    https://example.com/order
    order.xsd">
```

Đây là hint ánh xạ không gian tên tới lược đồ location.

Điều quan trọng về bảo mật (security) là ứng dụng không nên mặc định tin và fetch arbitrary lược đồ URL từ untrusted tài liệu. Resolver và lược đồ source nên do ứng dụng kiểm soát.

---

## 35. `xsi:noNamespaceSchemaLocation`

Nếu bộ từ vựng không có không gian tên, instance có thể dùng:

```xml
xsi:noNamespaceSchemaLocation="note.xsd"
```

Nó vẫn là lược đồ location hint, không biến untrusted URL thành trusted dependency.

---

## 36. `xsi:nil`

Ví dụ:

```xml
<middleName
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:nil="true"/>
```

Nếu lược đồ declaration cho phép `nillable`, phần tử có thể biểu diễn nil.

Bạn phải phân biệt ba trạng thái:

```xml
<middleName xsi:nil="true"/>
```

```xml
<middleName></middleName>
```

và phần tử hoàn toàn không xuất hiện.

Nil, empty và missing có thể có business meaning khác nhau. Đây là lý do đối tượng ánh xạ XML sang Java `null` đôi khi làm mất thông tin nếu ánh xạ không cẩn thận.

---

# XPath

## 37. XPath là gì?

XPath là ngôn ngữ expression/truy vấn dùng để chọn hoặc tính toán dựa trên XML/XDM.

Ví dụ tài liệu:

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

chọn các `title` các phần tử.

Bạn nên hình dung XPath như “đường đi + điều kiện” trên tree, nhưng modern XPath còn mạnh hơn nhiều và có hệ kiểu, functions, sequences.

---

## 38. Absolute path

```xpath
/library/book
```

đi từ tài liệu/root ngữ cảnh tới `library`, sau đó child `book`.

---

## 39. `//`

```xpath
//book
```

là shorthand liên quan descendant-or-self traversal.

Nó rất tiện nhưng dễ bị lạm dụng. Trên XML lớn, truy vấn quá rộng khó reason và có thể tốn tài nguyên. Nếu biết path rõ, path explicit thường tốt hơn.

---

## 40. Attribute selection

```xpath
/library/book/@id
```

chọn `id` các thuộc tính.

---

## 41. Predicate

```xpath
/library/book[@id='2']
```

chọn book có thuộc tính id bằng `2`.

Predicate có thể dùng expression phức tạp hơn, không chỉ thuộc tính equality.

---

## 42. Position

```xpath
/library/book[1]
```

chọn first book trong ngữ cảnh phù hợp.

```xpath
/library/book[last()]
```

chọn last book.

Khi dùng position với `//` hoặc grouped expressions, ngữ cảnh có thể khác điều bạn nghĩ. Đây là lý do senior XPath cần hiểu expression evaluation thay vì chỉ ghi nhớ syntax.

---

## 43. `text()`

```xpath
/library/book/title/text()
```

chọn direct các nút văn bản của `title`.

Trong nội dung hỗn hợp:

```xml
<p>Hello <b>world</b>!</p>
```

`p/text()` chỉ chọn direct các nút văn bản `"Hello "` và `"!"`, không tự trả văn bản trong `<b>`.

String-value của `p` có thể là `"Hello world!"` theo XPath mô hình dữ liệu.

Đây là khác biệt rất quan trọng.

---

## 44. Wildcard

```xpath
/library/*
```

chọn các phần tử con.

```xpath
//@*
```

có thể chọn rất rộng các các thuộc tính.

Wildcard useful nhưng làm truy vấn ít explicit hơn, nên chỉ dùng khi bộ từ vựng thực sự cần generic handling.

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

## 46. Default không gian tên và bug XPath nổi tiếng

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

Lý do là `library` và `book` thuộc không gian tên `https://example.com/books`. Trong nhiều XPath host APIs, unprefixed name trong expression không tự map tới không gian tên mặc định (default không gian tên) của source tài liệu.

Bạn cần bind một tiền tố của riêng mình:

```text
b → https://example.com/books
```

sau đó truy vấn:

```xpath
/b:library/b:book
```

Prefix `b` không cần xuất hiện trong source XML. Nó chỉ cần map tới đúng URI của không gian tên (không gian tên URI).

Đây là nguyên tắc quan trọng nhất khi debug XPath không gian tên.

---

# Các mô hình phân tích cú pháp (Parser Models)

## 47. Vì sao phải có nhiều loại bộ phân tích cú pháp?

Một file XML 20 KB và một file XML 10 GB có cùng cú pháp, nhưng cách xử lý tối ưu khác hoàn toàn.

Nếu load 10 GB thành DOM tree, memory usage có thể lớn hơn raw file nhiều lần. Vì vậy XML ecosystem có cả tree bộ phân tích cú pháp và xử lý theo luồng bộ phân tích cú pháp.

Ba mô hình bạn nên biết là DOM, SAX và StAX.

---

## 48. DOM

DOM bộ phân tích cú pháp đọc toàn bộ tài liệu rồi tạo tree trong memory.

Lợi ích là bạn có thể nhảy tới bất kỳ nút nào, dùng XPath thuận tiện, mutate tree và serialize lại.

Ví dụ mental model Java:

```java
Document doc = builder.parse(file);
```

sau đó:

```java
Element root = doc.getDocumentElement();
```

DOM rất dễ dùng với XML nhỏ và vừa.

Nhược điểm là memory cost. Mỗi phần tử không chỉ chiếm bytes của source; còn có đối tượng overhead, strings, pointers, không gian tên siêu dữ liệu (metadata) và child collections.

---

## 49. SAX

SAX là event-driven push bộ phân tích cú pháp.

Thay vì đưa bạn tree, bộ phân tích cú pháp gọi callbacks kiểu:

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

ứng dụng có thể nhận một chuỗi events tương ứng.

Ưu điểm của SAX là memory rất thấp vì bộ phân tích cú pháp không cần giữ toàn tree. Nhược điểm là state management khó hơn. Nếu muốn biết “đang ở trong user nào, đã đọc trường dữ liệu gì”, bạn phải tự giữ state.

---

## 50. StAX

StAX là xử lý theo luồng pull bộ phân tích cú pháp phổ biến trong Java ecosystem.

Khác SAX gọi ngược vào ứng dụng, StAX cho ứng dụng chủ động yêu cầu event tiếp theo.

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

Trong Java business ứng dụng, StAX thường là lựa chọn thuận tiện cho large XML vì pull model dễ viết state machine.

Không nên chọn bộ phân tích cú pháp chỉ theo “cái nào nhanh nhất”. Hãy chọn theo access pattern và memory requirement.

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

`setNamespaceAware(true)` cực kỳ quan trọng nếu XML dùng các không gian tên.

Tuy nhiên đoạn code này chưa phải secure cấu hình bộ phân tích cú phápuration. External DTD/thực thể processing có thể cần disable hoặc control tùy implementation. Phần Senior sẽ giải thích vì sao.

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

Với namespaced XML, bạn cần `NamespaceContext` hoặc cơ chế tương đương để tiền tố trong XPath map tới URI của không gian tên (không gian tên URI).

Không hardcode tiền tố source làm business identity.

---

## 54. Serialization

Sau khi tạo hoặc sửa XML tree, bạn có thể serialize nó thành bytes/văn bản.

Serialization phải xử lý đúng:

```text
encoding
escaping
namespace declarations
XML declaration
empty elements
text
```

Nếu output có cryptographic requirement, bạn còn phải phân biệt ordinary tuần tự hóa với chuẩn hóa chính tắc.

Một XML bộ tuần tự hóa được thiết kế đúng tốt hơn nhiều so với nối string thủ công.

---

## 55. Marshal và unmarshal

Trong đối tượng ánh xạ/liên kết các framework, bạn thường gặp hai từ:

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

có thể map thành Java đối tượng `User`.

Nhưng đối tượng model thường đơn giản hơn XML model. Mixed content, các không gian tên, nil-vs-missing, order, repeating các phần tử và unknown extension đều có thể làm ánh xạ mất nuance.

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

XSD kiểm tra structural/type các quy tắc. Nó không thay business logic.

Ví dụ lược đồ có thể nói `amount` là decimal dương, nhưng không biết user hiện tại có quyền transfer số tiền đó hay không. Authorization vẫn thuộc ứng dụng.

---

## 57. Lỗi “lược đồ không tìm thấy declaration”

Đây là lỗi rất phổ biến. Bạn có lược đồ định nghĩa:

```text
{urn:order}order
```

nhưng input thực tế là:

```xml
<order>
```

không không gian tên.

Dù local name đều là `order`, tên mở rộng khác nhau.

Hoặc input có không gian tên mặc định (default không gian tên) đúng nhưng XPath/lược đồ config không nhận biết không gian tên.

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

và bộ phân tích cú pháp/validator tự fetch URL đó, attacker có thể ảnh hưởng network access.

Production ứng dụng nên chủ động chọn lược đồ trusted, dùng local registry hoặc bộ phân giải. Instance hint không nên tự trở thành authority.

---

## 59. Anti-pattern: DOM cho file khổng lồ

Nếu input 5 GB, DOM có thể consume memory nhiều lần 5 GB và gây OutOfMemoryError.

Khi data có cấu trúc kiểu:

```xml
<records>
  <record>...</record>
  <record>...</record>
  ...
</records>
```

xử lý theo luồng bộ phân tích cú pháp là lựa chọn tự nhiên.

---

## 60. Anti-pattern: XPath `//` ở mọi nơi

Query:

```xpath
//price
```

có thể match price ở nhiều ngữ cảnh ngoài ý muốn.

Nếu bộ từ vựng biết rõ:

```xpath
/order/items/item/price
```

thường an toàn và dễ review hơn.

Đặc biệt trong security-sensitive code, truy vấn broad có thể chọn wrong nút.

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

`o:order` thuộc không gian tên `urn:order`. Attribute `id` không có không gian tên vì nó unprefixed. `c:customer` và `c:name` thuộc `urn:common`. `sku` cũng không có không gian tên. `o:item` và `o:price` thuộc `urn:order`.

Nếu dùng XPath, bạn có thể tự bind:

```text
ord → urn:order
com → urn:common
```

rồi dùng:

```xpath
/ord:order/ord:item/ord:price
```

Prefix trong truy vấn không cần giống tiền tố source.

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

Bạn cũng phải hiểu rằng không gian tên và lược đồ là hai lớp riêng. Namespace định danh bộ từ vựng; lược đồ mô tả grammar/type của bộ từ vựng.

Ở phần Senior, chúng ta sẽ thêm chuyển đổi, XQuery, tiến hóa lược đồ (lược đồ evolution), xử lý theo luồng architecture, XXE, XML Catalog, chuẩn hóa chính tắc và XML Signature.

---

# PHẦN BỔ SUNG SAU AUDIT — VALIDATION, NAMESPACE VÀ PARSER Ở MỨC THỰC CHIẾN

## 63. `xmlns=""`: reset không gian tên mặc định (default không gian tên) trong subtree

Default không gian tên có scope và có thể được reset. Ví dụ:

```xml
<root xmlns="urn:outer">
  <item>Outer</item>

  <legacy xmlns="">
    <item>Inner without namespace</item>
  </legacy>
</root>
```

`root` và `item` đầu thuộc `urn:outer`. Khi `legacy` khai báo `xmlns=""`, không gian tên mặc định (default không gian tên) bị xóa cho subtree đó, nên `legacy` và `item` bên trong không còn không gian tên.

Đây là một source bug rất khó nhìn bằng mắt vì local names vẫn giống nhau. Khi DOM/XPath/lược đồ báo không match, hãy inspect URI của không gian tên (không gian tên URI) thực thay vì chỉ nhìn tag văn bản.

---

## 64. `attributeFormDefault` và local các thuộc tính

Ngoài `elementFormDefault`, XSD còn có `attributeFormDefault`. Nó ảnh hưởng việc local các thuộc tính có phải namespace-qualified hay không.

Nếu lược đồ có target không gian tên nhưng một local thuộc tính vẫn unqualified, instance có thể trông như:

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

Hai forms có expanded-name khác nhau. Khi validator báo thuộc tính “không được phép” dù spelling `id` có vẻ đúng, hãy kiểm tra declaration là global/local và `attributeFormDefault`/`form` override của thuộc tính.

---

## 65. Global phần tử và local phần tử không chỉ khác vị trí trong file XSD

Element được khai báo trực tiếp dưới `xs:schema` là global declaration và có thể được reference/reuse theo quy tắc lược đồ. Element nằm trong `complexType`/model group thường là local declaration.

Điều này ảnh hưởng không gian tên qualification, reuse, substitution, code generation và cách bạn đọc lược đồ dependency graph. Khi debug Java được sinh tự động classes, việc two các phần tử cùng local name nhưng đến từ declarations khác nhau có thể dẫn tới types/annotations khác nhau.

Senior lược đồ reading vì vậy nên đi từ root/global declarations rồi follow type/reference graph, không đọc XSD như một file XML tuyến tính từ trên xuống.

---

## 66. XPath có static ngữ cảnh và dynamic ngữ cảnh

Một XPath expression không tồn tại trong vacuum. Processor evaluate nó với **static ngữ cảnh** và **dynamic ngữ cảnh**.

Static ngữ cảnh chứa những thứ như không gian tên tiền tố bindings, available functions, default function không gian tên hoặc base URI tùy host/version. Dynamic ngữ cảnh chứa ngữ cảnh item/nút, position, size, variable values và thời gian chạy data.

Vì vậy cùng expression:

```xpath
book/title
```

có thể trả kết quả khác hoàn toàn nếu ngữ cảnh nút khác. Đây là lý do code gọi XPath trên `Document` và code gọi cùng expression trên một `Element` không nhất thiết tương đương.

Khi debug XPath, đừng chỉ hỏi “expression đúng chưa?”. Hãy hỏi thêm “expression đang được evaluate từ nút nào và không gian tên ngữ cảnh nào?”.

---

## 67. `local-name()` không phải cách chữa không gian tên đúng mặc định

Developer đôi khi gặp default-namespace bug rồi viết:

```xpath
//*[local-name()='book']
```

Expression này có thể làm truy vấn trả result, nhưng nó bỏ qua định danh không gian tên. Nếu tài liệu trộn `urn:catalog:book` và `urn:malicious:book`, cả hai đều có local name `book`.

Trong generic tooling, `local-name()` có use case thật. Nhưng business/bảo mật (security) truy vấn nên bind URI của không gian tên (không gian tên URI) đúng và dùng qualified XPath. “Làm cho truy vấn chạy” không đồng nghĩa “truy vấn đúng semantic”.

---

## 68. SAX `characters()` có thể được gọi nhiều lần cho một đoạn văn bản

Một lỗi SAX rất phổ biến là nghĩ bộ phân tích cú pháp sẽ gọi `characters()` đúng một lần cho mỗi phần tử văn bản. API không đảm bảo như vậy. Text:

```xml
<name>Alice Wonderland</name>
```

có thể được deliver thành nhiều chunks tùy buffer/thực thể/bộ phân tích cú pháp implementation.

Handler đúng thường accumulate văn bản trong `StringBuilder` giữa `startElement` và `endElement`, rồi xử lý khi phần tử kết thúc. Không viết business logic giả định một callback tương ứng một value hoàn chỉnh.

Điểm này cho thấy xử lý theo luồng bộ phân tích cú pháp expose **events/chunks**, không expose đối tượng các trường dữ liệu sẵn như ánh xạ/liên kết framework.

---

## 69. StAX event model và nhận biết không gian tên reading

Với StAX, ứng dụng chủ động pull events như `START_ELEMENT`, `CHARACTERS`, `END_ELEMENT`. Khi gặp `START_ELEMENT`, hãy đọc `QName`/URI của không gian tên (không gian tên URI)/local part thay vì chỉ `getLocalName()` nếu bộ từ vựng có không gian tên.

Text cũng có thể cần accumulate qua nhiều character events. Whitespace events, các chú thích hoặc CDATA representation có thể xuất hiện tùy reader API/config. Vì vậy một state machine tốt xác định rõ “đang ở phần tử nào”, “đang thu trường dữ liệu nào”, và chỉ finalize value khi gặp end phần tử tương ứng.

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

`SchemaFactory` xử lý lược đồ language/compilation. `Schema` đại diện compiled lược đồ model có thể được reuse theo contract của implementation/API. `Validator` là đối tượng dùng để validate một source và thường không nên được share tùy tiện giữa concurrent operations nếu API không cam kết thread-safety.

Production code còn phải kiểm soát external lược đồ/DTD access và bộ phân giải; ví dụ code ngắn ở trên chỉ minh họa lifecycle, chưa phải security-hardening recipe hoàn chỉnh.

---

## 71. Validation lỗi model: cảnh báo, lỗi, fatal lỗi và line/column

XML APIs thường expose lỗi kèm locator information như line và column. Với SAX-style `ErrorHandler`, bạn có các mức như cảnh báo, lỗi và fatal lỗi theo bộ phân tích cú pháp/validator semantics.

Well-formedness violation thường là fatal ở XML phân tích cú pháp layer: bộ phân tích cú pháp không thể tiếp tục như HTML trình duyệt (browser) phục hồi lỗi (lỗi recovery). Schema kiểm tra tính hợp lệ (validation) lỗi nghĩa tài liệu đã có thể parse XML nhưng không thỏa contract XSD/DTD.

Khi đưa lỗi ra ứng dụng log/API response, nên preserve layer và location nếu an toàn:

```text
XML_PARSE_ERROR at line 12, column 18
XSD_VALIDATION_ERROR at /order/item[3]/price
```

để developer không mất thời gian tìm lỗi lược đồ trong khi tài liệu còn chưa đúng cú pháp XML. Với sensitive dữ liệu tải (payload), log ngữ cảnh vừa đủ chứ không dump toàn tài liệu.

---

## 72. Validation không nên bị trộn với business kiểm tra tính hợp lệ (validation)

Một chuỗi xử lý rõ ràng thường phân tầng:

```text
bytes / transport checks
→ secure XML parsing
→ namespace-aware processing
→ XSD/DTD validation nếu contract yêu cầu
→ object/domain mapping
→ business validation
→ authorization
```

XSD có thể kiểm tra `amount` là decimal, positive và đúng cardinality. Nhưng nó không biết account hiện tại có đủ balance hay user có quyền chuyển tiền. Ngược lại, business validator không nên phải tự kiểm tra XML tag đóng đúng hay không gian tên có đúng contract hay không.

Phân tầng làm lỗi thông điệp rõ hơn, test dễ hơn và giảm nguy cơ một layer “tin” dữ liệu mà layer trước chưa kiểm tra.

---

## 73. Validate trước ánh xạ hay validate trong lúc ánh xạ?

Không có một chuỗi xử lý duy nhất cho mọi library. Có hệ thống parse/validate rồi mới unmarshal; có ánh xạ/liên kết framework tích hợp lược đồ kiểm tra tính hợp lệ (validation) trong unmarshal; có xử lý theo luồng chuỗi xử lý validate và consume gần như cùng lúc.

Điều quan trọng là outcome phải rõ: **business layer chỉ nhận data sau khi structural contract cần thiết đã được kiểm tra**. Nếu hiệu năng (performance) khiến bạn tránh parse hai lần, hãy thiết kế chuỗi xử lý xử lý theo luồng/Source/handler phù hợp thay vì bỏ kiểm tra tính hợp lệ (validation) mà không nhận ra.

Với file cực lớn, việc build DOM chỉ để validate rồi build lần hai để process là dấu hiệu architecture cần xem lại.

---

## 74. Test XML bộ phân tích cú pháp/validator bằng negative cases, không chỉ happy path

Một test suite tốt không chỉ có một file valid. Hãy có fixtures cho wrong không gian tên, missing required phần tử, wrong order, invalid datatype, nil/empty/missing, duplicate ID, unexpected extension, malformed XML, huge nút văn bản, deep nesting và external-entity dữ liệu tải (payload).

Mục tiêu không phải “test XML Standard”, mà là verify **exact bộ phân tích cú pháp + exact cấu hình + exact phiên bản lược đồ** của ứng dụng xử lý boundary như bạn nghĩ. Parser defaults và implementation version khác nhau có thể thay hành vi bảo mật (security)/hiệu năng (performance).

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

Namespace trả lời **nút thuộc bộ từ vựng nào**. Schema trả lời **bộ từ vựng đó cho phép cấu trúc/type nào**. Parser model trả lời **ứng dụng nhận tree hay các sự kiện luồng**. XPath trả lời **cách chọn/tính trên model đó**. Business kiểm tra tính hợp lệ (validation) trả lời **data hợp domain và quyền hay không**.

Nếu bạn tách được năm câu hỏi này trong đầu, bạn đã qua được phần dễ nhầm nhất của XML Intermediate.
