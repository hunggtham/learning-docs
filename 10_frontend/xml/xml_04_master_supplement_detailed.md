# XML — Master Supplement

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **XML — Master Supplement**. Route đi từ XML 1.0/1.1 internals → XSD 1.1, XPath/XQuery/XSLT 3.x → canonicalization, signatures và serialization → edge cases/spec reading → document-centric production debugging.

## XML specification internals, XSD 1.1, XPath/XQuery/XSLT 3.x, canonicalization và các trường hợp biên (edge case / 경계 사례) cần biết để thực sự master XML

Tài liệu này là phần cuối của bộ XML. Bạn chỉ nên đọc sau khi đã hiểu ba phần trước. Mục tiêu không phải biến bạn thành người thuộc lòng W3C specification, mà là giúp bạn có mô hình tư duy (mental model / 사고 모델) đủ sâu để đọc specification khi cần, gỡ lỗi (debug / 디버그) parser khác nhau, hiểu vì sao serialization có thể thay đổi nhưng ngữ nghĩa (semantics / 의미론) không đổi, phân biệt schema-typed dữ liệu (data / 데이터) với raw XML, và xử lý những hệ thống dùng XML Signature, XSD 1.1, XSLT 3.0 hoặc document-centric XML phức tạp.

Ở mức này, XML không còn chỉ là “markup ngôn ngữ (language / 언어)”. Nó là một hệ sinh thái gồm lexical cú pháp (syntax / 문법), namespaces, lược đồ (schema / 스키마) hệ kiểu (type system / 타입 시스템), truy vấn (query / 쿼리) mô hình dữ liệu (data model / 데이터 모델), transformation engine, URI resolution, bảo mật (security / 보안) mô hình (model / 모델) và chuẩn gốc (canonical / 정본) biểu diễn (representation / 표현).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **XML specification internals, XSD 1.1, XPath/XQuery/XSLT 3.x, canonicalization và các trường hợp biên (edge case / 경계 사례) cần biết để thực sự master XML** cho ta quy tắc; **1. XML 1.0 và XML 1.1** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **2. XML 1.0 Fifth Edition và Unicode names** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. XML 1.0 và XML 1.1

Hai phiên bản (version / 버전) chính tồn tại là XML 1.0 và XML 1.1.

XML 1.0 là phiên bản (version / 버전) phổ biến nhất trong môi trường vận hành (production / 운영 환경). XML 1.1 thay đổi một số quy tắc (rule / 규칙) liên quan character repertoire, điều khiển (control / 제어) characters và newline handling để phù hợp hơn với một số Unicode/use cases.

Điều quan trọng là XML 1.1 không phải “XML mới hơn nên luôn tốt hơn”. Ecosystem hỗ trợ (support / 지원) quan trọng hơn phiên bản (version / 버전) number. Nếu partner, Java thư viện (library / 라이브러리), công cụ (tool / 도구), lược đồ (schema / 스키마) processor và downstream hệ thống (system / 시스템) đều dùng XML 1.0, việc tự chuyển sang 1.1 chỉ tạo tính tương thích (compatibility / 호환성) rủi ro (risk / 위험).

Vì vậy nếu không có yêu cầu (requirement / 요구사항) rõ, XML 1.0 vẫn là lựa chọn interoperable nhất.

---

> **Chuyển mạch:** XML 1.0/1.1 đặt version boundary; Fifth Edition và Unicode names làm rõ tên nào hợp lệ trong grammar. Phần UTF-8 tiếp theo tách encoding validity khỏi XML character validity.

## 2. XML 1.0 Fifth Edition và Unicode names

XML 1.0 Fifth Edition là một mốc quan trọng vì XML Name grammar hỗ trợ Unicode rộng hơn nhiều so với cách nhà phát triển (developer / 개발자) thường tưởng.

Một regex kiểu:

```regex
[A-Za-z_][A-Za-z0-9_-]*
```

không đại diện đầy đủ XML Name grammar.

Điều này quan trọng vì nhiều nhà phát triển (developer / 개발자) tự validate element name hoặc bản dựng (build / 빌드) động (dynamic / 동적) XML bằng regex ASCII. Nếu đầu vào (input / 입력) có Unicode name hợp lệ, regex có thể reject sai. Ngược lại, regex tự chế có thể cho phép cấu trúc (structure / 구조) không hợp grammar thực.

Quy tắc (rule / 규칙) đúng là dùng parser/serializer/lược đồ (schema / 스키마) thư viện (library / 라이브러리) để xử lý XML names.

---

> **Chuyển mạch:** XML edition và Unicode names xác định vocabulary, nhưng UTF‑8 validity chưa đủ; XML character rules tiếp theo mới quyết định document hợp lệ.

## 3. Valid UTF‑8 không đồng nghĩa valid XML character

UTF‑8 chỉ là encoding. XML phiên bản (version / 버전) còn quy định character nào được phép xuất hiện.

Vì vậy byte chuỗi (sequence / 시퀀스) có thể decode thành Unicode hợp lệ nhưng character đó vẫn không được phép trong XML phiên bản (version / 버전) đang dùng.

Đừng tự nghĩ “nếu string Java chứa được thì XML serialize được”. XML serializer chuẩn phải kiểm tra character legality.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **4. End-of-line normalization** tiếp nhận điểm tựa từ **3. Valid UTF‑8 không đồng nghĩa valid XML character** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Attribute giá trị (value / 값) normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. End-of-line normalization

XML parser có quy tắc (rule / 규칙) chuẩn hóa line endings.

Một tệp (file / 파일) có thể dùng CRLF, CR hoặc LF tùy nền tảng (platform / 플랫폼). Sau parsing, processor có thể expose newline theo normalized form.

Điều này cho thấy một nguyên tắc lớn: **raw lexical bytes và parsed character dữ liệu (data / 데이터) không phải cùng tầng (layer / 계층)**.

Nếu bạn compare raw tệp (file / 파일) byte-for-byte với dữ liệu (data / 데이터) sau parser, bạn đang compare hai representations khác nhau.

Đây cũng là lý do XML Digital Signature không thể chỉ “băm (hash / 해시) pretty-printed XML” tùy tiện.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **5. Attribute giá trị (value / 값) normalization** tiếp nhận điểm tựa từ **4. End-of-line normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. standalone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Attribute giá trị (value / 값) normalization

Attribute values cũng có normalization rules.

Ví dụ thực thể (entity / 엔터티) references có thể được expanded, whitespace có thể được normalized theo XML/DTD kiểu (type / 타입) rules, và ứng dụng (application / 애플리케이션) cuối cùng nhận string khác lexical nguồn (source / 소스).

Nếu DTD khai báo attribute kiểu (type / 타입) không phải CDATA, normalization có thể mạnh hơn.

Điều này có hai consequences. Thứ nhất, lô-gic nghiệp vụ (business logic / 비즈니스 로직) không nên phụ thuộc chính xác (exact / 정확한) lexical spelling của attribute nếu đặc tả hợp đồng (contract / 계약) nói ngữ nghĩa (semantic / 의미적) giá trị (value / 값). Thứ hai, cryptographic giao thức (protocol / 프로토콜) phải xác định canonicalization đúng thay vì ký raw nguồn (source / 소스) tùy công cụ (tool / 도구).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **6. standalone** tiếp nhận điểm tựa từ **5. Attribute giá trị (value / 값) normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. nội bộ (internal / 내부) subset và bên ngoài (external / 외부) subset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. `standalone`

XML declaration có thể chứa:

```xml
<?xml
  version="1.0"
  encoding="UTF-8"
  standalone="yes"?>
```

`standalone` không có nghĩa “tệp (file / 파일) này không cần internet” hoặc “không được tải (load / 로드) bên ngoài (external / 외부) resources”.

Nó liên quan việc bên ngoài (external / 외부) markup declarations có ảnh hưởng tới thông tin (information / 정보) được processor truyền cho ứng dụng (application / 애플리케이션) hay không theo XML rules.

