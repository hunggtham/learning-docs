# 23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Từ Submission đơn lẻ đến orchestration đồ thị (graph / 그래프)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. WebSquare Workflow giải quyết vấn đề gì?** để giải thích cách điều kiện hoặc mục tiêu đó vận hành. Mạch này nối workflow orchestration với data state và error architecture, để phân biệt lỗi điều phối phía client với tính nguyên tử của database.

Chapter 03 đã giải thích DataCollection và Submission như hai thành phần nguyên thủy (primitive / 기본 요소) cốt lõi của WebSquare. Chapter này đi thêm một tầng: khi một người dùng (user / 사용자) hành động (action / 동작) không còn tương ứng với một yêu cầu (request / 요청) đơn lẻ mà trở thành **một workflow có nhiều bước, nhiều chuyển tiếp trạng thái (state transition / 상태 전이) và nhiều dạng thất bại (failure mode / 실패 모드)**, ta phải lập luận (reasoning / 추론) thế nào để screen vẫn đúng khi timing thay đổi.

Mục tiêu không phải học thuộc `$p.workflow`. Mục tiêu là nhìn một luồng (flow / 흐름) như `validate → load prerequisite → save → refresh → notify` và biết bước nào thực sự phụ thuộc bước nào, trạng thái (state / 상태) nào được snapshot, lỗi nào có thể thử lại (retry / 재시도), và WebSquare Workflow chỉ orchestration phía máy khách (client / 클라이언트) chứ không biến nhiều HTTP yêu cầu (request / 요청) thành một cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션).

---

## 1. Từ Submission đơn lẻ đến orchestration đồ thị (graph / 그래프)

Một Submission đơn lẻ có mô hình tư duy (mental model / 사고 모델) tương đối thẳng:

```text
user intent
→ prepare request state
→ execute Submission
→ server
→ response
→ target DataCollection
→ UI reaction
```

Khi nghiệp vụ lớn hơn, nhà phát triển (developer / 개발자) thường viết chuỗi callback:

```text
loadCode
→ loadMaster
→ loadDetail
→ saveHeader
→ saveLines
→ refresh
```

Vấn đề là danh sách tuần tự này có thể đang che giấu phụ thuộc (dependency / 의존성) thật. `loadCode` và `loadMaster` có thể độc lập. `saveLines` có thể phụ thuộc `saveHeader` vì cần generated ID. `refresh` chỉ có ý nghĩa nếu save thành công. Nếu chỉ nối callback theo thứ tự mã (code / 코드) được viết, ta đang encode **temporal thứ tự (order / 순서)** thay vì **nghiệp vụ (business / 비즈니스) phụ thuộc (dependency / 의존성)**.

Mô hình tư duy (mental model / 사고 모델) tốt hơn là phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프):

```text
loadCode ─────┐
              ├─→ screen-ready
loadMaster ───┘

validate
→ saveHeader
→ obtain orderId/version
→ saveLines
→ refresh
```

Serial hay parallel phải là kết quả của phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), không phải preference coding style.

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **1. Từ Submission đơn lẻ đến orchestration đồ thị (graph / 그래프)** đặt đầu vào cho **2. WebSquare Workflow giải quyết vấn đề gì?**, rồi **3. Serial không có nghĩa là đúng** mở rộng hệ quả hoặc giới hạn liên quan.

## 2. WebSquare Workflow giải quyết vấn đề gì?

SP5 cung cấp Workflow để định nghĩa thứ tự thực thi nhiều Submission. Official guide mô tả cả serial step, parallel step, kết quả (result / 결과) handling và việc quyết định bước sau dựa trên kết quả trước. `$p.workflow` có các năng lực (capability / 역량) như thực thi workflow đã khai báo, chạy serial/parallel trực tiếp, kiểm tra workflow đang chạy và reject workflow; chính xác (exact / 정확한) signature cần đối chiếu engine bản dựng (build / 빌드).

Điểm quan trọng là Workflow giải quyết **máy khách (client / 클라이언트) orchestration**:

```text
Submission A
Submission B
Submission C
        ↓
ordering / parallelism / result coordination
```

Nó không tự tạo phân tán (distributed / 분산) giao dịch (transaction / 트랜잭션):

```text
A commit server
B commit server
C fail
```

Workflow biết C thất bại (fail / 실패) nhưng không thể tự quay lui (rollback / 롤백) cơ sở dữ liệu (database / 데이터베이스) lần ghi nhận (commit / 커밋) của A và B nếu backend không cung cấp giao dịch (transaction / 트랜잭션)/compensation đặc tả hợp đồng (contract / 계약).

Vì vậy:

```text
workflow atomicity ≠ database atomicity
```

Đây là bất biến (invariant / 불변식) quan trọng nhất của chapter.

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **2. WebSquare Workflow giải quyết vấn đề gì?** đặt đầu vào cho **3. Serial không có nghĩa là đúng**, rồi **4. Parallel cũng không có nghĩa là độc lập về trạng thái (state / 상태)** mở rộng hệ quả hoặc giới hạn liên quan.

