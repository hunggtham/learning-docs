# XML — cấp cao (senior / 시니어)

> **Mạch đọc:** Đọc **XML — cấp cao (senior / 시니어)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **XSLT, XQuery, lược đồ (schema / 스키마) evolution, streaming, bảo mật (security / 보안), canonicalization và enterprise tích hợp (integration / 통합)** sang **1. XSLT là gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

## XSLT, XQuery, lược đồ (schema / 스키마) evolution, streaming, bảo mật (security / 보안), canonicalization và enterprise tích hợp (integration / 통합)

Phần này dành cho giai đoạn bạn đã hiểu cú pháp XML, không gian tên (namespace / 네임스페이스), XSD, XPath và parser các mô hình (models / 모델들). Ở mức cấp cao (senior / 시니어), việc “đọc được XML” không còn đủ. Bạn phải có khả năng thiết kế một XML đặc tả hợp đồng (contract / 계약) có thể sống lâu trong hệ thống enterprise, xử lý tệp (file / 파일) lớn mà không làm nổ bộ nhớ (memory / 메모리), harden parser trước đầu vào (input / 입력) không đáng tin, phiên bản (version / 버전) lược đồ (schema / 스키마) mà không phá bên tiêu thụ (consumer / 소비자), dùng transformation/truy vấn (query / 쿼리) đúng chỗ, và hiểu vì sao canonicalization hoặc digital signature lại phức tạp hơn việc băm (hash / 해시) raw XML văn bản (text / 텍스트).

Tư duy xuyên suốt của phần này là chuyển từ “XML như dữ liệu” sang “XML như một processing nền tảng (platform / 플랫폼)”.

---

## 1. XSLT là gì?

XSLT là viết tắt của **XSL Transformations**. Nó là ngôn ngữ dùng để transform XML/XDM đầu vào (input / 입력) thành một đầu ra (output / 출력) cây (tree / 트리) hoặc serialization khác.

Ví dụ, nguồn (source / 소스) XML:

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

XSLT không nên được học như một thứ “XML có if và for”. mô hình tư duy (mental model / 사고 모델) đúng là: nguồn (source / 소스) cây (tree / 트리) đi vào processor, processor chọn template dựa trên mẫu (pattern / 패턴), template dùng XPath để đọc dữ liệu, rồi xây kết quả (result / 결과) cây (tree / 트리).

---

## 2. `xsl:template` và template dispatch

Một template:

```xml
<xsl:template match="book">
  ...
</xsl:template>
```

nói rằng khi processor cần xử lý một nút (node / 노드) phù hợp với mẫu (pattern / 패턴) `book`, template này có thể được áp dụng.

Khác với Java nơi bạn thường gọi phương thức (method / 메서드) trực tiếp, XSLT có thể vận hành theo kiểu dispatch dựa trên mẫu (pattern / 패턴). Đây là một điểm mạnh vì biểu định kiểu (stylesheet / 스타일시트) có thể được modular hóa theo nút (node / 노드) kiểu (type / 타입) hoặc concern.

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

Nó không có nghĩa “vòng lặp (loop / 루프) qua book rồi chạy khối (block / 블록) này” một cách imperative. Nó nói rằng processor hãy chọn các `book` rồi dispatch từng nút (node / 노드) qua template phù hợp.

Cách nghĩ template-driven giúp biểu định kiểu (stylesheet / 스타일시트) lớn có cấu trúc tốt hơn:

```text
match root
→ apply section templates
→ each section template delegates children
→ specialized templates override details
```

Nếu bạn dùng `xsl:for-each` cho mọi thứ, XSLT dễ biến thành imperative mã (code / 코드) khó maintain.

---

## 4. `xsl:value-of`

```xml
<xsl:value-of select="title"/>
```

lấy giá trị (value / 값) theo XPath expression rồi đầu ra (output / 출력) nó theo ngữ nghĩa (semantics / 의미론) của XSLT phiên bản (version / 버전).

Đừng dùng `value-of` như mặc định cho mọi nested content. Nếu nguồn (source / 소스) có mixed content:

```xml
<p>Hello <em>world</em>!</p>
```

và bạn muốn preserve markup ngữ nghĩa (semantics / 의미론), `apply-templates` thường phù hợp hơn việc chỉ lấy string giá trị (value / 값).

---

## 5. `xsl:for-each`

```xml
<xsl:for-each select="book">
  <p>
    <xsl:value-of select="title"/>
  </p>
</xsl:for-each>
```

`for-each` hoàn toàn hợp lệ và useful. Nhưng cấp cao (senior / 시니어) cần biết khi nào nó làm biểu định kiểu (stylesheet / 스타일시트) trở nên procedural quá mức.

Nếu same nút (node / 노드) cần nhiều rendering modes hoặc override hành vi (behavior / 동작) theo kiểu (type / 타입), template dispatch thường flexible hơn.

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

XSLT conditions dùng XPath expressions. Vì vậy hiểu XPath kiểu (type / 타입) mô hình (model / 모델) và chuỗi (sequence / 시퀀스) ngữ nghĩa (semantics / 의미론) rất quan trọng khi biểu định kiểu (stylesheet / 스타일시트) phức tạp.

---

## 7. Variables trong XSLT

```xml
<xsl:variable
  name="total"
  select="sum(item/price)"/>
```

Đừng nghĩ variable trong XSLT giống mutable variable trong Java. XSLT thiên functional/declarative. Một binding thường biểu diễn một giá trị (value / 값), không phải một ô nhớ bạn mutate theo vòng lặp (loop / 루프).

Tư duy immutable binding giúp transformation dễ reason hơn và phù hợp streaming/parallel tối ưu hóa (optimization / 최적화) hơn.

---

## 8. Modes

Modes cho phép cùng nguồn (source / 소스) nút (node / 노드) được xử lý khác nhau tùy concern.

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

Modes là một trong những công cụ quan trọng để chia một biểu định kiểu (stylesheet / 스타일시트) lớn thành các processing pipelines rõ ràng.

---

## 9. XSLT hiện đại không dừng ở phiên bản (version / 버전) 1.0

Nhiều nhà phát triển (developer / 개발자) chỉ từng gặp XSLT 1.0 trong hệ thống legacy nên nghĩ XSLT là một ngôn ngữ cũ, yếu và khó dùng. XSLT 2.0/3.0 cùng XPath hiện đại có hệ kiểu (type system / 타입 시스템), functions, grouping, packages, maps, arrays và streaming features mạnh hơn rất nhiều.

Điểm quan trọng không phải bạn phải dùng XSLT 3.0 ở mọi nơi, mà là khi rà soát (review / 검토) một hệ thống (system / 시스템), bạn phải biết processor đang hỗ trợ (support / 지원) phiên bản (version / 버전) nào. cú pháp (syntax / 문법) và năng lực (capability / 역량) có thể khác rất xa.

---

## 10. XSLT streaming

Nếu nguồn (source / 소스) XML là 20 GB, việc bản dựng (build / 빌드) toàn cây (tree / 트리) trước transformation có thể không khả thi. XSLT 3.0 có các streaming-oriented capabilities giúp processor xử lý dữ liệu theo stream trong những các ràng buộc (constraints / 제약조건들) nhất định.

Streaming biểu định kiểu (stylesheet / 스타일시트) không thể tùy ý “quay lại ancestor xa”, truy vấn (query / 쿼리) toàn descendants tương lai hoặc sort toàn dataset mà không buffer, vì processor chưa thấy toàn dữ liệu (data / 데이터).