Đây là một tính năng (feature / 기능) specification-level, hiếm khi ứng dụng (application / 애플리케이션) nhà phát triển (developer / 개발자) cần set thủ công.

---

# DTD Deeper

> **Chuyển mạch:** Trong **XML — Master Supplement**, **7. nội bộ (internal / 내부) subset và bên ngoài (external / 외부) subset** tiếp nhận điểm tựa từ **6. standalone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Parameter entities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nội bộ (internal / 내부) subset và bên ngoài (external / 외부) subset

DOCTYPE có thể có nội bộ (internal / 내부) subset:

```xml
<!DOCTYPE root [
  <!ELEMENT root (#PCDATA)>
]>
```

hoặc bên ngoài (external / 외부) subset:

```xml
<!DOCTYPE root SYSTEM "root.dtd">
```

hoặc kết hợp theo grammar phù hợp.

Điểm cần nhớ ở mức master là DTD processing không chỉ là “validate cấu trúc (structure / 구조)”. Nó có thể ảnh hưởng entities, default attribute values và thông tin (information / 정보) ứng dụng (application / 애플리케이션) nhận.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **8. Parameter entities** tiếp nhận điểm tựa từ **7. nội bộ (internal / 내부) subset và bên ngoài (external / 외부) subset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Unparsed entities và NOTATION** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Parameter entities

General thực thể (entity / 엔터티) dùng trong document content:

```xml
&company;
```

Parameter thực thể (entity / 엔터티) dùng trong DTD:

```dtd
<!ENTITY % common SYSTEM "common.dtd">
%common;
```

Parameter entities cho phép modularize DTD grammar.

Nhưng bên ngoài (external / 외부) parameter entities cũng là một phần của XXE attack surface. Nếu bạn chỉ disable general bên ngoài (external / 외부) entities nhưng vẫn để parameter thực thể (entity / 엔터티) resolution mở, parser có thể vẫn truy cập (access / 접근) bên ngoài (external / 외부) resources.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **9. Unparsed entities và NOTATION** tiếp nhận điểm tựa từ **8. Parameter entities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. không gian tên (namespace / 네임스페이스) URI là identifier, không phải URL để normalize tùy ý** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Unparsed entities và NOTATION

DTD còn có khái niệm unparsed thực thể (entity / 엔터티) và notation để liên kết XML document với bên ngoài (external / 외부) non-XML dữ liệu (data / 데이터) format.

Trong ứng dụng (application / 애플리케이션) hiện đại bạn ít gặp chúng, nhưng có thể thấy trong publishing, SGML-derived ecosystem hoặc old document standards.

Bạn không cần memorize cú pháp (syntax / 문법) chi tiết, chỉ cần nhận diện rằng DTD thực thể (entity / 엔터티) hệ thống (system / 시스템) rộng hơn việc thay `&name;` bằng văn bản (text / 텍스트).

---

# Không gian tên (namespace / 네임스페이스) Deeper

> **Chuyển mạch:** Trong **XML — Master Supplement**, **10. không gian tên (namespace / 네임스페이스) URI là identifier, không phải URL để normalize tùy ý** tiếp nhận điểm tựa từ **9. Unparsed entities và NOTATION** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Expanded name phải trở thành mô hình tư duy (mental model / 사고 모델) mặc định** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. không gian tên (namespace / 네임스페이스) URI là identifier, không phải URL để normalize tùy ý

Hai strings:

```text
https://example.com/ns
```

và:

```text
https://example.com/ns/
```

không nên được ứng dụng (application / 애플리케이션) tự coi là cùng không gian tên (namespace / 네임스페이스) chỉ vì “URL giống nhau”.

Không gian tên (namespace / 네임스페이스) định danh (identity / 식별자) dựa trên không gian tên (namespace / 네임스페이스) name theo specification, không dựa trên HTTP redirect, DNS equivalence hoặc URL canonicalization tự chế.

Đây là nguyên tắc cực kỳ quan trọng với signature, bảo mật (security / 보안) matching và lược đồ (schema / 스키마) resolution.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **11. Expanded name phải trở thành mô hình tư duy (mental model / 사고 모델) mặc định** gom các mảnh từ **10. không gian tên (namespace / 네임스페이스) URI là identifier, không phải URL để normalize tùy ý** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **12. QName** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Expanded name phải trở thành mô hình tư duy (mental model / 사고 모델) mặc định

Element:

```xml
<a:Order xmlns:a="urn:order"/>
```

không có định danh (identity / 식별자) lô-gic (logic / 논리) là `a:Order`.

Định danh (identity / 식별자) là:

```text
namespace = urn:order
local name = Order
```

Nếu đầu vào (input / 입력) đổi thành:

```xml
<o:Order xmlns:o="urn:order"/>
```

Ngữ nghĩa (semantics / 의미론) không gian tên (namespace / 네임스페이스) vẫn giữ nguyên.

Mọi mã (code / 코드) security-sensitive nên match bằng không gian tên (namespace / 네임스페이스) URI + cục bộ (local / 로컬) name.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **12. QName** gom các mảnh từ **11. Expanded name phải trở thành mô hình tư duy (mental model / 사고 모델) mặc định** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **13. cơ sở (base / 기반) URI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. QName

QName là qualified name như:

```text
xs:string
app:OrderType
```

Điểm khó là QName không chỉ xuất hiện trong element names. Nó còn có thể nằm **trong attribute giá trị (value / 값)**.

Ví dụ:

```xml
<xs:element type="app:OrderType"/>
```

Để hiểu `app:OrderType`, processor phải nhìn không gian tên (namespace / 네임스페이스) binding của prefix `app` trong ngữ cảnh (context / 맥락) hiện tại.

Nếu bạn bản sao (copy / 복사) một attribute QName-valued sang một element khác nhưng quên bản sao (copy / 복사) không gian tên (namespace / 네임스페이스) declaration, lexical văn bản (text / 텍스트) giống nhau nhưng meaning hỏng.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **13. cơ sở (base / 기반) URI** tiếp nhận điểm tựa từ **12. QName** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. XML thông tin (information / 정보) Set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. cơ sở (base / 기반) URI

XML nút (node / 노드)/document có thể có cơ sở (base / 기반) URI dựa trên document location, `xml:base` và processor ngữ cảnh (context / 맥락).

Functions hoặc processors có thể resolve relative URI dựa trên cơ sở (base / 기반) URI.

Ví dụ XSLT `document()`, lược đồ (schema / 스키마) imports hoặc ứng dụng (application / 애플리케이션) link resolution đều có thể bị ảnh hưởng.

Ở mức bảo mật (security / 보안), cơ sở (base / 기반) URI và URI resolver phải được xem cùng nhau. Một relative URI tưởng vô hại có thể resolve thành cục bộ (local / 로컬) tệp (file / 파일) hoặc remote mạng (network / 네트워크) tài nguyên (resource / 자원).

---

# Infoset và PSVI

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **14. XML thông tin (information / 정보) Set** tiếp nhận điểm tựa từ **13. cơ sở (base / 기반) URI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. PSVI là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. XML thông tin (information / 정보) Set

XML Infoset là mô hình abstract mô tả “thông tin (information / 정보)” có trong một XML document sau parsing, không tập trung vào chính xác (exact / 정확한) lexical spelling.

Ví dụ:

```xml
<a x="1"/>
```

và:

```xml
<a x='1'></a>
```

khác cách viết nhưng không nhất thiết khác thông tin (information / 정보) ở mức (level / 수준) mà nhiều XML applications quan tâm.

Infoset giúp bạn hiểu vì sao parse → serialize có thể đổi quote style, self-closing form hoặc attribute formatting mà ngữ nghĩa (semantics / 의미론) vẫn giữ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **15. PSVI là gì?** tiếp nhận điểm tựa từ **14. XML thông tin (information / 정보) Set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Default values từ lược đồ (schema / 스키마)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. PSVI là gì?

PSVI = Post-Schema-Validation Infoset.