## 3. Serial không có nghĩa là đúng

Serial thực thi (execution / 실행) phù hợp khi step sau cần đầu ra (output / 출력) hoặc side tác động (effect / 효과) của step trước.

Ví dụ tạo thứ tự (order / 순서):

```text
createOrder
→ response { orderId, version }
→ createOrderLines(orderId)
```

Nếu chạy parallel, line yêu cầu (request / 요청) chưa có `orderId`. Serial là phụ thuộc (dependency / 의존성) thật.

Nhưng luồng (flow / 흐름) sau không cần serial:

```text
loadDepartmentCodes
loadRoleCodes
loadCountryCodes
```

Nếu ba yêu cầu (request / 요청) độc lập, serial tạo độ trễ (latency / 지연 시간):

```text
T_total ≈ T_department + T_role + T_country
```

Parallel lý tưởng gần hơn với:

```text
T_total ≈ max(T_department, T_role, T_country)
```

Tất nhiên máy chủ (server / 서버) sức chứa (capacity / 용량), liên kết (connection / 연결) limit và downstream tải (load / 로드) vẫn phải được tính. Parallel không phải “càng nhiều càng nhanh”.

---

> **Nối mạch:** Serial ordering không đảm bảo correctness; parallel workflow vẫn chia sẻ state, nên snapshot request state trước orchestration để kiểm soát race và retry.

## 4. Parallel cũng không có nghĩa là độc lập về trạng thái (state / 상태)

Hai yêu cầu (request / 요청) có endpoint khác nhau vẫn có thể tranh chấp cùng máy khách (client / 클라이언트) trạng thái (state / 상태).

Ví dụ:

```text
sbmLoadCustomer → target dlResult
sbmLoadOrders   → target dlResult
```

Chúng chạy parallel nhưng cùng mục tiêu (target / 대상). yêu cầu (request / 요청) về sau ghi đè yêu cầu (request / 요청) về trước. Đây không phải mạng (network / 네트워크) bug; thiết kế (design / 설계) đã cho hai thao tác (operation / 연산) cùng quyền sở hữu (ownership / 소유권).

Parallel an toàn hơn khi:

```text
request identity độc lập
+ target state độc lập
+ side effect độc lập
+ completion aggregation rõ
```

Nếu hai step cùng sửa một DataMap hoặc cùng bật/tắt spinner toàn cục (global / 전역), vẫn có race dù endpoint độc lập.

---

> **Nối mạch:** Parallel workflow vẫn chia sẻ state; snapshot request trước orchestration tạo input bất biến, còn workflow instance identity tiếp theo theo dõi retry và resume.

## 5. Snapshot yêu cầu (request / 요청) trạng thái (state / 상태) trước khi orchestration

Một lỗi enterprise phổ biến là Workflow đọc DataMap mutable ở từng step thay vì chụp người dùng (user / 사용자) intent ban đầu.

Người dùng (user / 사용자) bấm tìm kiếm (search / 검색) với:

```text
customerId = A
```

Workflow bắt đầu. Trong lúc yêu cầu (request / 요청) đầu đang chạy, người dùng (user / 사용자) đổi đầu vào (input / 입력) thành B. Step sau serialize lại `dmSearch` và gửi B.

Một nghiệp vụ (business / 비즈니스) hành động (action / 동작) đã bị chia thành hai intent.

Khi consistency cần thiết, hãy snapshot:

```javascript
scwin.search = function () {
    var criteria = {
        customerId: dmSearch.get("customerId"),
        fromDate: dmSearch.get("fromDate"),
        toDate: dmSearch.get("toDate")
    };

    scwin.executeSearchFlow(criteria);
};
```

Chính xác (exact / 정확한) API lấy DataMap có thể khác theo dự án (project / 프로젝트) convention; mô hình tư duy (mental model / 사고 모델) là **workflow đầu vào (input / 입력) phải có định danh (identity / 식별자) và snapshot rõ**.

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **5. Snapshot yêu cầu (request / 요청) trạng thái (state / 상태) trước khi orchestration** đặt đầu vào cho **6. Workflow instance cũng cần định danh (identity / 식별자)**, rồi **7. Cancel vận chuyển (transport / 전송) và cancel nghiệp vụ (business / 비즈니스) intent là hai việc khác nhau** mở rộng hệ quả hoặc giới hạn liên quan.

## 6. Workflow instance cũng cần định danh (identity / 식별자)

Nếu người dùng (user / 사용자) chạy cùng workflow hai lần:

```text
Search A → workflow W1
Search B → workflow W2
```

thì tên workflow `wfSearch` không đủ phân biệt hai intent.

Cần lập luận (reasoning / 추론) với:

```text
workflowDefinitionId = wfSearch
workflowRunId        = R101 / R102
userIntentVersion    = 7 / 8
screenInstanceKey    = employeeSearch#3
```

Khi callback về, câu hỏi không chỉ là “workflow nào?” mà là “run này còn thuộc intent hiện tại của screen instance này không?”.

