# 17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao tệp (file / 파일) transfer là một ranh giới (boundary / 경계) riêng?** làm rõ cặp khái niệm dễ lẫn và giới hạn của cách giải thích; sau đó sang **2. Ba loại dữ liệu cần phân biệt** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối file, Excel và upload/download pipeline, để theo dõi dữ liệu qua validation, serialization, transport và lưu trữ.

## 1. Vì sao tệp (file / 파일) transfer là một ranh giới (boundary / 경계) riêng?

Ở màn hình CRUD thông thường, dữ liệu đi qua `DataMap`, `DataList` và `Submission`. tệp (file / 파일) transfer khác bản chất vì payload không còn chỉ là structured dữ liệu (data / 데이터) nhỏ có lược đồ (schema / 스키마) rõ. Một tệp (file / 파일) có thể lớn, có nhị phân (binary / 이진) content, MIME kiểu (type / 타입), filename, encoding, DRM, virus rủi ro (risk / 위험), temporary lưu trữ (storage / 저장소) và vòng đời (lifecycle / 생명주기) riêng.

Mô hình tư duy (mental model / 사고 모델) đúng không phải là:

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

Tệp (file / 파일) upload vì vậy là một chuỗi xử lý (pipeline / 파이프라인) có nhiều trust ranh giới (boundary / 경계). thành phần (component / 컴포넌트) chỉ là điểm bắt đầu của chuỗi xử lý (pipeline / 파이프라인), không phải ranh giới bảo mật (security boundary / 보안 경계).

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **1. Vì sao tệp (file / 파일) transfer là một ranh giới (boundary / 경계) riêng?** đặt tiêu chí; **2. Ba loại dữ liệu cần phân biệt** dùng tiêu chí đó để kiểm tra ranh giới, rồi **3. Upload thành phần (component / 컴포넌트) không thay thế máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)** mở rộng hệ quả.

## 2. Ba loại dữ liệu cần phân biệt

Một enterprise screen thường trộn ba loại dữ liệu nhưng chúng có vòng đời (lifecycle / 생명주기) khác nhau.

**nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터)** là bản ghi (record / 레코드) như customer, đặc tả hợp đồng (contract / 계약), approval trạng thái (state / 상태). Đây thường là `DataMap`/`DataList` và được lần ghi nhận (commit / 커밋) trong cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션).

**tệp (file / 파일) content** là byte stream. Nó có thể nằm ở filesystem, đối tượng (object / 객체) lưu trữ (storage / 저장소), dùng chung (shared / 공유) volume hoặc một document dịch vụ (service / 서비스).

**tệp (file / 파일) siêu dữ liệu (metadata / 메타데이터)** là filename, kích thước (size / 크기), content kiểu (type / 타입), lưu trữ (storage / 저장소) key, uploader, checksum, nghiệp vụ (business / 비즈니스) đơn vị sở hữu (owner / 오너) và trạng thái scan. siêu dữ liệu (metadata / 메타데이터) thường nằm trong cơ sở dữ liệu (database / 데이터베이스) và liên kết nghiệp vụ (business / 비즈니스) bản ghi (record / 레코드) với tệp (file / 파일) content.

Nếu ba loại này bị coi là một thứ, quay lui (rollback / 롤백) trở nên khó lập luận (reasoning / 추론). cơ sở dữ liệu (database / 데이터베이스) quay lui (rollback / 롤백) không tự xóa tệp (file / 파일) đã ghi vào dùng chung (shared / 공유) volume, và xóa tệp (file / 파일) vật lý không tự quay lui (rollback / 롤백) row siêu dữ liệu (metadata / 메타데이터).

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **2. Ba loại dữ liệu cần phân biệt** đặt vấn đề; **3. Upload thành phần (component / 컴포넌트) không thay thế máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)** đối chiếu bằng chứng, rồi **4. Extension không phải tệp (file / 파일) định danh (identity / 식별자)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Upload thành phần (component / 컴포넌트) không thay thế máy chủ (server / 서버) kiểm tra hợp lệ (validation / 검증)