Sau XSD kiểm tra hợp lệ (validation / 검증), processor không chỉ biết nodes/văn bản (text / 텍스트) nữa. Nó có thể biết thêm:

```text
element thuộc type nào
attribute thuộc type nào
value normalized/typed ra sao
default value nào được schema supply
validation status
```

Điều này tạo ra một typed view của XML.

Nếu ứng dụng (application / 애플리케이션) dùng schema-aware XSLT/XQuery processor, kiểu (type / 타입) thông tin (information / 정보) có thể ảnh hưởng expression ngữ nghĩa (semantics / 의미론).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **16. Default values từ lược đồ (schema / 스키마)** tiếp nhận điểm tựa từ **15. PSVI là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Tại sao XSD 1.1 xuất hiện?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Default values từ lược đồ (schema / 스키마)

Lược đồ (schema / 스키마) có thể định nghĩa default/fixed values.

Điều này nghĩa raw XML nguồn (source / 소스) không có attribute/element giá trị (value / 값) rõ ràng, nhưng post-validation mô hình ứng dụng (application model / 애플리케이션 모델) có thể expose schema-supplied giá trị (value / 값) tùy API.

Đây là lý do khi gỡ lỗi (debug / 디버그) “tại sao đối tượng (object / 객체) có giá trị mà nguồn (source / 소스) XML không có”, bạn phải kiểm tra lược đồ (schema / 스키마) defaults.

---

# XSD 1.1

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **17. Tại sao XSD 1.1 xuất hiện?** tiếp nhận điểm tựa từ **16. Default values từ lược đồ (schema / 스키마)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. xs:assert** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Tại sao XSD 1.1 xuất hiện?

XSD 1.0 rất mạnh về cấu trúc (structure / 구조) và kiểu (type / 타입) nhưng khó diễn tả một số cross-field các ràng buộc (constraints / 제약조건들).

Ví dụ yêu cầu (requirement / 요구사항):

```text
min <= max
```

hoặc:

```text
nếu type = BUSINESS thì companyName bắt buộc
```

XSD 1.1 thêm mechanisms như assertions và kiểu (type / 타입) alternatives để xử lý nhiều quy tắc (rule / 규칙) loại này.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **18. xs:assert** tiếp nhận điểm tựa từ **17. Tại sao XSD 1.1 xuất hiện?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. kiểu (type / 타입) alternatives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. `xs:assert`

Ví dụ concept:

```xml
<xs:assert test="@min le @max"/>
```

Assertion dùng XPath-like expression để kiểm tra ràng buộc (constraint / 제약조건) trên instance.

Điều này làm lược đồ (schema / 스키마) expressive hơn nhưng cũng đẩy business-like lô-gic (logic / 논리) vào lược đồ (schema / 스키마).

Bạn phải cân bằng giữa “lược đồ (schema / 스키마) kiểm tra hợp lệ (validation / 검증) mạnh” và “lược đồ (schema / 스키마) quá thông minh khó gỡ lỗi (debug / 디버그)”.

Ngoài ra processor hỗ trợ (support / 지원) XSD 1.1 không universal. Không assume Java default XML lược đồ (schema / 스키마) hiện thực (implementation / 구현) hỗ trợ (support / 지원) mọi tính năng (feature / 기능).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **19. kiểu (type / 타입) alternatives** tiếp nhận điểm tựa từ **18. xs:assert** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. XSD regex không giống regex bạn dùng trong Java** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. kiểu (type / 타입) alternatives

XSD 1.1 có thể chọn kiểu (type / 타입) dựa trên conditions.

Ví dụ conceptually, một element có attribute `kind="company"` có thể dùng CompanyType, còn `kind="person"` dùng PersonType.

Tính năng (feature / 기능) này powerful nhưng làm interoperability giảm nếu bên tiêu thụ (consumer / 소비자) chỉ hỗ trợ (support / 지원) XSD 1.0.

Trong cross-company tích hợp (integration / 통합), hỗ trợ (support / 지원) ma trận (matrix / 행렬) quan trọng hơn việc dùng tính năng (feature / 기능) mới nhất.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **20. XSD regex không giống regex bạn dùng trong Java** tiếp nhận điểm tựa từ **19. kiểu (type / 타입) alternatives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. whiteSpace facet** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. XSD regex không giống regex bạn dùng trong Java

`xs:pattern` dùng XML lược đồ (schema / 스키마) regex ngữ nghĩa (semantics / 의미론).

Các khái niệm như anchoring, character classes và Unicode categories không map 1:1 với JavaScript/Java/PCRE.

Nếu đặc tả hợp đồng (contract / 계약) có regex quan trọng, kiểm thử (test / 테스트) bằng đúng lược đồ (schema / 스키마) processor.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **21. whiteSpace facet** tiếp nhận điểm tựa từ **20. XSD regex không giống regex bạn dùng trong Java** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. xs:token không phải đơn vị từ (token / 토큰) bảo mật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. `whiteSpace` facet

XSD có `whiteSpace` facet với các hành vi (behavior / 동작) như:

```text
preserve
replace
collapse
```

Điều này ảnh hưởng lexical normalization trước khi giá trị (value / 값) được interpret.

Ví dụ `xs:string` và `xs:token` không có cùng whitespace hành vi (behavior / 동작).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **22. xs:token không phải đơn vị từ (token / 토큰) bảo mật** tiếp nhận điểm tựa từ **21. whiteSpace facet** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. xs:decimal** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. `xs:token` không phải đơn vị từ (token / 토큰) bảo mật

Tên `token` dễ gây hiểu nhầm.

`xs:token` là string-derived datatype với whitespace collapsing ngữ nghĩa (semantics / 의미론). Nó phù hợp với các văn bản (text / 텍스트) values nơi runs of whitespace không có ý nghĩa.

Đừng đọc `xs:token` rồi nghĩ nó liên quan JWT hoặc auth đơn vị từ (token / 토큰).

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **23. xs:decimal** tiếp nhận điểm tựa từ **22. xs:token không phải đơn vị từ (token / 토큰) bảo mật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Date/thời gian (time / 시간) types và timezone** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `xs:decimal`

`xs:decimal` là decimal number mô hình (model / 모델), không phải IEEE floating-point.

Với financial XML:

```xml
<amount>123.45</amount>
```

Ánh xạ (mapping / 매핑) sang Java `BigDecimal` thường phù hợp hơn `double`.

Nếu dùng `double`, nhị phân (binary / 이진) floating điểm (point / 지점) có thể tạo rounding artifacts không phù hợp money calculation.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **24. Date/thời gian (time / 시간) types và timezone** tiếp nhận điểm tựa từ **23. xs:decimal** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들) không dùng arbitrary XPath 3.1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Date/thời gian (time / 시간) types và timezone

`xs:dateTime` có lexical/timezone ngữ nghĩa (semantics / 의미론) phức tạp hơn việc “parse thành LocalDateTime”.

Ví dụ một giá trị (value / 값) có thể có timezone offset, còn giá trị (value / 값) khác không có timezone.

Nếu đặc tả hợp đồng (contract / 계약) cần instant tuyệt đối, phải định nghĩa timezone yêu cầu (requirement / 요구사항) rõ.

Ánh xạ (mapping / 매핑):

```text
xs:dateTime
```

sang Java kiểu (type / 타입) nào phụ thuộc ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약), không chỉ cú pháp (syntax / 문법).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **24. Date/thời gian (time / 시간) types và timezone** xác định đầu vào; **25. định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들) không dùng arbitrary XPath 3.1** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **26. Vì sao phải biết XPath phiên bản (version / 버전)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들) không dùng arbitrary XPath 3.1

Selectors/fields của `xs:key`, `xs:keyref`, `xs:unique` dùng một XPath subset/quy tắc (rule / 규칙) set dành riêng cho lược đồ (schema / 스키마) các ràng buộc (constraints / 제약조건들).

Đừng assume mọi expression chạy được trong Saxon XPath 3.1 sẽ chạy được trong `xs:key`.

