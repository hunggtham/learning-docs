# 03 — DataCollection & Submission

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **03 — DataCollection & Submission**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Tách dữ liệu khỏi thành phần (component / 컴포넌트)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. DataMap: bản ghi (record / 레코드) có lược đồ (schema / 스키마)** để đối chiếu nhận định với dữ liệu và nguồn. Mạch này nối DataCollection với Submission, binding và request lifecycle, để phân biệt model dữ liệu phía client với giao dịch phía server.

## 1. Tách dữ liệu khỏi thành phần (component / 컴포넌트)

Một trong những ý tưởng quan trọng nhất của WebSquare là không bắt mọi thành phần (component / 컴포넌트) tự giữ nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터). khung phần mềm (framework / 프레임워크) cung cấp **DataCollection**, một nhóm đối tượng (object / 객체) dữ liệu được tạo trong trình duyệt (browser / 브라우저) bộ nhớ (memory / 메모리) để màn hình dùng chung.

Ba loại thường gặp là:

`DataMap` — dữ liệu dạng một bản ghi (record / 레코드) hoặc key/giá trị (value / 값).

`DataList` — dữ liệu nhiều dòng, gần với bảng (table / 테이블)/danh sách (list / 목록).

`LinkedDataList` — một view dẫn xuất từ DataList, thường dùng cho filter/sort mà không cần coi kết quả đó là một nghiệp vụ (business / 비즈니스) dataset hoàn toàn mới.

Mô hình tư duy (mental model / 사고 모델):

```text
server data
    ↓
DataCollection
    ↓
binding / script
    ↓
components
```

Nếu thành phần (component / 컴포넌트) chỉ là view, mã (code / 코드) nghiệp vụ nên ưu tiên thao tác mô hình (model / 모델) thay vì cố đọc từng cell UI để dựng lại dữ liệu.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **1. Tách dữ liệu khỏi thành phần (component / 컴포넌트)** nêu điều cần giải thích; **2. DataMap: bản ghi (record / 레코드) có lược đồ (schema / 스키마)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. DataList: bảng (table / 테이블) mô hình (model / 모델) phía máy khách (client / 클라이언트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. DataMap: bản ghi (record / 레코드) có lược đồ (schema / 스키마)

Một `DataMap` thường có key definition và giá trị (value / 값) tương ứng. Nó phù hợp cho điều kiện tìm kiếm, form chi tiết hoặc yêu cầu (request / 요청) parameter dạng một đối tượng (object / 객체).

Ví dụ conceptual:

```text
dmSearch
 ├─ userId
 ├─ userName
 ├─ fromDate
 └─ toDate
```

Nếu các đầu vào (input / 입력) bind vào `dmSearch`, luồng (flow / 흐름) tìm kiếm trở nên dễ hiểu:

```text
User nhập điều kiện
→ dmSearch thay đổi
→ sbmSearch tham chiếu dmSearch
→ request được gửi
```

Điểm mạnh không chỉ là mã (code / 코드) ngắn hơn. Nó tạo một ranh giới (boundary / 경계) rõ giữa UI trạng thái (state / 상태) và yêu cầu (request / 요청) trạng thái (state / 상태).

> **Chuyển mạch:** DataMap giữ record theo schema; DataList mở record thành collection có ordering và selection. Row status tiếp theo biến mutation của từng row thành state machine có thể submit và rollback.

## 3. DataList: bảng (table / 테이블) mô hình (model / 모델) phía máy khách (client / 클라이언트)

`DataList` giữ nhiều row và cung cấp API như `getRowCount()`, `getCellData(rowIndex, colId)`, `getRowJSON(rowIndex)` và `getAllJSON(...)`.

```javascript
var count = dlUser.getRowCount();

for (var i = 0; i < count; i++) {
    var id = dlUser.getCellData(i, "USER_ID");
    console.log(id);
}
```

Nhưng DataList không nên bị hiểu đơn giản là JavaScript Array. Nó còn giữ siêu dữ liệu (metadata / 메타데이터) và row trạng thái (state / 상태) phục vụ binding, CRUD và Submission.

> **Chuyển mạch:** DataList giữ client-side model; row status biến mỗi row thành state machine, nên delete tiếp theo có thể là pending operation thay vì biến mất ngay.

## 4. Row status là một mini máy trạng thái (state machine / 상태 머신)

DataList có thể theo dõi trạng thái của từng row. Trong WebSquare5 SP5, các status thường gặp gồm:

```text
R = read / unchanged
U = updated
C = created / inserted
D = deleted
V = inserted rồi deleted
```

`getRowStatus(rowIndex)` cho phép kiểm tra trạng thái hiện tại. Một row không chỉ chứa dữ liệu (data / 데이터); nó còn chứa lịch sử thay đổi đủ để hệ thống biết row nào cần insert/cập nhật (update / 업데이트)/delete khi save.

```javascript
for (var i = 0; i < dlUser.getRowCount(); i++) {
    var status = dlUser.getRowStatus(i);

    if (status !== "R") {
        console.log("changed row", i, status);
    }
}
```

Cấp cao (senior / 시니어) ghi chú (note / 노트): đừng tự tạo thêm cột `STATUS` chỉ để duplicate row status khung phần mềm (framework / 프레임워크) nếu không có nghiệp vụ (business / 비즈니스) reason. Nếu máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) cần một status trường dữ liệu (field / 필드) tường minh (explicit / 명시적) thì ánh xạ (mapping / 매핑) có thể cần, nhưng phải phân biệt nghiệp vụ (business / 비즈니스) status với máy khách (client / 클라이언트) row trạng thái (state / 상태).

