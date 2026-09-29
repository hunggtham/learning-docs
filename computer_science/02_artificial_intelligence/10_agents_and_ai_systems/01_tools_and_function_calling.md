# Tools và hàm (function / 함수) Calling

> **Mạch đọc:** Đặt **Tools và hàm (function / 함수) Calling** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao structured tools cần tồn tại?** sang **công cụ (tool / 도구) lược đồ (schema / 스키마) là một Đặc tả API (API contract / API 계약)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


LLM sinh đơn vị từ (token / 토큰); công cụ (tool / 도구) tạo side tác động (effect / 효과). **hàm (function / 함수) calling / công cụ (tool / 도구) calling (도구 호출)** là giao thức (protocol / 프로토콜) biến intent của mô hình (model / 모델) thành structured yêu cầu (request / 요청) mà thời gian chạy (runtime / 런타임) có thể validate rồi thực thi.

Mô hình tư duy (mental model / 사고 모델):

```text
Natural-language goal
→ model chooses tool + arguments
→ runtime validates
→ tool executes
→ structured result
→ model continues reasoning
```

Mô hình (model / 모델) không trực tiếp “gọi API” theo nghĩa networking. Nó thường sinh đối tượng (object / 객체) conform lược đồ (schema / 스키마); orchestration tầng (layer / 계층) mới thực thi.

## Vì sao structured tools cần tồn tại?

Nếu yêu cầu mô hình (model / 모델) trả prose như `hãy gọi weather API với Seoul`, ứng dụng (application / 애플리케이션) phải parse văn bản (text / 텍스트) brittle. Structured lược đồ (schema / 스키마) làm ranh giới (boundary / 경계) rõ:

```json
{
  "name": "get_weather",
  "arguments": {"city": "Seoul"}
}
```

Thời gian chạy (runtime / 런타임) có thể kiểm kiểu (type / 타입), permission và required fields trước thực thi (execution / 실행).

## Công cụ (tool / 도구) lược đồ (schema / 스키마) là một Đặc tả API (API contract / API 계약)

Một công cụ (tool / 도구) tốt cần:

- tên phản ánh hành động (action / 동작);
- description nói rõ ngữ nghĩa (semantics / 의미론);
- arguments typed;
- required/optional rõ;
- enum khi lĩnh vực (domain / 도메인) hữu hạn;
- kết quả (result / 결과) cấu trúc (structure / 구조) ổn định;
- lỗi (error / 오류) taxonomy rõ.

Lược đồ (schema / 스키마) mơ hồ gây mô hình (model / 모델) lỗi (error / 오류) dù mô hình (model / 모델) mạnh.

Ví dụ `update_user(data)` quá rộng. Tốt hơn có các hành động (action / 동작) hẹp:

```text
update_shipping_address(user_id, address)
set_notification_preference(user_id, channel, enabled)
```

Hành động (action / 동작) hẹp dễ authorize, kiểm thử (test / 테스트) và kiểm tra (audit / 감사) hơn.

## Read tools và ghi (write / 쓰기) tools

Tách read-only và side-effecting tools.

```text
READ: search, fetch, inspect, query
WRITE: create, update, delete, send, deploy
```

Ghi (write / 쓰기) tools cần stricter approval, idempotency và kiểm tra (audit / 감사).

## Kiểm tra hợp lệ (validation / 검증) trước thực thi (execution / 실행)

Không tin arguments chỉ vì chúng parse được.

Kiểm tra hợp lệ (validation / 검증) layers:

```text
schema validation
→ semantic validation
→ authorization
→ policy/risk check
→ rate/budget check
→ execution
```

`amount: -1000` có thể đúng kiểu (type / 타입) number nhưng sai nghiệp vụ (business / 비즈니스) ngữ nghĩa (semantics / 의미론).

## Idempotency

Tác nhân (agent / 에이전트) thử lại (retry / 재시도) là bình thường. Với side effects, thử lại (retry / 재시도) có thể tạo duplicate email/payment/job.

Công cụ (tool / 도구) ghi (write / 쓰기) nên hỗ trợ idempotency key khi khả thi:

```text
create_payment(request_id="task-123-step-4", ...)
```

Nếu same yêu cầu (request / 요청) lặp lại, dịch vụ (service / 서비스) trả same kết quả (result / 결과) thay vì tạo hành động (action / 동작) mới.

## Công cụ (tool / 도구) kết quả (result / 결과) nên machine-readable

Tránh chỉ trả:

```text
Success
```

Tốt hơn:

```json
{
  "status": "updated",
  "resource_id": "A17",
  "version": 42,
  "changed_fields": ["email"]
}
```

Tác nhân (agent / 에이전트) cần concrete observation để cập nhật (update / 업데이트) trạng thái (state / 상태).

## Lỗi (error / 오류) taxonomy

Công cụ (tool / 도구) lỗi (error / 오류) không nên là một string chung.

Phân biệt:

```text
INVALID_ARGUMENT
NOT_FOUND
PERMISSION_DENIED
CONFLICT
RATE_LIMITED
TRANSIENT_FAILURE
TIMEOUT
```

Mỗi loại dẫn tới khôi phục (recovery / 복구) khác nhau. `TRANSIENT_FAILURE` có thể thử lại (retry / 재시도); `PERMISSION_DENIED` không nên vòng lặp (loop / 루프) thử lại (retry / 재시도).

## Hết thời gian chờ (timeout / 타임아웃) và cancellation

Công cụ (tool / 도구) lâu cần hết thời gian chờ (timeout / 타임아웃) rõ. tác nhân (agent / 에이전트) thời gian chạy (runtime / 런타임) cũng cần khả năng cancel để không để hành động (action / 동작) orphaned.

Công cụ (tool / 도구) kết quả (result / 결과) có thể ở trạng thái:

```text
PENDING → SUCCEEDED / FAILED / CANCELLED
```

Long-running tools nên trả thao tác (operation / 연산) ID rồi poll/event-driven cập nhật (update / 업데이트).

## Least Privilege

Tác nhân (agent / 에이전트) chỉ nên thấy công cụ (tool / 도구) cần cho tác vụ (task / 작업). công cụ (tool / 도구) credential cũng phải phạm vi (scope / 범위) tối thiểu.

Một tác nhân (agent / 에이전트) chỉ cần đọc invoice không nên có `delete_invoice`.

Ranh giới bảo mật (security boundary / 보안 경계) nên nằm ngoài prompt. “Đừng xóa dữ liệu” trong hệ thống (system / 시스템) prompt không mạnh bằng không expose delete permission.

## Công cụ (tool / 도구) selection

Mô hình (model / 모델) phải quyết định không chỉ arguments mà cả **có cần công cụ (tool / 도구) không**.

Thất bại (failure / 실패) modes:

- hallucinate công cụ (tool / 도구) không tồn tại;
- dùng công cụ (tool / 도구) không cần thiết;
- chọn công cụ (tool / 도구) gần nghĩa nhưng sai ngữ nghĩa (semantics / 의미론);
- gọi nhiều công cụ (tool / 도구) redundant;
- không gọi công cụ (tool / 도구) khi factual grounding cần thiết.

Công cụ (tool / 도구) descriptions và examples ảnh hưởng routing hành vi (behavior / 동작).

## Parallel công cụ (tool / 도구) calls

Independent read operations có thể chạy song song:

```text
search CRM ─┐
search docs ├─→ combine
search logs ─┘
```

Nhưng ghi (write / 쓰기) actions có phụ thuộc (dependency / 의존성) cần serialize.

Parallelism giảm độ trễ (latency / 지연 시간) nhưng tăng độ phức tạp (complexity / 복잡도) về thứ tự (ordering / 순서), errors và ngữ cảnh (context / 맥락) aggregation.

## Công cụ (tool / 도구) đầu ra (output / 출력) là untrusted đầu vào (input / 입력)

Web page, email hoặc document công cụ (tool / 도구) có thể chứa malicious instruction. Đây là **indirect prompt injection**.

Thời gian chạy (runtime / 런타임) không nên coi công cụ (tool / 도구) content là authority ngang hệ thống (system / 시스템) chính sách (policy / 정책).

Mental separation:

```text
instructions from trusted policy
≠
data returned by tool
```

## Transactions

Multi-step ghi (write / 쓰기) tác vụ (task / 작업) có consistency bài toán (problem / 문제):

```text
reserve inventory
charge payment
create shipment
```

Nếu bước 2 thất bại (fail / 실패) sau bước 1, cần quay lui (rollback / 롤백)/compensating hành động (action / 동작). tác nhân (agent / 에이전트) lập luận (reasoning / 추론) không thay thế transactional thiết kế (design / 설계).

## Công cụ (tool / 도구) lớp trừu tượng (abstraction / 추상화) mức (level / 수준)

Too low-level:

```text
http_request(method,url,body)
```

linh hoạt nhưng khó secure.

Too high-level:

```text
run_company()
```

mơ hồ, khó inspect.

Tốt nhất công cụ (tool / 도구) phản ánh meaningful nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) với đặc tả hợp đồng (contract / 계약) rõ.

## Example: cơ sở dữ liệu (database / 데이터베이스) assistant

Không nên cho mô hình (model / 모델) raw môi trường vận hành (production / 운영 환경) SQL ghi (write / 쓰기) toàn quyền. Có thể expose:

```text
find_customer(customer_id)
list_open_cases(customer_id)
create_case_note(case_id, text)
```

với authorization ở dịch vụ (service / 서비스) tầng (layer / 계층).

## Khả năng quan sát (observability / 관측 가능성)

Mỗi công cụ (tool / 도구) lời gọi (call / 호출) nên log:

```text
trace_id
agent/task id
tool name
sanitized args
result/error
latency
cost
approval event
side-effect resource/version
```

Không log secret/PII tùy tiện.

## Mô hình tư duy (mental model / 사고 모델)

> **công cụ (tool / 도구) calling là typed ranh giới (boundary / 경계) giữa probabilistic quyết định (decision / 결정) và deterministic năng lực (capability / 역량).**

LLM đề xuất; thời gian chạy (runtime / 런타임) kiểm soát; công cụ (tool / 도구) thực thi; kết quả (result / 결과) trở thành observation.

## Dùng chung (common / 공통) Misconceptions

### “JSON đúng lược đồ (schema / 스키마) nghĩa là hành động (action / 동작) đúng”

Lược đồ (schema / 스키마) chỉ kiểm shape. ngữ nghĩa (semantic / 의미적) tính đúng đắn (correctness / 정확성) và authorization vẫn phải validate.

### “Prompt đủ để bảo vệ dangerous tools”

Không. bảo mật (security / 보안) cần permission ranh giới (boundary / 경계), sandbox, approval và server-side chính sách (policy / 정책).

### “công cụ (tool / 도구) càng generic càng tốt”

Generic công cụ (tool / 도구) tăng flexibility nhưng giảm verifiability và an toàn (safety / 안전).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Công cụ (tool / 도구) calling nối [AI System Architecture](../00_foundations/04_ai_system_architecture.md) với tác nhân (agent / 에이전트) thời gian chạy (runtime / 런타임). Chapter tiếp theo mô tả vòng lặp (loop / 루프) điều phối nhiều công cụ (tool / 도구) calls qua thời gian (time / 시간).

Xem tiếp: [Agent Loop](./02_agent_loop.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from llm to agent](./00_from_llm_to_agent.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
