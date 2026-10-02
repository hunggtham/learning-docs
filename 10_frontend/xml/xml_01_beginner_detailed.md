# XML — Beginner

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **XML — Beginner**. Route đi từ document/tree model → syntax, elements/attributes và encoding → well-formedness, parser behavior và schema boundary → config/enterprise examples → chuẩn bị cho namespaces và XPath.

## Học XML từ con số 0: cú pháp, cấu trúc dữ liệu và cách parser thực sự hiểu tài liệu XML

Tài liệu này được viết cho người chưa có nền tảng XML. Mục tiêu không phải là giúp bạn “nhớ vài tag”, mà là giúp bạn hiểu XML đang giải quyết vấn đề gì, XML document được tổ chức ra sao, vì sao cú pháp của XML chặt chẽ hơn HTML, và một XML parser thực sự nhìn dữ liệu như thế nào. Nếu đọc hết phần này và tự làm các ví dụ đi kèm, bạn phải có thể tự viết một tài liệu XML đúng cú pháp, đọc được các tệp (file / 파일) cấu hình XML trong Java hoặc hệ thống enterprise, phân biệt được lỗi cú pháp với lỗi lược đồ (schema / 스키마), và hiểu vì sao XML vẫn tồn tại rất nhiều trong các hệ thống lớn dù JSON đã rất phổ biến.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **Học XML từ con số 0: cú pháp, cấu trúc dữ liệu và cách parser thực sự hiểu tài liệu XML** nêu điều cần giải thích; **1. XML là gì và vì sao nó tồn tại?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **2. XML document thực chất là một cây dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1. XML là gì và vì sao nó tồn tại?

XML là viết tắt của **Extensible Markup ngôn ngữ (language / 언어)**, tức là ngôn ngữ đánh dấu có khả năng mở rộng. Từ “markup” nghĩa là dữ liệu được bao quanh bởi các dấu hiệu cấu trúc như `<user>`, `<name>`, `<price>`. Từ “extensible” nghĩa là XML không ép bạn phải dùng một tập tag cố định. Bạn có thể tự định nghĩa vocabulary của riêng mình, miễn là toàn bộ tài liệu tuân theo quy tắc cú pháp XML.

Ví dụ sau là một XML document rất đơn giản:

```xml
<user>
  <name>Alice</name>
  <age>27</age>
</user>
```

XML chỉ biết đây là một cây có element `user`, bên trong có `name` và `age`. XML không biết `age` là tuổi con người, không biết giá trị `27` là số nguyên, và cũng không biết `name` có bắt buộc hay không. Những ý nghĩa đó phải được định nghĩa bởi ứng dụng (application / 애플리케이션), lược đồ (schema / 스키마), giao thức (protocol / 프로토콜) hoặc nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) ở tầng khác.

Điểm này rất quan trọng. Khi học HTML, bạn có thể học rằng `<a>` là hyperlink, `<button>` là button, `<table>` là bảng. Với XML thì không có một ý nghĩa chuẩn như vậy cho `<user>` hay `<order>`. XML chỉ cung cấp **cú pháp chung để biểu diễn dữ liệu có cấu trúc**. Chính Maven định nghĩa ý nghĩa của `<groupId>`, SOAP định nghĩa ý nghĩa của `<Envelope>`, Spring định nghĩa ý nghĩa của các tag cấu hình cũ, và Android định nghĩa ý nghĩa của các tag XML trong bố cục (layout / 레이아웃).

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **1. XML là gì và vì sao nó tồn tại?** nêu điều cần giải thích; **2. XML document thực chất là một cây dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. gốc (root / 루트) element là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. XML document thực chất là một cây dữ liệu

Một XML document nên được hình dung như một cây, không nên hình dung như một chuỗi văn bản (text / 텍스트) có nhiều dấu `<` và `>`. Xét ví dụ sau:

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

Một XML parser không chỉ “tìm văn bản (text / 텍스트) giữa hai tag”. Nó có thể tạo ra các đối tượng hoặc sự kiện tương ứng với document, element, attribute, văn bản (text / 텍스트) nút (node / 노드), comment và processing instruction. Khi sau này bạn dùng DOM, SAX, StAX, XPath hay XSLT, tất cả đều dựa trên tư duy cây hoặc stream được sinh ra từ XML này.

Đây cũng là lý do tại sao việc parse XML bằng `split("<name>")` hay regex là sai về mặt kiến trúc. Một tệp (file / 파일) XML có thể có không gian tên (namespace / 네임스페이스), CDATA, thực thể (entity / 엔터티), comment, encoding khác nhau và nested element rất sâu. String slicing chỉ hoạt động với ví dụ đồ chơi, không phải với XML thực tế.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **2. XML document thực chất là một cây dữ liệu** nêu điều cần giải thích; **3. gốc (root / 루트) element là gì?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. Element là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. gốc (root / 루트) element là gì?

Một XML document đúng cú pháp phải có đúng **một document element**, thường được gọi đơn giản là gốc (root / 루트) element. Ví dụ này hợp lệ:

```xml
<users>
  <user>Alice</user>
  <user>Bob</user>
</users>
```

Ở đây `users` là gốc (root / 루트) element.

Ví dụ sau không hợp lệ:

```xml
<user>Alice</user>
<user>Bob</user>
```

Lý do là tài liệu có hai top-level elements. XML parser không thể coi cả hai cùng là document element.

Điều này không có nghĩa bên ngoài gốc (root / 루트) hoàn toàn không được có gì. Một tài liệu vẫn có thể có XML declaration, comment, processing instruction hoặc DOCTYPE ở vị trí phù hợp. Nhưng về element cây (tree / 트리) thì chỉ có một element gốc.

---

> **Chuyển mạch:** Root element đặt giới hạn cho document tree; element tiếp theo mô tả node có content và attributes ra sao. Empty/self-closing syntax kiểm tra trường hợp node không có content.