Cấp cao (senior / 시니어) phải hiểu rằng streaming không chỉ là bật một flag. Transformation lô-gic (logic / 논리) phải **streamable**.

---

# XQuery

## 11. XQuery là gì?

XQuery là ngôn ngữ truy vấn (query / 쿼리) đầy đủ cho XML/XDM. Nếu XPath là expression ngôn ngữ (language / 언어), XQuery bổ sung cấu trúc để truy vấn (query / 쿼리), filter, phép nối (join / 조인), sort, group và construct kết quả (result / 결과).

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

XQuery rất phù hợp với XML-native databases hoặc hệ thống cần truy vấn (query / 쿼리) collections of XML documents.

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

Đây là một chuỗi xử lý (pipeline / 파이프라인) declarative. hiện đại (modern / 현대적) XQuery có thêm nhiều clauses nhưng FLWOR là mô hình tư duy (mental model / 사고 모델) cơ bản.

---

## 13. XPath và XQuery khác nhau ở đâu?

XPath thường được embed vào XSLT, Java API, lược đồ (schema / 스키마) assertions hoặc tools để select/calculate.

XQuery là một full ngôn ngữ (language / 언어) có thể tạo đầu ra (output / 출력) mới, define functions và implement truy vấn (query / 쿼리) lô-gic (logic / 논리) lớn.

Nếu chỉ cần lấy `/order/item/price`, XPath là đủ. Nếu cần phép nối (join / 조인) hai collections, aggregate, sort rồi construct report XML, XQuery phù hợp hơn.

---

# XDM và XPath nâng cao

## 14. XDM là gì?

XDM là **XQuery and XPath mô hình dữ liệu (data model / 데이터 모델)**. Đây là mô hình dữ liệu (data model / 데이터 모델) nền của XPath/XQuery/XSLT hiện đại.

XDM không chỉ có XML nodes. Nó còn có atomic values, sequences và trong 3.1 còn có hàm (function / 함수) items, maps và arrays.

Ví dụ XPath expression:

```xpath
(1, 2, 3)
```

trả về một chuỗi (sequence / 시퀀스) ba atomic values.

Điều này rất khác mô hình tư duy (mental model / 사고 모델) XPath 1.0 kiểu “mọi thứ là nút (node / 노드) set, string, number hoặc boolean”.

---

## 15. chuỗi (sequence / 시퀀스)

Chuỗi (sequence / 시퀀스) là ordered chuỗi (sequence / 시퀀스) of items.

Một expression có thể trả:

```text
zero items
one item
many items
```

Item có thể là nút (node / 노드) hoặc atomic giá trị (value / 값).

Không phải chuỗi (sequence / 시퀀스) nào cũng là danh sách (list / 목록) đối tượng (object / 객체) như Java, nhưng mô hình tư duy (mental model / 사고 모델) “ordered kết quả (result / 결과) of items” là đúng.

---

## 16. XPath axes

XPath có nhiều axes để di chuyển trong cây (tree / 트리):

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

Axes giúp truy vấn (query / 쿼리) rõ ràng và precise hơn việc dùng `//` rồi filter rộng.

---

## 17. Namespace-safe XPath

Đây là quy tắc (rule / 규칙) cấp cao (senior / 시니어) phải coi như phản xạ.

Đầu vào (input / 입력) A:

```xml
<a:order xmlns:a="urn:order"/>
```

Đầu vào (input / 입력) B:

```xml
<o:order xmlns:o="urn:order"/>
```

Hai đầu vào (input / 입력) cùng ngữ nghĩa (semantics / 의미론).

XPath ứng dụng (application / 애플리케이션) nên bind một prefix riêng:

```text
ord → urn:order
```

sau đó truy vấn (query / 쿼리):

```xpath
/ord:order
```

Không bao giờ coi prefix nguồn (source / 소스) là định danh (identity / 식별자).

---

# Lược đồ (schema / 스키마) thiết kế (design / 설계) và đặc tả hợp đồng (contract / 계약) Evolution

## 18. không gian tên (namespace / 네임스페이스) phải stable

Không gian tên (namespace / 네임스페이스) URI là định danh (identity / 식별자) của vocabulary. Đừng đổi không gian tên (namespace / 네임스페이스) chỉ vì:

```text
website đổi domain
server migrate
XSD file chuyển folder
team đổi tên
```

Nếu bạn đổi không gian tên (namespace / 네임스페이스), bên tiêu thụ (consumer / 소비자) có thể coi toàn bộ element là vocabulary mới.

Không gian tên (namespace / 네임스페이스) nên được phiên bản (version / 버전)/govern như một API định danh (identity / 식별자).

---

## 19. phiên bản (version / 버전) trong không gian tên (namespace / 네임스페이스)

Một chiến lược (strategy / 전략) là:

```text
urn:example:order:v1
urn:example:order:v2
```

Ưu điểm là breaking phiên bản (version / 버전) ranh giới (boundary / 경계) rất rõ. bên tiêu thụ (consumer / 소비자) không thể vô tình coi v2 là v1.

Nhược điểm là mọi XPath, XSD import, binding, serializer và message đều phải đổi không gian tên (namespace / 네임스페이스) khi phiên bản (version / 버전) đổi.

Chiến lược (strategy / 전략) này hợp khi major versions thực sự độc lập.

---

## 20. Stable không gian tên (namespace / 네임스페이스) + phiên bản (version / 버전) attribute

Một chiến lược (strategy / 전략) khác:

```xml
<order
  xmlns="urn:example:order"
  version="2">
```

Không gian tên (namespace / 네임스페이스) giữ ổn định, phiên bản (version / 버전) nằm trong dữ liệu (data / 데이터).

Ưu điểm là truy vấn (query / 쿼리) không gian tên (namespace / 네임스페이스) và vocabulary định danh (identity / 식별자) ít churn hơn.

Nhược điểm là ứng dụng (application / 애플리케이션) phải có lô-gic (logic / 논리) rõ để phân biệt phiên bản (version / 버전) ngữ nghĩa (semantics / 의미론), và lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증)/phiên bản (version / 버전) routing có thể phức tạp hơn.

Không có một chiến lược (strategy / 전략) luôn đúng.

---

## 21. Backward-compatible thay đổi (change / 변경)

Thêm optional element thường dễ compatible hơn:

```xml
<xs:element
  name="memo"
  minOccurs="0"/>
```

Nếu bên tiêu thụ (consumer / 소비자) cũ tolerant đúng cách, nó có thể ignore trường dữ liệu (field / 필드) mới.

Những thay đổi dễ breaking gồm rename required trường dữ liệu (field / 필드), đổi không gian tên (namespace / 네임스페이스), đổi kiểu (type / 타입) từ string sang decimal khi old values không hợp, đổi thứ tự (order / 순서) trong strict chuỗi (sequence / 시퀀스), hoặc làm optional trường dữ liệu (field / 필드) thành required.

Lược đồ (schema / 스키마) evolution phải được treat như API evolution.

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

Điều này rất hữu ích với giao thức (protocol / 프로토콜) cần vendor extension.

Nhưng `xs:any` ở khắp nơi sẽ làm lược đồ (schema / 스키마) gần như không còn ý nghĩa. Một good extension điểm (point / 지점) phải có location, không gian tên (namespace / 네임스페이스) chính sách (policy / 정책) và kiểm tra hợp lệ (validation / 검증) chính sách (policy / 정책) rõ.

