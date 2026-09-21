# XML — Bổ sung mức Master (Master Supplement)
## XML specification internals, XSD 1.1, XPath/XQuery/XSLT 3.x, chuẩn hóa chính tắc và các edge case cần biết để thực sự master XML

Tài liệu này là phần cuối của bộ XML. Bạn chỉ nên đọc sau khi đã hiểu ba phần trước. Mục tiêu không phải biến bạn thành người thuộc lòng W3C specification, mà là giúp bạn có mental model đủ sâu để đọc specification khi cần, debug bộ phân tích cú pháp khác nhau, hiểu vì sao tuần tự hóa có thể thay đổi nhưng semantics không đổi, phân biệt schema-typed data với raw XML, và xử lý những hệ thống dùng XML Signature, XSD 1.1, XSLT 3.0 hoặc hướng tài liệu XML phức tạp.

Ở mức này, XML không còn chỉ là “markup language”. Nó là một hệ sinh thái gồm lexical syntax, các không gian tên, lược đồ hệ kiểu, truy vấn data model, chuyển đổi engine, URI resolution, bảo mật (security) model và canonical representation.


## Quy ước thuật ngữ trong tài liệu

Tài liệu dùng tiếng Việt tự nhiên làm ngôn ngữ giải thích chính và giữ thuật ngữ gốc ở lần định nghĩa để tiện đối chiếu. Các cách gọi được dùng thống nhất gồm: **tài liệu XML (XML document)**, **phần tử (element)**, **thuộc tính (attribute)**, **phần tử gốc (root element)**, **nút văn bản (text node)**, **không gian tên (namespace)**, **tiền tố (prefix)**, **tên mở rộng (expanded name)**, **bộ từ vựng (vocabulary)**, **lược đồ (schema)**, **giao thức (protocol)**, **quy tắc nghiệp vụ (business rule)**, **đúng cú pháp XML (well-formed)**, **kiểm tra tính hợp lệ (validation)**, **phân tích cú pháp (parsing)**, **bộ phân tích cú pháp (parser)**, **xử lý theo luồng (streaming)**, **luồng (stream)**, **truy vấn (query)**, **chuyển đổi (transformation)**, **ánh xạ/liên kết (binding)**, **tuần tự hóa (serialization)**, **bộ tuần tự hóa (serializer)**, **chuẩn hóa chính tắc (canonicalization/C14N)**, **cấu hình (configuration)**, **thời gian chạy (runtime)** và **dữ liệu tải (payload)**. Sau khi thuật ngữ đã được định nghĩa, nội dung ưu tiên cách gọi tiếng Việt. Những tên chuẩn như XML, DTD, XSD, XPath, XSLT, XQuery, DOM, SAX, StAX, SOAP, WSDL, QName, PSVI, CDATA và tên API cụ thể được giữ nguyên.

---

## 1. XML 1.0 và XML 1.1

Hai version chính tồn tại là XML 1.0 và XML 1.1.

XML 1.0 là version phổ biến nhất trong production. XML 1.1 thay đổi một số rule liên quan character repertoire, control characters và newline handling để phù hợp hơn với một số Unicode/use cases.

Điều quan trọng là XML 1.1 không phải “XML mới hơn nên luôn tốt hơn”. Ecosystem support quan trọng hơn version number. Nếu partner, Java library, tool, bộ xử lý lược đồ và downstream system đều dùng XML 1.0, việc tự chuyển sang 1.1 chỉ tạo khả năng tương thích risk.

Vì vậy nếu không có requirement rõ, XML 1.0 vẫn là lựa chọn interoperable nhất.

---

## 2. XML 1.0 Fifth Edition và Unicode names

XML 1.0 Fifth Edition là một mốc quan trọng vì XML Name grammar hỗ trợ Unicode rộng hơn nhiều so với cách developer thường tưởng.

Một regex kiểu:

```regex
[A-Za-z_][A-Za-z0-9_-]*
```

không đại diện đầy đủ XML Name grammar.

Điều này quan trọng vì nhiều developer tự validate tên phần tử hoặc build dynamic XML bằng regex ASCII. Nếu input có Unicode name hợp lệ, regex có thể reject sai. Ngược lại, regex tự chế có thể cho phép structure không hợp grammar thực.

Rule đúng là dùng bộ phân tích cú pháp/bộ tuần tự hóa/lược đồ library để xử lý XML names.

---

## 3. Valid UTF‑8 không đồng nghĩa valid XML character

UTF‑8 chỉ là encoding. XML version còn quy định character nào được phép xuất hiện.

Vì vậy byte sequence có thể decode thành Unicode hợp lệ nhưng character đó vẫn không được phép trong XML version đang dùng.