## 4. Element là gì?

Element là thành phần cấu trúc chính của XML. Ví dụ:

```xml
<name>Alice</name>
```

Element này có start tag `<name>`, content là văn bản (text / 텍스트) `Alice`, và end tag `</name>`.

Element cũng có thể chứa các element khác:

```xml
<user>
  <name>Alice</name>
  <email>alice@example.com</email>
</user>
```

Khi đọc XML, bạn nên nghĩ rằng mỗi element là một nút (node / 노드) có tên và có thể có children. Children có thể là element khác, văn bản (text / 텍스트) hoặc các nút (node / 노드) đặc biệt khác.

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

> **Chuyển mạch:** Element có thể chứa content hoặc rỗng; empty-element syntax quy định serialization, còn case sensitivity tiếp theo ảnh hưởng name matching.

## 5. Empty element và self-closing cú pháp (syntax / 문법)

Nếu một element không có content, bạn có thể viết dạng đầy đủ:

```xml
<active></active>
```

hoặc viết dạng rút gọn:

```xml
<active/>
```

Trong XML, đây là empty-element cú pháp (syntax / 문법) thực sự. Nó không phải chỉ là “cách formatter viết cho đẹp”.

Điểm này khác với HTML. Trong HTML, các void element như `<img>` hoặc `<br>` được quyết định bởi HTML parser và HTML specification. Việc bạn viết `<br />` trong một trang HTML thông thường không biến nó thành XML. XML và HTML có hai parsing mô hình (model / 모델) khác nhau.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **6. XML phân biệt chữ hoa chữ thường** tiếp nhận điểm tựa từ **5. Empty element và self-closing cú pháp (syntax / 문법)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Proper nesting: element phải đóng đúng thứ tự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **XML — Beginner**, **7. Proper nesting: element phải đóng đúng thứ tự** tiếp nhận điểm tựa từ **6. XML phân biệt chữ hoa chữ thường** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Attribute là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

HTML trình duyệt (browser / 브라우저) có lỗi (error / 오류) khôi phục (recovery / 복구) rất mạnh và thường cố “sửa” markup sai để vẫn kết xuất (render / 렌더링) được. XML thì khác. XML parser được thiết kế để nghiêm ngặt hơn. Nếu tài liệu không well-formed, parser phải báo fatal lỗi (error / 오류) thay vì tự đoán cấu trúc theo kiểu trình duyệt (browser / 브라우저) HTML.

Điều này khiến XML thích hợp với các giao thức (protocol / 프로토콜) hoặc tệp (file / 파일) cấu hình nơi tính chính xác quan trọng hơn khả năng “kết xuất (render / 렌더링) được dù sai”.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **8. Attribute là gì?** tiếp nhận điểm tựa từ **7. Proper nesting: element phải đóng đúng thứ tự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Khi nào nên dùng element, khi nào nên dùng attribute?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Attribute là gì?

Attribute gắn siêu dữ liệu (metadata / 메타데이터) hoặc giá trị bổ sung cho element.

```xml
<employee id="E001" active="true">
  Alice
</employee>
```

Ở đây `id` và `active` là attributes của element `employee`.

Trong XML, attribute giá trị (value / 값) phải được đặt trong dấu nháy. Cả hai cách sau đều hợp lệ:

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **9. Khi nào nên dùng element, khi nào nên dùng attribute?** tiếp nhận điểm tựa từ **8. Attribute là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. văn bản (text / 텍스트) content thực chất vẫn là character dữ liệu (data / 데이터)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Trong thực tế, attribute thường phù hợp với siêu dữ liệu (metadata / 메타데이터) ngắn, identifier, flag, qualifier hoặc các giá trị mô tả element. Element thường phù hợp với nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터), nested cấu trúc (structure / 구조), repeating values và dữ liệu có khả năng mở rộng.

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

Cấp cao (senior / 시니어) XML thiết kế (design / 설계) không dựa trên một luật “attribute luôn tốt hơn element” hay ngược lại. Thiết kế phụ thuộc lĩnh vực (domain / 도메인), lược đồ (schema / 스키마), khả năng versioning và cách dữ liệu được truy vấn (query / 쿼리)/transform.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **9. Khi nào nên dùng element, khi nào nên dùng attribute?** nêu điều cần giải thích; **10. văn bản (text / 텍스트) content thực chất vẫn là character dữ liệu (data / 데이터)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Escaping: vì sao một số ký tự không được viết trực tiếp?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. văn bản (text / 텍스트) content thực chất vẫn là character dữ liệu (data / 데이터)

Xét:

```xml
<age>27</age>
```

Ở mức XML cốt lõi (core / 핵심), `27` chỉ là văn bản (text / 텍스트). XML parser không tự biết đó là integer.

Tương tự:

```xml
<active>true</active>
```

không tự động trở thành boolean.

Kiểu dữ liệu có thể được gán ở tầng XML lược đồ (schema / 스키마) hoặc ứng dụng (application / 애플리케이션). Điều này rất quan trọng khi bạn làm Java binding hoặc validate XML. Nếu không có lược đồ (schema / 스키마) hoặc ánh xạ (mapping / 매핑) quy tắc (rule / 규칙), parser chỉ trả về character dữ liệu (data / 데이터).

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **10. văn bản (text / 텍스트) content thực chất vẫn là character dữ liệu (data / 데이터)** nêu điều cần giải thích; **11. Escaping: vì sao một số ký tự không được viết trực tiếp?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. Numeric character references** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Escaping: vì sao một số ký tự không được viết trực tiếp?

Ký tự `<` được XML dùng để bắt đầu markup. Vì vậy nếu bạn muốn lưu nội dung văn bản (text / 텍스트) `5 < 10`, bạn không thể viết trực tiếp:

```xml
<value>5 < 10</value>
```

Bạn phải viết:

```xml
<value>5 &lt; 10</value>
```

Tương tự, dấu `&` bắt đầu thực thể (entity / 엔터티) tham chiếu (reference / 참조) nên phải viết thành `&amp;` khi bạn thực sự muốn ký tự `&`.

XML định nghĩa sẵn năm thực thể (entity / 엔터티) quan trọng:

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

Bạn không cần encode mọi Unicode character thành thực thể (entity / 엔터티). Nếu tệp (file / 파일) là UTF‑8, bạn có thể viết tiếng Việt, tiếng Hàn, tiếng Nhật trực tiếp miễn ký tự đó hợp lệ theo XML phiên bản (version / 버전).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, sau nội dung của **11. Escaping: vì sao một số ký tự không được viết trực tiếp?**, **12. Numeric character references** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **13. XML declaration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Numeric character references

Ngoài named thực thể (entity / 엔터티), XML còn cho phép numeric character tham chiếu (reference / 참조).

Decimal:

```xml
&#169;
```

Hexadecimal:

```xml
&#x00A9;
```

Cả hai biểu diễn ký tự ©.

Numeric tham chiếu (reference / 참조) hữu ích khi cần biểu diễn ký tự theo mã (code / 코드) điểm (point / 지점) hoặc trong một số toolchain đặc biệt, nhưng trong UTF‑8 XML hiện đại thường không cần lạm dụng.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **13. XML declaration** tiếp nhận điểm tựa từ **12. Numeric character references** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. XML declaration có bắt buộc không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. XML declaration

Bạn thường thấy đầu tệp (file / 파일):

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

`version="1.0"` cho biết XML phiên bản (version / 버전). Trong thực tế XML 1.0 là lựa chọn phổ biến nhất.

`encoding="UTF-8"` mô tả encoding của bytes trong tệp (file / 파일).

Một điểm rất quan trọng là declaration không “chuyển đổi encoding”. Nếu tệp (file / 파일) thực tế được lưu bằng một encoding khác nhưng declaration ghi UTF‑8, parser có thể decode sai hoặc báo lỗi. Vì vậy encoding declaration phải phản ánh đúng bytes thực tế.

Trong hệ thống mới, UTF‑8 gần như luôn là lựa chọn tốt nhất trừ khi giao thức (protocol / 프로토콜) hoặc hệ thống legacy yêu cầu khác.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **14. XML declaration có bắt buộc không?** tiếp nhận điểm tựa từ **13. XML declaration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. BOM là gì và có cần không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. XML declaration có bắt buộc không?

Không phải lúc nào XML declaration cũng bắt buộc. Ví dụ sau vẫn có thể là XML hợp lệ trong ngữ cảnh (context / 맥락) UTF‑8:

```xml
<user>
  <name>Alice</name>
</user>
```

Tuy nhiên trong tệp (file / 파일) cấu hình, tích hợp (integration / 통합) tệp (file / 파일) hoặc tài liệu cần trao đổi qua nhiều hệ thống, việc ghi rõ:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

giúp giảm ambiguity và làm intent rõ hơn.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **15. BOM là gì và có cần không?** tiếp nhận điểm tựa từ **14. XML declaration có bắt buộc không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Comment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. BOM là gì và có cần không?

BOM là Byte thứ tự (order / 순서) Mark. Với UTF‑16, BOM từng rất quan trọng để xác định byte thứ tự (order / 순서). Với UTF‑8, BOM không cần thiết.

XML processor chuẩn có rules xử lý BOM, nhưng một số toolchain hoặc hệ thống dựng (build system / 빌드 시스템) có thể có hành vi (behavior / 동작) riêng. Trong nhiều dự án hiện đại, `UTF‑8 without BOM` là lựa chọn đơn giản và ít rắc rối nhất, trừ khi hệ thống cụ thể yêu cầu BOM.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **16. Comment** tiếp nhận điểm tựa từ **15. BOM là gì và có cần không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. CDATA section** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Comment

Comment XML có dạng:

```xml
<!-- This is a comment -->
```

Comment không phải nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터). Parser có thể expose comment nút (node / 노드) hoặc bỏ qua tùy API/cấu hình (configuration / 구성).

Một lỗi tư duy thường gặp là để secret trong comment vì “không hiển thị”. Comment vẫn nằm trong tệp (file / 파일) và vẫn có thể được đọc bằng văn bản (text / 텍스트) editor, log, gói (package / 패키지) hoặc mạng (network / 네트워크) capture. Không bao giờ dùng XML comment để chứa password, API key hoặc đơn vị từ (token / 토큰).

Ngoài ra XML comment có restrictions riêng về chuỗi `--`, vì vậy không nên dùng comment như nơi lưu arbitrary văn bản (text / 텍스트).

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **17. CDATA section** tiếp nhận điểm tựa từ **16. Comment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Vì sao ]]> đặc biệt trong CDATA?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. CDATA section

CDATA giúp viết một đoạn character dữ liệu (data / 데이터) chứa nhiều `<` hoặc `&` mà không phải escape từng ký tự.

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

Điểm quan trọng là CDATA không tạo một loại dữ liệu mới. Trong nhiều mô hình dữ liệu (data model / 데이터 모델), phần bên trong CDATA vẫn trở thành character dữ liệu (data / 데이터) giống như khi bạn viết:

```xml
<text>5 &lt; 10</text>
```

so với:

```xml
<text><![CDATA[5 < 10]]></text>
```

Ứng dụng (application / 애플리케이션) thường nhận nội dung lô-gic (logic / 논리) là `5 < 10`.