> **Chuyển mạch:** Pending delete giữ row để rollback và submit; mutation tiếp theo phải phân biệt insert, remove khỏi view và delete khỏi persistence.

## 5. Delete không phải lúc nào cũng biến mất ngay

Trong CRUD grid, một row bị delete có thể được đánh dấu `D` nhưng vẫn tồn tại trong mô hình (model / 모델) để Submission biết phải gửi delete instruction. GridView có option để ẩn row đã delete, nhưng mô hình (model / 모델) vẫn có thể giữ nó.

Điều này giải thích bug kiểu “UI chỉ còn 9 dòng nhưng API DataList vẫn thấy 10”. Câu hỏi đúng là API đang trả **visible rows**, **all rows**, hay **rows bao gồm delete trạng thái (state / 상태)**. Khi export, validate hoặc count, phải chọn ngữ nghĩa (semantics / 의미론) phù hợp.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **5. Delete không phải lúc nào cũng biến mất ngay** nêu điều cần giải thích; **6. dữ liệu (data / 데이터) mutation cần phân biệt insert/remove/delete** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. dữ liệu (data / 데이터) mutation cần phân biệt insert/remove/delete

Một khung phần mềm (framework / 프레임워크) mô hình dữ liệu (data model / 데이터 모델) thường phân biệt insert để tạo row mới và đánh dấu trạng thái (state / 상태) mới, cập nhật (update / 업데이트) để sửa row hiện có, delete để đánh dấu row cho máy chủ (server / 서버) lần ghi nhận (commit / 커밋), còn remove có thể chỉ loại row khỏi máy khách (client / 클라이언트) mô hình (model / 모델) mà không mang cùng ngữ nghĩa (semantic / 의미적) delete, tùy API/bản dựng (build / 빌드).

Do tên API giữa generation/bản dựng (build / 빌드) có thể khác hoặc có option khác nhau, hãy tra tham chiếu (reference / 참조) đúng bản dựng (build / 빌드) trước khi chọn. Điều quan trọng là lập luận (reasoning / 추론): **bạn muốn thay UI danh sách (list / 목록), thay máy khách (client / 클라이언트) mô hình (model / 모델), hay phát sinh một delete thao tác (operation / 연산) cần máy chủ (server / 서버) lần ghi nhận (commit / 커밋)?**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **6. dữ liệu (data / 데이터) mutation cần phân biệt insert/remove/delete** nêu điều cần giải thích; **7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **8. Submission là communication description, không phải nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới

Nếu một màn hình cần filter/sort một DataList, tạo bản bản sao (copy / 복사) thủ công bằng vòng lặp (loop / 루프) thường làm mất row định danh (identity / 식별자) và status relationship. LinkedDataList tồn tại để biểu diễn một view dẫn xuất.

```text
source DataList
     │
     ├─ filter
     └─ sort
     │
     ▼
LinkedDataList
```

Không nên mặc định coi LinkedDataList là một nguồn chuẩn (source of truth / 정본) độc lập. Hãy hiểu quan hệ (relation / 관계) của nó với nguồn (source / 소스) trước khi cập nhật (update / 업데이트)/save.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **7. LinkedDataList: derived view, không nhất thiết là dữ liệu mới** nêu điều cần giải thích; **8. Submission là communication description, không phải nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. tham chiếu (reference / 참조) và mục tiêu (target / 대상) là đặc tả hợp đồng (contract / 계약) dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Submission là communication description, không phải nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션)

WebSquare `Submission` mô tả client-server communication: hành động (action / 동작)/endpoint, yêu cầu (request / 요청) tham chiếu (reference / 참조), phản hồi (response / 응답) mục tiêu (target / 대상), chế độ (mode / 모드) và callback vòng đời (lifecycle / 생명주기).

```text
dmSearch
   │ reference
   ▼
sbmSearch
   │ HTTP
   ▼
server
   │ response
   ▼
dlUser target
   │ binding
   ▼
GridView
```

Submission giúp chuẩn hóa serialization và ánh xạ (mapping / 매핑) nhưng nó không tự biến nhiều HTTP lời gọi (call / 호출) thành một cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션). giao dịch (transaction / 트랜잭션) thật nằm ở máy chủ (server / 서버).

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **8. Submission là communication description, không phải nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션)** nêu điều cần giải thích; **9. tham chiếu (reference / 참조) và mục tiêu (target / 대상) là đặc tả hợp đồng (contract / 계약) dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. Execute Submission và async lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. tham chiếu (reference / 참조) và mục tiêu (target / 대상) là đặc tả hợp đồng (contract / 계약) dữ liệu

**tham chiếu (reference / 참조)** biểu diễn máy khách (client / 클라이언트) dữ liệu (data / 데이터) được serialize thành yêu cầu (request / 요청). **mục tiêu (target / 대상)** biểu diễn máy khách (client / 클라이언트) mô hình (model / 모델) nhận phản hồi (response / 응답).

Nếu yêu cầu (request / 요청) chạy thành công nhưng Grid rỗng, hãy tách chuỗi xử lý (pipeline / 파이프라인):

```text
HTTP response có data?
        ↓
response mapping có đúng path/schema?
        ↓
Target DataList có data?
        ↓
GridView có bind đúng DataList?
```

Đừng nhảy thẳng từ “mạng (network / 네트워크) 200” sang “Grid bug”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **9. tham chiếu (reference / 참조) và mục tiêu (target / 대상) là đặc tả hợp đồng (contract / 계약) dữ liệu** nêu điều cần giải thích; **10. Execute Submission và async lập luận (reasoning / 추론)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. Success HTTP không đồng nghĩa success nghiệp vụ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Execute Submission và async lập luận (reasoning / 추론)

Một cách thường gặp để chạy Submission là:

```javascript
$p.executeSubmission(sbmSearchUser);
```

Nếu chế độ (mode / 모드) là asynchronous, dòng tiếp theo không chờ phản hồi (response / 응답).

```javascript
$p.executeSubmission(sbmSearchUser);
console.log(dlUser.getRowCount()); // không được giả định response đã về
```

Mô hình tư duy (mental model / 사고 모델) đúng:

```text
executeSubmission()
→ request scheduled/sent
→ current JS handler tiếp tục và kết thúc
→ response về sau
→ submitdone hoặc submiterror chạy
```

Nếu mã (code / 코드) cần dùng phản hồi (response / 응답), đặt nó ở vòng đời (lifecycle / 생명주기) callback tương ứng hoặc trong hàm (function / 함수) được callback gọi.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **11. Success HTTP không đồng nghĩa success nghiệp vụ** tiếp nhận điểm tựa từ **10. Execute Submission và async lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. lỗi (error / 오류) đường dẫn (path / 경로) phải là first-class đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Success HTTP không đồng nghĩa success nghiệp vụ

Máy chủ (server / 서버) có thể trả HTTP 200 nhưng payload báo nghiệp vụ (business / 비즈니스) thất bại (failure / 실패), ví dụ duplicate key, kiểm tra hợp lệ (validation / 검증) thất bại (fail / 실패) hoặc insufficient nghiệp vụ (business / 비즈니스) permission.

Cần phân biệt ít nhất ba lớp kết quả (result / 결과):

```text
transport result
HTTP/network có thành công không?

protocol/application result
payload có đúng schema không?

business result
operation có được chấp nhận không?
```

Một handler `submitdone` không nên mặc định hiển thị “Save success” chỉ vì vận chuyển (transport / 전송) không lỗi. Nó phải đọc nghiệp vụ (business / 비즈니스) kết quả (result / 결과) đặc tả hợp đồng (contract / 계약).

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **11. Success HTTP không đồng nghĩa success nghiệp vụ** xác định đầu vào; **12. lỗi (error / 오류) đường dẫn (path / 경로) phải là first-class đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Race điều kiện (condition / 조건) giữa các tìm kiếm (search / 검색) yêu cầu (request / 요청)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. lỗi (error / 오류) đường dẫn (path / 경로) phải là first-class đường dẫn (path / 경로)

Nhiều màn hình chỉ viết happy đường dẫn (path / 경로):

```javascript
scwin.sbmSave_submitdone = function () {
    alert("Saved");
};
```

Môi trường vận hành (production / 운영 환경) luồng (flow / 흐름) phải nghĩ đến hết thời gian chờ (timeout / 타임아웃), 401/403, 500, mạng (network / 네트워크) mất mát (loss / 손실), malformed payload, duplicate click và máy chủ (server / 서버) nghiệp vụ (business / 비즈니스) thất bại (failure / 실패). Nếu UI set loading trạng thái (state / 상태) trước yêu cầu (request / 요청) thì mọi terminal đường dẫn (path / 경로) phải reset trạng thái (state / 상태). Nếu chỉ reset ở success, người dùng (user / 사용자) có thể bị kẹt nút Save sau lỗi (error / 오류).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **12. lỗi (error / 오류) đường dẫn (path / 경로) phải là first-class đường dẫn (path / 경로)** xác định đầu vào; **13. Race điều kiện (condition / 조건) giữa các tìm kiếm (search / 검색) yêu cầu (request / 요청)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **14. truy vấn (query / 쿼리) luồng (flow / 흐름) và Save luồng (flow / 흐름) nên tách** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Race điều kiện (condition / 조건) giữa các tìm kiếm (search / 검색) yêu cầu (request / 요청)

Một trường hợp (case / 사례) phổ biến là yêu cầu (request / 요청) A được gửi trước nhưng chậm, yêu cầu (request / 요청) B được gửi sau nhưng nhanh. B hiển thị trước, rồi A về sau và ghi đè kết quả (result / 결과). UI cuối cùng không còn phản ánh người dùng (user / 사용자) intent mới nhất.

Giải pháp tùy khung phần mềm (framework / 프레임워크)/bản dựng (build / 빌드) và API: abort yêu cầu (request / 요청) cũ, disable new tìm kiếm (search / 검색) khi yêu cầu (request / 요청) đang chạy, hoặc attach yêu cầu (request / 요청) định danh (identity / 식별자) và bỏ phản hồi (response / 응답) stale. WebSquare có cơ chế (mechanism / 메커니즘) abort Submission ở các API/bản dựng (build / 빌드) tương ứng, nhưng first principle vẫn là: **asynchronous phản hồi (response / 응답) không đảm bảo về đúng thứ tự người dùng (user / 사용자) intent**.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **13. Race điều kiện (condition / 조건) giữa các tìm kiếm (search / 검색) yêu cầu (request / 요청)** xác định đầu vào; **14. truy vấn (query / 쿼리) luồng (flow / 흐름) và Save luồng (flow / 흐름) nên tách** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **15. CRUD screen mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. truy vấn (query / 쿼리) luồng (flow / 흐름) và Save luồng (flow / 흐름) nên tách

Tìm kiếm (search / 검색)/truy vấn (query / 쿼리) thường read-only, dễ thử lại (retry / 재시도)/cancel và phản hồi (response / 응답) thường thay kết quả (result / 결과) danh sách (list / 목록). Save là mutation, cần kiểm tra hợp lệ (validation / 검증), duplicate protection, tính đồng thời (concurrency / 동시성) handling và xử lý partial/nghiệp vụ (business / 비즈니스) thất bại (failure / 실패) cẩn thận.