WebSquare cung cấp upload thành phần (component / 컴포넌트) và server-side cấu hình (configuration / 구성) như `baseDir`, `subDir`, `maxUploadSize`, `allowedExtension`, `deniedExtension`, `uploadMode`, `folderName` và `fileDefiner` ở các dòng engine tương ứng.

Nhưng client-side restriction chỉ cải thiện UX. người dùng (user / 사용자) có thể bỏ qua UI và gửi HTTP yêu cầu (request / 요청) trực tiếp.

Bất biến (invariant / 불변식) môi trường vận hành (production / 운영 환경) phải là:

```text
client validation = fast feedback
server validation = authoritative decision
```

Máy chủ (server / 서버) phải xác thực authorization, kích thước (size / 크기), filename, extension/content kiểu (type / 타입), lưu trữ (storage / 저장소) destination và nghiệp vụ (business / 비즈니스) quyền sở hữu (ownership / 소유권).

> **Nối mạch:** Upload component không thay thế server validation; extension chỉ là metadata gợi ý, còn filename tiếp theo phải được xử lý như untrusted input.

## 4. Extension không phải tệp (file / 파일) định danh (identity / 식별자)

Tên `invoice.pdf` không chứng minh nội dung là PDF. Extension là siêu dữ liệu (metadata / 메타데이터) do máy khách (client / 클라이언트) cung cấp và có thể giả mạo.

Một chuỗi xử lý (pipeline / 파이프라인) an toàn hơn lập luận (reasoning / 추론) theo nhiều tín hiệu (signal / 신호):

```text
filename extension
+ declared MIME type
+ content signature / magic bytes khi phù hợp
+ parser validation
+ malware / policy scan nếu hệ thống yêu cầu
```

Không phải hệ thống nào cũng cần antivirus hoặc deep content inspection, nhưng bảo mật (security / 보안) quyết định (decision / 결정) không nên dựa duy nhất vào chuỗi sau dấu chấm.

> **Nối mạch:** Extension chỉ là metadata; filename phải được coi là untrusted input, rồi `baseDir`/`subDir` tiếp theo phải gắn với ownership nghiệp vụ và policy truy cập.

## 5. Filename là untrusted đầu vào (input / 입력)

Filename có thể chứa đường dẫn (path / 경로) separator, Unicode khó nhìn, tên quá dài hoặc ký tự đặc biệt. Không nên dùng filename do trình duyệt (browser / 브라우저) gửi làm vật lý (physical / 물리적) đường dẫn (path / 경로) một cách trực tiếp.

Tách hai khái niệm:

```text
originalFileName = tên hiển thị cho người dùng
storageName      = tên/key do server kiểm soát
```

Máy chủ (server / 서버) có thể tạo UUID/lưu trữ (storage / 저장소) key và giữ original name như siêu dữ liệu (metadata / 메타데이터). `fileDefiner` của WebSquare tồn tại để customize đường dẫn (path / 경로)/name trong những triển khai (deployment / 배포) dùng upload handler của engine, nhưng hiện thực (implementation / 구현) vẫn phải tuân theo chính sách (policy / 정책) của hệ thống.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, sau nội dung của **5. Filename là untrusted đầu vào (input / 입력)**, **6. baseDir, subDir và nghiệp vụ (business / 비즈니스) quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **7. Upload vòng đời (lifecycle / 생명주기) và orphan tệp (file / 파일)** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. `baseDir`, `subDir` và nghiệp vụ (business / 비즈니스) quyền sở hữu (ownership / 소유권)

Cấu hình máy chủ (server / 서버) có thể ánh xạ upload vào `baseDir` và các `subDir`. Đây là lưu trữ (storage / 저장소) routing, không phải authorization mô hình (model / 모델).

Một yêu cầu (request / 요청) có `subDir="finance"` không có nghĩa người dùng (user / 사용자) được phép ghi tệp (file / 파일) tài chính. nghiệp vụ (business / 비즈니스) permission phải được quyết định độc lập.

Cấp cao (senior / 시니어) mô hình tư duy (mental model / 사고 모델):

```text
storage location answers: lưu ở đâu?
authorization answers: ai được phép làm gì?
```