---

## 23. `processContents`

`strict`, `lax`, `skip` điều khiển wildcard processing.

`strict` yêu cầu content được validate theo lược đồ (schema / 스키마) rules phù hợp.

`lax` cho phép validate nếu có declaration/lược đồ (schema / 스키마) phù hợp, còn nếu không có thì có thể tiếp tục.

`skip` nói không schema-validate wildcard content.

Nếu bạn dùng `skip` cho security-sensitive extension, ứng dụng (application / 애플리케이션) vẫn phải validate nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) ở tầng (layer / 계층) khác.

---

## 24. định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들)

XSD có `xs:unique`, `xs:key`, `xs:keyref`.

Chúng cho phép enforce một số relational-like các ràng buộc (constraints / 제약조건들) trong document.

Ví dụ một danh sách (list / 목록) customer có ID unique, rồi thứ tự (order / 순서) tham chiếu (reference / 참조) customer bằng keyref.

Điều này hữu ích khi XML document là một self-contained dataset có nội bộ (internal / 내부) references.

---

## 25. `xs:unique`

`xs:unique` bảo đảm values được chọn bởi selector/trường dữ liệu (field / 필드) không trùng lặp theo lược đồ (schema / 스키마) ngữ nghĩa (semantics / 의미론).

Nó thích hợp với nghiệp vụ (business / 비즈니스) điều kiện (condition / 조건) kiểu “mọi SKU trong danh sách (list / 목록) phải unique”.

---

## 26. `xs:key`

`xs:key` giống key ràng buộc (constraint / 제약조건) với ngữ nghĩa (semantics / 의미론) chặt hơn về presence/giá trị (value / 값) theo XSD rules.

Nó có thể được tham chiếu (reference / 참조) bởi `xs:keyref`.

---

## 27. `xs:keyref`

`xs:keyref` cho phép một trường dữ liệu (field / 필드) trỏ tới key được định nghĩa.

Ví dụ:

```text
order/customerRef
```

phải match một customer ID tồn tại trong document.

Đây là integrity ràng buộc (constraint / 제약조건) ở lược đồ (schema / 스키마) tầng (layer / 계층).

---

## 28. Complex kiểu (type / 타입) derivation

XSD có extension và restriction.

Ví dụ một `EmployeeType` có thể extend `PersonType`.

```xml
<xs:complexContent>
  <xs:extension base="PersonType">
    ...
  </xs:extension>
</xs:complexContent>
```

Giống OO inheritance, kiểu (type / 타입) derivation mạnh nhưng có thể bị lạm dụng.

Một lược đồ (schema / 스키마) inheritance cây (tree / 트리) sâu làm bên tiêu thụ (consumer / 소비자) khó hiểu và mã (code / 코드) generation khó maintain. Composition thường dễ reason hơn nếu lĩnh vực (domain / 도메인) không thực sự cần polymorphism.

---

## 29. `xsi:type`

Instance có thể chọn derived kiểu (type / 타입):

```xml
<person
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:type="EmployeeType">
```

nếu lược đồ (schema / 스키마) cho phép.

`xsi:type` hữu ích nhưng làm instance document gắn chặt hơn với lược đồ (schema / 스키마) hệ kiểu (type system / 타입 시스템). Nếu đặc tả hợp đồng (contract / 계약) cần simple interoperability, tường minh (explicit / 명시적) elements đôi khi dễ hơn.

---

## 30. Substitution groups

Substitution group cho phép element declarations thay thế một head element theo lược đồ (schema / 스키마) rules.

Nó hỗ trợ polymorphic XML vocabulary.

Nhưng khi kết hợp với derived types và `xsi:type`, lược đồ (schema / 스키마) có thể rất khó đọc. cấp cao (senior / 시니어) phải cân bằng flexibility với maintainability.

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

Nếu Java binding map cả ba thành `null` hoặc `""`, nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론) có thể bị mất.

Đặc tả hợp đồng (contract / 계약) phải định nghĩa rõ điều này.

---

# XML Binding và Java

## 32. XML đối tượng (object / 객체) binding là convenience tầng (layer / 계층), không phải XML replacement

Khung phần mềm (framework / 프레임워크) như JAXB/Jakarta XML Binding có thể map:

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

Đây là developer-friendly lớp trừu tượng (abstraction / 추상화).

Nhưng XML có nhiều concepts OO mô hình (model / 모델) không biểu diễn tự nhiên: mixed content, attribute vs element, không gian tên (namespace / 네임스페이스), thứ tự (order / 순서), unknown extensions, substitution groups, nil-vs-missing.

Nếu tích hợp (integration / 통합) phức tạp, đừng để generated classes che mất đặc tả hợp đồng (contract / 계약) ngữ nghĩa (semantics / 의미론).

---

## 33. Contract-first vs object-first ở mức cấp cao (senior / 시니어)

Trong enterprise tích hợp (integration / 통합), một lược đồ (schema / 스키마) được nhiều Java/.NET/vendor các hệ thống (systems / 시스템들) dùng thường nên được thiết kế như một language-neutral đặc tả hợp đồng (contract / 계약).

Nếu generate XSD trực tiếp từ Java lớp (class / 클래스), lược đồ (schema / 스키마) dễ mang theo những quyết định nội bộ của Java mô hình (model / 모델) như inheritance, collection wrapper hoặc naming conventions mà partner không cần biết.

Vì vậy contract-first thường phù hợp với long-lived cross-system XML interfaces.

---

# Large XML và Streaming

## 34. Vì sao DOM có thể rất tốn bộ nhớ (memory / 메모리)?

Raw XML 500 MB không có nghĩa DOM chỉ dùng 500 MB RAM.

Một DOM cây (tree / 트리) cần đối tượng (object / 객체) cho mỗi element, văn bản (text / 텍스트) nút (node / 노드), attribute, không gian tên (namespace / 네임스페이스) binding và collections/pointers. bộ nhớ (memory / 메모리) footprint có thể tăng nhiều lần so với nguồn (source / 소스).

Vì vậy large XML phải được benchmark bằng actual parser, không estimate từ tệp (file / 파일) kích thước (size / 크기).

---

## 35. Streaming Parser mẫu (pattern / 패턴)

Với record-oriented XML:

```xml
<records>
  <record>...</record>
  <record>...</record>
</records>
```

StAX chuỗi xử lý (pipeline / 파이프라인) có thể:

```text
đọc tới <record>
→ parse fields
→ tạo domain object
→ process/write DB
→ discard object
→ đọc record tiếp theo
```

Bộ nhớ (memory / 메모리) gần như phụ thuộc kích thước (size / 크기) của một bản ghi (record / 레코드) thay vì kích thước (size / 크기) toàn tệp (file / 파일).

---

## 36. Partial Materialization

Bạn không bắt buộc phải stream từng thành phần nguyên thủy (primitive / 기본 요소) trường dữ liệu (field / 필드) bằng tay.

Một mẫu (pattern / 패턴) tốt là stream outer document, rồi khi tới một `<record>`, materialize riêng subtree đó thành đối tượng (object / 객체) hoặc mini-DOM, xử lý xong rồi discard.

Luồng (flow / 흐름):

```text
StAX outer loop
→ capture one record
→ JAXB/DOM record
→ business process
→ release
```

Đây là compromise rất practical.

---