CDATA cũng không phải bảo mật (security / 보안) tính năng (feature / 기능). Nó chỉ là một cách lexical để viết văn bản (text / 텍스트).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **18. Vì sao ]]> đặc biệt trong CDATA?** tiếp nhận điểm tựa từ **17. CDATA section** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Processing Instruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Vì sao `]]>` đặc biệt trong CDATA?

Chuỗi:

```text
]]>
```

là delimiter kết thúc CDATA section. Vì vậy bạn không thể chứa nguyên chuỗi (sequence / 시퀀스) này bên trong một CDATA section mà không split hoặc serialize lại.

Nếu bạn dùng XML serializer đúng chuẩn, serializer sẽ xử lý chuyện này tốt hơn việc tự nối string.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **18. Vì sao ]]> đặc biệt trong CDATA?** xác định đầu vào; **19. Processing Instruction** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. Whitespace trong XML có thực sự tồn tại không?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Processing Instruction

Processing instruction có cú pháp (syntax / 문법):

```xml
<?target data?>
```

Ví dụ cổ điển:

```xml
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
```

PI dùng để truyền instruction cho processor hoặc ứng dụng (application / 애플리케이션). Nó không phải nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터) thông thường.

XML declaration nhìn giống PI nhưng có grammar và vị trí đặc biệt. Không nên coi `<?xml ...?>` đơn giản là một PI tên `xml`.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **19. Processing Instruction** xác định đầu vào; **20. Whitespace trong XML có thực sự tồn tại không?** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **21. xml:space** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Whitespace trong XML có thực sự tồn tại không?

Có. Ví dụ:

```xml
<user>
  <name>Alice</name>
  <age>27</age>
</user>
```

Giữa các child element có newline và spaces dùng để indent. Tùy parser và mô hình dữ liệu (data model / 데이터 모델), các khoảng trắng đó có thể xuất hiện dưới dạng văn bản (text / 텍스트) nút (node / 노드).

Điều này dẫn tới một bug kinh điển khi dùng DOM: nhà phát triển (developer / 개발자) nghĩ `childNodes` chỉ chứa element, nhưng thực tế có thể có cả whitespace văn bản (text / 텍스트) nodes.

Vì vậy khi bạn muốn “lấy child elements”, hãy dùng API chọn element thay vì giả định mọi child nút (node / 노드) đều là element.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **21. xml:space** tiếp nhận điểm tựa từ **20. Whitespace trong XML có thực sự tồn tại không?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. xml:lang** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

`preserve` nói rằng whitespace trong subtree có ý nghĩa và nên được giữ theo XML processing expectations. Điều này đặc biệt quan trọng với document-centric XML, mã (code / 코드) snippets hoặc văn bản (text / 텍스트) formatting.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **22. xml:lang** tiếp nhận điểm tựa từ **21. xml:space** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. xml:base** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. `xml:lang`

`xml:lang` khai báo ngôn ngữ của nội dung.

```xml
<message xml:lang="ko">
  안녕하세요
</message>
```

Nó hữu ích với document processing, khả năng tiếp cận (accessibility / 접근성), transformation hoặc hệ thống đa ngôn ngữ.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **23. xml:base** tiếp nhận điểm tựa từ **22. xml:lang** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. xml:id** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. `xml:base`

`xml:base` đặt cơ sở (base / 기반) URI cho relative URIs trong subtree.

```xml
<catalog xml:base="https://example.com/assets/">
  <image href="a.png"/>
</catalog>
```

Ứng dụng (application / 애플리케이션) có thể resolve `a.png` thành URL tuyệt đối dựa trên cơ sở (base / 기반) URI này.

Ở mức cấp cao (senior / 시니어), cơ sở (base / 기반) URI còn ảnh hưởng XSLT, URI resolution và bảo mật (security / 보안), vì một relative đường dẫn (path / 경로) cuối cùng có thể trỏ tới bên ngoài (external / 외부) tài nguyên (resource / 자원).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **24. xml:id** tiếp nhận điểm tựa từ **23. xml:base** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Well-formed XML là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. `xml:id`

`xml:id` cung cấp standardized ID ngữ nghĩa (semantics / 의미론) trong XML ecosystem:

```xml
<section xml:id="intro">
  ...
</section>
```

Điều này khác với việc bạn tự đặt:

```xml
<section id="intro">
```

Vì một attribute có tên `id` không tự động có ID kiểu (type / 타입) ở mọi XML processing ngữ cảnh (context / 맥락). ID ngữ nghĩa (semantics / 의미론) có thể đến từ DTD, XSD, `xml:id` hoặc API cấu hình (configuration / 구성).

---

> **Chuyển mạch:** Trong **XML — Beginner**, **25. Well-formed XML là gì?** tiếp nhận điểm tựa từ **24. xml:id** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Valid XML khác well-formed như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Well-formed XML là gì?

“Well-formed” nghĩa là tài liệu tuân toàn bộ cú pháp cơ bản của XML.

Những điều beginner phải nhớ gồm có một gốc (root / 루트) element, tag phải đóng đúng thứ tự, tên phân biệt hoa thường, attribute giá trị (value / 값) phải có quote, không có duplicate attribute, ký tự đặc biệt phải escape đúng, và document chỉ chứa các ký tự hợp lệ theo XML phiên bản (version / 버전).

Ví dụ sau không well-formed:

```xml
<user>
  <name>Alice</user>
</name>
```

XML parser phải báo fatal lỗi (error / 오류).

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **26. Valid XML khác well-formed như thế nào?** tiếp nhận điểm tựa từ **25. Well-formed XML là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. XML Names có quy tắc riêng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Valid XML khác well-formed như thế nào?

Một XML document có thể well-formed nhưng không valid.

Ví dụ:

```xml
<user>
  <banana>123</banana>
</user>
```

Tài liệu này có thể hoàn toàn đúng cú pháp XML. Nhưng nếu lược đồ (schema / 스키마) quy định rằng `user` chỉ được chứa `name` và `email`, thì nó invalid theo lược đồ (schema / 스키마).

