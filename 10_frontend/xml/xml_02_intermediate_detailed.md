# XML — Intermediate

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **XML — Intermediate**. Route đi từ namespaces/name collisions → DTD/XSD validation → XPath queries → DOM/SAX/StAX parser models → lựa chọn parser theo document size and trust boundary.

## Không gian tên (namespace / 네임스페이스), DTD, XML lược đồ (schema / 스키마), XPath và các mô hình Parser

Tài liệu này tiếp nối phần Beginner. Ở phần trước, bạn đã biết XML là một cây dữ liệu strict, biết element, attribute, văn bản (text / 텍스트), encoding, CDATA và khái niệm well-formed. Tuy nhiên chỉ biết cú pháp XML chưa đủ để dùng XML trong hệ thống thật. Khi nhiều vocabulary được trộn với nhau, bạn cần không gian tên (namespace / 네임스페이스). Khi muốn kiểm tra XML có đúng cấu trúc hay không, bạn cần DTD hoặc XML lược đồ (schema / 스키마). Khi muốn tìm dữ liệu trong cây, bạn cần XPath. Khi document nhỏ hoặc rất lớn, bạn phải chọn DOM, SAX hoặc StAX phù hợp.

Phần Intermediate được viết theo đúng luồng (flow / 흐름) đó để bạn hiểu vì sao từng lớp tồn tại.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **Không gian tên (namespace / 네임스페이스), DTD, XML lược đồ (schema / 스키마), XPath và các mô hình Parser** xác định đầu vào; **1. Vấn đề name collision và lý do XML không gian tên (namespace / 네임스페이스) xuất hiện** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **2. Prefix chỉ là alias, không phải định danh (identity / 식별자) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. Vấn đề name collision và lý do XML không gian tên (namespace / 네임스페이스) xuất hiện

Giả sử hệ thống của bạn cần kết hợp dữ liệu từ hai lĩnh vực (domain / 도메인). Một lĩnh vực (domain / 도메인) nói về HTML-like document và một lĩnh vực (domain / 도메인) nói về furniture inventory. Cả hai đều dùng element tên `table`:

```xml
<document>
  <table>...</table>
  <table>...</table>
</document>
```

Nhìn vào XML này, ứng dụng (application / 애플리케이션) không biết `table` đầu tiên và `table` thứ hai thuộc vocabulary nào.

XML không gian tên (namespace / 네임스페이스) giải quyết vấn đề bằng cách làm cho tên lô-gic (logic / 논리) của element không còn chỉ là cục bộ (local / 로컬) name `table`. định danh (identity / 식별자) thật được xem như cặp:

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

Bây giờ hai element có cục bộ (local / 로컬) name giống nhau nhưng không gian tên (namespace / 네임스페이스) khác nhau, vì vậy ứng dụng (application / 애플리케이션) phân biệt được hoàn toàn.

---

> **Chuyển mạch:** Namespace giải quyết collision bằng expanded name; prefix chỉ là alias trong serialization. Phần expanded name tiếp theo cố định identity để parser và application cùng hiểu một element.

## 2. Prefix chỉ là alias, không phải định danh (identity / 식별자) thật

Đây là một trong những kiến thức quan trọng nhất của XML.

Hai tài liệu:

```xml
<a:user xmlns:a="https://example.com/user"/>
```

và:

```xml
<u:user xmlns:u="https://example.com/user"/>
```

có prefix khác nhau, nhưng cùng không gian tên (namespace / 네임스페이스) URI và cục bộ (local / 로컬) name. Về namespace-aware định danh (identity / 식별자), cả hai là cùng một expanded name:

```text
{https://example.com/user}user
```

Điều này có nghĩa khi mã (code / 코드) Java, XPath, XSLT hoặc lược đồ (schema / 스키마) xử lý XML, bạn không nên so sánh string prefix `a` hoặc `u` để xác định nghiệp vụ (business / 비즈니스) meaning. Prefix có thể đổi tự do miễn nó vẫn bind tới cùng không gian tên (namespace / 네임스페이스) URI.

Một XML serializer thậm chí có thể đọc đầu vào (input / 입력) prefix `a` rồi serialize đầu ra (output / 출력) thành `ns1` mà ngữ nghĩa (semantics / 의미론) vẫn không đổi.

---

> **Chuyển mạch:** Prefix chỉ là lexical alias; expanded name mới là `{namespace URI, local name}`, và default namespace tiếp theo áp dụng theo element context.

## 3. Expanded name

Expanded name là mô hình tư duy (mental model / 사고 모델) bạn nên dùng mọi lúc khi gặp không gian tên (namespace / 네임스페이스).

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

Khi bảo mật (security / 보안) hoặc lô-gic nghiệp vụ (business logic / 비즈니스 로직) match element, cách đúng về tư duy là match không gian tên (namespace / 네임스페이스) URI và cục bộ (local / 로컬) name, không match raw tag string.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **4. Default không gian tên (namespace / 네임스페이스)** tiếp nhận điểm tựa từ **3. Expanded name** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Default không gian tên (namespace / 네임스페이스) không áp dụng cho unprefixed attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Default không gian tên (namespace / 네임스페이스)

Nếu không muốn viết prefix lặp lại, XML cho phép default không gian tên (namespace / 네임스페이스):

```xml
<catalog xmlns="https://example.com/catalog">
  <book>
    <title>XML</title>
  </book>
</catalog>
```

Trong subtree này, các unprefixed elements `catalog`, `book`, `title` thuộc không gian tên (namespace / 네임스페이스) `https://example.com/catalog`.