## 37. Streaming không giải quyết mọi bộ nhớ (memory / 메모리) bài toán (problem / 문제)

Nếu yêu cầu (requirement / 요구사항) nói “mọi customer ID phải unique toàn tệp (file / 파일)”, bạn vẫn cần trạng thái (state / 상태) như HashSet hoặc bên ngoài (external / 외부) cơ sở dữ liệu (database / 데이터베이스).

Nếu cần sort toàn bộ bản ghi (record / 레코드), bạn phải buffer hoặc dùng bên ngoài (external / 외부) sort.

Streaming chỉ giúp không giữ toàn cây (tree / 트리). Nó không loại yêu cầu (requirement / 요구사항) lưu trạng thái (state / 상태) toàn cục.

---

# Bảo mật (security / 보안)

## 38. Vì sao XML có bảo mật (security / 보안) surface lớn?

XML processor lịch sử có nhiều năng lực (capability / 역량):

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

Các năng lực (capability / 역량) này rất hữu ích với trusted documents, nhưng nguy hiểm với attacker-controlled XML.

Cấp cao (senior / 시니어) phải coi parser như một thành phần (component / 컴포넌트) có filesystem/mạng (network / 네트워크) capabilities cần được sandbox/harden.

---

## 39. XXE là gì?

XXE là XML bên ngoài (external / 외부) thực thể (entity / 엔터티) attack.

Concept:

```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>

<data>&xxe;</data>
```

Nếu parser resolve thực thể (entity / 엔터티) `xxe`, nó có thể đọc cục bộ (local / 로컬) tệp (file / 파일) và đưa content vào parsed dữ liệu (data / 데이터).

Trên máy chủ (server / 서버), attack có thể nhắm:

```text
local file disclosure
SSRF
internal service access
cloud metadata endpoints
denial of service
```

Không phải mọi parser mặc định vulnerable, nhưng bạn không được dựa vào giả định (assumption / 가정). Hãy configure theo parser/phiên bản (version / 버전) thật.

---

## 40. bên ngoài (external / 외부) DTD và SSRF

Ngay cả không dùng thực thể (entity / 엔터티) trực tiếp, DOCTYPE:

```xml
<!DOCTYPE root SYSTEM
  "http://internal-service/private.dtd">
```

có thể khiến parser gửi mạng (network / 네트워크) yêu cầu (request / 요청) nếu bên ngoài (external / 외부) subset resolution enabled.

Đó là SSRF-style hành vi (behavior / 동작).

---

## 41. Parameter entities

DTD còn có parameter entities, thường dùng bên trong DTD grammar.

Bên ngoài (external / 외부) parameter thực thể (entity / 엔터티) cũng có thể trigger tài nguyên (resource / 자원) loading.

Vì vậy hardening chỉ “disable bên ngoài (external / 외부) general entities” nhưng bỏ parameter entities vẫn có thể chưa đủ.

---

## 42. Billion Laughs

Billion Laughs tận dụng recursive/nested thực thể (entity / 엔터티) expansion.

Concept đơn giản:

```text
entity A = "lol"
entity B = A repeated many times
entity C = B repeated many times
...
```

Nguồn (source / 소스) rất nhỏ nhưng expanded văn bản (text / 텍스트) có thể cực lớn, gây CPU/bộ nhớ (memory / 메모리) exhaustion.

Hiện đại (modern / 현대적) parsers thường có limits, nhưng ứng dụng (application / 애플리케이션) nên chủ động có tài nguyên (resource / 자원) limits.

---

## 43. XInclude

XInclude cho phép include bên ngoài (external / 외부) XML/tài nguyên (resource / 자원):

```xml
<xi:include
  xmlns:xi="http://www.w3.org/2001/XInclude"
  href="other.xml"/>
```

Nếu đầu vào (input / 입력) untrusted và XInclude enabled, attacker có thể influence bên ngoài (external / 외부) tài nguyên (resource / 자원) truy cập (access / 접근).

Nếu ứng dụng (application / 애플리케이션) không cần XInclude, disable nó.

---

## 44. lược đồ (schema / 스키마) resolution cũng là bên ngoài (external / 외부) truy cập (access / 접근)

XSD có imports/includes. Instance có `schemaLocation`. Nếu validator tự fetch remote schemas, attacker hoặc mạng (network / 네트워크) phụ thuộc (dependency / 의존성) có thể ảnh hưởng hành vi (behavior / 동작).

Một môi trường vận hành (production / 운영 환경) hệ thống (system / 시스템) tốt nên dùng trusted cục bộ (local / 로컬) lược đồ (schema / 스키마) registry hoặc resolver.

---

## 45. XML danh mục (catalog / 카탈로그)

XML danh mục (catalog / 카탈로그) là cơ chế ánh xạ (mapping / 매핑) bên ngoài (external / 외부) identifiers/URIs tới cục bộ (local / 로컬) resources.

Ví dụ concept:

```text
https://vendor.com/schema/order.xsd
→ /opt/app/schema/vendor-order-v3.xsd
```

Benefits gồm deterministic builds, offline processing, giảm độ trễ (latency / 지연 시간) và giảm arbitrary mạng (network / 네트워크) fetch.

Trong enterprise XML hạ tầng (infrastructure / 인프라), danh mục (catalog / 카탈로그) là công cụ (tool / 도구) rất giá trị.

---

## 46. Secure parser chiến lược (strategy / 전략)

Với untrusted XML, default mental checklist là: tắt DTD nếu không cần; tắt bên ngoài (external / 외부) general entities; tắt bên ngoài (external / 외부) parameter entities; khối (block / 블록) bên ngoài (external / 외부) DTD/lược đồ (schema / 스키마) resolution; tắt XInclude nếu không cần; giới hạn document kích thước (size / 크기)/độ sâu (depth / 깊이)/thực thể (entity / 엔터티) expansions; dùng secure processing options; và kiểm soát mọi URI resolver.

Chính xác (exact / 정확한) flag khác nhau giữa `DocumentBuilderFactory`, `SAXParserFactory`, `XMLInputFactory`, `SchemaFactory` và `TransformerFactory`.

Điều này có nghĩa không tồn tại một cấu hình (config / 설정) snippet universal cho mọi Java XML API.

---

## 47. Hardening một parser không harden toàn chuỗi xử lý (pipeline / 파이프라인)

Bạn có thể đã secure DOM parser nhưng sau đó XSLT `TransformerFactory` vẫn được phép `document()` tới bên ngoài (external / 외부) URI.

Hoặc `SchemaFactory` vẫn fetch imports.

Hoặc untrusted biểu định kiểu (stylesheet / 스타일시트) dùng extension hàm (function / 함수).

Cấp cao (senior / 시니어) phải threat-model từng thành phần (component / 컴포넌트):

```text
parser
validator
XPath/XQuery engine
XSLT engine
serializer
signature verifier
```

---

## 48. XSLT bảo mật (security / 보안)

XSLT có thể include/import stylesheets và trong một số processor có khả năng truy cập (access / 접근) bên ngoài (external / 외부) documents hoặc extension functions.

Do đó “untrusted XML” và “untrusted XSLT” là hai threat các mô hình (models / 모델들) khác nhau.

Không execute biểu định kiểu (stylesheet / 스타일시트) do người dùng (user / 사용자) upload với unrestricted server-side processor nếu không có sandbox/chính sách (policy / 정책).

---

## 49. XPath Injection