Đừng tự nghĩ “nếu string Java chứa được thì XML serialize được”. XML bộ tuần tự hóa chuẩn phải kiểm tra character legality.

---

## 4. End-of-line normalization

XML bộ phân tích cú pháp có rule chuẩn hóa line endings.

Một file có thể dùng CRLF, CR hoặc LF tùy platform. Sau phân tích cú pháp, processor có thể expose newline theo normalized form.

Điều này cho thấy một nguyên tắc lớn: **raw lexical bytes và parsed character data không phải cùng layer**.

Nếu bạn compare raw file byte-for-byte với data sau bộ phân tích cú pháp, bạn đang compare hai representations khác nhau.

Đây cũng là lý do XML Digital Signature không thể chỉ “hash pretty-printed XML” tùy tiện.

---

## 5. Attribute value normalization

Attribute values cũng có normalization rules.

Ví dụ thực thể references có thể được expanded, whitespace có thể được normalized theo XML/DTD type rules, và ứng dụng cuối cùng nhận string khác lexical source.

Nếu DTD khai báo thuộc tính type không phải CDATA, normalization có thể mạnh hơn.

Điều này có hai consequences. Thứ nhất, business logic không nên phụ thuộc exact lexical spelling của thuộc tính nếu contract nói semantic value. Thứ hai, cryptographic giao thức phải xác định chuẩn hóa chính tắc đúng thay vì ký raw source tùy tool.

---

## 6. `standalone`

XML declaration có thể chứa:

```xml
<?xml
  version="1.0"
  encoding="UTF-8"
  standalone="yes"?>
```

`standalone` không có nghĩa “file này không cần internet” hoặc “không được load các tài nguyên bên ngoài”.

Nó liên quan việc external markup declarations có ảnh hưởng tới information được processor truyền cho ứng dụng hay không theo XML rules.

Đây là một feature specification-level, hiếm khi ứng dụng developer cần set thủ công.

---

# DTD chuyên sâu

## 7. Internal subset và external subset

DOCTYPE có thể có internal subset:

```xml
<!DOCTYPE root [
  <!ELEMENT root (#PCDATA)>
]>
```

hoặc external subset:

```xml
<!DOCTYPE root SYSTEM "root.dtd">
```

hoặc kết hợp theo grammar phù hợp.

Điểm cần nhớ ở mức master là DTD processing không chỉ là “validate structure”. Nó có thể ảnh hưởng các thực thể, default giá trị thuộc tínhs và information ứng dụng nhận.

---

## 8. Parameter các thực thể

General thực thể dùng trong document content:

```xml
&company;
```

Parameter thực thể dùng trong DTD:

```dtd
<!ENTITY % common SYSTEM "common.dtd">
%common;
```

Parameter các thực thể cho phép modularize DTD grammar.

Nhưng external parameter các thực thể cũng là một phần của XXE bề mặt tấn công. Nếu bạn chỉ disable general các thực thể ngoài (external các thực thể) nhưng vẫn để parameter thực thể resolution mở, bộ phân tích cú pháp có thể vẫn access các tài nguyên bên ngoài.

---

## 9. Unparsed các thực thể và NOTATION

DTD còn có khái niệm unparsed thực thể và notation để liên kết tài liệu XML với external non-XML data format.

Trong ứng dụng hiện đại bạn ít gặp chúng, nhưng có thể thấy trong publishing, SGML-derived ecosystem hoặc old document standards.

Bạn không cần memorize syntax chi tiết, chỉ cần nhận diện rằng DTD thực thể system rộng hơn việc thay `&name;` bằng text.

---

# Không gian tên (Namespace) chuyên sâu

## 10. Namespace URI là identifier, không phải URL để normalize tùy ý

Hai strings:

```text
https://example.com/ns
```

và:

```text
https://example.com/ns/
```

không nên được ứng dụng tự coi là cùng không gian tên chỉ vì “URL giống nhau”.

Namespace identity dựa trên không gian tên name theo specification, không dựa trên HTTP redirect, DNS equivalence hoặc URL chuẩn hóa chính tắc tự chế.

Đây là nguyên tắc cực kỳ quan trọng với signature, bảo mật (security) matching và lược đồ resolution.

---

## 11. Expanded name phải trở thành mental model mặc định

Element:

```xml
<a:Order xmlns:a="urn:order"/>
```

không có identity logic là `a:Order`.

Identity là:

```text
namespace = urn:order
local name = Order
```

Nếu input đổi thành:

```xml
<o:Order xmlns:o="urn:order"/>
```

semantics không gian tên vẫn giữ nguyên.

Mọi code security-sensitive nên match bằng URI của không gian tên (không gian tên URI) + local name.