Đừng dùng cùng một helper mơ hồ cho mọi Submission nếu nó che mất ngữ nghĩa (semantics / 의미론) này.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **14. truy vấn (query / 쿼리) luồng (flow / 흐름) và Save luồng (flow / 흐름) nên tách** xác định đầu vào; **15. CRUD screen mẫu (pattern / 패턴)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **16. Dirty check** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. CRUD screen mẫu (pattern / 패턴)

Một luồng (flow / 흐름) enterprise điển hình:

```text
Search
  ↓
dlUser = server result, rowStatus R
  ↓
User edits Grid
  ↓
rowStatus U/C/D
  ↓
Validate changed rows
  ↓
Save Submission
  ↓
server transaction
  ↓
success
  ↓
re-query hoặc normalize client state
```

Sau save, **re-query** lấy lại dữ liệu chuẩn gốc (canonical / 정본) từ máy chủ (server / 서버) và an toàn khi máy chủ (server / 서버) có trigger/default/normalization. **cục bộ (local / 로컬) lần ghi nhận (commit / 커밋)/reset** giữ dữ liệu (data / 데이터) hiện tại rồi reset row trạng thái (state / 상태), nhanh hơn nhưng dễ lệch nếu máy chủ (server / 서버) biến đổi dữ liệu. Chọn dựa trên đặc tả hợp đồng (contract / 계약), không theo thói quen.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **16. Dirty check** tiếp nhận điểm tựa từ **15. CRUD screen mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Validate changed rows, không nhất thiết validate toàn bộ dataset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Dirty check

Trước khi save, nên biết có row thay đổi hay không. Có thể duyệt row status hoặc dùng API hỗ trợ của bản dựng (build / 빌드).

```javascript
scwin.hasChangedRows = function () {
    var count = dlUser.getRowCount();

    for (var i = 0; i < count; i++) {
        if (dlUser.getRowStatus(i) !== "R") {
            return true;
        }
    }

    return false;
};
```

Nhưng cần hiểu ngữ nghĩa (semantics / 의미론) của deleted row và filtered view. Nếu `getRowCount()` không bao gồm một loại row trong cấu hình (configuration / 구성) cụ thể, dirty check có thể sai. Kiểm tra API tham chiếu (reference / 참조)/bản dựng (build / 빌드) khi hiện thực (implementation / 구현) cần môi trường vận hành (production / 운영 환경) guarantee.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **17. Validate changed rows, không nhất thiết validate toàn bộ dataset** tiếp nhận điểm tựa từ **16. Dirty check** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Validate changed rows, không nhất thiết validate toàn bộ dataset

Một Grid 10.000 row nhưng người dùng (user / 사용자) chỉ sửa 2 row. Validate mọi cell mọi row trước save có thể lãng phí và tạo UX kém. Nếu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) cho phép, chỉ validate row trạng thái (state / 상태) `C`/`U` và các row `D` cần delete ràng buộc (constraint / 제약조건).

```javascript
scwin.validateChanges = function () {
    var count = dlUser.getRowCount();

    for (var i = 0; i < count; i++) {
        var status = dlUser.getRowStatus(i);

        if (status === "C" || status === "U") {
            if (!scwin.validateUserRow(i)) {
                return false;
            }
        }
    }

    return true;
};
```

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **18. máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적)** tiếp nhận điểm tựa từ **17. Validate changed rows, không nhất thiết validate toàn bộ dataset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Empty string, null và undefined** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적)

Máy khách (client / 클라이언트) không nên gửi “mọi thứ có trong DataList” rồi để máy chủ (server / 서버) đoán. đặc tả hợp đồng (contract / 계약) cần xác định trường dữ liệu (field / 필드) required/writable/server-owned, row status encode ra sao, null/empty ngữ nghĩa (semantics / 의미론), number/date format và lỗi (error / 오류) payload shape.

