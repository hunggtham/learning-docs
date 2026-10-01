# 15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Submission là vận chuyển (transport / 전송) đặc tả hợp đồng (contract / 계약), không phải giao dịch (transaction / 트랜잭션)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. CRUD row status cần ánh xạ (mapping / 매핑) đặc tả hợp đồng (contract / 계약) rõ** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

WebSquare là frontend nền tảng (platform / 플랫폼), nhưng phần khó nhất của màn hình enterprise thường nằm ở **ranh giới máy khách (client / 클라이언트)–máy chủ (server / 서버)**. DataList có row status, Submission có tham chiếu (reference / 참조)/mục tiêu (target / 대상) và Grid có kiểm tra hợp lệ (validation / 검증), nhưng cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션), authorization, locking và nghiệp vụ (business / 비즈니스) bất biến (invariant / 불변식) thật sự vẫn thuộc backend.

Chapter này không dạy lại Java/Spring hay cơ sở dữ liệu (database / 데이터베이스). Nó tập trung vào câu hỏi WebSquare nhà phát triển (developer / 개발자) phải lập luận (reasoning / 추론) được: **máy khách (client / 클라이언트) gửi đặc tả hợp đồng (contract / 계약) gì, máy chủ (server / 서버) trả đặc tả hợp đồng (contract / 계약) gì, row trạng thái (state / 상태) được dịch thành command thế nào, thử lại (retry / 재시도) có an toàn không, xung đột (conflict / 충돌) được biểu diễn ra sao, và UI làm gì khi kết quả giao dịch (transaction / 트랜잭션) không đơn giản là success/thất bại (fail / 실패)**.

## 1. Submission là vận chuyển (transport / 전송) đặc tả hợp đồng (contract / 계약), không phải giao dịch (transaction / 트랜잭션)

Mô hình tư duy (mental model / 사고 모델):

```text
WebSquare page
→ DataCollection
→ Submission serialization
→ HTTP
→ server controller/service
→ transaction/database
→ response
→ Submission target
→ UI state
```

`executeSubmission()` không mở cơ sở dữ liệu (database / 데이터베이스) giao dịch (transaction / 트랜잭션) trong trình duyệt (browser / 브라우저). Một Workflow chạy ba Submission liên tiếp cũng không tự làm ba HTTP lời gọi (call / 호출) thành một ACID giao dịch (transaction / 트랜잭션).

Nếu ba thao tác (operation / 연산) phải lần ghi nhận (commit / 커밋) hoặc quay lui (rollback / 롤백) cùng nhau, backend cần một giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) hoặc một nghiệp vụ (business / 비즈니스) command phù hợp.

> **Chuyển mạch:** Submission chỉ vận chuyển contract; CRUD row status cần mapping rõ sang backend operation, nhưng không thể thay thế authorization proof của server.

## 2. CRUD row status cần ánh xạ (mapping / 매핑) đặc tả hợp đồng (contract / 계약) rõ

Máy khách (client / 클라이언트) có thể giữ row `C/U/D`. máy chủ (server / 서버) phải biết ngữ nghĩa (semantics / 의미론) này bằng một đặc tả hợp đồng (contract / 계약) được thống nhất.

Có hai style phổ biến:

```text
style A: payload chứa row status + row data
style B: payload tách created/updated/deleted collections
```

Không có style luôn tốt hơn. Điều quan trọng là máy chủ (server / 서버) không “đoán” thao tác (operation / 연산) từ trường dữ liệu (field / 필드) rỗng hoặc vị trí row.

Ví dụ conceptual:

```json
{
  "created": [{"clientKey":"tmp-1","name":"A"}],
  "updated": [{"id":"U1001","version":7,"name":"B"}],
  "deleted": [{"id":"U1002","version":3}]
}
```

Đặc tả hợp đồng (contract / 계약) tách thao tác (operation / 연산) rõ và dễ validate.

> **Chuyển mạch:** CRUD mapping làm rõ operation, nhưng client row status không cấp quyền; writable-field whitelist ở boundary mới giới hạn dữ liệu server nhận.

## 3. máy khách (client / 클라이언트) row status không phải authorization proof

Người dùng (user / 사용자) có thể sửa payload trong DevTools:

```text
U → D
ROLE=USER → ROLE=ADMIN
PRICE=100 → PRICE=0
```