Không trộn hai câu hỏi.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **6. baseDir, subDir và nghiệp vụ (business / 비즈니스) quyền sở hữu (ownership / 소유권)** đặt đầu vào cho **7. Upload vòng đời (lifecycle / 생명주기) và orphan tệp (file / 파일)**, rồi **8. Idempotency cho upload** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Upload vòng đời (lifecycle / 생명주기) và orphan tệp (file / 파일)

Giả sử màn hình tạo hợp đồng làm theo thứ tự:

```text
1. upload attachment
2. server lưu file
3. user bấm Save contract
4. Save contract fail
```

Tệp (file / 파일) ở bước 2 có thể trở thành orphan vì nghiệp vụ (business / 비즈니스) bản ghi (record / 레코드) chưa tồn tại.

Có ba chiến lược (strategy / 전략) phổ biến.

**Upload after nghiệp vụ (business / 비즈니스) lần ghi nhận (commit / 커밋)** đơn giản hóa quyền sở hữu (ownership / 소유권) nhưng UX có thể chậm và khó preview trước save.

**Temporary upload** lưu tệp (file / 파일) ở staging area, sau khi nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션) thành công mới promote/attach vào bản ghi (record / 레코드) chính.

**Compensating cleanup** cho phép upload trước nhưng nếu save thất bại (fail / 실패) hoặc session hết hạn thì background job xóa orphan.

Không có một chiến lược (strategy / 전략) đúng cho mọi hệ thống. Điều cần master là nhận ra tệp (file / 파일) lưu trữ (storage / 저장소) và cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) thường không cùng một atomic giao dịch (transaction / 트랜잭션).

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **7. Upload vòng đời (lifecycle / 생명주기) và orphan tệp (file / 파일)** đặt đầu vào cho **8. Idempotency cho upload**, rồi **9. Progress không đồng nghĩa completion** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. Idempotency cho upload

Mobile mạng (network / 네트워크) hoặc người dùng (user / 사용자) double-click có thể làm cùng tệp (file / 파일) được upload hai lần. Chỉ disable button là chưa đủ vì thử lại (retry / 재시도) có thể đến từ mạng (network / 네트워크)/máy khách (client / 클라이언트) tầng (layer / 계층).

Có thể dùng yêu cầu (request / 요청) đơn vị từ (token / 토큰), upload session ID hoặc checksum + nghiệp vụ (business / 비즈니스) key tùy use trường hợp (case / 사례).

```text
upload intent id
      ↓
server nhận request
      ↓
đã xử lý intent này chưa?
   ├─ rồi → trả kết quả cũ
   └─ chưa → lưu và ghi nhận intent
```

Đây là cùng nguyên tắc idempotency đã gặp ở save mutation, nhưng tệp (file / 파일) khiến chi phí (cost / 비용) duplicate lớn hơn.

> **Nối mạch:** Idempotency ngăn upload lặp tạo bản sao; progress chỉ là telemetry, còn completion cần trạng thái bền vững trước khi xét download authorization.

## 9. Progress không đồng nghĩa completion

Progress bar 100% có thể chỉ nghĩa trình duyệt (browser / 브라우저) đã gửi đủ bytes. Nó chưa chắc nghĩa máy chủ (server / 서버) đã scan, persist siêu dữ liệu (metadata / 메타데이터) và lần ghi nhận (commit / 커밋) nghiệp vụ (business / 비즈니스) thao tác (operation / 연산).

Phân biệt:

```text
transfer progress
server processing
business acceptance
```

UI nên phản ánh máy trạng thái (state machine / 상태 머신) thật thay vì một boolean `uploaded=true` quá sớm.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **10. Download là authorization thao tác (operation / 연산)** nối từ **9. Progress không đồng nghĩa completion** sang **11. Content-Disposition và filename**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Download là authorization thao tác (operation / 연산)

Download thường bị xem như việc mở URL. Nhưng nếu tệp (file / 파일) chứa nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터), endpoint download phải kiểm tra định danh (identity / 식별자) và authorization tại thời điểm yêu cầu (request / 요청).

Không nên coi một đường dẫn (path / 경로) khó đoán là bảo mật (security / 보안) điều khiển (control / 제어).

```text
GET /download/very-random-path/file.pdf
```

vẫn cần authorization nếu tài liệu không công khai (public / 공개).