Điều này làm XML dễ đọc hơn, nhưng cũng gây một trong những bug XPath phổ biến nhất: nhà phát triển (developer / 개발자) thấy nguồn (source / 소스) không có prefix nên tưởng element “không không gian tên (namespace / 네임스페이스)”. Thực tế chúng đang nằm trong default không gian tên (namespace / 네임스페이스).

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **5. Default không gian tên (namespace / 네임스페이스) không áp dụng cho unprefixed attributes** tiếp nhận điểm tựa từ **4. Default không gian tên (namespace / 네임스페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. không gian tên (namespace / 네임스페이스) phạm vi (scope / 범위) và redeclaration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Default không gian tên (namespace / 네임스페이스) không áp dụng cho unprefixed attributes

Đây là quy tắc (rule / 규칙) phải thuộc lòng.

Xét:

```xml
<book
  xmlns="https://example.com/catalog"
  id="B001"/>
```

Element `book` thuộc không gian tên (namespace / 네임스페이스):

```text
https://example.com/catalog
```

Nhưng attribute `id` không có không gian tên (namespace / 네임스페이스).

Nếu bạn muốn namespaced attribute, phải viết prefix rõ:

```xml
<book
  xmlns="https://example.com/catalog"
  xmlns:app="https://example.com/app"
  app:id="B001"/>
```

Bây giờ `app:id` thuộc không gian tên (namespace / 네임스페이스) `https://example.com/app`.

Điểm này rất quan trọng với XPath, DOM, XML Signature và binding frameworks.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **6. không gian tên (namespace / 네임스페이스) phạm vi (scope / 범위) và redeclaration** tiếp nhận điểm tựa từ **5. Default không gian tên (namespace / 네임스페이스) không áp dụng cho unprefixed attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. không gian tên (namespace / 네임스페이스) URI có bắt buộc phải mở được như URL không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. không gian tên (namespace / 네임스페이스) phạm vi (scope / 범위) và redeclaration

Không gian tên (namespace / 네임스페이스) prefix binding có phạm vi (scope / 범위).

```xml
<root xmlns:p="urn:a">
  <p:item/>

  <section xmlns:p="urn:b">
    <p:item/>
  </section>
</root>
```

`p:item` đầu tiên thuộc `urn:a`, còn `p:item` bên trong `section` thuộc `urn:b`.

Vì vậy không được scan một tệp (file / 파일) rồi kết luận “prefix `p` luôn nghĩa urn:a”. Binding phải được resolve theo ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **7. không gian tên (namespace / 네임스페이스) URI có bắt buộc phải mở được như URL không?** tiếp nhận điểm tựa từ **6. không gian tên (namespace / 네임스페이스) phạm vi (scope / 범위) và redeclaration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Prefix xml** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. không gian tên (namespace / 네임스페이스) URI có bắt buộc phải mở được như URL không?

Không. không gian tên (namespace / 네임스페이스) URI là identifier. Nó có thể nhìn giống URL:

```text
https://example.com/order
```

hoặc là URN:

```text
urn:example:order
```

Processor không bắt buộc phải download lược đồ (schema / 스키마) từ không gian tên (namespace / 네임스페이스) URI.

Một sai lầm phổ biến là nghĩ rằng `xmlns="https://example.com/order"` nghĩa trình duyệt (browser / 브라우저) hoặc parser sẽ truy cập URL này. Không phải. lược đồ (schema / 스키마) location và không gian tên (namespace / 네임스페이스) định danh (identity / 식별자) là hai khái niệm khác nhau.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **8. Prefix xml** tiếp nhận điểm tựa từ **7. không gian tên (namespace / 네임스페이스) URI có bắt buộc phải mở được như URL không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Tại sao chỉ well-formed vẫn chưa đủ?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Prefix `xml`

Prefix `xml` được dành sẵn cho XML không gian tên (namespace / 네임스페이스) chuẩn và dùng trong:

```xml
xml:lang
xml:space
xml:base
xml:id
```

Bạn không được tự redefine `xml` sang không gian tên (namespace / 네임스페이스) của mình.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **9. Tại sao chỉ well-formed vẫn chưa đủ?** tiếp nhận điểm tựa từ **8. Prefix xml** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. DTD là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Tại sao chỉ well-formed vẫn chưa đủ?

XML cốt lõi (core / 핵심) chỉ kiểm tra cú pháp. Ví dụ:

```xml
<order>
  <banana>Hello</banana>
  <total>abc</total>
</order>
```

có thể hoàn toàn well-formed.

Nhưng ứng dụng (application / 애플리케이션) có thể yêu cầu `order` phải có `id`, `customer`, `total`, và `total` phải là decimal. Để diễn tả grammar hoặc đặc tả hợp đồng (contract / 계약) đó, XML ecosystem dùng các lược đồ (schema / 스키마) languages. Hai công nghệ bạn cần hiểu trước tiên là DTD và XSD.

---

# DTD

> **Chuyển mạch:** Trong **XML — Intermediate**, **10. DTD là gì?** tiếp nhận điểm tựa từ **9. Tại sao chỉ well-formed vẫn chưa đủ?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. nội bộ (internal / 내부) DTD và bên ngoài (external / 외부) DTD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. DTD là gì?

DTD là **Document kiểu (type / 타입) Definition**. Đây là cơ chế lược đồ (schema / 스키마) cổ điển đi cùng XML từ rất sớm.

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

Điểm đáng chú ý là cú pháp (syntax / 문법) DTD không phải XML cú pháp (syntax / 문법) thông thường. Đây là một lý do XSD sau này được thiết kế với cú pháp (syntax / 문법) XML.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **11. nội bộ (internal / 내부) DTD và bên ngoài (external / 외부) DTD** tiếp nhận điểm tựa từ **10. DTD là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. ELEMENT declaration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. nội bộ (internal / 내부) DTD và bên ngoài (external / 외부) DTD

DTD có thể nằm trong chính document:

```xml
<!DOCTYPE note [
  <!ELEMENT note (#PCDATA)>
]>
```

hoặc tham chiếu (reference / 참조) bên ngoài (external / 외부) tệp (file / 파일):

```xml
<!DOCTYPE note SYSTEM "note.dtd">
```

Bên ngoài (external / 외부) DTD rất quan trọng về bảo mật (security / 보안). Nếu parser được phép tự fetch URI hoặc tệp (file / 파일) từ DTD của untrusted đầu vào (input / 입력), attacker có thể lợi dụng bên ngoài (external / 외부) thực thể (entity / 엔터티) hoặc bên ngoài (external / 외부) subset để đọc tệp (file / 파일), SSRF hoặc gây denial of dịch vụ (service / 서비스). Phần cấp cao (senior / 시니어) sẽ đi sâu vào XXE.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **12. ELEMENT declaration** tiếp nhận điểm tựa từ **11. nội bộ (internal / 내부) DTD và bên ngoài (external / 외부) DTD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Cardinality trong DTD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. `ELEMENT` declaration

DTD có thể định nghĩa child chuỗi (sequence / 시퀀스):

```dtd
<!ELEMENT user (name,email)>
```

Điều này có nghĩa `user` cần `name` rồi đến `email`.

Nếu thứ tự (order / 순서) đảo lại, document có thể invalid theo DTD dù vẫn well-formed.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **13. Cardinality trong DTD** tiếp nhận điểm tựa từ **12. ELEMENT declaration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Choice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **14. Choice** tiếp nhận điểm tựa từ **13. Cardinality trong DTD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. #PCDATA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Choice
Phần này nối mạch bài học với “14. Choice”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```dtd
<!ELEMENT contact (email|phone)>
```

nghĩa là contact chứa một trong hai branch.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **15. #PCDATA** tiếp nhận điểm tựa từ **14. Choice** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. ATTLIST** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. `#PCDATA`
Phần này nối mạch bài học với “15. `#PCDATA`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```dtd
<!ELEMENT name (#PCDATA)>
```

`#PCDATA` nghĩa là parsed character dữ liệu (data / 데이터).

DTD cũng hỗ trợ mixed content, ví dụ:

```dtd
<!ELEMENT p (#PCDATA|em|strong)*>
```

cho phép văn bản (text / 텍스트) xen `em` và `strong`.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **16. ATTLIST** tiếp nhận điểm tựa từ **15. #PCDATA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Entities trong DTD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. `ATTLIST`

DTD có thể định nghĩa attributes:

```dtd
<!ATTLIST user
  id ID #REQUIRED
  active (true|false) "true">
```

Ở đây `id` là attribute có kiểu (type / 타입) `ID` và bắt buộc. `active` chỉ nhận `true` hoặc `false`, mặc định là `true`.

Các từ khóa thường gặp gồm `#REQUIRED`, `#IMPLIED` và `#FIXED`.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **17. Entities trong DTD** tiếp nhận điểm tựa từ **16. ATTLIST** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Entities trong DTD

Bạn có thể define thực thể (entity / 엔터티):

```dtd
<!ENTITY company "Acme Corporation">
```

sau đó dùng:

```xml
<name>&company;</name>
```

Parser có thể expand `&company;` thành văn bản (text / 텍스트).

Thực thể (entity / 엔터티) hệ thống (system / 시스템) rất mạnh nhưng cũng là lý do DTD trở thành attack surface. bên ngoài (external / 외부) entities, parameter entities và thực thể (entity / 엔터티) expansion đều cần được điều khiển (control / 제어) trong môi trường vận hành (production / 운영 환경).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?** tiếp nhận điểm tựa từ **17. Entities trong DTD** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. XSD là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?

DTD có khả năng mô tả cấu trúc (structure / 구조) nhưng hệ kiểu (type system / 타입 시스템) hạn chế, không gian tên (namespace / 네임스페이스) tích hợp (integration / 통합) không tự nhiên và cú pháp (syntax / 문법) riêng. Khi cần decimal, dateTime, typed attributes, reusable complex kiểu (type / 타입) hoặc advanced các ràng buộc (constraints / 제약조건들), XSD thường phù hợp hơn.

DTD vẫn tồn tại trong nhiều publishing/document các hệ thống (systems / 시스템들) và legacy standards, nên cấp cao (senior / 시니어) phải đọc được, nhưng với đặc tả ứng dụng (application contract / 애플리케이션 계약) mới, XSD phổ biến hơn.

---

# XML lược đồ (schema / 스키마) / XSD

> **Chuyển mạch:** Trong **XML — Intermediate**, **19. XSD là gì?** tiếp nhận điểm tựa từ **18. Vì sao DTD không đủ cho nhiều hệ thống enterprise?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Built-in dữ liệu (data / 데이터) types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. XSD là gì?

XSD là XML lược đồ (schema / 스키마) Definition. Khác DTD, XSD được viết bằng XML.

Ví dụ:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xs:element
    name="age"
    type="xs:integer"/>

</xs:schema>
```

Không gian tên (namespace / 네임스페이스) `http://www.w3.org/2001/XMLSchema` là vocabulary của XML lược đồ (schema / 스키마).

XSD không chỉ nói element nào được nằm ở đâu. Nó còn có hệ thống dữ liệu (data / 데이터) types, reusable types, restrictions, không gian tên (namespace / 네임스페이스) tích hợp (integration / 통합) và định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들).

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **19. XSD là gì?** nêu điều cần giải thích; **20. Built-in dữ liệu (data / 데이터) types** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **21. Simple kiểu (type / 타입) và complex kiểu (type / 타입)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Built-in dữ liệu (data / 데이터) types

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