---

# XPath 1.0 đến XPath 3.1

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **25. định danh (identity / 식별자) các ràng buộc (constraints / 제약조건들) không dùng arbitrary XPath 3.1** xác định đầu vào; **26. Vì sao phải biết XPath phiên bản (version / 버전)?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **27. XPath 1.0 mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Vì sao phải biết XPath phiên bản (version / 버전)?

Một trình duyệt (browser / 브라우저) API hoặc legacy Java engine có thể chỉ hỗ trợ (support / 지원) XPath 1.0, trong khi Saxon hoặc XML cơ sở dữ liệu (database / 데이터베이스) hỗ trợ (support / 지원) XPath 3.1.

Expression hợp lệ ở 3.1 có thể không chạy ở 1.0.

Vì vậy khi gỡ lỗi (debug / 디버그), luôn hỏi:

```text
XPath version nào?
processor nào?
schema-aware không?
```

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **27. XPath 1.0 mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **26. Vì sao phải biết XPath phiên bản (version / 버전)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **28. hiện đại (modern / 현대적) XPath mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. XPath 1.0 mô hình tư duy (mental model / 사고 모델)

XPath 1.0 chủ yếu xoay quanh:

```text
node-set
string
number
boolean
```

Nhiều built-in trình duyệt (browser / 브라우저) XPath APIs vẫn gần mô hình tư duy (mental model / 사고 모델) này.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **28. hiện đại (modern / 현대적) XPath mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **27. XPath 1.0 mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **29. Effective Boolean giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. hiện đại (modern / 현대적) XPath mô hình tư duy (mental model / 사고 모델)

XPath 2.0/3.x chuyển sang sequence-based typed mô hình dữ liệu (data model / 데이터 모델).

Expression có thể trả:

```text
sequence of nodes
sequence of strings
sequence of integers
mixed typed items
```

XDM là nền tảng.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **29. Effective Boolean giá trị (value / 값)** gom các mảnh từ **28. hiện đại (modern / 현대적) XPath mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **30. General comparison vs giá trị (value / 값) comparison** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Effective Boolean giá trị (value / 값)

Khi expression nằm trong điều kiện (condition / 조건), XPath dùng Effective Boolean giá trị (value / 값) rules.

Đây không giống JavaScript truthiness.

Ví dụ chuỗi (sequence / 시퀀스) nhiều atomic values có thể tạo động (dynamic / 동적) lỗi (error / 오류) trong ngữ cảnh (context / 맥락) mà JS chỉ coi array là truthy.

Cấp cao (senior / 시니어) XPath phải đọc EBV rules thay vì suy từ ngôn ngữ khác.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **30. General comparison vs giá trị (value / 값) comparison** tiếp nhận điểm tựa từ **29. Effective Boolean giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. nút (node / 노드) định danh (identity / 식별자)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. General comparison vs giá trị (value / 값) comparison

Hiện đại (modern / 현대적) XPath có general comparisons:

```xpath
=
!=
<
<=
>
>=
```

và giá trị (value / 값) comparisons:

```xpath
eq
ne
lt
le
gt
ge
```

General comparisons có sequence-oriented ngữ nghĩa (semantics / 의미론), còn giá trị (value / 값) comparisons kỳ vọng singleton atomic values theo rules chặt hơn.

Điều này rất quan trọng khi expression trả nhiều items.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **31. nút (node / 노드) định danh (identity / 식별자)** tiếp nhận điểm tựa từ **30. General comparison vs giá trị (value / 값) comparison** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Maps trong XPath/XQuery 3.1** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. nút (node / 노드) định danh (identity / 식별자)

Hai nodes có thể có cùng văn bản (text / 텍스트)/giá trị (value / 값) nhưng không phải cùng nút (node / 노드).

XPath có nút (node / 노드) comparison như:

```text
is
<<
>>
```

để hỏi định danh (identity / 식별자) hoặc document thứ tự (order / 순서).

Đừng dùng string equality nếu yêu cầu (requirement / 요구사항) thật sự là “đây có phải chính xác (exact / 정확한) same nút (node / 노드) không?”

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **31. nút (node / 노드) định danh (identity / 식별자)** xác định đầu vào; **32. Maps trong XPath/XQuery 3.1** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **33. Arrays** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Maps trong XPath/XQuery 3.1

Hiện đại (modern / 현대적) XDM có maps:

```xquery
map {
  "name": "Alice",
  "age": 27
}
```

Điều này giúp truy vấn (query / 쿼리) ecosystem xử lý dữ liệu (data / 데이터) giống JSON đối tượng (object / 객체), không chỉ XML nodes.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **32. Maps trong XPath/XQuery 3.1** xác định đầu vào; **33. Arrays** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **34. hàm (function / 함수) items** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Arrays

Arrays:

```xquery
[1, 2, 3]
```

là first-class items trong 3.1 ecosystem.

Điều này cho thấy XPath/XQuery đã mở rộng xa hơn “ngôn ngữ chọn XML tag”.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **34. hàm (function / 함수) items** tiếp nhận điểm tựa từ **33. Arrays** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Computed constructors trong XQuery** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. hàm (function / 함수) items

Functions có thể được truyền như values.

Điều này cho phép higher-order programming, hàm (function / 함수) composition và động (dynamic / 동적) invocation.

Nếu bạn chỉ biết XPath 1.0, đây là một thay đổi mô hình tư duy (mental model / 사고 모델) rất lớn.

---

# XQuery và XSLT hiện đại

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **35. Computed constructors trong XQuery** tiếp nhận điểm tựa từ **34. hàm (function / 함수) items** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. XQuery modules** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Computed constructors trong XQuery

XQuery có thể tạo XML mà tên hoặc giá trị (value / 값) được tính thời gian chạy (runtime / 런타임):

```xquery
element user {
  attribute id { $id },
  element name { $name }
}
```

Điều này useful khi đầu ra (output / 출력) cấu trúc (structure / 구조) động (dynamic / 동적).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **36. XQuery modules** tiếp nhận điểm tựa từ **35. Computed constructors trong XQuery** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. XSLT 3.0 packages** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. XQuery modules

Large XQuery ứng dụng (application / 애플리케이션) có modules, functions, namespaces và imports.

Một số XML-native cơ sở dữ liệu (database / 데이터베이스) dùng XQuery như ứng dụng (application / 애플리케이션)/truy vấn (query / 쿼리) ngôn ngữ (language / 언어) thực sự, không chỉ là một expression ngắn.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **37. XSLT 3.0 packages** tiếp nhận điểm tựa từ **36. XQuery modules** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. XSLT accumulators** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. XSLT 3.0 packages

Packages cung cấp modularity ở mức (level / 수준) cao hơn biểu định kiểu (stylesheet / 스타일시트) include/import cổ điển.

Chúng có concepts về exposed/accepted components, visibility và versioning.

Điều này giúp biểu định kiểu (stylesheet / 스타일시트) enterprise được tổ chức giống software modules hơn.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **38. XSLT accumulators** tiếp nhận điểm tựa từ **37. XSLT 3.0 packages** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Modes và on-no-match** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. XSLT accumulators

Streaming transformation đôi khi cần running trạng thái (state / 상태), ví dụ section number hoặc running total.

Accumulators cung cấp cơ chế declarative để tính trạng thái (state / 상태) theo traversal.

Chúng là ví dụ về việc XSLT 3.0 giải quyết vấn đề mà imperative programmer thường nghĩ phải dùng mutable variables.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **39. Modes và on-no-match** tiếp nhận điểm tựa từ **38. XSLT accumulators** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. định danh (identity / 식별자) Transformation mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Modes và `on-no-match`

Hiện đại (modern / 현대적) XSLT modes có thể định nghĩa default processing hành vi (behavior / 동작).

Ví dụ một chế độ (mode / 모드) có thể nói “nếu không có template specialized thì shallow-copy nút (node / 노드)”.