Đây là cùng một stale-result bài toán (problem / 문제) đã gặp ở Submission, popup và bản địa (native / 네이티브) cầu nối (bridge / 브리지), nhưng ở orchestration mức (level / 수준).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **6. Workflow instance cũng cần định danh (identity / 식별자)** đặt đầu vào cho **7. Cancel vận chuyển (transport / 전송) và cancel nghiệp vụ (business / 비즈니스) intent là hai việc khác nhau**, rồi **8. Workflow kết quả (result / 결과) không nên bị giảm thành boolean** mở rộng hệ quả hoặc giới hạn liên quan.

## 7. Cancel vận chuyển (transport / 전송) và cancel nghiệp vụ (business / 비즈니스) intent là hai việc khác nhau

SP5 Submission có cơ chế abort ở các bản dựng (build / 빌드) tương ứng, và Workflow có reject/cancel ngữ nghĩa (semantics / 의미론). Nhưng abort máy khách (client / 클라이언트) yêu cầu (request / 요청) không chứng minh máy chủ (server / 서버) chưa lần ghi nhận (commit / 커밋).

Timeline:

```text
client gửi Save
server commit
client bấm Cancel
browser abort connection
```

UI có thể nghĩ “đã hủy”, trong khi dữ liệu đã lưu.

Vì vậy cần tách:

```text
transport cancellation
business cancellation
```

Vận chuyển (transport / 전송) cancellation chỉ dừng chờ/nhận phản hồi (response / 응답) ở máy khách (client / 클라이언트) khi còn có thể. nghiệp vụ (business / 비즈니스) cancellation phải là lĩnh vực (domain / 도메인) command có đặc tả hợp đồng (contract / 계약) máy chủ (server / 서버) riêng nếu nghiệp vụ hỗ trợ.

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **7. Cancel vận chuyển (transport / 전송) và cancel nghiệp vụ (business / 비즈니스) intent là hai việc khác nhau** đặt đầu vào cho **8. Workflow kết quả (result / 결과) không nên bị giảm thành boolean**, rồi **9. lỗi (error / 오류) taxonomy cho WebSquare enterprise screen** mở rộng hệ quả hoặc giới hạn liên quan.

## 8. Workflow kết quả (result / 결과) không nên bị giảm thành boolean

Một orchestration lớn cần kết quả (result / 결과) mô hình (model / 모델) có cấu trúc.

Thay vì:

```javascript
success = true;
```

hãy lập luận (reasoning / 추론) theo:

```text
workflowRunId
stepId
requestId
status
httpStatus
businessCode
retryable
committed
correlationId
payload/result reference
```

`success=false` không nói được step nào thất bại (fail / 실패), có side tác động (effect / 효과) trước đó không, hay thử lại (retry / 재시도) toàn luồng (flow / 흐름) có duplicate dữ liệu không.

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **8. Workflow kết quả (result / 결과) không nên bị giảm thành boolean** đặt đầu vào cho **9. lỗi (error / 오류) taxonomy cho WebSquare enterprise screen**, rồi **10. submitdone không đồng nghĩa nghiệp vụ (business / 비즈니스) success** mở rộng hệ quả hoặc giới hạn liên quan.

## 9. lỗi (error / 오류) taxonomy cho WebSquare enterprise screen

Không nên gom mọi lỗi vào một `alert("오류")`.

Một taxonomy thực dụng:

```text
Client validation error
Transport error
Protocol/HTTP error
Authentication/session error
Authorization error
Business rule error
Concurrency/conflict error
Partial batch error
Integration/downstream error
Unexpected client/runtime error
```

Mỗi loại có đơn vị sở hữu (owner / 오너) và UX khác nhau.

Máy khách (client / 클라이언트) kiểm tra hợp lệ (validation / 검증) thường map về trường dữ liệu (field / 필드)/row. Authentication có thể yêu cầu re-auth hoặc redirect. Authorization không nên thử lại (retry / 재시도). xung đột (conflict / 충돌) cần reload/compare. vận chuyển (transport / 전송) hết thời gian chờ (timeout / 타임아웃) có thể thử lại (retry / 재시도) chỉ khi thao tác (operation / 연산) idempotent hoặc có idempotency key. nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) phải hiển thị message đủ ngữ cảnh (context / 맥락) nhưng không leak máy chủ (server / 서버) internals.

---

> **Nối mạch:** Error taxonomy phân biệt transport, application và domain failure; `submitdone` chỉ là callback, nên error envelope phải ổn định hơn message text.

## 10. `submitdone` không đồng nghĩa nghiệp vụ (business / 비즈니스) success

SP5 phân biệt `submitdone` và `submiterror` chủ yếu theo HTTP phản hồi (response / 응답) status. Vì vậy phản hồi (response / 응답) HTTP 200 có thể vẫn chứa:

```json
{
  "success": false,
  "code": "ORDER_ALREADY_APPROVED",
  "message": "..."
}
```

Mô hình tư duy (mental model / 사고 모델):

```text
transport success
≠ protocol success
≠ business success
≠ state convergence
```