---

## 12. QName

QName là qualified name như:

```text
xs:string
app:OrderType
```

Điểm khó là QName không chỉ xuất hiện trong tên phần tửs. Nó còn có thể nằm **trong giá trị thuộc tính**.

Ví dụ:

```xml
<xs:element type="app:OrderType"/>
```

Để hiểu `app:OrderType`, processor phải nhìn không gian tên ánh xạ/liên kết của tiền tố `app` trong context hiện tại.

Nếu bạn copy một thuộc tính QName-valued sang một phần tử khác nhưng quên copy khai báo không gian tên, lexical text giống nhau nhưng meaning hỏng.

---

## 13. Base URI

XML node/document có thể có base URI dựa trên document location, `xml:base` và processor context.

Functions hoặc processors có thể resolve relative URI dựa trên base URI.

Ví dụ XSLT `document()`, lược đồ imports hoặc ứng dụng link resolution đều có thể bị ảnh hưởng.

Ở mức bảo mật (security), base URI và URI bộ phân giải phải được xem cùng nhau. Một relative URI tưởng vô hại có thể resolve thành local file hoặc remote network resource.

---

# Infoset và PSVI

## 14. XML Information Set

XML Infoset là mô hình abstract mô tả “information” có trong một tài liệu XML sau phân tích cú pháp, không tập trung vào exact lexical spelling.

Ví dụ:

```xml
<a x="1"/>
```

và:

```xml
<a x='1'></a>
```

khác cách viết nhưng không nhất thiết khác information ở level mà nhiều XML các ứng dụng quan tâm.

Infoset giúp bạn hiểu vì sao parse → serialize có thể đổi quote style, self-closing form hoặc thuộc tính formatting mà semantics vẫn giữ.

---

## 15. PSVI là gì?

PSVI = Post-Schema-Validation Infoset.

Sau XSD kiểm tra tính hợp lệ (validation), processor không chỉ biết nodes/text nữa. Nó có thể biết thêm:

```text
element thuộc type nào
attribute thuộc type nào
value normalized/typed ra sao
default value nào được schema supply
validation status
```

Điều này tạo ra một typed view của XML.

Nếu ứng dụng dùng schema-aware XSLT/XQuery processor, type information có thể ảnh hưởng expression semantics.

---

## 16. Default values từ lược đồ

Schema có thể định nghĩa default/fixed values.

Điều này nghĩa raw XML source không có thuộc tính/phần tử value rõ ràng, nhưng post-validation ứng dụng model có thể expose schema-supplied value tùy API.

Đây là lý do khi debug “tại sao object có giá trị mà source XML không có”, bạn phải kiểm tra lược đồ defaults.

---

# XSD 1.1

## 17. Tại sao XSD 1.1 xuất hiện?

XSD 1.0 rất mạnh về structure và type nhưng khó diễn tả một số cross-field constraints.

Ví dụ requirement:

```text
min <= max
```

hoặc:

```text
nếu type = BUSINESS thì companyName bắt buộc
```

XSD 1.1 thêm mechanisms như assertions và type alternatives để xử lý nhiều rule loại này.

---

## 18. `xs:assert`

Ví dụ concept:

```xml
<xs:assert test="@min le @max"/>
```

Assertion dùng XPath-like expression để kiểm tra constraint trên instance.

Điều này làm lược đồ expressive hơn nhưng cũng đẩy business-like logic vào lược đồ.

Bạn phải cân bằng giữa “lược đồ kiểm tra tính hợp lệ (validation) mạnh” và “lược đồ quá thông minh khó debug”.

Ngoài ra processor support XSD 1.1 không universal. Không assume Java default XML Schema implementation support mọi feature.

---

## 19. Type alternatives

XSD 1.1 có thể chọn type dựa trên conditions.

Ví dụ conceptually, một phần tử có thuộc tính `kind="company"` có thể dùng CompanyType, còn `kind="person"` dùng PersonType.

Feature này powerful nhưng làm khả năng liên vận giảm nếu consumer chỉ support XSD 1.0.

Trong cross-company integration, support matrix quan trọng hơn việc dùng feature mới nhất.

---

## 20. XSD regex không giống regex bạn dùng trong Java

`xs:pattern` dùng XML Schema regex semantics.

Các khái niệm như anchoring, character classes và Unicode categories không map 1:1 với JavaScript/Java/PCRE.

Nếu contract có regex quan trọng, test bằng đúng bộ xử lý lược đồ.

---

## 21. `whiteSpace` facet

XSD có `whiteSpace` facet với các behavior như:

```text
preserve
replace
collapse
```

Điều này ảnh hưởng lexical normalization trước khi value được interpret.