Nếu mã (code / 코드) bản dựng (build / 빌드) expression:

```java
String xpath =
    "/users/user[name='" + input + "']";
```

thì đầu vào (input / 입력) chứa quotes hoặc XPath cú pháp (syntax / 문법) có thể thay đổi truy vấn (query / 쿼리).

Concept giống SQL Injection.

Defense là dùng variable binding nếu engine hỗ trợ, không cho người dùng (user / 사용자) cung cấp arbitrary expression fragments, hoặc validate đầu vào (input / 입력) theo allowlist rõ ràng.

---

# Canonicalization và XML Signature

## 50. Vì sao không thể băm (hash / 해시) raw XML văn bản (text / 텍스트) một cách ngây thơ?

Hai serializations:

```xml
<user id="1" active="true"/>
```

và:

```xml
<user active="true" id="1"></user>
```

có thể mang cùng thông tin (information / 정보) theo XML mô hình dữ liệu (data model / 데이터 모델) nhưng raw bytes khác.

Nếu signature phụ thuộc raw formatting, chỉ cần formatter đổi attribute thứ tự (order / 순서) hoặc empty element notation là băm (hash / 해시) thất bại (fail / 실패).

Chuẩn gốc (canonical / 정본) XML giải quyết bằng cách tạo biểu diễn (representation / 표현) deterministic theo thuật toán (algorithm / 알고리즘) chuẩn.

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

Signature thường chứa references, transforms, digest và signature giá trị (value / 값).

Điểm quan trọng là “signature valid” không có nghĩa toàn bộ XML document được nghiệp vụ (business / 비즈니스) ứng dụng (application / 애플리케이션) tin tưởng. Nó chỉ chứng minh references đã verify theo signature ngữ nghĩa (semantics / 의미론) và trusted key.

Ứng dụng (application / 애플리케이션) phải hiểu signed phạm vi (scope / 범위).

---

## 53. Signature Wrapping Attack

Một attack lớp (class / 클래스) quan trọng là signature wrapping.

Concept:

```text
signed element A hợp lệ
attacker thêm element B
signature verifier xác nhận A
business code query nhầm B
```

Ví dụ verifier verify element có ID `signed-order`, nhưng ứng dụng (application / 애플리케이션) sau đó chạy:

```java
getElementsByTagName("Order").item(0)
```

và nhận một attacker-controlled `Order` khác.

Defense là ứng dụng (application / 애플리케이션) phải tiến trình (process / 프로세스) **chính xác (exact / 정확한) nút (node / 노드) đã được signature verifier xác nhận**, không verify xong rồi truy vấn (query / 쿼리) document một lần nữa bằng selector mơ hồ.

---

## 54. ID ngữ nghĩa (semantics / 의미론) và signature

Tham chiếu (reference / 참조) kiểu:

```text
#order123
```

cần processor biết attribute nào là ID.

ID ngữ nghĩa (semantics / 의미론) có thể đến từ DTD, XSD, `xml:id` hoặc API/thư viện (library / 라이브러리) cấu hình (configuration / 구성).

Một attribute tên `id` không tự động có ID ngữ nghĩa (semantics / 의미론) trong mọi XML API.

Đây là một chi tiết nhỏ nhưng cực kỳ quan trọng với XML Signature bảo mật (security / 보안).

---

# Tích hợp (integration / 통합) kiến trúc (architecture / 아키텍처)

## 55. ranh giới (boundary / 경계) kiểm tra hợp lệ (validation / 검증) mẫu (pattern / 패턴)

Một inbound chuỗi xử lý (pipeline / 파이프라인) tốt có thể là:

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

XSD không thay authorization. Parser bảo mật (security / 보안) không thay nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증). ánh xạ (mapping / 매핑) không thay lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증).

---

## 56. lược đồ (schema / 스키마) compilation bộ nhớ đệm (cache / 캐시)

XSD compilation có chi phí (cost / 비용). Nếu mỗi yêu cầu (request / 요청) đều đọc XSD từ disk, resolve imports và compile lại, độ trễ (latency / 지연 시간) và CPU sẽ tăng.

Mẫu (pattern / 패턴) tốt:

```text
load trusted schemas at startup
→ compile
→ cache compiled schema
→ create validator instances theo library contract
```

Tương tự, XSLT biểu định kiểu (stylesheet / 스타일시트) có thể được compile/bộ nhớ đệm (cache / 캐시) nếu processor API cho phép.

---

## 57. Strict Reader vs Tolerant Reader

Strict reader reject trường dữ liệu (field / 필드) lạ.

Ưu điểm là đặc tả hợp đồng (contract / 계약) predictable và bảo mật (security / 보안) dễ reason.

Nhược điểm là forward tính tương thích (compatibility / 호환성) thấp.

Tolerant reader cho phép unknown optional extensions.

Ưu điểm là lược đồ (schema / 스키마) evolution tốt hơn.

Nhược điểm là bên tiêu thụ (consumer / 소비자) có thể silently ignore ngữ nghĩa (semantic / 의미적) quan trọng.

Một cấp cao (senior / 시니어) đặc tả hợp đồng (contract / 계약) phải nói rõ unknown element chính sách (policy / 정책), thay vì để parser hành vi (behavior / 동작) quyết định ngẫu nhiên.

---

## 58. “Be liberal in what you accept” không phải lúc nào tốt

Postel's Law từng rất phổ biến trong giao thức (protocol / 프로토콜) thiết kế (design / 설계), nhưng với security-critical contracts, quá tolerant có thể che lỗi hoặc bypass kiểm tra hợp lệ (validation / 검증).

Một chiến lược (strategy / 전략) hiện đại hơn là:

```text
strict core
explicit versioning
explicit extension points
known tolerance policy
```

---

## 59. Envelope mẫu (pattern / 패턴)

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

Header chứa cross-cutting siêu dữ liệu (metadata / 메타데이터) như correlation ID, routing, phiên bản (version / 버전), bảo mật (security / 보안) thông tin (information / 정보). Body chứa nghiệp vụ (business / 비즈니스) payload.

SOAP là ví dụ nổi tiếng của mẫu (pattern / 패턴) này.

---

## 60. không gian tên (namespace / 네임스페이스) Extension mẫu (pattern / 패턴)

Cốt lõi (core / 핵심) vocabulary:

```text
urn:example:order
```

Partner extension:

```text
urn:partner:custom
```

XML không gian tên (namespace / 네임스페이스) giúp hai bên mở rộng cùng document mà tránh collision.

Nếu lược đồ (schema / 스키마) có controlled wildcard extension điểm (point / 지점), partner có thể thêm siêu dữ liệu (metadata / 메타데이터) mà không đổi cốt lõi (core / 핵심) không gian tên (namespace / 네임스페이스).

---

## 61. lược đồ (schema / 스키마) Registry mẫu (pattern / 패턴)

Một tổ chức lớn nên quản lý lược đồ (schema / 스키마) giống API artifacts.

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

Không nên để mỗi nhóm (team / 팀) bản sao (copy / 복사) `common.xsd` khác nhau rồi tự sửa.

---

## 62. chuẩn gốc (canonical / 정본) mô hình dữ liệu (data model / 데이터 모델) mẫu (pattern / 패턴)

Nếu hệ thống nhận:

```text
Partner A XML
Partner B XML
Legacy SOAP XML
```

Nghiệp vụ (business / 비즈니스) mã (code / 코드) không nên hiểu từng bên ngoài (external / 외부) lược đồ (schema / 스키마).