Sau nghiệp vụ (business / 비즈니스) success, máy khách (client / 클라이언트) còn phải kiểm tra chuẩn gốc (canonical / 정본) trạng thái (state / 상태) đã hội tụ chưa: phiên bản (version / 버전) mới, generated key, normalized giá trị (value / 값), permission snapshot hoặc server-calculated trường dữ liệu (field / 필드) có được merge đúng không.

---

> **Nối mạch:** `submitdone` chỉ báo luồng kỹ thuật đã kết thúc; **error envelope** chuẩn hóa phần còn lại để **field/row/global error** có thể định vị và hiển thị nhất quán.

## 11. lỗi (error / 오류) envelope phải ổn định hơn message văn bản (text / 텍스트)

UI không nên branch theo văn bản (text / 텍스트):

```javascript
if (message === "이미 승인되었습니다") { ... }
```

Message thay đổi theo locale hoặc wording.

Đặc tả hợp đồng (contract / 계약) tốt hơn:

```json
{
  "success": false,
  "error": {
    "code": "ORDER_ALREADY_APPROVED",
    "category": "BUSINESS_RULE",
    "messageKey": "order.alreadyApproved",
    "fieldErrors": [],
    "rowErrors": [],
    "correlationId": "..."
  }
}
```

WebSquare page dùng `code/category` để chọn hành vi (behavior / 동작), locale tầng (layer / 계층) chọn message, correlation ID phục vụ sự cố (incident / 인시던트) dấu vết (trace / 추적).

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **11. lỗi (error / 오류) envelope phải ổn định hơn message văn bản (text / 텍스트)** đặt vấn đề; **12. trường dữ liệu (field / 필드) lỗi (error / 오류), row lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류) là ba coordinate hệ thống (system / 시스템)** đối chiếu bằng chứng, rồi **13. DataList dirty trạng thái (state / 상태) là máy trạng thái (state machine / 상태 머신), không phải boolean** mở rộng hệ quả hoặc giới hạn liên quan.

## 12. trường dữ liệu (field / 필드) lỗi (error / 오류), row lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류) là ba coordinate hệ thống (system / 시스템)

Form lỗi (error / 오류) có coordinate:

```text
field = amount
```

Grid batch lỗi (error / 오류) cần nghiệp vụ (business / 비즈니스) định danh (identity / 식별자):

```text
entityKey = ORDER_LINE_9281
field = quantity
```

Không nên chỉ trả:

```text
rowIndex = 7
```

vì sort/filter/paging có thể làm chỉ mục (index / 인덱스) 7 không còn là thực thể (entity / 엔터티) máy chủ (server / 서버) đã validate.

Toàn cục (global / 전역) lỗi (error / 오류) như “downstream settlement unavailable” không thuộc trường dữ liệu (field / 필드) hay row cụ thể.

Lỗi (error / 오류) ánh xạ (mapping / 매핑) đúng phải giữ coordinate hệ thống (system / 시스템) rõ.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **12. trường dữ liệu (field / 필드) lỗi (error / 오류), row lỗi (error / 오류) và toàn cục (global / 전역) lỗi (error / 오류) là ba coordinate hệ thống (system / 시스템)** đặt vấn đề; **13. DataList dirty trạng thái (state / 상태) là máy trạng thái (state machine / 상태 머신), không phải boolean** đối chiếu bằng chứng, rồi **14. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용)** mở rộng hệ quả hoặc giới hạn liên quan.

## 13. DataList dirty trạng thái (state / 상태) là máy trạng thái (state machine / 상태 머신), không phải boolean

Nhà phát triển (developer / 개발자) thường hỏi “DataList có thay đổi chưa?”. Câu hỏi chính xác hơn là row nào đang ở chuyển tiếp (transition / 전이) nào.

Conceptually:

```text
server baseline
→ user insert
→ C

server baseline
→ user edit
→ U

server baseline
→ user delete
→ D
```

Một row mới tạo rồi xóa trước khi save có thể có ngữ nghĩa (semantics / 의미론) khác row máy chủ (server / 서버) đã tồn tại rồi bị xóa. bản phát hành (release / 릴리스) notes của SP5 từng sửa hành vi (behavior / 동작) quanh modified/deleted serialization, cho thấy chính xác (exact / 정확한) trường hợp biên (edge case / 경계 사례) có thể thay đổi theo bản dựng (build / 빌드).

Do đó mã (code / 코드) môi trường vận hành (production / 운영 환경) không nên tự suy diễn row-state internals bằng array phụ nếu DataList đã là đơn vị sở hữu (owner / 오너).

---

> **Nối mạch:** Khi `dirty` đã được coi là state machine, **row/cell status** phải tính chi phí lưu và đồng bộ; từ đó **type conversion** trở thành contract bảo vệ dữ liệu qua các trạng thái.

## 14. Row status và cell status có bộ nhớ (memory / 메모리) chi phí (cost / 비용)

Tracking thay đổi cần siêu dữ liệu (metadata / 메타데이터). Với DataList rất lớn, siêu dữ liệu (metadata / 메타데이터) theo row/cell có thể trở thành bộ nhớ (memory / 메모리) pressure đáng kể. SP5 bản phát hành (release / 릴리스) notes 2024–2025 có thay đổi để giảm phần tử rowStatus/cellStatus không cần thiết khi set large dữ liệu (data / 데이터).