Bây giờ `price` không còn chỉ là arbitrary văn bản (text / 텍스트) về mặt lược đồ (schema / 스키마). lược đồ (schema / 스키마) validator có thể kiểm tra lexical giá trị (value / 값) có hợp `xs:decimal` hay không.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **20. Built-in dữ liệu (data / 데이터) types** nêu điều cần giải thích; **21. Simple kiểu (type / 타입) và complex kiểu (type / 타입)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **22. xs:sequence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Simple kiểu (type / 타입) và complex kiểu (type / 타입)

Một simple element có thể khai báo trực tiếp:

```xml
<xs:element
  name="name"
  type="xs:string"/>
```

Complex kiểu (type / 타입) dùng khi element có children hoặc attributes:

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

`user` không chỉ là một scalar giá trị (value / 값); nó là một cấu trúc (structure / 구조).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **22. xs:sequence** tiếp nhận điểm tựa từ **21. Simple kiểu (type / 타입) và complex kiểu (type / 타입)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. xs:choice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

hợp thứ tự (order / 순서).

Nếu đổi `email` trước `name`, có thể invalid.

Đây là điều cần nhớ khi phiên bản (version / 버전) XML đặc tả hợp đồng (contract / 계약): nếu lược đồ (schema / 스키마) dùng strict chuỗi (sequence / 시퀀스), chèn element mới vào sai vị trí có thể làm bên tiêu thụ (consumer / 소비자) cũ thất bại (fail / 실패).

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **23. xs:choice** tiếp nhận điểm tựa từ **22. xs:sequence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. xs:all** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `xs:choice`
Phần này nối mạch bài học với “23. `xs:choice`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xml
<xs:choice>
  <xs:element name="email"/>
  <xs:element name="phone"/>
</xs:choice>
```

Nghĩa là chọn một branch.

Choice rất hữu ích cho union-like structures nhưng nếu nested choice quá sâu, lược đồ (schema / 스키마) sẽ khó đọc và binding mã (code / 코드) cũng phức tạp.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **24. xs:all** tiếp nhận điểm tựa từ **23. xs:choice** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. minOccurs và maxOccurs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `xs:all`

`xs:all` được dùng khi một nhóm elements có thể xuất hiện với thứ tự (order / 순서) linh hoạt hơn `sequence`, trong các ràng buộc (constraints / 제약조건들) mà XSD phiên bản (version / 버전) quy định.

Điểm quan trọng là đừng nghĩ `xs:all` nghĩa “bất kỳ thứ gì, bao nhiêu lần cũng được”. Nó vẫn có quy tắc (rule / 규칙) về children và occurrence. Nếu cần repeating arbitrary structures, bạn phải đọc đúng XSD mô hình (model / 모델) thay vì suy từ tên `all`.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **25. minOccurs và maxOccurs** tiếp nhận điểm tựa từ **24. xs:all** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. XSD attribute declaration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. `minOccurs` và `maxOccurs`
Phần này nối mạch bài học với “25. `minOccurs` và `maxOccurs`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

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

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **26. XSD attribute declaration** tiếp nhận điểm tựa từ **25. minOccurs và maxOccurs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Restriction và facets** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. XSD attribute declaration
Phần này nối mạch bài học với “26. XSD attribute declaration”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xml
<xs:attribute
  name="id"
  type="xs:string"
  use="required"/>
```

`use="required"` bắt buộc attribute tồn tại.

Các cases khác có thể là optional hoặc prohibited tùy ngữ cảnh (context / 맥락).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **27. Restriction và facets** tiếp nhận điểm tựa từ **26. XSD attribute declaration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Enumeration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Restriction và facets

Bạn có thể tạo kiểu (type / 타입) mới dựa trên kiểu (type / 타입) có sẵn:

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

Facets là cách XSD biến generic kiểu (type / 타입) thành domain-specific giá trị (value / 값) không gian (space / 공간).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **28. Enumeration** tiếp nhận điểm tựa từ **27. Restriction và facets** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Pattern** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Enumeration
Phần này nối mạch bài học với “28. Enumeration”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xml
<xs:simpleType name="Status">
  <xs:restriction base="xs:string">
    <xs:enumeration value="NEW"/>
    <xs:enumeration value="PAID"/>
    <xs:enumeration value="CANCELLED"/>
  </xs:restriction>
</xs:simpleType>
```

Lược đồ (schema / 스키마) validator sẽ reject giá trị (value / 값) ngoài tập này.

Nhưng hãy nhớ rằng thêm hoặc xóa enum giá trị (value / 값) có thể là breaking đặc tả hợp đồng (contract / 계약) đối với generated clients.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **29. Pattern** tiếp nhận điểm tựa từ **28. Enumeration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Named kiểu (type / 타입) và anonymous kiểu (type / 타입)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Pattern
Phần này nối mạch bài học với “29. Pattern”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xml
<xs:pattern value="[A-Z]{2}[0-9]{4}"/>
```

Mẫu (pattern / 패턴) trong XML lược đồ (schema / 스키마) dùng regex dialect riêng. Bạn không nên bản sao (copy / 복사) Java regex hoặc JavaScript regex rồi assume chúng tương đương hoàn toàn.

Nếu mẫu (pattern / 패턴) là business-critical, đọc rules của XSD regex và kiểm thử (test / 테스트) bằng đúng lược đồ (schema / 스키마) processor.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **30. Named kiểu (type / 타입) và anonymous kiểu (type / 타입)** tiếp nhận điểm tựa từ **29. Pattern** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. targetNamespace** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Named kiểu (type / 타입) và anonymous kiểu (type / 타입)

Named kiểu (type / 타입):

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

Anonymous kiểu (type / 타입):

```xml
<xs:element name="user">
  <xs:complexType>
    ...
  </xs:complexType>
</xs:element>
```

Named kiểu (type / 타입) hợp khi cấu trúc (structure / 구조) được reuse hoặc phiên bản (version / 버전) độc lập. Anonymous kiểu (type / 타입) hợp với one-off cục bộ (local / 로컬) cấu trúc (structure / 구조).

Việc chọn kiểu nào là một phần của lược đồ (schema / 스키마) mẫu thiết kế (design pattern / 디자인 패턴), phần Master sẽ nói sâu hơn.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **31. targetNamespace** tiếp nhận điểm tựa từ **30. Named kiểu (type / 타입) và anonymous kiểu (type / 타입)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. elementFormDefault** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. `targetNamespace`

Một lược đồ (schema / 스키마) thường định nghĩa vocabulary trong một không gian tên (namespace / 네임스페이스) cụ thể:

```xml
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  targetNamespace="https://example.com/order"
  xmlns:o="https://example.com/order">
```

`targetNamespace` trả lời câu hỏi: “Các toàn cục (global / 전역) lược đồ (schema / 스키마) components này thuộc vocabulary không gian tên (namespace / 네임스페이스) nào?”

Nếu hiểu sai `targetNamespace`, bạn sẽ gặp lỗi kiểu lược đồ (schema / 스키마) nói `order` tồn tại nhưng validator báo “cannot find declaration” vì instance element không ở không gian tên (namespace / 네임스페이스) đúng.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **32. elementFormDefault** tiếp nhận điểm tựa từ **31. targetNamespace** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. xs:include và xs:import** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. `elementFormDefault`

Một lược đồ (schema / 스키마) có thể khai báo:

```xml
elementFormDefault="qualified"
```

Điều này ảnh hưởng cục bộ (local / 로컬) elements có cần không gian tên (namespace / 네임스페이스) qualification hay không.

Đây là một trong những điểm gây lỗi nhiều nhất khi làm SOAP/XSD Java binding. Một instance nhìn gần giống nhau nhưng khác không gian tên (namespace / 네임스페이스) qualification có thể invalid hoàn toàn.

Khi gỡ lỗi (debug / 디버그), luôn xem cùng lúc:

```text
targetNamespace
elementFormDefault
namespace declarations của instance
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **33. xs:include và xs:import** tiếp nhận điểm tựa từ **32. elementFormDefault** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. xsi:schemaLocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. `xs:include` và `xs:import`

`xs:include` thường dùng để compose lược đồ (schema / 스키마) components trong cùng không gian tên (namespace / 네임스페이스) family/ngữ cảnh (context / 맥락):

```xml
<xs:include schemaLocation="common.xsd"/>
```

`xs:import` dùng để đưa lược đồ (schema / 스키마) components thuộc không gian tên (namespace / 네임스페이스) khác vào:

```xml
<xs:import
  namespace="https://example.com/common"
  schemaLocation="common.xsd"/>
```

Một quy tắc (rule / 규칙) mô hình tư duy (mental model / 사고 모델) dễ nhớ là:

```text
same namespace → include
different namespace → import
```

Dù thực tế XSD có thêm details, mô hình tư duy (mental model / 사고 모델) này đủ tốt để bắt đầu.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **34. xsi:schemaLocation** tiếp nhận điểm tựa từ **33. xs:include và xs:import** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. xsi:noNamespaceSchemaLocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. `xsi:schemaLocation`

XML instance có thể chứa lược đồ (schema / 스키마) location hints:

```xml
<order
  xmlns="https://example.com/order"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="
    https://example.com/order
    order.xsd">
```

Đây là hint ánh xạ (mapping / 매핑) không gian tên (namespace / 네임스페이스) tới lược đồ (schema / 스키마) location.

Điều quan trọng về bảo mật (security / 보안) là ứng dụng (application / 애플리케이션) không nên mặc định tin và fetch arbitrary lược đồ (schema / 스키마) URL từ untrusted document. Resolver và lược đồ (schema / 스키마) nguồn (source / 소스) nên do ứng dụng (application / 애플리케이션) kiểm soát.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **35. xsi:noNamespaceSchemaLocation** tiếp nhận điểm tựa từ **34. xsi:schemaLocation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. xsi:nil** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. `xsi:noNamespaceSchemaLocation`

Nếu vocabulary không có không gian tên (namespace / 네임스페이스), instance có thể dùng:

```xml
xsi:noNamespaceSchemaLocation="note.xsd"
```

Nó vẫn là lược đồ (schema / 스키마) location hint, không biến untrusted URL thành trusted phụ thuộc (dependency / 의존성).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **36. xsi:nil** tiếp nhận điểm tựa từ **35. xsi:noNamespaceSchemaLocation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. XPath là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. `xsi:nil`

Ví dụ:

```xml
<middleName
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:nil="true"/>
```

Nếu lược đồ (schema / 스키마) declaration cho phép `nillable`, element có thể biểu diễn nil.

Bạn phải phân biệt ba trạng thái:

```xml
<middleName xsi:nil="true"/>
```

```xml
<middleName></middleName>
```

và element hoàn toàn không xuất hiện.

Nil, empty và missing có thể có nghiệp vụ (business / 비즈니스) meaning khác nhau. Đây là lý do đối tượng (object / 객체) ánh xạ (mapping / 매핑) XML sang Java `null` đôi khi làm mất thông tin nếu ánh xạ (mapping / 매핑) không cẩn thận.

---

# XPath

> **Chuyển mạch:** Trong **XML — Intermediate**, **36. xsi:nil** xác định đầu vào; **37. XPath là gì?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **38. Absolute path** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. XPath là gì?

XPath là ngôn ngữ expression/truy vấn (query / 쿼리) dùng để chọn hoặc tính toán dựa trên XML/XDM.

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

Bạn nên hình dung XPath như “đường đi + điều kiện” trên cây (tree / 트리), nhưng hiện đại (modern / 현대적) XPath còn mạnh hơn nhiều và có hệ kiểu (type system / 타입 시스템), functions, sequences.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **37. XPath là gì?** xác định đầu vào; **38. Absolute path** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **39. //** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Absolute path
Phần này nối mạch bài học với “38. Absolute path”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/book
```

đi từ document/gốc (root / 루트) ngữ cảnh (context / 맥락) tới `library`, sau đó child `book`.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **38. Absolute path** xác định đầu vào; **39. //** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **40. Attribute selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. `//`
Phần này nối mạch bài học với “39. `//`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
//book
```

là shorthand liên quan descendant-or-self traversal.

Nó rất tiện nhưng dễ bị lạm dụng. Trên XML lớn, truy vấn (query / 쿼리) quá rộng khó reason và có thể tốn tài nguyên. Nếu biết đường dẫn (path / 경로) rõ, đường dẫn (path / 경로) tường minh (explicit / 명시적) thường tốt hơn.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **40. Attribute selection** tiếp nhận điểm tựa từ **39. //** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Predicate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Attribute selection
Phần này nối mạch bài học với “40. Attribute selection”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/book/@id
```

chọn `id` attributes.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **41. Predicate** tiếp nhận điểm tựa từ **40. Attribute selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Position** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Predicate
Phần này nối mạch bài học với “41. Predicate”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/book[@id='2']
```

chọn book có attribute id bằng `2`.

Predicate có thể dùng expression phức tạp hơn, không chỉ attribute equality.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **42. Position** tiếp nhận điểm tựa từ **41. Predicate** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. text()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Position
Phần này nối mạch bài học với “42. Position”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/book[1]
```

chọn first book trong ngữ cảnh (context / 맥락) phù hợp.

```xpath
/library/book[last()]
```

chọn last book.

Khi dùng position với `//` hoặc grouped expressions, ngữ cảnh (context / 맥락) có thể khác điều bạn nghĩ. Đây là lý do cấp cao (senior / 시니어) XPath cần hiểu expression evaluation thay vì chỉ ghi nhớ cú pháp (syntax / 문법).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **43. text()** tiếp nhận điểm tựa từ **42. Position** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Wildcard** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. `text()`
Phần này nối mạch bài học với “43. `text()`”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/book/title/text()
```

chọn direct văn bản (text / 텍스트) nodes của `title`.

Trong mixed content:

```xml
<p>Hello <b>world</b>!</p>
```

`p/text()` chỉ chọn direct văn bản (text / 텍스트) nodes `"Hello "` và `"!"`, không tự trả văn bản (text / 텍스트) trong `<b>`.

String-value của `p` có thể là `"Hello world!"` theo XPath mô hình dữ liệu (data model / 데이터 모델).

Đây là khác biệt rất quan trọng.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **44. Wildcard** tiếp nhận điểm tựa từ **43. text()** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Các XPath functions thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Wildcard
Phần này nối mạch bài học với “44. Wildcard”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xpath
/library/*
```

chọn element children.

```xpath
//@*
```

có thể chọn rất rộng các attributes.

Wildcard useful nhưng làm truy vấn (query / 쿼리) ít tường minh (explicit / 명시적) hơn, nên chỉ dùng khi vocabulary thực sự cần generic handling.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **44. Wildcard** xác định đầu vào; **45. Các XPath functions thường gặp** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **46. Default không gian tên (namespace / 네임스페이스) và bug XPath nổi tiếng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Chính xác (exact / 정확한) set phụ thuộc XPath phiên bản (version / 버전). Phần cấp cao (senior / 시니어)/Master sẽ chuyển từ XPath 1.0 mô hình tư duy (mental model / 사고 모델) sang XPath 3.x/XDM.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **45. Các XPath functions thường gặp** xác định đầu vào; **46. Default không gian tên (namespace / 네임스페이스) và bug XPath nổi tiếng** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **47. Vì sao phải có nhiều loại parser?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Default không gian tên (namespace / 네임스페이스) và bug XPath nổi tiếng

Document:

```xml
<library xmlns="https://example.com/books">
  <book/>
</library>
```

Nhà phát triển (developer / 개발자) viết:

```xpath
/library/book
```

và không nhận được kết quả (result / 결과).

Lý do là `library` và `book` thuộc không gian tên (namespace / 네임스페이스) `https://example.com/books`. Trong nhiều XPath host APIs, unprefixed name trong expression không tự map tới default không gian tên (namespace / 네임스페이스) của nguồn (source / 소스) document.

Bạn cần bind một prefix của riêng mình:

```text
b → https://example.com/books
```

sau đó truy vấn (query / 쿼리):

```xpath
/b:library/b:book
```

Prefix `b` không cần xuất hiện trong nguồn (source / 소스) XML. Nó chỉ cần map tới đúng không gian tên (namespace / 네임스페이스) URI.

Đây là nguyên tắc quan trọng nhất khi gỡ lỗi (debug / 디버그) XPath không gian tên (namespace / 네임스페이스).

---