Ví dụ `xs:string` và `xs:token` không có cùng whitespace behavior.

---

## 22. `xs:token` không phải token bảo mật

Tên `token` dễ gây hiểu nhầm.

`xs:token` là string-derived datatype với whitespace collapsing semantics. Nó phù hợp với các text values nơi runs of whitespace không có ý nghĩa.

Đừng đọc `xs:token` rồi nghĩ nó liên quan JWT hoặc auth token.

---

## 23. `xs:decimal`

`xs:decimal` là decimal number model, không phải IEEE floating-point.

Với financial XML:

```xml
<amount>123.45</amount>
```

ánh xạ sang Java `BigDecimal` thường phù hợp hơn `double`.

Nếu dùng `double`, binary floating point có thể tạo rounding artifacts không phù hợp money calculation.

---

## 24. Date/time types và timezone

`xs:dateTime` có lexical/timezone semantics phức tạp hơn việc “parse thành LocalDateTime”.

Ví dụ một value có thể có timezone offset, còn value khác không có timezone.

Nếu contract cần instant tuyệt đối, phải định nghĩa timezone requirement rõ.

Mapping:

```text
xs:dateTime
```

sang Java type nào phụ thuộc semantic contract, không chỉ syntax.

---

## 25. Identity constraints không dùng arbitrary XPath 3.1

Selectors/fields của `xs:key`, `xs:keyref`, `xs:unique` dùng một XPath subset/rule set dành riêng cho lược đồ constraints.

Đừng assume mọi expression chạy được trong Saxon XPath 3.1 sẽ chạy được trong `xs:key`.

---

# XPath 1.0 đến XPath 3.1

## 26. Vì sao phải biết XPath version?

Một trình duyệt (browser) API hoặc legacy Java engine có thể chỉ support XPath 1.0, trong khi Saxon hoặc XML database support XPath 3.1.

Expression hợp lệ ở 3.1 có thể không chạy ở 1.0.

Vì vậy khi debug, luôn hỏi:

```text
XPath version nào?
processor nào?
schema-aware không?
```

---

## 27. XPath 1.0 mental model

XPath 1.0 chủ yếu xoay quanh:

```text
node-set
string
number
boolean
```

Nhiều built-in trình duyệt (browser) XPath APIs vẫn gần mental model này.

---

## 28. Modern XPath mental model

XPath 2.0/3.x chuyển sang sequence-based typed data model.

Expression có thể trả:

```text
sequence of nodes
sequence of strings
sequence of integers
mixed typed items
```

XDM là nền tảng.

---

## 29. Effective Boolean Value

Khi expression nằm trong condition, XPath dùng Effective Boolean Value rules.

Đây không giống JavaScript truthiness.

Ví dụ sequence nhiều atomic values có thể tạo dynamic error trong context mà JS chỉ coi array là truthy.

Senior XPath phải đọc EBV rules thay vì suy từ ngôn ngữ khác.

---

## 30. General comparison vs value comparison

Modern XPath có general comparisons:

```xpath
=
!=
<
<=
>
>=
```

và value comparisons:

```xpath
eq
ne
lt
le
gt
ge
```

General comparisons có sequence-oriented semantics, còn value comparisons kỳ vọng singleton atomic values theo rules chặt hơn.

Điều này rất quan trọng khi expression trả nhiều items.

---

## 31. Node identity

Hai nodes có thể có cùng text/value nhưng không phải cùng node.

XPath có node comparison như:

```text
is
<<
>>
```

để hỏi identity hoặc document order.

Đừng dùng string equality nếu requirement thật sự là “đây có phải exact same node không?”

---

## 32. Maps trong XPath/XQuery 3.1

Modern XDM có maps:

```xquery
map {
  "name": "Alice",
  "age": 27
}
```

Điều này giúp truy vấn ecosystem xử lý data giống JSON object, không chỉ XML nodes.

---

## 33. Arrays

Arrays:

```xquery
[1, 2, 3]
```

là first-class items trong 3.1 ecosystem.

Điều này cho thấy XPath/XQuery đã mở rộng xa hơn “ngôn ngữ chọn XML tag”.

---

## 34. Function items

Functions có thể được truyền như values.

Điều này cho phép higher-order programming, function composition và dynamic invocation.

Nếu bạn chỉ biết XPath 1.0, đây là một thay đổi mental model rất lớn.

---

# XQuery và XSLT hiện đại

## 35. Computed constructors trong XQuery

XQuery có thể tạo XML mà tên hoặc value được tính thời gian chạy:

```xquery
element user {
  attribute id { $id },
  element name { $name }
}
```

Điều này useful khi output structure dynamic.