`$p.download(...)` là cơ chế máy khách (client / 클라이언트) để bắt đầu download trong các luồng (flow / 흐름) phù hợp; nó không biến URL thành protected tài nguyên (resource / 자원).

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **11. Content-Disposition và filename** nối từ **10. Download là authorization thao tác (operation / 연산)** sang **12. Excel import là ingestion chuỗi xử lý (pipeline / 파이프라인)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Content-Disposition và filename

Máy chủ (server / 서버) thường quyết định trình duyệt (browser / 브라우저) hiển thị inline hay download bằng phản hồi (response / 응답) header. Filename trong `Content-Disposition` phải được encode và sanitize đúng.

Với tên tệp (file / 파일) đa ngôn ngữ, Korean/Vietnamese/Unicode, bug encoding rất dễ xuất hiện nếu máy chủ (server / 서버), trình duyệt (browser / 브라우저) và legacy khung phần mềm (framework / 프레임워크) không thống nhất charset.

Đừng sửa bằng cách encode/decode ngẫu nhiên nhiều lần. Xác định byte/string ranh giới (boundary / 경계) và header đặc tả hợp đồng (contract / 계약) trước.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **11. Content-Disposition và filename** đặt đầu vào cho **12. Excel import là ingestion chuỗi xử lý (pipeline / 파이프라인)**, rồi **13. lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) phải tường minh (explicit / 명시적)** mở rộng hệ quả hoặc giới hạn liên quan.

## 12. Excel import là ingestion chuỗi xử lý (pipeline / 파이프라인)

GridView có thể đọc Excel/CSV qua API và máy chủ (server / 서버) cấu hình (configuration / 구성) tùy bản dựng (build / 빌드). Nhưng import Excel không chỉ là “đưa sheet vào Grid”. Nó là ingestion chuỗi xử lý (pipeline / 파이프라인):

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

Nếu parse xong rồi insert thẳng cơ sở dữ liệu (database / 데이터베이스), người dùng (user / 사용자) chỉ biết lỗi sau khi đã có partial side tác động (effect / 효과).

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **12. Excel import là ingestion chuỗi xử lý (pipeline / 파이프라인)** đặt đầu vào cho **13. lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) phải tường minh (explicit / 명시적)**, rồi **14. kiểu (type / 타입) conversion không phải kiểm tra hợp lệ (validation / 검증)** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) phải tường minh (explicit / 명시적)

Excel thường có header do con người nhìn, còn DataList có column ID ổn định.

Ví dụ:

```text
Excel: 고객명 | 생년월일 | 상태
Model: CUSTOMER_NAME | BIRTH_DATE | STATUS_CODE
```

Đừng dựa hoàn toàn vào column position nếu tệp (file / 파일) do người dùng (user / 사용자) tạo/chỉnh sửa. Một cột mới ở đầu sheet có thể shift toàn bộ ánh xạ (mapping / 매핑).

Nếu template do hệ thống kiểm soát, phiên bản (version / 버전) template và validate header trước khi ingest.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **14. kiểu (type / 타입) conversion không phải kiểm tra hợp lệ (validation / 검증)** nối từ **13. lược đồ (schema / 스키마) ánh xạ (mapping / 매핑) phải tường minh (explicit / 명시적)** sang **15. Excel cell format và cell giá trị (value / 값)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. kiểu (type / 타입) conversion không phải kiểm tra hợp lệ (validation / 검증)

Chuỗi `20260922` có thể parse thành date format hợp lệ nhưng vẫn không thỏa nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙). `-100` có thể là number hợp lệ nhưng không hợp lệ với quantity.

Tách:

```text
syntactic validation: đọc được không?
semantic validation: giá trị có ý nghĩa hợp lệ không?
business validation: operation có được phép không?
```

Ba lớp lỗi nên có message khác nhau để người dùng (user / 사용자) sửa tệp (file / 파일) nhanh.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **15. Excel cell format và cell giá trị (value / 값)** nối từ **14. kiểu (type / 타입) conversion không phải kiểm tra hợp lệ (validation / 검증)** sang **16. dataConvertor và conversion ranh giới (boundary / 경계)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Excel cell format và cell giá trị (value / 값)