# Parser các mô hình (models / 모델들)

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **46. Default không gian tên (namespace / 네임스페이스) và bug XPath nổi tiếng** xác định đầu vào; **47. Vì sao phải có nhiều loại parser?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **48. DOM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Vì sao phải có nhiều loại parser?

Một tệp (file / 파일) XML 20 KB và một tệp (file / 파일) XML 10 GB có cùng cú pháp, nhưng cách xử lý tối ưu khác hoàn toàn.

Nếu tải (load / 로드) 10 GB thành DOM cây (tree / 트리), bộ nhớ (memory / 메모리) usage có thể lớn hơn raw tệp (file / 파일) nhiều lần. Vì vậy XML ecosystem có cả cây (tree / 트리) parser và streaming parser.

Ba mô hình bạn nên biết là DOM, SAX và StAX.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **48. DOM** tiếp nhận điểm tựa từ **47. Vì sao phải có nhiều loại parser?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. SAX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. DOM

DOM parser đọc toàn bộ document rồi tạo cây (tree / 트리) trong bộ nhớ (memory / 메모리).

Lợi ích là bạn có thể nhảy tới bất kỳ nút (node / 노드) nào, dùng XPath thuận tiện, mutate cây (tree / 트리) và serialize lại.

Ví dụ mô hình tư duy (mental model / 사고 모델) Java:

```java
Document doc = builder.parse(file);
```

sau đó:

```java
Element root = doc.getDocumentElement();
```

DOM rất dễ dùng với XML nhỏ và vừa.

Nhược điểm là bộ nhớ (memory / 메모리) chi phí (cost / 비용). Mỗi element không chỉ chiếm bytes của nguồn (source / 소스); còn có đối tượng (object / 객체) overhead, strings, pointers, không gian tên (namespace / 네임스페이스) siêu dữ liệu (metadata / 메타데이터) và child collections.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **49. SAX** tiếp nhận điểm tựa từ **48. DOM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. StAX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. SAX

SAX là event-driven push parser.

Thay vì đưa bạn cây (tree / 트리), parser gọi callbacks kiểu:

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

Ứng dụng (application / 애플리케이션) có thể nhận một chuỗi events tương ứng.

Ưu điểm của SAX là bộ nhớ (memory / 메모리) rất thấp vì parser không cần giữ toàn cây (tree / 트리). Nhược điểm là trạng thái (state / 상태) management khó hơn. Nếu muốn biết “đang ở trong người dùng (user / 사용자) nào, đã đọc trường dữ liệu (field / 필드) gì”, bạn phải tự giữ trạng thái (state / 상태).

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **50. StAX** tiếp nhận điểm tựa từ **49. SAX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. Chọn DOM, SAX hay StAX** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. StAX

StAX là streaming pull parser phổ biến trong Java ecosystem.

Khác SAX gọi ngược vào ứng dụng (application / 애플리케이션), StAX cho ứng dụng (application / 애플리케이션) chủ động yêu cầu sự kiện (event / 이벤트) tiếp theo.

Mô hình tư duy (mental model / 사고 모델):

```java
while (reader.hasNext()) {
    int event = reader.next();
}
```

Điều này thường khiến điều khiển (control / 제어) luồng (flow / 흐름) dễ reason hơn SAX, đặc biệt khi parse record-oriented XML lớn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **51. Chọn DOM, SAX hay StAX** tiếp nhận điểm tựa từ **50. StAX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Java DOM cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. Chọn DOM, SAX hay StAX

Nếu XML nhỏ hoặc vừa và bạn cần random truy cập (access / 접근), XPath hoặc mutation, DOM thường đơn giản nhất.

Nếu XML rất lớn và bạn chỉ cần đọc một lần từ đầu tới cuối, SAX hoặc StAX tốt hơn.

Trong Java nghiệp vụ (business / 비즈니스) ứng dụng (application / 애플리케이션), StAX thường là lựa chọn thuận tiện cho large XML vì pull mô hình (model / 모델) dễ viết máy trạng thái (state machine / 상태 머신).

Không nên chọn parser chỉ theo “cái nào nhanh nhất”. Hãy chọn theo truy cập (access / 접근) mẫu (pattern / 패턴) và bộ nhớ (memory / 메모리) yêu cầu (requirement / 요구사항).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **52. Java DOM cơ bản** tiếp nhận điểm tựa từ **51. Chọn DOM, SAX hay StAX** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **53. Java XPath cơ bản** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Tuy nhiên đoạn mã (code / 코드) này chưa phải secure parser cấu hình (configuration / 구성). bên ngoài (external / 외부) DTD/thực thể (entity / 엔터티) processing có thể cần disable hoặc điều khiển (control / 제어) tùy hiện thực (implementation / 구현). Phần cấp cao (senior / 시니어) sẽ giải thích vì sao.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **52. Java DOM cơ bản** xác định đầu vào; **53. Java XPath cơ bản** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **54. Serialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Java XPath cơ bản
Phần này nối mạch bài học với “53. Java XPath cơ bản”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```java
XPath xpath =
    XPathFactory.newInstance().newXPath();

String value =
    xpath.evaluate(
        "/library/book[1]/title",
        document
    );
```

Với namespaced XML, bạn cần `NamespaceContext` hoặc cơ chế tương đương để prefix trong XPath map tới không gian tên (namespace / 네임스페이스) URI.

Không hardcode prefix nguồn (source / 소스) làm nghiệp vụ (business / 비즈니스) định danh (identity / 식별자).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **53. Java XPath cơ bản** xác định đầu vào; **54. Serialization** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **55. Marshal và unmarshal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Serialization

Sau khi tạo hoặc sửa XML cây (tree / 트리), bạn có thể serialize nó thành bytes/văn bản (text / 텍스트).

Serialization phải xử lý đúng:

```text
encoding
escaping
namespace declarations
XML declaration
empty elements
text
```

Nếu đầu ra (output / 출력) có cryptographic yêu cầu (requirement / 요구사항), bạn còn phải phân biệt ordinary serialization với canonicalization.

Một XML serializer được thiết kế đúng tốt hơn nhiều so với nối string thủ công.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **55. Marshal và unmarshal** tiếp nhận điểm tựa từ **54. Serialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) nằm ở đâu trong luồng (flow / 흐름)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Marshal và unmarshal

Trong đối tượng (object / 객체) binding frameworks, bạn thường gặp hai từ:

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

có thể map thành Java đối tượng (object / 객체) `User`.

Nhưng mô hình đối tượng (object model / 객체 모델) thường đơn giản hơn XML mô hình (model / 모델). Mixed content, namespaces, nil-vs-missing, thứ tự (order / 순서), repeating elements và unknown extension đều có thể làm ánh xạ (mapping / 매핑) mất nuance.

Vì vậy cấp cao (senior / 시니어) không nên nghĩ “có JAXB thì không cần hiểu XML”.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **55. Marshal và unmarshal** xác định đầu vào; **56. lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) nằm ở đâu trong luồng (flow / 흐름)?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **57. Lỗi “lược đồ (schema / 스키마) không tìm thấy declaration”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) nằm ở đâu trong luồng (flow / 흐름)?

Một inbound XML luồng (flow / 흐름) đơn giản có thể là:

```text
bytes
→ secure parse
→ namespace-aware tree/stream
→ XSD validation
→ mapping
→ business validation
```

XSD kiểm tra structural/kiểu (type / 타입) rules. Nó không thay lô-gic nghiệp vụ (business logic / 비즈니스 로직).

Ví dụ lược đồ (schema / 스키마) có thể nói `amount` là decimal dương, nhưng không biết người dùng (user / 사용자) hiện tại có quyền transfer số tiền đó hay không. Authorization vẫn thuộc ứng dụng (application / 애플리케이션).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **56. lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) nằm ở đâu trong luồng (flow / 흐름)?** xác định đầu vào; **57. Lỗi “lược đồ (schema / 스키마) không tìm thấy declaration”** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **58. Anti-pattern: trust schemaLocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. Lỗi “lược đồ (schema / 스키마) không tìm thấy declaration”

Đây là lỗi rất phổ biến. Bạn có lược đồ (schema / 스키마) định nghĩa:

```text
{urn:order}order
```

nhưng đầu vào (input / 입력) thực tế là:

```xml
<order>
```

không không gian tên (namespace / 네임스페이스).

Dù cục bộ (local / 로컬) name đều là `order`, expanded name khác nhau.