---

## 36. XQuery modules

Large XQuery ứng dụng có modules, functions, các không gian tên và imports.

Một số XML-native database dùng XQuery như ứng dụng/truy vấn language thực sự, không chỉ là một expression ngắn.

---

## 37. XSLT 3.0 packages

Packages cung cấp modularity ở level cao hơn stylesheet include/import cổ điển.

Chúng có concepts về exposed/accepted components, visibility và versioning.

Điều này giúp stylesheet enterprise được tổ chức giống software modules hơn.

---

## 38. XSLT accumulators

Streaming chuyển đổi đôi khi cần running state, ví dụ section number hoặc running total.

Accumulators cung cấp cơ chế declarative để tính state theo traversal.

Chúng là ví dụ về việc XSLT 3.0 giải quyết vấn đề mà imperative programmer thường nghĩ phải dùng mutable variables.

---

## 39. Modes và `on-no-match`

Modern XSLT modes có thể định nghĩa default processing behavior.

Ví dụ một mode có thể nói “nếu không có template specialized thì shallow-copy node”.

Điều này giúp implement identity-transform-like pattern rất gọn.

---

## 40. Identity Transformation Pattern

Một chuyển đổi phổ biến là:

```text
copy toàn document
nhưng override vài node cần thay
```

Ví dụ đổi không gian tên, redact password hoặc rename một phần tử.

Thay vì viết output cho toàn tree, bạn dùng identity/default-copy rule rồi chỉ override difference.

Pattern này cực kỳ quan trọng trong migration và normalization.

---

# Bộ phân giải (resolver) và tài nguyên bên ngoài (external resources)

## 41. XML Catalog sâu hơn

XML Catalog không chỉ map lược đồ URL. Nó có thể map system identifiers, public identifiers hoặc URI references tùy catalog rules.

Trong build/integration environment, Catalog giúp biến external dependencies thành controlled local resources.

Điều này rất hữu ích nếu vendor lược đồ dùng absolute URL nhưng production không được internet access.

---

## 42. Controlled URI Resolver Pattern

Một architecture tốt là không cho processor tự truy cập filesystem/network.

Thay vào đó:

```text
processor asks resolver for URI
→ resolver checks allowlist/catalog
→ resolver returns trusted local resource
```

Pattern này áp dụng với XSD imports, XSLT includes/imports, `document()` và legacy DTD.

Điểm mạnh là bảo mật (security) policy tập trung ở một boundary.

---

# XML chính tắc (Canonical XML)

## 43. Canonicalization giải quyết vấn đề gì?

XML có nhiều lexical forms tương đương về semantic information.

Ví dụ thuộc tính order, quote style, empty phần tử syntax và khai báo không gian tên placement có thể khác.

Canonical XML định nghĩa cách biến XML information thành deterministic tuần tự hóa theo algorithm cụ thể.

Nó được dùng nhiều nhất trong digital signatures.

---

## 44. Inclusive và Exclusive Canonicalization

Trong XML Signature ecosystem có nhiều chuẩn hóa chính tắc algorithms.

Exclusive chuẩn hóa chính tắc đặc biệt hữu ích khi sign một subtree có thể được move hoặc embed trong namespace-rich context, vì bạn không muốn surrounding khai báo không gian têns thay đổi canonical form ngoài ý muốn.

Bạn không cần tự implement, nhưng phải biết algorithm identifier là một phần giao thức. Không tự đổi “vì output nhìn giống”.

---

# Chữ ký XML (XML Signature) chuyên sâu

## 45. Reference là trọng tâm của XML Signature

Signature không nhất thiết sign “document đang nhìn thấy”.

Nó sign data được xác định bởi references, URI resolution và transforms.

Conceptual flow:

```text
resolve reference
→ apply transforms
→ canonicalize nếu required
→ calculate digest
→ compare digest
→ verify signature value
→ verify key/certificate trust
→ bind verified data to business logic
```

Nếu bỏ step cuối, vẫn có thể có application-level vulnerability.

---

## 46. ID typing

Reference `#order123` phải resolve tới đúng node.

XML processor/library phải biết thuộc tính nào là ID.

Nguồn ID semantics có thể là:

```text
DTD type ID
XSD type
xml:id
manual API registration
library-specific rule
```

Nếu attacker tạo duplicate-looking IDs hoặc ứng dụng resolve khác verifier, bảo mật (security) có thể hỏng.

---

## 47. Signature Wrapping Defense

Giả sử signature verifier nói node A hợp lệ.

Business code không được bỏ node A rồi chạy truy vấn:

```text
find first <Order>
```

vì attacker có thể đưa một unsigned Order lên đầu.