Điều này giúp implement identity-transform-like mẫu (pattern / 패턴) rất gọn.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **40. định danh (identity / 식별자) Transformation mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **39. Modes và on-no-match** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. XML danh mục (catalog / 카탈로그) sâu hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. định danh (identity / 식별자) Transformation mẫu (pattern / 패턴)

Một transformation phổ biến là:

```text
copy toàn document
nhưng override vài node cần thay
```

Ví dụ đổi không gian tên (namespace / 네임스페이스), redact password hoặc rename một element.

Thay vì viết đầu ra (output / 출력) cho toàn cây (tree / 트리), bạn dùng định danh (identity / 식별자)/default-copy quy tắc (rule / 규칙) rồi chỉ override difference.

Mẫu (pattern / 패턴) này cực kỳ quan trọng trong di chuyển (migration / 마이그레이션) và normalization.

---

# Resolver và bên ngoài (external / 외부) Resources

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **41. XML danh mục (catalog / 카탈로그) sâu hơn** tiếp nhận điểm tựa từ **40. định danh (identity / 식별자) Transformation mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Controlled URI Resolver mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. XML danh mục (catalog / 카탈로그) sâu hơn

XML danh mục (catalog / 카탈로그) không chỉ map lược đồ (schema / 스키마) URL. Nó có thể map hệ thống (system / 시스템) identifiers, công khai (public / 공개) identifiers hoặc URI references tùy danh mục (catalog / 카탈로그) rules.

Trong bản dựng (build / 빌드)/tích hợp (integration / 통합) môi trường (environment / 환경), danh mục (catalog / 카탈로그) giúp biến bên ngoài (external / 외부) dependencies thành controlled cục bộ (local / 로컬) resources.

Điều này rất hữu ích nếu vendor lược đồ (schema / 스키마) dùng absolute URL nhưng môi trường vận hành (production / 운영 환경) không được internet truy cập (access / 접근).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **42. Controlled URI Resolver mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **41. XML danh mục (catalog / 카탈로그) sâu hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Canonicalization giải quyết vấn đề gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Controlled URI Resolver mẫu (pattern / 패턴)

Một kiến trúc (architecture / 아키텍처) tốt là không cho processor tự truy cập filesystem/mạng (network / 네트워크).

Thay vào đó:

```text
processor asks resolver for URI
→ resolver checks allowlist/catalog
→ resolver returns trusted local resource
```

Mẫu (pattern / 패턴) này áp dụng với XSD imports, XSLT includes/imports, `document()` và legacy DTD.

Điểm mạnh là bảo mật (security / 보안) chính sách (policy / 정책) tập trung ở một ranh giới (boundary / 경계).

---

# Chuẩn gốc (canonical / 정본) XML

> **Chuyển mạch:** Trong **XML — Master Supplement**, sau nội dung của **42. Controlled URI Resolver mẫu (pattern / 패턴)**, **43. Canonicalization giải quyết vấn đề gì?** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **44. Inclusive và Exclusive Canonicalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Canonicalization giải quyết vấn đề gì?

XML có nhiều lexical forms tương đương về ngữ nghĩa (semantic / 의미적) thông tin (information / 정보).

Ví dụ attribute thứ tự (order / 순서), quote style, empty element cú pháp (syntax / 문법) và không gian tên (namespace / 네임스페이스) declaration placement có thể khác.

Chuẩn gốc (canonical / 정본) XML định nghĩa cách biến XML thông tin (information / 정보) thành deterministic serialization theo thuật toán (algorithm / 알고리즘) cụ thể.

Nó được dùng nhiều nhất trong digital signatures.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **44. Inclusive và Exclusive Canonicalization** tiếp nhận điểm tựa từ **43. Canonicalization giải quyết vấn đề gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. tham chiếu (reference / 참조) là trọng tâm của XML Signature** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Inclusive và Exclusive Canonicalization

Trong XML Signature ecosystem có nhiều canonicalization algorithms.

Exclusive canonicalization đặc biệt hữu ích khi sign một subtree có thể được move hoặc embed trong namespace-rich ngữ cảnh (context / 맥락), vì bạn không muốn surrounding không gian tên (namespace / 네임스페이스) declarations thay đổi chuẩn gốc (canonical / 정본) form ngoài ý muốn.

Bạn không cần tự implement, nhưng phải biết thuật toán (algorithm / 알고리즘) identifier là một phần giao thức (protocol / 프로토콜). Không tự đổi “vì đầu ra (output / 출력) nhìn giống”.

---

# XML Signature sâu hơn

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **45. tham chiếu (reference / 참조) là trọng tâm của XML Signature** tiếp nhận điểm tựa từ **44. Inclusive và Exclusive Canonicalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **46. ID typing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. tham chiếu (reference / 참조) là trọng tâm của XML Signature

Signature không nhất thiết sign “document đang nhìn thấy”.

Nó sign dữ liệu (data / 데이터) được xác định bởi references, URI resolution và transforms.

Conceptual luồng (flow / 흐름):

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

> **Chuyển mạch:** Trong **XML — Master Supplement**, **46. ID typing** tiếp nhận điểm tựa từ **45. tham chiếu (reference / 참조) là trọng tâm của XML Signature** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **47. Signature Wrapping Defense** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. ID typing

Tham chiếu (reference / 참조) `#order123` phải resolve tới đúng nút (node / 노드).

XML processor/thư viện (library / 라이브러리) phải biết attribute nào là ID.

Nguồn ID ngữ nghĩa (semantics / 의미론) có thể là:

```text
DTD type ID
XSD type
xml:id
manual API registration
library-specific rule
```

Nếu attacker tạo duplicate-looking IDs hoặc ứng dụng (application / 애플리케이션) resolve khác verifier, bảo mật (security / 보안) có thể hỏng.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **47. Signature Wrapping Defense** tiếp nhận điểm tựa từ **46. ID typing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **48. không gian tên (namespace / 네임스페이스) confusion attack** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Signature Wrapping Defense

Giả sử signature verifier nói nút (node / 노드) A hợp lệ.

Nghiệp vụ (business / 비즈니스) mã (code / 코드) không được bỏ nút (node / 노드) A rồi chạy truy vấn (query / 쿼리):

```text
find first <Order>
```

vì attacker có thể đưa một unsigned thứ tự (order / 순서) lên đầu.

Correct mẫu (pattern / 패턴) là verifier trả hoặc bind chính xác (exact / 정확한) signed đối tượng (object / 객체)/nút (node / 노드) cho nghiệp vụ (business / 비즈니스) tầng (layer / 계층).

Đây gọi là **Verified nút (node / 노드) Binding mẫu (pattern / 패턴)**.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **48. không gian tên (namespace / 네임스페이스) confusion attack** tiếp nhận điểm tựa từ **47. Signature Wrapping Defense** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **49. Parser differential** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. không gian tên (namespace / 네임스페이스) confusion attack

Nếu mã (code / 코드) bảo mật (security / 보안) chỉ kiểm tra:

```java
localName.equals("Admin")
```

attacker có thể gửi:

```xml
<evil:Admin xmlns:evil="urn:evil"/>
```

Cục bộ (local / 로컬) name là `Admin`, nhưng vocabulary không gian tên (namespace / 네임스페이스) khác.

Security-sensitive XML processing phải check expanded name, không chỉ cục bộ (local / 로컬) name hoặc prefix.

---

# Parser Differential và tài nguyên (resource / 자원) Limits

> **Chuyển mạch:** Trong **XML — Master Supplement**, **49. Parser differential** tiếp nhận điểm tựa từ **48. không gian tên (namespace / 네임스페이스) confusion attack** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **50. XXE disabled vẫn chưa đủ chống DoS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Parser differential

Không phải mọi XML parser có same defaults.

Một parser có thể enable DTD, parser khác disable. Một XSD engine hỗ trợ (support / 지원) 1.1, engine khác chỉ 1.0. thực thể (entity / 엔터티) limit, không gian tên (namespace / 네임스페이스) hành vi (behavior / 동작) và XInclude defaults cũng có thể khác.