Hoặc đầu vào (input / 입력) có default không gian tên (namespace / 네임스페이스) đúng nhưng XPath/lược đồ (schema / 스키마) cấu hình (config / 설정) không namespace-aware.

Khi gỡ lỗi (debug / 디버그), luôn kiểm tra:

```text
namespace URI
local name
targetNamespace
elementFormDefault
schema source
```

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **58. Anti-pattern: trust schemaLocation** tiếp nhận điểm tựa từ **57. Lỗi “lược đồ (schema / 스키마) không tìm thấy declaration”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. Anti-pattern: DOM cho tệp (file / 파일) khổng lồ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. Anti-pattern: trust `schemaLocation`

Nếu untrusted XML nói:

```xml
xsi:schemaLocation="
  urn:order
  http://internal-server/schema.xsd"
```

và parser/validator tự fetch URL đó, attacker có thể ảnh hưởng truy cập mạng (network access / 네트워크 접근).

Môi trường vận hành (production / 운영 환경) ứng dụng (application / 애플리케이션) nên chủ động chọn lược đồ (schema / 스키마) trusted, dùng cục bộ (local / 로컬) registry hoặc resolver. Instance hint không nên tự trở thành authority.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **59. Anti-pattern: DOM cho tệp (file / 파일) khổng lồ** tiếp nhận điểm tựa từ **58. Anti-pattern: trust schemaLocation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. Anti-pattern: XPath // ở mọi nơi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. Anti-pattern: DOM cho tệp (file / 파일) khổng lồ

Nếu đầu vào (input / 입력) 5 GB, DOM có thể consume bộ nhớ (memory / 메모리) nhiều lần 5 GB và gây OutOfMemoryError.

Khi dữ liệu (data / 데이터) có cấu trúc (structure / 구조) kiểu:

```xml
<records>
  <record>...</record>
  <record>...</record>
  ...
</records>
```

streaming parser là lựa chọn tự nhiên.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **59. Anti-pattern: DOM cho tệp (file / 파일) khổng lồ** xác định đầu vào; **60. Anti-pattern: XPath // ở mọi nơi** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **61. Bài tập tổng hợp Intermediate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. Anti-pattern: XPath `//` ở mọi nơi

Truy vấn (query / 쿼리):

```xpath
//price
```

có thể match price ở nhiều ngữ cảnh (context / 맥락) ngoài ý muốn.

Nếu vocabulary biết rõ:

```xpath
/order/items/item/price
```

thường an toàn và dễ rà soát (review / 검토) hơn.

Đặc biệt trong security-sensitive mã (code / 코드), truy vấn (query / 쿼리) broad có thể chọn wrong nút (node / 노드).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **61. Bài tập tổng hợp Intermediate** gom các mảnh từ **60. Anti-pattern: XPath // ở mọi nơi** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **62. mô hình tư duy (mental model / 사고 모델) sau Intermediate** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

`o:order` thuộc không gian tên (namespace / 네임스페이스) `urn:order`. Attribute `id` không có không gian tên (namespace / 네임스페이스) vì nó unprefixed. `c:customer` và `c:name` thuộc `urn:common`. `sku` cũng không có không gian tên (namespace / 네임스페이스). `o:item` và `o:price` thuộc `urn:order`.

Nếu dùng XPath, bạn có thể tự bind:

```text
ord → urn:order
com → urn:common
```

rồi dùng:

```xpath
/ord:order/ord:item/ord:price
```

Prefix trong truy vấn (query / 쿼리) không cần giống prefix nguồn (source / 소스).

Nếu tệp (file / 파일) có 5 triệu `item`, StAX hoặc SAX thường hợp hơn DOM.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **62. mô hình tư duy (mental model / 사고 모델) sau Intermediate** gom các mảnh từ **61. Bài tập tổng hợp Intermediate** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **63. xmlns="": reset default không gian tên (namespace / 네임스페이스) trong subtree** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. mô hình tư duy (mental model / 사고 모델) sau Intermediate

Sau phần này, XML processing luồng (flow / 흐름) của bạn nên mở rộng thành:

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

Bạn cũng phải hiểu rằng không gian tên (namespace / 네임스페이스) và lược đồ (schema / 스키마) là hai lớp riêng. không gian tên (namespace / 네임스페이스) định danh vocabulary; lược đồ (schema / 스키마) mô tả grammar/kiểu (type / 타입) của vocabulary.

Ở phần cấp cao (senior / 시니어), chúng ta sẽ thêm transformation, XQuery, lược đồ (schema / 스키마) evolution, streaming kiến trúc (architecture / 아키텍처), XXE, XML danh mục (catalog / 카탈로그), canonicalization và XML Signature.

---

# PHẦN BỔ SUNG SAU kiểm tra (audit / 감사) — kiểm tra hợp lệ (validation / 검증), không gian tên (namespace / 네임스페이스) VÀ PARSER Ở MỨC THỰC CHIẾN

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **63. xmlns="": reset default không gian tên (namespace / 네임스페이스) trong subtree** gom các mảnh từ **62. mô hình tư duy (mental model / 사고 모델) sau Intermediate** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **64. attributeFormDefault và cục bộ (local / 로컬) attributes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. `xmlns=""`: reset default không gian tên (namespace / 네임스페이스) trong subtree

Default không gian tên (namespace / 네임스페이스) có phạm vi (scope / 범위) và có thể được reset. Ví dụ:

```xml
<root xmlns="urn:outer">
  <item>Outer</item>

  <legacy xmlns="">
    <item>Inner without namespace</item>
  </legacy>
</root>
```

`root` và `item` đầu thuộc `urn:outer`. Khi `legacy` khai báo `xmlns=""`, default không gian tên (namespace / 네임스페이스) bị xóa cho subtree đó, nên `legacy` và `item` bên trong không còn không gian tên (namespace / 네임스페이스).

Đây là một nguồn (source / 소스) bug rất khó nhìn bằng mắt vì cục bộ (local / 로컬) names vẫn giống nhau. Khi DOM/XPath/lược đồ (schema / 스키마) báo không match, hãy inspect không gian tên (namespace / 네임스페이스) URI thực thay vì chỉ nhìn tag văn bản (text / 텍스트).

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **64. attributeFormDefault và cục bộ (local / 로컬) attributes** tiếp nhận điểm tựa từ **63. xmlns="": reset default không gian tên (namespace / 네임스페이스) trong subtree** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. toàn cục (global / 전역) element và cục bộ (local / 로컬) element không chỉ khác vị trí trong tệp (file / 파일) XSD** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. `attributeFormDefault` và cục bộ (local / 로컬) attributes

Ngoài `elementFormDefault`, XSD còn có `attributeFormDefault`. Nó ảnh hưởng việc cục bộ (local / 로컬) attributes có phải namespace-qualified hay không.

Nếu lược đồ (schema / 스키마) có mục tiêu (target / 대상) không gian tên (namespace / 네임스페이스) nhưng một cục bộ (local / 로컬) attribute vẫn unqualified, instance có thể trông như:

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

Hai forms có expanded-name khác nhau. Khi validator báo attribute “không được phép” dù spelling `id` có vẻ đúng, hãy kiểm tra declaration là toàn cục (global / 전역)/cục bộ (local / 로컬) và `attributeFormDefault`/`form` override của attribute.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **65. toàn cục (global / 전역) element và cục bộ (local / 로컬) element không chỉ khác vị trí trong tệp (file / 파일) XSD** tiếp nhận điểm tựa từ **64. attributeFormDefault và cục bộ (local / 로컬) attributes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. XPath có static ngữ cảnh (context / 맥락) và động (dynamic / 동적) ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. toàn cục (global / 전역) element và cục bộ (local / 로컬) element không chỉ khác vị trí trong tệp (file / 파일) XSD

Element được khai báo trực tiếp dưới `xs:schema` là toàn cục (global / 전역) declaration và có thể được tham chiếu (reference / 참조)/reuse theo lược đồ (schema / 스키마) rules. Element nằm trong `complexType`/mô hình (model / 모델) group thường là cục bộ (local / 로컬) declaration.

Điều này ảnh hưởng không gian tên (namespace / 네임스페이스) qualification, reuse, substitution, mã (code / 코드) generation và cách bạn đọc lược đồ (schema / 스키마) phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프). Khi gỡ lỗi (debug / 디버그) Java generated classes, việc two elements cùng cục bộ (local / 로컬) name nhưng đến từ declarations khác nhau có thể dẫn tới types/annotations khác nhau.