Máy chủ (server / 서버) phải quyết định caller có quyền create/cập nhật (update / 업데이트)/delete trường dữ liệu (field / 필드)/thực thể (entity / 엔터티) đó không. Row status chỉ là **máy khách (client / 클라이언트) intent**, không phải bằng chứng (evidence / 증거) rằng thao tác (operation / 연산) hợp lệ.

> **Chuyển mạch:** Whitelist kiểm soát field nào được ghi; canonical value tiếp theo phải được thống nhất tại API boundary, không suy ra từ hidden/readOnly trên client.

## 4. Writable-field whitelist quan trọng hơn hidden/readOnly

Một screen có thể nhận đối tượng (object / 객체) gồm 30 trường dữ liệu (field / 필드) nhưng người dùng (user / 사용자) chỉ được sửa 4 trường dữ liệu (field / 필드). Nếu máy khách (client / 클라이언트) gửi lại toàn đối tượng (object / 객체), máy chủ (server / 서버) không nên mass-assign tất cả trường dữ liệu (field / 필드).

Đặc tả hợp đồng (contract / 계약) nên phân biệt:

```text
identity fields
writable fields
server-owned fields
calculated fields
audit fields
```

Ví dụ `createdBy`, `approvedAt`, `role`, `version` có thể là server-owned tùy lĩnh vực (domain / 도메인). UI hidden/readOnly chỉ giúp UX.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **4. Writable-field whitelist quan trọng hơn hidden/readOnly** đã nêu tiêu chí phân biệt, còn **5. chuẩn gốc (canonical / 정본) giá trị (value / 값) phải được thống nhất ở API ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **6. Empty, null, absent là ba ngữ nghĩa (semantic / 의미적) khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. chuẩn gốc (canonical / 정본) giá trị (value / 값) phải được thống nhất ở API ranh giới (boundary / 경계)

UI có thể hiển thị:

```text
₩1,234,567
2026.09.22
서울
```

Payload nên dùng biểu diễn (representation / 표현) ổn định:

```text
1234567
2026-09-22 hoặc contract date đã thống nhất
SEOUL hoặc code tương ứng
```

Đừng để backend parse string display phụ thuộc locale nếu mô hình (model / 모델) đã có chuẩn gốc (canonical / 정본) giá trị (value / 값).