Vì vậy giao thức (protocol / 프로토콜) bảo mật (security / 보안) không nên phụ thuộc undocumented default.

Cấu hình (configuration / 구성) phải tường minh (explicit / 명시적) và tested trên chính xác (exact / 정확한) hiện thực (implementation / 구현)/phiên bản (version / 버전).

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **50. XXE disabled vẫn chưa đủ chống DoS** tiếp nhận điểm tựa từ **49. Parser differential** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **51. DOM bộ nhớ (memory / 메모리) amplification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 50. XXE disabled vẫn chưa đủ chống DoS

Một attacker không cần bên ngoài (external / 외부) thực thể (entity / 엔터티) để gây tài nguyên (resource / 자원) exhaustion.

Họ có thể gửi document sâu hàng trăm nghìn levels, hàng triệu elements, attributes khổng lồ hoặc văn bản (text / 텍스트) nút (node / 노드) rất lớn.

Vì vậy XML ranh giới (boundary / 경계) cần kích thước (size / 크기)/độ sâu (depth / 깊이)/nút (node / 노드) limits độc lập với XXE cấu hình (configuration / 구성).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **51. DOM bộ nhớ (memory / 메모리) amplification** tiếp nhận điểm tựa từ **50. XXE disabled vẫn chưa đủ chống DoS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **52. Pretty-print có thể thay đổi dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 51. DOM bộ nhớ (memory / 메모리) amplification

Raw XML 100 MB có thể thành cây (tree / 트리) tiêu tốn vài trăm MB hoặc hơn.

Reason gồm Java objects, UTF string biểu diễn (representation / 표현), arrays, pointers, attributes và siêu dữ liệu (metadata / 메타데이터).

Nếu dịch vụ (service / 서비스) có 512 MB vùng nhớ động (heap / 힙), “tệp (file / 파일) chỉ 100 MB” vẫn có thể làm dịch vụ (service / 서비스) crash.

Streaming thiết kế (design / 설계) phải dựa trên benchmark và limits thực.

---

# Serialization và Lexical Preservation

> **Chuyển mạch:** Trong **XML — Master Supplement**, **51. DOM bộ nhớ (memory / 메모리) amplification** nêu điều cần giải thích; **52. Pretty-print có thể thay đổi dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **53. Parse → serialize không giữ chính xác (exact / 정확한) nguồn (source / 소스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 52. Pretty-print có thể thay đổi dữ liệu (data / 데이터)

Với bản ghi (record / 레코드) XML:

```xml
<user><name>Alice</name></user>
```

thêm indentation thường không ảnh hưởng nghiệp vụ (business / 비즈니스) fields.

Nhưng với mixed content:

```xml
<p>Hello <b>world</b>!</p>
```

nếu formatter chèn newline/spaces không đúng, văn bản (text / 텍스트) luồng (flow / 흐름) có thể đổi.

Document-centric XML phải được format cẩn thận.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **52. Pretty-print có thể thay đổi dữ liệu (data / 데이터)** nêu điều cần giải thích; **53. Parse → serialize không giữ chính xác (exact / 정확한) nguồn (source / 소스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **54. Prefix có thể đổi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 53. Parse → serialize không giữ chính xác (exact / 정확한) nguồn (source / 소스)

Một serializer không bắt buộc giữ:

```text
single quote vs double quote
original prefix name
attribute order
CDATA boundary
entity reference spelling
empty-element spelling
indentation
```

Nếu bạn cần chính xác (exact / 정확한) lexical preservation, ordinary DOM round-trip không đủ.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **53. Parse → serialize không giữ chính xác (exact / 정확한) nguồn (source / 소스)** nêu điều cần giải thích; **54. Prefix có thể đổi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **55. Attribute thứ tự (order / 순서) không phải nghiệp vụ (business / 비즈니스) thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 54. Prefix có thể đổi

Đầu vào (input / 입력):

```xml
<a:user xmlns:a="urn:user"/>
```

Đầu ra (output / 출력):

```xml
<ns1:user xmlns:ns1="urn:user"/>
```

có thể hoàn toàn equivalent theo không gian tên (namespace / 네임스페이스) ngữ nghĩa (semantics / 의미론).

Bên tiêu thụ (consumer / 소비자) không được depend chính xác (exact / 정확한) prefix string trừ khi một unusual giao thức (protocol / 프로토콜) định nghĩa lexical đặc tả hợp đồng (contract / 계약).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **55. Attribute thứ tự (order / 순서) không phải nghiệp vụ (business / 비즈니스) thứ tự (order / 순서)** tiếp nhận điểm tựa từ **54. Prefix có thể đổi** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **56. Empty element lexical form** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 55. Attribute thứ tự (order / 순서) không phải nghiệp vụ (business / 비즈니스) thứ tự (order / 순서)

Không viết mã (code / 코드) nghĩ “attribute đầu tiên là id, thứ hai là status”.

Attribute names xác định meaning, không phải vị trí.

Canonicalization có thứ tự (ordering / 순서) quy tắc (rule / 규칙) riêng chỉ để tạo deterministic biểu diễn (representation / 표현).

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **56. Empty element lexical form** tiếp nhận điểm tựa từ **55. Attribute thứ tự (order / 순서) không phải nghiệp vụ (business / 비즈니스) thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **57. thực thể (entity / 엔터티) references có thể không được preserve** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 56. Empty element lexical form
Phần này nối mạch bài học với “56. Empty element lexical form”, nêu mục đích, cách vận hành và giới hạn trước khi đi vào ví dụ.

```xml
<a/>
```

và:

```xml
<a></a>
```

thường biểu diễn cùng empty element.

Raw string diff không phải ngữ nghĩa (semantic / 의미적) XML diff.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, sau nội dung của **56. Empty element lexical form**, **57. thực thể (entity / 엔터티) references có thể không được preserve** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **58. CDATA có thể mất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 57. thực thể (entity / 엔터티) references có thể không được preserve

Đầu vào (input / 입력):

```xml
<name>&company;</name>
```

sau parsing có thể thành văn bản (text / 텍스트) `Acme Corporation`.

Serializer sau đó có thể đầu ra (output / 출력) direct văn bản (text / 텍스트) thay vì `&company;`.

Nghiệp vụ (business / 비즈니스) meaning không được phụ thuộc thực thể (entity / 엔터티) lexical choice.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **58. CDATA có thể mất** tiếp nhận điểm tựa từ **57. thực thể (entity / 엔터티) references có thể không được preserve** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **59. ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) vs lexical đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 58. CDATA có thể mất

Đầu vào (input / 입력):

```xml
<code><![CDATA[a < b]]></code>
```

có thể serialize thành:

```xml
<code>a &lt; b</code>
```

mà ngữ nghĩa (semantics / 의미론) character dữ liệu (data / 데이터) không đổi.

Vì vậy không được dùng “có CDATA hay không” làm nghiệp vụ (business / 비즈니스) flag.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **59. ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) vs lexical đặc tả hợp đồng (contract / 계약)** tiếp nhận điểm tựa từ **58. CDATA có thể mất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **60. RELAX NG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 59. ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) vs lexical đặc tả hợp đồng (contract / 계약)

Một XML API nên đặc tả hợp đồng (contract / 계약) trên:

```text
namespace
local name
element/attribute values
types
order
cardinality
schema rules
```

không nên đặc tả hợp đồng (contract / 계약) trên:

```text
prefix spelling
indentation
quote style
CDATA
attribute order
self-closing notation
```

trừ khi giao thức (protocol / 프로토콜) explicitly yêu cầu chuẩn gốc (canonical / 정본) lexical biểu diễn (representation / 표현).

---

# Alternative lược đồ (schema / 스키마) Languages

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **60. RELAX NG** tiếp nhận điểm tựa từ **59. ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약) vs lexical đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **61. Schematron** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 60. RELAX NG