Nếu máy khách (client / 클라이언트) gửi cả trường dữ liệu (field / 필드) không được phép sửa, máy chủ (server / 서버) vẫn phải whitelist/validate. Không tin payload chỉ vì nó do WebSquare tạo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **19. Empty string, null và undefined** tiếp nhận điểm tựa từ **18. máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약) phải tường minh (explicit / 명시적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Date và number không nên đi qua UI format mơ hồ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Empty string, null và undefined

Enterprise bug rất hay nằm ở ngữ nghĩa (semantic / 의미적) rỗng.

```text
""        = giá trị rỗng?
null      = không có giá trị?
undefined = field không tồn tại/không được gửi?
```

JavaScript, serializer, WebSquare DataCollection và máy chủ (server / 서버) binding khung phần mềm (framework / 프레임워크) có thể xử lý khác nhau. Với cập nhật (update / 업데이트) API, `field absent` và `field: null` thường mang ý nghĩa khác. Đừng normalize tất cả về `""` chỉ để “dễ”. đặc tả hợp đồng (contract / 계약) phải quyết định.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **20. Date và number không nên đi qua UI format mơ hồ** tiếp nhận điểm tựa từ **19. Empty string, null và undefined** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Submission so với AJAX thấp hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Date và number không nên đi qua UI format mơ hồ

Một số thành phần (component / 컴포넌트) có display/edit format. dữ liệu (data / 데이터) gửi máy chủ (server / 서버) nên có chuẩn gốc (canonical / 정본) biểu diễn (representation / 표현).

```text
UI: 2026/09/22
model: 20260922
hoặc API contract: 2026-09-22
```

Chọn một biểu diễn (representation / 표현) ổn định ở API ranh giới (boundary / 경계). Đừng parse locale-formatted string ở máy chủ (server / 서버) nếu có thể tránh.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **21. Submission so với AJAX thấp hơn** tiếp nhận điểm tựa từ **20. Date và number không nên đi qua UI format mơ hồ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Workflow và orchestration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Submission so với AJAX thấp hơn

WebSquare cũng có AJAX utility cho trường hợp cần điều khiển (control / 제어) yêu cầu (request / 요청)/phản hồi (response / 응답) ở mức thấp hơn. Nhưng đừng dùng AJAX chỉ vì quen `fetch`/jQuery.

Submission có lợi khi luồng (flow / 흐름) phù hợp DataCollection ánh xạ (mapping / 매핑), khung phần mềm (framework / 프레임워크) vòng đời (lifecycle / 생명주기) và convention của dự án (project / 프로젝트). AJAX phù hợp khi yêu cầu (request / 요청) không khớp mô hình (model / 모델) đó, cần raw payload/stream/special header hoặc tích hợp (integration / 통합) đặc biệt. quyết định (decision / 결정) nên dựa vào lớp trừu tượng (abstraction / 추상화) fit, không dựa vào sở thích cá nhân.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **21. Submission so với AJAX thấp hơn** xác định đầu vào; **22. Workflow và orchestration** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **23. hiệu năng (performance / 성능): payload trước, Grid sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Workflow và orchestration

Nếu nhiều Submission phụ thuộc thứ tự, dự án (project / 프로젝트) có thể dùng workflow hoặc orchestration bằng script.

```text
loadCodeList
   ↓
loadUserDetail
   ↓
loadPermission
```

Sai mẫu (pattern / 패턴) là fire cả ba cùng lúc rồi dùng `setTimeout` để hy vọng thứ tự. Nếu yêu cầu (request / 요청) độc lập, chạy song song có thể nhanh hơn. Nếu có phụ thuộc (dependency / 의존성), encode phụ thuộc (dependency / 의존성) tường minh (explicit / 명시적).

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **22. Workflow và orchestration** xác định đầu vào; **23. hiệu năng (performance / 성능): payload trước, Grid sau** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **24. ranh giới bảo mật (security boundary / 보안 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. hiệu năng (performance / 성능): payload trước, Grid sau

Khi màn hình chậm, tách độ trễ (latency / 지연 시간):

```text
T_total = request_wait
        + response_transfer
        + parse/mapping
        + DataCollection update
        + Grid rendering
        + script side effects
```

Nếu mạng (network / 네트워크) cho thấy phản hồi (response / 응답) mất 3 giây, tối ưu Grid không giải quyết chính. Nếu phản hồi (response / 응답) 50 ms nhưng UI freeze 2 giây với 50.000 row, vấn đề nằm máy khách (client / 클라이언트) rendering/dữ liệu (data / 데이터) processing. bằng chứng (evidence / 증거) trước tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **23. hiệu năng (performance / 성능): payload trước, Grid sau** đã nêu tiêu chí phân biệt, còn **24. ranh giới bảo mật (security boundary / 보안 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **25. Debugging Submission theo chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. ranh giới bảo mật (security boundary / 보안 경계)

DataCollection nằm trong trình duyệt (browser / 브라우저) bộ nhớ (memory / 메모리). người dùng (user / 사용자) có DevTools có thể đọc/sửa máy khách (client / 클라이언트) trạng thái (state / 상태).

```text
DataMap/DataList ≠ trusted storage
rowStatus ≠ authorization proof
hidden column ≠ secret
readOnly field ≠ immutable business data
```

Máy chủ (server / 서버) phải xác thực định danh (identity / 식별자), authorization, quyền sở hữu (ownership / 소유권) và bất biến (invariant / 불변식) trước khi lần ghi nhận (commit / 커밋).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **24. ranh giới bảo mật (security boundary / 보안 경계)** đã nêu tiêu chí phân biệt, còn **25. Debugging Submission theo chuỗi xử lý (pipeline / 파이프라인)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **26. submitdone và submiterror: hiểu đúng vận chuyển (transport / 전송) ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Debugging Submission theo chuỗi xử lý (pipeline / 파이프라인)

Khi Save thất bại, kiểm tra theo chuỗi xử lý (pipeline / 파이프라인): handler Save có chạy, kiểm tra hợp lệ (validation / 검증) có pass, DataCollection trước submit chứa gì, tham chiếu (reference / 참조) trỏ đúng đối tượng (object / 객체) không, yêu cầu (request / 요청) payload thực tế là gì, HTTP status/header/body là gì, nghiệp vụ (business / 비즈니스) kết quả (result / 결과) là gì, mục tiêu (target / 대상) ánh xạ (mapping / 매핑) sau phản hồi (response / 응답) ra sao, callback nào chạy và cuối cùng có callback khác ghi đè UI không.

Đi theo thứ tự này tốt hơn việc thêm `alert()` ngẫu nhiên.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **25. Debugging Submission theo chuỗi xử lý (pipeline / 파이프라인)** đã nêu tiêu chí phân biệt, còn **26. submitdone và submiterror: hiểu đúng vận chuyển (transport / 전송) ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **27. Async là default lập luận (reasoning / 추론); sync là tính tương thích (compatibility / 호환성) debt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. `submitdone` và `submiterror`: hiểu đúng vận chuyển (transport / 전송) ranh giới (boundary / 경계)

Tài liệu SP5 định nghĩa `submitdone(e)` chạy khi phản hồi (response / 응답) status mã (code / 코드) nằm trong vùng thành công, còn `submiterror(e)` chạy khi status nhỏ hơn 200 hoặc từ 300 trở lên. Điều này tạo một ranh giới (boundary / 경계) rất cụ thể: hai callback này trước hết phản ánh **HTTP/Submission vận chuyển (transport / 전송) kết quả (outcome / 결과)**, không phải nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과).

Sự kiện (event / 이벤트) đối tượng (object / 객체) của `submitdone` có các dữ liệu như `responseStatusCode`, `responseHeaders`, `responseText`, `responseBody` và, khi phản hồi (response / 응답) `Content-Type` chứa JSON, `responseJSON`. Vì vậy mã (code / 코드) môi trường vận hành (production / 운영 환경) không cần parse cùng một phản hồi (response / 응답) theo ba cách ngẫu nhiên. Hãy chọn biểu diễn (representation / 표현) dựa trên media kiểu (type / 타입) và đặc tả hợp đồng (contract / 계약).

```javascript
scwin.sbmSave_submitdone = function (e) {
    var result = e.responseJSON;

    if (!result || result.success !== true) {
        scwin.showBusinessError(result);
        return;
    }

    scwin.afterSave(result);
};
```

Ví dụ trên chỉ là đặc tả hợp đồng (contract / 계약) minh họa; key `success` không phải chuẩn WebSquare. Điểm cần nhớ là WebSquare quyết định vận chuyển (transport / 전송) callback, còn ứng dụng (application / 애플리케이션) quyết định nghiệp vụ (business / 비즈니스) success.

`submiterror(e)` cũng có `requestBody` và `responseText` ở SP5. Đây là bằng chứng (evidence / 증거) hữu ích khi gỡ lỗi (debug / 디버그) nhưng có thể chứa PII hoặc credential-like dữ liệu (data / 데이터). Không dump toàn bộ sự kiện (event / 이벤트) vào môi trường vận hành (production / 운영 환경) log chỉ vì nó tiện.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **26. submitdone và submiterror: hiểu đúng vận chuyển (transport / 전송) ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **27. Async là default lập luận (reasoning / 추론); sync là tính tương thích (compatibility / 호환성) debt** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **28. getAllJSON() không chỉ là “convert DataList thành Array”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Async là default lập luận (reasoning / 추론); sync là tính tương thích (compatibility / 호환성) debt

SP5 Development Guide khuyến nghị Submission bất đồng bộ (asynchronous / 비동기) và có cấu hình (configuration / 구성) cảnh báo khi dùng synchronous chế độ (mode / 모드). Lý do không chỉ là style: synchronous mạng (network / 네트워크) công việc (work / 작업) khóa thực thi (execution / 실행)/UI đường dẫn (path / 경로), làm trình duyệt (browser / 브라우저) kém responsive và khiến điều khiển (control / 제어) luồng (flow / 흐름) phụ thuộc một hành vi (behavior / 동작) mà nền tảng (platform / 플랫폼) web hiện đại tránh.

Khi gặp dự án (project / 프로젝트) legacy dùng sync Submission, đừng đổi toàn bộ sang async bằng search-replace. Sync mã (code / 코드) thường vô tình dựa vào bất biến (invariant / 불변식):

```text
executeSubmission()
→ response đã map xong
→ dòng kế tiếp đọc target
```

Khi chuyển async, bất biến (invariant / 불변식) đó biến mất. di chuyển (migration / 마이그레이션) phải tìm mọi read-after-submit, chuyển tiếp trạng thái (state transition / 상태 전이), popup close, điều hướng (navigation / 내비게이션) và lỗi (error / 오류) đường dẫn (path / 경로) phụ thuộc timing cũ rồi chuyển chúng vào callback/orchestration tường minh (explicit / 명시적).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **28. getAllJSON() không chỉ là “convert DataList thành Array”** tiếp nhận điểm tựa từ **27. Async là default lập luận (reasoning / 추론); sync là tính tương thích (compatibility / 호환성) debt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Filtered chỉ mục (index / 인덱스) và real chỉ mục (index / 인덱스) là hai coordinate hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. `getAllJSON()` không chỉ là “convert DataList thành Array”

SP5 cho phép `getAllJSON()` trả toàn bộ DataList và có option liên quan row-status dữ liệu (data / 데이터). Điều này củng cố mô hình tư duy (mental model / 사고 모델) rằng DataList gồm **nghiệp vụ (business / 비즈니스) cells + khung phần mềm (framework / 프레임워크) siêu dữ liệu (metadata / 메타데이터)**, không phải chỉ một array đối tượng (object / 객체).

Khi API máy chủ (server / 서버) chỉ cần nghiệp vụ (business / 비즈니스) dữ liệu (data / 데이터), đừng vô thức gửi siêu dữ liệu (metadata / 메타데이터). Khi save đặc tả hợp đồng (contract / 계약) cần thay đổi (change / 변경) ngữ nghĩa (semantics / 의미론), đừng vô thức bỏ siêu dữ liệu (metadata / 메타데이터) rồi tự đoán lại thay đổi (change / 변경) bằng cách compare đối tượng (object / 객체). Hãy chọn API theo ý nghĩa dữ liệu cần lấy.

Các API như `getInsertedJSON()`, `getUpdatedJSON()`, `getModifiedJSON()` và `getOnlyDeletedJSON()` tồn tại ở các SP5 bản dựng (build / 빌드) tương ứng để lấy tập thay đổi theo ngữ nghĩa (semantic / 의미적) rõ hơn. Chúng hữu ích khi save changed rows, nhưng chính xác (exact / 정확한) option và treatment của null/status phải được đối chiếu bản dựng (build / 빌드) đang chạy.

Mô hình tư duy (mental model / 사고 모델):

```text
getAllJSON       → snapshot rộng
getInsertedJSON  → rows mới
getUpdatedJSON   → rows đã sửa
getModifiedJSON  → change set theo contract API
getOnlyDeletedJSON → delete set
```

Đừng chọn API vì tên “có vẻ đúng”; kiểm tra xem deleted row, rowStatus và null conversion được trả như thế nào trong bản dựng (build / 빌드) thật.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **29. Filtered chỉ mục (index / 인덱스) và real chỉ mục (index / 인덱스) là hai coordinate hệ thống (system / 시스템)** tiếp nhận điểm tựa từ **28. getAllJSON() không chỉ là “convert DataList thành Array”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Null handling đã trở thành một phần version-sensitive của DataList** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Filtered chỉ mục (index / 인덱스) và real chỉ mục (index / 인덱스) là hai coordinate hệ thống (system / 시스템)

Khi DataList/LinkedDataList bị filter, vị trí người dùng thấy có thể khác chỉ mục (index / 인덱스) thật của nguồn (source / 소스). SP5 có API như `getFilteredRowIndex(realRowIndex)` để ánh xạ chỉ mục (index / 인덱스) thật sang vị trí sau filter.

Đây không phải detail nhỏ. Nếu mã (code / 코드) giữ `selectedIndex = 5`, sau filter/sort thì “5” có thể chỉ là **tọa độ của view**, không còn là định danh (identity / 식별자) của nghiệp vụ (business / 비즈니스) row.

```text
business key = identity ổn định
real row index = vị trí trong source model
filtered/view index = vị trí trong projection hiện tại
```

Cấp cao (senior / 시니어) mã (code / 코드) ưu tiên nghiệp vụ (business / 비즈니스) key cho thao tác (operation / 연산) sống lâu hơn một tương tác (interaction / 상호작용) tức thời. chỉ mục (index / 인덱스) chỉ nên được giữ ngắn hạn trong đúng coordinate hệ thống (system / 시스템) của nó.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **30. Null handling đã trở thành một phần version-sensitive của DataList** tiếp nhận điểm tựa từ **29. Filtered chỉ mục (index / 인덱스) và real chỉ mục (index / 인덱스) là hai coordinate hệ thống (system / 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. dữ liệu (data / 데이터) kiểu (type / 타입) coercion cũng là đặc tả hợp đồng (contract / 계약), không phải convenience vô hại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Null handling đã trở thành một phần version-sensitive của DataList

Các SP5 engine mới bổ sung `nullYN` ở column và `nullYNType` ở DataList cho các API trả JSON. Với column được đánh dấu phù hợp, empty dữ liệu (data / 데이터) có thể được giữ theo default hành vi (behavior / 동작), bị exclude khỏi đối tượng (object / 객체) hoặc được trả thành `null`, tùy cấu hình (configuration / 구성)/bản dựng (build / 빌드).

Điều này có consequence lớn với PATCH/cập nhật (update / 업데이트) đặc tả hợp đồng (contract / 계약):

```text
{ name: "" }   ≠   { name: null }   ≠   { }
```

Nếu backend hiểu ba payload trên khác nhau, một thay đổi engine/cấu hình (config / 설정) ở DataList có thể thay nghiệp vụ (business / 비즈니스) hành vi (behavior / 동작) dù handler JavaScript không đổi. Vì vậy regression kiểm thử (test / 테스트) serialization phải kiểm tra payload thật, không chỉ kiểm tra giá trị (value / 값) hiển thị trên Grid.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **30. Null handling đã trở thành một phần version-sensitive của DataList** nêu điều cần giải thích; **31. dữ liệu (data / 데이터) kiểu (type / 타입) coercion cũng là đặc tả hợp đồng (contract / 계약), không phải convenience vô hại** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **32. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용) thật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. dữ liệu (data / 데이터) kiểu (type / 타입) coercion cũng là đặc tả hợp đồng (contract / 계약), không phải convenience vô hại

SP5 các bản dựng (build / 빌드) gần đây có hành vi (behavior / 동작)/cấu hình (config / 설정) như `preserveType` hoặc `keepDataType` để xử lý việc string được set vào column khai báo `dataType="number"` và các kiểu (type / 타입) khác. Đây là dấu hiệu quan trọng: kiểu (type / 타입) của DataList có thể tham gia coercion khi dữ liệu (data / 데이터) đi vào mô hình (model / 모델).

Giả sử máy chủ (server / 서버) trả:

```json
{ "ACCOUNT_NO": "00123" }
```

Nếu column bị mô hình (model / 모델) như number và coercion biến nó thành `123`, leading zero đã mất trước khi Submission tiếp theo chạy. Vấn đề không nằm ở Grid formatter mà ở **lĩnh vực (domain / 도메인) modeling**: account number nhìn giống số nhưng bản chất là identifier, vì vậy nên là string.

Quy tắc first-principles: chọn DataList `dataType` theo ý nghĩa lĩnh vực (domain / 도메인) và phép toán hợp lệ, không theo hình dạng ký tự.

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **31. dữ liệu (data / 데이터) kiểu (type / 타입) coercion cũng là đặc tả hợp đồng (contract / 계약), không phải convenience vô hại** nêu điều cần giải thích; **32. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용) thật** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **33. Workflow không phải Promise chuỗi (chain / 사슬) “cổ điển” cần thay bằng tay** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용) thật