Bạn có thể transform/map tất cả thành nội bộ (internal / 내부) chuẩn gốc (canonical / 정본) mô hình (model / 모델).

Luồng (flow / 흐름):

```text
external XML
→ adapter / XSLT / mapper
→ canonical internal model
→ business services
```

Điều này giảm coupling.

Nhưng một chuẩn gốc (canonical / 정본) mô hình (model / 모델) quá generic cho toàn enterprise có thể thành “god mô hình (model / 모델)”. Nên phạm vi (scope / 범위) theo bounded ngữ cảnh (context / 맥락)/lĩnh vực (domain / 도메인).

---

## 63. Anti-Corruption tầng (layer / 계층)

DDD gọi tầng (layer / 계층) bảo vệ lĩnh vực (domain / 도메인) khỏi bên ngoài (external / 외부) mô hình (model / 모델) là Anti-Corruption tầng (layer / 계층).

XML legacy thường rất phù hợp mẫu (pattern / 패턴) này:

```text
vendor XML
→ parser
→ validation
→ transformation
→ internal DTO/domain
```

Legacy naming, không gian tên (namespace / 네임스페이스), null ngữ nghĩa (semantics / 의미론) và lược đồ (schema / 스키마) quirks dừng lại ở ranh giới (boundary / 경계).

---

# XML thiết kế (design / 설계) Idioms

## 64. tường minh (explicit / 명시적) units

Nếu number không có globally fixed đơn vị (unit / 단위), nên biểu diễn rõ:

```xml
<weight unit="kg">64</weight>
```

thay vì:

```xml
<weight>64</weight>
```

và để bên tiêu thụ (consumer / 소비자) đoán.

---

## 65. Stable identifiers

Nếu có:

```xml
<customer id="C123">
```

Đặc tả hợp đồng (contract / 계약) phải làm rõ ID unique ở phạm vi (scope / 범위) nào, có case-sensitive không, có tái sử dụng không và tồn tại bao lâu.

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

Wrapper giúp collection có chỗ chứa siêu dữ liệu (metadata / 메타데이터) như count, pagination hoặc future options. Nhưng nó làm lược đồ (schema / 스키마) verbose hơn.

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

Option A giúp lược đồ (schema / 스키마) compact, option B làm element ngữ nghĩa (semantics / 의미론) tường minh (explicit / 명시적) hơn.

Nếu mỗi contact kiểu (type / 타입) có cấu trúc (structure / 구조) khác nhau, distinct elements hoặc hệ kiểu (type system / 타입 시스템) thường rõ hơn discriminator string.

---

# Cấp cao (senior / 시니어) Anti-patterns

## 68. Đổi không gian tên (namespace / 네임스페이스) cho mọi minor bản phát hành (release / 릴리스)

Nếu `v1.1`, `v1.2`, `v1.3` đều có không gian tên (namespace / 네임스페이스) mới, bên tiêu thụ (consumer / 소비자) phải cập nhật (update / 업데이트) XPath/binding liên tục.

Chỉ phiên bản (version / 버전) không gian tên (namespace / 네임스페이스) khi chiến lược (strategy / 전략) thực sự yêu cầu breaking định danh (identity / 식별자).

---

## 69. `xs:any` ở mọi nơi

Lược đồ (schema / 스키마) nhìn flexible nhưng không validate được gì đáng kể.

Extension phải có ranh giới (boundary / 경계) rõ.

---

## 70. Deep inheritance cây (tree / 트리)

Lược đồ (schema / 스키마) kiểu (type / 타입) inheritance 7 tầng có thể làm generated mã (code / 코드) cực khó hiểu.

Nếu composition đủ, composition thường dễ maintain hơn.

---

## 71. Monolithic XSD

Một tệp (file / 파일) XSD chứa mọi lĩnh vực (domain / 도메인), phiên bản (version / 버전) và extension trở thành bottleneck quản trị (governance / 거버넌스).

Chia mô-đun (module / 모듈) theo vocabulary/lĩnh vực (domain / 도메인) và quản lý imports rõ ràng.

---

## 72. Everything required

Nếu mọi trường dữ liệu (field / 필드) bắt buộc, thêm tính năng (feature / 기능) mới gần như luôn breaking.

---

## 73. Everything optional

Nếu mọi trường dữ liệu (field / 필드) optional, lược đồ (schema / 스키마) không còn enforce nghiệp vụ (business / 비즈니스) shape.

Cấp cao (senior / 시니어) phải cân bằng evolvability và tính đúng đắn (correctness / 정확성).

---

# Hiệu năng (performance / 성능) và khả năng quan sát (observability / 관측 가능성)

## 74. hiệu năng (performance / 성능) limits

Môi trường vận hành (production / 운영 환경) XML processing nên nghĩ tới max bytes, độ sâu (depth / 깊이), number of elements, number of attributes, max văn bản (text / 텍스트) nút (node / 노드) kích thước (size / 크기), thực thể (entity / 엔터티) expansion limits và processing hết thời gian chờ (timeout / 타임아웃).

Bảo mật (security / 보안) và hiệu năng (performance / 성능) ở đây liên quan chặt nhau vì attacker có thể dùng XML độ phức tạp (complexity / 복잡도) để tiêu tốn CPU/RAM.

---

## 75. Logging

Khi kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패), log nên giúp gỡ lỗi (debug / 디버그):

```text
message type
namespace
schema version
correlation ID
line/column
validation path
error code
```

Nhưng không dump toàn XML nếu payload chứa password, PII hoặc financial dữ liệu (data / 데이터).

Một log “đủ để gỡ lỗi (debug / 디버그)” không đồng nghĩa “log toàn payload”.

---

## 76. Golden document tests

Một XML đặc tả hợp đồng (contract / 계약) tốt nên có mẫu (sample / 표본) tests cho minimum valid, full valid, old phiên bản (version / 버전), future extension, missing trường dữ liệu (field / 필드), nil trường dữ liệu (field / 필드), empty trường dữ liệu (field / 필드), wrong thứ tự (order / 순서), invalid kiểu (type / 타입), very large payload và malicious XXE đầu vào (input / 입력).

Các fixtures này giúp regression kiểm thử (test / 테스트) lược đồ (schema / 스키마), parser cấu hình (config / 설정) và ánh xạ (mapping / 매핑) mã (code / 코드).

---

## 77. mô hình tư duy (mental model / 사고 모델) sau cấp cao (senior / 시니어)

Sau phần này, luồng (flow / 흐름) hoàn chỉnh hơn là:

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

Nếu bạn hiểu được luồng (flow / 흐름) này và biết mỗi stage giải quyết vấn đề gì, bạn đã vượt khỏi mức “nhà phát triển (developer / 개발자) biết XML” và bắt đầu xử lý XML như một cấp cao (senior / 시니어) tích hợp (integration / 통합) engineer.

---

# PHẦN BỔ SUNG — SOAP, WSDL VÀ XML TRONG ENTERPRISE tích hợp (integration / 통합)

## 78. SOAP là gì và vì sao nó gắn chặt với XML?