RELAX NG là một lược đồ (schema / 스키마) ngôn ngữ (language / 언어) khác ngoài DTD và XSD.

Nó có XML cú pháp (syntax / 문법) và compact cú pháp (syntax / 문법).

RELAX NG nổi tiếng với grammar mô hình (model / 모델) tương đối elegant, đặc biệt cho document-centric XML và mixed content.

Bạn không nhất thiết phải dùng nó trong Java enterprise dự án (project / 프로젝트), nhưng master XML nên biết XSD không phải lược đồ (schema / 스키마) ngôn ngữ (language / 언어) duy nhất.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **61. Schematron** tiếp nhận điểm tựa từ **60. RELAX NG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **62. Kết hợp XSD và Schematron** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 61. Schematron

Schematron thiên quy tắc (rule / 규칙)/assertion kiểm tra hợp lệ (validation / 검증).

Ví dụ yêu cầu (requirement / 요구사항):

```text
nếu paymentMethod = CARD thì cardNumber phải tồn tại
```

hoặc:

```text
sum(item/amount) phải bằng total
```

Những các ràng buộc (constraints / 제약조건들) cross-tree này đôi khi khó diễn tả tự nhiên bằng XSD 1.0 nhưng phù hợp Schematron.

Schematron thường dùng XPath expressions trong assertions.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **62. Kết hợp XSD và Schematron** tiếp nhận điểm tựa từ **61. Schematron** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **63. Russian Doll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 62. Kết hợp XSD và Schematron

Một kiến trúc (architecture / 아키텍처) rất mạnh là:

```text
XSD
→ kiểm tra structure + datatype

Schematron
→ kiểm tra cross-field/cross-tree semantic constraints

application
→ domain logic + authorization
```

Không bắt một tầng (layer / 계층) làm mọi việc.

---

# XSD thiết kế (design / 설계) Patterns

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **63. Russian Doll** tiếp nhận điểm tựa từ **62. Kết hợp XSD và Schematron** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **64. Venetian Blind** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 63. Russian Doll

Russian Doll style dùng cục bộ (local / 로컬) anonymous types nested trong một gốc (root / 루트)/toàn cục (global / 전역) element.

Ưu điểm là lược đồ (schema / 스키마) self-contained và encapsulated.

Nhược điểm là kiểu (type / 타입) reuse thấp.

Mẫu (pattern / 패턴) phù hợp vocabulary nhỏ, cấu trúc (structure / 구조) ít tái sử dụng.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **64. Venetian Blind** tiếp nhận điểm tựa từ **63. Russian Doll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **65. Salami Slice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 64. Venetian Blind

Venetian Blind dùng toàn cục (global / 전역) named complex types nhưng cục bộ (local / 로컬) element declarations.

Ưu điểm là reusable kiểu (type / 타입) definitions mà vẫn hạn chế số toàn cục (global / 전역) elements.

Đây là mẫu (pattern / 패턴) phổ biến khi lĩnh vực (domain / 도메인) structures được reuse.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **65. Salami Slice** tiếp nhận điểm tựa từ **64. Venetian Blind** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **66. Garden of Eden** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 65. Salami Slice

Salami Slice dùng nhiều toàn cục (global / 전역) element declarations rồi tham chiếu (reference / 참조) chúng.

Ưu điểm là element reuse.

Nhược điểm là toàn cục (global / 전역) symbol không gian (space / 공간) lớn và lược đồ (schema / 스키마) điều hướng (navigation / 내비게이션) phức tạp hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **66. Garden of Eden** tiếp nhận điểm tựa từ **65. Salami Slice** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **67. Contract-first** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 66. Garden of Eden

Garden of Eden đưa cả elements và named types lên toàn cục (global / 전역) phạm vi (scope / 범위).

Ưu điểm là maximum reuse/extensibility.

Nhược điểm là lược đồ (schema / 스키마) có nhiều toàn cục (global / 전역) components và phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phức tạp.

Không có mẫu (pattern / 패턴) “cấp cao (senior / 시니어) nhất”. Chọn theo quản trị (governance / 거버넌스), reuse và versioning requirements.

---

# Contract-first và Code-first

> **Chuyển mạch:** Trong **XML — Master Supplement**, **67. Contract-first** tiếp nhận điểm tựa từ **66. Garden of Eden** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **68. Code-first** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 67. Contract-first

Luồng (flow / 흐름):

```text
design XML vocabulary/XSD
→ review với consumers
→ version/publish
→ generate or map code
```

Ưu điểm lớn nhất là đặc tả hợp đồng (contract / 계약) không phụ thuộc Java hiện thực (implementation / 구현).

Nó phù hợp B2B/enterprise tích hợp (integration / 통합) nơi nhiều ngôn ngữ (language / 언어)/nền tảng (platform / 플랫폼) cùng consume.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **68. Code-first** tiếp nhận điểm tựa từ **67. Contract-first** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **69. ranh giới (boundary / 경계) Parser** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 68. Code-first

Luồng (flow / 흐름):

```text
Java classes
→ framework generates XML/XSD
```

Nhanh cho nội bộ (internal / 내부) dịch vụ (service / 서비스).

Nhưng generated lược đồ (schema / 스키마) dễ phản ánh OO decisions như lớp (class / 클래스) inheritance, wrapper collections hoặc hiện thực (implementation / 구현) naming.

Nếu đặc tả hợp đồng (contract / 계약) tồn tại 10 năm và có nhiều partner, code-first có thể tạo technical debt.

---

# Master thiết kế (design / 설계) Patterns

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **68. Code-first** đã nêu tiêu chí phân biệt, còn **69. ranh giới (boundary / 경계) Parser** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **70. Resolver Gateway** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 69. ranh giới (boundary / 경계) Parser

Thay vì mỗi dịch vụ (service / 서비스) phương thức (method / 메서드) tự tạo parser, nên có một ranh giới (boundary / 경계) thành phần (component / 컴포넌트) chịu trách nhiệm:

```text
size limits
parser hardening
namespace handling
schema validation
error translation
```

Nghiệp vụ (business / 비즈니스) mã (code / 코드) chỉ nhận typed/trusted biểu diễn (representation / 표현).

Điều này tránh bảo mật (security / 보안) cấu hình (config / 설정) drift.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **69. ranh giới (boundary / 경계) Parser** đã nêu tiêu chí phân biệt, còn **70. Resolver Gateway** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **71. lược đồ (schema / 스키마) Registry** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 70. Resolver Gateway

Mọi bên ngoài (external / 외부) XML tài nguyên (resource / 자원) lookup đi qua resolver chung.

Resolver thực hiện allowlist, XML danh mục (catalog / 카탈로그), caching và khả năng quan sát (observability / 관측 가능성).

Không để XSLT/XSD/parser tự gọi internet ở nhiều nơi.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **71. lược đồ (schema / 스키마) Registry** tiếp nhận điểm tựa từ **70. Resolver Gateway** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **72. chuẩn gốc (canonical / 정본) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 71. lược đồ (schema / 스키마) Registry

Schemas nên có quyền sở hữu (ownership / 소유권), phiên bản (version / 버전), checksum, tính tương thích (compatibility / 호환성) status và bản phát hành (release / 릴리스) vòng đời (lifecycle / 생명주기).

Nếu một dùng chung (common / 공통) lược đồ (schema / 스키마) bị thay âm thầm, nhiều tích hợp (integration / 통합) có thể vỡ.

Lược đồ (schema / 스키마) phải được quản lý như API sản phẩm tạo ra (artifact / 산출물).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, sau nội dung của **71. lược đồ (schema / 스키마) Registry**, **72. chuẩn gốc (canonical / 정본) mô hình (model / 모델)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **73. Transformation chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 72. chuẩn gốc (canonical / 정본) mô hình (model / 모델)

Vendor-specific XML được transform thành nội bộ (internal / 내부) mô hình (model / 모델) ổn định.