Bản phát hành (release / 릴리스) ghi chú (note / 노트) SP5 2025 ghi nhận tối ưu nội bộ (internal / 내부) arrays liên quan `rowStatus` và `cellStatus` để giảm bộ nhớ (memory / 메모리) khi set lượng dữ liệu lớn. Điều này xác nhận một điều mà nhà phát triển (developer / 개발자) thường quên: thay đổi (change / 변경) tracking có footprint, đặc biệt với DataList lớn.

Nếu màn hình tải (load / 로드) 50.000 × 30 cells chỉ để read-only report, hãy hỏi liệu máy khách (client / 클라이언트) có thực sự cần toàn bộ dataset và full editing/thay đổi (change / 변경) tracking hay không. Pagination, máy chủ (server / 서버) aggregation, read-only projection hoặc lazy dữ liệu (data / 데이터) chiến lược (strategy / 전략) thường có leverage lớn hơn micro-optimize vòng lặp (loop / 루프) JavaScript.

Hiệu năng (performance / 성능) lập luận (reasoning / 추론) nên đi từ:

```text
number of rows × number of columns
→ metadata/change tracking
→ mapping/coercion
→ Grid rendering
→ formatter/event cost
```

chứ không chỉ nhìn DOM row count.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **32. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용) thật** xác định đầu vào; **33. Workflow không phải Promise chuỗi (chain / 사슬) “cổ điển” cần thay bằng tay** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **34. Submission serialization phải được regression-test như công khai (public / 공개) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Workflow không phải Promise chuỗi (chain / 사슬) “cổ điển” cần thay bằng tay