WebSquare binding/formatter nên giữ presentation và lĩnh vực (domain / 도메인) giá trị (value / 값) tách nhau.

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **5. chuẩn gốc (canonical / 정본) giá trị (value / 값) phải được thống nhất ở API ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **6. Empty, null, absent là ba ngữ nghĩa (semantic / 의미적) khác nhau** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **7. nghiệp vụ (business / 비즈니스) lỗi (error / 오류) nên có machine-readable mã (code / 코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Empty, null, absent là ba ngữ nghĩa (semantic / 의미적) khác nhau

Cập nhật (update / 업데이트) API cần đặc biệt rõ:

```text
field absent → không thay đổi?
field: null → xóa giá trị?
field: "" → chuỗi rỗng hợp lệ hay normalize null?
```

Nếu máy khách (client / 클라이언트) serializer tự chuyển đổi theo DataList/DataMap cấu hình (config / 설정), kiểm thử (test / 테스트) đặc tả hợp đồng (contract / 계약) phải kiểm tra payload thực tế trong mạng (network / 네트워크). Không chỉ nhìn JavaScript đối tượng (object / 객체) trước submit.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **7. nghiệp vụ (business / 비즈니스) lỗi (error / 오류) nên có machine-readable mã (code / 코드)** tiếp nhận điểm tựa từ **6. Empty, null, absent là ba ngữ nghĩa (semantic / 의미적) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. vận chuyển (transport / 전송) success, ứng dụng (application / 애플리케이션) success và giao dịch (transaction / 트랜잭션) success** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. nghiệp vụ (business / 비즈니스) lỗi (error / 오류) nên có machine-readable mã (code / 코드)

Phản hồi (response / 응답) chỉ trả message Korean như:

```text
"이미 처리된 데이터입니다."
```

khó cho máy khách (client / 클라이언트) ánh xạ (mapping / 매핑) hành vi (behavior / 동작) và i18n.

Tốt hơn:

```json
{
  "success": false,
  "code": "ALREADY_PROCESSED",
  "message": "이미 처리된 데이터입니다.",
  "details": {}
}
```

Máy khách (client / 클라이언트) dùng `code` để quyết định hành vi (behavior / 동작); `message` dùng hiển thị/log tùy chính sách (policy / 정책). Nếu frontend đa ngôn ngữ, có thể map mã (code / 코드) sang locale key thay vì phụ thuộc raw máy chủ (server / 서버) sentence.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **8. vận chuyển (transport / 전송) success, ứng dụng (application / 애플리케이션) success và giao dịch (transaction / 트랜잭션) success** tiếp nhận điểm tựa từ **7. nghiệp vụ (business / 비즈니스) lỗi (error / 오류) nên có machine-readable mã (code / 코드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Idempotency cho Save quan trọng khi mạng (network / 네트워크) không chắc chắn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. vận chuyển (transport / 전송) success, ứng dụng (application / 애플리케이션) success và giao dịch (transaction / 트랜잭션) success

Một phản hồi (response / 응답) HTTP 200 có thể chứa nghiệp vụ (business / 비즈니스) thất bại (failure / 실패). Một HTTP 500 có thể xảy ra sau khi giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) nhưng phản hồi (response / 응답) serialization/mạng (network / 네트워크) bị lỗi ở ranh giới (boundary / 경계) khác.

Do đó máy khách (client / 클라이언트) cần phân biệt:

```text
request reached server?
server understood request?
business command accepted?
transaction committed?
response reached client?
```

Trong hết thời gian chờ (timeout / 타임아웃)/mạng (network / 네트워크) mất mát (loss / 손실), máy khách (client / 클라이언트) đôi lúc **không biết** giao dịch (transaction / 트랜잭션) đã lần ghi nhận (commit / 커밋) hay chưa. Đây là lý do mutation thử lại (retry / 재시도) cần idempotency.

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **9. Idempotency cho Save quan trọng khi mạng (network / 네트워크) không chắc chắn** tiếp nhận điểm tựa từ **8. vận chuyển (transport / 전송) success, ứng dụng (application / 애플리케이션) success và giao dịch (transaction / 트랜잭션) success** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Optimistic locking là đặc tả hợp đồng (contract / 계약) giữa UI và cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Idempotency cho Save quan trọng khi mạng (network / 네트워크) không chắc chắn

Scenario:

```text
client gửi Create Payment
server commit thành công
response bị mất
client timeout
user bấm Save lại
```

Nếu máy chủ (server / 서버) tạo giao dịch (transaction / 트랜잭션) mới mỗi lần, duplicate có thể xảy ra.

Một idempotency/nghiệp vụ (business / 비즈니스) yêu cầu (request / 요청) key giúp máy chủ (server / 서버) nhận ra thử lại (retry / 재시도) của cùng logical command. Cách implement thuộc backend/lĩnh vực (domain / 도메인), nhưng WebSquare máy khách (client / 클라이언트) cần biết khi nào tạo/giữ key.

Quy tắc (rule / 규칙): thử lại (retry / 재시도) truy vấn (query / 쿼리) thường dễ hơn thử lại (retry / 재시도) mutation. Không auto-retry Save chỉ vì `submiterror` chạy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **9. Idempotency cho Save quan trọng khi mạng (network / 네트워크) không chắc chắn** nêu điều cần giải thích; **10. Optimistic locking là đặc tả hợp đồng (contract / 계약) giữa UI và cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **11. xung đột (conflict / 충돌) khác kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Optimistic locking là đặc tả hợp đồng (contract / 계약) giữa UI và cơ sở dữ liệu (database / 데이터베이스)

Máy khách (client / 클라이언트) đọc thực thể (entity / 엔터티) phiên bản (version / 버전) 7. Khi save:

```json
{
  "id": "ORD-1001",
  "version": 7,
  "status": "APPROVED"
}
```

Máy chủ (server / 서버) cập nhật (update / 업데이트) với expectation phiên bản (version / 버전) 7. Nếu phiên bản (version / 버전) hiện đã là 8, máy chủ (server / 서버) trả xung đột (conflict / 충돌).

Máy khách (client / 클라이언트) không nên silently overwrite. UX có thể:

```text
reload canonical server state
show conflict message
show diff nếu domain cần
cho user re-apply change
```

Row status `U` chỉ nói máy khách (client / 클라이언트) đã sửa; nó không nói máy chủ (server / 서버) row vẫn như lúc máy khách (client / 클라이언트) đọc.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **10. Optimistic locking là đặc tả hợp đồng (contract / 계약) giữa UI và cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **11. xung đột (conflict / 충돌) khác kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **12. All-or-nothing batch giao dịch (transaction / 트랜잭션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. xung đột (conflict / 충돌) khác kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패)

Kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패) nghĩa đầu vào (input / 입력) vi phạm quy tắc (rule / 규칙). xung đột (conflict / 충돌) nghĩa đầu vào (input / 입력) có thể hợp lệ nhưng trạng thái (state / 상태) nền đã thay đổi.