Điều này ngăn bên ngoài (external / 외부) không gian tên (namespace / 네임스페이스)/kiểu (type / 타입) quirks leak vào lĩnh vực (domain / 도메인).

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **72. chuẩn gốc (canonical / 정본) mô hình (model / 모델)** xác định đầu vào; **73. Transformation chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **74. Verified nút (node / 노드) Binding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 73. Transformation chuỗi xử lý (pipeline / 파이프라인)

Thay giant XSLT xử lý mọi thứ, có thể chia:

```text
sanitize/normalize
→ vocabulary migration
→ business enrichment
→ output rendering
```

Mỗi stage nhỏ và testable.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **73. Transformation chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **74. Verified nút (node / 노드) Binding** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **75. Full gỡ lỗi (debug / 디버그) luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 74. Verified nút (node / 노드) Binding

Khi dùng XML Signature, signature xác minh (verification / 확인) tầng (layer / 계층) phải trả chính xác (exact / 정확한) verified nút (node / 노드)/dữ liệu (data / 데이터) cho nghiệp vụ (business / 비즈니스) tầng (layer / 계층).

Nghiệp vụ (business / 비즈니스) mã (code / 코드) không tự truy vấn (query / 쿼리) lại toàn document.

Đây là mẫu (pattern / 패턴) bảo mật (security / 보안) cực quan trọng.

---

# Gỡ lỗi (debug / 디버그) và rà soát (review / 검토)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **74. Verified nút (node / 노드) Binding** xác định đầu vào; **75. Full gỡ lỗi (debug / 디버그) luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **76. Master bảo mật (security / 보안) rà soát (review / 검토)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 75. Full gỡ lỗi (debug / 디버그) luồng (flow / 흐름)

Khi XML tích hợp (integration / 통합) lỗi, đừng sửa ngẫu nhiên prefix hoặc XPath.

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

Đi theo tầng (layer / 계층) giúp gỡ lỗi (debug / 디버그) nhanh hơn nhiều.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **75. Full gỡ lỗi (debug / 디버그) luồng (flow / 흐름)** xác định đầu vào; **76. Master bảo mật (security / 보안) rà soát (review / 검토)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **77. Master hiệu năng (performance / 성능) rà soát (review / 검토)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 76. Master bảo mật (security / 보안) rà soát (review / 검토)

Một XML endpoint nhận untrusted đầu vào (input / 입력) phải được rà soát (review / 검토) cả đầu vào (input / 입력) kích thước (size / 크기), nesting độ sâu (depth / 깊이), DTD, bên ngoài (external / 외부) entities, parameter entities, bên ngoài (external / 외부) subset, XInclude, lược đồ (schema / 스키마) resolution, XSLT resolution, XPath construction, namespace-aware matching, signature tham chiếu (reference / 참조) binding và sensitive logging.

Nếu endpoint chỉ “disable XXE” nhưng không có đầu vào (input / 입력) kích thước (size / 크기) limit, nó vẫn có thể bị bộ nhớ (memory / 메모리) DoS.

Nếu signature verify đúng nhưng nghiệp vụ (business / 비즈니스) mã (code / 코드) đọc wrong nút (node / 노드), nó vẫn có thể vulnerable.

Bảo mật (security / 보안) XML là chuỗi xử lý (pipeline / 파이프라인) thuộc tính (property / 속성), không phải một parser flag.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **77. Master hiệu năng (performance / 성능) rà soát (review / 검토)** tiếp nhận điểm tựa từ **76. Master bảo mật (security / 보안) rà soát (review / 검토)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **78. Toàn bộ XML processing luồng (flow / 흐름)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 77. Master hiệu năng (performance / 성능) rà soát (review / 검토)

Hãy hỏi liệu DOM có thật sự cần không, đầu vào (input / 입력) maximum kích thước (size / 크기) là bao nhiêu, lược đồ (schema / 스키마)/XSLT có compile lại mỗi yêu cầu (request / 요청) không, resolver có truy cập mạng (network access / 네트워크 접근) không, XPath có broad `//` trên cây (tree / 트리) lớn không, chuỗi xử lý (pipeline / 파이프라인) có parse-serialize nhiều vòng không, và bộ nhớ (memory / 메모리) amplification đã được benchmark chưa.

Một hiệu năng (performance / 성능) bug XML thường đến từ kiến trúc (architecture / 아키텍처) hơn là một tag cụ thể.

---

# Full mô hình tư duy (mental model / 사고 모델)

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Master Supplement**, **77. Master hiệu năng (performance / 성능) rà soát (review / 검토)** xác định đầu vào; **78. Toàn bộ XML processing luồng (flow / 흐름)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **79. Khi nào có thể nói đã master XML?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 78. Toàn bộ XML processing luồng (flow / 흐름)

Đây là mô hình tư duy (mental model / 사고 모델) cuối cùng bạn nên giữ:

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

Mỗi arrow là một nơi có thể có bug, hiệu năng (performance / 성능) chi phí (cost / 비용) hoặc bảo mật (security / 보안) implication.

---

> **Chuyển mạch:** Trong **XML — Master Supplement**, **78. Toàn bộ XML processing luồng (flow / 흐름)** xác định đầu vào; **79. Khi nào có thể nói đã master XML?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **80. Cách học bộ bốn tệp (file / 파일)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 79. Khi nào có thể nói đã master XML?

Bạn không cần thuộc từng môi trường vận hành (production / 운영 환경) quy tắc (rule / 규칙) trong W3C specification.

Bạn có thể coi mình có XML mastery foundation khi nhìn một hệ thống XML lạ và biết hỏi đúng câu: XML phiên bản (version / 버전) nào, encoding nào, không gian tên (namespace / 네임스페이스) nào, lược đồ (schema / 스키마) phiên bản (version / 버전) nào, parser mô hình (model / 모델) nào, bên ngoài (external / 외부) resolution có được kiểm soát không, XPath/XSLT phiên bản (version / 버전) nào, đặc tả hợp đồng (contract / 계약) evolve thế nào, nil-vs-missing ngữ nghĩa (semantics / 의미론) ra sao, document có lớn tới mức cần streaming không, và giao thức (protocol / 프로토콜) có canonicalization/signature yêu cầu (requirement / 요구사항) không.

Đó là sự khác biệt giữa “biết viết XML” và “hiểu XML nền tảng (platform / 플랫폼)”.

---

> **Chuyển mạch:** Ở chặng này của **XML — Master Supplement**, **80. Cách học bộ bốn tệp (file / 파일)** tiếp nhận điểm tựa từ **79. Khi nào có thể nói đã master XML?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 80. Cách học bộ bốn tệp (file / 파일)

Phần Beginner nên đọc từ đầu đến cuối và tự gõ XML examples. Phần Intermediate cần thực hành không gian tên (namespace / 네임스페이스)/XPath/XSD vì chỉ đọc sẽ rất dễ quên. Phần cấp cao (senior / 시니어) nên học song song với Java XML APIs hoặc một tích hợp (integration / 통합) trường hợp (case / 사례) thực tế. Phần Master Supplement không cần học thuộc trong một lần; hãy dùng nó để xây mô hình tư duy (mental model / 사고 모델) và quay lại khi gặp lược đồ (schema / 스키마), signature, parser hoặc transformation trường hợp biên (edge case / 경계 사례).

Sau khi hoàn thành cả bốn phần, bước tiếp theo hiệu quả nhất không phải đọc thêm hàng trăm trang lý thuyết mà là tự làm một dự án (project / 프로젝트) nhỏ có không gian tên (namespace / 네임스페이스), XSD kiểm tra hợp lệ (validation / 검증), XPath truy vấn (query / 쿼리), StAX large-file parsing, XSLT transformation và secure parser cấu hình (configuration / 구성). Khi bạn tự gỡ lỗi (debug / 디버그) những tương tác (interaction / 상호작용) đó, kiến thức XML sẽ trở thành kỹ năng thực tế thay vì chỉ là kiến thức đọc.

> **Bàn giao:** Sau **80. Cách học bộ bốn tệp (file / 파일)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