Cấp cao (senior / 시니어) lược đồ (schema / 스키마) reading vì vậy nên đi từ gốc (root / 루트)/toàn cục (global / 전역) declarations rồi follow kiểu (type / 타입)/tham chiếu (reference / 참조) đồ thị (graph / 그래프), không đọc XSD như một tệp (file / 파일) XML tuyến tính từ trên xuống.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **65. toàn cục (global / 전역) element và cục bộ (local / 로컬) element không chỉ khác vị trí trong tệp (file / 파일) XSD** xác định đầu vào; **66. XPath có static ngữ cảnh (context / 맥락) và động (dynamic / 동적) ngữ cảnh (context / 맥락)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **67. local-name() không phải cách chữa không gian tên (namespace / 네임스페이스) đúng mặc định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. XPath có static ngữ cảnh (context / 맥락) và động (dynamic / 동적) ngữ cảnh (context / 맥락)

Một XPath expression không tồn tại trong vacuum. Processor evaluate nó với **static ngữ cảnh (context / 맥락)** và **động (dynamic / 동적) ngữ cảnh (context / 맥락)**.

Static ngữ cảnh (context / 맥락) chứa những thứ như không gian tên (namespace / 네임스페이스) prefix bindings, available functions, default hàm (function / 함수) không gian tên (namespace / 네임스페이스) hoặc cơ sở (base / 기반) URI tùy host/phiên bản (version / 버전). động (dynamic / 동적) ngữ cảnh (context / 맥락) chứa ngữ cảnh (context / 맥락) item/nút (node / 노드), position, kích thước (size / 크기), variable values và thời gian chạy (runtime / 런타임) dữ liệu (data / 데이터).

Vì vậy cùng expression:

```xpath
book/title
```

có thể trả kết quả khác hoàn toàn nếu ngữ cảnh (context / 맥락) nút (node / 노드) khác. Đây là lý do mã (code / 코드) gọi XPath trên `Document` và mã (code / 코드) gọi cùng expression trên một `Element` không nhất thiết tương đương.

Khi gỡ lỗi (debug / 디버그) XPath, đừng chỉ hỏi “expression đúng chưa?”. Hãy hỏi thêm “expression đang được evaluate từ nút (node / 노드) nào và không gian tên (namespace / 네임스페이스) ngữ cảnh (context / 맥락) nào?”.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **66. XPath có static ngữ cảnh (context / 맥락) và động (dynamic / 동적) ngữ cảnh (context / 맥락)** xác định đầu vào; **67. local-name() không phải cách chữa không gian tên (namespace / 네임스페이스) đúng mặc định** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **68. SAX characters() có thể được gọi nhiều lần cho một đoạn văn bản (text / 텍스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. `local-name()` không phải cách chữa không gian tên (namespace / 네임스페이스) đúng mặc định

Nhà phát triển (developer / 개발자) đôi khi gặp default-namespace bug rồi viết:

```xpath
//*[local-name()='book']
```

Expression này có thể làm truy vấn (query / 쿼리) trả kết quả (result / 결과), nhưng nó bỏ qua không gian tên (namespace / 네임스페이스) định danh (identity / 식별자). Nếu document trộn `urn:catalog:book` và `urn:malicious:book`, cả hai đều có cục bộ (local / 로컬) name `book`.

Trong generic tooling, `local-name()` có use trường hợp (case / 사례) thật. Nhưng nghiệp vụ (business / 비즈니스)/bảo mật (security / 보안) truy vấn (query / 쿼리) nên bind không gian tên (namespace / 네임스페이스) URI đúng và dùng qualified XPath. “Làm cho truy vấn (query / 쿼리) chạy” không đồng nghĩa “truy vấn (query / 쿼리) đúng ngữ nghĩa (semantic / 의미적)”.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **68. SAX characters() có thể được gọi nhiều lần cho một đoạn văn bản (text / 텍스트)** tiếp nhận điểm tựa từ **67. local-name() không phải cách chữa không gian tên (namespace / 네임스페이스) đúng mặc định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. StAX sự kiện (event / 이벤트) mô hình (model / 모델) và namespace-aware reading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. SAX `characters()` có thể được gọi nhiều lần cho một đoạn văn bản (text / 텍스트)

Một lỗi SAX rất phổ biến là nghĩ parser sẽ gọi `characters()` đúng một lần cho mỗi element văn bản (text / 텍스트). API không đảm bảo như vậy. văn bản (text / 텍스트):

```xml
<name>Alice Wonderland</name>
```

có thể được deliver thành nhiều chunks tùy buffer/thực thể (entity / 엔터티)/parser hiện thực (implementation / 구현).

Handler đúng thường accumulate văn bản (text / 텍스트) trong `StringBuilder` giữa `startElement` và `endElement`, rồi xử lý khi element kết thúc. Không viết lô-gic nghiệp vụ (business logic / 비즈니스 로직) giả định một callback tương ứng một giá trị (value / 값) hoàn chỉnh.

Điểm này cho thấy streaming parser expose **events/chunks**, không expose đối tượng (object / 객체) fields sẵn như binding khung phần mềm (framework / 프레임워크).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **69. StAX sự kiện (event / 이벤트) mô hình (model / 모델) và namespace-aware reading** tiếp nhận điểm tựa từ **68. SAX characters() có thể được gọi nhiều lần cho một đoạn văn bản (text / 텍스트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **70. XSD kiểm tra hợp lệ (validation / 검증) trong Java: SchemaFactory → Schema → Validator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. StAX sự kiện (event / 이벤트) mô hình (model / 모델) và namespace-aware reading

Với StAX, ứng dụng (application / 애플리케이션) chủ động pull events như `START_ELEMENT`, `CHARACTERS`, `END_ELEMENT`. Khi gặp `START_ELEMENT`, hãy đọc `QName`/không gian tên (namespace / 네임스페이스) URI/cục bộ (local / 로컬) part thay vì chỉ `getLocalName()` nếu vocabulary có không gian tên (namespace / 네임스페이스).

Văn bản (text / 텍스트) cũng có thể cần accumulate qua nhiều character events. Whitespace events, comments hoặc CDATA biểu diễn (representation / 표현) có thể xuất hiện tùy reader API/cấu hình (config / 설정). Vì vậy một máy trạng thái (state machine / 상태 머신) tốt xác định rõ “đang ở element nào”, “đang thu trường dữ liệu (field / 필드) nào”, và chỉ finalize giá trị (value / 값) khi gặp end element tương ứng.

Streaming mã (code / 코드) có ít bộ nhớ (memory / 메모리) nhưng đổi lại bạn phải quản lý trạng thái (state / 상태) chính xác hơn DOM.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **70. XSD kiểm tra hợp lệ (validation / 검증) trong Java: SchemaFactory → Schema → Validator** tiếp nhận điểm tựa từ **69. StAX sự kiện (event / 이벤트) mô hình (model / 모델) và namespace-aware reading** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **71. kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) mô hình (model / 모델): warning, lỗi (error / 오류), fatal lỗi (error / 오류) và line/column** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. XSD kiểm tra hợp lệ (validation / 검증) trong Java: `SchemaFactory` → `Schema` → `Validator`

Mô hình tư duy (mental model / 사고 모델) Java điển hình là compile XSD thành `Schema`, rồi tạo `Validator` cho kiểm tra hợp lệ (validation / 검증) thao tác (operation / 연산):

```java
SchemaFactory factory =
    SchemaFactory.newInstance(
        XMLConstants.W3C_XML_SCHEMA_NS_URI
    );

Schema schema = factory.newSchema(xsdFile);
Validator validator = schema.newValidator();

validator.validate(new StreamSource(xmlFile));
```

`SchemaFactory` xử lý lược đồ (schema / 스키마) ngôn ngữ (language / 언어)/compilation. `Schema` đại diện compiled lược đồ (schema / 스키마) mô hình (model / 모델) có thể được reuse theo đặc tả hợp đồng (contract / 계약) của hiện thực (implementation / 구현)/API. `Validator` là đối tượng (object / 객체) dùng để validate một nguồn (source / 소스) và thường không nên được share tùy tiện giữa concurrent operations nếu API không cam kết thread-safety.

Môi trường vận hành (production / 운영 환경) mã (code / 코드) còn phải kiểm soát bên ngoài (external / 외부) lược đồ (schema / 스키마)/DTD truy cập (access / 접근) và resolver; ví dụ mã (code / 코드) ngắn ở trên chỉ minh họa vòng đời (lifecycle / 생명주기), chưa phải security-hardening recipe hoàn chỉnh.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **71. kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) mô hình (model / 모델): warning, lỗi (error / 오류), fatal lỗi (error / 오류) và line/column** tiếp nhận điểm tựa từ **70. XSD kiểm tra hợp lệ (validation / 검증) trong Java: SchemaFactory → Schema → Validator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. kiểm tra hợp lệ (validation / 검증) không nên bị trộn với nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) mô hình (model / 모델): warning, lỗi (error / 오류), fatal lỗi (error / 오류) và line/column