Excel cell có thể có raw giá trị (value / 값) và display format khác nhau. Date/number đặc biệt dễ sai khi parser đọc serial number, formatted văn bản (text / 텍스트) hoặc locale-specific biểu diễn (representation / 표현).

Chuẩn gốc (canonical / 정본) mô hình (model / 모델) nên nhận một biểu diễn (representation / 표현) đã normalize.

```text
Excel display: 1,234.50
canonical model: 1234.5

Excel display: 2026.09.22
canonical model: 20260922 hoặc ISO contract
```

Không để nghiệp vụ (business / 비즈니스) tầng (layer / 계층) phụ thuộc vào format trang tính.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **15. Excel cell format và cell giá trị (value / 값)** đặt tiêu chí; **16. dataConvertor và conversion ranh giới (boundary / 경계)** dùng tiêu chí đó để kiểm tra ranh giới, rồi **17. CSV có thêm vấn đề encoding** mở rộng hệ quả.

## 16. `dataConvertor` và conversion ranh giới (boundary / 경계)

WebSquare máy chủ (server / 서버) cấu hình (configuration / 구성) hỗ trợ hook conversion cho Excel/CSV ở một số engine/bản dựng (build / 빌드). Hook như `dataConvertor` hữu ích khi site cần normalize cell trước khi trả về máy khách (client / 클라이언트).

Nhưng conversion hook không nên chứa toàn bộ lô-gic nghiệp vụ (business logic / 비즈니스 로직). Nó nằm ở dữ liệu (data / 데이터) ingestion ranh giới (boundary / 경계); nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) vẫn nên ở ứng dụng (application / 애플리케이션)/dịch vụ (service / 서비스) tầng (layer / 계층) để cùng quy tắc (rule / 규칙) được áp dụng cho cả UI, batch và API khác.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **16. dataConvertor và conversion ranh giới (boundary / 경계)** đặt tiêu chí; **17. CSV có thêm vấn đề encoding** dùng tiêu chí đó để kiểm tra ranh giới, rồi **18. Excel export: “nhìn giống Grid” chưa chắc là đúng dataset** mở rộng hệ quả.

## 17. CSV có thêm vấn đề encoding

CSV nhìn đơn giản nhưng có ambiguity về delimiter, quote, newline, BOM và encoding. Korean/Vietnamese dữ liệu (data / 데이터) làm lỗi encoding dễ lộ hơn.

Một CSV chuỗi xử lý (pipeline / 파이프라인) cần tường minh (explicit / 명시적) ít nhất:

```text
charset
BOM policy
delimiter
quote escaping
newline handling
column order/header
```

WebSquare máy chủ (server / 서버) cấu hình (configuration / 구성) có các option encoding/BOM cho CSV ở các bản dựng (build / 빌드) tương ứng. Hãy xem chúng là đặc tả hợp đồng (contract / 계약) triển khai (deployment / 배포), không phải chi tiết vô hại.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **18. Excel export: “nhìn giống Grid” chưa chắc là đúng dataset** nối từ **17. CSV có thêm vấn đề encoding** sang **19. Large Excel và bộ nhớ (memory / 메모리) pressure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. Excel export: “nhìn giống Grid” chưa chắc là đúng dataset

Grid có thể đang filter, sort, paging, hide deleted rows hoặc chỉ kết xuất (render / 렌더링) một phần dataset. Trước export phải trả lời:

```text
export visible rows?
all loaded rows?
all server rows?
changed rows only?
selected rows?
```

Nếu yêu cầu (requirement / 요구사항) là “toàn bộ kết quả 2 triệu dòng” nhưng trình duyệt (browser / 브라우저) chỉ tải (load / 로드) 100 dòng, client-side export không thể tự tạo ra phần dữ liệu (data / 데이터) chưa tồn tại.

Khi dataset lớn, server-side export thường là ranh giới (boundary / 경계) hợp lý hơn.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **19. Large Excel và bộ nhớ (memory / 메모리) pressure** nối từ **18. Excel export: “nhìn giống Grid” chưa chắc là đúng dataset** sang **20. Export là snapshot consistency bài toán (problem / 문제)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. Large Excel và bộ nhớ (memory / 메모리) pressure