Correct pattern là verifier trả hoặc bind exact signed object/node cho business layer.

Đây gọi là **Verified Node Binding Pattern**.

---

## 48. Namespace confusion attack

Nếu code bảo mật (security) chỉ kiểm tra:

```java
localName.equals("Admin")
```

attacker có thể gửi:

```xml
<evil:Admin xmlns:evil="urn:evil"/>
```

Local name là `Admin`, nhưng bộ từ vựng không gian tên khác.

Security-sensitive XML processing phải check tên mở rộng, không chỉ local name hoặc tiền tố.

---

# Khác biệt giữa bộ phân tích cú pháp (parser differential) và giới hạn tài nguyên (resource limits)

## 49. Parser differential

Không phải mọi XML bộ phân tích cú pháp có same defaults.

Một bộ phân tích cú pháp có thể enable DTD, bộ phân tích cú pháp khác disable. Một XSD engine support 1.1, engine khác chỉ 1.0. Entity limit, không gian tên behavior và XInclude defaults cũng có thể khác.

Vì vậy giao thức bảo mật (security) không nên phụ thuộc undocumented default.

Configuration phải explicit và tested trên exact implementation/version.

---

## 50. XXE disabled vẫn chưa đủ chống DoS

Một attacker không cần thực thể ngoài (external thực thể) để gây resource exhaustion.

Họ có thể gửi document sâu hàng trăm nghìn levels, hàng triệu các phần tử, các thuộc tính khổng lồ hoặc nút văn bản rất lớn.

Vì vậy XML boundary cần size/depth/node limits độc lập với XXE cấu hình.

---

## 51. DOM memory amplification

Raw XML 100 MB có thể thành tree tiêu tốn vài trăm MB hoặc hơn.

Reason gồm Java objects, UTF string representation, arrays, pointers, các thuộc tính và siêu dữ liệu (metadata).

Nếu service có 512 MB heap, “file chỉ 100 MB” vẫn có thể làm service crash.

Streaming design phải dựa trên benchmark và limits thực.

---

# Tuần tự hóa (serialization) và bảo toàn biểu diễn từ vựng (lexical preservation)

## 52. Pretty-print có thể thay đổi data

Với record XML:

```xml
<user><name>Alice</name></user>
```

thêm indentation thường không ảnh hưởng business fields.

Nhưng với nội dung hỗn hợp:

```xml
<p>Hello <b>world</b>!</p>
```

nếu formatter chèn newline/spaces không đúng, text flow có thể đổi.

Document-centric XML phải được format cẩn thận.

---

## 53. Parse → serialize không giữ exact source

Một bộ tuần tự hóa không bắt buộc giữ:

```text
single quote vs double quote
original prefix name
attribute order
CDATA boundary
entity reference spelling
empty-element spelling
indentation
```

Nếu bạn cần exact lexical preservation, ordinary DOM round-trip không đủ.

---

## 54. Prefix có thể đổi

Input:

```xml
<a:user xmlns:a="urn:user"/>
```

output:

```xml
<ns1:user xmlns:ns1="urn:user"/>
```

có thể hoàn toàn equivalent theo không gian tên semantics.

Consumer không được depend exact tiền tố string trừ khi một unusual giao thức định nghĩa lexical contract.

---

## 55. Attribute order không phải business order

Không viết code nghĩ “thuộc tính đầu tiên là id, thứ hai là status”.

Attribute names xác định meaning, không phải vị trí.

Canonicalization có ordering rule riêng chỉ để tạo deterministic representation.

---

## 56. Empty phần tử lexical form

```xml
<a/>
```

và:

```xml
<a></a>
```

thường biểu diễn cùng empty phần tử.

Raw string diff không phải semantic XML diff.

---

## 57. Entity references có thể không được preserve

Input:

```xml
<name>&company;</name>
```

sau phân tích cú pháp có thể thành text `Acme Corporation`.

Serializer sau đó có thể output direct text thay vì `&company;`.

Business meaning không được phụ thuộc thực thể lexical choice.

---

## 58. CDATA có thể mất

Input:

```xml
<code><![CDATA[a < b]]></code>
```

có thể serialize thành:

```xml
<code>a &lt; b</code>
```

mà semantics character data không đổi.

Vì vậy không được dùng “có CDATA hay không” làm business flag.

---

## 59. Semantic contract vs lexical contract

Một XML API nên contract trên:

```text
namespace
local name
element/attribute values
types
order
cardinality
schema rules
```

không nên contract trên:

```text
prefix spelling
indentation
quote style
CDATA
attribute order
self-closing notation
```

trừ khi giao thức explicitly yêu cầu canonical lexical representation.

---