Vì vậy hãy nhớ:

```text
well-formed = đúng cú pháp XML
valid       = đúng thêm grammar/schema áp dụng cho vocabulary đó
```

Mọi valid XML phải well-formed, nhưng well-formed XML chưa chắc valid.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **27. XML Names có quy tắc riêng** tiếp nhận điểm tựa từ **26. Valid XML khác well-formed như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Mixed content** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. XML Names có quy tắc riêng

Tên element hoặc attribute không phải một chuỗi tùy ý. XML có grammar dành cho Name và QName.

Trong thực tế bạn thường gặp các tên như:

```xml
<user>
<user-name>
<_internal>
<ns:user>
```

Nhưng không nên tự viết một regex ASCII đơn giản rồi nghĩ đã validate được đầy đủ XML Name. XML hỗ trợ Unicode name characters rộng hơn nhiều. Parser hoặc lược đồ (schema / 스키마) thư viện (library / 라이브러리) nên đảm nhiệm phần này.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **28. Mixed content** tiếp nhận điểm tựa từ **27. XML Names có quy tắc riêng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Data-centric XML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Mixed content

Mixed content là khi văn bản (text / 텍스트) và child elements xen kẽ nhau.

```xml
<p>
  XML is <em>extensible</em> and strict.
</p>
```

Đây là mẫu (pattern / 패턴) rất quan trọng trong publishing, books, manuals và các document format.

Trong mixed content, whitespace và văn bản (text / 텍스트) nút (node / 노드) thứ tự (order / 순서) có ý nghĩa lớn hơn nhiều so với data-centric XML. Nếu bạn tùy tiện pretty-print hoặc trim văn bản (text / 텍스트), bạn có thể làm thay đổi nội dung.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **29. Data-centric XML** tiếp nhận điểm tựa từ **28. Mixed content** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Document-centric XML** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Data-centric XML

Data-centric XML giống đối tượng (object / 객체)/bản ghi (record / 레코드):

```xml
<order>
  <id>123</id>
  <total>99.50</total>
</order>
```

Mỗi child element gần giống một trường dữ liệu (field / 필드). Loại XML này thường dễ map sang Java đối tượng (object / 객체) hoặc cơ sở dữ liệu (database / 데이터베이스) row.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **30. Document-centric XML** tiếp nhận điểm tựa từ **29. Data-centric XML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. XML khác HTML như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Ở đây văn bản (text / 텍스트) luồng (flow / 흐름) và mixed content quan trọng.

Điều này ảnh hưởng cách bạn thiết kế lược đồ (schema / 스키마), XPath, XSLT và parser. Một serializer phù hợp với record-like XML chưa chắc xử lý document XML tốt nếu nó vô tình normalize whitespace hoặc reorder content.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **31. XML khác HTML như thế nào?** tiếp nhận điểm tựa từ **30. Document-centric XML** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. XHTML là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. XML khác HTML như thế nào?

XML và HTML có cú pháp (syntax / 문법) bề ngoài giống nhau, nhưng mục tiêu và parsing mô hình (model / 모델) khác.

XML strict hơn: case-sensitive, proper nesting bắt buộc, attribute giá trị (value / 값) phải quote, self-closing cú pháp (syntax / 문법) có nghĩa thực sự, và parser không có HTML-style lỗi (error / 오류) khôi phục (recovery / 복구).

HTML có vocabulary và ngữ nghĩa (semantics / 의미론) do HTML tiêu chuẩn (standard / 표준) định nghĩa. `<button>` tự có hành vi (behavior / 동작), `<a>` tự có điều hướng (navigation / 내비게이션) ngữ nghĩa (semantics / 의미론). XML thì tag chỉ có meaning khi vocabulary/ứng dụng (application / 애플리케이션) định nghĩa.

Đây là lý do không nên lấy kinh nghiệm HTML rồi suy thẳng sang XML.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **32. XHTML là gì?** tiếp nhận điểm tựa từ **31. XML khác HTML như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. XML khác JSON như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. XHTML là gì?

XHTML là HTML vocabulary được biểu diễn theo XML cú pháp (syntax / 문법)/tiến trình (process / 프로세스) mô hình (model / 모델) trong các ngữ cảnh (context / 맥락) tương ứng.

Ví dụ:

```xml
<html xmlns="http://www.w3.org/1999/xhtml">
  <body>
    <br/>
  </body>
</html>
```

Một tệp (file / 파일) HTML thông thường có `<br />` vẫn có thể đang được parse bằng HTML parser nếu media kiểu (type / 타입) là `text/html`. Dấu `/` không tự chuyển parsing chế độ (mode / 모드).

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **33. XML khác JSON như thế nào?** tiếp nhận điểm tựa từ **32. XHTML là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Ví dụ thực tế: Maven pom.xml** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. XML khác JSON như thế nào?

JSON có mô hình đối tượng (object / 객체), array, number, boolean, null và string rất phù hợp với API hiện đại. XML có element, attribute, không gian tên (namespace / 네임스페이스), mixed content và một hệ sinh thái lược đồ (schema / 스키마)/truy vấn (query / 쿼리)/transform rất mạnh.

XML phù hợp đặc biệt tốt với document formats, namespace-rich protocols, enterprise tích hợp (integration / 통합), transformation chuỗi xử lý (pipeline / 파이프라인), SOAP, SVG và các tệp (file / 파일) cấu hình lâu đời.

JSON thường nhẹ và dễ dùng hơn cho API object-oriented thông thường.

Vì vậy không nên kết luận “XML cũ nên luôn thay bằng JSON”. Câu hỏi đúng là: lĩnh vực (domain / 도메인) nào đang cần mixed content, namespaces, XSD/XSLT, existing enterprise contracts hoặc document-centric processing?