Tạo workbook lớn có thể tiêu thụ nhiều vùng nhớ động (heap / 힙). WebSquare máy chủ (server / 서버) cấu hình (configuration / 구성) có các option như `rowAccessWindowSize` ở luồng (flow / 흐름) Excel download để giới hạn số row giữ trong bộ nhớ (memory / 메모리) trong những hiện thực (implementation / 구현) dùng streaming POI tương ứng.

Mô hình tư duy (mental model / 사고 모델):

```text
all rows in memory
→ peak heap lớn
→ GC pressure
→ OutOfMemory risk

stream/windowed write
→ bounded memory
→ throughput ổn định hơn
```

Không chọn batch/cửa sổ (window / 윈도우) kích thước (size / 크기) chỉ vì mẫu (sample / 표본) dùng một con số cố định. Đo vùng nhớ động (heap / 힙), thông lượng (throughput / 처리량) và tệp (file / 파일) kích thước (size / 크기) thực tế.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **20. Export là snapshot consistency bài toán (problem / 문제)** nối từ **19. Large Excel và bộ nhớ (memory / 메모리) pressure** sang **21. DRM và encryption hooks**, vì cơ chế trước tạo đầu vào cho bước sau.

## 20. Export là snapshot consistency bài toán (problem / 문제)

Nếu export 500.000 bản ghi (record / 레코드) mất 30 giây, dữ liệu cơ sở dữ liệu (database / 데이터베이스) có thể thay đổi trong lúc export.

Nghiệp vụ (business / 비즈니스) phải quyết định ngữ nghĩa (semantics / 의미론):

```text
snapshot tại thời điểm bắt đầu?
read committed trong suốt query?
export theo version/reporting store?
```

Đây không còn là vấn đề GridView. Nó là giao dịch (transaction / 트랜잭션)/dữ liệu (data / 데이터) consistency của backend.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **21. DRM và encryption hooks** nối từ **20. Export là snapshot consistency bài toán (problem / 문제)** sang **22. Temporary tệp (file / 파일) cũng là sensitive dữ liệu (data / 데이터)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 21. DRM và encryption hooks

Một số enterprise triển khai (deployment / 배포) dùng DRM cho Excel/tệp (file / 파일). WebSquare server-side cấu hình (configuration / 구성) có hook decrypt/encrypt cho upload/download ở các engine tương ứng.

Đừng nhầm DRM với vận chuyển (transport / 전송) bảo mật (security / 보안).

```text
TLS bảo vệ dữ liệu trên đường truyền
DRM/encryption-at-rest bảo vệ artifact theo policy khác
```

Một hệ thống có thể cần cả hai.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **21. DRM và encryption hooks** đặt vấn đề; **22. Temporary tệp (file / 파일) cũng là sensitive dữ liệu (data / 데이터)** đối chiếu bằng chứng, rồi **23. Hybrid/mobile download khác trình duyệt (browser / 브라우저) download** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. Temporary tệp (file / 파일) cũng là sensitive dữ liệu (data / 데이터)

Nếu upload được decrypt vào `tempDir`, temporary tệp (file / 파일) có thể chứa plain content. bảo mật (security / 보안) rà soát (review / 검토) phải hỏi:

```text
ai đọc được temp directory?
file tồn tại bao lâu?
cleanup khi crash thế nào?
disk encryption có không?
log có ghi path nhạy cảm không?
```

Temporary không có nghĩa là vô hại.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **22. Temporary tệp (file / 파일) cũng là sensitive dữ liệu (data / 데이터)** đặt vấn đề; **23. Hybrid/mobile download khác trình duyệt (browser / 브라우저) download** đối chiếu bằng chứng, rồi **24. Download URL và đơn vị từ (token / 토큰) thời gian tồn tại (lifetime / 수명)** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. Hybrid/mobile download khác trình duyệt (browser / 브라우저) download

Trong trình duyệt (browser / 브라우저) desktop, `$p.download` hoặc điều hướng (navigation / 내비게이션)/form download có thể đủ. Trong hybrid mobile app, tệp (file / 파일) cần được ghi vào thiết bị (device / 장치) filesystem rồi mở bằng bản địa (native / 네이티브) viewer hoặc hệ thống (system / 시스템) intent.

