# 17 — File, Excel, Upload & Download Pipeline

## 1. Vì sao file transfer là một boundary riêng?

Ở màn hình CRUD thông thường, dữ liệu đi qua `DataMap`, `DataList` và `Submission`. File transfer khác bản chất vì payload không còn chỉ là structured data nhỏ có schema rõ. Một file có thể lớn, có binary content, MIME type, filename, encoding, DRM, virus risk, temporary storage và lifecycle riêng.

Mental model đúng không phải là:

```text
file = một field lớn trong form
```

mà là:

```text
browser file selection
        ↓
client-side admission check
        ↓
multipart / upload transport
        ↓
WebSquare upload handler hoặc application endpoint
        ↓
server-side validation
        ↓
temporary / permanent storage
        ↓
metadata + business transaction
```

File upload vì vậy là một pipeline có nhiều trust boundary. Component chỉ là điểm bắt đầu của pipeline, không phải security boundary.

## 2. Ba loại dữ liệu cần phân biệt

Một enterprise screen thường trộn ba loại dữ liệu nhưng chúng có lifecycle khác nhau.

**Business data** là record như customer, contract, approval state. Đây thường là `DataMap`/`DataList` và được commit trong database transaction.

**File content** là byte stream. Nó có thể nằm ở filesystem, object storage, shared volume hoặc một document service.

**File metadata** là filename, size, content type, storage key, uploader, checksum, business owner và trạng thái scan. Metadata thường nằm trong database và liên kết business record với file content.

Nếu ba loại này bị coi là một thứ, rollback trở nên khó reasoning. Database rollback không tự xóa file đã ghi vào shared volume, và xóa file vật lý không tự rollback row metadata.

## 3. Upload component không thay thế server validation

WebSquare cung cấp upload component và server-side configuration như `baseDir`, `subDir`, `maxUploadSize`, `allowedExtension`, `deniedExtension`, `uploadMode`, `folderName` và `fileDefiner` ở các dòng engine tương ứng.

Nhưng client-side restriction chỉ cải thiện UX. User có thể bỏ qua UI và gửi HTTP request trực tiếp.

Invariant production phải là:

```text
client validation = fast feedback
server validation = authoritative decision
```

Server phải tự kiểm tra authorization, size, filename, extension/content type, storage destination và business ownership.

## 4. Extension không phải file identity

Tên `invoice.pdf` không chứng minh nội dung là PDF. Extension là metadata do client cung cấp và có thể giả mạo.

Một pipeline an toàn hơn reasoning theo nhiều signal:

```text
filename extension
+ declared MIME type
+ content signature / magic bytes khi phù hợp
+ parser validation
+ malware / policy scan nếu hệ thống yêu cầu
```

Không phải hệ thống nào cũng cần antivirus hoặc deep content inspection, nhưng security decision không nên dựa duy nhất vào chuỗi sau dấu chấm.

## 5. Filename là untrusted input

Filename có thể chứa path separator, Unicode khó nhìn, tên quá dài hoặc ký tự đặc biệt. Không nên dùng filename do browser gửi làm physical path một cách trực tiếp.

Tách hai khái niệm:

```text
originalFileName = tên hiển thị cho người dùng
storageName      = tên/key do server kiểm soát
```

Server có thể tạo UUID/storage key và giữ original name như metadata. `fileDefiner` của WebSquare tồn tại để customize path/name trong những deployment dùng upload handler của engine, nhưng implementation vẫn phải tuân theo policy của hệ thống.

## 6. `baseDir`, `subDir` và business ownership

Cấu hình server có thể ánh xạ upload vào `baseDir` và các `subDir`. Đây là storage routing, không phải authorization model.

Một request có `subDir="finance"` không có nghĩa user được phép ghi file tài chính. Business permission phải được quyết định độc lập.

Senior mental model:

```text
storage location answers: lưu ở đâu?
authorization answers: ai được phép làm gì?
```

Không trộn hai câu hỏi.

## 7. Upload lifecycle và orphan file

Giả sử màn hình tạo hợp đồng làm theo thứ tự:

```text
1. upload attachment
2. server lưu file
3. user bấm Save contract
4. Save contract fail
```