Điều này cho một bài học bền hơn API cụ thể:

```text
change tracking is not free
```

Nếu screen chỉ xem 100.000 row mà không edit, đừng mặc định kiến trúc (architecture / 아키텍처) giống editable 100.000-row máy khách (client / 클라이언트) bảng (table / 테이블). máy chủ (server / 서버) paging, chunk loading hoặc read-only biểu diễn (representation / 표현) có thể phù hợp hơn.

---

> **Nối mạch:** Contract kiểu dữ liệu chỉ có nghĩa khi phân biệt được `null`, chuỗi rỗng và field bị thiếu; **16** dùng ba trạng thái đó để giải thích merge, validate và hiển thị lỗi.

## 15. kiểu (type / 타입) conversion là đặc tả hợp đồng (contract / 계약), không phải convenience

DataList column có `dataType`, và các SP5 bản dựng (build / 빌드) mới bổ sung hành vi (behavior / 동작) như `preserveType`/`keepDataType` để xử lý dữ liệu string đi vào column number/date theo chính sách (policy / 정책) tương ứng.

Điều nguy hiểm là mã (code / 코드) chạy “có vẻ đúng” nhưng equality/sort/serialization dùng kiểu (type / 타입) khác kỳ vọng.

Ví dụ:

```text
"10" < "2"   // lexical semantics
10 < 2        // numeric semantics
```

Master quy tắc (rule / 규칙):

```text
server schema
↔ DataCollection schema
↔ UI display/edit conversion
```

phải được thiết kế nhất quán. Không dùng formatter để che kiểu (type / 타입) mô hình (model / 모델) sai.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **15. kiểu (type / 타입) conversion là đặc tả hợp đồng (contract / 계약), không phải convenience** đặt vấn đề; **16. null, empty string và missing trường dữ liệu (field / 필드) là ba trạng thái khác nhau** đối chiếu bằng chứng, rồi **17. Modified payload cần snapshot trước async save** mở rộng hệ quả hoặc giới hạn liên quan.

## 16. `null`, empty string và missing trường dữ liệu (field / 필드) là ba trạng thái khác nhau

SP5 mới hơn có `nullYN`/`nullYNType` cho DataList serialization/getter hành vi (behavior / 동작) ở các bản dựng (build / 빌드) tương ứng. Điều này tồn tại vì enterprise đặc tả hợp đồng (contract / 계약) thường cần phân biệt:

```text
field missing
field = null
field = ""
```

Ví dụ PATCH ngữ nghĩa (semantics / 의미론):

```text
missing  → không thay đổi
null     → clear value
""       → business value rỗng hoặc normalize tùy schema
```

Nếu frontend normalize tất cả về `""`, máy chủ (server / 서버) mất thông tin intent.

Null ngữ nghĩa (semantics / 의미론) phải được quyết định ở đặc tả hợp đồng (contract / 계약) ranh giới (boundary / 경계), không để accidental conversion quyết định.

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **16. null, empty string và missing trường dữ liệu (field / 필드) là ba trạng thái khác nhau** đặt vấn đề; **17. Modified payload cần snapshot trước async save** đối chiếu bằng chứng, rồi **18. Derived view không được trở thành chuẩn gốc (canonical / 정본) định danh (identity / 식별자)** mở rộng hệ quả hoặc giới hạn liên quan.

## 17. Modified payload cần snapshot trước async save

Giả sử Save lấy changed rows từ DataList. người dùng (user / 사용자) tiếp tục edit trong lúc yêu cầu (request / 요청) pending.

Nếu callback success rồi reset toàn DataList dirty trạng thái (state / 상태), edit mới chưa gửi có thể bị đánh dấu sạch.

Timeline:

```text
T0 snapshot changes A
T1 send A
T2 user edits B
T3 response A success
T4 reset all dirty state   ← B bị mất tracking
```

Cần một chiến lược (strategy / 전략) như:

```text
snapshot/version changes gửi đi
→ request identity
→ success chỉ acknowledge đúng snapshot
→ preserve changes phát sinh sau snapshot
```

Chính xác (exact / 정확한) hiện thực (implementation / 구현) phụ thuộc dự án (project / 프로젝트)/API, nhưng bất biến (invariant / 불변식) là **acknowledgement không được xóa mutation chưa được acknowledge**.

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, sau nội dung của **17. Modified payload cần snapshot trước async save**, **18. Derived view không được trở thành chuẩn gốc (canonical / 정본) định danh (identity / 식별자)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **19. Workflow không nên sở hữu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)** mở rộng hệ quả hoặc giới hạn liên quan.

## 18. Derived view không được trở thành chuẩn gốc (canonical / 정본) định danh (identity / 식별자)

LinkedDataList, Grid sort/filter và paging tạo view coordinate. nghiệp vụ (business / 비즈니스) save/lỗi (error / 오류) ánh xạ (mapping / 매핑) phải quay về stable thực thể (entity / 엔터티) định danh (identity / 식별자).