SOAP là một **messaging khung phần mềm (framework / 프레임워크)** dùng XML để đóng gói message. Khi nói SOAP, đừng chỉ nghĩ “API trả XML thay vì JSON”. SOAP định nghĩa một processing mô hình (model / 모델) với envelope, header blocks, body, faults, namespaces và khả năng mở rộng theo modules. XML phù hợp với SOAP vì không gian tên (namespace / 네임스페이스) cho phép nhiều chuẩn hoặc vendor extensions cùng xuất hiện trong một message mà không đụng tên, còn XSD cung cấp đặc tả hợp đồng (contract / 계약) kiểu (type / 타입)/cấu trúc (structure / 구조) rất mạnh.

Một SOAP 1.2 message tối giản có thể có dạng:

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

`Envelope` là outermost SOAP element. `Header` là optional và chứa zero hoặc nhiều header blocks. `Body` là nơi mang thông tin (information / 정보) hướng tới ultimate receiver. nghiệp vụ (business / 비즈니스) payload như `o:GetOrder` không thuộc SOAP không gian tên (namespace / 네임스페이스); nó thuộc vocabulary `urn:example:order`. Chính sự tách không gian tên (namespace / 네임스페이스) này làm SOAP extensible.

SOAP 1.1 và SOAP 1.2 có không gian tên (namespace / 네임스페이스)/giao thức (protocol / 프로토콜) details khác nhau. SOAP 1.2 dùng envelope không gian tên (namespace / 네임스페이스) `http://www.w3.org/2003/05/soap-envelope`; hệ thống SOAP 1.1 legacy thường dùng `http://schemas.xmlsoap.org/soap/envelope/`. Vì vậy khi gỡ lỗi (debug / 디버그) một SOAP tích hợp (integration / 통합), phiên bản (version / 버전) không phải chi tiết nhỏ: không gian tên (namespace / 네임스페이스), HTTP binding và fault format có thể khác.

---

## 79. SOAP Header không chỉ là chỗ đặt siêu dữ liệu (metadata / 메타데이터) tùy ý

SOAP Header được thiết kế để mang các blocks có ngữ nghĩa (semantics / 의미론) xử lý riêng, ví dụ bảo mật (security / 보안), giao dịch (transaction / 트랜잭션), routing, correlation hoặc addressing. Header khối (block / 블록) có thể mục tiêu (target / 대상) một nút (node / 노드)/intermediary cụ thể trên message đường dẫn (path / 경로).

SOAP còn có concept `mustUnderstand`. Nếu một header khối (block / 블록) bắt buộc phải được hiểu mà nút (node / 노드) nhận message không hiểu ngữ nghĩa (semantics / 의미론) của khối (block / 블록) đó, nút (node / 노드) không nên im lặng bỏ qua rồi xử lý nghiệp vụ (business / 비즈니스) body như bình thường; SOAP processing mô hình (model / 모델) có fault hành vi (behavior / 동작) cho tình huống này.

Điểm này cho thấy SOAP khác một JSON đối tượng (object / 객체) có trường dữ liệu (field / 필드) `headers`. Header trong SOAP là một phần của processing mô hình (model / 모델), không chỉ là convention do ứng dụng (application / 애플리케이션) tự nghĩ ra.

---

## 80. SOAP Body và nghiệp vụ (business / 비즈니스) payload

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

SOAP chỉ định envelope/body cấu trúc (structure / 구조), còn `Transfer`, `from`, `to`, `amount` là đặc tả hợp đồng (contract / 계약) của payment dịch vụ (service / 서비스). Các elements nghiệp vụ (business / 비즈니스) này thường được mô tả bằng XSD và được tham chiếu (reference / 참조)/import từ WSDL.

Điều đó tạo một layering rất rõ:

```text
XML syntax
→ SOAP envelope vocabulary
→ application namespace/vocabulary
→ XSD types
→ business semantics
```

Khi lỗi xảy ra, phải xác định lỗi nằm ở tầng (layer / 계층) nào thay vì chỉ nhìn “SOAP yêu cầu (request / 요청) invalid”.

---

## 81. SOAP Fault

SOAP dùng `Fault` để biểu diễn lỗi theo message format chuẩn. Với SOAP 1.2, Fault có các phần như mã (code / 코드), Reason và optional Detail.

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

Điểm cấp cao (senior / 시니어) cần hiểu là HTTP status và SOAP Fault là hai layers khác nhau. Một tích hợp (integration / 통합) khung phần mềm (framework / 프레임워크) có thể map vận chuyển (transport / 전송) thất bại (failure / 실패), SOAP giao thức (protocol / 프로토콜) fault và nghiệp vụ (business / 비즈니스) lỗi (error / 오류) theo cách khác nhau. Khi log/gỡ lỗi (debug / 디버그), phải giữ distinction này.

---

## 82. WSDL là gì?

WSDL là **Web Services Description ngôn ngữ (language / 언어)**. Trong các SOAP các hệ thống (systems / 시스템들) truyền thống, WSDL đóng vai trò đặc tả hợp đồng (contract / 계약) mô tả dịch vụ (service / 서비스) để máy khách (client / 클라이언트)/máy chủ (server / 서버) tooling biết dịch vụ (service / 서비스) cung cấp operations nào, message shape ra sao, binding/giao thức (protocol / 프로토콜) nào được dùng và endpoint ở đâu.

Bạn có thể hình dung WSDL 1.1 theo mô hình tư duy (mental model / 사고 모델):

```text
XML Schema / types
→ messages
→ operations / portType
→ binding
→ service / endpoint
```

Trong thực tế WSDL thường import hoặc embed XSD. XSD định nghĩa nghiệp vụ (business / 비즈니스) elements/types; WSDL ghép chúng thành dịch vụ (service / 서비스) operations và vận chuyển (transport / 전송) binding.

Đây là lý do khi một SOAP máy khách (client / 클라이언트) generate Java classes từ WSDL, bạn có thể thấy rất nhiều generated DTOs, dịch vụ (service / 서비스) interfaces và QName constants. Tooling đang biến XML đặc tả hợp đồng (contract / 계약) thành programming-language artifacts.

---

## 83. Contract-first SOAP luồng (flow / 흐름)

Trong một hệ thống contract-first, nhóm (team / 팀) có thể thiết kế XSD/WSDL trước rồi generate máy khách (client / 클라이언트)/máy chủ (server / 서버) stubs.

Luồng (flow / 흐름) khái niệm như sau:

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

Khung phần mềm (framework / 프레임워크) che đi rất nhiều bước, nhưng khi môi trường vận hành (production / 운영 환경) lỗi bạn phải có khả năng mở wire message và kiểm tra không gian tên (namespace / 네임스페이스), QName, element thứ tự (order / 순서), `xsi:nil`, lược đồ (schema / 스키마) kiểu (type / 타입) và SOAP phiên bản (version / 버전).

Một exception Java kiểu “unexpected element” thường thực chất là mismatch giữa expanded name trong XML và generated binding expectation.

---

## 84. WSDL/XSD mã (code / 코드) generation giúp nhanh nhưng có coupling

Generated classes giúp nhà phát triển (developer / 개발자) không phải tự viết parser cho mỗi SOAP message. Tuy nhiên mã (code / 코드) generation cũng làm ứng dụng (application / 애플리케이션) coupling mạnh với đặc tả hợp đồng (contract / 계약). Khi WSDL thay không gian tên (namespace / 네임스페이스), kiểu (type / 타입) hierarchy hoặc required trường dữ liệu (field / 필드), generated mã (code / 코드) có thể thay đổi hàng loạt.