# Các ngôn ngữ lược đồ thay thế (alternative schema languages)

## 60. RELAX NG

RELAX NG là một lược đồ language khác ngoài DTD và XSD.

Nó có XML syntax và compact syntax.

RELAX NG nổi tiếng với grammar model tương đối elegant, đặc biệt cho hướng tài liệu XML và nội dung hỗn hợp.

Bạn không nhất thiết phải dùng nó trong Java enterprise project, nhưng master XML nên biết XSD không phải lược đồ language duy nhất.

---

## 61. Schematron

Schematron thiên rule/assertion kiểm tra tính hợp lệ (validation).

Ví dụ requirement:

```text
nếu paymentMethod = CARD thì cardNumber phải tồn tại
```

hoặc:

```text
sum(item/amount) phải bằng total
```

Những constraints cross-tree này đôi khi khó diễn tả tự nhiên bằng XSD 1.0 nhưng phù hợp Schematron.

Schematron thường dùng XPath expressions trong assertions.

---

## 62. Kết hợp XSD và Schematron

Một architecture rất mạnh là:

```text
XSD
→ kiểm tra structure + datatype

Schematron
→ kiểm tra cross-field/cross-tree semantic constraints

application
→ domain logic + authorization
```

Không bắt một layer làm mọi việc.

---

# Các mẫu thiết kế XSD (XSD design patterns)

## 63. Russian Doll

Russian Doll style dùng local anonymous types nested trong một root/global phần tử.

Ưu điểm là lược đồ self-contained và encapsulated.

Nhược điểm là type reuse thấp.

Pattern phù hợp bộ từ vựng nhỏ, structure ít tái sử dụng.

---

## 64. Venetian Blind

Venetian Blind dùng global named complex types nhưng local phần tử declarations.

Ưu điểm là reusable type definitions mà vẫn hạn chế số global các phần tử.

Đây là pattern phổ biến khi domain structures được reuse.

---

## 65. Salami Slice

Salami Slice dùng nhiều global phần tử declarations rồi reference chúng.

Ưu điểm là phần tử reuse.

Nhược điểm là global symbol space lớn và lược đồ navigation phức tạp hơn.

---

## 66. Garden of Eden

Garden of Eden đưa cả các phần tử và named types lên global scope.

Ưu điểm là maximum reuse/extensibility.

Nhược điểm là lược đồ có nhiều global components và dependency graph phức tạp.

Không có pattern “senior nhất”. Chọn theo governance, reuse và versioning requirements.

---

# Thiết kế từ hợp đồng (contract-first) và từ mã nguồn (code-first)

## 67. Contract-first

Flow:

```text
design XML vocabulary/XSD
→ review với consumers
→ version/publish
→ generate or map code
```

Ưu điểm lớn nhất là contract không phụ thuộc Java implementation.

Nó phù hợp B2B/tích hợp doanh nghiệp nơi nhiều language/platform cùng consume.

---

## 68. Code-first

Flow:

```text
Java classes
→ framework generates XML/XSD
```

Nhanh cho internal service.

Nhưng generated lược đồ dễ phản ánh OO decisions như class inheritance, wrapper collections hoặc implementation naming.

Nếu contract tồn tại 10 năm và có nhiều partner, code-first có thể tạo technical debt.

---

# Các mẫu thiết kế mức Master (Master Design Patterns)

## 69. Boundary Parser

Thay vì mỗi service method tự tạo bộ phân tích cú pháp, nên có một boundary component chịu trách nhiệm:

```text
size limits
parser hardening
namespace handling
schema validation
error translation
```

Business code chỉ nhận typed/trusted representation.

Điều này tránh bảo mật (security) config drift.

---

## 70. Resolver Gateway

Mọi external XML resource lookup đi qua bộ phân giải chung.

Resolver thực hiện allowlist, XML Catalog, caching và observability.

Không để XSLT/XSD/bộ phân tích cú pháp tự gọi internet ở nhiều nơi.

---

## 71. Schema Registry

Schemas nên có ownership, version, checksum, khả năng tương thích status và release lifecycle.

Nếu một common lược đồ bị thay âm thầm, nhiều integration có thể vỡ.

Schema phải được quản lý như API artifact.

---

## 72. Canonical Model

Vendor-specific XML được transform thành internal model ổn định.

Điều này ngăn external không gian tên/type quirks leak vào domain.

---

## 73. Transformation Pipeline

Thay giant XSLT xử lý mọi thứ, có thể chia:

```text
sanitize/normalize
→ vocabulary migration
→ business enrichment
→ output rendering
```

Mỗi stage nhỏ và testable.

---

## 74. Verified Node Binding

Khi dùng XML Signature, signature verification layer phải trả exact verified node/data cho business layer.