Mô hình tư duy (mental model / 사고 모델):

```text
canonical DataList/entity
        ↓
filter/sort/derived view
        ↓
Grid view row
```

Không đi ngược bằng cách giả định `viewRowIndex === modelRowIndex`.

Chapter 13 đi sâu Grid coordinate; chapter này nhấn mạnh orchestration/lỗi (error / 오류) ánh xạ (mapping / 매핑) phải mang nghiệp vụ (business / 비즈니스) key qua toàn luồng (flow / 흐름).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **18. Derived view không được trở thành chuẩn gốc (canonical / 정본) định danh (identity / 식별자)** đặt đầu vào cho **19. Workflow không nên sở hữu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)**, rồi **20. Compensation khi multi-step luồng (flow / 흐름) không atomic** mở rộng hệ quả hoặc giới hạn liên quan.

## 19. Workflow không nên sở hữu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)

Workflow nên orchestration:

```text
prepare
→ call
→ branch result
→ continue/stop
```

Không nên chứa hàng trăm dòng quy tắc (rule / 규칙) tính giá, quyền hay trạng thái lĩnh vực (domain / 도메인). quy tắc (rule / 규칙) thuần nên nằm ở hàm (function / 함수)/mô-đun (module / 모듈) testable; bất biến (invariant / 불변식) authoritative nằm máy chủ (server / 서버).

Nếu Workflow definition trở thành “nghiệp vụ (business / 비즈니스) engine phía trình duyệt (browser / 브라우저)”, testability và bảo mật (security / 보안) đều giảm.

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **19. Workflow không nên sở hữu nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙)** đặt đầu vào cho **20. Compensation khi multi-step luồng (flow / 흐름) không atomic**, rồi **21. thử lại (retry / 재시도) phải gắn với idempotency** mở rộng hệ quả hoặc giới hạn liên quan.

## 20. Compensation khi multi-step luồng (flow / 흐름) không atomic

Luồng (flow / 흐름):

```text
create attachment metadata
→ upload binary
→ save business entity
```

Nếu bước cuối thất bại (fail / 실패), có thể còn siêu dữ liệu (metadata / 메타데이터)/tệp (file / 파일) orphan.

Các chiến lược (strategy / 전략):

```text
staging + promote
expiry cleanup
explicit compensation command
idempotent upsert
server-side transaction khi cùng boundary
```

Máy khách (client / 클라이언트) Workflow chỉ gọi chiến lược (strategy / 전략); nó không thay thế chiến lược (strategy / 전략).

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **20. Compensation khi multi-step luồng (flow / 흐름) không atomic** đặt đầu vào cho **21. thử lại (retry / 재시도) phải gắn với idempotency**, rồi **22. Loading indicator cũng cần quyền sở hữu (ownership / 소유권)** mở rộng hệ quả hoặc giới hạn liên quan.

## 21. thử lại (retry / 재시도) phải gắn với idempotency

Không thử lại (retry / 재시도) chỉ vì hết thời gian chờ (timeout / 타임아웃).

Tìm kiếm (search / 검색)/read thường dễ thử lại (retry / 재시도) hơn command tạo side tác động (effect / 효과). Save/create cần biết:

```text
requestId / idempotencyKey
server deduplication policy
commit ambiguity
```

Nếu hết thời gian chờ (timeout / 타임아웃) xảy ra sau máy chủ (server / 서버) lần ghi nhận (commit / 커밋), thử lại (retry / 재시도) blind có thể duplicate.

Master question trước thử lại (retry / 재시도):

> Tôi có chứng minh được yêu cầu (request / 요청) này chưa lần ghi nhận (commit / 커밋), hoặc thử lại (retry / 재시도) cùng định danh (identity / 식별자) sẽ không tạo side tác động (effect / 효과) thứ hai không?

Nếu không, phải truy vấn (query / 쿼리) status/reconcile thay vì thử lại (retry / 재시도) mù.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, sau nội dung của **21. thử lại (retry / 재시도) phải gắn với idempotency**, **22. Loading indicator cũng cần quyền sở hữu (ownership / 소유권)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **23. Workflow khả năng quan sát (observability / 관측 가능성)** mở rộng hệ quả hoặc giới hạn liên quan.

## 22. Loading indicator cũng cần quyền sở hữu (ownership / 소유권)

Hai yêu cầu (request / 요청) parallel dùng một spinner toàn cục (global / 전역):

```text
A start → spinner on
B start → spinner on
A done  → spinner off
B still running
```

UI báo ready sai.

Dùng thao tác (operation / 연산) count hoặc đơn vị sở hữu (owner / 오너) đơn vị từ (token / 토큰):

```text
pending = 2
A done → 1
B done → 0 → hide
```