File ở bước 2 có thể trở thành orphan vì business record chưa tồn tại.

Có ba strategy phổ biến.

**Upload after business commit** đơn giản hóa ownership nhưng UX có thể chậm và khó preview trước save.

**Temporary upload** lưu file ở staging area, sau khi business transaction thành công mới promote/attach vào record chính.

**Compensating cleanup** cho phép upload trước nhưng nếu save fail hoặc session hết hạn thì background job xóa orphan.

Không có một strategy đúng cho mọi hệ thống. Điều cần master là nhận ra file storage và database transaction thường không cùng một atomic transaction.

## 8. Idempotency cho upload

Mobile network hoặc user double-click có thể làm cùng file được upload hai lần. Chỉ disable button là chưa đủ vì retry có thể đến từ network/client layer.

Có thể dùng request token, upload session ID hoặc checksum + business key tùy use case.

```text
upload intent id
      ↓
server nhận request
      ↓
đã xử lý intent này chưa?
   ├─ rồi → trả kết quả cũ
   └─ chưa → lưu và ghi nhận intent
```

Đây là cùng nguyên tắc idempotency đã gặp ở save mutation, nhưng file khiến cost duplicate lớn hơn.

## 9. Progress không đồng nghĩa completion

Progress bar 100% có thể chỉ nghĩa browser đã gửi đủ bytes. Nó chưa chắc nghĩa server đã scan, persist metadata và commit business operation.

Phân biệt:

```text
transfer progress
server processing
business acceptance
```

UI nên phản ánh state machine thật thay vì một boolean `uploaded=true` quá sớm.

## 10. Download là authorization operation

Download thường bị xem như việc mở URL. Nhưng nếu file chứa business data, endpoint download phải kiểm tra identity và authorization tại thời điểm request.

Không nên coi một path khó đoán là security control.

```text
GET /download/very-random-path/file.pdf
```

vẫn cần authorization nếu tài liệu không public.

`$p.download(...)` là cơ chế client để bắt đầu download trong các flow phù hợp; nó không biến URL thành protected resource.

## 11. Content-Disposition và filename

Server thường quyết định browser hiển thị inline hay download bằng response header. Filename trong `Content-Disposition` phải được encode và sanitize đúng.

Với tên file đa ngôn ngữ, Korean/Vietnamese/Unicode, bug encoding rất dễ xuất hiện nếu server, browser và legacy framework không thống nhất charset.

Đừng sửa bằng cách encode/decode ngẫu nhiên nhiều lần. Xác định byte/string boundary và header contract trước.

## 12. Excel import là ingestion pipeline

GridView có thể đọc Excel/CSV qua API và server configuration tùy build. Nhưng import Excel không chỉ là “đưa sheet vào Grid”. Nó là ingestion pipeline:

```text
file
 ↓
parse
 ↓
column mapping
 ↓
type conversion
 ↓
row validation
 ↓
business validation
 ↓
preview/error report
 ↓
commit
```

Nếu parse xong rồi insert thẳng database, user chỉ biết lỗi sau khi đã có partial side effect.

## 13. Schema mapping phải explicit

Excel thường có header do con người nhìn, còn DataList có column ID ổn định.

Ví dụ:

```text
Excel: 고객명 | 생년월일 | 상태
Model: CUSTOMER_NAME | BIRTH_DATE | STATUS_CODE
```

Đừng dựa hoàn toàn vào column position nếu file do user tạo/chỉnh sửa. Một cột mới ở đầu sheet có thể shift toàn bộ mapping.

Nếu template do hệ thống kiểm soát, version template và validate header trước khi ingest.

## 14. Type conversion không phải validation

Chuỗi `20260922` có thể parse thành date format hợp lệ nhưng vẫn không thỏa business rule. `-100` có thể là number hợp lệ nhưng không hợp lệ với quantity.

Tách:

```text
syntactic validation: đọc được không?
semantic validation: giá trị có ý nghĩa hợp lệ không?
business validation: operation có được phép không?
```

Ba lớp lỗi nên có message khác nhau để user sửa file nhanh.

## 15. Excel cell format và cell value