---

> **Chuyển mạch:** Trong **XML — Beginner**, **33. XML khác JSON như thế nào?** cho ta quy tắc; **34. Ví dụ thực tế: Maven pom.xml** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **35. Tại sao không parse XML bằng regex?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

XML chỉ nói đây là một cây. Maven mới hiểu rằng `groupId`, `artifactId`, `version` có ý nghĩa trong phụ thuộc (dependency / 의존성)/bản dựng (build / 빌드) mô hình (model / 모델).

Tư duy này giúp bạn đọc mọi XML khung phần mềm (framework / 프레임워크): trước tiên hiểu XML cú pháp (syntax / 문법), sau đó tìm vocabulary ngữ nghĩa (semantics / 의미론) của khung phần mềm (framework / 프레임워크) đó.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **34. Ví dụ thực tế: Maven pom.xml** cho ta quy tắc; **35. Tại sao không parse XML bằng regex?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **36. DOM mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Tại sao không parse XML bằng regex?

Giả sử bạn muốn lấy `<name>`. Một cách ngây thơ là tìm substring giữa `<name>` và `</name>`. Nhưng ngay lập tức sẽ gặp vấn đề với không gian tên (namespace / 네임스페이스):

```xml
<u:name xmlns:u="urn:user">Alice</u:name>
```

hoặc CDATA, comments, thực thể (entity / 엔터티) references, nested content và encoding.

XML là grammar có cấu trúc. Regex/string split không hiểu cây (tree / 트리), không gian tên (namespace / 네임스페이스) và parser rules. Hãy dùng XML parser.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **36. DOM mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **35. Tại sao không parse XML bằng regex?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **37. Bài tập tổng hợp Beginner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. DOM mô hình tư duy (mental model / 사고 모델)

Một DOM-like parser có thể materialize toàn bộ cây (tree / 트리) thành objects:

```text
Document
Element
Attr
Text
Comment
ProcessingInstruction
```

DOM phù hợp khi document nhỏ hoặc vừa, bạn cần truy cập nhiều vị trí ngẫu nhiên, cần XPath hoặc cần sửa cây (tree / 트리) rồi serialize lại.

Ở phần Intermediate, bạn sẽ học vì sao SAX/StAX tốt hơn khi XML rất lớn.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **37. Bài tập tổng hợp Beginner** gom các mảnh từ **36. DOM mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **38. mô hình tư duy (mental model / 사고 모델) cần giữ lại sau Beginner** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Bạn phải tự trả lời được rằng `library` là gốc (root / 루트) element, `book` có hai attributes, `title` chứa văn bản (text / 텍스트) nút (node / 노드), `29.99` ở mức XML cốt lõi (core / 핵심) vẫn chỉ là character dữ liệu (data / 데이터), và `currency` là siêu dữ liệu (metadata / 메타데이터) mô tả cách hiểu price.

Nếu title cần chứa chuỗi `A < B`, bạn phải viết:

```xml
<title>A &lt; B</title>
```

Nếu bạn đổi end tag `</book>` thành `</Book>`, tài liệu sẽ không còn well-formed vì XML case-sensitive.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **38. mô hình tư duy (mental model / 사고 모델) cần giữ lại sau Beginner** gom các mảnh từ **37. Bài tập tổng hợp Beginner** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **39. Những lỗi beginner phải tránh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. mô hình tư duy (mental model / 사고 모델) cần giữ lại sau Beginner

Sau khi học xong phần này, bạn không nên nhìn XML như một tệp (file / 파일) văn bản (text / 텍스트) có tag nữa. Bạn phải nhìn nó như một biểu diễn (representation / 표현) của cây dữ liệu được sinh ra từ bytes thông qua decoding và parsing.

Luồng (flow / 흐름) đơn giản nhất là:

```text
bytes
→ decode theo encoding
→ XML parser
→ well-formedness checking
→ tree hoặc stream events
→ application hiểu vocabulary
```

Ở các phần sau, luồng (flow / 흐름) này sẽ được mở rộng thêm không gian tên (namespace / 네임스페이스), DTD, XSD, XPath, XSLT, bảo mật (security / 보안), canonicalization và signatures.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **39. Những lỗi beginner phải tránh** gom các mảnh từ **38. mô hình tư duy (mental model / 사고 모델) cần giữ lại sau Beginner** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **40. XML trong tệp (file / 파일) cấu hình không có nghĩa mọi tag đều thuộc XML tiêu chuẩn (standard / 표준)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Những lỗi beginner phải tránh

Không nối XML bằng string nếu có serializer phù hợp. Không parse XML bằng regex. Không coi văn bản (text / 텍스트) `"27"` là integer nếu chưa có kiểu (type / 타입) tầng (layer / 계층). Không nghĩ CDATA là encryption. Không để secret trong comment. Không bỏ qua encoding. Không coi XML và HTML là cùng parser. Không quên rằng whitespace có thể là dữ liệu thật.

Nếu các nguyên tắc này trở thành phản xạ, bạn đã có nền tảng đúng để học XML nghiêm túc.

---

# PHẦN BỔ SUNG — XML TRONG CÁC HỆ THỐNG THỰC TẾ

> **Chuyển mạch:** Trong **XML — Beginner**, **40. XML trong tệp (file / 파일) cấu hình không có nghĩa mọi tag đều thuộc XML tiêu chuẩn (standard / 표준)** tiếp nhận điểm tựa từ **39. Những lỗi beginner phải tránh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Android dùng XML như thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. XML trong tệp (file / 파일) cấu hình không có nghĩa mọi tag đều thuộc XML tiêu chuẩn (standard / 표준)