WebSquare có `xf:workflow` để mô tả thứ tự `submit`/`submitDone` khi nhiều Submission cần phối hợp; guide SP5 khuyến nghị workflow chủ yếu cho communication kiểu Select. Ý nghĩa kiến trúc là phụ thuộc (dependency / 의존성) được khai báo thay vì giấu trong timer hoặc callback lồng sâu.

Tuy vậy workflow không tự giải quyết nghiệp vụ (business / 비즈니스) giao dịch (transaction / 트랜잭션), quay lui (rollback / 롤백) hay phân tán (distributed / 분산) consistency. Nếu `loadA → loadB → loadC` chỉ là truy vấn (query / 쿼리) phụ thuộc (dependency / 의존성), workflow có thể phù hợp. Nếu `saveA → saveB` phải atomic ở cơ sở dữ liệu (database / 데이터베이스), giải pháp đúng thường là một server-side giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계), không phải hai máy khách (client / 클라이언트) Submission nối nhau rồi hy vọng cả hai cùng thành công.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **03 — DataCollection & Submission**, **33. Workflow không phải Promise chuỗi (chain / 사슬) “cổ điển” cần thay bằng tay** xác định đầu vào; **34. Submission serialization phải được regression-test như công khai (public / 공개) đặc tả hợp đồng (contract / 계약)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **35. Checklist lập luận (reasoning / 추론) trước khi sửa Submission bug** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Submission serialization phải được regression-test như công khai (public / 공개) đặc tả hợp đồng (contract / 계약)