Excel cell có thể có raw value và display format khác nhau. Date/number đặc biệt dễ sai khi parser đọc serial number, formatted text hoặc locale-specific representation.

Canonical model nên nhận một representation đã normalize.

```text
Excel display: 1,234.50
canonical model: 1234.5

Excel display: 2026.09.22
canonical model: 20260922 hoặc ISO contract
```

Không để business layer phụ thuộc vào format trang tính.

## 16. `dataConvertor` và conversion boundary

WebSquare server configuration hỗ trợ hook conversion cho Excel/CSV ở một số engine/build. Hook như `dataConvertor` hữu ích khi site cần normalize cell trước khi trả về client.

Nhưng conversion hook không nên chứa toàn bộ business logic. Nó nằm ở data ingestion boundary; business invariant vẫn nên ở application/service layer để cùng rule được áp dụng cho cả UI, batch và API khác.

## 17. CSV có thêm vấn đề encoding

CSV nhìn đơn giản nhưng có ambiguity về delimiter, quote, newline, BOM và encoding. Korean/Vietnamese data làm lỗi encoding dễ lộ hơn.

Một CSV pipeline cần explicit ít nhất:

```text
charset
BOM policy
delimiter
quote escaping
newline handling
column order/header
```

WebSquare server configuration có các option encoding/BOM cho CSV ở các build tương ứng. Hãy xem chúng là contract deployment, không phải chi tiết vô hại.

## 18. Excel export: “nhìn giống Grid” chưa chắc là đúng dataset

Grid có thể đang filter, sort, paging, hide deleted rows hoặc chỉ render một phần dataset. Trước export phải trả lời:

```text
export visible rows?
all loaded rows?
all server rows?
changed rows only?
selected rows?
```

Nếu requirement là “toàn bộ kết quả 2 triệu dòng” nhưng browser chỉ load 100 dòng, client-side export không thể tự tạo ra phần data chưa tồn tại.

Khi dataset lớn, server-side export thường là boundary hợp lý hơn.

## 19. Large Excel và memory pressure

Tạo workbook lớn có thể tiêu thụ nhiều heap. WebSquare server configuration có các option như `rowAccessWindowSize` ở flow Excel download để giới hạn số row giữ trong memory trong những implementation dùng streaming POI tương ứng.

Mental model:

```text
all rows in memory
→ peak heap lớn
→ GC pressure
→ OutOfMemory risk

stream/windowed write
→ bounded memory
→ throughput ổn định hơn
```

Không chọn batch/window size chỉ vì sample dùng một con số cố định. Đo heap, throughput và file size thực tế.

## 20. Export là snapshot consistency problem

Nếu export 500.000 record mất 30 giây, dữ liệu database có thể thay đổi trong lúc export.

Business phải quyết định semantics:

```text
snapshot tại thời điểm bắt đầu?
read committed trong suốt query?
export theo version/reporting store?
```

Đây không còn là vấn đề GridView. Nó là transaction/data consistency của backend.

## 21. DRM và encryption hooks

Một số enterprise deployment dùng DRM cho Excel/file. WebSquare server-side configuration có hook decrypt/encrypt cho upload/download ở các engine tương ứng.

Đừng nhầm DRM với transport security.

```text
TLS bảo vệ dữ liệu trên đường truyền
DRM/encryption-at-rest bảo vệ artifact theo policy khác
```

Một hệ thống có thể cần cả hai.

## 22. Temporary file cũng là sensitive data

Nếu upload được decrypt vào `tempDir`, temporary file có thể chứa plain content. Security review phải hỏi:

```text
ai đọc được temp directory?
file tồn tại bao lâu?
cleanup khi crash thế nào?
disk encryption có không?
log có ghi path nhạy cảm không?
```

Temporary không có nghĩa là vô hại.

## 23. Hybrid/mobile download khác browser download

Trong browser desktop, `$p.download` hoặc navigation/form download có thể đủ. Trong hybrid mobile app, file cần được ghi vào device filesystem rồi mở bằng native viewer hoặc system intent.

Tài liệu WebSquare mô tả flow dùng Cordova `FileTransfer` trong các hybrid setup cũ. Với project thực tế, plugin/API chính xác phụ thuộc Cordova/WebView/native stack đang dùng.