Khi bạn mở một tệp (file / 파일) như `pom.xml`, `AndroidManifest.xml` hoặc một tệp (file / 파일) Spring XML cũ, điều quan trọng đầu tiên là tách hai lớp kiến thức. Lớp thứ nhất là **XML cú pháp (syntax / 문법)**: element phải đóng đúng, attribute phải quote, không gian tên (namespace / 네임스페이스) phải được bind đúng, document phải well-formed. Lớp thứ hai là **vocabulary của công cụ**: Maven mới định nghĩa `dependency`, Android mới định nghĩa `activity`, Spring mới định nghĩa `bean`. XML parser chỉ hiểu cấu trúc; khung phần mềm (framework / 프레임워크) hiểu ý nghĩa nghiệp vụ của từng tag.

Đây là mô hình tư duy (mental model / 사고 모델) giúp bạn đọc một XML cấu hình (configuration / 구성) lạ mà không bị choáng. Bạn không cần học lại XML cho từng khung phần mềm (framework / 프레임워크). Bạn giữ nguyên kiến thức XML cốt lõi (core / 핵심), sau đó học vocabulary và lược đồ (schema / 스키마)/tham chiếu (reference / 참조) của khung phần mềm (framework / 프레임워크) đó.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **41. Android dùng XML như thế nào?** tiếp nhận điểm tựa từ **40. XML trong tệp (file / 파일) cấu hình không có nghĩa mọi tag đều thuộc XML tiêu chuẩn (standard / 표준)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Maven, Spring và cấu hình (configuration / 구성) XML trong Java enterprise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Android dùng XML như thế nào?

Android là một ví dụ rất rõ cho việc XML được dùng như một **declarative cấu hình (configuration / 구성) ngôn ngữ (language / 언어)**. Mỗi Android app vẫn có `AndroidManifest.xml`. tệp (file / 파일) manifest mô tả những thông tin mà Android bản dựng (build / 빌드) tools, hệ điều hành và Google Play cần biết về ứng dụng (application / 애플리케이션), chẳng hạn ứng dụng (application / 애플리케이션) components, permissions, intent filters và required features.

Một manifest đơn giản có thể có dạng:

```xml
<?xml version="1.0" encoding="utf-8"?>

<manifest
    xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission
        android:name="android.permission.INTERNET" />

    <application
        android:label="@string/app_name">

        <activity
            android:name=".MainActivity"
            android:exported="true">

            <intent-filter>
                <action
                    android:name="android.intent.action.MAIN" />

                <category
                    android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

        </activity>

    </application>

</manifest>
```

Ở đây XML cốt lõi (core / 핵심) chỉ nói rằng `manifest` là gốc (root / 루트), `application` và `activity` là child elements, còn các `android:*` là namespaced attributes. Chính Android định nghĩa rằng `activity` đại diện cho một Activity thành phần (component / 컴포넌트), `uses-permission` khai báo permission, và `intent-filter` mô tả loại Intent mà thành phần (component / 컴포넌트) có thể nhận.

Không gian tên (namespace / 네임스페이스) declaration:

```xml
xmlns:android="http://schemas.android.com/apk/res/android"
```

là một ví dụ thực tế cho kiến thức không gian tên (namespace / 네임스페이스) mà bạn sẽ học sâu ở Intermediate. Prefix `android` giúp phân biệt attributes thuộc Android vocabulary với unprefixed attributes hoặc vocabulary khác.

Android còn dùng XML cho tài nguyên (resource / 자원) files. Với View-based UI, bố cục (layout / 레이아웃) thường nằm trong `res/layout/*.xml` và mô tả hierarchy của `View`/`ViewGroup`:

```xml
<?xml version="1.0" encoding="utf-8"?>

<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/app_name" />

</LinearLayout>
```

Điểm đáng chú ý là giá trị (value / 값) như `@string/app_name`, `@drawable/icon` hoặc `@layout/main` không phải cú pháp (syntax / 문법) đặc biệt của XML tiêu chuẩn (standard / 표준). Đó là cú pháp (syntax / 문법) tham chiếu (reference / 참조) do Android tài nguyên (resource / 자원) hệ thống (system / 시스템) định nghĩa. XML parser chỉ thấy chúng là attribute strings; Android bản dựng (build / 빌드) tools hiểu và compile chúng thành tài nguyên (resource / 자원) references.

Jetpack Compose làm giảm nhu cầu dùng XML bố cục (layout / 레이아웃) cho những UI viết hoàn toàn bằng Compose, nhưng điều đó không làm XML biến mất khỏi Android. Manifest và nhiều loại tài nguyên (resource / 자원)/cấu hình (configuration / 구성) XML vẫn là một phần quan trọng của Android ecosystem. Vì vậy khi học Android/Kotlin, hiểu XML không gian tên (namespace / 네임스페이스) và tài nguyên (resource / 자원) XML vẫn rất hữu ích.

---

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **XML — Beginner**, **42. Maven, Spring và cấu hình (configuration / 구성) XML trong Java enterprise** tiếp nhận điểm tựa từ **41. Android dùng XML như thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Cách đọc một XML cấu hình (configuration / 구성) mà bạn chưa từng thấy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Maven, Spring và cấu hình (configuration / 구성) XML trong Java enterprise

Maven POM là ví dụ data-centric XML được dùng làm bản dựng (build / 빌드) cấu hình (configuration / 구성). `pom.xml` mô tả dự án (project / 프로젝트) mô hình (model / 모델), dependencies, plugins và bản dựng (build / 빌드) cấu hình (configuration / 구성). Maven thường dùng default không gian tên (namespace / 네임스페이스) và XSD-related siêu dữ liệu (metadata / 메타데이터), vì vậy đây là một tệp (file / 파일) rất tốt để luyện cách đọc không gian tên (namespace / 네임스페이스) thay vì chỉ nhìn cục bộ (local / 로컬) tag names.