Business code không tự truy vấn lại toàn document.

Đây là pattern bảo mật (security) cực quan trọng.

---

# Gỡ lỗi (debug) và rà soát (review)

## 75. Full debug flow

Khi XML integration lỗi, đừng sửa ngẫu nhiên tiền tố hoặc XPath.

Hãy đi theo thứ tự:

```text
raw bytes có decode đúng không?
XML declaration/HTTP charset có conflict không?
document có well-formed không?
root expanded name là gì?
namespace bindings đúng không?
schema targetNamespace là gì?
instance có qualified đúng không?
schema imports resolve file nào?
validator version nào?
XPath version/namespace context nào?
nil/empty/missing có bị map mất không?
parser có external resolution không?
serializer có đổi prefix/CDATA/whitespace không?
signature reference target node nào?
```

Đi theo layer giúp debug nhanh hơn nhiều.

---

## 76. Master bảo mật (security) review

Một XML endpoint nhận untrusted input phải được review cả input size, nesting depth, DTD, các thực thể ngoài (external các thực thể), parameter các thực thể, external subset, XInclude, lược đồ resolution, XSLT resolution, XPath construction, nhận biết không gian tên matching, signature reference ánh xạ/liên kết và sensitive logging.

Nếu endpoint chỉ “disable XXE” nhưng không có input size limit, nó vẫn có thể bị memory DoS.

Nếu signature verify đúng nhưng business code đọc wrong node, nó vẫn có thể vulnerable.

Security XML là chuỗi xử lý property, không phải một bộ phân tích cú pháp flag.

---

## 77. Master hiệu năng (performance) review

Hãy hỏi liệu DOM có thật sự cần không, input maximum size là bao nhiêu, lược đồ/XSLT có compile lại mỗi request không, bộ phân giải có network access không, XPath có broad `//` trên tree lớn không, chuỗi xử lý có parse-serialize nhiều vòng không, và memory amplification đã được benchmark chưa.

Một hiệu năng (performance) bug XML thường đến từ architecture hơn là một tag cụ thể.

---

# Mô hình tư duy tổng thể (Full Mental Model)

## 78. Toàn bộ XML processing flow

Đây là mental model cuối cùng bạn nên giữ:

```text
raw bytes
↓
encoding detection / decoding
↓
XML lexical parsing
↓
well-formedness checking
↓
namespace expansion
↓
optional DTD/entity processing
↓
tree hoặc streaming event model
↓
optional XSD validation
↓
typed information / PSVI / XDM
↓
XPath / XQuery / XSLT
↓
normalization / domain mapping
↓
business validation / authorization
↓
serialization
↓
canonicalization / digital signature nếu protocol yêu cầu
```

Mỗi arrow là một nơi có thể có bug, hiệu năng (performance) cost hoặc bảo mật (security) implication.

---

## 79. Khi nào có thể nói đã master XML?

Bạn không cần thuộc từng production rule trong W3C specification.

Bạn có thể coi mình có XML mastery foundation khi nhìn một hệ thống XML lạ và biết hỏi đúng câu: XML version nào, encoding nào, không gian tên nào, phiên bản lược đồ nào, bộ phân tích cú pháp model nào, external resolution có được kiểm soát không, XPath/XSLT version nào, contract evolve thế nào, nil-vs-missing semantics ra sao, document có lớn tới mức cần xử lý theo luồng không, và giao thức có chuẩn hóa chính tắc/signature requirement không.

Đó là sự khác biệt giữa “biết viết XML” và “hiểu XML platform”.

---

## 80. Cách học bộ bốn file

Phần Beginner nên đọc từ đầu đến cuối và tự gõ XML examples. Phần Intermediate cần thực hành không gian tên/XPath/XSD vì chỉ đọc sẽ rất dễ quên. Phần Senior nên học song song với Java XML APIs hoặc một integration case thực tế. Phần Master Supplement không cần học thuộc trong một lần; hãy dùng nó để xây mental model và quay lại khi gặp lược đồ, signature, bộ phân tích cú pháp hoặc chuyển đổi edge case.

Sau khi hoàn thành cả bốn phần, bước tiếp theo hiệu quả nhất không phải đọc thêm hàng trăm trang lý thuyết mà là tự làm một project nhỏ có không gian tên, XSD kiểm tra tính hợp lệ (validation), XPath truy vấn, StAX large-file phân tích cú pháp, XSLT chuyển đổi và secure cấu hình bộ phân tích cú phápuration. Khi bạn tự debug những tương tác (interaction) đó, kiến thức XML sẽ trở thành kỹ năng thực tế thay vì chỉ là kiến thức đọc.