Tài liệu WebSquare mô tả luồng (flow / 흐름) dùng Cordova `FileTransfer` trong các hybrid setup cũ. Với dự án (project / 프로젝트) thực tế, plugin/API chính xác phụ thuộc Cordova/WebView/bản địa (native / 네이티브) ngăn xếp (stack / 스택) đang dùng.

Điểm bất biến là:

```text
web URL
→ native download capability
→ app-accessible file path
→ platform viewer / share intent
```

Không hard-code Android đường dẫn (path / 경로) rồi giả định iOS giống nhau.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **24. Download URL và đơn vị từ (token / 토큰) thời gian tồn tại (lifetime / 수명)** nối từ **23. Hybrid/mobile download khác trình duyệt (browser / 브라우저) download** sang **25. thất bại (failure / 실패) taxonomy cho tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 24. Download URL và đơn vị từ (token / 토큰) thời gian tồn tại (lifetime / 수명)

Nếu backend dùng signed URL hoặc temporary đơn vị từ (token / 토큰), thời gian sống phải đủ cho người dùng (user / 사용자) bắt đầu download nhưng không quá dài.

Hybrid app có thể background/resume làm yêu cầu (request / 요청) trễ. Vì vậy expiry, thử lại (retry / 재시도) và re-authentication phải được thiết kế như một máy trạng thái (state machine / 상태 머신), không chỉ là string URL.

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **24. Download URL và đơn vị từ (token / 토큰) thời gian tồn tại (lifetime / 수명)** đặt đầu vào cho **25. thất bại (failure / 실패) taxonomy cho tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인)**, rồi **26. khả năng quan sát (observability / 관측 가능성) cho tệp (file / 파일) transfer** mở rộng hệ quả hoặc giới hạn liên quan.

## 25. thất bại (failure / 실패) taxonomy cho tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인)

Một upload có thể thất bại (fail / 실패) ở nhiều lớp:

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

Nếu mọi lỗi đều thành “Upload failed”, môi trường vận hành (production / 운영 환경) hỗ trợ (support / 지원) sẽ rất chậm.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **25. thất bại (failure / 실패) taxonomy cho tệp (file / 파일) chuỗi xử lý (pipeline / 파이프라인)** đặt đầu vào cho **26. khả năng quan sát (observability / 관측 가능성) cho tệp (file / 파일) transfer**, rồi **27. bảo mật (security / 보안) checklist thực tế** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. khả năng quan sát (observability / 관측 가능성) cho tệp (file / 파일) transfer

Không log nhị phân (binary / 이진) content hoặc sensitive document. Log siêu dữ liệu (metadata / 메타데이터) đủ để dấu vết (trace / 추적):

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

Correlation ID phải đi xuyên máy khách (client / 클라이언트) → upload endpoint → lưu trữ (storage / 저장소) → nghiệp vụ (business / 비즈니스) dịch vụ (service / 서비스) nếu muốn điều tra sự cố (incident / 인시던트) nhanh.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **27. bảo mật (security / 보안) checklist thực tế** nối từ **26. khả năng quan sát (observability / 관측 가능성) cho tệp (file / 파일) transfer** sang **28. mẫu (pattern / 패턴): attachment staging**, vì cơ chế trước tạo đầu vào cho bước sau.

## 27. bảo mật (security / 보안) checklist thực tế

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

Nếu một câu trả lời là “thành phần (component / 컴포넌트) đã xử lý”, hãy kiểm tra lại trust ranh giới (boundary / 경계).

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **28. mẫu (pattern / 패턴): attachment staging** nối từ **27. bảo mật (security / 보안) checklist thực tế** sang **29. mẫu (pattern / 패턴): server-side report export**, vì cơ chế trước tạo đầu vào cho bước sau.

## 28. mẫu (pattern / 패턴): attachment staging

Một mẫu (pattern / 패턴) môi trường vận hành (production / 운영 환경) dễ lập luận (reasoning / 추론):

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