Spring hiện đại thường ưu tiên Java cấu hình (configuration / 구성), annotations và Spring Boot conventions, nhưng hệ thống enterprise cũ vẫn có thể chứa nhiều Spring XML cấu hình (configuration / 구성). Ví dụ:

```xml
<bean
    id="userService"
    class="com.example.UserService">

    <property
        name="repository"
        ref="userRepository" />

</bean>
```

Trong ví dụ này, XML không tự biết `bean` là đối tượng (object / 객체) Java. Spring bộ chứa (container / 컨테이너) đọc vocabulary của Spring và biến cấu hình (configuration / 구성) thành đối tượng (object / 객체) definitions/phụ thuộc (dependency / 의존성) wiring.

Khi maintain legacy Java ứng dụng (application / 애플리케이션), bạn thường phải đọc XML cùng Java mã (code / 코드). Cách hiệu quả là xác định không gian tên (namespace / 네임스페이스)/lược đồ (schema / 스키마) của tệp (file / 파일) trước, sau đó xem khung phần mềm (framework / 프레임워크) map từng element/attribute sang hành vi thời gian chạy (runtime behavior / 런타임 동작) như thế nào.

---

> **Chuyển mạch:** Trong **XML — Beginner**, **43. Cách đọc một XML cấu hình (configuration / 구성) mà bạn chưa từng thấy** tiếp nhận điểm tựa từ **42. Maven, Spring và cấu hình (configuration / 구성) XML trong Java enterprise** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Khi nào XML hợp hơn JSON và khi nào JSON hợp hơn XML?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Cách đọc một XML cấu hình (configuration / 구성) mà bạn chưa từng thấy

Khi gặp một tệp (file / 파일) XML lạ, trước tiên hãy tìm gốc (root / 루트) element và không gian tên (namespace / 네임스페이스) declarations. gốc (root / 루트) cho bạn biết loại document tổng quát, còn không gian tên (namespace / 네임스페이스) cho biết vocabulary nào đang được dùng. Sau đó hãy phân biệt element nào là cấu trúc (structure / 구조) chính, attribute nào là siêu dữ liệu (metadata / 메타데이터)/cấu hình (configuration / 구성), và giá trị (value / 값) nào chỉ là string theo XML cốt lõi (core / 핵심) nhưng được khung phần mềm (framework / 프레임워크) diễn giải thành enum, lớp (class / 클래스) name, URI hoặc tài nguyên (resource / 자원) tham chiếu (reference / 참조).

Ví dụ nếu thấy:

```xml
<config
    xmlns="urn:example:config"
    xmlns:sec="urn:example:security">

    <server port="8080" />

    <sec:authentication enabled="true" />

</config>
```

bạn đã có thể suy ra rất nhiều trước khi biết khung phần mềm (framework / 프레임워크) cụ thể. `server` thuộc default không gian tên (namespace / 네임스페이스) `urn:example:config`; `authentication` thuộc bảo mật (security / 보안) không gian tên (namespace / 네임스페이스); `port="8080"` ở XML cốt lõi (core / 핵심) vẫn là văn bản (text / 텍스트) attribute giá trị (value / 값) và khung phần mềm (framework / 프레임워크)/lược đồ (schema / 스키마) mới quyết định nó phải là integer; `enabled="true"` cũng tương tự.

Sau đó mới tìm lược đồ (schema / 스키마) hoặc documentation của vocabulary. Đây là cách đọc XML từ **cấu trúc chung → không gian tên (namespace / 네임스페이스) → đặc tả hợp đồng (contract / 계약) → khung phần mềm (framework / 프레임워크) meaning**, thay vì học thuộc từng tệp (file / 파일) cấu hình.

---

> **Chuyển mạch:** Ở chặng này của **XML — Beginner**, **44. Khi nào XML hợp hơn JSON và khi nào JSON hợp hơn XML?** tiếp nhận điểm tựa từ **43. Cách đọc một XML cấu hình (configuration / 구성) mà bạn chưa từng thấy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 44. Khi nào XML hợp hơn JSON và khi nào JSON hợp hơn XML?

Nếu dữ liệu chỉ là đối tượng (object / 객체)/array đơn giản cho REST API giữa web frontend và backend, JSON thường ngắn, dễ đọc và map tự nhiên vào JavaScript/Java DTO. Nếu giao thức (protocol / 프로토콜) đã có XSD đặc tả hợp đồng (contract / 계약), cần không gian tên (namespace / 네임스페이스) để kết hợp nhiều vocabularies, cần mixed content như document publishing, cần XSLT transformation hoặc phải tương thích với SOAP/B2B standards có sẵn, XML có những khả năng mà JSON không thay thế trực tiếp chỉ bằng việc đổi cú pháp.

Ví dụ một JSON đối tượng (object / 객체) thường biểu diễn dữ liệu bản ghi (record / 레코드) rất tự nhiên:

```json
{
  "id": 123,
  "name": "Alice"
}
```

Trong khi XML mạnh hơn khi một document cần kết hợp siêu dữ liệu (metadata / 메타데이터), không gian tên (namespace / 네임스페이스) và mixed content:

```xml
<article
    xmlns="urn:example:article"
    xmlns:meta="urn:example:metadata"
    meta:id="A123">

    <p>
        Learn <em>XML</em> from its data model.
    </p>

</article>
```

Vì vậy lựa chọn đúng không phải “XML hay JSON cái nào hiện đại hơn”, mà là **mô hình dữ liệu (data model / 데이터 모델) và ecosystem nào phù hợp đặc tả hợp đồng (contract / 계약) của hệ thống**. Đây là tư duy bạn sẽ dùng lại khi học SOAP, XSD, Android resources và enterprise tích hợp (integration / 통합) ở các phần sau.

> **Bàn giao:** Sau **44. Khi nào XML hợp hơn JSON và khi nào JSON hợp hơn XML?**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