```text
INVALID_EMAIL → sửa email
VERSION_CONFLICT → reload/compare state
ALREADY_APPROVED → operation state đã chuyển
PERMISSION_DENIED → authorization
```

Nếu mọi lỗi đều hiện “저장 실패”, người dùng (user / 사용자) không biết hành động tiếp theo.

Lỗi (error / 오류) taxonomy là một phần của Đặc tả API (API contract / API 계약).

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **12. All-or-nothing batch giao dịch (transaction / 트랜잭션)** tiếp nhận điểm tựa từ **11. xung đột (conflict / 충돌) khác kiểm tra hợp lệ (validation / 검증) thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Partial success cần giao thức (protocol / 프로토콜) mạnh hơn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. All-or-nothing batch giao dịch (transaction / 트랜잭션)

Với 100 row save, backend có thể chọn một giao dịch (transaction / 트랜잭션):

```text
validate all
→ apply all
→ commit all
```

Một row thất bại (fail / 실패) thì quay lui (rollback / 롤백) tất cả. máy khách (client / 클라이언트) giữ toàn bộ changed rows dirty và highlight lỗi gây quay lui (rollback / 롤백).

Ưu điểm là bất biến (invariant / 불변식) toàn batch dễ giữ. Nhược điểm là một row lỗi chặn 99 row đúng.