Tương tự disable Save button phải gắn với command instance, không phải boolean toàn cục (global / 전역) dễ bị callback cũ reset.

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **22. Loading indicator cũng cần quyền sở hữu (ownership / 소유권)** đặt đầu vào cho **23. Workflow khả năng quan sát (observability / 관측 가능성)**, rồi **24. Testing orchestration bằng permutation, không chỉ happy đường dẫn (path / 경로)** mở rộng hệ quả hoặc giới hạn liên quan.

## 23. Workflow khả năng quan sát (observability / 관측 가능성)

Một workflow môi trường vận hành (production / 운영 환경) nên dấu vết (trace / 추적) được:

```text
screenInstanceKey
workflowDefinitionId
workflowRunId
userIntentVersion
stepId
submissionId
requestId
correlationId
start/end/elapsed
result category
```

Không cần log toàn payload nhạy cảm. Cần log định danh (identity / 식별자) và timing đủ nối đồ thị (graph / 그래프).

Khi sự cố (incident / 인시던트) “Save treo”, ta phải trả lời được nó treo ở kiểm tra hợp lệ (validation / 검증), Workflow hàng đợi (queue / 큐), Submission, gateway, máy chủ (server / 서버) hay callback ánh xạ (mapping / 매핑).

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **23. Workflow khả năng quan sát (observability / 관측 가능성)** đặt đầu vào cho **24. Testing orchestration bằng permutation, không chỉ happy đường dẫn (path / 경로)**, rồi **25. trường hợp (case / 사례) study — tìm kiếm (search / 검색) workflow trả trạng thái (state / 상태) lai** mở rộng hệ quả hoặc giới hạn liên quan.

## 24. Testing orchestration bằng permutation, không chỉ happy đường dẫn (path / 경로)

Một kiểm thử (test / 테스트) tốt thay đổi thứ tự (ordering / 순서):

```text
A nhanh, B chậm
A chậm, B nhanh
A timeout
B business fail
screen close giữa flow
session expire ở step 2
user chạy flow mới trước flow cũ xong
retry sau ambiguous timeout
```

Parallel luồng (flow / 흐름) cần kiểm thử (test / 테스트) permutation. Serial luồng (flow / 흐름) cần kiểm thử (test / 테스트) thất bại (fail / 실패) ở từng ranh giới (boundary / 경계).

Nếu kiểm thử (test / 테스트) chỉ chạy mạng (network / 네트워크) mock với phản hồi (response / 응답) cố định 100 ms, race bug gần như không được kiểm tra.

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **24. Testing orchestration bằng permutation, không chỉ happy đường dẫn (path / 경로)** nêu quy tắc; **25. trường hợp (case / 사례) study — tìm kiếm (search / 검색) workflow trả trạng thái (state / 상태) lai** thử quy tắc trong tình huống, rồi **26. trường hợp (case / 사례) study — Save header thành công, line thất bại (fail / 실패)** mở rộng hệ quả.

## 25. trường hợp (case / 사례) study — tìm kiếm (search / 검색) workflow trả trạng thái (state / 상태) lai

Screen cần tải (load / 로드) customer và permission-dependent hành động (action / 동작) danh sách (list / 목록).

```text
loadCustomer(A)
loadActions(A)
```

Người dùng (user / 사용자) nhanh chóng tìm kiếm (search / 검색) B. phản hồi (response / 응답) thứ tự (order / 순서):

```text
customer B
customer A
actions B
actions A
```

Nếu mỗi callback chỉ set mục tiêu (target / 대상), cuối cùng UI có thể hiển thị customer A nhưng tìm kiếm (search / 검색) box B.

Fix không phải “thêm delay”. Fix là intent định danh (identity / 식별자):

```text
searchRunId
→ attach vào cả request
→ callback chỉ apply nếu runId === currentRunId
```

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, sau khi thấy quy trình trong **25. trường hợp (case / 사례) study — tìm kiếm (search / 검색) workflow trả trạng thái (state / 상태) lai**, **26. trường hợp (case / 사례) study — Save header thành công, line thất bại (fail / 실패)** đặt nó vào một trường hợp đủ cụ thể để nhận ra điều kiện thành công và chỗ dễ sai. Từ đây, **27. trường hợp (case / 사례) study — Success callback reset edit mới** mở rộng hệ quả hoặc giới hạn liên quan.

## 26. trường hợp (case / 사례) study — Save header thành công, line thất bại (fail / 실패)

Header đã lần ghi nhận (commit / 커밋) và trả `orderId=1001`. Line save thất bại (fail / 실패) do kiểm tra hợp lệ (validation / 검증).

UI không được hiển thị “Save failed, nothing changed”. chuẩn gốc (canonical / 정본) trạng thái (state / 상태) đã thay đổi.

Possible đặc tả hợp đồng (contract / 계약):

```text
server endpoint atomic save header+lines
```

hoặc nếu ranh giới (boundary / 경계) buộc tách:

```text
header created
→ line failure
→ show partial state
→ allow resume/repair
→ compensation nếu domain cho phép
```

Lỗi (error / 오류) UX phải phản ánh giao dịch (transaction / 트랜잭션) reality.

---