Một màn hình có thể nhìn hoàn toàn đúng nhưng payload thay đổi sau engine upgrade, cấu hình (config / 설정) thay đổi (change / 변경) hoặc DataList lược đồ (schema / 스키마) edit. Vì vậy với luồng (flow / 흐름) quan trọng, kiểm thử (test / 테스트) nên cố định các trường hợp (case / 사례):

```text
empty string
null
field absent
number-like identifier
created row
updated row
deleted row
filtered dataset
server 2xx business failure
server 4xx/5xx
stale async response
```

Bằng chứng (evidence / 증거) cuối cùng là yêu cầu (request / 요청) body trong mạng (network / 네트워크) hoặc kiểm thử (test / 테스트) harness, không phải screenshot UI. Đây là điểm nối trực tiếp sang [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md).

> **Chuyển mạch:** Trong **03 — DataCollection & Submission**, **35. Checklist lập luận (reasoning / 추론) trước khi sửa Submission bug** tiếp nhận điểm tựa từ **34. Submission serialization phải được regression-test như công khai (public / 공개) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Checklist lập luận (reasoning / 추론) trước khi sửa Submission bug

Trước khi sửa mã (code / 코드), trả lời được các câu sau: nguồn chuẩn (source of truth / 정본) hiện nằm ở DataMap/DataList nào; row đang ở trạng thái (state / 상태) gì; chỉ mục (index / 인덱스) đang dùng là nguồn (source / 소스) chỉ mục (index / 인덱스) hay filtered/view chỉ mục (index / 인덱스); serializer có chuyển null/kiểu (type / 타입) không; yêu cầu (request / 요청) nào là latest người dùng (user / 사용자) intent; callback đang phản ánh vận chuyển (transport / 전송) hay nghiệp vụ (business / 비즈니스) kết quả (result / 결과); phản hồi (response / 응답) mục tiêu (target / 대상) có replace/merge trạng thái (state / 상태) nào; và sau success máy khách (client / 클라이언트) sẽ re-query hay tự lần ghi nhận (commit / 커밋) cục bộ (local / 로컬) trạng thái (state / 상태).

Nếu một câu chưa trả lời được, fix bằng thêm `if` thường chỉ che symptom.

> **Chuyển mạch:** Ở chặng này của **03 — DataCollection & Submission**, **36. Kết nối** tiếp nhận điểm tựa từ **35. Checklist lập luận (reasoning / 추론) trước khi sửa Submission bug** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 36. Kết nối

DataCollection và Submission trở nên phức tạp hơn khi page được chia thành nhiều frame/phạm vi (scope / 범위). Tiếp theo đọc [04 — Scope, WFrame, Popup & SPA](04_scope_wframe_popup_spa.md).

Khi cần kiểm thử payload, race, row-state và engine upgrade, đọc [11 — Testing, Testability & Regression Engineering](11_testing_testability_regression.md). Khi hành vi (behavior / 동작) chỉ khác giữa cục bộ (local / 로컬)/UAT/môi trường vận hành (production / 운영 환경), đối chiếu thêm [12 — Build, Configuration, Deployment & Environment Reasoning](12_build_config_deployment.md).

> **Bàn giao:** Sau **36. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