Điểm bất biến là:

```text
web URL
→ native download capability
→ app-accessible file path
→ platform viewer / share intent
```

Không hard-code Android path rồi giả định iOS giống nhau.

## 24. Download URL và token lifetime

Nếu backend dùng signed URL hoặc temporary token, thời gian sống phải đủ cho user bắt đầu download nhưng không quá dài.

Hybrid app có thể background/resume làm request trễ. Vì vậy expiry, retry và re-authentication phải được thiết kế như một state machine, không chỉ là string URL.

## 25. Failure taxonomy cho file pipeline

Một upload có thể fail ở nhiều lớp:

```text
selection       → file không tồn tại / user cancel
client policy   → size/type fail
transport       → offline/timeout
server parser   → malformed multipart
security        → extension/content/scan reject
storage         → disk/object store fail
metadata        → DB transaction fail
business        → ownership/state reject
post-processing → OCR/DRM/virus scan fail
```

Nếu mọi lỗi đều thành “Upload failed”, production support sẽ rất chậm.

## 26. Observability cho file transfer

Không log binary content hoặc sensitive document. Log metadata đủ để trace:

```text
requestId
uploadIntentId
businessKey đã mask khi cần
original filename đã sanitize
size
content type
storage key nội bộ
stage
elapsed time
result code
```

Correlation ID phải đi xuyên client → upload endpoint → storage → business service nếu muốn điều tra incident nhanh.

## 27. Security checklist thực tế

Trước khi productionize upload/download, phải trả lời được:

```text
Server có enforce max size không?
Extension/MIME/content validation nằm ở đâu?
Filename có thể escape storage directory không?
Download có authorization lại không?
Temporary file cleanup ra sao?
Upload retry có tạo duplicate không?
File metadata và business transaction có thể lệch không?
Có scan/DRM requirement không?
Log có lộ path hoặc document data không?
```

Nếu một câu trả lời là “component đã xử lý”, hãy kiểm tra lại trust boundary.

## 28. Pattern: attachment staging

Một pattern production dễ reasoning:

```text
Open create screen
    ↓
create uploadSessionId
    ↓
files → temporary storage(uploadSessionId)
    ↓
user Save
    ↓
server transaction creates business record
    ↓
attach/promote files using uploadSessionId
    ↓
mark session committed
    ↓
background cleanup uncommitted expired sessions
```

Pattern này tách upload UX khỏi business commit nhưng vẫn có cleanup semantics rõ.

## 29. Pattern: server-side report export

Với report lớn:

```text
client submits export request
        ↓
server creates export job
        ↓
query + generate file asynchronously
        ↓
store artifact
        ↓
client polls/receives completion
        ↓
authorized download
```

UI không bị freeze và request không cần giữ HTTP connection quá lâu. Đổi lại cần job state, expiry và cleanup.

## 30. Senior note: file path không phải business identifier

Đừng truyền physical path khắp hệ thống như `/data/upload/2026/09/a.pdf` rồi coi nó là identity. Storage layout có thể đổi.

Ưu tiên opaque file ID/storage key:

```text
business record → attachmentId → storage service → physical location
```

Điều này cho phép migrate filesystem sang object storage mà không đổi business contract.

## 31. Kết nối với các chapter khác

File/Excel pipeline nối trực tiếp với [05 — GridView & CRUD](05_gridview_crud_patterns.md), [12 — Build, Configuration & Deployment](12_build_config_deployment.md), [13 — GridView Editing & Identity](13_gridview_editing_identity_internals.md) và [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

Hybrid/mobile download được đào sâu ở [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md). Production tracing cho upload/export job được nối với [19 — Observability & Incident Response](19_observability_incident_response.md).

## 32. Mastery checkpoint

Bạn đã master chapter này khi có thể nhìn một yêu cầu “upload file rồi save”, “import Excel vào grid” hoặc “export toàn bộ dữ liệu” và tự tách được transport, parsing, validation, storage, business transaction, authorization, consistency, memory và cleanup; đồng thời biết phần nào thuộc WebSquare component/config và phần nào bắt buộc phải được giải quyết ở backend/platform.