Mẫu (pattern / 패턴) này tách upload UX khỏi nghiệp vụ (business / 비즈니스) lần ghi nhận (commit / 커밋) nhưng vẫn có cleanup ngữ nghĩa (semantics / 의미론) rõ.

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **29. mẫu (pattern / 패턴): server-side report export** nối từ **28. mẫu (pattern / 패턴): attachment staging** sang **30. cấp cao (senior / 시니어) ghi chú (note / 노트): tệp (file / 파일) đường dẫn (path / 경로) không phải nghiệp vụ (business / 비즈니스) identifier**, vì cơ chế trước tạo đầu vào cho bước sau.

## 29. mẫu (pattern / 패턴): server-side report export

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

UI không bị freeze và yêu cầu (request / 요청) không cần giữ HTTP liên kết (connection / 연결) quá lâu. Đổi lại cần job trạng thái (state / 상태), expiry và cleanup.

> **Nối mạch:** Ở chặng này của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **29. mẫu (pattern / 패턴): server-side report export** đặt đầu vào cho **30. cấp cao (senior / 시니어) ghi chú (note / 노트): tệp (file / 파일) đường dẫn (path / 경로) không phải nghiệp vụ (business / 비즈니스) identifier**, rồi **31. Kết nối với các chapter khác** mở rộng hệ quả hoặc giới hạn liên quan.

## 30. cấp cao (senior / 시니어) ghi chú (note / 노트): tệp (file / 파일) đường dẫn (path / 경로) không phải nghiệp vụ (business / 비즈니스) identifier

Đừng truyền vật lý (physical / 물리적) đường dẫn (path / 경로) khắp hệ thống như `/data/upload/2026/09/a.pdf` rồi coi nó là định danh (identity / 식별자). lưu trữ (storage / 저장소) bố cục (layout / 레이아웃) có thể đổi.

Ưu tiên opaque tệp (file / 파일) ID/lưu trữ (storage / 저장소) key:

```text
business record → attachmentId → storage service → physical location
```

Điều này cho phép migrate filesystem sang đối tượng (object / 객체) lưu trữ (storage / 저장소) mà không đổi nghiệp vụ (business / 비즈니스) đặc tả hợp đồng (contract / 계약).

> **Nối mạch:** Đặt trong câu hỏi lớn của **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **30. cấp cao (senior / 시니어) ghi chú (note / 노트): tệp (file / 파일) đường dẫn (path / 경로) không phải nghiệp vụ (business / 비즈니스) identifier** đặt đầu vào cho **31. Kết nối với các chapter khác**, rồi **32. Mastery checkpoint** mở rộng hệ quả hoặc giới hạn liên quan.

## 31. Kết nối với các chapter khác

Tệp (file / 파일)/Excel chuỗi xử lý (pipeline / 파이프라인) nối trực tiếp với [05 — GridView & CRUD](05_gridview_crud_patterns.md), [12 — Build, Configuration & Deployment](12_build_config_deployment.md), [13 — GridView Editing & Identity](13_gridview_editing_identity_internals.md) và [15 — Backend Contract, Transaction & Concurrency](15_backend_contract_transaction_concurrency.md).

Hybrid/mobile download được đào sâu ở [18 — Hybrid App, WebView & Native Bridge](18_hybrid_webview_native_bridge.md). môi trường vận hành (production / 운영 환경) tracing cho upload/export job được nối với [19 — Observability & Incident Response](19_observability_incident_response.md).

> **Nối mạch:** Trong **17 — tệp (file / 파일), Excel, Upload & Download chuỗi xử lý (pipeline / 파이프라인)**, **32. Mastery checkpoint** nối từ **31. Kết nối với các chapter khác** sang  Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## 32. Mastery checkpoint

Bạn đã master chapter này khi có thể nhìn một yêu cầu “upload tệp (file / 파일) rồi save”, “import Excel vào grid” hoặc “export toàn bộ dữ liệu” và tự tách được vận chuyển (transport / 전송), parsing, kiểm tra hợp lệ (validation / 검증), lưu trữ (storage / 저장소), nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션), authorization, consistency, bộ nhớ (memory / 메모리) và cleanup; đồng thời biết phần nào thuộc WebSquare thành phần (component / 컴포넌트)/cấu hình (config / 설정) và phần nào bắt buộc phải được giải quyết ở backend/nền tảng (platform / 플랫폼).

> **Bàn giao:** Sau **32. Mastery checkpoint**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