XML APIs thường expose lỗi kèm locator thông tin (information / 정보) như line và column. Với SAX-style `ErrorHandler`, bạn có các mức như warning, lỗi (error / 오류) và fatal lỗi (error / 오류) theo parser/validator ngữ nghĩa (semantics / 의미론).

Well-formedness violation thường là fatal ở XML parsing tầng (layer / 계층): parser không thể tiếp tục như HTML trình duyệt (browser / 브라우저) lỗi (error / 오류) khôi phục (recovery / 복구). lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) nghĩa document đã có thể parse XML nhưng không thỏa đặc tả hợp đồng (contract / 계약) XSD/DTD.

Khi đưa lỗi (error / 오류) ra ứng dụng (application / 애플리케이션) log/API phản hồi (response / 응답), nên preserve tầng (layer / 계층) và location nếu an toàn:

```text
XML_PARSE_ERROR at line 12, column 18
XSD_VALIDATION_ERROR at /order/item[3]/price
```

để nhà phát triển (developer / 개발자) không mất thời gian tìm lỗi lược đồ (schema / 스키마) trong khi document còn chưa well-formed. Với sensitive payload, log ngữ cảnh (context / 맥락) vừa đủ chứ không dump toàn document.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **72. kiểm tra hợp lệ (validation / 검증) không nên bị trộn với nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증)** tiếp nhận điểm tựa từ **71. kiểm tra hợp lệ (validation / 검증) lỗi (error / 오류) mô hình (model / 모델): warning, lỗi (error / 오류), fatal lỗi (error / 오류) và line/column** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **73. Validate trước ánh xạ (mapping / 매핑) hay validate trong lúc ánh xạ (mapping / 매핑)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. kiểm tra hợp lệ (validation / 검증) không nên bị trộn với nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증)

Một chuỗi xử lý (pipeline / 파이프라인) rõ ràng thường phân tầng:

```text
bytes / transport checks
→ secure XML parsing
→ namespace-aware processing
→ XSD/DTD validation nếu contract yêu cầu
→ object/domain mapping
→ business validation
→ authorization
```

XSD có thể kiểm tra `amount` là decimal, positive và đúng cardinality. Nhưng nó không biết account hiện tại có đủ balance hay người dùng (user / 사용자) có quyền chuyển tiền. Ngược lại, nghiệp vụ (business / 비즈니스) validator không nên phải tự kiểm tra XML tag đóng đúng hay không gian tên (namespace / 네임스페이스) có đúng đặc tả hợp đồng (contract / 계약) hay không.

Phân tầng làm lỗi (error / 오류) message rõ hơn, kiểm thử (test / 테스트) dễ hơn và giảm nguy cơ một tầng (layer / 계층) “tin” dữ liệu mà tầng (layer / 계층) trước chưa kiểm tra.

---

> **Chuyển mạch:** Trong **XML — Intermediate**, **73. Validate trước ánh xạ (mapping / 매핑) hay validate trong lúc ánh xạ (mapping / 매핑)?** tiếp nhận điểm tựa từ **72. kiểm tra hợp lệ (validation / 검증) không nên bị trộn với nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **74. kiểm thử (test / 테스트) XML parser/validator bằng negative cases, không chỉ happy đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. Validate trước ánh xạ (mapping / 매핑) hay validate trong lúc ánh xạ (mapping / 매핑)?

Không có một chuỗi xử lý (pipeline / 파이프라인) duy nhất cho mọi thư viện (library / 라이브러리). Có hệ thống parse/validate rồi mới unmarshal; có binding khung phần mềm (framework / 프레임워크) tích hợp lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) trong unmarshal; có streaming chuỗi xử lý (pipeline / 파이프라인) validate và consume gần như cùng lúc.

Điều quan trọng là kết quả (outcome / 결과) phải rõ: **nghiệp vụ (business / 비즈니스) tầng (layer / 계층) chỉ nhận dữ liệu (data / 데이터) sau khi structural đặc tả hợp đồng (contract / 계약) cần thiết đã được kiểm tra**. Nếu hiệu năng (performance / 성능) khiến bạn tránh parse hai lần, hãy thiết kế chuỗi xử lý (pipeline / 파이프라인) streaming/nguồn (source / 소스)/handler phù hợp thay vì bỏ kiểm tra hợp lệ (validation / 검증) mà không nhận ra.

Với tệp (file / 파일) cực lớn, việc bản dựng (build / 빌드) DOM chỉ để validate rồi bản dựng (build / 빌드) lần hai để tiến trình (process / 프로세스) là dấu hiệu kiến trúc (architecture / 아키텍처) cần xem lại.

---

> **Chuyển mạch:** Ở chặng này của **XML — Intermediate**, **73. Validate trước ánh xạ (mapping / 매핑) hay validate trong lúc ánh xạ (mapping / 매핑)?** cho ta quy tắc; **74. kiểm thử (test / 테스트) XML parser/validator bằng negative cases, không chỉ happy đường dẫn (path / 경로)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **75. mô hình tư duy (mental model / 사고 모델) Intermediate sau kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. kiểm thử (test / 테스트) XML parser/validator bằng negative cases, không chỉ happy đường dẫn (path / 경로)

Một bộ kiểm thử (test suite / 테스트 스위트) tốt không chỉ có một tệp (file / 파일) valid. Hãy có fixtures cho wrong không gian tên (namespace / 네임스페이스), missing required element, wrong thứ tự (order / 순서), invalid datatype, nil/empty/missing, duplicate ID, unexpected extension, malformed XML, huge văn bản (text / 텍스트) nút (node / 노드), deep nesting và external-entity payload.

Mục tiêu không phải “kiểm thử (test / 테스트) XML tiêu chuẩn (standard / 표준)”, mà là verify **chính xác (exact / 정확한) parser + chính xác (exact / 정확한) cấu hình (configuration / 구성) + chính xác (exact / 정확한) lược đồ (schema / 스키마) phiên bản (version / 버전)** của ứng dụng (application / 애플리케이션) xử lý ranh giới (boundary / 경계) như bạn nghĩ. Parser defaults và hiện thực (implementation / 구현) phiên bản (version / 버전) khác nhau có thể thay hành vi (behavior / 동작) bảo mật (security / 보안)/hiệu năng (performance / 성능).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Intermediate**, **74. kiểm thử (test / 테스트) XML parser/validator bằng negative cases, không chỉ happy đường dẫn (path / 경로)** cho ta quy tắc; **75. mô hình tư duy (mental model / 사고 모델) Intermediate sau kiểm tra (audit / 감사)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 75. mô hình tư duy (mental model / 사고 모델) Intermediate sau kiểm tra (audit / 감사)

Sau khi bổ sung các phần trên, luồng (flow / 흐름) nên được hiểu như sau:

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

Không gian tên (namespace / 네임스페이스) trả lời **nút (node / 노드) thuộc vocabulary nào**. lược đồ (schema / 스키마) trả lời **vocabulary đó cho phép cấu trúc/kiểu (type / 타입) nào**. Parser mô hình (model / 모델) trả lời **ứng dụng (application / 애플리케이션) nhận cây (tree / 트리) hay stream events**. XPath trả lời **cách chọn/tính trên mô hình (model / 모델) đó**. nghiệp vụ (business / 비즈니스) kiểm tra hợp lệ (validation / 검증) trả lời **dữ liệu (data / 데이터) hợp lĩnh vực (domain / 도메인) và quyền hay không**.

Nếu bạn tách được năm câu hỏi này trong đầu, bạn đã qua được phần dễ nhầm nhất của XML Intermediate.

> **Bàn giao:** Sau **75. mô hình tư duy (mental model / 사고 모델) Intermediate sau kiểm tra (audit / 감사)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