Vì vậy long-lived enterprise dịch vụ (service / 서비스) cần quản lý WSDL/XSD phiên bản (version / 버전) như API công khai (public API / 공개 API). Không sửa lược đồ (schema / 스키마) âm thầm rồi regenerate cả hai bên nếu còn bên ngoài (external / 외부) consumers.

Nếu generated classes quá phức tạp, nên map chúng sang nội bộ (internal / 내부) DTO/lĩnh vực (domain / 도메인) mô hình (model / 모델) ở ranh giới (boundary / 경계) thay vì để WSDL-generated types chạy xuyên nghiệp vụ (business / 비즈니스) tầng (layer / 계층).

---

## 85. SOAP, WS-* và vì sao enterprise các hệ thống (systems / 시스템들) vẫn dùng

SOAP thường xuất hiện trong banking, insurance, telecom, government, B2B tích hợp (integration / 통합) và các hệ thống được xây trong thời kỳ enterprise dịch vụ (service / 서비스) bus. Một lý do là ecosystem xung quanh SOAP có nhiều specifications cho concerns như bảo mật (security / 보안), addressing, độ tin cậy (reliability / 신뢰성) và transactions. Những hệ thống đã đầu tư vào WSDL/XSD quản trị (governance / 거버넌스), mã (code / 코드) generation và tích hợp (integration / 통합) middleware không có lý do kỹ thuật để rewrite chỉ vì JSON phổ biến hơn.

Điều này không có nghĩa SOAP nên là default cho mọi API mới. Với một công khai (public / 공개)/nội bộ (internal / 내부) CRUD API đơn giản, HTTP + JSON thường nhẹ và dễ vận hành hơn. Nhưng nếu bạn maintain cốt lõi (core / 핵심) banking hoặc B2B gateway, việc hiểu SOAP/WSDL/XSD là kỹ năng thực tế chứ không phải kiến thức lịch sử.

---

## 86. SOAP so với REST/JSON phải so ở đúng tầng

SOAP là messaging khung phần mềm (framework / 프레임워크)/giao thức (protocol / 프로토콜) family; REST là architectural style; JSON là dữ liệu (data / 데이터) serialization format. Vì vậy câu “SOAP hay JSON cái nào tốt hơn” đang so các khái niệm khác tầng.

Một SOAP dịch vụ (service / 서비스) thường dùng XML payload và WSDL đặc tả hợp đồng (contract / 계약). Một REST-like HTTP API thường dùng JSON, URLs, HTTP methods/status codes và OpenAPI. Nhưng về mặt kiến trúc (architecture / 아키텍처), lựa chọn còn phụ thuộc quản trị (governance / 거버넌스), legacy tính tương thích (compatibility / 호환성), bảo mật (security / 보안) requirements, tooling và partner contracts.

Cấp cao (senior / 시니어) không chọn công nghệ chỉ vì verbosity. Bạn phải đánh giá đặc tả hợp đồng (contract / 계약) vòng đời (lifecycle / 생명주기) và ecosystem của hệ thống.

---

## 87. Enterprise tích hợp (integration / 통합) luồng (flow / 흐름) nên cô lập XML ở ranh giới (boundary / 경계)

Nếu dịch vụ (service / 서비스) nhận SOAP từ bên ngoài (external / 외부) partner, một kiến trúc (architecture / 아키텍처) tốt thường là:

```text
SOAP transport
→ secure XML parser / SOAP framework
→ schema validation
→ generated/bound request object
→ adapter / anti-corruption layer
→ internal domain command
→ business logic
```

Phản hồi (response / 응답) đi ngược lại qua mapper và SOAP tầng (layer / 계층).

Điểm quan trọng là nghiệp vụ (business / 비즈니스) lĩnh vực (domain / 도메인) không nên phụ thuộc trực tiếp vào SOAP-specific types nếu không có lý do. Nếu ngày mai partner đổi SOAP phiên bản (version / 버전) hoặc một channel mới dùng JSON, cốt lõi (core / 핵심) lĩnh vực (domain / 도메인) không cần rewrite.

---

## 88. gỡ lỗi (debug / 디버그) SOAP theo tầng (layer / 계층) thay vì nhìn một XML khổng lồ

Khi SOAP yêu cầu (request / 요청) thất bại (fail / 실패), hãy bắt đầu từ vận chuyển (transport / 전송): endpoint, HTTP headers/content kiểu (type / 타입), TLS và authentication có đúng không. Sau đó kiểm tra SOAP phiên bản (version / 버전) bằng envelope không gian tên (namespace / 네임스페이스). Tiếp theo kiểm tra `Envelope`, `Header`, `Body` và Fault cấu trúc (structure / 구조). Sau đó mới đi vào nghiệp vụ (business / 비즈니스) payload không gian tên (namespace / 네임스페이스) và XSD thứ tự (order / 순서)/kiểu (type / 타입). Cuối cùng kiểm tra binding mã (code / 코드) hoặc generated classes.

Luồng (flow / 흐름) gỡ lỗi (debug / 디버그) này giúp tránh việc sửa ngẫu nhiên prefix. Trong XML, prefix có thể khác nhưng không gian tên (namespace / 네임스페이스) URI mới quyết định định danh (identity / 식별자). Một dịch vụ (service / 서비스) kỳ vọng `{urn:bank:v1}Transfer` sẽ không chấp nhận `{urn:bank:v2}Transfer` chỉ vì cả hai đều viết prefix `pay`.

---

## 89. SOAP bảo mật (security / 보안) vẫn bắt đầu từ XML bảo mật (security / 보안)

Dù SOAP khung phần mềm (framework / 프레임워크) xử lý envelope, XML parser và bên ngoài (external / 외부) resolution vẫn là phần threat surface. Ngoài ra SOAP các hệ thống (systems / 시스템들) còn có thể dùng message-level bảo mật (security / 보안) standards như WS-Security/XML Signature. Khi đó namespace-aware signature xác minh (verification / 확인), canonicalization và verified-node binding từ các phần trước trở nên đặc biệt quan trọng.

Không nên tự parse SOAP bằng string hoặc tự implement XML Signature. Hãy dùng khung phần mềm (framework / 프레임워크)/thư viện (library / 라이브러리) đã được rà soát (review / 검토), cấu hình parser/tài nguyên (resource / 자원) resolution chặt, rồi giữ lô-gic nghiệp vụ (business logic / 비즈니스 로직) tách khỏi raw XML.

---

## 90. mô hình tư duy (mental model / 사고 모델) enterprise cuối cùng

Khi gặp một hệ thống XML enterprise, hãy nhìn nó như một chuỗi contracts và processors:

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

Nếu có SOAP, SOAP envelope nằm giữa XML tầng (layer / 계층) và ứng dụng (application / 애플리케이션) payload. Nếu có XSLT, transformation nằm ở ranh giới (boundary / 경계) hoặc tích hợp (integration / 통합) chuỗi xử lý (pipeline / 파이프라인). Nếu có XML Signature, canonicalization/tham chiếu (reference / 참조) xác minh (verification / 확인) phải xảy ra theo giao thức (protocol / 프로토콜) trước khi nghiệp vụ (business / 비즈니스) mã (code / 코드) tin dữ liệu.

Đây là điểm mà toàn bộ kiến thức XML từ Beginner tới cấp cao (senior / 시니어) kết nối lại thành một hệ thống duy nhất.

> **Bàn giao:** Sau **90. mô hình tư duy (mental model / 사고 모델) enterprise cuối cùng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [xml 01 beginner detailed](./xml_01_beginner_detailed.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