UI phải nói rõ “không row nào được lưu” thay vì đánh dấu success từng row trước khi giao dịch (transaction / 트랜잭션) kết quả (result / 결과) cuối cùng có.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **13. Partial success cần giao thức (protocol / 프로토콜) mạnh hơn** tiếp nhận điểm tựa từ **12. All-or-nothing batch giao dịch (transaction / 트랜잭션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Created row cần máy khách (client / 클라이언트) correlation key** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Partial success cần giao thức (protocol / 프로토콜) mạnh hơn

Nếu backend cho phép row độc lập lần ghi nhận (commit / 커밋), phản hồi (response / 응답) phải nói row nào thành công/thất bại bằng stable key.

```json
{
  "results": [
    {"id":"A","status":"SUCCESS","version":8},
    {"id":"B","status":"ERROR","code":"DUPLICATE"}
  ]
}
```

Máy khách (client / 클라이언트) chỉ reset dirty trạng thái (state / 상태) cho row A; row B giữ edit/lỗi (error / 오류). Nếu máy khách (client / 클라이언트) reset toàn DataList sau HTTP 200, người dùng (user / 사용자) mất unsaved correction.

Partial success là phân tán (distributed / 분산) trạng thái (state / 상태) reconciliation bài toán (problem / 문제), không chỉ là “vòng lặp (loop / 루프) alert”.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **14. Created row cần máy khách (client / 클라이언트) correlation key** tiếp nhận điểm tựa từ **13. Partial success cần giao thức (protocol / 프로토콜) mạnh hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Delete cần phiên bản (version / 버전) và quyền sở hữu (ownership / 소유권) như cập nhật (update / 업데이트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Created row cần máy khách (client / 클라이언트) correlation key

Row mới chưa có máy chủ (server / 서버) ID. Nếu batch create 10 row và máy chủ (server / 서버) sinh chuỗi (sequence / 시퀀스), phản hồi (response / 응답) cần map ID về đúng máy khách (client / 클라이언트) row.

Có thể dùng temporary máy khách (client / 클라이언트) key:

```json
{"clientKey":"tmp-7","name":"Kim"}
```

Phản hồi (response / 응답):

```json
{"clientKey":"tmp-7","id":"USR-10442","status":"SUCCESS"}
```

Không map bằng array chỉ mục (index / 인덱스) nếu máy chủ (server / 서버) có thể reorder kết quả (result / 결과) hoặc partial thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, sau nội dung của **14. Created row cần máy khách (client / 클라이언트) correlation key**, **15. Delete cần phiên bản (version / 버전) và quyền sở hữu (ownership / 소유권) như cập nhật (update / 업데이트)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **16. tìm kiếm (search / 검색) đặc tả hợp đồng (contract / 계약) phải snapshot điều kiện đã execute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Delete cần phiên bản (version / 버전) và quyền sở hữu (ownership / 소유권) như cập nhật (update / 업데이트)

Delete không chỉ là `DELETE WHERE ID=?`. Nếu bản ghi (record / 레코드) đã đổi hoặc không còn thuộc quyền người dùng (user / 사용자), máy chủ (server / 서버) phải enforce quy tắc (rule / 규칙).

Máy khách (client / 클라이언트) gửi định danh (identity / 식별자)/phiên bản (version / 버전) cần thiết; máy chủ (server / 서버) xác thực permission/bất biến (invariant / 불변식). Nếu delete xung đột (conflict / 충돌), UI không nên đơn giản remove row cục bộ (local / 로컬) rồi coi như xong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **16. tìm kiếm (search / 검색) đặc tả hợp đồng (contract / 계약) phải snapshot điều kiện đã execute** tiếp nhận điểm tựa từ **15. Delete cần phiên bản (version / 버전) và quyền sở hữu (ownership / 소유권) như cập nhật (update / 업데이트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Latest-intent guard cần máy chủ (server / 서버)/máy khách (client / 클라이언트) cooperation khi có side tác động (effect / 효과)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. tìm kiếm (search / 검색) đặc tả hợp đồng (contract / 계약) phải snapshot điều kiện đã execute

Người dùng (user / 사용자) có thể sửa `dmSearch` sau khi yêu cầu (request / 요청) bắt đầu. phản hồi (response / 응답) A tương ứng điều kiện (condition / 조건) A, trong khi UI đầu vào (input / 입력) đã là B.

Nên giữ yêu cầu (request / 요청) định danh (identity / 식별자) và snapshot:

```javascript
scwin.lastExecutedSearch = {
    requestId: requestId,
    condition: /* clone plain data */
};
```

Khi export/report hoặc gỡ lỗi (debug / 디버그), biết dataset hiện tại sinh từ truy vấn (query / 쿼리) nào. Điều này cũng hỗ trợ stale-response guard.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **17. Latest-intent guard cần máy chủ (server / 서버)/máy khách (client / 클라이언트) cooperation khi có side tác động (effect / 효과)** tiếp nhận điểm tựa từ **16. tìm kiếm (search / 검색) đặc tả hợp đồng (contract / 계약) phải snapshot điều kiện đã execute** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Workflow phù hợp orchestration đọc hơn giao dịch (transaction / 트랜잭션) mutation phức tạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Latest-intent guard cần máy chủ (server / 서버)/máy khách (client / 클라이언트) cooperation khi có side tác động (effect / 효과)

Tìm kiếm (search / 검색) phản hồi (response / 응답) cũ có thể bỏ qua ở máy khách (client / 클라이언트). Save phản hồi (response / 응답) cũ thì phức tạp hơn vì máy chủ (server / 서버) side tác động (effect / 효과) có thể đã xảy ra.

Do đó:

```text
read request → cancellation/latest-response policy thường đủ
mutation → cần duplicate guard/idempotency/concurrency contract
```

Đừng áp cùng một “ignore stale phản hồi (response / 응답)” mẫu (pattern / 패턴) cho mọi thao tác (operation / 연산).

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **17. Latest-intent guard cần máy chủ (server / 서버)/máy khách (client / 클라이언트) cooperation khi có side tác động (effect / 효과)** xác định đầu vào; **18. Workflow phù hợp orchestration đọc hơn giao dịch (transaction / 트랜잭션) mutation phức tạp** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **19. tệp (file / 파일)/Excel import cần staging mindset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Workflow phù hợp orchestration đọc hơn giao dịch (transaction / 트랜잭션) mutation phức tạp

WebSquare Workflow có thể mô tả thứ tự nhiều Submission và official guide khuyến nghị dùng cho luồng (flow / 흐름) truy vấn (query / 쿼리)/select phù hợp. Nhưng nếu Save A rồi Save B phải atomic, hai Submission nối bằng Workflow vẫn không tạo máy chủ (server / 서버) giao dịch (transaction / 트랜잭션) chung.

Tốt hơn có thể là một backend command duy nhất nếu bất biến (invariant / 불변식) yêu cầu atomicity.

First principle: **giao dịch (transaction / 트랜잭션) ranh giới (boundary / 경계) phải nằm nơi có quyền kiểm soát tài nguyên (resource / 자원) cần lần ghi nhận (commit / 커밋)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **18. Workflow phù hợp orchestration đọc hơn giao dịch (transaction / 트랜잭션) mutation phức tạp** xác định đầu vào; **19. tệp (file / 파일)/Excel import cần staging mindset** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **20. Long-running thao tác (operation / 연산) cần job ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. tệp (file / 파일)/Excel import cần staging mindset

Excel 10.000 row không nên đi thẳng từ upload thành lần ghi nhận (commit / 커밋) nếu lĩnh vực (domain / 도메인) phức tạp.

Một chuỗi xử lý (pipeline / 파이프라인) an toàn hơn:

```text
parse
→ normalize
→ client preview
→ server validate
→ return row-level errors
→ user correct/confirm
→ commit command
```

Với dataset lớn, server-side staging/import job có thể phù hợp hơn giữ mọi row trong trình duyệt (browser / 브라우저). WebSquare Grid là UI cho tiến trình (process / 프로세스), không nhất thiết là nơi xử lý toàn bộ import.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **20. Long-running thao tác (operation / 연산) cần job ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **19. tệp (file / 파일)/Excel import cần staging mindset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Session expiration là giao thức (protocol / 프로토콜) sự kiện (event / 이벤트), không chỉ generic lỗi (error / 오류)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Long-running thao tác (operation / 연산) cần job ngữ nghĩa (semantics / 의미론)

Một report/export/import mất 2 phút không nên giả định HTTP yêu cầu (request / 요청) giữ UI blocking là tốt nhất.

Backend có thể dùng async job:

```text
POST create job
→ jobId
→ poll/status/subscription
→ completed/failed
→ download/result
```

Máy khách (client / 클라이언트) cần máy trạng thái (state machine / 상태 머신):

```text
IDLE → SUBMITTED → RUNNING → SUCCEEDED/FAILED/CANCELLED
```

Đừng dùng một boolean `isLoading` cho workflow nhiều trạng thái.

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **21. Session expiration là giao thức (protocol / 프로토콜) sự kiện (event / 이벤트), không chỉ generic lỗi (error / 오류)** tiếp nhận điểm tựa từ **20. Long-running thao tác (operation / 연산) cần job ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Correlation ID nối frontend sự cố (incident / 인시던트) với backend dấu vết (trace / 추적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Session expiration là giao thức (protocol / 프로토콜) sự kiện (event / 이벤트), không chỉ generic lỗi (error / 오류)

Nếu session hết hạn, nhiều Submission có thể đồng thời nhận 401/403 hoặc phản hồi (response / 응답) convention riêng. dùng chung (common / 공통) tầng (layer / 계층) cần chính sách (policy / 정책) tránh 10 popup “session expired”.

Ứng dụng (application / 애플리케이션) shell có thể coordinate:

```text
first auth-expired signal
→ freeze new protected actions
→ show one re-auth/login flow
→ pending operation policy
```

Nhưng backend status ngữ nghĩa (semantics / 의미론) phải rõ. Không map mọi 403 thành session expired vì 403 cũng có thể là permission denial.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **22. Correlation ID nối frontend sự cố (incident / 인시던트) với backend dấu vết (trace / 추적)** tiếp nhận điểm tựa từ **21. Session expiration là giao thức (protocol / 프로토콜) sự kiện (event / 이벤트), không chỉ generic lỗi (error / 오류)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. đặc tả hợp đồng (contract / 계약) versioning và backward tính tương thích (compatibility / 호환성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Correlation ID nối frontend sự cố (incident / 인시던트) với backend dấu vết (trace / 추적)

Máy khách (client / 클라이언트) log:

```text
screen=ORDER_DETAIL
operation=SAVE
requestId=abc-123
orderId=ORD-1001
```

Máy chủ (server / 서버)/gateway log cùng correlation/dấu vết (trace / 추적) ID giúp tìm giao dịch (transaction / 트랜잭션). Không log full payload nếu chứa PII.

Môi trường vận hành (production / 운영 환경) hỗ trợ (support / 지원) tốt cần đủ ngữ cảnh (context / 맥락) để trả lời: yêu cầu (request / 요청) nào, screen instance nào, nghiệp vụ (business / 비즈니스) thực thể (entity / 엔터티) nào, bản dựng (build / 빌드) nào.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **23. đặc tả hợp đồng (contract / 계약) versioning và backward tính tương thích (compatibility / 호환성)** tiếp nhận điểm tựa từ **22. Correlation ID nối frontend sự cố (incident / 인시던트) với backend dấu vết (trace / 추적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Client-generated nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dễ drift** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. đặc tả hợp đồng (contract / 계약) versioning và backward tính tương thích (compatibility / 호환성)

Frontend sản phẩm tạo ra (artifact / 산출물) và backend bản phát hành (release / 릴리스) có thể deploy lệch thời điểm. Nếu Đặc tả API (API contract / API 계약) thay breaking ngay, rolling triển khai (deployment / 배포)/bộ nhớ đệm (cache / 캐시) cũ có thể lỗi.

Cần chính sách (policy / 정책):

```text
additive field change
optional field/default
versioned endpoint/schema nếu cần
compatibility window
```

WebSquare W-Pack bộ nhớ đệm (cache / 캐시) làm khả năng máy khách (client / 클라이언트) cũ sống lâu hơn đáng kể. Backend nên tính đến stale máy khách (client / 클라이언트) trong triển khai (deployment / 배포) chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **24. Client-generated nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dễ drift** tiếp nhận điểm tựa từ **23. đặc tả hợp đồng (contract / 계약) versioning và backward tính tương thích (compatibility / 호환성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) quan trọng hơn screenshot kiểm thử (test / 테스트) cho tích hợp (integration / 통합)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Client-generated nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dễ drift

Nếu cùng quy tắc (rule / 규칙) được bản sao (copy / 복사) ở 20 screen và backend, sớm muộn sẽ lệch.

Máy khách (client / 클라이언트) có thể duplicate một subset để UX nhanh, nhưng máy chủ (server / 서버) vẫn là đơn vị sở hữu (owner / 오너) bất biến (invariant / 불변식). Khi quy tắc (rule / 규칙) thay đổi, cần centralize siêu dữ liệu (metadata / 메타데이터)/dùng chung (common / 공통) hàm (function / 함수) hoặc trả ràng buộc (constraint / 제약조건) từ máy chủ (server / 서버) nếu phù hợp.

Không nên đưa toàn nghiệp vụ (business / 비즈니스) engine xuống trình duyệt (browser / 브라우저) chỉ để tránh yêu cầu (request / 요청).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **25. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) quan trọng hơn screenshot kiểm thử (test / 테스트) cho tích hợp (integration / 통합)** tiếp nhận điểm tựa từ **24. Client-generated nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙) dễ drift** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. trường hợp (case / 사례) study: batch approval có xung đột (conflict / 충돌)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) quan trọng hơn screenshot kiểm thử (test / 테스트) cho tích hợp (integration / 통합)

Một regression suite nên chứng minh:

```text
C/U/D serialize đúng
null/empty semantics đúng
business error code map đúng
version conflict không reset dirty state
partial success reconcile đúng row
created clientKey map đúng server ID
timeout không auto-duplicate mutation
401/403 đi đúng auth/permission path
```

Screenshot không chứng minh các bất biến (invariant / 불변식) này.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **25. đặc tả hợp đồng (contract / 계약) kiểm thử (test / 테스트) quan trọng hơn screenshot kiểm thử (test / 테스트) cho tích hợp (integration / 통합)** cho ta quy tắc; **26. trường hợp (case / 사례) study: batch approval có xung đột (conflict / 충돌)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **27. ranh giới (boundary / 경계) với chuẩn gốc (canonical / 정본) backend docs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. trường hợp (case / 사례) study: batch approval có xung đột (conflict / 충돌)

Người dùng (user / 사용자) tìm kiếm (search / 검색) 200 yêu cầu (request / 요청), chọn 20 row và bấm Approve. máy khách (client / 클라이언트) snapshot `REQUEST_ID + VERSION`. máy chủ (server / 서버) nhận batch command.

Trong lúc người dùng (user / 사용자) thao tác, 2 row đã được người khác approve. máy chủ (server / 서버) có thể chọn all-or-nothing hoặc partial chính sách (policy / 정책). Nếu all-or-nothing, phản hồi (response / 응답) trả xung đột (conflict / 충돌) danh sách (list / 목록) và không lần ghi nhận (commit / 커밋) row nào. máy khách (client / 클라이언트) giữ 20 row unchanged/dirty theo workflow và yêu cầu refresh. Nếu partial, 18 row success được normalize/reset; 2 row xung đột (conflict / 충돌) giữ lỗi (error / 오류) trạng thái (state / 상태) và hiển thị chuẩn gốc (canonical / 정본) máy chủ (server / 서버) status.

Điểm quyết định không nằm ở Grid API. Nó nằm ở giao dịch (transaction / 트랜잭션) đặc tả hợp đồng (contract / 계약). Grid chỉ phản ánh kết quả (result / 결과).

> **Chuyển mạch:** Ở chặng này của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, trường hợp ở **26. trường hợp (case / 사례) study: batch approval có xung đột (conflict / 충돌)** cho thấy quy tắc hoạt động; **27. ranh giới (boundary / 경계) với chuẩn gốc (canonical / 정본) backend docs** kiểm tra nơi quy tắc ấy không còn áp dụng hoặc dễ bị hiểu nhầm. Từ đây, **28. Master checklist cho máy khách (client / 클라이언트)–máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. ranh giới (boundary / 경계) với chuẩn gốc (canonical / 정본) backend docs

Chi tiết Spring giao dịch (transaction / 트랜잭션) propagation, controller/dịch vụ (service / 서비스) kiến trúc (architecture / 아키텍처), cơ sở dữ liệu (database / 데이터베이스) isolation mức (level / 수준), SQL locking, authentication khung phần mềm (framework / 프레임워크) và API thiết kế (design / 설계) tổng quát thuộc chuẩn gốc (canonical / 정본) `10_backend/` và Khoa học máy tính (computer science / 컴퓨터 과학)/cơ sở dữ liệu (database / 데이터베이스) docs của repository.

WebSquare chapter này chỉ giữ phần giao nhau cần cho frontend lập luận (reasoning / 추론). Khi cần hiểu vì sao optimistic locking hoạt động ở SQL/JPA/MyBatis hoặc giao dịch (transaction / 트랜잭션) quay lui (rollback / 롤백) xảy ra thế nào, hãy đọc backend chuẩn gốc (canonical / 정본) thay vì duplicate ở đây.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **27. ranh giới (boundary / 경계) với chuẩn gốc (canonical / 정본) backend docs** đã nêu tiêu chí phân biệt, còn **28. Master checklist cho máy khách (client / 클라이언트)–máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **29. Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Master checklist cho máy khách (client / 클라이언트)–máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약)

Trước khi productionize một Save luồng (flow / 흐름), phải trả lời được:

```text
Operation identity là gì?
Business entity identity là gì?
Writable fields là gì?
Null/empty/absent nghĩa gì?
Concurrency version nằm ở đâu?
Retry có an toàn không?
Transaction all-or-nothing hay partial?
Error code machine-readable là gì?
Created row map server ID bằng gì?
Sau success client lấy canonical state ở đâu?
Timeout thì user biết trạng thái chắc chắn hay không chắc chắn?
Server authorization kiểm tra gì dù UI đã hidden/readOnly?
```

Nếu một câu chưa có answer, đó là đặc tả hợp đồng (contract / 계약) gap chứ không phải “việc frontend/backend tự xử lý”.

> **Chuyển mạch:** Trong **15 — Backend đặc tả hợp đồng (contract / 계약), giao dịch (transaction / 트랜잭션) & tính đồng thời (concurrency / 동시성) tích hợp (integration / 통합)**, **29. Kết nối** tiếp nhận điểm tựa từ **28. Master checklist cho máy khách (client / 클라이언트)–máy chủ (server / 서버) đặc tả hợp đồng (contract / 계약)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## 29. Kết nối

Ba chapter 13–15 đi từ định danh (identity / 식별자) của row → định danh (identity / 식별자) của screen instance → định danh (identity / 식별자) của giao dịch (transaction / 트랜잭션)/yêu cầu (request / 요청). Chapter cuối tổng hợp các lớp này thành cách lập luận (reasoning / 추론) cấp Master: [16 — Master Production Playbook & End-to-End Case Studies](16_master_production_playbook.md).

> **Bàn giao:** Sau **29. Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