> **Nối mạch:** Ở chặng này của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **26. trường hợp (case / 사례) study — Save header thành công, line thất bại (fail / 실패)** nêu quy tắc; **27. trường hợp (case / 사례) study — Success callback reset edit mới** thử quy tắc trong tình huống, rồi **28. môi trường vận hành (production / 운영 환경) rà soát (review / 검토) checklist** mở rộng hệ quả.

## 27. trường hợp (case / 사례) study — Success callback reset edit mới

Người dùng (user / 사용자) bấm Save A rồi tiếp tục sửa B. Save A success callback gọi dùng chung (common / 공통) hàm (function / 함수) reset toàn row status.

B không còn được gửi ở lần Save sau.

Nguyên nhân gốc (root cause / 근본 원인) là acknowledgement không có mutation định danh (identity / 식별자).

Regression kiểm thử (test / 테스트) phải thực hiện edit trong lúc Save pending; đây là trường hợp (case / 사례) rất dễ bị bỏ sót nếu kiểm thử (test / 테스트) disable toàn screen trong mọi yêu cầu (request / 요청).

---

> **Nối mạch:** Đặt trong câu hỏi lớn của **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **27. trường hợp (case / 사례) study — Success callback reset edit mới** nêu quy tắc; **28. môi trường vận hành (production / 운영 환경) rà soát (review / 검토) checklist** thử quy tắc trong tình huống, rồi **29. Master synthesis** mở rộng hệ quả.

## 28. môi trường vận hành (production / 운영 환경) rà soát (review / 검토) checklist

Trước khi approve một multi-request luồng (flow / 흐름), hãy trả lời:

```text
Dependency graph thật là gì?
Step nào có thể parallel?
Workflow input có snapshot không?
Mỗi run có identity không?
Target state có bị nhiều request cùng sở hữu không?
Cancel có nghĩa transport hay business cancel?
HTTP success được tách khỏi business success chưa?
Error có category/code/coordinate ổn định không?
Retry có idempotency contract không?
Partial commit được biểu diễn thế nào?
Dirty-state acknowledgement có xóa edit mới không?
Null/type semantics có explicit không?
Loading/disabled state thuộc operation nào?
Log có đủ workflowRunId/requestId/correlationId không?
Test đã đảo response order chưa?
```

---

> **Nối mạch:** Trong **23 — Workflow Orchestration, Advanced dữ liệu (data / 데이터) trạng thái (state / 상태) & Enterprise lỗi (error / 오류) kiến trúc (architecture / 아키텍처)**, **29. Master synthesis** tổng hợp từ **28. môi trường vận hành (production / 운영 환경) rà soát (review / 검토) checklist** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **30. Nguồn kiểm chứng theo bản dựng (build / 빌드)** mở rộng hệ quả hoặc giới hạn liên quan.

## 29. Master synthesis

Ở mức Master, DataCollection, Submission và Workflow không còn là ba API riêng lẻ. Chúng tạo một state-transition hệ thống (system / 시스템):

```text
User intent
→ immutable/snapshotted command input
→ workflow run identity
→ Submission graph
→ server side effects
→ result/error taxonomy
→ acknowledgement
→ client state convergence
→ render
```

Mỗi mũi tên cần quyền sở hữu (ownership / 소유권) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론).

Nếu chỉ nhớ `$p.executeSubmission()` hay `$p.workflow.executeSerial()`, ta mới biết cơ chế (mechanism / 메커니즘). Nếu có thể giải thích **phụ thuộc (dependency / 의존성), snapshot, định danh (identity / 식별자), atomicity, compensation, thử lại (retry / 재시도) an toàn (safety / 안전), dirty-state acknowledgement và bằng chứng (evidence / 증거)**, ta mới lập luận (reasoning / 추론) được môi trường vận hành (production / 운영 환경) workflow.

---

> **Nối mạch:** **Master synthesis** gom workflow, state và error contract thành một mô hình; **Nguồn kiểm chứng theo bản dựng** xác nhận mô hình đó bằng artifact/log trước khi áp dụng vào production.

## 30. Nguồn kiểm chứng theo bản dựng (build / 빌드)

Khi cần chính xác (exact / 정확한) API, đối chiếu WebSquare5 SP5 Development Guide/API tham chiếu (reference / 참조)/bản phát hành (release / 릴리스) Notes đúng engine bản dựng (build / 빌드), đặc biệt các phần Workflow, Submission, DataCollection và các bản phát hành (release / 릴리스) ghi chú (note / 노트) về `executeSerial`/`executeParallel`, `nullYNType`, `preserveType`/`keepDataType`, `getModifiedJSON()`/`getOnlyDeletedJSON()` và row/cell-status bộ nhớ (memory / 메모리) hành vi (behavior / 동작).

Các API/signature có thể tiến hóa theo bản dựng (build / 빌드). chuẩn gốc (canonical / 정본) bất biến (invariant / 불변식) của chapter là phụ thuộc (dependency / 의존성), định danh (identity / 식별자), giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) và trạng thái (state / 상태) convergence; không phải một signature cố định.

> **Bàn giao:** Sau **30. Nguồn kiểm chứng theo bản dựng (build / 빌드)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
